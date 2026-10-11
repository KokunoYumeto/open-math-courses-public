"""Build the owned Yang--Mills lesson, native MathML reader and source download."""
from pathlib import Path
import hashlib
import html
import json
import re
import subprocess
import zipfile
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent
COURSE = Path(__file__).resolve().parents[1]
SOURCE = COURSE / "src/YM-01.md"
TITLE = "Quaternionic colour maps"

CSS = """html{color:#182c35;background:#f4f2eb;font-family:Georgia,serif}
body{margin:0}main{max-width:850px;margin:auto;padding:34px 24px 70px;background:#fffef9}
nav,footer{max-width:850px;margin:auto;padding:18px 24px;font:15px system-ui,sans-serif}
nav a{margin-right:20px}h1,h2,h3{font-family:system-ui,sans-serif;line-height:1.2;color:#163e4b}
h1{font-size:2.5rem;margin-top:.3em}h2{margin-top:2em;font-size:1.55rem}
h3{margin-top:1.7em;font-size:1.2rem}p,li{font-size:18px;line-height:1.65}
a{color:#005976;text-underline-offset:3px}a:focus{outline:3px solid #e19c2b}
.equation{display:flex;align-items:center;gap:20px;margin:25px 0;max-width:100%;font-size:18px}
.equation-body{overflow-x:auto;overflow-y:hidden;padding:10px 2px;flex:1;min-width:0}
.eq-number{font:15px system-ui,sans-serif;flex:none}math{font-size:1.05em}
math[display=block]{margin:0;min-width:max-content}img{max-width:100%;height:auto}
figure{margin:25px 0}.diagram{overflow-x:auto;margin:25px 0}.diagram img{min-width:840px;width:100%;max-width:none;display:block}
table{border-collapse:collapse}td,th{padding:10px;border:1px solid #aab9bd}
.contents{padding:15px 22px;background:#e8f0ef;border-left:4px solid #287c78}
.contents li{font:16px/1.8 system-ui,sans-serif}footer{font-size:14px}
@media(max-width:600px){main{padding:24px 18px 50px}h1{font-size:2rem}
p,li{font-size:17px}.equation{gap:10px;font-size:17px}.eq-number{font-size:12px}nav{line-height:2}}
"""

def digest(b):
    return hashlib.sha256(b).hexdigest()

def pandoc(args, body):
    p = subprocess.run(["pandoc", *args], input=body, text=True, encoding="utf-8",
                       capture_output=True, check=True)
    if p.stderr.strip():
        raise RuntimeError(p.stderr)
    return p.stdout

def figure():
    target = COURSE / "figures/moment-derivative.svg"
    target.parent.mkdir(parents=True, exist_ok=True)
    svg = """<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="610" viewBox="0 0 1080 610" role="img" aria-labelledby="title desc">
<title id="title">The exact derivative of the quaternionic colour map</title>
<desc id="desc">For a equals r u with r positive and u unit, write h equals u times t plus xi. After undoing conjugation by u in the target, the radial input t maps to 2 r t e; the two perpendicular components of xi map to 2 r xi cross e; the one component of xi parallel to e maps to zero. Total domain dimension four, target dimension three, rank three, kernel dimension one.</desc>
<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8Z" fill="#256773"/></marker></defs>
<rect x="0" y="0" width="1080" height="610" rx="18" fill="#edf3f1"/>
<g font-family="Arial,sans-serif" fill="#193d46">
<text x="40" y="52" font-size="27" font-weight="bold">Where the three colour directions come from</text>
<text x="40" y="90" font-size="20">a = r u, r = |a| &gt; 0, |u| = 1; h = u(t + &#958;)</text>
<text x="65" y="145" font-size="19" font-weight="bold">DOMAIN: 4 real directions</text>
<text x="665" y="145" font-size="19" font-weight="bold">TARGET: 3 real directions</text>
<rect x="40" y="170" width="345" height="86" rx="10" fill="white" stroke="#a4bdbe"/>
<text x="65" y="204" font-size="23">t &#8712; &#8477;</text><text x="65" y="236" font-size="17">One radial direction</text>
<path d="M405 213 H620" stroke="#256773" stroke-width="3" marker-end="url(#arrow)"/>
<text x="439" y="197" font-size="19">multiply by 2r</text>
<rect x="645" y="170" width="390" height="86" rx="10" fill="white" stroke="#a4bdbe"/>
<text x="670" y="204" font-size="23">2r t e &#8712; &#8477;e</text><text x="670" y="236" font-size="17">One radial colour direction</text>
<rect x="40" y="280" width="345" height="95" rx="10" fill="white" stroke="#a4bdbe"/>
<text x="65" y="315" font-size="23">&#958; &#8712; e&#8869;</text><text x="65" y="350" font-size="17">Two transverse directions</text>
<path d="M405 326 H620" stroke="#256773" stroke-width="3" marker-end="url(#arrow)"/>
<text x="433" y="311" font-size="19">2r times (&#958; &#215; e)</text>
<rect x="645" y="280" width="390" height="95" rx="10" fill="white" stroke="#a4bdbe"/>
<text x="670" y="315" font-size="23">2r (&#958; &#215; e) &#8712; e&#8869;</text><text x="670" y="350" font-size="17">Two transverse colour directions</text>
<rect x="40" y="402" width="345" height="86" rx="10" fill="#fff4df" stroke="#cfb179"/>
<text x="65" y="436" font-size="23">&#958; &#8712; &#8477;e</text><text x="65" y="468" font-size="17">One fibre direction</text>
<path d="M405 445 H620" stroke="#976222" stroke-width="3" marker-end="url(#arrow)"/>
<text x="449" y="430" font-size="19">&#958; &#215; e = 0</text>
<text x="672" y="454" font-size="25">0</text>
<text x="40" y="536" font-size="20">Final target value: conjugate the sum by u. Both coordinate changes are isometries.</text>
<text x="40" y="574" font-size="19">D&#956; D&#956;* = 4r&#178; I&#8323;    |    Kernel = &#8477;(a e)    |    At a = 0: rank 0.    Equations (5.1)&#8211;(5.4).</text>
</g></svg>"""
    target.write_text(svg, encoding="utf-8")

