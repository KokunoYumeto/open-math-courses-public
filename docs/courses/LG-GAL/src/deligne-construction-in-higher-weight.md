# Deligne's construction in higher weight and the Ramanujan–Petersson bound

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A weight-two cusp form contributes to the first cohomology of a modular curve. Higher weight requires a coefficient system: the symmetric power of the first cohomology of the universal elliptic curve. Its parabolic cohomology retains the cusp forms and removes the contribution of the boundary. Deligne's construction turns a two-dimensional Hecke constituent of this cohomology into a Galois representation. The Weil theorem then controls its Frobenius eigenvalues.

Let \(f\) be a **normalized primitive cuspidal eigenform of exact level \(N\), weight \(k\geq2\), and Dirichlet character \(\chi\)**:

\[
f=\sum_{n\geq1}a_nq^n,\qquad a_1=1,\qquad
K=\mathbf Q(a_n,\chi(d):n\geq1,\ (d,N)=1).
\tag{1}
\]

Proposition 2.2 proves the number-field assertion under its stated geometric and comparison premises. Applying the modular law to \(-I\) gives \(f=\chi(-1)(-1)^kf\); since \(f\ne0\), this proves \(\chi(-1)=(-1)^k\). Definition (1) explicitly includes the character values. It agrees with the coefficient field defined using all the \(a_n\): the good-prime Hecke relation
\[
a_{p^2}=a_p^2-\chi(p)p^{k-1}
\tag{2}
\]
recovers \(\chi(p)\), and primes in every invertible residue class recover all character values.

Fix a finite place \(\lambda\mid\ell\) of \(K\). We use **arithmetic Frobenius** \(\operatorname{Fr}_p\), so the cyclotomic character satisfies \(\chi_\ell(\operatorname{Fr}_p)=p\) for \(p\ne\ell\). Geometric Frobenius is its inverse. Local reciprocity sends a uniformizer to geometric Frobenius; our Weil–Deligne convention is still \(r(w)Nr(w)^{-1}=|w|N\). The present lesson concerns good primes and does not use local–global compatibility at primes dividing \(N\).

## 1. The representation theorem

**Theorem 1.1 (Deligne; construction stated).** There is a continuous representation

\[
\rho_{f,\lambda}:G_{\mathbf Q}\longrightarrow
\operatorname{GL}_2(K_\lambda)
\tag{3}
\]

unramified outside \(N\ell\), such that for every prime \(p\nmid N\ell\),

\[
\det(X-\rho_{f,\lambda}(\operatorname{Fr}_p))
=X^2-a_pX+\chi(p)p^{k-1}.
\tag{4}
\]

It is irreducible over \(K_\lambda\). Its isomorphism class is determined by these good-prime polynomials.

We retain the full theorem, including its arbitrary character, coefficient field and irreducibility. The proof below constructs its coefficient space, supplies the cusp-product resolution and the passage through parabolic cohomology, and proves the ensuing algebraic deductions. Section 7 records the remaining proof obligations in the arithmetic moduli, congruence, comparison and irreducibility steps. Thus Theorem 1.1 is still a theorem whose complete proof is required in this edition; its freely accessible original source is evidence for its statement, not a replacement for those steps. Uniqueness, once existence and irreducibility are established, follows from the Frobenius-density and character proof in *Frobenius elements and determination by traces*.

The theorem is not restricted to a rational coefficient field or a trivial character. For general \(\chi\), complex conjugation of the modular form changes the character to \(\chi^{-1}\). Consequently the polarization argument for the totally real field in the previous lesson cannot simply be repeated without keeping track of these different constituents.

Write

\[
P_p(X)=X^2-a_pX+C_p,\qquad C_p=\chi(p)p^{k-1}.
\tag{5}
\]

Then the good Euler factor in the convention of *Compatible systems and global L-functions* is

\[
\det(1-\rho_{f,\lambda}(\operatorname{Fr}_p)T)^{-1}
=(1-a_pT+C_pT^2)^{-1}.
\tag{6}
\]

The polynomial belongs to \(K[X]\), independently of \(\lambda\). This is the good-prime compatibility assertion. It does not by itself describe the Euler factors at the finitely many bad primes.

## 2. The coefficient system and its two-dimensional constituent

For the geometric description suppose first that \(N\geq5\). The fine modular curve \(Y=Y_1(N)\) has a universal elliptic curve

\[
\pi:\mathcal E\longrightarrow Y.
\]

Its compactification \(X=X_1(N)\) has a finite nonempty cusp divisor \(D=X\setminus Y\). Set \(m=k-2\) and

\[
\mathcal F_\ell=R^1\pi_*\mathbf Q_\ell,\qquad
\mathcal L_m=\operatorname{Sym}^{m}\mathcal F_\ell.
\tag{7}
\]

The first sheaf is lisse of rank two; the second has rank \(m+1=k-1\). Smooth proper base change identifies its fibers with
\[
(\mathcal F_\ell)_{\bar y}=H^1(\mathcal E_{\bar y},\mathbf Q_\ell).
\tag{8}
\]
These are cohomology groups, rather than covariant Tate modules.

The relevant space is

\[
W_\ell=
H^1_{\mathrm{par}}(Y_{\overline{\mathbf Q}},\mathcal L_m)
:=\operatorname{im}\left(
H^1_c(Y_{\overline{\mathbf Q}},\mathcal L_m)
\longrightarrow H^1(Y_{\overline{\mathbf Q}},\mathcal L_m)\right).
\tag{9}
\]

This definition is essential. Cohomology with compact support alone can retain boundary eigenvalues of lower weight. For example, with constant coefficients on \(\mathbf G_m\), the localization sequence for \(\mathbf P^1\setminus\{0,\infty\}\) gives
\[
H^1_c(\mathbf G_m,\mathbf Q_\ell)
\simeq\operatorname{coker}\bigl(\mathbf Q_\ell
\longrightarrow\mathbf Q_\ell^2\bigr)\simeq\mathbf Q_\ell.
\]
Geometric Frobenius acts as \(1\) on this space. The map to ordinary first cohomology is zero, so its parabolic image is zero. Purity of weight one cannot be asserted for that compactly supported group.

A related boundary calculation occurs for the Legendre family over
\(U=\mathbf P^1_{\mathbf F_q}\setminus\{0,1,\infty\}\), with \(q\) odd and coefficient sheaf \(R^1\pi_*\mathbf Q_\ell\), \(\ell\nmid q\). With \(\varepsilon=(-1)^{(q-1)/2}\), the calculation is
\[
\#\mathcal E(\mathbf F_{q^n})=q^{2n}-q^n-1+\varepsilon^n,\qquad
\operatorname{tr}(F^n\mid H^1_c(U_{\overline{\mathbf F}_q},R^1\pi_*\mathbf Q_\ell))
=1+\varepsilon^n.
\]
Here \(\mathcal E\) means the total family, including the zero section. The second equality for every \(n\geq1\) determines its compact-support Euler polynomial: the identity
\(\log\det(1-FT)=-\sum_{n\geq1}\operatorname{tr}(F^n)T^n/n\)
gives \((1-T)(1-\varepsilon T)\). Thus the two eigenvalues are \(1,\varepsilon\). The sign is determined in the **base field**. For \(q=3\), the first two total-family counts are \(4,72\), the traces are \(0,2\), and the eigenvalues are \(1,-1\), even though \(-1\) becomes a square over \(\mathbf F_9\). Testing whether it is a square in one extension would not determine the base-field eigenvalues.

