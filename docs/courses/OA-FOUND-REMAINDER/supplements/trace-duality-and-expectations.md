# Trace Hilbert spaces, commutation, comparison and expectations

*Written by Claude Opus 5.5 (Anthropic), September 2026. Self-checked by the writing AI. Original text: CC0 1.0.*

This complete chapter consists of the trace-duality, trace-Hilbert-space, tracial-commutation, trace-comparison and expectation sections with their full proofs and examples. Results are referred to by their numbers below. The tracial commutation theorem is proved here from bounded-vector duality. General Tomita theory, coupling traces and standard-form theory are not premises. Selection and route notes: GPT-6.1 Sol (OpenAI), Ultra, October 2026; new notes CC0.

## Exact prerequisites

[Traces, part A](../reader/supplements/traces-on-von-neumann-algebras-part-a-def-v-2-1-to-def-v-2-17.html), Sections 2, 3 and 7, prove the definition ideals, finite-trace projection nets, supports, sums and the semifinite part, the trace norm and the isometric dense map into the predual. The pairing \(\tau(ax)=\tau(xa)\) for \(x\in\mathfrak m_\tau,a\in M\) is equation (0.1) below wherever that original label is cited. The public predual chapter proves \(M=(M_*)^*\), with weak-star topology equal to the ultraweak topology. Tomiyama positivity and bimodularity are Theorem 8.5 of [The universal enveloping algebra](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html), with no complete-positivity strengthening assumed. Normality is order normality, equivalent to ultraweak continuity for positive maps; the same chapter proves that normal representations have von Neumann range. The Riesz representation theorem for Hilbert spaces is in [Hilbert spaces and compact operators](../../foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators.html). The finite Baire-measure representation and continuous-function density used in Theorem 3.3 are proved in Theorem 2.2, Proposition 2.3 and Proposition 3.1(4) of Haar measure on locally compact groups, with the commutative Gelfand theorem in [C-star algebras](../../foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html). The scalar multiplication commutant is [Decomposable operators and the diagonal algebra](../reader/supplements/decomposable-operators-diagonal-algebra.html), Theorem 7.1(5). No closed unbounded-operator or Mackey-topology result is used in the selected sections.

\[\tau(xy)=\tau(yx)\quad(x,y\in\mathfrak n_\tau),\qquad \tau(ax)=\tau(xa)\quad(x\in\mathfrak m_\tau,\ a\in M).\tag{0.1}\]

## 1. Integrable elements and duality

Throughout this section \(\tau\) is a faithful semifinite normal trace on \(M\).

The prerequisite lesson introduced the norm \(\|x\|_1=\tau(|x|)\) on \(\mathfrak m_\tau\) and showed that \(x\mapsto\omega_x\) is isometric with dense range in \(M_*\). Let \(L^1(M,\tau)\) be the completion of \((\mathfrak m_\tau,\|\cdot\|_1)\). The map \(x\mapsto\omega_x\) extends to an isometric isomorphism of \(L^1(M,\tau)\) onto \(M_*\), and we use it to regard every element of \(L^1(M,\tau)\) as a normal functional. For \(y\in M\) and \(x\in L^1(M,\tau)\) we write
\[
\tau(yx)=\tau(xy)=\omega_x(y).
\tag{1.1}
\]
For \(x\in\mathfrak m_\tau\) this is the old meaning, by (0.1), and \(|\tau(yx)|\le\|y\|\,\|x\|_1\).

**Theorem 1.1** (Duality). The map \(\Phi\) that sends \(y\in M\) to the functional \(x\mapsto\tau(yx)\) on \(L^1(M,\tau)\) is an isometric linear bijection of \(M\) onto the dual space \(L^1(M,\tau)^*\). It carries the \(\sigma\)-weak topology of \(M\) to the weak\(^*\) topology of \(L^1(M,\tau)^*\).

**Proof.** Let \(j:L^1(M,\tau)\to M_*\), \(j(x)=\omega_x\), be the isometric isomorphism above. The map \(y\mapsto(\omega\mapsto\omega(y))\) is an isometric isomorphism of \(M\) onto \((M_*)^*\) that carries the \(\sigma\)-weak topology to the weak\(^*\) topology (background). Composing with the transpose of \(j\), which is an isometric isomorphism of \((M_*)^*\) onto \(L^1(M,\tau)^*\) and a homeomorphism for the weak\(^*\) topologies, we get \(\Phi(y)(x)=\omega_x(y)=\tau(yx)\). \(\square\)

So \(M\) is the dual of \(L^1(M,\tau)\), and we may think of \(M\) as \(L^\infty(M,\tau)\), with the operator norm in the role of the essential supremum. The elements of \(\mathfrak m_\tau\) lie in both spaces. The next result identifies them inside \(L^1(M,\tau)\): they are the integrable elements that are also bounded.

**Proposition 1.2** (Bounded densities). For \(x\in L^1(M,\tau)\) put
\[
N_\infty(x)=\sup\{|\tau(yx)|:\ y\in\mathfrak m_\tau,\ \|y\|_1\le1\}\in[0,\infty].
\]
Then \(x\) belongs to \(\mathfrak m_\tau\) if and only if \(N_\infty(x)<\infty\), and in that case \(N_\infty(x)=\|x\|\). Equivalently: a normal functional \(\omega\) on \(M\) equals \(\omega_x\) for some \(x\in\mathfrak m_\tau\) exactly when \(\omega\) is bounded on the \(\|\cdot\|_1\)-unit ball of \(\mathfrak m_\tau\).

**Proof.** Let \(x\in\mathfrak m_\tau\). For \(y\in\mathfrak m_\tau\), (0.1) and the trace-norm inequality give \(|\tau(yx)|=|\tau(xy)|\le\|x\|\,\|y\|_1\), so \(N_\infty(x)\le\|x\|\). By Theorem 1.1, \(\|x\|\) is the norm of \(\Phi(x)\), the supremum of \(|\tau(xy)|\) over the unit ball of \(L^1(M,\tau)\); since \(\mathfrak m_\tau\) is dense there, the supremum over its unit ball is the same. So \(N_\infty(x)=\|x\|\).

