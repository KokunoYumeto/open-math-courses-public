"""Exact two-stage elimination for the distinct-tangent normal form."""
from pathlib import Path
import json,time
import sympy as s
from flint import fmpq,fmpq_mpoly_ctx
b=Path(__file__).resolve().parent/'quartic-certificates'
A,B,D,E=s.symbols('A B D E')
local={str(t):t for t in [A,B,D,E]}
ctx=fmpq_mpoly_ctx.get(('D','B','A'),'lex')
def convert(expr):
    p=s.Poly(expr,D,B,A)
    return ctx.from_dict({e:fmpq(int(c.p),int(c.q)) for e,c in p.terms()})
def serialize(p):
    return [{'exponents':[int(i) for i in e],'coefficient':str(c)} for e,c in p.to_dict().items()]
r=json.loads((b/'case-2.1.json').read_text())
polys=[convert(s.fraction(s.cancel(s.sympify(r['values'][n],locals=local).subs(E,s.Rational(9,4)/A)))[0]) for n in ['I9','I12','I15','I18']]
start=time.monotonic();output={'original_substitution':'E=9/(4*A), valid since4*A*E=9','inputs':[serialize(p) for p in polys],'D_resultants':[],'B_resultants':[]}
rd=[]
for i in range(1,4):
    p=polys[0].resultant(polys[i],'D')
    rd.append(p)
    output['D_resultants'].append(serialize(p))
    print('D elimination',i,'degrees',p.degrees(),'terms',len(p.to_dict()),flush=True)
for i,j in [(0,1),(0,2),(1,2)]:
    p=rd[i].resultant(rd[j],'B')
    output['B_resultants'].append(serialize(p))
    print('B elimination',i,j,'degrees',p.degrees(),flush=True)
g=ctx.constant(0)
for p in output['B_resultants']:
    q=ctx.from_dict({tuple(t['exponents']):fmpq(t['coefficient']) for t in p})
    g=g.gcd(q)
output['gcd']=serialize(g);output['elapsed_seconds']=time.monotonic()-start
print('GCD',g.factor(),flush=True)
(b/'case-2.1-resultants.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf8',newline='\n')