Here is the count itself. Put \(Q=q^n\), and extend the quadratic character \(\eta\) of \(\mathbf F_Q^\times\) by \(\eta(0)=0\). Each fiber has
\(Q+1+\sum_x\eta(x(x-1)(x-t))\) points. Since \(\sum_t\eta(x-t)=0\), summing over \(t\ne0,1\) gives
\[
\begin{aligned}
\sum_{t\ne0,1}\sum_x\eta(x(x-1)(x-t))
&=-\sum_{x\ne0,1}\bigl(\eta(x-1)+\eta(x)\bigr)\\
&=\eta(-1)+1.
\end{aligned}
\]
Thus the total is \((Q-2)(Q+1)+1+\eta(-1)=Q^2-Q-1+\varepsilon^n\). To identify the trace with a single compact-support group, put \(s=1/t\), \(x=u/s\), \(y=v/s^2\). The family at infinity becomes
\[
v^2=s\,u(u-s)(u-1).
\]
It is the quadratic twist by \(s\) of the parameter-\(s\) Legendre curve. That curve has \(\Delta=16s^2(1-s)^2\) and \(c_4=16(s^2-s+1)\), and over the geometric local field its node is split. The Tate uniformization and Kummer proof in *Elliptic curves over local fields*, Lemma 3.0 and Theorem 3.1, make its inertia unipotent. Since the characteristic is odd, adjoining \(\sqrt s\) is a ramified quadratic extension; an inertia element with quadratic value \(-1\) has, on the twist, the negative of a unipotent matrix. Its two eigenvalues are \(-1\), so it has no fixed vector in characteristic zero. There are consequently no global invariant vectors. Curve duality gives \(H_c^2(U,R^1\pi_*\mathbf Q_\ell)=0\), and \(H_c^0=0\) because a lisse section on this connected nonproper curve cannot have proper support. The curve trace formula therefore identifies the negative of the sum of fiber traces with \(\operatorname{Tr}(F^n\mid H_c^1)\); the point count just proved makes it \(1+\varepsilon^n\). The determinant logarithm proves the displayed degree-two polynomial, without a tame Euler-characteristic formula. The actual finite-coefficient curve trace proof is *The trace formula for curves*, Theorem 1.1 and §§2–5; the adic passage is *The trace formula in all dimensions*, Theorem 5.1. Its finite-cover and compact-support prerequisites retain their recorded scope. The free primary [Stacks calculation](https://stacks.math.columbia.edu/tag/03VA) is material for this example, not its vanishing proof.

The comparison and Eichler–Shimura theorems identify the corresponding complex parabolic cohomology with

\[
S_k(\Gamma_1(N))\oplus\overline{S_k(\Gamma_1(N))},
\qquad
\dim_{\mathbf Q_\ell}W_\ell=2\dim_{\mathbf C}S_k(\Gamma_1(N)).
\tag{10}
\]

Here the bar denotes the conjugate contribution under the compatible Hecke normalization, not an assertion that \(\chi\) is real. We prove the complex period map below. Lemma 2.4 reduces its comparison with the étale coefficient group to the preceding lesson's actual curve proofs, including the finite-cover argument. Exercise 8.4 computes the complex total dimension and keeps the remaining analytic Riemann–Roch foundations visible.

Hecke correspondences act on \(W_\ell\) and commute with Galois. On the constituent associated with \(f\), the good operators act by \(a_p\), and the normalized diamond action contributes \(\chi(p)\). Proposition 2.2 below proves the two-dimensionality and coefficient descent using **all** Hecke operators, including the bad operators, once the compatible arithmetic correspondences and comparison exist. A form viewed at a larger level can occur several times for the good operators alone: the whole oldform eigenspace must not be declared two-dimensional.

With this cohomological convention the arithmetic Galois representation in (3) is realized on

\[
V_{f,\lambda}=W_{f,\lambda}^{\vee}.
\tag{11}
\]

Indeed, if \(A\) is arithmetic Frobenius on \(W_{f,\lambda}\), then geometric Frobenius on it is \(A^{-1}\), while arithmetic Frobenius on its dual is \((A^{-1})^{\mathsf t}\). Thus these last two operators have the same characteristic polynomial. In particular, geometric Frobenius on the cohomological constituent and arithmetic Frobenius on (3) have the eigenvalues in (4).

No extra Tate twist is inserted into (11). There is a different, canonical two-dimensional identity

\[
V^\vee\simeq V\otimes(\det V)^{-1}.
\tag{12}
\]

The map sends \(v\) to the functional \(w\mapsto v\wedge w\), with values in \(\det V\), and is an isomorphism in any basis. After §5 identifies the determinant, (12) involves both \(\chi^{-1}\) and \(\chi_\ell^{1-k}\). Omitting the nebentypus in a self-duality assertion would change the representation.

At levels below five one uses a fine auxiliary cover and descent. The handling of its level action and the unramified assertion at primes not dividing \(N\ell\) belong to Theorem 1.1. The outline through a convenient cover does not supply these descent proofs.

### 2.1. The period map in every weight on a fine curve

**Lemma 2.1 (complex Eichler–Shimura mechanism).** Suppose \(N\ge5\). For the rank-\(m+1\) local system \(V_m=\mathbf C[X,Y]_m\), with
\(\rho(\gamma)P(v)=P(\gamma^{-1}v)\), the maps
\[
f\longmapsto f(z)(X-zY)^m\,dz,
\qquad
\bar g\longmapsto \overline{g(z)}(X-\bar zY)^m\,d\bar z
\]
give an injective map from \(S_k\oplus\overline{S_k}\) to complex parabolic cohomology. If the line-bundle dimension calculation in Exercise 8.4 is available, this map is an isomorphism. This includes odd \(k\).

*Proof.* The elementary identity
\(\rho(\gamma)(X-zY)^m=(cz+d)^m(X-\gamma zY)^m\), combined with \(d(\gamma z)=(cz+d)^{-2}dz\), makes these closed forms covariant. On the half-plane a closed coefficient form has a primitive: integrate first horizontally and then vertically, and differentiate, using \(\partial_yP=\partial_xQ\). Its period from \(z_0\) to \(\gamma z_0\) is therefore a cocycle. Changing \(z_0\) changes it by a coboundary.

At a cusp the Fourier expansion of a cusp form is bounded by \(Ce^{-ay}\); its polynomial coefficient adds at most \(C'(1+y)^m\). Integration to the cusp consequently converges. If \(b_P\) is that integral, a stabilizer element has period \(b_P-\rho(\gamma)b_P\); hence the class is parabolic. A primitive with limiting value zero is covariant in the cusp strip. Subtract the differential of that primitive times a height cutoff. The resulting form has compact support and the same period class.

On the basis \(e_r=X^{m-r}Y^r\), use the coefficient pairing
\[
B(e_r,e_s)=0\ (r+s\ne m),\qquad
B(e_r,e_{m-r})=(-1)^r\binom mr^{-1}.
\]
Expansion gives \(B((aX+bY)^m,(cX+dY)^m)=(ad-bc)^m\). Pure powers span, by the Vandermonde determinant, so \(B\) is invariant under \(\mathrm{SL}_2\) and is nondegenerate in every parity. Integrate \(B\) of the wedge of compact representatives. If a period class is zero, its closed form has a covariant primitive: subtract the constant giving its cocycle coboundary. The integral against a compact closed representative is then the integral of a differential and is zero. Green–Stokes here follows on rectangles from the fundamental theorem of calculus; paired sides of a truncated domain cancel, and the cusp boundary tends to zero by the preceding exponential estimate. Thus this pairing depends only on the classes.

Since \(B((X-zY)^m,(X-\bar zY)^m)=(2iy)^m\) and \(dz\wedge d\bar z=-2i\,dx\wedge dy\), the mixed pairing is
\[
-(2i)^{m+1}\int f(z)\overline{g(z)}y^m\,dx\,dy.
\]
The two same-type pairings vanish. The integral of \(|f|^2y^m\) is finite by the cusp estimate and positive for \(f\ne0\), since a continuous nonzero function is nonzero on a small disk. Pairing a vanishing class \([f+\bar g]\) first against \(\bar f\), then against \(g\), proves \(f=g=0\). No parity assumption occurred. Exercise 8.4 gives equal dimensions for domain and codomain, proving surjectivity when its Riemann–Roch premises are established. The actual earlier LG-MF period proof proves this cup argument, but its final theorem restricts odd weights; the argument above supplies the regular-cusp extension needed here. ∎

### 2.2. A full Hecke eigenspace and its coefficient field

**Proposition 2.2.** Assume that the fine modular curve and its universal family exist, that their rational Betti and étale parabolic cohomologies compare compatibly with all normalized Hecke and diamond correspondences, and that Lemma 2.1's dimension input is proved. The simultaneous eigenspace for the full system \((a_n,\chi(d))\) has dimension two over \(K\), and hence over each \(K_\lambda\). The field \(K\) is a number field. These claims do not require good-Hecke multiplicity one on the whole old space.

*Proof.* The coefficient formula from the earlier congruence-level Hecke lesson is
\[
a_r(T_nh)=\sum_{d\mid(r,n)}\chi_h(d)d^{k-1}a_{rn/d^2}(h),
\qquad a_1(T_nh)=a_n(h).
\]
For a simultaneous eigenvector with eigenvalues \(a_n\), it implies \(a_n(h)=a_n a_1(h)\). If \(a_1(h)=0\), every Fourier coefficient is zero, so \(h=0\); otherwise \(h=a_1(h)f\). Thus its holomorphic eigenspace is exactly one-dimensional, including at the bad operators.

Define \(f^*(z)=\overline{f(-\bar z)}\). The matrix \(J=\operatorname{diag}(-1,1)\) conjugates \(\Gamma_1(N)\) to itself. Applying the modular law to \(J\gamma J\) proves that \(f^*\) is a cusp form of character \(\bar\chi=\chi^{-1}\), with Fourier coefficients \(\bar a_n\). The same conclusion holds at every cusp, because reflection takes rational cusps and their vanishing expansions to rational cusps and vanishing expansions. The rational double-coset sets are stable under \(\delta\mapsto J\delta J\); equivalently the displayed coefficient formula conjugates. Therefore the antiholomorphic class associated with \(f^*\) has eigenvalues \(a_n,\chi(d)\), and its eigenspace is also one-dimensional. Lemma 2.1 gives dimension two.

There is a rational coefficient structure: integral polynomials with the integral \(\Gamma_1(N)\)-action define a local system on a finite surface cell complex; parabolic cohomology is the image of its relative-to-absolute cochain map. Tensoring that finite integral complex with \(\mathbf Q\) gives its rational structure. On a rational correspondence \(\delta\) of determinant \(n>0\), the coefficient map \(\rho(\delta)^{-1}\) is substitution by the integral matrix \(\delta\). Pullback followed by the finite-cover sum therefore preserves the integral cohomology image modulo torsion. On a holomorphic period form the formula is
\[
\rho(\delta)^{-1}\delta^*\bigl(h(z)(X-zY)^m dz\bigr)
=n^{k-1}(cz+d)^{-k}h(\delta z)(X-zY)^m dz.
\]
This is exactly \(n^{k/2-1}h\Vert_k\delta\) on the form coefficient. It verifies the normalization as well as rationality; no square root of \(n\) enters the cohomological matrix.

The commuting operators generate a finite-dimensional commutative \(\mathbf Q\)-algebra \(A\subset\operatorname{End}_{\mathbf Q}(W_B)\). Their eigenvalue system is a homomorphism \(A\to\mathbf C\). Its image is a finite-dimensional domain over \(\mathbf Q\), hence a field: multiplication by a nonzero element is an injective endomorphism of that finite vector space, and is surjective. The image is exactly \(K\), since it contains all \(a_n\) and the diamond values and is generated by them. The corresponding eigenspace is the intersection of kernels of matrices with entries in \(K\); a finite collection suffices because dimensions can decrease only finitely often. Matrix rank is unchanged by extending a field. Its complex dimension two is thus its dimension over \(K\), and compatible comparison gives the same dimension over \(K_\lambda\). Galois commutes with the arithmetic correspondences, so preserves those kernels. ∎

This proposition proves the coefficient and multiplicity steps under its specified geometric premises. It does not prove that the resulting Galois action is irreducible, nor its determinant or unramifiedness. Those are separate assertions of Theorem 1.1. For the character-field equality after (2), apply the earlier Frobenius-density theorem to the cyclotomic extension: the automorphism \(\zeta_N\mapsto\zeta_N^d\) occurs at a prime away from \(N\), and reduction of roots of unity identifies its arithmetic Frobenius with \(p\bmod N\). Thus (2) recovers every \(\chi(d)\) without assuming an additional prime-in-progression theorem.

**Lemma 2.3 (finite-cover descent).** Let \(Z\to Y\) be a finite étale Galois cover with finite group \(G\), and \(\mathcal L\) a characteristic-zero coefficient local system on \(Y\). Pullback identifies its ordinary, compact and parabolic cohomologies with the \(G\)-invariants of the corresponding cohomologies of the pulled-back system on \(Z\). These identifications respect commuting Galois and correspondence actions.

*Proof.* On a geometric stalk, the pushforward of the pulled-back system is a direct sum indexed by the finite fiber. Its \(G\)-invariant vectors are the diagonal copy of the original stalk. Averaging \(e=|G|^{-1}\sum_{g\in G}g\) is an idempotent with that image. There are no higher direct images on a finite étale fiber, which is a finite set of separably closed points; finite proper base change gives the same assertion as sheaves. Ordinary and compact-support composition therefore compute upstairs cohomology as the cohomology of this pushforward. Splitting the sheaf by \(e\) splits its derived global sections, so its invariant cohomology is exactly downstairs cohomology. The compact-to-ordinary map commutes with \(e\); taking its image proves the parabolic assertion. All constructions use natural maps and the finite sum, hence commute with any compatible additional action. ∎

The lemma proves the averaging step of auxiliary-level descent. It requires an actual finite étale cover with descended coefficient system. The moduli at levels with stabilizers and their integral models are still required to realize that premise for every \(N\); an abstract finite group does not construct the auxiliary modular cover.

**Lemma 2.4 (reducing coefficient comparison to curve comparison).** Once the fine curve and elliptic family are constructed, degree-one ordinary, compact and parabolic comparison for \(\mathcal L_m\) reduces to constant-coefficient comparison for smooth projective curves and their finite correspondences. In particular it uses no higher-dimensional comparison theorem for the total elliptic surface. The actual curve comparison proofs are Lemmas 1.2 and 1.4 of *Modular curves and the Eichler–Shimura congruence*: the latter includes algebraically closed field extension, while the former retains its analytic Riemann–Roch foundations.

*Proof.* Fix \(A=\mathbf Z/\ell^r\). Elliptic Kummer identifies \(R^1\pi_*A\) with the dual of the finite locally free torsion system; this is the natural degree-one identification in the earlier elliptic lesson. The torsion-basis cover is finite étale, by the relative multiplication proof and the basis-locus construction in the earlier modular lesson, Lemma 1.0. The full torsion-basis cover \(Z\to Y\) is a torsor for the finite group \(G=\operatorname{GL}_2(A)\): changes of basis act freely and transitively on every fiber. It may be disconnected. On it the symmetric-power coefficient system is the constant free \(A\)-module \(M\), with descent action of \(G\).

Normalize the projective completion of \(Y\) in each component function field of \(Z\). It is finite by the trace-dual-lattice normalization proof in the modular lesson, Lemma 1.2; in characteristic zero its normal curve is smooth. Thus \(Z=\bar Z\setminus B\), with \(\bar Z\) smooth projective and \(B\) finite. The closed–open and curve Gysin sequences determine its constant-coefficient groups in degrees zero and one from those of \(\bar Z\), the point modules of \(B\), and their degree maps. Constant comparison on \(\bar Z\), with trace and cup normalization, preserves all these maps. It consequently compares ordinary and compact degree-one groups on \(Z\) as well. This applies both to algebraically closed field extension and to complex analytification; on the analytic side the same boundary maps are the oriented small-circle maps.

Here is descent with finite coefficients, where dividing by \(|G|\) would be invalid. The augmented Čech complex for the cover is exact on every geometric stalk: choose one lift of that stalk and insert it as first coordinate to obtain the contracting homotopy. Its \(p\)-fold intersections are disjoint copies of \(Z\) indexed by \(G^p\). Apply ordinary cohomology to this resolution. The resulting double complex is the group-bar complex of the cohomology complex of \(Z\), tensored with \(M\). Tensoring is exact because \(M\) is free over \(A\). Filtering gives
\[
H^p\bigl(G,H^q(Z,A)\otimes_A M\bigr)
\Longrightarrow H^{p+q}(Y,\mathcal L_{m,A}).
\]
The comparison maps identify the rows \(q=0,1\). In total degree one the only other datum is the differential from \(H^0(G,H^1)\) to \(H^2(G,H^0)\); the same bar double-complex map preserves it. Its kernel and the group \(H^1(G,H^0)\) therefore identify the two degree-one abutments. With compact support the cover is finite proper, so the identical Čech argument applies to compact cohomology. Here \(H_c^0(Z,A)=0\), and degree one is simply \((H_c^1(Z,A)\otimes_A M)^G\). The compact-to-ordinary maps commute with the comparison, proving the parabolic assertion.

The finite-coefficient cohomology groups are finite by the earlier curve finiteness proof. Their inverse systems are Mittag–Leffler: at each fixed finite group the descending sequence of images stabilizes. Compatible inverse limits therefore have no extra degree-one \(\varprojlim^1\) term; after tensoring with \(\mathbf Q_\ell\) they give the stated coefficient comparison. The finite Betti cell complexes give the same limit. Pullback and trace are natural throughout. For a coefficient correspondence take a common torsion-basis cover on its parameter curve; there its coefficient map is a constant module map and its geometric maps are finite curve maps. The earlier curve comparison preserves those maps and their traces, so the descended comparison preserves the normalized Hecke and diamond actions whenever those correspondences have actually been constructed. On the uniformizing half-plane, the elliptic fibers are \(\mathbf C/(\mathbf Z+z\mathbf Z)\); their torsion coordinates identify this compared system with the polynomial local system of Lemma 2.1. This proves the reduction, with its geometric and analytic foundations still explicit. ∎

## 3. What the congruence relation does imply

On the properly normalized \(f\)-constituent, the higher-weight congruence relation has the form

\[
F+C_pF^{-1}=a_pI,
\qquad
F^2-a_pF+C_pI=0.
\tag{13}
\]

For cohomology, \(F\) means geometric Frobenius; on the dual representation it means arithmetic Frobenius. The construction supplies the appropriate Hecke and diamond normalization. See [Deligne 1969, Proposition 4.8 and Theorem 4.9]. Formula (13) is an **annihilating relation**. Its conversion to a characteristic polynomial requires retaining more information.

**Proposition 3.1 (corrected characteristic-polynomial deduction).** Let \(V\) be two-dimensional over a field \(E\) of characteristic zero. Let \(F\in\operatorname{GL}(V)\), \(a\in E\), and \(C\in E^\times\). Suppose

\[
F+CF^{-1}=aI,\qquad \det F=C.
\tag{14}
\]

Then
\[
\det(X-F)=X^2-aX+C.
\tag{15}
\]
Alternatively, the first assumption alone suffices if \(F\) is not scalar.

*Proof.* Multiplication by \(F\) gives \(F^2-aF+CI=0\). Cayley–Hamilton, with \(t=\operatorname{tr}F\), gives \(F^2-tF+CI=0\) under the determinant assumption. Subtraction gives \((t-a)F=0\). Since \(F\) is invertible, \(t=a\), proving (15), including when \(F\) is scalar.

Without the determinant assumption, suppose \(F\) is nonscalar. Its minimal polynomial cannot have degree one. It therefore has degree two and equals its monic degree-two characteristic polynomial. The displayed monic annihilating polynomial must equal that minimal polynomial. This proves the alternative. ∎

Both the dimension and the missing determinant matter. For a concrete counterexample to the deduction without that determinant, take

\[
F=2I_2,\qquad a=1,\qquad C=-2.
\tag{16}
\]

Then \(F+CF^{-1}=I_2\), but
\[
\det(X-F)=(X-2)^2\ne X^2-X-2.
\]
This relation has the modular size and sign \(C=\chi(2)2^{k-1}\) when \(k=2\) and \(\chi(2)=-1\), although the example is only a linear-algebra example, not a claimed modular constituent.

For the actual representation, the local determinant \(C_p\) is a separate part of the construction. Proposition 3.1 proves the algebraic passage once it is available. The arbitrary-character determinant proof is still required: a cup pairing pairs a \(\chi\)-constituent with a \(\chi^{-1}\)-constituent, so the trivial-character weight-two pairing does not prove it. In particular, neither the relation (13) nor two-dimensionality alone fills that gap.

**Lemma 3.2 (Fricke covariance and its determinant consequence).** Suppose the fine arithmetic family and its cyclic-isogeny correspondences have been constructed. Fix \(\zeta_N\), a primitive \(N\)-th root of unity, over \(\mathbf Q(\zeta_N)\). The Fricke correspondence takes \((E,P)\) to \((E/\langle P\rangle,\phi Q)\), where \(e_N(P,Q)=\zeta_N\). Its coefficient pullback gives an invertible operator \(w\) on parabolic cohomology. Write \(B\) for the cup pairing from the symmetric-power Weil pairing, valued in \(\mathbf Q_\ell(1-k)\). Then
\[
w^2=(-N)^m,\qquad B(wx,wy)=N^mB(x,y),\qquad
\Psi(x,y):=B(x,wy)
\]
defines a nondegenerate alternating pairing on the full parabolic space. If its restriction to the two-dimensional \(f\)-space is nondegenerate, then
\[
\det W_{f,\lambda}=\chi_G^{-1}\chi_\ell^{1-k},
\qquad
\det V_{f,\lambda}=\chi_G\chi_\ell^{k-1}.
\]
The nondegeneracy of that **restricted** pairing is a separate primitive-factor assertion.

*Proof.* The point \(\phi Q\) is independent of the choice of \(Q\): the choices differ by multiples of \(P\). It has exact order \(N\), since \((P,Q)\) is a basis of \(E[N]\). The dual isogeny has kernel generated by \(\phi Q\). To compute the second Fricke point, take \(R\in E[N^2]\) with \([N]R=P\). Then \(\phi R\in E'[N]\), and the pairing-adjoint identity proved in the elliptic Tate-module lesson gives
\[
e_N^{E'}(\phi Q,\phi R)=e_N^E(Q,\widehat\phi\phi R)
=e_N^E(Q,P)=\zeta_N^{-1}.
\]
The next chosen point is therefore \(-\phi R\), whose image under \(\widehat\phi\) is \(-P\). Identifying the resulting marked curve with \((E,P)\) uses \([-1]\); the composite universal isogeny is \([-N]\). On the symmetric-power coefficients it acts as \((-N)^m\), proving the first identity. This works for composite \(N\) as well as prime \(N\), since all torsion here is in characteristic zero.

An isogeny of degree \(N\) multiplies the rank-two cohomological alternating pairing by \(N\), by the Weil-pairing adjoint formula. Its \(m\)-th symmetric-power coefficient pairing is therefore multiplied by \(N^m\). The base Fricke map is an isomorphism of the smooth curve, so preserves its degree-two trace. This proves the second identity on the parabolic cup pairing. The parity of \(B\) is \((-1)^{m+1}\): the coefficient pairing has parity \((-1)^m\) and exchanging two degree-one classes adds a minus sign. The adjoint of \(w\) is
\(w^\dagger=N^m w^{-1}=(-1)^m w\). Consequently
\[
\Psi(y,x)=(-1)^{m+1}B(wx,y)
=(-1)^{m+1}B(x,w^\dagger y)=-\Psi(x,y).
\]
In characteristic zero skew symmetry implies alternation. Perfectness of \(B\) and invertibility of \(w\) prove perfectness of \(\Psi\) on the full space.

If \(\sigma(\zeta_N)=\zeta_N^u\), transport of the defining point condition gives
\(\sigma w_N\sigma^{-1}=\langle u\rangle w_N\). Indeed \(\sigma Q\) pairs to \(\zeta_N^u\); after choosing a point pairing to \(\zeta_N\), its image in the quotient is \(u\) times that point. Also \(w_N\langle d\rangle=\langle d^{-1}\rangle w_N\), directly from replacing \(P\) by \(dP\). On cohomology pullback reverses composition, so the covariance is \(\sigma w\sigma^{-1}=w\langle u\rangle^*\). On the \(\chi\)-eigenspace this gives
\[
\Psi(\sigma x,\sigma y)
=\chi(u)^{-1}\chi_\ell(\sigma)^{1-k}\Psi(x,y).
\]
For a nondegenerate alternating form on a two-dimensional space, the multiplier of a matrix is its determinant: expand \(B(Ae_1,Ae_2)\) in a basis. This proves the two determinant formulas, the second by dualizing. No restriction of a globally perfect form to an arbitrary eigenspace is automatically perfect; a commuting algebra with a nilpotent operator can have an isotropic eigenline. That is why the primitive-factor premise has been retained. ∎

## 4. Why the Frobenius eigenvalues have the right size

For a smooth projective variety over \(\mathbf F_p\), the full Weil assertion is that every eigenvalue of geometric Frobenius on \(H^n\) is algebraic and has absolute value \(p^{n/2}\) under every complex embedding. The original proof is freely accessible in [Deligne, *La conjecture de Weil I*](https://www.numdam.org/item/PMIHES_1974__43__273_0/), §§3–7. The following argument proves its tensor estimate and removes two auxiliary proof inputs from the earlier trace-formula exposition. The full projective assertion still requires the geometric pencil and vanishing-cycle steps identified after Lemma 4.0C. We retain its full scope rather than treating the theorem statement as an earlier proof.

### 4.0. The tensor estimate and the remaining projective step

**Lemma 4.0A (similitudes on tensor coinvariants).** Let \(V\) be a nonzero symplectic space over a characteristic-zero \(\ell\)-adic field. Let \(G\) be an open subgroup of \(\operatorname{Sp}(V)\), and let \(A\) be a symplectic similitude of multiplier \(\mu\). On the coinvariants of \(V^{\otimes2h}\) under \(G\), \(A\), when it normalizes \(G\), acts by the scalar \(\mu^h\).

*Proof.* An open subgroup is Zariski dense in \(\operatorname{Sp}(V)\). Here is the needed density check. In a symplectic basis the open cell with invertible upper-left block has coordinates
\[
\begin{pmatrix}I&0\\C&I\end{pmatrix}
\begin{pmatrix}B&0\\0&B^{-\mathsf t}\end{pmatrix}
\begin{pmatrix}I&D\\0&I\end{pmatrix},
\qquad B\in\operatorname{GL}_r,\quad C=C^{\mathsf t},\ D=D^{\mathsf t}.
\]
Its entries and inverse coordinates are rational functions with denominators powers of \(\det B\). A polynomial vanishing on an \(\ell\)-adic ball in these coordinates is zero: vary one coordinate through infinitely many values, and induct on the number of coordinates. This cell is dense in the symplectic group. To check this last fact without a component assumption, the group acts transitively on symplectic bases by the successive choices of a nonzero vector, a vector pairing to one with it, and a symplectic basis of their complement. These parameter spaces are irreducible open vector spaces or affine bundles; induction gives irreducibility. Thus any open subgroup meeting the identity cell is dense. Invariant linear forms on the tensor space consequently have the same invariants under \(G\) and the full symplectic group; dualizing gives the same coinvariants.

Extend scalars to contain \(c\) with \(c^2=\mu\). Then \(c^{-1}A\) is symplectic and acts identically on those coinvariants. The scalar \(c\) acts on the \(2h\)-fold tensor by \(c^{2h}=\mu^h\). Descend the equality of linear maps to the original field. This uses no assertion about a basis of invariant contractions. ∎

**Lemma 4.0B (fundamental estimate).** Let \(U_0\) be a nonempty open of \(\mathbf P^1_{\mathbf F_q}\), and \(\mathcal V_0\) a lisse \(\mathbf Q_\ell\)-sheaf, \(\ell\nmid q\). Suppose it has a perfect alternating pairing into \(\mathbf Q_\ell(-b)\), open geometric symplectic monodromy, and rational local characteristic polynomials. Then every local eigenvalue is algebraic and every complex conjugate at a closed point \(x\) has modulus \(q_x^{b/2}\).

*Proof.* Fix the point being tested. Removing a different point makes \(U_0\) affine, and preserves geometric monodromy: a connected cover stays connected on a dense open. Write \(d_x=[\kappa(x):\mathbf F_q]\). Rational characteristic polynomials and Newton's identities give rational traces \(s_{x,n}=\operatorname{Tr}(F_x^n\mid\mathcal V_{0,x})\). On \(\mathcal T_h=\mathcal V_0^{\otimes2h}\) the trace is \(s_{x,n}^{2h}\ge0\). Hence
\[
f_{x,h}(t)=\det(1-F_xt^{d_x}\mid\mathcal T_{h,x})^{-1}
=\exp\left(\sum_{n\ge1}\frac{s_{x,n}^{2h}}n t^{nd_x}\right)
\]
has nonnegative rational Taylor coefficients. There are finitely many points of bounded degree, so \(L_h=\prod_x f_{x,h}\) is a defined formal series with the same property, and the coefficient of any single factor is at most that of \(L_h\).

The curve trace formula expresses
\[
L_h(t)=\frac{\det(1-Ft\mid H_c^1(U,\mathcal T_h))}
{\det(1-Ft\mid H_c^2(U,\mathcal T_h))}.
\]
There is no \(H_c^0\): a nonzero locally constant section on a connected affine curve has support the whole nonproper curve. Curve duality gives
\(H_c^2(U,\mathcal T_h)=(\mathcal T_{h,u})_{\pi_1(U)}(-1)\). A linear geometric Frobenius operator on the coefficient space has multiplier \(q^b\). Lemma 4.0A therefore makes its top-degree action the scalar \(q^{bh+1}\). The only possible poles of \(L_h\) are at \(t=q^{-bh-1}\). Its numerator is rational: multiply the rational formal series \(L_h\) by the rational denominator; the result is a polynomial with those rational Taylor coefficients. Thus we may take its complex Taylor radius, which is at least \(q^{-bh-1}\).

Nonnegative coefficient domination implies that every \(f_{x,h}\) has radius at least this value. If \(\alpha\) is an eigenvalue of \(F_x\), then \(\alpha^{2h}\) is an eigenvalue on \(\mathcal T_{h,x}\), so that local factor has a pole of modulus \(|\alpha|^{-2h/d_x}\). Its numerator is one and no such pole cancels. Consequently
\[
|\alpha|\le q_x^{b/2+1/(2h)}.
\]
The local polynomials are rational, so the argument applies to every conjugate of \(\alpha\). Let \(h\to\infty\). The pairing makes \(q_x^b/\alpha\) another eigenvalue: in a matrix, \(A^{\mathsf t}\Psi A=q_x^b\Psi\), so \(A\) is similar to \(q_x^b A^{-\mathsf t}\). Applying the upper bound to this eigenvalue gives the matching lower bound. This proves the lemma. ∎

**Lemma 4.0C (parabolic bound and power removal).** Under Lemma 4.0B, an eigenvalue \(\alpha\) on parabolic \(H^1(U,\mathcal V)\) is algebraic and satisfies
\[
q^{b/2}\le |\alpha|\le q^{b/2+1}
\]
under every complex embedding. Moreover, suppose the even-dimensional middle-cohomology estimate
\[
q^{d/2-1/2}\le |\alpha|\le q^{d/2+1/2}
\tag{4.0}
\]
has been proved for every smooth projective geometrically irreducible variety of even dimension \(d\). Then the full Weil assertion follows in every dimension and degree.

*Proof.* The symplectic representation has no fixed vectors, since the full symplectic group contains \(-I\) and the coefficient characteristic is zero. Thus \(H_c^2(U,\mathcal V)=0\). The trace formula gives \(L(U_0,\mathcal V_0,t)=\det(1-Ft\mid H_c^1)\), a rational polynomial. Its Euler product converges absolutely and is nonzero for \(|t|<q^{-b/2-1}\): there are at most \(q^d+1\) closed points of degree \(d\), each local eigenvalue has modulus \(q^{db/2}\), and the resulting geometric series converges. Its roots consequently yield the upper bound on \(H_c^1\), and hence on its parabolic image.

For the lower bound we need only ordinary curve duality, not a separately stated \(j_*\)-duality theorem. It pairs \(H_c^1(U,\mathcal V)\) with \(H^1(U,\mathcal V)\), with target \(\mathbf Q_\ell(-b-1)\). The map \(J:H_c^1\to H^1\) is self-adjoint up to the coefficient and degree signs, by the cup product. Therefore \(\ker J\) is the annihilator of \(\operatorname{im}J\): pair against all compact classes and use perfect duality. The induced pairing on its image is perfect. Frobenius eigenvalues on that image occur in pairs \(\alpha,q^{b+1}/\alpha\). The upper bound for the latter gives the lower bound for the former. Equivalently this image is \(H^1(\mathbf P^1,j_*\mathcal V)\): the quotient \(j_*\mathcal V/j_!\mathcal V\) is punctual, so compact \(H^1\) surjects onto it, while the degree-one edge map \(H^1(j_*\mathcal V)\to H^1(U,\mathcal V)\) is injective.

Now let \(X\) have any dimension \(d\), and let \(\alpha\) act on its middle cohomology. For every positive even integer \(h\), Künneth puts \(\alpha^h\) in the middle cohomology of \(X^h\), of even dimension \(hd\). The algebraicity of \(\alpha^h\) implies that of \(\alpha\), by the equation \(Z^h-\alpha^h=0\). Applying (4.0), taking \(h\)-th roots and then letting \(h\to\infty\) gives \(|\alpha|=q^{d/2}\) under all embeddings. Finite extension of the base field replaces \(q,\alpha\) by \(q^a,\alpha^a\), so the conclusion descends. Components can be made geometrically irreducible after such an extension; Frobenius before extension permutes them and its powers give the same modulus.

Finally weak Lefschetz reduces degree \(i<d\) to a smooth projective section of dimension \(i\), by successive injections (and isomorphisms until the last section). Duality reduces \(i>d\) to \(2d-i<d\). The needed weak Lefschetz range has an actual proof in the earlier smooth-duality lesson, Solution 5: the hyperplane complement is affine, affine vanishing and duality give \(H_c^r=0\) for \(r<d\), and the closed–open sequence gives the stated injections. These steps prove every degree once (4.0) is proved. ∎

The unresolved portion is **(4.0)**. The actual earlier trace-formula lesson, *The Riemann hypothesis over finite fields*, §§2–6, proves its rationality and three-term Leray reduction from a Lefschetz pencil, including the case where the nonzero vanishing cycles all lie in the radical. Its pencil lesson explicitly imports three geometric inputs: existence of the pencil, the general étale Picard–Lefschetz sequence, and the global assertions that the local inertia images generate monodromy and that the signed vanishing cycles are conjugate. Those are geometric proof obligations, not supplied by the tensor argument above. Rationality also uses the curve bound for covering curves and their twists, which Lemma 4.0D supplies below. The nodal resolution proved below supplies the Kuga–Sato compactification; it does not supply these arbitrary-dimensional pencil inputs.

The constant-coefficient curve trace identity required below is constructed in §§4.0C.1–6. We use the actual earlier curve duality, proper base change and proper-factor Künneth proofs. The product trace is constructed from the curve traces; the normal-coordinate calculation supplies the required divisor orientation. Higher cohomological continuity, which the earlier direct-image lesson imports, remains an explicit foundational proof obligation. The argument below records each use of it.

### 4.0C.1. Constant curve cohomology and its proof interfaces

Let \(C_0/\mathbf F_q\) be a smooth geometrically connected projective curve of genus \(g\), let \(k=\overline{\mathbf F}_q\), and put \(C=C_0\times k\). Fix \(\ell\nmid q\). We first work with \(A=\mathbf Z/\ell^r\), \(r\geq1\), and write \(A(1)=\mu_{\ell^r}\). Twists will be retained until a compatible system of roots is chosen for a finite linear-algebra calculation.

Here are the actual earlier interfaces used in this fragment.

1. *Pushforward, pullback and finite morphisms*, Lemma 6.1 and Theorem 6.2, proves topological invariance by its strictly henselian ring and stalk argument. Its Sections 2 and 5 supply the strict-local and closed-immersion functors. Localization with support is constructed from an injective resolution and sections supported on the closed set.
2. *The proper base change theorem*, Theorem 1.1, Sections 10--11 and Corollary 11.3, proves the canonical geometric-fibre comparison. No smooth-base-change theorem is an input. The pro-etale comparison needed below is proved directly by etale localization and the explicitly retained continuity prerequisite of *Pushforward, pullback and finite morphisms*, Section 2.
3. *Cohomological dimension and the Kunneth formula*, Lemma 8.4, Proposition 8.5 and Theorem 9.1, proves the tensor and proper-product comparisons with their actual external cup-product maps. We use one proper curve factor and a second curve factor, so the needed finite dimension bounds are the earlier curve bounds. Its Lemma 10.1 proves detection for bounded-below complexes supported on closed points. *Constructible sheaves*, Theorem 5.1 and Proposition 7.1, supplies the actually written Noetherian constructible-subobject proof used in that detection. The general open-product comparison of Theorem 10.2 is not imported: its field-extension input passes through smooth base change. The special coordinate comparison is proved below directly.
4. *Poincare duality for curves*, Section 2, Lemmas 4.1--4.2, Sections 8--11 and Section 12, proves the degree-normalized curve trace, point orientation and perfect curve cup pairing. Its degree-one proof uses the explicit finite-constant embeddings and effacement of Section 9 and the diagram chase of Section 10. Its separately stated comparison with a chosen Weil-pairing sign is not an input here.
5. *The Picard functor and the Picard scheme of a curve*, Theorem 2.1, Sections 4--6, Proposition 7.1 and Theorem 7.2, constructs the normalized Picard functor, its charts and the genus-\(g\) Jacobian. Over the algebraically closed \(k\), the chosen point of \(C\) permits the rigidification proof of Section 2; the section-free topology-comparison assertion of Section 3 is unnecessary. *Abelian varieties*, Theorems 6.1--6.2 and 7.1--7.2, proves multiplication, the prime-to-characteristic torsion ranks and their surjective transition maps.
6. *Brauer groups and Tsen's theorem*, Theorem 5.1, its following finite-coefficient-field paragraph and Corollary 6.1, proves the \(C_1\) and cohomological-dimension assertions for every transcendence-degree-one extension of the algebraically closed \(k\). *The multiplicative group on a curve*, Sections 4--6, proves the rational-units vanishing, divisor cocycles and Kummer degree calculation. The point calculation below can consequently use \(C_1\) directly.

Thus Kummer, the divisor degree sequence and those multiplication proofs give
\[
 H^0(C,A)=A,\qquad H^1(C,A)\simeq A^{2g},\qquad
 H^2(C,A(1))\xrightarrow[\deg]{\sim}A,
 \qquad H^i(C,A)=0\ (i>2).
 \tag{CT1}
\]
For precision, Kummer identifies \(H^1(C,A(1))\) with \(J\ell^r\), because constants have \(\ell^r\)-th roots and a torsion line bundle has degree zero. The proved multiplication theorem makes this group free of rank \(2g\). In degree two the earlier valuation-sequence and rational-units calculation identifies \(H^2(C,A(1))\) with \(\operatorname{Pic}(C)/\ell^r\). Multiplication on \(J(k)\) is surjective, so the degree map identifies this quotient with \(A\). A point has degree one and hence trace one. These explanations bind the stated Picard input of the older curve-cohomology exposition to the actual written Picard and multiplication proofs.

Kummer is available on the product as well: an \(n\)-th root of a unit is obtained on the finite etale cover defined by \(Z^n-u\), whose derivative is a unit when \(n\) is invertible. Its connecting map therefore defines the first Chern class of every line bundle used below. Cup products come from the coefficient multiplication and the derived tensor product. Exchanging homogeneous tensor factors of degrees \(a,b\) multiplies them by \((-1)^{ab}\); invariance of coefficient multiplication under that symmetry gives the graded commutativity used in the proof.

The curve pairing
\[
 H^i(C,A)\times H^{2-i}(C,A(1))
 \longrightarrow A,\qquad (a,b)\longmapsto\operatorname{tr}_C(a\cup b)
 \tag{CT2}
\]
is perfect by the inspected curve duality proof. All its groups are free. Consequently finite-coefficient Kunneth has no Tor terms for \(C\times C\). This assertion can also be checked directly: a bounded complex with free cohomology is quasi-isomorphic to the sum of its cohomology groups in their degrees, by lifting a basis of each group to cycles.

### 4.0C.2. The smooth-divisor orientation on the product

**Lemma 4.0C.2.** Let \(X/k\) be a smooth surface, let \(D\subset X\) be a smooth effective Cartier divisor, and write \(i:D\hookrightarrow X\), \(j:X-D\hookrightarrow X\). Curve orientation, etale excision and the coordinate calculation below give
\[
 Ri^!A=A_D(-1)[-2].
 \tag{CT3}
\]
The oriented map \(i_*A_D\longrightarrow A_X(1)[2]\) sends \(1\) to the Kummer class \(c_1(\mathcal O_X(D))\). It gives maps
\[
 i_*:H^a(D,A(b))\longrightarrow H^{a+2}(X,A(b+1))
 \tag{CT4}
\]
satisfying
\[
 i_*(u\cup i^*v)=i_*u\cup v.
 \tag{CT5}
\]

*Proof.* We first give the point calculation, then the product calculation and its etale excision. The result applies to the smooth surface \(C\times C\) and all its graph and diagonal divisors, for every curve in the stated scope.

Let \(i_0:\{0\}\hookrightarrow\mathbf A^1\) and \(j_0:\mathbf G_m\hookrightarrow\mathbf A^1\). The earlier point proof gives
\[
 Ri_0^!A=A(-1)[-2].
 \tag{CT6}
\]
Here is also a direct proof of that curve-trait calculation from the inspected \(C_1\) input. The strict henselization of a smooth curve local ring is a henselian DVR with residue field \(k\). Its fraction field \(L\) is algebraic over the curve function field, since its pointed etale neighbourhoods have finite separable generic extensions. Thus \(\operatorname{trdeg}_kL=1\). The proved Tsen/cohomological-dimension result gives \(H^a(L,A)=0\) for \(a>1\). Every unit of the henselian DVR has an \(\ell^r\)-th root: first take its residue root in \(k\), then lift the simple root of \(Z^{\ell^r}-u\), whose derivative is a unit. Kummer therefore identifies
\[
 H^1(L,A(1))=L^\times/L^{\times\ell^r}
 \xrightarrow[\operatorname{val}]{\sim} A.
\]
With its twist restored, \(H^1(L,A)=A(-1)\). The punctured-trait direct image has exactly these groups on its closed stalk; this follows from the actual strict-local higher-image formula. The localization triangle has middle term \(A\), and its map to the degree-zero group of that direct image is the identity. Its supported cone therefore has exactly \(A(-1)\) in degree two. Orient its Kummer boundary by valuation \(+1\). Changing a uniformizer by a unit leaves this class fixed. This proves (CT6) from curve and henselian calculations alone, with the same local conclusion as the earlier Lemma 4.2.

The same calculation proves the following *specific* field comparison. For an extension \(L/k\) of separably closed fields, the canonical comparison for \(j_0:\mathbf G_m\hookrightarrow\mathbf A^1\), with constant coefficient \(A\), is an isomorphism after base change to \(L\). Away from zero it is the identity. At zero its degree-zero map is the identity on \(A\), its degree-one map takes the Kummer generator \(t\) to the same valuation-one generator, and all higher groups vanish. If \(L\) is imperfect, pass to its algebraic closure: the extension is purely inseparable, so the actually proved topological invariance applies to both affine schemes and the canonical comparison. Over that algebraically closed field the preceding strict-trait and \(C_1\) calculation applies. Thus this special comparison is proved by stalks without a general field-extension base-change theorem.

Consider now \(B=\mathbf P^1\times\mathbf A^1\), with projection \(q:B\to\mathbf A^1\), and the open immersion \(h:\mathbf P^1\times\mathbf G_m\hookrightarrow B\). Let \(Q\) be the cone of the canonical map
\[
 q^{-1}Rj_{0,*}A\longrightarrow Rh_*A.
 \tag{CT6a}
\]
Off \(\mathbf P^1\times\{0\}\) this map is the identity. It is also an isomorphism at the points over the generic point \(\eta\) of \(\mathbf P^1\). Indeed its strict localization there is \(\operatorname{Spec}L\), where \(L=k(u)^{\mathrm{sep}}\). Restrict along this pro-etale map. At each pointed etale neighbourhood, higher images commute with that restriction by slice adjunction and the geometric-stalk formula (2.2) of the direct-image lesson. Passing to the affine limit uses precisely its cohomological-continuity prerequisite (2.3). The resulting comparison is the special \(j_0\) field comparison over \(L\), which was just proved. The exact inverse-image stalk formula detects every original stalk over \(\eta\). Consequently every cohomology sheaf of \(Q\) is supported on closed points of \(B\).

Here is the closed-point detection used at this step. On a Noetherian scheme a torsion sheaf supported on closed points is the filtered union of constructible subsheaves, by the actual subobject and approximation proofs of *Constructible sheaves*, Theorem 5.1 and Proposition 7.1. Each such subsheaf has finite support: a constructible set of closed points contains the generic points of its finitely many closure components; those components must therefore be points. It is exact closed pushforward from that finite set. Over the algebraically closed \(k\), sections on each of these points are exact and supply its stalk. Each finite-support subsheaf thus has zero higher cohomology and is generated by global sections. Qcqs cohomological continuity for filtered sheaves extends both assertions to their union. A bounded-below complex with such cohomology sheaves has hypercohomology spectral sequence with only column zero. Every total-degree diagonal is finite, and hence its global cohomology in degree \(a\) is \(\Gamma(B,H^a(Q))\). If these groups all vanish, global generation makes every cohomology sheaf zero. This is the proof at the needed bounded-below scope of the inspected Lemma 10.1; it requires no higher-dimensional trace or smooth base change.

The canonical proper-factor Kunneth maps compute the two global-section complexes in (CT6a) as
\[
 \begin{aligned}
 R\Gamma(B,q^{-1}Rj_{0,*}A)
 &\simeq R\Gamma(\mathbf P^1,A)\otimes_A^L
             R\Gamma(\mathbf A^1,Rj_{0,*}A),\\
 R\Gamma(\mathbf P^1\times\mathbf G_m,A)
 &\simeq R\Gamma(\mathbf P^1,A)\otimes_A^L
             R\Gamma(\mathbf G_m,A).
 \end{aligned}
 \tag{CT6b}
\]
These are exactly Theorem 9.1 with one proper curve factor; its tensor argument uses only the known finite cohomological dimensions of the curves here. Derived composition identifies \(R\Gamma(\mathbf A^1,Rj_{0,*}A)\) with \(R\Gamma(\mathbf G_m,A)\). The counits defining the external products show that (CT6a) induces the identity under these identifications. Thus \(R\Gamma(B,Q)=0\), and the preceding detection gives \(Q=0\).

Restrict this comparison to the affine open \(\mathbf A^1\times\mathbf A^1\). The localization triangle for \(\{0\}\subset\mathbf A^1\), pulled back by its coordinate projection, now identifies the supported complex for the coordinate line with \(A_{\mathbf A^1}(-1)[-2]\). Its orientation is the Kummer boundary of the first coordinate. This proves the coordinate-divisor calculation from the point calculation and proper-factor Kunneth.

Finally, locally near a point of \(D\), choose an equation \(t\) for it and a second function \(u\) whose differential is nonzero along \(D\). The smooth-coordinate criterion makes \((t,u):X\to\mathbf A^2\) etale on a neighbourhood: their two differentials give an invertible minor in a standard smooth presentation. This is the criterion actually proved in *Formally smooth, unramified and etale ring maps*, Theorems 3.1, 4.1 and 5.1, and *Smooth algebras over a field and the Jacobian criterion*, Theorem 2.1. Such neighbourhoods around closed points cover \(D\); any nonempty omitted locus of this finite-type curve would contain a closed point.

Etale excision identifies the pulled-back coordinate localization triangle with that for \(D\). This particular base change is formal: the pointed etale neighbourhoods of an etale \(V\to Z\) at \(\bar v\) and those of \(Z\) at its image have cofinal common refinements, obtained by their fibre products with \(V\) and the chosen lift. Their strict localizations are canonically isomorphic, and so are the complements of the pulled-back divisor. Equivalently, apply the direct-image presheaf/stalk formula (2.2) to these cofinal categories; slice restriction preserves acyclicity. This proves the canonical etale comparison for the open direct images, and closed direct image commutes by its stalk formula. It proves (CT3). The orientation is the boundary of the pulled-back normal coordinate. If \(t'=vt\) is another equation, the Kummer difference is the class of a unit extending across \(D\), so its localization boundary is zero. The local rank-one orientations consequently glue.

Here is the sign of the supported Kummer class explicitly. Use the divisor-cocycle convention of *The multiplicative group on a curve*, Section 5: local rational lifts of a divisor have transition \(f_j/f_i\), so the divisor connecting map is \(D\mapsto[\mathcal O_X(-D)]\). If \(b(t)\in H^1_D(X,\mathbf G_m)\) is the localization boundary of the normal parameter, its image therefore represents \(\mathcal O_X(-D)\). The framed bundle \((\mathcal O_X(D),1)\) gives the supported class \(-b(t)\): its local frame is \(t^{-1}\).

The Kummer and localization connecting maps anticommute. This follows on their double complex: the second differential on a row of cohomological degree \(a\) is multiplied by \((-1)^a\), so exchanging the two degree-one boundaries contributes \(-1\). If \(\kappa(t)\in H^1(X-D,A(1))\) is the Kummer class of the normal parameter, the supported Kummer class of \((\mathcal O_X(D),1)\) is consequently
\[
 \partial_{\mathrm{Kum},D}(-b(t))
 =-\partial_{\mathrm{Kum},D}\partial_{\mathrm{loc},\mathbf G_m}(t)
 =\partial_{\mathrm{loc},A(1)}\kappa(t).
 \tag{CT3a}
\]
The last class is the valuation-\(+1\) orientation above. Forgetting support gives \(c_1(\mathcal O_X(D))\). This proves the positive sign with the actual divisor-cocycle convention. In particular it supplies the required normalization without adopting the inaccurate intermediate sentence in the older point proof that calls its divisor connecting map \(D\mapsto\mathcal O_X(D)\). Naturality of the cochains under the smooth normal-coordinate map and their unit invariance prove the same identification on all overlaps.

Transposing the oriented identification (CT3) under the closed-immersion adjunction supplies the map in (CT4). The closed projection formula is particularly elementary: on a stalk in \(D\), \(i_*M\otimes N\) is \(M\otimes i^*N\); outside \(D\) both sides are zero. Applying this identity to flat resolutions gives its derived version. Cup with the oriented supported class then gives (CT5), or equivalently the same equality follows by adjunction and associativity of evaluation. This proves all assertions. \(\square\)

The coordinate argument uses the earlier proper-factor Kunneth proof and the written Noetherian constructible-subobject proof. It supplies the needed codimension-one orientation without using the general smooth-base-change theorem.

### 4.0C.3. A product trace and the graph normalization

Put \(S=C\times C\), with projections \(p_1,p_2\). Kunneth gives
\[
 H^4(S,A(2))=H^2(C,A(1))\otimes_A H^2(C,A(1)).
\]
Define
\[
 \operatorname{tr}_S=\operatorname{tr}_C\otimes\operatorname{tr}_C.
 \tag{CT7}
\]
The perfect pairings (CT2) and Kunneth also make the corresponding product pairings perfect; their tensor multiplication has the usual graded sign. This defines all product normalizations used below directly from curves.

**Lemma 4.0C.3.** For every section \(s:C\to S\) of \(p_1\), its oriented map from Lemma 4.0C.2 satisfies
\[
 \operatorname{tr}_S(s_*w)=\operatorname{tr}_C(w)
 \quad(w\in H^2(C,A(1))).
 \tag{CT8}
\]
In particular, if \(D=s(C)\), then
\[
 \operatorname{tr}_S\bigl(c_1(\mathcal O_S(D))\cup v\bigr)
 =\operatorname{tr}_C(s^*v)
 \quad(v\in H^2(S,A(1))).
 \tag{CT9}
\]

*Proof.* Let \(K=R\Gamma(C,A)\). Canonical proper base change for the product identifies
\(Rp_{1,*}A_S\) with the constant complex \(\underline K\). The curve trace on \(R\Gamma(C,A(1))[2]\) therefore supplies an actual morphism
\[
 T_{p_1}:Rp_{1,*}A_S(1)[2]\longrightarrow A_C.
 \tag{CT10}
\]
It is the constant curve trace on the second factor. Its composite with the trace on the first factor is exactly (CT7), by the external-product construction of Kunneth.

Since \(p_1s=\mathrm{id}\), push the oriented map of the section along \(p_1\) and compose with (CT10). This gives a morphism
\[
 A_C\longrightarrow Rp_{1,*}A_S(1)[2]
 \xrightarrow{T_{p_1}}A_C.
 \tag{CT11}
\]
It is the identity. To check this, use the canonical geometric-stalk proper-base-change comparison. On the fibre over \(x\), the section cuts out one reduced point of \(C\). The image of \(1\) is the Kummer class of that point, which has degree and trace one by (CT1). The composite (CT11) is a map between degree-zero sheaves, so its identity on every stalk proves its identity as a morphism. This argument checks an actual map, not only equality of the dimensions of its source and target.

Taking degree-two cohomology of (CT11) after a twist and using the trace on the base gives (CT8). Lemma 4.0C.2 gives \(c_1(\mathcal O_S(D))=s_*1\) and the projection formula. Apply (CT8) to \(w=s^*v\) to obtain (CT9). Both the diagonal and every graph \((\mathrm{id},h)\) are such sections. A graph meets a vertical fibre transversely, even when \(h\) is inseparable: its first projection is the identity and its normal equation has derivative one in the fibre direction. Thus the degree-one fibre calculation used in (CT11) includes every Frobenius graph. \(\square\)

### 4.0C.4. The signed diagonal and the fixed-point formula

Choose compatible primitive roots only to write the twists as copies of \(A\) during the following calculation. Let \(e_{i,j}\) be a basis of \(H^i(C,A)\), and let \(e_{i,j}^{\vee}\) be its **right** dual for (CT2):
\[
 \operatorname{tr}_C(e_{i,j}\cup e_{i,j'}^{\vee})=\delta_{jj'}.
\]
For the diagonal \(\delta:C\hookrightarrow S\), put \(d=c_1(\mathcal O_S(\Delta))\). We claim
\[
 d=\sum_{i=0}^2\sum_j(-1)^i e_{i,j}\otimes e_{i,j}^{\vee}.
 \tag{CT12}
\]
Here \(a\otimes b\) denotes \(p_1^*a\cup p_2^*b\).

To prove it, Lemma 4.0C.3 gives, whenever \(\deg a+\deg b=2\),
\[
 \operatorname{tr}_S(d\cup(a\otimes b))
 =\operatorname{tr}_C(a\cup b).
 \tag{CT13}
\]
Expand the component of \(d\) of bidegree \((i,2-i)\) as \(\sum_j e_{i,j}\otimes d_j\). In tensor multiplication, crossing the second factor of degree \(2-i\) past \(a\) of degree \(2-i\) contributes \((-1)^i\). Reversing \(e_{i,j}\cup a\) contributes the same sign. Their product is one, so the left side of (CT13) in this component is
\[
 \sum_j\operatorname{tr}_C(a\cup e_{i,j})
              \operatorname{tr}_C(d_j\cup b).
\]
Take \(a=(-1)^i e_{i,j_0}^{\vee}\). Its first pairing is \(\delta_{j_0j}\), by graded commutativity. The right side of (CT13) is the pairing of \((-1)^i e_{i,j_0}^{\vee}\) with \(b\). Perfection forces \(d_{j_0}=(-1)^i e_{i,j_0}^{\vee}\). This proves (CT12). This sign check agrees with [Stacks, Lemma 45.7.7](https://stacks.math.columbia.edu/tag/0FGZ); the normalization needed to apply it to our product has been proved in Lemmas 4.0C.2–3.

Let \(h:C\to C\) be a morphism and \(\gamma_h=(\mathrm{id},h)\). Pull back (CT12) to the graph and take the curve trace. The result is
\[
 \begin{aligned}
 \deg\bigl(\gamma_h^*\mathcal O_S(\Delta)\bigr)
 &=\operatorname{tr}_C(\gamma_h^*d)\\
 &=\sum_{i,j}(-1)^i
        \operatorname{tr}_C(e_{i,j}\cup h^*e_{i,j}^{\vee})\\
 &=\sum_{i=0}^2(-1)^i
        \operatorname{Tr}(h^*\mid H^i(C,A))\quad\text{in }A.
 \end{aligned}
 \tag{CT14}
\]
For the last equality, write \(h^*\) in the dual basis of degree \(2-i\). The displayed pairings are its diagonal matrix entries. Replacing \(2-i\) by \(i\) preserves parity. The degree equality in the first line is the curve Kummer normalization, not a surface intersection theorem.

If \(h\ne\mathrm{id}\), the section defining \(\Delta\) pulls back to a nonzero section on \(C\). Its zero divisor is the fixed-point scheme. This scheme is finite: a positive-dimensional equalizer in the integral curve would contain its generic point, and separatedness and reducedness would make \(h\) the identity. At a fixed point with parameter \(z\), its length is
\[
 \operatorname{length}_k k[[z]]/(z-h^\#z).
 \tag{CT15}
\]
The degree on the left of (CT14) is the sum of these lengths. Completion preserves finite module length. Thus (CT14) is the fixed-point formula modulo every \(\ell^r\), including inseparable maps and multiple fixed points.

The free curve groups, their perfect pairing, their trace and the Kummer maps are compatible with coefficient reduction. In degree one this compatibility is the multiplication-by-\(\ell\) transition on Jacobian torsion; the inspected earlier multiplication proof makes it surjective. Degree zero and degree two have ordinary reduction transitions. These finite systems have no degree-one derived-limit correction: their \(H^0\) transitions are surjective, and the map defining \(\varprojlim^1\) on their products is surjective by recursively choosing lifts. Passing to \(\mathbf Z_\ell\), then \(\mathbf Q_\ell\), therefore gives the exact identity
\[
 \deg\bigl(\gamma_h^*\mathcal O_S(\Delta)\bigr)
 =\sum_{i=0}^2(-1)^i
        \operatorname{Tr}(h^*\mid H^i(C,\mathbf Q_\ell)).
 \tag{CT16}
\]
Equality modulo all \(\ell^r\) implies equality in \(\mathbf Z_\ell\), because the intersection of its ideals \(\ell^r\mathbf Z_\ell\) is zero.

### 4.0C.5. Frobenius over every finite extension

Let \(\Phi:C\to C\) be the base extension of the \(q\)-power Frobenius of \(C_0\), viewed as a \(k\)-morphism. Its degree is \(q\). More generally \(\deg\Phi^a=q^a\): if \(K=k(C)\) is finite of degree \(d\) over \(k(t)\), Frobenius identifies the degree-\(d\) extensions \(K/k(t)\) and \(K^{q^a}/k(t^{q^a})\). The tower formula over \(k(t^{q^a})\) gives
\[
 [K:K^{q^a}]=q^a.
\]
Here \(k\) is perfect, so its coefficient field stays \(k\) under every power. A nonconstant morphism between projective smooth curves is finite: its fibres are zero-dimensional, and proper quasi-finite morphisms are finite. This identifies the function-field degree with the morphism degree.

The fixed geometric points of \(\Phi^a\) are exactly \(C_0(\mathbf F_{q^a})\). On an affine chart defined over \(\mathbf F_q\), being fixed says that all coordinates satisfy \(x^{q^a}=x\), whose roots in \(k\) are exactly \(\mathbf F_{q^a}\). These charts cover the curve. The differential of \(\Phi^a\) is zero. The fixed-point equation in (CT15) consequently has nonzero linear term and length one at every fixed point. Hence
\[
 \deg\bigl(\gamma_{\Phi^a}^*\mathcal O_S(\Delta)\bigr)
 =\#C_0(\mathbf F_{q^a}).
 \tag{CT17}
\]
The operator on \(H^0\) is one. On \(H^2\) it is \(q^a\): a degree-one line bundle has a Kummer class of trace one, and pullback multiplies its divisor degree by \(\deg\Phi^a\). Twists may be trivialized for this \(k\)-linear morphism using the already chosen roots. Applying (CT16) gives
\[
 \#C_0(\mathbf F_{q^a})
 =1+q^a-\operatorname{Tr}(F^a\mid H^1(C,\mathbf Q_\ell)),
 \qquad F=\Phi^*,\quad a\geq1.
 \tag{CT18}
\]

This \(F\) is geometric Frobenius on the untwisted cohomology. To check the convention, let \(\sigma_q\) act on \(k\) by \(a\mapsto a^q\), and let \(\rho_{\sigma_q}\) be the resulting semilinear coefficient automorphism of \(C\). On an affine algebra \(R\otimes_{\mathbf F_q}k\), the absolute \(q\)-power Frobenius is the composite of
\[
 r\otimes a\longmapsto r^q\otimes a,
 \qquad r\otimes a\longmapsto r\otimes a^q.
 \tag{CT19}
\]
Its pullback on constant-coefficient etale cohomology is canonically the identity. Here is the needed categorical check. For an affine etale \(U=\operatorname{Spec}B\to X=\operatorname{Spec}R\), relative Frobenius has the ring map
\[
 B\otimes_{R,F_R}R\longrightarrow B,
 \qquad b\otimes r\longmapsto b^q r.
 \tag{CT19a}
\]
It is integral, since every \(b\) satisfies its monic equation \(Z^q-b^q\) over the image. Given a map from its source algebra to an algebraically closed field, its unique lift to \(B\) sends \(b\) to the unique \(q\)-th root of the image of \(b\otimes1\). The tensor relations make that lift agree with the specified map on \(R\). This proves radiciality and surjectivity on geometric points.

Both schemes of (CT19a) are etale over \(X\), so their map is etale by the lifting proof of *Formally smooth, unramified and etale ring maps*, Proposition 7.4. Here is an affine check that it is an isomorphism. Its diagonal is a flat finitely presented quotient: it is a map between etale schemes over \(U\), so the same proposition applies. Lemma 7.5 of that lesson proves the kernel of such a quotient is generated by an idempotent. Radiciality makes the diagonal surjective on underlying points; hence that idempotent is zero. Thus the diagonal is an isomorphism. The map (CT19a) is faithfully flat because it is etale and surjective. Faithful-flat descent now makes it an isomorphism: for a faithfully flat map \(A'\to B\), the equalizer of \(B\rightrightarrows B\otimes_{A'}B\) is \(A'\); this is checked after tensoring with \(B\), where insertion of the unit contracts the augmented complex. Faithful flatness detects exactness. When the diagonal is an isomorphism the two arrows agree, so the equalizer is all of \(B\), proving \(A'=B\).

The relative Frobenius isomorphisms are natural in the affine etale objects, which form a basis for the site. They identify the inverse-image functor of absolute Frobenius with the identity on the small etale site. They fix the constant sheaf \(A\) and therefore its injective cohomology functor as well. This is also consistent with the inspected topological-invariance proof.

Pullback by the second map in (CT19) is the usual arithmetic Galois action: on finite etale equations and their descent data it applies \(\sigma_q\) to coefficients. The two maps commute, and their composite has identity pullback. Thus \(\Phi^*\) is the inverse of arithmetic Frobenius, which is geometric Frobenius. This argument concerns the untwisted constant coefficients; a root trivialization of a Tate twist is not claimed to be Galois equivariant.

### 4.0C.6. The determinant, logarithm and Euler product identity

**Theorem 4.0C.6.** Put
\[
 P_{C_0}(CT)=\det\bigl(1-TF\mid H^1(C,\mathbf Q_\ell)\bigr).
\]
Then, in \(\mathbf Q_\ell[[T]]\),
\[
 \begin{aligned}
 Z(C_0,T)
 &:=\exp\left(\sum_{a\geq1}
       \#C_0(\mathbf F_{q^a})\frac{T^a}{a}\right)\\
 &=\prod_{x\in|C_0|}(1-T^{\deg x})^{-1}\\
 &=\frac{P_{C_0}(CT)}{(1-T)(1-qT)}.
 \end{aligned}
 \tag{CT20}
\]
The polynomial lies in \(\mathbf Z[T]\), has degree \(2g\), and is independent of \(\ell\). For every \(b\geq1\), the same identities over \(\mathbf F_{q^b}\) have \(q^b\) and \(F^b\) in place of \(q\) and \(F\).

*Proof.* For a finite matrix \(B\) over a characteristic-zero field, differentiating its determinant by the adjugate formula gives
\[
 \frac{d}{dT}\log\det(1-TB)
 =-\operatorname{Tr}\bigl(B(1-TB)^{-1}\bigr)
 =-\sum_{a\geq1}\operatorname{Tr}(B^a)T^{a-1}.
\]
Its constant term is one, so integrating formally yields
\[
 \log\det(1-TB)
 =-\sum_{a\geq1}\operatorname{Tr}(B^a)\frac{T^a}{a}.
 \tag{CT21}
\]
Apply this to (CT18). The constant and degree-two terms give \(-\log(1-T)\) and \(-\log(1-qT)\); the degree-one term gives \(\log P_{C_0}(CT)\). Exponentiation proves the last equality of (CT20), as a formal identity without an analytic convergence premise.

A closed point of degree \(d\) contributes \(d\) geometric points over \(\mathbf F_{q^a}\) precisely when \(d\mid a\). Indeed its residue field is \(\mathbf F_{q^d}\); it has \(d\) embeddings into \(\mathbf F_{q^a}\) in that case and none otherwise. Thus, if \(b_d\) counts closed points of degree \(d\),
\[
 \#C_0(\mathbf F_{q^a})=\sum_{d\mid a}db_d.
\]
There are only finitely many closed points of bounded degree, since the curve has finite type over a finite field. Expanding the logarithm of the Euler product now gives the first expression in (CT20) coefficient by coefficient.

Each Euler-product factor has integer coefficients, so \(Z(C_0,T)\in\mathbf Z[[T]]\). Multiplying it by \((1-T)(1-qT)\) gives an integer series. Its image in \(\mathbf Q_\ell[[T]]\) is the finite polynomial \(P_{C_0}(CT)\), so every coefficient beyond its degree is zero already in \(\mathbf Z\). This proves integrality and makes the polynomial independent of \(\ell\). The rank in (CT1) is \(2g\). Frobenius is an etale-topos equivalence, so \(F\) is invertible and the determinant polynomial has that exact degree. Finally (CT18) already holds for every power: applying it with powers \(ba\) proves the assertion for every finite base-field extension. \(\square\)

The normal-coordinate construction proves the constant curve trace mechanism using the stated earlier interfaces. It uses neither the general smooth-base-change theorem nor the general smooth-variety trace theorem. Higher cohomological continuity in *Pushforward, pullback and finite morphisms*, §2, equation (2.3), is still required in the strict-trait calculation, the pro-étale generic restriction and the filtered-sheaf closed-point detection. That earlier lesson proves its degree-zero finite-data argument and imports the higher-cohomology assertion. Its proof, together with the recorded recursive foundations of curve duality, proper base change and the Picard construction, remains required by the proof rule. This precise scope is included in §7.

**Lemma 4.0D (the curve bound needed for Chebotarev).** For every smooth projective geometrically integral curve \(C_0/\mathbf F_q\) of genus \(g\),
\[
\bigl|\#C_0(\mathbf F_{q^a})-q^a-1\bigr|\le2gq^{a/2}
\qquad(a\ge1).
\]
Every geometric-Frobenius eigenvalue on its first cohomology is algebraic and has absolute value \(q^{1/2}\) under every embedding. The same statements apply to any smooth projective twist of the curve.

*Proof.* We supply the product-surface positivity, so that this step requires no unproved Hodge-index theorem. The actual earlier inputs are the coherent Euler-polynomial proof, *Euler characteristics and Hilbert polynomials*, Theorems 2.1 and 4.2; projective duality, *Dualizing sheaves and Serre duality for projective schemes*, Theorems 4.1–4.2; and curve Riemann–Roch and differential duality, *Abelian varieties*, Lemma 9.11. Work first over an algebraic closure, put \(S=C\times C\), and choose a point \(P\). Write \(V=\{P\}\times C\) and \(W=C\times\{P\}\).

Here is the numerical construction we use on \(S\). On the group generated by coherent sheaves with their exact-sequence relations, let \(\delta_L[F]=[F\otimes L]-[F]\). It lowers support dimension by one. Indeed the coherent filtration from the Euler-polynomial proof reduces to an ideal on an integral closed subscheme. A generic trivialization of \(L\), extended after multiplying by an ideal of the complement, injects the same ideal lattice into that sheaf and its twist; the difference of their classes is a difference of cokernels on proper closed subsets. Repeat this argument on those subsets. Three such operators therefore annihilate Euler characteristic on a surface. The finite-difference identities, integrated using \(\binom{n+1}{j+1}-\binom n{j+1}=\binom nj\), make
\(\chi(L^nM^t)\) a polynomial of total degree at most two, for all integers \(n,t\). The recurrences prove negative as well as positive indices. Define
\[
I(L,M)=\chi(LM)-\chi(L)-\chi(M)+\chi(\mathcal O_S).
\]
It is symmetric. The identity
\(\delta_{L_1L_2}=\delta_{L_1}+\delta_{L_2}+\delta_{L_1}\delta_{L_2}\)
and the vanishing of third differences make it additive in each argument. Also \(I(L,L)/2\) is the quadratic coefficient of \(\chi(L^n)\). This agrees with the numerical-intersection definition in [Stacks, Tag 0BEP](https://stacks.math.columbia.edu/tag/0BEP); the argument just given proves the required properties locally here.

For a smooth Cartier curve \(E\subset S\), its multiplication exact sequence and curve Riemann–Roch give
\[
I(L,\mathcal O(E))
=\chi(E,L(E)|_E)-\chi(E,\mathcal O(E)|_E)
=\deg(L|_E).
\]
In particular \(I(V,V)=I(W,W)=0\) and \(I(V,W)=1\). The restriction degrees along either family of fibers are constant: the line bundle is flat in that projective family, so the proved constancy of its Euler characteristic, and curve Riemann–Roch, give constant degree.

Suppose a line bundle \(D\) has degree zero on both fiber families. Then \(h^0(D^n)\le1\) for every integer \(n\). A nonzero section with a nonempty zero divisor would have a component dominating at least one factor; its restriction to a general opposite fiber would have positive degree. That contradicts degree zero. Thus any nonzero section is nowhere zero and trivializes the bundle, whose section space then consists of constants.

We also bound \(h^2(D^n)\) uniformly in \(n\). The dualizing sheaf of the smooth surface is \(K_S=p_1^*\Omega_C^1\otimes p_2^*\Omega_C^1\): the regular-immersion Koszul calculation used in Lemma 9.11, with codimension \(N-2\), identifies the projective dualizing sheaf with \(\det\Omega_S^1\), and the two projection differentials give this formula. Duality makes \(h^2(D^n)=h^0(K_S D^{-n})\). Let \(H=V+W\). The bundle \(K_S D^{-n}(-jH)\) has degree \(2g-2-j\) on either fiber. Its restriction to the reduced union \(H\) injects into the sum of the restrictions to \(V,W\), since sections agreeing at their intersection glue. A line bundle of degree \(e\) on a smooth curve has at most \(\max(e+1,0)\) sections: subtract \(e+1\) distinct points successively when \(e\ge0\), and use the absence of a section of negative degree. Hence the restriction space has dimension at most \(2\max(2g-1-j,0)\), independently of \(n\). For \(A>\max(2g-2,0)\), the bundle \(K_S D^{-n}(-AH)\) has negative degree on a general fiber and has no section. The restriction exact sequences for \(j=0,\ldots,A-1\) bound \(h^0(K_SD^{-n})\) by the finite sum of these constants. Therefore
\[
\chi(D^n)=h^0(D^n)-h^1(D^n)+h^2(D^n)
\]
is bounded above for positive \(n\). Its quadratic coefficient cannot be positive. We have proved \(I(D,D)\le0\).

For an arbitrary \(L\), put \(d_1(L)=I(L,V)\), \(d_2(L)=I(L,W)\), and
\(D=L-d_2(L)V-d_1(L)W\), using additive notation for line bundles. Then both fiber degrees of \(D\) are zero and
\[
I(L,L)\le2d_1(L)d_2(L).
\]
Consequently the symmetric bilinear form
\[
\langle L,M\rangle=d_1(L)d_2(M)+d_2(L)d_1(M)-I(L,M)
\]
is positive semidefinite. Applying its positivity to \(nL+tM\) for integers \(n,t\), then to rationals by homogeneity and reals by continuity, proves
\(\langle L,M\rangle^2\le\langle L,L\rangle\langle M,M\rangle\).

Let \(\Delta\) be the diagonal and \(\Gamma_a\) the graph of \(q^a\)-Frobenius. Their fiber degrees are \((1,1)\) and \((1,q^a)\). Frobenius has degree \(q^a\): for a transcendence element \(t\), the curve function field \(K\) is finite over \(\bar k(t)\). Frobenius identifies \(K/\bar k(t)\) with \(K^{q^a}/\bar k(t^{q^a})\), so the tower formula and \([\bar k(t):\bar k(t^{q^a})]=q^a\) give \([K:K^{q^a}]=q^a\). The normal bundle of a graph \((\mathrm{id},f)\) is \(f^*T_C\), by \((v,w)\mapsto w-df(v)\). Thus
\[
I(\Delta,\Delta)=2-2g,\qquad
I(\Gamma_a,\Gamma_a)=q^a(2-2g).
\]
Its intersection with \(\Delta\) consists of the \(\mathbf F_{q^a}\)-points, each of length one: the fixed-point equation has differential the identity because Frobenius has differential zero. Hence
\[
\langle\Delta,\Gamma_a\rangle=1+q^a-\#C_0(\mathbf F_{q^a}),\qquad
\langle\Delta,\Delta\rangle=2g,\quad
\langle\Gamma_a,\Gamma_a\rangle=2gq^a.
\]
Cauchy–Schwarz proves the displayed count bound.

For the cohomological conclusion, Theorem 4.0C.6 constructs the constant curve trace identity from its precise earlier curve interfaces. Its imported higher cohomological-continuity foundation remains to be proved, as recorded there. The intersection argument above proves the point-count bound in every extension field independently of that cohomological foundation. With that remaining foundation, the trace identity writes the point counts as
\(1+q^a-\sum_i\alpha_i^a\). Its determinant polynomial on \(H^1\) has rational coefficients, because its logarithm is recovered from these rational integer counts and the rational factors for \(H^0,H^2\). The eigenvalues are therefore algebraic. For any complex embedding, the series \(\sum_{a\ge1}(\sum_i\alpha_i^a)z^a\) converges for \(|z|<q^{-1/2}\), by the count bound. It is the rational function \(\sum_i\alpha_i z/(1-\alpha_i z)\); a pole for a distinct nonzero \(\alpha_i\) cannot cancel, since its multiplicity is a positive integer. Thus \(|\alpha_i|\le q^{1/2}\). Curve duality pairs \(\alpha_i\) with \(q/\alpha_i\), giving the opposite bound and equality. A twist is another smooth projective curve with the same geometric genus, so the proved argument applies to it directly. The point-count bound is proved. The trace mechanism is now written in §§4.0C.1–6; its higher-continuity and recursive earlier-foundation obligations remain explicit for the cohomological assertion. ∎

**Lemma 4.1 (splitting by fiberwise multiplication).** Let \(S\) be smooth of finite type over \(\mathbf F_p\), let \(\ell\ne p\), and let \(f:A\to S\) be an abelian scheme. Suppose the ordinary and compactly supported Leray spectral sequences exist and are compatible with their natural comparison map. Suppose multiplication by an integer \(t>1\) on \(A\) acts on \(R^jf_*\mathbf Q_\ell\) as \(t^j\). Then both spectral sequences degenerate at their second pages. In total degree \(n\), their \(j\)-th terms identify with the \(t^j\)-eigenspaces of multiplication on the respective abutments. Write \(H^i_{\mathrm{par}}=\operatorname{im}(H^i_c\to H^i)\) in every degree. Consequently

\[
H^i_{\mathrm{par}}(S,R^jf_*\mathbf Q_\ell)
\quad\text{is the }t^j\text{-eigenspace of }\quad
H^{i+j}_{\mathrm{par}}(A,\mathbf Q_\ell).
\tag{17}
\]

*Proof.* The second pages are \(H^i(S,R^jf_*\mathbf Q_\ell)\) and \(H^i_c(S,R^jf_*\mathbf Q_\ell)\). Multiplication acts on each as the scalar \(t^j\). A differential
\[
d_r:E_r^{i,j}\longrightarrow E_r^{i+r,j-r+1},
\qquad r\geq2,
\]
commutes with multiplication. Its source and target have the different scalars \(t^j\) and \(t^{j-r+1}\); hence \((t^j-t^{j-r+1})d_r=0\), and \(d_r=0\). Induction proves this at every page and in both sequences.

Degeneration alone usually gives a filtration, rather than a canonical direct sum. Here the filtration is split by multiplication. In total degree \(n\), each graded piece has its own scalar \(t^j\). Applying the factors \(M-t^j\), in filtration order, shows that their product annihilates the multiplication operator \(M\) on the abutment. Its roots are distinct in \(\mathbf Q_\ell\), so \(M\) is semisimple. The polynomial projectors
\[
\prod_{j'\ne j}\frac{M-t^{j'}}{t^j-t^{j'}}
\tag{18}
\]
split the filtration and identify its graded pieces with the stated eigenspaces. Only the indices occurring in that total degree enter the product.

The map from compact support to ordinary cohomology commutes with \(M\) and with Frobenius. Its image on each eigenspace is the corresponding eigenspace of its full image. This proves (17), including the Frobenius equivariance. ∎

For a product of elliptic curves, the multiplication hypothesis follows from Künneth: multiplication acts on their \(H^0,H^1,H^2\) by \(1,t,t^2\), respectively, and a tensor of total degree \(j\) has multiplier \(t^j\). The degree-one assertion follows from the Kummer identification of elliptic first cohomology with the dual Tate module proved in the earlier elliptic lesson, while the degree-two assertion follows from the degree \(t^2\) of multiplication on an elliptic curve.

**Proposition 4.2 (parabolic purity, conditional on compactification).** In Lemma 4.1, suppose in addition that \(A\) embeds as an open in a smooth projective \(A^*\) over the same finite field. Then geometric Frobenius on \(H^i_{\mathrm{par}}(S,R^jf_*\mathbf Q_\ell)\) has eigenvalues of absolute value \(p^{(i+j)/2}\) under every complex embedding.

*Proof.* Extension of supports and restriction give a factorization
\[
H^{i+j}_c(A,\mathbf Q_\ell)
\longrightarrow H^{i+j}(A^*,\mathbf Q_\ell)
\longrightarrow H^{i+j}(A,\mathbf Q_\ell).
\tag{19}
\]
Its image is therefore a Frobenius-stable subquotient of the middle group. Eigenvalues on a stable subspace and its quotient occur among those of the original operator: choose a basis adapted to the subspace and factor the characteristic polynomial of the resulting block triangular matrix. The Weil theorem gives the claimed absolute value on that middle group. Lemma 4.1 identifies the parabolic coefficient group with a stable summand of the image, so the same value holds there. ∎

Apply this mechanism to the \(m\)-fold fiber product \(\mathcal E^m\) over a fine modular curve. Künneth selects \(\mathcal F_\ell^{\otimes m}\) inside \(R^m f_*\mathbf Q_\ell\). The symmetric-power projector
\[
\frac1{m!}\sum_{\sigma\in\mathfrak S_m}\sigma
\tag{20}
\]
then selects \(\mathcal L_m\) in that tensor product. This is the usual permutation action on the tensor factors. When expressed using geometric permutations on degree-one cohomology, the Koszul signs must be compensated; an unadjusted geometric symmetrizer would select the wrong symmetry. The denominator is allowed because coefficients are in \(\mathbf Q_\ell\), even if \(\ell\mid m!\). Thus the relevant parabolic group occurs in total degree

\[
1+m=k-1.
\tag{21}
\]

The needed compactification is supplied by the following explicit resolution. Its proof works in every characteristic; it uses the nodal semistable local model, rather than general resolution of singularities in positive characteristic.

**Lemma 4.2A (resolution of a nodal fiber product).** Let \(C\) be a smooth projective curve over a field. Suppose \(\mathcal E^*\to C\) is a projective semistable curve with smooth total surface, and that its only nonsmooth fiber points are ordinary nodes with étale local equations \(xy=t\), where \(t\) is a parameter on \(C\). Every iterated fiber product of \(\mathcal E^*\) has a projective resolution smooth over the field, which is an isomorphism over its smooth locus. In particular the product of its smooth elliptic-family open is an open in a smooth projective variety.

*Proof.* At a point with \(r+1\) nodal factors, and any number \(s\) of additional smooth coordinates, the étale local ring has the model
\[
A=\kappa[X_0,Y_0,\ldots,X_r,Y_r,T_1,\ldots,T_s]/
(X_iY_i-X_0Y_0:1\le i\le r).
\]
The case \(r=0\) is already smooth. For \(r\ge1\), let \(I\) be generated by every monomial \(\prod_{i=0}^r Z_i^{a_i}\), where \((a_i)\) is a permutation of \(0,1,\ldots,r\), and each \(Z_i\) is either \(X_i\) or \(Y_i\). These choices are symmetric under permuting pairs or exchanging their branches. The ring is a domain. Adjoin \(t=X_0Y_0\) and write all its relations as \(X_iY_i=t\). Replacing these disjoint products by \(t\) gives a normal form \(t^a\prod X_i^{b_i}Y_i^{c_i}\), with \(b_ic_i=0\). In the Laurent ring \(\kappa[t,X_0^{\pm1},\ldots,X_r^{\pm1}]\), its image has exponents \(b_i-c_i\) on \(X_i\) and \(a+\sum c_i\) on \(t\). These recover all the normal-form exponents uniquely. Thus these monomials are independent and the proposed map to that domain is injective.

Consider the blow-up chart for \(M=\prod X_i^i\); its ring is \(A[I/M]\) inside the fraction field. It contains
\[
u=Y_0/X_1,\qquad v_i=X_i/X_{i+1}\ (0\le i<r),\qquad v_r=X_r.
\]
The first ratio comes from exchanging exponents zero and one and choosing \(Y_0\); each other ratio comes from exchanging two adjacent exponents. Conversely every original coordinate is a polynomial in these variables:
\[
X_i=v_r\prod_{j=i}^{r-1}v_j,\qquad
Y_0=uX_1,\qquad Y_i=uX_0X_1/X_i\ (i\ge1).
\]
The last expression is polynomial, since the exponents of every \(v_j\) in its numerator dominate those in its denominator. The empty product is one.

We must also check every generator ratio, not just these coordinates. In \(\prod X_i^i\), the exponent of \(v_j\) is \(j(j+1)/2\) for \(j<r\), and that of \(v_r\) is \(r(r+1)/2\). In an arbitrary generator, its \(v_r\)-exponent is the same. For \(1\le j<r\), its \(v_j\)-exponent is at least \(\sum_{i\le j}a_i\), whose minimum is \(0+1+\cdots+j\); choosing a \(Y_i\) with \(i>j\) only adds a nonnegative exponent. The \(v_0\)-exponent and the \(u\)-exponent are nonnegative, and the denominator has exponent zero in both. Hence every generator divided by \(M\) is polynomial. We have proved
\[
A[I/M]=\kappa[u,v_0,\ldots,v_r,T_1,\ldots,T_s].
\]
There are no relations among these variables: the inverse expressions give a birational parametrization of the dense open where the indicated ratios are defined. Every other blow-up chart is obtained by the permitted pair permutations and branch exchanges, so has the same polynomial description. Thus the blow-up is smooth in every characteristic.

Its exceptional locus lies over exactly the singular locus. The Jacobian of the equations has full rank unless at least two pairs have both coordinates zero. With at most one such pair, choose exponent zero there and a unit branch in every other pair; the corresponding generator is a unit, so the blow-up is an isomorphism there. With at least two such pairs, every generator has a positive exponent at one of them. No point over such a singular point can have an isomorphic local ring under the blow-up, since every local ring of the resolved space is regular whereas the original local ring is singular. Thus every singular point lies in the image of the exceptional locus, and no smooth point does.

For completeness the ideals glue. At a node the two branch ideals in the special fiber have generators \(x,y\), determined up to units and exchange; the equation is \(xy=t\) up to a unit. Their pullbacks to the product give the coordinates above. Replacing their generators by units, permuting the factors, or exchanging branches leaves the generated ideal unchanged. If one factor becomes smooth, one of its chosen coordinates is a unit. Assigning the largest exponent to that unit gives precisely the ideal for the remaining nodal factors; any other assignment gives a multiple of one of its generators, since the sorted remaining exponents are at least \(0,\ldots,r-1\). This proves agreement on overlaps where the number of nodal factors changes. The intrinsic branch ideals and their symmetric expression therefore descend from the étale charts, including nonsplit nodes. Blow-up commutes with étale base change, so its local smoothness descends as well. A blow-up of a coherent ideal is projective; the original product is projective over projective \(C\), and hence so is the resolution. This proves all claims. ∎

For the modular family, the remaining premise of this lemma is the existence of its projective semistable model over the fine compact modular curve. The earlier local elliptic lesson proves the node models for a Tate degeneration; the arbitrary-level arithmetic modular model in lesson 10 is still a separate construction obligation. Once that premise is established, Lemma 4.2A proves the entire product resolution. For \(m=0\), one needs only the compact modular curve.

With these inputs, Proposition 4.2 supplies purity of weight \(k-1\) for the required parabolic constituent at good primes. The passage through auxiliary levels and all characters is part of Deligne's construction. Its complete arithmetic conclusion is [Deligne 1974, Theorem (8.2)]: for each primitive cuspidal form as in (1), the two roots \(\alpha_p,\beta_p\) of \(P_p\), for \(p\nmid N\), satisfy

\[
|\sigma(\alpha_p)|=|\sigma(\beta_p)|
=p^{(k-1)/2}
\tag{22}
\]

for every complex embedding of their number field. This also covers a prime \(p=\ell\) for a separately chosen \(\lambda\): the complex assertion about \(P_p\) is independent of that choice. A good-prime Frobenius operator on (3) is only being asserted when \(p\nmid N\ell\).

**Theorem 4.3 (Weil implies the Ramanujan–Petersson bound).** Under the purity assertion (22),

\[
|\sigma(a_p)|\leq2p^{(k-1)/2}
\qquad(p\nmid N)
\tag{23}
\]

for every embedding \(\sigma:K\hookrightarrow\mathbf C\).

*Proof.* Extend \(\sigma\) to a splitting field of \(P_p\). By its coefficient of \(X\), \(\sigma(a_p)=\sigma(\alpha_p)+\sigma(\beta_p)\). The triangle inequality and (22) give
\[
|\sigma(a_p)|
\leq|\sigma(\alpha_p)|+|\sigma(\beta_p)|
=2p^{(k-1)/2}.
\]
Every extension has the same two absolute values, so the conclusion holds for the original \(\sigma\). ∎

In weight two this gives \(2\sqrt p\), the scale of Hasse's bound. In weight twelve it gives \(2p^{11/2}\). The change of exponent records the degree of the cohomology carrying the form.

## 5. The global determinant and oddness

View the Dirichlet character as a Galois character by the action on \(N\)-th roots of unity:

\[
\chi_G:G_{\mathbf Q}\longrightarrow
(\mathbf Z/N\mathbf Z)^\times
\xrightarrow{\chi}K^\times\longrightarrow K_\lambda^\times.
\tag{24}
\]

It is unramified outside \(N\) and takes \(\operatorname{Fr}_p\) to \(\chi(p)\) when \(p\nmid N\).

**Theorem 5.1.** The representation in Theorem 1.1 satisfies

\[
\det\rho_{f,\lambda}=\chi_G\chi_\ell^{\,k-1}.
\tag{25}
\]

*Proof.* Both sides are continuous one-dimensional characters of \(G_{\mathbf Q}\). At every \(p\nmid N\ell\), (4) identifies their values as \(\chi(p)p^{k-1}\). Their quotient \(\eta\) therefore equals \(1\) on all these Frobenius classes. It remains to justify the use of density for a possibly infinite image.

If \(\eta(g)\ne1\), continuity and the Hausdorff topology give an open neighborhood of \(g\) on which \(\eta\ne1\). It contains a coset \(gU\) of an open normal subgroup \(U\). Because \(\eta\) is a character, the union of the conjugates of this coset still has \(\eta\ne1\). Chebotarev for the finite Galois quotient \(G_{\mathbf Q}/U\) supplies a prime outside the finite set dividing \(N\ell\) whose Frobenius lies in that conjugacy class. Its character value must be \(1\), a contradiction. Hence \(\eta=1\). ∎

This proves a global equality, including on inertia and at complex conjugation. It uses the good-prime determinant provided by construction; it does not recover that local determinant from (13) alone.

**Corollary 5.2 (oddness).** For complex conjugation \(c\),
\[
\det\rho_{f,\lambda}(c)=-1,\qquad
\rho_{f,\lambda}(c)\sim
\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\tag{26}
\]

*Proof.* We have \(\chi_G(c)=\chi(-1)=(-1)^k\) and \(\chi_\ell(c)=-1\). Their product in (25) is \((-1)^k(-1)^{k-1}=-1\). Since \(c^2=1\), its eigenvalues lie in \(\{1,-1\}\); characteristic zero makes this operator diagonalizable. Its determinant forces one of each. ∎

**Corollary 5.3 (absolute irreducibility).** The irreducibility input in Theorem 1.1 and Corollary 5.2 imply that \(\rho_{f,\lambda}\) is absolutely irreducible.

*Proof.* A reducible two-dimensional representation over an algebraic closure has an invariant line. That line is invariant under \(c\), so it is one of the two one-dimensional eigenspaces in (26), extended from \(K_\lambda\). If an element of \(G_{\mathbf Q}\) preserves the extended eigenspace, its matrix entry taking the original eigenspace into the other one is zero already over \(K_\lambda\). Thus the original eigenspace is Galois invariant, contrary to irreducibility over \(K_\lambda\). ∎

The cusp-form hypothesis matters. The direct sum \(1\oplus\chi_G\chi_\ell^{k-1}\), for example, has good trace \(1+\chi(p)p^{k-1}\) and determinant \(\chi(p)p^{k-1}\), and is reducible. Thus the determinant and oddness deductions cannot prove cuspidal irreducibility by themselves.

## 6. The discriminant form and the weight-two specialization

For the level-one weight-twelve discriminant form, the modular-forms prerequisite gives

\[
\Delta=q\prod_{n\geq1}(1-q^n)^{24}
=\sum_{n\geq1}\tau(n)q^n.
\tag{27}
\]

The initial coefficients can be computed formally, without any analytic approximation. To find them through \(q^7\), keep factors with \(n\leq6\), expand each by the binomial theorem, and discard degree above six in the product after removing the leading \(q\). The result is

\[
\Delta=q-24q^2+252q^3-1472q^4
+4830q^5-6048q^6-16744q^7+O(q^8).
\tag{28}
\]

Thus \(K=\mathbf Q\), the character is trivial, and
\[
\rho_{\Delta,\ell}:G_{\mathbf Q}\longrightarrow
\operatorname{GL}_2(\mathbf Q_\ell),\qquad
\det\rho_{\Delta,\ell}=\chi_\ell^{11}.
\tag{29}
\]
It is unramified outside \(\ell\). At \(p=2,3\), provided \(p\ne\ell\), the complete good-prime polynomials are

\[
P_2(X)=X^2+24X+2048,\qquad
P_3(X)=X^2-252X+177147.
\tag{30}
\]

Their discriminants and roots make the bound visible:

\[
\begin{array}{c|c|c|c}
p&\operatorname{disc}(P_p)&\text{roots}&\text{squared root modulus}\\ \hline
2&-7616&-12\pm4i\sqrt{119}&144+16\cdot119=2048\\
3&-645084&126\pm i\sqrt{161271}&15876+161271=177147
\end{array}
\tag{31}
\]

The squared coefficient bounds are \(24^2=576\leq4\cdot2048=8192\) and \(252^2=63504\leq4\cdot177147=708588\). Also the coefficient at \(q^4\) checks (2) exactly:
\[
\tau(4)=\tau(2)^2-2^{11}=576-2048=-1472.
\]

For \(k=2\), \(\mathcal L_0=\mathbf Q_\ell\), and the parabolic group is \(H^1(X_1(N)_{\overline{\mathbf Q}},\mathbf Q_\ell)\). Its dual is the rational Tate module of the Jacobian. If the character is trivial, the primitive quotient constructed in *Galois representations of weight-two newforms* has the same good-prime polynomials as (3). Once the irreducibility assertion in Theorem 1.1 has been proved, the trace theorem of lesson 2 identifies its semisimplification with \(\rho_{f,\lambda}\). Since that semisimplification is irreducible of the same dimension, the original representation has no proper composition factor and is itself irreducible. This identifies the actual representations under the stated irreducibility premise, which remains a separate obligation in this edition. Matching finitely many coefficients proves no such identification.

## 7. Proof scope and remaining obligations

The original full construction, purity and irreducibility statements are retained in Theorem 1.1 and (22). Their complete proof chain is still required. The preceding sections now supply the period/cup injection in every regular-cusp weight, the full-Hecke multiplicity and rational coefficient descent under their geometric premises, the all-characteristic nodal product resolution, the symplectic tensor estimate, the parabolic duality bound, and the tensor-power removal of an even-dimensional error. Propositions 3.1 and 4.2 and Theorems 4.3 and 5.1 prove the stated algebraic deductions. Successful formula rendering would certify none of the remaining mathematics.

The exact outstanding core steps are these:

- **Arithmetic modular geometry at arbitrary level.** Construct the fine auxiliary modular curves over every required \(\mathbf Z[1/NM]\), the universal elliptic family, smooth compactification with semistable cusp model, and its descent at levels below five. The actual lesson 10 proves the interior level functors conditional on a family, ordinary subgroup computations and an integral modular-polynomial relation. Its §7 expressly retains the arbitrary-level models and supersingular compact correspondence as gaps. They are needed here before unramifiedness and the congruence relation can be asserted as proved.
- **Comparison and dimension foundations.** The actual earlier LG-MF period proof supplies its cup injection, but its final theorem excludes odd weights without \(-I\). Lemma 2.1 extends that injection to the fine curves here. Surjectivity uses Exercise 8.4 and the analytic Riemann–Roch proof in the dimension lesson, Appendix A; that appendix still requires its recorded real-analysis and Hilbert-space foundations. The current earlier modular lesson, Lemmas 1.2 and 1.4, writes complex curve comparison and algebraically closed field extension. Lemma 2.4 reduces the coefficient-system degree-one comparison to those actual curve proofs, without a higher-dimensional comparison import. The complex curve proof still uses the analytic Riemann–Roch foundations, and the arithmetic family and correspondences must exist before this reduction applies.
- **Higher-weight congruence and general-character determinant.** Prove the special-fiber correspondence, including supersingular points and the coefficient trace, giving (13). Lemma 3.2 proves the Fricke covariance and the global alternating pairing once the arithmetic cyclic-isogeny correspondence exists. Its restriction to the primitive full-Hecke eigenspace still requires a proof of nondegeneracy. The weight-two trivial-character argument in the earlier lesson does not cover arbitrary \(\chi\). The relation alone leaves the scalar defect of (16).
- **Cuspidal irreducibility.** Prove irreducibility over every \(K_\lambda\), including arbitrary nebentypus. Proposition 2.2 constructs a two-dimensional eigenspace under the comparison premises; it proves neither irreducibility nor the required primitive Fricke pairing. Corollary 5.3 proves absolute irreducibility only after irreducibility and the determinant have been established.
- **General smooth-projective purity.** The actual earlier trace-formula proof writes rationality, the even-dimensional Leray estimate, its radical alternative and the all-degree power argument. Its pencil lesson expressly states Veronese-pencil existence, the general étale Picard–Lefschetz sequence, and the global monodromy generation and cycle-conjugacy inputs without proof. Lemma 4.0D proves the all-extension point-count bound for curves, covers and twists from the inspected coherent prerequisites. Sections 4.0C.1–6 now construct the constant curve trace, its product and graph normalizations, and its determinant/Euler-product identity in every finite extension. They replace the previously imported general surface trace input. The higher cohomological-continuity assertion used in the strict-trait, generic-point and filtered-support arguments is still imported in the earlier direct-image lesson, §2, equation (2.3); its actual proof and the recorded recursive earlier foundations remain required. The constant-coefficient construction does not by itself prove the general lisse-sheaf trace formula used elsewhere in this lesson. Lemmas 4.0A–C remove the need for an imported symplectic invariant-basis theorem or an imported \(j_*\)-duality theorem, but these geometric pencil inputs remain. Thus general purity and consequently the full modular root assertion (22) are not yet fully proved in this edition. Lemma 4.2A closes the nodal-product resolution once the semistable family exists; it supplies no arbitrary-dimensional singular-fiber cohomology theorem.

The inspected earlier cohomological proofs used here have precise scopes: smooth duality, Gysin normalization, Künneth and weak Lefschetz occur in the smooth-duality lesson, Theorem 10.1, Proposition 12.1, Lemma 13.2 and Solution 5; the finite-coefficient curve trace formula is Theorem 1.1 and §§2–5 of *The trace formula for curves*, and its adic passage is *The trace formula in all dimensions*, Theorem 5.1. Their own recorded geometric and finiteness prerequisites remain part of the transitive proof requirement. The local elliptic torsion, Tate uniformization and twist calculations used in the Legendre example occur in the earlier lessons of this course, including Lemma 3.0, Theorem 3.1 and Lemma 4.0 of *Elliptic curves over local fields*.

All source links below lead to freely accessible primary material. They locate the geometry and statements checked during this rewrite. They are never counted as proofs supplied by the programme.

## 8. Exercises and complete solutions

**Exercise 8.1 (easy: determinant of the discriminant form).** Prove that \(\det\rho_{\Delta,\ell}=\chi_\ell^{11}\) on all of \(G_{\mathbf Q}\), not just on good Frobenius elements.

*Solution.* Weight twelve gives \(k-1=11\) and level one gives the trivial character. For \(p\ne\ell\), (4) gives determinant \(p^{11}\), equal to \(\chi_\ell^{11}(\operatorname{Fr}_p)\). The quotient character is continuous and equals one on every such Frobenius class. The finite-quotient Chebotarev argument in Theorem 5.1 proves it equals one everywhere. In particular, at complex conjugation its value is \((-1)^{11}=-1\), as required by oddness. ∎

**Exercise 8.2 (medium: congruence and the scalar case).** A two-dimensional invertible operator satisfies \(F+CF^{-1}=aI\). Supply the missing hypothesis needed to conclude (15), prove the corrected statement, and describe what happens if \(F\) is scalar.

*Solution.* One sufficient hypothesis is \(\det F=C\). Multiply the relation by \(F\), and subtract the Cayley–Hamilton relation with that determinant. This gives \((\operatorname{tr}F-a)F=0\); invertibility yields \(\operatorname{tr}F=a\), so both coefficients are as claimed.

If \(F=uI\), the given relation says \(a=u+C/u\). Its characteristic polynomial is always \((X-u)^2\), irrespective of that relation. It equals \(X^2-aX+C\) precisely when \(C=u^2\), which is precisely the added determinant hypothesis. Then \(a=2u\). For a nonscalar \(F\), its degree-two minimal polynomial instead gives the conclusion without the additional hypothesis. Example (16) exhibits the failure when the scalar case is left unrestricted. ∎

**Exercise 8.3 (medium: the Petersson estimate).** Derive an estimate of order \(p^{k/2}\) using the Petersson norm and compare it with (23).

*Solution.* Normalize the weight-\(k\) slash action of a positive-determinant real matrix by its determinant to the \(k/2\) power. This action preserves the Petersson density
\[
|h(z)|^2(\operatorname{Im}z)^k
\frac{dx\,dy}{(\operatorname{Im}z)^2}.
\]
Indeed, for \(\delta=\begin{pmatrix}a&b\\c&d\end{pmatrix}\) of determinant \(n>0\), subtraction of \(\delta z\) and its conjugate gives \(\operatorname{Im}(\delta z)=ny/|cz+d|^2\), and differentiation gives \(d(\delta z)=n(cz+d)^{-2}dz\). The slash factor \(n^{k/2}(cz+d)^{-k}\) cancels the first change in the weight, while the second preserves \(dx\,dy/y^2\). Change of variables therefore proves the stated density identity.
For the \(p+1\) cosets defining a good Hecke operator, the standard normalization is
\[
T_p=p^{\,k/2-1}\sum_{i=1}^{p+1}U_i,
\tag{32}
\]
where each \(U_i\) is such a slash action, with a character factor of modulus one when needed.

To compare norms, choose a finite-index subgroup contained in all the conjugated modular groups involved. On its common cover, use the Petersson norm divided by the index of the cover. Change of variables in the invariant density shows \(\|U_i h\|=\|h\|\) with these normalized norms. The triangle inequality therefore gives
\[
|a_p|\|f\|=\|T_pf\|
\leq(p+1)p^{k/2-1}\|f\|.
\]
The cusp form is nonzero, so its finite positive norm can be cancelled:
\[
|a_p|\leq(p+1)p^{k/2-1}
=p^{k/2}(1+p^{-1})=O(p^{k/2}).
\tag{33}
\]
The same proof applies to a conjugate normalized eigenform. Deligne gives \(2p^{(k-1)/2}\), reducing the exponent by one half. The ratio of the two displayed upper bounds is \((p+1)/(2\sqrt p)\), which grows with \(p\). The norm argument supplies a weaker estimate; it does not imply the Ramanujan–Petersson exponent. ∎

**Exercise 8.4 (hard: Euler–Poincaré and the dimension).** Let \(N\geq5\), let \(g\) be the genus of \(X_1(N)\), and let \(c\) be its number of cusps. Compute
\(\dim H^1_{\mathrm{par}}(Y_1(N)_{\overline{\mathbf Q}},\mathcal L_{k-2})\)
from Euler–Poincaré, and compare it with twice the dimension of \(S_k(\Gamma_1(N))\). Include weight two.

*Solution.* By comparison we can work on the punctured complex curve \(U=X_1(N)(\mathbf C)\setminus D\). Put \(m=k-2\) and \(r=m+1=k-1\). The group \(\Gamma_1(N)\) has no elliptic stabilizers: a noncentral finite-order matrix in \(\operatorname{SL}_2(\mathbf Z)\) has trace \(-1,0\) or \(1\), whereas a matrix in \(\Gamma_1(N)\) has trace congruent to \(2\) modulo \(N\). Also \(-I\notin\Gamma_1(N)\). For \(N\geq5\), no cusp stabilizer has the negative of a unipotent matrix, since its trace would be \(-2\), again incompatible with that congruence.

At each cusp the rank-two uniformizing local system consequently has nontrivial positive unipotent monodromy, conjugate to
\[
\begin{pmatrix}1&w\\0&1\end{pmatrix},
\qquad w\ne0.
\]
On \(\operatorname{Sym}^m\), choose variables \(e_1,e_2\) with \(e_1\) fixed and \(e_2\mapsto e_2+we_1\). In characteristic zero, the logarithm acts as \(w e_1\partial/\partial e_2\); its kernel on homogeneous degree \(m\) polynomials is the line spanned by \(e_1^m\). For \(m=0\) it is the entire one-dimensional space. Since a unipotent matrix and its logarithm have the same fixed vectors, the invariant dimension at each cusp is one. The coinvariant dimension is also one, by rank–nullity for the monodromy minus identity.

The global invariant dimension is
\[
s=\begin{cases}1&m=0,\\0&m>0.\end{cases}
\tag{34}
\]
Here is a direct verification. The group contains nontrivial upper and lower unipotents, for example \(T\) and \(\begin{pmatrix}1&0\\N&1\end{pmatrix}\). A vector fixed by either is killed by its logarithm. Thus a globally invariant homogeneous polynomial is killed by both \(e_1\partial/\partial e_2\) and \(e_2\partial/\partial e_1\). The first makes it a multiple of \(e_1^m\); the second then makes that multiple zero if \(m>0\). The dual symmetric-power system has the same invariant dimensions, since the determinant-one rank-two system is self-dual as a geometric local system.

Remove small open cusp disks to obtain a compact oriented surface \(M\) with \(c\) boundary circles. Pushing the radial coordinate in each punctured disk to its boundary gives a deformation retraction of \(U\) onto \(M\); compact support is computed by the relative cochains of \((M,\partial M)\). The finite polygon and cusp-cut constructions in the earlier modular-curves and period lessons give a finite cell decomposition of this pair. A rank-\(r\) local system contributes a vector space of dimension \(r\) to each relative cell cochain, independently of the attaching maps. Therefore the Euler characteristic of its cochain complex is \(r\) times that of the pair. Boundary circles have Euler characteristic zero, so
\[
\chi_c(U,\mathcal L_m)=r(2-2g-c).
\tag{35}
\]
This proves the required Euler–Poincaré value directly in characteristic zero.

We have \(H^0_c(U,\mathcal L_m)=0\): a locally constant section on connected \(U\) that vanishes near the boundary vanishes everywhere. The duality needed here has a finite-cell proof. Subdivide the oriented surface into triangles and form the transverse dual cells. A primal cell of dimension \(i\) meets its relative dual cell of dimension \(2-i\) once, positively after fixing its orientation; the boundary cells are omitted in the relative complex. Pair the two coefficient fibers by parallel transport to that intersection and evaluation in the dual local system. This identifies one finite cochain complex with the dual of the other. Boundary incidences are transposes with the orientation sign: both follow the same edge with reversed transverse orientation, and the coefficient transport is inverted. Thus the coboundaries are adjoints up to that sign. Finite-dimensional linear algebra gives perfect pairings on cohomology. In particular top relative cohomology is the dual of the global invariant space of the dual system. The coefficient pairing identifies its dimension with (34), so \(\dim H^2_c(U,\mathcal L_m)=s\). Thus
\[
\dim H^1_c(U,\mathcal L_m)=r(2g-2+c)+s.
\tag{36}
\]
The long exact sequence of \((M,\partial M)\) contains
\[
0\longrightarrow H^0(U,\mathcal L_m)
\longrightarrow\bigoplus_{d\in D}\mathcal L_m^{I_d}
\longrightarrow H^1_c(U,\mathcal L_m)
\longrightarrow H^1(U,\mathcal L_m)
\longrightarrow\bigoplus_{d\in D}(\mathcal L_m)_{I_d}
\longrightarrow H^2_c(U,\mathcal L_m)\longrightarrow0.
\tag{37}
\]
Ordinary \(H^2(U,\mathcal L_m)\) vanishes, since a surface with nonempty boundary retracts onto a graph. The first map is injective by the vanishing of \(H^0_c\). Consequently the kernel of \(H^1_c\to H^1\) has dimension \(c-s\). Subtracting it from (36) gives
\[
\dim H^1_{\mathrm{par}}
=r(2g-2+c)-c+2s
=\begin{cases}
2g,&k=2,\\
2(k-1)(g-1)+(k-2)c,&k\geq3.
\end{cases}
\tag{38}
\]

To compare with cusp forms, let \(\omega\) be the Hodge line bundle on the compact modular curve. Its square is the logarithmic cotangent bundle:
\[
\omega^2\simeq\Omega_X^1(D),\qquad
\deg\omega=g-1+\frac c2.
\tag{39}
\]
One can see this normalization directly on the uniformizing half-plane. An invariant differential on the elliptic fiber transforms by \((cz+d)^{-1}\), and \(dz\) transforms by \((cz+d)^{-2}\); their squares give the same transition functions. At a cusp with parameter \(q=\exp(2\pi iz/w)\), \(dz=(w/2\pi i)dq/q\), so the isomorphism extends to the logarithmic cotangent line. There are no elliptic points or negative cusp stabilizers requiring corrections in our range of \(N\). A weight-\(k\) cusp form is a section of \(\omega^k(-D)\), because its expansion has zero constant term at each cusp.

The degree in (39) is positive without a Gauss–Bonnet input. The earlier level-one valence lesson, Theorem 2.1, proves that \(\Delta\) has no zero on the half-plane and a simple zero at its cusp. Pulling it back gives a section of \(\omega^{12}\) whose cusp orders are the positive cusp widths. Hence \(12\deg\omega=\sum_d w_d>0\). The dimension lesson's analytic Riemann–Roch and duality calculation, with the foundation scope recorded in §7, now gives
\[
\begin{aligned}
h^0(\omega^k(-D))-h^0(\omega^{2-k})
&=\deg(\omega^k(-D))+1-g\\
&=(k-1)(g-1)+\frac{k-2}{2}c.
\end{aligned}
\tag{40}
\]
Indeed, the dual term is \(\Omega_X^1\otimes\omega^{-k}(D)=\omega^{2-k}\), by (39). For \(k>2\) it has negative degree and hence no nonzero section; a section would have an effective divisor of that negative degree. For \(k=2\) it is the trivial bundle, with its one-dimensional constant sections. Thus
\[
\dim S_k(\Gamma_1(N))=
\begin{cases}
g,&k=2,\\
(k-1)(g-1)+(k-2)c/2,&k\geq3.
\end{cases}
\tag{41}
\]
Doubling (41) gives (38) exactly. In particular, retaining the \(s\)-term is necessary in weight two.

For a numerical check, \(X_1(5)\) has genus zero and four cusps. These values can be checked directly. Reduction gives \(|\operatorname{SL}_2(\mathbf F_5)|=5(5^2-1)=120\): choose a nonzero first column in \(24\) ways and a second column with determinant one in \(5\) ways. The upper-unipotent image of \(\Gamma_1(5)\) has order \(5\), so the projective index is \(120/(2\cdot5)=12\). Cusps are the upper-unipotent orbits of nonzero first columns \((a,c)\), up to simultaneous sign. If \(c=0\), the two classes of \(a\in\mathbf F_5^\times/\{\pm1\}\) give two cusps. If \(c\ne0\), the translation is transitive on \(a\), and the two classes of \(c\) give two more. The local cusp stabilizer calculation gives width one in the first case and width five in the second. These finite-column identifications follow by completing a primitive column to a determinant-one matrix and using surjective integral reduction; right translation changes only the second column.

To count the genus, triangulate the base modular sphere with vertices its cusp and its two elliptic points; it has three edges and two faces. Upstairs there are \(12/2=6\) vertices above the order-two point, \(12/3=4\) above the order-three point, and four cusp vertices. Open edges and faces are unramified and have twelve lifts. Hence the compact surface has Euler number \(6+4+4-3\cdot12+2\cdot12=2\); its genus is zero. Thus \(\deg\omega=1\), \(\dim S_4=-3+4=1\), and (38) gives parabolic dimension \(-6+8=2\). At weight two both dimensions are zero. This means that no weight-two cusp form exists at this level. ∎

## References

- P. Deligne, *Formes modulaires et représentations \(\ell\)-adiques*, freely accessible original, §§2–5, particularly Theorem 2.10, Proposition 4.8, Theorem 4.9 and Lemmas 5.4–5.5. [Original text](https://www.numdam.org/item/SB_1968-1969__11__139_0/).
- P. Deligne, *La conjecture de Weil I*, freely accessible original, §§3–7 and Theorem 8.2. [Original article](https://www.numdam.org/item/PMIHES_1974__43__273_0/).
- The Stacks project authors, [the Legendre family, Tag 03VA](https://stacks.math.columbia.edu/tag/03VA). Section 2 writes the all-extension count and the vanishing argument used here; the source's trace formula is bound to the earlier programme proof with its own prerequisite scope.

The earlier programme proof locators and the exact versions inspected are recorded in the accompanying rewrite receipt. The sources retain their own rights; this independently written exposition retains the public-domain declaration above.
