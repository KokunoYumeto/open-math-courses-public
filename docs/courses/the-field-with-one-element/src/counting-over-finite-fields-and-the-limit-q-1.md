# Counting over finite fields and the limit q → 1

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October revision links the AI Integrated Stacks Project citations and is self-checked by the writing AI. The October revision also corrects points found by GPT-6 Astra (OpenAI), Ultra, in a separate review session. Public domain (CC0).*

## Introduction

Let \(\mathbb F_q\) be the field with \(q\) elements. Count the points of a projective space over \(\mathbb F_q\), the
subspaces of a given dimension of \(\mathbb F_q^n\), the flags, or the invertible matrices. Each answer is a
polynomial in \(q\). Now put \(q=1\) in the polynomial. For the group of invertible matrices, first divide by
\((q-1)^n\). The result is again a count: of the elements of a set with \(n\) elements, of its subsets, of its chains
of subsets, of its permutations.

No field has one element, because \(0\neq 1\) in a field. So the numbers at \(q=1\) are not counts over a field. But
the pattern is exact. It is also not special to the general linear group: for a Chevalley group scheme \(G\) of
rank \(r\) with Weyl group \(W\), the order of \(G(\mathbb F_q)\) behaves like \((q-1)^r\,|W|\) as \(q\) tends to
\(1\) [Soulé 1999, §1]. As [Soulé 1999, §1] recounts, Tits proposed to read the pattern as geometry over a
"field of characteristic one", with \(W\) as the group of points of \(G\) over that field. Many definitions of such
a geometry have been given since then, and this course studies them. This first lesson proves the facts that all
of them set out to explain, and it turns the facts into a list of requirements.

The lesson does five things.

1. **Counting.** Sections 2 and 3 introduce the Gaussian binomial coefficients \(\binom{n}{k}_q\) and prove the
   formulas for the order of \(\mathrm{GL}_n(\mathbb F_q)\) and for the numbers of subspaces and of flags
   (Theorems 3.2, 3.3 and 3.5).
2. **Why the value at \(q=1\) counts subsets and permutations.** The sets that we count are disjoint unions of
   cells, and a cell has \(q^d\) points. Theorem 4.2 gives, for every field \(F\), a map from the \(k\)-dimensional
   subspaces of \(F^n\) onto the subsets of \(\{1,\dots,n\}\) with \(k\) elements. Its fibres are affine spaces, and
   they are the orbits of the group of upper triangular matrices. Theorem 5.4 is the Bruhat decomposition of
   \(\mathrm{GL}_n(F)\), with a unique normal form for every matrix; its cells are indexed by the permutations.
   Section 6 collects the values at \(q=1\) (Theorem 6.2) and states the formula for a general Chevalley group.
3. **Tits's proposal.** Section 7 defines the geometry of a finite set and shows in what sense it is projective
   geometry over a field with one element: its incidence numbers are the values at \(q=1\) (Theorem 7.2), its lines
   have two points (Proposition 7.3), its automorphism group is the symmetric group (Theorem 7.4), and for every
   field it is both a part and a quotient of the projective geometry over that field (Theorem 7.5).
4. **The extensions \(\mathbb F_{1^n}\).** Section 8 treats \(\mathbb F_{1^n}=\{0\}\cup\mu_n\) and linear algebra
   over it: a vector space is a pointed set on which the group \(\mu_n\) of roots of unity acts freely away from the
   base point, and its automorphism group is a wreath product (Theorem 8.4). For \(n=q-1\) this group is the group
   of monomial matrices over \(\mathbb F_q\) (Corollary 8.6). Propositions 8.7 and 8.8 explain why Tits, [Connes–Consani 2011a] and [Soulé 2004] count the points of projective space over \(\mathbb F_1\) in three
   different ways.
5. **Requirements.** Section 9 states what a geometry over \(\mathbb F_1\) is asked to provide, as nine
   requirements (R1)–(R9). Later lessons of the course can be tested against them.

*What is assumed.* Core algebra: groups and group actions, finite fields, and linear algebra over a field. The
facts used are listed in Section 1. The proofs use no scheme theory. Where a scheme is mentioned, it is only to say
which set of points is being counted, and the reference is [Stacks].

Basic references are [Soulé 1999], [Soulé 2004], [Connes–Consani 2011a], [López Peña–Lorscheid 2011a] and
[Lorscheid 2018b]; the ideas about zeta functions and K-theory in Section 9 come from [Manin 1995]. The proposal itself is in no. 13 of a 1957 paper of Tits, whose beginning is reproduced in [Lorscheid–Thas 2023]. Section 7 reports the proposal and how these references describe it.

## 1. Conventions and background

Rings are commutative with \(1\). The letter \(q\) is a prime power when it appears in \(\mathbb F_q\), and an
indeterminate when we speak of polynomials in \(q\). For \(n\ge 0\) put \(\Omega_n=\{1,\dots,n\}\). The number of
elements of a finite set \(X\) is \(|X|\).

Let \(F\) be a field. The elements of \(F^n\) are column vectors, \(e_1,\dots,e_n\) is the standard basis, and
\[
E_j=\operatorname{span}(e_1,\dots,e_j)\quad(0\le j\le n),\qquad
E_S=\operatorname{span}(e_s: s\in S)\quad(S\subseteq\Omega_n).
\]
The group \(\mathrm{GL}_n(F)\) of invertible \(n\times n\) matrices acts on \(F^n\) from the left. We use these
subgroups:

- \(T\), the diagonal matrices (the *diagonal torus*);
- \(B\), the upper triangular matrices;
- \(U\), the upper triangular matrices with \(1\) on the diagonal;
- \(U^-\), the lower triangular matrices with \(1\) on the diagonal.

Every \(b\in B\) is \(b=tu\) with unique \(t\in T\) and \(u\in U\), and \(B\cap U^-=\{1\}\).

If \(X\) assigns a finite set \(X(\mathbb F_q)\) to every prime power \(q\), we write \(N_X(q)=|X(\mathbb F_q)|\).

We use the following facts.

- **(B1) Finite fields.** For every prime power \(q\) there is a field \(\mathbb F_q\) with \(q\) elements. It is
  unique up to isomorphism. The multiplicative group of a finite field with \(q\) elements is cyclic of order
  \(q-1\) [Stacks, Tags [09HW](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-section-roots-of-1) and [09HY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-section-finite)].
- **(B2) Linear algebra** over a field: bases, dimension, quotient spaces, the formula
  \(\dim(U+W)+\dim(U\cap W)=\dim U+\dim W\), and the fact that the determinant of a block triangular matrix is the
  product of the determinants of its diagonal blocks.
- **(B3) Orbits.** If a finite group \(G\) acts on a set and \(x\) is a point of the set, then
  \(|G|=|G\cdot x|\cdot|G_x|\), where \(G_x\) is the stabilizer of \(x\).
- **(B4) Polynomial identities.** Two polynomials with rational coefficients that take the same value at infinitely
  many integers are equal. There are infinitely many prime powers. So an identity between polynomials in \(q\) holds
  as soon as it holds for every prime power \(q\).

## 2. Gaussian binomial coefficients

**Definition 2.1.** For an integer \(n\ge 0\) put
\[
[n]_q=1+q+\dots+q^{n-1}\in\mathbb Z[q],\qquad [n]_q!=[1]_q[2]_q\cdots[n]_q ,
\]
with \([0]_q=0\) and \([0]_q!=1\). For integers \(0\le k\le n\) the *Gaussian binomial coefficient* is
\[
\binom{n}{k}_q=\frac{[n]_q!}{[k]_q!\,[n-k]_q!}\in\mathbb Q(q).
\]
For \(k<0\) or \(k>n\) we put \(\binom{n}{k}_q=0\).

Two identities are used all the time: \((q-1)[n]_q=q^n-1\), and \([n]_q=[k]_q+q^k[n-k]_q\) for \(0\le k\le n\).

**Lemma 2.2 (Pascal rules).** For \(n\ge 1\) and \(0\le k\le n\),
\[
\binom{n}{k}_q=\binom{n-1}{k-1}_q+q^{k}\binom{n-1}{k}_q
=q^{n-k}\binom{n-1}{k-1}_q+\binom{n-1}{k}_q .
\]

*Proof.* For \(k=0\) and for \(k=n\) all three expressions are equal to \(1\). Let \(1\le k\le n-1\). By the
definition,
\[
\binom{n-1}{k-1}_q=\frac{[k]_q}{[n]_q}\binom{n}{k}_q,\qquad
\binom{n-1}{k}_q=\frac{[n-k]_q}{[n]_q}\binom{n}{k}_q .
\]
So the first sum is \(\binom{n}{k}_q\,([k]_q+q^k[n-k]_q)/[n]_q=\binom{n}{k}_q\). The second sum is
\(\binom{n}{k}_q\,(q^{n-k}[k]_q+[n-k]_q)/[n]_q\), and \([n]_q=[n-k]_q+q^{n-k}[k]_q\). ∎

**Proposition 2.3.** Let \(0\le k\le n\).

- (a) \(\binom{n}{k}_q\) is a polynomial in \(q\) with non-negative integer coefficients.
- (b) Its degree is \(k(n-k)\), its leading coefficient is \(1\), and its constant term is \(1\).
- (c) \(\binom{n}{k}_q=\binom{n}{n-k}_q\).
- (d) Its value at \(q=1\) is the binomial coefficient \(\binom{n}{k}\).

*Proof.* (c) is clear from the definition. For the rest use induction on \(n\). If \(k=0\) or \(k=n\) the
coefficient is \(1\); this covers \(n=0\). Let \(1\le k\le n-1\) and use the first Pascal rule. By induction both
terms on its right side are polynomials with non-negative integer coefficients. This gives (a). The term
\(q^k\binom{n-1}{k}_q\) has degree \(k+k(n-1-k)=k(n-k)\) and leading coefficient \(1\), and the term
\(\binom{n-1}{k-1}_q\) has the smaller degree \((k-1)(n-k)\). The constant term comes from \(\binom{n-1}{k-1}_q\)
alone, because \(k\ge 1\). This gives (b). At \(q=1\) the rule becomes
\(\binom{n}{k}=\binom{n-1}{k-1}+\binom{n-1}{k}\), with the same boundary values. This gives (d). ∎

**Example 2.4.** We have \(\binom{n}{0}_q=\binom{n}{n}_q=1\) and \(\binom{n}{1}_q=[n]_q\). For \(n=4\) and \(k=2\),
\[
\binom{4}{2}_q=\frac{[4]_q[3]_q}{[2]_q}=(1+q^2)(1+q+q^2)=1+q+2q^2+q^3+q^4 .
\]
The value at \(q=1\) is \(6=\binom{4}{2}\). The polynomial \([6]_q=1+q+\dots+q^5\) also has the value \(6\) at
\(q=1\). So the value at \(q=1\) does not determine the polynomial. The polynomial is the finer invariant.

## 3. Counting over a finite field

In this section \(q\) is a prime power.

**Proposition 3.1.** Let \(V\) be a vector space of dimension \(n\) over \(\mathbb F_q\) and let \(0\le k\le n\).
The number of linearly independent \(k\)-tuples \((v_1,\dots,v_k)\) in \(V\) is \(\prod_{i=0}^{k-1}(q^n-q^i)\).

*Proof.* Choose the vectors one after the other. When \(v_1,\dots,v_i\) are chosen and independent, their span has
\(q^i\) elements, and \(v_{i+1}\) can be any of the \(q^n-q^i\) vectors outside this span. ∎

**Theorem 3.2 (order of the general linear group).** For \(n\ge 0\),
\[
|\mathrm{GL}_n(\mathbb F_q)|=\prod_{i=0}^{n-1}(q^n-q^i)=(q-1)^n\,q^{\binom{n}{2}}\,[n]_q! .
\]

*Proof.* A matrix is invertible exactly when its columns form a basis of \(\mathbb F_q^n\). So the order is the
number of linearly independent \(n\)-tuples, which is \(\prod_{i=0}^{n-1}(q^n-q^i)\) by Proposition 3.1. Now
\(q^n-q^i=q^i(q-1)[n-i]_q\), and \(0+1+\dots+(n-1)=\binom{n}{2}\). ∎

**Theorem 3.3 (subspaces).** Let \(V\) be a vector space of dimension \(n\) over \(\mathbb F_q\) and \(0\le k\le n\).
The number of subspaces of \(V\) of dimension \(k\) is \(\binom{n}{k}_q\).

*Proof.* Send a linearly independent \(k\)-tuple to its span. This map is onto the set of \(k\)-dimensional
subspaces, and the fibre over a subspace \(W\) is the set of ordered bases of \(W\). By Proposition 3.1 there are
\(\prod_{i<k}(q^n-q^i)\) tuples, and every fibre has \(\prod_{i<k}(q^k-q^i)\) elements. The quotient is
\[
\prod_{i=0}^{k-1}\frac{q^{n-i}-1}{q^{k-i}-1}=\prod_{i=0}^{k-1}\frac{[n-i]_q}{[k-i]_q}
=\frac{[n]_q!}{[n-k]_q!\,[k]_q!} ,
\]
which is \(\binom{n}{k}_q\). ∎

**Corollary 3.4.**

- (a) The projective space \(\mathbb P^{n-1}(\mathbb F_q)\), the set of one-dimensional subspaces of
  \(\mathbb F_q^n\), has \([n]_q=1+q+\dots+q^{n-1}\) elements. The set of hyperplanes of \(\mathbb F_q^n\) has the
  same number of elements.
- (b) Let \(U\subseteq W\) be subspaces of \(\mathbb F_q^n\) with \(\dim U=i\) and \(\dim W=j\), and let
  \(i\le m\le j\). The number of subspaces \(X\) with \(U\subseteq X\subseteq W\) and \(\dim X=m\) is
  \(\binom{j-i}{m-i}_q\).

*Reference:* [Soulé 2004, Introduction] names \(\mathbb P^N\) as the projective space whose points over
\(\mathbb F_1\) are the \(N\) letters permuted by the symmetric group; since \(\mathbb P^N\) has \([N+1]_q\) points,
the space with \(N\) points at \(q=1\) is \(\mathbb P^{N-1}\).

*Proof.* (a) is Theorem 3.3 for \(k=1\) and \(k=n-1\), with \(\binom{n}{n-1}_q=\binom{n}{1}_q=[n]_q\). (b) The map
\(X\mapsto X/U\) is a bijection from the subspaces between \(U\) and \(W\) to the subspaces of \(W/U\). It lowers
dimensions by \(i\), and \(\dim W/U=j-i\). Apply Theorem 3.3 to \(W/U\). ∎

**Theorem 3.5 (flags).** Let \(n_1,\dots,n_r\) be positive integers with sum \(n\), and put \(m_i=n_1+\dots+n_i\). A
*flag of type \((n_1,\dots,n_r)\)* in an \(n\)-dimensional vector space \(V\) is a chain of subspaces
\(0=V_0\subset V_1\subset\dots\subset V_r=V\) with \(\dim V_i=m_i\). A *complete flag* is a flag of type
\((1,\dots,1)\). The number of flags of type \((n_1,\dots,n_r)\) in \(\mathbb F_q^n\) is
\[
\frac{[n]_q!}{[n_1]_q!\,[n_2]_q!\cdots[n_r]_q!} .
\]
In particular there are \([n]_q!\) complete flags.

*Proof.* Induction on \(r\). For \(r=1\) there is one flag and the formula gives \(1\). Let \(r\ge 2\). There are
\(\binom{n}{n_1}_q\) choices for \(V_1\). For a fixed \(V_1\), the map \(V_i\mapsto V_i/V_1\) \((i\ge 1)\) is a
bijection from the flags of type \((n_1,\dots,n_r)\) with this first member to the flags of type
\((n_2,\dots,n_r)\) in \(V/V_1\), a space of dimension \(n-n_1\). By induction their number is
\([n-n_1]_q!/([n_2]_q!\cdots[n_r]_q!)\). The product with \(\binom{n}{n_1}_q=[n]_q!/([n_1]_q![n-n_1]_q!)\) is the
formula. ∎

The same definition applies to sets. A *flag of type \((n_1,\dots,n_r)\)* in a set \(\Omega\) with \(n\) elements is a
chain of subsets \(\emptyset=A_0\subset A_1\subset\dots\subset A_r=\Omega\) with \(|A_i|=m_i\). The group of
permutations of \(\Omega\) acts transitively on these flags. For \(\Omega=\Omega_n\) the stabilizer of the flag with
\(A_i=\Omega_{m_i}\) is \(S_{n_1}\times\dots\times S_{n_r}\), the permutations that preserve each block
\(\{m_{i-1}+1,\dots,m_i\}\) (with \(m_0=0\)). By (B3) there are \(n!/(n_1!\cdots n_r!)\) flags of subsets of this
type. A complete
flag of subsets of \(\Omega_n\) is the same as a permutation \(w\): take \(A_i=\{w(1),\dots,w(i)\}\).

