# Smooth pullback and the Fourier normal condition

*Programme proof text: AN-03 course-writing task, OpenAI Codex. CC0 1.0. Selection and prerequisite connections: GPT-6 Astra (OpenAI), Ultra.*

These are Sections 18.1–18.5 of the programme reading *Detecting regularity without choosing coordinates*. They construct arbitrary noncharacteristic smooth pullbacks, prove their Fourier bound, and identify diffeomorphism and submersion cases. Section numbers and formula labels retain their source meanings within this reading.

The earlier proofs used here are all supplied in this reader. The [Schwartz and Fourier foundation](schwartz-fourier-foundations-U017.md), F1–F5, proves Fourier inversion, finite seminorm estimates and the full Gaussian mass and transform in WF13. [Order, positivity and distributional limits](../../src/order-positivity-and-limits.md), Section 1, proves compact finite order. [Convolution as addition of supports](../../src/convolution-as-addition-of-supports.md), B0–B2 and Theorem 1.1, proves partitions, distributional gluing, smooth parameter pairings, tensor products and their exact support. [Tempered growth and spectral cutoffs](../../src/tempered-growth-and-spectral-cutoffs.md), Lemma 2.1, supplies Schwartz convolution and differentiation of its pairings. The [scalar foundation](metric-foundation-bridges.md), Sections 12–13, gives compactness, finite smooth partitions and the product, chain and segment-integral rules. The [integration foundation](banach-foundation-bridges.md), Sections 15–16, gives absolute integration, Fubini, convergence and linear substitution. Every reference below to the integration, Fourier or calculus chapters means these supplied proofs.

For coordinate substitutions, [Zero hypersurfaces as curvature measures](../../src/zero-hypersurfaces-as-curvature-measures.md), Lemma 3.0, proves the complete nonlinear change-of-variables formula with its determinant. [Regular level sets and transverse convolution](../../src/regular-level-sets-and-transverse-convolution.md), Lemmas 0.1–0.2, proves the smooth inverse and coordinate-completion theorems by a convergent iteration. These are the inverse and measure substitution results used in Sections 18.3 and 18.5. Smooth pullbacks by a diffeomorphism are given by the displayed test formula WF5: the product and chain rules prove continuity, the determinant chain rule proves composition, and Lemma 3.0 identifies it with composition of smooth functions. No general distributional pullback is assumed before WF12 constructs it.

### 18.1. The original Fourier estimate and every cutoff

Use the original convention

\[
\widehat f(\xi)=\int_{\mathbb R^d}e^{-ix\cdot\xi}f(x)\,dx,\qquad
f(x)=(2\pi)^{-d}\int_{\mathbb R^d}e^{ix\cdot\xi}\widehat f(\xi)\,d\xi.
\tag{WF1}
\]

For a compactly supported distribution \(v\), its Fourier transform is \(v(e^{-ix\cdot\xi})\), with a compact smooth cutoff equal to one on its support inserted in that pairing. The full finite-order test estimate and product rule give
\(|\widehat v(\xi)|\leq C(1+|\xi|)^m\) for some actual integer \(m\). Every frequency derivative has the same type of estimate, with its original multiplier \((-ix)^\alpha\) in the test. The estimate keeps the derivatives of the inserted support cutoff. A compact smooth test has rapidly decreasing transform by repeated integration by parts with \(1-\Delta_x\), whose full multiplier is \(1+|\xi|^2\). These facts follow on the original coordinates.

For \(b\in C_c^\infty\), inverse Fourier transformation of the test and the finite-order bound justify

\[
\widehat{bv}(\xi)=(2\pi)^{-d}
       \int_{\mathbb R^d}\widehat b(\xi-\eta)\widehat v(\eta)\,d\eta.
\tag{WF2}
\]

The integral is absolutely convergent: take the Schwartz decrease of \(\widehat b\) beyond the original polynomial order plus \(d\). It also converges in every test seminorm needed in the pairing, so the distribution can be passed through the integral. No Fourier multiplier constant is suppressed.

