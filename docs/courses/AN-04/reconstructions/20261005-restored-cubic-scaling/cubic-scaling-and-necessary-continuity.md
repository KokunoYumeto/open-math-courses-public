# Cubic scaling and necessary continuity

The sufficient corank estimate spends one quarter of an order for each nongraph variable. A necessary estimate for an arbitrary relation spends only one twelfth. The difference comes from a test that concentrates at one tangent relation: graph variables shrink like \(T^{-1}\), nongraph variables like \(T^{-2/3}\), and the central frequency grows like \(T^2\). The surviving cubic phase controls what this test can detect.

We use the signed cotangent forms, ordinary symbol classes and half-density normalization from [Oscillatory distributions and their order](../20261005-restored-oscillatory/oscillatory-distributions-and-order.md). [Corank geometry and sufficient continuity](../20261005-restored-corank-continuity/corank-geometry-and-sufficient-continuity.md) proves the pointwise tangent normalization and partial Fourier form used here, including its zero two-jet. [Graph operators, continuity and Egorov](../20261005-restored-graph-egorov/graph-operators-continuity-and-egorov.md) proves proper elliptic graph quantizations and their microlocal inverses. [Homogeneous submanifold normal forms](../20261005-restored-submanifolds/homogeneous-submanifold-normal-forms.md) gives the sharper constant-rank result and explains why flattening the entire relation requires more than tangent normalization.

The primary source is the approved purchased reprint of Hörmander IV, corrected second printing (1994), [Theorem 25.3.9]. We give the complete ordinary-symbol proof, with its quantifier over every operator, a uniform integrable bound for negative amplitude orders, a nonzero limiting integral and the two different norm Jacobians. We retain the individual radial exclusions. Removing those exclusions by nonhomogeneous transformations, and proving the fold/Airy estimates which can attain the necessary threshold, remain separate targets.

The exact analytic foundations are already proved in the programme. [Schwartz estimates and Fourier inversion Q3–Q4](../20261004-free-stationary-phase/quadratic-stationary-phase.md) give the rapid Fourier decrease, its parameter-uniform bounds and the inverse factor. [Measure and integration M3–M5](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md) give dominated convergence, product integration and the norm inequalities. The stationary-phase lesson's [Taylor proof with compact parameters](../20261004-free-stationary-phase/stationary-phase-and-critical-manifolds.md) supplies the exact fourth-order remainder below. [Ordinary analytic composition](../20261005-restored-analytic-composition/clean-composition-of-fourier-integral-operators.md) supplies the composition and smooth-error statements used with the current graph inverses. The [proof map](proof-map.json) records exact locators and hypotheses for every result and solution.

## 1. A universal boundedness assumption can be tested at one point

Let \(C\subset(T^*X\setminus0)\times(T^*Y\setminus0)\) be a real homogeneous canonical relation with the full punctured-cotangent closure convention. Write \(\sigma_C\) for the common pullback of the two cotangent symplectic forms to \(C\).

