# Conditional expectations from modular invariance

Course: OA-MOD. This lesson proves the modular criterion for a prescribed normal semifinite faithful weight. Its mathematical statements are relative to the explicit prerequisite results cited below.

An orthogonal projection of GNS spaces is easy to construct. The difficulty is to show that compression by that projection is again multiplication by an element of the smaller algebra, and that it preserves even the infinite values of a weight. We solve the first problem by comparing modular conjugations. For the second, we construct finite analytic cutoffs whose **right** multiplication operators are contractions. The same construction works when no faithful normal state exists.

## The criterion and its exact setting

Let \(M\) be a von Neumann algebra and let \(\varphi:M_+\to[0,\infty]\) be normal, semifinite and faithful. Let \(N\subseteq M\) be a von Neumann subalgebra with the **same identity**, and assume that

\[
\nu=\varphi|_{N_+}
\]

is semifinite. Normality and faithfulness of \(\nu\) follow by restriction. Throughout, a retraction is complex linear. A \(\varphi\)-preserving contractive retraction is a map \(F:M\to N\) such that

\[
F(n)=n\quad(n\in N),\qquad \|F(x)\|\leq\|x\|\quad(x\in M),
\qquad \nu(F(X))=\varphi(X)\quad(X\in M_+).
\tag{ME.1}
\]

The positive-cone equality is meaningful because CE-004 proves positivity from the first two conditions. It includes equality of infinite values; it is not a condition only on a finite definition algebra. We do not assume that \(F\) is normal.

**Modular expectation theorem.** Under these hypotheses, (ME.1) has a solution if and only if

\[
\sigma_t^\varphi(N)=N\qquad(t\in\mathbb R).
\tag{ME.2}
\]

The solution \(E\) is unique, normal, faithful and completely positive. For \(M\ne\{0\}\) it is unital and has norm one. Moreover,

\[
\sigma_t^\nu=\sigma_t^\varphi|_N,\qquad
E\sigma_t^\varphi=\sigma_t^\nu E.
\tag{ME.3}
\]

The proof below also identifies the GNS projection, the full closed Tomita maps and all modular power domains, and the full left, right and entire algebras of \(N\).

There is no countability, separability, finite-weight or faithful-state assumption. If \(M=\{0\}\), then \(N=\{0\}\), both GNS spaces are zero, the unique map has norm zero, and all assertions are interpreted on these zero spaces. The remaining proof concerns the nonzero case.

Our inputs are precise course results. WG-003–010 supplies finite ideals, GNS spaces, normality and finite positive contraction nets. WH-02 identifies faithful normal representation images and their intrinsic topologies; WH-09–12 supplies the full weight Hilbert algebra, its closed involution, its bounded-vector correspondence and the variational formula on the whole positive cone. MF-05–08 supplies the commutant theorem, modular covariance and finite analytic Gaussian vectors. KM-01, KM-02 and KM-05 supplies the weight KMS condition and its uniqueness; its proof does not use this expectation theorem. MA-08–09 supplies boundary uniqueness and the exact strip test for a spectral power domain; MA-16 supplies bounded-orbit Gaussian integrals. TC-03, TC-08–09 and SK-05, SK-07–08 supply closed antilinear adjoints, polar decompositions and reducing spectral restrictions. CE-004 and CE-006 supplies bimodularity, complete positivity and Schwarz for contractive retractions. NP-04 and NW-11 supplies the increasing-net criterion for normal maps and ultraweak lower semicontinuity of normal weights. Their proofs are not given here.

## The smaller GNS space detects the ambient algebra

Write \((H,\pi,\Lambda)\) for the \(\varphi\)-GNS triple, with inner products linear in the first variable. For a weight \(\omega\), use

\[
\mathfrak n_\omega=\{x:\omega(x^*x)<\infty\},\qquad
\mathfrak a_\omega=\mathfrak n_\omega\cap\mathfrak n_\omega^*.
\]

The first is a left ideal; the second is a *-algebra. In particular,

\[
\mathfrak n_\nu=N\cap\mathfrak n_\varphi,
\qquad \mathfrak a_\nu=N\cap\mathfrak a_\varphi.
\tag{ME.4}
\]

No intersection assertion about the larger linear definition algebras \(\mathfrak m_\omega\) is needed.

Let

\[
K=\overline{\Lambda(\mathfrak n_\nu)}\subseteq H,
\qquad P=P_K,
\qquad W\Lambda_\nu(a)=\Lambda(a).
\tag{ME.5}
\]

The equality of GNS pairings makes \(W:H_\nu\to K\) unitary. For \(n\in N\), both \(n\) and \(n^*\) preserve the left ideal \(\mathfrak n_\nu\), so \(K\) reduces \(\pi(n)\). Thus

\[
P\pi(n)=\pi(n)P,
\qquad \rho(n):=\pi(n)|_K=W\pi_\nu(n)W^*.
\tag{ME.6}
\]

The representation \(\rho\) is faithful and normal. Its image is a von Neumann algebra, and the inverse isomorphism on that image is normal and isometric, by WH-02.

WG-008, applied inside \(N\) to \(\nu\), gives a directed increasing net

\[
0\leq b_i\leq1,\qquad \nu(b_i)<\infty,\qquad b_i\longrightarrow1
\quad\hbox{strongly}.
\tag{ME.7}
\]

These need not be projections. Since \(b_i^2\leq b_i\), they belong to \(\mathfrak a_\nu\). Faithful normal representations preserve their increasing supremum, so the strong limit in (ME.7) holds in both representations above.

**Separation lemma.** If \(x\in M\) and \(\pi(x)P=0\), then \(x=0\).

Indeed, \(xb_i\in\mathfrak n_\varphi\) and

\[
\Lambda(xb_i)=\pi(x)\Lambda(b_i)=0.
\]

Faithfulness of \(\varphi\) gives \(xb_i=0\). Passing to the strong limit gives \(x=0\). Notice that a separating **subspace** suffices; we have not constructed or assumed a separating vector. Both restriction semifiniteness and the common identity enter this argument. \(\square\)

## Modular invariance gives the exact restricted domains

Assume (ME.2), and put \(\gamma_t=\sigma_t^\varphi|_N\). By MF-06 this group preserves \(\nu\). For elements of \(\mathfrak a_\nu\), the scalar strip function supplied by KM-02 for \(\varphi\) has precisely the KMS boundary values for \(\nu\) and \(\gamma\). All boundary products are products of elements of \(\mathfrak n_\nu\), hence lie in its finite definition algebra; the linear extensions of the two weights agree there by polarization of the GNS pairing. KM-05 therefore gives

\[
\gamma_t=\sigma_t^\nu.
\tag{ME.8}
\]

Thus the smaller modular group has been identified before any expectation or preservation assertion is used.

Let \(S_\varphi=J_\varphi\Delta_\varphi^{1/2}\) and \(S_\nu=J_\nu\Delta_\nu^{1/2}\) be the closed GNS Tomita maps. Their real modular unitaries act on finite vectors by the corresponding automorphisms. Equation (ME.8) and density imply

