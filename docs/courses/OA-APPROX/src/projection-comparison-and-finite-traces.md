# Projection comparison and normal center-valued traces

*Written by GPT-6.1 Sol (OpenAI), Ultra, October 2026. New original text and embedded diagrams: public domain (CC0).*

Projection comparison lets finite corners be matched without a dimension function. We use it first to prove finite matrix stability and finite projection sums. Abelian corners and coherent dyadic partitions then provide monic projections; these allow normal almost traces to converge in norm to the center-valued trace. Every orthogonal sum below is the strong net of finite partial sums.

Let \(M\subseteq B(H)\) be a unital strongly closed self-adjoint algebra on an arbitrary Hilbert space. The unit is denoted by \(1\); when working in a corner its unit is the corner projection. The zero Hilbert space and zero corner are allowed and all projection assertions there are immediate. A projection is an operator \(p=p^*=p^2\). Write \(p\le q\) when \(pH\subseteq qH\), equivalently \(pq=qp=p\). Put
\[
p\sim q \iff \exists v\in M:\ v^*v=p,\ vv^*=q,
\qquad
p\precsim q \iff \exists v\in M:\ v^*v=p,\ vv^*\le q.
\]
Such an operator \(v\) is a partial isometry. A projection \(p\) is **finite** if every \(v\in M\) with \(v^*v=p\) and \(vv^*\le p\) has \(vv^*=p\). Thus \(M\) is finite exactly when its unit is finite, or equivalently every isometry in \(M\) is unitary.

The external proof inputs are H00 (Hilbert completeness, adjoints, bounded operators), H01 (orthogonal projections and strong closure), H02 (positive supports), the bounded polar construction T04a, and the C*-algebra completeness/calculus/order arguments F01–F08. Zorn's lemma is used for maximal orthonormal sets and for maximal matching families. No trace, countable decomposition, type classification, center-valued trace, predual realization, automatic normality, or properly infinite halving theorem is used. H03 is available but is not needed for this chain.

For an arbitrary Hilbert space, the coordinate version of H00 causes no restriction: a maximal orthonormal set exists by Zorn. A nonzero vector perpendicular to its closed span would enlarge it, so its span is dense. Finite orthogonal projections and completeness identify the space isometrically onto the square-summable coordinates on that set. Conversely square-summable coordinates have norm-convergent finite partial sums. This includes arbitrary cardinalities and the empty basis of the zero space.

<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="comparison-mechanism-title" width="360" height="700" viewBox="0 0 360 700">
<title id="comparison-mechanism-title">How general comparison proves finite orthogonal sums</title>
<defs><marker id="comparison-mechanism-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="#455c71"/></marker></defs>
<rect width="360" height="700" rx="12" fill="#f7fafc"/>
<rect x="12" y="18" width="336" height="84" rx="8" fill="#fff" stroke="#526f87"/>
<text x="180" y="40" text-anchor="middle" fill="#153b56" font-family="Arial,sans-serif" font-size="16" font-weight="bold">Central comparison</text>
<text x="180" y="61" text-anchor="middle" fill="#182a38" font-family="Arial,sans-serif" font-size="14">zp ≼ zq; (1 − z)q ≼ (1 − z)p</text>
<text x="335" y="94" text-anchor="end" fill="#455c71" font-family="Arial,sans-serif" font-size="12">C05</text>
<path d="M180 102V123" stroke="#455c71" stroke-width="2" marker-end="url(#comparison-mechanism-arrow)"/>
<rect x="12" y="126" width="336" height="84" rx="8" fill="#fff" stroke="#526f87"/>
<text x="180" y="148" text-anchor="middle" fill="#153b56" font-family="Arial,sans-serif" font-size="16" font-weight="bold">Finite complement matching</text>
<text x="180" y="169" text-anchor="middle" fill="#182a38" font-family="Arial,sans-serif" font-size="14">p ∼ q in a finite algebra</text>
<text x="180" y="187" text-anchor="middle" fill="#182a38" font-family="Arial,sans-serif" font-size="14">⇒ 1 − p ∼ 1 − q</text>
<text x="335" y="202" text-anchor="end" fill="#455c71" font-family="Arial,sans-serif" font-size="12">C06</text>
<path d="M180 210V231" stroke="#455c71" stroke-width="2" marker-end="url(#comparison-mechanism-arrow)"/>
<rect x="12" y="234" width="336" height="84" rx="8" fill="#fff" stroke="#526f87"/>
<text x="180" y="256" text-anchor="middle" fill="#153b56" font-family="Arial,sans-serif" font-size="16" font-weight="bold">Invertibles approximate every x</text>
<text x="180" y="277" text-anchor="middle" fill="#182a38" font-family="Arial,sans-serif" font-size="14">x = u|x|; xε = u(|x| + ε1)</text>
<text x="335" y="310" text-anchor="end" fill="#455c71" font-family="Arial,sans-serif" font-size="12">C07</text>
<path d="M180 318V339" stroke="#455c71" stroke-width="2" marker-end="url(#comparison-mechanism-arrow)"/>
<rect x="12" y="342" width="336" height="84" rx="8" fill="#fff" stroke="#526f87"/>
<text x="180" y="364" text-anchor="middle" fill="#153b56" font-family="Arial,sans-serif" font-size="16" font-weight="bold">Finite matrix corners</text>
<text x="180" y="385" text-anchor="middle" fill="#182a38" font-family="Arial,sans-serif" font-size="14">N finite ⇒ Mn(N) finite</text>
<text x="180" y="403" text-anchor="middle" fill="#182a38" font-family="Arial,sans-serif" font-size="14">by the Schur-complement construction</text>
<text x="335" y="418" text-anchor="end" fill="#455c71" font-family="Arial,sans-serif" font-size="12">C08</text>
<path d="M180 426V447" stroke="#455c71" stroke-width="2" marker-end="url(#comparison-mechanism-arrow)"/>
<rect x="12" y="450" width="336" height="84" rx="8" fill="#fff" stroke="#526f87"/>
<text x="180" y="472" text-anchor="middle" fill="#153b56" font-family="Arial,sans-serif" font-size="16" font-weight="bold">Column embedding on one component</text>
<text x="180" y="493" text-anchor="middle" fill="#182a38" font-family="Arial,sans-serif" font-size="14">a ⟂ b; v*v = a; vv* = r ≤ b</text>
<text x="180" y="511" text-anchor="middle" fill="#182a38" font-family="Arial,sans-serif" font-size="14">T*T = diag(a + b, 0)</text>
<text x="335" y="526" text-anchor="end" fill="#455c71" font-family="Arial,sans-serif" font-size="12">C10</text>
<path d="M180 534V555" stroke="#455c71" stroke-width="2" marker-end="url(#comparison-mechanism-arrow)"/>
<rect x="12" y="558" width="336" height="84" rx="8" fill="#fff" stroke="#526f87"/>
<text x="180" y="580" text-anchor="middle" fill="#153b56" font-family="Arial,sans-serif" font-size="16" font-weight="bold">Finite orthogonal sum</text>
<text x="180" y="601" text-anchor="middle" fill="#182a38" font-family="Arial,sans-serif" font-size="14">TT* ≤ diag(b, b) is finite</text>
<text x="180" y="619" text-anchor="middle" fill="#182a38" font-family="Arial,sans-serif" font-size="14">Patch the two central components</text>
<text x="335" y="634" text-anchor="end" fill="#455c71" font-family="Arial,sans-serif" font-size="12">C09–C10</text>
</svg>


*Figure 1. The exact comparison, complement and matrix-corner route to finite orthogonal sums. The column operator is computed in C10; this is an operator schematic and makes no assertion about finite Hilbert-space dimension. Human proof methods: Peterson, Theorem 5.1.10 and Propositions 5.2.7–5.2.8.*

<a id="c01"></a>
## C01. Strong multiplication, supports and corners

If \(A_i\to A\) and \(B_i\to B\) strongly and \(\sup_i\|A_i\|\le C\), then
\[
\|(A_iB_i-AB)\xi\|
\le C\|(B_i-B)\xi\|+\|(A_i-A)B\xi\|\longrightarrow0.
\]
This is the only strong-product passage used below. Strong convergence of both an operator and its adjoint permits applying this estimate to their products. Norm closure of \(M\) follows from strong closure, so its C*-calculus is available by H00 and F01–F08.

H02 supplies the support \(s(h)\in M\) of a positive \(h\in M\), the projection onto \(\overline{hH}\). For \(x\in M\), T04a supplies
\[
x=v|x|,\qquad |x|=(x^*x)^{1/2},\qquad
v^*v=[\overline{|x|H}],\quad vv^*=[\overline{xH}],\quad v\in M.
\]
Its membership proof is the uniformly bounded strong limit
\(x(|x|+\varepsilon1)^{-1}\to v\). Also
\(\ker |x|=\ker x\), because \(\||x|\xi\|=\|x\xi\|\).

If \(v^*v=p\), then \(v\) vanishes on \((1-p)H\) and is an isometry on \(pH\); its range there is closed. Its range projection is \(vv^*\), and \(v=vp=(vv^*)v\). These facts follow by evaluating \(\|v\xi\|^2=\langle\xi,p\xi\rangle\) and by Hilbert completeness. In particular, if both supports are at most \(e\), then \(v= eve\).

For every projection \(e\in M\), the corner \(eMe\) on \(eH\) is a unital strongly closed self-adjoint algebra with unit \(e\): extend its strong limits by zero on \((1-e)H\) and use strong closure of \(M\). The same applies to \(M_n(M)\) on \(H^{\oplus n}\): a strong operator limit has strongly convergent entries, obtained by coordinate inclusions and projections, so every limiting entry belongs to \(M\). Finite matrices are bounded by the triangle inequality, and H00 gives their C*-norm and completeness. A projection \(e\) is finite in \(M\) exactly when the unit of \(eMe\) is finite, by the support identity above.