**Proposition 3.6 (the stabilizer of a flag).** Let \(n_1,\dots,n_r\) and \(m_i\) be as in Theorem 3.5, and let
\(P=P_{(n_1,\dots,n_r)}\) be the set of \(g\in\mathrm{GL}_n(\mathbb F_q)\) with \(gE_{m_i}=E_{m_i}\) for all \(i\).

- (a) \(P\) is the group of invertible block upper triangular matrices with diagonal blocks of sizes
  \(n_1,\dots,n_r\).
- (b) \(|P|=\prod_{i}|\mathrm{GL}_{n_i}(\mathbb F_q)|\cdot q^{\sum_{i<j}n_in_j}
  =(q-1)^n\,q^{\binom{n}{2}}\,[n_1]_q!\cdots[n_r]_q!\).
- (c) \(\mathrm{GL}_n(\mathbb F_q)\) acts transitively on the flags of type \((n_1,\dots,n_r)\), and \(P\) is the
  stabilizer of the flag \((E_{m_i})_i\).

Special cases: \(B=P_{(1,\dots,1)}\) has \((q-1)^n q^{\binom{n}{2}}\) elements, and for \(0<k<n\) the group
\(P_k:=P_{(k,n-k)}\), the stabilizer of \(E_k\), has \((q-1)^n q^{\binom{n}{2}}[k]_q![n-k]_q!\) elements. The torus
\(T\) has \((q-1)^n\) elements.

*Proof.* (a) For an invertible \(g\), the condition \(gE_m=E_m\) holds exactly when the first \(m\) columns of \(g\)
lie in \(E_m\), that is, when \(g_{ab}=0\) for \(a>m\ge b\). (b) By (B2) a block upper triangular matrix is
invertible exactly when its diagonal blocks are. The entries above the diagonal blocks are arbitrary, and there are
\(\sum_{i<j}n_in_j\) of them. Now use Theorem 3.2 for each block and the identity
\(\binom{n}{2}=\sum_i\binom{n_i}{2}+\sum_{i<j}n_in_j\). (c) Given a flag \((V_i)\), choose a basis
\(v_1,\dots,v_n\) of \(\mathbb F_q^n\) such that \(v_1,\dots,v_{m_i}\) is a basis of \(V_i\) for every \(i\). The
matrix with columns \(v_1,\dots,v_n\) sends \(E_{m_i}\) to \(V_i\). The stabilizer of \((E_{m_i})_i\) is \(P\) by
definition. ∎

By (B3), parts (b) and (c) and Theorem 3.2 give a second proof of Theorem 3.5:
\(|\mathrm{GL}_n(\mathbb F_q)|/|P|=[n]_q!/([n_1]_q!\cdots[n_r]_q!)\).

**Example 3.7 (small cases and edge cases).**

- For \(n=0\) the group \(\mathrm{GL}_0\) is trivial, and the empty product in Theorem 3.2 is \(1\).
- For \(n=1\), \(\mathrm{GL}_1(\mathbb F_q)=\mathbb F_q^\times\) has \(q-1\) elements.
- \(|\mathrm{GL}_2(\mathbb F_q)|=(q^2-1)(q^2-q)=(q-1)^2q(q+1)\). For \(q=2\) this is \(6\), for \(q=3\) it is \(48\).
- For \(q=2\) the factor \((q-1)^n\) is \(1\): the torus \(T\) is trivial. For example
  \(|\mathrm{GL}_3(\mathbb F_2)|=2^3\cdot[3]_2!=8\cdot 1\cdot 3\cdot 7=168\).
- \(\mathbb F_q^3\) has \([3]_q!=(1+q)(1+q+q^2)\) complete flags. For \(q=2\) this is \(21\): there are \(7\) points of
  \(\mathbb P^2(\mathbb F_2)\), and each lies on \(3\) lines.

