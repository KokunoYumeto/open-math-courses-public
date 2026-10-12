"""Exact number-field determinant certificate and original figure; CC0."""
from pathlib import Path
from fractions import Fraction as F
import json
import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
def exp_bounds(x,order=64):
    total=term=F(1)
    for n in range(1,order+1):
        term*=x/n;total+=term
    nxt=term*x/(order+1)
    return total,total+nxt/(1-x/(order+2))
assert exp_bounds(F(11,10))[1]<F(61,20)
assert (9*61)**2<3*(16*20)**2
assert exp_bounds(F(39,5))[0]>2380
assert F(26,15)**2>3
assert F(149,100)**2>F(14,5)**3/10
left=3*F(13,5)**2-3*F(13,5)-F(2,3)*F(26,15)*F(14,5)**2
pieces=[F(3,5),F(149,75),F(28,75),F(117,500)]
right=sum(pieces);margin=left-right
assert left==F(3848,1125) and right==F(4791,1500)
assert margin==F(1019,4500)>0
constant=3*F(14,5)**2+F(14,5)/10+F(1,10)
assert constant==F(239,10)<24
assert F(1,10)+F(49,50)+F(7,1000)<F(28,25)
pairs=[(r,s) for r in range(8) for s in range(8) if (r+s)%2==0]
assert len(pairs)==32
rcoords=sorted(r for r,s in pairs)
weights=[F(l)-F(7,2) for l in range(8) for _ in range(4)]
actual=sum(a*b for a,b in zip(weights,rcoords))
compressed=F(32*8*8,8)-F(32**2*8,24*4)
relaxed=F(32*8*9,8)-F(2*32**2*8,24*9)
unrestricted=F(32*8*7,8)
assert actual==168 and compressed==F(512,3) and relaxed==F(5728,27)
assert actual<compressed<relaxed<unrestricted
record={'state':'passed_exact_rational_certificate',
        'left_lower':str(left),'right_upper':str(right),
        'uniform_positive_margin':str(margin),'valuation_coefficient_upper':str(constant),
        'positive_gap_24':str(24-constant),'collision_coefficient_upper':'28/25',
        'example':{'selected_pairs':pairs,'N':32,'K':4,'L':8,'g':2,'m1':1,'m2':1,
                   'r_capacity':4,'exact_centered_maximum':str(actual),
                   'compressed_bound':str(compressed),'relaxed_bound':str(relaxed),
                   'no_capacity_bound':str(unrestricted)},
        'coverage':'Full infinite B>=10,z>=1,D0<=B/10 ranges proved by analytic monotonicity in the lesson; all global/local field degrees, ramification indices, residue subgroup orders and signed nonzero coefficients. Occupancy imported only from fully proved lesson6.4.'}