Suppose \(\widehat v\) decreases rapidly in an open cone \(V\), and the angular closure of a smaller cone \(W\) lies in \(V\). For \(\xi\in W,\eta\notin V\), angular separation gives
\(|\xi-\eta|\geq c(|\xi|+|\eta|)\) for some \(c>0\). To prove this, restrict to \(|\xi|+|\eta|=1\); the two closed angular sets are disjoint, so the continuous difference has a positive minimum. Scaling restores the original lengths. Split WF2 at \(\eta\in V\). On that region both original transforms decrease rapidly, and
\(1+|\xi|\leq(1+|\xi-\eta|)(1+|\eta|)\). Taking their exponents larger than \(N+d+1\) gives the requested output power \((1+|\xi|)^{-N}\) and an integrable residual power in \(\eta\). On the complement, take the cutoff exponent larger than \(N+m+d+1\); angular separation beats the full polynomial input bound. Thus multiplication preserves rapid decrease on \(W\).

Consequently the definition of \(\operatorname{WF}(u)\) using a cutoff equal to one near the original base point is unchanged if the cutoff is only nonzero there: multiply by its actual smooth reciprocal on a smaller neighborhood and use WF2. It is local. Its complement is open in the nonzero cotangent variables by the same smaller-neighborhood and smaller-cone construction, so the wavefront set is closed and conic. If all directions are regular over a compactly localized neighborhood, a finite cover of the original unit sphere and the cutoff estimate give rapid decrease everywhere. WF1 then proves smoothness with every derivative. Conversely compactly localized smooth functions have that decrease, so absence of all wavefront directions is exactly smoothness.

### 18.2. A full nonstationary integral bound

Let \(K\) be a fixed compact coordinate set and
\(I(\xi,\eta)=\int a(x)e^{i\Phi(x,\xi,\eta)}dx\), with \(a\) smooth and supported in \(K\). In each application below the original phase is linear in the frequency parameters, and its coordinate derivatives on \(K\) satisfy
\(|\partial_x^\alpha\Phi|\leq C_\alpha(|\xi|+|\eta|)\). Suppose its actual gradient satisfies
\(|\nabla_x\Phi|\geq c(|\xi|+|\eta|)\) on \(K\), for \(|\xi|+|\eta|\geq1\). Retain the entire operators

\[
\begin{aligned}
L&=\sum_j\frac{\partial_{x_j}\Phi}{i|\nabla_x\Phi|^2}\partial_{x_j},
&Le^{i\Phi}&=e^{i\Phi},\\
L^ta&=-\sum_j\partial_{x_j}
       \left(\frac{\partial_{x_j}\Phi}{i|\nabla_x\Phi|^2}a\right),
&I(\xi,\eta)&=\int (L^t)^Na(x)e^{i\Phi(x,\xi,\eta)}dx .
\end{aligned}
\tag{WF3}
\]

The superscript \(t\) denotes the bilinear integration transpose, not a conjugate adjoint. Boundary terms vanish because the original amplitude is compactly supported. Every derivative of each coefficient of \(L\) is bounded by \(C_\alpha(|\xi|+|\eta|)^{-1}\): the numerator has one frequency power, the denominator has two, and each differentiated quotient has the same net power, with the positive lower gradient bound retained. The full iterated product and chain rules in the calculus chapter give a finite sum at every \(N\), keeping every differentiated coefficient and amplitude. They therefore prove

\[
|I(\xi,\eta)|\leq C_N(1+|\xi|+|\eta|)^{-N}
                \max_{|\alpha|\leq N}\|\partial^\alpha a\|_\infty
\tag{WF4}
\]

on the separated region, enlarging \(C_N\) for bounded frequencies. Every fixed additional derivative of the amplitude or phase parameters has the corresponding estimate after increasing the number of integrations; its original polynomial frequency factors must be included before choosing \(N\). The constants depend on the actual compact set, gradient margin and finitely many original derivatives, rather than a replaced phase.

### 18.3. The exact diffeomorphism covector map

Let \(\kappa:X\to Y\) be a smooth diffeomorphism between coordinate opens of dimension \(d\), and put \(\phi=\kappa^{-1}\). The already constructed scalar pullback retains its full test Jacobian:

\[
\langle\kappa^*u,f\rangle
 =\langle u,(f\circ\phi)|\det D\phi|\rangle.
\tag{WF5}
\]

Fix \(x_0\), \(y_0=\kappa(x_0)\), and \(\xi_0\ne0\), and put
\(\eta_0=D\phi(y_0)^T\xi_0\). Suppose \((y_0,\eta_0)\) is regular for \(u\). Choose an original compact cutoff \(\chi\) equal to one on a neighborhood of \(y_0\) so that \(v=\chi u\) has rapidly decreasing transform on a cone \(V\) about \(\eta_0\). Shrink an \(x\)-cutoff \(b\) about \(x_0\) until its image lies in that neighborhood. Its transform after pullback is exactly

