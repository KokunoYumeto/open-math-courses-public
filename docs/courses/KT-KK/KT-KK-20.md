# The Baum–Connes assembly map and the conjecture

*Written by GPT-6.1 Sol (OpenAI). Public domain (CC0).*


Let \(G\) be second countable and locally compact. All spaces in the construction are locally compact, Hausdorff and second countable, all coefficient algebras are separable and graded, and all group actions preserve grading. A proper action means that \((g,x)\mapsto(gx,x)\) is a proper map. A \(G\)-compact space has compact orbit space. Haar measure is left Haar measure, with modular function defined by
\[
\int_G f(sg)\,ds=\Delta(g)^{-1}\int_G f(s)\,ds.
\tag{A1}
\]
The convolution and involution conventions are those of *Descent and the K-theory of crossed products*, Sections 1–3. That lesson proves both versions of descent, their naturality, their product compatibility and the full-to-reduced compatibility square. The cutoff argument below supplies the other factor in assembly.

## 1. A normalized cutoff on a proper cocompact space

**Lemma A.1.** A proper \(G\)-compact space \(X\) has a nonnegative \(c\in C_c(X)\) such that
\[
\int_G c(s^{-1}x)^2\,ds=1\qquad(x\in X).
\tag{A2}
\]
For compact \(K,L\subset X\), the transporter
\[
T(K,L)=\{g\in G:gK\cap L\ne\varnothing\}
\tag{A3}
\]
is compact.