Conversely, let \(C=N_\infty(x)<\infty\). The functional \(y\mapsto\tau(yx)\) on \(\mathfrak m_\tau\) has norm at most \(C\) for \(\|\cdot\|_1\), so it extends to a bounded functional on \(L^1(M,\tau)\), and Theorem 1.1 gives \(z\in M\) with \(\|z\|=C\) and \(\tau(yx)=\tau(zy)\) for all \(y\in\mathfrak m_\tau\). We show that \(z\in\mathfrak m_\tau\). Let \(z=u|z|\) be the polar decomposition, and choose projections \(e_i\in F_\tau\) that increase to \(1\) (semifiniteness). The element \(e_iu^*\) lies in \(\mathfrak m_\tau\), because \(\mathfrak m_\tau\) is an ideal containing \(e_i\). By (0.1),
\[
\tau(e_i|z|e_i)=\tau\bigl((e_iu^*)(ze_i)\bigr)=\tau\bigl(ze_i\,e_iu^*\bigr)=\tau(z\,e_iu^*)=\tau(e_iu^*\,x),
\]
and the last number is at most \(\|e_iu^*\|\,\|x\|_1\le\|x\|_1\) in absolute value. On the other hand \(e_i|z|e_i=(|z|^{1/2}e_i)^*(|z|^{1/2}e_i)\), so the trace property gives \(\tau(e_i|z|e_i)=\tau(|z|^{1/2}e_i|z|^{1/2})\), and these numbers increase to \(\tau(|z|)\) by normality. Hence \(\tau(|z|)\le\|x\|_1<\infty\), and \(z\in\mathfrak m_\tau\). Now \(\omega_z\) and \(\omega_x\) are normal and agree on \(\mathfrak m_\tau\), which is \(\sigma\)-weakly dense; so they are equal, and \(x=z\) in \(L^1(M,\tau)\). \(\square\)

**Example 1.3** (\(B(H)\) and the trace class). Let \(M=B(H)\) and let \(\tau=\operatorname{Tr}\) be the usual trace, \(\operatorname{Tr}(x)=\sum_i\langle x\varepsilon_i,\varepsilon_i\rangle\) for an orthonormal basis. For a unit vector \(\xi\) and any unit vector \(\eta\), the rank-one operator \(r=\langle\,\cdot\,,\xi\rangle\eta\) has norm \(1\), and for \(y\in\mathfrak m_{\operatorname{Tr}}\) the linear extension of the trace gives \(\operatorname{Tr}(yr)=\langle y\eta,\xi\rangle\). The trace-norm inequality gives \(|\langle y\eta,\xi\rangle|\le\|y\|_1\), so
\[
\|y\|\le\|y\|_1\qquad(y\in\mathfrak m_{\operatorname{Tr}}).
\]
Consequently, for \(x\in L^1(B(H),\operatorname{Tr})\) and \(y\in\mathfrak m_{\operatorname{Tr}}\) with \(\|y\|_1\le1\), \(|\operatorname{Tr}(yx)|\le\|y\|\,\|x\|_1\le\|x\|_1\). So \(N_\infty(x)\le\|x\|_1<\infty\) for every \(x\), and Proposition 1.2 shows that \(L^1(B(H),\operatorname{Tr})=\mathfrak m_{\operatorname{Tr}}\): no completion is needed. These are the trace-class operators, and Theorem 1.1 is the classical statement that \(B(H)\) is the dual of the trace class. In contrast, for a diffuse algebra such as \(L^\infty[0,1]\) the completion adds unbounded elements (Example 1.4).

**Example 1.4** (Measure spaces). Let \((X_k,\mu_k)_{k\in K}\) be finite measure spaces and let \((X,\mu)\) be their disjoint union: a function on \(X\) is measurable when its restriction to each \(X_k\) is, and \(\int_Xf\,d\mu=\sum_k\int_{X_k}f\,d\mu_k\) for \(f\ge0\). Put \(L^p(X,\mu)=\{f:\|f\|_p<\infty\}\) modulo null functions, for \(p=1,2\), and let \(L^\infty(X,\mu)\) be the bounded families \((f_k)\) with \(f_k\in L^\infty(X_k,\mu_k)\). Every \(\sigma\)-finite measure space has this form, with \(K\) countable.

Let \(M=L^\infty(X,\mu)\) act on \(L^2(X,\mu)=\bigoplus_kL^2(X_k,\mu_k)\) by multiplication. Each summand is a maximal abelian von Neumann algebra on \(L^2(X_k,\mu_k)\) (background), so \(M\) is a von Neumann algebra, the direct sum of these. Put \(\tau(f)=\int_Xf\,d\mu\) for \(f\in M_+\). Then:

- \(\tau\) is a trace, since \(M\) is commutative. It is faithful. It is normal: \(\tau(f)=\sum_k\langle f1_{X_k},1_{X_k}\rangle\) is a sum of vector functionals. It is semifinite: the projections \(\sum_{k\in F}1_{X_k}\), \(F\) finite, have finite trace and increase to \(1\).
- \(F_\tau\) consists of the bounded integrable functions \(f\ge0\), so \(\mathfrak m_\tau=L^\infty\cap L^1\), and \(\|f\|_1=\int|f|\,d\mu\) is the \(L^1\)-norm. Likewise \(\mathfrak n_\tau=L^\infty\cap L^2\) with the \(L^2\)-norm.
- \(L^\infty\cap L^1\) is dense in \(L^1(X,\mu)\): for \(f\in L^1\), the functions \(f\,1_{\{|f|\le n\}}\sum_{k\in F}1_{X_k}\) converge to \(f\) in \(L^1\) by dominated convergence, along \(n\to\infty\) and finite sets \(F\) increasing to \(K\). As \(L^1(X,\mu)\) is complete, \(L^1(M,\tau)=L^1(X,\mu)\), and the pairing (1.1) is \(\tau(gf)=\int_Xgf\,d\mu\).

Theorem 1.1 now says that \(L^\infty(X,\mu)\) is the dual of \(L^1(X,\mu)\) through \(g\mapsto(f\mapsto\int gf\,d\mu)\), and Proposition 1.2 says that an integrable \(f\) is essentially bounded exactly when \(g\mapsto\int gf\,d\mu\) is bounded on the unit ball of \(L^\infty\cap L^1\) for the \(L^1\)-norm, with bound \(\|f\|_\infty\). By Theorem 3.3, every commutative von Neumann algebra that carries a faithful semifinite normal trace is of this form.

**Remark 1.5.** Faithfulness is used to make \(\|\cdot\|_1\) a norm. If \(\tau\) is only semifinite and normal, \(\|\cdot\|_1\) vanishes exactly on \(\mathfrak m_\tau(1-s(\tau))=\mathfrak m_\tau\cap M(1-s(\tau))\), and the same results hold for the algebra \(Ms(\tau)\), whose predual is the set of normal functionals on \(M\) that vanish on \(M(1-s(\tau))\).

## 2. The Hilbert space of a trace

Throughout this section \(\tau\) is a faithful semifinite normal trace on \(M\). A reference for Sections 1–3 is [Kostecki, Section 5.2].

**Definition 2.1.** For \(x,y\in\mathfrak n_\tau\) put \(\langle x,y\rangle_2=\tau(y^*x)\); this makes sense because \(y^*x\in\mathfrak m_\tau\). It is a sesquilinear form, positive, and definite because \(\tau\) is faithful: \(\langle x,x\rangle_2=\tau(x^*x)=0\) forces \(x=0\). The completion of \(\mathfrak n_\tau\) is a Hilbert space \(L^2(M,\tau)\), and \(\mathfrak n_\tau\) is a dense subspace of it. The norm is \(\|x\|_2\).

