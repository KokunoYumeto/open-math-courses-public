# Entropy of finite-dimensional subalgebras

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October revisions are self-checked by the writing AI. Public domain (CC0).*

## Introduction

In classical ergodic theory the entropy of a measure-preserving transformation \(T\) is built from the entropy
\(H(\mathcal P)=-\sum_A\mu(A)\log\mu(A)\) of a finite partition and from the join
\(\mathcal P\vee T^{-1}\mathcal P\vee\dots\vee T^{-k}\mathcal P\). A finite partition amounts to a
finite-dimensional subalgebra of \(L^\infty(X,\mu)\), and the join corresponds to the algebra that the pieces generate.
In a noncommutative finite von Neumann algebra \(R\) with a trace \(\tau\), two finite-dimensional subalgebras usually
generate an infinite-dimensional algebra, so there is no join. This lesson builds a replacement: a number
\(H(N_1,\dots,N_k)\) attached to any finite family of finite-dimensional subalgebras, which behaves like the entropy of
the join, together with a relative entropy \(H(N\mid P)\).

The lesson has three parts.

1. **Definitions and algebraic properties** (Sections 3–5). We define the joint entropy (Definition 3.1) and prove
   that it is monotone (Proposition 3.3), subadditive (Proposition 3.4), and does not grow when several arguments are
   merged into one algebra containing them (Proposition 3.5). For one algebra it is the entropy of the trace on a
   maximal family of orthogonal minimal projections (Theorem 4.1), and for commuting families it is the entropy of the
   generated algebra (Theorem 4.4). The relative entropy (Definition 5.1) satisfies a triangle inequality and controls
   the change of the joint entropy when the arguments are moved (Propositions 5.2 and 5.3). For commuting
   subalgebras we compute it (Theorem 5.5), and an example shows that one tempting identity fails (Example 5.6).
2. **Perturbation of subalgebras** (Section 6). If every element of the unit ball of \(N\) lies within \(\delta\), in
   the norm \(\|x\|_2=\tau(x^*x)^{1/2}\), of the unit ball of \(P\), then after cutting \(N\) by a large projection of
   its commutant and conjugating by a unitary close to \(1\) in norm, \(N\) becomes a cut-down of a
   subalgebra of \(P\) (Theorem 6.10).
3. **Continuity** (Section 7). The relative entropy \(H(N\mid P)\) is small when \(N\) is nearly contained in \(P\),
   uniformly in everything except \(\dim N\) (Theorem 7.3). This is the key to the noncommutative Kolmogorov–Sinai
   theorem in the lesson "The entropy of a trace-preserving automorphism".

The later lessons of this course, "The entropy of a trace-preserving automorphism" and "Dynamical entropy of
C\*-algebras and von Neumann algebras", use Definition 3.1, Remark 3.2, Propositions 3.3–3.5, Corollary 3.6,
Theorem 4.1, Corollary 4.2, Theorem 4.4, Definition 5.1, Propositions 5.2 and 5.3, Theorem 5.5, Theorem 7.3 and
Corollary 7.4.

*What is assumed.* Basic von Neumann algebra theory: traces, projections and their comparison, polar decomposition,
the double commutant and Kaplansky density theorems, and the trace-preserving conditional expectation onto a
subalgebra. We also use three classical inequalities of matrix analysis. The facts used are stated precisely in
the next section, "Results used from other lessons", with the place where each is proved.

Basic references are [Connes–Størmer 1975] and [Connes 1994].

## Results used from other lessons

Throughout, \(R\) denotes a von Neumann algebra with a faithful normal tracial state \(\tau\). "Subalgebra"
always means a von Neumann subalgebra containing the unit of \(R\). For \(p\in1,\infty)\) put
\(\|a\|_p=\tau(|a|^p)^{1/p}\), and write \(\|a\|\) for the operator norm.

