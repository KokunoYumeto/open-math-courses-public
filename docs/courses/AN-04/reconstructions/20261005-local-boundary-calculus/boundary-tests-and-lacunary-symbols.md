# Boundary tests, lacunary symbols and all normal jets

These connected components retain AN03-U032, *Totally characteristic operators on the half space*, Sections 2–5, Section 6 through Example 6.7, and Sections 7–13. Original author: Claude Opus 5.5 (Anthropic), September 2026; editorial additions: Codex, September 2026. Both were dedicated to the public domain (CC0). Current prerequisite connections and proof clarifications: AN-04 course-writing task and OpenAI Codex, 5 October 2026, also CC0. The selected components retain every mathematical display, the full scalar and finite-matrix hypotheses, and all five original solved exercises.

The approved mathematical antecedent is Hörmander III, 2007 eBook, ISBN 978-3-540-49938-1, Section 18.3. Its use and ordinary citation are valid. Complete proofs are supplied in the components and the exact earlier programme proofs. The earlier linked components retain their individual licences.

The four components, in proof order, are [Boundary tests, lacunary symbols and all normal jets](boundary-tests-and-lacunary-symbols.md), [Resolved corner kernels and their exact inverse](resolved-corner-kernels.md), [Boundary adjoints, complete composition and distributional action](boundary-adjoints-composition-and-distributions.md), [Boundary operator bounds, conormal action and the residual obstruction](boundary-bounds-and-conormal-action.md). Original section and equation numbers are retained across them. Sections 6.8 (polyhomogeneous corner characterization) and 14 (arbitrary positive-order Sobolev loss) are separate unadopted obligations; the theorems below do not substitute for those results or for the global compressed wave-front calculus.

## 1. Exact prerequisites and full test-space topology

Use \(D=-i\partial\), forward Fourier exponential \(e^{-ix\cdot\xi}\), inverse factor \((2\pi)^{-n}\), and Hilbert pairing \((u,v)=\int u\overline v\), linear in the first slot. Every bar on a scalar symbol in the adjoint formulas becomes conjugate transpose for finite matrices; products keep the displayed order and source/target dimensions. Complex-linear distribution pairings are used explicitly as functionals on test functions; Hilbert antidual formulas insert the indicated complex conjugation. When \(n=1\), tangential space is the single point \(\mathbb R^0\), with measure one; its Fourier transform is the identity and its test functions are scalars. This includes the tensor tests in Section 12.

The [ordinary quadratic multiplier and operator calculus O0–O6](../20261004-free-intrinsic-graph/prerequisites/ordinary-operator-calculus.md) gives Schwartz quantization, the exact Gauss multiplier, its full pre-diagonal estimate (O9), all parameter derivatives and convergence on bounded symbol sets. The [Fourier](../20261004-free-intrinsic-graph/prerequisites/fourier-l2.md) and [measure](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md) proofs supply inversion, Plancherel, Fubini and dominated convergence. The [Lebesgue Schur and dyadic estimates](../20261004-free-intrinsic-graph/prerequisites/dyadic-endpoint.md), [Hahn–Banach and integral inequalities](../20261005-cauchy-foundations/integration-and-duality.md), and half-space Hilbert duality are exact earlier proofs. All kernel bounds used here are on Lebesgue measure spaces.

The [conormal amplitude and test-space proofs](../20261005-conormal-test-foundations/conormal-amplitudes-and-test-spaces.md) give all-real Besov norms (C2), coordinate and coefficient bounds, amplitude characterization, tangent generators and complete conormal spaces. The supported conormal companion gives the actual supported topology and distribution conventions. In ambient dimension \(N\), codimension \(k\), conormal order \(\mu\) means tangent-word Besov order \(-\mu-N/4\); its reduced amplitude has order \(\mu+(N-2k)/4\). In Section 11 below \(\mathcal A^\kappa\) uses the **Besov** index \(\kappa\), rather than the conormal index used by the companion. Thus its conormal order is exactly \(-\kappa-n/4\).

We use the following full topological facts so that no quotient-completeness citation is left in place of a proof.

### 1.1. Schwartz completeness and a complete quotient

Let \(p_j\) be the increasing Schwartz seminorms consisting of the suprema of all weighted derivatives through index \(j\). A sequence Cauchy in every \(p_j\) converges uniformly, with every derivative, on each compact set. The fundamental theorem of calculus on coordinate segments shows that its derivative limits are derivatives of its function limit. Its weighted bounds and the Cauchy bounds pass to the limit pointwise and then by taking suprema. Thus the limit is Schwartz and convergence holds in every \(p_j\). The metric
\(\sum_{j\ge0}2^{-j-1}\min(1,p_j(u-v))\) induces precisely the seminorm topology and Cauchy notion: finite initial sums control a fixed seminorm, and the geometric tail is uniformly small. This proves Schwartz Fréchet completeness directly.

Here is the quotient argument in the needed generality. For a closed subspace \(N\) of a complete space with increasing seminorms \(p_j\), put
\(\bar p_j([x])=\inf_{n\in N}p_j(x+n)\).
These seminorms induce the quotient topology: a basic ball for one increasing seminorm maps to exactly the corresponding strict quotient ball, and its inverse image is the union of its translates by \(N\), an open set. They separate points. Indeed if all \(\bar p_j([x])=0\), choose \(n_j\) with \(p_j(x+n_j)<1/j\); then \(-n_j\to x\), so closedness gives \(x\in N\).

If \(z_l\) is Cauchy in every \(\bar p_j\), choose a subsequence \(z_{l_j}\) so that
\(\bar p_j(z_{l_{j+1}}-z_{l_j})<2^{-j-1}\).
For each difference choose a representative \(h_j\) with \(p_j(h_j)<2^{-j}\), and a representative \(x_1\) of \(z_{l_1}\). For every fixed \(k\), the tail of \(\sum_jh_j\) is Cauchy in \(p_k\), since \(p_k\le p_j\) when \(j\ge k\). Completeness gives \(x=x_1+\sum_jh_j\); its partial sums represent the chosen subsequence. Thus the subsequence converges to \([x]\), and the original Cauchy sequence does too, by the triangle inequality. The same countable-seminorm metric proves that this is a Fréchet quotient. This applies to the closed subspace of Schwartz functions vanishing in the positive half-space.

### 1.2. Fourier kernels without an unproved representation theorem

