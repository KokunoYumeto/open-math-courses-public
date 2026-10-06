"""Original CC0 diagram of the cutoff isometry and proper-factorization unit.

The two bundled fonts retain the full terms in FONT-NOTICE.txt and both images.
"""
from pathlib import Path
import argparse
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties, fontManager

HERE = Path(__file__).resolve().parent
for name in ('DejaVuSans.ttf', 'DejaVuSans-Bold.ttf'):
    fontManager.addfont(str(HERE/'fonts'/name))
REG = FontProperties(fname=str(HERE/'fonts/DejaVuSans.ttf'))
BOLD = FontProperties(fname=str(HERE/'fonts/DejaVuSans-Bold.ttf'))
plt.rcParams.update({'svg.fonttype':'path', 'svg.hashsalt':'proper-auxiliary-v1'})
BLUE = '#175d76'

def compression(out,credit):
    matrices=[[[0,0,2,1],[0,0,1,3],[2,1,0,0],[1,3,0,0]],
              [[0,0,0,1],[0,0,0,3],[0,0,0,0],[1,3,0,0]],
              [[0,0,2],[0,0,1],[2,1,0]]]
    titles=['D = F l⁻¹','B = [D,P](2P − 1)','D_K = P(D − B)P on PH']
    labels=[['e₁⁺','e₂⁺','e₁⁻','e₂⁻'],['e₁⁺','e₂⁺','e₁⁻','e₂⁻'],['e₁⁺','e₂⁺','e₁⁻']]
    fig, axes=plt.subplots(1,3,figsize=(15.4,7.0))
    fig.subplots_adjust(left=.065,right=.96,top=.72,bottom=.33,wspace=.35)
    fig.suptitle('Remove the unrepresented couplings, then compress: the full scalar index is retained',
                 y=.97,fontsize=17,fontproperties=BOLD)
    fig.text(.5,.89,'Exact finite model (UP.20–UP.21): T = ((2,1),(1,3)); F exchanges the two grading blocks; l = diag(T⁻¹,T⁻¹).',
             ha='center',fontsize=12,fontproperties=REG)
    fig.text(.5,.82,'P = diag(1,1,1,0); φ(a) = aP. The last negative coordinate has zero source representation.',
             ha='center',fontsize=12,fontproperties=REG)
    for ax,matrix,title,names in zip(axes,matrices,titles,labels):
        n=len(matrix)
        ax.imshow(matrix,cmap='Blues',vmin=0,vmax=3,interpolation='nearest')
        ax.set_xticks(range(n),names);ax.set_yticks(range(n),names)
        for tick in ax.get_xticklabels()+ax.get_yticklabels(): tick.set_fontproperties(REG)
        ax.set_title(title,fontproperties=BOLD,fontsize=13,pad=13)
        for i,row in enumerate(matrix):
            for j,value in enumerate(row):
                ax.text(j,i,str(value),ha='center',va='center',fontsize=15,
                        fontproperties=BOLD,color='white' if value>=2 else BLUE)
        if n==4:
            ax.add_patch(plt.Rectangle((-.5,2.5),4,1,fill=False,edgecolor='#a94c15',lw=2))
            ax.add_patch(plt.Rectangle((2.5,-.5),1,4,fill=False,edgecolor='#a94c15',lw=2))
    fig.text(.5,.235,'D_K⁺ = [2  1] : ℂ² → ℂ; kernel = ℂ(1,−2); cokernel = 0; index = +1.',
             ha='center',fontsize=14,fontproperties=BOLD)
    fig.text(.5,.155,'‖[D,P]‖ = ‖B‖ = √10. B is bounded, odd and self-adjoint; D − B reduces P.',
             ha='center',fontsize=12,fontproperties=REG)
    fig.text(.5,.075,'The general proof preserves compact resolvent, all prescribed commutators and the whole KK class; this finite model asserts no summability.',
             ha='center',fontsize=11,fontproperties=REG)
    fig.savefig(out/'auxiliary-essential-compression.png',dpi=150,metadata={'Software':'draw_proper.py','Description':credit})
    fig.savefig(out/'auxiliary-essential-compression.svg',metadata={'Date':None,'Creator':'draw_proper.py','Description':credit})
    plt.close(fig)

