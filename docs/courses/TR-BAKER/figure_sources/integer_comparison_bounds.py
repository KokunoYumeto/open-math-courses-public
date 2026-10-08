"""Exact rational all-case integer-extension margins. CC0.

TR-BAKER-10 Section40, Lemma10.125 and Theorem10.126.
Universal field/scalar/depth and rank arguments are proved in the lesson.
"""
from fractions import Fraction as F
from datetime import datetime,timezone
from pathlib import Path
import json
from math import factorial

tau=F(1,10**6);lam=F(189,188)
rows=[
 ('I.1','2.66','1.449','1.4647','20.74',2,F(7,4),F(3,2),F(2),F('2.66')*F(9,8),[F('.5377'),F('.55'),F('.56')]),
 ('I.2','1.9','1.4494','1.3852','20.8',2,F(7,4),F(3,2),F(2),F(57,20),[F('.538'),F('.551'),F('.56')]),
 ('II','2.74','1.4372','0.8412','19',2,F(7,4),F(5,2),F(3,2),F('2.74')*F(5,4),[F('.53'),F('.54'),F('.55')]),
 ('III.1','2.78','1.4341','2.992','18.7',2,F(7,4),F(3,4),F(1,2),F('2.78'),[F('.528'),F('.536'),F('.55')]),
 ('III.2','2.6','1.432','3.26','18.2757',2,F(7,4),F(3,4),F(1),F('2.6'),[F('.5267'),F('.534'),F('.55')]),
 ('IV.P1','3','1.4441','3.849','20',2,F(7,4),F(1,2),F(1,2),F(3),[F('.5345'),F('.543'),F('.56')]),
 ('IV.Plarge','3','1.4441','3.849','20',2,F(7,4),F(7,2),F(4,3),F(3),[F('.5345'),F('.543'),F('.56')]),
 ('V','2.5','2.5347','0.4757','3.765',3,F(13,9),F(2),F(3,2),F(10,3),[F('.753'),F('.78'),F('.827')]),
]

def constants(row):
 name,c0,c1,c3,c4,q,c2,y,gamma,c01,c5s=row
 return name,F(c0),F(c1),F(c3),F(c4),q,c2,y/(1+tau),gamma,c01,c5s

def minimum_S(name,c3,q,r):
 if name.startswith('I.'):
  return c3*q*(r+1)**2*(F(39,10)*r+F(36,5))/F(11,10)
 if name=='II':return c3*q*(r+1)**2*(F(39,10)*r+F(36,5))
 if name=='V':return c3*q*(r+1)**2*(F(39,10)*r+F(36,5))/F(347,500)
 return c3*q*(r+1)**2*(1 if name=='III.2' else 2)

def arithmetic(row,r,high=False):
 name,c0,c1,c3,c4,q,c2,y,gamma,c01,c5s=constants(row)
 br=F(7200,29)*14**(r-2)
 eps=(3+F(14,r+1))/(7*br)
 g12=F(0) if name in ('I.2','III.2') else (1+F(5,r+1))/(546*br)
 Cr=F(1) if high else F(103*r+4,103*(r+1))+F(17*(r-1),24*(r+1)**2)
 eta=F(1) if high else 1-c5s[0 if r==2 else 1]/(r+1)
 g9=F(107,103) if high or name in ('I.2','III.2') else max(F(107,103),1+F(1,3*(r+1)))
 init=c1*(g12+eps)+(c1*eps/2+lam/c4+Cr/(c3*y)+(1+F(1,116))/(2*c2))/(c01-1)
 remainder=c1*(F(1,300)+1/(273*999*br))
 out=init+remainder+g9*eta/(c3*y)+lam*(1+gamma)/c4
 c5=c5s[2] if high else c5s[0 if r==2 else 1]
 gain=c5*q*(2-1/minimum_S(name,c3,q,r))-F(q,c2)
 return gain-out,gain,out

def records():
 output=[]
 for row in rows:
  for r in range(2,8):
   gap,gain,out=arithmetic(row,r)
   assert gap>F(1,200),(row[0],r,float(gap))
   output.append({'case':row[0],'rank':r,'gap':str(gap),'lower_decimal':float(gap),'uniform_after_rank8':False})
  gap,gain,out=arithmetic(row,8,high=True)
  assert gap>F(1,200),(row[0],'all_r_ge_8',float(gap))
  output.append({'case':row[0],'rank':'all_r_ge_8','gap':str(gap),'lower_decimal':float(gap),'uniform_after_rank8':True})
 return output

