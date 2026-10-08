"""Supplementary exact geometry, finite convolution and mollifier probes."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import hashlib,json
import mpmath as mp
OWN=Path(__file__).resolve().parent;mp.mp.dps=65
counts={};errors=[]
def exact(name,condition):
    assert condition,name
    counts[name]=counts.get(name,0)+1
def close(name,a,b,tol=mp.mpf("1e-48")):
    error=abs(a-b);assert error<tol,(name,str(error))
    counts[name]=counts.get(name,0)+1;errors.append(error)
def convolution(a,b):
    result={}
    for x,c in a.items():
        for y,d in b.items():result[x+y]=result.get(x+y,0)+c*d
    return {x:c for x,c in result.items()if c!=0}
def interval_margin(support,interval):
    return min(min(support)-interval[0],interval[1]-max(support))
for j in range(1,101):
    L,U=Q(-5),Q(6);a,b=-Q(j,j+6),Q(2*j+1,j+6)
    Y=(L+b,U+a);alpha,beta=Q(1,j+2),Q(2,j+3)
    T=(Y[0]+alpha,Y[1]-beta)
    W=convolution({-a:1,-b:-2},{T[0]:1,T[1]:1j})
    exact("finite_convolution_extreme_hull",min(W)==T[0]-b and max(W)==T[1]-a)
    exact("exact_interval_distance_identity",interval_margin(T,Y)==interval_margin(W,(L,U)))
    exact("positive_compact_margins",interval_margin(T,Y)>0)
    K1=(min(W)-Q(1,10),max(W)+Q(1,10))
    K2=(K1[0]+b,K1[1]+a)
    exact("convex_compact_confinement_receiver",K2[0]<=T[0]<=T[1]<=K2[1])
image=convolution({Q(0):1,Q(-1):-1},{Q(0):1,Q(1):1})
exact("cancelled_middle_atom",image=={Q(-1):-1,Q(1):1})
complex_image=convolution({Q(0):1,Q(-2):1j},{Q(0):1,Q(2):1j})
exact("bilinear_complex_reflection_cancellation",complex_image=={Q(-2):1j,Q(2):1j})
for j in range(1,81):
    e=Q(1,j+4)
    T=(-e,e,1-e,1+e);W=(-1-e,-1+e,1-e,1+e)
    exact("regularized_distance_identity",interval_margin(T,(Q(-1),Q(3)))==interval_margin(W,(Q(-2),Q(3)))==1-e)
    exact("disjoint_regularized_support_copies",e<1-e and -1+e<1-e)
for ix in range(13):
    for iy in range(11):
        x,y=-Q(2)+Q(ix,2),Q(iy,2)
        margin_T=min(x+3,5-x,y+1,6-y)
        W=[(x,y),(x-1,y),(x,y-2)]
        margin_W=min(min(p[0]for p in W)+4,5-max(p[0]for p in W),
                     min(p[1]for p in W)+3,6-max(p[1]for p in W))
        exact("rectangle_point_support_distance",margin_T==margin_W>0)
for j in range(1,51):
    t=Q(2,3)+Q(3*j,51);image_t=t-Q(2,3)
    exact("selected_component_distance",min(t-Q(2,3),Q(11,3)-t)==min(image_t,3-image_t)>0)
exact("trimmed_component_failure",Q(1)<Q(4,3))
for j in range(1,101):
    shift=Q(1,2)-Q(1,j+3)
    T=(Q(-1,4)+shift,Q(1,2)+shift)
    exact("translation_stays_in_equation_domain",Q(-1)<T[0]<=T[1]<1)
    exact("translation_images_in_one_compact",Q(-1,4)<=T[0] and T[1]<=1)
def bump(t):return mp.exp(-1/(1-t*t))if abs(t)<1 else mp.mpf(0)
pieces=[-1,-mp.mpf(1)/2,0,mp.mpf(1)/2,1]
mass=mp.quad(bump,pieces)
rho=lambda t:bump(t)/mass
m2=mp.quad(lambda t:t*t*rho(t),pieces)
for e in [mp.mpf(1)/16,mp.mpf(1)/8,mp.mpf(1)/4]:
    for z in [mp.mpf(0),mp.mpf(3)/4,mp.mpf(7)/3,mp.mpf(1)/2+mp.j/3]:
        factor=mp.quad(lambda t:rho(t)*mp.exp(-mp.j*e*t*z),pieces)
        v_transform=sum(mp.quad(lambda t:rho(t)*mp.exp(-mp.j*(c+e*t)*z),pieces)for c in [0,1])
        w_transform=mp.quad(lambda t:rho(t)*(mp.exp(-mp.j*(1+e*t)*z)-mp.exp(-mp.j*(-1+e*t)*z)),pieces)
        close("physical_mollified_transform_factor",v_transform,(1+mp.exp(-mp.j*z))*factor)
        close("physical_cancelled_convolution_transform",w_transform,(1-mp.exp(mp.j*z))*v_transform)
    for degree,expected in [(0,0),(1,2),(2,0),(3,2+6*e*e*m2)]:
        physical=mp.quad(lambda t:rho(t)*((1+e*t)**degree-(-1+e*t)**degree),pieces)
        close("physical_regularized_image_moment",physical,expected)
record={"schema":"AN02-original-distance-example-probes225/v1","observed_at_utc":datetime.now(timezone.utc).isoformat(),
    "status":"PASS","decimal_precision":mp.mp.dps,"probe_count":sum(counts.values()),"counts":counts,
    "maximum_identity_error":str(max(errors)),"symmetric_mollifier_second_moment":str(m2),
    "proof_status":"Supplementary exact-rational support geometry and physical mollifier transforms/moments;not a proof of the general criterion.",
    "independent_review":False,"source_code_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest().upper()}
(OWN/"supplementary-example-probes225.json").write_text(json.dumps(record,indent=2)+"\n",encoding="utf-8")
print(json.dumps(record))