def label(ax,x,y,s,size=12,bold=False,**kwargs):
    return ax.text(x,y,s,fontsize=size,fontproperties=BOLD if bold else REG,**kwargs)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output-dir',default=str(HERE/'figures'))
    out=Path(parser.parse_args().output_dir); out.mkdir(parents=True,exist_ok=True)
    fig, axes=plt.subplots(2,1,figsize=(15.4,9.4))
    fig.subplots_adjust(left=.055,right=.975,top=.84,bottom=.065,hspace=.27)
    fig.suptitle('A proper coefficient supplies the norm bridge; a forgetful unit supplies index +1',
                 y=.975,fontsize=18,fontproperties=BOLD)
    fig.text(.5,.925,'Exact hypotheses: a central nondegenerate C₀(X) action, X proper; even η and d with For(η ⊗ d) = 1.',
             ha='center',fontsize=12,fontproperties=REG)
    for ax in axes:
        ax.set(xlim=(0,1),ylim=(0,1)); ax.axis('off')
    a,b=axes
    label(a,0,1.02,'A. Square-normalized cutoff and the isometric compression (AU.1–AU.7)',14,True)
    label(a,.5,.85,'Σ_g c(g⁻¹x)² = 1; only finitely many translates occur on each compact set',14,True,ha='center')
    label(a,.17,.65,'H',17,True,ha='center')
    label(a,.66,.65,'H ⊗ ℓ²Γ',17,True,ha='center')
    a.annotate('',xy=(.52,.67),xytext=(.25,.67),arrowprops={'arrowstyle':'->','lw':2,'color':BLUE})
    label(a,.39,.74,'J isometry',13,True,ha='center')
    label(a,.5,.48,'Jξ = Σ_g π(c_g)ξ ⊗ δ_g;  JU_h = (U_h ⊗ λ_h)J',14,ha='center')
    label(a,.5,.31,'W(ξ ⊗ δ_g) = U_g⁻¹ξ ⊗ δ_g turns the amplification into the regular representation.',12,ha='center')
    label(a,.5,.14,'Every covariant norm ≤ reduced norm ⇒ q_P : P ⋊ₘ Γ → P ⋊ᵣ Γ is an actual *-isomorphism.',12,True,ha='center')
    label(a,.5,.01,'Finite stabilizers are allowed; Γ need not be amenable and X/Γ need not be compact.',11,ha='center')
    label(b,0,1.02,'B. The four typed factors and the exact unit evaluation (AU.8–AU.16)',14,True)
    names=['R','P ⋊ᵣ Γ','P ⋊ₘ Γ','M','ℂ']
    positions=[.04,.28,.52,.76,.96]
    for x,name in zip(positions,names):
        label(b,x,.79,name,16,True,ha='center')
    arrows=['jᵣ(η)','[q_P]⁻¹','jₘ(d)','[ε]']
    for left,right,name in zip(positions,positions[1:],arrows):
        b.annotate('',xy=(right-.055,.81),xytext=(left+.055,.81),arrowprops={'arrowstyle':'->','lw':2,'color':BLUE})
        label(b,(left+right)/2,.89,name,12,True,ha='center')
    label(b,.5,.60,'Their product is κ ∈ KK(R,ℂ), with R = C*ᵣΓ and M = C*ₘΓ.',13,ha='center')
    label(b,.5,.42,'q*κ = jₘ(γ) ⊗ ε;  uᵣ*κ = For(γ) = 1;  γ = η ⊗_P d.',14,True,ha='center')
    label(b,.5,.25,'ℓ(x) = x ⊗_R κ;  ℓ([1_R]) = +1;  K₀(R) = ℤ[1_R] ⊕ ker ℓ.',13,ha='center')
    label(b,.5,.08,'The inverse is for the proper coefficient quotient q_P. No inverse of q : M → R is assumed.',12,True,ha='center')
    notice=(HERE/'FONT-NOTICE.txt').read_text(encoding='utf-8')
    credit='Original mathematical diagram and generator: CC0 1.0. Bundled glyph terms follow.\n'+notice
    fig.savefig(out/'proper-auxiliary.png',dpi=150,metadata={'Software':'draw_proper.py','Description':credit})
    fig.savefig(out/'proper-auxiliary.svg',metadata={'Date':None,'Creator':'draw_proper.py','Description':credit})
    plt.close(fig)
    compression(out,credit)
    for name in ['proper-auxiliary.svg','auxiliary-essential-compression.svg']:
        path=out/name
        path.write_text(path.read_text(encoding='utf-8'),encoding='utf-8',newline='\n')

if __name__=='__main__':
    main()
