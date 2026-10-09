# Hilbert spaces and compact operators

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the Hilbert-space facts that the operator-algebra lessons use. It covers:
- the Cauchy–Schwarz inequality for positive semidefinite forms;
- the projection theorem and the Riesz–Fréchet theorem;
- bounded sesquilinear forms and adjoints;
- orthonormal bases: Bessel's inequality, Parseval's identity, existence and Hilbert dimension;
- compact operators: they form a closed ideal, closed under adjoints, in which the finite-rank operators are dense;
- the spectral theorem for compact self-adjoint operators;
- the Riesz theory of compact operators: for \(\lambda\ne0\), \(T-\lambda\) has finite-dimensional kernel and closed range; it is invertible when injective; and nonzero points of the spectrum are isolated eigenvalues;
- Hilbert tensor products;
- multiplication operators on a \(\sigma\)-finite measure space, which form an algebra equal to its own commutant.

It builds on Hahn–Banach, Baire and the basic theorems on Banach spaces, cited as *the first lesson*.

## Conventions

Hilbert spaces are complex unless a statement says otherwise. No separability is assumed. Inner products are linear in the first variable. \(B(H)\) is the algebra of bounded operators. The *spectrum* \(\sigma(T)\) of \(T\in B(H)\) is the set of \(\lambda\in\mathbb C\) for which \(T-\lambda\) has no inverse in \(B(H)\). For \(\xi,\eta\in H\), \(\theta_{\xi,\eta}\) is the rank-one operator \(\zeta\mapsto\langle\zeta,\eta\rangle\xi\). \(L^\perp=\{\xi:\langle\xi,\eta\rangle=0\ \forall\eta\in L\}\).

## 1. Positive semidefinite forms

A *sesquilinear form* on a complex vector space \(V\) is a map \(B:V\times V\to\mathbb C\), linear in the first variable and conjugate-linear in the second. It is *Hermitian* if \(B(\eta,\xi)=\overline{B(\xi,\eta)}\), and *positive semidefinite* if \(B(\xi,\xi)\ge0\) for all \(\xi\).

**Proposition 1.1.**
1. (Polarization) \(4B(\xi,\eta)=\sum_{k=0}^3i^kB(\xi+i^k\eta,\xi+i^k\eta)\).
2. A form with \(B(\xi,\xi)\in\mathbb R\) for all \(\xi\) is Hermitian.
3. (Cauchy–Schwarz) If \(B\) is positive semidefinite, then \(|B(\xi,\eta)|^2\le B(\xi,\xi)B(\eta,\eta)\). Consequently \(\{\xi:B(\xi,\xi)=0\}\) is a subspace, and \(\xi\mapsto B(\xi,\xi)^{1/2}\) is a seminorm.

**Proof.**
1. Expand each term by sesquilinearity: the terms \(B(\xi,\xi)\) and \(B(\eta,\eta)\) cancel, and the cross terms give \(4B(\xi,\eta)\).
2. Apply 1 to \(B(\eta,\xi)\) and to \(\overline{B(\xi,\eta)}\), and compare the expressions term by term, using that the diagonal values are real.
3. By 2, \(B\) is Hermitian. For \(t\in\mathbb R\) and \(\theta\) with \(e^{-i\theta}B(\xi,\eta)=|B(\xi,\eta)|\), the quantity
\[
0\le B(\xi+te^{i\theta}\eta,\ \xi+te^{i\theta}\eta)=B(\xi,\xi)+2t|B(\xi,\eta)|+t^2B(\eta,\eta)
\]
is a nonnegative quadratic polynomial in \(t\). If \(B(\eta,\eta)>0\), its discriminant is \(\le0\). If \(B(\eta,\eta)=0\), the linear polynomial \(B(\xi,\xi)+2t|B(\xi,\eta)|\) is nonnegative for all \(t\), so \(|B(\xi,\eta)|=0\).

For the consequence, Cauchy–Schwarz gives \(B(\xi+\eta,\xi+\eta)\le(B(\xi,\xi)^{1/2}+B(\eta,\eta)^{1/2})^2\). \(\square\)

An inner product is a positive definite Hermitian form. A *Hilbert space* is an inner product space that is complete for \(\|\xi\|=\langle\xi,\xi\rangle^{1/2}\). The *parallelogram law* \(\|\xi+\eta\|^2+\|\xi-\eta\|^2=2\|\xi\|^2+2\|\eta\|^2\) follows by expanding.

## 2. The projection theorem and the Riesz–Fréchet theorem

**Theorem 2.1.** Let \(C\) be a nonempty closed convex subset of a real or complex Hilbert space \(H\), and \(\xi\in H\). There is exactly one \(c_0\in C\) with \(\|\xi-c_0\|=\operatorname{dist}(\xi,C)\).

