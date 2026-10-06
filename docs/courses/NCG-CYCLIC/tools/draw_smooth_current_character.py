"""Reproduce the exact map/support/normalization diagram for Appendix B1--B6."""
from pathlib import Path
import argparse, os, shutil, subprocess
from html import escape
import re

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', type=Path, help='SVG output; a PNG with the same stem is also rendered')
parser.add_argument('--chromium', help='Chrome/Chromium executable (or set CHROME_BIN)')
parser.add_argument('--svg-only', action='store_true', help='Write only the editable SVG')
args = parser.parse_args()
default = (HERE.parent / 'public/assets/smooth-current-character-bridge.svg'
           if HERE.name == 'tools' else HERE / 'workflow-smooth-current-character-public-figure.svg')
OUT = (args.output or default).resolve()
OUT.parent.mkdir(parents=True, exist_ok=True)
parts = ['''<svg xmlns="http://www.w3.org/2000/svg" width="1440" height="1000" viewBox="0 0 1440 1000">
<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10z" fill="#31536b"/></marker></defs>
<rect width="1440" height="1000" fill="#f8fafc"/>
<style>text{font-family:Arial,sans-serif;fill:#173245}.title{font-size:32px;font-weight:700}.h{font-size:25px;font-weight:700}.t{font-size:24px}.s{font-size:21px}.m{font-size:23px;font-family:'Cambria Math',Cambria,serif}.b{fill:#fff;stroke:#8aa5b8;stroke-width:2}.a{stroke:#31536b;stroke-width:2.5;fill:none;marker-end:url(#arrow)}</style>
''']


def notation(value):
    """Typeset the explicitly grouped sub/superscripts in our exact labels."""
    out = []
    i = 0
    while i < len(value):
        if value[i] not in '_^':
            out.append(escape(value[i])); i += 1; continue
        shift = 'sub' if value[i] == '_' else 'super'
        i += 1
        if i < len(value) and value[i] == '(':
            depth, j = 1, i + 1
            while j < len(value) and depth:
                depth += (value[j] == '(') - (value[j] == ')')
                j += 1
            assert depth == 0
            token = value[i+1:j-1]; i = j
        elif i < len(value) and value[i] == '⌊':
            j = value.index('⌋', i) + 1
            token = value[i:j]; i = j
        elif i < len(value) and value[i] == '*':
            token = '*'; i += 1
        else:
            match = re.match(r'[A-Za-z0-9ℂ−+α-ωΑ-Ω]+', value[i:])
            assert match, value[i:]
            token = match.group(0); i += len(token)
        out.append(f'<tspan baseline-shift="{shift}" font-size="70%">{notation(token)}</tspan>')
    return ''.join(out)


def text(x, y, value, style="t", anchor="start"):
    parts.append(f'<text x="{x}" y="{y}" class="{style}" text-anchor="{anchor}">{notation(value)}</text>')


def box(x, y, w, h, color="#fff"):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="13" class="b" style="fill:{color}"/>')


def arrow(x1, y1, x2, y2):
    parts.append(f'<path d="M{x1},{y1} L{x2},{y2}" class="a"/>')


text(42, 52, "The smooth compact-support current bridge", "title")
text(42, 88, "B1–B6: actual maps, compact primitives, locally finite cycles and exact character factors", "s")

for x, name, subtitle in [(42, "Ω_c^*(M)", "globally smooth forms"), (510, "Ω_c^*(T)", "compatible simplex forms"), (978, "C_c^*(T; ℂ)", "finite-support cochains")]:
    box(x, 116, 420, 100)
    text(x + 210, 153, name, "h", "middle")
    text(x + 210, 191, subtitle, "t", "middle")
arrow(462, 166, 510, 166)
arrow(930, 166, 978, 166)
text(485, 139, "R", "m", "middle")
text(954, 139, "I_T", "m", "middle")
text(42, 256, "(Rω)_s = h_s^*ω;  I = I_T R;  Iω(s) = ∫_s h_s^*ω.  Both arrows are quasi-isomorphisms.", "m")

