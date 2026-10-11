# Compatible modular weights and the full positive cone

A compatible pair of modular flows determines an operator-valued weight. To construct it, we first pass to two crossed products with traces, construct a trace-preserving map there, and descend to their fixed algebras. One common spectral density and a surjective extended-positive average carry the scalar identity through this descent, including its infinite values. Inner products are linear in the first variable.

## Reconstruction from compatible modular flows

Let \(N\subset M\) be a unital inclusion of von Neumann algebras, with no countability assumption. Let \(\varphi\) on \(N\) and \(\psi\) on \(M\) be faithful normal semifinite weights. Suppose
\[
\sigma_t^\psi(n)=\sigma_t^\varphi(n)
\quad(n\in N,\ t\in\mathbb R).
\tag{OE.1}
\]
Then there is a unique faithful normal semifinite operator-valued weight \(E:M_+\to\widehat N_+\) such that
\[
\psi(x)=\widehat\varphi(E(x))
\quad(x\in M_+).
\tag{OE.2}
\]
Equality is in \([0,\infty]\). Conversely, composing an existing faithful normal semifinite operator-valued weight with such a \(\varphi\) gives a faithful normal semifinite scalar weight satisfying (OE.1).

The proof occupies OE-02–06. Its scalar Fourier input is Euclidean Fourier analysis. Its weight inputs are normal extension and full range, classification of every invariant normal weight, and forward modular restriction for an existing operator-valued weight. The last result is proved independently of this reconstruction. We will establish the additional commutant and orbit-integration facts below.

## A concrete common crossed-product pair

We first record the harmonic facts in precisely the multiplicity needed here. Write \(D_s\) for multiplication by \(e^{-isr}\) and \(R_t\) for translation \(\xi(r)\mapsto\xi(r+t)\) on \(L^2(\mathbb R)\).

**The scalar and tensor commutants.** An operator commuting with every \(D_s\) commutes with every multiplication operator. Indeed the generator of \(D_s\) is multiplication by \(-r\); commutation with the unitary group implies commutation with its spectral projections by spectral transport. Bounded simple functions and strong limits give all bounded measurable multipliers.

The multiplication algebra is maximal abelian. To check this directly, let \(A\) commute with its multipliers and choose \(g(r)=e^{-r^2}>0\). Define \(b=(Ag)/g\) almost everywhere. For every measurable set \(F\),
\[
\|1_F b g\|_2=\|A(1_F g)\|_2
\leq\|A\|\|1_F g\|_2.
\]
The sets where \(|b|>\|A\|+\varepsilon\) must have measure zero, so \(b\in L^\infty\) with norm at most \(\|A\|\). On every vector \(fg\), \(f\in L^\infty\), commutation gives \(A(fg)=bfg\). These vectors are dense: truncate the measurable ratio of an arbitrary \(L^2\) vector to \(g\). Thus \(A\) is multiplication by \(b\).

