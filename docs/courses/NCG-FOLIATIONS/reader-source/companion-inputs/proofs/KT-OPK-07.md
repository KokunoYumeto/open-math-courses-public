# The index map and the exact sequence at \(K_0\)

*Public domain (CC0).*
An invertible matrix in a quotient can fail to lift to an invertible matrix upstairs. Its inverse nevertheless allows a doubled lift. Conjugating a fixed scalar idempotent by that lift produces a class in the ideal's \(K_0\). This class measures the obstruction to an invertible lift after identity stabilization.

We use [Invertibles, unitaries and \(K_1\)](KT-OPK-06.md), the normal form and half-exactness in [Nonunital algebras: unitization, relative classes and half-exactness](KT-OPK-04.md), and the stable idempotent and path-conjugation results of [Idempotents, projections and their equivalences](KT-OPK-01.md). The Fredholm results are those of *Fredholm operators and the stable index*: Theorem 1.1, Corollary 1.2, Theorem 3.2 and Corollary 3.3. Their convention is cokernel minus kernel; the connecting map below has the opposite sign.

Let \(A\) be a complex Banach algebra, \(J\) a closed two-sided ideal and \(B=A/J\), with quotient \(\pi\) and inclusion \(\iota\). The C*-case uses *-homomorphisms. We always use the external unitizations and the unital surjection

\[
\pi^+:A^+\longrightarrow B^+,
\qquad \ker\pi^+=J.
\tag{0.1}
\]

Thus \(J^+\) embeds in \(A^+\) by \(j+\lambda1\mapsto j+\lambda1\), even if \(J\) or \(A\) already has a unit. A normalized invertible has scalar part the identity, as in the preceding lesson. The finite-matrix arguments also apply to normed local Banach algebras when every matrix unitization of \(A,J,B\) is closed under holomorphic functional calculus in its completion, and the stated quotient map is surjective and bounded with kernel \(J\). This is the local setting used below; completeness itself is not required by the algebraic stabilization arguments.

## 1. Two ways to obtain an invertible lift

**Lemma 1.1 (lifting an identity component).** Every normalized invertible in the identity component of \(GL_n(B^+)\) has a normalized invertible lift in the identity component of \(GL_n(A^+)\).

*Proof.* First normalize a path from 1 to the given invertible by dividing out its scalar image, as in the preceding lesson, Proposition 1.2; this preserves its endpoints. The exponential-component prerequisite, Recall 1.1 of *Invertible components and exponential laws*, writes an identity-component invertible as a product of exponentials. We can take the exponents in \(M_n(B)\): subdivide the normalized path so that each consecutive ratio is sufficiently close to 1, and take its logarithm. Each logarithm has scalar part zero. Lift these finitely many exponents entrywise to \(M_n(A)\). The product of their exponentials lifts the given invertible, is normalized and is connected to 1 by multiplying the paths \(\exp(t a)\) one factor at a time. In the normed local setting the same small-ratio logarithms and exponentials belong to the matrix algebra by holomorphic functional calculus; their paths are norm continuous. \(\square\)

This is an endpoint lifting statement. The individual quotient invertible outside the identity component need not lift.

For \(u\in G_n^1(B)\), write

\[
E(a)=\begin{pmatrix}1&a\\0&1\end{pmatrix},\qquad
F(b)=\begin{pmatrix}1&0\\-b&1\end{pmatrix},\qquad
L=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]

The four-factor identity is

\[
\operatorname{diag}(u,u^{-1})=E(u)F(u^{-1})E(u)L.
\tag{1.1}
\]

Choose arbitrary matrix lifts \(a,b\in M_n(A^+)\) of \(u,u^{-1}\), each of scalar part 1. Then

\[
w=E(a)F(b)E(a)L
\tag{1.2}
\]

is invertible, since the triangular factors have inverses \(E(-a),F(-b)\), and \(L^{-1}=-L\). Its quotient is \(\operatorname{diag}(u,u^{-1})\). Its scalar part is also 1, by applying (1.1) to the scalar identity. Neither \(a\) nor \(b\) needs to be invertible. This is the elementary lifting construction already used in the fourth lesson; Exercise 7.1 checks every product and gives its expanded form.