\[
\Delta_\varphi^{it}W=W\Delta_\nu^{it},\qquad
P\Delta_\varphi^{it}=\Delta_\varphi^{it}P.
\tag{ME.9}
\]

The second equality follows because the group and its inverses preserve \(K\).

We need the unbounded consequences of (ME.9). Fix \(a>0\). For \(\xi\in D(\Delta_\varphi^a)\), MA-09 gives its bounded, continuous vector continuation on the closed strip \(-a\leq\operatorname{Im}z\leq0\), holomorphic inside, with real boundary \(\Delta_\varphi^{it}\xi\) and lower boundary \(\Delta_\varphi^{it}\Delta_\varphi^a\xi\). Apply \(P\) to that function. Equation (ME.9) identifies the real boundary as the orbit of \(P\xi\); the converse part of MA-09 then proves

\[
P D(\Delta_\varphi^a)\subseteq D(\Delta_\varphi^a),\qquad
\Delta_\varphi^a P\xi=P\Delta_\varphi^a\xi.
\tag{ME.10}
\]

Use the upper strip for \(a<0\); the same argument gives (ME.10) with that exponent. There is no issue at \(a=0\). Replacing \(P\) by \(I-P\) proves reduction of every such domain.

Transporting the strip function for \(\Delta_\nu\) by \(W\) gives one direction of the domain comparison. For the other, take \(\xi\in K\cap D(\Delta_\varphi^a)\). The component of its strip function in \(K^\perp\) has zero real boundary by (ME.9), hence vanishes by MA-08. The function therefore takes values in \(K\), and \(W^*\) transports it to the smaller space. The converse part of MA-09 proves

\[
W D(\Delta_\nu^a)=K\cap D(\Delta_\varphi^a),\qquad
W\Delta_\nu^a W^*=\Delta_\varphi^a|_K
\quad(a\in\mathbb R).
\tag{ME.11}
\]

Each equality in (ME.11) includes its displayed domain. In particular it applies to both half powers and their inverses, with no bounded-inverse assumption.

On \(\Lambda_\nu(\mathfrak a_\nu)\), the two involutions agree under \(W\). Closing their graphs first gives
\(WS_\nu W^*\subseteq S_\varphi|_K\). This inclusion alone is insufficient. The domains of these operators are respectively \(W D(\Delta_\nu^{1/2})\) and \(K\cap D(\Delta_\varphi^{1/2})\), which are equal by (ME.11). Hence

\[
WS_\nu W^*=S_\varphi|_K,
\qquad WJ_\nu W^*=J_\varphi|_K=:J_K,
\qquad PJ_\varphi=J_\varphi P.
\tag{ME.12}
\]

For the second equality, compare the polar maps on the range of \(\Delta_\nu^{1/2}\), which is dense because \(\Delta_\nu\) is injective; extend by their isometry. This also proves that \(J_\varphi K=K\), and its antiunitarity gives the last equality. \(\square\)

## Compression produces a normal retraction

For \(x\in M\), consider the bounded operator

\[
C_x=P\pi(x)P|_K.
\tag{ME.13}
\]

We claim that \(C_x\in\rho(N)\). By MF-05 on the smaller GNS space,

\[
\rho(N)'=J_K\rho(N)J_K.
\]

For \(n\in N\), the ambient operator \(J_\varphi\pi(n)J_\varphi\) belongs to \(\pi(M)'\). It commutes with \(P\), by (ME.6) and (ME.12), and restricts to \(J_K\rho(n)J_K\) on \(K\). Consequently \(C_x\) commutes with every member of \(\rho(N)'\). The bicommutant identity gives the claim.

Define

\[
E(x)=\rho^{-1}(C_x),\qquad x\in M.
\tag{ME.14}
\]

This is a complex-linear contractive map, since compression is contractive and \(\rho\) is isometric. If \(n\in N\), (ME.6) gives \(C_n=\rho(n)\), so \(E(n)=n\). In particular \(E(1)=1\). The retraction theorem CE-004 and CE-006 now yields

\[
E(M_+)\subseteq N_+,\qquad E(x^*)=E(x)^*,
\qquad E(nxm)=nE(x)m,
\tag{ME.15}
\]

for \(n,m\in N\), and complete positivity and Schwarz:

\[
E(x)^*E(x)\leq E(x^*x).
\tag{ME.16}
\]

In particular \(\|E\|=1\).

Normality follows directly on nets. If \(0\leq X_j\uparrow X\), normality of \(\pi\) gives \(\pi(X_j)\uparrow\pi(X)\). Compression gives \(C_{X_j}\uparrow C_X\): the supremum follows by evaluating each quadratic form on a vector of \(K\). The inverse normal isomorphism \(\rho^{-1}\) then gives \(E(X_j)\uparrow E(X)\). NP-04 identifies this as normality.

There is also a useful faithful compression test. If \(X\geq0\) and \(E(X)=0\), then
\(\|\pi(X)^{1/2}k\|^2=\langle C_Xk,k\rangle=0\) for every \(k\in K\). Thus \(\pi(X^{1/2})P=0\), and ME-02 gives \(X=0\). Hence \(E\) is faithful before weight preservation has been proved. \(\square\)

## One weight inequality from right bounded vectors

Set \(\theta=\nu\circ E\). Additivity and positive homogeneity of \(\nu\), together with positivity and linearity of \(E\), make this a weight; normality of both maps proves its normality by increasing positive nets. For now no semifiniteness assertion about \(\theta\) is used.

Write \(\mathcal A_\omega=\Lambda_\omega(\mathfrak a_\omega)\) for the full left Hilbert algebra of an NSF weight, and \(\mathcal D_\omega=J_\omega\mathcal A_\omega\) for its full right Hilbert algebra. In the following formulas identify the smaller vectors with their images in \(K\) under \(W\). Every \(\eta\in\mathcal D_\nu\) can be written

\[
\eta=J_K\Lambda(b),\qquad b\in\mathfrak a_\nu.
\]

By (ME.12), this is also \(J_\varphi\Lambda(b)\), hence belongs to \(\mathcal D_\varphi\). MF-05–06 identifies its actual right multiplication operators as

\[
R^N_\eta=J_K\rho(b)J_K,\qquad
R^M_\eta=J_\varphi\pi(b)J_\varphi.
\tag{ME.17}
\]

Both norms equal \(\|b\|\), since the two representations are faithful and isometric. Thus a right contraction in the smaller full algebra is a right contraction in the ambient full algebra with exactly the same bound.

For \(X\in M_+\), the compression identity gives
\(\langle\rho(E(X))\eta,\eta\rangle=\langle\pi(X)\eta,\eta\rangle\) for \(\eta\in K\). Apply WH-12 in the two spaces to obtain