If \(A\) also commutes with every \(R_t\), then \(b(r+t)=b(r)\) for almost every \(r\), for each fixed \(t\). This implies that \(b\) is constant, without choosing one null set for all \(t\). Choose a nonnegative smooth compactly supported approximate identity \(\rho_\varepsilon\) of mass one, as constructed in BI-03. For each \(\varepsilon\), convolution \(b*\rho_\varepsilon\) is continuous, and the preceding almost-everywhere identity makes it invariant under every translation. It is therefore a constant \(c_\varepsilon\). For \(f\in L^1\), Fubini and the [\(L^1\) approximate-identity theorem in AN-02, §15.4](../constant-coefficient-equations-and-solvability/prerequisites/banach-foundation-bridges.html#the-original-scaled-approximate-identity) give
\[
\int f(r)(b*\rho_\varepsilon)(r)\,dr
\longrightarrow\int f(r)b(r)\,dr.
\]
Taking one \(f\) of integral one shows that \(c_\varepsilon\) has a limit \(c\); the formula for all \(f\) then gives \(b=c\) almost everywhere. Consequently \(\{D_s,R_t:s,t\in\mathbb R\}'=\mathbb C1\).

On \(H\otimes L^2(\mathbb R)\), take matrix coefficients between any two vectors in \(H\). If an operator commutes with \(1\otimes D_s\) and \(1\otimes R_t\), each such coefficient is a scalar operator on \(L^2(\mathbb R)\). Those scalars form a bounded sesquilinear form on \(H\), represented by some \(a\in B(H)\). Testing elementary tensors proves that the original operator is \(a\otimes1\). No basis or separability assumption on \(H\) is used.

**The regular pair.** Represent \(M\) faithfully and normally on the GNS space \(H_\psi\), and put \(U_t=\Delta_\psi^{it}\). On \(\mathcal H=L^2(\mathbb R,H_\psi)\) define
\[
\begin{aligned}
(\pi(m)\xi)(r)&=U_{-r}mU_r\xi(r),\\
(\lambda(t)\xi)(r)&=\xi(r-t),\\
(D_s\xi)(r)&=e^{-isr}\xi(r).
\end{aligned}
\tag{OE.3}
\]
Equation (OE.1) gives the same action on \(N\). Set
\[
\begin{gathered}
P=(\pi(M),\lambda(\mathbb R))'',\\
Q=(\pi(N),\lambda(\mathbb R))''\subset P.
\end{gathered}
\tag{OE.4}
\]
The unitary \((V\xi)(r)=U_r\xi(r)\) conjugates \(\pi(m)\) to \(m\otimes1\), proving faithfulness and normality. The strongly continuous shifts satisfy
\(\lambda(t)\pi(m)\lambda(t)^*=\pi(\sigma_t^\psi(m))\).
Conjugation by \(D_s\) preserves both generated algebras and defines their common dual action \(\theta_s\). It fixes \(\pi(M)\) and sends \(\lambda(t)\) to \(e^{-ist}\lambda(t)\).

**Fixed points.** The operators \((V_t\xi)(r)=U_t\xi(r+t)\) commute with \(P\), and \(VV_tV^*=1\otimes R_t\). If \(X\in P\) is fixed by every \(\theta_s\), then \(VXV^*\) commutes with both families in the tensor commutant calculation. Hence \(VXV^*=a\otimes1\). Every constant \(a'\in M'\) commutes with \(P\): it commutes with the coefficient algebra at every \(r\) and with the shifts. After conjugation by \(V\), this says that the multiplier \([a,U_r a'U_r^*]\) vanishes. For any fixed pair of vectors its scalar coefficient is continuous in \(r\) and zero almost everywhere, hence zero at \(r=0\). Thus \([a,a']=0\) and \(a\in M\). We have proved \(P^\theta=\pi(M)\).

The same argument with \(N'\) gives \(Q^\theta=\pi(N)\), since (OE.1) makes every coefficient of \(\pi(N)\) belong to \(N\). Testing one continuous coefficient at a time avoids a simultaneous uncountable null-set assertion. Finally, an invariant extended positive has invariant finite spectral projections and invariant infinite-part projection. Spectral-pair uniqueness therefore gives the same fixed-point identities in the extended positive cones. We henceforth identify \(M,N\) with \(\pi(M),\pi(N)\).

## Dual averages and one normalized trace density

For \(X\in P_+\), define its positive orbit integral by
\[
T_P(X)=\int_{\mathbb R}\theta_s(X)\,ds.
\tag{OE.5}
\]
Here is the precise construction. On a compact interval \(K\), the map \(s\mapsto\omega\circ\theta_s\) is norm continuous in the predual. For a vector functional this follows from strong continuity of \(D_s\) and
\(\|\omega_\xi-\omega_\eta\|\leq(\|\xi\|+\|\eta\|)\|\xi-\eta\|\).
The vector-series representation of normal functionals, followed by its norm-convergent tails, proves the assertion for every normal functional. Its norm integral defines a bounded predual map; its adjoint is the normal positive map
\[
B_K(X)=\int_K\theta_s(X)\,ds.
\]
The norm integral is obtained by compact-interval Riemann sums, as in BI-02. Thus its values belong to \(P\).

For positive \(X\), the increasing supremum of \(B_{[-j,j]}(X)\), evaluated on positive normal functionals, is an extended positive. Its evaluation is the scalar integral in (OE.5). Translation invariance of Lebesgue measure fixes this element under \(\theta\), so OE-02 places it in \(\widehat M_+\). Additivity and positive homogeneity follow from integration. For \(X_i\uparrow X\), normality of each compact average gives
\[
\begin{aligned}
T_P(X)(\omega)
&=\sup_j\sup_i\omega(B_{[-j,j]}X_i)\\
&=\sup_i T_P(X_i)(\omega).
\end{aligned}
\]
These scalar tests and the spectral-pair embedding prove normality. Since \(M\) is fixed, bounded sandwiches by \(M\) pass through the integral, giving bimodularity. If the integral is zero, each continuous nonnegative function \(s\mapsto\omega(\theta_sX)\) is zero at \(s=0\). Hence \(X=0\), proving faithfulness. The same construction gives \(T_Q:Q_+\to\widehat N_+\).

**Semifiniteness without a countable multiplicity assumption.** Put \(\lambda(f)=\int f(t)\lambda(t)\,dt\) for \(f\in C_c(\mathbb R)\). For fixed \(\xi\in\mathcal H\), the function \(v(t)=f(t)\lambda(t)\xi\) is continuous and compactly supported. Its range has a separable closed linear span. Expand there in a countable orthonormal basis, apply the \(m=1\) Plancherel formula of BI-03 to each coordinate, and interchange nonnegative sums and integrals. The minus sign in the Fourier kernel merely reflects the frequency variable. This proves
\[
\begin{aligned}
\int\|\theta_s(\lambda(f))\xi\|^2\,ds
&=2\pi\int |f(t)|^2\|\lambda(t)\xi\|^2\,dt\\
&=2\pi\|f\|_2^2\|\xi\|^2.
\end{aligned}
\]
Vector functionals consequently give
\[
T_P(\lambda(f)^*\lambda(f))
=2\pi\|f\|_2^2 1.
\tag{OE.6}
\]
Choose nonnegative \(f_j\in C_c\), of integral one and support shrinking to zero. Strong continuity gives \(\lambda(f_j)\to1\) strongly: apply the bound \(\int f_j(t)\|\lambda(t)\xi-\xi\|\,dt\) to each vector. Each \(\lambda(f_j)\) belongs to \(\mathfrak n_{T_P}\), and this is a left ideal, because
\[
T_P((A\lambda(f_j))^*A\lambda(f_j))
\leq\|A\|^2 T_P(\lambda(f_j)^*\lambda(f_j)).
\]
Thus \(A\lambda(f_j)\to A\) strongly for every \(A\in P\), proving semifiniteness. The argument applies to \(Q\) as well. The scalar-composition theorem now makes
\(W_P=\widehat\psi\circ T_P\) and \(W_Q=\widehat\varphi\circ T_Q\) faithful normal semifinite weights.

**The modular group and its trace normalization.** Apply OR-03 to these existing operator-valued weights. It gives the required modular action on \(M\), respectively \(N\). Phases cancel under conjugation by \(\lambda(u)\), so moving that conjugation through (OE.5) gives
\[
T_P(\lambda(u)X\lambda(u)^*)
=\widehat{\sigma_u^\psi}(T_P(X)).
\]
Modular invariance of \(\psi\), extended by CW-03, therefore gives \(W_P\circ\operatorname{Ad}\lambda(u)=W_P\). The same holds for \(W_Q\).

For clarity, invariance under this inner automorphism forces \(\lambda(u)\) into the scalar centralizer. The normalized inner cocycle identity is
\[
[D(W\circ\operatorname{Ad}v):DW]_t
=v^*\sigma_t^W(v).
\]
It follows directly from balanced matrix cocycles and modular transport: conjugate \(W\oplus W\) by \(d=\operatorname{diag}(1,v)\), and read the coefficient of \(e_{21}\) in \(d^*\sigma_t^{W\oplus W}(d e_{21}d^*)d\). If the weights agree, that coefficient is one. Thus \(\sigma_t^W(\lambda(u))=\lambda(u)\). Since \(M\) and the \(\lambda(u)\) generate \(P\),
\(\sigma_t^{W_P}=\operatorname{Ad}\lambda(t)\); likewise on \(Q\).

The unitary-generator theorem supplies one positive injective affiliated operator \(h\) with \(h^{it}=\lambda(t)\). Its spectral projections lie in \(Q\) and in both centralizers. Put \(k=h^{-1}\), and define \(\tau_P=(W_P)_k\), \(\tau_Q=(W_Q)_k\). The density construction makes these weights faithful normal semifinite; its modular formula makes their modular groups trivial.

A faithful normal semifinite weight with trivial modular group is a trace. Indeed the centralizer criterion makes every bounded element a two-sided multiplier of its finite linear domain and permits cyclicity there. For \(x=v|x|\) with \(\tau(x^*x)<\infty\), apply cyclicity to \(v(x^*x)v^*\) to get \(\tau(xx^*)=\tau(x^*x)\). If either side is finite the same argument, applied also to \(x^*\), applies; otherwise both are infinite. This proves the trace identity on all bounded \(x\).

The exact density cocycle and cocycle reversal yield
\[
\begin{gathered}
\bigl[DW_P:D\tau_P\bigr]_t=\lambda(t),\\
\bigl[DW_Q:D\tau_Q\bigr]_t=\lambda(t).
\end{gathered}
\tag{OE.7}
\]
Fixed-reference injectivity proves uniqueness with this normalization. Moreover \(\theta_s(h)=e^{-s}h\), by uniqueness of the generator. The weights \(W\) are dual-invariant, and their bounded density regularizations consequently give
\[
\tau\circ\theta_s
=W_{\theta_{-s}(k)}
=W_{e^{-s}k}=e^{-s}\tau.
\]
The last equality follows from \((ck)_\varepsilon=c k_{c\varepsilon}\), including infinite values. This fixes the scaling sign directly from the chosen dual action.

## Tracial induction without a semifinite restriction

For a faithful normal semifinite trace \(\tau\) on an algebra \(A\), define the pairing
\[
\langle H,y\rangle_\tau
=\widehat\tau(y^{1/2}Hy^{1/2}),
\quad H\in\widehat A_+,\ y\in A_+.
\]
By PT-08, \(\sigma^\tau\) is trivial. Every normal weight on \(A\) is therefore invariant. CW-11 applies with centralizer \(A\) and proves that
\(H\mapsto\langle H,\cdot\rangle_\tau\) is an order isomorphism onto **all** normal weights on \(A\), preserving increasing suprema in both directions. It includes zero, nonfaithful weights, and weights with an infinite part. In particular it does not assume that a represented weight is semifinite.

To identify its formula, take bounded spectral cutoffs \(H_j\uparrow H\), including the value \(j\) on the infinite part. Traciality gives
\[
\langle H,y\rangle_\tau
=\sup_j\tau(y^{1/2}H_jy^{1/2})
=\sup_j\tau(H_j^{1/2}yH_j^{1/2}).
\]
These are the normal density weights of CW-11. For fixed \(y\), evaluation is the normal extension of the weight \(a\mapsto\tau(y^{1/2}ay^{1/2})\); hence it is additive and preserves increasing suprema in \(H\) by CW-03. The same properties in \(y\) follow from the last displayed formula. Bounded trace cyclicity, first for \(H_j\) and then by normal extension, gives the sandwich identity
\[
\langle a^*Ha,y\rangle_\tau
=\langle H,aya^*\rangle_\tau
\quad(a\in A).
\]
Thus these pairings separate extended positives and reflect their order.

Now let \(Q\subset P\) be any unital inclusion with faithful normal semifinite traces \(\tau_Q,\tau_P\). For \(X\in P_+\), set
\[
\chi_X(y)=\tau_P(y^{1/2}Xy^{1/2}),
\quad y\in Q_+.
\tag{OE.8}
\]
Traciality rewrites this as \(\tau_P(X^{1/2}yX^{1/2})\), which proves that it is a normal weight on \(Q\). It need not be semifinite: for \(Q=\mathbb C1\subset B(\ell^2)\) and \(X=1\), it is infinite on every nonzero positive scalar. The full correspondence just proved supplies a unique \(S(X)\in\widehat Q_+\) satisfying
\[
\langle S(X),y\rangle_{\tau_Q}
=\chi_X(y)
\quad(y\in Q_+).
\tag{OE.9}
\]
Additivity, homogeneity, and normality transfer through this correspondence. More explicitly, if \(X_i\uparrow X\), then \(\chi_{X_i}\uparrow\chi_X\); order reflection and preservation of increasing suprema give \(S(X_i)\uparrow S(X)\). Cyclicity gives
\(\chi_{a^*Xa}(y)=\chi_X(aya^*)\) for \(a\in Q\), so the sandwich identity and uniqueness imply \(S(a^*Xa)=a^*S(X)a\).

Setting \(y=1\) gives
\[
\widehat\tau_Q(S(X))=\tau_P(X)
\quad(X\in P_+).
\tag{OE.10}
\]
Thus \(S\) is faithful. If \(\tau_P(X)<\infty\), faithfulness of \(\tau_Q\) forces the infinite part of \(S(X)\) to vanish. Its finite spectral projections \(q_j=1_{[0,j]}(S(X))\) increase strongly to one. Bimodularity makes \(S(q_jXq_j)\) bounded, while \(q_jXq_j\to X\) ultraweakly. The finite \(\tau_P\)-cone is ultraweakly dense, so \(S\) is semifinite. Compressions are not claimed to increase.

Any other trace-preserving normal operator-valued weight satisfies (OE.9), by applying its scalar identity to \(y^{1/2}Xy^{1/2}\), and hence equals \(S\). For the traces constructed in OE-03, this uniqueness also gives
\[
S\theta_s^P=\theta_s^Q S.
\tag{OE.11}
\]
Indeed \(\theta_{-s}^Q S\theta_s^P\) has scalar composite \(\tau_P\), because its two scaling factors cancel. For \(x\in M_+\), every spectral projection of \(S(x)\) is therefore fixed. OE-02 gives \(S(x)\in\widehat N_+\). Define \(E=S|_{M_+}\). It is normal and \(N\)-bimodular.

## Orbit integration and the equality at infinity

The shared group \(\lambda(t)\in Q\subset P\) has the same generator \(h\) in both algebras. Equations (OE.7), PT-04, and fixed-reference injectivity identify the entire scalar weights as \(W_P=(\tau_P)_h\), \(W_Q=(\tau_Q)_h\). For \(h_j=h\wedge j\in Q_+\), write \(C_j(Z)=h_j^{1/2}Zh_j^{1/2}\). The extended density identity, traciality, bimodularity, and (OE.10) give
\[
\begin{aligned}
\widehat W_Q(S(X))
&=\sup_j\widehat\tau_Q(C_j(S(X)))\\
&=\sup_j\tau_P(C_j(X))\\
&=W_P(X),\qquad X\in P_+.
\end{aligned}
\tag{OE.12}
\]
One may use \(h\wedge j\) here: for a bounded positive \(Z\), cyclicity moves it to the two outside factors and leaves the increasing middle density. For an extended positive \(Z\), bounded spectral cutoffs and two increasing suprema give the same formula. The sandwiches themselves need not increase as operators. All displayed scalar equalities include infinity.

**Positive integration against an unbounded normal weight.** We prove the precise interchange needed on the semifinite algebra \(P\). Let \(q\) be any normal weight on a von Neumann algebra \(A\) with a faithful normal semifinite trace \(\tau\), and let \(\alpha_s\) be a normal automorphism action with norm-continuous predual orbits. Let
\(B_KZ=\int_K\alpha_s(Z)\,ds\) for a compact interval \(K\). We claim
\[
q(B_KZ)=\int_K q(\alpha_s Z)\,ds
\quad(Z\in A_+).
\]
The trace correspondence of OE-04 writes \(q(Z)=\langle H,Z\rangle_\tau\) with \(H\in\widehat A_+\). Let \(H_n\uparrow H\) be bounded spectral cutoffs. Choose an increasing net \(e_i\uparrow1\) of positive contractions with \(\tau(e_i)<\infty\), supplied by finite-weight cutoffs. For each fixed \(n\), the normal positive functionals
\[
\rho_{n,i}(Z)
=\tau(e_i^{1/2}H_n^{1/2}ZH_n^{1/2}e_i^{1/2})
\]
are bounded, since \(\rho_{n,i}(1)\leq\|H_n\|\tau(e_i)\). Moving factors by traciality shows that their densities are \(H_n^{1/2}e_iH_n^{1/2}\uparrow H_n\). Therefore
\[
\rho_{n,i}(Z)\uparrow q_n(Z),
\qquad q_n(Z)=\langle H_n,Z\rangle_\tau,
\qquad q_n(Z)\uparrow q(Z).
\]

We justify the net interchange rather than applying a sequential convergence theorem to an arbitrary net. If a directed increasing family \(f_i\geq0\) of continuous functions on a compact interval has supremum \(f\), each set \(\{f>a\}\), for rational \(a\), is the union of the open sets \(\{f_i>a\}\). A countable base of the interval selects a countable subcover of each such union. Collect these indices for all rational \(a\), and successively choose upper bounds in the original directed set. The resulting increasing sequence has pointwise supremum \(f\). Ordinary monotone convergence now gives
\(\int f=\sup_i\int f_i\), including infinite values. This is a sequence of scalar tests for the fixed integrand, not a countable exhaustion of the algebra or its trace.

Apply this fact to \(f_i(s)=\rho_{n,i}(\alpha_sZ)\), then apply sequential monotone convergence to \(q_n\). Bounded-functional integration gives
\[
\begin{aligned}
q(B_KZ)
&=\sup_n\sup_i\int_K\rho_{n,i}(\alpha_sZ)\,ds\\
&=\int_K q(\alpha_sZ)\,ds.
\end{aligned}
\]
The scalar integrand is measurable by the same continuous-supremum construction. For \(Z\in\widehat A_+\), take its bounded spectral cutoffs \(Z_k\uparrow Z\). Normal extensions, followed by monotone convergence in \(k\) and in \(K=[-j,j]\), yield
\[
\widehat q\left(\int_{\mathbb R}\overline\alpha_s(Z)\,ds\right)
=\int_{\mathbb R}\widehat q(\overline\alpha_sZ)\,ds.
\]
The integral on the left is defined by these increasing compact averages. The same cutoff calculation shows that it is the normal extension of the bounded-input orbit integral. This proves the interchange at every extended positive input.

**The descent square.** Write bars for normal extensions to extended positive cones. For \(\omega\in Q_*^+\), the function \(q(Z)=S(Z)(\omega)\) is a normal weight on \(P\). Its normal extension is \(\widehat q(Z)=(\overline S Z)(\omega)\), by uniqueness of scalar extension. The interchange just proved, with \(A=P\) and \(\alpha=\theta^P\), and equivariance (OE.11) show
\[
\begin{gathered}
\overline S\,\overline T_P
=\overline T_Q\,\overline S
\quad\text{on }\widehat P_+.
\end{gathered}
\tag{OE.13}
\]
Indeed evaluation of either side at \(\omega\) is the integral of
\((\overline\theta_s^Q\overline S Z)(\omega)\).
Such evaluations separate \(\widehat Q_+\). In (OE.13), fixed-point spectral pairs embed \(\widehat M_+\) in \(\widehat P_+\) and \(\widehat N_+\) in \(\widehat Q_+\).

The full-range theorem gives
\(\overline T_P(\widehat P_+)=\widehat M_+\).
Choose any \(y\in M_+\) and a lift \(Z\in\widehat P_+\) with \(\overline T_P Z=y\). By normal extension of (OE.12), the square, and the scalar composite identities,
\[
\begin{aligned}
\psi(y)&=\widehat W_P(Z)\\
&=\widehat W_Q(\overline S Z)\\
&=\widehat\varphi(\overline T_Q\overline S Z)\\
&=\widehat\varphi(E(y)).
\end{aligned}
\tag{OE.14}
\]
For example, \(\widehat W_P=\widehat\psi\circ\overline T_P\) follows because both sides preserve increasing suprema and agree on bounded positives. No subtraction of infinite numbers occurs. In particular the lift argument proves (OE.14) when \(\psi(y)=\infty\).

## Faithfulness, semifiniteness, and uniqueness

Equation (OE.14) makes \(E\) faithful. If \(\psi(y)<\infty\), faithfulness of \(\varphi\) forces the infinite spectral projection of \(E(y)\) to vanish. Its finite spectral cuts \(q_j=1_{[0,j]}(E(y))\) increase strongly to one. Thus \(E(q_jyq_j)=q_jE(y)q_j\) is bounded, and \(q_jyq_j\to y\) ultraweakly. The finite \(\psi\)-cone is itself ultraweakly dense: for finite-weight positive contractions \(e_i\uparrow1\),
\[
\psi(e_iye_i)\leq\|y\|\psi(e_i^2)<\infty,
\qquad e_iye_i\longrightarrow y.
\]
Hence the bounded-output cone of \(E\) is ultraweakly dense, proving semifiniteness.

If \(E_1,E_2\) satisfy (OE.2), bimodularity gives
\[
\begin{aligned}
\widehat\varphi(c^*E_1(y)c)
&=\psi(c^*yc)\\
&=\widehat\varphi(c^*E_2(y)c)
\end{aligned}
\tag{OE.15}
\]
for \(c\in\mathfrak n_\varphi\), \(y\in M_+\), including infinite values. These are the extended quadratic forms on \(\Lambda_\varphi(\mathfrak n_\varphi)\) used in the all-positive uniqueness theorem. Its spectral-core argument applies: the dense left \(N\)-module is invariant under the finite spectral cuts of either form, so its finite-energy part is a core in the corresponding form norm. Equality in (OE.15) gives equality on the common finite domain in that module, and closedness gives equality of the full forms. Thus \(E_1(y)=E_2(y)\).

Conversely, start with an existing faithful normal semifinite \(E\). OVW-04 makes \(\psi=\widehat\varphi\circ E\) faithful normal semifinite, and OR-03 gives its modular restriction (OE.1). This completes both directions of OE-01.

## Why the whole positive cone matters

Three steps prevent a loss of infinite values. The trace representation in OE-04 includes normal weights whose finite-domain projection is smaller than one. The integration argument in OE-05 tests unbounded normal weights by bounded functionals before passing to increasing limits. Finally, the full-range theorem lifts every positive target through the extended average; density of the finite-output ideal alone would not supply that lift.

The scalar example \(\mathbb C1\subset B(\ell^2)\) in OE-04 shows why the semifinite-density assertion of PT-08 alone would be insufficient. CW-11 supplies its necessary extension. Likewise, equality checked only on a finite GNS ideal cannot replace (OE.14). The false all-positive reverse implication associated with IX.4.20 is corrected in Countable modular weight identities; it is not used here.

The theorem corresponds to Takesaki, *Theory of Operator Algebras II*, IX.4, Theorem 4.18. The trace and crossed-product construction is developed in U. Haagerup, [*Operator Valued Weights in von Neumann Algebras I*](https://www.isibang.ac.in/~soumyashant/misc/collected-works-of-haagerup/1970s/1979_Operator_valued_weights_in_von_Neumann_algebras_I.pdf), Theorems 1.12, 2.7 and 4.7, and [*II*](https://www.isibang.ac.in/~soumyashant/misc/collected-works-of-haagerup/1970s/1979_Operator_valued_weights_in_von_Neumann_algebras_II.pdf), Lemma 5.2 and Theorem 5.1. The proofs above give the required steps through the linked course results and the two local harmonic and integration arguments.
