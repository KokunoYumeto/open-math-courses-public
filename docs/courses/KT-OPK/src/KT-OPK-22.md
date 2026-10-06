# Cuntz algebras

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The Cuntz relations allow the identity to be decomposed into several projections, each equivalent to the identity. This makes the algebras very different from the finite algebras studied earlier. Their gauge-fixed algebra is nevertheless a familiar UHF algebra. We use that core, a full corner, Takai duality and the Pimsner–Voiculescu sequence to compute the K-groups, keeping track of the unit throughout.

We use the [PV sequence](KT-OPK-18.md#1-the-sequence-and-the-proof-inputs), the [UHF calculation](KT-OPK-16.md), and the precise crossed-product inputs listed below. Write \(\mathcal K\) for the compact operators on a separable infinite-dimensional Hilbert space. Haar measure on \(\mathbb T\) has mass one.

## 1. The universal relations

For an integer \(2\leq n<\infty\), the unital C*-algebra \(\mathcal O_n\) is universal for isometries satisfying

\[
s_i^*s_i=1,\qquad
\sum_{i=1}^n s_i s_i^*=1.
\tag{1.1}
\]

These relations imply orthogonality. Put \(q_i=s_i s_i^*\). Multiplying their sum by \(q_i\) on both sides gives
\(\sum_{j\ne i}q_iq_jq_i=0\). Every summand is positive, so \(q_jq_i=0\) for \(j\ne i\). Consequently

\[
s_i^*s_j=\delta_{ij}1.
\tag{1.2}
\]

There is a nonzero model: on the Hilbert space with orthonormal basis indexed by infinite words in \(\{1,\ldots,n\}\), let \(S_i\) prepend the letter \(i\). Its range consists of words beginning with \(i\); those ranges partition the basis. Thus (1.1) holds. The universal construction is legitimate: each generator has norm one in every representation, so the norm of any fixed *-polynomial is bounded by the sum of the absolute values of its coefficients. The supremum representation seminorm, quotient by its null space, and completion give the universal C*-algebra. The model shows its identity is nonzero.

For a finite word \(\mu=(\mu_1,\ldots,\mu_r)\), write \(s_\mu=s_{\mu_1}\cdots s_{\mu_r}\), and set \(s_\varnothing=1\). Repeated use of (1.2) cancels the common initial letters in \(s_\mu^*s_\nu\). The product is zero unless one word extends the other; otherwise it is the remaining word or its adjoint. Hence

\[
\overline{\operatorname{span}}
\{s_\mu s_\nu^*: \mu,\nu\text{ finite}\}
=\mathcal O_n.
\tag{1.3}
\]

**Finite simplicity and uniqueness.** Theorem 2.2 below proves Cuntz’s simplicity theorem and the resulting uniqueness of every nonzero family satisfying (1.1). The proof uses the finite-word compression in Lemma 2.1 and the gauge core, without an additional representation hypothesis.

The algebra \(\mathcal O_\infty\) is universal for countably many isometries satisfying (1.2). Every finite sum of their range projections is at most one. There is no relation asserting that an infinite sum equals one in norm. Existence follows by left creation operators on the Hilbert space of finite words over a countable alphabet, including the empty word. We compute its K-theory separately in §6.

## 2. The gauge action and its UHF core

Universality gives automorphisms

\[
\gamma_z(s_i)=zs_i,\qquad z\in\mathbb T.
\tag{2.1}
\]

The inverse is \(\gamma_{\bar z}\). The action is norm continuous on each normal word, hence on polynomials; isometry and norm approximation give point-norm continuity on the completion. The same proof applies to \(\mathcal O_\infty\).

Let \(F_n=\mathcal O_n^\gamma\). Averaging defines a conditional expectation

\[
E(a)=\int_{\mathbb T}\gamma_z(a)\,dz.
\tag{2.2}
\]

It is positive, contractive, unital, and fixes the fixed algebra. Its bimodule property follows by moving fixed coefficients outside the integral. It is faithful: if \(E(a^*a)=0\), every positive functional gives a zero integral of a nonnegative continuous function. Such a function vanishes everywhere because Haar measure has full support. Its value at the identity is zero for all positive functionals, so \(a^*a=0\).

Averaging (1.3) keeps exactly the terms with \(|\mu|=|\nu|\). At length \(r\), these terms form matrix units:

\[
\begin{gathered}
e_{\mu\nu}=s_\mu s_\nu^*,\qquad
e_{\mu\nu}e_{\kappa\lambda}
=\delta_{\nu\kappa}e_{\mu\lambda},\\
e_{\mu\nu}^*=e_{\nu\mu},\qquad
\sum_{|\mu|=r}e_{\mu\mu}=1.
\end{gathered}
\tag{2.3}
\]

Each diagonal entry is nonzero since \(s_\mu\) is an isometry. Thus the resulting unital map from \(M_{n^r}(\mathbb C)\) is injective. Inserting (1.1) between a word and an adjoint gives the inclusion

\[
s_\mu s_\nu^*
=\sum_{i=1}^n s_{\mu i}s_{\nu i}^*.
\tag{2.4}
\]

With the lexicographic ordering of the appended letter, this is \(x\mapsto x\otimes1_n\). The closure of these increasing matrix algebras is all of \(F_n\), by the averaged normal-word density. We have proved

\[
\begin{gathered}
F_n\cong\operatorname*{lim}_{r\to\infty}M_{n^r}(\mathbb C),\\
K_0(F_n)=\mathbb Z[1/n],\\
[1_{F_n}]=1,\qquad K_1(F_n)=0.
\end{gathered}
\tag{2.5}
\]

The group assertion uses Lesson 16: rank-one generators are multiplied by \(n\) under (2.4), and normalized rank at stage \(r\) is divided by \(n^r\).

### Finite-word compression proves simplicity

**Lemma 2.1 (removing nonzero degrees).** Given finitely many normal words \(s_\alpha s_\beta^*\) with \(|\alpha|\ne|\beta|\), there is a word \(\nu\) for which

\[
\begin{gathered}
s_\nu^*s_\alpha s_\beta^*s_\nu=0\\
\text{for every listed pair}.
\end{gathered}
\tag{2.6}
\]

*Proof.* Choose \(L\geq1\) at least the length of every \(\alpha\) and \(\beta\), and take

\[
\nu=\underbrace{1\cdots1}_{L}\,2\,
\underbrace{1\cdots1}_{L}.
\tag{2.7}
\]

The letter 2 is available because \(n\geq2\). If either \(\alpha\) or \(\beta\) is not a prefix of \(\nu\), cancellation makes (2.6) zero. Otherwise put \(r=|\alpha|\), \(t=|\beta|\); the compressed product is the adjoint of the tail of \(\nu\) after \(r\) letters times the tail after \(t\) letters. Suppose \(r<t\); the reverse case follows by adjoint. In these two tails the unique letter 2 occurs at positions \(L+1-r\) and \(L+1-t\). At the earlier of those positions the letters differ, and that position lies within both tails, since \(0\leq r<t\leq L\). Neither tail is a prefix of the other. Their product is therefore zero by (1.2). This also covers empty words. \(\square\)

**Theorem 2.2 (Cuntz simplicity and uniqueness).** For \(2\leq n<\infty\), every nonzero positive \(a\in\mathcal O_n\) admits \(y\in\mathcal O_n\) with

\[
y^*ay=1.
\tag{2.8}
\]

Consequently \(\mathcal O_n\) is simple, and any family satisfying (1.1) in a nonzero unital C*-algebra generates a copy of \(\mathcal O_n\), without an additional gauge-equivariance assumption.

*Proof.* The faithful expectation gives \(E(a)\ne0\). Set \(t=\|E(a)\|>0\), and choose \(0<\varepsilon<t/3\). Normal-word density gives a self-adjoint polynomial \(b\) with \(\|a-b\|<\varepsilon\): first approximate \(a\), then take the self-adjoint part. Its constant-degree part \(E(b)\) lies in some matrix stage \(F_r\cong M_{n^r}(\mathbb C)\), since any equal-length word can be expanded to a common length by (2.4). Its largest eigenvalue \(\lambda\) is at least \(t-\varepsilon\). Indeed, \(\|E(a)-E(b)\|<\varepsilon\) implies
\(E(a)\leq E(b)+\varepsilon1\leq(\lambda+\varepsilon)1\), and taking the norm of the positive \(E(a)\) proves the bound.

Choose a word \(\mu\) of length \(r\). Finite-dimensional diagonalization supplies a unitary \(w\in F_r\) such that

\[
s_\mu^*w^*E(b)ws_\mu=\lambda1.
\tag{2.9}
\]

To see the scalar assertion, the corner of \(F_r\) at \(s_\mu s_\mu^*\) is one-dimensional; choose \(w\) to carry its coordinate vector to a \(\lambda\)-eigenvector. Compression by \(s_\mu\) then identifies that corner with scalars.

The element \(c=s_\mu^*w^*bws_\mu\) is another finite normal-word polynomial. Because \(w\) has degree zero and \(s_\mu\) has degree \(r\), averaging gives \(E(c)=\lambda1\). Thus \(c-\lambda1\) is a finite sum of normal words of nonzero degree. Lemma 2.1 supplies \(\nu\) killing all those words, so the isometry \(v=ws_\mu s_\nu\) satisfies

\[
\begin{gathered}
v^*bv=\lambda1,\\
\|v^*av-\lambda1\|<\varepsilon.
\end{gathered}
\tag{2.10}
\]

Here \(\lambda\geq t-\varepsilon>\varepsilon\). Therefore \(v^*av\) is positive and invertible, with lower bound \((\lambda-\varepsilon)1\). Put \(y=v(v^*av)^{-1/2}\). Continuous functional calculus proves (2.8).

If \(J\) is a nonzero closed two-sided ideal, choose \(z\in J\setminus\{0\}\); then \(a=z^*z\) is nonzero, positive and in \(J\). Equation (2.8) places \(1\) in \(J\), so \(J=\mathcal O_n\). Finally universality sends \(\mathcal O_n\) onto the algebra generated by any given nonzero Cuntz family. The map is unital, so its kernel is proper; simplicity makes it zero. \(\square\)

This proves the finite simplicity and uniqueness theorem credited to Cuntz, using only the relations, the explicitly computed matrix core and faithful gauge averaging. The word in (2.7) explains why finite Fourier degrees can be eliminated while the positive constant-degree compression survives.

## 3. A full corner and the actual dual action

Set \(D=\mathcal O_n\rtimes_\gamma\mathbb T\), using the full crossed product. Denote its canonical group multipliers by \(\lambda_z\), and suppress the coefficient multiplier map in products. Define

\[
p_k=\int_{\mathbb T}z^{-k}\lambda_z\,dz,
\qquad k\in\mathbb Z.
\tag{3.1}
\]

These are mutually orthogonal projections in \(D\). This follows either from the integrated group multiplication or Fourier orthogonality. The compact-group corner theorem [KT-CP, Lesson 9, Theorem 9.6] identifies

\[
F_n\longrightarrow p_0Dp_0,
\qquad a\longmapsto ap_0
\tag{3.2}
\]

as an isomorphism. This theorem does not assert fullness for arbitrary compact actions; we now prove it here.

Covariance \(\lambda_zs_i\lambda_z^*=zs_i\) gives
\(p_ks_i=s_ip_{k-1}\). For a word of length \(r\), it follows that

\[
\begin{gathered}
s_\mu^*p_0s_\mu=p_{-r},\\
\sum_{|\mu|=r}s_\mu p_0s_\mu^*=p_r.
\end{gathered}
\tag{3.3}
\]

For the second identity, \(s_\mu p_0=p_rs_\mu\), and the range projections of all length-\(r\) words sum to one. The ideal \(I=\overline{Dp_0D}\) is preserved by multiplier multiplication. Hence (3.3) puts every \(p_k\) in \(I\). Finite sums of scalar characters are uniformly dense in \(C(\mathbb T)\); finite sums of scalar functions times coefficients approximate every continuous coefficient-valued function uniformly. The integrated norm is bounded by its \(L^1\)-norm. Thus the span of \(ap_k\) is dense in \(D\), and every such product belongs to \(I\). Therefore \(I=D\).

Full-corner Morita invariance, with the corner inclusion as the induced K-map, now gives

\[
\begin{gathered}
K_0(D)=\mathbb Z[1/n],\\
[p_0]=1,\qquad K_1(D)=0.
\end{gathered}
\tag{3.4}
\]

Here the algebras are separable, so the Morita prerequisite in [KT-CP, Lesson 9, “K-theory and two free actions”] applies.

Our dual convention is positive: the generator \(\sigma\) of the dual \(\mathbb Z\)-action fixes coefficients and satisfies

\[
\sigma(\lambda_z)=z\lambda_z,
\qquad \sigma(p_k)=p_{k-1}.
\tag{3.5}
\]

The partial isometries \(s_ip_k\) have initial projection \(p_k\), mutually orthogonal final projections, and the sum of their final projections is \(p_{k+1}\). They belong to \(D\), so

\[
[p_{k+1}]=n[p_k],\qquad [p_k]=n^k[p_0].
\tag{3.6}
\]

In particular \(\sigma_*[p_0]=[p_{-1}]=1/n\). An additive endomorphism of \(\mathbb Z[1/n]\) is determined by its value on one: the equation \(n^r x=1\) has a unique solution in this torsion-free group. Consequently

\[
\sigma_*(x)=x/n.
\tag{3.7}
\]

Using the inverse dual generator gives multiplication by \(n\). These two conventions give the same kernel and quotient calculation, but we retain (3.7) for the maps just constructed.

## 4. The PV calculation, including the unit

Takai duality [KT-CP, Lesson 8, Theorem 8.3] gives

\[
D\rtimes_\sigma\mathbb Z
\cong\mathcal O_n\otimes\mathcal K(L^2(\mathbb T)).
\tag{4.1}
\]

Its actual generator formula [there, Proposition 8.4, (8.15)] sends \(\lambda_z\) to right translation \(\xi(x)\mapsto\xi(xz)\). Averaging these translations is the rank-one projection \(e\) onto constant functions. Therefore the coefficient inclusion \(\iota:D\to D\rtimes\mathbb Z\), followed by (4.1), sends

\[
\iota(p_0)\longmapsto1_{\mathcal O_n}\otimes e.
\tag{4.2}
\]

This is why the normalized class one in (3.4) becomes the unit class of \(\mathcal O_n\) after stability. An abstract group isomorphism alone would not establish that identification.

Since \(K_1(D)=0\), the PV sequence reduces to

\[
\begin{gathered}
K_1(\mathcal O_n)\cong\ker(1-\sigma_*),\\
K_0(\mathcal O_n)\cong\operatorname{coker}(1-\sigma_*).
\end{gathered}
\tag{4.3}
\]

On \(\mathbb Z[1/n]\), the map \(1-\sigma_*\) is multiplication by \((n-1)/n\). It is injective, and its image is \((n-1)\mathbb Z[1/n]\), because multiplication by \(n\) is invertible. The quotient map is

\[
\begin{aligned}
\mathbb Z[1/n]&\longrightarrow\mathbb Z/(n-1)\mathbb Z,\\
a/n^r&\longmapsto a\pmod{n-1}.
\end{aligned}
\tag{4.4}
\]

It is well defined: equal fractions give equal integers after cross multiplication, and \(n\equiv1\) modulo \(n-1\). It is onto and its kernel consists exactly of fractions whose numerator is divisible by \(n-1\). Combining (4.2)–(4.4) proves the result with its distinguished class.

**Theorem 4.1.** For \(2\leq n<\infty\),

\[
\begin{gathered}
K_0(\mathcal O_n)\cong\mathbb Z/(n-1)\mathbb Z,\\
[1]\longmapsto1,\qquad K_1(\mathcal O_n)=0.
\end{gathered}
\tag{4.5}
\]

For \(n=2\) the cyclic group is zero: the identity is a nonzero projection whose K-class is zero. A tracial state cannot exist on any \(\mathcal O_n\), since (1.1) and traciality would give \(1=n\). This also illustrates why the trace methods for rotation algebras cannot be transferred unchanged.

### Tensoring with a finite Cuntz algebra: the torsion term

The scalar groups in Theorem 4.1 do not determine a tensor product merely by multiplying group ranks. Here is a coefficient calculation that also detects torsion; compare [Cuntz 1981 II, §2.1–2.2]. All tensor products in this subsection are minimal.

**Theorem 4.2 (finite Cuntz coefficients).** Let \(A\) be any C*-algebra and \(2\leq n<\infty\). Put \(d=n-1\), \(G_i=K_i(A)\), and \(C_n=A\otimes\mathcal O_n\). The map \(j:A\to C_n\), \(a\mapsto a\otimes1\), fits into the natural cyclic exact sequence whose consecutive arrows are

\[
\begin{gathered}
G_i\xrightarrow{\ d\ }G_i\\
\xrightarrow{\ j_*\ }K_i(C_n)\\
\xrightarrow{\ \partial_i\ }G_{i-1}\\
\xrightarrow{\ d\ }G_{i-1},\qquad i\pmod2.
\end{gathered}
\tag{4.6}
\]

Equivalently, with \(G[d]=\{g\in G:dg=0\}\), there is a natural short exact sequence

\[
\begin{gathered}
0\longrightarrow G_i/dG_i\\
\xrightarrow{\ \overline{j_*}\ }K_i(C_n)\\
\xrightarrow{\ \partial_i\ }G_{i-1}[d]\\
\longrightarrow0.
\end{gathered}
\tag{4.7}
\]

No unitality, separability, nuclearity or torsion-freeness assumption on \(A\) is required. A splitting of (4.7) is not asserted.

*Proof.* Give \(C_n\) the action \(\operatorname{id}_A\otimes\gamma\). Averaging elementary tensors and using their norm density identifies its fixed algebra as \(A\otimes F_n\): the average is \(\operatorname{id}_A\otimes E\), fixes this closed subalgebra and sends a dense algebraic tensor subspace into it. Let

\[
D_A=C_n\rtimes\mathbb T.
\tag{4.8}
\]

The averaging-corner theorem of KT-CP, Lesson 9, Theorem 9.6, identifies \(p_0D_Ap_0\) with \(A\otimes F_n\), also for nonunital \(A\). Now \(p_k\) and \(1\otimes s_\mu\) may be multipliers, so fullness needs a coefficient argument. The algebra \(D_A\) has dense span of \(cp_k\), \(c\in C_n\), by the character approximation used in §3. Here is the coefficient argument explicitly. Suppress \(1\otimes\) in word multipliers and write \(a\) for \(a\otimes1\). If \((e_\lambda)\) is an approximate identity of \(A\) and \(|\mu|=r\), the two factors in each of

\[
\begin{gathered}
(a s_\mu^*p_0)(e_\lambda p_0s_\mu)
       =a e_\lambda p_{-r},\\
\sum_{|\mu|=r}(a s_\mu p_0)(e_\lambda p_0s_\mu^*)
       =a e_\lambda p_r
\end{gathered}
\]

belong to \(D_A\), since a coefficient times a word is in \(C_n\) and multiplying it by a Fourier projection gives an element of \(D_A\). The products lie in the ideal \(I=\overline{D_Ap_0D_A}\), since each first factor ends in \(p_0\). Their limits put \(ap_{-r}\) and \(ap_r\) in \(I\). For \(r=0\), \((ap_0)(e_\lambda p_0)\to ap_0\) proves the same assertion. Multiplication by the word multipliers and density of normal words put every \(cp_k\) in the same ideal. Thus \(p_0\) is full. The arbitrary full-multiplier-corner K-theorem [Hilbert C*-modules, Lesson 14, Theorem 2.4], already used in §6 below, gives the corner inclusion isomorphisms in both degrees.

The finite stages of the core are \(M_{n^r}(A)\), with connecting map consisting of \(n\) identical blocks. Matrix stability and continuity therefore identify

\[
\begin{gathered}
K_i(D_A)\cong H_i,\\
H_i=\operatorname*{lim}\bigl(G_i\xrightarrow{\ n\ }G_i\\
\xrightarrow{\ n\ }G_i\longrightarrow\cdots\bigr).
\end{gathered}
\tag{4.9}
\]

Write a stage class as \(g/n^r\), and write \(\lambda_i:G_i\to H_i\), \(g\mapsto g/1\). These are algebraic localization symbols: \(\lambda_i\) can have a kernel when \(G_i\) has \(n\)-power torsion. In particular no injection into a rational vector space is assumed. Multiplication by \(n\) on \(H_i\) is invertible.

With the dual convention (3.5), the induced map on \(H_i\) is multiplication by \(1/n\), in both degrees. To verify this beyond scalar ranks, conjugate the \(p_{-1}\) corner into \(p_0\) by \(1\otimes s_1\). On the core this is the corner embedding \(b\mapsto(1\otimes s_1)b(1\otimes s_1^*)\). It sends a matrix class at stage \(r\) to the *same* class at stage \(r+1\), while the connecting core embedding sends it to \(n\) times that class. Hence it sends \(g/n^r\) to \(g/n^{r+1}\). Supported partial-isometry equivalence and matrix stability identify this corner conjugation with the induced dual map for both \(K_0\) and \(K_1\); normalized unitary representatives have identity on the complementary corner, as in Lesson 6. This proves the stated map without restricting coefficient groups to their ranks.

Takai duality, with its exact generator formulas, identifies \(D_A\rtimes_\sigma\mathbb Z\) with \(C_n\otimes\mathcal K(L^2(\mathbb T))\). Formula (4.2) now reads \(ap_0\mapsto j(a)\otimes e\). Thus the PV coefficient inclusion, under stability, is the map induced by \(j\) after \(\lambda_i\). The PV sequence of Lesson 18 has consecutive maps

\[
\begin{gathered}
H_i\xrightarrow{\ d/n\ }H_i\\
\xrightarrow{\ \iota_*\ }K_i(C_n)\\
\xrightarrow{\ \delta_i\ }H_{i-1}\\
\xrightarrow{\ d/n\ }H_{i-1},\\
\iota_*\lambda_i=j_*.
\end{gathered}
\tag{4.10}
\]

We finish the required algebraic comparison explicitly. For any abelian group \(G\) and \(H=\operatorname{lim}(G,\times n)\), the stage map induces isomorphisms

\[
\begin{gathered}
G/dG\cong H/dH,\\
G[d]\cong H[d].
\end{gathered}
\tag{4.11}
\]

For the first, send \(g/n^r\) modulo \(dH\) to \(g\) modulo \(dG\). A direct-limit equality says that after a further power of \(n\), the two cross-multiplied numerators agree. Since \(n\equiv1\pmod d\), their residues agree. This defines an inverse to the stage map: in \(H/dH\), multiplication by \(n\), and hence by \(n^{-1}\), is identity. For the second, if \(a\in G[d]\), then \(na=a\). If its stage image is zero, some \(n^sa\) is zero, so \(a=0\). Conversely, \(h=g/n^r\in H[d]\) means some \(n^s dg=0\). Set \(a=n^sg\); then \(da=0\) and \(h=a/n^{r+s}=\lambda(a)\), since \(n\) acts identically on elements killed by \(d\). This proves both assertions even with arbitrary torsion.

Because \(n\) is invertible on \(H_i\), multiplication by \(d/n\) has image \(dH_i\) and kernel \(H_i[d]\). Define \(\partial_i\) by applying \(\delta_i\) and then the inverse of the second map in (4.11). PV exactness, the first map in (4.11), and \(\iota_*\lambda_i=j_*\) now give (4.7), hence all six exact positions in (4.6). All corner, stage and boundary constructions commute with coefficient homomorphisms. The two algebraic comparison maps do too, proving naturality. No tensoring of an arbitrary short exact sequence, nor a general Künneth theorem, was used. \(\square\)

**Example 4.3 (a torsion tensor product).** For \(m,n\geq2\), put \(h=\gcd(m-1,n-1)\). Apply Theorem 4.2 to \(A=\mathcal O_m\). Its coefficient groups are \(G_0=\mathbb Z/(m-1)\) and \(G_1=0\), so

\[
\begin{gathered}
K_0(\mathcal O_m\otimes\mathcal O_n)\cong\mathbb Z/h,\\
K_1(\mathcal O_m\otimes\mathcal O_n)\cong\mathbb Z/h.
\end{gathered}
\tag{4.12}
\]

The degree-zero unit maps to \(1\) modulo \(h\). In degree one, the boundary is an isomorphism onto the subgroup of \(\mathbb Z/(m-1)\) killed by \(n-1\), generated by \((m-1)/h\); it specifies a generator of the degree-one group. For \(h=1\), both groups are zero. For \(m=n=3\), both are \(\mathbb Z/2\), even though each individual factor has zero \(K_1\). Thus omitting the torsion kernel would give a wrong answer. Formula (4.7) also shows \(K_*(A\otimes\mathcal O_2)=0\) for *every* \(A\), since \(d=1\). These are proved special tensor formulas, rather than an assertion of a general Künneth theorem.

## 5. Isomorphisms and matrix size

If \(\mathcal O_n\cong\mathcal O_m\), the finite K-zero groups have the same cardinality, so \(n-1=m-1\). In fact \(\mathcal O_n\) cannot be isomorphic to \(M_k(\mathcal O_m)\) when \(n\ne m\), since stability leaves that group cardinality unchanged.

For a fixed \(n\), stability identifies the unit of \(M_k(\mathcal O_n)\) with \(k[1]\). A unital isomorphism from \(\mathcal O_n\) must send its generating unit class to that class. In the cyclic group of order \(n-1\), the residue \(k\) generates exactly when

\[
\gcd(k,n-1)=1.
\tag{5.1}
\]

Thus (5.1) is necessary. Theorem 5.1 below proves its sufficiency by explicit generators, following Abrams, Ánh and Pardo. We use the assertion for these particular Cuntz algebras. In Blackadar’s definition (§6.11.4), “purely infinite” already entails simplicity; his surrounding broader classification statement also assumes separability, nuclearity and the bootstrap condition.

There is an elementary construction when \(k=1+r(n-1)\), \(r\geq0\). Start with the single isometry \(1\). Replacing one member \(t\) of an orthogonal family by \(ts_1,\ldots,ts_n\) preserves its total range projection and increases its size by \(n-1\). After \(r\) replacements we have \(k\) isometries \(t_1,\ldots,t_k\) with orthogonal ranges summing to one. The row \(T=(t_1,\ldots,t_k)\) satisfies \(T^*T=1_k\) and \(TT^*=1\). Hence

\[
\begin{gathered}
M_k(\mathcal O_n)\longrightarrow\mathcal O_n,\\
X\longmapsto TXT^*
\end{gathered}
\tag{5.2}
\]

is an isomorphism with inverse \(a\mapsto T^*aT\). This proves that congruence case without the general classification theorem.

### The coprime construction

**Theorem 5.1.** For \(n\geq2\) and \(k\geq1\),

\[
\begin{gathered}
M_k(\mathcal O_n)\cong\mathcal O_n\\
\Longleftrightarrow\quad\gcd(k,n-1)=1.
\end{gathered}
\tag{5.3}
\]

*Proof.* Necessity was proved by the unit class in (5.1). We give the constructive sufficiency argument of Abrams, Ánh and Pardo, with all generator and surjectivity checks in the C*-algebra itself.

First, the Cuntz row \((s_1,\ldots,s_n)\), together with \(j-1\) identity rows on disjoint coordinates, is a rectangular unitary from \(j+n-1\) coordinates to \(j\) coordinates. Conjugation by it identifies \(M_{j+n-1}(\mathcal O_n)\) with \(M_j(\mathcal O_n)\): its two products are the respective matrix identities, so conjugation by its adjoint is the inverse. Iteration reduces \(k\) to its representative \(d\in\{1,\ldots,n-1\}\) modulo \(n-1\), preserving the gcd. The case \(d=1\) is immediate. Suppose henceforth \(2\leq d<n\), and write

\[
\begin{gathered}
n=qd+r,\quad 2\leq r\leq d,\quad q\geq1,\\
h=d-r+1,\qquad \gcd(h,d)=1.
\end{gathered}
\tag{5.4}
\]

We use remainder \(d\) rather than 0 when \(d\mid n\). A remainder 1 would contradict the gcd hypothesis for \(d\geq2\). Put \(x_i=s_i^*\), \(y_i=s_i\); thus \(x_i y_j=\delta_{ij}1\) and \(\sum_i y_i x_i=1\). Let \(e_{ab}\) be the scalar matrix units of \(M_d(\mathcal O_n)\), \(e_a=e_{aa}\), and \(P_a=\sum_{j=1}^a e_j\).

We will construct coisometries \(X_1,\ldots,X_n\) with

\[
\begin{gathered}
X_iX_j^*=\delta_{ij}I_d,\\
\sum_iX_i^*X_i=I_d.
\end{gathered}
\tag{5.5}
\]

For \(1\leq i\leq q\), and for the next two matrices, specify

\[
\begin{aligned}
X_i&=\sum_{j=1}^d x_{(i-1)d+j}e_{j1},\\
R&:=X_{q+1}\\
&=\sum_{j=1}^r x_{qd+j}e_{j1}\\
&\qquad+\sum_{j=1}^{d-r}e_{r+j,j+1},\\
T&:=X_{q+2}\\
&=\sum_{j=1}^{r-2}e_{j,j+h}\\
&\qquad+\sum_{j=r-1}^d a_{q+2,j}e_{jd}.
\end{aligned}
\tag{5.6}
\]

For \(q+3\leq i\leq n\), put \(X_i=\sum_{j=1}^d a_{ij}e_{jd}\). Empty sums are zero. The entries \(a_{ij}\) fill the last-column positions in \(T\) and these remaining matrices. We take them, each exactly once, from the finite collection

\[
\begin{gathered}
\mathcal L=\{x_1^{d-1}\}\\
\quad\cup\{x_jx_1^l:\substack{2\leq j\leq n,\\0\leq l\leq d-2}\}.
\end{gathered}
\tag{5.7}
\]

The adjoints of these elements are the Cuntz family obtained by repeatedly expanding the first member of \((s_1,\ldots,s_n)\), until that branch has length \(d-1\). Explicitly the words are \(s_1^{d-1}\) and \(s_1^l s_j\). Distinct words differ at the first non-1 letter, or one is the terminal all-1 word; cancellation proves their orthogonality. Repeated insertion of \(\sum_j s_js_j^*=1\) proves that their range projections sum to 1. Thus, for \(a,b\in\mathcal L\),

\[
ab^*=\delta_{ab}1,
\qquad \sum_{a\in\mathcal L}a^*a=1.
\tag{5.8}
\]

There are \((n-1)(d-1)+1\) such entries. The number of empty positions is
\((d-r+2)+d(n-q-2)=(n-1)(d-1)+1\).
We must place the entries with one additional condition, needed for surjectivity.

Consider the permutation of \(\{1,\ldots,d\}\) given by addition of \(h\) modulo \(d\), always using representatives in that set. Its orbit beginning at 1 lists every index once, because \(\gcd(h,d)=1\); its last index is \(r\), since \(1-h\equiv r\pmod d\). Split this list immediately after \(r-1\) into sets \(I_1,I_2\). Then \(1,r-1\in I_1\), and the first index of \(I_2\) is \(d\), while its last is \(r\). Along either part, an index \(w<r-1\) goes to \(w+h\), and an index \(w>r\) goes to \(w-r+1\). Extend these two colors to generator indices by coloring \(j\) according to the representative \(\widehat j\in\{1,\ldots,d\}\) of \(j\pmod d\).

Place \(x_jx_1^l\) only in rows with the color of \(\widehat j\), and place \(x_1^{d-1}\) in a row of \(I_1\). Here is a proof that enough positions of each color exist. Write

\[
\begin{gathered}
a=|I_1|,\\
f=|I_1\cap\{1,\ldots,r\}|,\\
e=|I_1\cap\{r-1,\ldots,d\}|,\\
e+f=a+1.
\end{gathered}
\tag{5.9}
\]

The path from 1 to \(r-1\) has \(f-1\) forward steps of size \(h\) and \(e-1\) backward steps of size \(r-1\). Its total displacement gives
\(r-2=(f-1)h-(e-1)(r-1)\).
Substitute \(e=a+1-f\) and \(h=d-r+1\) to obtain
\(a(r-1)=df-d+1\).
The last-column positions of color 1 number \(a(n-q-2)+e\). The entries of \(\mathcal L\) of color 1 number \((d-1)(qa+f-1)+1\): among generator indices 1 through \(n\), there are \(qa+f\) of that color; exclude 1 from each of the \(d-1\) rows of monomials, then add the special all-1 entry. The two counts are equal, since

\[
\begin{aligned}
&a(n-q-2)+e\\
&\quad=aq(d-1)+a(r-1)\\
&\qquad-a+e\\
&\quad=aq(d-1)+df-d\\
&\qquad+1-a+e\\
&\quad=(d-1)(qa+f-1)+1.
\end{aligned}
\tag{5.10}
\]

Their total counts also agree, so color 2 has exactly enough positions. Arbitrary bijections within the two colors give the required placement.

We now verify (5.5). In \(X_1,\ldots,X_q,R\), the first-column entries are all the original \(x_j\), each once. Their products with adjoint first-column entries are Kronecker deltas. The other entries of \(R\) are scalar 1 on distinct rows and columns; they fill its remaining diagonal products. Their occupied columns are 2 through \(h\). The scalar entries of \(T\) occupy columns \(h+1\) through \(d-1\), and all the new entries occupy column \(d\). These column sets are disjoint from those of the earlier matrices. Within the new last-column entries, (5.8) gives precisely the needed Kronecker products. Thus each \(X_iX_i^*=I_d\), and \(X_iX_j^*=0\) for \(i\ne j\). For the other product sum, the original first column contributes \(\sum_j y_jx_j=1\) at coordinate 1; the scalar shifts contribute 1 at coordinates 2 through \(d-1\); and (5.8) contributes 1 at coordinate \(d\). This proves (5.5), and also

\[
\sum_{i=1}^{q+1}X_i^*X_i=P_h.
\tag{5.11}
\]

It remains to prove that the matrices generate all of \(M_d(\mathcal O_n)\). Let \(\mathcal C=C^*(X_1,\ldots,X_n)\), a unital algebra by (5.5). First every scalar diagonal projection belongs to \(\mathcal C\). To see this, list \(u_i=ih\pmod d\), \(1\leq i\leq d\). This is a permutation, with \(u_{d-1}=r-1\), \(u_d=d\). Start with \(P_{u_1}=P_h\) from (5.11). For \(i\leq d-2\), the index \(u_i\) is not \(r-1\), and the scalar shifts in (5.6) give

\[
\begin{aligned}
P_{u_i+h}&=P_h+T^*P_{u_i}T\\
&\qquad(u_i\leq r-2),\\
P_{u_i-r+1}&=P_h\\
&\quad-R^*(I_d-P_{u_i})R\\
&\qquad(u_i\geq r).
\end{aligned}
\tag{5.12}
\]

In the first identity only rows below \(r-1\) are used, so \(T\)'s unspecified entries contribute nothing. In the second identity only rows strictly above \(u_i\geq r\) are used, so \(R\)'s first-column entries contribute nothing. Induction therefore puts all \(P_j\) in \(\mathcal C\), the final one being \(I_d\). Differences give all \(e_j\). This also covers \(r=2\), when only the second recurrence is used, and \(r=d\), when only the first is used.

Now each scalar shift in (5.6) can be extracted by its two diagonal projections. We obtain \(e_{w,w+h}\) for \(w<r-1\), and \(e_{w,w-r+1}\) for \(w>r\). These are exactly the consecutive edges within the two parts of the orbit list defining \(I_1,I_2\). Products along a path, and adjoints along its reverse, give every \(e_{ab}\) with \(a,b\) in the same part. A part with just one index already has its diagonal projection.

The color condition supplies the missing bridge between the two parts. Extracting the entry \(x_1^{d-1}\), and moving its row within \(I_1\), gives \(x_1^{d-1}e_{1d}\in\mathcal C\). The first-column matrices also give
\(x_je_{\widehat j,1}\) and \(y_je_{1,\widehat j}\) for every \(j\). Suppose \(x_1^{l+1}e_{1d}\in\mathcal C\), where \(0\leq l\leq d-2\). Multiplication by \(y_1e_{11}\) gives \(y_1x_1x_1^l e_{1d}\). For \(j\geq2\), the entry \(x_jx_1^l\) appears in a row of the same color as \(\widehat j\); the matrix units already obtained in that part move it to row \(\widehat j\). Multiplication by \(y_je_{1,\widehat j}\) gives \(y_jx_jx_1^le_{1d}\). Summing over every \(1\leq j\leq n\) yields

\[
\sum_{j=1}^n y_jx_jx_1^le_{1d}
=x_1^le_{1d}\in\mathcal C.
\tag{5.13}
\]

Descending from \(l=d-2\) to 0 proves \(e_{1d}\in\mathcal C\). Its adjoint is also present. Combining this bridge with the two sets of matrix units gives every scalar \(e_{ab}\). The original first-column entries now give \(x_je_{ab}\) for every \(j,a,b\), by multiplication on the left and right by those matrix units; adjoints give \(y_je_{ab}\). Hence \(\mathcal C=M_d(\mathcal O_n)\).

Finally \(S_i=X_i^*\) satisfy the Cuntz relations by (5.5). Universality gives a unital map from \(\mathcal O_n\) onto their generated algebra, now proved to be \(M_d(\mathcal O_n)\). Theorem 2.2 makes it injective. The initial rectangular unitaries transfer this isomorphism to the original size \(k\). This proves sufficiency for every \(k\), including \(n=2\). \(\square\)

### Projection representatives and scale

**Proposition 5.2.** If a unital C*-algebra \(A\) contains two isometries with orthogonal ranges, every class of \(K_0(A)\) is represented by a projection in \(A\) itself. In particular \(K_0(A)^+=K_0(A)\), and the scale \(\{[p]:p\text{ a projection in }A\}\) is all of \(K_0(A)\).

*Proof.* From two orthogonal isometries we can form arbitrarily large finite orthogonal families by repeatedly replacing one member \(v\) by the two isometries obtained by appending the original pair. Their total range is at most 1. For a projection \(p\in M_l(A)\), choose such a family of size \(l\), and let \(V\) be its row. Then \(V^*V=I_l\), while \(VV^*\leq1\); the projection \(p'=VpV^*\in A\) is Murray–von Neumann equivalent to \(p\), implemented by the rectangular partial isometry \(Vp\).

Write any group class as \([p]-[q]\), and replace both matrix projections by projections \(p',q'\in A\) as just described. Let \(v_1,v_2\) be two orthogonal isometries. The element

\[
r=1-v_1v_1^*-v_2q'v_2^*
\tag{5.14}
\]

is a projection, since the two subtracted projections are orthogonal and their sum is at most 1. Additivity and equivalence give \([r]=[1]-[1]-[q']=-[q]\). Therefore

\[
p''=v_1p'v_1^*+v_2rv_2^*
\tag{5.15}
\]

is a projection in \(A\) with \([p'']=[p]-[q]\). This proves both assertions, without a cancellation assumption. Applied to \(\mathcal O_n\), use \(s_1,s_2\). A zero K-class still need not be a zero projection. \(\square\)

## 6. The Toeplitz model and \(\mathcal O_\infty\)

Let \(E_n\) be universal for \(n\) orthogonal isometries \(S_i\), with no relation requiring their ranges to exhaust the identity. Put

\[
q=1-\sum_{i=1}^nS_iS_i^*.
\tag{6.1}
\]

The left creation operators on finite words over \(n\) letters give its Fock representation; \(q\) is the projection onto the empty word. We first justify that this concrete model is faithful, so that the extension and the later embeddings are genuine algebra statements.

**Lemma 6.1.** A unital, gauge-equivariant representation of \(E_n\) with nonzero image of \(q\) is injective.

*Proof.* The fixed core is the closure of the increasing finite-dimensional algebras generated by equal-length normal words of length at most \(l\). Their matrix blocks are

\[
\begin{gathered}
S_\mu q S_\nu^*,\quad |\mu|=|\nu|=r<l,\\
S_\mu S_\nu^*,\quad |\mu|=|\nu|=l.
\end{gathered}
\tag{6.2}
\]

The first blocks at distinct lengths annihilate one another: after cancellation, \(qS_i=0=S_i^*q\). They also annihilate the last block. Their diagonal sums, together with the last block's diagonal sum, equal one by iterating (6.1). Inserting \(1=q+\sum_iS_iS_i^*\) repeatedly expresses every shorter normal word as a sum in these blocks. The algebra is therefore

\[
\left(\bigoplus_{r=0}^{l-1}M_{n^r}(\mathbb C)\right)
\oplus M_{n^l}(\mathbb C).
\tag{6.3}
\]

Each defect diagonal is equivalent to \(q\), and each terminal diagonal to one. All are nonzero in the universal algebra by the Fock model. A representation with nonzero defect keeps all these blocks nonzero, hence is injective on each block and their orthogonal sum. It is isometric on the entire fixed core. Both algebras admit gauge averaging, and equivariance intertwines it. If \(a\) maps to zero, its positive average \(E(a^*a)\) maps to zero and hence vanishes in the fixed core. Faithfulness of the universal average proves \(a=0\). \(\square\)

The Fock representation has a gauge action implemented by multiplying length-\(r\) basis vectors by \(z^r\), so the lemma applies. In this model the operators \(S_\mu qS_\nu^*\), with arbitrary finite words, are precisely the rank-one matrix units between word vectors. Their closed span is \(\mathcal K\), the ideal generated by \(q\). The quotient imposes exactly the missing Cuntz relation; the two universal maps on generators are inverse. Thus

\[
0\longrightarrow\mathcal K
\longrightarrow E_n
\longrightarrow\mathcal O_n
\longrightarrow0.
\tag{6.4}
\]

The scalar inclusion \(\mathbb C\to E_n\) induces isomorphisms on both K-groups. Proposition 6.2 below proves this from the Fock extension and the independently established finite Cuntz calculation; Theorem 6.3 also proves the full correspondence coefficient theorem. Thus

\[
\begin{gathered}
K_0(E_n)=\mathbb Z[1_{E_n}],\\
K_1(E_n)=0.
\end{gathered}
\tag{6.5}
\]

For the infinite algebra, let \(A_n=C^*(1,s_1,\ldots,s_n)\) inside \(\mathcal O_\infty\). Its defect is nonzero, since it dominates \(s_{n+1}s_{n+1}^*\). The natural map \(E_n\to A_n\) intertwines gauge actions, so Lemma 6.1 makes it an isomorphism. The union of the \(A_n\) is dense by the definition of the infinite universal algebra. Its unital connecting maps preserve the generators of (6.5), and hence induce the identity on \(\mathbb Z\). Continuity from Lesson 16 gives

\[
\begin{gathered}
K_0(\mathcal O_\infty)=\mathbb Z,
\qquad [1]=1,\\
K_1(\mathcal O_\infty)=0.
\end{gathered}
\tag{6.6}
\]

This uses a direct limit of Toeplitz algebras. It does not impose finite Cuntz sums inside \(\mathcal O_\infty\), or infer an infinite-algebra group from the finite extension alone.

**Proposition 6.2 (the scalar Toeplitz K-isomorphism).** The unital coefficient map \(\mathbb C\to E_n\) induces both K-isomorphisms; explicitly,

These are the groups and distinguished generator in (6.5).

*Proof.* Theorem 4.1 computed \(K_0(\mathcal O_n)=\mathbb Z/(n-1)\), with its unit the displayed generator, and \(K_1(\mathcal O_n)=0\), by the core, full corner, Takai duality and PV sequence. That computation used no Toeplitz K-isomorphism. Applying the six-term sequence to the already proved Fock extension (6.4), and using compact stability, therefore gives

\[
\begin{gathered}
K_1(E_n)=0,\\
\begin{aligned}
0\longrightarrow\mathbb Z[q]
&\xrightarrow{\ j_*\ }K_0(E_n)\\
&\xrightarrow{\ \pi_*\ }\mathbb Z/(n-1)\\
&\longrightarrow0.
\end{aligned}
\end{gathered}
\tag{6.7}
\]

The first arrow is injective because the preceding group \(K_1(\mathcal O_n)\) is zero. The vacuum rank-one projection \(q\) generates \(K_0(\mathcal K)\). Orthogonality and the isometries give the relation inside \(E_n\), before taking any quotient,

\[
j_*[q]=(1-n)[1_{E_n}].
\tag{6.8}
\]

Write \(g=[1_{E_n}]\). Since the quotient map is unital, \(\pi_*(g)\) generates \(\mathbb Z/(n-1)\). For any \(h\in K_0(E_n)\), choose an integer \(m\) with \(\pi_*(h)=\pi_*(mg)\). Exactness gives \(h-mg=l j_*[q]\) for some integer \(l\). Equation (6.8) shows that \(h\) is an integral multiple of \(g\). This reasoning includes \(n=2\), when the quotient is zero and one may take \(m=0\).

The element \(g\) has infinite order. If \(kg=0\), then (6.8) gives \(j_*(k[q])=(1-n)kg=0\); injectivity in (6.7) forces \(k=0\). Thus \(K_0(E_n)\) is the infinite cyclic group generated by the unit, proving the degree-zero assertion and its normalization. Both \(K_1(\mathbb C)\) and \(K_1(E_n)\) vanish, which proves the degree-one assertion. \(\square\)

### The general coefficient theorem

We now prove the full correspondence theorem behind the scalar calculation, following Pimsner's Fock rotation and Katsura's elementary K-theory version. The proof retains arbitrary coefficient algebras and Hilbert modules, including nonseparable ones and degenerate left actions.

A C*-correspondence over \(A\) is a right Hilbert \(A\)-module \(X\) with an adjointable left action \(\varphi:A\to\mathcal L(X)\). Its Toeplitz algebra \(\mathcal T_X\) is universal for a homomorphism \(\pi:A\to\mathcal T_X\) and a linear map \(t:X\to\mathcal T_X\) satisfying

\[
\begin{aligned}
t(\xi)^*t(\eta)&=\pi(\langle\xi,\eta\rangle),\\
\pi(a)t(\xi)&=t(\varphi(a)\xi),\\
t(\xi)\pi(a)&=t(\xi a).
\end{aligned}
\tag{6.9}
\]

The third identity follows from the first by expanding the positive square of their difference. The first also gives \(\|t(\xi)\|\leq\|\xi\|\). Universal existence follows by taking the supremum of representation norms on the algebra generated by these symbols; each polynomial is bounded by the coefficient norms and these bounds on \(t\). The Fock representation below shows that \(\pi\) is injective. The interior tensor products and direct sums of Hilbert modules used here are the constructions in the Hilbert C*-modules course; the displayed inner-product checks specify the maps we need.

**Theorem 6.3 (Toeplitz coefficient theorem).** For every C*-correspondence \(X\) over every C*-algebra \(A\),

\[
\begin{gathered}
\pi_*:K_i(A)\longrightarrow K_i(\mathcal T_X)\\
\text{is an isomorphism},\quad i=0,1.
\end{gathered}
\tag{6.10}
\]

*Proof.* We first construct an elementary difference map for two representations. If \(I\) is an ideal of a C*-algebra \(C\), let

\[
\begin{gathered}
\mathcal D(I,C)=\\
\{f\in C_0((-1,1),C):\\
f(s)-f(-s)\in I\\
\text{for every }s\}.
\end{gathered}
\tag{6.11}
\]

The positive-half inclusion \(j:SI\to\mathcal D(I,C)\) extends a function by zero on \((-1,0]\). Restriction to the negative half gives the exact sequence

\[
\begin{aligned}
0\longrightarrow SI&\xrightarrow{j}\mathcal D(I,C)\\
&\longrightarrow C_0((-1,0],C)\\
&\longrightarrow0.
\end{aligned}
\tag{6.12}
\]

Restriction is onto: reflect any negative-half function evenly to the positive half. The kernel is exactly \(SI\), by (6.11) and continuity at 0. The quotient is a cone and has zero K-groups. Explicitly, after its identification with \(C_0([0,1),C)\), the homotopy \(f(s)\mapsto f(v+(1-v)s)\), \(0\leq v\leq1\), contracts it, taking the value 0 at \(v=1\). Uniform vanishing at 1 makes the homotopy norm continuous. The six-term sequence therefore makes \(j_*\) an isomorphism in both degrees.

Given homomorphisms \(\rho_+,\rho_-:B\to C\) whose difference lies in \(I\), the formula

\[
\begin{gathered}
R(f)(s)\\
=\begin{cases}
\rho_+(f(s)),&s\geq0,\\
\rho_-(f(-s)),&s\leq0
\end{cases}
\end{gathered}
\tag{6.13}
\]

defines a homomorphism \(R:SB\to\mathcal D(I,C)\); \(f(0)=0\) checks the common endpoint. If \(\rho_+=\rho_-\), this map factors through the even cone \(C_0([0,1),C)\), so its K-map is zero. If \(\rho_+=\sigma+\rho_-\), where \(\sigma:B\to I\) and the two summands have orthogonal ranges, additivity gives \(R_*=(jS\sigma)_*\). Here additivity is the ordinary block-sum rule: orthogonal projection images add in \(K_0\); for normalized unitaries the two orthogonal nonconstant parts multiply, and a scalar two-by-two rotation identifies their product with their stabilized block sum. This also applies to relative classes in forced unitizations. These difference maps are natural under homomorphisms of \((I,C)\) and invariant under point-norm homotopies of the two representations. All these assertions follow directly from (6.11)–(6.13) and K-theory homotopy invariance.

Assume first that the left action on \(X\) is nondegenerate, meaning \(\overline{\varphi(A)X}=X\). Put

\[
\mathcal F=\bigoplus_{m\geq0}X^{\otimes m},
\qquad X^{\otimes0}=A.
\tag{6.14}
\]

The tensor products are over \(A\). On grade zero let \(\varphi_0(a)\) be left multiplication by \(a\); on higher grades let \(\varphi_m(a)\) act on the first tensor factor. Write \(\varphi_\infty(a)=\bigoplus_m\varphi_m(a)\). Creation by \(\xi\) sends \(a\in A\) to \(\xi a\), and \(\eta\in X^{\otimes m}\), \(m\geq1\), to \(\xi\otimes\eta\). Its adjoint on an elementary tensor is
\(\xi'\otimes\eta\mapsto\varphi_m(\langle\xi,\xi'\rangle)\eta\), with left multiplication on grade zero. The tensor inner product gives
\(T(\xi)^*T(\eta)=\varphi_\infty(\langle\xi,\eta\rangle)\), and the left-action identity in (6.9) holds grade by grade. Thus this is a Toeplitz representation, inducing \(\rho_+:\mathcal T_X\to\mathcal L(\mathcal F)\). Its coefficient map is faithful on the vacuum copy of \(A\), proving injectivity of \(\pi\).

There is a second representation \(\rho_-\), zero on the vacuum and equal to the coefficient and creation operators on the positive grades. In particular creation from grade zero is now zero. The same calculation checks (6.9): both its coefficient and creation inner-product operators are zero on grade zero and have the preceding formulas on the other grades. For generators the differences are

\[
\begin{aligned}
\rho_+(\pi(a))-\rho_-(\pi(a))&=\varphi_0(a),\\
\rho_+(t(\xi))-\rho_-(t(\xi))&=T_0(\xi),
\end{aligned}
\tag{6.15}
\]

where the first operator is supported on the vacuum and the second maps the vacuum to grade one. Both are compact Hilbert-module operators. For the second assertion, if \((e_\lambda)\) is an approximate identity of \(A\), the rank-one maps \(\theta_{\xi,e_\lambda}:A\to X\) converge to \(a\mapsto\xi a\), since \(\|\xi-\xi e_\lambda\|\to0\). Also \(\mathcal K(A)=A\) by \(\theta_{a,b}(c)=ab^*c\). The compact operators are an ideal in \(\mathcal L(\mathcal F)\), so the difference of the two representations is compact on every element: for products expand it as a sum with one difference factor, and then use polynomial density.

Write
\(D_{\mathcal F}=\mathcal D(\mathcal K(\mathcal F),\mathcal L(\mathcal F))\).
The pair \((\rho_+,\rho_-)\) gives \(R:S\mathcal T_X\to D_{\mathcal F}\) by (6.13). Let \(k_A:SA\to D_{\mathcal F}\) be the positive-half vacuum inclusion \(jS\varphi_0\). This induces an isomorphism. Indeed the vacuum projection is a full multiplier projection of \(\mathcal K(\mathcal F)\), and its corner is \(A\). For fullness, every rank-one \(\theta_{\xi,\eta}\) is a norm limit of vacuum factorizations: creation maps \(A\to\mathcal F\), \(a\mapsto\xi a\), are compact by the same approximate-identity argument, and inserting vacuum multiplication by \(e_\lambda\) gives \(\theta_{\xi e_\lambda,\eta}\to\theta_{\xi,\eta}\). Thus the ideal generated by the vacuum corner contains all compacts. The [arbitrary full-multiplier-corner theorem, Hilbert C*-modules Lesson 14, Theorem 2.4](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-CP/prerequisites/hilbert-c-star-modules-and-morita-equivalence/morita-invariance-of-k-theory-and-correspondence-maps.html#2-full-multiplier-corners) makes \((\varphi_0)_*\) an isomorphism, without countability assumptions; (6.12) then proves the assertion about \(k_A\).

On coefficient elements, the pair in (6.15) is the orthogonal sum of the vacuum representation and its common positive-grade representation. The even-cone cancellation after (6.13) consequently gives

\[
R_*(S\pi)_*=(k_A)_*.
\tag{6.16}
\]

Thus \(L=(k_A)_*^{-1}R_*\) is a left inverse to \((S\pi)_*\). We prove that it is also a right inverse, keeping the actual coefficient map throughout.

Let \(T=\mathcal T_X\), and extend scalars to form the Hilbert \(T\)-module
\(Y=\mathcal F\otimes_\pi T=\bigoplus_{m\geq0}Y_m\).
Here \(Y_m=X^{\otimes m}\otimes_\pi T\) is identified isometrically with \(\overline{t^m(X^{\otimes m})T}\) by \(\xi\otimes b\mapsto t^m(\xi)b\): its inner products agree by (6.9), and the indicated span gives surjectivity. These are separate summands of \(Y\), even when their images as subspaces of \(T\) overlap. Nondegeneracy gives \(Y_0=T\). For clarity, an approximate identity of \(A\) acts on both sides of each generator of \(T\): on the left use \(\varphi(e_\lambda)\xi\to\xi\), and on the right use \(\xi e_\lambda\to\xi\). Polynomial approximation therefore makes \(\pi(e_\lambda)\) an approximate identity of \(T\), proving the vacuum identification.

Every adjointable operator \(Q\) on \(\mathcal F\) extends to \(\Phi(Q)=Q\otimes1\) on \(Y\), a homomorphism of adjointable-operator algebras. It sends compacts to compacts. Define \(J\xi\in Y\) on grade \(m\) by \(t^m(\xi_m)\); then
\(\langle J\xi,J\eta\rangle=\pi(\langle\xi,\eta\rangle)\), and \(JT\) spans \(Y\). On these dense vectors a direct check gives

\[
\Phi(\theta_{\xi,\eta})=\theta_{J\xi,J\eta}.
\tag{6.17}
\]

No identity in a nonunital coefficient algebra is used in defining \(J\). Thus \(\Phi\) induces a homomorphism \(D\Phi:D_{\mathcal F}\to D_Y\), where \(D_Y=\mathcal D(\mathcal K(Y),\mathcal L(Y))\). Vacuum multiplication defines \(\widetilde\varphi_0:T\to\mathcal K(Y)\); its corner is full by the same vacuum factorization. Hence the positive-half map \(k_T=jS\widetilde\varphi_0:ST\to D_Y\) induces an isomorphism. Vacuum extension of scalars gives the actual equality

\[
\begin{gathered}
\Phi\varphi_0(a)=\widetilde\varphi_0(\pi(a)),\\
D\Phi\,k_A=k_T S\pi.
\end{gathered}
\tag{6.18}
\]

Here is the rotation proving the other inverse identity. Let \(\Pi=\Phi\varphi_\infty\). For \(\xi\in X\), let \(A_\xi\) be multiplication by \(t(\xi)\) on \(Y_0=T\), zero elsewhere; let \(B_\xi=\Phi(T_0(\xi))\), taking \(Y_0\) to \(Y_1\); and let \(C_\xi\) be the positive-grade truncated creation operator \(\Phi(\rho_-(t(\xi)))\). For \(0\leq v\leq1\), put

\[
\begin{aligned}
t_v(\xi)&=v A_\xi+\sqrt{1-v^2}\,B_\xi\\
&\qquad+C_\xi.
\end{aligned}
\tag{6.19}
\]

We verify the representation identities rather than assuming that this sum is a representation. The first two operators have domain \(Y_0\) and ranges in the orthogonal summands \(Y_0,Y_1\); the third has domain in the positive grades and range in grades at least two. Hence every mixed product in \(t_v(\xi)^*t_v(\eta)\) is zero. The products \(A_\xi^*A_\eta\) and \(B_\xi^*B_\eta\) both equal vacuum multiplication by \(\pi(\langle\xi,\eta\rangle)\). The third product equals \(\Pi(\langle\xi,\eta\rangle)\) on the positive grades. Since \(v^2+(1-v^2)=1\), their sum is exactly \(\Pi(\langle\xi,\eta\rangle)\). On each of the three summands, the left-action equation follows from \(\pi(a)t(\xi)=t(\varphi(a)\xi)\) or the Fock left-action formula. Thus \((\Pi,t_v)\) satisfies (6.9), inducing a homomorphism \(\rho_v:T\to\mathcal L(Y)\).

These homomorphisms vary continuously in point-norm: the generators do by (6.19), finite polynomials do by multiplication, and uniform contractivity extends continuity to all of \(T\). Their difference from \(\Phi\rho_-\) is compact. On coefficient generators it is vacuum multiplication; on creation generators it is \(vA_\xi+\sqrt{1-v^2}B_\xi\), whose two operators are compact by (6.17) and \(\mathcal K(T)=T\) on the vacuum. The ideal and approximation argument after (6.15) proves the assertion for every element.

At \(v=0\) we have \(\rho_0=\Phi\rho_+\). At \(v=1\), coefficient and creation operators both split into the vacuum representation of \(T\) and the truncated representation on the other grades, so
\(\rho_1=\widetilde\varphi_0+\Phi\rho_-\), an orthogonal sum. Applying (6.13) to these pairs gives a homotopy from \(D\Phi\,R\) to the difference map of \((\widetilde\varphi_0+\Phi\rho_-,\Phi\rho_-)\). Its common summand cancels through the even cone. Therefore

\[
(D\Phi)_*R_*=(k_T)_*.
\tag{6.20}
\]

Equations (6.18) and (6.20) give
\((k_T)_*(S\pi)_*L=(D\Phi)_*R_*=(k_T)_*\).
Cancel the isomorphism \((k_T)_*\) to obtain \((S\pi)_*L=1\). Together with (6.16), this proves that \((S\pi)_*\) is an isomorphism. The natural suspension identifications of Lessons 8 and 10 transfer the result to \(\pi_*\) in both degrees.

Finally remove nondegeneracy without restricting the correspondence. Let \(A^\dagger\) be the forced unitization, even if \(A\) is unital. Regard the same \(X\) as a Hilbert \(A^\dagger\)-module, with its inner product still in \(A\), right action \(\xi(a+\lambda1)=\xi a+\lambda\xi\), and left action \(\varphi^\dagger(a+\lambda1)=\varphi(a)+\lambda I_X\). The unit acts identically, so this correspondence is nondegenerate. Its universal Toeplitz algebra is precisely \(T^\dagger\), the forced unitization of \(T=\mathcal T_X\). To check this assertion, \((\pi^\dagger,t)\) in \(T^\dagger\) satisfies (6.9) for the enlarged correspondence, giving one universal map. Conversely, the original generators give a map from \(T\) to the enlarged Toeplitz algebra, whose coefficient unit acts identically on all its generators; extend that map as a unital homomorphism to \(T^\dagger\). Both composites fix the coefficient elements, creation elements and adjoined unit, hence are identity. This is an algebra isomorphism, not a K-theory assumption.

The nondegenerate case makes \((\pi^\dagger)_*:K_i(A^\dagger)\to K_i(T^\dagger)\) an isomorphism. It commutes with the two augmentations onto \(\mathbb C\) and is identity on the adjoined scalar summands. Restricting to their split K-theory kernels, which are exactly \(K_i(A)\) and \(K_i(T)\), gives the claimed isomorphism for the original, possibly degenerate, correspondence. \(\square\)

For \(A=\mathbb C\), \(X=\mathbb C^n\), the standard orthonormal basis maps to \(n\) orthogonal isometries and the coefficient unit is the unit of the generated algebra. Conversely those isometries define (6.9) by linearity. The two universal maps on these generators are inverse, so \(\mathcal T_X=E_n\) with its actual scalar coefficient map. Theorem 6.3 therefore supplies a second proof of Proposition 6.2, and agrees with its vacuum projection and unit normalization. The first proof used only the finite Cuntz computation and the Fock extension; the general proof used full-corner K-theory and the rotation, so neither proof assumes the other.

### Coefficients in the infinite Cuntz algebra

The scalar computation (6.6) has a stronger coefficient form; compare [Cuntz 1981 II, §2.4]. Before passing to the infinite limit, we prove the tensor identification needed to apply Theorem 6.3. All tensor products without a subscript below are minimal.

**Proposition 6.4 (Toeplitz tensor coefficients).** For every C*-algebra \(A\) and \(n\geq1\), the coefficient inclusion induces isomorphisms

\[
\begin{gathered}
K_i(A)\xrightarrow{\ \cong\ }K_i(A\otimes E_n),\\
a\longmapsto a\otimes1,\qquad i=0,1.
\end{gathered}
\tag{6.21}
\]

*Proof.* Suppose first that \(A\) is unital. For the correspondence \(X=A^n\) with coordinatewise left multiplication, its standard basis gives orthogonal isometries \(t_1,\ldots,t_n\). They commute with \(\pi(A)\), since \(a e_j=e_j a\). Conversely, a commuting representation of \(A\) and \(E_n\) gives (6.9) by \(t((a_j))=\sum_j t_j\pi(a_j)\). These two constructions are inverse on all generators. Thus

\[
\mathcal T_{A^n}=A\otimes_{\max}E_n
\tag{6.22}
\]

with its actual coefficient map.

We verify that the maximum and minimum tensor norms coincide here, rather than assume nuclearity of the coefficient algebra. The gauge action on the second factor is norm continuous in both completions, and the canonical quotient between them is equivariant. Its fixed algebra is the closure of \(A\) tensored with the finite cores (6.3): averaging a dense polynomial in the isometries keeps just its equal-length normal words.

For a finite sum of matrix algebras \(F\), the norms on \(A\odot F\) coincide. To see this directly, a representation of a full system of matrix units decomposes its Hilbert space as \(\mathbb C^d\otimes H_0\) on each block. An operator commuting with those units is \(1_d\otimes T\). Thus every commuting representation has exactly a matrix norm over a representation of \(A\), bounded by the C*-matrix norm on \(M_d(A)\); a faithful representation attains that norm. Central block projections give the maximum of the finitely many block norms. Applied to (6.3), this proves injectivity of the quotient on each fixed finite core and then on their closure.

Compact gauge averaging is faithful in the maximum completion as well. Indeed, if \(x\geq0\) is nonzero, a positive functional with positive value on \(x\) remains positive on a neighborhood of identity along its norm-continuous orbit; its Haar integral is positive. If an element lies in the quotient kernel, its positive square has average in that kernel, so injectivity on the fixed algebra makes the average zero. Faithfulness then makes the element zero. Consequently (6.22) is also \(A\otimes E_n\). Theorem 6.3 now proves (6.21) for unital \(A\), without any countability assumption.

For arbitrary \(A\), use its forced unitization \(A^\dagger\) and the augmentation \(\varepsilon:A^\dagger\to\mathbb C\). Tensoring this particular split extension gives

\[
\begin{gathered}
0\longrightarrow A\otimes E_n\\
\longrightarrow A^\dagger\otimes E_n\\
\xrightarrow{\ \varepsilon\otimes1\ }E_n
\longrightarrow0.
\end{gathered}
\tag{6.23}
\]

Here exactness does not require a general tensor exactness theorem. The quotient has the homomorphic section \(b\mapsto1\otimes b\). Subtracting its composite with the quotient is a bounded map into the closure of \(A\odot E_n\): this follows on algebraic tensors by writing each coefficient as \(a+\lambda1\), and then by norm approximation. It is identity on the quotient kernel, proving the stated kernel. The minimum tensor inclusion of the ideal is faithful by spatial representations.

Apply the unital case to \(A^\dagger\) and to \(\mathbb C\). The two K-isomorphisms commute with the augmentations and their sections. The split exact K-sequences identify their kernels with \(K_i(A)\) and \(K_i(A\otimes E_n)\), respectively. Restriction of the isomorphism therefore proves (6.21). Every construction commutes with coefficient homomorphisms, so the result is natural. \(\square\)

**Theorem 6.5 (infinite Cuntz coefficients).** For every C*-algebra \(A\), inclusion \(a\mapsto a\otimes1\) induces natural isomorphisms

\[
\begin{gathered}
K_i(A)\cong K_i(A\otimes\mathcal O_\infty),\\
i=0,1.
\end{gathered}
\tag{6.24}
\]

*Proof.* The faithful copies \(A_n\cong E_n\) constructed before Proposition 6.2 form an increasing dense union in \(\mathcal O_\infty\). Spatial tensoring preserves these inclusions. The union of \(A\otimes A_n\) is dense in \(A\otimes\mathcal O_\infty\): approximate the finitely many second factors of an algebraic tensor sum in one common stage, using \(\|a\otimes b\|=\|a\|\|b\|\). Each stage has both K-groups naturally identified with \(K_i(A)\) by Proposition 6.4. The stage embeddings preserve \(a\otimes1\), so their induced maps, under these identifications, are the identity. Continuity of both K-functors from Lessons 5 and 6 now proves (6.24), with the specified map and its naturality. \(\square\)

If \(A\) is unital, (6.24) sends \([1_A]\) to \([1_A\otimes1]\). In particular \(\mathcal O_\infty\otimes\mathcal O_\infty\) has degree-zero group \(\mathbb Z\), with unit one, and zero degree-one group. This is a K-theory calculation with its distinguished unit; it is not an algebra classification conclusion. The finite formula (4.7) and (6.24) also explain their different coefficient behavior: tensoring with \(\mathcal O_2\) kills both groups, whereas tensoring with \(\mathcal O_\infty\) preserves them.

The scalar and untwisted computations have a finite twisted extension. We now prove Cuntz’s inverse-automorphism sequence, the nonunital reduction, a quotient homotopy identity, and the countably infinite coefficient theorem. The Toeplitz coefficient isomorphism is the already proved Theorem 6.3; its specified map determines the signs below.

### Twisted Cuntz products

Let \(A\subset B(H)\) be a faithfully represented C*-algebra and let \(U_1,\ldots,U_n\) be pairwise commuting unitaries normalizing \(A\). Put \(\alpha_i=\operatorname{Ad}U_i|_A\). These are commuting automorphisms. In the unital case take the representation unital: if necessary restrict to \(1_AH\), an invariant subspace because each \(U_i\) fixes the projection \(1_A\). This is Cuntz’s hypothesis; the implementers may lie outside \(A\), so the automorphisms need not be inner in \(A\).

For unital \(A\), define \(B_\alpha\) as the universal unital C*-algebra generated by a unital coefficient copy \(j(A)\) and a Cuntz family \(s_1,\ldots,s_n\) with

\[
\begin{gathered}
s_i^*s_k=\delta_{ik}1,\qquad\sum_i s_is_i^*=1,\\
s_i j(a)=j(\alpha_i(a))s_i.
\end{gathered}
\tag{6.25}
\]

Here \(n\ge1\); for \(n=1\), the Cuntz generator is a unitary and \(\mathcal O_1=C(\mathbb T)\). A faithful coefficient model is obtained inside \(B(H)\otimes\mathcal O_n\), with \(j(a)=a\otimes1\) and \(s_i=U_i\otimes S_i\). The tensor product is spatial. For nonunital \(A\), use the closed ideal generated by its coefficients in the corresponding universal algebra for the forced unitization. The proof below identifies both definitions with Cuntz’s concrete twisted product [Cuntz 1981 II, Theorem 1.5 and §§2.2–2.4].

One can equivalently start with commuting abstract automorphisms. A faithful representation \(\pi\) of \(A\) gives a commuting implementation on \(\ell^2(\mathbb Z^n)\otimes H_\pi\): at coordinate \(g\), represent \(a\) by \(\pi(\alpha_{-g}(a))\), and let \(U_i\) translate by the positive coordinate vector. Direct calculation gives \(U_i\rho(a)U_i^*=\rho(\alpha_i(a))\). Thus the operator implementation assumption is available without requiring the automorphisms to be inner in the coefficient algebra.

**Theorem 6.6 (finite twisted Cuntz coefficients).** Write \(G_i=K_i(A)\), with indices modulo two, and

\[
\begin{gathered}
\Theta_i:G_i\longrightarrow G_i,\\
\Theta_i=1-\sum_{r=1}^n(\alpha_r^{-1})_*.
\end{gathered}
\tag{6.26}
\]

There is a natural cyclic exact sequence with consecutive arrows

\[
\begin{gathered}
G_i\xrightarrow{\Theta_i}G_i\xrightarrow{j_*}K_i(B_\alpha),\\
K_i(B_\alpha)\xrightarrow{\partial_i}G_{i-1}
\xrightarrow{\Theta_{i-1}}G_{i-1}.
\end{gathered}
\tag{6.27}
\]

Consequently

\[
\begin{gathered}
0\to\operatorname{coker}\Theta_i
\xrightarrow{\overline{j_*}}K_i(B_\alpha),\\
K_i(B_\alpha)\xrightarrow{\partial_i}\ker\Theta_{i-1}\to0.
\end{gathered}
\tag{6.28}
\]

No splitting is asserted, and no nuclearity, separability or torsion hypothesis on \(A\) is used. The boundaries are the actual exponential and index boundaries of the extension constructed below, transported by its vacuum corner. They are not unspecified arrows selected just to make the group sequence exact.

For unital coefficients the distinguished class is

\[
[1_{B_\alpha}]=\overline{j_*}\bigl([1_A]+\Theta_0G_0\bigr).
\tag{6.29}
\]

Each automorphism fixes the coefficient unit, so \(\Theta_0[1_A]=(1-n)[1_A]\). Equivalently the Cuntz ranges give \((n-1)[1_{B_\alpha}]=0\). Its exact order is the order of \([1_A]\) in the displayed cokernel; it need not be \(n-1\). The unit lifts to the unit of the Toeplitz algebra, and hence its exponential boundary is zero.

#### The vacuum ideal and faithful core

Assume first that \(A\) is unital. Let \(T_\alpha\) be universal for a unital coefficient map \(\pi\) and orthogonal isometries \(t_i\), with the same covariance relation but without requiring the range sum to be one. Put

\[
q=1-\sum_i t_it_i^*,\qquad r_i=t_it_i^*.
\tag{6.30}
\]

Each \(r_i\), and hence \(q\), commutes with \(\pi(A)\): covariance also reads \(\pi(a)t_i=t_i\pi(\alpha_i^{-1}(a))\). The algebra exists and its coefficient and vacuum coefficient maps are faithful. For example, the operators \(U_i\otimes L_i\) on \(H\otimes\ell^2(W)\), where \(W\) is the set of finite words and \(L_i\) prepends \(i\), give a representation with vacuum projection \(1\otimes e_\varnothing\). Thus \(a\mapsto q\pi(a)\) is injective in the universal algebra.

For a word \(\mu\), write \(t_\mu\) for its product, with \(t_\varnothing=1\). Cancellation and the covariance relation give normal-word density:

\[
\begin{gathered}
T_\alpha=\overline{\operatorname{span}}
\{t_\mu\pi(a)t_\nu^*:\\
a\in A,\ \mu,\nu\in W\}.
\end{gathered}
\tag{6.31}
\]

The closed span

\[
\begin{gathered}
J=\overline{\operatorname{span}}
\{t_\mu q\pi(a)t_\nu^*:\\
a\in A,\ \mu,\nu\in W\}.
\end{gathered}
\tag{6.32}
\]

is exactly the ideal generated by \(q\). Indeed \(qt_i=t_i^*q=0\). Multiplication by a creation operator prepends a letter; its adjoint either removes that letter or gives zero. Multiplication by \(\pi(b)\) changes the coefficient by the appropriate inverse word automorphism. For example, with \(\alpha_\mu=\alpha_{\mu_1}\cdots\alpha_{\mu_l}\),

\[
\begin{aligned}
&\pi(b)t_\mu q\pi(a)t_\nu^*\\
&\quad=t_\mu q\pi(\alpha_\mu^{-1}(b)a)t_\nu^*.
\end{aligned}
\tag{6.33}
\]

These operations preserve the displayed span and its adjoints. It is therefore an ideal containing \(q\), and every one of its generators lies in the ideal generated by \(q\).

Word cancellation with the two vacuum factors gives

\[
\begin{aligned}
&(t_\mu q\pi(a)t_\nu^*)(t_\kappa q\pi(b)t_\lambda^*)\\
&\quad=\delta_{\nu\kappa}\,t_\mu q\pi(ab)t_\lambda^*.
\end{aligned}
\tag{6.34}
\]

The involution also agrees with coefficient matrix adjoint. On every finite word set these formulas define an injective map from a matrix algebra over \(A\): multiplication by \(q t_\mu^*\) on the left and by \(t_\nu q\) on the right recovers the faithful corner \(q\pi(a)\). Passing through the increasing finite matrix corners proves

\[
\begin{gathered}
J\cong\mathcal K(\ell^2(W))\otimes A,\\
e_{\mu\nu}\otimes a\longmapsto t_\mu q\pi(a)t_\nu^*.
\end{gathered}
\tag{6.35}
\]

In particular the vacuum corner map \(v:A\to J\), \(v(a)=q\pi(a)\), is the actual rank-one stability map under this isomorphism, so \(v_*\) is an isomorphism in both degrees. The quotient imposes exactly the missing relation \(q=0\). Its universal property gives

\[
0\longrightarrow J\xrightarrow{\iota}T_\alpha
\xrightarrow{Q}B_\alpha\longrightarrow0.
\tag{6.36}
\]

To identify these universal algebras with the source's concrete models, we also verify faithfulness. There is a gauge action multiplying each creation generator by \(z\) and fixing coefficients. Its average is faithful: a nonzero positive element has a positive functional whose value remains positive on a neighborhood of the identity along its norm-continuous orbit; its Haar integral is positive.

For the Toeplitz algebra, the fixed core up to length \(l\) is an orthogonal direct sum

\[
\left(\bigoplus_{r=0}^{l-1}M_{n^r}(A)\right)\oplus M_{n^l}(A).
\tag{6.37}
\]

The defect blocks are \(t_\mu q\pi(a)t_\nu^*\) at a common length \(r<l\); the final block is \(t_\mu\pi(a)t_\nu^*\) at length \(l\). Multiplication and orthogonality follow from cancellation and \(qt_i=t_i^*q=0\). Their units sum to one by iterating \(1=q+\sum_i r_i\). Expanding a shorter normal word inserts this identity and replaces its coefficients on each longer branch by \(\alpha_i^{-1}(a)\), so these blocks contain every fixed normal word of length at most \(l\). Both coefficient maps are faithful on each block, by compression. Consequently any gauge-equivariant representation faithful on \(\pi(A)\) and \(q\pi(A)\) is faithful on the entire fixed core and then, by faithful averaging, on \(T_\alpha\).

Apply this to the model in \(B(H)\otimes\mathcal O_{n+1}\) using the first \(n\) canonical isometries. Its defect is \(1\otimes S_{n+1}S_{n+1}^*\), so the vacuum coefficient corner is faithful. It is exactly the concrete Toeplitz algebra in the original paper.

In the Cuntz quotient there are only the length-\(l\) matrix blocks \(M_{n^l}(A)\). They expand to successive lengths by

\[
\begin{aligned}
&s_\mu j(a)s_\nu^*\\
&\quad=\sum_i s_{\mu i}j(\alpha_i^{-1}(a))s_{\nu i}^*.
\end{aligned}
\tag{6.38}
\]

The concrete model inside \(B(H)\otimes\mathcal O_n\) is faithful on coefficients and therefore on each such block. Equivariance and faithful averaging make the universal map to that model injective. This proves the identification and also independence from the particular faithful commuting implementation.

#### The actual coefficient K-isomorphism

Take the right Hilbert \(A\)-module \(X=A^n\) with its standard inner product and left action

\[
\begin{gathered}
\varphi(a):A^n\longrightarrow A^n,\\
(\varphi(a)b)_r=\alpha_r^{-1}(a)b_r.
\end{gathered}
\tag{6.39}
\]

Its standard basis vectors give \(t(e_i)^*t(e_k)=\delta_{ik}\pi(1)\), and

\[
\pi(a)t(e_i)=t(e_i)\pi(\alpha_i^{-1}(a)).
\tag{6.40}
\]

Conversely, the generators of \(T_\alpha\) define the correspondence representation by \(t((b_i))=\sum_i t_i\pi(b_i)\). The inner product and the left and right action identities follow directly from the orthogonal isometries and covariance. The two universal maps fix all generators, hence are inverses. Thus \(T_\alpha=\mathcal T_X\) with its actual coefficient map.

KT-OPK-22, Theorem 6.3, now gives

\[
\begin{gathered}
\pi_*:K_i(A)\xrightarrow{\cong}K_i(T_\alpha),\\
i=0,1.
\end{gathered}
\tag{6.41}
\]

The inverse automorphisms in the left action are forced by the specified covariance. Replacing them by \(\alpha_i\) would construct a different covariance convention and would not prove the stated map.

#### The inverse-automorphism map and its boundaries

We prove

\[
\pi_*^{-1}\iota_*v_*=1-\sum_i(\alpha_i^{-1})_*.
\tag{6.42}
\]

For a projection \(e\in M_p(A)\), use the diagonal copies of \(q,r_i,t_i\) in \(M_p(T_\alpha)\). Since these projections commute with \(\pi_p(e)\),

\[
\pi_p(e)=q\pi_p(e)+\sum_i r_i\pi_p(e)
\tag{6.43}
\]

is an orthogonal decomposition of projections. Each \(r_i\pi_p(e)=t_i\pi_p(\alpha_i^{-1}(e))t_i^*\) is Murray–von Neumann equivalent to \(\pi_p(\alpha_i^{-1}(e))\), through \(t_i\pi_p(\alpha_i^{-1}(e))\). Additivity therefore gives the required formula on \([e]\), and then on all differences of projections.

For a unitary \(u\in U_p(A)\), the vacuum corner map represents its image by

\[
w_0=q\pi_p(u)+(1-q)I_p.
\tag{6.44}
\]

Let \(w_i=r_i\pi_p(u)+(1-r_i)I_p\). These unitaries act on orthogonal corners, so \(\pi_p(u)=w_0w_1\cdots w_n\). Stable K-one multiplication is addition, by KT-OPK-06, Theorem 2.2. To identify each \([w_i]\), for any isometry \(t\) with range projection \(r\) observe that

\[
W=\begin{pmatrix}t&1-r\\0&t^*\end{pmatrix}
\tag{6.45}
\]

is a unitary and

\[
\begin{gathered}
W\operatorname{diag}(z,1)W^*\\
=\operatorname{diag}(tzt^*+1-r,1).
\end{gathered}
\tag{6.46}
\]

These identities are verified by multiplication, using \(t^*t=1\) and \((1-r)t=0\). Apply them at matrix size \(p\), with \(t=t_i\) and \(z=\pi_p(\alpha_i^{-1}(u))\). Conjugation does not change a stable K-one class, since that group is abelian. Thus \([w_i]=\pi_*[\alpha_i^{-1}(u)]\), and subtracting these classes from \([\pi_p(u)]\) yields the same inverse-automorphism formula in degree one. Identity padding is included throughout; no unstabilized component assertion is used.

Transport the six-term sequence of the displayed extension by \(\pi_*\) on the middle algebra and by \(v_*\) on its ideal. The quotient composite \(Q\pi=j\) supplies the actual coefficient arrow. Set

\[
\partial_0=v_{*,1}^{-1}\varepsilon_E,
\qquad\partial_1=v_{*,0}^{-1}\delta_E,
\tag{6.47}
\]

where \(\varepsilon_E\) is the positive exponential boundary and \(\delta_E\) the index boundary of KT-OPK-11. Exactness and naturality of that six-term sequence now prove every position of the theorem for unital coefficients.

There is a useful direct sign test at \(n=1\). The quotient generator \(s_1\) is a unitary lifted by the isometry \(t_1\). The index defect formula in the stated convention gives

\[
\begin{aligned}
\delta_E[s_1]&=[1-t_1^*t_1]\\
&\quad-[1-t_1t_1^*]=-[q],\\
\partial_1[s_1]&=-[1_A].
\end{aligned}
\tag{6.48}
\]

This tests the boundary with an actual lift rather than an abstract kernel computation.

#### Nonunital coefficients, torsion and scalar coordinates

Let \(A^\dagger\) be the forced unitization, even if \(A\) already has a unit, and extend every automorphism by fixing its new unit. In the unital twisted algebra \(B_{\alpha^\dagger}\), the closed span of normal words with their coefficient in \(A\) is an ideal. Covariance preserves it because the automorphisms preserve \(A\). Augmentation of coefficients gives a quotient onto \(\mathcal O_n\), and the canonical Cuntz generators give a homomorphic section. Its kernel is exactly that span: subtract the section composed with augmentation on every normal word, then use norm density and boundedness. Thus

\[
\begin{aligned}
0\longrightarrow B_\alpha(A)
&\longrightarrow B_{\alpha^\dagger}(A^\dagger)\\
&\longrightarrow\mathcal O_n\longrightarrow0
\end{aligned}
\tag{6.49}
\]

is split exact.

If \(A\) was already unital, \(p=j(1_A)\) in this enlarged algebra commutes with its isometries, because each extended automorphism fixes \(1_A\). The coefficient ideal has unit \(p\), and its generators \(p s_i\) satisfy the original unital definition relative to that unit. The universal maps fixing those generators identify this ideal with the previously defined unital \(B_\alpha\). Thus the forced-unitization construction is consistent with that definition.

The source's generators are precisely the coefficient multiples \(a s_i\). They generate all coefficients, since \((a s_i)^*(b s_i)=j(\alpha_i^{-1}(a^*b))\) and the linear span of \(a^*b\) is dense in \(A\). They then generate every coefficient normal word. Indeed \(s_i j(a)=j(\alpha_i(a))s_i\) gives the one-letter case. If \(\eta\) is a word and \((e_\lambda)\) is an approximate identity of \(A\), then

\[
\begin{aligned}
&(s_i j(e_\lambda))(s_\eta j(a))\\
&\quad=s_i s_\eta j(\alpha_\eta^{-1}(e_\lambda)a)\\
&\quad\longrightarrow s_{i\eta}j(a).
\end{aligned}
\tag{6.50}
\]

Induction gives every \(s_\mu j(a)\). Approximate a middle coefficient by finite sums \(bc\), and write \(s_\mu j(bc)s_\nu^*=(s_\mu j(b))(s_\nu j(c^*))^*\), to obtain every two-sided normal word. Thus the concrete algebra generated in source §2.2 equals the coefficient ideal just described.

The Toeplitz construction admits the same augmentation and section, with scalar quotient \(E_n\). Let \(T_\alpha(A)\) be its coefficient ideal and \(J(A)=\mathcal K(\ell^2(W))\otimes A\) its vacuum ideal. Under the proved word-matrix identification, scalar augmentation on the enlarged vacuum ideal is \(e_{\mu\nu}\otimes(a+\lambda1)\mapsto\lambda e_{\mu\nu}\), with the scalar vacuum matrix units as section. Its kernel is \(J(A)\): subtract the section composed with augmentation on finite word matrices and then pass to norm limits. The quotient map sends \(T_\alpha(A)\) onto \(B_\alpha(A)\), and its kernel there is the intersection with the enlarged vacuum ideal, namely \(J(A)\). We therefore have the actual extension

\[
\begin{aligned}
0\longrightarrow J(A)&\longrightarrow T_\alpha(A)\\
&\longrightarrow B_\alpha(A)\longrightarrow0.
\end{aligned}
\tag{6.51}
\]

The scalar augmentations and their sections commute with all arrows of the enlarged Toeplitz extension, so they are morphisms of extensions. Naturality of the proved six-term sequence and of \(\pi_*,v_*\) decomposes the unitalized cycle into its scalar cycle and the cycle on the kernels. The latter is exactly the claimed sequence for \(A\). In particular the coefficient and vacuum K-isomorphisms restrict to these kernels in both degrees. This proves the nonunital case without tensoring an arbitrary extension or identifying the enlarged twisted algebra with an ordinary unitization of the smaller one. The same argument gives naturality for every equivariant coefficient homomorphism by extending it to the forced unitizations and restricting to the coefficient ideals.

The scalar component of the transported first map is **\(1-n\)** on \(K_0(\mathbb C)=\mathbb Z\). Indeed every extended automorphism acts identically on that summand. A positive \(n-1\) display is another exact-sequence convention; to make it the actual transported ideal map, replace the vacuum K-group identification by its negative and simultaneously negate the boundary into that ideal group. This is a change of K-group coordinates. The printed scalar decomposition in original §2.2 uses \(n-1\); with the stated \(1-\sum\alpha_i^{-1}\) identification its literal algebraic scalar component is \(1-n\). This sign should not be copied silently.

If all automorphisms are identity, the map is \(1-n\). The kernel and cokernel agree with the untwisted groups in existing Theorem 4.2, which displays \(n-1\). Its boundary is constructed through the gauge crossed product and the PV sequence, whereas the boundary here is the vacuum-transported Toeplitz boundary. No equality, or equality up to sign, between those two previously constructed boundary maps is asserted here; an additional comparison of the two extensions would be needed. Equality of their resulting abstract kernels and cokernels alone does not establish that comparison.

In particular, for \(d=n-1\) and identity twists, this theorem gives the complete coefficient formula

\[
\begin{gathered}
0\to G_i/dG_i\to K_i(A\otimes\mathcal O_n),\\
K_i(A\otimes\mathcal O_n)\to G_{i-1}[d]\to0,\\
G[d]=\{g:dg=0\}.
\end{gathered}
\tag{6.52}
\]

For \(n\ge2\), if \(G_{i-1}\) has no nonzero element annihilated by \(d\), the coefficient arrow identifies the middle group with \(G_i/dG_i\). Cuntz’s tensor quotient formula in both degrees follows when both coefficient groups are torsion-free. Without that hypothesis the kernel term must be retained; no general Künneth splitting is supplied or assumed. At \(n=1\) the first map for identity twists is zero, so the same short exact sequence reads \(0\to G_i\to K_i(A\otimes C(\mathbb T))\to G_{i-1}\to0\).

For \(n=1\), the result has \(1-\alpha_*^{-1}\). A convention with \(1-\alpha_*\) is obtained by changing the ideal identification by \(-\alpha_*\); the transported boundary then changes by \(-\alpha_*^{-1}\). This explicitly reconciles the inverse map without changing the coefficient inclusion.

### The sum of inverse twists on the whole quotient

**Proposition 6.7 (the quotient inverse-sum identity).** For commuting automorphisms, each \(\alpha_i\) extends to an automorphism \(\widetilde\alpha_i\) of \(B_\alpha\), acting as \(\alpha_i\) on coefficients and fixing every \(s_j\). The covariance relations are preserved because the automorphisms commute. Define

\[
\psi(b)=\sum_i s_i\widetilde\alpha_i^{-1}(b)s_i^*.
\tag{6.53}
\]

The summands are homomorphisms with orthogonal ranges. On coefficients \(\psi(j(a))=j(a)\), and on generators \(\psi(s_j)=\sum_i s_i s_j s_i^*\).

Put

\[
F=\sum_{i,j}s_i s_j s_i^*s_j^*.
\tag{6.54}
\]

The length-two matrix-unit relations show that \(F\) is the unitary that interchanges the two letters, so \(F=F^*\) and \(F^2=1\). It commutes with coefficients: the word automorphism \(\alpha_i\alpha_j\) equals \(\alpha_j\alpha_i\). Also \(Fs_j=\sum_i s_i s_j s_i^*\). The path

\[
\begin{gathered}
F_t=\frac{1+F}{2}+e^{\pi it}\frac{1-F}{2},\\
0\le t\le1.
\end{gathered}
\tag{6.55}
\]

consists of unitaries commuting with coefficients. Sending \(s_j\) to \(F_ts_j\) and fixing coefficients therefore gives a point-norm homotopy of homomorphisms from identity to \(\psi\). The same supported-isometry computation used above gives

\[
\begin{gathered}
\psi_*=\sum_i(\widetilde\alpha_i^{-1})_*=1\\
\text{on }K_*(B_\alpha).
\end{gathered}
\tag{6.56}
\]

This proves the source's identity on the whole quotient K-group, not merely on the coefficient image. For nonunital coefficients, apply the construction in the forced-unitization twisted algebra. Its homotopy and automorphisms preserve the coefficient ideal, and restrict to it, proving the same conclusion.

### Countably many twisted generators

**Theorem 6.8 (twisted infinite coefficients).** Suppose there is a countable commuting family of implemented automorphisms. For unital \(A\), define \(B_{\alpha,\infty}\) by a unital coefficient copy and countably many orthogonal isometries satisfying \(s_i j(a)=j(\alpha_i(a))s_i\), with no infinite norm-sum relation. For nonunital \(A\), take the coefficient ideal in this construction for \(A^\dagger\). In the unital case, the algebra generated by \(A\) and the first \(m\) isometries is a faithful copy of the finite Toeplitz algebra for \(\alpha_1,\ldots,\alpha_m\). To prove faithfulness, use the coefficient Toeplitz-core argument above in the concrete model \(s_i=U_i\otimes S_i\): its defect is \(1\otimes(1-\sum_{i\le m}S_iS_i^*)\), which is nonzero and has faithful coefficient corner, because it dominates the next range projection. The gauge action is retained. The universal model has the same faithful finite-stage cores, so it identifies with this concrete model as well.

These finite Toeplitz algebras form an increasing dense union. Their coefficient K-maps are isomorphisms by Theorem 6.3; the connecting maps preserve the actual coefficient map and hence act as identity under these identifications. Continuity of both K-functors therefore gives

\[
\begin{gathered}
j_*:K_i(A)\xrightarrow{\cong}K_i(B_{\alpha,\infty}),\\
i=0,1.
\end{gathered}
\tag{6.57}
\]

For nonunital coefficients, the split augmentation onto \(\mathcal O_\infty\) and its section reduce the assertion to the kernels exactly as above. This independently proves the twisted version of source §2.4; the existing Lesson 22 result covers its untwisted tensor special case.

For unital \(A\) the infinite coefficient isomorphism sends \([1_A]\) to \([1_{B_{\alpha,\infty}}]\). No algebra classification or additional simplicity conclusion is inferred from this K-theory isomorphism.

### Simplicity and pure infiniteness of infinite Cuntz coefficients

All tensor products in the proof are minimal. An infinite projection is a nonzero projection equivalent to a proper subprojection of itself. A properly infinite projection admits two orthogonal subprojections each equivalent to itself. The hereditary subalgebra generated by a positive element \(h\) is \(\operatorname{Her}(h)=\overline{hCh}=\overline{h^{1/2}Ch^{1/2}}\).

**Lemma 6.9a (an exact positive cutoff).** In any C*-algebra, if \(a,b\geq0\) and \(\varepsilon>\|a-b\|\), there is a contraction \(d\) in the algebra with

\[
d^*bd=(a-\varepsilon)_+.
\tag{6.S1}
\]

*Proof.* We give the norm-convergence details of the elementary cutoff argument [Kirchberg–Rørdam 2002, Lemma 2.2]. Write \(c=(a-\varepsilon)_+\). For \(r>1\), the function \(q_r(t)=\min(t,t^r)\) converges uniformly to \(t\) on the compact interval containing the spectrum of \(b\), as \(r\downarrow1\). Choose \(r>1\) with \(\delta=\|a-q_r(b)\|<\varepsilon\), and put \(b_0=q_r(b)\). Thus \(b_0\leq b,b^r\) and \(a-\delta1\leq b_0\).

Choose a continuous function \(e(t)\) which is zero for \(t\leq\delta\), takes values in \([0,1]\), and is one for \(t\geq\varepsilon\). Then \(e(a)c=c\) and scalar functional calculus gives

\[
\begin{gathered}
c\leq e(a)(a-\delta1)e(a)\\
\leq e(a)b_0e(a).
\end{gathered}
\tag{6.S2}
\]

Put \(x=b_0^{1/2}e(a)\), and use its polar decomposition \(x=v|x|\) in the bidual. The element \(y=vc^{1/2}\) belongs to the original algebra. Indeed \(x(|x|^2+t)^{-1/2}c^{1/2}\to vc^{1/2}\) in norm: its squared error is bounded by

\[
\sup_{s\geq0}s\left(1-\sqrt{s/(s+t)}\right)^2\leq t,
\tag{6.S3}
\]

using \(c\leq|x|^2\). Hence \(y^*y=c\) and \(yy^*\leq xx^*\leq b_0\leq b,b^r\).

For \(t>0\) set \(z_t=y^*(b^r+t)^{-1/2}b^{(r-1)/2}\), an element of the original algebra. The family \(z_t\), as \(t\downarrow0\), is norm Cauchy. Its squared difference is at most

\[
\begin{gathered}
\sup_{s\in\operatorname{sp}(b)}s^{r-1}|F_t(s)-F_u(s)|^2,\\
F_t(s)=s^{r/2}(s^r+t)^{-1/2}.
\end{gathered}
\tag{6.S4}
\]

To verify convergence, split the supremum at \(s=\alpha>0\). On \(s\leq\alpha\), the bound is at most \(\alpha^{r-1}\); on \(s\geq\alpha\), the displayed functions converge uniformly. First let \(t,u\downarrow0\), and then \(\alpha\downarrow0\). The strict inequality \(r>1\) is used here.

Also \(z_tb^{1/2}=y^*(b^r+t)^{-1/2}b^{r/2}\to y^*\) in norm, by \(yy^*\leq b^r\) and the scalar bound \(\sup_{s\geq0}s^r(1-\sqrt{s^r/(s^r+t)})^2\leq t\). Finally

\[
\begin{gathered}
z_t^*z_t\leq b^r(b^r+t)^{-1}\\
\leq1.
\end{gathered}
\tag{6.S5}
\]

Let \(z=\lim_{t\downarrow0}z_t\). It is a contraction and \(zbz^*=y^*y=c\). Taking \(d=z^*\) proves the assertion. \(\square\)

**Lemma 6.9b (finite positive fullness).** If a positive element \(a\) generates a C*-algebra \(C\) as a closed two-sided ideal, every element of \(C_+\) is a norm limit of finite sums \(\sum_j x_j^*ax_j\), with \(x_j\in C\).

*Proof.* The span of \(CaC\) is dense in \(C\); approximate a given \(b^{1/2}\) by \(y=\sum_{j=1}^m r_jas_j\). Put \(R=[r_1,\ldots,r_m]\), \(S=[s_1,\ldots,s_m]^T\), and \(D=\operatorname{diag}(a,\ldots,a)\). Then

\[
\begin{gathered}
y^*y=S^*DR^*RDS\\
\leq\|R\|^2S^*D^2S\\
\leq\|R\|^2\|a\|\sum_j s_j^*as_j=:c.
\end{gathered}
\tag{6.S6}
\]

Thus \(c\) is such a finite sum (absorb its scalar factor into the \(s_j\)). Write \(b'=y^*y\leq c\). For \(t>0\), \(w_t=(c+t1)^{-1/2}(b')^{1/2}\in C\), and

\[
\begin{gathered}
\|b^{\prime}-w_t^*cw_t\|\\
=t\|(c+t1)^{-1/2}(b^{\prime})^{1/2}\|^2\\
\leq t.
\end{gathered}
\tag{6.S7}
\]

The bound follows by swapping the two factors in this positive product and using \(b'\leq c\). Each \(w_t^*cw_t\) is again a finite sum of the required form. Let the approximation to \(b^{1/2}\) improve and then let \(t\downarrow0\). \(\square\)

**Lemma 6.9c (compression with an unused letter).** Let \(W\) be all finite words on the countable alphabet, including the empty word, and let \(L_i\delta_w=\delta_{iw}\) be the Fock representation of \(\mathcal O_\infty\). This representation is faithful. For its vector state \(\omega_w\) and any finite normal-word polynomial \(p\) with coefficients in a C*-algebra \(A\), choose a letter \(N\) absent from \(w\) and all its normal words. With \(t=s_ws_N\),

\[
\begin{gathered}
(1\otimes t)^*p(1\otimes t)\\
=\bigl((\operatorname{id}_A\otimes\omega_w)(p)\bigr)\otimes1.
\end{gathered}
\tag{6.S8}
\]

*Proof.* The restriction of the Fock representation to the first \(n\) generators is gauge equivariant and has nonzero defect, since that defect fixes the empty word. Lemma 6.1 makes it faithful on their copy of \(E_n\). The increasing union of those copies is dense in \(\mathcal O_\infty\), so the whole representation is faithful.

It suffices to compress \(s_\mu s_\nu^*\). If either \(\mu\) or \(\nu\) is not a prefix of \(wN\), the compressed product is zero. Because \(N\) occurs in neither normal word, being such a prefix is equivalent to being a prefix of \(w\). When both are prefixes, cancellation leaves the two tails of \(wN\). If their lengths differ, the unique final occurrence of \(N\) is at different positions, and the tails fail the prefix test. The product is again zero. If the lengths agree, the prefixes are equal and the product is one. These are exactly the diagonal matrix coefficients of \(L_\mu L_\nu^*\) at \(\delta_w\). Linearity proves the formula, including empty words. \(\square\)

**Theorem 6.9 (simplicity and pure infiniteness).** Let \(A\neq0\) be a simple C*-algebra. Then

\[
C=A\otimes_{\min}\mathcal O_\infty
\tag{6.S9}
\]

is simple, and every nonzero hereditary C*-subalgebra of \(C\) contains a properly infinite projection. No unitality, separability or nuclearity assumption on \(A\) is needed. More precisely, for every \(0\neq h\in C_+\), every \(b\in C_+\) and every \(\varepsilon>0\), there exists \(x\in C\) with

\[
\|x^*hx-b\|<\varepsilon.
\tag{6.S10}
\]

*Proof.* Represent \(A\) faithfully and nondegenerately, and represent \(\mathcal O_\infty\) by the faithful Fock representation of Lemma 6.9c. Their spatial tensor representation is faithful. For \(h\neq0\) positive, some slice \(a=(\operatorname{id}_A\otimes\omega_w)(h)\in A_+\) is nonzero. Otherwise every diagonal compression to \(H_A\otimes\delta_w\) vanishes; positivity makes \(h^{1/2}\) vanish on each such subspace and hence on their dense span, a contradiction.

The element \(c=a\otimes1\) is full in \(C\): the ideal it generates contains every \(ras\otimes d=(r\otimes d)c(s\otimes1)\), and \(\overline{AaA}=A\) by simplicity. Apply Lemma 6.9b to approximate the given \(b\) by a finite sum \(\sum_{i=1}^m y_i^*cy_i\). The multiplier isometries \(T_i=1\otimes s_i\) commute with \(c\) and satisfy \(T_i^*T_j=\delta_{ij}1\). Thus \(y=\sum_i T_i y_i\in C\) satisfies

\[
y^*cy=\sum_i y_i^*cy_i.
\tag{6.S11}
\]

Keep this \(y\) fixed. Approximate \(h\) by a finite normal-word polynomial \(p\), and use the unused-letter isometry \(v=1\otimes s_ws_N\in M(C)\) from Lemma 6.9c. Contractivity of compression and of the slice map gives

\[
\|v^*hv-c\|\leq2\|h-p\|.
\tag{6.S12}
\]

Choose the polynomial approximation after \(y\) has been fixed, so that \(2\|y\|^2\|h-p\|\) is smaller than the remaining error allowance. Then \(x=vy\in C\) proves the asserted comparison. All multiplier expressions used here land in \(C\); no identity in a nonunital \(A\) is inserted.

If a nonzero ideal contains \(h\neq0\) positive, it contains every \(x^*hx\) and therefore, by the comparison just proved, every positive element of \(C\). It equals \(C\), proving simplicity.

Let \(E\subset C\) be a nonzero hereditary subalgebra. Choose \(e\in E_+\) with \(\|e\|=1\). Define, by scalar continuous functional calculus,

\[
\begin{aligned}
a_0&=(4e-3)_+,\\
b_0&=\min\bigl(8(e-1/4)_+,1\bigr),\\
g&=\min\bigl(4(e-1/2)_+,1\bigr).
\end{aligned}
\tag{6.S13}
\]

These have norm one, vanish at zero, belong to \(E\), and satisfy \(ga_0=a_0\) and \(b_0g=g\). If \(g\) is a projection, we already have a nonzero projection in \(E\). Otherwise \(r=g-g^2\neq0\).

The comparison assertion gives \(z\in C\) with \(\|z^*a_0^2z-b_0\|<1/2\). Lemma 6.9a supplies a contraction \(d\in C\) with

\[
d^*z^*a_0^2zd=(b_0-1/2)_+.
\tag{6.S14}
\]

Put \(k=\min(8e,1)\in E\). Because \(k=1\) wherever \(b_0\neq0\), \(k(b_0-1/2)_+=(b_0-1/2)_+\). The element \(q=\sqrt2\,a_0zdk\) belongs to \(E\): it lies in \(ECE\subset E\). Moreover

\[
\begin{gathered}
q^*q=2(b_0-1/2)_+\leq1,\\
gq=q,\qquad q^*qg=g.
\end{gathered}
\tag{6.S15}
\]

The last identity uses \(b_0g=g\), so functional calculus gives \((b_0-1/2)_+g=g/2\). Consequently \(q^*qq=q\), \(rq=0\), and \(r(1-q^*q)^{1/2}=0\). Also \((1-q^*q)^{1/2}q=0\), from \(q^*qq=q\). In the forced unitization of \(E\), set

\[
u=q+(1-q^*q)^{1/2}.
\tag{6.S16}
\]

The mixed terms vanish, so \(u^*u=1\), while \(ru=0\). Since \(r\neq0\), \(u\) is not unitary. Thus \(p=1-uu^*\) is a nonzero projection. It belongs to \(E\), because the scalar quotient sends \(u\) to one. This proves existence of a nonzero projection in every such \(E\).

Finally every nonzero projection \(p\in C\) is properly infinite. The projections \(p_i=T_i pT_i^*\), \(i=1,2\), are orthogonal and equivalent to \(p\), and their sum \(P=p_1+p_2\in C\) is a projection. Comparison gives \(z\in C\) with \(\|z^*pz-P\|<1/2\). The positive element \(H=Pz^*pzP\) is invertible in \(PCP\). Then

\[
\begin{gathered}
w=pzP H^{-1/2}\in C,\\
w^*w=P,\qquad ww^*\leq p.
\end{gathered}
\tag{6.S17}
\]

The elements \(wT_i p\in C\), \(i=1,2\), have initial projection \(p\), orthogonal final projections, and total final projection at most \(p\). Hence \(p\) is properly infinite. Apply this to the projection just obtained in \(E\). Its implementing partial isometries also belong to \(E\), since they are in \(pCp\subset E\). \(\square\)

If \(A\) is unital, one gets the stronger exact normalization \(x^*hx=1_C\) for every \(h\neq0\) positive. Approximate \(1_C\) within \(1/2\) by the comparison assertion, obtaining \(y^*hy\) positive invertible, and put \(x=y(y^*hy)^{-1/2}\). The projection \(h^{1/2}xx^*h^{1/2}\in\operatorname{Her}(h)\) is then equivalent to \(1_C\).

The tensor norm in this statement is the spatial norm used in Cuntz's II §2.4. The same algebra is obtained with the maximum norm: for unital \(A\), finite normal-word sums lie in \(A\odot E_n\), where Proposition 6.4 proves equality of the two norms; their images in the maximum completion have norm at most that finite-stage norm, and the canonical minimum quotient gives the reverse inequality. Density proves equality on \(A\odot\mathcal O_\infty\). For nonunital \(A\), every commuting representation of \(A\) and \(\mathcal O_\infty\) extends to the forced unitization of \(A\) by \(a+\lambda1\mapsto\pi(a)+\lambda I\); applying the unital norm bound proves the same equality.

Source credit: [Cuntz II (1981)](https://www.theta.ro/jot/archive/1981-005-001/1981-005-001-009.pdf), §2.4, printed p. 107, states the tensor structural conclusion. Lemma 6.9a develops the elementary exact-cutoff argument of [Kirchberg–Rørdam (2002)](https://web.math.ku.dk/~rordam/manus/pi23.pdf), Lemma 2.2, p. 5, including its polar-membership and norm-limit details. The hereditary projection construction uses the scaling mechanism in [Kirchberg's 2022 manuscript](https://www.uni-muenster.de/imperia/md/content/MathematicsMuenster/ekneu1.pdf), Proposition 2.2.1(ii)⇒(i), printed pp. 150–151, with the plateau functions and multiplication order explicitly checked above. For comparison, [Kirchberg–Rørdam (2000)](https://web.math.ku.dk/~rordam/manus/pi1.pdf), Proposition 4.5, manuscript pp. 16–17, gives an alternative tensor proof using absorption results. The direct Fock-compression proof here establishes the stated structural properties separately from the coefficient K-isomorphisms and algebra classification.

## 7. Exercises with solutions

**Exercise 22.1 (basic: orthogonality and the unit).** Starting only with (1.1), prove (1.2) and \([1]=n[1]\) in K-zero.

*Solution.* The positive-compression argument of §1 gives \(q_iq_j=0\) for distinct indices. Since \(s_i^*=s_i^*q_i\) and \(s_j=q_js_j\), their cross product is zero. The diagonal product is one by isometry. Each \(q_i\) is equivalent to one through \(s_i\). Additivity on orthogonal projections gives \([1]=\sum_i[q_i]=n[1]\). This proves that the unit class is annihilated by \(n-1\); its exact order requires Theorem 4.1. \(\square\)

**Exercise 22.2 (intermediate: the connecting map).** Identify the core using the word matrix units, including its normalized K-zero classes.

*Solution.* At length \(r\), (1.2) gives a complete set of \(n^r\)-by-\(n^r\) matrix units. Their total diagonal projection is one by induction on the Cuntz sum, and each diagonal is nonzero. Equation (2.4) appends the same new letter to both indices, giving \(x\otimes1_n\). Its rank-one projection becomes a sum of \(n\) rank-one projections. Thus the stage K-map is multiplication by \(n\); the coordinate of rank \(a\) at stage \(r\) is \(a/n^r\). The union of those coordinates is \(\mathbb Z[1/n]\), and the stage unit has coordinate one. Gauge averaging proves density of the matrix union in the full fixed algebra, so no other core summands occur. \(\square\)

**Exercise 22.3 (intermediate: fullness).** Prove that the projection \(p_0\) in (3.1) is full, and determine the positive dual action on its class.

*Solution.* For every \(r\geq0\), conjugating by a length-\(r\) word gives \(p_{-r}=s_\mu^*p_0s_\mu\). Summing the opposite conjugations over all such words gives \(p_r\), using their total range one. Multiplier stability of the ideal generated by \(p_0\) puts all these projections in it. Coefficient-character approximation puts a dense span \(ap_k\) in the same ideal, proving fullness. Finally \(s_ip_k\) identifies \(p_k\) with each of \(n\) orthogonal pieces of \(p_{k+1}\), so \([p_{-1}]=[p_0]/n\). Positive duality sends \(p_0\) to \(p_{-1}\), not to \(p_1\). \(\square\)

**Exercise 22.4 (advanced: the extension calculation).** Assuming the scalar K-isomorphism (6.5), compute the K-groups from (6.4) and compare the unit generator with Theorem 4.1.

*Solution.* The vacuum projection \(q\) generates \(K_0(\mathcal K)=\mathbb Z\). In \(E_n\), each \(S_iS_i^*\) is equivalent to one, so

\[
[q]=(1-n)[1_{E_n}].
\tag{7.1}
\]

Thus the ideal-inclusion K-map is multiplication by \(1-n\), with its actual sign. Since \(K_1(\mathcal K)=K_1(E_n)=0\), the six-term sequence becomes

\[
\begin{gathered}
0\longrightarrow K_1(\mathcal O_n)
\longrightarrow\mathbb Z,\\
\mathbb Z\xrightarrow{\ 1-n\ }\mathbb Z
\longrightarrow K_0(\mathcal O_n)
\longrightarrow0,
\end{gathered}
\tag{7.2}
\]

where exactness at the first copy of \(\mathbb Z\) makes \(K_1\) the kernel of \(1-n\). That kernel is zero, and the cokernel is \(\mathbb Z/(n-1)\). The quotient is unital, so one maps to \([1_{\mathcal O_n}]\). This is the same distinguished generator as the corner–Takai computation. \(\square\)

**Exercise 22.5 (advanced: matrix amplification).** Decide what K-theory says about \(M_2(\mathcal O_3)\), \(M_3(\mathcal O_3)\), and \(M_2(\mathcal O_4)\). Prove every isomorphism you can obtain by (5.2), and specify the extra input for the remaining positive answer.

*Solution.* For \(\mathcal O_3\), K-zero has order two and the unit is its nonzero class. The unit of \(M_2(\mathcal O_3)\) has class zero, so an isomorphism is impossible. For size three, \(3=1+(3-1)\); the family \(s_1,s_2,s_3\) supplies the row in (5.2), proving \(M_3(\mathcal O_3)\cong\mathcal O_3\). For \(\mathcal O_4\), size two is coprime to three, so it passes the necessary test. Theorem 5.1 proves its isomorphism. Concretely, writing \(x_j=s_j^*\), use the four coisometries

\[
\begin{aligned}
X_1&=\begin{pmatrix}x_1&0\\x_2&0\end{pmatrix},\\
X_2&=\begin{pmatrix}x_3&0\\x_4&0\end{pmatrix},\\
X_3&=\begin{pmatrix}0&x_1\\0&x_2\end{pmatrix},\\
X_4&=\begin{pmatrix}0&x_3\\0&x_4\end{pmatrix}.
\end{aligned}
\tag{7.3}
\]

Their adjoints form a Cuntz family. The sum \(X_1^*X_1+X_2^*X_2=e_{11}\) extracts the two diagonal projections. The first-column matrices give \(y_je_{1,\widehat j}\), and the last-column matrices give \(x_je_{\widehat j,2}\), where \(\widehat j=1\) for odd \(j\) and 2 for even \(j\). Multiplying each pair and summing gives \(\sum_{j=1}^4y_jx_je_{12}=e_{12}\). Its adjoint and the diagonal projections give every scalar matrix unit; extraction of the original entries then gives every \(s_je_{ab}\) and \(s_j^*e_{ab}\). Hence they generate \(M_2(\mathcal O_4)\), and Theorem 2.2 makes the universal surjection an isomorphism. The positive answer is established by actual generators. \(\square\)

## Proof inputs and source comparison

This lesson proves the core, gauge fullness, dual K-map, finite K-groups with their unit, necessary classification restrictions, the congruence-size construction, the Toeplitz Fock and extension models, and the infinite direct-limit calculation. The main finite computation agrees with [Blackadar 1998, Exercise 10.11.8(a)–(e)], using the inverse shift convention. The unit check is supplied explicitly by (4.2). Theorems 2.2 and 5.1 prove finite simplicity, uniqueness and all coprime matrix-size isomorphisms. Proposition 5.2 proves the full properly infinite projection-representation and scale assertion. Propositions 6.2 and Theorem 6.3 prove the scalar and general Toeplitz coefficient K-isomorphisms, respectively.

**Exact programme prerequisites.** We use Lesson 18’s proved PV theorem, Lesson 16’s continuity and UHF computation, the full-corner Morita K-isomorphism, the compact fixed-point corner theorem, and Takai duality from the cited prerequisites. The arbitrary full-multiplier-corner proof used in Theorem 6.3 is Hilbert C*-modules Lesson 14, Theorem 2.4; the tensor construction and adjointable extension are that course’s Lesson 7, Theorems 1.2 and 2.1. The additional finite simplicity, coprime sufficiency, projection scale and full Toeplitz coefficient theorem are proved in this lesson, with their source credits retained below.

[Blackadar 1998] B. Blackadar, *K-Theory for Operator Algebras*, second edition, §6.11, especially Corollary 6.11.8, pp. 45–48; Exercise 10.11.8(a)–(f) and its following \(\mathcal O_\infty\) paragraph, pp. 88–89. [Author's electronic edition](https://bruceblackadar.com/Mathematics/book6.pdf).

[Blackadar 2006] B. Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, II.10.4.17–II.10.4.19, especially Theorem II.10.4.18, pp. 224–225 in the revised author's version. The corner is Morita equivalent to its generated ideal; fullness is a separate condition. [Author's revised edition](https://bruceblackadar.com/Mathematics/Cycr.pdf).

[Cuntz 1977] J. Cuntz, *Simple C*-algebra generated by isometries*, Communications in Mathematical Physics 57 (1977), 173–185; Theorem 2.2 supplies a full proof of the finite simplicity and uniqueness statement credited there. [Original article](https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-57/issue-2/Simple-C-algebras-generated-by-isometries/cmp/1103901288.pdf).

[Cuntz 1981] J. Cuntz developed the K-theory of properly infinite C*-algebras and computed the K-groups of the Cuntz algebras in 1981. Both are presented in B. Blackadar, *K-Theory for Operator Algebras*, second edition, §6.11 and Exercise 10.11.8, the latter through the Pimsner–Voiculescu sequence. [Author's electronic edition](https://bruceblackadar.com/Mathematics/book6.pdf). The additional Toeplitz input used here is formulated in [Katsura 2003].

[Katsura 2003] T. Katsura, *On C*-algebras associated with C*-correspondences*, arXiv:math/0309088v3, Definitions 2.1 and 3.1, pp. 4–5, and Proposition 8.2, p. 17. [Author's preprint](https://arxiv.org/pdf/math/0309088v3). The complete required proof in Appendix C, pp. 24–28, is the comparison source for Theorem 6.3. That theorem writes out the difference-map construction, vacuum corners, rotation identities and both inverses, and treats degenerate left actions by forced unitization. Proposition 6.2 gives an independent scalar proof from the actual Fock extension.

[KT-CP] [Takai duality, Lesson 8](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-CP/KT-CP-08.html#the-surviving-action-and-the-generator-formulas), Theorem 8.3 and Proposition 8.4; [Proper actions, free actions and the orbit space, Lesson 9](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-CP/KT-CP-09.html#averaging-corners-for-compact-groups), Theorem 9.6 and its K-theory prerequisites. The latter uses [Hilbert C*-modules and Morita equivalence, Lesson 14](https://kokunoyumeto.github.io/open-math-courses-public/courses/KT-CP/prerequisites/hilbert-c-star-modules-and-morita-equivalence/morita-invariance-of-k-theory-and-correspondence-maps.html), Corollary 2.2 and Theorem 5.1.

*Verification status: self-checked by the writing AI.*

[Abrams–Ánh–Pardo 2008] G. Abrams, P. N. Ánh and E. Pardo, *Isomorphisms between Leavitt algebras and their matrix rings*, Journal für die reine und angewandte Mathematik 624 (2008), 103–132, [author preprint, 22 February 2008, v2](https://arxiv.org/abs/math/0612552v2), §§1, 3–4 and Theorem 5.1. Theorem 5.1 above gives the full constructive C*-algebra argument; the orbit colors, entry counts, matrix-unit bridge and generator-surjectivity proof are all included.
[Pimsner 1997] M. V. Pimsner proved in 1997, by KK-theory and under hypotheses that include separability, that the coefficient inclusion into the Toeplitz algebra of a C*-correspondence induces an isomorphism of K-groups; the Fock rotation is the classical mechanism. The same isomorphism is proved by K-theory alone, without separability, in T. Katsura, *On C*-algebras associated with C*-correspondences*, Proposition 8.2 and Appendix C. [Author's preprint](https://arxiv.org/pdf/math/0309088v3). Theorem 6.3 follows this route and imposes no separability assumption.

[Cuntz 1981 II] J. Cuntz, *K-theory for certain C*-algebras. II*, Journal of Operator Theory 5 (1981), 101–108, Theorem 1.5 and §§2.1–2.2. [Freely readable original paper](https://www.theta.ro/jot/archive/1981-005-001/1981-005-001-009.pdf). Theorem 4.2 independently derives the untwisted coefficient result from the gauge core, its full averaging corner, Takai duality and the proved PV sequence, with complete torsion comparison. Theorems 6.6 and 6.8 and Proposition 6.7 now prove the finite twisted sequence, nonunital reduction, actual inverse-action map and boundaries, whole-quotient identity, and twisted infinite coefficients. Their vacuum coordinates have scalar map 1−n. No identity with the separately constructed gauge/PV boundary in Theorem 4.2 is asserted. No source expression is adapted.

[Cuntz 1981 II, infinite coefficients] J. Cuntz, *K-theory for certain C*-algebras. II*, Journal of Operator Theory 5 (1981), 101–108, §2.4. [Freely readable original paper](https://www.theta.ro/jot/archive/1981-005-001/1981-005-001-009.pdf). Propositions 6.4 and Theorem 6.5 provide the complete coefficient tensor identification, both natural K-isomorphisms and the direct-limit proof. Human source expression is not copied or reconstructed.
