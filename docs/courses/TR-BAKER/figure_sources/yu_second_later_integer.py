"""Exact rational comparisons for Theorem 10.206 and Figure 10.62.

GPT-6 Astra (OpenAI), Ultra. Independently authored mathematics and figure; CC0.
The positive coefficient identities and endpoint differences are exact.
The written proof connects these envelopes to the selected-family interpolation
and the full arithmetic height bound. These computations certify its rational inequalities.
"""
from fractions import Fraction as Q
from math import comb
from pathlib import Path
import json
import sympy as sp
from yu_second_fractional_profile import case_data, exp_bounds


def calculate():
    y=sp.symbols('y')
    lam,xi=Q(59,58),Q(101,100)
    eps,rem=Q(13,18000),Q(1,79)+Q(1,71928*1500)
    rows=[];count=0
    for name,c1,c3,c4,a,q,zeta,amin,dmin,w,nfactor,chi,pref,target in case_data():
        c2=Q(a,q*q)/zeta
        c=Q(27,50) if q==2 else Q(4,5)
        ell=Q(7,50) if q==2 else Q(11,50)
        gamma=c3*q*dmin
        elo,ehi=exp_bounds(c);hp=1/elo
        common=(w/(2*c2)*(1+y*y/(2*gamma))+y*y/(c2*c3*q)
                +(1+w/2)*c1*eps+(1+w)*c1*rem)
        polys=[]
        for j in range(1,5):
            eta=1-c*y
            analytic=2*c*q*eta**j*(1-y*y/(2*q**j*gamma))-lam*nfactor/(c4*q**j)
            b=lam*(1+(j+1)*ell+w+ell/(q-1))
            k=(Q(107,103)+Q(3,8)*y)*eta**(j+1)*hp+w*(1-Q(483,824)*y)
            for endpoint in ['minimum','infinity']:
                ratio=b/c4 if endpoint=='infinity' else (b*amin/c4+k/c3)/(1+amin)
                poly=sp.Poly(sp.expand(analytic-Q(q)/c2-common/q**j-xi*ratio/q**j),y)
                n=j+2;interval=Q(1,max(4 if q==2 else 5,j+2))
                assert poly.degree()<=n
                coeff=[Q(poly.nth(i))*interval**i for i in range(n+1)]
                bern=[sum(coeff[k]*Q(comb(i,k),comb(n,k)) for k in range(i+1)) for i in range(n+1)]
                identity=sum(bern[i]*comb(n,i)*(y/interval)**i*(1-y/interval)**(n-i) for i in range(n+1))
                assert sp.expand(identity-poly.as_expr())==0
                assert min(bern)>Q(1,4)
                count+=len(bern)
                polys.append({'step':j,'endpoint':endpoint,'interval_upper':str(interval),
                              'bernstein_coefficients':list(map(str,bern)),
                              'minimum':str(min(bern))})
        y6=Q(1,7);s6=gamma/y6**2
        al=2*c*q/ehi*(1-1/(2*q**5*s6))-lam*nfactor/(c4*q**5)
        com=Q(common.subs(y,y6));b=lam*(1+6*ell+w+ell/(q-1))
        k=(Q(107,103)+Q(3,8)*y6)*hp+w
        tail=[al-Q(q)/c2-com/q**5-xi*ratio/q**5
              for ratio in [b/c4,(b*amin/c4+k/c3)/(1+amin)]]
        assert min(tail)>Q(3,100)
        r0=3 if q==2 else 4;y0=Q(1,r0+1);tm=Q(12,29)*(r0+1)*12**r0
        il=c1*chi*q*q-xi*(1/tm+c*y0)/(q*c3*(1+amin))
        au=(Q(q)/c2+Q(common.subs(y,y0))/q
            +xi/q*(lam*(1+w+ell/(q-1)+2*ell)/c4
                   +((Q(107,103)+Q(3,8)*y0)*hp+w)/(c3*(1+amin))))
        assert il-au>Q(7,5)
        rows.append({'case':name,'finite_polynomials':polys,'tail_endpoint_gaps':list(map(str,tail)),
                     'input_lower':str(il),'arithmetic_upper':str(au),'input_gap':str(il-au),
                     'exp_c_lower':str(elo),'exp_c_upper':str(ehi)})
    assert count==308
    return {'state':'exact_later_integer_comparisons_passed',
            'finite_polynomials':56,'bernstein_coefficients':308,'tail_endpoint_checks':14,
            'input_checks':7,'finite_mass_gap':'1/4','tail_mass_gap':'3/100','input_gap':'7/5',
            'cases':rows,'proof_note':'TR-BAKER-10 Theorem10.206 and Solution83'}