record['cutoff_table']=json.loads('[\n  {\n    "eta": 5,\n    "nu": 4,\n    "k": "43/10",\n    "ell": "3",\n    "Kmin": 61,\n    "sqrt_k_upper": "41473/20000",\n    "sqrt_lambda3_over_nu_upper": "81849/25000",\n    "log_M_upper": "675321/100000",\n    "positive_margin_lower": "17/100",\n    "exact_margin": "340527/2000000",\n    "coefficient_upper": "269/5",\n    "target": "269/5",\n    "beta_f_upper": "113847153/100000000"\n  },\n  {\n    "eta": 5,\n    "nu": 6,\n    "k": "18/5",\n    "ell": "14/5",\n    "Kmin": 65,\n    "sqrt_k_upper": "189737/100000",\n    "sqrt_lambda3_over_nu_upper": "226431/100000",\n    "log_M_upper": "179083/25000",\n    "positive_margin_lower": "93/1000",\n    "exact_margin": "263401/2812500",\n    "coefficient_upper": "40537/1125",\n    "target": "361/10",\n    "beta_f_upper": "11337738279/10000000000"\n  },\n  {\n    "eta": 5,\n    "nu": 8,\n    "k": "17/5",\n    "ell": "13/5",\n    "Kmin": 75,\n    "sqrt_k_upper": "184391/100000",\n    "sqrt_lambda3_over_nu_upper": "42527/25000",\n    "log_M_upper": "187253/25000",\n    "positive_margin_lower": "1/250",\n    "exact_margin": "261701/60000000",\n    "coefficient_upper": "112391/4000",\n    "target": "281/10",\n    "beta_f_upper": "44950941/40000000"\n  },\n  {\n    "eta": 5,\n    "nu": 10,\n    "k": "3",\n    "ell": "13/5",\n    "Kmin": 85,\n    "sqrt_k_upper": "86603/50000",\n    "sqrt_lambda3_over_nu_upper": "148163/100000",\n    "log_M_upper": "388743/50000",\n    "positive_margin_lower": "11/1000",\n    "exact_margin": "88261/7500000",\n    "coefficient_upper": "239/10",\n    "target": "24",\n    "beta_f_upper": "5578490567/5000000000"\n  },\n  {\n    "eta": 5,\n    "nu": 15,\n    "k": "31/10",\n    "ell": "23/10",\n    "Kmin": 112,\n    "sqrt_k_upper": "176069/100000",\n    "sqrt_lambda3_over_nu_upper": "98007/100000",\n    "log_M_upper": "833483/100000",\n    "positive_margin_lower": "49/1000",\n    "exact_margin": "2207539/45000000",\n    "coefficient_upper": "55753/3000",\n    "target": "93/5",\n    "beta_f_upper": "54992357/50000000"\n  },\n  {\n    "eta": 10,\n    "nu": 4,\n    "k": "39/10",\n    "ell": "31/10",\n    "Kmin": 55,\n    "sqrt_k_upper": "39497/20000",\n    "sqrt_lambda3_over_nu_upper": "170763/50000",\n    "log_M_upper": "671309/100000",\n    "positive_margin_lower": "119/1000",\n    "exact_margin": "476537/4000000",\n    "coefficient_upper": "25847/500",\n    "target": "517/10",\n    "beta_f_upper": "5732823749/5000000000"\n  },\n  {\n    "eta": 10,\n    "nu": 6,\n    "k": "37/10",\n    "ell": "27/10",\n    "Kmin": 67,\n    "sqrt_k_upper": "96177/50000",\n    "sqrt_lambda3_over_nu_upper": "107839/50000",\n    "log_M_upper": "44537/6250",\n    "positive_margin_lower": "11/250",\n    "exact_margin": "3000583/67500000",\n    "coefficient_upper": "104149/3000",\n    "target": "174/5",\n    "beta_f_upper": "226315881/200000000"\n  },\n  {\n    "eta": 10,\n    "nu": 8,\n    "k": "33/10",\n    "ell": "13/5",\n    "Kmin": 73,\n    "sqrt_k_upper": "9083/5000",\n    "sqrt_lambda3_over_nu_upper": "42527/25000",\n    "log_M_upper": "149213/20000",\n    "positive_margin_lower": "43/1000",\n    "exact_margin": "1037519/24000000",\n    "coefficient_upper": "54571/2000",\n    "target": "273/10",\n    "beta_f_upper": "5628033849/5000000000"\n  },\n  {\n    "eta": 10,\n    "nu": 10,\n    "k": "29/10",\n    "ell": "13/5",\n    "Kmin": 82,\n    "sqrt_k_upper": "85147/50000",\n    "sqrt_lambda3_over_nu_upper": "148163/100000",\n    "log_M_upper": "96767/12500",\n    "positive_margin_lower": "1/500",\n    "exact_margin": "8323/3750000",\n    "coefficient_upper": "5779/250",\n    "target": "116/5",\n    "beta_f_upper": "174681953/156250000"\n  },\n  {\n    "eta": 10,\n    "nu": 15,\n    "k": "3",\n    "ell": "23/10",\n    "Kmin": 109,\n    "sqrt_k_upper": "86603/50000",\n    "sqrt_lambda3_over_nu_upper": "98007/100000",\n    "log_M_upper": "830233/100000",\n    "positive_margin_lower": "43/1000",\n    "exact_margin": "1181267/27000000",\n    "coefficient_upper": "16193/900",\n    "target": "18",\n    "beta_f_upper": "5506472913/5000000000"\n  }\n]\n')
for row in record['cutoff_table']:
    eta,nu=row['eta'],row['nu']
    k,ell=F(row['k']),F(row['ell']);lam=ell+F(2,nu)
    assert row['Kmin']==math.floor(k*(math.floor(ell*nu)+2))+1
    sk=F(row['sqrt_k_upper']);sr=F(row['sqrt_lambda3_over_nu_upper']);lm=F(row['log_M_upper'])
    assert sk**2>k and sr**2>lam**3/nu
    assert exp_bounds(lm)[0]>k*lam**2*nu**2+lam*nu
    exact_margin=k*ell**2-k*ell-F(2,3)*sk*lam**2-(2*k/nu+F(4,3)*sr+F(4,3)*lam/nu+3*lm/(eta*nu))
    assert exact_margin==F(row['exact_margin'])>F(row['positive_margin_lower'])>0
    exact_coefficient=k*lam**2+lam/nu+F(1,nu)
    assert exact_coefficient==F(row['coefficient_upper'])<=F(row['target'])
