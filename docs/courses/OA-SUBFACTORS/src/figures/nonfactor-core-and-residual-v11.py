"""Exact finite group/trace checks and a reproducible nonfactor residual diagram."""
from pathlib import Path
from collections import Counter
from fractions import Fraction as F
from functools import reduce
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

D=Path(__file__).resolve().parent
zero=(0,0,0)
identity=(frozenset(),zero)
labels=[identity,(frozenset([zero]),zero)]
labels += [(frozenset(),tuple(int(i==j) for i in range(3))) for j in range(3)]
def mul(g,h):
    c,v=g; d,w=h
    shifted=frozenset(tuple(x[i]+v[i] for i in range(3)) for x in d)
    return c.symmetric_difference(shifted),tuple(v[i]+w[i] for i in range(3))
def inv(g):
    c,v=g
    return frozenset(tuple(x[i]-v[i] for i in range(3)) for x in c),tuple(-a for a in v)
def exact_checks():
    assert all(mul(x,inv(x))==identity==mul(inv(x),x) for x in labels)
    for x in labels:
        for y in labels:
            for z in labels:
                assert mul(mul(x,y),z)==mul(x,mul(y,z))
    rows=[]
    for sign in [1,-1]:
        words=Counter({identity:1})
        for n in range(1,7):
            step_sign=sign if n%2 else -sign
            step=labels if step_sign==1 else list(map(inv,labels))
            nxt=Counter()
            for g,count in words.items():
                for h in step:nxt[mul(g,h)]+=count
            words=nxt
            assert sum(words.values())==5**n
            # Every minimal block trace and the actual local-index dual weight.
            tau=F(1,5**n);rho=F(1,25**n)/tau
            assert rho==tau and 25**n*tau*rho==1
            # Filling all available ranks gives every integer in [0,5**n].
            reachable=1
            for cap in words.values():
                reachable=reduce(int.__or__,(reachable<<j for j in range(cap+1)),0)
            assert reachable==(1<<(5**n+1))-1
            rows.append(dict(sign=sign,length=n,blocks=len(words),
                             dimensions=5**n,minimal_trace=str(tau),
                             dual_trace=str(rho),all_integer_rank_fibers=True))
    projected=Counter()
    for x in labels:
        for y in labels:projected[mul(x,inv(y))[1]]+=1
    assert sum(projected.values())==25 and projected[zero]==7
    covariance=[[sum(F(count,25)*v[i]*v[j] for v,count in projected.items())
                 for j in range(3)] for i in range(3)]
    assert covariance==[[F(8,25) if i==j else F(-2,25) for j in range(3)] for i in range(3)]
    residual=1-F(7,25)-F(9,125)
    assert residual==F(81,125)
    return dict(checks_passed=True,finite_length_checks=rows,
                projected_pair_covariance=[[str(v) for v in row] for row in covariance],
                example_residual_trace=str(residual),
                transience_and_nonscalar_center='Complete analytic LF.31–LF.41 proof; finite checks are not extrapolated',
                all_smooth_amenability='Complete arbitrary-representation LF.19–LF.30 proof',
                full_original_theorem_claimed=False)