def counting_example():
    q,r,depth=2,3,2
    c=Q(27,50);eta=1-c/Q(r+1);hf=eta**(r+1)
    s=Q(21,2)/hf**depth;t=Q(1200)*hf**depth
    rows=[]
    for j in range(1,r+1):
        radius=(q**j*s).__floor__();order=(eta**j*t).__floor__()
        mu=(c*eta**j*t/(r+1)).__floor__()+1
        if j<r:assert (eta**(j+1)*t).__floor__()+mu-1<=order
        rows.append({'step':j,'radius':radius,'order':order,'multiplicity_to_next':mu if j<r else None,
                     'cardinal_degree':(2*radius+1)*mu if j<r else None})
    return {'q':q,'rank':r,'depth':depth,'eta':str(eta),'S_I':str(s),'T_I':str(t),'rows':rows,
            'scope':'Exact floor-counting illustration, not a number-field parameter instance.'}


def draw_figure(destination,example):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig,axs=plt.subplots(1,2,figsize=(11.6,4.8),gridspec_kw={'width_ratios':[1.5,1]})
    ax=axs[0];colors=['#176b87','#2a9d8f','#6a4c93']
    for row,col in zip(example['rows'],colors):
        j=row['step'];rad=row['radius'];order=row['order']
        ax.plot([-rad,rad],[j,j],lw=9,color=col,solid_capstyle='butt')
        ax.text(rad+10,j,f'radius {rad}\norder {order}',va='center',fontsize=10)
        if j<3:
            ax.annotate('',xy=(0,j+0.84),xytext=(0,j+0.16),arrowprops={'arrowstyle':'->','color':'#222','lw':1.4})
            ax.text(8,j+0.5,f"multiplicity {row['multiplicity_to_next']}",va='center',fontsize=9)
    ax.set_xlim(-max(x['radius'] for x in example['rows'])*1.08,max(x['radius'] for x in example['rows'])*1.75)
    ax.set_ylim(3.45,.55);ax.set_yticks([1,2,3],['j = 1','j = 2','j = 3']);ax.set_xlabel('Integer node s; every integer in the bar is included')
    ax.set_title('Exact floors at contraction depth I = 2',fontsize=12)
    ax.grid(axis='x',alpha=.15)
    ax=axs[1];values=[.25,.03,1.4];labels=['Steps 1–4','Steps 5 onward','Input entry']
    bars=ax.bar(range(3),values,color=['#176b87','#2a9d8f','#6a4c93'],width=.65)
    for bar,lab in zip(bars,['1/4','3/100','7/5']):ax.text(bar.get_x()+bar.get_width()/2,bar.get_height()+.035,lab,ha='center',fontsize=12)
    ax.set_xticks(range(3),labels,fontsize=9);ax.set_ylim(0,1.66);ax.set_ylabel('Strict lower comparison margin');ax.set_title('Bounds proved for all admissible cases',fontsize=12)
    ax.grid(axis='y',alpha=.15);ax.set_axisbelow(True)
    fig.suptitle('Integer extension: radius growth, jet orders and comparison margins',fontsize=14,y=.99)
    fig.text(.5,.015,'Theorem 10.206 and Solution 83 · left: counting illustration · right: exact proved bounds',ha='center',fontsize=9)
    fig.tight_layout(rect=[0,.055,1,.94]);fig.savefig(destination,dpi=160);plt.close(fig)


if __name__=='__main__':
    data=calculate();data['counting_example']=counting_example()
    here=Path(__file__).resolve().parent
    (here/'second-later-integer-check.json').write_text(json.dumps(data,indent=2)+'\n')
    draw_figure(here/'yu-second-later-integer.png',data['counting_example'])
    print(json.dumps({k:v for k,v in data.items() if k!='cases'}))