## 2. The idempotent associated to a doubled lift

Put \(P_n=\operatorname{diag}(1_n,0_n)\). For a normalized lift \(w\) as above, let \(e=wP_nw^{-1}\). The quotient of \(e\) is \(P_n\), since \(\operatorname{diag}(u,u^{-1})\) commutes with \(P_n\). Hence \(e-P_n\in M_{2n}(J)\), and both idempotents belong to \(M_{2n}(J^+)\) with scalar part \(P_n\).

**Definition 2.1.** The index connecting map is

\[
\partial:K_1(B)\longrightarrow K_0(J),
\qquad \partial[u]=[wP_nw^{-1}]-[P_n].
\tag{2.1}
\]

The difference is taken in the scalar kernel defining \(K_0(J)\). It is not a claim that the first idempotent belongs to \(M_{2n}(J)\).

**Theorem 2.2.** Definition (2.1) is a well-defined natural group homomorphism.

*Proof: choice of lift.* If \(w'\) is another lift, \(z=w'w^{-1}\) has quotient 1, so \(z\in G_{2n}^1(J)\). The new idempotent is \(zez^{-1}\). Similarity in \(J^+\) preserves its stable idempotent class, so the difference in (2.1) is unchanged.

*Proof: homotopy of representatives.* Suppose normalized \(u,u'\) are joined by a path at a common size. Then \(v=u^{-1}u'\) is in the normalized identity component, as is \(uv^{-1}u^{-1}\). Lemma 1.1 supplies normalized invertible lifts \(a,b\) of these two elements. The matrix \(w\operatorname{diag}(a,b)\) lifts

\[
\operatorname{diag}(u,u^{-1})
\operatorname{diag}(v,uv^{-1}u^{-1})
=\operatorname{diag}(u',u'^{-1}).
\]

Right multiplication by \(\operatorname{diag}(a,b)\) leaves \(wP_nw^{-1}\) exactly unchanged, since that block matrix commutes with \(P_n\). Thus homotopic representatives give equal boundary classes. Adding an identity block to \(u\) adds the same scalar idempotent to both terms of (2.1), after a scalar permutation of coordinates. It therefore leaves their difference unchanged. The finite stable-path definition of \(K_1\) now proves independence of representatives.

*Proof: addition and naturality.* A direct sum of two doubled lifts, followed by the permutation grouping their selected blocks together, is a doubled lift for \(u\oplus v\). Its idempotent and reference idempotent are the direct sums of the two original pairs. Therefore \(\partial[u\oplus v]=\partial[u]+\partial[v]\). Block sum is the group law on \(K_1\), so \(\partial\) is a homomorphism.

If \(\phi:A\to A'\) sends \(J\) into \(J'\), it induces \(\phi_J:J\to J'\) and \(\bar\phi:B\to B'\). The external extension \(\phi^+\) sends \(w\) to an invertible lift of the doubled image representative and sends \(P_n\) to \(P_n\). Applying it to (2.1) gives

\[
(\phi_J)_*\partial=\partial'(\bar\phi)_*.
\tag{2.2}
\]

This proves naturality, including nonunital morphisms of extensions. \(\square\)

## 3. What a zero \(K_0\)-difference provides

The passage from a group equality to a conjugator requires stabilization. We isolate it before proving exactness.

**Lemma 3.1 (identity and zero padding).** Let \(D\) be a unital Banach algebra in the stated setting. If idempotents \(e,f\) have equal classes in \(K_0(D)\), then, after adding the same identity and zero blocks to each, they are joined by an idempotent path in one finite matrix algebra over \(D\). Consequently a conjugator in its invertible identity component carries one padded idempotent to the other.

