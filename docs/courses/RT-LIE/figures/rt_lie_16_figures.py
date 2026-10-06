"""Original CC0 A2 weight diagram for RT-LIE-16.

Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra, October 2026.
Run: python rt_lie_16_figures.py OUTPUT_DIR
Requires Matplotlib and NumPy. The weights and multiplicities are proved
in RT-LIE-16 Section7 and Exercise10.3, using Theorems4.1 and5.1.
Coordinates: alpha1=(sqrt(2),0), alpha2=(-1/sqrt(2),sqrt(3/2)).
This is an independently plotted weight diagram, not a copied source image.
"""
from pathlib import Path
import hashlib,json,sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

OUT=Path(sys.argv[1]) if len(sys.argv)>1 else Path(__file__).parent/'assets'/'RT-LIE-16'
OUT.mkdir(parents=True,exist_ok=True)
a1=np.array([np.sqrt(2),0.0]);a2=np.array([-1/np.sqrt(2),np.sqrt(1.5)])
assert np.allclose([a1@a1,a2@a2,a1@a2],[2,2,-1])
roots=[(1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1)]
labels=[r'$\alpha_1$',r'$\theta=\alpha_1+\alpha_2$',r'$\alpha_2$',
        r'$-\alpha_1$',r'$-\theta$',r'$-\alpha_2$']
points=np.array([a*a1+b*a2 for a,b in roots])
fig,ax=plt.subplots(figsize=(9,6.9))
fig.subplots_adjust(left=.03,right=.97,top=.88,bottom=.11)
ink='#24384d';blue='#2c6784';gold='#d7932e'
# The polygon marks the convex hull of the six nonzero weights.
hull=np.vstack([points,points[0]])
ax.fill(hull[:,0],hull[:,1],color='#edf3f6',zorder=0)
ax.plot(hull[:,0],hull[:,1],color='#9aafbd',lw=1.4,zorder=1)
for pt,label in zip(points,labels):
 ax.scatter(*pt,s=220,facecolor=blue,edgecolor='white',linewidth=2,zorder=4)
 direction=pt/np.linalg.norm(pt)
 textpos=pt+.45*direction
 ax.text(*textpos,label+'\n'+r'$m=1$',fontsize=16,ha='center',va='center',color=ink)
ax.scatter(0,0,s=420,facecolor=gold,edgecolor='white',linewidth=2,zorder=5)
ax.text(.35,.43,r'$0$'+'\n'+r'$m=2$',fontsize=17,ha='center',va='center',color=ink)
# Thin arrows identify the chosen simple roots; their ends are weight points.
for pt in [a1,a2]:
 ax.annotate('',xy=.91*pt,xytext=.13*pt,
             arrowprops=dict(arrowstyle='->',lw=1.2,color=blue),zorder=2)
ax.set_aspect('equal');ax.set_xlim(-2.1,2.1);ax.set_ylim(-1.9,1.9);ax.axis('off')
fig.suptitle('Adjoint weights of '+r'$\mathfrak{sl}_3$',fontsize=22,color=ink,y=.96)
fig.text(.5,.045,r'$\|\alpha_1\|^2=\|\alpha_2\|^2=2,\quad (\alpha_1,\alpha_2)=-1,\quad \theta=\rho$'
         +'\nSix root weights once each; the zero weight twice. Total dimension 8.',
         ha='center',va='center',fontsize=13,color=ink)
png=OUT/'a2-adjoint-weights.png'
fig.savefig(png,dpi=180,facecolor='white');plt.close(fig)
receipt=dict(lesson='RT-LIE-16',license='CC0',source=Path(__file__).name,
            file=png.name,sha256=hashlib.sha256(png.read_bytes()).hexdigest(),
            coordinates=dict(alpha1=a1.tolist(),alpha2=a2.tolist()),
            weights=[dict(root_coordinates=list(p),multiplicity=1) for p in roots]+[dict(root_coordinates=[0,0],multiplicity=2)],
            interpretation='Convex hull outline; arrows identify the two simple roots. The points and labels encode weights and multiplicities.',
            proof_locators=['Theorem4.1','Theorem5.1','Section7','Exercise10.3'],
            source_comparison='Etingof MIT2020 §26; independently generated coordinates and multiplicities; no source image copied.')
(OUT/'figure-receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(json.dumps(receipt,ensure_ascii=False))
