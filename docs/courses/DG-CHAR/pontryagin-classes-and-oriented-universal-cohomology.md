# Pontryagin classes and oriented universal cohomology

*Written by GPT-6.1 Sol (OpenAI), at Ultra, October 2026. Self-checked by the writing AI, GPT-6.1 Sol, at Ultra. Independently authored text dedicated under CC0.*

Complexification gives integral characteristic classes of real bundles in degrees divisible by four. We prove their torsion-qualified Whitney formula, compute the classes of projective tangent bundles, and identify the top class with the square of the Euler class. We then compute the universal oriented ring, both modulo two and with two inverted. The deleted-vector comparison needed for the latter computation is proved by an explicit homotopy.

Our convention is \(p_i(\xi)=(-1)^i c_{2i}(\xi\otimes_{\mathbb R}\mathbb C)\). The [Chern chapter](DG-CHAR-09.html) provides the integral classes, their conjugation rule and their full Whitney formula on paracompact Hausdorff bases. The bundle, [classification](DG-CHAR-03.html), [Thom/Euler](DG-CHAR-06.html), [Gysin/projective](DG-CHAR-08.html) and [Schubert](DG-CHAR-04.html) chapters provide the proved topology, exact sequences, orientations and universal real mod-two ring. We state precisely where paracompactness and coefficient assumptions enter.

## 1. Complexification and the two-torsion terms

For a real rank-\(n\) bundle \(\xi\), its complexification \(\xi_{\mathbb C}\) has complex rank \(n\). Every fibre vector has a unique form \(x+iy\), with \(x,y\) in the original real fibre. Thus its underlying real bundle is naturally \(\xi\oplus\xi\), and its complex structure on these coordinates is \(J(x,y)=(-y,x)\). The real-linear map \(x+iy\mapsto x-iy\) is complex linear as a map into the conjugate bundle. Hence
\[
\xi_{\mathbb C}\cong\overline{\xi_{\mathbb C}},\qquad
2c_{2j+1}(\xi_{\mathbb C})=0.
\tag{1.1}
\]
The second identity is the Chern conjugation rule; it means annihilation by two, including the possibility of zero.

Define
\[
p_0(\xi)=1,\quad p_i(\xi)=(-1)^ic_{2i}(\xi_{\mathbb C}),\quad
p_i(\xi)=0\text{ if }2i>n.
\tag{1.2}
\]
These definitions, naturality and stability under adding trivial real bundles work on every Hausdorff base: complexification respects pullbacks and sends a trivial real summand to a trivial complex summand. The orientation of \(\xi\) is irrelevant to \(p_i\).

**Theorem 1.1.** For real bundles on a paracompact Hausdorff base,
\[
2\bigl(p_k(\xi\oplus\eta)-\sum_{i+j=k}p_i(\xi)p_j(\eta)\bigr)=0
\quad\text{for every }k.
\tag{1.3}
\]

**Proof.** Complexification respects direct sums, so the Chern Whitney formula expresses \(c_{2k}((\xi\oplus\eta)_{\mathbb C})\) as the sum of products whose indices add to \(2k\). The even-even terms, multiplied by \((-1)^k\), give exactly the displayed Pontryagin products. Every remaining term has two odd indices and is annihilated by two by (1.1). Thus the difference is annihilated by two. ∎

This is an integral assertion, not a mod-two reduction assertion. After passing to coefficients in which two is invertible, the product formula holds exactly. Integrally it may fail. For an explicit failure, take the tautological real line \(L\) on \(\mathbb {RP}^4\). Write \(a=w_1(L)\) and \(t=c_1(L_{\mathbb C})\). By (1.1), \(2t=0\). The underlying real complexification is \(L\oplus L\), so the Chern-to-Stiefel–Whitney formula gives
\[
\rho_2t=w_2(L\oplus L)=a^2.
\]
Consequently \(\rho_2(t^2)=a^4\ne0\). A line has \(p(L)=1\), whereas
\[
p_1(L\oplus L)=-c_2(L_{\mathbb C}\oplus L_{\mathbb C})=-t^2\ne0.
\tag{1.4}
\]
This nonzero difference is two-torsion, exactly as (1.3) requires.

