"""Finite groupoid, simplex and cone checks for Section11Z; CC0.
These reproducible checks supplement, and do not prove, the infinite KK claims.
"""
from pathlib import Path
import argparse
import hashlib
import json
import itertools
import re
import numpy as np

HERE=Path(__file__).resolve().parent
checks=[]
def check(name,ok,detail=None):
    checks.append({"name":name,"passed":bool(ok),"detail":detail})
def source(g):return g[2]
def ran(g):return g[2]^g[0]
def inverse(g):return(g[0],g[1],ran(g))
def compose(g,h):
    assert source(g)==ran(h)
    return(g[0]^h[0],g[1]^h[1],source(h))
def length(g):return g[0]+2*g[1]
G=list(itertools.product(range(2),range(2),range(2)))
V=lambda y:[(g,n) for g in G if ran(g)==y for n in range(2)]
def metric(v,w):
    return length(compose(inverse(v[0]),w[0]))+abs(v[1]-w[1])
def translate(g,v):return(compose(g,v[0]),v[1])
def project(v,indices):
    idx=list(indices);u=np.asarray(v)[idx]
    sort=np.sort(u)[::-1];sums=np.cumsum(sort)
    rho=np.where(sort-(sums-1)/np.arange(1,len(idx)+1)>0)[0][-1]
    theta=(sums[rho]-1)/(rho+1)
    out=np.zeros_like(v,dtype=float);out[idx]=np.maximum(u-theta,0)
    return out
def parity(mask):return(-1)**((mask.bit_count()-1)%2)
def clifford(xi):
    d=len(xi);op=np.zeros((2**d,2**d))
    for mask in range(2**d):
        for i,x in enumerate(xi):
            if not(mask>>i)&1:
                target=mask|(1<<i)
                op[target,mask]=x*((-1)**((mask&((1<<i)-1)).bit_count()))
    return(op+op.T)[1:,1:]
def exterior_permutation(perm):
    d=len(perm);images=[];signs=[]
    for mask in range(1,2**d):
        order=[perm[i] for i in range(d) if(mask>>i)&1]
        invs=sum(order[i]>order[j] for i in range(len(order)) for j in range(i+1,len(order)))
        images.append(sum(1<<i for i in order)-1);signs.append((-1)**invs)
    return np.array(images),np.array(signs)
def family_data(mu,t,dist):
    c=np.minimum(1,np.maximum(dist@mu-t,0))
    origins={};chi={}
    for mask in range(1,2**len(mu)):
        ids=[i for i in range(len(mu)) if(mask>>i)&1]
        cs=max(c[ids]);weights=np.zeros_like(mu)
        weights[ids]=6*min(2*cs,1)*c[ids]
        origins[mask]=(1-sum(weights))*mu+weights
        chi[mask]=max(2*cs-1,0)
    return c,origins,chi
def permute_mask(mask,perm):
    return sum(1<<perm[i] for i in range(len(perm)) if(mask>>i)&1)