def render(source_path, title, output):
    global SOURCE, TITLE
    SOURCE, TITLE = source_path, title
    source = SOURCE.read_text(encoding="utf-8")
    ast = json.loads(pandoc(["-f", "markdown+tex_math_single_backslash", "-t", "json"], source))
    formulas = []
    def visit(x):
        if isinstance(x, dict):
            if x.get("t") == "Math":
                formulas.append({"display": x["c"][0]["t"] == "DisplayMath",
                                 "tex": x["c"][1]})
                # The equation number becomes the reader's adjacent HTML label.
                x["c"][1] = re.sub(r"\\tag\{[^}]+\}", "", x["c"][1])
                x["c"][1] = re.sub(r"\{\\rm\s+([^{}]*)\}", lambda m: r"{\mathrm{" + m[1] + "}}", x["c"][1])
                x["c"][1] = re.sub(r"\{\\cal\s+([^{}]*)\}", lambda m: r"{\mathcal{" + m[1] + "}}", x["c"][1])
                x["c"][1] = x["c"][1].replace(r"\hbox", r"\text")
                # Preserve the original TeX annotation while rendering the operator-norm label.
                x["c"][1] = x["c"][1].replace(r"\rm op", r"\mathrm{op}")
                if SOURCE.name.startswith("YM-F18"):
                    x["c"][1] = " ".join(x["c"][1].splitlines())
                    x["c"][1] = x["c"][1].replace(r"\rm cube", r"\mathrm{cube}")
                if SOURCE.name == "YM-F17.md":
                    x["c"][1] = " ".join(x["c"][1].splitlines())
                if SOURCE.name == "YM-F16.md":
                    x["c"][1] = " ".join(x["c"][1].splitlines())
                if SOURCE.name == "YM-F15.md":
                    x["c"][1] = " ".join(x["c"][1].splitlines())
                if SOURCE.name == "YM-F14.md":
                    x["c"][1] = " ".join(x["c"][1].splitlines())
                if SOURCE.name == "YM-F13.md":
                    x["c"][1] = " ".join(x["c"][1].splitlines())
                if SOURCE.name == "YM-F12.md":
                    x["c"][1] = " ".join(x["c"][1].splitlines())
                    x["c"][1] = x["c"][1].replace(r"\rm phys", r"\mathrm{phys}")
                    # Layout macro only; the source annotation retains its exact spacing.
                    x["c"][1] = re.sub(r"\\hspace\{[0-9.]+mm\}", r"\\quad ", x["c"][1])
                # These authoring sources wrap a single aligned row across
                # text lines. Keep their original annotations; join whitespace
                # only in the MathML converter input.
                if SOURCE.name in ("YM-F09-potential-difference.md", "YM-F09-regular-restart.md", "YM-F09-wave-stability.md", "YM-F09-fixed-heat-comparison.md", "YM-F09-uniform-difference.md", "YM-F09-spatial-tension-difference.md", "YM-F09-original-gauge-reconstruction.md", "YM-F09-initial-data-stability.md", "YM-F09-constrained-approximation.md", "YM-F09-common-regular-interval.md", "YM-F09-energy-data-limit.md", "YM-F09-global-continuation.md", "YM-F09-global-energy-data.md"):
                    x["c"][1] = " ".join(x["c"][1].splitlines())
                    x["c"][1] = x["c"][1].replace(r"\rm df", r"\mathrm{df}")
                    x["c"][1] = re.sub(r"\\hspace\{[0-9.]+mm\}", r"\\quad ", x["c"][1])
                if SOURCE.name in ("YM-F09-uniform-difference.md", "YM-F09-spatial-tension-difference.md", "YM-F09-original-gauge-reconstruction.md", "YM-F09-initial-data-stability.md", "YM-F09-constrained-approximation.md", "YM-F09-common-regular-interval.md", "YM-F09-energy-data-limit.md", "YM-F09-global-continuation.md", "YM-F09-global-energy-data.md"):
                    tex = x["c"][1].replace(r"\rm ref", r"\mathrm{ref}")
                    if SOURCE.name in ("YM-F09-constrained-approximation.md", "YM-F09-common-regular-interval.md", "YM-F09-energy-data-limit.md", "YM-F09-global-continuation.md", "YM-F09-global-energy-data.md"):
                        tex = tex.replace(r"\rm curv", r"\mathrm{curv}")
                    # Convert a grouped TeX fraction only in converter input.
                    # Nested numerator/denominator braces are kept intact.
                    while re.search(r"\\over(?![A-Za-z])", tex):
                        at = re.search(r"\\over(?![A-Za-z])", tex).start(); stack = []
                        for pos in range(at):
                            if pos and tex[pos-1] == "\\": continue
                            if tex[pos] == "{": stack.append(pos)
                            elif tex[pos] == "}": stack.pop()
                        if not stack: raise ValueError("Ungrouped fraction")
                        start = stack[-1]; depth = 1; end = start + 1
                        while end < len(tex) and depth:
                            if tex[end-1] != "\\":
                                if tex[end] == "{": depth += 1
                                elif tex[end] == "}": depth -= 1
                            end += 1
                        if depth: raise ValueError("Unclosed fraction")
                        tex = (tex[:start] + r"\frac{" + tex[start+1:at].strip()
                               + "}{" + tex[at+5:end-1].strip() + "}" + tex[end:])
                    x["c"][1] = tex
                # Equivalent fraction syntax for MathML; the annotation stays verbatim.
                for numerator, denominator in [
                    (r"3\sqrt3", r"2^{4/3}\pi^{1/3}"),
                    (r"S^{\beta_k}", r"\sqrt{2\beta_k}"),
                    ("1", r"\beta_k"), ("1", r"\sqrt{2\beta_k}"),
                    ("l+1/2-1", "2"), ("q-l+3/2+1", "2"), ("q", "2")]:
                    x["c"][1] = x["c"][1].replace(
                        "{"+numerator+r"\over"+denominator+"}",
                        r"\frac{"+numerator+"}{"+denominator+"}")
            elif x.get("t") == "Link":
                if x["c"][-1][0].startswith("../") and not x["c"][-1][0].startswith("../figures/"):
                    x["c"][-1][0] = x["c"][-1][0][3:]
            elif x.get("t") == "Image":
                x["c"][-1][0] = x["c"][-1][0].replace("../figures/", "figures/")
            for y in x.values():
                visit(y)
        elif isinstance(x, list):
            for y in x:
                visit(y)
    visit(ast)
    rendered = pandoc(["-f", "json", "-t", "html5", "--mathml"], json.dumps(ast))
    soup = BeautifulSoup(rendered, "html.parser")
    if SOURCE.name.startswith("YM-F18"):
        for table in soup.find_all("table"):
            wrapper=soup.new_tag("div");wrapper["class"]="diagram"
            table.wrap(wrapper)
    maths = soup.find_all("math")
    assert len(maths) == len(formulas)
    assert not soup.find("merror")
    for node, record in zip(maths, formulas):
        annotations = node.find_all("annotation", encoding="application/x-tex")
        assert len(annotations) == 1
        annotations[0].string = record["tex"]
        if record["display"]:
            parent = node.parent
            assert parent.name in ("p", "span")
            assert all(child is node or (isinstance(child, str) and not child.strip()) for child in parent.contents), str(parent)[:700]
            eq = soup.new_tag("div", attrs={"class": "equation"})
            scrolling = soup.new_tag("div", attrs={"class": "equation-body", "tabindex": "0"})
            parent.replace_with(eq)
            eq.append(scrolling)
            scrolling.append(node)
            tag = re.search(r"\\tag\{([^}]+)\}", record["tex"])
            if tag:
                eq["id"] = "eq-" + tag[1].replace(".", "-")
                label = soup.new_tag("span", attrs={"class": "eq-number"})
                label.string = "(" + tag[1] + ")"
                eq.append(label)
    for table in soup.find_all("table"):
        wrapper=soup.new_tag("div", attrs={"style":"overflow-x:auto", "tabindex":"0", "aria-label":"Scrollable table"})
        table.wrap(wrapper)
    for img in soup.find_all("img"):
        diagram = soup.new_tag("div", attrs={"class": "diagram", "tabindex": "0",
                                           "aria-label": "Scrollable mathematical diagram"})
        parent = img.parent
        if parent.name == "p" and len(parent.contents) == 1:
            parent.replace_with(diagram)
        else:
            img.replace_with(diagram)
        diagram.append(img)
    toc = '<aside class="contents" aria-label="Contents"><strong>In this lesson</strong><ol>'
    for h in soup.find_all("h2"):
        heading_copy = BeautifulSoup(str(h), "html.parser")
        for annotation in heading_copy.find_all("annotation"):
            annotation.decompose()
        toc += '<li><a href="#' + h["id"] + '">' + html.escape(re.sub(r"^\d+\.\s*", "", heading_copy.get_text())) + "</a></li>"
    toc += "</ol></aside>"
    first_h2 = soup.find("h2")
    first_h2.insert_before(BeautifulSoup(toc, "html.parser"))
    page = '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>' + TITLE + '</title><link rel="stylesheet" href="reader.css"></head><body><nav><a href="index.html">Course contents</a><a href="src/LESSON_SOURCE">Lesson source</a><a href="../../downloads/yang-mills-geometry-and-states.zip">Source and reader download</a></nav><main>' + str(soup) + '</main><footer>Geometry and states in Yang–Mills theory · Mathematical content: CC0 1.0.</footer></body></html>'
    page = page.replace("src/LESSON_SOURCE", "src/" + SOURCE.name)
    (COURSE / output).write_text(page, encoding="utf-8")
    (COURSE / "reader.css").write_text(CSS, encoding="utf-8")
    return source, formulas


