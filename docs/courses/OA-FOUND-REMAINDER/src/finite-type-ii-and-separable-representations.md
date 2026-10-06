# Finite type II algebras and separable representations

*Written by GPT-6.1 Sol (OpenAI), Ultra, September–October 2026. Self-checked by the writing AI. Original text: CC0 1.0.*

A representation need not preserve strong limits of projections. Nevertheless, a sigma-finite von Neumann algebra with no finite type I summand has no such failure on a separable Hilbert space: every representation there is normal. The properly infinite case was proved in [Proper infiniteness and automatic normality](../reader/proper-infiniteness-and-automatic-normality.html). Here we prove the finite type II case. The argument uses small projections twice: first to construct balanced signs, then to construct disjoint copies.

We use the normal–singular representation decomposition and singular-functional criterion in [The universal enveloping von Neumann algebra and W*-algebras](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html), Theorems 10.3 and 11.2. From [Projections and types](../../foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras.html) we use Proposition 13.3: in an algebra without a type I part every projection splits into two orthogonal equivalent projections. [Abelian operator algebras](../../foundations-of-von-neumann-algebras/abelian-operator-algebras.html), Lemma 4.2 and Theorem 7.1, supplies the clopen neighborhood basis and hyperstonean spectrum. [Traces, part A](../reader/supplements/traces-on-von-neumann-algebras-part-a-def-v-2-1-to-def-v-2-17.html), Theorem 5.2 and Corollary 5.4, supplies the faithful normal centre-valued trace and the equivalence
\[
p\precsim q\quad\Longleftrightarrow\quad T(p)\leq T(q).
\tag{0.1}
\]
Corollary 3.2 of [Central averaging and maximal ideals](../reader/central-averaging-and-maximal-ideals.html#3-finite-algebras-and-uniqueness) supplies \(T(I)=I\cap Z(M)\) for a norm-closed two-sided ideal \(I\) in a finite algebra. For commutative algebras we use their complete [Gelfand representation](../../foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#oa-fnd-cf-04) and the full [finite Radon representation](../../harmonic-analysis-on-locally-compact-groups/reader/haar-measure-on-locally-compact-groups.html#oa-fnd-hm-01), Theorem 2.2 and Proposition 2.3. Ordinary finite-measure Radon–Nikodym, Egoroff and countable-additivity facts are measure-theory prerequisites. The full [normal-vector decomposition](../../foundations-of-von-neumann-algebras/the-double-commutant-theorem.html#oa-fnd-bi-14), Theorem 10.1, supplies the final separable GNS embedding.

Blackadar’s freely readable *Operator Algebras* treats the factor specialization and the abelian boundary example; Takesaki’s book provides further context. The proof here handles an arbitrary centre explicitly, including a singular central state, clopen cutoffs, the absolutely continuous measure case and the disjoint-copy construction, using the complete programme prerequisites linked above.

Throughout, \(M\) is finite of type II, \(Z=Z(M)\), and
\[
T:M\longrightarrow Z
\]
is its unital centre-valued trace. “Sigma-finite” means that \(M\) has a faithful normal state. Type II here allows an arbitrary centre; no separability of the predual is assumed.

## 1. A kernel leaves its trace on the centre

Let \(\rho:M\to B(H)\) be a nonzero unital singular representation. Suppose \(N=\rho(M)''\) has a faithful normal state \(\omega\). Set
\[
\psi=\omega\circ\rho,\qquad I=\ker\rho.
\]
Then \(\psi\) is a singular state. Indeed, normal functionals on \(N\) extend normally to \(B(H)\) and are norm-convergent sums of vector coefficients; singular coefficients form a norm-closed space. Faithfulness gives
\[
\psi(x^*x)=0\quad\Longleftrightarrow\quad \rho(x)=0.
\tag{1.1}
\]

**Lemma 1.1.** If \(M\) is sigma-finite, there are decreasing central projections \(z_n\) such that
\[
z_n\longrightarrow0\ \text{strongly},\qquad
\rho(z_n)=1,\qquad \psi(z_n)=1.
\tag{1.2}
\]

**Proof.** The singular-functional criterion says that every nonzero projection has a nonzero subprojection on which \(\psi\) vanishes. Choose a maximal orthogonal family of such subprojections. Its strong sum is \(1\), and sigma-finiteness makes it countable. Denote it by \((e_j)\), allowing zero terms if necessary. By (1.1), every \(e_j\) belongs to \(I\).

Since \(T(I)=I\cap Z\), the positive central elements
\[
s_n=\sum_{j=1}^nT(e_j)
\]
belong to \(I\). They increase strongly to \(1\), by normality of \(T\). Define
\[
r_n=1_{[1/2,\,1]}(s_n)\in Z.
\]
These projections increase. They also belong to \(I\): bounded Borel functional calculus gives \(r_n=s_nb_n\), with \(b_n(t)=t^{-1}\) on \([1/2,1]\) and zero elsewhere. The inequality
\[
1-r_n\leq2(1-s_n)
\]
shows that \(r_n\uparrow1\) strongly. For example apply a faithful normal state of \(Z\); its value on \(1-r_n\) tends to zero, so the decreasing complementary projections have zero limit. Put \(z_n=1-r_n\). Since \(\rho(r_n)=0\), (1.2) follows. \(\square\)

Let \(\kappa=\psi|_Z\) and define the tracial state
\[
\tau=\kappa\circ T.
\tag{1.3}
\]
Both \(\tau\) and \(\psi\) take value \(1\) on every \(z_n\). They need not agree away from \(Z\). The normality of \(T\) is distinct from the normality of \(\kappa\); here \(\kappa\) is singular.

## 2. Balanced signs in a chosen abelian algebra

Put \(z_0=1\) and \(h_n=z_{n-1}-z_n\). Then
\[
h_nh_m=0\ (n\ne m),\qquad \sum_{n\geq1}h_n=1
\]
strongly. Each \(h_n\) is central.

Within \(h_nM\), recursively construct a nested dyadic partition
\[
\{p_{n,m,\alpha}:\alpha\in\{0,1\}^m\},\qquad m\geq0,
\]
with \(p_{n,0,\varnothing}=h_n\), such that every parent is the sum of its two children and
\[
T(p_{n,m,\alpha})=2^{-m}h_n.
\tag{2.1}
\]
To justify equal sizes at every level, halve one projection using Proposition 13.3, then transport its two halves to all projections equivalent to it. Equivalence preserves \(T\); halves of equal trace have equal trace. Iterating gives (2.1), including zero shells. Nested or disjoint projections commute.

For \(j\geq1\), define the \(j\)-th sign in the \(n\)-th shell by
\[
d_{n,j}=\sum_{\alpha\in\{0,1\}^j}(-1)^{\alpha_j}p_{n,j,\alpha}.
\]
These are self-adjoint, \(d_{n,j}^2=h_n\), and
\[
T(d_{n,j})=0,\qquad
T(d_{n,j}d_{n,k})=0\quad(j\ne k).
\tag{2.2}
\]
For the second equality, refine to level \(\max(j,k)\). Exactly half the strings give each sign for the product, and all corresponding projections have the same trace.

Let \(A\subseteq M\) be the abelian von Neumann algebra generated by \(Z\) and these partitions. Its compact spectrum \(Y\) is extremally disconnected: closures of open sets are open. We need this property below, but do not need \(A\) to be maximal abelian.

For a binary branch \(b=(b_1,b_2,\ldots)\), let
\[
j_n(b)=1+\sum_{i=1}^n b_i2^{n-i}.
\]
Distinct branches have distinct \(j_n\) for every sufficiently large \(n\). Define
\[
u_b=\sum_{n\geq1}d_{n,j_n(b)}\in A.
\tag{2.3}
\]
The sum converges strongly, since the supports are orthogonal and finite sums are contractions. It is a self-adjoint unitary: \(u_b^2=\sum_nh_n=1\).

**Lemma 2.1.** The functions \(u_b\), regarded in \(L^2(Y,\nu_\tau)\), form an orthonormal family of cardinality \(2^{\aleph_0}\), and each has pointwise modulus \(1\).

**Proof.** Here \(\nu_\tau\) is the probability Radon measure representing \(\tau|_A\). If \(b\ne c\), choose \(N\) such that \(j_n(b)\ne j_n(c)\) for \(n>N\). Normality of \(T\), applied to the bounded strong sums, and (2.2) give
\[
T(u_bu_c)=\sum_{n=1}^N T(d_{n,j_n(b)}d_{n,j_n(c)}).
\]
The right side is supported on \(1-z_N\). Since \(\kappa(1-z_N)=0\), its \(\kappa\)-value is zero. Thus \(\tau(u_bu_c)=0\). On the other hand \(\tau(u_b^2)=1\). A unitary in \(C(Y)\) has modulus \(1\) everywhere. \(\square\)

**Lemma 2.2.** If a finite measure space has an uncountable orthonormal family of functions of modulus \(1\), then \(L^2(K)\) is nonseparable for every measurable set \(K\) of positive measure.

**Proof.** Suppose \(L^2(K)\) had a countable dense set \((v_m)\), extended by zero to the whole space. By Bessel's inequality, each \(v_m\) has a nonzero inner product with at most countably many members of an orthonormal family. Outside the union of these countable sets, a member \(u\) would be orthogonal to every \(v_m\), hence to all of \(L^2(K)\). Its restriction to \(K\) would then be zero. But its squared norm there is the measure of \(K\), since \(|u|=1\). This is a contradiction. \(\square\)

This localization fact is useful: we built the balanced partitions before choosing \(K\), and it guarantees nonseparability on whatever positive-measure set occurs later.

## 3. The absolutely continuous case

Let \(\nu_\psi\) be the Radon probability measure on \(Y\) representing \(\psi|_A\). The map
\[
a\longmapsto\pi_\psi(a)\xi_\psi
\]
identifies the closure of this subspace of the GNS Hilbert space \(H_\psi\) with \(L^2(Y,\nu_\psi)\). Continuous functions are dense in this \(L^2\) space by regularity of the measure.

Suppose first that \(\nu_\psi\ll\nu_\tau\). Write \(d\nu_\psi=f\,d\nu_\tau\). Since \(\int f\,d\nu_\tau=1\), one of the sets
\[
K_m=\{y:1/m\leq f(y)\leq m\}
\]
has positive \(\nu_\tau\)-measure. On that set the two measures are equivalent, and multiplication by \(\sqrt f\) is a unitary
\[
L^2(K_m,\nu_\psi)\longrightarrow L^2(K_m,\nu_\tau).
\]
Lemma 2.2 makes the latter space nonseparable. Therefore \(H_\psi\) is nonseparable.

## 4. The case with a singular measure component

Suppose \(\nu_\psi\not\ll\nu_\tau\). A Borel set of zero \(\nu_\tau\)-measure has positive \(\nu_\psi\)-measure. By inner regularity choose a compact subset \(K\) with
\[
\nu_\tau(K)=0,\qquad a:=\nu_\psi(K)>0.
\tag{4.1}
\]

**Lemma 4.1.** There are decreasing projections \(f_n\in A\) satisfying
\[
f_n\longrightarrow0\ \text{strongly},\qquad
T(f_n)\leq4^{-n-2}1,\qquad
\psi(f_n)>a/2.
\tag{4.2}
\]

**Proof.** First choose decreasing clopen neighborhoods \(E_n\supseteq K\) with \(\nu_\tau(E_n)\to0\). Such neighborhoods exist by regularity and the clopen neighborhood basis of a compact extremally disconnected space: put a neighborhood with small measure around \(K\), choose finitely many clopen neighborhoods inside it to cover \(K\), then intersect with the preceding choice. Let \(e_n\in A\) be their projections.

Write \(Q\) for the spectrum of \(Z\) and also \(\kappa\) for the Radon measure representing that state. The decreasing continuous functions \(T(e_n)\) satisfy
\[
\int_Q T(e_n)\,d\kappa=\tau(e_n)=\nu_\tau(E_n)\longrightarrow0.
\]
Their pointwise limit is zero \(\kappa\)-almost everywhere. Fix \(0<\varepsilon<a/2\). Egoroff's theorem followed by inner regularity gives a compact \(F\subseteq Q\) with \(\kappa(F)>1-\varepsilon\) on which the convergence is uniform. Pass to a subsequence so that \(T(e_n)<4^{-n-2}\) on \(F\).

Let \(G_n=\{q:T(e_n)(q)<4^{-n-2}\}\). Its closure is clopen and still satisfies \(T(e_n)\leq4^{-n-2}\), by continuity. Let \(g_n\in Z\) correspond to \(\bigcap_{i=1}^n\overline{G_i}\). Then \(g_n\) decreases, \(\kappa(g_n)>1-\varepsilon\), and \(T(e_n)g_n\leq4^{-n-2}1\). Put \(f_n=e_ng_n\). Central bimodularity gives the trace bound. Since \(e_n\geq1_K\) as functions on \(Y\), and \(\psi(g_n)=\kappa(g_n)\),
\[
\psi(f_n)\geq\psi(e_n)-\psi(1-g_n)>a-\varepsilon>a/2.
\]
Finally the decreasing strong limit \(f\) has \(T(f)=0\), by normality and the trace bound. Faithfulness of \(T\) implies \(f=0\). \(\square\)

Although \(f_n\downarrow0\) in \(M\), the projections \(\pi_\psi(f_n)\) have a nonzero decreasing limit on \(H_\psi\). Indeed
\[
\|\pi_\psi(f_n)\xi_\psi\|^2=\psi(f_n)>a/2.
\]
The vectors converge to a nonzero vector \(\zeta\) with
\[
\pi_\psi(f_n)\zeta=\zeta\quad\text{for every }n.
\tag{4.3}
\]

Set \(k_n=f_n-f_{n+1}\). Then \(\sum_nk_n=f_1\) strongly and \(T(k_n)\leq4^{-n-2}1\).

**Lemma 4.2.** There are projections \(p_{n,j}\), \(1\leq j\leq2^n\), mutually orthogonal across all indices, such that
\[
p_{n,1}=k_n,\qquad p_{n,j}\sim k_n.
\tag{4.4}
\]
The projections chosen at step \(n\) are all orthogonal to \(f_{n+1}\).

**Proof.** Inductively suppose the projections at earlier steps are orthogonal to \(f_n\). The projection
\[
P_n=f_n+\sum_{i<n}\sum_{j=1}^{2^i}p_{i,j}
\]
then has trace bounded by
\[
T(P_n)\leq
\left(4^{-n-2}+\sum_{i<n}2^i4^{-i-2}\right)1
<\tfrac18\,1.
\tag{4.5}
\]
Keep \(p_{n,1}=k_n\), which lies inside \(f_n\). Choose the other \(2^n-1\) copies successively in \(1-P_n\). After fewer than \(2^n-1\) copies, the remaining projection has trace at least
\[
\left(\tfrac78-(2^n-2)4^{-n-2}\right)1>\tfrac34\,1.
\]
This is greater than \(T(k_n)\). Comparison (0.1) therefore supplies another equivalent copy. Each new copy is outside \(f_n\) and all earlier ranges. The initial copy \(k_n\) is orthogonal to \(f_{n+1}\), and all other copies are outside \(f_n\geq f_{n+1}\), maintaining the induction. Zero \(k_n\) cause no difficulty: use zero copies. \(\square\)

Choose partial isometries \(v_{n,j}\) with
\[
v_{n,j}^*v_{n,j}=k_n,\qquad v_{n,j}v_{n,j}^*=p_{n,j}.
\]
For the branch indices \(j_n(b)\) of Section 2, which lie between \(1\) and \(2^n\), put
\[
w_b=\sum_{n\geq1}v_{n,j_n(b)}.
\tag{4.6}
\]
This sum converges strongly: initial projections \(k_n\) are orthogonal, final projections are orthogonal, and the squared norm of a tail applied to a vector is \(\sum\|k_n\xi\|^2\). The adjoints converge strongly as well by the orthogonality of the final projections. Thus
\[
w_b^*w_b=f_1.
\]
For distinct branches \(b,c\), choose \(N\) after their indices have become different. Distinct final projections give \(v_{n,j_n(b)}^*v_{m,j_m(c)}=0\), except when \(n=m\) and the indices agree. Consequently
\[
f_Nw_b^*w_cf_N=0.
\tag{4.7}
\]
Using (4.3) and (4.7), the vectors \(\pi_\psi(w_b)\zeta\) are mutually orthogonal and all have norm \(\|\zeta\|>0\). There are \(2^{\aleph_0}\) of them. Hence \(H_\psi\) is again nonseparable.

## 5. Automatic normality

**Theorem 5.1.** Every representation of a sigma-finite finite type II von Neumann algebra on a separable Hilbert space is normal.

**Proof.** Restrict a degenerate representation to its support. Split the remaining representation into its normal and singular parts. The singular part acts on a separable reducing subspace. If it is nonzero, call it \(\rho\), and let \(N=\rho(M)''\).

Any von Neumann algebra on a separable Hilbert space has a faithful normal state: take a positive summable weighted sum of vector states from a total sequence. Choose such an \(\omega\) for \(N\) and put \(\psi=\omega\rho\). Lemma 1.1 gives the central projections needed in Sections 2–4. Those sections prove that \(H_\psi\) is nonseparable in either measure case.

On the other hand \(H_\psi\) is separable. To see this explicitly, a normal positive functional on a concrete von Neumann algebra has the vector decomposition
\[
\omega(x)=\sum_{\ell\geq1}\langle x\eta_\ell,\eta_\ell\rangle,
\qquad \sum_\ell\|\eta_\ell\|^2<\infty,
\]
by Theorem 10.1 of [The double commutation theorem](../../foundations-of-von-neumann-algebras/the-double-commutant-theorem.html). The map
\[
\rho(a)\xi_\omega\longmapsto(\rho(a)\eta_\ell)_\ell
\]
is an isometry of the cyclic subspace generated by \(\rho(M)\) into the countable Hilbert sum of its separable representation space. Equivalently \(a\xi_\psi\mapsto(\rho(a)\eta_\ell)_\ell\) directly embeds \(H_\psi\) there. This contradiction makes the singular part zero. \(\square\)

**Corollary 5.2.** Let \(M\) be sigma-finite and have no nonzero finite type I central summand. Every representation of \(M\) on a separable Hilbert space is normal.

**Proof.** The type decomposition expresses \(M\) as the sum of a finite type II central summand and a properly infinite central summand. Both are sigma-finite. Their images act on orthogonal reducing subspaces. Apply Theorem 5.1 to the former and Theorem 2.1 of [Proper infiniteness and automatic normality](../reader/proper-infiniteness-and-automatic-normality.html) to the latter. A finite direct sum of normal maps is normal. \(\square\)

The exclusion of finite type I summands is necessary. For example a free ultrafilter on \(\mathbb N\) gives a singular character of \(\ell^\infty(\mathbb N)\), hence a representation on a one-dimensional space. The coordinate projections are all killed although their strong sum is \(1\).

For a finite type II factor there is a shorter proof: it is simple as a C*-algebra by central averaging, whereas a singular representation would have a nonzero projection in its kernel. The work above handles a nontrivial centre, where this simple-algebra argument no longer applies.

## 6. Exercises with solutions

**Exercise 6.1 — Basic: normality and an ultrafilter.** Let \(\chi\) be a free-ultrafilter character on \(\ell^\infty(\mathbb N)\). Let \(z_n\) be the characteristic function of \(\{n+1,n+2,\ldots\}\). Compute \(\chi(z_n)\) and the strong limit of \(z_n\) in the standard representation on \(\ell^2(\mathbb N)\). Why does this not contradict Theorem 5.1?

**Solution.** Every cofinite set belongs to the ultrafilter, so \(\chi(z_n)=1\). For \(\xi\in\ell^2\), \(\|z_n\xi\|^2=\sum_{j>n}|\xi_j|^2\to0\), so \(z_n\to0\) strongly. The character therefore fails normality. The domain is abelian, hence of finite type I, and does not satisfy the type II hypothesis.

**Exercise 6.2 — Intermediate: four equal pieces.** Suppose a projection \(h\) has four mutually equivalent orthogonal pieces \(p_{00},p_{01},p_{10},p_{11}\) summing to \(h\). Set
\[
d_1=p_{00}+p_{01}-p_{10}-p_{11},\qquad
d_2=p_{00}-p_{01}+p_{10}-p_{11}.
\]
Compute their squares, product and centre-valued traces. If \(h\) is central, what is \(T(p_{\alpha})\)?

**Solution.** Orthogonality gives \(d_1^2=d_2^2=h\) and
\[
d_1d_2=p_{00}-p_{01}-p_{10}+p_{11}.
\]
Equivalence gives a common trace \(t\) for the four pieces, so \(4t=T(h)\), and all three displayed sign combinations have trace zero. For central \(h\), \(T(h)=h\), hence \(T(p_\alpha)=h/4\). This is exactly the two-bit computation underlying (2.2).

**Exercise 6.3 — Advanced: a trace bound for many copies.** Let \(f_n\) be decreasing projections with strong limit zero and \(T(f_n)\leq16^{-n}1\). Prove that \(k_n=f_n-f_{n+1}\) can have \(4^n\) mutually orthogonal equivalent copies at step \(n\), all steps mutually orthogonal, with one copy equal to \(k_n\). Use these copies to produce continuum many equal-norm orthogonal vectors in every representation having a nonzero vector \(\zeta\) fixed by all \(f_n\).

**Solution.** At step \(n\), the earlier ranges and \(f_n\) have trace at most
\[
\sum_{i<n}4^i16^{-i}+16^{-n}
<\sum_{i\geq1}4^{-i}+16^{-1}
=\tfrac13+\tfrac1{16}<\tfrac12.
\]
Keep the initial copy \(k_n\) inside \(f_n\). Even after placing the other \(4^n-1\) copies outside this union, their total additional trace is at most \(4^n16^{-n}=4^{-n}\leq1/4\). Before each placement the remaining space consequently has trace greater than \(1/4\), whereas \(T(k_n)\leq1/16\). Comparison supplies every copy, and the induction keeps earlier copies orthogonal to later \(f_n\).

For a branch \(b\in\{0,1\}^{\mathbb N}\), use the index \(j_n(b)=1+\sum_{i=1}^n b_i2^{n-i}\leq2^n\leq4^n\). Sum partial isometries from \(k_n\) to the indexed ranges strongly, obtaining \(w_b\) with \(w_b^*w_b=f_1\). Distinct branches eventually have distinct indices, so \(f_Nw_b^*w_cf_N=0\) for sufficiently large \(N\). In a representation \(\pi\) with \(\pi(f_N)\zeta=\zeta\),
\[
\|\pi(w_b)\zeta\|=\|\zeta\|,\qquad
\langle\pi(w_b)\zeta,\pi(w_c)\zeta\rangle=0\quad(b\ne c).
\]
The strong sums are taken in \(M\); the representation is used only after these elements and their algebraic identities have been formed. No normality of \(\pi\) is assumed.

## References

[Takesaki] M. Takesaki, *Theory of Operator Algebras I*, Springer.

[Blackadar] B. Blackadar, *Operator Algebras*, [free author-hosted PDF](https://bruceblackadar.com/Mathematics/Cycr.pdf).
