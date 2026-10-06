"""Finite exact consistency checks; these do not prove infinite PT assertions."""
from pathlib import Path
from fractions import Fraction
import hashlib
import json
import numpy as np

OUT=Path(__file__).resolve().parent
letters="aAbB"
inv={"a":"A","A":"a","b":"B","B":"b"}

def mul(a,b):
    out=list(a)
    for s in b:
        if out and out[-1]==inv[s]:
            out.pop()
        else:
            out.append(s)
    return "".join(out)

def words(r):
    result=[""]
    last=[""]
    for _ in range(r):
        last=[w+s for w in last for s in letters if not w or s!=inv[w[-1]]]
        result.extend(last)
    return result

def edge(w):
    return None if not w else frozenset([w,w[:-1]])

def gedge(h,e):
    return None if e is None else frozenset(mul(h,v) for v in e)

ws=words(5)
hs=words(3)
checked=0
exceptional=0
for h in hs:
    segment={h[:i] for i in range(len(h)+1)}
    actual_exceptions=set()
    for v in ws:
        hv=mul(h,v)
        e1=edge(hv)
        e2=gedge(h,edge(v))
        if hv not in segment:
            assert e1==e2,(h,v,hv,e1,e2)
            assert abs(len(hv)-len(v))<=len(h)
        else:
            actual_exceptions.add(v)
            assert len(v)<=len(h) and len(hv)<=len(h)
            exceptional+=1
        checked+=1
    assert len(actual_exceptions)==len(h)+1

# Exact rational coefficients square to 1/2; the actual J coefficient is 1/sqrt2.
coset_cases=0
for h in hs:
    for g in words(3):
        for eps in [0,1]:
            support={(g,0),(g,1)}
            translated={(mul(h,v),c^eps) for v,c in support}
            expected={(mul(h,g),0),(mul(h,g),1)}
            assert translated==expected
            assert sum(Fraction(1,2) for _ in expected)==1
            coset_cases+=1

# Complete left regular C4 matrices on all sixteen ordered monomials.
r=4
dim=2**r
physical=[]
for j in range(r):
    a=np.zeros((dim,dim),dtype=np.int64)
    for mask in range(dim):
        sign=(-1)**((mask&((1<<j)-1)).bit_count())
        a[mask^(1<<j),mask]=-sign  # k4=6 gives negative physical generators
    physical.append(a)
I=np.eye(dim,dtype=np.int64)
grading=np.diag([(-1)**mask.bit_count() for mask in range(dim)])
clifford_checks=0
for j,a in enumerate(physical):
    assert np.array_equal(a@a,I)
    assert np.array_equal(a.T,a)
    assert np.array_equal(grading@a,-a@grading)
    clifford_checks+=3
    for b in physical[j+1:]:
        assert np.array_equal(a@b,-b@a)
        clifford_checks+=1
assert sum(grading.diagonal()==1)==8 and sum(grading.diagonal()==-1)==8
assert (-1)**(r*(r-1)//2+1)==-1

block_checks=0
for nu in range(-8,9):
    for depth in range(1,8):
        a=np.array([[nu,depth],[depth,-nu]],dtype=np.int64)
        assert np.array_equal(a@a,(nu*nu+depth*depth)*np.eye(2,dtype=np.int64))
        block_checks+=1

countable_weight_checks=0
window_counts=[]
for radius in range(7):
    gs=words(radius)
    leaves=[(g,j) for g in gs for j in range(1,radius+1) if len(g)+j<=radius]
    expected=len(gs)+sum(len(words(radius-j)) for j in range(1,radius+1))
    assert len(gs)+len(leaves)==expected
    window_counts.append(expected)
for h in hs:
    for g in words(4):
        for j in range(1,10):
            assert abs((len(mul(h,g))+j)-(len(g)+j))<=len(h)
            countable_weight_checks+=1

report={"rooted_tree_columns_checked":checked,"segment_inputs_checked":exceptional,
        "finite_C2_average_covariance_cases":coset_cases,
        "full_C4_matrix_identities_checked":clifford_checks,
        "full_C4_even_and_odd_dimensions":[8,8],
        "exact_product_block_squares_checked":block_checks,
        "countable_tree_weight_difference_cases":countable_weight_checks,
        "countable_tree_window_counts_R0_to_R6":window_counts,
        "failures":[],
        "scope":"Finite formula consistency only. Infinite domains, scalar compact tails, reduced descent and Bott normalization are proved in Section 11D, not certified by these enumerations."}
(OUT/"FORMULA-CHECKS.json").write_text(json.dumps(report,indent=2)+"\n",encoding="utf-8")
print(json.dumps(report))
