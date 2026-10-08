"""Render the exact OES model figure. Run: python render.py.

Requires Python 3, NumPy, Matplotlib. Reads only neighboring data.json and writes
oes-models.png/.svg. No network or external images. Exact formulas are proved
in PART_MODELS.md. Numerical checks verify the illustration, not the theorem.
Original code: CC0-1.0 to the extent of rights held.
"""
from pathlib import Path
import json
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT=Path(__file__).resolve().parent
DATA=json.loads((ROOT/'data.json').read_text(encoding='utf-8'))
plt.rcParams.update({
    'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans',
    'font.size':12,'text.color':'#15313e','axes.labelcolor':'#15313e',
    'axes.edgecolor':'#9aa9b1','xtick.color':'#435d6a','ytick.color':'#435d6a',
    'xtick.labelsize':10,'ytick.labelsize':10,
    'axes.spines.top':False,'axes.spines.right':False,
    'figure.facecolor':'white','savefig.facecolor':'white',
    'svg.fonttype':'path','svg.hashsalt':'OES-models-20261007',
})
teal,purple,red='#137d8c','#7c50a7','#ad4250'
norm=math.e-1
correct=(math.e-1)/norm
wrong=(math.exp(2)-math.e)/norm
assert abs(correct-1)<1e-15 and abs(wrong-math.e)<1e-15
s=np.linspace(-math.pi,math.pi,501)
phase_a=s
phase_b=-s
assert np.max(np.abs(np.exp(1j*phase_a)*np.exp(1j*phase_b)-1))<1e-14
assert abs(np.exp(1j*math.pi/2)-1j)<1e-14
assert abs(np.exp(-1j*math.pi/2)+1j)<1e-14
assert np.max(np.abs(np.exp(-1j*s*(-1))-np.exp(1j*s)))<1e-14
# Independent exact support and integrated-weight formulas for the Fourier branch.
for h in [-2.,-.5,0.,1.,2.]:
    # u_h xi(q)=xi(q+h): support [-h,1-h], weighted mass exp(-h).
    mass=(math.exp(1-h)-math.exp(-h))/norm
    assert math.isclose(mass,math.exp(-h),rel_tol=2e-15)

fig=plt.figure(figsize=(16,12.8))
fig.text(.055,.960,DATA['title'],fontsize=22,weight='bold')
fig.text(.055,.929,'One fully computed translation system; one explicitly qualified factor calculation.',fontsize=12,color='#5b6f79')

def heading(x,y,letter,title):
    fig.text(x,y,letter,fontsize=15,weight='bold',color='white',
      bbox=dict(boxstyle='round,pad=0.28',facecolor='#15313e',edgecolor='none'))
    fig.text(x+.037,y,title,fontsize=15,weight='bold')

def box(x,y,w,h,label,color='#eef5f6',size=14):
    patch=FancyBboxPatch((x,y),w,h,transform=fig.transFigure,
      boxstyle='round,pad=0.008',facecolor=color,edgecolor='#adc2cb',linewidth=1.2)
    fig.patches.append(patch)
    fig.text(x+w/2,y+h/2,label,ha='center',va='center',fontsize=size)

def arrow(a,b,color='#435d6a',style='-|>',lw=1.8):
    fig.patches.append(FancyArrowPatch(a,b,transform=fig.transFigure,
      arrowstyle=style,mutation_scale=15,linewidth=lw,color=color))

heading(.055,.884,'A','The two corrections have different sides')
heading(.545,.884,'B','A finite test detects the wrong order')
heading(.055,.466,'C','The discrepancy phases cancel exactly')
heading(.545,.466,'D','Two quotient levels retain different data')

labels=[r'$\alpha=\operatorname{Ad}(v^*w)$',
        r'$\gamma=\alpha\operatorname{Ad}(w^*)=\operatorname{Ad}(v^*)$',
        r'$\gamma^\circ=\operatorname{Ad}(v)\gamma=\mathrm{id}$']
for b,label in zip(DATA['normalization']['diagram_boxes'],labels): box(*b,label,size=14)
arrow((.2525,.753),(.2525,.721))
arrow((.2525,.641),(.2525,.609))
fig.text(.267,.734,'compose on the right',fontsize=11,color=teal)
fig.text(.267,.622,'compose on the left',fontsize=11,color=teal)
fig.text(.078,.845,r'$v=M_{e^{iq}},\quad w=\mathcal{F}_-,\quad d_s=e^{is}$',fontsize=13)
fig.text(.078,.494,r'Reversing the first correction gives $\operatorname{Ad}(u_{-1})$.',fontsize=11,color=red)

ax=fig.add_axes([.617,.588,.292,.245])
bars=ax.bar([0,1],[correct,wrong],width=.51,color=[teal,red])
ax.set_xticks([0,1],['correct order','reversed first step'])
ax.set_yticks([0,1,math.e],['0','1',r'$e$'])
ax.set_ylim(0,3.25); ax.set_ylabel(r'weight of $A=\theta_{\xi,\xi}$')
ax.grid(axis='y',color='#e4ebef',lw=.8); ax.set_axisbelow(True)
for bar,label in zip(bars,['1',r'$e$']):
    ax.text(bar.get_x()+bar.get_width()/2,bar.get_height()+.10,label,ha='center',fontsize=18,weight='bold')
