"""Reproduce the exact CH figure from five public, self-contained files."""
from pathlib import Path
import argparse
import datetime as dt
import hashlib
import json
import math
import re
import shutil
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "an02-l111-make-figures.py"
SOURCE_SHA = "E940FAFE73A67CDF9F6F30CDF95C6A163FAFC161DA685E1F6386FDD5AE15AE8E"
EXPECTED = {
    "characteristic-halfspace-contours.png": ("an02-l111-characteristic-halfspace-contours.png", "5D84180001F7D3BC4BE05DE8EF8211DAEAD0CCAE611C12B2665A77262AC50830"),
    "characteristic-halfspace-contours.svg": ("an02-l111-characteristic-halfspace-contours.svg", "2CECC2001E23AE3B7094FCCBF98580B223F09087DC919866E30D7D3324F3D7B0"),
    "geometry.json": ("an02-l111-characteristic-halfspace-geometry.json", "AACF38278536868A00952A5F1B2633E677A356930ACC013DFDDFBA2BA664A411"),
}


def sha(data):
    return hashlib.sha256(data).hexdigest().upper()


def canonical_svg(text):
    dates = re.findall(r"<dc:date>(.*?)</dc:date>", text)
    assert len(dates) == 1, "Expected exactly one SVG rendering date."
    text = re.sub(r"<dc:date>.*?</dc:date>", "<dc:date>RENDER_DATE</dc:date>", text)
    identifiers = re.findall(r'\bid="([^"]+)"', text)
    assert len(identifiers) == len(set(identifiers)), "SVG identifiers must be unique."
    mapping = {identifier: f"SVG_IDENTIFIER_{index:04d}" for index, identifier in enumerate(identifiers)}
    text = re.sub(r'\bid="([^"]+)"', lambda match: f'id="{mapping[match[1]]}"', text)
    text = re.sub(r'(?<=#)([A-Za-z_][A-Za-z_0-9:.-]*)', lambda match: mapping.get(match[1], match[1]), text)
    return text, dates[0], identifiers


def check_geometry(g):
    checks = []

    def check(name, passed):
        assert passed, name
        checks.append({"name": name, "passed": True})

    R, c, T = g["R"], g["c"], g["T"]
    alpha, beta, theta = g["alpha"], g["beta"], g["theta0"]
    close = lambda x, y: math.isclose(x, y, rel_tol=1e-12, abs_tol=1e-12)
    check("drawing dimensions R<c<T", 0 < R < c < T)
    check("strict exponent ordering", 0 <= alpha < beta < 1)
    check("allowed split angle", math.pi/2 < theta < min(math.pi, math.pi/(2*beta)))
    check("phi_T exact formula", close(g["phi_T"], math.acos(c/T)))
    check("psi_T exact formula", close(g["psi_T"], math.pi-math.asin(R/T)))
    check("split within outer arcs", g["phi_T"] < theta < g["psi_T"])
    check("positive exact k0", g["k0"] > 0 and close(g["k0"], math.cos(beta*theta)))
    check("positive exact b0", g["b0"] > 0 and close(g["b0"], -math.cos(theta)))
    for index, (x, y) in enumerate(g["vertical_endpoints"]):
        check(f"vertical endpoint {index}: exact circle intersection", close(x, c) and close(x*x+y*y, T*T))
        check(f"vertical endpoint {index}: correct side", y < 0 if index == 0 else y > 0)
    for index, (x, y) in enumerate(g["left_ray_endpoints"]):
        check(f"left-ray endpoint {index}: exact circle intersection", x < 0 and close(abs(y), R) and close(x*x+y*y, T*T))
        check(f"left-ray endpoint {index}: correct side", y < 0 if index == 0 else y > 0)
    check("exact contour orientations", g["equations"] == [
        "vertical Re w=c upward", "lower ray w=-t-iR, t from infinity to 0",
        "right semicircle w=R exp(i theta), -pi/2 to pi/2",
        "upper ray w=-t+iR, t from 0 to infinity"])
    check("schematic interpretation retained", g["interpretation"] == "Illustrative parameters; exact contour equations and proof locators.")
    return checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", required=True, type=Path, help="A directory that does not yet exist.")
    args = parser.parse_args()
    output = args.output_dir.resolve()
    if output.exists():
        raise SystemExit("Choose a new output directory; existing outputs are never overwritten.")
    assert sha(SOURCE.read_bytes()) == SOURCE_SHA, "Rendering source differs from the supplied original."
    originals = {}
    for name, (renamed, expected) in EXPECTED.items():
        originals[name] = (HERE / renamed).read_bytes()
        assert sha(originals[name]) == expected, f"Supplied original changed: {renamed}"
    versions = {"python": sys.version}
    for package in ("numpy", "matplotlib"):
        versions[package] = __import__(package).__version__
    with tempfile.TemporaryDirectory(prefix="an02-l111-standalone-render-") as temp:
        scratch = Path(temp)
        renderer = scratch / "make_figures.py"
        shutil.copyfile(SOURCE, renderer)
        process = subprocess.run([sys.executable, str(renderer)], cwd=scratch, check=True,
                                 capture_output=True, text=True, timeout=120)
        generated = {name: (scratch / name).read_bytes() for name in EXPECTED}
        assert generated["characteristic-halfspace-contours.png"] == originals["characteristic-halfspace-contours.png"], "PNG bytes differ."
        assert generated["geometry.json"] == originals["geometry.json"], "Geometry bytes differ."
        fresh, fresh_date, fresh_ids = canonical_svg(generated["characteristic-halfspace-contours.svg"].decode("utf-8"))
        old, old_date, old_ids = canonical_svg(originals["characteristic-halfspace-contours.svg"].decode("utf-8"))
        assert fresh == old, "SVG differs beyond date and generated element identifiers."
        assert len(fresh_ids) == len(old_ids)
        geometry_checks = check_geometry(json.loads(generated["geometry.json"]))
        output.mkdir(parents=True)
        for name, (renamed, expected) in EXPECTED.items():
            # Only SVG's explicitly verified volatile fields are restored.
            data = originals[name] if name.endswith(".svg") else generated[name]
            assert sha(data) == expected
            (output / renamed).write_bytes(data)
        (output / "fresh-characteristic-halfspace-contours.svg").write_bytes(generated["characteristic-halfspace-contours.svg"])
        receipt = {
            "schema": "AN02-L111-standalone-figure-reproduction/v1", "status": "pass",
            "recorded_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(), "versions": versions,
            "private_inputs_required": False, "original_renderer_unchanged": True,
            "PNG_byte_identical": True, "geometry_byte_identical": True,
            "SVG_complete_comparison_except_explicit_volatile_fields": True,
            "SVG_volatile_replacements": {"date": {"fresh": fresh_date, "original": old_date},
                "identifiers_in_definition_order": [{"fresh": a, "original": b} for a, b in zip(fresh_ids, old_ids) if a != b]},
            "fresh_SVG_sha256": sha(generated["characteristic-halfspace-contours.svg"]),
            "geometry_checks": geometry_checks, "geometry_check_count": len(geometry_checks),
            "outputs": [{"name": renamed, "sha256": sha((output / renamed).read_bytes()), "bytes": len((output / renamed).read_bytes())} for renamed, _ in EXPECTED.values()],
            "renderer_stdout": process.stdout.strip(),
            "scope": "Figure fidelity and bounded geometry checks; the written proof establishes support, smoothness and boundary flatness.",
        }
        (output / "reproduction.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": "pass", "output_dir": str(output), "geometry_check_count": len(geometry_checks)}))


if __name__ == "__main__":
    main()