*Proof.* In a group completion, \([e]=[f]\) means that a finite stable idempotent class \([c]\) satisfies \([e]+[c]=[f]+[c]\) in the monoid. Add the complementary idempotent \(1-c\) on both sides. Since \(c\oplus(1-c)\) is algebraically equivalent to an identity block, we get \([e]+[1_l]=[f]+[1_l]\) for some finite \(l\). The complementary-summand identity follows either from the identity-denominator proof in the third lesson or directly from the maps \(x\mapsto(cx,(1-c)x)\) and \((y,z)\mapsto y+z\).

Thus \(e\oplus1_l\) and \(f\oplus1_l\) are algebraically equivalent after finite zero padding. The first lesson, §3, turns this equivalence into an idempotent homotopy after further zero padding. Its Theorem 2.4 transports that path by an invertible path starting at 1. The final invertible is the asserted conjugator. No cancellation hypothesis on the monoid has been used. \(\square\)

**Lemma 3.2 (removing the scalar conjugator).** Suppose \(e,P\in M_m(J^+)\) are idempotents with the same scalar matrix \(P\), where \(P\) itself is a scalar idempotent. If \(xPx^{-1}=e\), then \(a=\epsilon_J(x)\) commutes with \(P\), and \(y=xa^{-1}\) has scalar part 1 and still satisfies \(yPy^{-1}=e\).

*Proof.* Apply augmentation to the conjugation identity: \(aPa^{-1}=P\). Therefore \(a\) commutes with \(P\), and

\[
(xa^{-1})P(ax^{-1})=xPx^{-1}=e.
\]

The scalar part of \(xa^{-1}\) is 1. \(\square\)

The same normalization works in \(A^+\). If the conjugator \(x\) was obtained from an invertible path \(x(t)\) starting at 1, normalize the entire path by \(x(t)\epsilon_A(x(t))^{-1}\). Its final value still conjugates \(P\) to \(e\) when their scalar matrices agree, and it belongs to the normalized identity component.

## 4. Exactness at the four interior groups

**Theorem 4.1.** The spliced sequence

\[
K_1(J)\xrightarrow{\iota_*}K_1(A)
\xrightarrow{\pi_*}K_1(B)
\xrightarrow{\partial}K_0(J)
\xrightarrow{\iota_*}K_0(A)
\xrightarrow{\pi_*}K_0(B)
\tag{4.1}
\]

is exact at \(K_1(A),K_1(B),K_0(J),K_0(A)\). This makes no endpoint injectivity or surjectivity assertion.

*At \(K_1(A)\).* The composite from \(J\) to \(B\) is zero, so its induced composite is zero. Conversely represent a kernel class by normalized \(u\) over \(A^+\). After identity stabilization its quotient is in the normalized identity component over \(B^+\). Lemma 1.1 gives a normalized lift \(v\) in the identity component over \(A^+\) with \(\pi^+(v)=\pi^+(u)\). Then \(v^{-1}u\in G^1(J)\) and \([v^{-1}u]=[u]\) in \(K_1(A)\), since \([v]=0\). This realizes every kernel class from \(K_1(J)\).

*At \(K_1(B)\): the easy inclusion.* If a representative \(u\) has an invertible lift \(c\), use \(\operatorname{diag}(c,c^{-1})\) in (2.1). It commutes with \(P_n\), so its boundary is zero. Consequently \(\partial\pi_*=0\).

*At \(K_1(B)\): a zero boundary gives an exact lift.* Suppose \(\partial[u]=0\), with doubled lift \(w\) and \(e=wP_nw^{-1}\). Then \([e]=[P_n]\) in \(K_0(J^+)\). Lemma 3.1 supplies equal identity and zero padding making \(e\) conjugate to the padded scalar idempotent. Add an identity block to \(w\) on every added coordinate, so it still conjugates the padded reference to the padded \(e\). A common scalar permutation puts the reference in the form \(P=\operatorname{diag}(1_r,0_s)\). The quotient of the padded lift is then

\[
\pi^+(w)=\operatorname{diag}(u\oplus1_l,u^{-1}\oplus1_k)
\]

for some \(l,k\geq0\); the first block has size \(r\).

