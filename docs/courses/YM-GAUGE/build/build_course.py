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
                x["c"][1] = x["c"][1].replace(r"\hbox", r"\text")
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
            assert all(child is node or (isinstance(child, str) and not child.strip()) for child in parent.contents)
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
        toc += '<li><a href="#' + h["id"] + '">' + html.escape(re.sub(r"^\d+\.\s*", "", h.get_text())) + "</a></li>"
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

def short_page(title, body):
    return '<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(title)+'</title><link rel="stylesheet" href="reader.css"></head><body><nav><a href="index.html">Course contents</a><a href="../../downloads/yang-mills-geometry-and-states.zip">Download</a></nav><main><h1>'+html.escape(title)+'</h1>'+body+'</main><footer>Mathematical content: CC0 1.0.</footer></body></html>'

def writej(path,data):
    path.write_text(json.dumps(data,indent=2,ensure_ascii=False)+"\n",encoding="utf-8",newline="\n")

def build():
    # The first source and reader retain their delivered mathematics.
    figure()
    profile_figure()
    source1, formulas1=render(COURSE/"src/YM-01.md","Quaternionic colour maps","quaternionic-colour-maps.html")
    source2, formulas2=render(COURSE/"src/YM-02.md","Compact-support profiles, curvature and source","compact-support-profiles.html")
    course=json.loads((COURSE/"course.json").read_text(encoding="utf-8"))
    course.update(available_lessons=2,solved_exercises=12)
    course["units"][1].update(status="available",reader="compact-support-profiles.html",
        source="src/YM-02.md",source_sha256=digest((COURSE/"src/YM-02.md").read_bytes()),
        reader_sha256=digest((COURSE/"compact-support-profiles.html").read_bytes()),
        solution_count=7,internal_proof_dependencies=[{"lesson":"YM-01",
        "source_sha256":course["units"][0]["source_sha256"],
        "locators":"Sections 1–2: quaternion algebra, bracket and matrix metric; Theorem 6.1: full 24-dimensional quadratic map, fibres and derivative ranks.",
        "reader":"quaternionic-colour-maps.html"}],
        prerequisite_scope="YM-01; smooth functions, differentiation and integration by parts. The cutoff, all specialized field calculations, conservation, energy and correction identities are proved here.")
    for number in (6,7):
        course["units"][number]["status"]="planned"
        course["units"][number]["research_provider"]="Finite mathematical results available in PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md, PK1–PK54; teaching treatment forthcoming. No interacting continuum limit is asserted."
    writej(COURSE/"course.json",course)
    proof="https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/c1f29f3e6dfeb20e4be5254ea4fac7578255eacc/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/"
    provenance=json.loads((COURSE/"provenance.json").read_text(encoding="utf-8"))
    provenance["readings"]=[x for x in provenance["readings"] if x.get("lesson")!="YM-02"]
    for file,loc in [("PROOF.md","Sections 7–9: original profiles and colour map"),
        ("COMPACT_SUPPORT_CAUCHY_EVOLUTION.md","CE18–CE23 and Proposition 4.1: all energy coefficients and zero-energy set"),
        ("HIGHER_CARRIER_AND_EVOLUTION.md","HC14–HC20: initial acceleration, Gauss-preserving correction and exact residual")]:
        provenance["readings"].append({"lesson":"YM-02","url":proof+file,"locators":loc})
    provenance["proof_scope"]="YM-01 and YM-02 give complete specialized proofs, with YM-01's exact algebra and rank results used by YM-02. The later classical evolution and quantum continuum programme are not conclusions of these two lessons."
    writej(COURSE/"provenance.json",provenance)
    items=""
    for unit in course["units"]:
        label=html.escape(unit["title"])
        if unit.get("reader"):label='<a href="'+unit["reader"]+'">'+label+"</a>"
        else:label+=" — forthcoming"
        items+="<li>"+label+"</li>"
    intro="<p>Follow the exact maps from quaternionic colour coordinates to gauge profiles, classical evolution and physical-state constructions. The course retains the constants, metric comparisons, source terms and domain information needed to connect these subjects.</p><p>The first two lessons are available with twelve fully solved exercises. They establish the full quadratic colour map, compact-support fields, curvature, source, energy and initial correction. The remaining lessons are being developed. The continuum gapless-state construction remains an open research aim.</p><p><a href=\"preparation.html\">Preparation and proof routes</a> · <a href=\"src/YM-01.md\">Lesson 1 source</a> · <a href=\"src/YM-02.md\">Lesson 2 source</a> · <a href=\"provenance.json\">Sources and authorship</a></p><ol>"+items+"</ol>"
    (COURSE/"index.html").write_text(short_page(course["title"],intro),encoding="utf-8",newline="\n")
    prep="<p>Lesson 1 uses real-coordinate arithmetic, complex matrix multiplication and differentiation of polynomial expressions. It constructs quaternionic algebra and proves every group-action, fibre and rank statement it uses.</p><p>Lesson 2 uses these exact Lesson 1 results together with smooth multivariable calculus and integration by parts. It proves existence of the cutoff and every specialized curvature, source, conservation, energy and correction identity. Its seven solved exercises retain the full cutoff region and physical constants.</p><p>Later lessons require additional geometry, analysis and operator theory. Each will supply complete specialized proofs or use an exact earlier lesson with matching hypotheses. Planned teaching units are not available proof providers.</p><p><a href=\"quaternionic-colour-maps.html\">Lesson 1: Quaternionic colour maps</a> · <a href=\"compact-support-profiles.html\">Lesson 2: Compact-support profiles, curvature and source</a>.</p>"
    (COURSE/"preparation.html").write_text(short_page("Preparation and proof routes",prep),encoding="utf-8",newline="\n")
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
        archive.writestr(info,"Open docs/courses/YM-GAUGE/index.html in a current browser. Both native MathML readers work offline. Rebuild with Python, BeautifulSoup4 and Pandoc: python docs/courses/YM-GAUGE/build/build_course.py. All mathematical text, exercises, solutions, figures and original builder source: CC0 1.0.\n")
    print(json.dumps({"lesson1_formulas":len(formulas1),"lesson2_formulas":len(formulas2),"available_lessons":2,"solved_exercises":12}))

if __name__=="__main__":
    build()
