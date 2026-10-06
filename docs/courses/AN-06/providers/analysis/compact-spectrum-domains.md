# Compact positive inverses and diagonal domains

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

For a positive compact operator, a maximizing sequence for its quadratic form yields an eigenvector. Repeating this construction on orthogonal complements gives the full spectral expansion. Inverting its positive eigenvalues then determines the exact domain of the inverse and every diagonal multiplier.

We use the projection, adjoint, finite orthogonalization and Parseval proofs in [Finite-rank traces and the exact ideal bounds](finite-trace-ideals.md#elementary-hilbert-tools), the scalar limits and exponentials in [Elementary functions, angular coordinates and smooth cutoffs](elementary-functions-and-cutoffs.md), and the countable integration results in [Euclidean measure and product integration](finite-derivative-l2.md#euclidean-products).

The earlier programme treatment of this compact spectral result was written by Claude Opus 5.5 (Anthropic) and GPT-6.1 Sol (OpenAI), with CC0 exposition.

## The positive compact spectral proof

We use inner products linear in the first variable and write $K\ge0$ when $(Kx,x)\ge0$ for every $x$. First, for any bounded positive self-adjoint $K$, the quadratic form $q(x)=(Kx,x)$ obeys
\[
 |(Kx,y)|^2\le q(x)q(y).
\]
If $q(y)>0$, insert $x-cy$ into the nonnegative form and minimize over the complex number $c$; its linear term gives this inequality. If $q(y)=0$, the same polynomial in $c$ can remain nonnegative for every complex $c$ only when $(Kx,y)=0$. This also proves that $q(x)=0$ implies $Kx=0$, by testing against every $y$.

Let $M=\sup_{\|x\|=1}q(x)$. Homogeneity and the last inequality give
\[
 \|Kx\|^2=\sup_{\|y\|=1}|(Kx,y)|^2\le Mq(x).
\]
Thus $\|K\|\le M$, whereas Hilbert Cauchy–Schwarz gives $M\le\|K\|$. Hence $M=\|K\|$. Suppose now that $K$ is compact and nonzero. Choose unit vectors $x_j$ with $q(x_j)\to M>0$. Then
\[
 \begin{aligned}
 \|Kx_j-Mx_j\|^2
 &=\|Kx_j\|^2-2M q(x_j)+M^2\\
 &\le M\bigl(M-q(x_j)\bigr)\longrightarrow0.
 \end{aligned}
\]
Compactness gives a subsequence along which $Kx_j$ converges. The last display makes $x_j$ converge along it as well, to a unit vector $e_1$ with $Ke_1=Me_1$. This proves existence of a maximal positive eigenvalue without weak compactness or a spectral measure.

The orthogonal complement of $e_1$ is invariant, since $(Kx,e_1)=(x,Ke_1)$. The restriction remains positive, self-adjoint and compact. Repeat the preceding construction on each successive complement, stopping if the restriction is zero. It yields an orthonormal sequence $e_j$ with positive nonincreasing eigenvalues $\mu_j$. If the process is infinite, then $\mu_j\to0$: otherwise a subsequence has $\mu_j\ge\varepsilon>0$, and its images $Ke_j=\mu_je_j$ are pairwise separated by at least $\sqrt2\varepsilon$, contradicting compactness.

Let $\Pi_N$ project onto the first $N$ vectors. At each unfinished step the norm of $K$ on the remaining complement is $\mu_{N+1}$ by construction, so
\[
 \left\|Kx-\sum_{j\le N}\mu_j(x,e_j)e_j\right\|
 \le\mu_{N+1}\|x\|.
\]
In the infinite case the right side tends to zero; in the finite case the residual is zero when construction stops. This proves the norm-convergent expansion, indeed convergence in operator norm of the finite truncations. Each nonzero eigenvalue has finite multiplicity: an infinite-dimensional eigenspace would supply an infinite orthonormal sequence by successive finite orthogonalization, again contradicting compactness of its images. A vector orthogonal to all the constructed eigenvectors is killed by the expansion. Therefore, if $K$ is injective, this family is complete, whether or not separability of the original Hilbert space was assumed. The zero operator is injective only on the zero space. This proves every compact spectral assertion used next.

<a id="compact-inverse-domains"></a>

## Positive compact inverse

Let $K$ be a bounded compact positive self-adjoint injective operator on a complex Hilbert space $H$. The zero-space case is immediate. The preceding proof provides orthonormal eigenvectors $e_j$ with positive eigenvalues $\mu_j$, repeated according to their finite multiplicities, with a finite or countably infinite index set. Its norm-convergent expansion gives
\[
 Ku=\sum_j\mu_j\langle u,e_j\rangle e_j.
\]
The family is complete: a vector orthogonal to every $e_j$ is killed by the expansion and hence is zero by injectivity. Thus it is an orthonormal basis, even though separability of $H$ was not assumed. In the infinite case $\mu_j\to0$.

The inverse $A=K^{-1}$ has the *exact* domain and action
\[
 D(A)=\operatorname{Ran}K
 =\left\{u=\sum_j u_je_j:\sum_j\mu_j^{-2}|u_j|^2<\infty\right\},
 \qquad Au=\sum_j\mu_j^{-1}u_je_j.
 \tag{1}
\]
Indeed if $u=Kv$, then $u_j=\mu_jv_j$ and the displayed sum is $\|v\|^2$. Conversely, if the sum is finite, $v=\sum_j\mu_j^{-1}u_je_j$ exists in $H$ and $Kv=u$. This also proves that $D(A)$ is dense.

The operator in (1) is self-adjoint: its adjoint identity tested against each $e_j$ forces the coordinates of an adjoint image to be $\mu_j^{-1}u_j$. Such an image is in $H$ precisely on the displayed domain. On that domain the pairing identity follows from Cauchy–Schwarz. Thus both inclusion and maximality are proved, not inferred from a formal diagonal expression.

If an originally given operator $A_0$ has inverse $K$ on all of $H$, then $D(A_0)=\operatorname{Ran}K$ by the two inverse identities and $A_0=A$ on that original domain. Formula (1) therefore does not silently change the realization.

## All diagonal multipliers and ordered domains

Put $\lambda_j=\mu_j^{-1}$ and define
\[
 E(B)u=\sum_{\lambda_j\in B}u_je_j.
\]

for each Borel set $B$. Orthogonality proves intersection products and strong countable additivity; Parseval proves $E(\mathbb R)=I$. The scalar measure is $\mu_u=\sum_j|u_j|^2\delta_{\lambda_j}$. For any finite-valued complex Borel $f$,
\[
 D(f(A))=\{u:\sum_j|f(\lambda_j)|^2|u_j|^2<\infty\},
 \qquad f(A)u=\sum_j f(\lambda_j)u_je_j.
 \tag{2}
\]
Finite partial sums prove the norm identity. If $u_k\to u$ and $f(A)u_k\to v$, every coordinate satisfies $v_j=f(\lambda_j)u_j$; Parseval then proves membership in (2) and closedness. Testing the adjoint identity against each $e_j$ proves $f(A)^*=\overline f(A)$ with exactly the same squared-sum domain. Finite sequences are dense in this domain for the graph norm by truncation.

For two multipliers, direct substitution gives the ordered-product domain
\[
 D(f(A)g(A))=
 \{u:\sum_j|g(\lambda_j)|^2|u_j|^2<\infty,
       \ \sum_j|f(\lambda_j)g(\lambda_j)|^2|u_j|^2<\infty\},
\]
and action $(fg)(A)$ there. For integer $m\geq1$,
\[
 D(A^m)=\{u:\sum_j\lambda_j^{2m}|u_j|^2<\infty\},
 \qquad A^mu=\sum_j\lambda_j^mu_je_j,
\]
since lower moments follow from $\lambda^{2r}\leq1+\lambda^{2m}$ for $r\leq m$. The same maximal-domain formula (2) defines every real-order power when the positive spectral values are used. Bounded multipliers act everywhere and preserve every domain whose weight is multiplied by them; their graph-norm bound follows from the two sums.

<a id="compact-diagonal-evolution"></a>

## The diagonal evolution

For a real constant $c$, set $P=A-cI$ on $D(A)$ and $\nu_j=\lambda_j-c$. The diagonal domain calculation proves self-adjointness on that same domain. Define
\[
 U(t)u=\sum_j e^{-it\nu_j}u_je_j,\qquad t\in\mathbb R.
\]
The modulus-one coefficients and the exponential addition formula give unitarity, $U(t+s)=U(t)U(s)$ and $U(0)=I$. For any finite-valued weight $w_j$, equip its diagonal domain with the graph norm
\[
 \|u\|_w^2=\sum_j(1+|w_j|^2)|u_j|^2.
\]
The group preserves this norm. It is strongly continuous in that norm: choose a finite set of indices so that the weighted tail of $u$ is arbitrarily small. The squared norm of the difference on that tail is at most four times its weighted mass, uniformly in $t$ and $s$, while each of the finitely many remaining coefficients is continuous in time.

If $u\in D(P)$, the scalar fundamental theorem applied to the exponential gives
\[
 \left|\frac{e^{-ih\nu_j}-1}{h}\right|\leq|\nu_j|,
 \qquad
 \frac{e^{-ih\nu_j}-1}{h}\longrightarrow-i\nu_j.
\]
Subtract the limiting derivative. Its squared coefficient is bounded by $4|\nu_j|^2|u_j|^2$, whose sum is finite. The same finite-head and small-tail argument therefore permits differentiation in $H$, and gives $U'(t)u=-iPU(t)u$. Repeating with $P^k u$ proves
\[
 \frac{d^r}{dt^r}U(t)u=(-iP)^rU(t)u
 \quad\text{for }u\in D(P^r).
\]
Continuity of these derivatives follows from strong continuity applied to $P^r u$. More generally, the identical proof works in the weighted graph norm when $\sum_j(1+|w_j|^2)|\nu_j|^{2r}|u_j|^2<\infty$. Thus both the evolution and its derivatives act on precisely the diagonal domains stated, with no interchange of an uncontrolled infinite series.

## References

- Gerald Teschl, [*Mathematical Methods in Quantum Mechanics*, second author edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf), Section 6.2, Theorem 6.6, printed pages 160–161, for the compact self-adjoint spectral theorem.
