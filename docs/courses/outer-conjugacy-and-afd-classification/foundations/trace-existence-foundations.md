# Trace existence and central averaging

*Proof exposition by GPT-6 Astra and GPT-6.1 Sol (OpenAI), with the corner-trace construction based on programme exposition by Claude Opus 5.5 (Anthropic). Original programme text: CC0-1.0. Sources and contributions are identified below.*

<a id="t1"></a>

## T1. The three general assertions

Let \(M\subseteq B(H)\) be a von Neumann algebra on an arbitrary complex Hilbert space. No countability, separability, factoriality or faithful-state assumption is imposed.

1. **Semifinite scalar traces.** Every nonzero projection of \(M\) majorizes a nonzero finite projection if and only if \(M\) carries a faithful normal semifinite scalar trace \(\tau:M_+\to[0,\infty]\). Equivalently, every nonzero central projection majorizes a nonzero finite projection. Here a trace is additive, positively homogeneous, and satisfies \(\tau(x^*x)=\tau(xx^*)\); normality means preservation of all bounded increasing positive suprema, and semifiniteness means
   \[
   \tau(x)=\sup\{\tau(y):0\le y\le x,\ \tau(y)<\infty\}.
   \tag{T1a}
   \]
   The construction in GS1–GS3 proves this full condition, as well as the weaker order-density condition for finite-trace positive elements.
2. **Finite center-valued trace.** If \(M\) is finite, there is a unique normal positive linear center-module map \(T_M:M\to Z(M)\) satisfying \(T_M(1)=1\) and \(T_M(xy)=T_M(yx)\). It is faithful and contractive, fixes the center, and has norm one if \(M\ne0\). Normality here includes ultraweak continuity on the entire domain. The zero algebra has the zero map. FCT0–FCT8 give the construction and its consequences without first assuming scalar-trace existence.
3. **Norm-closed unitary averaging.** If \(M\) is finite and \(a\in M\), then
   \[
   \begin{aligned}
   D(a)&=\overline{\operatorname{co}}^{\,\|\cdot\|}
        \{uau^*:u\in\mathcal U(M)\},\\
   D(a)\cap Z(M)&=\{T_M(a)\}.
   \end{aligned}
   \tag{T1b}
   \]
   In particular \(T_M(a)\in D(a)\). This holds for complex \(a\), not only self-adjoint or positive elements. The same central singleton occurs for the ultraweakly closed convex hull. CA1–CA3 supply an actual convergent sequence of finite averages, including simultaneous averaging for a finite family.

The finite trace is proved in [FCT0–FCT8](#fct-0), the averaging assertion in [CA1–CA3](#ca-definitions), and the scalar trace in [GS1–GS3](#gs1). The [bounded interface](#s0) and the [elementary proof appendix](#appendix-cf) specify their earlier analytic and projection inputs. These proofs retain arbitrary orthogonal index sets and arbitrary increasing nets.

The three trace theorems provide the trace foundations for discrete trace-scaling stability. The extended-positive, density and modular-transfer hypotheses of that theorem are treated separately.

<a id="admitted-base"></a>

## Analytic foundations

The following accompanying programme proofs are used at the stated locations:

- [Bounded topology foundations](bounded-topology-foundations.md): NP1–NP2 for norm extension; AB04–AB05 for compact products and dual balls; GP0 for bounded continuous calculus; BK01–BK04 for concrete operator topology and increasing nets; CP01–CP07 for projective tensor preduals, vector-series functionals, norm closure and positive-functional decomposition; HA03 and HAP04–HAP05 for bounded nonunital bicommutant and Kaplansky approximation.
- Tracial normality foundations: BK05–BK07 for support and bounded polar constructions; NP3 for the support of a bounded positive normal functional; TP1 for bounded positive-functional order normality if and only if ultraweak continuity; TP2 for arbitrary projection joins; TP3 for the precise half-closed bounded spectral cuts.

The [source and authorship record](trace-existence-foundations.provenance.json) identifies the accompanying proofs. The appendices give continuous calculus (CF1–CF8), projection comparison (PC0–PC7), and faithful representations (ST1–ST2). Sections S0–S2 supply the bounded spectral and positive-map facts used in the trace construction.

<a id="s0"></a>

## S0. Commutants and the earlier proof notation

Every element of a unital C-star algebra is a linear combination of four unitaries. Indeed split it into real and imaginary self-adjoint parts; for a self-adjoint contraction \(h\), continuous calculus gives the unitary
\[
u=h+i(1-h^2)^{1/2},\qquad h=(u+u^*)/2.
\]
Consequently an operator commuting with every unitary of a unital C-star algebra commutes with the whole algebra. This supplies the commutant-unitary test denoted SF0 in the original projection proof. A closed subspace reducing these unitaries has its orthogonal projection in their commutant. Hilbert completeness, orthogonal projections and bounded adjoints have the full proofs in CF8 below; no unbounded operator construction is used.

The notation CP4–CP6 means the concrete predual/vector-series statements CP01–CP07 in the supplied bounded-topology companion. In particular a normal functional is a square-summable vector-pair series, these functionals are norm closed in the norm dual, fixed multiplication is globally ultraweakly continuous, and bounded strong convergence implies ultraweak convergence. These facts apply to arbitrary Hilbert spaces and projection corners.

<a id="s1"></a>

## S1. All bounded spectral cuts used here

**Lemma.** For bounded self-adjoint \(h\in M\), all the upper and lower threshold projections used below belong to \(M\), commute with \(h\), and have the stated spectral inequalities. Self-adjoint elements admit finite spectral step approximations in norm. The same assertions hold in every projection corner and preserve centrality.

**Proof.** Continuous calculus gives \(h_+=\max(h,0)\), \(h_-=\max(-h,0)\), and \(h_+h_-=0\). For bounded positive \(b\), its support \(s(b)\) is the projection onto \(\overline{bH}\). The support proof BK06/TP2 shows that it belongs to \(M\); explicitly the positive contractions
\[
b(b+n^{-1}1)^{-1}
\]
converge strongly to that projection. They vanish on \(\ker b\); on a vector \(b\eta\) their error is bounded by \(n^{-1}\|\eta\|\); boundedness then extends convergence to \(\overline{bH}\). This also proves that any operator commuting with \(b\) commutes with its support. Products of two commuting such approximating families commute, so the supports of commuting positive elements commute.

Put
\[
\begin{gathered}
e_t=s((h-t1)_+),\\
q_t=1-s((t1-h)_+).
\end{gathered}\tag{S1}
\]
These are the projections denoted \(1_{(t,\infty)}(h)\) and \(1_{[t,\infty)}(h)\). The notation is justified by the following direct inequalities, without assuming a general Borel calculus. Positive and negative parts have zero product. The support of either part therefore annihilates the other part, first on its range and then on its closure. It follows that
\[
\begin{aligned}
he_t&\ge t e_t,&
h(1-e_t)&\le t(1-e_t),\\
hq_t&\ge t q_t,&
h(1-q_t)&\le t(1-q_t).
\end{aligned}
\tag{S2}
\]
For \(s<t\), the scalar identity


\[
\begin{gathered}
\max(r-t,0)\\
=\max(\max(r-s,0)-(t-s),0)
\end{gathered}
\]


and continuous calculus show that \(\ker(h-s)_+\subseteq\ker(h-t)_+\). Hence \(e_t\le e_s\). All these cuts commute, since their continuous approximants are functions of \(h\). If \(h\) is central, their approximants and strong limits are central.

Choose a finite mesh \(t_0<-\|h\|<\|h\|<t_n\), including intermediate \(t_j\) with maximal gap less than \(\varepsilon\). Then \(e_{t_0}=1\), \(e_{t_n}=0\), and
\[
p_j=e_{t_j}-e_{t_{j+1}}\quad(0\le j<n)
\]
are orthogonal projections summing to one. Inequalities (S2) give
\[
t_jp_j\le hp_j\le t_{j+1}p_j.
\]
Choosing any coefficient in each interval gives a finite step element within \(\varepsilon\) of \(h\): each orthogonal corner error has norm at most the mesh size, and its diagonal sum has norm at most that same bound. For \(h\ge0\), intervals strictly below zero have zero projection by the upper bound and positivity. On an interval containing zero choose coefficient zero; on the remaining nonzero corners choose a nonnegative coefficient in the interval. The same error bound proves the positive step approximation.

For \(b\ge0\) and \(0<\delta<\|b\|\), the half-closed cut \(q_\delta\) is nonzero. Otherwise \(b\le\delta1\) by (S2), contradicting the norm inequality. Moreover \(\delta q_\delta\le b\), because \(b\) is nonnegative on the complementary corner. This is exactly TP3's nonzero-cut statement. In the corner with unit \(q_\delta\), the inverse of \(bq_\delta\) is bounded and positive: the continuous function \(r\mapsto1/\max(r,\delta)\), multiplied by \(q_\delta\), is its inverse. In particular its norm is at most \(\delta^{-1}\). Finally \(s(d_+)\), for central self-adjoint \(d\), cuts out a nonnegative part of \(d\) with full support on that cut; if \(d\not\le0\), this cut is nonzero. These prove all threshold, support and bounded-inverse operations used in FCT and CA. \(\square\)

This lemma supplies the actual bounded consequences of the original FCT references to SB1–SB6. It does not claim the full unbounded multiplication, Borel representation or scalar-measure theorems supplied elsewhere in OA-FLOW.

<a id="s2"></a>

## S2. Order-normal positive maps are globally normal

Suppose \(F:M\to N\) is a bounded positive linear map preserving bounded increasing positive suprema. For every \(\omega\in N_*^+\), the positive bounded functional \(\omega F\) preserves these suprema, since \(\omega\) does. TP1 in the supplied tracial-normality companion proves \(\omega F\in M_*\). Every element of \(N_*\) is a linear combination of four positive normal functionals, by CP07 or FCT0's explicit vector polarization. Thus pullback by \(F\) maps all of \(N_*\) to \(M_*\), proving ultraweak continuity on the entire domain. Conversely a globally ultraweakly continuous positive map preserves these suprema by BK04 and bounded strong-to-ultraweak convergence, as also proved in FCT0.

A unital star automorphism and its inverse preserve order and all existing bounded increasing suprema, by transporting upper bounds through the inverse. They are contractive by CF6, and the preceding argument proves their global normality. This is the entire positive-map consequence denoted NF6 in FCT8. ST1–ST2 in the appendix give the separate faithful-representation and inverse-normality argument, including the linear predual criterion needed to pass from ball continuity to global continuity.

## The normalized trace with its full center retained

Let \(M\subseteq B(H)\) be a finite von Neumann algebra on an arbitrary complex Hilbert space, and put \(Z=Z(M)\). Finiteness means that an isometry in every projection corner has full final projection. Equivalently, the identity is a finite projection, since finiteness passes to subprojections by PC5. No countability, factor, separability or scalar-trace assumption is made.

We construct a unique normal positive linear map \(T:M\to Z\) such that

<a id="equation-fct1"></a>

\[
\begin{gathered}
T(1)=1,\qquad T(zx)=zT(x),\\
T(xy)=T(yx)\quad(z\in Z,\ x,y\in M).
\end{gathered}
\tag{FCT1}
\]
It is faithful, has norm one when \(M\ne0\), and preserves all bounded increasing positive suprema. Normal here means continuous on the entire concrete ultraweak space, not just on bounded sets. For the zero algebra the map is zero; its norm is zero and its normalization is \(T(0)=0\).

The construction is quantitative: maps with trace distortion tending to one converge in operator norm. We prove that stability first, under an explicit tiling condition. We then supply the tilings, normal center-valued states and two local balancing arguments needed to produce those maps.

The exact earlier inputs are [CF1–CF8](#appendix-cf), [S0–S2](#s0), the [already supplied predual and density proofs](#admitted-base), [ST1–ST2](#oa-flow.st.1), and [PC0–PC7](#oa-flow.projection.pc0). Scalar trace existence, type-I classification, direct integrals and a fixed-point theorem are not premises.

*Programme exposition by GPT-6.1 Sol (OpenAI).*

<a id="fct-0"></a>

<a id="oa-flow.fct.0"></a>

## FCT0. Three analytic operations

For a positive functional \(f\) on a unital C-star algebra, the positive/negative decomposition of a self-adjoint element shows that \(f\) is real on self-adjoint elements, hence \(f(x^*)=\overline{f(x)}\). Positivity of \(f((x+ty)^*(x+ty))\) for all complex \(t\) proves

<a id="equation-fct2"></a>

\[
 |f(y^*x)|^2\le f(x^*x)f(y^*y).
 \tag{FCT2}
\]
Indeed the diagonal values are nonnegative and the mixed terms are conjugates. If \(f(y^*y)>0\), minimize the scalar quadratic. If that diagonal is zero, a nonzero mixed term would make the quadratic negative by a sufficiently large scalar of the opposite phase. This also proves the zero-diagonal case. Setting \(y=1\) and using \(x^*x\le\|x\|^2 1\), from CF7, gives \(\|f\|=f(1)\), including \(f=0\).

Suppose \(F:M\to Z\) is positive and linear. Every character \(\chi\) of the commutative unital C-star algebra \(Z\) is positive, by CF6 and positive square roots. Thus \(\chi\circ F\) is positive and
\[
 |\chi(F(x))|\le \chi(F(1))\|x\|\le\|F(1)\|\|x\|.
\]
CF6 proves \(\|z\|=\sup_\chi|\chi(z)|\) for every complex \(z\in Z\). Consequently

<a id="equation-fct3"></a>

\[
 \|F\|=\|F(1)\|.
 \tag{FCT3}
\]
This proves boundedness as well as the exact norm. It does not identify a complex image with its real part. The same argument works in a nonzero central corner, using its identity.

For completeness, a bounded increasing net \(a_j\ge0\) has its supremum as a strong limit in \(M\). Its limiting quadratic values define a bounded positive form: homogeneity and the parallelogram identity pass to the scalar limits along the directed net. Polarization and CF8's Hilbert representation theorem give a positive operator \(a\). We have \(0\le a-a_j\le C1\) for a common bound \(C\), so CF6–7 give

<a id="equation-fct4"></a>

\[
 \|(a-a_j)\xi\|^2\le C\langle(a-a_j)\xi,\xi\rangle\longrightarrow0.
 \tag{FCT4}
\]
Strong closedness puts \(a\) in \(M\), and its quadratic values show that it is the least upper bound. CP4–6's vector-series tail estimate makes every bounded strong limit an ultraweak limit. In particular an ultraweakly continuous positive map \(F\) preserves these suprema: the bounded increasing \(F(a_j)\) have a strong supremum \(b\) by this same argument, hence an ultraweak limit \(b\), while continuity gives the ultraweak limit \(F(a)\). Uniqueness of the limit gives \(b=F(a)\).

We will also use the following complete decomposition of normal functionals. By CP4–6 every \(\omega\in M_*\) is \(\sum_j\omega_{u_j,v_j}\), with both vector sequences square summable and inner products linear in the first variable. Polarization gives

<a id="equation-fct5"></a>

\[
 \omega_{u,v}=\frac14\sum_{k=0}^3 i^k\omega_{u+i^kv,u+i^kv}.
 \tag{FCT5}
\]
For each \(k\), the sum of these positive vector functionals is normal: \(\sum_j\|u_j+i^kv_j\|^2<\infty\). Thus every normal functional is a linear combination of four positive normal functionals. CP6 also proves that \(M_*\) is norm closed in \(M^*\). Finally \(x\mapsto axb\) is normal for bounded \(a,b\): substituting in its vector series replaces \((u_j,v_j)\) by \((bu_j,a^*v_j)\), which are still square summable. These assertions apply equally to \(Z\) and all concrete corners.

<a id="fct-1"></a>

<a id="oa-flow.fct.1"></a>

## FCT1. Quantitative stability, with the tiling premise explicit

Call a nonzero projection \(p\) a **central tile** if there are finitely many orthogonal projections

<a id="equation-fct6"></a>

\[
\begin{gathered}
p=p_1\sim p_2\sim\cdots\sim p_k,\\
p_1+\cdots+p_k=z\in Z,
\end{gathered}\tag{FCT6}
\]
where \(z\) is a nonzero central projection. Necessarily \(c(p)=z\), by PC2's preservation of central support under equivalence. This definition includes \(k=1\).

For this section alone assume that every projection is an arbitrary orthogonal sum of central tiles. A **normal center-valued state** is a normal positive linear \(\phi:M\to Z\) satisfying \(\phi(1)=1\) and \(\phi(zx)=z\phi(x)\). Suppose \(a_n>1\) decreases to one and such states satisfy, on all of \(M\),

<a id="equation-fct7"></a>

\[
 \phi_n(xx^*)\le a_n\phi_n(x^*x).
 \tag{FCT7}
\]
For \(m<n\) and a central tile as in (FCT6), a partial isometry between \(p\) and \(p_i\), used in both directions in (FCT7), gives

<a id="equation-fct8"></a>

\[
\begin{aligned}
k\phi_n(p)&\le a_n\sum_i\phi_n(p_i)=a_nz\\
&=a_n\sum_i\phi_m(p_i)\\
&\le ka_na_m\phi_m(p)\\
&\le ka_m^2\phi_m(p).
\end{aligned}\tag{FCT8}
\]
The last comparison uses \(\phi_m(p_i)\le a_m\phi_m(p)\). Thus \(D_{mn}=a_m^2\phi_m-\phi_n\) is nonnegative on tiles. Normality and finite partial sums extend the inequality to every projection. The bounded spectral step approximation proved in S1 extends it to every positive element; boundedness permits the norm limit. Hence \(D_{mn}\) is a positive map, with \(D_{mn}(1)=(a_m^2-1)1\). By (FCT3),

<a id="equation-fct9"></a>

\[
\begin{gathered}
\|D_{mn}\|=a_m^2-1,\\
\|\phi_m-\phi_n\|\le2(a_m^2-1).
\end{gathered}\tag{FCT9}
\]
The maps are norm Cauchy. Completeness of \(Z\), applied at each \(x\) and then to the uniform operator bound, gives a norm limit \(T:M\to Z\). Positivity, normalization and the center-module identities pass to it. For \(\omega\in Z_*\),

<a id="equation-fct10"></a>

\[
 \|\omega\circ T-\omega\circ\phi_n\|
 \le\|\omega\|\|T-\phi_n\|\longrightarrow0.
 \tag{FCT10}
\]
The terms belong to \(M_*\), whose norm closedness was proved in CP6. Thus \(T\) is ultraweakly continuous on its entire domain.

Taking limits in (FCT7) and interchanging \(x,x^*\) gives \(T(xx^*)=T(x^*x)\). For positive \(b\) and a unitary \(u\), apply this to \(ub^{1/2}\); it gives \(T(ubu^*)=T(b)\). Linearity gives that identity for every \(b\in M\), and replacing \(b\) by \(xu\) gives \(T(ux)=T(xu)\). Every element is a linear combination of four unitaries: split it into real and imaginary self-adjoint parts, scale each nonzero part to a contraction \(h\), and write

<a id="equation-fct11"></a>

\[
 h=\tfrac12(u+u^*),\qquad
 u=h+i(1-h^2)^{1/2}.
 \tag{FCT11}
\]
CF6–7 verify that \(u\) is unitary. Consequently \(T(xy)=T(yx)\) for all \(x,y\). The tiling premise and the approximate states used in this conditional stability lemma are proved next, before it is applied to establish existence.

<a id="fct-2"></a>

<a id="oa-flow.fct.2"></a>

## FCT2. Finite cancellation and unitary completion

Suppose \(p\sim q\) in the finite algebra, with prescribed partial isometry \(v\) from \(p\) to \(q\). PC2 compares their complements centrally: on a central piece \(z\), there is a partial isometry from \(z(1-p)\) to a subprojection of \(z(1-q)\). Add it to \(zv\). Orthogonality of the initial and final projections makes the sum an isometry in \(zM\). Since \(z\) is finite, its final projection is all of \(z\). Therefore that complement subequivalence is an equivalence. On \(1-z\) reverse the roles and repeat. PC1 adds the two complement equivalences, proving

<a id="equation-fct12"></a>

\[
 p\sim q\quad\Longrightarrow\quad1-p\sim1-q.
 \tag{FCT12}
\]
Adding the complementary partial isometry to the originally prescribed \(v\) extends \(v\) to a unitary. This works in every finite corner.

We need the version for different equivalent finite units. If \(e\sim f\), \(a\le e\), \(b\le f\), and \(a\sim b\), first transport \(b\) to \(eMe\) through an implementing equivalence between \(e,f\). Apply (FCT12) to the resulting two projections in that corner, then transport back. It gives \(e-a\sim f-b\). No trace is used.

A finite algebra contains no infinite orthogonal family of copies of one nonzero projection. Otherwise choose distinct copies \(p_0,p_1,\ldots\), and partial isometries from \(p_n\) onto \(p_{n+1}\). Their PC1 strong-star sum has initial projection \(P=\sum_{n\ge0}p_n\) and final projection \(P-p_0<P\). This contradicts finiteness of the subprojection \(P\).

<a id="fct-3"></a>

<a id="oa-flow.fct.3"></a>

## FCT3. Central tiles without a type-I classification

First split off the part generated by abelian projections. A projection \(e\) is abelian if \(eMe\) is commutative. Let \(z_a\) be the join in \(Z\) of the central supports of all such projections. If a nonzero projection \(p\le z_a\) had no nonzero abelian subprojection, it would have no polar bridge to any abelian projection: a nonzero bridge gives a subprojection of \(p\) equivalent to a subprojection of an abelian corner. Equivalence identifies those smaller corners, so the former is abelian. PC2 would then make \(c(p)\) orthogonal to every central support in that join, a contradiction. Thus every nonzero \(p\le z_a\) contains a nonzero abelian \(e\).

Fix such \(e\), and work on \(z=c(e)\). By PC4, every subprojection of \(e\) is \(ew\) for a central projection \(w\le z\), since \(eMe=Z(eMe)=Ze\). Construct orthogonal projections \(e_1,e_2,\ldots\) with \(e_1=e\). Set \(z_1=z\) and, after choosing \(e_1,\ldots,e_n\), put

<a id="equation-fct13"></a>

\[
 r_n=z-\sum_{j\le n}e_j,\qquad z_{n+1}=c(r_n).
 \tag{FCT13}
\]
We can choose \(e_{n+1}\le r_n\) equivalent to \(ez_{n+1}\); if the residual is zero all later terms are zero. To see this, compare \(ez_{n+1}\) and \(r_n\). On a central piece where \(r_n\precsim ez_{n+1}\), its final subprojection of that abelian projection is \(ew\). Its central support is the full comparison piece, because \(c(r_n)=z_{n+1}\). Thus \(w\) is that piece and the subequivalence is an equivalence. On the other comparison piece \(ez_{n+1}\precsim r_n\) directly. Add the two implementations. This proves the asserted choice.

The \(z_n\) decrease. If \(z_\infty=\bigwedge_nz_n\ne0\), the orthogonal \(e_nz_\infty\) would all be equivalent to the nonzero \(ez_\infty\), contradicting FCT2. Thus \(z_\infty=0\). The central projections \(w_n=z_n-z_{n+1}\) sum to \(z\). On \(w_n\), exactly the first \(n\) constructed projections fill the unit:

<a id="equation-fct14"></a>

\[
 w_n=\sum_{j=1}^n e_jw_n,\qquad e_jw_n\sim ew_n.
 \tag{FCT14}
\]
The equality follows because \(r_nw_n=0\), and the equivalences because \(w_n\le z_j\) for \(j\le n\). Every nonzero \(ew_n\) is therefore a central tile, and at least one is nonzero. This is an explicit finite homogeneous matrix-family construction; no classification theorem is hidden in it.

On \(M(1-z_a)\) there is no nonzero abelian projection. Every nonzero corner there contains two nonzero orthogonal equivalent projections. Indeed its algebra is not commutative. If all its projections were central, bounded spectral step approximation would make every self-adjoint element central and hence the algebra commutative. Take a noncentral projection \(r\); some off-diagonal corner \(rx(1-r)\), or its adjoint, is nonzero. PC1 polar decomposition gives the required orthogonal equivalent subprojections.

Choose a maximal family of such pairs in any nonzero central unit \(z\le1-z_a\), with all projections mutually orthogonal. A nonzero residual corner would contain another pair. Hence their sums are equivalent complementary halves of \(z\). Repeat in one half and transport its division to the other half. Induction gives, for every \(n\), a division of \(z\) into \(2^n\) orthogonal equivalent projections \(d_{n,j}\), with \(d_{n,0}\) decreasing and

<a id="equation-fct15"></a>

\[
 d_{n,0}=d_{n+1,0}+d_{n+1,1}.
 \tag{FCT15}
\]
All their central supports are \(z\), since equivalent projections whose sum is central have that common support.

For a nonzero \(p\) in this part, work on \(z=c(p)\) and make these dyadic divisions there. Compare \(d_{n,0}\) with \(p\). If on some nonzero central piece \(w\) one has \(wd_{n,0}\precsim wp\), transport that tile to a subprojection of \(p\). FCT2 extends the transport to a unitary in \(Mw\), so conjugating the whole finite division exhibits the transported projection as a central tile. If this never occurs, central comparison gives \(p\precsim d_{n,0}\) for every \(n\). The projections \(d_{n+1,1}=d_{n,0}-d_{n+1,0}\) are mutually orthogonal and equivalent to \(d_{n+1,0}\). Thus each contains a copy of the same \(p\), contradicting FCT2.

Every nonzero projection in \(M\) now has a nonzero central-tile subprojection: cut it first by \(z_a\) or \(1-z_a\), and use the appropriate construction. A maximal orthogonal family of such tiles below any \(p\) must fill \(p\), because otherwise the residual supplies another tile. This proves exactly the tiling premise of FCT1, with arbitrary orthogonal index sets.

<a id="fct-4"></a>

<a id="oa-flow.fct.4"></a>

## FCT4. Normal center-valued states from cyclic central compressions

We first prove a cyclic abelian fact. If an abelian von Neumann algebra \(A\subseteq B(K)\) has cyclic vector \(\xi\), then \(A'=A\). Let \(R\in A'\) and \(C=\|R\|>0\). Choose \(a_n\in A\) with \(a_n\xi\to R\xi\). Put

<a id="equation-fct16"></a>

\[
 r_n=1_{(2C,\infty)}(|a_n|),\qquad b_n=a_n(1-r_n).
 \tag{FCT16}
\]
CF6 constructs \(|a_n|\); S1 puts these bounded threshold projections in \(A\). Since \(R\) commutes with \(r_n\),

<a id="equation-fct17"></a>

\[
\begin{gathered}
\tfrac12\|a_nr_n\xi\|\\
\le\|a_nr_n\xi\|-C\|r_n\xi\|\\
\le\|r_n(a_n-R)\xi\|\\
\le\|(a_n-R)\xi\|.
\end{gathered}\tag{FCT17}
\]
The first inequality uses the spectral bound \(|a_n|\ge2C\) on \(r_n\). We have \(\|b_n\|\le2C\) and \(b_n\xi\to R\xi\). For \(a\in A\), commutation gives \(b_na\xi\to Ra\xi\). The common norm bound extends strong convergence from the dense set \(A\xi\) to every vector in \(K\). Strong closedness yields \(R\in A\). The zero operator needs no truncation. The approximation sequence concerns one vector; it does not assume that \(K\) is separable.

Apply PC7's vector-support construction to the concrete algebra \(Z\). The support of \(\omega_\xi|_Z\) is the projection onto \(\overline{Z'\xi}\), belongs to \(Z\), fixes \(\xi\), and makes the restricted vector functional faithful on that central corner. Choose a maximal orthogonal family of nonzero such central supports \(z_i\), with vectors \(\xi_i\in z_iH\). Their join is one: a nonzero remaining central corner contains a vector with a nonzero support below it.

