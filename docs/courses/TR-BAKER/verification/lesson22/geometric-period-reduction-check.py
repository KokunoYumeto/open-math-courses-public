"""Exact algebra and cohomology matrices in 22.116--117."""
from pathlib import Path
from datetime import datetime, timezone
import json
import sympy as s

x0,x1,a0,a1=s.symbols("x0 x1 a0 a1")
x=s.Matrix([x0,x1]); a=s.Matrix([[a0,a1]])
pairing=(a*x)[0]; projector=x*a/pairing
assert s.simplify(projector.trace()-1)==0
assert (projector*projector-projector).applyfunc(s.simplify)==s.zeros(2)
assert s.simplify(projector.det())==0

f1,f2,f3,t1,t2,t3=s.symbols("f1 f2 f3 t1 t2 t3")
equation=f1*t1+f2*t2+f3*t3-1
solved=s.solve(equation,t1)[0]
assert s.simplify(equation.subs(t1,solved))==0

t,z=s.symbols("t z")
intersections=s.solve([t-z*z,t-1],(t,z))
assert set(intersections)=={(1,-1),(1,1)}
jacobian=s.Matrix([t-z*z,t-1]).jacobian([t,z])
assert {jacobian.det().subs({t:T,z:Z}) for T,Z in intersections}=={-2,2}
restriction=s.Matrix([[1,-1],[1,-1]])
assert restriction.rank()==1
assert len(restriction.nullspace())==1
assert 2-restriction.rank()==1
d0=s.Matrix([[1,-1],[0,0]])
d1=s.Matrix([[0,1]])
assert d1*d0==s.zeros(1,2)
assert (2-d0.rank(),2-d1.rank()-d0.rank(),1-d1.rank())==(1,0,0)

result={
    "utc":datetime.now(timezone.utc).isoformat(),
    "state":"passed",
    "checks":{
        "incidence_complement_rank_one_trace_and_idempotence":3,
        "affine_torsor_local_solution":1,
        "two_reduced_transverse_intersection_points":2,
        "closed_cover_and_filtered_cochain_matrices":5
    },
    "total":11,
    "limits":"Exact identities for the affine construction and worked surface example; no computational claim to prove constructible base change or the filtration lemma."
}
Path(__file__).with_suffix(".json").write_text(
    json.dumps(result,indent=2)+"\n",encoding="utf-8")
print(json.dumps(result))