\[
\begin{aligned}
\theta(X)
&=\sup_{\substack{\eta\in\mathcal D_\nu\\\|R^N_\eta\|\leq1}}
       \langle\pi(X)\eta,\eta\rangle\\
&\leq\sup_{\substack{\eta\in\mathcal D_\varphi\\\|R^M_\eta\|\leq1}}
       \langle\pi(X)\eta,\eta\rangle
=\varphi(X).
\end{aligned}
\tag{ME.18}
\]

The suprema in WH-12 are valid for all positive elements. Thus (ME.18) includes \(\varphi(X)=\infty\) without making any finite-domain extension assumption. \(\square\)

## Analytic cutoffs with a right contraction

Retain the net \((b_i)\) from (ME.7) and fix a Gaussian width, say one. For \(z\in\mathbb C\), define

\[
c_i(z)=\frac1{\sqrt\pi}\int_{\mathbb R}e^{-(t-z)^2}\sigma_t^\varphi(b_i)\,dt,
\qquad c_i=c_i(0).
\tag{ME.19}
\]

The integral is interpreted in the faithful GNS representation, strongly on each vector. The absolute scalar kernel is integrable and the operator integrand is uniformly bounded. Finite Riemann sums and tails show that its value belongs to the strongly closed algebra \(\pi(N)\); (ME.19) denotes the corresponding element of \(N\). MA-16, or differentiation of this kernel in its \(L^1\) norm, shows operator-norm entireness and gives

\[
\|c_i(z)\|\leq e^{(\operatorname{Im}z)^2},\qquad
c_i(z)^*=c_i(\overline z),\qquad
\sigma_s^\varphi(c_i(z))=c_i(z+s)\quad(s\in\mathbb R).
\tag{ME.20}
\]

The translation formula follows by changing variables. Thus \(c_i(z)\) is the specified entire continuation of the orbit of \(c_i\). At \(z=0\), real averaging gives \(0\leq c_i\leq1\), and \(c_i\leq c_j\) when \(i\leq j\).

The finite-star assertion is a separate step. Apply MF-08 to the finite-star vector \(\Lambda(b_i)\). Its Gaussian vector belongs to the maximal entire algebra, and its left multiplier is \(\pi(c_i)\). Its complex translates have left multiplier \(\pi(c_i(z))\), by the vector/operator integral identity in that result. WH-11 identifies a left-bounded vector with its unique finite-ideal GNS element, and the finite-star part of the same result identifies the full left algebra. Consequently

\[
c_i(z)\in\mathfrak a_\nu,
\qquad \Lambda(c_i(z))=\Delta_\varphi^{iz}\Lambda(c_i)
\quad(z\in\mathbb C).
\tag{ME.21}
\]

In particular all powers and involutions required in (ME.21) have their actual finite-star domains. A bounded entire element of an algebra need not in general have finite weight; here finiteness comes from the Gaussian **vector** construction.

For every fixed \(z\), we have

\[
c_i(z)\longrightarrow1\quad\hbox{strongly*}.
\tag{ME.22}
\]

Here is the net argument. Fix a vector \(\xi\in H\) and \(T<\infty\). The set \(\{\Delta_\varphi^{-it}\xi:|t|\leq T\}\) is norm compact. Strong convergence of the uniformly bounded net \(\pi(b_i)\to I\) is uniform on this set: cover it by finitely many norm balls, choose a common upper index for their centers, and use the uniform norm bound on the errors. Hence

\[
\sup_{|t|\leq T}\|\pi(\sigma_t^\varphi(b_i)-1)\xi\|
=\sup_{|t|\leq T}\|(\pi(b_i)-I)\Delta_\varphi^{-it}\xi\|
\longrightarrow0.
\tag{ME.23}
\]

The complex Gaussian has integral \(\sqrt\pi\); this follows by shifting a finite rectangular contour and sending its vertical sides to infinity, where the Gaussian bounds kill them. In the integral for \((\pi(c_i(z))-I)\xi\), (ME.23) controls the compact interval. The tails are bounded, uniformly in \(i\), by \(2\|\xi\|\) times the integral of the absolute scalar kernel. First choose \(T\) for those tails, then an index for the compact interval. This proves strong convergence for every fixed \(z\). The adjoint identity in (ME.20) proves strong* convergence. It uses no dominated-convergence assertion for arbitrary nets. WH-02 also interprets these bounded convergences intrinsically as sigma-strong* convergences in \(N\) and \(M\).

Now put

\[
a_i=c_i(-i/2),\qquad \eta_i=\Lambda(a_i).
\tag{ME.24}
\]

Since \(c_i=c_i^*\), we have \(S_\varphi\Lambda(c_i)=\Lambda(c_i)\). The polar identity \(\Delta_\varphi^{1/2}=J_\varphi S_\varphi\) on its domain and (ME.21) give

\[
\eta_i=\Delta_\varphi^{1/2}\Lambda(c_i)
=J_\varphi\Lambda(c_i)\in K.
\tag{ME.25}
\]

Therefore the two actual right multiplication operators are

\[
R^M_{\eta_i}=J_\varphi\pi(c_i)J_\varphi,
\qquad R^N_{\eta_i}=J_K\rho(c_i)J_K,
\qquad 0\leq R^M_{\eta_i},R^N_{\eta_i}\leq I.
\tag{ME.26}
\]

They converge strongly to their respective identities, while

\[
a_i\longrightarrow1\quad\hbox{strongly*},\qquad
\|a_i\|\leq e^{1/4}.
\tag{ME.27}
\]

The shift is \(-i/2\) in the convention \(\Delta^{it}\Lambda(x)=\Lambda(\sigma_t(x))\). Its sign is fixed by (ME.25), not by an analogy with a tracial cutoff. \(\square\)

## Preservation on the entire positive cone

We prove the inequality opposite to (ME.18). Fix \(X\in M_+\). If \(\theta(X)=\infty\), then \(\varphi(X)\leq\theta(X)\) is automatic. Suppose therefore that \(Y=E(X)\) has \(\nu(Y)<\infty\). Its square root belongs to \(\mathfrak n_\nu\), while each \(a_i\) in (ME.24) belongs to \(\mathfrak a_\nu\). The left-ideal property makes \(X^{1/2}a_i\in\mathfrak n_\varphi\) and \(Y^{1/2}a_i\in\mathfrak n_\nu\). Since \(\eta_i=\Lambda(a_i)\in K\), compression gives

\[
\begin{aligned}
\varphi(a_i^*Xa_i)
&=\|\pi(X^{1/2})\eta_i\|^2
=\langle\pi(X)\eta_i,\eta_i\rangle\\
&=\langle\rho(Y)\eta_i,\eta_i\rangle
=\nu(a_i^*Ya_i)\\
&=\|R^N_{\eta_i}\,W\Lambda_\nu(Y^{1/2})\|^2
\leq\nu(Y)=\theta(X).
\end{aligned}
\tag{ME.28}
\]

The penultimate equality is the mixed bounded-vector identity of WH-04 and WH-11: right multiplication by \(\eta_i\) on the GNS vector of \(Y^{1/2}\) equals left multiplication by \(Y^{1/2}\) on \(\eta_i\). The bound uses the actual right contraction from (ME.26). It does not assert that \(\mathfrak n_\nu\) is a right ideal.

