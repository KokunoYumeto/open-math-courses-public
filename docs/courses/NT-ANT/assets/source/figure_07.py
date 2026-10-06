"""Original CC0 diagram for NT-ANT-07; run with Python and matplotlib."""
from pathlib import Path
import json,hashlib,math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

HERE=Path(__file__).resolve().parent
out=HERE/"figures"
out.mkdir(exist_ok=True)
s=math.sqrt(2)
v1=(1,1);v2=(s,-s)
vertices=[(0,0),v1,(1+s,1-s),v2]
points=[(a+b*s,a-b*s) for a in range(-5,6) for b in range(-5,6)
        if max(abs(a+b*s),abs(a-b*s))<=3.4]
fig,ax=plt.subplots(figsize=(7,7),dpi=180)
fig.patch.set_facecolor("white")
ax.set_facecolor("white")
ax.add_patch(Polygon(vertices,closed=True,facecolor="#9ad7cc",edgecolor="#246e60",alpha=.65,lw=2))
ax.axhline(0,color="#92989c",lw=1)
ax.axvline(0,color="#92989c",lw=1)
ax.scatter([p[0] for p in points],[p[1] for p in points],s=45,color="#243b56",zorder=3)
ax.scatter([0],[0],s=65,color="#111827",zorder=4)
for v,color,label,pos in [(v1,"#b64a35",r"$j(1)=(1,1)$",(-.7,1.85)),
                         (v2,"#2862a4",r"$j(\sqrt{2})$",(2.3,-1.25))]:
    ax.annotate("",xy=v,xytext=(0,0),arrowprops={"arrowstyle":"->","color":color,"lw":3},zorder=5)
    ax.annotate(label,xy=v,xytext=pos,fontsize=22,color=color,
                arrowprops={"arrowstyle":"-","color":color,"lw":1},ha="center")
ax.text(1.15,-.32,r"$P$",fontsize=26,color="#194d43",ha="center",va="center")
ax.set_xlim(-3.4,3.4);ax.set_ylim(-3.4,3.4)
ax.set_aspect("equal",adjustable="box")
ax.set_xticks([-2,0,2]);ax.set_yticks([-2,0,2])
ax.tick_params(labelsize=21)
ax.grid(alpha=.15)
ax.set_xlabel(r"$\sigma_1(a+b\sqrt{2})=a+b\sqrt{2}$",fontsize=22,labelpad=12)
ax.set_ylabel(r"$\sigma_2(a+b\sqrt{2})=a-b\sqrt{2}$",fontsize=22,labelpad=12)
ax.set_title(r"$j(\mathbf{Z}[\sqrt{2}])$",fontsize=25,pad=12)
fig.subplots_adjust(left=.17,bottom=.17,right=.96,top=.87)
target=out/"minkowski-sqrt2.png"
fig.savefig(target,metadata={})
plt.close(fig)
# Remove metadata without changing pixels. No private paths or timestamps in public bytes.
data=target.read_bytes();offset=8;chunks=[data[:8]]
while offset<len(data):
    length=int.from_bytes(data[offset:offset+4],"big");kind=data[offset+4:offset+8]
    end=offset+length+12
    if kind not in {b"tEXt",b"zTXt",b"iTXt",b"eXIf",b"tIME"}:chunks.append(data[offset:end])
    offset=end
target.write_bytes(b"".join(chunks))
data=target.read_bytes()
record={
 "id":"minkowski-sqrt2","path":"../assets/minkowski-sqrt2.png",
 "source":"assets/minkowski-sqrt2.png","source_sha256":hashlib.sha256(data).hexdigest().upper(),
 "media_type":"image/png","bytes":len(data),"width":int.from_bytes(data[16:20],"big"),
 "height":int.from_bytes(data[20:24],"big"),
 "authorship":{"kind":"original","credit":"GPT-6.1 Sol (OpenAI), Codex, Ultra",
              "statement":"Original CC0 plot generated from the two real embeddings and the exact lattice basis. No source figure was copied."},
 "source_attribution":["NT-ANT-07, Proposition 7.2 and the Q(sqrt2) example; exact vertices 0, (1,1), (sqrt2,-sqrt2), (1+sqrt2,1-sqrt2).",
                       "Milne, Algebraic Number Theory, Proposition 4.26; Neukirch, Algebraic Number Theory, I (5.2), for the covolume theorem."]
}
(HERE/"figure_07.json").write_text(json.dumps(record,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"status":"generated","sha256":record["source_sha256"],"dimensions":[record["width"],record["height"]],"points":len(points)}))
