"""Exact q-deleted value interpolation and proved closure margins. CC0."""
from fractions import Fraction as F
from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from successor_fixed_order_endpoints import certificate

HERE=Path(__file__).resolve().parent
nodes=[-2,-1,1,2]
values=[]
for s in nodes:
    value=F(1)
    for t in nodes:
        if t!=s:value*=F(-t,s-t)
    values.append(value)
assert values==[F(-1,6),F(2,3),F(2,3),F(-1,6)] and sum(values)==1
def v2(value):
    def order(integer):
        result=0
        while integer%2==0:integer//=2;result+=1
        return result
    return order(abs(value.numerator))-order(value.denominator)
valuations=list(map(v2,values));assert valuations==[-1,1,1,-1]
root=F(1)
for s in nodes:root*=F(-2*s)
assert root==64 and v2(root)==6
data=certificate();table=data['table']
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,(left,right)=plt.subplots(1,2,figsize=(14,6),gridspec_kw={'width_ratios':[1.1,1]})
fig.suptitle('Successor integer closure at the unchanged derivative order',fontsize=18,fontweight='bold')
left.plot(nodes,[0]*4,'o',color='#267ca1',ms=10)
left.plot([-3,3],[0,0],color='#bec8d3',zorder=0)
left.scatter([0],[0],marker='*',s=150,color='#c37d2d',zorder=4)
left.annotate(r'Target $x=0$',xy=(0,0),xytext=(-.8,.65),arrowprops={'arrowstyle':'->','color':'#c37d2d'})
left.text(0,1.25,'p = 2; q = 3; R = 3; M = 1; E = 1',ha='center')
for s,value,valuation in zip(nodes,values,valuations):
    left.text(s,-.4,str(value),ha='center',color='#304e67')
    left.text(s,-.85,str(valuation),ha='center',color='#b04b36' if valuation<0 else '#267ca1')
left.text(0,-1.2,r'Cardinal values $L_s(0)$ and their $v_2$',ha='center')
left.text(0,-1.75,r'One value per node: no extra ordinary jet',ha='center')
left.text(0,-2.2,r'Deleted-cardinal bound $-B=-2$; actual minimum $-1$',ha='center')
left.text(0,-2.7,r'$W(0)=\prod_s(-2s)=64,\quad v_2(W(0))=6\geq4\theta=4$',ha='center')
left.set(xlim=(-3.1,3.1),ylim=(-3,1.9),xticks=[-3,-2,-1,0,1,2,3],yticks=[],xlabel='Integer nodes; multiples of 3 are deleted')
left.set_title('The single deleted-cardinal loss is retained',fontsize=12)
for side in ['top','left','right']:left.spines[side].set_visible(False)
positions=list(range(8));margin=[x['strict_mass_margin_per_1000']/1000 for x in table]
right.barh(positions,margin,color='#267ca1')
for y,val in zip(positions,margin):right.text(val+.018,y,f'{round(val*1000)}/1000',va='center',fontsize=10)
right.set(yticks=positions,yticklabels=[x['case'] for x in table],xlabel=r'Strict normal mass margin in units $c_1W_*$',xlim=(0,1.75))
right.invert_yaxis();right.set_title('Every original case and every rank',fontsize=12)
fig.text(.745,.025,'Both precision entries exceed the full K arithmetic cost.\nThe fractional step is still needed to supply these input zeros.',ha='center',fontsize=10)
for side in ['top','right']:right.spines[side].set_visible(False)
fig.subplots_adjust(left=.035,right=.985,bottom=.24,top=.76,wspace=.25)
output=HERE/'fixed-order-successor-profile.png';fig.savefig(output,dpi=155,bbox_inches='tight');plt.close(fig)
print(json.dumps({'figure':str(output),'cardinal_values':list(map(str,values)),'valuations':valuations,'root_value':str(root),'root_valuation':v2(root)}))