<a id="c01b"></a>
For later optional H03 topology statements, the commutant definition also follows directly from these Hilbert inputs. If \(T\in M''\) and \(\xi_1,\ldots,\xi_n\in H\), let \(K\) be the closure of \(\{(x\xi_1,\ldots,x\xi_n):x\in M\}\) in \(H^{\oplus n}\). This set is already a linear subspace because \(M\) is linear. It reduces every diagonal operator from \(M\), so its orthogonal projection has entries in \(M'\). The diagonal operator from \(T\) commutes with those entries and hence with this projection. The tuple \((\xi_1,\ldots,\xi_n)\) belongs to \(K\), since \(1\in M\); therefore its image under \(T\) belongs to \(K\). Finite-vector approximation follows: for any positive error some \(x\in M\) approximates \(T\) on all these vectors. Choosing such \(x\) over finite sets of vectors and decreasing errors constructs a net converging strongly to \(T\). Strong closure gives \(T\in M\). Thus \(M=M''\), proved here without importing a bicommutant or density theorem. Corners, matrices and the center are strongly closed self-adjoint algebras too, so this argument applies to them. H03 consequently supplies their concrete preduals whenever used in the extension.

<a id="c02"></a>
## C02. Arbitrary projection lattice and orthogonal sums

For finitely many projections \(p_1,\ldots,p_m\), their join is
\(s(p_1+\cdots+p_m)\). Indeed a vector is in the kernel of this positive sum exactly when it is in every \(\ker p_i\), because its quadratic value is \(\sum_i\|p_i\xi\|^2\). Thus the support has range \(\overline{p_1H+\cdots+p_mH}\).

For a set-indexed family \((p_i)_{i\in I}\), let \(p_F\) be the join for a finite \(F\subset I\), with \(p_\varnothing=0\). These projections converge strongly to the projection \(P\) onto
\[
L=\overline{\operatorname{span}\bigcup_{i\in I}p_iH}.
\]
They vanish on \(L^\perp\). Every vector in a finite sum of the ranges is fixed eventually; density in \(L\) and the common norm bound one prove convergence on all of \(H\). Strong closure puts \(P\) in \(M\), and its range description makes it the least upper bound \(\bigvee_i p_i\). Meets are
\(\bigwedge_i p_i=1-\bigvee_i(1-p_i)\). Empty joins and meets are respectively zero and one. In particular a meet has range equal to the intersection of the ranges.

If the \(p_i\) are pairwise orthogonal, their finite sums are their finite joins, so
\(\sum_i p_i:=\operatorname{s\!-!lim}_F\sum_{i\in F}p_i=\bigvee_i p_i\).
Every arbitrary sum in this note means this net of finite partial sums, rather than a chosen enumeration.

Now suppose \(v_i\in M\) have pairwise orthogonal initial projections \(p_i=v_i^*v_i\) and pairwise orthogonal final projections \(q_i=v_iv_i^*\). For distinct indices,
\[
v_i^*v_j=v_i^*q_iq_jv_j=0,
\qquad v_iv_j^*=v_ip_ip_jv_j^*=0.
\]
For finite \(F\), \(v_F=\sum_{i\in F}v_i\) therefore satisfies
\[
v_F^*v_F=\sum_{i\in F}p_i,\quad v_Fv_F^*=\sum_{i\in F}q_i,
\qquad \|v_F\|\le1.
\]
For each \(\xi\), the finite sums \(\sum_{i\in F}\|v_i\xi\|^2\) are bounded by \(\|\xi\|^2\). Choose a finite \(F_0\) whose sum is within \(\varepsilon^2\) of their supremum. For finite \(F,G\supseteq F_0\), orthogonality gives
\(\|(v_F-v_G)\xi\|^2\le\sum_{i\notin F_0}\|v_i\xi\|^2\le\varepsilon^2\), where the tail is the supremum of finite tail sums. Consequently \(v_F\) is strong Cauchy; completeness constructs its bounded strong limit \(v\). The same argument for adjoints constructs a strong limit \(w\) of \(v_F^*\). Matrix coefficients give \(w=v^*\). C01 then gives
\[
v^*v=\sum_i p_i,\qquad vv^*=\sum_i q_i,\qquad v\in M.
\tag{C02.1}
\]
This includes empty families, whose sum is zero. It proves both arbitrary orthogonal-sum equivalence and orthogonal additivity of subequivalence: if \(p_i\precsim q_i\) and the two projection families are separately orthogonal, choose implementing partial isometries with final supports \(r_i\le q_i\) and apply (C02.1).

<a id="c03"></a>
## C03. Elementary equivalence and finiteness facts

Equivalence is reflexive (implemented by \(p\)), symmetric (use the adjoint), and transitive: if \(v\) implements \(p\sim q\) and \(w\) implements \(q\sim r\), then \(wv\) implements \(p\sim r\). Subequivalence is transitive by the same product: when \(vv^*\le q=w^*w\), its final support is \(wvv^*w^*\le ww^*\).

For \(r\le p=v^*v\), the restriction \(vr\) implements
\(r\sim vrv^*\le vv^*\). Thus equivalence preserves subprojection comparisons and gives an algebraic *-isomorphism of the two corners, with maps \(a\mapsto vav^*\) and \(b\mapsto v^*bv\).

Finiteness is hereditary. If \(r\le p\) and \(u^*u=r\), \(uu^*\le r\), then \(u+(p-r)\) has initial support \(p\) and final support \(uu^*+(p-r)\le p\); all mixed products vanish because the two initial and final supports are orthogonal. Finiteness of \(p\) forces \(uu^*=r\). Finiteness is also invariant under equivalence, since the displayed corner maps transport an isometry with a proper final support to one in the other corner. It follows that
\[
p\precsim q\text{ and }q\text{ finite}\quad\Longrightarrow\quad p\text{ finite}.
\tag{C03.1}
\]
The zero projection is finite.

<a id="c04"></a>
## C04. Central support and contact between corners

Every element of \(M\) is a linear combination of unitaries. For a self-adjoint contraction \(h\), F06–F08 give a commuting square root \(k=(1-h^2)^{1/2}\); \(h+ik\) is unitary and \(h\) is its real part. Scale arbitrary self-adjoint elements and decompose an arbitrary element into its real and imaginary parts.

For \(p\in\mathcal P(M)\), define
\[
c(p)=\bigvee_{u\in\mathcal U(M)}upu^*.
\]
It belongs to \(M\) by C02. Conjugation by any unitary permutes the ranges defining its join; hence it fixes \(c(p)\). The preceding unitary span makes \(c(p)\) central. It majorizes \(p\), and any central projection majorizing \(p\) majorizes every conjugate and therefore this join. Thus it is the least central projection majorizing \(p\). Its range is
\[
c(p)H=\overline{\operatorname{span}\{xp\xi:x\in M,\ \xi\in H\}},
\tag{C04.1}
\]
because every \(x\) is a finite linear combination of unitaries. This is the precise meaning of \(c(p)=[MpH]\). It includes \(c(0)=0\).

Equivalent projections have the same central support: a central \(z\) with \(zp=p\) also fixes \(q=vpv^*\), and the adjoint argument reverses the implication.

For arbitrary projections,
\[
c(p)c(q)=0\quad\Longleftrightarrow\quad pMq=\{0\}.
\tag{C04.2}
\]
If the central supports are orthogonal, \(pxq=c(p)c(q)pxq=0\). Conversely, if \(pMq=0\), then
\(\langle xp\xi,yq\eta\rangle=\langle\xi,px^*yq\eta\rangle=0\) for all \(x,y,\xi,\eta\). The two closed spans in (C04.1) are orthogonal, proving the forward product is zero.

Moreover \(pMq\ne0\) exactly when \(p\) and \(q\) have nonzero equivalent subprojections. For a nonzero \(x\in pMq\), C01's polar isometry has initial support under \(q\) and nonzero final support under \(p\); reverse it to match in the stated order. Conversely a matching \(v\) from \(p_0\le p\) onto \(q_0\le q\) has nonzero adjoint \(v^*=pv^*q\in pMq\).

<a id="c05"></a>
## C05. General comparison and projection Cantor–Bernstein

Consider sets of triples \((p_i,q_i,v_i)\) with nonzero pairwise orthogonal \(p_i\le p\), nonzero pairwise orthogonal \(q_i\le q\), and \(v_i^*v_i=p_i\), \(v_iv_i^*=q_i\). These sets lie in the fixed set \(\mathcal P(M)\times\mathcal P(M)\times M\) and are ordered by inclusion. The empty set is admissible. A union of a chain is admissible, since every two of its members lie together in one member of that chain. Zorn supplies a maximal matching family. Put
\[
P=\sum_i p_i,\quad Q=\sum_i q_i,\quad v=\sum_i v_i,\qquad
p_0=p-P,\quad q_0=q-Q.
\]
C02 proves all sums exist in \(M\) and \(P\sim Q\) via \(v\). If \(p_0Mq_0\ne0\), C04 supplies a further nonzero matching in these residual projections, contradicting maximality. Hence \(c(p_0)c(q_0)=0\). Take \(z=c(q_0)\). Then \(zp_0=0\), \((1-z)q_0=0\), and central restriction of \(v\) gives
\[
zp=zP\sim zQ\le zq,
\qquad
(1-z)q=(1-z)Q\sim(1-z)P\le(1-z)p.
\tag{C05.1}
\]
Thus, for every pair, there is a central projection \(z\) with \(zp\precsim zq\) and \((1-z)q\precsim(1-z)p\). No countability assumption enters the matching. In a factor \(z\) is zero or one, so any two projections are comparable. Zero projections and empty maximal families are already included.

For completeness, two-sided subequivalence gives equivalence without a finiteness assumption. Suppose \(u^*u=p\), \(uu^*\le q\), \(v^*v=q\), \(vv^*\le p\). Put \(p'=vv^*\), \(p_0=p-p'\), and \(w=vu\). This is an isometry on \(pH\) whose range is under \(p'\). Define
\[
p_n=w^np_0(w^*)^n\quad(n\ge0),\qquad e=\sum_{n\ge0}p_n,\qquad f=ueu^*.
\]
The \(p_n\) are pairwise orthogonal: after cancelling common powers of the isometry, \(p_0\) is perpendicular to the range of every positive power of \(w\), because those ranges are under \(p'\). C02 gives \(e\). Strong multiplication gives
\[
vfv^*=wew^*=e-p_0,
\qquad
v(q-f)v^*=p'-(e-p_0)=p-e.
\]
Therefore \(ue\) matches \(e\) onto \(f\), while \(v^*(p-e)\) matches \(p-e\) onto \(q-f\). Their orthogonal sum implements \(p\sim q\). This also covers \(p_0=0\), when the first sum is zero. Together with (C05.1), it gives the usual factor trichotomy: either equivalence, or strict subequivalence in exactly one direction, where strict means subequivalent but not equivalent.

<a id="c06"></a>
## C06. Complement cancellation inside a finite algebra

Assume now \(M\) is finite, and let \(p\sim q\) via \(v\). Apply C05 to \(1-p\) and \(1-q\). For a central \(z\), choose \(w_1\) with
\[
w_1^*w_1=z(1-p),\qquad w_1w_1^*=r\le z(1-q),
\]
and \(w_2\) with
\[
w_2^*w_2=(1-z)(1-q),\qquad
w_2w_2^*=s\le(1-z)(1-p).
\]
The orthogonal sum \(vz+w_1\) has initial support \(z\) and final support \(zq+r\le z\). Since \(z\le1\) is finite by C03, its final support equals \(z\), forcing \(r=z(1-q)\). Similarly \(v^*(1-z)+w_2\) has initial support \(1-z\), so finiteness forces \(s=(1-z)(1-p)\). Thus
\[
w=w_1+w_2^*,\qquad w^*w=1-p,\quad ww^*=1-q.
\]
Finally \(v+w\) is unitary, and \((v+w)p(v+w)^*=q\). This proves equivalent complements in every finite algebra. It uses finiteness of central subprojections of the already finite unit; it does not use closure of finite projections under sums or joins.

<a id="c07"></a>
## C07. Dense invertibles in a finite algebra

Let \(N\) be any finite concrete algebra as above, with unit \(e\). For \(x\in N\), write \(x=v|x|\) by C01. The two supports of \(v\) are equivalent. C06 extends \(v\) to a unitary \(u\in N\) by matching their complements. Its added part vanishes on the support of \(|x|\), so \(x=u|x|\). For \(\varepsilon>0\),
\[
x_\varepsilon=u(|x|+\varepsilon e)
\]
is invertible, with inverse \((|x|+\varepsilon e)^{-1}u^*\), and
\(\|x_\varepsilon-x\|\le\varepsilon\). The inverse exists by H02 or the continuous reciprocal on the nonnegative spectrum. Hence invertibles are norm dense in \(N\). This includes each nonzero finite corner; zero corners are handled directly.

<a id="c08"></a>
## C08. Finite matrix algebras over a finite algebra

If invertibles are norm dense in a unital Banach algebra \(N\), they are norm dense in every \(M_n(N)\). Here are the needed algebra and estimates. The assertion for \(n=1\) is the hypothesis. For \(n>1\), write
\[
A=\begin{pmatrix}a&r\\ c&D\end{pmatrix},
\]
where \(D\in M_{n-1}(N)\), \(r\) is a row and \(c\) a column. Given \(\varepsilon>0\), choose invertible \(b\in N\) with \(\|b-a\|<\varepsilon/3\). By induction choose invertible \(E\in M_{n-1}(N)\) satisfying
\(\|E-(D-cb^{-1}r)\|<\varepsilon/3\). Then
\[
A'=\begin{pmatrix}b&r\\c&E+cb^{-1}r\end{pmatrix}
=\begin{pmatrix}1&0\\cb^{-1}&1\end{pmatrix}
 \begin{pmatrix}b&0\\0&E\end{pmatrix}
 \begin{pmatrix}1&b^{-1}r\\0&1\end{pmatrix}
\]
is invertible: the triangular factors are inverted by negating their off-diagonal blocks, and the diagonal factor by inverting its blocks. Also \(\|A'-A\|<2\varepsilon/3<\varepsilon\), by the coordinate-block norm bounds. No bound on \(\|b^{-1}\|\) is required; it is fixed before approximating the Schur complement.

A concrete unital C*-algebra with dense invertibles is finite. Indeed, suppose \(V^*V=e\), choose invertible \(A\) with \(\|A-V\|<1\), and observe
\(\|V^*A-e\|<1\). The element \(V^*A\) is invertible: for \(y=e-V^*A\), the series \(\sum_{k\ge0}y^k\) converges by completeness, since its tail is bounded by a geometric tail, and multiplying its partial sums gives an inverse in the limit. Thus \(V^*=(V^*A)A^{-1}\) is invertible. The identity \(V^*V=e\) implies \(V=(V^*)^{-1}\), so \(VV^*=e\).

Applying this to C07 proves
\[
N\text{ finite}\quad\Longrightarrow\quad M_n(N)\text{ finite for every finite }n.
\tag{C08.1}
\]
This is an actual proof of matrix finiteness, rather than a stable-finiteness import. In particular, for a finite projection \(b\in M\), \(\operatorname{diag}(b,b)\) is finite in \(M_2(M)\): its corner is exactly \(M_2(bMb)\), which is finite by (C08.1).

<a id="c09"></a>
## C09. Central patching of finite projections

Let \((p_i)_{i\in I}\) be finite projections with pairwise orthogonal central supports \(z_i=c(p_i)\). Then \(p=\sum_i p_i\) is finite, even if \(I\) is uncountable. Indeed \(z_ip=p_i\). For \(t^*t=p\) and \(tt^*\le p\), centrality gives
\[
(tz_i)^*(tz_i)=p_i,\qquad (tz_i)(tz_i)^*=z_itt^*\le p_i.
\]
Finiteness of \(p_i\) forces \(z_itt^*=p_i\) for every \(i\). Put \(Z=\sum_i z_i\). Since \(p\le Z\) and \(t=ptp\), the range of \(tt^*\) is under \(Z\). Taking the strong limit of the finite sums \(\sum_{i\in F}z_itt^*\) yields \(tt^*=p\), by C01. This includes the empty family.

The same proof applies to projections supported on any prescribed pairwise orthogonal central projections, without requiring those central projections to be their exact central supports. In particular, for a central \(z\), if \(ze\) and \((1-z)e\) are finite, then \(e\) is finite.

The bounded central assembly needed for the homogeneous components also has a direct proof. If \(z_i\) are pairwise orthogonal central projections and \(x_i\in Mz_i\) with \(\sup_i\|x_i\|\le C\), then finite sums \(x_F=\sum_{i\in F}x_i\) have norm at most \(C\), because
\(\|x_F\xi\|^2=\sum_{i\in F}\|x_i z_i\xi\|^2\le C^2\sum_{i\in F}\|z_i\xi\|^2\).
The tail of the last orthogonal square sum tends to zero, so these sums converge strongly to \(x\in M\); the same holds for their adjoints. One has \(z_i x=x_i\) and \(x=(\sum_i z_i)x\), and the preceding bound and restriction to each central summand give
\[
\|x\|=\sup_i\|x_i\|.
\tag{C09.1}
\]
An empty supremum here is zero. In particular arbitrary central orthogonal families of corner unitaries assemble by C02 to a unitary on the sum of their central units. The uniform norm bounds used by averaging survive this exact assembly.

The supremum of any family of finite **central** projections is finite. To see this without assuming directed finite joins, well-order the family \((z_\alpha)\) by ZFC and form
\(d_\alpha=z_\alpha(1-\bigvee_{\beta<\alpha}z_\beta)\). These are pairwise orthogonal central projections, each finite because it is under \(z_\alpha\). Their sum is the original join: by transfinite induction the joins of the two families agree at every initial segment, including limit segments by C02. Apply the central patching argument to the \(d_\alpha\). This assertion concerns central projections; arbitrary infinite orthogonal sums of finite projections need not be finite.

<a id="c10"></a>
## C10. Finite orthogonal sums in an arbitrary algebra

Let \(p,q\in M\) be finite and orthogonal. C05 gives a central \(z\) such that
\(zp\precsim zq\) and \((1-z)q\precsim(1-z)p\).
On the first component put \(a=zp\), \(b=zq\), and choose \(v\) with
\(v^*v=a\), \(vv^*=r\le b\). In \(M_2(M)\), take the concrete column operator
\[
T=\begin{pmatrix}v&0\\b&0\end{pmatrix}.
\]
Because \(a\perp b\) and \(v=va\), \(vb=0\) and \(bv^*=0\). Consequently
\[
T^*T=\begin{pmatrix}a+b&0\\0&0\end{pmatrix},\qquad
TT^*=\begin{pmatrix}r&0\\0&b\end{pmatrix}
\le\begin{pmatrix}b&0\\0&b\end{pmatrix}.
\tag{C10.1}
\]
The last projection is finite by C08, because \(b\le q\) is finite by C03. Hence C03 in \(M_2(M)\) makes \(\operatorname{diag}(a+b,0)\) finite. If \(a+b\) were not finite in \(M\), embedding an isometry of its corner as \(\operatorname{diag}(s,0)\) would contradict that matrix projection's finiteness. Thus \(z(p+q)\) is finite. The second component uses the same column with \(a=(1-z)q\), \(b=(1-z)p\), and gives finiteness of \((1-z)(p+q)\). C09 patches the two components, proving \(p+q\) finite.

Induction proves that every finite orthogonal sum of finite projections is finite. The empty sum is zero, already finite. No assertion about an arbitrary infinite orthogonal sum follows. The logical order is C05 → C06 in an already finite algebra → C07 → C08 → C10 in an arbitrary algebra. In particular C06 does not presuppose C10; there is no finite-sum/complement cycle.

<a id="c11"></a>
## C11. Finite joins and complements of equivalent finite projections

For arbitrary \(p,q\), apply C01 to \(x=(1-p)q\). Its kernel is the orthogonal direct sum
\((1-q)H\oplus(qH\cap pH)\), so its initial support is \(q-p\wedge q\). Its range is contained in \((p\vee q-p)H\). To prove density there, a vector \(\eta\) in that subspace perpendicular to \((1-p)qH\) has \(p\eta=0\) and \(q\eta=0\), so it is perpendicular to both ranges defining \(p\vee q\), and therefore is zero. Thus
\[
p\vee q-p\sim q-p\wedge q.
\tag{C11.1}
\]
If \(p,q\) are finite, the right side is finite by C03, hence so is the left. It is orthogonal to \(p\), and C10 makes their sum \(p\vee q\) finite. Induction gives finite joins of any finite family of finite projections.

If \(p,q\) are finite and equivalent in an arbitrary \(M\), set \(e=p\vee q\). It is finite. C06 in \(eMe\) matches \(e-p\) with \(e-q\); adding the identity on \(1-e\) matches \(1-p\) with \(1-q\). Adding this match to the original \(v\) gives a unitary \(u\in M\) with \(upu^*=q\). This is the stronger arbitrary-ambient form, proved after finite joins. It is kept separate from the earlier finite-ambient C06 used in the noncircular matrix proof.

<a id="c12"></a>
## C12. The exact semifinite projection consequence

If **semifinite** is defined to mean that each nonzero projection contains a nonzero finite projection, this property is a hypothesis. It gives a net of finite projections increasing strongly to one: the set of finite projections is directed by C11's finite join; its join must be one, since a nonzero complementary projection would contain another nonzero finite projection. C02 gives strong convergence of this directed net.

If instead semifinite is defined to mean that \(1=\sum_{i\in I}p_i\) for an orthogonal family of finite projections, the nonzero-corner property follows from C04 and C03. For nonzero \(q\), some \(qp_i\ne0\); otherwise the finite sums converge strongly to one and \(q\) would be zero. Thus \(qMp_i\ne0\), and C04 provides a nonzero subprojection of \(q\) equivalent to a subprojection of \(p_i\), hence finite. Conversely, the nonzero-corner property gives such an orthogonal family by Zorn: a maximal orthogonal family of nonzero finite projections has zero complementary projection. C10 makes each finite partial sum finite, and C02 gives their strong limit one. Both definitions therefore provide the exact SF projection input under either convention, including arbitrary cardinality and the zero algebra.

If the word instead presupposes a faithful normal semifinite **weight**, its equivalence to these projection definitions is a separate weight-theoretic prerequisite and is not proved here. No measure-theoretic finiteness of a weight is substituted for projection finiteness.

## Finite homogeneous components and monic projections

In D04–D10 the ambient algebra is finite. A projection is abelian when its corner is commutative. A nonzero projection is monic when it belongs to a finite orthogonal family of equivalent projections summing to its central support in this ambient algebra.

<a id="d01"></a>
## D01. Finite projection approximants from continuous cutoffs

For a self-adjoint \(h\in eMe\), set
\[
E_t=s((h-te)_+)\le e\qquad(t\in\mathbb R).
\]
The continuous positive part is supplied by F06–F08 and its support by H02. Every \(E_t\) commutes with \(h\) and with every \(E_s\): the resolvent construction of a support commutes with any operator commuting with the supported positive element, and the relevant continuous functions of \(h\) commute. Also \(E_t\le E_s\) for \(s<t\). Indeed \((h-te)_+\le(h-se)_+\) by continuous calculus; a vector in the kernel of the latter has zero quadratic value for the former, hence is in its kernel by H02's positive-form Cauchy–Schwarz argument.

The positive and negative parts of \(h-te\) annihilate each other. The negative part therefore vanishes on the range of \(E_t\), and the positive part vanishes on its complementary range. Consequently
\[
(h-te)E_t\ge0,\qquad (h-te)(e-E_t)\le0.
\tag{D01.1}
\]
Choose \(C>\|h\|\) and a finite grid \(-C=t_0<t_1<\cdots<t_N=C\) with mesh at most \(\delta\). Then \(E_{t_0}=e\), because \(h+Ce\) is positive invertible by F06, and \(E_{t_N}=0\). The differences \(d_k=E_{t_k}-E_{t_{k+1}}\) are mutually orthogonal projections summing to \(e\). They reduce \(h\), and (D01.1) gives
\[
t_kd_k\le hd_k\le t_{k+1}d_k.
\]
Orthogonal decomposition of quadratic forms therefore gives
\[
0\le h-\sum_{k=0}^{N-1}t_kd_k\le\delta e,
\qquad
\left\|h-\sum_{k=0}^{N-1}t_kd_k\right\|\le\delta.
\tag{D01.2}
\]
This proves uniform approximation of every self-adjoint element by finite linear combinations of projections in its corner. If every projection of a corner is central in that corner, then (D01.2), norm closure of the center, and the real/imaginary decomposition show that corner is abelian. Zero corners are included directly.

<a id="d02"></a>
## D02. Abelian projections and their ambient centers

The following facts hold in an arbitrary ambient \(M\), without finiteness. If \(p\) is abelian and \(r\le p\), then
\[
c(r)p=r.
\tag{D02.1}
\]
Indeed \(rM(p-r)=r(pMp)(p-r)=0\) by commutativity. C04 gives \(c(r)c(p-r)=0\), so \(c(r)(p-r)=0\), whereas \(c(r)r=r\).

For a central projection \(z\), one also has
\[
c(zp)=zc(p).
\tag{D02.2}
\]
The right side is a central majorant of \(zp\). If a central projection \(d\) majorizes \(zp\), then \(d\vee(1-z)\) majorizes \(p\); multiplying its majorization of \(c(p)\) by \(z\) gives \(zc(p)\le d\). This proves minimality.

The map
\[
\theta:Z(M)c(p)\longrightarrow pMp,\qquad a\longmapsto ap
\tag{D02.3}
\]
is a unital *-isomorphism. It is a homomorphism because \(a\) is central. If \(ap=0\), then \(a\) annihilates every vector \(xp\xi\), since \(axp\xi=xap\xi=0\); C04's dense range description implies \(ac(p)=0\), hence \(a=0\). Thus F05–F07 make \(\theta\) isometric with closed range. Every projection \(r\le p\) is in that range by (D02.1). D01's finite projection approximants make its range all of \(pMp\).

Abelian projections are finite: an isometry in the commutative corner has \(vv^*=v^*v=p\). Abelianity is hereditary and preserved by equivalence, by C03's corner maps. A sum of abelian projections with mutually orthogonal central supports is abelian. To check the latter, put \(p=\sum_i p_i\) and \(z_i=c(p_i)\). On each \(z_i\), elements of \(pMp\) lie in \(p_iMp_i\) and commute. The strong sum of the \(z_i\) supports \(p\), so taking finite central sums shows that their full commutator is zero.

Two abelian projections with the same central support are equivalent. Apply C05 to \(p,q\) with \(c(p)=c(q)=c\). On a central comparison piece \(z\le c\), suppose \(pz\sim r\le qz\). Then \(c(r)=c(pz)=z\) by equivalence and (D02.2), so (D02.1) for \(q\) gives \(r=c(r)q=qz\). Thus the subequivalence is equivalence on this piece; the reversed piece is treated the same way, and C02 adds them. This also handles zero comparison pieces.

<a id="d03"></a>
## D03. Every type I corner has an abelian projection of full support

Here **type I** means every nonzero projection has a nonzero abelian subprojection. If \(r\ne0\) lies in a type I algebra, choose by Zorn a maximal family of nonzero abelian \(q_i\le r\) whose central supports are mutually orthogonal. Its sum \(q\) is abelian by D02, and
\(c(q)=\bigvee_i c(q_i)\): any central majorant of the sum majorizes each summand and conversely. This equals \(c(r)\). Otherwise the nonzero central projection
\(z=c(r)-\bigvee_i c(q_i)\) has \(rz\ne0\), by minimality of \(c(r)\). Type I supplies a nonzero abelian projection under \(rz\), with central support at most \(z\), contradicting maximality. Thus \(q\le r\) is abelian with \(c(q)=c(r)\). The family need not be countable.

<a id="d04"></a>
## D04. No infinite orthogonal family of equivalent nonzero projections in a finite algebra

If an orthogonal family \((p_i)_{i\in I}\) of nonzero projections in a finite \(M\) is infinite and all its members are equivalent, ZFC selects distinct members \(p_0,p_1,\ldots\). Choose partial isometries matching \(p_n\) onto \(p_{n+1}\). C02's sum has initial projection \(e=\sum_{n\ge0}p_n\) and final projection \(e-p_0<e\). This contradicts finiteness of \(e\le1\) by C03. Consequently every such family is finite. This is an arbitrary-cardinality argument; it does not assume countable decomposition of \(M\).

<a id="d05"></a>
## D05. Finite type I components are centrally homogeneous

Let \(M\) be finite and type I, and choose a nonzero abelian \(p\). A maximal orthogonal family \(p_1,\ldots,p_n\) of projections equivalent to \(p\), containing \(p\), exists by Zorn and is finite by D04. Its members are abelian by D02, each has central support \(c=c(p)\), and their sum \(e\) is at most \(c\).

If the residual \(r=c-e\) had \(c(r)=c\), D03 would give an abelian \(q\le r\) with \(c(q)=c\). D02 would give \(q\sim p\), contradicting maximality. Hence \(c(r)<c\), and
\[
z=c-c(r)>0,\qquad \sum_{i=1}^n zp_i=z.
\tag{D05.1}
\]
The projections \(zp_i\) are abelian, equivalent, and nonzero, since each has central support \(z\) by (D02.2). Thus \(Mz\) is a finite homogeneous component with \(n\) equivalent abelian projections summing to its unit.

Now take a maximal orthogonal family of nonzero central homogeneous components of a finite type I algebra. Its central sum is one: if the complement were nonzero, it would remain finite and type I and the preceding construction would supply another component. This again uses Zorn on a fixed set of projections and their finite implementing families. For each positive integer \(n\), group the components having \(n\) members. Their sum \(z_n\) is central. On that sum, add the first, second, ..., \(n\)-th members of their respective families separately. C02's sums of the matching partial isometries give \(n\) equivalent projections, D02's central sums make them abelian, and their sum is \(z_n\). Consequently
\[
1=\sum_{n\ge1}z_n,
\qquad Mz_n\text{ has }n\text{ equivalent abelian projections summing to }z_n
\tag{D05.2}
\]
for each nonzero \(z_n\). The original collection of components can be uncountable; grouping by \(n\) does not assert a countable central-support family. Uniqueness of the multiplicity labels is not needed or asserted by this existence construction.

<a id="d06"></a>
## D06. Exact matrix-unit realization on a homogeneous piece

Suppose \(p_1,\ldots,p_n\) are equivalent abelian projections summing to a central \(z\). Their common central support is \(z\), because the sum is \(z\). Choose \(v_i\) with \(v_i^*v_i=p_1\), \(v_iv_i^*=p_i\), and \(v_1=p_1\). Then
\(e_{ij}=v_iv_j^*\) satisfy \(e_{ij}^*=e_{ji}\), \(e_{ij}e_{kl}=\delta_{jk}e_{il}\), and \(\sum_i e_{ii}=z\). The maps
\[
Mz\longrightarrow M_n(p_1Mp_1),\quad x\longmapsto[v_i^*xv_j]_{ij},
\qquad
[a_{ij}]\longmapsto\sum_{i,j=1}^n v_i a_{ij}v_j^*
\tag{D06.1}
\]
are mutually inverse unital *-homomorphisms. To verify multiplicativity, insert \(\sum_k v_kv_k^*=z\) between the factors; to verify the inverse, use \(v_j^*v_k=\delta_{jk}p_1\) and \(zxz=x\). All sums are finite, so there is no missing convergence or surjectivity assertion. D02 identifies \(p_1Mp_1\) isometrically with \(Z(M)z\); hence
\[
Mz\cong M_n(Z(M)z).
\tag{D06.2}
\]
F05–F07 give exact norm preservation of these algebraic *-isomorphisms. This is the finite homogeneous matrix identification consumed by the averaging argument. It uses no character theorem, direct-integral classification or representation-independence theorem.

The center of \(Mz\) is exactly \(Z(M)z\), since a central corner element extended by zero commutes with both central pieces of \(M\). At the concrete level the maps in (D06.1) are finite sums of bounded left/right multiplication and therefore are ultraweak continuous by H03's series-vector formulas. The center/corner identification (D02.3) has the following direct bounded weak-operator inverse estimate: approximate vectors of \(zH\) by finite sums \(xp_1\xi\), using C04. For such vectors,
\[
\langle xp_1\xi,a yp_1\eta\rangle
=\langle p_1\xi,(ap_1)(p_1x^*yp_1\eta)\rangle
\qquad(a\in Z(M)z).
\]
Thus bounded weak-operator convergence of \(ap_1\) implies that of \(a\), first on a dense family and then everywhere. H03 turns bounded weak-operator convergence into ultraweak convergence.

Full ultraweak continuity of this specific inverse follows directly as well. H03 constructs a Banach predual \(Q\) for each concrete corner; its canonical image in the full norm dual is isometric by F01's norming-functional theorem, and hence norm closed. Therefore the corner's series-vector functionals are norm closed. Given a vector coefficient \(a\mapsto\langle\xi,a\eta\rangle\) on \(Z(M)z\), replace \(\xi,\eta\in zH\) by finite sums of vectors \(xp_1\alpha\). The preceding coefficient identity expresses each resulting approximant, after applying \(\theta^{-1}\), as a finite sum of vector coefficients on \(p_1Mp_1\). Vector-norm approximation makes the original functionals converge in functional norm. Because \(\theta^{-1}\) is isometric, their transported functionals converge in the same norm, so norm closure makes the transported coefficient normal. For a series-vector functional, first truncate the series, with functional-norm tail bounded by the sum of the products of the vector norms, and then use the same argument. Hence every concrete normal functional composed with \(\theta^{-1}\) is normal, proving ultraweak continuity for this inverse on arbitrary nets. Forward continuity is bounded multiplication by \(p_1\), directly in the series-vector formula. This is a local proved normality statement for (D02.3), rather than a general automatic-normality import. C01's finite-vector argument justifies applying H03 to all the concrete corners and centers involved. Algebraic order and all existing positive suprema are also preserved by the *-isomorphism and its inverse by F08 and the definition of a supremum.

<a id="d07"></a>
## D07. The finite algebra splits into these pieces and a no-abelian piece

In an arbitrary \(M\), let \(z_I\) be the join of all abelian projections. The family is preserved by every unitary conjugation, so C04's unitary-span argument makes \(z_I\) central. If \(0\ne q\le z_I\), then \(qr\ne0\) for some abelian \(r\): otherwise \(q\) would vanish on their joined range and satisfy \(qz_I=0\). C04's polar contact gives a nonzero subprojection of \(q\) equivalent to a subprojection of \(r\), hence abelian by D02. Therefore \(Mz_I\) is type I. Its complement has no nonzero abelian projection by definition.

For finite \(M\), both central pieces are finite by C03. Apply D05–D06 to \(Mz_I\). We obtain arbitrary central homogeneous matrix pieces, grouped as in (D05.2), together with \(M(1-z_I)\), which is finite and has no nonzero abelian projection. This is the finite central decomposition required here. No infinite or general type classification follows from it.

<a id="d08"></a>
## D08. Halving and coherent dyadic partitions on the no-abelian piece

Suppose \(N\) has no nonzero abelian projection. Every nonzero corner \(rNr\) is then nonabelian. D01 implies that some projection \(a\le r\) is not central in that corner. Hence \(aN(r-a)\ne0\): if this corner and its adjoint were zero, then \(a\) would commute with every element of \(rNr\). C04 gives nonzero equivalent subprojections under \(a\) and \(r-a\), which are orthogonal.

For a given projection \(r\), choose by Zorn a maximal family of these equivalent pairs \((a_i,b_i)\) with all the projections in the combined family mutually orthogonal and under \(r\). C02 gives \(A=\sum_i a_i\sim B=\sum_i b_i\). A nonzero residual \(r-A-B\) would yield another pair by the preceding paragraph, so
\[
r=A+B,\qquad A\sim B.
\tag{D08.1}
\]
The zero corner has the zero pair. For a nonzero corner both halves are nonzero.

In a finite \(N\) without nonzero abelian projections, (D08.1) can be iterated coherently. At level \(m\), choose an orthogonal partition \((e_{m,k})_{0\le k<2^m}\) into equivalent projections and matching \(v_{m,k}\) from \(e_{m,0}\) onto \(e_{m,k}\), with the first matching the identity. Halve \(e_{m,0}=f_0+f_1\) by (D08.1), and define
\[
e_{m+1,2k+j}=v_{m,k}f_jv_{m,k}^*\qquad(j=0,1).
\]
These projections remain pairwise orthogonal and equivalent, sum to the unit, and refine the old partition. With
\(P_{k/2^m}=\sum_{i<k}e_{m,i}\), the projections \(P_t\) are well defined for every dyadic \(t\in[0,1]\), increase with \(t\), and satisfy \(P_0=0\), \(P_1=1\). If two dyadic intervals have the same length, refine to a common level; their difference projections are sums of the same number of equivalent cells and are equivalent by C02. Put \(q_m=P_{2^{-m}}=e_{m,0}\). Then
\[
q_m=q_{m+1}+(q_m-q_{m+1}),\qquad q_{m+1}\sim q_m-q_{m+1}.
\tag{D08.2}
\]
Each \(q_m\) is monic, with \(2^m\) equivalent copies summing to one, and has central support one. Central restrictions of these partitions preserve all identities. This constructs the dyadic partitions needed for estimates with \(N=2^m\to\infty\), rather than claiming unspecified equal partitions for all positive integers.

<a id="d09"></a>
## D09. A dyadic central cut fits under every nonzero projection

Let finite \(N\) have no nonzero abelian projection, and let \(p\ne0\). Work on the central support \(c(p)\), and restrict the partitions in D08 to this central unit. There is a nonzero central \(z\le c(p)\) and some \(m\ge0\) such that
\[
q_m z\precsim pz.
\tag{D09.1}
\]
If not, apply C05 to \(q_m c(p)\) and \(p\) for each \(m\). Its first comparison part must be zero: on every nonzero central part \(z\le c(p)\), both \(q_mz\) and \(pz\) are nonzero by their full central supports, so that part would give (D09.1). Consequently \(p\precsim q_m c(p)\) for every \(m\). By (D08.2),
\(p\precsim (q_m-q_{m+1})c(p)\) for every \(m\ge0\). Those annular projections are mutually orthogonal. Choosing a copy of \(p\) under each yields infinitely many mutually orthogonal nonzero equivalent projections, contradicting D04. This proves (D09.1) without a trace-size estimate.

A nonzero subprojection of \(pz\) equivalent to \(q_mz\) is monic: the central cut of the dyadic partition supplies a finite family of equivalent copies summing to \(z\). Equivalence preserves this property. If a partition containing the chosen copy itself is required, C06 extends its equivalence with \(q_mz\) to a unitary, which conjugates the partition and fixes its central sum.

<a id="d10"></a>
## D10. Monic subprojections and arbitrary monic decompositions

On a homogeneous piece with unit \(z\) and abelian cells \(e_1,\ldots,e_n\), every nonzero \(p\le z\) has a nonzero monic subprojection. Since \(c(e_1)=z\), C04 gives a nonzero partial-isometry match from a subprojection \(s\le e_1\) to a subprojection \(r\le p\). Let \(w=c(s)>0\). D02 gives \(s=we_1\), and the central restrictions \(we_i\) are \(n\) equivalent cells summing to \(w\). Thus \(r\sim s\) is monic in the original ambient algebra. C06 extends this equivalence to a unitary of the finite algebra; conjugating the finite partition then makes \(r\) itself one of its cells while retaining the central sum.

For a general finite \(M\), use D07. A nonzero \(p\) has a nonzero central restriction either on a homogeneous piece or on the piece without nonzero abelian projections. The first case uses the preceding paragraph, and the second uses D09. All central units of these components and their further central cuts are central in the original \(M\). Hence every nonzero \(p\) contains a nonzero monic projection relative to \(Z(M)\).

Choose by Zorn a maximal orthogonal family \((r_i)\) of nonzero monic subprojections of \(p\). Its strong sum is \(p\): a nonzero residual would contain another such projection. Empty families cover \(p=0\). Thus every projection in a finite \(M\) is an arbitrary orthogonal sum of monic projections. No countability of this decomposition is asserted.

## The finite spectral cuts used by the constructions

Continuous positive parts and their closed-range supports give every finite cut below. The endpoint conventions are recorded explicitly, so the constructions apply to eigenvalues at the cut endpoints as well.

<a id="s01"></a>
## S01. Strict and non-strict threshold projections

For \(h=h^*\in M\) and \(t\in\mathbb R\), set
\[
 a_t=(h-t1)_+,\qquad b_t=(t1-h)_+,\qquad
 P_t=s(a_t),\qquad Q_t=1-s(b_t),
\]
where \(s(a)\) is the projection onto \(\overline{\operatorname{ran}a}\) supplied by [H02](regular-group-operator-foundations.md#h02). Continuous positive parts give
\[
 h-t1=a_t-b_t,\qquad a_tb_t=b_ta_t=0.
\]
All these operators belong to \(M\). Indeed, continuous functions of \(h\) are norm limits of polynomials. For \(c\ge0\), H02 gives the exact formula
\[
 s(c)=1-\underset{r\to\infty}{\operatorname{s-lim}}(1+rc)^{-1}.
\]
Each inverse belongs to \(M\) by H01. Apply this formula to \(a_t\) and \(b_t\). The algebra is closed under both norm and strong limits.

An operator commuting with \(h\) commutes with \(a_t,b_t\), their resolvents, and their support projections. This follows first for polynomials, then for their norm limits, and finally for the strong limits, since multiplication by a fixed bounded operator preserves strong convergence. Consequently, all the projections \(P_t,Q_t\) commute with \(h\), with each other, and with every operator commuting with \(h\). If \(h\) is central in \(M\), the projections are central in \(M\).

The closed ranges of \(a_t\) and \(b_t\) are orthogonal: for every \(\xi,\eta\in H\),
\[
 \langle a_t\xi,b_t\eta\rangle
 =\langle\xi,a_tb_t\eta\rangle=0.
\]
Thus \(s(a_t)s(b_t)=0\), or \(P_t\le Q_t\). Compression by a commuting projection preserves positivity: if \(c\ge0\) commutes with a projection \(r\), then \(cr=c^{1/2}rc^{1/2}\ge0\). It follows that
\[
 (h-t1)P_t\ge0,\qquad (h-t1)(1-P_t)\le0,
\]
\[
 (h-t1)Q_t\ge0,\qquad (h-t1)(1-Q_t)\le0.
\]
For example, \((h-t1)P_t=a_t\), because \(a_tP_t=a_t\) and \(b_tP_t=0\); on \(1-P_t\), only the non-positive term remains. The corresponding statements for \(Q_t\) follow because \(b_tQ_t=0\).

The projection
\[
 E_t=Q_t-P_t=1-s(a_t)-s(b_t)
\]
is exactly the projection onto \(\ker(h-t1)\). One inclusion follows from \(a_tE_t=b_tE_t=0\). For the other, \((h-t1)\xi=0\) gives \(a_t\xi=b_t\xi\); these two vectors lie in orthogonal ranges, so both vanish. Thus \(P_t\) excludes the eigenspace at \(t\), whereas \(Q_t\) includes it. These are, respectively, the strict cut above \(t\) and the non-strict cut at \(t\).

<a id="s02"></a>
## S02. Nesting and exact interval endpoints

If \(0\le a\le b\), then \(\ker b\subseteq\ker a\). In fact, \(b\xi=0\) gives
\[
 0\le\langle a\xi,\xi\rangle\le\langle b\xi,\xi\rangle=0,
\]
and the positive-form argument in H02 gives \(a\xi=0\). Taking orthogonal complements proves \(s(a)\le s(b)\).

For \(s<t\), the scalar continuous inequalities
\[
 (x-t)_+\le(x-s)_+,\qquad (s-x)_+\le(t-x)_+
\]
pass to \(h\) by F06–F08. Therefore
\[
 P_t\le P_s,\qquad Q_t\le Q_s.
\]
There is also the mixed inequality \(Q_t\le P_s\). To prove it, form the commuting projection \(r=Q_t(1-P_s)\). S01 gives
\[
 tr\le hr\le sr.
\]
Hence \((t-s)r\le0\). Since \(t-s>0\) and \(r\ge0\), this implies \(r=0\), as required.

For \(s<t\), the following differences are therefore projections:

| Interval | Projection |
| --- | --- |
| \([s,t)\) | \(Q_s-Q_t\) |
| \((s,t]\) | \(P_s-P_t\) |
| \((s,t)\) | \(P_s-Q_t\) |
| \([s,t]\) | \(Q_s-P_t\) |

Each commutes with \(h\), and on each projection \(r\) the inequalities \(sr\le hr\le tr\) hold. The endpoint conventions are exact. The eigenspace projection \(E_s\) lies in \(Q_s\), is orthogonal to \(P_s\), and is orthogonal to \(Q_t\) and \(P_t\). The projection \(E_t\) lies in \(Q_t\) and \(P_s\), and is orthogonal to \(P_t\). These relations prove the indicated inclusion or exclusion of each endpoint. At coincident endpoints the empty intervals have projection zero, while \([s,s]\) has projection \(E_s\). The displayed formulas for open intervals are asserted only when \(s<t\).

We may consequently write \(1_{[s,t)}(h)=Q_s-Q_t\) for this particular finite construction. This notation requires only continuous positive parts and their closed-range supports.

<a id="s03"></a>
## S03. Uniform approximation by finitely many projections

Every bounded selfadjoint \(h\in M\) is a norm limit of finite real linear combinations of mutually orthogonal projections in \(M\) commuting with \(h\). If \(h=0\), the single combination \(0\cdot1\) suffices. Otherwise put \(R=\|h\|>0\). For a positive integer \(m\), let
\[
 t_j=-R+\frac{2Rj}{m}\quad(0\le j\le m),
 \qquad \Delta=\frac{2R}{m}.
\]
The norm and order conclusions of F06–F08 give \(-R1\le h\le R1\), so \(Q_{-R}=1\), \(P_R=0\), and \(Q_R=E_R\). Define
\[
 p_j=Q_{t_j}-Q_{t_{j+1}}\quad(0\le j<m),
 \qquad p_m=Q_R.
\]
S02 and telescoping show that these projections are mutually orthogonal and sum to \(1\). They all commute with \(h\). Their bounds are
\[
 t_jp_j\le hp_j\le t_{j+1}p_j\quad(0\le j<m),
 \qquad hp_m=Rp_m.
\]
The last equality follows from \(p_m=E_R\). Thus the upper endpoint, which the half-open intervals exclude, is retained as its own projection.

Set
\[
 h_m=\sum_{j=0}^{m-1}t_jp_j+Rp_m.
\]
On each of the first \(m\) pieces, \(0\le(h-h_m)p_j\le\Delta p_j\), and on the last piece the difference is zero. Addition gives
\[
 0\le h-h_m\le\Delta\sum_{j=0}^{m-1}p_j\le\Delta1.
\]
The norm bound for positive operators in F08 now gives
\[
 \|h-h_m\|\le\frac{2\|h\|}{m}.
\]
In particular, \(m>2\|h\|/\varepsilon\) gives an approximation with error strictly less than \(\varepsilon\). Zero pieces may be omitted. The argument works in arbitrary Hilbert-space dimension and introduces no countable spectral resolution.

For a positive element the approximants can themselves be chosen positive. If \(h\ge0\) and \(R=\|h\|>0\), instead use \(t_j=Rj/m\), \(0\le j\le m\). Now \(Q_0=1\) and \(Q_R=E_R\); the same differences \(p_j=Q_{t_j}-Q_{t_{j+1}}\) and top projection \(p_m=Q_R\) sum to one. Their coefficients \(t_j\) and \(R\) are nonnegative, and the same interval bounds give
\[
0\le h_m=\sum_{j<m}t_jp_j+Rp_m\le h,
\qquad 0\le h-h_m\le\frac Rm1.
\]
The zero positive element uses the zero sum. Thus every positive element is a norm limit of positive finite projection sums, the precise form used by LC and CT.


<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="finite-cuts-title" data-diagram="finite-cuts" xmlns:xlink="http://www.w3.org/1999/xlink" width="778" height="547" viewBox="0 0 777.6 547.2" version="1.1">
<title id="finite-cuts-title">Strict threshold endpoints and the finite lower-step approximation</title>
 
 <defs>
  <style type="text/css">*{stroke-linejoin: round; stroke-linecap: butt}</style>
 </defs>
 <g id="figure_1">
  <g id="patch_1">
   <path d="M 0 547.2 
L 777.6 547.2 
L 777.6 0 
L 0 0 
z
" style="fill: #ffffff"/>
  </g>
  <g id="axes_1">
   <g id="patch_2">
    <path d="M 171.072 182.7648 
L 750.384 182.7648 
L 750.384 38.304 
L 171.072 38.304 
z
" style="fill: #ffffff"/>
   </g>
   <g id="matplotlib.axis_1">
    <g id="xtick_1">
     <g id="line2d_1">
      <defs>
       <path id="m14f956db99" d="M 0 0 
L 0 3.5 
" style="stroke: #000000; stroke-width: 0.8"/>
      </defs>
      <g>
       <use xlink:href="#m14f956db99" x="257.108436" y="182.7648" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_1">
      <!-- $s$ -->
      <g transform="translate(254.458436 197.363237) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-Oblique-73" d="M 3200 3397 
L 3091 2853 
Q 2863 2978 2609 3040 
Q 2356 3103 2088 3103 
Q 1634 3103 1373 2948 
Q 1113 2794 1113 2528 
Q 1113 2219 1719 2053 
Q 1766 2041 1788 2034 
L 1972 1978 
Q 2547 1819 2739 1644 
Q 2931 1469 2931 1166 
Q 2931 609 2489 259 
Q 2047 -91 1331 -91 
Q 1053 -91 747 -37 
Q 441 16 72 128 
L 184 722 
Q 500 559 806 475 
Q 1113 391 1394 391 
Q 1816 391 2080 572 
Q 2344 753 2344 1031 
Q 2344 1331 1650 1516 
L 1591 1531 
L 1394 1581 
Q 956 1697 753 1886 
Q 550 2075 550 2369 
Q 550 2928 970 3256 
Q 1391 3584 2113 3584 
Q 2397 3584 2667 3537 
Q 2938 3491 3200 3397 
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-Oblique-73"/>
      </g>
     </g>
    </g>
    <g id="xtick_2">
     <g id="line2d_2">
      <g>
       <use xlink:href="#m14f956db99" x="543.896554" y="182.7648" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_2">
      <!-- $t$ -->
      <g transform="translate(541.896554 197.363237) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-Oblique-74" d="M 2706 3500 
L 2619 3053 
L 1472 3053 
L 1100 1153 
Q 1081 1047 1072 975 
Q 1063 903 1063 863 
Q 1063 663 1183 572 
Q 1303 481 1569 481 
L 2150 481 
L 2053 0 
L 1503 0 
Q 991 0 739 200 
Q 488 400 488 806 
Q 488 878 497 964 
Q 506 1050 525 1153 
L 897 3053 
L 409 3053 
L 500 3500 
L 978 3500 
L 1172 4494 
L 1747 4494 
L 1556 3500 
L 2706 3500 
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-Oblique-74" transform="translate(0 0.78125)"/>
      </g>
     </g>
    </g>
   </g>
   <g id="matplotlib.axis_2"/>
   <g id="LineCollection_1">
    <path d="M 188.279287 54.761559 
L 736.044594 54.761559 
" clip-path="url(#pd88586373a)" style="fill: none; stroke: #d9dde2"/>
   </g>
   <g id="LineCollection_2">
    <path d="M 257.108436 54.761559 
L 721.705188 54.761559 
" clip-path="url(#pd88586373a)" style="fill: none; stroke: #205ca8; stroke-width: 4"/>
   </g>
   <g id="LineCollection_3">
    <path d="M 188.279287 91.333914 
L 736.044594 91.333914 
" clip-path="url(#pd88586373a)" style="fill: none; stroke: #d9dde2"/>
   </g>
   <g id="LineCollection_4">
    <path d="M 257.108436 91.333914 
L 721.705188 91.333914 
" clip-path="url(#pd88586373a)" style="fill: none; stroke: #205ca8; stroke-width: 4"/>
   </g>
   <g id="LineCollection_5">
    <path d="M 188.279287 127.906268 
L 736.044594 127.906268 
" clip-path="url(#pd88586373a)" style="fill: none; stroke: #d9dde2"/>
   </g>
   <g id="LineCollection_6">
    <path d="M 257.108436 127.906268 
L 543.896554 127.906268 
" clip-path="url(#pd88586373a)" style="fill: none; stroke: #205ca8; stroke-width: 4"/>
   </g>
   <g id="LineCollection_7">
    <path d="M 188.279287 164.478623 
L 736.044594 164.478623 
" clip-path="url(#pd88586373a)" style="fill: none; stroke: #d9dde2"/>
   </g>
   <g id="patch_3">
    <path d="M 171.072 182.7648 
L 750.384 182.7648 
" style="fill: none; stroke: #697684; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="patch_4">
    <path d="M 674.950183 54.761559 
Q 701.631065 54.761559 726.075879 54.761559 
" style="fill: none; stroke: #205ca8; stroke-width: 2; stroke-linecap: round"/>
    <path d="M 722.075879 52.761559 
L 726.075879 54.761559 
L 722.075879 56.761559 
" style="fill: none; stroke: #205ca8; stroke-width: 2; stroke-linecap: round"/>
   </g>
   <g id="text_3">
    <!-- $P_s=\operatorname{supp}((h-s1)_+)$ -->
    <g transform="translate(61.839119 57.649059) scale(0.105 -0.105)">
     <defs>
      <path id="DejaVuSans-Oblique-50" d="M 1081 4666 
L 2541 4666 
Q 3178 4666 3512 4369 
Q 3847 4072 3847 3500 
Q 3847 2731 3353 2303 
Q 2859 1875 1966 1875 
L 1172 1875 
L 806 0 
L 172 0 
L 1081 4666 
z
M 1613 4147 
L 1275 2394 
L 2069 2394 
Q 2606 2394 2893 2669 
Q 3181 2944 3181 3456 
Q 3181 3784 2986 3965 
Q 2791 4147 2438 4147 
L 1613 4147 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-3d" d="M 678 2906 
L 4684 2906 
L 4684 2381 
L 678 2381 
L 678 2906 
z
M 678 1631 
L 4684 1631 
L 4684 1100 
L 678 1100 
L 678 1631 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-73" d="M 2834 3397 
L 2834 2853 
Q 2591 2978 2328 3040 
Q 2066 3103 1784 3103 
Q 1356 3103 1142 2972 
Q 928 2841 928 2578 
Q 928 2378 1081 2264 
Q 1234 2150 1697 2047 
L 1894 2003 
Q 2506 1872 2764 1633 
Q 3022 1394 3022 966 
Q 3022 478 2636 193 
Q 2250 -91 1575 -91 
Q 1294 -91 989 -36 
Q 684 19 347 128 
L 347 722 
Q 666 556 975 473 
Q 1284 391 1588 391 
Q 1994 391 2212 530 
Q 2431 669 2431 922 
Q 2431 1156 2273 1281 
Q 2116 1406 1581 1522 
L 1381 1569 
Q 847 1681 609 1914 
Q 372 2147 372 2553 
Q 372 3047 722 3315 
Q 1072 3584 1716 3584 
Q 2034 3584 2315 3537 
Q 2597 3491 2834 3397 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-75" d="M 544 1381 
L 544 3500 
L 1119 3500 
L 1119 1403 
Q 1119 906 1312 657 
Q 1506 409 1894 409 
Q 2359 409 2629 706 
Q 2900 1003 2900 1516 
L 2900 3500 
L 3475 3500 
L 3475 0 
L 2900 0 
L 2900 538 
Q 2691 219 2414 64 
Q 2138 -91 1772 -91 
Q 1169 -91 856 284 
Q 544 659 544 1381 
z
M 1991 3584 
L 1991 3584 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-70" d="M 1159 525 
L 1159 -1331 
L 581 -1331 
L 581 3500 
L 1159 3500 
L 1159 2969 
Q 1341 3281 1617 3432 
Q 1894 3584 2278 3584 
Q 2916 3584 3314 3078 
Q 3713 2572 3713 1747 
Q 3713 922 3314 415 
Q 2916 -91 2278 -91 
Q 1894 -91 1617 61 
Q 1341 213 1159 525 
z
M 3116 1747 
Q 3116 2381 2855 2742 
Q 2594 3103 2138 3103 
Q 1681 3103 1420 2742 
Q 1159 2381 1159 1747 
Q 1159 1113 1420 752 
Q 1681 391 2138 391 
Q 2594 391 2855 752 
Q 3116 1113 3116 1747 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-28" d="M 1984 4856 
Q 1566 4138 1362 3434 
Q 1159 2731 1159 2009 
Q 1159 1288 1364 580 
Q 1569 -128 1984 -844 
L 1484 -844 
Q 1016 -109 783 600 
Q 550 1309 550 2009 
Q 550 2706 781 3412 
Q 1013 4119 1484 4856 
L 1984 4856 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-Oblique-68" d="M 3566 2113 
L 3156 0 
L 2578 0 
L 2988 2091 
Q 3016 2238 3031 2350 
Q 3047 2463 3047 2528 
Q 3047 2791 2881 2937 
Q 2716 3084 2419 3084 
Q 1956 3084 1617 2771 
Q 1278 2459 1178 1941 
L 800 0 
L 225 0 
L 1172 4863 
L 1747 4863 
L 1375 2950 
Q 1594 3244 1934 3414 
Q 2275 3584 2650 3584 
Q 3113 3584 3367 3334 
Q 3622 3084 3622 2631 
Q 3622 2519 3608 2391 
Q 3594 2263 3566 2113 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-2212" d="M 678 2272 
L 4684 2272 
L 4684 1741 
L 678 1741 
L 678 2272 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-31" d="M 794 531 
L 1825 531 
L 1825 4091 
L 703 3866 
L 703 4441 
L 1819 4666 
L 2450 4666 
L 2450 531 
L 3481 531 
L 3481 0 
L 794 0 
L 794 531 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-29" d="M 513 4856 
L 1013 4856 
Q 1481 4119 1714 3412 
Q 1947 2706 1947 2009 
Q 1947 1309 1714 600 
Q 1481 -109 1013 -844 
L 513 -844 
Q 928 -128 1133 580 
Q 1338 1288 1338 2009 
Q 1338 2731 1133 3434 
Q 928 4138 513 4856 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-2b" d="M 2944 4013 
L 2944 2272 
L 4684 2272 
L 4684 1741 
L 2944 1741 
L 2944 0 
L 2419 0 
L 2419 1741 
L 678 1741 
L 678 2272 
L 2419 2272 
L 2419 4013 
L 2944 4013 
z
" transform="scale(0.015625)"/>
     </defs>
     <use xlink:href="#DejaVuSans-Oblique-50" transform="translate(0 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-73" transform="translate(60.302734 -16.390625) scale(0.7)"/>
     <use xlink:href="#DejaVuSans-3d" transform="translate(118.989258 0.015625)"/>
     <use xlink:href="#DejaVuSans-73" transform="translate(222.260742 0.015625)"/>
     <use xlink:href="#DejaVuSans-75" transform="translate(274.360352 0.015625)"/>
     <use xlink:href="#DejaVuSans-70" transform="translate(337.739258 0.015625)"/>
     <use xlink:href="#DejaVuSans-70" transform="translate(401.21582 0.015625)"/>
     <use xlink:href="#DejaVuSans-28" transform="translate(464.692383 0.015625)"/>
     <use xlink:href="#DejaVuSans-28" transform="translate(503.706055 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-68" transform="translate(542.719727 0.015625)"/>
     <use xlink:href="#DejaVuSans-2212" transform="translate(625.581055 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-73" transform="translate(728.852539 0.015625)"/>
     <use xlink:href="#DejaVuSans-31" transform="translate(780.952148 0.015625)"/>
     <use xlink:href="#DejaVuSans-29" transform="translate(844.575195 0.015625)"/>
     <use xlink:href="#DejaVuSans-2b" transform="translate(898.183594 -16.390625) scale(0.7)"/>
     <use xlink:href="#DejaVuSans-29" transform="translate(973.208008 0.015625)"/>
    </g>
   </g>
   <g id="patch_5">
    <path d="M 674.950183 91.333914 
Q 701.631065 91.333914 726.075879 91.333914 
" style="fill: none; stroke: #205ca8; stroke-width: 2; stroke-linecap: round"/>
    <path d="M 722.075879 89.333914 
L 726.075879 91.333914 
L 722.075879 93.333914 
" style="fill: none; stroke: #205ca8; stroke-width: 2; stroke-linecap: round"/>
   </g>
   <g id="text_4">
    <!-- $Q_s=1-\operatorname{supp}((s1-h)_+)$ -->
    <g transform="translate(40.314119 94.221414) scale(0.105 -0.105)">
     <defs>
      <path id="DejaVuSans-Oblique-51" d="M 2309 -84 
Q 2275 -88 2237 -89 
Q 2200 -91 2125 -91 
Q 1250 -91 756 411 
Q 263 913 263 1797 
Q 263 2319 452 2844 
Q 641 3369 978 3788 
Q 1369 4269 1858 4509 
Q 2347 4750 2938 4750 
Q 3794 4750 4287 4245 
Q 4781 3741 4781 2869 
Q 4781 1928 4265 1147 
Q 3750 366 2919 44 
L 3553 -825 
L 2847 -825 
L 2309 -84 
z
M 2919 4238 
Q 2400 4238 2003 3986 
Q 1606 3734 1313 3219 
Q 1125 2891 1026 2522 
Q 928 2153 928 1778 
Q 928 1128 1239 775 
Q 1550 422 2119 422 
Q 2631 422 3032 676 
Q 3434 931 3719 1434 
Q 3909 1772 4009 2142 
Q 4109 2513 4109 2881 
Q 4109 3528 3796 3883 
Q 3484 4238 2919 4238 
z
" transform="scale(0.015625)"/>
     </defs>
     <use xlink:href="#DejaVuSans-Oblique-51" transform="translate(0 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-73" transform="translate(78.710938 -16.390625) scale(0.7)"/>
     <use xlink:href="#DejaVuSans-3d" transform="translate(137.397461 0.015625)"/>
     <use xlink:href="#DejaVuSans-31" transform="translate(240.668945 0.015625)"/>
     <use xlink:href="#DejaVuSans-2212" transform="translate(323.774414 0.015625)"/>
     <use xlink:href="#DejaVuSans-73" transform="translate(427.045898 0.015625)"/>
     <use xlink:href="#DejaVuSans-75" transform="translate(479.145508 0.015625)"/>
     <use xlink:href="#DejaVuSans-70" transform="translate(542.524414 0.015625)"/>
     <use xlink:href="#DejaVuSans-70" transform="translate(606.000977 0.015625)"/>
     <use xlink:href="#DejaVuSans-28" transform="translate(669.477539 0.015625)"/>
     <use xlink:href="#DejaVuSans-28" transform="translate(708.491211 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-73" transform="translate(747.504883 0.015625)"/>
     <use xlink:href="#DejaVuSans-31" transform="translate(799.604492 0.015625)"/>
     <use xlink:href="#DejaVuSans-2212" transform="translate(882.709961 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-68" transform="translate(985.981445 0.015625)"/>
     <use xlink:href="#DejaVuSans-29" transform="translate(1049.360352 0.015625)"/>
     <use xlink:href="#DejaVuSans-2b" transform="translate(1102.96875 -16.390625) scale(0.7)"/>
     <use xlink:href="#DejaVuSans-29" transform="translate(1177.993164 0.015625)"/>
    </g>
   </g>
   <g id="text_5">
    <!-- $Q_s-Q_t:\ s,t)$ -->
    <g transform="translate(97.224119 130.803612) scale(0.105 -0.105)">
     <defs>
      <path id="DejaVuSans-3a" d="M 750 794 
L 1409 794 
L 1409 0 
L 750 0 
L 750 794 
z
M 750 3309 
L 1409 3309 
L 1409 2516 
L 750 2516 
L 750 3309 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-5b" d="M 550 4863 
L 1875 4863 
L 1875 4416 
L 1125 4416 
L 1125 -397 
L 1875 -397 
L 1875 -844 
L 550 -844 
L 550 4863 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-2c" d="M 750 794 
L 1409 794 
L 1409 256 
L 897 -744 
L 494 -744 
L 750 256 
L 750 794 
z
" transform="scale(0.015625)"/>
     </defs>
     <use xlink:href="#DejaVuSans-Oblique-51" transform="translate(0 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-73" transform="translate(78.710938 -16.390625) scale(0.7)"/>
     <use xlink:href="#DejaVuSans-2212" transform="translate(137.397461 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-51" transform="translate(240.668945 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-74" transform="translate(319.379883 -16.390625) scale(0.7)"/>
     <use xlink:href="#DejaVuSans-3a" transform="translate(369.042969 0.015625)"/>
     <use xlink:href="#DejaVuSans-5b" transform="translate(454.687175 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-73" transform="translate(493.700847 0.015625)"/>
     <use xlink:href="#DejaVuSans-2c" transform="translate(545.800457 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-74" transform="translate(597.069988 0.015625)"/>
     <use xlink:href="#DejaVuSans-29" transform="translate(636.278972 0.015625)"/>
    </g>
   </g>
   <g id="text_6">
    <!-- $E_t=Q_t-P_t:\ \{t\}$ -->
    <g transform="translate(83.154119 167.375967) scale(0.105 -0.105)">
     <defs>
      <path id="DejaVuSans-Oblique-45" d="M 1081 4666 
L 4031 4666 
L 3928 4134 
L 1606 4134 
L 1338 2753 
L 3566 2753 
L 3463 2222 
L 1234 2222 
L 909 531 
L 3284 531 
L 3181 0 
L 172 0 
L 1081 4666 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-7b" d="M 3272 -594 
L 3272 -1044 
L 3078 -1044 
Q 2300 -1044 2036 -812 
Q 1772 -581 1772 109 
L 1772 856 
Q 1772 1328 1603 1509 
Q 1434 1691 991 1691 
L 800 1691 
L 800 2138 
L 991 2138 
Q 1438 2138 1605 2317 
Q 1772 2497 1772 2963 
L 1772 3713 
Q 1772 4403 2036 4633 
Q 2300 4863 3078 4863 
L 3272 4863 
L 3272 4416 
L 3059 4416 
Q 2619 4416 2484 4278 
Q 2350 4141 2350 3700 
L 2350 2925 
Q 2350 2434 2208 2212 
Q 2066 1991 1722 1913 
Q 2069 1828 2209 1606 
Q 2350 1384 2350 897 
L 2350 122 
Q 2350 -319 2484 -456 
Q 2619 -594 3059 -594 
L 3272 -594 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-7d" d="M 800 -594 
L 1019 -594 
Q 1456 -594 1589 -459 
Q 1722 -325 1722 122 
L 1722 897 
Q 1722 1384 1862 1606 
Q 2003 1828 2350 1913 
Q 2003 1991 1862 2212 
Q 1722 2434 1722 2925 
L 1722 3700 
Q 1722 4144 1589 4280 
Q 1456 4416 1019 4416 
L 800 4416 
L 800 4863 
L 997 4863 
Q 1775 4863 2036 4633 
Q 2297 4403 2297 3713 
L 2297 2963 
Q 2297 2497 2465 2317 
Q 2634 2138 3078 2138 
L 3272 2138 
L 3272 1691 
L 3078 1691 
Q 2634 1691 2465 1509 
Q 2297 1328 2297 856 
L 2297 109 
Q 2297 -581 2036 -812 
Q 1775 -1044 997 -1044 
L 800 -1044 
L 800 -594 
z
" transform="scale(0.015625)"/>
     </defs>
     <use xlink:href="#DejaVuSans-Oblique-45" transform="translate(0 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-74" transform="translate(63.183594 -16.390625) scale(0.7)"/>
     <use xlink:href="#DejaVuSans-3d" transform="translate(112.84668 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-51" transform="translate(216.118164 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-74" transform="translate(294.829102 -16.390625) scale(0.7)"/>
     <use xlink:href="#DejaVuSans-2212" transform="translate(344.492188 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-50" transform="translate(447.763672 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-74" transform="translate(508.066406 -16.390625) scale(0.7)"/>
     <use xlink:href="#DejaVuSans-3a" transform="translate(557.729492 0.015625)"/>
     <use xlink:href="#DejaVuSans-7b" transform="translate(643.373699 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-74" transform="translate(706.996746 0.015625)"/>
     <use xlink:href="#DejaVuSans-7d" transform="translate(746.20573 0.015625)"/>
    </g>
   </g>
   <g id="text_7">
    <!-- Strict and non-strict cuts retain different endpoint eigenspaces -->
    <g transform="translate(256.028781 24.304) scale(0.13 -0.13)">
     <defs>
      <path id="DejaVuSans-53" d="M 3425 4513 
L 3425 3897 
Q 3066 4069 2747 4153 
Q 2428 4238 2131 4238 
Q 1616 4238 1336 4038 
Q 1056 3838 1056 3469 
Q 1056 3159 1242 3001 
Q 1428 2844 1947 2747 
L 2328 2669 
Q 3034 2534 3370 2195 
Q 3706 1856 3706 1288 
Q 3706 609 3251 259 
Q 2797 -91 1919 -91 
Q 1588 -91 1214 -16 
Q 841 59 441 206 
L 441 856 
Q 825 641 1194 531 
Q 1563 422 1919 422 
Q 2459 422 2753 634 
Q 3047 847 3047 1241 
Q 3047 1584 2836 1778 
Q 2625 1972 2144 2069 
L 1759 2144 
Q 1053 2284 737 2584 
Q 422 2884 422 3419 
Q 422 4038 858 4394 
Q 1294 4750 2059 4750 
Q 2388 4750 2728 4690 
Q 3069 4631 3425 4513 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-74" d="M 1172 4494 
L 1172 3500 
L 2356 3500 
L 2356 3053 
L 1172 3053 
L 1172 1153 
Q 1172 725 1289 603 
Q 1406 481 1766 481 
L 2356 481 
L 2356 0 
L 1766 0 
Q 1100 0 847 248 
Q 594 497 594 1153 
L 594 3053 
L 172 3053 
L 172 3500 
L 594 3500 
L 594 4494 
L 1172 4494 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-72" d="M 2631 2963 
Q 2534 3019 2420 3045 
Q 2306 3072 2169 3072 
Q 1681 3072 1420 2755 
Q 1159 2438 1159 1844 
L 1159 0 
L 581 0 
L 581 3500 
L 1159 3500 
L 1159 2956 
Q 1341 3275 1631 3429 
Q 1922 3584 2338 3584 
Q 2397 3584 2469 3576 
Q 2541 3569 2628 3553 
L 2631 2963 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-69" d="M 603 3500 
L 1178 3500 
L 1178 0 
L 603 0 
L 603 3500 
z
M 603 4863 
L 1178 4863 
L 1178 4134 
L 603 4134 
L 603 4863 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-63" d="M 3122 3366 
L 3122 2828 
Q 2878 2963 2633 3030 
Q 2388 3097 2138 3097 
Q 1578 3097 1268 2742 
Q 959 2388 959 1747 
Q 959 1106 1268 751 
Q 1578 397 2138 397 
Q 2388 397 2633 464 
Q 2878 531 3122 666 
L 3122 134 
Q 2881 22 2623 -34 
Q 2366 -91 2075 -91 
Q 1284 -91 818 406 
Q 353 903 353 1747 
Q 353 2603 823 3093 
Q 1294 3584 2113 3584 
Q 2378 3584 2631 3529 
Q 2884 3475 3122 3366 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-20" transform="scale(0.015625)"/>
      <path id="DejaVuSans-61" d="M 2194 1759 
Q 1497 1759 1228 1600 
Q 959 1441 959 1056 
Q 959 750 1161 570 
Q 1363 391 1709 391 
Q 2188 391 2477 730 
Q 2766 1069 2766 1631 
L 2766 1759 
L 2194 1759 
z
M 3341 1997 
L 3341 0 
L 2766 0 
L 2766 531 
Q 2569 213 2275 61 
Q 1981 -91 1556 -91 
Q 1019 -91 701 211 
Q 384 513 384 1019 
Q 384 1609 779 1909 
Q 1175 2209 1959 2209 
L 2766 2209 
L 2766 2266 
Q 2766 2663 2505 2880 
Q 2244 3097 1772 3097 
Q 1472 3097 1187 3025 
Q 903 2953 641 2809 
L 641 3341 
Q 956 3463 1253 3523 
Q 1550 3584 1831 3584 
Q 2591 3584 2966 3190 
Q 3341 2797 3341 1997 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-6e" d="M 3513 2113 
L 3513 0 
L 2938 0 
L 2938 2094 
Q 2938 2591 2744 2837 
Q 2550 3084 2163 3084 
Q 1697 3084 1428 2787 
Q 1159 2491 1159 1978 
L 1159 0 
L 581 0 
L 581 3500 
L 1159 3500 
L 1159 2956 
Q 1366 3272 1645 3428 
Q 1925 3584 2291 3584 
Q 2894 3584 3203 3211 
Q 3513 2838 3513 2113 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-64" d="M 2906 2969 
L 2906 4863 
L 3481 4863 
L 3481 0 
L 2906 0 
L 2906 525 
Q 2725 213 2448 61 
Q 2172 -91 1784 -91 
Q 1150 -91 751 415 
Q 353 922 353 1747 
Q 353 2572 751 3078 
Q 1150 3584 1784 3584 
Q 2172 3584 2448 3432 
Q 2725 3281 2906 2969 
z
M 947 1747 
Q 947 1113 1208 752 
Q 1469 391 1925 391 
Q 2381 391 2643 752 
Q 2906 1113 2906 1747 
Q 2906 2381 2643 2742 
Q 2381 3103 1925 3103 
Q 1469 3103 1208 2742 
Q 947 2381 947 1747 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-6f" d="M 1959 3097 
Q 1497 3097 1228 2736 
Q 959 2375 959 1747 
Q 959 1119 1226 758 
Q 1494 397 1959 397 
Q 2419 397 2687 759 
Q 2956 1122 2956 1747 
Q 2956 2369 2687 2733 
Q 2419 3097 1959 3097 
z
M 1959 3584 
Q 2709 3584 3137 3096 
Q 3566 2609 3566 1747 
Q 3566 888 3137 398 
Q 2709 -91 1959 -91 
Q 1206 -91 779 398 
Q 353 888 353 1747 
Q 353 2609 779 3096 
Q 1206 3584 1959 3584 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-2d" d="M 313 2009 
L 1997 2009 
L 1997 1497 
L 313 1497 
L 313 2009 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-65" d="M 3597 1894 
L 3597 1613 
L 953 1613 
Q 991 1019 1311 708 
Q 1631 397 2203 397 
Q 2534 397 2845 478 
Q 3156 559 3463 722 
L 3463 178 
Q 3153 47 2828 -22 
Q 2503 -91 2169 -91 
Q 1331 -91 842 396 
Q 353 884 353 1716 
Q 353 2575 817 3079 
Q 1281 3584 2069 3584 
Q 2775 3584 3186 3129 
Q 3597 2675 3597 1894 
z
M 3022 2063 
Q 3016 2534 2758 2815 
Q 2500 3097 2075 3097 
Q 1594 3097 1305 2825 
Q 1016 2553 972 2059 
L 3022 2063 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-66" d="M 2375 4863 
L 2375 4384 
L 1825 4384 
Q 1516 4384 1395 4259 
Q 1275 4134 1275 3809 
L 1275 3500 
L 2222 3500 
L 2222 3053 
L 1275 3053 
L 1275 0 
L 697 0 
L 697 3053 
L 147 3053 
L 147 3500 
L 697 3500 
L 697 3744 
Q 697 4328 969 4595 
Q 1241 4863 1831 4863 
L 2375 4863 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-67" d="M 2906 1791 
Q 2906 2416 2648 2759 
Q 2391 3103 1925 3103 
Q 1463 3103 1205 2759 
Q 947 2416 947 1791 
Q 947 1169 1205 825 
Q 1463 481 1925 481 
Q 2391 481 2648 825 
Q 2906 1169 2906 1791 
z
M 3481 434 
Q 3481 -459 3084 -895 
Q 2688 -1331 1869 -1331 
Q 1566 -1331 1297 -1286 
Q 1028 -1241 775 -1147 
L 775 -588 
Q 1028 -725 1275 -790 
Q 1522 -856 1778 -856 
Q 2344 -856 2625 -561 
Q 2906 -266 2906 331 
L 2906 616 
Q 2728 306 2450 153 
Q 2172 0 1784 0 
Q 1141 0 747 490 
Q 353 981 353 1791 
Q 353 2603 747 3093 
Q 1141 3584 1784 3584 
Q 2172 3584 2450 3431 
Q 2728 3278 2906 2969 
L 2906 3500 
L 3481 3500 
L 3481 434 
z
" transform="scale(0.015625)"/>
     </defs>
     <use xlink:href="#DejaVuSans-53"/>
     <use xlink:href="#DejaVuSans-74" transform="translate(63.476562 0)"/>
     <use xlink:href="#DejaVuSans-72" transform="translate(102.685547 0)"/>
     <use xlink:href="#DejaVuSans-69" transform="translate(143.798828 0)"/>
     <use xlink:href="#DejaVuSans-63" transform="translate(171.582031 0)"/>
     <use xlink:href="#DejaVuSans-74" transform="translate(226.5625 0)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(265.771484 0)"/>
     <use xlink:href="#DejaVuSans-61" transform="translate(297.558594 0)"/>
     <use xlink:href="#DejaVuSans-6e" transform="translate(358.837891 0)"/>
     <use xlink:href="#DejaVuSans-64" transform="translate(422.216797 0)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(485.693359 0)"/>
     <use xlink:href="#DejaVuSans-6e" transform="translate(517.480469 0)"/>
     <use xlink:href="#DejaVuSans-6f" transform="translate(580.859375 0)"/>
     <use xlink:href="#DejaVuSans-6e" transform="translate(642.041016 0)"/>
     <use xlink:href="#DejaVuSans-2d" transform="translate(705.419922 0)"/>
     <use xlink:href="#DejaVuSans-73" transform="translate(741.503906 0)"/>
     <use xlink:href="#DejaVuSans-74" transform="translate(793.603516 0)"/>
     <use xlink:href="#DejaVuSans-72" transform="translate(832.8125 0)"/>
     <use xlink:href="#DejaVuSans-69" transform="translate(873.925781 0)"/>
     <use xlink:href="#DejaVuSans-63" transform="translate(901.708984 0)"/>
     <use xlink:href="#DejaVuSans-74" transform="translate(956.689453 0)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(995.898438 0)"/>
     <use xlink:href="#DejaVuSans-63" transform="translate(1027.685547 0)"/>
     <use xlink:href="#DejaVuSans-75" transform="translate(1082.666016 0)"/>
     <use xlink:href="#DejaVuSans-74" transform="translate(1146.044922 0)"/>
     <use xlink:href="#DejaVuSans-73" transform="translate(1185.253906 0)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(1237.353516 0)"/>
     <use xlink:href="#DejaVuSans-72" transform="translate(1269.140625 0)"/>
     <use xlink:href="#DejaVuSans-65" transform="translate(1308.003906 0)"/>
     <use xlink:href="#DejaVuSans-74" transform="translate(1369.527344 0)"/>
     <use xlink:href="#DejaVuSans-61" transform="translate(1408.736328 0)"/>
     <use xlink:href="#DejaVuSans-69" transform="translate(1470.015625 0)"/>
     <use xlink:href="#DejaVuSans-6e" transform="translate(1497.798828 0)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(1561.177734 0)"/>
     <use xlink:href="#DejaVuSans-64" transform="translate(1592.964844 0)"/>
     <use xlink:href="#DejaVuSans-69" transform="translate(1656.441406 0)"/>
     <use xlink:href="#DejaVuSans-66" transform="translate(1684.224609 0)"/>
     <use xlink:href="#DejaVuSans-66" transform="translate(1719.429688 0)"/>
     <use xlink:href="#DejaVuSans-65" transform="translate(1754.634766 0)"/>
     <use xlink:href="#DejaVuSans-72" transform="translate(1816.158203 0)"/>
     <use xlink:href="#DejaVuSans-65" transform="translate(1855.021484 0)"/>
     <use xlink:href="#DejaVuSans-6e" transform="translate(1916.544922 0)"/>
     <use xlink:href="#DejaVuSans-74" transform="translate(1979.923828 0)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(2019.132812 0)"/>
     <use xlink:href="#DejaVuSans-65" transform="translate(2050.919922 0)"/>
     <use xlink:href="#DejaVuSans-6e" transform="translate(2112.443359 0)"/>
     <use xlink:href="#DejaVuSans-64" transform="translate(2175.822266 0)"/>
     <use xlink:href="#DejaVuSans-70" transform="translate(2239.298828 0)"/>
     <use xlink:href="#DejaVuSans-6f" transform="translate(2302.775391 0)"/>
     <use xlink:href="#DejaVuSans-69" transform="translate(2363.957031 0)"/>
     <use xlink:href="#DejaVuSans-6e" transform="translate(2391.740234 0)"/>
     <use xlink:href="#DejaVuSans-74" transform="translate(2455.119141 0)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(2494.328125 0)"/>
     <use xlink:href="#DejaVuSans-65" transform="translate(2526.115234 0)"/>
     <use xlink:href="#DejaVuSans-69" transform="translate(2587.638672 0)"/>
     <use xlink:href="#DejaVuSans-67" transform="translate(2615.421875 0)"/>
     <use xlink:href="#DejaVuSans-65" transform="translate(2678.898438 0)"/>
     <use xlink:href="#DejaVuSans-6e" transform="translate(2740.421875 0)"/>
     <use xlink:href="#DejaVuSans-73" transform="translate(2803.800781 0)"/>
     <use xlink:href="#DejaVuSans-70" transform="translate(2855.900391 0)"/>
     <use xlink:href="#DejaVuSans-61" transform="translate(2919.376953 0)"/>
     <use xlink:href="#DejaVuSans-63" transform="translate(2980.65625 0)"/>
     <use xlink:href="#DejaVuSans-65" transform="translate(3035.636719 0)"/>
     <use xlink:href="#DejaVuSans-73" transform="translate(3097.160156 0)"/>
    </g>
   </g>
   <g id="line2d_3">
    <defs>
     <path id="mebaefaf58e" d="M 0 4 
C 1.060812 4 2.078319 3.578535 2.828427 2.828427 
C 3.578535 2.078319 4 1.060812 4 0 
C 4 -1.060812 3.578535 -2.078319 2.828427 -2.828427 
C 2.078319 -3.578535 1.060812 -4 0 -4 
C -1.060812 -4 -2.078319 -3.578535 -2.828427 -2.828427 
C -3.578535 -2.078319 -4 -1.060812 -4 0 
C -4 1.060812 -3.578535 2.078319 -2.828427 2.828427 
C -2.078319 3.578535 -1.060812 4 0 4 
z
" style="stroke: #205ca8; stroke-width: 1.6"/>
    </defs>
    <g clip-path="url(#pd88586373a)">
     <use xlink:href="#mebaefaf58e" x="257.108436" y="54.761559" style="fill: #ffffff; stroke: #205ca8; stroke-width: 1.6"/>
    </g>
   </g>
   <g id="line2d_4">
    <defs>
     <path id="m56d0b2e3e0" d="M 0 4 
C 1.060812 4 2.078319 3.578535 2.828427 2.828427 
C 3.578535 2.078319 4 1.060812 4 0 
C 4 -1.060812 3.578535 -2.078319 2.828427 -2.828427 
C 2.078319 -3.578535 1.060812 -4 0 -4 
C -1.060812 -4 -2.078319 -3.578535 -2.828427 -2.828427 
C -3.578535 -2.078319 -4 -1.060812 -4 0 
C -4 1.060812 -3.578535 2.078319 -2.828427 2.828427 
C -2.078319 3.578535 -1.060812 4 0 4 
z
" style="stroke: #205ca8; stroke-width: 1.6"/>
    </defs>
    <g clip-path="url(#pd88586373a)">
     <use xlink:href="#m56d0b2e3e0" x="257.108436" y="91.333914" style="fill: #205ca8; stroke: #205ca8; stroke-width: 1.6"/>
    </g>
   </g>
   <g id="line2d_5">
    <g clip-path="url(#pd88586373a)">
     <use xlink:href="#m56d0b2e3e0" x="257.108436" y="127.906268" style="fill: #205ca8; stroke: #205ca8; stroke-width: 1.6"/>
    </g>
   </g>
   <g id="line2d_6">
    <g clip-path="url(#pd88586373a)">
     <use xlink:href="#mebaefaf58e" x="543.896554" y="127.906268" style="fill: #ffffff; stroke: #205ca8; stroke-width: 1.6"/>
    </g>
   </g>
   <g id="line2d_7">
    <g clip-path="url(#pd88586373a)">
     <use xlink:href="#m56d0b2e3e0" x="543.896554" y="164.478623" style="fill: #205ca8; stroke: #205ca8; stroke-width: 1.6"/>
    </g>
   </g>
  </g>
  <g id="axes_2">
   <g id="patch_6">
    <path d="M 171.072 489.744 
L 750.384 489.744 
L 750.384 273.0528 
L 171.072 273.0528 
z
" style="fill: #ffffff"/>
   </g>
   <g id="FillBetweenPolyCollection_1">
    <defs>
     <path id="m738951d162" d="M 184.799773 -83.165125 
L 184.799773 -83.165125 
L 186.186416 -83.165125 
L 187.57306 -83.165125 
L 188.959704 -83.165125 
L 190.346347 -83.165125 
L 191.732991 -83.165125 
L 193.119635 -83.165125 
L 194.506278 -83.165125 
L 195.892922 -83.165125 
L 197.279566 -83.165125 
L 198.666209 -83.165125 
L 200.052853 -83.165125 
L 201.439497 -83.165125 
L 202.82614 -83.165125 
L 204.212784 -83.165125 
L 205.599428 -83.165125 
L 206.986072 -83.165125 
L 208.372715 -83.165125 
L 209.759359 -83.165125 
L 211.146003 -83.165125 
L 212.532646 -83.165125 
L 213.91929 -83.165125 
L 215.305934 -83.165125 
L 216.692577 -83.165125 
L 218.079221 -83.165125 
L 219.465865 -83.165125 
L 220.852508 -83.165125 
L 222.239152 -83.165125 
L 223.625796 -83.165125 
L 225.012439 -83.165125 
L 226.399083 -83.165125 
L 227.785727 -83.165125 
L 229.172371 -83.165125 
L 230.559014 -83.165125 
L 231.945658 -83.165125 
L 233.332302 -83.165125 
L 234.718945 -83.165125 
L 236.105589 -83.165125 
L 237.492233 -83.165125 
L 238.878876 -83.165125 
L 240.26552 -83.165125 
L 241.652164 -83.165125 
L 243.038807 -83.165125 
L 244.425451 -83.165125 
L 245.812095 -83.165125 
L 247.198738 -83.165125 
L 248.585382 -83.165125 
L 249.972026 -83.165125 
L 251.35867 -83.165125 
L 252.745313 -83.165125 
L 254.131957 -83.165125 
L 255.518601 -83.165125 
L 256.905244 -83.165125 
L 258.291888 -83.165125 
L 259.678532 -83.165125 
L 261.065175 -83.165125 
L 262.451819 -83.165125 
L 263.838463 -83.165125 
L 265.225106 -83.165125 
L 266.61175 -83.165125 
L 267.998394 -83.165125 
L 269.385037 -83.165125 
L 270.771681 -83.165125 
L 272.158325 -83.165125 
L 273.544969 -83.165125 
L 274.931612 -83.165125 
L 276.318256 -83.165125 
L 277.7049 -83.165125 
L 279.091543 -83.165125 
L 280.478187 -83.165125 
L 281.864831 -83.165125 
L 283.251474 -83.165125 
L 284.638118 -83.165125 
L 286.024762 -83.165125 
L 287.411405 -83.165125 
L 288.798049 -83.165125 
L 290.184693 -83.165125 
L 291.571336 -83.165125 
L 292.95798 -83.165125 
L 294.344624 -83.165125 
L 295.731268 -83.165125 
L 297.117911 -83.165125 
L 298.504555 -83.165125 
L 299.891199 -83.165125 
L 301.277842 -83.165125 
L 302.664486 -83.165125 
L 304.05113 -83.165125 
L 305.437773 -83.165125 
L 306.824417 -83.165125 
L 308.211061 -83.165125 
L 309.597704 -83.165125 
L 310.984348 -83.165125 
L 312.370992 -83.165125 
L 313.757636 -83.165125 
L 315.144279 -83.165125 
L 316.530923 -83.165125 
L 317.917567 -83.165125 
L 319.30421 -83.165125 
L 320.690854 -83.165125 
L 322.077498 -83.165125 
L 322.077498 -129.074278 
L 322.077498 -129.074278 
L 320.690854 -128.610549 
L 319.30421 -128.14682 
L 317.917567 -127.683092 
L 316.530923 -127.219363 
L 315.144279 -126.755634 
L 313.757636 -126.291905 
L 312.370992 -125.828176 
L 310.984348 -125.364447 
L 309.597704 -124.900719 
L 308.211061 -124.43699 
L 306.824417 -123.973261 
L 305.437773 -123.509532 
L 304.05113 -123.045803 
L 302.664486 -122.582075 
L 301.277842 -122.118346 
L 299.891199 -121.654617 
L 298.504555 -121.190888 
L 297.117911 -120.727159 
L 295.731268 -120.263431 
L 294.344624 -119.799702 
L 292.95798 -119.335973 
L 291.571336 -118.872244 
L 290.184693 -118.408515 
L 288.798049 -117.944786 
L 287.411405 -117.481058 
L 286.024762 -117.017329 
L 284.638118 -116.5536 
L 283.251474 -116.089871 
L 281.864831 -115.626142 
L 280.478187 -115.162414 
L 279.091543 -114.698685 
L 277.7049 -114.234956 
L 276.318256 -113.771227 
L 274.931612 -113.307498 
L 273.544969 -112.843769 
L 272.158325 -112.380041 
L 270.771681 -111.916312 
L 269.385037 -111.452583 
L 267.998394 -110.988854 
L 266.61175 -110.525125 
L 265.225106 -110.061397 
L 263.838463 -109.597668 
L 262.451819 -109.133939 
L 261.065175 -108.67021 
L 259.678532 -108.206481 
L 258.291888 -107.742753 
L 256.905244 -107.279024 
L 255.518601 -106.815295 
L 254.131957 -106.351566 
L 252.745313 -105.887837 
L 251.35867 -105.424108 
L 249.972026 -104.96038 
L 248.585382 -104.496651 
L 247.198738 -104.032922 
L 245.812095 -103.569193 
L 244.425451 -103.105464 
L 243.038807 -102.641736 
L 241.652164 -102.178007 
L 240.26552 -101.714278 
L 238.878876 -101.250549 
L 237.492233 -100.78682 
L 236.105589 -100.323092 
L 234.718945 -99.859363 
L 233.332302 -99.395634 
L 231.945658 -98.931905 
L 230.559014 -98.468176 
L 229.172371 -98.004447 
L 227.785727 -97.540719 
L 226.399083 -97.07699 
L 225.012439 -96.613261 
L 223.625796 -96.149532 
L 222.239152 -95.685803 
L 220.852508 -95.222075 
L 219.465865 -94.758346 
L 218.079221 -94.294617 
L 216.692577 -93.830888 
L 215.305934 -93.367159 
L 213.91929 -92.903431 
L 212.532646 -92.439702 
L 211.146003 -91.975973 
L 209.759359 -91.512244 
L 208.372715 -91.048515 
L 206.986072 -90.584786 
L 205.599428 -90.121058 
L 204.212784 -89.657329 
L 202.82614 -89.1936 
L 201.439497 -88.729871 
L 200.052853 -88.266142 
L 198.666209 -87.802414 
L 197.279566 -87.338685 
L 195.892922 -86.874956 
L 194.506278 -86.411227 
L 193.119635 -85.947498 
L 191.732991 -85.483769 
L 190.346347 -85.020041 
L 188.959704 -84.556312 
L 187.57306 -84.092583 
L 186.186416 -83.628854 
L 184.799773 -83.165125 
z
" style="stroke: #e5edf8"/>
    </defs>
    <g clip-path="url(#p3c6d678dee)">
     <use xlink:href="#m738951d162" x="0" y="547.2" style="fill: #e5edf8; stroke: #e5edf8"/>
    </g>
   </g>
   <g id="FillBetweenPolyCollection_2">
    <defs>
     <path id="mf8fe1b0f8d" d="M 322.077498 -129.074278 
L 322.077498 -129.074278 
L 323.464141 -129.074278 
L 324.850785 -129.074278 
L 326.237429 -129.074278 
L 327.624072 -129.074278 
L 329.010716 -129.074278 
L 330.39736 -129.074278 
L 331.784003 -129.074278 
L 333.170647 -129.074278 
L 334.557291 -129.074278 
L 335.943935 -129.074278 
L 337.330578 -129.074278 
L 338.717222 -129.074278 
L 340.103866 -129.074278 
L 341.490509 -129.074278 
L 342.877153 -129.074278 
L 344.263797 -129.074278 
L 345.65044 -129.074278 
L 347.037084 -129.074278 
L 348.423728 -129.074278 
L 349.810371 -129.074278 
L 351.197015 -129.074278 
L 352.583659 -129.074278 
L 353.970302 -129.074278 
L 355.356946 -129.074278 
L 356.74359 -129.074278 
L 358.130234 -129.074278 
L 359.516877 -129.074278 
L 360.903521 -129.074278 
L 362.290165 -129.074278 
L 363.676808 -129.074278 
L 365.063452 -129.074278 
L 366.450096 -129.074278 
L 367.836739 -129.074278 
L 369.223383 -129.074278 
L 370.610027 -129.074278 
L 371.99667 -129.074278 
L 373.383314 -129.074278 
L 374.769958 -129.074278 
L 376.156601 -129.074278 
L 377.543245 -129.074278 
L 378.929889 -129.074278 
L 380.316533 -129.074278 
L 381.703176 -129.074278 
L 383.08982 -129.074278 
L 384.476464 -129.074278 
L 385.863107 -129.074278 
L 387.249751 -129.074278 
L 388.636395 -129.074278 
L 390.023038 -129.074278 
L 391.409682 -129.074278 
L 392.796326 -129.074278 
L 394.182969 -129.074278 
L 395.569613 -129.074278 
L 396.956257 -129.074278 
L 398.3429 -129.074278 
L 399.729544 -129.074278 
L 401.116188 -129.074278 
L 402.502832 -129.074278 
L 403.889475 -129.074278 
L 405.276119 -129.074278 
L 406.662763 -129.074278 
L 408.049406 -129.074278 
L 409.43605 -129.074278 
L 410.822694 -129.074278 
L 412.209337 -129.074278 
L 413.595981 -129.074278 
L 414.982625 -129.074278 
L 416.369268 -129.074278 
L 417.755912 -129.074278 
L 419.142556 -129.074278 
L 420.529199 -129.074278 
L 421.915843 -129.074278 
L 423.302487 -129.074278 
L 424.689131 -129.074278 
L 426.075774 -129.074278 
L 427.462418 -129.074278 
L 428.849062 -129.074278 
L 430.235705 -129.074278 
L 431.622349 -129.074278 
L 433.008993 -129.074278 
L 434.395636 -129.074278 
L 435.78228 -129.074278 
L 437.168924 -129.074278 
L 438.555567 -129.074278 
L 439.942211 -129.074278 
L 441.328855 -129.074278 
L 442.715498 -129.074278 
L 444.102142 -129.074278 
L 445.488786 -129.074278 
L 446.87543 -129.074278 
L 448.262073 -129.074278 
L 449.648717 -129.074278 
L 451.035361 -129.074278 
L 452.422004 -129.074278 
L 453.808648 -129.074278 
L 455.195292 -129.074278 
L 456.581935 -129.074278 
L 457.968579 -129.074278 
L 459.355223 -129.074278 
L 459.355223 -174.983431 
L 459.355223 -174.983431 
L 457.968579 -174.519702 
L 456.581935 -174.055973 
L 455.195292 -173.592244 
L 453.808648 -173.128515 
L 452.422004 -172.664786 
L 451.035361 -172.201058 
L 449.648717 -171.737329 
L 448.262073 -171.2736 
L 446.87543 -170.809871 
L 445.488786 -170.346142 
L 444.102142 -169.882414 
L 442.715498 -169.418685 
L 441.328855 -168.954956 
L 439.942211 -168.491227 
L 438.555567 -168.027498 
L 437.168924 -167.563769 
L 435.78228 -167.100041 
L 434.395636 -166.636312 
L 433.008993 -166.172583 
L 431.622349 -165.708854 
L 430.235705 -165.245125 
L 428.849062 -164.781397 
L 427.462418 -164.317668 
L 426.075774 -163.853939 
L 424.689131 -163.39021 
L 423.302487 -162.926481 
L 421.915843 -162.462753 
L 420.529199 -161.999024 
L 419.142556 -161.535295 
L 417.755912 -161.071566 
L 416.369268 -160.607837 
L 414.982625 -160.144108 
L 413.595981 -159.68038 
L 412.209337 -159.216651 
L 410.822694 -158.752922 
L 409.43605 -158.289193 
L 408.049406 -157.825464 
L 406.662763 -157.361736 
L 405.276119 -156.898007 
L 403.889475 -156.434278 
L 402.502832 -155.970549 
L 401.116188 -155.50682 
L 399.729544 -155.043092 
L 398.3429 -154.579363 
L 396.956257 -154.115634 
L 395.569613 -153.651905 
L 394.182969 -153.188176 
L 392.796326 -152.724447 
L 391.409682 -152.260719 
L 390.023038 -151.79699 
L 388.636395 -151.333261 
L 387.249751 -150.869532 
L 385.863107 -150.405803 
L 384.476464 -149.942075 
L 383.08982 -149.478346 
L 381.703176 -149.014617 
L 380.316533 -148.550888 
L 378.929889 -148.087159 
L 377.543245 -147.623431 
L 376.156601 -147.159702 
L 374.769958 -146.695973 
L 373.383314 -146.232244 
L 371.99667 -145.768515 
L 370.610027 -145.304786 
L 369.223383 -144.841058 
L 367.836739 -144.377329 
L 366.450096 -143.9136 
L 365.063452 -143.449871 
L 363.676808 -142.986142 
L 362.290165 -142.522414 
L 360.903521 -142.058685 
L 359.516877 -141.594956 
L 358.130234 -141.131227 
L 356.74359 -140.667498 
L 355.356946 -140.203769 
L 353.970302 -139.740041 
L 352.583659 -139.276312 
L 351.197015 -138.812583 
L 349.810371 -138.348854 
L 348.423728 -137.885125 
L 347.037084 -137.421397 
L 345.65044 -136.957668 
L 344.263797 -136.493939 
L 342.877153 -136.03021 
L 341.490509 -135.566481 
L 340.103866 -135.102753 
L 338.717222 -134.639024 
L 337.330578 -134.175295 
L 335.943935 -133.711566 
L 334.557291 -133.247837 
L 333.170647 -132.784108 
L 331.784003 -132.32038 
L 330.39736 -131.856651 
L 329.010716 -131.392922 
L 327.624072 -130.929193 
L 326.237429 -130.465464 
L 324.850785 -130.001736 
L 323.464141 -129.538007 
L 322.077498 -129.074278 
z
" style="stroke: #e5edf8"/>
    </defs>
    <g clip-path="url(#p3c6d678dee)">
     <use xlink:href="#mf8fe1b0f8d" x="0" y="547.2" style="fill: #e5edf8; stroke: #e5edf8"/>
    </g>
   </g>
   <g id="FillBetweenPolyCollection_3">
    <defs>
     <path id="md747f2d7c8" d="M 459.355223 -174.983431 
L 459.355223 -174.983431 
L 460.741866 -174.983431 
L 462.12851 -174.983431 
L 463.515154 -174.983431 
L 464.901798 -174.983431 
L 466.288441 -174.983431 
L 467.675085 -174.983431 
L 469.061729 -174.983431 
L 470.448372 -174.983431 
L 471.835016 -174.983431 
L 473.22166 -174.983431 
L 474.608303 -174.983431 
L 475.994947 -174.983431 
L 477.381591 -174.983431 
L 478.768234 -174.983431 
L 480.154878 -174.983431 
L 481.541522 -174.983431 
L 482.928165 -174.983431 
L 484.314809 -174.983431 
L 485.701453 -174.983431 
L 487.088097 -174.983431 
L 488.47474 -174.983431 
L 489.861384 -174.983431 
L 491.248028 -174.983431 
L 492.634671 -174.983431 
L 494.021315 -174.983431 
L 495.407959 -174.983431 
L 496.794602 -174.983431 
L 498.181246 -174.983431 
L 499.56789 -174.983431 
L 500.954533 -174.983431 
L 502.341177 -174.983431 
L 503.727821 -174.983431 
L 505.114464 -174.983431 
L 506.501108 -174.983431 
L 507.887752 -174.983431 
L 509.274396 -174.983431 
L 510.661039 -174.983431 
L 512.047683 -174.983431 
L 513.434327 -174.983431 
L 514.82097 -174.983431 
L 516.207614 -174.983431 
L 517.594258 -174.983431 
L 518.980901 -174.983431 
L 520.367545 -174.983431 
L 521.754189 -174.983431 
L 523.140832 -174.983431 
L 524.527476 -174.983431 
L 525.91412 -174.983431 
L 527.300763 -174.983431 
L 528.687407 -174.983431 
L 530.074051 -174.983431 
L 531.460695 -174.983431 
L 532.847338 -174.983431 
L 534.233982 -174.983431 
L 535.620626 -174.983431 
L 537.007269 -174.983431 
L 538.393913 -174.983431 
L 539.780557 -174.983431 
L 541.1672 -174.983431 
L 542.553844 -174.983431 
L 543.940488 -174.983431 
L 545.327131 -174.983431 
L 546.713775 -174.983431 
L 548.100419 -174.983431 
L 549.487062 -174.983431 
L 550.873706 -174.983431 
L 552.26035 -174.983431 
L 553.646994 -174.983431 
L 555.033637 -174.983431 
L 556.420281 -174.983431 
L 557.806925 -174.983431 
L 559.193568 -174.983431 
L 560.580212 -174.983431 
L 561.966856 -174.983431 
L 563.353499 -174.983431 
L 564.740143 -174.983431 
L 566.126787 -174.983431 
L 567.51343 -174.983431 
L 568.900074 -174.983431 
L 570.286718 -174.983431 
L 571.673361 -174.983431 
L 573.060005 -174.983431 
L 574.446649 -174.983431 
L 575.833293 -174.983431 
L 577.219936 -174.983431 
L 578.60658 -174.983431 
L 579.993224 -174.983431 
L 581.379867 -174.983431 
L 582.766511 -174.983431 
L 584.153155 -174.983431 
L 585.539798 -174.983431 
L 586.926442 -174.983431 
L 588.313086 -174.983431 
L 589.699729 -174.983431 
L 591.086373 -174.983431 
L 592.473017 -174.983431 
L 593.85966 -174.983431 
L 595.246304 -174.983431 
L 596.632948 -174.983431 
L 596.632948 -220.892583 
L 596.632948 -220.892583 
L 595.246304 -220.428854 
L 593.85966 -219.965125 
L 592.473017 -219.501397 
L 591.086373 -219.037668 
L 589.699729 -218.573939 
L 588.313086 -218.11021 
L 586.926442 -217.646481 
L 585.539798 -217.182753 
L 584.153155 -216.719024 
L 582.766511 -216.255295 
L 581.379867 -215.791566 
L 579.993224 -215.327837 
L 578.60658 -214.864108 
L 577.219936 -214.40038 
L 575.833293 -213.936651 
L 574.446649 -213.472922 
L 573.060005 -213.009193 
L 571.673361 -212.545464 
L 570.286718 -212.081736 
L 568.900074 -211.618007 
L 567.51343 -211.154278 
L 566.126787 -210.690549 
L 564.740143 -210.22682 
L 563.353499 -209.763092 
L 561.966856 -209.299363 
L 560.580212 -208.835634 
L 559.193568 -208.371905 
L 557.806925 -207.908176 
L 556.420281 -207.444447 
L 555.033637 -206.980719 
L 553.646994 -206.51699 
L 552.26035 -206.053261 
L 550.873706 -205.589532 
L 549.487062 -205.125803 
L 548.100419 -204.662075 
L 546.713775 -204.198346 
L 545.327131 -203.734617 
L 543.940488 -203.270888 
L 542.553844 -202.807159 
L 541.1672 -202.343431 
L 539.780557 -201.879702 
L 538.393913 -201.415973 
L 537.007269 -200.952244 
L 535.620626 -200.488515 
L 534.233982 -200.024786 
L 532.847338 -199.561058 
L 531.460695 -199.097329 
L 530.074051 -198.6336 
L 528.687407 -198.169871 
L 527.300763 -197.706142 
L 525.91412 -197.242414 
L 524.527476 -196.778685 
L 523.140832 -196.314956 
L 521.754189 -195.851227 
L 520.367545 -195.387498 
L 518.980901 -194.923769 
L 517.594258 -194.460041 
L 516.207614 -193.996312 
L 514.82097 -193.532583 
L 513.434327 -193.068854 
L 512.047683 -192.605125 
L 510.661039 -192.141397 
L 509.274396 -191.677668 
L 507.887752 -191.213939 
L 506.501108 -190.75021 
L 505.114464 -190.286481 
L 503.727821 -189.822753 
L 502.341177 -189.359024 
L 500.954533 -188.895295 
L 499.56789 -188.431566 
L 498.181246 -187.967837 
L 496.794602 -187.504108 
L 495.407959 -187.04038 
L 494.021315 -186.576651 
L 492.634671 -186.112922 
L 491.248028 -185.649193 
L 489.861384 -185.185464 
L 488.47474 -184.721736 
L 487.088097 -184.258007 
L 485.701453 -183.794278 
L 484.314809 -183.330549 
L 482.928165 -182.86682 
L 481.541522 -182.403092 
L 480.154878 -181.939363 
L 478.768234 -181.475634 
L 477.381591 -181.011905 
L 475.994947 -180.548176 
L 474.608303 -180.084447 
L 473.22166 -179.620719 
L 471.835016 -179.15699 
L 470.448372 -178.693261 
L 469.061729 -178.229532 
L 467.675085 -177.765803 
L 466.288441 -177.302075 
L 464.901798 -176.838346 
L 463.515154 -176.374617 
L 462.12851 -175.910888 
L 460.741866 -175.447159 
L 459.355223 -174.983431 
z
" style="stroke: #e5edf8"/>
    </defs>
    <g clip-path="url(#p3c6d678dee)">
     <use xlink:href="#md747f2d7c8" x="0" y="547.2" style="fill: #e5edf8; stroke: #e5edf8"/>
    </g>
   </g>
   <g id="FillBetweenPolyCollection_4">
    <defs>
     <path id="mbcf194dccc" d="M 596.632948 -220.892583 
L 596.632948 -220.892583 
L 598.019592 -220.892583 
L 599.406235 -220.892583 
L 600.792879 -220.892583 
L 602.179523 -220.892583 
L 603.566166 -220.892583 
L 604.95281 -220.892583 
L 606.339454 -220.892583 
L 607.726097 -220.892583 
L 609.112741 -220.892583 
L 610.499385 -220.892583 
L 611.886028 -220.892583 
L 613.272672 -220.892583 
L 614.659316 -220.892583 
L 616.04596 -220.892583 
L 617.432603 -220.892583 
L 618.819247 -220.892583 
L 620.205891 -220.892583 
L 621.592534 -220.892583 
L 622.979178 -220.892583 
L 624.365822 -220.892583 
L 625.752465 -220.892583 
L 627.139109 -220.892583 
L 628.525753 -220.892583 
L 629.912396 -220.892583 
L 631.29904 -220.892583 
L 632.685684 -220.892583 
L 634.072327 -220.892583 
L 635.458971 -220.892583 
L 636.845615 -220.892583 
L 638.232259 -220.892583 
L 639.618902 -220.892583 
L 641.005546 -220.892583 
L 642.39219 -220.892583 
L 643.778833 -220.892583 
L 645.165477 -220.892583 
L 646.552121 -220.892583 
L 647.938764 -220.892583 
L 649.325408 -220.892583 
L 650.712052 -220.892583 
L 652.098695 -220.892583 
L 653.485339 -220.892583 
L 654.871983 -220.892583 
L 656.258626 -220.892583 
L 657.64527 -220.892583 
L 659.031914 -220.892583 
L 660.418558 -220.892583 
L 661.805201 -220.892583 
L 663.191845 -220.892583 
L 664.578489 -220.892583 
L 665.965132 -220.892583 
L 667.351776 -220.892583 
L 668.73842 -220.892583 
L 670.125063 -220.892583 
L 671.511707 -220.892583 
L 672.898351 -220.892583 
L 674.284994 -220.892583 
L 675.671638 -220.892583 
L 677.058282 -220.892583 
L 678.444925 -220.892583 
L 679.831569 -220.892583 
L 681.218213 -220.892583 
L 682.604857 -220.892583 
L 683.9915 -220.892583 
L 685.378144 -220.892583 
L 686.764788 -220.892583 
L 688.151431 -220.892583 
L 689.538075 -220.892583 
L 690.924719 -220.892583 
L 692.311362 -220.892583 
L 693.698006 -220.892583 
L 695.08465 -220.892583 
L 696.471293 -220.892583 
L 697.857937 -220.892583 
L 699.244581 -220.892583 
L 700.631224 -220.892583 
L 702.017868 -220.892583 
L 703.404512 -220.892583 
L 704.791156 -220.892583 
L 706.177799 -220.892583 
L 707.564443 -220.892583 
L 708.951087 -220.892583 
L 710.33773 -220.892583 
L 711.724374 -220.892583 
L 713.111018 -220.892583 
L 714.497661 -220.892583 
L 715.884305 -220.892583 
L 717.270949 -220.892583 
L 718.657592 -220.892583 
L 720.044236 -220.892583 
L 721.43088 -220.892583 
L 722.817523 -220.892583 
L 724.204167 -220.892583 
L 725.590811 -220.892583 
L 726.977455 -220.892583 
L 728.364098 -220.892583 
L 729.750742 -220.892583 
L 731.137386 -220.892583 
L 732.524029 -220.892583 
L 733.910673 -220.892583 
L 733.910673 -266.801736 
L 733.910673 -266.801736 
L 732.524029 -266.338007 
L 731.137386 -265.874278 
L 729.750742 -265.410549 
L 728.364098 -264.94682 
L 726.977455 -264.483092 
L 725.590811 -264.019363 
L 724.204167 -263.555634 
L 722.817523 -263.091905 
L 721.43088 -262.628176 
L 720.044236 -262.164447 
L 718.657592 -261.700719 
L 717.270949 -261.23699 
L 715.884305 -260.773261 
L 714.497661 -260.309532 
L 713.111018 -259.845803 
L 711.724374 -259.382075 
L 710.33773 -258.918346 
L 708.951087 -258.454617 
L 707.564443 -257.990888 
L 706.177799 -257.527159 
L 704.791156 -257.063431 
L 703.404512 -256.599702 
L 702.017868 -256.135973 
L 700.631224 -255.672244 
L 699.244581 -255.208515 
L 697.857937 -254.744786 
L 696.471293 -254.281058 
L 695.08465 -253.817329 
L 693.698006 -253.3536 
L 692.311362 -252.889871 
L 690.924719 -252.426142 
L 689.538075 -251.962414 
L 688.151431 -251.498685 
L 686.764788 -251.034956 
L 685.378144 -250.571227 
L 683.9915 -250.107498 
L 682.604857 -249.643769 
L 681.218213 -249.180041 
L 679.831569 -248.716312 
L 678.444925 -248.252583 
L 677.058282 -247.788854 
L 675.671638 -247.325125 
L 674.284994 -246.861397 
L 672.898351 -246.397668 
L 671.511707 -245.933939 
L 670.125063 -245.47021 
L 668.73842 -245.006481 
L 667.351776 -244.542753 
L 665.965132 -244.079024 
L 664.578489 -243.615295 
L 663.191845 -243.151566 
L 661.805201 -242.687837 
L 660.418558 -242.224108 
L 659.031914 -241.76038 
L 657.64527 -241.296651 
L 656.258626 -240.832922 
L 654.871983 -240.369193 
L 653.485339 -239.905464 
L 652.098695 -239.441736 
L 650.712052 -238.978007 
L 649.325408 -238.514278 
L 647.938764 -238.050549 
L 646.552121 -237.58682 
L 645.165477 -237.123092 
L 643.778833 -236.659363 
L 642.39219 -236.195634 
L 641.005546 -235.731905 
L 639.618902 -235.268176 
L 638.232259 -234.804447 
L 636.845615 -234.340719 
L 635.458971 -233.87699 
L 634.072327 -233.413261 
L 632.685684 -232.949532 
L 631.29904 -232.485803 
L 629.912396 -232.022075 
L 628.525753 -231.558346 
L 627.139109 -231.094617 
L 625.752465 -230.630888 
L 624.365822 -230.167159 
L 622.979178 -229.703431 
L 621.592534 -229.239702 
L 620.205891 -228.775973 
L 618.819247 -228.312244 
L 617.432603 -227.848515 
L 616.04596 -227.384786 
L 614.659316 -226.921058 
L 613.272672 -226.457329 
L 611.886028 -225.9936 
L 610.499385 -225.529871 
L 609.112741 -225.066142 
L 607.726097 -224.602414 
L 606.339454 -224.138685 
L 604.95281 -223.674956 
L 603.566166 -223.211227 
L 602.179523 -222.747498 
L 600.792879 -222.283769 
L 599.406235 -221.820041 
L 598.019592 -221.356312 
L 596.632948 -220.892583 
z
" style="stroke: #e5edf8"/>
    </defs>
    <g clip-path="url(#p3c6d678dee)">
     <use xlink:href="#mbcf194dccc" x="0" y="547.2" style="fill: #e5edf8; stroke: #e5edf8"/>
    </g>
   </g>
   <g id="matplotlib.axis_3">
    <g id="xtick_3">
     <g id="line2d_8">
      <path d="M 184.799773 489.744 
L 184.799773 273.0528 
" clip-path="url(#p3c6d678dee)" style="fill: none; stroke: #e3e6ea; stroke-width: 0.6; stroke-linecap: square"/>
     </g>
     <g id="line2d_9">
      <g>
       <use xlink:href="#m14f956db99" x="184.799773" y="489.744" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_8">
      <!-- $-1$ -->
      <g transform="translate(177.399773 504.342437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-2212" transform="translate(0 0.09375)"/>
       <use xlink:href="#DejaVuSans-31" transform="translate(83.789062 0.09375)"/>
      </g>
     </g>
    </g>
    <g id="xtick_4">
     <g id="line2d_10">
      <path d="M 322.077498 489.744 
L 322.077498 273.0528 
" clip-path="url(#p3c6d678dee)" style="fill: none; stroke: #e3e6ea; stroke-width: 0.6; stroke-linecap: square"/>
     </g>
     <g id="line2d_11">
      <g>
       <use xlink:href="#m14f956db99" x="322.077498" y="489.744" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_9">
      <!-- $-1/2$ -->
      <g transform="translate(309.977498 504.342437) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-2f" d="M 1625 4666 
L 2156 4666 
L 531 -594 
L 0 -594 
L 1625 4666 
z
" transform="scale(0.015625)"/>
        <path id="DejaVuSans-32" d="M 1228 531 
L 3431 531 
L 3431 0 
L 469 0 
L 469 531 
Q 828 903 1448 1529 
Q 2069 2156 2228 2338 
Q 2531 2678 2651 2914 
Q 2772 3150 2772 3378 
Q 2772 3750 2511 3984 
Q 2250 4219 1831 4219 
Q 1534 4219 1204 4116 
Q 875 4013 500 3803 
L 500 4441 
Q 881 4594 1212 4672 
Q 1544 4750 1819 4750 
Q 2544 4750 2975 4387 
Q 3406 4025 3406 3419 
Q 3406 3131 3298 2873 
Q 3191 2616 2906 2266 
Q 2828 2175 2409 1742 
Q 1991 1309 1228 531 
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-2212" transform="translate(0 0.78125)"/>
       <use xlink:href="#DejaVuSans-31" transform="translate(83.789062 0.78125)"/>
       <use xlink:href="#DejaVuSans-2f" transform="translate(147.412109 0.78125)"/>
       <use xlink:href="#DejaVuSans-32" transform="translate(177.478516 0.78125)"/>
      </g>
     </g>
    </g>
    <g id="xtick_5">
     <g id="line2d_12">
      <path d="M 459.355223 489.744 
L 459.355223 273.0528 
" clip-path="url(#p3c6d678dee)" style="fill: none; stroke: #e3e6ea; stroke-width: 0.6; stroke-linecap: square"/>
     </g>
     <g id="line2d_13">
      <g>
       <use xlink:href="#m14f956db99" x="459.355223" y="489.744" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_10">
      <!-- $0$ -->
      <g transform="translate(456.155223 504.342437) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-30" d="M 2034 4250 
Q 1547 4250 1301 3770 
Q 1056 3291 1056 2328 
Q 1056 1369 1301 889 
Q 1547 409 2034 409 
Q 2525 409 2770 889 
Q 3016 1369 3016 2328 
Q 3016 3291 2770 3770 
Q 2525 4250 2034 4250 
z
M 2034 4750 
Q 2819 4750 3233 4129 
Q 3647 3509 3647 2328 
Q 3647 1150 3233 529 
Q 2819 -91 2034 -91 
Q 1250 -91 836 529 
Q 422 1150 422 2328 
Q 422 3509 836 4129 
Q 1250 4750 2034 4750 
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-30" transform="translate(0 0.78125)"/>
      </g>
     </g>
    </g>
    <g id="xtick_6">
     <g id="line2d_14">
      <path d="M 596.632948 489.744 
L 596.632948 273.0528 
" clip-path="url(#p3c6d678dee)" style="fill: none; stroke: #e3e6ea; stroke-width: 0.6; stroke-linecap: square"/>
     </g>
     <g id="line2d_15">
      <g>
       <use xlink:href="#m14f956db99" x="596.632948" y="489.744" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_11">
      <!-- $1/2$ -->
      <g transform="translate(588.732948 504.342437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-31" transform="translate(0 0.78125)"/>
       <use xlink:href="#DejaVuSans-2f" transform="translate(63.623047 0.78125)"/>
       <use xlink:href="#DejaVuSans-32" transform="translate(93.689453 0.78125)"/>
      </g>
     </g>
    </g>
    <g id="xtick_7">
     <g id="line2d_16">
      <path d="M 733.910673 489.744 
L 733.910673 273.0528 
" clip-path="url(#p3c6d678dee)" style="fill: none; stroke: #e3e6ea; stroke-width: 0.6; stroke-linecap: square"/>
     </g>
     <g id="line2d_17">
      <g>
       <use xlink:href="#m14f956db99" x="733.910673" y="489.744" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_12">
      <!-- $1$ -->
      <g transform="translate(730.710673 504.342437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-31" transform="translate(0 0.09375)"/>
      </g>
     </g>
    </g>
    <g id="text_13">
     <!-- Scalar interval used to define the operator cuts -->
     <g transform="translate(342.163937 518.020562) scale(0.1 -0.1)">
      <defs>
       <path id="DejaVuSans-6c" d="M 603 4863 
L 1178 4863 
L 1178 0 
L 603 0 
L 603 4863 
z
" transform="scale(0.015625)"/>
       <path id="DejaVuSans-76" d="M 191 3500 
L 800 3500 
L 1894 563 
L 2988 3500 
L 3597 3500 
L 2284 0 
L 1503 0 
L 191 3500 
z
" transform="scale(0.015625)"/>
       <path id="DejaVuSans-68" d="M 3513 2113 
L 3513 0 
L 2938 0 
L 2938 2094 
Q 2938 2591 2744 2837 
Q 2550 3084 2163 3084 
Q 1697 3084 1428 2787 
Q 1159 2491 1159 1978 
L 1159 0 
L 581 0 
L 581 4863 
L 1159 4863 
L 1159 2956 
Q 1366 3272 1645 3428 
Q 1925 3584 2291 3584 
Q 2894 3584 3203 3211 
Q 3513 2838 3513 2113 
z
" transform="scale(0.015625)"/>
      </defs>
      <use xlink:href="#DejaVuSans-53"/>
      <use xlink:href="#DejaVuSans-63" transform="translate(63.476562 0)"/>
      <use xlink:href="#DejaVuSans-61" transform="translate(118.457031 0)"/>
      <use xlink:href="#DejaVuSans-6c" transform="translate(179.736328 0)"/>
      <use xlink:href="#DejaVuSans-61" transform="translate(207.519531 0)"/>
      <use xlink:href="#DejaVuSans-72" transform="translate(268.798828 0)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(309.912109 0)"/>
      <use xlink:href="#DejaVuSans-69" transform="translate(341.699219 0)"/>
      <use xlink:href="#DejaVuSans-6e" transform="translate(369.482422 0)"/>
      <use xlink:href="#DejaVuSans-74" transform="translate(432.861328 0)"/>
      <use xlink:href="#DejaVuSans-65" transform="translate(472.070312 0)"/>
      <use xlink:href="#DejaVuSans-72" transform="translate(533.59375 0)"/>
      <use xlink:href="#DejaVuSans-76" transform="translate(574.707031 0)"/>
      <use xlink:href="#DejaVuSans-61" transform="translate(633.886719 0)"/>
      <use xlink:href="#DejaVuSans-6c" transform="translate(695.166016 0)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(722.949219 0)"/>
      <use xlink:href="#DejaVuSans-75" transform="translate(754.736328 0)"/>
      <use xlink:href="#DejaVuSans-73" transform="translate(818.115234 0)"/>
      <use xlink:href="#DejaVuSans-65" transform="translate(870.214844 0)"/>
      <use xlink:href="#DejaVuSans-64" transform="translate(931.738281 0)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(995.214844 0)"/>
      <use xlink:href="#DejaVuSans-74" transform="translate(1027.001953 0)"/>
      <use xlink:href="#DejaVuSans-6f" transform="translate(1066.210938 0)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(1127.392578 0)"/>
      <use xlink:href="#DejaVuSans-64" transform="translate(1159.179688 0)"/>
      <use xlink:href="#DejaVuSans-65" transform="translate(1222.65625 0)"/>
      <use xlink:href="#DejaVuSans-66" transform="translate(1284.179688 0)"/>
      <use xlink:href="#DejaVuSans-69" transform="translate(1319.384766 0)"/>
      <use xlink:href="#DejaVuSans-6e" transform="translate(1347.167969 0)"/>
      <use xlink:href="#DejaVuSans-65" transform="translate(1410.546875 0)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(1472.070312 0)"/>
      <use xlink:href="#DejaVuSans-74" transform="translate(1503.857422 0)"/>
      <use xlink:href="#DejaVuSans-68" transform="translate(1543.066406 0)"/>
      <use xlink:href="#DejaVuSans-65" transform="translate(1606.445312 0)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(1667.96875 0)"/>
      <use xlink:href="#DejaVuSans-6f" transform="translate(1699.755859 0)"/>
      <use xlink:href="#DejaVuSans-70" transform="translate(1760.9375 0)"/>
      <use xlink:href="#DejaVuSans-65" transform="translate(1824.414062 0)"/>
      <use xlink:href="#DejaVuSans-72" transform="translate(1885.9375 0)"/>
      <use xlink:href="#DejaVuSans-61" transform="translate(1927.050781 0)"/>
      <use xlink:href="#DejaVuSans-74" transform="translate(1988.330078 0)"/>
      <use xlink:href="#DejaVuSans-6f" transform="translate(2027.539062 0)"/>
      <use xlink:href="#DejaVuSans-72" transform="translate(2088.720703 0)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(2129.833984 0)"/>
      <use xlink:href="#DejaVuSans-63" transform="translate(2161.621094 0)"/>
      <use xlink:href="#DejaVuSans-75" transform="translate(2216.601562 0)"/>
      <use xlink:href="#DejaVuSans-74" transform="translate(2279.980469 0)"/>
      <use xlink:href="#DejaVuSans-73" transform="translate(2319.189453 0)"/>
     </g>
    </g>
   </g>
   <g id="matplotlib.axis_4">
    <g id="ytick_1">
     <g id="line2d_18">
      <path d="M 171.072 464.034875 
L 750.384 464.034875 
" clip-path="url(#p3c6d678dee)" style="fill: none; stroke: #e3e6ea; stroke-width: 0.6; stroke-linecap: square"/>
     </g>
     <g id="line2d_19">
      <defs>
       <path id="mdd30b81cce" d="M 0 0 
L -3.5 0 
" style="stroke: #000000; stroke-width: 0.8"/>
      </defs>
      <g>
       <use xlink:href="#mdd30b81cce" x="171.072" y="464.034875" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_14">
      <!-- $-1$ -->
      <g transform="translate(149.272 467.834093) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-2212" transform="translate(0 0.09375)"/>
       <use xlink:href="#DejaVuSans-31" transform="translate(83.789062 0.09375)"/>
      </g>
     </g>
    </g>
    <g id="ytick_2">
     <g id="line2d_20">
      <path d="M 171.072 418.125722 
L 750.384 418.125722 
" clip-path="url(#p3c6d678dee)" style="fill: none; stroke: #e3e6ea; stroke-width: 0.6; stroke-linecap: square"/>
     </g>
     <g id="line2d_21">
      <g>
       <use xlink:href="#mdd30b81cce" x="171.072" y="418.125722" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_15">
      <!-- $-1/2$ -->
      <g transform="translate(139.872 421.924941) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-2212" transform="translate(0 0.78125)"/>
       <use xlink:href="#DejaVuSans-31" transform="translate(83.789062 0.78125)"/>
       <use xlink:href="#DejaVuSans-2f" transform="translate(147.412109 0.78125)"/>
       <use xlink:href="#DejaVuSans-32" transform="translate(177.478516 0.78125)"/>
      </g>
     </g>
    </g>
    <g id="ytick_3">
     <g id="line2d_22">
      <path d="M 171.072 372.216569 
L 750.384 372.216569 
" clip-path="url(#p3c6d678dee)" style="fill: none; stroke: #e3e6ea; stroke-width: 0.6; stroke-linecap: square"/>
     </g>
     <g id="line2d_23">
      <g>
       <use xlink:href="#mdd30b81cce" x="171.072" y="372.216569" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_16">
      <!-- $0$ -->
      <g transform="translate(157.672 376.015788) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-30" transform="translate(0 0.78125)"/>
      </g>
     </g>
    </g>
    <g id="ytick_4">
     <g id="line2d_24">
      <path d="M 171.072 326.307417 
L 750.384 326.307417 
" clip-path="url(#p3c6d678dee)" style="fill: none; stroke: #e3e6ea; stroke-width: 0.6; stroke-linecap: square"/>
     </g>
     <g id="line2d_25">
      <g>
       <use xlink:href="#mdd30b81cce" x="171.072" y="326.307417" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_17">
      <!-- $1/2$ -->
      <g transform="translate(148.272 330.106636) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-31" transform="translate(0 0.78125)"/>
       <use xlink:href="#DejaVuSans-2f" transform="translate(63.623047 0.78125)"/>
       <use xlink:href="#DejaVuSans-32" transform="translate(93.689453 0.78125)"/>
      </g>
     </g>
    </g>
    <g id="ytick_5">
     <g id="line2d_26">
      <path d="M 171.072 280.398264 
L 750.384 280.398264 
" clip-path="url(#p3c6d678dee)" style="fill: none; stroke: #e3e6ea; stroke-width: 0.6; stroke-linecap: square"/>
     </g>
     <g id="line2d_27">
      <g>
       <use xlink:href="#mdd30b81cce" x="171.072" y="280.398264" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_18">
      <!-- $1$ -->
      <g transform="translate(157.672 284.197483) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-31" transform="translate(0 0.09375)"/>
      </g>
     </g>
    </g>
    <g id="text_19">
     <!-- Scalar value / coefficient -->
     <g transform="translate(133.792313 443.14215) rotate(-90) scale(0.1 -0.1)">
      <use xlink:href="#DejaVuSans-53"/>
      <use xlink:href="#DejaVuSans-63" transform="translate(63.476562 0)"/>
      <use xlink:href="#DejaVuSans-61" transform="translate(118.457031 0)"/>
      <use xlink:href="#DejaVuSans-6c" transform="translate(179.736328 0)"/>
      <use xlink:href="#DejaVuSans-61" transform="translate(207.519531 0)"/>
      <use xlink:href="#DejaVuSans-72" transform="translate(268.798828 0)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(309.912109 0)"/>
      <use xlink:href="#DejaVuSans-76" transform="translate(341.699219 0)"/>
      <use xlink:href="#DejaVuSans-61" transform="translate(400.878906 0)"/>
      <use xlink:href="#DejaVuSans-6c" transform="translate(462.158203 0)"/>
      <use xlink:href="#DejaVuSans-75" transform="translate(489.941406 0)"/>
      <use xlink:href="#DejaVuSans-65" transform="translate(553.320312 0)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(614.84375 0)"/>
      <use xlink:href="#DejaVuSans-2f" transform="translate(646.630859 0)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(680.322266 0)"/>
      <use xlink:href="#DejaVuSans-63" transform="translate(712.109375 0)"/>
      <use xlink:href="#DejaVuSans-6f" transform="translate(767.089844 0)"/>
      <use xlink:href="#DejaVuSans-65" transform="translate(828.271484 0)"/>
      <use xlink:href="#DejaVuSans-66" transform="translate(889.794922 0)"/>
      <use xlink:href="#DejaVuSans-66" transform="translate(925 0)"/>
      <use xlink:href="#DejaVuSans-69" transform="translate(960.205078 0)"/>
      <use xlink:href="#DejaVuSans-63" transform="translate(987.988281 0)"/>
      <use xlink:href="#DejaVuSans-69" transform="translate(1042.96875 0)"/>
      <use xlink:href="#DejaVuSans-65" transform="translate(1070.751953 0)"/>
      <use xlink:href="#DejaVuSans-6e" transform="translate(1132.275391 0)"/>
      <use xlink:href="#DejaVuSans-74" transform="translate(1195.654297 0)"/>
     </g>
    </g>
   </g>
   <g id="line2d_28">
    <path d="M 184.799773 464.034875 
L 322.077498 464.034875 
" clip-path="url(#p3c6d678dee)" style="fill: none; stroke: #205ca8; stroke-width: 2.6; stroke-linecap: square"/>
   </g>
   <g id="line2d_29">
    <path d="M 322.077498 418.125722 
L 459.355223 418.125722 
" clip-path="url(#p3c6d678dee)" style="fill: none; stroke: #205ca8; stroke-width: 2.6; stroke-linecap: square"/>
   </g>
   <g id="line2d_30">
    <path d="M 459.355223 372.216569 
L 596.632948 372.216569 
" clip-path="url(#p3c6d678dee)" style="fill: none; stroke: #205ca8; stroke-width: 2.6; stroke-linecap: square"/>
   </g>
   <g id="line2d_31">
    <path d="M 596.632948 326.307417 
L 733.910673 326.307417 
" clip-path="url(#p3c6d678dee)" style="fill: none; stroke: #205ca8; stroke-width: 2.6; stroke-linecap: square"/>
   </g>
   <g id="line2d_32">
    <path d="M 184.799773 464.034875 
L 733.910673 280.398264 
" clip-path="url(#p3c6d678dee)" style="fill: none; stroke: #697684; stroke-width: 1.6; stroke-linecap: square"/>
   </g>
   <g id="patch_7">
    <path d="M 171.072 489.744 
L 171.072 273.0528 
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="patch_8">
    <path d="M 171.072 489.744 
L 750.384 489.744 
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="text_20">
    <!-- $p_0:\ [-1,-0.5)$ -->
    <g transform="translate(218.563635 479.643986) scale(0.09 -0.09)">
     <defs>
      <path id="DejaVuSans-Oblique-70" d="M 3175 2156 
Q 3175 2616 2975 2859 
Q 2775 3103 2400 3103 
Q 2144 3103 1911 2972 
Q 1678 2841 1497 2591 
Q 1319 2344 1212 1994 
Q 1106 1644 1106 1300 
Q 1106 863 1306 627 
Q 1506 391 1875 391 
Q 2147 391 2380 519 
Q 2613 647 2778 891 
Q 2956 1147 3065 1494 
Q 3175 1841 3175 2156 
z
M 1394 2969 
Q 1625 3272 1939 3428 
Q 2253 3584 2638 3584 
Q 3175 3584 3472 3232 
Q 3769 2881 3769 2247 
Q 3769 1728 3584 1258 
Q 3400 788 3053 416 
Q 2822 169 2531 39 
Q 2241 -91 1919 -91 
Q 1547 -91 1294 64 
Q 1041 219 916 525 
L 556 -1331 
L -19 -1331 
L 922 3500 
L 1497 3500 
L 1394 2969 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-2e" d="M 684 794 
L 1344 794 
L 1344 0 
L 684 0 
L 684 794 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-35" d="M 691 4666 
L 3169 4666 
L 3169 4134 
L 1269 4134 
L 1269 2991 
Q 1406 3038 1543 3061 
Q 1681 3084 1819 3084 
Q 2600 3084 3056 2656 
Q 3513 2228 3513 1497 
Q 3513 744 3044 326 
Q 2575 -91 1722 -91 
Q 1428 -91 1123 -41 
Q 819 9 494 109 
L 494 744 
Q 775 591 1075 516 
Q 1375 441 1709 441 
Q 2250 441 2565 725 
Q 2881 1009 2881 1497 
Q 2881 1984 2565 2268 
Q 2250 2553 1709 2553 
Q 1456 2553 1204 2497 
Q 953 2441 691 2322 
L 691 4666 
z
" transform="scale(0.015625)"/>
     </defs>
     <use xlink:href="#DejaVuSans-Oblique-70" transform="translate(0 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(63.476562 -16.390625) scale(0.7)"/>
     <use xlink:href="#DejaVuSans-3a" transform="translate(130.229492 0.015625)"/>
     <use xlink:href="#DejaVuSans-5b" transform="translate(215.873699 0.015625)"/>
     <use xlink:href="#DejaVuSans-2212" transform="translate(254.887371 0.015625)"/>
     <use xlink:href="#DejaVuSans-31" transform="translate(338.676433 0.015625)"/>
     <use xlink:href="#DejaVuSans-2c" transform="translate(402.29948 0.015625)"/>
     <use xlink:href="#DejaVuSans-2212" transform="translate(473.051433 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(576.322917 0.015625)"/>
     <use xlink:href="#DejaVuSans-2e" transform="translate(639.945964 0.015625)"/>
     <use xlink:href="#DejaVuSans-35" transform="translate(671.733074 0.015625)"/>
     <use xlink:href="#DejaVuSans-29" transform="translate(735.356121 0.015625)"/>
    </g>
   </g>
   <g id="text_21">
    <!-- $p_1:\ [-0.5,0)$ -->
    <g transform="translate(361.37636 479.643986) scale(0.09 -0.09)">
     <use xlink:href="#DejaVuSans-Oblique-70" transform="translate(0 0.015625)"/>
     <use xlink:href="#DejaVuSans-31" transform="translate(63.476562 -16.390625) scale(0.7)"/>
     <use xlink:href="#DejaVuSans-3a" transform="translate(130.229492 0.015625)"/>
     <use xlink:href="#DejaVuSans-5b" transform="translate(215.873699 0.015625)"/>
     <use xlink:href="#DejaVuSans-2212" transform="translate(254.887371 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(338.676433 0.015625)"/>
     <use xlink:href="#DejaVuSans-2e" transform="translate(402.29948 0.015625)"/>
     <use xlink:href="#DejaVuSans-35" transform="translate(434.086589 0.015625)"/>
     <use xlink:href="#DejaVuSans-2c" transform="translate(497.709636 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(548.979167 0.015625)"/>
     <use xlink:href="#DejaVuSans-29" transform="translate(612.602214 0.015625)"/>
    </g>
   </g>
   <g id="text_22">
    <!-- $p_2:\ [0,0.5)$ -->
    <g transform="translate(502.434085 479.643986) scale(0.09 -0.09)">
     <use xlink:href="#DejaVuSans-Oblique-70" transform="translate(0 0.015625)"/>
     <use xlink:href="#DejaVuSans-32" transform="translate(63.476562 -16.390625) scale(0.7)"/>
     <use xlink:href="#DejaVuSans-3a" transform="translate(130.229492 0.015625)"/>
     <use xlink:href="#DejaVuSans-5b" transform="translate(215.873699 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(254.887371 0.015625)"/>
     <use xlink:href="#DejaVuSans-2c" transform="translate(318.510417 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(369.779949 0.015625)"/>
     <use xlink:href="#DejaVuSans-2e" transform="translate(433.402996 0.015625)"/>
     <use xlink:href="#DejaVuSans-35" transform="translate(465.190105 0.015625)"/>
     <use xlink:href="#DejaVuSans-29" transform="translate(528.813152 0.015625)"/>
    </g>
   </g>
   <g id="text_23">
    <!-- $p_3:\ [0.5,1)$ -->
    <g transform="translate(639.71181 479.643986) scale(0.09 -0.09)">
     <defs>
      <path id="DejaVuSans-33" d="M 2597 2516 
Q 3050 2419 3304 2112 
Q 3559 1806 3559 1356 
Q 3559 666 3084 287 
Q 2609 -91 1734 -91 
Q 1441 -91 1130 -33 
Q 819 25 488 141 
L 488 750 
Q 750 597 1062 519 
Q 1375 441 1716 441 
Q 2309 441 2620 675 
Q 2931 909 2931 1356 
Q 2931 1769 2642 2001 
Q 2353 2234 1838 2234 
L 1294 2234 
L 1294 2753 
L 1863 2753 
Q 2328 2753 2575 2939 
Q 2822 3125 2822 3475 
Q 2822 3834 2567 4026 
Q 2313 4219 1838 4219 
Q 1578 4219 1281 4162 
Q 984 4106 628 3988 
L 628 4550 
Q 988 4650 1302 4700 
Q 1616 4750 1894 4750 
Q 2613 4750 3031 4423 
Q 3450 4097 3450 3541 
Q 3450 3153 3228 2886 
Q 3006 2619 2597 2516 
z
" transform="scale(0.015625)"/>
     </defs>
     <use xlink:href="#DejaVuSans-Oblique-70" transform="translate(0 0.015625)"/>
     <use xlink:href="#DejaVuSans-33" transform="translate(63.476562 -16.390625) scale(0.7)"/>
     <use xlink:href="#DejaVuSans-3a" transform="translate(130.229492 0.015625)"/>
     <use xlink:href="#DejaVuSans-5b" transform="translate(215.873699 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(254.887371 0.015625)"/>
     <use xlink:href="#DejaVuSans-2e" transform="translate(318.510417 0.015625)"/>
     <use xlink:href="#DejaVuSans-35" transform="translate(350.297527 0.015625)"/>
     <use xlink:href="#DejaVuSans-2c" transform="translate(413.920574 0.015625)"/>
     <use xlink:href="#DejaVuSans-31" transform="translate(465.190105 0.015625)"/>
     <use xlink:href="#DejaVuSans-29" transform="translate(528.813152 0.015625)"/>
    </g>
   </g>
   <g id="patch_9">
    <path d="M 603.894124 284.59899 
Q 667.904499 282.530868 730.797424 280.498851 
" style="fill: none; stroke: #b63831; stroke-linecap: round"/>
    <path d="M 726.328675 278.442084 
L 730.797424 280.498851 
L 726.470761 282.83979 
" style="fill: none; stroke: #b63831; stroke-linecap: round"/>
   </g>
   <g id="text_24">
    <!-- $p_4=E_1$: coefficient $1$ -->
    <g style="fill: #b63831" transform="translate(486.810768 289.580095) scale(0.11 -0.11)">
     <defs>
      <path id="DejaVuSans-34" d="M 2419 4116 
L 825 1625 
L 2419 1625 
L 2419 4116 
z
M 2253 4666 
L 3047 4666 
L 3047 1625 
L 3713 1625 
L 3713 1100 
L 3047 1100 
L 3047 0 
L 2419 0 
L 2419 1100 
L 313 1100 
L 313 1709 
L 2253 4666 
z
" transform="scale(0.015625)"/>
     </defs>
     <use xlink:href="#DejaVuSans-Oblique-70" transform="translate(0 0.015625)"/>
     <use xlink:href="#DejaVuSans-34" transform="translate(63.476562 -16.390625) scale(0.7)"/>
     <use xlink:href="#DejaVuSans-3d" transform="translate(130.229492 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-45" transform="translate(233.500977 0.015625)"/>
     <use xlink:href="#DejaVuSans-31" transform="translate(296.68457 -16.390625) scale(0.7)"/>
     <use xlink:href="#DejaVuSans-3a" transform="translate(343.955078 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(377.646484 0.015625)"/>
     <use xlink:href="#DejaVuSans-63" transform="translate(409.433594 0.015625)"/>
     <use xlink:href="#DejaVuSans-6f" transform="translate(464.414062 0.015625)"/>
     <use xlink:href="#DejaVuSans-65" transform="translate(525.595703 0.015625)"/>
     <use xlink:href="#DejaVuSans-66" transform="translate(587.119141 0.015625)"/>
     <use xlink:href="#DejaVuSans-66" transform="translate(622.324219 0.015625)"/>
     <use xlink:href="#DejaVuSans-69" transform="translate(657.529297 0.015625)"/>
     <use xlink:href="#DejaVuSans-63" transform="translate(685.3125 0.015625)"/>
     <use xlink:href="#DejaVuSans-69" transform="translate(740.292969 0.015625)"/>
     <use xlink:href="#DejaVuSans-65" transform="translate(768.076172 0.015625)"/>
     <use xlink:href="#DejaVuSans-6e" transform="translate(829.599609 0.015625)"/>
     <use xlink:href="#DejaVuSans-74" transform="translate(892.978516 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(932.1875 0.015625)"/>
     <use xlink:href="#DejaVuSans-31" transform="translate(963.974609 0.015625)"/>
    </g>
   </g>
   <g id="text_25">
    <!-- $h_m=\sum_{j=0}^{3}t_jp_j+1\cdot p_4$ -->
    <g transform="translate(198.527545 284.256488) scale(0.12 -0.12)">
     <defs>
      <path id="DejaVuSans-Oblique-6d" d="M 5747 2113 
L 5338 0 
L 4763 0 
L 5166 2094 
Q 5191 2228 5203 2325 
Q 5216 2422 5216 2491 
Q 5216 2772 5059 2928 
Q 4903 3084 4622 3084 
Q 4203 3084 3875 2770 
Q 3547 2456 3450 1953 
L 3066 0 
L 2491 0 
L 2900 2094 
Q 2925 2209 2937 2307 
Q 2950 2406 2950 2484 
Q 2950 2769 2794 2926 
Q 2638 3084 2363 3084 
Q 1938 3084 1609 2770 
Q 1281 2456 1184 1953 
L 800 0 
L 225 0 
L 909 3500 
L 1484 3500 
L 1375 2956 
Q 1609 3263 1923 3423 
Q 2238 3584 2597 3584 
Q 2978 3584 3223 3384 
Q 3469 3184 3519 2828 
Q 3781 3197 4126 3390 
Q 4472 3584 4856 3584 
Q 5306 3584 5551 3325 
Q 5797 3066 5797 2591 
Q 5797 2488 5784 2364 
Q 5772 2241 5747 2113 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSansDisplay-2211" d="M 244 6509 
L 5803 6509 
L 5803 5656 
L 1566 5656 
L 4534 2488 
L 1469 -888 
L 5919 -888 
L 5919 -1738 
L 109 -1738 
L 109 -1078 
L 3316 2463 
L 244 5728 
L 244 6509 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-Oblique-6a" d="M 928 3500 
L 1503 3500 
L 813 -63 
L 809 -78 
Q 694 -675 544 -897 
Q 403 -1106 132 -1218 
Q -138 -1331 -506 -1331 
L -722 -1331 
L -628 -844 
L -481 -844 
Q -144 -844 -1 -703 
Q 141 -563 238 -63 
L 928 3500 
z
M 1197 4863 
L 1772 4863 
L 1631 4134 
L 1056 4134 
L 1197 4863 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-22c5" d="M 684 2619 
L 1344 2619 
L 1344 1825 
L 684 1825 
L 684 2619 
z
" transform="scale(0.015625)"/>
     </defs>
     <use xlink:href="#DejaVuSans-Oblique-68" transform="translate(0 0.598437)"/>
     <use xlink:href="#DejaVuSans-Oblique-6d" transform="translate(63.378906 -15.807813) scale(0.7)"/>
     <use xlink:href="#DejaVuSans-3d" transform="translate(153.78418 0.598437)"/>
     <use xlink:href="#DejaVuSans-33" transform="translate(310.055664 122.046875) scale(0.7)"/>
     <use xlink:href="#DejaVuSansDisplay-2211" transform="translate(287.055664 0.598437)"/>
     <use xlink:href="#DejaVuSans-Oblique-6a" transform="translate(257.055664 -98.496875) scale(0.7)"/>
     <use xlink:href="#DejaVuSans-3d" transform="translate(290.141602 -98.496875) scale(0.7)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(362.431641 -98.496875) scale(0.7)"/>
     <use xlink:href="#DejaVuSans-Oblique-74" transform="translate(406.967773 0.598437)"/>
     <use xlink:href="#DejaVuSans-Oblique-6a" transform="translate(446.176758 -15.807813) scale(0.7)"/>
     <use xlink:href="#DejaVuSans-Oblique-70" transform="translate(468.359375 0.598437)"/>
     <use xlink:href="#DejaVuSans-Oblique-6a" transform="translate(531.835938 -15.807813) scale(0.7)"/>
     <use xlink:href="#DejaVuSans-2b" transform="translate(573.500977 0.598437)"/>
     <use xlink:href="#DejaVuSans-31" transform="translate(676.772461 0.598437)"/>
     <use xlink:href="#DejaVuSans-22c5" transform="translate(759.87793 0.598437)"/>
     <use xlink:href="#DejaVuSans-Oblique-70" transform="translate(811.147461 0.598437)"/>
     <use xlink:href="#DejaVuSans-34" transform="translate(874.624023 -15.807813) scale(0.7)"/>
    </g>
    <!-- $0\leq h-h_m\leq\frac{1}{2}\,1$ -->
    <g transform="translate(198.527545 311.616488) scale(0.12 -0.12)">
     <defs>
      <path id="DejaVuSans-2264" d="M 4684 3175 
L 1684 2309 
L 4684 1453 
L 4684 897 
L 678 2047 
L 678 2578 
L 4684 3725 
L 4684 3175 
z
M 678 531 
L 4684 531 
L 4684 0 
L 678 0 
L 678 531 
z
" transform="scale(0.015625)"/>
     </defs>
     <use xlink:href="#DejaVuSans-30" transform="translate(0 0.16875)"/>
     <use xlink:href="#DejaVuSans-2264" transform="translate(83.105469 0.16875)"/>
     <use xlink:href="#DejaVuSans-Oblique-68" transform="translate(186.376953 0.16875)"/>
     <use xlink:href="#DejaVuSans-2212" transform="translate(269.238281 0.16875)"/>
     <use xlink:href="#DejaVuSans-Oblique-68" transform="translate(372.509766 0.16875)"/>
     <use xlink:href="#DejaVuSans-Oblique-6d" transform="translate(435.888672 -16.2375) scale(0.7)"/>
     <use xlink:href="#DejaVuSans-2264" transform="translate(526.293945 0.16875)"/>
     <use xlink:href="#DejaVuSans-31" transform="translate(629.56543 43.965625) scale(0.7)"/>
     <use xlink:href="#DejaVuSans-32" transform="translate(629.56543 -39.2375) scale(0.7)"/>
     <use xlink:href="#DejaVuSans-31" transform="translate(702.837239 0.16875)"/>
     <path d="M 629.56543 18.965625 
L 629.56543 25.215625 
L 674.101562 25.215625 
L 674.101562 18.965625 
L 629.56543 18.965625 
z
"/>
    </g>
   </g>
   <g id="text_26">
    <!-- Finite approximation: $R=1$, $m=4$, $\Delta=2R/m=1/2$ -->
    <g transform="translate(297.903 261.0528) scale(0.13 -0.13)">
     <defs>
      <path id="DejaVuSans-46" d="M 628 4666 
L 3309 4666 
L 3309 4134 
L 1259 4134 
L 1259 2759 
L 3109 2759 
L 3109 2228 
L 1259 2228 
L 1259 0 
L 628 0 
L 628 4666 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-78" d="M 3513 3500 
L 2247 1797 
L 3578 0 
L 2900 0 
L 1881 1375 
L 863 0 
L 184 0 
L 1544 1831 
L 300 3500 
L 978 3500 
L 1906 2253 
L 2834 3500 
L 3513 3500 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-6d" d="M 3328 2828 
Q 3544 3216 3844 3400 
Q 4144 3584 4550 3584 
Q 5097 3584 5394 3201 
Q 5691 2819 5691 2113 
L 5691 0 
L 5113 0 
L 5113 2094 
Q 5113 2597 4934 2840 
Q 4756 3084 4391 3084 
Q 3944 3084 3684 2787 
Q 3425 2491 3425 1978 
L 3425 0 
L 2847 0 
L 2847 2094 
Q 2847 2600 2669 2842 
Q 2491 3084 2119 3084 
Q 1678 3084 1418 2786 
Q 1159 2488 1159 1978 
L 1159 0 
L 581 0 
L 581 3500 
L 1159 3500 
L 1159 2956 
Q 1356 3278 1631 3431 
Q 1906 3584 2284 3584 
Q 2666 3584 2933 3390 
Q 3200 3197 3328 2828 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-Oblique-52" d="M 1613 4147 
L 1294 2491 
L 2106 2491 
Q 2584 2491 2879 2755 
Q 3175 3019 3175 3444 
Q 3175 3784 2976 3965 
Q 2778 4147 2406 4147 
L 1613 4147 
z
M 2772 2241 
Q 2972 2194 3105 2009 
Q 3238 1825 3413 1275 
L 3809 0 
L 3144 0 
L 2778 1197 
Q 2638 1659 2453 1815 
Q 2269 1972 1888 1972 
L 1191 1972 
L 806 0 
L 172 0 
L 1081 4666 
L 2503 4666 
Q 3150 4666 3495 4373 
Q 3841 4081 3841 3531 
Q 3841 3044 3547 2687 
Q 3253 2331 2772 2241 
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-394" d="M 2188 4044 
L 906 525 
L 3472 525 
L 2188 4044 
z
M 50 0 
L 1831 4666 
L 2547 4666 
L 4325 0 
L 50 0 
z
" transform="scale(0.015625)"/>
     </defs>
     <use xlink:href="#DejaVuSans-46" transform="translate(0 0.015625)"/>
     <use xlink:href="#DejaVuSans-69" transform="translate(57.519531 0.015625)"/>
     <use xlink:href="#DejaVuSans-6e" transform="translate(85.302734 0.015625)"/>
     <use xlink:href="#DejaVuSans-69" transform="translate(148.681641 0.015625)"/>
     <use xlink:href="#DejaVuSans-74" transform="translate(176.464844 0.015625)"/>
     <use xlink:href="#DejaVuSans-65" transform="translate(215.673828 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(277.197266 0.015625)"/>
     <use xlink:href="#DejaVuSans-61" transform="translate(308.984375 0.015625)"/>
     <use xlink:href="#DejaVuSans-70" transform="translate(370.263672 0.015625)"/>
     <use xlink:href="#DejaVuSans-70" transform="translate(433.740234 0.015625)"/>
     <use xlink:href="#DejaVuSans-72" transform="translate(497.216797 0.015625)"/>
     <use xlink:href="#DejaVuSans-6f" transform="translate(538.330078 0.015625)"/>
     <use xlink:href="#DejaVuSans-78" transform="translate(599.511719 0.015625)"/>
     <use xlink:href="#DejaVuSans-69" transform="translate(658.691406 0.015625)"/>
     <use xlink:href="#DejaVuSans-6d" transform="translate(686.474609 0.015625)"/>
     <use xlink:href="#DejaVuSans-61" transform="translate(783.886719 0.015625)"/>
     <use xlink:href="#DejaVuSans-74" transform="translate(845.166016 0.015625)"/>
     <use xlink:href="#DejaVuSans-69" transform="translate(884.375 0.015625)"/>
     <use xlink:href="#DejaVuSans-6f" transform="translate(912.158203 0.015625)"/>
     <use xlink:href="#DejaVuSans-6e" transform="translate(973.339844 0.015625)"/>
     <use xlink:href="#DejaVuSans-3a" transform="translate(1036.71875 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(1070.410156 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-52" transform="translate(1102.197266 0.015625)"/>
     <use xlink:href="#DejaVuSans-3d" transform="translate(1191.162109 0.015625)"/>
     <use xlink:href="#DejaVuSans-31" transform="translate(1294.433594 0.015625)"/>
     <use xlink:href="#DejaVuSans-2c" transform="translate(1358.056641 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(1389.84375 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-6d" transform="translate(1421.630859 0.015625)"/>
     <use xlink:href="#DejaVuSans-3d" transform="translate(1538.525391 0.015625)"/>
     <use xlink:href="#DejaVuSans-34" transform="translate(1641.796875 0.015625)"/>
     <use xlink:href="#DejaVuSans-2c" transform="translate(1705.419922 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(1737.207031 0.015625)"/>
     <use xlink:href="#DejaVuSans-394" transform="translate(1768.994141 0.015625)"/>
     <use xlink:href="#DejaVuSans-3d" transform="translate(1856.884766 0.015625)"/>
     <use xlink:href="#DejaVuSans-32" transform="translate(1960.15625 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-52" transform="translate(2023.779297 0.015625)"/>
     <use xlink:href="#DejaVuSans-2f" transform="translate(2093.261719 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-6d" transform="translate(2126.953125 0.015625)"/>
     <use xlink:href="#DejaVuSans-3d" transform="translate(2243.847656 0.015625)"/>
     <use xlink:href="#DejaVuSans-31" transform="translate(2347.119141 0.015625)"/>
     <use xlink:href="#DejaVuSans-2f" transform="translate(2410.742188 0.015625)"/>
     <use xlink:href="#DejaVuSans-32" transform="translate(2440.808594 0.015625)"/>
    </g>
   </g>
   <g id="line2d_33">
    <defs>
     <path id="m190d675860" d="M 0 3 
C 0.795609 3 1.55874 2.683901 2.12132 2.12132 
C 2.683901 1.55874 3 0.795609 3 0 
C 3 -0.795609 2.683901 -1.55874 2.12132 -2.12132 
C 1.55874 -2.683901 0.795609 -3 0 -3 
C -0.795609 -3 -1.55874 -2.683901 -2.12132 -2.12132 
C -2.683901 -1.55874 -3 -0.795609 -3 0 
C -3 0.795609 -2.683901 1.55874 -2.12132 2.12132 
C -1.55874 2.683901 -0.795609 3 0 3 
z
" style="stroke: #205ca8"/>
    </defs>
    <g clip-path="url(#p3c6d678dee)">
     <use xlink:href="#m190d675860" x="184.799773" y="464.034875" style="fill: #205ca8; stroke: #205ca8"/>
    </g>
   </g>
   <g id="line2d_34">
    <defs>
     <path id="m58dbf5a597" d="M 0 3 
C 0.795609 3 1.55874 2.683901 2.12132 2.12132 
C 2.683901 1.55874 3 0.795609 3 0 
C 3 -0.795609 2.683901 -1.55874 2.12132 -2.12132 
C 1.55874 -2.683901 0.795609 -3 0 -3 
C -0.795609 -3 -1.55874 -2.683901 -2.12132 -2.12132 
C -2.683901 -1.55874 -3 -0.795609 -3 0 
C -3 0.795609 -2.683901 1.55874 -2.12132 2.12132 
C -1.55874 2.683901 -0.795609 3 0 3 
z
" style="stroke: #205ca8; stroke-width: 1.4"/>
    </defs>
    <g clip-path="url(#p3c6d678dee)">
     <use xlink:href="#m58dbf5a597" x="322.077498" y="464.034875" style="fill: #ffffff; stroke: #205ca8; stroke-width: 1.4"/>
    </g>
   </g>
   <g id="line2d_35">
    <g clip-path="url(#p3c6d678dee)">
     <use xlink:href="#m190d675860" x="322.077498" y="418.125722" style="fill: #205ca8; stroke: #205ca8"/>
    </g>
   </g>
   <g id="line2d_36">
    <g clip-path="url(#p3c6d678dee)">
     <use xlink:href="#m58dbf5a597" x="459.355223" y="418.125722" style="fill: #ffffff; stroke: #205ca8; stroke-width: 1.4"/>
    </g>
   </g>
   <g id="line2d_37">
    <g clip-path="url(#p3c6d678dee)">
     <use xlink:href="#m190d675860" x="459.355223" y="372.216569" style="fill: #205ca8; stroke: #205ca8"/>
    </g>
   </g>
   <g id="line2d_38">
    <g clip-path="url(#p3c6d678dee)">
     <use xlink:href="#m58dbf5a597" x="596.632948" y="372.216569" style="fill: #ffffff; stroke: #205ca8; stroke-width: 1.4"/>
    </g>
   </g>
   <g id="line2d_39">
    <g clip-path="url(#p3c6d678dee)">
     <use xlink:href="#m190d675860" x="596.632948" y="326.307417" style="fill: #205ca8; stroke: #205ca8"/>
    </g>
   </g>
   <g id="line2d_40">
    <g clip-path="url(#p3c6d678dee)">
     <use xlink:href="#m58dbf5a597" x="733.910673" y="326.307417" style="fill: #ffffff; stroke: #205ca8; stroke-width: 1.4"/>
    </g>
   </g>
   <g id="line2d_41">
    <defs>
     <path id="ma6f3eeb5d4" d="M 0 4 
C 1.060812 4 2.078319 3.578535 2.828427 2.828427 
C 3.578535 2.078319 4 1.060812 4 0 
C 4 -1.060812 3.578535 -2.078319 2.828427 -2.828427 
C 2.078319 -3.578535 1.060812 -4 0 -4 
C -1.060812 -4 -2.078319 -3.578535 -2.828427 -2.828427 
C -3.578535 -2.078319 -4 -1.060812 -4 0 
C -4 1.060812 -3.578535 2.078319 -2.828427 2.828427 
C -2.078319 3.578535 -1.060812 4 0 4 
z
" style="stroke: #b63831"/>
    </defs>
    <g clip-path="url(#p3c6d678dee)">
     <use xlink:href="#ma6f3eeb5d4" x="733.910673" y="280.398264" style="fill: #b63831; stroke: #b63831"/>
    </g>
   </g>
  </g>
  <g id="text_27">
   <!-- Endpoint schematic and scalar example of S01–S03. The norm bound is proved for every bounded selfadjoint operator. -->
   <g style="fill: #364252" transform="translate(90.488281 533.52) scale(0.1 -0.1)">
    <defs>
     <path id="DejaVuSans-45" d="M 628 4666 
L 3578 4666 
L 3578 4134 
L 1259 4134 
L 1259 2753 
L 3481 2753 
L 3481 2222 
L 1259 2222 
L 1259 531 
L 3634 531 
L 3634 0 
L 628 0 
L 628 4666 
z
" transform="scale(0.015625)"/>
     <path id="DejaVuSans-2013" d="M 313 1978 
L 2888 1978 
L 2888 1528 
L 313 1528 
L 313 1978 
z
" transform="scale(0.015625)"/>
     <path id="DejaVuSans-54" d="M -19 4666 
L 3928 4666 
L 3928 4134 
L 2272 4134 
L 2272 0 
L 1638 0 
L 1638 4134 
L -19 4134 
L -19 4666 
z
" transform="scale(0.015625)"/>
     <path id="DejaVuSans-62" d="M 3116 1747 
Q 3116 2381 2855 2742 
Q 2594 3103 2138 3103 
Q 1681 3103 1420 2742 
Q 1159 2381 1159 1747 
Q 1159 1113 1420 752 
Q 1681 391 2138 391 
Q 2594 391 2855 752 
Q 3116 1113 3116 1747 
z
M 1159 2969 
Q 1341 3281 1617 3432 
Q 1894 3584 2278 3584 
Q 2916 3584 3314 3078 
Q 3713 2572 3713 1747 
Q 3713 922 3314 415 
Q 2916 -91 2278 -91 
Q 1894 -91 1617 61 
Q 1341 213 1159 525 
L 1159 0 
L 581 0 
L 581 4863 
L 1159 4863 
L 1159 2969 
z
" transform="scale(0.015625)"/>
     <path id="DejaVuSans-79" d="M 2059 -325 
Q 1816 -950 1584 -1140 
Q 1353 -1331 966 -1331 
L 506 -1331 
L 506 -850 
L 844 -850 
Q 1081 -850 1212 -737 
Q 1344 -625 1503 -206 
L 1606 56 
L 191 3500 
L 800 3500 
L 1894 763 
L 2988 3500 
L 3597 3500 
L 2059 -325 
z
" transform="scale(0.015625)"/>
     <path id="DejaVuSans-6a" d="M 603 3500 
L 1178 3500 
L 1178 -63 
Q 1178 -731 923 -1031 
Q 669 -1331 103 -1331 
L -116 -1331 
L -116 -844 
L 38 -844 
Q 366 -844 484 -692 
Q 603 -541 603 -63 
L 603 3500 
z
M 603 4863 
L 1178 4863 
L 1178 4134 
L 603 4134 
L 603 4863 
z
" transform="scale(0.015625)"/>
    </defs>
    <use xlink:href="#DejaVuSans-45"/>
    <use xlink:href="#DejaVuSans-6e" transform="translate(63.183594 0)"/>
    <use xlink:href="#DejaVuSans-64" transform="translate(126.5625 0)"/>
    <use xlink:href="#DejaVuSans-70" transform="translate(190.039062 0)"/>
    <use xlink:href="#DejaVuSans-6f" transform="translate(253.515625 0)"/>
    <use xlink:href="#DejaVuSans-69" transform="translate(314.697266 0)"/>
    <use xlink:href="#DejaVuSans-6e" transform="translate(342.480469 0)"/>
    <use xlink:href="#DejaVuSans-74" transform="translate(405.859375 0)"/>
    <use xlink:href="#DejaVuSans-20" transform="translate(445.068359 0)"/>
    <use xlink:href="#DejaVuSans-73" transform="translate(476.855469 0)"/>
    <use xlink:href="#DejaVuSans-63" transform="translate(528.955078 0)"/>
    <use xlink:href="#DejaVuSans-68" transform="translate(583.935547 0)"/>
    <use xlink:href="#DejaVuSans-65" transform="translate(647.314453 0)"/>
    <use xlink:href="#DejaVuSans-6d" transform="translate(708.837891 0)"/>
    <use xlink:href="#DejaVuSans-61" transform="translate(806.25 0)"/>
    <use xlink:href="#DejaVuSans-74" transform="translate(867.529297 0)"/>
    <use xlink:href="#DejaVuSans-69" transform="translate(906.738281 0)"/>
    <use xlink:href="#DejaVuSans-63" transform="translate(934.521484 0)"/>
    <use xlink:href="#DejaVuSans-20" transform="translate(989.501953 0)"/>
    <use xlink:href="#DejaVuSans-61" transform="translate(1021.289062 0)"/>
    <use xlink:href="#DejaVuSans-6e" transform="translate(1082.568359 0)"/>
    <use xlink:href="#DejaVuSans-64" transform="translate(1145.947266 0)"/>
    <use xlink:href="#DejaVuSans-20" transform="translate(1209.423828 0)"/>
    <use xlink:href="#DejaVuSans-73" transform="translate(1241.210938 0)"/>
    <use xlink:href="#DejaVuSans-63" transform="translate(1293.310547 0)"/>
    <use xlink:href="#DejaVuSans-61" transform="translate(1348.291016 0)"/>
    <use xlink:href="#DejaVuSans-6c" transform="translate(1409.570312 0)"/>
    <use xlink:href="#DejaVuSans-61" transform="translate(1437.353516 0)"/>
    <use xlink:href="#DejaVuSans-72" transform="translate(1498.632812 0)"/>
    <use xlink:href="#DejaVuSans-20" transform="translate(1539.746094 0)"/>
    <use xlink:href="#DejaVuSans-65" transform="translate(1571.533203 0)"/>
    <use xlink:href="#DejaVuSans-78" transform="translate(1631.306641 0)"/>
    <use xlink:href="#DejaVuSans-61" transform="translate(1690.486328 0)"/>
    <use xlink:href="#DejaVuSans-6d" transform="translate(1751.765625 0)"/>
    <use xlink:href="#DejaVuSans-70" transform="translate(1849.177734 0)"/>
    <use xlink:href="#DejaVuSans-6c" transform="translate(1912.654297 0)"/>
    <use xlink:href="#DejaVuSans-65" transform="translate(1940.4375 0)"/>
    <use xlink:href="#DejaVuSans-20" transform="translate(2001.960938 0)"/>
    <use xlink:href="#DejaVuSans-6f" transform="translate(2033.748047 0)"/>
    <use xlink:href="#DejaVuSans-66" transform="translate(2094.929688 0)"/>
    <use xlink:href="#DejaVuSans-20" transform="translate(2130.134766 0)"/>
    <use xlink:href="#DejaVuSans-53" transform="translate(2161.921875 0)"/>
    <use xlink:href="#DejaVuSans-30" transform="translate(2225.398438 0)"/>
    <use xlink:href="#DejaVuSans-31" transform="translate(2289.021484 0)"/>
    <use xlink:href="#DejaVuSans-2013" transform="translate(2352.644531 0)"/>
    <use xlink:href="#DejaVuSans-53" transform="translate(2402.644531 0)"/>
    <use xlink:href="#DejaVuSans-30" transform="translate(2466.121094 0)"/>
    <use xlink:href="#DejaVuSans-33" transform="translate(2529.744141 0)"/>
    <use xlink:href="#DejaVuSans-2e" transform="translate(2593.367188 0)"/>
    <use xlink:href="#DejaVuSans-20" transform="translate(2625.154297 0)"/>
    <use xlink:href="#DejaVuSans-54" transform="translate(2656.941406 0)"/>
    <use xlink:href="#DejaVuSans-68" transform="translate(2718.025391 0)"/>
    <use xlink:href="#DejaVuSans-65" transform="translate(2781.404297 0)"/>
    <use xlink:href="#DejaVuSans-20" transform="translate(2842.927734 0)"/>
    <use xlink:href="#DejaVuSans-6e" transform="translate(2874.714844 0)"/>
    <use xlink:href="#DejaVuSans-6f" transform="translate(2938.09375 0)"/>
    <use xlink:href="#DejaVuSans-72" transform="translate(2999.275391 0)"/>
    <use xlink:href="#DejaVuSans-6d" transform="translate(3038.638672 0)"/>
    <use xlink:href="#DejaVuSans-20" transform="translate(3136.050781 0)"/>
    <use xlink:href="#DejaVuSans-62" transform="translate(3167.837891 0)"/>
    <use xlink:href="#DejaVuSans-6f" transform="translate(3231.314453 0)"/>
    <use xlink:href="#DejaVuSans-75" transform="translate(3292.496094 0)"/>
    <use xlink:href="#DejaVuSans-6e" transform="translate(3355.875 0)"/>
    <use xlink:href="#DejaVuSans-64" transform="translate(3419.253906 0)"/>
    <use xlink:href="#DejaVuSans-20" transform="translate(3482.730469 0)"/>
    <use xlink:href="#DejaVuSans-69" transform="translate(3514.517578 0)"/>
    <use xlink:href="#DejaVuSans-73" transform="translate(3542.300781 0)"/>
    <use xlink:href="#DejaVuSans-20" transform="translate(3594.400391 0)"/>
    <use xlink:href="#DejaVuSans-70" transform="translate(3626.1875 0)"/>
    <use xlink:href="#DejaVuSans-72" transform="translate(3689.664062 0)"/>
    <use xlink:href="#DejaVuSans-6f" transform="translate(3728.527344 0)"/>
    <use xlink:href="#DejaVuSans-76" transform="translate(3789.708984 0)"/>
    <use xlink:href="#DejaVuSans-65" transform="translate(3848.888672 0)"/>
    <use xlink:href="#DejaVuSans-64" transform="translate(3910.412109 0)"/>
    <use xlink:href="#DejaVuSans-20" transform="translate(3973.888672 0)"/>
    <use xlink:href="#DejaVuSans-66" transform="translate(4005.675781 0)"/>
    <use xlink:href="#DejaVuSans-6f" transform="translate(4040.880859 0)"/>
    <use xlink:href="#DejaVuSans-72" transform="translate(4102.0625 0)"/>
    <use xlink:href="#DejaVuSans-20" transform="translate(4143.175781 0)"/>
    <use xlink:href="#DejaVuSans-65" transform="translate(4174.962891 0)"/>
    <use xlink:href="#DejaVuSans-76" transform="translate(4236.486328 0)"/>
    <use xlink:href="#DejaVuSans-65" transform="translate(4295.666016 0)"/>
    <use xlink:href="#DejaVuSans-72" transform="translate(4357.189453 0)"/>
    <use xlink:href="#DejaVuSans-79" transform="translate(4398.302734 0)"/>
    <use xlink:href="#DejaVuSans-20" transform="translate(4457.482422 0)"/>
    <use xlink:href="#DejaVuSans-62" transform="translate(4489.269531 0)"/>
    <use xlink:href="#DejaVuSans-6f" transform="translate(4552.746094 0)"/>
    <use xlink:href="#DejaVuSans-75" transform="translate(4613.927734 0)"/>
    <use xlink:href="#DejaVuSans-6e" transform="translate(4677.306641 0)"/>
    <use xlink:href="#DejaVuSans-64" transform="translate(4740.685547 0)"/>
    <use xlink:href="#DejaVuSans-65" transform="translate(4804.162109 0)"/>
    <use xlink:href="#DejaVuSans-64" transform="translate(4865.685547 0)"/>
    <use xlink:href="#DejaVuSans-20" transform="translate(4929.162109 0)"/>
    <use xlink:href="#DejaVuSans-73" transform="translate(4960.949219 0)"/>
    <use xlink:href="#DejaVuSans-65" transform="translate(5013.048828 0)"/>
    <use xlink:href="#DejaVuSans-6c" transform="translate(5074.572266 0)"/>
    <use xlink:href="#DejaVuSans-66" transform="translate(5102.355469 0)"/>
    <use xlink:href="#DejaVuSans-61" transform="translate(5137.560547 0)"/>
    <use xlink:href="#DejaVuSans-64" transform="translate(5198.839844 0)"/>
    <use xlink:href="#DejaVuSans-6a" transform="translate(5262.316406 0)"/>
    <use xlink:href="#DejaVuSans-6f" transform="translate(5290.099609 0)"/>
    <use xlink:href="#DejaVuSans-69" transform="translate(5351.28125 0)"/>
    <use xlink:href="#DejaVuSans-6e" transform="translate(5379.064453 0)"/>
    <use xlink:href="#DejaVuSans-74" transform="translate(5442.443359 0)"/>
    <use xlink:href="#DejaVuSans-20" transform="translate(5481.652344 0)"/>
    <use xlink:href="#DejaVuSans-6f" transform="translate(5513.439453 0)"/>
    <use xlink:href="#DejaVuSans-70" transform="translate(5574.621094 0)"/>
    <use xlink:href="#DejaVuSans-65" transform="translate(5638.097656 0)"/>
    <use xlink:href="#DejaVuSans-72" transform="translate(5699.621094 0)"/>
    <use xlink:href="#DejaVuSans-61" transform="translate(5740.734375 0)"/>
    <use xlink:href="#DejaVuSans-74" transform="translate(5802.013672 0)"/>
    <use xlink:href="#DejaVuSans-6f" transform="translate(5841.222656 0)"/>
    <use xlink:href="#DejaVuSans-72" transform="translate(5902.404297 0)"/>
    <use xlink:href="#DejaVuSans-2e" transform="translate(5934.392578 0)"/>
   </g>
  </g>
 </g>
 <defs>
  <clipPath id="pd88586373a">
   <rect x="171.072" y="38.304" width="579.312" height="144.4608"/>
  </clipPath>
  <clipPath id="p3c6d678dee">
   <rect x="171.072" y="273.0528" width="579.312" height="216.6912"/>
  </clipPath>
 </defs>
</svg>

The upper panel shows the endpoint conventions proved in S01–S02. The lower panel shows the scalar example \(R=1,m=4\) of S03: each half-open interval receives its lower endpoint coefficient, and \(\{1\}\) receives coefficient one. The shaded difference is at most \(\Delta=1/2\). These scalar diagrams explain the operator construction from [continuous positive parts and [range supports](regular-group-operator-foundations.md#h02); the displayed norm estimate is proved for every bounded selfadjoint operator.

<a id="s04"></a>
## S04. Central cuts for a positive contraction

Let \(a\in Z(M)\) satisfy \(0\le a\le1\), and let \(N\ge1\) be an integer. Apply S01 to \(a\), writing its projections as \(Q_t\). Then
\[
 z_k=Q_{k/N}-Q_{(k+1)/N}\quad(0\le k<N),
 \qquad z_N=Q_1=E_1
\]
are central, mutually orthogonal, and sum to \(1\), because \(Q_0=1\) and \(P_1=0\). They satisfy
\[
 \frac{k}{N}z_k\le az_k\le\frac{k+1}{N}z_k
 \quad(0\le k<N),\qquad az_N=z_N.
\]
The first pieces have the exact half-open convention \([k/N,(k+1)/N)\); the final piece is the eigenspace at \(1\).

For the averaging argument, take \(a=T(e)\), where \(e\) is a projection and \(T:M\to Z(M)\) is a positive unital centre-valued trace. Positivity gives \(0\le T(e)\le1\), so all these cuts apply. If \(T\) is faithful and centre-linear, then the last piece has the additional property
\[
 T((1-e)z_N)=z_N-T(e)z_N=0.
\]
The operator \((1-e)z_N\) is positive, since \(z_N\) is central. Faithfulness gives \((1-e)z_N=0\), or \(ez_N=z_N\). The cuts themselves do not require faithfulness.

<a id="s05"></a>
## S05. Integer central ranks without a representation theorem

Let \(D\) be a nonzero unital abelian \(C^*\)-algebra, let \(n\ge1\), and let \(p=(p_{ij})\) be a projection in \(M_n(D)\). Its ordinary diagonal trace is
\[
 d=\sum_{i=1}^n p_{ii}\in D.
\]
It is selfadjoint. The full character construction in [T05a and CS01–CS06](regular-group-operator-foundations.md#t05a) supplies characters separating the elements of \(D\), and every character \(\chi\) extends entrywise to a unital \(*\)-homomorphism \(\chi_n:M_n(D)\to M_n(\mathbb C)\).

For each \(\chi\), the numerical matrix \(\chi_n(p)\) is a selfadjoint projection. Its trace is an integer between zero and \(n\). Here is the finite-dimensional argument. Apply Gram–Schmidt successively to its images of the standard basis vectors, discarding zero remainders, to obtain an orthonormal basis for its range. Do the same with the images under its complementary projection to obtain an orthonormal basis for its kernel. These two subspaces are orthogonal and together span \(\mathbb C^n\). In the combined basis the projection has \(r\) diagonal entries equal to one and the others zero. Its trace is unchanged by this basis change, since finite sums show \(\operatorname{Tr}(AB)=\operatorname{Tr}(BA)\), and hence \(\operatorname{Tr}(U^*PU)=\operatorname{Tr}(PUU^*)\). Thus
\[
 \chi(d)=\operatorname{Tr}(\chi_n(p))\in\{0,1,\ldots,n\}.
\]

Put \(q(X)=\prod_{j=0}^n(X-j)\). Every character vanishes on \(q(d)\), so character separation gives \(q(d)=0\). This proves the spectrum assertion directly. If \(\lambda\notin\{0,\ldots,n\}\), the polynomial identity
\[
 q(X)-q(\lambda)=(X-\lambda)r_\lambda(X)
\]
gives
\[
 (d-\lambda1)\left(-\frac{r_\lambda(d)}{q(\lambda)}\right)
 =\left(-\frac{r_\lambda(d)}{q(\lambda)}\right)(d-\lambda1)=1.
\]
Consequently \(\sigma_D(d)\subseteq\{0,1,\ldots,n\}\).

There is also an explicit decomposition into central rank pieces. For \(0\le k\le n\), let
\[
 L_k(X)=\prod_{\substack{0\le j\le n\\j\ne k}}
 \frac{X-j}{k-j},\qquad w_k=L_k(d).
\]
These have real coefficients, so the \(w_k\) are selfadjoint. For each character,
\[
 \chi(w_k)=
 \begin{cases}1,&\chi(d)=k,\\0,&\chi(d)\ne k.\end{cases}
\]
Applying character separation to each algebraic identity gives
\[
 w_k^2=w_k,\quad w_kw_l=0\ (k\ne l),\quad
 \sum_{k=0}^n w_k=1,\quad (d-k1)w_k=0.
\]
Therefore
\[
 d=\sum_{k=0}^n k w_k,
 \qquad 0\le d\le n1.
\]
Some rank pieces may be zero. When \(D=Z(M)\), these are central projections in \(M\). If the already established matrix-corner trace formula is \(T(p)=d/n\), they satisfy \(T(p)w_k=(k/n)w_k\), exactly as needed by finite matrix averaging. This deduction uses that formula as a separate hypothesis; it does not establish the centre-valued trace or the alignment of equivalent projections. No normality of the characters is needed. If \(D\) is the zero algebra, \(p=d=w_k=0\) and the assertion is immediate, without characters.

<a id="s06"></a>
## S06. Projections determine bounded linear functionals

Let \(f,g:M\to\mathbb C\) be bounded linear functionals agreeing on every projection. For \(h=h^*\), S03 gives finite projection combinations \(h_m\) with \(\|h-h_m\|\to0\). Linearity gives \(f(h_m)=g(h_m)\), and
\[
 |f(h)-g(h)|\le(\|f\|+\|g\|)\|h-h_m\|\longrightarrow0.
\]
Every \(x\in M\) is \((x+x^*)/2+i(x-x^*)/(2i)\), a sum of two selfadjoint parts, so \(f=g\) on \(M\).

For completeness, a positive complex-linear functional \(\varphi\) with \(\varphi(1)=1\) is automatically bounded with norm one. Positive parts give \(\varphi(h)\in\mathbb R\) for selfadjoint \(h\), and then \(\varphi(x^*)=\overline{\varphi(x)}\). The sesquilinear form \((a,b)\mapsto\varphi(b^*a)\) is positive. Put \(\alpha=\varphi(b^*a)\), \(\beta=\varphi(b^*b)\), and \(\gamma=\varphi(a^*a)\). For every complex \(t\), positivity gives
\[
 0\le\gamma-\overline t\alpha-t\overline\alpha+|t|^2\beta.
\]
If \(\beta>0\), take \(t=\alpha/\beta\). If \(\beta=0\), take \(t=r\alpha\) with \(r>0\); then \(0\le\gamma-2r|\alpha|^2\) for every \(r\), forcing \(\alpha=0\). These two cases prove
\[
 |\varphi(b^*a)|^2\le\varphi(a^*a)\varphi(b^*b).
\]
Set \(b=1\). Since \(0\le a^*a\le\|a\|^2 1\),
\[
 |\varphi(a)|^2\le\varphi(a^*a)\le\|a\|^2.
\]
Thus \(\|\varphi\|\le1\), and evaluation at \(1\) gives equality.

In particular, if \(\rho\) is a tracial state and \(T:M\to Z(M)\) is positive and unital, then \(\rho\circ T\) is also a positive unital scalar functional, hence has norm one. Agreement of \(\rho\) and \(\rho\circ T\) on projections implies agreement everywhere by S03 and the estimate
\[
 |\rho(h)-\rho(T(h))|\le2\|h-h_m\|.
\]
This estimate needs neither normality of \(\rho\) nor a separately imported norm estimate for \(T\).

## Constructing the normal center-valued trace

The proofs in this section use C05–C06, D10 and the support-based finite spectral approximation S01–S03. They do not presuppose a scalar trace on a general finite algebra.

<a id="center-map-norm"></a>
**Norm of a positive central map (CN).** If a positive linear map \(F:A\to Z\) has commutative unital C*-algebra range and \(F(1)=c\ge0\), then \(\|F\|=\|c\|\).

**Proof.** For every character \(\chi\) of \(Z\), \(\chi F\) is a positive scalar functional. Its positive-form Cauchy–Schwarz inequality gives
\[
|\chi F(x)|^2\le \chi(c)\,\chi F(x^*x)
\le \chi(c)^2\|x\|^2.
\]
The inequality \(x^*x\le\|x\|^2 1\) is F08. Characters preserve positivity by CS04 and norm \(Z\) by CS05 of [Regular-group operator foundations](regular-group-operator-foundations.md#t05a). Hence \(\|F(x)\|\le\|c\|\|x\|\); evaluation at the unit proves equality. The positive-form Cauchy–Schwarz argument, including its zero-denominator case, is the quotient argument in GNS. \(\square\)

<a id="central-map-assembly"></a>
**Assembly on central components (CA).** Suppose \((z_\alpha)\) is an arbitrary orthogonal central partition of the unit, and each \(F_\alpha:Mz_\alpha\to Zz_\alpha\) is normal and has norm at most \(C\). The componentwise map \(F:M\to Z\) is bounded by \(C\) and normal.

**Proof.** The strong orthogonal sum of the output components exists, with norm the supremum of their norms, by H00–H01 and the central product construction SUP in Hypertraces. It is linear and bounded. A series-vector normal test on \(Z\) is
\(\eta(d)=\sum_j\langle\xi_j,d\eta_j\rangle\), with \(\sum_j\|\xi_j\|\|\eta_j\|<\infty\). Its \(\alpha\)-component has norm at most \(\sum_j\|z_\alpha\xi_j\|\|z_\alpha\eta_j\|\). Thus
\[
\sum_\alpha\|\eta|_{Zz_\alpha}\|
\le\sum_{j,\alpha}\|z_\alpha\xi_j\|\|z_\alpha\eta_j\|
\le\sum_j\|\xi_j\|\|\eta_j\|.
\]
The last inequality is Cauchy–Schwarz on the orthogonal coordinate families. These sums have countably many nonzero terms, even for an uncountable partition. Pulling each component test back by its normal map and normal central compression gives normal functionals on \(M\) with summable norms. Their sum belongs to the norm-closed concrete predual H03, and equals \(\eta F\). All normal tests on \(Z\) therefore pull back to normal tests on \(M\), which proves ultraweak continuity. \(\square\)

<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-labelledby="trace-mechanism-title" width="360" height="700" viewBox="0 0 360 700">
<title id="trace-mechanism-title">Construction of the normal center-valued trace</title>
<defs><marker id="trace-mechanism-arrow" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0 0L8 4L0 8Z" fill="#455c71"/></marker></defs>
<rect width="360" height="700" rx="12" fill="#f7fafc"/>
<rect x="12" y="18" width="336" height="84" rx="8" fill="#fff" stroke="#526f87"/>
<text x="180" y="40" text-anchor="middle" fill="#153b56" font-family="Arial,sans-serif" font-size="16" font-weight="bold">Normal central compression</text>
<text x="180" y="61" text-anchor="middle" fill="#182a38" font-family="Arial,sans-serif" font-size="14">Φ : M → Z; Φ(1) = 1</text>
<text x="180" y="79" text-anchor="middle" fill="#182a38" font-family="Arial,sans-serif" font-size="14">Faithful restriction to q₀Mq₀</text>
<text x="335" y="94" text-anchor="end" fill="#455c71" font-family="Arial,sans-serif" font-size="12">NC, LC</text>
<path d="M180 102V123" stroke="#455c71" stroke-width="2" marker-end="url(#trace-mechanism-arrow)"/>
<rect x="12" y="126" width="336" height="84" rx="8" fill="#fff" stroke="#526f87"/>
<text x="180" y="148" text-anchor="middle" fill="#153b56" font-family="Arial,sans-serif" font-size="16" font-weight="bold">Remove pairs with ratio greater than C</text>
<text x="180" y="169" text-anchor="middle" fill="#182a38" font-family="Arial,sans-serif" font-size="14">C &gt; 1; eᵢ ∼ fᵢ; Φ(eᵢ) &gt; CΦ(fᵢ)</text>
<text x="180" y="187" text-anchor="middle" fill="#182a38" font-family="Arial,sans-serif" font-size="14">Residual e₀ ∼ f₀ ≠ 0</text>
<text x="335" y="202" text-anchor="end" fill="#455c71" font-family="Arial,sans-serif" font-size="12">LC1</text>
<path d="M180 210V231" stroke="#455c71" stroke-width="2" marker-end="url(#trace-mechanism-arrow)"/>
<rect x="12" y="234" width="336" height="84" rx="8" fill="#fff" stroke="#526f87"/>
<text x="180" y="256" text-anchor="middle" fill="#153b56" font-family="Arial,sans-serif" font-size="16" font-weight="bold">A finite comparison constant</text>
<text x="180" y="277" text-anchor="middle" fill="#182a38" font-family="Arial,sans-serif" font-size="14">Φ(a) ≤ μΦ(b) for all matched cuts</text>
<text x="180" y="295" text-anchor="middle" fill="#182a38" font-family="Arial,sans-serif" font-size="14">0 &lt; μ ≤ C</text>
<text x="335" y="310" text-anchor="end" fill="#455c71" font-family="Arial,sans-serif" font-size="12">LC</text>
<path d="M180 318V339" stroke="#455c71" stroke-width="2" marker-end="url(#trace-mechanism-arrow)"/>
<rect x="12" y="342" width="336" height="84" rx="8" fill="#fff" stroke="#526f87"/>
<text x="180" y="364" text-anchor="middle" fill="#153b56" font-family="Arial,sans-serif" font-size="16" font-weight="bold">Refine within matched corners</text>
<text x="180" y="385" text-anchor="middle" fill="#182a38" font-family="Arial,sans-serif" font-size="14">p ∼ q ≠ 0; x ∈ pMp</text>
<text x="180" y="403" text-anchor="middle" fill="#182a38" font-family="Arial,sans-serif" font-size="14">Φ(xx*) ≤ (1 + ε)Φ(x*x)</text>
<text x="335" y="418" text-anchor="end" fill="#455c71" font-family="Arial,sans-serif" font-size="12">LC3, LC</text>
<path d="M180 426V447" stroke="#455c71" stroke-width="2" marker-end="url(#trace-mechanism-arrow)"/>
<rect x="12" y="450" width="336" height="84" rx="8" fill="#fff" stroke="#526f87"/>
<text x="180" y="472" text-anchor="middle" fill="#153b56" font-family="Arial,sans-serif" font-size="16" font-weight="bold">Copy a monic corner and normalize</text>
<text x="180" y="493" text-anchor="middle" fill="#182a38" font-family="Arial,sans-serif" font-size="14">bᵢⱼ = wᵢxwⱼ*; sum both indices</text>
<text x="180" y="511" text-anchor="middle" fill="#182a38" font-family="Arial,sans-serif" font-size="14">Ψ(xx*) ≤ aΨ(x*x); a &gt; 1</text>
<text x="335" y="526" text-anchor="end" fill="#455c71" font-family="Arial,sans-serif" font-size="12">NA1, NA</text>
<path d="M180 534V555" stroke="#455c71" stroke-width="2" marker-end="url(#trace-mechanism-arrow)"/>
<rect x="12" y="558" width="336" height="84" rx="8" fill="#fff" stroke="#526f87"/>
<text x="180" y="580" text-anchor="middle" fill="#153b56" font-family="Arial,sans-serif" font-size="16" font-weight="bold">Take the norm limit</text>
<text x="180" y="601" text-anchor="middle" fill="#182a38" font-family="Arial,sans-serif" font-size="14">aₙ ↓ 1; Ψₙ → T in operator norm</text>
<text x="180" y="619" text-anchor="middle" fill="#182a38" font-family="Arial,sans-serif" font-size="14">T normal, faithful, central and tracial</text>
<text x="335" y="634" text-anchor="end" fill="#455c71" font-family="Arial,sans-serif" font-size="12">CT</text>
</svg>


*Figure 2. The central state, residual matching, finite comparison constant, monic copying and norm limit in NC–CT. The strict central inequalities are interpreted on their stated supports in LC. The argument follows the approximate-trace method in Peterson, Lemmas 6.4.8–6.4.9 and Theorem 6.4.10, with a separate construction of the finite constant in LC1.*

<a id="normal-center-state"></a>
**A normal center-valued state (NC).** Every concrete von Neumann algebra \(M\), with center \(Z\), has a normal positive unital center-linear map \(\Phi:M\to Z\).

**Proof.** SUP constructs an orthogonal central partition \((z_\alpha)\) from the supports of normal vector states of \(Z\). On each \(Zz_\alpha\) the corresponding vector state is faithful. To treat one component, write its unit as \(z\), choose the normalized vector \(\xi=z\xi\), and put \(K=\overline{Zz\xi}\). Its vector state \(\omega(d)=\langle\xi,d\xi\rangle\) on \(Zz\) is faithful, normal and tracial, because this algebra is abelian. The map \(d1\mapsto d\xi\) identifies its trace Hilbert completion with \(K\). The full normal realization proof REP in Hypertraces applies to this faithful normal trace. In an abelian algebra its left and right multiplications coincide, so REP proves
\[
\theta(Zz)'=\theta(Zz),\qquad \theta(d)=d|_K,
\]
and proves that \(\theta\) and its inverse are normal. This invocation of REP uses only its preceding scalar, Hilbert-space and predual constructions, and no center-valued trace theorem.

Let \(P\) be the projection onto \(K\). The subspace reduces \(Z\), so \(P\) commutes with it. If \(x\in Mz\), the compression \(PxP|_K\) commutes with \(\theta(Zz)\), and hence belongs to \(\theta(Zz)\). Define
\[
\Phi_z(x)=\theta^{-1}(PxP|_K).
\]
Compression is positive, unital and normal by H03's series-vector tests. The inverse \(\theta^{-1}\) is a normal *-isomorphism, so this map is positive, unital and normal. Commutation with \(Z\) proves \(\Phi_z(dx)=d\Phi_z(x)\). CN gives its norm one. Assemble these maps by CA. Their componentwise positivity, unit value and center-linearity survive assembly. The zero algebra uses its zero map. \(\square\)

<a id="local-almost-trace"></a>
**An almost tracial corner (LC).** Let \(M\ne0\) be finite, let \(\Phi:M\to Z\) be a normal center-valued state, and let \(\varepsilon>0\). There is a nonzero projection \(p\) such that \(\Phi\) is faithful on \(pMp\) and
\[
\Phi(xx^*)\le(1+\varepsilon)\Phi(x^*x)\qquad(x\in pMp).
\tag{LC}
\]

**Proof.** Choose a maximal orthogonal family of projections \(q_i\) with \(\Phi(q_i)=0\), and set \(q_0=1-\sum_i q_i\). Normality gives \(\Phi(q_0)=1\). The restriction of \(\Phi\) to \(q_0Mq_0\) is faithful: a nonzero positive element of weight zero has a nonzero positive spectral threshold projection of weight zero in that corner, contradicting maximality. The threshold projection and its lower order bound are supplied by S01–S03. Center-linearity also shows that, for a nonzero projection \(a\le q_0\), the central support of the positive element \(\Phi(a)\) is \(c(a)\). Indeed a central cut of \(\Phi(a)\) vanishes exactly when that cut of \(a\) vanishes, by faithfulness.

We first obtain a finite comparison constant. Fix a real \(C>1\). Choose a maximal family of pairs \((e_i,f_i)\) of equivalent nonzero subprojections of \(q_0\), with each family separately orthogonal, such that
\(\Phi(e_i)-C\Phi(f_i)\) is positive with support their common central support. Such families are ordered by inclusion; unions of chains give upper bounds, so Zorn applies. Put
\[
e_0=q_0-\sum_i e_i,\qquad f_0=q_0-\sum_i f_i.
\]
Orthogonal additivity of equivalence and finite-complement matching give \(e_0\sim f_0\). Also \(f_0\ne0\): otherwise normality would give
\(1\ge\Phi(\sum_i e_i)\ge C\Phi(\sum_i f_i)=C1\), which is impossible. Hence \(e_0\ne0\).

For every \(a\le e_0\), \(b\le f_0\) with \(a\sim b\),
\[
\Phi(a)\le C\Phi(b).
\tag{LC1}
\]
If this failed, the support of the positive part of \(\Phi(a)-C\Phi(b)\) would give a nonzero central cut on which the inequality is strictly reversed. The equivalent cut projections would extend the maximal family. Their common support is exactly this cut, since it lies under \(c(a)=c(b)\). This proves (LC1).

Let \(\mu\) be the infimum of all nonnegative real constants satisfying (LC1) on these residual corners. It is finite, at most \(C\), and its defining inequalities hold at the infimum because the positive cone is norm closed. It is positive: the full equivalent pair \(e_0,f_0\) gives \(\|\Phi(e_0)\|\le\mu\|\Phi(f_0)\|\), and both weights are nonzero. Since \(\mu/(1+\varepsilon)<\mu\), there are equivalent \(e\le e_0\), \(f\le f_0\) for which
\((1+\varepsilon)\Phi(e)\not\le\mu\Phi(f)\). Cut by the support \(z\ne0\) of the positive part of \((1+\varepsilon)\Phi(e)-\mu\Phi(f)\), replacing \(e,f\) by \(ez,fz\). On this central corner
\[
(1+\varepsilon)\Phi(e)-\mu\Phi(f)>0
\tag{LC2}
\]
means a positive element with support \(z=c(e)=c(f)\). All the upper inequalities \(\Phi(a)\le\mu\Phi(b)\) for equivalent subprojections remain valid after this cut.

Now choose a maximal separately orthogonal family \((\widehat e_i,\widehat f_i)\) of equivalent nonzero subprojections of \(e,f\), respectively, satisfying
\((1+\varepsilon)\Phi(\widehat e_i)\le\mu\Phi(\widehat f_i)\) on their common central support. Set
\[
p=e-\sum_i\widehat e_i,\qquad q=f-\sum_i\widehat f_i.
\]
They are equivalent by finite-complement matching: transport one sum by an equivalence \(e\sim f\), then match its complement in the finite corner. If \(p=0\), summing the inequalities would give \((1+\varepsilon)\Phi(e)\le\mu\Phi(f)\), contradicting (LC2). Thus \(p\sim q\ne0\). For equivalent \(a\le p\), \(b\le q\), the first residual bound and the second maximality give
\[
\Phi(a)\le\mu\Phi(b)\le(1+\varepsilon)\Phi(a).
\tag{LC3}
\]
For the second inequality, a nonzero support of the positive part of \(\mu\Phi(b)-(1+\varepsilon)\Phi(a)\) would provide another admissible central-cut pair. This is again forbidden by maximality.

If \(p_1,p_2\le p\) are equivalent, transport \(p_1\) through an equivalence \(p\sim q\) to obtain \(r\le q\) equivalent to both. Applying (LC3) to \((p_1,r)\) and \((p_2,r)\) gives
\[
\Phi(p_1)\le\mu\Phi(r)\le(1+\varepsilon)\Phi(p_2).
\]
For a unitary \(u\in pMp\), positive finite spectral sums consequently satisfy \(\Phi(udu^*)\le(1+\varepsilon)\Phi(d)\). S03's positive spectral sums converge in norm to every \(d\ge0\); boundedness CN and closedness of the positive cone preserve the inequality. Finally the polar partial isometry of \(x\in pMp\) extends to a unitary of this finite corner by finite-complement matching. Thus \(xx^*=u(x^*x)u^*\), giving (LC). Faithfulness holds because \(p\le q_0\). \(\square\)

<a id="normal-almost-trace"></a>
**A normal almost trace on the whole finite algebra (NA).** For every \(a>1\), a finite von Neumann algebra has a normal center-valued state \(\Psi\) satisfying \(\Psi(xx^*)\le a\Psi(x^*x)\) for all \(x\).

**Proof.** Apply NC and LC with \(\varepsilon=a-1\). The monic-decomposition lemma supplies a nonzero monic \(h\le p\), so (LC) holds on \(hMh\). Choose equivalent orthogonal copies \(h_1,\ldots,h_k\) summing to their central unit \(z_0=c(h)\), and partial isometries \(w_i\) with \(w_i^*w_i=h_i\), \(w_iw_i^*=h\). On \(Mz_0\), define
\[
F(x)=\sum_{i=1}^k\Phi(w_ixw_i^*).
\]
This is positive, normal and center-linear. Its unit value is \(k\Phi(h)\), whose support is \(z_0\). For \(x\in Mz_0\), put \(b_{ij}=w_ixw_j^*\in hMh\). Since \(\sum_jh_j=z_0\),
\[
F(xx^*)=\sum_{i,j}\Phi(b_{ij}b_{ij}^*)
\le a\sum_{i,j}\Phi(b_{ij}^*b_{ij})=aF(x^*x).
\tag{NA1}
\]
Choose \(\delta>0\) with nonzero central threshold \(z=1_{[\delta,\infty)}(F(z_0))\). S01 gives \(F(z_0)z\ge\delta z\), so its inverse \(y\in Zz\) exists by the continuous calculus. The map \(x\mapsto yF(x)\), \(x\in Mz\), is a normal center-valued state on that component, and retains (NA1). Normality of multiplication by \(y\) follows directly from H03. Positivity follows because the two central factors commute. Center-linearity and \(yF(z)=z\) prove the unit and central identity conditions.

This construction works in every nonzero remaining central corner of \(M\). Zorn therefore gives a maximal orthogonal family of central corners with such maps, and their sum is one: a nonzero remainder would provide another corner. CA assembles them to the required normal center-valued state, whose norm is one by CN. The zero algebra is immediate. \(\square\)

<a id="center-valued-trace"></a>
**The normal center-valued trace (CT).** A finite von Neumann algebra has a unique normal positive unital center-linear tracial map \(T:M\to Z(M)\). It has norm one when the algebra is nonzero and is faithful.

**Proof.** Choose real numbers \(a_n>1\) decreasing to one and normal almost traces \(\Psi_n\) supplied by NA. For a monic projection \(h\), take equivalent copies \(h_i\), \(1\le i\le k\), summing to the central support \(z\). The almost-trace inequality applied to their implementing partial isometries gives both \(\Psi_n(h)\le a_n\Psi_n(h_i)\) and \(\Psi_n(h_i)\le a_n\Psi_n(h)\). For \(m<n\), consequently,
\[
k\Psi_n(h)\le a_n z
=a_n\sum_i\Psi_m(h_i)
\le k a_na_m\Psi_m(h)
\le k a_m^2\Psi_m(h).
\]
Every projection is an orthogonal sum of monic projections. Applying the normal maps to its increasing net of finite sums proves that \(a_m^2\Psi_m-\Psi_n\) is nonnegative on every projection. Positive norm spectral approximation S03 then makes it a positive map on all positive elements. Its unit value is \((a_m^2-1)1\), so CN gives
\[
\|a_m^2\Psi_m-\Psi_n\|=a_m^2-1,
\qquad
\|\Psi_m-\Psi_n\|\le2(a_m^2-1).
\]
Thus the maps converge in operator norm to a bounded linear map \(T\). Positivity, unitality and center-linearity pass to the limit. For every normal functional \(\eta\) on \(Z\), \(\eta\Psi_n\to\eta T\) in norm. The concrete predual of \(M\) is norm closed by H03, so \(\eta T\) is normal. This proves normality of \(T\).

Passing to the limit in the almost-trace inequalities gives \(T(xx^*)\le T(x^*x)\). Replacing \(x\) by \(x^*\) gives equality. Polarization of the sesquilinear expression \(T(x^*y)-T(yx^*)\), whose diagonal is now zero, proves \(T(x^*y)=T(yx^*)\); hence \(T(ab)=T(ba)\) for arbitrary \(a,b\).

For a monic \(h\) as above, traciality makes the \(T(h_i)\)'s equal, and their sum is \(z\); therefore \(T(h)=z/k\). This forces the value of any normal center-valued trace on all monic projections, on their orthogonal sums by normality, and on every selfadjoint element by S03. Linearity proves uniqueness on \(M\). It also proves faithfulness: every nonzero projection contains a nonzero monic projection, whose trace is nonzero; every nonzero positive element dominates a positive scalar multiple of a nonzero threshold projection. Finally CN gives the norm assertion. \(\square\)

**Trace detects comparison.** For projections in a finite algebra, \(p\precsim q\) if and only if \(T(p)\le T(q)\). The forward implication is positivity and traciality. For the reverse, comparison supplies a central cut on which \(p\precsim q\), with the reverse subequivalence on its complement. On that complement choose a copy \(q'\le p\) of \(q\). The trace inequality makes \(T(p-q')=0\), and faithfulness forces \(p=q'\). Assemble the central equivalences. In particular equal center-valued traces imply equivalence, and finite-complement matching extends its partial isometry to a unitary.

<a id="s07"></a>
## S07. The two trace-factorization applications

For the normal-trace application, suppose that the centre-valued trace and the orthogonal decomposition of projections into monic projections have already been supplied. If \(p\) is monic, let \(p_1,\ldots,p_n\) be equivalent orthogonal copies of \(p\) summing to a central projection \(z\). A partial isometry \(v_i\) witnessing the equivalence has \(v_i^*v_i=p\) and \(v_iv_i^*=p_i\). Traciality gives \(\tau(p_i)=\tau(p)\) and \(T(p_i)=T(p)\). Their sums are \(\tau(z)\) and \(T(z)=z\), the latter because \(T\) is centre-linear and unital. Consequently
\[
 \tau(p)=\frac{\tau(z)}n,\qquad T(p)=\frac zn.
\]
Thus \(\tau(p)=\tau(T(p))\). For an orthogonal monic decomposition \(e=\sum_{\alpha}p_\alpha\), the net \(e_G=\sum_{\alpha\in G}p_\alpha\), over finite subsets \(G\), increases strongly to \(e\). The normality clauses give \(\tau(e_G)\to\tau(e)\) and \(\tau(T(e_G))\to\tau(T(e))\); the latter uses normality of \(T\) and of \(\tau\) restricted to the centre. Equality for every finite sum therefore gives equality on \(e\). S06 then gives \(\tau=\tau\circ T\) on all of \(M\).

For the application to an arbitrary tracial state, suppose the finite averaging construction gives, for each projection \(e\) and each dyadic \(N\), a finite average of unitary conjugates with
\[
 \left\|\frac1L\sum_{j=1}^L u_j e u_j^*-T(e)\right\|\le\frac2N.
\]
Traciality gives \(\rho(u_j e u_j^*)=\rho(e)\), so applying the norm-one functional \(\rho\) yields \(|\rho(e)-\rho(T(e))|\le2/N\). Letting dyadic \(N\) increase proves agreement on projections, and S06 gives \(\rho=\rho\circ T\) on all of \(M\), without normality. S04 provides precisely the finite central thresholds used in that averaging construction, and S05 provides its matrix rank pieces. The existence and faithfulness of the centre-valued trace, the monic decomposition, projection comparison, finite complements, and the dyadic matrix averaging construction remain their respective hypotheses and providers.

## Reading

Jesse Peterson, [*Notes on operator algebras*](https://math.vanderbilt.edu/peters10/teaching/spring2020/OperatorAlgebras.pdf), dated April 27, 2020. Projection comparison and complement methods appear in Lemma 5.1.5, Proposition 5.1.9, Theorem 5.1.10 and Propositions 5.2.7–5.2.8, pp.84–90. The finite homogeneous construction is related to Proposition 5.4.2, p.95; the halving and monic methods are Lemmas 6.4.1–6.4.3 and Proposition 6.4.4, pp.102–103. The approximate center-trace method is Lemmas 6.4.8–6.4.9 and Theorem 6.4.10, pp.104–106. Here LC1 constructs a finite uniform comparison constant before its infimum is taken. CN proves the positive-map norm estimate for arbitrary elements; NA1 gives both different quadratic products explicitly.

The earlier complete proof providers are [Regular-group operator foundations, H00–H03, T04a and CS01–CS06](regular-group-operator-foundations.md#h00), Infinite tensor products, F01–F08, and Hypertraces, GNS, COMPACT, REP and SUP. NC uses only the abelian faithful-trace instance of REP, whose proof precedes every center-valued trace application. The three diagrams are embedded as editable SVG in this lesson source.
