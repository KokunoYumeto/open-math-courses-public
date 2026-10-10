# Zero entropy and the eigenvalue two

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson completes the counterexample to the entropy conjecture. Section 1 shows that the map \(f\) of [A clock with registers](a-clock-with-registers.md) has zero topological entropy: the attraction theorem of [Every orbit is attracted](every-orbit-is-attracted.md) reduces the question to the two invariant sets \(Z_0\) and \(Z_\infty\), where the dynamics is a radial register map or a rotation. Sections 2 to 4 find a sphere in \(M\) on which \(f\) acts, up to homotopy, by \(z\mapsto z^2\); since squaring has degree two on the Riemann sphere, the class of this sphere is an eigenvector of \(f_*\) on \(H_2(M;\mathbb R)\) with eigenvalue \(2\). Section 5 states the theorem.

From [Topological entropy and attraction](topological-entropy-and-attraction.md) we use Proposition 1.3 (independence of the metric), Lemma 2.1 (invariant pieces), Theorem 3.1 (entropy localization) and Lemma 4.1 (radial register maps). From [A clock with registers](a-clock-with-registers.md) we use the definitions and Proposition 6.1, and from [Every orbit is attracted](every-orbit-is-attracted.md) Theorem 1.1. For homology we use the core course [Algebraic Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D60) (Fomberg's notes): functoriality [Fomberg, Proposition 1.9], homotopy invariance [Fomberg, Theorem 1.13], maps of pairs and the homotopy invariance of their induced maps [Fomberg, Definition 1.27 and Remark 1.35] and excision [Fomberg, Theorem 1.23]. At the chain level a composite of maps of pairs induces the composite of the chain maps, so functoriality also holds for maps of pairs. From [Orientations and fundamental classes](course:poincare-duality-on-manifolds/orientations-and-fundamental-classes) we use homology with real coefficients (Section 1), the local degree (Proposition 3.2), the real determinant of a complex matrix (Lemma 3.4), the complex orientation (Corollary 3.5), classes on compact sets (Theorem 4.1) and fundamental classes (Corollary 5.1). All homology groups have real coefficients unless stated otherwise.

## 1. Zero entropy

Recall the compact forward invariant sets
\[
Z_0=\{(50\bmod100,\,0,\,\mathbf v):\mathbf v\in\Sigma^q\},\qquad Z_\infty=\{(t,\,\infty,\,0,\ldots,0):t\in\mathbb R/100\mathbb Z\}
\]
of [Every orbit is attracted](every-orbit-is-attracted.md), and the formulas \(f(50,0,\mathbf v)=(50,0,LS(v_1),\ldots,LS(v_q))\) and \(f(t,\infty,0,\ldots,0)=(t+1,\infty,0,\ldots,0)\) from Section 1 there.

**Proposition 1.1.** \(h_{\mathrm{top}}(f|_{Z_0})=0\), \(h_{\mathrm{top}}(f|_{Z_\infty})=0\), and \(h_{\mathrm{top}}(f)=0\).

*Proof.* *The set \(Z_0\).* Let \(T=LS:\Sigma\to\Sigma\). It is continuous, because \(S\) is continuous with values in \(\mathbb C\subseteq\Sigma\). Since \(|S|\leq3\), \(T(\Sigma)\subseteq D_{3L}=\{|v|\leq3L\}\). For \(0<r\leq3L\) we have \(S(re^{i\theta})=p(r)e^{i\theta}\), and \(T(0)=0\); so
\[
T(re^{i\theta})=R(r)e^{i\theta}\quad(0\leq r\leq3L),\qquad R(r)=L\,p(r).
\]
The function \(R:[0,3L]\to[0,3L]\) is continuous and nondecreasing (because \(p\) is nondecreasing on \([0,3L]\) and \(0\leq p\leq3\)), and \(R(0)=0\). By Lemma 4.1 of the first lesson, \(T^{\times q}\) has zero entropy for the maximum metric on \(\Sigma^q\).

The map \(\kappa:\Sigma^q\to Z_0\), \(\kappa(\mathbf v)=(50,0,\mathbf v)\), is a continuous bijection from a compact space onto a Hausdorff space, hence a homeomorphism, and \(f\circ\kappa=\kappa\circ T^{\times q}\). Fix a compatible metric \(d\) on \(M\) and put \(d'(\mathbf u,\mathbf v)=d(\kappa\mathbf u,\kappa\mathbf v)\), a compatible metric on \(\Sigma^q\). Then \(\kappa\) is an isometry from \((\Sigma^q,d')\) onto \((Z_0,d)\) that intertwines \(T^{\times q}\) with \(f|_{Z_0}\); so the two maps have the same separated sets, up to \(\kappa\), and the same entropy. By Proposition 1.3 of the first lesson, the entropy of \(T^{\times q}\) for \(d'\) equals its entropy for the maximum metric, which is zero.

*The set \(Z_\infty\).* There \(f\) advances the clock by one, so \((f|_{Z_\infty})^{100}\) is the identity, and Lemma 2.1(c) of the first lesson gives \(h_{\mathrm{top}}(f|_{Z_\infty})=0\).

*The whole map.* The set \(Z=Z_0\cup Z_\infty\) is compact and forward invariant, and Lemma 2.1(b) of the first lesson gives \(h_{\mathrm{top}}(f|_Z)=\max\{0,0\}=0\). By Theorem 1.1 of [Every orbit is attracted](every-orbit-is-attracted.md), \(d(f^nx,Z)\to0\) for every \(x\in M\). The map \(f\) is continuous (Proposition 6.1 of [A clock with registers](a-clock-with-registers.md)), so Theorem 3.1 of the first lesson applies to \(F=f\) on \(X=M\) and gives \(h_{\mathrm{top}}(f)=0\). \(\square\)

## 2. A sphere on which the map squares

Let \(g:\Sigma\to\Sigma\) be the squaring map, \(g(z)=z^2\) for finite \(z\) and \(g(\infty)=\infty\); in the chart \(w=1/z\) it reads \(w\mapsto w^2\), so \(g\) is smooth. Define
\[
i(z)=(0,z,0,\ldots,0),\qquad j(z)=(1,z,0,\ldots,0),\qquad \pi(t,z,\mathbf v)=z .
\]
These are continuous maps \(i,j:\Sigma\to M\) and \(\pi:M\to\Sigma\), with \(\pi\circ i=\mathrm{id}_\Sigma\).

**Lemma 2.1.** \(f\circ i=j\circ g\), and \(i\) is homotopic to \(j\). Consequently \(f\circ i\) is homotopic to \(i\circ g\).

*Proof.* Let \(z\in\Sigma\) and compute \(f(0,z,0,\ldots,0)\) from (5.2) of [A clock with registers](a-clock-with-registers.md). The clock: \(b(0)=1\) by part (ii) of the clock barrier lemma (\(|0-50|\geq2\)), so \(h(0,z)=1\) and the new reading is \(1\). The main coordinate: for finite \(z\) it is \(z^2+20\sum_\ell\bar\beta_\ell(0)S(0)=z^2\), because \(S(0)=0\); for \(z=\infty\) it is \(\infty\). The registers: \(a(0)S(0)+U_\ell(0,z)=0\), because \(S(0)=0\) and \(U_\ell(0,z)=U^\circ_\ell(0,z)\) contains the factor \(\alpha(0)=0\). Hence \(f(i(z))=(1,g(z),0,\ldots,0)=j(g(z))\).

The map \(K:[0,1]\times\Sigma\to M\), \(K(s,z)=(s\bmod100,z,0,\ldots,0)\), is continuous with \(K(0,\cdot)=i\) and \(K(1,\cdot)=j\). Then \((s,z)\mapsto K(s,g(z))\) is a homotopy from \(i\circ g\) to \(j\circ g=f\circ i\). \(\square\)

## 3. Squaring has degree two

The Riemann sphere is a compact connected complex manifold of complex dimension one: its two charts \(z\) and \(w=1/z\) have the holomorphic transition \(w=1/z\) on \(\mathbb C\setminus\{0\}\), and it is the union of the connected open sets \(\mathbb C\) and \(\Sigma\setminus\{0\}\), which meet. By Corollary 3.5 of [Orientations and fundamental classes](course:poincare-duality-on-manifolds/orientations-and-fundamental-classes) it carries the complex orientation \(x\mapsto\mu_x\), an \(\mathbb R\)-orientation which corresponds in the chart \(z\) to the standard orientation \(\mu^{\rm std}\) of \(\mathbb R^2=\mathbb C\). Precisely: for \(x\in\mathbb C\), the inclusion \(\varepsilon_x:H_2(\mathbb C,\mathbb C\setminus x)\to H_2(\Sigma,\Sigma\setminus x)\) is an isomorphism by excision of the closed set \(\{\infty\}\subseteq\Sigma\setminus x\), and \(\varepsilon_x(\mu^{\rm std}_x)=\mu_x\). By Corollary 5.1 there, the fundamental class \([\Sigma]\) generates \(H_2(\Sigma)\cong\mathbb R\), and for every \(x\) the restriction
\[
\rho_x:H_2(\Sigma)\longrightarrow H_2(\Sigma,\Sigma\setminus x)
\]
is an isomorphism; by Theorem 4.1 there, \(\rho_x[\Sigma]=\mu_x\).

**Proposition 3.1.** \(g_*[\Sigma]=2[\Sigma]\) in \(H_2(\Sigma;\mathbb R)\).

*Proof.* *Local degrees.* In the chart \(z\), \(g\) is the map \(z\mapsto z^2\) of \(\mathbb C=\mathbb R^2\), whose real derivative at \(p\) is the real form of multiplication by \(2p\). By Lemma 3.4 of the orientation lesson (with \(d=1\)) its determinant is \(|2p|^2\), which equals \(4\) at \(p=\pm1\). Proposition 3.2 of the orientation lesson, applied at \(p=1\) and at \(p=-1\), both with \(g(p)=1\), gives open discs \(B_+\) about \(1\) and \(B_-\) about \(-1\) with \(g(x)\neq1\) for \(x\in B_\pm\setminus\{\pm1\}\), such that
\[
g_*:H_2(B_\pm,B_\pm\setminus\{\pm1\})\longrightarrow H_2(\mathbb C,\mathbb C\setminus1)\quad\text{sends }\mu^{\rm std}_{\pm1}\text{ to }\mu^{\rm std}_1 .\tag{3.1}
\]
Here \(\mu^{\rm std}_{\pm1}\) denotes the class in \(H_2(B_\pm,B_\pm\setminus\{\pm1\})\) that the inclusion into \((\mathbb C,\mathbb C\setminus\{\pm1\})\) carries to \(\mu^{\rm std}_{\pm1}\); this inclusion is an excision isomorphism. The proof of that proposition allows any smaller radius, so we take both radii less than one; then \(B_+\cap B_-=\emptyset\), \(-1\notin B_+\) and \(1\notin B_-\).

*Restriction to the preimage.* Let \(P=\{1,-1\}=g^{-1}(1)\). Since \(g(\Sigma\setminus P)\subseteq\Sigma\setminus1\), the map \(g\) is a map of pairs \((\Sigma,\Sigma\setminus P)\to(\Sigma,\Sigma\setminus1)\). As maps of pairs \((\Sigma,\emptyset)\to(\Sigma,\Sigma\setminus1)\), the identity followed by \(g\) equals \(g\) followed by the identity; by functoriality
\[
\rho_1\,g_*[\Sigma]=g_*\,\rho_P[\Sigma],\tag{3.2}
\]
where \(\rho_P:H_2(\Sigma)\to H_2(\Sigma,\Sigma\setminus P)\) is induced by the identity.

*Splitting.* Let \(U=B_+\cup B_-\). The closed set \(\Sigma\setminus U\) lies in the open set \(\Sigma\setminus P\), so excision [Fomberg, Theorem 1.23] shows that the inclusion induces an isomorphism \(e:H_2(U,U\setminus P)\to H_2(\Sigma,\Sigma\setminus P)\). A singular simplex in \(U\) has connected image, so it lies in \(B_+\) or in \(B_-\); the same holds in \(U\setminus P\). Hence the relative chain complex of \((U,U\setminus P)\) is the direct sum of those of \((B_+,B_+\setminus1)\) and \((B_-,B_-\setminus\{-1\})\), and
\[
H_2(U,U\setminus P)=H_2(B_+,B_+\setminus1)\oplus H_2(B_-,B_-\setminus\{-1\}),
\]
the summands being included by the inclusions of pairs. Write \(e^{-1}\rho_P[\Sigma]=(a_+,a_-)\).

*The components.* Let \(r\) be the identity of \(\Sigma\), viewed as a map of pairs \((\Sigma,\Sigma\setminus P)\to(\Sigma,\Sigma\setminus1)\). Then \(r\rho_P=\rho_1\), so \(r(\rho_P[\Sigma])=\mu_1\). On the second summand, \(r\circ e\) is induced by the inclusion \((B_-,B_-\setminus\{-1\})\to(\Sigma,\Sigma\setminus1)\), which factors through \((\Sigma\setminus1,\Sigma\setminus1)\) because \(1\notin B_-\); the relative homology of that pair is zero, so this component vanishes. On the first summand, \(r\circ e\) is the inclusion \(e_+:H_2(B_+,B_+\setminus1)\to H_2(\Sigma,\Sigma\setminus1)\), an isomorphism by excision of \(\Sigma\setminus B_+\subseteq\Sigma\setminus1\). Hence \(e_+(a_+)=\mu_1\). The inclusion \(e_+\) factors through \((\mathbb C,\mathbb C\setminus1)\), so \(e_+(\mu^{\rm std}_1)=\varepsilon_1(\mu^{\rm std}_1)=\mu_1\), and therefore \(a_+=\mu^{\rm std}_1\). In the same way, with the point \(-1\) in place of \(1\), \(a_-=\mu^{\rm std}_{-1}\).

*Conclusion.* By functoriality, \(g_*\circ e\) restricted to the summand of \(B_\pm\) is the map induced by \(g|_{B_\pm}:(B_\pm,B_\pm\setminus\{\pm1\})\to(\Sigma,\Sigma\setminus1)\), which is \(\varepsilon_1\) composed with the map in (3.1). Therefore
\[
g_*\rho_P[\Sigma]=\varepsilon_1(\mu^{\rm std}_1)+\varepsilon_1(\mu^{\rm std}_1)=2\mu_1=\rho_1(2[\Sigma]).
\]
With (3.2) this gives \(\rho_1(g_*[\Sigma])=\rho_1(2[\Sigma])\), and \(\rho_1\) is injective. \(\square\)

The same argument shows that \(z\mapsto z^k\) multiplies \([\Sigma]\) by \(k\) for every \(k\geq1\) (Exercise 6.2).

## 4. The eigenvector

**Theorem 4.1.** The class \(\alpha=i_*[\Sigma]\in H_2(M;\mathbb R)\) is nonzero, and \(f_*\alpha=2\alpha\).

*Proof.* By Lemma 2.1, homotopy invariance and functoriality,
\[
f_*\alpha=(f\circ i)_*[\Sigma]=(i\circ g)_*[\Sigma]=i_*\bigl(g_*[\Sigma]\bigr)=i_*(2[\Sigma])=2\alpha,
\]
using Proposition 3.1. Since \(\pi\circ i=\mathrm{id}_\Sigma\), \(\pi_*\alpha=[\Sigma]\neq0\), so \(\alpha\neq0\). \(\square\)

**Corollary 4.2.** \(\rho(f_*)\geq2\), where \(\rho\) is defined in (2.1) of [Topological entropy and attraction](topological-entropy-and-attraction.md).

*Proof.* As real chain complexes, \(C_\bullet(M;\mathbb C)=C_\bullet(M;\mathbb R)\oplus i\,C_\bullet(M;\mathbb R)\), and the chain map of \(f\) preserves both summands. Hence \(H_2(M;\mathbb C)=H_2(M;\mathbb R)\oplus i\,H_2(M;\mathbb R)\), and the complex linear map \(f_*\) on \(H_2(M;\mathbb C)\) acts on each summand as the real \(f_*\). The vector \(\alpha\) of the first summand is nonzero and satisfies \(f_*\alpha=2\alpha\), so \(2\) is an eigenvalue of \(f_*\) on \(H_2(M;\mathbb C)\). \(\square\)

## 5. The theorem

**Theorem 5.1 (a \(C^1\) counterexample to the entropy conjecture; OpenAI, 2026).** Let \(q\geq2\) and \(M=(\mathbb R/100\mathbb Z)\times\Sigma\times\Sigma^q\), a compact smooth manifold without boundary of dimension \(2q+3\geq7\). The map \(f:M\to M\) of [A clock with registers](a-clock-with-registers.md) is continuously differentiable, neither injective nor surjective, and satisfies
\[
h_{\mathrm{top}}(f)=0<\log2\leq\log\rho(f_*).
\]
More precisely, \(f_*\alpha=2\alpha\) for the nonzero class \(\alpha=i_*[\Sigma]\in H_2(M;\mathbb R)\). So the entropy conjecture (2.1) fails for \(C^1\) maps.

*Proof.* \(f\) is \(C^1\) by Proposition 6.1 of [A clock with registers](a-clock-with-registers.md). It is not injective: \(S\) vanishes on \(\{|v|\geq3L+1\}\cup\{\infty\}\), and \(v_1\) enters (5.2) only through \(S(v_1)\), so changing \(v_1\) within that set does not change the image. It is not surjective: every register output satisfies \(|v_\ell'|\leq L\cdot3+\tfrac15\), so no point with \(v_1=\infty\) is an image. Proposition 1.1 gives \(h_{\mathrm{top}}(f)=0\), and Theorem 4.1 and Corollary 4.2 give the eigenvector and \(\rho(f_*)\geq2\). \(\square\)

The manifold \(M\) is diffeomorphic to \(S^1\times(S^2)^{q+1}\), through \(t\mapsto e^{2\pi it/100}\) and stereographic projection; the theorem is often stated in that form.

**Remark 5.2 (where the homology growth goes).** The classes \(f^n_*\alpha=2^n\alpha\) grow exponentially, while every orbit converges to \(Z_0\cup Z_\infty\), where the entropy is zero. There is no conflict. The localization theorem of the first lesson turns pointwise attraction into zero entropy without any uniform time of approach, and the time of approach is indeed not uniform (Exercise 7.2 of [Every orbit is attracted](every-orbit-is-attracted.md)). A homology class, on the other hand, concerns a whole sphere at once: on \(i(\Sigma)\) the points with \(|z|\leq\tfrac12\) tend to \(Z_0\) and the points with \(|z|\geq2\) tend to \(Z_\infty\) (Exercise 6.5), so the spheres \(f^n\circ i\) stretch between the two sets.

**Remark 5.3 (regularity and known cases).** By Yomdin's theorem the inequality (2.1) holds for \(C^\infty\) maps, so a counterexample cannot be smooth of all orders; the construction controls only first derivatives (Remark 6.2 of [A clock with registers](a-clock-with-registers.md)). The eigenvalue lies in \(H_2\) of a manifold of dimension at least seven, neither in first homology (Manning's theorem) nor in top homology (Misiurewicz and Przytycki), and \(f\) is not a diffeomorphism. These results are named in the first lesson for context; they are not used in the proof.

**Remark 5.4 (formal verification).** OpenAI's release contains a Lean formalization of Theorem 5.1. Its formal statement says: for some \(q>0\) there is a self-map \(f\) of \(S^1\times(S^2)^{q+1}\) that is \(C^1\) (locally the restriction of a \(C^1\) map of the ambient Euclidean space), has topological entropy zero (Mathlib's cover entropy) and has a nonzero \(v\in H_2(S^1\times(S^2)^{q+1};\mathbb R)\) with \(f_*v=2v\); moreover \(\log2\) is at most the logarithm of the spectral radius of \(f_*\) on real homology, \(f\) is not bijective, and \(2q+3\geq5\). The formal construction uses three registers, with readout windows about \(76\), \(76.5\) and \(77\) (Exercise 6.4).

