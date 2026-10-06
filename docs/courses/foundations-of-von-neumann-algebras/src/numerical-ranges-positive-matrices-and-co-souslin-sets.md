# Spectral estimates and Borel selection: two reading routes

*Original lesson by Claude Opus 5.5 (Anthropic). Learner routes, explanatory checkpoints and proof self-checks by GPT-6.1 Sol (OpenAI), at Ultra, October 2026. The perturbation estimate in Proposition 1.4a and its proof were added by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Original course contributions: CC0.*

There are two independent entrances to this lesson. The spectral route estimates an operator or algebra element from scalar observations and norms, then studies iteration of a positive matrix. The selection route constructs measurable choices by coding countable trees and well-orders. Read the route needed for the current problem; neither requires the other.

For the spectral route, imagine repeatedly applying a matrix with positive entries. Which direction dominates its powers, and how does the norm reveal a spectral bound? Numerical ranges connect scalar observations to exponential growth; the Perron–Frobenius proof then controls the dominant direction and every other eigenvalue. The exact positive and primitive hypotheses matter.

For the selection route, imagine a measurable family of nonempty closed sets and ask for one point in each. Successive choices form branches in a tree. Well-founded trees supply ordinal ranks, and the separation and reduction theorems turn those ranks into Borel constructions. This route starts after the positive-matrix proof and uses the Borel-model lesson, not the numerical-range results.

The original theorem labels remain the cross-references used by the separate routes and exercises. The scalar and ordinal background proofs are placed at their respective entrances.

## Conventions

