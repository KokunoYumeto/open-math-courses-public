"""Draw the original displacement weight and its proved directional norm map."""
from pathlib import Path
import json, hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent
q1,q2,q3=12/100,1/100,25/100
r=(np.sqrt(q1)+q3)/(1+q3*np.sqrt(q2))
angle=np.linspace(0,2*np.pi,2401)
x,y=np.cos(angle),np.sin(angle)
den=np.sqrt(np.abs(x)+q1*np.abs(y))+q3*np.sqrt(np.abs(y)+q2*np.abs(x))
rad=((1+q3*np.sqrt(q2))/den)**2
plt.rcParams.update({'font.size':12,'axes.titlesize':14,'axes.labelsize':12})
fig,(ax,bx)=plt.subplots(1,2,figsize=(13,6),gridspec_kw={'width_ratios':[1,1.6]})
fig.patch.set_facecolor('#f8fafc')
ax.plot(rad*x,rad*y,color='#145c91',lw=2.5)
ax.axhline(0,color='#a2acb9',lw=.7);ax.axvline(0,color='#a2acb9',lw=.7)
ax.scatter([1,0],[0,1/r**2],color='#a43837',zorder=3)
ax.annotate(r'$(1,0)$',(1,0),xytext=(10,9),textcoords='offset points')
ax.annotate(r'$(0,r^{-2})$',(0,1/r**2),xytext=(12,-8),textcoords='offset points')
ax.set(xlabel=r'original $h_1$',ylabel=r'original $h_2$',title=r'Exact level set $g(h)=1$',xlim=(-1.7,1.9),ylim=(-3.3,3.3))
ax.set_aspect('equal',adjustable='box')
tt=np.linspace(.42,1.86,1600)
bx.plot(tt,np.maximum(1,r/tt),color='#145c91',lw=2.8)
bx.axvline(r,color='#a43837',ls='--',lw=1.4)
bx.axvline(1/r,color='#846534',ls=':',lw=1.5)
bx.annotate(r'correct axis match $r$',(r,1),xytext=(.76,1.17),arrowprops={'arrowstyle':'->','color':'#a43837'})
bx.text(1/r+.02,1.30,r'written reciprocal $r^{-1}$',rotation=90,ha='left',va='center',fontsize=11)
bx.set(xlabel=r'ratio $τ$',ylabel=r'exact norm $max{1,r/τ}$',title='Sharp map from the full weight to axis bounds',xlim=(.42,1.86),ylim=(.97,1.45))
bx.grid(alpha=.16)
bx.text(.94,1.05,'r = 0.5818635722085614…\n0.582 is slightly larger',fontsize=11,color='#213952')
fig.suptitle('The original anisotropy weight keeps both square roots and every coefficient',fontsize=15,y=.98)
fig.text(.5,.025,'Proof: AN1–AN13. Original source: Chen–Hou Part I, hol:g and wg:hol. Curves are drawing samples of exact formulas.',ha='center',fontsize=10)
fig.subplots_adjust(left=.07,right=.95,bottom=.16,top=.86,wspace=.36)
for ext in ('png','svg'):fig.savefig(HERE/('chen-hou-anisotropy-map.'+ext),dpi=180,facecolor=fig.get_facecolor())
plt.close(fig)
meta={'proof':'CHEN_HOU_ANISOTROPY_PROOF_20261011.md','locators':'AN1–AN13','kind':'Numerical drawing samples of exact original displacement weight and proved sharp map; not numerical proof',
      'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'parameters':['12/100','1/100','25/100'],'r_drawing_only':float(r),
      'coordinates':'Original h1 and h2, without changing their relative scale','point_count':2401,'visual_inspection':'pending'}
(HERE/'chen-hou-anisotropy-map.json').write_text(json.dumps(meta,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'figure':str(HERE/'chen-hou-anisotropy-map.png')}))
