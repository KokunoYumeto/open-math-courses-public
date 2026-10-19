# The cohomology problem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A von Neumann algebra \(M\) acts on itself by left and right multiplication, and the bounded multilinear maps \(M^k\to M\) form a complex, the bounded Hochschild complex. In degree one its cocycles are the derivations, and the theorem of Kadison and Sakai that every derivation of a von Neumann algebra is inner says that the first cohomology vanishes. Kadison and Ringrose asked whether all higher cohomology groups vanish as well. This course gives the proof, found by OpenAI in 2026, that they do: every bounded Hochschild cocycle of degree at least two is the coboundary of a bounded cochain.

This lesson sets up the complex and states the theorem (Section 1). Section 2 proves the facts about tracial von Neumann algebras used throughout, in particular that normal maps are continuous on bounded sets for the tracial \(2\)-norm. Section 3 records the two classical reductions on which the proof rests and the route of the course.

**Prerequisites.** From *Foundations of von Neumann algebras*: [*The double commutant theorem*](course:foundations-of-von-neumann-algebras/the-double-commutant-theorem) (Proposition 7.2, polar decomposition inside a von Neumann algebra; Theorem 10.1, positive normal functionals as sums of vector functionals); [*Compact and trace-class operators, the predual of B(H) and the operator topologies*](course:foundations-of-von-neumann-algebras/compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies) (Lemma 8.5 and Proposition 8.6 on bounded sets; Theorems 9.4 and 9.5 on preduals and continuity on the unit ball); [*Kaplansky's density theorem and its consequences*](course:foundations-of-von-neumann-algebras/kaplansky-s-density-theorem-and-its-consequences) (Corollary 1.4, monotone nets of projections); [*The spectral theorem for bounded self-adjoint operators*](course:foundations-of-von-neumann-algebras/the-spectral-theorem-for-bounded-self-adjoint-operators) (spectral projections); [*Projections and types of von Neumann algebras*](course:foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras) (left and right supports, finite algebras, central summands). From *Type III factors: central sequences, full factors and almost periodic states*: [*Ultraproducts and the asymptotic centralizer*](course:type-iii-factors/ultraproducts-and-the-asymptotic-centralizer), Theorem 3.2 (a tracial ultraproduct of finite von Neumann algebras is a finite von Neumann algebra with faithful normal tracial state).

**Conventions.** All von Neumann algebras and maps are complex. A map \(f:M^k\to M\) is *separately normal* if it is ultraweakly continuous in each variable when the others are fixed. A finite von Neumann algebra is said to be of *type \(\mathrm{II}_1\)* when it has no nonzero type I central summand; its centre need not be trivial. A *faithful normal tracial state* \(\rho\) on a von Neumann algebra is an ultraweakly continuous state with \(\rho(xy)=\rho(yx)\) for all \(x,y\) and \(\rho(x^*x)=0\) only for \(x=0\).

## 1. Bounded Hochschild cohomology

For \(k\ge1\) let \(C_b^k(M,M)\) be the Banach space of bounded \(k\)-linear maps \(f:M^k\to M\), with
\[
\begin{aligned}
\|f\|=\sup\{&\|f(a_1,\ldots,a_k)\|:\\
&\|a_1\|,\ldots,\|a_k\|\le1\},
\end{aligned}
\]
and put \(C_b^0(M,M)=M\). Boundedness refers to this norm, defined with the operator norm on each variable; no complete boundedness is assumed. The differential \(d:C_b^k(M,M)\to C_b^{k+1}(M,M)\) is
\[
\begin{aligned}
&(df)(a_1,\ldots,a_{k+1})\\
&=a_1f(a_2,\ldots,a_{k+1})\\
&\quad+\sum_{j=1}^k(-1)^jf(a_1,\ldots,a_ja_{j+1},\\
&\qquad\qquad\ldots,a_{k+1})\\
&\quad+(-1)^{k+1}f(a_1,\ldots,a_k)a_{k+1},
\end{aligned}
\]
and \((db)(a)=ab-ba\) for \(b\in M\). It is bounded, with \(\|df\|\le(k+2)\|f\|\).

**Lemma 1.1.** \(d\circ d=0\).

**Proof.** On \(C_b^k\) write \(d=\sum_{j=0}^{k+1}(-1)^j\delta_j\), where \((\delta_0f)(a_1,\ldots,a_{k+1})=a_1f(a_2,\ldots,a_{k+1})\), \(\delta_jf\) evaluates \(f\) after multiplying \(a_j\) and \(a_{j+1}\) for \(1\le j\le k\), and \((\delta_{k+1}f)(a_1,\ldots,a_{k+1})\) is \(f(a_1,\ldots,a_k)a_{k+1}\). For \(0\le i<j\le k+2\) the identity
\[
\delta_j\delta_i=\delta_i\delta_{j-1}\qquad(C_b^k\to C_b^{k+2})
\]
holds. If \(j>i+1\), both sides perform the same two operations on disjoint positions. If \(j=i+1\), both sides combine three consecutive inputs, and they agree by associativity of the product, or by \((ax)b=a(xb)\) when one of the operations is an outer multiplication. Then
\[
d^2=\sum_{i<j}(-1)^{i+j}\delta_j\delta_i+\sum_{j\le i}(-1)^{i+j}\delta_j\delta_i .
\]
In the first sum, \(\delta_j\delta_i=\delta_i\delta_{j-1}\) and \((-1)^{i+j}=-(-1)^{i+(j-1)}\); as \((i,j)\) runs over the pairs with \(i<j\), the pair \((i,j-1)\) runs over the pairs \((i,i')\) with \(i\le i'\le k+1\). The first sum is therefore the negative of the second. \(\square\)

Put
\[
H_b^k(M,M)=\frac{\ker\bigl(d:C_b^k\to C_b^{k+1}\bigr)}{\operatorname{im}\bigl(d:C_b^{k-1}\to C_b^k\bigr)},
\]
with the actual image in the denominator, not its closure. A *cocycle* is an element of the kernel; a *primitive* of a cocycle \(f\) is a cochain \(g\) with \(dg=f\). In degree one the cocycles are the derivations, \(f(ab)=af(b)+f(a)b\), and the coboundaries are the inner derivations \(a\mapsto ab-ba\). Every derivation of a von Neumann algebra is inner (Kadison, Sakai, 1966), so \(H^1_b(M,M)=0\). That theorem is context for the course and is not used in it.

**Theorem 1.2 (OpenAI, 2026).** Let \(M\) be a von Neumann algebra and \(k\ge2\). Every cocycle \(f\in C_b^k(M,M)\) has a primitive \(g\in C_b^{k-1}(M,M)\). Hence \(H_b^k(M,M)=0\).

## 2. Tracial algebras, the 2-norm and ultrapowers

Let \((N,\rho)\) be a finite von Neumann algebra with a faithful normal tracial state, and put \(\|x\|_2=\rho(x^*x)^{1/2}\). The trace property gives \(\|x^*\|_2=\|x\|_2\). Since \(y^*x^*xy\le\|x\|^2y^*y\), also \(\|xy\|_2\le\|x\|\,\|y\|_2\), and then \(\|yz\|_2=\|z^*y^*\|_2\le\|z\|\,\|y\|_2\). Together,
\[
\|xyz\|_2\le\|x\|\,\|y\|_2\,\|z\| .
\]
On operator-norm bounded subsets of \(N\) the topology of the \(2\)-norm coincides with the strong and with the strong-star operator topology (Exercise 4.4).

**Definition 2.1.** A linear map \(R:N\to N\) is *continuous on balls for the \(2\)-norm* if \(\|R(x_j)\|_2\to0\) whenever \(\sup_j\|x_j\|<\infty\) and \(\|x_j\|_2\to0\).

**Lemma 2.2.** Let \(R:N\to N\) be bounded and linear.

1. \(R\) is continuous on balls for the \(2\)-norm if and only if for every \(r<\infty\) and \(\varepsilon>0\) there is \(\delta>0\) with \(\|R(x)\|_2<\varepsilon\) whenever \(\|x\|\le r\) and \(\|x\|_2<\delta\).
2. If so, and \(\omega\) is a free ultrafilter on \(\mathbb N\), then \(R^\omega((x_j)_\omega)=(R(x_j))_\omega\) is a well-defined bounded linear map on the tracial ultrapower \(N^\omega\), with \(\|R^\omega\|\le\|R\|\), and it is again continuous on balls for the \(2\)-norm of the ultrapower trace. In particular, \((R^\omega)^\nu\) on \((N^\omega)^\nu\) has the same properties for every free ultrafilter \(\nu\).

Here \(N^\omega=\ell^\infty(\mathbb N,N)/\mathcal I_\omega\), where \(\mathcal I_\omega\) consists of the bounded sequences with \(\lim_{j\to\omega}\|x_j\|_2=0\), with the quotient norm and the trace \(\rho^\omega((x_j)_\omega)=\lim_{j\to\omega}\rho(x_j)\). It is a von Neumann algebra with faithful normal tracial state \(\rho^\omega\) (Theorem 3.2 of the ultraproduct lesson cited above), its \(2\)-norm is \(\|(x_j)_\omega\|_2=\lim_{j\to\omega}\|x_j\|_2\), and \(N\) is identified with the constant sequences.

**Proof.** (1) If the uniform statement fails for some \(r,\varepsilon\), there are \(x_j\) with \(\|x_j\|\le r\), \(\|x_j\|_2<1/j\) and \(\|R(x_j)\|_2\ge\varepsilon\), contradicting continuity. The converse is immediate.

(2) By (1), \(R\) maps bounded sequences in \(\mathcal I_\omega\) into \(\mathcal I_\omega\): if \(\lim_{j\to\omega}\|x_j\|_2=0\), then \(\{j:\|x_j\|_2<\delta\}\in\omega\), so \(\{j:\|R(x_j)\|_2<\varepsilon\}\in\omega\). Applied to the difference of two representatives, this shows that \(R^\omega\) is well defined. For every representative, \(\|R^\omega(X)\|\le\sup_j\|R(x_j)\|\)\(\le\|R\|\sup_j\|x_j\|\), and the infimum over representatives gives \(\|R^\omega(X)\|\le\|R\|\,\|X\|\).

For the modulus, let \(r<\infty\) and \(\varepsilon>0\), and take \(\delta\) from (1) for the radius \(r+1\) and the tolerance \(\varepsilon/2\). If \(\|X\|\le r\), the quotient norm allows a representative with \(\sup_j\|x_j\|\le r+1\). If moreover \(\|X\|_2<\delta\), then \(\{j:\|x_j\|_2<\delta\}\in\omega\), and \(\|R^\omega(X)\|_2=\lim_{j\to\omega}\|R(x_j)\|_2\)\(\le\varepsilon/2<\varepsilon\). So \(\delta\) works for \(R^\omega\) at the radius \(r\). The argument did not use separability of \(N\), so it applies again to \(N^\omega\) in place of \(N\). \(\square\)

**Lemma 2.3 (normal maps are continuous on balls).** Let \(B:N\to N\) be bounded, linear and normal. Then \(B\) is continuous on balls for the \(2\)-norm.

**Proof.** Two facts about projections are used. First, \(\rho(p\vee q)\le\rho(p)+\rho(q)\) for projections \(p,q\in N\). Indeed, the closure of the range of \((1-p)q\) is the closure of \((1-p)(p\vee q)H\), which is the range of the projection \(p\vee q-p\). So the left support of \((1-p)q\) is \(p\vee q-p\), while its right support is at most \(q\). Left and right supports are \(uu^*\) and \(u^*u\) for the partial isometry \(u\in N\) of the polar decomposition, so they have equal trace, and \(\rho(p\vee q)-\rho(p)\le\rho(q)\). Second, for projections \(e_h\) the increasing finite joins converge strongly to \(\bigvee_he_h\) (Corollary 1.4 of the Kaplansky lesson). Strong convergence of a bounded net implies ultraweak convergence (Lemma 8.5 of the lesson on operator topologies), and \(\rho\) is normal. So \(\rho(\bigvee_he_h)\le\sum_h\rho(e_h)\).

Suppose that \(B\) is not continuous on balls. By Lemma 2.2(1) there are \(R,\eta>0\) and \(x_j\in N\) with \(\|x_j\|\le R\), \(\|x_j\|_2\to0\) and \(\|B(x_j)\|_2\ge\eta\). Choose \(\alpha>0\) with \(\|B\|\alpha<\eta/4\). With the polar decomposition \(x_j=v_j|x_j|\) in \(N\), put
\[
\begin{gathered}
r_j=1_{(\alpha,\infty)}(|x_j|),\quad y_j=v_j|x_j|r_j,\\
\ell_j=v_jr_jv_j^*,\quad e_j=r_j\vee\ell_j .
\end{gathered}
\]
The spectral projection \(r_j\) lies below the support \(v_j^*v_j\) of \(|x_j|\), so \(\ell_j\) is a projection. Since \(|y_j|=|x_j|r_j\) is invertible on \(r_jH\), the right and left supports of \(y_j\) are \(r_j\) and \(\ell_j\), and \(y_j=e_jy_je_j\). Also \(\|y_j\|\le R\) and \(\|x_j-y_j\|=\|v_j|x_j|(1-r_j)\|\le\alpha\), hence
\[
\|B(y_j)\|_2\ge\|B(x_j)\|_2-\|B\|\alpha\ge3\eta/4 .
\]
From \(\alpha^2r_j\le|x_j|^2\) and \(\rho(v_jr_jv_j^*)=\rho(r_jv_j^*v_jr_j)=\rho(r_j)\),
\[
\begin{aligned}
\rho(e_j)&\le\rho(r_j)+\rho(\ell_j)=2\rho(r_j)\\
&\le2\alpha^{-2}\|x_j\|_2^2 .
\end{aligned}
\]
Pass to a subsequence with \(\sum_j\rho(e_j)<\infty\), and put \(p_j=\bigvee_{h\ge j}e_h\). The projections \(p_j\) decrease, and \(\rho(p_j)\le\sum_{h\ge j}\rho(e_h)\to0\). Their infimum has trace \(0\), so it is \(0\) because \(\rho\) is faithful, and \(p_j\to0\) strongly (Corollary 1.4 of the Kaplansky lesson).

Fix \(j\). As \(h\to\infty\), \(p_j-p_h\to p_j\) strongly, so \((p_j-p_h)y_j(p_j-p_h)\to p_jy_jp_j=y_j\) strongly (Proposition 8.6 of the lesson on operator topologies), using \(e_j\le p_j\). This bounded convergence is also ultraweak, and the normal map \(B\) preserves it. The \(2\)-norm is ultraweakly lower semicontinuous, being
\[
\begin{aligned}
\|y\|_2=\sup\{&|\rho(c^*y)|:\ c\in N,\\
&\|c\|_2\le1\},
\end{aligned}
\]
a supremum of ultraweakly continuous functions. Hence
\[
\begin{aligned}
&\liminf_{h\to\infty}\|B((p_j-p_h)y_j(p_j-p_h))\|_2\\
&\qquad\ge3\eta/4 .
\end{aligned}
\]
Starting from \(j_1=1\), choose \(j_{s+1}>j_s\) such that
\[
\begin{gathered}
t_s=(p_{j_s}-p_{j_{s+1}})\,y_{j_s}\,(p_{j_s}-p_{j_{s+1}})\\
\text{satisfies}\quad\|B(t_s)\|_2\ge\eta/2 .
\end{gathered}
\]
The projections \(q_s=p_{j_s}-p_{j_{s+1}}\) are pairwise orthogonal, since \(q_{s'}\le p_{j_{s+1}}\) for \(s'>s\). As \(t_s=q_st_sq_s\) and \(\|t_s\|\le R\), every choice of signs \(\epsilon_s=\pm1\) gives \(\|\sum_{s\le n}\epsilon_st_s\|\le R\). For independent uniform random signs, \(\mathbb E[\epsilon_s\epsilon_{s'}]=0\) for \(s\ne s'\), so
\[
\begin{aligned}
\frac{n\eta^2}4&\le\sum_{s=1}^n\|B(t_s)\|_2^2\\
&=\mathbb E\Bigl\|B\Bigl(\sum_{s=1}^n\epsilon_st_s\Bigr)\Bigr\|_2^2\\
&\le\|B\|^2R^2 ,
\end{aligned}
\]
which fails for large \(n\). \(\square\)

Exercise 4.5 proves the converse: a bounded linear map of \(N\) that is continuous on balls for the \(2\)-norm is normal.

## 3. Classical reductions and the route

Two classical theorems reduce Theorem 1.2 to separately normal cocycles on algebras of type \(\mathrm{II}_1\). They are used in the course without proof.

**K1 (normal reduction; Johnson, Kadison and Ringrose).** Let \(M\) be a von Neumann algebra and \(k\ge2\). If \(f\in C_b^k(M,M)\) is a cocycle, there are a separately normal bounded cocycle \(f_0\) and \(b\in C_b^{k-1}(M,M)\) with \(f=f_0+db\).

This is Lemma 5.4 and Theorem 5.6 of B. E. Johnson, R. V. Kadison and J. R. Ringrose, [*Cohomology of operator algebras III: reduction to normal cohomology*](https://www.numdam.org/item/BSMF_1972__100__73_0/), Bull. Soc. Math. France 100 (1972), 73–96.

**K2 (algebras without a type \(\mathrm{II}_1\) summand).** Let \(M\) be a von Neumann algebra with no type \(\mathrm{II}_1\) central summand, and \(k\ge2\). Then \(H_b^k(M,M)=0\).

This combines the type I case, Theorem 4.4 of R. V. Kadison and J. R. Ringrose, [*Cohomology of operator algebras I. Type I von Neumann algebras*](https://archive.ymsc.tsinghua.edu.cn/pacm_paperurl/20170108203222172234112), Acta Math. 126 (1971), 227–243, with the properly infinite case of E. Christensen, E. G. Effros and A. Sinclair, [*Completely bounded multilinear maps and C\*-algebraic cohomology*](https://gdz.sub.uni-goettingen.de/id/PPN356556735_0090), Invent. Math. 90 (1987), 279–296. The combined statement is equation (1.1) of E. Christensen, F. Pop, A. M. Sinclair and R. R. Smith, [*Hochschild cohomology of factors with property \(\Gamma\)*](https://arxiv.org/abs/math/0107078), Ann. of Math. 158 (2003), 635–659.

**Free Haar families.** In a von Neumann algebra with faithful tracial state \(\tau\), a unitary \(u\) is *Haar* if \(\tau(u^k)=0\) for \(k\ne0\). Unitaries \(g_1,g_2,\ldots\) form a *free Haar family* if \(\tau(w(g))=0\) for every nonidentity reduced word \(w\) in the free group on \(x_1,x_2,\ldots\).

**The route.** Let \(M\) be of type \(\mathrm{II}_1\) with separable predual and faithful normal tracial state \(\tau\). The remaining lessons prove Theorem 1.2 in four steps.

1. [*Rigidity of first-letter identities*](rigidity-of-first-letter-identities.md) proves a statement about a single bounded map \(R\), continuous on balls for the \(2\)-norm, on a finite von Neumann algebra containing a free Haar family. If \(R\) multiplies every word with pairwise distinct indices on the left by \(a\) or by \(b\), according to whether its first letter is a generator or an inverse, then \(a=b\).
2. [*A random walk with asymptotically free products*](a-random-walk-with-asymptotically-free-products.md) constructs a symmetric probability measure \(\mu\) on the unitary group of \(M\), with a \(2\)-norm dense set of atoms, whose long independent products have asymptotically the joint moments of free Haar unitaries.
3. [*The Liouville theorem*](the-liouville-theorem.md) proves: if \(T:M\to M\) is bounded, linear, continuous on balls for the \(2\)-norm, and harmonic, \(T(x)=\mathbb E_{U\sim\mu}[T(xU)U^*]\), then \(T(x)=T(1)x\). A nonconstant limit of the associated martingale would produce, in an ultrapower, exactly the identities excluded by the rigidity theorem.
4. [*Bounded primitives*](bounded-primitives.md) averages a separately normal cocycle in its last variable along the walk. The Liouville theorem makes the average a right module map in that variable, and this yields a primitive \(g\) with \(\|g\|\le\|f\|\). The uniform bound removes the separability assumption and allows central pieces to be assembled; K1 and K2 handle the general case.

## 4. Exercises

**4.1** (easy). Show that \(\|df\|\le(k+2)\|f\|\) on \(C_b^k(M,M)\), and that the kernel of \(d:C_b^0\to C_b^1\) is the centre of \(M\).

**4.2** (easy). Show that the cocycles of degree one are the derivations of \(M\).

**4.3** (medium). For \(f\in C_b^2(M,M)\), define a bilinear product on \(M\oplus M\) by
\[
\begin{aligned}
&(a,a')*(b,b')\\
&\quad=\bigl(ab,\ a'b+ab'+f(a,b)\bigr).
\end{aligned}
\]
Show that \(*\) is associative if and only if \(df=0\).

**4.4** (medium). Let \(N\subseteq B(H)\) be a von Neumann algebra with a faithful normal tracial state \(\rho\), and let \((x_i)\) be a net in \(N\) with \(\sup_i\|x_i\|<\infty\). Show that \(\|x_i\|_2\to0\) if and only if \(x_i\to0\) strongly, and that both are equivalent to \(x_i\to0\) strongly-star.

**4.5** (hard). Let \((N,\rho)\) be as in Exercise 4.4 and let \(B:N\to N\) be bounded, linear and continuous on balls for the \(2\)-norm. Show that \(B\) is normal. Together with Lemma 2.3: a bounded linear map of \(N\) is normal if and only if it is continuous on balls for the \(2\)-norm.

## 5. Solutions

**4.1.** Each of the \(k+2\) terms of \((df)(a_1,\ldots,a_{k+1})\) has norm at most \(\|f\|\prod_i\|a_i\|\). The element \(b\) lies in the kernel of \(d\) exactly when \(ab-ba=0\) for all \(a\in M\).

**4.2.** For \(f\in C_b^1\), \((df)(a_1,a_2)\) is \(a_1f(a_2)-f(a_1a_2)+f(a_1)a_2\), which vanishes for all \(a_1,a_2\) exactly when \(f\) is a derivation.

**4.3.** Expand both products of three elements. In the first component both are \(abc\). In the second component, \(((a,a')*(b,b'))*(c,c')\) has
\[
a'bc+ab'c+f(a,b)c+abc'+f(ab,c),
\]
and \((a,a')*((b,b')*(c,c'))\) has
\[
a'bc+ab'c+abc'+af(b,c)+f(a,bc).
\]
The difference is
\[
\begin{aligned}
&f(a,b)c+f(ab,c)\\
&\quad-af(b,c)-f(a,bc)\\
&\quad=-(df)(a,b,c).
\end{aligned}
\]
So \(*\) is associative exactly when \(df=0\).

**4.4.** Let \(r=\sup_i\|x_i\|\). The state \(\rho\) is ultraweakly, hence ultrastrongly, continuous (Theorem 9.1 of the lesson on operator topologies), so by Theorem 10.1 of the double commutant lesson there are vectors \(\xi_n\) with \(\sum_n\|\xi_n\|^2<\infty\) and \(\rho(y)=\sum_n\langle y\xi_n,\xi_n\rangle\) for \(y\in N\). Then \(\|x\|_2^2=\sum_n\|x\xi_n\|^2\).

If \(x_i\to0\) strongly, choose \(n_0\) with \(r^2\sum_{n>n_0}\|\xi_n\|^2<\varepsilon\). The finitely many terms with \(n\le n_0\) tend to \(0\), so \(\limsup_i\|x_i\|_2^2\le\varepsilon\) for every \(\varepsilon>0\).

Conversely, let \(e\) be the projection onto the closed span \(K\) of the vectors \(x'\xi_n\), \(x'\in N'\), \(n\ge1\). The subspace \(K\) is invariant under the self-adjoint set \(N'\), so \(e\) commutes with \(N'\) and lies in \(N''=N\). Since every \(\xi_n\) lies in \(K\), \(\rho(1-e)=\sum_n\|(1-e)\xi_n\|^2=0\), and \(e=1\) by faithfulness. For \(x'\in N'\),
\[
\begin{aligned}
\|x_ix'\xi_n\|&=\|x'x_i\xi_n\|\\
&\le\|x'\|\,\|x_i\xi_n\|\\
&\le\|x'\|\,\|x_i\|_2 .
\end{aligned}
\]
So \(\|x_i\|_2\to0\) gives \(x_i\eta\to0\) for all \(\eta\) in a dense subspace of \(H\), and the bound \(\|x_i\|\le r\) extends this to all \(\eta\in H\). Finally, \(\|x_i^*\|_2=\|x_i\|_2\), so the same argument applied to \((x_i^*)\) gives strong-star convergence.

**4.5.** For \(c\in N\) put \(\psi_c(x)=\rho(c^*B(x))\). By the Cauchy–Schwarz inequality, \(|\psi_c(x)-\psi_c(x')|\le\|c\|_2\,\|B(x-x')\|_2\). Let \((x_i)\) be a net in the unit ball \(N_1\) converging strongly to \(x\in N_1\). By Exercise 4.4, \(\|x_i-x\|_2\to0\); by Lemma 2.2(1) with the radius \(2\), \(\|B(x_i-x)\|_2\to0\). So \(\psi_c\) is strongly continuous on \(N_1\), and by Theorem 9.5 of the lesson on operator topologies it is ultraweakly continuous.

The functionals \(\rho(c^*\,\cdot\,)\), \(c\in N\), are ultraweakly continuous, and they are norm dense in the predual \(N_*\). Indeed, by Theorem 9.4(b) of the same lesson every bounded functional on \(N_*\) is evaluation at some \(a\in N\); if it vanishes on all \(\rho(c^*\,\cdot\,)\), then \(\rho(a^*a)=0\) and \(a=0\), and the Hahn–Banach theorem gives density. Given \(\omega\in N_*\), choose \(c_n\) with \(\|\omega-\rho(c_n^*\,\cdot\,)\|\to0\). Then
\[
\begin{aligned}
\|\omega\circ B-\psi_{c_n}\|&\le\|B\|\,\|\omega-\rho(c_n^*\,\cdot\,)\|\\
&\to0 ,
\end{aligned}
\]
and \(N_*\) is norm closed in \(N^*\) (Theorem 9.4(a)), so \(\omega\circ B\in N_*\). Since the ultraweak topology is \(\sigma(N,N_*)\) (Theorem 9.4(b)), \(B\) is ultraweakly continuous.

## Sources

- [OpenAI-295] OpenAI, *Vanishing of higher bounded Hochschild cohomology*, OpenAI Math Release preprint, 23 September 2026, Section 1 (the problem, the classical reductions and the strategy), Section 3.1 (Lemma 2.2) and Section 5.1 (Lemma 2.3). https://github.com/openai/math/tree/main/preprints/Vanishing-of-higher-bounded-Hochschild-cohomology-September-23-2026
- C. A. Akemann, [*The dual space of an operator algebra*](https://www.ams.org/journals/tran/1967-126-02/S0002-9947-1967-0206732-8/), Trans. Amer. Math. Soc. 126 (1967), 286–302, Corollary III.10: the general continuity theorem of which Lemma 2.3 is the tracial case.
- The papers of Johnson, Kadison and Ringrose, Kadison and Ringrose, Christensen, Effros and Sinclair, and Christensen, Pop, Sinclair and Smith cited in Section 3.
