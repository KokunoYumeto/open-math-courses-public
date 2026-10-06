"""Run the unchanged HQ plot and 206 checks without any private inputs.

All five accompanying figure files are self-contained. Pass a new output
directory. Raw PNG bytes must match. SVG comparison preserves every byte except
Matplotlib's date and generated identifiers. Geometry must match in all fields
except the separately recorded historical visual-inspection annotation.
"""
from __future__ import annotations

from pathlib import Path
import argparse
import datetime as dt
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "an02-l110-render-and-validate.py"
SOURCE_SHA = "6DDE93B6DB4E6CCC9ADA6637B1FB8EA345F2FB6094B72B3D4150EF53CA0373A3"
EXPECTED = {
    "higher-order-q-mechanisms.png": {
        "name": "an02-l110-higher-order-q-mechanisms.png",
        "sha256": "4E01C84950FACEE7F4D020FE8EDA1F1200DB4ECABA71B57331E5A993D32FA0A0"},
    "higher-order-q-mechanisms.svg": {
        "name": "an02-l110-higher-order-q-mechanisms.svg",
        "sha256": "F6D191F99B0C54E8824B3466758FA74E1DF2804908F91D7071AC590AE7DE137C"},
    "higher-order-q-mechanisms.json": {
        "name": "an02-l110-higher-order-q-geometry.json",
        "sha256": "3B07AB32AEF3F0E24DAB8D5711959C949F91C5EEB6E2E3A0BA80740D50C385F0"},
}
INSPECTION_KEYS = (
    "visually_inspected", "visually_inspected_at_utc", "visual_inspection_findings")


def sha(data):
    return hashlib.sha256(data).hexdigest().upper()