For the explicitly polynomially bounded compressed symbol \(a^\flat\), its partial inverse Fourier transform in frequency is a tempered distribution in \((x,z)\); the invertible linear substitution \(z=x-y\) gives \(K_a\). Pairing it with \(v(y)\varphi(x)\) and using Fourier inversion gives the operator integral (4.3), with the appropriate complex conjugation for the Hilbert pairing. These operations are inverse, so its kernel determines \(a^\flat\). Product tests determine the kernel: O0.1 proves density by Fourier inversion, frequency truncation and finite Riemann sums on compact supports. Therefore the action on Schwartz tests also determines \(a^\flat\), and hence \(a(x,\xi',\xi_n)\) for \(x_n>0\); continuity determines it at zero. Only this explicitly constructed kernel is used. No general Schwartz kernel representation theorem is needed.

All-real Besov completeness and the endpoint sequence inequalities are the exact proofs in the conormal companion. Local smooth and symbol completeness follows by the same uniform derivative limit argument above, with each specified weight. Every asymptotic formula below means its actual finite expansion with a remainder at each requested order; the complete quadratic-multiplier estimate proves those remainders. Construction of prescribed infinite symbol sums is a separate step of the later global calculus.

### 1.3. Conventions for the retained calculus

Throughout \(n\geq1\), \(x=(x',x_n)\in\mathbb R^{n-1}\times\mathbb R\), and
\[
\mathbb R^n_\pm=\{x:\pm x_n>0\},\qquad \overline{\mathbb R}{}^n_+=\{x:x_n\geq0\}.
\]
We write \(D=-i\partial\), \(\widehat u(\xi)=\int e^{-ix\cdot\xi}u(x)\,dx\) (inverse factor \((2\pi)^{-n}\)), \(\langle\xi\rangle=(1+|\xi|^2)^{1/2}\), and \((u,v)=\int u\overline v\), linear in the first argument. For a function of \((x,\xi)\) we write \(a^{(\alpha)}_{(\beta)}=\partial_\xi^\alpha\partial_x^\beta a\).

\(C^\infty(\overline{\mathbb R}{}^n_+)\) denotes the functions on \(\overline{\mathbb R}{}^n_+\) that are smooth in \(\mathbb R^n_+\) and whose derivatives all extend continuously to \(\overline{\mathbb R}{}^n_+\). Compactly localized such functions admit Schwartz extensions by Lemma 3.2(c) below, whose proof uses only the just-proved quotient completeness; a partition gives the local smooth extension assertion. \(C^\infty_b\) means smooth with all derivatives bounded.

**Sobolev and Besov spaces.** \(H_{(s)}\) is the space of tempered distributions \(u\) whose Fourier transform is locally square integrable and for which the norm \(\|u\|_{(s)}^2=(2\pi)^{-n}\int\langle\xi\rangle^{2s}|\widehat u|^2d\xi\) is finite. With the sharp annuli \(A_0=\{|\xi|<1\}\), \(A_j=\{2^{j-1}\leq|\xi|<2^j\}\) and the Fourier projections \(\Pi_j\) onto them, the dyadic Besov norm is
\[
\|u\|_{B^s_{2,p}}=\big\|\big(2^{js}\|\Pi_ju\|_{L^2}\big)_{j\geq0}\big\|_{\ell^p},\qquad 1\leq p\leq\infty .
\tag{1.1}
\]
\(B^s_{2,p}\) is the space of tempered distributions with locally square-integrable Fourier transform for which this norm is finite. Since \(\langle\xi\rangle\) is comparable to \(2^j\) on \(A_j\), \(B^s_{2,2}=H_{(s)}\) with equivalent norms. A distribution \(u\) on an open set \(\Omega\subset\mathbb R^n\) lies in the local space \(B^s_{2,p,\mathrm{loc}}(\Omega)\) if \(\chi u\), extended by zero, lies in \(B^s_{2,p}\) for every \(\chi\in C_0^\infty(\Omega)\).

**Values of symbols.** All symbols may take values in \(L(\mathbb C^p,\mathbb C^q)\) for fixed finite \(p,q\). Then \(|\cdot|\) is the operator norm, products keep their order, and complex conjugation of a symbol is replaced by the conjugate transpose \(a^*\). Every statement below holds in this generality with the same proof, except the square-root step in the proof of Theorem 10.1, where we say what changes. The reader may keep \(p=q=1\) in mind.

We also use Peetre's inequality \((1+|\xi+\zeta|)^s\leq(1+|\xi|)^s(1+|\zeta|)^{|s|}\) for real \(s\), which follows from \(1+|\xi|\leq(1+|\xi+\zeta|)(1+|\zeta|)\).

## 2. Totally characteristic differential operators

Let \(\mathcal V_b\) be the smooth vector fields \(V=\sum_jv_j\partial_j\), \(v_j\in C^\infty(\overline{\mathbb R}{}^n_+)\), that are tangent to the boundary, that is, \(v_n(x',0)=0\). Let \(\operatorname{Diff}_b(\overline{\mathbb R}{}^n_+)\) be the algebra of operators on \(C^\infty(\overline{\mathbb R}{}^n_+)\) generated by \(\mathcal V_b\) and by multiplication with functions in \(C^\infty(\overline{\mathbb R}{}^n_+)\), and \(\operatorname{Diff}^m_b\) the span of products containing at most \(m\) vector fields. Its elements are the *totally characteristic* differential operators.

**Proposition 2.1** (Structure of totally characteristic differential operators).

(a) \(\mathcal V_b\) is the \(C^\infty(\overline{\mathbb R}{}^n_+)\)-module generated by \(\partial_1,\ldots,\partial_{n-1}\) and \(x_n\partial_n\).

(b) For every integer \(k\geq0\),
\[
x_n^kD_n^k=\prod_{j=0}^{k-1}\big(x_nD_n+ij\big)=:q_k(x_nD_n).
\tag{2.1}
\]
Hence \(\{x_n^jD_n^j:j\leq k\}\) and \(\{(x_nD_n)^j:j\leq k\}\) span the same space, with constant coefficients.

(c) \(\operatorname{Diff}^m_b\) consists exactly of the finite sums
\[
P=\sum_{|\alpha|\leq m}c_\alpha(x)\,x_n^{\alpha_n}D^\alpha,\qquad c_\alpha\in C^\infty(\overline{\mathbb R}{}^n_+),
\tag{2.2}
\]
equivalently of the sums \(\sum_{|\alpha|\leq m}c'_\alpha(x)D'^{\alpha'}(x_nD_n)^{\alpha_n}\).

(d) For \(P\) as in (2.2) and \(u\in C^\infty(\overline{\mathbb R}{}^n_+)\), \((Pu)(x',0)=\sum_{\alpha_n=0}c_\alpha(x',0)D'^{\alpha'}u(x',0)\): the boundary value of \(Pu\) depends only on the boundary value of \(u\).

**Proof.** (a) If \(v_n(x',0)=0\), then \(v_n(x)=x_nw(x)\) with \(w(x)=\int_0^1(\partial_nv_n)(x',\theta x_n)\,d\theta\in C^\infty(\overline{\mathbb R}{}^n_+)\). Thus \(V=\sum_{j<n}v_j\partial_j+w\,x_n\partial_n\). Conversely each generator is tangent.

(b) For \(k\geq0\) and \(u\) smooth, \(x_nD_n(x_n^kD_n^ku)=x_n^{k+1}D_n^{k+1}u+x_n(D_nx_n^k)D_n^ku=x_n^{k+1}D_n^{k+1}u-ik\,x_n^kD_n^ku\), because \(D_nx_n^k=-ikx_n^{k-1}\). So \(x_n^{k+1}D_n^{k+1}=(x_nD_n+ik)\,x_n^kD_n^k\), and induction gives (2.1). The polynomial \(q_k\) is monic of degree \(k\), so the triangular system can be inverted.

(c) Moving a function to the left across a generator produces only multiplication operators: \(\partial_jc=c\partial_j+(\partial_jc)\) and \(x_n\partial_nc=c\,x_n\partial_n+x_n(\partial_nc)\). So a product of at most \(m\) vector fields and functions is a sum of terms \(c(x)M_1\cdots M_l\), \(l\leq m\), with each \(M_i\) one of the generators in (a). These generators commute pairwise, because \([x_n\partial_n,\partial_j]=0\) for \(j<n\). So each word is a constant times \(D'^{\beta'}(x_nD_n)^{\beta_n}\) with \(|\beta|\leq m\), and (b) rewrites it in the form (2.2). Conversely \(x_n^{\alpha_n}D^\alpha=D'^{\alpha'}q_{\alpha_n}(x_nD_n)\) is a product of \(|\alpha|\) generators.

(d) At \(x_n=0\) every term with \(\alpha_n>0\) carries the factor \(x_n^{\alpha_n}\), which vanishes. \(\square\)

Part (d) is the motivation for the whole lesson. An operator that respects the boundary in this way can be followed by boundary operators. Theorem 5.1(c) below extends (d) to the pseudodifferential operators of this lesson and to normal derivatives of every order.

## 3. Function spaces on the half space

### Restrictions and supports

**Two ways to attach a space to the half space.** Let \(F\) be a space of distributions on \(\mathbb R^n\).

* \(\overline F(\mathbb R^n_+)\) is the space of restrictions \(U|_{\mathbb R^n_+}\), \(U\in F\), with the quotient topology of \(F/\{U\in F:U=0\text{ in }\mathbb R^n_+\}\).
* \(\dot F(\overline{\mathbb R}{}^n_+)\) is the space of \(U\in F\) with \(\operatorname{supp}U\subset\overline{\mathbb R}{}^n_+\), with the topology of \(F\).

These are different objects and must be kept apart. A restriction of a Schwartz function may have any boundary values. A Schwartz function supported in \(\overline{\mathbb R}{}^n_+\) vanishes to infinite order on \(x_n=0\), since all its derivatives are continuous and vanish for \(x_n<0\). The zero extension of an element of \(\overline{\mathcal S}(\mathbb R^n_+)\) is an integrable function in \(\dot{\mathcal S}'(\overline{\mathbb R}{}^n_+)\); it lies in \(\dot{\mathcal S}(\overline{\mathbb R}{}^n_+)\) only when all its normal derivatives vanish at the boundary. In this notation, \(C^\infty(\overline{\mathbb R}{}^n_+)=\overline{C^\infty}(\mathbb R^n_+)\), by the locally applied Schwartz extension proof in Lemma 3.2(c).

**Lemma 3.1** (Supports in the closed half space). Let \(U\in\mathcal S'(\mathbb R^n)\) with \(\operatorname{supp}U\subset\overline{\mathbb R}{}^n_+\), and let \(\varphi\in\mathcal S(\mathbb R^n)\) vanish in \(\mathbb R^n_+\). Then \(U(\varphi)=0\).

**Proof.** First, \(U(\psi)=0\) whenever \(\psi\in\mathcal S\) vanishes on a neighbourhood \(W\) of \(\operatorname{supp}U\): for \(\psi\in C_0^\infty\) this is the definition of the support, and in general \(\psi\,\theta(\cdot/R)\to\psi\) in \(\mathcal S\) for a cutoff \(\theta\) equal to 1 near 0, while each \(\psi\theta(\cdot/R)\) vanishes on \(W\). Now put \(\varphi_\delta(x)=\varphi(x',x_n+\delta)\). It vanishes on \(\{x_n>-\delta\}\), a neighbourhood of \(\overline{\mathbb R}{}^n_+\), so \(U(\varphi_\delta)=0\); and \(\varphi_\delta\to\varphi\) in \(\mathcal S\) as \(\delta\to0\). \(\square\)

### Restricted Schwartz functions

For \(v\in\overline{\mathcal S}(\mathbb R^n_+)\) and multi-indices \(\alpha,\beta\) put
\[
q_{\alpha,\beta}(v)=\sup_{x\in\mathbb R^n_+}|x^\alpha D^\beta v(x)| .
\]

**Lemma 3.2** (Restricted Schwartz functions).

(a) Each \(q_{\alpha,\beta}\) is finite and continuous on \(\overline{\mathcal S}(\mathbb R^n_+)\). For every continuous seminorm \(q\) on \(\overline{\mathcal S}(\mathbb R^n_+)\) there are \(k\) and \(C\) with
\[
q(v)\leq C\sum_{|\alpha|+|\beta|\leq2k}q_{\alpha,\beta}(v) .
\tag{3.1}
\]
So the \(q_{\alpha,\beta}\) define the quotient topology.

(b) \(\overline{\mathcal S}(\mathbb R^n_+)\) is a Fréchet space.

(c) A function \(w\in C^\infty(\overline{\mathbb R}{}^n_+)\) is the restriction of a Schwartz function if and only if every \(q_{\alpha,\beta}(w)\) is finite.

(d) If \(g\in\overline{\mathcal S}(\mathbb R^n_+)\), \(k\geq1\), and \(\partial_n^jg(x',0)=0\) for \(j<k\), then \(g=x_n^kh\) with \(h\in\overline{\mathcal S}(\mathbb R^n_+)\).

**Proof.** (a) For every extension \(V\) of \(v\), \(q_{\alpha,\beta}(v)\leq\sup_{\mathbb R^n}|x^\alpha D^\beta V|\); so \(q_{\alpha,\beta}\) is bounded by a quotient seminorm, hence finite and continuous. Conversely let \(q\) be continuous, and let \(\pi\) be the restriction map. Then \(q\circ\pi\) is a continuous seminorm on \(\mathcal S(\mathbb R^n)\), so there are \(k,C\) with \(q(\pi V)\leq C\sum_{|\alpha|+|\beta|\leq k}\sup_{\mathbb R^n}|x^\alpha D^\beta V|\). Fix \(V\in\mathcal S\). Put \(\tilde V=V\) on \(x_n\geq0\) and
\[
\tilde V(x)=\theta(x_n)\sum_{j\leq k}\partial_n^jV(x',0)\frac{x_n^j}{j!}\qquad(x_n<0),
\]
with \(\theta\in C_0^\infty(\mathbb R)\) equal to 1 on \((-1,1)\). The two pieces have the same derivatives of order \(\leq k\) on \(x_n=0\), so \(\tilde V\in C^k(\mathbb R^n)\). For \(|\alpha|+|\beta|\leq k\), \(\sup_{\mathbb R^n}(1+|x|)^{|\alpha|}|D^\beta\tilde V|\) is bounded by a constant times \(\sum_{|\alpha'|+|\gamma|\leq2k}q_{\alpha',\gamma}(\pi V)\): on \(x_n\geq0\) this is clear, and on \(x_n<0\) the derivatives are combinations of derivatives of \(\theta(x_n)x_n^j\) (bounded, with support in a fixed interval) and of \(D'^{\beta'}\partial_n^jV(x',0)\), \(|\beta'|+j\leq2k\), whose weighted suprema are limits from \(\mathbb R^n_+\). Now take \(\phi\in C_0^\infty(\mathbb R^n_-)\) with \(\int\phi=1\), \(\phi_\varepsilon(x)=\varepsilon^{-n}\phi(x/\varepsilon)\), \(0<\varepsilon\leq1\). Then \(\tilde V*\phi_\varepsilon\in\mathcal S(\mathbb R^n)\). For \(x\in\mathbb R^n_+\) the convolution only uses values at \(x-y\) with \((x-y)_n>x_n>0\), so \(\pi(\tilde V*\phi_\varepsilon)=\pi(V*\phi_\varepsilon)\). For \(|\beta|\leq k\), \(D^\beta(\tilde V*\phi_\varepsilon)=(D^\beta\tilde V)*\phi_\varepsilon\), and \(1+|x|\leq(1+R)(1+|x-y|)\) for \(y\in\operatorname{supp}\phi_\varepsilon\subset\{|y|\leq R\}\). Hence \(q(\pi(V*\phi_\varepsilon))\leq C'\sum_{|\alpha|+|\beta|\leq2k}q_{\alpha,\beta}(\pi V)\), uniformly in \(\varepsilon\). Since \(V*\phi_\varepsilon\to V\) in \(\mathcal S\), (3.1) follows.

(b) The subspace \(\{V\in\mathcal S:V=0\text{ in }\mathbb R^n_+\}\) is closed, since point evaluations are continuous. The full quotient construction in Section 1.1 above proves this assertion.

(c) Necessity is clear. Conversely let every \(q_{\alpha,\beta}(w)\) be finite, let \(w_0\) be the zero extension of \(w\), and let \(\phi_\varepsilon\) be as in (a). Then \(W_\varepsilon=w_0*\phi_\varepsilon\in\mathcal S(\mathbb R^n)\), because \(w_0\) is bounded and rapidly decreasing and all derivatives fall on \(\phi_\varepsilon\). If \(\operatorname{supp}\phi\subset\{y_n\leq-c\}\), then for \(x\) near a point of \(\mathbb R^n_+\) the integral \(\int w_0(x-y)\phi_\varepsilon(y)dy\) only involves points with \((x-y)_n\geq x_n+c\varepsilon\), so we may differentiate under it: \(D^\beta W_\varepsilon(x)=\int(D^\beta w)(x-y)\phi_\varepsilon(y)\,dy\). By the mean value theorem along segments, which stay in \(\mathbb R^n_+\),
\[
|x^\alpha(D^\beta W_\varepsilon-D^\beta w)(x)|\leq C\varepsilon\sum_{|\alpha'|\leq|\alpha|,\,|\gamma|=|\beta|+1}q_{\alpha',\gamma}(w)\qquad(x\in\mathbb R^n_+).
\]
So \(\pi W_\varepsilon\to w\) in every \(q_{\alpha,\beta}\). By (a) the family is Cauchy in \(\overline{\mathcal S}(\mathbb R^n_+)\), by (b) it converges to some \(\pi W\), and since \(q_{0,0}\) is continuous the limit agrees with \(w\) on \(\mathbb R^n_+\).

(d) On \(x_n>1\) put \(h=g/x_n^k\). On \(0\leq x_n<2\) Taylor's formula with integral remainder and the vanishing jets give \(g=x_n^kh\) with \(h(x)=\frac1{(k-1)!}\int_0^1(1-\theta)^{k-1}(\partial_n^kg)(x',\theta x_n)\,d\theta\). The two definitions agree for \(1<x_n<2\). The second one is smooth up to \(x_n=0\), and both have finite weighted suprema of all derivatives (on \(x_n\leq2\) the weights are controlled by \(1+|x'|\)). So \(h\in\overline{\mathcal S}(\mathbb R^n_+)\) by (c). \(\square\)

## 4. Symbols, compressed quantization and lacunarity

### The symbol class and its quantization

**Definition 4.1** (The class \(S^m_+\)). For \(m\in\mathbb R\), \(S^m_+\) is the set of \(a\in C^\infty(\overline{\mathbb R}{}^n_+\times\mathbb R^n)\) such that for all multi-indices \(\alpha,\beta\) and all integers \(\nu\geq0\)
\[
p^m_{\alpha,\beta,\nu}(a)=\sup_{x\in\overline{\mathbb R}{}^n_+,\ \xi\in\mathbb R^n}(1+|\xi|)^{|\alpha|-m}(1+x_n)^{\nu}\,|a^{(\alpha)}_{(\beta)}(x,\xi)|<\infty .
\tag{4.1}
\]
These seminorms make \(S^m_+\) a Fréchet space: a sequence that is Cauchy for all of them converges locally uniformly with all derivatives, and the weighted bounds pass to the limit. We put \(S^{-\infty}_+=\bigcap_mS^m_+\). The estimates are uniform in \(x'\), with no decay in \(x'\), and require rapid decay in \(x_n\).

**Compression and quantization.** For \(a\in S^m_+\) put
\[
a^\flat(x,\xi)=a(x,\xi',x_n\xi_n)\quad(x_n\geq0),\qquad a^\flat(x,\xi)=0\quad(x_n<0),
\tag{4.2}
\]
and, for \(u\in\mathcal S(\mathbb R^n)\),
\[
T_au(x)=(2\pi)^{-n}\int e^{ix\cdot\xi}a^\flat(x,\xi)\,\widehat u(\xi)\,d\xi .
\tag{4.3}
\]
Since \(1+|(\xi',x_n\xi_n)|\leq(1+x_n)(1+|\xi|)\), the compressed symbol grows at most polynomially and the integral converges absolutely. We always write the last variable of \(a\) as \(\xi_n\); thus \(\partial_{\xi_n}a\) is the derivative of \(a\) in its last slot, \((\partial_{\xi_n}a)^\flat\) its compression, and \(\partial_{\xi_n}(a^\flat)=x_n(\partial_{\xi_n}a)^\flat\). We also write \(\xi_na\) for the symbol \((x,\xi)\mapsto\xi_na(x,\xi)\); its compression is \(x_n\xi_na^\flat\).

Two remarks explain the choice of class. First, away from the boundary \(T_a\) is an ordinary pseudodifferential operator. Indeed, for \(x_n\geq1\) the compressed symbol obeys the ordinary estimates of \(S^m\) uniformly. Each \(\partial_{\xi_n}\) of \(a^\flat\) brings a factor \(x_n\), and each \(\partial_{x_n}\) brings \((\partial_{x_n}a)^\flat\) or \(\xi_n(\partial_{\xi_n}a)^\flat\), where \(|\xi_n|\leq(1+|(\xi',x_n\xi_n)|)/x_n\). Moreover \((1+|\xi|)\leq1+|(\xi',x_n\xi_n)|\leq x_n(1+|\xi|)\). So every derivative obeys the estimate of \(S^m\) up to powers of \(x_n\), and the rapid decay in \(x_n\) absorbs every power of \(x_n\). Second, near \(x_n=0\) the compressed symbol is not a classical symbol: \(\partial_{\xi_n}a^\flat=x_n(\partial_{\xi_n}a)^\flat\) gains no power of \(\langle\xi\rangle\).

If \(P=\sum_{|\alpha|\leq m}c_\alpha(x)x_n^{\alpha_n}D^\alpha\) with \(c_\alpha\in C^\infty_b(\overline{\mathbb R}{}^n_+)\) vanishing for \(x_n\geq R\), then \(P=T_p\) with \(p(x,\xi)=\sum c_\alpha(x)\xi^\alpha\in S^{m}_+\): indeed \(p^\flat=\sum c_\alpha(x)\xi'^{\alpha'}(x_n\xi_n)^{\alpha_n}\), and left quantization places functions of \(x\) on the left. So Proposition 2.1 suggests the definition.

**The kernel.** The compressed symbol is a polynomially bounded measurable function. So, by the explicit Fourier-kernel construction in Section 1.2, the operator \(T_a:\mathcal S\to\mathcal S'\) has the tempered kernel \(K_a(x,y)=(2\pi)^{-n}\int e^{i(x-y)\cdot\xi}a^\flat(x,\xi)\,d\xi\). For \(x_n>0\) the substitution \(\eta_n=x_n\xi_n\) suggests
\[
K_a(x,y)=x_n^{-1}A\Big(x,\,x'-y',\,\frac{x_n-y_n}{x_n}\Big),\qquad A(x,z)=(2\pi)^{-n}\int e^{iz\cdot\xi}a(x,\xi)\,d\xi .
\tag{4.4}
\]
For residual symbols this is an identity of functions (Theorem 6.2(b)). We want \(T_au\) to depend only on \(u|_{\mathbb R^n_+}\), that is, \(K_a(x,y)=0\) for \(y_n<0\). With \(z_n=(x_n-y_n)/x_n\), the condition \(y_n<0\) means \(z_n>1\). So \(A(x,\cdot)\) should vanish on \(z_n>1\); this is a condition on the Fourier transform of \(a\) in its last variable.

### Lacunary symbols

**Definition 4.2** (Lacunary symbols). For \(a\in S^m_+\) and fixed \((x,\xi')\), the function \(\xi_n\mapsto a(x,\xi',\xi_n)\) is tempered; let \(\mathcal F_na(x,\xi',\cdot)\) be its Fourier transform, a tempered distribution in the dual variable \(t\) (formally \(\int e^{-it\xi_n}a\,d\xi_n\)). We call \(a\) *lacunary* if
\[
\operatorname{supp}\mathcal F_na(x,\xi',\cdot)\subset[-1,\infty)\qquad\text{for all }(x,\xi')\in\overline{\mathbb R}{}^n_+\times\mathbb R^{n-1},
\tag{4.5}
\]
that is, \(\int a(x,\xi',\xi_n)\widehat\varphi(\xi_n)\,d\xi_n=0\) for every \(\varphi\in C_0^\infty((-\infty,-1))\). We call \(a\) *strongly lacunary* if these supports lie in \([-\tfrac12,1]\). \(S^m_{\mathrm{la}}\) denotes the lacunary elements of \(S^m_+\) and \(S^{-\infty}_{\mathrm{la}}=\bigcap_mS^m_{\mathrm{la}}\).

Each defining condition is a continuous linear functional on \(S^m_+\), since \(|\int a\widehat\varphi|\leq p(a)\int(1+|\xi'|+|\xi_n|)^{|m|}|\widehat\varphi(\xi_n)|d\xi_n\). So \(S^m_{\mathrm{la}}\) is a closed subspace and a Fréchet space.

The following closure properties are used constantly. If \(a\) is lacunary (strongly lacunary), then so are \(\partial_x^\beta a\), \(\partial_{\xi'}^\gamma a\), \(\partial_{\xi_n}a\), \(\xi^\gamma a\), and \(c(x)a\) for \(c\in C^\infty_b(\overline{\mathbb R}{}^n_+)\). Indeed \(\mathcal F_n\) commutes with operations in \(x\) and \(\xi'\), turns \(\partial_{\xi_n}\) into multiplication by \(it\), and turns multiplication by \(\xi_n\) into \(i\partial_t\); none of these enlarges the support.

**Proposition 4.3** (Lacunarity is exactly the support condition). For \(a\in S^m_+\) the following are equivalent.

1. \(a\) is lacunary.
2. \(T_av=0\) in \(\mathbb R^n_+\) for every \(v\in\mathcal S(\mathbb R^n)\) that vanishes in \(\mathbb R^n_+\).
3. \(T_av=0\) in \(\mathbb R^n_+\) for every \(v\in C_0^\infty(\mathbb R^n_-)\).

**Proof.** Fix \(x\in\mathbb R^n_+\) and \(v\in\mathcal S\). Let \(w(\xi',y_n)=\int e^{-iy'\cdot\xi'}v(y',y_n)\,dy'\), so that \(\widehat v(\xi',\xi_n)=\int e^{-iy_n\xi_n}w(\xi',y_n)\,dy_n\). By Fubini,
\[
T_av(x)=(2\pi)^{-n}\int e^{ix'\cdot\xi'}J(x,\xi')\,d\xi',\qquad
J(x,\xi')=\int a(x,\xi',x_n\xi_n)\,e^{ix_n\xi_n}\,\widehat v(\xi',\xi_n)\,d\xi_n .
\]
Substitute \(\eta_n=x_n\xi_n\), and write \(e^{ix_n\xi_n}\widehat v(\xi',\xi_n)=\int e^{-i(y_n-x_n)\xi_n}w(\xi',y_n)\,dy_n\). With \(s=(y_n-x_n)/x_n\) one finds
\[
J(x,\xi')=x_n^{-1}\int a(x,\xi',\eta_n)\,\widehat{\phi_{x,\xi'}}(\eta_n)\,d\eta_n,\qquad \phi_{x,\xi'}(s)=x_n\,w\big(\xi',x_n(1+s)\big).
\tag{4.6}
\]
(1 \(\Rightarrow\) 2) If \(v=0\) in \(\mathbb R^n_+\), then \(w(\xi',y_n)=0\) for \(y_n>0\), so \(\phi=\phi_{x,\xi'}\) vanishes for \(s>-1\). The translates \(\phi_\delta(s)=\phi(s+\delta)\) vanish on \((-1-\delta,\infty)\), a neighbourhood of \([-1,\infty)\), and \(\phi_\delta\to\phi\) in \(\mathcal S(\mathbb R)\). Hence \(\int a\,\widehat\phi\,d\eta_n=\langle\mathcal F_na,\phi\rangle=\lim_{\delta\to0}\langle\mathcal F_na,\phi_\delta\rangle=0\). So \(J=0\) and \(T_av(x)=0\).

(2 \(\Rightarrow\) 3) is trivial.

(3 \(\Rightarrow\) 1) Take \(v(y)=v_1(y')v_2(y_n)\) with \(v_1\in C_0^\infty(\mathbb R^{n-1})\) and \(v_2\in C_0^\infty((-\infty,0))\). Then \(w=\widehat{v_1}(\xi')v_2(y_n)\) and \(J(x,\xi')=\widehat{v_1}(\xi')\,j(x,\xi')\) with \(j(x,\xi')=x_n^{-1}\int a(x,\xi',\eta_n)\widehat{\psi_x}(\eta_n)\,d\eta_n\), \(\psi_x(s)=x_nv_2(x_n(1+s))\). For fixed \(x\), the continuous polynomially bounded function \(\xi'\mapsto e^{ix'\cdot\xi'}j(x,\xi')\) annihilates every \(\widehat{v_1}\), and these are dense in \(\mathcal S(\mathbb R^{n-1})\); so \(j(x,\cdot)=0\). As \(v_2\) runs through \(C_0^\infty((-\infty,0))\), \(\psi_x\) runs through all of \(C_0^\infty((-\infty,-1))\). This proves (4.5) for \(x_n>0\), and continuity in \(x\) gives it at \(x_n=0\). \(\square\)

### Every symbol is lacunary up to a residual symbol

**Lemma 4.4** (Lacunary modification of a symbol). Let \(\rho\in\mathcal S(\mathbb R)\) with \(\widehat\rho\in C_0^\infty((-\tfrac12,1))\) and \(\widehat\rho=1\) near 0. For \(a\in S^m_+\) put
\[
a_\rho(x,\xi)=\int a(x,\xi',\xi_n-t)\,\rho(t)\,dt .
\tag{4.7}
\]
Then:

(a) \(a\mapsto a_\rho\) is continuous \(S^m_+\to S^m_+\), and \(a_\rho\) is strongly lacunary, with \(\operatorname{supp}\mathcal F_na_\rho(x,\xi',\cdot)\subset\operatorname{supp}\widehat\rho\).

(b) \(a-a_\rho\in S^{-\infty}_+\), and \(a\mapsto a-a_\rho\) is continuous from \(S^m_+\) into every \(S^{m'}_+\).

(c) If \(a\) is lacunary (strongly lacunary), so is \(a-a_\rho\).

(d) The kernel of \(T_{a_\rho}\) vanishes on the open set \(\{x_n>0,\ y_n/x_n\notin[\tfrac12,2]\}\).

(e) The natural map \(S^m_{\mathrm{la}}/S^{-\infty}_{\mathrm{la}}\to S^m_+/S^{-\infty}_+\) is bijective.

**Proof.** (a) By Peetre's inequality,
\[
|(a_\rho)^{(\alpha)}_{(\beta)}(x,\xi)|\leq\int|a^{(\alpha)}_{(\beta)}(x,\xi',\xi_n-t)||\rho(t)|\,dt\leq p(a)(1+x_n)^{-\nu}(1+|\xi|)^{m-|\alpha|}\int(1+|t|)^{|m-|\alpha||}|\rho(t)|\,dt .
\]
By the convolution theorem \(\mathcal F_na_\rho=\widehat\rho\,\mathcal F_na\), whose support lies in \(\operatorname{supp}\widehat\rho\subset(-\tfrac12,1)\).

(b) Since \(\widehat\rho(\tau)=\int e^{-i\tau t}\rho(t)dt\) equals 1 near 0, \(\int\rho=1\) and \(\int t^j\rho(t)\,dt=0\) for \(j\geq1\). Hence, for every \(N\),
\[
a_\rho(x,\xi)-a(x,\xi)=\int\Big(a(x,\xi',\xi_n-t)-\sum_{j<N}\partial_{\xi_n}^ja(x,\xi)\frac{(-t)^j}{j!}\Big)\rho(t)\,dt .
\tag{4.8}
\]
Where \(|t|<(1+|\xi|)/2\), Taylor's formula bounds the bracket by \(|t|^N/N!\) times the supremum of \(|\partial^N_{\xi_n}a|\) on the segment from \(\xi\) to \(\xi-te_n\); there \(1+|\xi|\) and the norm of the point differ by a factor at most 2, so the bracket is at most \(C_Np(a)|t|^N(1+|\xi|)^{m-N}(1+x_n)^{-\nu}\). Where \(|t|\geq(1+|\xi|)/2\), each term of the bracket is at most \(Cp(a)(1+|t|)^{|m|+N}(1+x_n)^{-\nu}\), and \(1+|\xi|\leq2(1+|t|)\) gives \((1+|t|)^{|m|+N}\leq2^{N+|m|}(1+|\xi|)^{m-N}(1+|t|)^{2N+2|m|}\). Integrating against the rapidly decreasing \(|\rho|\) gives \(|a_\rho-a|\leq C_Np(a)(1+|\xi|)^{m-N}(1+x_n)^{-\nu}\) for all \(N,\nu\). Derivatives commute with the convolution, so the same argument applied to \(a^{(\alpha)}_{(\beta)}\in S^{m-|\alpha|}_+\) proves (b), with every seminorm controlled by finitely many seminorms of \(a\).

(c) \(\mathcal F_n(a-a_\rho)=(1-\widehat\rho)\mathcal F_na\) has support inside that of \(\mathcal F_na\).

(d) Fix \(x\) with \(x_n>0\) and let \(v\in\mathcal S\) vanish on the closed slab \(\{y:x_n/2\leq y_n\leq2x_n\}\). In (4.6) the function \(\phi_{x,\xi'}\) then vanishes on \([-\tfrac12,1]\), which is a neighbourhood of the compact set \(\operatorname{supp}\widehat\rho\). Hence \(J=0\) and \(T_{a_\rho}v(x)=0\). If \(\psi\in C_0^\infty\) and \(v\in C_0^\infty\) have \(\operatorname{supp}\psi\times\operatorname{supp}v\) inside the open set of (d), this gives \((T_{a_\rho}v,\psi)=0\); such products span a dense set of test functions by the complete O0.1 argument identified in Section 1.2, which proves (d).

(e) The kernel of the map is \(S^m_{\mathrm{la}}\cap S^{-\infty}_+=S^{-\infty}_{\mathrm{la}}\); surjectivity is (a)–(b). \(\square\)

By (e), the lacunary condition only restricts the residual part of a symbol. It has no effect on principal symbols or asymptotic expansions.

## 5. Action on restricted Schwartz functions

### Continuity, commutators and boundary jets

**Theorem 5.1** (Action, commutators and boundary jets). Let \(a\in S^m_{\mathrm{la}}\).

(a) For \(u\in\overline{\mathcal S}(\mathbb R^n_+)\) and any \(U\in\mathcal S(\mathbb R^n)\) equal to \(u\) in \(\mathbb R^n_+\), the restriction \((T_aU)|_{\mathbb R^n_+}\) depends only on \(u\); we call it \(T_au\). It lies in \(\overline{\mathcal S}(\mathbb R^n_+)\), and \((a,u)\mapsto T_au\) is a continuous bilinear map \(S^m_{\mathrm{la}}\times\overline{\mathcal S}(\mathbb R^n_+)\to\overline{\mathcal S}(\mathbb R^n_+)\). More precisely, for every \((\alpha,\beta)\) there are a seminorm \(p\) of \(S^m_+\) and a continuous seminorm \(\bar p\) of \(\overline{\mathcal S}(\mathbb R^n_+)\), depending only on \(\alpha,\beta,m,n\), with \(q_{\alpha,\beta}(T_au)\leq p(a)\,\bar p(u)\).

(b) As operators on \(\overline{\mathcal S}(\mathbb R^n_+)\), for \(j<n\),
\[
[T_a,D_j]=iT_{\partial_{x_j}a},\qquad [T_a,x_j]=-iT_{\partial_{\xi_j}a},
\]
and for the normal direction
\[
[T_a,D_n]=iT_{\partial_{x_n}a}+iT_{\partial_{\xi_n}a}D_n,\qquad [T_a,x_n]=-i\,x_n\,T_{\partial_{\xi_n}a}.
\tag{5.1}
\]

(c) For every integer \(k\geq0\) and \(u\in\overline{\mathcal S}(\mathbb R^n_+)\),
\[
D_n^k(T_au)(x',0)=\sum_{j=0}^k\binom kj\,a_{kj}(x',D')\big(D_n^ju(\cdot,0)\big)(x'),\qquad
a_{kj}(x',\xi')=\sum_{i=0}^j\binom ji\big(D_{x_n}^{k-j}D_{\xi_n}^ia\big)(x',0,\xi',0).
\tag{5.2}
\]
Here \(a_{kj}\in S^m(\mathbb R^{n-1}\times\mathbb R^{n-1})\), its \(i\)-th summand has order \(m-i\), and \(a_{kj}(x',D')\) is the left quantization on \(\mathbb R^{n-1}\).

(d) If \(D_n^ju(\cdot,0)=0\) for \(j<k\), then \(D_n^j(T_au)(\cdot,0)=0\) for \(j<k\). In particular \(T_a\) maps \(\dot{\mathcal S}(\overline{\mathbb R}{}^n_+)\) into itself.

The normal commutator has precisely the factor \(x_n\), as the full calculation and Example 5.2 below show.

**Proof.** (a) Let \(U\in\mathcal S\) and, for \(x\in\overline{\mathbb R}{}^n_+\), put \(W(x)=(2\pi)^{-n}\int e^{ix\cdot\xi}a^\flat(x,\xi)\widehat U(\xi)\,d\xi\), so \(W=T_aU\) in \(\mathbb R^n_+\). From (4.2), for \(x_n\geq0\),
\[
D_{x_j}\big(e^{ix\cdot\xi}a^\flat\big)=e^{ix\cdot\xi}\big(\xi_ja^\flat+(D_{x_j}a)^\flat\big)\ (j<n),\qquad
D_{x_n}\big(e^{ix\cdot\xi}a^\flat\big)=e^{ix\cdot\xi}\big(\xi_na^\flat+(D_{x_n}a)^\flat+\xi_n(D_{\xi_n}a)^\flat\big).
\tag{5.3}
\]
By induction, \(D_x^\beta(e^{ix\cdot\xi}a^\flat)=e^{ix\cdot\xi}\sum_\gamma\xi^\gamma c_\gamma^\flat\), a finite sum with \(|\gamma|\leq|\beta|\), where each \(c_\gamma\) is a constant times some \(\partial_x^\mu\partial_{\xi_n}^ia\in S^{m-i}_+\). Since \(1+|(\xi',x_n\xi_n)|\leq(1+x_n)(1+|\xi|)\), each term is at most \(|\xi|^{|\gamma|}p(c_\gamma)(1+x_n)^{m_+-\nu}(1+|\xi|)^{m_+}\), \(m_+=\max(m,0)\), for any \(\nu\). For the weight \(x'^{\alpha'}\) we integrate by parts in \(\xi'\), using \(x'^{\alpha'}e^{ix\cdot\xi}=D_{\xi'}^{\alpha'}e^{ix\cdot\xi}\); \(\xi'\)-derivatives of \(c_\gamma^\flat\) are compressions of \(\xi'\)-derivatives and obey the same bounds. For the weight \(x_n^{\alpha_n}\) we take \(\nu\geq\alpha_n+m_+\). Thus
\[
\sup_{x\in\overline{\mathbb R}{}^n_+}|x^\alpha D^\beta W(x)|\leq p(a)\,p'(U)
\]
with \(p\) a seminorm of \(S^m_+\) and \(p'\) a Schwartz seminorm. The same bounds justify differentiation under the integral, and the integrands are continuous up to \(x_n=0\); so \(W\in C^\infty(\overline{\mathbb R}{}^n_+)\), and \(W|_{\mathbb R^n_+}\in\overline{\mathcal S}(\mathbb R^n_+)\) by Lemma 3.2(c). By Proposition 4.3, \(W|_{\mathbb R^n_+}\) depends only on \(U|_{\mathbb R^n_+}\). Taking the infimum over all extensions gives \(q_{\alpha,\beta}(T_au)\leq p(a)\bar p'(u)\) with the quotient seminorm \(\bar p'\), and Lemma 3.2(a) turns this into joint continuity.

(b) For \(U\in\mathcal S\) and \(x_n>0\), differentiation under the integral gives \(D_jT_aU=\operatorname{Op}(\xi_ja^\flat+D_{x_j}(a^\flat))U\), while \(T_aD_jU=\operatorname{Op}(a^\flat\xi_j)U\). Hence \([T_a,D_j]=-\operatorname{Op}(D_{x_j}(a^\flat))=i\operatorname{Op}(\partial_{x_j}(a^\flat))\). For \(j<n\), \(\partial_{x_j}(a^\flat)=(\partial_{x_j}a)^\flat\). For \(j=n\), \(\partial_{x_n}(a^\flat)=(\partial_{x_n}a)^\flat+\xi_n(\partial_{\xi_n}a)^\flat\), and \(\operatorname{Op}(c^\flat\xi_n)=T_cD_n\). Next, \(\widehat{x_jU}=-D_{\xi_j}\widehat U\); integrating by parts in \(\xi_j\) gives \(T_a(x_jU)=(2\pi)^{-n}\int D_{\xi_j}(e^{ix\cdot\xi}a^\flat)\widehat U\,d\xi=x_jT_aU+\operatorname{Op}(D_{\xi_j}(a^\flat))U\), so \([T_a,x_j]=-i\operatorname{Op}(\partial_{\xi_j}(a^\flat))\). For \(j<n\) this is \(-iT_{\partial_{\xi_j}a}\). For \(j=n\), \(\partial_{\xi_n}(a^\flat)=x_n(\partial_{\xi_n}a)^\flat\), and the factor \(x_n\) stands on the left. The symbols on the right are lacunary, so the identities pass to \(\overline{\mathcal S}(\mathbb R^n_+)\).

(c) By (5.3), \(D^k_{x_n}(e^{ix\cdot\xi}a^\flat)=e^{ix\cdot\xi}(\xi_n+D_{x_n})^ka^\flat\) for \(x_n\geq0\). Regard \(a\) as a function of \((x,\xi',\zeta)\), with \(\zeta=x_n\xi_n\) in the last slot and \(\xi_n\) as a parameter. Then \(D_{x_n}(a^\flat)=[(D_{x_n}+\xi_nD_\zeta)a]^\flat\), and \(D_{x_n}\), \(\xi_nD_\zeta\) commute; so \(D^\ell_{x_n}(a^\flat)=\sum_i\binom\ell i\xi_n^i(D^{\ell-i}_{x_n}D^i_\zeta a)^\flat\). At \(x_n=0\) (where \(\zeta=0\)),
\[
(\xi_n+D_{x_n})^ka^\flat\big|_{x_n=0}=\sum_{\ell}\binom k\ell\xi_n^{k-\ell}\sum_{i\leq\ell}\binom\ell i\xi_n^i\big(D^{\ell-i}_{x_n}D^i_{\xi_n}a\big)(x',0,\xi',0).
\]
The power \(\xi_n^j\) occurs for \(j=k-\ell+i\), and \(\binom k{k-j+i}\binom{k-j+i}i=\binom kj\binom ji\). So \(D^k_n(T_aU)(x',0)=\sum_j\binom kj(2\pi)^{-n}\int e^{ix'\cdot\xi'}a_{kj}(x',\xi')\xi_n^j\widehat U(\xi)\,d\xi\), and \((2\pi)^{-1}\int\xi_n^j\widehat U(\xi',\xi_n)d\xi_n\) is the Fourier transform in \(x'\) of \(D_n^jU(\cdot,0)\). This is (5.2). The symbol \(D^i_{\xi_n}D^{k-j}_{x_n}a\) lies in \(S^{m-i}_+\), and its restriction to \(x_n=0,\xi_n=0\) lies in \(S^{m-i}(\mathbb R^{n-1}\times\mathbb R^{n-1})\).

(d) This is read off from (5.2). If all jets of \(u\) vanish, those of \(T_au\) vanish too; the zero extension of \(T_au\) is then smooth, with all weighted derivatives bounded, hence in \(\dot{\mathcal S}(\overline{\mathbb R}{}^n_+)\). \(\square\)

Formula (5.2) is the purpose of the construction: the normal derivatives of the output at the boundary are obtained by letting pseudodifferential operators on the boundary act on normal derivatives of the input of the same or lower order. Proposition 2.1(d) is the case \(k=0\) for differential operators.

**Example 5.2** (The factor \(x_n\) in the normal commutator). Take \(\theta\in C_0^\infty(\mathbb R)\) with \(\theta=1\) near 0, and \(a(x,\xi)=\theta(x_n)\xi_n\). This symbol lies in \(S^1_{\mathrm{la}}\), because its normal Fourier transform is supported at \(t=0\). Here \(T_a=\theta(x_n)x_nD_n\), and \([T_a,x_n]u=\theta(x_n)x_nD_n(x_nu)-x_n\theta(x_n)x_nD_nu=-i\theta(x_n)x_nu\), while \(T_{\partial_{\xi_n}a}=\theta(x_n)\). So \([T_a,x_n]=-i\,x_nT_{\partial_{\xi_n}a}\), as (5.1) says, and there is no term \(-iT_{\partial_{\xi_n}a}=-i\theta(x_n)\) without the factor \(x_n\).

### Composition with totally characteristic derivatives

Composing \(T_c\) on the right with a totally characteristic differential operator gives again an operator of the class, with an exact formula for its symbol.

**Lemma 5.3** (Composition with totally characteristic derivatives). For \(c\in S^\mu_{\mathrm{la}}\), on \(\overline{\mathcal S}(\mathbb R^n_+)\),
\[
T_cD_j=T_{\xi_jc}\ (j<n),\qquad T_c\,x_nD_n=T_{\xi_n(1-i\partial_{\xi_n})c},\qquad T_c\,D_nx_n=T_{(\xi_n-i-i\xi_n\partial_{\xi_n})c},
\tag{5.4}
\]
and more generally
\[
T_c\,x_n^kD_n^kD'^{\beta'}=T_{\xi'^{\beta'}\xi_n^k(1-i\partial_{\xi_n})^kc}.
\tag{5.5}
\]
**Proof.** For \(j<n\), \(T_cD_j=\operatorname{Op}(c^\flat\xi_j)\) and \(c^\flat\xi_j=(\xi_jc)^\flat\). By (5.1), \(T_cx_n=x_nT_{(1-i\partial_{\xi_n})c}\), so \(T_cx_n^k=x_n^kT_{(1-i\partial_{\xi_n})^kc}\). Moreover \(x_n^kT_gD_n^k=\operatorname{Op}(x_n^k\xi_n^kg^\flat)=T_{\xi_n^kg}\), because \(x_n^k\xi_n^kg^\flat=(\xi_n^kg)^\flat\). Together these give (5.5) and the first two identities in (5.4). The third identity in (5.4) follows from \(D_nx_n=x_nD_n-i\). \(\square\)

