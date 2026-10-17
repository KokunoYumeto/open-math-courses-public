"""Finite algebra/support checks; the full analytic proof is in the lesson."""
from pathlib import Path
import json,hashlib
import sympy as s
Q=s.Rational;checks=[]
def eq(name,a,b):
 assert s.simplify(a-b)==0,name
 checks.append({'name':name,'passed':True,'kind':'exact identity'})
def pos(name,x):
 assert s.simplify(x).is_positive,name
 checks.append({'name':name,'passed':True,'kind':'exact positive margin','value':str(x)})
eq('minimum ratio',1/Q(4,3),Q(3,4))
eq('left maximum output',Q(4,3)*Q(3,4),1)
eq('right minimum output',4-Q(4,3)*Q(3,4),3)
pos('separate collar output gap',3-1)
pos('left deep cutoff and interior output gap',Q(1,4)-Q(1,8))
pos('right deep cutoff and interior output gap',Q(31,8)-Q(15,4))
eq('positive input margin for output x at least1/16',Q(3,4)*Q(1,16),Q(3,64))
t,xi,kappa=s.symbols('t xi kappa',real=True)
eq('right inward covector sign',(4-t)*(-xi),-(4-t)*xi)
eq('right endpoint support change',4-Q(31,8),Q(1,8))
eq('symmetric interior buffer',4-Q(15,4),Q(1,4))
N=s.symbols('N',integer=True,positive=True);z=s.Function('z')(t);u=z*s.exp(s.I*N*t)
eq('second derivative plane wave',-s.diff(u,t,2),s.exp(s.I*N*t)*(N*N*z-2*s.I*N*s.diff(z,t)-s.diff(z,t,2)))
p=Path(__file__).with_name('global-scalar-tests-on-one-dimensional-manifolds.md')
r={'schema':'AN04-one-dimensional-scalar-assembly-finite-checks/v1','passed':True,'exact_checks':len(checks),
 'checks':checks,'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),
 'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'analytic_proof_established_by_these_checks':False,'numerical_checks':0}
Path(__file__).with_name('model-check.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n','utf-8')
print(json.dumps({'passed':True,'exact_checks':len(checks)}))