Let \(K_i=\overline{Z\xi_i}\), and let \(q_i\) project onto \(K_i\). This subspace reduces \(Z\), so \(q_i\in Z'\) and \(q_i\le z_i\). The compression

<a id="equation-fct18"></a>

\[
 \theta_i:Zz_i\longrightarrow B(K_i),\qquad \theta_i(z)=z|_{K_i}
 \tag{FCT18}
\]
is a unital normal representation: its vector-series tests are restrictions of the ambient tests. It is faithful because \(\theta_i(z)=0\) gives \(\|z\xi_i\|^2=0\), and the support construction makes the functional faithful on \(Zz_i\). ST2 therefore proves that its image is a von Neumann algebra and its inverse on that image is normal on the entire domain.

For \(x\in M\), the compressed operator \((q_ixq_i)|_{K_i}\) commutes with \(\theta_i(Zz_i)\), since both \(x\) and \(q_i\) commute with \(Z\). Its commutant equals that cyclic abelian algebra by the proof above. Consequently

<a id="equation-fct19"></a>

\[
 E_i(x)=\theta_i^{-1}((q_ixq_i)|_{K_i})\in Zz_i
 \tag{FCT19}
\]
is well defined, positive and normal; \(E_i(1)=z_i\) and \(E_i(zx)=zE_i(x)\). FCT0 gives \(\|E_i\|=1\). The bounded central diagonal sum

<a id="equation-fct20"></a>

\[
 E(x)=\sum_i E_i(x)
 \tag{FCT20}
\]
exists strongly by PC1, since the summands have orthogonal central supports and norm at most \(\|x\|\). It is a unital positive linear center-module map.

Its full normality needs an arbitrary-index check. If \(\omega\in Z_*^+\), then \(\sum_i\omega(z_i)=\omega(1)\): finite sums of the projections increase strongly to one and CP's tail estimate applies. Only countably many of these values are nonzero, since at most finitely many exceed \(1/n\). Each positive normal \(\omega\circ E_i\) has norm \(\omega(z_i)\), by FCT0. Their sum therefore converges in norm in \(M_*\), and evaluation of the bounded central sum shows that it is \(\omega\circ E\). Formula (FCT5) proves the same assertion for all \(\omega\in Z_*\). Hence \(E\) is normal, without sigma-finiteness or a direct integral of \(M\).

<a id="fct-5"></a>

<a id="oa-flow.fct.5"></a>

## FCT5. A corner with arbitrarily small trace distortion

Fix the normal center-valued state \(E\) and a number \(a>1\). We construct a nonzero projection \(p\) with \(E(p)\ne0\) such that

<a id="equation-fct21"></a>

\[
 E(xx^*)\le aE(x^*x)\quad(x\in pMp).
 \tag{FCT21}
\]
In central inequalities, a positive element with support \(z\) is positive on its whole central support; this does not assert a uniform positive lower bound.

First choose a maximal orthogonal family of nonzero projections with zero \(E\)-value. Its sum \(q\) has \(E(q)=0\) by normality. Set \(r=1-q\); then \(E(r)=1\), and \(E\) is faithful on \(rMr\). Indeed a nonzero positive \(b\in rMr\) with zero value has a nonzero spectral projection \(e=1_{[\delta,\infty)}(b)\), and \(0\le\delta E(e)\le E(b)=0\), contradicting maximality. For \(e\le r\),

<a id="equation-fct22"></a>

\[
 s_Z(E(e))=c_M(e).
 \tag{FCT22}
\]
One inclusion follows from the center-module identity. Conversely \(zE(e)=0\) implies \(E(ze)=0\), hence \(ze=0\) by faithfulness. This proves the reverse inclusion.

Inside \(r\), choose a maximal family of pairs \((e_i,f_i)\) with separately orthogonal initial and final families, \(e_i\sim f_i\ne0\), and

<a id="equation-fct23"></a>

\[
\begin{gathered}
E(e_i)-E(f_i)\ge0,\\
s_Z(E(e_i)-E(f_i))=c(e_i)=c(f_i).
\end{gathered}
\tag{FCT23}
\]
Chain unions supply the maximal family. Its partial-isometry sum gives \(\sum_i e_i\sim\sum_i f_i\). Put \(e=r-\sum_i e_i\) and \(f=r-\sum_i f_i\). FCT2 gives \(e\sim f\). They are nonzero: for an empty family both equal \(r\); otherwise normality gives \(E(f)-E(e)=\sum_i(E(e_i)-E(f_i))\ge0\), with at least one nonzero positive summand. Thus \(f\ne0\), and equivalence gives \(e\ne0\).

For equivalent \(e'\le e\), \(f'\le f\), maximality forces \(E(e')\le E(f')\). If not, cut both projections by the nonzero central positive spectral support of \(E(e')-E(f')\). On this cut the difference is positive with full central support; (FCT22) and equivalence ensure nonzero matching projections. That pair would extend the family, a contradiction.

Let \(\mu\) be the infimum of the scalars \(c\in[0,1]\) such that \(E(e')\le cE(f')\) for all these equivalent pairs. The set contains one and is closed, because the positive cone is norm closed. A decreasing sequence of admissible scalars tending to its infimum proves that \(\mu\) itself is admissible. It is positive: the pair \(e,f\) and \(E(e)\ne0\) exclude zero.

Since \(\mu/a<\mu\) is not admissible, there is a matching pair \(\widetilde e\le e,\ \widetilde f\le f\) for which \(aE(\widetilde e)\not\le\mu E(\widetilde f)\). Cut by the nonzero positive central spectral support of that difference. Relabel the cuts; then they are still equivalent and

<a id="equation-fct24"></a>

\[
 D=aE(\widetilde e)-\mu E(\widetilde f)\ge0,
 \qquad D\ne0.
 \tag{FCT24}
\]
The first matching-family bound also holds on these central cuts, since it holds for every pair below \(e,f\).

Choose a second maximal separately orthogonal matching family \((\widehat e_j,\widehat f_j)\) below \(\widetilde e,\widetilde f\) satisfying

<a id="equation-fct25"></a>

\[
 aE(\widehat e_j)\le\mu E(\widehat f_j).
 \tag{FCT25}
\]
Let \(p=\widetilde e-\sum_j\widehat e_j\) and \(q=\widetilde f-\sum_j\widehat f_j\). FCT2 gives \(p\sim q\). They are nonzero: if \(p=0\), equivalence gives \(q=0\); normal summation of (FCT25) would contradict (FCT24). Also \(E(p)\ne0\), since \(p\le r\).

For every matching pair \(p'\le p,q'\le q\), we have \(aE(p')\ge\mu E(q')\). A nonzero negative central spectral part of their difference would cut out a new pair satisfying (FCT25). The cut is nonzero by (FCT22) and preservation of central support, so maximality rules it out. For equivalent \(p_1,p_2\le p\), transport \(p_1\) through a fixed equivalence \(p\sim q\), obtaining \(q'\le q\) equivalent to both. Therefore

<a id="equation-fct26"></a>

\[
 E(p_1)\le\mu E(q')\le aE(p_2).
 \tag{FCT26}
\]
The factor \(\mu\) is present in both comparisons.

If \(b\in(pMp)_+\) and \(u\) is a unitary of that corner, approximate \(b\) in norm by finite nonnegative combinations of its spectral projections. Each projection and its \(u\)-conjugate are equivalent below \(p\). Applying (FCT26) term by term and taking the norm limit gives \(E(ubu^*)\le aE(b)\). For \(x\in pMp\), PC1 polar decomposition and FCT2 extend its partial isometry to a corner unitary \(u\), with \(xx^*=u(x^*x)u^*\). This proves (FCT21) on the full corner, including noninvertible \(x\).

<a id="fct-6"></a>

<a id="oa-flow.fct.6"></a>

## FCT6. Moving the corner estimate to the whole algebra

Use FCT3 to choose a nonzero central tile \(p_1\le p\), with equivalent orthogonal \(p_1,\ldots,p_k\) filling a central unit \(z_0\). It still satisfies (FCT21) on its corner, and \(E(p_1)\ne0\) by faithfulness on \(r\). Choose partial isometries

<a id="equation-fct27"></a>

\[
\begin{gathered}
v_i^*v_i=p_i,\qquad v_iv_i^*=p_1,\\
F(x)=\sum_{i=1}^kE(v_ixv_i^*)\quad(x\in Mz_0).
\end{gathered}
\tag{FCT27}
\]
This finite sum is a normal positive center-module map. For \(x\in Mz_0\), all \(v_ixv_j^*\) belong to \(p_1Mp_1\). Thus the entire matrix calculation is

<a id="equation-fct28"></a>

\[
\begin{aligned}
 F(xx^*)&=\sum_{i,j}E((v_ixv_j^*)(v_ixv_j^*)^*)\\
 &\le a\sum_{i,j}E((v_ixv_j^*)^*(v_ixv_j^*))\\
 &=a\sum_{i,j}E(v_jx^*p_ixv_j^*)
 =aF(x^*x).
\end{aligned}
 \tag{FCT28}
\]
Both resolutions of the identity are the actual finite sums \(\sum_i p_i=z_0\). Also \(F(z_0)=kE(p_1)\), a nonzero central positive element supported on \(z_0\), by (FCT22).

Choose \(\delta>0\) with \(w=1_{[\delta,\infty)}(F(z_0))\ne0\). On \(w\), the central inverse \(h=(F(z_0)|_w)^{-1}\) is bounded and positive by S1; it is extended by zero outside \(w\). Define

<a id="equation-fct29"></a>

\[
 \phi_w(x)=hF(x),\qquad x\in Mw.
 \tag{FCT29}
\]
It is normal and positive, is a \(Zw\)-module map, has \(\phi_w(w)=w\), and satisfies \(\phi_w(xx^*)\le a\phi_w(x^*x)\). Normality of multiplication by \(h\) follows from the vector-series substitution in FCT0. Its norm is one by (FCT3). No unbounded inverse is multiplied into a normal map.

This construction works inside every nonzero central corner of \(M\), with the same prescribed \(a>1\). Choose a maximal orthogonal family of central projections \(w_j\) carrying these maps. A nonzero remaining central corner would supply another, so \(\sum_jw_j=1\). Define

<a id="equation-fct30"></a>

\[
 \phi_a(x)=\sum_j\phi_{w_j}(w_jx).
 \tag{FCT30}
\]
The diagonal sum exists with norm bound \(\|x\|\), by PC1. It is unital, positive and a center-module map; the distortion estimate holds on each orthogonal central component and hence globally. Its full ultraweak normality follows by the FCT4 summable-predual argument: for \(\omega\in Z_*^+\) each summand has functional norm \(\omega(w_j)\), whose total is \(\omega(1)\); use (FCT5) for general \(\omega\). This proves the normality of the whole assembly, for arbitrary index sets.

Choose, for example, \(a_n=1+2^{-n}\). FCT3 and FCT6 now verify both premises of the conditional stability lemma FCT1. It gives the normalized normal center-valued trace \(T\) in (FCT1).

<a id="fct-7"></a>

<a id="oa-flow.fct.7"></a>

## FCT7. Faithfulness, uniqueness and projection comparison

For every central tile in (FCT6), traciality and normalization give

<a id="equation-fct31"></a>

\[
 T(p)=z/k.
 \tag{FCT31}
\]
A nonzero projection \(q\) contains a nonzero tile \(p\), so \(T(q)\ge T(p)>0\). If \(x\ge0\) is nonzero, some positive spectral cutoff \(q=1_{[\delta,\infty)}(x)\) is nonzero; S1 proves this directly whenever \(0<\delta<\|x\|\). Then \(T(x)\ge\delta T(q)>0\). Thus \(T\) is faithful on the entire positive cone, and \(T(x^*x)=0\) implies \(x=0\).

Any other **normal** normalized center-valued trace has the same value (FCT31) on every central tile. FCT3 decomposes each projection into tiles, and normality identifies its value with their arbitrary positive sum. Therefore the two traces agree on all projections. Uniform spectral step approximation and boundedness then give equality on all self-adjoint elements and hence all of \(M\). This is uniqueness among normal traces; it does not assume or assert normality of an arbitrary algebraic trace.

For projections, the full order criterion is

<a id="equation-fct32"></a>

\[
\begin{gathered}
p\precsim q\ \Longleftrightarrow\ T(p)\le T(q),\\
p\sim q\ \Longleftrightarrow\ T(p)=T(q).
\end{gathered}
\tag{FCT32}
\]
The forward implication uses the implementing partial isometry and positivity. Conversely PC2 splits centrally into \(zp\precsim zq\) and \((1-z)q\precsim(1-z)p\). On the second piece, place a copy of \((1-z)q\) under \((1-z)p\). The positive residual has nonnegative trace, whereas \(T(p)\le T(q)\) makes its trace nonpositive. Faithfulness makes that residual zero, so the reverse subequivalence there is an equivalence. Add the two central implementations to get \(p\precsim q\). Equality of traces gives both subequivalences; PC3 gives equivalence. This proof includes zero projections.

The support identity is \(s_Z(T(p))=c(p)\): \(T(p)\) is supported on \(c(p)\); a central \(z\) annihilating \(T(p)\) gives \(T(zp)=0\), hence \(zp=0\) by faithfulness.

The converse existence assertion is also precise. If an arbitrary von Neumann algebra has a normal normalized center-valued trace, it is finite. Otherwise PC5 supplies a nonzero properly infinite central unit \(z\), split as \(z=r+s\) with \(r\sim s\sim z\). The trace law gives \(T(r)=T(s)=T(z)=z\), while additivity gives \(T(z)=2z\), a contradiction. After finiteness is established, the preceding construction and normal uniqueness prove that any such trace is faithful. No scalar-trace existence theorem was used to prove this implication.

<a id="fct-8"></a>

<a id="oa-flow.fct.8"></a>

## FCT8. Naturality and sigma-finiteness of the center

A unital star automorphism \(\alpha\) of a von Neumann algebra preserves positive order and its bounded increasing suprema: transport any upper bound through its inverse. It and its inverse are bounded by CF6 contractivity. The positive-map criterion S2 then proves ultraweak continuity on the entire domain. The restriction preserves the center, since commutators transport through \(\alpha\).

For finite \(M\), the map \(S=\alpha^{-1}\circ T\circ\alpha\) is a normal normalized positive center-module trace. Uniqueness from FCT7 implies

<a id="equation-fct33"></a>

\[
 T(\alpha(x))=\alpha(T(x)).
 \tag{FCT33}
\]
Thus naturality includes every unital star automorphism; the only added normality premise is the earlier proved S2 criterion, not an assumed continuity of an algebraic map.

Use the sigma-finite convention that an algebra admits a faithful normal state; its equivalence to countable decomposability is proved in PC7. Restriction of such a state from \(M\) to \(Z\) is faithful and normal. Conversely a faithful normal state \(\omega\) on \(Z\) gives a faithful normal state \(\omega\circ T\) on \(M\): for nonzero \(x\ge0\), faithfulness of \(T\) and then of \(\omega\) give a strictly positive value. Hence

<a id="equation-fct34"></a>

\[
\begin{gathered}
M\text{ finite}:\\
M\text{ sigma-finite}\ \Longleftrightarrow\ Z(M)\text{ sigma-finite}.
\end{gathered}
\tag{FCT34}
\]
In particular every nonzero finite factor admits a faithful normal tracial state, by taking the scalar state of its center. More generally FCT4's maximal central supports \(z_i\) admit faithful normal central vector states; composition with \(T|_{Mz_i}\) makes each \(Mz_i\) sigma-finite. Their arbitrary central sum is all of \(M\). This decomposition is obtained after the trace construction, and was not a countability reduction in its proof.

Every positive normal functional \(\omega\) on \(Z\) produces a finite normal scalar trace \(\omega\circ T\). These traces separate \(M_+\): if \(T(x)>0\), some central vector functional is strictly positive on it. This states precisely the scalar consequence without presuming a faithful scalar state on an arbitrary center.

<a id="ca-definitions"></a>

## Finite unitary averages

*Programme exposition by GPT-6.1 Sol (OpenAI). The argument proves simultaneous norm convergence before identifying the finite-algebra central limit.*

Let \(M\) be a von Neumann algebra and \(Z=Z(M)\). No separability or sigma-finiteness is assumed in this extracted argument. Put
\[
\begin{aligned}
D(a)&=\overline{\operatorname{co}}^{\,\|\cdot\|}
\{uau^*:u\in\mathcal U(M)\},\\
D_{\mathrm w}(a)&=\overline{\operatorname{co}}^{\,\sigma\text{-weak}}
\{uau^*:u\in\mathcal U(M)\}.
\end{aligned}
\tag{0.1}
\]
An **averaging map** is a finite convex combination
\[
\begin{gathered}
F(x)=\sum_{j=1}^r t_j u_jxu_j^*,\\
t_j\geq0,\quad \sum_jt_j=1.
\end{gathered}\tag{0.2}
\]
These maps are positive, unital, contractive and fix \(Z\). Their composites are averaging maps. In particular
\[
\operatorname{dist}(F(x),Z)\leq\operatorname{dist}(x,Z).
\tag{0.3}
\]

<a id="ca1"></a>

## CA1. Shrinking the spectral width

For a self-adjoint \(h\) in a nonzero central corner \(Mz\), write
\[
\begin{aligned}
\alpha_z(h)&=\min\sigma_{Mz}(hz),\\
\beta_z(h)&=\max\sigma_{Mz}(hz),\\
w_z(h)&=\beta_z(h)-\alpha_z(h).
\end{aligned}
\]
The zero-width case is already scalar in that corner.

**Lemma 1.1.** For \(h=h^*\in M\), there are a central projection \(z\) and a self-adjoint unitary \(u\) such that \(k=(h+uhu^*)/2\) satisfies
\[
w_z(k)\leq\tfrac34w_1(h),\qquad
w_{1-z}(k)\leq\tfrac34w_1(h)
\tag{1.1}
\]
on every nonzero indicated corner.

**Proof.** Put \(\alpha=\alpha_1(h)\), \(\beta=\beta_1(h)\), \(m=(\alpha+\beta)/2\), and take the lower spectral projection
\[
p=1_{(-\infty,m]}(h),\qquad q=1-p.
\]
Then
\[
\alpha p\leq hp\leq mp,\qquad
mq\leq hq\leq\beta q.
\tag{1.2}
\]
The comparison theorem gives \(z\in\operatorname{Proj}(Z)\) with \(pz\precsim qz\) and \(q(1-z)\precsim p(1-z)\).

On \(Mz\), choose \(v\) with \(v^*v=pz\), \(vv^*=f\leq qz\). The operator
\[
u_z=v+v^*+(qz-f)
\]
is a self-adjoint unitary in the corner: it exchanges \(pz\) and \(f\), and is the identity on their orthogonal complement. Inequality (1.2) implies
\[
\begin{gathered}
hz\geq\alpha pz+m qz,\\
u_zhzu_z\geq\alpha f+m(pz+qz-f).
\end{gathered}
\]
Therefore
\[
\begin{gathered}
\tfrac12(hz+u_zhzu_z)\\
\geq\tfrac{\alpha+m}{2}(pz+f)+m(qz-f)\\
\geq\tfrac{\alpha+m}{2}z.
\end{gathered}
\]
The upper bound is \(\beta z\). Their difference is \(3(\beta-\alpha)/4\).

On \(M(1-z)\), exchange \(q(1-z)\) with a subprojection of \(p(1-z)\), using a partial isometry in the other comparison. The reversed estimates give
\[
\alpha(1-z)\leq k(1-z)
\leq\tfrac{\beta+m}{2}(1-z).
\]
Its width has the same bound. The sum of the two corner unitaries gives \(u\). Zero corners can be omitted. \(\square\)

**Corollary 1.2.** For every self-adjoint \(h\) and every \(\varepsilon>0\), some averaging map \(F\) and \(c\in Z_{\mathrm{sa}}\) satisfy
\[
\|F(h)-c\|<\varepsilon.
\tag{1.3}
\]

**Proof.** Start with the central partition \(\{1\}\). Apply Lemma 1.1 separately in every nonzero member of the current finite partition, combine the corner unitaries into a global unitary, and refine the partition by the resulting comparison cuts. After \(n\) steps the largest corner width is at most
\[
(3/4)^n w_1(h).
\]
For the final averaged operator, take \(c\) to be the sum of the corner spectral midpoints multiplied by their central projections. The spectral theorem bounds the norm error by half the largest width. Choose \(n\) large enough. \(\square\)

The comparison cut can change at every step. The proof controls a finite central partition, rather than asserting that the global spectral width itself always shrinks.

<a id="ca2"></a>

## CA2. Simultaneous averages and an actual central limit

**Lemma 2.1.** Given \(a_1,\ldots,a_m\in M\) and \(\varepsilon>0\), there is one averaging map \(F\) such that
\[
\operatorname{dist}(F(a_i),Z)<\varepsilon\quad(1\leq i\leq m).
\tag{2.1}
\]

**Proof.** List the real and imaginary parts of the \(a_i\). Apply Corollary 1.2 to the first, then to the image of the second under the first average, and continue through the finite list. Once an image is within \(\varepsilon/2\) of \(Z\), subsequent averages preserve this bound by (0.3). The final composite works for every \(a_i\), because distance to \(Z\) is subadditive and invariant under scalar multiplication. \(\square\)

**Theorem 2.2.** For every finite family \(a_1,\ldots,a_m\), there is a sequence of averaging maps \(F_n\) and \(c_1,\ldots,c_m\in Z\) such that
\[
\|F_n(a_i)-c_i\|\longrightarrow0
\quad(1\leq i\leq m).
\tag{2.2}
\]
Every norm-closed convex subset of \(M\) invariant under unitary conjugation, if nonempty, meets \(Z\).

**Proof.** Choose an average \(F_1\) making each distance to \(Z\) less than \(2^{-1}\). Inductively apply Lemma 2.1 to the family \(F_n(a_i)\), with error \(2^{-(n+1)}\), and put
\[
F_{n+1}=G_{n+1}F_n.
\]
Choose \(c_{i,n}\in Z\) with \(\|F_n(a_i)-c_{i,n}\|<2^{-n}\). Since \(G_{n+1}\) fixes the centre,
\[
\begin{aligned}
&\|F_{n+1}(a_i)-F_n(a_i)\|\\
&=\|G_{n+1}(F_n(a_i)-c_{i,n})\\
&\qquad -(F_n(a_i)-c_{i,n})\|\\
&<2^{1-n}.
\end{aligned}
\tag{2.3}
\]
The series of these bounds converges, so each image sequence is norm Cauchy. Its limit is central because its distance to \(Z\) tends to zero and \(Z\) is norm closed.

For a nonempty invariant convex set, choose any \(a\) in it. Every averaged image of \(a\) belongs to the set, and its central norm limit belongs by closedness. \(\square\)

In particular \(D(a)\cap Z\ne\varnothing\). An approximate approach to the centre alone would not prove this: the centre need not be norm compact. Estimate (2.3) provides convergence.

<a id="ca3"></a>

## CA3. Finite algebras and uniqueness

**Theorem 3.1.** The following are equivalent:

1. \(M\) is finite.
2. \(D(a)\cap Z\) is a singleton for every \(a\in M\).
3. \(D_{\mathrm w}(a)\cap Z\) is a singleton for every \(a\in M\).

In the finite case both singletons are \(\{T_M(a)\}\), where \(T_M\) is the existing centre-valued trace.

**Proof.** If \(M\) is finite, the trace proved in FCT0–FCT7 is normal, bounded, fixes \(Z\), and satisfies \(T_M(uau^*)=T_M(a)\). It is therefore constant on both hulls in (0.1). Any central point in either hull equals its own trace and hence equals \(T_M(a)\). Theorem 2.2 supplies a central point in the smaller hull, proving all the finite-case assertions.

Clearly condition 3 implies condition 2. We prove the converse to finiteness by an explicit witness. If \(M\) is not finite, the central decomposition proved in PC5 gives a nonzero central projection \(z\) with \(Mz\) properly infinite. In that corner choose orthogonal \(p,r\), both equivalent to \(z\). Then \(p\sim z\), and \(z-p\sim z\) as well: it contains \(r\sim z\) and is at most \(z\), so projection Schröder–Bernstein applies.

For every \(n\geq2\), partition \(z=q_1+\cdots+q_n\) with \(q_j\sim z\). To construct such a finite partition, put \(n\) orthogonal copies of \(z\) inside \(z\), and absorb the remainder into the last copy by Schröder–Bernstein. For each \(j\), both \(q_j\) and \(z-q_j\) are equivalent to \(z\). The equivalences \(p\sim q_j\) and \(z-p\sim z-q_j\) combine into a unitary of \(Mz\) carrying \(p\) to \(q_j\). Extending by \(1-z\) gives a unitary in \(M\). Their average sends \(p\) to \(z/n\), so
\[
0\in D(p).
\]
Also \(p\) and \(z-p\) are unitarily conjugate. Thus
\[
D(p)=D(z-p)=z-D(p),
\]
and \(z\in D(p)\) as well. Two different central points contradict condition 2. \(\square\)

The quantifier “for every \(a\)” matters. Even an infinite algebra has singleton central hulls for its central elements.

**Corollary 3.2.** For every norm-closed two-sided ideal \(I\) of a finite \(M\),
\[
T_M(I)=I\cap Z.
\tag{3.1}
\]

**Proof.** If \(a\in I\), all its unitary conjugates, averages and norm limits lie in \(I\). Theorem 3.1 therefore gives \(T_M(a)\in I\cap Z\). Conversely \(T_M\) fixes \(I\cap Z\). \(\square\)

<a id="gs1"></a>

## GS1. A normal trace on any corner extends to its central support

**Theorem.** Let \(e\) be any projection in a von Neumann algebra \(M\), and let \(\theta:(eMe)_+\to[0,\infty]\) be any normal trace. It need not be faithful, finite or semifinite. There is a unique normal trace \(\rho\) on \(M\) which agrees with \(\theta\) on \((eMe)_+\) and vanishes on \(1-c(e)\). It is faithful on \(Mc(e)\) if and only if \(\theta\) is faithful, and is semifinite if and only if \(\theta\) is semifinite.

**Proof.** If \(e=0\), the zero trace has all the asserted properties, with faithfulness on the zero corner understood vacuously. Otherwise choose a maximal orthogonal family of nonzero projections \(f_i\precsim e\), including \(f_0=e\). Central support comparison in PC2 implies that their sum is \(c(e)\): if the residual \(r\le c(e)\) were nonzero, then \(rMe\ne0\), and its polar bridge would supply another nonzero member. Choose
\[
v_i^*v_i=e_i\le e,\qquad
v_iv_i^*=f_i,\qquad v_0=e.
\]
Here the \(e_i\) need not be orthogonal. Define, for \(x\ge0\),
\[
\rho(x)=\sum_i\theta(v_i^*xv_i).
\tag{GS1}
\]
An arbitrary sum of nonnegative extended real numbers means the supremum of its finite subsums. Addition and nonnegative scaling commute with these sums (with \(0\cdot\infty=0\)). The trace is normal: if \(x_\lambda\uparrow x\), bounded congruence gives \(v_i^*x_\lambda v_i\uparrow v_i^*xv_i\), and normality of \(\theta\) followed by interchanging the two suprema gives
\[
\begin{aligned}
\rho(x)
&=\sup_{F\text{ finite}}\sup_\lambda
       \sum_{i\in F}\theta(v_i^*x_\lambda v_i)\\
&=\sup_\lambda\rho(x_\lambda).
\end{aligned}
\tag{GS2}
\]
For a finite set \(F\), the equality between its sum of suprema and the supremum of its increasing sums follows by taking a common upper index for finitely many prescribed lower bounds. This argument also applies when a supremum is infinite.

For \(a\in M\), set \(b_{ji}=v_j^*av_i\in eMe\). Since \(\sum_jf_j=c(e)\) and this support is central, increasing finite sums give
\[
\begin{gathered}
v_i^*a^*av_i=\sum_j b_{ji}^*b_{ji},\\
v_j^*aa^*v_j=\sum_i b_{ji}b_{ji}^*.
\end{gathered}
\]
Normality and the trace identity of \(\theta\) imply
\[
\begin{aligned}
\rho(a^*a)
&=\sum_{i,j}\theta(b_{ji}^*b_{ji})\\
&=\sum_{i,j}\theta(b_{ji}b_{ji}^*)=\rho(aa^*).
\end{aligned}
\tag{GS3}
\]
There is no conditional interchange of series: either double sum is the supremum of all finite subsums in the product index set, and finite rectangles are cofinal for such subsums.

If \(x\in(eMe)_+\), then \(x^{1/2}v_i\in eMe\). Traciality of \(\theta\) and its normality therefore give
\[
\begin{aligned}
\rho(x)
&=\sum_i\theta(x^{1/2}f_i x^{1/2})\\
&=\theta(x^{1/2}c(e)x^{1/2})=\theta(x).
\end{aligned}
\tag{GS4}
\]
The formula also gives \(\rho(1-c(e))=0\). If \(\rho'\) is another normal trace with these two properties, then \(\rho'(x(1-c(e)))=0\), by the bound \(x(1-c(e))\le\|x\|(1-c(e))\). Normality on the finite sums of \(x^{1/2}f_i x^{1/2}\), followed by its trace identity, gives
\[
\begin{aligned}
\rho'(x)&=\sum_i\rho'(v_i^*xv_i)\\
&=\sum_i\theta(v_i^*xv_i)=\rho(x).
\end{aligned}
\]
This proves uniqueness, hence independence of the chosen family.

If \(\theta\) is faithful and \(\rho(x)=0\) for \(x\in(Mc(e))_+\), then \(v_i^*xv_i=0\) for every \(i\). Consequently \(x^{1/2}v_i=0\), then \(x^{1/2}f_i=0\), and finally \(x^{1/2}=0\). The converse follows by restriction.

It remains to check semifiniteness, including infinite-valued \(\theta\). If \(\rho\) is semifinite and \(0\le y\le x\in(eMe)_+\), then \(y=eye\): the positive square root of \(y\) annihilates \((1-e)H\), because its squared norms there are bounded by those of \(x^{1/2}\). Thus the finite-value approximants under \(x\) for \(\rho\) lie in the corner, and restriction proves semifiniteness of \(\theta\).

Conversely assume \(\theta\) is semifinite. Every nonzero projection \(r\le e\) contains a nonzero projection of finite \(\theta\)-value. Indeed choose nonzero \(0\le b\le r\) with \(\theta(b)<\infty\). Such \(b\) exists by semifiniteness; if \(\theta(r)=0\), take \(b=r\). S1 supplies a nonzero cut \(q\le r\) and \(\delta>0\) such that \(\delta q\le b\), so \(\theta(q)<\infty\). For every \(i\), a maximal orthogonal family \(r_{i\ell}\le e_i\) of such finite-value projections fills \(e_i\). Transfer it to
\[
g_{i\ell}=v_i r_{i\ell}v_i^*\le f_i.
\]
The \(g_{i\ell}\), over all pairs \((i,\ell)\), are orthogonal and sum to \(c(e)\). Formula (GS1) has only its \(i\)-term nonzero on \(g_{i\ell}\), and yields \(\rho(g_{i\ell})=\theta(r_{i\ell})<\infty\). Adjoin \(1-c(e)\), whose value is zero. Let \(P_F\) range over finite sums from this filling orthogonal family. Then \(P_F\uparrow1\), each \(\rho(P_F)<\infty\), and for every \(x\ge0\),
\[
\begin{aligned}
y_F&=x^{1/2}P_Fx^{1/2}\uparrow x,\\
\rho(y_F)&=\rho(P_FxP_F)
          \le\|x\|\rho(P_F)<\infty.
\end{aligned}
\tag{GS5}
\]
The equality is the trace identity applied to \(P_Fx^{1/2}\). Normality now proves (T1a). This argument supplies actual increasing finite-value approximants and does not require an unexamined density-of-definition-ideal equivalence. \(\square\)

The corner-extension theorem includes nonfaithful and infinite-valued normal traces. Its orthogonal cuts give increasing finite-value approximants whenever the corner trace is semifinite.

<a id="gs2"></a>

## GS2. Every projection-semifinite algebra has a faithful normal semifinite trace

Assume every nonzero projection of \(M\) majorizes a nonzero finite projection. Given a nonzero central projection \(z\), choose a nonzero finite \(e\le z\). Its corner \(eMe\) is finite. FCT0–FCT7 supply its faithful normal normalized center-valued trace \(T_e\). A unit vector in \(eH\), restricted to \(Z(eMe)\), defines a positive normal functional \(\varphi\) with \(\varphi(e)=1\). Thus
\[
\theta=\varphi\circ T_e
\]
is a nonzero bounded positive normal scalar trace on \(eMe\).

Let \(q\) be its support, supplied by NP3 in the accompanying tracial-normality foundations: \(q\) is the least projection of full \(\theta\)-value, \(\theta(x)=\theta(qxq)\), and \(\theta|_{qMq}\) is faithful. The trace is invariant under every corner unitary \(u\), so \(uqu^*\) is again its least full-value projection. Uniqueness of the support gives \(uqu^*=q\). S0 then gives \(q\in Z(eMe)\). It is nonzero and finite, and \(\theta|_{qMq}\) is finite and faithful.

GS1 extends this trace to a normal semifinite trace \(\rho_z\) on \(M\), faithful on \(Ms_z\) and zero off \(s_z=c_M(q)\). Here \(0\ne s_z\le z\). The support construction does not assert that the original \(\theta\) was faithful on the whole finite corner.

Choose a maximal family of such traces \((\rho_j)\) with pairwise orthogonal nonzero central supports \(s_j\). A nonzero residual central projection would give another by the preceding construction, so \(\sum_js_j=1\). Define
\[
\tau(x)=\sum_j\rho_j(xs_j),\qquad x\in M_+.
\tag{GS6}
\]
Additivity, homogeneity and normality follow from the same finite-subsums calculation (GS2). Centrality and the trace identity of each \(\rho_j\) give \(\tau(a^*a)=\tau(aa^*)\). If \(\tau(x)=0\), faithfulness on every \(Ms_j\) gives \(xs_j=0\) for all \(j\), hence \(x=0\).

For each \(j\), the GS1 construction supplies an orthogonal family of finite-\(\rho_j\) projections filling \(s_j\). Their union over arbitrary \(j\) is orthogonal, fills one, and has finite \(\tau\)-value on each member, since the other central traces vanish there. Its finite sums \(P_F\) satisfy (GS5) with \(\tau\) in place of \(\rho\). This proves semifiniteness in the exact form (T1a). For \(M=0\), use the zero trace. No countability restriction has entered the construction.

<a id="gs3"></a>

## GS3. The converse and the central formulation

Suppose a faithful semifinite scalar trace \(\tau\) exists; for this direction it need not be normal. For a nonzero projection \(p\), choose nonzero \(0\le b\le p\) with \(\tau(b)<\infty\), using semifiniteness and faithfulness. A nonzero cut \(q\le p\) from S1 satisfies \(\delta q\le b\), hence \(\tau(q)<\infty\). If a partial isometry has initial projection \(q\) and final projection \(q'\le q\), then traciality gives \(\tau(q')=\tau(q)\). Since this number is finite, additivity gives \(\tau(q-q')=0\); faithfulness gives \(q=q'\). Thus \(q\) is finite, proving projection semifiniteness.

Finally suppose only that every nonzero central projection majorizes a nonzero finite projection. Given any nonzero \(p\), choose nonzero finite \(e\le c(p)\). Then \(c(e)c(p)=c(e)\ne0\), so PC2 supplies nonzero equivalent subprojections of \(p\) and \(e\). Finiteness passes to subprojections and through equivalence by PC5, and \(p\) therefore has a nonzero finite subprojection. The reverse implication for central projections is immediate. This proves the equivalence of the two projection formulations and completes all of T1.

<a id="appendix-cf"></a>

## Appendix: continuous calculus and Hilbert tools

*Programme exposition by GPT-6.1 Sol (OpenAI).*

The primitive conventions are complex and real numbers, complete normed spaces, inner products, elementary real differentiation, and the axiom of choice in the programme's ordinary set theory (including ordinal comparison and transfinite recursion). We give the analytic and algebraic tools needed beyond those conventions. A C\*-algebra means a complete complex normed \*-algebra with the C\*-identity. The continuous-calculus results below concern nonzero unital algebras. Only that scope is used here; zero corners are handled separately. Inner products are linear in the first variable.

<a id="OA-FLOW.CF.1"></a>
<a id="oa-flow.cf.1"></a>
### CF1. Choice, norm separation and norm integrals

We first fix the set-theoretic consequence of choice that we use. For any set \(S\), order types of well-orders on its subsets form a set, since their relations are subsets of \(S\times S\). An ordinal larger than all those order types cannot inject into \(S\): an injection would transfer its ordering to a subset of \(S\) and contradict the choice of that ordinal. A choice function on the nonempty subsets of \(S\) now enumerates \(S\) by transfinite recursion: at each stage take its value on the elements not yet taken. This enumeration must exhaust \(S\) before the preceding ordinal, since otherwise it would supply an injection. Its enumeration order well-orders \(S\).

It follows that if every chain in a partially ordered set has an upper bound, there is a maximal element. Well-order the underlying set as just proved. Starting with an upper bound of the empty chain, at each successor stage choose the first element strictly above the last one, if there is one; at a limit stage choose the first upper bound of the chain already constructed. If this never stops, the construction injects an ordinal that cannot inject into the underlying set into that set, a contradiction. At a limit stage the chosen upper bound is distinct from all earlier elements, since the earlier strictly ascending chain has no last element. A stopping successor stage supplies the required maximal element. Thus no later mathematical maximality theorem is imported.

The finite-dimensional compactness used below has this elementary proof. If an open cover of a closed bounded real box had no finite subcover, bisect each coordinate and choose a subbox still having no finite subcover. Repeat. Real completeness supplies a point in all the nested closed boxes, whose diameters tend to zero; an open member of the cover containing that point contains a sufficiently small whole box, a contradiction. A closed subset of a compact space is compact by adding its open complement to a cover, so closed complex discs and compact spectral sets have the same finite-cover property. Continuous images are compact by pulling back covers. A continuous real function on a compact set is bounded by a finite subcover of the sets \(|f|<n\). If its supremum \(m\) were not attained, the sets \(f<m-1/n\) would cover the set, and a finite subcover would force its supremum below \(m\), a contradiction; the infimum is treated with \(-f\). On a compact box a continuous Banach-valued function is uniformly continuous: choose at each centre \(x\) a radius \(2r_x\) on which its change from \(f(x)\) is less than \(\varepsilon/2\), take a finite subcover by the balls of radius \(r_x\), and use the least of those finitely many radii for the distance between two points. Both then lie within \(2r_x\) of the same centre. Finitely many local bounds also prove boundedness. The scalar mean value theorem follows from attained extrema and the two one-sided derivative signs at an interior extremum, first for equal endpoint values and then after subtracting their affine interpolant.

**Norm separation.** A bounded complex-linear functional on a subspace of a complex normed space extends with the same norm. To prove this, first let a real functional \(f\) on \(W\) satisfy \(f(w)\le p(w)\) for a sublinear \(p\). On adding a vector \(v\notin W\), choose

\[
\begin{gathered}
\sup_{w\in W}\bigl(f(w)-p(w-v)\bigr)\\
\le c\le\\
\inf_{w\in W}\bigl(p(w+v)-f(w)\bigr).
\end{gathered}
\]

The left endpoint is at most the right: sublinearity applied to \((w_2+v)+(w_1-v)\) and linearity of \(f\) give this for every pair \(w_1,w_2\). Both endpoints are finite on their required sides by using \(w=0\). The definition \(f(w+tv)=f(w)+tc\) is dominated by \(p\), using separately \(t>0\), \(t<0\), and \(t=0\). Chain unions preserve this property, so the preceding maximality argument extends \(f\) to the whole real space. For a complex functional \(\varphi\), extend \(\operatorname{Re}\varphi\) with \(p(x)=\|\varphi\|\|x\|\), and set \(\Phi(x)=F(x)-iF(ix)\). This is complex linear and extends \(\varphi\). Multiplying \(x\) by a unit scalar makes \(\Phi(x)\) real and nonnegative, so \(|\Phi(x)|\le\|\varphi\|\|x\|\). In particular, for any nonzero \(x\) there is a norm-one functional with \(\Phi(x)=\|x\|\). Consequently

\[\|x\|=\sup_{\|\Phi\|\le1}|\Phi(x)|,\]

and a vector annihilated by all bounded functionals is zero.

For a continuous map \(f:[a,b]\to X\) into a Banach space, its Riemann sums are Cauchy in norm: compare two sums on a common refinement and use uniform continuity times \(b-a\). Completeness defines the integral. Refinement also proves \(\|\int f\|\le\int\|f\|\), and every bounded linear map passes through it. The difference quotient of \(t\mapsto\int_a^t f\) differs from \(f(t)\) by at most its modulus of continuity, proving that this integral has derivative \(f(t)\). If \(g\) is continuously differentiable, the function \(g(t)-\int_a^t g'(s)\,ds\) has derivative zero. Apply each norm-separating functional, and the scalar mean value theorem just proved to its real and imaginary parts, to show that it is constant. Its value at \(a\) is \(g(a)\), so \(g(b)-g(a)=\int_a^b g'\). These statements apply to complex-valued periodic integrals as well. An integral on \([0,\infty)\) exists whenever the integrals of the norm on tails tend to zero.

We also fix the norm-series operation used below. If \(\sum_j\|x_j\|<\infty\), finite subsums form a norm-Cauchy net, since their complementary norm sum can be made arbitrarily small; completeness supplies its limit. Any countable regrouping has the same limit: first keep a finite set with small complementary norm sum, then keep the finitely many groups containing its terms. For two such series in a Banach algebra, the complementary norm sum outside a finite rectangle is bounded by


\[
\begin{gathered}
(\sum_{j\notin J}\|x_j\|)\sum_k\|y_k\|\\
{}+\sum_j\|x_j\|(\sum_{k\notin K}\|y_k\|)
\end{gathered}
\]

.
It tends to zero. Rectangular partial sums converge to the product by continuity of multiplication, so their double sum and regroupings equal that product. For commuting \(x,y\), induction on \(n\), using Pascal's identity, proves the binomial formula for \((x+y)^n\). Together these observations justify every product and regrouping of exponential series used here.

<a id="OA-FLOW.CF.2"></a>
<a id="oa-flow.cf.2"></a>
### CF2. Spectrum in a Banach algebra, without imported complex analysis

Let \(D\) be a nonzero unital Banach algebra with \(\|1\|=1\). If \(\|v\|<1\), the convergent geometric series is the two-sided inverse of \(1-v\). It follows that the invertibles form an open set and inversion is continuous: write \(b=a(1+a^{-1}(b-a))\). Define \(\sigma_D(x)\) by failure of invertibility of \(\lambda1-x\). It is closed and lies in \(|\lambda|\le\|x\|\). On its complement the resolvent \(R(\lambda)=(\lambda1-x)^{-1}\) has the locally norm-convergent expansion

\[R(\lambda+h)=\sum_{k=0}^{\infty}(-h)^kR(\lambda)^{k+1}.\]

Thus it is continuously complex differentiable, with derivative \(-R(\lambda)^2\). No contour theorem is being assumed here.

We need a simple circle calculation. If \(g\) is continuously complex differentiable on an annulus, put \(m(\rho)=(2\pi)^{-1}\int_0^{2\pi}g(\rho e^{it})\,dt\). Differentiating under the integral gives

\[m'(\rho)=\frac1{2\pi i\rho}\int_0^{2\pi}
\frac{\partial}{\partial t}g(\rho e^{it})\,dt=0.\]

Differentiation under the integral follows from the continuous derivative on a compact subannulus and uniform convergence of difference quotients. If \(g\) is defined on a disc including its centre, continuity also gives \(m(\rho)\to g(0)\) as \(\rho\downarrow0\).

The spectrum cannot be empty. Otherwise \(\Phi(R(\lambda))\) is defined and differentiable on the whole plane for every bounded functional \(\Phi\). Its circle mean equals its value at zero. The geometric expansion for \(|\lambda|>\|x\|\) gives \(\|R(\lambda)\|\le(|\lambda|-\|x\|)^{-1}\), so those means tend to zero as \(\rho\to\infty\). All functionals then vanish on \(R(0)\), impossible for an inverse in a nonzero algebra. We have proved that \(\sigma_D(x)\) is nonempty and compact.

Write \(r=\max_{\lambda\in\sigma_D(x)}|\lambda|\). Polynomial factorization shows that \(\lambda\in\sigma_D(x)\) implies \(\lambda^n\in\sigma_D(x^n)\): the commuting factors of \(x^n-\lambda^n1\) include \(x-\lambda1\), and a product of commuting elements is invertible only if every factor is invertible (multiply the inverse product by the other factors to obtain both-sided inverses). Hence \(r\le\|x^n\|^{1/n}\). Conversely, fix \(\rho>r\). Apply the circle calculation on \(|\lambda|>r\) to \(g(\lambda)=\lambda^{n+1}\Phi(R(\lambda))\). On a sufficiently large circle the geometric expansion has circle mean \(\Phi(x^n)\), since all nonconstant integer powers of \(e^{it}\) integrate to zero. The mean is independent of radius. Therefore

\[\|x^n\|\le\rho^{n+1}\max_{|\lambda|=\rho}\|R(\lambda)\|.\]

Norm separation justifies the displayed norm bound from the scalar bounds. Taking \(n\)th roots and then decreasing \(\rho\) to \(r\) proves

\[\lim_{n\to\infty}\|x^n\|^{1/n}=r.\]

The elementary identity

\[
\begin{gathered}
(\lambda1-yx)^{-1}\\
=\lambda^{-1}\bigl(1+y(\lambda1-xy)^{-1}x\bigr)\\
(\lambda\ne0)
\end{gathered}
\]

is verified by multiplication on both sides. Consequently \(xy\) and \(yx\) have the same nonzero spectral points. Finally, a nonzero complex unital Banach division algebra is \(\mathbb C1\): choose a spectral point of \(x\); then \(x-\lambda1\) must be zero because it is noninvertible.

<a id="OA-FLOW.CF.3"></a>
<a id="oa-flow.cf.3"></a>
### CF3. C\*-norms and self-adjoint spectra

The involution is isometric: \(\|x\|^2=\|x^*x\|\le\|x^*\|\|x\|\) and the same inequality for \(x^*\) give equality. The nonzero identity has norm one because its C\*-identity says \(\|1\|^2=\|1\|\). For \(h=h^*\) the norm-convergent exponential \(e^{ith}\) is unitary. Indeed multiplication of absolutely convergent series gives \(e^{ith}e^{-ith}=1\), and taking adjoints gives \((e^{ith})^*=e^{-ith}\). Its norm is one by the C\*-identity. The derivative is \(ih e^{ith}\): on a bounded real interval the series and its termwise derivative converge uniformly by their factorial bounds; integrate the uniformly convergent derivative series, use Section 1 on each partial sum, and differentiate the resulting integral identity.

For \(s>0\) the integral

\[v=\int_0^\infty e^{-st}e^{ith}\,dt\]

converges in norm. Differentiation of the integrand and the fundamental theorem proved in Section 1 give \((s1-ih)v=v(s1-ih)=1\), with \(\|v\|\le1/s\). Applying this to the self-adjoint \(r1-h\) shows that \(r+is-h=i(s1-i(r1-h))\) is invertible. Negative imaginary parts follow by taking adjoints. Thus \(\sigma(h)\subset\mathbb R\). The integral constructs the inverse within the same C*-algebra.

If \(x\) is normal, then \(\|x^2\|^2=\|(x^*x)^2\|=\|x^*x\|^2=\|x\|^4\); the middle equality uses the C\*-identity on the self-adjoint \(x^*x\). Induction yields \(\|x^{2^k}\|=\|x\|^{2^k}\). Section 2's spectral-radius formula now gives \(\|x\|=r(x)\) for every normal \(x\).

**Spectral permanence.** Suppose \(E\subset D\) is a closed unital C\*-subalgebra with the same identity. For self-adjoint \(h\in E\), off-real inverses belong to \(E\) by the integral just proved. If a real \(\lambda1-h\) is invertible in \(D\), its inverses at \(\lambda+i/n\) converge in \(D\) to that inverse, by continuity of inversion. Closure puts the limit in \(E\). Thus \(h\) has the same spectrum in both algebras. For arbitrary \(x\in E\) invertible in \(D\), both \(x^*x\) and \(xx^*\) are self-adjoint and invertible in \(D\), so their inverses belong to \(E\). The elements \((x^*x)^{-1}x^*\) and \(x^*(xx^*)^{-1}\) are respectively a left and a right inverse of \(x\) in \(E\); they agree. Apply this to \(x-\lambda1\) to obtain equality of its two spectra.

<a id="OA-FLOW.CF.4"></a>
<a id="oa-flow.cf.4"></a>
### CF4. Characters and their compact space

In a commutative unital Banach algebra, every proper ideal lies in a maximal proper ideal by Section 1: a union of a chain of proper ideals still omits \(1\). A maximal ideal \(J\) is closed. Its closure is an ideal; if that closure contained \(1\), an element of \(J\) within distance less than one of \(1\) would be invertible by the geometric series, contradicting properness. The quotient by a closed ideal is complete: for a Cauchy sequence of cosets choose a subsequence with successive quotient distances less than \(2^{-n}\), choose lifts of those successive differences of norm less than \(2^{1-n}\), and sum their absolutely convergent series. Its cosets converge; then the original Cauchy sequence converges. The quotient norm is submultiplicative, and its identity has norm one, since an element of the ideal within distance less than one of \(1\) would be invertible. For maximal \(J\), commutativity implies the quotient is a division algebra, hence is \(\mathbb C\) by Section 2. The quotient gives a character, meaning a unital complex algebra homomorphism \(\chi:D\to\mathbb C\).

Characters satisfy \(\chi(x)\in\sigma_D(x)\), since an inverse for \(x-\chi(x)1\) would remain an inverse after applying \(\chi\). Thus \(|\chi(x)|\le\|x\|\) and \(\|\chi\|=1\). Every spectral point arises this way: the principal ideal generated by a noninvertible \(x-\lambda1\) is proper, so enlarge it to a maximal ideal.

For clarity, compactness of the character space needs no unproved Banach–Alaoglu invocation. Embed the characters in

\[P=\prod_{x\in D}\{z\in\mathbb C:|z|\le\|x\|\}\]

by their values. Each factor is compact by finite-dimensional Euclidean compactness. The product is compact by this choice proof. A proper filter extends to an ultrafilter by maximality; maximality forces it to contain one of \(S\) and its complement for every subset \(S\), since otherwise adjoining \(S\) still has the finite-intersection property. In a compact space every ultrafilter converges: the closed sets that are closures of its members have the finite-intersection property and hence a common point; every neighbourhood of that point must belong to the ultrafilter. Conversely, if every ultrafilter converges, a family of closed sets with the finite-intersection property generates a proper filter, extends to an ultrafilter, and its limit belongs to all those sets. These two arguments establish the compactness criterion. An ultrafilter on \(P\) has a limit in every coordinate; each neighbourhood restricting finitely many coordinates belongs to it, so it converges to the tuple of those limits. This proves product compactness. The character equations \(\chi(1)=1\), \(\chi(x+y)=\chi(x)+\chi(y)\), \(\chi(tx)=t\chi(x)\), and \(\chi(xy)=\chi(x)\chi(y)\) define a closed subset of \(P\). The character space \(X\) is therefore compact and Hausdorff, with the topology of coordinate evaluation.

<a id="OA-FLOW.CF.5"></a>
<a id="oa-flow.cf.5"></a>
### CF5. The compact polynomial-density step

We give the exact approximation lemma. On \([0,1]\), the Bernstein polynomial of a continuous \(f\) is

\[B_nf(t)=\sum_{k=0}^n f(k/n){n\choose k}t^k(1-t)^{n-k}.\]

The coefficients are nonnegative and sum to one. Their first and second centred moments are \(0\) and \(t(1-t)/n\), by differentiating \((1-t+ts)^n\) at \(s=1\). For any \(\eta>0\) the total coefficient mass where \(|k/n-t|\ge\eta\) is at most \(1/(4n\eta^2)\). Uniform continuity, followed by this bound on the remaining terms, gives

\[|B_nf(t)-f(t)|\le\omega_f(\eta)+\frac{2\|f\|_\infty}{4n\eta^2}.\]

Choose \(\eta\) first and then \(n\); this proves uniform approximation. Rescaling proves polynomial approximation of \(|t|\) on every compact interval.

Let \(K\) be compact Hausdorff and let \(\mathcal R\subset C(K,\mathbb R)\) be a real algebra containing constants and separating points. Its uniform closure is an algebra. If \(g\) is in that closure, polynomial approximation of absolute value on \([-\|g\|,\|g\|]\) shows \(|g|\) lies in it. Consequently it is closed under pairwise maximum and minimum. Given \(f\in C(K,\mathbb R)\) and \(\varepsilon>0\), for each pair \(p,q\) choose an affine transform \(g_{pq}\in\mathcal R\) of a separating function such that \(g_{pq}(p)=f(p)\) and \(g_{pq}(q)=f(q)\); when \(p=q\), a constant suffices. For fixed \(p\), the open sets where \(g_{pq}>f-\varepsilon\) cover \(K\). Take finitely many, and let \(h_p\) be the maximum of their \(g_{pq}\). It exceeds \(f-\varepsilon\) everywhere and equals \(f\) at \(p\). The sets where \(h_p<f+\varepsilon\) cover \(K\). Take finitely many and form their minimum \(h\). Then \(f-\varepsilon<h<f+\varepsilon\) everywhere. Since \(h\) lies in the closure, so does \(f\). For a complex algebra closed under conjugation, its real-valued part separates points (take real or imaginary parts of a separator), and this argument proves density in \(C(K,\mathbb C)\).

<a id="OA-FLOW.CF.6"></a>
<a id="oa-flow.cf.6"></a>
### CF6. Continuous calculus, with all identifications proved

For a commutative unital C\*-algebra \(D\), set \(\widehat x(\chi)=\chi(x)\) on its compact character space. This map is a unital algebra homomorphism into \(C(X)\). For self-adjoint \(h\), Section 3 shows \(\chi(h)\in\mathbb R\). Splitting an arbitrary \(x\) into self-adjoint real and imaginary parts gives \(\widehat{x^*}=\overline{\widehat x}\). Every element is normal, so Sections 2–4 give

\[\|\widehat x\|_\infty=\max_{\lambda\in\sigma_D(x)}|\lambda|=\|x\|.\]

The image is closed, since it is isometric and \(D\) is complete. It contains constants, is closed under conjugation, and separates distinct characters. Section 5 makes it dense, hence equal to \(C(X)\).

Here \(C(X)\) is complete in its supremum norm: a norm-Cauchy sequence converges pointwise in \(\mathbb C\), the convergence is uniform by the Cauchy bound, and the uniform limit is continuous by a three-term \(\varepsilon\) estimate at each point. Its algebra operations and involution are pointwise, and its C\*-identity is the scalar identity \(|\overline z z|=|z|^2\).

Now let \(a\) be normal in a unital C\*-algebra \(D\). The closed algebra \(E=C^*(1,a)\) is commutative. The map \(\chi\mapsto\chi(a)\) from its character space to \(\sigma_E(a)=\sigma_D(a)\) is surjective by Section 4 and spectral permanence. It is injective because a character's values on \(1,a,a^*\) determine its values on all \*-polynomials and then, by continuity, on their closure \(E\). It is continuous by the coordinate topology. A continuous bijection from a compact space to a Hausdorff space is a homeomorphism: images of closed subsets are compact and hence closed (separate a point outside a compact set by finitely many disjoint neighbourhood pairs). Composing this identification with the inverse Gelfand map constructs an isometric unital \*-isomorphism

\[
\begin{gathered}
\Phi_a:C(\sigma_D(a))\longrightarrow C^*(1,a),\\
\Phi_a(\operatorname{id})=a.
\end{gathered}
\]

We denote \(\Phi_a(f)\) by \(f(a)\). To justify uniqueness without assuming continuity of an algebraic \*-homomorphism, observe that every unital \*-homomorphism \(\pi\) between C\*-algebras is contractive. Algebraic inverse preservation gives \(\sigma(\pi(y))\subset\sigma(y)\); applying normal norm-equals-radius to the self-adjoint \(y=x^*x\) gives \(\|\pi(x)\|^2\le\|x\|^2\). Thus any proposed calculus with the same coordinate is continuous and agrees on \*-polynomials. Those polynomials are dense by Section 5 on the compact subset \(\sigma(a)\subset\mathbb C\), so the calculus is unique.

For completeness, spectra of \(f(a)\) are exactly \(f(\sigma(a))\). In \(C(K)\), a continuous function minus \(\lambda\) is invertible exactly when it is nowhere zero: in that case its reciprocal is continuous; otherwise evaluation at a zero forbids an inverse. The isomorphism and spectral permanence give the claim in \(D\). If \(f\) is continuous and \(g\) is continuous on \(f(\sigma(a))\), the map \(g\mapsto(g\circ f)(a)\) is an isometric unital \*-isomorphism into \(C^*(1,f(a))\): its image is precisely that algebra by coordinate/conjugate-coordinate polynomial density. Uniqueness proves

\[g(f(a))=(g\circ f)(a).\]

If an operator commutes with \(a\) and \(a^*\), it commutes with every \*-polynomial and their norm limits, hence with every \(f(a)\). These statements include all of F1, in particular for self-adjoint \(a\).

<a id="OA-FLOW.CF.7"></a>
<a id="oa-flow.cf.7"></a>
### CF7. Positivity and order

Define \(D_+=\{h=h^*: \sigma(h)\subset[0,\infty)\}\). For a self-adjoint \(h\), the calculus shows

\[
\begin{gathered}
h\in D_+\quad\Longleftrightarrow\\
\|t1-h\|\le t\text{ for some }t\ge0.
\end{gathered}
\]

The forward direction uses \(t=\|h\|\); the reverse puts every real spectral value in \([0,2t]\). This criterion proves that \(D_+\) is closed under nonnegative scaling and addition: add the two norm inequalities and use the triangle inequality. It is norm closed: if \(h_n\ge0\) tends to \(h\), choose one common \(t\) larger than all \(\|h_n\|\) and pass to the limit. It is pointed, because \(h,-h\ge0\) force \(\sigma(h)=\{0\}\) and the self-adjoint norm formula gives \(h=0\). The calculus supplies a positive square root of every positive \(h\).

We still have to prove, rather than assume, that \(x^*x\) is positive. Put \(h=x^*x\). Its real spectrum permits continuous positive and negative parts \(h_+\) and \(h_-\), with \(h=h_+-h_-\) and \(h_+h_-=0\). Let \(v=h_-^{1/2}\) and \(w=xv\). Commuting calculus gives

\[w^*w=vhv=-v^4.\]

Write \(w=k+i\ell\) with \(k,\ell\) self-adjoint. Their squares are positive by spectral mapping, so

\[
\begin{aligned}
ww^*&=2k^2+2\ell^2-w^*w\\
&=2k^2+2\ell^2+v^4\ge0.
\end{aligned}
\]

Section 2's \(xy/yx\) identity says that \(w^*w\) and \(ww^*\) have the same nonzero spectrum. The former has nonpositive spectrum and the latter nonnegative spectrum, so \(\sigma(w^*w)\subset\{0\}\). The self-adjoint norm formula implies \(v^4=0\), hence \(v=0\) by its calculus, and \(h_-=0\). Thus \(x^*x\ge0\).

Conversely, every positive element is a square \(b^*b\) by its positive square root. It follows that \(c^*hc\ge0\) for \(h\ge0\), because it is \((h^{1/2}c)^*(h^{1/2}c)\). This proves order preservation under congruence. The positive square root is unique: if \(b\ge0\) and \(b^2=h\), composition of the calculus for \(b\) with the scalar identity \(\sqrt{t^2}=t\) on \([0,\infty)\) gives \(\sqrt h=b\).

For a positive element, \(h\le t1\) is equivalent to \(\|h\|\le t\) for \(t\ge0\), by its real spectrum and the calculus. Consequently if \(0\le h\le k\), then \(h\le k\le\|k\|1\), so \(\|h\|\le\|k\|\). This proves the abstract statements of F2. The concrete criterion is proved after the Hilbert tools, to avoid a hidden adjoint input.

<a id="OA-FLOW.CF.8"></a>
<a id="oa-flow.cf.8"></a>
### CF8. Hilbert space facts and the concrete positive-operator criterion

Let \(H\) be an arbitrary complex Hilbert space. The zero space gives all the statements immediately; otherwise \(B(H)\) is nonzero and unital. For \(\eta\ne0\), nonnegativity of \(\|\xi-t\eta\|^2\) at \(t=\langle\xi,\eta\rangle/\|\eta\|^2\) proves

\[|\langle\xi,\eta\rangle|^2\le\|\xi\|^2\|\eta\|^2.\]

The case \(\eta=0\) is immediate. For a closed linear subspace \(V\) and \(\xi\in H\), choose \(v_n\in V\) whose squared distances to \(\xi\) tend to their infimum \(m\). The parallelogram identity gives

\[
\begin{aligned}
\|v_n-v_k\|^2
&=2\|\xi-v_n\|^2+2\|\xi-v_k\|^2\\
&\quad-4\left\|\xi-\frac{v_n+v_k}{2}\right\|^2
\longrightarrow0.
\end{aligned}
\]

Completeness and closedness give a minimizer \(v\). Varying \(v\) by \(tw\), for real \(t\) and then purely imaginary \(t\), proves \(\xi-v\perp V\). The decomposition \(\xi=v+(\xi-v)\) is unique. It proves that the orthogonal projection \(P_V\) is linear, contractive, idempotent, and self-adjoint.

Every bounded linear functional \(f\) has the form \(f(\xi)=\langle\xi,\eta\rangle\) for a unique \(\eta\). If \(f\ne0\), its closed kernel has orthogonal complement; project a vector outside that kernel to obtain a nonzero \(v\perp\ker f\). Every \(\xi-(f(\xi)/f(v))v\) lies in the kernel, so

\[f(\xi)=\frac{f(v)}{\|v\|^2}\langle\xi,v\rangle
=\left\langle\xi,\frac{\overline{f(v)}}{\|v\|^2}v\right\rangle.\]

Uniqueness follows by taking the difference vector as a test vector, and Cauchy–Schwarz plus that test gives \(\|f\|=\|\eta\|\). For \(T\in B(H)\) apply this representation to \(\xi\mapsto\langle T\xi,\eta\rangle\). The representing vector is \(T^*\eta\); uniqueness proves linearity in \(\eta\), and its norm is at most \(\|T\|\|\eta\|\). This constructs the adjoint, proves \(T^{**}=T\) and \(\|T^*\|=\|T\|\), and verifies the product-adjoint rule by testing inner products. Moreover

\[\|T\xi\|^2=\langle T^*T\xi,\xi\rangle
\le\|T^*T\|\|\xi\|^2,\]

which, together with submultiplicativity, proves \(\|T^*T\|=\|T\|^2\). A norm-Cauchy sequence of operators has pointwise limits, which define a bounded linear operator and are approached uniformly on the unit ball; this proves completeness of \(B(H)\). Thus it is a C\*-algebra, and all preceding results apply. These arguments prove F3 without a dimensional or separability restriction.

If \(T\in B(H)\) is abstractly positive, write \(T=S^*S\) by Section 7; then \(\langle T\xi,\xi\rangle=\|S\xi\|^2\ge0\). Conversely, suppose that all these quadratic values are real and nonnegative. Reality forces \(T=T^*\): apply the complex polarization identity to the sesquilinear form of \(T-T^*\), whose diagonal is zero. The identity itself follows by expanding the four diagonals at \(\xi\pm\eta\) and \(\xi\pm i\eta\). For a real \(\lambda<0\), Cauchy–Schwarz gives

\[
\begin{gathered}
\|(T-\lambda1)\xi\|\|\xi\|\\
\ge\langle(T-\lambda1)\xi,\xi\rangle\\
\ge|\lambda|\|\xi\|^2.
\end{gathered}
\]

This lower bound makes the range closed: a Cauchy sequence of images has Cauchy preimages. The range is dense, since a vector perpendicular to it is annihilated by the self-adjoint \(T-\lambda1\) and the same lower bound forces that vector to vanish. Therefore \(T-\lambda1\) is bijective with bounded inverse. All negative real numbers are outside the spectrum; all nonreal numbers already are outside it by Section 3. Thus \(T\ge0\) in the abstract sense. This proves the concrete part of F2.

<a id="oa-flow.projection.pc0"></a>

## Appendix: projection comparison

*Programme exposition by GPT-6.1 Sol (OpenAI). The bounded polar proof, arbitrary sums and comparison do not assume trace existence. SF0 means the unitary test in S0, and CP means the concrete-predual foundations. The equation labels NP1–NP6 here identify projection formulas; they are distinct from the named sections in the accompanying foundations.*

<a id="oa-flow.pc.0"></a><a id="pc-0"></a>

### PC-0. The two set-theoretic operations

We need no unproved infinite-cardinal arithmetic. If \(u:A\to B\) and \(v:B\to A\) are injections, set \(A_0=A\setminus v(B)\) and \(D=\bigcup_{n\geq0}(vu)^nA_0\). The map equal to \(u\) on \(D\) and to \(v^{-1}\) on \(A\setminus D\) is a bijection \(A\to B\). The second inverse is defined since \(A_0\subseteq D\). Their images are disjoint because \(vu(D)\subseteq D\). For surjectivity, if \(v(b)\in D\), then \(v(b)\notin A_0\), so \(v(b)\in vu(D)\) and injectivity gives \(b\in u(D)\); otherwise the inverse branch maps \(v(b)\) to \(b\).

An infinite set \(I\) is in bijection with \(I\setminus\{i_0\}\) for any \(i_0\in I\): choose distinct \(i_0,i_1,\ldots\), shift \(i_n\mapsto i_{n+1}\), and fix all other points.

Every infinite set \(I\) has a partition \(I=I_0\sqcup I_1\) with both pieces in bijection with \(I\). Here are details at the choice convention of [CF-1](#oa-flow.cf.1). Well-order \(I\), and identify its cardinal with an infinite initial ordinal \(\kappa\). If any infinite cardinal up to \(\kappa\) failed to have \(|\lambda\times\{0,1\}|=\lambda\), take the least failing one \(\lambda\). Order its pairs first by their ordinal coordinate, then by the second coordinate. The predecessors of any pair have cardinal at most \(2|\beta|+1<\lambda\), by minimality when \(|\beta|\) is infinite and by finiteness otherwise; adjoining one point does not change an infinite cardinal by the preceding shift argument. The order type cannot exceed \(\lambda\): a point at position \(\lambda\) would have \(\lambda\) predecessors. Thus there is an injection of the pairs into \(\lambda\); the converse injection is immediate, and the bijection just proved gives a contradiction. Transport the two images to \(I\).

<a id="oa-flow.projection.pc1"></a>

<a id="oa-flow.pc.1"></a><a id="pc-1"></a>

### PC-1. Corners, supports and arbitrary orthogonal sums

The orthogonal projection onto an intersection of projection ranges commutes with every unitary of \(M'\), since that intersection reduces those unitaries. [SF-0](#s0) puts the projection in \(M\). This supplies all meets. Complements give joins; equivalently a join projects onto the closed span of the ranges. Orthogonal joins are their strong sums.

For \(e\in M\) a projection, \(eMe\) acting on \(eH\) is a concrete von Neumann algebra. Indeed extend a weak operator limit on \(eH\) by zero on \((1-e)H\); it is a weak operator limit of elements of \(M\), hence lies in \(M\) and is compressed by \(e\). The following finite-vector argument gives its bicommutant characterization locally.

For completeness the latter argument uses only Hilbert projection. For a unital \*-algebra \(A\) and a tuple \((\xi_1,\ldots,\xi_n)\), project onto the closed orbit \(\overline{\{(a\xi_j)_j:a\in A\}}\). Its matrix entries commute with \(A\). Every diagonal \(x\in A''\) therefore preserves this space, which contains the original tuple. Thus \(x\) is a strong limit of elements of \(A\), on arbitrary finite tuples. If \(A\) is weak operator closed the limit belongs to \(A\), proving \(A=A''\).

Given \(x\in M\), put \(h=(x^*x)^{1/2}\). The rule \(h\xi\mapsto x\xi\) is a well-defined isometry, because \(\|h\xi\|=\|x\xi\|\). Extend it to \(\overline{hH}=(\ker x)^\perp\), and set it to zero on \(\ker x\). This gives a partial isometry \(v\), with
\[
x=vh,\qquad v^*v=[x^*H],\qquad vv^*=[xH].
\tag{PC1}
\]
The brackets mean projection onto the closed indicated range. The initial range equality follows from \((x^*H)^\perp=\ker x\). Every unitary of \(M'\) commutes with \(x,h\), preserves their kernels and ranges, and therefore commutes with this isometry and its zero summand. [SF-0](#s0) gives \(v\in M\); consequently both support projections lie in \(M\). This proves the entire bounded polar input, including zero and noninjective operators.

Suppose \((v_i)_{i\in I}\subset M\) are partial isometries with initial projections \(p_i\) and final projections \(q_i\), each family separately orthogonal. For every finite \(F\subset I\),
\[
\left\|\sum_{i\in F}v_i\xi\right\|^2
=\sum_{i\in F}\|p_i\xi\|^2\leq\|\xi\|^2.
\tag{NP1}
\]
The scalar sum is the supremum of its finite subsums. For any \(\varepsilon>0\) a finite subsum is within \(\varepsilon^2\) of that supremum, so every complementary finite vector sum has norm at most \(\varepsilon\). Completeness gives a strong limit \(v\); applying the same argument to the adjoints gives their strong limit \(v^*\). The limits commute with \(M'\), hence belong to \(M\). Uniformly bounded strong products converge strongly by expanding their differences, so
\[
v^*v=\sum_i p_i,\qquad vv^*=\sum_i q_i.
\tag{PC2}
\]
Thus equivalences or subequivalences can be added over arbitrary orthogonal index sets. More generally uniformly bounded operators supported on separate orthogonal corners have a strong-star diagonal sum, by the same squared-norm tail estimate.

Composition of implementing partial isometries proves transitivity of \(\precsim\): if \(u^*u=p,\ uu^*\leq q=v^*v,\ vv^*\leq r\), then \((vu)^*(vu)=p\) and \((vu)(vu)^*\leq r\). Adjoints give symmetry of \(\sim\); identity projections give reflexivity.

<a id="oa-flow.projection.pc2"></a>

<a id="oa-flow.pc.2"></a><a id="pc-2"></a>

### PC-2. Central supports and comparison

For a projection \(p\), let \(c(p)\) project onto \(\overline{\operatorname{span}}MpH\). This space reduces \(M\), so its projection commutes with \(M\). It also reduces \(M'\), because \(y'xp\xi=xpy'\xi\). [SF-0](#s0) puts that projection in \(M\); hence \(c(p)\in Z(M)\). It dominates \(p\). Any central projection \(z\geq p\) contains every \(xpH\), so \(c(p)\leq z\). This proves the least-central-projection definition without an imported support theorem.

If \(pMq=\{0\}\), then \(p\) vanishes on \(MqH\), giving \(pc(q)=0\). Since \(c(q)\) is central, minimality gives \(c(p)\leq1-c(q)\). Conversely orthogonal central supports force \(pxq=0\) for every \(x\in M\). We have proved
\[
pMq=\{0\}\quad\Longleftrightarrow\quad c(p)c(q)=0.
\tag{PC3}
\]
When \(pMq\neq0\), polar decomposition of a nonzero \(pxq\) supplies nonzero equivalent projections below \(q\) and \(p\), respectively. Equivalence also preserves central support: every central projection dominating one initial projection dominates the final projection, by commuting through its partial isometry, and conversely.

Take a maximal collection of nonzero partial isometries with separately orthogonal initial projections below \(p\) and final projections below \(q\). Chain unions supply upper bounds, so [CF-1](#oa-flow.cf.1) applies. Let \(v\) be its [PC-1](#oa-flow.projection.pc1) strong-star sum and set \(p_0=p-v^*v,\ q_0=q-vv^*\). A nonzero bridge from \(p_0\) to \(q_0\) could be added, so \(c(p_0)c(q_0)=0\). With \(z=c(q_0)\) we have \(zp_0=0\) and \((1-z)q_0=0\). Compressing \(v\) gives
\[
\begin{gathered}
zp\sim z v^*v\precsim zq,\\
(1-z)q\sim(1-z)vv^*\precsim(1-z)p.
\end{gathered}
\tag{NP2}
\]
This is central comparison for arbitrary projections and arbitrary cardinality.

<a id="oa-flow.projection.pc3"></a>

<a id="oa-flow.pc.3"></a><a id="pc-3"></a>

### PC-3. Mutual subequivalence and the join formula

Suppose \(p\precsim q\) and \(q\precsim p\), implemented by \(u^*u=p,\ uu^*\leq q\) and \(v^*v=q,\ vv^*\leq p\). In the corner with unit \(p\), \(T=vu\) is an isometry. Put
\[
\begin{gathered}
a_0=p-vv^*,\quad a_n=T^na_0(T^*)^n,\\
A=\sum_{n\geq0}a_n,\quad B=uAu^*.
\end{gathered}
\]
Since \(a_0T=0\), the \(a_n\) are orthogonal: for \(m>n\), their product contains \(a_0T^{m-n}=0\). Also \(v^*a_0v=0\) and \(v^*a_{n+1}v=ua_nu^*\), so \(v^*Av=B\). The projection \(p-A\) is at most \(vv^*\). Therefore \(v^*(p-A)\) has initial projection \(p-A\) and final projection \(q-B\). Its initial and final projections are orthogonal to those of \(uA\). Their sum satisfies
\[
\begin{gathered}
W=uA+v^*(p-A),\\
W^*W=p,\qquad WW^*=q.
\end{gathered}
\tag{NP3}
\]
This proves mutual subequivalence implies equivalence, including zero projections.

For \(x=(1-p)q\), its kernel is \((1-q)H\oplus(pH\cap qH)\). Its initial support is therefore \(q-p\wedge q\). Also \(\ker x^*=pH\oplus((1-p)H\cap(1-q)H)\), so its final support is \(p\vee q-p\). [PC-1](#oa-flow.projection.pc1) gives
\[
(p\vee q)-p\sim q-(p\wedge q).
\tag{NP4}
\]

<a id="oa-flow.projection.pc4"></a>

<a id="oa-flow.pc.4"></a><a id="pc-4"></a>

### PC-4. The center of any projection corner

For \(e\neq0\), work in \(Mc(e)\), with identity \(c(e)\). Compression maps \(Z(M)c(e)\) into \(Z(eMe)\). It is injective: a central \(h\) with \(he=0\) annihilates \(MeH\), whose span is dense in \(c(e)H\).

Choose a maximal orthogonal family \((r_i)\) of nonzero projections subequivalent to \(e\), including \(r_0=e\). The residual projection is zero: otherwise PC3 provides a bridge to \(e\) and thus an additional member. Choose \(v_i^*v_i\leq e,\ v_iv_i^*=r_i,\ v_0=e\). For \(h\in Z(eMe)\) define
\[
\widetilde h=\sum_i v_i h v_i^*.
\tag{PC4}
\]
Each summand is supported on \(r_i\) and has norm at most \(\|h\|\); [PC-1](#oa-flow.projection.pc1) supplies the bounded strong-star sum. It compresses to \(h\) at \(e\). For \(x\in Mc(e)\), \(v_i^*xv_j\in eMe\), so it commutes with \(h\). Multiplying this identity by \(v_i,v_j^*\) shows \(r_i\widetilde h x r_j=r_i x\widetilde h r_j\). Since finite sums of \(r_i\) converge strongly to \(c(e)\), all matrix corners determine an operator, and \(\widetilde h\) is central.

Commutation of \(h\) with \(v_i^*v_i\) gives, in each \(r_i\) corner, preservation of products and adjoints; hence extension and compression are inverse unital \*-isomorphisms. Their continuity is also explicit. For vectors \(\xi,\eta\),
\[
\begin{gathered}
\langle\widetilde h\xi,\eta\rangle\\
=\sum_i\langle h v_i^*\xi,v_i^*\eta\rangle,\\
\sum_i\|v_i^*\xi\|^2\leq\|\xi\|^2.
\end{gathered}\tag{PC5}
\]
Only countably many coordinates are nonzero: for each integer \(n\), finitely many squared norms exceed \(1/n\). Thus this is a CP vector-series functional on \(eMe\). A square-summable series of ambient vector pairs remains square summable after these substitutions, by the same inequality and the countable union of their supports. Extension is ultraweakly continuous on its entire domain; compression is too by its vector-pair substitutions. In particular central projections of \(eMe\) are precisely \(ez\), \(z\in Z(M)c(e)\), and this identification preserves bounded increasing suprema.

<a id="oa-flow.projection.pc5"></a>

<a id="oa-flow.pc.5"></a><a id="pc-5"></a>

### PC-5. Finite central parts and properly infinite halving

Finiteness passes to subprojections: a partial isometry from \(r\leq p\) onto a strict subprojection of \(r\), added to \(p-r\), would make \(p\) equivalent to a strict subprojection of itself. Finiteness passes through equivalence by conjugating the corner with its implementing partial isometry. The same corner isomorphism preserves proper infiniteness.

In any projection corner with unit \(e\), choose a maximal orthogonal family of finite central projections. Its sum \(z_f\) is finite. Indeed an equivalence from \(z_f\) to a subprojection commutes with each central summand and restricts there to equality; its full final projection must therefore equal \(z_f\). Every finite central projection is below \(z_f\), since its portion outside \(z_f\), if nonzero, could be added. Hence \(e-z_f\), when nonzero, has no nonzero finite central compression and is properly infinite. This decomposition is unique and, by [PC-4](#oa-flow.projection.pc4), arises from an ambient central split on \(c(e)\).

We prove halving in a corner \(A\) whose unit \(e\) is properly infinite. In every nonzero central corner \(zA\), infiniteness gives \(w^*w=z,\ ww^*<z\). Its defect \(d=z-ww^*\neq0\) has orthogonal equivalent translates \(w^nd(w^*)^n\), because \(dw=0\). Let \(h=c_A(d)\leq z\). Equivalence preserves their common central support \(h\), so they lie in \(hA\) and have full support there.

Extend this countable seed to a maximal orthogonal family \((d_i)_{i\in I}\) equivalent to \(d\) inside \(hA\). Let \(Q=\sum_i d_i,\ r=h-Q\), and fix \(i_0\). Comparison in \(hA\) gives a central \(t\leq h\) with \(rt\precsim d_{i_0}t\) and \(d_{i_0}(h-t)\precsim r(h-t)\). If \(t=0\), another copy of \(d\) fits in \(r\), contradicting maximality. Thus \(t\neq0\).

The infinite family absorbs this residual on \(t\). Every \(d_it\) is nonzero because \(c_A(d_i)=h\), and they remain mutually equivalent by central compression of their implementing partial isometries. Map \(rt\) into \(d_{i_0}t\), and use a bijection \(I\to I\setminus\{i_0\}\) to map \(Qt\) into the other summands. Orthogonal addition gives \(t\precsim Qt\); the reverse subequivalence is inclusion. [PC-3](#oa-flow.projection.pc3) gives \(t\sim Qt\). Partition \(I\) into two pieces each in bijection with \(I\), using [PC-0](#oa-flow.projection.pc0). Their sums in \(Qt\) are each equivalent to \(Qt\). Transport them through the equivalence \(t\sim Qt\). We obtain \(t=r_t+s_t\), with \(r_t\sim s_t\sim t\).

This construction works inside every nonzero central portion of \(e\). A maximal orthogonal family of central portions admitting such a halving must therefore fill \(e\). Adding their halves and their equivalences by [PC-1](#oa-flow.projection.pc1) proves
\[
e=r+s,\qquad r\sim s\sim e.
\tag{NP5}
\]
No countability assumption was used. Repeated splitting is consequently legitimate.

There are countably many orthogonal copies of \(e\) inside \(e\): choose an isometry \(w\) from \(e\) onto \(s\), and put \(e_n=w^n r(w^*)^n\). Their orthogonality follows from \(rw=0\); each is equivalent to \(e\). Their sum \(Q\) contains \(e_0\sim e\), so \(e\precsim Q\leq e\) and [PC-3](#oa-flow.projection.pc3) gives \(Q\sim e\). Transport the family through this equivalence to obtain a filling family
\[
\begin{gathered}
e=\sum_{n\geq0}f_n,\qquad f_n\sim e,\\
f_nf_m=0\ (n\neq m).
\end{gathered}\tag{PC6}
\]
This argument does not incorrectly assume that the first shift's original ranges already fill \(e\).

<a id="oa-flow.projection.pc6"></a>

<a id="oa-flow.pc.6"></a><a id="pc-6"></a>

### PC-6. The finite-join consequence

If \(p,q\) are finite, NP4 makes \(p\vee q-p\) finite. Replace \(q\) by this projection and work in the corner with unit \(p+q\). If that unit were infinite, [PC-5](#oa-flow.projection.pc5) would give a nonzero properly infinite central piece; compress to it. We would have a properly infinite unit \(1=p+q\) with both summands finite.

Choose its halving \(1=r+s,\ r\sim s\sim1\). Compare \(p\wedge r\) and \(q\wedge s\), with central \(z\) satisfying \(z(p\wedge r)\precsim z(q\wedge s)\) and the reverse comparison on \(1-z\). On \(z\), NP4 and orthogonal addition give
\[
\begin{aligned}
zr&=z(r-p\wedge r)+z(p\wedge r)\\
&\precsim z((p\vee r)-p)+z(q\wedge s)\leq zq.
\end{aligned}
\tag{NP6}
\]
The target summands are orthogonal: \(q\wedge s\) is orthogonal to both \(p\) and \(r\), thus to their join. Both lie under \(q\). If \(z\neq0\), \(zr\sim z\) is infinite and cannot be subequivalent to finite \(zq\); hence \(z=0\). On \(1-z\) interchange \(p,r\) with \(q,s\) to get the same contradiction unless \(1-z=0\). This is impossible for a nonzero unit. Therefore \(p\vee q\) is finite. Induction also proves every finite orthogonal sum of finite projections finite.

<a id="oa-flow.projection.pc7"></a>

<a id="oa-flow.pc.7"></a><a id="pc-7"></a>

### PC-7. Countability belongs to the source corner

A faithful normal state on \(fMf\) makes \(f\) countably decomposable. Every nonzero orthogonal subprojection has strictly positive state value. Finitely many can have value at least \(1/n\), since their finite sums have value at most one; taking their union over \(n\) proves countability. No state on \(M\) is inferred.

Conversely suppose \(f\neq0\) is countably decomposable. For a unit vector \(\xi\in fH\), let \(r_\xi\) project onto \(\overline{M'\xi}\). [SF-0](#s0) gives \(r_\xi\in M\), and \(r_\xi\leq f\). The vector functional is faithful on \(r_\xi Mr_\xi\): if a positive \(a\) there has zero value, then \(a^{1/2}\xi=0\), so commutation makes \(a^{1/2}\) zero on the dense orbit \(M'\xi\).

A maximal orthogonal collection of such nonzero \(r_{\xi_j}\leq f\) fills \(f\); a nonzero remainder would contain a vector providing an additional one. It is finite or countable by assumption. With strictly positive \(c_j\) summing to one,
\[
\omega(x)=\sum_j c_j\langle x\xi_j,\xi_j\rangle,\qquad x\in fMf,
\tag{PC7}
\]
is normal by CP's square-summable vector-series description. It is a state. Zero value on positive \(x\) forces \(x^{1/2}\) to vanish on every commutant orbit, hence on their filling sum, proving faithfulness. This proves the exact equivalence of the two corner conventions.

Now let \(e\) be properly infinite and let \(f\) be countably decomposable, with \(c(f)\leq c(e)\). A maximal orthogonal family of nonzero \(q_i\leq f\) with \(q_i\precsim e\) fills \(f\): a nonzero residual \(a\) has \(c(a)c(e)=c(a)\neq0\), so PC3 supplies another subprojection. The family is countable by the hypothesis on \(f\). Use distinct copies \(e_i\sim e\) from [PC-5](#oa-flow.projection.pc5) to place each \(q_i\) under \(e_i\), then add the implementing partial isometries. We have proved
\[
\begin{gathered}
c(f)\leq c(e),\quad e\text{ properly infinite},\\
f\text{ countably decomposable}\\
\Longrightarrow\quad f\precsim e.
\end{gathered}
\tag{PC8}
\]
The zero source case is immediate. In particular two countably decomposable properly infinite projections with the same central support are equivalent by applying PC8 twice and [PC-3](#oa-flow.projection.pc3). The whole ambient algebra need not be countably decomposable.

## Appendix: faithful representations and global inverse normality

*Programme exposition by GPT-6 Astra (OpenAI).*

<a id="oa-flow.st.1"></a>

### ST-1. Compact balls and a useful linear criterion

For any normed space \(E\), place the closed unit ball of \(E^*\) in
\[
\prod_{e\in E}\{z\in\mathbb C:|z|\leq\|e\|\}
\]
by evaluation. Each coordinate disc is compact, including a radius-zero disc. The arbitrary product is compact by the ultrafilter proof in CF Section 4, from the maximal principle proved in CF Section 1. The linearity equations are closed conditions on finitely many coordinates. Their solutions are exactly the functionals of norm at most one, so the dual ball is closed and compact in this product. The inherited topology is precisely the weak-star topology. Thus the unit ball of \(M\) is ultraweakly compact by the concrete duality just bound. This proves compactness for the concrete predual topology.

We also need the following linear criterion. Let \(E\) be Banach, \(X=E^*\), and \(f\in X^*\). If \(f|_{B_X}\) is weak-star continuous at zero, then \(f\) belongs to the canonical copy of \(E\) in \(X^*\).

For \(\varepsilon>0\), continuity supplies \(e_1,\ldots,e_n\in E\) and \(\delta>0\) such that \(|f(x)|\leq\varepsilon\) whenever \(\|x\|\leq1\) and \(|x(e_j)|<\delta\) for all \(j\). Put \(K=\bigcap_j\ker e_j\), with \(e_j\) viewed as a functional on \(X\). Then \(\|f|_K\|\leq\varepsilon\). Hahn–Banach extends \(f|_K\) to \(h\in X^*\) with \(\|h\|\leq\varepsilon\). The functional \(f-h\) vanishes on \(K\), so it factors through the finite-dimensional map \(x\mapsto(x(e_j))_j\). Extending its linear functional on the image to \(\mathbb C^n\) gives
\[
f-h\in\operatorname{span}\{e_1,\ldots,e_n\}\subseteq E.
\tag{ST1}
\]
Thus \(f\) has distance at most \(\varepsilon\) from \(E\). The canonical inclusion \(E\to E^{**}\) is isometric by the norming Hahn–Banach identity in CF Section 1; completeness makes its range closed. Letting \(\varepsilon\downarrow0\) proves the criterion. It is a criterion for linear functionals and is not a general theorem about arbitrary convex sets.


<a id="oa-flow.st.2"></a>

### ST-2. An ultraweakly continuous faithful representation

Suppose \(\pi:M\to B(K)\) is a faithful \*-representation and is ultraweakly continuous. Put \(p=\pi(1)\) and work on \(pK\). It is isometric: contractivity is the C\* estimate in CF6, and if a positive \(b\) lost norm, choose a continuous scalar function zero on \([0,\|\pi(b)\|]\) but nonzero at \(\|b\|\). Continuous functional calculus would give \(f(b)\ne0\) but \(\pi(f(b))=0\). Applying positive norm preservation to \(x^*x\) gives the assertion for every \(x\). Therefore \(A=\pi(M)\) is a C\* algebra and \(\pi(B_M)=B_A\).

The last ball is ultraweakly compact by ST-1 and continuity, hence closed in the Hausdorff ultraweak topology. By HAP05 in the supplied bounded-topology foundations, every contraction in \(A''\subseteq B(pK)\) is a bounded strong limit of contractions in \(A\). BK03/CP06 in that companion prove ultraweak convergence of that net, so compact-ball closedness puts its limit back in \(A\). Thus \(A=A''\). Compression shows it is also ultraweakly closed in \(B(K)\): all limits stay compressed by \(p\), and restricting vector-series tests gives exactly the corner topology.

On the unit balls, \(\pi\) is a continuous bijection from a compact space to a Hausdorff space and hence a homeomorphism. Explicitly a closed subset of the compact ball is compact, its image is compact and therefore closed, proving continuity of the inverse without an additional topological theorem. For \(\omega\in M_*\), the bounded linear functional \(f=\omega\circ\pi^{-1}\) on \(A\) is continuous on \(B_A\). Applying ST-1's criterion to \(A=(A_*)^*\) proves \(f\in A_*\). This holds for every \(\omega\), so \(\pi^{-1}\) is ultraweakly continuous on all of \(A\), not merely on a ball.

Positive normal functionals pull back in both directions, preserving positivity, and
\[
(\omega\circ\pi^{-1})(\pi(x)^*\pi(x))=\omega(x^*x).
\tag{ST2}
\]
These equalities give both directions of the intrinsic \(\sigma\)-strong topology, and applying them also to \(x^*\) gives the \(\sigma\)-strong* topology. On uniformly norm-bounded sets these are the concrete strong and strong* topologies. Here is the full comparison: each positive normal \(\omega\) has a vector series \(\sum_j\langle x u_j,v_j\rangle\); for \(b\geq0\), Cauchy–Schwarz for \(b^{1/2}\) gives
\[
0\leq\omega(b)\leq
\frac12\sum_j\bigl(\langle b u_j,u_j\rangle+\langle b v_j,v_j\rangle\bigr).
\tag{ST3}
\]
At \(b=z^*z\), the right side is a sum of squared vector norms. A uniformly bounded strongly null net makes its finite initial sum tend to zero and its tail uniformly small. Conversely, the positive single-vector tests are among the defining seminorms. Repeat for adjoints. For the weak topology, a bounded weakly convergent net makes each finite initial vector-coefficient sum converge, and the same Cauchy–Schwarz tail bound as BK03/CP06 is uniform; hence bounded weak and ultraweak convergence agree. These arguments apply to arbitrary nets.

Thus the stated topology conclusion holds for every faithful ultraweakly continuous representation, on arbitrary Hilbert spaces and with a possibly proper identity corner. The additional equivalence with the order-normal definition for arbitrary positive maps is not asserted by this proof.

<a id="source-notice"></a>

## Sources and authorship

The finite trace is constructed from center-valued positive maps with arbitrarily small trace distortion. The proof gives central tilings, finite matrix estimates, bounded central normalization, and normality of arbitrary central sums. Norm averaging is developed separately, followed by extension of an arbitrary normal corner trace and construction of a faithful normal semifinite scalar trace. The analytic appendices supply the continuous calculus, projection comparison and faithful-representation results used throughout.

- Jesse Peterson, [*Notes on operator algebras* (2020), §6.4, Lemmas 6.4.1–6.4.9 and Theorem 6.4.10, pp. 102–106](https://math.vanderbilt.edu/peters10/teaching/spring2020/OperatorAlgebras.pdf#page=102): the central-tile, two-family balancing and approximate-trace construction underlying FCT. Sections FCT0–FCT8 give the full arguments at arbitrary-center and arbitrary-Hilbert-space generality.
- Masamichi Takesaki, [*Theory of Operator Algebras I*, V.2, Theorems 2.6 and 2.15, and V.4, Lemmas 4.1–4.5 and Theorem 4.6](https://doi.org/10.1007/978-1-4612-6188-9): finite and semifinite traces and the spectral-width method for unitary averaging. Sections CA1–CA3 use this averaging method, including simultaneous norm limits and the finite-algebra singleton theorem. Sections GS1–GS3 use corner extension and central assembly for scalar traces.
- J. R. Ringrose, [*Lectures on the trace in a finite von Neumann algebra*, Theorem 5.4, pp. 350–352](https://bpb-us-e2.wpmucdn.com/sites.uci.edu/dist/9/3878/files/2019/10/Ringrose.pdf#page=42): a complementary construction through a fixed point in the predual. The proof here uses the approximate-trace construction instead.
- Vahid Shirbisheh, [*Lectures on C-star algebras*, arXiv:1211.3404v2](https://arxiv.org/pdf/1211.3404v2), Theorems 3.1.34 and 3.2.4 and Proposition 4.1.8; Peterson's [2015 notes](https://math.vanderbilt.edu/peters10/teaching/spring2015/OperatorAlgebras.pdf), Theorems 1.1.4, 1.2.6 and 1.3.1 and Proposition 3.0.21; and his [2020 notes](https://math.vanderbilt.edu/peters10/teaching/spring2020/OperatorAlgebras.pdf), §§5.1–5.2: comparison sources for the continuous-calculus and projection proofs.

The FCT, CF, PC and averaging exposition is by GPT-6.1 Sol (OpenAI). The faithful-representation exposition and the bounded-interface and scalar-trace arguments are by GPT-6 Astra (OpenAI). The corner-extension treatment also uses the independently written programme exposition *Traces on von Neumann algebras* by Claude Opus 5.5 (Anthropic), Lemma 6.1 and Theorems 6.2 and 6.7. [Sources and contributions](trace-existence-foundations.provenance.json) identify these programme components.

The original programme exposition in this companion is dedicated to CC0-1.0 to the extent of rights held. The cited human works retain their own rights. The [bounded-topology](bounded-topology-foundations.md) and tracial-normality companions state their own authorship and component terms.
