# Supported sources, restricted solutions and normal recovery

These proofs connect the two-weight spaces to the higher-order Cauchy equation. They keep support, restriction, intrinsic derivatives and actual boundary traces distinct. The support and duality arguments develop the existing AN-03 bridge by Claude Opus 5.5 (Anthropic), with Codex editorial contributions, *Totally characteristic operators on the half space*, Proposition 10.2(a,b) and PS6–PS11. That source is CC0. This selected real-order treatment and its connecting proofs are by GPT-6 Astra (OpenAI), Ultra, 5 October 2026, also CC0. The linked two-weight/trace component retains its separate GFDL 1.2 licence.

The mathematical antecedent is Hörmander III, approved 2007 eBook ISBN 978-3-540-49938-1, Appendix B.2, especially B.2.1, B.2.3–B.2.4, B.2.6–B.2.9. The complete used proofs follow. The exact programme bindings are in the accompanying proof map.

## H1. The original spaces and their quotient topology

Write \(z=(t,x)\in\mathbb R\times\mathbb R^d\), \(\zeta=(\tau,\xi)\), \(h=\langle\xi\rangle\), \(R=\langle(\tau,\xi)\rangle\). Let \(H^{(r,q)}\) have norm
\[
\|U\|_{(r,q)}^2=(2\pi)^{-(d+1)}\int R^{2r}h^{2q}|\widehat U|^2\,d\tau\,d\xi.
\tag{HS1}
\]
All indices are real; fixed finite-dimensional Hermitian coefficients are allowed. [The multiplier and Hilbert proof, Sections2–4](two-weight-hilbert-spaces-and-traces.md) gives these as complete Hilbert spaces continuously embedded in \(\mathcal S'\), with dense Schwartz vectors and exact smooth Fourier multiplier domains. Coordinate permutation puts the normal coordinate first without altering any constant.

Let \(r^+\) restrict to \(t>0\). The dot space \(\dot H^{(r,q)}\) consists of whole-space members supported in \(t\geq0\), with their whole-space norm. The bar space \(\overline H^{(r,q)}=r^+H^{(r,q)}\) has quotient norm \(\inf_{r^+U=u}\|U\|_{(r,q)}\). The kernel of restriction is the subspace supported in \(t\leq0\). Both support subspaces are closed: norm convergence implies distributional convergence on every compact smooth test, and preserves vanishing on the required open side.

Here is the full quotient-completeness argument. For a closed subspace \(M\) of a Banach space \(X\), approximate each coset infimum to prove the triangle inequality; homogeneity is immediate, and zero norm is exactly membership in \(\overline M=M\). The quotient map has norm at most one. From a Cauchy sequence \(z_j\) of cosets select a subsequence with successive quotient differences less than \(2^{-j}\). Choose representatives \(h_j\) of those differences with \(\|h_j\|<2^{1-j}\), and one representative \(x_1\) of the first coset. The norm-summable series \(x_1+\sum h_j\) converges by completeness; its partial sums represent the subsequence, so the subsequence converges in the quotient. The original Cauchy sequence has the same limit by the triangle inequality. This proves completeness, including both zero and full subspaces, without assuming nearest representatives.

In the Hilbert case a nearest representative does exist. For any closed affine coset, let its distance to zero be \(a\). A sequence with norms tending to \(a\) is Cauchy because
\(\|v_j-v_k\|^2\leq2\|v_j\|^2+2\|v_k\|^2-4a^2\), by the parallelogram identity and the midpoint belonging to the same coset. Its limit \(v\) minimizes the norm. Minimizing \(\|v+sw\|^2\) for real and purely imaginary \(s\), for \(w\in M\), gives \(v\perp M\). This also gives uniqueness. Subtracting \(v\) from the original representative gives the orthogonal projection onto \(M\), a linear contraction by orthogonality and Pythagoras. Thus the quotient is isometric to the closed orthogonal complement. These facts will justify both antidual norms below.

The intrinsic \(D_tu\) on a bar space is obtained by differentiating any extension and then restricting. Differences of extensions have backward support, which differentiation preserves, so this is well defined. It does not mean the derivative of a zero extension.

## H2. Multiplication, density and every mixed embedding

For all real \(r,q\), compact smooth coefficient multiplication is bounded on \(H^{(r,q)}\). Indeed \(\langle\zeta\rangle\leq\sqrt2\langle\eta\rangle\langle\zeta-\eta\rangle\), by expanding squares and using \(2|a||b|\leq|a|^2+|b|^2\). Interchanging \(\zeta,\eta\) and applying this also to tangential coordinates proves
\[
\frac{R(\zeta)^rh(\xi)^q}{R(\eta)^rh(\eta')^q}
 \leq 2^{(|r|+|q|)/2}\langle\zeta-\eta\rangle^{|r|+|q|}.
\tag{HS2}
\]
The Fourier product formula and the Schwartz transform of a compact smooth coefficient bound the weighted output by convolution of the weighted input with an L1 function. The complete [Young inequality](../20261005-cauchy-foundations/integration-and-duality.md) gives the L2 bound, including the Fourier coefficient. The same proof in only the normal or tangential Fourier variable covers smooth compact cutoffs in that variable, constant in the others. Multiplication preserves supports; taking infima over extensions gives the bar bound. Finite matrices follow by entries and the finite sum inequality. Hence all compactly localized smooth coefficients and every needed cutoff are legitimate on these spaces.

The dot test space \(C_c^\infty(t>0)\) is dense at every real pair. Translate a dot vector forward by \(\epsilon>0\); the Fourier phase tends to one and has modulus one, so dominated convergence gives norm convergence. Mollify with a smooth integral-one kernel supported in a ball of radius less than \(\epsilon/2\). Its Fourier multiplier is uniformly bounded and tends to one, so the weighted norm again converges. For each fixed mollification radius it decreases faster than any polynomial, and the resulting vector belongs to every ordinary Sobolev order and has support separated from the boundary. Multiply it by \(\theta(z/L)\), with \(\theta=1\) near zero and compactly supported. At an integer \(k\geq\max(r,r+q,0)\), the finite Leibniz formula shows convergence in ordinary \(H^k\): the term with no derivative on the cutoff tends by dominated convergence, while the terms with a positive cutoff derivative have a factor \(L^{-j}\) times an L2 derivative of the mollified vector. Ordinary \(H^k\) bounds the mixed norm since \(R^rh^q\leq R^{\max(r,r+q)}\). Choose the three parameters successively to make the error less than \(1/j\). This proves density, even for boundary-supported distributions at their allowed negative orders. Reflection gives the corresponding negative-side density. Restrictions of whole-space Schwartz approximants are dense in the bar space.

The exact embedding criterion, when \(d\geq1\), is
\[
H^{(r,q)}\hookrightarrow H^{(a,b)},\quad
\dot H^{(r,q)}\hookrightarrow\dot H^{(a,b)},\quad
\overline H^{(r,q)}\hookrightarrow\overline H^{(a,b)}
\quad\Longleftrightarrow\quad a\leq r,\quad a+b\leq r+q.
\tag{HS3}
\]
For sufficiency the weight ratio is \((R/h)^{a-r}h^{a+b-r-q}\leq1\); use the same support or infimize over extensions. Necessity will be completed after the duality proof H3. If \(d=0\), \(h=1\) and just \(a\leq r\) remains.

## H3. The full supported/restricted antiduals

The whole-space antidual of \(H^{(r,q)}\), under the pairing linear in its first argument, is isometrically \(H^{(-r,-q)}\), with Fourier pairing \((2\pi)^{-(d+1)}\int\widehat U\overline{\widehat V}\). Cauchy–Schwarz proves boundedness. Every functional is represented by applying the complete [Hilbert representation proof T1](../20261004-free-canonical-composition/compactness-and-essential-norms.md) after the onto multiplier isometry of the companion. The norm is attained in the corresponding direction: for fixed \(U\), the representing opposite-order vector with transform \(R^{2r}h^{2q}\widehat U\) has norm \(\|U\|_{(r,q)}\) and its pairing with \(U\) is \(\|U\|_{(r,q)}^2\).

If \(V\) vanishes on \(t>0\), it pairs to zero with each compact test there, and therefore with every dot vector by H2's density. Conversely, annihilating every dot vector implies vanishing on those compact tests. The annihilator of the dot subspace is exactly the kernel of restriction in the opposite-order space. Extend a bounded functional on the dot subspace to the whole Hilbert space with the same norm by composing with its orthogonal projection, constructed in H1. Whole-space representation gives a vector \(V\), unique modulo that annihilator. The quotient norm is at most the functional norm by this norm-preserving representative, and at least it by Cauchy–Schwarz and infimizing. Thus
\[
(\dot H^{(r,q)})^*=\overline H^{(-r,-q)}
\quad\text{isometrically}.
\tag{HS4}
\]
Conversely, a functional on the latter quotient lifts to a whole-space functional annihilating the kernel. Its representing vector belongs to the original dot space: a vector outside that closed subspace has a nonzero orthogonal component, whose representing opposite-order functional annihilates the subspace but not that vector, contradicting the annihilation requirement. This is the full double-annihilator argument. It proves the reverse antidual identity and its norm as well. On smooth vectors Plancherel identifies the form with the actual half-space integral. No arbitrary supported extension of a bar vector was used.

To complete (HS3), fix nonzero \(\chi\in C_c^\infty(t>0)\). For \(\chi_L=e^{iLt}\chi\), weighted Fourier translation and (HS2) give
\(\|\chi_L\|_{(r,q)}\asymp L^r\) as \(L\to\infty\), with a positive finite limit after division by \(L^r\). For \(\chi_L=e^{iLx_1}\chi\), the order is \(L^{r+q}\). To justify the limits for every sign of the orders, translate the Fourier integration variable, use the pointwise ratios to the central weight, and dominate by \(C\langle\eta\rangle^{2(|r|+|q|)}|\widehat\chi(\eta)|^2\) from (HS2). Dot norms are these same norms. For bar norms the whole extension gives the upper bound; pairing \(\chi_L\) with itself via (HS4) gives the lower bound \(\|\chi\|_2^2/\|\chi_L\|_{(-r,-q)}\), with the matching power. A continuous embedding consequently forces \(a\leq r\) in the first sequence and \(a+b\leq r+q\) in the second. This proves necessity without assuming that the minimizing extension is the given compact test.

## H4. One-sided multipliers, including their exact support

For real \(a\), set
\[
J_\pm^a=(h(D_x)\pm iD_t)^a,\qquad
(h\pm i\tau)^a=\exp\!\left(a\left(\tfrac12\log(h^2+\tau^2)
                  \pm i\arctan(\tau/h)\right)\right).
\tag{HS5}
\]
The branch is defined on the right half-plane. Write \(A(y)=\int_0^y(1+s^2)^{-1}ds\). The two functions \(e^{iA(y)}\) and \((1+iy)/(1+y^2)^{1/2}\) have the same logarithmic derivative \(i/(1+y^2)\) and value one at zero; their quotient has derivative zero and is therefore one. This proves the polar identity used in (HS5) directly. Its derivative and the logarithm derivative give \(\partial_\tau(h+i\tau)^a=ia(h+i\tau)^{a-1}\), with the conjugate formula for the minus sign. All further derivatives are polynomially bounded, as are those of the reciprocal: repeated product and chain rules use only powers of \((h\pm i\tau)^{-1}\), derivatives of \(h\), and fixed real constants. Here \(|h\pm i\tau|=R\geq1\). Leibniz therefore gives continuous Schwartz multipliers and their tempered-distribution transposes, inverse to each other. Their moduli are exactly \(R^a\), so they are onto isometries \(H^{(r,q)}\to H^{(r-a,q)}\).

The support proof only needs positive real gamma parameters. For \(c>0\), let \(\Gamma(c)=\int_0^\infty s^{c-1}e^{-s}ds\). The integral is finite and positive: near zero use \(c>0\); on the tail exponential decay beats a fixed power. Substitution and one integration by parts give \(\Gamma(c+1)=c\Gamma(c)\). For fixed \(h\geq1\), let \(F(\tau)=\int_0^\infty s^{c-1}e^{-(h+i\tau)s}ds\). Dominated differentiation and integration of the derivative of \(s^ce^{-(h+i\tau)s}\) give
\(F'=-icF/(h+i\tau)\), with \(F(0)=h^{-c}\Gamma(c)\). The derivative formula just proved makes \((h+i\tau)^cF\) constant. Therefore
\[
(h+i\tau)^{-c}=\Gamma(c)^{-1}
 \int_0^\infty s^{c-1}e^{-sh}e^{-is\tau}\,ds.
\tag{HS6}
\]
This proves the actual real-order Laplace identity without requiring a complex-parameter gamma theorem.

Let \(E_s=\mathcal F_x^{-1}(e^{-sh(\xi)})\). The inverse full Fourier kernel of (HS6) is
\[
K_{-c}(t,x)=\Gamma(c)^{-1}
\int_0^\infty s^{c-1}\delta(t-s)E_s(x)\,ds.
\tag{HS7}
\]
The tangential inverse Fourier coefficient is \((2\pi)^{-d}\); inverse transformation of \(e^{-is\tau}\) is \(\delta(t-s)\), without another factor. On a Schwartz test, express the spatial pairing by its spatial Fourier transform. Its integral is bounded by a fixed Schwartz seminorm times \(e^{-s}\), uniformly for small \(s\) as well. Thus the tested integral is bounded by \(C\int_0^\infty s^{c-1}e^{-s}ds\), and defines a tempered distribution. Fubini against a full Schwartz test verifies its Fourier transform is (HS6). Its support lies in \(t\geq0\). For a Schwartz input supported in \(t\geq0\), the same integral gives \(\int_0^\infty s^{c-1}e^{-sh(D_x)}u(t-s,x)ds/\Gamma(c)\); it is zero when \(t<0\). Absolute tested convergence justifies this equality. For arbitrary real \(a\), choose an integer \(k>a\) and use
\(J_+^a=(h(D_x)+\partial_t)^kJ_+^{-(k-a)}\), taking \(k\geq0\).
Each term of the finite power preserves normal support; tangential multipliers act at fixed time and normal derivatives preserve support.

For each dot vector, H2 supplies supported compact smooth approximants in its original mixed norm. The full multiplier is continuous into the corresponding target mixed space, hence into distributions. Support is closed under this convergence. Therefore both \(J_+^a\) and its inverse preserve the positive-side subspaces at every pair of real indices. Reflection \(t\mapsto-t\), a literal Fourier isometry, proves that both \(J_-^a\) and its inverse preserve the negative-side subspaces. Tangential weights preserve either side and commute with these operations. We have proved precisely the support statements needed for every Hilbert-space quotient below; no unproved support inference from multiplier size is involved.

## H5. Exact quotient isometries and the common minimal extension

The full isometry \(J_-^rh(D_x)^q:H^{(r,q)}\to L^2\) maps the kernel of positive restriction onto the L2 functions supported in \(t\leq0\), by H4 and the inverse. Quotienting gives an onto isometry to \(L^2(t>0)\). Likewise \(J_+^rh(D_x)^q\) maps the positive dot space onto the positive-supported L2 space. Explicitly,
\[
J_+^rh^q:\dot H^{(r,q)}\simeq L^2(t\geq0),\qquad
J_-^rh^q:\overline H^{(r,q)}\simeq L^2(t>0).
\tag{HS8}
\]
The L2 quotient identification is obtained by restricting an L2 function and extending the restriction by zero; its disjoint negative and positive squared norms add, so the zero extension has the minimum norm. No boundary mass exists in L2.

In particular the minimal extension of a bar vector is
\[
g=J_-^ru\in L^2(\mathbb R_+;H^q_x),\qquad
E_ru=J_-^{-r}(H(t)g),\qquad
r^+E_ru=u,\quad \|E_ru\|_{(r,q)}=\|u\|_{\overline H^{(r,q)}}.
\tag{HS9}
\]
The vector-valued L2 identification here follows by applying tangential Plancherel to the full norm and using [Fubini and the complete Bochner Hilbert construction](../20261005-cauchy-foundations/integration-and-duality.md). The formula agrees with zero extension after the full isometry, since tangential weights commute with normal restriction and extension. It is independent of \(q\): if the same distribution belongs at several tangential orders, its images \(g\) agree as distributions and therefore as almost-everywhere Hilbert-valued functions at a common lower order. Their zero extensions agree as distributions as well. The same \(E_r\) works for the intersection of all tangential orders. It generally occupies both sides of the boundary.

## H6. The normal step, complete integer jets and supported sources

At every real pair the exact characterization is
\[
\begin{gathered}
u\in\overline H^{(r,q)}\quad\Longleftrightarrow\quad
u\in\overline H^{(r-1,q+1)},\quad D_tu\in\overline H^{(r-1,q)},\\
\tfrac12\|u\|_{\overline H^{(r,q)}}^2
\leq\|u\|_{\overline H^{(r-1,q+1)}}^2+
       \|D_tu\|_{\overline H^{(r-1,q)}}^2
\leq\|u\|_{\overline H^{(r,q)}}^2.
\end{gathered}
\tag{HS10}
\]
For necessity, any common whole-space extension has the exact squared Fourier identity \(R^2=h^2+\tau^2\); the sum of the two infima is at most that common extension norm, and then infimize. For sufficiency apply \(J_-^{r-1}h^q\) to any extension of \(u\) and restrict. Call the result \(V\). The first hypothesis and (HS8) give \(hV\in L^2(t>0)\); the second gives \(D_tV\in L^2(t>0)\). All multipliers commute on the quotient because they preserve its kernel. Thus \(J_-^rh^qu=hV-iD_tV\) is L2 there. Applying the inverse quotient map in (HS8) gives membership in the desired bar space; the squared triangle inequality bounds its norm by twice the two input squared norms. To see that this inverse produces the original \(u\), compare any two whole-space extensions after the invertible multiplier: their difference vanishes on \(t>0\), so its inverse image has the same backward support by H4. This completes the half-space step, without assuming a boundary trace.

For an integer \(k\geq0\) it follows inductively that
\[
\overline H^{(k,q)}=
\{u:D_t^ju\in L^2(\mathbb R_+;H^{q+k-j}_x),\ 0\leq j\leq k\},
\qquad
\|u\|_{\overline H^{(k,q)}}^2\asymp
\sum_{j=0}^k\|D_t^ju\|_{L^2H^{q+k-j}}^2.
\tag{HS11}
\]
The case \(k=0\) is the actual L2 quotient of H5. At the induction step the jet conditions put \(u\) in the first space of (HS10) on its right and \(D_tu\) in the second, using the full preceding jet characterization; (HS10) gives membership and the upper bound by that finite jet sum. In the converse direction expand \((\tau^2+h^2)^k\) for any whole extension; its binomial coefficients bound all the required jet norms, and taking the infimum proves the lower bound. Whole-space and dot versions use the same Fourier identity with ambient derivatives. These are distinct from intrinsic derivatives of a bar vector extended by zero.

For a supported source \(f\in\dot H^{(r,q)}\), put \(v=J_+^{-1}f\). Then
\[
f=f_0+D_tf_n,\qquad f_0=h(D_x)v\in\dot H^{(r+1,q-1)},
\quad f_n=iv\in\dot H^{(r+1,q)}.
\tag{HS12}
\]
The identity is exactly \((h+iD_t)v=f\); H4 gives both supports. The ratio of each component's target weight and multiplier to the source weight has modulus one, since \(|h+i\tau|=R\). Hence each component norm equals the original source norm. This keeps all boundary distributions present; restricting the identity to the open half-space is a different operation.

## H7. Tangential operator families on every integer normal scale

Let \(B(t)=b(t,x,D_x)\) have spatial order \(l\), with every time derivative uniformly in that ordinary spatial class. Then, for every integer \(k\) and real \(q\),
\[
B:H^{(k,q)}\to H^{(k,q-l)},\qquad
B:\dot H^{(k,q)}\to\dot H^{(k,q-l)},\qquad
B:\overline H^{(k,q)}\to\overline H^{(k,q-l)}
\tag{HS13}
\]
continuously, with constants from finitely many time and symbol seminorms. For \(k\geq0\), use the whole-space integer jet identity (HS11). Each \(\partial_t^j(Bu)\) is the sum of \(\binom ji(\partial_t^{j-i}B)\partial_t^iu\), \(0\leq i\leq j\). The proved [global spatial Sobolev map G1](../20261005-cauchy-foundations/sharp-lower-bound.md) sends that input into \(H^{q+k-i-l}_x\), which embeds in the required \(H^{q+k-j-l}_x\). Integrating and summing proves the bound. The same finite-dimensional proof covers rectangular matrices.

For \(k=-a<0\), take the actual tangential adjoint. Its time derivatives satisfy the same order bounds by ordinary composition and adjoints. The positive-order result maps \(B^*:H^{(a,l-q)}\to H^{(a,-q)}\). Whole-space antiduality H3 then gives exactly the negative-order map in (HS13). Agreement with the distributional operator follows by Schwartz density and its continuous transpose construction, proved for the joint time/spatial tests in [spacetime composition M1](../20261005-restored-first-order-cauchy/spacetime-symbol-composition.md). The operator acts at fixed time, so it preserves either normal support: a test with time support on one side has its transpose on that same side. Thus its whole-space map restricts to dot spaces and descends to bar quotients by taking infima. No fractional normal-order interpolation is assumed in (HS13); all tangential orders are real.

## H8. Differential recovery with all real indices

On a collar let \(P=D_t^\mu+\sum_{|\alpha|\leq\mu,\alpha_t<\mu}a_\alpha D^\alpha\), with smooth coefficients and \(\mu\geq1\). For local restricted spaces suppose \(u\in\overline H^{(r_1,q_1)}_{\rm loc}\) and \(Pu\in\overline H^{(r_2-\mu,q_2)}_{\rm loc}\). Then
\[
u\in\overline H^{(a,b)}_{\rm loc}\quad\text{if}\quad
a\leq r_2,\quad a+b\leq r_1+q_1,\quad a+b\leq r_2+q_2.
\tag{HS14}
\]
There is no extra \(a\leq r_1\) restriction. To prove the first gain assume \(a\leq r_1+1\), take a compact collar cutoff \(\chi\), and let \(v=\chi u\). A derivative with \(j\) normal and \(l\) tangential differentiations maps \((r,q)\) to \((r-j,q-l)\), directly from its bounded Fourier ratio. H2 supplies coefficient multiplication and embeddings. Thus \(\chi Pu\in\overline H^{(a-\mu,b)}\). Each term of \([P,\chi]u\) has total order at most \(\mu-1\), so its normal regularity is at least \(r_1-\mu+1\geq a-\mu\), and its total regularity is at least \(r_1+q_1-\mu+1\geq a+b-\mu\). A larger cutoff equal to one near \(\operatorname{supp}\chi\) makes every coefficient compactly supported. Hence \(Pv\) has the same target membership.

Every lower-normal term of \(Pv\) has normal regularity at least \(r_1-\mu+1\) and total regularity at least \(r_1+q_1-\mu\). Subtracting them gives \(D_t^\mu v\in\overline H^{(a-\mu,b)}\). Descend through \(j=\mu-1,\ldots,0\): the original membership gives \(D_t^jv\in\overline H^{(a-j-1,b+1)}\) by the same two inequalities, while the next derivative is already in \(\overline H^{(a-j-1,b)}\). The actual normal step (HS10) gives \(D_t^jv\in\overline H^{(a-j,b)}\). At \(j=0\) this proves the desired first gain.

If \(a\leq r_1\), direct embedding proves the result. Otherwise put \(S=a+b\), lower the initial tangential order to \(S-r_1\), and repeat the first gain at \(a_j=\min(a,r_1+j)\), \(b_j=S-a_j\). Each increase is at most one and satisfies \(a_j\leq r_2\), \(S\leq r_2+q_2\). After \(\lceil a-r_1\rceil\) steps the target is reached. Choose finitely many nested cutoffs in advance; all conclusions hold on the final requested patch. The same proof holds in whole-space local charts, using the exact whole-space normal identity instead of its quotient version. For an invertible smooth leading matrix, multiply on the left by its smooth inverse and use H2; the proof keeps matrix order throughout. For order zero and invertible coefficient, the source membership and embedding suffice directly.

Boundary traces, including their strict threshold, actual continuity and extension independence, are the complete [Section9 proof in the two-weight companion](two-weight-hilbert-spaces-and-traces.md). Together these results supply the half-space analytic inputs for U031. The compressed boundary-wavefront calculus and the complete higher-order receiving lesson require their own additional review.