Let \(x\in GL_{r+s}(J^+)\) conjugate \(P\) to this padded \(e\). Lemma 3.2 replaces it by \(y\in G_{r+s}^1(J)\) with the same conjugation. Then \(y^{-1}w\) commutes with \(P\). Relative to the two scalar summands it is therefore block diagonal, say \(\operatorname{diag}(c,d)\), with both blocks invertible. Its quotient is unchanged, because \(\pi^+(y)=1\). The first block \(c\) is an exact normalized invertible lift of \(u\oplus1_l\). Thus \([u]\) is in the image of \(K_1(A)\). This proves \(\ker\partial=\operatorname{im}\pi_*\), and proves the stronger representative lifting statement used in Exercise 7.5.

*At \(K_0(J)\): the easy inclusion.* The two idempotents in (2.1) are conjugate over \(A^+\). Their difference is zero there. Since \(K_0(A)\) is a subgroup of \(K_0(A^+)\), this says \(\iota_*\partial=0\).

*At \(K_0(J)\): a kernel difference is a boundary.* By the fourth lesson's normal form, represent a class by \([e]-[P]\), where \(e\in M_m(J^+)\), \(P=\operatorname{diag}(1_r,0_{m-r})\) and \(\epsilon_J(e)=P\). Suppose its image in \(K_0(A)\) is zero. Thus \([e]=[P]\) over \(A^+\). Lemma 3.1 gives common identity and zero padding and a conjugator \(w\) in the invertible identity component over \(A^+\), with

\[
e=wPw^{-1}.
\tag{4.2}
\]

Here and in the rest of this argument the symbols denote the padded matrices. Normalize \(w\) by its scalar part as in Lemma 3.2 and the paragraph following it. The scalar part commutes with \(P\), and the normalized \(w\) remains in the normalized identity component. Since \(\pi^+(e)=P\), its quotient commutes with \(P\). Hence

\[
\pi^+(w)=\operatorname{diag}(c,d),
\qquad [c]+[d]=0\quad\hbox{in }K_1(B).
\tag{4.3}
\]

Add identities to the selected block of both \(e,P\), and zeros to their complementary block, extending \(w\) by identities. Such padding preserves the difference. It lets us make the sizes of \(c,d\) equal. Since \([d]=[c^{-1}]\), further identity stabilization makes \(d\) and \(c^{-1}\) connected in a common normalized invertible group. Thus \(d^{-1}c^{-1}\) is in that group's identity component. Lemma 1.1 gives an invertible normalized lift \(V\) of it. Now use

\[
z=w\operatorname{diag}(1,V).
\tag{4.4}
\]

The correcting matrix is on the right and commutes with \(P\). Consequently \(zPz^{-1}=e\) exactly. Its quotient is

\[
\operatorname{diag}(c,d)\operatorname{diag}(1,d^{-1}c^{-1})
=\operatorname{diag}(c,c^{-1}).
\]

So \(z\) is a doubled lift for \(c\), and (2.1) gives \([e]-[P]=\partial[c]\). This proves \(\ker\iota_*=\operatorname{im}\partial\).

*At \(K_0(A)\).* This is exactly the half-exactness theorem of the fourth lesson, Theorem 3.1. Its proof uses finite idempotent equivalences, identity complements and the elementary doubled lift, so it applies to the stated normed local setting as well. The preceding arguments use only those same finite-matrix facts and the logarithmic lifting of Lemma 1.1. This completes exactness in all the stated cases. \(\square\)

**Corollary 4.2 (split extensions).** If \(\pi\) has a bounded homomorphic section \(s:B\to A\), then \(\partial=0\), and

\[
0\longrightarrow K_1(J)\longrightarrow K_1(A)
\longrightarrow K_1(B)\longrightarrow0
\tag{4.5}
\]

is split exact. The corresponding split \(K_0\)-sequence is the fourth lesson's Theorem 4.1.