Equation (ME.27) implies \(a_i^*Xa_i\to X\) strongly on a uniformly bounded positive net. For example, in a faithful representation the difference is

\[
a_i^*X(a_i-I)+(a_i^*-I)X,
\]

whose value on each vector tends to zero by the uniform bound and strong* convergence. Such bounded strong convergence is ultraweak convergence. NW-11 gives lower semicontinuity of \(\varphi\) on the positive cone, and hence

\[
\varphi(X)\leq\liminf_i\varphi(a_i^*Xa_i)\leq\theta(X).
\tag{ME.29}
\]

Equivalently, all the terms lie in the ultraweakly closed sublevel set \(\{Z\in M_+:\varphi(Z)\leq\theta(X)\}\), so their limit lies there. This formulation also makes the arbitrary-net use explicit.

Combining (ME.29) with (ME.18) proves

\[
\boxed{\nu(E(X))=\varphi(X)\qquad(X\in M_+).}
\tag{ME.30}
\]

In particular \(\theta\) is now known to be semifinite and faithful because it equals \(\varphi\). The forward implication of the theorem has been proved, including all infinite values. \(\square\)

## A preserving retraction is determined by its GNS projection

The following argument makes no modular invariance or normality assumption about a proposed retraction. Let \(F:M\to N\) satisfy (ME.1), with \(K,P,W,\rho\) as in ME-02. CE-004 and CE-006 gives bimodularity, involution preservation and Schwarz. For \(x\in\mathfrak n_\varphi\),

\[
\nu(F(x)^*F(x))\leq\nu(F(x^*x))=\varphi(x^*x)<\infty.
\tag{ME.31}
\]

Thus \(F(x)\in\mathfrak n_\nu\), and

\[
\Lambda(x)\longmapsto W\Lambda_\nu(F(x))
\]

extends to a contraction \(Q:H\to K\). It is the identity on the dense subset \(\Lambda(\mathfrak n_\nu)\), hence on \(K\). A contractive retraction of a Hilbert space onto a closed subspace is its orthogonal projection: for \(k\in K\), \(v\in\ker Q\), and \(t\in\mathbb C\), contractivity gives \(\|k\|\leq\|k+tv\|\); expanding the square and varying \(t\) forces \(k\perp v\). Every \(h\in H\) decomposes as \(Qh+(h-Qh)\) with the second vector in the kernel, which proves the assertion. Consequently

\[
P\Lambda(x)=W\Lambda_\nu(F(x))\qquad(x\in\mathfrak n_\varphi).
\tag{ME.32}
\]

For arbitrary \(x\in M\) and \(a\in\mathfrak n_\nu\), the product \(xa\) belongs to \(\mathfrak n_\varphi\). Bimodularity and (ME.32) give

\[
\begin{aligned}
\rho(F(x))\Lambda(a)
&=\Lambda(F(x)a)=\Lambda(F(xa))\\
&=P\Lambda(xa)=P\pi(x)P\Lambda(a).
\end{aligned}
\tag{ME.33}
\]

The vectors \(\Lambda(a)\) are dense in \(K\). Therefore

\[
\rho(F(x))=P\pi(x)P|_K\qquad(x\in M).
\tag{ME.34}
\]

The right side depends only on \(M,N,\varphi\), not on \(F\). Faithfulness of \(\rho\) proves uniqueness whenever a preserving retraction exists. It also proves automatic normality: for an increasing positive net, (ME.34) and the inverse normal isomorphism \(\rho^{-1}\) give preservation of its supremum exactly as in ME-04. Faithfulness alternatively follows from preservation, since \(F(X)=0\), \(X\geq0\), implies \(\varphi(X)=0\).

Applying (ME.32) to the constructed \(E\) yields the promised GNS formula

\[
P\Lambda(x)=W\Lambda_\nu(E(x))\qquad(x\in\mathfrak n_\varphi).
\tag{ME.35}
\]

For later finite coefficients, polarization of (ME.34) gives, for \(a,b\in\mathfrak n_\nu\) and \(x\in M\),

\[
\widetilde\varphi(b^*xa)
=\widetilde\nu(b^*E(x)a).
\tag{ME.36}
\]

Both arguments lie in their finite definition algebras: \(xa\in\mathfrak n_\varphi\), \(b\in\mathfrak n_\varphi\), and \(E(x)a,b\in\mathfrak n_\nu\). Thus the tildes denote legitimate linear extensions; no subtraction of infinite weights occurs. \(\square\)

## The converse reduces the closed Tomita map

Assume a retraction \(F\) satisfying (ME.1) exists. We now prove (ME.2). Formula (ME.32) is already established without modular invariance. If \(x\in\mathfrak a_\varphi\), apply (ME.31) to both \(x\) and \(x^*\). It follows that \(F(x)\in\mathfrak a_\nu\). On the full finite-star Tomita core,

\[
P S_{\varphi,0}\Lambda(x)
=\Lambda(F(x^*))
=S_{\varphi,0}\Lambda(F(x))
=S_{\varphi,0}P\Lambda(x).
\tag{ME.37}
\]

Moreover \(P\Lambda(\mathfrak a_\varphi)=\Lambda(\mathfrak a_\nu)\), because \(F\) fixes the latter algebra.

Take \(\xi\in D(S_\varphi)\). By definition of graph closure, choose \(x_j\in\mathfrak a_\varphi\) with \(\Lambda(x_j)\to\xi\) and \(\Lambda(x_j^*)\to S_\varphi\xi\). A sequence suffices in this metric graph norm and makes no countability assumption about the algebra. Projecting both convergences and using (ME.37), then using closedness, gives

\[
P\xi\in D(S_\varphi),\qquad S_\varphi P\xi=P S_\varphi\xi.
\tag{ME.38}
\]

The same follows for \(I-P\). Introduce the bounded self-adjoint unitary

\[
U=I-2P,\qquad U^2=I.
\]

Equation (ME.38) gives \(U D(S_\varphi)=D(S_\varphi)\) and \(S_\varphi U=U S_\varphi\) there. Both inclusions are exact because applying \(U\) a second time reverses the first. Thus

\[
U S_\varphi U=S_\varphi
\quad\hbox{as closed operators, with domain }D(S_\varphi).
\tag{ME.39}
\]

We also verify the adjoint domains. With the antilinear adjoint convention of TC-03, \(\eta\in D(S_\varphi^*)\) means
\(\langle S_\varphi\xi,\eta\rangle=\langle S_\varphi^*\eta,\xi\rangle\) for all \(\xi\in D(S_\varphi)\). For such \(\eta,\xi\),

\[
\begin{aligned}
\langle S_\varphi\xi,U\eta\rangle
&=\langle U S_\varphi\xi,\eta\rangle
=\langle S_\varphi U\xi,\eta\rangle\\
&=\langle S_\varphi^*\eta,U\xi\rangle
=\langle U S_\varphi^*\eta,\xi\rangle.
\end{aligned}
\tag{ME.40}
\]