def analytic_endpoints():
 """Finite exact arithmetic in the universal proofs, not rank sampling."""
 def exp_lower(x,n):return sum(x**j/factorial(j) for j in range(n+1))
 def exp_upper(x):return exp_lower(x,10)+x**11/(factorial(11)*(1-x/12))
 def log_interval(y,n):
  lower=2*sum(y**(2*j+1)/(2*j+1) for j in range(n))
  return lower,lower+2*y**(2*n+1)/((2*n+1)*(1-y*y))
 assert exp_upper(F(5267,10000))<F(17,10)
 assert exp_upper(F(753,1000))<F(213,100)
 lo,hi=log_interval(F(1,3),4);assert lo>F(693,1000) and hi<F(347,500)
 lo,hi=log_interval(F(1,2),5);assert lo>F(1098,1000) and hi<F(1099,1000)
 assert log_interval(F(47,197),2)[0]>F(12,25)
 assert log_interval(F(1173,3173),2)[0]>F(3,4)
 odd_endpoint=(F(693,1000)-F(14,61))*exp_lower(F(504,1525),5)
 assert odd_endpoint>F(129,200)
 V_endpoint=(F(1098,1000)-F(827,2173))*exp_lower(F(1173,1000)*F(827,2173),5)
 assert V_endpoint>F(1098,1000)
 odd_growth=2*F(5267,10000)/F(17,10)*F(129,200)-F(347,500)/F(7,4)
 V_growth=2*F(753,1000)/F(213,100)*F(1098,1000)-F(1099,1000)/F(13,9)
 assert odd_growth>F(1,400) and V_growth>F(1,100)
 assert 2*F(5267,10000)*F(61,75)*F(12,25)-F(347,500)/F(7,4)>F(7,500)
 assert 2*F(753,1000)*F(2173,3000)*F(3,4)-F(1099,1000)/F(13,9)>F(1,20)
 assert lam*F(347,500)/(5*F(18))<F(1,125)
 assert lam*F(1099,1000)/(5*F(15,4))<F(3,50)
 assert 2*F(7,500)-F(1,125)>F(1,125)
 assert F(3,20)-F(3,50)>F(3,100)
 assert 2*F(61,75)**3>F(43,40)
 assert all(x>F(5,4) for x in [3*F(749,1000)**3,3*F(161,200)**4,3*F(8173,9000)**9])
 odd_chord=3*lam*F(7,4)*F(347,500)/(18*4*F(6,83))
 V_chord=3*lam*F(13,9)*F(1099,1000)/(F(15,4)*9*F(2,9))
 assert odd_chord<F(3,4) and V_chord<F(2,3)
 assert exp_lower(F(15),6)>1000 and exp_lower(F(3),5)>F(214,13)
 assert all(minimum_S(row[0],F(row[3]),row[5],2)>58 for row in rows)
 assert 2*F(14,25)*(1-F(14,75))**2*(2-F(14,75))<F(27,20)
 assert 2*F(827,1000)*(1-F(827,3000))**2*(2-F(827,3000))<F(3,2)
 return {'state':'passed','odd_growth_margin':str(odd_growth),'V_growth_margin':str(V_growth),'odd_depth_chord_ratio':str(odd_chord),'V_depth_chord_ratio':str(V_chord),'logarithm_and_exponential_endpoints':'exact positive-series bounds passed','input_endpoint_bounds':'passed'}

if __name__=='__main__':
 import argparse
 parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path)
 args=parser.parse_args()
 rec=records();data={'utc':datetime.now(timezone.utc).isoformat(),'state':'passed','rows':rec,'analytic_endpoints':analytic_endpoints(),
  'scope':'48 exact rank2–7 rows and8 analytically uniform rank>=8 endpoint bounds. The enclosing formulas require their written universal field, scalar, depth, floor and monotonicity proofs; no conclusion inferred merely from a finite rank sample.'}
 if args.output:args.output.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({'state':data['state'],'rows':len(rec),'minimum':min(rec,key=lambda x:x['lower_decimal'])}))