*Proof.* The unital extension \(s^+\) lifts every normalized invertible, so (2.1) gives \(\partial=0\); also \(\pi_*s_*=1\). To prove injectivity on the left, suppose a normalized matrix over \(J^+\) becomes nullhomotopic over \(A^+\), after stabilization. Let \(h(t)\) be a normalized path from that matrix to 1. Then

\[
s^+(\pi^+(h(t)))^{-1}h(t)
\]

is a normalized invertible path over \(J^+\) with the same endpoints, since its quotient is 1. Thus the original \(J\)-class was zero. Middle exactness is Theorem 4.1, and the section supplies the splitting. \(\square\)

## 5. The partial-isometry formula

Let \(A\) be a C*-algebra. Suppose normalized unitary \(u\) over \(B^+\) has a partial-isometry lift \(v\in M_n(A^+)\). Its scalar part is 1. Write

\[
p=1-vv^*,\qquad q=1-v^*v.
\]

These are projections in \(M_n(J)\), since the quotient of \(v\) is unitary. Put

\[
W=\begin{pmatrix}v&p\\q&v^*\end{pmatrix}.
\tag{5.1}
\]

**Proposition 5.1.** The matrix \(W\) is a normalized unitary lift of \(\operatorname{diag}(u,u^*)\), and

\[
\partial[u]=[1-v^*v]-[1-vv^*]=[q]-[p].
\tag{5.2}
\]

*Proof.* The partial-isometry relations give \(pv=0\), \(vq=0\), and their adjoints \(v^*p=0\), \(qv^*=0\). Both \(p,q\) are idempotent. Thus

\[
W^*W=
\begin{pmatrix}v^*v+q&0\\0&p+vv^*\end{pmatrix}=1,
\qquad
WW^*=
\begin{pmatrix}vv^*+p&0\\0&q+v^*v\end{pmatrix}=1.
\]

The off-diagonal entries in the quotient vanish, giving the required doubled quotient; scalar augmentation gives the identity. Moreover

\[
WP_nW^*=\operatorname{diag}(vv^*,q).
\]

To simplify the resulting difference in \(K_0(J)\), note that \(p\) belongs to \(J\) and \(vv^*=1-p\) belongs to \(J^+\). The complementary-summand identity in \(J^+\) gives \([vv^*]+[p]=[1_n]\). Hence

\[
[WP_nW^*]-[P_n]=[vv^*]+[q]-[1_n]=[q]-[p],
\]

as asserted. \(\square\)

For a unital extension and an ordinary unitary \(u\in M_n(B)\) with ordinary partial-isometry lift \(v\in M_n(A)\), apply this calculation directly with the ordinary units. Equivalently, replace \(v\) in the external unitization by \(v+(1_{\mathrm{ext}}-1_A)1_n\). The resulting defect projections are the same ordinary \(1_A-v^*v\) and \(1_A-vv^*\) in \(J\), and the two unitization conventions agree by the fourth and sixth lessons.

A partial-isometry lift is an additional hypothesis in this proposition. Definition 2.1 works without it, by the elementary invertible lift.

## 6. The Fredholm sign and a cone extension

**Theorem 6.1.** For an infinite-dimensional Hilbert space \(H\), the extension

\[
0\longrightarrow\mathcal K(H)\longrightarrow B(H)
\xrightarrow{\pi}Q(H)\longrightarrow0
\]

has connecting map

\[
\partial[\pi(T)]
=\dim\ker T-\dim\ker T^*
=\operatorname{Ind}(T)
\tag{6.1}
\]

under the rank normalization \(K_0(\mathcal K(H))\cong\mathbb Z\), for every Fredholm \(T\), and for finite matrices by acting on \(H^n\). Thus \(\partial=-\kappa_*\) in the notation of the preceding lesson.

