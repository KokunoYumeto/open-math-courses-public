# Normalized induction and Jacquet modules

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

Parabolic induction builds a representation from two characters of the diagonal torus. The Jacquet module measures what remains when upper unipotent translations are made trivial. Their adjunction tells us exactly why a noncuspidal irreducible representation embeds in a principal series. Keeping the square root of the modulus in both constructions is essential: it determines which character is a subrepresentation, which is a quotient, and what happens to the Steinberg representation.

We use the smooth representation, exact compact average and contragredient conventions of Smooth local representations and the Hecke-module dictionary. Let \(F\), \(\mathcal O\), \(\varpi\), \(q\), \(G=\mathrm{GL}_2(F)\) and \(K_0=\mathrm{GL}_2(\mathcal O)\) be as there. Haar measure on \(G\) has \(\operatorname{vol}(K_0)=1\); additive measure has \(\operatorname{vol}(\mathcal O)=1\). Put

\[
B=TN,\quad T=\{\operatorname{diag}(a,d)\},\quad
N=\{n(x)=\begin{pmatrix}1&x\\ 0&1\end{pmatrix}\},\quad
w=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix},\quad \nu(x)=|x|.
\]

We prove the induction, averaging, reciprocity, principal-Jacquet and embedding assertions used here. Section 5 proves both directions of the compact-support characterization of supercuspidality, together with admissibility of every irreducible smooth GL₂ representation.

## 1. Induction with the square-root modulus

The modulus used for normalized induction is

\[
\delta_B(\operatorname{diag}(a,d))=|a/d|.
\tag{1.1}
\]

It is the factor by which torus conjugation scales additive Haar measure on \(N\), since \(t n(x)t^{-1}=n(ax/d)\). Some definitions of the modular function of a locally compact group use its reciprocal; (1.1) fixes our induction convention without that ambiguity.

For a smooth \(T\)-representation \(\sigma\), extend it trivially over \(N\). Define \(I(\sigma)\) to be the smooth functions with values in its space such that

\[
f(ntg)=\delta_B(t)^{1/2}\sigma(t)f(g),
\qquad (R(h)f)(g)=f(gh).
\tag{1.2}
\]

Smooth here includes a right compact open stabilizer. In the character case write
\(I(\chi_1,\chi_2)\) for \(\sigma(t)=\chi_1(a)\chi_2(d)\).

Two elementary decompositions describe these functions. First \(G=BK_0\): scale the bottom row of a matrix to a primitive row in \(\mathcal O^2\), complete it to a matrix in \(K_0\), and multiply by its inverse to leave an upper triangular matrix. Thus
\(B\backslash G\simeq\mathbb P^1(F)\) is compact. Second,

\[
G=B\ \sqcup\ BwN.
\tag{1.3}
\]

If \(g=\begin{pmatrix}a&b\\ c&d\end{pmatrix}\) has \(c\ne0\), its explicit open-cell factorization is
\(g=\begin{pmatrix}\det(g)/c&a\\ 0&c\end{pmatrix}w n(d/c)\).
If \(c=0\), it is in \(B\). The open cell has coordinate \(x\in F\); the remaining closed point corresponds to \(B\). Locally constant sections on this compact quotient have a common right open stabilizer: cover it by finitely many local constant charts and intersect the fixing subgroups. This explains the equivalence with the usual locally constant induction definition.

**Proposition 1.1 — admissibility.** Every character principal series \(I(\chi_1,\chi_2)\) is admissible.

**Proof.** Restriction to \(K_0\) determines the function by (1.2). If it is fixed by compact open \(J\), it is fixed by \(J\cap K_0\), and its restriction is determined by the finite set \(K_0/(J\cap K_0)\). Some possible values are excluded by the left \(B\cap K_0\)-character condition, but that only decreases the dimension. Thus
\(\dim I(\chi_1,\chi_2)^J\leq[K_0:J\cap K_0]<\infty\).
Smoothness is in the definition. \(\square\)