Therefore \(U\eta\in D(S_\varphi^*)\) and \(S_\varphi^*U\eta=U S_\varphi^*\eta\). Applying \(U\) again proves equality of the transported domain. On the full product domain

\[
D(\Delta_\varphi)=\{\xi\in D(S_\varphi):S_\varphi\xi\in D(S_\varphi^*)\},
\]

these identities prove \(U\Delta_\varphi U=\Delta_\varphi\). SK-08 now gives reduction by \(P=(I-U)/2\) of all spectral projections and all power domains. The polar identity on the dense range of \(\Delta_\varphi^{1/2}\) also gives \(P J_\varphi=J_\varphi P\).

It remains to identify the reduced Tomita map with the smaller one. On the smaller finite-star core it is \(WS_\nu W^*\subseteq S_\varphi|_K\), as before. Conversely, if \(\xi\in K\cap D(S_\varphi)\), project the preceding full graph approximation. Its vectors \(\Lambda(F(x_j))\) belong to \(\Lambda(\mathfrak a_\nu)\), converge to \(\xi\), and their involutions converge to \(S_\varphi\xi\). Closure of the smaller graph proves the reverse inclusion. Orthogonal reduction identifies the adjoint restriction as well: test its defining pairing separately against vectors in \(K\) and \(K^\perp\), on which the two closed restrictions have orthogonal values. We obtain

\[
\begin{gathered}
WS_\nu W^*=S_\varphi|_K,\qquad
WS_\nu^*W^*=S_\varphi^*|_K,\qquad
WJ_\nu W^*=J_\varphi|_K,\\
W D(\Delta_\nu^a)=K\cap D(\Delta_\varphi^a),\qquad
W\Delta_\nu^aW^*=\Delta_\varphi^a|_K\quad(a\in\mathbb R).
\end{gathered}
\tag{ME.41}
\]

Here the adjoint domain is \(K\cap D(S_\varphi^*)=K\cap D(\Delta_\varphi^{-1/2})\); the last equality is TC-09. Spectral restriction also gives \(\Delta_\varphi^{it}|_K=W\Delta_\nu^{it}W^*\).

For \(n\in N\), MF-06 and this real-power restriction imply

\[
\bigl(\pi(\sigma_t^\varphi(n))-\pi(\sigma_t^\nu(n))\bigr)P=0.
\tag{ME.42}
\]

To see the equality, apply both sides to a vector of \(K\); its modular translates stay in \(K\), and \(\pi(n)|_K=\rho(n)\). The difference in (ME.42) belongs to \(\pi(M)\), so the separation lemma ME-02 proves equality of the two algebra elements. Thus \(\sigma_t^\varphi(n)=\sigma_t^\nu(n)\in N\). Applying the same assertion at \(-t\) proves global equality (ME.2). This completes the converse and the theorem. \(\square\)

The reflection \(I-2P\) in (ME.39) is essential. The operator \(I-P\) is a projection, so conjugating by it discards \(K\). For instance, if \(N=M=\mathbb C\) with its usual finite weight, then \(P=I\) and \(S\) is nonzero complex conjugation. One has \((I-P)S(I-P)=0\), whereas \((I-2P)S(I-2P)=S\). This elementary check explains the corrected reflection step in the antecedent proof; it does not alter the criterion's statement.

## Covariance and the projection relations

Under either equivalent hypothesis, (ME.9) and (ME.14) show for \(x\in M\) that

\[
\begin{aligned}
\rho(E(\sigma_t^\varphi(x)))
&=\Delta_\varphi^{it}|_K\,\rho(E(x))\,\Delta_\varphi^{-it}|_K\\
&=\rho(\sigma_t^\nu(E(x))).
\end{aligned}
\tag{ME.43}
\]

Faithfulness of \(\rho\) proves the covariance in (ME.3). The GNS projection therefore respects the real modular time evolution and, with their domains, every real power and both closed involutions. In particular \(P D(S_\varphi^*)\subseteq D(S_\varphi^*)\) and \(S_\varphi^*P=P S_\varphi^*\); this follows also from \(S_\varphi^*=J_\varphi\Delta_\varphi^{-1/2}\) and (ME.10), (ME.12).

The compression identity on \(K\) is equivalent to the bounded-operator identity on \(H\)

\[
P\pi(x)P=\pi(E(x))P=P\pi(E(x)),\qquad x\in M.
\tag{ME.44}
\]

Both sides vanish on \(K^\perp\), and on \(K\) they agree by definition. Thus products of compressed operators have the concrete form

\[
P\pi(x)P\pi(y)P=\pi(E(x)E(y))P.
\tag{ME.45}
\]

In general this is different from \(\pi(E(xy))P\). The relation (ME.44) is the projection relation used in basic constructions; it proves neither an index formula nor a complete relative tensor product construction.

Combining (ME.18) with (ME.30) also yields the full-positive smaller-test formula

\[
\varphi(X)=
\sup_{\substack{\eta\in\mathcal D_\nu\\\|R^N_\eta\|\leq1}}
\langle\pi(X)\eta,\eta\rangle
=
\sup_{\substack{\eta\in\mathcal D_\nu\\\|R^N_\eta\|<1}}
\langle\pi(X)\eta,\eta\rangle
\quad(X\in M_+).
\tag{ME.46}
\]

The strict version follows either from WH-12 or by multiplying each test vector by a scalar increasing to one. Infinite suprema are preserved by that argument. This supplies a norm-controlled test family from the smaller algebra without replacing the ambient weight by a state.

## Full and entire Hilbert algebras under projection

Continue to identify the smaller GNS space with \(K\). Write \(\mathcal A_\varphi,\mathcal A_\nu\) for the full left algebras, \(\mathcal D_\varphi,\mathcal D_\nu\) for the full right algebras, and \(\mathcal A_{0,\varphi},\mathcal A_{0,\nu}\) for the maximal entire algebras of MF-07. Then

\[
\begin{aligned}
\mathcal A_\nu&=\mathcal A_\varphi\cap K=P\mathcal A_\varphi,\\
\mathcal D_\nu&=\mathcal D_\varphi\cap K=P\mathcal D_\varphi,\\
\mathcal A_{0,\nu}&=\mathcal A_{0,\varphi}\cap K=P\mathcal A_{0,\varphi}.
\end{aligned}
\tag{ME.47}
\]

These are assertions about the full algebras, not about an arbitrary initially chosen dense core.

For the first line, WH-11 gives \(\mathcal A_\omega=\Lambda_\omega(\mathfrak a_\omega)\). Schwarz applied to \(x\) and \(x^*\), together with (ME.35), gives \(P\mathcal A_\varphi\subseteq\mathcal A_\nu\). The reverse inclusion follows because the smaller finite-star vectors belong to the larger algebra and are fixed by \(P\). If \(\Lambda(x)\in\mathcal A_\varphi\cap K\), then (ME.35) gives \(\Lambda(x)=\Lambda(E(x))\). Faithfulness of \(\varphi\) implies \(x=E(x)\in N\), which proves the intersection assertion as well.

