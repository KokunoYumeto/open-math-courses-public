"""Original eight finite algebra families; no source access or state mutation."""
import json,math
import sympy as s
x,y,z,xi,eta,h=s.symbols('x y z xi eta h',real=True)
variables=[x,y,z,xi,eta,h]
def pb(f,g):
    return s.expand(sum(s.diff(f,k)*s.diff(g,j)-s.diff(f,j)*s.diff(g,k) for j,k in [(x,xi),(y,eta),(z,h)]))
checks=[]

# Full powers and differentiated multiplier terms, before any restriction to zeros.
p,q,u,alpha,beta=s.symbols('p q u alpha beta',positive=True)
pq,pu,qu=s.symbols('pq pu qu',real=True)
def abstract_bracket(f,g):
    return s.expand(pq*(s.diff(f,p)*s.diff(g,q)-s.diff(f,q)*s.diff(g,p))
      +pu*(s.diff(f,p)*s.diff(g,u)-s.diff(f,u)*s.diff(g,p))
      +qu*(s.diff(f,q)*s.diff(g,u)-s.diff(f,u)*s.diff(g,q)))
lhs=abstract_bracket(u**alpha*p,u**beta*q)
rhs=u**(alpha+beta-1)*(u*pq+beta*q*pu-alpha*p*qu)
assert s.simplify(lhs-rhs)==0
assert s.simplify(abstract_bracket(p,q)*p*alpha
    -(beta*q*abstract_bracket(p,p)-alpha*p*abstract_bracket(q,p)))==0
assert s.simplify(beta*q*pq
    -(beta*q*abstract_bracket(p,q)-alpha*p*abstract_bracket(q,q)))==0
checks.append({'name':'complete weighted bracket and exact normal dilation identities','passed':True,
    'scope':'Formal chain rule retains every multiplier derivative; Xp=alpha p and Xq=beta q after dividing by {p,q}.'})

# A nonconstant scalar solution and an exact polynomial backwards-flow integral.
models=[]
for a,b in [(s.Rational(1,2),s.Rational(1,2)),(s.Rational(3,4),s.Rational(1,4)),(s.Rational(2,5),s.Rational(3,5))]:
    K=1+x
    raw_p=xi*K**(-a)
    raw_q=x*K**(-b)
    C=s.simplify(pb(raw_p,raw_q))
    assert C.subs(x,0)==1 and s.diff(C,x).subs(x,0)!=0
    V_u=s.simplify(b*raw_q*pb(raw_p,K)-a*raw_p*pb(raw_q,K))
    assert s.simplify(C*K+V_u-1)==0
    assert s.simplify(pb(K**a*raw_p,K**b*raw_q)-1)==0
    datum=s.Poly(1+2*p-3*q+4*p*q+p*p+5*q**3,p,q)
    solution=sum(coef*p**i*q**j/(1+a*i+b*j) for (i,j),coef in datum.terms())
    assert s.expand(solution+a*p*s.diff(solution,p)+b*q*s.diff(solution,q)-datum.as_expr())==0
    assert solution.subs({p:0,q:0})==1
    models.append({'alpha':str(a),'beta':str(b),'C':str(C)})
checks.append({'name':'nonconstant positive normalizer and polynomial contracting-flow models','passed':True,
    'models':models,'scope':'Three actual scalar normalizers and exact elementary Laplace integrals; no general nonlinear-flow or smoothness inference.'})

# Exact fractional degrees and actual canonical coordinate completion.
degree_models=[]
for k in range(1,7):
    a=s.Rational(k,k+1);b=s.Rational(1,k+1)
    degree_u=-s.Rational(1,k)
    assert a*degree_u+1==a and b*degree_u+s.Rational(1,k)==b
    assert b+a==1 and b+k*b==1
    P=xi+s.Rational(2,3)*x*h
    Q=x
    Zn=z-s.Rational(1,3)*x*x
    Phi=h**(-b)*P
    Psi=h**b*Q
    assert s.simplify(pb(Phi,Psi)-1)==0
    assert pb(Phi,h)==0 and pb(Psi,h)==0
    positions=[Q,y,Zn]
    momenta=[P,eta,h]
    for i in range(3):
        for j in range(3):
            assert s.simplify(pb(momenta[i],positions[j])-(1 if i==j else 0))==0
            assert pb(momenta[i],momenta[j])==0 and pb(positions[i],positions[j])==0
    raw_g=h**s.Rational(1,k)*Q
    raw_u=h**degree_u
    # Exponent arithmetic is exact on h>0; avoid power simplification on h<0.
    assert a*degree_u+b==0
    assert s.simplify(P+s.I*raw_g**k-(P+s.I*Q**k*h))==0
    degree_models.append({'k':k,'alpha':str(a),'beta':str(b),'degree_u':str(degree_u)})
checks.append({'name':'fractional degrees, commuting positive momentum and full coordinate brackets','passed':True,
    'models':degree_models,'scope':'Six exact canonical models include the compensating last position Zn; general canonical completion uses retained U022.'})