**Proof.** The inverse image of \(L\times K\) under the proper action map is compact. Its group projection is exactly \(T(K,L)\), proving the last assertion. The orbit map \(X\to X/G\) is open: the inverse image of the image of an open set is the union of its translates. Around each point choose a precompact open neighbourhood \(U\) and a nonnegative compactly supported continuous function positive on \(U\). These functions exist by the proved cutoff construction in [*Noncompact foundations for equivariant induction*, NCF.1](supporting/noncompact-foundations/noncompact-foundations.html#ncf-001). Compactness of \(X/G\) selects finitely many such \(U\)'s whose orbit images cover the quotient. The sum \(b\) of their functions is positive somewhere on every orbit. Its support \(K\) is compact, and \(GK=X\).

Set
\[
h(x)=\int_G b(s^{-1}x)^2\,ds.
\tag{A4}
\]
For \(x\) in a fixed compact neighbourhood \(L\), the integrand vanishes unless \(s\in T(K,L)\). This is one compact integration set for all such \(x\). Continuity and uniform continuity on that compact set make \(h\) continuous there. Its value is positive: if \(b(s_0^{-1}x)>0\), the same inequality holds on a nonempty open neighbourhood of \(s_0\), which has positive Haar measure by [NCF.4](supporting/noncompact-foundations/noncompact-foundations.html#ncf-004). Substitution \(s=gt\), using left invariance, gives \(h(gx)=h(x)\). Thus \(c=b h^{-1/2}\) is continuous, nonnegative and compactly supported, and its orbit integral is \(h(x)/h(x)=1\). All integrals here have compact support locally in \(x\); the proved integration results in [NCF.5](supporting/noncompact-foundations/noncompact-foundations.html#ncf-005) therefore apply. \(\square\)

Write \(D_X=C_0(X)\rtimes G\) and \(D_{X,r}=C_0(X)\rtimes_rG\). Both contain the same compactly supported convolution algebra, with action \((\alpha_g a)(x)=a(g^{-1}x)\).

**Proposition A.2 (the cutoff projection).** The function
\[
p_c(g,x)=\Delta(g)^{-1/2}c(x)c(g^{-1}x)
\tag{A5}
\]
is a projection in \(D_X\), and its image is a projection in \(D_{X,r}\). Its K-theory class is independent of \(c\).

**Proof.** A nonzero value requires \(x\in\operatorname{supp}c\) and \(g^{-1}x\in\operatorname{supp}c\). Lemma A.1 bounds \(g\) in a compact transporter. Thus \(p_c\in C_c(G\times X)\). The involution is
\[
f^*(g,x)=\Delta(g)^{-1}\overline{f(g^{-1},g^{-1}x)}.
\tag{A6}
\]
Inserting (A5) gives \(p_c^*=p_c\). Convolution gives
\[
\begin{aligned}
(p_c*p_c)(g,x)
&=\int_G p_c(s,x)p_c(s^{-1}g,s^{-1}x)\,ds\\
&=\Delta(g)^{-1/2}c(x)c(g^{-1}x)
       \int_G c(s^{-1}x)^2\,ds\\
&=p_c(g,x).
\end{aligned}
\tag{A7}
\]
The identities hold before either completion. In particular, the modular factor in (A5) is needed for self-adjointness when \(G\) is not unimodular.

If \(c_0,c_1\) satisfy (A2), so does
\[
c_t(x)=\sqrt{(1-t)c_0(x)^2+t c_1(x)^2}\quad(0\leq t\leq1).
\tag{A8}
\]
This is a continuous path in the uniform norm, supported in one compact set. Its projections have one compact group support by (A3); their coefficients converge uniformly there. The crossed-product norm is bounded by the group \(L^1\) coefficient norm, so \(t\mapsto p_{c_t}\) is norm continuous in both completions. It is a projection homotopy, proving independence.

There is also an explicit comparison useful later. For normalized \(c,d\), put
\[
v_{c,d}(g,x)=\Delta(g)^{-1/2}c(x)d(g^{-1}x).
\tag{A9}
\]
The same multiplication gives \(v_{c,d}^*=v_{d,c}\) and \(v_{c,d}v_{d,e}=v_{c,e}\). Hence \(v_{c,d}^*v_{c,d}=p_d\) and \(v_{c,d}v_{c,d}^*=p_c\). This is an actual partial isometry in either crossed product. \(\square\)

We write \([p_X]\) for the resulting even class. As a scalar-source KK-cycle it is \((p_cD_{X,(r)},\mathbb C,0)\): the identity of this singly generated module is the compact rank-one operator \(\theta_{p_c,p_c}\), so the zero operator has the required compact defect. The partial isometry (A9) or the projection homotopy (A8) gives the same KK-class for another cutoff. The full-to-reduced quotient sends the full class to the reduced class; no equality of the two crossed-product algebras is required for this assertion.

## 2. Naturality in spaces and coefficients

**Lemma A.3.** Every continuous equivariant map \(f:X\to Y\) between proper \(G\)-compact spaces is proper. Pullback carries the cutoff class of \(Y\) to that of \(X\):
\[
[p_Y]\widehat\otimes_{D_{Y,(r)}}[f^*\rtimes_{(r)}G]=[p_X].
\tag{A10}
\]

**Proof.** By Lemma A.1 choose a compact \(K\subset X\) with \(GK=X\). For compact \(L\subset Y\), write \(x=gk\in f^{-1}(L)\). Then \(g f(k)\in L\), so \(g\in T(f(K),L)\). Consequently \(f^{-1}(L)\) is a closed subset of the compact set \(T(f(K),L)K\), and is compact. Pullback is therefore a homomorphism \(f^*:C_0(Y)\to C_0(X)\). It is nondegenerate, since a function equal to one on \(f(K')\), for compact \(K'\subset X\), acts as one on every function supported in \(K'\).

If \(c_Y\) is a normalized cutoff, \(c_Y\circ f\) is compactly supported by properness and is normalized by equivariance. Pullback of (A5) is exactly its projection. The descended homomorphism class is the class of the crossed homomorphism, by equation (2.6) of the descent lesson. Proposition A.2 gives (A10). \(\square\)

For a separable \(G\)-algebra \(A\), define
\[
\begin{aligned}
\mu_{X,A,(r)}:KK_i^G(C_0(X),A)&\longrightarrow K_i(A\rtimes_{(r)}G),\\
\mu_{X,A,(r)}(x)&=[p_X]\widehat\otimes_{D_{X,(r)}}j_{G,(r)}(x).
\end{aligned}
\tag{A11}
\]
For graded coefficients use the scalar-cycle notation \(K_i(B)=KK_i(\mathbb C,B)\). Thus (A11) is a construction entirely in the proved KK category. The comparison with projection and unitary K-theory for trivially graded coefficients is a separate coefficient Fredholm-picture result.

**Theorem A.4.** Formula (A11) is a well-defined group homomorphism, independent of the cutoff. For an equivariant map \(f:X\to Y\), put \(f_*x=[f^*]\widehat\otimes_{C_0(X)}x\). Then
\[
\mu_{Y,A,(r)}(f_*x)=\mu_{X,A,(r)}(x).
\tag{A12}
\]
For \(\eta\in KK_j^G(A,B)\), it satisfies
\[
\mu_{X,B,(r)}(x\widehat\otimes_A\eta)
=\mu_{X,A,(r)}(x)\widehat\otimes_{A\rtimes_{(r)}G}j_{G,(r)}(\eta).
\tag{A13}
\]
The reduced map is the full map followed by the coefficient quotient:
\[
\mu_{X,A,r}(x)=\mu_{X,A}(x)\widehat\otimes_{A\rtimes G}[q_A].
\tag{A14}
\]

**Proof.** Proposition A.2 gives a cutoff-independent class. Descent respects cycle homotopy and addition by Theorem 2.2 of the descent lesson, and product by its Theorem 3.2. Associativity of the proved product therefore makes (A11) a well-defined homomorphism. For (A12), product compatibility gives

\([p_Y]j(f_*x)=[p_Y][f^*\rtimes G]j(x)=[p_X]j(x)\),

with the same calculation in the reduced completion. This uses Lemma A.3 at its middle step. For (A13), expand \(j(x\eta)=j(x)j(\eta)\) and reassociate; the cutoff factor is even, so no sign arises. Finally (3.9) of the descent lesson says \([q_{C_0(X)}]j_{G,r}(x)=j_G(x)[q_A]\). Multiply on the left by the full cutoff class, whose quotient is the reduced cutoff class, to obtain (A14). \(\square\)

If \(\mathcal E\) is a given model for the classifying space of proper actions, take the directed family of its closed, locally compact, \(G\)-compact subspaces used to define equivariant K-homology with \(G\)-compact supports. With coefficients the definition is
\[
RK_i^G(\mathcal E;A)=\underset{X\subset\mathcal E}{\operatorname{colim}}\,
KK_i^G(C_0(X),A).
\tag{A15}
\]
The structure map for \(X\subset Y\) is pullback of the source representation along restriction \(C_0(Y)\to C_0(X)\). Formula (A12) says exactly that (A11) is constant under these structure maps. It therefore induces a unique assembly homomorphism
\[
\mu_{A,r}:RK_i^G(\mathcal E;A)\longrightarrow K_i(A\rtimes_rG).
\tag{A16}
\]
This step is purely a passage to a direct limit of the proved maps. Construction of the classifying model and the independence of its choice are separate geometric inputs; none is inferred from a cutoff calculation. For an equivariant homotopy through proper maps of \(G\)-compact spaces, the corresponding source homomorphisms form a homotopy, so (A12) respects that homotopy as well.

## 3. The finite-group calculation

For finite \(G\), use Haar probability measure. The point is a classifying proper space: every subgroup has the point as a contractible fixed set, and there is exactly one equivariant map from any space to it. We may take \(X=\{*\}\), \(c=1\). In counting-measure notation its projection is
\[
p_G=\frac1{|G|}\sum_{g\in G}u_g.
\tag{A17}
\]

**Theorem A.5.** For every separable graded finite-group algebra \(A\), (A16) is the Green–Julg isomorphism
\[
KK_i^G(\mathbb C,A)\ \cong\ K_i(A\rtimes_rG).
\tag{A18}
\]

**Proof.** We identify the assembly cycle with the cycle isomorphism already proved in [*Equivariant KK-theory and the Green–Julg theorem*, Theorem 4.3](KT-KK-17.html#4-invariant-compact-operators-and-green-julg). That theorem proves all homotopy relations as well as the bijection. Its normalization makes the scalar representation unital and the operator invariant, adds a degenerate balanced regular module and applies equivariant stabilization. Thus it suffices to compare cycles on finite sums and the countable balanced amplification of
\[
\mathcal R_A=L^2(G)\otimes A,\qquad
(U_s\xi)(t)=\alpha_s(\xi(ts)).
\tag{A19}
\]
Let \(D=A\rtimes G\). Sections of its crossed module have variables \(h,t\in G\). The descended scalar group representation is
\[
(V_s\zeta)(h)(t)=\alpha_s(\zeta(s^{-1}h)(ts)).
\tag{A20}
\]
The projection (A17) acts as the average of these \(V_s\)'s. Its range is exactly their invariant submodule.

For \(f\in C(G,A)\), define
\[
\zeta_f(h)(t)=\alpha_{t^{-1}}(f(th)).
\tag{A21}
\]
It is invariant by substitution into (A20). Conversely, for invariant \(\zeta\), use \(s=t^{-1}\) in (A20) to obtain (A21) with \(f(r)=\zeta(r)(e)\). Since \(G\) is finite, these are bounded operations on finite tuples, with no point evaluation on an arbitrary \(L^2\)-function.

Using probability measure in both variables, equation (1.2) of the descent lesson gives
\[
\begin{aligned}
\langle\zeta_f,\zeta_k\rangle_D(r)
&=\int_G\int_G
 \alpha_{h^{-1}}\alpha_{t^{-1}}
      (f(th)^*k(thr))\,dt\,dh\\
&=\int_G\alpha_{s^{-1}}(f(s)^*k(sr))\,ds\\
&=(f^**k)(r).
\end{aligned}
\tag{A22}
\]
For the second equality set \(s=th\) for each \(t\); the remaining \(t\)-integral has mass one. Right convolution in the crossed module similarly gives \(\zeta_f b=\zeta_{f*b}\). Thus \(f\mapsto\zeta_f\) extends to a unitary
\[
D\ \longrightarrow\ p_G(\mathcal R_A\rtimes G).
\tag{A23}
\]
Surjectivity follows from the converse to (A21), first on finite tuples and then on their completion. Amplifying gives the unitary for the balanced standard \(D\)-module.

The invariant compact algebra on \(\mathcal R_A\) is \(D\) by Proposition 4.1 of the equivariant lesson. Its kernel for \(a\in C(G,A)\) is the integrated covariant operator
\[
(K_a\xi)(t)=\int_G\alpha_{t^{-1}}(a(s))\xi(s^{-1}t)\,ds.
\tag{A24}
\]
Substitution of (A21) gives \(K_a\zeta_f=\zeta_{a*f}\). Hence (A23) identifies the descended invariant compact operators with left multiplication by \(D\). It identifies their invariant multipliers as well: multiply by a compact-algebra approximate identity, use (A24), and pass to the strict limit on the generated module. This is precisely the multiplier extension proved in Lemma 4.2 of that lesson.

An invariant normalized cycle operator \(F\) commutes with \(p_G\). Its assembly product is therefore its restriction to the range of \(p_G\); compression preserves its compact defects. Under (A23), this is the same odd multiplier of the standard compact algebra used by the Green–Julg cycle comparison. Degenerate cycles and the balancing added in normalization map to their corresponding degenerate cycles. Thus the two homomorphisms agree on every class, and Theorem 4.3 proves that assembly is an isomorphism. Full and reduced crossed products agree for compact groups by the faithful regular-representation proof in Proposition 4.1, so the conclusion is the reduced one. A trivial right Clifford factor passes unchanged through (A19)–(A24), proving both degrees. \(\square\)

## 4. A concrete lattice cutoff and the trace implication

For \(\mathbb Z\) acting on \(\mathbb R\) by translations, let
\[
h(x)=\max(1-|x|,0),\qquad c(x)=\sqrt{h(x)}.
\tag{A25}
\]
If \(x=k+t\), \(k\in\mathbb Z\), \(0\leq t\leq1\), the only possibly nonzero translates are \(h(x-k)=1-t\) and \(h(x-k-1)=t\). Their sum is one, including endpoints. Thus (A2) holds and
\[
p(n,x)=\sqrt{h(x)h(x-n)}.
\tag{A26}
\]
It vanishes for \(|n|\geq2\), and at \(|n|=1\) has support in the overlap of adjacent intervals. Formula (A7) proves that it is a projection; its class is the concrete cutoff class, independent of the tent-shaped choice. For \(\mathbb Z^d\) acting on \(\mathbb R^d\), use \(\prod_j h(x_j)\); the orbit sum factors into \(d\) sums equal to one. This computes the cutoff projection, rather than yet asserting the lattice assembly isomorphism.

Here is the precise elementary implication of trace integrality. For a countable discrete group \(\Gamma\), the reduced regular representation defines
\[
\tau(a)=\langle\delta_e,a\delta_e\rangle
\quad(a\in C_r^*(\Gamma)).
\tag{A27}
\]
On finite group-algebra sums it is the coefficient of \(e\). In a product the contributions to that coefficient are paired by \(g\leftrightarrow g^{-1}\), so \(\tau(ab)=\tau(ba)\). Density and continuity extend this identity. Also \(\tau(a^*a)=\|a\delta_e\|^2\geq0\) and \(\tau(1)=1\). Right translations commute with the reduced algebra. If \(\tau(a^*a)=0\), then \(a\delta_e=0\) and consequently \(a\delta_g=0\) for every \(g\); hence \(a=0\). The trace is faithful.

For projections \(p\in M_n(C_r^*(\Gamma))\), put \(\tau_n(p)=\sum_j\tau(p_{jj})\). A rectangular partial isometry \(v\) satisfies \(\tau_n(vv^*)=\tau_m(v^*v)\), by expanding the matrix entries and using the trace identity. Adding a zero block does not change this value, and block sums add it. It therefore extends to a homomorphism \(\tau_*:K_0(C_r^*(\Gamma))\to\mathbb R\), using the projection definition of K-theory proved in the index-pairing lesson.

**Proposition A.6.** If \(\tau_*(K_0(C_r^*(\Gamma)))\subset\mathbb Z\), the only projections and the only idempotents in \(C_r^*(\Gamma)\) are \(0,1\). More generally, if assembly is surjective and its image has integral trace, this conclusion holds.

**Proof.** A projection \(p\) has \(0\leq\tau(p)\leq1\). Integrality gives value zero or one. Faithfulness applied to \(p^*p=p\), or to \((1-p)^*(1-p)=1-p\), gives \(p=0\) or \(p=1\).

For an idempotent \(e\), put \(H=1-(e-e^*)^2\geq1\). Expansion shows that \(H\) commutes with \(e,e^*\) and that \(He=ee^*e\). Consequently \(p=ee^*H^{-1}\) is self-adjoint and
\[
p^2=p,\qquad pe=e,\qquad ep=p.
\tag{A28}
\]
For example \(H ee^*=ee^*ee^*\) proves the first identity. Thus \(p=0\) forces \(e=0\), while \(p=1\) and \(ep=p\) force \(e=1\). The surjectivity variant follows because every K-class then belongs to the integral-trace image. \(\square\)

Theorem A.10 below proves integral trace on the entire torsion-free assembly image. Combined with this proposition, it gives the projection and idempotent consequence under surjectivity.


## 5. Covering Dirac classes and the Mishchenko index

Let \(\Gamma\) be a countable discrete group acting freely and properly by spin\(^{c}\) isometries on a connected manifold \(X\), with closed quotient \(M=X/\Gamma\). The spin\(^{c}\) structure and connection on \(X\) are the lifts of those on \(M\). A lifted finite-rank Hermitian coefficient bundle is allowed. Put \(A=C^*(\Gamma)\), or \(A=C_r^*(\Gamma)\), and denote its canonical unitaries by \(u_\gamma\). The algebra \(A\) is unital and separable. The Mishchenko bundle is
\[
\mathcal L=X\times_\Gamma A,\qquad
\gamma(x,a)=(\gamma x,u_\gamma a).
\tag{M1}
\]
Its transition maps are left multiplication, hence are right \(A\)-linear unitaries. This convention matters.

Clifford multiplication is self-adjoint, with \(c(v)^2=|v|^2\); the spinor Dirac convention is \(D=-i\sum_jc(e_j)\nabla_{e_j}\). In even dimension use its spinor grading. In odd dimension use the positive spinor representation followed by the last right \(Cl_1\) factor.

### 5.1. Smooth cutoffs and the lifted operator

**Lemma M.1.** There is a smooth compactly supported real cutoff \(c\geq0\) with
\[
\sum_{\gamma\in\Gamma}c(\gamma^{-1}x)^2=1.
\tag{M2}
\]
The lifted spinor Dirac \(D_X\), initially on smooth compactly supported sections, is self-adjoint. It has locally compact resolvents and represents an equivariant cycle with source \(C_0(X)\).

**Proof.** Freeness and properness give covering charts. Indeed, choose a compact neighbourhood of \(x\). Only finitely many of its translates can meet it, by the compact-transporter proof of Lemma A.1. For each nonidentity element in that finite set choose a smaller neighbourhood of \(x\) disjoint from its translate, using \(\gamma x\ne x\). Their finite intersection has disjoint translates. Its quotient image is a chart, and the quotient map restricts to a diffeomorphism there.

Choose finitely many relatively compact such charts whose quotient images cover \(M\), with smooth nonnegative bump functions positive on smaller charts. Euclidean bump functions and a finite partition produce them. Let \(b\) be their sum on \(X\). The sum \(h(x)=\sum_\gamma b(\gamma^{-1}x)^2\) is locally finite, smooth, positive and invariant: local finiteness follows from the compact transporter of \(\operatorname{supp}b\) with any compact neighbourhood. Then \(c=b/\sqrt h\) proves (M2). Every derivative of \(c\) is bounded, since its support is compact.

Here is a proper smooth exhaustion with bounded gradient, without assuming a compact base argument on \(X\). Let \(K=\operatorname{supp}c\), \(U=\{c>0\}\), and \(S=\{\gamma:\gamma K\cap K\ne\varnothing\}\). This is finite and symmetric. The translates of the open set \(U\) cover connected \(X\). Their intersection graph is connected; otherwise the unions over its two collections of components would partition \(X\) into disjoint nonempty open sets. Edges from \(\gamma U\) to \(\delta U\) have \(\gamma^{-1}\delta\in S\). Hence \(S\) generates \(\Gamma\). Let \(\ell\) be its word length and set
\[
r(x)=\sum_\gamma \ell(\gamma)c(\gamma^{-1}x)^2.
\tag{M3}
\]
The sum is locally finite. If \(x\in\gamma_0K\), all active indices belong to \(\gamma_0S\). Subtract \(\ell(\gamma_0)\) when differentiating, using (M2). The inequalities
\(\lvert\ell(\gamma)-\ell(\gamma_0)\rvert\leq\max_{s\in S}\ell(s)\),
the finite size of \(S\), and the common gradient bound on translates of \(c^2\) give a uniform bound on \(\lvert dr\rvert\). If \(r(x)\leq R\), one active index has word length at most \(R\); thus \(x\) belongs to a finite union of translates of \(K\). The sublevel is closed, hence compact.

We give the domain details needed below. The exact elliptic parametrix and Sobolev estimate in *Unbounded Kasparov modules and spectral triples*, Lemmas 4.2a–4.2b apply on any selected compact coordinate support: their kernels are cut off in that support and their proof is local. In particular a distributional solution of \(D_Xv\in L^2_{\mathrm{loc}}\) belongs to \(H^1_{\mathrm{loc}}\). To see the estimate explicitly, the order-minus-one local parametrix applied to \(D_Xv\), plus its smoothing error and a commutator supported in the larger chart, bounds the \(H^1\) norm on the smaller support by the local \(L^2\) norms of \(v,D_Xv\). A finite partition gives the estimate on every compact set. Smooth approximation in \(H^1\) therefore approximates compactly supported such vectors in the graph norm, since the coefficients and their first derivatives are bounded on that support.

The lifted Dirac is formally symmetric by integration by parts and compatibility of its Clifford connection. Explicitly, the extra adjoint term in an orthonormal frame is \(-i\sum_jc(\nabla_{e_j}e_j+(\operatorname{div}e_j)e_j)\). Its coefficient along \(e_k\) is zero because metric compatibility gives \(\operatorname{div}e_k=-\sum_j\langle\nabla_{e_j}e_j,e_k\rangle\). If \(D_X^*v=\pm iv\), the preceding local regularity applies. Choose \(\chi_R=\chi(r/R)\), with \(\chi=1\) on \([0,1]\), zero on \([2,\infty)\), and bounded derivative. The commutator is Clifford multiplication by \(d\chi_R\), of norm at most \(C/R\). Formal symmetry, justified by the compactly supported graph approximation, gives
\[
\|\chi_Rv\|^2
\leq \|[D_X,\chi_R]v\|\,\|\chi_Rv\|
\leq C R^{-1}\|v\|\,\|\chi_Rv\|.
\tag{M4}
\]
Since \(\chi_Rv\to v\), both deficiency spaces vanish. For clarity, this proves self-adjointness: the ranges of the closed minimal \(D_X\pm i\) are closed by
\(\|(D_X\pm i)w\|^2=\|D_Xw\|^2+\|w\|^2\);
their orthogonal complements are those deficiency spaces, so both ranges are all of \(L^2\). Smooth compactly supported sections remain a graph core by definition of that minimal closure.

For \(a\in C_c^\infty(X)\), the local estimate sends \(a(D_X\pm i)^{-1}\) into a bounded \(H^1\) set on a compact support. This inclusion in \(L^2\) is compact: on each chart high Fourier frequencies have norm bounded by \(R^{-1}\) times the \(H^1\) bound, and the low-frequency cutoff has a square-integrable kernel on the two compact supports, approximable by finite sums of product functions. A finite partition proves compactness. Approximation extends it to \(a\in C_0(X)\). Smooth compactly supported functions preserve the domain and have bounded Clifford commutators. The proved bounded-transform theorem, Theorem 2.2 of that lesson, now gives the cycle. The group preserves the lifted connection and its core, so it commutes with both resolvents and the transform. For odd dimension use the fixed right \(Cl_1\) transfer throughout. \(\square\)

### 5.2. The range of the assembly projection

Write \(\mathcal H=L^2(X,S_X)\), including any lifted finite-rank coefficient bundle. Descent identifies its coefficient module with \(\mathcal H\otimes A\). On finite sections the identification sends \(\zeta:\Gamma\to\mathcal H\) to \(\sum_h\zeta(h)\otimes u_h\); indeed,
\[
\left\langle\sum_h\zeta(h)\otimes u_h,
                  \sum_k\eta(k)\otimes u_k\right\rangle
=\sum_r\left(\sum_h\langle\zeta(h),\eta(hr)\rangle\right)u_r,
\tag{M5}
\]
which is exactly the descended inner product. The right convolution agrees as well, and these finite sections are dense. A crossed element \(a u_\gamma\) acts by
\[
(\phi(a)U_\gamma)\otimes L_{u_\gamma}.
\tag{M6}
\]
The descended transform is \(F_{D_X}\otimes1\). These statements hold for either completion by the actual descent construction in *Descent and the K-theory of crossed products*, Section 1.

The cutoff projection acts on this module as
\[
P=\sum_\gamma
 \phi\!\left(c\,(c\circ\gamma^{-1})\right)
                U_\gamma\otimes L_{u_\gamma}.
\tag{M7}
\]
Only finitely many terms are nonzero, by the transporter of \(K\) with itself. Lemma A.2 proves that \(P\) is a self-adjoint projection.

Let \(\mathcal H_{\mathcal L}=L^2(M,S_M\otimes\mathcal L)\), with its \(A\)-valued inner product given by integration over \(M\). A section lifts to an \(A\)-valued section \(\Psi\) on \(X\) satisfying
\[
\Psi(\gamma x)=(\gamma_S\otimes L_{u_\gamma})\Psi(x).
\tag{M8}
\]
For a smooth section with finite group-algebra coefficients in finitely many quotient charts define \(J\Psi=c\Psi\). Such sections are dense: finite trivializing charts and a partition reduce approximation to scalar smooth functions and to the dense group algebra in \(A\). On the compact support of \(c\), their lifted coefficients use finitely many deck transitions. Thus \(J\Psi\) belongs to the algebraic dense part of \(\mathcal H\otimes A\).

**Lemma M.2.** Multiplication by \(c\) extends to an even unitary
\[
J:\mathcal H_{\mathcal L}\longrightarrow P(\mathcal H\otimes A).
\tag{M9}
\]

**Proof.** The pointwise \(A\)-valued inner product of two lifts in (M8) is invariant, since both the spinor action and left multiplication by \(u_\gamma\) are unitary. On a quotient chart, integrate over its disjoint lifts. Equation (M2) says that the weights \(c^2\) sum to one. A finite partition on \(M\) gives
\[
\int_X c(x)^2\langle\Psi(x),\Phi(x)\rangle\,dx
 =\int_M\langle\Psi,\Phi\rangle\,dy.
\tag{M10}
\]
This proves isometry with the exact \(A\)-valued inner product, not merely after applying a trace. Inserting (M8) into (M7) gives \(PJ\Psi=J\Psi\).

For a compactly supported smooth \(Z\) with finite \(A\)-coefficients on \(X\), define
\[
\Psi_Z(x)=\sum_\gamma c(\gamma^{-1}x)
       (\gamma_S\otimes L_{u_\gamma})Z(\gamma^{-1}x).
\tag{M11}
\]
This is locally finite and smooth; on each compact quotient chart only finitely many terms contribute, by properness and the support of \(Z\). Changing \(\gamma\) to \(s\gamma\) proves (M8). Formula (M7) gives \(J\Psi_Z=PZ\). Such \(Z\)'s are dense, so their projected vectors are dense in the range of \(P\). The isometry has closed range, proving surjectivity. \(\square\)

### 5.3. Domains, product recognition and the twisted Dirac

Put \(D_0=D_X\otimes1\) on \(\mathcal H\otimes A\). It is self-adjoint regular by the tensor-resolvent proof of Lemma 0.0 in the unbounded lesson: the two resolvents are \((D_X\pm i)^{-1}\otimes1\), have dense ranges, and satisfy the inverse and adjoint identities. Its graph core consists of smooth compactly supported spinors with finite group-algebra coefficients.

The finite sum (M7) preserves that core and has bounded commutator with \(D_0\). The group terms commute with \(D_X\); the remaining commutators are Clifford multiplications by derivatives of the finitely many smooth compactly supported coefficients in (M7). Also \(P(D_0\pm i)^{-1}\) is compact: each term is a localized compact Hilbert-space resolvent tensored with left multiplication by a unitary in the unital algebra \(A\). A finite-rank Hilbert-space approximation tensored with that unitary is a finite-rank Hilbert-\(A\) operator.

**Lemma M.3.** The operator
\[
T=P D_0 P\quad\hbox{on }P(\mathcal H\otimes A)
\tag{M12}
\]
is self-adjoint regular, has compact resolvents, and represents the product of the cutoff class with the descended Dirac cycle.

**Proof.** Remove the off-diagonal blocks of \(D_0\) relative to \(P\). Their boundedness is precisely the bounded commutator just proved. The resulting block-diagonal operator \(D_{\mathrm{diag}}\) is a bounded self-adjoint perturbation of \(D_0\). At sufficiently large imaginary parameter its inverse is the convergent Neumann series built from the inverse of \(D_0\); the adjoint inverse has the opposite parameter. These inverses prove self-adjoint regularity and preserve both projection ranges. Restricting them to the first range proves that assertion for \(T\), with domain \(P\operatorname{Dom}D_0\).

The resolvent identity expresses \(P(D_{\mathrm{diag}}-z)^{-1}\) as \(P(D_0-z)^{-1}\) plus that same compact first factor times bounded operators. Hence the compressed resolvent is compact. The projected core remains a graph core, since projection is bounded for the graph norm by the bounded commutator.

The first product module is \(p(C_0(X)\rtimes_{(r)}\Gamma)\), with operator zero. Its smooth finite crossed-algebra columns, multiplied by \(p\), are dense. For such a column \(\xi\), its represented commutator with \(D_0\) is bounded by the same finite derivative calculation as above. This gives the creation-operator error between \(T\) and \(D_0\); taking adjoints gives the adjoint error. The commutator identity first holds on the core, and bounded extension gives both domain inclusions, including the adjoint inclusion via the self-adjoint maximal domain. Positivity and domain conditions relative to the first operator zero are automatic. The actual product criterion, Theorem 5.4 of the unbounded lesson, therefore identifies the bounded transform of \(T\) with \([p]\otimes j_{\Gamma,(r)}[D_X]\). \(\square\)

The flat connection on \(\mathcal L\) is differentiation in each covering trivialization; its transition maps \(u_\gamma\) are constant. The twisted Dirac \(D_{\mathcal L}\) on \(M\) is consequently the operator whose lift is \(D_X\) acting on the spinor part of (M8).

On the dense smooth sections used above, the Leibniz rule and (M7) give
\[
\begin{aligned}
PD_0J\Psi
&=c D_X\Psi
   -ic\,\mathrm{cl}\!\left(
       \sum_\gamma(c\circ\gamma^{-1})\,d(c\circ\gamma^{-1})
                     \right)\Psi\\
&=cD_X\Psi=JD_{\mathcal L}\Psi.
\end{aligned}
\tag{M13}
\]
The middle sum is half the derivative of (M2), hence zero. This identity includes the cutoff derivative term; it has not been discarded as a compact error.

The inverse in (M11) carries the projected smooth core to smooth twisted sections. Conversely the finite local-coefficient smooth sections are mapped by \(J\) to that projected core. Lemma M.3 thus identifies the closures and their domains:
\[
J^{-1}TJ=\overline{D_{\mathcal L}}.
\tag{M14}
\]
In particular the twisted Dirac is self-adjoint regular with compact resolvents, without appealing to an unproved Hilbert-module elliptic index theorem.

**Theorem M.4.** For the lifted Dirac class of the free cocompact covering,
\[
\mu_{X,(r)}([D_X])=\operatorname{Ind}_A(D_{\mathcal L}).
\tag{M15}
\]
The right side is the scalar KK class of its bounded transform, identified with \(K_{\dim M\bmod2}(A)\) by the proved scalar Fredholm pictures in *Pictures of KK*, Sections 2–3 and 9. All statements apply to full and reduced group algebras, and to a lifted finite-rank coefficient twist.

**Proof.** The definition of assembly is the product in Lemma M.3. Equations (M9) and (M14) identify its cycle with the twisted Dirac cycle. In odd dimension every unitary and projection above is even and commutes with the last right Clifford factor; the calculation therefore passes through the exact odd convention unchanged. The full-to-reduced map carries (M7), the inner products and the unitary to their reduced versions. Its effect is the coefficient change already proved for descent, so it carries the full index to the reduced index. \(\square\)




### 5.4. Removing connectedness of the covering

The covering comparison (M15) also holds for any countable principal free cocompact \(\Gamma\)-covering of a closed spin\(^{c}\) manifold, including a disconnected total space. This extension preserves the preceding connected-cover argument as its proved local input.

**Proof.** First take one connected component of the base and one component \(X_0\) of its covering. The stabilizer \(\Gamma_0\) of \(X_0\) acts freely and properly on it, and \(X_0/\Gamma_0\) is that base component: any two lifts of the same point differ by a unique deck element, which must preserve the selected component if both lifts lie there. The other components are precisely the translates indexed by \(\Gamma/\Gamma_0\). The connected-cover proof M.1 therefore proves essential self-adjointness and localized compact resolvents for its Dirac. On the entire covering the Dirac is the orthogonal direct sum of those unitarily equivalent component operators. Its self-adjoint domain consists of the vectors with square-summable component graph norms; the finite-component smooth compactly supported cores form a graph core. This follows directly by first truncating the graph-norm sum and then using the component cores. Both opposite resolvents are the bounded componentwise resolvents, so the direct sum is self-adjoint.

Every compact subset of the manifold meets finitely many components, since its open component cover has a finite subcover. A compactly supported multiplier therefore involves only finitely many of the compact localized resolvents; it gives a compact operator on the direct sum. The group action and the Dirac intertwine on components. A closed manifold has finitely many base components by the same argument, so summing over them causes no further issue. Countability follows from second countability of the covering and makes the Hilbert space separable.

The projection (M7) still has only finitely many deck terms by the compact transporter of its cutoff support, regardless of whether \(\Gamma\) itself is finitely generated. Its derivative commutator is bounded by the same finite-support estimate. Every norm, tensor-resolvent, block compression, graph-core and exact derivative-cancellation calculation (M8)--(M14) consequently applies to this self-adjoint direct sum. The quotient unitary maps onto the sections over all base components exactly as before. This proves (M15) with unchanged full/reduced and odd conventions. A finite-rank coefficient twist changes only the already controlled component Diracs. \(\square\)

## 6. Models, lattices and trace integrality

### 6.1. A proved universal comparison system and independence of the model

Here \(G\) is an arbitrary second-countable locally compact group. A proper \(G\)-space on which \(C_0\) and \(KK\) are used is locally compact, Hausdorff and second countable; proper means that \((g,x)\mapsto(gx,x)\) is proper. A universal ambient space need not itself be locally compact. We will use only its closed, locally compact, \(G\)-compact subspaces. This distinction is essential for the following construction.

Let
\[
 {\cal U}=\{u\in L^2(G,dg):u\text{ is real and nonnegative a.e.},\
                  \|u\|_2=1\},\qquad
 (\lambda_su)(g)=u(s^{-1}g).
 \tag{U1}
\]
This is a closed subspace of the unit sphere of a separable Hilbert space, with a continuous isometric action. Here are proofs of the analytic assertions being used. Haar measure is finite on compact sets; second countability gives a countable cover by relatively compact open sets, hence a countable compact exhaustion and sigma-finiteness. Regularity approximates a finite-measure measurable set from inside by a compact set and from outside by an open set. A compactly supported continuous function equal to one on the compact set and between zero and one in that open set then approximates its indicator in \(L^2\). Truncation, simple functions and the exhaustion prove density of \(C_c(G)\) in \(L^2(G)\). Taking finite unions of a countable relatively compact base, rational coefficients and this regular approximation proves separability. For a function in \(C_c(G)\), continuity of translation follows by uniform continuity on a compact neighborhood of its support and integration there. Density and isometry give strong continuity on \(L^2(G)\). These uses of compactly supported functions and regular integration are exactly NCF.1, NCF.4 and NCF.5.

For \(u,v\in C_c(G)\), the coefficient \(\langle\lambda_gu,v\rangle\) vanishes outside \((\operatorname{supp}v)(\operatorname{supp}u)^{-1}\). Cauchy--Schwarz and \(L^2\)-approximation therefore give
\[
 \langle\lambda_gu,v\rangle\longrightarrow0\quad(g\longrightarrow\infty)
 \tag{U2}
\]
for arbitrary \(u,v\in L^2(G)\). The convergence is uniform when \(u,v\) range over two fixed compact subsets: choose finite norm nets in them and bound the difference of coefficients by the two approximation errors times the bounded norms. In particular, if \(K,L\subset{\cal U}\) are compact, the transporter \(\{g:gK\cap L\ne\varnothing\}\) is closed and is contained in a compact set, since a matching pair has coefficient one. Thus the action on \({\cal U}\) is proper: the inverse image of a compact subset of \({\cal U}^2\) is closed in the product of a compact transporter and a compact second-coordinate projection. This also proves the needed local version: near a pair of unit vectors, continuity and a fixed positive coefficient threshold bound all possible transporters.

For compact \(H\subset G\), choose a nonzero nonnegative \(f\in C_c(G)\). Haar probability on \(H\) gives \(v=\int_H\lambda_h f\,dh\). Its support is compact; it is \(H\)-fixed and nonnegative, and \(\int_Gv=\int_Gf>0\), so it is nonzero. With \(u_H=v/\|v\|_2\), the formula
\[
 (u,t)\longmapsto
 \frac{(1-t)u+t u_H}{\|(1-t)u+t u_H\|_2}
 \tag{U3}
\]
contracts \({\cal U}^H\). The denominator is at least \(1/\sqrt2\), because inner products of nonnegative vectors are nonnegative. A noncompact closed subgroup cannot fix a unit vector, since its coefficient would be constantly one in (U2). In particular all stabilizers are compact.

**Lemma A.7a (cutoff without cocompactness).** Every proper \(G\)-space \(X\) in the stated category has a continuous \(b:X\to[0,\infty)\) such that
\[
 \int_G b(g^{-1}x)\,dg=1,\qquad
 \operatorname{supp}b\cap\pi^{-1}(L)\text{ is compact for every compact }
 L\subset X/G.
 \tag{U4}
\]
Consequently \(F_b(x)(g)=\sqrt{b(g^{-1}x)}\) is a continuous equivariant map \(X\to{\cal U}\).

**Proof.** First \(Y=X/G\) is Hausdorff, locally compact and second countable. Properness makes the orbit relation closed: a convergent net of related pairs is lifted into the inverse image of a compact neighborhood of its limit, where a convergent subnet supplies the limiting group element. The quotient map \(\pi\) is open. Its product with itself is also an open quotient map, so the closed orbit relation descends to a closed diagonal in \(Y^2\); this is the Hausdorff assertion. Images of relatively compact open neighborhoods have compact closures in \(Y\), and images of a countable base form a base. NCF.1 therefore supplies a locally finite partition of unity with compact supports subordinate to any prescribed open cover, after refinement by relatively compact open sets.

Choose nonnegative \(f_i\in C_c(X)\) whose positive sets \(W_i\) meet every orbit, and put
\[
 h_i(x)=\int_G f_i(g^{-1}x)\,dg,\qquad
 V_i=\pi(W_i).
\]
The function \(h_i\) is invariant, finite and continuous: on a compact neighborhood \(K\) of an argument, every contributing group element lies in the compact transporter from \(\operatorname{supp}f_i\) to \(K\). Integration thus takes place over one compact set. Positivity on \(V_i\) follows from Haar positivity on a nonempty open set. Write \(\bar h_i\) for the descended function on \(Y\), and choose a locally finite partition \(\rho_i\) with compact support contained in \(V_i\), allowing repeated indices after refinement. Define
\[
 b(x)=\sum_i
       \frac{\rho_i(\pi x)}{\bar h_i(\pi x)}\,f_i(x).
 \tag{U5}
\]
Each summand is extended by zero outside \(V_i\). This extension is continuous because \(\operatorname{supp}\rho_i\) is compact inside \(V_i\), where \(\bar h_i\) has a positive minimum. The sum is locally finite over the quotient. Its integral is \(\sum_i\rho_i(\pi x)=1\), by left invariance of Haar measure. Over a compact \(L\subset Y\), only finitely many \(\rho_i\) occur; the support of \(b\) there is contained in the finite union of their \(\operatorname{supp}f_i\). Being closed in that compact union, it is compact.

The square root in (U4) has norm one. On a compact neighborhood \(K\subset X\), only finitely many summands can contribute on the orbits through \(K\); their contributing group elements again lie in one compact transporter. Joint continuity of \(b(g^{-1}x)\) on that compact set, followed by integration, proves norm continuity of \(F_b\). Finally
\(F_b(sx)(g)=F_b(x)(s^{-1}g)\), proving equivariance. \(\square\)

Any two continuous equivariant maps \(F_0,F_1:X\to{\cal U}\) have the equivariant homotopy obtained by normalized convex interpolation, with denominator at least \(1/\sqrt2\). This assertion applies to all such maps, not only the cutoff maps.

**Lemma A.7b (the subspaces actually used by \(KK\)).** For every compact \(K\subset{\cal U}\), its saturation \(Z_K=GK\) is closed, locally compact, Hausdorff, second countable, proper and \(G\)-compact.

**Proof.** Uniform convergence in (U2) gives, for any \(v\in{\cal U}\), a compact \(C\subset G\) such that
\(|\langle\lambda_gk,v\rangle|<1/2\) for \(g\notin C,\ k\in K\).
If \(\|\lambda_gk-v\|_2<1/2\), the real inner product is
\(1-\|\lambda_gk-v\|_2^2/2>7/8\), hence \(g\in C\).
Thus \(GK\) near \(v\) is contained in the compact image \(CK\). Every point in its closure is consequently in \(CK\subset GK\); this proves closedness, without an unproved assertion about arbitrary images of closed sets. For \(v\in GK\), the closure in \(GK\) of its radius-\(1/4\) neighborhood is contained in a compact image of this kind and is compact. This proves local compactness. The remaining separation and countability properties are inherited from the separable metric space \({\cal U}\); restriction of a proper action stays proper. The quotient is the continuous image of \(K\), so it is compact. \(\square\)

For later functoriality, an equivariant map from a \(G\)-compact proper locally compact space \(X\) to any proper target \(T\) is proper, provided the compact-transporter property holds in \(T\). Indeed choose compact \(K\subset X\) with \(GK=X\), and let \(L\subset T\) be compact. A point \(gk\) mapping into \(L\) has \(g\) in the compact transporter from \(f(K)\) to \(L\). The closed preimage of \(L\) is therefore contained in a compact image of this transporter times \(K\). This proves the slight strengthening of A.3 that is needed here, including \(T={\cal U}\). For a Hausdorff compactly generated target, this proper map is closed: if \(C\subset X\) is closed and \(L\) is any compact subset of the target, then \(f(C)\cap L=f(C\cap f^{-1}L)\) is compact and thus closed in \(L\). The defining compact-test property gives closedness in the target. Its image \(S\) is also locally compact and second countable. Indeed the fiber over a point is compact; cover it by finitely many relatively compact open subsets of \(X\). The complement of the image of their closed complement is an open neighborhood in \(S\), and its closure is contained in the compact image of their finitely many compact closures. For second countability, take all finite unions \(V\) of a countable base of \(X\); the sets \(S\setminus f(X\setminus V)\) form a countable base, since the compact fiber over a point of any open set can be covered by finitely many base sets inside its inverse image. Its quotient is compact because it is the image of \(f(K)\). This proves, rather than assumes, that all comparison and homotopy images are legitimate locally compact stages. Metric spaces, including \({\cal U}\), have the compact-test property. A Hausdorff space with the weak topology of locally compact CW cell domains also has it: a compact-test closed set has closed preimage in each cell domain, since that domain is locally compact, hence compactly generated; the final cell topology then makes the set closed. Thus this formulation also permits the usual proper CW ambient models, without asserting they are themselves locally compact.

**Theorem A.7 (model independence, including cycles and cutoffs).** Define
\[
 RK^G_i({\cal U};A)
   =\varinjlim_{K\subset{\cal U}\ {\rm compact}}
       KK^G_i(C_0(Z_K),A).
 \tag{U6}
\]
The inclusions are proper and \(Z_{K_1}\cup Z_{K_2}\subset Z_{K_1\cup K_2}\), so this is a directed system. The maps in A.4 define an assembly map on (U6), independent of all cutoff choices. For any Hausdorff compactly generated universal proper ambient model \(E\), the direct limit over its closed \(G\)-compact locally compact second-countable subspaces is canonically isomorphic to (U6), and the assembly maps agree. All spaces used for \(C_0\) and \(KK\) remain in the original proper-space category; the preceding closed-image argument supplies those hypotheses for every comparison image.

Here “universal” has its usual, explicit map-and-homotopy meaning: every proper space in the category admits an equivariant map into \(E\), and any two such maps are equivariantly homotopic. It suffices to require this for \(G\)-compact spaces and their cylinders; no building theorem or unproved existence result is invoked.

**Proof.** A cutoff map embeds each \(G\)-compact stage \(X\) into the comparison system as a proper map with image in \(Z_{F_b(K)}\), where \(GK=X\). A homotopy between any two maps has image in the saturation of the compact set \(F(K\times[0,1])\). It is proper as a map from \(X\times[0,1]\), by the same transporter argument. Therefore source pullback gives the required pushforward
\(KK^G(C_0(X),A)\to KK^G(C_0(Z_{F_b(K)}),A)\); homotopy invariance says that its class is independent of the map after passage to a common stage. Restrictions to smaller stages and all choices are compatible by the same homotopy. Conversely, for each \(Z_K\), universality gives a map to \(E\); its image is a closed \(G\)-compact stage, and the same argument makes the resulting direct-limit map independent and compatible. Compositions are identities because any map from a stage to its own model is homotopic, in a larger stage, to its inclusion. For \({\cal U}\) this is the explicit convex homotopy; for \(E\) it is its defining property. These statements use only proper maps and proper homotopies between the locally compact stages, so their \(C_0\)-pullbacks exist.

A.3--A.4 show equality of assembly under every one of those maps and homotopies; A.2 proves independence of each cutoff projection. They therefore give the canonical equality of assembly on the two limits. A Kasparov homotopy or equality of cycle classes within any one stage is already respected by descent and Kasparov product, and equality arising only after a larger stage is respected by the just-proved compatibility. This proves cycle independence as well as model independence, for both full and reduced assembly and with coefficients. \(\square\)

For \(\Gamma=\mathbb Z^n\), its translation action on \(\mathbb R^n\) is a universal model in precisely this category. To prove the defining property, take (U4) for any proper \(\Gamma\)-space and set
\[
 f(x)=\sum_{m\in\mathbb Z^n}b(m^{-1}x)m\in\mathbb R^n.
 \tag{U7}
\]
The sum is locally finite: on a compact neighborhood of \(x\), the proper-over-quotient support in (U4) and the compact-transporter property allow only finitely many \(m\). Its weights sum to one, so \(f(sx)=s+f(x)\). Any two equivariant maps to this affine space have the straight-line equivariant homotopy. Translation is proper, and the standard compact cube has saturation \(\mathbb R^n\). This proves the asserted model and shows that its whole space is already a cofinal stage:
\[
 RK^\Gamma_i(E\Gamma;A)=KK^\Gamma_i(C_0(\mathbb R^n),A).
 \tag{U8}
\]
A torsion-free discrete group has no nontrivial compact stabilizers in a proper space: its stabilizers are finite by properness and discreteness, and finite subgroups of a torsion-free group are trivial. Thus for such a group the construction uses free proper spaces, as required for the covering formulation below.

**Source and scope.** Wolfgang Lück, *Survey on classifying spaces for families of subgroups*, arXiv:math/0312378v2, Definitions 1.8 and 2.1 and Theorem 2.5, gives the free-source formulation of the proper/numerable distinction and universal map-and-homotopy formulation. The entire comparison proof actually used here is (U1)--(U8), including the local compactness of the stages; no cited theorem replaces it.


### 6.2. Free quotients and assembly on all analytic cycles

This section treats a countable discrete group \(\Gamma\), a free proper \(\Gamma\)-compact space \(X\), and \(Y=X/\Gamma\). Put \(D=C_0(X)\rtimes\Gamma\). The assertions are not restricted to Dirac classes.

**Lemma A.8a (dual Green--Julg, with its proof).** For a separable \(\Gamma\)-algebra \(B\), with trivial action on the scalar coefficient,
\[
 KK_i^\Gamma(B,\mathbb C)\cong KK_i(B\rtimes\Gamma,\mathbb C).
 \tag{Q1}
\]
A cycle \((H,\phi,F,U)\) is sent to \((H,\phi\rtimes U,F)\).

**Proof.** For a nondegenerate coefficient representation, integration and the full crossed-product universal property give mutually inverse correspondences between representations of \(B\rtimes\Gamma\) and covariant pairs \((\phi,U)\). For a generator \(aU_g\), the commutator is
\([F,\phi(a)]_{\rm gr}U_g+(-1)^{|a|}\phi(a)[F,U_g]\), for homogeneous \(a\). Both terms are compact by the equivariant cycle conditions. The other defects are compact after multiplication by this generator for the same reason. Finite sums are dense; their operator-norm limits preserve the compact conditions. Conversely, the crossed-product conditions on \(aU_e\) give the ordinary cycle conditions, and the commutator on \(aU_g\), minus the already compact first term, gives the localized equivariance defect. Strong continuity has no additional requirement for a discrete group. Essential replacement, proved in the product lesson, permits nonessential initial representations; the strict multiplier representation supplies the group unitaries on the essential subspace. These operations agree under orthogonal sums, degenerate additions, locally compact changes and cycle homotopies. The same calculation on Hilbert \(C([0,1])\)-modules proves the homotopy assertion. Ordered right Clifford factors commute with all group unitaries, giving both degrees. This proves (Q1), not merely a correspondence between a selection of geometric cycles. \(\square\)

**Lemma A.8b (the free-action Morita equivalence).** Full and reduced \(D\) agree. If \(c\) is the normalized cutoff in A.1, its projection \(p\) is full, and
\[
 pDp=C(Y)p\cong C(Y).
 \tag{Q2}
\]
An explicit \(D\)-\(C(Y)\) imprimitivity module \(E\) is the completion of \(C_c(X)\), with
\[
 \begin{split}
 (\xi h)(x)&=\xi(x)h([x]),\\
 \langle\xi,\eta\rangle([x])
   &=\sum_{\gamma}\overline{\xi(\gamma^{-1}x)}\eta(\gamma^{-1}x),\\
 (f\xi)(x)&=\sum_{\gamma}f(\gamma,x)\xi(\gamma^{-1}x).
 \end{split}
 \tag{Q3}
\]

**Proof.** A free proper discrete action has evenly covered local charts. At \(x\), first take a relatively compact neighborhood. Properness bounds its possible self-transporters by a finite set. Freeness separates \(x\) from its images under the finitely many nonidentity elements; shrinking the neighborhood separates all of those images, while the other elements were already excluded. Its translates are pairwise disjoint. This proves the chart assertion locally and proves that \(X\to Y\) is a covering.

The kernel
\[
 k_{\xi,\eta}(\gamma,x)
       =\xi(x)\overline{\eta(\gamma^{-1}x)}
 \tag{Q4}
\]
has compact support and finite group support by properness. Direct summation gives
\(k_{\xi,\eta}^*=k_{\eta,\xi}\) and
\(k_{\xi,\eta}k_{\zeta,\omega}
 =k_{\xi\langle\eta,\zeta\rangle,\omega}\).
Moreover these kernels span the crossed-product core exactly. Indeed a core function has only finitely many \(\gamma\)'s and a compact \(x\)-support. Partition that support among finitely many of the free charts \(V_j\). For its term at \(\gamma\), choose \(\xi_j\) to be the partitioned coefficient and choose \(\eta_j\in C_c(\gamma^{-1}V_j)\) equal to one on \(\gamma^{-1}\operatorname{supp}\xi_j\). The kernel \(k_{\xi_j,\eta_j}\) is zero at every group element other than \(\gamma\): otherwise a nonidentity translate of \(V_j\) would meet \(V_j\). At \(\gamma\) it is exactly the partitioned coefficient. Summing proves the spanning assertion.

The orbit sum in (Q3) is positive and continuous, and locally finite in a covering chart; it vanishes only when the vector is zero. Thus it completes \(C_c(X)\) to a Hilbert \(C(Y)\)-module. Multiplication by \(a\in C_0(X)\) is bounded by \(\|a\|\), and translations are unitary; this proves that the covariant representation integrates in the full norm. Its kernels (Q4) act as the rank-one operators of (Q3).

Since \(\langle c,c\rangle=1\), \(p=k_{c,c}\), and the kernel identities give
\(k_{\xi,c}\,p\,k_{c,\eta}=k_{\xi,\eta}\).
The core-spanning assertion proves fullness of \(p\) in the full algebra. Also \(p f p=h_fp\), where
\(h_f=\langle c,fc\rangle\in C(Y)\).
Conversely every \(hp\), \(h\in C(Y)\), is in \(pDp\): invariant \(h\) is a bounded multiplier and \(p\) has compact support. In every covariant representation \(\|hp\|\leq\|h\|\); the orbit representation on \(\ell^2(\Gamma)\) gives the reverse inequality at each orbit, since \(p\) is its rank-one projection onto the unit vector \(c\). Thus the full norm of \(hp\) is exactly \(\|h\|\). Completion gives (Q2).

The map \(\xi\mapsto k_{\xi,c}\) identifies (Q3) isometrically with \(Dp\), since its inner product is \(\langle\xi,\eta\rangle p\). The spanning assertion and the kernel identities give dense range. The full-corner construction now proves imprimitivity directly: rank-one operators on \(Dp\) are left multiplication by \(DpD\), dense in \(D\), and a multiplier annihilating \(Dp\) annihilates that dense ideal and is zero. The dual module \(pD\), with the evaluation maps \(d_1p\otimes pd_2\mapsto d_1pd_2\), gives both inverse KK classes by the actual interior-tensor identities.

Finally the regular quotient is faithful on \(pDp=C(Y)\), by the same orbit representations. If its kernel is \(I\), then \(pIp=0\). For \(a\in I\), \(pa^*ap=0\) gives \(ap=0\); applying this to \(ad\in I\) for every \(d\in D\) gives \(aDp=0\). Fullness implies \(aD=0\), hence \(a=0\). This proves full equals reduced here, without a general amenability theorem. \(\square\)

Combining (Q1)--(Q3) gives an actual isomorphism
\[
 \Theta_X:KK_i^\Gamma(C_0(X),\mathbb C)
              \longrightarrow KK_i(C(Y),\mathbb C),\qquad
 \Theta_X(x)=[E^*]\otimes_D(\phi\rtimes U,F).
 \tag{Q5}
\]
For an invariant covering Dirac, compression by \(p\), with scalar coefficients, is the quotient Dirac: (M9)--(M14), with \(A=\mathbb C\), give its full source action and closure. Consequently \(\Theta_X[D_X]=[D_Y]\), with precisely the odd and grading conventions already fixed there.

Let \(A=C^*(\Gamma)\), or \(C_r^*(\Gamma)\), and let
\(\mathcal L=X\times_\Gamma A\) use the left-unitary action \(u_\gamma\) and the usual right \(A\)-module structure. The locally constant transitions and a finite chart partition of the compact \(Y\) make its section module finitely generated projective over \(C(Y)\otimes A\): the local components weighted by square roots of a partition embed it isometrically in a finite free module, and the adjoint patches them back. Denote its scalar KK class by \([\mathcal L]\).

In this subsection write \(\mu_X^A\) for **scalar-coefficient** assembly with target completion \(A=C^*(\Gamma)\) or \(C_r^*(\Gamma)\), and \(j_\Gamma^A\) for that scalar cycle's full or reduced descent. Thus \(\mu_X^{C^*(\Gamma)}=\mu_{X,\mathbb C}\) and \(\mu_X^{C_r^*(\Gamma)}=\mu_{X,\mathbb C,r}\) in the notation of A.4. The superscript selects the target completion; it does not change the input coefficient to \(A\).

**Theorem A.8 (Mishchenko comparison for every analytic cycle).** For every \(x\) in (Q5), writing \(y=\Theta_X(x)\),
\[
 \mu_X^A(x)
    =[\mathcal L]\otimes_{C(Y)\otimes A}(y\boxtimes1_A).
 \tag{Q6}
\]
This includes both degrees, arbitrary analytic cycles, and homotopies.

**Proof.** The covariant pair \((a\mapsto a\otimes1,\ U_\gamma\mapsto
U_\gamma\otimes u_\gamma)\) defines a homomorphism
\[
 \delta:D\longrightarrow D\otimes A,\qquad
 \delta(aU_\gamma)=aU_\gamma\otimes u_\gamma .
 \tag{Q7}
\]
Existence in the minimal tensor product follows directly from the full universal property into its multiplier algebra; core terms are in \(D\otimes A\), and their dense closure gives the displayed range.

On the crossed Hilbert module of a scalar cycle, the map from compactly supported vectors to \(H\otimes A\) is
\(\zeta\mapsto\sum_\gamma\zeta(\gamma)\otimes u_\gamma\).
The descent inner product becomes
\(\sum_{\gamma,\eta}\langle\zeta(\gamma),\zeta'(\eta)\rangle
u_\gamma^*u_\eta\), exactly the tensor inner product. Its range is dense; it intertwines right multiplication, the descended operator \(F\otimes1\), and the left generator with \(\phi(a)U_\gamma\otimes u_\gamma\). Thus
\[
 j_\Gamma^A(x)=[\delta]\otimes_{D\otimes A}
                         ((\phi\rtimes U,F)\boxtimes1_A).
 \tag{Q8}
\]
This is also a direct cycle proof of the comparison, rather than an imported coaction formula.

Transport the projection \(\delta(p)\) through \(E\boxtimes A\). On the module of functions in (Q3) with \(A\)-coefficients, it is
\[
 (PZ)(x)=c(x)\sum_\gamma c(\gamma^{-1}x)
                   u_\gamma Z(\gamma^{-1}x).
 \tag{Q9}
\]
A section of \(\mathcal L\) lifts to
\(\Psi(\gamma x)=u_\gamma\Psi(x)\). The map \(\Psi\mapsto c\Psi\) lands in the range of \(P\), and its pointwise orbit inner product is
\(\sum_\gamma c(\gamma^{-1}x)^2\Psi(x)^*\Phi(x)=\Psi(x)^*\Phi(x)\).
Its inverse on the range is the sum in (Q9) without the outer \(c(x)\). These sums are locally finite, and the range vectors have support in the compact support of \(c\); they give inverse adjointable unitaries, commuting with \(C(Y)\). Hence
\[
 [\delta(p)]\otimes_{D\otimes A}[E\boxtimes A]=[\mathcal L].
 \tag{Q10}
\]
The Morita inverse identities give
\((\phi\rtimes U,F)=[E]\otimes_{C(Y)}y\). Substitute this into (Q8), multiply by \([p]\), and use (Q10) and associativity. The result is (Q6). All operators and maps commute with the last right Clifford factor, so the statement holds in both degrees. They also act on interval-coefficient modules, proving the assertion about every analytic homotopy. \(\square\)

When \(Y\) is a closed spin\(^{c}\) manifold and \(a\in K_j(C(Y))\), let
\(a\cap[D_Y]\in KK_{j+\dim Y}(C(Y),\mathbb C)\) mean the usual action through diagonal multiplication. Formula (Q6), including the \(C(Y)\)-linear unitary in (Q10), proves
\[
 \mu_X^A\bigl(\Theta_X^{-1}(a\cap[D_Y])\bigr)
                =a\otimes_{C(Y)}[D_{\mathcal L}].
 \tag{Q11}
\]
For finite-rank bundle representatives this is the tensor connection Dirac and the full-source version of (M13). For odd representatives it follows from the same diagonal action, (Q6), and associativity; it is not an assertion that all odd representatives are bundles. Product recognition for the Dirac action is the actual Theorem 5.4 of Lesson 11; all the module and closure assertions are those of M.3. Thus (Q11) retains the scalar and odd source actions needed for the torus calculation.

**Source.** The freely available primary author paper by Markus Land, arXiv:1306.5657v2, Section 4, Propositions 4.1--4.5 give the free-source comparison. Its quoted external proof of (Q1) is not used as a provider: that result is proved in A.8a. Likewise (Q2)--(Q11) supply the full local corner, module and coaction arguments actually used here.


### 6.3. Lattice assembly and its ordered Connes–Thom comparison

Write \(T^n=(\mathbb R/\mathbb Z)^n\), order the positive coordinates \(x_1,\ldots,x_n\), and use periodic spinors. Let \(D_n\) be the ordinary positive-volume spin\(^{c}\) Dirac of the flat torus. For \(n=1\), \(D_1=-i\,d/dx\). The full-source covering cycle of M.3 is
\(d_n=[D_{\mathcal L_n}]\in KK^n(C(T^n),C^*(\mathbb Z^n))\).
All integer degrees below use the ordered right-Clifford convention of the preceding lessons.

**Lemma A.9a (the torus duality actually needed here).** The map
\[
 \operatorname{PD}_n:K_j(C(T^n))\longrightarrow
 KK_{j+n}(C(T^n),\mathbb C),\qquad
 a\longmapsto a\cap[D_n],
 \tag{T1}
\]
is an isomorphism for every \(n\geq0\).

**Proof.** This is proved for the torus, without assuming the general manifold duality statement. Evaluation at \(1\) on the circle has the homomorphic section of constants and kernel \(C_0(S^1\setminus\{1\})\cong C_0(\mathbb R)\). The actual semisplit excision and both-variable exact sequences, [Lesson 14, Theorems 4.1–4.2](KT-KK-14.html#4-excision-and-the-six-term-sequences), apply to its tensor product with every \(C(T^r)\): pointwise evaluation and the same constants section give the split extension explicitly. Its extension cycle is zero, since a homomorphic section makes its Stinespring projection commute and its commutator operator zero; equivalently its direct split extension has a degenerate boundary cycle. Thus both K-theory and contravariant scalar KK split into the base summand and its suspended summand. The fixed Bott inverse cycles give the suspension identifications. Lesson 07, Theorems 2.2 and 3.2, gives \(KK_0(\mathbb C,\mathbb C)=\mathbb Z\) by rank/index and \(KK_1(\mathbb C,\mathbb C)=0\); finite-dimensional unitary diagonalization also proves the latter scalar K-group is zero.

For the circle let \(z(x)=e^{2\pi ix}\), \(e\) be evaluation at \(1\), and \(d=[D_1]\). The reduced class of \(z\) is a generator of \(K_1(C_0(S^1\setminus\{1\}))\): in the increasing coordinate \(\xi=-\cot(\pi x)\) it is exactly the positive Cayley generator \((\xi-i)/(\xi+i)\) of the scalar Bott proof in Lesson 18, Section 5. The positive circle Dirac compresses \(z\) to the unilateral shift. Its kernel is zero and its cokernel has dimension one, so
\(\langle[z],d\rangle=-1\), the actual calculation (CI.39) of Lesson 15. This pairing with the reduced generator proves that \(d\) generates the odd suspended KK summand: composing restriction with the fixed Bott inverse identifies that summand with \(\mathbb Z\), and this pairing is exactly its integer coordinate. The even group is generated by \(e\). Consequently
\[
 1\cap d=d,\qquad [z]\cap d=-e.
 \tag{T2}
\]
For the second identity both sides lie in the even group \(\mathbb Z e\), and pairing with the scalar unit computes their coefficient as \(-1\).

Iterate the split extension. Naturality of restriction and the fixed suspension isomorphisms shows inductively that exterior products of \(1,[z]\) form an integral basis of \(K_*(C(T^n))\), and exterior products of \(e,d\) form an integral basis of its scalar KK groups. Indeed restriction to the new suspended ideal carries \([z]\boxtimes b\), or \(d\boxtimes b\), to the suspension of \(b\), up to the fixed invertible Bott sign; the constant/evaluation factors give the other split summand. This proves surjectivity and independence of these products at each step, not a Künneth assumption.

Set \(\epsilon_n=(-1)^{n(n-1)/2}\). The operator and grading calculation of [Lesson 13, Proposition 7.2](KT-KK-13.html#7-pullback-and-direct-sums), applies to the ordered derivatives as follows. Their squares add on the Fourier core, so the sum is self-adjoint on the domain weighted by \(1+\sum k_j^2\), has compact resolvent, and its domain is contained in each derivative domain. Smooth finite Fourier creations have bounded derivative errors; the anticommutation gives the adjoint errors and first-factor positivity \(2D_{\rm first}^2\geq0\). The unbounded product criterion of Lesson 11, Theorem 5.4, therefore identifies that sum with the exterior product. In two odd factors the product matrices are \(\sigma_1,-\sigma_2\), whereas the ordinary direct sum uses \(\sigma_1,\sigma_2\); conjugation by \(\sigma_1\) reverses the grading and changes between them. In mixed parity the ordinary graded sum agrees. Iteration gives, with the integer rank retained,
\[
 [D_n]=\epsilon_n\,d\boxtimes_R\cdots\boxtimes_R d.
 \tag{T3}
\]
The same calculation works for the flat \(A\)-module twists, with compactness and domains supplied by M.3.

For a subset \(S\subset\{1,\ldots,n\}\), let \(a_S\) be the exterior product with \(z\) in \(S\) and \(1\) elsewhere, and let \(b_T\) have \(d\) in \(T\) and \(e\) elsewhere. Move each odd \(d\) past the later odd \(z\)'s using the proved graded exterior interchange law, then use (T2). The result is
\[
 \operatorname{PD}_n(a_S)
       =\epsilon_n(-1)^{\sum_{s\in S}s}\,b_{S^c}.
 \tag{T4}
\]
This is a signed permutation of integral bases, proving (T1) in both degrees. For \(n=0\) it is the identity. \(\square\)

We next identify \(d_n\) with the invertible Thom correspondence itself. The sign and the target coordinate convention are part of this identification. On \(B=C(\mathbb R/\mathbb Z)\) use translation
\(\alpha_t f(x)=f(x-t)\).
The actual Green theorem, [KT-CP Lesson 07, Lemmas 7.1–7.2, Proposition 7.3 and Theorem 7.4](../KT-CP/KT-CP-07.html#completion-in-the-full-crossed-product-norms), proves positivity, full norm completion and imprimitivity; its transported formula (7.38), for \(G=\mathbb R,H=\mathbb Z,A=\mathbb C\), gives the module \(E_+\) with
\[
 (\xi u_m)(r)=\xi(r-m),\qquad
 \langle\xi,\eta\rangle_+(m)=
       \int_{\mathbb R}\overline{\xi(r)}\eta(r+m)\,dr.
 \tag{T5}
\]
Left functions multiply and left group elements translate by \(r\mapsto r-t\). Its source is \(B\rtimes_\alpha\mathbb R\).

For the Mishchenko convention (M8), use the equally invertible **holonomy-compatible** Green module \(E_-\), obtained by the target automorphism
\(\iota(u_m)=u_{-m}\). Explicitly
\[
 (\xi\cdot u_m)(r)=\xi(r+m),\qquad
 \langle\xi,\eta\rangle_-(m)
       =\int_{\mathbb R}\overline{\xi(r)}\eta(r-m)\,dr.
 \tag{T6}
\]
The right action is the old action by \(\iota(u_m)\) and the inner product is \(\iota^{-1}\) of the old one; hence positivity, completion and imprimitivity follow by an isometric change of coefficient algebra, with inverse \(\iota\). This proves the change rather than ignoring a holonomy inversion.

The map
\[
 (\mathcal P\xi)(x)=\sum_{m\in\mathbb Z}\xi(x+m)u_{-m}
 \tag{T7}
\]
extends to a unitary from \(E_-\) onto the \(L^2\) section module of \(\mathcal L_1\). The sum is locally finite on its initial compactly supported domain, and
\((\mathcal P\xi)(x+1)=u_1(\mathcal P\xi)(x)\).
It intertwines the right action in (T6), as follows by reindexing \(m\). Expanding the inner product and integrating over \(0\leq x\leq1\) gives the coefficient at \(u_k\) equal to
\(\int_{\mathbb R}\overline{\xi(r)}\eta(r-k)\,dr\), exactly (T6). Finite local trivializations and finite group-algebra coefficients approximate every section in norm; their scalar compactly supported lifts times right coefficients belong to the range, proving density and hence surjectivity. The unitary retains the left action of \(f(x)\), and left translation becomes \(\Psi(x)\mapsto\Psi(x-t)\).

In Lesson 18 the canonical group multiplier is \(u_t=e^{itP_\alpha}\). Since \(D_{\mathcal L_1}=-i\,d/dx\), the last translation is \(e^{-itD_{\mathcal L_1}}\); therefore \(P_\alpha=-D_{\mathcal L_1}\) under (T7). Choose the odd bounded transform \(h(s)=s/\sqrt{1+s^2}\) for the Thom cycle. The full-source cycle identification is
\[
 t_\alpha\otimes_{B\rtimes\mathbb R}[E_-]
       =-[D_{\mathcal L_1}]\quad\hbox{in }KK^1(B,C^*(\mathbb Z)).
 \tag{T8}
\]
The closures and graph cores agree under (T7), first on smooth compactly supported lifts and then by the self-adjoint regular closures proved in M.3. Negative \(h(D)\) represents the additive inverse in the exact odd picture of Lesson 07. Thus (T8) includes the operator, source action and odd sign.

For \(n\) coordinates, independent applications of the same proved Green theorem give the exterior module \(E_-^{(n)}\). The tensor maps on compactly supported product functions preserve the iterated inner products by Fubini and have dense range by compact-support partitions. They identify the iterated crossed product with \(C(T^n)\rtimes\mathbb R^n\), and \(E_-^{(n)}\) is its imprimitivity module to \(C^*(\mathbb Z^n)\), with the target automorphism \(u_m\mapsto u_{-m}\) in every coordinate. These iterated covariant integrated maps are inverse on generators, so no unproved tensor/crossed-product identification is required. The multidimensional version of (T7) is the same periodization sum over \(m\in\mathbb Z^n\).

Let \(t_{\downarrow}^{(n)}\) denote the iterated KK Thom element crossing in the order \(e_n,e_{n-1},\ldots,e_1\), the precise ordered convention of [KT-CP Lesson 11](../KT-CP/KT-CP-11.html#iteration-in-ordered-coordinates). Inactive-factor naturality, proved in Lesson 18, Proposition 4.2, and the graded exterior flip show that
\(t_{\downarrow}^{(n)}=\epsilon_n(t_{\alpha_1}\boxtimes_R\cdots\boxtimes_Rt_{\alpha_n})\)
under the just-described product-coordinate identification. Reversing \(n\) odd factors makes \(n(n-1)/2\) odd transpositions. Equations (T3) and (T8), including their identical matrix calculation for the flat twists, now give
\[
 d_n=(-1)^n\,t_{\downarrow}^{(n)}
           \otimes_{C(T^n)\rtimes\mathbb R^n}[E_-^{(n)}].
 \tag{T9}
\]
Both \(\epsilon_n\)'s cancel. The target inversion built into \(E_-^{(n)}\) is indispensable; (T9) with the usual \(E_+\) and unchanged target coordinates would be a different formula.

**Theorem A.9 (lattice assembly).** For every \(n\geq0\), full and reduced assembly for \(\mathbb Z^n\) are isomorphisms in both degrees. More precisely, for \(a\in K_j(C(T^n))\),
\[
 \mu_{j+n}\!\left(\Theta_{\mathbb R^n}^{-1}
                       (\operatorname{PD}_n(a))\right)
     =(-1)^n\,{\mathcal G}_{-,*}\,
                         \Gamma_{\alpha,\downarrow}^{(n),j}(a).
 \tag{T10}
\]
Here \(\Gamma\) is the actual KK Connes--Thom map of Lesson 18 and
\({\mathcal G}_{-,*}\) is the isomorphism induced by the specified holonomy-compatible Green module.

**Proof.** The proper universal model and its cofinal whole-space stage are (U7)--(U8). Formula (Q5) identifies its entire source with scalar K-homology of \(T^n\). Lemma A.9a identifies that entire group with \(K_{*-n}(C(T^n))\). For every one of those classes (Q11), followed by the full-source correspondence equality (T9), proves (T10). The KK Thom element is invertible by the actual Fack--Skandalis proof of Lesson 18, Theorem 6.1; its ordered iteration is invertible. Green imprimitivity and multiplication by \((-1)^n\) are also invertible. Therefore the assembly map itself is an isomorphism.

For completeness, the full and reduced group algebras of \(\mathbb Z^n\) agree with \(C(T^n)\). The full universal algebra of \(n\) commuting unitaries is \(C(T^n)\): Laurent polynomials are uniformly dense, by successive one-variable Fourier convolution (or the compact commutative approximation theorem), and evaluation at each character supplies the exact supremum norm. Fourier series identify \(\ell^2(\mathbb Z^n)\) with \(L^2(T^n)\); the regular unitaries become multiplication by the coordinate functions. This representation is faithful because Haar measure has full support and a nonzero continuous function has nonzero norm as a multiplication operator. Thus the regular quotient is injective. Full-to-reduced compatibility in A.4 finishes the reduced assertion with the same coordinates. \(\square\)

To translate (T10) into the positive-in-both-parities convention \(\Phi\) of [KT-CP Lesson 11](../KT-CP/KT-CP-11.html#iteration-in-ordered-coordinates), recall the actual comparison proved in Lesson 18, Proposition 6.2:
\(\Gamma_\alpha^j=(-1)^j\Phi_\alpha^j\).
During \(n\) steps the input parities are \(j,j+1,\ldots,j+n-1\), so
\[
 \Gamma_{\alpha,\downarrow}^{(n),j}
     =(-1)^{nj+n(n-1)/2}\Phi_{\alpha,\downarrow}^{(n),j},
 \qquad
 \mu(\Theta^{-1}\operatorname{PD}_n(a))
     =(-1)^{n+nj+n(n-1)/2}
                  {\mathcal G}_{-,*}\Phi_{\alpha,\downarrow}^{(n),j}(a).
 \tag{T11}
\]
This retains integer rank, rather than dropping \(\epsilon_n\) after reduction modulo two.

**The assigned two-Thom exercise.** For \(n=2\), first cross the \(x_2\)-translation and then the \(x_1\)-translation. Each is an isomorphism, their product has degree two, and (T11) says in both parities
\[
 \mu_i\bigl(\Theta^{-1}\operatorname{PD}_2(a)\bigr)
       =-{\mathcal G}_{-,*}
                 \Phi_{\alpha_1}^{\,j+1}\Phi_{\alpha_2}^{\,j}(a),
 \qquad i=j\pmod2.
 \tag{T12}
\]
The quotient identification and the signed-permutation duality (T4) are isomorphisms; hence (T12) proves the required \(\mathbb Z^2\) assembly isomorphism by two actual Connes--Thom maps. Its cutoff projection is the product tent cutoff of A.6. The physical torus Dirac has matrix
\(-i(\sigma_1\partial_{x_1}+\sigma_2\partial_{x_2})\) and grading \(\sigma_3\), whereas the ordered two-circle product has the minus before \(\sigma_2\). Equations (T3), (T8) and the holonomy inversion (T6) explain every sign in (T12).


### 6.4. Integral trace on the entire torsion-free assembly image

This proof covers all analytic cycles, without assuming their generation by manifolds or a general Poincaré duality theorem. Its inputs are A.7--A.8, the actual scalar pictures, Bott inverse and semisplit excision, and the finite-complex arguments proved next. A tracial Chern character is used only on finite complexes, not on arbitrary compact Hausdorff spaces.

**Lemma A.10a (finite-complex reduction).** Every free proper \(\Gamma\)-compact space \(X\), for countable discrete \(\Gamma\), admits an equivariant map to a free proper \(\Gamma\)-compact locally finite simplicial space \(Z\) whose quotient is a finite polyhedron. The map of quotient spaces pulls the flat Mishchenko bundle on \(Z/\Gamma\) back to that on \(X/\Gamma\).

**Proof.** Use the free charts proved in A.8b. Compactness of \(X/\Gamma\) permits finitely many nonnegative \(f_i\in C_c(X)\), supported in such charts, whose positive translates cover \(X\). Put
\[
 h(x)=\sum_{i,\gamma}f_i(\gamma^{-1}x)^2,\qquad
 t_{\gamma,i}(x)=f_i(\gamma^{-1}x)^2/h(x).
 \tag{R1}
\]
The denominator is positive, invariant and continuous; properness makes the sums locally finite. For each \(i\), at most one \(t_{\gamma,i}\) is nonzero, since the translated chart supports are disjoint. These barycentric coordinates define a continuous equivariant map into the join of finitely many copies of the discrete set \(\Gamma\), with vertex tags \(i\). Continuity holds in the simplicial topology: near each \(x\) only finitely many \(\gamma\)'s can occur, by the compact-transporter argument, so the map locally takes values in a finite subcomplex.

Only finitely many orbits of simplices occur. If both \((\gamma,i)\) and \((\eta,j)\) occur, then
\(\gamma^{-1}\eta\operatorname{supp}f_j\) meets \(\operatorname{supp}f_i\); there are finitely many such elements. After translating the first occurring vertex to \((e,i)\), all the other labels belong to these fixed finite lists. Take all those simplices and their faces, and all their translates, to form \(Z\). A stabilizer of a simplex fixes its uniquely tagged vertices, so it is trivial. Every vertex belongs to finitely many simplices: there are finitely many orbit representatives, and translating a specified vertex of one representative to the given vertex determines the translating element uniquely. Thus \(Z\) is locally finite and locally compact. A compact subset meets finitely many closed simplices, by a finite cover of its finite-star neighborhoods. Transporters of two such compact subsets are finite, because matching two finite sets of vertices determines only finitely many translations. Hence the action is proper.

The quotient has finitely many cells, and no cell closure identifies two of its own faces: the vertex tags in a simplex are all distinct, and any equality of a face with its translate fixes one vertex and hence has translating element \(e\). Barycentric subdivision, with vertices the actual cells and simplices their inclusion chains, consequently triangulates this finite quotient (distinct cells give distinct new vertices). It is a finite polyhedron \(P=Z/\Gamma\). The same subdivision upstairs retains a proper covering \(Z\to P\). The constructed map \(f:X\to Z\) is proper by A.3; on each orbit it is a bijection onto the orbit of its image. Therefore the map
\((x,a)\mapsto(f(x),a)\) gives the asserted isometric identification of the pulled-back principal bundle and its associated \(A\)-module bundle. This also follows directly in the free local charts. \(\square\)

Here are the finite-complex algebra and character facts used in the trace argument.

**Lemma A.10b (rational external-product decomposition, proved by cells).** For a finite CW complex \(P\) and any unital C*-algebra \(A\), external product gives an isomorphism
\[
 \left(K_0(C(P))\otimes K_0(A)\ \oplus\
       K_1(C(P))\otimes K_1(A)\right)\otimes\mathbb Q
          \ \xrightarrow{\ \cong\ }\
                    K_0(C(P)\otimes A)\otimes\mathbb Q ,
 \tag{R2}
\]
and the corresponding odd decomposition. Scalar K-groups of \(P\) are finitely generated.

**Proof.** For a closed subcomplex \(F\subset P\), restriction \(C(P)\to C(F)\) has a completely positive contractive linear section. One explicit construction, for a compatible compact metric, is this. On \(P\setminus F\), choose a locally finite partition on balls with centers \(x_i\) and radius smaller than \(\operatorname{dist}(x_i,F)/3\). Choose \(a_i\in F\) with distance less than \(2\operatorname{dist}(x_i,F)\). Set \(\sigma f(x)=\sum_i\rho_i(x)f(a_i)\) off \(F\), and \(f(x)\) on \(F\). For a point in one of those balls, \(\operatorname{dist}(x,a_i)\leq(7/2)\operatorname{dist}(x,F)\); uniform continuity of \(f\) proves continuity at \(F\). Convex sums prove the norm bound, unitality and positivity of every matrix amplification, hence complete positivity. The case \(F=\varnothing\) is immediate. NCF.1 supplies the required partition.

Tensoring this extension with \(A\) preserves its kernel. Indeed \(\sigma\otimes1_A\) is completely positive contractive, and
\((1-\sigma q)\otimes1_A\) is bounded and takes finite sums into
\(C_0(P\setminus F)\otimes A\). On the kernel of \(q\otimes1_A\) it is the identity; approximating by finite sums proves that this kernel is exactly the stated ideal. The tensor extension is therefore semisplit. Its boundary is the exterior tensor of the scalar boundary with \(1_A\): tensor the actual Stinespring module and commutator cycle of [Lesson 14, Section 3](KT-KK-14.html#3-semisplit-extensions-and-their-classes), to see this directly. Thus external products commute with the two exact sequences of [Lesson 14, Theorem 4.2](KT-KK-14.html#4-excision-and-the-six-term-sequences), with precisely its graded interchange signs.

Apply those sequences to successive skeleta of \(P\). Each relative ideal is a finite direct sum of \(C_0(\mathbb R^r)\). On such an ideal, external product is an isomorphism by the fixed Bott inverse cycles, with their coefficient tensor extensions, and scalar K-theory is \(\mathbb Z\) in parity \(r\) and zero in the other parity. Tensor the scalar exact sequence with the graded vector space \(K_*(A)\otimes\mathbb Q\); this is exact because it is a vector space over a field. Tensoring the coefficient sequence with \(\mathbb Q\) is also exact. The diagrams commute by the boundary calculation just given. Induction and the explicit five-term exact-sequence chase prove an isomorphism on each skeleton: for surjectivity, lift the boundary image using the outer isomorphisms, subtract that lift, and lift the remaining kernel; for injectivity, its image in the next term is zero by that term's injection, so lift from the preceding term, correct the lift by the term before it, and use its isomorphism to obtain zero. This is the standard five-lemma argument on a five-term segment, with its outside maps invertible. It proves both parities in (R2). The same skeletal exact sequences, with finite free relative groups, prove finite generation of scalar K-groups. No general Künneth or UCT theorem is a premise. \(\square\)

**Lemma A.10c (tracial character on a finite polyhedron).** Let \(P\) be a finite polyhedron and \(\tau:A\to\mathbb C\) a continuous positive trace, with \(\tau(1)=1\). There is a natural real even character
\(\operatorname{ch}_\tau:K_0(C(P)\otimes A)\to H^{\rm even}(P;\mathbb R)\).
For a scalar bundle \(E\) and a projective \(A\)-module \(V\),
\[
 \operatorname{ch}_\tau(E\boxtimes V)
       =\operatorname{ch}(E)\tau_*[V].
 \tag{R3}
\]
It vanishes on every odd-by-odd external product in (R2). The ordinary character
\[
 \operatorname{ch}:K_0(C(P))\otimes\mathbb R
                 \longrightarrow H^{\rm even}(P;\mathbb R)
 \tag{R4}
\]
is an isomorphism. A flat bundle with fiber \(A\) has character \(1\).

**Proof: forms, including their cohomology.** Use differential forms smooth on each closed simplex, extending smoothly a little beyond it, with compatible restrictions on its faces; refinements do not change their cohomology. The open stars of vertices form a finite cover. An intersection of stars is nonempty exactly when those vertices span a face, and it contracts by the affine homotopy to the barycenter of that face. On each containing simplex the ordinary homotopy formula is
\[
 H\omega=\int_0^1\iota_{\partial_t}h^*\omega\,dt,\qquad
                   dH+Hd=h_1^*-h_0^* .
 \tag{R5}
\]
These identities agree on faces, proving the Poincaré lemma on every intersection. A piecewise smooth partition subordinate to the stars is obtained by applying a smooth bump, zero for \(t\leq\epsilon\), to their barycentric coordinates and normalizing the sum, where \(0<\epsilon<1/(\dim P+1)\). Supports are inside the stars. It contracts the augmented horizontal rows of the Čech-form double complex: \(s(\omega)_{i_0\ldots i_{r-1}}=\sum_j\rho_j\omega_{j i_0\ldots i_{r-1}}\), with \(\delta s+s\delta=1\). The vertical Poincaré lemma and this row contraction identify form cohomology with the simplicial cohomology of the nerve, which is the chosen triangulation of \(P\).

For completeness this is its singular cohomology as well, by the actual subdivision and prism proof of CF.0: use the subcomplex of singular chains lying in one of the stars; subdivision makes its inclusion a chain homotopy equivalence. The augmented Čech resolution of those chains is exact, since for each small simplex the set of containing cover indices is a nonempty simplex, contracted by adding one chosen index. Its intersections have only degree-zero cohomology by the same affine contractions. Thus its cohomology is the same nerve cohomology. This proves the precise forms-to-singular comparison used here, only for finite polyhedra and their finite mapping cones.

**Proof: the character and relative construction.** Every class is a difference of finite matrix projections by the actual scalar picture, Lesson 07, Theorem 2.2. A continuous projection can be made piecewise smooth without changing its class. Approximate its finitely many matrix entries uniformly by finite sums of piecewise polynomial scalar functions times elements of \(A\); barycentric partitions on a sufficiently fine finite subdivision provide the approximation. Symmetrize, and retract by the spectral cut around \(1\), whose fixed gap makes this a piecewise smooth projection. The close-projection polar intertwiner identifies its module with the original one. The same construction on the finite triangulated prism \(P\times[0,1]\) proves invariance under continuous homotopies. For naturality under a continuous map between finite polyhedra, a sufficiently fine source subdivision has the image of each closed vertex star inside a target open star, by the Lebesgue-number argument on the finite target star cover. Assign such a target vertex to each source vertex. For each source simplex the assigned vertices span a target simplex, since their stars have a common image point; affine interpolation gives a piecewise linear map. The straight carrier homotopy within those target simplices joins it to the original map. Pullback of forms is natural for the piecewise linear map and the projection-path argument handles the homotopy, proving the needed continuous-map naturality. The fiber module of a projection is locally trivial as a projective \(A\)-module: close projections are intertwined by the same explicit polar unitary. This supplies the bundle interpretation without an assumed generalized bundle theorem.

For a piecewise smooth connection \(\nabla\), with curvature \(R\), define
\[
 \operatorname{ch}_\tau(\nabla)
       =\sum_{m\geq0}\frac{1}{(-2\pi i)^m m!}
                          \operatorname{Tr}_\tau(R^m).
 \tag{R6}
\]
The sum terminates by dimension; degree zero is the trace of the fiber projection. Here \(\operatorname{Tr}_\tau\) means the ordinary matrix trace followed by \(\tau\), restricted to the projection corner. Connections exist by the projected connection \(p\,d\) and partitions. In a trivialization \(R=d\omega+\omega^2\), direct expansion gives
\(dR+\omega R-R\omega=0\).
The graded trace of a commutator is zero, so (R6) is closed. For a path of connections,
\[
 \partial_t\operatorname{Tr}_\tau(R_t^m)
       =m\,d\operatorname{Tr}_\tau(\dot\nabla_t R_t^{m-1})
 \tag{R7}
\]
by the same expansion, cyclicity and the just-proved curvature identity. Thus changing connection changes the character by an exact form. Additivity is the block-sum formula, and unitary module isomorphisms conjugate the curvature without changing its trace. Equations (R5)--(R7) prove homotopy invariance, giving the asserted map on K-classes. For Hermitian connections its components are real. For a flat bundle the curvature is zero; its fiber trace is one, giving character \(1\) in every path component.

These statements have a compact-support and relative version, which will also be needed. A relative projection pair may be made equal, with its specified comparison, on a collar of the collapsed subcomplex or near infinity. Choose the two connections to agree through that comparison there; extend them using the affine space of connections and a partition. Their difference character is compactly supported (or relative), and (R7) is a compactly supported transgression for any change respecting that comparison. The finite mapping cone of a subcomplex is again a finite polyhedron, so (R5) applies there; collapsing its contractible cone gives the relative group by CF.2 and the actual excision of Lesson 14. On a line, a compact-support projection pair can be made equal outside a compact interval: at infinity it is close to its constant limiting projection, and the close-projection unitary is joined to \(1\) and tapered off there. The same argument works on \(P\times\mathbb R\). Thus this construction applies to the projection definitions of the suspension K-groups as well.

Product connections for a scalar bundle and an \(A\)-module bundle have curvature \(R_E\otimes1+1\otimes R_V\); the summands commute as even forms. Expanding the exponential and taking the trace proves (R3), and proves the corresponding relative and compact-support products. For the planar projection \(q\) of RK.6, the unit frame \(v=(1,z)/\sqrt{1+|z|^2}\), in the coordinate \(z=re^{i\theta}\), gives
\[
 \omega=v^*dv=\frac{i r^2}{1+r^2}\,d\theta,\qquad
 R=d\omega=\frac{2i r}{(1+r^2)^2}\,dr\wedge d\theta.
\]
Consequently
\[
 \frac{-1}{2\pi i}\int_{\mathbb R^2}R
   =-\int_0^\infty\frac{2r}{(1+r^2)^2}\,dr=-1.
\]
This is the character of \([q]-[P]\): the constant projection has zero positive-degree curvature, while the rank terms cancel. The same normalization follows from Stokes on the two trivializing discs, with transition of the tautological line of degree \(-1\). It agrees with CF.5b. Changing the sign of a Bott generator changes this to \(+1\). Accordingly fiber integration of the compact-support character of an exterior Bott product is \(c_b\) times the original character, where \(c_b=\pm1\) is the explicitly chosen Bott sign. It is an invertible scalar, retained in the following suspension comparisons.

For \(u\in K_1(C(P))\) and \(v\in K_1(A)\), their suspension representatives lie in \(K_0^c(P\times\mathbb R)\) and \(K_0^c(\mathbb R;A)\). For the latter relative bundle, (R6) is identically zero: curvature two-forms on a line vanish, while its degree-zero trace difference is locally constant and zero near infinity, hence zero on the entire line. The compact-support product character is therefore zero on \(P\times\mathbb R^2\). The inverse Bott comparison and its nonzero \(c_b\) then give \(\operatorname{ch}_\tau(u\boxtimes v)=0\). This proves the odd-by-odd assertion with the actual suspension representatives, irrespective of their product's fixed Clifford sign.

**Proof of (R4), without a rational comparison assertion on arbitrary compact spaces.** Use the preceding scalar relative character and define the odd character by the suspension representative and fiber integration over \(\mathbb R\). They are natural and compatible with the finite-pair exact sequences: the connecting maps are induced by the collapse maps of the finite mapping cones, as in Lesson 14's mapping-cone proof and CF.2; the character respects those maps and the suspension construction. When closing the two-periodic sequence, retain the just-computed factor \(c_b\). Multiplying the corresponding closing cohomology arrow by this same \(c_b\) keeps it exact and makes the diagram commute. This states the sign rather than treating a positive course Bott element as an unspecified positive cohomology generator.

On an \(r\)-cell the character is an isomorphism over \(\mathbb R\): in even dimension its generator is an ordered exterior product of planar Bott generators, with character integral a product of the factors \(c_b=\pm1\), by the compact-support product formula and Fubini. In odd dimension suspension gives the same nonzero normalized value. Degree-zero cells give rank. Relative groups are direct sums of these cell groups. The scalar K-groups are finitely generated by A.10b, so tensoring their exact sequences with \(\mathbb R\) preserves exactness. The finite-pair diagrams just proved, induction on the skeleta and the same five-term chase prove an isomorphism on the whole complex in both parities. The even one is (R4). This proves precisely the injectivity used below; it imports neither a general manifold index formula nor a comparison theorem on an arbitrary compact Hausdorff base. \(\square\)

**Proposition A.10d (the all-cycle tracial pairing identity).** For a flat rank-one \(A\)-module bundle \(L\) over a finite polyhedron \(P\), with the normalized trace just specified, and every \(y\in KK_0(C(P),\mathbb C)\),
\[
 \tau_*\!\left([L]\otimes_{C(P)\otimes A}
                                 (y\boxtimes1_A)\right)
             =\langle[1_P],y\rangle\in\mathbb Z .
 \tag{R8}
\]

**Proof.** By (R2), rationally write
\([L]=\sum_\ell a_\ell\boxtimes v_\ell+
       \sum_m b_m\boxtimes w_m\),
where \(a_\ell\in K_0(C(P))\otimes\mathbb Q\),
\(v_\ell\in K_0(A)\), \(b_m\in K_1(C(P))\otimes\mathbb Q\) and
\(w_m\in K_1(A)\), allowing rational coefficients in the scalar factors. Equations (R3) and A.10c give
\[
 1=\operatorname{ch}_\tau(L)
       =\operatorname{ch}\!\left(
                     \sum_\ell\tau_*(v_\ell)a_\ell\right).
\]
Injectivity in (R4) makes the real K-class in parentheses equal to \([1_P]\).
Kasparov exterior interchange shows that pairing the even terms with
\(y\boxtimes1_A\) gives
\(\langle a_\ell,y\rangle v_\ell\). Pairing the odd terms gives zero: their scalar factor lies in \(KK_1(\mathbb C,\mathbb C)=0\). All rational equalities are legitimate under \(\tau_*\), since a homomorphism into \(\mathbb R\) kills torsion and extends uniquely over \(\mathbb Q\). Applying the real extension of the integer-valued scalar pairing to the equality of real K-classes proves (R8). Its right side is the actual scalar Fredholm index from Lesson 07, hence is an integer. No assumption on the nature of the representative of \(y\) was made. \(\square\)

**Theorem A.10 (torsion-free assembly trace integrality).** For every countable torsion-free discrete group \(\Gamma\),
\[
 \tau_*(\mu_r(x))\in\mathbb Z
       \quad\text{for every }x\in RK_0^\Gamma(E\Gamma;\mathbb C).
 \tag{R9}
\]
Consequently surjectivity of reduced assembly implies that the only projections and idempotents in the unamplified \(C_r^*(\Gamma)\) are \(0,1\).

**Proof.** A class is represented at a proper \(\Gamma\)-compact stage \(X\). Its action is free by the last assertion of A.7. Write \(y=\Theta_X(x)\) on the compact quotient \(Y\), using (Q5). A.10a gives a proper equivariant map to the covering \(Z\to P\) of a finite polyhedron, with quotient map \(f_0:Y\to P\). The quotient identification is natural for this map, as can be checked without a general Morita-naturality assertion. Choose a cutoff on \(Z\) and pull it back to \(X\); it has compact support by properness of the map and is normalized by equivariance, as in A.3. Then \(f^*p_Z=p_X\). The Morita source modules in (Q5) are \(p_ZD_Z\) and \(p_XD_X\), and extending the first through \(f^*\rtimes\Gamma\) gives the second. Their left invariant-function action is pulled back by \(f_0^*\). The kernel unitary in A.8b identifies these modules with the canonical cutoff-independent quotient modules. Associativity therefore gives \(\Theta_Z(f_*x)=f_{0,*}\Theta_X(x)\) on every cycle class. Assembly naturality and (Q6) now give
\[
 \mu_r(x)=
 [L_P]\otimes_{C(P)\otimes C_r^*(\Gamma)}
                   ((f_{0,*}y)\boxtimes1).
 \tag{R10}
\]
Apply (R8), with the normalized trace proved in A.6. Its integer value is
\(\langle1_P,f_{0,*}y\rangle=\langle f_0^*1_P,y\rangle
=\langle1_Y,y\rangle\).
Here \(f_0\) is a map between compact quotients and its pullback is unital, so the last equality is exact. Thus (R9) holds for every analytic cycle at every stage and respects the direct limit by A.7. Proposition A.6 gives the stated projection and idempotent consequence under surjectivity. The same proof gives the trace formula for full assembly followed by the regular quotient.

For an even-dimensional covering Dirac, M.4 and (R8)--(R10) also give
\(\tau_*\operatorname{Ind}_{C_r^*(\Gamma)}(D_{\mathcal L})
=\operatorname{index}(D_M)\), including finite-rank twists. This statement does not need a triangulation or generation theorem for manifolds: the finite-complex reduction applies to its covering, and its quotient scalar class pairs with \(1\) by the actual Fredholm picture. No identification with the von Neumann dimensions of lifted kernels is a premise of this proof. \(\square\)

**Primary free source and exact scope.** Thomas Schick, *\(L^2\)-index, KK-theory, and connections*, arXiv:math/0306171, Sections 5--6, Lemma 5.2, Theorem 5.4 and Proposition 6.7 give the tracial-connection method and the vanishing of the odd-by-odd contribution. Its externally quoted general Künneth theorem is not a proof provider here: A.10b proves the finite-complex rational form actually used. A.10c also proves the finite-polyhedron form/cohomology, relative-character and rational comparison steps, and A.10a supplies the reduction of every analytic proper stage. Therefore A.10d--A.10 apply to all analytic cycles; they are not an elliptic-only argument silently extended by a missing generation theorem. The separate von Neumann-kernel definition of the \(L^2\)-index is not a premise of (R8).

<a id="6-the-conjecture-and-its-mathematical-scope"></a>

## 7. The conjecture and its mathematical scope

For a given classifying space \(\mathcal E G\) for proper actions, the **Baum–Connes conjecture** asserts that
\[
\mu_r:RK_i^G(\mathcal E G;\mathbb C)\longrightarrow K_i(C_r^*(G))
\]
is an isomorphism in both degrees. Its **coefficient version** asserts that (A16) is an isomorphism for every separable \(G\)-algebra \(A\). These are assertions about the reduced crossed product. Formula (A14) does not assert that the full assembly map or the coefficient quotient is always an isomorphism.

The following are statements of known results, not premises of the proofs in Sections 1–6. The freely accessible survey by Gomez Aparicio, Julg and Valette, Section 1.5, records the coefficient theorem for groups with the Haagerup property and for hyperbolic groups. Here the Haagerup property means the existence of a metrically proper continuous affine isometric action on a Hilbert space; for a finitely generated discrete group, hyperbolicity means that some Cayley graph has uniformly thin geodesic triangles. Their Section 2.4, Theorem 2.6, records the scalar-coefficient Connes–Kasparov theorem for almost connected groups, meaning that the group of components is compact. The survey also describes Lafforgue's scalar-coefficient results for semisimple groups and discrete subgroups satisfying his specified rapid-decay and geometric hypotheses, in Section 6.1.

The coefficient formulation has counterexamples: the same survey's Section 7.2 distinguishes groupoid counterexamples from the transformation-groupoid examples giving group counterexamples with a suitable coefficient algebra. Valette's freely available 2026 course states the coefficient formulation and its limitation in Section 7.3.2. These counterexamples are not claims that scalar assembly fails for every group in question. No proof of these general status statements is given here.

Two further assigned statements are recorded without use in the proofs. The **strong Novikov assertion** is rational injectivity of the reduced assembly map from \(K_*(B\Gamma)\); its higher-signature implication asserts that the numbers
\(\langle L(M)\smile f^*\alpha,[M]\rangle\), for \(f:M\to B\Gamma\) and \(\alpha\in H^*(B\Gamma;\mathbb Q)\), are invariant under oriented homotopy equivalence of the manifold with its reference map. This implication and its signature-class interpretation are stated here. For a free group \(F_r\), scalar reduced assembly is an isomorphism; the Pimsner–Voiculescu computation gives \(K_0(C_r^*(F_r))=\mathbb Z[1]\) and \(K_1(C_r^*(F_r))=\mathbb Z^r\), generated by its free-generator unitaries. These are survey statements in Gomez Aparicio–Julg–Valette, Sections 2.5 and 3.2, and Valette, Sections 7.4.1 and 10.2, not prerequisites for the lattice, trace or finite-group proofs.

For a countable torsion-free discrete group \(\Gamma\), Theorem A.10 proves the **assembly trace integrality statement**
\[
\tau_*\!\left(\operatorname{im}
 \left(\mu_r:RK_0^\Gamma(\mathcal E\Gamma)\to
                         K_0(C_r^*(\Gamma))\right)\right)
 \subset\mathbb Z.
\tag{A29}
\]
The proof is (R1)–(R10): it reduces every free cocompact analytic stage to a finite complex and proves the flat-bundle tracial pairing there. It uses neither an unproved geometric generation theorem nor the separate von Neumann-kernel formulation of the covering index. If reduced assembly is surjective, (A29) and Proposition A.6 prove the torsion-free Kadison–Kaplansky projection and idempotent conclusion.

Theorem A.9 proves the lattice assembly isomorphism:
\[
\mu_r:KK_i^{\mathbb Z^n}(C_0(\mathbb R^n),\mathbb C)
       \longrightarrow K_i(C_r^*(\mathbb Z^n))
\quad\hbox{is an isomorphism.}
\tag{A30}
\]
The actual cutoff/descent map is identified with ordered iterated Connes–Thom by (T10)–(T11), including every analytic class through the proved torus duality (T4). The holonomy-compatible Green module (T6) includes the target inversion required by the specified Mishchenko convention. The finite-group assembly isomorphism is Theorem A.5.

<a id="7-exercises-and-their-current-solutions"></a>

## 8. Exercises and solutions

**8.1.** Compute the cutoff projection for translation of \(\mathbb Z\) on \(\mathbb R\).

**Solution.** Use \(h(x)=\max(1-|x|,0)\). At \(x=k+t\), \(0\leq t\leq1\), its two nonzero translates have values \(1-t,t\), so their sum is one. Thus \(c=\sqrt h\) is a cutoff and \(p(n,x)=\sqrt{h(x)h(x-n)}\). The values vanish outside the adjacent-interval overlaps for \(n=\pm1\), and outside \(n=0,\pm1\). The convolution proof (A7) shows it is a projection. Its class is independent of the chosen normalized cutoff by the explicit path and partial-isometry proof of Proposition A.2.

**8.2.** Identify finite-group assembly with Green–Julg.

**Solution.** The cutoff for the point is the averaging projection \(p_G\). Its range in the crossed regular module consists of the tuples \(\zeta_f(h)(t)=\alpha_{t^{-1}}f(th)\). Equation (A22) gives the exact crossed-product inner product, and (A23) is the resulting unitary. Equation (A24) identifies invariant compact operators and their multipliers with the same operators in the proved Green–Julg correspondence. Compression of an invariant cycle operator therefore gives that correspondence on every cycle and homotopy, as proved in Theorem A.5.

**8.3.** Deduce the idempotent conclusion from surjective assembly and integral trace on its image.

**Solution.** Surjectivity puts every \(K_0\)-class in the integral-trace image. A projection in the unamplified reduced algebra has trace in \([0,1]\), hence trace zero or one. The faithful trace proof preceding Proposition A.6 gives projection zero or identity. For an idempotent \(e\), the explicitly constructed projection \(p=ee^*(1-(e-e^*)^2)^{-1}\) has \(pe=e\) and \(ep=p\). Either possible value of \(p\) therefore forces the same value of \(e\). Theorem A.10 supplies the integral-trace hypothesis for every countable torsion-free group; with surjective reduced assembly, this solves the assigned torsion-free consequence.

**8.4.** Prove the \(\mathbb Z^2\) assembly isomorphism using two Connes–Thom maps.

**Solution.** Cross the second coordinate and then the first, using the two positive-in-both-parities Connes–Thom isomorphisms. Equation (T12) identifies their composition, followed by the specified Green equivalence and a minus sign, with assembly under the quotient identification (Q5) and the integral torus duality (T4). Each factor is invertible, proving the actual assembly map is an isomorphism in both degrees. The derivative matrices and the target coordinate inversion that produce the minus sign are displayed immediately after (T12).

## What this lesson does not prove

The proved results are cutoff, cycle and model independence; full/reduced assembly and its space/coefficient naturality; finite-group and lattice isomorphisms; the covering Dirac and all-cycle Mishchenko comparisons; and integral trace on the entire torsion-free assembly image, with the projection/idempotent consequence under surjectivity. The general Baum–Connes conjecture and the group/status, higher-signature and free-group results in Section 7 are stated and unused. This lesson does not prove those survey theorems or identify the numerical tracial index with the separate von Neumann-kernel definition of the L²-index.

## Freely accessible reading

- Markus Land, [*The Analytical Assembly Map and Index Theory*](https://arxiv.org/abs/1306.5657), Sections 2–4, for assembly, Mishchenko bundles and their comparison.
- Alain Valette, [*The Baum–Connes conjecture: a concise course*](https://arxiv.org/abs/2610.01802), version 1, 1 October 2026, Sections 4.1, 7.2–7.4 and 8, for the formulations and covering-index/Dirac context.
- Maria Paula Gomez Aparicio, Pierre Julg and Alain Valette, [*The Baum–Connes conjecture: an extended survey*](https://arxiv.org/abs/1905.10081), Section 1.5, Section 2.4, Section 6.1 and Section 7.2, for the explicitly stated status results. Its 2019 list of open cases is not asserted as a current list of open problems.

- Wolfgang Lück, [*Survey on classifying spaces for families of subgroups*](https://arxiv.org/abs/math/0312378), Definitions 1.8 and 2.1 and Theorem 2.5, for the universal proper/numerable distinction; the used model comparison is proved in (U1)–(U8).
- Thomas Schick, [*L²-index, KK-theory, and connections*](https://arxiv.org/abs/math/0306171), Sections 5–6, for the tracial connection method; the finite-complex and all-cycle steps actually used are proved in (R1)–(R10).