*Proof.* The Fredholm prerequisite gives closed range and finite-dimensional defects. In the polar decomposition \(T=v|T|\), the projections \(1-v^*v\) and \(1-vv^*\) are precisely the kernel and cokernel projections, so they are finite rank. In the quotient, \(\pi(v)\) is unitary and \(\pi(|T|)\) is positive invertible, by its Corollary 1.2. The positive logarithm joins \(\pi(|T|)\) to 1, so \([\pi(T)]=[\pi(v)]\). Proposition 5.1 applies to \(v\). The fourth lesson identifies a finite-rank projection's class with its rank, giving (6.1). The proof uses no separability assumption. Changing the Fredholm lift by a compact operator leaves the index unchanged by the prerequisite's Corollary 3.3, in agreement with the lift independence already proved for \(\partial\). \(\square\)

On \(\ell^2(\mathbb N_0)\), let \(S\varepsilon_j=\varepsilon_{j+1}\). Then \(S^*S=1\) and \(SS^*=1-p_0\), where \(p_0\) is rank one. Therefore

\[
\partial[\pi(S)]=-[p_0]=-1.
\tag{6.2}
\]

The preceding lesson proves \(K_1(B(H))=0\) and \(K_1(Q(H))\cong\mathbb Z\). Thus the quotient map on \(K_1\) is not surjective. In fact (6.1) and the preceding lesson's Calkin computation make this connecting map an isomorphism, with the sign in (6.2).

For any C*-algebra \(D\), define its cone and suspension by

\[
CD=\{f\in C([0,1],D):f(0)=0\},
\qquad
SD=\{f\in C([0,1],D):f(0)=f(1)=0\}.
\tag{6.3}
\]

Evaluation at 1 gives the exact cone extension

\[
0\longrightarrow SD\longrightarrow CD
\xrightarrow{\operatorname{ev}_1}D\longrightarrow0.
\tag{6.4}
\]

Surjectivity follows by lifting \(d\) to the continuous function \(t\mapsto td\); this is a linear lift, not a claimed homomorphic section. The cone contracts through homomorphisms \(f(t)\mapsto f(st)\), so its \(K_0\) and \(K_1\) vanish by homotopy invariance. Theorem 4.1 consequently makes the cone boundary an isomorphism

\[
K_1(D)\xrightarrow{\ \cong\ }K_0(SD).
\tag{6.5}
\]

This prepares the next lesson's suspension picture. With the endpoint convention in (6.3), a doubled lift is a path starting at the identity at 0 and ending at \(\operatorname{diag}(u,u^{-1})\) at 1. Its conjugated idempotent has the same scalar endpoint \(P_n\) at both ends, exactly as required for a class in \(K_0(SD)\).

## 7. Exercises with complete solutions

**Exercise 7.1 — Multiplying the four factors (basic).** Verify (1.1), and expand its lifted version for arbitrary lifts \(a,b\).

*Solution.* First multiply

\[
E(u)F(u^{-1})
=\begin{pmatrix}0&u\\-u^{-1}&1\end{pmatrix}.
\]

Multiplication by \(E(u)\) then gives \(\begin{psmallmatrix}0&u\\-u^{-1}&0\end{psmallmatrix}\); multiplication by \(L\) gives \(\operatorname{diag}(u,u^{-1})\). Both inverse identities \(uu^{-1}=u^{-1}u=1\) have been used. With arbitrary lifts, the same ordered multiplication gives

\[
E(a)F(b)E(a)L
=\begin{pmatrix}a(2-ba)&ab-1\\1-ba&b\end{pmatrix}.
\tag{7.1}
\]

This formula holds without assuming \(ab=ba\). Its inverse is the reversed product

\[
L^{-1}E(-a)F(-b)E(-a),
\]

so the lifted matrix is invertible regardless of the defects \(1-ab,1-ba\). In the quotient those defects vanish and the first diagonal entry is \(u(2-u^{-1}u)=u\), giving (1.1). If both lifts have scalar part 1, the expanded matrix has scalar diagonal entries 1 and scalar off-diagonal entries zero. This also verifies normalization explicitly.

**Exercise 7.2 — Powers of the shift (basic).** Compute \(\partial[\pi(S^k)]\) and \(\partial[\pi((S^*)^k)]\) for \(k\geq0\).

