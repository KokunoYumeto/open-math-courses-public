"""Exact all-original first fractional and contracted comparison bounds. CC0.

Requires the accompanying universal nested-radius and field proofs.
No all-depth zero-production conclusion is inferred here.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import json
from integer_comparison_bounds import rows,constants,minimum_S,lam

def exp_lower(x):return sum(x**j/factorial(j) for j in range(11))
def exp_upper(x):return exp_lower(x)+x**11/(factorial(11)*(1-x/12))

def bound(row,r,uniform=False):
 name,c0,c1,c3,c4,q,c2,y,omega,C,cs=constants(row)
 c=cs[2] if uniform else cs[0 if r==2 else 1 if r<=7 else 2]
 eta=1-c/(r+1);H=eta**(r+1)
 br=F(7200,29)*14**(r-2);eps=(3+F(14,r+1))/(7*br)
 g12=F(0) if name in ('I.2','III.2') else (1+F(5,r+1))/(546*br)
 Cr=F(1) if uniform else F(103*r+4,103*(r+1))+F(17*(r-1),24*(r+1)**2)
 g9=F(107,103) if uniform or r>=8 or name in ('I.2','III.2') else max(F(107,103),1+F(1,3*(r+1)))
 Sm=minimum_S(name,c3,q,r);ell=F(347,500) if q==2 else F(1099,1000)
 Hupper=1/exp_lower(c) if uniform else H
 assert H**(-1)+1/Sm<q
 A=c1*(g12+eps)+(c1*eps/2+lam/c4+Cr/(c3*y)+F(117,232*c2))/(C-1)
 Dmin=F(6) if uniform else F(5)
 arith=A+c1*(F(1,300)+1/(273*999*br))+g9*Hupper/(c3*y)+lam/c4+lam*ell/(Dmin*c4)*(1+F(1,q-1))+(H**(-1)+1/Sm)/c2+lam*omega/(c4*q**r)
 if uniform:
  floorloss=F(q*(r+1)*(2*r+1),q**r*Sm)
  nested=2*c*q/exp_upper(c)*sum(F(1,q**j) for j in range(4))-floorloss
 else:
  floorloss=F(q*(r+1),q**r*Sm)*((1-H)+2*sum(eta**j-H for j in range(1,r+1)))
  nested=2*c*q*sum((q*eta)**j for j in range(r+1))/q**r-floorloss
 inputprecision=c1*q-F(c1,7*(r+1)*br*q**r)-((1-H)+F(1,6*(r+1)))/(q**r*c3*y)
 contracted=A+c1*(F(1,300)+1/(273*999*br))+g9*(Hupper if uniform else eta*H)/(c3*y)+lam/c4+lam*ell/(Dmin*c4)*(1+F(1,q-1))+(H**(-1)+1/Sm)/c2+lam*omega/c4
 contracted_gain=2*c*q*(q-1)
 contracted_input=c1*q**(r+1)-F(c1,7*(r+1)*br)-F(3*c,(r+1)*c3*y)
 return arith,nested,inputprecision,contracted,contracted_gain,contracted_input

def records():
 out=[]
 for row in rows:
  for r in range(2,8):
   ar,nest,inp,ca,cg,ci=bound(row,r)
   out.append({'case':row[0],'rank':r,'analytic_nested_gap':str(nest-ar),'input_gap':str(inp-ar),'nested_gap_decimal':float(nest-ar),'input_gap_decimal':float(inp-ar),'contracted_gap':str(cg-ca),'contracted_input_gap':str(ci-ca),'contracted_gap_decimal':float(cg-ca),'contracted_input_gap_decimal':float(ci-ca)})
  ar,nest,inp,ca,cg,ci=bound(row,8,True)
  out.append({'case':row[0],'rank':'all_r_ge_8','analytic_nested_gap':str(nest-ar),'input_gap':str(inp-ar),'nested_gap_decimal':float(nest-ar),'input_gap_decimal':float(inp-ar),'contracted_gap':str(cg-ca),'contracted_input_gap':str(ci-ca),'contracted_gap_decimal':float(cg-ca),'contracted_input_gap_decimal':float(ci-ca)})
 assert all(F(v['analytic_nested_gap'])>F(1,50) and F(v['input_gap'])>1 and F(v['contracted_gap'])>F(1,50) and F(v['contracted_input_gap'])>1 for v in out)
 return out

if __name__=='__main__':
 import argparse
 parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path);args=parser.parse_args()
 out=records();data={'state':'passed','rows':out,'scope':'48finite original rank2–7 comparisons and8 analytically uniform rank>=8 rows, each with two first-fractional and two first-contraction strict comparisons. Universal proofs are in Section41; later stages remain separate.'}
 if args.output:args.output.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'state':data['state'],'rows':len(out),'minimum_nested_gap':min(x['nested_gap_decimal'] for x in out),'minimum_input_gap':min(x['input_gap_decimal'] for x in out),'minimum_contracted_gap':min(x['contracted_gap_decimal'] for x in out),'minimum_contracted_input_gap':min(x['contracted_input_gap_decimal'] for x in out)}))
