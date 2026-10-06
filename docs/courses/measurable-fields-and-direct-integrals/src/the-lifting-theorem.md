# The lifting theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

An element of \(L^\infty(\mu)\) is a class of functions that agree almost everywhere. A *lifting* chooses one representative of every class, all at once, so that sums, products and complex conjugates of representatives are again the chosen representatives. This lesson proves that liftings exist on every complete strictly localizable measure space of positive measure (Theorem 6.2, the lifting theorem of von Neumann and Maharam), in the form of a Boolean homomorphism from the measure algebra into the measurable sets, and deduces the form used for \(L^\infty\) (Corollary 6.3).

The theorem was proved by von Neumann for Lebesgue measure on the interval [von Neumann 1931] and by Maharam in general [Maharam 1958]. The proof below follows the one in [Fremlin, Volume 3, Section 341], which is free to read; the formula for the one-step extension in Lemma 2.1 is due to Graf and von Weizsäcker.

We use from the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10): measure spaces, complete and strictly localizable measure spaces ([Fremlin, Volume 2, 211E](https://www1.essex.ac.uk/maths/people/fremlin/chap21.pdf)), conditional expectations ([Fremlin, Volume 2, 233D](https://www1.essex.ac.uk/maths/people/fremlin/chap23.pdf)) and Lévy's martingale theorem ([Fremlin, Volume 2, 275I](https://www1.essex.ac.uk/maths/people/fremlin/chap27.pdf)). We also use Zorn's lemma.

## 1. Measure algebras

Let \((X,\Sigma,\mu)\) be a measure space and \(\mathcal N=\{E\in\Sigma:\mu E=0\}\). Write \(E\sim F\) when \(E\triangle F\in\mathcal N\). This equivalence relation is compatible with complements, finite unions and finite intersections, so the quotient \(\mathfrak A=\Sigma/{\sim}\) is a Boolean algebra, the *measure algebra* of \(\mu\). We write \(E^\bullet\) for the class of \(E\); the map \(E\mapsto E^\bullet\) preserves the Boolean operations. We write \(a\cap b\), \(a\cup b\), \(1\setminus a\), \(0=\emptyset^\bullet\), \(1=X^\bullet\), and \(a\subseteq b\) when \(a\cap b=a\). A *subalgebra* is a subset containing \(0\) and \(1\) and closed under these operations. A *Boolean homomorphism* between Boolean algebras preserves \(\cap\), \(\cup\), complements, \(0\) and \(1\).

**Definition 1.1.**

1. A *lifting* of \(\mu\) is a Boolean homomorphism \(\theta:\mathfrak A\to\Sigma\) with \((\theta a)^\bullet=a\) for every \(a\in\mathfrak A\).
2. Let \(\mathfrak B\) be a subalgebra of \(\mathfrak A\). A *partial lower density* with domain \(\mathfrak B\) is a map \(\theta:\mathfrak B\to\Sigma\) with \((\theta b)^\bullet=b\) for every \(b\in\mathfrak B\), \(\theta0=\emptyset\) and \(\theta(a\cap b)=\theta a\cap\theta b\) for all \(a,b\in\mathfrak B\). If \(\mathfrak B=\mathfrak A\), \(\theta\) is a *lower density*.

A partial lower density is monotone: if \(a\subseteq b\), then \(\theta a=\theta(a\cap b)=\theta a\cap\theta b\subseteq\theta b\). A lifting is a lower density. If \(\mu X=0\) and \(X\neq\emptyset\), there is no lifting, since \(\mathfrak A=\{0\}\) and a lifting would send \(0=1\) both to \(\emptyset\) and to \(X\).

For the rest of this section and in Sections 2 to 4, \(\mu\) is a *probability measure*, \(\mu X=1\). Then \(\bar\mu(E^\bullet)=\mu E\) is well defined on \(\mathfrak A\), and \(\bar\mu a=0\) only for \(a=0\).

**Lemma 1.2.** Let \(\mu\) be a probability measure.

1. For \(E_n\in\Sigma\), \(\bigl(\bigcup_nE_n\bigr)^\bullet\) is the least upper bound of the elements \(E_n^\bullet\) in \(\mathfrak A\). We write \(\sup_na_n\) for the least upper bound of a sequence.
2. Every subset \(S\) of \(\mathfrak A\) has a least upper bound \(\sup S\), and \(\sup S=\sup S_0\) for some countable \(S_0\subseteq S\). Likewise \(S\) has a greatest lower bound \(\inf S=1\setminus\sup\{1\setminus s:s\in S\}\).

*Proof.* (1) \(\bigcup_nE_n\) contains each \(E_n\). If \(F^\bullet\supseteq E_n^\bullet\) for all \(n\), then each \(E_n\setminus F\) is null, so \(\bigl(\bigcup_nE_n\bigr)\setminus F\) is null.

(2) Let \(\beta\) be the supremum of \(\bar\mu(\sup S_0)\) over the countable \(S_0\subseteq S\), and choose countable sets \(S_k\) with \(\bar\mu(\sup S_k)\to\beta\). The countable set \(S_0=\bigcup_kS_k\) has \(\bar\mu(\sup S_0)=\beta\). For \(s\in S\), the countable set \(S_0\cup\{s\}\) has \(\bar\mu(\sup(S_0\cup\{s\}))\le\beta\), while \(\sup(S_0\cup\{s\})\supseteq\sup S_0\); so \(\bar\mu(s\setminus\sup S_0)=0\) and \(s\subseteq\sup S_0\). Thus \(\sup S_0\) is an upper bound of \(S\), and every upper bound of \(S\) is one of \(S_0\), hence contains \(\sup S_0\). \(\square\)

A subalgebra \(\mathfrak B\) is *closed* if \(\sup_nb_n\in\mathfrak B\) for every sequence in \(\mathfrak B\). By Lemma 1.2(2), a closed subalgebra contains the supremum and the infimum of each of its subsets. In particular, for \(e\in\mathfrak A\) the element
\[
\operatorname{upr}(e,\mathfrak B)=\inf\{b\in\mathfrak B:b\supseteq e\}
\]
belongs to \(\mathfrak B\), and it is the smallest element of \(\mathfrak B\) that contains \(e\). For \(S\subseteq\mathfrak A\), let \(\langle S\rangle\) be the intersection of all closed subalgebras that contain \(S\); it is the smallest closed subalgebra containing \(S\).

**Lemma 1.3.** Let \(\mu\) be a probability measure.

1. Let \(\mathfrak B\) be a closed subalgebra and \(e\in\mathfrak A\). The elements \((a\cap e)\cup(b\setminus e)\), \(a,b\in\mathfrak B\), form a closed subalgebra \(\mathfrak B_1\); it is the subalgebra generated by \(\mathfrak B\cup\{e\}\).
2. For a closed subalgebra \(\mathfrak B\), the family \(\Sigma_{\mathfrak B}=\{E\in\Sigma:E^\bullet\in\mathfrak B\}\) is a \(\sigma\)-algebra containing \(\mathcal N\).
3. Let \(\mathfrak B_0\subseteq\mathfrak B_1\subseteq\cdots\) be closed subalgebras and \(\mathfrak B=\langle\bigcup_n\mathfrak B_n\rangle\). Then \(\Sigma_{\mathfrak B}\) is the \(\sigma\)-algebra generated by \(\bigcup_n\Sigma_{\mathfrak B_n}\).

*Proof.* (1) Since \(e\) and \(1\setminus e\) are disjoint,
\[
\bigl((a\cap e)\cup(b\setminus e)\bigr)\cap\bigl((a'\cap e)\cup(b'\setminus e)\bigr)=(a\cap a'\cap e)\cup\bigl((b\cap b')\setminus e\bigr),
\qquad
1\setminus\bigl((a\cap e)\cup(b\setminus e)\bigr)=\bigl((1\setminus a)\cap e\bigr)\cup\bigl((1\setminus b)\setminus e\bigr).
\]
So \(\mathfrak B_1\) is a subalgebra. It contains \(\mathfrak B\) (take \(a=b\)) and \(e\) (take \(a=1\), \(b=0\)), and every subalgebra containing \(\mathfrak B\cup\{e\}\) contains it. By Lemma 1.2(1), applied to representatives, \(\sup_n\bigl((a_n\cap e)\cup(b_n\setminus e)\bigr)=\bigl((\sup_na_n)\cap e\bigr)\cup\bigl((\sup_nb_n)\setminus e\bigr)\), so \(\mathfrak B_1\) is closed.

(2) \(E\mapsto E^\bullet\) preserves complements and, by Lemma 1.2(1), countable unions; and \(E^\bullet=0\in\mathfrak B\) for \(E\in\mathcal N\).

(3) Let \(\mathcal T\) be the \(\sigma\)-algebra generated by \(\bigcup_n\Sigma_{\mathfrak B_n}\). Then \(\mathcal T\subseteq\Sigma_{\mathfrak B}\) by (2). Conversely, \(\{F^\bullet:F\in\mathcal T\}\) is a closed subalgebra, by Lemma 1.2(1), which contains every \(\mathfrak B_n\); so it contains \(\mathfrak B\). Hence for \(E\in\Sigma_{\mathfrak B}\) there is \(F\in\mathcal T\) with \(F^\bullet=E^\bullet\). Then \(E\triangle F\in\mathcal N\subseteq\Sigma_{\mathfrak B_0}\subseteq\mathcal T\), and \(E=F\triangle(E\triangle F)\in\mathcal T\). \(\square\)

## 2. Adding one element

**Lemma 2.1.** Let \(\mu\) be a probability measure, \(\mathfrak B\) a closed subalgebra, \(\theta:\mathfrak B\to\Sigma\) a partial lower density and \(e\in\mathfrak A\). Then \(\theta\) extends to a partial lower density \(\theta_1\) on the subalgebra \(\mathfrak B_1\) generated by \(\mathfrak B\cup\{e\}\).

*Proof.* Put \(v=\operatorname{upr}(e,\mathfrak B)\) and \(w=\operatorname{upr}(1\setminus e,\mathfrak B)\), elements of \(\mathfrak B\) with \(e\subseteq v\) and \(1\setminus e\subseteq w\), and choose \(E\in\Sigma\) with \(E^\bullet=e\). By Lemma 1.3(1) every element of \(\mathfrak B_1\) is \((a\cap e)\cup(b\setminus e)\) with \(a,b\in\mathfrak B\). Define
\[
\theta_1\bigl((a\cap e)\cup(b\setminus e)\bigr)=\Bigl(\theta\bigl((a\cap v)\cup(b\setminus v)\bigr)\cap E\Bigr)\cup\Bigl(\theta\bigl((a\setminus w)\cup(b\cap w)\bigr)\setminus E\Bigr).
\]

*Well defined.* Suppose \((a\cap e)\cup(b\setminus e)=(a'\cap e)\cup(b'\setminus e)\). Intersecting with \(e\) and with \(1\setminus e\) gives \(a\cap e=a'\cap e\) and \(b\setminus e=b'\setminus e\). So \(a\triangle a'\subseteq1\setminus e\), that is, \(e\subseteq1\setminus(a\triangle a')\in\mathfrak B\), and therefore \(v\subseteq1\setminus(a\triangle a')\); also \(a\triangle a'\subseteq1\setminus e\subseteq w\). Likewise \(1\setminus e\subseteq1\setminus(b\triangle b')\in\mathfrak B\) gives \(w\subseteq1\setminus(b\triangle b')\), and \(b\triangle b'\subseteq e\subseteq v\). Hence \(a\cap v=a'\cap v\), \(a\setminus w=a'\setminus w\), \(b\setminus v=b'\setminus v\) and \(b\cap w=b'\cap w\), and the two expressions for \(\theta_1\) agree.

*Values.* Write \(p(a,b)=(a\cap v)\cup(b\setminus v)\) and \(q(a,b)=(a\setminus w)\cup(b\cap w)\), elements of \(\mathfrak B\). Since \(e\subseteq v\) and \(1\setminus e\subseteq w\), we have \(p(a,b)\cap e=a\cap e\) and \(q(a,b)\setminus e=b\setminus e\). As \((\theta c)^\bullet=c\) and \(E^\bullet=e\),
\[
\Bigl(\theta_1\bigl((a\cap e)\cup(b\setminus e)\bigr)\Bigr)^\bullet=\bigl(p(a,b)\cap e\bigr)\cup\bigl(q(a,b)\setminus e\bigr)=(a\cap e)\cup(b\setminus e).
\]

*Intersections.* As in Lemma 1.3(1), \(p(a,b)\cap p(a',b')=p(a\cap a',b\cap b')\) and \(q(a,b)\cap q(a',b')=q(a\cap a',b\cap b')\). For sets \(P,Q,P',Q'\) one has \(\bigl((P\cap E)\cup(Q\setminus E)\bigr)\cap\bigl((P'\cap E)\cup(Q'\setminus E)\bigr)=(P\cap P'\cap E)\cup\bigl((Q\cap Q')\setminus E\bigr)\). Since \(\theta\) preserves intersections, \(\theta_1(c\cap c')=\theta_1c\cap\theta_1c'\) for \(c,c'\in\mathfrak B_1\). Also \(\theta_10=\emptyset\), taking \(a=b=0\).

*Extension.* For \(a\in\mathfrak B\), take \(b=a\): then \(p(a,a)=q(a,a)=a\) and \(\theta_1a=(\theta a\cap E)\cup(\theta a\setminus E)=\theta a\). \(\square\)

## 3. Increasing sequences

**Lemma 3.1.** Let \(\mu\) be a probability measure, \(\mathfrak B_0\subseteq\mathfrak B_1\subseteq\cdots\) closed subalgebras, and \(\theta_n:\mathfrak B_n\to\Sigma\) partial lower densities such that \(\theta_{n+1}\) extends \(\theta_n\). Let \(\mathfrak B=\langle\bigcup_n\mathfrak B_n\rangle\). Then there is a partial lower density \(\theta\) with domain \(\mathfrak B\) that extends every \(\theta_n\).

*Proof.* Write \(\Sigma_n=\Sigma_{\mathfrak B_n}\) and \(\Sigma_\infty=\Sigma_{\mathfrak B}\); by Lemma 1.3(3), \(\Sigma_\infty\) is generated by \(\bigcup_n\Sigma_n\). For \(a\in\mathfrak B\) choose \(G_a\in\Sigma\) with \(G_a^\bullet=a\), and for each \(n\) a \(\Sigma_n\)-measurable function \(g_{a,n}:X\to[0,1]\) that is a conditional expectation of \(1_{G_a}\) given \(\Sigma_n\) ([Fremlin, Volume 2, 233D](https://www1.essex.ac.uk/maths/people/fremlin/chap23.pdf); a version with values in \([0,1]\) exists because \(0\le1_{G_a}\le1\) and \(\mathcal N\subseteq\Sigma_n\)). By Lévy's martingale theorem ([Fremlin, Volume 2, 275I](https://www1.essex.ac.uk/maths/people/fremlin/chap27.pdf)), \(g_{a,n}\) converges almost everywhere to a conditional expectation of \(1_{G_a}\) given \(\Sigma_\infty\). Since \(G_a\in\Sigma_\infty\), that is \(1_{G_a}\) itself, so
\[
\lim_{n\to\infty}g_{a,n}=1_{G_a}\quad\text{almost everywhere.}
\tag{3.1}
\]
The class of \(g_{a,n}\) modulo null functions depends only on \(a\) and \(n\). For \(k\ge1\) put \(H_{k,n}(a)=\{x:g_{a,n}(x)\ge1-2^{-k}\}\in\Sigma_n\), so that \(H_{k,n}(a)^\bullet\in\mathfrak B_n\) depends only on \(a\), \(k\), \(n\). Put
\[
\tilde H_{k,n}(a)=\theta_n\bigl(H_{k,n}(a)^\bullet\bigr),\qquad
\theta a=\bigcap_{k\ge1}\bigcup_{n}\bigcap_{m\ge n}\tilde H_{k,m}(a)\in\Sigma .
\]

*Zero and order.* If \(a=0\), then \(G_0\) is null, \(g_{0,n}=0\) almost everywhere, \(H_{k,n}(0)^\bullet=0\) and \(\tilde H_{k,n}(0)=\emptyset\); so \(\theta0=\emptyset\). If \(a\subseteq b\), then \(1_{G_a}\le1_{G_b}\) almost everywhere, hence \(g_{a,n}\le g_{b,n}\) almost everywhere, \(H_{k,n}(a)^\bullet\subseteq H_{k,n}(b)^\bullet\), \(\tilde H_{k,n}(a)\subseteq\tilde H_{k,n}(b)\) and \(\theta a\subseteq\theta b\).

*Intersections.* For \(a,b\in\mathfrak B\), \(1_{G_{a\cap b}}\ge1_{G_a}+1_{G_b}-1\) almost everywhere, so \(g_{a\cap b,n}\ge g_{a,n}+g_{b,n}-1\) almost everywhere. Hence \(H_{k+1,n}(a)\cap H_{k+1,n}(b)\setminus H_{k,n}(a\cap b)\) is null, and
\[
\tilde H_{k,n}(a\cap b)\supseteq\theta_n\bigl(H_{k+1,n}(a)^\bullet\cap H_{k+1,n}(b)^\bullet\bigr)=\tilde H_{k+1,n}(a)\cap\tilde H_{k+1,n}(b).
\]
If \(x\in\theta a\cap\theta b\) and \(k\ge1\), there are \(n_1,n_2\) with \(x\in\tilde H_{k+1,m}(a)\) for \(m\ge n_1\) and \(x\in\tilde H_{k+1,m}(b)\) for \(m\ge n_2\); then \(x\in\tilde H_{k,m}(a\cap b)\) for \(m\ge\max(n_1,n_2)\). So \(\theta a\cap\theta b\subseteq\theta(a\cap b)\), and the reverse inclusion holds by monotonicity.

*Classes.* Let \(V_a=\bigcap_k\bigcup_n\bigcap_{m\ge n}H_{k,m}(a)=\{x:\liminf_mg_{a,m}(x)\ge1\}\). Since the \(g_{a,m}\) take values in \([0,1]\), (3.1) shows that \(V_a\triangle G_a\) is null. Each \(\tilde H_{k,m}(a)\triangle H_{k,m}(a)\) is null, because \(\bigl(\theta_m c\bigr)^\bullet=c\); so \(\theta a\triangle V_a\subseteq\bigcup_{k,m}\tilde H_{k,m}(a)\triangle H_{k,m}(a)\) is null, and \((\theta a)^\bullet=a\).

*Extension.* Let \(a\in\mathfrak B_n\) and \(m\ge n\). Then \(G_a\in\Sigma_m\), so \(g_{a,m}=1_{G_a}\) almost everywhere, \(H_{k,m}(a)^\bullet=a\), and \(\tilde H_{k,m}(a)=\theta_ma=\theta_na\) for every \(k\). For \(r<n\) the set \(\bigcap_{m\ge r}\tilde H_{k,m}(a)\) is contained in \(\theta_na\), and for \(r\ge n\) it equals \(\theta_na\). So \(\theta a=\theta_na\). \(\square\)

## 4. Lower densities of probability spaces

**Theorem 4.1.** Every probability space \((X,\Sigma,\mu)\) has a lower density \(\theta\) with \(\theta1=X\).

*Proof.* Let \(\mathcal P\) be the set of partial lower densities whose domain is a closed subalgebra and which send \(1\) to \(X\), ordered by extension. It contains the map \(0\mapsto\emptyset\), \(1\mapsto X\) on \(\{0,1\}\). We show that every non-empty chain \(\mathcal C\subseteq\mathcal P\) has an upper bound in \(\mathcal P\).

If \(\mathcal C\) has a countable cofinal subset, it has a cofinal increasing sequence \(\theta_0\le\theta_1\le\cdots\), and Lemma 3.1 extends all \(\theta_n\), hence all members of \(\mathcal C\), to a member of \(\mathcal P\).

Otherwise, let \(\mathfrak B\) be the union of the domains of the members of \(\mathcal C\), and \(\theta\) their common extension to \(\mathfrak B\), well defined because \(\mathcal C\) is a chain. It is a partial lower density on the subalgebra \(\mathfrak B\). The subalgebra \(\mathfrak B\) is closed: given \(c_k\in\mathfrak B\), choose \(\psi_k\in\mathcal C\) with \(c_k\) in its domain; the countable set \(\{\psi_k\}\) is not cofinal, so some \(\psi\in\mathcal C\) is not below any \(\psi_k\), hence above all of them, and \(\sup_kc_k\) lies in the closed domain of \(\psi\).

By Zorn's lemma \(\mathcal P\) has a maximal element \(\theta\), with domain \(\mathfrak B\). If \(e\in\mathfrak A\setminus\mathfrak B\), Lemma 2.1 extends \(\theta\) to the subalgebra generated by \(\mathfrak B\cup\{e\}\), which is closed by Lemma 1.3(1); this contradicts maximality. So \(\mathfrak B=\mathfrak A\). \(\square\)

## 5. From lower densities to liftings

A subset \(I\) of a Boolean algebra is an *ideal* if \(0\in I\), \(b\subseteq a\in I\) implies \(b\in I\), and \(a,b\in I\) implies \(a\cup b\in I\); it is *proper* if \(1\notin I\).

**Lemma 5.1.** Every proper ideal \(I\) of a Boolean algebra \(\mathfrak A\) is contained in a proper ideal \(M\) such that \(\pi(a)=0\) for \(a\in M\) and \(\pi(a)=1\) for \(a\notin M\) defines a Boolean homomorphism \(\pi:\mathfrak A\to\{0,1\}\).

*Proof.* The union of a chain of proper ideals is a proper ideal, so by Zorn's lemma \(I\) is contained in a maximal proper ideal \(M\). For each \(a\), exactly one of \(a\) and \(1\setminus a\) lies in \(M\). Both cannot, since then \(1=a\cup(1\setminus a)\in M\). If neither does, \(\{c:c\subseteq m\cup a\text{ for some }m\in M\}\) is an ideal strictly larger than \(M\); it is proper, for \(1\subseteq m\cup a\) would give \(1\setminus a\subseteq m\) and \(1\setminus a\in M\). This contradicts maximality. Next, \(a\cap b\notin M\) if \(a,b\notin M\): then \(1\setminus a\) and \(1\setminus b\) lie in \(M\), so \(1\setminus(a\cap b)\in M\). Together with \(a\cap b\subseteq a\) this shows \(\pi(a\cap b)=\pi(a)\pi(b)\), and \(\pi(1\setminus a)=1-\pi(a)\). So \(\pi\) is a Boolean homomorphism. \(\square\)

**Lemma 5.2.** Let \((X,\Sigma,\mu)\) be complete with \(\mu X>0\), and \(\theta:\mathfrak A\to\Sigma\) a lower density. There is a lifting \(\theta'\) with \(\theta'a\supseteq\theta a\) for every \(a\in\mathfrak A\).

*Proof.* For \(x\in\theta1\) let \(I_x=\{a\in\mathfrak A:x\in\theta(1\setminus a)\}\), and for \(x\notin\theta1\) let \(I_x=\{0\}\). Each \(I_x\) is a proper ideal. For \(x\in\theta1\): \(0\in I_x\); if \(b\subseteq a\in I_x\), then \(x\in\theta(1\setminus a)\subseteq\theta(1\setminus b)\); if \(a,b\in I_x\), then \(x\in\theta(1\setminus a)\cap\theta(1\setminus b)=\theta(1\setminus(a\cup b))\); and \(1\notin I_x\) because \(\theta0=\emptyset\). For \(x\notin\theta1\), \(\{0\}\) is proper because \(\mathfrak A\neq\{0\}\). Lemma 5.1 gives Boolean homomorphisms \(\pi_x:\mathfrak A\to\{0,1\}\) vanishing on \(I_x\). Put \(\theta'a=\{x:\pi_x(a)=1\}\). Then \(\theta'\) preserves the Boolean operations, \(\theta'0=\emptyset\) and \(\theta'1=X\). If \(x\in\theta a\), then \(x\in\theta1\) and \(1\setminus a\in I_x\), so \(\pi_x(a)=1\): thus \(\theta a\subseteq\theta'a\). Likewise \(\theta(1\setminus a)\subseteq\theta'(1\setminus a)=X\setminus\theta'a\). Hence
\[
\theta a\subseteq\theta'a\subseteq X\setminus\theta(1\setminus a),
\]
where the outer sets lie in \(\Sigma\) and both have class \(a\). Their difference is null, so by completeness \(\theta'a\in\Sigma\) and \((\theta'a)^\bullet=a\). \(\square\)

## 6. The lifting theorem

Recall that \((X,\Sigma,\mu)\) is *strictly localizable* if \(X\) is the disjoint union of sets \(X_i\in\Sigma\), \(i\in I\), with \(\mu X_i<\infty\), such that a set \(E\subseteq X\) lies in \(\Sigma\) whenever every \(E\cap X_i\) does, and then \(\mu E=\sum_i\mu(E\cap X_i)\). Every finite measure space is strictly localizable, with one piece.

**Theorem 6.1.** Every strictly localizable measure space with \(\mu X>0\) has a lower density \(\theta\) with \(\theta1=X\).

*Proof.* Let \((X_i)_{i\in I}\) be a decomposition. Since \(\mu X=\sum_i\mu X_i>0\), some \(\mu X_j>0\). The union \(Z\) of the pieces of measure zero lies in \(\Sigma\), because its intersection with each piece is empty or the piece, and \(\mu Z=0\); replacing \(X_j\) by \(X_j\cup Z\) and discarding the pieces of measure zero, we may assume \(\mu X_i>0\) for all \(i\). On each \(X_i\) the measure \(\mu_i(E)=\mu E/\mu X_i\), \(E\in\Sigma\), \(E\subseteq X_i\), is a probability measure, with the same null sets as \(\mu\) there; Theorem 4.1 gives a lower density \(\theta_i\) for it with \(\theta_iX_i^\bullet=X_i\). For \(E\in\Sigma\) put
\[
\theta(E^\bullet)=\bigcup_i\theta_i\bigl((E\cap X_i)^\bullet\bigr).
\]
This depends only on \(E^\bullet\), since \(E\sim F\) implies \(E\cap X_i\sim F\cap X_i\) for every \(i\). The set \(\theta(E^\bullet)\) meets \(X_i\) in \(\theta_i\bigl((E\cap X_i)^\bullet\bigr)\in\Sigma\), so it lies in \(\Sigma\), and \(\mu\bigl(\theta(E^\bullet)\triangle E\bigr)=\sum_i\mu\bigl(\theta_i((E\cap X_i)^\bullet)\triangle(E\cap X_i)\bigr)=0\). Intersections, \(\theta0=\emptyset\) and \(\theta1=X\) hold piece by piece. \(\square\)

**Theorem 6.2** (Lifting theorem; von Neumann, Maharam). Every complete strictly localizable measure space \((X,\Sigma,\mu)\) with \(\mu X>0\) has a lifting \(\theta:\mathfrak A\to\Sigma\).

*Proof.* Apply Lemma 5.2 to the lower density of Theorem 6.1. \(\square\)

**Corollary 6.3** (Liftings of \(L^\infty\)). Let \((X,\Sigma,\mu)\) be complete and strictly localizable with \(\mu X>0\). There is a map \(\rho\) from \(L^\infty(X,\Sigma,\mu)\) into the bounded \(\Sigma\)-measurable functions on \(X\) such that \(\rho(f)\) is a representative of \(f\) for every \(f\), \(\rho\) is linear and multiplicative, \(\rho(\bar f)=\overline{\rho(f)}\), \(\rho(1)=1\), and \(\sup_x|\rho(f)(x)|=\|f\|_\infty\).

*Proof.* Let \(\theta\) be a lifting. A *simple* class is \(f=\sum_jc_j1_{a_j}\) with finitely many disjoint \(a_j\in\mathfrak A\) of union \(1\); put \(\rho(f)=\sum_jc_j1_{\theta a_j}\). The sets \(\theta a_j\) are disjoint with union \(X\), so \(\rho(f)\) does not depend on the presentation (pass to a common refinement), and \(\rho\) is linear, multiplicative and compatible with conjugation on simple classes. The set \(\theta a_j\) is empty exactly when \(a_j=0\), so \(\sup_x|\rho(f)(x)|=\max\{|c_j|:a_j\neq0\}=\|f\|_\infty\). Simple classes are dense in \(L^\infty\). An isometric map from a dense subspace into the Banach space of bounded functions with the supremum norm extends uniquely to an isometric linear map on \(L^\infty\), and multiplicativity and conjugation pass to the limit. If \(f_n\to f\) in \(L^\infty\) with \(f_n\) simple, then \(\rho(f_n)\to\rho(f)\) uniformly, so \(\rho(f)\) is \(\Sigma\)-measurable and equals \(\lim f_n=f\) almost everywhere. \(\square\)

## 7. Exercises

**Exercise 7.1.** Let \(\theta\) be a lifting and \(\phi(E)=\theta(E^\bullet)\) for \(E\in\Sigma\). Show that \(\phi(\phi E)=\phi E\), that \(\phi E=\emptyset\) when \(\mu E=0\), and that \(\phi E=\phi F\) when \(E\triangle F\) is null.

*Solution.* \((\phi E)^\bullet=E^\bullet\), so \(\phi(\phi E)=\theta((\phi E)^\bullet)=\theta(E^\bullet)=\phi E\). If \(\mu E=0\), then \(E^\bullet=0\) and \(\phi E=\theta0=\emptyset\). If \(E\triangle F\) is null, \(E^\bullet=F^\bullet\).

**Exercise 7.2.** Let \(X\) be a set, \(\Sigma=\mathcal PX\) and \(\mu\) counting measure. Show that \(\mathfrak A=\Sigma\) and that the identity is the only lifting.

*Solution.* Only \(\emptyset\) is null, so \(E\sim F\) means \(E=F\). A lifting satisfies \((\theta E)^\bullet=E\), that is, \(\theta E=E\).

**Exercise 7.3** (Lebesgue lower density). Let \(\mu\) be Lebesgue measure on the Lebesgue measurable subsets of \(X=[0,1]\). For measurable \(E\) let \(\theta(E^\bullet)\) be the set of \(x\in X\) with \(\lim_{\delta\downarrow0}\mu(E\cap[x-\delta,x+\delta])/2\delta=1\). Using Lebesgue's density theorem — for measurable \(E\subseteq\mathbb R\) the limit is \(1\) at almost every point of \(E\) and \(0\) at almost every point outside \(E\) ([Fremlin, Volume 2, 223B](https://www1.essex.ac.uk/maths/people/fremlin/chap22.pdf)) — show that \(\theta\) is a lower density. Show that \(\tfrac12\) lies neither in \(\theta a\) nor in \(\theta(1\setminus a)\) for \(a=[0,\tfrac12]^\bullet\), so that \(\theta\) is not a lifting.

*Solution.* The value depends only on \(E^\bullet\), since \(\mu(E\cap J)=\mu(F\cap J)\) for every interval \(J\) when \(E\triangle F\) is null. By the density theorem \(\theta(E^\bullet)\triangle E\) is null; so \(\theta(E^\bullet)\) is measurable, Lebesgue measure being complete, and has class \(E^\bullet\). Clearly \(\theta0=\emptyset\), and \(\theta\) is monotone. For the intersection, with \(J=[x-\delta,x+\delta]\),
\[
\frac{\mu(E\cap F\cap J)}{2\delta}\ge\frac{\mu(E\cap J)}{2\delta}+\frac{\mu(F\cap J)}{2\delta}-1,
\]
because \(\mu((E\cup F)\cap J)\le2\delta\). If \(x\in\theta(E^\bullet)\cap\theta(F^\bullet)\), the right side tends to \(1\), so \(x\in\theta((E\cap F)^\bullet)\). At \(x=\tfrac12\) the sets \([0,\tfrac12]\) and \((\tfrac12,1]\) both have \(\mu(\,\cdot\,\cap J)/2\delta=\tfrac12\) for small \(\delta\). A lifting would put \(\tfrac12\) in exactly one of \(\theta a\) and \(\theta(1\setminus a)\), whose union is \(\theta1=X\).

## Where this leads

The lesson [Vector-valued functions, tensor products with \(L^p\), and preduals](vector-valued-functions-tensor-products-with-lp-and-preduals.md) uses Corollary 6.3 for the existence of liftings on every Radon measure space. Liftings that fix the continuous functions (strong liftings) and liftings that commute with translations on locally compact groups are treated in [Fremlin, Volume 4, Sections 453 and 447](https://www1.essex.ac.uk/maths/people/fremlin/mt.htm); translation-invariant liftings on \(\mathbb R^r\) and \(\{0,1\}^I\) are in [Fremlin, Volume 3, Section 345].

## References

- [Fremlin] D. H. Fremlin, *Measure Theory*, Volumes 2 and 3, Torres Fremlin, Colchester, 2001–2002; [author's site](https://www1.essex.ac.uk/maths/people/fremlin/mt.htm), free, under the Design Science License. Volume 3, Section 341, is [Chapter 34](https://www1.essex.ac.uk/maths/people/fremlin/chap34.pdf).
- [Maharam 1958] D. Maharam, On a theorem of von Neumann, *Proceedings of the American Mathematical Society* 9 (1958), 987–994, [doi:10.1090/S0002-9939-1958-0105479-6](https://doi.org/10.1090/S0002-9939-1958-0105479-6). Free at https://www.ams.org/journals/proc/1958-009-06/S0002-9939-1958-0105479-6/
- [von Neumann 1931] J. von Neumann, Algebraische Repräsentanten der Funktionen „bis auf eine Menge vom Maße Null“, *Journal für die reine und angewandte Mathematik* 165 (1931), 109–115; scan at the [Göttingen digitization centre](https://gdz.sub.uni-goettingen.de/download/pdf/PPN243919689_0165/LOG_0015.pdf).
