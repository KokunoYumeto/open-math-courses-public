from pathlib import Path
import argparse,json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle,FancyBboxPatch
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.hashsalt':'infinite-matrix-flatness-common-domain-v1','axes.spines.top':False,'axes.spines.right':False})
p=argparse.ArgumentParser();p.add_argument('--output',type=Path);args=p.parse_args()
root=Path(__file__).resolve().parent;out=args.output or root/'figures';out.mkdir(parents=True,exist_ok=True)
fig,axes=plt.subplots(1,2,figsize=(15,8.8),gridspec_kw={'width_ratios':[1,1.15]})
fig.subplots_adjust(left=.055,right=.975,bottom=.33,top=.80,wspace=.24)
fig.suptitle('All corrections share one coefficient domain',fontsize=18,y=.965)
fig.text(.5,.895,'Bounded analytic division preserves each radius; only derivatives spend the reserved margin.',ha='center',fontsize=12,color='#334155')
ax=axes[0];ax.set_aspect('equal');ax.set_xlim(-1.18,1.18);ax.set_ylim(-1.18,1.18)
samples=[1,.875,.75,.625,.5];colors=['#334155','#2563eb','#0891b2','#16a34a','#d97706']
for s,color in zip(samples,colors):
 ax.add_patch(Rectangle((-s**1.5,-s),2*s**1.5,2*s,fill=False,ec=color,lw=1.8))
ax.set_xlabel(r'$\operatorname{Re}u/R_u(r_0)$');ax.set_ylabel(r'$\operatorname{Re}z/R_z(r_0)$')
ax.set_title(r'Exact real slice: $R_u(r)=r^{3/2},\ R_z(r)=r$',fontsize=12,pad=15)
ax.grid(alpha=.15)
for index,(s,color) in enumerate(zip(samples,colors)):
 ax.text(-1.10,-1.48-.10*index,f's = r/r₀ = {["1","7/8","3/4","5/8","1/2"][index]}',color=color,fontsize=10)
ax.text(-1.10,-2.07,'The full domains are complex polydiscs.\nThis displayed slice is not a support cone.',fontsize=10,color='#475569')
right=axes[1];right.axis('off');right.set_xlim(0,1);right.set_ylim(0,1)
right.set_title('A fixed interval for a word of any length',fontsize=12,pad=15)
def box(y,text,color='#eff6ff',height=.2):
 right.add_patch(FancyBboxPatch((.01,y),.98,height,boxstyle='round,pad=.02',fc=color,ec='#94a3b8'))
 right.text(.5,y+height/2,text,ha='center',va='center',fontsize=11,linespacing=1.6)
box(.75,r'$L$ derivatives: total scalar margin $r_0/2$'+'\n'+r'$\Delta r=r_0/(2L)$ for each derivative',height=.20)
box(.45,'Uniform coefficient operators on every intermediate radius\n'+r'$\|h\|,\|p\|,\|k\|\leq H$'+'\nNo radius loss is spent on a division operator.',color='#f0fdf4',height=.23)
box(.12,r'$\mathrm{cost}\leq C^K(|m|+K)!/|m|!$'+'\n'+r'$K=Q+L$ includes every tail and derivative index.'+'\nOne final domain works for the complete sum.',color='#fff7ed',height=.24)
for a,b in [(.745,.685),(.44,.38)]:
 right.annotate('',(.5,b),(.5,a),arrowprops={'arrowstyle':'->','lw':1.5,'color':'#475569'})
right.text(.5,-.16,'For zero-remainder detection, reserve one further fixed interval\ninside the output domain before the iteration index is chosen.\nNo shrinking per iteration. Proof: MFA.2–MFA.3 and MFB.2/MFB.4.',ha='center',va='top',fontsize=10,color='#334155')
fig.text(.055,.025,'Illustrative radius family for the principal relation (-z,u); exact sample L=4. General proof uses its finite-data weights and the same allocation mechanism.',fontsize=10,color='#475569')
fig.savefig(out/'infinite-matrix-flatness-common-domain.png',dpi=150,metadata={'Software':'Matplotlib; reproducible local proof illustration'})
fig.savefig(out/'infinite-matrix-flatness-common-domain.svg',metadata={'Date':None,'Creator':'Reproducible local proof illustration'})
plt.close(fig)
data={'proof_locators':['MFA.1–MFA.3','MFB.2','MFB.4'],'illustrative_principal_relation':['-z','u'],'weights':{'u':'3/2','z':'1'},'normalized_samples':['1','7/8','3/4','5/8','1/2'],'sample_derivative_count':4,'sample_normalized_scalar_margin_each':'1/8','rectangle_halfwidths':'(s^(3/2),s), s=r/r0','domain':'Exact real slice of complex coefficient polydiscs, not a support cone','general_margin':'r0/(2L), allocated before all homogeneous/Taylor/tail/iteration indices','uniform_operator_bounds':'H on the full fixed radius interval; no derivative commutation assumed','zero_detection':'One additional fixed radius interval inside the output domain, before all iteration indices'}
(out/'infinite-matrix-flatness-common-domain-data.json').write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'outputs':3,'directory':str(out)}))
