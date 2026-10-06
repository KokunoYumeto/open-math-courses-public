# Cone geometry, support corners, and positive functionals

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Original text and embedded diagram: public domain (CC0).*

Normal positive functionals need not be faithful, and a von Neumann algebra need not admit a faithful normal state. We first control cone vectors and their support projections, then reduce each functional to its own supported corner. The realization theorem needed in that corner is the cyclic theorem stated below.

## Objects and the two modular inputs

The inner product is linear in its second variable. Thus
\[
 \omega_\xi(a)=\langle\xi,a\xi\rangle.
\]
For a first-variable-linear source inner product \((\cdot\mid\cdot)\), our convention is \(\langle\xi,\eta\rangle=(\eta\mid\xi)\). An antiunitary involution satisfies \(\langle J\xi,J\eta\rangle=\langle\eta,\xi\rangle\).

Let \(N\) be an arbitrary von Neumann algebra. Choose a faithful normal semifinite weight on \(N\), and use its full left Hilbert algebra to construct a faithful normal representation \(N\cong M\subset B(H)\). The choice of weight and the faithful full-Hilbert-algebra realization are part of the construction input. In this chapter the form is this constructed form. The modular construction needed here has the following exact output, denoted **MC**:

1. \(J\) is an antiunitary involution, \(JMJ=M'\), and \(JzJ=z^*\) for \(z\in Z(M)\).
2. \(P\subset H\) is a closed convex cone, fixed pointwise by \(J\), and self-dual:
   \[
   P=\{u\in H:\langle u,v\rangle\in[0,\infty)\text{ for every }v\in P\}.
   \]
3. For every \(a\in M\), \(aJaJ(P)\subset P\).
4. In every cyclic separating representation of a von Neumann algebra \(A\subset B(K)\), including \(A=qMq\subset B(qH)\) for the corners below, the closure \(S\) of \(a\gamma\mapsto a^*\gamma\) has adjoint core \(A'\gamma\), with \(S^*(b'\gamma)=b'^*\gamma\), and has the modular polar decomposition. Its natural cone
   \[
   P_\gamma=\overline{\{aJ_\gamma aJ_\gamma\gamma:a\in A\}}
   \]
   is self-dual.

The commutant has the same geometric data \((H,J,P)\). Indeed \(JM'J=M\), its center equals \(Z(M)\), and, if \(a'=JaJ\in M'\), then
\[
 a'Ja'J=(JaJ)a=aJaJ.
\]
The two factors commute, so this operator preserves \(P\) by MC3. The cyclic-core output MC4 already applies to every cyclic separating representation. Thus the arguments below apply to the commutant with this same cone.

MC includes existence and self-duality of the cone; they are not proved by the geometric lemmas below. The free bounded modular route [RC–GP–RS–IK–MC–MP](https://kokunoyumeto.github.io/open-math-courses-public/courses/OA-MOD/notes/real-coercivity/bounded-modular-polar.html) supplies the commutant and polar-operator part, with its exact graph domains. The additional natural-cone construction is the part of Araki's Theorems 1–4 and Haagerup's Theorem 1.6 used as a conditional input here; the endpoint cone-duality proof is a separate dependency from the commutant theorem. The separate analytic input **CR** is:

> In the natural cone of a cyclic separating vector, every bounded normal positive functional has a representing vector in that cone.

Araki's Theorem 6, printed pages 335–339, supplies CR subject to its analytic antecedents. The geometry below proves uniqueness without CR, and proves the full passage from CR to arbitrary, possibly nonfaithful functionals. Only that last passage uses CR. Bounded continuous functional calculus, the bicommutant characterization, and Hilbert-space completeness are the elementary operator prerequisites.

## CG01. Normal supports without a representing vector

A bounded increasing net \((a_i)\) of positive operators has a strong supremum. Indeed, its scalar quadratic forms have limits, polarization gives a bounded positive operator \(a\), and
\[
 \|(a-a_i)u\|^2\le C\langle u,(a-a_i)u\rangle\longrightarrow0
\]
when \(0\le a-a_i\le C1\). A strongly closed algebra contains this supremum. The same argument applies to increasing nets of projections.

Let \(\omega\) be a bounded normal positive functional on \(M\). Positivity gives the Cauchy–Schwarz inequality
\[
 |\omega(x^*y)|^2\le\omega(x^*x)\omega(y^*y).
\]
For completeness, apply positivity to \((x+ty)^*(x+ty)\), minimize its scalar quadratic polynomial when \(\omega(y^*y)>0\), and use arbitrarily small positive denominators when \(\omega(y^*y)=0\). Consequently a projection \(e\) with \(\omega(e)=0\) satisfies \(\omega(xe)=\omega(ex)=0\) for every \(x\).

Null projections are closed under joins, including uncountable joins. If \(e,f\) are null and \(h=e+f\), then \(\omega(h)=0\). The continuous-calculus contractions
\[
 h(h+\varepsilon)^{-1}\le\varepsilon^{-1}h
\]
increase strongly to the range projection of \(h\), which is \(e\vee f\): \(\ker h=\ker e\cap\ker f\). Normality gives \(\omega(e\vee f)=0\). The directed net of finite joins of any family of null projections has a strong supremum and zero \(\omega\)-value. Let \(r\) be the join of all null projections and put
\[
 s(\omega)=1-r.
\]
This is the least projection \(p\) for which \(\omega(1-p)=0\). Cauchy–Schwarz gives
\[
 \omega(x)=\omega(pxp),\qquad p=s(\omega).
 \tag{1}
\]
The restriction to \(pMp\) is faithful. To see this, if \(b\in(pMp)_+\) and \(\omega(b)=0\), the same contractions \(b(b+\varepsilon)^{-1}\) show that the range projection of \(b\) is null. It lies below both \(p\) and \(r\), so it is zero and \(b=0\).

If \(\psi\le\omega\), then \(\psi(1-s(\omega))=0\), and hence
\[
 s(\psi)\le s(\omega).
 \tag{2}
\]
This is an order statement about functional supports. It makes no assertion that functional order is the order of their eventual cone vectors.

## CG02. Algebra and commutant supports of a cone vector

For any \(\xi\in H\), the projection \(s_\xi\) onto \(\overline{M'\xi}\) belongs to \(M\): the subspace reduces \(M'\). It is the least projection in \(M\) fixing \(\xi\). Since
\[
 \omega_\xi(1-e)=\|(1-e)\xi\|^2
\]
for a projection \(e\in M\), CG01 implies \(s_\xi=s(\omega_\xi)\). Vector functionals are normal because bounded increasing positive nets converge strongly, as proved above.

If \(\xi\in P\), then \(J\xi=\xi\), and applying \(J\) to \(\overline{M'\xi}\) gives \(\overline{M\xi}\). Therefore the projection \(q_\xi\) onto the latter subspace satisfies
\[
 \boxed{q_\xi=Js_\xi J.}
 \tag{3}
\]
In particular \(\xi\) is separating for \(M\) exactly when \(s_\xi=1\), and is cyclic exactly when \(q_\xi=1\). The same conclusions hold on every support corner constructed below.

## CG03. Orthogonality detects disjoint supports

For \(\xi,\eta\in P\),
\[
 \langle\eta,\xi\rangle=0
 \quad\Longleftrightarrow\quad
 s_\xi s_\eta=0.
 \tag{4}
\]
Here is a direct proof of the nontrivial implication. Fix \(a\in M\) and \(z\in\mathbb C\). Cone preservation and self-duality give
\[
 0\le\langle\eta,(1+za)J(1+za)J\xi\rangle
   =2\operatorname{Re}(zA)+|z|^2C,
 \tag{5}
\]
where \(A=\langle\eta,a\xi\rangle\) and \(C=\langle\eta,aJaJ\xi\rangle\ge0\). In this convention \(J(1+za)J=1+\overline zJaJ\), and
\(\langle\eta,JaJ\xi\rangle=\overline A\), so the displayed expansion includes both scalar conjugations. If \(A\ne0\), choose \(z=-t\overline A/|A|\) and let \(t>0\) decrease to zero. The right side is \(-2t|A|+t^2C<0\) for small \(t\), a contradiction. Thus \(\eta\perp M\xi\).

By CG02, \(q_\xi\eta=0\). Conjugating by \(J\) gives \(s_\xi\eta=0\). The projection \(1-s_\xi\) fixes \(\eta\), so minimality of \(s_\eta\) gives \(s_\eta\le1-s_\xi\). Conversely, disjoint supports put \(\xi\) and \(\eta\) in orthogonal projection ranges. Applying \(J\) also gives \(q_\xi q_\eta=0\).

## CG04. Orthogonal positive and negative parts

Let \(H_J=\{v:Jv=v\}\), regarded as a real Hilbert space. Every \(v\in H_J\) has a unique decomposition
\[
 v=v_+-v_-,\qquad v_+,v_-\in P,
 \qquad\langle v_+,v_-\rangle=0.
 \tag{6}
\]
To prove it, let \(d=\inf_{u\in P}\|v-u\|\) and choose a minimizing sequence \(u_n\). The parallelogram identity and \((u_n+u_m)/2\in P\) give
\[
 \|u_n-u_m\|^2
 \le2\|v-u_n\|^2+2\|v-u_m\|^2-4d^2\longrightarrow0.
\]
Its limit \(p\in P\) attains the minimum. Varying \(p\) to \(p+t u\), \(u\in P\), \(t\ge0\), gives \(\langle p-v,u\rangle\ge0\). Varying to \((1+t)p\) for small positive and negative \(t\) gives \(\langle p-v,p\rangle=0\). Self-duality gives \(n=p-v\in P\), and \(v=p-n\) with \(p\perp n\).

If \(v=p-n\) is any such decomposition, then for \(u\in P\),
\[
 \|v-u\|^2=\|p-u\|^2+\|n\|^2+2\langle n,u\rangle\ge\|n\|^2.
\]
Equality holds at \(u=p\), and can hold only there. Thus \(p\) is the unique closest point and \(n=p-v\) is unique too. CG03 shows that their algebra supports are disjoint.

Every \(v\in H\) is a complex linear combination of four cone vectors: apply (6) to \((v+Jv)/2\) and \((v-Jv)/(2i)\). In particular the complex span of \(P\) is dense in \(H\), indeed equals \(H\).

## CG05. The two norm bounds and uniqueness

For \(\xi,\eta\in P\),
\[
 \boxed{\|\xi-\eta\|^2\le\|\omega_\xi-\omega_\eta\|
       \le\|\xi-\eta\|\,\|\xi+\eta\|.}
 \tag{7}
\]
Write \(d=\xi-\eta=p-n\) as in CG04, and let \(e=s_p\), \(f=s_n\). These projections are orthogonal. If \(\delta=\omega_\xi-\omega_\eta\), then \(ed=p\) and \(fd=-n\), so
\[
\begin{aligned}
 \delta(e)&=\|p\|^2+2\langle p,\eta\rangle\ge\|p\|^2,\\
 \delta(f)&=-\|n\|^2-2\langle n,\xi\rangle\le-\|n\|^2.
\end{aligned}
\]
The pairings are real and nonnegative by self-duality. Since \(e-f\) is a self-adjoint contraction,
\[
 \|\delta\|\ge\delta(e-f)
 \ge\|p\|^2+\|n\|^2=\|d\|^2.
\]
This proves the lower bound without first assuming that any given normal functional has a representative.

For a Hermitian functional the norm can be tested on self-adjoint contractions: for any contraction \(a\), choose a scalar \(\lambda\) of modulus one with \(\lambda\delta(a)=|\delta(a)|\), and test \((\lambda a+\overline\lambda a^*)/2\). For self-adjoint \(a\),
\[
 \delta(a)=\operatorname{Re}\langle\xi-\eta,a(\xi+\eta)\rangle.
\]
Cauchy–Schwarz proves the upper bound in (7). For any positive functional \(\omega\), Cauchy–Schwarz gives \(|\omega(a)|^2\le\omega(1)\omega(a^*a)\le\omega(1)^2\) for a contraction \(a\); testing at one therefore gives \(\|\omega\|=\omega(1)\). In particular \(\|\omega_\xi\|=\|\xi\|^2\). The lower bound proves that a normal positive functional has at most one representative in \(P\). It also shows that the set of functionals represented in \(P\) is norm closed: a norm-Cauchy sequence of represented functionals has norm-Cauchy representatives, whose limit lies in \(P\) and represents the limit by the upper bound.

<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="650" viewBox="0 0 1100 650" role="img" aria-labelledby="title desc">
  <title id="title">Positive decomposition and norm bound in the two-point algebra</title>
  <desc id="desc">The positive quadrant is the natural cone for the diagonal algebra C squared. Xi is three comma one, eta is one comma two, their difference is two comma minus one, its positive part is two comma zero, and its negative part is zero comma one. The squared distance is five and the functional difference norm is eleven.</desc>
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10Z" fill="context-stroke"/></marker>
    <style>text{font-family:Arial,sans-serif;fill:#172737}.title{font-size:28px;font-weight:700}.body{font-size:21px}.small{font-size:18px}.label{font-size:23px;font-weight:600}.axis{stroke:#506472;stroke-width:2}.grid{stroke:#d9e3e7;stroke-width:1}.vector{stroke-width:4;fill:none;marker-end:url(#arrow)}</style>
  </defs>
  <rect width="1100" height="650" fill="#fff"/>
  <text x="42" y="48" class="title">The support test controls the vector distance</text>
  <text x="42" y="79" class="body">Exact model: M = C², H = C², J = coordinate conjugation, P = R²₊</text>
  <g transform="translate(85 430)">
    <rect x="0" y="-285" width="365" height="285" fill="#e8f5ed"/>
    <path d="M0 -190H365M0 -95H365M95 -285V115M190 -285V115M285 -285V115" class="grid"/>
    <path d="M-30 0H380M0 130V-305" class="axis" marker-end="url(#arrow)"/>
    <text x="-21" y="24" class="small">0</text>
    <text x="90" y="24" class="small">1</text><text x="184" y="24" class="small">2</text><text x="279" y="24" class="small">3</text>
    <text x="-22" y="-88" class="small">1</text><text x="-22" y="-184" class="small">2</text><text x="-29" y="103" class="small">−1</text>
    <text x="345" y="-264" class="label">P</text>
    <path d="M0 0L285 -95" class="vector" stroke="#25669a"/>
    <path d="M0 0L95 -190" class="vector" stroke="#9262a6"/>
    <path d="M0 0L190 95" class="vector" stroke="#c55d23"/>
    <path d="M0 0L190 0" class="vector" stroke="#247c53"/>
    <path d="M190 0L190 95" class="vector" stroke="#c55d23" stroke-dasharray="7 5"/>
    <path d="M0 0L0 -95" class="vector" stroke="#247c53"/>
    <circle cx="190" cy="0" r="5" fill="#247c53"/>
    <text x="275" y="-114" class="label">ξ = (3, 1)</text>
    <text x="77" y="-211" class="label">η = (1, 2)</text>
    <text x="207" y="100" class="label">d = (2, −1)</text>
    <text x="168" y="-20" class="label">p = (2, 0)</text>
    <text x="-30" y="-121" class="small">n = (0, 1)</text>
    <text x="202" y="58" class="small">−n</text>
  </g>
  <g transform="translate(575 146)">
    <text x="0" y="0" class="label">Orthogonal cone parts (CG04)</text>
    <text x="0" y="37" class="body">d = p − n,     ⟨p, n⟩ = 0</text>
    <text x="0" y="74" class="body">p is the closest cone point to d.</text>
    <text x="0" y="126" class="label">Orthogonal support projections (CG03)</text>
    <text x="0" y="163" class="body">e = diag(1, 0),   f = diag(0, 1)</text>
    <text x="0" y="200" class="body">e f = 0,     ‖e − f‖ = 1</text>
    <text x="0" y="252" class="label">The norm test (CG05)</text>
    <text x="0" y="289" class="body">ωξ = (9, 1),   ωη = (1, 4)</text>
    <text x="0" y="326" class="body">δ(e − f) = 8 + 3 = ‖δ‖ = 11</text>
    <text x="0" y="363" class="body">‖d‖² = 4 + 1 = 5 ≤ 11</text>
    <text x="0" y="400" class="body">Excess = 2⟨p, η⟩ + 2⟨n, ξ⟩ = 6</text>
  </g>
  <text x="42" y="609" class="small">The diagram depicts this two-point model. The general proof uses a self-dual cone and projection supports.</text>
  <text x="42" y="634" class="small">Proofs CG03–CG05; related conclusions: Araki 1974, Theorem 4(6)–(8), pp. 328–332; Haagerup 1975, Lemma 2.10.</text>
</svg>

In this figure \(M=\mathbb C^2\) acts diagonally on \(H=\mathbb C^2\), \(J\) is coordinate conjugation, and \(P=\mathbb R_+^2\). With \(\xi=(3,1)\) and \(\eta=(1,2)\), the closest cone point to \(d=(2,-1)\) is \(p=(2,0)\), and \(n=(0,1)\). The support test \(e-f=\operatorname{diag}(1,-1)\) gives \(\|\omega_\xi-\omega_\eta\|=|8|+|-3|=11\ge5=\|d\|^2\). The excess is \(2\langle p,\eta\rangle+2\langle n,\xi\rangle=6\). This is a concrete commutative example of CG04–CG05, not a claim that a general natural cone is two-dimensional. Araki's related general conclusions are Theorem 4(6)–(8), printed pages 328–332; Haagerup's two bounds are Lemma 2.10, printed pages 278–279.

## CG06. A corner commutant proved by a Gram form

We need a corner theorem at arbitrary Hilbert-space cardinality. If \(A\subset B(K)\) is a von Neumann algebra and \(p\in A\) is a projection, then, on \(pK\),
\[
 (pAp)'=pA'p.
 \tag{8}
\]
Here is its full proof. Let \(T\in(pAp)'\), acting on \(pK\). On the algebraic span of \(ApK\) define
\[
 \widehat T\Big(\sum_i a_i u_i\Big)=\sum_i a_i T u_i,
 \qquad a_i\in A,\quad u_i\in pK.
 \tag{9}
\]
The positive matrix \(G=(pa_i^*a_jp)_{ij}\) on \((pK)^n\) gives
\(\|\sum_i a_i u_i\|^2=\langle u,Gu\rangle\).
The diagonal operator \(D=\operatorname{diag}(T,\ldots,T)\) and its adjoint commute with \(G\), because its entries lie in \(pAp\). Continuous functional calculus gives commutation with \(G^{1/2}\); hence
\[
 \Big\|\sum_i a_i T u_i\Big\|^2
   =\|G^{1/2}Du\|^2
   \le\|T\|^2\|G^{1/2}u\|^2.
\]
This proves that (9) is well defined and bounded, even when the displayed vector has more than one expression.

The closed subspace \(L=\overline{ApK}\) reduces both \(A\) and \(A'\). Thus its projection is central in \(A\). Extend \(\widehat T\) by zero on \(L^\perp\). On the dense algebraic span it commutes with every member of \(A\), and therefore it belongs to \(A'\). Its restriction to \(pK\) is \(T\). This gives the difficult inclusion in (8); the other inclusion follows by multiplication. The proof uses finite Gram matrices, not a countable generating set.

Let \(z_A(p)\) be the projection onto \(\overline{ApK}\). The preceding reduction shows that it is the least central projection above \(p\). If \(e\in A\), \(f\in A'\) are projections and \(ef=0\), then \(f\) kills \(AeK\), so \(f z_A(e)=0\). Taking the least central projection above \(f\) gives
\[
 z_A(e)z_{A'}(f)=0.
 \tag{10}
\]
Finally,
\[
 Z(pAp)=pZ(A).
 \tag{11}
\]
To see this, extend \(T\in Z(pAp)\) by (9). The operator \(T\) itself belongs to \(A\), so it commutes with every \(b\in A'\) on \(pK\). On \(ApK\), equation (9) then shows \(\widehat T b=b\widehat T\). Both extensions preserve \(L\), and the extension is zero on \(L^\perp\), so \(\widehat T\) also commutes with \(A'\). The bicommutant theorem puts it in \(A\cap A'=Z(A)\), with \(p\widehat T p=T\). The reverse inclusion in (11) is immediate.

## CG07. The simultaneous support corner

For \(p\in M\) put \(j(p)=JpJ\) and \(q=pj(p)\). The central identity in MC gives
\[
 z_{M'}(j(p))=z_M(p).
\]
If \(p\ne0\), then \(q\ne0\), since otherwise (10) would make this nonzero central projection orthogonal to itself.

The map
\[
 \theta:pMp\longrightarrow qMq\subset B(qH),
 \qquad \theta(a)=a|_{qH},
 \tag{12}
\]
is a faithful normal unital *-isomorphism, and
\[
 (qMq)'=qM'q\quad\text{on }qH.
 \tag{13}
\]
To verify (13) without an induction theorem, first apply (8) to \(M,p\) on \(H\), obtaining \((pMp)'=pM'p\) on \(pH\). There \(q\) belongs to the latter commutant. Apply (8) again, now to \(pM'p\) and its projection \(q\). It gives \((qM'q)'=qMq\). In particular \(qMq\) is a von Neumann algebra; taking commutants gives (13).

Because \(j(p)\) commutes with \(pMp\), (12) is multiplicative. It is onto because \(qxq=q(pxp)q\) for \(x\in M\). For injectivity suppose \(a\in pMp\) and \(aq=0\). Then \(aj(p)=0\). Let \(e\le p\) be the range projection of \(|a|\), obtained by increasing continuous-calculus contractions. Commutation with \(j(p)\) gives \(ej(p)=0\). By (10), \(z_M(e)\) is orthogonal to \(z_{M'}(j(p))=z_M(p)\), while \(z_M(e)\le z_M(p)\). Hence \(e=0\) and \(a=0\).

A faithful *-isomorphism reflects positivity: apply it to the negative part of a self-adjoint operator, using continuous functional calculus. It is therefore an order isomorphism. Suprema of bounded increasing positive nets are characterized by order alone, so both \(\theta\) and its inverse preserve them. This proves the asserted normality.

The restriction \(J_q=J|_{qH}\) is an antiunitary involution, since \(JqJ=q\). The cone
\[
 P_q=qP=P\cap qH
 \tag{14}
\]
is closed: \(qP\subset P\) follows from MC with \(a=p\), and a vector of \(P\cap qH\) is its own image under \(q\). If \(v\in qH\) pairs nonnegatively with \(P_q\), then \(\langle v,u\rangle=\langle v,qu\rangle\ge0\) for all \(u\in P\); self-duality implies \(v\in P_q\). Thus \(P_q\) is self-dual on \(qH\).

Equations (13)–(14) give \(J_q(qMq)J_q=(qMq)'\). Cone preservation restricts as well: if \(a\in pMp\), then the operator \(\theta(a)J_q\theta(a)J_q\) on \(qH\) is the restriction of \(aJaJ\). The center is \(qZ(M)q\), by (11) and (12), and \(J_q cJ_q=c^*\) follows from MC. Hence the corner has all the displayed geometric properties of the constructed form. These conclusions correspond to Haagerup's Lemma 2.6, printed page 277, with the reduction facts here supplied by CG06.

## CG08. A cyclic separating cone vector on a state corner

Suppose \(M\) has a faithful normal state \(\alpha\). There is a cyclic separating vector \(\gamma\in P\).

Choose by the maximal principle a family of nonzero vectors in \(P\) with mutually orthogonal algebra supports \(p_i\). If \(r=1-\bigvee_i p_i\ne0\), CG07 gives a nonzero projection \(rJrJ\). Its cone is self-dual, and therefore cannot be \(\{0\}\) on its nonzero Hilbert space. A nonzero vector in this cone has algebra support below \(r\), contradicting maximality. Thus \(\bigvee_i p_i=1\).

Faithfulness gives \(\alpha(p_i)>0\). Finite sums of their values are at most one. For each positive integer \(k\), only finitely many values can exceed \(1/k\); their union shows that the family is countable. Normalize the vectors to have norm one and enumerate them as \(\gamma_i\). Choose strictly positive scalars \(c_i\) with \(\sum_i c_i^2<\infty\), and set
\[
 \gamma=\sum_i c_i\gamma_i\in P.
\]
Orthogonal supports make the series norm convergent. For \(b'\in M'\), each \(b'\gamma_i\) lies in \(p_iH\), so
\[
 \|b'\gamma\|^2=\sum_i c_i^2\|b'\gamma_i\|^2.
\]
If \(b'\gamma=0\), it follows that \(b'\gamma_i=0\) for every \(i\). Commutation with \(M\) makes \(b'\) vanish on \(M\gamma_i\), and therefore on its closure \(q_iH\), where \(q_i=Jp_iJ\). The join of the \(q_i\) is one, so \(b'=0\). The projection onto \(\overline{M\gamma}\) is consequently one. Since \(J\gamma=\gamma\), CG02 then also gives \(s_\gamma=1\). Thus \(\gamma\) is cyclic and separating. This proves the assertion without assuming a countable Hilbert-space dimension or a faithful normal state on the original arbitrary algebra.

## CG09. Identifying the cone after choosing that vector

Let \(\gamma\in P\) be cyclic and separating. The modular-core part of MC identifies its modular conjugation \(J_\gamma\) with \(J\), and hence identifies its natural cone with \(P\), as follows.

Let \(S\) be the closure of \(a\gamma\mapsto a^*\gamma\). On this core the linear operator \(JS\) has nonnegative quadratic form:
\[
 \langle a\gamma,Ja^*\gamma\rangle
   =\langle\gamma,a^*Ja^*J\gamma\rangle\ge0.
 \tag{15}
\]
It is therefore symmetric on the core, by polarization. The closed operator \(JS\) remains positive. Its adjoint is \(S^*J\); the adjoint-core assertion in MC makes \(M\gamma=JM'\gamma\) a core for that adjoint. On that core,
\[
 S^*J(a\gamma)=S^*((JaJ)\gamma)
   =(Ja^*J)\gamma=Ja^*\gamma.
\]
Thus \(JS\) and its adjoint have the same core and action, so \(JS\) is positive self-adjoint. Its positive polar factor is \((S^*S)^{1/2}\). The graph of the initial \(S\) is invariant under interchanging its coordinates; its closure is too, and therefore \(S^2u=u\) on its domain. This gives trivial kernel, while the range contains the dense space \(M\gamma\). Uniqueness of polar decomposition now gives \(J=J_\gamma\).

MC now gives a self-dual cone \(P_\gamma\) generated by \(aJaJ\gamma\). It is contained in \(P\) by cone preservation. Inclusion reverses under taking dual cones, so self-duality of both gives \(P_\gamma=P\). This proves the comparison needed here directly; it does not use a comparison of two different weight representations.

## CG09a. A dominated functional has a bounded commutant derivative

One elementary part of the analytic realization problem can be supplied without a representation theorem. Let \(\gamma\) be cyclic for \(M\), and let \(0\le\psi\le C\omega_\gamma\). The rule
\[
 \beta(a\gamma,b\gamma)=\psi(a^*b)
 \tag{16}
\]
is a well-defined positive sesquilinear form on \(M\gamma\), with
\[
 |\beta(a\gamma,b\gamma)|^2
 \le\psi(a^*a)\psi(b^*b)
 \le C^2\|a\gamma\|^2\|b\gamma\|^2.
\]
This both makes the definition independent of representatives and extends it continuously to \(H\). The Hilbert-space representation of bounded forms gives a unique \(0\le T\le C1\) with \(\beta(u,v)=\langle u,Tv\rangle\). For \(x\in M\), (16) gives
\[
 \beta(xa\gamma,b\gamma)=\beta(a\gamma,x^*b\gamma).
\]
Thus \(x^*T=Tx^*\) on a dense set and then on \(H\), so \(T\in M'\). Its bounded positive square root gives
\[
 \psi(a)=\langle\gamma,Ta\gamma\rangle
        =\langle T^{1/2}\gamma,aT^{1/2}\gamma\rangle.
 \tag{17}
\]
This proves bounded commutant realization for a dominated functional. It does not assert that \(T^{1/2}\gamma\) lies in the natural cone, and so does not replace CR.

## CG10. Positive functionals on an arbitrary algebra

Assume MC and CR. Every \(\omega\in M_*^+\) has a unique vector \(\xi_\omega\in P\) with
\[
 \omega(a)=\langle\xi_\omega,a\xi_\omega\rangle
 \quad(a\in M).
 \tag{18}
\]
No faithfulness, separability, countable decomposability, or cardinality restriction on \(M\) is imposed.

If \(\omega=0\), use zero. Otherwise let \(p=s(\omega)\), \(q=pJpJ\), and use (12) to transport \(\omega|_{pMp}\) to the von Neumann algebra \(qMq\). By CG01 this transported functional is faithful and normal, and its normalization is a faithful normal state. CG07–CG08 give a cyclic separating cone vector on \(qH\); CG09 identifies its natural cone with \(P_q\). CR gives a vector \(\xi\in P_q\) representing the transported functional. For every \(a\in M\),
\[
 \langle\xi,a\xi\rangle
 =\langle\xi,qaq\xi\rangle
 =\omega(pap)=\omega(a),
\]
where the last equality is (1). The vector lies in \(P\), and uniqueness follows from CG05. This closes the arbitrary-cardinality and nonfaithful reduction. It is Haagerup's Lemma 2.10 reduction, printed pages 278–279, with the corner algebra and cyclic cone identification proved above.

Combining CG01, CG02, CG05 and (18) gives precisely
\[
\begin{gathered}
 \|\xi_\omega-\xi_\psi\|^2\le\|\omega-\psi\|,\qquad
 q_{\xi_\omega}=Js(\omega)J,\\
 \psi\le\omega\Longrightarrow s(\psi)\le s(\omega),\qquad
 \|\xi_\omega\|^2=\omega(1).
\end{gathered}
\]
The proof of these geometric formulas is complete above. Existence of the initially constructed self-dual cone remains the MC construction input; existence in the cyclic natural cone remains CR. The cyclic input is Araki's Theorem 6, printed pages 335–339; its analytic construction uses positive affiliated-operator approximation in the cyclic representation.


## References

Huzihiro Araki, [Some properties of modular conjugation operator of von Neumann algebras and a non-commutative Radon–Nikodym theorem with a chain rule](https://msp.org/pjm/1974/50-2/pjm-v50-n2-p02-p.pdf), *Pacific Journal of Mathematics* 50 (1974), 309–354. Theorem 4(6)–(8) gives the orthogonal cone decomposition, support and squared-distance conclusions; Theorem 6 gives the cyclic normal-functional construction.

Uffe Haagerup, [The standard form of von Neumann algebras](https://journals.msp.org/mscand/article/download/2067/2066/2098), *Mathematica Scandinavica* 37 (1975), 271–283. Lemma 2.6 treats the standard corner and Lemma 2.10 passes from cyclic normal-functional representatives to arbitrary algebras. The corner commutant, support and norm arguments used in that passage are proved above.