**Proof.** Let \(d=\operatorname{dist}(\xi,C)\) and \(c_n\in C\) with \(\|\xi-c_n\|\to d\). The parallelogram law applied to \(\xi-c_n\) and \(\xi-c_m\), together with \(\frac{c_n+c_m}2\in C\), gives
\[
\|c_n-c_m\|^2=2\|\xi-c_n\|^2+2\|\xi-c_m\|^2-4\Big\|\xi-\frac{c_n+c_m}2\Big\|^2\le2\|\xi-c_n\|^2+2\|\xi-c_m\|^2-4d^2\to0.
\]
So \((c_n)\) is Cauchy. Its limit \(c_0\in C\) attains the distance. Two minimizers form a minimizing sequence when alternated, so they are equal. \(\square\)

**Theorem 2.2** (projection theorem). Let \(L\) be a closed subspace of a real or complex Hilbert space \(H\). Then:
1. \(H=L\oplus L^\perp\);
2. the map \(P:\xi\mapsto c_0\) of Theorem 2.1 is the orthogonal projection onto \(L\), a bounded self-adjoint idempotent with \(\|P\|\le1\);
3. for every subspace \(Y\), \(\overline Y=(Y^\perp)^\perp\).

**Proof.** Let \(c_0\) be the nearest point of \(L\) to \(\xi\). For \(\eta\in L\) and scalars \(t\), \(\|\xi-c_0-t\eta\|^2\ge\|\xi-c_0\|^2\). Expanding gives \(-2\operatorname{Re}(\bar t\langle\xi-c_0,\eta\rangle)+|t|^2\|\eta\|^2\ge0\). Small \(t\) of suitable phase force \(\langle\xi-c_0,\eta\rangle=0\). So \(\xi=c_0+(\xi-c_0)\) with \(\xi-c_0\in L^\perp\). The decomposition is unique because \(L\cap L^\perp=\{0\}\).

The projection is linear and idempotent, with \(\|P\xi\|^2+\|(1-P)\xi\|^2=\|\xi\|^2\). It is self-adjoint because \(\langle P\xi,\eta\rangle=\langle P\xi,P\eta\rangle=\langle\xi,P\eta\rangle\).

For 3: \((Y^\perp)^\perp\) is closed and contains \(Y\). By 1, applied to \(\overline Y\), we have \(H=\overline Y\oplus\overline Y^\perp\) and \(Y^\perp=\overline Y^\perp\). An element of \((Y^\perp)^\perp\) has zero component in \(\overline Y^\perp\). \(\square\)

**Theorem 2.3** (Riesz–Fréchet). Every bounded linear functional \(f\) on \(H\) is \(f(\xi)=\langle\xi,\eta\rangle\) for exactly one \(\eta\in H\), and \(\|f\|=\|\eta\|\).

**Proof.** If \(f=0\), take \(\eta=0\). Otherwise \(\ker f\) is a closed proper subspace. By Theorem 2.2 there is a unit vector \(u\perp\ker f\). For every \(\xi\), the vector \(f(\xi)u-f(u)\xi\) lies in \(\ker f\), so it is orthogonal to \(u\). This gives \(f(\xi)=f(u)\langle\xi,u\rangle=\langle\xi,\overline{f(u)}u\rangle\).

Uniqueness: \(\langle\xi,\eta-\eta'\rangle=0\) for all \(\xi\) forces \(\eta=\eta'\). The norm equality is Cauchy–Schwarz together with \(\xi=\eta\). \(\square\)

## 3. Sesquilinear forms and adjoints

**Theorem 3.1.** Let \(B\) be a sesquilinear form on \(H\) with \(|B(\xi,\eta)|\le C\|\xi\|\|\eta\|\). There is exactly one \(t\in B(H)\) with \(B(\xi,\eta)=\langle t\xi,\eta\rangle\), and \(\|t\|=\sup\{|B(\xi,\eta)|:\|\xi\|,\|\eta\|\le1\}\le C\). If \(B(\xi,\xi)\ge0\) for all \(\xi\), then \(\langle t\xi,\xi\rangle\ge0\).

**Proof.** For fixed \(\xi\), the map \(\eta\mapsto\overline{B(\xi,\eta)}\) is a bounded linear functional. By Theorem 2.3 it is \(\langle\eta,t\xi\rangle\) for a unique vector \(t\xi\). Uniqueness makes \(t\) linear. The norm formula follows from \(\|t\xi\|=\sup_{\|\eta\|\le1}|\langle t\xi,\eta\rangle|\). \(\square\)

**Corollary 3.2.** Every \(T\in B(H)\) has a unique adjoint \(T^*\in B(H)\) with \(\langle T\xi,\eta\rangle=\langle\xi,T^*\eta\rangle\). Moreover:
- \(T^{**}=T\), \(\|T^*\|=\|T\|\) and \(\|T^*T\|=\|T\|^2\);
- \((ST)^*=T^*S^*\), and \(T\mapsto T^*\) is conjugate-linear;
- (complex scalars) if \(\langle T\xi,\xi\rangle=0\) for all \(\xi\), then \(T=0\);
- (complex scalars) if \(\langle T\xi,\xi\rangle\in\mathbb R\) for all \(\xi\), then \(T=T^*\);
- for self-adjoint \(T\), \(\|T\|=\sup_{\|\xi\|=1}|\langle T\xi,\xi\rangle|\).

