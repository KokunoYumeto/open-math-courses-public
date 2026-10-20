"""Reproduce the exact cusp pullback and prescribed-boundary trace schematic."""
from pathlib import Path
import argparse,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np
matplotlib.rcParams['svg.hashsalt']='analytic-fixed-boundary'
p=argparse.ArgumentParser();p.add_argument('--output-dir',type=Path,default=Path(__file__).resolve().parent)
out=p.parse_args().output_dir;out.mkdir(parents=True,exist_ok=True)
bg='#f5f8fd';blue='#2466a3';green='#147e6b';orange='#bc6828';ink='#203d55';muted='#536b83'
fig=plt.figure(figsize=(10,18),facecolor=bg)
fig.text(.5,.974,'The prescribed divisor and the proper trace',ha='center',fontsize=23,color=ink)
fig.text(.5,.949,'A. Real cusp slice in the target, FB.8 and FB.49–50',ha='center',fontsize=18,color=muted)
ax=fig.add_axes([.18,.735,.64,.20],facecolor='white')
xx=np.linspace(0,1,250)
ax.plot(xx,xx**1.5,color=blue,lw=3,label='S: t² = x³')
ax.plot(xx,-xx**1.5,color=blue,lw=3)
ax.axvline(0,color=orange,lw=2.5,label='added A: x = 0')
ax.set_xlim(-.15,1.12);ax.set_ylim(-1.12,1.12);ax.set_aspect('equal')
ax.set_xlabel('Re x',fontsize=17);ax.set_ylabel('Re t',fontsize=17)
ax.tick_params(labelsize=15);ax.grid(alpha=.16);ax.legend(fontsize=14,loc='center left',bbox_to_anchor=(1.03,.5),frameon=False)
fig.text(.5,.687,'Im x = Im t = 0; equal coordinate scales.',ha='center',fontsize=16,color=muted)
fig.text(.5,.663,r'$x=u^2,\quad t=u^3(1+v),\quad J=2u^4$',ha='center',fontsize=22,color=green)
fig.text(.5,.638,r'$g^*(t^2-x^3)=u^6v(v+2)$',ha='center',fontsize=22,color=green)
fig.text(.5,.615,'The entire cover includes the complementary QG.F charts.',ha='center',fontsize=15,color=muted)
fig.text(.5,.578,'B. Coherent image with the original boundary, FB.24–30',ha='center',fontsize=18,color=muted)
a=fig.add_axes([.06,.379,.88,.18]);a.set_axis_off();a.set_xlim(0,1);a.set_ylim(0,1)
a.add_patch(FancyBboxPatch((.01,.02),.98,.95,boxstyle='round,pad=.007',facecolor='white',edgecolor='#adc4da'))
a.text(.5,.81,r'$M_0=E_\Sigma(*D_0),\quad D_0=(g^{-1}S)_{\rm red}$',ha='center',fontsize=22,color=blue)
a.text(.18,.51,r'$\mathcal{H}^0 g_+M_0$',ha='center',fontsize=22,color=blue)
a.text(.51,.51,r'$Q_0$',ha='center',fontsize=25,color=green)
a.text(.83,.51,r'$Q_T$',ha='center',fontsize=25,color=blue)
a.annotate('',(.43,.55),(.31,.55),arrowprops={'arrowstyle':'->','lw':2,'color':green})
a.annotate('',(.75,.55),(.58,.55),arrowprops={'arrowstyle':'->','lw':2,'color':blue})
a.text(.5,.26,r'$Q_0|_{X\setminus S}=L\otimes\mathcal{O}$',ha='center',fontsize=23,color=green)
a.text(.5,.09,'The normalized trace image has no pole along the added A.',ha='center',fontsize=16,color=muted)
fig.text(.5,.351,'Map and module panels are schematics; no metric scale.',ha='center',fontsize=15,color=muted)
fig.text(.5,.307,'C. Ramified disc: t = w³, FB.44–46',ha='center',fontsize=20,color=muted)
fig.text(.5,.270,r'$u(f\,dt)=3w^2f(w^3)\,dw$',ha='center',fontsize=25,color=blue)
fig.text(.5,.228,r'$\operatorname{Tr}(w^{3\ell+2}\,dw)=t^\ell\,dt$',ha='center',fontsize=25,color=green)
fig.text(.5,.192,r'$\operatorname{Tr}(3w^2f(w^3)\,dw)=3f(t)\,dt$',ha='center',fontsize=23,color=green)
fig.text(.5,.155,r'$\frac{1}{3}\operatorname{Tr}\circ u=1$',ha='center',fontsize=27,color=blue)
fig.text(.5,.114,'Holomorphic source: ℓ ≥ 0. Finite source poles: finitely many ℓ < 0.',ha='center',fontsize=17,color=muted)
fig.text(.5,.077,'Degree zero uses the function trace; degree one uses the form trace.',ha='center',fontsize=16,color=muted)
fig.text(.5,.049,'The Jacobian in the unit fixes their compatibility.',ha='center',fontsize=16,color=muted)
fig.savefig(out/'analytic-fixed-boundary.png',dpi=180,metadata={'Software':'Matplotlib'})
fig.savefig(out/'analytic-fixed-boundary.svg',metadata={'Date':None})
plt.close(fig)
data={'proofs':['FB.8','FB.24–30','FB.44–50'],
      'target_real_slice':{'equation':'t^2=x^3','added_boundary':'x=0','imaginary_coordinates':0,
                           'equal_axes':True,'x_bounds':['-3/20','28/25'],'t_bounds':['-28/25','28/25']},
      'source_chart':{'x':'u^2','t':'u^3*(1+v)','jacobian':'2*u^4','cusp_pullback':'u^6*v*(v+2)',
                      'complete_cover_locator':'QG.F complementary charts'},
      'coherent_image':'im(H^0(g_+M0)->QT)','source_module':'E_Sigma(*D0)','target_localization':'S',
      'ramification_degree':3,'top_form_unit':'3*w^2*f(w^3)*dw','trace_exponent':'k=3*l+2',
      'unnormalized_unit_trace':3,'normalized_unit_trace':1,'map_panels_have_metric_scale':False}
(out/'analytic-fixed-boundary-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