For every real bundle on a paracompact Hausdorff base, the same comparison gives
\[
\rho_2p_i(\xi)=w_{2i}(\xi)^2.
\tag{1.5}
\]
Indeed \(w((\xi_{\mathbb C})_{\mathbb R})=w(\xi)^2\). In characteristic two its degree-\(4i\) component is \(w_{2i}(\xi)^2\); all distinct-index pairs cancel. It also equals \(\rho_2c_{2i}(\xi_{\mathbb C})\), and the integral sign disappears upon reduction.

## 2. Complex bundles, projective spaces and the top Euler square

For a complex bundle \(V\), complexifying its underlying real bundle gives
\[
(V_{\mathbb R})_{\mathbb C}\cong V\oplus\overline V.
\tag{2.1}
\]
Explicitly \(x\otimes z\mapsto(zx,\overline z x)\) defines a complex-linear map, with the second entry interpreted in \(\overline V\). In the real decomposition \(x+iy\), it sends this vector to \((x+iy,x-iy)\), using the original complex structure on \(V\) for these two outputs. Its inverse takes \((v,w)\) to \(x+iy\) with \(x=(v+w)/2\) and \(y=(v-w)/(2i)\). This verifies the isomorphism fibrewise and continuously.

On a paracompact Hausdorff base, Chern Whitney and conjugation therefore give
\[
p_k(V_{\mathbb R})=(-1)^k\sum_{i+j=2k}(-1)^j c_i(V)c_j(V).
\tag{2.2}
\]
For instance
\[
p_1=c_1^2-2c_2,\qquad
p_2=c_2^2-2c_1c_3+2c_4.
\]
On a flag space with Chern roots \(t_1,\ldots,t_r\), (2.1) has roots \(t_j,-t_j\); hence
\[
p(V_{\mathbb R})=\prod_{j=1}^r(1+t_j^2).
\tag{2.3}
\]
This equality in roots descends by the integral flag injection. In this complex-bundle case no two-torsion qualification is needed.

With \(x=c_1(\gamma^*)\) on \(\mathbb {CP}^n\), the proved stable complex tangent isomorphism gives
\[
p(T\mathbb {CP}^n)=(1+x^2)^{n+1}
\quad\text{in }\mathbb Z[x]/(x^{n+1}).
\tag{2.4}
\]
Here tangent means its underlying real tangent bundle. Equivalently \(p_i=\binom{n+1}{i}x^{2i}\), with only \(4i\leq2n\) surviving. Thus \(p_1(\mathbb {CP}^2)=3x^2\) and its number is three, using the positive top evaluation already proved. On \(\mathbb {CP}^3\), \(p=1+4x^2\); on \(\mathbb {CP}^4\), \(p=1+5x^2+10x^4\). A sphere has \(TS^n\oplus\varepsilon^1\cong\varepsilon^{n+1}\), so all its positive-degree Pontryagin classes vanish by stability.

**Theorem 2.1.** For an oriented real rank-\(2k\) bundle, \(k\geq1\), on any Hausdorff base,
\[
p_k(\xi)=e(\xi)^2\in H^{4k}(B;\mathbb Z).
\tag{2.5}
\]

**Proof.** The real isomorphism \((\xi_{\mathbb C})_{\mathbb R}\cong\xi\oplus\xi\) compares two orientations. If \(v_1,\ldots,v_{2k}\) is positive for \(\xi\), the complex orientation orders \(v_1,iv_1,\ldots,v_{2k},iv_{2k}\). The ordered real sum orientation orders all \(v_j\) first and all \(iv_j\) second. The interleaving permutation has sign
\[
(-1)^{(2k)(2k-1)/2}=(-1)^k.
\]
Euler orientation reversal and the ordered Euler product rule give
\(c_{2k}(\xi_{\mathbb C})=e((\xi_{\mathbb C})_{\mathbb R})=(-1)^ke(\xi)^2\).
Multiplying by the sign in (1.2) proves the integral equality. It used the metric-free top Chern definition and the full oriented Thom product, so paracompactness was not needed. ∎

## 3. Oriented Grassmannians and their mod-two ring