**Proof.** Apply Theorem 3.1 to \(B(\xi,\eta)=\langle\xi,T\eta\rangle\) to obtain \(T^*\). The algebraic rules follow from uniqueness. \(\|T\xi\|^2=\langle T^*T\xi,\xi\rangle\le\|T^*T\|\|\xi\|^2\) gives \(\|T\|^2\le\|T^*T\|\le\|T^*\|\|T\|\). So \(\|T\|\le\|T^*\|\), and by symmetry the two norms are equal. The two complex-scalar statements follow from Proposition 1.1(1) and (2), applied to \(B(\xi,\eta)=\langle T\xi,\eta\rangle\).

*The last statement.* Let \(m=\sup_{\|\xi\|=1}|\langle T\xi,\xi\rangle|\), so \(|\langle T\xi,\xi\rangle|\le m\|\xi\|^2\). For unit \(\xi,\eta\), expanding and using self-adjointness gives
\[
4\operatorname{Re}\langle T\xi,\eta\rangle=\langle T(\xi+\eta),\xi+\eta\rangle-\langle T(\xi-\eta),\xi-\eta\rangle\le m(\|\xi+\eta\|^2+\|\xi-\eta\|^2)=4m.
\]
Replacing \(\eta\) by \(e^{i\theta}\eta\) gives \(|\langle T\xi,\eta\rangle|\le m\), so \(\|T\|\le m\). The reverse inequality is Cauchy–Schwarz. \(\square\)

## 4. Orthonormal bases

An *orthonormal family* \((e_i)_{i\in I}\) satisfies \(\langle e_i,e_j\rangle=\delta_{ij}\). It is an *orthonormal basis* if its closed linear span is \(H\).

**Theorem 4.1.** Let \((e_i)_{i\in I}\) be an orthonormal family in \(H\).
1. (Bessel) \(\sum_i|\langle\xi,e_i\rangle|^2\le\|\xi\|^2\). In particular \(\langle\xi,e_i\rangle\ne0\) for at most countably many \(i\).
2. For \((c_i)\in\ell^2(I)\), the sum \(\sum_ic_ie_i\) converges, as the net of finite partial sums, and \(\|\sum_ic_ie_i\|^2=\sum_i|c_i|^2\).
3. The following are equivalent:
   - the family is a basis;
   - it is maximal among orthonormal families;
   - \(\xi=\sum_i\langle\xi,e_i\rangle e_i\) for every \(\xi\);
   - Parseval's identity \(\langle\xi,\eta\rangle=\sum_i\langle\xi,e_i\rangle\langle e_i,\eta\rangle\) holds for all \(\xi,\eta\).
4. Every orthonormal family is contained in an orthonormal basis. A separable Hilbert space has a finite or countable orthonormal basis.
5. Any two orthonormal bases of \(H\) have the same cardinality, the *Hilbert dimension* of \(H\).

**Proof.**
1. For finite \(F\subseteq I\), \(\xi-\sum_{i\in F}\langle\xi,e_i\rangle e_i\) is orthogonal to each \(e_i\) with \(i\in F\). So \(\|\xi\|^2\ge\sum_{i\in F}|\langle\xi,e_i\rangle|^2\). The set \(\{i:|\langle\xi,e_i\rangle|>1/n\}\) is finite for every \(n\).

2. Only countably many \(c_i\) are nonzero. The partial sums form a Cauchy net, because \(\|\sum_{i\in F\setminus G}c_ie_i\|^2=\sum_{F\setminus G}|c_i|^2\).

3. *Basis implies expansion.* The vector \(\xi-\sum_i\langle\xi,e_i\rangle e_i\) is orthogonal to every \(e_j\), hence to their closed span \(H\), so it is zero.
- *Expansion implies Parseval:* take inner products of the expansions.
- *Parseval implies maximality:* a unit vector \(e\) orthogonal to all \(e_i\) would have \(\|e\|^2=\sum|\langle e,e_i\rangle|^2=0\).
- *Maximality implies basis:* if the closed span \(L\) were not \(H\), Theorem 2.2 would give a unit vector in \(L^\perp\), which could be added to the family.

4. Orthonormal families containing the given one, ordered by inclusion, have unions of chains as upper bounds. Zorn's lemma (first lesson, Theorem 1.1) gives a maximal one, a basis by 3. For separable \(H\), apply the Gram–Schmidt process to a dense sequence.