assert exp_bounds(F(11,10))[1]<F(601,200)
assert (F(601,200)*F(9,8))**2<4*F(29,10)
assert (F(601,200)*F(29,25))**2<4*F(33,10)
assert F(1,4)+F(189,50)+F(7,200)==F(813,200)<5
(ROOT/'BL-number-field-endpoints.json').write_text(json.dumps(record,indent=2)+'\n')
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig,axes=plt.subplots(1,3,figsize=(14.3,4.6),constrained_layout=True,
                     gridspec_kw={'width_ratios':[1,1.05,1.35]})
ax=axes[0];ax.scatter([r for r,s in pairs],[s for r,s in pairs],s=42,color='#195a83')
ax.set(xlabel='First coordinate r',ylabel='Second coordinate s',xticks=range(8),yticks=range(8),
       xlim=(-.6,7.6),ylim=(-.6,7.6),title='Selected residue class: r + s ≡ 0 (mod 2)')
ax.set_aspect('equal');ax.grid(alpha=.18)
ax=axes[1];labels=['Exact maximum','Compressed bound','Relaxed class bound','No capacity bound']
vals=[actual,compressed,relaxed,unrestricted]
bars=ax.barh(range(4),list(map(float,vals)),color=['#195a83','#5595ad','#9db3bd','#ceac61'])
for bar,v in zip(bars,vals):ax.text(float(v)+2,bar.get_y()+bar.get_height()/2,str(v),va='center',fontsize=10)
ax.set(yticks=range(4),yticklabels=labels,xlim=(0,265),title='Centered first-coordinate budgets')
ax.invert_yaxis();ax.set_xlabel('Absolute centered sum')
ax=axes[2];bottom=0
for v,label,color in zip(pieces,['Rounding: 3/5','Square roots: 149/75','Coordinate term: 28/75','Logarithm: 117/500'],
                         ['#195a83','#5595ad','#9db3bd','#ceac61']):
    ax.bar(0,float(v),bottom=bottom,width=.7,label=label,color=color);bottom+=float(v)
ax.axhline(float(left),ls='--',color='#a04632',label='Left lower bound: 3848/1125')
ax.text(-.7,float(left)+.08,f'Gap\n{margin}',va='bottom',fontsize=9)
ax.set(ylim=(0,4.85),xlim=(-.8,1.25),xticks=[],ylabel='Normalized sufficient comparison',
       title='Uniform strict determinant margin')
ax.legend(loc='upper right',fontsize=8)
fig.suptitle('Residue capacity and the complete number-field bound: valuation coefficient 23.9 < 24',fontsize=13)
fig.savefig(ROOT/'BL-number-field-occupancy.png',dpi=160);plt.close(fig)
print(json.dumps({'state':record['state'],'margin':str(margin),'valuation_coefficient_upper':str(constant)}))
