#!/usr/bin/env python3
"""Original exact cone geometry and transport directions; no sampled PDE solution."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np

ROOT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.hashsalt':'decreasing-cone-031','savefig.dpi':160})
meta={'Title':'Fundamental solutions in shrinking cones','Creator':'Original reproducible mathematical renderer','Date':'2026-10-04'}

def axis(ax):
    ax.spines[['top','right']].set_visible(False)
    ax.set_xlabel('t');ax.set_ylabel('y',rotation=0,labelpad=12)
    ax.set_aspect('equal');ax.grid(alpha=.16);ax.set_axisbelow(True)

fig,ax=plt.subplots(figsize=(7.3,5.5),layout='constrained')
colors=['#d6e5f4','#bad6e4','#83b6c2','#409094']
for j,c in zip([1,2,4,8],colors):
    ax.add_patch(Polygon([(0,0),(-4/j,4),(4/j,4)],closed=True,facecolor=c,edgecolor='#30516d',linewidth=1.05,label=f'j = {j}'))
ax.plot([0,0],[0,4],color='#101820',lw=2.4,label='intersection: t = 0, y ≥ 0')
ax.scatter([0],[0],s=30,color='#101820',zorder=8)
ax.set_xlim(-4.3,4.3);ax.set_ylim(-.12,4.35);axis(ax)
ax.set_title('Closed transverse cones: y ≥ j|t|',pad=14)
ax.text(.02,.96,'All real x are allowed.\nBoth sloping faces are included.',transform=ax.transAxes,ha='left',va='top',fontsize=10,bbox={'facecolor':'white','edgecolor':'none','alpha':.9})
ax.legend(loc='lower right',framealpha=.95,fontsize=9)
fig.savefig(ROOT/'shrinking-cones.png',metadata={'Title':meta['Title'],'Author':'OpenAI','Description':'Original exact transverse cone sections; no PDE solution plotted.'})
fig.savefig(ROOT/'shrinking-cones.svg',metadata=meta);plt.close(fig)

fig,ax=plt.subplots(figsize=(7.3,5.7),layout='constrained')
j=2;yb=.8;send=2.4
ax.add_patch(Polygon([(0,0),(-2.15,4.3),(2.15,4.3)],closed=True,facecolor='#deedf0',edgecolor='#385a68',linewidth=1.4))
for xi,c in [(2,'#2166ac'),(-2,'#2166ac'),(4,'#2b8c73'),(-4,'#2b8c73')]:
    tend=-send/xi;yend=yb+send
    ax.annotate('',xy=(tend,yend),xytext=(0,yb),arrowprops={'arrowstyle':'->','color':c,'lw':2.1})
    ax.text(tend+(.05 if tend>0 else -.05),yend+.07,f'ξ = {xi}',ha='left'if tend>0 else'right',color=c,fontsize=10)
ax.plot([0,-send],[yb,yb+send],ls='--',color='#b33b36',lw=1.9)
ax.scatter([-.8],[1.6],marker='x',s=58,color='#b33b36',zorder=8)
ax.text(-2.70,3.62,'ξ = 1: leaves cone',color='#a62b29',fontsize=10)
ax.text(-.91,1.38,'first boundary contact',color='#a62b29',fontsize=9,ha='right')
ax.scatter([0],[yb],s=38,color='#101820',zorder=8)
ax.text(.10,yb-.07,'start: (0, 0.8)',fontsize=10)
ax.text(.03,.97,'Q transport: (Δt, Δy) = (−s/ξ, s)\nAllowed exactly when |ξ| ≥ j.',transform=ax.transAxes,va='top',ha='left',fontsize=10,bbox={'facecolor':'white','edgecolor':'none','alpha':.91})
ax.set_title('Cone-preserving transport for j = 2',pad=14)
ax.set_xlim(-2.8,2.5);ax.set_ylim(-.08,4.35);axis(ax)
fig.savefig(ROOT/'cone-transport.png',metadata={'Title':meta['Title'],'Author':'OpenAI','Description':'Exact high-frequency transpose transport slopes inside the closed cone.'})
fig.savefig(ROOT/'cone-transport.svg',metadata=meta);plt.close(fig)

geo={'schema':'decreasing-cone-geometry/v1','coordinates':{'horizontal':'t','vertical':'y','unrestricted':'x'},'closed_cone':'y>=j*abs(t)','edge':'{(x,0,0):x real}','intersection':'{(x,y,0):y>=0}','sections':[{'j':j,'clip_y':4,'vertices':[[0,0],[-4/j,4],[4/j,4]]}for j in [1,2,4,8]],'transport':{'operator':'Q=P(-D)','j':2,'start':[0,.8],'parameter_end':2.4,'allowed_xi':[2,-2,4,-4],'rays':[{'xi':xi,'displacement':['-s/xi','s'],'end':[-2.4/xi,3.2]}for xi in [2,-2,4,-4]],'excluded_xi':1,'excluded_first_contact':[-.8,1.6]},'scope':'support enclosures and exact inverse directions, not exact support or a numerical PDE solution','proof_locators':['DC2','DC3','DC9','DC10']}
(ROOT/'decreasing-cones.geometry.json').write_text(json.dumps(geo,indent=2)+'\n',encoding='utf-8')
print('Rendered two PNGs, two SVGs and exact geometry.')
