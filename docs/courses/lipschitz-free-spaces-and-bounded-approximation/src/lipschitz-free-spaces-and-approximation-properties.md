# Lipschitz-free spaces and approximation properties

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A metric space \(M\) with a chosen base point has a Banach space \(\mathcal F(M)\) attached to it, its *Lipschitz-free space*. The space \(M\) sits in \(\mathcal F(M)\) with its distances, and every Lipschitz map between metric spaces becomes a bounded linear operator between their free spaces. A Banach space has the *approximation property* if the identity can be approximated, on every compact set, by operators of finite rank; it has the *bounded* approximation property if this can be done with operators of bounded norm. If all distances in \(M\) are at least \(1\), then \(\mathcal F(M)\) has the approximation property, by a theorem of Kalton [K04, Proposition 4.4]; this course proves it for the spaces that it constructs and does not use the general theorem. Kalton asked whether \(\mathcal F(M)\) then also has the bounded approximation property [K04, remarks after Proposition 4.4]. [OpenAI-LF] constructs a countable metric space with all distances at least \(1\) for which it does not. This course gives the construction and the proof.

This lesson gives the definitions, treats the bounded case, in which the free space is the space \(\ell_1\) with another norm, and states the two theorems of the course.

- Lipschitz functions and the free space (Section 1).
- Lipschitz maps induce linear operators (Lemma 2.1).
- The approximation properties (Section 3).
- Bounded spaces with distances at least \(1\): coefficients in \(\ell_1\) (Proposition 4.1).
- The theorems, and new norms on \(\ell_1\) (Section 5).

The lesson follows [OpenAI-LF, Sections 1 and 2]. It uses normed spaces, the dual of a normed space and its completeness, and compact sets in metric spaces (core course [Functional Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D20)).

## 1. Lipschitz functions and the free space

A *pointed metric space* \((M,d,o)\) is a metric space \((M,d)\) with a chosen point \(o\in M\), the *base point*. A real function \(f\) on \(M\) is *Lipschitz* if there is \(\Lambda\ge0\) with \(|f(x)-f(y)|\le\Lambda\,d(x,y)\) for all \(x,y\); the smallest such \(\Lambda\) is written \(\|f\|_{\mathrm{Lip}}\). Let \(\operatorname{Lip}_0(M)\) be the vector space of the Lipschitz functions \(f\) on \(M\) with \(f(o)=0\). On this space \(\|\cdot\|_{\mathrm{Lip}}\) is a norm: if \(\|f\|_{\mathrm{Lip}}=0\), then \(f\) is constant, so \(f=0\).

Let \(\operatorname{Lip}_0(M)^*\) be the dual space, with the dual norm. For \(x\in M\) let \(\delta_x\) be the evaluation at \(x\):
\[
\delta_x(f)=f(x)\qquad(f\in\operatorname{Lip}_0(M)) .
\]
Since \(|f(x)|=|f(x)-f(o)|\le\|f\|_{\mathrm{Lip}}\,d(x,o)\), the functional \(\delta_x\) is bounded, and \(\delta_o=0\).

**Definition.** The *Lipschitz-free space* \(\mathcal F(M)\) is the closure, in \(\operatorname{Lip}_0(M)^*\), of the linear span of the evaluations \(\delta_x\), \(x\in M\).

The dual of a normed space is complete, and a closed subspace of a complete space is complete. So \(\mathcal F(M)\) is a Banach space. By the definition of the dual norm, for every \(u\in\mathcal F(M)\),
\[
\|u\|=\sup\,|u(f)| ,
\]
where the supremum is over the functions \(f\in\operatorname{Lip}_0(M)\) with \(\|f\|_{\mathrm{Lip}}\le1\).
A finite linear combination \(\sum_xc_x\delta_x\) is called an *evaluation combination*. The evaluation combinations are dense in \(\mathcal F(M)\).

**Lemma 1.1.** For all \(x,y\in M\), \(\|\delta_x-\delta_y\|=d(x,y)\). In particular \(\|\delta_x\|=d(x,o)\).

