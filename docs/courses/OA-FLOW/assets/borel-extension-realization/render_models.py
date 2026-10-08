"""Original reproducible figures for EX19--EX21, R4, and R9.10--R9.18.

No source images or sampled source artwork. Coordinates are the displayed
closed-form mathematical models. Fonts are supplied by matplotlib, not copied.
"""
from pathlib import Path
import hashlib
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

OUT = Path(__file__).resolve().parent
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11,
                     'axes.spines.top': False, 'axes.spines.right': False,
                     'svg.fonttype': 'none',
                     'svg.hashsalt': 'borel-extension-models-v1'})
BLUE, RED, GREY = '#165c92', '#b43b45', '#5a6270'

def save(fig, stem):
    for ext in ('png', 'svg'):
        metadata = {'Creator': 'Original mathematical model; CC0-1.0'}
        if ext == 'svg':
            metadata['Date'] = None
        fig.savefig(OUT / f'{stem}.{ext}', dpi=180, bbox_inches='tight',
                    metadata=metadata)
    plt.close(fig)

t = np.linspace(-np.pi, np.pi, 1001)
fig, axes = plt.subplots(3, 1, figsize=(10.8, 7.4), sharex=True, sharey=True)
for ax, r in zip(axes, (-1, 0, 2)):
    ax.plot(t, np.cos(r*t), color=BLUE, lw=2, label='Real part: cos(rt)')
    ax.plot(t, np.sin(r*t), color=RED, lw=2, ls='--', label='Imaginary part: sin(rt)')
    samples = np.linspace(-np.pi, np.pi, 13)
    ax.scatter(samples, np.cos(r*samples), s=14, color=BLUE, zorder=3)
    ax.scatter(samples, np.sin(r*samples), s=14, color=RED, zorder=3)
    ax.axvline(0, color=GREY, lw=.75, alpha=.6)
    ax.set_ylim(-1.2, 1.2)
    ax.set_yticks([-1, 0, 1])
    ax.set_ylabel(f'r = {r}')
    ax.grid(alpha=.15)
handles, labels = axes[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='upper center', bbox_to_anchor=(.5,.883),
           ncol=2, fontsize=10)
axes[-1].set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
                   [r'$-\pi$', r'$-\pi/2$', '0', r'$\pi/2$', r'$\pi$'])
axes[-1].set_xlabel('Real action parameter t')
fig.suptitle('The shear realizes every real character', fontsize=17, y=.995)
fig.text(.5, .925, r'$\theta_t(a,r)=(ae^{irt},r),\quad\delta_E(a,r)(t)=e^{irt}$',
         ha='center', fontsize=14)
fig.text(.5, .015, 'EX19–EX20: r ranges over all real numbers. These three exact curves are examples, not a restriction of the range.',
         ha='center', fontsize=10)
fig.tight_layout(rect=(0,.045,1,.84))
save(fig, 'real-characters')

fig, axes = plt.subplots(1,3,figsize=(15,4.9),gridspec_kw={'width_ratios':[1.1,1,1]})
ax=axes[0]
ax.plot([-1.1,0],[0,0],color=BLUE,lw=2.5)
ax.plot([0,1.1],[1,1],color=BLUE,lw=2.5)
ax.scatter([0],[0],color=BLUE,s=45,zorder=4)
ax.scatter([0],[1],facecolors='white',edgecolors=BLUE,s=55,zorder=4)
ax.axvline(0,color=GREY,ls=':',lw=1.4)
ax.text(-.04,1.46,r'$j(A):x=0$',ha='right',fontsize=10,color=GREY)
ax.text(.63,.63,r'$v(x)=(b(x),x)$',ha='center',fontsize=11,color=BLUE)
ax.set_title('Borel section in the ambient group')
ax.set_ylabel('Ambient first coordinate u')
ax.set_xlabel('Quotient coordinate x')
ax.set_xlim(-1.2,1.2);ax.set_ylim(-.4,1.65)
ax.set_yticks([0,1]);ax.grid(alpha=.12)
ks=np.array([1,2,3,4,8,16]);xs=1/ks
for ax,y,col,title,ylabel in [
    (axes[1],-1,RED,'Coordinates before transport','Coordinate a'),
    (axes[2],0,BLUE,'Images in the Euclidean group','Ambient coordinate u')]:
    ax.scatter(xs,np.repeat(y,len(xs)),s=32,color=col,zorder=4)
    ax.scatter([0],[0],s=48,color='black',zorder=5)
    ax.annotate('identity (0,0)',xy=(0,0),xytext=(.22,.47),
                arrowprops={'arrowstyle':'->','color':'black'},fontsize=10)
    ax.set_xlim(-.13,1.12);ax.set_ylim(-1.4,.8)
    ax.set_yticks([-1,0]);ax.set_xlabel('Quotient coordinate x')
    ax.set_ylabel(ylabel);ax.set_title(title);ax.grid(alpha=.12)
axes[1].scatter([0],[-1],s=50,facecolors='white',edgecolors=RED,zorder=5)
axes[1].text(.57,-.72,r'$(-1,1/k)$',ha='center',color=RED,fontsize=13)
axes[1].text(.57,-1.26,'Product-coordinate picture only',ha='center',fontsize=9,color=GREY)
axes[2].text(.57,-.40,r'$F(-1,1/k)=(0,1/k)$',ha='center',color=BLUE,fontsize=12)
axes[2].annotate('',xy=(.035,.04),xytext=(1,.04),
                 arrowprops={'arrowstyle':'->','color':BLUE,'lw':1.2})