**Proposition 1.2 — induced contragredient.**
\(I(\chi_1,\chi_2)^\vee\simeq I(\chi_1^{-1},\chi_2^{-1})\).

**Proof.** The bilinear pairing can be written, up to a fixed positive scalar, as

\[
\langle f,f'\rangle=\int_F f(w n(x))f'(w n(x))\,dx.
\tag{1.4}
\]

It converges. In Iwasawa coordinates for \(w n(x)\), the ratio of the diagonal norms is \(\max(1,|x|)^{-2}\); the two inverse characters cancel in the product, leaving a bound \(C\max(1,|x|)^{-2}\). Its integral is finite by the valuation shells. This is the same density integral as the compact \(K_0\)-pairing; we can verify invariance directly in the open chart.

Right upper unipotents translate \(x\). For \(t=\operatorname{diag}(a,d)\),
\(w n(x)t=\operatorname{diag}(d,a)w n(xd/a)\).
The product multiplier is \(|d/a|\), which cancels the change of additive measure. For right \(w\) and \(x\ne0\),
\(w n(x)w=\begin{pmatrix}x^{-1}&-1\\ 0&x\end{pmatrix}w n(-x^{-1})\).
The product multiplier is \(|x|^{-2}\), exactly the Jacobian of inversion. This change of variables follows on balls avoiding zero from their scaled radii, or from the local-field derivative of inversion. The point zero has measure zero. The elements \(N,T,w\) generate \(G\) by (1.3), proving invariance.

The pairing is nondegenerate. A nonzero section is nonzero on an open-cell ball; pairing with a section supported on a sufficiently small such ball detects it. Smoothness and invariance give an injection of the claimed induced representation into the smooth dual. For \(J\subset K_0\), both inducing characters and their inverses allow values at exactly the same double cosets \((B\cap K_0)\backslash K_0/J\): a value is allowed precisely when the character is trivial on the corresponding stabilizer. Their fixed-space dimensions are therefore equal. Fixed-space duality from the preceding lesson makes the injection surjective on every \(J\)-fixed space, hence on all smooth vectors. \(\square\)

## 2. Coinvariants and exact averaging

For a smooth representation \(V\), define

\[
V(N)=\operatorname{span}\{\pi(n)v-v:n\in N,v\in V\},\qquad V_N=V/V(N).
\tag{2.1}
\]

The torus acts on \(V_N\), since it normalizes \(N\). We use two names to keep its normalization explicit: \(V_N\) has the original torus action, whereas

\[
r_N(V)=\delta_B^{-1/2}\otimes V_N
\tag{2.2}
\]

is the normalized Jacquet module. Vanishing is independent of the twist.

For a compact additive open subgroup \(U\subset F\), put
\(E_Uv=\operatorname{vol}(U)^{-1}\int_U\pi(n(x))v\,dx\).
This is an exact finite-sum average. The subgroups \(\varpi^{-m}\mathcal O\), \(m\geq0\), exhaust \(F\).

**Lemma 2.1 — Jacquet averaging lemma.** A vector \(v\) lies in \(V(N)\) if and only if \(E_Uv=0\) for some compact additive open \(U\). Once this happens, it holds for every larger such \(U\).

**Proof.** If \(v=\sum_i(\pi(n(x_i))v_i-v_i)\), choose \(U\) containing all the finitely many \(x_i\). Translation invariance of its average kills each difference. Conversely, if \(E_Uv=0\), write the integral as a finite linear combination of orbit vectors. Then \(v=v-E_Uv\) is the same finite average of differences \(v-\pi(n(x))v\), and belongs to \(V(N)\). For \(U\subset U'\), averaging first over \(U\) and then over \(U'\) gives \(E_{U'}E_U=E_{U'}\), proving the last assertion. \(\square\)

**Proposition 2.2 — exactness.** Both \(V\mapsto V_N\) and \(r_N\) preserve short exact sequences of smooth representations.