\[
\widehat{b\kappa^*u}(\xi)
=(2\pi)^{-d}\int\widehat v(\eta)I(\xi,\eta)\,d\eta,\qquad
I(\xi,\eta)=\int b(\phi(y))|\det D\phi(y)|
        e^{i(y\cdot\eta-\phi(y)\cdot\xi)}dy.
\tag{WF6}
\]

For each fixed \(\xi\), this is the Fourier inverse formula applied to a compact smooth test, and is absolutely convergent at large \(\eta\) by WF3. Its phase gradient is the original
\(\eta-D\phi(y)^T\xi\). On the compact support, both \(D\phi^T\) and its inverse have uniform finite norm bounds. Thus when \(|\eta|\) is below a sufficiently small multiple of \(|\xi|\), or above a sufficiently large multiple, the gradient is bounded below by \(c(|\xi|+|\eta|)\). For the remaining comparable lengths, continuity of \(D\phi\) and sufficiently small base/direction neighborhoods place \(D\phi(y)^T\xi\) in an angular cone whose closure lies in \(V\). If \(\eta\notin V\), compact angular separation gives the same lower bound. This compactness argument retains the full derivative matrix and its original covectors.

On those separated regions WF4 beats the polynomial bound for \(\widehat v\), with \(N\) larger than that order, the requested decay exponent and \(d\). On the remaining region \(\eta\in V\) and \(|\eta|\) comparable with \(|\xi|\), use the rapid input decrease and the original constant bound \(|I|\leq\int|b(\phi(y))||\det D\phi(y)|dy\). The integration volume is at most \(C(1+|\xi|)^d\); choosing the input decay exponent larger than that volume power and the requested output exponent proves rapid output decrease. Hence regularity at \((y_0,\eta_0)\) implies regularity at \((x_0,\xi_0)\). Applying this proved implication to the actual inverse diffeomorphism and using WF5's composition law proves both inclusions, giving the exact equality

\[
\operatorname{WF}(\kappa^*u)
 =\{(x,D\kappa(x)^T\eta):(\kappa(x),\eta)\in\operatorname{WF}(u)\}.
\tag{WF7}
\]

Invertibility keeps every displayed output covector nonzero. Both original Jacobians remain in WF5--WF6; they do not change the covector relation.

### 18.4. Products and the exact projection converse

For compact localizations \(v\) on \(\mathbb R^a\) and \(w\) on \(\mathbb R^b\), their already constructed tensor product has

\[
\widehat{v\otimes w}(\xi,\eta)=\widehat v(\xi)\widehat w(\eta).
\tag{WF8}
\]

Here the order of the two factors is input-coordinate order, as indicated by the variables; converting to the geometric chapter's output-then-input notation requires that actual permutation. The equality follows by its two original iterated test pairings and the factored exponential.

Write \(Z_u=\{(x,0):x\in\operatorname{supp}u\}\). Then

\[
\operatorname{WF}(u\otimes v)
\subset
\bigl((\operatorname{WF}(u)\cup Z_u)
      \times(\operatorname{WF}(v)\cup Z_v)\bigr)
          \setminus\{(\xi,\eta)=(0,0)\}.
\tag{WF9}
\]

Outside the product support the tensor distribution vanishes, by the proved exact support formula. At a point inside it but outside the displayed covector set, at least one nonzero component is a regular direction for its factor. Near that pair direction its length is at least a fixed positive fraction of the total frequency length. Its factor in WF8 decreases to every order, while the other has its original polynomial bound. Their product therefore decreases to every order in that product cone. Product spatial cutoffs are equal to one near the base point, so this proves the claimed inclusion with the correct original Fourier definition. WF2 then handles all smaller nonproduct cutoffs. No general equality for two arbitrary singular factors is asserted.

For the original projection \(\pi(x,y)=x\), define \(\pi^*u=u\otimes1\) by
\(\langle\pi^*u,f\rangle=\langle u,x\mapsto\int f(x,y)dy\rangle\). The integral test is smooth with compact support and every \(x\)-derivative is its actual integrated derivative, so this is a continuous distribution. The constant factor is smooth, and WF9 gives one inclusion in

