from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, FancyBboxPatch

HERE=Path(__file__).resolve().parent
fig=plt.figure(figsize=(15.5,10),facecolor='white')
gs=fig.add_gridspec(2,2,height_ratios=[1,1.12],hspace=.46,wspace=.20)
ax=fig.add_subplot(gs[0,0]); bx=fig.add_subplot(gs[0,1])
cx=fig.add_subplot(gs[1,0]); dx=fig.add_subplot(gs[1,1])

# Exact real slice of the complex support: Im(t)=Im(s)=Im(v), spatial equality.
t,v=2.,-1.
s=np.linspace(v,t,250)
ax.axhline(0,color='#8b98a4',lw=1)
ax.plot([v,t],[0,0],color='#2b779b',lw=7,alpha=.7)
ax.scatter([v,t],[0,0],color=['#b95e29','#236183'],s=90,zorder=5)
ax.scatter([.4],[0],color='#a34786',s=75,zorder=6)
ax.text(v,-.19,'input v = −1',ha='center',fontsize=11)
ax.text(t,-.19,'output t = 2',ha='center',fontsize=11)
ax.text(.4,.16,'intermediate s',ha='center',fontsize=12,color='#81326b')
ax.annotate('',xy=(1.0,0),xytext=(-.25,0),arrowprops=dict(arrowstyle='->',lw=2,color='white'))
ax.text(.5,.48,'v ≤ s ≤ t: the actual compact trace fibre',ha='center',fontsize=12)
ax.text(.5,-.54,'s−t ≤ 0 and v−s ≤ 0; therefore v−t ≤ 0.\n'
        'All imaginary coordinates agree; all spatial coordinates agree.',ha='center',fontsize=10.5,linespacing=1.4)
ax.set_ylim(-.75,.8);ax.set_xlim(-1.6,2.6)
ax.set_xlabel('Real time coordinate (a slice, not all of the complex support)',fontsize=10)
ax.set_yticks([]);ax.set_xticks([-1,0,1,2])
ax.set_title('Proper line-cone composition — U.1–U.2',fontsize=12)

# The exact support conditions of the two ray kernels in independent differences.
bx.add_patch(Polygon([[0,0],[-3,0],[-3,-3],[0,-3]],fc='#e0eef5',ec='#477f9c',lw=1.5))
bx.plot([-3,0],[0,-3],color='#368164',lw=2.5)
bx.scatter([-1.6],[-1.4],color='#368164',s=60)
bx.text(-1.45,-1.16,'a+b = −3',fontsize=11,color='#24674e')
bx.text(-2.45,-.68,'a ≤ 0, b ≤ 0',fontsize=11)
bx.text(-1.7,-2.65,'a = s−t,  b = v−s',fontsize=10.5)
bx.set_xlim(-3.15,.25);bx.set_ylim(-3.15,.25);bx.set_aspect('equal')
bx.set_xlabel('a: first real normal coordinate',fontsize=10)
bx.set_ylabel('b: second real normal coordinate',fontsize=10)
bx.set_title('Independent cut variables — U.15\nThe green fibre projects to v−t = −3.',fontsize=12)

cx.axis('off');dx.axis('off')
def box(axis,y,h,txt,c,fs=11.5):
    axis.add_patch(FancyBboxPatch((.015,y),.97,h,boxstyle='round,pad=.008',fc=c,ec='#4a6274',lw=1.2))
    axis.text(.5,y+h/2,txt,ha='center',va='center',fontsize=fs,linespacing=1.4)
box(cx,.72,.25,'Positive residue normalization — U.5–U.8\n'
    '−(2πi)⁻¹ ∂̄log(a+ib) ∧ d(a+ib)\n'
    '= 1₍ₐ<₀₎ δ(b) da ∧ db\n'
    'The normalized Cauchy pole gives δ at the endpoint.','#ecf5e6')
box(cx,.40,.25,'Spatial poles and finite derivatives — U.7–U.14\n'
    'β! / [(2πi)ᵈ ∏ⱼ(yⱼ−xⱼ)^(βⱼ+1)]\n'
    'gives exactly ∂ₓᵝ on holomorphic input.\n'
    'Full normal current blocks retain output ∂̄ components.','#e9eef9',11)
box(cx,.08,.25,'Exact inverse in canonical cohomology — U.17–U.18\n'
    '∂ₜ[−log(s−t)/(2πi)] = 1/[2πi(s−t)]\n'
    '−∂ₛ[−log(s−t)/(2πi)] = 1/[2πi(s−t)]\n'
    'Both ∂ₜ * h and h * ∂ₜ equal the diagonal unit.','#e5f2ed',10.5)
box(dx,.72,.25,'Actual convergent composition — U.11–U.16\n'
    'Aβ(t,s,x) = Σₘ≥1 bₘ,β(t,x)(t−s)^(m−1)/(m−1)!\n'
    '|Aβ| ≤ Bβ Cβ / (1−Cβ|t−s|)²\n'
    'One radius: Cβ diam(Dₜ) < 1/2 for the finite list.','#edf5e8',10.5)
box(dx,.40,.25,'Canonical ring map and matrix complex — U.19–U.20\n'
    'κ(P∘Q) = Tr(κ(P) ∪ κ(Q))\n'
    'κ(Qⱼ) * κ(Qⱼ₋₁) = 0\n'
    'Example: h∘(t h) = t h²−h³, all time signs retained.','#e6eff9',11)
box(dx,.08,.25,'Remaining scope — U.6\n'
    'Full convergent z dependence; derived relative action;\n'
    'propagation and singular separation; E∞ and finite D-type;\n'
    'finite poles, intrinsic order, C1 and analytic proper regularity.','#fff0dc',10.5)

fig.suptitle('Canonical polynomial kernels: proper supports, exact residues and actual composition',fontsize=16,y=.985)
fig.text(.055,.015,'Original CC0 argument: U.1–U.5. Supports shown in exact real slices; complex and spatial constraints are stated explicitly.\n'
         'Free human sources: Kashiwara–Kawai, HolIII III.1–III.3, IV.2 and IV.5; Kashiwara–Schapira, Microhyp §3.1.\n'
         'This finite-polynomial result supplies canonical K matrix classes. It does not claim the full E or E∞ comparison or a finite D-type embedding.',fontsize=9.5,color='#435b6d')
fig.subplots_adjust(top=.89,bottom=.10)
fig.savefig(HERE/'canonical-line-cone-kernels.png',dpi=160,bbox_inches='tight')
fig.savefig(HERE/'canonical-line-cone-kernels.svg',bbox_inches='tight')
(HERE/'canonical-line-cone-figure-data.json').write_text(json.dumps({
    'real_time_output':t,'real_time_input':v,'intermediate_segment':[v,t],
    'normal_coordinates':{'a':'s-t','b':'v-s'},'trace_fibre':'a+b=-3; -3<=a<=0',
    'imaginary_constraint':'Im(t)=Im(s)=Im(v)',
    'spatial_constraint':'all input/intermediate/output spatial coordinates equal',
    'proof_locators':['U.1','U.2','U.5','U.7','U.8','U.11','U.12','U.15','U.17','U.18','U.19','U.20'],
    'scope':'finite polynomial spatial degree only; arbitrary E and E-infinity comparison open'
},indent=2)+'\n',encoding='utf-8')
print('Rendered canonical-line-cone-kernels.png and .svg')