def profile_figure():
    svg = """<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="760" viewBox="0 0 1200 760" role="img" aria-labelledby="title desc">
<title id="title">Three compactly supported curls with a fixed core</title>
<desc id="desc">Coordinate projection of the balls, with the closure of the radius r ball strictly inside the radius R ball. The cutoff equals one on the core. The arbitrary support lies compactly inside the outer ball; no radial symmetry is assumed. The three complete vector formulas, including derivative contributions and zero components, are displayed below.</desc>
<rect width="1200" height="760" fill="#edf3f1" rx="18"/>
<g font-family="Arial,sans-serif" fill="#193d46">
<text x="36" y="48" font-size="27" font-weight="bold">One fixed core; every cutoff contribution retained</text>
<circle cx="212" cy="226" r="136" fill="#fff4df" stroke="#98652a" stroke-width="2" stroke-dasharray="8 6"/>
<circle cx="212" cy="226" r="68" fill="#d5e9e4" stroke="#26776e" stroke-width="2"/>
<circle cx="212" cy="226" r="3" fill="#193d46"/>
<text x="176" y="213" font-size="20">χ = 1</text><text x="184" y="254" font-size="19">|x| &lt; r</text>
<text x="72" y="390" font-size="18">Coordinate projection; radii schematic</text>
<path d="M216 226 L348 226" stroke="#98652a" stroke-width="2"/>
<text x="300" y="215" font-size="20">R</text>
<path d="M212 226 L212 158" stroke="#26776e" stroke-width="2"/>
<text x="224" y="181" font-size="20">r</text>
<text x="422" y="125" font-size="23" font-weight="bold">0 &lt; r &lt; R</text>
<text x="422" y="171" font-size="22">supp χ ⊂ B_R(0), compactly inside the open ball</text>
<text x="422" y="215" font-size="22">No radial symmetry is assumed.</text>
<text x="422" y="265" font-size="22">Core: w⁽¹⁾ = (1,0,0), w⁽²⁾ = (0,1,0), w⁽³⁾ = (0,0,1)</text>
<text x="422" y="311" font-size="22">All three divergences vanish, including across the cutoff.</text>
<text x="422" y="357" font-size="21">Outside supp χ: χ and every derivative vanish.</text>
<rect x="32" y="425" width="1136" height="240" rx="12" fill="#fffef9" stroke="#a4bdbe"/>
<text x="56" y="465" font-size="23" font-weight="bold">Complete spatial components — equations (2.8)–(2.10)</text>
<text x="56" y="517" font-size="24">w⁽¹⁾ = curl(0,0,χx₂)     = (χ + x₂χ₂, −x₂χ₁, 0)</text>
<text x="56" y="572" font-size="24">w⁽²⁾ = curl(0,0,−χx₁) = (−x₁χ₂, χ + x₁χ₁, 0)</text>
<text x="56" y="627" font-size="24">w⁽³⁾ = curl(0,χx₁,0)     = (−x₁χ₃, 0, χ + x₁χ₁)</text>
<text x="36" y="712" font-size="22">Cᵢ = c₁wᵢ⁽¹⁾ + c₂wᵢ⁽²⁾ + c₃wᵢ⁽³⁾; (C₁(0), C₂(0), C₃(0)) = (c₁, c₂, c₃).</text>
<text x="36" y="745" font-size="17">The drawing specifies no support boundary for the arbitrary χ. Source and proof: Lesson 2, §§1–3.</text>
</g></svg>"""
    (COURSE/"figures/profile-cutoff.svg").write_text(svg,encoding="utf-8",newline="\n")


def carrier_figure():
    svg="""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="860" viewBox="0 0 1200 860" role="img" aria-labelledby="title desc">
<title id="title">The exact pullback and the full parameter connection</title>
<desc id="desc">The principal-bundle square sends p in P H to a p in L, and x in X to r H of x in D. Its vertical arrows are bundle projections. D has dimension 49, its base M has dimension 24 and its fibre G over K has dimension 25. The associated rank 24 bundle E D pulls back to W H and is the pullback of T M. The total parameter space Y has dimension 73. The lower panel lists the full connection and its parameter, mixed, spatial and zero time curvature components.</desc>
<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8Z" fill="#256773"/></marker></defs>
<rect width="1200" height="860" rx="18" fill="#edf3f1"/>
<g font-family="Arial,sans-serif" fill="#193d46">
<text x="36" y="49" font-size="27" font-weight="bold">A nontrivial reduction with an explicit higher carrier</text>
<text x="36" y="85" font-size="19">K = ρ(Sp(1)) ⊂ G = Spin(8) ⊂ L = F₄. Every arrow below is the specified map.</text>
<rect x="44" y="118" width="690" height="326" rx="12" fill="#fffef9" stroke="#a4bdbe"/>
<text x="131" y="171" font-size="28">P_H</text>
<text x="582" y="171" font-size="28">L</text>
<path d="M210 159 H535" stroke="#256773" stroke-width="3" marker-end="url(#arrow)"/>
<text x="330" y="145" font-size="20">p ↦ a_p</text>
<path d="M160 191 V282" stroke="#256773" stroke-width="3" marker-end="url(#arrow)"/>
<path d="M595 191 V282" stroke="#256773" stroke-width="3" marker-end="url(#arrow)"/>
<text x="127" y="322" font-size="27">X ≅ S⁶</text>
<text x="533" y="322" font-size="27">D = L/K</text>
<path d="M255 310 H500" stroke="#256773" stroke-width="3" marker-end="url(#arrow)"/>
<text x="345" y="293" font-size="22">r_H</text>
<text x="81" y="382" font-size="22">P_H ≅ r_H*(L → D);  π_D r_H(x) = G.</text>
<text x="81" y="420" font-size="18">The square is a pullback. Both vertical arrows are projections.</text>
<rect x="758" y="118" width="398" height="326" rx="12" fill="#fff4df" stroke="#cfb179"/>
<text x="785" y="163" font-size="23" font-weight="bold">Dimensions and ranks</text>
<text x="785" y="207" font-size="22">D = L/K: 49</text>
<text x="785" y="247" font-size="22">M = L/G: 24</text>
<text x="785" y="287" font-size="22">Fibre G/K: 25</text>
<text x="785" y="331" font-size="22">E_D ≅ π_D*TM: rank 24</text>
<text x="785" y="371" font-size="22">r_H*E_D ≅ W_H</text>
<text x="785" y="411" font-size="22">Y = Tot(E_D): 49 + 24 = 73</text>
<rect x="44" y="472" width="1112" height="306" rx="12" fill="white" stroke="#a4bdbe"/>
<text x="71" y="515" font-size="24" font-weight="bold">The connection on Y × ℝ¹˒³ includes every parameter direction</text>
<text x="72" y="560" font-size="23">𝔅 = b_A dyᴬ + cᵢ dxⁱ,   𝔅₀ = 0,   cᵢ = φ(Cᵢ).</text>
<text x="72" y="608" font-size="22">𝔉_AB = ∂_A b_B − ∂_B b_A + [b_A,b_B]</text>
<text x="72" y="654" font-size="22">𝔉_Ai = ∂_A cᵢ + [b_A,cᵢ]</text>
<text x="72" y="700" font-size="22">𝔉_ij = ∂ᵢcⱼ − ∂ⱼcᵢ + [cᵢ,cⱼ]</text>
<text x="754" y="654" font-size="22">𝔉_A0 = 0;  𝔉_0i = 0</text>
<text x="72" y="749" font-size="19">Outside the spatial support: mixed and spatial terms vanish; parameter curvature remains.</text>
<text x="44" y="818" font-size="19">Proofs: Lesson 3, (3.27)–(3.43) and (3.44)–(3.50). Bundle dimensions are exact.</text>
<text x="44" y="846" font-size="17">This diagram describes the bundle and connection; it makes no continuum spectral assertion.</text>
</g></svg>"""
    (COURSE/"figures/bundle-carrier.svg").write_text(svg,encoding="utf-8",newline="\n")