**Lemma 2.2** (The two actions). Let \(a\in M\) and \(x\in\mathfrak n_\tau\).

1. \(\|ax\|_2\le\|a\|\,\|x\|_2\), \(\|xa\|_2\le\|a\|\,\|x\|_2\) and \(\|x^*\|_2=\|x\|_2\).
2. There are bounded operators \(\pi_\tau(a)\) and \(\rho_\tau(a)\) on \(L^2(M,\tau)\) with \(\pi_\tau(a)x=ax\) and \(\rho_\tau(a)x=xa\). The map \(\pi_\tau\) is a unital \(*\)-homomorphism. The map \(\rho_\tau\) is linear and unital, with \(\rho_\tau(ab)=\rho_\tau(b)\rho_\tau(a)\) and \(\rho_\tau(a^*)=\rho_\tau(a)^*\). Every \(\pi_\tau(a)\) commutes with every \(\rho_\tau(b)\).
3. The map \(x\mapsto x^*\) extends to a conjugate-linear isometry \(J\) of \(L^2(M,\tau)\) with \(J^2=1\), \(\langle J\xi,J\eta\rangle_2=\langle\eta,\xi\rangle_2\), and \(J\pi_\tau(a)J=\rho_\tau(a^*)\).
4. For \(x,y\in\mathfrak n_\tau\), \(\langle\pi_\tau(a)x,y\rangle_2=\tau(a\,xy^*)=\omega_{xy^*}(a)\). The maps \(\pi_\tau\) and \(\rho_\tau\) are injective and normal, in the sense that \(a\mapsto\langle\pi_\tau(a)\xi,\eta\rangle_2\) and \(a\mapsto\langle\rho_\tau(a)\xi,\eta\rangle_2\) lie in \(M_*\) for all vectors \(\xi,\eta\).
5. \(\mathfrak m_\tau\) is dense in \(L^2(M,\tau)\). If \(e_i\in F_\tau\) are projections that increase to \(1\), then \(\pi_\tau(e_i)\to1\) and \(\rho_\tau(e_i)\to1\) strongly.

We call \(\pi_\tau\) the *standard representation* of \(M\) defined by \(\tau\), \(\rho_\tau\) the *right representation* and \(J\) the *conjugation*. When no confusion arises we write \(\pi,\rho\).

**Proof.** (1) Since \(x^*a^*ax\le\|a\|^2x^*x\), monotonicity of \(\tau\) gives the first inequality. By the trace identity for \(z=xa\), \(\tau(a^*x^*xa)=\tau(xaa^*x^*)\le\|a\|^2\tau(xx^*)=\|a\|^2\tau(x^*x)\). Finally \(\tau(xx^*)=\tau(x^*x)\).

(2) By (1), left and right multiplication by \(a\) are bounded on \(\mathfrak n_\tau\) for \(\|\cdot\|_2\), with norm at most \(\|a\|\), and extend to \(L^2(M,\tau)\). The algebraic rules hold on \(\mathfrak n_\tau\) and pass to the closure. For adjoints, let \(x,y\in\mathfrak n_\tau\). Then \(\langle ax,y\rangle_2=\tau(y^*ax)=\tau((a^*y)^*x)=\langle x,a^*y\rangle_2\). Also \(\langle xa,y\rangle_2=\tau(y^*x\,a)=\tau(a\,y^*x)\) by (0.1), since \(y^*x\in\mathfrak m_\tau\), and \(\tau(a\,y^*x)=\tau((ya^*)^*x)=\langle x,ya^*\rangle_2\). The commutation is associativity: \((ax)b=a(xb)\).

(3) By (1), \(J\) is isometric on \(\mathfrak n_\tau\), so it extends; \(J^2=1\) is clear. For \(x,y\in\mathfrak n_\tau\), \(\langle x^*,y^*\rangle_2=\tau(yx^*)=\tau(x^*y)=\langle y,x\rangle_2\) by (0.1), and this passes to limits. Finally \(J\pi_\tau(a)Jx=(ax^*)^*=xa^*=\rho_\tau(a^*)x\).

(4) By (0.1) with the elements \(y^*\) and \(ax\) of \(\mathfrak n_\tau\), \(\tau(y^*\,ax)=\tau(ax\,y^*)\), and \(xy^*\in\mathfrak m_\tau\). So \(a\mapsto\langle\pi_\tau(a)x,y\rangle_2\) is \(\omega_{xy^*}\), which is normal. For arbitrary vectors \(\xi,\eta\), approximate them by \(x,y\in\mathfrak n_\tau\); the functionals converge in norm, and \(M_*\) is norm closed. For \(\rho_\tau\), part (3) gives \(\langle\rho_\tau(a)\xi,\eta\rangle_2=\langle J\pi_\tau(a^*)J\xi,\eta\rangle_2=\langle\pi_\tau(a)J\eta,J\xi\rangle_2\), which is normal in \(a\). If \(\pi_\tau(a)=0\), then \(ae_i=\pi_\tau(a)e_i=0\) for projections \(e_i\in F_\tau\) increasing to \(1\), so \(a=0\); and \(\rho_\tau(a)=J\pi_\tau(a^*)J\).

(5) For \(y\in\mathfrak n_\tau\), \(e_iy\in\mathfrak m_\tau\), and \(\|y-e_iy\|_2^2=\tau(y^*(1-e_i)y)=\tau(y^*y)-\tau(y^*e_iy)\to0\) because \(y^*e_iy\uparrow y^*y\) and \(\tau\) is normal. So \(\mathfrak m_\tau\) is dense, and \(\pi_\tau(e_i)\to1\) on the dense set \(\mathfrak n_\tau\); being contractions, they converge strongly. Then \(\rho_\tau(e_i)=J\pi_\tau(e_i)J\to1\) strongly. \(\square\)

The next two results decide when a vector of \(L^2(M,\tau)\), or an element of \(M\), comes from \(\mathfrak n_\tau\). They are the Hilbert-space analogues of Proposition 1.2.

**Proposition 2.3** (Square-integrable elements). For \(x\in M\) put
\[
N_2(x)=\sup\{|\tau(y^*x)|:\ y\in\mathfrak m_\tau,\ \|y\|_2\le1\}\in[0,\infty].
\]
Then \(x\in\mathfrak n_\tau\) if and only if \(N_2(x)<\infty\), and then \(N_2(x)=\|x\|_2\).