For the second line, apply \(J_\varphi\) to the first. MF-05–06 gives \(\mathcal D_\omega=J_\omega\mathcal A_\omega\), while \(J_\varphi K=K\) and \(P J_\varphi=J_\varphi P\). This proves both the intersection and image statements, with the smaller right involution being the exact restriction of the ambient adjoint involution by (ME.41).

For the last line, use the definition

\[
\mathcal A_{0,\omega}
=\{\xi\in\bigcap_{m\in\mathbb Z}D(\Delta_\omega^m):
             \Delta_\omega^m\xi\in\mathcal A_\omega
             \text{ for every }m\in\mathbb Z\}.
\tag{ME.48}
\]

The exact restricted power domains show that an ambient entire vector in \(K\) has all its integer powers in \(\mathcal A_\varphi\cap K=\mathcal A_\nu\). Conversely all powers of a smaller entire vector are ambient powers and belong to the ambient full algebra. This proves the intersection equality. If \(\xi\in\mathcal A_{0,\varphi}\), domain reduction gives
\(\Delta_\varphi^mP\xi=P\Delta_\varphi^m\xi\in\mathcal A_\nu\) for every integer \(m\). Therefore \(P\xi\in\mathcal A_{0,\nu}\). Smaller entire vectors are fixed by \(P\), proving the image equality. Negative integers are included throughout. The entire modular actions agree on these spaces by the same spectral domains and (ME.11).

Finally the two projection-module identities are

\[
P(\xi\eta)=\xi(P\eta)
\quad(\xi\in\mathcal A_\nu,\ \eta\in\mathcal A_\varphi),
\tag{ME.49}
\]

\[
P(R_\eta^M\xi)=R_\eta^M(P\xi)
\quad(\eta\in\mathcal D_\nu,\ \xi\in\mathcal A_\varphi).
\tag{ME.50}
\]

For (ME.49), write \(\xi=\Lambda(n)\), \(n\in\mathfrak a_\nu\); its left multiplier is \(\pi(n)\), which commutes with \(P\) by (ME.6). For (ME.50), write \(\eta=J_K\Lambda(n)\). Its ambient right multiplier is \(J_\varphi\pi(n)J_\varphi\), which commutes with \(P\) by (ME.6), (ME.12). Thus both formulas hold as bounded multiplication identities on the displayed vectors, indeed on every ambient vector for those fixed multipliers. Their restrictions to \(K\) are exactly the corresponding smaller multiplication operators; no extension of an unbounded product has been presumed. \(\square\)

## Three models that separate the assumptions

**An expectation where no faithful normal state exists.** Let \(I\) be an uncountable set and put

\[
M=\prod_{i\in I}M_2(\mathbb C),\qquad
N=\prod_{i\in I}\{\text{diagonal matrices}\},\qquad
d=\begin{pmatrix}1&0\\0&3\end{pmatrix}.
\]

Here the product consists of uniformly bounded families, with coordinatewise operations. Define the sum of a nonnegative family as the supremum of its finite subsums, and set

\[
\varphi(X)=\sum_{i\in I}\operatorname{Tr}(dX_i),\qquad X\in M_+.
\tag{ME.51}
\]

This is faithful and normal. For normality, on an increasing positive net each finite coordinate sum increases to its value at the supremum; taking the supremum over finite subsets commutes with that directed supremum. Cutting off to a finite subset of coordinates gives an increasing net of positive finite-weight elements converging to any given positive element. Thus both \(\varphi\) and its restriction to \(N\) are semifinite. These are nets indexed by finite subsets, not a countable decomposition.

The modular group acts coordinatewise by
\(\sigma_t^\varphi(x)_i=d^{it}x_i d^{-it}\). One can see its full GNS realization directly: \(\Lambda(x)=(x_i d^{1/2})_{i\in I}\) belongs to the Hilbert direct sum of the Hilbert–Schmidt spaces, and the modular unitaries send \(\xi_i\) to \(d^{it}\xi_i d^{-it}\). Finite-coordinate vectors form a core, and the closed direct-sum action gives the stated group. It preserves \(N\). The theorem's expectation is

\[
E(x)_i=\begin{pmatrix}(x_i)_{11}&0\\0&(x_i)_{22}\end{pmatrix}.
\tag{ME.52}
\]

Indeed, each coordinate map is the average of the identity and conjugation by \(\operatorname{diag}(1,-1)\). It is a contractive retraction, and \(\operatorname{Tr}(dE(X)_i)=\operatorname{Tr}(dX_i)\) term by term, including infinite sums. Uniqueness identifies it with the constructed map. In the displayed GNS space, \(P\) removes the off-diagonal Hilbert–Schmidt entries in each coordinate.

There is no faithful normal state on \(M\). If \(\omega\) were one, let \(z_i\) be the central identity projection of the \(i\)-th block. Faithfulness would give \(\omega(z_i)>0\) for every \(i\). For each positive integer \(m\), at most \(m\) of these values can exceed \(1/m\), because every finite sum is at most \(\omega(1)=1\). Their union over \(m\) is countable and contains every strictly positive value, a contradiction. The modular expectation above consequently cannot be reduced to a faithful-state argument on the whole algebra.

**A finite restriction can still fail modular invariance.** In \(M=M_2(\mathbb C)\), take

\[
d=\operatorname{diag}(1,4),\qquad
p=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad
N=\mathbb Cp+\mathbb C(1-p),\qquad \varphi(X)=\operatorname{Tr}(dX).
\]

Both weights are finite and faithful. Yet

\[
\sigma_t^\varphi(p)=\frac12
\begin{pmatrix}1&4^{-it}\\4^{it}&1\end{pmatrix}.
\tag{ME.53}
\]

The off-diagonal entries of every element of \(N\) are equal. Choosing \(t\) with \(4^{it}=i\) shows that (ME.53) is not in \(N\). Therefore no \(\varphi\)-preserving contractive retraction onto this \(N\) exists. There is nevertheless an ordinary normal conditional expectation: the dephasing map \(D(x)=pxp+(1-p)x(1-p)\). It sends the matrix unit \(e_{11}\) to \(I/2\), whose \(\varphi\)-value is \(5/2\), whereas \(\varphi(e_{11})=1\). The obstruction concerns the prescribed weight.

**Invariance alone does not supply a semifinite restriction.** Let \(M=B(\ell^2(\mathbb N))\), let \(\varphi=\operatorname{Tr}\), and let \(N=\mathbb C I\). The modular group is trivial, so \(N\) is invariant. The restriction has value infinity on every nonzero positive scalar multiple of \(I\); its finite positive cone is just \(\{0\}\), hence it is not semifinite. If a preserving positive retraction existed and \(q\) were a rank-one projection, its image would be \(\lambda I\) for some \(\lambda\geq0\). The restricted weight of that image would be either zero or infinity, and could not equal \(\operatorname{Tr}(q)=1\). This locates the necessity of the restriction assumption independently of any countability issue.