## 6. Exercises

**6.1.** Let \(C(t,\mathbf v)=20\sum_\ell\bar\beta_\ell(t)S(v_\ell)\). Show that \(H_s(t,z,\mathbf v)=z^2+sC(t,\mathbf v)\) for finite \(z\), and \(H_s(t,\infty,\mathbf v)=\infty\), defines a homotopy \(H:[0,1]\times M\to\Sigma\) from \(g\circ\pi\) to \(\pi\circ f\). Deduce \(\pi_*f_*=g_*\pi_*\) on \(H_2(M)\), and check that this agrees with Theorem 4.1.

**6.2.** Let \(k\geq1\) and \(g_k(z)=z^k\), \(g_k(\infty)=\infty\). Show that \((g_k)_*[\Sigma]=k[\Sigma]\).

**6.3.** Show that \(f^n\circ i\) is homotopic to \(i\circ g_{2^n}\) for every \(n\geq1\), and deduce \(f^n_*\alpha=2^n\alpha\) in two ways.

**6.4.** Explain why a single readout window cannot satisfy condition (3.1) of [A clock with registers](a-clock-with-registers.md). For \(c=76,76.5,77\) let \(\beta_c\) be a smooth function with values in \([0,1]\) that vanishes outside \((c-\tfrac25,c+\tfrac25)\) and equals one on \([c-\tfrac14,c+\tfrac14]\). Check that these three windows satisfy all the requirements on the \(\beta_\ell\) there.

