"""Independent CC0 exact checks for the physical modified-cup bias.

The PG input is the proved actual S_3 x Z tower PG1--PG18, not a new
subfactor construction. No asymptotic assertion is inferred from computation.
"""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import math

ROOT = Path(__file__).resolve().parent
ID = (0, 1, 2)
A = (1, 0, 2)
B = (0, 2, 1)
ONE = (ID, 0)
LABELS = (ONE, (A, 1), (B, 0))
ODD = (F(1, 4), F(1, 2), F(1, 4))
EVEN = (F(2, 5), F(1, 5), F(2, 5))
LAMBDA = F(1, 100)


def mul(g, h):
    p, r = g
    q, s = h
    return tuple(p[q[j]] for j in range(3)), r + s


def inv(g):
    p, r = g
    q = [0, 0, 0]
    for i, j in enumerate(p):
        q[j] = i
    return tuple(q), -r


def pow2(r):
    return F(2**r) if r >= 0 else F(1, 2**(-r))


def convolution(x, y):
    out = Counter()
    for g, a in x.items():
        for h, b in y.items():
            out[mul(g, h)] += a * b
    return out


H = Counter(mul(inv(a), c) for a in LABELS for c in LABELS)
PREFIX = [(a, c, mul(inv(LABELS[a]), LABELS[c]), ODD[a] * EVEN[c])
          for a in range(3) for c in range(3)]


def rational_row(m, tail, suffix):
    """Haar coefficients on actual U=C_[1,2m], V=C_[3,2m]."""
    suffix_prob = {h: F(n, 10**(m-1)) / pow2(h[1])
                   for h, n in suffix.items()}
    assert sum(suffix_prob.values()) == 1
    assert sum(F(n, 10**(m-1))*pow2(h[1]) for h,n in suffix.items()) == 1
    ordinary = modified = excess = cross = F(0)
    for a, c, p, physical_weight in PREFIX:
        kappa = pow2(2*p[1])
        assert physical_weight == F(1,10)/pow2(p[1])
        assert kappa*physical_weight == EVEN[a]*ODD[c]
        mean = F(0)
        for h, n in suffix.items():
            coefficient = physical_weight*F(tail.get(mul(p,h),0), n)
            prob = suffix_prob[h]
            centered = coefficient-LAMBDA
            mean += prob*coefficient
            ordinary += physical_weight*prob*centered**2
            modified += physical_weight*prob*(kappa*coefficient-LAMBDA)**2
            excess += physical_weight*prob*kappa**2*centered**2
            cross += physical_weight*prob*kappa*(kappa-1)*centered
        assert mean == LAMBDA
    floor = LAMBDA**2 * sum(w*(pow2(2*p[1])-1)**2 for _,_,p,w in PREFIX)
    assert floor == F(9,80000)
    assert cross == 0
    assert modified == floor+excess
    assert F(1,16)*ordinary <= excess <= 16*ordinary
    return {'m':m, 'ordinary_variance':str(ordinary), 'modified_scalar_error':str(modified),
            'bias_floor':str(floor), 'centered_excess':str(excess),
            'orthogonal_cross_term':str(cross), 'normalization_checks':'exact'}


def float_row(m, tail, suffix):
    # Integers remain exact; only the plotted trace arithmetic uses float.
    den = 10**(m-1)
    ordinary = modified = excess = 0.0
    for _,_,p,physical_weight in PREFIX:
        weight = float(physical_weight)
        kappa = math.ldexp(1.0,2*p[1])
        for h,n in suffix.items():
            prob = n/den * math.ldexp(1.0,-h[1])
            coefficient = weight*tail.get(mul(p,h),0)/n
            centered = coefficient-float(LAMBDA)
            ordinary += weight*prob*centered**2
            modified += weight*prob*(kappa*coefficient-float(LAMBDA))**2
            excess += weight*prob*kappa**2*centered**2
    floor = float(F(9,80000))
    assert abs(modified-floor-excess) < 2e-15
    return {'m':m,'ordinary_variance':ordinary,'modified_scalar_error':modified,
            'centered_excess':excess,'bias_floor':floor}


