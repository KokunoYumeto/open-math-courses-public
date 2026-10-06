# Positive vectors from a faithful state

*Original AI-authored pedagogical exposition by the OA-MOD course project; CC0-1.0. The proofs use the precise earlier results stated below.*

A faithful normal state supplies a cyclic separating vector. Starting from that vector, we construct a cone in which every bounded normal positive functional has exactly one representative. The construction uses the faithful-state modular theorem and a two-by-two matrix algebra. No theorem about an unbounded weight is used in this argument. The general-weight construction and its additional obligations remain in OA-MOD-SF and OA-MOD-WH.

The principal freely accessible historical source is Uffe Haagerup, *The standard form of von Neumann algebras*, Math. Scand. 37 (1975), 271–283, especially Theorem 1.1, Lemmas 1.3–1.5 and 2.10. Its proof of the cone theorem uses an earlier dual-cone result; its bounded-functional theorem cites the state case. We supply both arguments here at the stated faithful-state scope, including the relevant domain and comparison proofs. Existing original arguments in OA-MOD-SF are retained and specialized with their assumptions checked explicitly.

## Inputs and the exact scope

Let \(M\) be a nonzero von Neumann algebra with a faithful normal state \(\varphi\). Work in its faithful normal GNS representation on \(H\), with cyclic separating unit vector \(\xi\). We suppress the representation symbol. Inner products are linear in the first variable. The faithful-state theorem OA-MOD-FS supplies