fig.text(.585,.547,r'$\xi(q)=\frac{1}{\sqrt{e-1}}1_{[0,1]}(q)e_0,\qquad\Phi(A)=1$',fontsize=13)
fig.text(.585,.509,r'$u_{-1}\xi$ has support $[1,2]$; $\Phi\operatorname{Ad}(u_{-1})=e\Phi$.',fontsize=11)
fig.text(.585,.486,'Exact integrals; A is positive rank one, not asserted to be a projection.',fontsize=10,color='#5b6f79')

ax=fig.add_axes([.09,.205,.372,.18])
ax.plot(s,phase_a,color=teal,lw=2.7,label=r'$k_b$: phase $+s$')
ax.plot(s,phase_b,color=purple,lw=2.7,label=r'$\operatorname{Ad}(b)$ on $u_s$: phase $-s$')
ax.plot(s,np.zeros_like(s),color='#15313e',lw=2.0,label='product: phase 0')
ax.set_xlim(-math.pi,math.pi); ax.set_ylim(-3.5,3.5)
ax.set_xticks([-math.pi,0,math.pi], [r'$-\pi$','0',r'$\pi$'])
ax.set_yticks([-math.pi,0,math.pi], [r'$-\pi$','0',r'$\pi$'])
ax.set_xlabel(r'translation parameter $s$'); ax.set_ylabel('phase before exponentiation')
ax.grid(color='#e4ebef',lw=.7)
ax.scatter([math.pi/2,math.pi/2,math.pi/2],[math.pi/2,-math.pi/2,0],color=[teal,purple,'#15313e'],zorder=5,s=25)
ax.text(math.pi/2+.10,math.pi/2,r'$i$',fontsize=13,color=teal)
ax.text(math.pi/2+.10,-math.pi/2,r'$-i$',fontsize=13,color=purple)
ax.text(math.pi/2+.10,.10,'1',fontsize=12)
ax.legend(loc='upper center',bbox_to_anchor=(.5,1.28),ncol=1,frameon=False,fontsize=10)
fig.text(.085,.148,r'$b(q)=e^{iq}h,\quad z(q)=e^{-iq},\quad k_b=\partial z,\quad bz=h$.',fontsize=12)
fig.text(.085,.111,r'$\Gamma_{\operatorname{Ad}(b)|_N}=\operatorname{Ad}(b)\alpha_{k_b}$; the inverse leaves phase $-2s$.',fontsize=11)

fig.text(.573,.426,'Assume a given properly infinite trace-scaling factor coefficient N.',fontsize=11,color=purple)
fig.text(.585,.391,r'$G/I_0\ \cong\ \operatorname{Out}(P)$',fontsize=14,weight='bold')
box(.580,.297,.151,.068,r'$[\mathrm{id}]_{I_0}$',size=14)
box(.788,.297,.151,.068,r'$[\beta_1]_{I_0}$',color='#f4eff9',size=14)
fig.text(.6555,.277,'lift: 1',ha='center',fontsize=11)
fig.text(.8635,.277,r'lift: $[\delta_{-1}]\ne1$',ha='center',fontsize=11,color=purple)
fig.text(.754,.322,r'$\ne$',ha='center',fontsize=18)
arrow((.6555,.263),(.750,.232),color=teal)
arrow((.8635,.263),(.769,.232),color=purple)
box(.644,.158,.247,.064,r'$[\mathrm{id}]_I=[\beta_1]_I$',size=14)
fig.text(.918,.180,r'$G/I$',fontsize=13,ha='center')
fig.text(.574,.118,'These are quotient classes, not metric coordinates or a choice of section.',fontsize=10,color='#5b6f79')
fig.text(.574,.091,'The failed representative prescription does not prove nonsplitting.',fontsize=11,color=red)

fig.lines.append(plt.Line2D([.515,.515],[.084,.894],transform=fig.transFigure,color='#d7e0e5',lw=1))
fig.text(.055,.056,'Proof locators: OES7.12–OES7.18; Diagnostics 3–7. Haar pair: ds and dt/(2π).',fontsize=10,color='#5b6f79')
fig.text(.055,.032,'Original figure and exact data: CC0-1.0. DejaVu font terms retained separately. Human-source context is in the lesson caption.',fontsize=9,color='#5b6f79')
fig.savefig(ROOT/'oes-models.png',dpi=160,metadata={'Software':'Matplotlib; original OES renderer','Title':DATA['title']})
fig.savefig(ROOT/'oes-models.svg',metadata={'Date':None,'Title':DATA['title'],'Description':'Exact normalization-order witness, phase cancellation, and a qualified factor quotient calculation; see data.json for hypotheses and proof locators.'})
plt.close(fig)
print(json.dumps({'finite_weight_values':[correct,wrong],'phase_cancellation_max_error':float(np.max(np.abs(np.exp(1j*s)*np.exp(-1j*s)-1))),'dual_parameter_for_character_a_1':-1,'support_translation_checks':'pass at five exact shifts','outputs':['oes-models.png','oes-models.svg'],'output_pixels':[2560,2048]},indent=2))
