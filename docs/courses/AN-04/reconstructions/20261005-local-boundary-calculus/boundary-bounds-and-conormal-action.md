# Boundary operator bounds, conormal action and the residual obstruction

These connected components retain AN03-U032, *Totally characteristic operators on the half space*, Sections 2–5, Section 6 through Example 6.7, and Sections 7–13. Original author: Claude Opus 5.5 (Anthropic), September 2026; editorial additions: Codex, September 2026. Both were dedicated to the public domain (CC0). Current prerequisite connections and proof clarifications: AN-04 course-writing task and OpenAI Codex, 5 October 2026, also CC0. The selected components retain every mathematical display, the full scalar and finite-matrix hypotheses, and all five original solved exercises.

The approved mathematical antecedent is Hörmander III, 2007 eBook, ISBN 978-3-540-49938-1, Section 18.3. Its use and ordinary citation are valid. Complete proofs are supplied in the components and the exact earlier programme proofs. The earlier linked components retain their individual licences.

The four components, in proof order, are [Boundary tests, lacunary symbols and all normal jets](boundary-tests-and-lacunary-symbols.md), [Resolved corner kernels and their exact inverse](resolved-corner-kernels.md), [Boundary adjoints, complete composition and distributional action](boundary-adjoints-composition-and-distributions.md), [Boundary operator bounds, conormal action and the residual obstruction](boundary-bounds-and-conormal-action.md). Original section and equation numbers are retained across them. Sections 6.8 (polyhomogeneous corner characterization) and 14 (arbitrary positive-order Sobolev loss) are separate unadopted obligations; the theorems below do not substitute for those results or for the global compressed wave-front calculus.

Use the [test and symbol component](boundary-tests-and-lacunary-symbols.md), the [corner kernel bound](resolved-corner-kernels.md), and the full [adjoint, composition and distributional action](boundary-adjoints-composition-and-distributions.md). The half-space Hilbert companion also supplies the exact closed-subspace projection and full Hilbert antidual representation used in Proposition 10.2. Its one-sided multiplier is a later prerequisite, not a replacement for the order-zero argument below.

## 10. Boundedness on \(L^2\), Sobolev and Besov spaces

Operators of order 0 are bounded on \(L^2(\mathbb R^n_+)\). We prove this first. Then we extend it to Sobolev spaces of integer order, using the commutator identities and duality, and to all real orders and all Besov exponents by interpolation.

### Boundedness on \(L^2\)

**Theorem 10.1** (Boundedness on \(L^2\)). If \(a\in S^0_{\mathrm{la}}\), then \(T_a\) extends to a bounded operator on \(L^2(\mathbb R^n_+)\), with norm bounded in terms of finitely many seminorms of \(a\).

**Proof.** *Step A (order \(-n-2\)).* For \(a\in S^{-n-2}_{\mathrm{la}}\), Proposition 6.4 and the full Lebesgue Schur proof B3 linked in Section 1, give \(\|T_au\|_{L^2(\mathbb R^n_+)}\leq C\|u\|_{L^2(\mathbb R^n_+)}\) for \(u\in\overline{\mathcal S}(\mathbb R^n_+)\), since \(T_au(x)=\int_{\mathbb R^n_+}K_a(x,y)u(y)dy\). Restrictions of Schwartz functions are dense in \(L^2(\mathbb R^n_+)\).

