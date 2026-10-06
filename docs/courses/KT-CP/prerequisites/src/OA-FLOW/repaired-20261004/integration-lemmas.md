# Bounded forms and finite-dimensional separation

*Written and self-checked by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Original exposition: CC0 1.0.*

These two earlier-input corollaries make explicit the Hilbert bounded-form step in Lemma 8.2 and the finite-dimensional separation step in Lemma 7.1 of [Covariance and crossed products with nonunital coefficients](covariance-and-crossed-products.md). Inner products are linear in the first variable. The inputs are the complete [Hilbert projection, Riesz and adjoint proofs in CF Section 8](continuous-calculus-and-hilbert-spaces.md#oa-flow.cf.8), and the [scalar compactness](continuous-calculus-and-hilbert-spaces.md#oa-flow.cf.1) and [product compactness](continuous-calculus-and-hilbert-spaces.md#oa-flow.cf.4) proofs. No separability is assumed.

<a id="KTCP-INTEGRATION-FORM-001"></a>

## 1. A bounded sesquilinear form determines its operator

**Theorem 1.1.** Let \(H,K\) be complex Hilbert spaces, and let \(B:H\times K\to\mathbb C\) be linear in its first variable and conjugate linear in its second. If
\[
 |B(u,v)|\leq M\|u\|\|v\|\qquad(u\in H,v\in K),
\]
for a finite \(M\geq0\), there is a unique bounded linear \(T:H\to K\) such that
\[
 B(u,v)=\langle Tu,v\rangle,\qquad \|T\|\leq M.
 \tag{B1}
\]
The same conclusion applies to a form initially defined on dense linear subspaces and satisfying that bound. If \(H=K\) and \(0\leq B(u,u)\leq C\|u\|^2\), then \(T\) is self-adjoint and \(0\leq T\leq CI\). In the dense-subspace version, this last assertion uses the same dense subspace in both variables.

**Proof.** For fixed \(u\), the function \(v\mapsto\overline{B(u,v)}\) is a bounded linear functional on \(K\). CF Section 8 gives a unique \(Tu\) with this functional equal to \(\langle v,Tu\rangle\), and \(\|Tu\|\leq M\|u\|\). Conjugating yields (B1). Uniqueness of its representing vector, applied to addition and scalar multiplication in the first variable, proves linearity of \(T\). If two operators satisfy (B1), their difference at \(u\) is perpendicular to every \(v\), hence zero.

For the dense-subspace version, choose sequences \(u_n\to u\), \(v_n\to v\) in those subspaces. Boundedness of convergent sequences and the estimate
\[
 |B(u_n,v_n)-B(u_m,v_m)|
 \leq M\|u_n-u_m\|\|v_n\|+M\|u_m\|\|v_n-v_m\|
\]
give a Cauchy sequence of values and independence of the choices. Its limit is a sesquilinear form on \(H\times K\) with the same bound; apply the first part. This uses sequences approximating individual vectors, and imposes no countable density assumption.

In the last assertion, real diagonal values imply \(B(u,v)=\overline{B(v,u)}\). Indeed, for any sesquilinear form \(S\),
\[
 S(u,v)=\frac14\sum_{j=0}^3 i^j S(u+i^jv,u+i^jv).
\]
Apply this identity to \(S(u,v)=B(u,v)-\overline{B(v,u)}\), whose diagonal is zero. The adjoint theorem in CF Section 8 now gives \(T=T^*\). The inequalities on the diagonal are exactly the quadratic-form inequalities \(0\leq T\leq CI\). They pass from a dense subspace to its closure by continuity. \(\square\)

<a id="KTCP-INTEGRATION-SEPARATION-001"></a>

## 2. A closest point supplies strict separation

**Theorem 2.1.** Let \(C\subseteq\mathbb R^n\) be nonempty, closed and convex, with its Euclidean inner product. Every \(x\in\mathbb R^n\) has a unique nearest point \(p\in C\). For all \(y\in C\),
\[
 \langle x-p,y-p\rangle\leq0.
 \tag{B2}
\]
If \(x\notin C\), the nonzero vector \(r=x-p\) strictly separates \(x\) from \(C\):
\[
 \langle r,y\rangle\leq\langle r,p\rangle
 <\langle r,x\rangle,
 \qquad
 \langle r,x\rangle-\langle r,p\rangle=\|r\|^2>0.
 \tag{B3}
\]

**Proof.** Choose \(y_0\in C\) and \(R>\|x-y_0\|\). The nonempty set
\(C\cap\{y:\|y-x\|\leq R\}\) is compact. To see this with the stated inputs, put its closed ball in the product of the \(n\) closed coordinate intervals of radius \(R\) about \(x\). Those intervals are compact by CF Section 1; their finite product is compact by CF Section 4. The ball and \(C\) are closed, so their intersection is a closed subset of that compact product. The continuous function \(y\mapsto\|x-y\|\) attains a minimum there: its image is a nonempty compact subset of \(\mathbb R\), hence contains its infimum. That minimum is no larger than \(\|x-y_0\|<R\); points outside the ball have distance greater than \(R\). Thus its minimizer \(p\) is a global nearest point in \(C\).

If \(p,q\) were two distinct minimizers with distance \(d\), their midpoint would lie in \(C\), while expanding the Euclidean squares gives
\[
 \left\|x-\frac{p+q}{2}\right\|^2
 =d^2-\frac14\|p-q\|^2<d^2,
\]
a contradiction. For \(y\in C\) and \(0<t\leq1\), convexity places \(p+t(y-p)\) in \(C\). Minimality and expansion give
\[
 0\leq -2t\langle x-p,y-p\rangle+t^2\|y-p\|^2.
\]
Divide by \(t\) and let \(t\downarrow0\) to obtain (B2). If \(x\notin C\), \(r\neq0\), and (B2) gives the weak inequality in (B3). Its strict gap is \(\langle r,x-p\rangle=\|r\|^2\). For \(n=0\), the unique nonempty subset is the single point and there is no outside \(x\); the nearest-point conclusion is immediate. \(\square\)
