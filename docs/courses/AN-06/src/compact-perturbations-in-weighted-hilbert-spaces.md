# Compact perturbations in weighted Hilbert spaces

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

**Working question: What changes when the amplitude weight approaches zero?** On \((0,1)\), the measures \(dx\) and \(x\,dx\) give different norms; a vector can be large near zero in one norm and small in the other. Compactness in the unweighted space alone does not justify a weighted extension. The conserved weighted norm supplies the missing endpoint, after which interpolation transfers the compact part.

A scattering matrix naturally preserves a weighted norm. Its difference from the identity is initially compact in an unweighted space. The weight can approach zero, so the two norms need not be equivalent. This lesson shows how the preserved norm supplies the other endpoint, and how interpolation transfers compactness to all intervening weights.

Let \((M,\mu)\) be a measure space. Let \(a:M\to(0,\infty)\) be bounded and measurable, and set

\[
 H_\kappa=L^2(M,a^\kappa d\mu),\qquad 0\leq\kappa\leq2.
\tag{1}
\]

The hypotheses also permit a weight that is positive and bounded almost everywhere, since changing it on a null set changes none of these spaces. A positive bounded continuous weight on a locally compact measured space is one application.

All pairings are linear in their first variable. Lemma 1.2 proves the precise compact alternative needed here, including the norm bound for its inverse. Section 2 includes the scalar three-lines argument. The earlier programme reading [Bounded strips and the three-lines inequality](../providers/analysis/bounded-strips.md#three-lines), with its [bounded-strip maximum principle](../providers/analysis/bounded-strips.md#bounded-strip-maximum), supplies the rectangle principle from the proved Cauchy mean-value formula. The finite-rank approximation, cutoff convergence, weighted adjoint identity and interpolation argument are proved below.

The [function-space and convergence proofs](../providers/analysis/finite-derivative-l2.md#complete-function-spaces) apply to an arbitrary measure space, with no sigma-finiteness assumption. [Elementary Hilbert tools](../providers/analysis/finite-trace-ideals.md#elementary-hilbert-tools) prove polarization, projections, representing vectors and adjoints. [Compact Fredholm operators, elementary tools](../providers/analysis/compact-fredholm-families.md#fredholm-finite-tools) proves the finite-dimensional and metric compactness facts. The [exponential and real powers](../providers/analysis/elementary-functions-and-cutoffs.md#scalar-exponential) define the complex powers of the positive weight used in Section 2.

<a id="weighted-compact-spaces"></a>

To see the spaces and their inclusions explicitly, put \(A=\max(1,\|a\|_\infty)\). Multiplication by \(a^{\kappa/2}\) is an onto isometry from \(H_\kappa\) to \(L^2(\mu)\), with inverse multiplication by \(a^{-\kappa/2}\). The inverse is measurable and has the required weighted square integral even when it is unbounded pointwise. Thus each \(H_\kappa\) is a complete Hilbert space. Positivity of \(a\) makes the weighted and unweighted null sets identical. For \(0\leq\alpha\leq\beta\leq2\),
\[
 \|u\|_\beta\leq A^{(\beta-\alpha)/2}\|u\|_\alpha.
\]
These are continuous inclusions; they need not have bounded inverses.

<a id="weighted-compact-tools"></a>

## 1. Two compactness facts

We need two elementary Hilbert-space consequences of compactness. Their proof also explains why a strong cutoff can be used on either side of a compact operator.

**Lemma 1.1.** Let \(K:H\to H\) be compact on a Hilbert space.

1. \(K\) is an operator norm limit of finite-rank operators, and \(K^*\) is compact.
2. If \(P_j\) are orthogonal projections and \(P_j\to I\) strongly, then
   \(\|P_jKP_j-K\|\to0\).

**Proof.** Cover the image of the unit ball under \(K\) by finitely many balls of radius \(\varepsilon\), with centers \(y_1,\ldots,y_m\). Let \(P\) project onto their linear span. For every unit \(x\), choose one center within \(\varepsilon\) of \(Kx\). Then
\(\|(I-P)Kx\|\leq\varepsilon\), since \((I-P)y_l=0\) and \(\|I-P\|\leq1\). Thus \(PK\) has finite rank and \(\|PK-K\|\leq\varepsilon\).

Taking adjoints gives a finite-rank approximation \(K^*P\) to \(K^*\), with the same norm error. A norm limit of compact operators is compact: approximate its unit-ball image by the finite \(\varepsilon\)-nets of an approximant's image; the resulting total boundedness and completeness give a compact closure. This proves 1.

Here finite-rank operators are compact because a bounded set in a finite-dimensional Hilbert space has a finite coordinate grid at every prescribed error, and that space is complete. Composition with bounded maps preserves compactness: a bounded map before a compact map sends the unit ball into a fixed multiple of a ball, while a bounded map after it is continuous on the compact image closure. We use this fact for the inverses and truncations below.

Strong convergence and \(\|I-P_j\|\leq1\) give uniform convergence of \((I-P_j)y\) to zero on every compact set. Indeed, take a finite \(\varepsilon\)-net for that set, use convergence at each center, and bound the remainder by \(\varepsilon\). Apply this to the compact closure of \(K\)'s unit-ball image to obtain \(\|(I-P_j)K\|\to0\). Apply it to \(K^*\), and take adjoints, to obtain \(\|K(I-P_j)\|\to0\). Finally,

\[
 K-P_jKP_j=(I-P_j)K+P_jK(I-P_j).
\]

Both terms tend to zero in norm. \(\square\)

<a id="weighted-compact-alternative"></a>

**Lemma 1.2 (compact alternative).** If \(K\) is compact on a Hilbert space and \(A=I+K\) is injective, then \(A\) is surjective and its inverse is bounded.

**Proof.** First there is a constant \(c>0\) such that \(\|Ax\|\ge c\|x\|\). Otherwise choose unit vectors \(x_j\) with \(Ax_j\to0\). Compactness gives a subsequence for which \(Kx_j\) converges. Since \(x_j=Ax_j-Kx_j\), this subsequence converges to a unit vector \(x\), and continuity gives \(Ax=0\), contradicting injectivity. The lower bound also shows that the image under \(A\) of any closed subspace is closed: a convergent sequence \(Ax_j\) makes \(x_j\) Cauchy, and its limit belongs to the subspace.

Suppose \(A\) is not surjective. Put \(H_j=A^jH\), starting with \(H_0=H\). These subspaces are closed by the preceding argument. Each inclusion \(H_{j+1}\subset H_j\) is strict. Indeed equality would give, for every \(x\), an element \(y\) with \(A^jx=A^{j+1}y\); injectivity of \(A^j\) would imply \(x=Ay\), hence surjectivity. Choose a unit vector \(u_j\in H_j\) orthogonal to \(H_{j+1}\). For \(k>j\), both \(Au_j\) and \(Ku_k\) belong to \(H_{j+1}\): the latter follows from \(KA=AK\), since \(K=A-I\). Therefore

\[
 \big(Ku_j-Ku_k,u_j\big)
 =\big(Au_j-u_j-Ku_k,u_j\big)=-1.
\]

Cauchy–Schwarz gives \(\|Ku_j-Ku_k\|\ge1\). This contradicts the existence of a convergent subsequence of \(Ku_j\), and proves surjectivity. The first lower bound gives \(\|A^{-1}\|\le c^{-1}\).

The orthogonal vectors used here require only projection onto a closed Hilbert subspace. For completeness, minimize \(\|x-v\|\) over \(v\) in that subspace. A minimizing sequence is Cauchy by the parallelogram identity applied to its midpoints; completeness gives a minimizer \(v\). Minimality for \(v+tw\), first for real \(t\) and then for purely imaginary \(t\), yields \((x-v,w)=0\). Thus a proper closed inclusion has the nonzero orthogonal difference used above. \(\square\)

<a id="weighted-compact-cutoffs"></a>

For the weighted spaces, let

\[
 \chi_j=1_{\{a>1/j\}}.
\tag{2}
\]

Multiplication by \(\chi_j\) is an orthogonal projection in each \(H_\kappa\). It converges strongly to the identity there by dominated convergence. Consequently the common space
\(\mathcal D_a=\bigcup_j\chi_jH_0\) is dense in every \(H_\kappa\): on each truncated set all the weights in (1) are bounded above and below by positive constants. No positive lower bound for \(a\) on all of \(M\) is required.

<a id="weighted-compact-interpolation"></a>

## 2. Interpolation for one weight

**Lemma 2.1.** Suppose \(L_0\) is bounded on \(H_0\), \(L_2\) is bounded on \(H_2\), and they agree on \(H_0\subset H_2\). Write \(N_l=\|L_l\|\). For every \(0\leq\theta\leq1\), their common restriction has a unique compatible bounded extension to \(H_{2\theta}\), with

\[
 \|L\|_{H_{2\theta}\to H_{2\theta}}
       \leq N_0^{1-\theta}N_2^\theta.
\tag{3}
\]

**Proof.** If either endpoint norm is zero, compatibility and the density of \(H_0\) in \(H_2\) show that both operators vanish, and the conclusion follows. Suppose both are positive. Take \(f,h\in\mathcal D_a\), supported in a common set \(\{a>1/j\}\). For \(0\leq\operatorname{Re}z\leq1\), put

\[
 F(z)=\int_M L_0(a^{-z}f)\,a^z\overline h\,d\mu.
\tag{4}
\]

The logarithm of \(a\) is bounded on these supports. If its absolute value there is at most \(B\), the \(m\)-th coefficient in either exponential series has norm at most \(B^m\|f\|_0/m!\) or \(B^m\|h\|_0/m!\); the derivative series has the corresponding summable bound on each compact set. Therefore \(z\mapsto a^{-z}f\) and \(z\mapsto a^z\overline h\) are norm holomorphic, by their uniformly convergent power series on compact sets of \(z\). The bounded bilinear integral in (4) makes \(F\) holomorphic and continuous on the closed strip. It is bounded there: imaginary powers of \(a\) have modulus one, and real powers on the supports have uniform upper bounds.

On the lower endpoint of the vertical strip, multiplication by \(a^{it}\) is unitary on \(H_0\), so
\(|F(it)|\leq N_0\|f\|_0\|h\|_0\). On the other endpoint use compatibility and the unitary map
\(C:H_2\to H_0\), \(Cu=au\), to write

\[
 F(1+it)=
  \big(C L_2 C^{-1}(a^{-it}f),a^{-it}h\big)_0.
\]

Thus \(|F(1+it)|\leq N_2\|f\|_0\|h\|_0\). Here is the scalar three-lines step. For nonzero \(f,h\), divide \(F(z)\) by
\(\|f\|_0\|h\|_0N_0^{1-z}N_2^z\), using the real logarithms of the positive endpoint norms, to get a bounded holomorphic function \(G\) on the strip with boundary modulus at most one. For \(\delta>0\), the function \(G(z)e^{\delta(z^2-1)}\) has modulus at most one on both vertical boundaries. On the two horizontal boundaries of a rectangle \(0\leq\operatorname{Re}z\leq1\), \(|\operatorname{Im}z|\leq R\), its modulus is at most \(\|G\|_\infty e^{-\delta R^2}\). For all sufficiently large \(R\), this is at most one. The [proved finite-rectangle maximum principle](../providers/analysis/bounded-strips.md#finite-rectangle-maximum) on that rectangle gives \(|G(\theta)|\leq e^{\delta(1-\theta^2)}\). Let \(\delta\downarrow0\). Zero test vectors give the same conclusion immediately. Therefore

\[
 |F(\theta)|\leq
 N_0^{1-\theta}N_2^\theta\|f\|_0\|h\|_0.
\tag{5}
\]

For \(u\in\mathcal D_a\), put \(f=a^\theta u\). Equation (5), tested against the dense space of \(h\)'s, bounds
\(\|a^\theta L_0u\|_0\) by its right side with \(\|f\|_0=\|u\|_{2\theta}\). This proves (3) on \(\mathcal D_a\), and density extends the operator. If \(u\in H_0\), then \(\chi_ju\to u\) in both \(H_0\) and \(H_{2\theta}\). The two operator limits agree because \(H_0\) embeds continuously into \(H_{2\theta}\). This proves compatibility with \(L_0\), and compatibility with \(L_2\) follows in the same way, using \(H_{2\theta}\subset H_2\). \(\square\)

This is an interpolation statement for an arbitrary positive bounded weight. It does not require a frequency decomposition or a power growth condition at infinity.

<a id="weighted-compact-preserved-norm"></a>

## 3. A preserved norm supplies the missing endpoint

The compact extension through the dual weighted space is Hörmander’s argument in [H2, Lemma 14.6.9]. Here the weight is only measurable and the underlying measure space is arbitrary.

**Theorem 3.1.** Let \(T\) be compact on \(H_0\), and suppose

\[
 \|f+Tf\|_1=\|f\|_1\qquad(f\in H_0).
\tag{6}
\]

Then \(T\) extends compatibly to a compact operator on every \(H_\kappa\), \(0\leq\kappa\leq2\). The operator \(I+T\) is a bounded bijection in every one of these spaces, and is unitary in \(H_1\).

**Proof.** Because \(a>0\), (6) implies \(\ker(I+T)=\{0\}\) in \(H_0\). Lemma 1.2 makes \(U=I+T\) a bounded bijection there. Write

\[
 U^{-1}=I+S,\qquad S=-U^{-1}T.
\tag{7}
\]

The operator \(S\) is compact in \(H_0\). Polarizing (6) gives
\((Uf,Ug)_1=(f,g)_1\). Substitute \(g=(I+S)h\), expand, and cancel \((f,h)_1\). The result has a positive sign:

\[
 (Tf,h)_1=(f,Sh)_1\qquad(f,h\in H_0).
\tag{8}
\]

In the unweighted pairing, (8) is \((aTf,h)_0=(af,Sh)_0=(S^*(af),h)_0\) for every \(h\in H_0\). Both compared vectors belong to \(H_0\) because \(a\) is bounded. Testing their difference proves \(aTf=S^*(af)\). The unitary map \(C:H_2\to H_0\), \(Cf=af\), therefore gives the compact extension

\[
 T_2=C^{-1}S^*C.
\tag{9}
\]

It agrees with \(T\) on \(H_0\). Taking the conjugate of (8) with the two variables exchanged gives \((Sf,h)_1=(f,Th)_1\), so likewise
\(S_2=C^{-1}T^*C\) is a compact extension of \(S\). Lemma 1.1 supplies compactness of both adjoints. The identities

\[
 T+S+TS=0,\qquad T+S+ST=0
\tag{10}
\]

hold on \(H_0\) by (7), hence on \(H_2\) by density and boundedness. Apply Lemma 2.1 separately to \(T\) and \(S\). They extend boundedly to every intermediate space. Compatibility, density of \(H_0\), and (10) show that \(I+S\) is a two-sided inverse of \(I+T\) there.

It remains to prove compactness in the intermediate spaces. Lemma 1.1 in each endpoint gives

\[
 \|\chi_jT\chi_j-T\|_{H_l\to H_l}\longrightarrow0,
 \qquad l=0,2.
\tag{11}
\]

Interpolate the difference in (11) to get convergence in every \(H_\kappa\) operator norm. The truncated map \(\chi_jT\chi_j\) is compact on \(H_\kappa\): input truncation maps \(H_\kappa\) boundedly to \(H_0\), the unweighted \(T\) is compact, and output truncation maps \(H_0\) boundedly to \(H_\kappa\). Its compatible extension is exactly that composition. Thus (11) approximates \(T\) by compact operators in each norm, proving compactness. Finally (6) passes from dense \(H_0\) to \(H_1\). Together with bijectivity it says \(I+T\) is unitary there. \(\square\)

<a id="weighted-compact-examples"></a>

## 4. Examples and limits of the hypothesis

**Example 4.1.** On \(M=(0,1)\) take Lebesgue measure and \(a(x)=x\). The vector \(e(x)=\sqrt2\) has \(H_1\) norm one. For real \(\phi\), define on \(H_0\)

\[
 Tf=(e^{i\phi}-1)(f,e)_1e.
\tag{12}
\]

The functional \((f,e)_1\) is bounded on \(H_0\), since \(ae\in H_0\). This finite-rank operator multiplies the \(H_1\)-orthogonal component along \(e\) by \(e^{i\phi}-1\), so \(I+T\) preserves the \(H_1\) norm. Theorem 3.1 applies. The same functional is bounded on \(H_\kappa\) exactly as needed here, because its squared dual norm is
\(2\int_0^1x^{2-\kappa}dx=2/(3-\kappa)\) for \(0\leq\kappa\leq2\).

**Example 4.2.** Compactness in \(H_0\) alone does not give a bounded weighted extension. Keep \(a(x)=x\) and put \(Tf=(\int_0^1f(x)dx)1\). This has rank one on \(H_0\), but the functional is unbounded on \(H_2\). Indeed, for
\(f_\delta(x)=x^{-2}1_{(\delta,1)}(x)\), both
\(\|f_\delta\|_{H_2}^2\) and \(\int f_\delta\) equal \(\delta^{-1}-1\). Thus the integral divided by the norm is \(\sqrt{\delta^{-1}-1}\), which diverges. The output vector \(1\) has fixed nonzero \(H_2\) norm \(1/\sqrt3\), so these same inputs also make the operator-norm ratio diverge. The preserved norm assumption (6) is what supplies the endpoint in (9).

### Use the conclusion

Compare the rank-one example that preserves the weighted norm with the counterexample that is unbounded on the weighted space. Check consistency of the endpoint extensions before using interpolation.

<a id="weighted-compact-exercises"></a>

## 5. Exercises and checked solutions

**Exercise 5.1 (foundation).** For \(a(x)=x\) on \((0,1)\), determine exactly when \(x^{-r}\) belongs to \(H_\kappa\). Give an element of \(H_2\) outside \(H_0\).

**Exercise 5.2 (foundation).** Verify (8) when \(H_0=\mathbb C\), \(a\) is constant, and \(U=e^{i\phi}\). Explain why a minus sign on its right would be incorrect.

**Exercise 5.3 (intermediate).** Let \(H=\ell^2\) and \(P_j\) truncate after coordinate \(j\). Show that \(P_j\to I\) strongly but \(\|P_j-I\|=1\). For \(Ke_m=m^{-1}e_m\), compute \(\|P_jKP_j-K\|\).

**Exercise 5.4 (intermediate).** For the rank-one operator in (12), compute its exact operator norm on \(H_\kappa\), \(0\leq\kappa\leq2\), and verify its endpoint interpolation bound at \(\kappa=1\).

**Exercise 5.5 (advanced).** Suppose compatible operators on \(H_0,H_2\) are compact on both endpoints. Use Lemma 2.1 and the cutoffs \(\chi_j\) to prove compactness on all \(H_\kappa\), without assuming (6). Explain which part of Theorem 3.1 still needs (6).

<a id="weighted-compact-solutions"></a>

**Solution 5.1.** The squared norm is \(\int_0^1x^{\kappa-2r}dx\), which is finite precisely when \(\kappa-2r>-1\), or \(r<(\kappa+1)/2\). Equality gives logarithmic divergence. For instance \(x^{-1}\in H_2\) and \(x^{-1}\notin H_0\).

**Solution 5.2.** Here \(T=e^{i\phi}-1\) and \(S=e^{-i\phi}-1\). Thus
\((Tf,h)_1=a(e^{i\phi}-1)f\overline h=(f,Sh)_1\). Conjugation of \(S\), because it occurs in the second variable, gives \(e^{i\phi}-1\). A minus sign would give its negative. For \(\phi=\pi\) both scalars are \(-2\), making the incorrect sign especially visible.

**Solution 5.3.** Every \(\ell^2\) tail has norm tending to zero, so the convergence is strong. But \((I-P_j)e_{j+1}=e_{j+1}\), giving norm one. The diagonal difference is zero for \(m\leq j\) and equals \(-m^{-1}\) thereafter. Its norm is \(1/(j+1)\), which tends to zero. The diagonal \(K\) is compact because those finite-rank truncations converge in norm.

**Solution 5.4.** The output vector has squared norm
\(\|e\|_\kappa^2=2/(\kappa+1)\). The functional has squared dual norm \(2/(3-\kappa)\), as computed above. A rank-one map has norm equal to the product of its vector and functional norms: Cauchy–Schwarz gives the upper bound and a scalar multiple of the representing vector gives equality. Consequently

\[
 \|T\|_\kappa=
 \frac{2|e^{i\phi}-1|}{\sqrt{(\kappa+1)(3-\kappa)}}.
\]

Both endpoint norms equal \(2|e^{i\phi}-1|/\sqrt3\); the middle norm is \(|e^{i\phi}-1|\), below their geometric mean. If \(\phi\) is a multiple of \(2\pi\), all these norms are zero.

**Solution 5.5.** Lemma 1.1 gives endpoint norm convergence of \(\chi_jL\chi_j\to L\). Lemma 2.1 applies to their differences, so the convergence holds in every intermediate operator norm. Each truncated map is compact there by the input/output composition through \(H_0\) used in Theorem 3.1. Norm limits are compact. Thus the interpolation of compactness itself does not need (6). The preserved norm is needed to construct the second endpoint from the first, to force initial injectivity, and to obtain unitarity in the middle space.

## References

- [Measure and complete function spaces](../providers/analysis/finite-derivative-l2.md#complete-function-spaces), for arbitrary measure spaces.
- [Elementary Hilbert tools](../providers/analysis/finite-trace-ideals.md#elementary-hilbert-tools), for arbitrary Hilbert spaces.
- [Finite-dimensional and metric compactness](../providers/analysis/compact-fredholm-families.md#fredholm-finite-tools).
- [Bounded strips and the three-lines inequality](../providers/analysis/bounded-strips.md#three-lines), with both boundary constants and the finite-rectangle proof.

- [H2] Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, reprint of the 1983 edition, Springer, 2005, Lemma 14.6.9, pp. 262–263. ISBN 978-3-540-26964-9. [Edition information](https://doi.org/10.1007/b138375).