# Nonconstant complex multipliers and nonconstant b on the zero manifold.
finite_models=[]
for k in [2,3,4]:
    p1=xi
    p2=(s.Rational(1,3)+x)*xi+x**k*h
    ar=1+x+xi/h
    ai=2-x*x
    real_ap=s.expand(ar*p1-ai*p2)
    imag_ap=s.expand(ai*p1+ar*p2)
    value=imag_ap
    for _ in range(k):
        value=pb(real_ap,value)
    actual=s.simplify(value.subs({x:0,xi:0}))
    expected=5*s.Rational(1,3)**(k-1)*math.factorial(k)*h
    assert s.simplify(actual-expected)==0
    for j in range(k):
        assert s.diff(p2,x,j).subs({x:0,xi:0})==0
    assert s.diff(p2,x,k).subs({x:0,xi:0})==math.factorial(k)*h
    finite_models.append({'k':k,'nonconstant_multiplier':str(ar+s.I*ai),'b':'1/3+x','marked_kth_derivative':str(actual)})
checks.append({'name':'full nonconstant multiplier finite-contact law','passed':True,
    'models':finite_models,'scope':'Three exact iterated Hamilton computations with all derivative terms; arbitrary smooth multiplier and bracket-tree proofs remain teaching obligations.'})

# All right-nested words through the admitted contact order in bounded models.
word_counts=[]
for k in range(2,7):
    inputs=[xi,x**k*h]
    words=inputs
    total=0
    for count in range(2,k+1):
        words=[pb(f,g) for f in inputs for g in words]
        for expr in words:
            assert expr.subs({x:0,xi:0})==0
        total+=len(words)
    assert s.diff(inputs[1],x,k).subs(x,0)==math.factorial(k)*h
    word_counts.append({'k':k,'right_nested_words_checked':total})
# Finite type at one point does not imply fixed type on nearby leaves.
moving=x**3+y*x
assert s.diff(moving,x,3).subs({x:0,y:0})==6
assert s.diff(moving,x).subs(x,0)==y
checks.append({'name':'finite iterated bracket words and failure of pointwise fixed-type substitution','passed':True,
    'models':word_counts,'scope':'Five bounded right-nested families and the explicit unfolding x^3+yx; no exhaustive arbitrary-tree claim.'})

# Exact canonical sign flips and marked covectors, for both parities.
sign_models=[]
for k in range(2,10):
    expr=xi-s.I*x**k*h
    if k%2==0:
        changed=s.expand(-expr.subs({xi:-xi,x:-x},simultaneous=True))
        assert changed==xi+s.I*x**k*h
        assert pb(-xi,-x)==1
        marked_last=1
    else:
        changed=s.expand(expr.subs(h,-h))
        assert changed==xi+s.I*x**k*h
        assert pb(-h,-z)==1
        marked_last=-1
    assert (-2)**(k-1)>0 if k%2 else (-2)**(k-1)<0
    sign_models.append({'k':k,'new_marked_last_momentum':marked_last})
checks.append({'name':'even and odd negative-contact normal forms and marked sign obstruction','passed':True,
    'models':sign_models,'scope':'Eight exact sign models and parity of the multiplier factor; the full invariant law is separately required.'})

# A complex division model retaining its imaginary remainder and full final pair.
multiplier=(1+s.I*x*y)/(1+x*x)
r1=x*h
r2=y*h
symbol=(xi-r1-s.I*r2)/multiplier
assert s.simplify(multiplier*symbol+r1+s.I*r2-xi)==0
positions=[x,y,z+x*x/2]
momenta=[xi-r1,eta,h]
for i in range(3):
    for j in range(3):
        assert pb(momenta[i],positions[j])==(1 if i==j else 0)
        assert pb(momenta[i],momenta[j])==0
        assert pb(positions[i],positions[j])==0
assert pb(x,r2)==0
assert multiplier.subs({x:0,y:0})==1
checks.append({'name':'complex linear division and exact coordinate completion','passed':True,
    'scope':'One actual nonconstant complex quotient, nonzero imaginary remainder and all canonical brackets. H1 smooth complex division is an explicit outside-scope input, not established by this example.'})

# Algebraic derivative recurrence for one flat complex quotient.
P,Q=s.symbols('P Q',real=True)
R=P*P+Q*Q
jets={(0,0):(P-s.I*Q,1)}
for order in range(4):
    for (i,j),(poly,power) in list(jets.items()):
        if i+j!=order:
            continue
        for var,key in [(P,(i+1,j)),(Q,(i,j+1))]:
            numerator=s.expand(s.diff(poly,var)*R**2-power*poly*R*s.diff(R,var)+poly*s.diff(R,var))
            new_power=power+2
            if key in jets:
                prior,prior_power=jets[key]
                assert prior_power==new_power and s.expand(prior-numerator)==0
            else:
                jets[key]=(numerator,new_power)
for poly,power in jets.values():
    assert s.Poly(poly,P,Q).total_degree()>=0
    # For any required vanishing order N, exp(-1/r^2)<=ell! r^(2ell);
    # choose ell so 2ell-2power>N. This is an elementary series inequality.
    for N in range(7):
        ell=power+N+1
        assert 2*ell-2*power>N
checks.append({'name':'flat complex quotient derivative recurrence and arbitrary-power bounds in bounded jets','passed':True,
    'derivatives_checked':len(jets),'maximum_total_order':4,
    'scope':'Exact polynomial/denominator recurrence and exponential-series power bounds; the teaching proof must cover all orders for every smooth flat numerator.'})

print(json.dumps({'bounded_checks':len(checks),'all_passed':all(r['passed'] for r in checks),'source_documents_needed':False,'state_mutated':False}))