For \(n\geq1\), let \(BSO(n)\) be the oriented real \(n\)-planes in \(\mathbb R^\infty\), and \(q:BSO(n)\to BO(n)\) forget their orientation. The unit sphere of the determinant line \(\det\gamma_n\) is precisely this double cover: a unit determinant vector chooses one of the two orientations. The total cover topology is the weak topology of its compact finite oriented Grassmannian stages. This follows from the compact-fibre local chart argument supplied for flags in the Chern chapter, now with fibre two points. It is Hausdorff and paracompact by the proved compact-limit lemmas. The pulled-back universal bundle \(\widetilde\gamma_n\) has the orientation recorded by the base point.

These spaces are path connected. In ambient dimension \(N>n\), extend an oriented orthonormal \(n\)-frame to a positively oriented basis of \(\mathbb R^N\), adjusting the complementary basis if necessary. The connected group \(SO(N)\) moves this basis to any other one. Its connectedness follows explicitly by successive plane rotations that move its first column to the first coordinate vector and then repeat on the orthogonal complement; in the final two-plane use an ordinary rotation. This is the same positive-linear-group path calculation used for fibre orientations earlier. Thus each such finite oriented Grassmannian, and the infinite union, is path connected. In rank one, the oriented line is its positive unit vector, so \(BSO(1)=S^\infty\); its contractibility was proved by the shift-and-rotation homotopy in the classification chapter. Define \(BSO(0)\) to be a point.

**Theorem 3.1.**
\[
H^*(BSO(n);\mathbb F _2)=\mathbb F _2[w_2,\ldots,w_n].
\tag{3.1}
\]
The indicated classes are those of \(\widetilde\gamma_n\); for ranks zero and one the ring is just \(\mathbb F _2\).

**Proof.** The class of the determinant line is \(w_1(\gamma_n)\), by the determinant identity proved in the squares chapter. The double-cover Gysin sequence is therefore multiplication by \(w_1\) on the polynomial ring \(H^*(BO(n);\mathbb F _2)=\mathbb F _2[w_1,\ldots,w_n]\), with the cover cohomology between consecutive multiplication maps. Multiplication by \(w_1\) is injective, so exactness makes \(q^*\) surjective with kernel the ideal \((w_1)\). Its ring quotient is exactly (3.1). Rank zero uses a point; the rank-one quotient also agrees with the contractible sphere model. ∎

## 4. The deleted-vector comparison, with an actual homotopy

For \(n\geq2\), take the unit sphere bundle \(E_n=S(\widetilde\gamma_n)\). A point is an oriented \(n\)-plane \(X\) with a unit vector \(v\in X\). Put \(Y=X\cap v^\perp\), oriented so that \(v\) followed by a positive basis of \(Y\) is positive in \(X\). Then
\[
f:E_n\longrightarrow BSO(n-1),\qquad (X,v)\longmapsto Y
\tag{4.1}
\]
is continuous, and \(\pi^*\widetilde\gamma_n\cong\varepsilon^1\oplus f^*\widetilde\gamma_{n-1}\). Here the unit-vector line comes first in the orientation. We may regard a point of \(E_n\) as the pair \((Y,v)\), with \(Y\) oriented and \(v\) a unit vector perpendicular to it. All these spaces have compact finite-dimensional stages and the compact-fibre/direct-limit topology verified in Section3.

**Lemma 4.1.** The map (4.1) is a homotopy equivalence.

**Proof.** Let \(S_e(e_i)=e_{2i}\), \(S_o(e_i)=e_{2i-1}\), and let \(e_1\) be the first coordinate vector. Define
\[
s(Y)=(S_eY,e_1).
\]
The vector is perpendicular to the even-coordinate plane. The composite \(fs\) is the even shift of \(Y\); the injective operators \(A_t=(1-t)I+tS_e\), with the largest-coordinate proof from the classification chapter, give a homotopy to the identity through oriented planes.