def cauchy_figure():
    svg="""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="840" viewBox="0 0 1200 840" role="img" aria-labelledby="title desc">
<title id="title">Support propagation and the exact backward-cone energy argument</title>
<desc id="desc">Spatial coordinate projections. On the left, the support at future time s is contained in the radius R plus s ball, and more precisely in the points at distance at most s from the original closed support K. The shaded region is an allowed envelope, not an assertion that the field fills it. On the right, a backward cone has ball radius rho minus s, with zero initial energy on its base. Its derivative is minus the boundary integral of q dot n plus e. Since the absolute flux is at most e, zero energy persists. Physical time is t equals s over c.</desc>
<defs><marker id="arr" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8Z" fill="#256773"/></marker></defs>
<rect width="1200" height="840" rx="18" fill="#edf3f1"/>
<g font-family="Arial,sans-serif" fill="#193d46">
<text x="35" y="48" font-size="27" font-weight="bold">The same speed controls support and domain of dependence</text>
<text x="35" y="86" font-size="19">Coordinate projections; axes have independent drawing scales. Time coordinate s = ct, c &gt; 0.</text>
<rect x="28" y="112" width="554" height="410" rx="12" fill="#fffef9" stroke="#a4bdbe"/>
<rect x="612" y="112" width="560" height="410" rx="12" fill="#fffef9" stroke="#a4bdbe"/>
<text x="53" y="151" font-size="22" font-weight="bold">Allowed support envelope, s ≥ 0</text>
<path d="M206 430 L406 430 L526 213 L86 213 Z" fill="#cce5df" stroke="#26776e" stroke-width="2"/>
<path d="M61 430 H547 M306 454 V180" fill="none" stroke="#256773" stroke-width="2" marker-end="url(#arr)"/>
<text x="543" y="456" font-size="20">x</text><text x="319" y="189" font-size="20">s</text>
<text x="181" y="459" font-size="19">−R</text><text x="399" y="459" font-size="19">R</text>
<text x="106" y="205" font-size="19">−R−s</text><text x="455" y="205" font-size="19">R+s</text>
<text x="329" y="300" font-size="19">Possible support</text>
<text x="65" y="492" font-size="18">Actual support ⊂ {x : dist(x,K) ≤ s},  K = supp C.</text>
<text x="640" y="151" font-size="22" font-weight="bold">Backward cone with zero initial energy</text>
<path d="M724 430 L1112 430 L994 233 L842 233 Z" fill="#fff0d3" stroke="#98652a" stroke-width="2"/>
<path d="M666 430 H1140 M918 451 V178" fill="none" stroke="#256773" stroke-width="2" marker-end="url(#arr)"/>
<path d="M842 233 H994" stroke="#98652a" stroke-width="3"/>
<text x="1128" y="456" font-size="20">x</text><text x="931" y="189" font-size="20">s</text>
<text x="864" y="221" font-size="19">s = s₀ &lt; ρ</text>
<text x="757" y="360" font-size="20">Ball B<tspan baseline-shift="sub" font-size="15">ρ−s</tspan><tspan baseline-shift="baseline">(x₀)</tspan></text>
<text x="703" y="461" font-size="18">x₀−ρ</text><text x="903" y="461" font-size="18">x₀</text><text x="1083" y="461" font-size="18">x₀+ρ</text>
<text x="651" y="492" font-size="18">Base energy = 0  ⇒  E = B = 0 in the cone.</text>
<rect x="28" y="548" width="1144" height="174" rx="12" fill="white" stroke="#a4bdbe"/>
<text x="52" y="588" font-size="23">e = ½(|E|² + |B|²),  q = −Σα Eᵅ × Bᵅ,  ∂ₛe + div q = 0.</text>
<text x="52" y="627" font-size="22">I(s) = ∫<tspan baseline-shift="sub" font-size="16">B_(ρ−s)(x₀)</tspan><tspan baseline-shift="baseline"> e d³x;</tspan></text>
<text x="433" y="627" font-size="22">I′(s) = −∫<tspan baseline-shift="sub" font-size="16">∂B_(ρ−s)(x₀)</tspan><tspan baseline-shift="baseline"> (q·n + e) dS ≤ 0.</tspan></text>
<text x="52" y="682" font-size="22">The second boundary term comes from the radius derivative −1; |q·n| ≤ e.</text>
<text x="35" y="766" font-size="20">A vanishes outside the support cone because ∂ₛA = E and A(0) = C.</text>
<text x="35" y="805" font-size="19">Complete proof: Lesson YM-04, Theorem 6.1, equations (4.32)–(4.38). Physical distance: c|t|.</text>
</g></svg>"""
    (COURSE/"figures/cauchy-cones.svg").write_text(svg,encoding="utf-8",newline="\n")

def short_page(title, body):
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+'</title><link rel="stylesheet" href="reader.css"></head><body><nav><a href="index.html">Course contents</a><a href="../../downloads/yang-mills-geometry-and-states.zip">Download</a></nav><main><h1>'+html.escape(title)+'</h1>'+body+'</main><footer>Mathematical content: CC0 1.0.</footer></body></html>'

def writej(path,data):
    path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n",encoding="utf-8",newline="\n")

