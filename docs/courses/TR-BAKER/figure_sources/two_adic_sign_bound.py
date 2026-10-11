"""Original rational 2-adic sign figure and exact certificate; CC0."""
from pathlib import Path
from fractions import Fraction as F
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
ROOT=Path(__file__).resolve().parent
def exp_bounds(x,order=32):
    total=term=F(1)
    for n in range(1,order+1):term*=x/n;total+=term
    nxt=term*x/(order+1)
    return total,total+nxt/(1-x/(order+2))
assert exp_bounds(F(69,100))[1]<2<exp_bounds(F(7,10))[0]
assert exp_bounds(F(2,5))[0]>F(7,5)
c=F(361,10)*F(121,100)*F(100,69)**4
assert c==F(4368100000,22667121) and 208-c==F(346661168,22667121)>0
grid=[]
for b2 in range(1,11):
    row=[]
    for b1 in range(1,11):
        d=abs(3**b1-5**b2);assert d
        v=0
        while d%2==0:d//=2;v+=1
        if b1%2:assert v==1
        else:assert v>=2
        row.append(v)
    grid.append(row)
record={'state':'passed_exact_certificate','coefficient_upper':str(c),'positive_margin_208':str(208-c),'exact_integer_grid':grid,'examples':{'3-5^2':1,'3^2-5^2':4},'coverage':'Complete proof covers all independent rational 2-adic units, signed nonzero coefficients and logarithmic heights >=max(height,ln2); finite grid illustrates exact sign cases only.'}
(ROOT/'two-adic-sign-endpoints.json').write_text(json.dumps(record,indent=2)+'\n')
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,axes=plt.subplots(1,2,figsize=(11.6,5.5),constrained_layout=True)
ax=axes[0];ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
nodes=[(.5,.86,r'$\alpha_i=\eta_i\beta_i,\quad\eta_i\in\{1,-1\}$'+'\n'+r'$\beta_i\in 1+4\mathbb{Z}_2$'),(.5,.58,r'$\eta=\eta_1^{b_1}\eta_2^{-b_2}$'),(.25,.28,r'$\eta=-1$'+'\n'+r'$v_2(\Lambda)=1$'),(.76,.28,r'$\eta=1$'+'\n'+'Both-deep estimate\n'+r'coefficient $<208$')]
for x,y,t in nodes:ax.text(x,y,t,ha='center',va='center',bbox={'boxstyle':'round,pad=.6','facecolor':'#edf3f5','edgecolor':'#527485'})
for a,b in [((.5,.78),(.5,.64)),((.47,.52),(.27,.39)),((.53,.52),(.73,.40))]:ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','lw':1.6,'color':'#527485'})
ax.set_title('Exact normalization and sign alternatives')
ax=axes[1];im=ax.imshow(grid,origin='lower',extent=(.5,10.5,.5,10.5),cmap='Blues',vmin=0,vmax=max(map(max,grid)))
for j,row in enumerate(grid,1):
    for i,v in enumerate(row,1):ax.text(i,j,str(v),ha='center',va='center',color='white' if v>=4 else '#183449',fontsize=10)
ax.set(xticks=range(1,11),yticks=range(1,11),xlabel=r'Exponent $b_1$',ylabel=r'Exponent $b_2$',title=r'Exact $v_2(3^{b_1}-5^{b_2})$')
fig.colorbar(im,ax=ax,label='Exact integer valuation',shrink=.8)
fig.savefig(ROOT/'two-adic-sign-bound.png',dpi=160);plt.close(fig)
print(json.dumps({'state':record['state'],'coefficient_upper':str(c),'positive_margin_208':str(208-c)}))
