"""Reproduce the exact support sets in HS7–HS11; no solution samples."""
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Circle, Wedge
import numpy as np

HERE=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':11,'svg.hashsalt':'AN02-HS-028'})
fig,axes=plt.subplots(1,2,figsize=(13,6.4),constrained_layout=True)
ax,local=axes
ax.add_patch(Polygon([(-2,0),(2,0),(0,2)],facecolor='#c7dfec',edgecolor='#285d7a',lw=2,label=r'$K=(y-C)\cap H_{e_t}$'))
ax.add_patch(Polygon([(0,0),(1,0),(.5,.5)],facecolor='#efc47b',edgecolor='#946624',lw=2,label=r'$(x_0-C)\cap H_{e_t}$'))
ax.axhline(.5,color='#9a3162',ls='--',lw=1.4,label=r'earliest possible time $t_0=1/2$')
ax.add_patch(Circle((.5,.5),.25,fill=False,ls=':',edgecolor='#4c4c4c',lw=1.5))
ax.scatter([0,.5],[2,.5],color='#151515',s=35,zorder=5)
ax.annotate(r'$y=(0,2)$',(0,2),xytext=(.18,2.04))
ax.annotate(r'$x_0=(1/2,1/2)$',(.5,.5),xytext=(.8,.86),arrowprops={'arrowstyle':'-','color':'#222'})
ax.set(xlim=(-2.25,2.5),ylim=(-.15,2.35),xlabel=r'$z$',ylabel=r'$t$',title='The past slice is compact')
ax.set_aspect('equal')
ax.legend(loc='upper left',bbox_to_anchor=(-.02,-.15),fontsize=9,frameon=False)

cx,ct=.5,.5
local.fill_between([.15,.5,.85],[.15,.5,.15],[.15,.15,.15],color='#efc47b',alpha=.55,label=r'backward cone $x_0-C$')
local.add_patch(Wedge((cx,ct),.2,0,360,width=.1,facecolor='#b5b5b5',edgecolor='#666',alpha=.75,label='possible commutator annulus'))
local.add_patch(Wedge((cx,ct),.2,225,315,width=.1,facecolor='#a14138',edgecolor='#822f27',alpha=.9,label='annulus in the strict past'))
local.add_patch(Circle((cx,ct),.1,facecolor='white',edgecolor='#555',lw=1.2))
local.add_patch(Circle((cx,ct),.25,fill=False,ls=':',edgecolor='#4c4c4c',lw=1.5,label=r'local neighborhood, radius $1/4$'))
local.axhline(.5,color='#9a3162',ls='--',lw=1.4)
local.scatter([cx],[ct],color='#151515',s=30,zorder=6)
local.annotate(r'$\chi=1$',(cx,ct),xytext=(.47,.545))
local.annotate(r'$r=1/10$',(.5,.6),xytext=(.19,.77),arrowprops={'arrowstyle':'-','color':'#222'})
local.annotate(r'$r=1/5$',(.5,.7),xytext=(.67,.77),arrowprops={'arrowstyle':'-','color':'#222'})
local.annotate('No source here:\ntime is below $t_0$',(.5,.34),xytext=(.62,.23),fontsize=10,arrowprops={'arrowstyle':'->','color':'#822f27'},color='#822f27')
local.set(xlim=(.16,.84),ylim=(.16,.84),xlabel=r'$z$',ylabel=r'$t$',title='Local cutoff at the hypothetical first point')
local.set_xticks([.25,.5,.75]);local.set_yticks([.25,.5,.75]);local.set_aspect('equal')
local.legend(loc='upper left',bbox_to_anchor=(-.01,-.15),fontsize=9,frameon=False)
fig.suptitle('HS7–HS11: support bounds and a compact-localization contradiction',fontsize=14)
fig.savefig(HERE/'hyperbolic-first-support.png',dpi=200,metadata={'Software':'AN02 original exact support diagram'})
fig.savefig(HERE/'hyperbolic-first-support.svg',metadata={'Date':None,'Creator':'GPT-6.1 Sol (OpenAI), Ultra; CC0'})
plt.close(fig)
record={
 'schema':'AN02-hyperbolic-first-support-exact-geometry/v1',
 'coordinates':['z','t'],'normal':['0','1'],
 'cone':'t >= abs(z)','y':['0','2'],'hypothetical_first_point':['1/2','1/2'],
 'compact_slice_vertices':[['-2','0'],['2','0'],['0','2']],
 'local_backward_slice_vertices':[['0','0'],['1','0'],['1/2','1/2']],
 'cutoff_inner_radius':'1/10','cutoff_outer_radius':'1/5','local_neighborhood_radius':'1/4',
 'first_time':'1/2','strict_past_annulus_angles_degrees':['225','315'],
 'proof_locators':['HS5','HS7','HS8','HS9','HS10','HS11'],
 'set_plot_only':True,'actual_solution_values_or_occupied_support_claimed':False,
 'human_comparison':'Hörmander II, printed p.210 / PDF p.216'
}
(HERE/'geometry.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'PNG':str(HERE/'hyperbolic-first-support.png'),'SVG':str(HERE/'hyperbolic-first-support.svg')}))
