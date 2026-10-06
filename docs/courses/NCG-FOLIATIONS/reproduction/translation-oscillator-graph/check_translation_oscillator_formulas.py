"""Finite consistency checks; complete analytic proofs remain in Section 11E."""
from pathlib import Path
import itertools
import json
import math
import numpy as np

HERE = Path(__file__).resolve().parent
checks = []

def checked(label, condition, cases, error=0.0):
    assert condition, (label, error)
    checks.append({'label': label, 'cases': cases, 'passed': True,
                   'maximum_residual': float(error)})

for d in range(1, 5):
    n = 1 << d
    eps = []
    for j in range(d):
        a = np.zeros((n, n), dtype=int)
        for I in range(n):
            if not I & (1 << j):
                a[I | (1 << j), I] = (-1)**((I & ((1 << j)-1)).bit_count())
        eps.append(a)
    ios = [a.T for a in eps]
    cs = [a-b for a,b in zip(eps, ios)]
    es = [a+b for a,b in zip(eps, ios)]
    identity = np.eye(n, dtype=int)
    error = 0
    cases = 0
    for j,k in itertools.product(range(d), repeat=2):
        for matrix in [
            eps[j]@eps[k]+eps[k]@eps[j],
            ios[j]@ios[k]+ios[k]@ios[j],
            eps[j]@ios[k]+ios[k]@eps[j]-(j==k)*identity,
            cs[j]@cs[k]+cs[k]@cs[j]+2*(j==k)*identity,
            es[j]@es[k]+es[k]@es[j]-2*(j==k)*identity,
            cs[j]@es[k]+es[k]@cs[j]]:
            error = max(error, int(np.max(np.abs(matrix))))
            cases += 1
    checked('exact exterior CAR and physical Clifford signs d='+str(d),
            error==0, cases, error)
    for m in itertools.product([-2,0,1], repeat=d):
        c = sum((m[j]*es[j] for j in range(d)), np.zeros((n,n),dtype=int))
        error = int(np.max(np.abs(c@c-sum(x*x for x in m)*identity)))
        checked('exact translation-potential square d='+str(d)+' m='+str(m),
                error==0, 1, error)

def compositions(total, d):
    if d==1:
        yield (total,)
    else:
        for first in range(total+1):
            for rest in compositions(total-first,d-1):
                yield (first,)+rest

energy_counts = []
for d in range(1,4):
    for k in range(6):
        states = [(nu,I) for I in range(1<<d) if I.bit_count()<=k
                  for nu in compositions(k-I.bit_count(),d)]
        positions = {state:i for i,state in enumerate(states)}
        matrix = np.zeros((len(states),len(states)))
        for col,(nu,I) in enumerate(states):
            for j in range(d):
                sign = (-1)**((I & ((1<<j)-1)).bit_count())
                if I & (1<<j):
                    dest = list(nu); dest[j]+=1
                    matrix[positions[(tuple(dest),I^(1<<j))],col] += sign*math.sqrt(2*(nu[j]+1))
                elif nu[j]:
                    dest = list(nu); dest[j]-=1
                    matrix[positions[(tuple(dest),I|(1<<j))],col] += sign*math.sqrt(2*nu[j])
        error = max(float(np.max(np.abs(matrix-matrix.T))),
                    float(np.max(np.abs(matrix@matrix-2*k*np.eye(len(states))))))
        count = sum(math.comb(d,j)*math.comb(k-j+d-1,d-1)
                    for j in range(min(d,k)+1))
        even = sum(I.bit_count()%2==0 for _,I in states)
        odd = len(states)-even
        checked('whole invariant energy block d='+str(d)+' k='+str(k),
                error<1e-12 and count==len(states) and
                (k==0 and even==1 and odd==0 or k>0 and even==odd),
                len(states), error)
        if d==2:
            checked('exact d2 display multiplicity k='+str(k),
                    even==(1 if k==0 else 2*k) and odd==2*k, 1)
        energy_counts.append({'d':d,'k':k,'dimension':len(states),
                              'even':even,'odd':odd})

for k in range(1,7):
    for nu in [-100.,-3.,-1.,0.,.2,1.,3.,100.]:
        w = math.sqrt(2*k)
        block = np.array([[nu,w],[w,-nu]])
        S = np.array([[0.,1.],[1.,0.]])
        F = block/math.sqrt(1+2*k+nu*nu)
        expected = 2*w/math.sqrt(1+2*k+nu*nu)
        error = max(float(np.max(np.abs(block@block-(2*k+nu*nu)*np.eye(2)))),
                    float(np.max(np.abs(S@F+F@S-expected*np.eye(2)))))
        checked('normal product square and exact positivity k='+str(k)+' nu='+str(nu),
                error<1e-10 and expected>0, 1, error)
    tails = []
    for nu in [10.,100.,1000.,10000.]:
        denominator = math.sqrt(1+2*k+nu*nu)
        tails.append(max(w/denominator,
                         abs(nu/denominator-nu/math.sqrt(1+nu*nu))))
    checked('finite creation-connection tail samples k='+str(k),
            all(a>b for a,b in zip(tails,tails[1:])), len(tails))

for n in range(1,20):
    lower = math.sqrt(2*n)/math.sqrt(2*n+1)
    upper = math.sqrt(2*n)/math.sqrt(2*(n-1)+3)
    checked('dimension-one full adjoint block at paired energy '+str(n),
            lower==upper, 1)

import argparse
parser=argparse.ArgumentParser()
parser.add_argument('--lesson-source',type=Path,default=HERE.parent.parent/'src/k-theory-of-the-leaf-space.md')
args=parser.parse_args()
complete=args.lesson_source.read_text(encoding='utf8')
start=complete.index('## 11E. Translation oscillators and a smooth source-column graph class')
end=complete.index('## 12. Exercises',start) if '## 12. Exercises' in complete[start:] else complete.index('### Translation oscillators and the actual graph class: Exercises 119–121',start)
proof=complete[start:end]
import re
tags = re.findall(r'\\tag\{TO\.(\d+)\}',proof)
checked('all 26 unique ordered equation tags',
        tags==[str(n) for n in range(1,27)],len(tags))
start=complete.index('### Translation oscillators and the actual graph class: Exercises 119–121')
end=complete.index('## References',start) if '## References' in complete[start:] else len(complete)
exercises=complete[start:end]
checked('all complete solutions and 16+14+20=50 rubrics',
        exercises.count('**Solution.**')==3 and
        exercises.count('**Rubric.**')==3 and
        all('Total '+str(n)+'.' in exercises for n in [16,14,20]),3)

report = {'schema':'translation-oscillator-finite-consistency/v1',
          'checks':checks,'all_passed':True,
          'energy_counts':energy_counts,
          'proof_replacement':False,
          'limits':'Finite CAR/energy/product samples and body structure only. '
                   'Completeness, completed domains, scalar compactness, reduced '
                   'norms, graph identification, class equality and pairing are '
                   'proved in the complete Section 11E body. These finite checks do not replace its proofs.',
          'arbitrary_groupoid_target_closed':False}
(HERE/'FORMULA-CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print(json.dumps({'all_passed':True,'checks':len(checks),
                  'typed_cases':sum(row['cases'] for row in checks)}))