**Proof.** The number \(\tau(y^*x)\) is defined because \(\mathfrak m_\tau\) is an ideal. If \(x\in\mathfrak n_\tau\), then \(\tau(y^*x)=\langle x,y\rangle_2\), so \(N_2(x)\le\|x\|_2\) by Cauchy–Schwarz, and equality holds because \(\mathfrak m_\tau\) is dense in \(L^2(M,\tau)\).

Conversely let \(N_2(x)<\infty\). The map \(y\mapsto\overline{\tau(y^*x)}\) is linear and bounded on the dense subspace \(\mathfrak m_\tau\), so the Riesz representation theorem gives \(\xi\in L^2(M,\tau)\) with \(\tau(y^*x)=\langle\xi,y\rangle_2\) for all \(y\in\mathfrak m_\tau\). Let \(e_i\in F_\tau\) be projections increasing to \(1\). For \(y\in\mathfrak m_\tau\),
\[
\langle e_ix,y\rangle_2=\tau(y^*e_ix)=\tau((e_iy)^*x)=\langle\xi,e_iy\rangle_2=\langle\pi_\tau(e_i)\xi,y\rangle_2 ,
\]
where \(e_ix\in\mathfrak m_\tau\). By density, \(e_ix=\pi_\tau(e_i)\xi\) in \(L^2(M,\tau)\). Hence \(\tau(x^*e_ix)=\|e_ix\|_2^2\le\|\xi\|_2^2\). As \(x^*e_ix\uparrow x^*x\), normality gives \(\tau(x^*x)\le\|\xi\|_2^2<\infty\). \(\square\)

**Proposition 2.4** (Bounded vectors). For \(\xi\in L^2(M,\tau)\) the following are equivalent:

- (i) \(\xi\in\mathfrak n_\tau\);
- (ii) \(N_\infty(\xi)=\sup\{|\langle\xi,y\rangle_2|:\ y\in\mathfrak m_\tau,\ \|y\|_1\le1\}<\infty\);
- (iii) \(N_\ell(\xi)=\sup\{\|\pi_\tau(a)\xi\|_2:\ a\in\mathfrak n_\tau,\ \|a\|_2\le1\}<\infty\);
- (iv) \(N_r(\xi)=\sup\{\|\rho_\tau(a)\xi\|_2:\ a\in\mathfrak n_\tau,\ \|a\|_2\le1\}<\infty\).

When they hold, and \(\xi=x\in\mathfrak n_\tau\), all three suprema equal the operator norm \(\|x\|\).

**Proof.** (i)\(\Rightarrow\)(iii): for \(a\in\mathfrak n_\tau\), \(\pi_\tau(a)x=ax=\rho_\tau(x)a\), so \(\|ax\|_2\le\|x\|\,\|a\|_2\) by Lemma 2.2(1). Thus \(N_\ell(x)\le\|x\|\).

(iii)\(\Rightarrow\)(ii): let \(y\in\mathfrak m_\tau\) with polar decomposition \(y=u|y|\). Then \(k=|y^*|=u|y|u^*\) satisfies \(ku=u|y|=y\), and \(k\in F_\tau\), so \(k^{1/2}\in\mathfrak n_\tau\) with \(\|k^{1/2}\|_2^2=\tau(k)=\tau(|y|)=\|y\|_1\). Write \(y=k^{1/2}(k^{1/2}u)\). As \(\pi_\tau(k^{1/2})\) is self-adjoint,
\[
|\langle\xi,y\rangle_2|=|\langle\pi_\tau(k^{1/2})\xi,\,k^{1/2}u\rangle_2|\le\|\pi_\tau(k^{1/2})\xi\|_2\,\|k^{1/2}u\|_2\le N_\ell(\xi)\,\|k^{1/2}\|_2\cdot\|k^{1/2}\|_2=N_\ell(\xi)\,\|y\|_1 ,
\]
using Lemma 2.2(1) for \(\|k^{1/2}u\|_2\le\|k^{1/2}\|_2\). So \(N_\infty(\xi)\le N_\ell(\xi)\).

