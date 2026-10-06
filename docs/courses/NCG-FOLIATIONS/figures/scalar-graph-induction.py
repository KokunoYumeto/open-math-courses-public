from pathlib import Path
import math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none'})
fig,axs=plt.subplots(2,2,figsize=(16,10),gridspec_kw={'height_ratios':[1,1]})
fig.patch.set_facecolor('#f7fafc')
fig.suptitle('Scalar graph induction on the compact SU(2) / F₂ suspension',fontsize=22,fontweight='bold',y=.98)
ax=axs[0,0];ax.set_axis_off();ax.set_xlim(0,1);ax.set_ylim(0,1)
boxes=[(.04,.62,.37,.18,'B = C(SU(2)) ⋊ᵣ F₂\nfaithful ΠB on HN ⊗ HT'),(.57,.62,.39,.18,'A = Cr*(Hol(V,F))\nfaithful ΠA on E ⊗B HB'),(.12,.16,.78,.22,'DG = P(1K ⊗ DB)P,    Dom DG = P Dom D0\nDB = DN ⊗ ΓT + 1 ⊗ DT\nfull normal spin + even tree completion')]
for x,y,w,h,label in boxes:
    ax.add_patch(plt.Rectangle((x,y),w,h,fc='white',ec='#25536b',lw=2))
    ax.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=12)
ax.annotate('',xy=(.57,.70),xytext=(.41,.70),arrowprops={'arrowstyle':'->','color':'#25536b'})
ax.text(.50,.845,'i: faithful normalized plaque corner (SG.18)',ha='center',fontsize=11)
ax.text(.50,.92,'1. Exact reduced scalar representation',ha='center',fontweight='bold',fontsize=15)
ax.text(.50,.48,'‖ΠB(b)‖ = ‖b‖r       and       ‖ΠA(a)‖ = ‖a‖r',ha='center',color='#1f6b46',fontsize=14)

ax=axs[0,1];ax.set_aspect('equal');ax.set_axis_off();ax.set_xlim(-2.1,2.1);ax.set_ylim(-2.1,2.5)
root=(0,0);positions=[root]
for j in range(4):
    angle=math.pi/4+j*math.pi/2
    p=(.85*math.cos(angle),.85*math.sin(angle));positions.append(p)
    ax.plot([0,p[0]],[0,p[1]],color='#788d9c',lw=2)
    # A rooted Cayley ball has precisely three children at every nonroot vertex.
    for delta in (-.31,0,.31):
        ca=angle+delta;c=(1.72*math.cos(ca),1.72*math.sin(ca));positions.append(c)
        ax.plot([p[0],c[0]],[p[1],c[1]],color='#788d9c',lw=1.8)
        middle=((p[0]+c[0])/2,(p[1]+c[1])/2)
        ax.scatter(*middle,marker='s',s=28,color='#e79a32',zorder=3)
        ax.annotate('',xy=(c[0]*1.14,c[1]*1.14),xytext=c,arrowprops={'arrowstyle':'->','color':'#a7b5bf'})
    ax.scatter(p[0]/2,p[1]/2,marker='s',s=28,color='#e79a32',zorder=3)
ax.scatter([p[0] for p in positions],[p[1] for p in positions],s=60,color='#25536b',zorder=4)
ax.scatter(0,0,s=170,color='#1f986b',zorder=5)
ax.text(0,.18,'e: unmatched + root',ha='center',fontsize=10,bbox={'facecolor':'white','edgecolor':'none','alpha':.95})
ax.text(0,2.32,'2. Vertex → parent-edge pairing',ha='center',fontweight='bold',fontsize=15)
ax.text(0,-2.02,'Exact radius-two ball; the full tree continues.  Index Q = +1.',ha='center',fontsize=11)

ax=axs[1,0];x=np.linspace(-4,4,400)
for length,color in [(1,'#e79a32'),(2,'#357ea4'),(3,'#885fa7')]:
    y=np.sqrt(x*x+length*length)
    ax.plot(x,y,color=color,label=f'n = {length}');ax.plot(x,-y,color=color)
ax.plot(x,x,'--',color='#1f986b',label='root: eigenvalue ν')
ax.set_title('3. Complete multiplicity control',fontweight='bold',pad=14)
ax.set_xlabel('Normal eigenvalue parameter ν (schematic continuous curves)')
ax.set_ylabel('Block eigenvalue')
ax.text(0,.1,'nonroot block: ±√(ν² + n²)',ha='center',fontsize=12,bbox={'fc':'white','ec':'none'})
ax.grid(alpha=.22);ax.legend(loc='upper left',fontsize=10,ncol=2)
ax=axs[1,1];ax.set_axis_off();ax.set_xlim(0,1);ax.set_ylim(0,1)
ax.set_title('4. Graph compactness is coefficient-localized',fontweight='bold',pad=14)
lines=[('k ∈ K(K)', '#25536b'),('b(DB − z)⁻¹ ∈ K(HB)', '#25536b'),('k ⊗ b(DB − z)⁻¹ ∈ K(K ⊗ HB)', '#1f6b46'),('P and R multiply J = K(K) ⊗ B(HB)', '#25536b'),('‖[DGRt, a]‖ ≤ 5‖[DG,a]‖ / (4(1+t²))', '#25536b'),(r'Local Bott pairing: $(i_* b_U)\cdot z_G = +1$', '#1f6b46')]
for j,(label,color) in enumerate(lines):ax.text(.50,.90-j*.13,label,ha='center',color=color,fontsize=13)
ax.text(.50,.07,'Scope: this suspension and the stated sufficient interface.\nArbitrary holonomy groupoids and literal local graph Dirac remain open.',ha='center',fontsize=11,color='#973f3f')
fig.tight_layout(rect=[0,.02,1,.94]);fig.savefig(OUT/'scalar-graph-induction.png',dpi=160);fig.savefig(OUT/'scalar-graph-induction.svg')
print('Rendered original mathematical PNG and SVG.')