**Remark (the schemes behind the counts).** Projective space and the Grassmannians are schemes over \(\mathbb Z\)
([Stacks, Tag [01ND](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/constructions.html#constructions-section-projective-space)], [Stacks, Tag [089R](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/constructions.html#constructions-section-grassmannian)]), and the sets counted above are their sets of points with values in
\(\mathbb F_q\). A point of a projective space or of a Grassmannian with values in a field \(F\) is a quotient of
\(F^n\) of a fixed dimension, or, by taking kernels, a subspace of the complementary dimension. By
Proposition 2.3(c) the count is the same in both descriptions. Nothing below depends on the scheme structure.

## 4. Subsets for subspaces: the cells of a Grassmannian

By Proposition 2.3(d), the polynomial \(\binom{n}{k}_q\) that counts subspaces has the value \(\binom{n}{k}\) at
\(q=1\), the number of subsets with \(k\) elements. This section explains the fact by a map from subspaces to
subsets. The map exists over every field.

**Definition 4.1.** Let \(F\) be a field. For a non-zero vector \(v\in F^n\) the *height* \(\operatorname{ht}(v)\) is
the largest index \(i\) with \(v_i\ne 0\). So \(v\in E_j\) exactly when \(\operatorname{ht}(v)\le j\). For a subspace
\(V\subseteq F^n\) the *jump set* is
\[
J(V)=\{\operatorname{ht}(v): v\in V,\ v\ne 0\}\subseteq\Omega_n .
\]
For a subset \(S=\{s_1<\dots<s_k\}\) of \(\Omega_n\) put
\[
D(S)=\{(j,s): s\in S,\ j\in\Omega_n\setminus S,\ j<s\},\qquad d(S)=|D(S)|=\sum_{i=1}^{k}(s_i-i).
\]
The formula for \(d(S)\) holds because exactly \(s_i-i\) of the numbers below \(s_i\) are not in \(S\).

**Theorem 4.2 (cells of the Grassmannian).** Let \(F\) be a field and \(0\le k\le n\).

- (a) \(|J(V)|=\dim V\) for every subspace \(V\subseteq F^n\).
- (b) Let \(S\subseteq\Omega_n\) have \(k\) elements and let \(C_S(F)\) be the set of subspaces \(V\) with
  \(J(V)=S\). Every \(V\in C_S(F)\) has a unique basis \((v^{(s)})_{s\in S}\) such that \(v^{(s)}_s=1\) and
  \(v^{(s)}_t=0\) for \(t\in S\setminus\{s\}\). It satisfies \(\operatorname{ht}(v^{(s)})=s\). The map
  \[
  C_S(F)\to F^{D(S)},\qquad V\mapsto\big(v^{(s)}_j\big)_{(j,s)\in D(S)}
  \]
  is a bijection.
- (c) \(J(bV)=J(V)\) for all \(b\in B\). Each \(C_S(F)\) is a single orbit of \(U\), and a single orbit of \(B\):
  \(C_S(F)=U\cdot E_S=B\cdot E_S\). The coordinate subspace \(E_S\) is the only coordinate subspace in \(C_S(F)\).
- (d) If \(F=\mathbb F_q\), then \(|C_S(\mathbb F_q)|=q^{d(S)}\).

*Proof.* (a) Put \(V_j=V\cap E_j\) for \(0\le j\le n\), so \(V_0=0\) and \(V_n=V\). The linear map \(V_j\to F\),
\(v\mapsto v_j\), has kernel \(V_{j-1}\). So \(\dim V_j-\dim V_{j-1}\) is \(0\) or \(1\), and it is \(1\) exactly when
some \(v\in V_j\) has \(v_j\ne 0\), that is, when \(j\in J(V)\). Summing over \(j\) gives \(\dim V=|J(V)|\).

(b) Let \(V\in C_S(F)\); then \(\dim V=k\) by (a). The projection \(\pi\colon V\to F^S\), \(v\mapsto(v_t)_{t\in S}\),
is injective: a non-zero \(v\in V\) has \(\operatorname{ht}(v)\in S\), and its coordinate at that index is not zero.
Since \(\dim V=k=\dim F^S\), \(\pi\) is bijective. The two conditions on \(v^{(s)}\) say that \(\pi(v^{(s)})\) is the
standard basis vector of \(F^S\) with index \(s\). So the basis exists and is unique. The height of \(v^{(s)}\) lies
in \(S\), and the only non-zero coordinate of \(v^{(s)}\) with index in \(S\) is the one at \(s\). Hence
\(\operatorname{ht}(v^{(s)})=s\), and
\[
v^{(s)}=e_s+\sum_{(j,s)\in D(S)}a_{j,s}\,e_j ,\qquad a_{j,s}=v^{(s)}_j .
\]
The map in (b) is injective, because \(V\) is spanned by the \(v^{(s)}\). It is surjective: given
\(a\in F^{D(S)}\), define \(v^{(s)}\) by the displayed formula and let \(V\) be their span. The coordinates of
\(v^{(s)}\) with index in \(S\) form a standard basis vector, so the \(v^{(s)}\) are independent and \(\dim V=k\).
Let \(v=\sum_s c_sv^{(s)}\ne 0\) and let \(s_0\) be the largest \(s\) with \(c_s\ne 0\). Every \(v^{(s)}\) with
\(c_s\ne0\) lies in \(E_s\subseteq E_{s_0}\), and the coordinate of \(v\) at \(s_0\) is \(c_{s_0}\). So
\(\operatorname{ht}(v)=s_0\in S\). Thus \(J(V)\subseteq S\), and \(J(V)=S\) by (a). By uniqueness the \(v^{(s)}\) are
the basis attached to \(V\), so \(V\) is mapped to \(a\).

(c) Let \(b\in B\) and \(v\ne 0\) with \(h=\operatorname{ht}(v)\). Then \((bv)_i=\sum_{j\ge i}b_{ij}v_j\). This is
\(0\) for \(i>h\) and equal to \(b_{hh}v_h\ne 0\) for \(i=h\). So \(\operatorname{ht}(bv)=\operatorname{ht}(v)\), and
\(J(bV)=J(V)\). The non-zero vectors of \(E_S\) have heights in \(S\), so \(J(E_S)\subseteq S\), and \(J(E_S)=S\) by
(a). In particular \(E_{S'}\in C_S(F)\) only for \(S'=S\). Now let \(V\in C_S(F)\) with basis \((v^{(s)})\) as in
(b). Define a matrix \(u\) by \(ue_s=v^{(s)}\) for \(s\in S\) and \(ue_j=e_j\) for \(j\notin S\). Column \(s\) of
\(u\) lies in \(E_s\) and has the entry \(1\) in row \(s\). So \(u\in U\), and \(uE_S=V\). Hence
\(C_S(F)\subseteq U\cdot E_S\subseteq B\cdot E_S\subseteq C_S(F)\).

(d) follows from (b). ∎

The decomposition of the set of \(k\)-dimensional subspaces into the sets \(C_S(F)\) is the Schubert cell
decomposition mentioned in [López Peña–Lorscheid 2011a, §1.7].

**Corollary 4.3.** For \(0\le k\le n\),
\[
\binom{n}{k}_q=\sum_{S\subseteq\Omega_n,\ |S|=k}q^{d(S)}
=\sum_{1\le s_1<\dots<s_k\le n}q^{(s_1-1)+(s_2-2)+\dots+(s_k-k)}
\]
as polynomials in \(q\). Each subset contributes one monomial. At \(q=1\) each subset contributes \(1\).

*Proof.* For a prime power \(q\), the sets \(C_S(\mathbb F_q)\) with \(|S|=k\) form a partition of the set of
\(k\)-dimensional subspaces of \(\mathbb F_q^n\), by Theorem 4.2(a). Count with Theorems 3.3 and 4.2(d), and use
(B4). ∎

So the passage from \(q\) to \(1\) is not a limit of sets. It is a map \(V\mapsto J(V)\), defined over every field,
whose fibres are affine spaces. Putting \(q=1\) counts the fibres.

**Proposition 4.4 (subspaces stable under the torus).** Let \(F\) be a field with \(|F|\ge 3\). A subspace
\(V\subseteq F^n\) satisfies \(tV\subseteq V\) for all \(t\in T\) if and only if \(V=E_S\) for some
\(S\subseteq\Omega_n\). If \(|F|=2\), then \(T=\{1\}\) and every subspace is stable.

*Proof.* Coordinate subspaces are stable. Conversely let \(V\) be stable, let \(v\in V\) and \(i\in\Omega_n\). Since
\(|F|\ge 3\) there is \(c\in F\) with \(c\ne 0,1\). Let \(t\in T\) have the entry \(c\) in position \(i\) and \(1\)
elsewhere. Then \(tv-v=(c-1)v_ie_i\in V\), so \(v_ie_i\in V\). Hence \(V\) is spanned by the \(e_i\) that it
contains. ∎

So for \(|F|\ge 3\) each cell \(C_S(F)\) contains exactly one subspace fixed by the torus, namely \(E_S\).

**Example 4.5 (\(n=4\), \(k=2\)).** The six subsets and their exponents \(d(S)=(s_1-1)+(s_2-2)\) are
\[
\{1,2\}\mapsto 0,\quad \{1,3\}\mapsto 1,\quad \{1,4\}\mapsto 2,\quad \{2,3\}\mapsto 2,\quad \{2,4\}\mapsto 3,\quad
\{3,4\}\mapsto 4 .
\]
The sum of the monomials is \(1+q+2q^2+q^3+q^4\), in agreement with Example 2.4. For \(S=\{2,4\}\) the basis of
Theorem 4.2(b) is
\[
v^{(2)}=(a,1,0,0)^{\mathsf T},\qquad v^{(4)}=(b,0,c,1)^{\mathsf T},
\]
with three free parameters \(a,b,c\), and \(D(S)=\{(1,2),(1,4),(3,4)\}\). Edge cases: the cell of \(\{1,2\}\) is the
single point \(E_2\), which \(B\) fixes; the cell of \(\{3,4\}\) has \(q^4\) elements and consists of the planes
\(V\) with \(V\cap E_2=0\). Over \(\mathbb F_2\) the cells have \(1,2,4,4,8,16\) elements, \(35\) in all. Over
\(\mathbb F_2\) all \(35\) planes are stable under \(T\), because \(T\) is trivial; over \(\mathbb F_3\) exactly the
six coordinate planes are.

## 5. The Bruhat decomposition of the general linear group

The factor \([n]_q!\) in Theorem 3.2 has the value \(n!\) at \(q=1\). This section explains it in the same way as
Section 4: \(\mathrm{GL}_n(F)\) is a disjoint union of \(n!\) cells, one for each permutation.

Let \(F\) be a field and \(n\ge 1\). For \(w\in S_n\) let \(P_w\) be the permutation matrix with
\(P_we_j=e_{w(j)}\). Then \(P_vP_w=P_{vw}\), and for every matrix \(g\)
\[
(P_w^{-1}gP_w)_{ab}=g_{w(a),w(b)},\qquad (P_w^{-1}g)_{ab}=g_{w(a),b}. \tag{5.1}
\]
A matrix is *monomial* if every row and every column contains exactly one non-zero entry. Let \(N\) be the set of
monomial matrices in \(\mathrm{GL}_n(F)\).

**Lemma 5.1 (monomial matrices).**

- (a) Every monomial matrix is \(P_wt\) with unique \(w\in S_n\) and \(t\in T\). The set \(N\) is a subgroup of
  \(\mathrm{GL}_n(F)\), \(T\) is a normal subgroup of \(N\), and \(P_wt\mapsto w\) induces an isomorphism
  \(N/T\to S_n\). The permutation matrices form a subgroup of \(N\) which maps isomorphically onto \(N/T\).
- (b) If \(|F|\ge 3\), then \(N\) is the normalizer of \(T\) in \(\mathrm{GL}_n(F)\).
- (c) If \(|F|=2\), then \(T=\{1\}\), \(N\) is the group of permutation matrices, and the normalizer of \(T\) is all
  of \(\mathrm{GL}_n(F)\).

We call \(W=N/T\cong S_n\) the *Weyl group* of \(\mathrm{GL}_n\).

*Reference:* [Lorscheid 2018b, §1.1] defines the Weyl group of \(\mathrm{GL}(n,\mathbb F_q)\) as the normalizer of
the diagonal torus modulo the torus, and states that this normalizer consists of the monomial matrices; for \(q=2\)
the torus is trivial and its normalizer is the whole group, so we define \(W\) through the monomial matrices.

*Proof.* (a) Let \(g\) be monomial and let \(w(j)\) be the row of the non-zero entry of column \(j\). Since every
row contains exactly one non-zero entry, \(w\) is a bijection, and \(g=P_wt\) with \(t_j=g_{w(j),j}\). Uniqueness
is clear. For \(t\in T\) and \(v\in S_n\) the matrix \(P_v^{-1}tP_v\) is diagonal, by (5.1). Hence
\(P_wt\cdot P_{w'}t'=P_{ww'}\,(P_{w'}^{-1}tP_{w'})\,t'\) is monomial, and so is
\((P_wt)^{-1}=P_{w^{-1}}(P_wt^{-1}P_w^{-1})\). So \(N\) is a group, and \(P_wt\mapsto w\) is a surjective
homomorphism \(N\to S_n\) with kernel \(T\). Its restriction to the permutation matrices is an isomorphism.

(b) Monomial matrices normalize \(T\) by (a). Conversely let \(g\) normalize \(T\). First, a vector \(v\) which is an
eigenvector of every \(t\in T\) is a multiple of some \(e_i\). Indeed, if \(v_i\ne 0\) and \(v_j\ne 0\) with
\(i\ne j\), take \(t\in T\) with \(t_i\ne t_j\), which exists because \(|F^\times|\ge 2\); then \(tv\) is not a
multiple of \(v\). Now for \(t\in T\) put \(t'=g^{-1}tg\in T\). Then \(t(ge_i)=g(t'e_i)=t'_i\,ge_i\). So \(ge_i\) is
an eigenvector of every \(t\in T\), hence a multiple of some \(e_{\sigma(i)}\). Since \(g\) is invertible,
\(\sigma\) is a permutation and \(g\) is monomial.

(c) is clear. ∎

**Definition 5.2.** Let \(w\in S_n\).

- The *length* \(\ell(w)\) is the number of inversions of \(w\), that is, of pairs \(a<b\) with \(w(a)>w(b)\).
- \(\Phi_w=\{(i,j): 1\le i<j\le n,\ w^{-1}(i)>w^{-1}(j)\}\).
- \(U_w=U\cap P_wU^-P_w^{-1}\).

For \(i\ne j\) and \(c\in F\) let \(x_{ij}(c)\) be the matrix with \(1\) on the diagonal, \(c\) in position \((i,j)\)
and \(0\) elsewhere. Left multiplication by \(x_{ij}(c)\) adds \(c\) times row \(j\) to row \(i\).

**Lemma 5.3.**

- (a) \(|\Phi_w|=\ell(w)\).
- (b) \(U_w\) is the set of \(u\in U\) such that \(u_{ij}=0\) for all \(i<j\) with \((i,j)\notin\Phi_w\). The map
  \(u\mapsto(u_{ij})_{(i,j)\in\Phi_w}\) is a bijection \(U_w\to F^{\Phi_w}\).
- (c) \(U_w\) is a group, \(P_w^{-1}U_wP_w\subseteq U^-\), and \(x_{ij}(c)\in U_w\) for \((i,j)\in\Phi_w\).

*Proof.* (a) The map \((a,b)\mapsto(w(b),w(a))\) is a bijection from the set of inversions of \(w\) to \(\Phi_w\).
(b) By (5.1), \(P_w^{-1}uP_w\in U^-\) means that \(u_{w(a),w(a)}=1\) and \(u_{w(a),w(b)}=0\) for \(a<b\). In other
words \(u_{ii}=1\), and \(u_{ij}=0\) whenever \(w^{-1}(i)<w^{-1}(j)\). For \(u\in U\) this leaves exactly the entries
in the positions \((i,j)\in\Phi_w\) free. (c) \(U_w\) is the intersection of two subgroups. The rest follows from
the definition and from (b). ∎

For the identity permutation \(\Phi_w\) is empty and \(U_w=\{1\}\). For the permutation \(w_0\) with
\(w_0(a)=n+1-a\), \(\Phi_{w_0}\) contains all pairs and \(U_{w_0}=U\).

**Theorem 5.4 (Bruhat decomposition with normal form).** Let \(F\) be a field and \(n\ge 1\).

- (a) For every \(g\in\mathrm{GL}_n(F)\) there are unique \(w\in S_n\), \(u\in U_w\) and \(b\in B\) with
  \(g=uP_wb\).
- (b) \(BP_wB=U_wP_wB\) for every \(w\in S_n\), and \(\mathrm{GL}_n(F)\) is the disjoint union of the \(n!\) double
  cosets \(BP_wB\).

*Reference:* [Connes–Consani 2011a, Theorem 4.5] quotes the corresponding statement for all Chevalley groups from
[Chevalley 1955, Théorème 2]; see Theorem 6.4.

*Proof.* *Existence.* We transform \(g\) by row operations and find distinct indices \(i_1,\dots,i_n\). Put \(m=g\).
For \(j=1,\dots,n\) in turn, assume that before step \(j\) the matrix \(m\) has these properties:

- (i) for \(a<j\), the first non-zero entry of row \(i_a\) is in column \(a\);
- (ii) every row \(i\notin\{i_1,\dots,i_{j-1}\}\) has zeros in the columns \(1,\dots,j-1\).

For \(j=1\) nothing is assumed. Let \(R=\Omega_n\setminus\{i_1,\dots,i_{j-1}\}\). By (ii) the first \(j-1\) columns
of \(m\) have non-zero entries only in the rows \(i_1,\dots,i_{j-1}\). They are linearly independent, because \(m\)
is invertible, so they span the space of all vectors with non-zero entries only in these rows. Column \(j\) is not in
this span. So it has a non-zero entry in some row of \(R\). Let \(i_j\) be the largest \(i\in R\) with
\(m_{i,j}\ne 0\). For every \(i\in R\) with \(i<i_j\), replace \(m\) by \(x_{i,i_j}(c)\,m\) with
\(c=-m_{i,j}/m_{i_j,j}\). This changes only row \(i\). It makes the entry of row \(i\) in column \(j\) zero, and it does
not change the entries of row \(i\) in the columns before \(j\), because row \(i_j\) is zero there. After these
operations, (i) and (ii) hold for \(j+1\). Indeed row \(i_j\) is unchanged; it is zero in the columns before \(j\)
and not zero in column \(j\). The rows in \(R\setminus\{i_j\}\) are zero in the columns \(1,\dots,j\): those below
row \(i_j\) by the choice of \(i_j\), those above it by the operations.

After step \(n\), define \(w\in S_n\) by \(w(a)=i_a\). The final matrix is \(m=xg\), where \(x\) is a product of
matrices \(x_{i,i_j}(c)\) with \(i<i_j\) and \(i\notin\{i_1,\dots,i_j\}\). For such a pair,
\(w^{-1}(i)>j=w^{-1}(i_j)\). So \((i,i_j)\in\Phi_w\), and \(x_{i,i_j}(c)\in U_w\) by Lemma 5.3(c). Hence
\(x\in U_w\). By (i), for every \(a\) the first non-zero entry of row \(w(a)\) of \(m\) is in column \(a\). By
(5.1) this says that \(b=P_w^{-1}m\) is upper triangular with non-zero diagonal entries, so \(b\in B\). Therefore
\(g=x^{-1}m=uP_wb\) with \(u=x^{-1}\in U_w\).

*An invariant.* For \(1\le i\le n\) and \(0\le j\le n\) let \(r_{ij}(g)\) be the rank of the submatrix of \(g\)
formed by the rows \(i,\dots,n\) and the columns \(1,\dots,j\). Let \(b\in B\). The rows \(i,\dots,n\) of \(bg\) are
obtained from the rows \(i,\dots,n\) of \(g\) by multiplication with the lower right block of \(b\), which is
invertible. The columns \(1,\dots,j\) of \(gb\) are obtained from the columns \(1,\dots,j\) of \(g\) by
multiplication with the upper left block of \(b\). So \(r_{ij}(bgb')=r_{ij}(g)\) for all \(b,b'\in B\). For a
permutation matrix, column \(c\) of the submatrix is non-zero exactly when \(w(c)\ge i\), and the non-zero columns
are distinct standard basis vectors. So \(r_{ij}(P_w)=|\{c\le j: w(c)\ge i\}|\). Then
\(r_{ij}(P_w)-r_{i,j-1}(P_w)\) is \(1\) if \(w(j)\ge i\) and \(0\) otherwise, and \(w(j)\) is the largest \(i\) for
which this difference is \(1\). So the numbers \(r_{ij}\) determine \(w\), and \(BP_wB\) and \(BP_{w'}B\) are
disjoint for \(w\ne w'\).

*Uniqueness.* Let \(uP_wb=u'P_{w'}b'\) with \(u\in U_w\), \(u'\in U_{w'}\) and \(b,b'\in B\). Both sides lie in a
double coset, so \(w=w'\) by the invariant. Then \(P_w^{-1}(u'^{-1}u)P_w=b'b^{-1}\). The left side lies in \(U^-\) by
Lemma 5.3(c), the right side in \(B\), and \(B\cap U^-=\{1\}\). So \(u=u'\) and \(b=b'\).

*Part (b).* We have \(U_wP_wB\subseteq BP_wB\). By existence, the sets \(U_wP_wB\) cover \(\mathrm{GL}_n(F)\). If
\(g\in BP_wB\), then \(g\in U_{w'}P_{w'}B\subseteq BP_{w'}B\) for some \(w'\), and \(w'=w\) because the double cosets
are disjoint. So \(BP_wB=U_wP_wB\). ∎

**Corollary 5.5 (the Bruhat count).** For a prime power \(q\) and \(w\in S_n\),
\[
|BP_wB|=q^{\ell(w)}\,|B|=(q-1)^n\,q^{\binom{n}{2}}\,q^{\ell(w)},\qquad
|\mathrm{GL}_n(\mathbb F_q)|=(q-1)^n\,q^{\binom{n}{2}}\sum_{w\in S_n}q^{\ell(w)} .
\]

*Proof.* By Theorem 5.4 the map \(U_w\times B\to BP_wB\), \((u,b)\mapsto uP_wb\), is a bijection. By Lemma 5.3,
\(|U_w|=q^{\ell(w)}\), and \(|B|=(q-1)^nq^{\binom{n}{2}}\) by Proposition 3.6. ∎

**Corollary 5.6.**

- (a) \(\sum_{w\in S_n}q^{\ell(w)}=[n]_q!\) as polynomials in \(q\).
- (b) Let \(F\) be a field and let \(E^w_\bullet\) be the complete flag with members
  \(\operatorname{span}(e_{w(1)},\dots,e_{w(j)})\). Every complete flag in \(F^n\) is \(u\cdot E^w_\bullet\) for a
  unique \(w\in S_n\) and a unique \(u\in U_w\). So the set of complete flags is the disjoint union of \(n!\) cells,
  the cell of \(w\) is in bijection with \(F^{\ell(w)}\), and the cells are the orbits of \(B\).

*Proof.* (a) Compare Corollary 5.5 with Theorem 3.2 for all prime powers and use (B4). Exercise 6 gives a direct
proof. (b) The proof of Proposition 3.6(c) works over any field: \(\mathrm{GL}_n(F)\) acts transitively on complete
flags, and the stabilizer of \(E_\bullet=(E_1\subset\dots\subset E_n)\) is \(B\). Note that
\(E^w_\bullet=P_wE_\bullet\). Write \(g=uP_wb\) as in Theorem 5.4; then \(gE_\bullet=uE^w_\bullet\). If
\(uE^w_\bullet=u'E^{w'}_\bullet\), then \(uP_w=u'P_{w'}b\) for some \(b\in B\), and the uniqueness in Theorem 5.4
gives \(w=w'\) and \(u=u'\). The cell of \(w\) is the image of \(BP_wB\), which is a \(B\)-orbit. ∎

**Example 5.7.** *The case \(n=2\).* There are two permutations, the identity and the transposition \(s\), with
\(\ell(s)=1\) and \(U_s=U\). The cell \(B\) consists of the invertible matrices with lower left entry \(0\). Let
\(g=\begin{pmatrix}a&b\\ c&d\end{pmatrix}\) with \(c\ne 0\). Then
\[
g=\begin{pmatrix}1&a/c\\0&1\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}
\begin{pmatrix}c&d\\0&b-ad/c\end{pmatrix},
\]
and \(b-ad/c=-\det(g)/c\ne 0\). Over \(\mathbb F_q\) the two cells have \(|B|=(q-1)^2q\) and \(q\,|B|\) elements. The
sum is \((q-1)^2q(1+q)\), as in Example 3.7.

*The case \(n=3\).* Write \(w\) as the word \(w(1)w(2)w(3)\). The lengths are
\[
\ell(123)=0,\quad \ell(213)=\ell(132)=1,\quad \ell(231)=\ell(312)=2,\quad \ell(321)=3 ,
\]
and \(1+2q+2q^2+q^3=(1+q)(1+q+q^2)=[3]_q!\).

*Edge cases.* For \(n=1\) there is one cell. For \(q=2\) we have \(B=U\), and the cell of \(w\) has
\(2^{\ell(w)+\binom{n}{2}}\) elements; for \(n=3\) the sizes are \(8,16,16,32,32,64\), with sum \(168\).

## 6. The value at q = 1

**Definition 6.1.** Let \(X\) assign a finite set \(X(\mathbb F_q)\) to every prime power \(q\). A *counting
polynomial* for \(X\) is a polynomial \(N_X\in\mathbb Z[q]\) with \(|X(\mathbb F_q)|=N_X(q)\) for every prime power
\(q\). By (B4) there is at most one. Write it in powers of \(q-1\):
\[
N_X(q)=\sum_{j\ge 0}a_j\,(q-1)^j,\qquad a_j\in\mathbb Z .
\]
The numbers \(a_j\) are the *coefficients at \(q=1\)*. If \(N_X\ne 0\), the *order at \(q=1\)* is the smallest \(r\)
with \(a_r\ne 0\), and \(a_r\) is the *leading coefficient at \(q=1\)*. If the order is \(0\), the leading
coefficient is the value \(N_X(1)\).

[Lorscheid 2018b, §1] records the name "limit \(q\to 1\)" for the analogue at \(q=1\). For the groups, the limit
is taken in [Lorscheid 2018b, §1.1] after division by \(|T|=(q-1)^n\); this is the passage to the leading
coefficient.

**Theorem 6.2 (values at \(q=1\)).** Let \(n\ge 1\), \(0\le k\le n\), and let \(n_1,\dots,n_r\) be positive integers
with sum \(n\). Each of the following has a counting polynomial. The list gives the polynomial, its order at
\(q=1\), its leading coefficient at \(q=1\), and an object attached to the finite set \(\Omega_n\) which has this
number of elements.

- (1) Points of \(\mathbb P^{n-1}\): \([n]_q\); order \(0\); \(n\); the elements of \(\Omega_n\).
- (2) Subspaces of dimension \(k\) of the \(n\)-dimensional space: \(\binom{n}{k}_q\); order \(0\);
  \(\binom{n}{k}\); the subsets of \(\Omega_n\) with \(k\) elements.
- (3) Flags of type \((n_1,\dots,n_r)\): \([n]_q!/([n_1]_q!\cdots[n_r]_q!)\); order \(0\);
  \(n!/(n_1!\cdots n_r!)\); the flags of subsets of the same type.
- (4) Complete flags: \([n]_q!\); order \(0\); \(n!\); the permutations of \(\Omega_n\).
- (5) The torus \(T\): \((q-1)^n\); order \(n\); \(1\); the trivial group.
- (6) The group \(B\): \((q-1)^nq^{\binom{n}{2}}\); order \(n\); \(1\); the trivial group.
- (7) The group \(P_{(n_1,\dots,n_r)}\): \((q-1)^nq^{\binom{n}{2}}[n_1]_q!\cdots[n_r]_q!\); order \(n\);
  \(n_1!\cdots n_r!\); the group \(S_{n_1}\times\dots\times S_{n_r}\).
- (8) The group \(\mathrm{GL}_n\): \((q-1)^nq^{\binom{n}{2}}[n]_q!\); order \(n\); \(n!\); the group \(S_n\).
- (9) The group \(N\) of monomial matrices: \(n!\,(q-1)^n\); order \(n\); \(n!\); the group \(S_n\).
- (10) The group \(\mathrm{SL}_n\) of matrices of determinant \(1\): \((q-1)^{n-1}q^{\binom{n}{2}}[n]_q!\); order
  \(n-1\); \(n!\); the group \(S_n\).

The leading coefficients are compatible with the group actions: the identity
\(|\mathrm{GL}_n(\mathbb F_q)|=|P(\mathbb F_q)|\cdot|\{\text{flags}\}|\) for \(P=P_{(n_1,\dots,n_r)}\) becomes
\(|S_n|=|S_{n_1}\times\dots\times S_{n_r}|\cdot|\{\text{flags of subsets}\}|\).

*Proof.* (1)–(4) are Corollary 3.4, Theorem 3.3 and Theorem 3.5, with Proposition 2.3(d) and the count of flags of
subsets after Theorem 3.5. The quotient in (3) is a polynomial with integer coefficients, because it is the product
\(\binom{n}{n_1}_q\binom{n-n_1}{n_2}_q\cdots\binom{n_r}{n_r}_q\) of the Gaussian binomial coefficients from the
proof of Theorem 3.5. (5)–(7) are Proposition 3.6. (8) is Theorem 3.2. (9) holds because
\(N=\bigsqcup_wP_wT\) by Lemma 5.1. (10) holds because the determinant is a surjective homomorphism
\(\mathrm{GL}_n(\mathbb F_q)\to\mathbb F_q^\times\) with kernel \(\mathrm{SL}_n(\mathbb F_q)\). In each case the
polynomial is a power of \(q-1\) times a polynomial whose value at \(q=1\) is the stated number, since
\(q^{\binom{n}{2}}\) and \([m]_q!\) have the values \(1\) and \(m!\) at \(q=1\). The last statement is (B3) for both
actions. ∎

Two warnings. First, the orders of the groups (5)–(10) vanish at \(q=1\), except the order of \(\mathrm{SL}_1\),
the trivial group, which is \(1\); only the leading coefficient is meaningful.
Second, the leading coefficient forgets a lot: \(T\) and \(B\) both give \(1\).

The next proposition says what all coefficients at \(q=1\) count, and it identifies the part of
\(\mathrm{GL}_n(\mathbb F_q)\) that belongs to the leading coefficient.

**Proposition 6.3 (torus decompositions).**

- (a) For every field \(F\) and \(d\ge 0\), the set \(F^d\) is the disjoint union, over the subsets
  \(Y\subseteq\Omega_d\), of the sets \(\{x: x_i\ne 0\iff i\in Y\}\cong(F^\times)^Y\). Hence
  \(q^d=\sum_{j}\binom{d}{j}(q-1)^j\).
- (b) Each of the sets in (1)–(4) and (8) of Theorem 6.2 is, for every \(q\), a disjoint union of subsets in
  bijection with \((\mathbb F_q^\times)^j\) for various \(j\), and the number \(a_j\) of pieces with exponent \(j\)
  does not depend on \(q\). These numbers are the coefficients at \(q=1\) of the counting polynomial. In particular
  the coefficients are non-negative. For the subspaces of dimension \(k\), \(a_j=\sum_{|S|=k}\binom{d(S)}{j}\). For
  \(\mathrm{GL}_n\), \(a_j=\sum_{w\in S_n}\binom{\binom{n}{2}+\ell(w)}{j-n}\).
- (c) Every \(g\in\mathrm{GL}_n(F)\) is \(g=uP_wtu'\) with unique \(w\in S_n\), \(u\in U_w\), \(t\in T\),
  \(u'\in U\). The elements with \(u=u'=1\) are exactly the monomial matrices. Over \(\mathbb F_q\) they are the
  union of the pieces with exponent \(n\), and \(a_n=n!\).

*Proof.* (a) Sort the vectors by the set of indices of their non-zero coordinates, and count. (b) Theorem 4.2
writes the set of \(k\)-dimensional subspaces as \(\bigsqcup_SC_S\) with \(C_S\cong\mathbb F_q^{d(S)}\); this covers
(1) and (2). Corollary 5.6(b) does the same for complete flags. For flags of any type use the induction in the
proof of Theorem 3.5: choose for every \(V_1\) an isomorphism of \(V/V_1\) with \(\mathbb F_q^{n-n_1}\); then the
set of flags is in bijection with the disjoint union, over the cells \(C_S\) of the possible \(V_1\), of the
products of \(C_S\) with the set of flags of type \((n_2,\dots,n_r)\) in \(\mathbb F_q^{n-n_1}\), and a product of
affine spaces is an affine space. For the group use (c): it gives a bijection
\(\mathrm{GL}_n(\mathbb F_q)\cong\bigsqcup_w\mathbb F_q^{\ell(w)}\times(\mathbb F_q^\times)^n\times\mathbb F_q^{\binom{n}{2}}\).
Apply (a) to each affine space. Counting the points gives \(N(q)=\sum_ja_j(q-1)^j\) for all prime powers \(q\), and
then as polynomials by (B4). (c) Combine Theorem 5.4 with the unique factorization \(b=tu'\) of \(b\in B\). A
monomial matrix \(P_wt\) has this form with \(u=u'=1\), and by uniqueness these are the only such elements. ∎

So \(\mathrm{GL}_n(\mathbb F_q)\) is the group \(N(\mathbb F_q)\) of monomial matrices, with exactly
\(n!\,(q-1)^n\) elements, together with pieces of higher order in \(q-1\).

**Theorem 6.4 (cell decomposition of a Chevalley group).** Let \(\mathfrak G\) be a pinned split reductive group
scheme over \(\mathbb Z\), in the sense of Pinnings and the classification of split reductive groups,
with character lattice \(L\), roots \(\Phi\) and the positive roots of its pinning. The Chevalley group scheme of a
root system \((L,\Phi,(n_r))\) in the sense of [Connes–Consani 2011a, §4.1 and §4.3] is of this kind; see
*Varieties over the field with one element after Soulé and Connes–Consani*, Section 8.6. Let \(\ell\) be the rank
of the lattice \(L\), let \(N\) be the number of
positive roots, let \(W\) be the Weyl group, and for \(w\in W\) let \(N(w)\) be the number of positive roots \(r\)
such that \(w(r)\) is negative. For every field \(K\), the group \(\mathfrak G(K)\) is the disjoint union of cells
\(C_w=\mathcal U(K)\,\mathcal T(K)\,n_w\,\mathcal U_w(K)\), \(w\in W\), and the product map
\(\mathcal U(K)\times\mathcal T(K)\times\mathcal U_w(K)\to C_w\) is a bijection. Here \(\mathcal T\) is a split
maximal torus of \(\mathfrak G\), \(\mathcal U\) is the subgroup generated by the root subgroups of the positive
roots, \(\mathcal U_w\) is the subgroup generated by the root subgroups of the positive roots \(r\) such that
\(w(r)\) is negative, and \(n_w\) is a point with values in \(K\) of the normalizer of \(\mathcal T\) in
\(\mathfrak G\), chosen so that it represents \(w\). As sets,
\(\mathcal T(K)\cong(K^\times)^\ell\), \(\mathcal U(K)\cong K^N\) and \(\mathcal U_w(K)\cong K^{N(w)}\).
Consequently
\[
|\mathfrak G(\mathbb F_q)|=(q-1)^\ell\,q^N\sum_{w\in W}q^{N(w)} .
\]

*Proof.* Write \(\mathcal B=\mathcal U\mathcal T\) for the Borel subgroup of the pinning, so that multiplication
\(\mathcal U\times\mathcal T\to\mathcal B\) is an isomorphism. By
Root data, Weyl chambers and the Bruhat decomposition, Section 5, multiplication of the positive root
subgroups, in any order, is an isomorphism onto \(\mathcal U\); and for a set \(\Psi\subseteq\Phi^+\) containing
every root that is a sum of roots of \(\Psi\), the product of the root subgroups of \(\Psi\) is a closed subgroup
\(\mathcal U_\Psi\), isomorphic to an affine space. The set \(\Phi_w=\{r\in\Phi^+:w(r)<0\}\) has this property,
because \(w\) maps a root that is a sum of roots of \(\Phi_w\) to a sum of negative roots, and
\(\mathcal U_w=\mathcal U_{\Phi_w}\). So \(\mathcal U(K)\cong K^N\) and \(\mathcal U_w(K)\cong K^{N(w)}\), and
\(\mathcal T(K)\cong(K^\times)^\ell\) because \(\mathcal T\) is split.

Theorems 6.2 and 8.1 there give, for every field \(K\),
\(\mathfrak G(K)=\bigsqcup_{v\in W}\mathcal B(K)\,n_v\,\mathcal B(K)\), and every element of
\(\mathcal B(K)\,n_v\,\mathcal B(K)\) is \(u\,n_v\,b\) for exactly one \(u\in\mathcal U_{\Psi_v}(K)\) and
\(b\in\mathcal B(K)\), where \(\Psi_v=\{r\in\Phi^+:v^{-1}(r)<0\}\): the map \((u,b)\mapsto u\,n_v\,b\) is an
immersion, hence injective on points. Let \(g\in\mathfrak G(K)\). Applied to \(g^{-1}\), this gives a unique \(v\)
and a unique pair \((u,b)\) with \(g^{-1}=u\,n_v\,b\). Put \(w=v^{-1}\), so that \(\Psi_v=\Phi_w\). Both
\(n_v^{-1}\) and \(n_w\) represent \(w\), so \(n_v^{-1}=t_1n_w\) with \(t_1\in\mathcal T(K)\). Write
\(b^{-1}t_1=u't'\) with \(u'\in\mathcal U(K)\) and \(t'\in\mathcal T(K)\). Then
\[
g=b^{-1}\,n_v^{-1}\,u^{-1}=u'\,t'\,n_w\,u^{-1},\qquad u^{-1}\in\mathcal U_w(K).
\]
Conversely, \(n_w^{-1}=n_vt_2\) with \(t_2\in\mathcal T(K)\), so an element \(u'\,t'\,n_w\,u''\) of \(C_w\) has the
inverse \(u''^{-1}\,n_v\,(t_2t'^{-1}u'^{-1})\) in \(\mathcal U_w(K)\,n_v\,\mathcal B(K)\). Hence \(g\in C_w\)
exactly when \(g^{-1}\in\mathcal B(K)\,n_{w^{-1}}\,\mathcal B(K)\); the cells are disjoint and cover
\(\mathfrak G(K)\); and the triple \((u',t',u'')\) is determined by \(g\), because \(v\), \(u\) and \(b\) are. Over
\(\mathbb F_q\) the cell \(C_w\) has \(q^N(q-1)^\ell q^{N(w)}\) elements, and summing over \(w\) gives the formula.
∎

This is [Connes–Consani 2011a, Theorem 4.5, Lemmas 4.6 and 4.7, and equation (2) of §1]; the decomposition is
quoted there from [Chevalley 1955, Théorème 2].

The group scheme \(\mathrm{GL}_n\) is the Chevalley group scheme of the root system with \(L=\mathbb Z^n\) and the
roots \(e_i-e_j\), \(i\ne j\); the lesson does not prove this identification. With it, Corollary 5.5 is the case
\(\mathfrak G=\mathrm{GL}_n\) of the formula. There \(\ell=n\), the positive roots \(e_i-e_j\) correspond to the
pairs \(i<j\), so \(N=\binom{n}{2}\), the Weyl group is \(S_n\), and \(N(w)=\ell(w)\). Applying
Theorem 5.4 to \(g^{-1}\) gives the mirrored form \(g=b\,P_v\,u'\) with \(u'\in U_{v^{-1}}\), which is the form used
in the statement. In general, the order at \(q=1\) of \(|\mathfrak G(\mathbb F_q)|\) is the rank \(\ell\), and the
leading coefficient is \(|W|\). [Soulé 1999, §1] states this in the form
\(|G(\mathbb F_q)|\sim(q-1)^r\,|W|\) as \(q\to 1\), for a Chevalley group scheme \(G\) of rank \(r\).

**Remark 6.5 (another meaning of \(N(1)\); not proved in this lesson).** For a smooth toric variety,
[Soulé 2004, Théorème 2] states that the counting polynomial \(N\) exists and that \(N(1)\) is the Euler–Poincaré
characteristic of the space of complex points; [Soulé 1999, §6] already relates the behaviour at \(q=1\) to this
Euler characteristic. For example \(\mathbb P^{n-1}(\mathbb C)\) has Euler characteristic \(n\).

## 7. Tits's proposal and the geometry of a finite set

In Tits's paper a *geometry* consists of a set of elements divided into families, a reflexive and symmetric
relation of incidence between the elements, and a group of permutations of the elements that preserves the
families and the incidence. The first example there is the projective geometry of dimension \(n\) over a field:
the elements are the linear varieties of dimensions \(0\) to \(n-1\) of a projective space of dimension \(n\), the
families collect those of a fixed dimension, and the group is the group of projectivities. The paper then considers the geometry attached to a Chevalley group \(G\) over \(\mathbb F_q\). Its families are homogeneous
spaces of \(G\), and the number of elements of each family is a quotient of two orders.

No. 13 of the paper, whose beginning is reproduced in [Lorscheid–Thas 2023], then introduces the "field of
characteristic 1", written \(K_1\). Its only element is
\(1=0\), and Tits notes that \(K_1\) is generally not regarded as a field. The projective space of
dimension \(n\) over \(K_1\) is a set of \(n+1\) points. All its subsets are linear varieties, the dimension of a
subset is its number of points minus one, and the projectivities are all permutations of the points. In the
quotient that counts a family of the geometry of a Chevalley group over \(\mathbb F_q\), numerator and denominator
contain the factor \(q-1\) equally often. The value of the quotient at \(q=1\) after cancellation is the number of
elements of the corresponding family of the geometry over \(K_1\). The group of that geometry is the Weyl group,
and its order is obtained from the order of the Chevalley group by removing the factors \(q-1\) and then putting
\(q=1\). This is the passage to the leading coefficient of Definition 6.1.

[Soulé 1999, §1], [Soulé 2004, §1.1] and [Connes–Consani 2011a, §1] describe the proposal in this form: for a
Chevalley group \(G\), the Weyl group \(W\) is the group of points of \(G\) over the field of characteristic one,
in symbols \(G(\mathbb F_1)=W\). [Soulé 1999, §1] describes the geometry over \(K_1\) as the limit of the
geometries of the groups \(G(\mathbb F_q)\) when \(q\) goes to \(1\), the finite geometry attached to the Coxeter
group \(W\). [Manin 1995, §1.6] records the case of the general linear group as the
formula \(\mathrm{GL}(n,\mathbb F_1)=S_n\), and adds that the points over \(\mathbb F_1\) of a classical linear
group form its Weyl group. [Lorscheid 2018b, §1.1] explains the word "geometry": it is a collection of homogeneous
spaces of one group, with an incidence relation between their elements. For the general linear group the
homogeneous spaces are the sets of subspaces of a fixed dimension, and incidence is inclusion. According to
[Lorscheid 2018b, §1.1], Tits treats semisimple groups, so the projective linear group takes the place of
\(\mathrm{GL}_n\).

This section makes the proposal precise for the general linear group and proves it.

**Definition 7.1.**

- Let \(V\) be a vector space of dimension \(n\) over a field. The *geometry of \(V\)*, written
  \(\mathrm{PG}(V)\), is the set of subspaces \(X\) with \(0\ne X\ne V\), with the *type* \(\dim X\) and the
  *incidence* relation: \(X\) and \(X'\) are incident if \(X\subseteq X'\) or \(X'\subseteq X\).
- Let \(\Omega\) be a set with \(n\) elements. The *geometry of \(\Omega\)*, written \(\Sigma(\Omega)\), is the set
  of subsets \(A\) with \(\emptyset\ne A\ne\Omega\), with the type \(|A|\) and the incidence relation given by
  inclusion in the same way.

In both cases elements of type \(1\) are *points* and elements of type \(2\) are *lines* (for \(n\ge 3\)). An
*isomorphism* of geometries is a bijection that preserves type and incidence in both directions.

For a set \(\Omega\) with \(n+1\) elements, \(\Sigma(\Omega)\) with the group of all permutations of \(\Omega\) is
the projective geometry of dimension \(n\) over \(K_1\) of Tits's no. 13: a subset with \(k\) elements is a
linear variety of dimension \(k-1\). Theorem 7.4 below shows that the permutations are all the automorphisms.

**Theorem 7.2 (the incidence numbers at \(q=1\)).** Let \(0\le i\le m\le j\le n\).

- (a) In \(\mathbb F_q^n\), the number of subspaces of dimension \(m\) between a subspace of dimension \(i\) and a
  subspace of dimension \(j\) containing it is \(\binom{j-i}{m-i}_q\).
- (b) In a set with \(n\) elements, the number of subsets with \(m\) elements between a subset with \(i\) elements
  and a subset with \(j\) elements containing it is \(\binom{j-i}{m-i}\). This is the value of (a) at \(q=1\).

In particular, for \(n\ge 3\), a line of \(\mathrm{PG}(\mathbb F_q^n)\) has \(q+1\) points and a line of
\(\Sigma(\Omega)\) has \(2\) points; a point lies on \([n-1]_q\) lines, respectively on \(n-1\) lines.

*Proof.* (a) is Corollary 3.4(b). (b) If \(A\subseteq C\), the map \(X\mapsto X\setminus A\) is a bijection from the
subsets between \(A\) and \(C\) to the subsets of \(C\setminus A\). The rest is Proposition 2.3(d). ∎

**Proposition 7.3 (a projective geometry with thin lines).** Let \(n\ge 3\). Consider the following statements
about points and lines.

- (P1) Two distinct points lie on exactly one line.
- (P2) If \(a,b,c,d\) are four distinct points and the lines \(ab\) and \(cd\) have a common point, then the lines
  \(ac\) and \(bd\) have a common point.
- (P3) Every line has at least three points.

For every field \(F\), the geometry \(\mathrm{PG}(F^n)\) satisfies (P1), (P2) and (P3). The geometry
\(\Sigma(\Omega)\) of a set with \(n\) elements satisfies (P1) and (P2), and every line of it has exactly two
points.

*Proof.* In \(\mathrm{PG}(F^n)\): the line through two distinct points \(a,b\) is the subspace \(a+b\), which gives
(P1). A line is a two-dimensional space and has \(|F|+1\ge 3\) one-dimensional subspaces, which gives (P3). For (P2),
the subspaces \(a+b\) and \(c+d\) have dimension \(2\) and meet in a non-zero subspace, so their sum \(Y\) has
dimension at most \(3\) by (B2). The lines \(a+c\) and \(b+d\) are two-dimensional subspaces of \(Y\), so they meet
in a subspace of dimension at least \(2+2-3=1\). In \(\Sigma(\Omega)\): the line through the points \(\{x\}\) and
\(\{y\}\) is \(\{x,y\}\), and it contains no other point. This gives (P1) and the last claim. If \(a,b,c,d\) are four
distinct points, the lines \(ab\) and \(cd\) are disjoint subsets, so they have no common point and (P2) holds for
lack of cases. ∎

[Connes–Consani 2011a, §1] describes this situation in the language of Tits's buildings: the requirement (P3) is
called thickness, and replacing it by "exactly two points on a line" gives a degenerate but coherent geometry.

**Theorem 7.4 (automorphisms).**

- (a) Let \(|\Omega|=n\ge 2\). Every permutation \(\sigma\) of \(\Omega\) defines an automorphism
  \(A\mapsto\sigma(A)\) of \(\Sigma(\Omega)\), and every automorphism of \(\Sigma(\Omega)\) is of this form for a
  unique \(\sigma\). So the automorphism group is the symmetric group.
- (b) Let \(F\) be a field and \(n\ge 2\). The group \(\mathrm{GL}_n(F)\) acts on \(\mathrm{PG}(F^n)\) by
  automorphisms, and the elements that act trivially are the scalar matrices.

*Proof.* (a) Let \(\varphi\) be an automorphism. It permutes the points, so \(\varphi(\{x\})=\{\sigma(x)\}\) for a
permutation \(\sigma\). For an element \(A\), the point \(\{x\}\) is incident with \(A\) exactly when \(x\in A\).
Since \(\varphi\) preserves incidence in both directions, \(\sigma(x)\in\varphi(A)\) exactly when \(x\in A\). So
\(\varphi(A)=\sigma(A)\). (b) Invertible matrices preserve dimension and inclusion. Let \(g\) fix every
one-dimensional subspace, so \(gv=\lambda_vv\) for every \(v\ne 0\). If \(v\) and \(v'\) are independent, then
\(g(v+v')=\lambda_{v+v'}(v+v')=\lambda_vv+\lambda_{v'}v'\) gives \(\lambda_v=\lambda_{v'}\). If they are dependent,
\(\lambda_v=\lambda_{v'}\) is clear. So \(g\) is a scalar matrix. ∎

Over \(\mathbb F_q\) the scalar matrices form a group of order \(q-1\). At \(q=1\) this is the trivial group, and
the three groups \(\mathrm{GL}_n\), \(\mathrm{SL}_n\) and \(\mathrm{GL}_n\) modulo scalars all correspond to
\(S_n\); compare Theorem 6.2.

**Theorem 7.5 (the geometry of a set inside the geometry of a vector space).** Let \(F\) be a field and
\(n\ge 2\).

- (a) The map \(\iota\colon\Sigma(\Omega_n)\to\mathrm{PG}(F^n)\), \(S\mapsto E_S\), is injective and preserves type
  and incidence in both directions.
- (b) The map \(J\colon\mathrm{PG}(F^n)\to\Sigma(\Omega_n)\), \(V\mapsto J(V)\), preserves type and inclusion, and
  \(J\circ\iota\) is the identity. It is constant on the orbits of \(B\), and its fibres are exactly the orbits of
  \(B\). Over \(\mathbb F_q\) the fibre over \(S\) has \(q^{d(S)}\) elements.
- (c) For \(g=P_wt\in N\) we have \(gE_S=E_{w(S)}\). So \(N\) acts on the image of \(\iota\) through
  \(N\to N/T\cong S_n\), and \(\iota\) is compatible with the actions of \(S_n\).
- (d) If \(|F|\ge 3\), the image of \(\iota\) is the set of elements of \(\mathrm{PG}(F^n)\) that are fixed by
  the torus \(T\).

*Proof.* (a) \(\dim E_S=|S|\), and \(E_S\subseteq E_{S'}\) exactly when \(S\subseteq S'\). (b) If \(V\subseteq V'\)
then \(J(V)\subseteq J(V')\) by the definition of \(J\). The rest is Theorem 4.2. (c) \(P_wte_s=t_se_{w(s)}\).
(d) is Proposition 4.4. ∎

So the geometry of the set \(\Omega_n\) is inside the projective geometry over every field, as the part fixed by
the torus (if the field has at least three elements), and the Weyl group \(N/T\) acts on it. It is also a quotient
of that geometry, by the map \(J\). [Connes–Consani 2011a, §1] and [Lorscheid 2018b, §1.1] point to Tits's theory
of buildings for the conceptual explanation of these facts; there the thin geometries of this kind are the
apartments. This lesson does not use that theory.

**Example 7.6 (from projective three-space to the tetrahedron).** Let \(n=4\). The geometry
\(\mathrm{PG}(\mathbb F_q^4)\) has points, lines and planes. Their numbers are
\[
[4]_q=1+q+q^2+q^3,\qquad \binom{4}{2}_q=1+q+2q^2+q^3+q^4,\qquad [4]_q .
\]
For \(q=2\) this is \(15\), \(35\), \(15\); for \(q=3\) it is \(40\), \(130\), \(40\). A line has \(q+1\) points and
lies in \(q+1\) planes. A point lies on \([3]_q=1+q+q^2\) lines, and a plane contains \([3]_q\) lines. There are
\([4]_q!=(1+q)(1+q+q^2)(1+q+q^2+q^3)\) complete flags: \(315\) for \(q=2\) and \(2080\) for \(q=3\). Counting the
incident pairs of a point and a line in two ways gives \([4]_q[3]_q=\binom{4}{2}_q(q+1)\); both sides are
\(1+2q+3q^2+3q^3+2q^4+q^5\).

At \(q=1\) the numbers are \(4\), \(6\), \(4\): the vertices, edges and faces of a tetrahedron. An edge has \(2\)
vertices and lies in \(2\) faces. A vertex lies on \(3\) edges and a face has \(3\) edges. There are \(24\) complete
flags (a vertex on an edge on a face), and the incidence count reads \(4\cdot 3=6\cdot 2\). The automorphism group is
\(S_4\). The case \(n=3\), \(q=2\) is treated in [Lorscheid 2018b, Example 1.1]: the plane with \(7\) points and
\(7\) lines becomes a triangle.

The symmetric group sits inside \(\mathrm{GL}_n(\mathbb Z)\) as the group of permutation matrices, and so inside
\(\mathrm{GL}_n(F)\) for every field \(F\). One may hope that the Weyl group of every Chevalley group sits inside
its group of integral points in the same way. This is not so.

**Proposition 7.7 (signs).** Let \(F\) be a field. Let \(N'\) be the group of monomial matrices of determinant
\(1\) in \(\mathrm{SL}_2(F)\) and \(T'\) its subgroup of diagonal matrices. Then \(N'/T'\) has two elements, and
every element of \(N'\setminus T'\) has square \(-1\). So if the characteristic of \(F\) is not \(2\), no element
of \(N'\setminus T'\) has order \(2\), and no subgroup of \(N'\) maps isomorphically onto \(N'/T'\). The same holds
over \(\mathbb Z\): the monomial matrices in \(\mathrm{SL}_2(\mathbb Z)\) form a cyclic group of order \(4\).

*Reference:* [Lorscheid 2018b, §3.2].

*Proof.* An element of \(N'\setminus T'\) is \(\begin{pmatrix}0&b\\ c&0\end{pmatrix}\) with \(-bc=1\), and its square
is \(bc\cdot 1=-1\). Over \(\mathbb Z\) the entries are \(\pm1\), so
\(N'=\{\pm 1,\pm j\}\) with \(j=\begin{pmatrix}0&1\\ -1&0\end{pmatrix}\), and \(j\) has order \(4\). ∎

So the Weyl group of \(\mathrm{SL}_2\), which has order \(2\), is not a subgroup of \(\mathrm{SL}_2(\mathbb Z)\) in
a way compatible with \(N'\to N'/T'\). The statement "the points of \(G\) over \(\mathbb F_1\) form the Weyl group"
cannot mean that the Weyl group is lifted in this way to a subgroup of \(G(\mathbb Z)\). What does sit inside the
integral points is an extension of the Weyl group by a group of signs: for \(\mathrm{GL}_d\) the group of monomial
matrices with entries \(0\) and \(\pm 1\), and for \(\mathrm{SL}_2\) the cyclic group of order \(4\) of
Proposition 7.7. For a Chevalley group \(G\) with split maximal torus \(T\) of rank \(\ell\) and normalizer \(N\), the
group \(N(\mathbb Z)\) is an extension of \(W\) by \(T(\mathbb Z)\cong(\mathbb Z/2\mathbb Z)^{\ell}\)
[Connes–Consani 2011a, Theorem 4.3]. [Soulé 1999, §5.5] arrives at the same kind of group: there the points of a Chevalley
group \(G\) with values in a ring \(R\) are to be the elements of \(G(R)\) that every homomorphism
\(R\to\mathbb C\) maps into the standard maximal compact subgroup of \(G(\mathbb C)\), and the resulting group
\(G(\mathbb F_1)\) is described as an extension of \(W\) by a finite elementary abelian \(2\)-group. For
\(R=\mathbb Z\) and \(G=\mathrm{GL}_d\) this is the group of Exercise 7. We meet it again in Section 8, as a group
of points over \(\mathbb F_{1^2}\).

## 8. The extensions \(\mathbb F_{1^n}\)

In this section \(n\ge 1\) is the degree of an extension, and dimensions are called \(d\).

[Soulé 1999, §1 and §4.1] and [Soulé 2004, §1.3] report two ideas from unpublished work of Smirnov and of Kapranov and Smirnov: a vector space over \(\mathbb F_1\) is a finite pointed set, and for every
\(n\ge 1\) the field \(\mathbb F_1\) has an extension of degree \(n\) whose invertible elements are the roots of unity
of order \(n\). [Soulé 1999, §4.1] compares this with a finite field \(\mathbb F_q\), whose extension of degree \(n\)
is obtained by adjoining roots of unity, and decides that
\(\mathbb F_{1^n}\otimes_{\mathbb F_1}\mathbb Z=\mathbb Z[T]/(T^n-1)\), the ring of functions on the group scheme of
\(n\)-th roots of unity. [Connes–Consani 2011a, §1] reports from the work of Kapranov and Smirnov that the points
of \(\mathrm{GL}_d\) over \(\mathbb F_{1^n}\) form the wreath product of the symmetric group \(S_d\) with
\(\mu_n^d\). The definitions below are the lesson's own. They are chosen so that these statements become theorems.

In this course a *monoid* is a commutative monoid, written multiplicatively, with a unit \(1\) and an absorbing
element \(0\); morphisms preserve \(1\) and \(0\).

**Definition 8.1.** Let \(\mu_n=\{z\in\mathbb C: z^n=1\}\), a cyclic group of order \(n\). Put
\[
\mathbb F_{1^n}=\{0\}\cup\mu_n ,
\]
a monoid under multiplication. In particular \(\mathbb F_1=\{0,1\}\).

Every non-zero element of \(\mathbb F_{1^n}\) is invertible. There is no addition. [Lorscheid 2018b, Prologue]
remarks that in most approaches the object called \(\mathbb F_1\) is this monoid: it has two elements and it is not
a field.

**Proposition 8.2.**

- (a) The morphisms of monoids \(\mathbb F_{1^m}\to\mathbb F_{1^n}\) correspond to the group homomorphisms
  \(\mu_m\to\mu_n\). An injective morphism exists if and only if \(m\) divides \(n\), and then its image is the
  unique copy \(\{0\}\cup\mu_m\) of \(\mathbb F_{1^m}\) in \(\mathbb F_{1^n}\).
- (b) The automorphisms of \(\mathbb F_{1^n}\) are the maps \(z\mapsto z^a\) with \(a\) prime to \(n\). They form a
  group isomorphic to \((\mathbb Z/n\mathbb Z)^\times\).

*Proof.* A morphism \(f\) satisfies \(f(z)f(z^{-1})=1\) for \(z\in\mu_m\), so \(f(\mu_m)\subseteq\mu_n\), and \(f\)
restricts to a group homomorphism. Conversely a group homomorphism extends by \(0\mapsto 0\). The cyclic group
\(\mu_n\) has a subgroup of order \(m\) exactly when \(m\) divides \(n\), and then only one. The endomorphisms of a
cyclic group of order \(n\) are the power maps, and \(z\mapsto z^a\) is bijective exactly when \(a\) is prime to
\(n\). ∎

Compare with finite fields: \(\mathbb F_{q^m}\) embeds in \(\mathbb F_{q^n}\) exactly when \(m\) divides \(n\).

**Definition 8.3.** A *vector space over \(\mathbb F_{1^n}\)* is a finite set \(V\) with an element \(0\in V\) and
an action of the group \(\mu_n\) on \(V\) such that \(\zeta\cdot 0=0\) for all \(\zeta\), and such that \(\mu_n\)
acts freely on \(V\setminus\{0\}\): if \(\zeta v=v\) and \(v\ne 0\), then \(\zeta=1\). For \(n=1\) this is a finite
pointed set.

- The *dimension* of \(V\) is the number of orbits of \(\mu_n\) in \(V\setminus\{0\}\). A *basis* is a set of
  representatives of these orbits.
- A *subspace* is a subset that contains \(0\) and is stable under \(\mu_n\).
- A *linear map* \(f\colon V\to V'\) is a map with \(f(0)=0\) and \(f(\zeta v)=\zeta f(v)\) such that
  \(f(v)=f(v')\ne 0\) implies \(v=v'\). Its *kernel* is \(f^{-1}(0)\).
- The *standard space* of dimension \(d\) is \(\{0\}\sqcup(\mu_n\times\Omega_d)\), with
  \(\zeta\cdot(\eta,i)=(\zeta\eta,i)\) and the basis \(e_i=(1,i)\).
- The *projective space* of \(V\) is \(\mathbb P(V)=(V\setminus\{0\})/\mu_n\).

Linear maps are closed under composition: if \(g(f(v))=g(f(v'))\ne 0\), then \(f(v)=f(v')\ne 0\), and so
\(v=v'\). The condition that \(f\) is injective away from its kernel is the one used for the category of finite
pointed sets in [López Peña–Lorscheid 2011a, §1.3]. It makes the rank formula in (e) below true.

**Theorem 8.4 (linear algebra over \(\mathbb F_{1^n}\)).** Let \(V\) be a vector space of dimension \(d\) over
\(\mathbb F_{1^n}\).

- (a) \(|V|=dn+1\), and \(V\) is isomorphic to the standard space of dimension \(d\).
- (b) \(V\) has \(\prod_{i=0}^{d-1}n(d-i)=n^d\,d!\) ordered bases.
- (c) The group \(\mathrm{GL}_d(\mathbb F_{1^n})\) of automorphisms of \(V\) has order \(n^d\,d!\). After the
  choice of a basis it is the group of \(d\times d\) monomial matrices whose non-zero entries lie in \(\mu_n\),
  that is, the wreath product \(\mu_n^d\rtimes S_d\). For \(n=1\) it is \(S_d\).
- (d) \(V\) has \(\binom{d}{k}\) subspaces of dimension \(k\) and \(d!\) complete flags of subspaces, for every
  \(n\). The projective space \(\mathbb P(V)\) has \(d\) elements, for every \(n\).
- (e) For a linear map \(f\colon V\to V'\), the kernel and the image are subspaces, and
  \(\dim V=\dim\ker f+\dim f(V)\).

*Proof.* (a) Every orbit in \(V\setminus\{0\}\) has \(n\) elements. If \(v_1,\dots,v_d\) is a basis, every non-zero
element is \(\zeta v_i\) for unique \(\zeta\) and \(i\), and \(\zeta v_i\mapsto(\zeta,i)\) is an isomorphism to the
standard space. (b) The first basis vector is any of the \(dn\) non-zero elements. The next one is any element
outside \(\{0\}\) and the orbits already used. (c) For two ordered bases \((v_i)\) and \((v'_i)\) there is exactly
one automorphism with \(v_i\mapsto v'_i\), namely \(\zeta v_i\mapsto\zeta v'_i\). So the order is the number of
ordered bases. Fix a basis. An automorphism \(f\) satisfies \(f(v_i)=\zeta_iv_{\sigma(i)}\) with
\(\zeta_i\in\mu_n\) and a permutation \(\sigma\). Let \(M(f)\) be the complex matrix with
\(M(f)e_i=\zeta_ie_{\sigma(i)}\). If \(g(v_i)=\eta_iv_{\tau(i)}\), then
\(f(g(v_i))=\eta_i\zeta_{\tau(i)}v_{\sigma\tau(i)}\), so \(M(f\circ g)=M(f)M(g)\). The map \(M\) is injective, and
every monomial matrix with entries in \(\mu_n\cup\{0\}\) occurs. By Lemma 5.1(a), applied to these matrices, the
group is the semidirect product of the diagonal matrices \(\mu_n^d\) with the permutation matrices. (d) A subspace
is \(\{0\}\) together with a union of orbits, so a subspace of dimension \(k\) is a choice of \(k\) of the \(d\)
orbits, and a complete flag is an ordering of the orbits. The elements of \(\mathbb P(V)\) are the orbits. (e) The
kernel and the image contain \(0\) and are stable under \(\mu_n\). The map \(f\) restricts to a bijection from
\(V\setminus\ker f\) to \(f(V)\setminus\{0\}\) that commutes with \(\mu_n\). Count orbits. ∎

Compare with \(\mathbb F_q\): a space of dimension \(d\) has \(q^d\) elements, \(\prod_i(q^d-q^i)\) ordered bases,
\(\binom{d}{k}_q\) subspaces of dimension \(k\), \([d]_q!\) complete flags and \([d]_q\) points in its projective
space. The numbers in (d) are the values at \(q=1\). The numbers in (a)–(c) are not values at \(q=1\) of the
corresponding polynomials. They are their terms of low order in \(q-1\), with \(q-1\) replaced by \(n\):
\(q^d=1+d(q-1)+\dots\) gives \(1+dn\), and \(\prod_i(q^d-q^i)=d!\,(q-1)^d+\dots\) gives \(d!\,n^d\). Corollary 8.6
explains this.

Two remarks on the definition. First, without the injectivity condition the map from a space of dimension \(2\)
onto a space of dimension \(1\) that sends both basis vectors to the basis vector would be linear, with kernel
\(\{0\}\); then (e) fails. Second, the standard space is not a Cartesian power. The set \(\mathbb F_{1^n}^d\) of
\(d\)-tuples has \((n+1)^d\) elements. The standard space of dimension \(d\) is its subset of tuples with at most
one non-zero coordinate.

**Proposition 8.5 (base change to a ring).** Let \(k\) be a non-zero ring and \(\chi\colon\mu_n\to k^\times\) a
group homomorphism. For a vector space \(V\) over \(\mathbb F_{1^n}\) let \(V_k\) be the quotient of the free
\(k\)-module with basis \(\{[v]: v\in V\setminus\{0\}\}\) by the submodule generated by the elements
\([\zeta v]-\chi(\zeta)[v]\).

- (a) If \(v_1,\dots,v_d\) is a basis of \(V\), then \([v_1],\dots,[v_d]\) is a basis of the \(k\)-module \(V_k\).
  So \(V_k\) is free of rank \(\dim V\).
- (b) A linear map \(f\colon V\to V'\) induces a \(k\)-linear map \(f_k\colon V_k\to V'_k\) with
  \([v]\mapsto[f(v)]\), where \([0]=0\). An automorphism with \(f(v_i)=\zeta_iv_{\sigma(i)}\) induces the monomial
  matrix with the entry \(\chi(\zeta_i)\) in position \((\sigma(i),i)\). If \(\chi\) is injective, then
  \(f\mapsto f_k\) is an injective homomorphism from \(\mathrm{GL}_d(\mathbb F_{1^n})\) to \(\mathrm{GL}_d(k)\).
- (c) A subspace \(V'\subseteq V\) of dimension \(k'\) gives the submodule of \(V_k\) spanned by \(k'\) of the basis
  vectors \([v_i]\), for a basis of \(V\) that contains a basis of \(V'\). Inclusions are preserved.

*Proof.* (a) Every non-zero element of \(V\) is \(\zeta v_i\) for unique \(\zeta,i\). The \(k\)-linear map from the
free module to \(k^d\) with \([\zeta v_i]\mapsto\chi(\zeta)e_i\) sends the generators of the submodule to \(0\),
because \(\chi\) is a homomorphism. So it induces \(\varphi\colon V_k\to k^d\). The map
\(\psi\colon k^d\to V_k\), \(e_i\mapsto[v_i]\), satisfies \(\varphi\psi=1\), and
\(\psi\varphi([\zeta v_i])=\chi(\zeta)[v_i]=[\zeta v_i]\). (b) The map \(f_k\) is well defined because
\([f(\zeta v)]-\chi(\zeta)[f(v)]=[\zeta f(v)]-\chi(\zeta)[f(v)]=0\) in \(V'_k\). The matrix is read off from (a). It
determines \(\sigma\), because units of a non-zero ring are not zero, and it determines the \(\zeta_i\) if \(\chi\)
is injective. (c) follows from (a). ∎

The case \(n=1\) is the passage from a pointed set to the free module on its non-zero elements, and from a
permutation to its permutation matrix. The universal case is the ring
\[
R_n=\mathbb Z[\mu_n]=\mathbb Z[T]/(T^n-1),
\]
the group ring of \(\mu_n\), with \(\chi\) the inclusion \(\mu_n\subset R_n^\times\) that sends a generator to
\(T\). This is the ring that [Soulé 1999, §4.1] and [Soulé 2004, §2.4] take as
\(\mathbb F_{1^n}\otimes_{\mathbb F_1}\mathbb Z\); [López Peña–Lorscheid 2011a, Introduction] describes it as the
group ring of the cyclic group of order \(n\). A field \(\mathbb F_q\) admits an injective \(\chi\) exactly when
\(n\) divides \(q-1\), by (B1).

**Corollary 8.6 (\(\mathbb F_q\) without its addition).** Let \(q\) be a prime power and \(n=q-1\). An
isomorphism \(\chi\colon\mu_n\to\mathbb F_q^\times\), extended by \(0\mapsto 0\), is an isomorphism from the monoid
\(\mathbb F_{1^{q-1}}\) to the multiplicative monoid of \(\mathbb F_q\). Base change along \(\chi\) is an
isomorphism from \(\mathrm{GL}_d(\mathbb F_{1^{q-1}})\) to the group \(N(\mathbb F_q)\) of monomial matrices in
\(\mathrm{GL}_d(\mathbb F_q)\). Its order \(d!\,(q-1)^d\) is the term of lowest order at \(q=1\) in
\(|\mathrm{GL}_d(\mathbb F_q)|\).

*Proof.* The isomorphism \(\chi\) exists by (B1). By Proposition 8.5(b) base change is injective with image the
monomial matrices with non-zero entries in \(\chi(\mu_n)=\mathbb F_q^\times\), which are all monomial matrices.
The last statement is Proposition 6.3(c). ∎

So \(\mathbb F_{1^n}\) is what is left of the field with \(n+1\) elements when the addition is forgotten, in the
cases where \(n+1\) is a prime power; and it is defined for every \(n\). For \(n=2\) the group
\(\mathrm{GL}_d(\mathbb F_{1^2})\) is the group of monomial matrices with entries \(0,\pm1\), which is also the
group of monomial matrices in \(\mathrm{GL}_d(\mathbb Z)\) (Exercise 7). This is the extension of the Weyl group by
signs from the end of Section 7.

**Proposition 8.7 (the ring \(R_n\)).** Let \(R_n=\mathbb Z[T]/(T^n-1)\).

- (a) \(R_n\) is a free \(\mathbb Z\)-module with basis \(1,T,\dots,T^{n-1}\).
- (b) For \(n\ge 2\), \(R_n\) is not an integral domain.
- (c) \(a+bT\mapsto(a+b,a-b)\) is an isomorphism from \(R_2\) to the ring of pairs \((x,y)\in\mathbb Z^2\) with
  \(x\equiv y\) modulo \(2\).
- (d) The elements of finite multiplicative order in \(R_n\) are the \(2n\) elements \(\pm T^i\),
  \(0\le i<n\).

*Reference:* [Soulé 2004, §6.2] uses (d) without proof. It is the cyclic case of a consequence of a theorem of
Higman: for a finite abelian group \(A\), the group of units of the group ring \(\mathbb Z[A]\) is the product of
\(\pm A\) and a free abelian group [Higman 1940]; so its elements of
finite order are the elements \(\pm a\) with \(a\in A\).

*Proof.* (a) Division with remainder by the monic polynomial \(T^n-1\). (b)
\((T-1)(1+T+\dots+T^{n-1})=0\) in \(R_n\), and both factors are non-zero by (a). (c) The map is the pair of the
evaluations at \(T=1\) and \(T=-1\), so it is a ring homomorphism. It is injective, and \((x,y)\) is in the image
exactly when \((x+y)/2\) and \((x-y)/2\) are integers. (d) The elements \(\pm T^i\) have finite order and are
distinct by (a). Conversely let \(u=\sum_{i=0}^{n-1}a_iT^i\) with \(u^m=1\) for some \(m\ge 1\). For every
\(\omega\in\mu_n\) the evaluation \(T\mapsto\omega\) is a ring homomorphism \(R_n\to\mathbb C\), so
\(u(\omega)^m=1\) and \(|u(\omega)|=1\). Since \(\sum_{\omega\in\mu_n}\omega^{i-j}\) is \(n\) for \(i=j\) and \(0\)
for \(i\ne j\) (with \(0\le i,j<n\)),
\[
n=\sum_{\omega\in\mu_n}|u(\omega)|^2=\sum_{i,j}a_ia_j\sum_{\omega\in\mu_n}\omega^{i-j}=n\sum_ia_i^2 .
\]
So \(\sum_ia_i^2=1\). The \(a_i\) are integers, so one of them is \(\pm 1\) and the others are \(0\). ∎

The ring \(R_2\) has a simple geometric description, noted in [Connes–Consani 2011a, §2.4]. Every prime ideal of
\(R_2\) contains \(T-1\) or \(T+1\), because their product is \(0\). The quotients \(R_2/(T-1)\) and \(R_2/(T+1)\)
are both \(\mathbb Z\), and \(R_2/(T-1,T+1)=\mathbb Z/2\). So the set of prime ideals of \(R_2\) is the union of two
copies of the set of prime ideals of \(\mathbb Z\), and the two copies have exactly the prime \(2\) in common.

By (d), the monoid \(\mathbb F_{1^n}\) is smaller than the monoid of \(0\) and all roots of unity of its base change
\(R_n\): the sign \(-1\) is a root of unity in \(R_n\) for every \(n\), and it is not a power of \(T\). This has a
consequence for counting points.

**Proposition 8.8 (points of projective space with coordinates in a group with zero).** Let \(D\) be a finite
abelian group and \(D_0=D\cup\{0\}\) the monoid obtained by adding an absorbing element. For \(d\ge 0\) put
\[
\mathbb P^d(D_0)=\big(D_0^{d+1}\setminus\{(0,\dots,0)\}\big)/D ,
\]
where \(D\) acts by multiplication on all coordinates. For \(0\le k\le d\) let \(\mathbb P^d(D_0)^{(k)}\) be the
set of classes with exactly \(k+1\) non-zero coordinates. Let \(N(q)=[d+1]_q\). Then
\[
|\mathbb P^d(D_0)^{(k)}|=\binom{d+1}{k+1}|D|^k,\qquad |\mathbb P^d(D_0)|=\frac{(|D|+1)^{d+1}-1}{|D|}=N(|D|+1),
\]
and \(N(q)=\sum_{k=0}^{d}\binom{d+1}{k+1}(q-1)^k\). In particular \(\mathbb P^d(D_0)^{(0)}\) has
\(d+1=N(1)\) elements for every \(D\).

*Proof.* The action of \(D\) on the non-zero tuples is free: if \(\lambda x=x\) and \(x_i\ne 0\), then
\(\lambda x_i=x_i\) in the group \(D\), so \(\lambda=1\). The tuples with non-zero coordinates exactly at a set
\(Y\) of \(k+1\) indices form a copy of \(D^{k+1}\), with \(|D|^k\) orbits. Sum over \(Y\), and then over \(k\),
using \(\sum_{k}\binom{d+1}{k+1}x^k=((1+x)^{d+1}-1)/x\). ∎

The proposition contains four counts of "the points of \(\mathbb P^d\) over \(\mathbb F_1\)".

- For \(D=\mathbb F_q^\times\), \(D_0\) is the monoid of \(\mathbb F_q\) and \(\mathbb P^d(D_0)\) is
  \(\mathbb P^d(\mathbb F_q)\), with \(N(q)\) points.
- For \(D=\mu_n\), so \(D_0=\mathbb F_{1^n}\), there are \(N(n+1)\) points. This is the count of
  [Connes–Consani 2011a, §3, §3.4 and §5]: the number of points over \(\mathbb F_{1^n}\) is the value of the
  counting polynomial at \(q=n+1\), and the sets \(\mathbb P^d(D_0)^{(k)}\) are the graded pieces defined there. For
  \(n=1\) there are \(N(2)=2^{d+1}-1\) points, one for each non-empty subset of the coordinates. These are the
  points of the projective space over \(\mathbb F_1\) described in [Lorscheid 2018b, Remark 2.7]; the lesson
  *Monoid schemes* treats this space.
- The piece of degree \(0\) has \(N(1)=d+1\) points for every \(n\): the coordinate points. This is the set of
  \(d+1\) points on which Tits defines projective geometry of dimension \(d\) over the field of
  characteristic one. It is also the projective space \(\mathbb P(V)\) of a vector space of dimension
  \(d+1\) in Theorem 8.4(d).
- In [Soulé 1999, §5.3 and §6] and [Soulé 2004, §5.2.4 and §6] the coordinates are \(0\) and the roots of unity of
  the ring \(R_n\). By Proposition 8.7(d) this is a group with zero with \(2n\) non-zero elements. Two coordinate
  vectors of this kind define the same point with values in \(R_n\) exactly when they differ by a unit of \(R_n\)
  [Stacks, Tag [01ND](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/constructions.html#constructions-section-projective-space)], and such a unit is a root of unity, because it is the quotient of two non-zero coordinates.
  So Proposition 8.8 applies, and the count is \(N(2n+1)\), in agreement with [Soulé 2004, Théorème 2]. Accordingly
  [Soulé 1999, §6] puts \(q=2n+1\) and lets \(N(q)\) be the number of points with values
  in \(R_n\). For \(n=1\) the count is \(N(3)=(3^{d+1}-1)/2\). [Connes–Consani 2011a, §1] points out that this
  number is not \(d+1\).

So the last three counts are values of the same polynomial \(N\): Tits's count \(d+1\) is the value at \(1\); the count of [Connes–Consani 2011a] for \(\mathbb F_{1^n}\) is the value at \(n+1\); and the count
of [Soulé 1999] and [Soulé 2004] for \(\mathbb F_{1^n}\) is the value at \(2n+1\). A requirement about counting
points has to say which rule is meant; see (R3) below.

**Remark 8.9 (other objects called \(\mathbb F_{1^n}\)).** In [Lorscheid 2018b, Example 2.11] the extension
\(\mathbb F_{1^n}\) is a blueprint whose underlying monoid is \(\{0\}\cup\mu_n\) and whose associated ring is the
subring \(\mathbb Z[\zeta_n]\) of \(\mathbb C\) generated by a primitive \(n\)-th root of unity. This ring is a
quotient of \(R_n\) by \(T\mapsto\zeta_n\). It is an integral domain, so by Proposition 8.7(b) it is a proper
quotient for \(n\ge 2\). For \(n=2\) it is \(\mathbb Z\), with \(T\mapsto -1\): there the element \(-1\) of
\(\mathbb F_{1^2}\) is the additive inverse of \(1\). [Connes–Consani 2011a, §2.4] uses the same quotient for
\(n=2\). The lesson *Blueprints and blue schemes* treats the blueprint version.

## 9. What a geometry over \(\mathbb F_1\) is asked to provide

The sections above contain theorems about finite fields, finite sets and pointed sets with a group action. None
of them needs a field with one element. The task of a geometry over \(\mathbb F_1\) is to make these theorems
consequences of one theory, in which the objects over \(\mathbb F_1\) and the objects over \(\mathbb Z\) or
\(\mathbb F_q\) are related by base change. The following list states what is asked. The references are named with
each item.

A *candidate theory* consists of a category \(\mathcal C\), whose objects we call *objects over \(\mathbb F_1\)*,
and a rule which assigns to every object \(X\) a scheme \(X_{\mathbb Z}\) over \(\mathbb Z\). A *model* of a scheme
\(Y\) is an object \(X\) of \(\mathcal C\) with an isomorphism \(X_{\mathbb Z}\cong Y\). A scheme \(Y\) of finite
type over \(\mathbb Z\) defines the finite sets \(Y(\mathbb F_q)\), and so it may have a counting polynomial
\(N_Y\) (Definition 6.1). If it has one, \(r\) denotes its order at \(q=1\) and \(a_r\) its leading coefficient at
\(q=1\).

- **(R1) Base change.** The rule \(X\mapsto X_{\mathbb Z}\) extends to a functor from \(\mathcal C\) to schemes
  over \(\mathbb Z\). It plays the role of \(X\otimes_{\mathbb F_1}\mathbb Z\).
  *References:* [Soulé 1999, §2]; [Soulé 2004, Introduction and §2.1]; [Lorscheid 2018b, §1].
- **(R2) Models.** The following schemes have models: (a) affine spaces, split tori and projective
  spaces; (b) toric varieties; (c) Grassmannians and flag varieties; (d) split reductive group schemes, in
  particular \(\mathrm{GL}_m\) and \(\mathrm{SL}_m\).
  *References:* [Soulé 1999, §2], which asks which varieties over \(\mathbb Z\) are obtained by base change from
  \(\mathbb F_1\); [Soulé 2004, §2.1 and §5.4]; [Connes–Consani 2011a, §1].
- **(R3) Counting.** Let \(X\) be a model of a scheme \(Y\) that has a counting polynomial \(N_Y\).
  (a) The theory attaches to \(X\) finite sets \(X(\mathbb F_{1^n})\), \(n\ge 1\), and there is a function \(c\),
  the same for all \(X\), with \(|X(\mathbb F_{1^n})|=N_Y(c(n))\). The rule is \(c(n)=n+1\) in
  [Connes–Consani 2011a, §3 and §5] and \(c(n)=2n+1\) in [Soulé 1999, §6] and [Soulé 2004, §6.1].
  (b) The theory singles out in \(X(\mathbb F_{1^n})\), or attaches to \(X\) in another way, a finite set of
  *points of lowest degree* over \(\mathbb F_{1^n}\) with \(a_r\,n^r\) elements. For \(n=1\) this number is the
  leading coefficient \(a_r\). For \(\mathbb P^{m-1}\), for the Grassmannian of \(k\)-dimensional subspaces of
  \(m\)-space and for the variety of complete flags in \(m\)-space, where \(r=0\), the set has \(m\),
  \(\binom{m}{k}\) and \(m!\) elements for every \(n\), and it is identified with the set of elements, of
  \(k\)-element subsets, and of complete flags of subsets of \(\Omega_m\).
  *References:* [Soulé 1999, §6]; [Soulé 2004, §6.1]; [Connes–Consani 2011a, §1 and §3].
- **(R4) Groups.** Let \(G\) be a split reductive group scheme over \(\mathbb Z\) with Weyl group \(W\).
  (a) \(G\) has a model \(\mathcal G\). (b) The category \(\mathcal C\), or a category with the same objects and
  more morphisms, has products that are preserved by base change, and \(\mathcal G\) is a group object whose
  multiplication has the multiplication of \(G\) as its base change. (c) The set of points of lowest degree of
  \(\mathcal G\) over \(\mathbb F_1\), in the sense of (R3)(b), is a group under this multiplication, and it is
  isomorphic to \(W\). For \(G=\mathrm{GL}_m\) it is \(S_m\).
  *References:* [Soulé 1999, §1 and §5.5]; [Manin 1995, §1.6]; [Soulé 2004, §1.1 and §5.4];
  [Connes–Consani 2011a, §1]; [Lorscheid 2018b, §3.2]; [López Peña–Lorscheid 2011a, §2.12].
- **(R5) Homogeneous spaces and incidence.** The action of \(\mathrm{GL}_m\) on a Grassmannian is the base change
  of an action of the model of \(\mathrm{GL}_m\) on the model of the Grassmannian. On the sets of (R3)(b) for
  \(n=1\) it induces the action of \(S_m\) on the \(k\)-element subsets of \(\Omega_m\), and the incidence between
  subspaces of different dimensions induces inclusion of subsets. So the theory recovers the geometry
  \(\Sigma(\Omega_m)\) of Section 7 with its automorphism group.
  *References:* [Lorscheid 2018b, §1.1 and §3.2].
- **(R6) Extensions.** For every \(n\ge 1\) there is a base change from \(\mathbb F_1\) to \(\mathbb F_{1^n}\),
  and objects over \(\mathbb F_{1^n}\) have a base change to schemes over
  \(\mathbb Z[T]/(T^n-1)\). Linear algebra over \(\mathbb F_{1^n}\) is that of Section 8: the points of lowest
  degree of \(\mathrm{GL}_d\) over \(\mathbb F_{1^n}\), in the sense of (R3)(b), form the group
  \(\mu_n^d\rtimes S_d\), which has \(d!\,n^d\) elements.
  *References:* [Soulé 1999, §4.1]; [Soulé 2004, §2.4 and §3.8.2]; [Connes–Consani 2011a, §1 and §2.4];
  [López Peña–Lorscheid 2011a, Introduction].
- **(R7) The integers.** The spectrum of \(\mathbb Z\) is itself an object over \(\mathbb F_1\), not of finite
  type; it has a completion that includes the archimedean place; and the product of two copies of it over
  \(\mathbb F_1\) exists and is not again a copy of it. This product is to play the role of the surface
  \(C\times C\) in Weil's proof for a curve \(C\) over a finite field.
  *References:* [Manin 1995, §0], which asks for a category in which the powers
  \(\operatorname{Spec}\mathbb Z\times\dots\times\operatorname{Spec}\mathbb Z\) can be defined;
  [Soulé 1999, §2] and [Soulé 2004, §1.2 and §2.1], which explain why \(\operatorname{Spec}\mathbb Z\) cannot be of
  finite type over \(\mathbb F_1\) and do not try to define the product; [Lorscheid 2018b, §1.2];
  [López Peña–Lorscheid 2011a, §1.4], which reports that in the theory of [Durov 2007] the product of the completed
  spectrum with itself is the completed spectrum again.
- **(R8) Zeta functions.** An object whose base change has a counting polynomial \(N\) has a zeta function that
  is computed from \(N\). [Manin 1995, §1.6] introduces an absolute Tate motive with zeta function
  \((s-1)/2\pi\), imagined as the motive of an affine line over the absolute point
  \(\operatorname{Spec}\mathbb F_1\), and gives the absolute point the zeta function \(s/2\pi\). In
  [Soulé 2004, §6.3] the zeta function of the point is \(s\), that of the affine line is \(s-1\), and that of
  \(\mathbb P^d\) is \(s(s-1)\cdots(s-d)\); the last formula is already in [Soulé 1999, §1 and §6]. Up to the
  factors \(2\pi\) these agree with the functions of [Manin 1995, §1.6], which are zeta functions of motives: in
  [Manin 1995, §1.1] the zeta function of the motive of the projective line over \(\mathbb F_q\) is the inverse of
  the zeta function of the line. [Connes–Consani 2011a, §1] replaces the definition of [Soulé 2004] by its
  inverse, so that the projective line gets \(1/(s(s-1))\).
- **(R9) K-theory.** The algebraic K-theory of \(\mathbb F_1\), built from the groups
  \(\mathrm{GL}_d(\mathbb F_1)=S_d\), is given in degrees \(i\ge 1\) by the stable homotopy groups of spheres.
  *References:* [Manin 1995, §1.6]; [Soulé 1999, §1]; [Soulé 2004, §7.1]; [Lorscheid 2018b, §1].

The requirements (R1)–(R6) are about the material of this lesson. The requirements (R7)–(R9) are stated for
completeness. (R7) is the subject of the lesson *Weil's proof for curves and what is missing over the integers*.
The zeta functions of (R8) are treated in the lessons *Monoid schemes* and *Varieties over the field with one
element after Soulé and Connes–Consani*.

**What this lesson has shown.** At the level of sets and linear algebra, the parts of (R3)–(R6) that speak about
sets of points hold for the general linear group, with finite pointed sets in the place of objects over
\(\mathbb F_1\):

- base change of vector spaces is Proposition 8.5;
- the sets of (R3)(b) for \(n=1\) are the sets of subsets and of flags of subsets, by Theorem 6.2; they are the
  sets of \(B\)-orbits, by Theorems 4.2 and 7.5 and Corollary 5.6, and over a field with at least three elements
  they are also the sets of points fixed by the torus, by Proposition 4.4;
- the count (R3)(a) with \(c(n)=n+1\) holds for projective space, and so does (R3)(b) for every \(n\), by
  Proposition 8.8;
- the groups of points of lowest degree are \(S_m\) and \(\mu_n^d\rtimes S_d\), by Theorems 7.4 and 8.4 and
  Proposition 6.3, and for \(n=q-1\) they are the groups of monomial matrices over \(\mathbb F_q\), by
  Corollary 8.6.

What is missing is the geometry: objects whose base change is the scheme \(\mathrm{GL}_m\) or the Grassmannian
itself, and morphisms whose base change is the group law. Proposition 7.7 shows one obstacle to (R4): in general
the Weyl group cannot be lifted to a subgroup of \(G(\mathbb Z)\). For \(\mathrm{SL}_2\), the monomial matrices in
\(\mathrm{SL}_2(\mathbb Z)\) form a cyclic group of order \(4\), and no subgroup of it maps isomorphically onto its
quotient by \(\{\pm 1\}\), which is the Weyl group.

**Remark 9.1 (what the references establish; not proved in this lesson).**

- [Soulé 2004, Théorème 1] constructs models of smooth toric varieties in the sense of that paper, and
  [Soulé 2004, §5.4] leaves (R2)(c) and (R2)(d) open.
- [Lorscheid 2018b, §2.1 and §2.2] explains that the only varieties obtained by base change from monoid schemes
  are toric varieties, by a theorem of [Deitmar 2008], so that semisimple groups have no models among them. The
  theorem has hypotheses on the monoid scheme itself. The lessons *Monoid schemes* and *Torified varieties and the
  limits of monoid schemes* give the exact statements.
- [Connes–Consani 2011a, Theorem 4.10] shows that Chevalley group schemes define varieties over
  \(\mathbb F_{1^2}\) in the sense of that paper, with the counting rule \(c(n)=n+1\). The same paper states at its
  end that the group law is not defined over \(\mathbb F_{1^2}\) there, and that the terms of lowest degree form
  the extension of the Weyl group constructed in [Tits 1966]. By [Connes–Consani 2011a, Theorem 4.3], for the
  coefficients \(\{\pm 1\}\) this extension is the group of integral points of the normalizer of the torus; for
  \(\mathrm{GL}_d\) that is the group of Exercise 7, because an invertible integral matrix that normalizes the
  group of diagonal matrices over \(\mathbb Q\) is monomial by Lemma 5.1(b).
- [López Peña–Lorscheid 2011a, Theorem 2.6], quoting [Lorscheid 2012b], states that for every split reductive
  group scheme \(G\) with Weyl group \(W\) there is a group object \(\mathcal G\), for a suitable notion of
  morphism, with \(\mathcal G_{\mathbb Z}\cong G\) as group schemes and \(\mathcal G(\mathbb F_1)\cong W\) as
  groups.
- [Lorscheid 2018b, Theorems 3.7 and 3.8] state the corresponding results for blueprints. Theorem 3.7 is quoted
  there from [Lorscheid 2018a], and Theorem 3.8 from [Lorscheid 2018a] and [Lorscheid 2016]. The lesson
  *Blueprints and blue schemes* treats them.

The last lesson of the course, *What a unified theory must contain*, returns to requirements of this kind and
tests the approaches against them.

## 10. Exercises

**Exercise 1 (symmetry of the coefficients).** Show that \(q^{k(n-k)}\binom{n}{k}_{1/q}=\binom{n}{k}_q\), so that
the coefficients of \(q^j\) and of \(q^{k(n-k)-j}\) in \(\binom{n}{k}_q\) are equal. Give a second proof with
Corollary 4.3, by an involution \(S\mapsto S'\) of the \(k\)-element subsets of \(\Omega_n\) with
\(d(S')=k(n-k)-d(S)\).

*Solution.* We have \([m]_{1/q}=q^{-(m-1)}[m]_q\), so \([m]_{1/q}!=q^{-\binom{m}{2}}[m]_q!\). Hence
\(\binom{n}{k}_{1/q}=q^{-\binom{n}{2}+\binom{k}{2}+\binom{n-k}{2}}\binom{n}{k}_q\), and
\(\binom{n}{2}-\binom{k}{2}-\binom{n-k}{2}=k(n-k)\): this is the number of pairs with one element in a fixed
\(k\)-element subset of \(\Omega_n\) and one outside. For the second proof let \(S'=\{n+1-s: s\in S\}\). If
\(S=\{s_1<\dots<s_k\}\), the elements of \(S'\) in increasing order are \(s'_i=n+1-s_{k+1-i}\). Then
\(d(S)=\sum_js_j-\tfrac{k(k+1)}{2}\) and \(d(S')=k(n+1)-\sum_js_j-\tfrac{k(k+1)}{2}\), so
\(d(S)+d(S')=k(n+1)-k(k+1)=k(n-k)\).

**Exercise 2 (the \(q\)-binomial theorem).** Show that for \(n\ge 0\)
\[
\prod_{i=0}^{n-1}(1+q^ix)=\sum_{k=0}^{n}q^{\binom{k}{2}}\binom{n}{k}_q\,x^k .
\]
Deduce that \(\sum_{k=0}^n(-1)^kq^{\binom{k}{2}}\binom{n}{k}_q=0\) for \(n\ge 1\). What do the two identities say at
\(q=1\)?

*Solution.* Induction on \(n\); the case \(n=0\) is \(1=1\). Multiply the identity for \(n\) by \(1+q^nx\). The
coefficient of \(x^k\) becomes
\[
q^{\binom{k}{2}}\binom{n}{k}_q+q^{n}q^{\binom{k-1}{2}}\binom{n}{k-1}_q
=q^{\binom{k}{2}}\Big(\binom{n}{k}_q+q^{\,n+1-k}\binom{n}{k-1}_q\Big)=q^{\binom{k}{2}}\binom{n+1}{k}_q ,
\]
because \(\binom{k-1}{2}+n=\binom{k}{2}+n+1-k\), and by the second Pascal rule for \(n+1\). For \(x=-1\) the
product contains the factor \(1-q^0=0\). At \(q=1\) the identities are the binomial theorem
\((1+x)^n=\sum_k\binom{n}{k}x^k\) and \(\sum_k(-1)^k\binom{n}{k}=0\).

**Exercise 3 (complements).** Let \(U\subseteq\mathbb F_q^n\) be a subspace of dimension \(k\). Show that \(U\) has
exactly \(q^{k(n-k)}\) complements, that is, subspaces \(U'\) with \(U\oplus U'=\mathbb F_q^n\). So there are
\(q^{k(n-k)}\binom{n}{k}_q\) pairs of complementary subspaces of dimensions \(k\) and \(n-k\). What does this say at
\(q=1\)?

*Solution.* Let \(\pi\colon\mathbb F_q^n\to Q=\mathbb F_q^n/U\) be the quotient map. A subspace \(U'\) is a
complement exactly when \(\pi\) restricts to an isomorphism \(U'\to Q\). So complements correspond to linear maps
\(\sigma\colon Q\to\mathbb F_q^n\) with \(\pi\sigma=1\), by \(U'=\sigma(Q)\). If \(\sigma_0\) is one such map, the
others are \(\sigma_0+\varphi\) with \(\varphi\colon Q\to U\) linear, and there are \(q^{k(n-k)}\) such
\(\varphi\). At \(q=1\) the number of pairs is \(\binom{n}{k}\): a subset has exactly one complement. The cell of
highest dimension in Theorem 4.2 is of this kind: \(C_{\{n-k+1,\dots,n\}}\) is the set of complements of
\(E_{n-k}\).

**Exercise 4 (maps of given rank).** Let \(a,b\ge 0\) and \(0\le r\le\min(a,b)\).

- (a) Show that the number of linear maps \(\mathbb F_q^a\to\mathbb F_q^b\) of rank \(r\) is
  \(\binom{a}{r}_q\prod_{i=0}^{r-1}(q^b-q^i)\).
- (b) Let \(V\) and \(V'\) be vector spaces over \(\mathbb F_{1^n}\) of dimensions \(a\) and \(b\). Show that the
  number of linear maps \(V\to V'\) whose image has dimension \(r\) is \(\binom{a}{r}\,n^r\,b(b-1)\cdots(b-r+1)\).
- (c) Compare (b) for \(n=q-1\) with the term of lowest order at \(q=1\) in (a).

*Solution.* (a) A map of rank \(r\) has a kernel \(K\) of dimension \(a-r\); there are
\(\binom{a}{a-r}_q=\binom{a}{r}_q\) choices. The map is then an injective linear map
\(\mathbb F_q^a/K\to\mathbb F_q^b\), that is, a linearly independent \(r\)-tuple in \(\mathbb F_q^b\), and there are
\(\prod_{i<r}(q^b-q^i)\) of these. (b) By Theorem 8.4(e) the kernel \(K\) is a subspace of dimension \(a-r\);
there are \(\binom{a}{r}\) choices. Choose a basis of \(V\) that contains a basis of \(K\), and let
\(v_1,\dots,v_r\) be its elements outside \(K\). The map is determined by \(f(v_1),\dots,f(v_r)\). These are
non-zero and lie in different orbits: if \(f(v_i)=\zeta f(v_j)=f(\zeta v_j)\), then \(v_i=\zeta v_j\), so \(i=j\).
Conversely any such choice defines a linear map. There are \(nb\cdot n(b-1)\cdots n(b-r+1)\) choices. (c) We have
\(\prod_{i<r}(q^b-q^i)=(q-1)^rq^{\binom{r}{2}}[b]_q[b-1]_q\cdots[b-r+1]_q\). So the term of lowest order in (a) is
\(\binom{a}{r}\,b(b-1)\cdots(b-r+1)\,(q-1)^r\), which is (b) with \(n=q-1\). For \(n=1\), \(a=b=2\) the numbers
for \(r=0,1,2\) are \(1,4,2\): these are the \(7\) injective maps from a subset of a set with two elements into a
set with two elements.

**Exercise 5 (cells in \(\mathrm{GL}_3\) and the big cell).**

- (a) Let \(F\) be any field and
  \(g=\begin{pmatrix}1&2&0\\0&1&1\\0&1&2\end{pmatrix}\in\mathrm{GL}_3(F)\). Find \(w\), \(u\in U_w\) and \(b\in B\)
  with \(g=uP_wb\).
- (b) Let \(w_0(a)=n+1-a\). Show that \(g\in\mathrm{GL}_n(F)\) lies in \(BP_{w_0}B\) if and only if, for
  \(j=1,\dots,n-1\), the minor of \(g\) on the rows \(n-j+1,\dots,n\) and the columns \(1,\dots,j\) is not zero.
  How many elements does this cell have over \(\mathbb F_q\)?

*Solution.* (a) \(\det g=1\). Follow the proof of Theorem 5.4. Column \(1\) has its only non-zero entry in row
\(1\), so \(i_1=1\) and nothing is changed. In column \(2\), among the rows \(2,3\) the lowest non-zero entry is in
row \(3\), so \(i_2=3\); subtract row \(3\) from row \(2\), which gives the row \((0,0,-1)\). Then \(i_3=2\). So
\(w(1)=1\), \(w(2)=3\), \(w(3)=2\), \(\ell(w)=1\), \(\Phi_w=\{(2,3)\}\), and
\[
u=x_{23}(1)=\begin{pmatrix}1&0&0\\0&1&1\\0&0&1\end{pmatrix},\qquad
P_wb=\begin{pmatrix}1&2&0\\0&0&-1\\0&1&2\end{pmatrix},\qquad
b=\begin{pmatrix}1&2&0\\0&1&2\\0&0&-1\end{pmatrix}.
\]
(b) By the proof of Theorem 5.4, \(g\in BP_wB\) exactly when \(r_{ij}(g)=r_{ij}(P_w)\) for all \(i,j\), because
these numbers are constant on double cosets and distinguish them. For \(w_0\),
\(r_{ij}(P_{w_0})=|\{c\le j: n+1-c\ge i\}|=\min(j,n+1-i)\). If \(g\) is in the cell, then
\(r_{n-j+1,j}(g)=j\), which says that the minor is not zero. Conversely, if all these minors are non-zero, then
for \(j\le n+1-i\) the submatrix on the rows \(i,\dots,n\) and the columns \(1,\dots,j\) has the invertible
\(j\times j\) block on the rows \(n-j+1,\dots,n\) inside it, so its rank is \(j\); and for \(j>n+1-i\) it contains
the invertible square block on the rows \(i,\dots,n\) and the columns \(1,\dots,n+1-i\), so its rank is \(n+1-i\)
(for \(i=1\) this block is \(g\)). The cell has \(q^{\binom{n}{2}}|B|=(q-1)^nq^{n(n-1)}\) elements.

**Exercise 6 (inversions).** Prove \(\sum_{w\in S_n}q^{\ell(w)}=[n]_q!\) directly.

*Solution.* Write \(w\) as the word \(w(1)\cdots w(n)\). Deleting the letter \(n\) gives a permutation \(w'\) of
\(\Omega_{n-1}\), and \(w\) is recovered from \(w'\) and the position \(p\in\{1,\dots,n\}\) of the letter \(n\).
The letter \(n\) is larger than all others, so it forms inversions exactly with the \(n-p\) letters to its right,
and the other inversions are those of \(w'\). Hence
\(\sum_{w\in S_n}q^{\ell(w)}=(1+q+\dots+q^{n-1})\sum_{w'\in S_{n-1}}q^{\ell(w')}\), and the claim follows by
induction.

**Exercise 7 (signs).**

- (a) Show that the monomial matrices in \(\mathrm{GL}_d(\mathbb Z)\) are the monomial matrices with non-zero
  entries \(\pm 1\). Show that they form a group of order \(2^dd!\) which is isomorphic to
  \(\mathrm{GL}_d(\mathbb F_{1^2})\) and to the group of monomial matrices in \(\mathrm{GL}_d(\mathbb F_3)\).
- (b) Show that the group in (a) is the set of integral matrices \(g\) with \(g^{\mathsf T}g=1\), that is, the
  intersection of \(\mathrm{GL}_d(\mathbb Z)\) with the orthogonal group.
- (c) In the situation of Proposition 7.7 with \(F=\mathbb F_q\), show that there is a subgroup of \(N'\) that
  maps isomorphically onto \(N'/T'\) if and only if \(q\) is even.

*Solution.* (a) A monomial matrix \(P_wt\) with integer entries has determinant \(\pm\prod_jt_j\). It is invertible
over \(\mathbb Z\) exactly when this is \(\pm 1\), that is, when all \(t_j=\pm 1\). These matrices are the monomial
matrices with entries in \(\mu_2\cup\{0\}\), which is \(\mathrm{GL}_d(\mathbb F_{1^2})\) by Theorem 8.4(c).
Reduction modulo \(3\) is a group homomorphism that maps them bijectively to the monomial matrices over
\(\mathbb F_3\), because \(\mathbb F_3^\times=\{\pm1\}\); this is Corollary 8.6 for \(q=3\). (b) Let \(g\) be integral with
\(g^{\mathsf T}g=1\). Every column of \(g\) is an integral vector whose squares of entries have sum \(1\), so it is
\(\pm e_i\) for some \(i\). Two different columns are orthogonal, so they belong to different indices \(i\). Hence
\(g\) is monomial with entries \(\pm 1\). The converse is clear. Since integral matrices are real, the group is
also the intersection of \(\mathrm{GL}_d(\mathbb Z)\) with the unitary group, which is the standard maximal
compact subgroup of \(\mathrm{GL}_d(\mathbb C)\); so it is the group of [Soulé 1999, §5.5] for \(\mathrm{GL}_d\).
(c) If \(q\) is even, then \(-1=1\), the matrix \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\) has determinant \(1\) and
order \(2\), and with the identity it forms such a subgroup. If \(q\) is odd, Proposition 7.7 applies.

**Exercise 8 (towers).** Let \(m,n\ge 1\) and regard \(\mathbb F_{1^n}\) as a submonoid of \(\mathbb F_{1^{mn}}\)
(Proposition 8.2). Let \(V\) be a vector space of dimension \(d\) over \(\mathbb F_{1^{mn}}\).

- (a) Show that \(V\), with the action restricted to \(\mu_n\), is a vector space of dimension \(md\) over
  \(\mathbb F_{1^n}\). In particular \(\mathbb F_{1^{mn}}\) has dimension \(m\) over \(\mathbb F_{1^n}\), and
  \(\mathbb F_{1^n}\) has dimension \(n\) over \(\mathbb F_1\).
- (b) Compare the numbers of points of \(\mathbb P(V)\) over the two monoids, and compare with
  \(\mathbb F_q\subseteq\mathbb F_{q^m}\).

*Solution.* (a) The subgroup \(\mu_n\) of \(\mu_{mn}\) acts freely on \(V\setminus\{0\}\), which has \(dmn\)
elements, so there are \(dm\) orbits. For \(V=\mathbb F_{1^{mn}}\) we have \(d=1\). (b) Over \(\mathbb F_{1^{mn}}\)
the projective space has \(d\) points, over \(\mathbb F_{1^n}\) it has \(md\) points: every point over the larger
monoid is a union of \(m\) points over the smaller one. A vector space of dimension \(d\) over \(\mathbb F_{q^m}\)
has dimension \(md\) over \(\mathbb F_q\), with \([d]_{q^m}\) and \([md]_q\) points in the projective spaces, and
\([md]_q=[m]_q\,[d]_{q^m}\): every point over the larger field is a projective space with \([m]_q\) points over the
smaller one. At \(q=1\) this is \(md=m\cdot d\).

## What this lesson does not prove

- **The background (B1)–(B4)** of Section 1.
- **The statements of Tits's paper** about the geometries of general Chevalley groups. They are
  reported in Section 7, together with the accounts of them in [Soulé 1999, §1], [Soulé 2004, §1.1],
  [Connes–Consani 2011a, §1] and [Lorscheid 2018b, §1.1]. The lesson proves the case of the general linear group.
  The same holds for the description in [Soulé 1999, §5.5] of the integral points of a Chevalley group in the
  maximal compact subgroup; the lesson proves the case of \(\mathrm{GL}_d\) (Exercise 7).
- **Remark 6.5**: for a smooth toric variety the value \(N(1)\) is the Euler–Poincaré characteristic of the space
  of complex points, [Soulé 2004, Théorème 2].
- **The theorem of Higman** [Higman 1940]: for a finite abelian group
  \(A\), the group of units of \(\mathbb Z[A]\) is the product of \(\pm A\) and a free abelian group. The lesson
  proves the consequence that it uses, for a cyclic group: the elements of finite order of
  \(\mathbb Z[T]/(T^n-1)\) are the elements \(\pm T^i\) (Proposition 8.7(d)).
- **The results quoted in Remark 9.1**: [Soulé 2004, Théorème 1]; the theorem of [Deitmar 2008] as used in
  [Lorscheid 2018b, §2.1]; [Connes–Consani 2011a, Theorem 4.10]; [López Peña–Lorscheid 2011a, Theorem 2.6], which
  is [Lorscheid 2012b, Theorem 7.9]; [Lorscheid 2018b, Theorems 3.7 and 3.8]. Also the identification of the
  group of lowest degree with the extension of [Tits 1966], [Connes–Consani 2011a, Theorem 4.3].
- **The facts behind (R7)–(R9)**: the statement about the product in the theory of [Durov 2007], reported in
  [López Peña–Lorscheid 2011a, §1.4]; the zeta functions of [Manin 1995, §1.6], [Soulé 1999, §6] and
  [Soulé 2004, §6]; and the theorem of Barratt, Priddy and Quillen which identifies the homotopy groups in degrees
  \(i\ge 1\) of the plus construction of the classifying space of the infinite symmetric group with the stable
  homotopy groups of spheres, used in [Soulé 1999, §1] and [Soulé 2004, §7.1].

## References

Section, theorem and equation numbers of [Connes–Consani 2011a], [López Peña–Lorscheid 2011a], [Lorscheid 2018b]
and [Soulé 2004] refer to the arXiv versions. Tits's 1957 paper is cited by its numbered paragraphs ("no."); the beginning
of its no. 13, which [Soulé 2004, §1.1] and [Connes–Consani 2011a, §1] cite as §13, is reproduced in [Lorscheid–Thas 2023].

- [Soulé 2004] C. Soulé, *Les variétés sur le corps à un élément*, Mosc. Math. J. 4 (2004), no. 1, 217–244.
  [arXiv:math/0304444](https://arxiv.org/pdf/math/0304444).
- [Soulé 1999] C. Soulé, *On the field with one element*, talk at the Arbeitstagung, Bonn, June 1999, preprint
  IHES/M/99/55. Free at https://www.mpim-bonn.mpg.de/preblob/175 (the Arbeitstagung notes, DVI file)
- [Connes–Consani 2011a] A. Connes, C. Consani, *On the notion of geometry over \(\mathbb F_1\)*, J. Algebraic
  Geom. 20 (2011), no. 3, 525–557. arXiv:0809.2926. Free at https://alainconnes.org/wp-content/uploads/GeomoverF1.pdf
- [López Peña–Lorscheid 2011a] J. López Peña, O. Lorscheid, *Mapping \(\mathbb F_1\)-land: an overview of
  geometries over the field with one element*, in: Noncommutative geometry, arithmetic, and related topics, Johns
  Hopkins Univ. Press, Baltimore, 2011, 241–265. [arXiv:0909.0069](https://arxiv.org/pdf/0909.0069).
- [Lorscheid 2018b] O. Lorscheid, *\(\mathbb F_1\) for everyone*, [arXiv:1801.05337](https://arxiv.org/pdf/1801.05337).
- [Lorscheid 2012b] O. Lorscheid, *Algebraic groups over the field with one element*, Math. Z. 271 (2012),
  117–138. [arXiv:0907.3824](https://arxiv.org/pdf/0907.3824).
- [Lorscheid 2018a] O. Lorscheid, *The geometry of blueprints. Part II: Tits–Weyl models of algebraic groups*,
  [arXiv:1201.1324](https://arxiv.org/pdf/1201.1324).
- [Lorscheid 2016] O. Lorscheid, *A blueprinted view on \(\mathbb F_1\)-geometry*, in: Absolute arithmetic and
  \(\mathbb F_1\)-geometry, edited by K. Thas, European Mathematical Society, 2016. [arXiv:1301.0083](https://arxiv.org/pdf/1301.0083).
- [Deitmar 2008] A. Deitmar, *\(\mathbb F_1\)-schemes and toric varieties*, Beiträge Algebra Geom. 49 (2008),
  no. 2, 517–525. [arXiv:math/0608179](https://arxiv.org/pdf/math/0608179).
- [Durov 2007] N. Durov, *New approach to Arakelov geometry*, [arXiv:0704.2030](https://arxiv.org/pdf/0704.2030).
- [Stacks] The [Stacks project](https://stacks.math.columbia.edu/), cited by tag. Each tag links to the same place in [AI Integrated Stacks Project](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/), the programme's edition of the Stacks project, which agrees with it modulo corrections made by GPT-6 Astra (OpenAI, Ultra setting) on suggestions of GPT-5.6 Sol (OpenAI, Ultra setting). Of the tags cited in this lesson, Tag 09HW carries such corrections: wording, notation and small precisions in statements and proofs. None of them changes the results used here.
- [Tits 1966] J. Tits, *Normalisateurs de tores. I. Groupes de Coxeter étendus*, J. Algebra 4 (1966), 96–116. Free at https://doi.org/10.1016/0021-8693(66)90053-6
- [Chevalley 1955] C. Chevalley, *Sur certains groupes simples*, Tôhoku Math. J. (2) 7 (1955), 14–66. Free at https://doi.org/10.2748/tmj/1178245104
- [Manin 1995] Yu. Manin, *Lectures on zeta functions and motives (according to Deninger and Kurokawa)*,
  Astérisque 228 (1995), 121–163. Free at https://www.numdam.org/item/AST_1995__228__121_0/
- [Higman 1940] G. Higman, *Units in group rings*, DPhil thesis, University of Oxford, 1940. Free at https://doi.org/10.5287/ora-bmo6o5bjx
- [Lorscheid–Thas 2023] O. Lorscheid, K. Thas, *Towards the horizons of Tits's vision: on band schemes, crowds and \(\mathbb F_1\)-structures*, [arXiv:2305.13809](https://arxiv.org/pdf/2305.13809).