**Proof.** For \(0\to V'\to V\to V''\to0\), coinvariants are plainly surjective at the right. If \(v'\in V'\) maps to zero in \(V_N\), Lemma 2.1 gives an average killing it in \(V\), hence also in \(V'\), so it was already zero in \(V'_N\). If the image of \(v\in V\) is zero in \(V''_N\), an average \(E_U\) kills that image. Thus \(E_Uv\in V'\), and \(v-E_Uv\in V(N)\) by its finite difference expression. The class of \(v\) is therefore in the image of \(V'_N\). This proves exactness in the middle. Twisting the torus action by a character preserves it. \(\square\)

This proof uses the increasing compact subgroups of this unipotent group. Coinvariants for an arbitrary group are generally only right exact.

## 3. Reciprocity by evaluating at the identity

**Theorem 3.1 — normalized Frobenius reciprocity.** For smooth \(V\) of \(G\) and smooth \(\sigma\) of \(T\),

\[
\operatorname{Hom}_G(V,I(\sigma))
\simeq\operatorname{Hom}_T(V_N,\delta_B^{1/2}\sigma)
\simeq\operatorname{Hom}_T(r_N(V),\sigma).
\tag{3.1}
\]

**Proof.** Given \(A:V\to I(\sigma)\), set \(\ell(v)=(Av)(1)\). Equivariance and (1.2) give
\(\ell(\pi(n)v)=\ell(v)\) and
\(\ell(\pi(t)v)=\delta_B(t)^{1/2}\sigma(t)\ell(v)\).
Hence it factors through the stated torus map on the unnormalized coinvariants.

Conversely, from such an \(\ell\), define

\[
(A_\ell v)(g)=\ell(\pi(g)v).
\tag{3.2}
\]

Its left \(N,T\)-transformation is (1.2). A compact open subgroup fixing \(v\) fixes this function on the right, so it is a smooth induced vector. Also \(A_\ell(\pi(h)v)(g)=A_\ell v(gh)\), proving \(G\)-equivariance. Evaluation at one recovers \(\ell\). Starting from \(A\), formula (3.2) gives \((A\pi(g)v)(1)=(Av)(g)\), recovering \(A\). These are inverse linear maps, natural in both arguments. Moving the square-root twist from the target to the source gives the second isomorphism. \(\square\)

Evaluation on an induced function transforms by \(\delta_B^{1/2}\sigma\), rather than by \(\sigma\) alone. Omitting this factor would change the inducing characters in the embedding theorem.

## 4. The two Bruhat cells and the principal-series Jacquet module

**Theorem 4.1.** There is an exact sequence of torus modules

\[
0\longrightarrow\chi_2\otimes\chi_1
\longrightarrow r_N(I(\chi_1,\chi_2))
\longrightarrow\chi_1\otimes\chi_2\longrightarrow0.
\tag{4.1}
\]

In particular its dimension is two and its semisimplification consists of those two characters. This does not assert splitting when the characters coincide.

**Proof.** Evaluation at one gives a surjection of \(B\)-modules
\(I\to\mathbb C_{\delta_B^{1/2}(\chi_1\otimes\chi_2)}\), with \(N\) trivial on the target. Its kernel consists of sections vanishing near the closed point. On the open cell such a section is exactly
\(\psi(x)=f(w n(x))\in C_c^\infty(F)\).
Conversely a compactly supported locally constant \(\psi\) extends using (1.2) and zero near the closed point. Thus we have an exact \(B\)-sequence with this open-cell kernel.

Right \(n(b)\) acts on it by \(\psi(x)\mapsto\psi(x+b)\). Its coinvariants are one dimensional, identified by \(\psi\mapsto\int_F\psi(x)dx\). To prove this directly, choose an additive compact open \(U\) fixing \(\psi\) and write it as a finite sum \(\sum_i c_i1_{x_i+U}\). Its integral is zero exactly when \(\sum_i c_i=0\). In that case it is a sum of the translated differences \(1_{x_i+U}-1_U\). All differences have zero integral; this proves both the kernel and surjectivity claims.

On this open-cell function the torus action is

\[
R(t)\psi(x)=|d/a|^{1/2}\chi_1(d)\chi_2(a)\psi(xd/a).
\tag{4.2}
\]

Integration contributes the additional factor \(|a/d|\), so the open-cell unnormalized coinvariant character is
\(\delta_B^{1/2}(\chi_2\otimes\chi_1)\).
The closed-cell character is \(\delta_B^{1/2}(\chi_1\otimes\chi_2)\). Apply Proposition 2.2 to the two-cell sequence and twist by \(\delta_B^{-1/2}\). This proves (4.1), with dimensions one on both ends. \(\square\)

If these two characters are distinct, choose a torus element at which their values differ. Its two distinct eigenvalues split the two-dimensional module, and commuting torus elements preserve the eigenspaces. For equal characters this argument is unavailable; a semisimplification statement is the safe general conclusion.

## 5. Noncuspidal embeddings and a support test

A smooth irreducible representation is called **cuspidal** or **supercuspidal** here when \(V_N=0\). For GL₂ there is one proper parabolic up to conjugacy. The phrase “absolutely cuspidal” in Jacquet–Langlands describes this class.

**Theorem 5.1 — noncuspidal embedding.** Every irreducible smooth representation with \(V_N\ne0\) embeds in some \(I(\chi_1,\chi_2)\).

**Proof.** We first prove the existence of a character quotient of \(V_N\), without assuming a separate Jacquet-admissibility theorem. Choose a nonzero cyclic vector \(v\) of \(V\). Its compact \(K_0\)-orbit spans a finite-dimensional space: smoothness gives a finite orbit modulo an open stabilizer in the compact group. Choose a basis \(v_1,\ldots,v_s\) of that span. By \(G=BK_0\), the classes of these vectors generate \(V_N\) under \(T\): after \(N\) has been made trivial, \([\pi(tn)v_i]=\pi(t)[v_i]\). Choose an open subgroup \(T_0\) of the compact unit torus fixing these finitely many classes. Commutativity makes it fix all of \(V_N\). Thus \(V_N\) is a finitely generated module over the commutative group algebra \(\mathbb C[T/T_0]\).

Such a nonzero module has a maximal proper submodule. In Zorn's argument a chain of proper submodules cannot have union equal to the module, since its finite set of generators would then lie in one member. The simple quotient has countable dimension: the original irreducible smooth \(V\) has countable dimension by the coset argument in the preceding lesson. Apply the countable Schur lemma to this simple torus representation. Every torus action commutes with every other one, hence is scalar; simplicity forces the quotient to be one dimensional. This supplies a smooth character \(\lambda\) of \(T\).

Set \(\sigma=\delta_B^{-1/2}\lambda\), and write it as \(\chi_1\otimes\chi_2\), since \(T\simeq F^\times\times F^\times\). Its quotient map is a nonzero member of the middle space in (3.1). Reciprocity gives a nonzero map \(V\to I(\chi_1,\chi_2)\). Its invariant kernel is zero by irreducibility, proving the embedding. \(\square\)

For \(\ell\in V^\vee\) and \(v\in V\), a matrix coefficient is
\(m_{v,\ell}(g)=\ell(\pi(g)v)\).
Its support is compact modulo the centre if it is contained in \(ZC\) for a compact \(C\subset G\). Scalar central character makes its nonvanishing set centre-invariant; only that support condition, rather than a bound on central growth, is intended.

**Theorem 5.2 — compact coefficients force cuspidality.** If every matrix coefficient of an irreducible smooth \(V\) is compactly supported modulo \(Z\), then \(V_N=0\).

**Proof.** Suppose \(V_N\ne0\), and choose the embedding of Theorem 5.1. Write \(\ell(v)\) for evaluation at one after that embedding. It is a nonzero linear functional with
\(\ell(\pi(n)v)=\ell(v)\) and \(\ell(\pi(t)v)=\lambda(t)\ell(v)\), where \(\lambda=\delta_B^{1/2}(\chi_1\otimes\chi_2)\). It need not itself be smooth, so we now produce a smooth functional.

Choose \(n\geq1\) such that \(\lambda\) is trivial on diagonal units congruent to one modulo \(\varpi^n\). Average
\(\ell_n(u)=\operatorname{vol}(K_n)^{-1}\int_{K_n}\ell(\pi(k)u)dk\).
For each \(u\) this is a finite sum, and the resulting functional is \(K_n\)-fixed, hence in \(V^\vee\).

Every \(k=\begin{pmatrix}a&b\\ c&d\end{pmatrix}\in K_n\) has the factorization

\[
k=n(b/d)\operatorname{diag}(\det(k)/d,d)
\begin{pmatrix}1&0\\ c/d&1\end{pmatrix}.
\tag{5.1}
\]

Both diagonal units are congruent to one, and both unipotent parameters lie in \(\varpi^n\mathcal O\). Put \(t_r=\operatorname{diag}(\varpi^r,1)\), and fix \(v\) with \(\ell(v)\ne0\). In \(t_r^{-1}kt_r\), the upper parameter expands but remains invisible to \(\ell\); the diagonal still has character one; the lower parameter contracts to \(\varpi^r c/d\). For all sufficiently large \(r\), uniformly in \(k\in K_n\), that lower unipotent fixes \(v\) by smoothness. Hence

\[
\ell_n(\pi(t_r)v)
=\lambda(t_r)\ell(v)\ne0
\quad(r\text{ sufficiently large}).
\tag{5.2}
\]

These \(t_r\) escape every compact subset modulo the centre. For example the continuous centre-invariant function \(\|g\|\|g^{-1}\|\), using the maximum-entry norm, is \(q^r\) on them and bounded on each compact projective subset. Thus the smooth matrix coefficient (5.2) is not compact modulo the centre, a contradiction. \(\square\)

**Theorem 5.3 — vanishing Jacquet module gives compact support.** Let \(V\) be an irreducible smooth representation with \(V_N=0\). For every compact open \(J\) and every \(v\in V\), the vector-valued function
\[
g\longmapsto E_J\pi(g)v
\]
vanishes outside \(ZC_{J,v}\), for a compact subset \(C_{J,v}\subset G\). In particular every smooth matrix coefficient is compactly supported modulo \(Z\), and \(V\) is admissible.

**Proof.** The compact \(K_0\)-orbit of \(v\) spans a finite-dimensional space \(W\). Indeed an open stabilizer has finite index after intersection with \(K_0\). Choose a basis \(v_1,\ldots,v_s\) of \(W\). Since \(V_N=0\), Lemma 2.1 gives one sufficiently large additive subgroup
\[
U=\varpi^{-R}\mathcal O,\qquad R\geq0,\qquad E_Uv_i=0
\quad(1\leq i\leq s).
\tag{5.3}
\]
Choose \(m\geq1\) with \(K_m\subset J\). The subgroup \(K_m\) is normal in \(K_0\), since conjugation by an integral invertible matrix preserves \(M_2(\mathcal O)\).

We use the Cartan decomposition in the form
\[
G=\bigcup_{r\geq0}ZK_0t_rK_0,\qquad
t_r=\operatorname{diag}(\varpi^r,1).
\tag{5.4}
\]
Here is an elementary proof, valid over every nonarchimedean local field. Scale an invertible matrix by a scalar so all its entries are integral and at least one is a unit. Integral row and column permutations move a unit to the first diagonal entry. Scale that entry to one using a diagonal unit, and eliminate its row and column by integral elementary matrices. The result is \(\operatorname{diag}(1,b)\), with \(b\ne0\) integral. Write \(b=\varpi^ru\), with \(u\) a unit and \(r\geq0\), absorb \(u\) into \(K_0\), and interchange the two coordinates. This is (5.4).

For \(r\geq m+R\), \(x\in U\) and \(k\in K_0\), we have
\[
kt_rn(x)(kt_r)^{-1}
=kn(\varpi^rx)k^{-1}\in K_m\subset J.
\tag{5.5}
\]
The normalized compact average satisfies \(E_J\pi(j)=E_J\) for \(j\in J\). Consequently
\[
E_J\pi(kt_r)v_i
=E_J\pi(kt_rn(x))v_i.
\]
Average this identity over \(x\in U\), using the exact finite-sum integral. Equation (5.3) gives
\[
E_J\pi(kt_r)v_i
=E_J\pi(kt_r)E_Uv_i=0
\qquad(r\geq m+R).
\tag{5.6}
\]
Every \(\pi(k_2)v\) is a linear combination of the \(v_i\). The smooth central character from Lesson 5, Theorem 4.1, makes the scalar \(z\) in (5.4) act by \(\omega(z)\). Thus the vector-valued function vanishes outside \(ZC_{J,v}\), where
\[
C_{J,v}=\bigcup_{0\leq r<m+R}K_0t_rK_0
\tag{5.7}
\]
is a finite union of compact sets.

If \(\ell\in V^\vee\), choose \(J\) fixing it. Then \(\ell(u)=\ell(E_Ju)\), so (5.6) proves compact support of \(\ell(\pi(g)v)\) modulo \(Z\). This support assertion uses no admissibility or Kirillov model.

To prove admissibility, choose \(v\ne0\). Irreducibility says that its \(G\)-orbit spans \(V\), so the vectors \(E_J\pi(g)v\) span \(V^J\). By the bound just proved, it suffices to use \(g\in C_{J,v}\); central elements only multiply vectors by scalars. The locally constant orbit map \(g\mapsto\pi(g)v\) has finite image on this compact set: finitely many right cosets of the open stabilizer of \(v\) cover it. Hence these averages span a finite-dimensional space. This proves \(\dim V^J<\infty\) for every \(J\). \(\square\)

Together, Theorems 5.2–5.3 prove the equivalence between vanishing Jacquet module and compact support of all smooth matrix coefficients. The stronger vector-valued support bound is what also gives admissibility; bounding one scalar coefficient at a time would not supply a uniform bound for the fixed space.

**Theorem 5.4 — smooth admissibility for GL₂.** Every irreducible smooth complex representation of \(\mathrm{GL}_2(F)\) is admissible.

**Proof.** If \(V_N=0\), use Theorem 5.3. Otherwise Theorem 5.1 embeds \(V\) into a character principal series, whose fixed spaces are finite dimensional by Proposition 1.1. The injection on \(J\)-fixed spaces therefore proves the same bound for \(V\). The proof of Theorem 5.1 used compact orbit spans, countable Schur and a finitely generated torus quotient; it did not assume admissibility. Thus there is no circular invocation of the theorem being proved. \(\square\)

## 6. The trivial and Steinberg representations

Let
\(\sigma_-=(\nu^{-1/2},\nu^{1/2})\) and
\(\sigma_+=(\nu^{1/2},\nu^{-1/2})\).
For \(I_-=I(\sigma_-)\), the multiplier in (1.2) is one, so it is \(C^\infty(\mathbb P^1(F))\), with constant functions a trivial subrepresentation. Define

\[
\mathrm{St}=I_-/\mathbb C1.
\tag{6.1}
\]

This is the usual Steinberg space. Its irreducibility will be proved in the following local-classification lesson; the following construction and Jacquet calculation require no classification theorem.

By Proposition 1.2 and exact smooth duality,
\(I_+\) has a trivial quotient and its kernel is \(\mathrm{St}^\vee\). We can identify that kernel with \(\mathrm{St}\) directly. For \(f\in I_-\), define

\[
(Af)(g)=\int_F\bigl(f(w n(x)g)-f(g)\bigr)dx.
\tag{6.2}
\]

The integrand has compact support in \(x\): large \(x\) approaches the closed point of the compact projective line, and local constancy makes both values equal eventually. The formula commutes with right translation and retains every right stabilizer of \(f\). Left upper unipotents translate \(x\), and left \(t\) rescales it by \(d/a\). Since \(f\) is left \(B\)-invariant, these operations give
\((Af)(ntg)=\delta_B(t)(Af)(g)\).
That is exactly the induction multiplier for \(I_+\), so \(A:I_-\to I_+\) is a smooth intertwiner.

Its kernel is the constants. If \(Af=0\), take a point where the real part of \(f\) achieves its maximum on the compact projective line. At a corresponding \(g\), the real part of the integrand in (6.2) is nonpositive everywhere and is strictly negative on an open ball if that real part is not constant. Its integral cannot then vanish. Thus the real part is constant; applying the same argument to the imaginary part proves the claim. Therefore \(A\) injects \(\mathrm{St}\) into \(I_+\).

Let \(L:I_+\to\mathbb C\) be its nonzero invariant quotient functional, given by pairing with the constant vector in \(I_-\). There is no invariant functional on \(I_-\). To check this, restrict one to its open-cell \(C_c^\infty(F)\). Translation invariance makes it a multiple of integration by the coinvariant proof in Section 4. Under \(T\), that integration transforms by \(\delta_B\), so invariance makes the multiple zero. It would then be a multiple of closed-point evaluation; right \(w\) applied to an open-cell function nonzero at \(w\) shows that evaluation is not invariant. Hence \(LA=0\), and the image lies in \(\ker L\).

For every \(J\subset K_0\), the restrictions of \(I_-\) and \(I_+\) to \(K_0\) have identical fixed-space dimensions: all the inducing characters are trivial on compact units. Exactness of compact invariants gives
\[
\dim\mathrm{St}^J=\dim I_-^J-1=\dim I_+^J-1=\dim(\ker L)^J.
\]
The injection is therefore onto on each fixed space and onto globally. We have proved

\[
0\longrightarrow\mathrm{St}\longrightarrow
I(\nu^{1/2},\nu^{-1/2})\longrightarrow1\longrightarrow0,
\tag{6.3}
\]

and also \(\mathrm{St}\simeq\mathrm{St}^\vee\). Reversing the inducing characters instead gives the trivial subrepresentation in (6.1). This explains the subrepresentation/quotient orientation in the example.

For the trivial representation, unnormalized coinvariants are trivial, so

\[
r_N(1)=\nu^{-1/2}\otimes\nu^{1/2}=\sigma_-.
\tag{6.4}
\]

Apply exactness to \(0\to1\to I_-\to\mathrm{St}\to0\). The two distinct characters in \(r_N(I_-)\) are \(\sigma_-\) and \(\sigma_+\). Removing the injected \(\sigma_-\) leaves

\[
r_N(\mathrm{St})=\nu^{1/2}\otimes\nu^{-1/2}=\sigma_+.
\tag{6.5}
\]

Thus Steinberg is not supercuspidal. In the unnormalized convention its Jacquet character is \(\delta_B\); the trivial representation's is one. These are receiving calculations, not consequences of the word “special” sometimes used for Steinberg.

## 7. Exercises with complete solutions

**Exercise 7.1 — the modulus.** Derive (1.1) from the action of \(T\) on \(N\), and explain the square root in the normalized induction convention.

**Solution 7.1.** Matrix multiplication gives \(t n(x)t^{-1}=n((a/d)x)\). Additive Haar measure scales by \(|a/d|\), so the conjugation modulus is \(\delta_B(t)=|a/d|\). In normalized induction a product of a section and a dual section transforms by \(\delta_B\), since their character parts cancel and each contributes its square root. In the open Bruhat chart this is exactly the density factor that cancels the coordinate change, as (1.4) verifies. Thus the square root makes the induced dual use inverse characters without an additional modulus twist. For unitary characters, the same density cancellation with complex conjugation gives an invariant positive inner product.

**Exercise 7.2 — the averaging criterion.** Prove Jacquet's lemma, including persistence under enlargement of the averaging subgroup.

**Solution 7.2.** A vector in \(V(N)\) is a finite sum of differences with finitely many unipotent parameters. Choose a compact additive open subgroup containing those parameters. Averaging over it kills each difference by translation of its Haar measure. Conversely, if an average kills a vector, subtract that average from the vector; its finite orbit decomposition writes the result as a finite linear combination of unipotent differences. This proves the criterion. For nested subgroups, iterated normalized averages satisfy \(E_{U'}E_U=E_{U'}\), so once an average is zero all larger ones are zero. Neither direction requires admissibility.

**Exercise 7.3 — two Jacquet modules.** Compute the normalized and unnormalized Jacquet modules of the trivial and Steinberg representations, retaining the inducing order.

**Solution 7.3.** The trivial representation has unnormalized Jacquet character one and normalized character \(\delta_B^{-1/2}=\sigma_-\). Start with \(I_-=I(\nu^{-1/2},\nu^{1/2})\), whose constants give \(0\to1\to I_-\to\mathrm{St}\to0\). The principal-series two-cell computation gives the two distinct normalized characters \(\sigma_-\) and \(\sigma_+\). Exactness injects the one-dimensional \(\sigma_-\) from the trivial subrepresentation, so the quotient is the one-dimensional \(\sigma_+\). Multiplying by \(\delta_B^{1/2}\) makes the unnormalized Steinberg character \(\delta_B\). Equivalently use (6.3): the quotient trivial character in \(I_+\) is \(\sigma_-\), leaving the Steinberg subrepresentation's \(\sigma_+\). Both computations agree and show that its Jacquet module is nonzero.

**Exercise 7.4 — reciprocity and its factor.** Prove (3.1), verifying smoothness and that its two constructions are inverse.

**Solution 7.4.** For an intertwiner \(A\), identity evaluation \(\ell(v)=(Av)(1)\) is unchanged by \(\pi(n)\), so it kills \(V(N)\). Its value on \(\pi(t)v\) is \(\delta_B(t)^{1/2}\sigma(t)\ell(v)\), giving the required map on unnormalized coinvariants. Conversely set \((A_\ell v)(g)=\ell(\pi(g)v)\). These two transformation identities prove its left induction law. A compact open stabilizer of \(v\) fixes the function on the right, proving smoothness. Multiplication \(\pi(g)\pi(h)=\pi(gh)\) proves the intertwining identity. Evaluation at one gives back \(\ell\), and equivariance of an original \(A\) gives \((A\pi(g)v)(1)=(Av)(g)\), recovering its entire function. Finally twisting the source torus action by \(\delta_B^{-1/2}\) converts the middle Hom space to \(\operatorname{Hom}_T(r_N(V),\sigma)\). This proves the adjunction with its precise normalization.

## References

- H. Jacquet and R. P. Langlands, [*Automorphic Forms on GL(2)*](https://publications.ias.edu/sites/default/files/Automorphic-forms-on-GL2.pdf) (1970), §3, equation (3.1), uses \(B(\mu_1,\mu_2)\) with precisely the multiplier \(\mu_1(a)\mu_2(d)|a/d|^{1/2}\). Thus its parameters agree with ours; no further twist is needed. The compact-support argument before Proposition 2.20 and the averaging characterization in Proposition 2.22 are original references for the supercuspidal characterization proved here in Theorems 5.2–5.3.
- J. R. Getz and H. Hahn, *An Introduction to Automorphic Representations*, draft of 22 April 2022, §§8.1–8.3, especially Propositions 8.2.2–8.2.3 and 8.3.1, Theorem 8.3.3 and the smooth admissibility theorem 5.3.4. The [author's graduate-text page](https://sites.duke.edu/jgetz/graduate-text/) supplies the reference. Our noncuspidal GL₂ embedding proof uses a finitely generated torus quotient and countable Schur, avoiding a separate quoted theorem on admissibility of Jacquet modules.
- The smooth local lesson, Propositions 1.1 and 2.1, Theorems 4.1 and 5.2, for exact averages, countable Schur, admissible duality and its exactness.
