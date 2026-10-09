"""Reproduce exact frequency geometry and certified product samples."""
from pathlib import Path
from tempfile import TemporaryDirectory
import json, math, os
ROOT=Path(__file__).resolve().parent
with TemporaryDirectory(prefix="an02-own249-mpl-")as temp:
 os.environ["MPLCONFIGDIR"]=temp
 import matplotlib
 matplotlib.use("Agg")
 import matplotlib.pyplot as plt
 import numpy as np
 import mpmath as mp
 from matplotlib.patches import Circle
 mp.mp.dps=85
 plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,"svg.hashsalt":"reciprocal-cone-249","axes.spines.top":False,"axes.spines.right":False})
 out=ROOT/"figures";out.mkdir(exist_ok=True)
 def save(fig,name):
  fig.savefig(out/(name+".png"),dpi=160,bbox_inches="tight",pad_inches=.15,metadata={"Software":"Open Mathematics Courses"})
  fig.savefig(out/(name+".svg"),bbox_inches="tight",pad_inches=.15,metadata={"Date":None,"Creator":"Open Mathematics Courses"})
  plt.close(fig)
 xi=40.;r=64.;d=1/8
 beta=1+math.log(3)/math.log(2);D=4*beta+1
 assert r>D*math.log(2+math.hypot(xi,r))
 fig,axes=plt.subplots(1,2,figsize=(13.8,5.4),layout="constrained")
 for a,normalized in zip(axes,[False,True]):
  xx=np.linspace(-25,120,701); yy=np.linspace(-8,94,601)
  X,Y=np.meshgrid(xx,yy)
  region=Y>np.log(2+np.hypot(X,Y))
  if normalized:
   XP=(X-xi)/r;YP=Y/r;center=(0,1);radius=2*d;witness=math.log(42)/r
   a.set(xlim=(-.9,1.25),ylim=(-.14,1.48),xlabel="Re w",ylabel="Im w",title="Normalized: w = (z − 40) / 64")
  else:
   XP=X;YP=Y;center=(xi,r);radius=r*2*d;witness=math.log(42)
   a.set(xlim=(-25,120),ylim=(-8,94),xlabel="Real frequency ξ",ylabel="Imaginary frequency η",title="Original frequency z = ξ + iη")
  a.contourf(XP,YP,region.astype(int),levels=[.5,1.5],colors=["#ddecff"],alpha=.85)
  a.contour(XP,YP,Y-np.log(2+np.hypot(X,Y)),levels=[0],colors=["#3d73a4"],linewidths=1)
  a.add_patch(Circle(center,radius,edgecolor="#216b43",facecolor="#cfe9d5",alpha=.85,lw=1.6))
  a.scatter(*center,c="#174e31",s=35,zorder=5)
  real_center=0 if normalized else xi
  a.plot([real_center-witness,real_center+witness],[0,0],c="#8c519c",lw=6,solid_capstyle="butt",zorder=5)
  a.annotate("real witness interval",xy=(real_center,0),xytext=(.26,.09 if normalized else 12),textcoords="data",fontsize=10,arrowprops={"arrowstyle":"->","color":"#8c519c"}) if normalized else a.annotate("real witness interval",xy=(real_center,0),xytext=(52,15),fontsize=10,arrowprops={"arrowstyle":"->","color":"#8c519c"})
  zeros=[(4*math.pi*k,-2*math.log(1.5))for k in range(-2,10)]
  zx=[(x-xi)/r if normalized else x for x,y in zeros];zy=[y/r if normalized else y for x,y in zeros]
  a.scatter(zx,zy,marker="x",c="#ac382e",s=26,zorder=4)
  a.annotate("target i"if normalized else "target 40 + 64i",xy=center,xytext=(center[0]+radius*.85,center[1]+radius*.75),fontsize=10)
  a.text(center[0],center[1]-radius*.75,"harmonic ball",ha="center",fontsize=10)
  a.axhline(0,c="#7c8185",lw=.6);a.grid(alpha=.15);a.set_aspect("equal",adjustable="box")
 save(fig,"frequency-normalization-and-harmonic-ball")
 eta=np.linspace(0,12,401)
 fig,axes=plt.subplots(1,2,figsize=(13.8,5.2),layout="constrained")
 axes[0].plot(eta,1/(1.5-np.exp(-eta/2)),label="ξ = 0: exact upper endpoint",color="#205a98")
 axes[0].plot(eta,1/(1.5+np.exp(-eta/2)),label="ξ = 2π: exact lower endpoint",color="#31754b")
 axes[0].axhline(2/3,ls="--",c="#7e6a8d",label="limit 2/3")
 axes[0].set(xlabel="η ≥ 0",ylabel="exp(−η/4) × |1/F(ξ+iη)|",title="Two-atom inverse: sharp rate exp(η/4)")
 axes[0].legend(fontsize=9);axes[0].grid(alpha=.15)
 samples=[]
 for J in range(4,49):
  R=mp.mpf(2)**J;z=R+6j*mp.log(R+2);K=J+120
  logp=mp.fsum(mp.log(abs(mp.sin(z/mp.mpf(2)**j)/(z/mp.mpf(2)**j)))for j in range(1,K+1))
  s=mp.exp(mp.mpf(".5"))*abs(z)**2*mp.mpf(4)**(-K)/18
  bound=6*mp.log(R+2)-mp.log(2)*J*(J-1)/2
  assert 2*s<mp.mpf(2)**-240
  samples.append(dict(J=J,K=K,R=str(R),imaginary=str(mp.im(z)),log_finite_product=str(logp),proved_upper_bound=str(bound),relative_tail_bound=str(2*s)))
 js=[x["J"]for x in samples]; vals=[float(x["log_finite_product"])for x in samples];bounds=[float(x["proved_upper_bound"])for x in samples]
 axes[1].plot(js,vals,"o-",ms=3,c="#205a98",label="certified product samples")
 axes[1].plot(js,bounds,c="#a56b28",label="proved upper bound")
 axes[1].plot(js,[-10*math.log(2**J+2)for J in js],":",c="#7e6a8d",label="comparison −10 log(R+2)")
 axes[1].set(xlabel="J, with R = 2^J and η = 6 log(R+2)",ylabel="natural logarithm of modulus",title="Smooth compact kernel: zero-free is insufficient")
 axes[1].legend(fontsize=9);axes[1].grid(alpha=.15)
 save(fig,"exponential-rate-and-smooth-counterexample")
 geometry=dict(schema="AN02-reciprocal-geometry249/v1",normalization=dict(xi=40,r=64,d="1/8",D0=1,D=D,witness_radius=math.log(42),original_harmonic_ball_radius=16,normalized_harmonic_ball_radius=.25,zeros="4πk − 2i log(3/2), k ∈ Z; markers k=−2,...,9",region="η > log(2+sqrt(ξ^2+η^2))",dimension=1),atomic_parameters=dict(a="-3/4",b="1/2",lam="3/2",growth_rate="1/4"),product_parameters=dict(d=6,J_first=4,J_last=48,K="J+120",uniform_relative_tail_bound="2^(-240)"),product_samples=samples)
 (out/"geometry249.json").write_text(json.dumps(geometry,indent=2)+"\n",encoding="utf-8")
 print(json.dumps(dict(figures=2,product_samples=len(samples),rigorous_relative_tail_bound="2^(-240)",owned_MPL_temporary_directory_removed_on_exit=True)))