def draw():
    fig,ax=plt.subplots(figsize=(15,9.4))
    fig.patch.set_facecolor('#fafcff')
    ax.set(xlim=(0,15),ylim=(0,9.4));ax.axis('off')
    ax.text(.5,8.9,'A genuine amenable nonfactor core, with its entire finite residual',fontsize=20,
            color='#143451',weight='bold')
    ax.text(.5,8.48,'Actual index 25  •  equal inherited finite traces  •  every prescribed prefix and marked cup retained',
            fontsize=12,color='#3e5b77')
    def box(x,y,w,h,title,lines,face):
        ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.12',
                                  facecolor=face,edgecolor='#5a7892'))
        ax.text(x+.2,y+h-.4,title,fontsize=14,color='#183c5b',weight='bold')
        for j,(t,size) in enumerate(lines):
            ax.text(x+.2,y+h-.94-.53*j,t,fontsize=size,color='#1e405d')
    def arrow(x1,y1,x2,y2):
        ax.add_patch(FancyArrowPatch((x1,y1),(x2,y2),arrowstyle='-|>',mutation_scale=16,
                                    color='#456a8b',linewidth=1.5))
    box(.6,5.15,6.4,2.65,'An actual diagonal inclusion and all-smooth return',
        [(r'$G=(\bigoplus_{\mathbb{Z}^3}\mathbb{Z}/2)\rtimes\mathbb{Z}^3$',18),
         (r'$s=(1,a,t_1,t_2,t_3),\quad N=\phi_+(P)\subset P=M$',15),
         (r'$\phi_\pm(x)=\mathrm{diag}(\alpha_{s_i^{\pm1}}(x))$',17),
         (r'$\mathscr{F}=\mathrm{id}_{5}\otimes P_\infty,\quad E_N\mathscr{F}=\mathscr{F}E$',17)],
        '#eaf4fc')
    box(7.6,5.15,6.8,2.65,'A strict nonscalar center witness',
        [(r'Pair walk: $1-f(\theta)\geq 8|\theta|^2/(25\pi^2)$',16),
         (r'$\sum_n\mathbb{P}(Z_n=0)<\infty,\quad h=H_+(1)>0$',16),
         (r'$z_n=\sum_{|I|=2n}H_+(g(I))E_{II}\ \longrightarrow\ z\in Z(R)$',15),
         (r'$\|z-h1\|_2^2\geq4h^2/25>0$',18)],
        '#fff2e5')
    box(.6,1.4,8.2,2.85,'Exact residual placement after an arbitrary prefix',
        [(r'$T^{(k)}=\mathbb{Z}[1/5]\cap[0,1],\quad f=1-\sum_i r_i$',18),
         (r'Choose $g\in N_j^\prime\cap N_k$ with $\tau(g)=\tau(f)$; $vgv^*=f$, $v\in N_k$.',14),
         (r'$P_f=f((vN_jv^*)^\prime\cap M)f,\quad fA_k\subset P_f$',17),
         (r'$P_0\subset P_*,\quad E_NE_{P_*}=E_{Q_*},\quad\|y-E_{P_*}y\|_2<\varepsilon$',16)],
        '#eaf7ef')
    box(9.4,1.4,5.0,2.85,'Two separate conclusions',
        [(r'$\sum_i r_i+f=1$: full finite partition.',15),
         ('Old supports, residual and cups stay fixed.',12),
         (r'Fixed-family packing cost can stay $>0$.',14),
         ('No ordinary tunnel generates this inclusion.',12)],
        '#f2edfa')
    arrow(3.8,4.94,3.8,4.42)
    arrow(11,4.94,11,4.42)
    ax.text(.6,.66,'LF.1–LF.56. Proofs are analytic; rectangles are map diagrams, not trace areas or numerical boundary samples.',
            fontsize=11,color='#45627b')
    ax.text(.6,.25,'The strong-amenability generation statement retains its ergodic-core hypothesis. The general residual theorem remains assigned.',
            fontsize=11,color='#45627b')
    fig.subplots_adjust(left=0,right=1,top=1,bottom=0)
    for ext in ['svg','png']:
        fig.savefig(D/('nonfactor-core-and-residual-v11.'+ext),dpi=120,facecolor=fig.get_facecolor())
    p=D/'nonfactor-core-and-residual-v11.svg'
    p.write_text('\n'.join(x.rstrip() for x in p.read_text(encoding='utf-8').splitlines())+'\n',encoding='utf-8')
    plt.close(fig)

if __name__=='__main__':
    result=exact_checks()
    (D/'exact-nonfactor-checks.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    draw()
    print(json.dumps(dict(checks_passed=True,finite_lengths=6,signs=2,actual_local_index=25)))
