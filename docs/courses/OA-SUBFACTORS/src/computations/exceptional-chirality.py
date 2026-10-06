"""Exact E6/E8 ordered-trace certificates. Standard library only.

Original authored code: CC0. GPT-6.1 Sol (OpenAI), Ultra, September 2026.
See the complete intrinsic-projection and row-generation proof in lesson39.
"""
from pathlib import Path
from collections import defaultdict
import hashlib, importlib.util, json, sys

sys.dont_write_bytecode = True
source = Path(__file__).with_name("exceptional-flatness.py")
spec = importlib.util.spec_from_file_location("exceptional",source)
lib = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lib)
certificate = json.loads(source.with_name("exceptional-flatness-certificate.json").read_text(encoding="utf-8"))

def run(data):
    K,z = lib.field(data["cyclotomic_modulus"],data["field_order"])
    zero,one = K(),K(1)
    degree = len(data["cyclotomic_modulus"])-1
    graph = {int(j):ns for j,ns in data["graph_adjacency"].items()}
    def decode(row):
        return K.vector([lib.F(row.get(str(j),"0")) for j in range(degree)])
    mu = {int(j):decode(w) for j,w in data["perron_weights"].items()}
    b,k = data["branch"],data["k"]
    eps = z**(data["h"]-1)
    ieps = 1/eps
    delta = -(eps**2+ieps**2)
    q = [zero,one]
    for j in range(k+1):
        q.append(delta*q[-1]-q[-2])
    def paths(length,start):
        out = [(start,)]
        for j in range(length):
            out = [p+(a,) for p in out for a in graph[p[-1]]]
        return out
    prefixes = [p for p in paths(k+1,0) if p[-1] == b]
    n = len(prefixes)
    lookup = {p:i for i,p in enumerate(prefixes)}
    def metric(p):
        value = one
        for a in p[1:-1]:
            value *= mu[a]
        return value
    g = [metric(p) for p in prefixes]
    def mul(A,B):
        return [[sum((A[i][j]*B[j][l] for j in range(n)),zero) for l in range(n)] for i in range(n)]
    I = [[K(i==j) for j in range(n)] for i in range(n)]
    generators = {}
    for pos in range(1,k+1):
        U = [[zero for j in range(n)] for i in range(n)]
        for j,p in enumerate(prefixes):
            a,c,d = p[pos-1:pos+2]
            if a == d:
                for v in graph[a]:
                    r = p[:pos]+(v,)+p[pos+1:]
                    U[lookup[r]][j] += mu[c]/mu[a]
        generators[pos] = U
    F = I
    for j in range(1,k):
        removed = mul(mul(F,generators[j+1]),F)
        F = [[F[r][s]-q[j]/q[j+1]*removed[r][s] for s in range(n)] for r in range(n)]
    assert mul(F,F) == F
    assert sum((F[i][i] for i in range(n)),zero) == 2
    # Independent columns of the positive weighted projection have a nonsingular principal minor.
    pair = next((i,j) for i in range(n) for j in range(i+1,n)
                if F[i][i]*F[j][j]-F[i][j]*F[j][i])
    print(json.dumps({"graph":data["graph"],"branch_block":n,"suffix_Wenzl_rank":2,"columns":pair}),flush=True)
    swaps = [pos for h in range(k-1) for pos in range(k+1+h,1+h,-1)]
    word = ["v"]*(k+1)+["h"]*(k-1)
    for pos in swaps:
        assert word[pos-1:pos+1] == ["v","h"]
        word[pos-1:pos+1] = ["h","v"]
    assert word == ["v"]+["h"]*(k-1)+["v"]*k
    def swap(vector,pos):
        out = defaultdict(K)
        for p,value in vector.items():
            out[p] += eps*value
            a,c,d = p[pos-1:pos+2]
            if a == d:
                for v in graph[a]:
                    r = p[:pos]+(v,)+p[pos+1:]
                    out[r] += ieps*mu[c]/mu[a]*value
        return {p:value for p,value in out.items() if value}
    xi = tuple(data["selected_prefix"])
    def color(p):
        return 0 if p[2] == 0 else (1 if p[:k+1] == xi else 2)
    equations = {}
    suffixes = paths(k-1,b)
    for number,suffix in enumerate(suffixes):
        H = []
        for col in pair:
            vector = {p+suffix[1:]:F[i][col] for i,p in enumerate(prefixes) if F[i][col]}
            for pos in swaps:
                vector = swap(vector,pos)
            H.append(vector)
        for a in range(2):
            for c in range(2):
                denominator = metric(prefixes[pair[c]]+suffix[1:])
                slot = 2*a+c
                for r,vr in H[a].items():
                    for s,vs in H[c].items():
                        if color(r) != color(s):
                            row = equations.setdefault((r,s),[zero]*4)
                            row[slot] += vr*vs.conj()/denominator
    print(json.dumps({"graph":data["graph"],"suffixes":len(suffixes),"off_partition_equations":len(equations)}),flush=True)
    pivots = {}
    for original in equations.values():
        row = list(original)
        for j,v in sorted(pivots.items()):
            if row[j]:
                coefficient = row[j]
                row = [x-coefficient*y for x,y in zip(row,v)]
        j = next((j for j,v in enumerate(row) if v),None)
        if j is not None:
            coefficient = row[j]
            row = [x/coefficient for x in row]
            for old,v in list(pivots.items()):
                if v[j]:
                    coefficient = v[j]
                    pivots[old] = [x-coefficient*y for x,y in zip(v,row)]
            pivots[j] = row
    assert len(pivots) == 3, {"graph":data["graph"],"rank":len(pivots)}
    free = next(j for j in range(4) if j not in pivots)
    coefficients = [zero]*4
    coefficients[free] = one
    for j,row in pivots.items():
        coefficients[j] = -row[free]
    assert all(sum((v*c for v,c in zip(row,coefficients)),zero) == 0 for row in equations.values())
    sigma = [[sum((coefficients[2*a+c]*F[r][pair[a]]*F[pair[c]][s]
                  for a in range(2) for c in range(2)),zero) for s in range(n)] for r in range(n)]
    trace = sum((sigma[i][i] for i in range(n)),zero)
    assert trace
    sigma = [[v/trace for v in row] for row in sigma]
    assert mul(sigma,sigma) == sigma
    assert all(sigma[i][j] == g[j]/g[i]*sigma[j][i].conj() for i in range(n) for j in range(n))
    for pos in range(2,k+1):
        assert all(not v for row in mul(generators[pos],sigma) for v in row)
        assert all(not v for row in mul(sigma,generators[pos]) for v in row)
    short_path = xi+(b,)
    selected = lookup[short_path]
    bridge = I
    for pos in range(1,k+1):
        bridge = mul(bridge,generators[pos])
    invariant = mul(sigma,bridge)[selected][selected]*mu[b]/delta**(k+1)
    assert invariant != invariant.conj(), "Ordered trace must differ from its conjugate"
    def encode(value):
        return {str(j):str(v) for j,v in enumerate(value.a) if v}
    return {"graph":data["graph"],"k":k,"branch_endpoint":b,"prefix_paths":prefixes,
            "suffix_Wenzl_rank":2,"linear_constraint_rank":3,
            "equations":len(equations),"all_equations_checked":True,"projection_trace":1,
            "sigma":{f"{i},{j}":encode(v) for i,row in enumerate(sigma) for j,v in enumerate(row) if v},
            "ordered_bridge":"U1 U2 ... Uk","inclusion_trace":encode(invariant),
            "trace_minus_conjugate":encode(invariant-invariant.conj()),
            "nonreal":True}