**Proof.** If \(\|f\|_{\mathrm{Lip}}\le1\), then \(|(\delta_x-\delta_y)(f)|=|f(x)-f(y)|\le d(x,y)\). For the other inequality let \(f(z)=d(z,y)-d(o,y)\). Then \(f(o)=0\), and \(|f(z)-f(z')|\) is \(|d(z,y)-d(z',y)|\), which is at most \(d(z,z')\) by the triangle inequality. So \(f\) is admissible, and \((\delta_x-\delta_y)(f)=d(x,y)\). \(\blacksquare\)

So \(x\mapsto\delta_x\) maps \(M\) into \(\mathcal F(M)\) and keeps all distances, and the base point goes to \(0\).

**Example 1.2.** Let \(M=\{0,1,2,\dots\}\) with the distance \(|x-y|\) and the base point \(0\). A function \(f\) with \(f(0)=0\) is determined by its increments \(g_n=f(n)-f(n-1)\), \(n\ge1\), and \(\|f\|_{\mathrm{Lip}}=\sup_n|g_n|\). So for real numbers \(c_1,\dots,c_m\),
\[
\begin{aligned}
\Bigl\|\sum_{n=1}^mc_n(\delta_n-\delta_{n-1})\Bigr\|&=\sup_{|g_n|\le1}\ \sum_{n=1}^mc_ng_n\\
&=\sum_{n=1}^m|c_n| .
\end{aligned}
\]
The free space of this space is the space \(\ell_1\), with the vectors \(\delta_n-\delta_{n-1}\) in the role of the unit vectors.

## 2. Lipschitz maps become linear operators

Let \((N,d,o)\) and \((N',d',o')\) be pointed metric spaces. A map \(u\) from \(N\) to \(N'\) is *pointed* if \(u(o)=o'\), and \(\Lambda\)-*Lipschitz* if \(d'(u(x),u(y))\le\Lambda\,d(x,y)\) for all \(x,y\).

**Lemma 2.1** (linearization). Let \(u\) be a pointed \(\Lambda\)-Lipschitz map from \(N\) to \(N'\). There is exactly one bounded linear operator \(\widehat u\) from \(\mathcal F(N)\) to \(\mathcal F(N')\) with
\[
\widehat u\,\delta_x=\delta_{u(x)}\qquad(x\in N) ,
\]
and \(\|\widehat u\|\le\Lambda\). If \(v\) is a pointed Lipschitz map from \(N'\) to a third space, then \(\widehat{v\circ u}=\widehat v\,\widehat u\); and the identity map of \(N\) induces the identity operator.

**Proof.** For \(f\in\operatorname{Lip}_0(N')\) the function \(f\circ u\) vanishes at \(o\) and \(\|f\circ u\|_{\mathrm{Lip}}\le\Lambda\,\|f\|_{\mathrm{Lip}}\). So \(f\mapsto f\circ u\) is a linear map from \(\operatorname{Lip}_0(N')\) to \(\operatorname{Lip}_0(N)\) of norm at most \(\Lambda\). Its adjoint maps \(\phi\in\operatorname{Lip}_0(N)^*\) to the functional \(f\mapsto\phi(f\circ u)\) and has a norm of at most \(\Lambda\). It maps \(\delta_x\) to \(f\mapsto f(u(x))\), that is, to \(\delta_{u(x)}\). So it maps evaluation combinations to evaluation combinations and, being continuous, \(\mathcal F(N)\) into \(\mathcal F(N')\). Let \(\widehat u\) be its restriction to \(\mathcal F(N)\). A bounded operator is determined by its values on the evaluations, because their span is dense; this gives the uniqueness and the two rules. \(\blacksquare\)

**Corollary 2.2.** Let \(N\subseteq M\) contain the base point of \(M\), with the distance of \(M\), let \(i\) be the inclusion of \(N\) in \(M\), and let \(r\) be a pointed \(1\)-Lipschitz map from \(M\) to \(N\) with \(r(x)=x\) for \(x\in N\). Then \(\widehat r\,\widehat i\) is the identity of \(\mathcal F(N)\), the operator \(\widehat i\) keeps norms, and \(\widehat i\,\widehat r\) is a projection of norm at most \(1\) of \(\mathcal F(M)\) onto the image of \(\widehat i\).

**Proof.** \(r\circ i\) is the identity of \(N\), so \(\widehat r\,\widehat i=\mathrm{Id}\) by Lemma 2.1. Both operators have a norm of at most \(1\); so \(\|v\|=\|\widehat r\,\widehat i\,v\|\le\|\widehat i\,v\|\le\|v\|\). Finally \((\widehat i\,\widehat r)^2=\widehat i\,(\widehat r\,\widehat i)\,\widehat r=\widehat i\,\widehat r\). \(\blacksquare\)

## 3. Approximation properties

Let \(X\) be a Banach space. A bounded linear operator \(T\) from \(X\) to \(X\) has *finite rank* if its range has finite dimension.

**Definition.** The space \(X\) has the *approximation property* (AP) if for every compact set \(C\subseteq X\) and every \(\varepsilon>0\) there is a bounded linear operator \(T\) on \(X\) of finite rank with
\[
\sup_{u\in C}\|Tu-u\|<\varepsilon .
\]
For a number \(\lambda\ge1\), the space has the \(\lambda\)-*bounded approximation property* (\(\lambda\)-BAP) if such operators can always be found with \(\|T\|\le\lambda\). It has the *bounded approximation property* (BAP) if it has \(\lambda\)-BAP for some \(\lambda\), and the *metric approximation property* (MAP) if it has \(1\)-BAP.

In AP the norm of \(T\) may depend on \(C\) and \(\varepsilon\). In BAP one bound has to serve for all compact sets and all \(\varepsilon\). A finite set is compact. So \(\lambda\)-BAP gives, for every finite set \(F\subseteq X\) and every \(\varepsilon>0\), an operator \(T\) of finite rank with \(\|T\|\le\lambda\) and \(\|Tu-u\|<\varepsilon\) for all \(u\in F\). This weak consequence is all that the proofs of this course use of BAP.

**Lemma 3.1.** Let \(S_1,S_2,\dots\) be bounded linear operators on \(X\) with \(\|S_m\|\le\lambda\) for all \(m\), and let \(S_mv\to v\) for every \(v\) in a dense subset \(D\) of \(X\). Then for every compact set \(C\subseteq X\),
\[
\sup_{u\in C}\|S_mu-u\|\to0\qquad(m\to\infty) .
\]

**Proof.** Let \(\varepsilon>0\). The compact set \(C\) is covered by finitely many balls of radius \(\varepsilon\) with centres \(u_1,\dots,u_r\in C\). Choose \(v_i\in D\) with \(\|u_i-v_i\|<\varepsilon\). For all large \(m\), \(\|S_mv_i-v_i\|<\varepsilon\) for \(i=1,\dots,r\). Let \(u\in C\) and choose \(i\) with \(\|u-u_i\|<\varepsilon\), so that \(\|u-v_i\|<2\varepsilon\). Then
\[
\begin{aligned}
\|S_mu-u\|&\le\|S_m(u-v_i)\|\\
&\quad+\|S_mv_i-v_i\|+\|v_i-u\|\\
&\le2\lambda\varepsilon+\varepsilon+2\varepsilon .
\end{aligned}
\]
\(\blacksquare\)

**Lemma 3.2.** Let \(J\) be a bounded linear bijection from a Banach space \(Y\) onto \(X\) with bounded inverse, and let \(X\) have \(\lambda\)-BAP. Then \(Y\) has \(\lambda'\)-BAP with \(\lambda'=\|J\|\,\|J^{-1}\|\,\lambda\). If \(J\) keeps norms, then \(Y\) has \(\lambda\)-BAP, and an operator \(T\) on \(X\) and the operator \(J^{-1}TJ\) on \(Y\) have the same norm, the same rank, and the same errors at corresponding points.

**Proof.** Let \(C\subseteq Y\) be compact and \(\varepsilon>0\). The set \(J(C)\) is compact. Choose \(T\) on \(X\) of finite rank with \(\|T\|\le\lambda\) and \(\|Tw-w\|<\varepsilon/\|J^{-1}\|\) on \(J(C)\). The operator \(J^{-1}TJ\) has finite rank and a norm of at most \(\lambda'\), and for \(u\in C\) the error \(J^{-1}TJu-u\) is \(J^{-1}(TJu-Ju)\), which has a norm less than \(\varepsilon\). The last statement is clear. \(\blacksquare\)

**Example 3.3.** The space \(\ell_1\) has MAP: the projections \(q_m\) onto the first \(m\) coordinates have finite rank and norm \(1\), and \(q_mc\to c\) for every \(c\in\ell_1\); apply Lemma 3.1.

## 4. Bounded spaces with distances at least one

A metric space is *uniformly discrete* if the distances between different points are bounded below by a positive number. After a change of scale this number is \(1\). The *diameter* of a metric space is the supremum of its distances.

For a countable set \(E\) let \(\ell_1(E)\) be the space of the families \(c=(c_x)_{x\in E}\) of real numbers with \(\|c\|_1=\sum_x|c_x|<\infty\).

**Proposition 4.1** (coefficients). Let \((N,d,o)\) be a countable pointed metric space with \(d(x,y)\ge1\) for \(x\ne y\) and diameter at most \(B<\infty\), and \(N\ne\{o\}\). For \(c\in\ell_1(N\setminus\{o\})\) the series
\[
Jc=\sum_{x\ne o}c_x\,\delta_x
\]
converges in \(\mathcal F(N)\). The map \(J\) is a linear bijection from \(\ell_1(N\setminus\{o\})\) onto \(\mathcal F(N)\), and
\[
\tfrac12\,\|c\|_1\le\|Jc\|\le B\,\|c\|_1 .
\]
The space \(\mathcal F(N)\) has \(2B\)-BAP.

**Proof.** *Finitely many coefficients.* Let \(c\) have finitely many entries different from \(0\). By Lemma 1.1, \(\|\delta_x\|=d(x,o)\le B\); so \(\|Jc\|\le B\|c\|_1\). For the lower bound define a function \(f\) on \(N\): at a point \(x\ne o\) with \(c_x\ne0\) let \(f(x)=\tfrac12\) if \(c_x>0\) and \(f(x)=-\tfrac12\) if \(c_x<0\); at all other points let \(f=0\). Then \(f(o)=0\), and two values of \(f\) differ by at most \(1\), which is at most the distance of the two points. So \(\|f\|_{\mathrm{Lip}}\le1\) and
\[
\|Jc\|\ge(Jc)(f)=\tfrac12\sum_{x\ne o}|c_x| .
\]

*All of \(\ell_1\).* By the upper bound the series for \(Jc\) converges absolutely for every \(c\in\ell_1(N\setminus\{o\})\), and both bounds pass to the limit. So \(J\) is linear, bounded and injective, and \(\|J^{-1}w\|_1\le2\|w\|\) on its range. The range is closed: if \(Jc_m\) converges, then \(\|c_m-c_l\|_1\le2\|Jc_m-Jc_l\|\) shows that \((c_m)\) is a Cauchy sequence, with a limit \(c\), and \(Jc_m\to Jc\). The range contains every \(\delta_x\), and the span of the evaluations is dense in \(\mathcal F(N)\). So the range is \(\mathcal F(N)\).

*The approximation property.* Since \(N\ne\{o\}\), \(B\ge1\). Choose finite sets \(E_1\subseteq E_2\subseteq\dots\) with union \(N\setminus\{o\}\), and let \(q_m\) be the projection of \(\ell_1(N\setminus\{o\})\) that keeps the coordinates in \(E_m\) and replaces the others by \(0\). The operators
\[
S_m=J\,q_m\,J^{-1}
\]
on \(\mathcal F(N)\) have finite rank and \(\|S_m\|\le B\cdot1\cdot2\). Every evaluation combination \(v\) satisfies \(S_mv=v\) for all large \(m\). By Lemma 3.1, \(S_m\to\mathrm{Id}\) uniformly on every compact set. \(\blacksquare\)

So the free space of a bounded countable space with distances at least \(1\) is the space \(\ell_1\) with an equivalent norm, and the points \(x\ne o\) of the space are the unit vectors. The norm depends on the metric. The proposition bounds the constant of the bounded approximation property by twice the diameter. The theorem of the next section shows that the constant can be large.

## 5. The theorems

**Theorem 5.1** (bounded blocks; [OpenAI-LF, Section 1]). For every integer \(p\ge1\) there are a countably infinite pointed metric space \((M_p,d_p,o)\) and a finite set \(A_p\subseteq M_p\) that contains \(o\), such that
\[
\begin{gathered}
d_p(x,y)\ge1\quad(x\ne y),\\
\operatorname{diam}M_p\le B_p ,
\end{gathered}
\]
with \(B_p=300p^2+150p+5\), and such that every bounded linear operator \(T_0\) of finite rank on \(\mathcal F(M_p)\) with \(\|T_0\|\le p\) satisfies
\[
\max_{a\in A_p}\|T_0\delta_a-\delta_a\|\ge\tfrac12 .
\]

The points of \(A_p\) are called *anchors*. The theorem says that no operator of finite rank and norm at most \(p\) is close to the identity at all the finitely many anchors. In particular \(\mathcal F(M_p)\) does not have \(p\)-BAP. By Proposition 4.1 it has \(2B_p\)-BAP. The construction of the space \(M_p\) is the subject of [Colored graphs with a tree limit](colored-graphs-with-a-tree-limit.md), and the proof of the theorem is given in [Signed measures and matched walks](signed-measures-and-matched-walks.md) and [Scalar tests and the anchor obstruction](scalar-tests-and-the-anchor-obstruction.md).

**Theorem 5.2** ([OpenAI-LF, Section 1]). There is a countable pointed metric space \((M,d,o)\) with \(d(x,y)\ge1\) for \(x\ne y\) such that \(\mathcal F(M)\) has the approximation property and does not have \(\lambda\)-BAP for any \(\lambda\). The space \(M\) is unbounded, and it has a closed bounded ball that is not compact.

Theorem 5.2 is deduced from Theorem 5.1 in [A wedge of bounded blocks](a-wedge-of-bounded-blocks.md): the spaces \(M_p\) are glued at their base points.

A metric space with distances at least \(1\) in which every closed bounded ball is compact has finite balls. For countable spaces of this kind the free space has MAP, by a theorem of Dalet quoted in [OpenAI-LF, Section 1]; that theorem is not used here. It explains why the example must contain a bounded infinite set.

The first consequence of Theorem 5.1 concerns norms on \(\ell_1\).

**Corollary 5.3** (new norms on \(\ell_1\)). For every integer \(p\ge1\) the real space \(\ell_1\) has a norm \(\|\cdot\|_p\) with
\[
\tfrac12\,\|c\|_1\le\|c\|_p\le B_p\,\|c\|_1
\]
such that \((\ell_1,\|\cdot\|_p)\) has \(2B_p\)-BAP and does not have \(p\)-BAP. For \(p=1\): \(\ell_1\) has an equivalent norm without the metric approximation property.

**Proof.** The set \(M_p\setminus\{o\}\) is countably infinite; number its points, so that \(\ell_1(M_p\setminus\{o\})\) becomes \(\ell_1\). Let \(J_p\) be the map of Proposition 4.1 for \(M_p\) and \(B=B_p\), and put \(\|c\|_p=\|J_pc\|\). The two inequalities are those of Proposition 4.1. For the new norm \(J_p\) is a linear bijection onto \(\mathcal F(M_p)\) that keeps norms. By Lemma 3.2 the new norm has \(2B_p\)-BAP. If it had \(p\)-BAP, then so would \(\mathcal F(M_p)\), again by Lemma 3.2. Applied to the finite set \(\{\delta_a:a\in A_p\}\) and \(\varepsilon=\tfrac12\), this would give an operator of finite rank and norm at most \(p\) with \(\|T\delta_a-\delta_a\|<\tfrac12\) for all \(a\in A_p\), against Theorem 5.1. \(\blacksquare\)

Whether every equivalent norm on \(\ell_1\) has MAP was a known question, mentioned by Kalton [K04, remarks after Proposition 4.4]; the case \(p=1\) answers it.

## 6. Exercises

**6.1.** Let \(N=\{o,x,y\}\) with all three distances equal to \(1\). Compute \(\|\delta_x-\delta_y\|\) and \(\|\delta_x+\delta_y\|\), and conclude that both constants \(\tfrac12\) and \(B\) of Proposition 4.1 cannot be improved in general.

**6.2.** Let \(M\) be a finite pointed metric space with \(n+1\) points. Show that the evaluations \(\delta_x\), \(x\ne o\), form a basis of \(\mathcal F(M)\), so that \(\dim\mathcal F(M)=n\).

**6.3.** Let \(X\) be a separable Banach space with \(\lambda\)-BAP. Show that there is a sequence of operators \(T_m\) of finite rank with \(\|T_m\|\le\lambda\) and \(T_mu\to u\) for every \(u\in X\).

**6.4.** Let \(X\) have \(\lambda\)-BAP and let \(P\) be a bounded projection of \(X\) onto a closed subspace \(Y\). Show that \(Y\) has \(\lambda'\)-BAP with \(\lambda'=\max\{1,\|P\|\}\,\lambda\).

**6.5.** Let \((M,d,o)\) be a pointed metric space and \(o'\in M\). Show that \(f\mapsto f-f(o')\) is a linear bijection from \(\operatorname{Lip}_0(M)\) for the base point \(o\) onto \(\operatorname{Lip}_0(M)\) for the base point \(o'\) that keeps norms, and conclude that the free spaces for the two base points are isometric.

## 7. Solutions

**6.1.** \(\|\delta_x-\delta_y\|=d(x,y)=1\) by Lemma 1.1, and \(\|c\|_1=2\) for this combination; so \(\tfrac12\) is attained. A function \(f\) with \(f(o)=0\) and \(\|f\|_{\mathrm{Lip}}\le1\) has \(|f(x)|\le1\) and \(|f(y)|\le1\), and \(f(x)=f(y)=1\) is admissible. So \(\|\delta_x+\delta_y\|=2=B\,\|c\|_1\) with \(B=1\), the diameter.

**6.2.** The \(n\) evaluations span \(\mathcal F(M)\), which is the span itself because a subspace of finite dimension is closed. They are linearly independent: for \(x\ne o\) the function that is \(1\) at \(x\) and \(0\) elsewhere is Lipschitz on a finite space and vanishes at \(o\); a combination \(\sum_yc_y\delta_y=0\) applied to it gives \(c_x=0\).

**6.3.** Let \(u_1,u_2,\dots\) be dense in \(X\). For every \(m\) choose \(T_m\) of finite rank with \(\|T_m\|\le\lambda\) and \(\|T_mu_i-u_i\|<1/m\) for \(i\le m\). Then \(T_mu_i\to u_i\) for every \(i\), and Lemma 3.1 for the compact set \(\{u\}\) gives \(T_mu\to u\) for every \(u\).

**6.4.** Let \(C\subseteq Y\) be compact and \(\varepsilon>0\). Choose \(T\) on \(X\) of finite rank with \(\|T\|\le\lambda\) and \(\|Tu-u\|<\varepsilon/\max\{1,\|P\|\}\) on \(C\). The operator \(PT\), restricted to \(Y\), maps \(Y\) to \(Y\), has finite rank and a norm of at most \(\|P\|\lambda\), and for \(u\in C\): \(\|PTu-u\|=\|P(Tu-u)\|<\varepsilon\), because \(Pu=u\).

**6.5.** The function \(f-f(o')\) vanishes at \(o'\) and has the same Lipschitz constant as \(f\); the inverse map is \(g\mapsto g-g(o)\). The adjoint of this bijection is a bijection between the two dual spaces that keeps norms. It maps the evaluation at \(x\) for the base point \(o'\) to the functional \(f\mapsto f(x)-f(o')\), that is, to \(\delta_x-\delta_{o'}\) for the base point \(o\). These span the same subspace as the \(\delta_x\), because \(\delta_o=0\) gives \(\delta_{o'}=-(\delta_o-\delta_{o'})\). So the adjoint maps one free space onto the other.

## References

- [OpenAI-LF] OpenAI, *A uniformly discrete counterexample to bounded approximation in Lipschitz-free spaces*, OpenAI Math Release preprint, 26 September 2026, Sections 1 and 2. https://github.com/openai/math/tree/main/preprints/Failure-of-Bounded-Approximation-in-a-Lipschitz-Free-Space-over-a-Uniformly-Discrete-Metric-Space-September-26-2026
- [K04] N. J. Kalton, *Spaces of Lipschitz and Hölder functions and their applications*, Collectanea Mathematica 55 (2004), 171–217, Proposition 4.4 and the remarks after it; free on the archive of the author's university. https://kaltonmemorial.missouri.edu/assets/docs/collect2004.pdf
