"""Polynomial identities witnessing the two branch ideals.

This small tracked Buchberger calculation is independent of the symbolic
library's Groebner-basis implementation. Its output is checked by multiplying
the stored coefficients by the original input polynomials.
"""
from pathlib import Path
import json,time
import sympy as s
from flint import fmpq,fmpq_mpoly_ctx

root=Path(__file__).resolve().parent/'quartic-certificates'
A,B,D,E=s.symbols('A B D E')
local={str(t):t for t in (A,B,D,E)}
data=json.loads((root/'case-2.1.json').read_text())
source=[s.fraction(s.sympify(data['values'][n],locals=local))[0]
        for n in ('I9','I12','I15','I18')]

def run(expressions,targets,names):
    ctx=fmpq_mpoly_ctx.get(tuple(names),'lex')
    variables=[local[n] for n in names]
    def convert(q):
        return ctx.from_dict({e:fmpq(int(c.p),int(c.q))
                              for e,c in s.Poly(q,*variables).terms()})
    original=[convert(q) for q in expressions]
    zero=ctx.constant(0);one=ctx.constant(1)
    def lead(p):return max(p.to_dict())
    def monomial(e,c):return ctx.from_dict({e:c})
    basis=[]
    def reduce(p,v):
        remainder=zero
        while p:
            e=lead(p);c=p.to_dict()[e]
            for g,w in basis:
                f=lead(g)
                if all(a>=b for a,b in zip(e,f)):
                    q=monomial(tuple(a-b for a,b in zip(e,f)),c/g.leading_coefficient())
                    p=p-q*g;v=[a-q*b for a,b in zip(v,w)]
                    break
            else:
                q=monomial(e,c);remainder=remainder+q;p=p-q
        return remainder,v
    for i,p in enumerate(original):
        v=[one if j==i else zero for j in range(len(original))]
        g,v=reduce(p,v)
        if g:
            c=g.leading_coefficient();basis.append((g/c,[q/c for q in v]))
    pairs={(i,j) for i in range(len(basis)) for j in range(i)}
    processed=0
    while pairs:
        def key(pair):
            a,b=(lead(basis[i][0]) for i in pair)
            l=tuple(max(x,y) for x,y in zip(a,b))
            return (sum(l),l,pair)
        i,j=min(pairs,key=key);pairs.remove((i,j));processed+=1
        a,b=lead(basis[i][0]),lead(basis[j][0])
        if all(min(x,y)==0 for x,y in zip(a,b)):continue
        l=tuple(max(x,y) for x,y in zip(a,b))
        u=monomial(tuple(x-y for x,y in zip(l,a)),fmpq(1))
        v=monomial(tuple(x-y for x,y in zip(l,b)),fmpq(1))
        g,w=reduce(u*basis[i][0]-v*basis[j][0],
                   [u*x-v*y for x,y in zip(basis[i][1],basis[j][1])])
        if g:
            c=g.leading_coefficient();k=len(basis)
            basis.append((g/c,[q/c for q in w]))
            pairs.update((k,h) for h in range(k))
    def serialize(q):
        return [{'exponents':[int(i) for i in e],'coefficient':str(c)}
                for e,c in q.to_dict().items()]
    identities=[]
    for expr in targets:
        target=convert(expr)
        remainder,v=reduce(target,[zero]*len(original))
        assert not remainder
        coefficients=[-q for q in v]
        assert sum((q*p for q,p in zip(coefficients,original)),zero)==target
        identities.append({'target':serialize(target),
                           'coefficients':[serialize(q) for q in coefficients]})
    return {'variables':names,'inputs':[serialize(q) for q in original],
            'identities':identities,'pairs_processed':processed,'basis_size':len(basis)}

start=time.monotonic()
first=[s.expand(q.subs({A:-s.Rational(3,2),E:-s.Rational(3,2)})) for q in source]
result={'first':run(first,[B+D+s.Rational(15,2),(B+s.Rational(15,4))**2],['D','B'])}
print('First identities checked',flush=True)
second=[s.expand(q.subs(E,s.Rational(3,2)-A)) for q in source]+[4*A*A-6*A+9]
result['second']=run(second,[2*A*B/3-5*A-B+D,
                             (B-s.Rational(15,4)+5*A/2)**2],['D','B','A'])
result['elapsed_seconds']=time.monotonic()-start
(root/'branch-identities.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8',newline='\n')
print('Second identities checked; elapsed',result['elapsed_seconds'],flush=True)
