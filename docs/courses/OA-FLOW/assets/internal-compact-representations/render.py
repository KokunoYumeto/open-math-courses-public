"""Exact S3 multiplier coordinates, Figure 132.1. Original code: CC0-1.0.
Run with Python, numpy and matplotlib. Output files are next to this script.
The columns plotted are U(g^{-1}); they are coefficient coordinates of k_j(g).
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams["svg.hashsalt"] = "oa-flow-internal-compact-representations-20261009-v1"

OUT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','font.size':12,'svg.fonttype':'path'})
R=np.array([[-.5,-np.sqrt(3)/2],[np.sqrt(3)/2,-.5]])
S=np.diag([1.,-1.])
fig,axes=plt.subplots(2,3,figsize=(11,7.3),layout='constrained')
records=[]
for ax,(k,l) in zip(axes.flat,[(0,0),(1,0),(2,0),(0,1),(1,1),(2,1)]):
    U=np.linalg.matrix_power(R,k)@np.linalg.matrix_power(S,l)
    T=U.T
    g=['1','r','r^2'][k]+('s' if l else '')
    if g=='1s': g='s'
    a=np.linspace(0,2*np.pi,241)
    ax.plot(np.cos(a),np.sin(a),color='#d4dbe2',lw=1.2)
    ax.axhline(0,color='#d4dbe2',lw=.8)
    ax.axvline(0,color='#d4dbe2',lw=.8)
    for j,color in [(0,'#1268b3'),(1,'#d66d11')]:
        v=T[:,j]
        ax.annotate('',xy=v,xytext=(0,0),arrowprops={'arrowstyle':'-|>','color':color,'lw':2.7,'mutation_scale':17})
        ax.text(*(1.18*v),rf'$k_{j+1}$',color=color,ha='center',va='center',fontsize=14)
    ax.set(xlim=(-1.45,1.45),ylim=(-1.42,1.42),aspect='equal',xticks=[-1,0,1],yticks=[-1,0,1])
    ax.set_title(rf'$g={g}$',fontsize=16,pad=5)
    ax.spines[['top','right','left','bottom']].set_visible(False)
    records.append({'g':g,'U_g_inverse':T.tolist()})
fig.suptitle(r'The multiplier over each fibre of $S_3$'+'\n'+r'Columns of $U(g^{-1})$ in the fixed internal basis $(v_1,v_2)$',fontsize=18)
fig.savefig(OUT/'s3-multiplier.png',dpi=160,facecolor='white')
fig.savefig(OUT/'s3-multiplier.svg',facecolor='white',metadata={'Date': None})
(OUT/'data.json').write_text(json.dumps({'R':[['-1/2','-sqrt(3)/2'],['sqrt(3)/2','-1/2']],'S':[[1,0],[0,-1]],'g_order':'r^k s^l','plotted_matrix':'transpose(R^k S^l) = U(g^{-1})','samples':records},indent=2),encoding='utf-8')
plt.close(fig)
