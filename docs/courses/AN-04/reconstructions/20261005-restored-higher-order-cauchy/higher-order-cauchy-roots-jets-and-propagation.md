# Higher-order Cauchy problems: roots, jets and propagation

Original programme exposition and all twenty-three original solved exercises are retained and completed here. Current source and proof review: GPT-6 Astra (OpenAI), Ultra, 5 October 2026. This independently written lesson is dedicated under CC0. Linked prerequisite components retain their respective licences, including the separately supplied GFDL 1.2 notices. Approved purchased sources are valid mathematical sources and ordinary citations; no citation replaces a programme proof.

Begin with the [scalar first-order Cauchy lesson](../20261005-restored-first-order-cauchy/first-order-cauchy-energy-and-wavefront.md). Its weak energy and existence theorem supplies each branch evolution below.

The aim is to solve a scalar equation of order \(m\) by following its \(m\) simple characteristic branches. The branches separate the equation into first-order evolutions; the initial data remain a vector of normal derivatives. Interpolation reconnects these two descriptions and explains the different Sobolev orders of the data. We then pass from a global symbol model to local differential operators, prove semiglobal existence, and identify the singularities arriving at a noncharacteristic initial surface.

Throughout,
\[
 D_t=-i\partial_t,\qquad D_x=-i\partial_x,
 \qquad (u,v)=\int u\overline v,
\]
so the pairing is linear in its first entry. Initial data in this convention are \(D_t^ju(0)\), rather than \(\partial_t^ju(0)\). The scalar first-order energy and existence theorem is the input from the preceding lesson. The exact earlier programme proofs are [ordinary products, adjoints and remainders](../20261004-free-intrinsic-graph/prerequisites/ordinary-operator-calculus.md), [all-real global Sobolev maps](../20261005-cauchy-foundations/sharp-lower-bound.md), [actual asymptotic sums](../20261004-free-canonical-composition/homogeneous-symbol-transport.md) and [ordered conic parametrices](../20261004-free-intrinsic-graph/prerequisites/conic-parametrices-and-localization.md). The proof map identifies the unique used locators and complete earlier closure. Section 4 develops the mixed half-space spaces, duality, one-sided extension and differential normal recovery using exact preceding programme proofs. The boundary calculus retains its distinct supported and restricted distribution meanings.

## 1. Uniformly simple roots give bounded branch symbols

Consider
\[
 P=\sum_{k=0}^m P_k(t,x,D_x)D_t^k,\qquad P_m=I. \tag{HC1}
\]
The symbol of \(P_k\) belongs to the bounded ordinary spatial class \(S^{m-k}_{1,0}\), with every derivative in the full base \((t,x)\) bounded in its symbol seminorms. Its specified principal part \(p_k\) is homogeneous of degree \(m-k\) for \(\xi\ne0\); after a fixed low-frequency cutoff it differs from the full symbol by \(S^{m-k-1}\). We require this one-step principal-symbol property. A full classical expansion of every lower-order coefficient is not assumed.

The principal polynomial
\[
 p(t,x,\tau,\xi)=\sum_{k=0}^m p_k(t,x,\xi)\tau^k
\]
is monic in \(\tau\). Its roots are real for \(\xi\ne0\), and at every root
\[
 |p_\tau(t,x,\tau,\xi)|\ge c|\xi|^{m-1},\qquad c>0. \tag{HC2}
\]
Order them as \(\lambda_1<\cdots<\lambda_m\). Bounded coefficients of the normalized monic polynomial give \(|\lambda_j|\le C|\xi|\). One elementary root bound follows by dividing the polynomial by \(\tau^m\): if \(|\tau|/|\xi|\) is sufficiently large, the sum of the other terms has modulus less than one and cannot cancel the leading term.

