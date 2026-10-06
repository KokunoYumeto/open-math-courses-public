"""CC0 exact module-map schematic for Lemma 11.7, (H.38)--(H.42)."""
from pathlib import Path
import json
import hashlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

out = Path(__file__).resolve().parent
ink, teal, rust, bg = "#26364e", "#00798a", "#b25315", "#fbfcfe"
plt.rcParams.update({"font.family": "DejaVu Sans", "mathtext.fontset": "dejavusans",
                     "svg.fonttype": "none", "svg.hashsalt": "gaussian-compression-v1"})
fig = plt.figure(figsize=(16, 10.5), facecolor=bg)
ax = fig.add_axes([.045, .12, .91, .73]); ax.axis("off")
ax.set_xlim(0, 1); ax.set_ylim(0, 1)

def card(x, y, w, h, title, lines, color=teal):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.012,rounding_size=.018",
                              facecolor="#eef5f8",edgecolor="#d4dfe8",linewidth=1.2))
    ax.text(x+.02,y+h-.035,title,va="top",fontsize=18,weight="bold",color=color)
    for dy, line, size in lines:
        ax.text(x+.02,y+h-dy,line,va="top",fontsize=size,color=ink)

card(.01,.59,.38,.34,"The whole standard right module",[
    (.12,r"$V:A\longrightarrow E,\quad V^*V=1_A$",22),
    (.20,r"$(Vk)(u,y,x)=g_u(y)k(u,x)$",20),
    (.275,"Even; all H* and H phases evaluated",15)])
card(.60,.59,.38,.34,"The represented reverse tensor",[
    (.12,r"$E=\mathcal{H}_W\widehat{\otimes}_C\mathscr{E}_S$",23),
    (.20,r"$P=VV^*,\quad \pi(a)\text{ changes }u$",19),
    (.275,"y stays fixed; right convolution changes x",15)])
ax.annotate("",xy=(.59,.76),xytext=(.41,.76),arrowprops={"arrowstyle":"->","lw":2.5,"color":teal})
ax.text(.50,.80,"V",ha="center",fontsize=22,color=teal)
ax.annotate("",xy=(.41,.65),xytext=(.59,.65),arrowprops={"arrowstyle":"->","lw":2.5,"color":teal})
ax.text(.50,.605,r"$V^*$",ha="center",fontsize=21,color=teal)
card(.01,.22,.97,.27,"Compression and its positive multiplicative defect",[
    (.095,r"$\Phi(a)=V^*\pi(a)V=M_\kappa(a),\quad \kappa(d)=\langle g_u,g_{u'}\rangle$",23),
    (.17,r"$\Phi(a^*a)-\Phi(a)^*\Phi(a)=[(1-P)\pi(a)V]^*[(1-P)\pi(a)V]$",22)],rust)
ax.text(.02,.145,r"$\pi(a)V=T_{\zeta_a}\in\mathcal{K}_A(A,E),\quad \zeta_a(u,y,x)=a(u,x)g_x(y)$",fontsize=22,color=teal)
ax.text(.02,.065,"Localized Gaussian blocks are compact. The defect can be nonzero; the Gaussian line is not left invariant.",fontsize=17,color=rust)

fig.suptitle("The Gaussian right module retains a nontrivial left-action defect",fontsize=23,color=ink,weight="bold",y=.966)
fig.text(.5,.895,r"$g_u(y)=Z^{-1/2}e^{-d(y,u)^2/2}\,\mathrm{vol}_y$; complete curvature −1 disks; full calibrated W and S",
         ha="center",fontsize=18,color=ink)
fig.text(.045,.085,"Proof: Lemma 11.7, (H.38)–(H.42). Exact module maps; schematic placement, not a metric embedding.",fontsize=13,color=ink)
fig.text(.045,.055,"Human context: Connes, Survey §12; Connes–Skandalis, longitudinal product; Kasparov, Clifford method.",fontsize=13,color=ink)
fig.text(.045,.025,"Original CC0 diagram. The Gaussian defect and compact-block proof are supplied in Lemma 11.7; no reverse identity is asserted.",fontsize=12.5,color=ink)
names=[]
for ext in ("png", "svg"):
    name="kt-hyperbolic-gaussian-compression."+ext
    if ext=="svg":
        fig.savefig(out/name,metadata={"Title":"The Gaussian right module and its convolution defect",
                    "Creator":"Matplotlib; original CC0 mathematical illustration","Date":None,
                    "Rights":"CC0 1.0","Description":"Exact Hilbert-module map schematic for Lemma11.7, H.38-H.42."})
    else:
        fig.savefig(out/name,dpi=180)
    names.append(name)
plt.close(fig)
(out/"gaussian-compression-receipt.json").write_text(json.dumps({"license":"CC0 1.0",
    "proof_locators":["Lemma 11.7","H.38","H.39","H.40","H.41","H.42"],
    "placement":"schematic module maps; no metric embedding","reverse_identity_asserted":False,
    "sha256":{n:hashlib.sha256((out/n).read_bytes()).hexdigest().upper() for n in names}},indent=2)+"\n",encoding="utf-8")
print(json.dumps({"rendered":names,"reverse_identity_asserted":False}))
