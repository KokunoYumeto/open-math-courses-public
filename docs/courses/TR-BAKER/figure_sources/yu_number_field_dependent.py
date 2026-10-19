"""Exact checks and original diagram for TR-BAKER-10, Section 80.

GPT-6 Astra (OpenAI), Ultra. CC0; font glyphs retain their licences.
The uniform proofs are Lemmas 10.240–10.241 and Theorem 10.242.
Finite arithmetic checks below illustrate and check their exact transfers.
"""
from pathlib import Path
from fractions import Fraction as F
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

out = Path(__file__).resolve().parent

def mul(x,y):
    return (x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0])

def power(x,n):
    z=(1,0)
    for _ in range(n): z=mul(z,x)
    return z

def valuation(n,p):
    if n==0:return 'infinity'
    k=0
    while n%p==0:n//=p;k+=1
    return k

a=(1,1);c=(6,1);ac=mul(a,c)
product=mul(power(ac,2),power((3,0),6))
assert ac==(8,7)
assert product==(118098,81648)
assert (108*108-2)%343==0
assert (product[0]+108*product[1]-1)%343==245
assert mul(mul(a,c),ac)==power(ac,2)
cases=[]
for multiplier,b in [(1,(1,1,1,6)),(7,(1,1,1,6)),(1,(1,-1,1,6))]:
    k=(-multiplier,-multiplier,multiplier,0);x=2
    reduced=tuple(k[x]*b[i]-k[i]*b[x] for i in (0,1,3))
    original_min=min(valuation(v,7) for v in b if v)
    expected=valuation(k[x],7)+original_min
    assert min(valuation(v,7) for v in reduced if v)==valuation(reduced[-1],7)==expected
    Bnew=2*multiplier*6;Bnnew=multiplier*6
    epsnew=F(k[x],2*multiplier)*F(1,2)*F(1,16)
    assert epsnew*Bnew/Bnnew==F(1,2)*F(1,16)
    cases.append({'relation':k,'original_coefficients':b,'reduced_coefficients':reduced,'B_new':Bnew,'Bn_new':Bnnew,'epsilon_new':str(epsnew),'minimum_valuation':expected})

margins={
    'A_squared_over_Q_coefficient_below_30':F(30)-F(58**2,16)/F(8,3)**2,
    'log_fifth_power_envelope_below_70':F(70)-3*F(15,8)**5,
    '2100_below_2_to_12':F(2**12-2100),
    'rank_one_target_margin':1-F(12,16**4),
    'redundant_rank_absorption':1-F(4,16),
    'internal_rank_absorption':1-F(2,16),
}
assert all(v>0 for v in margins.values())
# Polynomial identities used in the proof, recorded coefficientwise.
# D_n=6n^2+11n+5; D_n-(3n+11)=6n^2+8n-6
# =6(n-2)^2+32(n-2)+34 >0 for n>=2.
assert (6,8,-6)==(6,32-24,24-64+34)
# D_n-D_(n-1)=12n+5.
assert (12,11-6)==(12,5)
certificate={'state':'passed','scope':'Exact rational margins, polynomial identities, quadratic-field arithmetic and three coefficient transfers; uniform proof supplied in Section80, not inferred from finite sampling.','margins':{k:str(v) for k,v in margins.items()},'transfers':cases,'quadratic_product':product,'root_mod_343':108,'product_minus_one_mod_343':245,'exact_valuation':2,'field_scope':'odd p, or p=2 with zeta3 in K; original d,e,f retained'}
(out/'yu-number-field-dependent-check.json').write_text(json.dumps(certificate,indent=2)+'\n',encoding='utf-8')

plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
fig,ax=plt.subplots(figsize=(13.2,8.2));fig.patch.set_facecolor('#f8fafc');ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
ax.text(.5,.985,'Dependence and the distinguished coefficient',ha='center',va='top',fontsize=19,weight='bold',color='#162b43')
ax.text(.5,.905,r'Original field data and weights: $d,e,f,N$, $w_i\geq Q^{-1}$, $h(\beta_i)\leq Jw_i$',ha='center',fontsize=13)

def box(x,y,w,h,title,lines,colour,gap=.06):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012',linewidth=1.5,edgecolor=colour,facecolor='white'))
    ax.text(x+.025,y+h-.035,title,color=colour,fontsize=15,weight='bold',va='top')
    for j,line in enumerate(lines): ax.text(x+.025,y+h-.105-gap*j,line,fontsize=12,va='top')

box(.045,.445,.43,.395,'Last base is redundant',[
    r'Choose an independent basis among $i<n$.',
    r'$D=w_K[M_K:\mathbb{Z}^s]$ clears denominators.',
    r'$Y^D=\prod_{j\in I}\beta_j^{M_j}$ exactly.',
    r'$W\log(2QB^*)<8Q^{n-s}U$',
    r'$4\mathcal{A}_sQ^{n-s}U<\mathcal{A}_nU$'], '#176c86')
box(.525,.445,.43,.395,'Last base raises the rank',[
    r'Use a relation supported on $i<n$.',
    r'Choose $k_x>0$ with minimum $v_p(k_x)$.',
    r"$b'_i=k_xb_i-k_ib_x$,  $b'_n=k_xb_n$",
    r"$v_p(b'_n)=\min_i v_p(b'_i)$",
    r"$U'\leq2QU$,  $2Q\mathcal{A}_{n-1}U<\mathcal{A}_nU$"], '#84549b')
ax.text(.5,.405,'Torsion and rank one use the proved elementary one-logarithm bound.',ha='center',fontsize=12,color='#334155')
box(.045,.045,.91,.32,r'Exact example: $\mathbb{Q}(\sqrt{2})$, $p=7$, $\sqrt{2}\equiv3\ (\mathrm{mod}\ 7)$',[
    r'$a=1+\sqrt{2}$,  $c=6+\sqrt{2}$;   $(a,c,ac,3)$ with coefficients $(1,1,1,6)$',
    r'Relation $(-1,-1,1,0)$  $\longrightarrow$  bases $(a,c,3)$ with coefficients $(2,2,6)$',
    r"$B=B_n=6$, $\varepsilon=1/2$  $\longrightarrow$  $B'=12$, $B'_n=6$, $\varepsilon'=1/64$",
    r'$3^6(ac)^2-1\equiv245=5\cdot49\ (\mathrm{mod}\ 343)$: exact valuation $2$'], '#216b53',gap=.055)
ax.text(.5,.003,'Proof locators: Lemmas 10.240–10.241, Theorem 10.242 and Solution 94.',ha='center',fontsize=11,color='#475569')
fig.savefig(out/'yu-number-field-dependent.png',dpi=165,bbox_inches='tight',facecolor=fig.get_facecolor());plt.close(fig)
print(json.dumps({'state':'passed','exact_margins':len(margins),'coefficient_transfers':len(cases),'valuation':2}))