Here is a homotopy from \((Y,v)\) to \(sf(Y,v)\). First send \(Y\) to \(A_tY\), transporting its orientation, and send \(v\) to the normalized orthogonal projection of \(A_tv\) off \(A_tY\). This projection never vanishes, because \(A_t\) is injective on \(Y\oplus\mathbb Rv\). Its matrix in a finite frame is the continuous Gram-matrix projection; at the endpoint the pair is \((S_eY,S_ev)\). Next keep \(S_eY\) fixed and rotate the vector to \(S_ov\) by \(\cos(\pi t/2)S_ev+\sin(\pi t/2)S_ov\). Its two terms are orthogonal unit vectors, both perpendicular to \(S_eY\).

On the odd-coordinate space let \(T(e_{2i-1})=e_{2i+1}\). Move \(S_ov\) to \(TS_ov\) using the normalized straight path \(((1-t)I+tT)S_ov\). The largest nonzero coordinate proves that this path never vanishes. It stays in odd coordinates, perpendicular to \(S_eY\). At its endpoint the first coordinate is zero. Finally rotate \(TS_ov\) to \(e_1\), using their orthogonality. The final pair is \((S_eY,e_1)\), as required.

All formulas are continuous on finite stages, take each such stage times the compact interval into a finite stage, and therefore are jointly continuous by the compact-product lemma. The Gram normalization has positive factor and the transported orientation is continuous. This proves both homotopy identities. Rank one was deliberately handled separately: its sphere fibre consists of two points, so the corresponding total space has two components and is not the comparison in this lemma. ∎

The nonzero-vector total space retracts radially onto \(E_n\), so it has the same cohomology. The Gysin sequence can now be written, without an unproved limit step, using \(H^*(BSO(n-1))\) in place of deleted total-space cohomology. Under this identification \(\pi^*p_i=p_i(\widetilde\gamma_{n-1})\), by the actual bundle decomposition preceding the lemma and Pontryagin stability.

## 5. The universal ring with two inverted

Let \(A\) be a commutative ring with identity in which two is a unit, including \(\mathbb Z[1/2]\), \(\mathbb Q\), and fields of odd characteristic. Characteristic classes in this section are the images of their integral classes under coefficient change.

**Theorem 5.1.** For \(m\geq0\),
\[
H^*(BSO(2m+1);A)=A[p_1,\ldots,p_m].
\tag{5.1}
\]
For \(m\geq1\),
\[
H^*(BSO(2m);A)=A[p_1,\ldots,p_{m-1},e],
\quad |p_i|=4i,\quad |e|=2m,
\tag{5.2}
\]
with \(p_m=e^2\). In odd rank the Euler class is zero with these coefficients. There are no further polynomial relations.

**Proof.** Induct in rank. Rank zero is a point and rank one is the contractible sphere model, so its cohomology is \(A\) in degree zero. The earlier Thom/Euler theorem proves \(2e=0\) in odd rank; coefficient change makes \(e=0\) over \(A\).

Suppose \(n=2m\). By induction the cohomology of \(BSO(n-1)\) is \(A[p_1,\ldots,p_{m-1}]\). Every generator lifts under \(\pi^*\), by the comparison lemma, so this map is surjective in every degree. Its Gysin sequence therefore gives short exact sequences
\[
0\longrightarrow H^{q-n}(BSO(n);A)
\xrightarrow{\ \smile e\ }H^q(BSO(n);A)
\xrightarrow{\ \pi^*\ }H^q(BSO(n-1);A)\longrightarrow0.
\tag{5.3}
\]
Given a class in degree \(q\), lift its image by its unique polynomial in the lower Pontryagin classes. The difference is \(e\) times a unique class of degree \(q-n\). Repeating in that smaller degree expresses it as a polynomial in the claimed generators; the procedure terminates in negative degree. For independence, a zero polynomial first restricts to its constant-in-\(e\) term on \(BSO(n-1)\), which must be zero by induction. Divide the remaining relation by \(e\) using the injection in (5.3), and repeat. Thus no polynomial relation exists. The integral identity (2.5) gives \(p_m=e^2\).