*Solution.* Let \(p_k\) project onto \(\operatorname{span}\{\varepsilon_0,\ldots,\varepsilon_{k-1}\}\), with \(p_0=0\). The shift powers satisfy

\[
(S^k)^*S^k=1,\qquad S^k(S^k)^*=1-p_k.
\]

Their initial defect is zero and their final defect is \(p_k\). Proposition 5.1 therefore gives

\[
\partial[\pi(S^k)]=-[p_k]=-k.
\]

For \((S^*)^k\), the initial defect is \(p_k\) and the final defect is zero, so

\[
\partial[\pi((S^*)^k)]=[p_k]=k.
\]

Both are zero for \(k=0\). This agrees with additivity, since the quotient shift is unitary and its adjoint represents its inverse class. The formula uses kernel minus cokernel throughout.

**Exercise 7.3 — Naturality, including nonunital maps (intermediate).** Prove that the connecting maps commute with a morphism of extensions.

*Solution.* Suppose \(\phi:A\to A'\) maps \(J\) into \(J'\), and \(\pi'\phi=\bar\phi\pi\). External extension makes the same square commute on unitizations, even if \(\phi\) is nonunital. For normalized \(u\) choose an invertible doubled lift \(w\). Then \(\phi^+(w)\) has quotient

\[
\operatorname{diag}(\bar\phi^+(u),\bar\phi^+(u)^{-1}).
\]

Since \(\phi^+\) is unital, it fixes every scalar entry of \(P_n\), and it preserves inverses. Its restriction to \(J^+\) is \(\phi_J^+\). Consequently

\[
\begin{aligned}
(\phi_J)_*\bigl([wP_nw^{-1}]-[P_n]\bigr)
&=[\phi^+(w)P_n\phi^+(w)^{-1}]-[P_n]\\
&=\partial'(\bar\phi)_*[u].
\end{aligned}
\]

Lift independence and stabilization, already proved, make this equality valid on all classes. This is (2.2). The other arrows in the exact sequence commute by functoriality of \(K_0,K_1\), so this gives a natural morphism of the entire spliced sequence.

**Exercise 7.4 — Checking the partial-isometry lift (intermediate).** Verify that (5.1) is unitary, compute its conjugated idempotent and derive the defect formula.

*Solution.* Put \(p=1-vv^*\), \(q=1-v^*v\). Partial isometry means \(vv^*v=v\); hence \(p,q\) are projections and \(pv=vq=0\). Taking adjoints gives \(v^*p=qv^*=0\). Since

\[
W^*=\begin{pmatrix}v^*&q\\p&v\end{pmatrix},
\]

the upper-left block of \(W^*W\) is \(v^*v+q^2=1\), the lower-right block is \(p^2+vv^*=1\), and the off-diagonal blocks are \(v^*p+qv^*=0\) and \(pv+vq=0\). Similarly \(WW^*\) has diagonal blocks \(vv^*+p^2=1\), \(q^2+v^*v=1\), and off-diagonal blocks \(vq+pv=0\), \(qv^*+v^*p=0\). Thus \(W^{-1}=W^*\).

Multiplying the first column by its adjoint gives

\[
WP_nW^*
=\begin{pmatrix}vv^*&vq\\qv^*&q^2\end{pmatrix}
=\operatorname{diag}(vv^*,q).
\]

Both defects lie in \(J\), since \(\pi(v)=u\) is unitary. In \(J^+\), \(vv^*=1-p\), so \([vv^*]-[1_n]=-[p]\). Subtracting \([P_n]\) from the computed idempotent class yields \([q]-[p]\), namely the formula (5.2). The calculation makes no assumption that every quotient unitary has such a partial-isometry lift; this exercise uses the stated lift hypothesis.

**Exercise 7.5 — Zero boundary and a stabilized unitary lift (advanced).** Let \(u\) be a normalized unitary over \(B^+\). Show that \(\partial[u]=0\) if and only if, for some finite \(N\), \(u\oplus1_{N-n}\) has an exact normalized unitary lift in \(M_N(A^+)\), where \(u\) has size \(n\). For a unital extension one may use ordinary unitaries and obtain a lift in \(M_N(A)\).

*Solution.* If a unitary lift exists, it is an invertible lift. Its doubled matrix commutes with the reference scalar projection, so (2.1) gives boundary zero. Identity stabilization leaves the boundary unchanged; this proves necessity.

Conversely, the proof of exactness at \(K_1(B)\) in Theorem 4.1 produces an actual normalized invertible \(c\in M_N(A^+)\) with

\[
\pi^+(c)=u\oplus1_{N-n}=:u_N.
\]

It obtains this exact representative by removing the normalized \(J\)-conjugator from a padded doubled lift; it does not merely assert a lift of a homotopy class. Take its polar unitary

\[
v=c(c^*c)^{-1/2}.
\tag{7.2}
\]

Continuous functional calculus makes \(v\) unitary. Both scalar augmentation and the quotient map commute with the positive inverse square root. Since the scalar part of \(c\) is 1, the scalar part of \(v\) is 1. Since \(u_N\) is unitary,

\[
\pi^+(v)=u_N(u_N^*u_N)^{-1/2}=u_N.
\]

This is the required exact normalized unitary lift. The size \(N\) depends on the finite group-completion and homotopy witnesses; boundary zero does not assert a lift at an arbitrarily prescribed smaller size.

If \(A\) is unital and \(u\) is an ordinary unitary in \(M_n(B)\), replace it first by its normalized external representative, as in the preceding lesson, Proposition 1.2. The first component of \(A^+\cong A\oplus\mathbb C\) sends the normalized lift just constructed to an ordinary unitary in \(M_N(A)\), whose quotient is \(u\oplus1\). This proves the asserted unital version and the requested formulation using unitizations. For a nonunital algebra the normalized formulation is the precise meaning of the same statement.

## References and convention checks

The invertible-lift boundary in (2.1) is the convention of Blackadar [B98, Definition 8.3.1] and [B06, V.1.2.12]. The proof here expands the required group-completion stabilization and keeps the correcting block on the right in (4.4), so the idempotent equality is retained literally. The partial-isometry formula is [B98, §8.3.2], [B06, V.1.2.13] and [E24, Lemma 8.6.1].

The existing lesson *Frequency calculus for an action of Euclidean space* in *Cyclic cohomology and noncommutative geometry* uses this boundary in formula (7.1), with kernel-minus-cokernel sign. *Hilbert modules and fields on the leaf space* in *Noncommutative geometry of foliations* uses the expanded parametrix factorization in formula (11) and the same sign in formula (12). Exercise 7.1 verifies that common finite-matrix construction. Neither specialized symbol calculus nor a general Hilbert-module index theorem is needed to prove the exact sequence here.

- [B98] B. Blackadar, *K-Theory for Operator Algebras*, second edition, Cambridge University Press, 1998, §8.3, printed pp. 62–64, especially Definition 8.3.1 and Propositions 8.3.3, 8.3.4 and 8.3.6. [Author's corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).
- [B06] B. Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, Springer, 2006, revised author version 2017, V.1.2.10–V.1.2.17.
- [E24] H. Emerson, *An Introduction to C*-Algebras and Noncommutative Geometry*, Birkhäuser, 2024, §§8.4–8.6, especially Theorem 8.5.11, Lemmas 8.6.1–8.6.2 and Corollary 8.6.3. Its relative-excision construction is not assumed in the direct proof above; the course's relative comparison is proved in the six-term-sequence lesson.
- *Fredholm operators and the stable index*, in *Foundations of von Neumann algebras: remaining topics*, Theorem 1.1 and Corollary 1.2 for the Fredholm polar facts, and Corollary 3.3 for compact-perturbation invariance. Its \(\kappa\) is the negative of \(\operatorname{Ind}\) in (6.1), as already fixed in the preceding lesson.

[Blackadar’s freely readable revised Operator Algebras](https://www.bruceblackadar.com/Mathematics/Cycr.pdf).
