# Central sequences in modular crossed products

Approximate innerness of a modular automorphism produces centralizing unitaries of degree one in its discrete crossed product. This requires both a modular estimate for the approximate implementers and a passage from algebraic generators to every normal functional. After adding a tracial product factor, the unitaries become exact halving matrix units of degree one. The equivariant absorption theorem then applies.

## 1. The statements and the fixed conventions

Let \(M\ne0\) have separable predual, let \(\varphi\) be a faithful normal state, and fix \(T\in\mathbb R\). Write

\[
\alpha=\sigma_T^\varphi,\qquad
N=M\rtimes_\alpha\mathbb Z,\qquad UaU^*=\alpha(a).
\]

Use the positive-character dual action

\[
\gamma_z(a)=a,\qquad \gamma_z(U)=zU
\quad(z\in\mathbb T).
\tag{CDS.1}
\]

Let \(E:N\to M\) be the faithful normal expectation and put \(\psi=\varphi E\).

Assume that \(\alpha\) is approximately inner for pointwise norm convergence on the predual. There are unitaries \(w_n\in M\) with

\[
\operatorname{Ad}(w_n)\longrightarrow\alpha
\quad\hbox{in that topology}.
\tag{CDS.2}
\]

Indeed, choose a countable norm-dense set in \(M_*\), and at step \(n\) use the closure hypothesis to approximate the first \(n\) tests within \(1/n\). The isometry of the predual actions extends the convergence to every functional. Inverse convergence follows from DAS06.

**Central-unitary theorem.** The unitaries

\[
z_n=w_n^*U
\tag{CDS.3}
\]

are centralizing in \(N\):

\[
\|\eta z_n-z_n\eta\|\longrightarrow0
\qquad(\eta\in N_*).
\tag{CDS.4}
\]

They have degree one, \(\gamma_z(z_n)=zz_n\).

Let \(R=\bigotimes_{k\ge1}(M_2,\operatorname{tr}_2)\), and let \(\beta\) be the circle action of ECA01, with \(\beta_z(e_{12}^{(k)})=ze_{12}^{(k)}\).

**Absorption consequences.** The action \(\gamma\otimes\mathrm{id}_R\) on \(N\bar\otimes R\) is conjugate to

\[
(\gamma\otimes\mathrm{id}_R)\otimes\beta.
\tag{CDS.5}
\]

If \(M\cong M\bar\otimes R\) normally, then already

\[
(N,\gamma)\cong(N\bar\otimes R,\gamma\otimes\beta).
\tag{CDS.6}
\]

All displayed conjugacies have normal inverses. They are actual conjugacies of actions, not just cocycle conjugacies. These assertions do not require \(M\) or \(N\) to be factors.

The crossed-product representation, faithful expectation and its standard form are proved in DAS02–03. The argument uses AI04, the faithful-state modular theorem, FS02, FS04 and FS09, the cone estimates, SF07 and SF10–11, and CP04–07. The final tensor step uses the full proof ECA01–08, the product modular formula TG04, and the normalized cocycle SI14.

## 2. A faithful state controls the moving multipliers

For a faithful normal state \(\rho\) on an algebra \(A\), write \(\Omega=\xi_\rho\) in its standard GNS representation and

\[
\|x\|_\rho=\sqrt{\rho(x^*x)},\qquad
\|x\|_\rho^\#=\sqrt{\rho(x^*x)+\rho(xx^*)}.
\]

