# Complex scalars, measure spaces and Lipschitz extension

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The real space \(\ell_1\) has metric Markov cotype two with the constant \(12\sqrt{21}\). This lesson draws consequences. The complex space \(\ell_1\) has the property with the constant \(12\sqrt{42}\). The space \(L_1(\mu)\) of every measure space has it with the constant \(12\sqrt{21}\), by the same proof. The main consequence concerns the extension of Lipschitz maps: by a theorem of Mendel and Naor, which is stated here as a hypothesis and not proved, every Lipschitz map from a subset of a Hilbert space into \(\ell_1\) extends to the whole Hilbert space, and its Lipschitz constant grows at most by a universal factor. The two conditions of that theorem that concern the Hilbert space and the space \(\ell_1\) are proved here: a Hilbert space has Markov type two with the constant \(1\), and \(\ell_1\) is the dual of the space \(c_0\).

- Bi-Lipschitz maps and complex scalars (Lemma 1.1, Corollary 1.2).
- The spaces \(L_1(\mu)\) (Theorem 2.1).
- Markov type two of Hilbert space (Proposition 3.2).
- \(\ell_1\) is the dual of \(c_0\) (Lemma 4.1).
- The hypothesis (MN) and the extension of Lipschitz maps (Corollary 5.1).

The lesson follows [OpenAI-MC, Section 6]; Theorem 2.1 is not stated in that text. It uses [Metric Markov cotype two](metric-markov-cotype-two.md), the cut representation of [Cuts, the cubic map and a quartic potential](cuts-the-cubic-map-and-a-quartic-potential.md), and Theorem 3.1 of [The stopped walk and the cotype inequality](the-stopped-walk-and-the-cotype-inequality.md). Section 2 uses measurable and integrable functions (core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10)); Section 4 uses normed spaces and bounded linear functionals (core course [Functional Analysis](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D20)).

## 1. Bi-Lipschitz maps and complex scalars

