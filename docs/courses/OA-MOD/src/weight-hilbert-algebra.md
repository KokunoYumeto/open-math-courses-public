# Weights and the Hilbert spaces of multiplication

**Self-checked by the writing AI.**

A faithful normal semifinite weight determines a Hilbert space, but the finite elements must also remember multiplication and adjoints. Conversely, a Hilbert algebra already contains enough information to measure positive operators: a positive operator has finite weight precisely when its square root is multiplication by a vector. We prove both directions, including the exact domains and the completion required on the algebra side.

The argument proceeds through bounded multiplication vectors, polar factorization and weak compactness, with the free sources and exact preceding proofs specified below. It does not use the modular fundamental theorem, identify an algebra with its modular conjugate, or assume a faithful state. The predual-valued completely positive maps are established separately in WH-17 after the weight construction.

The principal free comparison is François Combes, [*Poids associé à une algèbre hilbertienne à gauche* (1971)](https://www.numdam.org/item/CM_1971__23_1_49_0.pdf), Lemmas 2.2–2.4 and Theorems 2.11 and 2.13. The complete proofs of the two theorems inform this comparison. Their earlier bounded-vector and dominated-functional inputs are supplied here by HA, RD, WG, NW and OW. Combes's modular covariance and maximal modular algebra lemmas already use modular theory and are not inputs to this construction. Modular invariance is proved later in MF06. Theorem 2.13's hypothesis that a weight is the supremum of its dominated normal positive functionals is supplied by NW11; it is retained in the fullness argument.

A second free comparison is Brent Nelson, [*Tomita–Takesaki Theory*, pages 32–36, Lemmas 4.1–4.4 and Theorems 4.5–4.7](https://users.math.msu.edu/users/banelson/files/Tomita-Takesaki%20Theory.pdf). WH05–07 prove additivity and normality directly, before the variational formula; this avoids the unproved directedness assertion in the notes' Lemma 4.4. WH10 supplies the totality argument needed for closability, and WH11 proves finite weight before applying the GNS map to the recovered element. WH17 proves the completely positive maps in full, with each open-ball image taken in its map's actual domain, correcting the interchanged subscripts in Lemma 4.2.

## Interfaces and analytic prerequisites

All Hilbert spaces and index sets are arbitrary. Inner products are linear in the first variable. A von Neumann algebra is concrete and unital; the zero algebra is allowed. A normal weight preserves bounded increasing positive suprema, and semifiniteness means ultraweak density of its finite definition algebra, as in WG-002.

The proof uses the following preceding programme results. Each link leads to a written proof, not to a replacement citation.

- WG003–010 prove the finite ideals and their positive cone, the GNS construction, finite positive contraction nets, density of the finite-star domain, and faithfulness and normality of the representation.
- NW11 recovers a normal weight from dominated normal positive functionals. OW02–03 construct their exact implementing vectors for a normal semifinite weight.
- HA05–08 and RD02–07 prove bounded multiplication, right-algebra graph density, commutant generation, product cores and the adjoint intersection of the multiplication ideal. FL01–04 give the opposite-algebra construction and full completion used in WH03–04.
- BK01–07 prove the continuous calculus, polynomial approximation, bicommutant theorem, operator topologies, monotone convergence, inverse order, supports and rectangular polar decomposition. DW02 proves the needed Douglas factorization.
- CP06 and CP11 construct the Banach preduals. NP04 and NP06 prove the continuity of normal positive maps and representations. WH02 then proves image closure.
- AB05 proves Banach–Alaoglu. CV2 and CV3 prove weak compactness of Hilbert balls and the full convex Krein–Šmulian theorem for arbitrary Banach spaces.

Krein–Šmulian is used only in WH02. The direct normality proof in WH07 uses Hilbert weak compactness with subnets. The unbounded spectral and graph arguments used by RD are written in SK01–08 and TC03–09; the bounded calculus alone would not supply them.

We shall use strong continuity of positive square roots on a uniformly bounded positive set. Here is the needed argument. If \(0\leq a_i,a\leq C1\) and \(a_i\to a\) strongly, fixed powers and therefore fixed polynomials converge strongly, by induction and the uniform operator bounds. Uniform polynomial approximation of \(t^{1/2}\) on \([0,C]\), followed by bounded continuous functional calculus, makes the errors in both square roots uniformly small in operator norm. Applying this to each vector proves \(a_i^{1/2}\to a^{1/2}\) strongly. This works for arbitrary nets.

## The image of a faithful normal representation

**Lemma.** If \(\pi:M\to B(H)\) is a faithful normal *-representation of a von Neumann algebra, then \(\pi(M)\) is an ultraweakly closed *-subalgebra with identity \(p=\pi(1)\). It acts as a von Neumann algebra on \(pH\), and as zero on \((I-p)H\). The map \(\pi\) is an ultraweak and sigma-strong* homeomorphism onto its image, with the inherited corner topologies. When \(\pi\) is unital, \(p=I_H\).

**Proof.** First \(\pi\) is isometric. Contractivity follows from positivity and the C*-identity. To check the reverse inequality without assuming that its image is closed, let \(b\in M_+\). If \(\|\pi(b)\|<\|b\|\), choose a continuous function on \([0,\|b\|]\) vanishing on \([0,\|\pi(b)\|]\) but nonzero at \(\|b\|\). Continuous functional calculus gives \(f(b)\ne0\), since the norm of a positive element belongs to its spectrum, but
\(\pi(f(b))=f(\pi(b))=0\), contradicting faithfulness. Applying this to \(b=x^*x\) proves isometry.

For every \(r>0\), the closed ball \(rB_M\) is compact for \(\sigma(M,M_*)\), by AB05 and CP06, CP11. Normality makes \(\pi\) ultraweakly continuous, by NP-04. Its image \(\pi(rB_M)\) is therefore ultraweakly compact and closed in \(B(H)\). Isometry gives

\[
\pi(rB_M)=\pi(M)\cap rB_{B(H)}.
\tag{WH.1}
\]

The linear subspace \(\pi(M)\) is convex. Apply CV3, the convex Krein–Šmulian theorem, in the Banach dual \(B(H)\) to (WH.1): \(\pi(M)\) is ultraweakly closed. Multiplicativity gives \(\pi(x)=p\pi(x)p\), with identity \(p=\pi(1)\). Thus the image is a von Neumann algebra on \(pH\); the inherited ultraweak and sigma-strong* topologies are exactly the corner topologies, since compressing the test vectors by \(p\) gives the same seminorms and functionals. In the nonunital case the continuous function used above vanishes at zero, so its functional-calculus identity also holds in this corner.

Both \(\pi\) and its inverse are now positive *-isomorphisms between von Neumann algebras. They transport order bounds in both directions, so preserve existing bounded increasing positive suprema. NP-04 and NP-06 give ultraweak and sigma-strong* continuity in both directions. The identity assertion follows by evaluating \(\pi(1)\). \(\square\)

The weak-star closed-ball argument is essential here. A merely bounded positive normal map can have a nonclosed image, as NP-08 shows.

## Completing the two multiplication domains

Let \(\mathcal A\subseteq H\) be any left Hilbert algebra. Retain

\[
M=L(\mathcal A)'',\qquad S=\overline{\sharp},\qquad F=S^*,
\]

and the right-bounded space \(\mathcal B_r\), its operators \(R_\eta\), and the right algebra

\[
\mathcal A_r=\mathcal B_r\cap D(F).
\tag{WH.2}
\]

By RD-04–05, \(\mathcal A_r\) is a right Hilbert algebra, its closed involution is \(F\), and \(R(\mathcal A_r)''=M'\).

Define the **left-bounded space relative to this right algebra** by

\[
\mathcal B_l=
\left\{\xi\in H:\ \exists C<\infty\
\forall\eta\in\mathcal A_r,\ 
\|R_\eta\xi\|\leq C\|\eta\|\right\}.
\tag{WH.3}
\]

For \(\xi\in\mathcal B_l\), let \(\lambda_\xi\) be the unique bounded operator satisfying

\[
\lambda_\xi\eta=R_\eta\xi\qquad(\eta\in\mathcal A_r).
\tag{WH.4}
\]

Put

\[
\mathfrak n_l=\{\lambda_\xi:\xi\in\mathcal B_l\},
\qquad
\mathcal A_l=\mathcal B_l\cap D(S).
\tag{WH.5}
\]

**Theorem.** The map \(\lambda:\mathcal B_l\to M\) is linear and injective, and

\[
x\xi\in\mathcal B_l,\qquad \lambda_{x\xi}=x\lambda_\xi
\quad(x\in M,\ \xi\in\mathcal B_l).
\tag{WH.6}
\]

Thus \(\mathfrak n_l\) is a left ideal in \(M\). Moreover,

\[
\mathcal A\subseteq\mathcal A_l,\qquad \lambda_a=L_a\quad(a\in\mathcal A).
\tag{WH.7}
\]

The space \(\mathcal A_l\) is a left Hilbert algebra with

\[
\xi\zeta=\lambda_\xi\zeta,\qquad \xi^\sharp=S\xi,\qquad
\lambda_{S\xi}=\lambda_\xi^*,
\tag{WH.8}
\]

and

\[
\overline{S|_{\mathcal A_l}}=S,\qquad
\lambda(\mathcal A_l)''=M,\qquad
\lambda(\mathcal A_l)=\mathfrak n_l\cap\mathfrak n_l^*.
\tag{WH.9}
\]

**Proof.** The opposite-algebra axioms and the two dualizations are proved in FL01–03. Apply HA and RD to the opposite algebra of \(\mathcal A_r\), whose product is \(\eta\circ\zeta=\zeta\eta\). Its left multiplication is \(R_\eta\), its generated algebra is \(M'\), its closed involution is \(F\), and the adjoint involution is \(F^*=S\). The right-bounded-vector construction in that application is exactly (WH.3–4): the test operator for \(\xi\) sends \(\eta\) to \(R_\eta\xi\). HA-05 therefore proves linearity, injectivity, membership in \((M')'=M\), and (WH.6).

For \(a\in\mathcal A\) and \(\eta\in\mathcal A_r\),
\(R_\eta a=L_a\eta\), so \(a\in\mathcal B_l\) and \(\lambda_a=L_a\). Also \(a\in D(S)\), proving (WH.7).

The right algebra in the application to \(\mathcal A_r^{\mathrm{op}}\) has product \(\xi\circ\zeta=\lambda_\zeta\xi\). Taking its opposite makes the product \(\xi\zeta=\lambda_\xi\zeta\), as asserted. HA-08 and RD-04 give the Hilbert algebra axioms and closed involution \(S\). RD-05 gives the generated algebra \((M')'=M\). RD-07 gives precisely the ideal intersection in (WH.9). These are applications to a fully established right Hilbert algebra, not an assumption that \(\mathcal A\) was already full. \(\square\)

## Mixed bounded vectors and fullness

**Mixed-product lemma.** For every \(\xi\in\mathcal B_l\) and every \(\eta\in\mathcal B_r\),

\[
\lambda_\xi\eta=R_\eta\xi.
\tag{WH.10}
\]

The right algebra obtained by dualizing \(\mathcal A_l\) is exactly \(\mathcal A_r\), with the same products, involution and right operators.

**Proof.** Choose the positive contractions \(e_i\in R(\mathcal A_r)\) of RD-05, with \(e_i\to I\) strongly. Because each \(e_i\) is self-adjoint, it has the form \(R_{\alpha_i}^*\) with \(\alpha_i\in\mathcal A_r\). For \(\eta\in\mathcal B_r\), HA-08 gives

\[
\eta_i=e_i\eta\in\mathcal A_r,\qquad
R_{\eta_i}=e_iR_\eta.
\]

Thus \(\eta_i\to\eta\) in norm and \(R_{\eta_i}\to R_\eta\) strongly. For \(\xi\in\mathcal B_l\), (WH.4) gives
\(\lambda_\xi\eta_i=R_{\eta_i}\xi\); the limits prove (WH.10).

The closed involution of \(\mathcal A_l\) is \(S\), so the adjoint-domain condition for its right algebra is membership in \(D(F)\). If \(\eta\) belongs to that right algebra, restricting its right-boundedness inequality to \(\mathcal A\subseteq\mathcal A_l\) puts \(\eta\) in \(\mathcal B_r\). Therefore \(\eta\in\mathcal A_r\). Conversely, if \(\eta\in\mathcal A_r\), then for every \(\xi\in\mathcal A_l\),

\[
\|\lambda_\xi\eta\|=\|R_\eta\xi\|
\leq\|R_\eta\|\|\xi\|.
\]

Hence it is right bounded for \(\mathcal A_l\); it is already in \(D(F)\), and its right operator is \(R_\eta\). The involution and products consequently agree. \(\square\)

We call a left Hilbert algebra **full** when it equals the left algebra obtained by this two-step dualization. Since the right algebra of \(\mathcal A_l\) is \(\mathcal A_r\), its next left dual is again \(\mathcal A_l\). Thus \(\mathcal A_l\) is full. The original \(\mathcal A\) is a graph core in this completion, because both closed involutions are \(S\); equality need not hold.

## Measuring square roots by vectors

Keep an arbitrary \(\mathcal A\) and the completed multiplication spaces of WH-03. For \(a\in M_+\), define

\[
\psi(a)=
\begin{cases}
\|\xi\|^2,&a^{1/2}=\lambda_\xi\text{ for some }\xi\in\mathcal B_l,\\
+\infty,&a^{1/2}\notin\mathfrak n_l.
\end{cases}
\tag{WH.11}
\]

Injectivity of \(\lambda\) makes the finite value unambiguous. In the finite case, \(\lambda_\xi\) is self-adjoint, so (WH.9) implies \(\xi\in\mathcal A_l\) and \(S\xi=\xi\).

**Finite-cone theorem.** The set

\[
P=\{a\in M_+:a^{1/2}\in\mathfrak n_l\}
\tag{WH.12}
\]

is additive, positively homogeneous and hereditary. Its finite value in (WH.11) is additive and positively homogeneous, and is increasing for the positive order.

**Proof of heredity.** If \(0\leq b\leq a\in P\), Douglas factorization in \(M\) gives \(c\in M\), \(\|c\|\leq1\), with \(b^{1/2}=ca^{1/2}\). If \(a^{1/2}=\lambda_\xi\), covariance gives
\(b^{1/2}=\lambda_{c\xi}\). Thus \(b\in P\) and

\[
\psi(b)=\|c\xi\|^2\leq\|\xi\|^2=\psi(a).
\tag{WH.13}
\]

**Proof of additivity.** Suppose \(a,b\in P\), with square-root vectors \(\xi,\eta\). Write \(t=(a+b)^{1/2}\). The polar decomposition of the column operator

\[
\binom{a^{1/2}}{b^{1/2}}=\binom{u}{v}t
\tag{WH.14}
\]

lies in the rectangular matrix algebra over \(M\). Its initial projection is \(p=s(t)\), so

\[
u^*u+v^*v=p,\qquad up=u,\quad vp=v,\qquad
a^{1/2}=ut,\quad b^{1/2}=vt.
\]

In particular \(u^*a^{1/2}+v^*b^{1/2}=pt=t\).
Define \(\zeta=u^*\xi+v^*\eta\). Covariance and linearity yield

\[
\lambda_\zeta=t.
\]

Thus \(a+b\in P\). Applying \(\lambda\) to \(u\zeta\), \(v\zeta\) and \(p\zeta\), then using injectivity, gives

\[
u\zeta=\xi,\qquad v\zeta=\eta,\qquad p\zeta=\zeta.
\]

Consequently

\[
\psi(a)+\psi(b)=\|u\zeta\|^2+\|v\zeta\|^2
=\langle p\zeta,\zeta\rangle=\|\zeta\|^2
=\psi(a+b).
\tag{WH.15}
\]

This norm identity uses the polar support; a generic pair of contractions would not suffice.

For \(r>0\), the square-root vector of \(ra\) is \(\sqrt r\,\xi\). This proves homogeneity and preservation of the finite cone under nonzero rescaling. The zero operator has the unique vector zero. Thus \(\psi(0)=0\), and homogeneity at zero uses \(0\cdot\infty=0\). \(\square\)

If a positive sum belongs to \(P\), heredity puts each summand in \(P\). Therefore, if either summand has infinite value, the sum does also. The finite and infinite cases together prove that (WH.11) is a weight.

## The exact finite ideals and GNS norm

**Theorem.** The weight in (WH.11) satisfies

\[
\mathfrak n_\psi=\mathfrak n_l,\qquad
\psi(x^*x)=\|\xi\|^2\quad\text{when }x=\lambda_\xi.
\tag{WH.16}
\]

Its definition algebra is

\[
\mathfrak m_\psi=\operatorname{span}\mathfrak n_l^*\mathfrak n_l,
\qquad
(\mathfrak m_\psi)_+=P.
\tag{WH.17}
\]

For \(x=\lambda_\xi\), \(y=\lambda_\eta\),

\[
\widetilde\psi(y^*x)=\langle\xi,\eta\rangle.
\tag{WH.18}
\]

**Proof.** Let \(x=\lambda_\xi\in\mathfrak n_l\), and write its bounded polar decomposition \(x=w|x|\). Covariance gives

\[
|x|=w^*x=\lambda_{w^*\xi}.
\]

Thus \(x^*x\in P\), so \(x\in\mathfrak n_\psi\). The final support \(q=ww^*\) satisfies \(qx=x\), and injectivity gives \(q\xi=\xi\). Hence

\[
\psi(x^*x)=\|w^*\xi\|^2=\langle q\xi,\xi\rangle=\|\xi\|^2.
\]

Conversely, if \(\psi(x^*x)<\infty\), then \(|x|=\lambda_\zeta\) for some \(\zeta\). The same polar decomposition gives \(x=\lambda_{w\zeta}\), proving (WH.16).

The algebra and positive-cone identities in (WH.17) are now precisely WG-003 applied to the weight already proved in WH-05. Polarization of (WH.16), using linearity of \(\lambda\), gives (WH.18). All evaluations of \(\widetilde\psi\) lie in its finite algebra; no complex extension of \(\psi\) to arbitrary elements of \(M\) is used. \(\square\)

These statements give the hereditary-cone and ideal assertions compared with Combes, Lemma 2.10 and Theorem 2.11, and Nelson, Lemma 4.1. Applying the same construction to the opposite right algebra gives the corresponding right-ideal assertions.

## Arbitrary-net normality and semifiniteness

**Theorem.** The weight \(\psi\) is faithful, normal and semifinite.

**Proof of normality.** Suppose \(0\leq a_i\uparrow a\) is a bounded increasing net in \(M\). Set \(L=\sup_i\psi(a_i)\). Monotonicity already gives \(L\leq\psi(a)\); if \(L=\infty\), equality follows. Assume \(L<\infty\). Then

\[
a_i^{1/2}=\lambda_{\xi_i},\qquad \|\xi_i\|^2=\psi(a_i)\leq L.
\]

The closed Hilbert ball of radius \(\sqrt L\) is weakly compact. Therefore this net has a subnet \(\xi_{i(j)}\) converging weakly to some \(\xi\) in the same ball. For each \(\eta\in\mathcal A_r\),

\[
a_{i(j)}^{1/2}\eta=R_\eta\xi_{i(j)}.
\tag{WH.19}
\]

The left side converges in norm to \(a^{1/2}\eta\), by WH-01. The right side converges weakly to \(R_\eta\xi\), since \(R_\eta\) is bounded. Thus

\[
R_\eta\xi=a^{1/2}\eta\qquad(\eta\in\mathcal A_r).
\]

This is the boundedness criterion (WH.3), with constant \(\|a^{1/2}\|\). Hence \(\xi\in\mathcal B_l\), \(\lambda_\xi=a^{1/2}\), and
\(\psi(a)=\|\xi\|^2\leq L\). Combining with the opposite inequality proves normality. Compactness was used for the actual arbitrary net; no separability or countable exhaustion was inserted.

**Proof of faithfulness.** If \(\psi(a)=0\), its square-root vector is zero, so \(a^{1/2}=\lambda_0=0\). Thus \(a=0\).

**Proof of semifiniteness.** Let \(\mathcal C=L(\mathcal A)\). It is a nondegenerate *-algebra by HA-02, and lies in \(\mathfrak n_\psi\) by WH-03 and WH-06. For a finite subset \(E\subseteq\mathcal C\) and \(\varepsilon>0\), put

\[
b_E=\sum_{r\in E}r^*r,\qquad
c_{E,\varepsilon}=b_E(b_E+\varepsilon I)^{-1}.
\tag{WH.20}
\]

Finite additivity makes \(\psi(b_E)<\infty\). Since
\(0\leq c_{E,\varepsilon}\leq\varepsilon^{-1}b_E\), these are finite-weight positive contractions. Order the pairs by enlarging \(E\) and decreasing \(\varepsilon\). Inverse order proves that \(c_{E,\varepsilon}\) increases.

For fixed \(E\), its limit as \(\varepsilon\downarrow0\) is \(s(b_E)\). The common kernel of the \(b_E\)'s is the common kernel of \(\mathcal C\), which is zero by nondegeneracy and *-closure. Their support ranges therefore span \(H\). The strong supremum \(c\leq I\) of the contraction net dominates every \(s(b_E)\), so it acts as the identity on those ranges and hence equals \(I\). We have obtained an increasing finite positive contraction net with supremum \(I\). WG-008 proves semifiniteness. \(\square\)

Normality was proved before invoking any normal-weight characterization for \(\psi\). In particular, the proof does not assume the source's predual-valued map or supremum formula in order to prove that \(\psi\) is a weight.

## Recovering the representation and the full algebra

Let \((H_\psi,\pi_\psi,\Lambda_\psi)\) be the weight's GNS triple. Define on its dense range

\[
U\Lambda_\psi(\lambda_\xi)=\xi\qquad(\xi\in\mathcal B_l).
\tag{WH.21}
\]

**Theorem.** The map \(U\) extends uniquely to a unitary \(H_\psi\to H\), and

\[
U\pi_\psi(x)U^*=x\quad(x\in M).
\tag{WH.22}
\]

It identifies the finite-star algebra exactly:

\[
U\Lambda_\psi(\mathfrak n_\psi\cap\mathfrak n_\psi^*)
=\mathcal A_l.
\tag{WH.23}
\]

Under this identification its product is \(\lambda_\xi\eta\), its involution is \(S\), and its closed involution has domain \(D(S)\).

**Proof.** Equation (WH.18) makes (WH.21) a well-defined isometry. Its range is \(\mathcal B_l\), which contains the dense space \(\mathcal A\). Thus it extends to a surjective isometry. For \(x\in M\), covariance gives

\[
U\pi_\psi(x)\Lambda_\psi(\lambda_\xi)
=U\Lambda_\psi(x\lambda_\xi)=x\xi,
\]

proving (WH.22) by density.

By WH-06 and (WH.9),
\(\mathfrak n_\psi\cap\mathfrak n_\psi^*=\lambda(\mathcal A_l)\).
This proves (WH.23). If \(\xi,\eta\in\mathcal A_l\), then
\(\lambda_\xi\lambda_\eta=\lambda_{\lambda_\xi\eta}\), by covariance; hence the product transports as stated. The equality
\(\lambda_\xi^*=\lambda_{S\xi}\) transports the involution. Its closure is \(S\), by WH-03. \(\square\)

The construction recovers the full completion \(\mathcal A_l\). It recovers the original algebra exactly when that algebra was full. A proper algebra core and its full completion can therefore determine the same weight.

## From a faithful normal semifinite weight to an algebra

Now start with a faithful normal semifinite weight \(\varphi\) on \(M\). Write its GNS triple as \((H,\pi,\Lambda)\), and put

\[
\mathfrak a_\varphi=\mathfrak n_\varphi\cap\mathfrak n_\varphi^*,
\qquad \mathcal A_\varphi=\Lambda(\mathfrak a_\varphi).
\tag{WH.24}
\]

Faithfulness makes \(\Lambda\) injective. Consequently

\[
\Lambda(x)\Lambda(y)=\Lambda(xy),\qquad
\Lambda(x)^\sharp=\Lambda(x^*)
\quad(x,y\in\mathfrak a_\varphi)
\tag{WH.25}
\]

are well-defined algebra operations. The domain \(\mathfrak a_\varphi\) is a *-algebra: it is closed under linear combinations and adjoints, and \(xy\in\mathfrak n_\varphi\), \((xy)^*=y^*x^*\in\mathfrak n_\varphi\), by the left-ideal property.

**Proposition.** The algebra \(\mathcal A_\varphi\) is dense in \(H\), has bounded left multiplication

\[
L_{\Lambda(x)}=\pi(x),
\tag{WH.26}
\]

satisfies the left adjoint identity, and has dense product span. Its generated von Neumann algebra is \(\pi(M)\).

**Proof.** Density is WG-009. The GNS module identity gives (WH.26) on the dense domain and the bound \(\|L_{\Lambda(x)}\|\leq\|x\|\). The adjoint identity follows from \(\pi(x)^*=\pi(x^*)\).

Choose the finite positive contractions \(e_i\uparrow1\) of WG-008. They belong to \(\mathfrak a_\varphi\), since \(e_i^2\leq e_i\). Normality gives \(\pi(e_i)\to I\) strongly. For \(x\in\mathfrak a_\varphi\),

\[
\Lambda(e_i)\Lambda(x)=\pi(e_i)\Lambda(x)\longrightarrow\Lambda(x).
\]

Thus products are dense.

WG-007 and WG-010 make \(\pi\) normal and faithful. WH-02 makes its image a von Neumann algebra. For any \(a\in M\), \(e_i a e_i\in\mathfrak m_\varphi\subseteq\mathfrak a_\varphi\) and \(e_i a e_i\to a\) sigma-strong*, by bounded strong* convergence. NP-06 implies
\(\pi(e_i a e_i)\to\pi(a)\) strongly. Thus \(\pi(\mathfrak a_\varphi)\) generates \(\pi(M)\), proving the final assertion. \(\square\)

Only closability remains among the four Hilbert algebra axioms. It requires more than the normality of \(\pi\).

## Closability on the full finite-star domain

Let

\[
\Phi_\varphi=\{\omega\in M_*^+:\omega\leq\varphi\}.
\]

For each \(\omega\in\Phi_\varphi\), OW-02–03 give

\[
0\leq h_\omega\leq I,\quad h_\omega\in\pi(M)',\quad
h_\omega^{1/2}\Lambda(x)=\pi(x)\eta_\omega
\quad(x\in\mathfrak n_\varphi),
\tag{WH.27}
\]

and

\[
\omega(a)=\langle\pi(a)\eta_\omega,\eta_\omega\rangle
\quad(a\in M).
\tag{WH.28}
\]

**Two totality facts.** One has

\[
\sup_{\omega\in\Phi_\varphi}\|h_\omega^{1/2}\xi\|=\|\xi\|
\quad(\xi\in H),
\tag{WH.29}
\]

and

\[
\overline{\operatorname{span}
\{b\eta_\omega:b\in\pi(M)',\ \omega\in\Phi_\varphi\}}=H.
\tag{WH.30}
\]

**Proof.** On \(\xi=\Lambda(x)\), NW-11 and (WH.27) give

\[
\|\Lambda(x)\|^2=\varphi(x^*x)
=\sup_\omega\omega(x^*x)
=\sup_\omega\|h_\omega^{1/2}\Lambda(x)\|^2.
\]

The supremum in (WH.29) is a 1-Lipschitz function of \(\xi\), since every operator involved is a contraction. Density of the GNS range extends the equality to every vector. In particular, the \(h_\omega^{1/2}\)'s have common kernel zero.

Let \(K\) be the closed subspace in (WH.30). It reduces \(\pi(M)'\); its projection \(P\) lies in \(\pi(M)''=\pi(M)\). By WH-02 there is a projection \(p\in M\) with \(P=\pi(p)\). Each \(\eta_\omega\) belongs to \(K\), so

\[
\omega(1-p)=\|(I-P)\eta_\omega\|^2=0.
\]

NW-11 gives \(\varphi(1-p)=0\). Faithfulness implies \(p=1\), hence \(K=H\). \(\square\)

**Closability theorem.** The conjugate-linear operator

\[
s_0:\mathcal A_\varphi\to H,\qquad
s_0\Lambda(x)=\Lambda(x^*)
\tag{WH.31}
\]

is closable. Therefore \(\mathcal A_\varphi\) is a left Hilbert algebra.

**Proof.** For \(x\in\mathfrak a_\varphi\), \(b\in\pi(M)'\), and \(\omega,\rho\in\Phi_\varphi\), equations (WH.27–28) give

\[
\begin{aligned}
\langle\Lambda(x^*),h_\omega^{1/2}b\eta_\rho\rangle
&=\langle\pi(x^*)\eta_\omega,b\eta_\rho\rangle\\
&=\langle\eta_\omega,b\pi(x)\eta_\rho\rangle\\
&=\langle h_\rho^{1/2}b^*\eta_\omega,\Lambda(x)\rangle.
\end{aligned}
\tag{WH.32}
\]

All operators in this calculation are bounded; the two appearances of \(\Lambda\) are permitted because both \(x\) and \(x^*\) are in \(\mathfrak n_\varphi\).

Suppose \(\Lambda(x_n)\to0\) and \(\Lambda(x_n^*)\to\zeta\) in Hilbert norm. Equation (WH.32) implies

\[
\langle\zeta,h_\omega^{1/2}b\eta_\rho\rangle=0
\quad\text{for every }\omega,\rho,b.
\]

Fix \(\omega\). Totality (WH.30) implies \(h_\omega^{1/2}\zeta=0\). The common-kernel consequence of (WH.29) then gives \(\zeta=0\). This is exactly the graph criterion for closability of a conjugate-linear operator on a Hilbert space. It uses sequences only to test closure in the metrizable Hilbert graph norm; it does not assume a separable Hilbert space. WH-09 supplies the other three axioms. \(\square\)

Write \(S_\varphi=\overline{s_0}\). Its domain is, exactly, the set of norm limits of \(\Lambda(x_n)\) for which \(\Lambda(x_n^*)\) also converges, and the latter limit is \(S_\varphi\) of the former. HA04, the closed-graph argument, and TC03–05 give its closed involution. Its polar data are constructed separately in TC07–10, using the written spectral calculus. The fundamental modular theorem remains separate.

## Fullness and recovery of the original weight

Apply WH-03 to \(\mathcal A_\varphi\), identifying the generated algebra with \(\pi(M)\). Use its spaces \(\mathcal B_l,\mathcal B_r,\mathcal A_r\) and its map \(\lambda\).

**Theorem.** One has the exact bijection

\[
\mathcal B_l=\Lambda(\mathfrak n_\varphi),\qquad
\lambda_{\Lambda(x)}=\pi(x)\quad(x\in\mathfrak n_\varphi).
\tag{WH.33}
\]

Moreover \(\mathcal A_\varphi\) is full, and the reconstructed weight satisfies

\[
\psi(\pi(a))=\varphi(a)\qquad(a\in M_+),
\tag{WH.34}
\]

including infinite values.

**Proof.** Equation (WH.27) implies that \(\eta_\omega\) is right bounded for \(\mathcal A_\varphi\), with \(R_{\eta_\omega}=h_\omega^{1/2}\). This operator is self-adjoint. RD-07, applied to the pair \(\eta_\omega,\eta_\omega\), gives

\[
\eta_\omega\in\mathcal A_r,\qquad
F\eta_\omega=\eta_\omega.
\tag{WH.35}
\]

Take \(\xi\in\mathcal B_l\). Since \(\lambda_\xi\in\pi(M)\), there is a unique \(x\in M\) with \(\lambda_\xi=\pi(x)\). Using NW-11, (WH.4), (WH.29) and (WH.35),

\[
\begin{aligned}
\varphi(x^*x)
&=\sup_{\omega\in\Phi_\varphi}\|\pi(x)\eta_\omega\|^2\\
&=\sup_{\omega\in\Phi_\varphi}\|R_{\eta_\omega}\xi\|^2
=\|\xi\|^2<\infty.
\end{aligned}
\tag{WH.36}
\]

Thus \(x\in\mathfrak n_\varphi\). For each \(\omega\), (WH.27) and (WH.4) give

\[
h_\omega^{1/2}\Lambda(x)
=\pi(x)\eta_\omega
=h_\omega^{1/2}\xi.
\]

Their common kernel is zero, so \(\Lambda(x)=\xi\).

Conversely, let \(x\in\mathfrak n_\varphi\) and write \(x=u|x|\). The self-adjoint element \(|x|\) lies in \(\mathfrak a_\varphi\), since
\(\varphi(|x|^2)=\varphi(x^*x)<\infty\). Therefore
\(\Lambda(|x|)\in\mathcal A_\varphi\subseteq\mathcal B_l\).
Covariance under \(\pi(u)\) gives

\[
\Lambda(x)=\pi(u)\Lambda(|x|)\in\mathcal B_l,\qquad
\lambda_{\Lambda(x)}=\pi(u)\pi(|x|)=\pi(x).
\]

This proves (WH.33).

The ideal intersection (WH.9) now reads

\[
\lambda(\mathcal A_l)
=\pi(\mathfrak n_\varphi)\cap\pi(\mathfrak n_\varphi)^*
=\pi(\mathfrak a_\varphi)
=\lambda(\mathcal A_\varphi).
\]

Injectivity gives \(\mathcal A_l=\mathcal A_\varphi\), proving fullness.

Finally, \(\psi(\pi(a))<\infty\) if and only if
\(\pi(a^{1/2})\in\lambda(\mathcal B_l)=\pi(\mathfrak n_\varphi)\).
Faithfulness of \(\pi\) makes this equivalent to
\(a^{1/2}\in\mathfrak n_\varphi\), or \(\varphi(a)<\infty\). In that case the square-root vector is \(\Lambda(a^{1/2})\), whose squared norm is \(\varphi(a)\). Otherwise both values are infinite. \(\square\)

Thus the passage from a full left Hilbert algebra to its weight and back is inverse, up to the specified canonical unitary, to the passage from a faithful normal semifinite weight to its finite-star algebra.

## The right weight and the variational formula

Return to an arbitrary left Hilbert algebra \(\mathcal A\), with full completion \(\mathcal A_l\), right algebra \(\mathcal A_r\), and reconstructed weight \(\psi\) on \(M\). The symmetric construction on \(\mathcal A_r^{\mathrm{op}}\) defines a faithful normal semifinite weight \(\chi\) on \(M'\):

\[
\chi(b)=
\begin{cases}
\|\eta\|^2,&b^{1/2}=R_\eta,\ \eta\in\mathcal B_r,\\
+\infty,&\text{otherwise},
\end{cases}
\qquad b\in(M')_+.
\tag{WH.37}
\]

Its finite ideal is \(\mathfrak n_r=R(\mathcal B_r)\), and

\[
\widetilde\chi(R_\eta^*R_\zeta)=\langle\zeta,\eta\rangle.
\tag{WH.38}
\]

These are WH-05–08 applied to the opposite right algebra. That application has the same right-bounded space on the other side: \(\mathcal A\subseteq\mathcal A_l\), while (WH.10) proves boundedness on \(\mathcal A_l\) for every original \(\eta\in\mathcal B_r\); restriction gives the converse.

**Theorem.** Under the GNS unitary of WH-08, \(\chi\) is the opposite weight \(\psi^{\mathrm{opp}}\) of OW. Furthermore, for every \(a\in M_+\),

\[
\psi(a)=
\sup_{\substack{\eta\in\mathcal A_r\\\|R_\eta\|\leq1}}
\langle a\eta,\eta\rangle
=
\sup_{\substack{\eta\in\mathcal A_r\\\|R_\eta\|<1}}
\langle a\eta,\eta\rangle.
\tag{WH.39}
\]

The analogous formula for \(\chi\) uses \(\xi\in\mathcal A_l\) with \(\|\lambda_\xi\|\leq1\) or \(<1\).

**Proof of the opposite identification.** Identify the GNS space of \(\psi\) with \(H\), so
\(\Lambda_\psi(\lambda_\xi)=\xi\) and \(\pi_\psi(x)=x\).
For \(\eta\in\mathcal B_r\), the vector functional
\(\omega_\eta(x)=\langle x\eta,\eta\rangle\) is normal and positive. If \(x=\lambda_\xi\in\mathfrak n_\psi\), then (WH.10) gives

\[
\omega_\eta(x^*x)=\|R_\eta\xi\|^2
\leq\|R_\eta\|^2\psi(x^*x).
\tag{WH.40}
\]

Testing finite positive elements with their square roots, and using any strictly larger positive constant for infinite values if necessary, proves domination by a finite multiple of \(\psi\). Its comparison operator is

\[
h_{\omega_\eta}=R_\eta^*R_\eta,
\tag{WH.41}
\]

by polarization on all \(\xi=\Lambda_\psi(x)\).

If \(\chi(b)<\infty\), take \(b^{1/2}=R_\eta\). Equation (WH.41) gives \(h_{\omega_\eta}=b\), and

\[
\psi^{\mathrm{opp}}(b)=\|\omega_\eta\|=\|\eta\|^2=\chi(b).
\]

Conversely, suppose \(b=h_\omega\) for a normal positive functional dominated by a finite multiple of \(\psi\). OW-03 supplies \(\eta_\omega\in H\) with

\[
b^{1/2}\Lambda_\psi(x)=x\eta_\omega
\quad(x\in\mathfrak n_\psi),\qquad
\|\eta_\omega\|^2=\|\omega\|.
\]

Taking \(x=L_a\) with \(a\in\mathcal A\) gives
\(b^{1/2}a=L_a\eta_\omega\).
Thus \(\eta_\omega\in\mathcal B_r\), \(R_{\eta_\omega}=b^{1/2}\), and
\(\chi(b)=\|\omega\|=\psi^{\mathrm{opp}}(b)\).
The finite cones and their values agree, so the infinite values agree as well.

**Proof of the variational formula.** Equation (WH.40) shows that every \(\omega_\eta\) with \(\|R_\eta\|\leq1\) is at most \(\psi\) on \(M_+\). Conversely, if \(0\leq\omega\leq\psi\), OW-02 gives \(h_\omega\leq I\), and the implementing vector in the preceding paragraph has
\(R_{\eta_\omega}=h_\omega^{1/2}\).
Because this operator is self-adjoint, RD-07 gives \(\eta_\omega\in\mathcal A_r\). Thus every dominated normal positive functional is one of the displayed vector functionals with right norm at most one. NW-11, applied to the already proved normal weight \(\psi\), gives the first equality in (WH.39).

For \(0<t<1\), the vector \(t\eta\) has right norm \(<1\) whenever \(\|R_\eta\|\leq1\), and its functional is \(t^2\omega_\eta\). Letting \(t\uparrow1\) proves equality with the strict-norm supremum, including the case of an infinite supremum. Applying the same reasoning to the opposite right algebra proves the formula for \(\chi\). \(\square\)

The same suprema in (WH.39) result if \(\mathcal A_r\) is replaced by \(\mathcal B_r\): (WH.40) bounds all such vector functionals by \(\psi\), and \(\mathcal A_r\subseteq\mathcal B_r\) already attains the stated supremum. This also applies to the strict norm bound, and symmetrically to the left side.

This proof also identifies the two relevant functional sets exactly:

\[
\{\omega_\eta:\eta\in\mathcal A_r,\ \|R_\eta\|\leq1\}
=\{\omega\in M_*^+:\omega\leq\psi\},
\tag{WH.42}
\]

\[
\{\omega_\eta:\eta\in\mathcal A_r,\ \|R_\eta\|<1\}
=\bigcup_{0\leq c<1}\{\omega\in M_*^+:\omega\leq c\psi\}.
\tag{WH.43}
\]

For the reverse inclusion in (WH.43), OW-02 gives \(\|R_{\eta_\omega}\|\leq\sqrt c<1\); the case \(c=0\) gives the zero vector. Both sets are hereditary and convex: domination is preserved when a positive functional is decreased, and for a convex combination in (WH.43) a common constant \(c<1\) is the maximum of the finitely many constants. This proves the hereditary convexity of the functional sets. WH17 supplies the separate completely positive maps; compare Nelson, Lemma 4.2 and Corollary 4.3.

## Every von Neumann algebra has such a weight

**Theorem.** Every von Neumann algebra admits a faithful normal semifinite weight. No sigma-finiteness assumption is required.

**Proof.** In a faithful concrete representation, normal positive functionals separate nonzero positive elements: if \(a\ne0\), choose \(\xi\) with \(\langle a\xi,\xi\rangle>0\). The vector functional is normal.

For a nonzero normal positive functional \(\omega\), denote by \(s(\omega)\) its support projection, using WS04–06 in the bounded case. In particular,

\[
\omega(x^*x)=0\quad\Longleftrightarrow\quad xs(\omega)=0.
\tag{WH.44}
\]

Choose, by Zorn's lemma, a maximal family of normal states \((\omega_i)_{i\in I}\) whose nonzero supports \(p_i=s(\omega_i)\) are pairwise orthogonal. For a chain of such families, its union is again such a family, so the maximality argument applies.

The strong sum \(p=\sum_i p_i\) equals \(1\). Otherwise choose a unit vector in \((1-p)H\). Its vector state has a nonzero support below \(1-p\), since it vanishes on \(p\), contradicting maximality.

Define

\[
\varphi(a)=\sum_{i\in I}\omega_i(a)
=\sup_{F\subseteq I\text{ finite}}\sum_{i\in F}\omega_i(a),
\qquad a\in M_+.
\tag{WH.45}
\]

Suprema of finite nonnegative subsums commute with addition and nonnegative scalar multiplication; for addition, combine the two finite sets used to approximate the two separate suprema. Thus (WH.45) is a weight.

If \(a_j\uparrow a\), normality of each finite sum and commutation of the two suprema give

\[
\varphi(a)=\sup_F\sup_j\sum_{i\in F}\omega_i(a_j)
=\sup_j\varphi(a_j).
\]

This proves arbitrary-net normality.

If \(\varphi(a)=0\), then every \(\omega_i(a)=0\). Equation (WH.44) gives \(a^{1/2}p_i=0\) for every \(i\). Their finite sums converge strongly to \(1\), so \(a^{1/2}=0\); the weight is faithful.

For a finite \(F\subseteq I\), let \(p_F=\sum_{i\in F}p_i\). Supportedness and orthogonality give
\(\omega_i(p_F)=1\) for \(i\in F\) and zero otherwise. Hence
\(\varphi(p_F)=|F|<\infty\). The projections \(p_F\uparrow1\), so WG-008 proves semifiniteness. For the zero algebra, the zero weight has all three properties and the empty family suffices. \(\square\)

The projections in this proof form a specially chosen orthogonal family. It does not assert that the set of all finite projections of an arbitrary weight is directed.

## A proper core and a non-state example

Let \(I\) be any set and let \(w_i>0\). On the diagonal algebra \(M=\ell^\infty(I)\), define

\[
\varphi(a)=\sum_{i\in I}w_i a_i\quad(a\geq0).
\tag{WH.46}
\]

This is faithful. It is normal because finite sums preserve increasing suprema and the two suprema commute, as in WH-13. Finite-support projections have finite weight and increase to \(1\), proving semifiniteness.

Its exact domains are

\[
\mathfrak n_\varphi
=\left\{x\in\ell^\infty(I):\sum_iw_i|x_i|^2<\infty\right\},
\qquad
\mathfrak n_\varphi^*=\mathfrak n_\varphi,
\tag{WH.47}
\]

\[
H_\varphi=\ell^2(I,w),\qquad
\Lambda(x)=x,\qquad
\pi(a)\xi=(a_i\xi_i)_i.
\]

The arbitrary-coordinate completeness and finite-truncation density proofs are given in OW09. They prove that this is the completion of the stated GNS range. Its full Hilbert algebra is
\(\ell^2(I,w)\cap\ell^\infty(I)\), with pointwise multiplication and conjugation.

For comparison start with the smaller Hilbert algebra \(\mathcal A=c_{00}(I)\). RD-08 computes both bounded multiplication spaces as \(\ell^2(I,w)\cap\ell^\infty(I)\). If \(a\in M_+\), its square-root multiplier has vector \((\sqrt{a_i})_i\) exactly when \(\sum_iw_i a_i<\infty\). Therefore (WH.11) recovers (WH.46) from this smaller algebra. The recovered finite-star algebra is its full completion, not necessarily \(c_{00}(I)\).

With \(I=\mathbb N\), \(w_i=1\), the sequence \(x_i=1/i\) belongs to the full algebra but has infinite support, so the inclusion is proper. The finite square sum follows from the telescoping estimate in HA10. With uncountable \(I\) and \(w_i=1\), the Hilbert space is nonseparable and the weight has no finite value at \(1\). No sequence of finite-support projections converges strongly to \(1\): a coordinate outside the countable union of the sequence's supports is annihilated by every member. The finite-subset net does converge strongly.

## Problems with worked solutions

**Problem 1: a noncentral null space prevents the proposed involution.** On \(M_2(\mathbb C)\), let \(\varphi(a)=a_{11}\). Explain why the rule \(\Lambda(x)\mapsto\Lambda(x^*)\) is not well-defined on the GNS quotient, even though the representation is faithful.

**Solution.** The weight is bounded, so \(\mathfrak n_\varphi=M_2(\mathbb C)\), and its GNS space identifies with the first column: \(\Lambda(x)=xe_1\). The representation is the usual matrix action, hence is faithful. But \(E_{12}e_1=0\), whereas \(E_{12}^*e_1=E_{21}e_1=e_2\ne0\). Thus a zero GNS vector would have a nonzero proposed involution image. Faithfulness of the representation does not replace faithfulness of the weight in (WH.25). The faithful support corner is \(\mathbb C E_{11}\), as WS-06 prescribes.

**Problem 2: when is the finite-star algebra unital?** For a faithful normal semifinite weight, prove that its full Hilbert algebra has an algebra identity if and only if \(\varphi(1)<\infty\).

**Solution.** If \(\varphi(1)<\infty\), then \(1\in\mathfrak n_\varphi\), and \(\Lambda(1)\) is a two-sided identity by (WH.25). Conversely suppose \(v=\Lambda(x)\) is an algebra identity. Its left multiplier is the identity on the dense Hilbert algebra, hence is \(I_H\). Equation (WH.26) gives \(\pi(x)=I_H=\pi(1)\), and faithfulness of \(\pi\) gives \(x=1\). Since \(x\in\mathfrak n_\varphi\), one has \(\varphi(1)<\infty\). This also covers the zero algebra with its identity zero.

**Problem 3: rescale the scalar product.** Start with a left Hilbert algebra \(\mathcal A\subseteq H\) and multiply its inner product by \(r>0\). Under the natural identification of the two vector completions and their bounded multiplication algebras, determine the reconstructed weight.

**Solution.** All vector norms are multiplied by \(\sqrt r\), so the boundedness ratios defining \(\mathcal B_l,\mathcal B_r\) and their operator norms are unchanged. Graph closure is unchanged because the two graph norms differ by the same scalar; the adjoint pairing is multiplied by \(r\) on both sides, so the involution domains and actions are unchanged. The square-root vector for a positive operator is therefore the same vector, while its squared norm is multiplied by \(r\). Finite cones agree and the new weight is \(r\psi\), with the same infinite values. The Hilbert-space unitary from the rescaled space to the original one multiplies vectors by \(\sqrt r\), which is compatible with this calculation.

**Problem 4: a nontracial block and its square-root vector.** Let \(D=\operatorname{diag}(2,7)\), and let \(\varphi(a)=\operatorname{Tr}(Da)\) on \(M_2(\mathbb C)\). Realize the GNS space as Hilbert–Schmidt matrices by \(\Lambda(x)=xD^{1/2}\). For

\[
a=\begin{pmatrix}1&1/2\\1/2&2\end{pmatrix},
\]

identify the vector whose left multiplier is \(a^{1/2}\), and compute its squared norm. Explain why replacing it by \(D^{1/2}a^{1/2}\) generally changes the left multiplier.

**Solution.** The trace identities, positivity and Hilbert–Schmidt completion are proved by finite sums in OW10. The displayed matrix is positive because its quadratic form is

\[
 |z_1+z_2/2|^2+\tfrac74|z_2|^2\geq0.
\]

Every matrix is finite for this weight, and

\[
\langle xD^{1/2},yD^{1/2}\rangle_{\mathrm{HS}}
=\operatorname{Tr}(D y^*x).
\]

Left multiplication acts as \(L_b(z)=bz\). By (WH.33), the vector attached to \(L_{a^{1/2}}\) is \(a^{1/2}D^{1/2}\). Its squared norm is

\[
\operatorname{Tr}(D^{1/2}aD^{1/2})
=\operatorname{Tr}(Da)=2+14=16.
\]

Since \(D\) is invertible, the vector \(D^{1/2}a^{1/2}\) equals \(\Lambda(x)\) with
\(x=D^{1/2}a^{1/2}D^{-1/2}\); its left multiplier is \(L_x\). Equality with \(L_{a^{1/2}}\) would require \(D\) to commute with \(a^{1/2}\), and hence with \(a\), which fails because the off-diagonal entries of \(a\) are nonzero and the diagonal entries of \(D\) are distinct. The vector ordering is therefore part of the reconstruction formula.

## Exact exports and the remaining boundary

The two constructions preserve all of the following data: the algebra representation, the finite left ideal, the finite definition algebra, the GNS norm and pairing, the finite-star algebra, its closed involution, and the weight's finite and infinite values. The Hilbert algebra is recovered as its full completion; for a faithful normal semifinite input weight that finite-star algebra is already full. The right reconstructed weight agrees with the opposite weight under the specified GNS unitary.

The proofs cover nonunital Hilbert algebras, arbitrary von Neumann algebras, uncountable index sets, nonseparable Hilbert spaces and genuinely infinite weights. The only countable approximations used in the closability criterion are graph-norm sequences; all global operator approximation and normality statements retain their nets.

Locally compact group and Plancherel examples, C*-weight variants, modular automorphisms, standard forms and relative weight theory are developed in their respective lessons. The variational formula proved in WH-12 is used after the direct normality theorem. The completely positive maps below are a further consequence of the constructed multiplication domains; they are not silently imported through the source's proof order.

The correspondence includes all finite-domain identities and infinite values; it does not require a state or a countable family of approximation projections.

## Completely positive maps from the finite algebras

Let

\[
\mathfrak m_l=\operatorname{span}\mathfrak n_l^*\mathfrak n_l,
\qquad
\mathfrak m_r=\operatorname{span}\mathfrak n_r^*\mathfrak n_r.
\]

Their matrix orders are inherited from \(M\) and \(M'\). To make the codomain convention explicit, a matrix \([f_{ij}]\) of normal functionals on a von Neumann algebra \(N\) is positive in \(M_n(N_*)\) when the map

\[
N\longrightarrow M_n(\mathbb C),\qquad b\longmapsto[f_{ij}(b)]
\]

is completely positive. Concretely, for every positive \([b_{kl}]\in M_m(N)\), the scalar matrix with entries \(f_{ij}(b_{kl})\), indexed by the pairs \((i,k),(j,l)\), must be positive. This is the dual matrix order used here; positivity of the individual diagonal functionals alone would not define it.

**Theorem.** There are well-defined completely positive linear maps

\[
\Theta_l:\mathfrak m_l\longrightarrow(M')_*,
\qquad
\Theta_r:\mathfrak m_r\longrightarrow M_*,
\tag{WH.48}
\]

given by

\[
\Theta_l\!\left(\sum_{j=1}^q\lambda_{\xi_j}^*\lambda_{\eta_j}\right)(b)
=\sum_{j=1}^q\langle b\eta_j,\xi_j\rangle,
\quad b\in M',\quad \xi_j,\eta_j\in\mathcal B_l,
\tag{WH.49}
\]

\[
\Theta_r\!\left(\sum_{j=1}^qR_{\xi_j}^*R_{\eta_j}\right)(a)
=\sum_{j=1}^q\langle a\eta_j,\xi_j\rangle,
\quad a\in M,\quad \xi_j,\eta_j\in\mathcal B_r.
\tag{WH.50}
\]

In particular, these maps send the indicated squares to the corresponding vector functionals. Their images of the positive parts of the closed and open unit balls are exactly

\[
\begin{aligned}
\Theta_l(\{x\in(\mathfrak m_l)_+:\|x\|\leq1\})
&=\{\omega_\xi|_{M'}:\xi\in\mathcal B_l,\ \|\lambda_\xi\|\leq1\},\\
\Theta_l(\{x\in(\mathfrak m_l)_+:\|x\|<1\})
&=\{\omega_\xi|_{M'}:\xi\in\mathcal B_l,\ \|\lambda_\xi\|<1\},
\end{aligned}
\tag{WH.51}
\]

with the analogous two equalities for \(\Theta_r\), using \(\mathcal B_r\), \(R_\eta\) and vector functionals on \(M\). Here \(\omega_\xi(b)=\langle b\xi,\xi\rangle\).

**Proof of well-definedness.** For a displayed expression \(x=\sum_j\lambda_{\xi_j}^*\lambda_{\eta_j}\), the right side of (WH.49) is a finite sum of vector coefficients, hence is a normal bounded functional \(f\) on \(M'\). For \(\zeta\in\mathcal B_r\), the mixed-product identity (WH.10) gives

\[
\begin{aligned}
f(R_\zeta^*R_\zeta)
&=\sum_j\langle R_\zeta\eta_j,R_\zeta\xi_j\rangle\\
&=\sum_j\langle\lambda_{\eta_j}\zeta,\lambda_{\xi_j}\zeta\rangle
=\langle x\zeta,\zeta\rangle.
\end{aligned}
\tag{WH.52}
\]

If the expression represents \(x=0\), this is zero for every \(\zeta\in\mathcal B_r\).

Take the positive contractions \(e_i\in R(\mathcal A_r)\) of RD-05, with \(e_i\to I\) strongly. For any \(b\in(M')_+\), the left-ideal property gives \(b^{1/2}e_i\in\mathfrak n_r\), so it equals \(R_{\zeta_i}\) for some \(\zeta_i\in\mathcal B_r\). Consequently

\[
e_i b e_i=R_{\zeta_i}^*R_{\zeta_i},\qquad f(e_i b e_i)=0.
\]

This net is norm bounded and converges strongly, hence ultraweakly, to \(b\). Normality of \(f\) gives \(f(b)=0\). Every element of \(M'\) is a complex linear combination of positive elements, so \(f=0\). Thus (WH.49) is independent of the expression for \(x\), and the formula proves linearity. If \(x\in(\mathfrak m_l)_+\), WH-06 supplies \(x^{1/2}=\lambda_\xi\), so
\(\Theta_l(x)=\omega_\xi|_{M'}\), proving positivity.

**Proof of complete positivity.** Write \(e_i=R_{\alpha_i}\) with \(\alpha_i\in\mathcal A_r\); these operators are self-adjoint. For \(x\in\mathfrak m_l\) and \(b\in M'\), formula (WH.49) and (WH.10) give

\[
\begin{aligned}
\Theta_l(x)(e_i b e_i)
&=\sum_j\langle b e_i\eta_j,e_i\xi_j\rangle\\
&=\sum_j\langle b\lambda_{\eta_j}\alpha_i,
                    \lambda_{\xi_j}\alpha_i\rangle\\
&=\langle xb\alpha_i,\alpha_i\rangle.
\end{aligned}
\tag{WH.53}
\]

For fixed \(i\), define on all of \(M\)

\[
T_i(x)(b)=\langle xb\alpha_i,\alpha_i\rangle,\qquad b\in M'.
\]

This is a normal functional of \(b\), since it equals
\(\langle b\alpha_i,x^*\alpha_i\rangle\). We verify that \(T_i\) is completely positive with the stated matrix order.

Let \(X=[x_{jk}]\in M_n(M)_+\) and \(B=[b_{uv}]\in M_m(M')_+\). On the direct sum \(H^{nm}\), with coordinates labelled \((j,u)\), define

\[
(\mathsf X z)_{j,u}=\sum_k x_{jk}z_{k,u},
\qquad
(\mathsf B z)_{j,u}=\sum_v b_{uv}z_{j,v}.
\]

Both operators are positive: each is, after grouping coordinates, a direct sum of copies of a positive matrix operator. Their entries commute, so \(\mathsf X\mathsf B=\mathsf B\mathsf X\), and their product is positive. For example,
\(\mathsf X\mathsf B=\mathsf X^{1/2}\mathsf B\mathsf X^{1/2}\geq0\), since commutation passes to the bounded square root.

Compress this product by the bounded map

\[
V_i:\mathbb C^{nm}\to H^{nm},\qquad
(c_{j,u})\longmapsto(c_{j,u}\alpha_i).
\]

The resulting positive scalar matrix has entry

\[
\langle x_{jk}b_{uv}\alpha_i,\alpha_i\rangle
=T_i(x_{jk})(b_{uv})
\]

in position \((j,u),(k,v)\). This is exactly the required matrix test. Thus \(T_i\) is completely positive.

For fixed \(x=\sum_j\lambda_{\xi_j}^*\lambda_{\eta_j}\), the first line of (WH.53) and \(e_i\to I\) strongly give

\[
\|\Theta_l(x)\circ(b\mapsto e_i b e_i)-\Theta_l(x)\|
\longrightarrow0.
\tag{WH.54}
\]

Indeed each summand's error, uniformly for \(\|b\|\leq1\), is at most
\(\|e_i\eta_j-\eta_j\|\,\|\xi_j\|
+\|\eta_j\|\,\|e_i\xi_j-\xi_j\|\), using \(\|e_i\|\leq1\).
Thus \(T_i(x)\to\Theta_l(x)\) in predual norm for every \(x\in\mathfrak m_l\). For each fixed positive matrix \(X\) with entries in \(\mathfrak m_l\) and each positive \(B\), its finite scalar matrices in the preceding test converge entrywise to the test matrix for \(\Theta_l\). Positivity is closed in a finite-dimensional matrix space. This proves complete positivity of \(\Theta_l\).

**Proof of the range identities.** Every \(x\in(\mathfrak m_l)_+\) has \(x^{1/2}=\lambda_\xi\) and

\[
\Theta_l(x)=\omega_\xi|_{M'},\qquad
\|x\|=\|\lambda_\xi\|^2.
\]

Conversely, every \(\xi\in\mathcal B_l\) gives
\(x=\lambda_\xi^*\lambda_\xi\in(\mathfrak m_l)_+\), with the same functional and norm identity. This proves both equalities in (WH.51), including the strict inequalities.

Finally apply the established proof to the opposite right Hilbert algebra \(\mathcal A_r^{\mathrm{op}}\). Its generated algebra is \(M'\), its completed left multiplication map is \(R\) on \(\mathcal B_r\), and its commutant is \(M\), as established in WH-03–04 and WH-12. Therefore (WH.49) becomes exactly (WH.50); its positivity and matrix tests give \(\Theta_r\), and (WH.51) gives the two claimed right-hand range identities. This proves all assertions in (WH.48–51). \(\square\)

The domains \(\mathfrak m_l,\mathfrak m_r\) need not be norm closed, and no bounded extension of \(\Theta_l,\Theta_r\) to the entire algebras is asserted. Their complete positivity means exactly the finite matrix tests above. Together with WH12, this proves the predual-map and functional-cone statements compared with Nelson, Lemma 4.2 and Corollary 4.3. The construction of the weights precedes these maps.