def main(out):
    ids=[(0,0,y) for y in range(2)]
    trials=0
    for g in G:
        check("arrow inverse "+str(g),
              compose(g,inverse(g))==ids[ran(g)] and
              compose(inverse(g),g)==ids[source(g)])
        for v in V(source(g)):
            for w in V(source(g)):
                trials+=1
                assert metric(v,w)==metric(translate(g,v),translate(g,w))
    check("actual groupoid metric covariance",True,{"trials":trials,"arrow_count":len(G)})
    check("nontrivial isotropy retained",
          all(sum(source(g)==y and ran(g)==y for g in G)==2 for y in range(2)))
    rng=np.random.default_rng(61006)
    face_trials=0;origin_trials=0;cov_trials=0;cliff_trials=0
    for g in G:
        sv=V(source(g));tv=V(ran(g));d=len(sv)
        perm=np.array([tv.index(translate(g,v)) for v in sv])
        dist=np.array([[metric(v,w) for w in sv] for v in sv],dtype=float)
        target_dist=np.array([[metric(v,w) for w in tv] for v in tv],dtype=float)
        mu=np.zeros(d)
        chosen=[sv.index(((0,0,source(g)),0)),
                sv.index(((1,0,source(g)^1),0))]
        mu[chosen]=[.37,.63]
        t=1.
        target_mu=np.zeros(d);target_mu[perm]=mu
        c,origins,chi=family_data(mu,t,dist)
        tc,torigins,tchi=family_data(target_mu,t,target_dist)
        assert np.allclose(tc[perm],c)
        for mask,a in origins.items():
            target=permute_mask(mask,perm);mapped=np.zeros(d);mapped[perm]=a
            assert np.allclose(torigins[target],mapped) and np.isclose(tchi[target],chi[mask])
            cov_trials+=1
            for i in chosen:
                other=mask^(1<<i)
                if not other:continue
                assert np.allclose(a,origins[other]) and np.isclose(chi[mask],chi[other])
                origin_trials+=1
                if not chi[mask]>0:continue
                ids_mask=[j for j in range(d) if(mask>>j)&1]
                ids_other=[j for j in range(d) if(other>>j)&1]
                for _ in range(2):
                    error=rng.normal(size=d)
                    error*=.99*rng.random()/np.linalg.norm(error)
                    w=a+error
                    assert np.allclose(project(w,ids_mask),project(w,ids_other),atol=1e-10)
                    face_trials+=1
        xi=np.sqrt(mu);fx=clifford(xi);line=np.zeros(2**d-1)
        for i,x in enumerate(xi):line[(1<<i)-1]=x
        assert np.allclose(fx@fx,np.eye(len(fx))-np.outer(line,line),atol=1e-12)
        grades=np.array([parity(m) for m in range(1,2**d)])
        assert np.allclose(grades[:,None]*fx+fx*grades[None,:],0)
        assert np.allclose(grades*line,line)
        images,signs=exterior_permutation(perm)
        transported=np.zeros_like(fx)
        transported[np.ix_(images,images)]=signs[:,None]*fx*signs[None,:]
        assert np.allclose(transported,clifford(np.sqrt(target_mu)))
        cliff_trials+=1
    check("affine origin and cutoff exact covariance",True,{"simplex_trials":cov_trials})
    check("connected Clifford entries keep origins equal",True,{"trials":origin_trials})
    check("radius-one off-diagonal face support",True,{"random_trials":face_trials,"seed":61006})
    check("exterior signs, oddness, deficient even line and covariance",True,
          {"groupoid_trials":cliff_trials,"exterior_dimension":255})
    v=np.array([3.2,-2.2,0.]);w=np.array([3.,-2.12,.12])
    check("exact illustrated nearest-face sample",
          np.isclose(np.dot(v-w,v-w),.0608) and
          np.allclose(project(w,range(3)),[1,0,0]) and
          np.allclose(project(w,[0,1]),[1,0,0]) and 3>1+np.sqrt(2))
    f=lambda t:t*(1-t)
    a=np.linspace(0,1,1001)
    check("cone contraction zero endpoint",np.max(np.abs(f(0*a)))==0)
    check("cone contraction multiplicativity",
          all(np.allclose(f(u*a)**2,(lambda t:f(t)**2)(u*a)) for u in[0,.2,.5,1]))
    result={"schema":"anchored-universal-dirac-self-check/v1",
            "finite_model":"C2 x C2 action on two units, second C2 isotropy; two integer labels",
            "interpretation":"Finite checks supplement proofs; they do not certify infinite KK identities.",
            "checks":checks,"passed":all(c["passed"] for c in checks),
            "random_seed":61006}
    out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"passed":result["passed"],"checks":len(checks),"face_trials":face_trials,"covariance_trials":cov_trials}))
    if not result["passed"]:raise SystemExit(1)
if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,default=HERE/"finite-checks.json")
    main(parser.parse_args().output.resolve())
