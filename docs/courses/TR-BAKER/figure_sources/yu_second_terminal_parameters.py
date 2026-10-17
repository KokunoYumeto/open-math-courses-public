"""Exact endpoint comparisons for the final second-scale integer extension.

GPT-6 Astra (OpenAI), Ultra. CC0.
The accompanying proof establishes each all-rank enclosure and its scope.
This certificate does not claim the remaining fixed-order induction.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from yu_second_fractional_profile import case_data, exp_bounds


def calculate():
    lam, xi = F(59,58), F(101,100)
    stated = {
        'I.1': (F(91,1000),F(33,100)),
        'I.2': (F(91,1000),F(11,50)),
        'II': (F(91,1000),F(27,100)),
        'III.1': (F(66,1000),F(29,100)),
        'III.2': (F(66,1000),F(11,25)),
        'IV': (F(49,1000),F(29,50)),
        'V': (F(1,20),F(3,4)),
    }
    result=[]
    for name,c1,c3,c4,a,q,zeta,amin,dmin,w,nu,chi,*_ in case_data():
        c2=F(a,q*q)/zeta
        c=F(27,50) if q==2 else F(4,5)
        ell=F(7,50) if q==2 else F(11,50)
        em,ep=exp_bounds(c);hp=1/em
        rows=[]
        for r in range(3 if q==2 else 4,9):
            tail=r==8;y=F(1,r+1);eta=1-c*y
            sm=c3*q*dmin/y**2;tm=F(12,29)*(r+1)*12**r
            W=(w/(2*c2)*(1+1/(2*sm))+y*y/(c2*c3*q)
                +(1+w/2)*c1*F(13,18000)
                +(1+w)*c1*(F(1,79)+F(1,71928*1500)))
            L=(2*c*q*(1/ep if tail else eta**r)*(1-1/(2*q**r*sm))
                -lam*nu/(c4*q**r))
            b=lam*(1+(r+1)*ell+w+ell/(q-1))
            k=((F(107,103)+F(3,8)*y)*(hp**2 if tail else eta**(r+1)*hp)
                +w*(1 if tail else 1-F(483,824)*y))
            J=c1*chi*q-xi*(1/tm+c*y*(1 if tail else eta**r))/(q**r*c3*(1+amin))
            for endpoint,v in [('minimum',(b*amin/c4+k/c3)/(1+amin)),('infinity',b/c4)]:
                arithmetic=F(q)/c2+W/q**r+xi*v/q**r
                mass_gap,input_gap=L-arithmetic,J-arithmetic
                assert mass_gap>stated[name][0] and input_gap>stated[name][1]
                assert mass_gap>F(1,25) and input_gap>F(1,5)
                rows.append({'rank':'all >=8' if tail else r,'A0_endpoint':endpoint,
                    'mass_lower':str(L),'input_lower':str(J),'arithmetic_upper':str(arithmetic),
                    'mass_gap':str(mass_gap),'input_gap':str(input_gap)})
        result.append({'case':name,'comparisons':rows,'strict_mass_margin':str(stated[name][0]),
            'strict_input_margin':str(stated[name][1]),
            'minimum_mass_gap':str(min(F(x['mass_gap']) for x in rows)),
            'minimum_input_gap':str(min(F(x['input_gap']) for x in rows))})
    assert sum(len(x['comparisons']) for x in result)==82
    degree=F(2436,5*16*2**13);root=F(45,8)/lam
    assert degree==F(609,163840)<1 and root==F(1305,236)>1
    return {'state':'exact_final_integer_comparisons_passed','endpoint_combinations':82,
        'inequalities_checked':164,'cases':result,
        'strict_torus_degree_upper':str(degree),'strict_root_count_factor':str(root),
        'scope':'Final integer extension j=r at any permitted contracted depth; actual multiplicity-stop starting block; conditional final additive-polynomial contradiction. Fixed-order fractional/successor induction remains unproved.'}


def render(data, destination):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    fig,axs=plt.subplots(1,2,figsize=(12,4.8),layout='constrained',gridspec_kw={'width_ratios':[1.25,1]})
    x=list(range(7));a=axs[0]
    mass=[F(row['strict_mass_margin']) for row in data['cases']]
    inp=[F(row['strict_input_margin']) for row in data['cases']]
    a.bar([v-.18 for v in x],[float(v) for v in mass],width=.34,color='#176b87',label='Mass minus arithmetic')
    a.bar([v+.18 for v in x],[float(v) for v in inp],width=.34,color='#267d69',label='Input minus arithmetic')
    for i,(m,n) in enumerate(zip(mass,inp)):
        a.text(i-.18,float(m)+.012,str(m),ha='center',va='bottom',fontsize=7,rotation=90)
        a.text(i+.18,float(n)+.012,str(n),ha='center',va='bottom',fontsize=7,rotation=90)
    a.set(xticks=x,xticklabels=[row['case'] for row in data['cases']],ylim=(0,.93),
          title='The final integer extension j = r',ylabel='Strict lower gap in normalized valuation')
    a.legend(loc='upper left',fontsize=8);a.grid(axis='y',alpha=.18);a.set_axisbelow(True)
    b=axs[1];b.axis('off');b.set_title('Conditional on the final stage zeros')
    boxes=[(.82,r'Integral support: $|m_i|<609/327680<1$'+'\n'+r'Every $m_i=0$'),
           (.48,r'Nonzero additive polynomial $P(X)$'+'\n'+r'$\deg P\leq D_{\mathrm{a}}$'),
           (.14,r'$2R+1>(1305/236)D_{\mathrm{a}}>D_{\mathrm{a}}$'+'\n'+'Too many distinct integer roots')]
    for y,label in boxes:
        b.text(.5,y,label,ha='center',va='center',transform=b.transAxes,fontsize=11,
               bbox={'boxstyle':'round,pad=.65','fc':'#edf5f6','ec':'#176b87'})
    for y0,y1 in [(.70,.60),(.36,.26)]:
        b.annotate('',xy=(.5,y1),xytext=(.5,y0),xycoords='axes fraction',arrowprops={'arrowstyle':'->','lw':1.5})
    fig.savefig(destination,dpi=160);plt.close(fig)


if __name__=='__main__':
    data=calculate()
    Path(__file__).with_name('second-terminal-parameters-check.json').write_text(json.dumps(data,indent=2)+'\n')
    import sys
    if '--figure' in sys.argv:
        render(data,Path(__file__).with_name('yu-second-terminal-parameters.png'))
    print(json.dumps({k:v for k,v in data.items() if k!='cases'}))
