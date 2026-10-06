"""Exact normal-root geometry for ND2--ND6; original CC0 figure."""
from pathlib import Path
import hashlib
import json
import matplotlib
matplotlib.use("Agg")
matplotlib.rcParams.update({"svg.hashsalt":"AN02-normal-root-distance-v1", "font.family":"DejaVu Sans", "font.size":15})
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

OUT = Path(__file__).resolve().parent
rows = [("1/2", .5, 2, "1/4"), ("1/4", .25, 4, "1/16"), ("1/8", .125, 8, "1/64")]
fig, axes = plt.subplots(1, 3, figsize=(18, 7), dpi=150)
for ax, (label, scale, radius, bound) in zip(axes, rows):
    ax.axhline(0, color="#aaa", linewidth=.8)
    ax.axvline(0, color="#aaa", linewidth=.8)
    ax.add_patch(Circle((0,0),1,facecolor="#dcecf8",edgecolor="#3673a0",alpha=.8))
    ax.scatter([-radius,radius],[0,0],c="#b33a2d",s=75,zorder=3)
    ax.scatter([0],[0],marker="x",c="#1b2633",s=65,zorder=4)
    for root in (-radius,radius):
        ax.annotate(f"zero {root:+d}",(root,0),xytext=(0,20),textcoords="offset points",ha="center",fontsize=14,color="#8d2821")
    ax.annotate("centre",(0,0),xytext=(0,-25),textcoords="offset points",ha="center",fontsize=13)
    ax.set(xlim=(-9.4,9.4),ylim=(-4,4),xlabel="Re z",ylabel="Im z",aspect="equal")
    ax.set_xticks([-8,-4,0,4,8]); ax.set_yticks([-2,0,2])
    ax.set_title(f"T = {label}; normal root radius = {radius}",fontsize=17,pad=20)
    ax.text(.5,-.32,rf"$p_T(z)=1-T^2z^2$"+f"\nexact unit-disc error = {bound}",transform=ax.transAxes,ha="center",va="top",fontsize=17)
fig.suptitle("A shrinking physical window moves every normalized normal zero outward",fontsize=23,y=.97)
fig.text(.5,.045,"Restriction B(t) = 1 - t²; N = 1; physical root distance = 1. Blue disc: |z| ≤ 1. Cross: centre, not a zero.",ha="center",fontsize=16)
fig.subplots_adjust(top=.82,bottom=.32,left=.06,right=.98,wspace=.25)
fig.savefig(OUT/"normal-root-distance.png",metadata={"Software":"AN02 original normal-root-distance renderer"},facecolor="white")
fig.savefig(OUT/"normal-root-distance.svg",metadata={"Date":None,"Creator":"GPT-6.1 Sol (OpenAI), Ultra; CC0"},facecolor="white")
plt.close(fig)
data = {"polynomial":"1-t^2","centre":0,"normal":1,"physical_root_distance":1,"test_disc_radius":1,"panels":[{"T":label,"normalized_roots":[-radius,radius],"exact_unit_disc_error":bound} for label,scale,radius,bound in rows]}
(OUT/"geometry.json").write_text(json.dumps(data,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"rendered":True,"png_sha256":hashlib.sha256((OUT/"normal-root-distance.png").read_bytes()).hexdigest().upper()}))
