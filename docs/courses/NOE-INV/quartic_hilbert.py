"""Exact first constant-term elimination for the ternary-quartic character.

The Weyl numerator uses the three positive roots. For a negative first
weight -r, sum its r residues by tracing in a^r=t*y^b. The normalized trace
is the constant coefficient of the reduced inverse; Cramer's rule computes
it without adjoining roots of unity. No guessed finite truncation is used.
"""
from pathlib import Path
import json,time
from itertools import permutations
from flint import fmpq_mpoly_ctx
from quartic_algebra import indices

ctx=fmpq_mpoly_ctx.get(('t','y'),'lex')
root=Path(__file__).resolve().parent/'quartic-generator-certificates'
root.mkdir(exist_ok=True)
weights=[(i-k,j-k) for i,j,k in indices(4)]
one={(0,0,0):1}

def multiply(p,q,r,b):
    out={}
    for (a,t,y),c in p.items():
        for (d,u,z),e in q.items():
            power=a+d;quotient,power=divmod(power,r)
            key=(power,t+u+quotient,y+z+b*quotient)
            out[key]=out.get(key,0)+c*e
    return {e:c for e,c in out.items() if c}

def determinant(m):
    n=len(m);answer=ctx.constant(0)
    for p in permutations(range(n)):
        sign=(-1)**sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        term=ctx.constant(sign)
        for i,j in enumerate(p):term*=m[i][j]
        answer+=term
    return answer

def residue(index):
    a,b=weights[index];r=-a
    denominator=one
    for j,(u,v) in enumerate(weights):
        if j==index:continue
        denominator=multiply(denominator,{(0,0,0):1,(u,1,v):-1},r,b)
    numerator=one
    for u,v in ((-1,1),(-2,-1),(-1,-2)):
        numerator=multiply(numerator,{(0,0,0):1,(u,0,v):-1},r,b)
    columns=[multiply(denominator,{(j,0,0):1},r,b) for j in range(r)]
    all_terms=[e for column in columns for e in column]+list(numerator)
    shift_t=max(0,-min(e[1] for e in all_terms))
    shift_y=max(0,-min(e[2] for e in all_terms))
    def coefficient(p,i):
        return ctx.from_dict({(t+shift_t,y+shift_y):c for (a,t,y),c in p.items() if a==i})
    matrix=[[coefficient(p,i) for p in columns] for i in range(r)]
    modified=[row.copy() for row in matrix]
    for i in range(r):modified[i][0]=coefficient(numerator,i)
    n,d=determinant(modified),determinant(matrix)
    assert d
    g=n.gcd(d);n=n//g;d=d//g
    return n,d

def serialize(p):
    return [{'exponents':[int(i) for i in e],'coefficient':str(c)} for e,c in p.to_dict().items()]

if __name__=='__main__':
    start=time.monotonic();rows=[]
    for i,(a,b) in enumerate(weights):
        if a>=0:continue
        n,d=residue(i)
        rows.append({'weight':[a,b],'numerator':serialize(n),'denominator':serialize(d)})
        print('First-variable residue',a,b,'terms',len(n.to_dict()),len(d.to_dict()),flush=True)
    (root/'first-variable-residues.json').write_text(json.dumps({'weights':weights,'positive_roots':[[-1,1],[-2,-1],[-1,-2]],'residues':rows,'elapsed_seconds':time.monotonic()-start},indent=2)+'\n',encoding='utf8',newline='\n')
    print('Elapsed',time.monotonic()-start,flush=True)