\[
\operatorname{WF}(\pi^*u)
 =\{(x,y;\xi,0):(x,\xi)\in\operatorname{WF}(u)\}.
\tag{WF10}
\]

For the converse suppose \(\pi^*u\) is regular at \((x_0,y_0;\xi_0,0)\). By WF2 choose product cutoffs \(\alpha(x),\beta(y)\) supported in that regular base neighborhood, both equal to one near their respective points, with \(\beta\geq0\) and \(\int\beta>0\). Their full transform is
\(\widehat{\alpha u}(\xi)\widehat\beta(\eta)\). The regular cone contains \((\xi,0)\) for all \(\xi\) in a smaller cone about \(\xi_0\). Its restriction at \(\eta=0\) is the original nonzero scalar \((\int\beta)\widehat{\alpha u}(\xi)\). Division by that scalar proves rapid decrease of the original factor, contradicting singularity at \((x_0,\xi_0)\). This proves the exact converse, not only the forward inclusion.

### 18.5. Constructing the pullback for the original smooth map

Let \(F:X\subset\mathbb R^b\to Y\subset\mathbb R^a\) be smooth. Its precise normal set and the required condition are

\[
N_F=\{(F(x),\eta):\eta\ne0,\ DF(x)^T\eta=0\},
\qquad N_F\cap\operatorname{WF}(u)=\varnothing.
\tag{WF11}
\]

We construct the map under this original transversality condition; no pullback at a forbidden covector is assumed. Near any fixed \(x_0\), the unit directions in the kernel of \(DF(x_0)^T\) form a compact set, possibly empty. WF11 makes every such direction regular at \(F(x_0)\). A finite regular cone cover, a common sufficiently small target cutoff \(\chi\), and WF2 give an open cone \(V_{\rm reg}\) on which \(\widehat{\chi u}\) decreases to every order, containing an angular neighborhood of those kernel directions. On the compact complementary unit directions \(DF(x_0)^T\eta\) has a positive lower norm. Continuity allows a fixed original neighborhood \(U_0\) of \(x_0\) and a constant \(c>0\) with
\(|DF(x)^T\eta|\geq c|\eta|\) there for every complementary direction. Shrink \(U_0\) so its image lies in the region where \(\chi=1\).

For \(f\in C_c^\infty(U_0)\), put \(v=\chi u\) and define

\[
\langle F^*u,f\rangle
=(2\pi)^{-a}\int_{\mathbb R^a}\widehat v(\eta)
                   \left(\int_{U_0}f(x)e^{iF(x)\cdot\eta}dx\right)d\eta.
\tag{WF12}
\]

On \(V_{\rm reg}\), the rapid input decrease and \(\int|f|\) give an integrable bound. On its complement, the actual phase gradient is \(DF(x)^T\eta\), so WF4 gives a bound \(C_N(1+|\eta|)^{-N}\max_{|\alpha|\leq N}\|\partial^\alpha f\|_\infty\). Multiplying by the original polynomial bound for \(\widehat v\) and choosing \(N>m+a\) proves absolute convergence. It also proves a continuous finite-order distribution estimate on each original compact test support, with its complete coordinate and map derivative constants. For smooth \(u\), WF1 and absolute testing show that this is exactly the smooth scalar function \(u(F(x))\).

Here is the needed independence and locality, rather than an assumed gluing rule. Use the original Cartesian Gaussian regularization
\[
g_\epsilon(y)=(4\pi\epsilon)^{-a/2}
      e^{-|y|^2/(4\epsilon)},\qquad
v_\epsilon=g_\epsilon*v,\qquad
\widehat v_\epsilon(\eta)=e^{-\epsilon|\eta|^2}\widehat v(\eta).
\tag{WF13}
\]
Its full mass and Fourier identity are proved in the integration/Fourier chapters. The two absolute bounds for WF12 dominate uniformly for \(0<\epsilon\leq1\), since \(0<e^{-\epsilon|\eta|^2}\leq1\). Thus WF12 is the limit of the actual smooth pullbacks \(v_\epsilon\circ F\).

If two target cutoffs equal one near \(F(\operatorname{supp}f)\), their difference times \(u\) is a compact distribution \(w\) vanishing near that compact image. The distance between that image and \(\operatorname{supp}w\) is positive. Its original compact finite-order estimate, applied to every derivative of \(g_\epsilon(F(x)-y)\), shows uniform convergence to zero on that image, including every fixed \(x\)-derivative: the full differentiated Gaussian has finitely many polynomial factors in the original difference coordinates and inverse powers of \(\epsilon\), times the same exponential. For distance at least \(d>0\), each such factor is bounded by \(C\epsilon^{-M}e^{-d^2/(8\epsilon)}\), tending to zero. The inserted support cutoff derivatives also remain in this estimate. Consequently the two limits agree on \(f\).

