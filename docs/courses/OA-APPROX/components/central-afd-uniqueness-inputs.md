# From finite approximation to the dyadic factor

*Original programme exposition: CC0-1.0 to the extent of rights held.*

We prove that every factor of type \(\mathrm{II}_1\) with separable predual and finite-dimensional local approximation is normally isomorphic to the dyadic factor \(R\) constructed in [FG2](central-sequence-foundations.md#fg2-tracial-dyadic-product). In particular an increasing generating sequence of finite-dimensional algebras gives this conclusion. The whole trace-cut, matrix-projection and exact-containment arguments are supplied below.

Use the [complete retained PC0–7/FCT0–7](central-finite-trace-inputs.md) and [NT1–4](central-sequence-foundations.md#nt1-normal-functional-decomposition). Their earlier CF, CP, spectral-calculus and normal-range proofs keep their exact versions and terms. Inner products are linear in the second variable. For a normalized faithful normal trace \(\tau\), write \(\|x\|_2=\tau(x^*x)^{1/2}\). Traciality and positive order give
\[
\|axb\|_2\leq\|a\|\,\|x\|_2\,\|b\|,\qquad
\|x^*\|_2=\|x\|_2.
\tag{AF0}
\]
For example the right multiplier estimate follows by changing
\(\tau(b^*x^*xb)\) to \(\tau(x^*xbb^*)\) and then testing the positive inequality \(bb^*\leq\|b\|^2 1\) through \(|x|\). NT2 proves that this norm gives intrinsic strong* convergence on bounded sets.

<a id="af1-finite-matrices-and-trace-projections"></a>

## AF1. Finite matrices and their trace projections

Let \(D\) be any finite-dimensional unital star subalgebra of a von Neumann algebra. It is a C-star algebra: finite-dimensional subspaces are norm closed, as follows by minimizing the norm on the Euclidean unit sphere of a chosen basis; its multiplication and involution are inherited. For completeness, this minimization uses compactness of that finite sphere and injectivity of the basis map. It gives a strictly positive minimum, proving equivalence of its coordinate and operator norms.

Every element of \(D\) obeys a polynomial identity because its powers are linearly dependent. The spectrum is therefore finite. If a scalar \(\lambda\) is not a root of the polynomial identity \(P\), division
\(P(t)=P(\lambda)+(t-\lambda)Q(t)\)
gives an inverse for \(x-\lambda\), namely \(-Q(x)/P(\lambda)\). For self-adjoint elements the spectrum is real by CF. A function which is one on part of this finite spectrum and zero on the rest is a continuous function there; CF calculus supplies its projection in \(D\).

There is a nonzero minimal projection below any nonzero projection: whenever a projection is not minimal, cut to a strictly smaller nonzero corner; the dimension of the corner strictly decreases, so this procedure terminates. If \(p\) is minimal, \(pDp=\mathbb Cp\), since a nonscalar self-adjoint element in the corner would have at least two spectral values and thus a nonzero proper spectral projection. Real and imaginary parts give the conclusion for all corner elements. Splitting the unit until all summands are minimal terminates too: nonzero orthogonal projections are linearly independent in the finite-dimensional vector space. Thus \(1=\sum_{i=1}^m p_i\) with minimal \(p_i\).

Two of these projections either have \(p_iDp_j=0\), or are equivalent inside \(D\). For a nonzero \(x\in p_iDp_j\), \(x^*x=\alpha p_j\), \(\alpha>0\); the element \(v=x/\sqrt\alpha\) has initial projection \(p_j\), and its nonzero final projection below \(p_i\) is \(p_i\). Such equivalence is transitive by multiplying the implementing partial isometries. Each equivalence class has sum \(z\) central in \(D\), because all corners joining different classes are zero. Within a class choose \(v_i^*v_i=p_1\), \(v_iv_i^*=p_i\), including \(v_1=p_1\). Then \(v_iv_j^*\) are matrix units. Every corner \(p_iDp_j\) is one-dimensional, because compression by \(v_i^*,v_j\) puts it in \(\mathbb Cp_1\). Hence these matrix units span the entire class corner. We have proved, with no classification premise,
\[
D=\bigoplus_{k=1}^r M_{d_k}(\mathbb C).
\tag{AF1.1}
\]

Suppose now that \(D\subset M\), where \(M\) has faithful normal finite trace \(\tau\). Put \(t_k=\tau(f_{11}^{(k)})>0\) for its matrix units. Equivalence and the trace give the same value on each diagonal unit of that block. Finite-dimensional Hilbert projection defines the unique element \(E_D(x)\in D\) with
\[
\tau(a^*E_D(x))=\tau(a^*x)\qquad(a\in D).
\tag{AF1.2}
\]
Indeed the explicit formula is
\[
E_D(x)=\sum_k t_k^{-1}\sum_{i,j}
\tau(f_{ji}^{(k)}x)f_{ij}^{(k)}.
\tag{AF1.3}
\]
The matrix units are pairwise orthogonal for the trace inner product, with squared norm \(t_k\). This verifies both existence and uniqueness. The formula makes \(E_D\) normal by NT1's module-functionals argument. It fixes \(D\), is unital, and is \(D\)-bimodular: test \(E_D(bxc)\) using (AF1.2), move \(b,c\) across the trace, use the defining identity for \(x\), and move them back. Uniqueness gives \(E_D(bxc)=bE_D(x)c\).

It is completely positive. For \(X=[x_{ij}]\geq0\) in \(M_\ell(M)\) and any \(b_i\in D\), trace preservation and bimodularity give
\[
\tau\!\left(\sum_{i,j}b_i^*E_D(x_{ij})b_j\right)
=\tau\!\left(\sum_{i,j}b_i^*x_{ij}b_j\right)\geq0.
\]
In any chosen block of (AF1.1), choose a unit vector \(\eta\), and take \(b_i\) to be the rank-one matrix sending \(\eta\) to a prescribed vector \(\xi_i\), zero on \(\eta^\perp\), and zero in the other blocks. The displayed value is \(t_k\) times the matrix quadratic form on \((\xi_i)\). Since \(t_k>0\), all these forms are nonnegative in every block. Thus \([E_D(x_{ij})]\geq0\).
The Schwarz proof in NT1 gives
\[
E_D(x)^*E_D(x)\leq E_D(x^*x)\leq\|x\|^2 1.
\]
Consequently \(E_D\) is an operator-norm contraction. The Hilbert projection identity also gives, for any \(a\in D\),
\[
\|x-a\|_2^2=\|x-E_D(x)\|_2^2+\|E_D(x)-a\|_2^2.
\tag{AF1.4}
\]
In particular it minimizes the \(2\)-norm error. These proofs concern every finite-dimensional subalgebra, including direct sums with unequal block weights; no expectation onto a general infinite-dimensional subalgebra is a premise.

<a id="af2-trace-cuts-and-projection-repair"></a>

## AF2. Trace cuts, projection repair and rounding

In a factor of type \(\mathrm{II}_1\), every nonzero projection corner has no abelian projection. PC4 makes the center of that corner scalar; an abelian subcorner would therefore be one-dimensional, making its unit minimal in \(M\), contrary to type \(\mathrm{II}_1\). FCT3's explicit maximal-pair construction halves the unit of any such corner into two equivalent projections. Repeating that construction halves each remaining piece.

If \(0<s<\tau(p)\), expand \(s/\tau(p)\) in binary. At step \(j\), halve the current remaining dyadic piece, retaining a half of trace \(\tau(p)2^{-j}\) if the \(j\)-th digit is one and continuing within the other half. The selected pieces are orthogonal; their strong sum belongs to \(M\) by PC1 and has trace \(s\) by normality. The endpoints \(s=0,\tau(p)\) use \(0,p\). This constructs every trace cut. FCT7's trace comparison on a factor gives
\[
\tau(p)=\tau(q)\ \Longrightarrow\ p\sim q.
\tag{AF2.1}
\]

Here is the quantitative projection repair, also valid for arbitrary finite von Neumann algebras when \(e\sim f\). Put
\[
B=e-f,\qquad r=fe+(1-f)(1-e).
\]
Multiplication gives
\[
re=fr,\qquad r^*r=rr^*=1-B^2,\qquad r+r^*=2(1-B^2).
\tag{AF2.2}
\]
The positive contraction \(B^2\) commutes with \(e,f,r\); positivity and its bound follow as well from its two diagonal blocks
\(e(1-f)e\) and \((1-e)f(1-e)\).
Let \(k=1_{\{1\}}(B^2)\), provided by the complete bounded spectral calculus. On \(1-k\), the bounded polar construction gives a unitary \(u_0\) with \(r=u_0(1-B^2)^{1/2}\). The positive square root commutes with \(e\) and \(r\), so the range-isometry definition gives
\[
u_0e(1-k)=f(1-k)u_0.
\]
Equation (AF2.2) shows that the real part of \(u_0\) is \((1-B^2)^{1/2}\) on this support. To justify cancellation without an unbounded inverse, multiply their difference by that square root. The result is zero; its range is dense in \((1-k)H\), so the bounded difference itself is zero. Thus
\[
(u_0-(1-k))^*(u_0-(1-k))
=2((1-k)-(1-B^2)^{1/2})
\leq2B^2(1-k).
\tag{AF2.3}
\]
The last inequality is CF calculus applied to \(1-\sqrt{1-t}\leq t\), \(0\leq t\leq1\).

On the exceptional support, \(r=0\). Since \(k\) commutes with \(e,f\), its \(e\)-part lies in \(eH\cap(1-f)H\), and its \(1-e\)-part lies in \((1-e)H\cap fH\). Conversely those two intersections have \(B^2=1\). Hence
\[
k=p+q,\qquad p=e\wedge(1-f),\qquad q=(1-e)\wedge f.
\]
The center-valued traces of \(e,f\) agree, and the equivalence implemented on \(1-k\) has equal traces there as well. Subtraction gives equal center-valued traces for \(p,q\). FCT7 supplies a partial isometry \(v\) with \(v^*v=p,vv^*=q\). Then \(w=v-v^*\) is a skew-adjoint unitary on \(k\), carries \(p\) to \(q\), and has \((w-k)^*(w-k)=2k\). The orthogonal sum \(u=u_0+w\) is unitary, and
\[
ueu^*=f,\qquad
(u-1)^*(u-1)\leq2(e-f)^2,\qquad
\|u-1\|_2\leq\sqrt2\,\|e-f\|_2
\tag{AF2.4}
\]
when a finite trace is specified. This includes a zero exceptional support.

We also need one spectral rounding estimate. For \(0\leq h\leq1\), set \(q=1_{[1/2,1]}(h)\). Pointwise
\[
|t-1_{[1/2,1]}(t)|\leq2t(1-t).
\]
Squaring and applying bounded spectral calculus and the positive trace gives
\[
\|h-q\|_2\leq2\|h-h^2\|_2.
\tag{AF2.5}
\]
No statement about higher spectral cutoffs is needed in this route.

<a id="af3-dyadic-approximants"></a>

## AF3. Replace a finite approximant by a dyadic matrix factor

Let \(D=\bigoplus_kM_{d_k}\subset M\), where \(M\) is a factor of type \(\mathrm{II}_1\). Fix \(\eta>0\). Put \(t_k=\tau(f_{11}^{(k)})\) and choose \(p\) large, with \(r_k=\lfloor2^p t_k\rfloor>0\). AF2 cuts a projection \(g_k\leq f_{11}^{(k)}\) of trace \(r_k2^{-p}\), and splits it into \(r_k\) pieces of trace \(2^{-p}\). Transport these pieces to every diagonal of that block by \(f_{i1}^{(k)}\). The remaining projection has trace
\[
1-\sum_kd_kr_k2^{-p},
\]
an integral multiple of \(2^{-p}\); split it into that many pieces of trace \(2^{-p}\), with no piece needed if it is zero. All the resulting projections are equivalent by (AF2.1).

Connect a fixed reference piece to the first piece of each transported family by an implementing partial isometry. Connect it to the other pieces of that family using the prescribed block matrix units. Connect it to each leftover piece arbitrarily. The resulting \(v_a\) have a common initial reference and orthogonal final projections summing to one. The elements \(v_av_b^*\) form a full \(2^p\)-matrix system. Its algebra \(Q\) contains every transported connection and therefore
\[
\widetilde f_{ij}^{(k)}=f_{i1}^{(k)}g_kf_{1j}^{(k)}.
\]
The difference from \(f_{ij}^{(k)}\) is a partial isometry with initial support \(f_{jj}^{(k)}\) minus its transported cut. Hence
\[
\|f_{ij}^{(k)}-\widetilde f_{ij}^{(k)}\|_2^2
=t_k-r_k2^{-p}<2^{-p}.
\tag{AF3.1}
\]
Every coefficient of \(x=\sum\lambda_{ij}^{(k)}f_{ij}^{(k)}\) has modulus at most \(\|x\|\), by its matrix-corner test. Thus, with \(s=\sum_kd_k^2\), replacing its matrix units gives an element of \(Q\) with error at most \(s2^{-p/2}\|x\|\). AF1's nearest-point property gives
\[
\|x-E_Q(x)\|_2\leq\eta\|x\|\qquad(x\in D)
\tag{AF3.2}
\]
when \(p\) is sufficiently large. It can be chosen above any prescribed integer. The original finite algebra is approximated here; no assertion of exact inclusion of a projection with irrational trace in a dyadic matrix algebra is made.

Suppose \(M\) has **local finite-dimensional approximation**: every finite set has arbitrarily small \(2\)-norm error in some finite-dimensional star subalgebra. Such an algebra may be made unital by adjoining \(1\). For every finite-dimensional linear subspace \(V=\operatorname{span}(x_1,\ldots,x_m)\), this gives dyadic matrix factors approximating its operator-norm unit ball uniformly. Indeed
\[
C_V=\sup_{\|\sum_j\lambda_jx_j\|\leq1}\sum_j|\lambda_j|<\infty
\]
by the finite-sphere norm bound proved in AF1. Choose a finite algebra \(D\) so that each \(\|x_j-E_D(x_j)\|_2\) is small. Apply (AF3.2) with an independently small parameter; \(\|E_D(x_j)\|\leq\|x_j\|\). Adding these two errors and then summing with the coefficients controls the unit ball by \(C_V\). This proves the stated uniformity.

<a id="af4-exact-dyadic-containment"></a>

## AF4. Preserve the previous dyadic algebra exactly

Suppose \(M\) has that local approximation property, and \(N\cong M_d\subset M\) is unital, \(d=2^n\). For a finite-dimensional subspace \(V\) and \(\varepsilon>0\), we construct a unital dyadic matrix factor \(Q\supset N\) with
\[
\|x-E_Q(x)\|_2\leq\varepsilon\|x\|\qquad(x\in V).
\tag{AF4.1}
\]
Fix matrix units \(e_{ij}\) for \(N\) and put \(e=e_{11}\). Form
\[
W=\mathbb Ce+\sum_{i,j}e_{1i}Ve_{j1}\subset eMe.
\]
AF3 supplies \(D\cong M_{2^p}\), \(p>n\), whose trace projection approximates the unit ball of \(W\) to within \(\delta\), where \(\delta>0\) will be chosen small. Set \(h=E_D(e)\). AF1 gives \(0\leq h\leq1\), and
\[
\|h-e\|_2\leq\delta,\qquad
\|h-h^2\|_2\leq3\delta.
\]
For the second assertion expand
\(h-h^2=(h-e)+(e-h)e+h(e-h)\)
and use (AF0). Rounding by (AF2.5) gives \(q\in D\) with
\(\|q-e\|_2\leq7\delta\).
Since \(\tau(e)=1/d\), Schwarz gives
\(|\tau(q)-1/d|\leq7\delta\).
Enlarge or shrink \(q\) within the matrix algebra to a comparable projection \(q_1\) of trace exactly \(1/d\). This is possible because that trace and \(\tau(q)\) are integral multiples of \(2^{-p}\). In ordinary matrix coordinates it just adds or removes the required number of orthogonal rank-one projections. Comparability gives
\[
\|q-q_1\|_2^2=|\tau(q)-1/d|,\qquad
\|q_1-e\|_2\leq a(\delta):=7\delta+\sqrt{7\delta}.
\tag{AF4.2}
\]
Equal traces and (AF2.4) give a unitary \(u\) with
\(uq_1u^*=e\) and \(\|u-1\|_2\leq\sqrt2\,a(\delta)\).

Choose unital \(d\)-matrix units \(w_{ij}\) inside \(D\) with \(w_{11}=q_1\): divide its defining matrix space into \(d\) blocks of equal dimension, the first being the range of \(q_1\). Put
\[
v=\sum_{i=1}^d e_{i1}u w_{1i}.
\tag{AF4.3}
\]
Matrix-unit multiplication and \(uq_1u^*=e\) give
\[
v^*v=1,\qquad vv^*=1,\qquad vw_{ij}v^*=e_{ij}.
\]
Thus \(Q=vDv^*\) contains \(N\) exactly. The entire \(v\) need not be close to one.

The estimates concern only its first-corner action. For \(z=eze\in W\) put \(z'=q_1E_D(z)q_1\). The inequalities for left/right multiplication give
\[
\|z-z'\|_2
\leq\|z-q_1zq_1\|_2+\|q_1(z-E_D(z))q_1\|_2
\leq(2a(\delta)+\delta)\|z\|.
\]
Also \(\|z'\|\leq\|z\|\), and \(vq_1=uq_1\), so \(vz'v^*=uz'u^*\). Hence
\[
\|z-vz'v^*\|_2
\leq[\delta+(2+2\sqrt2)a(\delta)]\|z\|.
\tag{AF4.4}
\]
For \(x\in V\), the entries \(z_{ij}=e_{1i}xe_{j1}\in W\) have norm at most \(\|x\|\), and
\(x=\sum_{i,j}e_{i1}z_{ij}e_{1j}\).
Replace each entry by the element of \(eQe\) just constructed. The resulting element of \(Q\) differs from \(x\) by at most
\[
d^2[\delta+(2+2\sqrt2)a(\delta)]\|x\|.
\tag{AF4.5}
\]
Choose \(\delta\) to put this bound below \(\varepsilon\), and use AF1's minimizing projection onto \(Q\). This proves (AF4.1), with \(p>n\). No corner amenability or prior corner AFD theorem enters this construction.

<a id="af5-full-finite-afd-uniqueness"></a>

## AF5. The complete finite AFD uniqueness theorem

**Theorem.** For every factor \(M\) of type \(\mathrm{II}_1\) with separable predual, the following are equivalent:

1. \(M\) is normally isomorphic to \(R\).
2. An increasing sequence of finite-dimensional unital star algebras generates \(M\).
3. \(M\) has local finite-dimensional \(2\)-norm approximation.

**Proof.** A faithful normal normalized trace exists by FCT6–7, because the center is scalar. Condition1 gives condition 2 by transporting the local tensor matrices in FG2. For condition 2, the union is a unital star algebra. Its norm closure has bicommutant \(M\), and BD1–5 supplies bounded strong approximation and hence bounded ultraweak approximation. NT2 gives \(2\)-norm approximation by these bounded elements. Approximating them in norm by elements of the union puts finitely many desired approximants in one finite stage. This proves condition 3.

Assume condition 3. The faithful trace GNS Hilbert space is separable by NT2. Its subset consisting of the unit-ball vectors \(x\Omega\), \(x\in M\), is a separable metric space by TS1; choose a \(2\)-norm dense sequence \(x_j\) in that ball. Starting with \(\mathbb C1\), use AF4 successively on
\(V_k=\operatorname{span}(x_1,\ldots,x_k)\).
This gives
\[
N_k\cong M_{2^{n_k}},\qquad N_k\subset N_{k+1},\qquad
n_k<n_{k+1},\qquad
\|x_j-E_{N_k}(x_j)\|_2\leq2^{-k}\quad(j\leq k).
\tag{AF5.1}
\]
AF1 bounds those approximants by one. NT2 therefore puts every \(x_j\) in the strongly closed generated algebra. Approximate any other unit-ball \(x\) by the chosen \(x_j\)'s; they remain bounded, so NT2 puts \(x\) in that algebra as well. Thus \((\bigcup_kN_k)''=M\).

Every unital inclusion \(M_a\subset M_b\) has \(b=ar\) and relative commutant \(M_r\). Here is the finite argument. Its diagonal matrix units divide \(\mathbb C^b\) into \(a\) mutually orthogonal ranges, with equal dimension \(r\), because the off-diagonal units give isometries between them. Choose a basis in the first range and transport it to the others. In those coordinates the inclusion is \(M_a\otimes1_r\). A matrix commuting with all those matrix units has zero off-diagonal blocks and identical diagonal \(r\)-blocks, giving exactly \(1_a\otimes M_r\). Their products generate the whole \(M_b\).

Apply this to successive \(N_k\)'s. Between them insert the finitely many \(M_2\) tensor levels of their relative commutant; also insert the initial levels inside \(N_1\). To justify these finite tensor factorizations, label the basis of a \(2^r\)-dimensional matrix space by binary strings of length \(r\). An elementary matrix is exactly the product of its \(r\) coordinate matrix units, proving the isomorphism with \(r\) copies of \(M_2\). We obtain increasing
\(A_m\cong M_{2^m}\)
with \(A_{m+1}\cong A_m\otimes M_2\) and generated algebra \(M\). Choose the coordinate isomorphisms inductively through the relative commutant so that all inclusions agree with \(x\mapsto x\otimes1_2\).

The trace of each finite matrix stage is its normalized matrix trace. Indeed its diagonal units are equivalent and sum to one, so have trace \(2^{-m}\); an off-diagonal unit has trace zero by the trace relation with a diagonal unit. Thus the compatible algebraic-union isomorphism from FG2's local matrices onto \(\bigcup_mA_m\) preserves traces. It extends isometrically to a unitary between their trace Hilbert completions, because the local vectors are dense on each side. On the \(M\) side this density follows from bounded density and trace \(2\)-norm convergence; on the \(R\) side it is the construction of FG2.

The unitary intertwines every local left multiplier. Conjugation by it therefore identifies the two bicommutants. The trace GNS representation of \(M\) is faithful and normal, has von Neumann image, and has a normal inverse onto that image by the complete STC/ST1–2 route in NT2. Operator conjugation is normal by its vector-pair substitutions. Consequently this is a normal isomorphism of the original \(M\) with \(R\). This proves condition 1 and all equivalences. \(\square\)

In particular, the increasing finite group algebras in Proposition 6.1 satisfy condition 2. Every part of its identification with \(R\) is now covered, including direct sums in the initial stages and irrational traces in the approximation steps.

## Freely accessible method comparisons

Claire Anantharaman and Sorin Popa's [author draft](https://idpoisson.fr/anantharaman/publications/IIun.pdf), Lemma 11.2.1 and Theorem 11.2.2, printed 185–188 (PDF 191–194), supplies the dyadic-cut and tracial-completion method. Its nesting proof uses amenability, then AFD, of a matrix corner. AF4 instead proves exact containment using a single projection repair and the old matrix units. The trace projections, finite matrix decompositions, scalar trace cuts and all predecessor proofs are supplied here.

The programme's [local-approximation lesson](../src/hyperfinite-finite-factors.md) also develops the projection-repair and exact-first-corner method. This module gives the whole finite-uniqueness input using only finite-dimensional trace projections and FG2's independently constructed dyadic factor. Its statement and complete proof apply to every separable-predual factor of type \(\mathrm{II}_1\) with the stated approximation property. No implication from amenability to AFD, arbitrary finite-commutant classification, or modular theorem is used as an unstated premise.