def density_floor(weights, coefficients, cup):
    assert sum(weights)==1 and sum(w*k for w,k in zip(weights,coefficients))==1
    variance = sum(w*(k-1)**2 for w,k in zip(weights,coefficients))
    return {'density_variance':str(variance),'cup_parameter':str(cup),
            'bias_floor':str(cup**2*variance)}


def sparse_matrix_unit_check():
    """Separate Q(sqrt(2)) matrix-unit check at the actual first blocked stage."""
    def add(x,y):
        return x[0]+y[0],x[1]+y[1]
    def mult(x,y):
        return x[0]*y[0]+2*x[1]*y[1],x[0]*y[1]+x[1]*y[0]
    zero=(F(0),F(0))
    def charge(word,start=1):
        g=ONE
        for pos,j in enumerate(word,start):
            g=mul(g,inv(LABELS[j]) if pos%2 else LABELS[j])
        return g
    def square(matrix):
        ans={}
        for (u,v),a in matrix.items():
            for (v2,w),b in matrix.items():
                if v2==v:
                    ans[u,w]=add(ans.get((u,w),zero),mult(a,b))
        return {k:v for k,v in ans.items() if v!=zero}
    words=list(product(range(3),repeat=4))
    weight={u:ODD[u[0]]*EVEN[u[1]]*ODD[u[2]]*EVEN[u[3]] for u in words}
    suffix_blocks={}
    for u in product(range(3),repeat=2):
        suffix_blocks.setdefault(charge(u,start=3),[]).append(u)
    mats={}
    for name,sign in [('ordinary',1),('modified',-1)]:
        q={}
        for a,c,b,d in product(range(3),repeat=4):
            row=(a,c,c,a); col=(b,d,d,b)
            exponent=sign*((a==1)-(c==1)+(b==1)-(d==1))
            coefficient=F(1,10)*pow2(exponent//2)
            q[row,col]=(coefficient,F(0)) if exponent%2==0 else (F(0),coefficient)
            assert charge(row)==charge(col)==ONE
        assert square(q)==q
        trace=sum(weight[u]*q[u,u][0] for u in [(a,c,c,a) for a,c in product(range(3),repeat=2)])
        assert trace==LAMBDA
        averaged={}
        for (u,v),value in q.items():
            if u[2:]!=v[2:]:
                continue
            block=suffix_blocks[charge(u[2:],start=3)]
            for tailword in block:
                row=u[:2]+tailword; col=v[:2]+tailword
                new=value[0]/len(block),value[1]/len(block)
                averaged[row,col]=add(averaged.get((row,col),zero),new)
        assert all(u==v and z[1]==0 for (u,v),z in averaged.items())
        variance=sum(weight[u]*(averaged.get((u,u),zero)[0]-LAMBDA)**2 for u in words)
        assert variance==F(19,20000)
        mats[name]={'projection_check':'exact Q(sqrt(2))','physical_trace':str(trace),
                    'physical_Haar_scalar_error':str(variance),
                    'Haar_matrix_units':sum(len(b)**2 for b in suffix_blocks.values())}
    return mats


def run():
    exact=[]
    plotted=[]
    tail=Counter({ONE:1})
    suffix=H
    for m in range(2,65):
        if m<=12:
            exact.append(rational_row(m,tail,suffix))
        plotted.append(float_row(m,tail,suffix))
        tail=suffix
        suffix=convolution(suffix,H)
    assert exact[0]['ordinary_variance']=='19/20000'
    assert exact[0]['modified_scalar_error']=='19/20000'
    assert exact[0]['centered_excess']=='67/80000'
    for x,y in zip(plotted,plotted[1:]):
        assert y['ordinary_variance']<=x['ordinary_variance']+2e-15
        assert y['modified_scalar_error']<=x['modified_scalar_error']+2e-15
    data={'schema':'physical-modified-cup-bias-checks/v1','license':'CC0-1.0',
          'mathematical_scope':'ACT.1--ACT.8 finite bias and actual PG Haar values; no general bicommutant proof',
          'one_step_floors':{
              'weighted_spin_p_1_4':density_floor([F(1,4),F(3,4)],[F(3),F(1,3)],F(3,16)),
              'PG_target_j_even':density_floor(EVEN,[F(5,8),F(5,2),F(5,8)],F(1,10)),
              'PG_target_j_odd':density_floor(ODD,[F(8,5),F(2,5),F(8,5)],F(1,10))},
          'separate_sparse_matrix_unit_check':sparse_matrix_unit_check(),
          'exact_PG_blocked_rows':exact,'plotted_PG_blocked_rows':plotted,
          'figure_boundary':'Actual finite physical Haar values. PG14 proves their stated limit; samples do not prove a convergence rate.'}
    (ROOT/'physical-cup-bias-checks.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
    print(json.dumps({'exact_rows':len(exact),'plotted_rows':len(plotted),
                      'initial_blocked_row':exact[0],'one_step_floors':data['one_step_floors'],
                      'last_plotted_row':plotted[-1]},indent=2))
    make_figure(data)


def make_figure(data):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig = plt.figure(figsize=(11.8,8.0),facecolor='#fbfaf6',layout='constrained')
    gs = fig.add_gridspec(2,1,height_ratios=[0.68,1.0])
    top=fig.add_subplot(gs[0]); top.axis('off')
    top.text(0.02,0.92,'The natural reflection retains a fixed physical bias',
             fontsize=18,fontweight='bold',color='#25334a',transform=top.transAxes)
    top.text(0.02,0.73,r'$Q_m(g)-\lambda 1=\lambda(\kappa-1)+\kappa^{1/2}[Q_m(e)-\lambda 1]\kappa^{1/2}$',
             fontsize=17,color='#25334a',transform=top.transAxes)
    top.text(0.02,0.53,r'$\|Q_m(g)-\lambda 1\|_2^2=\lambda^2\tau[(\kappa-1)^2]+\|\kappa^{1/2}[Q_m(e)-\lambda 1]\kappa^{1/2}\|_2^2$',
             fontsize=15,color='#25334a',transform=top.transAxes)
    top.text(0.02,0.32,'The two terms are orthogonal: the second has expectation zero onto the fixed upper factor.',
             fontsize=12,color='#41516a',transform=top.transAxes)
    top.text(0.02,0.11,'ACT.1--ACT.5: every finite depth; physical normalized trace; no infinite reflection map.',
             fontsize=12,color='#41516a',transform=top.transAxes)
    ax=fig.add_subplot(gs[1]); ax.set_facecolor('#ffffff')
    rows=data['plotted_PG_blocked_rows']; depths=[r['m'] for r in rows]
    ax.semilogy(depths,[r['modified_scalar_error'] for r in rows],color='#ab4f21',lw=2.5,
                label=r'Modified scalar error $w_m^2$')
    ax.semilogy(depths,[r['ordinary_variance'] for r in rows],color='#176d8d',lw=2.5,
                label=r'Ordinary cup variance $v_m$')
    ax.axhline(float(F(9,80000)),color='#806332',ls='--',lw=1.7,
               label=r'Exact modified bias floor $9/80000$')
    ax.scatter([2],[float(F(19,20000))],s=38,color='#25334a',zorder=4)
    ax.annotate(r'$v_2=w_2^2=19/20000$',xy=(2,float(F(19,20000))),xytext=(8,0.00070),
                fontsize=11,arrowprops={'arrowstyle':'->','color':'#41516a'})
    ax.set_xlabel('Finite blocked depth m in the actual PG tower',fontsize=12)
    ax.set_ylabel('Physical squared norm',fontsize=12)
    ax.set_title('PG: U = C[1, 2m], V = C[3, 2m], ordinary Q₀ and its canonical modification',
                 loc='left',fontsize=13,pad=13)
    ax.grid(alpha=0.16,which='both'); ax.legend(loc='upper right',fontsize=11,frameon=False)
    ax.spines[['top','right']].set_visible(False)
    fig.savefig(ROOT/'physical-modified-cup-bias-v27.png',dpi=180,facecolor=fig.get_facecolor())
    plt.close(fig)


if __name__=='__main__':
    run()