(ii)\(\Rightarrow\)(i): the map \(w\mapsto\langle\xi,w^*\rangle_2\) is linear on \(\mathfrak m_\tau\) and bounded for \(\|\cdot\|_1\), since \(\|w^*\|_1=\|w\|_1\). By Theorem 1.1 there is \(x'\in M\) with \(\|x'\|=N_\infty(\xi)\) and \(\langle\xi,w^*\rangle_2=\tau(wx')\) for \(w\in\mathfrak m_\tau\); with \(w=y^*\) this reads \(\langle\xi,y\rangle_2=\tau(y^*x')\). Let \(e_i\in F_\tau\) be projections increasing to \(1\). For \(y\in\mathfrak m_\tau\),
\[
\langle e_ix',y\rangle_2=\tau(y^*e_ix')=\tau((e_iy)^*x')=\langle\xi,e_iy\rangle_2=\langle\pi_\tau(e_i)\xi,y\rangle_2 ,
\]
so \(e_ix'=\pi_\tau(e_i)\xi\). Then \(\tau(x'^*e_ix')=\|\pi_\tau(e_i)\xi\|_2^2\le\|\xi\|_2^2\), and normality gives \(\tau(x'^*x')\le\|\xi\|_2^2\): so \(x'\in\mathfrak n_\tau\). Finally \(\pi_\tau(e_i)\xi\to\xi\) and \(e_ix'\to x'\) in \(L^2(M,\tau)\) (Lemma 2.2(5)), so \(\xi=x'\).

Norms: for \(x\in\mathfrak n_\tau\), \(N_\infty(x)=\sup\{|\tau(wx)|:w\in\mathfrak m_\tau,\|w\|_1\le1\}\), which is \(\|x\|\) by Theorem 1.1 and density. With the inequalities above, \(\|x\|=N_\infty(x)\le N_\ell(x)\le\|x\|\).

(i)\(\Leftrightarrow\)(iv): \(J\) is isometric, maps \(\mathfrak n_\tau\) onto itself, and \(\|\rho_\tau(a)\xi\|_2=\|J\rho_\tau(a)\xi\|_2=\|\pi_\tau(a^*)J\xi\|_2\) by Lemma 2.2(3). As \(a\mapsto a^*\) preserves \(\mathfrak n_\tau\) and \(\|\cdot\|_2\), \(N_r(\xi)=N_\ell(J\xi)\), and \(\|x^*\|=\|x\|\). \(\square\)

**Example 2.5.** (a) *\(B(H)\).* By Example 1.3, \(\|y\|\le\|y\|_1\) for \(y\in\mathfrak m_{\operatorname{Tr}}\). For \(x\in\mathfrak n_{\operatorname{Tr}}\) this gives \(\|x\|^2=\|x^*x\|\le\|x^*x\|_1=\|x\|_2^2\). Let \(\xi\in L^2(B(H),\operatorname{Tr})\) be the limit of \(x_n\in\mathfrak n_{\operatorname{Tr}}\). For \(a\in\mathfrak n_{\operatorname{Tr}}\), \(\|\pi(a)\xi\|_2=\lim_n\|ax_n\|_2\le\|a\|\,\|\xi\|_2\le\|a\|_2\|\xi\|_2\). So \(N_\ell(\xi)\le\|\xi\|_2\), and \(\xi\in\mathfrak n_{\operatorname{Tr}}\) by Proposition 2.4. Every vector is bounded: \(L^2(B(H),\operatorname{Tr})\) is the space of Hilbert–Schmidt operators, with \(\|x\|\le\|x\|_2\).

(b) *\(L^\infty[0,1]\).* With Lebesgue measure, \(L^2(M,\tau)=L^2[0,1]\) by Example 1.4, and for \(f\in L^2\), \(N_\ell(f)=\sup\{\|gf\|_2:\ g\in L^\infty,\ \|g\|_2\le1\}\). For \(f(t)=t^{-1/4}\) and \(g=\delta^{-1/2}1_{[0,\delta]}\), \(\|gf\|_2^2=\delta^{-1}\int_0^\delta t^{-1/2}\,dt=2\delta^{-1/2}\to\infty\). So \(f\) is not a bounded vector, although it lies in \(L^2\). Here the bounded vectors are exactly the essentially bounded functions, and Proposition 2.4 recovers \(\|f\|_\infty=\sup\{\|gf\|_2:\|g\|_2\le1\}\).

## 3. The commutation theorem

**Theorem 3.1** (The commutation theorem). Let \(\tau\) be a faithful semifinite normal trace on \(M\). Then \(\pi_\tau(M)\) and \(\rho_\tau(M)\) are von Neumann algebras on \(L^2(M,\tau)\),
\[
\pi_\tau(M)'=\rho_\tau(M),\qquad \rho_\tau(M)'=\pi_\tau(M),\qquad J\pi_\tau(M)J=\rho_\tau(M).
\tag{3.1}
\]
\(\pi_\tau\) is a normal \(*\)-isomorphism of \(M\) onto \(\pi_\tau(M)\), and \(\rho_\tau\) is a normal anti-isomorphism of \(M\) onto \(\rho_\tau(M)\). The center of \(\pi_\tau(M)\) is \(\pi_\tau(Z)=\rho_\tau(Z)\).

**Proof.** By Lemma 2.2, \(\pi_\tau\) is a faithful normal representation, so its image is a von Neumann algebra (background), and \(\pi_\tau\) is an isomorphism onto it. Since \(J\) is a conjugate-linear isometry with \(J^2=1\), the map \(X\mapsto JXJ\) preserves products, adjoints and strong limits. By Lemma 2.2(3), \(\rho_\tau(M)=J\pi_\tau(M)J\); so \(\rho_\tau(M)\) is strongly closed, contains \(1\) and is closed under adjoints: a von Neumann algebra.

By Lemma 2.2(2), \(\rho_\tau(M)\subseteq\pi_\tau(M)'\). For the converse, let \(b\in\pi_\tau(M)'\) and \(x\in\mathfrak n_\tau\). Consider the vector \(\xi=bx\). For \(a\in\mathfrak n_\tau\),
\[
\|\pi_\tau(a)\xi\|_2=\|b\,\pi_\tau(a)x\|_2=\|b(ax)\|_2\le\|b\|\,\|ax\|_2\le\|b\|\,\|x\|\,\|a\|_2 .
\]
So \(N_\ell(\xi)\le\|b\|\|x\|\), and Proposition 2.4 gives an element \(w\in\mathfrak n_\tau\) with \(bx=w\). For \(a\in\mathfrak n_\tau\),
\[
\rho_\tau(w)a=aw=\pi_\tau(a)bx=b\,\pi_\tau(a)x=b(ax)=b\,\rho_\tau(x)a .
\]
Both \(\rho_\tau(w)\) and \(b\rho_\tau(x)\) are bounded and agree on the dense set \(\mathfrak n_\tau\), so \(b\rho_\tau(x)=\rho_\tau(w)\in\rho_\tau(M)\). Now let \(e_i\in F_\tau\) be projections increasing to \(1\); they lie in \(\mathfrak n_\tau\). By Lemma 2.2(5), \(b\rho_\tau(e_i)\to b\) strongly, and \(\rho_\tau(M)\) is strongly closed; so \(b\in\rho_\tau(M)\). This proves \(\pi_\tau(M)'=\rho_\tau(M)\), and then \(\rho_\tau(M)'=\pi_\tau(M)''=\pi_\tau(M)\) by the bicommutant theorem.

\(\rho_\tau\) is injective and normal by Lemma 2.2(4), and it reverses products. For \(a\in Z\) and \(x\in\mathfrak n_\tau\), \(ax=xa\), so \(\pi_\tau(a)=\rho_\tau(a)\). The center of \(\pi_\tau(M)\) is \(\pi_\tau(M)\cap\pi_\tau(M)'=\pi_\tau(M)\cap\rho_\tau(M)\), and \(\pi_\tau\) maps \(Z\) onto the center of \(\pi_\tau(M)\) because it is an isomorphism. \(\square\)

When \(\tau(1)<\infty\), the vector \(1\in\mathfrak n_\tau\) is cyclic for \(\pi_\tau(M)\) and for \(\rho_\tau(M)\), since \(\pi_\tau(x)1=x=\rho_\tau(x)1\); by (3.1) it is then also separating for both.

**Example 3.2** (Matrices). Let \(M=M_n(\mathbb C)\) and \(\tau=\operatorname{Tr}\). Then \(L^2(M,\tau)\) is \(M_n(\mathbb C)\) with \(\langle x,y\rangle_2=\operatorname{Tr}(y^*x)\), \(\pi\) and \(\rho\) are left and right multiplication, and \(J\) is the adjoint. Theorem 3.1 is here elementary: if a linear map \(T\) of \(M_n(\mathbb C)\) commutes with every left multiplication, then \(T(x)=T(x\cdot1)=xT(1)\), so \(T=\rho(T(1))\).

**Theorem 3.3** (Commutative algebras). Let \(A\) be a commutative von Neumann algebra carrying a faithful semifinite normal trace \(\tau\).

1. \(\pi_\tau(A)\) is maximal abelian on \(L^2(A,\tau)\): \(\pi_\tau(A)'=\pi_\tau(A)\).
2. There are compact Hausdorff spaces \(\Omega_k\) (\(k\in K\)) with finite positive Baire measures \(\mu_k\), and a \(*\)-isomorphism \(\Phi\) of \(A\) onto the algebra \(L^\infty(X,\mu)\) of the disjoint union \((X,\mu)\) of the \((\Omega_k,\mu_k)\), as in Example 1.4, such that \(\tau(a)=\int_X\Phi(a)\,d\mu\) for \(a\in A_+\).

Consequently, by Example 1.4, \(\mathfrak m_\tau\), \(\mathfrak n_\tau\), \(L^1(A,\tau)\) and \(L^2(A,\tau)\) correspond to \(L^\infty\cap L^1\), \(L^\infty\cap L^2\), \(L^1(X,\mu)\) and \(L^2(X,\mu)\). The space \(X\) is locally compact, each \(\Omega_k\) being open and compact in it, and \(\mu\) is finite on compact sets.

**Proof.** (1) For \(a\in A\) and \(x\in\mathfrak n_\tau\), \(ax=xa\), so \(\pi_\tau(a)=\rho_\tau(a)\). By Theorem 3.1, \(\pi_\tau(A)'=\rho_\tau(A)=\pi_\tau(A)\).

(2) By Zorn's lemma choose a maximal family \((e_k)_{k\in K}\) of mutually orthogonal nonzero projections of finite trace. Its sum is \(1\): otherwise the remainder would majorize a nonzero projection of finite trace (semifiniteness). The algebra \(A_k=Ae_k\), acting on \(e_kH\), is a commutative von Neumann algebra with unit \(e_k\), and \(\tau_k=\tau|_{A_k}\) is a faithful normal finite trace on it.

Fix \(k\). By the Gelfand–Naimark theorem there is an isometric \(*\)-isomorphism \(\Gamma_k:A_k\to C(\Omega_k)\) onto the continuous functions on a compact Hausdorff space. By the Riesz–Markov theorem there is a finite positive Baire measure \(\mu_k\) on \(\Omega_k\) with \(\tau_k(a)=\int\Gamma_k(a)\,d\mu_k\). The continuous functions are dense in \(L^2(\Omega_k,\mu_k)\): given \(g\in L^2\), the truncations \(g1_{\{|g|\le n\}}\) converge to \(g\) in \(L^2\); if \(|g|\le n\), choose continuous \(f_m\to g\) in \(L^1\) and replace \(f_m\) by \(\tilde f_m=f_m\min(1,n/|f_m|)\), which is continuous with \(|\tilde f_m-g|\le|f_m-g|\) (the map \(z\mapsto z\min(1,n/|z|)\) is a 1-Lipschitz retraction onto the disc of radius \(n\), which contains the values of \(g\)); then \(\|\tilde f_m-g\|_2^2\le2n\|\tilde f_m-g\|_1\to0\).

Since \(\tau_k\) is finite, \(\mathfrak n_{\tau_k}=A_k\), and \(\|a\|_2^2=\tau_k(a^*a)=\int|\Gamma_k(a)|^2\,d\mu_k\). So \(a\mapsto\Gamma_k(a)\) extends to a unitary \(U_k\) of \(L^2(A_k,\tau_k)\) onto \(L^2(\Omega_k,\mu_k)\), and \(U_k\pi_{\tau_k}(a)U_k^*\) is multiplication by \(\Gamma_k(a)\), because both agree on the dense set of continuous functions. By part (1) applied to \((A_k,\tau_k)\), the set \(\mathcal R=\{M_{\Gamma_k(a)}:a\in A_k\}\) of these multiplication operators is maximal abelian. It lies in the commutative set of all multiplications \(M_g\), \(g\in L^\infty(\Omega_k,\mu_k)\); a commutative set containing a maximal abelian algebra equals it. So every \(M_g\) equals some \(M_{\Gamma_k(a)}\), and then \(g=\Gamma_k(a)\) almost everywhere (apply both to the vector \(1\)). Hence \(\Phi_k(a)=\Gamma_k(a)\) (as a class in \(L^\infty\)) is a \(*\)-homomorphism of \(A_k\) onto \(L^\infty(\Omega_k,\mu_k)\). It is injective: if \(\Gamma_k(a)=0\) almost everywhere, then \(\tau_k(a^*a)=0\) and \(a=0\). And \(\tau_k(a)=\int\Phi_k(a)\,d\mu_k\).

Finally \(a\mapsto(ae_k)_k\) is a \(*\)-isomorphism of \(A\) onto the bounded families \((a_k)\) with \(a_k\in A_k\): a bounded family has the strong sum \(\sum_ka_k\in A\). Put \(\Phi(a)=(\Phi_k(ae_k))_k\in L^\infty(X,\mu)\). For \(a\in A_+\), the partial sums of \(\sum_ka^{1/2}e_ka^{1/2}\) increase to \(a\), so normality gives \(\tau(a)=\sum_k\tau_k(ae_k)=\int_X\Phi(a)\,d\mu\). The statements about \(X\) are clear from the definition of the disjoint union. \(\square\)

So the commutation theorem is the noncommutative form of the statement that \(L^\infty\) is maximal abelian on \(L^2\).

## 7. Comparing two traces

We first describe all normal traces through functionals. This is used in Section 8.

**Proposition 7.1** (Normal traces as sums of functionals). For a trace \(\tau\) on \(M\) the following are equivalent:

- (a) \(\tau\) is normal;
- (b) there are normal positive functionals \(\varphi_i\) with \(\tau(x)=\sum_i\varphi_i(x)\) for \(x\in M_+\);
- (c) \(\tau\) is lower semicontinuous on \(M_+\) for the \(\sigma\)-weak topology.

If \(\tau\) is normal and semifinite, one can take \(\varphi_i(x)=\tau(e_ixe_i)\) for mutually orthogonal projections \(e_i\) of finite trace with \(\sum_ie_i=1\).

**Proof.** (a)\(\Rightarrow\)(b). Let \(z\) be the central projection of the semifinite part of \(\tau\) (background). As in (b) of Theorem 6.3, there are mutually orthogonal projections \(e_i\le z\) of finite trace with \(\sum_ie_i=z\). For \(x\in M_+\), normality and the trace identity for \(e_ix^{1/2}\) give
\[
\tau(xz)=\tau(x^{1/2}zx^{1/2})=\sum_i\tau(x^{1/2}e_ix^{1/2})=\sum_i\tau(e_ixe_i).
\]
Since \(e_i\in\mathfrak m_\tau\), \(\varphi_i(x)=\tau(e_ixe_i)=\tau(xe_i)=\omega_{e_i}(x)\) defines a normal positive functional (background on the trace norm). If \(1-z\ne0\), use Zorn's lemma to choose normal states \(\omega_j\) whose supports \(s_j\) are mutually orthogonal and lie below \(1-z\), with the family maximal for these properties. Their supports add up to \(1-z\): otherwise a vector state at a unit vector in the range of the remainder would have its support there, against maximality. For \(x\in M_+\), \(\omega_j(x)=0\) for all \(j\) exactly when \(s_jxs_j=0\) for all \(j\), that is, when \(x^{1/2}(1-z)=0\). So the family consisting of countably many copies of each \(\omega_j\) has sum \(\infty\) at \(x\) when \(x(1-z)\ne0\), and \(0\) otherwise; that is exactly \(\tau(x(1-z))\). Together, the two families consist of normal positive functionals whose sum at \(x\) is \(\tau(xz)+\tau(x(1-z))=\tau(x)\).

(b)\(\Rightarrow\)(c): each finite partial sum is \(\sigma\)-weakly continuous, and a supremum of continuous functions is lower semicontinuous.

(c)\(\Rightarrow\)(a): if \(x_i\uparrow x\), then \(x_i\to x\) \(\sigma\)-weakly, so \(\tau(x)\le\liminf_i\tau(x_i)=\sup_i\tau(x_i)\le\tau(x)\). \(\square\)

A finite trace that is not normal, such as a limit along a free ultrafilter on \(\ell^\infty(\mathbb N)\), is therefore not \(\sigma\)-weakly lower semicontinuous.

The main result of this section compares two traces. It is a Radon–Nikodym theorem, and its density is central.

**Theorem 7.2** (Comparing two traces). Let \(\tau\) be a faithful semifinite normal trace and \(\tau'\) a semifinite normal trace on \(M\). Then \(\tau_0=\tau+\tau'\) is a faithful semifinite normal trace, and there is a unique central element \(a\) with \(0\le a\le1\) such that
\[
\tau(x)=\tau_0(ax),\qquad \tau'(x)=\tau_0((1-a)x)\qquad(x\in M_+).
\tag{7.1}
\]
Moreover \(s(a)=1\) and \(s(1-a)=s(\tau')\).

**Proof.** \(\tau_0\) is normal and semifinite (background on sums), and faithful because \(\tau\) is. Note that \(\mathfrak n_{\tau_0}=\mathfrak n_\tau\cap\mathfrak n_{\tau'}\). For \(x,y\in\mathfrak n_{\tau_0}\), the Cauchy–Schwarz inequality for the positive form \((x,y)\mapsto\tau(y^*x)\) gives
\[
|\tau(y^*x)|^2\le\tau(x^*x)\tau(y^*y)\le\tau_0(x^*x)\tau_0(y^*y)=\|x\|_{2,\tau_0}^2\|y\|_{2,\tau_0}^2 .
\]
So there is a unique operator \(A\) on \(L^2(M,\tau_0)\) with \(\langle Ax,y\rangle_2=\tau(y^*x)\) for \(x,y\in\mathfrak n_{\tau_0}\), and \(0\le A\le1\). Let \(u\in M\) be unitary. For \(x,y\in\mathfrak n_{\tau_0}\),
\[
\langle A\pi_{\tau_0}(u)x,y\rangle_2=\tau(y^*ux)=\tau((u^*y)^*x)=\langle Ax,u^*y\rangle_2=\langle\pi_{\tau_0}(u)Ax,y\rangle_2 ,
\]
and, using (0.1) with \(y^*x\in\mathfrak m_\tau\),
\[
\langle A\rho_{\tau_0}(u)x,y\rangle_2=\tau(y^*xu)=\tau(uy^*x)=\tau((yu^*)^*x)=\langle Ax,\rho_{\tau_0}(u^*)y\rangle_2=\langle\rho_{\tau_0}(u)Ax,y\rangle_2 .
\]
Every element of \(M\) is a combination of unitaries, so \(A\) commutes with \(\pi_{\tau_0}(M)\) and with \(\rho_{\tau_0}(M)\). By Theorem 3.1, \(A\in\rho_{\tau_0}(M)\cap\pi_{\tau_0}(M)\), the center of \(\pi_{\tau_0}(M)\), which is \(\pi_{\tau_0}(Z)\). So \(A=\pi_{\tau_0}(a)\) for a central \(a\), with \(0\le a\le1\) because \(\pi_{\tau_0}\) is an order isomorphism onto its image. Then \(\tau(y^*x)=\tau_0(y^*ax)\) for \(x,y\in\mathfrak n_{\tau_0}\), and for \(x\in F_{\tau_0}\), taking \(x^{1/2}\) for both vectors, \(\tau(x)=\tau_0(ax)\). For general \(x\in M_+\), let \(e_i\in F_{\tau_0}\) be projections increasing to \(1\); then \(x_i=x^{1/2}e_ix^{1/2}\in F_{\tau_0}\) increase to \(x\), and normality of \(\tau\) and of \(\tau_0(a\,\cdot\,)\) gives \(\tau(x)=\tau_0(ax)\). For \(x\in F_{\tau_0}\), \(\tau'(x)=\tau_0(x)-\tau(x)=\tau_0((1-a)x)\), and the same limit argument extends this to \(M_+\).

If \(q=1-s(a)\), then \(\tau(q)=\tau_0(aq)=0\), so \(q=0\). A central projection \(q\) has \(\tau'(q)=\tau_0((1-a)q)=0\) exactly when \((1-a)q=0\), because \(\tau_0\) is faithful. The largest such \(q\) is \(1-s(1-a)\), and it is also \(1-s(\tau')\) (background on supports). So \(s(1-a)=s(\tau')\).

Uniqueness: if \(a'\) also satisfies (7.1), put \(b=a-a'\) and \(q=1_{(0,\infty)}(b)\). For projections \(e\in F_{\tau_0}\), \(\tau_0(bq\,e)=\tau(qe)-\tau(qe)=0\), where \(bq\,e=(bq)^{1/2}e(bq)^{1/2}\ge0\). By faithfulness \(e(bq)^{1/2}=0\) for all such \(e\), whose supremum is \(1\); so \(bq=0\). In the same way \(b(1-q)=0\), and \(a=a'\). \(\square\)

**Example 7.3** (Semifiniteness of \(\tau'\) is needed). On \(M=\mathbb C\) let \(\tau(t)=t\) and \(\tau'(t)=\infty\) for \(t>0\), \(\tau'(0)=0\). Then \(\tau'\) is a faithful normal trace that is not semifinite, and \(\tau+\tau'=\tau'\). No \(a\in[0,1]\) satisfies \(\tau(1)=\tau'(a)\): the right side is \(0\) or \(\infty\).

**Corollary 7.4** (Factors). On a semifinite factor, any two semifinite normal traces are proportional: if \(\tau\ne0\), then \(\tau'=c\tau\) for some \(c\in[0,\infty)\).

**Proof.** The support of a nonzero normal trace is a nonzero central projection, hence \(1\), so \(\tau\) is faithful. By Theorem 7.2, \(a=\lambda1\) with \(0<\lambda\le1\), and \(\tau'=(1-\lambda)\tau_0=\lambda^{-1}(1-\lambda)\tau\). \(\square\)

For \(B(H)\) this recovers that the semifinite normal traces are the multiples \(c\operatorname{Tr}\) with \(c<\infty\); the multiple \(\infty\cdot\operatorname{Tr}\) is normal but not semifinite.

**Example 7.5** (A computation). Let \(M=\ell^\infty(\mathbb N)\) with \(\mathbb N=\{0,1,2,\dots\}\), \(\tau(f)=\sum_nf(n)\) and \(\tau'(f)=\sum_nnf(n)\). Then \(\tau_0(f)=\sum_n(1+n)f(n)\) and \(a(n)=1/(1+n)\). Here \(s(a)=1\), while \(1-a\) vanishes at \(0\): its support is the indicator of \(\{1,2,\dots\}\), which is \(s(\tau')\).

## 9. Conditional expectations that preserve a trace

**Theorem 9.1** (Trace-preserving conditional expectation). Let \(\tau\) be a faithful semifinite normal trace on \(M\) and \(N\subseteq M\) a von Neumann subalgebra with the same unit. The following are equivalent:

- (a) the restriction of \(\tau\) to \(N_+\) is semifinite;
- (b) there is a normal projection of norm one \(E\) of \(M\) onto \(N\) with \(\tau(E(x))=\tau(x)\) for \(x\in M_+\).

When they hold, \(E\) is unique and faithful, \(E(axb)=aE(x)b\) for \(a,b\in N\), and \(E(x)\) is the unique element of \(N\) with
\[
\tau(E(x)\,y)=\tau(xy)\qquad(y\in\mathfrak m_\tau\cap N).
\tag{9.1}
\]
We call \(E\) the *conditional expectation* of \(M\) onto \(N\) with respect to \(\tau\).

**Proof.** (a)\(\Rightarrow\)(b). The restriction \(\tau_N\) is a faithful semifinite normal trace on \(N\). Its definition ideal is \(\mathfrak m_\tau\cap N\): the inclusion \(\subseteq\) is clear, and if \(x\in\mathfrak m_\tau\cap N\), then \(|x|\in F_\tau\cap N\) and \(x=u|x|\) with \(u\in N\), so \(x\) lies in the definition ideal of \(\tau_N\). For such \(x\), \(|x|\) is the same in \(N\) and in \(M\), so the two trace norms agree. Hence the inclusion extends to an isometry \(j:L^1(N,\tau_N)\to L^1(M,\tau)\). Let \(E\) be its transpose under the dualities of Theorem 1.1: for \(x\in M\), \(E(x)\in N\) is the element with \(\tau_N(E(x)y)=\tau(xy)\) for \(y\in L^1(N,\tau_N)\), in particular (9.1). Then \(E\) is linear, \(\|E(x)\|\le\|x\|\), \(E(b)=b\) for \(b\in N\), and \(E\) is continuous for the \(\sigma\)-weak topologies, because transposes are weak\(^*\) continuous and Theorem 1.1 identifies the topologies. By Tomiyama's theorem \(E\) is positive and \(N\)-bimodular, and a positive \(\sigma\)-weakly continuous map is normal. For \(x\in M_+\), let \(e_i\in F_\tau\cap N\) be projections increasing to \(1\) (semifiniteness of \(\tau_N\)). Using (0.1) and (9.1),
\[
\tau(x)=\sup_i\tau(x^{1/2}e_ix^{1/2})=\sup_i\tau(xe_i)=\sup_i\tau(E(x)e_i)=\sup_i\tau(E(x)^{1/2}e_iE(x)^{1/2})=\tau(E(x)).
\]
If \(E(x^*x)=0\), then \(\tau(x^*x)=0\) and \(x=0\): \(E\) is faithful.

(b)\(\Rightarrow\)(a). Let \(e_i\in F_\tau\) be projections increasing to \(1\). Then \(E(e_i)\in N_+\), \(\tau(E(e_i))=\tau(e_i)<\infty\), and \(E(e_i)\) increases to \(E(1)=1\) by normality. For \(b\in N\), the elements \(E(e_i)bE(e_i)\) lie in the definition ideal of \(\tau_N\) and converge \(\sigma\)-weakly to \(b\). So that ideal is \(\sigma\)-weakly dense, and \(\tau_N\) is semifinite.

Uniqueness. Let \(E'\) be a normal projection of norm one onto \(N\) with \(\tau\circ E'=\tau\). By Tomiyama's theorem it is positive and \(N\)-bimodular. For \(x\in M_+\) and \(y\in F_\tau\cap N\),
\[
\tau(E'(x)y)=\tau(y^{1/2}E'(x)y^{1/2})=\tau(E'(y^{1/2}xy^{1/2}))=\tau(y^{1/2}xy^{1/2})=\tau(xy).
\]
By linearity \(E'(x)\) satisfies (9.1) for all \(x\in M\), and an element of \(N\) is determined by its pairing with the dense subspace \(\mathfrak m_\tau\cap N\) of \(L^1(N,\tau_N)\) (Theorem 1.1 for \(N\)). So \(E'=E\). \(\square\)

**Example 9.2.** (a) *Diagonals.* In \(B(\ell^2)\) with the usual trace, let \(N\) be the diagonal operators. The trace is semifinite on \(N\), and \(E(x)\) is the diagonal of \(x\): both sides of (9.1) equal \(\sum_nx_{nn}y_n\) for a finitely supported diagonal \(y\).

(b) *Scalars.* For \(N=\mathbb C1\subseteq B(\ell^2)\), \(\operatorname{Tr}(\lambda1)=\infty\) for \(\lambda>0\), so the restriction is not semifinite, and there is no trace-preserving normal projection of norm one onto \(\mathbb C1\). Directly: such a map would be \(x\mapsto\varphi(x)1\) with a normal state \(\varphi\), and \(\operatorname{Tr}(x)=\infty\cdot\varphi(x)\) would fail for a rank-one \(x\) (the left side is finite and nonzero, the right side is \(0\) or \(\infty\)).

(c) *Partial traces.* Let \(\tau_0\) be a faithful semifinite normal trace on \(N_0\), let \(M=N_0\bar\otimes B(K)\) with the amplified trace \(\tau(x)=\sum_i\tau_0(x_{ii})\), and \(N=N_0\otimes1\). Then \(\tau(y\otimes1)=(\dim K)\,\tau_0(y)\), so the restriction is semifinite exactly when \(\dim K=n<\infty\). In that case \(E(x)=\bigl(\tfrac1n\sum_ix_{ii}\bigr)\otimes1\), the normalized partial trace.

(d) *The center.* If \(\tau\) is a faithful normal finite trace, the conditional expectation onto the center \(Z\) is the center-valued trace \(T\): for \(y\in Z\), \(\tau(T(x)y)=\tau(T(xy))=\tau(xy)\), because every finite trace factors through the center-valued trace (background), so \(T(x)\) satisfies (9.1).

