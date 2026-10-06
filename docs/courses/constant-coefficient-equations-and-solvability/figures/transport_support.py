"""Reproduce the transport support diagram. Original drawing, CC0-1.0.

The operator is partial_1 + 2 partial_2 + 1. Its active space is span(1,2),
its inactive space is span(2,-1), and the forward kernel has support t(1,2),
t >= 0. Arrows indicate unbounded continuation, not finite endpoints.
"""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
matplotlib.rcParams['svg.hashsalt']='transport-support-v1'
import matplotlib.pyplot as plt
import numpy as np

out=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(7.5,6.2),layout='constrained')
ax.set_xlim(-2.5,2.5);ax.set_ylim(-3.1,3.1);ax.set_aspect('equal')
ax.axhline(0,color='#cbd5e1',linewidth=1)
ax.axvline(0,color='#cbd5e1',linewidth=1)
t=np.linspace(-1.5,1.5,100)
ax.plot(t,2*t,color='#65758b',linewidth=2,linestyle='--')
ax.plot(2*t,-t,color='#247ba0',linewidth=2,linestyle=':')
ax.annotate('',xy=(1.47,2.94),xytext=(0,0),arrowprops={'arrowstyle':'->','color':'#23865b','lw':4})
ax.scatter([0],[0],s=52,color='#23865b',zorder=5)
ax.text(-1.65,-2.3,r'$V_P=\mathbb{R}(1,2)$',fontsize=13,color='#526277',bbox={'facecolor':'white','edgecolor':'none','alpha':0.95})
ax.text(0.65,-1.0,r'$N_P=\mathbb{R}(2,-1)$',fontsize=13,color='#247ba0',bbox={'facecolor':'white','edgecolor':'none','alpha':0.95})
ax.text(-2.32,2.40,r'$\operatorname{supp}E_+=\{t(1,2):t\geq0\}$',fontsize=12,color='#23865b',bbox={'facecolor':'white','edgecolor':'none','alpha':0.95})
ax.text(0.12,0.1,'0',fontsize=12)
ax.set_xlabel(r'$x_1$',fontsize=13);ax.set_ylabel(r'$x_2$',fontsize=13,rotation=0,labelpad=12)
ax.set_title(r'$L=\partial_{x_1}+2\partial_{x_2}+1$',fontsize=15,pad=14)
ax.grid(alpha=0.12)
fig.savefig(out/'transport-support.png',dpi=180,metadata={'Author':'GPT-6.1 Sol (OpenAI), Ultra','Description':'Original mathematical support diagram, CC0-1.0'})
fig.savefig(out/'transport-support.svg',metadata={'Creator':'GPT-6.1 Sol (OpenAI), Ultra','Date':'2026-09','Description':'Original mathematical support diagram, CC0-1.0'})
plt.close(fig)