Now suppose \(n=2m+1\geq3\). Since \(e=0\), Gysin makes \(\pi^*\) injective. The comparison identifies its target with
\[
A[p_1,\ldots,p_{m-1},e'],\qquad (e')^2=p_m,
\]
the already computed even-rank ring. The sphere-bundle antipodal map covers the identity on \(BSO(n)\). In the pair description it sends \((Y,v)\) to \((-Y,-v)\), where \(-Y\) means the opposite orientation: this compensates the sign of \(-v\) to keep the total \(n\)-plane orientation fixed. On target cohomology it fixes the Pontryagin classes and sends \(e'\) to \(-e'\). Hence the image of \(\pi^*\) consists of invariant polynomials. Such polynomials contain only even powers of \(e'\), because an odd-power coefficient would satisfy \(a=-a\), forcing \(a=0\) when two is invertible. The invariant ring is therefore
\(A[p_1,\ldots,p_{m-1},(e')^2]\).
Every one of these generators lies in the image: \(p_i\) lifts by stability and \((e')^2\) is the image of \(p_m\) by (2.5). The image is exactly that ring. Its generators are independent since their monomials are distinct monomials in the even-rank polynomial ring. This proves the odd case and completes the induction. ∎

The odd-rank argument identifies the image using the antipodal action. It requires neither a rank-only comparison nor a cohomology inverse-limit assertion. The integral equality \(p_m=e^2\) survives before coefficients change; the polynomial presentations (5.1)–(5.2) are stated only with two inverted.

The coefficient ring need not be an integral domain. In even rank, the Gysin injection supplies each division by \(e\) and the lower-rank polynomial ring supplies unique coefficients; neither step cancels a coefficient in \(A\). In odd rank, the only coefficient cancellation is \(2a=0\Rightarrow a=0\), which follows because two is a unit. The proof therefore also covers rings with zero divisors, such as \(\mathbb Z/9\mathbb Z\).

## 6. Exercises with solutions

**Exercise 6.1 — Easy.** Compute \(p(T\mathbb {CP}^3)\) and compare with \(p(TS^6)\).

**Solution.** Equation (2.4), truncated at \(x^4=0\), gives \(1+4x^2\). Its would-be next term has degree eight and vanishes on this real six-dimensional space. Sphere tangent stabilization gives \(p(TS^6)=1\). The two tangent bundles therefore have different Pontryagin data on their respective bases, despite both having real rank six.

**Exercise 6.2 — Medium.** Prove the top Euler-square identity, keeping the orientation sign.

**Solution.** For real rank \(2k\), move the imaginary basis vectors from the second block into interleaved positions. The number of crossings is \((2k)(2k-1)/2\), of parity \(k\). Thus the complex orientation gives Euler class \((-1)^ke(\xi\oplus\xi)=(-1)^ke(\xi)^2\). This is the top Chern class of the complexification. The Pontryagin sign \((-1)^k\) cancels it. This proves the integral equality over any Hausdorff base with the stated bundle orientation.

**Exercise 6.3 — Medium.** Prove the qualified Whitney formula and exhibit a nonzero two-torsion error.

**Solution.** Split the even-index Chern Whitney sum into its even-even and odd-odd terms. The former are exactly the signed Pontryagin products; multiplying each latter term by two gives zero by conjugation. For two copies of the tautological line on \(\mathbb {RP}^4\), write \(t=c_1(L_{\mathbb C})\). Its mod-two reduction is \(a^2\), so \(t^2\) has nonzero reduction \(a^4\). Thus \(p_1(2L)=-t^2\ne0\), while each individual line has all positive Pontryagin classes zero. Since \(2t=0\), the difference is annihilated by two.

**Exercise 6.4 — Hard.** Prove the universal oriented ring theorem and list the degree-eight bases for \(BSO(4)\) and \(BSO(5)\) over \(A\).

**Solution.** Replace the sphere-bundle total space by \(BSO(n-1)\) using the actual shift/projection/rotation homotopy of Lemma4.1. In even rank its lower Pontryagin generators lift, so Gysin gives (5.3); successive subtraction of the lower-rank polynomial and division by the injective Euler map proves generation and independence. In odd rank the Euler map is zero and pullback injects into the even-rank ring. Antipodal invariance removes its odd Euler powers, while the remaining Euler square is the pulled-back top Pontryagin class. This identifies the image exactly and proves the theorem, starting from the separately contractible rank-one model. For \(BSO(4)\) the ring is \(A[p_1,e]\), with both generators of degree four, so the degree-eight basis is \(p_1^2,p_1e,e^2\). For \(BSO(5)\) it is \(A[p_1,p_2]\), and the basis is \(p_1^2,p_2\).

**Exercise 6.5 — Medium.** Compute the unoriented universal ring \(H^*(BO(n);A)\) with two inverted, supplying the double-cover transfer proof.

**Solution.** For a double cover \(q:\widetilde X\to X\) with deck map \(t\), define \(T\) on singular chains by summing the two lifts of each simplex. Each lift exists by choosing its vertex lift and using path lifting on the contractible simplex; the homotopy-lifting proof in the classification chapter makes it continuous and unique. Restricting to a face gives exactly the two lifts of that face, so \(T\partial=\partial T\). Moreover \(q_*T=2\operatorname{id}\) and \(Tq_*=\operatorname{id}+t_*\). Dualizing gives a transfer \(\tau\) with \(\tau q^*=2\operatorname{id}\) and \(q^*\tau=\operatorname{id}+t^*\). Thus \(q^*\) is injective when two is a unit; its image consists precisely of the invariants, since an invariant \(b\) equals \(q^*(\tau b/2)\).

Apply this to the orientation cover. Orientation reversal fixes all Pontryagin classes and negates the even-rank Euler generator. The invariant rings computed from Theorem5.1 are
\[
H^*(BO(n);A)=A[p_1,\ldots,p_{\lfloor n/2\rfloor}].
\]
In even rank the final generator pulls back to \(e^2\). In rank one there are no positive generators and the ring is \(A\); rank zero is a point. This proof computes an invariant image, rather than assuming a covering pullback surjective.

**Exercise 6.6 — Medium.** Verify the mod-two reduction formula and the rank-two oriented normalization.

**Solution.** Underlying real complexification is \(\xi\oplus\xi\). Its total mod-two class is \(w(\xi)^2\), whose component in degree \(4i\) is exactly \(w_{2i}(\xi)^2\). Chern reduction identifies this component with \(\rho_2p_i\). For an oriented two-plane, (2.5) gives \(p_1=e^2\). Its integral universal ring is already \(\mathbb Z[e]\): Lemma4.1 identifies the unit sphere total space with the contractible \(BSO(1)\), and Gysin makes multiplication by \(e\) an isomorphism between consecutive positive even degrees and gives zero odd groups. Starting from \(H^0=\mathbb Z\), these powers are the integral basis in every degree. This rank-two argument does not require two inverted, although the complete higher-rank polynomial theorem does.

## Sources and scope

Freely accessible comparisons are Allen Hatcher, *Vector Bundles and K-Theory*, version 2.2 (2017), [author PDF](https://pi.math.cornell.edu/~hatcher/VBKT/VB.pdf), Section 3.2, and Haynes Miller, *Algebraic Topology II* (2020), [Chapter 5](https://ocw.mit.edu/courses/18-906-algebraic-topology-ii-spring-2020/d567d6a5a35a1553ad4984de13700cf8_MIT18_906S20_ch5.pdf), Lecture 36. Miller's Theorem 36.5 states the oriented polynomial presentations over every \(\mathbb Z[1/2]\)-algebra. Sections 4–5 provide the complete homotopy and invariant-image proofs for that coefficient scope; Section 1 retains the integral two-torsion error before two is inverted.

Sections 1–5 prove the Whitney formula with its integral two-torsion term, the projective calculation, the Euler-square identity and the oriented universal-ring presentation. The deleted-vector homotopy and coefficient-limit argument are explicit. Antipodal invariance determines the odd-rank image. The mod-two oriented-ring calculation uses the complete frame and Euler obstruction proofs in the earlier companion.

Natural Pontryagin classes and the integral top Euler-square identity work on every Hausdorff base with the stated orientation. Whitney, complex-root and coefficient-reduction calculations use a paracompact Hausdorff base. The universal presentations have their explicit coefficient assumptions. The full frame-obstruction theory is supplied in [the frame-obstruction companion](frame-fields-and-primary-obstructions.md). This version records only a check by the writing AI; independent review is separate. The complete assigned teaching and proof prerequisites are now supplied across the course.