## Problems with complete solutions

**Problem 1: nested subalgebras.** Suppose \(L\subseteq N\subseteq M\) share their identity, both restrictions of the NSF weight \(\varphi\) are semifinite, and both subalgebras are invariant under \(\sigma^\varphi\). Write \(E_N^M,E_L^M,E_L^N\) for the expectations given by the theorem. Prove the tower formula and identify the corresponding products of GNS projections.

**Solution.** The restriction theorem gives \(\sigma^{\varphi|_N}=\sigma^\varphi|_N\), so \(L\) satisfies the theorem inside \(N\). The composition \(E_L^N E_N^M\) is a contractive retraction onto \(L\). For every \(X\in M_+\), preservation at each step gives

\[
(\varphi|_L)(E_L^N E_N^M(X))
=(\varphi|_N)(E_N^M(X))=\varphi(X).
\]

Uniqueness therefore proves

\[
E_L^M=E_L^N E_N^M,\qquad
E_L^M E_N^M=E_L^M,\qquad E_N^M E_L^M=E_L^M.
\tag{ME.54}
\]

The last equality also follows because \(E_N^M\) fixes \(L\). In the ambient GNS space, \(K_L\subseteq K_N\), since \(\mathfrak n_{\varphi|_L}\subseteq\mathfrak n_{\varphi|_N}\). For their orthogonal projections \(Q,P\), this gives \(PQ=QP=Q\): the equality \(PQ=Q\) follows from the range inclusion and the other from taking adjoints. Formula (ME.35) identifies these projections with the three expectations; the projection of \(K_N\) onto \(K_L\) is \(Q|_{K_N}\). No tensor-product or index assumption is needed.

**Problem 2: the exact finite-weight error identity.** For \(x\in\mathfrak n_\varphi\) and \(b\in\mathfrak n_\nu\), prove

\[
\varphi((x-b)^*(x-b))
=\varphi((x-E(x))^*(x-E(x)))
 +\nu((E(x)-b)^*(E(x)-b)).
\tag{ME.55}
\]

Deduce the minimizing property of \(E(x)\), and relate the first term on the right to the positive conditional variance.

**Solution.** Schwarz and preservation put \(E(x)\) in \(\mathfrak n_\nu\). All differences in (ME.55) belong to the appropriate linear left ideals, so every displayed value is finite. Equation (ME.35) gives

\[
\Lambda(x-b)=(I-P)\Lambda(x)+(P\Lambda(x)-\Lambda(b)).
\]

These summands lie respectively in \(K^\perp\) and \(K\). Taking their squared norms proves (ME.55). The second term is nonnegative and vanishes precisely when \(b=E(x)\), by faithfulness. Hence \(E(x)\) is the unique minimizing element among \(\mathfrak n_\nu\), for this GNS error.

Bimodularity and involution preservation give an equality of bounded elements of \(N\):

\[
E((x-E(x))^*(x-E(x)))
=E(x^*x)-E(x)^*E(x)\geq0.
\tag{ME.56}
\]

Applying \(\nu\) and preservation identifies its value with the first term on the right of (ME.55). If one writes that value as \(\varphi(x^*x)-\nu(E(x)^*E(x))\), both terms are finite here, so the subtraction is justified. For arbitrary \(x\in M\), (ME.56) still holds as an operator identity, but subtracting two infinite weight values would not be justified.

**Problem 3: check the imaginary-time sign.** In \(M=M_2(\mathbb C)\), let \(d\) be strictly positive, let \(\varphi(X)=\operatorname{Tr}(dX)\), and identify the GNS space with Hilbert–Schmidt matrices by \(\Lambda(x)=xd^{1/2}\). For \(0\leq c\leq I\), compute the element \(a\) with \(\Lambda(a)=J\Lambda(c)\), and identify its right multiplication operator on this Hilbert space. Explain why a minus imaginary half-shift occurs.

**Solution.** In this realization \(J\xi=\xi^*\) and \(\sigma_t(x)=d^{it}xd^{-it}\). Consequently

\[
J\Lambda(c)=d^{1/2}c,\qquad
a=d^{1/2}cd^{-1/2}=\sigma_{-i/2}(c),\qquad
\Lambda(a)=d^{1/2}c.
\tag{ME.57}
\]

For a finite GNS vector \(xd^{1/2}\), multiplication of GNS elements on the right by \(a\) gives
\(xa d^{1/2}=xd^{1/2}c\). Thus its actual bounded right multiplication operator is \(\xi\mapsto\xi c\), which is positive and contractive on Hilbert–Schmidt space when \(0\leq c\leq I\). It is exactly \(J\pi(c)J\). The opposite shift would instead give \(d^{-1/2}cd^{1/2}\), and generally fails the required GNS identity. For a numerical check, take \(d=\operatorname{diag}(2,7)\) and \(c=\left(\begin{smallmatrix}1/2&1/4\\1/4&1/2\end{smallmatrix}\right)\). The upper-right entry of \(a\) is \(\sqrt{2/7}/4\), whereas the opposite shift gives \(\sqrt{7/2}/4\). This difference is present even though \(c\) is a positive contraction.

**Problem 4: why the identity is shared.** Take \(M=\mathbb C\oplus\mathbb C\), \(N=\mathbb C\oplus0\), and \(\varphi(s,t)=s+t\) on positive elements. Verify invariance and semifiniteness of the restriction. Show directly that there is no \(\varphi\)-preserving complex-linear contractive retraction onto \(N\).

**Solution.** The algebra is commutative, so the modular action is trivial. The restriction to \(N\) is the ordinary faithful finite weight on its own identity \((1,0)\). Any linear retraction has the form
\(F(a,b)=(a+\lambda b,0)\) for a scalar \(\lambda\). If \(\lambda\ne0\), choose \(a=1\) and \(b=\overline\lambda/|\lambda|\). The input has norm one but the output has norm \(1+|\lambda|\), contradicting contractivity. Hence \(\lambda=0\). This retraction sends \((0,1)\) to zero and cannot preserve its weight one. The missing assumption is the common identity; the separation lemma would otherwise see only the corner belonging to the smaller identity.

## Antecedents and further course work

The mathematical antecedent for the modular criterion is Takesaki, *Theory of Operator Algebras II*, Chapter IX, Definition 4.1 and Theorem 4.2, including the Hilbert-algebra and GNS consequences developed in that proof. Earlier conditional expectations are treated in Volume I; the present unit uses the already authored CE contractive-retraction results. The finite-ideal, Hilbert-algebra, fundamental modular, KMS, spectral-domain and normal-weight inputs are the exact course items listed in ME-01 and invoked at their proof steps. These references identify mathematical antecedents and prerequisites; the exposition, examples and problems here are independently written.