box(42, 282, 1356, 186, "#edf5fa")
text(65, 321, "Compact primitive: the step needed for an arbitrary current", "h")
text(65, 357, "Rω = dη", "m")
text(65, 390, "η compatible, compact", "s")
arrow(324, 365, 385, 365)
text(407, 357, "(η, −ω) is a closed cone element", "m")
text(407, 390, "finite Čech descent + partitions (B1)", "s")
arrow(830, 365, 890, 365)
text(914, 357, "ω = dα", "m")
text(914, 390, "α globally smooth, compact", "s")
text(65, 439, "All constructions stay in a common compact neighborhood. Closed C therefore gives C(dα) = 0.", "t")

box(42, 494, 652, 204)
box(720, 494, 678, 204)
text(65, 532, "Cycle current: a literal identity", "h")
text(65, 570, "c = Σ_s λ_s s, locally finite, ∂c = 0", "m")
text(65, 606, "S_c(ω) = Σ_s λ_s ∫_s h_s^*ω = c(Iω)", "m")
text(65, 644, "Compact support meets finitely many simplices.", "s")
text(65, 677, "Finite local volume bound; Stokes cancels faces.", "s")
text(743, 532, "Any closed current: cohomological identity", "h")
text(743, 570, "H_p^lf(T; ℂ) ≅ Hom_ℂ(H_c^p(M; ℂ), ℂ)", "m")
text(743, 606, "C(ω) = ⟨[C], I_*[ω]⟩ for closed compact ω", "m")
text(743, 644, "The smooth comparison defines [C] (B.11)–(B.12).", "s")
text(743, 677, "Every homology class has an order-zero S_c.", "s")

box(42, 724, 1356, 192, "#edf5fa")
text(65, 762, "The exact K-current equality (B.23)–(B.25)", "h")
text(65, 801, "τ̂_C = (−1)^⌊d/2⌋ τ_C / a_d", "m")
text(720, 801, "J_(τ̂_C)(z) = ⟨[C], ch_(c,d)(z)⟩", "m")
text(65, 838, "a_(2m) = m! (2πi)^m", "m")
text(720, 838, "a_(2m+1) = (2m+1)! (2πi)^(m+1) / m!", "m")
text(65, 875, "Even m ≥ 1; odd m ≥ 0; κ^+([u]) = θ([u^−1]) = −θ([u]); increasing interval first.", "s")
text(65, 901, "Degree zero: the locally finite measure gives a rank two-trace, J_(τ_μ)(z) = μ(rank z).", "s")
text(42, 957, "Domains, signs and support are exact. No fixed-arity amalgamation is claimed. Proof: Appendix B1–B6; Appendix A.", "s")
parts.append('</svg>')
OUT.write_text('\n'.join(parts), encoding='utf-8')
print(OUT.as_posix())

if not args.svg_only:
    chrome = args.chromium or os.environ.get('CHROME_BIN')
    if not chrome:
        for candidate in ['google-chrome', 'chromium', 'chromium-browser', 'chrome']:
            chrome = shutil.which(candidate)
            if chrome:
                break
    if not chrome:
        windows = Path(os.environ.get('PROGRAMFILES', 'C:/Program Files')) / 'Google/Chrome/Application/chrome.exe'
        if windows.is_file():
            chrome = str(windows)
    if not chrome:
        parser.error('SVG written. Pass --chromium or set CHROME_BIN to render its PNG.')
    png = OUT.with_suffix('.png')
    command = [chrome, '--headless', '--disable-gpu', '--hide-scrollbars',
               '--force-device-scale-factor=1', '--window-size=1440,1000',
               '--screenshot=' + str(png), OUT.as_uri()]
    completed = subprocess.run(command, check=True, capture_output=True, text=True,
                               timeout=45, creationflags=(subprocess.CREATE_NO_WINDOW if os.name == 'nt' else 0))
    assert png.is_file(), completed.stderr
    print(png.as_posix())