5. If one basis is finite, \(H\) is finite-dimensional, and both bases have \(\dim H\) elements. Suppose both are infinite, \((e_i)_{i\in I}\) and \((f_j)_{j\in J}\). Each \(e_i\) has at most countably many \(j\) with \(\langle e_i,f_j\rangle\ne0\), by 1. Every \(j\) occurs for some \(i\), since \(f_j\ne0\) is the sum of its expansion in the \(e_i\). So \(J\) is a union of countable sets indexed by \(I\), and \(|J|\le|I|\) (first lesson, Theorem 8.4(3)). Symmetrically \(|I|\le|J|\), and \(|I|=|J|\) by the Cantor–Schröder–Bernstein theorem (first lesson, Theorem 8.1). \(\square\)

## 5. Compact operators

\(T\in B(H)\) is *compact* if the image of the unit ball is relatively compact. \(K(H)\) is the set of compact operators and \(F(H)\) the set of finite-rank operators.

**Theorem 5.1.**
1. \(K(H)\) is a norm-closed two-sided ideal of \(B(H)\) that contains \(F(H)\).
2. \(T\) is compact iff \(T^*\) is compact.
3. \(K(H)\) is the norm closure of \(F(H)\).
4. A compact operator maps weakly convergent sequences to norm convergent sequences.
5. Let \((P_i)\) be a net in \(B(H)\) with \(\|P_i\|\le1\) and \(P_i\xi\to\xi\) for every \(\xi\in H\). Then \(\|T-P_iT\|\to0\) for every compact \(T\). This applies to the projections \(P_n\) onto \(\operatorname{span}\{e_1,\dots,e_n\}\) for an orthonormal basis \((e_k)\) of a separable \(H\) (Theorem 4.1(3)).

**Proof.** 5. The closure \(K\) of \(T(\text{ball})\) is compact. Given \(\varepsilon>0\), cover \(K\) by finitely many balls \(B(y_k,\varepsilon)\), and choose \(i_0\) with \(\|(1-P_i)y_k\|<\varepsilon\) for every \(k\) and every \(i\ge i_0\). For \(y\in K\) with \(\|y-y_k\|<\varepsilon\),
\[
\|(1-P_i)y\|\le\|(1-P_i)y_k\|+\|1-P_i\|\,\|y-y_k\|<3\varepsilon .
\]
So \(\|T-P_iT\|=\sup_{y\in K}\|(1-P_i)y\|\le3\varepsilon\) for \(i\ge i_0\).

1. A finite-rank bounded operator maps the ball into a bounded subset of a finite-dimensional space, which is relatively compact. Sums of compact operators are compact, since the image of the ball lies in the sum of two relatively compact sets. Products with bounded operators are compact, since bounded operators are continuous.

*Closedness.* Let \(T_n\to T\) in norm with \(T_n\) compact, and \(\varepsilon>0\). Choose \(n\) with \(\|T-T_n\|<\varepsilon/3\), and cover \(T_n(\text{ball})\) by finitely many \(\varepsilon/3\)-balls. The \(\varepsilon\)-balls with the same centres cover \(T(\text{ball})\). So \(T(\text{ball})\) is totally bounded, hence relatively compact, since \(H\) is complete.

2. If \(T\) is compact, so is \(TT^*\). For \(\|\xi_n\|\le1\), choose a subsequence along which \(TT^*\xi_n\) converges. Then
\[
\|T^*(\xi_n-\xi_m)\|^2=\langle TT^*(\xi_n-\xi_m),\xi_n-\xi_m\rangle\le2\|TT^*(\xi_n-\xi_m)\|\to0,
\]
so \(T^*\xi_n\) converges along the subsequence. Apply this to \(T^*\) for the converse.

3. Let \(T\) be compact. The closure \(K\) of \(T(\text{ball})\) is a compact metric space, so it has a countable dense subset. The range of \(T\) is the union of the sets \(nT(\text{ball})\), so its closure \(L\) is separable. Let \((e_k)\) be an orthonormal basis of \(L\), and \(P_n\) the projection onto \(\operatorname{span}\{e_1,\dots,e_n\}\). Then \(P_ny\to y\) for \(y\in L\) (Theorem 4.1(3)), and \(P_n=0\) on \(L^\perp\). The argument of 5, applied with \(K\subseteq L\), gives \(\|T-P_nT\|\to0\). Each \(P_nT\) has finite rank.

4. Let \(\xi_n\to\xi\) weakly. Then \((\xi_n)\) is bounded (first lesson, Corollary 4.3(2)), and \(T\xi_n\to T\xi\) weakly. If \(\|T\xi_n-T\xi\|\not\to0\), a subsequence stays at distance \(\ge\varepsilon\). A further subsequence converges in norm, by compactness, and its limit must be the weak limit \(T\xi\), a contradiction. \(\square\)

## 6. The spectral theorem for compact self-adjoint operators

**Lemma 6.1.** Let \(T\) be compact and self-adjoint, \(T\ne0\). Then \(\|T\|\) or \(-\|T\|\) is an eigenvalue of \(T\).