At a root,
\[
 p_\tau(\lambda_j)=\prod_{\nu\ne j}(\lambda_j-\lambda_\nu).
\]
For \(m\ge2\), the upper bound on all but one factor and (HC2) give \(|\lambda_j-\lambda_\nu|\ge c'|\xi|\). Thus separation is uniform. The implicit-function theorem on the unit spatial cosphere gives smooth roots. Their increasing order prevents a permutation on overlaps. Homogeneity then gives
\[
 |\partial_{t,x}^\beta\partial_\xi^\alpha\lambda_j|
 \le C_{\alpha\beta}|\xi|^{1-|\alpha|}. \tag{HC3}
\]
For completeness, differentiate \(p(t,x,\lambda_j,\xi)=0\). At each derivative order the only highest derivative of \(\lambda_j\) occurs multiplied by \(p_\tau(\lambda_j)\). Every other term uses bounded coefficient derivatives and already controlled root derivatives. Divide by (HC2), induct on derivative order, and restore the homogeneous degrees. For \(m=1\) there is no pairwise-gap argument to make; the same implicit derivative computation applies.

Let \(\chi\) equal one near \(\xi=0\) and have compact support. The symbols \((1-\chi)\lambda_j\) give global tangential operators \(A_j\) of order one. Their principal symbols are real; consequently \(-iA_j\) has purely imaginary order-one principal part, with a bounded order-zero real part. The scalar first-order energy theorem applies to \(\partial_t-iA_j\).

## 2. Left division and interpolation recover all Cauchy jets

The first reduction is an exact identity of operators:
\[
 P-(D_t-A_j)Q_j=R_j(t,x,D_x),\qquad
 Q_j=\sum_{k=0}^{m-1}Q_{jk}D_t^k,\quad
 Q_{jk}\in S^{m-1-k},\quad Q_{j,m-1}=I. \tag{HC4}
\]
To construct it, set \(Q_{j,m-1}=I\). For \(k=m-1,m-2,\ldots,1\), define
\[
 Q_{j,k-1}=P_k-(D_tQ_{jk})+A_jQ_{jk},\qquad
 R_j=P_0-(D_tQ_{j0})+A_jQ_{j0}. \tag{HC35}
\]
For \(m=1\), the recursion is empty and the last formula uses \(Q_{j0}=I\). Expanding \((D_t-A_j)Q_j\), the coefficient of \(D_t^k\) is \(Q_{j,k-1}+D_tQ_{jk}-A_jQ_{jk}\), which this recursion sets equal to \(P_k\). Thus all positive normal powers cancel exactly. If \(Q_{jk}\) has spatial order \(m-1-k\), the three terms defining the next coefficient have orders at most \(m-k\); its time derivatives retain these bounds by the full-base hypotheses. Descending induction proves every claimed quotient order and uniform parameter bound. The identity
\[
 D_t B(t)=B(t)D_t+(D_tB)(t),\qquad D_tB=-i\partial_tB,
\]
retains every coefficient time derivative. At each step monicity removes exactly one normal coefficient. The final defect is tangential. Its tentative order is \(m\), but its principal polynomial is
\(p-(\tau-\lambda_j)q_j\), where
\[
 q_j(t,x,\tau,\xi)=\prod_{\nu\ne j}(\tau-\lambda_\nu).
\]
That polynomial is zero. Hence \(R_j\in S^{m-1}\), including its low-frequency part.

Lagrange interpolation, applied to the polynomial \(\tau^k\) for \(k<m\), is the identity
\[
 \tau^k=\sum_{j=1}^m
 \frac{\lambda_j^k}{p_\tau(\lambda_j)}q_j(\tau). \tag{HC5}
\]
Indeed, both sides have degree at most \(m-1\) and agree at every \(\lambda_\ell\). Their difference has \(m\) distinct zeros and is therefore zero. The tangential symbol
\[
 M_{kj}=(1-\chi)\lambda_j^k/p_\tau(\lambda_j)
\]
has order \(k+1-m\). Quantize (HC5) and use the complete ordinary product expansion. The leading terms cancel; the composition defect loses one spatial order. Thus
\[
 D_t^ku=\sum_jM_{kj}Q_ju+
          \sum_{\ell<m}B_{k\ell}D_t^\ell u,
 \qquad B_{k\ell}\in S^{k-\ell-1}. \tag{HC6}
\]
The cutoff part is included in \(B_{k\ell}\). Its compact frequency support is smoothing at every required spatial order.

Applying the all-real Sobolev maps gives
\[
 \sum_{k<m}\|D_t^ku\|_{H^{s+m-1-k}}
 \le C_s\left(\sum_j\|Q_ju\|_{H^s}
        +\sum_{\ell<m}\|D_t^\ell u\|_{H^{s+m-2-\ell}}\right). \tag{HC7}
\]
The row and column orders explain the weights: subtracting \(k+1-m\) from \(s\) gives \(s+m-1-k\), while subtracting \(k-\ell-1\) from \(s+m-2-\ell\) gives the same output order.

## 3. Energy for weak jets, at every real Sobolev order

**Higher-order energy theorem.** For \(s\in\mathbb R\), \(T>0\), and
\[
 u\in\bigcap_{k=0}^{m-1}C^k([0,T];H^{s+m-1-k}),
 \qquad Pu\in L^1((0,T);H^s),
\]
there is a constant \(C_{s,T}\) such that
\[
 \sup_{0\le t\le T}\sum_{k<m}\|D_t^ku(t)\|_{H^{s+m-1-k}}
 \le C_{s,T}\left(
 \sum_{k<m}\|D_t^ku(0)\|_{H^{s+m-1-k}}
 +\int_0^T\|Pu(t)\|_{H^s}\,dt\right). \tag{HC8}
\]
Its constants depend on the operator bounds and root separation. They are not uniform as distinct roots merge.

**Proof.** Write \(Y(t)\) for the weighted jet sum on the left of (HC7), and \(w_j=Q_ju\). Identity (HC4) gives, distributionally,
\[
 (\partial_t-iA_j)w_j=i(Pu-R_ju). \tag{HC9}
\]
The forcing belongs to \(L^1H^s\), because \(R_j\) has order \(m-1\) and \(u\in C_tH^{s+m-1}\). The first-order energy theorem in its weak domain gives
\[
 \sum_j\|w_j(t)\|_{H^s}
 \le C\left(Y(0)+\int_0^t\|Pu\|_{H^s}\,dr+\int_0^tY(r)\,dr\right). \tag{HC10}
\]
No \(C^1_tH^s\) assumption on \(w_j\) is needed: (HC9) supplies an absolutely continuous primitive in \(H^{s-1}\).

In the lower-order sum in (HC7), remove the term with \(\ell=m-1\). Since \(Q_{j,m-1}=I\), one quotient expresses this highest lower-order jet as \(w_j\) minus terms involving the lower jets. Its \(H^{s-1}\) norm is bounded by \(\|w_j\|_{H^s}\) and
\[
 Z(t)=\sum_{k<m-1}\|D_t^ku(t)\|_{H^{s+m-2-k}}.
\]
Each summand has time derivative \(iD_t^{k+1}u\) in the displayed lower Sobolev space. Thus
\(Z(t)\le Z(0)+\int_0^tY(r)\,dr\). Combine this with (HC7) and (HC10):
\[
 Y(t)\le C\left(Y(0)+\int_0^t\|Pu\|_{H^s}\,dr+\int_0^tY(r)\,dr\right).
\]
Grönwall proves (HC8). When \(m=1\), \(Z\) is the empty sum and this is exactly the first-order argument.

The stronger estimate retains the weighted forcing norm. The same proof, using the first-order pointwise energy bound on every subinterval, has constants \(A_s,B_s\ge0\) such that
\[
 Y(t)\le A_s e^{B_st}Y(0)
       +A_s\int_0^t e^{B_s(t-r)}\|Pu(r)\|_{H^s}\,dr. \tag{HC34}
\]
Indeed the quotient bounds and the lower-jet primitive give a Volterra inequality with a constant times \(\int_0^tY\); its resolvent is the displayed exponential kernel. These constants use the fixed bounded full-base symbol seminorms and the root gaps. For \(1\le p<\infty\) and \(\lambda\ge\max(1,2B_s)\), Minkowski's integral inequality gives
\[
 \sum_{k<m}\left(\lambda\int_0^T
 e^{-p\lambda t}\|D_t^ku(t)\|_{H^{s+m-1-k}}^p\,dt\right)^{1/p}
 \le C_s\left(Y(0)+\int_0^Te^{-\lambda r}\|Pu(r)\|_{H^s}\,dr\right). \tag{HC11}
\]
To verify the uniform endpoints, the normalized \(L^p\) norm of
\(e^{-(\lambda-B_s)t}\) on the positive half-line is
\((\lambda/[p(\lambda-B_s)])^{1/p}\le2\). The kernel translated to \(r\) has the same bound; the external source factor is exactly \(e^{-\lambda r}\). For \(p=\infty\), use the weighted supremum in each left-hand summand: the exponential kernel has supremum one, and no \(\lambda\) prefactor occurs. Thus \(C_s\) is independent of \(p,\lambda,T\) in the stated large-\(\lambda\) range. Dependence on the Sobolev parameter is retained through the imported symbol bounds; no uniform-in-\(s\) bound is presumed. The finite-interval unweighted (HC8) follows by taking the supremum in (HC34).

## 4. Green's formula, existence and the missing trace step

### Mixed spaces, restrictions and the one-sided multipliers

Before constructing a weak solution, establish the normal regularity and trace tools that will identify its Cauchy jets. Write
\[
 h(\xi)=\langle\xi\rangle,\qquad R(\tau,\xi)=\langle(\tau,\xi)\rangle,
 \qquad
 \|U\|_{(r,q)}^2=(2\pi)^{-(n+1)}
       \int R^{2r}h^{2q}|\widehat U(\tau,\xi)|^2\,d\tau\,d\xi.
 \tag{HC37}
\]
The orders \(r,q\) are arbitrary real numbers. The argument also applies to a fixed finite-dimensional Hermitian coefficient space. The whole-space Hilbert structure, distributional multiplier domains and smooth-coefficient bounds are proved in [the complete two-weight Hilbert and trace treatment](../20261005-mixed-halfspace-foundations/two-weight-hilbert-spaces-and-traces.md), with [H1–H3 coefficient multiplication, density and duality](../20261005-mixed-halfspace-foundations/halfspace-support-and-duality.md). A compactly supported smooth coefficient is a mixed symbol of order \((0,0)\), so that theorem makes its multiplication bounded on every displayed scale. Localized smooth coefficients and their finitely many derivatives are sufficient below.

Let \(r^+\) denote restriction to \(t>0\). Define
\[
 \begin{aligned}
 \dot H^{(r,q)}&=\{U\in H^{(r,q)}:\operatorname{supp}U\subset\{t\ge0\}\},\\
 \overline H^{(r,q)}&=r^+H^{(r,q)},\qquad
 \|u\|_{\overline H^{(r,q)}}=\inf_{r^+U=u}\|U\|_{(r,q)}.
 \end{aligned} \tag{HC38}
\]
The dot space has the ambient norm. The bar space is the quotient by the closed subspace of distributions supported in \(t\le0\). These subspaces are closed because norm convergence implies distributional convergence. Completeness of the quotient is the closed-subspace quotient theorem in [the complete quotient and orthogonal projection proof, H1](../20261005-mixed-halfspace-foundations/halfspace-support-and-duality.md). An intrinsic normal derivative on the bar space is obtained by differentiating any extension and restricting; the derivative of a difference supported in \(t\le0\) has the same support, so the definition is independent of the extension. It does not mean differentiating a zero extension.

Set
\[
 J_+^a=(h(D_x)+iD_t)^a,\qquad
 J_-^a=(h(D_x)-iD_t)^a,\qquad a\in\mathbb R,
 \tag{HC39}
\]
using the right-half-plane logarithm of \(h\pm i\tau\). These are smooth tempered-distribution multipliers, with inverses \(J_\pm^{-a}\), and moduli exactly \(R^a\). The complete one-sided multiplier proof is [H4–H5](../20261005-mixed-halfspace-foundations/halfspace-support-and-duality.md); the full complex-order version is [PS6–PS11 and the explicit Gamma proof](../20261005-positive-boundary-orders/positive-order-halfspace-bounds.md). These exact proofs are included in this edition. Reflection \(t\mapsto-t\) gives the corresponding proof for \(J_-^a\): both it and its inverse preserve support in \(t\le0\). The factor \(h(D_x)^q\) acts only tangentially, so preserves either normal half-space. Thus the existing one-sided proof supplies
\[
 \begin{aligned}
 J_+^rh(D_x)^q &: \dot H^{(r,q)}\longrightarrow L^2(\{t\ge0\}),\\
 J_-^rh(D_x)^q &: \overline H^{(r,q)}\longrightarrow L^2(\{t>0\})
 \end{aligned} \tag{HC40}
\]
as onto isometries for every real pair. For the first map, use the whole-space norm and the support of the inverse. For the second, the whole-space isometry maps the full kernel of restriction onto the \(L^2\) functions supported in \(t\le0\). Its quotient is exactly \(L^2\) on the positive half-space. This proves the assertion also at negative and nonintegral orders.

In particular there is one explicit minimal-norm extension of \(u\in\overline H^{(r,q)}\):
\[
 \begin{aligned}
 g&=J_-^ru\in L^2((0,\infty);H^q_x),\\
 E_ru&=J_-^{-r}\bigl(H(t)g\bigr),\qquad
 r^+E_ru=u,\qquad
 \|E_ru\|_{(r,q)}=\|u\|_{\overline H^{(r,q)}}.
 \end{aligned} \tag{HC41}
\]
Here \(H(t)g\) is its zero extension as an \(L^2\) function of time with values in \(H^q_x\). The inverse quotient map in (HC40) proves the identity, and the full Fourier norm proves the equality. The same \(E_r\) is independent of \(q\), because tangential weights commute with every operation in this formula. Realizations of \(g\) at different tangential orders agree as distributions, hence so do their zero extensions and resulting extensions. This gives one extension for the intersection over all tangential orders as well. Neither \(u\) nor \(E_ru\) is asserted to have forward support.

### Duality, embeddings and the supported decomposition

The full supported/restricted antidual proof is [H3](../20261005-mixed-halfspace-foundations/halfspace-support-and-duality.md), which retains Proposition 10.2(b) with its density and orthogonal projection arguments. Apply it to \(h(D_x)^qU\) and \(h(D_x)^{-q}v\). These maps preserve support and restriction and are isometries between the mixed and ordinary spaces; their factors cancel in the Fourier pairing. Consequently
\[
 (\dot H^{(r,q)})^*=\overline H^{(-r,-q)},\qquad
 (\overline H^{(r,q)})^*=\dot H^{(-r,-q)}
 \tag{HC42}
\]
isometrically, with antiduals under the pairing linear in the first entry. Pair \(U\) with any whole-space extension \(V\) of the bar vector by \((2\pi)^{-(n+1)}\int\widehat U\overline{\widehat V}\). The programme duality proof shows independence of \(V\) and representation of every bounded functional. On smooth vectors it is the ordinary integral. A bar vector is not identified with an arbitrary supported extension.

The dense test space is also dense in the mixed dot space. Translate a dot vector forward by \(\epsilon>0\); Fourier dominated convergence proves convergence in (HC37). Mollify with a smooth kernel supported in a ball of radius less than \(\epsilon/2\). Its uniformly bounded Fourier multipliers converge to one; weighted dominated convergence applies again. The mollified vector has every ordinary Sobolev order and support a positive distance from the boundary. Cut it off on successively larger balls. At an integer ordinary order above \(\max(r,r+q,0)\), Leibniz and dominated convergence prove cutoff convergence; that ordinary norm bounds the mixed norm. A diagonal choice gives approximation by \(C_c^\infty(t>0)\) in the dot space. Restrictions of whole-space smooth approximations are dense in the bar space. Boundary-supported distributions remain in the supported space at the negative orders where their ambient norm is finite.

The mixed embeddings are
\[
 H^{(r,q)}\hookrightarrow H^{(a,b)},\quad
 \dot H^{(r,q)}\hookrightarrow\dot H^{(a,b)},\quad
 \overline H^{(r,q)}\hookrightarrow\overline H^{(a,b)}
 \quad\text{if }a\le r,\quad a+b\le r+q,
 \tag{HC43}
\]
with norm at most one: the target/input weight ratio is \((R/h)^{a-r}h^{a+b-r-q}\le1\). The bar bound follows by infimizing over extensions. With at least one tangential coordinate, both conditions are necessary for a continuous global inclusion. Take a nonzero smooth compact test \(\chi\) supported strictly in \(t>0\), modulated by \(e^{iLt}\) and then by \(e^{iLx_1}\). Its whole-space norms have orders \(L^r\) and \(L^{r+q}\), respectively, with positive limiting constants after division by those powers. Indeed translating its Fourier transform gives those pointwise weight limits; the rapid decay of \(\widehat\chi\) and polynomial weight-ratio bounds control the tails and justify dominated convergence. For a bar norm, pairing the modulated test with itself in (HC42) gives the matching lower bound, while its full extension gives the upper bound. A continuous inclusion forces precisely the two displayed inequalities. With no tangential coordinate only the ordinary normal-order condition has content.

Forward support in a negative-normal-order existence argument comes from a different formula. For \(f\in\dot H^{(r,q)}\), set \(v=J_+^{-1}f\). Then
\[
 f=f_0+D_tf_n,\qquad
 f_0=h(D_x)v\in\dot H^{(r+1,q-1)},\qquad
 f_n=iv\in\dot H^{(r+1,q)},
 \tag{HC44}
\]
and each component norm is exactly \(\|f\|_{(r,q)}\). The identity is \((h+iD_t)v=f\), with \(D_t=-i\partial_t\). The modulus \(|h+i\tau|=R\) gives the norms; the one-sided inverse gives the supports. This works at all real orders, for finite-dimensional vectors, and commutes with every tangential weight. The unrestricted Fourier decomposition used later need not preserve support.

### The normal step, complete jets and boundary slices

For all real \(r,q\), the precise one-step assertion is
\[
 \begin{gathered}
 u\in\overline H^{(r,q)}
 \quad\Longleftrightarrow\quad
 u\in\overline H^{(r-1,q+1)},\quad
 D_tu\in\overline H^{(r-1,q)},\\
 \tfrac12\|u\|_{\overline H^{(r,q)}}^2
 \le \|u\|_{\overline H^{(r-1,q+1)}}^2
       +\|D_tu\|_{\overline H^{(r-1,q)}}^2
 \le\|u\|_{\overline H^{(r,q)}}^2.
 \end{gathered} \tag{HC45}
\]
Necessity and the upper bound follow from any whole-space extension and the identity \(R^{2r}h^{2q}=h^2R^{2r-2}h^{2q}+\tau^2R^{2r-2}h^{2q}\), followed by its infimum norm. For sufficiency put \(V=J_-^{r-1}h(D_x)^qu\) on the half-space. The two assumed memberships give \(hV,D_tV\in L^2(t>0)\). Hence
\[
 J_-^rh(D_x)^qu=hV-iD_tV\in L^2(t>0).
\]
The inverse quotient isomorphism (HC40) gives the desired membership. The squared triangle bound \(\|hV-iD_tV\|_2^2\le2(\|hV\|_2^2+\|D_tV\|_2^2)\) proves the lower inequality. Operators commute on the restriction quotient, so no trace or boundary delta has entered this proof.

For nonnegative integer \(k\), this gives the complete intrinsic jet description
\[
 \overline H^{(k,q)}
 =\{u:D_t^ju\in L^2((0,\infty);H^{q+k-j}_x),\ 0\le j\le k\},
 \qquad
 \|u\|_{\overline H^{(k,q)}}^2\asymp
 \sum_{j=0}^k\|D_t^ju\|_{L^2_tH^{q+k-j}_x}^2.
 \tag{HC46}
\]
At \(k=0\), the bar space is \(L^2_tH^q_x\), identified by zero extension. Inductively the jet conditions give \(u\in\overline H^{(k-1,q+1)}\) and \(D_tu\in\overline H^{(k-1,q)}\); (HC45) gives membership and a bound by their complete jet sums. Conversely, for every full extension the expansion of \((\tau^2+h^2)^k\) bounds the jet sum by a fixed multiple of its mixed norm; infimize over extensions. Constants depend on \(k\), and the highest jet is retained. Whole-space and dot versions use the same Fourier identity with ambient derivatives. A zero-extended bar vector need not have these ambient derivatives.

For integer \(j\ge0\), real \(r>j+1/2\) and any \(q\), [Section 9 of the included two-weight companion](../20261005-mixed-halfspace-foundations/two-weight-hilbert-spaces-and-traces.md) proves (MSB44)–(MSB49):
\[
 \begin{aligned}
 D_t^ju(t)&\in H^{r+q-j-1/2}_x\quad(t\ge0),\\
 \sup_{t\ge0}\|D_t^ju(t)\|_{H^{r+q-j-1/2}}^2
 &\le\frac{c_{r,j}}{2\pi}\|u\|_{\overline H^{(r,q)}}^2,
 \qquad
 c_{r,j}=\int_{\mathbb R}\lambda^{2j}(1+\lambda^2)^{-r}\,d\lambda<\infty.
 \end{aligned} \tag{HC47}
\]
The slices are continuous in the target norm. That programme proof retains the Fourier coefficient, proves independence of the extension and proves boundary continuity. The threshold is strict; no endpoint \(r=j+1/2\) or arbitrary distributional trace is inferred.

**A minimal extension can occupy both sides.** In the one-dimensional normal model take \(u(t)=e^{-t}\) for \(t>0\). Formula (HC41) gives \(J_-u=(1-\partial_t)u=2e^{-t}\) and \(E_1u=e^{-|t|}\). Its squared whole-space \(H^1\) norm is \(2\), equal to \(\|2e^{-t}\|_{L^2(t>0)}^2\). The sum of the two intrinsic squared \(L^2\) norms in (HC45) is \(1\), so the factor \(1/2\) is attained. The zero extension has a jump and a delta in its derivative and is not in \(H^1\). Bar and dot norms cannot be interchanged.

### Boundary operators survive changes of charts

The preceding trace is expressed in one collar. To use it at a curved initial surface, we must know which parts survive a change of collar. Here we use ordinary isotropic Sobolev spaces: \(\overline H^s=\overline H^{(s,0)}\). We do not assert that an arbitrary boundary coordinate change preserves the two separate mixed orders.

A smooth manifold with boundary has Hausdorff, second-countable charts into relatively open subsets of \(t\ge0\). Smooth chart transitions and their inverses extend smoothly to neighborhoods of the closed half-space. Near a boundary point, write a transition as \(\Phi(x,t)=(F(x,t),t\beta(x,t))\). The integral identity
\[
 \Phi_n(x,t)=t\int_0^1\partial_t\Phi_n(x,\lambda t)\,d\lambda
\]
gives this factorization. At the boundary the tangential derivative is invertible. The derivatives of the transition and its given inverse multiply to the identity, and the positive interior maps to the positive interior; hence \(\beta(x,0)>0\). After shrinking, the extension has invertible derivative and \(\beta>0\). The complete smooth inverse construction in [the finite inverse theorem P3 in the exact U001 map](../20261004-free-stationary-phase/proof-map.html) supplies a neighborhood diffeomorphism. It preserves both normal sides.

Pullback by this diffeomorphism transports supported distributions to supported distributions. It also transports the full backward-supported kernel of interior restriction to that kernel. Thus it acts on restricted distributions independently of their extension. The supported action is independent of the chosen smooth extension of the chart transition as well. Two such extensions have identical derivatives of every order on the closed positive side. Their transformed tests therefore differ by a function flat there. A compactly localized distribution has finite order \(N\). Cut a flat test off in a collar of width \(\varepsilon\); Taylor's formula to order greater than \(2N\) makes its derivatives through order \(N\) tend uniformly to zero. The support condition discards the rest of the test. The finite-order bound then annihilates that difference. This proves independence even for distributions supported at the boundary.

The full localized all-real Sobolev coordinate proof is [H1–H3 of the global boundary companion](../20261005-global-boundary-operators/global-boundary-operator-calculus.md), using the complete [Besov coordinate proof B2](../20261005-conormal-test-foundations/conormal-amplitudes-and-test-spaces.md). Its integer estimates retain the Jacobian in the adjoint; the frequency-block proof gives every real intermediate order. Both sides are preserved, so the bound restricts to the dot space and descends to the bar quotient. The inverse bound gives equivalent norms, including finite-dimensional frame changes.

The actual locally finite coordinate cover and subordinate smooth partition are [PS5](../20261004-free-intrinsic-graph/prerequisites/global-principal-symbol.md). The same compact-shell construction works with half-balls: their relative interiors cover, their closed smaller half-balls are compact, and the usual coordinate bumps restrict smoothly. Dividing by the locally finite positive bump sum gives the boundary partition. Only finitely many terms meet a fixed compact set. These facts define the local supported and restricted spaces independently of charts and supply the finite patching below.

Let \(E\to X\) and \(F\to\partial X\) be finite-rank smooth bundles. A **boundary differential operator** \(B:C^\infty(X;E)\to C^\infty(\partial X;F)\) of total order at most \(\mu\) is locally
\[
 Bu=\sum_{|\alpha|+j\le\mu}
             A_{\alpha j}(x)D_x^\alpha\gamma_j u,
 \qquad \gamma_j u=(D_t^ju)|_{t=0}.
\]
Its **transversal order** is at most \(k\) if only \(j\le k\) occur. Equivalently, \(B\) annihilates every smooth section vanishing to order \(k+1\) on the boundary. One implication follows by differentiating \(t^{k+1}v\). For the converse, test \(t^j\eta(t)v(x)\), with \(\eta=1\) near zero, at each \(j>k\), and choose the tangential jets of \(v\) arbitrarily. This isolates every coefficient with that normal degree. The ideal of sections vanishing to order \(k+1\) is intrinsic, so the transversal order is invariant under boundary coordinate and frame changes. It can be strictly smaller than the total order.

**Boundary differential trace theorem.** For finite \(\mu,k\) as above and every real \(s>k+1/2\),
\[
 B:\overline H^s_{\mathrm{loc}}(X^\circ;E)
       \longrightarrow H^{s-\mu-1/2}_{\mathrm{loc}}(\partial X;F)
 \quad\text{continuously}.
 \tag{HC51}
\]
It agrees with \(B\) on smooth sections and is its unique continuous extension. It also sends compactly supported inputs to compactly supported boundary outputs, with the corresponding finite-chart norm bound. No compactness of \(X\) is assumed.

**Proof.** In a localized collar, (HC47) with \(r=s,q=0\) gives
\(\gamma_j:\overline H^s\to H^{s-j-1/2}\), because \(j\le k<s-1/2\). The tangential differential term of degree \(|\alpha|\) maps this to \(H^{s-j-|\alpha|-1/2}\). Smooth matrix multiplication is bounded there, and \(j+|\alpha|\le\mu\) gives its continuous inclusion in \(H^{s-\mu-1/2}\). Summing the finitely many terms proves the local bound; all constants depend only on fixed compact patches and finitely many coefficient and coordinate derivatives.

Smooth sections up to the boundary are locally dense in the restricted space. Indeed, choose whole-space extensions on finitely many patches meeting a fixed compact set, apply the ordinary Sobolev smoothing approximation there, and reconstruct the localized sections with the smooth partition and original frames. The quotient norm bounds the restricted approximation error. On each overlap, the two local formulas for \(B\) agree on these smooth approximants by the definition of the boundary operator. The real-order coordinate/frame bounds on \(\partial X\) let us pass to their limits in the same target Sobolev space. The limits agree and glue. The finite patch estimates prove continuity on every compact output set; density proves uniqueness. A test neighborhood disjoint from the input support has zero output, which proves the compact-support assertion. All bundle matrix products keep their original order. This completes the proof. \(\square\)

This is the precise manifold boundary-differential statement in Hörmander's Appendix B.2.10, with source credit. Its strict threshold concerns transversal order; its output loss concerns total order. The distributional boundary extension and compressed wavefront class used later are different objects and retain the exact global-boundary-calculus inputs in Section 9.

### Differential equations recover the missing normal orders

Here is the full local differential theorem needed in Section 5. On an open collar \(X\), let
\[
 P=D_t^\mu+\sum_{|\alpha|\le\mu,\ \alpha_t<\mu}
                 a_\alpha(x,t)D^\alpha,
 \qquad a_\alpha\in C^\infty(X),\qquad\mu\ge1.
\]
Define local bar spaces by requiring \(\chi u\) to belong to (HC38) for each smooth compact collar cutoff. If
\[
 u\in\overline H^{(r_1,q_1)}_{\rm loc},\qquad
 Pu\in\overline H^{(r_2-\mu,q_2)}_{\rm loc},
\]
then
\[
 u\in\overline H^{(a,b)}_{\rm loc}
 \quad\text{whenever}\quad
 a\le r_2,\qquad a+b\le r_1+q_1,\qquad a+b\le r_2+q_2.
 \tag{HC48}
\]
There is no requirement \(a\le r_1\). All six indices are real. For order zero with an invertible coefficient the conclusion follows directly from the forcing membership and (HC43).

**Proof.** First suppose \(a\le r_1+1\), choose a compact cutoff \(\chi\), and put \(v=\chi u\). A derivative with \(j\) normal and \(\ell\) tangential differentiations maps \((r_1,q_1)\) to \((r_1-j,q_1-\ell)\), by its bounded weighted Fourier ratio. Smooth coefficient multiplication is bounded as above. By (HC43) and the two inequalities involving \(r_2,q_2\), \(\chi Pu\in\overline H^{(a-\mu,b)}\). Every term of \([P,\chi]u\) has total derivative order at most \(\mu-1\); its normal order is at least \(r_1-\mu+1\ge a-\mu\) and its total mixed order at least \(r_1+q_1-\mu+1\ge a+b-\mu\). Thus \(Pv\) belongs to the same space. Compute the commutator using a larger cutoff equal to one on \(\operatorname{supp}\chi\), keeping all coefficient bounds compactly based.

Every term of \(Pv\) except \(D_t^\mu v\) has normal degree below \(\mu\) and total degree at most \(\mu\). Its normal order is at least \(r_1-\mu+1\), and total order at least \(r_1+q_1-\mu\), sufficient for \(\overline H^{(a-\mu,b)}\). Subtract these actual terms; hence \(D_t^\mu v\in\overline H^{(a-\mu,b)}\).

Descend from \(j=\mu-1\) to zero. Initially
\(D_t^jv\in\overline H^{(r_1-j,q_1)}\subset\overline H^{(a-j-1,b+1)}\),
by \(a\le r_1+1\) and \(a+b\le r_1+q_1\). The next derivative already belongs to \(\overline H^{(a-j-1,b)}\). Apply (HC45); it gives \(D_t^jv\in\overline H^{(a-j,b)}\). At zero this proves the claim locally for \(u\).

If \(a\le r_1\), embedding suffices. Otherwise put \(S=a+b\), first lower the initial tangential order to \(S-r_1\), and iterate the preceding step at
\[
 a_\nu=\min(a,r_1+\nu),\qquad b_\nu=S-a_\nu,
 \qquad1\le\nu\le\lceil a-r_1\rceil.
\]
Each normal increase is at most one. Every target has total order \(S\), satisfies \(a_\nu\le a\le r_2\), and has \(S\le r_2+q_2\). Finite nested cutoffs prove the local induction on the desired final patch. The last pair is \((a,b)\), including fractional differences of the orders. For an invertible smooth leading matrix, multiply on the left by its smooth inverse on a smaller collar. Its mixed multiplication bound preserves the forcing class; the same finite-dimensional argument applies without commuting matrices. \(\square\)

This is the programme proof of the differential normal-recovery theorem in Hörmander's Appendix B.2.9, with credit to that source. A tangential pseudodifferential coefficient needs a separate mapping check. The integer normal mapping for the Cauchy model follows from (HC46), the full time Leibniz rule and the spatial Sobolev maps, then from whole-space duality at negative integers. Such an operator acts at fixed time and preserves both normal supports: its whole-space bound descends to the bar quotient, and (HC42) gives the dot bound. The differential theorem alone is not used to justify that model.

### Green's formula and weak existence

**Global Cauchy theorem.** Under (HC1)–(HC2), for every real \(s\),
\[
 f\in L^1((0,T);H^s),\qquad
 \phi_j\in H^{s+m-1-j},\quad 0\le j<m,
\]
there is a unique solution in the jet class of the energy theorem with
\(Pu=f\) in \(0<t<T\) and \(D_t^ju(0)=\phi_j\).

The Green form is needed with its exact sign and coefficient derivatives. If \(v\) is smooth and zero near \(T\), repeated integration by parts gives
\
 \int_0^T(u,P^*v)\,dt
 =\int_0^T(Pu,v)\,dt
 -i\sum_{j+k<m}(D_t^ju(0),D_t^k[P_{j+k+1}^*v). \tag{HC12}
\]
The brackets mean composition: \(D_t^k\) differentiates \(P_{j+k+1}^*\) as well as \(v\). The initial term for one normal derivative is already \(-i(u(0),v(0))\); iteration gives precisely the index budget in (HC12).

Apply (HC8) to the normally reordered adjoint, reverse \(t\), and multiply by its nonzero leading normal sign to restore monicity. Its normalized roots are still real and uniformly simple. At Sobolev parameter \(1-m-s\), the estimate controls
\[
 \|D_t^kv(0)\|_{H^{-s-k}}
 \le C\|P^*v\|_{L^1H^{1-m-s}}.
\]
Every term in the Leibniz expansion of the boundary form pairs with \(\phi_j\). If \(r\le k\) derivatives fall on \(v\), its resulting Sobolev order after \(P_{j+k+1}^*\) is
\(-s-r-(m-j-k-1)\ge -s-m+1+j\), the dual order of \(\phi_j\). Coefficient time derivatives retain the same spatial order.

The anti-linear functional on the range of \(P^*\) defined by
\
 P^*v\longmapsto
 \int_0^T(f,v)\,dt
 -i\sum_{j+k<m}(\phi_j,D_t^k[P_{j+k+1}^*v)
\]
is bounded in \(L^1H^{1-m-s}\). Zero terminal jets and (HC8) show that \(P^*v=0\) implies \(v=0\), so it is well defined. Hahn–Banach and the finite-interval Hilbert-valued \(L^1\) dual representation established in the preceding lesson give
\(u\in L^\infty H^{s+m-1}\) satisfying this weak identity. Interior tests give \(Pu=f\). It remains to prove regular jets and identify their traces; the weak identity alone does not do that.

We first take \(f,\phi_j\) smooth with compact temporal support and Schwartz spatial data. For mixed spaces use the Fourier weight
\[
 H^{(r,q)}:\quad \langle(\tau,\xi)\rangle^r\langle\xi\rangle^q.
\]
A bar denotes restriction of a whole-space distribution; a dot denotes a whole-space distribution supported in the closed half-space. The proof above gives the exact normal step
\[
 u\in\overline H^{(r,q)}
 \quad\Longleftrightarrow\quad
 u\in\overline H^{(r-1,q+1)},\quad
 D_tu\in\overline H^{(r-1,q)}. \tag{HC13}
\]
The sum of the two squared quotient norms lies between one half and one times the squared original norm. On the whole space the squared weights satisfy the exact identity
\[
 \langle(\tau,\xi)\rangle^{2r}\langle\xi\rangle^{2q}
 =(\tau^2+\langle\xi\rangle^2)
 \langle(\tau,\xi)\rangle^{2r-2}\langle\xi\rangle^{2q}.
\]
For integer \(r\ge0\), the mixed norm is equivalent to the complete sum of \(L^2_tH^{q+r-j}_x\) norms for \(0\le j\le r\). A bounded tangential family of spatial order \(d\) maps this scale to \(H^{(r,q-d)}\): apply the full time Leibniz rule and the spatial Sobolev maps to every jet. Negative integer normal orders follow by duality with the actual time-dependent tangential adjoint. Its kernel is supported at \(t=s\), so the map descends to restricted quotient spaces. These are the integer normal indices used in the following iteration.

On \((0,T)\), a temporal partition gives one piece zero near \(T\) and another zero near zero. Apply (HC13) to the first in the forward half-space and to the second after reflection \(t\mapsto T-t\). Smooth cutoff multiplication preserves the integer mixed scales, and every derivative of a cutoff has lower normal order. Adding the pieces gives the finite-interval recovery statement with both endpoints accounted for.

Initially \(D_t^ju\in\overline H^{(-j,s+m-1)}\). Suppose at stage \(k<m\) that
\[
 D_t^ju\in\overline H^{(k-j,s+m-1-k)},\qquad 0\le j\le m.
\]
The equation puts the highest derivative in
\[
 D_t^mu=f-\sum_{j<m}P_jD_t^ju
 \in\overline H^{(k-m+1,s+m-2-k)}.
\]
Each lower term belongs to \(\overline H^{(k-j,s+j-1-k)}\); its normal order is at least the target normal order, and their total orders are equal. This is exactly the mixed embedding criterion. Descending through \(j=m-1,m-2,\ldots,0\), use (HC13) on the already known next derivative and the preceding stage. It gives
\(D_t^ju\in\overline H^{(k+1-j,s+m-2-k)}\). Thus at \(k=m\),
\[
 D_t^ju\in\overline H^{(m-j,s-1)}.
\]
The exact trace theorem has the strict threshold \(r>j+1/2\). Applied to each of these jets, it yields continuous slices
\(D_t^ju\in C_tH^{s+m-j-3/2}\) for \(j<m\). This provisional half-order loss is enough to justify (HC12) distributionally.

Compare the weak identity with (HC12). Choose the initial jets of \(v\) so that all derivatives below \(m-1\) vanish. Only \(u(0)-\phi_0\) survives, paired with an arbitrary \(D_t^{m-1}v(0)\), so \(u(0)=\phi_0\). Next allow \(D_t^{m-2}v(0)\), keeping lower derivatives zero. The already identified \(u(0)\) cancels, leaving \(D_tu(0)-\phi_1\). Continue down the triangular Green form. Since \(P_m=I\), its diagonal pairing is always the arbitrary remaining test jet. All \(m\) traces are identified.

Construct smooth-data solutions at every higher Sobolev parameter. Each has the provisional continuous jet class just proved. Energy uniqueness at a common lower parameter identifies any two. They therefore form one solution with all spatial Sobolev orders. Repeatedly solving the normally monic equation for its highest derivative gives every time derivative, hence a smooth solution. Approximate general \(f\) in \(L^1H^s\) and each \(\phi_j\) in its exact weighted space by these smooth data. Estimate (HC8) makes their entire jet vector Cauchy in the required continuous norms. The limit solves the equation distributionally and has the prescribed traces. The same estimate proves uniqueness.

## 5. Strict hyperbolicity relative to a level function

Let \(P\) be a scalar differential operator of order \(m\) on a smooth manifold \(X\), with principal symbol \(p\). It is **strictly hyperbolic relative to \(\phi\)** if
\[
 p(x,d\phi(x))\ne0
\]
and, whenever \(\xi\) is not a multiple of \(d\phi(x)\), the equation
\(p(x,\xi+\tau d\phi(x))=0\) has \(m\) distinct real roots. The first condition makes each level noncharacteristic and implies \(d\phi\ne0\). Dividing locally by the nonzero leading normal coefficient gives a monic polynomial with real coefficients, since its roots are real. This also supplies a real representative of the principal symbol for Hamiltonian propagation.

Choose a vector field \(v\) with \(v\phi=1\), and use its integral curves as a product coordinate with \(t=\phi\). Then \(v=\partial_t\). Data \(v^ju|_{t=0}=\psi_j\) correspond to \(D_t^ju(0)=(-i)^j\psi_j\). If another transverse field \(v'\) also satisfies \(v'\phi=1\), its difference from \(v\) is tangent to the levels. Iterating the full product rule gives
\[
 \psi'_j=\psi_j+\sum_{k<j}B_{jk}\psi_k,\qquad
 \operatorname{ord}(B_{jk})\le j-k. \tag{HC36}
\]
Induct on \(j\): one new tangent derivative raises tangential order by at most one, while a normal derivative raises the jet index by one and differentiates every coefficient as well. The highest normal term remains \(v^j\), so the diagonal is the identity. Each lower term maps \(H^{s+m-1-k}\) into \(H^{s+m-1-j}\), preserving the weighted data class. This retains the actual lower coordinate terms without treating noncommuting vector fields as a binomial formula.

On a compact coordinate patch normalize the operator to monic form. Choose \(0\le\chi\le1\), equal to one on the smaller required patch, and extend the roots by
\[
 \widetilde\lambda_j=\chi\lambda_j+(1-\chi)j|\xi|.
\]
Every adjacent gap is a convex combination of two positive gaps, so strict separation persists uniformly. Extend the remaining lower-order coefficients to agree with the original full symbols on the smaller patch and to have bounded seminorms globally. The resulting operator is differential in \(t\) and pseudodifferential in \(x\); it need not be differential in every variable outside the patch. The global Cauchy theorem now supplies local solutions for the original differential equation.

**Local mixed Cauchy statement.** If \(Y\Subset X\) is a product patch, \(r\ge0\),
\[
 f\in\overline H^{(r,q)}(\mathbb R_+\times\mathbb R^n),\qquad
 \phi_j\in H^{r+q+m-1-j},
\]
then one can solve \(Pu=f\) on \(Y\cap\{t>0\}\), with the prescribed jets on \(Y\cap\{t=0\}\), and obtain
\[
 u\in\overline H^{(r+m-1,q)},\qquad
 D_t^ju\in C_tH^{r+q+m-1-j}\quad(j<m). \tag{HC14}
\]
First \(f\in L^2_tH^{r+q}_x\subset L^1_tH^{r+q}_x\) on a finite slab. Solve at \(s=r+q\). The complete jet norm gives \(u\in\overline H^{(m-1,r+q)}\). For the actual differential operator on \(Y\), the proved differential theorem (HC48) gives the remaining normal regularity. It says that
\[
 u\in\overline H^{(r_1,q_1)}_{\mathrm{loc}},\quad
 Pu\in\overline H^{(r_2-m,q_2)}_{\mathrm{loc}}
 \Longrightarrow u\in\overline H^{(a,b)}_{\mathrm{loc}}
\]
provided \(a\le r_2\), \(a+b\le r_1+q_1\), and \(a+b\le r_2+q_2\). There is no additional \(a\le r_1\) condition. Here take \((r_1,q_1)=(m-1,r+q)\), \((r_2,q_2)=(r+m,q)\), and \((a,b)=(r+m-1,q)\). All three inequalities hold. We apply this differential input to the original operator on its agreement patch, rather than to its tangential pseudodifferential extension on the whole space. Local cutoffs yield the requested restricted solution.

## 6. Supported local solutions, one-sided uniqueness and semiglobal existence

**Companion local restricted-source statement.** This is a separately proved consequence of the mixed-space inputs and global Cauchy theorem. Proposition 23.2.6 itself uses the supported spaces, whose proof follows separately below. For an arbitrary source \(f\in\overline H^{(r,q)}\) on the half-space, and any real \(r,q\), one can find \(u\in\overline H^{(r+m-1,q)}\) solving \(Pu=f\) on the requested smaller patch. No Cauchy jets are prescribed in this statement. We first prove the corresponding local whole-space construction and then restrict it.

Choose the common extension (HC41), proved above from the one-sided programme multipliers. Let \(J_r^-\) have symbol \((\langle\xi\rangle-i\tau)^r\), using the continuous complex power in the right half-plane. Its modulus is \(\langle(\tau,\xi)\rangle^r\). Both it and its inverse have backward normal support, so they act on restrictions to \(t>0\). That input says
\[
 \begin{aligned}
 g&=J_r^-f\in L^2_tH^q_x(\mathbb R_+\times\mathbb R^n),\\
 F&=E_rf:=(J_r^-)^{-1}(H(t)g),\\
 \|F\|_{H^{(r,q)}}&=\|g\|_{L^2_tH^q_x}=\|f\|_{\overline H^{(r,q)}}.
 \end{aligned} \tag{HC28}
\]
Zero extension of \(g\) is legitimate in \(L^2\) in time. On restriction, the inverse identity gives \(F=f\). The operators commute with every spatial Fourier weight. Consequently the *same* \(E_r\), independent of \(q\), preserves every tangential order present in \(f\); it also preserves their intersection when \(q=+\infty\). This avoids selecting different whole-space extensions at different orders. Choose a smooth compact temporal cutoff equal to one on a slightly larger requested product patch. Multiplication by this cutoff preserves every real mixed order: its Fourier convolution has arbitrarily rapid decay in the normal variable, while the ratio of shifted Fourier weights has at most polynomial growth. A compact spatial localization has the same boundedness. These localizations supply a compactly based source \(F\), without asserting that it is supported in the forward half-space.

When \(r\ge0\), \(F\in L^2_tH^{r+q}_x\). Start the global extended Cauchy problem before its compact temporal support, with zero jets, and use the global theorem at \(s=r+q\). On the larger agreement patch the solution lies in \(H^{(m-1,r+q)}\). The differential normal-recovery input of Section5, now used in a whole-space local chart, upgrades it to \(H^{(r+m-1,q)}\). Its proof is the same normal-recovery identity before taking a quotient: no boundary restriction or trace endpoint is involved. Thus the whole-space local statement holds for nonnegative normal order.

For negative \(r\), choose an integer \(N\) with \(r+N\ge0\) and descend one normal order at a time. On the whole space use the exact Fourier decomposition
\[
 F=F_0+D_tF_n,\qquad
 F_0=\langle D_x\rangle^2\langle(D_t,D_x)\rangle^{-2}F,
 \qquad F_n=D_t\langle(D_t,D_x)\rangle^{-2}F. \tag{HC22}
\]
The identity follows from \(\langle(\tau,\xi)\rangle^2=\tau^2+\langle\xi\rangle^2\). The exact ratios of target to input weighted multipliers are \(\langle\xi\rangle/\langle(\tau,\xi)\rangle\) for \(F_0\in H^{(r+1,q-1)}\), and \(\tau/\langle(\tau,\xi)\rangle\) for \(F_n\in H^{(r+1,q)}\); both have modulus at most one. This decomposition need not preserve forward support.

At the inductive order obtain \(u_0\in H^{(r+m,q-1)}\) and \(u_n\in H^{(r+m,q)}\) for these two sources on a slightly larger agreement patch. With \(U=u_0+D_tu_n\), the error is \([P,D_t]u_n\). Its term of normal degree \(k<m\) has spatial order at most \(m-k\); hence it has normal order at least \(r+1\) and total mixed order \(r+q\). It belongs to \(H^{(r+1,q-1)}\). Multiply the locally computed error by a cutoff supported in the larger patch and equal to one on a smaller patch. This gives a whole-space source in that class. Apply the inductive construction to it and subtract the correction \(v\in H^{(r+m,q-1)}\), which embeds in \(H^{(r+m-1,q)}\). Then \(P(U-v)=F\) on the smaller patch.

There are finitely many descending steps. Choose their nested agreement patches in advance, with every cutoff equal to one on the next one. Differential locality makes all cutoff errors vanish on the final requested patch. Cut off the final solution only after its equation there has been obtained, and then restrict to the half-space. This gives the stated restricted solution. Unlike the separate supported construction below, it uses an arbitrary whole-space extension and does not claim forward support. For finite \(r\) and \(q=+\infty\), use this one extension, the same finitely many nested cutoffs and the same Fourier decomposition at every tangential order. Each global Cauchy solve has the same source and zero jets; energy uniqueness at a common lower Sobolev order identifies its higher-order realizations. This identifies the complete finite descent as well, including each cutoff correction.

For \(r=+\infty\) and any fixed finite \(q\), first observe that \(f\in\overline H^{(0,Q)}\) for every finite \(Q\). Indeed choose a finite nonnegative \(r'\) with \(r'+q\ge Q\) and apply the mixed embedding inequalities. Use the single extension \(E_0\) and solve the zero-jet global problem at all spatial orders. The resulting local solution lies in \(H^{(m-1,Q)}\) for every \(Q\). For each finite requested normal order \(r\ge0\), apply differential recovery on the agreement patch with original pair \((m-1,Q)\), source pair \((r+m,q)\), and target \((r+m-1,q)\), choosing \(Q\ge r+q\). The exact inequalities are \(r+m-1\le r+m\), \(r+m-1+q\le m-1+Q\), and \(r+m-1+q\le r+m+q\). Thus this *one* solution has all requested normal orders; lower normal orders follow by embedding. When both indices are infinite, make this argument for every finite \(q\). No all-orders extension across the boundary or additional initial jets are being presumed.

**Supported local solution.** A source in \(\dot H^{(r,q)}\), for arbitrary real \(r,q\), has a local solution in \(\dot H^{(r+m-1,q)}\). The statement also has its all-orders interpretation when either order is \(+\infty\).

For \(r\ge0\), start the Cauchy problem at a level below the support, with all initial jets zero. Energy uniqueness makes the solution zero before the source begins. The preceding differential mixed recovery applies also across the beginning level: the solution has zero matching jets, so no boundary delta appears in its whole-space derivatives there. A compact cutoff inside the agreement patch retains closed forward support and gives the supported local solution.

For \(r<0\), the proved support-retaining decomposition (HC44) gives
\[
 f=f_0+D_tf_n,\quad
 f_0\in\dot H^{(r+1,q-1)},\quad
 f_n\in\dot H^{(r+1,q)}. \tag{HC15}
\]
It uses the one-sided symbol \((\langle\xi\rangle+i\tau)^a\langle\xi\rangle^b\), so support is part of the input. Assume the statement at \(r+1\), after finitely many steps starting at a nonnegative order. Obtain \(u_0\in\dot H^{(r+m,q-1)}\), \(u_n\in\dot H^{(r+m,q)}\) solving the respective equations. Set \(U=u_0+D_tu_n\). Then
\[
 PU-f=[P,D_t]u_n.
\]
The commutator has total order at most \(m\), but normal order at most \(m-1\), since the leading normal coefficient is one. A term of normal degree \(k\le m-1\) has spatial degree at most \(m-k\). Its action on \(u_n\) has normal order \(r+m-k\ge r+1\) and total mixed order \(r+q\). It therefore belongs to \(\dot H^{(r+1,q-1)}\). Solve for this error at the inductive order and subtract the correction. Its class \(\dot H^{(r+m,q-1)}\) embeds into \(\dot H^{(r+m-1,q)}\). The support is retained at each step. For finite \(r\) and \(q=+\infty\), the source is already one whole-space supported distribution at every tangential order. Choose the same one-sided decomposition, nested cutoffs and global zero-jet Cauchy solves for each finite step. Their realizations at different Sobolev orders agree by global energy uniqueness, so the finite correction produces one all-tangential-order supported solution. For \(r=+\infty\), mixed embedding gives the original supported source in \(L^2_tH^Q_x\) for every \(Q\). Solve once at every spatial order with zero jets at a level before its support; these global solutions again agree. On the differential agreement patch, apply full-space normal recovery with the three inequalities already checked in the restricted companion construction for every finite requested normal order. The source and solution are zero on the past side, so this recovery includes the initial level and preserves the whole-space supported class. A final compact cutoff preserves it too. This proves both infinite-index variants without substituting a quotient-space decomposition for the support-retaining one.

**One-sided local distribution uniqueness.** Every point has a neighborhood basis \(V\) such that \(Pu=0\) in \(V\) and \(\operatorname{supp}u\subset\{\phi\ge\phi(x_0)\}\) imply \(u=0\) in \(V\), for arbitrary distributions there.

Choose coordinates with
\(\phi=\phi(x_0)+t-|x|^2\), and take
\(V_\epsilon=\{|t|<\epsilon^2,|x|<\epsilon\}\). For small \(\epsilon\), the flat \(t\)-levels remain strictly hyperbolic, by compact continuity of the simple-root condition. For \(g\in C_c^\infty(V_\epsilon)\), the supported local construction for the adjoint in reverse time gives a smooth \(w\) with \(P^*w=g\), zero when \(t>\epsilon^2-\delta\), for some \(0<\delta<\epsilon^2\). The joint support of \(u,w\) lies in
\[
 0\le|x|^2\le t\le\epsilon^2-\delta.
\]
This is a compact subset of \(V_\epsilon\). Choose \(\eta\in C_c^\infty(V_\epsilon)\) equal to one near that joint support and \(\operatorname{supp}g\). The differential commutator \([P^*,\eta]w\) has support disjoint from \(\operatorname{supp}u\). Therefore the legitimate compact test \(\eta w\) gives
\(0=(Pu,\eta w)=(u,g)\). Every compact test \(g\) is arbitrary, hence \(u=0\). The compact cutoff is essential: a locally defined adjoint solution cannot be paired directly with an arbitrary distribution unless its joint support is controlled.

**Semiglobal theorem.** Set \(X_+=\{\phi>0\}\), \(X_0=\{\phi=0\}\), and let \(Y\Subset X\). If \(f\in H^s_{\mathrm{loc}}(X)\) is supported in \(\overline X_+\), there is \(u\in H^{s+m-1}_{\mathrm{loc}}(X)\), supported in \(\overline X_+\), with \(Pu=f\) in \(Y\). If \(s\ge0\), \(v\phi=1\), \(f\in\overline H^s_{\mathrm{loc}}(X_+)\), and \(\psi_j\in H^{s+m-1-j}_{\mathrm{loc}}(X_0)\), there is \(u\in\overline H^{s+m-1}_{\mathrm{loc}}(X_+)\) solving the equation in \(Y\cap X_+\) and \(v^ju=\psi_j\) on \(Y\cap X_0\), for \(j<m\).

Here is the full patching mechanism. Choose a compact neighborhood \(K\Subset X\) of \(\overline Y\), and a finite system of local solution patches covering it. Near the current level \(\phi=c\), refine the one-sided uniqueness neighborhoods \(V_a\) so that every intersecting pair \(V_a,V_b\) is contained in one common solution patch. On each \(V_a\), one-sided uniqueness identifies whichever local solutions were chosen there. On \(V_a\cap V_b\), compare each with the solution in their common patch. Thus they actually agree and glue to a solution \(w\) on the union \(V\).

The refinement can be chosen before selecting the local solutions. Cover the compact current level set by finitely many smaller coordinate neighborhoods whose closures lie in solution patches. A Lebesgue number for this finite compact cover gives a radius such that each sufficiently small coordinate cluster lies in one solution patch. Choose the curved uniqueness neighborhoods with closures inside clusters of less than one sixth of this radius, shrinking uniformly over the finitely many coordinate charts. Two intersecting neighborhoods have union in one cluster of less than the full radius; hence they have the stated common solution patch. Comparison with its supported solution is legitimate on each whole uniqueness neighborhood, so overlap equality follows from actual one-sided uniqueness, rather than from an assertion that arbitrary local solutions agree.

Choose \(\eta\in C_c^\infty(V)\) equal to one near the compact current level set in \(K\). The new residual \(f-P(\eta w)\) is zero below \(c\) by support and zero in a band above \(c\) by the equation. The finite coordinate margins and strict-root constants persist when \(c\) varies in the compact interval \(\phi(K)\); shifting a level changes neither \(d\phi\) nor those constants. Hence a finite cover gives one positive band width \(\delta\) that works at every needed level. Multiply the residual by a fixed compact cutoff equal to one near \(\overline Y\) to define it globally without losing its support or local regularity. Solve this residual above \(c+\delta\), cut off again, and repeat. After at most \(1+\lceil(\max_K\phi-c)/\delta\rceil\) steps the residual vanishes on \(Y\). All residual regularity used here is retained: \([P,\eta]\) has order at most \(m-1\), so it maps \(H^{s+m-1}\) to \(H^s\). Every cutoff equals one near the current compact level set, so the residual is actually zero in a neighborhood of that level within the fixed compact region used by the next source cutoff. Its zero past extension therefore has the asserted supported regularity. With prescribed jets, perform this first cancellation in the bar spaces; after the residual vanishes on a full initial collar its zero extension has the same regularity, and the supported construction applies. Only finitely many fixed charts, nested margins and cutoffs occur. The finite sum of corrections is the desired solution. With prescribed jets, only the first step uses the local Cauchy construction; later corrections start a positive distance above \(X_0\) and leave every initial jet unchanged. The equation is asserted on \(Y\), and neither uniqueness nor an equation on all of \(X\) is inferred.

## 7. Improve every factor to a spatially smoothing error

The branch factorization can be refined without imposing stronger classical hypotheses:
\[
 P-(D_t-\widetilde A_j)\widetilde Q_j=\widetilde R_j,
 \quad \widetilde R_j\in S^{-\infty},
 \quad \widetilde A_j-A_j\in S^0,
 \quad \widetilde Q_{jk}-Q_{jk}\in S^{m-2-k}. \tag{HC16}
\]
Fix a branch and suppress its index. At step \(\mu\ge1\), assume \(R\in S^{m-\mu}\). If \(a,q_k,r\) denote the current symbols, the tangential expression
\[
 h=\sum_{k<m}q_k a^k
\]
is elliptic of order \(m-1\), with principal value \(p_\tau(\lambda)\). Choose a reciprocal with the usual high-frequency cutoff and put \(\ell=-r/h\in S^{1-\mu}\) at the leading required order. The leading normal polynomial of \(B=R+\ell Q\) now vanishes at \(\tau=\lambda\). Replace \(A\) by \(A+\ell\).

For \(m\ge2\), divide \(B=\sum_{l<m}B_lD_t^l\) exactly on the left by \(D_t-A-\ell\). Its quotient correction \(S=\sum_{k<m-1}s_kD_t^k\) is determined by
\[
 s_{m-2}=B_{m-1},\qquad
 s_{l-1}=B_l-D_ts_l+(A+\ell)s_l\quad(l=m-2,\ldots,1). \tag{HC17}
\]
Products here are operator compositions. The symbol orders are \(s_k\in S^{m-1-k-\mu}\). Put \(Q_{\mathrm{new}}=Q+S\). The exact defect is
\[
 R_{\mathrm{new}}=B-(D_t-A-\ell)S.
\]
It has no positive normal powers. Its leading tangential symbol is the remainder of the leading polynomial at \(\lambda\), already canceled, so it belongs to \(S^{m-\mu-1}\). For \(m=1\), \(Q=I\) and \(\ell=-R\) cancels the defect directly; there is no quotient correction.

Repeat for every \(\mu\). The corrections to \(A\) have orders \(0,-1,-2,\ldots\), and those to \(Q_k\) have orders \(m-2-k,m-3-k,\ldots\). The AN-03 asymptotic-sum construction, using seminorms of every base derivative through the coefficient index, gives actual uniformly bounded symbols with these expansions. For any finite requested order, compare their product with the corresponding finite-stage factorization; the remaining tails make its defect lower than that order. Thus the actual final remainder belongs to every spatial negative order. To retain an exactly tangential defect, after summing the corrections to \(A\), recompute every coefficient of \(\widetilde Q\) by the exact finite recursion (HC35) with this final \(\widetilde A\). Compare it with each finite-stage quotient, descending in the normal degree. For any prescribed \(L\), choose the stage far enough out that \(\widetilde A-A^{(N)}\), with every required parameter derivative, has order below \(-L-2m\). The finite recursion, ordinary product bounds and its coefficient time derivatives then put each difference \(\widetilde Q_k-Q_k^{(N)}\) below order \(-L-m\), and the resulting tangential remainder difference below \(-L\). The finite-stage remainder has order \(m-N\); choosing \(N>L+m\) makes the final one order below \(-L\). Since \(L\) is arbitrary, it is spatially smoothing. This recomputation keeps exactly \(\widetilde Q_{m-1}=I\), exactly cancels all positive normal powers, and preserves the previously constructed asymptotic quotient coefficients and their full parameter bounds.

The error remains an operator family, and is not asserted to vanish exactly. Its spatial smoothing property alone says nothing about arbitrary pure temporal singularities.

## 8. Local forced propagation along the simple branches

Choose a real normalized principal symbol \(p\) as in Section 5. For a differential equation \(Pu=f\), ordinary elliptic regularity gives
\[
 \operatorname{WF}(u)\setminus\operatorname{WF}(f)\subset p^{-1}(0).
\]
On each connected bicharacteristic segment avoiding \(\operatorname{WF}(f)\), membership in \(\operatorname{WF}(u)\) is constant. This is a local assertion, independent of whether a long characteristic escapes the chosen domain.

We give the additional steps needed beyond homogeneous first-order evolution. Localize \(u\) by a proper ordinary cutoff, compactly based, equal to one on a smaller cone at a selected characteristic covector and zero in a cone about pure normal covectors \((\tau,0)\). The latter are noncharacteristic for the monic differential operator. The new compact distribution \(v\) has no pure temporal wavefront direction, and \(g=Pv\) is regular on the selected smaller cone: the ordinary commutator of \(P\) and the cutoff has microsupport outside it, modulo a full smoothing remainder.

A compact distribution with this absence of pure temporal wavefront has actual time slices in a uniform negative spatial Sobolev space. To see it, split its Fourier transform into \(|\tau|>C\langle\xi\rangle\), where it is rapidly decreasing, and the remaining cone, where it has polynomial bound \(\langle(\tau,\xi)\rangle^N\). After \(k\) time derivatives, integrating in \(\tau\) bounds its partial inverse transform by \(C_k\langle\xi\rangle^{N+k+1}\). For one fixed \(r<-N-1-n/2\), dominated Fourier integration proves \(v\in C_t^kH^{r-k}_x\) for every \(k\). These slices agree with noncharacteristic pullback. The same cone split shows that a spatially smoothing family acts smoothly in spacetime on \(v\). A tangential operator of finite order preserves the no-pure-temporal property on a proper local patch: near its kernel diagonal use the ordinary/tangential composition with the nonnormal cone cutoff; away from the diagonal its spatially smooth kernel and the same Fourier estimates give all time derivatives.

Extend the localized differential operator to the bounded global simple-root model in Section 5. The coefficient agreement makes its discrepancy zero near the diagonal over \(\operatorname{supp}v\); the remaining spatially smoothing kernel acts smoothly on \(v\). Factor it using (HC16). At the selected branch, \(Q_j\) is ordinarily elliptic and
\[
 (D_t-A_j)w=g-R_jv,\qquad w=Q_jv. \tag{HC18}
\]
The residual is now genuinely smooth. The ordinary/tangential cutoff theorem justifies the ordinary elliptic test for \(Q_j\) away from \(\xi=0\).

The scalar source \(s=g-R_jv\) in (HC18) may be regular near the chosen characteristic while singular at other normal frequencies over the same spatial direction. A spatial test would see those frequencies. Remove them first. Shrink to a short compact transported spatial tube \(\Gamma\), with two larger tubes around its closure. Source regularity gives an open conic neighborhood of the entire characteristic graph over the largest of these tubes. Choose a full spacetime cone cutoff \(\theta\) equal to one on a smaller neighborhood of \(\tau=\lambda_j(t,x,\xi)\), supported in that known regular neighborhood. Its transition region is also a region where \(s\) is regular. Compactness and the no-pure-temporal condition give \(C\) such that every wavefront direction of the relevant compact inputs has \(|\tau|\le C\langle\xi\rangle\). Choose a bounded-slope cutoff \(\kappa\) equal to one for these slopes and supported in a larger bounded-slope cone. Choose a spatial conic cutoff \(\chi\) equal to one on the middle transported tube and supported in the largest one. Each cutoff has nested base supports inside the proper agreement patch.

On this bounded-slope cone, \(L=D_t-A_j\) is an ordinary operator with real principal symbol \(\tau-\lambda_j\). The support of \((1-\theta)\kappa\chi\) is separated from its characteristic set. Ordinary conic composition and its full remainder correction give an order-minus-one operator \(B\), properly supported, with leading symbol
\[
 b_{-1}=\frac{(1-\theta)\kappa\chi}{\tau-\lambda_j}, \tag{HC29}
\]
and the microlocal parametrix identity on this support. All correction symbols can be supported in the same elliptic region, with slightly nested margins. Thus \(B\) is smooth microlocally on a smaller characteristic tube. Where \(\theta=0\) and \(\kappa=\chi=1\), \(LB=I\) modulo full smoothing; where \(\theta\) varies, \(s\) was already regular. Put \(h=Bs\) and \(w_1=w-h\). Then \(h\) is regular on the selected characteristic arc, while \(g_1=Lw_1=s-LBs\) is regular at every bounded-slope covector over \(\Gamma\): near the characteristic graph and the transition region this follows from source regularity and pseudolocality, and in the remaining elliptic region it follows from the parametrix identity. At high slopes it follows from the no-pure-temporal property. Proper-support and cutoff remainders have full smoothing kernels or microsupport outside the smaller tube. Tangential nonlocal composition contributes spatially smoothing terms; the compact Fourier bound from the preceding paragraph makes those terms fully smooth here. Consequently every properly localized tangential test supported in \(\Gamma\) maps \(g_1\) to a fully smooth spacetime function. The argument establishes regularity over *all* normal frequencies seen by this test, rather than just regularity at one characteristic covector.

Construct such a test \(\Phi\) commuting with \(L\) modulo spatial smoothing. Its leading transport equation is
\[
 (\partial_t-H_{\lambda_j})\phi_0=0.
\]
For the general nonclassical lower-order symbol, proceed by orders rather than homogeneous coefficients. If the current exact commutator has symbol \(r_N\in S^{-N}\), solve
\[
 (\partial_t-H_{\lambda_j})\phi_N=-i r_N
\]
along the real flow, with zero initial value for \(N\ge1\). The principal commutator is \(-i(\partial_t-H_{\lambda_j})\phi_N\), so this cancels \(r_N\). All other terms gain one order: the scalar zero-product terms commute, \(A_j-\lambda_j\) has order zero, and frequency derivatives in the finite composition expansion lower the order. Induction gives a full test by parameter-aware asymptotic summation. Its microsupport follows the short transported tube, and its smoothing/proper-support errors remain explicitly in the equation.

Before passing to a slice, apply ordinary elliptic regularity to \(Lw_1=g_1\). Since \(g_1\) is smooth over the entire smaller spatial tube, every wavefront covector of \(w_1\) there has \(\tau=\lambda_j\). Pure temporal wavefront has already been excluded. If the starting spacetime covector on this graph is regular, shrink its spatial cone: its graph lift is regular, and all other normal lifts are regular by that elliptic argument. The noncharacteristic pullback inclusion now gives a regular initial slice. This uses regularity of every normal lift above the chosen spatial direction; regularity of an isolated arbitrary spacetime covector would not suffice. Choose the initial spatial test elliptic there with smooth compactly localized initial output. The equation for \(\Phi w_1\) has smooth forcing: \(\Phi g_1\) is smooth by the previous source removal, and the retained smoothing kernels act smoothly on \(w_1\) by its no-pure-temporal property. First-order existence at every Sobolev order and uniqueness at one common lower order make \(\Phi w_1\) smooth in space; differentiated equations make it smooth in time too. Restart at any intermediate slice to get the converse implication from spatial regularity there to spacetime regularity. Reverse time to propagate regularity in the other direction. The singular set is closed, and this argument shows its complement open and transported along the arc; hence its intersection with a source-free connected arc is both open and closed.

On the branch \(\tau=\lambda_j\),
\[
 p=(\tau-\lambda_j)q_j,
 \qquad H_p=q_jH_{\tau-\lambda_j}. \tag{HC19}
\]
The factor \(q_j\) is real and nonzero. The same unparameterized arcs are therefore followed; its sign may reverse their Hamiltonian parameter. Transfer the scalar conclusion through the elliptic \(Q_j\) and the original cutoff. This proves the strictly hyperbolic local propagation theorem, without claiming the later general real-principal-type theorem.

## 9. Boundary equality, intrinsic jets and the domain of forward propagation

Let \(X_+=\{\phi>0\}\), with initial surface \(X_0=\{\phi=0\}\). Assume that the interior solution is extendible across that surface and that
\[
 Pu=f\text{ in }X_+,\qquad f\in\mathcal N(\overline X_+).
\]
Here \(\mathcal N\) is the dual conormal class \(\mathcal A'\) whose compressed boundary wavefront lies in the embedded nonzero tangential cotangent bundle. The exact noncharacteristic extension input gives the unique \(\mathcal N\) representative of \(u\), and the intrinsic normal jets have the corresponding dual extensions. With \(v\phi=1\), let \(\psi_j=(v^ju)|_{X_0}\). These are genuine intrinsic traces. In a flat chart,
\[
 D_t(Hu)=H(D_tu)-i\,u|_{t=0}\otimes\delta(t),
\]
so the intrinsic derivative of its supported representative is the raw derivative plus \(i\,u|_{t=0}\delta(t)\). Retain this correction whenever derivatives or Green identities use supported representatives.

We need the intrinsic jets in \(\mathcal N\), rather than only in \(\mathcal A'\). Here is the precise use of the existing differential forward wavefront input. The intrinsic derivative acts weakly continuously on \(\mathcal A'\): its transpose is the ordinary differential map on the filtered conormal tests. Smooth boundary functions are weakly dense in this dual topology. Therefore the full local commutator formula, initially on smooth functions, extends to the intrinsic action. If \(B_b\) is a proper totally characteristic test with compressed symbol \(b(x,t;\xi,\zeta)\), it is
\[
 [\nabla_t^{\mathrm{int}},B_b]
   =B_{D_tb}+B_{D_\zeta b}\nabla_t^{\mathrm{int}},
 \qquad D_\zeta=-i\partial_\zeta. \tag{HC23}
\]
Its second normal term must be retained. Tangential derivatives have just their coefficient derivative commutator. For a precise verification, first compute this identity in the open interior, where the intrinsic derivative is the usual derivative and the complete symbol computation applies. Every displayed term extends to the dual class: use [CNF J3–J4](../20261005-conormal-test-foundations/dual-conormal-distributions-and-jets.md) for intrinsic differentiation and [GB D1](../20261005-global-boundary-operators/global-boundary-operator-calculus.md) for the full operator action. The difference of the two sides lies in \(\mathcal A'\) and restricts to zero. The proved interior injectivity of that class, CNF U3, makes the difference zero. Thus the raw supported commutator has not been transferred by discarding a boundary delta.

At a compressed covector outside \(\operatorname{WF}_b(u)\), the conic parametrix and residual localization in AN-03 let us choose an order-zero test whose symbol is, modulo residual terms, independent of the base variables on a small neighborhood and supported in the known regular cone, and elliptic at that covector. Its output belongs to \(\mathcal A\) and to \(\mathcal A'\), hence is smooth there. The coefficient derivative in (HC23) is residual on that smaller base patch; its full localized action is smooth by the proved residual map and dual/conormal intersection. Proper-support and cutoff discrepancies are residual there and act smoothly on the dual distribution. Rearranging the complete normal identity gives
\[
 (B_b+B_{D_\zeta b})\nabla_t^{\mathrm{int}}u
      =\nabla_t^{\mathrm{int}}(B_bu)
         \quad\text{modulo smooth localized terms}. \tag{HC24}
\]
The new test has the same order-zero principal symbol as \(B_b\), since \(D_\zeta b\) has order minus one. It is elliptic at the candidate and its output is smooth. Thus the intrinsic derivative has no wavefront there. The tangential argument is the same with no extra normal term. Multiplication by smooth coefficients preserves the dual class and forward wavefront inclusion. We obtain
\[
 \operatorname{WF}_b(vu)\subset\operatorname{WF}_b(u),
 \qquad vu\in\mathcal A',
 \qquad u\in\mathcal N\Longrightarrow v^ju\in\mathcal N
       \quad\text{for every }j\ge0. \tag{HC25}
\]
The vector field acts intrinsically here. The interior injectivity of the dual extension identifies these iterated derivatives with the canonical extensions of the corresponding interior derivatives. Proper tangential coefficients preserve \(\mathcal N\), so every \(Q_ju\) also belongs to that class. This verifies the exact jet hypothesis in the boundary argument; it does not treat the higher-order companion system as an ordinary elliptic boundary system.

**Boundary wavefront equality.** On the embedded tangential bundle,
\[
 \operatorname{WF}_b(u)|_{X_0}
 =\operatorname{WF}_b(f)|_{X_0}
     \cup\bigcup_{j=0}^{m-1}\operatorname{WF}(\psi_j). \tag{HC20}
\]
The forward differential action and the exact intrinsic trace inclusion give the inclusion from right to left. They retain every normal commutator term; ordinary restriction of an arbitrary ambient extension is not a substitute.

For the reverse inclusion, choose a boundary tangential covector outside the right-hand side. Work in a compact product patch with \(v=\partial_t\), and proper-localize the actual \(\mathcal N\) representative. The exact tangential action preserves \(\mathcal N\), and a spatially smoothing symbol has no boundary wavefront. For such an output, compactness of the compressed cosphere and closedness give one sufficiently small collar with no interior wavefront either. The output is then conormal and dual conormal, so \(\mathcal A\cap\mathcal A'=C^\infty\) makes it smooth up to the boundary. This is the step that turns spatial smoothing into full smoothness here.

Use the refined factors and, for each branch, a scalar commuting test \(\Phi_j\), elliptic at the chosen initial covector, with its microsupport in an arbitrarily small transported cone. The boundary source is regular there. The exact tangential microsupport inclusion therefore makes \(\Phi_j f\) smooth in a smaller compact collar; the same argument applies to \(\Phi_jR_ju\) and \([D_t-A_j,\Phi_j]Q_ju\). All these terms belong to the dual conormal class before the smoothness upgrade. Thus
\[
 (D_t-A_j)(\Phi_jQ_ju)
\]
is smooth in that collar. The complete intrinsic trace action expresses \((Q_ju)(0)\) as \(\sum_{k<m}Q_{jk}(0)D_t^ku(0)\). Proper tangential tests with the chosen microsupport make this initial value smooth, since all initial jets are regular at the selected covector.

The first-order smooth Cauchy solution agrees with \(\Phi_jQ_ju\) even if the latter was initially only a dual distribution. We prove the necessary distributional uniqueness, including the spatial test topology. Extend the scalar symbol smoothly to a short time interval on both sides of zero. Zero-extend the difference between the distribution and the smooth Cauchy solution for \(t\ge0\). The intrinsic boundary-delta identity and its zero initial trace make the scalar equation homogeneous across zero. The distribution part has compact spatial output support; the smooth solution lies in every spatial Sobolev space. Their difference consequently acts continuously on smooth time-dependent spatial Schwartz tests on a compact temporal strip, with a finite number of seminorms.

For a compact smooth test forcing \(g\), solve the backward adjoint first-order equation \(L^*z=g\), with zero terminal value at \(T\), using the first-order theorem at every Sobolev order. We verify that \(z\) is Schwartz in space without assuming distributional uniqueness to identify an unbounded moment. For integer \(N\ge1\) take the bounded weights
\[
 w_R(x)=\langle x\rangle^N
                 (1+|x|^2/R^2)^{-N/2},\qquad R\ge1. \tag{HC26}
\]
They tend locally smoothly to \(\langle x\rangle^N\). Their positive-order derivatives satisfy
\(|\partial_x^\alpha w_R|\le C_{\alpha N}\langle x\rangle^{N-|\alpha|}\), uniformly in \(R\). For a bounded order-one symbol \(a\), the normalized commutator
\[
 [a(x,D_x),w_R]\langle x\rangle^{1-N}
                      \in S^0
       \quad\text{uniformly in }R. \tag{HC27}
\]
This is the usual ordinary product estimate with its zero-product term canceled. In the finite expansion every remaining term has a positive derivative of \(w_R\), a frequency derivative of \(a\), and the indicated inverse weight, so its base derivatives are uniformly bounded and its frequency order is at most zero. In the integral remainder the ratio \(\langle x+y\rangle^{N-1}/\langle x\rangle^{N-1}\) has at most \(C_N\langle y\rangle^{N-1}\) growth. Integrate by parts in frequency more than \(N+n+2\) times to absorb it and every fixed requested derivative. This gives the same uniform ordinary seminorm bounds for the actual remainder, rather than only a formal symbolic identity. The time derivatives of the symbol obey the identical estimate.

Assume all weights through \(N-1\) of \(z\) have every spatial Sobolev order, uniformly on the finite strip. The equation for the legitimate bounded-weight function \(w_Rz\) has source \(w_Rg+[L^*,w_R]z\). The first term is uniformly bounded in every Sobolev space because \(g\) is compact smooth; (HC27) and the inductive lower moment bound control the second uniformly in \(R\). Its terminal value is zero. The ordinary first-order energy estimate therefore bounds \(w_Rz\) in every continuous spatial Sobolev norm uniformly in \(R\). Here is the complete limit argument, using [Fatou's inequality M3](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md). The unweighted all-orders construction already makes \(z(t,\cdot)\) smooth. For each fixed time and each nonnegative integer \(k\), all derivatives through \(k\) of \(w_Rz\) converge locally pointwise to those of \(\langle x\rangle^Nz\). Apply Fatou to the nonnegative finite sum of their squared moduli. The integer Sobolev norm is equivalent to this derivative sum by the Fourier binomial formula, so the uniform \(H^k\) energy bound gives an \(H^k\) bound for the limit, with a constant independent of time. Arbitrary real orders follow by embedding from larger integers. Distributional identification is the same local convergence. No subsequence or weak-compactness theorem is required. To obtain strong measurability, approximate this weighted vector by smooth spatial cutoffs: each cutoff is continuous into every spatial Sobolev space, and the cutoffs converge at each time in that space by the usual derivative-sum cutoff estimate. Their pointwise limit is strongly measurable. The commutator and equation then supply its Bochner primitive at one lower order; identification in distributions supplies the representative, and using one additional spatial order gives continuity at every desired order. The equation then gives its time continuity and time derivatives in every Sobolev order by the weak primitive argument, retaining only already controlled lower moments in the commutator. Induct on \(N\), and use Sobolev embedding at arbitrarily large spatial order. We have proved every spatial Schwartz seminorm and every time derivative uniformly. No uniqueness assertion for an arbitrary tempered moment was used in this induction.

Choose \(g\) supported below some \(T_0<T\). The adjoint solution is zero on a neighborhood of \(T\), by energy uniqueness and zero terminal data. Multiply \(z\) by a smooth time cutoff which is one from zero through \(T_0\), whose lower derivative support lies strictly in \(t<0\), and whose upper derivative support lies in that zero terminal neighborhood. The lower commutator is disjoint from the zero-extended difference; the upper commutator is zero. The resulting compact-time Schwartz test is admissible for distributional adjoint pairing. It gives zero against \(g\). Every compact smooth \(g\) on the shorter strip was arbitrary, so the difference is zero there. Thus every \(\Phi_jQ_ju\) is smooth up to the boundary.

It remains to recover \(u\), rather than only its \(m\) quotients. Put
\[
 e_k=m-1-k,\quad z_k=\langle D_x\rangle^{e_k}D_t^ku,
 \qquad A_{jk}=\Phi_jQ_{jk}\langle D_x\rangle^{-e_k}. \tag{HC21}
\]
This is an ordinary tangential order-zero matrix. Its principal matrix at the chosen covector has entries
\(\phi_{j,0}c_{jk}/|\xi|^{e_k}\), where \(c_{jk}\) is the coefficient of \(\tau^k\) in \(q_j\). The polynomial interpolation identity proves that \((c_{jk})\) is invertible. Nonzero scalar row factors and column normalizations preserve invertibility; compactness and strict root separation give uniform inverse bounds on a smaller cone. The exact ordered ordinary matrix parametrix yields
\[
 C A=\Psi I+K,
\]
where \(\Psi\) is a tangential scalar test elliptic at the candidate and \(K\) is spatially smoothing on a smaller cone. Use one further conic cutoff to remove its off-cone microsupport. The exact \(\mathcal N\) tangential action makes the remaining errors smooth in a smaller collar, as above. The first row consequently gives a smooth elliptic tangential test of \(z_0\); compose with the inverse scalar Sobolev weight to obtain one of \(u\). The exact tangential tester criterion removes the candidate from \(\operatorname{WF}_b(u)\), proving (HC20). This concrete matrix argument uses the AN-03 order-zero parametrix, rather than a generalized elliptic boundary-system theorem for different hypotheses.

Interior propagation now traces singularities backward along each simple characteristic until forcing is encountered, the initial surface is reached, or the arc leaves the domain under consideration. If the backward segment stays in a compact part of the product domain until it reaches \(X_0\), every singularity arises from \(\operatorname{WF}(f)\) on that segment or from the inverse image of the right-hand side of (HC20) under restriction of full covectors to the boundary. Locally in a small such collar this is the union of the \(m\) forward characteristic branches from those sources. A global assertion requires this backward-access condition, or boundary data at every other incoming part of the domain.

For example, on \(X=(-1,1)_t\times(0,1)_x\), take \(\phi=t\), \(P=D_t-D_x\), and
\(u=\delta(x+t-3/2)\) in \(X_+\). This is an extendible distributional solution with \(f=0\). It is zero near every point of \(X_0\), so all initial jets and their boundary wavefronts are empty there. Nevertheless it is singular when \(t>1/2\) along \(x=3/2-t\). Its backward characteristic exits through \(x=1\) before it reaches \(t=0\). The local equality (HC20) holds, and the example shows why it cannot alone imply an unrestricted global domain-of-dependence conclusion.

## 10. Original graded exercises with complete solutions

**Exercise 1 — basic: normalize the roots.** Let \(p=\tau^3-4\xi^2\tau\), on \(\xi>0\). Find its ordered roots and the three quotient polynomials. Verify every interpolation identity for \(k=0,1,2\).

**Solution.** The roots are \(-2\xi,0,2\xi\). The quotients are
\(q_1=\tau^2-2\xi\tau\), \(q_2=\tau^2-4\xi^2\), and \(q_3=\tau^2+2\xi\tau\). Their values at their roots are \(8\xi^2,-4\xi^2,8\xi^2\). For \(k=0\), \((q_1+q_3)/(8\xi^2)-q_2/(4\xi^2)=1\). For \(k=1\), \((-q_1+q_3)/(4\xi)=\tau\). For \(k=2\), \((q_1+q_3)/2=\tau^2\). All three are identities of entire polynomials, rather than evaluations only at a selected branch.

**Exercise 2 — basic: every weighted row.** For general \(m\), compute the Sobolev shift of \(M_{kj}Q_ju\) and of \(B_{k\ell}D_t^\ell u\). Explain the one-derivative difference between the principal reconstruction and its error.

**Solution.** \(M_{kj}\) has order \(k+1-m\), so it maps \(H^s\) to \(H^{s+m-1-k}\). The remainder has order \(k-\ell-1\), so input \(H^{s+m-2-\ell}\) gives the same output \(H^{s+m-1-k}\). The leading polynomial interpolation is exact. Every nonleading term in the ordinary composition has at least one frequency derivative, hence loses one spatial order; this is exactly the weaker input norm needed in the remainder. Low-frequency cutoff errors are smoothing and satisfy these same maps.

**Exercise 3 — basic: coefficient time derivatives.** In one spatial dimension let \(A=tD_x\) and \(P=D_t^2-t^2D_x^2\). Compute \((D_t-A)(D_t+A)\) on an arbitrary smooth function and the resulting left-factor residual. Explain the domain of this symbol example.

**Solution.** The cross term is \([D_t,tD_x]=-iD_x\). Thus the product is \(D_t^2-t^2D_x^2-iD_x\), and \(P-(D_t-A)(D_t+A)=iD_x\). It has spatial order one. The principal roots \(\pm t|\xi|\) merge at \(t=0\); this example checks division and coefficient derivatives but is not strictly hyperbolic on an interval containing zero. On a compact interval separated from zero the roots are uniformly distinct. To use the global symbol hypotheses, extend the coefficient smoothly with bounded time derivatives and keep it separated from zero; the unbounded coefficient \(t\) on all of \(\mathbb R\) is not itself a bounded global symbol.

**Exercise 4 — intermediate: all Fourier signs for the wave equation.** Solve \((D_t^2-c^2D_x^2)u=f\) for constant \(c>0\), with \(D_tu(0)=\phi_1\), \(u(0)=\phi_0\). Give the solution for \(f=0\), and the contribution of \(\widehat f(t,\xi)=1\). Check both zero-frequency limits. For \(f=0\), also compute the two branch projections on a positive high-frequency cone and their weighted Sobolev orders.

**Solution.** The spatial Fourier equation is \(-\partial_t^2\widehat u-c^2\xi^2\widehat u=\widehat f\), and \(\partial_t\widehat u(0)=i\widehat\phi_1\). Therefore
\[
 \widehat u(t,\xi)=\cos(c\xi t)\widehat\phi_0
 +i\frac{\sin(c\xi t)}{c\xi}\widehat\phi_1
 -\int_0^t\frac{\sin(c\xi(t-r))}{c\xi}\widehat f(r,\xi)\,dr.
\]
For unit forcing its contribution is \((\cos(c\xi t)-1)/(c^2\xi^2)\). The removable limits are \(\widehat\phi_0+it\widehat\phi_1\) and \(-t^2/2\). Differentiating verifies both the equation and the two jets, including the forcing sign.

For the homogeneous solution, on a cone with \(\xi>0\) bounded away from zero, set
\[
 a_+=\tfrac12\widehat\phi_0+\frac{\widehat\phi_1}{2c\xi},\qquad
 a_-=\tfrac12\widehat\phi_0-\frac{\widehat\phi_1}{2c\xi},\qquad
 \widehat u_\pm=e^{\pm ic\xi t}a_\pm. \tag{HC30}
\]
Their sum is the cosine-sine formula. With \(q_+=D_t+cD_x\) and \(q_-=D_t-cD_x\),
\[
 \widehat u_+=\frac{\widehat{q_+u}}{2c\xi},\qquad
 \widehat u_-=-\frac{\widehat{q_-u}}{2c\xi}. \tag{HC31}
\]
Indeed \(q_+\) kills the negative branch and equals \(2c\xi\) on the positive branch; \(q_-\) kills the positive branch and equals \(-2c\xi\) on the negative branch. If \(\phi_0\in H^{s+1}\) and \(\phi_1\in H^s\), a smooth high-frequency cutoff followed by \(1/\xi\) has order minus one, so both projected branches belong to \(H^{s+1}\) and their \(D_t\) jets to \(H^s\). The individual split coefficients need not have limits at zero frequency; the combined sine formula has the removable limit already computed. On a negative-frequency cone the names of the increasingly ordered roots swap, while the formulas with their signed \(\xi\) remain valid.

**Exercise 5 — intermediate: why root gaps enter the estimate.** For normalized roots \(-\epsilon,\epsilon\), compute the quotient coefficient matrix and its inverse. Exhibit an associated positive quadratic form and its degeneration as \(\epsilon\to0\).

**Solution.** The two quotients are \(\tau-\epsilon\) and \(\tau+\epsilon\), so
\[
 C=\begin{pmatrix}-\epsilon&1\\\epsilon&1\end{pmatrix},
 \qquad C^{-1}=\begin{pmatrix}-1/(2\epsilon)&1/(2\epsilon)\\1/2&1/2\end{pmatrix}.
\]
The columns of the companion eigenvector matrix are \((1,-\epsilon)^T\) and \((1,\epsilon)^T\). Thus
\[
 V=\begin{pmatrix}1&1\\-\epsilon&\epsilon\end{pmatrix},\qquad
 V^{-1}=\begin{pmatrix}1/2&-1/(2\epsilon)\\1/2&1/(2\epsilon)\end{pmatrix},
 \qquad (V^{-1})^*V^{-1}
 =\operatorname{diag}(1/2,1/(2\epsilon^2)).
\]
This is a positive form in the normalized companion coordinates \((u,D_tu)\); its second coefficient exhibits the inverse gap squared. At either root \(|p_\tau|=2\epsilon\), so the uniform strictness hypothesis fails as \(\epsilon\to0\); uniform energy constants across this family are not promised. The quotient inverse \(C^{-1}\) and eigenvector inverse \(V^{-1}\) are different matrices and their quadratic forms should not be interchanged.

**Exercise 6 — intermediate: failure of the strict weighted estimate at a repeated root.** For \(P=(D_t-cD_x)^2\), take \(u(0)=0\), \(D_tu(0)=\phi_1\). Show that the order-two estimate with \(u(t)\in H^{s+1}\), \(D_tu(t)\in H^s\) cannot have a constant depending only on \(T,c,s\) and the initial \(H^s\) norm.

**Solution.** Its Fourier solution is \(\widehat u=it e^{ic\xi t}\widehat\phi_1\), and
\(D_t\widehat u=e^{ic\xi t}(1+ic\xi t)\widehat\phi_1\). Choose smooth Fourier data supported in \(N<\xi<N+1\), normalized to have \(H^s\) norm one. At any fixed \(t>0\), \(\|u(t)\|_{H^{s+1}}\) is at least a fixed multiple of \(tN\), while \(\|D_tu(t)\|_{H^s}\) grows like \((1+c^2N^2t^2)^{1/2}\) if \(c\ne0\). Even when \(c=0\), the first norm grows like \(tN\). The initial weighted norm is one. This disproves the strict theorem's weights after dropping simple roots; it does not prove that every multiple-root problem has no solution.

**Exercise 7 — basic: the weighted endpoints and their forcing norms.** Starting from (HC8), derive the weaker weighted-jet bound with unweighted \(L^1\) forcing for every \(1\le p\le\infty\). Then use (HC34) to derive the stronger (HC11), keeping its large-\(\lambda\) range and every endpoint. Explain why the first argument alone cannot give weighted forcing.

**Solution.** For finite \(p\), bound each jet by its supremum and compute \(\lambda\int_0^Te^{-p\lambda t}dt=(1-e^{-p\lambda T})/p\le1\). Taking its \(1/p\)-power and summing gives a weighted left-hand bound with right-hand side \(C_{s,T}(Y(0)+\int_0^T\|Pu\|_{H^s}dt)\). At infinity, \(\sup e^{-\lambda t}\|D_t^ku\|\le\sup\|D_t^ku\|\), with no prefactor. This uses the unweighted forcing norm present in (HC8).

For the stronger bound, multiply (HC34) by \(e^{-\lambda t}\). Its initial kernel is \(e^{-(\lambda-B_s)t}\), and the source kernel at time \(r\) is \(\mathbf1_{t\ge r}e^{-(\lambda-B_s)(t-r)}e^{-\lambda r}\|Pu(r)\|_{H^s}\). If \(\lambda\ge\max(1,2B_s)\), its normalized finite-\(p\) norm is at most \((\lambda/[p(\lambda-B_s)])^{1/p}\le2\), independently of \(r,T,p\); its infinity norm is at most one. Minkowski therefore gives exactly (HC11), with weighted forcing \(\int e^{-\lambda r}\|Pu(r)\|_{H^s}dr\). Applying the bound to each of the \(m\) jets contributes only a fixed factor \(m\) to the constant. The exponential Volterra kernel supplies this improvement; replacing it by an unweighted supremum discards the needed \(r\)-weight.

**Exercise 8 — intermediate: the whole Green form for order two.** Let \(P=D_t^2+B(t)D_t+C(t)\). Write every initial boundary term in (HC12), and expand the coefficient derivative in the adjoint normal expression.

**Solution.** The boundary sum is
\((u(0),B(0)^*v(0))+(u(0),D_tv(0))+(D_tu(0),v(0))\), multiplied by \(-i\). The adjoint is \(P^*=D_t^2+D_tB^*+C^*\), and in normal order
\(D_tB^*=B^*D_t+(D_tB^*)\). Here the coefficient derivative is \(-i\partial_tB^*\). The boundary term involving \(B\) has no time derivative for order two, while the reordered adjoint does. For higher orders the brackets \(D_t^k[P_l^*v]\) retain all their derivatives. Testing \(v(0)=0\) and arbitrary \(D_tv(0)\) identifies \(u(0)\); then arbitrary \(v(0)\) identifies \(D_tu(0)\) after that first cancellation.

**Exercise 9 — intermediate: trace threshold.** Compute the scaling of
\(\int_\mathbb R\tau^{2j}(a^2+\tau^2)^{-r}d\tau\), for \(a>0\), and find the exact convergence threshold. What is the trace Sobolev order after including a tangential weight \(a^{2q}\)?

**Solution.** Substitute \(\tau=a\sigma\). The integral is \(a^{2j+1-2r}\int_\mathbb R\sigma^{2j}(1+\sigma^2)^{-r}d\sigma\). Its tail is integrable exactly when \(2j-2r<-1\), or \(r>j+1/2\); equality diverges logarithmically. Cauchy–Schwarz in the normal Fourier variable therefore yields boundary order \(q+r-j-1/2\). For integer \(r=m\) and \(j<m\), the constant is \(\Gamma(j+1/2)\Gamma(m-j-1/2)/\Gamma(m)\). The endpoint is not part of the trace theorem.

**Exact constant, with its proof.** Define \(\Gamma(a)=\int_0^\infty x^{a-1}e^{-x}\,dx\) for \(a>0\). Near zero the power is integrable; the exponential bounds every power at infinity, so this is finite and positive, as in the included positive-order companion. For \(a,b>0\), Tonelli M4 and the one-dimensional substitution \(v=uy\), followed by \(w=u(1+y)\), give
\[
\begin{aligned}
\Gamma(a)\Gamma(b)
 &=\int_0^\infty\!\int_0^\infty
 u^{a-1}v^{b-1}e^{-u-v}\,dv\,du\\
 &=\int_0^\infty y^{b-1}
       \left(\int_0^\infty u^{a+b-1}e^{-u(1+y)}\,du\right)dy\\
 &=\Gamma(a+b)\int_0^\infty y^{b-1}(1+y)^{-a-b}\,dy .
\end{aligned}
\tag{HC53}
\]
These substitutions can first be made on compact positive intervals, using the proved one-dimensional change of variables; monotone convergence then gives the displayed improper positive integrals. P3 M8 identifies those compact integrals with the measure integrals. All exchanges are nonnegative, so no unproved cancellation or analytic continuation enters. In the trace constant, split at zero and put \(y=\sigma^2\). This gives \(\int_0^\infty y^{j-1/2}(1+y)^{-r}\,dy\). Taking \(b=j+1/2\) and \(a=r-j-1/2>0\) proves
\[
c_{r,j}=\frac{\Gamma(j+1/2)\Gamma(r-j-1/2)}{\Gamma(r)}
\quad (r>j+1/2).
\tag{HC54}
\]
This proves the stated integer case and its full real-order extension.

**Exercise 10 — intermediate: the mixed recovery inequalities.** In (HC14), verify all B.2.9 inequalities and explain why the target normal order may exceed the original one.

**Solution.** The original pair is \((m-1,r+q)\), the source pair in the theorem is \((r+m,q)\), and the target is \((r+m-1,q)\). Its normal order is at most \(r+m\); its total order equals the original total \(r+q+m-1\), and is one less than the source total \(r+q+m\). These are exactly the three required inequalities. For \(r>0\), the target normal order exceeds \(m-1\). The equation supplies this gain; an additional requirement that the target normal order not exceed the original one would incorrectly exclude the intended application.

**Exercise 11 — advanced: the negative-order correction.** Prove every mixed order used in the correction after (HC15), including the normal-order distinction for \([P,D_t]\).

**Solution.** Differentiating the coefficients of \(P=\sum P_kD_t^k\) gives \([P,D_t]=i\sum_{k<m}(\partial_tP_k)D_t^k\); the coefficient of \(D_t^m\) is constant and contributes zero. Each coefficient has spatial degree at most \(m-k\). Applied to \(u_n\in H^{(r+m,q)}\), the \(k\)-th term has normal order \(r+m-k\) and total order \(r+q\). Embedding into \((r+1,q-1)\) uses \(m-k\ge1\) and equal total orders. The inductive correction belongs to \((r+m,q-1)\), which embeds into \((r+m-1,q)\), again with equal totals and one more original normal order. Both \(u_0\) and \(D_tu_n\) lie in this last space; normal differentiation preserves closed half-space support, including its possible boundary distributions. Thus the final supported solution has exactly the requested order.

**Exercise 12 — intermediate: support makes the uniqueness pairing legal.** In the curved box, find a positive spatial margin for the joint support and explain every cutoff commutator in the adjoint pairing.

**Solution.** The joint support obeys \(|x|\le\sqrt{\epsilon^2-\delta}<\epsilon\), so its spatial margin is \(\epsilon-\sqrt{\epsilon^2-\delta}>0\). Its lower time margin is at least \(\epsilon^2\), and its upper time margin at least \(\delta\). It is compact in the open box. Choose \(\eta=1\) on a neighborhood of this set and of the test forcing support. Every term of the differential commutator contains a positive derivative of \(\eta\) and a derivative of \(w\), so its support lies where \(\eta\) varies and within \(\operatorname{supp}w\). That set is disjoint from \(\operatorname{supp}u\). Consequently \((u,[P^*,\eta]w)=0\), while \(\eta P^*w=g\). This justifies the compact test identity used in uniqueness.

**Exercise 13 — advanced: the correction sign in the smoothing factor.** At a symbolic stage let \(R\) have leading symbol \(r\) and \(Q\) have polynomial \(q(\tau)\). Find the sign of the correction to \(A\) and give the quotient correction polynomial at leading order.

**Solution.** Replacing \(A\) by \(A+\ell\) changes \(P-(D_t-A)Q\) to \(R+\ell Q\). Its value at the branch is \(r+\ell q(\lambda)\), so \(\ell=-r/q(\lambda)\). The quotient correction polynomial is \((r+\ell q(\tau))/(\tau-\lambda)\), of degree at most \(m-2\), because the numerator vanishes at \(\lambda\). It is added to \(Q\), rather than subtracted: the new defect is \(R+\ell Q-(D_t-A-\ell)S\). At operator level (HC17) retains coefficient derivatives and ordinary composition, and the residual drops one spatial order. For \(m=1\), \(q=1\), the numerator is zero and there is no quotient polynomial.

**Exercise 14 — advanced: normalize every quotient column.** For the cubic in Exercise 1, form the order-zero quotient matrix on \(\xi>0\), using \(z=(|\xi|^2u,|\xi|D_tu,D_t^2u)\). Find its inverse and recover all three jets.

**Solution.** With unit commuting principal row factors the matrix is
\[
 A=\begin{pmatrix}0&-2&1\\-4&0&1\\0&2&1\end{pmatrix},
 \qquad A^{-1}=\begin{pmatrix}1/8&-1/4&1/8\\-1/4&0&1/4\\1/2&0&1/2\end{pmatrix}.
\]
For \(w_j=q_j(D_t)u\), the reconstruction is
\(z_0=(w_1-2w_2+w_3)/8\), \(z_1=(-w_1+w_3)/4\), and \(z_2=(w_1+w_3)/2\). Divide the first by \(|\xi|^2\) and the second by \(|\xi|\) to recover \(u,D_tu\). This is the full system; retaining only one quotient would not recover arbitrary jets. In variable coefficients these matrix products acquire lower-order symbolic corrections, handled by the ordinary ordered parametrix and its residuals.

**Exercise 15 — intermediate: Hamiltonian parameter versus forward time.** Compute \(H_p\) on the two branches of \(p=\tau^2-c^2\xi^2\) and compare with \(H_{\tau\mp c\xi}\). Which parameter should define forward Cauchy propagation?

**Solution.** On \(\tau=c\xi\), \(p=(\tau-c\xi)(\tau+c\xi)\), so \(H_p=2c\xi H_{\tau-c\xi}\); on \(\tau=-c\xi\), \(H_p=-2c\xi H_{\tau+c\xi}\). The spatial velocities of the normalized branch fields are \(-c\) and \(c\), respectively, and both have \(\dot t=1\). The sign of \(2c\xi\), or of \(-2c\xi\), can reverse the parameter of \(H_p\). Forward Cauchy propagation uses increasing \(t\), equivalently the normalized first-order branch parameter, while the unparameterized characteristic curves are the same.

**Exercise 16 — intermediate: a raw boundary derivative is different.** Let \(u\) be smooth on \(t\ge0\), with nonzero initial value. Compute the derivative of its zero extension and the intrinsic normal derivative. Why can an arbitrary ambient derivative not supply the Cauchy jet used in (HC20)?

**Solution.** Since \(D_tH=-i\delta\), \(D_t(Hu)=H(D_tu)-iu(0)\delta\). Adding \(iu(0)\delta\) gives the supported representative of the intrinsic derivative. The raw ambient derivative includes a distribution concentrated on the boundary, even though the interior derivative is smooth. An arbitrary extension can add further boundary-supported distributions without changing its interior restriction. The canonical dual conormal extension and its intrinsic trace remove this ambiguity; (HC20) uses those traces and all \(m\) normal jets.

**Exercise 17 — advanced: why tangential smoothing alone is insufficient.** Let \(B\) have a smooth spatial kernel \(K(x,y)\), and take \(u(t,x)=\delta(t-t_*)g(x)\), with compact smooth \(g\) and \(Bg\ne0\). Compare this with its action in the boundary proof.

**Solution.** \(Bu=\delta(t-t_*)Bg(x)\) still has pure temporal wavefront at every point where \(Bg\ne0\); no spatial-frequency decay removes the normal delta. In the interior propagation proof the ordinary cutoff first excludes all pure temporal wavefront directions of the compact input. In the boundary proof, the input is in \(\mathcal N\), and the exact tangential theorem first removes every compressed boundary covector for a spatially smoothing output. Closedness on a compact output collar then excludes interior wavefront approaching the boundary; the conormal/dual intersection upgrades it to full smoothness. These are the actual extra hypotheses and mechanisms.

**Exercise 18 — advanced: an incoming spatial edge.** Verify the domain example at the end of Section 9, including extendibility, the equation, the initial traces and the characteristic through \((t,x)=(3/4,3/4)\). State the valid propagation conclusion.

**Solution.** The ambient distribution \(\delta(x+t-3/2)\) restricts to the interior solution, so it is extendible. Its two partial derivatives are both \(\delta'(x+t-3/2)\), hence \((D_t-D_x)u=0\). At any \((0,x_0)\) with \(0<x_0<1\), a sufficiently small neighborhood has \(x+t<3/2\), so \(u\) and every initial jet vanish there. Its ordinary wavefront along the graph consists of nonzero covectors \(a(dt+dx)\), which satisfy \(\tau-\xi=0\). The normalized branch has \(\dot t=1,\dot x=-1\), so its backward line from \((3/4,3/4)\) reaches \((1/2,1)\) and exits the open spatial interval, before reaching \(t=0\). The boundary equality at \(X_0\) is valid, and local propagation follows this incoming characteristic. To deduce a global containment from initial data and forcing alone, require backward characteristics to remain in the domain until they reach the initial surface, or supply data on the incoming spatial edge.

**Exercise 19 — advanced: interior distributions need not be extendible.** On \(t>0\), let \(u(t,x)=e^{1/t}g(x)\), where \(g\) is a nonnegative nonzero smooth function of compact support. Show that \(u\) is an interior distribution and that no distribution across \(t=0\) restricts to it. Explain which hypothesis of the boundary theorem this example tests.

**Solution.** The function is smooth on the open half-space, so it defines a distribution there. Choose a nonnegative spatial test \(\psi\) with \(c_0=\int g\psi>0\), and a nonnegative normal test \(\eta\in C_c^\infty((1,2))\) with integral one. For \(\eta_\epsilon(t)=\epsilon^{-1}\eta(t/\epsilon)\), all these product tests are supported in one fixed compact neighborhood of \(t=0\), and
\[
 (u,\eta_\epsilon\psi)\ge c_0 e^{1/(2\epsilon)}. \tag{HC32}
\]
If an extension \(U\) existed, its continuity on tests supported in that compact set would give an order \(M\) and \(|(U,\eta_\epsilon\psi)|\le C\epsilon^{-M-1}\). Restriction identifies this pairing with the preceding one, since its support lies in \(t>0\). Exponential growth exceeds that polynomial for small \(\epsilon\), a contradiction. Thus membership in \(\mathcal D'(X_+)\) alone does not give the extendibility required for \(\overline{\mathcal D'}(X_+)\), much less the canonical \(\mathcal N\) extension and intrinsic jets. This example tests the distribution class; it is not asserted to solve an equation with the forcing hypotheses of the boundary theorem.

**Exercise 20 — intermediate: forcing contributes boundary wavefront.** Take \(P=D_t\), \(f(t,x)=\delta(x)\), and zero initial value. Compute an extendible solution and its compressed boundary wavefront. Explain why the forcing term is necessary in (HC20).

**Solution.** The monic first-order symbol is \(p=\tau\), with \(p_\tau=1\), so the strict condition holds. The solution \(u=it\delta(x)\) satisfies \(D_tu=\delta(x)\) and \(u(0)=0\). These distributions are smooth in time with values in spatial distributions, extend across the boundary, and have no ordinary wavefront in pure temporal directions. Their canonical extensions and intrinsic jets belong to \(\mathcal N\). The only possible compressed singularities lie at \(t=0,x=0,\zeta=0,\xi\ne0\), by tangential localization away from the wavefront of \(\delta(x)\). Every one is present: the intrinsic derivative is \(f\), its initial trace is \(\delta(x)\), and the differential forward inclusion (HC25) followed by the exact trace inclusion gives
\[
 \{(0,0;\xi,0):\xi\ne0\}
   =\operatorname{WF}(\delta)\subset\operatorname{WF}_b(f)
   \subset\operatorname{WF}_b(u). \tag{HC33}
\]
The first inclusion regards the ordinary trace covector as the corresponding boundary covector. The opposite containment was just localized directly, so this describes the boundary wavefront exactly. All initial data in the order-one problem vanish, yet the boundary forcing has nonempty wavefront. Including \(\operatorname{WF}_b(f)\) in the boundary equality is essential.

**Exercise 21 — intermediate: the minimal extension of an exponential.** In the one-dimensional normal model let \(u_\alpha(t)=e^{-\alpha t}\) on \(t>0\), with \(\alpha>0\). Compute its minimal \(H^1\) extension from (HC41), its squared quotient norm and the ratio of the two lower squared norms in (HC45) to that quotient norm. Determine when the lower bound is attained.

**Solution.** Here \(J_-=1-\partial_t\), so \(g=(1+\alpha)e^{-\alpha t}\). The inverse has kernel \(e^tH(-t)\), since \((1-\partial_t)(e^tH(-t))=\delta_0\). Thus
\[
 E_1u_\alpha(t)=e^t\int_{\max(t,0)}^\infty(1+\alpha)e^{-(1+\alpha)s}\,ds
 =\begin{cases}e^{-\alpha t},&t\ge0,\\ e^t,&t<0.\end{cases}
 \tag{HC49}
\]
The boundary values agree, so its weak first derivative has no delta. The squared \(H^1\) norm is
\((1+\alpha^2)/(2\alpha)+1=(1+\alpha)^2/(2\alpha)=\|g\|_2^2\),
which is minimal by (HC41). The two lower squared quotient norms sum to \((1+\alpha^2)/(2\alpha)\). Their ratio is \((1+\alpha^2)/(1+\alpha)^2\), at least \(1/2\) because \((\alpha-1)^2\ge0\), with equality exactly at \(\alpha=1\). On a mixed collar the same operator \(E_1\) commutes with every tangential Sobolev weight, including nonintegral orders; it selects one extension for their intersections. This normal model exhibits its boundary mechanism, not a nonzero constant vector in a spatial \(L^2\) space.

**Exercise 22 — advanced: a supported delta and the sign of the decomposition.** In one normal dimension determine the orders \(r\) for which \(\delta_0\in H^r(\mathbb R)\). Apply (HC44) to it. Verify the component orders, support and equality as ambient distributions, including the boundary term.

**Solution.** Since \(\widehat\delta_0=1\), its squared norm is \((2\pi)^{-1}\int(1+\tau^2)^r\,d\tau\), finite exactly for \(r<-1/2\). The inverse of \(J_+=1+\partial_t\) has kernel \(H(t)e^{-t}\). Therefore
\[
 f_0=H(t)e^{-t},\qquad f_n=iH(t)e^{-t},\qquad
 D_tf_n=\delta_0-H(t)e^{-t},\qquad f_0+D_tf_n=\delta_0.
 \tag{HC50}
\]
Both components have forward support. The Fourier modulus of \(H(t)e^{-t}\) is \((1+\tau^2)^{-1/2}\), so each squared \(H^{r+1}\) norm equals the displayed squared \(H^r\) norm of \(\delta_0\). In this zero-dimensional tangential model the extra tangential weight is one. The ambient derivative must retain its delta; deleting it would give zero instead of the supported source. On restriction to \(t>0\), the same source is zero, which explains why the bar and dot problems differ at the boundary.

**Exercise 23 — advanced: two order-three boundary operators.** In a two-dimensional collar, compare \(B_1u=(D_x^2D_tu)|_{t=0}\) and \(B_2u=(D_t^3u)|_{t=0}\). Find their total and transversal orders and their guaranteed maps on restricted \(H^s\). Under \(X=x+ct,T=at\), with \(a>0\), compute \(B_1\) in the new chart. Show explicitly why \(B_2\) has no continuous extension from restricted \(H^2\) to \(H^{-3/2}\), although \(B_1\) does.

**Solution.** Both total orders are three. Their transversal orders are one and three, respectively. Formula (HC51) gives target \(H^{s-7/2}\) for \(B_1\) when \(s>3/2\), and for \(B_2\) when \(s>7/2\). If \(v(X,T)=u(X-cT/a,T/a)\), the actual chain rule gives \(D_x=D_X\) and \(D_t=cD_X+aD_T\). Therefore
\[
 B_1u=\bigl(cD_X^3v+aD_X^2D_Tv\bigr)|_{T=0}.
 \tag{HC52}
\]
The added term has transversal order zero; the nonzero coefficient \(a\) retains transversal order one. The change of collar does not raise that order to three.

At \(s=2\), the normal trace of \(D_tu\) belongs to \(H^{1/2}\), and two tangential derivatives give the continuous \(B_1\) map into \(H^{-3/2}\). For the second operator, fix nonzero \(g\in C_c^\infty(\mathbb R)\), and let \(\chi(t)=t^3\eta(t)\), where \(\eta\in C_c^\infty(\mathbb R)\) equals one near zero. Put
\[
 u_\varepsilon(x,t)=\varepsilon^{3/2}g(x)\chi(t/\varepsilon),
 \qquad 0<\varepsilon\le1.
\]
For \(\ell+j\le2\), its whole-space \(L^2\) derivative norm is
\(\varepsilon^{2-j}\|D_x^\ell g\|_2\|D_t^j\chi\|_2\). These finitely many quantities are bounded, so the whole-space and hence the restricted \(H^2\) norms are bounded. But \((-i)^3=i\) and \(\chi'''(0)=6\), giving \(B_2u_\varepsilon=6i\varepsilon^{-3/2}g\). Its \(H^{-3/2}\) norm diverges. Every member is smooth up to the boundary, so a continuous extension agreeing with the smooth boundary operator would contradict this sequence. Total order alone cannot select the trace threshold.

## Source and prerequisite notes

The historical source for the higher-order statements is Lars Hörmander, *The Analysis of Linear Partial Differential Operators III*, approved 2007 eBook, ISBN 978-3-540-49938-1, Section 23.2, printed pages 390–400 (PDF pages 405–415). The progression above includes Lemma 23.2.1, Theorem 23.2.2, Definition 23.2.3, Theorem 23.2.4, Propositions 23.2.5–23.2.6, Theorem 23.2.7, Lemma 23.2.8 and Theorems 23.2.9–23.2.10. The global forward reading of the last consequence is qualified by the domain-access condition and the explicit incoming-edge example, as required by local propagation.

Appendix B.2, especially B.2.1, B.2.3–B.2.4, B.2.6–B.2.7 and B.2.9–B.2.10, supplies the mathematical antecedents for the mixed spaces. The actual programme proofs are the included MH two-weight and support/duality companions, GB coordinate bounds and the complete Section 4 above. The ordinary/tangential composition antecedent is III, Theorem 18.1.35; the exact all-remainder proof is [the FC spacetime companion](../20261005-restored-first-order-cauchy/spacetime-symbol-composition.md). Noncharacteristic pullback uses I, Theorem 8.2.4, approved 2003 eBook ISBN 978-3-642-61497-2; [the included complete pullback and slice companion](../20261005-restored-first-order-cauchy/smooth-pullback-and-time-slices.md) proves the needed statements and retains its GFDL notices.

Boundary extension and jets use [NE's full weighted normal equation](../20261005-normal-extension/normal-extension-and-boundary-defect.md), [CNF's dual action and intrinsic jets](../20261005-conormal-test-foundations/dual-conormal-distributions-and-jets.md), [BW's complete compressed differential proof](../20261005-boundary-wavefront-and-tangential/compressed-wavefront-and-differential-action.md), [normal and tangential action](../20261005-boundary-wavefront-and-tangential/normal-extension-and-tangential-action.md) and [smooth testers and exact trace consequences](../20261005-boundary-wavefront-and-tangential/smooth-testers-and-boundary-consequences.md). These retain the existing AN-03 bridge material by Claude Opus 5.5 (Anthropic), with Codex editorial contributions, and its source context in Hörmander III, 18.3.31–18.3.33. The actual ordered quotient inverse uses the included ordinary matrix parametrix. The positive-real beta bridge was compared with AN03-U008 Section 16.9; (HC53) gives an independent positive-integral proof using only the exact earlier measure and one-dimensional substitution proofs.

Self-checked by the writing AI. The current proof map records each exact provider; finite model checks supplement the proofs. Independent human review, the remaining course and public clearance are separate and remain pending.