- \(\mathbb N=\{1,2,3,\dots\}\). "Countable" means finite or countably infinite.
- Algebras are complex. In Sections 1–3, a *unital Banach algebra* is a Banach algebra \(A\) with an identity \(1\) of norm \(\|1\|=1\); in particular \(A\neq\{0\}\). Every unital Banach algebra with \(1\neq0\) has an equivalent algebra norm of this kind ([the norm of the identity](banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.md#oa-fnd-bn-03)). We write \(\lambda\) for \(\lambda1\), \(\sigma(a)\) for the spectrum, \(r(a)\) for the spectral radius, and \(e^{a}=\sum_{n\geq0}a^n/n!\). \(A^*\) is the space of bounded linear functionals on \(A\).
- In Section 4, \(n\geq1\), and vectors \(x\in\mathbb C^n\) are columns, \(|x|=(|x_1|,\dots,|x_n|)\), and \(\mathbf 1=(1,\dots,1)\). For real vectors, \(x\leq y\) means \(x_i\leq y_i\) for all \(i\). We write \(x\geq0\) if every \(x_i\geq0\), and \(x\gg0\) if every \(x_i>0\); the same notation is used entrywise for matrices. \(T^{\top}\) is the transpose, and \(u^{\top}x=\sum_iu_ix_i\). On \(\mathbb C^n\) we use \(\|x\|=\max_i|x_i|\), and on matrices the corresponding operator norm \(\|T\|=\max_i\sum_j|t_{ij}|\), which makes \(M_n(\mathbb C)\) a unital Banach algebra.
- In Sections 5–11, Borel spaces, standard Borel spaces, Polish spaces and Souslin sets are as in [Polish spaces and standard Borel spaces](polish-spaces-and-standard-borel-spaces.md#oa-fnd-pb-02). In a standard Borel space, the *Souslin sets* are the empty set and the images of standard Borel spaces under Borel maps; for every Polish topology that generates the Borel sets, these are exactly the continuous images of Polish spaces ([Souslin–Borel spaces](polish-spaces-and-standard-borel-spaces.md#oa-fnd-pb-08)). \(\Lambda=\mathbb N^{\mathbb N}\) is the Baire space, \(\mathbb N^{<\mathbb N}\) consists of the finite sequences \(s=(s_1,\dots,s_k)\) including the empty sequence \(\varnothing\), \(|s|=k\) the length, \(t|k=(t_1,\dots,t_k)\), and \(\Lambda_s=\{t\in\Lambda:t|\,|s|=s\}\), as in that lesson. \(\mathcal C=\{0,1\}^{\mathbb N}\) is the Cantor space.
- For a countable set \(Y\), a subset \(S\subseteq Y\) is identified with its indicator function, a point of \(2^Y=\{0,1\}^Y\). With the product topology, \(2^Y\) is compact and metrizable, hence Polish. The sets \(\{S:y\in S\}\) and \(\{S:y\notin S\}\) are open and closed, and the maps \(S\mapsto1_S(y)\), \(y\in Y\), generate the Borel sets.

## A. Estimate spectra and understand positive iteration

Start with norm-one unital functionals. They produce a compact convex numerical range containing the spectrum, but in a general Banach algebra they must not be silently identified with C*-algebra states. The norm-derivative and exponential formulas explain what those observations measure. Hermitian elements and positive matrices then give two different ways to sharpen the resulting spectral estimates.

### Scalar estimates for the spectral route

*From [Banach algebras, spectrum, holomorphic functional calculus and Gelfand theory](banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.md).* Let \(A\) be a unital Banach algebra and \(x\in A\).

- **(B1)** \(\sigma(x)\) is compact, nonempty, and lies in \(\{|\lambda|\leq\|x\|\}\); \(\sigma(\alpha+\beta x)=\alpha+\beta\sigma(x)\) for \(\alpha,\beta\in\mathbb C\); \(r(x)=\lim_n\|x^n\|^{1/n}=\inf_n\|x^n\|^{1/n}\); and \(\|(\lambda-x)^{-1}\|\geq1/\operatorname{dist}(\lambda,\sigma(x))\) for \(\lambda\notin\sigma(x)\). See [spectrum](banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.md#oa-fnd-bn-06), [the resolvent](banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.md#oa-fnd-bn-07), [nonempty spectrum](banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.md#oa-fnd-bn-08) and [the spectral radius formula](banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.md#oa-fnd-bn-09).
- **(B2)** *Holomorphic functional calculus.* For \(f\) holomorphic on an open set \(U\supseteq\sigma(x)\), an element \(f(x)\) is defined. The map \(f\mapsto f(x)\) is a unital algebra homomorphism, \(u(x)=x\) for \(u(\lambda)=\lambda\), and \(f(x)=g(x)\) whenever \(f=g\) on an open set containing \(\sigma(x)\). If \(f(\lambda)=\sum_nc_n\lambda^n\) for \(|\lambda|<\rho_0\) and \(r(x)<\rho_0\), then \(f(x)=\sum_nc_nx^n\), with convergence in norm. Moreover \(\sigma(f(x))=f(\sigma(x))\), and \((g\circ f)(x)=g(f(x))\) whenever \(g\) is holomorphic on an open set containing \(f(\sigma(x))\). See [the definition](banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.md#oa-fnd-bn-10), [the homomorphism property and power series](banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.md#oa-fnd-bn-11), and [spectral mapping and composition](banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.md#oa-fnd-bn-12).
- **(B3)** The series \(e^x=\sum_nx^n/n!\) converges absolutely and is the functional calculus of \(\lambda\mapsto e^\lambda\). If \(xy=yx\), then \(e^{x+y}=e^xe^y\); so \(e^x\) is invertible, and \(t\mapsto e^{tx}\) is norm continuous. See [the exponential](banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.md#oa-fnd-bn-14).
- **(B4)** For a discrete group \(G\) with identity \(e\), the space \(\ell^1(G)\) with the product \((x\ast y)(g)=\sum_hx(h)y(h^{-1}g)\), the \(\ell^1\) norm and the involution \(x^*(g)=\overline{x(g^{-1})}\) is a Banach algebra with isometric involution, with identity \(\delta_e\) and \(\|\delta_e\|=1\) ([group algebras](banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.md#oa-fnd-bn-20)). For \(G=\mathbb Z\), the Fourier transform identifies \(\ell^1(\mathbb Z)\) with the algebra of absolutely convergent Fourier series, and the spectrum of an element is the range of the corresponding function on the circle ([the Wiener algebra](banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.md#oa-fnd-bn-21), [the Gelfand representation](banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.md#oa-fnd-bn-18)). In particular \(\delta_1+\delta_{-1}\) corresponds to \(s\mapsto2\cos2\pi s\), and its spectrum is \([-2,2]\).

*From [C\*-algebras: continuous functional calculus, automatic continuity, positive cones, approximate identities and quotients](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md).* Let \(A\) be a unital C\*-algebra with \(1\neq0\); then \(\|1\|=1\).

- **(C1)** For \(h=h^*\), \(\sigma(h)\subseteq[-\|h\|,\|h\|]\) and \(r(h)=\|h\|\). For every \(x\), \(\|x\|^2=\|x^*x\|\) ([self-adjoint and normal elements](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-01)).
- **(C2)** The set \(A_+\) of self-adjoint elements with spectrum in \([0,\infty)\) is a convex cone. For every \(x\in A\), both \(x^*x\) and \(\|x\|^2-x^*x\) lie in \(A_+\) ([the positive cone](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-15)). A linear functional \(\varphi\) is *positive* if \(\varphi(A_+)\subseteq[0,\infty)\), and a *state* is a positive linear functional of norm one ([states](c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.md#oa-fnd-cf-22)).

*Functional analysis.*

- **(H1)** (Hahn–Banach theorem, real form) Let \(E\) be a real vector space, \(p\) a seminorm on \(E\), \(M\subseteq E\) a subspace and \(\psi_0\) a linear functional on \(M\) with \(\psi_0\leq p\) on \(M\). Then \(\psi_0\) extends to a linear functional \(\psi\) on \(E\) with \(\psi\leq p\) [Theorem 2.1 of the Hahn–Banach lesson](hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.md#oa-fnd-hb-02) proves this, even for a sublinear bound.
- **(H2)** (Complex form) If \(\psi\) is a real-linear functional on a complex normed space with \(|\psi(x)|\leq\|x\|\), then \(\omega(x)=\psi(x)-i\psi(ix)\) is complex-linear, \(\operatorname{Re}\omega=\psi\), and \(|\omega(x)|\leq\|x\|\). Every linear functional on a subspace that is bounded by the norm extends to the whole space with the same bound; in particular every vector \(x_0\) has some \(\omega\) with \(\|\omega\|\leq1\) and \(\omega(x_0)=\|x_0\|\) [Theorem 2.2 and Corollary 2.3 of the Hahn–Banach lesson](hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.md#oa-fnd-hb-02) give the full scalar-rotation and extension proofs.
- **(H3)** (Banach–Alaoglu theorem) The closed unit ball of the dual of a normed space is weak\*-compact [Theorem 3.1 of the weak-topology lesson](weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian.md#oa-fnd-wt-03) proves this for every normed space.

#### Elementary scalar facts

A closed interval is compact. Otherwise bisect an interval with an open cover having no finite subcover, repeatedly retaining a closed half with the same property. The nested halves have lengths tending to zero and one common point, by completeness of the real numbers. An open set of the cover containing that point contains every sufficiently small retained half, a contradiction. Finite products of these intervals are compact by [Tychonoff's theorem](weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian.md#oa-fnd-wt-02). A closed bounded subset of \(\mathbb C^n=\mathbb R^{2n}\) is a closed subset of such a compact box, hence compact. Equivalence of finite-dimensional norms is proved in [Theorem 7.1 of the Hahn–Banach lesson](hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.md#oa-fnd-hb-07), using this compactness. The [sequential compactness argument](polish-spaces-and-standard-borel-spaces.md) lets us pass to the convergent vector sequence in Theorem 4.2. The identity theorem used in Lemma 3.3 is [Theorem 3.7 of the Cauchy lesson](cauchy-s-theorem-for-cycles-and-its-consequences.md#oa-fnd-ct-03).

Here are the two scalar computations also used there. If \(|\sum_j z_j|=\sum_j|z_j|\) and the sum is nonzero, multiply by a unit complex number to make the sum positive real. Since \(\operatorname{Re}z_j\leq|z_j|\), equality of their sums makes every rotated \(z_j\) nonnegative real. Thus all nonzero terms have the same argument. If the sum is zero, equality forces every term to be zero. From the exponential definitions and multiplication of absolutely convergent series,
\[
\sin(x+iy)=\sin x\cosh y+i\cos x\sinh y.
\]
Consequently
\[
\begin{gathered}
|\sin(x+iy)|^2\\
=\sin^2x\cosh^2y+\cos^2x\sinh^2y
\\
=\sin^2x+\sinh^2y,
\end{gathered}
\]
using \(\sin^2x+\cos^2x=1\) and \(\cosh^2y-\sinh^2y=1\), which follow by expanding the same exponential definitions.

Finally \(1-1/y\leq\log y\leq y-1\) for \(y>0\), as used in Theorem 2.3: the derivatives of \(y-1-\log y\) and \(\log y-1+1/y\) are respectively \((y-1)/y\) and \((y-1)/y^2\). Each function decreases up to \(1\), increases after \(1\), and equals zero there.

### 1. Unital functionals and the numerical range

In Sections 1–3, \(A\) is a unital Banach algebra, so \(\|1\|=1\). The numerical-range arguments in Sections 1–3 are proved below.

**Definition 1.1.** A functional \(\omega\in A^*\) is *unital* if \(\omega(1)=1=\|\omega\|\). Let \(V(A)\) be the set of unital functionals. The *numerical range* of \(a\in A\) is
\[
W(a)=W_A(a)=\{\omega(a):\ \omega\in V(A)\},
\]
and the *numerical radius* of \(a\) is \(v(a)=\max\{|z|:z\in W(a)\}\).

For example, let \(A=B(H)\) for a Hilbert space \(H\neq0\), and let \(\xi\in H\) be a unit vector. The functional \(x\mapsto\langle x\xi,\xi\rangle\) takes the value \(\|\xi\|^2=1\) at \(1\), and \(|\langle x\xi,\xi\rangle|\leq\|x\|\). So it is unital, and \(W(x)\) contains every value of the quadratic form \(\xi\mapsto\langle x\xi,\xi\rangle\) on the unit sphere. For a general C\*-algebra, Corollary 3.6 shows that the unital functionals are exactly the states.

**Proposition 1.2.** Let \(a,b\in A\).
1. \(V(A)=\{\omega\in A^*:\ \|\omega\|\leq1,\ \omega(1)=1\}\). This set is nonempty, convex and weak\*-compact.
2. \(W(a)\) is a nonempty compact convex subset of the closed disc of radius \(\|a\|\).
3. \(W(\alpha+\beta a)=\alpha+\beta W(a)\) for \(\alpha,\beta\in\mathbb C\), and \(W(a+b)\subseteq W(a)+W(b)\).

**Proof.** (1) If \(\omega(1)=1\), then \(1=|\omega(1)|\leq\|\omega\|\,\|1\|=\|\omega\|\). So \(\|\omega\|\leq1\) and \(\omega(1)=1\) together give \(\|\omega\|=1\). The set is convex, and it is weak\*-closed in the closed unit ball of \(A^*\), which is weak\*-compact by (H3). By (H2) some \(\omega\) has \(\|\omega\|\leq1\) and \(\omega(1)=\|1\|=1\), so the set is not empty.

(2) The map \(\omega\mapsto\omega(a)\) is affine and weak\*-continuous. It carries the nonempty compact convex set \(V(A)\) onto a nonempty compact convex set, and \(|\omega(a)|\leq\|\omega\|\,\|a\|=\|a\|\).

(3) For \(\omega\in V(A)\), \(\omega(\alpha+\beta a)=\alpha+\beta\omega(a)\) and \(\omega(a+b)=\omega(a)+\omega(b)\). \(\square\)

The next theorem shows that \(W(a)\) depends only on the norm on the space spanned by \(1\) and \(a\).

**Theorem 1.3.** Let \(a\in A\) and \(\alpha\in\mathbb C\). The following are equivalent.
1. \(\alpha\in W(a)\).
2. The formula \(f(\lambda+\mu a)=\lambda+\mu\alpha\), for \(\lambda,\mu\in\mathbb C\), defines a linear functional \(f\) on \(\operatorname{span}\{1,a\}\) with \(|f(y)|\leq\|y\|\).
3. \(|\lambda+\mu\alpha|\leq\|\lambda+\mu a\|\) for all \(\lambda,\mu\in\mathbb C\).
4. \(|\lambda+\alpha|\leq\|\lambda+a\|\) for all \(\lambda\in\mathbb C\).

**Proof.** (1) ⇒ (4). If \(\alpha=\omega(a)\) with \(\omega\in V(A)\), then \(|\lambda+\alpha|=|\omega(\lambda+a)|\leq\|\lambda+a\|\).

(4) ⇒ (3). For \(\mu=0\) the claim reads \(|\lambda|\leq\|\lambda1\|\), which is an equality. For \(\mu\neq0\), apply (4) to \(\lambda/\mu\) and multiply by \(|\mu|\).

(3) ⇒ (2). If \(\lambda+\mu a=\lambda'+\mu'a\), then (3) for the pair \((\lambda-\lambda',\mu-\mu')\) gives \(|(\lambda-\lambda')+(\mu-\mu')\alpha|\leq0\), so \(\lambda+\mu\alpha=\lambda'+\mu'\alpha\). Hence \(f\) is well defined, also when \(1\) and \(a\) are linearly dependent. It is linear, and (3) is the bound \(|f(y)|\leq\|y\|\).

(2) ⇒ (1). By (H2), \(f\) extends to some \(\omega\in A^*\) with \(\|\omega\|\leq1\). Then \(\omega(1)=f(1)=1\), so \(\omega\in V(A)\) by Proposition 1.2(1), and \(\omega(a)=f(a)=\alpha\). \(\square\)

**Corollary 1.4.** Let \(a\in A\).
1. If \(B\subseteq A\) is a closed subalgebra that contains \(1\) and \(a\), with the norm of \(A\), then \(W_B(a)=W_A(a)\).
2. \(\sigma(a)\subseteq W(a)\). Hence \(W(a)\) contains the convex hull of \(\sigma(a)\), and \(r(a)\leq v(a)\leq\|a\|\).

**Proof.** (1) Condition (4) of Theorem 1.3 involves only the norms of the elements \(\lambda+a\), which lie in \(B\).

(2) Let \(\alpha\in\sigma(a)\) and \(\lambda\in\mathbb C\). By (B1), \(\lambda+\alpha\in\sigma(\lambda+a)\), so \(|\lambda+\alpha|\leq r(\lambda+a)\leq\|\lambda+a\|\). Theorem 1.3 gives \(\alpha\in W(a)\). The rest follows from the convexity of \(W(a)\) and from Proposition 1.2(2). \(\square\)

Part (1) is in contrast with the spectrum, which can shrink when the algebra grows; see the example of the disc algebra in [the lesson on Banach algebras](banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.md).

**Proposition 1.4a** (Stability under norm perturbation). For \(a,b\in A\), the Hausdorff distance between their numerical ranges is at most \(\|a-b\|\). In particular, both the numerical radius and the largest real part of the numerical range change by at most \(\|a-b\|\).

Here the Hausdorff distance of nonempty compact sets \(K,L\subseteq\mathbb C\) is the larger of \(\sup_{z\in K}\inf_{w\in L}|z-w|\) and \(\sup_{w\in L}\inf_{z\in K}|z-w|\). The numerical-range estimate is Lemma 2.1 of [H. Blazhko, D. Homza, F. L. Schwenninger, J. de Vries and M. Wojtylak, *The algebraic numerical range as a spectral set in Banach algebras* (2025)](https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/algebraic-numerical-range-as-a-spectral-set-in-banach-algebras/96536D155B032F6C67B750582F5DBF07#sec2).

**Proof.** Put \(\delta=\|a-b\|\). If \(z\in W(a)\), choose \(\omega\in V(A)\) with \(z=\omega(a)\). The point \(w=\omega(b)\) belongs to \(W(b)\), and
\[
|z-w|=|\omega(a-b)|\le\delta.
\]
Thus every point of \(W(a)\) is within \(\delta\) of \(W(b)\). Interchanging \(a\) and \(b\) gives the other half of the Hausdorff estimate. Since \(|z|\le |w|+\delta\), taking maxima gives \(v(a)\le v(b)+\delta\); interchanging the elements yields the absolute-difference bound. Likewise \(\operatorname{Re}z\le\operatorname{Re}w+\delta\), which proves the claim about largest real parts. The same argument applies to \(e^{i\theta}a,e^{i\theta}b\) for every real \(\theta\), with the same constant. It needs only the norm-one functionals and their common domain, so it also holds in the normed-space formulation of Remark 1.5. \(\square\)

**Remark 1.5** (only the norm and the unit matter). Apart from the spectrum in Corollary 1.4(2), nothing in this section used the product of \(A\). For a complex normed space \(E\) and a vector \(e\in E\) with \(\|e\|=1\), define \(V(E,e)\) and \(W(x)\), \(x\in E\), as above with \(e\) in place of \(1\). Proposition 1.2, Theorem 1.3 and Corollary 1.4(1) hold with the same proofs, and so do parts (1) and (2) of Theorem 2.3 below. The product enters through the spectrum and through the exponential in Theorem 2.3(3).

### 2. The numerical range from the norm

For \(a\in A\) let \(m(a)=\max\operatorname{Re}W(a)\), the largest real part of a point of \(W(a)\); it exists because \(W(a)\) is compact. For real \(\theta\), \(W(e^{i\theta}a)=e^{i\theta}W(a)\) by Proposition 1.2(3), so
\[
m(e^{i\theta}a)=\max_{z\in W(a)}\operatorname{Re}\big(e^{i\theta}z\big).
\]
By the next lemma these numbers determine \(W(a)\).

**Lemma 2.1** (support functions). Let \(K\subseteq\mathbb C\) be nonempty, compact and convex, and put \(h_K(\theta)=\max_{z\in K}\operatorname{Re}(e^{i\theta}z)\) for \(\theta\in\mathbb R\). Then
\[
\begin{gathered}
K\\
=\{z\in\mathbb C :\ \operatorname{Re}(e^{i\theta}z)\leq h_K(\theta)\text{ for all }\theta\in\mathbb R\}.
\end{gathered}
\]
Hence two nonempty compact convex sets with the same function \(h\) are equal. If \(h_K(\theta)=R\) for every \(\theta\), then \(K\) is the closed disc \(\{|z|\leq R\}\).

**Proof.** Every point of \(K\) lies in the set on the right. Let \(p\notin K\), and let \(q\in K\) be a point nearest to \(p\), which exists because \(K\) is compact. For \(z\in K\) and \(0<s\leq1\) the point \(q+s(z-q)\) lies in \(K\), so
\[
\begin{gathered}
|p-q|^2\\
\leq|p-q-s(z-q)|^2\\
=|p-q|^2-2s\operatorname{Re}\big(\overline{(p-q)}(z-q)\big)\\
+s^2|z-q|^2 .
\end{gathered}
\]
Dividing by \(s\) and letting \(s\to0\) gives \(\operatorname{Re}\big(\overline{(p-q)}(z-q)\big)\leq0\). Choose \(\theta\) with \(e^{i\theta}=\overline{(p-q)}/|p-q|\). Then \(\operatorname{Re}(e^{i\theta}z)\leq\operatorname{Re}(e^{i\theta}q)\) for all \(z\in K\), so \(h_K(\theta)=\operatorname{Re}(e^{i\theta}q)\), while \(\operatorname{Re}(e^{i\theta}p)=\operatorname{Re}(e^{i\theta}q)+|p-q|>h_K(\theta)\). So \(p\) is not in the set on the right. If \(h_K\equiv R\), the width \(h_K(\theta)+h_K(\theta+\pi)=2R\) is nonnegative, so \(R\geq0\). The closed disc of radius \(R\) is compact and convex, and its function \(h\) is constant, equal to \(R\); this gives the last claim. \(\square\)

**Lemma 2.2** (subadditive functions near zero). Let \(F:[0,\infty)\to\mathbb R\) satisfy \(F(0)=0\), \(F(s+t)\leq F(s)+F(t)\) for \(s,t\geq0\), and \(F(t)\to0\) as \(t\to0^+\). Suppose that \(\alpha=\sup_{t>0}F(t)/t\) is finite. Then \(F(t)/t\to\alpha\) as \(t\to0^+\).

**Proof.** Clearly \(\limsup_{t\to0^+}F(t)/t\leq\alpha\). Fix \(t>0\). For \(0<s<t\) write \(t=ns+\delta\) with an integer \(n\geq1\) and \(0\leq\delta<s\). Subadditivity gives \(F(t)\leq nF(s)+F(\delta)\), so
\[
\frac{F(t)}{t}\leq\frac{ns}{t}\cdot\frac{F(s)}{s}+\frac{F(\delta)}{t}.
\tag{2.1}
\]
As \(s\to0^+\), \(ns/t\to1\) because \(t-s<ns\leq t\), and \(F(\delta)\to0\) because \(0\leq\delta<s\). Choose \(s_k\to0^+\) with \(F(s_k)/s_k\to L=\liminf_{s\to0^+}F(s)/s\). If \(L\) were \(-\infty\), the right side of (2.1) would tend to \(-\infty\) along \(s_k\), which is impossible; so \(L\) is finite, and (2.1) gives \(F(t)/t\leq L\). Taking the supremum over \(t\) gives \(\alpha\leq L\). \(\square\)

**Theorem 2.3.** Let \(a\in A\).
1. The function \(g(u)=\|u+a\|-u\), \(u\in\mathbb R\), is nonincreasing, and
\[
\begin{gathered}
m(a)\\
=\inf_{u\in\mathbb R}g(u)\\
=\lim_{u\to+\infty}\big(\|u+a\|-u\big)\\
=\inf_{t>0}\frac{\|1+ta\|-1}{t}\\
=\lim_{t\to0^+}\frac{\|1+ta\|-1}{t}.
\end{gathered}
\tag{2.2}
\]
2. \(\operatorname{Re}W(a)=[-m(-a),\,m(a)]\).
3. We have
\[
\begin{gathered}
m(a)\\
=\lim_{t\to0^+}\frac{\|e^{ta}\|-1}{t}\\
=\lim_{t\to0^+}\frac{\log\|e^{ta}\|}{t}\\
=\sup_{t>0}\frac{\log\|e^{ta}\|}{t}.
\end{gathered}
\tag{2.3}
\]
In particular \(\|e^{ta}\|\leq e^{t\,m(a)}\) for all \(t\geq0\), and \(m(a)\) is the smallest real number \(w\) with \(\|e^{ta}\|\leq e^{tw}\) for all \(t\geq0\).

**Proof.** (1) For \(u<u'\), \(\|u'+a\|\leq\|u+a\|+(u'-u)\), so \(g(u')\leq g(u)\). For \(\alpha\in W(a)\) and real \(u\), Theorem 1.3(4) gives \(u+\operatorname{Re}\alpha\leq|u+\alpha|\leq\|u+a\|\), that is, \(\operatorname{Re}\alpha\leq g(u)\). Hence \(m(a)\leq c\), where \(c=\inf_ug(u)\); in particular \(c\) is finite.

For the reverse inequality we find \(\omega\in V(A)\) with \(\operatorname{Re}\omega(a)=c\). Regard \(A\) as a real vector space. If \(a=s_01\) with \(s_0\) real, then \(W(a)=\{s_0\}\) and \(g(u)=|u+s_0|-u=s_0\) for \(u\geq-s_0\), so \(c=s_0=m(a)\). Otherwise \(1\) and \(a\) are linearly independent over \(\mathbb R\), and \(\psi_0(s+ra)=s+rc\), for \(s,r\in\mathbb R\), defines a real-linear functional on their real span. We check that \(\psi_0(y)\leq\|y\|\) there. For \(r=0\) this reads \(s\leq|s|\). For \(r>0\), since \(c\leq g(s/r)\),
\[
\begin{gathered}
s+rc\\
\leq r\big(s/r+g(s/r)\big)\\
=r\,\|s/r+a\|\\
=\|s+ra\|.
\end{gathered}
\]
For \(r<0\) put \(q=-r>0\) and \(w=s/q\). For every real \(u\),
\[
\begin{gathered}
g(u)-\big(w-\|w-a\|\big)\\
=\|u+a\|+\|w-a\|-(u+w)\\
\geq\|(u+w)1\|-(u+w)\\
\geq0,
\end{gathered}
\]
so \(c\geq w-\|w-a\|\), and \(s+rc=q(w-c)\leq q\|w-a\|=\|s+ra\|\). By (H1), \(\psi_0\) extends to a real-linear \(\psi\) on \(A\) with \(\psi\leq\|\cdot\|\); applied to \(-x\), this gives \(|\psi(x)|\leq\|x\|\). By (H2), \(\omega(x)=\psi(x)-i\psi(ix)\) is complex-linear, \(\operatorname{Re}\omega=\psi\) and \(\|\omega\|\leq1\). Now \(\operatorname{Re}\omega(1)=\psi(1)=1\) and \(|\omega(1)|\leq1\), so \(\omega(1)=1\). Thus \(\omega\in V(A)\) and \(\operatorname{Re}\omega(a)=\psi(a)=c\), and \(m(a)=c\).

Finally, \((\|1+ta\|-1)/t=g(1/t)\) for \(t>0\). Since \(g\) is nonincreasing, its infimum over \(u>0\) equals its infimum over \(\mathbb R\) and its limit as \(u\to+\infty\), which is the limit of \(g(1/t)\) as \(t\to0^+\). This proves (2.2).

(2) \(\operatorname{Re}W(a)\) is the image of the compact convex set \(W(a)\) under the real-linear map \(\operatorname{Re}\), so it is a compact interval. Its maximum is \(m(a)\). Its minimum is \(-\max\operatorname{Re}(-W(a))=-m(-a)\), since \(W(-a)=-W(a)\).

(3) *The first limit.* For \(t\geq0\),
\[
\begin{gathered}
\Big|\,\|e^{ta}\|-\|1+ta\|\,\Big|\\
\leq\Big\|\sum_{n\geq2}\frac{t^na^n}{n!}\Big\|\\
\leq\sum_{n\geq2}\frac{(t\|a\|)^n}{n!}\\
\leq t^2\|a\|^2e^{t\|a\|}.
\end{gathered}
\]
Divide by \(t\) and use (2.2).

*The second limit.* Put \(h(t)=\|e^{ta}\|\). It is positive, because \(e^{ta}\) is invertible (B3), and \(h(t)\to\|1\|=1\) as \(t\to0\). The inequalities \(1-1/y\leq\log y\leq y-1\) for \(y>0\) give
\[
\frac{h(t)-1}{t\,h(t)}\leq\frac{\log h(t)}{t}\leq\frac{h(t)-1}{t},
\]
and both bounds tend to \(m(a)\) by the first limit.

*The supremum.* The function \(F(t)=\log h(t)\) has \(F(0)=0\) and \(F(t)\to0\) as \(t\to0^+\). It is subadditive, because \(e^{(s+t)a}=e^{sa}e^{ta}\) by (B3), so \(h(s+t)\leq h(s)h(t)\). And \(F(t)\leq t\|a\|\), since \(h(t)\leq e^{t\|a\|}\). By Lemma 2.2, \(\sup_{t>0}F(t)/t=\lim_{t\to0^+}F(t)/t=m(a)\). So \(F(t)\leq t\,m(a)\) for \(t>0\). If \(h(t)\leq e^{tw}\) for all \(t>0\), then \(F(t)/t\leq w\) for all \(t>0\), and \(m(a)\leq w\). \(\square\)

So \(m(a)\) is the right derivative at \(0\) of \(t\mapsto\|1+ta\|\), and also the exact exponential growth rate of \(\|e^{ta}\|\) for \(t\geq0\).

**Corollary 2.4** (dissipative elements). \(\operatorname{Re}W(a)\subseteq(-\infty,0]\) if and only if \(\|e^{ta}\|\leq1\) for all \(t\geq0\).

**Proof.** Both conditions say that \(m(a)\leq0\), by Theorem 2.3(3). \(\square\)

For bounded operators, the dissipativity condition is expressed directly by the numerical-range inequality proved here.

**Example 2.5** (a nilpotent matrix and two norms). Let \(N=\begin{pmatrix}0&1\\0&0\end{pmatrix}\in M_2(\mathbb C)\). Then \(N^2=0\), \(\sigma(N)=\{0\}\) and \(r(N)=0\). We compute \(W(N)\) for two algebra norms on \(M_2(\mathbb C)\) with \(\|1\|=1\), using Theorem 2.3(1) and Lemma 2.1. For \(z\in\mathbb C\), \(1+zN=\begin{pmatrix}1&z\\0&1\end{pmatrix}\).

(a) *The operator norm for the Euclidean norm on \(\mathbb C^2\).* Then \(M_2(\mathbb C)=B(\mathbb C^2)\) is a C\*-algebra, and by (C1), \(\|1+zN\|^2=\|(1+zN)^*(1+zN)\|\) is the largest eigenvalue of the self-adjoint matrix \(\begin{pmatrix}1&z\\\bar z&1+|z|^2\end{pmatrix}\). This matrix has trace \(2+|z|^2\) and determinant \(1\), so its eigenvalues are \(\big(2+|z|^2\pm|z|\sqrt{|z|^2+4}\big)/2\), and the larger one equals \(\big((|z|+\sqrt{|z|^2+4})/2\big)^2\). For \(t>0\) and real \(\theta\),
\[
\begin{gathered}
\frac{\|1+te^{i\theta}N\|-1}{t}\\
=\frac{t+\sqrt{t^2+4}-2}{2t}\\
=\frac12+\frac{t}{2\big(\sqrt{t^2+4}+2\big)}\longrightarrow\frac12 .
\end{gathered}
\]
So \(m(e^{i\theta}N)=1/2\) for every \(\theta\), and \(W(N)=\{|z|\leq1/2\}\).

(b) *The operator norm for the maximum norm on \(\mathbb C^2\)*, which is the largest row sum of absolute values. Here \(\|1+zN\|=1+|z|\), so \(m(e^{i\theta}N)=1\) for every \(\theta\), and \(W(N)=\{|z|\leq1\}\).

In both cases \(\|N\|=1\). In (a), \(r(N)=0<v(N)=\tfrac12<\|N\|\); in (b), \(v(N)=\|N\|\). So the numerical range depends on the norm, and not only on the algebra.

### 3. Hermitian elements

**Definition 3.1.** An element \(h\in A\) is *hermitian* if \(W(h)\subseteq\mathbb R\).

By Proposition 1.2(3), the hermitian elements form a real vector space that contains \(\mathbb R1\). It is closed, since \(\omega(h_n)\to\omega(h)\) for every \(\omega\in V(A)\) when \(h_n\to h\). By Corollary 1.4(2), a hermitian element has real spectrum.

**Theorem 3.2.** For \(h\in A\) the following are equivalent.
1. \(h\) is hermitian.
2. \(\|e^{ith}\|=1\) for every \(t\in\mathbb R\).
3. \(\|e^{ith}\|\leq1\) for every \(t\in\mathbb R\).
4. \(\|1+ith\|=1+o(t)\) as \(t\to0\) through real values; that is, \((\|1+ith\|-1)/t\to0\).

**Proof.** Since \(W(\pm ih)=\pm iW(h)\), we have \(m(ih)=-\min\operatorname{Im}W(h)\) and \(m(-ih)=\max\operatorname{Im}W(h)\). So \(h\) is hermitian exactly when \(m(ih)\leq0\) and \(m(-ih)\leq0\), and then both numbers are \(0\).

(1) ⇔ (3). By Theorem 2.3(3), \(m(ih)\leq0\) exactly when \(\|e^{tih}\|\leq1\) for all \(t\geq0\), and \(m(-ih)\leq0\) exactly when \(\|e^{-tih}\|\leq1\) for all \(t\geq0\).

(2) ⇔ (3). If (3) holds, then \(1=\|1\|=\|e^{ith}e^{-ith}\|\leq\|e^{ith}\|\,\|e^{-ith}\|\leq1\), so both norms equal \(1\).

(1) ⇔ (4). By Theorem 2.3(1), \(m(\pm ih)=\lim_{t\to0^+}(\|1\pm ith\|-1)/t\). If \(h\) is hermitian, both limits are \(0\), which is (4). Conversely, (4) gives \(m(ih)=m(-ih)=0\). \(\square\)

The proof of Sinclair's theorem below uses the power series of the arcsine. We derive the facts we need.

**Lemma 3.3** (the arcsine series). Let \(c_n=\binom{2n}{n}4^{-n}/(2n+1)\) for \(n\geq0\), and \(S(z)=\sum_{n\geq0}c_nz^{2n+1}\) for \(|z|<1\).
1. \(c_n>0\), the series converges for \(|z|<1\), and \(\sum_nc_n\leq\pi/2\).
2. Let \(0<c'<\pi/2\), choose \(\delta>0\) with \(\sin^2c'+\sinh^2\delta<1\), and let \(R=\{x+iy:\ |x|<c',\ |y|<\delta\}\). Then \(|\sin z|<1\) and \(S(\sin z)=z\) for every \(z\in R\).

**Proof.** Since \(\binom{2n}{n}\leq4^n\), \(0<c_n\leq1\), so the series converges for \(|z|<1\). Let \(P(w)=\sum_n\binom{2n}{n}w^n\) for real \(|w|<1/4\). From \((n+1)\binom{2n+2}{n+1}=2(2n+1)\binom{2n}{n}\) we get
\[
\begin{gathered}
P'(w)\\
=\sum_{n\geq0}(n+1)\binom{2n+2}{n+1}w^n\\
=4wP'(w)+2P(w),
\end{gathered}
\]
so \[
\begin{gathered}
\big((1-4w)^{1/2}P(w)\big)'\\
=(1-4w)^{-1/2}\big((1-4w)P'(w)-2P(w)\big)\\
=0.
\end{gathered}
\] As \(P(0)=1\), \(P(w)=(1-4w)^{-1/2}\). Differentiating \(S\) term by term, \[
\begin{gathered}
S'(y)\\
=\sum_n\binom{2n}{n}4^{-n}y^{2n}\\
=P(y^2/4)\\
=(1-y^2)^{-1/2}
\end{gathered}
\] for \(-1<y<1\). For \(|x|<\pi/2\), \(\cos x>0\), so
\[
\frac{d}{dx}S(\sin x)=\frac{\cos x}{\sqrt{1-\sin^2x}}=1,
\]
and \(S(\sin0)=0\). Hence \(S(\sin x)=x\) for \(|x|<\pi/2\).

For \(z=x+iy\in R\), \[
\begin{gathered}
|\sin z|^2\\
=\sin^2x+\sinh^2y<\sin^2c'+\sinh^2\delta<1.
\end{gathered}
\] So \(z\mapsto S(\sin z)-z\) is holomorphic on the connected open set \(R\) and vanishes on the real segment \((-c',c')\); by the identity theorem it vanishes on \(R\).

Finally, for \(0<x<\pi/2\) and every \(N\), \(\sum_{n\leq N}c_n\sin^{2n+1}x\leq S(\sin x)=x<\pi/2\). Letting \(x\) increase to \(\pi/2\) gives \(\sum_{n\leq N}c_n\leq\pi/2\) for every \(N\). \(\square\)

**Theorem 3.4** (Sinclair). If \(h\in A\) is hermitian, then \(\|h\|=r(h)\), and
\[
W(h)=[\min\sigma(h),\ \max\sigma(h)],
\]
the convex hull of \(\sigma(h)\).


**Proof.** *Step 1: if \(h\) is hermitian and \(r(h)<\pi/2\), then \(\|h\|\leq\pi/2\).* The spectrum of \(h\) is real, so \(\sigma(h)\subseteq[-r(h),r(h)]\). Choose \(c'\) with \(r(h)<c'<\pi/2\), and let \(\delta\) and the rectangle \(R\) be as in Lemma 3.3; then \(R\) is an open set containing \(\sigma(h)\). Let \(s=\sin h\) be the functional calculus of \(\sin\) at \(h\). Since \(\sin z=(e^{iz}-e^{-iz})/(2i)\), (B2) and (B3) give \(s=(e^{ih}-e^{-ih})/(2i)\), and Theorem 3.2 gives
\[
\|s\|\leq\tfrac12\big(\|e^{ih}\|+\|e^{-ih}\|\big)=1 .
\]
By spectral mapping (B2), \(\sigma(s)=\sin(\sigma(h))\subseteq\sin([-r(h),r(h)])\), which lies in \((-1,1)\); so \(r(s)<1\). By the power series rule in (B2), the functional calculus of \(S\) at \(s\) is \(S(s)=\sum_nc_ns^{2n+1}\), with convergence in norm. By the composition rule in (B2), \(S(s)=S(\sin h)=(S\circ\sin)(h)\). By Lemma 3.3, \(S\circ\sin\) is the identity function on the open set \(R\supseteq\sigma(h)\), so \((S\circ\sin)(h)=h\) by (B2). Therefore
\[
\begin{gathered}
\|h\|\\
=\Big\|\sum_nc_ns^{2n+1}\Big\|\\
\leq\sum_nc_n\|s\|^{2n+1}\\
\leq\sum_nc_n\\
\leq\frac\pi2 .
\end{gathered}
\]

*Step 2: \(\|h\|=r(h)\).* Let \(h\) be hermitian. For real \(t>0\) with \(t\,r(h)<\pi/2\), the element \(th\) is hermitian and \(r(th)=t\,r(h)\), so Step 1 gives \(t\|h\|\leq\pi/2\). If \(r(h)=0\), this holds for every \(t>0\), and \(h=0\). If \(r(h)>0\), let \(t\) increase to \(\pi/(2r(h))\); this gives \(\|h\|\leq r(h)\). The reverse inequality holds for every element (B1).

*Step 3: the numerical range.* The spectrum of \(h\) lies in \([-\|h\|,\|h\|]\). For \(u\geq\|h\|\), the element \(u+h\) is hermitian and \(\sigma(u+h)=u+\sigma(h)\subseteq[0,\infty)\), so by Step 2, \(\|u+h\|=r(u+h)=u+\max\sigma(h)\). Thus \(g(u)=\|u+h\|-u=\max\sigma(h)\) for \(u\geq\|h\|\), and Theorem 2.3(1) gives \(m(h)=\max\sigma(h)\). Since \(W(h)\) is real, \(\max W(h)=m(h)=\max\sigma(h)\). The same argument for the hermitian element \(-h\) gives \[
\begin{gathered}
\min W(h)\\
=-\max W(-h)\\
=-\max\sigma(-h)\\
=\min\sigma(h).
\end{gathered}
\] As \(W(h)\) is a compact convex subset of \(\mathbb R\), it is the interval between these two numbers. \(\square\)

The same renorming trick that makes an operator group isometric gives a version for bounded groups.

**Corollary 3.5** (bounded groups). Let \(a\in A\), and suppose \(M=\sup_{t\in\mathbb R}\|e^{ita}\|\) is finite. Then \(\|a\|\leq M\,r(a)\). The case \(M=1\) is the first statement of Theorem 3.4.

**Proof.** For \(x\in A\) put \(|x|=\sup_{t\in\mathbb R}\|e^{ita}x\|\). Then \(\|x\|\leq|x|\leq M\|x\|\) (take \(t=0\), and use \(\|e^{ita}x\|\leq\|e^{ita}\|\|x\|\)). So \(E=(A,|\cdot|)\) is a Banach space, and the algebra \(B(E)\) of bounded operators on \(E\), with the operator norm \(|\cdot|_{\mathrm{op}}\), is a unital Banach algebra whose identity has norm \(1\). For \(b\in A\) let \(L_b\) be left multiplication, \(L_bx=bx\). Then \(|L_bx|\leq M\|bx\|\leq M\|b\|\,|x|\), so \(|L_b|_{\mathrm{op}}\leq M\|b\|\), and \(b\mapsto L_b\) is a continuous unital homomorphism \(A\to B(E)\). Applying it to the exponential series gives \(e^{isL_a}=L_{e^{isa}}\). For \(x\in A\) and real \(s\), by (B3),
\[
\begin{gathered}
|e^{isL_a}x|\\
=|e^{isa}x|\\
=\sup_t\|e^{ita}e^{isa}x\|\\
=\sup_t\|e^{i(t+s)a}x\|\\
=|x| .
\end{gathered}
\]
So every \(e^{isL_a}\) is an isometry of \(E\), and \(|e^{isL_a}|_{\mathrm{op}}=1\). By Theorem 3.2, applied in \(B(E)\), \(L_a\) is hermitian there, and Theorem 3.4 gives \(|L_a|_{\mathrm{op}}=r_{B(E)}(L_a)\). By (B1),
\[
\begin{gathered}
r_{B(E)}(L_a)\\
=\lim_n|L_{a^n}|_{\mathrm{op}}^{1/n}\\
\leq\lim_n\big(M\|a^n\|\big)^{1/n}\\
=r(a).
\end{gathered}
\]
Finally \(\|a\|=\|a1\|\leq|L_a1|\leq|L_a|_{\mathrm{op}}\,|1|\leq r(a)\,M\), because \(|1|=\sup_t\|e^{ita}\|=M\). \(\square\)

**Corollary 3.6** (C\*-algebras). Let \(A\) be a unital C\*-algebra with \(1\neq0\).
1. The hermitian elements of \(A\) are exactly its self-adjoint elements.
2. The unital functionals are exactly the states. So \(W(a)=\{\varphi(a):\ \varphi\text{ a state}\}\).
3. For \(h=h^*\), \(W(h)=[\min\sigma(h),\max\sigma(h)]\), and \(v(h)=\|h\|\).

**Proof.** *Self-adjoint elements are hermitian.* Let \(h=h^*\) and \(t\in\mathbb R\). The involution is isometric and conjugate-linear, so applying it to the partial sums of the exponential series gives \((e^{ith})^*=e^{-ith}\). By (B3) and (C1), \(\|e^{ith}\|^2=\|e^{-ith}e^{ith}\|=\|1\|=1\). So \(h\) is hermitian by Theorem 3.2.

(3) follows from this and Theorem 3.4. Also \[
\begin{gathered}
v(h)\\
=\max(|\min\sigma(h)|,|\max\sigma(h)|)\\
=r(h)\\
=\|h\|
\end{gathered}
\] by (C1).

(1) It remains to show that a hermitian \(x\) is self-adjoint. Write \(x=h+ik\) with \(h=(x+x^*)/2\) and \(k=(x-x^*)/(2i)\), both self-adjoint. Then \(ik=x-h\) is hermitian, as a difference of hermitian elements. So \(W(ik)=iW(k)\) is contained in \(\mathbb R\cap i\mathbb R=\{0\}\), and \(W(k)=\{0\}\). By (3), \(\sigma(k)=\{0\}\), and \(\|k\|=r(k)=0\) by (C1). So \(x=h\).

(2) Let \(\omega\in V(A)\) and \(a\in A_+\). Then \(\omega(a)\in W(a)=[\min\sigma(a),\max\sigma(a)]\subseteq[0,\infty)\) by (3). So \(\omega\) is positive and of norm one: a state. Conversely, let \(\varphi\) be a state. For \(x,y\in A\) the form \(\langle x,y\rangle_\varphi=\varphi(y^*x)\) is sesquilinear, and \(\langle x,x\rangle_\varphi\geq0\) by (C2). The polarization and quadratic-minimization proof in [Proposition 3.2 of the GNS lesson](representations-and-positive-functionals-the-gns-construction-and-the-gelfand-naimark.md#oa-fnd-gn-03) shows that this form is hermitian and satisfies Cauchy–Schwarz, so
\[
\begin{gathered}
|\varphi(x)|^2\\
=|\langle x,1\rangle_\varphi|^2\\
\leq\varphi(x^*x)\,\varphi(1)\\
\leq\|x\|^2\varphi(1)^2,
\end{gathered}
\]
using \(\varphi(\|x\|^2-x^*x)\geq0\) from (C2). Hence \(1=\|\varphi\|\leq\varphi(1)\leq\|\varphi\|\,\|1\|=1\), so \(\varphi(1)=1\) and \(\varphi\in V(A)\). \(\square\)

In a Banach algebra with an isometric involution, self-adjoint elements need not be hermitian, even when their spectrum is real and their norm equals their spectral radius.

**Example 3.7** (group algebras). Let \(G\) be a discrete group with identity \(e\), and \(A=\ell^1(G)\) as in (B4). Write \(a\in A\) as \(a=a(e)\delta_e+b\) with \(b(e)=0\). Then
\[
W(a)=\{z\in\mathbb C :\ |z-a(e)|\leq\|b\|_1\}.
\]
Indeed, for \(z\in\mathbb C\), \(\delta_e\) and \(zb\) have disjoint supports, so \(\|\delta_e+zb\|_1=1+|z|\,\|b\|_1\). For \(t>0\) and real \(\theta\) this gives \((\|1+te^{i\theta}b\|-1)/t=\|b\|_1\). By Theorem 2.3(1), \(m(e^{i\theta}b)=\|b\|_1\) for all \(\theta\), and Lemma 2.1 gives \(W(b)=\{|z|\leq\|b\|_1\}\). Then \(W(a)=a(e)+W(b)\) by Proposition 1.2(3).

So the hermitian elements of \(\ell^1(G)\) are exactly the real multiples of \(\delta_e\). The self-adjoint elements, those with \(a(g^{-1})=\overline{a(g)}\), form a much larger set when \(G\neq\{e\}\). For \(G=\mathbb Z\) and \(a=\delta_1+\delta_{-1}\): \(a\) is self-adjoint, \(\sigma(a)=[-2,2]\) by (B4), and \(\|a\|_1=2=r(a)\); but \(W(a)\) is the closed disc of radius \(2\). Exercise 2 gives a self-adjoint element whose spectrum is not even real.

### 4. Positive matrices and the Perron–Frobenius eigenvalue

 The notation for vectors and matrices is fixed in the Conventions.

**Lemma 4.1.** Let \(T\in M_n(\mathbb C)\) and \(x,y,u\in\mathbb C^n\).
1. If \(T\geq0\), then \(|Tx|\leq T|x|\), and \(0\leq x\leq y\) implies \(0\leq Tx\leq Ty\).
2. If \(T\gg0\), \(x\geq0\) and \(x\neq0\), then \(Tx\gg0\).
3. If \(|x|\leq y\), then \(\|x\|\leq\|y\|\). If \(T\geq0\), then \(\|T\|=\|T\mathbf 1\|\).
4. If \(u\gg0\), \(x\geq0\) and \(x\neq0\), then \(u^{\top}x>0\).

**Proof.** (1) \(|(Tx)_i|=|\sum_jt_{ij}x_j|\leq\sum_jt_{ij}|x_j|\); the second claim is clear. (2) Each \((Tx)_i=\sum_jt_{ij}x_j\) has a positive term. (3) The first claim is clear; for \(T\geq0\), \((T\mathbf 1)_i=\sum_jt_{ij}\) is the \(i\)-th row sum. (4) \(u^{\top}x=\sum_iu_ix_i\) has a positive term and no negative one. \(\square\)

**Theorem 4.2** (the spectral radius is an eigenvalue). Let \(T\geq0\) and \(\rho=r(T)\). Then \(\rho\) is an eigenvalue of \(T\) with an eigenvector \(x\geq0\), \(x\neq0\).

**Proof.** For \(|\lambda|>\rho\) the series \(R(\lambda)=\sum_{k\geq0}T^k/\lambda^{k+1}\) converges absolutely, since \(\|T^k\|\leq(\rho+\varepsilon)^k\) for large \(k\) when \(\rho+\varepsilon<|\lambda|\) (B1). It is the inverse of \(\lambda-T\), because \[
\begin{gathered}
(\lambda-T)\sum_{k\leq K}T^k/\lambda^{k+1}\\
=1-T^{K+1}/\lambda^{K+1}\to1.
\end{gathered}
\] For real \(t>\rho\) every term is \(\geq0\), so \(R(t)\geq0\). By Lemma 4.1(1), \(|R(\lambda)x|\leq R(|\lambda|)|x|\) termwise, so \(\|R(\lambda)\|\leq\|R(|\lambda|)\|\) by Lemma 4.1(3).

Choose \(\mu\in\sigma(T)\) with \(|\mu|=\rho\), and \(\zeta\) with \(|\zeta|=1\) and \(\mu=\rho\zeta\). For \(t>\rho\), put \(\lambda=t\zeta\). Then \(|\lambda|=t\) and \(|\lambda-\mu|=t-\rho\), so by (B1)
\[
\|R(t)\|\geq\|R(\lambda)\|\geq\frac1{\operatorname{dist}(\lambda,\sigma(T))}\geq\frac1{t-\rho}.
\]
Since \(R(t)\geq0\), \(\|R(t)\|=\|R(t)\mathbf 1\|\) by Lemma 4.1(3). Put \(y_t=R(t)\mathbf 1\geq0\) and \(x_t=y_t/\|y_t\|\). Then \(x_t\geq0\), \(\|x_t\|=1\), and \((t-T)x_t=\mathbf 1/\|y_t\|\), whose norm is at most \(t-\rho\). Choose \(t_k\downarrow\rho\) such that \(x_{t_k}\) converges, to \(x\) say. Then \(x\geq0\), \(\|x\|=1\), and \((\rho-T)x=\lim_k(t_k-T)x_{t_k}=0\). \(\square\)

**Definition 4.3.** A matrix \(T\geq0\) is *primitive* if \(T^m\gg0\) for some \(m\geq1\). Every \(T\gg0\) is primitive. For a primitive \(T\), \(\rho=r(T)\) is the *Perron–Frobenius eigenvalue* of \(T\), and a vector \(v\gg0\) with \(Tv=\rho v\) is a *Perron–Frobenius eigenvector*. By the next theorem such \(v\) exists and is unique up to a positive factor.

**Theorem 4.4** (Perron–Frobenius, primitive matrices). Let \(T\geq0\) be primitive and \(\rho=r(T)\).
1. \(\rho>0\), and there is \(v\gg0\) with \(Tv=\rho v\).
2. Every \(y\in\mathbb C^n\) with \(Ty=\rho y\) is a multiple of \(v\).
3. Every eigenvalue \(\lambda\neq\rho\) of \(T\) has \(|\lambda|<\rho\).
4. There is \(u\gg0\) with \(u^{\top}T=\rho u^{\top}\). The space \(\mathbb C^n\) is the direct sum of \(\mathbb Cv\) and \(\ker u^{\top}\), both invariant under \(T\), and \(\rho\) is a simple root of the characteristic polynomial of \(T\).
5. If \(x\geq0\), \(x\neq0\), is an eigenvector of \(T\) for any eigenvalue, then \(x\) is a positive multiple of \(v\), and \(Tx=\rho x\).
6. (Max–min formula)
\[
\begin{gathered}
\rho\\
=\max_{x\geq0,\ x\neq0}\ \min_{i:\,x_i>0}\frac{(Tx)_i}{x_i}\\
=\min_{x\gg0}\ \max_i\frac{(Tx)_i}{x_i}.
\end{gathered}
\]
7. \((T/\rho)^k\to P=vu^{\top}/(u^{\top}v)\) as \(k\to\infty\), where \(P\) is the projection onto \(\mathbb Cv\) along \(\ker u^{\top}\). Consequently \(T^kw/\|T^kw\|\to v/\|v\|\) for every \(w\geq0\), \(w\neq0\).

The strict-positivity case and the max–min formula are both proved below.

**Proof.** *Step A: parts (1)–(3) when \(T\gg0\).*

(1) Theorem 4.2 gives \(x\geq0\), \(x\neq0\), with \(Tx=\rho x\). By Lemma 4.1(2), \(\rho x=Tx\gg0\). So \(\rho>0\) and \(x\gg0\); put \(v=x\).

(2) Since \(T\) and \(\rho\) are real, the real and imaginary parts of \(y\) satisfy the same equation; so we may assume \(y\) real and \(y\neq0\). Replacing \(y\) by \(-y\) if necessary, \(y\) has a positive entry. Let \(c=\min\{v_i/y_i:\ y_i>0\}>0\), attained at the index \(j\), and put \(z=v-cy\). Then \(z\geq0\): for \(y_i>0\) by the choice of \(c\), and for \(y_i\leq0\) because \(v_i>0\). Also \(z_j=0\) and \(Tz=\rho z\). If \(z\neq0\), then \(\rho z=Tz\gg0\) by Lemma 4.1(2), which contradicts \(z_j=0\). So \(z=0\) and \(y=v/c\).

(3) Let \(Tw=\lambda w\) with \(w\neq0\) and \(|\lambda|=\rho\). Then \(\rho|w|=|Tw|\leq T|w|\) by Lemma 4.1(1). Put \(d=T|w|-\rho|w|\geq0\), and suppose \(d\neq0\). Then \(Td\gg0\), that is, \(Tq\gg\rho q\) for \(q=T|w|\gg0\). Let \(\varepsilon=\min_i\big((Tq)_i-\rho q_i\big)/q_i>0\). Then \(Tq\geq(\rho+\varepsilon)q\), and by Lemma 4.1(1) and induction \(T^kq\geq(\rho+\varepsilon)^kq\) for all \(k\). By Lemma 4.1(3), \(\|T^k\|\,\|q\|\geq\|T^kq\|\geq(\rho+\varepsilon)^k\|q\|\), so \(\|T^k\|^{1/k}\geq\rho+\varepsilon\) for all \(k\), which contradicts \(\|T^k\|^{1/k}\to\rho\) (B1). Hence \(T|w|=\rho|w|=|Tw|\). For each \(i\), \(|\sum_jt_{ij}w_j|=\sum_jt_{ij}|w_j|\) with all \(t_{ij}>0\); by the case of equality in the triangle inequality, all nonzero \(w_j\) have the same argument, so \(w=e^{i\vartheta}|w|\) for some real \(\vartheta\). Then \(\lambda w=Tw=e^{i\vartheta}T|w|=e^{i\vartheta}\rho|w|=\rho w\), so \(\lambda=\rho\).

*Step B: parts (1)–(3) when \(T^m\gg0\).* Put \(T_1=T^m\). By (B1), \(r(T_1)=\rho^m\), and Step A applies to \(T_1\): \(\rho^m>0\), and there is \(v\gg0\) with \(T_1v=\rho^mv\) that spans the solutions of \(T_1y=\rho^my\). By Theorem 4.2 there is \(x\geq0\), \(x\neq0\), with \(Tx=\rho x\). Then \(T_1x=\rho^mx\), so \(x\) is a multiple of \(v\), and a positive one because \(x\geq0\). So \(Tv=\rho v\) and \(\rho>0\); this is (1). If \(Ty=\rho y\), then \(T_1y=\rho^my\) and \(y\in\mathbb Cv\); this is (2). If \(Tw=\lambda w\) with \(w\neq0\) and \(|\lambda|=\rho\), then \(T_1w=\lambda^mw\) with \(|\lambda^m|=\rho^m\). By Step A(3) for \(T_1\), \(\lambda^m=\rho^m\); then \(w\in\mathbb Cv\), and \(\lambda w=Tw=\rho w\) gives \(\lambda=\rho\). This is (3).

*Step C: parts (4)–(7).* The matrix \(T^{\top}\geq0\) is primitive, since \((T^{\top})^m=(T^m)^{\top}\gg0\), and it has the same characteristic polynomial as \(T\), hence \(r(T^{\top})=\rho\). Part (1) for \(T^{\top}\) gives \(u\gg0\) with \(T^{\top}u=\rho u\), that is, \(u^{\top}T=\rho u^{\top}\).

(4) Put \(K=\ker u^{\top}\), a subspace of dimension \(n-1\). Since \(u^{\top}v>0\) by Lemma 4.1(4), \(v\notin K\), and \(\mathbb C^n=\mathbb Cv\oplus K\). Both summands are invariant: \(Tv=\rho v\), and for \(x\in K\), \(u^{\top}Tx=\rho u^{\top}x=0\). If \(\rho\) were an eigenvalue of \(T|_K\), a corresponding eigenvector would lie in \(\mathbb Cv\cap K=\{0\}\) by (2), which is absurd. In a basis adapted to the decomposition, \(T\) is block diagonal, so \(\det(\lambda-T)=(\lambda-\rho)\det(\lambda-T|_K)\) with \(\det(\rho-T|_K)\neq0\). So \(\rho\) is a simple root.

(5) If \(Tx=\kappa x\) with \(x\geq0\), \(x\neq0\), then \(\rho u^{\top}x=u^{\top}Tx=\kappa u^{\top}x\), and \(u^{\top}x>0\) by Lemma 4.1(4). So \(\kappa=\rho\), and \(x\in\mathbb Cv\) by (2); as \(x\geq0\), it is a positive multiple of \(v\).

(6) For \(x\geq0\), \(x\neq0\), let \(\underline r(x)=\min_{i:\,x_i>0}(Tx)_i/x_i\). Then \(\underline r(x)\,x\leq Tx\), since the coordinates with \(x_i=0\) give \(0\leq(Tx)_i\). Applying \(u^{\top}\) gives \(\underline r(x)\,u^{\top}x\leq\rho u^{\top}x\), so \(\underline r(x)\leq\rho\), with equality at \(x=v\). For \(x\gg0\) let \(\overline r(x)=\max_i(Tx)_i/x_i\). Then \(Tx\leq\overline r(x)\,x\), so \(\rho u^{\top}x\leq\overline r(x)\,u^{\top}x\) and \(\rho\leq\overline r(x)\), with equality at \(x=v\).

(7) If \(K=\{0\}\), then \(P=1\) and \(T/\rho=1\), so the assertion is immediate. Otherwise every eigenvalue of \(T|_K\) is an eigenvalue of \(T\) other than \(\rho\), so it has modulus less than \(\rho\) by (3). Hence the spectral radius of \(T|_K/\rho\) is less than \(1\), and \((T|_K/\rho)^k\to0\) by (B1). Every \(x\in\mathbb C^n\) is \(Px+(x-Px)\) with \(Px=(u^{\top}x/u^{\top}v)\,v\) and \(x-Px\in K\), so \((T/\rho)^kx=Px+(T|_K/\rho)^k(x-Px)\to Px\). For \(w\geq0\), \(w\neq0\), we have \(u^{\top}w>0\), so \(T^kw/\rho^k\) tends to the nonzero vector \(Pw\), a positive multiple of \(v\); normalizing gives the last claim. \(\square\)

A matrix \(T\geq0\) is *irreducible* if for all \(i\neq j\) some power \(T^k\), \(k\geq1\), has \((T^k)_{ij}>0\); for \(n=1\) every matrix counts as irreducible. Primitive matrices are irreducible, but not conversely.

**Proposition 4.5** (irreducible matrices). Let \(T\geq0\) be irreducible and \(\rho=r(T)\).
1. \(1+T\) is primitive, and \(r(1+T)=1+\rho\).
2. There is \(v\gg0\) with \(Tv=\rho v\). Parts (2), (4), (5) and (6) of Theorem 4.4 hold for \(T\), and \(\rho>0\) when \(n\geq2\).
3. Parts (3) and (7) of Theorem 4.4 can fail: for \(T=\begin{pmatrix}0&1\\1&0\end{pmatrix}\), which is irreducible, \(\rho=1\), \(-1\) is an eigenvalue, and \(T^k\) alternates between \(1\) and \(T\).


**Proof.** (1) Let \(n\geq2\) and \(i\neq j\), and choose \(k\) with \((T^k)_{ij}>0\). Expanding the matrix product, \((T^k)_{ij}\) is a sum of products \(t_{i_0i_1}t_{i_1i_2}\cdots t_{i_{k-1}i_k}\) over chains with \(i_0=i\) and \(i_k=j\), all terms \(\geq0\); so some chain has all its factors positive. Removing the loops of this chain gives a chain from \(i\) to \(j\) with distinct indices, hence of length \(l\leq n-1\), and \((T^l)_{ij}>0\). Now \((1+T)^{n-1}=\sum_{l=0}^{n-1}\binom{n-1}{l}T^l\) has all entries positive: the off-diagonal ones by what we just showed, the diagonal ones because of the term \(l=0\). For \(n=1\), \(1+T\gg0\) directly. By (B1), \(\sigma(1+T)=1+\sigma(T)\), and \(|1+\lambda|\leq1+|\lambda|\leq1+\rho\) for \(\lambda\in\sigma(T)\), with equality at \(\lambda=\rho\in\sigma(T)\) (Theorem 4.2). So \(r(1+T)=1+\rho\).

(2) Theorem 4.4 applies to \(1+T\). The equations \((1+T)y=(1+\rho)y\) and \(Ty=\rho y\) are the same; \(\det\big(\lambda-(1+T)\big)=\det\big((\lambda-1)-T\big)\), so multiplicities of roots correspond; \(1+T\) and \(T\) have the same eigenvectors; and \(\big((1+T)x\big)_i/x_i=1+(Tx)_i/x_i\). This transfers (1), (2), (4), (5) and (6). If \(n\geq2\) and \(\rho=0\), then \(Tv=0\) with \(v\gg0\) forces \(T=0\), which is not irreducible.

(3) The eigenvalues of this \(T\) are \(\pm1\), and \(T^2=1\). \(\square\)

**Example 4.6** (the hypotheses matter). For the \(2\times2\) identity matrix, \(\rho=1\) has a two-dimensional eigenspace, and \((1,0)\) is a nonnegative eigenvector that is not \(\gg0\). For \(\begin{pmatrix}1&1\\0&1\end{pmatrix}\), \(\rho=1\) is a double root, and the only eigenvectors are the multiples of \((1,0)\). For \(\begin{pmatrix}0&1\\0&0\end{pmatrix}\), \(\rho=0\). None of these three matrices is irreducible. On the other hand, \(T=\begin{pmatrix}1&2\\3&4\end{pmatrix}\gg0\) has eigenvalues \((5\pm\sqrt{33})/2\); here \(\rho=(5+\sqrt{33})/2\), the other eigenvalue has modulus less than \(1\), and \(v=(2,\rho-1)\gg0\) is a Perron–Frobenius eigenvector, since its first coordinate gives \(2+2(\rho-1)=2\rho\) and its second \(6+4(\rho-1)=\rho(\rho-1)\), which is the equation \(\rho^2=5\rho+2\).

## B. Code obstructions and construct Borel choices

Begin here after the Borel-model lesson if the problem is measurable selection. The background proofs establish the order-type and boundedness tools before they are used in tree coding. The representation of co-Souslin sets by well-orders leads to reduction and separation; these in turn yield the countable-to-one and closed-set selector theorems. Each implication is proved below, including the auxiliary ordinal statements.

### Background proofs for the selection route

*From [Polish spaces and standard Borel spaces](polish-spaces-and-standard-borel-spaces.md) and The Effros Borel structure.* Let \(X\) and \(Y\) be standard Borel spaces.

- **(D1)** Borel sets are Souslin sets. Countable unions and countable intersections of Souslin sets are Souslin sets. If \(A\subseteq X\) and \(B\subseteq Y\) are Souslin, so is \(A\times B\subseteq X\times Y\). If \(f:X\to Y\) is Borel, then \(f(A)\) is Souslin for every Souslin \(A\subseteq X\), and \(f^{-1}(B)\) is Souslin for every Souslin \(B\subseteq Y\). See [closure properties](polish-spaces-and-standard-borel-spaces.md#oa-fnd-pb-02), [Borel sets and Souslin sets](polish-spaces-and-standard-borel-spaces.md#oa-fnd-pb-12) and [Borel maps between Souslin spaces](polish-spaces-and-standard-borel-spaces.md#oa-fnd-pb-06).
- **(D2)** (Souslin’s theorem) A Souslin set whose complement is a Souslin set is Borel ([the separation theorem](polish-spaces-and-standard-borel-spaces.md#oa-fnd-pb-03)).
- **(D3)** A nonempty Souslin subset of a Polish space \(Z\) has the form \(g(\Lambda)\) for a continuous \(g:\Lambda\to Z\) ([closure properties](polish-spaces-and-standard-borel-spaces.md#oa-fnd-pb-02)).
- **(D4)** There is a Souslin set \(U\subseteq\mathcal C\times\mathcal C\) such that every Souslin subset of \(\mathcal C\) equals \(U_y=\{x:(y,x)\in U\}\) for some \(y\in\mathcal C\); and there is a Souslin set \(D\subseteq\mathcal C\) that is not Borel, so that \(\mathcal C\setminus D\) is not a Souslin set ([a Souslin set that is not Borel](polish-spaces-and-standard-borel-spaces.md#oa-fnd-pb-12)).
- **(D5)** (Change of topology) If \((X,\tau)\) is Polish and \(B_1,B_2,\ldots\) are Borel, there is a Polish topology \(\tau'\supseteq\tau\) with the same Borel sets in which every \(B_n\) is open and closed ([zero-dimensional refinement](polish-spaces-and-standard-borel-spaces.md#oa-fnd-pb-04)). Borel subsets of standard Borel spaces, with the relative Borel structure, are again standard (Borel subsets of standard spaces). Open subsets of Polish spaces are Polish (Polish subspaces).
- **(D6)** Every Borel subset of a Polish space is the image of a closed subset of \(\Lambda\) under a continuous bijection ([closed subsets of the Baire space](polish-spaces-and-standard-borel-spaces.md#oa-fnd-pb-04) and [Lusin sets](polish-spaces-and-standard-borel-spaces.md#oa-fnd-pb-05)).
- **(D7)** If a Borel map on a standard Borel space is injective and takes values in a separable metrizable space, then its image is Borel and the map is a Borel isomorphism onto the image. The graph of a Borel map \(f:X\to Y\) is a Borel subset of \(X\times Y\) ([Borel maps between Souslin spaces](polish-spaces-and-standard-borel-spaces.md#oa-fnd-pb-06)).
- **(D8)** For a Polish space \(X\), the *Effros Borel structure* on the set \(\mathcal C_0(X)\) of nonempty closed subsets is the \(\sigma\)-algebra generated by the sets \(\{F:F\cap U\neq\varnothing\}\), \(U\subseteq X\) open. It is standard (spaces of closed sets).
- **(D9)** (Cantor's intersection theorem) In a complete metric space, a decreasing sequence of nonempty closed sets with diameters tending to \(0\) has exactly one common point ([Polish spaces and standard Borel spaces](polish-spaces-and-standard-borel-spaces.md), elementary fact B1).

*Well-orders.*

- **(S1)** If \((W,<)\) is well-ordered and \(f:W\to W\) is strictly increasing, then \(f(w)\geq w\) for all \(w\) (Theorem 0.1 below). So no well-ordered set is isomorphic to a proper initial segment \(\{w:w<q\}\) of itself (Theorem 0.1).
- **(S2)** Every well-ordered set is isomorphic to exactly one ordinal, its *order type*. Ordinals are linearly ordered, every nonempty set of ordinals has a least element, and each ordinal is the set of smaller ordinals, so that \(\alpha<\beta\) makes \(\alpha\) a proper initial segment of \(\beta\) (Theorem 0.1). For two well-ordered sets, exactly one of the following holds: they are isomorphic, the first is isomorphic to a proper initial segment of the second, or the second is isomorphic to a proper initial segment of the first (Theorem 0.1).

We use elementary finite-dimensional linear algebra over \(\mathbb C\). The remaining topological and scalar facts are justified immediately below. The background statements are proved below.

#### Well-orders and their order types

The following proof supplies (S1)–(S2). We use the usual axioms of set theory, including Separation and Replacement, to form subsets and images of sets; no collection of all ordinals is treated as a set. An *initial segment* of a well-order is a downward closed subset, possibly the whole order. A proper initial segment is exactly the set of predecessors of its least omitted point.

**Theorem 0.1** (Well-orders and ordinals). If a strictly increasing map \(f:W\to W\) acts on a well-ordered set, then \(f(w)\geq w\) for every \(w\). No well-order is isomorphic to a proper initial segment of itself. Every well-order is isomorphic to exactly one ordinal. Ordinals are linearly ordered by membership; every nonempty set of ordinals has a least member, and an ordinal is exactly the set of its predecessors. Consequently two well-orders are either isomorphic or exactly one is isomorphic to a proper initial segment of the other. A countable well-order has a countable ordinal as its order type.

*Proof.* **Induction and increasing maps.** A property holds throughout a well-order if, whenever it holds at all predecessors of a point, it holds at that point: a nonempty set of failures would have a least member. If \(w\) is the least point with \(f(w)<w\), put \(v=f(w)\). Then \(v<w\), so \(f(v)\geq v=f(w)\), whereas strict increase gives \(f(v)<f(w)\), a contradiction. Thus \(f(w)\geq w\). An isomorphism of \(W\) onto the predecessors of \(q\in W\) would give \(f(q)<q\), which is impossible.

**Comparison of well-orders.** Consider all order isomorphisms between initial segments of two well-orders \(W,V\). Any two agree on their common domain. Otherwise take the first point where they disagree. Their values at all preceding points agree, and each value at the new point must be the least element of \(V\) outside that common predecessor image. The values therefore agree, a contradiction. These maps are subsets of the set \(W\times V\). Their union is an order isomorphism between initial segments: domains are nested initial segments, compatibility makes the union a function, and the ranges are initial segments too. If both domain and range were proper, map the least unused point of \(W\) to the least unused point of \(V\). This would give another initial-segment isomorphism strictly extending the union, a contradiction. Thus one order is exhausted. The alternatives cannot overlap, since composing competing comparisons would make a well-order isomorphic to a proper initial segment of itself.

**Ordinals.** A set \(\alpha\) is an ordinal if it is transitive (\(x\in\alpha\) implies \(x\subseteq\alpha\)) and membership is a strict well-order on \(\alpha\). If \(x\in\alpha\), its predecessors in \(\alpha\) are precisely the members of \(x\): transitivity of \(\alpha\) puts those members in \(\alpha\). Also \(x\) is transitive, because \(z\in y\in x\), with all three in \(\alpha\), implies \(z\in x\) by transitivity of the membership order. Thus \(x\) is itself an ordinal. In particular the proper initial segments of an ordinal are its members. No ordinal belongs to itself: if \(\alpha\in\alpha\), membership restricted to \(\alpha\) would have the forbidden loop \(\alpha\in\alpha\).

An isomorphism between initial segments of ordinals is the identity on its domain. Induct on \(x\) in that domain. The predecessors of its image are the images of the predecessors of \(x\), so
\[
f(x)=\{f(y):y\in x\}=\{y:y\in x\}=x.
\]
The preceding comparison theorem now implies that for any two ordinals \(\alpha,\beta\), exactly one of \(\alpha=\beta\), \(\alpha\in\beta\), \(\beta\in\alpha\) holds. Moreover \(\beta+1:=\beta\cup\{\beta\}\) is an ordinal: it is transitive, its old elements retain their membership order, and \(\beta\) is the new last element. Given a nonempty set \(S\) of ordinals, choose \(\beta\in S\). The nonempty subset \(S\cap(\beta+1)\) has a least member \(\gamma\) in this well-order. Every member of \(S\) outside \(\beta+1\) is larger than \(\beta\), so \(\gamma\) is least in all of \(S\). Since all members of an ordinal are smaller ordinals and comparison identifies every smaller ordinal with a proper initial segment, an ordinal is exactly the set of smaller ordinals.

**Constructing the order type.** We justify the recursion
\[
F(w)=\{F(u):u<w\}
\]
on a well-order \(W\). Call a function on an initial segment *compatible* if it satisfies this formula at every point of its domain. Two compatible functions agree on the intersection of their domains: the first disagreement would have exactly the same predecessor values on both sides. By Separation form the initial segment \(D\subseteq W\) consisting of points contained in some compatible domain. At each point of \(D\) its compatible value exists and is unique. Replacement therefore supplies the function \(F_D\) with those values. It obeys the recursion, because any compatible domain containing a point contains all its predecessors. If \(D\ne W\), let \(w\) be its least omitted point. Then \(D=\{u:u<w\}\), and extending \(F_D\) by the value \(\{F_D(u):u<w\}\) at \(w\) gives a compatible function containing \(w\), a contradiction. Hence \(D=W\), and the recursion defines a unique function on all of \(W\).

Inductively \(F(w)\) is an ordinal and \(u\mapsto F(u)\), for \(u<w\), is an isomorphism onto \(F(w)\). Indeed, predecessor values are ordinals, and \(u<v<w\) implies \(F(u)\in F(v)\) by the recursion. They are distinct, since an ordinal cannot belong to itself. A membership in the reverse direction would give \(F(v)\in F(u)\in F(v)\), and transitivity of the ordinal \(F(v)\) would force \(F(v)\in F(v)\), a contradiction. Thus membership agrees exactly with the predecessor order. The set of predecessor values is transitive, since every member of \(F(u)\) is an earlier value, and it is well-ordered by pulling nonempty subsets back to the predecessor order. This proves the induction assertion. The same argument applied to all values shows that
\[
\alpha=\{F(w):w\in W\}
\]
is an ordinal and \(F:W\to\alpha\) is an order isomorphism. Two ordinals isomorphic to \(W\) are isomorphic to each other; the identity result above forces equality. Finally this isomorphism is a bijection, so if \(W\) is countable, so is \(\alpha\). \(\square\)

### 5. Souslin and co-Souslin sets

From now on \(X\) and \(Y\) are standard Borel spaces, unless something else is said.

**Definition 5.1.** A subset of \(X\) is *co-Souslin* if its complement is a Souslin set.

When a Polish topology generating the Borel sets is fixed, the Souslin sets are the analytic sets, and the co-Souslin sets are the sets denoted by \(\Pi^1_1\).

**Proposition 5.2.**
1. Borel sets are both Souslin and co-Souslin. A set that is both Souslin and co-Souslin is Borel.
2. Countable unions and countable intersections of co-Souslin sets are co-Souslin.
3. If \(f:X\to Y\) is Borel and \(C\subseteq Y\) is co-Souslin, then \(f^{-1}(C)\) is co-Souslin.
4. If \(S\subseteq X\times Y\) is Souslin, its projection \(\{x:(x,y)\in S\text{ for some }y\}\) is Souslin. If \(C\subseteq X\times Y\) is co-Souslin, then \(\{x:(x,y)\in C\text{ for all }y\}\) is co-Souslin.
5. Some co-Souslin set in \(\mathcal C\) is not a Souslin set, namely \(\mathcal C\setminus D\) for the set \(D\) of (D4).

**Proof.** (1) is (D1) and (D2). (2) and (3) follow from (D1) by taking complements: the complement of a countable intersection is a countable union, and \(X\setminus f^{-1}(C)=f^{-1}(Y\setminus C)\). (4) Fix Polish topologies generating the Borel sets. The projection is continuous, hence Borel, and (D1) applies. The second set is the complement of the projection of the Souslin set \((X\times Y)\setminus C\). (5) is (D4). \(\square\)

### 6. Trees on a countable set

In Sections 6 and 7, \(Q\) and \(P\) are countable nonempty sets with the discrete topology. \(Q^{<\mathbb N}\) consists of the finite sequences \(s=(s_1,\dots,s_k)\) with entries in \(Q\), including the empty sequence \(\varnothing\); \(|s|=k\) is the length, and \(s{}^\frown a=(s_1,\dots,s_k,a)\). We write \(s\sqsubseteq t\) if \(s\) is an initial segment of \(t\), that is, \(|s|\leq|t|\) and \(t_i=s_i\) for \(i\leq|s|\), and \(s\sqsubset t\) if moreover \(s\neq t\). For \(x\in Q^{\mathbb N}\) and \(k\geq0\), \(x|k=(x_1,\dots,x_k)\). The space \(Q^{\mathbb N}\) has the product topology. It is Polish, and the cylinders \(O_s=\{x\in Q^{\mathbb N}:\ x|\,|s|=s\}\) are open and closed and form a base; for each \(x\), the cylinders \(O_{x|k}\), \(k\geq0\), form a neighbourhood base at \(x\). For \(Q=\mathbb N\) this is the Baire space \(\Lambda\), and \(O_s=\Lambda_s\).

Subsets of \(Q^{<\mathbb N}\) are points of the Polish space \(2^{Q^{<\mathbb N}}\) (Conventions). The next lemma shows that this Borel structure is the Effros structure (D8), so no choice is involved.

**Lemma 6.1.** Let \(Z\) be a countable set with the discrete topology. On the set of nonempty subsets of \(Z\), which are the nonempty closed subsets, the Effros Borel structure equals the Borel structure of \(2^Z\setminus\{\varnothing\}\).

**Proof.** Every subset of \(Z\) is open. The Effros structure is generated by the sets \(\{S:S\cap U\neq\varnothing\}=\bigcup_{z\in U}\{S:z\in S\}\), and conversely \(\{S:z\in S\}=\{S:S\cap\{z\}\neq\varnothing\}\). So both \(\sigma\)-algebras are generated by the sets \(\{S:z\in S\}\), \(z\in Z\). \(\square\)

**Definition 6.2.** A *tree* on \(Q\) is a set \(T\subseteq Q^{<\mathbb N}\) such that \(s\in T\) whenever \(s\sqsubseteq t\in T\). Its *body* is
\[
[T]=\{x\in Q^{\mathbb N}:\ x|k\in T\text{ for all }k\geq0\}.
\]
The tree \(T\) is *well-founded* if \([T]=\varnothing\) and *ill-founded* otherwise, and *pruned* if every \(s\in T\) has an extension \(s{}^\frown a\in T\). We write \(\mathrm{Tree}(Q)\) and \(\mathrm{WF}(Q)\) for the sets of trees and of well-founded trees on \(Q\), and \(\mathrm{PT}(Q)\) for the set of nonempty pruned trees.

A tree is well-founded exactly when it contains no infinite chain \(s^1\sqsubset s^2\sqsubset\cdots\). Indeed, the lengths along such a chain tend to infinity, and there is a unique \(x\in Q^{\mathbb N}\) with \(x|\,|s^k|=s^k\) for all \(k\). Each \(x|j\) is an initial segment of some \(s^k\), so it lies in \(T\), and \(x\in[T]\). Conversely, \(x\in[T]\) gives the chain \(x|1\sqsubset x|2\sqsubset\cdots\). The empty set is a well-founded tree, and every nonempty tree contains \(\varnothing\).

**Proposition 6.3.**
1. \(\mathrm{Tree}(Q)\) is closed in \(2^{Q^{<\mathbb N}}\), and \([T]\) is closed in \(Q^{\mathbb N}\) for every tree \(T\).
2. For a closed set \(F\subseteq Q^{\mathbb N}\), the set \(T_F=\{x|k:\ x\in F,\ k\geq0\}\) is a pruned tree with \([T_F]=F\). The map \(F\mapsto T_F\) is a Borel isomorphism of the Effros space \(\mathcal C_0(Q^{\mathbb N})\) onto \(\mathrm{PT}(Q)\), which is a \(G_\delta\) subset of \(2^{Q^{<\mathbb N}}\). The inverse map is \(T\mapsto[T]\).
3. The set \(\mathrm{WF}(Q)\) is co-Souslin in \(2^{Q^{<\mathbb N}}\).

**Proof.** (1) A set \(T\) is a tree when, for every pair \(s\sqsubseteq t\), either \(t\notin T\) or \(s\in T\). For one pair this condition defines an open and closed set, and there are countably many pairs. If \(x\notin[T]\), then \(x|k\notin T\) for some \(k\), and the whole open set \(O_{x|k}\) misses \([T]\).

(2) The initial segments of \(x|k\) are the \(x|j\), \(j\leq k\), so \(T_F\) is a tree; it is pruned, since \(x|k\sqsubset x|(k+1)\). Clearly \(F\subseteq[T_F]\). If \(y\in[T_F]\), then for each \(k\) some \(x^k\in F\) has \(x^k|k=y|k\); so \(x^k\to y\), and \(y\in F\) because \(F\) is closed.

For \(s\in Q^{<\mathbb N}\), \(\{F:s\in T_F\}=\{F:F\cap O_s\neq\varnothing\}\), a generator of the Effros structure (D8). The coordinate maps generate the Borel sets of \(2^{Q^{<\mathbb N}}\), so \(F\mapsto T_F\) is Borel. It is injective because \(F=[T_F]\), and its values are nonempty pruned trees. Conversely, let \(T\in\mathrm{PT}(Q)\) and \(s\in T\). Fix an enumeration of \(Q\), and extend \(s\) one step at a time, each time by the first \(a\) in the enumeration that keeps the sequence in \(T\). This defines \(x\in[T]\) with \(x|\,|s|=s\). So \([T]\) is nonempty and closed, and \(T=T_{[T]}\): every \(s\in T\) is an initial segment of a point of \([T]\), and \(T_{[T]}\subseteq T\) by the definition of \([T]\). So \(F\mapsto T_F\) maps onto \(\mathrm{PT}(Q)\), with inverse \(T\mapsto[T]\). The inverse is Borel: an open set \(U\subseteq Q^{\mathbb N}\) is a countable union of cylinders \(O_s\), and for \(T\in\mathrm{PT}(Q)\), \([T]\cap O_s\neq\varnothing\) exactly when \(s\in T\); so \(\{T:[T]\cap U\neq\varnothing\}\) is a countable union of Borel sets. Finally,
\[
\begin{gathered}
\mathrm{PT}(Q)\\
=\mathrm{Tree}(Q)\cap\{T :\varnothing\in T\}\\
\cap\bigcap_{s\in Q^{<\mathbb N}}\Big(\{T:s\notin T\}\\
\cup\bigcup_{a\in Q}\{T:s{}^\frown a\in T\}\Big),
\end{gathered}
\]
the intersection of a closed set with countably many open sets.

(3) The set \(\{(T,x)\in2^{Q^{<\mathbb N}}\times Q^{\mathbb N}:\ x|k\in T\text{ for all }k\}\) is closed, because each condition \(x|k\in T\) involves one coordinate of \(T\) and finitely many coordinates of \(x\). Its projection to \(2^{Q^{<\mathbb N}}\) is the set of subsets \(T\) with a branch, which is Souslin by Proposition 5.2(4). The complement of this projection is co-Souslin, and its intersection with the closed set \(\mathrm{Tree}(Q)\) is \(\mathrm{WF}(Q)\). \(\square\)

We now order finite sequences of natural numbers so that well-founded trees become well-ordered.

**Definition 6.4** (the Kleene–Brouwer order). For distinct \(s,t\in\mathbb N^{<\mathbb N}\), put \(s<_{\mathrm{KB}}t\) if either \(t\sqsubset s\), or there is an index \(i\leq\min(|s|,|t|)\) with \(s_j=t_j\) for \(j<i\) and \(s_i<t_i\). Write \(s\leq_{\mathrm{KB}}t\) if \(s<_{\mathrm{KB}}t\) or \(s=t\).

So a proper extension of \(t\) comes before \(t\), and sequences that branch apart are compared at the first place where they differ.

**Lemma 6.5.** \(<_{\mathrm{KB}}\) is a strict linear order on \(\mathbb N^{<\mathbb N}\). The empty sequence is its largest element, and \(s{}^\frown a<_{\mathrm{KB}}s\) for all \(s\) and \(a\).

**Proof.** Two distinct sequences are comparable: either one is a proper initial segment of the other, or they first differ at some index \(i\leq\min(|s|,|t|)\). The two alternatives of the definition exclude each other and cannot hold in both directions, so \(<_{\mathrm{KB}}\) is asymmetric. For transitivity let \(s<_{\mathrm{KB}}t<_{\mathrm{KB}}u\). There are four cases.
- If \(t\sqsubset s\) and \(u\sqsubset t\), then \(u\sqsubset s\), so \(s<_{\mathrm{KB}}u\).
- If \(t\sqsubset s\), and \(t,u\) first differ at \(i\) with \(t_i<u_i\), then \(i\leq|t|\), so \(s\) agrees with \(t\) up to \(i\), and \(s,u\) first differ at \(i\) with \(s_i=t_i<u_i\).
- If \(s,t\) first differ at \(i\) with \(s_i<t_i\), and \(u\sqsubset t\): when \(|u|\geq i\), \(s\) and \(u\) first differ at \(i\) with \(s_i<t_i=u_i\); when \(|u|<i\), \(u\) is a proper initial segment of \(s\), because \(s_j=t_j=u_j\) for \(j\leq|u|\) and \(|s|\geq i>|u|\).
- If \(s,t\) first differ at \(i\) with \(s_i<t_i\), and \(t,u\) first differ at \(i'\) with \(t_{i'}<u_{i'}\), let \(j=\min(i,i')\). Then \(s\) and \(u\) agree before \(j\), and \(s_j<u_j\): if \(i<i'\), \(s_i<t_i=u_i\); if \(i'<i\), \(s_{i'}=t_{i'}<u_{i'}\); if \(i=i'\), \(s_i<t_i<u_i\).

In each case \(s<_{\mathrm{KB}}u\). Every nonempty sequence properly extends \(\varnothing\), so \(\varnothing\) is the largest element. The last claim holds because \(s\sqsubset s{}^\frown a\). \(\square\)

**Theorem 6.6.** A tree \(T\) on \(\mathbb N\) is well-founded if and only if \(<_{\mathrm{KB}}\) restricted to \(T\) is a well-order.

**Proof.** If \(x\in[T]\), then \(x|0>_{\mathrm{KB}}x|1>_{\mathrm{KB}}x|2>_{\mathrm{KB}}\cdots\) by Lemma 6.5, an infinite strictly decreasing sequence in \(T\); so \(<_{\mathrm{KB}}\) is not a well-order on \(T\).

If a linear order on the countable set of nodes were not a well-order, a nonempty subset without a least node would give an infinite decreasing sequence: fix an enumeration, start with one node of the subset, and repeatedly take the first smaller node in that enumeration. Thus absence of decreasing sequences suffices. Conversely, let \(T\) be well-founded, and suppose \(s^0>_{\mathrm{KB}}s^1>_{\mathrm{KB}}s^2>_{\mathrm{KB}}\cdots\) in \(T\). We build \(x\in[T]\), which is a contradiction. We show by induction on \(m\geq0\) that there are \(x_1,\dots,x_m\in\mathbb N\) and an index \(k_m\) such that \(s^k\) extends \(x|m=(x_1,\dots,x_m)\) for all \(k\geq k_m\). For \(m=0\) take \(k_0=0\). Given \(m\), put \(w=x|m\). The terms of the sequence are distinct, so at most one \(k\geq k_m\) has \(s^k=w\); hence there is \(k'_m\geq k_m\) such that \(s^k\) properly extends \(w\) for all \(k\geq k'_m\), and the entry \(s^k_{m+1}\) is defined. For \(k\geq k'_m\), \(s^{k+1}<_{\mathrm{KB}}s^k\) and both properly extend \(w\). Either \(s^{k+1}\) extends \(s^k\), and then \(s^{k+1}_{m+1}=s^k_{m+1}\); or they first differ at an index \(i>m\) with \(s^{k+1}_i<s^k_i\), and then \(s^{k+1}_{m+1}\leq s^k_{m+1}\). So the entries \(s^k_{m+1}\), \(k\geq k'_m\), form a nonincreasing sequence in \(\mathbb N\), which is eventually constant, say equal to \(x_{m+1}\) for \(k\geq k_{m+1}\). This completes the induction. Each \(x|m\) is an initial segment of some \(s^k\in T\), so \(x|m\in T\) for all \(m\), and \(x\in[T]\). \(\square\)

For example, the whole set \(\mathbb N^{<\mathbb N}\) is an ill-founded tree, and \((1)>_{\mathrm{KB}}(1,1)>_{\mathrm{KB}}(1,1,1)>_{\mathrm{KB}}\cdots\). The well-founded tree \(\{\varnothing,(1),(2),(3),\dots\}\) is ordered as \((1)<_{\mathrm{KB}}(2)<_{\mathrm{KB}}(3)<_{\mathrm{KB}}\cdots<_{\mathrm{KB}}\varnothing\), a well-order of type \(\omega+1\).

Finally we look at trees on a product. A sequence \((q_1,p_1),\dots,(q_k,p_k)\) in \(Q\times P\) is the same as a pair \((s,t)\in Q^{<\mathbb N}\times P^{<\mathbb N}\) with \(|s|=|t|\), and \((Q\times P)^{\mathbb N}\) is homeomorphic to \(Q^{\mathbb N}\times P^{\mathbb N}\). So a tree on \(Q\times P\) is a set \(T\) of such pairs, closed under taking initial segments of both entries at once, and \([T]\subseteq Q^{\mathbb N}\times P^{\mathbb N}\). For \(x\in Q^{\mathbb N}\), the *section* of \(T\) at \(x\) is
\[
T(x)=\{t\in P^{<\mathbb N}:\ (x|\,|t|,\,t)\in T\},
\]
a tree on \(P\).

**Lemma 6.7** (sections). Let \(T\) be a tree on \(Q\times P\).
1. \([T(x)]=\{y\in P^{\mathbb N}:(x,y)\in[T]\}\) for every \(x\in Q^{\mathbb N}\).
2. The map \((T,x)\mapsto T(x)\), from \(\mathrm{Tree}(Q\times P)\times Q^{\mathbb N}\) to \(\mathrm{Tree}(P)\), is continuous.
3. Let \(C\subseteq Q^{\mathbb N}\times P^{\mathbb N}\) be closed and \(T_C\) its tree (Proposition 6.3(2)). Then \(x\mapsto T_C(x)\) is continuous, and \(x\) lies outside the projection \(\{x:(x,y)\in C\text{ for some }y\}\) if and only if \(T_C(x)\in\mathrm{WF}(P)\).

**Proof.** (1) \(y\in[T(x)]\) means \(y|k\in T(x)\), that is, \((x|k,y|k)\in T\), for all \(k\); this says \((x,y)\in[T]\).

(2) For fixed \(t\) with \(|t|=k\), the condition \(t\in T(x)\) holds exactly when \((x,T)\) lies in \(\bigcup_{|s|=k}\big(O_s\times\{T:(s,t)\in T\}\big)\). This set is open, and so is its complement \(\bigcup_{|s|=k}\big(O_s\times\{T:(s,t)\notin T\}\big)\), because the cylinders \(O_s\) with \(|s|=k\) partition \(Q^{\mathbb N}\). So each coordinate of \(T(x)\) is a continuous function of \((T,x)\).

(3) By Proposition 6.3(2), \([T_C]=C\), so by (1), \([T_C(x)]\) is the set of \(y\) with \((x,y)\in C\). It is empty exactly when \(x\) is outside the projection of \(C\). Continuity is (2) with \(T=T_C\) fixed. \(\square\)

### 7. Countable orders and well-orders

Relations on \(Q\) are subsets \(R\subseteq Q\times Q\), that is, points of \(2^{Q\times Q}\). The *domain* of \(R\) is \(D(R)=\{q:(q,q)\in R\}\). We write \(q\leq_Rq'\) for \((q,q')\in R\), and \(q<_Rq'\) if moreover \(q\neq q'\).

**Definition 7.1.** A relation \(R\) is an *order* if
1. \(q\leq_Rq'\) implies \(q,q'\in D(R)\);
2. \(q\leq_Rq'\) and \(q'\leq_Rq\) imply \(q=q'\);
3. \(q\leq_Rq'\leq_Rq''\) implies \(q\leq_Rq''\).

It is a *linear order* if moreover any \(q,q'\in D(R)\) satisfy \(q\leq_Rq'\) or \(q'\leq_Rq\), and a *well-order* if moreover every nonempty subset of \(D(R)\) has an \(R\)-least element. We write \(\mathrm{PO}(Q)\supseteq\mathrm{LO}(Q)\supseteq\mathrm{WO}(Q)\) for these sets of relations.

So an order is a reflexive partial order on its domain that relates nothing outside the domain. Since \(Q\) is countable, a linear order \(R\) is a well-order exactly when there is no sequence \((z_k)_{k\geq1}\) in \(D(R)\) with \(z_{k+1}<_Rz_k\) for all \(k\). Indeed, such a sequence has no least element. Conversely, if a nonempty \(S\subseteq D(R)\) has no least element, fix an enumeration of \(Q\), pick \(z_1\in S\), and let \(z_{k+1}\) be the first element of \(S\) in the enumeration with \(z_{k+1}<_Rz_k\).

**Proposition 7.2.**
1. \(\mathrm{PO}(Q)\) and \(\mathrm{LO}(Q)\) are closed subsets of \(2^{Q\times Q}\). So they are compact metrizable spaces and standard Borel spaces.
2. \(\mathrm{WO}(Q)\) is co-Souslin, in \(\mathrm{LO}(Q)\) and in \(2^{Q\times Q}\).
3. For \(R\in\mathrm{LO}(Q)\), let \(T_R\) consist of the finite sequences \((z_1,\dots,z_k)\) with entries in \(D(R)\) and \(z_{i+1}<_Rz_i\) for \(i<k\). Then \(T_R\) is a tree, \(R\mapsto T_R\) is continuous from \(\mathrm{LO}(Q)\) to \(2^{Q^{<\mathbb N}}\), and \(R\in\mathrm{WO}(Q)\) if and only if \(T_R\in\mathrm{WF}(Q)\).

**Proof.** (1) For fixed elements, each condition in Definition 7.1 and the linearity condition involve finitely many coordinates of \(R\), so they define open and closed sets; \(\mathrm{PO}(Q)\) and \(\mathrm{LO}(Q)\) are countable intersections of such sets. Closed subsets of \(2^{Q\times Q}\) are compact and metrizable, hence Polish.

(2) The set of pairs \((R,z)\in\mathrm{LO}(Q)\times Q^{\mathbb N}\) with \(z_{k+1}<_Rz_k\) for all \(k\) is closed, since each condition involves finitely many coordinates of \((R,z)\). By the remark before the proposition, its projection to \(\mathrm{LO}(Q)\) is \(\mathrm{LO}(Q)\setminus\mathrm{WO}(Q)\), which is therefore Souslin by Proposition 5.2(4). So \(\mathrm{WO}(Q)\) is co-Souslin in \(\mathrm{LO}(Q)\), and in \(2^{Q\times Q}\) because \(\mathrm{LO}(Q)\) is closed there.

(3) Initial segments of strictly decreasing sequences are strictly decreasing, so \(T_R\) is a tree. For fixed \(s=(z_1,\dots,z_k)\), the condition \(s\in T_R\) involves the coordinates \((z_i,z_i)\) and \((z_{i+1},z_i)\) of \(R\) and the conditions \(z_{i+1}\neq z_i\); so it defines an open and closed set, and \(R\mapsto T_R\) is continuous. The body \([T_R]\) is the set of infinite strictly decreasing sequences, which is empty exactly when \(R\) is a well-order. \(\square\)

Strict decrease matters in (3). If the tree were built from sequences with \(z_{i+1}\leq_Rz_i\), every constant sequence \((z,z,\dots,z)\) with \(z\in D(R)\) would belong to it, and for a nonempty domain the tree would never be well-founded.

To compare well-orders we use embeddings.

**Definition 7.3.** For \(R,S\in\mathrm{LO}(\mathbb N)\), write \(R\preceq S\) if some injective map \(\varphi:D(R)\to D(S)\) satisfies \(m\leq_Rn\iff\varphi(m)\leq_S\varphi(n)\) for \(m,n\in D(R)\). Write \(R\prec S\) if such a \(\varphi\) can be chosen with values in \(\{n\in D(S):\ n<_Sq\}\) for some \(q\in D(S)\).

**Lemma 7.4.**
1. The sets \(\{(R,S):R\preceq S\}\) and \(\{(R,S):R\prec S\}\) are Souslin subsets of \(\mathrm{LO}(\mathbb N)\times\mathrm{LO}(\mathbb N)\).
2. If \(R\preceq S\) and \(S\in\mathrm{WO}(\mathbb N)\), then \(R\in\mathrm{WO}(\mathbb N)\).
3. Let \(R,S\in\mathrm{WO}(\mathbb N)\) have order types \(|R|\) and \(|S|\) (S2). Then \(R\preceq S\) if and only if \(|R|\leq|S|\), and \(R\prec S\) if and only if \(|R|<|S|\).

**Proof.** (1) Extending \(\varphi\) arbitrarily outside \(D(R)\), \(R\preceq S\) holds exactly when some \(\varphi\in\Lambda\) satisfies, for all \(m,n\in\mathbb N\) with \(m,n\in D(R)\): \(\varphi(m)\neq\varphi(n)\) if \(m\neq n\), and \((m,n)\in R\iff(\varphi(m),\varphi(n))\in S\). For fixed \(m,n\), the set of \((\varphi,S)\) with \((\varphi(m),\varphi(n))\in S\) is the union over \(p,p'\) of the open sets \(\{\varphi:\varphi(m)=p,\ \varphi(n)=p'\}\times\{S:(p,p')\in S\}\), and its complement is the analogous union; so it is open and closed. Hence the set of \((\varphi,R,S)\) satisfying all conditions is closed in \(\Lambda\times\mathrm{LO}(\mathbb N)^2\), and its projection is Souslin by Proposition 5.2(4). For \(\prec\), add a variable \(q\in\mathbb N\) and the conditions \(q\in D(S)\) and \(\varphi(m)<_Sq\) for \(m\in D(R)\), which are of the same kind.

(2) \(\varphi\) carries a strictly \(R\)-decreasing sequence to a strictly \(S\)-decreasing one, because it is injective and preserves the order in both directions.

(3) Let \(S_{<q}\) denote the restriction of \(S\) to \(\{n\in D(S):n<_Sq\}\), a proper initial segment. If \(|R|\leq|S|\), then by (S2) \(R\) is isomorphic to \(S\) or to some \(S_{<q}\); in either case \(R\preceq S\), and in the second case \(R\prec S\). Suppose now \(R\preceq S\) through \(\varphi\), but \(|S|<|R|\). By (S2), \(S\) is isomorphic to some \(R_{<q}\) through \(\psi\). Then \(\psi\circ\varphi\) is a strictly increasing map of \(D(R)\) into \(\{n:n<_Rq\}\), so \(\psi(\varphi(q))<_Rq\), which contradicts (S1). Hence \(R\preceq S\) implies \(|R|\leq|S|\). If \(R\prec S\) through a map into \(S_{<q}\), then \(R\preceq S_{<q}\), so \(|R|\leq|S_{<q}|\); and \(|S_{<q}|<|S|\), since \(S_{<q}\preceq S\) and \(S_{<q}\) is not isomorphic to \(S\) by (S1). If \(|R|<|S|\), then \(R\) is isomorphic to a proper initial segment of \(S\) by (S2), so \(R\prec S\). \(\square\)

### 8. Every co-Souslin set comes from the well-orders

We code trees on \(\mathbb N\) by linear orders on \(\mathbb N\). Fix a bijection \(e:\mathbb N\to\mathbb N^{<\mathbb N}\): list words in increasing order of the weight \(|s|+\sum_js_j\), and lexicographically within each weight. Every weight class is finite, every word occurs, and there are infinitely many words, so this produces exactly such a bijection.

**Lemma 8.1.** For \(T\subseteq\mathbb N^{<\mathbb N}\) let
\[
\begin{gathered}
K(T)\\
=\{(m,n)\in\mathbb N\times\mathbb N :\\
\ e(m)\in T,\ e(n)\in T,\\
\ e(m)\leq_{\mathrm{KB}}e(n)\}.
\end{gathered}
\]
Then \(K\) is a continuous map of \(2^{\mathbb N^{<\mathbb N}}\) into \(\mathrm{LO}(\mathbb N)\), the domain of \(K(T)\) is \(e^{-1}(T)\), and \(e\) is an order isomorphism of \(\big(e^{-1}(T),\leq_{K(T)}\big)\) onto \((T,\leq_{\mathrm{KB}})\). In particular, when \(T\) is a tree, \(K(T)\) is a well-order exactly when \(T\) is well-founded.

**Proof.** The coordinate \((m,n)\) of \(K(T)\) is \(0\) when \(e(n)<_{\mathrm{KB}}e(m)\), and otherwise equals \(1_T(e(m))\,1_T(e(n))\); so it is continuous in \(T\). The order properties follow from Lemma 6.5, and the last claim from Theorem 6.6. \(\square\)

**Theorem 8.2** (universality of the well-orders). Let \(X\) be a standard Borel space and \(A\subseteq X\) a co-Souslin set.
1. There is a Borel map \(F:X\to\mathrm{LO}(\mathbb N)\) with \(A=F^{-1}(\mathrm{WO}(\mathbb N))\).
2. If \(X=\Lambda\), the map \(F\) can be chosen continuous.

**Proof.** (1) Fix a Polish topology on \(X\) that generates its Borel sets, and a compatible metric. If \(A=X\), take \(F\) constant, equal to the empty relation, which is a well-order. Otherwise \(X\setminus A\) is a nonempty Souslin set, so \(X\setminus A=g(\Lambda)\) for a continuous \(g:\Lambda\to X\) by (D3). For \(x\in X\) put
\[
\tau(x)=\{s\in\mathbb N^{<\mathbb N}:\ x\in\overline{g(\Lambda_s)}\}.
\]
If \(s\sqsubseteq t\), then \(\Lambda_t\subseteq\Lambda_s\), so \(\tau(x)\) is a tree. The map \(\tau:X\to2^{\mathbb N^{<\mathbb N}}\) is Borel, since \(\{x:s\in\tau(x)\}=\overline{g(\Lambda_s)}\) is closed for each \(s\).

*Claim: \(\tau(x)\) is ill-founded if and only if \(x\in g(\Lambda)\).* If \(x=g(z)\), then \(x\in g(\Lambda_{z|k})\) for all \(k\), so \(z\in[\tau(x)]\). Conversely, let \(z\in[\tau(x)]\), so that \(x\in\overline{g(\Lambda_{z|k})}\) for all \(k\), and suppose \(x\neq g(z)\). Choose disjoint open sets \(U\ni g(z)\) and \(V\ni x\) with \(\overline U\cap V=\varnothing\), for instance balls of radius one third of the distance. By continuity, \(\Lambda_{z|k}\subseteq g^{-1}(U)\) for large \(k\), so \(\overline{g(\Lambda_{z|k})}\subseteq\overline U\), which misses \(V\ni x\). This is a contradiction, so \(x=g(z)\).

Put \(F=K\circ\tau\), a Borel map into \(\mathrm{LO}(\mathbb N)\) by Lemma 8.1. By the claim and Lemma 8.1, \(F(x)\in\mathrm{WO}(\mathbb N)\) exactly when \(\tau(x)\) is well-founded, that is, when \(x\in A\).

(2) If \(A=\Lambda\), take \(F\) constant. Otherwise \(\Lambda\setminus A=g(\Lambda)\) for a continuous \(g:\Lambda\to\Lambda\). The set \(C=\{(g(y),y):y\in\Lambda\}\) is closed in \(\Lambda\times\Lambda\), and its projection to the first factor is \(\Lambda\setminus A\). By Lemma 6.7(3), \(x\mapsto T_C(x)\) is continuous, and \(x\in A\) exactly when \(T_C(x)\) is well-founded. So \(F(x)=K(T_C(x))\) is continuous and \(A=F^{-1}(\mathrm{WO}(\mathbb N))\) by Lemma 8.1. \(\square\)

**Corollary 8.3.** \(\mathrm{WO}(\mathbb N)\) and \(\mathrm{WF}(\mathbb N)\) are co-Souslin but not Souslin. In particular they are not Borel.


**Proof.** They are co-Souslin by Propositions 7.2(2) and 6.3(3). If \(\mathrm{WO}(\mathbb N)\) were Souslin, then by Theorem 8.2 and (D1) every co-Souslin subset of \(\mathcal C\) would be Souslin, against Proposition 5.2(5). By Proposition 7.2(3), \(\mathrm{WO}(\mathbb N)\) is the preimage of \(\mathrm{WF}(\mathbb N)\) under the continuous map \(R\mapsto T_R\) on \(\mathrm{LO}(\mathbb N)\); so if \(\mathrm{WF}(\mathbb N)\) were Souslin, \(\mathrm{WO}(\mathbb N)\) would be too. Borel sets are Souslin (D1). \(\square\)

### 9. Reduction and the second separation theorem

**Theorem 9.1** (reduction). Let \(X\) be a standard Borel space and \(A_n\), \(n\in I\), countably many co-Souslin subsets of \(X\). There are pairwise disjoint co-Souslin sets \(C_n\subseteq A_n\) with \(\bigcup_nC_n=\bigcup_nA_n\).

Marker’s freely readable notes give the two-set rank argument; the proof here establishes the stated countable reduction.

**Proof.** Number \(I\) by an initial segment of \(\mathbb N\). By Theorem 8.2, choose Borel maps \(F_n:X\to\mathrm{LO}(\mathbb N)\) with \(A_n=F_n^{-1}(\mathrm{WO}(\mathbb N))\). Let \(C_n\) be the set of \(x\in A_n\) such that
\[
\begin{gathered}
F_m(x)\not\preceq F_n(x)\ \text{ for all }m<n,\\
F_m(x)\not\prec F_n(x)\ \text{ for all }m>n .
\end{gathered}
\tag{9.1}
\]
Each set \(\{x:F_m(x)\preceq F_n(x)\}\) is the preimage of a Souslin set (Lemma 7.4(1)) under the Borel map \(x\mapsto(F_m(x),F_n(x))\), hence Souslin by (D1); the same holds for \(\prec\). So \(C_n\) is the intersection of \(A_n\) with countably many co-Souslin sets, and it is co-Souslin (Proposition 5.2(2)).

Fix \(x\), and let \(J=\{n:x\in A_n\}\). For \(n\in J\) let \(\alpha_n\) be the order type of the well-order \(F_n(x)\). Let \(n\in J\). If \(m\notin J\), then \(F_m(x)\) is not a well-order, so neither \(F_m(x)\preceq F_n(x)\) nor \(F_m(x)\prec F_n(x)\) holds, by Lemma 7.4(2). If \(m\in J\), then \(F_m(x)\preceq F_n(x)\) means \(\alpha_m\leq\alpha_n\), and \(F_m(x)\prec F_n(x)\) means \(\alpha_m<\alpha_n\), by Lemma 7.4(3). So (9.1) says: \(\alpha_m>\alpha_n\) for \(m\in J\) with \(m<n\), and \(\alpha_m\geq\alpha_n\) for \(m\in J\) with \(m>n\). In other words, \(x\in C_n\) exactly when \(\alpha_n\) is the least of the ordinals \(\alpha_m\), \(m\in J\), and \(n\) is the first index where this least value occurs. A nonempty set of ordinals has a least element (S2), so every \(x\in\bigcup_nA_n\) lies in exactly one \(C_n\). \(\square\)

**Corollary 9.2** (second separation theorem). Let \(X\) be a standard Borel space.
1. If \(A_n\), \(n\in I\), are countably many Souslin subsets of \(X\), there are pairwise disjoint co-Souslin sets \(C_n\) with \(A_n\setminus\bigcup_{m\neq n}A_m\subseteq C_n\).
2. In particular, for Souslin sets \(A\) and \(B\) there are disjoint co-Souslin sets \(C\) and \(D\) with \(A\setminus B\subseteq C\) and \(B\setminus A\subseteq D\).

**Proof.** (1) The sets \(E_n=X\setminus\bigcup_{m\neq n}A_m\) are co-Souslin by (D1). Theorem 9.1 gives pairwise disjoint co-Souslin sets \(C_n\subseteq E_n\) with \(\bigcup_nC_n=\bigcup_nE_n\). Let \(x\in A_n\setminus\bigcup_{m\neq n}A_m\). Then \(x\in E_n\), and \(x\notin E_k\) for \(k\neq n\), because \(x\in A_n\) and \(n\neq k\). So \(x\) lies in some \(C_k\subseteq E_k\), and necessarily \(k=n\). (2) is (1) for two sets. \(\square\)

Lusin’s separation theorem separates *disjoint* Souslin sets by Borel sets ([the separation theorem](polish-spaces-and-standard-borel-spaces.md#oa-fnd-pb-03)). In Corollary 9.2 the sets \(C\) and \(D\) cannot always be chosen Borel; Exercise 5 gives an example.

### 10. Sets of uniqueness and countable-to-one maps

**Theorem 10.1** (sets of uniqueness). Let \(X,Y\) be standard Borel spaces and \(G\subseteq X\times Y\) a Borel set. The set of \(y\in Y\) for which exactly one \(x\in X\) has \((x,y)\in G\) is co-Souslin. In particular, for a Borel map \(f:X\to Y\), the set
\[
Z_f=\{y\in Y :\ f^{-1}(y)\text{ has exactly one point}\}
\]
is co-Souslin.


**Proof.** The second statement is the first for the graph of \(f\), which is Borel by (D7).

*Reduction.* Fix Polish topologies on \(X\) and \(Y\) that generate their Borel sets, and a compatible metric on \(Y\). By (D6) there are a closed set \(F\subseteq\Lambda\) and a continuous bijection \(k:F\to G\). Put \(p=\pi_Y\circ k:F\to Y\), a continuous map. For each \(y\), \(k\) maps \(p^{-1}(y)\) bijectively onto \(\{(x,y)\in G\}\). So the set in the theorem is \(Z_p\), and it suffices to show that \(Z_p\) is co-Souslin.

*The sets.* For \(s\in\mathbb N^{<\mathbb N}\) put \(A_s=p(F\cap\Lambda_s)\), a Souslin set (a continuous image of a closed subset of \(\Lambda\), or empty), and for \(|s|=k\geq1\) let \(B_s=\bigcup\{A_t:\ |t|=k,\ t\neq s\}\), a Souslin set. Fix \(k\geq1\). By Corollary 9.2(1), applied to the countable family \((A_s)_{|s|=k}\), there are pairwise disjoint co-Souslin sets \(C_s\), \(|s|=k\), with \(A_s\setminus B_s\subseteq C_s\). For \(|s|\geq1\) put
\[
\begin{gathered}
C'_s\\
=C_s\cap\bigcap_{1\leq j<|s|}C_{s|j},\\
C^*_s\\
=C'_s\cap\overline{A_s}\cap(Y\setminus B_s).
\end{gathered}
\]
These sets are co-Souslin, and for each \(k\) the sets \(C^*_s\), \(|s|=k\), are pairwise disjoint.

*Claim: \(A_s\setminus B_s\subseteq C^*_s\).* Let \(y\in A_s\setminus B_s\) with \(|s|=k\). Then \(y\in C_s\), \(y\in\overline{A_s}\) and \(y\notin B_s\). Let \(1\leq j<k\). Then \(y\in A_s\subseteq A_{s|j}\). If \(y\in A_u\) for some \(u\neq s|j\) with \(|u|=j\), then \(y=p(z)\) for some \(z\in F\cap\Lambda_u\), and \(z|k\neq s\), so \(y\in A_{z|k}\subseteq B_s\), which is false. So \(y\in A_{s|j}\setminus B_{s|j}\subseteq C_{s|j}\). Hence \(y\in C^*_s\).

Let \(Z'=\bigcap_{k\geq1}\bigcup_{|s|=k}C^*_s\), a co-Souslin set by Proposition 5.2(2). We show \(Z_p=Z'\).

*\(Z_p\subseteq Z'\).* Let \(p^{-1}(y)=\{z\}\) and \(k\geq1\). Then \(y\in A_{z|k}\). If \(y\in A_t\) with \(|t|=k\) and \(t\neq z|k\), then \(y\) would have a preimage in \(\Lambda_t\), different from \(z\). So \(y\in A_{z|k}\setminus B_{z|k}\subseteq C^*_{z|k}\) by the claim.

*\(Z'\subseteq Z_p\).* Let \(y\in Z'\). For each \(k\geq1\) there is exactly one \(s^k\) with \(|s^k|=k\) and \(y\in C^*_{s^k}\), by disjointness. For \(k\geq1\), \(y\in C^*_{s^{k+1}}\subseteq C_{s^{k+1}|k}\) and \(y\in C^*_{s^k}\subseteq C_{s^k}\); as the sets \(C_t\), \(|t|=k\), are disjoint, \(s^{k+1}|k=s^k\). So there is \(z\in\Lambda\) with \(z|k=s^k\) for all \(k\). Now \(y\in\overline{A_{z|k}}\), so \(A_{z|k}\neq\varnothing\) and \(F\cap\Lambda_{z|k}\neq\varnothing\) for all \(k\). The cylinders \(\Lambda_{z|k}\) form a neighbourhood base at \(z\) and \(F\) is closed, so \(z\in F\). If \(y\neq p(z)\), choose open \(U\ni p(z)\) and \(V\ni y\) with \(\overline U\cap V=\varnothing\). By continuity \(p(F\cap\Lambda_{z|k})\subseteq U\) for large \(k\), so \(\overline{A_{z|k}}\subseteq\overline U\) misses \(y\); this is false. So \(y=p(z)\). If also \(y=p(z')\) with \(z'\in F\), \(z'\neq z\), choose \(k\) with \(z'|k\neq z|k\). Then \(y\in A_{z'|k}\subseteq B_{z|k}\), while \(y\in C^*_{z|k}\subseteq Y\setminus B_{z|k}\). This is impossible, so \(p^{-1}(y)=\{z\}\) and \(y\in Z_p\). \(\square\)

The set \(\{y:f^{-1}(y)\text{ has at least two points}\}\) is the projection of the Borel set \(\{(x,x')\in X\times X:x\neq x',\ f(x)=f(x')\}\) under \((x,x')\mapsto f(x)\), so it is Souslin, and "at most one preimage" is a co-Souslin condition for simple reasons. The content of Theorem 10.1 is that "at least one preimage", which by itself is only a Souslin condition, becomes co-Souslin in combination with "at most one".

**Example 10.2** (the theorem is sharp). Let \(D\subseteq\mathcal C\) be the Souslin set of (D4) that is not Borel, and write \(D=g(\Lambda)\) with \(g\) continuous (D3).

(a) *\(Z_f\) need not be Borel.* Let \(X\) be the disjoint union of \(\Lambda\) and \(\mathcal C\), a Polish space, and let \(f:X\to\mathcal C\) be \(g\) on \(\Lambda\) and the identity on \(\mathcal C\). Then \(f^{-1}(y)\) consists of \(y\) and the points of \(g^{-1}(y)\), so it is a singleton exactly when \(y\notin D\). Hence \(Z_f=\mathcal C\setminus D\), which is co-Souslin and not Borel.

(b) *The domain must be standard.* Give \(D\) its relative Borel structure and let \(f:D\to\mathcal C\) be the inclusion. Every fibre has at most one point, and \(Z_f=D\). This set is not co-Souslin: otherwise it would be Borel by (D2).

**Lemma 10.3** (isolated points). Let \(L\) be a nonempty countable closed subset of a Polish space. Then every nonempty \(S\subseteq L\) contains a point \(q\) with an open set \(V\) such that \(V\cap S=\{q\}\).

**Proof.** First, a nonempty countable complete metric space \((M,d)\) has an isolated point. If \(M\) is finite, every point is isolated. Otherwise enumerate \(M=\{l_1,l_2,\dots\}\), and suppose no point is isolated. Then every open ball in \(M\) is infinite, since a ball with finitely many points would contain an isolated point. Choose recursively points \(c_j\in M\) and radii \(0<r_j<2^{-j}\) such that the closed ball \(\overline B_j=\{l:d(l,c_j)\leq r_j\}\) lies in the open ball \(\{l:d(l,c_{j-1})<r_{j-1}\}\) (in \(M\) itself for \(j=1\)) and does not contain \(l_j\). This is possible: the open ball is infinite, so it contains some \(c_j\neq l_j\), and a small radius does the rest. The closed balls \(\overline B_j\) decrease and their diameters tend to \(0\), so by (D9) they have a common point. It differs from every \(l_j\), which is absurd.

Now let \(\emptyset\neq S\subseteq L\). The closure \(\overline S\subseteq L\) is nonempty, countable and closed, hence complete for a complete compatible metric. So it has an isolated point \(q\): some open \(V\) has \(V\cap\overline S=\{q\}\). Since \(q\in\overline S\), \(V\) meets \(S\), and \(V\cap S\subseteq\{q\}\); so \(V\cap S=\{q\}\). \(\square\)

**Theorem 10.4** (countable-to-one maps). Let \(X,Y\) be standard Borel spaces and \(f:X\to Y\) a Borel map such that every fibre \(f^{-1}(y)\) is countable.
1. \(f(B)\) is Borel for every Borel set \(B\subseteq X\); in particular \(f(X)\) is Borel.
2. There is a Borel map \(g:f(X)\to X\) with \(f(g(y))=y\) for all \(y\in f(X)\).


**Proof.** *Reduction.* Fix Polish topologies on \(X\) and \(Y\) that generate their Borel sets, and a countable base \((V_m)\) of \(Y\). By (D5) we may refine the topology of \(X\), without changing its Borel sets, so that every \(f^{-1}(V_m)\) is open. Then \(f\) is continuous, and each fibre \(f^{-1}(y)\) is closed and countable. Let \((U_n)\) be a countable base of \(X\).

(1) Let \(B\subseteq X\) be Borel, and for each \(n\) let \(B_n\) be the set of \(y\) such that \(f^{-1}(y)\cap B\cap U_n\) has exactly one point. The set \(B\cap U_n\) is a standard Borel space (D5), and Theorem 10.1, applied to the restriction of \(f\) to it, shows that \(B_n\) is co-Souslin. Clearly \(B_n\subseteq f(B)\). Conversely, let \(y\in f(B)\). Lemma 10.3, applied to \(L=f^{-1}(y)\) and \(S=f^{-1}(y)\cap B\), gives a point \(q\) and an open set \(V\) with \(V\cap S=\{q\}\). A basic set \(U_n\) with \(q\in U_n\subseteq V\) then has \(f^{-1}(y)\cap B\cap U_n=\{q\}\), so \(y\in B_n\). Hence \(f(B)=\bigcup_nB_n\) is co-Souslin (Proposition 5.2(2)). It is also Souslin (D1), so it is Borel (D2).

(2) For each \(n\), the set \(M_n\) of \(y\) with at least two preimages in \(U_n\) is the image of the Borel set \[
\begin{gathered}
P_n\\
=\{(x,x')\in U_n\times U_n:\ x\neq x',\ f(x)=f(x')\}
\end{gathered}
\] under the map \((x,x')\mapsto f(x)\). The set \(P_n\) is a standard Borel space (D5), and on \(P_n\) this map is Borel with countable fibres, since the fibre over \(y\) lies in \(f^{-1}(y)\times f^{-1}(y)\), a countable set by the explicit pairing in [Proposition 8.3 of the Hahn–Banach lesson](hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.md#oa-fnd-hb-08). By (1), applied to this map on \(P_n\), \(M_n\) is Borel. So is \(f(U_n)\), by (1). Hence \(B'_n=f(U_n)\setminus M_n\), the set of \(y\) with exactly one preimage in \(U_n\), is Borel. Every \(y\in f(X)\) lies in some \(B'_n\): apply Lemma 10.3 to \(S=L=f^{-1}(y)\) and choose a basic set as in (1). So \(\bigcup_nB'_n=f(X)\). Put \(E_n=B'_n\setminus(B'_1\cup\dots\cup B'_{n-1})\), a Borel partition of \(f(X)\). On the Borel set \(X_n=U_n\cap f^{-1}(E_n)\), \(f\) is injective with image \(E_n\). By (D7), \(f|_{X_n}\) is a Borel isomorphism of \(X_n\) onto \(E_n\). Define \(g=(f|_{X_n})^{-1}\) on \(E_n\). Then \(g\) is Borel on each set of a countable Borel partition of \(f(X)\), hence Borel, and \(f(g(y))=y\). \(\square\)

**Example 10.5** (the hypotheses are needed). (a) *Countable fibres.* The set \(D\) of (D4) is not Borel, but it is \(g(\Lambda)\) for a continuous \(g\) on the standard Borel space \(\Lambda\). By Theorem 10.4, some fibres of \(g\) are uncountable. (b) *A standard domain.* The inclusion of \(D\) into \(\mathcal C\), as in Example 10.2(b), is injective, and its image \(D\) is not Borel.

Part (2) can also be derived from the Borel transversal theorem of [Polish spaces and standard Borel spaces](polish-spaces-and-standard-borel-spaces.md#oa-fnd-pb-10): after the reduction the fibres of \(f\) are closed, and \(f^{-1}(f(U))\) is Borel for every open \(U\) by part (1).

### 11. Borel selectors for closed sets

Given a nonempty closed subset of a Polish space, we want to choose one of its points, or a dense sequence of its points, in a Borel way. We prove this for families of closed sets indexed by an arbitrary measurable space. The Effros space of all nonempty closed sets is one such family.

**Theorem 11.1** (Kuratowski–Ryll-Nardzewski). Let \((\Omega,\mathcal S)\) be a measurable space, \(X\) a Polish space, and \(\Phi\) a map that assigns to each \(\omega\in\Omega\) a nonempty closed set \(\Phi(\omega)\subseteq X\), such that
\[
\begin{gathered}
\{\omega:\ \Phi(\omega)\cap U\neq\varnothing\}\in\mathcal S\\
\text{for every open }U\\
\subseteq X.
\end{gathered}
\tag{11.1}
\]
1. For every open \(U\subseteq X\) there is an \(\mathcal S\)-measurable \(f:\Omega\to X\) with \(f(\omega)\in\Phi(\omega)\) for all \(\omega\), and \(f(\omega)\in U\) whenever \(\Phi(\omega)\cap U\neq\varnothing\).
2. There are \(\mathcal S\)-measurable maps \(f_1,f_2,\ldots:\Omega\to X\) such that, for every \(\omega\), all \(f_n(\omega)\) lie in \(\Phi(\omega)\) and \(\{f_n(\omega):n\geq1\}\) is dense in \(\Phi(\omega)\).
3. Conversely, if maps as in (2) exist, then \(\Phi\) satisfies (11.1).

**Proof.** If \(\Omega=\varnothing\), the unique empty maps prove all assertions. Otherwise the nonempty values of \(\Phi\) force \(X\ne\varnothing\). *Step 1: one selector.* Let \(d\) be a complete compatible metric on \(X\) and \((x_i)_{i\geq1}\) a dense sequence. For \(x\in X\) and \(r>0\), \[
\begin{gathered}
\{\omega:d(x,\Phi(\omega))<r\}\\
=\{\omega:\Phi(\omega)\cap B(x,r)\neq\varnothing\}\in\mathcal S,
\end{gathered}
\] where \(B(x,r)\) is the open ball. For each \(\omega\) we choose indices \(\iota_k(\omega)\), \(k\geq0\), and put \(p_k(\omega)=x_{\iota_k(\omega)}\), so that
\[
\begin{gathered}
d\big(p_k(\omega),\Phi(\omega)\big)<2^{-k},\\
d\big(p_{k+1}(\omega),p_k(\omega)\big)<2^{-k}.
\end{gathered}
\tag{11.2}
\]
Let \(\iota_0(\omega)\) be the least \(i\) with \(d(x_i,\Phi(\omega))<1\). Given \(\iota_k(\omega)\), let \(\iota_{k+1}(\omega)\) be the least \(i\) with \(d(x_i,\Phi(\omega))<2^{-k-1}\) and \(d(x_i,p_k(\omega))<2^{-k}\). Such \(i\) exist. For \(k=0\) this follows from density. For the recursion, pick \(z\in\Phi(\omega)\) with \(d(p_k(\omega),z)<2^{-k}\), and then \(x_i\) with \(d(x_i,z)<\min\big(2^{-k-1},\,2^{-k}-d(p_k(\omega),z)\big)\).

Each \(\iota_k\) is \(\mathcal S\)-measurable, by induction: \(\{\iota_{k+1}=i\}\) is the union over \(j\) of the sets \(\{\iota_k=j\}\cap H_{k,i,j}\setminus\bigcup_{i'<i}H_{k,i',j}\), where \(H_{k,i,j}=\{\omega:d(x_i,\Phi(\omega))<2^{-k-1}\}\) if \(d(x_i,x_j)<2^{-k}\), and \(H_{k,i,j}=\varnothing\) otherwise. So each \(p_k\) is measurable, taking countably many values on measurable sets. By (11.2), \((p_k(\omega))_k\) is a Cauchy sequence, with \(d(p_k(\omega),p_l(\omega))<2^{1-k}\) for \(l>k\). Its limit \(p(\omega)\) satisfies \(d(p(\omega),\Phi(\omega))=\lim_kd(p_k(\omega),\Phi(\omega))=0\), because \(y\mapsto d(y,\Phi(\omega))\) is \(1\)-Lipschitz; so \(p(\omega)\in\Phi(\omega)\), as \(\Phi(\omega)\) is closed. Since \(d(p_k,p)\leq2^{1-k}\), for every closed \(E\subseteq X\)
\[
p^{-1}(E)=\bigcap_kp_k^{-1}\big(\{y:\ d(y,E)\leq2^{1-k}\}\big),
\]
which lies in \(\mathcal S\). Closed sets generate the Borel sets, so \(p\) is measurable.

*Step 2: selectors into an open set.* Let \(U\subseteq X\) be open and nonempty, and \(\Omega_U=\{\omega:\Phi(\omega)\cap U\neq\varnothing\}\in\mathcal S\). By (D5), \(U\) is Polish; fix a complete metric on \(U\) compatible with its topology. For \(\omega\in\Omega_U\), \(\Phi(\omega)\cap U\) is a nonempty closed subset of \(U\). For \(V\) open in \(U\), hence open in \(X\), \[
\begin{gathered}
\{\omega\in\Omega_U :\Phi(\omega)\cap U\cap V\neq\varnothing\}\\
=\{\omega:\Phi(\omega)\cap V\neq\varnothing\}\in\mathcal S.
\end{gathered}
\] So Step 1, applied on the measurable space \(\Omega_U\) with the relative \(\sigma\)-algebra, to \(U\) and to \(\omega\mapsto\Phi(\omega)\cap U\), gives a measurable \(p_U :\Omega_U\to U\) with \(p_U(\omega)\in\Phi(\omega)\cap U\). Put \(f=p_U\) on \(\Omega_U\) and \(f=p\) on \(\Omega\setminus\Omega_U\), with \(p\) from Step 1. Then \(f\) is measurable, \(f(\omega)\in\Phi(\omega)\) always, and \(f(\omega)\in U\) when \(\omega\in\Omega_U\). For \(U=\varnothing\) take \(f=p\). This proves (1).

*Step 3: a dense sequence.* Let \((U_n)\) be a countable base of \(X\), and let \(f_n\) be the map of (1) for \(U_n\). A nonempty relatively open subset of \(\Phi(\omega)\) contains a nonempty set \(\Phi(\omega)\cap U_n\), and then \(f_n(\omega)\) lies in it. This proves (2).

*Step 4: the converse.* If the \(f_n\) are as in (2) and \(U\) is open, then by density \(\{\omega:\Phi(\omega)\cap U\neq\varnothing\}=\bigcup_nf_n^{-1}(U)\), which lies in \(\mathcal S\). \(\square\)

**Corollary 11.2** (Borel selectors on the Effros space). Let \(X\) be a Polish space and \(\mathcal C_0(X)\) the standard Borel space of its nonempty closed subsets (D8).
1. For every open \(U\subseteq X\) there is a Borel map \(f:\mathcal C_0(X)\to X\) with \(f(F)\in F\) for all \(F\), and \(f(F)\in U\) whenever \(F\cap U\neq\varnothing\).
2. There are Borel maps \(f_n:\mathcal C_0(X)\to X\) such that \(\{f_n(F):n\geq1\}\) is a dense subset of \(F\) for every \(F\).

**Proof.** Apply Theorem 11.1 to \(\Omega=\mathcal C_0(X)\) with the Effros structure and \(\Phi(F)=F\). Condition (11.1) holds by the definition of the Effros structure. \(\square\)

In (1) the selector must be allowed to leave \(U\) when \(F\) misses \(U\), since then no point of \(F\) lies in \(U\); what (1) guarantees is that it always stays in \(F\). A choice function that took a fixed value outside \(F\) for those \(F\) would not serve in (2), where every \(f_n(F)\) must lie in \(F\).

## Exercises

**Exercise 1** (medium; commutative case). Let \(K\) be a nonempty compact Hausdorff space and \(A=C(K)\) with the supremum norm. Show that for every \(f\in A\), \(W(f)\) is the closed convex hull of \(f(K)=\sigma(f)\).

*Solution.* Let \(R=\|f\|\). For \(|w|\leq R\) and \(0<t\leq1/R\) (any \(t>0\) if \(R=0\)),
\[
1+t\operatorname{Re}w\leq|1+tw|\leq1+t\operatorname{Re}w+\tfrac12t^2|w|^2 ;
\]
the first inequality is \(\operatorname{Re}z\leq|z|\), and the second follows by squaring, since \[
\begin{gathered}
(1+t\operatorname{Re}w+\tfrac12t^2|w|^2)^2-|1+tw|^2\\
=(t\operatorname{Re}w+\tfrac12t^2|w|^2)^2\\
\geq0
\end{gathered}
\] and the base is nonnegative. Apply this to \(w=e^{i\theta}f(k)\) and take the maximum over \(k\in K\):
\[
\begin{gathered}
\Big|\frac{\|1+te^{i\theta}f\|-1}{t}-\max_{k\in K}\operatorname{Re}\big(e^{i\theta}f(k)\big)\Big|\\
\leq\tfrac12tR^2 .
\end{gathered}
\]
By Theorem 2.3(1), \(m(e^{i\theta}f)=\max_k\operatorname{Re}(e^{i\theta}f(k))\), which is the function \(h\) of Lemma 2.1 for the closed convex hull of \(f(K)\): the maximum of a real-linear function over the closed convex hull of a compact set equals its maximum over the set. Both \(W(f)\) and this hull are nonempty, compact and convex, so they are equal by Lemma 2.1. Finally, \(\sigma(f)=f(K)\), because \(\lambda-f\) is invertible in \(C(K)\) exactly when it has no zero.

**Exercise 2** (easy; a self-adjoint element with nonreal spectrum). On \(A=\mathbb C^2\), with coordinatewise operations and the norm \(\|(z,w)\|=\max(|z|,|w|)\), put \((z,w)^*=(\bar w,\bar z)\). Show that this is an isometric involution, that \(A\) is not a C\*-algebra, and that \(a=(i,-i)\) is self-adjoint and not hermitian. Compute \(\sigma(a)\) and \(W(a)\).

*Solution.* The map is conjugate-linear, \((x^*)^*=x\), and \((xy)^*=x^*y^*=y^*x^*\) because the product is commutative; it preserves the maximum norm. For \(x=(1,0)\), \(x^*x=(0,1)(1,0)=0\), while \(\|x\|^2=1\); so the C\*-identity fails. Next, \(a^*=(\overline{-i},\overline{i})=(i,-i)=a\). The algebra is \(C(\{1,2\})\), so by Exercise 1, \(\sigma(a)=\{i,-i\}\) and \(W(a)\) is the segment from \(-i\) to \(i\). This is not contained in \(\mathbb R\), so \(a\) is not hermitian. Note that the spectrum of \(a\) is not real, which cannot happen for a hermitian element (Corollary 1.4(2)).

**Exercise 3** (easy; stochastic matrices). Let \(T\gg0\) be an \(n\times n\) matrix whose rows sum to \(1\). Show that \(r(T)=1\), and that \(T^k\) converges to the matrix all of whose rows equal the vector \(u\gg0\) determined by \(u^{\top}T=u^{\top}\) and \(\sum_iu_i=1\).

*Solution.* \(T\mathbf 1=\mathbf 1\), so \(\mathbf 1\geq0\) is an eigenvector for the eigenvalue \(1\). By Theorem 4.4(5), \(1=r(T)\), and \(v=\mathbf 1\) is a Perron–Frobenius eigenvector. Let \(u\gg0\) be as in Theorem 4.4(4), normalized by \(u^{\top}\mathbf 1=1\); by Theorem 4.4(2) applied to \(T^{\top}\), it is the only such vector. By Theorem 4.4(7), \(T^k\to\mathbf 1u^{\top}/(u^{\top}\mathbf 1)=\mathbf 1u^{\top}\), the matrix whose rows all equal \(u^{\top}\).

**Exercise 4** (medium; operations on relations). Let \(Q\) be countable. For relations \(R,S\) on \(Q\) put \[
\begin{gathered}
R\ast S\\
=\{(q,q',q''):(q,q')\in R,\ (q',q'')\in S\}\\
\subseteq Q^3
\end{gathered}
\] and \[
\begin{gathered}
R\circ S\\
=\{(q,q''):(q,q',q'')\in R\ast S\text{ for some }q'\}.
\end{gathered}
\] Show that \((R,S)\mapsto R\ast S\) is continuous, that \((R,S)\mapsto R\circ S\) is Borel, and that it is not continuous when \(Q\) is infinite. Use this to show once more that \(\mathrm{PO}(Q)\) is a Borel set, from the description: \(R\in\mathrm{PO}(Q)\) if and only if \(R\cap R^{-1}\) is the diagonal of \(D(R)\), both projections of \(R\) equal \(D(R)\), and \(R\circ R\subseteq R\).

*Solution.* The coordinate \((q,q',q'')\) of \(R\ast S\) is \(1_R(q,q')1_S(q',q'')\), a continuous function of \((R,S)\). The set of \((R,S)\) with \((q,q'')\in R\circ S\) is the union over \(q'\) of the open and closed sets \(\{(q,q')\in R\}\times\{(q',q'')\in S\}\); so it is open, its complement is closed, and each coordinate of \(R\circ S\) is a Borel function of \((R,S)\). Hence the map is Borel. If \(Q\) is infinite, pick distinct \(a,b,c_1,c_2,\ldots\in Q\), and put \(R_n=\{(a,c_n)\}\) and \(S=\{(c_n,b):n\geq1\}\). Every coordinate of \(R_n\) is eventually \(0\), so \(R_n\to\varnothing\). But \(R_n\circ S=\{(a,b)\}\) for all \(n\), while \(\varnothing\circ S=\varnothing\). For the last claim: \(R\mapsto R^{-1}\), \(R\mapsto D(R)\) and \(R\mapsto\{(q,q):q\in D(R)\}\) are continuous; the projections \(\{q:\exists q'\,(q,q')\in R\}\) and \(\{q':\exists q\,(q,q')\in R\}\) are Borel functions of \(R\), for the same reason as \(R\circ S\); and \(R\mapsto(R\circ R,R)\) is Borel, while the inclusion relation \(\{(P',P''):P'\subseteq P''\}\) is closed. Each of the three conditions defines the preimage of a closed set under a Borel map, and the set of pairs of equal points is closed. So \(\mathrm{PO}(Q)\) is Borel. Proposition 7.2(1) shows more: it is closed.

**Exercise 5** (hard; the second separation theorem cannot use Borel sets). Using the universal Souslin set \(U\subseteq\mathcal C\times\mathcal C\) of (D4), find disjoint co-Souslin sets in \(\mathcal C\times\mathcal C\) that no Borel set separates. Conclude that in Corollary 9.2(2) the sets \(C\) and \(D\) cannot always be chosen Borel.

*Solution.* Let \(V=(\mathcal C\times\mathcal C)\setminus U\). Every co-Souslin subset of \(\mathcal C\) is a section \(V_y=\{x:(y,x)\in V\}\). Let \(h:\mathcal C\times\mathcal C\to\mathcal C\) be the homeomorphism that interleaves coordinates, \(h(u,u')=(u_1,u'_1,u_2,u'_2,\dots)\), and write \(h^{-1}(w)=(\pi(w),\pi'(w))\). The sets
\[
\begin{gathered}
A\\
=\{(w,x):\ (\pi(w),x)\in V\},\\
B\\
=\{(w,x):\ (\pi'(w),x)\in V\}
\end{gathered}
\]
are co-Souslin in \(\mathcal C\times\mathcal C\), as preimages of \(V\) under continuous maps (Proposition 5.2(3)). By Theorem 9.1 there are disjoint co-Souslin sets \(A'\subseteq A\) and \(B'\subseteq B\) with \(A'\cup B'=A\cup B\). Suppose a Borel set \(E\) had \(A'\subseteq E\) and \(E\cap B'=\varnothing\). Let \(G\subseteq\mathcal C\) be any Borel set. Both \(G\) and \(\mathcal C\setminus G\) are co-Souslin, so \(G=V_u\) and \(\mathcal C\setminus G=V_{u'}\) for some \(u,u'\). For \(w=h(u,u')\) the sections at \(w\) are \(A_w=G\) and \(B_w=\mathcal C\setminus G\). So \(A'_w\subseteq G\) and \(B'_w\subseteq\mathcal C\setminus G\) are disjoint with union \(\mathcal C\), which forces \(A'_w=G\) and \(B'_w=\mathcal C\setminus G\). Then \(E_w\) contains \(G\) and misses \(\mathcal C\setminus G\), so \(E_w=G\). Thus every Borel subset of \(\mathcal C\) is a section of the one Borel set \(E\). But \(G_0=\{x:(x,x)\notin E\}\) is Borel, so \(G_0=E_{w_0}\) for some \(w_0\), and then \(w_0\in G_0\) if and only if \((w_0,w_0)\notin E\), if and only if \(w_0\notin E_{w_0}=G_0\). This contradiction shows that no Borel set separates \(A'\) from \(B'\).

Now put \(A''=(\mathcal C\times\mathcal C)\setminus B'\) and \(B''=(\mathcal C\times\mathcal C)\setminus A'\), two Souslin sets. Since \(A'\) and \(B'\) are disjoint, \(A''\setminus B''=A'\) and \(B''\setminus A''=B'\). Disjoint Borel sets \(C\supseteq A'\) and \(D\supseteq B'\) would give a Borel set \(C\) that separates \(A'\) from \(B'\), which is impossible.

## References

Open ones first.


*Freely accessible reading:* [Hanna Blazhko; Daniil Homza; Felix L. Schwenninger; Jens de Vries; Michał Wojtylak, *The algebraic numerical range as a spectral set in Banach algebras*, §2, Lemma 2.1](https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/algebraic-numerical-range-as-a-spectral-set-in-banach-algebras/96536D155B032F6C67B750582F5DBF07) gives a route through algebraic numerical ranges and the perturbation estimate of Proposition 1.4a; the classical facts referenced there are proved here. The lesson includes its own complete proofs at the stated hypotheses; references to human sources do not imply permission to adapt their expression.

For tree ranks and two-set coanalytic reduction, see [D. Marker, §5, pp. 43–48](https://homepages.math.uic.edu/~marker/math512/dst.pdf). Sections 6–9 here include the complete countable reduction and second separation arguments.
