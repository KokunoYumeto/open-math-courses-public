"""Exact coordinate-map illustration for M1–M3 in parameter-morse-reduction.md.
Human source route: Lebl Basic Analysis II 6.3 section8.5,
https://www.jirka.org/ra/html/sec_svinvfuncthm.html; Guillemin–Sternberg
author draft 2010-01-13 section13.14.3. Original example and figure.
Public domain (CC0), like its companion exposition.
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

out=Path(__file__).resolve().parent
u=np.linspace(-1.4,1.4,420)
v=np.linspace(-1.1,1.1,340)
U,V=np.meshgrid(u,v)
Q=(U*U-V*V)/2
levels=[-0.4,0,0.4]
colors=['#B54727','#222222','#17699C']
# Parametrize each level exactly before sampling; do not interpolate contours.
paths=[]
level_error=0.
for level in levels:
    if level>0:
        extent=min(1.1,np.sqrt(1.4**2-2*level))
        t=np.linspace(-extent,extent,500)
        group=[np.column_stack((sign*np.sqrt(t*t+2*level),t)) for sign in [-1,1]]
    elif level<0:
        extent=min(1.4,np.sqrt(1.1**2+2*level))
        t=np.linspace(-extent,extent,500)
        group=[np.column_stack((t,sign*np.sqrt(t*t-2*level))) for sign in [-1,1]]
    else:
        t=np.linspace(-1.1,1.1,500)
        group=[np.column_stack((t,sign*t)) for sign in [-1,1]]
    for path in group:
        level_error=max(level_error,float(np.max(np.abs((path[:,0]**2-path[:,1]**2)/2-level))))
    paths.append(group)
if level_error>1e-12:raise RuntimeError('Phase-level parametrization failed')

def mapping(s,z1,z2):
    if s is None:return z1,z2
    return s+z1-z2*z2/(1+s),z2/np.sqrt(1+s)

plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(1,3,figsize=(13.6,5.2))
fig.subplots_adjust(left=0.055,right=0.99,bottom=0.20,top=0.82,wspace=0.28)
max_error=0.
for ax,s in zip(axes,[None,-0.5,0.5]):
    for z1 in np.linspace(-1.4,1.4,9):
        ax.plot(*mapping(s,np.full_like(v,z1),v),color='#CAD3D9',lw=0.8)
    for z2 in np.linspace(-1.1,1.1,9):
        ax.plot(*mapping(s,u,np.full_like(u,z2)),color='#CAD3D9',lw=0.8)
    for group,color in zip(paths,colors):
        for segment in group:
            ax.plot(*mapping(s,segment[:,0],segment[:,1]),color=color,lw=1.8)
    point=(0,0) if s is None else (s,0)
    ax.plot(*point,'ko',ms=5)
    ax.annotate('critical point',point,xytext=(7,8),textcoords='offset points',fontsize=8)
    ax.set_aspect('equal',adjustable='box')
    if s is None:
        ax.set(title='Signed quadratic coordinates',xlabel='$z_1$',ylabel='$z_2$')
    else:
        ax.set(title=f'Exact image at $s={s:g}$',xlabel='$x$',ylabel='$y$')
        X,Y=mapping(s,U,V)
        error=np.max(np.abs(((X-s+Y*Y)**2-(1+s)*Y*Y)/2-Q))
        max_error=max(max_error,float(error))
        if error>1e-12:raise RuntimeError('Coordinate map does not preserve phase')
fig.suptitle('One quadratic saddle, two curved parameter charts',fontsize=15)
fig.legend([Line2D([0],[0],color=c,lw=2) for c in colors],
           [r'$\phi=-0.4$',r'$\phi=0$',r'$\phi=0.4$'],loc='lower center',
           ncol=3,fontsize=10,frameon=False,bbox_to_anchor=(0.5,0.025))
fig.savefig(out/'parameter-morse-map.png',dpi=175)
fig.savefig(out/'parameter-morse-map.svg')
plt.close(fig)
(out/'parameter-morse-checks.json').write_text(json.dumps({
    'scope':'Sampled map identity, not a mathematical proof or source clearance',
    'z1_range':[-1.4,1.4],'z2_range':[-1.1,1.1],
    'parameter_values':[-0.5,0.5],'phase_levels':levels,
    'sampled_identity_points':2*U.size,'maximum_roundoff_error':max_error,
    'maximum_phase_level_roundoff_error':level_error,
    'passed':True},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'figure':str(out/'parameter-morse-map.png'),'maximum_identity_error':max_error}))
