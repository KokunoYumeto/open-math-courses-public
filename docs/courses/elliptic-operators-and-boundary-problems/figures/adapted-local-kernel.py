"""Reproduce the exact local inverse and strict-domain proof diagram."""
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
out=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(13,8.8));ax.set(xlim=(0,13),ylim=(0,8.8));ax.axis("off")
ax.text(6.5,8.5,"The full multiplier controls both local regularity and its exact domain",ha="center",fontsize=15,weight="bold")
ax.text(6.5,8.08,r"$P_{r,m}=I+D_x^{2r}+D_y^{2m},\quad p=1+\xi^{2r}+\eta^{2m},\quad q=p^{-1},\quad 1\leq r<m$",ha="center",fontsize=14)
def box(x,y,w,h,title,lines,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.1",fc=color,ec="#547489",lw=1.2))
    ax.text(x+w/2,y+h-.3,title,ha="center",va="center",fontsize=12,weight="bold",color="#183d53")
    for i,(line,fs) in enumerate(lines):ax.text(x+w/2,y+h-.78-i*.43,line,ha="center",va="center",fontsize=fs)
box(.35,4.7,5.9,2.75,"Actual reciprocal derivatives and Fourier shifts",[
 (r"$|\partial_\xi^a\partial_\eta^bq|\leq C_{a,b}p^{-1-a/(2r)-b/(2m)}$",13),
 (r"$\Delta_kq(k,\ell)=q(k-1,\ell)-q(k,\ell)$",12),
 (r"$(e^{ix}-1)^NK_Q=(2\pi)^{-2}\sum\Delta_k^Nq\,e^{i(kx+\ell y)}$",12),
 ("The identical y-shift retains the same full reciprocal.",11),
 ("AH26–AH31: every shift, sign and Fourier factor remains.",10)],"#edf4f9")
box(6.75,4.7,5.9,2.75,"Smooth kernel away from the torus origin",[
 (r"$\rho=r/m>0,\quad 2r+\rho N>d+2$",13),
 ("Both shifted series have d continuous derivatives.",11),
 (r"$(x,y)\neq(0,0)$ modulo $2\pi$",13),
 (r"$e^{ix}-1\neq0\quad\mathrm{or}\quad e^{iy}-1\neq0$",13),
 ("Divide by that actual factor. Arbitrary d gives smoothness.",10)],"#eff6ed")
box(.35,1.27,5.9,2.75,"Local support and the exact inverse",[
 (r"$f=P_{r,m}w,\quad \chi=1\ \mathrm{near}\ \overline{V}\subset U$",13),
 (r"$w=Q(\chi f)+Q((1-\chi)f)$",14),
 ("Input (1−χ)f: supported away from V.",11),
 ("Q(χf) is smooth; Q((1−χ)f) is smooth on V.",11),
 ("E2: the output support may still meet V.",10)],"#f4f0f9")
box(6.75,1.27,5.9,2.75,"Two different axis distributions prove strictness",[
 (r"$\widehat u(N,0)=\langle N,0\rangle^{-\sigma-2r-1}$",13),
 (r"$u\in\mathcal{D}_\sigma(P_{r,m})\setminus H^{\sigma+2m}$",13),
 (r"$\widehat v(0,N)=\langle0,N\rangle^{-\sigma-2r-1}$",13),
 (r"$v\in H^{\sigma+2r}\setminus\mathcal{D}_\sigma(P_{r,m})$",13),
 ("AH22–AH24 retain both complete axis multipliers.",10)],"#faf2e9")
ax.annotate("",xy=(6.65,6.1),xytext=(6.38,6.1),arrowprops=dict(arrowstyle="->",color="#547489",lw=1.8))
ax.annotate("",xy=(3.3,4.1),xytext=(9.6,4.53),arrowprops=dict(arrowstyle="->",color="#547489",lw=1.5))
ax.text(6.5,.62,"Proof: Nonelliptic Fredholm operators on their exact adapted spaces, AH22–AH32 and E2/E6.",ha="center",fontsize=10)
ax.text(6.5,.27,r"E6: local $w\mapsto E_\eta w$, $(E_\eta w)(\varphi)=w(\eta\varphi|_U)$; $P_{r,m}E_\eta w|_W=P_{r,m}(w|_W)$.",ha="center",fontsize=10)
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
for ext in ["svg","png"]:fig.savefig(out/f"adapted-local-kernel.{ext}",dpi=180,facecolor="white")
plt.close(fig)