On bounded sets, \(\|x_n\|_\rho^\#\to0\) is equivalent to strong* convergence to zero in this representation, and hence to intrinsic sigma-strong* convergence. To verify the nontrivial direction, \(\|x_n\|_\rho\to0\) gives \(x_n\Omega\to0\). The vector \(\Omega\) is cyclic for \(A'\), by FS02. For \(b'\in A'\),

\[
x_nb'\Omega=b'x_n\Omega\longrightarrow0.
\]

Density and uniform boundedness give strong convergence on every vector. Applying the same argument to \(x_n^*\) proves the assertion. Conversely every positive normal functional has its cone vector by SF10, so strong* convergence gives each intrinsic seminorm. We abbreviate this bounded convergence as strongly* below.

Suppose \(a_n\) is uniformly bounded and centralizes just this state:

\[
\|\rho a_n-a_n\rho\|\longrightarrow0.
\]

AI04 gives

\[
a_n\Omega-\Omega a_n\longrightarrow0.
\tag{CDS.7}
\]

If \(r_n\to0\) strongly* and \(r_n\) is bounded, then

\[
\|r_na_n\Omega\|
\le\|r_n\|\|a_n\Omega-\Omega a_n\|
  +\|a_n\|\|r_n\Omega\|\longrightarrow0.
\tag{CDS.8}
\]

Its adjoint is \(a_n^*r_n^*\), which is bounded directly on \(\Omega\). The adjoint sequence \(a_n^*\) centralizes \(\rho\) as well. Applying (CDS.8) to the adjoint products proves

\[
r_na_n\longrightarrow0,\qquad a_nr_n\longrightarrow0
\quad\hbox{strongly*}.
\tag{CDS.9}
\]

Only centrality relative to the one faithful state was used. An arbitrary moving bounded multiplier would not justify the same inference.

We will also use the predual bounds, valid for positive normal \(\rho\),

\[
\|\rho r\|\le\sqrt{\rho(1)}\sqrt{\rho(rr^*)},
\qquad
\|r\rho\|\le\sqrt{\rho(1)}\sqrt{\rho(r^*r)}.
\tag{CDS.10}
\]

They follow by evaluating on the unit ball and applying Cauchy–Schwarz, as in ECA02. Thus multiplication of a fixed normal functional by a bounded strongly* null sequence tends to zero in predual norm. For general functionals use the four-positive-functional decomposition of CP07.

## 3. State centrality forces modular near-invariance

Let \(a_n\) be bounded and \(\|\varphi a_n-a_n\varphi\|\to0\). We prove

\[
\sigma_t^\varphi(a_n)-a_n\longrightarrow0
\quad\hbox{strongly* for each }t\in\mathbb R,
\tag{CDS.11}
\]

with convergence uniform for \(t\) in a fixed compact interval in the state seminorm.

Put \(\Omega=\xi_\varphi\), and let \(S=J\Delta^{1/2}\) be its closed Tomita operator. Every \(a_n\Omega\) lies in \(D(S)=D(\Delta^{1/2})\). The complete polar-domain formulas in FS04 give

\[
\Delta^{1/2}a_n\Omega=Ja_n^*\Omega=\Omega a_n.
\]

Therefore AI04 yields

\[
\|(\Delta^{1/2}-1)a_n\Omega\|
 =\|\Omega a_n-a_n\Omega\|\longrightarrow0.
\tag{CDS.12}
\]


For \(s>0\) and \(t\in\mathbb R\),

\[
|s^{it}-1|\le C_t|\sqrt s-1|,
\qquad C_t=4\max\{1,|t|\}.
\tag{CDS.13}
\]

Indeed, write \(r=\sqrt s\). If \(1/2\le r\le2\), use
\(|e^{2it\log r}-1|\le2|t||\log r|\le4|t||r-1|\).
Outside that interval, \(2\le4|r-1|\) bounds the left side. The spectral theorem on the full domain in (CDS.12) now gives

\[
\|(\Delta^{it}-1)a_n\Omega\|
 \le C_t\|(\Delta^{1/2}-1)a_n\Omega\|.
\tag{CDS.14}
\]

There is no spectral mass at zero, since \(\Delta\) is injective. The argument does not assume a bounded inverse for \(\Delta\).

FS04 gives \(\Delta^{it}\Omega=\Omega\), and FS09 implements the modular group. Hence the left side of (CDS.14) is
\(\|\sigma_t^\varphi(a_n)-a_n\|_\varphi\).
Apply the same proof to \(a_n^*\), whose functional defect has the same norm. This proves (CDS.11) by Section 2. On \(|t|\le L\), replace \(C_t\) by \(4\max\{1,L\}\) in both estimates, proving the stated uniformity.

This is near-invariance of one bounded sequence under modular time. It does not assert that the same sequence implements all modular automorphisms.

## 4. Consequences of approximate implementation

For the unitaries in (CDS.2), invariance of \(\varphi\) under \(\alpha\) gives

\[
\|w_n\varphi w_n^*-\varphi\|\longrightarrow0.
\]

Multiplication by a unitary is isometric on the predual, so

\[
\|\varphi w_n-w_n\varphi\|\longrightarrow0.
\tag{CDS.15}
\]

Section 3 applies to \(w_n\) and \(w_n^*\). In particular,

\[
\alpha(w_n)-w_n\longrightarrow0,\qquad
\alpha(w_n^*)-w_n^*\longrightarrow0
\quad\hbox{strongly* in }M.
\tag{CDS.16}
\]


We also need

\[
w_na w_n^*-\alpha(a)\longrightarrow0
\quad\hbox{strongly*}\qquad(a\in M).
\tag{CDS.17}
\]

Here is a direct proof of the topology implication. Put \(\alpha_n=\operatorname{Ad}(w_n)\). Predual norm convergence implies pointwise ultraweak convergence \(\alpha_n(x)\to\alpha(x)\) for every \(x\). For a positive normal \(\rho\), let \(d_n=\alpha_n(a)-\alpha(a)\). Expand

\[
\begin{aligned}
\rho(d_n^*d_n)
={}&\rho(\alpha_n(a^*a))
 -\rho(\alpha_n(a^*)\alpha(a))\\
 &-\rho(\alpha(a)^*\alpha_n(a))
 +\rho(\alpha(a)^*\alpha(a)).
\end{aligned}
\tag{CDS.18}
\]

Every term converges by the stated ultraweak convergence and the normality of fixed multiplication; the limit is zero. Replacing \(a\) by \(a^*\) gives the other seminorm. This proves (CDS.17) without converting weak convergence to strong convergence for arbitrary operators.

The regular representation of \(N\) may be taken on

\[
K=\ell^2(\mathbb Z;H_\varphi),\qquad
(a\eta)_k=\alpha^{-k}(a)\eta_k,\qquad
(U\eta)_k=\eta_{k-1}.
\tag{CDS.19}
\]

The faithful state \(\psi=\varphi E\) has cyclic separating vector
\(\Omega_N=\delta_0\Omega\), by DAS03. A sequence in \(M\) that tends strongly* to zero there also tends strongly* to zero in \(N\): its \(\psi\)-seminorms equal its \(\varphi\)-seminorms, and Section 2 applies to both faithful states.

Finally \(w_n\), viewed in \(N\), centralizes \(\psi\). Bimodularity of \(E\) identifies its functional commutator with
\((\varphi w_n-w_n\varphi)E\). The lift \(\chi\mapsto\chi E\) is isometric, since \(E\) is contractive and fixes \(M\). Thus (CDS.15) is exactly the corresponding estimate for \(\psi\).

## 5. From the generators to the entire predual

Put \(z_n=w_n^*U\). These are unitaries, and their degree in (CDS.1) is one. Define

\[
\delta_n=\operatorname{Ad}(w_n^*)\circ\alpha.
\]

Continuity of inversion and composition in the predual topology, proved in DAS06, gives \(\delta_n\to\mathrm{id}_M\).

The expectation intertwines the normalizer \(z_n\):

\[
E(z_nXz_n^*)=\delta_n(E(X)).
\tag{CDS.20}
\]

For a Fourier polynomial this follows by multiplication; normality extends it to all \(X\). Applying it to the inverse normalizer and using the isometric lift of functionals yields

\[
\|z_n\psi z_n^*-\psi\|
 =\|\varphi\circ\delta_n^{-1}-\varphi\|\longrightarrow0.
\]

Hence

\[
\|z_n\psi-\psi z_n\|\longrightarrow0.
\tag{CDS.21}
\]


For a fixed coefficient \(a\in M\), the exact commutator identity is

\[
z_na-az_n
 =w_n^*\bigl(\alpha(a)-w_na w_n^*\bigr)U.
\tag{CDS.22}
\]

The parenthesis tends strongly* to zero in \(N\), by Section 4. Since \(w_n^*\) centralizes the faithful state \(\psi\), (CDS.9) justifies the moving multiplier in (CDS.22). Right multiplication by the fixed \(U\) is continuous. Thus the commutator tends strongly* to zero.

For the implementing unitary itself,

\[
z_nU-Uz_n
 =\bigl(w_n^*-\alpha(w_n^*)\bigr)U^2
 \longrightarrow0
\quad\hbox{strongly*},
\tag{CDS.23}
\]

by (CDS.16). The identity
\([z_n,U^*]=-U^*[z_n,U]U^*\) handles the inverse. Taking adjoints handles commutators with \(z_n^*\). The Leibniz rule, involving only fixed polynomial factors, therefore gives

\[
[z_n,a]\longrightarrow0\quad\hbox{strongly*}
\qquad(a\in\mathcal P),
\tag{CDS.24}
\]

where \(\mathcal P\) is the unital *-algebra of finite Fourier polynomials.

It remains to prove predual norm centrality on all of \(N_*\). The span of

\[
a\psi b:X\longmapsto\psi(bXa),
\qquad a,b\in\mathcal P,
\tag{CDS.25}
\]

is norm dense in \(N_*\). Indeed \(\mathcal P\Omega_N\) is dense in \(K\): each Fourier degree contains all vectors \(\alpha^{-k}(a)\Omega\) in its coordinate. Every normal functional on the concrete \(N\subset B(K)\) is a summable series of vector coefficients, by CP04–06. First truncate that series, then approximate its finitely many vectors by \(\mathcal P\Omega_N\). The inequality

\[
\|\omega_{\xi,\eta}-\omega_{\xi',\eta'}\|
 \le\|\xi-\xi'\|\|\eta\|+\|\xi'\|\|\eta-\eta'\|
\]

proves the required norm approximation. These polynomial coefficients have exactly the form (CDS.25).

With the bounded module actions, the exact identity is

\[
[z_n,a\psi b]
 =[z_n,a]\psi b
   +a[z_n,\psi]b
   +a\psi[z_n,b].
\tag{CDS.26}
\]

The middle term tends to zero by (CDS.21); the outer terms do so by (CDS.24) and (CDS.10). Thus each functional (CDS.25) has commutator norm tending to zero. Uniformly in \(n\), the commutator map on the predual has norm at most \(2\), because \(\|z_n\|=1\). Norm density proves (CDS.4) for every \(\eta\in N_*\).

## 6. Exact halving units after a tracial amplification

Let \(e_n=e_{12}^{(n)}\) in the \(n\)-th leg of \(R\). ECA08 proves that \((e_n)\) is centralizing in \(R\), and

\[
e_n^2=0,\qquad e_n^*e_n+e_ne_n^*=1.
\]

On \(\widetilde N=N\bar\otimes R\), set

\[
v_n=z_n\otimes e_n,\qquad
\widetilde\gamma=\gamma\otimes\mathrm{id}_R.
\tag{CDS.27}
\]

The two tensor legs commute exactly, so

\[
v_n^2=0,\qquad
v_n^*v_n+v_nv_n^*=1,\qquad
\widetilde\gamma_z(v_n)=zv_n.
\tag{CDS.28}
\]


These units centralize the entire predual of \(\widetilde N\). For elementary normal functionals,

\[
\begin{aligned}
&(\eta\otimes\chi)(z_n\otimes e_n)
 -(z_n\otimes e_n)(\eta\otimes\chi)\\
&\quad=(\eta z_n-z_n\eta)\otimes(\chi e_n)
 +(z_n\eta)\otimes(\chi e_n-e_n\chi).
\end{aligned}
\tag{CDS.29}
\]

The norm tends to zero, since a normal product functional has norm
\(\|\eta\otimes\chi\|=\|\eta\|\|\chi\|\).
For completeness, the upper bound follows by lifting the two functionals to projective vector-series representatives in CP04–06, tensoring their coefficient vectors, and taking the infima of the lift norms. The lower bound follows by testing on \(a\otimes b\) with both factors arbitrarily near their norm suprema. This also constructs the normal product functional. Finite sums of such functionals are norm dense: approximate vectors in a faithful tensor representation by finite sums of elementary tensor vectors, then use the same vector-coefficient and series argument as in Section 5. The uniform bound \(\|v_n\|=1\) extends (CDS.29) to all normal functionals.

The algebra \(\widetilde N\) has separable predual, as required by ECA. Here are the representation details. The positive cone of \(M_*\) is norm separable. The estimate
\(\|\xi_\rho-\xi_\eta\|^2\le\|\rho-\eta\|\), together with SF10–11's onto correspondence with the standard cone, makes that cone separable. Its dense complex span makes \(H_\varphi\) separable. Thus \(K=\ell^2(\mathbb Z;H_\varphi)\) is separable. The finite-support tensor basis for \(H_R\) is countable, as proved in TS05, so \(K\otimes H_R\) is separable. The concrete-predual quotient of CP04–06 gives a separable predual for \(\widetilde N\).

ECA01–07 now applies to (CDS.28)–(CDS.29), and proves (CDS.5), with its explicit normal equivariant isomorphism and inverse. This use of ECA involves exact halving relations, not asymptotic replacements for them.

There is also a useful identification with a modular crossed product:

\[
\widetilde N
 \cong(M\bar\otimes R)
       \rtimes_{\sigma_T^\varphi\otimes\mathrm{id}}\mathbb Z.
\tag{CDS.30}
\]

The coordinate regrouping

\[
\ell^2(\mathbb Z;H_\varphi\otimes H_R)
 \longrightarrow\ell^2(\mathbb Z;H_\varphi)\otimes H_R
\]

is an onto unitary, first defined on elementary finite-coordinate vectors. It sends the regular coefficient of \(a\otimes b\) to the coefficient of \(a\) tensored with \(b\), and the shift to \(U\otimes1\). These images generate exactly \(N\bar\otimes R\). Therefore the map and its inverse are normal on the whole algebras, and the diagonal circle implementers show that (CDS.30) is dual-equivariant. TG04 identifies its automorphism with \(\sigma_T^{\varphi\otimes\tau}\), since the trace's modular operator is one.

## 7. Changing the state and removing the amplification

We first make state transport explicit. For faithful normal states \(\varphi,\chi\) on the same algebra, SI14 gives

\[
c_t=[D\chi:D\varphi]_t,\qquad
c_{s+t}=c_s\sigma_s^\varphi(c_t),\qquad
\sigma_t^\chi=\operatorname{Ad}(c_t)\sigma_t^\varphi.
\tag{CDS.31}
\]

Put \(c_k=c_{kT}\), \(\alpha=\sigma_T^\varphi\), and \(\alpha'=\sigma_T^\chi\). These identities include all negative integers.

Represent both regular crossings over the same faithful normal representation of \(M\). On the regular Hilbert space, the diagonal operator

\[
(D\eta)_k=c_{-k}^*\eta_k
\tag{CDS.32}
\]

is unitary, with inverse multiplying coordinate \(k\) by \(c_{-k}\). Since
\((\alpha')^{-k}=\operatorname{Ad}(c_{-k})\alpha^{-k}\), it sends the \(\alpha'\)-coefficient of \(a\) to the \(\alpha\)-coefficient of \(a\). On the shift its coordinate multiplier is

\[
c_{-k}^*c_{1-k}=\alpha^{-k}(c_1).
\]

Thus it proves a normal onto isomorphism

\[
M\rtimes_{\alpha'}\mathbb Z\longrightarrow
M\rtimes_\alpha\mathbb Z,\qquad
a\longmapsto a,\quad U_\chi\longmapsto c_1U_\varphi.
\tag{CDS.33}
\]

The image generates the whole target because it contains \(M\) and hence \(U_\varphi=c_1^*(c_1U_\varphi)\). The inverse sends \(U_\varphi\) to \(c_1^*U_\chi\). The diagonal unitary in (CDS.32) commutes with the diagonal circle implementers. Consequently (CDS.33) conjugates the dual actions exactly.

The common representation can be compared explicitly with the faithful GNS representation of \(\chi\): the map \(a\Omega_\chi\mapsto a\xi_\chi\) is an isometry into the standard representation already used. Faithfulness and the support description in SF06, together with \(J\xi_\chi=\xi_\chi\), make \(\xi_\chi\) cyclic, so the map is onto. It intertwines \(M\), and its coordinatewise sum intertwines the corresponding regular coefficients and shifts. Thus the use of a common representation in (CDS.32) introduces no unproved representation-independence assumption.

Now assume a normal isomorphism \(J:M\to M\bar\otimes R\) with normal inverse is given. Put

\[
\chi=(\varphi\otimes\tau)\circ J.
\]

This is a faithful normal state. Its GNS comparison

\[
a\Omega_\chi\longmapsto J(a)\Omega_{\varphi\otimes\tau}
\]

is an onto isometry and intertwines the complete Tomita graph cores; closure and polar uniqueness intertwine their modular operators. Therefore \(J\sigma_T^\chi J^{-1}
=\sigma_T^\varphi\otimes\mathrm{id}_R\), also as given by TG04. The coordinatewise GNS unitary extends this to a normal isomorphism of the regular crossings preserving their shifts and dual actions.

Combining that isomorphism with (CDS.30) and (CDS.33) gives

\[
(N,\gamma)\cong
 (N\bar\otimes R,\gamma\otimes\mathrm{id}_R).
\tag{CDS.34}
\]

Transport (CDS.5) through (CDS.34) on the first tensor factor. This proves (CDS.6), including a normal inverse and exact equivariance.

Only the indicated state-independent dual action was transported. We did not claim that a chosen isomorphism \(J\) preserves the original state, or that a coefficient-preserving map removes the tracial amplification.

## 8. Applications and exact boundary checks

**The approximate-finite-dimensional input.** For an AFD or semidiscrete type III₁ factor with separable predual, MI01–06 proves that every \(\sigma_T^\varphi\) is approximately inner. Hence the central-unitary conclusion (CDS.3)–(CDS.4) and the amplified absorption (CDS.5) hold for each faithful normal state and each fixed \(T\). If its tracial-product absorption has also been established, Section 7 yields the unamplified dual-action absorption. The earlier action-classification and strong-stability arguments needed in the complete uniqueness theorem are separate obligations; this lemma does not infer them from approximate innerness.

**An exact inner modular action.** On \(M_2\) take

\[
h=\operatorname{diag}(4/5,1/5),\qquad
\varphi(a)=\operatorname{Tr}(ha),\qquad
T=\frac{\pi}{2\log4}.
\]

The bounded-density formula FS10 gives \(\sigma_t^\varphi(a)=h^{it}ah^{-it}\). Thus \(\sigma_T^\varphi=\operatorname{Ad}(w)\) with
\(w=\operatorname{diag}(i,1)\); the scalar phase of \(h^{iT}\) cancels in its conjugation. The constant implementer \(w_n=w\) centralizes \(\varphi\) and is fixed by \(\sigma_t^\varphi\). Consequently \(w^*U\) is exactly central in the crossed product. The adjoint in (CDS.3) matters. For \(a=e_{12}\),

\[
w^*\alpha(a)-aw^*=0,\qquad
w\alpha(a)-aw=-2e_{12}.
\tag{CDS.35}
\]

Using \(wU\) instead would fail to commute with this coefficient.

**Why the two tensor legs are used.** Multiplying a square-zero partial isometry by an arbitrary unitary need not preserve its square-zero relation. In \(M_2\), put

\[
e=e_{12},\qquad s=e_{12}+e_{21}.
\]

Then \(s\) is unitary, but \(es=e_{11}\) and \((es)^2=e_{11}\ne0\). The exact relations in (CDS.28) follow from the separate tensor legs, where commutation is automatic. Mere asymptotic commutation would not give those identities at each index.

**A central unitary alone is insufficient.** For \(M=\mathbb C\), the modular action is trivial and
\(N=L(\mathbb Z)\). Taking \(w_n=1\) gives the central degree-one unitary \(U\). But this abelian algebra has no nonzero square-zero partial isometry, and it cannot be isomorphic to \(N\bar\otimes R\), which contains a noncommutative matrix algebra. Thus the central-unitary conclusion does not remove the tracial-absorption hypothesis from (CDS.6). Adding \(R\) as in Section 6 supplies exactly the missing halving units.

**Time and continuity.** The construction is for a fixed \(T\); \(T=0\) is allowed. In that case \(w_n=1\) is available, \(N=M\bar\otimes L(\mathbb Z)\), and the same conclusions hold. The compact-time estimate in Section 3 concerns near-invariance of \(w_n\); it is not a simultaneous approximate implementation of the full modular group by one compatible family of unitaries.

## Source

Masamichi Takesaki, *Theory of Operator Algebras III*, Chapter XVIII, Section 4, proof of Theorem 4.16(i), printed p.396. This lesson supplies the modular near-invariance estimate, the entire predual argument, the exact independent-leg matrix construction, and the normal dual-equivariant state transport used in that part of the proof. It does not assert the remaining action-classification steps of the uniqueness theorem.