**(B1) Conditional expectations.** For every subalgebra \(N\subset R\) there is a unique map
\(E_N:R\to N\) that is linear, positive, unital, \(N\)-bimodular (\(E_N(bxc)=bE_N(x)c\) for \(b,c\in N\)) and
satisfies \(\tau\circ E_N=\tau\). It is normal and completely positive. If \(N\subset P\) then
\(E_N\circ E_P=E_N\). On \(L^2(R,\tau)\) it is the orthogonal projection onto \(L^2(N,\tau)\); hence
\(\|x-E_N(x)\|_2\le\|x-y\|_2\) for all \(y\in N\), and \(\|x\|_2^2=\|E_N(x)\|_2^2+\|x-E_N(x)\|_2^2\). Moreover
\(\|E_N(x)\|_1\le\|x\|_1\). Existence, uniqueness, normality, faithfulness, bimodularity and the formula
\(\tau(E_N(x)y)=\tau(xy)\) for \(y\in N\) are [Integration for a trace, Theorem 9.1; complete
positivity is Contractive retractions and the algebraic structure of expectations,
§CE-006. The rest follows: \(E_N\circ E_P\) is a \(\tau\)-preserving normal projection
of norm one onto \(N\), hence equal to \(E_N\) by uniqueness; the formula says that \(x-E_N(x)\) is orthogonal to \(N\) in
\(L^2(R,\tau)\); and \(\|E_N(x)\|_1=\sup\{|\tau(E_N(x)b)|:b\in N,\ \|b\|\le1\}=\sup\{|\tau(xb)|\}\le\|x\|_1\) by (B7).

**(B2) Operator concavity of \(\eta\) and Jensen's operator inequality.** Let \(\eta(t)=-t\log t\) for \(t>0\) and
\(\eta(0)=0\). The function \(\eta\) is operator concave on \([0,\infty)\): for bounded positive operators \(a,b\) and
\(t\in[0,1]\), \(\eta(ta+(1-t)b)\ge t\eta(a)+(1-t)\eta(b)\). Moreover for every unital completely positive map
\(\Phi\) between C\*-algebras and every positive \(a\), \(\eta(\Phi(a))\ge\Phi(\eta(a))\). Proved in Operator
convex functions and the continuity of entropy, Theorem 2.2 and Corollary 3.2, the lesson before this
one, where Jensen's inequality is proved for all unital positive maps and every operator convex function. See also
[Choi 1974] (free at Project Euclid).

**(B3) Operator monotonicity of the logarithm** (the Löwner–Heinz theorem for \(\log\)). If \(a,b\) are bounded
invertible positive operators with \(a\le b\), then \(\log a\le\log b\). Proof: by the Löwner–Heinz inequality
(C\*-algebras, continuous functional calculus, automatic continuity and positive cones, Theorem 9.1),
\((a^\alpha-1)/\alpha\le(b^\alpha-1)/\alpha\) for \(0<\alpha\le1\); these tend in norm to \(\log a\) and \(\log b\) as
\(\alpha\to0\), uniformly on the spectra, which lie in a compact subset of \((0,\infty)\), and the positive cone is
closed.

**(B4) Joint convexity of relative entropy.** Let \(Q\) be a C\*-algebra of finite dimension with a faithful positive
trace \(\varphi\). For positive \(a,b\in Q\) with \(\operatorname{supp}a\le\operatorname{supp}b\) put
\(S_\varphi(a\mid b)=\varphi(a\log a)-\varphi(a\log b)\), where \(\log b\) is computed on the support of \(b\) and
\(0\log0=0\). If \(a_1,\dots,a_r,b_1,\dots,b_r\) are positive with \(\operatorname{supp}a_j\le\operatorname{supp}b_j\),
then
\[
S_\varphi\Bigl(\sum_ja_j\Bigm|\sum_jb_j\Bigr)\le\sum_jS_\varphi(a_j\mid b_j).
\]
(This is joint convexity combined with the homogeneity \(S(\lambda a\mid\lambda b)=\lambda S(a\mid b)\); on a direct
sum of matrix algebras it reduces to the matrix case block by block.) Proved in Entropy defect and abelian models,
Theorem 2.3 and Proposition 2.5(a), a lesson of this course that does not use the present one: for
positive \(a\in Q\), the functional \(\varphi(a\,\cdot\,)\) has relative entropy \(S_\varphi(a\mid b)\) with respect to
\(\varphi(b\,\cdot\,)\) by Theorem 2.3 there, because the scalars by which \(\varphi\) differs from the canonical trace on
the summands cancel, and Proposition 2.5(a) is the stated inequality. See also, e.g., [Lindblad 1974], [Lieb 1973]
(free in the publisher's open archive).

**(B5) Projections in a finite algebra.** For projections \(e,f\in R\), Kaplansky's parallelogram law gives
\(e\vee f-f\sim e-e\wedge f\), hence \(\tau(e\vee f)+\tau(e\wedge f)=\tau(e)+\tau(f)\). If \(e\sim f\) then
\(1-e\sim1-f\), because \(R\) is finite. The parallelogram law is Projections and types of von Neumann algebras,
Proposition 4.4; equivalent projections have equal trace by Traces on von Neumann algebras,
Proposition 2.2; the last statement is Projections and types of von Neumann algebras, Proposition
14.2.

**(B6) Finite-dimensional algebras.** Every finite-dimensional von Neumann algebra \(N\) is isomorphic to
\(\bigoplus_{k=1}^sM_{n_k}(\mathbb C)\); it has a system of matrix units \((e^{(k)}_{ij})\),
\(1\le i,j\le n_k\), \(1\le k\le s\), with \(e^{(k)}_{ij}e^{(l)}_{rs}=\delta_{kl}\delta_{jr}e^{(k)}_{is}\),
\((e^{(k)}_{ij})^*=e^{(k)}_{ji}\) and \(\sum_{k,i}e^{(k)}_{ii}=1\). A tracial linear functional on
\(M_n(\mathbb C)\) is a scalar multiple of the matrix trace. Proved in AF-algebras, Theorem 2.4 and Definition
2.1 for the structure and the matrix units, and Lemma 10.2 there for the traces.

**(B7) Standard facts on the trace norms.** \(|\tau(ab)|\le\|a\|\,\|b\|_1\); \(\|ab\|_p\le\|a\|\,\|b\|_p\) and
\(\|ab\|_p\le\|a\|_p\|b\|\); \(\|a^*\|_p=\|a\|_p\); \(\|a\|_1\le\|a\|_2\le\|a\|\); for \(a\) in a subalgebra \(Q\),
\(\|a\|_1=\sup\{|\tau(ab)|:b\in Q,\ \|b\|\le1\}\). Every \(a\in R\) has a polar decomposition \(a=w|a|\) in \(R\),
and spectral projections of self-adjoint elements of a subalgebra lie in that subalgebra. The image of a von Neumann
algebra under a normal \*-homomorphism is a von Neumann algebra. On bounded subsets of \(R\), strong operator
convergence implies convergence in \(\|\cdot\|_2\). The norm inequalities are proved in Trace densities and
noncommutative integration, §§TI-09–TI-10 and, for \(p=1\), in Traces on von Neumann
algebras, Proposition 7.1; the formula for \(\|a\|_1\) is the duality of Integration for a trace,
Theorem 1.1, applied to \(Q\) with the restriction of \(\tau\); polar decompositions are in The
double commutant theorem, Proposition 7.2; a spectral projection of \(x=x^*\in Q\) commutes with
every operator that commutes with \(x\) (The spectral theorem for bounded self-adjoint operators, Theorem
3.1(5)), so it lies in \(Q''=Q\); the image of a normal \*-homomorphism is a von Neumann algebra by
Spatial tensor products of von Neumann algebras, Theorem 8.2(1). For the last statement, \(\tau\) is
\(\sigma\)-strongly continuous (Compact and trace-class operators, Theorem 9.1(ii)), so
\(\tau=\sum_n\langle\,\cdot\,\xi_n,\xi_n\rangle\) with \(\sum_n\|\xi_n\|^2<\infty\) (The double commutant theorem, Theorem
10.1), and \(\|y_i\|_2^2=\sum_n\|y_i\xi_n\|^2\to0\) for a bounded net \(y_i\to0\) strongly, by the tail
estimate in the proof of Lemma 8.5 of the lesson on trace-class operators.

**(B8) Kaplansky density theorem.** If \(A_0\subset R\) is a unital \*-subalgebra with \(A_0''=R\), then the unit ball
of \(A_0\) is strongly dense in the unit ball of \(R\). Proved in Kaplansky's density theorem and its
consequences, Theorem 7.1.

## 1. Setting and notation

Throughout, \((R,\tau)\) is as in the Background section. We write \(\tau\eta(a)\) for \(\tau(\eta(a))\) and
\(\eta\tau(a)\) for \(\eta(\tau(a))\), for \(a\in R_+\). The following scalar facts are used constantly.

- \(\eta\) is continuous and concave on \([0,\infty)\), \(\eta\ge0\) on \([0,1]\), \(\eta\le1/e\) everywhere.
- For \(s,t\ge0\),
  \[
  \eta(st)=s\,\eta(t)+t\,\eta(s). \tag{1.1}
  \]
  The same identity holds for commuting positive operators: \(\eta(ab)=\eta(a)b+a\eta(b)\) if \(ab=ba\). (Both
  sides are continuous functions on the joint spectrum, and they agree there.)
- \(\eta\) is subadditive on \([0,\infty)\): \(\eta(s+t)\le\eta(s)+\eta(t)\), since a concave function \(g\) with
  \(g(0)=0\) satisfies \(g(s)\ge\frac{s}{s+t}g(s+t)\) and \(g(t)\ge\frac{t}{s+t}g(s+t)\).
- If \(z_1,\dots,z_r\ge0\) have pairwise orthogonal supports (\(z_iz_j=0\) for \(i\ne j\)), then
  \(\eta(\sum_iz_i)=\sum_i\eta(z_i)\).
- The binary entropy \(h(t)=\eta(t)+\eta(1-t)\) is increasing on \([0,\tfrac12]\) and \(h(t)\to0\) as \(t\to0\).
- Let \(\tilde\eta(t)=\eta(t)\) for \(0\le t\le1/e\) and \(\tilde\eta(t)=1/e\) for \(t\ge1/e\). Then
  \(\tilde\eta\) is concave, nondecreasing, \(\eta\le\tilde\eta\), and \(\tilde\eta(t)\to0\) as \(t\to0\).

For a projection \(e\in R\) with \(\tau(e)>0\), the corner \(eRe\) with the tracial state \(\tau_e=\tau(e)^{-1}\tau\) is
again an algebra of our type. For \(z\in(eRe)_+\) we have \(\eta(z)\in eRe\) and \(\tau\eta(z)=\tau(e)\,\tau_e\eta(z)\).

**Finite-dimensional subalgebras.** Consider a finite-dimensional subalgebra \(N\subset R\) with matrix units
\((e^{(k)}_{ij})\) as in (B6), and let \(c_k=\sum_ie^{(k)}_{ii}\) be its minimal central projections. By (B6) the
restriction of \(\tau\) to \(Nc_k\cong M_{n_k}\) is a multiple of the matrix trace, so all minimal projections of \(N\)
below \(c_k\) have the same trace
\[
t_k=\tau(c_k)/n_k>0 .
\]
Every family of pairwise orthogonal minimal projections of \(N\) with sum \(1\) has exactly
\[
M(N)=\sum_kn_k\le\sum_kn_k^2=\dim N
\]
members, \(n_k\) of them below \(c_k\). Let \(\operatorname{Tr}_N\) be the trace on \(N\) that takes the value \(1\) on
every minimal projection, so that \(\operatorname{Tr}_N(1)=M(N)\), and put
\[
D_N=\sum_kt_kc_k,\qquad L_N=\log D_N=\sum_k(\log t_k)\,c_k .
\]
Both lie in the center of \(N\), \(D_N\) is invertible in \(N\), \(0\le D_N\le1\) (as \(t_k\le\tau(1)=1\)), and
\(\tau(a)=\operatorname{Tr}_N(D_Na)\) for \(a\in N\).

**Lemma 1.1.** Let \(N\subset R\) be finite-dimensional. For \(X\in N_+\) put \(\widehat X=D_NX\). Then
\(\widehat X\ge0\), \(\operatorname{Tr}_N(\widehat X)=\tau(X)\), \(\operatorname{Tr}_N|\widehat X-\widehat Y|=\|X-Y\|_1\)
for \(X,Y\in N_+\), and
\[
\tau\eta(X)=\operatorname{Tr}_N\eta(\widehat X)+\tau(L_NX). \tag{1.2}
\]
If \(0\le X\le1\), then \(0\le\widehat X\le1\).

*Proof.* \(D_N\) is central and positive, so \(\widehat X=D_N^{1/2}XD_N^{1/2}\ge0\) and
\(|D_N(X-Y)|=D_N|X-Y|\); applying \(\operatorname{Tr}_N\) gives the two trace identities. Since \(D_N\) and \(X\)
commute, (1.1) gives \(\eta(D_NX)=\eta(D_N)X+D_N\eta(X)\). Now \(\eta(D_N)=-D_NL_N\), so
\(\operatorname{Tr}_N(\eta(D_N)X)=-\operatorname{Tr}_N(D_NL_NX)=-\tau(L_NX)\), while
\(\operatorname{Tr}_N(D_N\eta(X))=\tau\eta(X)\). This is (1.2). If \(X\le1\) then
\(\widehat X=D_N^{1/2}XD_N^{1/2}\le D_N\le1\). \(\square\)

## 2. Trace inequalities for the function \(\eta\)

**Lemma 2.1 (Jensen's inequality for conditional expectations).** Let \(N\subset P\subset R\) be subalgebras and
\(a\in R_+\). Then \(\tau\eta(E_N(a))\ge\tau\eta(E_P(a))\). In particular (take \(N=\mathbb C\))
\(\tau\eta(a)\le\eta\tau(a)\).

*Proof.* Put \(b=E_P(a)\in P_+\); then \(E_N(a)=E_N(b)\) by (B1). By (B2) applied to the unital completely positive
map \(E_N\), \(\eta(E_N(b))\ge E_N(\eta(b))\). Apply \(\tau\) and use \(\tau\circ E_N=\tau\). For \(N=\mathbb C\),
\(E_{\mathbb C}(a)=\tau(a)1\) and \(E_R(a)=a\). \(\square\)

**Lemma 2.2 (subadditivity).** Let \(\varphi\) be a positive trace on a von Neumann algebra \(A\) with
\(\varphi(1)<\infty\). For \(a,b\in A_+\),
\[
\varphi\eta(a+b)\le\varphi\eta(a)+\varphi\eta(b).
\]

*Proof.* For \(\varepsilon>0\) put \(a_\varepsilon=a+\varepsilon\), \(b_\varepsilon=b+\varepsilon\),
\(c_\varepsilon=a_\varepsilon+b_\varepsilon\). These are invertible and \(a_\varepsilon\le c_\varepsilon\), so
\(\log a_\varepsilon\le\log c_\varepsilon\) by (B3). Hence
\[
\varphi(a_\varepsilon\log c_\varepsilon)-\varphi(a_\varepsilon\log a_\varepsilon)
=\varphi\bigl(a_\varepsilon^{1/2}(\log c_\varepsilon-\log a_\varepsilon)a_\varepsilon^{1/2}\bigr)\ge0,
\]
and the same with \(b_\varepsilon\). Adding the two inequalities gives
\(\varphi(a_\varepsilon\log a_\varepsilon)+\varphi(b_\varepsilon\log b_\varepsilon)\le\varphi(c_\varepsilon\log c_\varepsilon)\),
that is \(\varphi\eta(c_\varepsilon)\le\varphi\eta(a_\varepsilon)+\varphi\eta(b_\varepsilon)\). As
\(\varepsilon\to0\), \(\eta(a_\varepsilon)\to\eta(a)\) in norm, because \(\eta\) is uniformly continuous on
\([0,\|a\|+1]\); the same holds for \(b\) and for \(c_\varepsilon\to a+b\). \(\square\)

**Lemma 2.3 (a lower bound for sums).** Let \(\varphi\) be a faithful positive trace on a C\*-algebra \(Q\) of
finite dimension. For \(A,C\in Q_+\) with \(\alpha=\varphi(A)>0\), \(\gamma=\varphi(C)>0\),
\[
\varphi\eta(A+C)\ge\varphi\eta(A)+\varphi\eta(C)+\eta(\alpha+\gamma)-\eta(\alpha)-\eta(\gamma).
\]

*Proof.* By (1.1), \(\varphi\eta(\lambda B)=\lambda\varphi\eta(B)+\eta(\lambda)\varphi(B)\) for \(\lambda>0\). Hence
\(\varphi\eta(A)=\alpha\varphi\eta(A/\alpha)+\eta(\alpha)\), and similarly for \(C\) and \(A+C\). The function
\(B\mapsto\varphi\eta(B)\) is concave on \(Q_+\) by (B2). Writing
\((A+C)/(\alpha+\gamma)=\frac{\alpha}{\alpha+\gamma}\frac A\alpha+\frac{\gamma}{\alpha+\gamma}\frac C\gamma\),
\[
\varphi\eta(A+C)=(\alpha+\gamma)\varphi\eta\Bigl(\frac{A+C}{\alpha+\gamma}\Bigr)+\eta(\alpha+\gamma)
\ge\alpha\varphi\eta\Bigl(\frac A\alpha\Bigr)+\gamma\varphi\eta\Bigl(\frac C\gamma\Bigr)+\eta(\alpha+\gamma),
\]
which is the claim. \(\square\)

The next inequality is the engine behind the merging property of the joint entropy.

**Lemma 2.4 (the two-index inequality).** Let \(Q\) be a C\*-algebra of finite dimension with a faithful positive trace
\(\varphi\). Let \((x_{ij})_{i\in I,j\in J}\) be a finite family in \(Q_+\) with \(\sum_{i,j}x_{ij}=1\), and put
\(x_i^{(1)}=\sum_jx_{ij}\), \(x_j^{(2)}=\sum_ix_{ij}\). Then
\[
\sum_{i,j}\varphi\eta(x_{ij})\le\sum_i\varphi\eta(x^{(1)}_i)+\sum_j\varphi\eta(x^{(2)}_j). \tag{2.1}
\]

*Proof.* Write \(S=S_\varphi\) as in (B4). First we show: if \(y_j\le x_j\) are positive with \(\sum_jx_j=1\), then
\[
\sum_j\varphi\bigl(y_j(\log x_j-\log y_j)\bigr)\le\varphi\eta\Bigl(\sum_jy_j\Bigr). \tag{2.2}
\]
Indeed \(y_j\le x_j\) gives \(\operatorname{supp}y_j\le\operatorname{supp}x_j\), and (B4) gives
\(\sum_jS(y_j\mid x_j)\ge S(\sum_jy_j\mid1)=-\varphi\eta(\sum_jy_j)\), which is (2.2).

Next, for each \(j\) we have \(x_{ij}\le x^{(2)}_j\), so \(\log x^{(2)}_j\) (on its support) may be paired with each
\(x_{ij}\), and by linearity
\(\sum_i\varphi(x_{ij}\log x_j^{(2)})=\varphi(x^{(2)}_j\log x^{(2)}_j)=-\varphi\eta(x^{(2)}_j)\). Therefore
\[
\sum_{i,j}\varphi\eta(x_{ij})-\sum_j\varphi\eta(x^{(2)}_j)=\sum_i\sum_j\varphi\bigl(x_{ij}(\log x^{(2)}_j-\log x_{ij})\bigr).
\]
For fixed \(i\), apply (2.2) with \(y_j=x_{ij}\) and \(x_j=x^{(2)}_j\) (these satisfy \(\sum_jx^{(2)}_j=1\)): the inner
sum is at most \(\varphi\eta(\sum_jx_{ij})=\varphi\eta(x^{(1)}_i)\). Summing over \(i\) gives (2.1). \(\square\)

For \(Q=\mathbb C\) and \(\varphi=\mathrm{id}\), (2.1) is the classical inequality
\(H(I,J)\le H(I)+H(J)\) for a probability array \((p_{ij})\).

**Corollary 2.5.** Let \(Q,\varphi\) be as in Lemma 2.4 and let \((x_{\mathbf i})\), \(\mathbf i=(i_1,\dots,i_n)\in
I_1\times\dots\times I_n\), be a finite family in \(Q_+\) with sum \(1\). For \(1\le l\le n\) and \(j\in I_l\) let
\(x^{(l)}_j=\sum_{\mathbf i:\,i_l=j}x_{\mathbf i}\). Then
\(\sum_{\mathbf i}\varphi\eta(x_{\mathbf i})\le\sum_{l=1}^n\sum_{j\in I_l}\varphi\eta(x^{(l)}_j)\).

*Proof.* Induction on \(n\); \(n=1\) is an equality. For \(n\ge2\) regard \(\mathbf i\) as a pair
\((i_1,\mathbf i')\) with \(\mathbf i'\in I_2\times\dots\times I_n\) and apply (2.1): the left side is at most
\(\sum_{j\in I_1}\varphi\eta(x^{(1)}_j)+\sum_{\mathbf i'}\varphi\eta(y_{\mathbf i'})\), where
\(y_{\mathbf i'}=\sum_{i_1}x_{(i_1,\mathbf i')}\). The family \((y_{\mathbf i'})\) has sum \(1\) and its marginals are
the \(x^{(l)}_j\), \(l\ge2\); apply the induction hypothesis. \(\square\)

**Lemma 2.6 (continuity of entropy in finite dimensions).** Let \(Q\) be a C\*-algebra of finite dimension, \(M=M(Q)\),
and \(\operatorname{Tr}=\operatorname{Tr}_Q\) its canonical trace (value \(1\) on minimal projections). Put
\[
\omega_M(s)=2\tilde\eta(s/2)+(2+\log M)\,s\qquad(s\ge0).
\]
Then \(\omega_M\) is concave, nondecreasing, \(\omega_M(0)=0\), \(\omega_M(s)\to0\) as \(s\to0\), and for
\(A,B\in Q_+\) with \(\operatorname{Tr}A=\operatorname{Tr}B=1\),
\[
|\operatorname{Tr}\eta(A)-\operatorname{Tr}\eta(B)|\le\omega_M(\operatorname{Tr}|A-B|).
\]

*Proof.* The properties of \(\omega_M\) follow from those of \(\tilde\eta\). Every eigenvalue of \(A\) is at most
\(\operatorname{Tr}A=1\), so \(0\le A\le1\), and likewise \(0\le B\le1\). Put \(C=B-A\); then \(-1\le C\le1\). Write
\(C=C_+-C_-\) with \(C_\pm\ge0\), \(C_+C_-=0\). Since \(\operatorname{Tr}C=0\),
\(\operatorname{Tr}C_+=\operatorname{Tr}C_-=r\), where \(2r=\operatorname{Tr}|C|\le2\). Put
\(Y=A+C_+=B+C_-\).

*Claim.* If \(A\ge0\), \(\operatorname{Tr}A=1\), \(0\le C'\le1\) and \(\operatorname{Tr}C'=r\le1\), then
\(|\operatorname{Tr}\eta(A+C')-\operatorname{Tr}\eta(A)|\le\eta(r)+(2+\log M)r\).

For the upper bound, Lemma 2.2 gives \(\operatorname{Tr}\eta(A+C')\le\operatorname{Tr}\eta(A)+\operatorname{Tr}\eta(C')\).
Listing the \(M\) eigenvalues \(\mu_1,\dots,\mu_M\) of \(C'\) with multiplicity, concavity of \(\eta\) gives
\(\operatorname{Tr}\eta(C')=\sum_m\eta(\mu_m)\le M\eta(r/M)=\eta(r)+r\log M\). For the lower bound we may assume
\(r>0\); Lemma 2.3 gives
\(\operatorname{Tr}\eta(A+C')\ge\operatorname{Tr}\eta(A)+\operatorname{Tr}\eta(C')+\eta(1+r)-\eta(1)-\eta(r)\). Here
\(\operatorname{Tr}\eta(C')\ge0\) since the eigenvalues of \(C'\) lie in \([0,1]\), \(\eta(1)=0\), and
\(\eta(1+r)=-(1+r)\log(1+r)\ge-(1+r)r\ge-2r\). So
\(\operatorname{Tr}\eta(A+C')\ge\operatorname{Tr}\eta(A)-2r-\eta(r)\). This proves the claim.

Apply the claim to \((A,C_+)\) and to \((B,C_-)\) (note \(C_\pm\le\|C\|\le1\)):
\(|\operatorname{Tr}\eta(A)-\operatorname{Tr}\eta(B)|\le|\operatorname{Tr}\eta(Y)-\operatorname{Tr}\eta(A)|+|\operatorname{Tr}\eta(Y)-\operatorname{Tr}\eta(B)|\le2\eta(r)+2(2+\log M)r\).
With \(r=\operatorname{Tr}|A-B|/2\) and \(\eta\le\tilde\eta\) this is at most \(\omega_M(\operatorname{Tr}|A-B|)\).
\(\square\)

Inequalities of this type go back to [Fannes 1973].

## 3. The joint entropy

**Definition 3.1.** For \(k\ge1\) let \(\mathcal S_k(R)\) be the set of families \(x=(x_{\mathbf i})\) of elements of
\(R_+\), indexed by \(\mathbf i=(i_1,\dots,i_k)\in I_1\times\dots\times I_k\) for some finite sets \(I_1,\dots,I_k\),
such that \(\sum_{\mathbf i}x_{\mathbf i}=1\). For \(1\le l\le k\) and \(j\in I_l\) the **marginals** are
\[
x^{(l)}_j=\sum_{\mathbf i:\ i_l=j}x_{\mathbf i}.
\]
For finite-dimensional subalgebras \(N_1,\dots,N_k\) of \(R\) and \(x\in\mathcal S_k(R)\) put
\[
\Phi_{N_1,\dots,N_k}(x)=\sum_{\mathbf i}\eta\tau(x_{\mathbf i})-\sum_{l=1}^k\sum_{j\in I_l}\tau\eta\bigl(E_{N_l}(x^{(l)}_j)\bigr),
\tag{3.1}
\]
and define the **joint entropy**
\[
H(N_1,\dots,N_k)=\sup_{x\in\mathcal S_k(R)}\Phi_{N_1,\dots,N_k}(x).
\]
For \(k=1\) this is the **entropy** \(H(N)=\sup_{x\in\mathcal S_1(R)}\sum_i\bigl(\eta\tau(x_i)-\tau\eta(E_N(x_i))\bigr)\).

The first term in (3.1) measures how finely the family \(x\) splits the trace; each subtracted term measures how much
of that splitting survives when the pieces are seen only through one of the algebras. For a partition of unity by
projections in a commutative situation the subtracted terms vanish exactly when the projections lie in the algebras
(Example 4.5 below).

**Remark 3.2.** Let \(N_1,\dots,N_k\) be finite-dimensional subalgebras.

(a) \(H(N_1,\dots,N_k)\ge0\): the one-element family \(x=(1)\) (all \(I_l\) singletons) gives \(\Phi(x)=0\).
Finiteness follows from Corollary 4.2 below.

(b) \(H\) is symmetric in its arguments: permuting the algebras and the index sets together does not change (3.1).

(c) *Invariance.* If \(\theta\) is an automorphism of \(R\) with \(\tau\circ\theta=\tau\), then
\(H(\theta(N_1),\dots,\theta(N_k))=H(N_1,\dots,N_k)\). Indeed \(E_{\theta(N)}=\theta\circ E_N\circ\theta^{-1}\) by the
uniqueness in (B1), \(\eta(\theta(a))=\theta(\eta(a))\), and \(x\mapsto(\theta(x_{\mathbf i}))\) is a bijection of
\(\mathcal S_k(R)\) with \(\Phi_{\theta(N_1),\dots}(\theta(x))=\Phi_{N_1,\dots}(x)\). This applies in particular to
inner automorphisms \(\operatorname{Ad}u\).

(d) *Localization.* If \(Q\subset R\) is a subalgebra containing \(N_1,\dots,N_k\), the supremum may be taken over
\(\mathcal S_k(Q)\). Indeed for \(x\in\mathcal S_k(R)\) the family \(E_Q(x)=(E_Q(x_{\mathbf i}))\) lies in
\(\mathcal S_k(Q)\), \(\tau(E_Q(x_{\mathbf i}))=\tau(x_{\mathbf i})\), the marginals of \(E_Q(x)\) are the
\(E_Q(x^{(l)}_j)\), and \(E_{N_l}\circ E_Q=E_{N_l}\); so \(\Phi(E_Q(x))=\Phi(x)\). Consequently \(H(N_1,\dots,N_k)\)
depends only on the algebra \(Q\) that the \(N_l\) generate and on the restriction of \(\tau\) to it.

**Proposition 3.3 (monotonicity).** If \(N_j\subset P_j\) are finite-dimensional subalgebras, \(1\le j\le k\), then
\(H(N_1,\dots,N_k)\le H(P_1,\dots,P_k)\).

*Proof.* By Lemma 2.1, \(\tau\eta(E_{N_j}(y))\ge\tau\eta(E_{P_j}(y))\) for every \(y\in R_+\). Hence
\(\Phi_{N_1,\dots,N_k}(x)\le\Phi_{P_1,\dots,P_k}(x)\) for every \(x\in\mathcal S_k(R)\). \(\square\)

**Proposition 3.4 (subadditivity).** For finite-dimensional subalgebras \(N_1,\dots,N_p\) and \(1\le k<p\),
\[
H(N_1,\dots,N_p)\le H(N_1,\dots,N_k)+H(N_{k+1},\dots,N_p).
\]

*Proof.* Let \(x\in\mathcal S_p(R)\) and write \(\mathbf i=(\mathbf i',\mathbf i'')\) with
\(\mathbf i'=(i_1,\dots,i_k)\), \(\mathbf i''=(i_{k+1},\dots,i_p)\). Put
\(x'_{\mathbf i'}=\sum_{\mathbf i''}x_{(\mathbf i',\mathbf i'')}\) and
\(x''_{\mathbf i''}=\sum_{\mathbf i'}x_{(\mathbf i',\mathbf i'')}\). Then \(x'\in\mathcal S_k(R)\),
\(x''\in\mathcal S_{p-k}(R)\), and the marginals of \(x'\) and \(x''\) are exactly the marginals of \(x\) (those with
\(l\le k\), respectively \(l>k\)). So the subtracted terms of \(\Phi_{N_1,\dots,N_p}(x)\) are the sum of those of
\(\Phi_{N_1,\dots,N_k}(x')\) and \(\Phi_{N_{k+1},\dots,N_p}(x'')\). For the first terms, the numbers
\(p_{\mathbf i'\mathbf i''}=\tau(x_{(\mathbf i',\mathbf i'')})\) form a probability array with row sums
\(\tau(x'_{\mathbf i'})\) and column sums \(\tau(x''_{\mathbf i''})\), so Lemma 2.4 with \(Q=\mathbb C\) gives
\(\sum_{\mathbf i}\eta\tau(x_{\mathbf i})\le\sum_{\mathbf i'}\eta\tau(x'_{\mathbf i'})+\sum_{\mathbf i''}\eta\tau(x''_{\mathbf i''})\).
Hence \(\Phi_{N_1,\dots,N_p}(x)\le\Phi_{N_1,\dots,N_k}(x')+\Phi_{N_{k+1},\dots,N_p}(x'')\le
H(N_1,\dots,N_k)+H(N_{k+1},\dots,N_p)\). \(\square\)

**Proposition 3.5 (merging).** Let \(N_1,\dots,N_m\) be finite-dimensional subalgebras, \(1\le n\le m\), and suppose
that a finite-dimensional subalgebra \(P\) contains \(N_1,\dots,N_n\). Then
\[
H(N_1,\dots,N_n,N_{n+1},\dots,N_m)\le H(P,N_{n+1},\dots,N_m).
\]

*Proof.* By Proposition 3.3 it suffices to treat \(N_1=\dots=N_n=P\). Let \(x\in\mathcal S_m(R)\), indexed by
\(I_1\times\dots\times I_m\). Put \(J=I_1\times\dots\times I_n\) and regard the same family as an element \(X\) of
\(\mathcal S_{m-n+1}(R)\) indexed by \(J\times I_{n+1}\times\dots\times I_m\). The first terms of
\(\Phi_{P,\dots,P,N_{n+1},\dots}(x)\) and \(\Phi_{P,N_{n+1},\dots}(X)\) coincide, and so do the terms for the
marginals \(l>n\). The first marginal of \(X\) is \(x'_{\mathbf j}=\sum_{i_{n+1},\dots,i_m}x_{(\mathbf j,i_{n+1},\dots,i_m)}\),
\(\mathbf j\in J\). Hence
\[
\Phi_{P,N_{n+1},\dots,N_m}(X)-\Phi_{P,\dots,P,N_{n+1},\dots,N_m}(x)
=\sum_{l=1}^n\sum_{j\in I_l}\tau\eta\bigl(E_P(x^{(l)}_j)\bigr)-\sum_{\mathbf j\in J}\tau\eta\bigl(E_P(x'_{\mathbf j})\bigr).
\]
The family \(y_{\mathbf j}=E_P(x'_{\mathbf j})\) lies in \(P_+\), has sum \(1\), and its \(l\)-th marginal is
\(E_P(x^{(l)}_j)\). Corollary 2.5 in the finite-dimensional algebra \(P\) with the trace \(\tau|_P\) shows that the
right side is \(\ge0\). So \(\Phi_{P,\dots,P,N_{n+1},\dots}(x)\le\Phi_{P,N_{n+1},\dots}(X)\le H(P,N_{n+1},\dots,N_m)\).
\(\square\)

**Corollary 3.6.** Let \(N_1,\dots,N_{k+1},N,P\) be finite-dimensional subalgebras.

1. \(H(N_1,\dots,N_k)\le H(N_1,\dots,N_k,N_{k+1})\).
2. \(H(N_1,\dots,N_k,\mathbb C)=H(N_1,\dots,N_k)\) and \(H(\mathbb C)=0\).
3. \(H(N,N,\dots,N)=H(N)\) for any number of repetitions.
4. If \(N_1,\dots,N_k\subset P\), then \(H(N_1,\dots,N_k)\le H(P)\).

*Proof.* (1) Given \(x\in\mathcal S_k(R)\), extend it to \(\mathcal S_{k+1}(R)\) with \(I_{k+1}=\{*\}\) a singleton and
the same entries. The new marginal is \(1\), and \(\tau\eta(E_{N_{k+1}}(1))=0\); so the value of \(\Phi\) is
unchanged. (2) \(H(\mathbb C)=0\) because \(\tau\eta(E_{\mathbb C}(x_i))=\eta\tau(x_i)\). Then (1) and Proposition 3.4
give \(H(N_1,\dots,N_k)\le H(N_1,\dots,N_k,\mathbb C)\le H(N_1,\dots,N_k)+0\). (3) Proposition 3.5 with \(P=N\) gives
\(\le\), and (1) gives \(\ge\). (4) Proposition 3.5 with \(n=m=k\) gives \(H(N_1,\dots,N_k)\le H(P)\). \(\square\)

## 4. Computing the entropy

**Theorem 4.1.** Let \(N\subset R\) be finite-dimensional and let \((e_\alpha)_{\alpha\in A}\) be pairwise orthogonal
minimal projections of \(N\) with \(\sum_\alpha e_\alpha=1\). Then
\[
H(N)=\sum_{\alpha\in A}\eta\tau(e_\alpha)=\sum_kn_k\,\eta(t_k),
\]
with the notation of Section 1. The supremum defining \(H(N)\) is attained at the family \((e_\alpha)\).

*Proof.* Put \(h=\sum_\alpha\eta\tau(e_\alpha)\); there are \(n_k\) projections of trace \(t_k\) below \(c_k\), so
\(h=\sum_kn_k\eta(t_k)=-\tau(L_N)\).

*The family attains \(h\).* \(E_N(e_\alpha)=e_\alpha\) and \(\eta(e_\alpha)=0\), so the value of the family is \(h\).

*Every family gives at most \(h\).* Let \(x\in\mathcal S_1(R)\) and put \(X_i=E_N(x_i)\in N_+\). Then
\(\sum_iX_i=1\) and \(\tau(X_i)=\tau(x_i)\), so the value of \(x\) is
\(\sum_i(\eta\tau(X_i)-\tau\eta(X_i))\). By Lemma 1.1, with \(\widehat X_i=D_NX_i\),
\[
\sum_i\bigl(\eta\tau(X_i)-\tau\eta(X_i)\bigr)
=\sum_i\bigl(\eta(\operatorname{Tr}_N\widehat X_i)-\operatorname{Tr}_N\eta(\widehat X_i)\bigr)-\tau\Bigl(L_N\sum_iX_i\Bigr).
\]
The last term is \(-\tau(L_N)=h\). Each \(\widehat X_i\) satisfies \(0\le\widehat X_i\le\sum_j\widehat X_j=D_N\le1\);
if \(\mu_1,\mu_2,\dots\) are its eigenvalues (with multiplicity, in the blocks of \(N\)), subadditivity of \(\eta\) gives
\(\operatorname{Tr}_N\eta(\widehat X_i)=\sum_m\eta(\mu_m)\ge\eta(\sum_m\mu_m)=\eta(\operatorname{Tr}_N\widehat X_i)\).
So the value of \(x\) is at most \(h\). \(\square\)

**Corollary 4.2.** For finite-dimensional \(N\) with central weights \(w_k=\tau(c_k)\),
\[
H(N)=\sum_kw_k\log\frac{n_k}{w_k}=H(Z(N))+\sum_kw_k\log n_k,\qquad H(N)\le\log M(N)\le\log\dim N,
\]
where \(Z(N)\) is the center of \(N\). For finite-dimensional \(N_1,\dots,N_k\),
\(0\le H(N_1,\dots,N_k)\le\sum_jH(N_j)\le\sum_j\log\dim N_j<\infty\).

*Proof.* \(n_k\eta(w_k/n_k)=w_k\log(n_k/w_k)\), and \(Z(N)\) is abelian with minimal projections \(c_k\), so
\(H(Z(N))=\sum_k\eta(w_k)\) by Theorem 4.1. The bound \(H(N)\le\log M(N)\) is Jensen's inequality for the concave
\(\eta\) applied to the \(M(N)\) numbers \(\tau(e_\alpha)\), which sum to \(1\). The last chain follows from
Proposition 3.4 and Remark 3.2(a). \(\square\)

**Example 4.3.** (a) For a projection \(e\in R\) and \(N=\mathbb Ce+\mathbb C(1-e)\), \(H(N)=h(\tau(e))\).
(b) If \(N\cong M_n(\mathbb C)\) is a unital matrix subalgebra (for instance in a II₁ factor), every minimal
projection has trace \(1/n\) and \(H(N)=\log n\).
(c) If \(R=L^\infty(X,\mu)\) and \(N\) is the algebra of functions constant on the atoms of a finite measurable
partition \(\mathcal P\), then \(H(N)=-\sum_{A\in\mathcal P}\mu(A)\log\mu(A)\) is the classical entropy of
\(\mathcal P\).

**Theorem 4.4 (commuting families).** Let \(N_1,\dots,N_k\) be finite-dimensional subalgebras and suppose there are
pairwise commuting subalgebras \(P_j\subset N_j\) with \((P_1\cup\dots\cup P_k)''=(N_1\cup\dots\cup N_k)''=:Q\).
Then \(Q\) is finite-dimensional and
\[
H(N_1,\dots,N_k)=H(Q).
\]
In particular \(H(N_1,\dots,N_k)=H((N_1\cup\dots\cup N_k)'')\) whenever the \(N_j\) commute pairwise.

*Proof.* Since the \(P_j\) commute pairwise, the linear span of the products \(p_1p_2\cdots p_k\) (\(p_j\in P_j\)) is a
\*-algebra; it is finite-dimensional, hence equal to \(Q\).

*Upper bound.* Each \(N_j\subset Q\), so \(H(N_1,\dots,N_k)\le H(Q)\) by Corollary 3.6(4).

*Lower bound.* Choose a maximal abelian subalgebra \(A_j\subset P_j\) and let \((e^{(j)}_i)_{i\in I_j}\) be its minimal
projections; they are pairwise orthogonal with sum \(1\). We first check that each \(e=e^{(j)}_i\) is minimal in
\(P_j\). For \(a\in A_j\) we have \(ae=\lambda_ae\) for a scalar \(\lambda_a\), since \(A_je\) is a one-dimensional
algebra. If \(b\in eP_je\), then \(ab=aeb=\lambda_ab\) and \(ba=bea=\lambda_ab\), so \(b\) commutes with \(A_j\) and
lies in \(A_j\) by maximality; thus \(b\in eA_je=\mathbb Ce\). Hence \(eP_je=\mathbb Ce\).

The products \(x_{\mathbf i}=e^{(1)}_{i_1}e^{(2)}_{i_2}\cdots e^{(k)}_{i_k}\) are projections (the factors commute)
with sum \(1\), and their \(l\)-th marginals are \(x^{(l)}_j=e^{(l)}_j\). Each nonzero \(x_{\mathbf i}\) is minimal in
\(Q\): for a spanning element \(p_1\cdots p_k\) of \(Q\),
\[
x_{\mathbf i}\,p_1\cdots p_k\,x_{\mathbf i}=\prod_j\bigl(e^{(j)}_{i_j}p_je^{(j)}_{i_j}\bigr)\in\mathbb Cx_{\mathbf i},
\]
because all factors commute and \(e^{(j)}_{i_j}P_je^{(j)}_{i_j}=\mathbb Ce^{(j)}_{i_j}\). By Proposition 3.3,
\(H(N_1,\dots,N_k)\ge H(A_1,\dots,A_k)\ge\Phi_{A_1,\dots,A_k}(x)\). In \(\Phi\) the subtracted terms vanish, since
\(E_{A_l}(e^{(l)}_j)=e^{(l)}_j\) is a projection. So \(\Phi_{A_1,\dots,A_k}(x)=\sum_{\mathbf i}\eta\tau(x_{\mathbf i})\),
which is \(H(Q)\) by Theorem 4.1 (the zero terms contribute \(\eta(0)=0\)). \(\square\)

**Example 4.5 (the classical case).** If \(R=L^\infty(X,\mu)\) and \(N_j\) corresponds to a finite partition
\(\mathcal P_j\), then Theorem 4.4 and Example 4.3(c) give
\(H(N_1,\dots,N_k)=H(\mathcal P_1\vee\dots\vee\mathcal P_k)\). So the joint entropy extends the entropy of a join.

**Example 4.6 (two masas in unbiased position).** Let \(R=M_2(\mathbb C)\) with the normalized trace, \(A\) the
diagonal matrices, \(u=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix}\), and \(B=uAu^*\). By Corollary 3.6,
\(\log2=H(A)\le H(A,B)\le H(M_2(\mathbb C))=\log2\). So \(H(A,B)=\log2<H(A)+H(B)=2\log2\). Although \(A\) and \(B\) are
"independent" in the sense that \(\tau(ab)=\tau(a)\tau(b)\) for \(a\in A\), \(b\in B\), their joint entropy is no more
than that of the \(2\times2\) matrices they generate. This is the noncommutative effect that the definition is designed
to capture.

## 5. Relative entropy

**Definition 5.1.** For subalgebras \(N,P\subset R\) (not necessarily finite-dimensional) put
\[
H(N\mid P)=\sup_{x\in\mathcal S_1(R)}\sum_i\Bigl(\tau\eta\bigl(E_P(x_i)\bigr)-\tau\eta\bigl(E_N(x_i)\bigr)\Bigr)\in[0,\infty].
\]
Note that \(H(N\mid\mathbb C)=H(N)\) for finite-dimensional \(N\).

**Proposition 5.2.** Let \(N,N',P,P',Q\) be subalgebras of \(R\).

1. \(H(N\mid P)\ge0\), and \(H(N\mid P)=0\) if \(N\subset P\).
2. If \(N\subset N'\) and \(P'\subset P\), then \(H(N\mid P)\le H(N'\mid P')\): the relative entropy increases in
   the first argument and decreases in the second.
3. \(H(N\mid P)\le H(N)\) if \(N\) is finite-dimensional.
4. (Triangle inequality) \(H(N\mid Q)\le H(N\mid P)+H(P\mid Q)\).
5. If \(\theta\) is a \(\tau\)-preserving automorphism, \(H(\theta(N)\mid\theta(P))=H(N\mid P)\).
6. (Localization) If \(Q\) contains \(N\) and \(P\), the supremum may be taken over \(\mathcal S_1(Q)\).

*Proof.* (1) The family \((1)\) gives \(0\). If \(N\subset P\), each term is \(\le0\) by Lemma 2.1. (2) By Lemma 2.1,
\(\tau\eta(E_N(y))\ge\tau\eta(E_{N'}(y))\) and \(\tau\eta(E_P(y))\le\tau\eta(E_{P'}(y))\). (3) Use (2) with
\(P'=\mathbb C\). (4) For \(x\in\mathcal S_1(R)\), split each term as
\([\tau\eta E_Q(x_i)-\tau\eta E_P(x_i)]+[\tau\eta E_P(x_i)-\tau\eta E_N(x_i)]\); all quantities are finite. (5) As in
Remark 3.2(c). (6) As in Remark 3.2(d). \(\square\)

**Proposition 5.3 (moving the arguments).** For finite-dimensional subalgebras \(N_j,P_j\), \(1\le j\le k\),
\[
H(N_1,\dots,N_k)\le H(P_1,\dots,P_k)+\sum_{j=1}^kH(N_j\mid P_j).
\]

*Proof.* For \(x\in\mathcal S_k(R)\),
\(\Phi_{N_1,\dots,N_k}(x)=\Phi_{P_1,\dots,P_k}(x)+\sum_j\sum_{i\in I_j}\bigl(\tau\eta E_{P_j}(x^{(j)}_i)-\tau\eta E_{N_j}(x^{(j)}_i)\bigr)\).
For each \(j\) the marginal family \((x^{(j)}_i)_{i\in I_j}\) belongs to \(\mathcal S_1(R)\), so the inner sum is at most
\(H(N_j\mid P_j)\). \(\square\)

We now compute the relative entropy for commuting algebras. We need to localize at central projections.

**Lemma 5.4 (localization at a central projection).** Fix a subalgebra \(N\subset R\) and a projection
\(c\in N\cap N'\) with \(\tau(c)>0\). Let \(E^c_{Nc}\) be the \(\tau_c\)-preserving conditional expectation of \(cRc\) onto
\(Nc\). Then \(E_N(y)=E^c_{Nc}(y)\) for \(y\in cRc\), and \(E_N(y)c=E_N(cyc)\) for every \(y\in R\).

*Proof.* \(E_N(y)c=cE_N(y)c=E_N(cyc)\) by bimodularity. For \(y\in cRc\), \(E_N(y)=E_N(cyc)=cE_N(y)c\in Nc\), and for
\(b\in Nc\), \(\tau_c(E_N(y)b)=\tau_c(yb)\). By uniqueness in (B1) (applied in \(cRc\)), \(E_N(y)=E^c_{Nc}(y)\).
\(\square\)

**Theorem 5.5 (commuting subalgebras).** Let \(N_1,N_2\subset R\) be commuting finite-dimensional subalgebras and
\(Q=(N_1\cup N_2)''\). Then \(Q\) is finite-dimensional and

1. \(H(N_2\mid N_1)=H(Q)-H(N_1)\);
2. \(H(Q\mid N_1)\ge H(Q)-H(N_1)\), with equality when \(N_1\) is abelian.

*Proof.* \(Q\) is the span of the products \(ab\), \(a\in N_1\), \(b\in N_2\), hence finite-dimensional. Let
\(\mathcal C\) be the set of minimal central projections \(c\) of \(N_1\). Each \(c\) commutes with \(N_1\) and \(N_2\),
so \(c\) is central in \(Q\). For \(c\in\mathcal C\), \(N_1c\) is a factor \(\cong M_{a_c}(\mathbb C)\); let
\((f_{c,r})_{r=1}^{a_c}\) be orthogonal minimal projections of \(N_1c\) with sum \(c\), so \(\tau(f_{c,r})=\tau(c)/a_c\).
Let \((g_s)_{s\in S}\) be orthogonal minimal projections of \(N_2\) with sum \(1\), and put
\(u_{c,s}=\tau(g_sc)/\tau(c)\), so that \(\sum_su_{c,s}=1\).

*Step 1: the number \(H(Q)-H(N_1)\).* For \(g\in N_2\), the functional \(a\mapsto\tau(ag)\) on \(N_1c\) is tracial
(\(\tau(a_1a_2g)=\tau(a_2ga_1)=\tau(a_2a_1g)\)), so by (B6) it equals \(\lambda\tau|_{N_1c}\) with
\(\lambda=\tau(cg)/\tau(c)\):
\[
\tau(fg)=\tau(f)\,\tau(cg)/\tau(c)\qquad(f\in N_1c,\ g\in N_2). \tag{5.1}
\]
The projections \(f_{c,r}g_s\) (for \(c\in\mathcal C\), \(r\le a_c\), \(s\in S\)) have sum \(1\), and each nonzero one
is minimal in \(Q\): for \(a\in N_1\), \(b\in N_2\),
\(f_{c,r}g_s\,ab\,f_{c,r}g_s=(f_{c,r}af_{c,r})(g_sbg_s)\in\mathbb Cf_{c,r}g_s\). By Theorem 4.1 and (5.1),
\[
H(Q)=\sum_{c,s}a_c\,\eta\Bigl(\frac{\tau(c)}{a_c}u_{c,s}\Bigr)
=\sum_{c}\Bigl(\tau(c)\sum_s\eta(u_{c,s})+a_c\eta\Bigl(\frac{\tau(c)}{a_c}\Bigr)\Bigr),
\]
using (1.1) and \(\sum_su_{c,s}=1\). Since \(H(N_1)=\sum_ca_c\eta(\tau(c)/a_c)\),
\[
H(Q)-H(N_1)=\sum_{c\in\mathcal C}\tau(c)\sum_{s\in S}\eta(u_{c,s}). \tag{5.2}
\]

*Step 2: \(H(N_2\mid N_1)\ge\) (5.2).* Use the family \((g_s)\). Since \(g_s\in N_2\), \(\eta(E_{N_2}(g_s))=\eta(g_s)=0\).
Since \(g_s\) commutes with \(N_1\), so does \(E_{N_1}(g_s)\) (for a unitary \(v\in N_1\),
\(vE_{N_1}(g_s)v^*=E_{N_1}(vg_sv^*)=E_{N_1}(g_s)\)), so \(E_{N_1}(g_s)\) is central in \(N_1\):
\(E_{N_1}(g_s)=\sum_cu_{c,s}c\). Hence \(\sum_s\tau\eta(E_{N_1}(g_s))=\sum_{c,s}\tau(c)\eta(u_{c,s})\), which is (5.2).

*Step 3: \(H(N_2\mid N_1)\le\) (5.2).* Let \(\widetilde N_2=(N_2\cup\{c:c\in\mathcal C\})''\); every \(c\in\mathcal C\) is
central in \(\widetilde N_2\) and \(\widetilde N_2c=N_2c\). By Proposition 5.2(2),
\(H(N_2\mid N_1)\le H(\widetilde N_2\mid N_1)\). By Proposition 5.2(6) we may use families \(x\in\mathcal S_1(Q)\). For
such \(x\), the elements \(x_ic\) lie in \(cRc\) and \(\sum_ix_ic=c\). By Lemma 5.4 (applied to \(N_1\) and to
\(\widetilde N_2\)), \(E_{N_1}(x_i)=\sum_cE^c_{N_1c}(x_ic)\) and \(E_{\widetilde N_2}(x_i)=\sum_cE^c_{N_2c}(x_ic)\),
orthogonal sums. Therefore
\[
\sum_i\bigl(\tau\eta E_{N_1}(x_i)-\tau\eta E_{\widetilde N_2}(x_i)\bigr)
=\sum_c\tau(c)\sum_i\bigl(\tau_c\eta E^c_{N_1c}(x_ic)-\tau_c\eta E^c_{N_2c}(x_ic)\bigr)
\le\sum_c\tau(c)H_c(N_2c\mid N_1c),
\]
where \(H_c\) denotes relative entropy in \((cRc,\tau_c)\). By Proposition 5.2(3) and Theorem 4.1 in \((cRc,\tau_c)\),
\(H_c(N_2c\mid N_1c)\le H_c(N_2c)=\sum_s\eta(\tau_c(g_sc))=\sum_s\eta(u_{c,s})\). (The nonzero \(g_sc\) are minimal
projections of \(N_2c\) with sum \(c\), because \(b\mapsto bc\) maps \(N_2\) onto \(N_2c\) with kernel a direct summand.)
This proves (1).

*Step 4: part (2).* \(N_2\subset Q\), so \(H(Q\mid N_1)\ge H(N_2\mid N_1)\) by Proposition 5.2(2). If \(N_1\) is
abelian, then \(a_c=1\), \(N_1c=\mathbb Cc\), and as in Step 3 (with \(Q\) in place of \(\widetilde N_2\)),
\(H(Q\mid N_1)\le\sum_c\tau(c)H_c(Qc)\). By Theorem 4.1 and (1.1),
\(H(Q)=\sum_c\bigl(\tau(c)H_c(Qc)+\eta(\tau(c))\bigr)\) and \(H(N_1)=\sum_c\eta(\tau(c))\). So
\(H(Q\mid N_1)\le H(Q)-H(N_1)\). \(\square\)

When \(N_1\) is not abelian, the inequality in (2) can be strict.

**Example 5.6.** Let \(R=M_2(\mathbb C)\otimes M_2(\mathbb C)\) with the normalized trace, \(N_1=M_2\otimes1\),
\(N_2=1\otimes M_2\), so \(Q=R\), \(H(Q)=\log4\) and \(H(N_1)=\log2\). Let \(\varepsilon_1,\varepsilon_2\) be the standard
basis of \(\mathbb C^2\) and consider the four unit vectors
\[
\xi_\pm=\tfrac1{\sqrt2}(\varepsilon_1\otimes\varepsilon_1\pm\varepsilon_2\otimes\varepsilon_2),\qquad
\zeta_\pm=\tfrac1{\sqrt2}(\varepsilon_1\otimes\varepsilon_2\pm\varepsilon_2\otimes\varepsilon_1).
\]
They form an orthonormal basis, and each satisfies \(\langle(a\otimes1)\xi,\xi\rangle=\frac12(a_{11}+a_{22})\) for
\(a\in M_2\). Let \(q_1,\dots,q_4\) be the corresponding rank-one projections. Then
\(\tau(q_m(a\otimes1))=\frac14\cdot\frac12(a_{11}+a_{22})=\tau(\tfrac14(a\otimes1))\), so \(E_{N_1}(q_m)=\frac14\). The
family \((q_m)\) gives
\[
H(Q\mid N_1)\ge\sum_{m=1}^4\bigl(\tau\eta(E_{N_1}(q_m))-\tau\eta(q_m)\bigr)=4\,\eta(\tfrac14)=\log4 .
\]
Since \(H(Q\mid N_1)\le H(Q)=\log4\), we get \(H(Q\mid N_1)=\log4\), while
\(H(N_2\mid N_1)=H(Q)-H(N_1)=\log2\).

*Reference:* [Connes–Størmer 1975] states \(H(N_2\mid N_1)=H((N_1\cup N_2)''\mid N_1)=H((N_1\cup N_2)'')-H(N_1)\) for
all commuting finite-dimensional \(N_1,N_2\); in Example 5.6, where \(N_1\) and \(N_2\) are full matrix algebras, the
middle term is larger than the other two, so we prove Theorem 5.5 instead.

Next we introduce the operation used to compare a subalgebra with a slightly smaller version of itself.

**Definition 5.7.** For a subalgebra \(N\subset R\) and a projection \(f\in N'\cap R\), put
\[
N^f=\{xf+\lambda(1-f):x\in N,\ \lambda\in\mathbb C\}.
\]
It is the image of \(N\oplus\mathbb C\) under the normal \*-homomorphism \((x,\lambda)\mapsto xf+\lambda(1-f)\), hence a
subalgebra (B7). It contains \(f\), and \(N^ff=Nf\). If \(N\) is finite-dimensional, \(\dim N^f\le\dim N+1\) and
\(M(N^f)\le M(N)+1\). For a unitary \(u\in R\), \(uN^fu^*=(uNu^*)^{ufu^*}\).

**Proposition 5.8 (adjoining commuting abelian pieces).** Fix a subalgebra \(P\subset R\) and a finite-dimensional
abelian subalgebra \(A\subset P'\cap R\) with minimal projections \(a_1,\dots,a_r\). Then
\[
H\bigl((P\cup A)''\mid P\bigr)\le\sum_{j=1}^r\tau\eta\bigl(E_P(a_j)\bigr)\le H(A).
\]
In particular, for a projection \(f\in P'\cap R\), \(H(P^f\mid P)\le h(\tau(f))\).

*Proof.* Put \(Q=(P\cup A)''\). The map \(\pi:(p_j)_j\mapsto\sum_jp_ja_j\) from \(P^{\oplus r}\) to \(R\) is a normal
\*-homomorphism (the \(a_j\) are orthogonal projections commuting with \(P\)); its image is a subalgebra containing \(P\)
and \(A\), so it equals \(Q\). If \(y=\pi((p_j))\ge0\), then also \(y=\pi(((p_j+p_j^*)/2)_+)\); so every \(y\in Q_+\) has
the form \(y=\sum_jp_ja_j\) with \(p_j\in P_+\).

Put \(c_j=E_P(a_j)\). For a unitary \(v\in P\), \(vc_jv^*=E_P(va_jv^*)=c_j\), so \(c_j\) lies in the center of \(P\);
also \(c_j\ge0\) and \(\sum_jc_j=1\). For \(y=\sum_jp_ja_j\in Q_+\):

- the \(p_ja_j\) have orthogonal supports and \(\eta(p_ja_j)=\eta(p_j)a_j\) by (1.1) (as \(\eta(a_j)=0\)), so
  \(\tau\eta(y)=\sum_j\tau(\eta(p_j)a_j)=\sum_j\tau(\eta(p_j)c_j)\), using \(\tau(ba_j)=\tau(bE_P(a_j))\) for
  \(b\in P\);
- \(E_P(y)=\sum_jp_jc_j\), and by Lemma 2.2 and (1.1) (the \(p_j\) and \(c_j\) commute),
  \(\tau\eta(E_P(y))\le\sum_j\tau\eta(p_jc_j)=\sum_j\bigl(\tau(\eta(p_j)c_j)+\tau(p_j\eta(c_j))\bigr)\).

Hence \(\tau\eta(E_P(y))-\tau\eta(E_Q(y))\le\sum_j\tau(p_j\eta(c_j))\) for \(y\in Q_+\).

The right side depends only on \(y\): if \(q\in P\) and \(qa_j=0\), then \(qc_j=E_P(qa_j)=0\), hence \(qc_j^m=0\) for all
\(m\ge1\), and \(q\eta(c_j)=0\) because \(\eta\) is a uniform limit on \([0,1]\) of polynomials vanishing at \(0\).
Now let \(x\in\mathcal S_1(Q)\) (this suffices by Proposition 5.2(6)), \(x_i=\sum_jp_{ij}a_j\). Then
\((\sum_ip_{ij}-1)a_j=0\), so \(\sum_ip_{ij}\eta(c_j)=\eta(c_j)\), and
\[
\sum_i\bigl(\tau\eta E_P(x_i)-\tau\eta(x_i)\bigr)\le\sum_j\tau\eta(c_j)\le\sum_j\eta\tau(c_j)=\sum_j\eta\tau(a_j)=H(A),
\]
by Lemma 2.1 and Theorem 4.1. For the last claim take \(A=\mathbb Cf+\mathbb C(1-f)\) and note
\(P^f\subset(P\cup A)''\). \(\square\)

**Proposition 5.9 (collapsing a corner).** Let \(N\subset R\) be finite-dimensional and \(E\in N'\cap R\) a projection.
Then
\[
H(N\mid N^E)\le H\bigl((N\cup\{E\})''\mid N^E\bigr)\le\tau(1-E)\log M(N).
\]

*Proof.* The first inequality is Proposition 5.2(2). If \(E=1\) both sides vanish, so let \(e=1-E\ne0\). Put
\(Q=(N\cup\{E\})''=NE+Ne\); \(E\) is central in \(Q\) and \(N^E=NE+\mathbb Ce\). For \(y\in Q\),
\[
E_{N^E}(y)=yE+\tau_e(ye)\,e .
\]
Indeed the right side lies in \(N^E\) (as \(yE\in NE\)), and for \(z=bE+\lambda e\in N^E\) both \(y\) and the right side
have trace \(\tau(ybE)+\lambda\tau(ye)\) against \(z\). For \(y\in Q_+\) the pieces \(yE\) and \(ye\) have orthogonal
supports, so
\[
\tau\eta(E_{N^E}(y))-\tau\eta(y)=\tau(e)\bigl(\eta\tau_e(ye)-\tau_e\eta(ye)\bigr).
\]
For \(x\in\mathcal S_1(Q)\), the family \((x_ie)_i\) lies in \((Ne)_+\) and has sum \(e\), so it belongs to
\(\mathcal S_1(eRe)\), and \(E^e_{Ne}(x_ie)=x_ie\). Therefore
\(\sum_i(\eta\tau_e(x_ie)-\tau_e\eta(x_ie))\le H_e(Ne)\), the entropy of \(Ne\) in \((eRe,\tau_e)\). By Corollary 4.2,
\(H_e(Ne)\le\log M(Ne)\le\log M(N)\) (the map \(b\mapsto be\) sends \(N\) onto \(Ne\) and kills a direct summand). By
Proposition 5.2(6) this bounds \(H(Q\mid N^E)\). \(\square\)

## 6. Perturbing a finite-dimensional subalgebra into another

A reference for this section is [Connes–Størmer 1975].

**Definition 6.1.** For subalgebras \(N,P\subset R\) and \(\delta>0\) write \(N\overset{\delta}{\subset}P\) if for every
\(x\in N\) with \(\|x\|\le1\) there is \(y\in P\) with \(\|y\|\le1\) and \(\|x-y\|_2<\delta\).

**Lemma 6.2 (meets of projections).** If \(f_1,\dots,f_r\) are projections below a projection \(q\), then
\(\tau(q-f_1\wedge\dots\wedge f_r)\le\sum_i\tau(q-f_i)\).

*Proof.* For \(r=2\), (B5) gives \(\tau(q-f_1\wedge f_2)=\tau(q)-\tau(f_1)-\tau(f_2)+\tau(f_1\vee f_2)\), and
\(\tau(f_1\vee f_2)\le\tau(q)\). Induction on \(r\). \(\square\)

**Lemma 6.3 (spectral cut).** Let \(a\in R\) be self-adjoint, \(e\in R\) a projection, and
\(q=\chi_{[1/2,\infty)}(a)\). Then \(\|a-q\|_2\le\|a-e\|_2\) and \(\|q-e\|_2\le2\|a-e\|_2\). If \(a\) lies in a
subalgebra \(P\), so does \(q\).

*Proof.* Put \(b=1-2a\), so \(q=\chi_{(-\infty,0]}(b)\) and \(bq=-b_-\). Expanding the squares,
\(\|a-e\|_2^2-\|a-q\|_2^2=\tau(be)-\tau(bq)\). Now \(\tau(be)=\tau(eb_+e)-\tau(b_-^{1/2}eb_-^{1/2})\ge-\tau(b_-)=\tau(bq)\).
The second inequality follows from the triangle inequality. The last claim is (B7). \(\square\)

**Lemma 6.4 (truncated polar decompositions).**

(a) Let \(e\in R\) be a projection and \(y\in R\) with \(y^*y\le e\). Put \(\kappa=\|y^*y-e\|_2\), let \(y=w|y|\) be the
polar decomposition and \(f=\chi_{[1/2,1]}(|y|)\). Then \(f\le e\), \(\|f-e\|_2\le2\sqrt\kappa\) and
\(\|wf-y\|_2\le\sqrt\kappa\).

(b) Let \(P\subset R\) be a subalgebra, \(z\in P\) with \(\|z\|\le1\), and \(u\in R\) a partial isometry with
\(u^*u=e\). Suppose \(\beta=\|z-u\|_2\le1\). Let \(z=w|z|\) be the polar decomposition and
\(g=\chi_{[1/2,1]}(|z|)\). Then \(g\in P\), \(v=wg\in P\) is a partial isometry with \(v^*v=g\), \(g\) is below the
support of \(|z|\), \(vv^*\) is below the range projection of \(z\), and
\[
\|g-e\|_2\le2\sqrt{3\beta},\qquad\|v-u\|_2\le\sqrt{3\beta}+\beta .
\]

*Proof.* (a) From \(y^*y\le e\) we get \(y^*y=ey^*ye\), so \(|y|\) commutes with \(e\) and \(0\le|y|\le e\); in
particular \(f\le e\). Since \(e-|y|\) and \(e+|y|\) are commuting positive elements with \(e-|y|\le e+|y|\),
\(\|e-|y|\|_2^2=\tau((e-|y|)^2)\le\tau((e-|y|)(e+|y|))=\tau(e-y^*y)\le\|e-y^*y\|_1\le\kappa\). By Lemma 6.3,
\(\|f-|y|\|_2\le\sqrt\kappa\) and \(\|f-e\|_2\le2\sqrt\kappa\). Finally \(\|wf-y\|_2=\|w(f-|y|)\|_2\le\sqrt\kappa\).

(b) First, \(\||z|-e\|_2^2\le3\beta\). Indeed, \(\||z|-e\|_2^2=\tau(z^*z)-2\tau(e|z|e)+\tau(e)\), and
\(|z|\ge|z|^2=z^*z\) (as \(\|z\|\le1\)) gives \(\tau(e|z|e)\ge\tau(ez^*ze)\). So
\[
\||z|-e\|_2^2\le\bigl(\tau(z^*z)-\tau(ez^*ze)\bigr)+\bigl(\tau(e)-\tau(ez^*ze)\bigr)
=\|z(1-e)\|_2^2+\bigl(\|ue\|_2^2-\|ze\|_2^2\bigr).
\]
Here \(z(1-e)=(z-u)(1-e)\) has \(\|\cdot\|_2\le\beta\), and
\(\|ue\|_2^2-\|ze\|_2^2\le(\|ue\|_2+\|ze\|_2)\,\|(u-z)e\|_2\le2\beta\). So \(\||z|-e\|_2^2\le\beta^2+2\beta\le3\beta\).

The projection \(g\) lies in \(P\) and is below the support \(w^*w\) of \(|z|\); hence \(v^*v=gw^*wg=g\), and
\(vv^*\le ww^*\). By Lemma 6.3, \(\|g-|z|\|_2\le\sqrt{3\beta}\) and \(\|g-e\|_2\le2\sqrt{3\beta}\). Finally
\(\|v-u\|_2\le\|w(g-|z|)\|_2+\|z-u\|_2\le\sqrt{3\beta}+\beta\). \(\square\)

**Lemma 6.5 (orthogonal projections).** For \(m\ge1\) and \(\varepsilon>0\) define \(\delta_1(\varepsilon)=\varepsilon/2\)
and \(\delta_m(\varepsilon)=\min\{\varepsilon/4,\delta_{m-1}(\varepsilon/(8m))\}\).

(i) Let \(e_1,\dots,e_m\in R\) be pairwise orthogonal projections, \(P\subset R\) a subalgebra, and
\(a_1,\dots,a_m\in P\) with \(\|a_i\|\le1\) and \(\|a_i-e_i\|_2<\delta_m(\varepsilon)\). Then there are pairwise
orthogonal projections \(q_1,\dots,q_m\in P\) with \(\|q_i-e_i\|_2<\varepsilon\).

(ii) If moreover \(\sum_ie_i=1\), \(m\ge2\), and \(\|a_i-e_i\|_2<\delta_{m-1}(\varepsilon/m)\) for \(i<m\), the
\(q_i\) can be chosen with \(\sum_iq_i=1\).

In particular, if \(\mathcal A\subset R\) is an abelian subalgebra with minimal projections \(e_1,\dots,e_m\) and
\(\mathcal A\overset{\delta}{\subset}P\) with \(\delta\le\delta_{m-1}(\varepsilon/m)\), there are projections
\(q_i\in P\) with \(\sum_iq_i=1\) and \(\|q_i-e_i\|_2<\varepsilon\).

*Proof.* (i) Induction on \(m\). Replacing \(a_i\) by \((a_i+a_i^*)/2\) keeps \(\|a_i\|\le1\) and does not increase
\(\|a_i-e_i\|_2\), so let the \(a_i\) be self-adjoint. For \(m=1\), Lemma 6.3 gives \(q_1=\chi_{[1/2,\infty)}(a_1)\) with
\(\|q_1-e_1\|_2\le2\|a_1-e_1\|_2<\varepsilon\). Let \(m\ge2\) and \(\varepsilon_1=\varepsilon/(8m)\). Since
\(\delta_m(\varepsilon)\le\delta_{m-1}(\varepsilon_1)\), the induction hypothesis gives orthogonal projections
\(q_1,\dots,q_{m-1}\in P\) with \(\|q_i-e_i\|_2<\varepsilon_1\). Put \(r=1-\sum_{i<m}q_i\in P\),
\(r_0=1-\sum_{i<m}e_i\), so \(e_m=r_0e_mr_0\) and \(\|r-r_0\|_2<(m-1)\varepsilon_1\). Let \(b=ra_mr\in P\). Then
\[
b-e_m=(r-r_0)a_mr+r_0(a_m-e_m)r+r_0e_m(r-r_0),
\]
so \(\|b-e_m\|_2<2(m-1)\varepsilon_1+\delta_m(\varepsilon)\). Let \(q_m=\chi_{[1/2,\infty)}(b)\in P\). Since
\(b(1-r)=0\), \(q_m\le r\), so \(q_m\) is orthogonal to \(q_1,\dots,q_{m-1}\). By Lemma 6.3,
\(\|q_m-e_m\|_2<4(m-1)\varepsilon_1+2\delta_m(\varepsilon)\le\varepsilon/2+\varepsilon/2\).

(ii) Apply (i) to \(e_1,\dots,e_{m-1}\) with \(\varepsilon/m\), and put \(q_m=1-\sum_{i<m}q_i\). Then
\(\|q_m-e_m\|_2=\|\sum_{i<m}(e_i-q_i)\|_2<(m-1)\varepsilon/m\). The last statement follows, taking \(a_i\in P\) with
\(\|a_i\|\le1\) and \(\|a_i-e_i\|_2<\delta\) (the case \(m=1\) is trivial). \(\square\)

**Lemma 6.6 (approximate matrix units).** Let \(N\subset R\) be a subalgebra with \(\dim N\le n\) and
matrix units \((e^{(k)}_{ij})\), and let \(M=M(N)\). Let \(0<\varepsilon_1\le1/9\) and
\(0<\delta\le\min\{\varepsilon_1,\delta_M(\varepsilon_1)\}\). If \(N\overset{\delta}{\subset}P\), there are
\(p^{(k)}_{ij}\in P\) satisfying the relations of matrix units,
\(p^{(k)}_{ij}p^{(l)}_{rs}=\delta_{kl}\delta_{jr}p^{(k)}_{is}\), \((p^{(k)}_{ij})^*=p^{(k)}_{ji}\) (but possibly
\(\sum_{k,i}p^{(k)}_{ii}\ne1\)), such that
\[
\|p^{(k)}_{j1}-e^{(k)}_{j1}\|_2\le11\sqrt{n\varepsilon_1}\qquad\text{for all }j,k .
\]
Consequently, for every \(\varepsilon>0\) there is \(\delta>0\), depending only on \(n\) and \(\varepsilon\), such that
\(N\overset{\delta}{\subset}P\) and \(\dim N\le n\) give such \(p^{(k)}_{ij}\) with
\(\|p^{(k)}_{j1}-e^{(k)}_{j1}\|_2<\varepsilon\).

*Proof.* *Diagonal.* The \(M\) projections \(e^{(k)}_{ii}\) are orthogonal and lie in the unit ball of \(N\). By
Definition 6.1 and Lemma 6.5(i) there are orthogonal projections \(q^{(k)}_i\in P\) with
\(\|q^{(k)}_i-e^{(k)}_{ii}\|_2<\varepsilon_1\).

*Off-diagonal.* Fix \(k\), drop it from the notation, and let \(2\le j\le n_k\). Choose \(y\in P\), \(\|y\|\le1\), with
\(\|y-e_{j1}\|_2<\delta\), and put \(z_j=q_jyq_1\in P\). Since \(e_{j1}=e_{jj}e_{j1}e_{11}\),
\[
\|z_j-e_{j1}\|_2\le\|(q_j-e_{jj})yq_1\|_2+\|e_{jj}(y-e_{j1})q_1\|_2+\|e_{j1}(q_1-e_{11})\|_2<3\varepsilon_1=:\beta .
\]
Apply Lemma 6.4(b) to \(z_j\) and \(u=e_{j1}\) (with \(u^*u=e_{11}\)). We get a projection \(g_j\in P\) and a partial
isometry \(v_j\in P\) with \(v_j^*v_j=g_j\le q_1\) (the support of \(|z_j|\) is below \(q_1\)),
\(v_jv_j^*\le q_j\) (the range of \(z_j\) is below \(q_j\)), and, using \(\sqrt{3\beta}=3\sqrt{\varepsilon_1}\) and
\(3\varepsilon_1\le\sqrt{\varepsilon_1}\),
\[
\|g_j-e_{11}\|_2\le6\sqrt{\varepsilon_1},\qquad\|v_j-e_{j1}\|_2\le4\sqrt{\varepsilon_1}.
\]

*Correcting the initial projections.* Put \(p_{11}=q_1\wedge g_2\wedge\dots\wedge g_{n_k}\in P\) (so \(p_{11}=q_1\) if
\(n_k=1\)). Since \(\|q_1-g_j\|_2\le\varepsilon_1+6\sqrt{\varepsilon_1}\le7\sqrt{\varepsilon_1}\) and
\(q_1-g_j\) is a projection, Lemma 6.2 gives
\(\tau(q_1-p_{11})\le\sum_{j\ge2}\tau(q_1-g_j)\le49n\varepsilon_1\). Hence \(\|q_1-p_{11}\|_2\le7\sqrt{n\varepsilon_1}\),
\(\|p_{11}-e_{11}\|_2\le8\sqrt{n\varepsilon_1}\), and \(\|g_j-p_{11}\|_2\le7\sqrt{n\varepsilon_1}\) since
\(p_{11}\le g_j\le q_1\). Put \(p_{j1}=v_jp_{11}\) for \(j\ge2\), and \(p_{ij}=p_{i1}p_{j1}^*\). Then
\[
\|p_{j1}-e_{j1}\|_2\le\|v_j(p_{11}-g_j)\|_2+\|v_j-e_{j1}\|_2\le7\sqrt{n\varepsilon_1}+4\sqrt{\varepsilon_1}\le11\sqrt{n\varepsilon_1}.
\]

*Relations.* \(p_{j1}^*p_{j1}=p_{11}g_jp_{11}=p_{11}\), and \(p_{j1}p_{j1}^*\le q_j\) (also for \(j=1\)). As the \(q\)'s
are orthogonal (also across different \(k\)), \(p_{i1}^*p_{j1}=p_{i1}^*q_iq_jp_{j1}=\delta_{ij}p_{11}\), and products
from different blocks vanish. Then \(p_{ij}p_{rs}=p_{i1}(p_{j1}^*p_{r1})p_{s1}^*=\delta_{jr}p_{i1}p_{11}p_{s1}^*=\delta_{jr}p_{is}\),
and \(p_{ij}^*=p_{ji}\).

For the last statement choose \(\varepsilon_1\le1/9\) with \(11\sqrt{n\varepsilon_1}<\varepsilon\) and
\(\delta=\min\{\varepsilon_1,\delta_1(\varepsilon_1),\dots,\delta_n(\varepsilon_1)\}\); note \(M\le n\). \(\square\)

**Proposition 6.7 (intertwining partial isometry).** Let \(N\subset R\) be finite-dimensional with matrix units
\((e^{(k)}_{ij})\), and let \((p^{(k)}_{ij})\) be elements of a subalgebra \(P\) satisfying the relations of matrix
units, with
\[
\gamma:=\sum_{k,j}\|p^{(k)}_{j1}-e^{(k)}_{j1}\|_2\le1 .
\]
Let \(\psi:N\to P\) be the \*-homomorphism with \(\psi(e^{(k)}_{ij})=p^{(k)}_{ij}\), \(p_0=\psi(1)\), and
\(\widetilde N=\psi(N)+\mathbb C(1-p_0)\subset P\), a subalgebra with \(\dim\widetilde N\le\dim N+1\). Then there is a
partial isometry \(w\in R\) such that, with \(f=w^*w\) and \(\tilde f=ww^*\):

1. \(wx=\psi(x)w\) for \(x\in N\); \(f\in N'\cap R\), \(\tilde f\le p_0\), \(\tilde f\in\widetilde N'\cap R\), and
   \(wxw^*=\psi(x)\tilde f\) for \(x\in N\);
2. \(\|w-1\|_2\le3\sqrt\gamma\) and \(\|1-f\|_2\le\sqrt{2\gamma}\);
3. if \(E\in N'\cap R\) is a projection with \(E\le f\), then \(F=wEw^*\) is a projection in \(\widetilde N'\cap R\) and
   \((wE)x(wE)^*=\psi(x)F\) for \(x\in N\);
4. there is a unitary \(u\in R\) with \(uf=w\), \(ufu^*=\tilde f\), \(uN^fu^*=\widetilde N^{\tilde f}\), and
   \(\|u-1\|_2\le3\sqrt\gamma+3\sqrt{2\gamma}\).

*Proof.* Put \(z=\sum_{k,j}p^{(k)}_{j1}e^{(k)}_{1j}\). By the matrix unit relations of both systems,
\(ze^{(k)}_{ij}=p^{(k)}_{i1}e^{(k)}_{1j}=p^{(k)}_{ij}z\), so \(zx=\psi(x)z\) for all \(x\in N\). Also
\(z^*z=\sum_{k,j}e^{(k)}_{j1}p^{(k)}_{11}e^{(k)}_{1j}\), a sum of positive operators
\(T_{kj}\le e^{(k)}_{jj}\) living under the orthogonal projections \(e^{(k)}_{jj}\); so \(z^*z\le1\) and \(\|z\|\le1\).
Since \(1=\sum_{k,j}e^{(k)}_{j1}e^{(k)}_{1j}\),
\(\|z-1\|_2\le\sum_{k,j}\|(p^{(k)}_{j1}-e^{(k)}_{j1})e^{(k)}_{1j}\|_2\le\gamma\).

(1) \(z^*z\) commutes with \(N\): \(z^*zx=z^*\psi(x)z=(\psi(x^*)z)^*z=(zx^*)^*z=xz^*z\). Hence \(|z|\) and its support
\(f\) lie in \(N'\). Let \(z=w|z|\). Then \((wx-\psi(x)w)|z|=zx-\psi(x)z=0\), so \(wx-\psi(x)w\) vanishes on the range
of \(f\); and \((wx-\psi(x)w)(1-f)=w(1-f)x-\psi(x)w(1-f)=0\). So \(wx=\psi(x)w\). Taking adjoints,
\(xw^*=w^*\psi(x)\); hence \(wxw^*=\psi(x)ww^*=\psi(x)\tilde f\), and \(\tilde f\psi(x)=wxw^*=\psi(x)\tilde f\). Since
\(z=p_0z\), \(\tilde f\le p_0\); so \(\tilde f\) commutes with \(\psi(N)\) and with \(1-p_0\).

(2) Since \(0\le|z|\le1\), \((1-t)^2\le1-t^2\) on \([0,1]\) gives
\(\|1-|z|\|_2^2\le\tau(1-z^*z)=2\operatorname{Re}\tau(1-z)-\|1-z\|_2^2\le2\|1-z\|_2\le2\gamma\). Since
\((1-f)|z|=0\), \(1-f=(1-f)(1-|z|)\) and \(\|1-f\|_2\le\sqrt{2\gamma}\). Finally
\(w-1=w(1-|z|)+(z-1)\), so \(\|w-1\|_2\le\sqrt{2\gamma}+\gamma\le3\sqrt\gamma\).

(3) \(wE\) is a partial isometry with \((wE)^*wE=EfE=E\), so \(F\) is a projection. For \(x\in N\),
\((wE)x(wE)^*=wxEw^*=\psi(x)wEw^*=\psi(x)F\). Taking \(x\) unitary shows \(F\) commutes with \(\psi(N)\); and
\(F\le\tilde f\le p_0\).

(4) Since \(f\sim\tilde f\), (B5) gives a partial isometry \(w'\) with \(w'^*w'=1-f\), \(w'w'^*=1-\tilde f\). Put
\(u=w+w'\); it is a unitary (the initial and final projections of \(w\) and \(w'\) are complementary), \(uf=w\) and
\(ufu^*=\tilde f\). For \(x\in N\), \(u(xf)u^*=ufxfu^*=wxw^*=\psi(x)\tilde f\), and \(u(1-f)u^*=1-\tilde f\); so
\(uN^fu^*=\{\psi(x)\tilde f+\lambda(1-\tilde f)\}=\widetilde N^{\tilde f}\) (for \(y=\psi(x)+\mu(1-p_0)\in\widetilde N\),
\(y\tilde f=\psi(x)\tilde f\)). Finally \(\|u-1\|_2\le\|w-f\|_2+\|w'-(1-f)\|_2\le(\|w-1\|_2+\|1-f\|_2)+(\|w'\|_2+\|1-f\|_2)\)
and \(\|w'\|_2=\|1-f\|_2\). \(\square\)

**Lemma 6.8 (shrinking a projection into the commutant).** Let \(N\subset R\) be finite-dimensional, \(M=M(N)\) and
\(K_M=2^MM!\). There is a finite group \(G\) of unitaries of \(N\) with \(|G|\le K_M\) and \(G'\cap R=N'\cap R\).
Consequently, for every projection \(e\in R\), the projection \(E=\bigwedge_{g\in G}geg^*\) lies in \(N'\cap R\),
\(E\le e\), and \(\tau(1-E)\le K_M\,\tau(1-e)\).

*Proof.* Let \(G\) be the set of unitaries \(\sum_k\sum_i\epsilon_{k,i}e^{(k)}_{\sigma_k(i)i}\) with signs
\(\epsilon_{k,i}\in\{\pm1\}\) and permutations \(\sigma_k\) of \(\{1,\dots,n_k\}\): the block diagonal signed
permutation matrices. It is a group of order \(\prod_k2^{n_k}n_k!\le2^MM!\). It contains \(1-2e^{(k)}_{ii}\) (one sign
flipped), so the algebra it generates contains every \(e^{(k)}_{ii}\); it contains the transposition matrix \(g\) of
\(i\) and \(j\) in block \(k\), and \(e^{(k)}_{ii}g=e^{(k)}_{ij}\). So \(G\) generates \(N\) as an algebra and
\(G'\cap R=N'\cap R\). For \(h\in G\), \(hEh^*=\bigwedge_ghgeg^*h^*=E\), so \(E\in G'=N'\). Clearly \(E\le e\), and
Lemma 6.2 with \(q=1\) gives \(\tau(1-E)\le\sum_g\tau(1-geg^*)=|G|\,\tau(1-e)\). \(\square\)

**Lemma 6.9 (from a partial isometry to a unitary).** Let \(E\in R\) be a projection and \(x\in R\) a partial isometry
with \(x^*x=E\) and \(\|x-E\|\le d_0\le1/4\). Then there is a unitary \(v\in R\) with \(vE=x\), \(vEv^*=xx^*\) and
\(\|v-1\|\le5d_0\).

*Proof.* Put \(F=xx^*\). From \(F-E=(x-E)x^*+E(x-E)^*\), \(d:=\|F-E\|\le2d_0\le1/2\). Let
\(T=(1-E)(1-F)(1-E)=(1-E)-(1-E)F(1-E)\). Since \(F(1-E)=(F-E)(1-E)\) has norm \(\le d\),
\(T\ge(1-d^2)(1-E)\); so \(T\) is invertible in \((1-E)R(1-E)\), with inverse square root \(T^{-1/2}\) there. Put
\(y=(1-F)(1-E)T^{-1/2}\). Then \(y^*y=1-E\). Also \(y=(1-F)y\), and \(yy^*\) is the range projection of
\((1-F)(1-E)\), which is \(1-F\) because \((1-F)(1-E)(1-F)\ge(1-d^2)(1-F)\) by the same argument. So \(yy^*=1-F\).
Moreover \(\|y-(1-E)\|\le\|T^{-1/2}-(1-E)\|+\|(1-F)(1-E)-(1-E)\|\le\bigl((1-d^2)^{-1/2}-1\bigr)+d\le2d\), using
\((1-s)^{-1/2}-1\le s/(1-s)\le\frac43s\) for \(s=d^2\le\frac14\) and \(\frac43d^2\le d\).

Put \(v=x+y\). Since \(x=Fx=xE\) and \(y=(1-F)y=y(1-E)\), the cross terms \(x^*y\) and \(xy^*\) vanish, so
\(v^*v=E+(1-E)=1\) and \(vv^*=F+(1-F)=1\). Also \(vE=x\), \(vEv^*=xx^*\), and
\(\|v-1\|\le\|x-E\|+\|y-(1-E)\|\le d_0+4d_0\). \(\square\)

**Theorem 6.10 (perturbation theorem).** For every \(n\ge1\) and \(\varepsilon'\in(0,1]\) there is \(\delta>0\),
depending only on \(n\) and \(\varepsilon'\), with the following property. Let \((R,\tau)\) be as above and
\(N,P\subset R\) subalgebras with \(\dim N\le n\) and \(N\overset{\delta}{\subset}P\). Then there are a projection
\(E\in N'\cap R\) with \(\tau(1-E)\le\varepsilon'\), a unitary \(v\in R\) with \(\|v-1\|\le\varepsilon'\), and a
subalgebra \(\widetilde N\subset P\) with \(\dim\widetilde N\le n+1\), such that \(F=vEv^*\in\widetilde N'\) and
\[
vN^Ev^*=\widetilde N^{F}.
\]

*Proof.* Put \(K=2^nn!\), \(\alpha=(\varepsilon'/5)^2\), \(\gamma=\alpha\varepsilon'/(11K)\),
\(\varepsilon_1=\min\{1/9,\ \gamma^2/(121n^3)\}\), and \(\delta=\min\{\varepsilon_1,\delta_1(\varepsilon_1),\dots,\delta_n(\varepsilon_1)\}\).
Let \(N\overset{\delta}{\subset}P\), \(\dim N\le n\), \(M=M(N)\le n\), with matrix units \((e^{(k)}_{ij})\).

*Step 1.* Lemma 6.6 gives matrix units \((p^{(k)}_{ij})\) in \(P\) with
\(\sum_{k,j}\|p^{(k)}_{j1}-e^{(k)}_{j1}\|_2\le M\cdot11\sqrt{n\varepsilon_1}\le11n^{3/2}\sqrt{\varepsilon_1}\le\gamma\).

*Step 2.* Proposition 6.7 gives \(\psi\), \(\widetilde N\subset P\) (\(\dim\widetilde N\le n+1\)) and a partial isometry
\(w\) with \(\|w-1\|_2^2\le9\gamma\), \(\tau(1-f)=\|1-f\|_2^2\le2\gamma\), where \(f=w^*w\in N'\).

*Step 3.* Let \(h=(w-1)^*(w-1)\) and \(e_0=\chi_{[0,\alpha]}(h)\). Since \(h\ge\alpha(1-e_0)\),
\(\tau(1-e_0)\le\tau(h)/\alpha\le9\gamma/\alpha\), and \(\|(w-1)e_0\|^2=\|e_0he_0\|\le\alpha\). Put
\(e=e_0\wedge f\); by Lemma 6.2, \(\tau(1-e)\le9\gamma/\alpha+2\gamma\le11\gamma/\alpha\). Lemma 6.8 gives a projection
\(E\in N'\cap R\) with \(E\le e\) and \(\tau(1-E)\le K\cdot11\gamma/\alpha=\varepsilon'\).

*Step 4.* Put \(x=wE\). Since \(E\le f\), \(x^*x=E\); and \(\|x-E\|=\|(w-1)e_0E\|\le\sqrt\alpha=\varepsilon'/5\le1/4\).
Lemma 6.9 gives a unitary \(v\) with \(vE=x\), \(F:=vEv^*=wEw^*\), and \(\|v-1\|\le5\sqrt\alpha=\varepsilon'\).

*Step 5.* By Proposition 6.7(3), \(F\in\widetilde N'\) and for \(y\in N\),
\(v(yE)v^*=(vE)y(vE)^*=(wE)y(wE)^*=\psi(y)F\); also \(v(1-E)v^*=1-F\). Hence
\(vN^Ev^*=\{\psi(y)F+\lambda(1-F)\}=\widetilde N^F\), since \(F\le p_0\) gives \((\psi(y)+\mu(1-p_0))F=\psi(y)F\).
\(\square\)

## 7. Continuity of the relative entropy

**Proposition 7.1 (conjugation by a unitary close to 1).** Let \(Q\subset R\) be finite-dimensional, \(M=M(Q)\), and
\(v\in R\) unitary. Then
\[
H(Q\mid vQv^*)\le\omega_M\bigl(2\|v-1\|\bigr),
\]
with \(\omega_M\) as in Lemma 2.6. In particular, for every \(m\) and \(\varepsilon>0\) there is \(\varepsilon'>0\) such
that \(H(Q\mid vQv^*)<\varepsilon\) whenever \(\dim Q\le m\) and \(\|v-1\|<\varepsilon'\).

*Proof.* The map \(y\mapsto vE_Q(v^*yv)v^*\) is the \(\tau\)-preserving conditional expectation onto \(vQv^*\) (it is
positive, unital, \(vQv^*\)-bimodular and preserves \(\tau\)), so \(\tau\eta(E_{vQv^*}(y))=\tau\eta(E_Q(v^*yv))\).
Let \(x\in\mathcal S_1(R)\) and put \(X_i=E_Q(x_i)\), \(X'_i=E_Q(v^*x_iv)\), \(s_i=\tau(x_i)\). Then \(X_i,X'_i\in Q_+\),
\(\sum_iX_i=\sum_iX'_i=1\), \(\tau(X_i)=\tau(X'_i)=s_i\), \(\sum_is_i=1\), and by (B1), (B7),
\[
\|X_i-X'_i\|_1\le\|x_i-v^*x_iv\|_1\le\|(1-v^*)x_i\|_1+\|v^*x_i(1-v)\|_1\le2\|v-1\|\,s_i .
\]
The quantity to bound is \(\sum_i(\tau\eta(X'_i)-\tau\eta(X_i))\). By Lemma 1.1 (in \(Q\)),
\[
\sum_i\bigl(\tau\eta(X'_i)-\tau\eta(X_i)\bigr)=\sum_i\bigl(\operatorname{Tr}_Q\eta(\widehat{X'_i})-\operatorname{Tr}_Q\eta(\widehat X_i)\bigr)+\tau\Bigl(L_Q\sum_i(X'_i-X_i)\Bigr),
\]
and the last term is \(\tau(L_Q(1-1))=0\). For \(s_i=0\) we have \(X_i=X'_i=0\). For \(s_i>0\), (1.1) gives
\(\operatorname{Tr}_Q\eta(\widehat X_i)=s_i\operatorname{Tr}_Q\eta(\widehat X_i/s_i)+\eta(s_i)\), and the same for
\(X'_i\) with the same \(\eta(s_i)\). By Lemma 2.6 and Lemma 1.1,
\[
\operatorname{Tr}_Q\eta(\widehat{X'_i})-\operatorname{Tr}_Q\eta(\widehat X_i)\le s_i\,\omega_M\bigl(\|X_i-X'_i\|_1/s_i\bigr).
\]
Since \(\omega_M\) is concave and nondecreasing and \(\sum_is_i=1\),
\(\sum_is_i\omega_M(\|X_i-X'_i\|_1/s_i)\le\omega_M(\sum_i\|X_i-X'_i\|_1)\le\omega_M(2\|v-1\|)\). For the last
statement use \(M(Q)\le\dim Q\le m\), monotonicity of \(\omega_M\) in \(M\), and \(\omega_m(s)\to0\). \(\square\)

**Remark 7.2.** The cancellation of the term \(\tau(L_Q\,\cdot\,)\) over the whole family is essential. For a single
positive \(x\), the absolute value of \(\tau\eta(E_{vQv^*}(x))-\tau\eta(E_Q(x))\) is *not* bounded by
\(c\,\tau(x)\) with \(c\) depending only on \(\dim Q\) and \(\|v-1\|\): Exercise 8.5 gives, for \(\dim Q=2\) and a fixed
\(\|v-1\|\), examples where the ratio to \(\tau(x)\) is arbitrarily large in absolute value. The reason is that \(L_Q\) is large on
minimal projections of small trace.

**Theorem 7.3 (continuity of relative entropy).** For every \(n\ge1\) and \(\varepsilon>0\) there is \(\delta>0\),
depending only on \(n\) and \(\varepsilon\), such that for every finite von Neumann algebra \(R\) with a faithful normal
tracial state \(\tau\) and all subalgebras \(N,P\subset R\),
\[
\dim N\le n\ \text{ and }\ N\overset{\delta}{\subset}P\quad\Longrightarrow\quad H(N\mid P)<\varepsilon .
\]

*Proof.* Choose \(\varepsilon'\in(0,\tfrac12]\) with
\[
\varepsilon'\log n+\omega_{n+1}(2\varepsilon')+h(\varepsilon')<\varepsilon,
\]
which is possible since each term tends to \(0\) with \(\varepsilon'\). Let \(\delta\) be given by Theorem 6.10 for
\(n\) and \(\varepsilon'\). If \(\dim N\le n\) and \(N\overset{\delta}{\subset}P\), take \(E\), \(v\), \(\widetilde N\)
and \(F=vEv^*\) as in Theorem 6.10. By the triangle inequality (Proposition 5.2(4)),
\[
H(N\mid P)\le H(N\mid N^E)+H(N^E\mid vN^Ev^*)+H(\widetilde N^F\mid\widetilde N)+H(\widetilde N\mid P),
\]
where we used \(vN^Ev^*=\widetilde N^F\). We bound the four terms.

- \(H(N\mid N^E)\le\tau(1-E)\log M(N)\le\varepsilon'\log n\) by Proposition 5.9.
- \(H(N^E\mid vN^Ev^*)\le\omega_{M(N^E)}(2\|v-1\|)\le\omega_{n+1}(2\varepsilon')\) by Proposition 7.1, since
  \(M(N^E)\le M(N)+1\le n+1\).
- \(H(\widetilde N^F\mid\widetilde N)\le h(\tau(F))=h(\tau(1-E))\le h(\varepsilon')\) by Proposition 5.8, because
  \(F\in\widetilde N'\), \(\tau(1-F)=\tau(1-E)\le\varepsilon'\le\frac12\), and \(h\) is symmetric and increasing on
  \([0,\frac12]\).
- \(H(\widetilde N\mid P)=0\) by Proposition 5.2(1), since \(\widetilde N\subset P\).

The sum is less than \(\varepsilon\). \(\square\)

*Reference:* [Connes–Størmer 1975, Theorem 1 of Section 3].

**Corollary 7.4.** Let \(P_1\subset P_2\subset\cdots\) be subalgebras of \(R\) with
\(\bigl(\bigcup_qP_q\bigr)''=R\). Then \(H(N\mid P_q)\) decreases to \(0\) as \(q\to\infty\), for every finite-dimensional
subalgebra \(N\subset R\).

*Proof.* The sequence decreases by Proposition 5.2(2). Let \(\varepsilon>0\), \(n=\dim N\), and \(\delta\) as in
Theorem 7.3. The unit ball of \(N\) is norm compact; choose \(x_1,\dots,x_r\) in it such that every \(x\) in the unit
ball of \(N\) has \(\|x-x_s\|<\delta/3\) for some \(s\). The union \(A_0=\bigcup_qP_q\) is a unital \*-algebra with
\(A_0''=R\). By (B8) and (B7), for each \(s\) there is \(y_s\) in the unit ball of \(A_0\) with
\(\|x_s-y_s\|_2<\delta/3\); since the \(P_q\) increase, all \(y_s\) lie in one \(P_{q_0}\). For \(q\ge q_0\) and \(x\) in
the unit ball of \(N\), pick \(s\) as above: \(\|x-y_s\|_2\le\|x-x_s\|+\|x_s-y_s\|_2<\delta\). So
\(N\overset{\delta}{\subset}P_q\), and \(H(N\mid P_q)<\varepsilon\). \(\square\)

## 8. Exercises

**Exercise 8.1.** Let \(N\) be finite-dimensional with central weights \(w_k=\tau(c_k)\) and block sizes \(n_k\).
Show that \(H(Z(N))\le H(N)\le\log M(N)\), and that \(H(N)=\log M(N)\) exactly when every minimal projection of \(N\)
has trace \(1/M(N)\).

*Solution.* By Corollary 4.2, \(H(N)=H(Z(N))+\sum_kw_k\log n_k\ge H(Z(N))\). By Theorem 4.1,
\(H(N)=\sum_\alpha\eta(\tau(e_\alpha))\), a sum of \(M=M(N)\) terms with \(\sum_\alpha\tau(e_\alpha)=1\). Strict
concavity of \(\eta\) gives \(\frac1M\sum_\alpha\eta(\tau(e_\alpha))\le\eta(1/M)\), with equality if and only if all
\(\tau(e_\alpha)\) equal \(1/M\). Since \(M\eta(1/M)=\log M\), the claims follow.

**Exercise 8.2.** Let \(N\subset R\) be finite-dimensional and \(P\subset R\) any subalgebra. Show that
\(H(N\mid P)=0\) if and only if \(N\subset P\).

*Solution.* If \(N\subset P\) use Proposition 5.2(1). Conversely, let \(H(N\mid P)=0\) and let \(e\in N\) be a
projection. The family \((e,1-e)\) gives
\(0\ge\tau\eta(E_P(e))+\tau\eta(E_P(1-e))-\tau\eta(e)-\tau\eta(1-e)=\tau\eta(E_P(e))+\tau\eta(1-E_P(e))\). Since
\(0\le E_P(e)\le1\) and \(\eta\ge0\) on \([0,1]\), both terms are \(\ge0\), so \(\tau(\eta(E_P(e)))=0\). As \(\tau\) is
faithful and \(\eta(E_P(e))\ge0\), \(\eta(E_P(e))=0\); so the spectrum of \(E_P(e)\) lies in \(\{0,1\}\) and \(E_P(e)\)
is a projection. Then \(\|E_P(e)\|_2^2=\tau(E_P(e))=\tau(e)=\|e\|_2^2\), and by (B1)
\(\|e-E_P(e)\|_2^2=\|e\|_2^2-\|E_P(e)\|_2^2=0\), so \(e=E_P(e)\in P\). Since \(N\) is spanned by its projections,
\(N\subset P\).

**Exercise 8.3.** With \(A\), \(B\) as in Example 4.6, show that \(H(A\mid B)=\log2\).

*Solution.* \(H(A\mid B)\le H(A)=\log2\) by Proposition 5.2(3). Let \(e_1,e_2\) be the diagonal matrix units and
\(f_j=ue_ju^*\). Since \(|\langle u\varepsilon_j,\varepsilon_i\rangle|^2=\frac12\), \(\tau(e_if_j)=\frac14\), and
\(E_B(e_i)=\sum_j\frac{\tau(e_if_j)}{\tau(f_j)}f_j=\frac12\). The family \((e_1,e_2)\) gives
\(\sum_i(\tau\eta(\tfrac12)-\tau\eta(e_i))=2\cdot\frac12\log2=\log2\).

**Exercise 8.4 (splitting a unitary).** Let \(u\in R\) be a unitary with \(\|u-1\|_2\le\alpha\le1\). Show that there are
unitaries \(v,v'\in R\) with \(u=vv'\), \(\|v-1\|\le\alpha^{1/2}\), and \(\tau(\operatorname{supp}(v'-1))\le\alpha\).

*Solution.* If \(\alpha=0\), then \(\|u-1\|_2=0\), so \(u=1\) because \(\tau\) is faithful, and \(v=v'=1\) will do.
Let \(\alpha>0\), and let \(e'\) denote the spectral projection of the normal operator \(u\) for the set
\(\{\lambda\in\mathbb T:|\lambda-1|^2\ge\alpha\}\). It commutes with \(u\), and \(|u-1|^2\ge\alpha e'\), so
\(\alpha\tau(e')\le\tau(|u-1|^2)=\|u-1\|_2^2\le\alpha^2\) and \(\tau(e')\le\alpha\). Put \(v=u(1-e')+e'\) and
\(v'=(1-e')+ue'\). Both are unitaries, since \(u\) commutes with \(e'\), and \(vv'=u(1-e')+ue'=u\). Now
\(v-1=(u-1)(1-e')\) and \(|u-1|^2(1-e')\le\alpha(1-e')\), so \(\|v-1\|\le\alpha^{1/2}\). Finally \(v'-1=(u-1)e'\), whose
support is below \(e'\).

**Exercise 8.5 (no pointwise estimate in Proposition 7.1).** Let \(K\ge3\), let \(R\) contain a unital copy of
\(M_K(\mathbb C)\) (for example \(R=M_K(\mathbb C)\), or the hyperfinite II₁ factor when \(K\) is a power of \(2\)),
with \(\tau\) restricting to the normalized trace. Let \(\xi_1,\dots,\xi_K\) be an orthonormal basis of
\(\mathbb C^K\), \(e\) the projection onto \(\mathbb C\xi_1\), \(Q=\mathbb Ce+\mathbb C(1-e)\), \(x\) the projection onto
\(\mathbb C\xi_2\), and \(v\) the rotation by an angle \(\theta\) in the plane of \(\xi_1,\xi_2\) (the identity on the
other basis vectors). Show that
\[
\frac{\tau\eta(E_{vQv^*}(x))-\tau\eta(E_Q(x))}{\tau(x)}=h(\sin^2\theta)-\sin^2\theta\,\log(K-1),
\]
and that, for fixed \(\theta\) with \(\sin\theta\ne0\) (for example \(0<\theta<\pi/2\)), it tends to \(-\infty\) as
\(K\to\infty\), while \(\|v-1\|=2|\sin(\theta/2)|\) and \(\dim Q=2\) are fixed. (For \(\sin\theta=0\) both sides are
\(0\).)

*Solution.* For \(y\in R\), \(E_Q(y)=K\tau(ye)\,e+\frac K{K-1}\tau(y(1-e))(1-e)\). Since \(\tau(xe)=0\) and
\(\tau(x)=1/K\), \(E_Q(x)=\frac1{K-1}(1-e)\) and \(\tau\eta(E_Q(x))=\frac{K-1}K\eta(\frac1{K-1})=\frac1K\log(K-1)\). As in
the proof of Proposition 7.1, \(\tau\eta(E_{vQv^*}(x))=\tau\eta(E_Q(v^*xv))\). The projection \(v^*xv\) projects onto
\(v^*\xi_2=\sin\theta\,\xi_1+\cos\theta\,\xi_2\) (up to the sign convention of the rotation), so
\(\tau(v^*xve)=\sin^2\theta/K\) and \(E_Q(v^*xv)=\sin^2\theta\,e+\frac{\cos^2\theta}{K-1}(1-e)\). Hence, by (1.1),
\[
\tau\eta(E_Q(v^*xv))=\frac1K\eta(\sin^2\theta)+\frac{K-1}K\eta\Bigl(\frac{\cos^2\theta}{K-1}\Bigr)
=\frac1K\Bigl(\eta(\sin^2\theta)+\eta(\cos^2\theta)+\cos^2\theta\log(K-1)\Bigr).
\]
Subtracting and dividing by \(\tau(x)=1/K\) gives the formula. Finally \(\|v-1\|=\max|\lambda-1|\) over the eigenvalues
\(1,e^{\pm i\theta}\) of \(v\), which is \(2|\sin(\theta/2)|\).

The difference can also be made large and positive. Put \(v_1=v^*\) and \(x_1=v^*xv\), so \(\tau(x_1)=1/K\) and
\(\|v_1-1\|=\|v-1\|\). Then \(E_{v_1Qv_1^*}(x_1)=v^*E_Q(x)v\), so
\(\tau\eta(E_{v_1Qv_1^*}(x_1))-\tau\eta(E_Q(x_1))=\tau\eta(E_Q(x))-\tau\eta(E_Q(v^*xv))\), and the ratio to
\(\tau(x_1)\) is \(\sin^2\theta\,\log(K-1)-h(\sin^2\theta)\), which tends to \(+\infty\) when \(\sin\theta\ne0\). So not
even a one-sided pointwise bound holds.

## References



- [Connes–Størmer 1975] A. Connes and E. Størmer, Entropy for automorphisms of II₁ von Neumann algebras, Acta Math.
  134 (1975), no. 3–4, 289–306. Free at https://doi.org/10.1007/BF02392105
- [Connes 1994] A. Connes, *Noncommutative geometry*, Academic Press, San Diego, CA, 1994. Free at
  https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf
- [Lieb 1973] E. H. Lieb, Convex trace functions and the Wigner–Yanase–Dyson conjecture, Advances in Math. 11
  (1973), 267–288. https://doi.org/10.1016/0001-8708(73)90011-X. Free at https://doi.org/10.1016/0001-8708(73)90011-x
- [Lindblad 1974] G. Lindblad, Expectations and entropy inequalities for finite quantum systems, Comm. Math. Phys.
  39 (1974), 111–119. https://doi.org/10.1007/BF01608390. Free at https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-39/issue-2/Expectations-and-entropy-inequalities-for-finite-quantum-systems/cmp/1103860161.full
- [Choi 1974] M.-D. Choi, A Schwarz inequality for positive linear maps on C\*-algebras, Illinois J. Math. 18 (1974),
  565–574. https://doi.org/10.1215/ijm/1256051007
- [Fannes 1973] M. Fannes, A continuity property of the entropy density for spin lattice systems, Comm. Math. Phys.
  31 (1973), 291–294. https://doi.org/10.1007/BF01646490. Free at https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-31/issue-4/A-continuity-property-of-the-entropy-density-for-spin-lattice/cmp/1103859037.full
