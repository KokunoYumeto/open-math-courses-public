"""Exact original-coordinate sample for the boundary sign proof LG5--LG8."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from matplotlib.lines import Line2D

D = Path(__file__).resolve().parent
R = 2.0
T = np.diag([-2.0, 0.5])
assert np.linalg.det(T) == -1.0
theta = np.linspace(0.0, 2.0*np.pi, 1201)
z = R*np.vstack([np.cos(theta), np.sin(theta)])
w = T@z
assert np.max(np.abs(w[0]**2/16.0 + w[1]**2 - 1.0)) < 2e-15

blue, red, green, ink = '#17649a', '#ae352d', '#337447', '#343d49'
plt.rcParams.update({'font.size': 12, 'mathtext.fontset': 'dejavusans'})
fig, axes = plt.subplots(1, 2, figsize=(13.5, 6.3))
fig.subplots_adjust(left=.07, right=.985, top=.79, bottom=.25, wspace=.21)

def arrow(ax, a, b, color, scale=20):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=scale,
                                linewidth=2.3,color=color,zorder=5))

for ax in axes:
    ax.axhline(0,color='#c9ced4',lw=.8)
    ax.axvline(0,color='#c9ced4',lw=.8)
    ax.set_aspect('equal',adjustable='box')
    ax.spines[['top','right']].set_visible(False)
    ax.grid(alpha=.15)

ax=axes[0]
ax.plot(z[0],z[1],color=ink,lw=1.8)
def circle(t): return np.array([R*np.cos(t),R*np.sin(t)])
arrow(ax,circle(.14*np.pi),circle(.26*np.pi),blue)
arrow(ax,circle(1.14*np.pi),circle(1.26*np.pi),blue)
ax.scatter([2],[0],color=blue,s=32,zorder=6)
ax.text(2.05,.16,r'$z(0)=(2,0)$',fontsize=10)
ax.text(-2.42,2.39,r'$z(\theta)=(2\cos\theta,\;2\sin\theta)$')
ax.set_title(r'$B_2:\quad dx_1\wedge d\xi_1$ outward orientation',pad=12,fontsize=13)
ax.set_xlabel(r'$z_1=x_1$');ax.set_ylabel(r'$z_2=\xi_1$')
ax.set_xlim(-2.65,2.65);ax.set_ylim(-2.65,2.65)
ax.set_xticks([-2,0,2]);ax.set_yticks([-2,0,2])
ax.text(-2.4,-2.44,'Positive boundary direction: counterclockwise',color=blue,fontsize=10)

ax=axes[1]
ax.plot(w[0],w[1],color=ink,lw=1.8)
def image(t): return T@circle(t)
arrow(ax,image(.14*np.pi),image(.26*np.pi),blue)
def ambient(t): return np.array([4*np.cos(t),np.sin(t)])
arrow(ax,ambient(1.52*np.pi),ambient(1.67*np.pi),red)
ax.scatter([-4],[0],color=blue,s=32,zorder=6)
ax.annotate(r'$Tz(0)=(-4,0)$',xy=(-4,0),xytext=(-4.55,-1.60),
            fontsize=10,arrowprops={'arrowstyle':'-','color':'#69717b','lw':.8})

t=np.pi/4
nu=np.array([np.cos(t),np.sin(t)])
transverse=T@nu
normal=np.linalg.inv(T).T@nu
normal=normal/np.linalg.norm(normal)
p=image(t)
assert np.allclose(normal,np.array([-1.0,4.0])/np.sqrt(17.0))
assert abs(transverse@normal - 4.0/np.sqrt(34.0)) < 1e-15
arrow(ax,p,p+.48*transverse,blue,scale=17)
arrow(ax,p,p+.70*normal,green,scale=17)
ax.text(-4.44,1.47,r'$T\nu$',color=blue,fontsize=11)
ax.text(-2.60,1.49,r'$\nu_w$',color=green,fontsize=11)
ax.text(-4.6,2.34,r'$w(\theta)=(-4\cos\theta,\;\sin\theta)$')
ax.set_title(r'$T(B_2):\quad T=\mathrm{diag}(-2,\frac{1}{2}),\quad\det T=-1$',pad=12,fontsize=13)
ax.set_xlabel(r'$w_1=x_1$');ax.set_ylabel(r'$w_2=\xi_1$')
ax.set_xlim(-4.8,4.8);ax.set_ylim(-2.65,2.65)
ax.set_xticks([-4,-2,0,2,4]);ax.set_yticks([-1,0,1])
ax.text(-4.6,-2.38,'The image of the positive sphere path is clockwise.',color=blue,fontsize=10)

fig.suptitle('The determinant sign compares two actual boundary orientations',fontsize=15,y=.985)
handles=[Line2D([0],[0],color=blue,lw=2.3,label='Direction and outward transversal carried by T'),
         Line2D([0],[0],color=red,lw=2.3,label='Positive ambient ellipsoid direction'),
         Line2D([0],[0],color=green,lw=2.3,label='Euclidean outward image normal')]
fig.legend(handles=handles,loc='lower center',bbox_to_anchor=(.5,.055),ncol=1,frameon=False,fontsize=11)
fig.text(.5,.018,r'At $\theta=\pi/4$: $T\nu=(-\sqrt{2},\sqrt{2}/4)$, '
         r'$\nu_w=(-1,4)/\sqrt{17}$, and $(T\nu)\cdot\nu_w=4/\sqrt{34}>0$ '
         r'(LG5--LG8).',ha='center',fontsize=11)
for suffix in ['png','svg']:
    fig.savefig(D/f'linear-phase-boundary-orientation-264.{suffix}',dpi=200,
                metadata={'Creator':'Codex','Description':'Original mathematical illustration of LG5--LG8; full coordinate sample retained.'})
plt.close(fig)
(D/'linear-phase-boundary-orientation-264.json').write_text(json.dumps({
    'radius':2,'T':[[-2,0],[0,.5]],'determinant':-1,
    'input_coordinates':['x_1','xi_1'],'output_coordinates':['x_1','xi_1'],
    'input_parameterization':'(2*cos(theta), 2*sin(theta))',
    'image_parameterization':'(-4*cos(theta), sin(theta))',
    'ellipse_equation':'w_1^2/16 + w_2^2 = 1',
    'image_of_positive_input_direction':'clockwise',
    'positive_ambient_output_direction':'counterclockwise',
    'proved_normal_transversal_dot_product_at_pi_over_4':'4/sqrt(34)',
    'proof_locators':['LG5','LG6','LG7','LG8'],
    'external_source_expression_used':False,'analytic_index_depicted':False,
},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
