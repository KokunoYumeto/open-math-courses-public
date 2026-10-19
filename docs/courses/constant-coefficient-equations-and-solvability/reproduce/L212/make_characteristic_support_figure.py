"""Two exact sections of an indefinite boundary and its characteristic support.

Original illustration,code and data: GPT-6.1 Sol (OpenAI),October2026.
CC0 1.0: https://creativecommons.org/publicdomain/zero/1.0/
"""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
HERE=Path(__file__).resolve().parent;OUT=HERE/'figures';OUT.mkdir(exist_ok=True)
BLUE='#357da5';GREEN='#3d8b64'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.hashsalt':'sharp-characteristic-curvature-L212'})

def main():
    fig,axes=plt.subplots(1,2,figsize=(12.5,5.4))
    z=np.linspace(-1,1,1001)
    for ax,boundary,support,variable,title in [
      (axes[0],-z*z,np.zeros_like(z),'T','Bicharacteristic section: y = 0'),
      (axes[1],z*z,2*z*z,'Y','Transverse section: t = 0')]:
        ax.fill_between(z,boundary,2.4,color=GREEN,alpha=.11)
        ax.fill_between(z,support,2.4,color=BLUE,alpha=.14)
        ax.plot(z,boundary,color=GREEN,linewidth=2.2,label='Boundary of X')
        ax.plot(z,support,color=BLUE,linewidth=2.2,label='Characteristic support boundary')
        ax.plot(0,0,'o',markerfacecolor='white',markeredgecolor='#a13a44',markersize=7,zorder=5)
        ax.set(xlim=(-1.05,1.05),ylim=(-1.2,2.4),xlabel=variable,ylabel='S',title=title)
        ax.set_xticks([-1,-.5,0,.5,1]);ax.set_yticks([-1,0,1,2]);ax.grid(alpha=.13)
        ax.legend(loc='upper center',fontsize=9,framealpha=.95)
    axes[0].text(-.92,-.88,r'$S=-T^2$',color=GREEN,fontsize=13)
    axes[0].text(.62,.14,r'$S=0$',color=BLUE,fontsize=13)
    axes[0].annotate('t direction',xy=(.55,0),xytext=(.02,-.42),
      arrowprops={'arrowstyle':'->','color':'#555555'},fontsize=10)
    axes[1].text(-.92,1.14,r'$S=Y^2$',color=GREEN,fontsize=13)
    axes[1].text(.56,1.66,r'$S=2Y^2$',color=BLUE,fontsize=13)
    fig.text(.27,.025,r'$T=16t,\quad S=256s$'+'\n'+'Negative curvature in the characteristic tangent direction.',
      ha='center',va='bottom',fontsize=10)
    fig.text(.77,.025,r'$Y=16y,\quad S=256s$'+'\n'+'Positive transverse curvature remains allowed in the comparison.',
      ha='center',va='bottom',fontsize=10)
    fig.subplots_adjust(left=.07,right=.985,top=.88,bottom=.20,wspace=.25)
    fig.savefig(OUT/'indefinite-boundary-and-characteristic-support.png',dpi=160,
      metadata={'Software':'Exact characteristic supporting surface sections'})
    svg=OUT/'indefinite-boundary-and-characteristic-support.svg'
    fig.savefig(svg,metadata={'Date':None,'Creator':'GPT-6.1 Sol (OpenAI),October2026;CC0 1.0'})
    svg.write_bytes(('\n'.join(x.rstrip() for x in svg.read_text(encoding='utf-8').splitlines())+'\n').encode())
    plt.close(fig)
    data={'chapter':'Characteristic supporting surfaces and boundary curvature','creator':'GPT-6.1 Sol (OpenAI),October2026',
      'license':'CC0-1.0','proof_locators':['Theorem1.1','Sections3-5','Example6.1,equations6.1-6.4'],
      'operator':'2*D_t*D_s-D_y^2+i*D_s','D':'-i*partial','principal_symbol':'2*tau*varsigma-eta^2',
      'normal':[0,0,1],'bicharacteristic_vector_original_coordinates':[2,0,0],
      'boundary_graph':'g(t,y)=-t^2+y^2','tangent_Hessian':[[-2,0],[0,2]],
      'directional_curvature_b_b':-8,'characteristic_graph':'h(t,y)=2*y^2/(1+4*t)',
      'null_solution':'exp(t/2)*(s-h(t,y))_+/sqrt(1+4*t)',
      'full_separation':'h-g>=3/5*(t^2+y^2) when |t|<=1/16',
      'displayed_scale':{'T':'16*t','Y':'16*y','S':'256*s'},
      'left_section':{'slice':'y=0','boundary':'S=-T^2','support_boundary':'S=0','T_range':['-1','1']},
      'right_section':{'slice':'t=0','boundary':'S=Y^2','support_boundary':'S=2*Y^2','Y_range':['-1','1']},
      'scope':'Two exact real sections,not a claim that slice comparison alone proves the full theorem. Blue support is before translation. Domain X is the open side above its graph;drawn curves give its boundary.'}
    (HERE/'characteristic-support-data.json').write_bytes((json.dumps(data,indent=2)+'\n').encode())
    print(json.dumps({'status':'FIGURE_GENERATED','PNG':1,'SVG':1,'exact_sections':2}))
if __name__=='__main__':main()
