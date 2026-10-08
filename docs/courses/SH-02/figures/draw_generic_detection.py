"""GBD3/GBD10/GBD13 actual-map schematic; independently authored CC0-1.0."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none'})
fig=plt.figure(figsize=(14,9),facecolor='#f7f9fc')
fig.text(.05,.94,'Generic conormal detection retains the restriction arrows',size=22,weight='bold',color='#19334c')
fig.text(.05,.89,'Original Whitney strata • arbitrary bounded weak k-coefficients • generic complex normal covector',size=12)
ax=fig.add_axes([.08,.43,.37,.36])
ax.set_xlim(-.07,1.1);ax.set_ylim(-1.2,1.2)
ax.add_patch(Rectangle((0,-1),1,2,fc='#e6eef9',ec='#376196',lw=2))
for alpha in [.25,.55]:
    ax.add_patch(Rectangle((0,-alpha),alpha,2*alpha,fc='none',ec='#427d58',lw=1.5,ls='--'))
ax.axhline(0,color='#263e52',lw=2)
ax.plot([0,1],[-1,-1],color='#ad3e4f',lw=3)
ax.plot([0,1],[1,1],color='#ad3e4f',lw=3)
ax.plot(0,0,'o',color='#263e52')
ax.set_xlabel('ρ / r²');ax.set_ylabel('g / (a r²)')
ax.set_title('Value-space traps on π=s (GBD3–GBD5)',size=13)
ax.text(.62,.18,'Zₛ : g=0',size=12)
ax.text(.65,.75,'Cₛ(r)',size=12)
ax.text(.28,-.40,'Cₛ(v)',size=11,color='#427d58')
ax.text(.94,1.04,'Eₛ⁺',ha='right',color='#ad3e4f')
ax.text(.94,-1.15,'Eₛ⁻',ha='right',color='#ad3e4f')
fig.text(.08,.35,'Cₛ(v): ρ≤v², |g|≤av²; dashed α=v²/r².',size=12)
fig.text(.08,.30,'κ-fibre: [max(√ρ, √(|g|/a)), r].',size=12)
fig.text(.08,.24,'This is a diagram of values, not a coordinate\nchart or a claim that every value is attained.\nπ, ρ and g keep their original meanings.',size=11,color='#506479')

bx=fig.add_axes([.52,.23,.44,.57]);bx.set(xlim=(0,10),ylim=(0,10));bx.axis('off')
def arrow(a,b,label='',color='#315f90'):
    bx.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=15,lw=1.8,color=color))
    if label: bx.text((a[0]+b[0])/2,(a[1]+b[1])/2+.2,label,ha='center',size=11,color=color)
bx.text(5,9.4,'The central square and both generizations',ha='center',weight='bold',size=14)
bx.text(1.7,8.1,'RΓ(Cₛ;F)',ha='center',size=14)
bx.text(7.6,8.1,'RΓ(Zₛ;F)',ha='center',size=14)
arrow((3.2,8.2),(6.1,8.2),'restriction ≃')
bx.text(1.7,5.9,'Fₛ',ha='center',size=14);bx.text(7.6,5.9,'Fₛ',ha='center',size=14)
arrow((1.7,7.6),(1.7,6.35));arrow((7.6,7.6),(7.6,6.35))
bx.text(2.1,6.8,'resₛ ≃',size=11);bx.text(8.0,6.8,'resₛ ≃',size=11)
bx.text(4.7,5.9,'=',ha='center',size=16)
bx.text(5,4.7,'GBD8–GBD10: evaluation fixes the actual maps.',ha='center',size=11)
bx.text(5,3.4,'P₍ₛ,₀₎ = RΓ(Zₛ;F)',ha='center',size=13)
bx.text(1.9,1.4,'P₍ₛ,ₜ<₀₎',ha='center',size=13);bx.text(8.0,1.4,'P₍ₛ,ₜ>₀₎',ha='center',size=13)
arrow((4.1,3.0),(2.2,1.9),'≃');arrow((6.0,3.0),(7.8,1.9),'≃')
bx.text(5,.4,'Each arrow is resE ± ∘ resZ⁻¹ (GBD13).',ha='center',size=11)
fig.text(.05,.14,'N=0 makes both endpoint restrictions invertible; the phase path compares g and −g.',size=12)
fig.text(.05,.09,'Proper support composition + nonvertex vanishing return the original supported stalk (GBD14–GBD15).',size=12)
fig.text(.05,.04,'Locators: SH02-NMC-GENERIC-DETECTION, GBD3/GBD5/GBD8–GBD15. Full nongeneric detection needs separate inputs.',size=10,color='#506479')
out=Path(__file__).resolve().parent
if out.name=='figures': out=out.parent
fig.savefig(out/'generic-conormal-detection.svg',bbox_inches='tight')
fig.savefig(out/'generic-conormal-detection.png',dpi=140,bbox_inches='tight')