**Proof.** By Corollary 3.2, there are unit vectors \(\xi_n\) with \(\langle T\xi_n,\xi_n\rangle\to\lambda\), where \(|\lambda|=\|T\|\). Then
\[
\|T\xi_n-\lambda\xi_n\|^2=\|T\xi_n\|^2-2\lambda\langle T\xi_n,\xi_n\rangle+\lambda^2\le2\lambda^2-2\lambda\langle T\xi_n,\xi_n\rangle\to0.
\]
A subsequence has \(T\xi_n\to\eta\), by compactness. Then \(\lambda\xi_n\to\eta\), so \(\|\eta\|=|\lambda|\ne0\), and \(T\eta=\lim\lambda T\xi_n=\lambda\eta\). \(\square\)

**Theorem 6.2.** Let \(T\) be compact and self-adjoint, \(T\ne0\). There are an orthonormal family \((e_n)_{n\in N}\), with \(N=\{1,\dots,r\}\) or \(N=\mathbb N\), and real numbers \(\lambda_n\ne0\) with \(|\lambda_1|\ge|\lambda_2|\ge\dots\), tending to \(0\) if \(N=\mathbb N\), such that
\[
T=\sum_n\lambda_n\theta_{e_n,e_n},
\]
with convergence in norm. The nonzero eigenvalues of \(T\) are the \(\lambda_n\). The eigenspace of an eigenvalue \(\mu\ne0\) is spanned by the \(e_n\) with \(\lambda_n=\mu\) and is finite-dimensional. \(T\ge0\) iff all \(\lambda_n>0\).

**Proof.** *The eigenvectors.* Put \(H_1=H\). Lemma 6.1 gives a unit eigenvector \(e_1\) with eigenvalue \(\lambda_1\), \(|\lambda_1|=\|T\|\). The space \(H_2=\{e_1\}^\perp\) is invariant under \(T\), because \(T\) is self-adjoint, and \(T|_{H_2}\) is compact and self-adjoint. Repeat. The process stops if \(T|_{H_{r+1}}=0\). Otherwise it produces \((e_n,\lambda_n)\) for all \(n\), with \(|\lambda_n|\) nonincreasing.

*The eigenvalues tend to \(0\).* If not, \(|\lambda_n|\ge\delta>0\) for all \(n\). Then \(\|Te_n-Te_m\|^2=\lambda_n^2+\lambda_m^2\ge2\delta^2\), so \((Te_n)\) has no convergent subsequence, contradicting compactness.

*The expansion.* \(T-\sum_{n\le k}\lambda_n\theta_{e_n,e_n}\) vanishes on \(\operatorname{span}\{e_1,\dots,e_k\}\) and equals \(T\) on \(H_{k+1}\). So its norm is \(\|T|_{H_{k+1}}\|=|\lambda_{k+1}|\to0\).

*Eigenvalues and eigenspaces.* If \(T\xi=\mu\xi\) with \(\mu\ne0\), then \(\mu\xi=\sum\lambda_n\langle\xi,e_n\rangle e_n\). So \(\xi\) lies in the closed span of the \(e_n\), and \(\langle\xi,e_n\rangle=0\) unless \(\lambda_n=\mu\). Only finitely many \(\lambda_n\) equal \(\mu\), because \(\lambda_n\to0\).

*Positivity.* \(\langle T\xi,\xi\rangle=\sum\lambda_n|\langle\xi,e_n\rangle|^2\). \(\square\)

## 7. The Riesz theory of compact operators

**Theorem 7.1.** Let \(T\in K(H)\) and \(\lambda\in\mathbb C\setminus\{0\}\), and put \(S=T-\lambda\).
1. \(\ker S\) is finite-dimensional.
2. \(S(H)\) is closed.
3. If \(S\) is injective, it is surjective, hence invertible in \(B(H)\).
4. Consequently, every nonzero point of the spectrum \(\sigma(T)\) is an eigenvalue of finite multiplicity.
5. The nonzero eigenvalues of \(T\) have no accumulation point other than \(0\). Each nonzero point of \(\sigma(T)\) is isolated.

**Proof.** 1. On \(\ker S\), \(T=\lambda\). So the unit ball of \(\ker S\) equals \(\lambda^{-1}T(\text{ball of }\ker S)\), which is relatively compact. An infinite orthonormal sequence in \(\ker S\) would have mutual distances \(\sqrt2\). So \(\ker S\) is finite-dimensional.

2. Let \(Sx_n\to y\). Write \(x_n=u_n+v_n\) with \(u_n\in\ker S\) and \(v_n\perp\ker S\), so \(Sv_n=Sx_n\).

*\((v_n)\) is bounded.* Otherwise, along a subsequence with \(\|v_n\|\to\infty\), the unit vectors \(w_n=v_n/\|v_n\|\) have \(Sw_n\to0\). A further subsequence has \(Tw_n\to z\). Then \(\lambda w_n=Tw_n-Sw_n\to z\), so \(w_n\to z/\lambda\), a unit vector orthogonal to \(\ker S\) with \(S(z/\lambda)=0\), which is impossible.