*Step B (doubling).* Suppose every operator with symbol in \(S^{-2k}_{\mathrm{la}}\) is bounded, and let \(a\in S^{-k}_{\mathrm{la}}\). For \(u\in\overline{\mathcal S}(\mathbb R^n_+)\), Theorems 7.3 and 8.1 give \(\|T_au\|^2=(T_{a^\dagger}T_au,u)=(T_cu,u)\) with \(c=a^\dagger\#a\in S^{-2k}_{\mathrm{la}}\) (writing \(\#\) for the composition symbol of Theorem 8.1). So \(\|T_au\|^2\leq\|T_c\|\,\|u\|^2\).

*Step C.* By Steps A–B, operators with symbols in \(S^{-k}_{\mathrm{la}}\) are bounded for \(k\geq(n+2)/2\), then for \(k\geq(n+2)/4\), and so on; after finitely many steps, for every \(k>0\).

*Step D (order 0).* Let \(a\in S^0_{\mathrm{la}}\) and \(M>\sup|a|\). The function \(c_0=(M^2-|a|^2)^{1/2}-M\) lies in \(S^0_+\): it is \(G(a,\overline a)\) with \(G\) smooth on a neighbourhood of the closed range and \(G(0)=0\), so by the chain rule every derivative is a sum of products containing at least one derivative of \(a\) (or \(a\) itself, since \(|G(a)|\leq C|a|\)), which gives the decay in \(x_n\). Let \(c=(c_0)_\rho\in S^0_{\mathrm{la}}\) (Lemma 4.4). For \(u\in\overline{\mathcal S}(\mathbb R^n_+)\),
\[
\|(M+T_c)u\|^2+\|T_au\|^2=M^2\|u\|^2+(T_ru,u),\qquad r=M(c+c^\dagger)+c^\dagger\#c+a^\dagger\#a,
\]
using \(2\operatorname{Re}(T_cu,u)=(T_{c+c^\dagger}u,u)\), \(\|T_cu\|^2=(T_{c^\dagger\#c}u,u)\) and \(\|T_au\|^2=(T_{a^\dagger\#a}u,u)\). The symbol \(r\) is lacunary. Its leading part, by Theorem 7.3(a) and (8.3), is \(2Mc_0+c_0^2+|a|^2\) modulo \(S^{-1}_+\) (recall \(c-c_0\in S^{-\infty}_+\) and \(c_0\) is real). This equals \((M+c_0)^2-M^2+|a|^2=0\). So \(r\in S^{-1}_{\mathrm{la}}\), \(T_r\) is bounded by Step C, and \(\|T_au\|^2\leq(M^2+\|T_r\|)\|u\|^2\). \(\square\)

**Matrix-valued symbols.** For \(a\) with values in \(L(\mathbb C^p,\mathbb C^q)\) take \(M>\sup\|a\|\) and
\[
 c_0=(M^2I_p-a^*a)^{1/2}-M I_p,
 \qquad
 C_M(A)=M\sum_{k=1}^\infty\binom{1/2}{k}
                (-A^*A/M^2)^k .
\]
The full square-root series, including its constant term, is
\[
 (M^2I_p-A^*A)^{1/2}
 =M\sum_{k=0}^\infty\binom{1/2}{k}(-A^*A/M^2)^k
 =M I_p+C_M(A).
\]
The square root is positive; \(c_0\) is its displayed difference from \(M I_p\). For \(\|A\|\le r<M\), the ordered power series and all its real and imaginary entry derivatives converge uniformly. Its first term is \(-A^*A/(2M)\); hence \(C_M(0)=0\) and its first derivative at zero is zero. The square root itself equals \(M I_p\) there. The product and chain rules, with the uniform derivative bounds on this ball, prove \(c_0\in S^0_+\). The leading symbol of \(r\), with all identities explicit, is
\[
 M(c_0+c_0^*)+c_0^*c_0+a^*a
 =(M I_p+c_0)^2-M^2I_p+a^*a=0 .
\]
Thus the same ordered proof applies, with the input and output vector dimensions retained.

For completeness the series assertion just used follows directly from
\(c_k=\binom{1/2}{k}(-1)^k\). Its recurrence is
\((k+1)c_{k+1}=(k-\tfrac12)c_k\), so \(|c_k|\le1\) and the
series \(y(z)=\sum_{k\ge0}c_kz^k\) converges absolutely for \(|z|<1\).
It satisfies \(2(1-z)y'=-y\), by comparing coefficients, and
\(y(0)=1\). Therefore the power series \(h=y^2\) satisfies
\((1-z)h'=-h\), \(h(0)=1\). Coefficient comparison gives
\(h=1-z\). For real \(0\le z<1\), continuity and \(y^2=1-z>0\)
give \(y(z)>0\).
For a matrix \(B=A^*A/M^2\) with \(\|B\|\le q<1\), absolute
operator-norm convergence permits multiplication of the two series and
gives \(y(B)^2=I-B\); real coefficients make \(y(B)\) self-adjoint.
The finite-dimensional spectral proof in the earlier stationary-phase
foundations identifies its eigenvalues as the positive numbers
\(y(\lambda)\). A derivative of order \(d\) in the real and imaginary
entries of \(A\) differentiates at most \(d\) factors in an ordered
product \(B^k\); on a fixed smaller ball it is bounded by a constant
times \(k^d q^{k-d}\) for \(k\ge d\), with finitely many initial
terms handled separately. The geometric series with this polynomial
factor converges. This proves every stated uniform derivative bound
and justifies the symbol chain rule for the finite-matrix square root.

The operator norm bound is linear in a finite collection of symbol
seminorms, despite the square-root construction. The finite doubling
argument needs only finitely many continuous composition and adjoint
seminorms. Choose a finite seminorm \(p(a)\) dominating all of them
and the supremum norm. If \(p(a)>0\), apply the construction to
\(a/p(a)\) with \(M=2\); every bound just proved is then uniform,
so \(\|T_a\|\le C p(a)\). If \(p(a)=0\), the supremum bound makes
\(a=0\). This proves the required homogeneous finite-seminorm
continuity, including the rectangular matrix case.

### Sobolev spaces on the half space

Let \(\dot H_{(s)}(\overline{\mathbb R}{}^n_+)=\{u\in H_{(s)}:\operatorname{supp}u\subset\overline{\mathbb R}{}^n_+\}\), with the norm of \(H_{(s)}\), and let \(\overline H_{(s)}(\mathbb R^n_+)\) be the space of restrictions, with \(\|u\|_{\overline H_{(s)}}=\inf\{\|U\|_{(s)}:U=u\text{ in }\mathbb R^n_+\}\). Define \(\dot B^s_{2,p}(\overline{\mathbb R}{}^n_+)\) in the same way as \(\dot H_{(s)}\). We prove the three facts about these spaces that we need.

**Proposition 10.2** (Sobolev spaces on the half space).

(a) \(C_0^\infty(\mathbb R^n_+)\) is dense in \(\dot H_{(s)}(\overline{\mathbb R}{}^n_+)\), and \(\overline{\mathcal S}(\mathbb R^n_+)\) is dense in \(\overline H_{(s)}(\mathbb R^n_+)\), for every real \(s\).

(b) The sesquilinear form \((u,v)=(2\pi)^{-n}\int\widehat u\,\overline{\widehat V}\,d\xi\), for \(u\in\dot H_{(s)}(\overline{\mathbb R}{}^n_+)\) and \(V\in H_{(-s)}\) any extension of \(v\in\overline H_{(-s)}(\mathbb R^n_+)\), is well defined. It identifies each of \(\dot H_{(s)}(\overline{\mathbb R}{}^n_+)\) and \(\overline H_{(-s)}(\mathbb R^n_+)\) isometrically with the antidual of the other. For \(u\in\dot{\mathcal S}(\overline{\mathbb R}{}^n_+)\), \(v\in\overline{\mathcal S}(\mathbb R^n_+)\) it equals \(\int_{\mathbb R^n_+}u\overline v\).

(c) Let \(k\geq0\) be an integer. For \(u\in\dot H_{(k)}(\overline{\mathbb R}{}^n_+)\), \(\|u\|_{(k)}^2=\sum_{|\alpha|\leq k}\frac{k!}{\alpha!(k-|\alpha|)!}\|D^\alpha u\|^2_{L^2}\). For \(u\in\overline H_{(k)}(\mathbb R^n_+)\), with \(N_k(u)^2=\sum_{|\alpha|\leq k}\|D^\alpha u\|^2_{L^2(\mathbb R^n_+)}\),
\[
C^{-1}N_k(u)\leq\|u\|_{\overline H_{(k)}}\leq C\,N_k(u).
\tag{10.1}
\]

**Proof.** (a) Let \(u\in\dot H_{(s)}\). The translates \(u_h=u(\cdot-he_n)\), supported in \(x_n\geq h\), converge to \(u\) in \(H_{(s)}\) as \(h\downarrow0\), by dominated convergence on the Fourier side. Mollifying with a kernel supported in \(\{|x|<h/2\}\) gives smooth functions supported in \(x_n\geq h/2\), converging in \(H_{(s)}\); these lie in \(H_{(\sigma)}\) for every \(\sigma\). Cutting off with \(\theta(x/R)\) converges in \(H_{(k)}\) for integers \(k\geq s\) (Leibniz' rule and dominated convergence), hence in \(H_{(s)}\). The second statement holds because \(\mathcal S\) is dense in \(H_{(s)}\) and restriction is continuous and onto.

(b) \(H_{(s)}\) and \(H_{(-s)}\) are each other's antiduals, isometrically, under this form: Cauchy–Schwarz with the weights \(\langle\xi\rangle^{\pm s}\), with equality for \(\widehat V=\langle\xi\rangle^{2s}\widehat u\). If \(V=0\) in \(\mathbb R^n_+\), then \((\varphi,V)=0\) for \(\varphi\in C_0^\infty(\mathbb R^n_+)\), and by (a) \((u,V)=0\) for all \(u\in\dot H_{(s)}\); so the form is well defined, and the annihilator of \(\dot H_{(s)}\) in \(H_{(-s)}\) is exactly \(\{V:V=0\text{ in }\mathbb R^n_+\}\). A continuous antilinear functional on the closed subspace \(\dot H_{(s)}\) extends with the same norm to \(H_{(s)}\) (orthogonal projection) and is then represented by some \(V\); two representatives differ by an element of the annihilator. So the antidual of \(\dot H_{(s)}\) is \(H_{(-s)}\) modulo the annihilator, that is \(\overline H_{(-s)}\), and the norms agree (the infimum over the coset is at most the norm of the norm-preserving extension). Conversely, a functional on the quotient \(\overline H_{(-s)}\) is a functional on \(H_{(-s)}\) vanishing on the annihilator; it is represented by \(u\in H_{(s)}\) orthogonal to the annihilator, and the double annihilator of the closed subspace \(\dot H_{(s)}\) is itself. The last statement is Plancherel.

(c) The identity is Plancherel with \((1+|\xi|^2)^k=\sum_{|\alpha|\leq k}\frac{k!}{\alpha!(k-|\alpha|)!}\xi^{2\alpha}\). For (10.1), any extension \(U\) gives \(N_k(u)^2\leq\sum_{|\alpha|\leq k}\|D^\alpha U\|^2_{L^2(\mathbb R^n)}\leq C\|U\|^2_{(k)}\). For the other inequality, let \(c_1,\ldots,c_{k+1}\) solve the Vandermonde system \(\sum_{l=1}^{k+1}c_l(-l)^i=1\), \(i=0,\ldots,k\) (the nodes \(-1,\ldots,-(k+1)\) are distinct). For \(u\in\overline{\mathcal S}(\mathbb R^n_+)\) let \(Eu=u\) on \(x_n\geq0\) and \(Eu(x)=\sum_lc_lu(x',-lx_n)\) for \(x_n<0\). The normal derivatives of order \(i\leq k\) from both sides agree on \(x_n=0\), so \(Eu\in C^k\), and \(\|D^\alpha Eu\|_{L^2(\mathbb R^n_-)}\leq\sum_l|c_l|l^{\alpha_n-1/2}\|D^\alpha u\|_{L^2(\mathbb R^n_+)}\). Hence \(\|u\|_{\overline H_{(k)}}\leq\|Eu\|_{(k)}\leq CN_k(u)\) on the dense set \(\overline{\mathcal S}(\mathbb R^n_+)\), and by continuity of both sides everywhere. \(\square\)

### Sobolev continuity at integer orders

**Theorem 10.3** (Integer orders). Let \(a\in S^0_{\mathrm{la}}\) and \(k\in\mathbb Z\). Then \(T_a\) is bounded on \(\dot H_{(k)}(\overline{\mathbb R}{}^n_+)\) and on \(\overline H_{(k)}(\mathbb R^n_+)\). These bounded operators are the restrictions of the maps of Theorem 9.1.

**Proof.** Iterating the commutator identities (5.1) gives, for every \(\alpha\),
\[
D^\alpha T_a=\sum_{|\beta|\leq|\alpha|}T_{c_{\alpha\beta}}D^\beta\quad\text{on }\overline{\mathcal S}(\mathbb R^n_+),\qquad c_{\alpha\beta}\in S^0_{\mathrm{la}},
\tag{10.2}
\]
each \(c_{\alpha\beta}\) being a constant-coefficient combination of \(x\)- and \(\xi_n\)-derivatives of \(a\), linear in \(a\). (Indeed \(D_jT_c=T_cD_j-iT_{\partial_{x_j}c}-i\delta_{jn}T_{\partial_{\xi_n}c}D_n\), and \(\partial_{\xi_n}c\in S^{-1}_{\mathrm{la}}\subset S^0_{\mathrm{la}}\).)

*Nonnegative \(k\), supported spaces.* For \(u\in\dot{\mathcal S}(\overline{\mathbb R}{}^n_+)\), \(T_au\in\dot{\mathcal S}(\overline{\mathbb R}{}^n_+)\) (Theorem 5.1(d)), and its derivatives on \(\mathbb R^n\) are the zero extensions of the derivatives in \(\mathbb R^n_+\). By Proposition 10.2(c), (10.2) and Theorem 10.1, \(\|T_au\|_{(k)}^2\leq C\sum_{|\alpha|\leq k}\|D^\alpha T_au\|^2_{L^2(\mathbb R^n_+)}\leq C'\sum_{|\beta|\leq k}\|D^\beta u\|^2_{L^2}\leq C''\|u\|^2_{(k)}\). By density (Proposition 10.2(a)) \(T_a\) extends to \(\dot H_{(k)}\).

*Nonnegative \(k\), restricted spaces.* For \(u\in\overline{\mathcal S}(\mathbb R^n_+)\), (10.1), (10.2) and Theorem 10.1 give \(\|T_au\|_{\overline H_{(k)}}\leq CN_k(T_au)\leq C'N_k(u)\leq C''\|u\|_{\overline H_{(k)}}\); then use density.

*Negative \(k\).* Let \(k\geq0\). For \(u\in\overline{\mathcal S}(\mathbb R^n_+)\) and \(v\in\dot{\mathcal S}(\overline{\mathbb R}{}^n_+)\), Theorem 7.3 gives \((T_au,v)=(u,T_{a^\dagger}v)\), so \(|(T_au,v)|\leq\|u\|_{\overline H_{(-k)}}\|T_{a^\dagger}v\|_{(k)}\leq C\|u\|_{\overline H_{(-k)}}\|v\|_{(k)}\) by the supported case for \(a^\dagger\in S^0_{\mathrm{la}}\). By Proposition 10.2(a),(b), \(\|T_au\|_{\overline H_{(-k)}}\leq C\|u\|_{\overline H_{(-k)}}\), and density extends \(T_a\). In the same way, for \(u\in\dot{\mathcal S}(\overline{\mathbb R}{}^n_+)\) and \(v\in\overline{\mathcal S}(\mathbb R^n_+)\), \(|(T_au,v)|\leq\|u\|_{(-k)}\|T_{a^\dagger}v\|_{\overline H_{(k)}}\leq C\|u\|_{(-k)}\|v\|_{\overline H_{(k)}}\), which bounds \(T_a\) on \(\dot H_{(-k)}\).

*Consistency.* The maps of Theorem 9.1 are weakly continuous, the spaces here embed continuously into \(\dot{\mathcal S}'(\overline{\mathbb R}{}^n_+)\) or \(\overline{\mathcal S'}(\mathbb R^n_+)\), and the two definitions agree on the dense subspaces used above. \(\square\)

### All real orders and all Besov exponents

**Lemma 10.4** (A mollifier supported in the half space). Let \(\phi\in C_0^\infty(\mathbb R^n_+)\) with \(\int\phi=1\), and put \(\psi=2\phi-\phi*\phi\). Then \(\psi\in C_0^\infty(\mathbb R^n_+)\), \(\widehat\psi=1-(1-\widehat\phi)^2\), and for all \(\zeta\in\mathbb R^n\)
\[
|\widehat\psi(\zeta)|\leq C\min(1,|\zeta|^{-2}),\qquad|1-\widehat\psi(\zeta)|\leq C\min(1,|\zeta|^2).
\tag{10.3}
\]
With \(\psi_\varepsilon(x)=\varepsilon^{-n}\psi(x/\varepsilon)\) and \(|s|\leq\tfrac12\),
\[
\int_0^1|\widehat\psi(\varepsilon\xi)|^2\varepsilon^{1-2s}d\varepsilon\leq C\langle\xi\rangle^{2s-2},\qquad
\int_0^1|1-\widehat\psi(\varepsilon\xi)|^2\varepsilon^{-3-2s}d\varepsilon\leq C\langle\xi\rangle^{2s+2}.
\tag{10.4}
\]

**Proof.** \(\operatorname{supp}(\phi*\phi)\subset\operatorname{supp}\phi+\operatorname{supp}\phi\subset\mathbb R^n_+\). \(\widehat\psi\) is a Schwartz function, and \(|1-\widehat\phi(\zeta)|\leq C\min(1,|\zeta|)\) since \(\widehat\phi(0)=1\); this gives (10.3). For (10.4) with \(|\xi|\leq1\): the first integral is at most \(C\int_0^1\varepsilon^{1-2s}d\varepsilon<\infty\) (as \(1-2s\geq0\)), and the second at most \(C|\xi|^4\int_0^1\varepsilon^{1-2s}d\varepsilon\). For \(|\xi|\geq1\) substitute \(u=\varepsilon|\xi|\) and extend to \((0,\infty)\): the integrals become \(|\xi|^{2s-2}\int_0^\infty\min(1,u^{-4})u^{1-2s}du\) and \(|\xi|^{2s+2}\int_0^\infty\min(1,u^4)u^{-3-2s}du\), which converge because \(1-2s>-1\), \(-3-2s<-1\) and \(-3+4-2s>-1\). \(\square\)

The quadratic vanishing of \(1-\widehat\psi\) at 0 is needed for \(s\geq0\), and it cannot be had with \(\psi\geq0\): see Example 10.5. That is why \(\psi\) is built from \(\phi\) in this way.

**Example 10.5** (A positive mollifier is not good enough). Let \(0\leq\phi\in C_0^\infty(\mathbb R^n_+)\) with \(\int\phi=1\). Its first moment \(m=\int x\phi\,dx\) has \(m_n>0\), and \(\widehat\phi(\zeta)=1-i\zeta\cdot m+O(|\zeta|^2)\). For \(\xi=\lambda e_n\) we get \(|1-\widehat\phi(\varepsilon\xi)|\geq m_n\varepsilon\lambda/2\) when \(\varepsilon\lambda\) is small, so \(\int_0^1|1-\widehat\phi(\varepsilon\xi)|^2\varepsilon^{-3-2s}d\varepsilon=\infty\) for \(s\geq0\). So the second inequality of (10.4) fails for \(\phi\), and it fails for every \(\psi\geq0\) supported in \(\mathbb R^n_+\): quadratic vanishing forces \(\int x_n\psi=0\), which is impossible when \(\psi\geq0\) and \(x_n>0\) on the support. The function \(\psi=2\phi-\phi*\phi\) of Lemma 10.4 takes negative values.

**Theorem 10.6** (Sobolev and Besov continuity). Let \(a\in S^0_{\mathrm{la}}\), \(\sigma\in\mathbb R\) and \(1\leq p\leq\infty\). Then \(T_a\) is bounded on \(\dot B^\sigma_{2,p}(\overline{\mathbb R}{}^n_+)\). In particular:

1. (\(p=2\)) \(T_a\) is bounded on \(\dot H_{(\sigma)}(\overline{\mathbb R}{}^n_+)\), and, by duality with \(a^\dagger\) (Proposition 10.2(b)), on \(\overline H_{(\sigma)}(\mathbb R^n_+)\), for every real \(\sigma\).
2. (\(p=\infty\)) \(T_a\) is bounded on \(\dot B^\sigma_{2,\infty}(\overline{\mathbb R}{}^n_+)\).

**First proof, for \(p=2\) (continuous interpolation).** Write \(\sigma=k+s\) with \(k\in\mathbb Z\), \(|s|\leq\tfrac12\), and let \(u\in\dot H_{(\sigma)}(\overline{\mathbb R}{}^n_+)\). The pieces \(\psi_\varepsilon*u\) and \(u-\psi_\varepsilon*u\) are supported in \(\overline{\mathbb R}{}^n_+\), because \(\operatorname{supp}\psi\subset\mathbb R^n_+\); they lie in \(\dot H_{(k+1)}\) and \(\dot H_{(k-1)}\). By (10.4) and Fubini,
\[
\int_0^1\Big(\|\psi_\varepsilon*u\|^2_{(k+1)}\varepsilon^{1-2s}+\|u-\psi_\varepsilon*u\|^2_{(k-1)}\varepsilon^{-3-2s}\Big)d\varepsilon\leq C\|u\|^2_{(\sigma)} .
\]
Put \(v_\varepsilon=T_a(\psi_\varepsilon*u)\), \(w_\varepsilon=T_a(u-\psi_\varepsilon*u)\) and \(U=T_au=v_\varepsilon+w_\varepsilon\). By Theorem 10.3 the same integral with \(v_\varepsilon,w_\varepsilon\) in place of the two pieces is at most \(C'\|u\|^2_{(\sigma)}\). The distribution \(U\) already belongs to \(H_{(k-1)}\):
the input does by the continuous embedding and the compatible integer
operator acts there. Thus its Fourier transform is an actual locally
square-integrable function. For each \(\varepsilon\), the Fourier
identity \(U=v_\varepsilon+w_\varepsilon\) holds almost everywhere;
the integrals below have jointly measurable Fourier representatives.
Indeed on any compact interval of positive \(\varepsilon\), the
Schwartz multiplier estimates and dominated convergence make
\(\varepsilon\mapsto\psi_\varepsilon*u\) norm continuous in
\(H_{(k+1)}\), and its complement norm continuous in \(H_{(k-1)}\).
The bounded integer operators preserve these continuities. Uniform
step approximations on that interval therefore converge in the
corresponding weighted product \(L^2\) spaces. Choose a subsequence
whose successive \(L^2\) errors are summable; on each bounded frequency
set, Cauchy--Schwarz and Fubini make the sum of their absolute
differences finite almost everywhere. Its measurable limit represents
the norm-continuous family. Exhausting the positive scale intervals
and frequency balls gives the required joint representatives and
justifies every use of Fubini below.
If \(\tfrac12<\varepsilon\langle\xi\rangle<1\), then \(|\widehat U(\xi)|^2\leq C\big(|\widehat{v_\varepsilon}(\xi)|^2(\varepsilon\langle\xi\rangle)^{2k+2}+|\widehat{w_\varepsilon}(\xi)|^2(\varepsilon\langle\xi\rangle)^{2k-2}\big)\). Multiply by \(\varepsilon^{-1-2\sigma}\) and integrate over these \(\varepsilon\) (all in \((0,1]\)): the left side becomes \(c_\sigma\langle\xi\rangle^{2\sigma}|\widehat U(\xi)|^2\) with \(c_\sigma=\int_{1/2}^1u^{-1-2\sigma}du>0\), and the right side is at most the integrand of the previous display, evaluated for \(v_\varepsilon,w_\varepsilon\) at the frequency \(\xi\). Integrating in \(\xi\) gives \(\|U\|^2_{(\sigma)}\leq C''\|u\|^2_{(\sigma)}\). \(\square\)

**Second proof, for all \(p\) (dyadic form).** Let \(\sigma=k+s\) as before and \(u\in\dot B^\sigma_{2,p}(\overline{\mathbb R}{}^n_+)\). Since \(B^\sigma_{2,p}\subset H_{(\sigma-\delta)}\) for every \(\delta>0\) (the squares \(2^{2j(\sigma-\delta)}\|\Pi_ju\|^2_{L^2}\) are at most \(2^{-2j\delta}\) times the square of the norm in \(B^\sigma_{2,p}\), so they are summable) and \(s>-1\), \(u\in\dot H_{(k-1)}\). For each \(j\geq0\) put \(\varepsilon_j=2^{-j}\), \(v_j=\psi_{\varepsilon_j}*u\in\dot H_{(k+1)}\), \(w_j=u-v_j\in\dot H_{(k-1)}\). Then \(T_au=T_av_j+T_aw_j\) (the maps of Theorems 9.1 and 10.3 agree), and, since \(\langle\xi\rangle\) is comparable to \(2^j\) on \(A_j\),
\[
2^{j\sigma}\|\Pi_jT_au\|_{L^2}\leq C\big(2^{j(s-1)}\|T_av_j\|_{(k+1)}+2^{j(s+1)}\|T_aw_j\|_{(k-1)}\big)\leq C'\big(2^{j(s-1)}\|v_j\|_{(k+1)}+2^{j(s+1)}\|w_j\|_{(k-1)}\big).
\]
On \(A_l\), \(|\widehat\psi(2^{-j}\xi)|\leq C\min(1,2^{2(j-l)})\) and \(|1-\widehat\psi(2^{-j}\xi)|\leq C\min(1,2^{2(l-j)})\) by (10.3). With \(y_l=2^{l\sigma}\|\Pi_lu\|_{L^2}\) this gives
\[
2^{j(s-1)}\|v_j\|_{(k+1)}\leq C\Big(\sum_l\big[2^{(j-l)(s-1)}\min(1,2^{2(j-l)})\big]^2y_l^2\Big)^{1/2},\quad
2^{j(s+1)}\|w_j\|_{(k-1)}\leq C\Big(\sum_l\big[2^{(j-l)(s+1)}\min(1,2^{2(l-j)})\big]^2y_l^2\Big)^{1/2}.
\]
For \(|s|\leq\tfrac12\) both brackets are at most \(2^{-|j-l|/2}\): for \(j\geq l\) they are \(2^{(j-l)(s-1)}\) and \(2^{(j-l)(s-1)}\); for \(j<l\) they are \(2^{(j-l)(s+1)}\) and \(2^{(j-l)(s+1)}\). Since \((\sum_lc_ly_l^2)^{1/2}\leq\sum_lc_l^{1/2}y_l\), we get \(x_j:=2^{j\sigma}\|\Pi_jT_au\|_{L^2}\leq C\sum_l2^{-|j-l|/2}y_l\). Convolution with the summable sequence \(2^{-|m|/2}\) is bounded on \(\ell^p(\mathbb Z)\) for every \(1\leq p\leq\infty\), by the triangle inequality for translates (Section 1), so \(\|T_au\|_{B^\sigma_{2,p}}\leq C\|u\|_{B^\sigma_{2,p}}\). Finally \(T_au\) is supported in \(\overline{\mathbb R}{}^n_+\). \(\square\)

The dyadic proof treats all \(1\leq p\leq\infty\) at once and contains the case \(p=2\).

## 11. Conormal distributions are preserved

Let \(\mathcal P_b\) be the set of operators \(P=\sum_{|\alpha|\leq M}c_\alpha(x)x_n^{\alpha_n}D^\alpha\) with \(c_\alpha\in C^\infty_b(\mathbb R^n)\) and any \(M\). For \(\kappa\in\mathbb R\) put
\[
\mathcal A^\kappa=\big\{u\in\dot{\mathcal S}'(\overline{\mathbb R}{}^n_+):\ Pu\in B^\kappa_{2,\infty}(\mathbb R^n)\text{ for every }P\in\mathcal P_b\big\},
\tag{11.1}
\]
the distributions supported in the closed half space that are conormal to the boundary uniformly at infinity.

**Lemma 11.1** (Exact compositions). Let \(a\in S^m_{\mathrm{la}}\).

(a) If \(P\in\mathcal P_b\) has order \(\leq M\), then \(PT_a=T_{p\star a}\) on \(\overline{\mathcal S}(\mathbb R^n_+)\), where
\[
p\star a=\sum_\alpha c_\alpha(x)\prod_{j<n}(\xi_j+D_{x_j})^{\alpha_j}\;q_{\alpha_n}\big(\xi_n+x_nD_{x_n}+\xi_nD_{\xi_n}\big)\,a\in S^{m+M}_{\mathrm{la}},
\tag{11.2}
\]
with \(q_k\) from (2.1).

(b) Let \(M\geq0\) be even and \(Q(\xi)=|\xi|^M\). Then \(T_Q:=\sum_{|\beta|=M/2}\frac{(M/2)!}{\beta!}D'^{2\beta'}x_n^{2\beta_n}D_n^{2\beta_n}\in\mathcal P_b\) is the operator with compressed symbol \(Q^\flat=(|\xi'|^2+x_n^2\xi_n^2)^{M/2}\), and for \(f\in S^\mu_{\mathrm{la}}\)
\[
T_fT_Q=T_{f\circ Q},\qquad f\circ Q=\sum_{|\beta|=M/2}\frac{(M/2)!}{\beta!}\,\xi'^{2\beta'}\xi_n^{2\beta_n}(1-i\partial_{\xi_n})^{2\beta_n}f\in S^{\mu+M}_{\mathrm{la}},\qquad f\circ Q-Qf\in S^{\mu+M-1}_+ .
\tag{11.3}
\]

(c) If \(c\in S^\mu_{\mathrm{la}}\) and \(M\geq0\) is an even integer with \(M>\mu\), then \(c=f\circ Q+g\) with \(f,g\in S^0_{\mathrm{la}}\).

**Proof.** (a) By (5.3), \(D_{x_j}(e^{ix\cdot\xi}c^\flat)=e^{ix\cdot\xi}((\xi_j+D_{x_j})c)^\flat\) for \(j<n\), and \(x_nD_{x_n}(e^{ix\cdot\xi}c^\flat)=e^{ix\cdot\xi}((\xi_n+x_nD_{x_n}+\xi_nD_{\xi_n})c)^\flat\), because \(x_n\xi_nc^\flat=(\xi_nc)^\flat\). So \(D_jT_c=T_{(\xi_j+D_{x_j})c}\) and \(x_nD_nT_c=T_{(\xi_n+x_nD_{x_n}+\xi_nD_{\xi_n})c}\), and \(c_\alpha(x)T_c=T_{c_\alpha c}\). These symbol operators preserve lacunarity and raise the order by at most one (the factor \(x_n\) is absorbed by the decay in \(x_n\)). By (2.1), \(x_n^{\alpha_n}D^\alpha=D'^{\alpha'}q_{\alpha_n}(x_nD_n)\), which gives (11.2).

(b) Expanding \((|\xi'|^2+x_n^2\xi_n^2)^{M/2}\) and quantizing on the left gives \(\operatorname{Op}(Q^\flat)=\sum\frac{(M/2)!}{\beta!}x_n^{2\beta_n}D^{2\beta}=T_Q\). By (5.5), \(T_fD'^{2\beta'}x_n^{2\beta_n}D_n^{2\beta_n}=T_{\xi'^{2\beta'}\xi_n^{2\beta_n}(1-i\partial_{\xi_n})^{2\beta_n}f}\). Expanding \((1-i\partial_{\xi_n})^{2\beta_n}f=f+(\text{terms with }\partial_{\xi_n})\) shows \(f\circ Q-Qf\in S^{\mu+M-1}_+\).

(c) Let \(\chi\in C_0^\infty(\mathbb R^n)\) equal 1 near 0; then \((1-\chi)/Q\in S^{-M}\). Put \(g_0=c\). Given \(g_i\in S^{\mu-i}_{\mathrm{la}}\), put \(f_i=\big((1-\chi)g_i/Q\big)_\rho\in S^{\mu-i-M}_{\mathrm{la}}\) (Lemma 4.4) and \(g_{i+1}=g_i-f_i\circ Q\). Then
\[
g_{i+1}=\chi g_i+\Big(\frac{(1-\chi)g_i}Q-f_i\Big)Q-\big(f_i\circ Q-f_iQ\big)\in S^{\mu-i-1}_{\mathrm{la}},
\]
since the first two terms are in \(S^{-\infty}_+\) and the last is in \(S^{\mu-i-1}_+\) by (b); it is lacunary as a combination of lacunary symbols. After \(N\) steps with \(\mu-N\leq0\), \(c=\big(\sum_{i<N}f_i\big)\circ Q+g_N\), with \(\sum f_i\in S^{\mu-M}_{\mathrm{la}}\subset S^0_{\mathrm{la}}\) and \(g_N\in S^0_{\mathrm{la}}\). \(\square\)

**Theorem 11.2** (Conormal distributions are preserved). Let \(\kappa\in\mathbb R\) and \(k=-\kappa-n/4\).

(a) \(I^k(\mathbb R^n,\partial\mathbb R^n_+)\cap\dot{\mathcal E}'(\overline{\mathbb R}{}^n_+)\subset\mathcal A^\kappa\subset I^k(\mathbb R^n,\partial\mathbb R^n_+)\cap\dot{\mathcal S}'(\overline{\mathbb R}{}^n_+)\).

(b) For every real \(m\) and every \(a\in S^m_{\mathrm{la}}\), \(T_a\mathcal A^\kappa\subset\mathcal A^\kappa\).

(c) If \(a\in S^m_{\mathrm{la}}\) and \(u\in I^k(\mathbb R^n,\partial\mathbb R^n_+)\cap\dot{\mathcal E}'(\overline{\mathbb R}{}^n_+)\), then \(T_au\in I^k(\mathbb R^n,\partial\mathbb R^n_+)\cap\dot{\mathcal S}'(\overline{\mathbb R}{}^n_+)\).

**Proof.** (a) Let \(u\in I^k\cap\dot{\mathcal E}'(\overline{\mathbb R}{}^n_+)\) and \(P\in\mathcal P_b\). By (2.1), \(P=\sum c_\alpha D'^{\alpha'}q_{\alpha_n}(x_nD_n)\) is a sum of words in the tangent operators \(D_j\) (\(j<n\)) and \(x_nD_n\), times \(C^\infty_b\) functions. By the definition of conormal distributions (Section 1), these words map \(u\) into \(B^{\kappa}_{2,\infty,\mathrm{loc}}\), since \(\kappa=-k-n/4\); and multiplication by \(c_\alpha\) preserves that space. \(Pu\) has compact support, so \(Pu=\vartheta Pu\in B^\kappa_{2,\infty}\) with \(\vartheta\in C_0^\infty\) equal to 1 near \(\operatorname{supp}u\). For the second inclusion, let \(L_1,\ldots,L_N\) be first-order operators on \(\mathbb R^n\) whose principal symbols vanish on \(N^*(\partial\mathbb R^n_+)\), and \(\vartheta\in C_0^\infty(\mathbb R^n)\). By Hadamard's lemma and the commutation argument of Proposition 2.1, \(\vartheta L_1\cdots L_N\) is an element of \(\mathcal P_b\) (with compactly supported coefficients). So \(\vartheta L_1\cdots L_Nu\in B^\kappa_{2,\infty}\) for \(u\in\mathcal A^\kappa\), which is the definition of \(I^k(\mathbb R^n,\partial\mathbb R^n_+)\).

(b) Let \(u\in\mathcal A^\kappa\) and \(P\in\mathcal P_b\) of order \(M_P\). By Lemma 11.1(a), \(PT_a=T_c\) with \(c=p\star a\in S^{m+M_P}_{\mathrm{la}}\). Choose an even \(M>m+M_P\), \(M\geq0\), and write \(c=f\circ Q+g\) as in Lemma 11.1(c). Then \(PT_a=T_fT_Q+T_g\). These identities hold on \(\overline{\mathcal S}(\mathbb R^n_+)\), hence on \(\dot{\mathcal S}'(\overline{\mathbb R}{}^n_+)\): both sides are weakly continuous and agree on \(C_0^\infty(\mathbb R^n_+)\) (Theorem 9.1(e)). They agree there because every element of \(\mathcal P_b\) commutes with extension by zero: if \(w\in\overline{\mathcal S}(\mathbb R^n_+)\) has zero extension \(w_0\), then \(x_n^{\alpha_n}D^\alpha w_0\) and the zero extension of \(x_n^{\alpha_n}D^\alpha w\) differ by terms \(x_n^{\alpha_n}\delta^{(l)}(x_n)\otimes g_l(x')\) with \(l<\alpha_n\), and these vanish. With Theorem 9.1(b), both sides therefore send \(\varphi\in C_0^\infty(\mathbb R^n_+)\) to the zero extension of the same function. Now \(T_Qu\in B^\kappa_{2,\infty}\) because \(T_Q\in\mathcal P_b\), it is supported in \(\overline{\mathbb R}{}^n_+\), and \(u\in B^\kappa_{2,\infty}\) (take \(P=1\)). By Theorem 10.6 with \(p=\infty\), \(T_f\) and \(T_g\) are bounded on \(\dot B^\kappa_{2,\infty}(\overline{\mathbb R}{}^n_+)\). So \(PT_au\in B^\kappa_{2,\infty}\) for every \(P\in\mathcal P_b\), that is, \(T_au\in\mathcal A^\kappa\).

(c) follows from (a) and (b). \(\square\)

The order \(m\) of \(a\) plays no role: conormal distributions are infinitely regular in the directions of the totally characteristic operators, so any loss of order can be moved onto the elliptic b-operator \(T_Q\), which conormality controls. The exact formulas (11.2)–(11.3) do not need the coefficients of \(P\) to decay in \(x_n\), as the composition theorem would; this is what allows the global class \(\mathcal A^\kappa\) in (b). Without conormality nothing of this kind holds; see Example 11.3.

**Example 11.3** (Besov regularity alone is not preserved at positive order). Let \(a\) be as in Example 8.3, of order 1, and \(u=\delta(x_n-\tfrac32)\otimes\varphi(x')\) with \(0\neq\varphi\in C_0^\infty(\mathbb R^{n-1})\). Then \(u\in\dot B^{-1/2}_{2,\infty}(\overline{\mathbb R}{}^n_+)\) and \(u\) has compact support, but \(u\) is not conormal to the boundary. The exact distributional identity is
\[
 T_au=x_nD_nu=-i\varphi(x')\big(\tfrac32\delta'(x_n-\tfrac32)-\delta(x_n-\tfrac32)\big),
 \qquad
 \widehat{T_au}(\xi',\xi_n)
 =\widehat\varphi(\xi')e^{-3i\xi_n/2}\big(\tfrac32\xi_n+i\big).
\]

**Editorial correction to the Fourier lower bound.** It holds on a bounded tangential set where \(|\widehat\varphi|\) is bounded below, rather than at every point of \(\{|\xi'|\le1\}\). Since Fourier inversion and \(\varphi\neq0\) imply \(\widehat\varphi\not\equiv0\), continuity gives a bounded set \(E\) of positive measure and a constant \(c>0\) with \(|\widehat\varphi|\ge c\) on \(E\). In dimension one, \(E=\mathbb R^0\), with its measure one and the nonzero scalar \(\varphi\). For sufficiently large \(j\),
\[
 E\times[\tfrac35\,2^j,\tfrac45\,2^j]\subset A_j,
 \qquad
 \|\Pi_jT_au\|_2^2
 \ge (2\pi)^{-n}c^2|E|
       \int_{(3/5)2^j}^{(4/5)2^j}
           \big(\tfrac94\xi_n^2+1\big)\,d\xi_n
 \ge C2^{3j}.
\]
Thus \(2^{-j/2}\|\Pi_jT_au\|_2\ge C'2^j\), so \(T_au\notin B^{-1/2}_{2,\infty}\). For the original input, integration over \(A_j\) is bounded above by integration over \(|\xi_n|<2^j\) and all tangential frequencies, giving
\[
 \|\Pi_j u\|_2^2
 \le (2\pi)^{-n}2^{j+1}\|\widehat\varphi\|_2^2.
\]
The order-zero annulus is finite as well, so the stated input membership follows. It is not conormal to the boundary: it is singular on \(x_n=3/2\) wherever \(\varphi\neq0\), whereas a boundary-conormal distribution is smooth off \(x_n=0\). Conormality is what makes the order irrelevant in Theorem 11.2.

## 12. Residual operators need not gain regularity

An ordinary pseudodifferential operator of order \(-\infty\) maps every Sobolev space into every other. For totally characteristic operators this fails: the singularity of the kernel at the corner (Remark 6.3) can prevent any gain.

**Theorem 12.1** (No gain of regularity). Let \(a\in S^{-\infty}_{\mathrm{la}}\) with resolved kernel \(F\) (Theorem 6.2).

(a) Suppose that for some \(s<s'\) there is \(C\) with
\[
|(T_au,v)|\leq C\|u\|_{(s)}\|v\|_{(-s')}\qquad(u,v\in C_0^\infty(\mathbb R^n_+)),
\tag{12.1}
\]
which holds in particular if \(T_a\) maps \(\dot H_{(s)}(\overline{\mathbb R}{}^n_+)\) continuously into \(\dot H_{(s')}(\overline{\mathbb R}{}^n_+)\). Then \(F(x',y',0,r)=0\) for all \(x',y',r\).

(b) There are \(a\in S^{-\infty}_{\mathrm{la}}\) with \(F(\cdot,\cdot,0,\cdot)\not\equiv0\). For these, \(T_a\) maps no \(\dot H_{(s)}(\overline{\mathbb R}{}^n_+)\) into any \(\dot H_{(s')}(\overline{\mathbb R}{}^n_+)\) with \(s'>s\).

(c) There are also \(a\in S^{-\infty}_{\mathrm{la}}\), \(a\neq0\), for which \(T_a\) maps \(\dot H_{(s)}(\overline{\mathbb R}{}^n_+)\) into \(\dot H_{(s')}(\overline{\mathbb R}{}^n_+)\) for all \(s,s'\).

**Proof.** (a) *Test functions.* Let \(\varphi,\vartheta\in C_0^\infty(\mathbb R^{n-1})\), \(w,z\in C_0^\infty((0,\infty))\), and integers \(J,J'\geq0\). Put \(u(y)=\varphi(y')D^J_{y_n}w(y_n)\), \(v(x)=\vartheta(x')D^{J'}_{x_n}z(x_n)\), and \(u_\varepsilon(y)=\varepsilon^{-1/2}u(y',y_n/\varepsilon)\), \(v_\varepsilon(x)=\varepsilon^{-1/2}v(x',x_n/\varepsilon)\), \(0<\varepsilon\leq1\). Then \(\widehat{u_\varepsilon}(\xi)=\varepsilon^{1/2}\widehat u(\xi',\varepsilon\xi_n)\), so
\[
\|u_\varepsilon\|^2_{(\sigma)}=(2\pi)^{-n}\int\big(1+|\xi'|^2+\theta^2/\varepsilon^2\big)^\sigma|\widehat u(\xi',\theta)|^2\,d\xi'\,d\theta .
\]
For \(\sigma\geq0\) the weight is at most \(\varepsilon^{-2\sigma}(1+|\xi'|^2+\theta^2)^\sigma\). For \(\sigma<0\) it is at most \(\varepsilon^{-2\sigma}|\theta|^{2\sigma}\), and \(|\widehat u(\xi',\theta)|=|\widehat\varphi(\xi')||\theta|^J|\widehat w(\theta)|\), so the integral is finite if \(2\sigma+2J>-1\). Hence \(\|u_\varepsilon\|_{(\sigma)}\leq C\varepsilon^{-\sigma}\) when \(J>-\sigma-\tfrac12\), and likewise for \(v_\varepsilon\). Choosing \(J>-s-\tfrac12\) and \(J'>s'-\tfrac12\), (12.1) gives \(|(T_au_\varepsilon,v_\varepsilon)|\leq C\varepsilon^{s'-s}\to0\).

*The limit.* By Theorem 6.2(b), \((T_au_\varepsilon,v_\varepsilon)=\iint K(x,y)u_\varepsilon(y)\overline{v_\varepsilon(x)}\,dy\,dx\). Substitute \(x_n=\varepsilon X\), \(y_n=\varepsilon Y\). Since \(\varepsilon K(x',\varepsilon X,y',\varepsilon Y)=2F\big(x',y',\varepsilon\tfrac{X+Y}2,r\big)/(X+Y)\) with \(r=2(X-Y)/(X+Y)\), and \(F\) is bounded with decay in \(x'-y'\), while \(X,Y\) stay in a compact subset of \((0,\infty)\), dominated convergence gives
\[
\lim_{\varepsilon\to0}(T_au_\varepsilon,v_\varepsilon)=\iint\kappa(x',y',X,Y)\,u(y',Y)\,\overline{v(x',X)}\,dx'\,dy'\,dX\,dY,\qquad \kappa=\frac{2F\big(x',y',0,\frac{2(X-Y)}{X+Y}\big)}{X+Y}.
\]
So this integral vanishes for all choices above.

*Conclusion.* Let \(\kappa_{\varphi\vartheta}(X,Y)=\iint\kappa\,\varphi(y')\overline{\vartheta(x')}\,dx'\,dy'\), a smooth function on \((0,\infty)^2\), homogeneous of degree \(-1\). Integrating by parts in \(X\) and \(Y\), the vanishing says \(\iint(\partial_X^{J'}\partial_Y^J\kappa_{\varphi\vartheta})\,w(Y)\overline{z(X)}\,dX\,dY=0\) for all \(w,z\), so \(\partial_X^{J'}\partial_Y^J\kappa_{\varphi\vartheta}=0\)
by the product-test density proof O0.1. If \(J'=0\), this already
says \(\partial_Y^J\kappa_{\varphi\vartheta}=0\); if \(J=0\)
at the last step the conclusion is already \(\kappa=0\).
For a positive derivative order, the fundamental theorem of calculus
iterated that many times gives the claimed polynomial. Hence, for fixed \(Y\), \(X\mapsto\partial_Y^J\kappa_{\varphi\vartheta}(X,Y)\) is a polynomial of degree \(<J'\). But \(\partial_Y^J\kappa_{\varphi\vartheta}(X,Y)=X^{-1-J}g(Y/X)\) with \(g(\varrho)=\partial_\varrho^J[\kappa_{\varphi\vartheta}(1,\varrho)]\), and \(\kappa_{\varphi\vartheta}(1,\varrho)\) is smooth on \([0,1]\) and flat at \(\varrho=0\) (as \(\varrho\to0\), \(r\to2\), where \(F\) vanishes to infinite order); so \(\partial_Y^J\kappa_{\varphi\vartheta}(X,Y)\to0\) as \(X\to\infty\), and the polynomial is 0. So \(\partial_Y^J\kappa_{\varphi\vartheta}\equiv0\), and the same argument in \(Y\) (now using \(r\to-2\)) gives \(\kappa_{\varphi\vartheta}\equiv0\). As \(\varphi,\vartheta\) are arbitrary and \(r=2(X-Y)/(X+Y)\) takes every value in \((-2,2)\), \(F(x',y',0,r)=0\) for \(|r|<2\); for \(|r|\geq2\) it vanishes anyway.

(b) Let \(\theta(x_n)=e^{-x_n}\) and \(0\neq h\in C_0^\infty(\{|z|<\tfrac12\})\), and put \(a(x,\xi)=\theta(x_n)\widehat h(\xi)\). Then \(a\in S^{-\infty}_+\) and \(A(x,z)=\theta(x_n)h(z)\), which vanishes for \(z_n\geq\tfrac12\); so \(a\) is (strongly) lacunary. By (6.6), \(F(x',y',0,r)=2h\big(x'-y',\tfrac{2r}{2+r}\big)/(2+r)\), and \(2r/(2+r)\) runs through \((-\infty,1)\supset(-\tfrac12,\tfrac12)\) as \(r\) runs through \((-2,2)\); so \(F(\cdot,\cdot,0,\cdot)\not\equiv0\). By (a), no gain is possible.

(c) Let \(\theta_1\in C_0^\infty((2,3))\), \(\theta_1\neq0\), and \(a(x,\xi)=\theta_1(x_n)\widehat h(\xi)\) with \(h\) as in (b). On \(\operatorname{supp}\theta_1\), \(x_n\) is bounded above and below, so \(a^\flat\) is an ordinary symbol of order \(-\infty\) on \(\mathbb R^n\times\mathbb R^n\), and \(T_a\) maps \(H_{(s)}\) into \(H_{(s')}\) for all \(s,s'\), by the Sobolev continuity of ordinary pseudodifferential operators (Section 1). Its outputs are supported in \(\{2\leq x_n\leq3\}\). Here \(F=0\) for \(t<1\). \(\square\)

So a residual operator may or may not improve regularity: by (b) some gain nothing at all, and by (c) others gain every amount. The reason for (a) is dilation invariance. Near the corner the kernel is \(F(x',y',0,r)/t\), homogeneous of degree \(-1\) in \((x_n,y_n)\). Normal dilations \(u\mapsto\lambda^{1/2}u(x',\lambda x_n)\) preserve the \(L^2\) norm but change the \(\dot H_{(s)}\) norms of normal oscillations by different powers of \(\lambda\), so an operator that commutes with them cannot gain derivatives unless it vanishes. Test functions with vanishing normal moments make the argument work at every \(s\): with generic bumps the norms \(\|u_\varepsilon\|_{(\sigma)}\) are of size \(\varepsilon^{1/2}\) for \(\sigma<-\tfrac12\), and the estimate then says nothing when \(s<s'<-\tfrac12\) or \(\tfrac12<s<s'\).

## 13. Exercises

**Exercise 1.** Express \((x_nD_n)^3\) in the basis \(x_n^jD_n^j\), and check the result on \(x_n^\lambda\) for \(x_n>0\).

*Solution.* Write \(L=x_nD_n\). By (2.1), \(x_n^2D_n^2=L^2+iL\) and \(x_n^3D_n^3=L(L+i)(L+2i)=L^3+3iL^2-2L\). Hence \(L^3=x_n^3D_n^3-3iL^2+2L=x_n^3D_n^3-3ix_n^2D_n^2-x_nD_n\). Check: \(D_nx_n^\lambda=-i\lambda x_n^{\lambda-1}\), so \(L^3x_n^\lambda=(-i\lambda)^3x_n^\lambda=i\lambda^3x_n^\lambda\), while the right side gives \(i[\lambda(\lambda-1)(\lambda-2)+3\lambda(\lambda-1)+\lambda]x_n^\lambda=i\lambda^3x_n^\lambda\).

**Exercise 2.** Show that the pointwise product of two lacunary symbols need not be lacunary, although by Theorem 8.1 the composition symbol always is.

*Solution.* With \(\mathcal Ff(t)=\int e^{-it\xi}f(\xi)d\xi\) we have \(\mathcal F(fg)=(2\pi)^{-1}\mathcal Ff*\mathcal Fg\), so supports add. Take \(0\neq g\in C_0^\infty((-0.95,-0.85))\), \(G\in\mathcal S(\mathbb R)\) with \(\mathcal FG=g\), \(0\neq\psi\in\mathcal S(\mathbb R^{n-1})\), and \(a(x,\xi)=e^{-x_n}\psi(\xi')G(\xi_n)\in S^{-\infty}_{\mathrm{la}}\). Then \(\mathcal F_n(a^2)\) is a multiple of \(g*g\), which is supported in \((-1.9,-1.7)\) and is not zero (its Fourier transform is a multiple of \(G^2\)). So \(a^2\) is not lacunary.

**Exercise 3.** Show that on \(\overline{\mathcal S}(\mathbb R^n_+)\), for \(a\in S^m_{\mathrm{la}}\),
\[
[D_j,T_a]=T_{D_{x_j}a}\ (j<n),\qquad[x_nD_n,T_a]=T_{x_nD_{x_n}a},
\]
so commutators with the generators of \(\operatorname{Diff}_b\) do not raise the order, unlike \([D_n,T_a]\).

*Solution.* By the proof of Lemma 11.1(a), \(D_jT_a=T_{(\xi_j+D_{x_j})a}\) and \(x_nD_nT_a=T_{(\xi_n+x_nD_{x_n}+\xi_nD_{\xi_n})a}\). By (5.4), \(T_aD_j=T_{\xi_ja}\) and \(T_ax_nD_n=T_{\xi_n(1-i\partial_{\xi_n})a}=T_{\xi_na+\xi_nD_{\xi_n}a}\). Subtract. Since \(x_n\) is absorbed by the decay in \(x_n\), \(x_nD_{x_n}a\in S^m_{\mathrm{la}}\). In contrast \([D_n,T_a]=-iT_{\partial_{x_n}a}-iT_{\partial_{\xi_n}a}D_n\) by (5.1), and \(D_n\) is not in \(\operatorname{Diff}_b\).

**Exercise 4.** For the symbol of Example 6.6, find the ratios \(y/x\) at which the kernel can be nonzero, and show directly that \(F\) is smooth for \(t\geq0\).

*Solution.* \(h((x-y)/x)\neq0\) requires \(|1-y/x|<\tfrac12\), that is \(\tfrac12<y/x<\tfrac32\). In the formula for \(F\), \(h(2r/(2+r))\neq0\) requires \(-\tfrac12<2r/(2+r)<\tfrac12\), that is \(-\tfrac25<r<\tfrac23\). On this interval \(2+r\geq\tfrac85\), so \(F\) is a product of smooth functions of \((t,r)\) for \(t\geq0\), with support in \(-\tfrac25\leq r\leq\tfrac23\); it vanishes near \(r=\pm2\). The two descriptions agree, because \(y/x=(2-r)/(2+r)\) maps \((-\tfrac25,\tfrac23)\) onto \((\tfrac12,\tfrac32)\).

**Exercise 5.** Let \(a\in S^m_{\mathrm{la}}\) and \(u\in\overline{\mathcal S}(\mathbb R^n_+)\) with \(u(x',0)=0\). Show that \((T_au)(x',0)=0\) and compute \(D_n(T_au)(x',0)\).

*Solution.* By (5.2) with \(k=0\), \((T_au)(x',0)=a_{00}(x',D')u(\cdot,0)=0\). With \(k=1\), \(D_n(T_au)(x',0)=a_{10}(x',D')u(\cdot,0)+a_{11}(x',D')D_nu(\cdot,0)=a_{11}(x',D')\big(D_nu(\cdot,0)\big)\), where \(a_{11}(x',\xi')=a(x',0,\xi',0)+(D_{\xi_n}a)(x',0,\xi',0)\). The first term is the value of the symbol at the boundary with the normal frequency compressed to 0; the second is a correction of order \(m-1\).

## 13.1. Precise topology of the local conormal action

The maps in Theorem 11.2 are continuous in the actual conormal
seminorms. For a specified output tangent word \(P\), Lemma 11.1
performs finitely many symbol operations to obtain
\(PT_a=T_fT_Q+T_g\), where \(f,g\) are order zero and \(Q\)
has a fixed finite differential order depending on that output word
and the order of \(a\). The all-endpoint bound of Theorem 10.6 gives
\[
 \|PT_au\|_{B^\kappa_{2,\infty}}
 \le C_P(a)\bigl(\|T_Qu\|_{B^\kappa_{2,\infty}}
                         +\|u\|_{B^\kappa_{2,\infty}}\bigr).
 \tag{LB1}
\]
Here \(C_P(a)\) is bounded on each bounded set of finitely many
original symbol seminorms, by the proved finite-seminorm bounds in
the decomposition and the order-zero theorem. The input differential
polynomial \(T_Q\) is a finite sum of actual tangent words by (2.1).
Thus the right side uses only finitely many original input seminorms.
For compact input and compact output, multiply by the fixed smooth
cutoffs and use Theorem 11.2(a); the same estimate gives continuity
at the original local conormal order. No loss of its conormal index
has been introduced.

The residual map of Theorem 9.3 has the uniform finite distribution
order asserted there. On any family of supported distributions with
one common finite test bound, the argument gives one common conormal
order and seminorm bounds, with each requested tangent word allowed
its own finite residual-symbol seminorm. This is the actual receiving
estimate later used by the global calculus. It does not say that an
arbitrary residual operator gains Sobolev derivatives; Theorem 12.1
proves precisely why that stronger claim fails.
