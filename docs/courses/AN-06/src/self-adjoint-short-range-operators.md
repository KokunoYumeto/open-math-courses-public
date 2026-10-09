# Self-adjoint short-range operators

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

**Working question: Which closed realization is being scattered?** A formal expression \(p(D)+V\) is not yet a self-adjoint operator. A bounded potential permits the elementary domain argument in the first lesson, but a general differential perturbation needs its own closure and factorization. Keeping that distinction prevents an unproved relative-bound assumption from entering the wave construction.

A symmetric differential perturbation can be unbounded on \(L^2\). Compactness on the endpoint graph space still gives a self-adjoint closure and an exact resolvent factorization. The operator domain will be the closure of its Schwartz graph; every resolvent composition below is justified on that domain.

Let \(p\) be real, simply characteristic, with no invariant direction, and let \(P_0=p(D)\) on its maximal \(L^2\) domain. Let \(V\) be a short-range finite-order local differential expression with \(L^2_{\mathrm{loc}}\) coefficients, in the sense of [Short-range compactness and local tests](short-range-compactness-and-local-tests.md#short-range-local-criterion). Use its graph space \(X_p\), unique compact extension \(V:X_p\to B\), and distribution-to-norm convergence theorem. Assume \(V\) is symmetric on compact smooth functions:

\[
 (V\phi,\psi)=(\phi,V\psi),\qquad \phi,\psi\in C_c^\infty.
\tag{1}
\]

The pairing is linear in its first argument. The compact alternative needed here and in the later boundary analysis is proved next on an arbitrary Banach space. Its finite-dimensional facts—bounded coordinates, compact unit spheres, closed finite-dimensional subspaces and complete quotients—are proved in [Compact Fredholm operators, elementary tools](../providers/analysis/compact-fredholm-families.md#fredholm-finite-tools). We use the complete shell duality, density and embeddings of [Endpoint spaces and flat energy shells](endpoint-spaces-and-flat-energy-shells.md#endpoint-shell-spaces). The Fourier transform on Schwartz functions and tempered distributions is proved in [Measure and Fourier foundations](../providers/analysis/finite-derivative-l2.md#fourier-normalization).

<a id="short-range-compact-alternative"></a>

**Compact alternative used below.** If \(C\) is compact on a Banach space \(Y\), then \(A=I+C\) has closed range, finite-dimensional kernel, and
\[
 \dim\ker A=\dim(Y/\operatorname{ran}A).
\]
Consequently injectivity implies a bounded inverse on all of \(Y\).

**Proof.** The unit ball in \(\ker A\) is precompact, because \(x=-Cx\) there. A normed space with precompact unit ball is finite dimensional: in an infinite-dimensional space, successively choose unit vectors at distance greater than \(1/2\) from the spans of the preceding vectors. The elementary selection works for any proper closed subspace \(M\): take \(v\notin M\), put \(d=\operatorname{dist}(v,M)>0\), choose \(w\in M\) with \(\|v-w\|<2d\), and normalize \(v-w\). Its distance from \(M\) exceeds \(1/2\). Applying this to the closed finite-dimensional spans gives a sequence with no convergent subsequence.

There is a constant \(c>0\) such that \(\|Ax\|\geq c\operatorname{dist}(x,\ker A)\). Otherwise choose quotient classes of norm one with images tending to zero and representatives \(x_j\) of norm at most two. A subsequence of \(Cx_j\) converges by compactness; \(x_j=Ax_j-Cx_j\) then converges to a vector of \(\ker A\), contradicting its quotient norm one. If \(Ax_j\) converges, subtract kernel vectors so that these representatives are bounded, using this estimate. Compactness again gives a subsequence for which \(Cx_j\), and hence \(x_j\), converge. Its limit maps to the prescribed output limit. Thus the range is closed. The same arguments apply to every \(A^k=I+C_k\), since its finite polynomial remainder \(C_k\) is compact. Indeed the image of a precompact set under a bounded map is precompact, and the sum of finitely many precompact sets is precompact: choose convergent subsequences successively for each summand. Thus every positive power of \(C\), and then the finite binomial remainder of \((I+C)^k\), is compact.

Put \(N_k=\ker A^k\) and \(R_k=\operatorname{ran}A^k\), with \(N_0=0\), \(R_0=Y\). The increasing chain \(N_k\) stabilizes. If it did not, choose unit \(x_k\in N_k\) at distance greater than \(1/2\) from \(N_{k-1}\). For \(l<k\), both \(Ax_k\) and \(Cx_l\) belong to \(N_{k-1}\), so \(\|Cx_k-Cx_l\|>1/2\), contradicting compactness. Likewise the decreasing chain \(R_k\) stabilizes: if all its inclusions were strict, choose unit \(x_k\in R_{k-1}\) at distance greater than \(1/2\) from \(R_k\). For \(l>k\), both \(Ax_k\) and \(Cx_l\) belong to \(R_k\), giving the same contradiction. These choices use the closedness just proved and the elementary subspace selection above. Equality in the range chain propagates by applying \(A\); equality in the kernel chain propagates by taking the inverse image under \(A\).

Choose \(m\) beyond both stabilization indices. Then
\(Y=N_m\oplus R_m\). Indeed, if \(x=A^my\in N_m\), then \(y\in N_{2m}=N_m\) and \(x=0\). For arbitrary \(x\), \(A^mx\in R_m=R_{2m}\); write \(A^mx=A^{2m}y\) to get \(x-A^my\in N_m\). Both summands are closed and \(N_m\) is finite dimensional. The projection onto \(N_m\) is bounded because the quotient map \(Y\to Y/R_m\) is one-to-one on this finite-dimensional summand: its norm on that summand is bounded below on the compact unit sphere. Its complementary projection \(Q:Y\to R_m\) is bounded too. On \(R_m\), \(A\) is injective by the zero intersection and onto by stabilization. Since \(\ker A\subset N_m\), for \(x\in R_m\) and \(k\in\ker A\) we have \(x=Q(x-k)\). Hence
\[
 \|x\|\leq\|Q\|\operatorname{dist}(x,\ker A)
       \leq \|Q\|c^{-1}\|Ax\|.
\]
This proves boundedness of the inverse on \(R_m\), which complements the generalized kernel \(N_m\). On \(N_m\), ordinary finite-dimensional rank–nullity gives equal kernel dimension and range codimension. Since \(A\) preserves both summands and is onto \(R_m\), this proves the displayed equality on \(Y\). When \(\ker A=0\), the quotient lower bound becomes \(\|Ax\|\geq c\|x\|\); the equality gives surjectivity and this bound gives boundedness of the inverse. \(\square\)

<a id="short-range-endpoint-symmetry"></a>

## 1. Extending symmetry to endpoint waves

**Lemma 1.1.** For all \(u,v\in X_p\),

\[
 (Vu,v)=(u,Vv).
\tag{2}
\]

Both pairings are absolutely convergent.

**Proof.** The graph norm controls \(u,v\in B^*\), while \(Vu,Vv\in B\). Shell Cauchy–Schwarz proves absolute integrability and continuity of the pairings in the graph norms. Smooth density therefore reduces the assertion to smooth \(u,v\in X_p\).

Choose a real compact smooth \(\chi\), equal to one near zero, and set \(u_R=\chi(x/R)u,\ v_R=\chi(x/R)v\). These functions are compact and smooth. Polynomial Leibniz and the uniform bounds on the derivatives of \(\chi(x/R)\), \(R\geq1\), show that \(u_R,v_R\) are uniformly bounded in \(X_p\). They converge to \(u,v\) in distributions. Theorem 4.1 of [Short-range compactness and local tests](short-range-compactness-and-local-tests.md#short-range-distribution-continuity) gives \(Vu_R\to Vu,\ Vv_R\to Vv\) in \(B\).

Apply (1) to \(u_R,v_R\). For example,

\[
 |(Vu_R-Vu,v_R)|
       \leq\|Vu_R-Vu\|_B\|v_R\|_{B^*}\longrightarrow0.
\]

Also \((Vu,v_R)\to(Vu,v)\) by dominated convergence, since \(|Vu\,v|\) is integrable and the cutoffs are uniformly bounded. The other side has the same two steps. This proves (2) for smooth inputs, then for all inputs by graph-norm density. \(\square\)

<a id="short-range-selfadjointness"></a>

## 2. Essential self-adjointness

Initially let

\[
 P=P_0+V,\qquad \mathcal D(P)=\mathcal S(\mathbb R^n).
\]

Schwartz functions belong to \(X_p\), so \(V\) maps this domain to \(B\subset L^2\). The maximal multiplier \(P_0\) is self-adjoint by [Resolvents, domains and spectral density](resolvents-domains-and-spectral-density.md#u001-specified-domains).

**Theorem 2.1.** \(P\) is essentially self-adjoint. Write \(H=\overline P\) for its self-adjoint closure.

**Proof.** Lemma 1.1 and the real Fourier symbol make \(P\) symmetric on its dense domain. It is closable: if \(u_j\to0\) and \(Pu_j\to h\) in \(L^2\), then \((h,v)=\lim(u_j,Pv)=0\) for all \(v\) in the dense domain, hence \(h=0\). Its closure is closed and symmetric.

Corollary 4.3 of [Short-range compactness and local tests](short-range-compactness-and-local-tests.md#short-range-imaginary-axis) gives

\[
 \|VR_p(it)\|_{B\to B}\longrightarrow0
       \quad(|t|\to\infty).
\tag{3}
\]

Choose one \(T>0\) sufficiently large that this norm is less than one at both \(t=T\) and \(t=-T\). The convergent geometric series makes \(I+VR_p(\pm iT)\) invertible on \(B\). Explicitly, for a bounded \(C\) with \(\|C\|<1\), completeness of \(B\) defines \(S f=\sum_{k\ge0}(-C)^kf\), with \(\|S\|\le(1-\|C\|)^{-1}\). The geometric tail bound gives convergence in operator norm; multiplying its finite sums on either side by \(I+C\) leaves a remainder of norm at most \(\|C\|^{N+1}\). Passing to the limit proves both inverse identities.

<a id="short-range-schwartz-inverse"></a>

For nonreal \(z\), \(P_0-z\) is a bijection on \(\mathcal S\). Indeed its inverse is Fourier multiplication by \(1/(p-z)\); the denominator is bounded below by \(|\operatorname{Im}z|\), and every derivative of the reciprocal has at most polynomial growth. It therefore maps Schwartz functions to Schwartz functions. On that domain the exact factorization is

\[
 (P-z)u=(I+VR_p(z))(P_0-z)u.
\tag{4}
\]

Consequently, for the chosen \(z=\pm iT\),
\(\operatorname{Ran}(P\mp iT)=(I+VR_p(\pm iT))\mathcal S\).
Schwartz functions are dense in \(B\), and an invertible bounded map preserves density. Both these ranges are therefore dense in \(B\), hence in \(L^2\).

To complete the operator argument explicitly, let \(A=\overline P\). Symmetry gives

\[
 \|(A-it)u\|_2^2=\|Au\|_2^2+t^2\|u\|_2^2,\qquad t\in\mathbb R.
\tag{5}
\]

For \(t\ne0\), this estimate and closedness show that \(\operatorname{Ran}(A-it)\) is closed: a Cauchy output sequence makes both its inputs and their \(A\) images Cauchy. Since it contains the dense initial range, it equals \(L^2\). Thus \(A-it\) is onto for both chosen signs.

The orthogonal-complement identity
\(\operatorname{Ran}(A-it)^\perp=\ker(A^*+it)\)
shows that the two corresponding adjoint defect kernels vanish. If \(v\in\mathcal D(A^*)\), use the onto range at \(it\) to choose \(w\in\mathcal D(A)\) with
\((A-it)w=(A^*-it)v\). Then \(v-w\in\ker(A^*-it)=0\), using the onto range at the opposite sign. Hence \(v=w\in\mathcal D(A)\). The reverse inclusion follows from symmetry, so \(A=A^*\). \(\square\)

The theorem identifies the operator as the closure of its Schwartz restriction. For a general differential \(V\), an equality of its domain with the free maximal domain would need an additional argument.

<a id="short-range-resolvent-domain"></a>

## 3. Justifying the resolvent factorization on \(B\)

For \(\operatorname{Im}z\ne0\), write \(R_H(z)=(H-z)^{-1}\). This inverse exists on all of \(L^2\): if \(z=a+ib\), symmetry and self-adjointness give

\[
 \|(H-z)u\|_2^2=\|(H-a)u\|_2^2+b^2\|u\|_2^2.
\]

The same closed-range argument as above applies to \(H-a\). The orthogonal complement of the range is \(\ker(H-\overline z)=0\), by the same estimate, so the range is also dense and hence equals \(L^2\). Consequently \(\|R_H(z)\|_{L^2\to L^2}\le |b|^{-1}\), and its range lies in \(\mathcal D(H)\).

**Lemma 3.1.** If \(f\in B\), then \(R_p(z)f\in\mathcal D(H)\) and

\[
 (H-z)R_p(z)f=f+VR_p(z)f.
\tag{6}
\]

**Proof.** Choose \(f_j\in\mathcal S\) converging to \(f\) in \(B\), hence in \(L^2\). Put \(u_j=R_p(z)f_j\in\mathcal S\). The ordinary resolvent bound gives \(u_j\to R_p(z)f\) in \(L^2\). Theorem 1.1 of [Global polynomial resolvent estimates](global-polynomial-resolvent-estimates.md#global-polynomial-domains), applied to each derivative of the polynomial, gives \(u_j\to R_p(z)f\) in \(X_p\), and therefore \(Vu_j\to VR_p(z)f\) in \(B\subset L^2\). Also
\[
 P_0u_j=f_j+zu_j\longrightarrow f+zR_p(z)f
\]
in \(L^2\). Thus \(Pu_j\) converges to the sum of these two limits. Closedness of \(H\), as the closure of this restriction, proves membership and (6). \(\square\)

<a id="short-range-resolvent-factorization"></a>

**Theorem 3.2.** For every nonreal \(z\), \(I+VR_p(z)\) is invertible on \(B\), and

\[
 R_H(z)f=R_p(z)(I+VR_p(z))^{-1}f\in X_p,\qquad f\in B.
\tag{7}
\]

Both resolvent identities are valid on \(B\):

\[
 R_p(z)=R_H(z)+R_H(z)VR_p(z),
\tag{8}
\]

\[
 R_p(z)=R_H(z)+R_p(z)VR_H(z).
\tag{9}
\]

**Proof.** The free resolvent maps \(B\) boundedly to \(X_p\), and \(V:X_p\to B\) is compact, so \(VR_p(z)\) is compact on \(B\). If
\((I+VR_p(z))f=0\), Lemma 3.1 gives
\((H-z)R_p(z)f=0\). The nonreal resolvent of the self-adjoint \(H\) is injective, so \(R_p(z)f=0\), then \(f=0\). Apply the compact alternative proved above to get the bounded inverse on \(B\).

Take \(g=(I+VR_p(z))^{-1}f\). Equation (6) gives
\((H-z)R_p(z)g=f\), which proves (7). In particular every occurrence of \(VR_H(z)f\) in (9) is defined in \(B\).

Applying \(R_H(z)\) to (6) gives (8) directly. Alternatively, (7) gives \(f=g+VR_p(z)g\) and \(R_H(z)f=R_p(z)g\); applying \(R_p(z)\) to the first equality gives (9). All compositions have now been assigned their domains and spaces. \(\square\)

No real-boundary invertibility is asserted here. At real energies a nonzero kernel may occur; the limiting-absorption and point-spectrum analysis must handle it separately.

<a id="short-range-resolvent-continuity"></a>

## 4. Local continuity and a concrete potential

**Corollary 4.1.** On each open half-plane, \(R_H(z)\) is locally bounded as an operator \(B\to X_p\) and is weak-star continuous in every graph component.

**Proof.** The free map \(R_p(z):B\to X_p\) is locally bounded and has weak-star continuous components. The short-range convergence theorem upgrades this to norm continuity of \(VR_p(z)\) on \(B\) in operator norm. To check the uniform assertion, if it failed at \(z\), choose \(z_j\to z\) and \(\|f_j\|_B\leq1\) for which
\(\|V(R_p(z_j)-R_p(z))f_j\|_B\) stays positive. The difference is uniformly bounded in \(X_p\) by the compact energy bound. Its \(L^2\) norm tends to zero, because the Hilbert resolvent identity gives
\[
 \|(R_p(z_j)-R_p(z))f_j\|_2
       \leq\frac{|z_j-z|}{|\operatorname{Im}z_j|\,|\operatorname{Im}z|}
                       \|f_j\|_2.
\]
The convergence theorem contradicts that positive lower bound.

The identity
\[
 T(z')-T(z)=T(z')\,[VR_p(z)-VR_p(z')]\,T(z),
 \qquad T(z)=(I+VR_p(z))^{-1},
\]
and a geometric series near each \(z\) give local norm continuity and local boundedness of \(T\). For a fixed \(f\in B\), subtract (7) at the two parameters:

\[
 \begin{aligned}
 R_H(z')f-R_H(z)f
 &=R_p(z')[T(z')-T(z)]f\\
 &\quad+[R_p(z')-R_p(z)]T(z)f.
 \end{aligned}
\]

The first term tends to zero in \(X_p\), by the local bound for the free resolvent and norm continuity of \(T\). The second tends weak-star to zero in each graph component, by the free endpoint theorem with its fixed forcing \(T(z)f\in B\). Local boundedness follows directly from the product of the two local operator bounds. This proves the claim. \(\square\)

<a id="short-range-parabolic-example"></a>

**Example 4.2.** Let \(p(\xi)=\xi_1-\xi_2^2\), and let \(V\) be a real measurable function satisfying
\[
 |V(x)|\leq C(1+|x|)^{-1-\delta},\qquad\delta>0.
\]
The hypotheses on the free polynomial can be checked directly:

\[
 \widetilde p(\xi)^2=p(\xi)^2+4\xi_2^2+5,
 \qquad |\nabla p(\xi)|^2=1+4\xi_2^2.
\]

Thus \(\widetilde p\le\sqrt5\,(|p|+|\nabla p|)\), so \(p\) is simply characteristic. If a vector \(w\) were invariant, comparing \(p(\xi+tw)=p(\xi)\) for all \(\xi,t\) gives \(w_2=0\) from the coefficient of \(t\xi_2\), and then \(w_1=0\). Its invariant space is therefore zero. Strength properness and the [decaying-coefficient criterion](short-range-compactness-and-local-tests.md#short-range-decaying) make this multiplication short range. Its real values give (1). The theorem supplies a self-adjoint closure and (7), even though the free operator is nonelliptic and is not lower bounded. In this bounded-potential example, [the bounded-perturbation theorem](resolvents-domains-and-spectral-density.md#u001-specified-domains) makes \(A=P_0+V\) self-adjoint on the free maximal domain. It extends the initial Schwartz operator, so its closed graph contains that of \(H\), giving \(H\subset A\). Taking adjoints reverses this inclusion: directly from the adjoint definition, \(A^*\subset H^*\). Since both operators are self-adjoint, \(A\subset H\) as well. They are equal, proving the claimed domain identification for this example.

### Use the conclusion

Verify the extended symmetry pairing before using the deficiency argument. In the resolvent factorization, identify the space on which the compact factor is inverted and the domain to which the resulting solution belongs.

<a id="short-range-selfadjoint-exercises"></a>

## 5. Exercises

**Exercise 5.1 (foundation).** In the scalar model \(P_0=a\), \(V=b\), verify (7)-(9) with \(a,b\in\mathbb R\). Use the calculation to check the plus sign in \(I+VR_p(z)\).

**Exercise 5.2 (foundation).** Prove that a closed symmetric operator \(A\) has closed range for \(A-it\), \(t\ne0\), using (5). Identify where closedness, rather than symmetry alone, is used.

**Exercise 5.3 (intermediate).** Verify that multiplication by \(1/(p-z)\) maps \(\mathcal S\) to itself for a real polynomial and nonreal \(z\). Explain why the same global Schwartz assertion cannot simply be used at a real regular energy.

**Exercise 5.4 (intermediate).** In Lemma 1.1's cutoff limit, prove separately the norm-error estimate and the dominated-convergence step for \((Vu_R,v_R)\). Explain why a distributional limit alone would not justify their pairing limit.

**Exercise 5.5 (advanced).** Let \(C(z)=VR_p(z)\) and suppose \(I+C(z_0)\) is invertible on \(B\). Derive a sufficient norm-neighborhood condition for \(I+C(z)\) to remain invertible. Give an explicit bound for its inverse and derive the inverse-difference formula used in Corollary 4.1.

<a id="short-range-selfadjoint-solutions"></a>

## 6. Complete solutions

**Solution 5.1.** Here \(R_p(z)=(a-z)^{-1}\), so
\[
 R_p(z)\left(1+bR_p(z)\right)^{-1}
       =\frac1{a-z}\frac{a-z}{a+b-z}
       =\frac1{a+b-z}.
\]
Also \(R_p-R_H=b/[(a-z)(a+b-z)]\), which equals both products on the right of (8) and (9). A minus sign in the factor would instead produce the denominator \(a-b-z\).

**Solution 5.2.** If \((A-it)u_j\) is Cauchy, apply (5) to \(u_j-u_k\). Both \(u_j\) and \(Au_j\) are Cauchy in \(L^2\), with limits \(u,h\). Closedness says \(u\in\mathcal D(A)\) and \(Au=h\). The original output limit is therefore \((A-it)u\), proving it lies in the range. Symmetry supplies (5); closedness supplies membership of the limiting input in the domain.

**Solution 5.3.** Every derivative of \(1/(p-z)\) is a finite sum of products of polynomial derivatives divided by a positive power of \(p-z\). The denominator's absolute value is at least \(|\operatorname{Im}z|>0\), so all these derivatives grow at most polynomially. Leibniz's rule then shows that multiplying any Schwartz Fourier function by the reciprocal preserves every Schwartz seminorm. At a real energy with a nonempty regular shell, the denominator vanishes on that shell. The upper and lower boundary reciprocals then contain a principal-value pole and a delta surface term, so they are distributions rather than smooth multipliers of polynomial growth. A real energy with an empty shell need not have this obstruction: for \(p(\xi)=|\xi|^2\) and \(\lambda=-1\), the reciprocal is \((1+|\xi|^2)^{-1}\). It is smooth, and all its derivatives have at most polynomial growth, so it preserves Schwartz space by the same Leibniz argument. Its boundary value has no singular surface contribution.

**Solution 5.4.** Write
\[
 (Vu_R,v_R)-(Vu,v)
       =(Vu_R-Vu,v_R)+(Vu,v_R-v).
\]
The first term is bounded by
\(\|Vu_R-Vu\|_B\|v_R\|_{B^*}\), which tends to zero by strong compactness convergence and the uniform cutoff norm bound. The second is the integral of
\(Vu\,\overline v\,(\chi(x/R)-1)\), bounded in absolute value by a constant times the integrable function \(|Vu\,v|\); its pointwise factor tends to zero. Dominated convergence applies. A bare distributional limit does not control the first norm error or an integral against a varying, potentially noncompact endpoint wave.

**Solution 5.5.** Put \(T_0=(I+C(z_0))^{-1}\). Factor
\[
 I+C(z)=
   \left[I+(C(z)-C(z_0))T_0\right](I+C(z_0)).
\]
If \(\|(C(z)-C(z_0))T_0\|\leq q<1\), the geometric series in the bracket converges. Hence
\[
 \|(I+C(z))^{-1}\|\leq\|T_0\|/(1-q).
\]
For any two invertible factors \(A',A\), multiplying their difference by the inverses gives \(A'^{-1}-A^{-1}=A'^{-1}(A-A')A^{-1}\). Taking \(A'=I+C(z')\), \(A=I+C(z)\) yields exactly the displayed formula in Corollary 4.1.

## References


- [T] Gerald Teschl, *Mathematical Methods in Quantum Mechanics: With Applications to Schrödinger Operators*, second edition, American Mathematical Society, 2014, Section 2.2, Lemma 2.7 and Corollary 2.8, pages 74–75. [Author's authorized online edition](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe2.pdf).