def cyclotomic(n):
    """Integer coefficients from x^n-1 = product_{d|n} Phi_d."""
    polynomial = [-1]+[0]*(n-1)+[1]
    for d in range(1,n):
        if n % d:
            continue
        divisor = cyclotomic(d)
        quotient = [0]*(len(polynomial)-len(divisor)+1)
        remainder = list(polynomial)
        for j in range(len(quotient)-1,-1,-1):
            coefficient = remainder[j+len(divisor)-1]
            quotient[j] = coefficient
            for i,value in enumerate(divisor):
                remainder[j+i] -= coefficient*value
        assert not any(remainder)
        polynomial = quotient
    return polynomial

def main():
    assert hashlib.sha256(source.read_bytes()).hexdigest().upper() == certificate["checker_sha256"]
    for data in certificate["graphs"]:
        assert cyclotomic(data["field_order"]) == data["cyclotomic_modulus"]
    results = [run(data) for data in certificate["graphs"]]
    expected = {
        "E6":{"2":"-11","6":"11","10":"3","14":"-8"},
        "E8":{"2":"-76","6":"-15","10":"27","14":"42","18":"49","22":"22","26":"-12","30":"-77"}
    }
    for row in results:
        assert row["trace_minus_conjugate"] == expected[row["graph"]]
    receipt = {
        "schema":"exceptional-ordered-trace-exact-certificate/v1",
        "arithmetic":"Rational polynomial reduction modulo the minimal cyclotomic polynomials",
        "row_generators":"Mixed first cup and mixed short-tip projection, together with N",
        "constraint_partition":"Output p2=0; output prefix xi; all other outputs",
        "basis":"Positive diagonal path metric; four endomorphisms of the suffix Wenzl range",
        "checker_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest().upper(),
        "field_library_sha256":hashlib.sha256(source.read_bytes()).hexdigest().upper(),
        "flatness_certificate_sha256":hashlib.sha256(source.with_name("exceptional-flatness-certificate.json").read_bytes()).hexdigest().upper(),
        "results":results
    }
    target = Path(__file__).with_name("exceptional-chirality-certificate.json")
    target.write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"graphs":len(results),"nonreal_ordered_traces":"exactly passed","certificate":target.name}),flush=True)

if __name__ == "__main__":
    main()
