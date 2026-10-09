# Haagerup's criterion for a trivial bicentralizer

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(\varphi\) be a faithful normal state on a type III factor \(M\), and \(a\) an element of its bicentralizer. Every bounded sequence that asymptotically commutes with \(\varphi\) asymptotically commutes with \(a\). To show that \(a\) is a scalar, it therefore suffices to produce, for the vector \(\eta=(a-\varphi(a))\xi_\varphi\), projections \(p\) that commute with \(\varphi\) as closely as we like and yet fail to commute with \(\eta\) by a fixed proportion of \(\|\eta\|\). Haagerup found a way to produce such projections from a weaker, local supply of elements, and used it to prove that the bicentralizer of an injective factor of type III₁ is trivial [Haagerup]. Ando, Haagerup, Houdayer and Marrakchi isolated the local condition as a criterion in its own right [AHHM, Theorem 7.2]. This lesson proves that criterion, Theorem 5.2 below. It is the analytic input of the triviality theorem proved in the last lesson of this course.

The proof uses the geometry of the standard form and nothing about injectivity. We use a standard form \((M,H,J,P)\) and its axioms as in [All projection corners and canonical positive-functional vectors](course:OA-FLOW/OA-FLOW-CR#OA-FLOW.CR.1): the corner standard forms of CR-3 there, the identification of the modular conjugation of a cyclic separating cone vector in CR-4, and the inequality (CR18) of CR-6; the joint spectral measure of left and right multiplication by a self-adjoint element, Theorem NC-20 of [Joint spectral measures and commutator estimates in standard form](course:OA-MOD/OA-MOD-NC#OA-MOD-NC-20), and the estimate (NC.4) there; the facts on projections in countably decomposable type III factors listed as (B8) in [Ultraproducts and the asymptotic centralizer](course:type-iii-factors/ultraproducts-and-the-asymptotic-centralizer#results-used-from-other-lessons); and Definition 1.1 of [The bicentralizer](the-bicentralizer.md). A factor is of type III when it has no nonzero finite projection.

## 1. Conventions and the criterion

Throughout, \((M,H,J,P)\) is a standard form: \(JMJ=M'\), \(J\) is an antiunitary involution fixing the self-dual cone \(P\), and \(xJxJ\) maps \(P\) into \(P\) for \(x\in M\). For \(a\in M\) and \(\zeta\in H\) the right action is
\[
\zeta a=Ja^*J\zeta .
\]
It commutes with the left action, \(\zeta(ab)=(\zeta a)b\), and it is complex linear in \(a\). For projections \(e,f\in M\) we write \(e\zeta f=eJfJ\zeta\); the operator \(eJfJ\) is a projection. Since \(J\) is antiunitary and \(J^2=1\),
\[
J(a\zeta)=(J\zeta)a^*,\qquad J(\zeta a)=a^*(J\zeta).
\tag{1.1}
\]
Let \(H_{\mathrm{sa}}=\{\eta\in H:J\eta=\eta\}\). Inner products of two vectors of \(H_{\mathrm{sa}}\) are real, because \(\langle J\zeta,J\zeta'\rangle=\overline{\langle\zeta,\zeta'\rangle}\). For \(\eta\in H_{\mathrm{sa}}\), (1.1) gives \(J(\eta a)=a^*\eta\) and \(J(a\eta)=\eta a^*\), so
\[
\|\eta a\|=\|a^*\eta\|,\qquad\|a\eta-\eta a\|=\|a^*\eta-\eta a^*\|\qquad(\eta\in H_{\mathrm{sa}},\ a\in M).
\tag{1.2}
\]
The vectors of \(P\) lie in \(H_{\mathrm{sa}}\). If \((e_i)\) are pairwise orthogonal projections of \(M\), the projections \(e_iJe_iJ\) are pairwise orthogonal, so \(\sum_ie_i\zeta e_i\) converges for every \(\zeta\), with norm at most \(\|\zeta\|\).

Every normal positive functional \(\psi\) is the vector functional \(\omega_\zeta=\langle\,\cdot\,\zeta,\zeta\rangle\) of a unique \(\zeta\in P\). A vector \(\xi\in P\) is cyclic and separating exactly when \(\omega_\xi\) is faithful. For such \(\xi\), CR-4 shows that \((H,\xi)\) is the GNS representation of \(\omega_\xi\) and that \(J\) is its modular conjugation; so \(\xi a=J_\xi a^*J_\xi\xi=\Delta_\xi^{1/2}a\xi\), and by (NC.4)
\[
\|[a,\omega_\xi]\|\le2\|a\xi-\xi a\|\qquad(a\in M),
\tag{1.3}
\]
where \([a,\psi]=a\psi-\psi a\) in the notation of the first lesson.

For a faithful normal state \(\theta\) on any von Neumann algebra, let \((H_\theta,\xi_\theta)\) be its GNS representation, \(J_\theta\) its modular conjugation, and \(\xi_\theta a=J_\theta a^*J_\theta\xi_\theta\). These data are determined by \((M,\theta)\) up to a unitary that fixes \(\xi_\theta\).

**Definition 1.1.** Let \(\kappa\ge1\). A von Neumann algebra \(M\) satisfies *Haagerup's condition with constant \(\kappa\)* if: for every faithful normal state \(\theta\) on \(M\), every \(\delta>0\), and every \(x\in M\) with
\[
x\xi_\theta=\xi_\theta x^*,\qquad\theta(x)=0,\qquad\theta(x^*x)=1,
\]
there is \(a\in M\) such that
\[
\|a\|_\theta^2+\|ax\|_\theta^2<\kappa\,\|xa-ax\|_\theta^2,\qquad\|a\xi_\theta-\xi_\theta a\|^2<\delta\,\|xa-ax\|_\theta^2 .
\]

[AHHM, Theorem 7.2] states the condition with \(\|a\|_\theta+\|ax\|_\theta<\kappa\|xa-ax\|_\theta\); since \(\|a\|^2_\theta+\|ax\|^2_\theta\le(\|a\|_\theta+\|ax\|_\theta)^2\), that form implies Definition 1.1 with \(\kappa^2\) in place of \(\kappa\), so Theorem 5.2 below contains their statement.

**Lemma 1.2.** (1) If \(\alpha\colon N\to M\) is a \(*\)-isomorphism and \(M\) satisfies Haagerup's condition with constant \(\kappa\), so does \(N\). (2) If \(M\) is a countably decomposable type III factor satisfying the condition and \(q\in M\) is a nonzero projection, then \(qMq\) satisfies it with the same constant.

**Proof.** (1) For a faithful normal state \(\theta\) on \(N\), the state \(\theta\circ\alpha^{-1}\) on \(M\) has the GNS representation \((H_\theta,\xi_\theta,\pi_\theta\circ\alpha^{-1})\), with the same represented algebra and vector, hence the same \(J_\theta\). Apply the condition in \(M\) to \(\alpha(x)\) and pull the element back by \(\alpha^{-1}\); all quantities are preserved. (2) By (B8), \(q\) is equivalent to \(1\), so \(qMq\cong M\); apply (1). \(\square\)

**Lemma 1.3.** Let \(M\) be a countably decomposable type III factor.

1. Every nonzero projection \(p\) is the sum of two nonzero projections, and any two nonzero projections are equivalent.
2. If \(\psi\) is a normal positive functional and \(p\ne0\) a projection, there is a projection \(q\le p\) with \(q\ne0\), \(p-q\ne0\) and \(\psi(q)\le\psi(p)/16\).

**Proof.** (1) By (B8) every nonzero projection is equivalent to \(1\), so any two are equivalent. If \(pMp=\mathbb Cp\), then \(p\) is abelian, hence finite ([Projections and types of von Neumann algebras, Lemma 6.2](course:foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras#OA-FND-TY-09)), which is excluded. So \(pMp\) contains a self-adjoint element that is not a multiple of \(p\), and one of its spectral projections \(p_1\) satisfies \(0\ne p_1\ne p\); then \(p=p_1+(p-p_1)\). (2) Split \(p=r_1+r_1'\) with both summands nonzero and let \(r\) be the one of smaller \(\psi\)-value, so \(\psi(r)\le\psi(p)/2\). Repeating four times gives \(q\ne0\) with \(\psi(q)\le\psi(p)/16\); the summand discarded at the last step lies under \(p-q\), so \(p-q\ne0\). \(\square\)

## 2. The local step

In Sections 2–5, \(M\) is a countably decomposable type III factor in standard form \((M,H,J,P)\) that satisfies Haagerup's condition with a constant \(\kappa\ge1\); \(\xi\in P\) is a cyclic and separating unit vector, and \(\varphi=\omega_\xi\).

**Lemma 2.1.** Let \(\eta\in H_{\mathrm{sa}}\) be a unit vector with \(\langle\eta,\xi\rangle=0\), and \(0<\delta\le1\). There is \(a\in M\) with
\[
\|a\xi\|^2+\|a\eta\|^2<4\kappa\|a\eta-\eta a\|^2,\qquad\|a\xi-\xi a\|^2<\delta\|a\eta-\eta a\|^2 .
\]

**Proof.** Let \(\psi=\omega_\eta\) and \(K=8/\delta\ge8\).

*Case 1: \(\psi\le K\varphi\).* For \(y\in M\), \(\|y\eta\|^2=\psi(y^*y)\le K\|y\xi\|^2\). So \(y\xi\mapsto y\eta\) is well defined on the dense subspace \(M\xi\) and extends to an operator \(x'\) with \(\|x'\|\le K^{1/2}\); it commutes with \(M\), so \(x'\in M'\). Put \(x=Jx'J\in M\). Then \(x\xi=Jx'\xi=J\eta=\eta\) and \(\xi x^*=JxJ\xi=x'\xi=\eta\). So \(x\xi=\xi x^*=\eta\), \(\varphi(x)=\langle\eta,\xi\rangle=0\), \(\varphi(x^*x)=\|\eta\|^2=1\) and \(\|x\|\le K^{1/2}\). Since \((H,\xi)\) is the GNS representation of \(\varphi\) with modular conjugation \(J\), Haagerup's condition with \(\delta'=\delta/(4K)\) gives \(a\in M\) with
\[
\|a\|_\varphi^2+\|ax\|_\varphi^2<\kappa\|xa-ax\|_\varphi^2,\qquad\|a\xi-\xi a\|^2<\delta'\|xa-ax\|_\varphi^2 .
\]
Since \(\eta a=(x\xi)a=x(\xi a)\),
\[
a\eta-\eta a=(ax-xa)\xi+x(a\xi-\xi a),
\]
and \(\|x(a\xi-\xi a)\|\le K^{1/2}(\delta')^{1/2}\|xa-ax\|_\varphi=\tfrac12\delta^{1/2}\|xa-ax\|_\varphi\le\tfrac12\|xa-ax\|_\varphi\). Hence \(\|a\eta-\eta a\|\ge\frac12\|xa-ax\|_\varphi\). As \(\|a\xi\|=\|a\|_\varphi\) and \(\|a\eta\|=\|ax\xi\|=\|ax\|_\varphi\),
\[
\|a\xi\|^2+\|a\eta\|^2<4\kappa\|a\eta-\eta a\|^2,\qquad\|a\xi-\xi a\|^2<4\delta'\|a\eta-\eta a\|^2=\tfrac{\delta}{K}\|a\eta-\eta a\|^2\le\delta\|a\eta-\eta a\|^2 .
\]

*Case 2: \(\psi\not\le K\varphi\).* Then \(\psi(p)>K\varphi(p)\) for some projection \(p\): otherwise \(\psi\le K\varphi\) on positive combinations of spectral projections, and every positive element is a norm limit of these. In particular \(\psi(p)>0\) and \(p\ne0\). Lemma 1.3 gives \(q\le p\) with \(q\ne0\), \(p-q\ne0\), \(\psi(q)\le\psi(p)/16\), and a partial isometry \(v\) with \(v^*v=p-q\), \(vv^*=q\). By (1.2),
\[
\|v\xi\|^2=\varphi(p-q)\le\varphi(p),\quad\|\xi v\|^2=\|v^*\xi\|^2=\varphi(q)\le\varphi(p),\quad\|v\eta\|^2=\psi(p-q)\ge\tfrac{15}{16}\psi(p),\quad\|\eta v\|^2=\psi(q)\le\tfrac1{16}\psi(p).
\]
So \(\|v\eta-\eta v\|\ge\frac{\sqrt{15}-1}4\psi(p)^{1/2}\), and \(\big(\frac{\sqrt{15}-1}4\big)^2=1-\frac{\sqrt{15}}8>\frac12\); thus \(\|v\eta-\eta v\|^2>\psi(p)/2\). Hence
\[
\|v\xi\|^2+\|v\eta\|^2\le\varphi(p)+\psi(p)<2\psi(p)<4\|v\eta-\eta v\|^2,
\]
\[
\|v\xi-\xi v\|^2\le2\|v\xi\|^2+2\|\xi v\|^2\le4\varphi(p)<\tfrac4K\psi(p)<\tfrac8K\|v\eta-\eta v\|^2=\delta\|v\eta-\eta v\|^2 .
\]
Take \(a=v\). \(\square\)

**Lemma 2.2.** Let \(\eta\) and \(\delta\) be as in Lemma 2.1. There is \(b=b^*\in M\) with
\[
\|b\xi\|^2+\|b\eta\|^2+\tfrac{16\kappa}{\delta}\|b\xi-\xi b\|^2<16\kappa\|b\eta-\eta b\|^2 .
\]
In particular \(\|b\xi\|^2+\|b\eta\|^2<16\kappa\|b\eta-\eta b\|^2\) and \(\|b\xi-\xi b\|^2<\delta\|b\eta-\eta b\|^2\).

**Proof.** Let \(c=4\kappa\), \(\delta_0=\delta/(16c)\le1/64\) and \(\gamma=4c/\delta\). Lemma 2.1 with \(\delta_0\) gives \(a\) with \(\|a\xi\|^2+\|a\eta\|^2<cD^2\) and \(\|a\xi-\xi a\|^2<\delta_0D^2\), where \(D=\|a\eta-\eta a\|>0\). By (1.2), with \(\xi,\eta\in H_{\mathrm{sa}}\),
\[
\|a^*\xi\|=\|\xi a\|<(\sqrt c+\sqrt{\delta_0})D,\quad\|a^*\eta\|=\|\eta a\|<(\sqrt c+1)D,\quad\|a^*\xi-\xi a^*\|=\|a\xi-\xi a\|,\quad\|a^*\eta-\eta a^*\|=D .
\]
Put \(Q(y)=\|y\xi\|^2+\|y\eta\|^2+\gamma\|y\xi-\xi y\|^2\). Then \(Q(a)<(c+\gamma\delta_0)D^2=(c+\frac14)D^2\), and, using \((u+v)^2\le2u^2+2v^2\),
\[
Q(a^*)<\big(2c+2\delta_0+2c+2+\tfrac14\big)D^2<(4c+\tfrac52)D^2 .
\]
So \(Q(a)+Q(a^*)<(5c+3)D^2\le8cD^2\), because \(c\ge4\). Write \(a=b_1+ib_2\) with \(b_1,b_2\) self-adjoint. For each of the complex-linear maps \(y\mapsto y\xi,\ y\eta,\ y\xi-\xi y,\ y\eta-\eta y\), the parallelogram law gives \(\|L(a)\|^2+\|L(a^*)\|^2=2\|L(b_1)\|^2+2\|L(b_2)\|^2\). Hence
\[
Q(b_1)+Q(b_2)=\tfrac12\big(Q(a)+Q(a^*)\big)<4cD^2,\qquad\|b_1\eta-\eta b_1\|^2+\|b_2\eta-\eta b_2\|^2=D^2 .
\]
So \(Q(b_j)<4c\|b_j\eta-\eta b_j\|^2=16\kappa\|b_j\eta-\eta b_j\|^2\) for \(j=1\) or \(j=2\); take \(b=b_j\). \(\square\)

## 3. Spectral cuts

Let \(b=b^*\in M\) and \(e_\lambda=1_{(-\infty,\lambda]}(b)\). For \(\zeta\in H\), the proof of Theorem NC-20 applies verbatim to the vector \(\zeta\) in place of \(\xi_\phi\): with \(E\) the joint spectral measure of the commuting operators \(\zeta\mapsto b\zeta\) and \(\zeta\mapsto\zeta b\), the measure \(\nu_\zeta=\langle E(\cdot)\zeta,\zeta\rangle\) on \(\operatorname{sp}(b)\times\operatorname{sp}(b)\) satisfies, for bounded Borel functions \(f,g\),
\[
\|f(b)\zeta-\zeta g(b)\|^2=\int|f(s)-g(t)|^2\,d\nu_\zeta(s,t).
\tag{3.1}
\]
Taking \(f,g\) equal to the identity or zero on \(\operatorname{sp}(b)\) gives \(\int|s-t|^2d\nu_\zeta=\|b\zeta-\zeta b\|^2\), \(\int s^2d\nu_\zeta=\|b\zeta\|^2\), \(\int t^2d\nu_\zeta=\|\zeta b\|^2\).

**Lemma 3.1.** For \(\zeta\in H\):

1. \(\displaystyle\int_{\mathbb R}\|e_\lambda\zeta-\zeta e_\lambda\|^2|\lambda|\,d\lambda\le\tfrac1{\sqrt2}\|b\zeta-\zeta b\|\big(\|b\zeta\|^2+\|\zeta b\|^2\big)^{1/2}\), which is at most \(\|b\zeta-\zeta b\|\,\|b\zeta\|\) when \(J\zeta=\zeta\);
2. \(\displaystyle\int_{\mathbb R}\|e_\lambda\zeta-\zeta e_\lambda\|^2|\lambda|\,d\lambda\ge\tfrac14\|b\zeta-\zeta b\|^2\);
3. with \(f_\lambda=e_\lambda\) for \(\lambda<0\) and \(f_\lambda=1-e_\lambda\) for \(\lambda\ge0\), \(\|f_\lambda\zeta-\zeta f_\lambda\|=\|e_\lambda\zeta-\zeta e_\lambda\|\) and \(\displaystyle\int_{\mathbb R}\|f_\lambda\zeta\|^2|\lambda|\,d\lambda=\tfrac12\|b\zeta\|^2\).

**Proof.** By (3.1), \(\|e_\lambda\zeta-\zeta e_\lambda\|^2=\int h_\lambda\,d\nu_\zeta\), where \(h_\lambda(s,t)=1\) if \(\min(s,t)\le\lambda<\max(s,t)\) and \(0\) otherwise. By Tonelli,
\[
\int_{\mathbb R}\|e_\lambda\zeta-\zeta e_\lambda\|^2|\lambda|\,d\lambda=\int\Big|\int_s^t|\lambda|\,d\lambda\Big|\,d\nu_\zeta(s,t)=\tfrac12\int\big|t|t|-s|s|\big|\,d\nu_\zeta(s,t).
\]
For real \(s,t\),
\[
\tfrac12(t-s)^2\le\big|t|t|-s|s|\big|\le|t-s|(|s|+|t|).
\tag{3.2}
\]
Indeed, if \(st\ge0\) the middle term is \(|t^2-s^2|=|t-s|(|s|+|t|)\), and \(|s|+|t|\ge|t-s|\); if \(st<0\) it is \(s^2+t^2\), and \(\frac12(t-s)^2\le s^2+t^2\le(|s|+|t|)^2=|t-s|(|s|+|t|)\). The upper bound and Cauchy–Schwarz give
\[
\tfrac12\int|t-s|(|s|+|t|)\,d\nu_\zeta\le\tfrac12\Big(\int|t-s|^2d\nu_\zeta\Big)^{1/2}\Big(2\int(s^2+t^2)\,d\nu_\zeta\Big)^{1/2},
\]
which is (1). If \(J\zeta=\zeta\), then \(\|\zeta b\|=\|b\zeta\|\) by (1.1). The lower bound in (3.2) gives (2). For (3), \((1-e)\zeta-\zeta(1-e)=-(e\zeta-\zeta e)\). With \(\mu\) the spectral measure of \(b\) at \(\zeta\), \(\|f_\lambda\zeta\|^2\) is \(\mu((-\infty,\lambda])\) for \(\lambda<0\) and \(\mu((\lambda,\infty))\) for \(\lambda\ge0\); by Tonelli the integral is \(\int_{s<0}\int_s^0|\lambda|\,d\lambda\,d\mu(s)+\int_{s>0}\int_0^s\lambda\,d\lambda\,d\mu(s)=\frac12\int s^2d\mu=\frac12\|b\zeta\|^2\). \(\square\)

**Lemma 3.2.** Let \(\eta\in H_{\mathrm{sa}}\) be a unit vector with \(\langle\eta,\xi\rangle=0\), and \(0<\alpha\le1\). There is a nonzero projection \(f\in M\) with
\[
\|f\xi\|^2+\|f\eta\|^2<64\kappa\|f\eta-\eta f\|^2,\qquad\|f\xi-\xi f\|^2<\alpha\|f\eta-\eta f\|^2 .
\]

**Proof.** Let \(K=16\kappa\) and \(\delta_1=\alpha^2/(64K)\le1\). Lemma 2.2 with \(\delta_1\) gives \(b=b^*\) with \(\|b\xi\|^2+\|b\eta\|^2<KD^2\) and \(\|b\xi-\xi b\|^2<\delta_1D^2\), where \(D=\|b\eta-\eta b\|\). With \(f_\lambda\) as in Lemma 3.1, using Lemma 3.1(1) for \(\zeta=\xi\) (which is \(J\)-fixed), Lemma 3.1(2) for \(\zeta=\eta\), and Lemma 3.1(3):
\[
\int\|f_\lambda\xi-\xi f_\lambda\|^2|\lambda|\,d\lambda<\sqrt{\delta_1K}\,D^2=\tfrac\alpha8D^2,\quad\int\|f_\lambda\eta-\eta f_\lambda\|^2|\lambda|\,d\lambda\ge\tfrac14D^2,\quad\int(\|f_\lambda\xi\|^2+\|f_\lambda\eta\|^2)|\lambda|\,d\lambda<\tfrac K2D^2 .
\]
With \(C=4K=64\kappa\),
\[
\int\Big(\|f_\lambda\xi\|^2+\|f_\lambda\eta\|^2+\tfrac C\alpha\|f_\lambda\xi-\xi f_\lambda\|^2\Big)|\lambda|\,d\lambda<\Big(\tfrac K2+\tfrac C8\Big)D^2=KD^2\le C\int\|f_\lambda\eta-\eta f_\lambda\|^2|\lambda|\,d\lambda .
\]
All integrands vanish for \(|\lambda|>\|b\|\). So for some \(\lambda\), \(f=f_\lambda\) satisfies \(\|f\xi\|^2+\|f\eta\|^2+\frac C\alpha\|f\xi-\xi f\|^2<C\|f\eta-\eta f\|^2\). The right side is then positive, so \(f\ne0\), and both assertions follow. \(\square\)

## 4. Non-orthogonal pairs and exhaustion

**Lemma 4.1.** Let \(\eta\in H_{\mathrm{sa}}\) be a unit vector with \(\eta\ne\pm\xi\), and \(\vartheta=\arccos\langle\xi,\eta\rangle\in(0,\pi)\). For every \(0<\delta\le1\) there is a nonzero projection \(f\in M\) with
\[
\|f\xi\|^2+\|f\eta\|^2<\frac{512\kappa}{\sin^2\vartheta}\|f\eta-\eta f\|^2,\qquad\|f\xi-\xi f\|^2<\delta\|f\eta-\eta f\|^2 .
\]

**Proof.** The number \(\langle\xi,\eta\rangle\) is real, and it is not \(\pm1\) since \(\eta\ne\pm\xi\). The vector \(\eta'=(\eta-\cos\vartheta\,\xi)/\sin\vartheta\) is a unit vector in \(H_{\mathrm{sa}}\) orthogonal to \(\xi\). Let \(\delta'=\frac\delta4\sin^2\vartheta\). Lemma 3.2 with \(\eta'\) and \(\alpha=\delta'\) gives \(f\ne0\) with \(\|f\xi\|^2+\|f\eta'\|^2<64\kappa\|f\eta'-\eta'f\|^2\) and \(\|f\xi-\xi f\|^2<\delta'\|f\eta'-\eta'f\|^2\). From \(\sin\vartheta(f\eta'-\eta'f)=(f\eta-\eta f)-\cos\vartheta(f\xi-\xi f)\),
\[
(\sin\vartheta-\sqrt{\delta'})\|f\eta'-\eta'f\|\le\|f\eta-\eta f\|,
\]
and \(\sqrt{\delta'}=\frac{\sqrt\delta}2\sin\vartheta\le\frac12\sin\vartheta\), so \(\|f\eta'-\eta'f\|^2\le\frac4{\sin^2\vartheta}\|f\eta-\eta f\|^2\). This gives \(\|f\xi-\xi f\|^2<\delta\|f\eta-\eta f\|^2\). Finally \(\|f\eta\|\le|\cos\vartheta|\|f\xi\|+\sin\vartheta\|f\eta'\|\le(\|f\xi\|^2+\|f\eta'\|^2)^{1/2}\), so
\[
\|f\xi\|^2+\|f\eta\|^2\le2(\|f\xi\|^2+\|f\eta'\|^2)<128\kappa\|f\eta'-\eta'f\|^2\le\frac{512\kappa}{\sin^2\vartheta}\|f\eta-\eta f\|^2 .\qquad\square
\]

**Lemma 4.2.** Let \(\eta\in H_{\mathrm{sa}}\) be a unit vector with \(\langle\eta,\xi\rangle=0\), and \(0<\delta\le1\). There is a family \((e_i)_{i\in I}\) of pairwise orthogonal nonzero projections of \(M\) with \(\sum_ie_i=1\) and
\[
\Big\|\xi-\sum_ie_i\xi e_i\Big\|^2\le\delta,\qquad\Big\|\eta-\sum_ie_i\eta e_i\Big\|^2\ge\varepsilon_0=\frac{2^{-16}}{\kappa}.
\]

**Proof.** Put \(C_4=2^{11}\kappa\), \(C_3=2C_4\), so \(\varepsilon_0=1/(16C_3)\). For projections \(e,f\in M\) write \(e\,j(f)=eJfJ\). For a family \(F=(p_i)\) of pairwise orthogonal nonzero projections put \(p_F=1-\sum_ip_i\),
\[
X_F=\xi-p_F\xi p_F-\sum_ip_i\xi p_i,\qquad Y_F=\eta-p_F\eta p_F-\sum_ip_i\eta p_i ,
\]
and let \(\mathfrak F\) be the set of such families with
\[
\text{(i)}\ \ \|\xi-p_F\xi p_F\|^2+\|\eta-p_F\eta p_F\|^2\le C_3\|Y_F\|^2,\qquad\text{(ii)}\ \ \|X_F\|^2\le\delta\|Y_F\|^2 .
\]
The empty family belongs to \(\mathfrak F\). Order \(\mathfrak F\) by inclusion. If \((F_\alpha)\) is a chain with union \(F\), then \(p_{F_\alpha}\) decreases strongly to \(p_F\), so \(p_{F_\alpha}j(p_{F_\alpha})\to p_Fj(p_F)\) strongly, and the orthogonal series \(\sum_{F_\alpha}p_i\zeta p_i\) converge to \(\sum_Fp_i\zeta p_i\); the non-strict inequalities pass to the limit, and \(F\in\mathfrak F\). By Zorn's lemma there is a maximal \(F=(q_i)_{i\in I}\); put \(q=p_F\).

We claim \(\|Y_F\|^2\ge\varepsilon_0\). Suppose not. Then (i) gives \(\|\xi-q\xi q\|^2+\|\eta-q\eta q\|^2<C_3\varepsilon_0=\frac1{16}\). Put \(\xi'=q\xi q\), \(\eta'=q\eta q\). Then \(\|\xi'\|,\|\eta'\|\in(\frac34,1]\); in particular \(q\ne0\). Also \(\langle\xi',\eta'\rangle=\langle\xi',\eta\rangle=-\langle\xi-\xi',\eta\rangle\), so \(|\langle\xi',\eta'\rangle|<\frac14\). The unit vectors \(\xi''=\xi'/\|\xi'\|\), \(\eta''=\eta'/\|\eta'\|\) satisfy \(|\langle\xi'',\eta''\rangle|<\frac{1/4}{9/16}=\frac49\), so \(\eta''\ne\pm\xi''\) and their angle \(\vartheta''\) has \(\sin^2\vartheta''>1-\frac{16}{81}>\frac34\).

By CR-3, with \(\hat q=q\,j(q)\), \(qMq\) acts on \(\hat qH\) with the standard form \((qMq,\hat qH,J|_{\hat qH},\hat qP)\); its left and right actions are the restrictions of those of \(M\). The vector \(\xi'=\hat q\xi\) lies in \(\hat qP\). It is cyclic and separating for \(qMq\): if a projection \(r\le q\) has \(r\xi'=0\), then \(r\,j(r)\xi=j(r)\,r\,j(q)\xi=0\), so \(r\xi=0\) by the first support fact of CR-1, and \(r=0\); thus \(\omega_{\xi'}\) is faithful on \(qMq\), and CR-3 gives cyclicity. Also \(J\eta'=\eta'\), since \(J\) commutes with \(\hat q\). The corner \(qMq\) is a countably decomposable type III factor (by (B8) it is isomorphic to \(M\)), and it satisfies Haagerup's condition with constant \(\kappa\) by Lemma 1.2. Lemma 4.1 in \(qMq\), applied to \(\xi'',\eta''\) with \(\delta/2\), gives a nonzero projection \(r\le q\) with
\[
\|r\xi''\|^2+\|r\eta''\|^2<\tfrac{2048\kappa}3\|r\eta''-\eta''r\|^2,\qquad\|r\xi''-\xi''r\|^2<\tfrac\delta2\|r\eta''-\eta''r\|^2 .
\]
Since \(\|\xi'\|,\|\eta'\|\le1\) and \(\|\eta'\|>\frac34\),
\[
\|r\xi'\|^2+\|r\eta'\|^2<\tfrac{2048\kappa}3\cdot\tfrac{16}9\|r\eta'-\eta'r\|^2<C_4\|r\eta'-\eta'r\|^2,\qquad\|r\xi'-\xi'r\|^2<\tfrac\delta2\cdot\tfrac{16}9\|r\eta'-\eta'r\|^2<\delta\|r\eta'-\eta'r\|^2 .
\]
Let \(s=q-r\) and \(F'=F\cup\{r\}\), so \(p_{F'}=s\). Since \(q\,j(q)=s\,j(s)+r\,j(r)+s\,j(r)+r\,j(s)\), a sum of four pairwise orthogonal projections,
\[
Y_{F'}=Y_F+\big(s\,j(r)+r\,j(s)\big)\eta,\qquad r\eta'-\eta'r=r\,j(q)\eta-q\,j(r)\eta=r\,j(s)\eta-s\,j(r)\eta .
\]
\(Y_F\) lies in the range of \(1-q\,j(q)-\sum_iq_i\,j(q_i)\), which is orthogonal to \(q\,j(q)\); so \(\|Y_{F'}\|^2=\|Y_F\|^2+\|r\eta'-\eta'r\|^2\), and likewise \(\|X_{F'}\|^2=\|X_F\|^2+\|r\xi'-\xi'r\|^2\). Hence (ii) holds for \(F'\). For (i), \(1-s\,j(s)=(1-q\,j(q))+r\,j(r)+s\,j(r)+r\,j(s)\), so
\[
\|\xi-s\xi s\|^2=\|\xi-q\xi q\|^2+\|r\,j(r)\xi\|^2+\|s\,j(r)\xi\|^2+\|r\,j(s)\xi\|^2\le\|\xi-q\xi q\|^2+\|r\,j(q)\xi\|^2+\|q\,j(r)\xi\|^2 .
\]
Here \(r\,j(q)\xi=r\xi'\), and \(\|q\,j(r)\xi\|=\|J(q\,j(r)\xi)\|=\|r\,j(q)\xi\|\). So \(\|\xi-s\xi s\|^2\le\|\xi-q\xi q\|^2+2\|r\xi'\|^2\), and in the same way, as \(J\eta=\eta\), \(\|\eta-s\eta s\|^2\le\|\eta-q\eta q\|^2+2\|r\eta'\|^2\). Therefore
\[
\|\xi-s\xi s\|^2+\|\eta-s\eta s\|^2\le C_3\|Y_F\|^2+2C_4\|r\eta'-\eta'r\|^2=C_3\|Y_{F'}\|^2 .
\]
So \(F'\in\mathfrak F\), and \(F'\) strictly contains \(F\), against maximality. This proves the claim.

The family \((q_i)\), together with \(q\) when \(q\ne0\), consists of pairwise orthogonal nonzero projections with sum \(1\); for it \(\xi-\sum e_i\xi e_i=X_F\) and \(\eta-\sum e_i\eta e_i=Y_F\). Since \(\|Y_F\|\le\|\eta\|=1\), (ii) gives \(\|X_F\|^2\le\delta\), and \(\|Y_F\|^2\ge\varepsilon_0\). \(\square\)

## 5. Random signs and the criterion

**Lemma 5.1.** Let \(\eta\in H\) with \(\langle\eta,\xi\rangle=0\), and \(0<\delta\le1\). There is a projection \(p\in M\) with
\[
\|p\xi-\xi p\|^2\le\delta,\qquad\|p\eta-\eta p\|^2\ge\varepsilon_1\|\eta\|^2,\qquad\varepsilon_1=\frac{2^{-20}}{\kappa}.
\]

**Proof.** We may assume \(\eta\ne0\). *Step 1: \(\eta\in H_{\mathrm{sa}}\), \(\|\eta\|=1\).* Lemma 4.2 with \(\delta/4\) gives \((e_i)\); the family is countable, because \(\varphi\) is faithful and \(\sum_i\varphi(e_i)=1\). Enumerate it as \(e_1,e_2,\ldots\), let \(f_n=1-\sum_{i\le n}e_i\), and for \(g\in\{-1,1\}^n\) let \(u_g=\sum_{i\le n}g_ie_i+f_n\), a self-adjoint unitary of \(M\). Expanding \(u_g\zeta u_g\) and averaging over the \(2^n\) sign vectors kills every cross term, since the average of \(g_ig_j\) (\(i\ne j\)) and of \(g_i\) is zero:
\[
\frac1{2^n}\sum_gu_g\zeta u_g=\Pi_n(\zeta),\qquad\Pi_n(\zeta)=\sum_{i\le n}e_i\zeta e_i+f_n\zeta f_n .
\]
As \(n\to\infty\), \(f_n\to0\) strongly, so \(\Pi_n(\zeta)\to\sum_ie_i\zeta e_i\). Choose \(n\) with \(\|\eta-\Pi_n(\eta)\|^2\ge\varepsilon_0/2\) and \(\|\xi-\Pi_n(\xi)\|\le\frac34\sqrt\delta\) (possible as \(\|\xi-\sum e_i\xi e_i\|\le\frac12\sqrt\delta\)). The average of the vectors \(\eta-u_g\eta u_g\) is \(\eta-\Pi_n(\eta)\), so some \(g\) has \(\|\eta-u_g\eta u_g\|^2\ge\varepsilon_0/2\). As \(u_g^2=1\), \(\eta-u_g\eta u_g=(\eta u_g-u_g\eta)u_g\), and right multiplication by a unitary is isometric; so \(\|u_g\eta-\eta u_g\|^2\ge\varepsilon_0/2\). Each \(e_i\zeta e_i\) and \(f_n\zeta f_n\) is fixed by \(\zeta\mapsto u_g\zeta u_g\), so \(u_g\Pi_n(\xi)=\Pi_n(\xi)u_g\), and
\[
\|u_g\xi-\xi u_g\|=\|u_g(\xi-\Pi_n(\xi))-(\xi-\Pi_n(\xi))u_g\|\le\tfrac32\sqrt\delta .
\]
The projection \(p=\frac12(1+u_g)\) has \(p\xi-\xi p=\frac12(u_g\xi-\xi u_g)\) and \(p\eta-\eta p=\frac12(u_g\eta-\eta u_g)\), so \(\|p\xi-\xi p\|^2\le\frac9{16}\delta\) and \(\|p\eta-\eta p\|^2\ge\varepsilon_0/8\).

*Step 2: general \(\eta\).* Put \(\eta_1=\frac12(\eta+J\eta)\) and \(\eta_2=\frac1{2i}(\eta-J\eta)\). Both lie in \(H_{\mathrm{sa}}\), \(\eta=\eta_1+i\eta_2\), and both are orthogonal to \(\xi\), since \(\langle J\eta,\xi\rangle=\langle J\eta,J\xi\rangle=\langle\xi,\eta\rangle=0\). As \(\langle\eta_1,\eta_2\rangle\) is real, \(\|\eta\|^2=\|\eta_1\|^2+\|\eta_2\|^2\). Choose \(k\) with \(\|\eta_k\|^2\ge\frac12\|\eta\|^2\) and apply Step 1 to \(\eta_k/\|\eta_k\|\). For \(\zeta\in H_{\mathrm{sa}}\) and a projection \(p\), (1.1) gives \(J(p\zeta-\zeta p)=-(p\zeta-\zeta p)\). So \(p\eta_1-\eta_1p\) and \(i(p\eta_2-\eta_2p)\) lie in \(iH_{\mathrm{sa}}\) and \(H_{\mathrm{sa}}\) respectively, and vectors of these two real subspaces are orthogonal for the real part of the inner product. Hence
\[
\|p\eta-\eta p\|^2=\|p\eta_1-\eta_1p\|^2+\|p\eta_2-\eta_2p\|^2\ge\tfrac{\varepsilon_0}8\|\eta_k\|^2\ge\tfrac{\varepsilon_0}{16}\|\eta\|^2 .\qquad\square
\]

**Theorem 5.2** (Haagerup's criterion [Haagerup], [AHHM, Theorem 7.2]). Let \(M\) be a countably decomposable factor of type III that satisfies Haagerup's condition with some constant \(\kappa\ge1\). Then \(\mathrm B(M,\theta)=\mathbb C1\) for every faithful normal state \(\theta\) on \(M\).

**Proof.** Take a standard form and let \(\xi\in P\) be the vector of \(\theta\); it is cyclic and separating. Let \(a\in\mathrm B(M,\theta)\) and \(a'=a-\theta(a)1\); then \(a'\in\mathrm B(M,\theta)\) and \(\eta=a'\xi\) is orthogonal to \(\xi\). Lemma 5.1 with \(\delta=1/n\) gives projections \(p_n\) with \(\|p_n\xi-\xi p_n\|^2\le1/n\) and \(\|p_n\eta-\eta p_n\|^2\ge\varepsilon_1\|\eta\|^2\). By (1.3), \(\|[p_n,\theta]\|\le2n^{-1/2}\), so \((p_n)\in\mathrm{AC}(M,\theta)\) and \(\|[a',p_n]\|_\theta\to0\). Now
\[
p_n\eta-\eta p_n=p_na'\xi-a'(\xi p_n)=(p_na'-a'p_n)\xi+a'(p_n\xi-\xi p_n),
\]
so \(\|p_n\eta-\eta p_n\|\le\|[p_n,a']\|_\theta+\|a'\|n^{-1/2}\to0\). Hence \(\eta=0\); as \(\xi\) is separating, \(a'=0\) and \(a\in\mathbb C1\). \(\square\)

The condition of Definition 1.1 is about single elements \(x\) and single states, while the conclusion concerns all of \(\mathrm B(M,\theta)\). The passage from one to the other is the exhaustion of Lemma 4.2, which uses Haagerup's condition in every corner \(qMq\), and the averaging over signs in Lemma 5.1. In the last lesson the condition is verified for a self-bicentralizing factor whose bicentralizer flow is trivial, using states on \(B(H)\) that are invariant under the modular group.

## 6. Exercises

**Exercise 6.1.** Show that the inequalities (3.2) are sharp: find \(s,t\) with equality on the left and \(s,t\) with equality on the right.

**Exercise 6.2.** Let \((e_i)\) be pairwise orthogonal projections of \(M\) with \(\sum_ie_i=1\). Show that \(\zeta\mapsto\sum_ie_i\zeta e_i\) is the orthogonal projection of \(H\) onto \(\{\zeta:e_i\zeta=\zeta e_i\text{ for all }i\}\).

**Exercise 6.3.** Let \(\psi,\varphi\) be normal positive functionals and \(K\ge0\). Show that \(\psi(p)\le K\varphi(p)\) for every projection \(p\) implies \(\psi\le K\varphi\).

**Exercise 6.4.** In Lemma 2.1, Case 1, show that the element \(x\) is unique: if \(x_1\xi=x_2\xi\) for \(x_1,x_2\in M\), then \(x_1=x_2\). Show also that \(x\xi=\xi x^*\) holds for \(x\in M\) if and only if \(x\xi\in H_{\mathrm{sa}}\).

## 7. Solutions

**6.1.** Equality on the left holds for \(s=-t\), \(t>0\): the middle term is \(2t^2=\frac12(2t)^2\). Equality on the right holds whenever \(st\ge0\), for instance \(s=0\).

**6.2.** The operators \(e_iJe_iJ\) are pairwise orthogonal projections, so \(E=\sum_ie_iJe_iJ\) is a projection, and \(E\zeta=\sum_ie_i\zeta e_i\). If \(e_i\zeta=\zeta e_i\) for all \(i\), then \(e_i\zeta e_i=e_i(e_i\zeta)=e_i\zeta\) and \(E\zeta=\sum_ie_i\zeta=\zeta\). Conversely \(e_k(E\zeta)=e_k\zeta e_k=(E\zeta)e_k\) for every \(k\).

**6.3.** For \(y\ge0\) and \(n\ge1\) let \(y_n=\sum_{k\ge1}\frac kn1_{[k/n,(k+1)/n)}(y)\), a finite positive combination of spectral projections with \(\|y-y_n\|\le\frac1n\). Then \(\psi(y_n)\le K\varphi(y_n)\), and letting \(n\to\infty\) gives \(\psi(y)\le K\varphi(y)\).

**6.4.** \(\xi\) is separating. Next, \(\xi x^*=JxJ\xi=J(x\xi)\), since \(J\xi=\xi\); so \(x\xi=\xi x^*\) says exactly that \(J(x\xi)=x\xi\).

## References

- [Haagerup] U. Haagerup, Connes' bicentralizer problem and uniqueness of the injective factor of type III₁, Acta Mathematica 158 (1987), 95–148. https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6396-11511_2006_Article_BF02392257.pdf
- [AHHM] H. Ando, U. Haagerup, C. Houdayer, A. Marrakchi, Structure of bicentralizer algebras and inclusions of type III factors, Mathematische Annalen 376 (2020), 1145–1194. https://arxiv.org/abs/1804.05706