The same argument handles restriction to smaller original neighborhoods. For a compact test crossing several \(U_0\)'s, choose a finite smooth partition subordinate to them and sum WF12. On an overlap the preceding common Gaussian comparison gives equality; refinements therefore have the same sum. This constructs a unique local distribution \(F^*u\) on all of \(X\) with these formulas, preserving the original map. It proves its locality and compatibility with restriction. At a diffeomorphism, the smooth Gaussian approximations and the full measure substitution show agreement with WF5, including its actual inverse Jacobian. At the projection the same approximations and the integrated test show agreement with WF10's construction.

Its precise wavefront bound is

\[
\operatorname{WF}(F^*u)
\subset\{(x,DF(x)^T\eta):(F(x),\eta)\in\operatorname{WF}(u)\}.
\tag{WF14}
\]

For completeness fix a nonzero \(\xi_0\) outside the displayed set over \(x_0\). The singular unit target directions over \(F(x_0)\) are compact. WF11 says their images under \(DF(x_0)^T\) never vanish, and the chosen output direction is different from every resulting direction. Compactness yields positive margins for both assertions. Choose a closed angular neighborhood \(\Gamma\) of that singular set retaining these margins. Its complementary directions have a finite regular cone cover; WF2 again chooses a common target cutoff so that \(\widehat v\) decreases to every order outside \(\Gamma\). Shrink both original base and output direction neighborhoods so the margins hold for all \(x\) in the support of a cutoff \(b\) and every allowed output \(\xi\). If the singular set is empty, local smoothness already proved in Section18.1 supplies the conclusion directly.

The localized output transform is WF12 with \(f(x)=b(x)e^{-ix\cdot\xi}\). Its inner phase is exactly \(F(x)\cdot\eta-x\cdot\xi\), with gradient \(DF(x)^T\eta-\xi\). For \(\eta\in\Gamma\), the two compact margins give
\(|DF(x)^T\eta-\xi|\geq c(|\eta|+|\xi|)\): normalize their combined lengths to one; if the continuous difference had zero minimum, the covectors would have the excluded common direction, or a nonzero singular target direction would map to zero. WF4 therefore beats the full polynomial input bound and gives every output inverse power after integration in \(\eta\).

For \(\eta\notin\Gamma\), use the rapidly decreasing input. Split at \(|\eta|\leq c_0|\xi|\), with \(c_0>0\) smaller than the reciprocal of twice the actual compact bound for \(\|DF^T\|\). On that region the gradient has norm at least \(|\xi|/2\), so WF4 and the rapid input bound give every output power. On the other region \(|\eta|>c_0|\xi|\), the original bound for the inner integral is \(\int|b|\); taking the input decay exponent larger than the requested output exponent plus \(a+1\) gives every output power after integrating the full tail. This proves WF14 with the original Fourier constant still present in WF12. It proves a bound, and does not claim a converse for an arbitrary smooth map.

For a submersion \(F\), the normal set is empty, so the construction applies to every \(u\). Retain a nonzero \(a\)-row derivative minor at \(x_0\) and complete \(F\)'s coordinates by the remaining original \(x\)-coordinates. The resulting map \(\kappa(x)=(F(x),x_J)\) has its actual nonzero determinant. The proved inverse/implicit theorem gives a local diffeomorphism; in these coordinates \(F=\pi\circ\kappa\). Gaussian comparison in WF12 proves \(F^*u=\kappa^*(\pi^*u)\). WF7 and the exact WF10 converse therefore give

\[
\operatorname{WF}(F^*u)
 =\{(x,DF(x)^T\eta):(F(x),\eta)\in\operatorname{WF}(u)\}
 \quad\text{for a submersion}.
\tag{WF15}
\]

The derivative identity is the original chain rule
\(DF^T=D\kappa^T D\pi^T\). Its injectivity on target covectors is precisely full row rank, so every right-hand covector is nonzero. Every dimension-zero case has its point mass and empty Fourier factor; when the target has dimension zero, its distributions are smooth constants and both wavefront sets are empty.