Three directions build on the theorem. First, (ME.44) provides the bounded projection relation needed for a basic construction; developing its relative commutant, index and canonical weights requires further proofs. Second, dropping finiteness of an expectation's values leads to the extended positive cone and general operator-valued weights; ordinary bounded compression alone does not construct that theory. Third, weight-compatible GNS subspaces are relevant to relative tensor products and correspondences, whose balanced domains, completion, unit and associativity maps must be established separately.

The next item supplies the relative-commutant assertion. The full operator-valued-weight construction, the remaining source exercise phenomena and the later three-volume callbacks retain their own source owners. The solved problems here do not silently discharge those obligations. Complete transitive prerequisite closure, independent final reviews, cumulative rendering and source-free reproducibility, and the separate manager content audit are also distinct from the written theorem proved in this unit.

## A minimal relative commutant forces faithfulness and uniqueness

Let \(N\subseteq M\) be von Neumann algebras with the same identity and
assume

\[
 N'\cap M=\mathcal Z(N).
 \tag{ME.58}
\]

Let \(E:M\to N\) be a normal complex-linear projection of norm one.
Then \(E\) is faithful and is the unique normal norm-one projection of
\(M\) onto \(N\).

More precisely, for every faithful normal semifinite weight \(\psi\) on
\(N\), the composite

\[
 \varphi=\psi\circ E
 \tag{ME.59}
\]

is faithful, normal and semifinite, and \(E\) is the unique
\(\varphi\)-preserving conditional expectation onto \(N\).

**The scalar composite is normal and semifinite.** Tomiyama's theorem
CE-004 makes \(E\) positive and \(N\)-bimodular. Normality of \(E\) and
of \(\psi\) makes \(\varphi\) normal. To see semifiniteness without
assuming faithfulness, use WS-02 for \(\psi\): there is an increasing net
of positive contractions \(e_i\in\mathfrak n_\psi\) converging strongly
to \(1\). For \(y\in M\), bimodularity gives

\[
\begin{aligned}
 E((ye_i)^*ye_i)
 &=e_iE(y^*y)e_i\\
 &\leq\lVert y\rVert^2e_i^2.
\end{aligned}
 \tag{ME.60}
\]

Thus \(e_i,ye_i\in\mathfrak n_\varphi\), and
\(e_iye_i=e_i^*(ye_i)\in\mathfrak m_\varphi\). These compressions
converge strongly to \(y\). Hence the finite definition algebra of
\(\varphi\) is ultraweakly dense, which proves semifiniteness.

**The relative commutant removes the null corner.** Let \(p=s(\varphi)\).
Because \(\varphi\) is normal and semifinite, WS-04–06 identify its null
left ideal
\(\mathcal K_\varphi:=\{x\in M:\varphi(x^*x)=0\}\) by

\[
 \mathcal K_\varphi=M(1-p).
 \tag{ME.61}
\]

Faithfulness of \(\psi\) says

\[
 x\in\mathcal K_\varphi
 \quad\Longleftrightarrow\quad
 E(x^*x)=0.
\]

If \(b\in N\) and \(x\in\mathcal K_\varphi\), then

\[
 E((xb)^*xb)=b^*E(x^*x)b=0.
\]

Thus \(M(1-p)\) is invariant under right multiplication by \(N\).
Taking \(x=1-p\), and then repeating the argument with \(b^*\), gives

\[
 (1-p)bp=0=pb(1-p).
\]

Therefore \(p\in N'\cap M=\mathcal Z(N)\), so \(1-p\in N\). Since \(E\)
fixes \(N\),

\[
 0=\varphi(1-p)=\psi(E(1-p))=\psi(1-p).
\]

The weight \(\psi\) is faithful, hence \(p=1\). This proves that
\(\varphi\) is faithful. If \(E(x^*x)=0\), then
\(\varphi(x^*x)=0\), so \(x=0\); therefore \(E\) is faithful as well.

**Two projections give one weight.** Let \(E_0,E_1:M\to N\) be normal
norm-one projections. Fix an n.s.f. weight \(\psi\) on \(N\), whose
existence is WH-13, and put
\(\varphi_j=\psi\circ E_j\). The preceding argument makes both weights
n.s.f. Each \(E_j\) preserves \(\varphi_j\), and
\(\varphi_j|_{N_+}=\psi\). The converse half of the modular expectation
theorem ME-01 therefore gives

\[
 \left.\sigma_t^{\varphi_0}\right|_N
 =\sigma_t^\psi
 =\left.\sigma_t^{\varphi_1}\right|_N.
 \tag{ME.62}
\]

Set \(u_t=[D\varphi_1:D\varphi_0]_t\). The intertwining identity in
SI-14 and (ME.62) imply

\[
 u_t\sigma_t^\psi(n)u_t^*=\sigma_t^\psi(n)
 \qquad(n\in N).
\]

Since \(\sigma_t^\psi(N)=N\), we have
\(u_t\in N'\cap M=\mathcal Z(N)\). Every central element of \(N\) lies
in the \(\psi\)-centralizer by CZ-05. Consequently
\(\sigma_s^{\varphi_0}(u_t)=\sigma_s^\psi(u_t)=u_t\), and the cocycle law
reduces to

\[
 u_{s+t}=u_su_t.
 \tag{ME.63}
\]

PT-03 now gives a unique positive injective self-adjoint operator \(h\)
affiliated with \(\mathcal Z(N)\) such that \(u_t=h^{it}\). PT-05,
applied on \(M\), identifies
\(\varphi_1=(\varphi_0)_h\). Put
\(h_\varepsilon=h(1+\varepsilon h)^{-1}\). For \(x\in N_+\), the
bounded-regularization formula gives

\[
\begin{aligned}
 \psi(x)
 &=\varphi_1(x)\\
 &=\sup_{\varepsilon>0}
   \varphi_0\!\left(
     h_\varepsilon^{1/2}x h_\varepsilon^{1/2}
   \right).
\end{aligned}
\]

Because \(h_\varepsilon\) is affiliated with the center of \(N\), the
argument of \(\varphi_0\) lies in \(N_+\). There
\(\varphi_0=\psi\), so the last supremum is exactly \(\psi_h(x)\).
Consequently

\[
 \psi_h=\psi\quad\hbox{on }N_+.
 \tag{ME.64}
\]

Uniqueness of the centralizer density in PT-05, now on \(N\), yields
\(h=1\). Hence \(\varphi_1=\varphi_0\). Both \(E_0\) and \(E_1\) are
expectations preserving this one weight, so uniqueness in ME-01 gives
\(E_0=E_1\).

Finally, the argument began with an arbitrary n.s.f. \(\psi\) on \(N\).
For its composite (ME.59), \(E\) is positive, normal, bimodular,
faithful and \(\varphi\)-preserving. It is therefore the conditional
expectation relative to \(\varphi\), as asserted. \(\square\)

The mathematical antecedent is Takesaki, *Theory of Operator Algebras II*, IX.4, Proposition 4.3. The proof here makes the finite-domain approximation, support argument, cocycle normalization, and density uniqueness explicit.