\[
 S=\overline{S_0},\quad S_0(x\xi)=x^*\xi,\qquad
 F=S^*=\overline{F_0},\quad F_0(x'\xi)=x'^*\xi,
\]

\[
 S=J\Delta^{1/2},\quad F=J\Delta^{-1/2},\quad
 JMJ=M',\quad J\xi=\xi,\quad\Delta\xi=\xi,
 \qquad\sigma_t(x)=\Delta^{it}x\Delta^{-it}\in M.
 \tag{FSN.1}
\]

Here \(x\in M\), \(x'\in M'\), and all equalities of unbounded operators include their domains. No separability of \(H\) or of the predual is assumed. The sequence of approximants used for a single vector is not a countable basis.

The earlier Hilbert-space proofs supply orthogonal projections and the Riesz theorem. QF-03–04 supplies representation and unitary covariance of a densely defined closed nonnegative form. BK-07 supplies polar decomposition of a bounded map between different Hilbert spaces. SK-05–09 supplies the spectral calculus, including half-power domains, spectral cutoffs and dominated convergence. MA-02–03 and MA-16 supply vectorwise strong Gaussian integration and its spectral transform. The retained scalar contracts **MA-DEP-SCALAR-COMPLEX** and **MA-DEP-SCALAR-INTEGRATION** supply the scalar identity theorem and dominated differentiation used in the analytic-element argument. CP supplies the concrete predual, bounded positive functionals, their norm \(\omega(1)\), and normality of vector functionals. None of these prerequisites is the natural-cone conclusion being proved here.

For \(C\subset H\), use the complex Hilbert-space dual cone

\[
 C^\vee=\{v\in H:\langle u,v\rangle\text{ is real and nonnegative for every }u\in C\}.
 \tag{FSN.2}
\]

The real-part dual in all of \(H\) is a different object. All closures below are norm closures.

## Positive symmetric operators have affiliated positive extensions

Let \(T\) be a densely defined nonnegative symmetric operator. Complete \(D(T)\) in the inner product

\[
 \langle u,v\rangle_V=\langle u,v\rangle+\langle Tu,v\rangle.
\]

The inclusion into \(H\) extends to a contraction \(j:V\to H\). This map is injective: if \(u_n\to w\) in \(V\) and \(u_n\to0\) in \(H\), then, for every \(v\in D(T)\),

\[
 \langle u_n,v\rangle_V=\langle u_n,(1+T)v\rangle\longrightarrow0.
\]

Density of \(D(T)\) in \(V\) gives \(w=0\). Thus the completed form is a densely defined closed nonnegative form on the actual subspace \(j(V)\subset H\). QF-03 represents it by a positive self-adjoint operator \(h\). For \(u\in D(T)\), continuity in the form norm gives
\(\bar q(u,v)=\langle Tu,v\rangle\) for every \(v\in D(\bar q)\). The operator-domain part of that theorem implies \(h\supset T\).

If \(T\) is affiliated with \(M\), each unitary of \(M'\) preserves its domain and form, and so acts isometrically on the form completion. The extended action agrees with its action on \(H\). QF-04 therefore gives \(uhu^*=h\); equivalently, all spectral projections of \(h\) belong to \(M\). This proves the required affiliation without assuming that the original positive symmetric operator is self-adjoint.

## Duality of the two positive multiplication cones

Set

\[
 C_l=\overline{M_+\xi},\qquad C_r=\overline{M'_+\xi}.
 \tag{FSN.3}
\]

These are closed convex cones. We prove

\[
 C_l=C_r^\vee,\qquad C_r=C_l^\vee.
 \tag{FSN.4}
\]

For positive \(a\in M\), \(b\in M'\), their square roots commute, and
\(\langle a\xi,b\xi\rangle=\|a^{1/2}b^{1/2}\xi\|^2\ge0\). Thus \(C_l\subset C_r^\vee\).

Take \(\eta\in C_r^\vee\). The linear functional
\(f(x')=\langle x'\xi,\eta\rangle\) on \(M'\) is positive, hence satisfies \(f(x'^*)=\overline{f(x')}\). Consequently

\[
 \langle F_0x'\xi,\eta\rangle=\langle\eta,x'\xi\rangle.
\]

The right side is bounded by \(\|\eta\|\|x'\xi\|\). The conjugate-linear adjoint criterion gives \(\eta\in D(F_0^*)=D(S)\) and \(S\eta=\eta\).

On the dense subspace \(M'\xi\), define

\[
 T_0(x'\xi)=x'\eta.
\]

It is well defined because \(\xi\) is separating for \(M'\). For \(x',y'\in M'\), positivity and the Hermitian identity for \(f\) give

\[
 \langle x'\eta,y'\xi\rangle
 =\langle\eta,x'^*y'\xi\rangle
 =\langle y'^*x'\xi,\eta\rangle
 =\langle x'\xi,y'\eta\rangle,
\]

\[
 \langle T_0x'\xi,x'\xi\rangle
 =\langle\eta,x'^*x'\xi\rangle\ge0.
\]

Thus \(T_0\) is positive symmetric and closable. Its domain is invariant under every unitary \(u'\in M'\), and \(T_0u'=u'T_0\) there; the inverse unitary gives equality of the domains. Passing to its graph closure \(T\) proves affiliation with \(M\). Apply FSN-02 to obtain an affiliated positive self-adjoint extension \(h\). Since \(\xi\in D(T_0)\), we have \(h\xi=\eta\). The operators
\(h_n=h1_{[0,n]}(h)\) are bounded positive elements of \(M\), and spectral convergence on \(D(h)\) gives \(h_n\xi\to\eta\). Hence \(\eta\in C_l\), proving the first equality in (FSN.4). The same argument for \(M'\) proves the second; its required adjoint-core identity is \(S_0^*=F\), already in (FSN.1).

Closedness of \(S\) gives \(S\theta=\theta\) for \(\theta\in C_l\), because it fixes every positive multiple \(a\xi\). Similarly \(F\) fixes \(C_r\). Since \(J\xi=\xi\) and \(JMJ=M'\),

\[
 JC_l=C_r,\qquad \Delta^{1/2}C_l=C_r.
 \tag{FSN.5}
\]

Both assertions include surjectivity of the indicated map on these cones. The complex linear spans of \(C_l,C_r\) are dense, because positive elements linearly span each algebra and \(\xi\) is cyclic for both. In particular both cones are pointed.

## Analytic vectors with bounded multiplication

For \(r>0\), let \(g_r(t)=\sqrt{r/\pi}e^{-rt^2}\). If \(a\in M\), define

\[
 a_r(z)=\int_{\mathbb R}g_r(t-z)\sigma_t(a)\,dt\qquad(z\in\mathbb C).
 \tag{FSN.6}
\]

These are vectorwise strong integrals. The bound
\(\int|g_r(t-z)|dt=e^{r(\operatorname{Im}z)^2}\) gives bounded operators in \(M\); finite Riemann sums and strong closedness justify membership. Difference quotients converge in operator norm because the scalar kernels do so in \(L^1\), locally uniformly in \(z\). Thus \(a_r(z)\) is norm entire. For real \(s\), change of variable gives \(a_r(s)=\sigma_s(a_r(0))\). Also

\[
 \|a_r(0)\|\le\|a\|,\qquad a_r(0)\longrightarrow a\text{ strongly* as }r\to\infty.
 \tag{FSN.7}
\]

The last assertion follows by the Gaussian approximate-identity estimate separately on each vector for \(a\) and \(a^*\).

Let \(\mathcal E\) be the unital star algebra generated by these Gaussian elements and all their complex translates. It consists of norm-entire elements for \(\sigma\). The multiplication law and the relation \(\sigma_z(a)^*=\sigma_{\bar z}(a^*)\) follow by analytic continuation of their real identities, tested against bounded functionals. It is invariant under all complex translates.

For completeness the vector-domain implication used below follows directly from spectral bands. If \(a\in\mathcal E\), the entire vector function \(f(z)=\sigma_z(a)\xi\) agrees with \(\Delta^{it}a\xi\) on the real axis. Put \(E_n=1_{[1/n,n]}(\Delta)\). The two entire \(E_nH\)-valued functions \(E_nf(z)\) and \(\Delta^{iz}E_na\xi\) agree for real \(z\), hence everywhere. For real \(s\),
\(\Delta^s E_na\xi=E_nf(-is)\) has squared norms bounded by \(\|f(-is)\|^2\). Monotone convergence of its spectral integrals yields

\[
 a\xi\in D(\Delta^s),\qquad
 \Delta^s a\xi=\sigma_{-is}(a)\xi.
 \tag{FSN.8}
\]

This establishes the actual domain, not merely a formal analytic continuation.

## The self-dual cone and the standard-form axioms

Define

\[
 P=\overline{\{aJaJ\xi:a\in M\}}.
 \tag{FSN.9}
\]

Bounded strong* approximation in (FSN.7) shows that \(a\) may equivalently range over \(\mathcal E\). For \(a\in\mathcal E\), put \(b=\sigma_{-i/4}(a)\). By (FSN.1) and (FSN.8),

\[
 \Delta^{1/4}aa^*\xi
 =\sigma_{-i/4}(a)\sigma_{-i/4}(a^*)\xi
 =bJb\xi=bJbJ\xi.
 \tag{FSN.10}
\]

Indeed \(Jb\xi=\Delta^{1/2}b^*\xi=\sigma_{-i/2}(b^*)\xi\). The map \(a\mapsto\sigma_{-i/4}(a)\) is a bijection of \(\mathcal E\).

The analytic vectors \(aa^*\xi\) are dense in \(C_l\): write a positive element as a square and apply (FSN.7) to its square root. If \(\theta_n,\theta\in C_l\) and \(\theta_n\to\theta\), then (FSN.5) gives \(\Delta^{1/2}(\theta_n-\theta)=J(\theta_n-\theta)\to0\), so spectral Cauchy–Schwarz gives

\[
 \|\Delta^{1/4}(\theta_n-\theta)\|^2
 \le\|\Delta^{1/2}(\theta_n-\theta)\|\|\theta_n-\theta\|\longrightarrow0.
\]

Consequently

\[
 P=\overline{\Delta^{1/4}C_l}
  =\overline{\Delta^{-1/4}C_r}.
 \tag{FSN.11}
\]

The second equality uses \(\Delta^{1/2}C_l=C_r\) and the exact spectral domains. These are closures of linear images of convex cones, so \(P\) is a closed convex cone.

Directly on (FSN.9), commutation of \(M\) and \(JMJ\) gives \(Jv=v\) for \(v\in P\), and

\[
 xJxJ(aJaJ\xi)=(xa)J(xa)J\xi\in P\qquad(x,a\in M).
 \tag{FSN.12}
\]

Thus \(xJxJP\subset P\). Real modular powers preserve \(P\), because they fix \(\xi\), commute with \(J\) and conjugate \(a\) to \(\sigma_t(a)\).

For \(u\in C_l,v\in C_r\), spectral cutoffs followed by convergence in the displayed half-power domains prove
\(\langle\Delta^{1/4}u,\Delta^{-1/4}v\rangle=\langle u,v\rangle\ge0\). Hence \(P\subset P^\vee\). Conversely let \(w\in P^\vee\), and put

\[
 w_r=\int_{\mathbb R}g_r(t)\Delta^{it}w\,dt
     =\exp\bigl(- (\log\Delta)^2/(4r)\bigr)w.
\]

The positive kernel and modular invariance give \(w_r\in P^\vee\). The Gaussian spectral multiplier puts \(w_r\) in every real-power domain, and \(w_r\to w\). For every \(v\in C_r\), spectral pairing and (FSN.11) give

\[
 \langle\Delta^{-1/4}w_r,v\rangle
 =\langle w_r,\Delta^{-1/4}v\rangle\ge0.
\]

By (FSN.4), \(\Delta^{-1/4}w_r\in C_l\), and thus \(w_r\in P\). Closedness gives \(w\in P\). We have proved \(P=P^\vee\).

Finally, if \(z=z^*\in Z(M)\), then \(Sz=zS\) on \(D(S)\): first check this on \(M\xi\), then pass to its graph closure. The same argument on \(M'\xi\) gives \(Fz=zF\). Thus \(z\) preserves \(D(\Delta)=D(FS)\), and \(\Delta z=z\Delta\) there. It follows that \(z\) commutes with \((1+\Delta)^{-1}\), hence with all spectral projections of \(\Delta\) and its half power on the actual domain. Now \(S=J\Delta^{1/2}\) gives \(Jz=zJ\) on the dense range of \(\Delta^{1/2}\); boundedness extends it to \(H\). Splitting an arbitrary central element into real and imaginary self-adjoint parts proves

\[
 JzJ=z^*\quad(z\in Z(M)).
\]

Together with (FSN.1), pointwise fixedness, self-duality and (FSN.12), these are all four standard-form axioms. The real and imaginary parts of any vector lie in the real space \(H_J=\{v:Jv=v\}\); the next section proves that \(P\) spans this space over \(\mathbb R\).

## Geometry controls the represented functionals

The real Hilbert space \(H_J\) has its inherited real inner product. For a vector \(v\in H_J\), choose a sequence in \(P\) whose distances to \(v\) decrease to the infimum. Convexity and the parallelogram identity make this a Cauchy sequence, so there is a closest vector \(a\in P\). The same identity proves uniqueness. Differentiating squared distance along the segments to \(0\) and \(2a\), and along \(a+t u\) for \(u\in P,t\ge0\), gives

\[
 \langle v-a,a\rangle=0,\qquad
 \langle a-v,u\rangle\ge0\quad(u\in P).
\]

Since \(a-v\in H_J\), these are real pairings. Self-duality gives \(b=a-v\in P\). We have proved

\[
 v=a-b,\qquad a,b\in P,\qquad\langle a,b\rangle=0.
 \tag{FSN.13}
\]

Conversely such an \(a\) minimizes the distance: for \(u\in P\),
\(\|v-u\|^2=\|b\|^2+\|a-u\|^2+2\langle b,u\rangle\ge\|b\|^2\).
Thus this decomposition is unique. In particular \(P\) spans \(H_J\) over \(\mathbb R\), and spans \(H\) over \(\mathbb C\).

For \(u\in P\), let \(p_u\in M\) be the projection onto \(\overline{M'u}\); its conjugate \(Jp_uJ\) projects onto \(\overline{Mu}\). These projections exist in the indicated commutants because their closed subspaces reduce the corresponding star algebra.

If \(a,b\in P\) are orthogonal, then for every \(x\in M,t\in\mathbb C\), invariance and self-duality give

\[
 0\le\langle(1+t x)J(1+t x)J a,b\rangle
 =2\operatorname{Re}\bigl(t\langle xa,b\rangle\bigr)
   +|t|^2\langle xJxJa,b\rangle.
\]

Arbitrarily small \(t\) of arbitrary phase imply \(\langle xa,b\rangle=0\). Replacing \(x\) by \(y^*x\) proves \(Ma\perp Mb\); conjugating their projections by \(J\) yields

\[
 p_a p_b=0.
 \tag{FSN.14}
\]

The converse is immediate because \(p_a a=a,p_b b=b\).

Write \(\omega_u(x)=\langle xu,u\rangle\). For \(u,v\in P\),

\[
 \|u-v\|^2\le\|\omega_u-\omega_v\|
 \le(\|u\|+\|v\|)\|u-v\|.
 \tag{FSN.15}
\]

To prove the lower bound, decompose \(u-v=a-b\) by (FSN.13), and take the self-adjoint contraction \(d=p_a-p_b\). Using (FSN.14),

\[
 (\omega_u-\omega_v)(d)
 =\|a\|^2-\|b\|^2+2\langle v,a+b\rangle.
\]

All cone pairings are nonnegative, and
\(0\le\langle u,b\rangle=\langle v,b\rangle-\|b\|^2\). The expression is therefore at least \(\|a\|^2+\|b\|^2=\|u-v\|^2\), and the functional norm bounds it above. This also covers \(a=0\), \(b=0\), or both. The upper bound follows from

\[
 (\omega_u-\omega_v)(x)
 =\langle x(u-v),u\rangle+\langle xv,u-v\rangle
\]

and Cauchy–Schwarz, for every \(\|x\|\le1\). Thus a positive normal functional has at most one representative in \(P\). This is proved before asserting that every such functional has one.

## Comparing two faithful states by four closed graphs

Let \(\varphi_1,\varphi_2\) be faithful normal states of the same algebra, with triples \((H_j,\xi_j,J_j)\) and cones \(P_j\) as constructed above. On \(N=M_2(M)\), the functional

\[
 \Phi(X)=\tfrac12\bigl(\varphi_1(X_{11})+\varphi_2(X_{22})\bigr)
 \tag{FSN.16}
\]

is a faithful normal state. Normality follows from its bounded diagonal compressions. If a positive \(X=Y^*Y\) has \(\Phi(X)=0\), faithfulness applied to its two diagonal sums gives \(Y_{ij}=0\) for all four entries. Thus \(X=0\).

Its GNS Hilbert space is the direct sum of four slots \(H_{ij}=H_j\): the vector for \(X\) has components \(2^{-1/2}X_{ij}\xi_j\). Left multiplication acts by the usual row matrix operations. In particular every slot is densely filled by single-entry matrices. The initial Tomita operator exchanges slots \((i,j)\) and \((j,i)\), acting on their vector cores by

\[
 T_{ij,0}(x\xi_j)=x^*\xi_i.
 \tag{FSN.17}
\]

The common factor \(2^{-1/2}\) cancels in this formula.

The slot projections preserve the initial graph, with the stated exchange. Applying them to convergent graph sequences proves that the closed Tomita operator has slot restrictions exactly \(T_{ij}=\overline{T_{ij,0}}\). Thus these operators have dense domains; the closed involution identity gives \(T_{ji}=T_{ij}^{-1}\), including domains and ranges. Their kernels are zero and their ranges are dense. The squared graph form is an orthogonal sum of the four slot forms. Hence \(\Delta_\Phi\) reduces the slots, and its restriction \(D_{ij}\) has half-power domain \(D(T_{ij})\). Its polar conjugation exchanges them by antiunitaries

\[
 T_{ij}=K_{ij}D_{ij}^{1/2},\qquad
 K_{ij}:H_j\longrightarrow H_i,\qquad K_{ji}=K_{ij}^{-1}.
 \tag{FSN.18}
\]

On the diagonal \(K_{jj}=J_j\). These conclusions are restrictions of the faithful-state Tomita construction on \(N\); they assume no theorem about relative modular operators.

By FS applied to \(\Phi\), \(Q=J_\Phi e_{12}J_\Phi\) commutes with \(N\). Starting in slot \((i,2)\), its three factors visit \((2,i)\), then \((1,i)\), then \((i,1)\). Thus its coefficient in row \(i\) is \(K_{1i}K_{i2}\). Commutation with \(e_{21}\) makes the two row coefficients equal; commutation with \(\operatorname{diag}(x,x)\) makes this coefficient intertwine the two representations. Therefore

\[
 U=J_1K_{12}=K_{12}J_2:H_2\longrightarrow H_1,
 \qquad Ux=xU,\qquad UJ_2=J_1U.
 \tag{FSN.19}
\]

The notation \(Ux=xU\) uses the appropriate representation of \(x\) on each side. The map \(U\) is unitary, as a product of two antiunitaries.

We check that \(UP_2=P_1\), rather than inferring this from intertwining. Put \(g_j(x)=xJ_jx\xi_j\), so the closures of these generators are \(P_j\). Products \(y^*x\) and \(x^*y\) belong to \(M\), and hence to the exact core domains in (FSN.17). Pointwise \(J_j\)-fixedness of the generators, commutation of the two algebras and (FSN.19) give the full pairing computation

\[
\begin{aligned}
 \langle g_1(x),Ug_2(y)\rangle
 &=\langle J_1x\xi_1,Ux^*J_2yJ_2y\xi_2\rangle\\
 &=\langle J_1x\xi_1,J_1UyJ_2(x^*y\xi_2)\rangle\\
 &=\langle UyJ_2(x^*y\xi_2),x\xi_1\rangle\\
 &=\langle K_{12}(x^*y\xi_2),y^*x\xi_1\rangle\\
 &=\langle D_{21}^{1/2}(y^*x\xi_1),y^*x\xi_1\rangle\ge0.
\end{aligned}
 \tag{FSN.20}
\]

For the last equality, use \(T_{21}(y^*x\xi_1)=x^*y\xi_2\) and \(K_{12}=K_{21}^{-1}\). The positive operator acts on \(H_1\), and its argument is in its half-power domain. Thus self-duality gives \(UP_2\subseteq P_1\). Interchanging the states gives the reverse inclusion, since its unitary is \(U^*=K_{21}J_1=J_2K_{21}\).

This cone-preserving intertwiner is unique. Indeed, two such maps send each \(v\in P_2\) to vectors in \(P_1\) representing the same functional. Inequality (FSN.15) makes those vectors equal; complex spanning gives equality of the maps. We denote it \(I_{1\leftarrow2}\). Uniqueness proves composition, identity and inverse laws for comparisons of any three faithful states.

## Every bounded normal positive functional has a vector

Fix the original faithful state \(\varphi\). For \(\omega\in M_*^+\) and \(\varepsilon>0\), set

\[
 \rho_\varepsilon=\omega+\varepsilon\varphi,\qquad
 c_\varepsilon=\rho_\varepsilon(1)>0,
 \qquad\psi_\varepsilon=c_\varepsilon^{-1}\rho_\varepsilon.
\]

Then \(\psi_\varepsilon\) is a faithful normal state. Its cyclic vector belongs to its cone: it is the generator corresponding to \(a=1\). By FSN-07,

\[
 v_\varepsilon=\sqrt{c_\varepsilon}\,
 I_{\varphi\leftarrow\psi_\varepsilon}\xi_{\psi_\varepsilon}\in P
\]

represents \(\rho_\varepsilon\). For \(\varepsilon,\delta>0\), (FSN.15) gives

\[
 \|v_\varepsilon-v_\delta\|^2
 \le\|\rho_\varepsilon-\rho_\delta\|
 =|\varepsilon-\delta|.
 \tag{FSN.21}
\]

Take \(\varepsilon=1/n\). Closedness of \(P\) gives a limit \(v_\omega\in P\). The upper bound in (FSN.15), or the vector-functional estimate used to prove it, shows that this vector represents \(\omega\), because \(\rho_{1/n}\to\omega\) in predual norm. Uniqueness is again the lower bound. The choice of sequence and all comparison choices disappear by uniqueness. For \(\omega=0\) this gives \(v_0=0\).

The map \(P\to M_*^+\) is consequently a homeomorphism for the Hilbert norm and the predual norm, with

\[
 \|v_\omega-v_\nu\|\le\|\omega-\nu\|^{1/2},\qquad
 \|v_\omega\|^2=\omega(1),\qquad
 v_{c\omega}=\sqrt c\,v_\omega\quad(c\ge0).
 \tag{FSN.22}
\]

This construction used faithful bounded states on \(M\) and \(M_2(M)\) only. In particular, it did not select an unbounded weight on the complement of the support of \(\omega\).

## Supports and monotone functional nets

For a vector \(v\in P\), the projection \(p_v\) of FSN-06 is exactly the support of \(\omega_v\). It fixes \(v\). If a projection \(e\in M\) satisfies \(\omega_v(1-e)=0\), then \((1-e)v=0\); since \(e\) commutes with \(M'\), its range contains \(\overline{M'v}\), so \(p_v\le e\). This is the least-support characterization, including \(v=0\). Also \(Jp_vJ\) projects onto \(\overline{Mv}\). Hence (FSN.14) gives

\[
 s(\omega)s(\nu)=0\quad\Longleftrightarrow\quad
 \langle v_\omega,v_\nu\rangle=0.
 \tag{FSN.23}
\]

Faithfulness of \(\omega\) is equivalent to \(p_{v_\omega}=1\); its representative is then both cyclic and separating. The converse follows from its support.

If \((\omega_i)\) is any increasing net of normal positive functionals whose pointwise supremum is a bounded normal positive functional \(\omega\), then

\[
 \|\omega-\omega_i\|=(\omega-\omega_i)(1)\longrightarrow0,
 \qquad v_{\omega_i}\longrightarrow v_\omega.
\]

The corresponding conclusion holds for a decreasing net with a pointwise infimum \(\omega\in M_*^+\). Here the norm identities use positivity and evaluation at the identity; no sequential dominated convergence has been applied to an arbitrary net. A bounded limiting functional is required in the increasing case. An infinite-valued weight cannot be represented by a Hilbert-space vector, whose value at \(1\) is finite.

## Three computations that test the construction

**A nontracial matrix state.** Let \(M=M_d(\mathbb C)\), let \(D>0\) have \(\operatorname{Tr}D=1\), and put \(\varphi(x)=\operatorname{Tr}(Dx)\). Identify its GNS space with Hilbert–Schmidt matrices by \(x\xi\mapsto xD^{1/2}\). Then

\[
 J(X)=X^*,\qquad\Delta(X)=DXD^{-1},\qquad
 aJaJ\xi=aD^{1/2}a^*.
\]

Every generator is a positive matrix. Conversely, for \(B\ge0\), choose \(a=B^{1/2}D^{-1/4}\); then \(aD^{1/2}a^*=B\). Thus \(P\) is exactly the positive-matrix cone, although \(\varphi\) need not be tracial. The functional \(\omega_E(x)=\operatorname{Tr}(Ex)\), \(E\ge0\), has representative \(E^{1/2}\). These identities verify the quarter-power choice and the distinction between the cyclic vector \(D^{1/2}\) and the whole cone.

**Cone order does not imply functional order.** In \(M_2(\mathbb C)\), take

\[
 A=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
 B=\begin{pmatrix}2&1\\1&1\end{pmatrix}.
\]

Both are positive and \(B-A=\begin{pmatrix}1&1\\1&1\end{pmatrix}\ge0\), so \(A\le B\) in the cone. But their represented functionals have density difference

\[
 B^2-A^2=\begin{pmatrix}4&3\\3&2\end{pmatrix},
\]

whose determinant is \(-1\). For \(w=(2,-3)^T\) and the positive rank-one projection \(e=ww^*/13\),
\((\omega_B-\omega_A)(e)=-2/13<0\). Therefore the vector-functional correspondence is not an order isomorphism. This does not contradict its norm homeomorphism or its preservation of orthogonal supports.

**The square-root exponent is optimal at zero.** For a state \(\varphi\) and \(\varepsilon>0\), uniqueness gives \(v_{\varepsilon\varphi}=\sqrt\varepsilon\,v_\varphi\). Consequently

\[
 \|v_{\varepsilon\varphi}-v_0\|=\sqrt\varepsilon,
 \qquad\|\varepsilon\varphi-0\|=\varepsilon.
\]

No uniform local Lipschitz estimate for the inverse map can hold at zero. The exponent \(1/2\) in (FSN.22) is attained.

The state assumption in this companion is explicit. Its conclusions are sufficient for arguments whose algebra carries a faithful normal state. Existence and comparison of standard forms for arbitrary algebras, and the construction from arbitrary normal semifinite faithful weights, retain their full separate proofs in SF and WH; this companion makes no reduction of that scope.
