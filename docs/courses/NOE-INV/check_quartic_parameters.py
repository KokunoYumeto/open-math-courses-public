"""Construct the rational parameter equations on singular quartic normal forms."""
from pathlib import Path
import argparse,json,hashlib,time
import sympy as s
from quartic_algebra import from_expr,parameters

parser=argparse.ArgumentParser()
parser.add_argument('--case',required=True,choices=['1.1','1.2','2.1','2.2','2.3'])
args=parser.parse_args()
x,y,z=s.symbols('x y z')
A,B,C,D,E,L,M,N=s.symbols('A B C D E L M N')
models={'1.1':x*x*z*z+(L*x*y*y+M*x*x*y+N*x**3)*z+A*y**4+B*x*y**3+C*x*x*y*y+D*x**3*y+E*x**4,
        '1.2':x*x*z*z+y**3*z+A*y**4+B*x*y**3+C*x*x*y*y+D*x**3*y+E*x**4,
        '2.1':x*y*z*z+(y**3+x**3)*z+A*y**4+B*x*y**3-s.Rational(9,2)*x*x*y*y+D*x**3*y+E*x**4,
        '2.2':x*y*z*z+x**3*z+A*y**4+B*x*y**3+C*x*x*y*y+D*x**3*y+E*x**4,
        '2.3':x*y*z*z+A*y**4+B*x*y**3+C*x*x*y*y+D*x**3*y+E*x**4}
print('Computing case'+args.case,flush=True)
start=time.monotonic()
values=parameters(from_expr(models[args.case],(x,y,z)))
directory=Path(__file__).resolve().parent/'quartic-certificates'
directory.mkdir(exist_ok=True)
data={'case':args.case,'normal_form':str(models[args.case]),'definitions':'quartic_algebra.py','values':{name:str(s.factor(p)) for name,p in values.items()},'elapsed_seconds':time.monotonic()-start}
(directory/('case-'+args.case+'.json')).write_text(json.dumps(data,indent=2)+'\n',encoding='utf8',newline='\n')
for name,value in values.items():print(name,s.factor(value),flush=True)
print('Elapsed',data['elapsed_seconds'],flush=True)
