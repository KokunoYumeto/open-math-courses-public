# Python 3 standard library only. Run with the certificate JSON as argv[1].
import json, math, sys
from pathlib import Path

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0: a.pop()
    return a

def add(a,b):
    return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
                 for i in range(max(len(a),len(b)))])

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return trim(c)

def rem(a,F):
    a=trim(a); n=len(F)-1
    assert F[-1]==1
    while len(a)>n:
        k=len(a)-1-n; c=a[-1]
        for j in range(n+1): a[j+k]-=c*F[j]
        a=trim(a)
    return a

def determinant(A):
    A=[row[:] for row in A]; n=len(A)
    if n==1: return A[0][0]
    sign=1; previous=1
    for k in range(n-1):
        pivot_row=next((i for i in range(k,n) if A[i][k]),None)
        if pivot_row is None: return 0
        if pivot_row!=k:
            A[k],A[pivot_row]=A[pivot_row],A[k]; sign=-sign
        pivot=A[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator=A[i][j]*pivot-A[i][k]*A[k][j]
                assert numerator%previous==0
                A[i][j]=numerator//previous
            A[i][k]=0
        previous=pivot
    return sign*A[-1][-1]

def matrix(F,g):
    n=len(F)-1; columns=[]
    for j in range(n):
        r=rem([0]*j+g,F)
        columns.append(r+[0]*(n-len(r)))
    return [[columns[j][i] for j in range(n)] for i in range(n)]

def norm(F,g): return determinant(matrix(F,g))

def polynomials(p):
    n=(p-1)//2; S=[[2],[0,1]]
    for j in range(2,n+1):
        S.append(add([0]+S[-1],[-x for x in S[-2]]))
    F=[1]
    for j in range(1,n+1): F=add(F,S[j])
    assert len(F)==n+1 and F[-1]==1
    return F,S

def isprime(q):
    return q>=2 and all(q%d for d in range(2,math.isqrt(q)+1))

def degree(p,q):
    return next(k for k in range(1,(p-1)//2+1)
                if pow(q,k,p) in (1,p-1))

def check(data):
    rows=[]
    for field in data['finite_certificate']['fields']:
        p=field['conductor']; n=(p-1)//2; F,S=polynomials(p)
        assert F==field['minimal_polynomial_coefficients_ascending']
        derivative=[j*F[j] for j in range(1,n+1)]
        D=(-1)**(n*(n-1)//2)*norm(F,derivative)
        assert D==p**(n-1)==field['discriminant']
        N=math.factorial(n)**2*D; denominator=n**(2*n)
        B=math.isqrt(N//denominator)
        assert B==field['minkowski_bound_floor']
        assert N==field['minkowski_squared_numerator']
        assert denominator==field['minkowski_squared_denominator']
        assert B*B*denominator<=N<(B+1)*(B+1)*denominator
        required=[]
        for q in range(2,B+1):
            if not isprime(q): continue
            f=1 if q==p else degree(p,q)
            if q**f<=B: required.append((q,f,q**f))
        assert required==[(r['rational_prime'],r['residue_degree'],r['prime_ideal_norm'])
                          for r in field['required_prime_orbits']]
        bynorm={r['absolute_norm']:r for r in field['principal_generators']}
        assert set(bynorm)=={q**f for q,f,_ in required}
        for q,f,qf in required:
            r=bynorm[qf]; a=r['basis_coefficients']; assert len(a)==n
            g=[a[0]]
            for j in range(1,n): g=add(g,[a[j]*x for x in S[j]])
            assert g==r['polynomial_coefficients_ascending']
            A=matrix(F,g); exact=determinant(A)
            assert A==r['multiplication_matrix_columns_are_g_times_Tj']
            assert exact==r['signed_norm'] and abs(exact)==qf
            if q==p: assert norm(F,[2,-1])==p
        rows.append({'p':p,'bound_floor':B,'orbits':len(required),
                     'generators_verified':len(bynorm),'all_exact_checks_passed':True})
    assert [row['p'] for row in rows]==[3,5,7,11,13,17,19,23]
    return rows

if __name__=='__main__':
    result=check(json.loads(Path(sys.argv[1]).read_text(encoding='utf-8')))
    print(json.dumps(result,indent=2))
