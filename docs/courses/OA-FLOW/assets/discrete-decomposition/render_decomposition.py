"""Exact original proof diagram; no finite-dimensional type III model."""
from pathlib import Path
import argparse,json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--output-dir",type=Path,default=Path(__file__).resolve().parent/"assets")
    out=parser.parse_args().output_dir;out.mkdir(parents=True,exist_ok=True)
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":14,"svg.hashsalt":"oa-flow-original-dd-20261004","mathtext.fontset":"dejavusans"})
    fig=plt.figure(figsize=(16,12.5),dpi=200,facecolor="#f6f8fb")
    ax=fig.add_axes([.025,.025,.95,.95]);ax.set_xlim(0,100);ax.set_ylim(0,100);ax.axis("off")
    ink="#18334c";blue="#176ca2";green="#207255";orange="#b96313"
    def text(x,y,s,size=14,color=ink,ha="left",va="center"):
        ax.text(x,y,s,fontsize=size,color=color,ha=ha,va=va)
    def box(x,y,w,h,title,body,color=blue):
        ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=.5,rounding_size=1.0",edgecolor=color,facecolor="white",lw=1.6))
        text(x+w/2,y+h-2.7,title,15,color,ha="center")
        text(x+w/2,y+h/2-1.2,body,13,ha="center")
    def arrow(x1,y1,x2,y2,color=blue):
        ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle="-|>",mutation_scale=18,lw=1.7,color=color))
    text(1,97,"An actual discrete decomposition from the type parameter",22)
    text(1,93.6,r"$M\ne0,\ M_*\ {\rm separable},\ M\ {\rm type\ III},\ S(M)=\{0\}\cup\lambda^{\mathbb{Z}},\quad 0<\lambda<1$",15)
    text(1,89.8,"A. Every intermediate hypothesis is constructed   [DD1–5]",16)
    box(1,74,20,13,"Faithful state",r"$\psi=\sum_{j\geq1}2^{-j}\omega_j$"+"\nnormal, positive, faithful")
    box(26,74,20,13,"Inner → periodic",r"$P=\frac{2\pi}{-\log\lambda}$"+"\n"+r"$\sigma_P^\psi={\rm Ad}\,b$"+"\n"+r"$\eta=\psi_{e^{-\Theta/P}}$")
    box(51,74,20,13,"Infinite on M",r"$\phi(x)=\sum_{j\geq0}\eta(v_j^*xv_j)$"+"\n"+r"$\phi(1)=\infty,\ \sigma_P^\phi=1$")
    box(76,74,22,13,"Scaling / regular",r"$N=M_\phi\ {\rm II}_\infty$"+"\n"+r"$\tau\theta=\lambda\tau$"+"\n"+r"$N\rtimes_\theta\mathbb{Z}\cong M$")
    for x in [21.6,46.6,71.6]:arrow(x,80.5,x+3.7,80.5)
    text(10.5,71.5,"CP / local proof",12,ha="center")
    text(36,71.5,"IP + PW",12,ha="center")
    text(61,71.5,"CA full graphs",12,ha="center")
    text(87,71.5,"PF + GT onto W",12,ha="center")
    ax.plot([1,98],[68,68],color="#ccd7e2")
    text(1,65,"B. The complete spectral coordinates   [DD6–7]",16)
    text(1,61.3,r"$W(\delta_n\otimes\Lambda_\tau(x))=\Lambda_\phi(U^n x),\quad x\in\mathfrak{n}_\tau,\qquad \mathcal{K}=\ell^2(\mathbb{Z},H_\tau)$",15)
    xs=[12+12*j for j in range(7)];ns=list(range(-3,4))
    for x,n in zip(xs,ns):
        box(x-4.5,47.3,9,9.0,r"$H_\tau$",r"$n="+str(n)+"$",blue)
        val={-3:"8",-2:"4",-1:"2",0:"1",1:r"\frac{1}{2}",2:r"\frac{1}{4}",3:r"\frac{1}{8}"}[n]
        text(x,58.3,r"$2^{-n}="+val+"$",14,ha="center")
    for j in range(6):arrow(xs[j]+4.8,51.8,xs[j+1]-4.8,51.8,green)
    text(2,51.8,r"$\cdots$",19,ha="center");text(97,51.8,r"$\cdots$",19,ha="center")
    text(49,44.7,r"$W^*\pi_\phi(U)W:\ n\mapsto n+1\quad\mathrm{(no\ norm\ scaling)}$",14,green,ha="center")
    text(1,41.2,r"$T=W^*\Delta_\phi W=\bigoplus_n\lambda^n I,\qquad D(T)=\{\xi:\sum_n\lambda^{2n}\|\xi_n\|^2<\infty\}$",15)
    text(1,37.8,r"$\operatorname{Sp}(T)=\{0\}\cup\lambda^{\mathbb{Z}},\qquad\ker T=0:\quad \|T(\delta_n\otimes\zeta)\|=\lambda^n\to0$",15)
    text(1,34.5,"Shown values use λ = 1/2. Equal horizontal steps are integer degrees; both tails are infinite.",12)
    ax.plot([1,98],[31.8,31.8],color="#ccd7e2")
    text(1,29,"C. Full domains, not finite truncations   [DD9]",16)
    text(1,25.7,r"$\|\zeta\|=1,\quad \lambda=\frac{1}{2},\quad k\geq1$",14)
    box(1,10,46,13,r"$\xi_{-k}=2^{-k}\zeta$",
        r"$\|\xi\|^2=\frac{1}{3},\qquad\sum_k\|T\xi_{-k}\|^2=\infty$"+"\n"+r"$\xi\in D(\log T),\qquad \xi\notin D(T)$",orange)
    box(52,10,46,13,r"$\eta_k=2^{-k}\zeta$",
        r"$\|T\eta\|^2=\frac{1}{15},\qquad\sum_k\|T^{-1}\eta_k\|^2=\infty$"+"\n"+r"$\eta\in D(T),\qquad\eta\notin D(T^{-1})$",orange)
    text(1,6.4,r"Double dual [DD8]:  $\Phi:D\cong N\bar\otimes B(\ell^2\mathbb{Z}),\quad \Phi\beta_m\Phi^{-1}=\theta^m\bar\otimes{\rm Ad}(S^{-m})$",13)
    text(1,2.7,r"$d\otimes E_{ij}\mapsto\theta^m(d)\otimes E_{i-m,j-m},\qquad \widehat\tau\beta_m=\lambda^m\widehat\tau\quad\mathrm{on\ every\ positive\ element}$",13)
    fig.savefig(out/"discrete-decomposition.png",dpi=200,metadata={"Software":"OA-FLOW original DD reconstruction"})
    fig.savefig(out/"discrete-decomposition.svg",metadata={"Date":None,"Creator":"OA-FLOW original DD reconstruction"})
    plt.close(fig)
    data={"native_pixels":[3200,2500],"scope":"Proof schematic for nonzero separable-predual type III lambda factor; not a finite-dimensional factor model","illustrative_lambda":"1/2","shown_integer_degrees":ns,"shown_positive_values":["8","4","2","1","1/2","1/4","1/8"],"general_spectral_values":"lambda^n, every n in Z","zero_point":"operator spectral point, zero spectral projection, no eigenvector","coordinate_space":"each H_tau is the complete trace GNS space","left_unitary_shift":"n -> n+1, no lambda^(1/2) norm scaling","tail_vectors":{"xi":{"nonzero_indices":"n=-k,k>=1","coordinate":"2^-k zeta","norm_squared":"1/3","T_image_norm_squared":"infinity","log_domain":True,"T_domain":False},"eta":{"nonzero_indices":"n=k,k>=1","coordinate":"2^-k zeta","norm_squared":"1/3","T_image_norm_squared":"1/15","inverse_T_image_norm_squared":"infinity","T_domain":True,"inverse_T_domain":False}},"dual_sign":"i,j -> i-m,j-m","whole_cone_scaling":"tau_hat beta_m=lambda^m tau_hat","CC0":"to extent of rights held"}
    (out/"discrete-decomposition-data.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8",newline="\n")
if __name__=="__main__":main()
