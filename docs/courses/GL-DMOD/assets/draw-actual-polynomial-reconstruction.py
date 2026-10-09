from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import json
HERE=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(15,9),facecolor='white')
ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
def box(x,y,w,h,txt,color,fs=12):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.009',fc=color,ec='#40566d',lw=1.4))
    ax.text(x+w/2,y+h/2,txt,ha='center',va='center',fontsize=fs,linespacing=1.4)
def arrow(start,end,label=None,ls='-'):
    ax.annotate('',xy=end,xytext=start,arrowprops=dict(arrowstyle='->',color='#476887',lw=1.8,linestyle=ls))
    if label:
        ax.text((start[0]+end[0])/2,(start[1]+end[1])/2+.028,label,ha='center',va='center',fontsize=11,bbox=dict(fc='white',ec='none',pad=3))
box(.03,.79,.37,.14,'Polynomial source R₀ = ⊕β A₀ z^β\nR₀/(h) = H[z],  H = C{u}\nFinite polynomial degree; actual coefficients','#e9f1fc')
box(.60,.79,.37,.14,'Actual factorial ring E₀\nE₀/(h) = T = C{u,z}\nCommon coefficient domain and factorial bounds','#e9f1fc')
arrow((.415,.855),(.585,.855),'F.7: exact on finite modules')
box(.03,.55,.37,.14,'h-adic formal source\nR̂₀ = H[z][[h]]\nFinite modules complete and separated','#f2f3f7')
box(.60,.55,.37,.14,'h-adic formal target\nÊ₀ = T[[h]]\nThis is not the infinite-order ring E∞','#f2f3f7')
arrow((.215,.78),(.215,.705),'exact completion')
arrow((.785,.78),(.785,.705),'exact; detects zero')
arrow((.415,.615),(.585,.615),'finite quotients + Artin–Rees')
box(.03,.29,.43,.16,'Principal reconstruction, F.9–F.10\npᵢ(u,Z)=det(Z−Aᵢ(u)),  pᵢ(0,Z)=Z^b\nT/(p₁,…,p_d) ≅ H[z]/(p₁,…,p_d)\nActual Weierstrass division; all branches retained','#edf6e6',11)
box(.54,.29,.43,.16,'Actual multiplication map, F.11–F.12\nμ₀: E₀ ⊗R₀ M₀ → M₀\nK = ker μ₀,  K ∩ hP = hK,  K/hK=0\nFinite Nakayama ⇒ K=0; E ⊗R M ≅ M','#e6f5ec',11)
arrow((.215,.535),(.215,.465))
arrow((.785,.535),(.785,.465))
arrow((.475,.37),(.525,.37))
box(.03,.065,.56,.13,'Every R-submodule N ⊂ M is stable under E, F.13\nUse h-saturation, actual flatness, G.1 and finite A₀-Nakayama.\nEntire actual stalk; supported sections are included.','#e6f5ec',11)
box(.65,.065,.32,.13,'L.1–L.6 supplies the actual bounded resolution\nand one base. OPEN: E∞ comparison,\nfinite D-type embedding and C1','#fff0dc',10.5)
arrow((.755,.275),(.42,.205))
arrow((.755,.275),(.81,.205),ls='--')
fig.suptitle('Actual polynomial reconstruction after finite generic-position realization',fontsize=17,y=.98)
fig.text(.065,.025,'Exact proof: F.1–F.7. Premise: the actual finite lattice and finite principal fibre of G.1.  '
         'Human proof target: Kashiwara–Kawai, free HolIII PDF, III.5.\n'
         'Solid arrows are actual or h-adic finite-module comparisons. The dashed arrow records an obligation still requiring proof.',
         fontsize=10,color='#43576b')
fig.subplots_adjust(top=.94,bottom=.065)
fig.savefig(HERE/'actual-polynomial-reconstruction.png',dpi=160,bbox_inches='tight')
fig.savefig(HERE/'actual-polynomial-reconstruction.svg',bbox_inches='tight')
(HERE/'actual-polynomial-figure-data.json').write_text(json.dumps({'actual_source':'R0=direct sum_beta A0*z^beta','actual_target':'E0','principal_source':'H[z]','principal_target':'T=C{u,z}','formal_source':'H[z][[h]]','formal_target':'T[[h]]','kernel_condition':'K intersection hP=hK and K/hK=0','tensor_scope':'finite-order actual stalk; explicit G.1 premise','open':['infinite-order comparison','faithful finite D-type embedding','C1']},indent=2)+'\n',encoding='utf-8')
print('Rendered actual-polynomial-reconstruction.png and .svg')