*Conclusion.* A subsequence of the bounded sequence has \(Tv_n\to z'\). Then \(\lambda v_n=Tv_n-Sv_n\to z'-y\), so \(v_n\to v=(z'-y)/\lambda\), and \(Sv=y\).

3. Suppose \(S\) is injective but \(S(H)\ne H\). Each \(S^k\) is of the form \((-\lambda)^k+T_k\) with \(T_k\) compact, so \(S^k(H)\) is closed by 2. The sequence \(H\supsetneq S(H)\supsetneq S^2(H)\supsetneq\dots\) is strictly decreasing: if \(S^k(H)=S^{k+1}(H)\), take \(x\notin S(H)\). Then \(S^kx=S^{k+1}y\) for some \(y\), so \(S^k(x-Sy)=0\), and injectivity gives \(x=Sy\), a contradiction.

Choose unit vectors \(x_k\in S^k(H)\ominus S^{k+1}(H)\). For \(k<m\),
\[
Tx_k-Tx_m=\lambda x_k+\big(Sx_k-Sx_m-\lambda x_m\big),
\]
and the bracket lies in \(S^{k+1}(H)\), which is orthogonal to \(x_k\). So \(\|Tx_k-Tx_m\|\ge|\lambda|\), and \((Tx_k)\) has no convergent subsequence, contradicting compactness. Hence \(S\) is surjective, and its inverse is bounded by the inverse mapping theorem (first lesson, Corollary 5.2).

4. If \(\lambda\ne0\) is not an eigenvalue, then \(S\) is injective, hence invertible by 3, so \(\lambda\notin\sigma(T)\). The multiplicity is finite by 1.

5. Suppose \(\lambda_n\to\lambda\ne0\) are distinct eigenvalues with eigenvectors \(e_n\). Eigenvectors for distinct eigenvalues are linearly independent. Let \(M_n=\operatorname{span}\{e_1,\dots,e_n\}\) and choose unit vectors \(y_n\in M_n\ominus M_{n-1}\). Then \((T-\lambda_n)M_n\subseteq M_{n-1}\). For \(m<n\),
\[
\frac{Ty_n}{\lambda_n}-\frac{Ty_m}{\lambda_m}=y_n-\Big(\frac{(\lambda_n-T)y_n}{\lambda_n}+\frac{Ty_m}{\lambda_m}\Big),
\]
and the bracket lies in \(M_{n-1}\perp y_n\). So the left side has norm \(\ge1\). Since \(\|y_n/\lambda_n\|\) is bounded, this contradicts compactness. Hence the nonzero eigenvalues accumulate only at \(0\), and by 4 every nonzero point of \(\sigma(T)\) is isolated. \(\square\)

## 8. Hilbert tensor products

For a set \(S\), \(\ell^2(S)\) is the space of functions \(c:S\to\mathbb C\) with \(\sum_s|c_s|^2<\infty\), with \(\langle c,d\rangle=\sum_sc_s\bar d_s\). It is a Hilbert space. Completeness: a Cauchy sequence \((c^{(n)})\) converges at each \(s\) to some \(c_s\). For every finite \(F\subseteq S\), \(\sum_{s\in F}|c_s-c^{(n)}_s|^2=\lim_m\sum_{s\in F}|c^{(m)}_s-c^{(n)}_s|^2\le\sup_{m\ge n}\|c^{(m)}-c^{(n)}\|^2\). So \(c-c^{(n)}\in\ell^2(S)\) and \(\|c-c^{(n)}\|\to0\). The functions \(\delta_s\) form an orthonormal basis.

**Theorem 8.1** (Hilbert tensor products). Let \(H\) and \(K\) be Hilbert spaces.
1. There are a Hilbert space \(H\otimes K\) and a bilinear map \((\xi,\eta)\mapsto\xi\otimes\eta\) from \(H\times K\) to \(H\otimes K\) with
\[
\langle\xi\otimes\eta,\xi'\otimes\eta'\rangle=\langle\xi,\xi'\rangle\langle\eta,\eta'\rangle ,
\]
such that the elementary tensors \(\xi\otimes\eta\) span a dense subspace.
2. If \((e_i)_{i\in I}\) and \((f_j)_{j\in J}\) are orthonormal bases of \(H\) and \(K\), then \((e_i\otimes f_j)\) is an orthonormal basis of \(H\otimes K\).
3. (*Universal property.*) Let \(B:H\times K\to\mathcal K\) be a bilinear map into a Hilbert space with \(\langle B(\xi,\eta),B(\xi',\eta')\rangle=\langle\xi,\xi'\rangle\langle\eta,\eta'\rangle\). There is exactly one isometry \(U:H\otimes K\to\mathcal K\) with \(U(\xi\otimes\eta)=B(\xi,\eta)\). It is unitary if the vectors \(B(\xi,\eta)\) span a dense subspace. So \(H\otimes K\) is unique up to a unitary that matches the elementary tensors.

**Proof.** (1) and (2). Fix orthonormal bases as in (2), and put \(H\otimes K=\ell^2(I\times J)\) and \((\xi\otimes\eta)(i,j)=\langle\xi,e_i\rangle\langle\eta,f_j\rangle\).
- By Parseval's identity (Theorem 4.1(3)), \(\sum_{i,j}|\langle\xi,e_i\rangle|^2|\langle\eta,f_j\rangle|^2=\|\xi\|^2\|\eta\|^2\), so \(\xi\otimes\eta\in\ell^2(I\times J)\).
- The map is bilinear, and by Parseval's identity
\[
\langle\xi\otimes\eta,\xi'\otimes\eta'\rangle=\sum_i\langle\xi,e_i\rangle\langle e_i,\xi'\rangle\sum_j\langle\eta,f_j\rangle\langle f_j,\eta'\rangle=\langle\xi,\xi'\rangle\langle\eta,\eta'\rangle .
\]
- \(e_i\otimes f_j=\delta_{(i,j)}\). These form an orthonormal basis, so the elementary tensors span a dense subspace.

(3) For finite sums,
\[
\Big\|\sum_kc_kB(\xi_k,\eta_k)\Big\|^2=\sum_{k,l}c_k\bar c_l\langle\xi_k,\xi_l\rangle\langle\eta_k,\eta_l\rangle=\Big\|\sum_kc_k\,\xi_k\otimes\eta_k\Big\|^2 .
\]
So \(\sum_kc_k\,\xi_k\otimes\eta_k\mapsto\sum_kc_kB(\xi_k,\eta_k)\) is well defined, since a combination equal to \(0\) goes to a vector of norm \(0\), and it is isometric. It extends by continuity to \(H\otimes K\). Uniqueness holds because the elementary tensors are total. An isometry has closed range, so if its range is dense, it is onto. \(\square\)

## 9. Multiplication operators

Let \((Z,\Sigma,\nu)\) be a \(\sigma\)-finite measure space. \(L^\infty(\nu)\) is the space of essentially bounded measurable functions modulo null functions, with the essential supremum norm \(\|f\|_\infty\). For \(f\in L^\infty(\nu)\), \(m_f\) is the operator \(\xi\mapsto f\xi\) on \(L^2(\nu)\). Measure theory is cited from the course *Measure theory*, which gives D. H. Fremlin's *Measure Theory* with Fremlin's paragraph numbers, as [MT 244H], for example.

**Theorem 9.1.**
1. \(f\mapsto m_f\) is an isometric unital \(*\)-homomorphism from \(L^\infty(\nu)\) into \(B(L^2(\nu))\).
2. An operator \(T\in B(L^2(\nu))\) commutes with every \(m_f\) if and only if \(T=m_g\) for some \(g\in L^\infty(\nu)\). So the algebra \(\{m_f:f\in L^\infty(\nu)\}\) equals its own commutant: it is *maximal abelian*.

**Proof.** (1) \(\|f\xi\|_2\le\|f\|_\infty\|\xi\|_2\), and \(\langle f\xi,\eta\rangle=\langle\xi,\bar f\eta\rangle\). For \(\varepsilon>0\), the set \(\{|f|>\|f\|_\infty-\varepsilon\}\) has positive measure. Since \(\nu\) is \(\sigma\)-finite, it contains a set \(E\) with \(0<\nu(E)<\infty\). Then \(\|f1_E\|_2\ge(\|f\|_\infty-\varepsilon)\|1_E\|_2\). So \(\|m_f\|=\|f\|_\infty\).

(2) *Reduction to a finite measure.* Write \(Z\) as a disjoint union of sets \(Z_n\in\Sigma\) of finite measure. Let \(w=\sum_n2^{-n}(1+\nu(Z_n))^{-1}1_{Z_n}\). Then \(w>0\) everywhere, and \(\lambda=w\,\nu\) is a finite measure with the same null sets as \(\nu\).
- So \(L^\infty(\lambda)=L^\infty(\nu)\).
- \(V\xi=w^{-1/2}\xi\) is a unitary from \(L^2(\nu)\) onto \(L^2(\lambda)\), with inverse \(\xi\mapsto w^{1/2}\xi\).
- \(Vm_fV^{-1}=m_f\).

So we may assume \(\nu(Z)<\infty\). Then \(1\in L^2(\nu)\), and \(L^\infty(\nu)\subseteq L^2(\nu)\).

*The function \(g\).* Let \(T\) commute with every \(m_f\), and put \(g=T1\in L^2(\nu)\). For \(f\in L^\infty(\nu)\),
\[
Tf=Tm_f1=m_fT1=fg .
\]
- *\(g\) is essentially bounded.* For \(c>\|T\|\) let \(E=\{|g|>c\}\). Then \(c^2\nu(E)\le\|1_Eg\|_2^2=\|T1_E\|_2^2\le\|T\|^2\nu(E)\), so \(\nu(E)=0\). Hence \(\|g\|_\infty\le\|T\|\).
- *\(T=m_g\).* The two operators agree on \(L^\infty(\nu)\), which contains the simple functions. These are dense in \(L^2(\nu)\) [MT 244H(a)].

The converse holds because the algebra is commutative. \(\square\)

## Exercises

**Exercise 1** (diagonal operators). Let \((e_n)\) be an orthonormal basis of \(H\) and \(T=\sum_n\mu_n\theta_{e_n,e_n}\) for a bounded sequence \((\mu_n)\). Show that \(T\) is compact iff \(\mu_n\to0\).

*Solution.* If \(\mu_n\to0\), the finite-rank truncations converge to \(T\) in norm, so \(T\) is compact by Theorem 5.1(1). If \(|\mu_{n_k}|\ge\delta>0\) along a subsequence, then \(\|Te_{n_k}-Te_{n_l}\|^2\ge2\delta^2\), so \(T\) is not compact. \(\square\)

**Exercise 2** (Hilbert–Schmidt operators). Show that an operator \(T\) with \(\sum_n\|Te_n\|^2<\infty\) for some orthonormal basis \((e_n)\) is compact.

*Solution.* Let \(P_k\) be the projection onto \(\operatorname{span}\{e_1,\dots,e_k\}\). Then \(\|T(1-P_k)\xi\|\le\sum_{n>k}|\langle\xi,e_n\rangle|\|Te_n\|\le\|\xi\|(\sum_{n>k}\|Te_n\|^2)^{1/2}\) by Cauchy–Schwarz. So \(TP_k\to T\) in norm, and each \(TP_k\) has finite rank. \(\square\)

**Exercise 3** (the Volterra operator). On \(L^2[0,1]\), let \((V\xi)(s)=\int_0^s\xi(t)\,dt\). Show that \(V\) is compact and that \(\sigma(V)=\{0\}\).

*Solution.*
- *Compactness:* with an orthonormal basis \((e_n)\), \(\sum_n\|Ve_n\|^2=\int_0^1\sum_n|\langle 1_{[0,s]},\overline{e_n}\rangle|^2ds=\int_0^1\|1_{[0,s]}\|^2ds=\frac12\), by Parseval applied to the basis \((\overline{e_n})\). By Exercise 2, \(V\) is compact.
- *Spectrum:* by Theorem 7.1(4), a nonzero point of \(\sigma(V)\) would be an eigenvalue. If \(V\xi=\lambda\xi\), then \(\xi=\lambda^{-1}V\xi\) is continuous, then \(C^1\), with \(\xi=\lambda\xi'\) and \(\xi(0)=0\). So \(\xi=0\). Finally \(0\in\sigma(V)\), because \(V\) is not invertible in infinite dimensions: a compact invertible operator would make the identity compact. \(\square\)

**Exercise 4** (closed range of \(1-T\)). Let \(T\) be compact. Show that \(\dim\ker(1-T)=\dim\ker(1-T^*)\).

*Solution.*
- Both kernels are finite-dimensional (Theorem 7.1(1), applied to \(T\) and to \(T^*\), which is compact by Theorem 5.1(2)).
- Let \(S=1-T\). Since \(S(H)\) is closed, \(\ker S^*=S(H)^\perp\), and \(H=S(H)\oplus\ker S^*\).
- Suppose \(\dim\ker S<\dim\ker S^*\). Choose an injective linear map \(A\) from \(\ker S\) into \(\ker S^*\) that is not onto, and extend it by \(0\) on \((\ker S)^\perp\). This gives a finite-rank operator. Then \(S'=S+A=1-(T-A)\) is injective with range \(S(H)+A(\ker S)\ne H\), contradicting Theorem 7.1(3).
- Exchanging \(T\) and \(T^*\) gives the reverse inequality. \(\square\)

## Where this leads

The continuous functional calculus and the operator algebra \(B(H)\) are developed in C\*-algebras: continuous functional calculus, automatic continuity, positive cones, approximate identities and quotients. The spectral theorem for bounded self-adjoint operators with projection-valued measures, and Calkin's theorem on the ideals of \(B(H)\), are proved in [The spectral theorem for bounded self-adjoint operators](the-spectral-theorem-for-bounded-self-adjoint-operators.md). The trace class and the operator topologies are in Compact and trace-class operators, the predual of B(H), and the operator topologies. Hilbert tensor products are used for \(L^2\) of a product of Radon measures in Haar measure on locally compact groups, and multiplication operators are the starting point of Abelian operator algebras.

## References

Hilbert (1904–1910), Riesz (1907, 1918) and Fréchet (1907). The Riesz theory of compact operators is from F. Riesz, "Über lineare Funktionalgleichungen", *Acta Mathematica* 41 (1918) 71–98. The proofs are written here in our own words.