**6.5.** Show that on \(i(\Sigma)\) the points with \(|z|\leq\tfrac12\) tend to \(Z_0\), and the points with \(|z|\geq2\), including \(z=\infty\), tend to \(Z_\infty\).

## 7. Solutions

**6.1.** For finite \(z\), \(H_s\) is a continuous function of \((s,t,z,\mathbf v)\). Near \(z=\infty\), in the coordinates \(w=1/z\) and \(w'=1/H_s\), we get \(w'=w^2/(1+sC\,w^2)\), as in (6.4) of [A clock with registers](a-clock-with-registers.md). Since \(|sC|\leq60q\), the denominator has modulus at least \(\tfrac12\) for \(|w|<(120q)^{-1/2}\), uniformly in \(s\), \(t\) and \(\mathbf v\); so \(w'\) is continuous there, with value \(0\) at \(w=0\). Thus \(H\) is continuous, \(H_0=g\circ\pi\) and \(H_1=\pi\circ f\). Homotopy invariance gives \(\pi_*f_*=g_*\pi_*\). Applied to \(\alpha\): \(\pi_*f_*\alpha=g_*[\Sigma]=2[\Sigma]\), and also \(\pi_*(2\alpha)=2[\Sigma]\).

**6.2.** The preimage of \(1\) is the set \(P_k\) of \(k\)-th roots of unity, and \(g_k(\Sigma\setminus P_k)\subseteq\Sigma\setminus1\). At \(\zeta\in P_k\) the complex derivative is \(k\zeta^{k-1}\neq0\), with real determinant \(k^2>0\). Repeat the proof of Proposition 3.1 with \(k\) disjoint discs about the points of \(P_k\): each contributes \(\mu_1\), so \(\rho_1((g_k)_*[\Sigma])=k\mu_1\).

**6.3.** By induction, using that composition preserves homotopies:
\[
\begin{aligned}
f^{n+1}\circ i&=f\circ(f^n\circ i)\simeq f\circ i\circ g_{2^n}\\
&\simeq i\circ g\circ g_{2^n}=i\circ g_{2^{n+1}}.
\end{aligned}
\]
Hence \(f^n_*\alpha=i_*(g_{2^n})_*[\Sigma]=2^n\alpha\) by Exercise 6.2; alternatively apply Theorem 4.1 \(n\) times.

**6.4.** The support of a single window lies in an interval of length less than one, while (3.1) asks that the window equal one on all of \([76,77]\), which has length one. For the three windows: the support of \(\beta_c\) is contained in \([c-\tfrac25,c+\tfrac25]\), hence in the open interval \(J_c=(c-\tfrac9{20},c+\tfrac9{20})\) of length \(\tfrac9{10}<1\), and \(J_c\subseteq(75.55,77.45)\subseteq(74,80)\). The sets where they equal one cover \([75.75,77.25]\supseteq[76,77]\). Such functions exist: take a cutoff for \(([c-\tfrac14,c+\tfrac14],(c-\tfrac25,c+\tfrac25))\).

**6.5.** Start at \(i(z)=(0,z,0,\ldots,0)\). If \(|z|\leq\tfrac12\), then as long as the clock reading \(s_n\) lies in \([0,50]\) and \(|z_n|\leq\tfrac12\), no readout occurs, \(z_{n+1}=z_n^2\), and \(e(z_n)=0\), so \(s_{n+1}=s_n+b(s_n)\leq50\) by part (iii) of the clock barrier lemma. By induction the clock never exceeds \(50\), and Lemma 2.1 of [Every orbit is attracted](every-orbit-is-attracted.md) gives \(t_n\to50\) and \(z_n\to0\). If \(2\leq|z|<\infty\), then \(\chi(z_n)=0\) as long as \(|z_n|\geq2\), so the inputs vanish, the registers stay zero, the readouts add \(20\sum_\ell\bar\beta_\ell S(0)=0\), and \(z_{n+1}=z_n^2\); by induction \(z_n=z^{2^n}\to\infty\) with zero registers. For \(z=\infty\) the orbit lies in \(Z_\infty\).

## References

- [OpenAI-C1] OpenAI, *A \(C^1\) counterexample to the entropy conjecture*, OpenAI Math Release preprint, 25 September 2026, Sections 4 and 5. https://github.com/openai/math/tree/main/preprints/A-C1-Counterexample-to-the-Entropy-Conjecture-September-25-2026
- [OpenAI-Lean] OpenAI Math Release, *A \(C^1\) counterexample to the entropy conjecture*, scope of the Lean formalization. https://github.com/openai/math/blob/main/lean/docs/151.md
- [Fomberg] Y. Fomberg, *Algebraic Topology*, lecture notes (lectures by N. Lazarovich, Spring 2025); a text of the core course Algebraic Topology. https://yp.srht.site/notes/math/algebraic_topology.pdf