fig.suptitle('A jump in the section changes coordinates, not the realized group',fontsize=17,y=1.01)
fig.text(.5,.005,r'R4.1–R4.4: $F(a,x)=(a+b(x),x)$.  The metric $d_F(z,w)=|F(z)-F(w)|$ makes $(-1,1/k)\to(0,0)$.',
         ha='center',fontsize=11)
fig.tight_layout(rect=(0,.065,1,.96))
save(fig,'section-topology')

fig, axes = plt.subplots(1, 2, figsize=(12, 6.7))
h = 1/8
q = 2*h
for ax in axes:
    ax.axvline(0, color=GREY, lw=.7, alpha=.45)
    ax.axhline(0, color=GREY, lw=.7, alpha=.45)
    ax.set_xlim(-.37,.37)
    ax.set_xticks([-q,0,q],[r'$-1/4$','0',r'$1/4$'])
    ax.set_xlabel('Quotient coordinate x')
    ax.grid(alpha=.12)
ax = axes[0]
ax.add_patch(Rectangle((-q,-q),q,2*q,facecolor=BLUE,alpha=.16,edgecolor='none'))
ax.add_patch(Rectangle((0,-1-q),q,2*q,facecolor=BLUE,alpha=.16,edgecolor='none'))
for xy in [([-q,-q],[-q,q]),([-q,0],[-q,-q]),([-q,0],[q,q]),
           ([q,q],[-1-q,-1+q]),([0,q],[-1-q,-1-q]),([0,q],[-1+q,-1+q]),
           ([0,0],[-1-q,-1+q])]:
    ax.plot(*xy,color=BLUE,lw=1.3,ls='--')
ax.plot([0,0],[-q,q],color=BLUE,lw=2.2)
ax.scatter([0,0],[-q,q],s=35,facecolors='white',edgecolors=BLUE,zorder=5)
ax.scatter([0],[0],s=40,color='black',zorder=6)
ax.set_ylim(-1.39,.42)
ax.set_yticks([-1-q,-1,-1+q,-q,0,q],
              [r'$-5/4$',r'$-1$',r'$-3/4$',r'$-1/4$','0',r'$1/4$'])
ax.set_ylabel('Section coefficient a')
ax.set_title('The neighborhood in section coordinates')
ax.text(-.125,.09,r'$x\leq0$',ha='center',fontsize=12,color=BLUE)
ax.text(.125,-.93,r'$x>0$',ha='center',fontsize=12,color=BLUE)
ax.text(.02,.03,'identity',fontsize=10)
ax = axes[1]
ax.add_patch(Rectangle((-q,-q),2*q,2*q,facecolor=BLUE,alpha=.16,edgecolor='none'))
ax.add_patch(Rectangle((-q,-q),2*q,2*q,fill=False,edgecolor=BLUE,lw=1.4,ls='--'))
ax.scatter([0],[0],s=40,color='black',zorder=6)
ax.set_ylim(-.37,.37)
ax.set_yticks([-q,0,q],[r'$-1/4$','0',r'$1/4$'])
ax.set_ylabel('Ambient coordinate u = a + b(x)')
ax.set_title('Its image under F is an open rectangle')
ax.text(.02,.03,'identity',fontsize=10)
fig.suptitle('Brown neighborhoods recover the topology across a section jump',fontsize=16,y=.99)
fig.text(.5,.913,r'$r=-2,\ h=1/8,\quad B=(-h,h)s((-2-h,-2+h)),\quad W=B^{-1}B$',ha='center',fontsize=13)
fig.text(.5,.083,r'$W=\{(a,x):|x|<1/4,\ |a+b(x)|<1/4\},\qquad F(W)=(-1/4,1/4)^2$',ha='center',fontsize=13)
fig.text(.5,.031,'R9.10–R9.18, exact sets. Dashed boundary segments are excluded; the solid vertical segment is included.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.13,1,.87),w_pad=4)
save(fig,'brown-neighborhood')

manifest={
 'license':'Original mathematical figure source and model data: CC0-1.0; matplotlib fonts retain their terms.',
 'models':{
  'real-characters':{'proof':'EXTENSIONS.md EX19–EX21; Section 6 character classification',
    't_min':'-pi','t_max':'pi','curve_samples':1001,'parameters_r':[-1,0,2],
    'formula':'real=cos(r*t), imaginary=sin(r*t)',
    'range_claim':'all r in R, proved analytically; three plotted samples are illustrative'},
  'section-topology':{'proof':'REALIZATION.md R4.1–R4.4',
    'b':'0 for x<=0, 1 for x>0',
    'ambient_order':'(u,x); plot horizontal x, vertical u',
    'coordinate_order':'(a,x); plot horizontal x, vertical a',
    'k':[int(k) for k in ks],
    'sequence':'(-1,1/k)', 'image_sequence':'(0,1/k)',
    'realized_limit':'(0,0) under metric pulled back through F',
    'product_coordinate_limit':'(-1,0), shown hollow; not the realized limit'},
  'brown-neighborhood':{'proof':'REALIZATION.md R9.10–R9.18 and R4.1–R4.2',
    'r':-2,'h':'1/8','regular_domain':'R minus {0}',
    'B':'(-h,h) s((-2-h,-2+h))',
    'W':'B^{-1} B = {(a,x): abs(x)<1/4, abs(a+b(x))<1/4}',
    'F_W':'(-1/4,1/4)^2 in coordinates (u,x)',
    'boundary':'dashed excluded; solid at x=0 and -1/4<a<1/4 included',
    'depiction':'exact planar sets, not samples or schematic bounds'}},
 'outputs':{}
}
for stem in manifest['models']:
 for ext in ('png','svg'):
  p=OUT/f'{stem}.{ext}'
  manifest['outputs'][p.name]={'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
(OUT/'models.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps(manifest['outputs'],indent=2))