**Lemma 1.1.** Let \((X,d_X)\) and \((Y,d_Y)\) be metric spaces, \(L\ge1\), and let \(\theta\) be a map from \(X\) onto \(Y\) with
\[
d_X(x,x')\le d_Y(\theta x,\theta x')\le L\,d_X(x,x')
\]
for all \(x,x'\in X\). If \(Y\) has metric Markov cotype two with the constant \(C\), then \(X\) has it with the constant \(LC\).

**Proof.** Let \(\pi\), \(A\), \(t\) and \(x_1,\dots,x_n\in X\) be given. Apply the property of \(Y\) to the points \(\theta x_i\), and let \(y'_i\in Y\) be the new points. The map \(\theta\) is onto, so \(y'_i=\theta y_i\) with \(y_i\in X\). By the first inequality for \(\theta\), each distance \(d_X(x_i,y_i)\) and \(d_X(y_i,y_j)\) is at most the distance of the images. By the second, \(\mathcal E_{M_t}(\theta x)\le L^2\,\mathcal E_{M_t}(x)\). So
\[
\begin{aligned}
&\sum_i\pi_i\,d_X(x_i,y_i)^2+t\,\mathcal E_A(y)\\
&\qquad\le C^2L^2\,\mathcal E_{M_t}(x) .
\end{aligned}
\]
\(\blacksquare\)

The proof uses that \(\theta\) is onto: the new points for \(\theta x_i\) are found in \(Y\) and must be images of points of \(X\). This is the place where the argument fails for a subspace.

**Corollary 1.2** ([OpenAI-MC, Section 6]). The space \(\ell_1(\mathbb C)\) of complex sequences \(x\) with \(\|x\|_1=\sum_k|x(k)|<\infty\) has metric Markov cotype two with the constant \(12\sqrt{42}\).

**Proof.** Let \(\theta\) map \(x\in\ell_1(\mathbb C)\) to the real sequence with the entries \(\operatorname{Re}x(1)\), \(\operatorname{Im}x(1)\), \(\operatorname{Re}x(2)\), \(\operatorname{Im}x(2)\), and so on. For a complex number \(\zeta\), \(|\zeta|\le|\operatorname{Re}\zeta|+|\operatorname{Im}\zeta|\le\sqrt2\,|\zeta|\). So \(\theta\) is a real-linear map onto the real space \(\ell_1\) with \(\|x\|_1\le\|\theta x\|_1\le\sqrt2\,\|x\|_1\). Lemma 1.1 with \(L=\sqrt2\) gives the constant \(\sqrt2\cdot12\sqrt{21}\). \(\blacksquare\)

## 2. The spaces of integrable functions

Let \((\Omega,\Sigma,\mu)\) be a measure space and \(L_1(\mu)\) the space of real integrable functions on it, with functions that agree almost everywhere identified, and with the norm \(\|x\|_1=\int|x|\,d\mu\). The space \(\ell_1\) is the case of the counting measure on \(\{1,2,3,\dots\}\).

**Theorem 2.1.** Let \(A\) be a stochastic matrix on \([n]\) with a stationary vector \(\pi\), \(t\ge1\) and \(x_1,\dots,x_n\in L_1(\mu)\). Then there are \(y_1,\dots,y_n\in L_1(\mu)\) with
\[
\begin{aligned}
&\sum_i\pi_i\,\|x_i-y_i\|_1^2+t\,\mathcal E_A(y)\\
&\qquad\le3024\,\mathcal E_{M_t}(x) .
\end{aligned}
\]
In particular \(L_1(\mu)\) has metric Markov cotype two with the constant \(12\sqrt{21}\).

**Proof.** If all \(x_i\) are equal, take \(y_i=x_i\). Otherwise it suffices to find a finite nonempty set \(\mathcal B\), weights \(w_B>0\), vertices \(z_i\in\{0,1\}^{\mathcal B}\) and an affine map \(T\) from \(\mathbb R^{\mathcal B}\) to \(L_1(\mu)\) with the three properties of the cut representation:
\[
\begin{gathered}
T(z_i)=x_i,\\
\|x_i-x_j\|_1=\sum_Bw_B\,|z_i(B)-z_j(B)|,\\
\|T(u)-T(u')\|_1\le\sum_Bw_B\,|u_B-u'_B| .
\end{gathered}
\]
The proofs of Proposition 2.1 and Theorem 3.1 of the lesson on the stopped walk use the points \(x_i\) and the space \(\ell_1\) only through these three properties and the triangle inequality of the norm.

Choose measurable functions \(x_i\) on \(\Omega\) that represent the given classes. For a cut \(B\) of \([n]\) and \(\omega\in\Omega\) define
\[
b_B(\omega)=\Bigl(\min_{i\in B}x_i(\omega)-\max_{i\notin B}x_i(\omega)\Bigr)_+
\]
and \(v(\omega)=\min_ix_i(\omega)\). These functions are measurable, as minima and maxima of finitely many measurable functions, and \(|v|\le\sum_i|x_i|\) and \(0\le b_B\le\sum_i|x_i|\); so they are integrable. Let \(w_B=\int b_B\,d\mu\), let \(\mathcal B\) be the set of the cuts with \(w_B>0\), let \(z_i(B)=1\) if \(i\in B\) and \(0\) otherwise, and
\[
T(u)=v+\sum_{B\in\mathcal B}u_B\,b_B .
\]
A cut outside \(\mathcal B\) has \(b_B=0\) almost everywhere. Lemma 1.1 of the lesson on cuts is a statement about \(n\) real numbers; apply it to the numbers \(x_1(\omega),\dots,x_n(\omega)\) for each \(\omega\). As in the proof of Proposition 1.2 there it gives, for every \(\omega\), with sums over all cuts,
\[
\begin{gathered}
v(\omega)+\sum_{B\ni i}b_B(\omega)=x_i(\omega),\\
\sum_B|z_i(B)-z_j(B)|\,b_B(\omega)\\
=|x_i(\omega)-x_j(\omega)| .
\end{gathered}
\]
The first equation gives \(T(z_i)=x_i\) almost everywhere. Integrating the second equation gives the second property. The third follows from \(\|b_B\|_1=w_B\). If \(\mathcal B\) were empty, the second property would give \(x_i=x_j\) in \(L_1(\mu)\) for all \(i,j\). \(\blacksquare\)

The mean-of-medians description of the new points holds here too, with the median taken at every \(\omega\).

## 3. Markov type two

**Definition 3.1** (Ball). A metric space \((X,d)\) has *Markov type two with the constant \(M>0\)* if for all \(n,t\ge1\), every probability vector \(\pi\), every stochastic matrix \(A\) that is reversible for \(\pi\), and all \(x_1,\dots,x_n\in X\),
\[
\mathcal E_{A^t}(x)\le M^2\,t\,\mathcal E_A(x) .
\]

In terms of the walk: the mean squared distance between the points at the times \(0\) and \(t\) is at most \(M^2t\) times the mean squared distance between the points at the times \(0\) and \(1\). Markov type bounds the energy of *the same* points after \(t\) steps from above; metric Markov cotype asks for *new* points whose one-step energy is small.

**Proposition 3.2.** Every real Hilbert space has Markov type two with the constant \(1\).

**Proof.** The two reductions in the proof of Proposition 3.4 of the first lesson apply without change: it suffices to treat the case in which all \(\pi_i>0\) and the points are real numbers \(f_1,\dots,f_n\). Write \(f=\sum_kc_k\varphi_k\) with the orthonormal basis of eigenvectors of Lemma 3.2 there, with eigenvalues \(\lambda_k\in[-1,1]\). By Lemma 3.1 there, for \(P=A^t\) and for \(P=A\),
\[
\begin{aligned}
\mathcal E_{A^t}(f)&=2\sum_kc_k^2\,(1-\lambda_k^t),\\
\mathcal E_A(f)&=2\sum_kc_k^2\,(1-\lambda_k) .
\end{aligned}
\]
For \(-1\le\lambda\le1\),
\[
\begin{aligned}
1-\lambda^t&=(1-\lambda)(1+\lambda+\dots+\lambda^{t-1})\\
&\le t\,(1-\lambda) .
\end{aligned}
\]
\(\blacksquare\)

The same computation is Exercise 5.2 of [Markov type and the reduction to a finite walk](course:markov-type-and-superreflexivity/markov-type-and-the-reduction-to-a-finite-walk) (course *Markov type and superreflexivity*), where Markov type of normed spaces with a general exponent is studied.

## 4. Duality with the null sequences

Let \(c_0\) be the space of the real sequences \(x=(x(k))_{k\ge1}\) with \(x(k)\to0\), with the norm \(\|x\|_\infty=\sup_k|x(k)|\). The *dual* of a normed space \(E\) is the space of the linear maps \(\lambda\) from \(E\) to \(\mathbb R\) for which \(\|\lambda\|=\sup\{|\lambda(x)|:\|x\|\le1\}\) is finite, with this norm.

**Lemma 4.1.** For \(a\in\ell_1\) let \(\lambda_a(x)=\sum_ka(k)x(k)\) for \(x\in c_0\). The map \(a\mapsto\lambda_a\) is linear, maps \(\ell_1\) onto the dual of \(c_0\), and \(\|\lambda_a\|=\|a\|_1\).

**Proof.** The series converges and \(|\lambda_a(x)|\le\|a\|_1\|x\|_\infty\), so \(\lambda_a\) lies in the dual and \(\|\lambda_a\|\le\|a\|_1\). For \(K\ge1\) let \(x^K\) be the sequence with \(x^K(k)=\pm1\), the sign of \(a(k)\), for \(k\le K\) with \(a(k)\ne0\), and \(x^K(k)=0\) otherwise. It lies in \(c_0\) with a norm \(\le1\), and \(\lambda_a(x^K)=\sum_{k\le K}|a(k)|\). So \(\|\lambda_a\|\ge\sum_{k\le K}|a(k)|\) for every \(K\), and \(\|\lambda_a\|=\|a\|_1\).

Let \(\lambda\) be in the dual of \(c_0\), let \(e_k\) be the sequence with \(1\) at the place \(k\) and \(0\) elsewhere, and \(a(k)=\lambda(e_k)\). With signs as above, \(\sum_{k\le K}|a(k)|=\lambda\bigl(\sum_{k\le K}\pm e_k\bigr)\le\|\lambda\|\). So \(a\in\ell_1\). The functionals \(\lambda\) and \(\lambda_a\) agree on every \(e_k\), so on all sequences with finitely many entries different from \(0\). For \(x\in c_0\) the sequences obtained from \(x\) by replacing the entries after the place \(K\) by \(0\) converge to \(x\) in the norm of \(c_0\). Both functionals are continuous, so \(\lambda=\lambda_a\). \(\blacksquare\)

## 5. Extension of Lipschitz maps

For a map \(f\) between metric spaces let \(\operatorname{Lip}(f)\) be the smallest \(L\ge0\) with \(d(f(x),f(x'))\le L\,d(x,x')\) for all \(x,x'\) in the domain of \(f\); the map is *Lipschitz* if such an \(L\) exists.

A real-valued Lipschitz function on a subset of a metric space always extends to the whole space with the same constant (Exercise 6.1). The argument of that exercise treats one real coordinate at a time and does not carry over to maps into \(\ell_1\) (see the solution of Exercise 6.2). For maps into a normed space the question is whether an extension exists whose constant is larger by a bounded factor. For maps from subsets of a Hilbert space into \(\ell_1\) this question was asked by Ball [MN, after Question 1.15]. Ball's approach, completed by Mendel and Naor, reduces it to the two properties of this course.

**Hypothesis (MN)** ([MN, Theorem 1.11 and Corollary 1.13]). There is a number \(c<\infty\) with the following property. Let \((X,d)\) be a metric space that has Markov type two with the constant \(M\). Let \(Y\) be a Banach space that is isometric to the dual of a Banach space and has metric Markov cotype two with the constant \(N\). Then for every subset \(Z\subseteq X\) and every Lipschitz map \(f\) from \(Z\) to \(Y\) there is a map \(F\) from \(X\) to \(Y\) with \(F(z)=f(z)\) for \(z\in Z\) and
\[
\operatorname{Lip}(F)\le c\,M\,N\,\operatorname{Lip}(f) .
\]

This statement is not proved in this course or elsewhere in the programme. In [MN], Theorem 1.11 has one more condition on \(Y\), a barycentre map with a constant \(\Gamma\); for normed spaces it holds with \(\Gamma=1\) [MN, after Definition 1.3]. Theorem 1.11 extends the map to finitely many further points with a bound that does not depend on their number, and Corollary 1.13 passes to the whole space when \(Y\) is a dual Banach space.

**Corollary 5.1** ([OpenAI-MC, Section 6]). Assume (MN). There is a number \(K<\infty\) such that for every real Hilbert space \(\mathcal H\), every subset \(Z\subseteq\mathcal H\) and every Lipschitz map \(f\) from \(Z\) to \(\ell_1\) there is a map \(F\) from \(\mathcal H\) to \(\ell_1\) with \(F(z)=f(z)\) for \(z\in Z\) and
\[
\operatorname{Lip}(F)\le K\,\operatorname{Lip}(f) .
\]
One can take \(K=12\sqrt{21}\,c\) with the number \(c\) of (MN).

**Proof.** The space \(\mathcal H\) has Markov type two with the constant \(1\) (Proposition 3.2). The space \(\ell_1\) is isometric to the dual of \(c_0\) (Lemma 4.1) and has metric Markov cotype two with the constant \(12\sqrt{21}\) (Corollary 3.2 of the lesson on the stopped walk). Apply (MN). \(\blacksquare\)

What is proved in this course and what is assumed: the cotype of \(\ell_1\), of complex \(\ell_1\) and of \(L_1(\mu)\), the Markov type of Hilbert space and the duality are proved in full. The step from these properties to the extension of maps is the hypothesis (MN). Corollary 5.1 is stated for \(\ell_1\) only: the space \(L_1(\mu)\) is in general not a dual space, and this course makes no statement about extensions into it.

## 6. Exercises

**6.1.** Let \(Z\) be a nonempty subset of a metric space \((X,d)\) and \(f\) a function from \(Z\) to \(\mathbb R\) with \(|f(z)-f(z')|\le L\,d(z,z')\). Show that
\[
F(x)=\inf_{z\in Z}\bigl(f(z)+L\,d(x,z)\bigr)
\]
is a real number for every \(x\in X\), that \(F=f\) on \(Z\) and that \(|F(x)-F(x')|\le L\,d(x,x')\).

**6.2.** Let \(\ell_\infty\) be the space of bounded real sequences with the supremum norm. Show that every Lipschitz map from a subset \(Z\) of a metric space \(X\) into \(\ell_\infty\) extends to \(X\) with the same Lipschitz constant.

**6.3.** Show that the number \(\sqrt2\) in the proof of Corollary 1.2 cannot be replaced by a smaller one for the map \(\theta\).

**6.4.** Let \(X\) be a metric space with Markov type two with the constant \(M\) and \(X'\subseteq X\). Show that \(X'\) has Markov type two with the constant \(M\). Where does the same argument fail for metric Markov cotype two?

**6.5.** Let \(\mu\) be the measure on \(\{1,\dots,K\}\) with the weights \(\mu_1,\dots,\mu_K>0\), so that \(\|x\|_1=\sum_k\mu_k|x(k)|\). Write the weight \(w_B\) of a cut in the proof of Theorem 2.1 as a sum, and compute the cuts and weights for \(x_1=(0,0)\), \(x_2=(1,3)\) with \(\mu=(2,5)\).

## 7. Solutions

**6.1.** Fix \(z_0\in Z\). For every \(z\in Z\), \(f(z)\ge f(z_0)-L\,d(z,z_0)\) and \(d(z,z_0)\le d(z,x)+d(x,z_0)\), so
\[
f(z)+L\,d(x,z)\ge f(z_0)-L\,d(x,z_0) .
\]
So the infimum is a real number. For \(x\in Z\) the choice \(z=x\) gives \(F(x)\le f(x)\), and the last inequality with \(z_0=x\) gives \(F(x)\ge f(x)\). For \(x,x'\in X\) and every \(z\), the triangle inequality gives \(d(x,z)\le d(x',z)+d(x,x')\). Multiply by \(L\), add \(f(z)\) and take the infimum over \(z\): \(F(x)\le F(x')+L\,d(x,x')\). The same holds with \(x\) and \(x'\) exchanged.

**6.2.** Let \(L=\operatorname{Lip}(f)\). Every coordinate \(f_k\) of \(f\) satisfies \(|f_k(z)-f_k(z')|\le L\,d(z,z')\). Extend each \(f_k\) to \(F_k\) by Exercise 6.1 and put \(F=(F_k)_k\). Then \(\sup_k|F_k(x)-F_k(x')|\le L\,d(x,x')\). The sequence \(F(x)\) is bounded: for a fixed \(z_0\in Z\), \(|F_k(x)-f_k(z_0)|\le L\,d(x,z_0)\) for all \(k\), and \(f(z_0)\) is bounded. For \(\ell_1\) the same procedure gives no bound, because the norm of \(\ell_1\) is the sum over the coordinates and the coordinates of \(F\) are controlled only one at a time.

**6.3.** For \(x=(1+i,0,0,\dots)\): \(\|x\|_1=\sqrt2\) and \(\|\theta x\|_1=2=\sqrt2\,\|x\|_1\).

**6.4.** Definition 3.1 is a condition on every finite family of points of the space; a family of points of \(X'\) is a family of points of \(X\), and the two sides are the same in both spaces. For cotype, the points \(x_i\in X'\) are points of \(X\), and \(X\) gives new points \(y_i\in X\); these need not lie in \(X'\).

**6.5.** \(w_B=\sum_k\mu_k\,b_B(k)\). In both coordinates the values of \(x_1,x_2\) are \(0\) and a positive number, so the only cut with a positive weight is \(\{2\}\), with \(b_{\{2\}}=(1,3)\) and \(w_{\{2\}}=2\cdot1+5\cdot3=17=\|x_1-x_2\|_1\).

## References

- [OpenAI-MC] OpenAI, *Metric Markov Cotype Two of \(\ell_1\)*, OpenAI Math Release preprint, 5 October 2026, Section 6. https://github.com/openai/math/tree/main/preprints/Metric-Markov-Cotype-Two-of-l1-October-5-2026
- [MN] M. Mendel and A. Naor, *Spectral calculus and Lipschitz extension for barycentric metric spaces*, arXiv:1301.3963, version 2, Definitions 1.1 to 1.3, Theorem 1.11, Corollary 1.13, Question 1.15. https://arxiv.org/abs/1301.3963
