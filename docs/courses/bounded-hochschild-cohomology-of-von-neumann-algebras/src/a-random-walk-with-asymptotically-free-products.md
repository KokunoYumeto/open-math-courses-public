# A random walk with asymptotically free products

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(M\) be a von Neumann algebra of type \(\mathrm{II}_1\) with separable predual and faithful normal tracial state \(\tau\); its centre may be nontrivial. This lesson constructs one symmetric probability measure \(\mu\) on the unitary group \(\mathcal U(M)\), with countably many atoms, whose long products behave like free Haar unitaries. If \(G_1,\ldots,G_r\) are independent products of \(n_\ell\) independent \(\mu\)-distributed unitaries, then for every nonidentity word \(w\) the trace \(\tau(w(G_1,\ldots,G_r))\) tends to \(0\) in probability as \(\ell\to\infty\). The atoms of \(\mu\) include a \(2\)-norm dense sequence of unitaries. The Liouville theorem of the next lesson rests on this measure.

Section 1 proves the facts about freeness that are used. Section 2 chooses finitely many unitaries that satisfy finitely many trace conditions approximately: for a factor through Popa's free independence theorem in a tracial ultrapower, and in general fibre by fibre in the central decomposition. Section 3 places these choices at increasingly rare levels of a single measure.

**Prerequisites.** [*The cohomology problem*](the-cohomology-problem.md), Exercise 4.4 (on bounded sets, convergence in the \(2\)-norm is strong convergence). From *Generators of II₁ factors*: [*Haar unitaries, freeness and tracial ultraproducts*](course:generators-of-ii1-factors/haar-unitaries-freeness-and-ultraproducts) (Lemma 1.1, Definition 3.1, the tracial ultraproduct of Section 4) and [*Free independence in ultraproducts*](course:generators-of-ii1-factors/free-independence-in-ultraproducts) (Corollary 4.4 and the remark after it). From *Measurable fields and direct integrals*: [*The central decomposition and the types of the fibres*](course:measurable-fields-and-direct-integrals/the-central-decomposition-and-the-types-of-the-fibres) (Facts 1.1 and 1.2, Corollary 3.6, Theorems 4.1 and 5.3). From *Foundations of von Neumann algebras*: [*Kaplansky's density theorem and its consequences*](course:foundations-of-von-neumann-algebras/kaplansky-s-density-theorem-and-its-consequences) (Corollary 4.5, unitaries are exponentials; Theorem 7.1); [*Compact and trace-class operators, the predual of B(H) and the operator topologies*](course:foundations-of-von-neumann-algebras/compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies) (Lemma 8.5, Theorems 9.4 and 9.6); [*Weak topologies*](course:foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian) (Theorem 3.1, Banach–Alaoglu, and Proposition 3.2, metrizability); [*The double commutant theorem*](course:foundations-of-von-neumann-algebras/the-double-commutant-theorem) (Theorem 4.4); [*The universal enveloping von Neumann algebra of a C\*-algebra and W\*-algebras*](course:foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras) (Corollary 11.4, isomorphisms are normal).

**Notation.** A *tracial von Neumann algebra* \((N,\tau)\) is a von Neumann algebra with a faithful normal tracial state, and \(\|x\|_2=\tau(x^*x)^{1/2}\). Then \(|\tau(x)|\le\|x\|_2\) and \(\|axb\|_2\le\|a\|\,\|x\|_2\,\|b\|\) (Lemma 1.1 of the Haar lesson); in particular \(\|axb\|_2=\|x\|_2\) for unitaries \(a,b\). An element \(x\) is *centred* if \(\tau(x)=0\), and \(x^\circ=x-\tau(x)1\). A unitary \(t\) is *Haar* if \(\tau(t^k)=0\) for all \(k\ne0\). \(\mathcal U(N)\) is the unitary group. \(\mathbb F_r\) is the free group on \(x_1,\ldots,x_r\), \(|w|\) is the length of the reduced form of \(w\), and \(w(g_1,\ldots,g_r)\) is the evaluation at unitaries \(g_i\).

## 1. Freeness

**Definition 1.1.** Unital \(*\)-subalgebras \(A_i\), \(i\in I\), of a tracial von Neumann algebra \((N,\tau)\) are *free* if \(\tau(a_1a_2\cdots a_m)=0\) whenever \(m\ge1\), each \(a_j\) is a centred element of some \(A_{i_j}\), and \(i_j\ne i_{j+1}\) for \(1\le j<m\). A product of this form is called *alternating*. A unitary \(t\) is *free from* a unital C\*-subalgebra \(D\) when \(C^*(t)\) and \(D\) are free; this is Definition 3.1 of the Haar lesson.

Free algebras remain free when each is replaced by a unital \(*\)-subalgebra.

**Lemma 1.2 (successive freeness).** Let \(D_0\subseteq N\) be a unital C\*-subalgebra and \(t_1,\ldots,t_d\) unitaries such that \(t_j\) is free from \(D_{j-1}=C^*(D_0,t_1,\ldots,t_{j-1})\) for each \(j\). Then \(D_0,C^*(t_1),\ldots,C^*(t_d)\) are free.

**Proof.** Induction on \(d\); for \(d=1\) this is the hypothesis. Let \(d\ge2\), and let \(x=a_1\cdots a_m\) be an alternating product for the family, \(a_j\) being a centred element of the member with index \(i_j\in\{0,\ldots,d\}\), where index \(0\) stands for \(D_0\). If no \(i_j\) equals \(d\), then \(\tau(x)=0\) by the induction hypothesis. Otherwise group each maximal run of consecutive factors with indices different from \(d\) into one element. Such a run is an alternating product for \(D_0,C^*(t_1),\ldots,C^*(t_{d-1})\), so it lies in \(D_{d-1}\) and is centred by the induction hypothesis. Two factors with index \(d\) are separated by at least one run, since consecutive indices differ. So \(x\) is an alternating product of centred elements of \(C^*(t_d)\) and of \(D_{d-1}\) with at least one factor from \(C^*(t_d)\), and \(\tau(x)=0\) because \(t_d\) is free from \(D_{d-1}\). \(\square\)

**Lemma 1.3 (grouping).** Let \(A_i\), \(i\in I\), be free unital \(*\)-subalgebras of \(N\), let \(I=I_1\sqcup I_2\), and let \(B_k\) be the unital \(*\)-subalgebra generated by the \(A_i\) with \(i\in I_k\). Then \(B_1\) and \(B_2\) are free.

**Proof.** Let \(W_k\) be the set of alternating products of centred elements of the \(A_i\) with \(i\in I_k\), and \(V_k\) the span of \(1\) and \(W_k\). Then \(V_k\) contains each such \(A_i\), because \(a=\tau(a)1+a^\circ\), and it is closed under adjoints, because the adjoint of an alternating product is the alternating product of the adjoints in reverse order. It is closed under multiplication. Indeed, the product of \(a_1\cdots a_m\) and \(b_1\cdots b_n\) in \(W_k\) is alternating if \(a_m\) and \(b_1\) come from different algebras; otherwise it equals
\[
\begin{aligned}
&\tau(a_mb_1)\,(a_1\cdots a_{m-1})(b_2\cdots b_n)\\
&\quad+a_1\cdots a_{m-1}\,(a_mb_1)^\circ\,b_2\cdots b_n ,
\end{aligned}
\]
where empty products are \(1\). The second term is alternating, and the first lies in \(V_k\) by induction on \(m+n\). Hence \(V_k=B_k\). Every element of \(W_k\) has trace \(0\) by freeness, so every centred element of \(B_k\) lies in the span of \(W_k\).

Let \(b_1,\ldots,b_m\) be centred elements alternating between \(B_1\) and \(B_2\), and expand each \(b_j\) as a combination of elements of \(W_1\) or \(W_2\). Each resulting term is a concatenation of alternating products. At each junction one factor comes from an algebra with index in \(I_1\) and the other from one with index in \(I_2\). So each term is an alternating product for the family \((A_i)\), and has trace \(0\). \(\square\)

**Lemma 1.4 (distinguished letters).** Let \(D_0\subseteq N\) be a unital C\*-subalgebra, and \(t_1,\ldots,t_d\) Haar unitaries such that \(D_0,C^*(t_1),\ldots,C^*(t_d)\) are free. Let \(F\subseteq\mathcal U(D_0)\). A *path expression* is a finite formal product of letters from \(F\cup\{U_1^{\pm1},\ldots,U_d^{\pm1}\}\). The letter \(U_j^{\pm1}\) has the *label* \(j\), and occurrences of labels are counted in the formal product, before any simplification. Let \(y_1,\ldots,y_r\) be path expressions, and \(y_i(t)\in\mathcal U(N)\) their values at \(U_j=t_j\). Suppose that for each \(i\) some label \(h_i\) occurs exactly once in the whole list \(y_1,\ldots,y_r\), and that this occurrence lies in \(y_i\). Then
\[
\begin{gathered}
\tau\bigl(w(y_1(t),\ldots,y_r(t))\bigr)=0\\
(w\in\mathbb F_r,\ w\ne e).
\end{gathered}
\]

**Proof.** The labels \(h_i\) are distinct, since a label shared by \(y_i\) and \(y_{i'}\) would occur twice. Put \(H=\{h_1,\ldots,h_r\}\). Let \(B\) be the unital \(*\)-algebra generated by \(D_0\) and the \(t_j\) with \(j\notin H\), and \(C\) the one generated by the \(t_h\) with \(h\in H\). By Lemma 1.3, \(B\) and \(C\) are free.

A nonempty reduced word in the \(t_h\), \(h\in H\), is centred: grouping equal adjacent letters writes it as \(t_{g_1}^{k_1}\cdots t_{g_q}^{k_q}\) with \(k_j\ne0\) and \(g_j\ne g_{j+1}\), an alternating product of the centred elements \(t_{g_j}^{k_j}\) of the free family.

The only letter of \(y_i\) with a label in \(H\) is the occurrence of \(h_i\), so
\[
\begin{gathered}
y_i(t)=A_i\,t_{h_i}^{\epsilon_i}\,B_i,\\
A_i,B_i\in\mathcal U(B),\quad\epsilon_i=\pm1 .
\end{gathered}
\]
Let \(w=x_{i_1}^{\sigma_1}\cdots x_{i_m}^{\sigma_m}\) be reduced, \(m\ge1\). Since \(y_i(t)^{-1}=B_i^*t_{h_i}^{-\epsilon_i}A_i^*\),
\[
w(y(t))=c_0\,t_{h_{i_1}}^{e_1}\,c_1\cdots t_{h_{i_m}}^{e_m}\,c_m ,
\]
with \(e_k=\epsilon_{i_k}\sigma_k\) and \(c_k\in\mathcal U(B)\). The word \(t_{h_{i_1}}^{e_1}\cdots t_{h_{i_m}}^{e_m}\) is reduced: two adjacent letters cancel only if \(i_k=i_{k+1}\) and \(\sigma_k=-\sigma_{k+1}\), which does not occur in the reduced word \(w\).

Write \(c_k=\tau(c_k)1+c_k^\circ\) and expand into \(2^{m+1}\) terms. In each term the scalars factor out, and the retained centred coefficients \(c_k^\circ\) cut the reduced word into nonempty contiguous pieces; a piece lies before the first retained coefficient, between two retained coefficients, or after the last one. Each piece is a centred element of \(C\). If no centred coefficient is retained, the term is a multiple of the whole reduced word, which has trace \(0\). Otherwise the term is a multiple of an alternating product of centred elements of \(B\) and \(C\). There is a letter between any two retained coefficients, and at least one piece since \(m\ge1\). Freeness of \(B\) and \(C\) gives trace \(0\). \(\square\)

## 2. Finitely many conditions

**Definition 2.1.** Let \((N,\tau)\) be a tracial von Neumann algebra, \(F\subseteq\mathcal U(N)\) finite and \(d\ge1\). A *test* over \(F\) with \(d\) unknowns consists of a list \(y=(y_1,\ldots,y_r)\) of path expressions in the letters \(F\cup\{U_1^{\pm1},\ldots,U_d^{\pm1}\}\) and a word \(w\in\mathbb F_r\setminus\{e\}\), such that for each \(i\) some label occurs exactly once in the list, in \(y_i\). Its *value* at \(u=(u_1,\ldots,u_d)\in\mathcal U(N)^d\) is \(\tau(w(y_1(u),\ldots,y_r(u)))\).

**Lemma 2.2 (the factor case).** Let \(P\) be a II₁ factor with faithful normal tracial state \(\tau\), \(F\subseteq\mathcal U(P)\) finite, \(d\ge1\), \(\varepsilon>0\), and \(\mathcal T\) a finite set of tests over \(F\) with \(d\) unknowns. There is \(u\in\mathcal U(P)^d\) at which every test in \(\mathcal T\) has value of absolute value less than \(\varepsilon\).

**Proof.** Let \(\omega\) be a free ultrafilter on \(\mathbb N\) and \(P^\omega\) the tracial ultrapower, with trace \(\tau_\omega((x_n)_\omega)=\lim_{n\to\omega}\tau(x_n)\); \(P\) is identified with the constant sequences. The C\*-algebra \(D_0=C^*(F)\subseteq P^\omega\) is norm separable: polynomials with rational coefficients in the elements of \(F\) and their adjoints are dense in it. The inclusion \(P\subseteq P\) is irreducible, since \(P\) is a factor. Corollary 4.4 of the lesson on free independence, applied \(d\) times as in the remark after it, gives Haar unitaries \(t_1,\ldots,t_d\in P^\omega\), each with a representing sequence \((t_{j,n})_n\) of unitaries of \(P\), such that \(t_j\) is free from \(C^*(D_0,t_1,\ldots,t_{j-1})\). By Lemma 1.2, \(D_0,C^*(t_1),\ldots,C^*(t_d)\) are free, and by Lemma 1.4 every test in \(\mathcal T\) has value \(0\) at \(t=(t_1,\ldots,t_d)\).

The quotient map from bounded sequences onto \(P^\omega\) is a unital \(*\)-homomorphism, so the value of a test at \(t\) is \(\lim_{n\to\omega}\) of its values at \(t_n=(t_{1,n},\ldots,t_{d,n})\). For each test the set of \(n\) where that value has absolute value less than \(\varepsilon\) belongs to \(\omega\); so does the intersection of these finitely many sets, which is therefore nonempty. For \(n\) in it, \(u=t_n\) has the required property. \(\square\)

**Lemma 2.3 (separability).** Let \((M,\tau)\) be a tracial von Neumann algebra with separable predual.

1. The closed unit ball \(M_1\) is separable for the \(2\)-norm. In particular \(\mathcal U(M)\) contains a sequence that is dense for the \(2\)-norm.
2. Let \(L^2(M)\) be the completion of \(M\) for \(\langle x,y\rangle=\tau(y^*x)\), with \(\hat x\) the class of \(x\), and \(\lambda(x)\hat y=\widehat{xy}\). Then \(L^2(M)\) is separable, \(\lambda\) is an injective unital \(*\)-homomorphism onto a von Neumann algebra \(\lambda(M)\) on \(L^2(M)\), and \(\tau\circ\lambda^{-1}\) is a faithful normal tracial state on \(\lambda(M)\).

**Proof.** (1) The ultraweak topology of \(M\) is \(\sigma(M,M_*)\) (Theorem 9.4 of the lesson on operator topologies), so \(M_1\) is ultraweakly compact (Banach–Alaoglu) and metrizable (Proposition 3.2 of the lesson on weak topologies), hence separable. Let \(D\subseteq M_1\) be countable and ultraweakly dense in \(M_1\), and let \(C\) be the countable set of convex combinations of elements of \(D\) with rational coefficients. Let \(x\in M_1\). It lies in the ultraweak closure of the convex hull of \(D\), hence in its weak closure (Lemma 8.5 there, the hull being bounded), which equals its strong closure (Theorem 9.6(a) there). So \(x\) is the strong limit of a net in \(M_1\) from the convex hull of \(D\), hence its \(2\)-norm limit (Exercise 4.4 of the lesson on the cohomology problem). Elements of the convex hull are operator-norm limits of elements of \(C\), and \(\|\cdot\|_2\le\|\cdot\|\). So \(C\) is \(2\)-norm dense in \(M_1\), and the subset \(\mathcal U(M)\) of this separable metric space is separable.

(2) Since \(M=\bigcup_nnM_1\), part (1) shows that \(L^2(M)\) is separable. As \(\|xy\|_2\le\|x\|\,\|y\|_2\), \(\lambda(x)\) extends to a bounded operator. The map \(\lambda\) is linear, multiplicative and unital, and \(\langle\lambda(x)\hat y,\hat z\rangle=\tau(z^*xy)=\langle\hat y,\lambda(x^*)\hat z\rangle\) gives \(\lambda(x)^*=\lambda(x^*)\). If \(\lambda(x)=0\), then \(\hat x=\lambda(x)\hat1=0\) and \(x=0\). An injective \(*\)-homomorphism between C\*-algebras is isometric, so \(\lambda(rM_1)\) is the intersection of \(\lambda(M)\) with the ball of radius \(r\).

For \(y,z\in M\), the function \(x\mapsto\langle\lambda(x)\hat y,\hat z\rangle=\tau(yz^*x)\) is ultraweakly continuous. For \(\xi,\eta\in L^2(M)\), the function \(x\mapsto\langle\lambda(x)\xi,\eta\rangle\) is a uniform limit of such functions on \(rM_1\), hence ultraweakly continuous there. So \(\lambda\) maps the ultraweakly compact set \(rM_1\) onto a weakly compact, hence weakly closed, set. By Theorem 9.6(b) of the lesson on operator topologies, the convex set \(\lambda(M)\) is ultraweakly closed, and by the double commutant theorem it is a von Neumann algebra. Finally, \(\lambda^{-1}\) is a \(*\)-isomorphism between von Neumann algebras, hence ultraweakly continuous (Corollary 11.4 of the lesson on W\*-algebras), so \(\tau\circ\lambda^{-1}\) is normal; it is faithful and tracial because \(\tau\) is. \(\square\)

In the rest of this lesson, a von Neumann algebra with separable predual and faithful normal tracial state is identified with \(\lambda(M)\) on the separable Hilbert space \(L^2(M)\).

**Lemma 2.4 (fibres).** Let \((M,\tau)\) be of type \(\mathrm{II}_1\) with separable predual. Write \(M=\int^\oplus M(\gamma)\,d\mu(\gamma)\) by the central decomposition (Theorem 4.1 of the lesson on the central decomposition), with \(\mu\) a Borel probability measure on \(\mathbb R\) and every \(M(\gamma)\) a factor. Every \(x\in M\) is \(\int^\oplus x(\gamma)\) for a measurable field with \(x(\gamma)\in M(\gamma)\) and \(\|x(\gamma)\|\le\|x\|\), determined almost everywhere, and \(x\mapsto x(\gamma)\) is almost everywhere linear, multiplicative and \(*\)-preserving (Facts 1.1(e) and 1.2(b) there).

1. There are a measurable function \(\rho\ge0\) with \(\int\rho\,d\mu=1\) and, for \(\nu\)-almost every \(\gamma\), where \(\nu=\rho\mu\), a faithful normal tracial state \(\tau_\gamma\) on the II₁ factor \(M(\gamma)\), such that for every \(x\in M\) the function \(\gamma\mapsto\tau_\gamma(x(\gamma))\) is \(\nu\)-measurable and
\[
\tau(x)=\int\tau_\gamma(x(\gamma))\,d\nu(\gamma).
\]
2. There are measurable operator fields \(v_1,v_2,\ldots\) such that \(\int^\oplus v_j\in\mathcal U(M)\) for every \(j\) and, for \(\nu\)-almost every \(\gamma\), the \(v_j(\gamma)\) form a subset of \(\mathcal U(M(\gamma))\) that is dense for the \(2\)-norm of \(\tau_\gamma\).

**Proof.** (1) By Corollary 3.6 there, there are normal positive functionals \(\varphi_\gamma\) on \(M(\gamma)\), tracial and faithful for almost every \(\gamma\), such that \(\gamma\mapsto\varphi_\gamma(x(\gamma))\) is integrable and \(\tau(x)=\int\varphi_\gamma(x(\gamma))\,d\mu(\gamma)\). Put \(\rho(\gamma)=\varphi_\gamma(1)\); then \(\int\rho\,d\mu=\tau(1)=1\). Where \(\rho(\gamma)=0\), the positive functional \(\varphi_\gamma\) vanishes, since \(|\varphi_\gamma(x)|\le\|x\|\varphi_\gamma(1)\). Where \(\rho(\gamma)>0\), put \(\tau_\gamma=\varphi_\gamma/\rho(\gamma)\). This gives the formula. For \(\nu\)-almost every \(\gamma\), the factor \(M(\gamma)\) is nonzero, \(\tau_\gamma\) is a faithful normal tracial state, and \(M(\gamma)\) is of type \(\mathrm{II}_1\) by Theorem 5.3 there, because \(M\) is; so \(M(\gamma)\) is a II₁ factor.

(2) By Fact 1.2(a) there, there are measurable operator fields \(a_1,a_2,\ldots\) with \(\|a_k(\gamma)\|\le1\) for every \(\gamma\) such that, for almost every \(\gamma\), the \(a_k(\gamma)\) lie in \(M(\gamma)\) and are ultraweakly dense in its unit ball. Let \(\mathcal Q\) be the countable set of noncommutative polynomials \(q\) in finitely many variables \(X_k\) and \(X_k^*\), with coefficients in \(\mathbb Q+i\mathbb Q\), that equal their formal adjoint. For \(q\in\mathcal Q\), the field \(q(a)\) is measurable (Fact 1.1(d)), self-adjoint and bounded, and
\[
\begin{aligned}
v_q(\gamma)&=\exp\bigl(iq(a(\gamma))\bigr)\\
&=\sum_{n\ge0}\frac{(iq(a(\gamma)))^n}{n!}
\end{aligned}
\]
is a measurable field of unitaries: applied to a measurable section, the partial sums give measurable sections converging at every point (Fact 1.1(a)). Almost everywhere \(v_q(\gamma)\in M(\gamma)\), so \(\int^\oplus v_q\) is a unitary of \(M\).

Fix \(\gamma\) outside a \(\nu\)-null set, so that (1) holds at \(\gamma\) and the \(a_k(\gamma)\) are ultraweakly dense in the unit ball of \(M(\gamma)\). Let \(A_\gamma\) be the \(*\)-algebra generated by the \(a_k(\gamma)\); its weak closure is \(M(\gamma)\). Let \(u\in\mathcal U(M(\gamma))\) and \(\delta>0\). By Corollary 4.5 of the Kaplansky lesson, \(u=\exp(ih)\) with \(h=h^*\in M(\gamma)\) and \(\|h\|\le\pi\). By Kaplansky's density theorem (Theorem 7.1(2) there), \(h\) is the strong limit of a net of self-adjoint elements of \(A_\gamma\) of norm at most \(\pi\), hence its \(2\)-norm limit (Exercise 4.4 of the lesson on the cohomology problem, for \(M(\gamma)\) and \(\tau_\gamma\)). Choose such an element \(b=p(a(\gamma))\), \(p\) a polynomial with complex coefficients, with \(\|b-h\|_2<\delta/2\). Since \(b=b^*\), we may replace \(p\) by \((p+p^*)/2\). Approximating its finitely many coefficients by elements of \(\mathbb Q+i\mathbb Q\) and symmetrizing gives \(q\in\mathcal Q\) with \(\|q(a(\gamma))-b\|<\delta/2\), as \(\|a_k(\gamma)\|\le1\). So \(\|q(a(\gamma))-h\|_2<\delta\).

For self-adjoint \(a,b\) in a tracial algebra, \(\|e^{ia}-e^{ib}\|_2\le\|a-b\|_2\). Indeed, \(s\mapsto e^{i(1-s)a}e^{isb}\) is norm differentiable with derivative \(-ie^{i(1-s)a}(a-b)e^{isb}\), so
\[
e^{ia}-e^{ib}=i\int_0^1e^{i(1-s)a}(a-b)e^{isb}\,ds ,
\]
and the integrand has \(2\)-norm \(\|a-b\|_2\). Hence \(\|v_q(\gamma)-u\|_2<\delta\). \(\square\)

**Proposition 2.5 (finitely many conditions).** Let \((M,\tau)\) be of type \(\mathrm{II}_1\) with separable predual, \(F\subseteq\mathcal U(M)\) finite, \(d\ge1\), \(\varepsilon>0\), and \(\mathcal T\) a finite set of tests over \(F\) with \(d\) unknowns. There is \(u\in\mathcal U(M)^d\) at which every test in \(\mathcal T\) has value of absolute value less than \(\varepsilon\).

**Proof.** Use the notation of Lemma 2.4. Remove a \(\nu\)-null set so that at every remaining \(\gamma\): (1) and (2) of Lemma 2.4 hold, the values \(f(\gamma)\), \(f\in F\), are unitaries of \(M(\gamma)\), and the fibre map is multiplicative on the countably many products used below. For such \(\gamma\) and \(u\in\mathcal U(M(\gamma))^d\), let \(\mathrm{val}_T(\gamma,u)\) be the value of the test \(T\) computed in \((M(\gamma),\tau_\gamma)\) with the coefficients \(f(\gamma)\).

For unitaries in a tracial algebra,
\[
\|z_1\cdots z_L-z_1'\cdots z_L'\|_2\le\sum_{j=1}^L\|z_j-z_j'\|_2 ,
\]
by writing the difference as \(\sum_jz_1\cdots z_{j-1}(z_j-z_j')z_{j+1}'\cdots z_L'\); also \(\|z^*-z'^*\|_2=\|z-z'\|_2\), and \(|\tau(x)|\le\|x\|_2\). So if \(T\) has \(L_T\) letters \(U_j^{\pm1}\) after expanding \(w(y)\), then
\[
\begin{aligned}
&|\mathrm{val}_T(\gamma,u)-\mathrm{val}_T(\gamma,u')|\\
&\qquad\le L_T\sum_j\|u_j-u_j'\|_2 .
\end{aligned}
\]
Hence the set \(S_\gamma\) of \(u\in\mathcal U(M(\gamma))^d\) with \(|\mathrm{val}_T(\gamma,u)|<\varepsilon/2\) for all \(T\in\mathcal T\) is open for the product of the \(2\)-norm topologies. It is nonempty by Lemma 2.2, applied to the II₁ factor \(M(\gamma)\), the coefficients \(f(\gamma)\) and \(\varepsilon/2\).

Enumerate the \(d\)-tuples of the fields \(v_j\) of Lemma 2.4(2) as \(v^{(1)},v^{(2)},\ldots\). Their values at \(\gamma\) are dense in \(\mathcal U(M(\gamma))^d\), so some \(v^{(k)}(\gamma)\) lies in \(S_\gamma\). Let \(E_k\) be the set of \(\gamma\) with \(v^{(k)}(\gamma)\in S_\gamma\). The value of \(T\) at the unitaries \(\int^\oplus v^{(k)}_j\) of \(M\) is an element \(x\) of \(M\) with \(x(\gamma)=\) the corresponding product in \(M(\gamma)\), so \(\mathrm{val}_T(\gamma,v^{(k)}(\gamma))=\tau_\gamma(x(\gamma))\) is \(\nu\)-measurable by Lemma 2.4(1). Hence each \(E_k\) is \(\nu\)-measurable, and after changing it by a null set we may take it Borel. The \(E_k\) cover \(\nu\)-almost every \(\gamma\).

Put \(E_k'=E_k\setminus\bigcup_{j<k}E_j\), and let \(u_i(\gamma)=v_i^{(k)}(\gamma)\) for \(\gamma\in E_k'\) and \(u_i(\gamma)=1\) outside \(\bigcup_kE_k\). Applied to a measurable section, \(u_i\) glues measurable sections along a countable measurable partition, so \(u_i\) is a measurable field (Fact 1.1(a)), and \(\int^\oplus u_i\) is a unitary of \(M\). For \(T\in\mathcal T\), the value of \(T\) at \((\int^\oplus u_i)_i\) is \(\tau(x)\) for an \(x\in M\) with \(\tau_\gamma(x(\gamma))=\mathrm{val}_T(\gamma,u(\gamma))\) almost everywhere, so its absolute value is at most \(\int|\mathrm{val}_T(\gamma,u(\gamma))|\,d\nu\le\varepsilon/2<\varepsilon\). \(\square\)

## 3. One measure for all tests

For a probability measure \(\mu\) on \(\mathcal U(M)\) with countable support, \(\mu^{*n}\) is the law of the product \(U_1\cdots U_n\) of independent unitaries \(U_1,\ldots,U_n\) with law \(\mu\). The measure is *symmetric* if \(U^{-1}\) has the same law as \(U\). All probability spaces below are countable, and probabilities are sums.

**Theorem 3.1.** Let \((M,\tau)\) be of type \(\mathrm{II}_1\) with separable predual. There are a symmetric probability measure \(\mu\) on \(\mathcal U(M)\) with countable support and integers \(n_1<n_2<\cdots\) such that:

1. the atoms of \(\mu\) include a sequence that is dense in \(\mathcal U(M)\) for the \(2\)-norm, and they generate \(M\) as a von Neumann algebra;
2. for every \(r\ge1\), every nonempty finite set \(\mathcal W\subseteq\mathbb F_r\setminus\{e\}\) and every \(\eta>0\), if \(G_1^{(\ell)},\ldots,G_r^{(\ell)}\) are independent with law \(\mu^{*n_\ell}\), then
\[
\begin{aligned}
&\Pr\Bigl(\max_{w\in\mathcal W}\bigl|\tau\bigl(w(G^{(\ell)}_1,\ldots,\\
&\qquad G^{(\ell)}_r)\bigr)\bigr|\ge\eta\Bigr)\to0
\end{aligned}
\]
as \(\ell\to\infty\).

**Proof.** *Parameters.* For \(\ell\ge1\) put
\[
\begin{gathered}
p_\ell=2^{-2^\ell},\qquad p_0=1-\sum_{\ell\ge1}p_\ell,\\
n_\ell=p_\ell^{-3/2}=2^{3\cdot2^{\ell-1}},\\
K_\ell=\ell n_\ell,\qquad d_\ell=K_\ell^4 .
\end{gathered}
\]
These are integers, \(n_\ell\) increases strictly, and \(p_0\ge2/3\) because \(p_\ell\le4^{-\ell}\). At time \(n_\ell\), \(\ell\) paths with \(K_\ell\) increments in all will be sampled. Level \(\ell\) occurs in each path with high probability, higher levels rarely, and the \(d_\ell\) labels of level \(\ell\) make a repeated label unlikely.

*Construction.* Let \((v_j)_{j\ge1}\) be a \(2\)-norm dense sequence in \(\mathcal U(M)\) (Lemma 2.3) and
\[
\mu_0=\sum_{j\ge1}2^{-j-1}\bigl(\delta_{v_j}+\delta_{v_j^{-1}}\bigr).
\]
Unitaries \(u_{\ell,1},\ldots,u_{\ell,d_\ell}\) are chosen by induction on \(\ell\ge1\). At stage \(\ell\), choose a finite set \(F_\ell=\{v_j^{\pm1}:j\le J_\ell\}\) with \(\mu_0(F_\ell)>1-K_\ell^{-2}\), and let the *alphabet* \(\mathcal A_\ell\) be the finite set consisting of \(F_\ell\) and the \(u_{j,h}^{\pm1}\) with \(j<\ell\). The tests of stage \(\ell\) are the tests over \(\mathcal A_\ell\) with \(d_\ell\) unknowns \((y,w)\) such that:

- \(y=(y_1,\ldots,y_\ell)\) consists of \(\ell\) path expressions of length \(n_\ell\);
- each \(y_i\) contains at least one letter \(U_h^{\pm1}\);
- no label occurs twice in the whole list, regardless of signs;
- \(w\) is reduced with \(1\le|w|\le\ell\).

Designating one letter \(U_h^{\pm1}\) in each \(y_i\) shows that these are tests in the sense of Definition 2.1, and there are finitely many. Proposition 2.5 with \(\varepsilon=1/\ell\) gives \(u_{\ell,1},\ldots,u_{\ell,d_\ell}\in\mathcal U(M)\) at which every test of stage \(\ell\) has value of absolute value less than \(1/\ell\). Put
\[
\begin{gathered}
\mu_\ell=\frac1{2d_\ell}\sum_{h=1}^{d_\ell}\bigl(\delta_{u_{\ell,h}}+\delta_{u_{\ell,h}^{-1}}\bigr),\\
\mu=p_0\mu_0+\sum_{\ell\ge1}p_\ell\mu_\ell .
\end{gathered}
\]
Then \(\mu\) is a symmetric probability measure with countable support.

*Sampling.* An increment is sampled in two steps: a *level* \(j\ge0\) with probability \(p_j\); at level \(0\) an atom of \(\mu_0\) with law \(\mu_0\); at level \(j\ge1\) a *label* \(h\in\{1,\ldots,d_j\}\) and a sign \(\epsilon=\pm1\), uniformly and independently, with value \(u_{j,h}^\epsilon\). The value of an increment has law \(\mu\), also when different labels give the same unitary. A *path* of length \(n\) is a sequence of \(n\) independent increments, and the product of their values has law \(\mu^{*n}\).

*Bad events.* Sample \(\ell\) independent paths of length \(n_\ell\), with \(K_\ell\) increments in all. Let \(\mathcal B_\ell\) be the event that a level above \(\ell\) occurs, or a level-\(0\) increment lies outside \(F_\ell\), or two increments have level \(\ell\) and the same label, or some path has no increment of level \(\ell\). For a fixed pair of increments, the probability of level \(\ell\) with the same label is \(p_\ell^2/d_\ell\le1/d_\ell\), and a fixed path has no increment of level \(\ell\) with probability \((1-p_\ell)^{n_\ell}\le e^{-p_\ell n_\ell}\). Union bounds give
\[
\begin{aligned}
\Pr(\mathcal B_\ell)\le{}&K_\ell\sum_{j>\ell}p_j+K_\ell\,\mu_0(\mathcal U(M)\setminus F_\ell)\\
&+\frac{K_\ell^2}{2d_\ell}+\ell\,e^{-p_\ell n_\ell}.
\end{aligned}
\]
Since \(p_{j+1}=p_j^2\) and \(p_\ell\le1/4\), \(\sum_{j>\ell}p_j\le p_\ell^2/(1-p_\ell^2)\le\frac{16}{15}p_\ell^2\). The four terms are therefore at most
\[
\begin{gathered}
\tfrac{16}{15}\,\ell\,p_\ell^{1/2},\qquad K_\ell^{-1},\\
\tfrac12K_\ell^{-2},\qquad\ell\,e^{-p_\ell^{-1/2}},
\end{gathered}
\]
and all tend to \(0\).

*Outside the bad event.* Replace every level-\(\ell\) increment, with label \(h\) and sign \(\epsilon\), by the letter \(U_h^\epsilon\), and every other increment by its value. Outside \(\mathcal B_\ell\) this turns the \(\ell\) paths into a list tested at stage \(\ell\): the other values lie in \(\mathcal A_\ell\), each path contains a letter \(U_h^{\pm1}\), and no label repeats. Evaluating at \(U_h=u_{\ell,h}\) returns the products of the paths. So outside \(\mathcal B_\ell\), the products \(G_1,\ldots,G_\ell\) of the \(\ell\) paths satisfy \(|\tau(w(G_1,\ldots,G_\ell))|<1/\ell\) for every reduced \(w\in\mathbb F_\ell\) with \(1\le|w|\le\ell\).

*Conclusion.* Let \(r\), \(\mathcal W\) and \(\eta\) be given, and let \(\ell\ge r\), \(\ell\ge\max_{w\in\mathcal W}|w|\) and \(1/\ell<\eta\). Realize \(G^{(\ell)}_1,\ldots,G^{(\ell)}_r\) as the products of the first \(r\) of \(\ell\) independent paths of length \(n_\ell\). A word of \(\mathcal W\) is a reduced word of \(\mathbb F_\ell\) in the first \(r\) generators, of length at most \(\ell\). So the event in (2) is contained in \(\mathcal B_\ell\), and its probability tends to \(0\).

*Atoms.* Each \(v_j\) has mass at least \(p_02^{-j-1}>0\). The von Neumann algebra generated by the \(v_j\) is strongly closed. Every unitary of \(M\) is a \(2\)-norm limit of a sequence of \(v_j\)'s, hence a strong limit (Exercise 4.4 of the lesson on the cohomology problem), so it lies in that algebra. Every element of \(M\) is a combination of unitaries: a self-adjoint \(x\) with \(\|x\|\le1\) is \((z+z^*)/2\) for the unitary \(z=x+i(1-x^2)^{1/2}\). So the atoms generate \(M\). \(\square\)

A \(*\)-monomial in unitaries is a group word, and the identity word has trace \(1\). So (2) says that all joint \(*\)-moments of \(G^{(\ell)}_1,\ldots,G^{(\ell)}_r\) converge in probability to those of free Haar unitaries.

**Remark 3.2.** Theorem 3.1 concerns traces of words, that is, scalar moments. It makes no assertion about operator norms of polynomials in the products. Because it is stated for finite sets of words, further conditions whose failure probabilities tend to \(0\) can be imposed at the same stage \(\ell\).

## 4. Exercises

**4.1** (easy). Show that \(n_\ell=p_\ell^{-3/2}\) is an integer, that \(p_\ell\le4^{-\ell}\), and that \(\sum_{j>\ell}p_j\le\frac{16}{15}p_\ell^2\).

**4.2** (easy). Show that the hypothesis of Lemma 1.4 cannot be dropped: give two path expressions without distinguished labels and a word \(w\ne e\) for which the trace in Lemma 1.4 equals \(1\).

**4.3** (medium). Let \((N,\tau)\) be a tracial von Neumann algebra with a central projection \(z\) such that \(0<\tau(z)<1\), and let \(t\) be a Haar unitary of \(N\). Show that \(t\) is not free from \(C^*(z)\). Explain why the proof of Proposition 2.5 passes to the fibres.

**4.4** (easy). Show that \(\mu^{*n}\) is symmetric when \(\mu\) is.

**4.5** (medium). Let \((N,\tau)\) be a tracial von Neumann algebra and \(t\) a Haar unitary free from a unital C\*-subalgebra \(D\). Show that \(\tau(d_0td_1t^{-1})=\tau(d_0)\tau(d_1)\) for \(d_0,d_1\in D\).

## 5. Solutions

**4.1.** \(p_\ell^{-3/2}=2^{\frac32 2^\ell}=2^{3\cdot2^{\ell-1}}\), an integer for \(\ell\ge1\). For \(\ell\ge1\), \(2^\ell\ge2\ell\), so \(p_\ell\le2^{-2\ell}\). Since \(p_{j+1}=p_j^2\), the tail is \(p_\ell^2+p_\ell^4+p_\ell^8+\cdots\)\(\le p_\ell^2\sum_{k\ge0}p_\ell^{2k}=p_\ell^2/(1-p_\ell^2)\), and \(p_\ell^2\le1/16\).

**4.2.** Take \(y_1=y_2=U_1\) and \(w=x_1x_2^{-1}\). The label \(1\) occurs twice, and \(w(y_1(t),y_2(t))=t_1t_1^{-1}=1\) has trace \(1\).

**4.3.** Put \(c=\tau(z)\). The elements \(z-c\) and \(t\) are centred, and \(z\) commutes with \(t\), so
\[
\begin{aligned}
&\tau\bigl((z-c)\,t\,(z-c)\,t^{-1}\bigr)\\
&=\tau\bigl((z-c)^2\bigr)=c(1-c)\ne0 .
\end{aligned}
\]
This alternating product shows that \(t\) is not free from \(C^*(z)\). A finite set \(F\) of coefficients may contain such central elements, for instance \(2z-1\), so Lemma 2.2 cannot be applied to \(M\) itself when the centre is nontrivial. In the fibres of the central decomposition the centre is trivial, and Lemma 2.2 applies there.

**4.4.** If \(U_1,\ldots,U_n\) are independent with law \(\mu\), then \((U_1\cdots U_n)^{-1}=U_n^{-1}\cdots U_1^{-1}\), and \(U_n^{-1},\ldots,U_1^{-1}\) are independent with law \(\mu\). So the inverse of the product has law \(\mu^{*n}\).

**4.5.** Write \(d_k=\tau(d_k)1+d_k^\circ\) and expand. The term \(d_0^\circ td_1^\circ t^{-1}\) is an alternating product of centred elements and has trace \(0\). The terms with \(d_1^\circ\) and the scalar \(\tau(d_0)\), and with \(d_0^\circ\) and the scalar \(\tau(d_1)\), are multiples of \(\tau(td_1^\circ t^{-1})=\tau(d_1^\circ)=0\) and of \(\tau(d_0^\circ tt^{-1})=\tau(d_0^\circ)=0\). The remaining term is \(\tau(d_0)\tau(d_1)\tau(tt^{-1})=\tau(d_0)\tau(d_1)\).

## Sources

- [OpenAI-295] OpenAI, *Vanishing of higher bounded Hochschild cohomology*, OpenAI Math Release preprint, 23 September 2026, Section 2 (the random walk). https://github.com/openai/math/tree/main/preprints/Vanishing-of-higher-bounded-Hochschild-cohomology-September-23-2026
- S. Popa, [*Free-independent sequences in type II₁ factors and related problems*](https://www.numdam.org/item/AST_1995__232__187_0/), Astérisque 232 (1995), 187–202, and [*Independence properties in subalgebras of ultraproduct II₁ factors*](https://arxiv.org/abs/1308.3982), J. Funct. Anal. 266 (2014), 5818–5846: the free independence theorem used in Lemma 2.2, proved in the course on generators of II₁ factors.
- B. Blackadar, [*Operator algebras: theory of C\*-algebras and von Neumann algebras*](https://bruceblackadar.com/Mathematics/Cycr.pdf), author's online text, Sections III.1.6 and III.5.1: the central decomposition.