**Theorem 1.1 (necessary corank bound).** Suppose neither individual lifted radial vector is tangent to \(C\). If every ordinary scalar half-density operator in \(I^m(X\times Y,C')\) is continuous
\[
A:L^2_{\mathrm{comp}}(Y)\longrightarrow L^2_{\mathrm{loc}}(X),
\tag{1.1}
\]
then at every \(c\in C\),
\[
\operatorname{corank}\sigma_C(c)\leq-12m.
\tag{1.2}
\]
No constant-rank neighborhood is assumed. The same necessity holds for bundle operators if both bundle ranks are positive at the point being tested.

Fix \(c_0\). The tangent normal form supplies \(n\) shared graph variables and \(a,b\) nongraph variables on the output and input, respectively:
\[
\dim X=n+a,\qquad \dim Y=n+b,\qquad
k=\operatorname{corank}\sigma_C(c_0)=a+b.
\tag{1.3}
\]
The radial exclusions give \(n\geq1\). In separate homogeneous canonical coordinates near \(c_0\), a partial phase is
\[
\Phi=\phi(x',x'',y'',\eta')-y'\cdot\eta',
\qquad \eta'\text{ near the ray }\theta=e_1.
\tag{1.4}
\]
It is real and homogeneous of degree one in \(\eta'\). The variables \((x',x'',y'',\eta')\) are coordinates on \(C\); at the marked point the base variables are zero and \(\eta'=\theta\). The difference
\[
h(x',x'',y'',\eta')=
\phi(x',x'',y'',\eta')-x'\cdot\eta'
\tag{1.5}
\]
has zero value, first derivatives and second derivatives there. All of these facts were proved from the tangent relation in the corank lesson, even when rank changes nearby.

The partial amplitude order and operator normalization are
\[
\mu=m+k/4,\qquad c_{n,k}=(2\pi)^{-n-k/4},
\tag{1.6}
\]
so a chosen operator has the local form
\[
(Bu)(x',x'')=c_{n,k}\iint
e^{i\phi(x',x'',y'',\eta')}
a(x',x'',y'',\eta')\widehat u(\eta',y'')\,d\eta'\,dy''.
\tag{1.7}
\]
The partial Fourier transform uses \(\widehat u(\eta',y'')=\int e^{-iy'\cdot\eta'}u(y',y'')\,dy'\), with inverse factor \((2\pi)^{-n}\).

**Lemma 1.2 (test after canonical changes).** The universal boundedness assumption in Theorem 1.1 implies boundedness for every compactly localized operator of the form (1.7) on the normalized relation.

**Proof.** Let \(U_X,U_Y\) be proper elliptic order-zero graph quantizations from the original charts to the normalized charts, and let \(V_X,V_Y\) be their proper microlocal inverses. For a normalized \(B\) supported in smaller interior base and conic neighborhoods, set \(A=V_XBU_Y\). Graph composition preserves order \(m\) and takes its relation back to \(C\). Add compact base cutoffs and extend by zero from the interior coordinate products. The supports can be chosen without changing the tested operator on its smaller neighborhoods. Indeed compact kernel support of \(B\) has two compact intermediate projections. Properness of \(V_X\) and \(U_Y\) gives compact sets of exterior base points over those projections, and cutoffs equal to one on these sets retain the composition. The microlocal inverse identities hold on smaller closed angular sets containing \(WF'(B)\), so each error composed against \(B\) has empty wavefront and is smooth there, by the complete composition proof. The resulting original operator belongs to \(I^m(C')\), hence is bounded by the assumption.

The two inverse identities and the wavefront composition theorem give
\[
U_XAV_Y=B+S
\tag{1.8}
\]
on the smaller working supports, where \(S\) has a smooth compactly localized kernel. The graph operators on the left are locally \(L^2\) bounded, and \(S\) is bounded on these compact supports. Proper supports allow the successive bounds to use common compact sets. Thus \(B\) is bounded. No flattening of the nonlinear relation or constant-rank hypothesis was used. ∎

It is therefore enough to construct **one fixed** normalized operator and a sequence of inputs which contradict its boundedness if (1.2) fails. The operator will not vary with the scaling parameter.

## 2. Choose a fixed amplitude and concentrated inputs

Choose smooth compact base factors equal to one near the marked base point. Choose a smooth angular factor equal to one near \(\theta\), with support in the phase cone, and a radial factor which vanishes near zero frequency and is one at large frequency. Denote their product by \(\chi(x',x'',y'',\eta')\). Use the ordinary symbol
\[
a=\chi\langle\eta'\rangle^\mu.
\tag{2.1}
\]
Its order is \(\mu\), so (1.7) has FIO order \(m\). For completeness, a frequency derivative of the smooth angular factor is homogeneous of degree minus its derivative order on the supported cone; all its normalized angular derivatives are bounded. The radial cutoff has derivatives in a fixed frequency annulus. Together with the proved estimates for \(\langle\eta'\rangle^\mu\), Leibniz's rule gives exactly \(S^\mu_{1,0}\) bounds for this fixed amplitude. The phase and order identification are the nondegenerate partial representation of the corank lesson; choosing an amplitude here does not assume any additional boundedness theorem. A further input base cutoff equal to one near zero makes the kernel support compact. For the inputs below this cutoff is exactly one for all sufficiently large \(T\). Thus we may use (1.7) exactly on those inputs. The construction uses a real phase and bounded cutoffs; an integrand outside the supported phase cone is defined to be zero.

Put \(\kappa=2/3\), and take \(u\in C_c^\infty(\mathbb R^n\times\mathbb R^b)\), to be specified later. Define
\[
u_T(y',y'')=
u(Ty',T^\kappa y'')e^{iT^2\theta\cdot y'},
\qquad T\geq2.
\tag{2.2}
\]
All these inputs have supports in a common compact neighborhood. Their exact norm is
\[
\|u_T\|_2=T^{-(n+\kappa b)/2}\|u\|_2.
\tag{2.3}
\]
Indeed the exponential has modulus one, while the input change of variables has Jacobian \(T^{-n-\kappa b}\).

The partial Fourier transform is also exact:
\[
\widehat u_T(\eta',y'')=
T^{-n}\widehat u(\eta'/T-T\theta,T^\kappa y'').
\tag{2.4}
\]
The frequency is centered at \(T^2\theta\) with spread \(T\), and the input nongraph scale is \(T^{-\kappa}\). Both features will enter the estimate.

Evaluate the output at
\[
x'=X'/T,\qquad x''=X''/T^\kappa,
\]
and substitute \(\eta'=T^2\theta+T\zeta\), \(y''=Y''/T^\kappa\) in (1.7). The factor \(T^n\) from \(d\eta'\) cancels \(T^{-n}\) in (2.4). The remaining parameter measure contributes \(T^{-\kappa b}\). Consequently
\[
\begin{split}
f_T(X',X'')&=(Bu_T)(X'/T,X''/T^\kappa)\\
&=c_{n,k}T^{-\kappa b}\iint
e^{i\phi(X'/T,X''/T^\kappa,Y''/T^\kappa,T^2\theta+T\zeta)}\\
&\qquad\qquad\quad\cdot
a(X'/T,X''/T^\kappa,Y''/T^\kappa,T^2\theta+T\zeta)
\widehat u(\zeta,Y'')\,d\zeta\,dY''.
\end{split}
\tag{2.5}
\]
These are ordinary absolutely convergent integrals for each smooth input: the partial Fourier transform decreases faster than every power and the amplitude has finite symbol order. This is the actual distributional kernel action: insert a smooth frequency cutoff in its defining oscillatory integral, perform the partial Fourier integration, and use the compact-input Fourier estimates to pass to the absolutely convergent limit. Fubini and dominated convergence justify the substitutions. The same estimates are uniform in \(Y''\) because the profile and all its derivatives have common compact support.

## 3. Only the pure nongraph cubic terms survive

The linear graph phase must be subtracted at its actual frequency:
\[
(X'/T)\cdot(T^2\theta+T\zeta)
=T X'\cdot\theta+X'\cdot\zeta.
\tag{3.1}
\]
In particular the second term remains of order one. Homogeneity gives
\[
\begin{split}
&\phi(X'/T,X''/T^\kappa,Y''/T^\kappa,T^2\theta+T\zeta)
-T X'\cdot\theta\\
&\qquad=X'\cdot\zeta+
T^2h(X'/T,X''/T^\kappa,Y''/T^\kappa,\theta+\zeta/T).
\end{split}
\tag{3.2}
\]

Write the third-order Taylor polynomial of \(h\) at \((0,0,0,\theta)\), in its base variables and its frequency increment. Define \(Q(X'',Y'')\) to be its part involving only the nongraph base variables. Explicitly,
\[
Q(X'',Y'')=
\frac16D^3h(0,0,0,\theta)
[(0,X'',Y'',0),(0,X'',Y'',0),(0,X'',Y'',0)].
\tag{3.3}
\]
It is a real homogeneous polynomial of degree three, possibly zero.

**Lemma 3.1 (cubic limit).** For \(\kappa=2/3\), uniformly on compact sets of \((X',X'',Y'',\zeta)\),
\[
T^2h(X'/T,X''/T^\kappa,Y''/T^\kappa,\theta+\zeta/T)
\longrightarrow Q(X'',Y'').
\tag{3.4}
\]

**Proof.** The constant, linear and quadratic terms are zero by (1.5). A pure nongraph cubic monomial has total scaling factor \(T^{-3\kappa}=T^{-2}\), so multiplying by \(T^2\) leaves exactly (3.3).

Any other cubic monomial contains a graph base variable or frequency increment, whose weight is \(T^{-1}\). Its other two factors have weights at most \(T^{-\kappa}\), hence its total weight is at most \(T^{-1-2\kappa}=T^{-7/3}\). After multiplication by \(T^2\) it tends to zero, uniformly on the specified compact sets. Terms with more graph/frequency factors decay at least as quickly.

Taylor's fourth-order remainder is bounded by a constant times the fourth power of the total increment on a fixed normalized neighborhood. On compact sets its increment is \(O(T^{-\kappa})\), so the multiplied remainder is \(O(T^{2-4\kappa})=O(T^{-2/3})\). This proves (3.4); mixed third-order terms give at worst \(O(T^{-1/3})\). No oscillatory term has been replaced by a small error before its scale was checked. ∎

The choice \(\kappa=2/3\) balances the cubic base phase with the central frequency: \(T^2(T^{-\kappa})^3=1\). The tangent normal form controls the two-jet, so a cubic balance is available at every marked point. It does not imply that the entire relation is flat.

## 4. The limit passes through the Fourier integral

Remove the rapid graph oscillation and amplitude size by setting
\[
g_T(X',X'')=
T^{-2\mu+\kappa b}e^{-iT X'\cdot\theta}f_T(X',X'').
\tag{4.1}
\]
For fixed \((X',X'',Y'',\zeta)\), the base and angular cutoffs in (2.1) are eventually one, as is its high-frequency radial cutoff. Also
\[
T^{-2\mu}\langle T^2\theta+T\zeta\rangle^\mu
\longrightarrow1,
\tag{4.2}
\]
since \(|\theta|=1\). Thus (3.4) gives the pointwise limiting integrand
\[
c_{n,k}e^{iX'\cdot\zeta+iQ(X'',Y'')}
\widehat u(\zeta,Y'').
\tag{4.3}
\]

We need a bound uniform over the whole \(\zeta\) integral, including the region where \(T^2\theta+T\zeta\) nearly cancels. A pointwise comparison with \(T^{2\mu}\) alone is insufficient when \(\mu<0\).

**Lemma 4.1 (uniform amplitude bound).** For every real \(\mu\), every \(T\geq2\), and all \(\zeta\), the normalized amplitude in (4.1) satisfies
\[
\left|T^{-2\mu}
a(X'/T,X''/T^\kappa,Y''/T^\kappa,T^2\theta+T\zeta)\right|
\leq C_\mu\langle\zeta\rangle^{2|\mu|}.
\tag{4.4}
\]
The bound is independent of the rescaled base variables.

**Proof.** The cutoffs are bounded, so it is enough to check the weight. If \(|\zeta|<T/2\), then \(|T^2\theta+T\zeta|\) lies between \(T^2/2\) and \(3T^2/2\). The normalized weight is bounded for either sign of \(\mu\).

For \(|\zeta|\geq T/2\) and \(\mu<0\), use \(\langle T^2\theta+T\zeta\rangle^\mu\leq1\). Then
\[
T^{-2\mu}\langle T^2\theta+T\zeta\rangle^\mu
\leq T^{2|\mu|}\leq C_\mu\langle\zeta\rangle^{2|\mu|}.
\]
For \(\mu\geq0\), the triangle inequality gives
\[
T^{-2}\langle T^2\theta+T\zeta\rangle
\leq C(1+|\zeta|/T)\leq C\langle\zeta\rangle.
\]
Raising to \(\mu\) gives an upper bound \(C_\mu\langle\zeta\rangle^\mu\), which is at most the required bound. The case \(\mu=0\) is immediate. ∎

The function \(\widehat u(\zeta,Y'')\) has compact \(Y''\) support and decreases rapidly in \(\zeta\), uniformly in \(Y''\). Therefore
\[
C_\mu\langle\zeta\rangle^{2|\mu|}
|\widehat u(\zeta,Y'')|
\]
is integrable. The real phase has modulus one. Dominated convergence proves
\[
\begin{split}
g_T(X',X'')&\longrightarrow
c_{n,k}\iint e^{iX'\cdot\zeta+iQ(X'',Y'')}
\widehat u(\zeta,Y'')\,d\zeta\,dY''\\
&=(2\pi)^{-k/4}\int
e^{iQ(X'',Y'')}u(X',Y'')\,dY''
=G(X',X'').
\end{split}
\tag{4.5}
\]
The second equality uses the exact partial Fourier inversion factor.

The convergence is uniform on each compact output set. To see this, first make the integral over large \(|\zeta|\) uniformly small using (4.4) and the common rapidly decreasing majorant. On its bounded complement, Lemma 3.1 and the amplitude convergence are uniform on compact output sets; \(Y''\) already stays in a fixed compact set. Combining the two estimates gives uniform convergence. We only need this local statement; \(G\) need not be globally square integrable in \(X''\).

## 5. Select a nonzero limit and compare the two Jacobians

The limit cannot be assumed nonzero for an arbitrary input. Choose it explicitly. Let \(v\in C_c^\infty(\mathbb R^n)\) have \(v(0)\neq0\). Let \(\rho\in C_c^\infty(\mathbb R^b)\) be nonnegative with positive integral. Put
\[
u(X',Y'')=v(X')e^{-iQ(0,Y'')}\rho(Y'').
\tag{5.1}
\]
Then
\[
G(0,0)=(2\pi)^{-k/4}v(0)\int\rho(Y'')\,dY''\neq0.
\tag{5.2}
\]
If \(b=0\), use the one-point integral convention and take its factor to be one. The same argument covers \(a=0\).

The function \(G\) is continuous. On each compact output neighborhood, the polynomial phase is continuous and bounded in modulus after exponentiation, and the profile has fixed compact \(Y''\) support. Dominated convergence in that finite integral proves continuity, including the one-point convention when \(b=0\). There is a fixed compact box \(D\) with positive measure around the marked output such that \(\|G\|_{L^2(D)}>0\). Uniform convergence in (4.5) implies that for all sufficiently large \(T\),
\[
\|g_T\|_{L^2(D)}\geq c>0.
\tag{5.3}
\]
One could also obtain a positive eventual lower bound from pointwise convergence and Fatou; neither method requires a global output limit.

The box in the original output variables is
\[
D_T=\{(X'/T,X''/T^\kappa):(X',X'')\in D\}.
\]
For large \(T\) it lies where a single fixed output cutoff equals one. Its Jacobian is \(T^{-n-\kappa a}\). Equations (4.1) and (5.3) give
\[
\begin{split}
\|Bu_T\|_{L^2(D_T)}
&=T^{2\mu-\kappa b-(n+\kappa a)/2}
\|g_T\|_{L^2(D)}\\
&\geq cT^{2\mu-\kappa b-(n+\kappa a)/2}.
\end{split}
\tag{5.4}
\]
The input norm (2.3) instead has the \(b\) Jacobian. By Lemma 1.2 our fixed operator is bounded between the common compact input support and that fixed output localization. Consequently
\[
cT^{2\mu-\kappa b-(n+\kappa a)/2}
\leq C\|u_T\|_2
=C T^{-(n+\kappa b)/2}\|u\|_2.
\tag{5.5}
\]
The constants may depend on this operator and input profile; they are independent of \(T\). Cancellation of the common powers gives
\[
T^{2\mu-\kappa(a+b)/2}\leq C',
\qquad\text{hence }2\mu\leq\kappa k/2=k/3.
\tag{5.6}
\]
Substitute \(\mu=m+k/4\):
\[
2m+k/2\leq k/3,
\qquad m\leq-k/12.
\tag{5.7}
\]
This is (1.2) at \(c_0\). Since the point was arbitrary, it holds throughout \(C\), proving Theorem 1.1.

For positive-rank bundles, use this scalar kernel in one input/output frame component, with smooth compact frame cutoffs. Compact metric equivalence and the same graph quantizations preserve the lower bound. A zero-rank bundle would have only the zero operator and gives no scalar test, so the necessity assertion requires the stated positive ranks. ∎

The proof concerns all operators in the order class. A particular smoothing operator is bounded regardless of the declared order and cannot impose the geometric bound on the class. The concentrated inputs vary; the positive leading amplitude chosen in (2.1) is fixed throughout.

## 6. The cubic model explains the gap

Consider the one-frequency partial phase
\[
\phi(x,z,w,\eta)=(x+zw^2)\eta,
\qquad \eta>0.
\tag{6.1}
\]
Here \(n=1\), \(a=b=1\). It gives the exact canonical relation
\[
(x,z;\eta,w^2\eta;
y=x+zw^2,w;\eta,-2zw\eta).
\tag{6.2}
\]
The common symplectic form has rank two at \(w=0\), rank four at \(w\neq0\); its corank at the marked point is \(k=2\). The common canonical one-form is \(\eta\,dx+w^2\eta\,dz\), nonzero throughout this cone. Thus the individual radial exclusions hold, but rank changes. These form and rank calculations were given in the corank lesson and can also be checked directly from (6.2).

Under our scaling, its phase is exactly
\[
\phi(X/T,Z/T^{2/3},W/T^{2/3},T^2+T\zeta)
=TX+X\zeta+ZW^2+T^{-1}\zeta ZW^2.
\tag{6.3}
\]
Thus \(Q(Z,W)=ZW^2\). The limiting operator on a profile is
\[
G(X,Z)=(2\pi)^{-1/2}\int e^{iZW^2}u(X,W)\,dW.
\tag{6.4}
\]
Taking \(u=v\rho\) with positive \(\int\rho\) makes \(G(0,0)\neq0\). Formula (5.6) then forces \(m\leq-1/6\).

The sufficient theorem applies to this relation when \(m\leq-1/2\), since its largest corank is two. The necessary argument gives \(m\leq-1/6\). These two statements alone do not decide boundedness at the intervening orders. The full constant-rank sharpness theorem cannot be substituted because this relation changes rank. Nor does this example by itself establish the two-sided fold hypotheses needed for the later fold theorem.

More generally, the cubic-controlled family could use any \(\kappa\geq2/3\). The pure nongraph cubic then remains bounded; for \(\kappa>2/3\) it tends to zero.

The other Taylor terms and the remainder also tend to zero for every such \(\kappa\), including \(\kappa>1\). A cubic monomial with \(r\) graph/frequency factors has exponent \(2-r-(3-r)\kappa\). For \(r=1,2,3\) this is strictly negative whenever \(\kappa\ge2/3\). The total increment is \(O(T^{-\min(1,\kappa)})\), so the fourth-order remainder after multiplication by \(T^2\) is \(O(T^{2-4\min(1,\kappa)})\), again tending to zero. At \(\kappa=2/3\) use the profile cancelling \(Q(0,Y'')\) as above; at larger \(\kappa\), the limiting cubic vanishes, and a profile \(v(X')\rho(Y'')\) has nonzero limit. Thus the same fixed-operator argument is justified throughout the stated range.

 The same norm calculation yields
\[
m\leq k(\kappa-1)/4.
\tag{6.5}
\]
Among these choices, \(\kappa=2/3\) gives the strongest obstruction. For \(\kappa<2/3\), a nonzero pure cubic term grows like \(T^{2-3\kappa}\), so the finite limiting integral used here is no longer available. One must analyze the extra oscillation before claiming a stronger bound. If the entire relation has been flattened, \(h=0\), the nongraph variables need not shrink; the separate flat-family test recovers the sharp \(m\leq-k/4\).

## 7. Exercises with complete solutions

**Exercise 7.1 (three distinct order statements; introductory).** At a point with \(k=3\), compute the sufficient bound, universal necessary bound and constant-rank sharp bound. What do these statements say about \(m=-1/2\) if rank may change, and if it is constant near that point?

**Solution.** The sufficient bound is \(m\leq-3/4\), while the necessary bound is \(m\leq-3/12=-1/4\). The constant-rank sharp bound is again \(m\leq-3/4\). The order \(-1/2\) obeys the necessary inequality but fails the sufficient one, so those estimates alone do not decide universal boundedness for a changing-rank relation. For constant rank the sharp theorem supplies an unbounded member of the class at that order. It does not assert that each individual operator of that declared order is unbounded.

**Exercise 7.2 (the input scale; intermediate).** Derive (2.3) and (2.4) for arbitrary positive \(\kappa\). Identify the central frequency and its spread, and state why the modulation does not affect the input norm.

**Solution.** Substitute \(Y'=Ty'\), \(Y''=T^\kappa y''\) in the squared norm. The measure is \(T^{-n-\kappa b}dY'dY''\), and the modulation has absolute value one, giving \(\|u_T\|_2=T^{-(n+\kappa b)/2}\|u\|_2\). In the partial transform substitute only \(Y'=Ty'\); its exponent is \(-iY'\cdot(\eta'/T-T\theta)\) and its measure is \(T^{-n}dY'\). This yields \(T^{-n}\widehat u(\eta'/T-T\theta,T^\kappa y'')\). The profile frequency variable stays bounded when \(\eta'=T^2\theta+T\zeta\), so the center is \(T^2\theta\) and the spread is \(T\).

**Exercise 7.3 (classify the Taylor terms; intermediate).** A cubic monomial contains \(r\) graph-base or frequency-increment factors and \(3-r\) nongraph-base factors. Find its power after multiplication by \(T^2\) at \(\kappa=2/3\). Do the same for a fourth-order remainder containing only nongraph factors.

**Solution.** The power is \(2-r-(3-r)\kappa\). Substituting \(\kappa=2/3\) gives \(-r/3\). The pure nongraph term \(r=0\) survives; the cases \(r=1,2,3\) decay like \(T^{-1/3},T^{-2/3},T^{-1}\), respectively. A pure fourth-order remainder has power \(2-4\kappa=-2/3\). These weights account for every cubic block and justify the uniform compact limit rather than assuming all of the cubic error is small.

**Exercise 7.4 (negative order near frequency cancellation; advanced).** Take \(\mu=-2\), \(\theta=e_1\), and \(\zeta=-T\theta\). Can the normalized weight in (4.2) be bounded independently of \(\zeta\)? Verify the polynomial majorant (4.4) at this point.

**Solution.** The frequency cancels: \(T^2\theta+T\zeta=0\). The raw normalized weight is \(T^4\), so it cannot have a uniform constant bound. The majorant is \(\langle\zeta\rangle^4=(1+T^2)^2\), which is at least \(T^4\). Our actual amplitude vanishes at zero frequency because of its cutoff, but near a fixed allowed low frequency the same raw-weight growth occurs; thus a low-frequency cutoff alone is not a proof of a constant bound. The polynomial majorant combined with the rapidly decreasing Fourier profile controls the whole integral.

**Exercise 7.5 (force a nonzero cubic limit; intermediate).** Let \(Q(Z,W)=W^3+ZW^2+Z^3\), with one variable on each side. Construct a compact smooth input whose limiting value at \((X,Z)=(0,0)\) is nonzero. Explain why this is preferable to assuming an arbitrary oscillatory integral is nonzero.

**Solution.** Choose \(v(0)\neq0\) and nonnegative compact smooth \(\rho\) with positive integral. Set \(u(X,W)=v(X)e^{-iW^3}\rho(W)\), since \(Q(0,W)=W^3\). At \((0,0)\) the two phases cancel exactly, so \(G(0,0)=(2\pi)^{-k/4}v(0)\int\rho\neq0\). An arbitrary compact input might have cancellation or zero average, giving no lower bound. This choice proves the needed nonvanishing with no sign or stationary-phase assumption on the cubic polynomial.

**Exercise 7.6 (unequal parameter dimensions; advanced).** Let \(n=2\), \(a=2\), \(b=1\), \(\kappa=2/3\), and \(m=-1/4\). Compute \(\mu\), the input norm exponent, the output lower-bound exponent, and their difference. What changes if \(m\) increases by \(\varepsilon>0\)?

**Solution.** Here \(k=3\) and \(\mu=m+k/4=1/2\). The input exponent is \(-(2+2/3)/2=-4/3\). The output exponent is \(2\mu-\kappa b-(n+\kappa a)/2=1-2/3-(2+4/3)/2=-4/3\), so the difference is zero. At the necessary threshold this test does not contradict boundedness. Increasing \(m\) by \(\varepsilon\) increases \(\mu\) by the same amount and the output exponent by \(2\varepsilon\); the ratio lower bound grows like \(T^{2\varepsilon}\), contradicting boundedness of the fixed operator. Interchanging the \(a\) and \(b\) Jacobians prematurely would obscure this cancellation.

**Exercise 7.7 (the exact changing-rank phase; advanced).** For (6.1), verify the signed canonical relation (6.2), compute the common form, and derive (6.3) without Taylor approximation.

**Solution.** Differentiating gives output frequencies \((\phi_x,\phi_z)=(\eta,w^2\eta)\), input graph base \(y=\phi_\eta=x+zw^2\), and input nongraph frequency \(-\phi_w=-2zw\eta\), yielding (6.2). The output pullback is
\[
\sigma=d\eta\wedge dx+w^2d\eta\wedge dz+2w\eta\,dw\wedge dz.
\]
The input pullback equals it by direct differentiation of \(y=x+zw^2\) and \(\eta''=-2zw\eta\). At \(w=0\) it has rank two. At \(w\neq0\), its square has a nonzero coefficient proportional to \(w\eta\), so its rank is four. Substitution into \((x+zw^2)\eta\) gives \((X/T+ZW^2/T^2)(T^2+T\zeta)=TX+X\zeta+ZW^2+T^{-1}\zeta ZW^2\), proving (6.3) exactly.

**Exercise 7.8 (keep the surviving graph Fourier term; intermediate).** For the flat phase \(\phi(x',\eta')=x'\cdot\eta'\), compare subtracting \(T X'\cdot\theta\) with subtracting the full \(T X'\cdot\theta+X'\cdot\zeta\). Why must \(X'\cdot\zeta\) stay in the Fourier integral in (4.5)?

**Solution.** The scaled phase is exactly \(T X'\cdot\theta+X'\cdot\zeta\). Demodulation by the rapid first term leaves \(e^{iX'\cdot\zeta}\), which reconstructs the profile \(u(X',Y'')\) by Fourier inversion. Subtracting both terms would remove that reconstruction and replace it by a zero-base evaluation. Conversely the exact scaled difference \(T^2[\phi(X'/T,\theta+\zeta/T)-\langle X'/T,\theta+\zeta/T\rangle]\) is zero in the flat model. These are different operations: subtracting the linear reference phase when estimating \(h\), and demodulating only the rapid part of the actual output. Keeping their frequencies identical avoids a false vanishing-error estimate.

**Exercise 7.9 (choose the nongraph shrinkage; advanced).** Derive (6.5) for \(\kappa\geq2/3\). Explain why taking \(\kappa=0\) in a general nonzero cubic model does not prove the sharp constant-rank bound. Explain when a zero-shrinkage test is justified instead.

**Solution.** The same two Jacobians give ratio exponent \(2\mu-\kappa k/2=2m+(1-\kappa)k/2\). Its nonpositivity is \(m\leq k(\kappa-1)/4\). At \(\kappa=2/3\) the cubic limit persists; at larger \(\kappa\) its pure nongraph part decays, and all other Taylor terms do too. At \(\kappa=0\) a nonzero pure nongraph cubic grows like \(T^2\), so the dominated finite-phase limit of this proof is unavailable. One cannot ignore that growing oscillation while retaining the norm calculation. After the entire relation has been flattened by the constant-rank theorem, \(h=0\) exactly and nongraph variables can stay in fixed compact sets. The separate fixed-profile modulation test then forces \(\mu\leq0\), or \(m\leq-k/4\). Tangent normalization alone does not authorize that step.

## References

- [Hörmander IV, Theorem 25.3.9] Lars Hörmander, *The Analysis of Linear Partial Differential Operators IV: Fourier Integral Operators*, Springer, approved purchased reprint of the corrected second printing (1994), §25.3, Theorem 25.3.9 and its proof. The preceding partial normalization is equation 25.3.5 and the cubic preparation is equation 25.3.6. The following nonhomogeneous-transformation remark and fold/Airy theorems are separate targets.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Restoration and exact programme prerequisite review: GPT-6 Astra (OpenAI), Ultra, 5 October 2026. Human mathematical review remains pending. Original text: public domain (CC0).*