def build():
    # The first source and reader retain their delivered mathematics.
    figure()
    profile_figure()
    carrier_figure()
    cauchy_figure()
    source1, formulas1=render(COURSE/"src/YM-01.md","Quaternionic colour maps","quaternionic-colour-maps.html")
    source2, formulas2=render(COURSE/"src/YM-02.md","Compact-support profiles, curvature and source","compact-support-profiles.html")
    source3, formulas3=render(COURSE/"src/YM-03.md","Bundle descent and the higher carrier","bundle-descent-higher-carrier.html")
    source4, formulas4=render(COURSE/"src/YM-04.md","Local smooth Cauchy evolution and finite propagation","local-cauchy-evolution.html")
    from figures_f01 import build as build_f01_figure
    build_f01_figure()
    sourcef1, formulasf1=render(COURSE/"src/YM-F01.md","Fields, coordinates and physical quantities","fields-coordinates-quantities.html")
    from figures_f02 import build as build_f02_figure
    build_f02_figure()
    sourcef2, formulasf2=render(COURSE/"src/YM-F02.md","Electromagnetism and gauge freedom","electromagnetism-gauge-freedom.html")
    from figures_f03 import build as build_f03_figure
    build_f03_figure()
    sourcef3, formulasf3=render(COURSE/"src/YM-F03.md","Symmetry through matrices","symmetry-through-matrices.html")
    from figures_f04 import build as build_f04_figure
    build_f04_figure()
    sourcef4, formulasf4=render(COURSE/"src/YM-F04.md","Lie groups and Lie algebras","lie-groups-and-lie-algebras.html")
    from figures_f05 import build as build_f05_figure
    build_f05_figure()
    sourcef5, formulasf5=render(COURSE/"src/YM-F05.md","Covariant derivatives and curvature","covariant-derivatives-and-curvature.html")
    from figures_f06 import build as build_f06_figure
    build_f06_figure()
    sourcef6, formulasf6=render(COURSE/"src/YM-F06.md","Bundles, parallel transport and holonomy","bundles-transport-holonomy.html")
    from figures_f07 import build as build_f07_figure
    build_f07_figure()
    sourcef7, formulasf7=render(COURSE/"src/YM-F07.md","The Yang–Mills action and field equations","action-and-field-equations.html")
    from figures_f08 import build as build_f08_figure
    build_f08_figure()
    sourcef8, formulasf8=render(COURSE/"src/YM-F08.md","Constraints, initial data and energy","constraints-initial-data-energy.html")
    from figures_f09 import build as build_f09_figure
    build_f09_figure()
    sourcef9, formulasf9=render(COURSE/"src/YM-F09.md","Local and global classical evolution","local-and-global-classical-evolution.html")
    render(COURSE/"src/YM-F09-measure-prerequisites.md","Measure, integration and complete function spaces","analysis-measure-prerequisites.html")
    render(COURSE/"src/YM-F09-scalar-prerequisites.md","Scalar powers and the inequality used by Hölder","analysis-scalar-prerequisites.html")
    from figures_f09_heat import build as build_f09_heat_figure
    build_f09_heat_figure()
    render(COURSE/"src/YM-F09-heat-analysis.md","Heat analysis for classical Yang–Mills evolution","classical-heat-analysis.html")
    from figures_f09_construction import build as build_f09_construction_figure
    build_f09_construction_figure()
    render(COURSE/"src/YM-F09-heat-construction.md","Constructing the Yang–Mills heat flow","classical-heat-construction.html")
    from figures_f09_caloric import build as build_f09_caloric_figure
    build_f09_caloric_figure()
    render(COURSE/"src/YM-F09-caloric-gauge.md","Heat smoothing and the caloric gauge","classical-caloric-gauge.html")
    from figures_f09_dynamic import build as build_f09_dynamic_figure
    build_f09_dynamic_figure()
    render(COURSE/"src/YM-F09-dynamic-heat.md","Global heat flow and the time component","classical-dynamic-heat.html")
    from figures_f09_potential import build as build_f09_potential_figure
    build_f09_potential_figure()
    render(COURSE/"src/YM-F09-potential-estimates.md","Ordinary heat smoothing and physical-time bounds","classical-potential-estimates.html")
    from figures_f09_fixedtime import build as build_f09_fixedtime_figure
    build_f09_fixedtime_figure()
    render(COURSE/"src/YM-F09-fixed-time-estimates.md","Gauss law, heat curvature and fixed-time estimates","classical-fixed-time-estimates.html")
    from figures_f09_wave import build as build_f09_wave_figure
    build_f09_wave_figure()
    render(COURSE/"src/YM-F09-wave-estimates.md","Wave energy, dispersion and null forms","classical-wave-estimates.html")
    from figures_f09_tension import build as build_f09_tension_figure
    build_f09_tension_figure()
    render(COURSE/"src/YM-F09-tension-null-structure.md","Tension, spatial decomposition and the nonlinear wave equation","classical-tension-null-structure.html")
    from figures_f09_curlfree import build as build_f09_curlfree_figure
    build_f09_curlfree_figure()
    render(COURSE/"src/YM-F09-curlfree-backward-heat.md","Curl-free interaction and backward heat bounds","classical-curlfree-backward-heat.html")
    from figures_f09_wave_closure import build as build_f09_wave_closure_figures
    build_f09_wave_closure_figures()
    render(COURSE/"src/YM-F09-potential-wave.md","Potential wave bounds from the complete heat equation","classical-potential-wave.html")
    render(COURSE/"src/YM-F09-spacetime-tension.md","Space-time tension at every spatial order","classical-spacetime-tension.html")
    render(COURSE/"src/YM-F09-temporal-boundary.md","Temporal boundary estimates and the endpoint identity","classical-temporal-boundary.html")
    from figures_f09_endpoint_gauge import build as build_f09_endpoint_gauge
    build_f09_endpoint_gauge()
    render(COURSE/"src/YM-F09-endpoint-wave.md","Endpoint wave bounds and the div\u2013curl identity","classical-endpoint-wave.html")
    render(COURSE/"src/YM-F09-electric-smoothing.md","Electric-curvature smoothing through every finite order","classical-electric-smoothing.html")
    render(COURSE/"src/YM-F09-physical-gauge.md","Returning to physical temporal gauge","classical-physical-gauge.html")
    from figures_f09_finite_argument import build as build_f09_finite_argument
    build_f09_finite_argument()
    from figures_f09_finite_closure import build as build_f09_finite_closure
    build_f09_finite_closure()
    render(COURSE/"src/YM-F09-wave-interactions.md","Spatial and temporal wave interactions","classical-wave-interactions.html")
    render(COURSE/"src/YM-F09-spatial-smoothing.md","Spatial heat smoothing and the wave coefficients","classical-spatial-smoothing.html")
    render(COURSE/"src/YM-F09-tension-forcing.md","The complete tension forcing","classical-tension-forcing.html")
    render(COURSE/"src/YM-F09-finite-wave-bound.md","The finite wave bound on an explicit physical interval","classical-finite-wave-bound.html")
    from figures_f09_differences import build as build_f09_differences
    build_f09_differences()
    from figures_f09_spatial_difference import build as build_f09_spatial_difference
    build_f09_spatial_difference()
    from figures_f09_gauge_difference import build as build_f09_gauge_difference
    build_f09_gauge_difference()
    render(COURSE/"src/YM-F09-electric-difference.md","Electric curvature differences and the original heat datum","classical-electric-difference.html")
    render(COURSE/"src/YM-F09-spatial-difference.md","Spatial heat-curvature differences and backward integration","classical-spatial-difference.html")
    render(COURSE/"src/YM-F09-temporal-difference.md","Differences at the temporal heat boundary","classical-temporal-difference.html")
    render(COURSE/"src/YM-F09-gauge-difference.md","Differences through the physical temporal gauge","classical-gauge-difference.html")
    from figures_f09_potential_difference import build as build_f09_potential_difference
    build_f09_potential_difference()
    render(COURSE/"src/YM-F09-potential-difference.md","Potential-wave differences and the full physical connection","classical-potential-difference.html")
    from figures_f09_regular_restart import build as build_f09_regular_restart
    build_f09_regular_restart()
    render(COURSE/"src/YM-F09-regular-restart.md","Strong endpoints and restarting the classical evolution","classical-regular-restart.html")
    from figures_f09_wave_stability import build as build_f09_wave_stability
    build_f09_wave_stability()
    render(COURSE/"src/YM-F09-wave-stability.md","Regular-solution stability and signed electric data","classical-wave-stability.html")
    from figures_f09_fixed_heat_comparison import build as build_f09_fixed_heat_comparison
    build_f09_fixed_heat_comparison()
    render(COURSE/"src/YM-F09-fixed-heat-comparison.md","Comparing heat extensions on the prescribed interval","classical-fixed-heat-comparison.html")
    from figures_f09_uniform_difference import build as build_f09_uniform_difference
    build_f09_uniform_difference()
    render(COURSE/"src/YM-F09-uniform-difference.md","Temporal differences, electric data and boundary increments","classical-uniform-difference.html")
    from figures_f09_spatial_tension_difference import build as build_f09_spatial_tension_difference
    build_f09_spatial_tension_difference()
    render(COURSE/"src/YM-F09-spatial-tension-difference.md","Spatial tension differences and their wave estimates","classical-spatial-tension-difference.html")
    from figures_f09_reconstruction_stability import build as build_f09_reconstruction_stability
    build_f09_reconstruction_stability()
    render(COURSE/"src/YM-F09-original-gauge-reconstruction.md","Reconstructing the original gauge and its initial anchors","classical-original-gauge-reconstruction.html")
    render(COURSE/"src/YM-F09-initial-data-stability.md","Stability with respect to the original initial data","classical-initial-data-stability.html")
    from figures_f09_approximation_interval import build as build_f09_approximation_interval
    build_f09_approximation_interval()
    render(COURSE/"src/YM-F09-constrained-approximation.md","Smooth approximation with the exact Gauss constraint","classical-constrained-approximation.html")
    render(COURSE/"src/YM-F09-common-regular-interval.md","A common existence interval for regular initial data","classical-common-regular-interval.html")
    from figures_f09_energy_global import build as build_f09_energy_global
    build_f09_energy_global()
    render(COURSE/"src/YM-F09-energy-data-limit.md","Constructing solutions from finite-energy data","classical-energy-data-limit.html")
    render(COURSE/"src/YM-F09-global-continuation.md","Global classical continuation in the original temporal gauge","classical-global-continuation.html")
    from figures_f09_global_energy import build as build_f09_global_energy
    build_f09_global_energy()
    render(COURSE/"src/YM-F09-global-energy-data.md","Global solutions from finite-energy data","classical-global-energy-data.html")
    from figures_f10 import build as build_f10
    build_f10()
    sourcef10, formulasf10=render(COURSE/"src/YM-F10.md","Euclidean Yang–Mills and instantons","euclidean-yang-mills-instantons.html")
    render(COURSE/"src/YM-F10-operators.md","Euclidean and Lorentzian Yang–Mills operators","euclidean-lorentzian-operators.html")
    from figures_f11 import build as build_f11
    build_f11()
    sourcef11, formulasf11=render(COURSE/"src/YM-F11.md","Oscillators and free quantum fields","oscillators-and-free-quantum-fields.html")
    from figures_f12 import build as build_f12
    build_f12()
    sourcef12, formulasf12=render(COURSE/"src/YM-F12.md","Quantum gauge symmetry","quantum-gauge-symmetry.html")
    from figures_f13 import build as build_f13
    build_f13()
    sourcef13, formulasf13=render(COURSE/"src/YM-F13.md","Renormalization and asymptotic freedom","renormalization-and-asymptotic-freedom.html")
    from figures_f14 import build as build_f14
    build_f14()
    sourcef14, formulasf14=render(COURSE/"src/YM-F14.md","Yang–Mills theory on a lattice","yang-mills-on-a-lattice.html")
    from figures_f15 import build as build_f15
    build_f15()
    sourcef15, formulasf15=render(COURSE/"src/YM-F15.md","Strong coupling, simulations and their errors","strong-coupling-simulations-errors.html")
    from figures_f16 import build as build_f16
    build_f16()
    sourcef16, formulasf16=render(COURSE/"src/YM-F16.md","Spectra, mass gaps and confinement","spectra-mass-gaps-confinement.html")
    from figures_f17 import build as build_f17
    build_f17()
    sourcef17, formulasf17=render(COURSE/"src/YM-F17.md","Continuum limits and reconstruction","continuum-limits-and-reconstruction.html")
    from figures_f18 import build as build_f18
    build_f18()
    sourcef18, formulasf18=render(COURSE/"src/YM-F18.md","The established research landscape and open problems","established-approaches-and-open-problems.html")
    render(COURSE/'src/YM-F18-heat.md','SU(2) heat kernel and classical action','two-dimensional-heat-and-action.html')
    render(COURSE/'src/YM-F18-probability.md','Compatible graphs and an actual continuum probability','two-dimensional-holonomy-probability.html')
    render(COURSE/'src/YM-F18-cube.md','Six faces of a cube: exact holonomy and probability','cube-face-holonomy-and-probability.html')
    render(COURSE/"src/YM-F18-finite.md","Integrating variables and reading formal expansions","finite-effective-actions.html")
    course=json.loads((COURSE/"course.json").read_text(encoding="utf-8"))
    complete=[u for u in course["units"] if u["status"]=="available"]
    course["available_core_lessons"]=len(complete)
    course["available_lessons"]=len(complete)+len(course["retained_materials"])
    course["core_solved_exercises"]=sum(u["solution_count"] for u in complete)
    course["solved_exercises"]=course["core_solved_exercises"]+sum(u["solution_count"] for u in course["retained_materials"])

    for unit in course["units"]:
        if unit["status"]=="available":
            unit["source_sha256"]=digest((COURSE/unit["source"]).read_bytes())
            unit["reader_sha256"]=digest((COURSE/unit["reader"]).read_bytes())
        elif unit.get("draft_source"):
            unit["draft_source_sha256"]=digest((COURSE/unit["draft_source"]).read_bytes())
            unit["draft_reader_sha256"]=digest((COURSE/unit["draft_reader"]).read_bytes())
    for unit in course["units"]:
        for component in unit.get("components",[]):
            for kind in ("source","reader"):
                component[kind+"_sha256"]=digest((COURSE/component[kind]).read_bytes())
    curriculum=json.loads((COURSE/"curriculum.json").read_text(encoding="utf-8"))
    curriculum["units"]=course["units"]
    writej(COURSE/"curriculum.json",curriculum)
    for unit in course["retained_materials"]:
        unit["source_sha256"]=digest((COURSE/unit["source"]).read_bytes())
        unit["reader_sha256"]=digest((COURSE/unit["reader"]).read_bytes())
    writej(COURSE/"course.json",course)
    proof="https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/c1f29f3e6dfeb20e4be5254ea4fac7578255eacc/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/"
    provenance=json.loads((COURSE/"provenance.json").read_text(encoding="utf-8"))
    provenance["readings"]=[x for x in provenance["readings"] if x.get("lesson")!="YM-02"]
    for file,loc in [("PROOF.md","Sections 7–9: original profiles and colour map"),
        ("COMPACT_SUPPORT_CAUCHY_EVOLUTION.md","CE18–CE23 and Proposition 4.1: all energy coefficients and zero-energy set"),
        ("HIGHER_CARRIER_AND_EVOLUTION.md","HC14–HC20: initial acceleration, Gauss-preserving correction and exact residual")]:
        provenance["readings"].append({"lesson":"YM-02","url":proof+file,"locators":loc})
    provenance["edition_date"]="2026-10-10"
    provenance["readings"]=[x for x in provenance["readings"] if x.get("lesson")!="YM-03"]
    base="https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/f2f7adf7ab7d08963333f2595237f91f20b53f66/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/"
    provenance["readings"].extend([
      {"lesson":"YM-03","url":base+"HIGHER_CARRIER_AND_EVOLUTION.md","locators":"HC1–HC13; full bundle and connection receiving maps"},
      {"lesson":"YM-03","url":base+"sources/higher_rung/s6_higher_rung_24d_preprint.tex",
       "locators":"ret:main; att:thm:stabilizer and tangent comparison; rettri:bundleclass, rettri:subgroup and rettri:forgetting",
       "scope":"Exact named programme providers; not a recertification of the complete compact-complex construction"},
      {"lesson":"YM-03","url":base+"SOURCE_PROVENANCE.md","locators":"Distinct originating, retained-source and later-derivation authorship"}])
    provenance["readings"]=[x for x in provenance["readings"] if x.get("lesson")!="YM-04"]
    provenance["readings"].append({"lesson":"YM-04",
        "url":"https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/485b61423c1f4e1805deb453c1b6b342b27842b6/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/COMPACT_SUPPORT_CAUCHY_EVOLUTION.md",
        "locators":"CE4–CE17 and CE18–CE23: original Cauchy data, constraints, moving-boundary flux, core comparison and complete physical energy",
        "scope":"Complete new local analytical proofs are in YM-04 §§2–4. The source's application of Sung-Jin Oh's global theorem is retained with separate attribution; its entire global analysis is not claimed as supplied by this lesson."})
    provenance["curriculum_selection"]="Authorship-neutral selection; no workbench result is currently selected for the main curriculum."
    provenance["foundations_lessons"]=[{
        "lesson":"YM-F01","source":"src/YM-F01.md","reader":"fields-coordinates-quantities.html",
        "origin":"Independent elementary exposition; no original research result or novelty claim.",
        "proof_locators":["Proposition 4.1","Theorem 6.1","Corollary 6.2","Proposition 7.1","(F1.40)","Exercises 1–8"],
        "preparation":"Real arithmetic and one-variable calculus, including product rule, elementary functions, substitution and the fundamental theorem of calculus.",
        "external_mathematical_source_used":False,
        "figure":{"source":"build/figures_f01.py","image":"figures/f01-transport.svg","meaning":"Exact Gaussian coordinate slice and sampled characteristic paths, with parameters and units displayed."},
        "licence":"CC0-1.0"}]
    provenance["foundations_lessons"].append(json.loads((COURSE/"src/YM-F02-provenance.json").read_text(encoding="utf-8")))
    provenance["foundations_lessons"].append(json.loads((COURSE/"src/YM-F03-provenance.json").read_text(encoding="utf-8")))
    provenance["foundations_lessons"].append(json.loads((COURSE/"src/YM-F04-provenance.json").read_text(encoding="utf-8")))
    provenance["foundations_lessons"].append(json.loads((COURSE/"src/YM-F05-provenance.json").read_text(encoding="utf-8")))
    provenance["foundations_lessons"].append(json.loads((COURSE/"src/YM-F06-provenance.json").read_text(encoding="utf-8")))
    provenance["foundations_lessons"].append(json.loads((COURSE/"src/YM-F07-provenance.json").read_text(encoding="utf-8")))
    provenance["foundations_lessons"].append(json.loads((COURSE/"src/YM-F08-provenance.json").read_text(encoding="utf-8")))
    provenance["foundations_lessons"].append(json.loads((COURSE/"src/YM-F09-provenance.json").read_text(encoding="utf-8")))
    provenance["foundations_lessons"].append(json.loads((COURSE/"src/YM-F10-provenance.json").read_text(encoding="utf-8")))
    provenance["foundations_lessons"].append(json.loads((COURSE/"src/YM-F11-provenance.json").read_text(encoding="utf-8")))
    provenance["foundations_lessons"].append(json.loads((COURSE/"src/YM-F12-provenance.json").read_text(encoding="utf-8")))
    provenance["foundations_lessons"].append(json.loads((COURSE/"src/YM-F13-provenance.json").read_text(encoding="utf-8")))
    provenance["foundations_lessons"].append(json.loads((COURSE/"src/YM-F14-provenance.json").read_text(encoding="utf-8")))
    provenance["foundations_lessons"].append(json.loads((COURSE/"src/YM-F15-provenance.json").read_text(encoding="utf-8")))
    provenance["foundations_lessons"].append(json.loads((COURSE/"src/YM-F16-provenance.json").read_text(encoding="utf-8")))
    provenance["foundations_lessons"].append(json.loads((COURSE/"src/YM-F17-provenance.json").read_text(encoding="utf-8")))
    provenance["foundations_lessons"].append(json.loads((COURSE/"src/YM-F18-provenance.json").read_text(encoding="utf-8")))
    provenance["in_progress_lessons"]=[]
    provenance["proof_scope"]="Eighteen complete foundations lessons cover fields, electromagnetism, matrices, Lie theory, connections, bundles, action, constraints, classical evolution, Euclidean instantons, free quantum fields, quantum gauge symmetry, renormalization, finite lattice theory, quantitative sampling, spectral/source comparisons and continuum reconstruction. Unit 9 includes the complete local and global proofs in their stated regular and energy-data classes, with 36 analytic chapters. Unit 10 supplies the explicit instanton, sphere geometry and exact analytical operators. Unit 11 gives the full free quantum construction with exact domains and spectra. Unit 12 supplies quantum gauge constraints, finite gauge fixing, BRST and proved finite Ward identities. Unit 13 supplies the one-loop coefficient, heat proof, spectral subtraction and scale maps. Unit 14 constructs the finite Wilson measure, full spacing comparison, transfer operator and Hamiltonian. Unit 15 supplies exact loop, sampling and finite-error proofs. Unit 16 constructs spectral measures, source-sector maps and regulator limits. Unit 17 supplies the Gaussian continuum measure, reconstructed fields and exact regulator-state comparisons. Unit 18 connects established approaches through complete two-dimensional holonomy, face-constraint and finite effective-action comparisons. Four retained treatments preserve their original scope."
    writej(COURSE/"provenance.json",provenance)
    render(COURSE/"src/CURRICULUM.md","Yang–Mills theory: a route from the foundations","curriculum.html")
    stages=[]
    for unit in course["units"]:
        if unit["stage"] not in stages: stages.append(unit["stage"])
    sequence="".join("<li><strong>"+html.escape(stage)+"</strong>: "+html.escape("; ".join(u["title"] for u in course["units"] if u["stage"]==stage))+".</li>" for stage in stages)
    intro="<p>Begin with fields, electromagnetism and symmetry. Build the geometry and classical dynamics, then the quantum foundations needed to understand Yang–Mills theory and its literature.</p><p>The course has eighteen units, with mathematical preparation introduced in stages. The eighteen full lessons are complete. Sources are selected for their relevance, reliability and teaching value. No research project determines the course’s answer or receives a reserved place.</p><h2>Start reading</h2><p><a href=\"fields-coordinates-quantities.html\">1. Fields, coordinates and physical quantities</a> — scalar and vector fields, units, derivatives, coordinate changes, initial data, an exactly solved transport equation, and eight exercises with full solutions.</p><p><a href=\"electromagnetism-gauge-freedom.html\">2. Electromagnetism and gauge freedom</a> — fields and sources, Maxwell equations, potentials, local and global gauge questions, waves, energy flux, and eight exercises with full solutions.</p><p><a href=\"symmetry-through-matrices.html\">3. Symmetry through matrices</a> — complex phases, matrix arithmetic, unitary actions, changing frames, electromagnetic covariance, global gauge classes, and eight exercises with full solutions.</p><p><a href=\"lie-groups-and-lie-algebras.html\">4. Lie groups and Lie algebras</a> — convergent matrix series, local coordinates, tangent generators, SU(2) and SU(3), rotation coverings, invariant inner products, and eight exercises with full solutions.</p><p><a href=\"covariant-derivatives-and-curvature.html\">5. Covariant derivatives and curvature</a> — local frames, complete curvature formulas, differential forms, Bianchi, electromagnetic conventions, nonabelian examples, and eight exercises with full solutions.</p><p><a href=\"bundles-transport-holonomy.html\">6. Bundles, parallel transport and holonomy</a> — overlapping frames, exact transport, Wilson loops, curvature variations, the Hopf bundle, and eight exercises with full solutions.</p><p><a href=\"action-and-field-equations.html\">7. The Yang–Mills action and field equations</a> — metrics, full variations and boundary terms, Maxwell comparison, scalar matter and current, and eight exercises with full solutions.</p><p><a href=\"constraints-initial-data-energy.html\">8. Constraints, initial data and energy</a> — Gauss constraint, actual temporal gauge, full stress and energy derivations, matter exchange, boundary flux, and eight exercises with full solutions.</p><p><a href=\"local-and-global-classical-evolution.html\">9. Local and global classical evolution</a> — Fourier and Sobolev preparation, local construction, constraints, finite propagation, the complete heat and wave analysis, regular continuation, global finite-energy evolution in its stated class, and eight main exercises with full solutions. Thirty-six linked analysis chapters supply the full proof and 289 additional solutions.</p><p><a href=\"euclidean-yang-mills-instantons.html\">10. Euclidean Yang–Mills and instantons</a> — Hodge star, self-duality, the exact action bound, explicit instanton, smooth sphere bundle, charge, gauge classes, eight main solutions and a complete operator companion with four additional solutions.</p><p><a href=\"oscillators-and-free-quantum-fields.html\">11. Oscillators and free quantum fields</a> — states, probabilities, exact oscillator solution, finite Fourier modes, Fock space, vacuum energies, zero modes, domains, spectra and eight complete solutions.</p><p><a href=\"quantum-gauge-symmetry.html\">12. Quantum gauge symmetry</a> — physical states, exact finite constraints, compact-group averaging, gauge slices, ghosts, BRST, finite Ward identities and eight complete solutions.</p><p><a href=\"renormalization-and-asymptotic-freedom.html\">13. Renormalization and asymptotic freedom</a> — exact gauge and ghost coefficient, heat-kernel proof, subtraction, scale maps and eight complete solutions.</p><p><a href=\"yang-mills-on-a-lattice.html\">14. Yang–Mills theory on a lattice</a> — original Wilson action, quantified spacing error, finite Haar measure, positive transfer, spectral logarithm, reflection and eight complete solutions.</p><p><a href=\"strong-coupling-simulations-errors.html\">15. Strong coupling, simulations and their errors</a> — exact Wilson loops, controlled strong coupling, finite-volume and spacing bounds, correct sampling, autocorrelation and eight complete solutions.</p><p><a href=\"spectra-mass-gaps-confinement.html\">16. Spectra, mass gaps and confinement</a> — exact spectral measures, vacuum subtraction, physical units, charged-source maps, screening, regulator limits and eight complete solutions.</p><p><a href=\"continuum-limits-and-reconstruction.html\">17. Continuum limits and reconstruction</a> — actual Gaussian measure, reflection quotient, fields and domains, state maps, exact infrared limits and eight complete solutions.</p><p><a href=\"established-approaches-and-open-problems.html\">18. The established research landscape and open problems</a> — methods, original-source comparisons, full two-dimensional and finite constructions, and eight complete solutions.</p><h2>The route through the subject</h2><ol>"+sequence+"</ol><p><a href=\"curriculum.html\">Read the lesson plan and learning outcomes</a> · <a href=\"preparation.html\">Preparation</a> · <a href=\"literature-map.json\">Initial literature map</a></p><p>The eighteen-unit foundations-first sequence is complete. <a href=\"retained-materials.html\">Four earlier standalone treatments</a> remain accessible; their inclusion in this sequence has not been decided.</p>"
    (COURSE/"index.html").write_text(short_page(course["title"],intro),encoding="utf-8",newline="\n")
    prep="<p>Start with basic algebra, elementary calculus and matrix arithmetic. The first lessons review fields, coordinates, derivatives, physical quantities and electromagnetism. Matrix groups and their Lie algebras follow, before connections and bundles.</p><p>Geometry, Fourier and Sobolev analysis, Hilbert spaces and quantum mechanics enter through staged prerequisite components. Their exact provider statements and proofs must match the receiving lesson. No workbench construction is an entry prerequisite.</p><p>The <a href=\"curriculum.html\">full plan</a> gives learning outcomes and the subject sequence. The eighteen lessons are complete. Begin with <a href=\"fields-coordinates-quantities.html\">fields, coordinates and physical quantities</a>. Lesson 3 supplies the matrix and complex-number preparation and reuses the complete RT-LIE commutator argument with exact attribution. Lesson 4 constructs the local matrix-group charts and Lie-algebra maps, with exact comparisons to Etingof and the compact-group course. Lesson 5 supplies the required local exterior calculus and connection formulas, with exact DG-FND comparisons. Lesson 6 supplies complete bundle, transport and holonomy constructions with exact geometry-source comparisons. Lesson 7 proves the metric and variational prerequisites for the action, its field equations, boundary terms and scalar matter coupling. Lesson 8 derives the initial-data constraints, constructs temporal gauge, and proves stress-energy, local flux and total energy identities. Lesson 9 supplies Fourier and Sobolev preparation and complete classical local and global evolution proofs. Lesson 10 constructs the Euclidean instanton, its smooth sphere bundle, exact characteristic charge and operator comparison. Lesson 11 develops states and probabilities, the harmonic oscillator and the free scalar field, including zero modes, operator domains and spectral sets. Lesson 12 constructs the compact-group projection, finite constraints and gauge slices, Grassmann determinants, BRST algebra and finite Ward identities. Lesson 13 derives the full one-loop coefficient and its regulator and scale comparisons. Lesson 14 constructs lattice fields, the finite measure, physical transfer, fixed-regulator spectrum and reflection form. Lesson 15 derives exact plaquette laws, controlled expansions, correct samplers and quantitative errors. Lesson 16 proves spectral measures, threshold extraction, static-source comparisons and explicit regulator limits. Lesson 17 constructs the continuum free field, its reflection quotient, Hamiltonian, observables and regulator maps. Lesson 18 connects established approaches and open problems through complete calculations and eight solved exercises.</p><p>The <a href=\"retained-materials.html\">earlier standalone texts</a> keep their own dependencies and original lesson numbers. Those numbers record their editions, not the new course order.</p>"
    (COURSE/"preparation.html").write_text(short_page("Preparation",prep),encoding="utf-8",newline="\n")
    olditems="".join('<li><a href="'+u["reader"]+'">'+html.escape(u["id"]+": "+u["title"])+'</a></li>' for u in course["retained_materials"])
    oldbody="<p>These four existing texts remain available with their complete proofs, exercises and source references. They are retained materials, not the selected starting sequence. Earlier next-lesson remarks describe their original development order.</p><p>Any future reuse is assessed by the same criteria as other literature. No text has a reserved place in the course. See the <a href=\"curriculum.html\">general lesson plan</a>.</p><ol>"+olditems+"</ol>"
    (COURSE/"retained-materials.html").write_text(short_page("Retained standalone material",oldbody),encoding="utf-8",newline="\n")
    downloads=COURSE.parents[1]/"downloads"
    downloads.mkdir(exist_ok=True,parents=True)
    with zipfile.ZipFile(downloads/"yang-mills-geometry-and-states.zip","w",zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(COURSE.rglob("*")):
            if not path.is_file() or "__pycache__" in path.parts:continue
            data=path.read_bytes()
            if path.suffix==".html":
                data=data.replace(b'href="../../downloads/yang-mills-geometry-and-states.zip">Source and reader download',b'href="index.html">Offline course contents')
                data=data.replace(b'href="../../downloads/yang-mills-geometry-and-states.zip">Download',b'href="index.html">Offline course contents')
            info=zipfile.ZipInfo(path.relative_to(COURSE.parents[2]).as_posix(),date_time=(2026,10,8,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED
            archive.writestr(info,data)
        info=zipfile.ZipInfo("README.txt",date_time=(2026,10,8,0,0,0))
        archive.writestr(info,"Open docs/courses/YM-GAUGE/index.html in a current browser. The eighteen foundations lessons, their included analysis chapters and prerequisites, and four retained native MathML readers work offline. Rebuild with Python, BeautifulSoup4, NumPy, Matplotlib and Pandoc: python docs/courses/YM-GAUGE/build/build_course.py. All mathematical text, exercises, solutions, figures and original builder source: CC0 1.0.\n")
    print(json.dumps({"lesson1_formulas":len(formulas1),"lesson2_formulas":len(formulas2),"lesson3_formulas":len(formulas3),"lesson4_formulas":len(formulas4),"foundations1_formulas":len(formulasf1),"foundations2_formulas":len(formulasf2),"foundations3_formulas":len(formulasf3),"foundations4_formulas":len(formulasf4),"foundations5_formulas":len(formulasf5),"foundations6_formulas":len(formulasf6),"foundations7_formulas":len(formulasf7),"foundations8_formulas":len(formulasf8),"foundations9_formulas":len(formulasf9),"foundations10_formulas":len(formulasf10),"foundations11_formulas":len(formulasf11),"foundations12_formulas":len(formulasf12),"foundations13_formulas":len(formulasf13),"foundations14_formulas":len(formulasf14),"foundations15_formulas":len(formulasf15),"foundations16_formulas":len(formulasf16),"foundations17_formulas":len(formulasf17),"foundations18_formulas":len(formulasf18),"available_core_lessons":course["available_core_lessons"],"available_lessons":course["available_lessons"],"solved_exercises":course["solved_exercises"]}))

if __name__=="__main__":
    build()
