# Encoding symbols by tiling equations

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson begins the translation of the word rule of [An arithmetic word rule with no vertical period](an-arithmetic-word-rule-with-no-vertical-period.md) into tiling equations with one common unknown set, in a group \(G=\mathbb Z^2\times V\) with \(V\) finite and cyclic [OpenAI-PT, Section 3]. A first equation makes the unknown set the graph of a function of a point \(x\in\mathbb Z^2\) and some auxiliary digits. A symbol is represented by the *dependence* of one output of that function on one of its input digits: the symbol is *active* if changing that digit can change the output. Further equations prescribe what the outputs may depend on, and cycle tests forbid prescribed combinations of active symbols, in particular all forbidden words. The lesson [Forcing activity and excluding periodicity](forcing-activity-and-excluding-periodicity.md) forces enough activity to read off an array from every common solution. Encoding functional constraints by tiling equations goes back to Greenfeld and Tao [Greenfeld–Tao 2023, Sections 4–8; Greenfeld–Tao 2024, Theorem 4.1]; the constructions here carry out the tests with a *cyclic* finite factor.

- Channels, primes and the group (Section 1).
- The graph equation and sheared coordinates (Section 2).
- Dependence tiles and active labels (Section 3).
- Cycle tests (Section 4).

We keep the prime \(p>200\), \(N=p^2\), the alphabet \(\Sigma=\mathbb F_p^\times\), the set \(\mathcal W\subseteq\Sigma^N\) of allowed words, and the line maps \(L_n(x)=x_2+nx_1\) with kernels \(\mathbb Zu_n\), \(u_n=(1,-n)\), from [An arithmetic word rule with no vertical period](an-arithmetic-word-rule-with-no-vertical-period.md). Multiplicities \(r_{A,F}\) and Lemma 1.2 are those of Tilings of abelian groups and periodicity. From the core course [Abstract Algebra I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C30) (Judson, *Abstract Algebra: Theory and Applications*) we use: the existence of infinitely many primes ([Theorem 2.2.6](https://judsonbooks.org/aata-files/aata-html/integers-section-division-algorithm.html)); that coprime integers \(a,b\) have \(ar+bs=1\) for some integers \(r,s\) ([Corollary 2.2.3](https://judsonbooks.org/aata-files/aata-html/integers-section-division-algorithm.html)); that a product of cyclic groups of pairwise coprime orders is cyclic ([Corollary 9.2.10](https://judsonbooks.org/aata-files/aata-html/isomorph-section-direct-products.html)); and the Chinese remainder theorem ([Theorem 16.5.3](https://judsonbooks.org/aata-files/aata-html/rings-section-software-application.html)).

## 1. Channels, primes and the group

The *channels* are the elements of
\[
\mathcal I=\{0,1,\ldots,N-1\}\sqcup\{\eta_1,\eta_2\}.
\]
The first \(N\) channels are *ordinary*, one for each column of an array; the two others are *seeds*. Each channel \(i\) has a set of *labels*: \(J_n=\Sigma\) for an ordinary channel \(n\), and \(J_{\eta_t}=\{*\}\), a single label, for a seed. The seeds will force the ordinary channels to show the constant words \(1\) and \(2\) somewhere. Put
\[
\begin{gathered}S=(\mathbb Z/p^2\mathbb Z)^2,\qquad D=\#S=p^4,\\ s(x)=x\bmod p^2 .\end{gathered}
\]
So \(s(x)\in S\) records the residues of a point \(x\in\mathbb Z^2\) modulo \(p^2\).

**Lemma 1.1** (choice of primes; [OpenAI-PT, Section 3.1]). There are primes \(a_i,b_i\) for \(i\in\mathcal I\) and \(r_{ij}\) for \(i\in\mathcal I\), \(j\in J_i\), all distinct and all different from \(p\), such that
\[
a_{\eta_1}=2,\qquad a_{\eta_2}=3,\qquad b_{\eta_1},b_{\eta_2}>D,
\]
and every \(r_{ij}\) can be written as
\[
r_{ij}=\kappa_{ij}a_i+\lambda_{ij}b_i,\qquad\kappa_{ij},\lambda_{ij}\in\mathbb Z_{\ge0}.
\]

*Proof.* Choose the \(a_i\) and \(b_i\) one after the other, each a prime different from \(p\) and from those already chosen, with \(a_{\eta_1}=2\), \(a_{\eta_2}=3\) (possible since \(p>3\)) and \(b_{\eta_1},b_{\eta_2}>D\); there are infinitely many primes. Let \(a,b\) be distinct primes and \(r\ge(a-1)b\) an integer. Since \(b\) is invertible modulo \(a\) (Corollary 2.2.3 of Judson), there is \(\lambda\in\{0,\ldots,a-1\}\) with \(\lambda b\equiv r\pmod a\), and then \(\kappa=(r-\lambda b)/a\) is an integer with \(\kappa\ge(r-(a-1)b)/a\ge0\). So it suffices to choose each \(r_{ij}\), one after the other, as a prime at least \((a_i-1)b_i\) that differs from \(p\) and from all primes chosen before. \(\square\)

Put
\[
\begin{gathered}
P_i=\mathbb Z/a_i\mathbb Z\times\mathbb Z/b_i\mathbb Z,\qquad r_i=\prod_{j\in J_i}r_{ij},\\
K_i=\mathbb Z/r_i\mathbb Z,\qquad K=\prod_{i\in\mathcal I}K_i,\\
P=\prod_{i\in\mathcal I}P_i .
\end{gathered}
\]
The map \(K_i\to\prod_{j\in J_i}\mathbb Z/r_{ij}\mathbb Z\) that takes residues is an isomorphism: it is a homomorphism, injective because an integer divisible by the distinct primes \(r_{ij}\) is divisible by \(r_i\), and surjective by the Chinese remainder theorem. The residue of \(k\in K_i\) modulo \(r_{ij}\) is the *\(j\)-th digit* of \(k\), and \(U_{ij}\le K_i\) is the subgroup of elements whose other digits are all \(0\). The group of this lesson, of [Forcing activity and excluding periodicity](forcing-activity-and-excluding-periodicity.md) and of [A common solution of the tiling equations](a-common-solution-of-the-tiling-equations.md) is
\[
\begin{gathered}G=\mathbb Z^2\times V,\\ V=\mathbb Z/D\mathbb Z\times\prod_{i\in\mathcal I}\bigl(\mathbb Z/r_i^2\mathbb Z\times P_i\bigr).\end{gathered}
\]

**Lemma 1.2** (\(V\) is cyclic). The group \(V\) is cyclic of order \(D\prod_i r_i^2a_ib_i\).

*Proof.* Writing each \(P_i\) as a product of its two cyclic factors, \(V\) is a product of cyclic groups of orders \(D=p^4\), \(r_i^2\), \(a_i\) and \(b_i\), \(i\in\mathcal I\). These orders are pairwise coprime, since they are powers of products of pairwise distinct primes. By Corollary 9.2.10 of Judson, the product is cyclic. \(\square\)

The set \(S\) is not a factor of \(V\). Its \(D\) elements will only index the values of the coordinate \(\mathbb Z/D\mathbb Z\).

## 2. The graph equation and sheared coordinates

We write an element of \(G\) as
\[
\bigl(x,z,(v_i,c_i)_{i\in\mathcal I}\bigr)
\]
with \(z\in\mathbb Z/D\mathbb Z\), \(v_i\in\mathbb Z/r_i^2\mathbb Z\) and \(c_i\in P_i\). Its *horizontal coordinate* is \(x\in\mathbb Z^2\), its *low coordinates* are \(k_i=v_i\bmod r_i\in K_i\), and \(c_i\) is its *useful output* in channel \(i\). Let
\[
q_0\colon G\to\mathbb Z^2\times K,\qquad q_0(g)=(x,k),
\]
keep the horizontal and the low coordinates. It is a surjective homomorphism, and its kernel is
\[
\begin{aligned}H_0={}&\{0\}\times\mathbb Z/D\mathbb Z\\&\times\prod_{i\in\mathcal I}\bigl(r_i\mathbb Z/r_i^2\mathbb Z\times P_i\bigr).\end{aligned}
\]
We call \(q_0(g)\) the *base* of \(g\); the cosets of \(H_0\) are the *fibres* \(q_0^{-1}(x,k)\).

**Lemma 2.1** (the graph equation; [OpenAI-PT, Section 3.2]). For \(A\subseteq G\), \(A\oplus H_0=G\) holds exactly when \(A\) contains exactly one element above every base \((x,k)\in\mathbb Z^2\times K\).

*Proof.* This is Lemma 1.2(2) of Tilings of abelian groups and periodicity for the subgroup \(H_0\), whose cosets are the fibres of \(q_0\). \(\square\)

A set with \(A\oplus H_0=G\) is called a *graph*. For a graph we write \(z(x,k)\), \(v_i(x,k)\) and \(c_i(x,k)\) for the coordinates of its unique point above \((x,k)\), and call \(c_i(x,k)\) the useful output of channel \(i\) at \((x,k)\). The high part of \(v_i\) is recorded in sheared form. For an integer \(y\) let \([y]_{r}\in\{0,\ldots,r-1\}\) be its least nonnegative residue modulo \(r\); for \(y\in\mathbb Z/r\mathbb Z\) the same notation is used for the least nonnegative representative. Define \(\beta_i(x,k)\in K_i\) by
\[
v_i(x,k)=x_1+[k_i-x_1]_{r_i}+r_i\,\beta_i(x,k)
\]
in \(\mathbb Z/r_i^2\mathbb Z\). Here \(r_i\beta\) is well defined in \(\mathbb Z/r_i^2\mathbb Z\) for \(\beta\in\mathbb Z/r_i\mathbb Z\).

**Lemma 2.2** (sheared coordinates; [OpenAI-PT, Section 3.2]).

1. For fixed \(x\in\mathbb Z^2\) and \(k_i\in K_i\), the map \(\beta\mapsto x_1+[k_i-x_1]_{r_i}+r_i\beta\) is a bijection from \(K_i\) onto the set of elements of \(\mathbb Z/r_i^2\mathbb Z\) with residue \(k_i\) modulo \(r_i\). So a graph is the same as a choice of three functions \(c_i\), \(\beta_i\) and \(z\) on \(\mathbb Z^2\times K\), arbitrary and independent of each other.
2. Let \(h\in\mathbb Z^2\). If a point with horizontal coordinate \(x\), low coordinate \(k_i\) and sheared coordinate \(\beta\) is translated by an element of \(G\) whose horizontal coordinate is \(h\) and whose coordinate in \(\mathbb Z/r_i^2\mathbb Z\) is \(h_1\bmod r_i^2\), the image has horizontal coordinate \(x+h\), low coordinate \(k_i+h_1\) and the same sheared coordinate \(\beta\).

*Proof.* (1) The residue of \(x_1+[k_i-x_1]_{r_i}+r_i\beta\) modulo \(r_i\) is \(x_1+(k_i-x_1)=k_i\). The elements of \(\mathbb Z/r_i^2\mathbb Z\) with residue \(k_i\) are the \(r_i\) elements \(y_0+r_i\beta\), \(\beta\in K_i\), for any one of them \(y_0\), and these are distinct. (2) The new coordinate is \(x_1+h_1+[k_i-x_1]_{r_i}+r_i\beta\), and \([(k_i+h_1)-(x_1+h_1)]_{r_i}=[k_i-x_1]_{r_i}\). This holds for every integer \(h_1\), negative ones included. \(\square\)

The sheared coordinate is a choice of coordinates on each fibre. It does not split \(\mathbb Z/r_i^2\mathbb Z\) into a product of two groups of order \(r_i\).

## 3. Dependence tiles and active labels

For \(g\in G\) we write \(c_i(g)\) for the \(P_i\)-coordinate of \(g\).

**Lemma 3.1** (invariance tiles; [OpenAI-PT, Lemma 3.1]). Let \(i\in\mathcal I\) and \(\sigma\in\mathbb Z^2\times K\). There is a finite nonempty set \(F_{i,\sigma}\subset G\) with \(\#F_{i,\sigma}=\#H_0\) such that for every graph \(A\), \(A\oplus F_{i,\sigma}=G\) holds exactly when \(c_i(b-\sigma)=c_i(b)\) for all \(b\in\mathbb Z^2\times K\).

*Proof.* Choose \(g\in G\) with \(q_0(g)=\sigma\) and \(c_i(g)=0\), and put
\[
\begin{gathered}
E_0=\{h\in H_0:c_i(h)=0\},\\
E_{\ne}=H_0\setminus E_0,\\
F_{i,\sigma}=E_{\ne}\cup(g+E_0).
\end{gathered}
\]
The two parts are disjoint, since their \(P_i\)-coordinates are nonzero and zero, so \(\#F_{i,\sigma}=\#H_0\). Let \(A\) be a graph, let \(a_b\) denote its point above \(b\), and let \(y\in G\) have base \(b\). A representation \(y=a+f\) with \(f\in E_{\ne}\) forces \(q_0(a)=b\), so \(a=a_b\) and \(f=y-a_b\); this \(f\) lies in \(H_0\) and lies in \(E_{\ne}\) exactly when \(c_i(y)\ne c_i(b)\). A representation with \(f\in g+E_0\) forces \(q_0(a)=b-\sigma\), so \(a=a_{b-\sigma}\) and \(f=y-a_{b-\sigma}\), and \(f-g\in H_0\) lies in \(E_0\) exactly when \(c_i(y)=c_i(b-\sigma)\). Hence
\[
\begin{aligned}r_{A,F_{i,\sigma}}(y)={}&[c_i(y)\ne c_i(b)]\\&+[c_i(y)=c_i(b-\sigma)],\end{aligned}
\]
where \([\cdot]\) is \(1\) for a true statement and \(0\) otherwise. If \(c_i(b-\sigma)=c_i(b)\), this is \(1\) for every \(y\) above \(b\). If \(c_i(b-\sigma)\ne c_i(b)\), the point \(y\) above \(b\) with \(c_i(y)=c_i(b-\sigma)\) has multiplicity \(2\). \(\square\)

The tile does not depend on the graph, and its equation constrains only the useful output \(c_i\); the functions \(\beta_\ell\), \(z\) and the other \(c_\ell\) are not restricted by it. The *dependence conditions* are
\[
\begin{aligned}
c_n(x,k)&=\tilde c_n(L_n(x),k_n),\\
c_{\eta_t}(x,k)&=\tilde c_{\eta_t}(s(x),k_{\eta_t})
\end{aligned}\tag{3.1}
\]
for the ordinary channels \(0\le n<N\), for \(t=1,2\), and for some functions \(\tilde c_n\colon\mathbb Z\times K_n\to P_n\) and \(\tilde c_{\eta_t}\colon S\times K_{\eta_t}\to P_{\eta_t}\).

**Corollary 3.2** (dependence tiles; [OpenAI-PT, Section 3.3]). There is a finite family of finite nonempty subsets of \(G\) such that a graph tiles \(G\) with every member of the family exactly when it satisfies (3.1).

*Proof.* Let \(\epsilon_\ell\in K\) have the coordinate \(1\in K_\ell\) in channel \(\ell\) and \(0\) elsewhere. The family consists of: \(F_{i,(0,\epsilon_\ell)}\) for all channels \(i\ne\ell\); \(F_{n,(u_n,0)}\) for every ordinary channel \(n\); and \(F_{\eta_t,((p^2,0),0)}\), \(F_{\eta_t,((0,p^2),0)}\) for \(t=1,2\). By Lemma 3.1, the graph tiles with \(F_{i,\sigma}\) exactly when \(c_i\) is invariant under translation of the base by \(\sigma\), and then also by every element of the subgroup generated by \(\sigma\) (Exercise 5.2). So the family is tiled exactly when: each \(c_i\) is invariant under \(\{0\}\times\prod_{\ell\ne i}K_\ell\), that is, depends on \(k\) only through \(k_i\); each \(c_n\) is invariant under \(\mathbb Zu_n=\ker L_n\) in \(x\), that is, depends on \(x\) only through \(L_n(x)\), since \(L_n\) is surjective; and each \(c_{\eta_t}\) is invariant under \(p^2\mathbb Z^2\), that is, depends on \(x\) only through \(s(x)\). These are the conditions (3.1). \(\square\)

**Definition 3.3** (active labels). Let \(A\) be a graph satisfying (3.1). For \(x\in\mathbb Z^2\) and a channel \(i\), let \(g_{i,x}\colon K_i\to P_i\) be the function \(k_i\mapsto c_i(x,k)\), which depends only on \(k_i\). A label \(j\in J_i\) is *active* for channel \(i\) at \(x\) if there are \(w,w'\in K_i\) with
\[
w-w'\in U_{ij},\qquad g_{i,x}(w)\ne g_{i,x}(w').
\]
The active labels form the set \(\mathcal A_i(x)\subseteq J_i\).

So the label \(j\) is inactive exactly when changing the \(j\)-th digit of the input never changes the output. By (3.1), \(\mathcal A_n(x)\) depends only on \(L_n(x)\), and \(\mathcal A_{\eta_t}(x)\subseteq\{*\}\) depends only on \(s(x)\). Active sets may be empty at this stage.

**Lemma 3.4.** A function \(\varphi\) on \(K_i\) with no active label is constant.

*Proof.* Let \(w,w'\in K_i\). By the isomorphism \(K_i\cong\prod_j\mathbb Z/r_{ij}\mathbb Z\), \(w-w'=\sum_j\delta_j\) with \(\delta_j\in U_{ij}\). Changing one digit at a time, \(w'\), \(w'+\delta_{j_1}\), \(w'+\delta_{j_1}+\delta_{j_2}\), and so on up to \(w\), consecutive inputs differ by an element of one \(U_{ij}\), so \(\varphi\) takes the same value on all of them. \(\square\)

## 4. Cycle tests

**Lemma 4.1** (exclusion of simultaneous activity; [OpenAI-PT, Lemma 3.2]). Let \(C=(i_1,\ldots,i_t)\), \(t\ge1\), be a cyclically ordered list of distinct channels, and choose a label \(j(i)\in J_i\) for each \(i\) on \(C\). There is a finite family of finite nonempty subsets of \(G\) such that a graph satisfying (3.1) tiles \(G\) with every member of the family exactly when, at every \(x\in\mathbb Z^2\), at least one of the labels \(j(i)\), \(i\) on \(C\), is inactive.

*Proof.* For \(i\) on \(C\) let \(\operatorname{prev}(i)\) be the channel before \(i\) in the cyclic order; for \(t=1\), \(\operatorname{prev}(i_1)=i_1\). For every family \(d=(d_i)_{i\in C}\) of maps
\[
d_i\colon P_{\operatorname{prev}(i)}\to U_{i,j(i)}
\]
and every \(e=(e_i)_{i\in\mathcal I}\in P\), put \(d_i[e]=d_i(e_{\operatorname{prev}(i)})\) for \(i\) on \(C\) and \(d_i[e]=0\) otherwise, and let \(F_d\) be the set of all \(\bigl(0,\zeta,(\upsilon_i,e_i)_{i\in\mathcal I}\bigr)\in G\) with \(e\in P\), \(\zeta\in\mathbb Z/D\mathbb Z\) and \(\upsilon_i\bmod r_i=d_i[e]\) for every \(i\in\mathcal I\). The family consists of the tiles \(F_d\) for all such \(d\); there are finitely many. Each \(F_d\) has \(\#P\cdot D\cdot\prod_ir_i=\#H_0\) elements, one for every \(e\in P\), every \(\zeta\) and every lift \(\upsilon_i\) of \(d_i[e]\).

*The criterion.* Fix \(d\), a graph \(A\) satisfying (3.1) and a point \(y\) with base \((x,k)\) and useful outputs \(c=(c_i)_i\). In a representation \(y=a+f\) with \(f\in F_d\) and \(P\)-coordinate \(e\), the base of \(a\) must be \((x,(k_i-d_i[e])_i)\), so \(a\) is determined by \(e\), and the useful outputs of \(y\) must be the components of an element \(\Phi_{x,k,d}(e)\in P\): writing \(\Phi\) for \(\Phi_{x,k,d}\), for \(i\in\mathcal I\)
\[
\begin{aligned}\Phi(e)_i={}&e_i\\&+g_{i,x}(k_i-d_i[e]).\end{aligned}\tag{4.1}
\]
Conversely, if \(\Phi_{x,k,d}(e)=c\), then \(f=y-a\) has \(P\)-coordinate \(e\), its \(v_i\)-coordinate has residue \(k_i-(k_i-d_i[e])=d_i[e]\), and every \(\zeta\) and every such lift occurs in \(F_d\); so \(f\in F_d\). Hence \(r_{A,F_d}(y)\) is the number of \(e\in P\) with \(\Phi_{x,k,d}(e)=c\), and \(A\oplus F_d=G\) exactly when \(\Phi_{x,k,d}\) is a bijection of \(P\) for every base \((x,k)\).

*If some chosen label is inactive at \(x\), every \(\Phi_{x,k,d}\) is a bijection.* Let \(j(i_0)\) be inactive at \(x\). Since \(d_{i_0}[e]\in U_{i_0,j(i_0)}\), the \(i_0\)-component of (4.1) is \(e_{i_0}+g_{i_0,x}(k_{i_0})\), independent of \(e_{\operatorname{prev}(i_0)}\). Given a target \(c\), this component determines \(e_{i_0}=c_{i_0}-g_{i_0,x}(k_{i_0})\). For the channel \(i\) after \(i_0\), \(d_i[e]=d_i(e_{i_0})\) is now known, and its component determines \(e_i\). Going once around the cycle determines all components on \(C\); off \(C\), \(e_i=c_i-g_{i,x}(k_i)\). The \(e\) found in this way satisfies every equation, the first one included, because the first one did not involve the last component found. So every target has exactly one preimage.

*If all chosen labels are active at \(x\), some \(\Phi_{x,k,d}\) is not injective.* For \(i\) on \(C\) choose \(w_i,w_i'\in K_i\) with
\[
\begin{gathered}w_i-w_i'\in U_{i,j(i)},\\ \varepsilon_i=g_{i,x}(w_i)-g_{i,x}(w_i')\ne0 .\end{gathered}
\]
Let \(k_i=w_i\) for \(i\) on \(C\) and \(k_i\) arbitrary otherwise, and extend \(\varepsilon\) by \(0\) off \(C\) to an element of \(P\). For \(i\) on \(C\) choose \(d_i\) with
\[
d_i(0)=0,\qquad d_i\bigl(\varepsilon_{\operatorname{prev}(i)}\bigr)=w_i-w_i' ;
\]
this is possible because \(\varepsilon_{\operatorname{prev}(i)}\ne0\). Then for \(i\) on \(C\) the \(i\)-components of \(\Phi_{x,k,d}(0)\) and \(\Phi_{x,k,d}(\varepsilon)\) are
\[
g_{i,x}(w_i)\quad\text{and}\quad\varepsilon_i+g_{i,x}(w_i'),
\]
which are equal; off \(C\) both components are \(g_{i,x}(k_i)\). So the distinct elements \(0\) and \(\varepsilon\) have the same image. \(\square\)

We impose the following instances of Lemma 4.1.

1. For every word \(w\in\Sigma^N\setminus\mathcal W\), the cycle \((0,1,\ldots,N-1)\) with the labels \(j(n)=w(n)\).
2. For \(t\in\{1,2\}\), every ordinary channel \(n\) and every \(j\in\Sigma\setminus\{t\}\), the cycle \((\eta_t,n)\) with the labels \(*\) and \(j\).

There are finitely many instances, each with finitely many tiles. By Lemma 4.1, a graph satisfying (3.1) tiles with all of them exactly when, for every \(x\in\mathbb Z^2\),
\[
\prod_{n=0}^{N-1}\mathcal A_n(x)\subseteq\mathcal W\tag{4.2}
\]
and, for \(t=1,2\) and every ordinary \(n\),
\[
\begin{aligned}&*\in\mathcal A_{\eta_t}(x)\\&\Longrightarrow\ \mathcal A_n(x)\subseteq\{t\}.\end{aligned}\tag{4.3}
\]
In (4.2) the product is read as a set of words \(n\mapsto j_n\) with \(j_n\in\mathcal A_n(x)\). It says that every way of choosing one active label in each ordinary channel gives an allowed word. Both statements hold trivially where some active sets are empty. The lesson [Forcing activity and excluding periodicity](forcing-activity-and-excluding-periodicity.md) adds tiles that make every ordinary active set nonempty at every point and each seed active somewhere.

Every tile of this lesson has \(\#H_0=D\prod_{i\in\mathcal I}r_i\,\#P_i\) elements: \(H_0\) itself, the invariance tiles of Lemma 3.1, and the cycle tiles of Lemma 4.1.

## 5. Exercises

**5.1.** Let \(a,b\ge2\) be coprime. Show that \(ab-a-b\) is not of the form \(\kappa a+\lambda b\) with integers \(\kappa,\lambda\ge0\), but every integer \(r>ab-a-b\) is.

**5.2.** Let \(A\) be a graph and \(\sigma_1,\ldots,\sigma_k\in\mathbb Z^2\times K\). Show that if \(c_i(b-\sigma_j)=c_i(b)\) for all \(b\) and all \(j\), then \(c_i(b-\sigma)=c_i(b)\) for every \(\sigma\) in the subgroup generated by \(\sigma_1,\ldots,\sigma_k\).

**5.3.** Apply Lemma 4.1 to a cycle of length one, \(C=(i)\) with a label \(j\). Show directly from (4.1) that a graph satisfying (3.1) tiles with all the tiles \(F_d\) exactly when \(j\) is inactive at every \(x\).

**5.4.** Let \(r=6\), so that \(K_i=\mathbb Z/6\mathbb Z\cong\mathbb Z/2\mathbb Z\times\mathbb Z/3\mathbb Z\) with two digits, and let \(P_i=\mathbb Z/5\mathbb Z\). Give functions \(\varphi\colon K_i\to P_i\) with exactly the active labels \(\varnothing\), \(\{2\}\), \(\{3\}\) and \(\{2,3\}\), where the labels are named by the primes \(2\) and \(3\).

**5.5.** In the proof of Lemma 4.1, the cycle tile uses maps \(d_i\) from \(P_{\operatorname{prev}(i)}\) into \(U_{i,j(i)}\). Show that if instead every \(d_i\) were constant, the tile \(F_d\) would be tiled by every graph satisfying (3.1), so the test would forbid nothing.

## 6. Solutions

**5.1.** If \(ab-a-b=\kappa a+\lambda b\) with \(\kappa,\lambda\ge0\), then \(ab=(\kappa+1)a+(\lambda+1)b\). Reducing modulo \(a\) gives \(a\mid(\lambda+1)b\), so \(a\mid\lambda+1\) and \(\lambda+1\ge a\); similarly \(\kappa+1\ge b\). Then \((\kappa+1)a+(\lambda+1)b\ge2ab>ab\), a contradiction. If \(r>ab-a-b\), choose \(\lambda\in\{0,\ldots,a-1\}\) with \(\lambda b\equiv r\pmod a\). Then \(r-\lambda b\) is divisible by \(a\) and \(r-\lambda b\ge r-(a-1)b>-a\), so \(r-\lambda b\ge0\) and \(\kappa=(r-\lambda b)/a\) works.

**5.2.** Substituting \(b+\sigma_j\) for \(b\) gives \(c_i(b)=c_i(b+\sigma_j)\), so \(c_i\) is invariant under \(\pm\sigma_j\). If it is invariant under \(\sigma\) and \(\sigma'\), then \(c_i(b-\sigma-\sigma')=c_i(b-\sigma)=c_i(b)\). So the set of \(\sigma\) with \(c_i(b-\sigma)=c_i(b)\) for all \(b\) is a subgroup, and it contains the \(\sigma_j\).

**5.3.** For \(C=(i)\), \(d_i\colon P_i\to U_{ij}\), and the \(i\)-component of (4.1) is \(e_i\mapsto e_i+g_{i,x}(k_i-d_i(e_i))\), while the other components are translations. If \(j\) is inactive at \(x\), this component is \(e_i+g_{i,x}(k_i)\), a translation, and \(\Phi\) is a bijection. If \(j\) is active, choose \(w,w'\) with \(w-w'\in U_{ij}\) and \(\varepsilon=g_{i,x}(w)-g_{i,x}(w')\ne0\), take \(k_i=w\), \(d_i(0)=0\) and \(d_i(\varepsilon)=w-w'\); then \(e_i=0\) and \(e_i=\varepsilon\) give \(g_{i,x}(w)\) and \(\varepsilon+g_{i,x}(w')\), which are equal.

**5.4.** Write \(k\in\mathbb Z/6\mathbb Z\) through its digits \((k\bmod2,k\bmod3)\). The constant \(0\) has no active label; \(\varphi(k)=k\bmod2\) (as an element of \(\mathbb Z/5\mathbb Z\)) has exactly the label \(2\) active; \(\varphi(k)=k\bmod3\) has exactly the label \(3\) active; \(\varphi(k)=(k\bmod2)+(k\bmod3)\) has both.

**5.5.** If \(d_i\) is constant with value \(\delta_i\), then \(d_i[e]=\delta_i\) does not depend on \(e\), and (4.1) is \(e\mapsto\bigl(e_i+g_{i,x}(k_i-\delta_i)\bigr)_i\), a translation of \(P\). It is a bijection for every base, whatever the activity.

## References

- [OpenAI-PT] OpenAI, *A translational tile with no fully periodic tiling in dimension three*, OpenAI Math Release preprint, 23 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/A-translational-tile-with-no-fully-periodic-tiling-in-dimension-three-September-23-2026
- [Greenfeld–Tao 2023] R. Greenfeld, T. Tao, *Undecidable translational tilings with only two tiles, or one nonabelian tile*, Discrete Comput. Geom. 70 (2023), 1652–1706. https://arxiv.org/abs/2108.07902
- [Greenfeld–Tao 2024] R. Greenfeld, T. Tao, *A counterexample to the periodic tiling conjecture*, Ann. of Math. 200 (2024), 301–363. https://arxiv.org/abs/2211.15847