def svg_canonical(text):
    """Retain the complete SVG while renaming IDs in definition order."""
    dates = re.findall(r"<dc:date>(.*?)</dc:date>", text)
    assert len(dates) == 1
    text = re.sub(r"<dc:date>.*?</dc:date>",
                  "<dc:date>RENDER_DATE</dc:date>", text)
    ids = re.findall(r'\bid="([^"]+)"', text)
    assert len(ids) == len(set(ids))
    mapping = {identifier: f"SVG_IDENTIFIER_{index:04d}"
               for index, identifier in enumerate(ids)}
    text = re.sub(r'\bid="([^"]+)"',
                  lambda match: f'id="{mapping[match[1]]}"', text)
    text = re.sub(r'(?<=#)([A-Za-z_][A-Za-z_0-9:.-]*)',
                  lambda match: mapping.get(match[1], match[1]), text)
    return text, dates[0], ids


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", required=True, type=Path,
                        help="A directory that does not yet exist.")
    args = parser.parse_args()
    output = args.output_dir.resolve()
    if output.exists():
        raise SystemExit("Choose a new output directory; existing outputs are never overwritten.")
    assert SOURCE.is_file() and sha(SOURCE.read_bytes()) == SOURCE_SHA
    originals = {}
    for name, row in EXPECTED.items():
        data = (HERE / row["name"]).read_bytes()
        assert sha(data) == row["sha256"], row["name"]
        originals[name] = data
    dependency_versions = {}
    for package in ("numpy", "sympy", "matplotlib"):
        module = __import__(package)
        dependency_versions[package] = module.__version__
    with tempfile.TemporaryDirectory(prefix="an02-l110-independent-reproduction-") as temp:
        scratch = Path(temp)
        script = scratch / "render_and_validate.py"
        shutil.copyfile(SOURCE, script)
        process = subprocess.run([sys.executable, str(script)], cwd=scratch,
                                 check=True, capture_output=True, text=True)
        checks = json.loads((scratch / "validation.json").read_text(encoding="utf-8"))
        assert checks["status"] == "passed" and checks["check_count"] == 206
        assert len(checks["checks"]) == 206
        assert all(check["passed"] is True for check in checks["checks"])
        generated = {name: (scratch / "figures" / name).read_bytes()
                     for name in EXPECTED}
        assert generated["higher-order-q-mechanisms.png"] == originals["higher-order-q-mechanisms.png"]
        fresh_svg, fresh_date, fresh_ids = svg_canonical(
            generated["higher-order-q-mechanisms.svg"].decode("utf-8"))
        old_svg, old_date, old_ids = svg_canonical(
            originals["higher-order-q-mechanisms.svg"].decode("utf-8"))
        assert fresh_svg == old_svg, "SVG differs beyond its date and generated IDs."
        assert len(fresh_ids) == len(old_ids)
        # Restore only those volatile fields to the original byte representation.
        replacement_ids = dict(zip(fresh_ids, old_ids))
        restored_svg = generated["higher-order-q-mechanisms.svg"].decode("utf-8")
        restored_svg = re.sub(r'\bid="([^"]+)"',
                             lambda match: f'id="{replacement_ids[match[1]]}"',
                             restored_svg)
        restored_svg = re.sub(r'(?<=#)([A-Za-z_][A-Za-z_0-9:.-]*)',
                             lambda match: replacement_ids.get(match[1], match[1]),
                             restored_svg)
        restored_svg = restored_svg.replace(
            "<dc:date>" + fresh_date + "</dc:date>",
            "<dc:date>" + old_date + "</dc:date>").encode("utf-8")
        assert restored_svg == originals["higher-order-q-mechanisms.svg"]
        fresh_geometry = json.loads(generated["higher-order-q-mechanisms.json"])
        old_geometry = json.loads(originals["higher-order-q-mechanisms.json"])
        for key in INSPECTION_KEYS:
            fresh_geometry.pop(key, None)
        geometric_reference = dict(old_geometry)
        for key in INSPECTION_KEYS:
            geometric_reference.pop(key, None)
        assert fresh_geometry == geometric_reference
        # The original geometry metadata includes a historical visual inspection
        # annotation. It is preserved, not claimed as newly executed by this run.
        for key in INSPECTION_KEYS:
            if key in old_geometry:
                fresh_geometry[key] = old_geometry[key]
        fresh_geometry = {key: fresh_geometry[key] for key in old_geometry}
        original_geometry_newline = "\r\n" if b"\r\n" in originals["higher-order-q-mechanisms.json"] else "\n"
        restored_geometry = (json.dumps(fresh_geometry, ensure_ascii=False, indent=2) + "\n").replace(
            "\n", original_geometry_newline).encode("utf-8")
        assert restored_geometry == originals["higher-order-q-mechanisms.json"]
        output.mkdir(parents=True)
        final = {
            "higher-order-q-mechanisms.png": generated["higher-order-q-mechanisms.png"],
            "higher-order-q-mechanisms.svg": restored_svg,
            "higher-order-q-mechanisms.json": restored_geometry,
        }
        for name, data in final.items():
            assert sha(data) == EXPECTED[name]["sha256"]
            (output / EXPECTED[name]["name"]).write_bytes(data)
        (output / "independent-bounded-checks.json").write_bytes(
            (scratch / "validation.json").read_bytes())
        (output / "fresh-unnormalized-higher-order-q-mechanisms.svg").write_bytes(
            generated["higher-order-q-mechanisms.svg"])
        (output / "fresh-unannotated-higher-order-q-geometry.json").write_bytes(
            generated["higher-order-q-mechanisms.json"])
        receipt = {
            "schema": "AN02-L110-isolated-figure-and-check-reproduction/v1",
            "reproduced_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
            "python": sys.version,
            "dependency_versions": dependency_versions,
            "unchanged_renderer_sha256": SOURCE_SHA,
            "reproduction_wrapper_sha256": sha(Path(__file__).read_bytes()),
            "all206_bounded_checks_passed": True,
            "PNG_raw_bytes_exact": True,
            "geometry_raw_bytes_exact": True,
            "geometry_raw_generator_bytes_exact": generated["higher-order-q-mechanisms.json"] == originals["higher-order-q-mechanisms.json"],
            "geometry_all_mathematical_fields_regenerated_exact": True,
            "historical_visual_inspection_annotation_preserved": True,
            "geometry_original_UTF8_and_line_ending_serialization_preserved": True,
            "SVG_after_only_volatile_fields_normalized_bytes_exact": True,
            "SVG_raw_generator_bytes_exact": generated["higher-order-q-mechanisms.svg"] == originals["higher-order-q-mechanisms.svg"],
            "SVG_only_normalized_fields": {
                "generated_date": fresh_date, "original_date": old_date,
                "identifiers": [{"generated": fresh, "original": old}
                                for fresh, old in zip(fresh_ids, old_ids)
                                if fresh != old],
            },
            "SVG_complete_normalized_document_sha256": sha(fresh_svg.encode("utf-8")),
            "named_outputs": EXPECTED,
            "raw_generated_outputs_retained": [
                "fresh-unnormalized-higher-order-q-mechanisms.svg",
                "fresh-unannotated-higher-order-q-geometry.json"],
            "no_private_input_files_required_or_read": True,
            "renderer_stdout": process.stdout.strip(),
            "limits": "Exact identities and bounded samples supplement the proof. Global bounds, support and all jets are proved in the written argument. No new visual inspection or independent proof review is claimed by this wrapper.",
        }
        (output / "reproduction.json").write_text(
            json.dumps(receipt, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8", newline="\n")
    print(json.dumps({"passed": True, "checks": 206, "output_dir": str(output),
                      "exact_named_PNG_SVG_geometry_bytes": True}))


if __name__ == "__main__":
    main()
