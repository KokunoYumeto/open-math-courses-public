# Semi-infinite orbits and weight functors

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Public domain (CC0).*

A Schubert variety is finite dimensional, while an orbit of a unipotent loop group extends through infinitely many lattice bounds. Their intersection has a precise dimension. This dimension determines the degree in which a perverse sheaf contributes a weight. We will prove the dimension formula using ordinary lattice determinants, prove classical hyperbolic restriction, and construct the resulting decomposition of cohomology.

For the geometry, let \(k\) be algebraically closed in any characteristic, \(O=k[[t]]\), \(F=k((t))\), and \(G\) connected reductive. Fix \(T\subset B\), let \(N\) be the unipotent radical of \(B\), and let positive roots be those of \(N\). Put \(\rho=\frac12\sum_{\alpha>0}\alpha\). Dominant coweights have nonnegative positive-root pairings. Schubert and semi-infinite orbit closures in this lesson have their reduced structures.

The sheaf-theoretic theorems below are proved for \(k=\mathbb C\), classical constructible sheaves, and a characteristic-zero coefficient field \(\Lambda\). Write \(IC_\lambda\) with the perverse normalization: its restriction to the open Schubert orbit is \(\Lambda[\langle2\rho,\lambda\rangle]\). The geometric proofs do not restrict the characteristic of \(k\). The rational-adic extension over other algebraically closed fields is a separate unfinished assertion specified in §21; it is not an input to the classical proofs.

The construction of the Grassmannian is proved in Loop groups and the affine Grassmannian, Theorem 7.1. Orbit dimensions, projective reduced Schubert closures, and their component class are proved in Orbits and Schubert varieties in the affine Grassmannian, Theorems 2.3 and 3.5 and §5. Root coordinates and rank-one identities are proved in Roots and reductive groups of rank one, Theorem 7.1, and Root data, Weyl chambers and the Bruhat decomposition, §5. We use these exact earlier proofs.

## 1. Statements, conventions, and exact earlier inputs

Put \(O=k[[t]]\), \(F=k((t))\), \(K=G(O)\), and let \(N\) be the unipotent radical of the chosen positive Borel \(B\). Write

\[
S_\nu=N(F)t^\nu K/K,\qquad
\eta\le\nu\Longleftrightarrow
\nu-\eta\in\sum_i\mathbb Z_{\ge0}\alpha_i^\vee.
\]

Closures and locally closed orbit loci in this lesson have their **reduced** structures. The hyperplane assertions identify underlying supports and their reduced closed subschemes. The lattice embeddings and cutoff operators themselves are constructed on arbitrary coefficient rings and retain their nilpotents. This distinction is necessary: for a torus, \(N=1\), but the full Grassmannian contains \(1+\epsilon t^{-1}\), \(\epsilon^2=0\), whereas its reduced semi-infinite orbit is a point. A closed weight-subspace condition must not be claimed to identify that point's full nilpotent functor.

The earlier orbit is irreducible: its acting finite jet group is smooth and connected, hence irreducible, so its image and reduced closure are irreducible. The hyperplane argument below uses the principal ideal theorem from Dimension theory of Noetherian local rings, Theorem 3.1, and the finite-type height formula from Krull dimension and Noether normalization, Theorems 4.2–4.3. Their complete algebraic proofs are given there.

The results proved here are

\[
\overline{S_\nu}=\bigcup_{\eta\le\nu}S_\eta,
\qquad
\overline{S_\nu}\setminus S_\nu
=\overline{S_\nu}\cap H_\nu
\tag{1.1}
\]

for a compatible hyperplane in an ordinary lattice Plücker ind-projective embedding, and, for dominant \(\lambda\),

\[
S_\nu\cap\overline{\operatorname{Gr}^{\lambda}}
\text{ is empty unless }t^\nu\in\overline{\operatorname{Gr}^{\lambda}},
\quad
\dim C=\langle\rho,\lambda+\nu\rangle
\tag{1.2}
\]

for every irreducible component \(C\) of a nonempty intersection. The same nonemptiness criterion and pure dimension hold for \(S_\nu\cap\operatorname{Gr}^{\lambda}\). No dual-group weight multiplicity statement is used.

## 2. An ordinary exterior-power ind-space

Choose a \(T\)-weight basis \(e_1,\ldots,e_d\) of \(V\), with weights \(\gamma_1,\ldots,\gamma_d\), counted with multiplicity. Fix a determinant-index component \(e\) of \(\operatorname{Gr}_{GL(V)}\). For sufficiently large \(N\), put

\[
Q_N=t^{-N}V_O/t^NV_O,\quad r_N=dN-e,
\quad
\mathcal F_N^e=\bigwedge^{r_N}Q_N\otimes(\det V)^{-N}.
\tag{2.1}
\]

A bounded lattice \(\Lambda\), \(t^NV_O\subset\Lambda\subset t^{-N}V_O\), gives the line

\[
\ell_\Lambda=
\det(\Lambda/t^NV_O)\otimes(\det V)^{-N}
\subset\mathcal F_N^e.
\tag{2.2}
\]

This is the ordinary finite Grassmannian Plücker map, restricted to the lattice stage. Increasing the cutoff inserts the standard occupied vectors \(t^Ne_i\), \(1\le i\le d\), and the corresponding determinant inverse. More generally, the transition to \(M>N\) wedges with the standard tail \(t^NV_O/t^MV_O\), whose determinant is canonically \((\det V)^{M-N}\). It is a linear injective map \(\mathcal F_N^e\to\mathcal F_M^e\). Exact-sequence determinant conventions give compatible transitions and identify the lattice line (2.2) at the two cutoffs. Equivalently, fix the weight basis and the increasing-level order of occupied vectors; normalize tail determinants so the standard tail has coefficient one. This fixes every exterior sign consistently.

Thus \(\mathcal F^e=\varinjlim_N\mathcal F_N^e\) has a basis of finite excitations of the standard occupied tail, and the full lattice ind-scheme embeds into \(\mathbb P(\mathcal F^e)\). Every construction restricts to an ordinary finite projective embedding on a bounded stage. No representation of an affine Lie algebra is involved.

For \(\Lambda_\nu=t^\nu V_O\), let \(a_i=\langle\gamma_i,\nu\rangle\). Its Plücker vector \(v_\nu\) has occupied vectors \(t^me_i\), \(a_i\le m<N\), and weight

\[
\chi_\nu
=\sum_i(N-a_i)\gamma_i-N\sum_i\gamma_i
=-\sum_i\langle\gamma_i,\nu\rangle\gamma_i
=-B\nu.
\tag{2.3}
\]

Here \(B:X_*(T)\to X^*(T)\) denotes the trace pairing defined by those weights. Since determinant characters annihilate coroots, \(e=\sum_i a_i\) is constant on each \(G\)-component. The normalization in (2.1) is therefore compatible with its entire component, not merely with a single torus point.

## 3. The finite-cutoff lift of triangular loops

Order the distinct weights by a linear extension of the positive-root order, with higher weights first. Their sums give a flag of \(V\) preserved by \(N\). The action of \(N\) on each associated graded weight space is the identity: the matrix coefficients of \(u_\alpha(z)\) are polynomials, and torus equivariance says that a coefficient from weight \(\gamma\) to weight \(\gamma'\) is a multiple of \(z^q\) with \(\gamma'-\gamma=q\alpha\), \(q\ge0\); its constant term is the identity. Ordered root products give the assertion for \(N\).

Let \(R\) be any \(k\)-algebra and \(n\in N(R[[t]][1/t])\). Given \(N\), choose \(M\) so large that

\[
n(t^{-N}V_{O_R})\subset t^{-M}V_{O_R},
\qquad
t^MV_{O_R}\subset n(t^NV_{O_R}).
\tag{3.1}
\]

Both conditions follow from common pole bounds for the finitely many entries of \(n\) and \(n^{-1}\). Define finite modules

\[
A=n(t^{-N}V_{O_R})/t^MV_{O_R},\qquad
U=n(t^NV_{O_R})/t^MV_{O_R}.
\tag{3.2}
\]

There are an inclusion \(A\subset Q_M\otimes R\) and an exact sequence

\[
0\longrightarrow U\longrightarrow A
\longrightarrow Q_N\otimes R\longrightarrow0,
\tag{3.3}
\]

where the last identification is induced by \(n^{-1}\).

These are finite locally free modules with locally free quotients, including over rings with nilpotents. To see this directly, intersect with the weight flag. Since \(n\) and \(n^{-1}\) preserve it, the intersection of \(n(t^aV_{O_R})\) with a flag term is \(n\) applied to the corresponding flag term of \(t^aV_{O_R}\). Its graded image is the standard \(t^a\) weight lattice because \(n\) is the identity on the weight graded pieces. Condition (3.1) makes all the quotient filtrations strict. Their graded pieces are the free modules with levels \(-N,\ldots,M-1\), or \(N,\ldots,M-1\), in the appropriate weight space. The complementary quotient \((Q_M\otimes R)/A\) has levels \(-M,\ldots,-N-1\). Successive extensions by free modules split over \(R\). This proves the asserted module properties without assuming flatness of an unspecified intersection.

The weight filtration gives a canonical determinant identification

\[
\det U\simeq(\det V)^{M-N}\otimes R.
\tag{3.4}
\]

It uses the identity action on each graded weight space, not a chosen basis of \(n(t^NV_O)\). The determinant of a filtered module is the tensor product of the determinants of its graded pieces: lift local graded bases and wedge them; changing a lift adds an earlier filtration vector and leaves the wedge unchanged. This elementary construction also proves functoriality and transitivity of (3.4). Normalize it by the standard tail as in Section 2.

There is an explicit polynomial formula for the normalized tail vector. The classes of \(n(t^qe_i)\), \(N\le q<M\), give a basis of \(U\): in the weight filtration their graded classes are precisely the standard basis vectors \(t^qe_i\). Lifting a graded basis generates the filtered module and is independent by induction on the flag. Vectors with \(q\ge M\) project into earlier, higher-weight filtration terms and are already generated there, by that same induction. Wedge these basis vectors in the fixed standard order; (3.4) sends their determinant to the standard tail determinant. Likewise, the classes with \(-N\le q<M\) give a basis of \(A\). Thus (3.5) is computed by taking the transported occupied basis vectors with \(-N\le q<N\), adjoining the transported tail with \(N\le q<M\), and taking their ordinary finite wedge modulo \(t^M\). Only finitely many coefficients of the matrix \(n\) occur. This formula proves polynomial dependence without an unspecified choice of splitting or an inversion of a parameter.

For an exterior vector in \(\bigwedge^{r_N}Q_N\), transport it through (3.3), choose any lifts in \(A\), and wedge them with the determinant of \(U\). Changing a lift by an element of \(U\) gives a wedge with too many \(U\)-vectors and is zero. Cancelling the determinant factors through (3.4) gives a well-defined linear injection

\[
\widehat n_{N,M}:\mathcal F_N^e\otimes R
\longrightarrow\mathcal F_M^e\otimes R.
\tag{3.5}
\]

For a lattice \(\Lambda\) bounded by \(N\), (3.3) restricted to its quotient is precisely

\[
0\to U\to n\Lambda/t^MV_{O_R}
\to\Lambda/t^NV_{O_R}\to0.
\]

Therefore (3.5) carries \(\ell_\Lambda\) to \(\ell_{n\Lambda}\). In particular it is valid when \(n\) has poles; truncating just the transformed generators at the original cutoff would omit \(U\) and would not give this map.

Enlarging \(M\) adds its standard tail and gives the same map in the direct limit. Enlarging \(N\) commutes with inserting its tail. The group law is also exact. For consecutive loops \(m,n\), choose intermediate and final cutoffs \(P,Q\). The combined tail has the exact sequence

\[
0\to n(t^PV_O)/t^QV_O
\to nm(t^NV_O)/t^QV_O
\to m(t^NV_O)/t^PV_O\to0.
\tag{3.6}
\]

The last quotient is identified using \(n^{-1}\). Use the fixed order of transported occupied vectors followed by the transported tail vectors. Applying \(m\) and then \(n\) produces exactly those same vectors as applying \(nm\), with that same order. Any temporary choice of quotient lifts differs by tail vectors and disappears on wedging. The weight-filtered transition determinants are one. This checks the determinant signs as well as the vectors, without changing from a kernel-first to a quotient-first convention midway. Hence \(\widehat n\widehat m=\widehat{nm}\). The identity loop gives the standard transition; applying this to \(n^{-1}\) gives the inverse. We have constructed the canonical lift of \(LN\) to \(\mathcal F^e\) using finite exterior powers only.

The added tail retains the transported high-level vectors that can move below the original cutoff. It is part of the determinant construction before any exterior expansion is taken.

For a concrete rank-one check, take the standard \(SL_2\)-module, \(\nu=0\), \(n=u_\alpha(ct^{-1})\), \(N=1\), \(M=2\). The normalized image of the vacuum is the finite wedge

\[
e_1\wedge(e_2+ct^{-1}e_1)\wedge te_1
\wedge(te_2+ce_1)
=e_1\wedge e_2\wedge te_1\wedge te_2
-c\,t^{-1}e_1\wedge e_1\wedge te_1\wedge te_2.
\tag{3.7}
\]

The other tail correction vanishes because \(e_1\) is already occupied. The first term has weight zero and coefficient one; the second has weight \(\alpha\). Its point at \(c=\infty\) is the occupied lattice \(t^{-1}Oe_1\oplus tOe_2\), namely \(t^{-\alpha^\vee}\). Thus the finite wedge exhibits both the increasing-weight mechanism and the sign of the lower specialization in Section 6. The displayed formula and its interpretation remain valid in characteristic two.

## 4. Increasing weights, and the trace form

For a root loop \(u_\alpha(f)\), give the Laurent coefficients of \(f\) the character \(\alpha\). Choose a common bound for its poles and for its inverse. At any fixed input and output cutoffs, the explicit finite wedge formula after (3.4) makes (3.5) polynomial in finitely many of those coefficients, with no parameter denominators. Torus conjugation is compatible with the normalized tails. Thus each operator coefficient carrying weight \(\chi\) to \(\chi'\) has character \(\chi'-\chi\) and is a polynomial of degree \(q\ge0\) in variables of character \(\alpha\). It is zero unless \(\chi'-\chi=q\alpha\). Its degree-zero part is the identity, obtained by setting \(f=0\).

For arbitrary \(n\in N(F)\), apply the finite ordered positive-root factorization. It follows that

\[
\widehat n v=v+\text{weights strictly above the weight of }v
\tag{4.1}
\]

for every weight vector \(v\); above means addition of a nonzero nonnegative integral combination of simple roots. This also follows directly by exterior expansion of the weight-triangular matrix and the normalized tail. The finite cutoff gives only finitely many resulting exterior basis terms. Replacements of occupied vectors high in the tail do not require an infinite exterior product: they are included in \(U\) and its determinant before the finite wedge is taken.

The bilinear form on the real cocharacter space associated to (2.3) is

\[
B(x,y)=\sum_i\langle\gamma_i,x\rangle\langle\gamma_i,y\rangle.
\]

It is positive definite because the weights generate the character lattice. It is Weyl invariant because a normalizer representative permutes the weight spaces with multiplicity. Reflection invariance gives

\[
B(\alpha_i^\vee)
=c_i\alpha_i,\qquad
c_i=\tfrac12 B(\alpha_i^\vee,\alpha_i^\vee)>0.
\tag{4.2}
\]

Indeed the reflection negates \(\alpha_i^\vee\), while its action on a character \(\chi\) is \(\chi-\langle\chi,\alpha_i^\vee\rangle\alpha_i\); comparison gives (4.2). These are rational numbers computed from an integral lattice pairing. No Lie-algebra trace form in the field's characteristic is being used; positivity is a statement over \(\mathbb R\), so bad characteristic cannot make it degenerate.

If \(\kappa(\eta)=\kappa(\nu)\), write \(\nu-\eta=\sum m_i\alpha_i^\vee\), \(m_i\in\mathbb Z\). The simple roots are linearly independent, and (4.2) shows

\[
\chi_\eta\ge\chi_\nu
\Longleftrightarrow m_i\ge0\text{ for all }i
\Longleftrightarrow\eta\le\nu.
\tag{4.3}
\]

Here the left inequality uses the nonnegative integral root cone. If it holds, its real coefficients \(m_ic_i\) are nonnegative, so the integral \(m_i\) are nonnegative. Conversely \(B(\alpha_i^\vee)=c_i\alpha_i\) is an integral character and lies in the integral root lattice in this situation: explicitly \(c_i=\sum_{q>0}q^2\dim V_{q,i}\) after grouping the \(SL_2\)-torus weights \(q\) and \(-q\); hence \(c_i\) is an integer. This proves the converse in the integral cone too. The component condition is indispensable; positivity of the trace form alone does not recover an integral coroot difference.

## 5. The orbit partition and the closed weight condition

The proof of GL-SAT-01, Lemma 4.0, extends from its stated finite field to algebraically closed \(k\) without any change. For clarity: extend \(g^{-1}B\in(G/B)(F)\) to an \(O\)-point using the projective embedding and a common homogeneous-coordinate valuation. The special fibre has a lift in \(G(k)\) by the flag cells. Smoothness of the affine \(B\)-torsor lifts it successively modulo \(t^m\); finite presentation and completeness give a lift \(h\in G(O)\). Thus \(g=b h^{-1}\), and \(B=N\rtimes T\), together with torus coordinate valuations, gives \(g=n t^\nu K\). If two such expressions have indices \(\eta,\nu\), their ratio lies in \(B(F)\cap G(O)=B(O)\), since \(B\) is closed and \(O\hookrightarrow F\). Projection to \(T\) forces every valuation of \(t^{\nu-\eta}\) to vanish, hence \(\eta=\nu\). This proves the partition over every algebraically closed extension field of \(k\).

Let \(\mathcal F_{\ge\chi}\) be the sum of weight spaces whose weights differ from \(\chi\) by a nonnegative integral combination of simple roots, and define \(\mathcal F_{>\chi}\) similarly with nonzero difference. Equation (4.1) says that the Plücker line of every point of \(S_\eta\) has a nonzero \(\chi_\eta\) component proportional to \(v_\eta\), with all its other components strictly greater. In the normalization (3.5) that coefficient is one; changing a vector representative of the line multiplies it by a nonzero scalar.

Restrict to the component \(\kappa(\nu)\). By the partition and (4.3), the underlying support of

\[
\operatorname{Gr}_{G,\kappa(\nu)}
\cap\mathbb P(\mathcal F_{\ge\chi_\nu})
\tag{5.1}
\]

is exactly \(\bigcup_{\eta\le\nu}S_\eta\). Its condition is closed on every bounded stage: intersect the fixed weight subspace with \(\mathcal F_N^e\) and impose ordinary linear equations on its Plücker line. The component is open and closed by GL-SAT-04. These conditions commute with increasing cutoffs. Therefore the union is closed as a support in the reduced ind-variety. The analogous strict-weight condition has support \(\bigcup_{\eta<\nu}S_\eta\).

## 6. Rank-one lower specializations and the boundary equation

For a positive simple root \(\alpha\), put \(m=\langle\alpha,\nu\rangle\). The explicit scaled map is
\[
\begin{pmatrix}a&b\\c&d\end{pmatrix}
\longmapsto\varphi_\alpha
\begin{pmatrix}a&t^{m-1}b\\t^{1-m}c&d\end{pmatrix}.
\]
The inner matrix map is conjugation by \(\operatorname{diag}(t^{m-1},1)\) in \(GL_2(F)\), so preserves \(SL_2\) and its multiplication. Its upper root is \(u_\alpha(c t^{m-1})\), its lower root is \(u_{-\alpha}(c t^{1-m})\), and its Weyl representative is \(t^{(m-1)\alpha^\vee}n_{s_\alpha}\). The central kernel of \(\varphi_\alpha\) is retained in the stabilizer.

The lower root and constant torus stabilize \(t^\nu K\): conjugating by \(t^{-\nu}\) makes the lower root parameter \(ct\). The scaled \(SL_2\)-orbit therefore gives a morphism

\[
SL_2/B^-\simeq\mathbb P^1\longrightarrow\operatorname{Gr}_G.
\tag{6.1}
\]

Its affine upper-root chart is \(c\mapsto u_\alpha(c t^{m-1})t^\nu K\), wholly contained in \(S_\nu\). The root intersection with the stabilizer is zero, because after conjugation the upper parameter is \(ct^{-1}\), integral precisely for \(c=0\). On the other chart the Weyl representative sends the torus point to

\[
t^{(m-1)\alpha^\vee}n_{s_\alpha}t^\nu K
=t^{\nu-\alpha^\vee}K.
\tag{6.2}
\]

This fixes the sign directly, without identifying a loop translation with a differently signed apartment action. The chart transition is the usual upper/lower triangular \(SL_2\) transition, and its stabilizing factors give a regular map at infinity. It works when \(m\) is negative or zero as well. Since the source is quasi-compact, its lattice representatives on the two charts have a common finite bound, so (6.1) is an actual finite-stage specialization. Consequently \(t^{\nu-\alpha^\vee}\in\overline{S_\nu}\). The closure is \(N(F)\)-stable, so it contains the entire lower orbit. Iterating these simple-coroot curves proves all lower inclusions. Combining them with (5.1) proves the closure equality in (1.1), with reduced structures.

Choose the exterior-basis coordinate functional \(f_\nu\) that equals one on \(v_\nu\), vanishes on the other basis vectors of its weight, and vanishes on all other weights. The compatible finite-excitation basis defines it on the direct limit, so its restrictions are compatible finite-stage linear forms. Let \(H_\nu=\{f_\nu=0\}\). On \(S_\nu\), (4.1) gives \(f_\nu\ne0\). On \(S_\eta\), \(\eta<\nu\), the leading weight is strictly above \(\chi_\nu\), and every other weight is higher still, so \(f_\nu=0\). This proves the boundary equality in (1.1). It also makes \(S_\nu\) a locally closed reduced locus in every bounded stage: it is the complement of this hyperplane in its closed semi-infinite closure support.

## 7. Finite orbit indices, attraction, and hyperplane dimension

Write \(Z_\lambda=\overline{\operatorname{Gr}^{\lambda}}\) for the reduced projective Schubert variety. It is integral of dimension \(D=\langle2\rho,\lambda\rangle\).

Choose a strictly dominant integral cocharacter \(\xi\), for instance the sum of positive coroots. For \(n=\prod_{\alpha>0}u_\alpha(f_\alpha)\), conjugation by \(\xi(s)\) replaces each parameter by \(s^{\langle\alpha,\xi\rangle}f_\alpha\). This is a loop over \(k[s]\) with a uniform pole bound and extends to the identity at \(s=0\). Hence every \(x\in S_\eta\) has an actual finite-stage curve with

\[
\lim_{s\to0}\xi(s)x=t^\eta.
\tag{7.1}
\]

If \(x\in Z_\lambda\), its whole curve lies there by torus stability and closedness. Thus \(t^\eta\in Z_\lambda\). Conversely that torus point itself lies in \(S_\eta\cap Z_\lambda\).

The earlier Cartan closure theorem makes this equivalent to \(\eta^+\le\lambda\), where \(\eta^+\) is the dominant Weyl translate. For every such \(\eta\),

\[
w_0\lambda\le\eta\le\lambda.
\tag{7.2}
\]

Indeed a dominant coweight minus any Weyl translate is a nonnegative integral sum of simple coroots: apply a reduced Weyl word and use its positive inversion roots and the nonnegative dominant pairings. Combine this with \(\lambda-\eta^+\in Q^\vee_+\); apply \(w_0\) for the other inequality. There are finitely many possible \(\eta\). Alternatively, the bounded lattice realization of \(Z_\lambda\), applied to \(t^\eta\), bounds every \(\langle\gamma_i,\eta\rangle\); the weights generate the character lattice, so this integral box is finite. Therefore \(Z_\lambda\) has a finite partition into the locally closed loci \(S_\eta\cap Z_\lambda\).

By (7.2), \(Z_\lambda\subset\overline{S_\lambda}\). Since it contains \(t^\lambda\notin H_\lambda\),

\[
A_0=S_\lambda\cap Z_\lambda
=Z_\lambda\setminus H_\lambda
\tag{7.3}
\]

is a nonempty dense open irreducible locus of dimension \(D\). This proves the needed top extreme without importing a negative-loop orbit-intersection theorem.

Here is the hyperplane fact used in both dimension chains. If \(Y\) is an integral projective variety of dimension \(d>0\) in a finite projective space, and a hyperplane does not contain \(Y\), then its section is nonempty and every irreducible component has dimension \(d-1\). Its homogeneous coordinate ring \(A\) is a finitely generated standard graded domain of dimension \(d+1\). The hyperplane form is nonzero. Every prime minimal over it has height one by the earlier principal ideal theorem: height zero is impossible in a domain. The earlier finite-type domain height formula gives \(\dim A/\mathfrak p=d\). These primes are homogeneous: for a prime minimal over a graded ideal, the ideal generated by its homogeneous elements still contains the given ideal and is prime. Indeed the prime test holds for homogeneous elements by the original prime test; taking lowest nonzero graded terms makes its quotient a domain. Minimality makes this homogeneous prime the original prime. They cannot be the irrelevant maximal ideal when \(d>0\), since that ideal has height \(d+1\). Taking Proj gives nonempty components of dimension \(d-1\). The dimension calculation is elementary on a degree-one chart: \(A_f=(A_f)_0[f,f^{-1}]\), where different powers of \(f\) have different degrees, so this is a Laurent polynomial algebra over the degree-zero chart algebra. Nonempty opens of a finite-type field domain have its dimension, by the earlier height formula at closed points. Thus the chart dimension is one less than the cone dimension. These charts cover all nonirrelevant homogeneous primes. This proves the fact with the stated earlier algebra rather than treating a hyperplane citation as a proof.

Finally, an irreducible closed subvariety \(Y\subset Z_\lambda\) has a unique dense orbit locus in this finite partition: its generic point belongs to some \(S_\mu\), whose intersection with \(Y\) is locally closed and contains the generic point, hence contains a dense open. In fact \(Y\subset\overline{S_\mu}\), and the boundary hyperplane makes \(Y\cap S_\mu=Y\setminus H_\mu\), a dense open irreducible subset. This identifies the required generic index without assuming that it is a whole component of a different intersection.

## 8. The downward dimension chain

Let \(C\) be an irreducible component of \(S_\nu\cap Z_\lambda\), and let \(d=\dim C\). Its closure \(Y_0=\overline C\) is integral projective of dimension \(d\), contained in \(\overline{S_\nu}\), and its dense open is \(C\). If \(d>0\), the hyperplane \(H_\nu\) is nonzero on that open, so choose an irreducible component \(Y_1\) of \(Y_0\cap H_\nu\). It is nonempty of dimension \(d-1\). Its dense orbit locus has an index \(\nu_1<\nu\). Repeat on \(Y_1\), using \(H_{\nu_1}\), until the dimension is zero. At each positive dimension, projectivity and the hyperplane fact guarantee the next nonempty section. No assertion that an intermediate locus is a component of \(S_{\nu_j}\cap Z_\lambda\) is needed.

This gives \(d\) strict drops

\[
\nu=\nu_0>\nu_1>\cdots>\nu_d\ge w_0\lambda.
\]

Since \(\langle\rho,\alpha_i^\vee\rangle=1\), every nonzero integral positive-coroot drop has \(\rho\)-height at least one. Therefore

\[
d\le\langle\rho,\nu-\nu_d\rangle
\le\langle\rho,\nu-w_0\lambda\rangle.
\tag{8.1}
\]

The endpoint need not equal \(w_0\lambda\). Its lower bound is enough. In particular this argument proves that the bottom intersection has dimension zero, rather than assuming an unproved bottom extreme.

## 9. The chain containing the chosen component

This chain begins with \(Y^0=Z_\lambda\), generic index \(\mu_0=\lambda\), and keeps the fixed closed irreducible subvariety \(\overline C\) inside every chosen \(Y^j\). Suppose \(Y^j\) has generic index \(\mu_j\). Then \(Y^j\subset\overline{S_{\mu_j}}\), so \(C\subset Y^j\cap S_\nu\) forces \(\nu\le\mu_j\).

If \(\mu_j=\nu\), the dense open irreducible set \(Y^j\cap S_\nu\) contains \(C\). It is closed inside \(S_\nu\cap Z_\lambda\), because \(Y^j\) is closed in \(Z_\lambda\). The maximality of the irreducible component \(C\) therefore gives \(Y^j\cap S_\nu=C\), and \(\dim Y^j=\dim C\). This is the stopping rule.

If \(\mu_j>\nu\), the boundary equation puts \(\overline C\) in \(Y^j\cap H_{\mu_j}\). It is nonempty, while \(H_{\mu_j}\) does not contain the dense generic orbit locus of \(Y^j\). Choose an irreducible component \(Y^{j+1}\) of that section containing \(\overline C\). It has dimension exactly one less. Its generic index satisfies

\[
\nu\le\mu_{j+1}<\mu_j.
\]

The process must stop: the integer height \(\langle\rho,\mu_j-\nu\rangle\) strictly decreases and remains nonnegative. It cannot terminate at a different index in dimension zero, because a zero-dimensional integral variety is a point and cannot contain the nonempty locus \(C\subset S_\nu\) while its generic point belongs to a different orbit. Thus it stops at \(\mu_e=\nu\), with

\[
\dim C=D-e,
\qquad e\le\langle\rho,\lambda-\nu\rangle.
\tag{9.1}
\]

Combining (8.1) and (9.1), and using \(\rho\circ w_0=-\rho\), gives

\[
\langle\rho,\lambda+\nu\rangle
=D-\langle\rho,\lambda-\nu\rangle
\le\dim C
\le\langle\rho,\nu-w_0\lambda\rangle
=\langle\rho,\lambda+\nu\rangle.
\]

Equality holds throughout. Every component has the required dimension, so the closed-Schubert intersection is equidimensional. The fixed component is retained throughout the upward chain, so the stopping argument applies to each of its components.

## 10. The open Schubert orbit and the opposite statement

The nonempty closed-Schubert intersection has pure dimension \(d=\langle\rho,\lambda+\nu\rangle\). Its complement inside the open Schubert orbit is contained in the finite union of \(S_\nu\cap Z_\tau\), where \(\tau<\lambda\) is dominant in the same component. Apply the already established closed-intersection formula to each \(\tau\). Every nonempty such intersection has dimension

\[
\langle\rho,\tau+\nu\rangle
<\langle\rho,\lambda+\nu\rangle,
\]

because \(\lambda-\tau\) is a nonzero integral positive-coroot sum. A finite union of these smaller-dimensional closed subsets cannot contain any component \(C\). Thus each component meets \(\operatorname{Gr}^{\lambda}\) in a nonempty dense open. Their intersections give precisely the components of \(S_\nu\cap\operatorname{Gr}^{\lambda}\), with the same pure dimension. This proves both the open-orbit nonemptiness criterion and dimension, including the case \(d=0\), when the smaller-dimensional intersections are necessarily empty.

For \(T_\nu=N^-(F)t^\nu K/K\), act by a representative of \(w_0\). It identifies this locus with \(S_{w_0\nu}\), preserves the Schubert variety indexed by the dominant representative, and reverses \(\rho\). If the Schubert index \(\lambda\) is written antidominantly, its dominant representative is \(w_0\lambda\), giving

\[
\dim(T_\nu\cap\overline{\operatorname{Gr}^{\lambda}})
=\dim(T_\nu\cap\operatorname{Gr}^{\lambda})
=-\langle\rho,\lambda+\nu\rangle
\]

when nonempty, with the same torus-point criterion and pure-dimensional interpretation.


## 11. Classical sheaf operations and finite-stage attractors

We use the actual classical proofs in Constructible complexes on algebraic varieties: F.1–F.2 for compact-support cohomological dimension; H.1–H.6 for proper-support base change, adjunction, projection and dual exchanges; and J–K for constructible biduality and finiteness. The product calculation in Equivariant perverse sheaves and perverse sheaves on stacks, Lemma B.5, proves that projection from a product with a contractible manifold is acyclic on inverse images of arbitrary base sheaves. The bounded perverse t-structure and finite length are proved in The perverse t-structure, Theorem 2.1 and §5. Intermediate extension and its strict boundary bounds are proved in Intermediate extensions and intersection complexes, §1. These are earlier programme proofs, rather than external theorem citations.

Here is the product comparison used with an ordinary, possibly nonproper, map \(f:Y\to S\). For a contractible disc \(D\), the natural map
\[
\operatorname{pr}_S^*Rf_*K\longrightarrow
R(1_D\times f)_*\operatorname{pr}_Y^*K
\]
is an isomorphism. On a product open \(D'\times U\), Lemma B.5 identifies both sides with \(R\Gamma(f^{-1}U,K)\). Such product opens form a basis. The identifications are induced by the adjunction unit, so they glue and preserve the natural comparison maps. The same argument applies to the contractible slit regions used below.

Let \(Y\) be a finite union of projective Schubert varieties and choose a lattice bound containing it. The exterior-power embedding of §2 is \(T\)-equivariant, so a dominant cocharacter acts through a finite weight representation on that stage. Choose \(\xi=2\rho^\vee\), the sum of positive coroots. It pairs positively with every positive root. Formula (7.1) proves that the attracting point set of \(t^\nu\) is \(S_\nu\cap Y\): every point belongs to exactly one \(S_\eta\), and its limit is exactly \(t^\eta\). Separatedness makes that limit unique. Replacing \(\xi\) by \(-\xi\) gives the repeller \(T_\nu\cap Y\). The fixed point set is therefore the finite set of torus points occurring in \(Y\).

The graded-coordinate charts in §12 construct the actual finite-type attractor and repeller schemes. Their underlying reduced loci are these semi-infinite intersections. We do not identify their full nilpotent functors with reduced orbit loci. For classical sheaves, nilpotent scheme structure has no effect on the analytic space or its sheaves. Thus hyperbolic restriction at each fixed point computes precisely the compact-support and extraordinary-restriction functors used below. When \(G\) is a torus, \(\xi=0\); the reduced Schubert stages are finite sets of points and the same statement holds.

## 12. Classical coefficient and geometry hypotheses

Let \(\Lambda\) be a characteristic-zero field, as in the sheaf-theoretic scope of this lesson. Work with bounded algebraically constructible complexes of finite-dimensional \(\Lambda\)-vector spaces on complex algebraic varieties, using their analytic topologies. Write \(D_X\) for the classical Verdier dual. The earlier proofs listed in §11 show that these operations preserve bounded constructibility.

For a \(\mathbb C^*\)-action \(a\), call \(F\) weakly equivariant if
\[
 a^*F\simeq L\boxtimes F                                   \tag{WE}
\]
for a finite-rank local system \(L\) on \(\mathbb C^*\); no claim of coherent equivariance is built into this definition. Naive equivariance is the case \(L=\Lambda\). If \(F\ne0\), finite-dimensional stalks already force \(\operatorname{rank}L=1\), but the circle calculation below works for every finite-rank \(L\).

Equivariant inverse images, direct images, proper-support images and exceptional inverse images preserve (WE). For \(f_*\), use the product comparison proved above on contractible discs in \(\mathbb C^*\), and trivialize \(L\) there; it yields \(Rf_*(L\boxtimes F)=L\boxtimes Rf_*F\). The equivariant action square is a product square after an isomorphism of its upper corner. For \(f_!\), use actual proper-support base change and the local projection formula. Duality sends (WE) to the corresponding statement with \(L^\vee\): action and projection are both smooth of relative dimension one, so their common orientation shift \([2]\) cancels. The proved identity \(f^!=D f^*D\) then proves preservation by \(f^!\). Open extension by zero and closed direct image are included. Replacing the action by its inverse replaces \(L\) by inversion-pullback. A natural isomorphism proved for these objects also holds on their finite extension/cone closure, by the exact triangle axiom.

We require either a specified equivariant closed embedding \(X\hookrightarrow\mathbb P(W)\), with \(W\) a finite-dimensional weight representation, or specified invariant affine charts with finite homogeneous coordinate generators. No local-linearization theorem is invoked to obtain these data.

Denote by \(X^0,X^+,X^-\) the fixed, attracting and repelling spaces, with evaluation maps
\[
 X^0\xrightarrow{i^\pm}X^\pm\xrightarrow{p^\pm}X,
 \qquad q^\pm:X^\pm\to X^0,\quad q^\pm i^\pm=1.
\]
For an affine scheme with graded coordinate ring, these spaces are obtained by setting the coordinates of the prohibited weight signs to zero, and \(q^\pm\) sets the remaining nonzero weights to zero. A finite homogeneous generating set gives an equivariant closed embedding into a weight vector space. The description is schematic: a homogeneous function on an equivariant \(\mathbb A^1_R\) is its value at 1 times the appropriate nonnegative power of the parameter, while a prohibited negative power must have zero coefficient.

For \(X\subset\mathbb P(W)\), attractors and repellers are disjoint unions indexed by the finitely many weights of their limits. On eigen-coordinate charts the preceding affine descriptions represent them and glue. In the projective weight decomposition, a nonzero point's attracting limit is its lowest nonzero weight and its repelling limit its highest. The same description is schematic on each homogeneous-coordinate chart. The diagonal
\[
 e:X^0\longrightarrow X^+\times_X X^-
\]
is open and closed: the summands with equal limit weights are exactly the fixed locus, by the affine coordinate description; the pairs of limit weights index open-and-closed summands of the fiber product. Nilpotent coefficients are included in the coordinate ideals, not discarded by a pointwise assertion.

## 13. The relative affine-line calculation

Let \(q:\mathbb C\times S\to S\), let \(j:\mathbb C^*\times S\hookrightarrow\mathbb C\times S\), and let \(z:S\hookrightarrow\mathbb C\times S\) be the zero section. For \(B\in D_c^b(S,\Lambda)\),
\[
 Rq_*q^*B\simeq B,\qquad
 Rq_*j_!(L\boxtimes B)=0.                                 \tag{A1}
\]
The first isomorphism is the adjunction unit, and its inverse is restriction to any constant section. It follows from the contractible-product calculation of the product calculation in §11, applied termwise to the finite ordinary cohomology tower.

Here is a proof of the second assertion which retains a nontrivial \(L\). Cover \(\mathbb C^*\) by two angular slit regions. Each region is contractible, and their intersection consists of two contractible regions. Trivialize \(L\) on the slit regions; the transition on one overlap can be made the identity, and on the other it is the monodromy \(T\). The two-term Čech complex has differential \((v,w)\mapsto(v-w,v-Tw)\). Canceling one identity summand reduces it to
\[
 [V\xrightarrow{T-1}V],\qquad V=L_1,
\]
in degrees 0 and 1. The identical slit cover on every punctured disc about 0 gives the same complex. Restriction from \(\mathbb C^*\) to a punctured disc induces its identity, compatibly with smaller radii. This is the actual cochain comparison, not merely equality of cohomology ranks.

On products with \(S\), each slit-region projection is universally acyclic by the already proved arbitrary-base-sheaf lemma. Thus the same computation has \(V\otimes B\) in place of \(V\). It computes both
\[
 Rq_*Rj_*(L\boxtimes B),\qquad z^*Rj_*(L\boxtimes B),
\]
and their restriction map is an isomorphism. Apply \(Rq_*\) to the boundary triangle
\[
 j_!(L\boxtimes B)\to Rj_*(L\boxtimes B)
 \to z_*z^*Rj_*(L\boxtimes B)\to.
\]
Since \(qz=1\), the second arrow becomes precisely the isomorphism just computed. This proves (A1).

Consequently, if \(K\in D_c^b(\mathbb C\times S)\) has \(j^*K\simeq L\boxtimes B\), then the **restriction** map
\[
 Rq_*K\longrightarrow z^*K                                \tag{A2}
\]
is an isomorphism. Apply \(Rq_*\) to \(j_!j^*K\to K\to z_*z^*K\). This deduction is important: it does not assert ordinary base change at 0 for an arbitrary nonproper projection.

Finally, an endomorphism \(u:q^*B\to q^*B\) which is zero at 0 and invertible at 1 forces \(B=0\). The natural restriction maps \(Rq_*q^*B\to B\) at both sections are isomorphisms by (A1); naturality makes \(Rq_*u\) simultaneously zero and invertible.

## 14. Projective contraction, with the graph argument written out

Let \(A,B\) be weight vector bundles over a complex variety \(S\) on which the torus acts trivially. Suppose every weight of \(A\) is strictly greater than every weight of \(B\). Put
\[
 Y=\mathbb P(A\oplus B)\setminus\mathbb P(A),\quad
 Z=\mathbb P(B),\quad i:Z\hookrightarrow Y,
\]
and let \(\pi:Y\to Z\) be projection to the \(B\)-line. Write \(\tau:Z\to S\), which is proper, and \(f=\tau\pi\). For a weakly equivariant \(F\), the natural restriction and counit maps are isomorphisms
\[
 Rf_*F\longrightarrow R\tau_*i^*F,
 \qquad R\tau_!i^!F\longrightarrow Rf_!F.                  \tag{PC}
\]
The pushforward to \(S\) in this statement is essential: the action on \(Z\) need not be trivial, and no false local assertion \(R\pi_*F=i^*F\) is being used.

It suffices for the first assertion to prove \(Rf_*F_U=0\), where \(U=Y\setminus Z\), \(\sigma:U\hookrightarrow Y\), and \(F_U=\sigma_!\sigma^*F\). Form the closure \(\Gamma\) of the action graph in
\(\mathbb C\times Y\times\mathbb P(A\oplus B)\), with projections \(r_1,r_2\) to the first coordinate and respectively the first and second projective points. Both are isomorphisms over \(\mathbb C^*\). The following coordinates prove the required properness and zero-fiber claim.

Choose weight coordinates \(y_i,z_i\) in \(A\) of weights \(a_i\) and \(y_j,z_j\) in \(B\) of weights \(b_j\). On the graph,
\[
 y_jz_i=t^{a_i-b_j}y_i z_j.                                \tag{G}
\]
These are regular equations since \(a_i-b_j>0\), so they hold on its closure. At \(t=0\), some \(B\)-coordinate of the first point is invertible on an appropriate projective chart because the first point lies in \(Y\). Equations (G) force every \(A\)-coordinate of the second point to vanish. The second point therefore lies in \(Z\). For \(t\ne0\), it already lies in \(Y\). Thus the entire closure lies in \(\mathbb C\times Y\times Y\); its projection \(r_1\) is proper, being closed in the projective bundle over \(\mathbb C\times Y\). Moreover
\[
 r_2^{-1}(\mathbb C\times U)=\mathbb C^*\times U,
\]
on which \(r_1\) identifies the restriction of \(r_2\) with the action. All these claims are local in a weight frame and hence glue. The equations establish the same schematic open containment over rings as well; no division by a weight integer occurs.

Let \(Q=1_{\mathbb C}\times f\), \(p_Y:\mathbb C\times Y\to Y\), and
\[
 C=Rf_*F_U,\qquad
 D=RQ_*Rr_{2*}r_2^*p_Y^*F_U.
\]
Since \(fr_1=fr_2\), composition, the properness of \(r_1\), and proper-support base change for extension by zero give
\[
 D\simeq RQ_*(j\times\sigma)_!a^*\sigma^*F
   \simeq RQ_*j_!(L\boxtimes F_U).                         \tag{D}
\]
On \(\mathbb C^*\times S\), the isomorphism \(r_2\) and product comparison give \(D|_{\mathbb C^*\times S}\simeq q^*C\), where now \(q:\mathbb C\times S\to S\). By (A2), \(z^*D\simeq Rq_*D\). On the other hand, push (D) to \(S\) and compose in the other order:
\[
 Rq_*D\simeq Rf_*R(p_Y)_*j_!(L\boxtimes F_U)=0
\]
by (A1) with base \(Y\). Thus \(z^*D=0\), and localization identifies \(D\) with \(j_!j^*q^*C\).

The unit for \(r_2^*\dashv Rr_{2*}\), followed by \(RQ_*\), gives \(q^*C\to D\). At 1 it is an isomorphism. Compose it with the extension-by-zero map
\(D=j_!j^*q^*C\to q^*C\). This is an endomorphism of \(q^*C\), invertible at 1 and zero at 0. The last conclusion of §13 gives \(C=0\). The localization triangle for \(U\subset Y\) proves the first map in (PC). Apply that assertion to \(D_YF\), use constructible biduality and both proved dual exchanges, and dualize; this gives exactly the second map in (PC), with its counit direction. This completes the contraction proof.

## 15. The canonical map and the linear-space proof

For the fiber product \(W=X^+\times_X X^-\), denote its projections by \(r:W\to X^-\), \(s:W\to X^+\). Proper-support base change, by adjunction, gives the extraordinary/ordinary exchange
\[
 p^{-!}Rp^+_*\simeq Rr_*s^!.
\]
One can check its direction by pairing both sides against a test complex and applying the already proved \(*\)-\(!\) base-change isomorphism. The unit \(F\to Rp^+_*p^{+*}F\), this exchange, and projection to the open-and-closed summand \(e:X^0\hookrightarrow W\), give
\[
 i^{-*}p^{-!}F\longrightarrow i^{+!}p^{+*}F.                \tag{B}
\]
More explicitly the middle step is
\(i^{-*}Rr_*s^!p^{+*}F\to i^{-*}Rr_*e_*e^!s^!p^{+*}F\);
since \(re=i^-\), \(se=i^+\), it ends at \(i^{+!}p^{+*}F\). Precompose the restriction \(Rq^-_*\to i^{-*}\), and postcompose the counit \(i^{+!}\to Rq^+_!\). This defines (HL), functorially in \(F\), before asserting it is invertible.

First suppose \(X=V=A\oplus B\oplus V_0\), with positive, negative and zero weights respectively. Regard \(V_0\) as the base \(S\). The attracting and repelling spaces are \(A\times S\) and \(B\times S\), and their intersection is \(S\). Applying (PC) to \(\mathbb P(E\oplus\mathcal O_S)\setminus\mathbb P(E)\), with the action inverted if needed, proves vector contraction:
\[
 Rq^-_*K\simeq i^{-*}K,\qquad
 i^{+!}K\simeq Rq^+_!K                                   \tag{VC}
\]
for the appropriate weakly equivariant complexes. The second map is the dual version of the first. These are the actual restriction and counit maps used above.

Let \(j:V\setminus A\hookrightarrow V\) and \(F_0=j_!j^*F\). The localization triangle
\(F_0\to F\to p^+_*p^{+*}F\to\), after \(i^{-*}p^{-!}\), identifies (B) with its second arrow: the square \(A\cap B=S\) is Cartesian, so proper closed base change makes its last term \(i^{+!}p^{+*}F\). It remains to show
\[
 Rq^-_*p^{-!}F_0=0.                                      \tag{V0}
\]

Set
\[
 Y=\mathbb P(A\oplus B\oplus\mathcal O_S)\setminus\mathbb P(B),
 \quad Z=\mathbb P(A\oplus\mathcal O_S),
\]
and let \(\rho:V\hookrightarrow Y\) be the chart where the last coordinate is nonzero. The composite \(i'=\rho p^-:B\hookrightarrow Y\) is closed: it is cut out by all \(A\)-coordinates; excluding \(\mathbb P(B)\) forces the last coordinate to be nonzero. Let \(j':Y\setminus B\hookrightarrow Y\), and put \(\bar F=\rho_!F_0\). Push the triangle
\[
 i'_*i'^!\bar F\to\bar F\to Rj'_*j'^*\bar F\to
\]
along \(f:Y\to S\).

Its first term is \(Rq^-_*p^{-!}F_0\), since \(\rho^!\rho_!=1\) for the open chart. Its second term vanishes by (PC) for the inverse action: all weights of \(B\) are greater, for that action, than the weights of \(A\oplus\mathcal O_S\), and \(i_Z^*\bar F=0\) because \(F_0\) vanishes on \(A\).

The open complement of \(B\) in \(Y\) is
\[
 Y'=\mathbb P(A\oplus B\oplus\mathcal O_S)
           \setminus\mathbb P(B\oplus\mathcal O_S).
\]
Again use the inverse action. Here the high-weight bundle is \(B\oplus\mathcal O_S\), the low-weight bundle is \(A\), and (PC) contracts after pushforward to \(\mathbb P(A)\). The restriction of \(j'^*\bar F\) to \(\mathbb P(A)\) is zero: it is extension by zero from the chart with last coordinate nonzero. Hence its pushforward to \(S\) is zero. By composition this is the third term \(Rf_*Rj'_*j'^*\bar F\). The triangle now proves (V0). Combining it with (VC) proves (HL) for \(V\). If \(A=0\) or \(B=0\), (VC) gives the assertion directly, so empty projective bundles need not be introduced.

## 16. Closed affine subvarieties and projective charts

Let \(b:X\hookrightarrow V\) be an equivariant closed immersion into a weight vector space. Its ideal is homogeneous, and the schematic coordinate description of §12 proves
\[
 X^\pm=X\times_V V^\pm,
 \qquad X^0=X\times_V V^0.
\]
Indeed each homogeneous equation restricts along an equivariant affine-line map to its value at 1 times a permitted power; vanishing at 1 therefore forces the whole map to lie in \(X\). Equations of prohibited weight already vanish in \(V^\pm\). Thus the closed base-change squares are actual schematic squares. Proper closed base change and composition identify
\[
 L_V^\pm b_*F\simeq b^0_*L_X^\pm F,
 \quad L^-=Rq^-_*p^{-!},\quad L^+=Rq^+_!p^{+*}.
\]
The unit, exchange and counit descriptions in §15 commute with these identifications: the relevant adjunction composites pull back the same section/support, and proper-support base change is compatible with pasting by Appendix H.2 of the constructible-complexes lesson. Hence the image of (HL) for \(X\) is the map for \(V\) applied to \(b_*F\). Closed direct image is conservative on stalks, so the vector-space result proves (HL) for \(X\). Any finite homogeneous coordinate generators provide this embedding for an affine \(X\).

Now suppose \(X\hookrightarrow\mathbb P(W)\) is specified. Eigen-coordinate opens \(D(\ell)\) are invariant affine opens. Each is an affine space with linear weights given by differences from the weight of \(\ell\), and \(X\cap D(\ell)\) is a closed affine subvariety. They cover \(X^0\), since a fixed line belongs to an individual weight space and has some nonzero eigen-coordinate.

For an invariant open \(U\subset X\),
\[
 U^\pm=X^\pm\times_{X^0}U^0.                             \tag{O}
\]
To prove this, an orbit whose limit belongs to \(U\) cannot meet the invariant closed complement: its closed orbit closure would then put its limit in that complement. This argument on geometric points gives precisely the required open containment over all base rings; the affine-coordinate description identifies the resulting attractor functors. An orbit lying in \(U\) may have its limit outside \(U\); (O) does not assert the false identity \(U^\pm=(p^\pm)^{-1}U\).

Restriction of ordinary direct image to a target open is base change, by restricting injective resolutions; proper-support image has actual arbitrary base change. Exceptional inverse image is local on both its source and target, by composition with open immersions. Therefore restricting (HL) to \(U^0\) gives its construction for \(F|_U\). All fixed eigen-coordinate charts satisfy the affine theorem, and restriction to their cover is conservative. This proves (HL) on \(X\), with its canonical map and weak equivariance.

The exterior-power embedding in §2 and the finite-stage reduction in §11 supply exactly these charts for the Grassmannian. Every supported complex in what follows is treated on an actual finite projective stage.


## 17. Concentration and exactness of weight functors

Let \(P\) be an \(L^+G\)-equivariant perverse sheaf supported on a finite projective Schubert union \(Y\). A sufficiently high jet quotient of \(L^+G\) acts on this support. Coherent equivariance along a transitive smooth orbit implies that each ordinary cohomology sheaf is locally constant there: pull it back along the smooth orbit map, use the equivariance isomorphism to make it constant, then use local sections to descend lissity. Restriction along \(\xi\) gives the naive equivariance required for hyperbolic restriction.

Write \(O_\lambda=\operatorname{Gr}^{\lambda}\), \(d_\lambda=\langle2\rho,\lambda\rangle\), and \(h_\nu=\langle2\rho,\nu\rangle\). The intrinsic perverse support condition, together with this lissity, gives
\[
\mathcal H^b(P|_{O_\lambda})=0\quad(b>-d_\lambda).
\]
Indeed a nonzero lisse sheaf on the orbit has support of its full dimension \(d_\lambda\), so the support inequality forces this bound.

For a complex algebraic variety \(Z\) of dimension at most \(d\), every constructible sheaf \(A\) has \(H_c^a(Z,A)=0\) for \(a>2d\). To prove it, take a finite smooth stratification adapted to \(A\), using Appendix K of the earlier constructible-complexes lesson. A stratum of complex dimension \(e\) has real coordinate charts of dimension \(2e\), so Appendix F.2 bounds its compact-support cohomological dimension by \(2e\). A closed-open filtration and its localization sequences prove the assertion by finite induction. The bound is \(2d\); a Čech cover does not add a degree to it.

By the dimension theorem of §§8–10, a cohomology sheaf on \(S_\nu\cap O_\lambda\), occurring in degree \(b\), contributes only in total degrees
\[
i\le 2\dim(S_\nu\cap O_\lambda)+b
 \le\langle\rho,2\lambda+2\nu\rangle-d_\lambda=h_\nu.
\]
Use its finite ordinary cohomology tower and then the finite orbit filtration. This proves
\[
H_c^i(S_\nu\cap Y,P)=0\quad(i>h_\nu).
\tag{17.1}
\]
For the opposite orbit the dominant-index dimension formula is \(\dim(T_\nu\cap O_\lambda)=\langle\rho,\lambda-\nu\rangle\). Apply the same argument to the perverse dual \(D_YP\). It gives compact cohomology on \(T_\nu\) only in degrees at most \(-h_\nu\). Constructible biduality and the proved dual exchanges identify its dual with
\[
R\Gamma(T_\nu\cap Y,p^{-!}P),
\]
whose cohomology therefore vanishes below \(h_\nu\). The canonical hyperbolic isomorphism (HL) of §§14–16 transfers this lower bound to (17.1). Consequently
\[
H_c^i(S_\nu\cap Y,P)=0\quad(i\ne h_\nu).
\tag{17.2}
\]

**Theorem 17.1.** The functor
\[
F_\nu(P)=H_c^{h_\nu}(S_\nu\cap Y,P)
\]
is finite dimensional and exact on the equivariant perverse heart.

**Proof.** Constructible finiteness gives finite dimension. Apply compact cohomology to the triangle associated to a short exact sequence in the heart. The groups in the two adjacent degrees vanish for all three terms by (17.2), leaving a short exact sequence in degree \(h_\nu\). A larger support stage gives the same functor: the complex is extension by zero from its closed support, and closed base change and composition identify the compact cohomology maps. Thus the definition is independent of the chosen stage. \(\square\)

## 18. The canonical decomposition of global cohomology

Fix one component class \(\kappa\). For all its orbit indices, \(h_\nu\) has the same parity: their differences are coroot sums, and \(\langle2\rho,\alpha_i^\vee\rangle=2\). There are only finitely many indices on \(Y\).

Put
\[
Y_{\le h}=\bigcup_{h_\eta\le h}(S_\eta\cap Y),\qquad
U_{\ge h}=Y\setminus Y_{<h},\qquad
Y_h=\bigcup_{h_\eta=h}(S_\eta\cap Y).
\]
The first union is closed: it is the finite union of the semi-infinite closure supports with indices of height at most \(h\). Formula (1.1) shows that taking any such closure only adds lower heights. Hence \(U_{\ge h}\) is open and \(Y_h\) is closed in it. Each individual slice is open and closed in \(Y_h\), because its closure adds no other index of equal height. Thus
\[
H_c^h(Y_h,P)=\bigoplus_{h_\nu=h}F_\nu(P).
\tag{18.1}
\]

A finite closed-open induction using (17.2) says that a union of height strata has compact cohomology only in their heights. In particular \(U_{>h}\) has no cohomology in degrees \(h\) or \(h+1\): its heights in this component are at least \(h+2\). The localization triangle for \(U_{>h}\subset U_{\ge h}\) therefore makes the restriction
\[
H_c^h(U_{\ge h},P)\longrightarrow H_c^h(Y_h,P)
\tag{18.2}
\]
an isomorphism. Likewise \(Y_{<h}\) has no cohomology in degrees \(h-1\) or \(h\). The localization triangle for \(U_{\ge h}\subset Y\) makes extension by zero
\[
H_c^h(U_{\ge h},P)\longrightarrow H^h(Y,P)
\tag{18.3}
\]
an isomorphism; \(Y\) is proper, so compact and ordinary cohomology coincide.

Compose the inverse of (18.2) with (18.3), and use (18.1). These are canonical natural maps. Repeating over all heights and the finitely many open-and-closed component classes gives
\[
H^*(\operatorname{Gr}_G,P)
 =\bigoplus_{\nu\in X_*(T)}F_\nu(P),
\quad F_\nu(P)\text{ lies in degree }\langle2\rho,\nu\rangle.
\tag{18.4}
\]
Only finitely many summands are nonzero. This constructs the splitting itself; degeneration and an equality of dimensions would not supply these maps. The closed-support comparisons used in Theorem 17.1 commute with the two localization triangles, so the splitting is also independent of stage. Exactness of all \(F_\nu\) proves that total cohomology is exact on this perverse heart.

## 19. Rank-two slices and their weights

Let \(G=GL_2\), \(\lambda=(a,b)\), \(a\ge b\), and \(r=a-b\). In the determinant component \(a+b\), put \(\nu_i=(a-i,b+i)\). A point of \(S_{\nu_i}\) has a representative
\[
\begin{pmatrix}1&f\\0&1\end{pmatrix}t^{\nu_i},
\qquad f\in F/t^{r-2i}O.
\]
The equality of representatives follows by conjugating their difference into \(GL_2(O)\): the upper parameter is integral exactly when \(f-f'\in t^{r-2i}O\).

The determinant and Smith-factor proof of Lesson4 says that the closed Schubert variety is exactly the reduced locus of lattices
\(t^aO^2\subset\Lambda\subset t^bO^2\) with determinant valuation \(a+b\). The displayed two generators impose
\[
0\le i\le r,\qquad v(f)\ge-i.
\]
For example, containing \(t^ae_2\) requires subtracting \(ft^ae_1\); its first-generator coefficient is \(ft^i\), giving precisely the same bound. Hence
\[
S_{\nu_i}\cap\overline{\operatorname{Gr}^{\lambda}}
 =t^{-i}O/t^{r-2i}O\simeq\mathbb A^{r-i},
\quad0\le i\le r.
\tag{19.1}
\]
The coefficients of powers \(-i,-i+1,\ldots,r-2i-1\) are affine coordinates. These are the only nonempty slices, since all other torus indices fail the lattice bounds. Their dimensions equal \(\langle\rho,\lambda+\nu_i\rangle=r-i\).

For \(0<i<r\), the open orbit condition is that the coefficient of \(t^{-i}\) be nonzero, so its slice is \(\mathbb G_m\times\mathbb A^{r-i-1}\). The two extreme slices are \(\mathbb A^r\) and a point. This follows by checking which generator entry has valuation exactly \(b\), rather than using a dual representation's weights.

For \(\lambda=(1,0)\), the Schubert variety is \(\mathbb P^1\) by the line description in Lesson4. Its two slices are \(\mathbb A^1\) at \((1,0)\) and a point at \((0,1)\). With \(IC_\lambda=\Lambda[1]\), their compact cohomology contributes one copy of \(\Lambda\) in degrees1 and−1 respectively. Complex orientation identifies \(H_c^2(\mathbb A^1,\Lambda)=\Lambda\), and all other compact cohomology vanishes: one-point compactification is the oriented sphere \(S^2\), whose two-cell cochain calculation gives this assertion. Thus (18.4) recovers \(H^*(\mathbb P^1,\Lambda[1])\) with the stated shifts.

For \(\lambda=(2,0)\), the three closed slices are \(\mathbb A^2,\mathbb A^1,\mathrm{pt}\), with indices \((2,0),(1,1),(0,2)\) and cohomological weights2,0,−2. Lesson4's rank-two chart identifies the only singularity with \(xz=y^2\). We verify its intersection complex for our characteristic-zero coefficients. The map
\((s,t)\mapsto(s^2,st,t^2)\) identifies the cone with \(\mathbb C^2/\{\pm1\}\): its invariant monomials are generated by those three degree-two monomials, with the single displayed relation, and away from zero its fibers are the two sign translates. A radial link is homeomorphic to \(S^3/\{\pm1\}=\mathbb{RP}^3\), by normalizing the image of each unit vector. This is a continuous bijection between compact Hausdorff spaces. The cellular cochain complex of \(\mathbb{RP}^3\) has one cell in each degree0–3, with alternating boundary maps0,2,0. Since2 is invertible in \(\Lambda\), its cohomology is \(\Lambda\) in degrees0 and3 only.

For completeness, the cell boundary follows from the hemisphere model of \(\mathbb{RP}^n\): its one \(n\)-cell attaches by identifying antipodal points of the boundary sphere. Above a generic point of the preceding cell there are two sheets. Their local orientation signs sum to \(1+(-1)^n\), because the antipodal map on \(S^{n-1}\) reverses each of its \(n\) ambient coordinates and has degree \((-1)^n\). Thus the boundaries in dimensions1,2,3 are respectively0,2,0, proving the asserted cochain calculation.

The punctured cone therefore has the same local cohomology as that link. For its smooth open inclusion \(j\), the stalk of \(Rj_*\Lambda[2]\) at the vertex has degrees−2 and1. The middle-extension truncation from the earlier IC lesson removes degree1 and retains degree−2. The natural constant-sheaf map is an isomorphism on this truncation and on the smooth locus. The vertex costalk of \(\Lambda[2]\) has its only cohomology in degree2, from the relative cone/link sequence. These strict stalk and costalk bounds exclude a point-supported quotient or subobject. Consequently \(IC_{(2,0)}=\Lambda[2]\). Its three weight functors are each \(\Lambda\), in degrees2,0,−2, as computed directly from (19.1).

![Three rank-two slices and their cohomological weights](assets/mv-gl2-slices.svg)

*For the Schubert surface of \(GL_2\) with index \((2,0)\), the closed semi-infinite slices have complex dimensions2,1,0. The normalization \(IC=\Lambda[2]\) puts their top compact cohomology in degrees2,0,−2. Formula (19.1) gives their coordinates; the cone/link calculation gives the IC normalization.*

Translating by the central coweight \((-1,-1)\) gives the \(SL_2\) surface indexed by \(\alpha^\vee=(1,-1)\). Its slice indices are \(\alpha^\vee,0,-\alpha^\vee\), with the same dimensions and degrees. The coefficient restriction matters: the link calculation uses invertibility of2 and is not a characteristic-two coefficient calculation.

## 20. MV cycles and top compact cohomology

An **MV cycle of indices \((\lambda,\nu)\)** is the reduced closure of an irreducible component of \(S_\nu\cap\operatorname{Gr}^{\lambda}\). The dimension theorem proves that all these components have dimension \(d=\langle\rho,\lambda+\nu\rangle\). Their closures are the top-dimensional components of the closed-Schubert slice, by §10.

For any pure \(d\)-dimensional complex algebraic variety \(Z\),
\[
H_c^{2d}(Z,\Lambda)=\bigoplus_{C\in\operatorname{Irr}(Z)}\Lambda[C].
\tag{20.1}
\]
Here \([C]\) means the orientation generator on a smooth dense open of \(C\), extended in top compact cohomology. Choose disjoint smooth dense opens of the finitely many components, removing their intersections and singular loci. Their complement has dimension at most \(d-1\), so both its degrees2d−1 and2d vanish by the compact-support bound in §17. Localization identifies top compact cohomology with that of the smooth opens. Each such open is analytically connected by Connectedness and full faithfulness, Theorem 2.1. Complex coordinate changes preserve real orientation. Poincaré duality, Theorem 1.1 and Corollary 2.5, identifies the top compact cohomology of each connected oriented smooth open with \(\Lambda\), compatibly with restriction to smaller opens. This proves (20.1) and its canonical generators.

Thus the MV cycles give a canonical basis of the **top compact cohomology of the open slice with constant coefficients**. The minuscule and rank-two examples in §19 also identify that space with the corresponding \(F_\nu(IC_\lambda)\).

For the open inclusion \(j:O_\lambda\hookrightarrow Z_\lambda\), put \(\Delta_\lambda={}^pH^0j_!\Lambda[d_\lambda]\), the standard object. The adjunction proved in Gluing t-structures, Theorem 2.1, makes \(j_!\) right t-exact: it is left adjoint to the t-exact restriction. Hence \(A=j_!\Lambda[d_\lambda]\) belongs to \({}^pD^{\le0}\). With \(K={}^p\tau_{\le-1}A\), its truncation triangle is \(K\to A\to\Delta_\lambda\to K[1]\). On a boundary orbit \(i_\mu\), we have \(i_\mu^*A=0\), so
\[
i_\mu^*\Delta_\lambda\simeq i_\mu^*K[1]
\in D^{\le-d_\mu-2}.
\tag{20.2}
\]
Indeed the ordinary support characterization for \(K\in{}^pD^{\le-1}\), together with lissity of its cohomology on the orbit, gives upper ordinary degree \(-d_\mu-1\); the shift by1 lowers it by one more.

Combine this with the slice dimensions as in §17. On the boundary of \(S_\nu\cap Z_\lambda\), compact cohomology of \(\Delta_\lambda\) occurs only in degrees at most \(h_\nu-2\). Both degrees \(h_\nu-1\) and \(h_\nu\) vanish, so localization identifies the open-slice group with \(F_\nu(\Delta_\lambda)\). Its open restriction is \(\Lambda[d_\lambda]\), and \(h_\nu+d_\lambda=2d\). Thus we have proved the general standard-object cycle basis
\[
F_\nu(\Delta_\lambda)
 =H_c^{2d}(S_\nu\cap O_\lambda,\Lambda)
 =\bigoplus_C\Lambda[C].
\tag{20.3}
\]
This two-degree boundary margin eliminates the connecting map without an IC parity assumption.

The corresponding IC basis is obtained after the convolution and group-reconstruction arguments: Identifying the dual group, §8.5 proves full classical semisimplicity, then \(\Delta_\lambda=IC_\lambda\), and transfers (20.3) to the IC weight space. That later result is not an input to the concentration or canonical cohomology decomposition proved here. In particular one must not replace the two-degree standard-object margin above by an unproved deletion of the IC boundary.

The general identification
\[
F_\nu(IC_\lambda)\stackrel{?}{\simeq}
H_c^{2d}(S_\nu\cap\operatorname{Gr}^{\lambda},\Lambda)
\tag{20.4}
\]
has not been proved in this lesson and is not used as an input. Strict IC boundary stalk bounds alone give degree at most \(h_\nu-1\) on the boundary; they do not eliminate the connecting map from that degree into the top open-slice cohomology. A complete proof must supply the additional argument, rather than treating a cycle citation as an identification. Formula (20.1), the standard-object basis(20.3), the general dimension theorem, and the explicitly computed examples do not have that gap. The canonical surjection \(\Delta_\lambda\twoheadrightarrow IC_\lambda\) gives, by exactness, a quotient of the cycle space; identifying it with the entire space requires proving that the kernel has zero weight functors.

## 21. Coefficient scope

The geometry of §§1–10 and(19.1) is proved over every algebraically closed field. The classical hyperbolic and weight-functor theorems in §§12–18 are proved over \(\mathbb C\) with the classical operations specified in §11.

For an algebraically closed field \(k\), \(\ell\ne\operatorname{char}k\), and rational \(\ell\)-adic coefficients, the analogous hyperbolic map has the same geometric diagram. Its proof additionally requires a complete constructible rational-adic six-operation theory, including nonproper direct and proper-support images, exceptional inverse image, compatible units and counits, and the exchanges used in §§14–16. The current earlier lesson The pro-étale site and l-adic complexes proves derived-completion and proper-base-change results but explicitly leaves that full theory open. Reduction modulo \(\ell^r\) and a limiting assertion do not prove those nonproper comparisons. The rational-adic versions of(17.2) and(18.4) therefore remain unproved here. They are not asserted as consequences of the classical proof. No future lesson or external theorem is used to discharge this obligation.

## 22. Exercises with solutions

**Exercise 1 (easy).** For \(GL_2\), \(\lambda=(3,0)\), give every nonempty closed slice, its Laurent coordinates, its dimension, and its weight degree.

**Solution.** Formula (19.1) gives indices \((3,0),(2,1),(1,2),(0,3)\). The coordinates are respectively powers0,1,2; powers−1,0; power−2; and no powers. Thus the slices are \(\mathbb A^3,\mathbb A^2,\mathbb A^1,\mathrm{pt}\), with dimensions3,2,1,0. Since \(2\rho=(1,-1)\), their degrees are3,1,−1,−3. For the two intermediate indices the open-orbit slices require the first listed coefficient to be nonzero; the extreme slices already lie in the open orbit. These calculations concern geometry and do not assume a formula for the general intersection complex.

**Exercise 2 (easy).** Compute the two weight functors and shifted cohomology for \(IC_{(1,0)}\) of \(GL_2\).

**Solution.** The closed variety is \(\mathbb P^1\), with \(IC=\Lambda[1]\). The attracting slices are \(\mathbb A^1\) and a point. The first has compact cohomology \(\Lambda\) in degree2; after the shift it contributes \(F_{(1,0)}=\Lambda\) in degree1. The point after the shift contributes \(F_{(0,1)}=\Lambda\) in degree−1. The sphere cell calculation gives \(H^0(\mathbb P^1,\Lambda)=H^2(\mathbb P^1,\Lambda)=\Lambda\), so its shifted cohomology has exactly those two degrees. The maps in §18 identify these copies canonically.

**Exercise 3 (medium).** Compute all weight functors for the \(SL_2\) Schubert surface of index \(\alpha^\vee\), and explain the coefficient restriction in the cone proof.

**Solution.** Its three slices are \(\mathbb A^2,\mathbb A^1,\mathrm{pt}\) at \(\alpha^\vee,0,-\alpha^\vee\). Section19 proves \(IC=\Lambda[2]\). The one-point compactifications of \(\mathbb C^2\) and \(\mathbb C\) are oriented spheres \(S^4\) and \(S^2\), so their only compact cohomology is \(\Lambda\) in degrees4 and2. After shifting by2, these give \(\Lambda\) in degrees2 and0; the point gives \(\Lambda\) in degree−2. The link is \(\mathbb{RP}^3\). Its boundary map2 is invertible over characteristic-zero \(\Lambda\), but vanishes over \(\mathbb F_2\), producing additional local cohomology. Therefore this proof cannot claim the same constant intersection complex with characteristic-two coefficients.

**Exercise 4 (medium).** Explain why dimensions and perversity give only one half of weight concentration. Supply the other half and deduce exactness.

**Solution.** On \(O_\lambda\), perversity and equivariant lissity give ordinary degree \(b\le-d_\lambda\). The slice dimension gives compact degree at most \(2\rho(\lambda+\nu)\). Adding yields total degree at most \(h_\nu\), which proves only upper vanishing. Apply this estimate to the perverse dual on the opposite slice; its bound is \(-h_\nu\). Point duality converts it to lower vanishing below \(h_\nu\) for \(R\Gamma(T_\nu,p^{-!}P)\). The proved canonical hyperbolic map identifies this complex with compact cohomology of \(S_\nu\), giving both vanishings. A short exact sequence in the heart gives a triangle; the compact cohomology groups in the adjacent degrees vanish, so its degree-\(h_\nu\) sequence is short exact.

**Exercise 5 (hard).** Construct the direct-sum cohomology isomorphism, including its maps. Explain why an arbitrary splitting of a filtration is unnecessary.

**Solution.** In one component all heights have the same parity. The finite union \(Y_{\le h}\) is closed by the semi-infinite closure theorem, and \(U_{\ge h}\) is its complementary upper open. The open \(U_{>h}\) has no compact cohomology in degrees \(h,h+1\); localization therefore makes restriction from \(U_{\ge h}\) to \(Y_h\) an isomorphism in degree \(h\). The closed lower union \(Y_{<h}\) has no degrees \(h-1,h\), so extension by zero from \(U_{\ge h}\) to proper \(Y\) is also an isomorphism in that degree. Invert the first and compose with the second. The height stratum is the disjoint open-and-closed union of the slices of height \(h\), so its compact cohomology is their direct sum. Repeat in every height and component. Every arrow was a restriction or extension map in a localization triangle, so the resulting isomorphism is natural and canonical, with no choice of filtration splitting.

## Appendix A. Finite covers and the geometry of cohomological comparison

The algebraic inputs needed for comparison in positive characteristic include extension of tame covers, finite arithmetic normalizations and suitable smooth neighborhoods. We prove those inputs here before applying them to the rational-adic arguments of this course.

### A.1. Three geometric assertions and their proof order

The precise assertions are the following.

1. For a normal integral Noetherian base \(S\), a smooth relative curve \(X\to S\) with nonempty geometrically connected fibres and a section has the following extension property: a generic finite étale \(G\)-torsor whose order is invertible on \(S\), and whose generic section fibre is split, extends uniquely to a finite étale \(G\)-torsor over \(X\). This is Corollary A.13.2.
2. The normalization of a finite-type domain over \(\mathbb Z\) in any finite extension of its fraction field is finite. This is Theorem A.14.2, including imperfect residue fields.
3. Every point of a smooth map has an affine étale neighborhood \(U\to X\) factoring through an affine étale \(V\to S\), with \(U\to V\) affine smooth, a section and nonempty geometrically connected fibres. This is Theorem A.15.5, over arbitrary bases.

Sections A.2–A.5 supply the trace lattice, puncture and formal comparison. Section A.7 proves dense-fibre purity using those comparisons. Section A.8 reduces the curve extension to a trait, and Sections A.9–A.13 prove that trait step by a surface normal form and the valuation of the section. Sections A.14–A.15 provide the arithmetic models and smooth neighborhoods. The coefficient scope in §21 is unchanged: these geometric results supply inputs to cohomological comparison, rather than asserting the rational-adic weight theorem on their own.

## A.2. Finite separable normalization and its actual lattice

### A.2.1. Integral elements form a ring

Let R be a commutative ring and let z₁,…,zₛ belong to a commutative R-algebra, each satisfying a monic polynomial over R. The algebra R[z₁,…,zₛ] is a finite R-module: powers at least the corresponding polynomial degree are reduced to lower powers, so finitely many bounded monomials generate it.

Every element t of this algebra is integral. Choose module generators including1. Multiplication by t is represented on these generators by a matrix M over R (relations among the generators cause no difficulty). The adjugate identity for T−M shows that its monic determinant polynomial annihilates multiplication by t on all generators. Applied to1, it gives a monic equation for t. The adjugate identity follows by the cofactor expansion, so this argument needs neither freeness of the finite module nor an unproved characteristic-polynomial theorem. In particular sums and products of integral elements are integral.

### A.2.2. Nondegeneracy of separable trace

Let K be a field and let L be a finite product of finite separable field extensions of K. After extension to a separable closure Kˢ, its algebra becomes a finite product of copies of Kˢ. To see this explicitly, generate each field by a finite tower of separable elements; at each step its separable minimal polynomial factors into distinct linear factors, and the Chinese remainder maps split that step into the corresponding factors. Iterating gives the product, with the number of factors equal to dim_K L.

The trace of multiplication in a product algebra is the sum of its coordinates. Its bilinear trace pairing is therefore the ordinary diagonal pairing after extension to Kˢ, which is nondegenerate. A linear map of finite K-vector spaces has the same matrix rank after a field extension, by its nonzero minors. Hence

\[
L\longrightarrow\operatorname{Hom}_K(L,K),\qquad z\longmapsto(w\longmapsto\operatorname{Tr}_{L/K}(zw)).
\]

is an isomorphism. This is valid even when char(K) divides dim_K L. No division by that dimension or averaging by a group order occurs.

### A.2.3. Normalization is finite in this separable situation

**Lemma A.2.3.** Let R be a Noetherian integrally closed domain, K=Frac(R), and L a finite separable K-algebra as in §A.2.2. Its integral closure N of R in L is a finite R-algebra. Integral closure commutes with localization at a nonzero element of R.

**Proof.** First choose a K-basis α₁,…,αᵣ consisting of integral elements. Start with any basis. An element z algebraic over K satisfies a monic equation

\[
z^d+c_1z^{d-1}+\cdots+c_d=0.
\]

Choose a nonzero a∈R with all a c_i∈R. Then az satisfies a monic equation with coefficients aⁱc_i∈R. Scaling each basis element separately preserves linear independence and makes it integral. The same construction works for a product of fields by taking a product of the equations of its coordinates.

Let β₁,…,βᵣ be the trace-dual basis, supplied by §A.2.2. For z∈N, every zα_i is integral by §A.2.1. Its trace is integral over R: the trace is the sum of its images under the embeddings in the separable closure, and these images satisfy the same monic equation. The sum is integral by §A.2.1. That trace belongs to K, hence belongs to R by integral closedness. Therefore

\[
z=\sum_i\operatorname{Tr}(z\alpha_i)\beta_i\in\bigoplus_iR\beta_i.
\]

N is an R-submodule of this finite free module, so it is finitely generated because R is Noetherian. Its unit and products already belong to N by §A.2.1, giving the finite algebra.

For localization, an element integral over R_a satisfies an equation with coefficients c_i/a^{t_i}, with c_i∈R. Choose n with ni≥t_i for every coefficient. Multiplying the element by aⁿ gives a monic equation with coefficients c_i a^{ni−t_i}∈R. Thus the element belongs to N_a. The reverse inclusion follows by localizing a monic equation. This proves the localization assertion. □

This proves the finite normalization needed for a generically separable cover over an already normal Noetherian affine chart. It does not prove finiteness of a purely inseparable normalization over an arbitrary base, or normality of a smooth chart or a power-series ring.

### A.2.4. A common denominator for every power

**Lemma A.2.4.** For a Noetherian domain R and u∈Frac(R), integrality is equivalent to the existence of c≠0 in R with cuⁿ∈R for every n≥0.

**Proof.** A monic equation makes R[u] a finite module spanned by finitely many powers. Clearing those powers' denominators gives c. Conversely R[u]⊂c⁻¹R is a submodule of a finite free module, hence finite; multiplication by u and the determinant argument in §A.2.1 give a monic equation. □

For completeness, submodules of Rʳ are finite when R is Noetherian: project to one coordinate, choose lifts of generators of the resulting ideal, and apply induction on r to the kernel. This is the module finiteness used here and in Lemma A.2.3. Free human-source comparison: [Stacks, Lemma 10.37.4](https://stacks.math.columbia.edu/tag/00GX); the complete argument required here is above.

## A.3. A finite étale algebra over a normal domain is that normalization

Use the algebraic finite-étale description: a finite locally free algebra C whose geometric fibres are finite products of finite separable fields. Let R be a normal Noetherian domain. The trace pairing of C is perfect. Indeed, in a local free basis its determinant is nonzero in every residue field by §A.2.2 applied to that fibre, and is therefore a unit. These local trace isomorphisms agree, since they come from the same multiplication trace.

C injects into its generic algebra C_K, because it is locally free over the domain. It consists of integral elements, by the multiplication-matrix argument of §A.2.1. Conversely, if z∈C_K is integral over R, then Tr(zc)∈R for every c∈C, by the same integral trace argument used in §A.2.3. The perfect trace pairing supplies c₀∈C giving this functional. Over K, nondegeneracy then gives z=c₀. Consequently C is exactly the integral closure of R in C_K.

This argument also proves the asserted equality on every localization, using §A.2.3. It avoids assuming that normality is automatically preserved by an étale map as an unstated premise.

## A.4. Splitting a cover over a punctured formal base

### A.4.1. Functions across the puncture

Let (A,m) be a Noetherian local domain with a regular sequence a,b∈m. Thus a is a nonzerodivisor and b is a nonzerodivisor on A/aA. Put U=Spec(A)−{m}. Then Γ(U,O)=A.

First, b is a nonzerodivisor on every A/aⁿA. If bc∈aⁿA, reduction modulo a gives c=a c₁. Cancellation of a reduces the claim to exponent n−1; induction gives c∈aⁿA. Powers of b are likewise injective. Hence, inside Frac(A),

\[
A_a\cap A_b=A.
\]

if f/aⁿ=g/bʳ, then bʳf∈aⁿA, so f∈aⁿA. A section over U restricts to elements in A_a and A_b with equal generic values, and is therefore the restriction of an element of A. Agreement on the dense principal open D(a) implies agreement on all U: on each nonempty affine open both regular functions inject into the fraction field. This proves the assertion, including uniqueness.

### A.4.2. Lifting an ordered split algebra through nilpotents

If J is a nilpotent ideal in a commutative ring R, every idempotent of R/J lifts uniquely to R. For a square-zero ideal and a lift u, the element 2u−1 is a unit, since its square is1 modulo J. Replacing u by

\[
u-(u^2-u)(2u-1)^{-1}
\]

gives an idempotent; direct expansion shows the error is zero when J²=0. Successive powers of J give existence for any nilpotent J. For uniqueness, if e and f are idempotents with the same reduction, e(1−f) and f(1−e) are idempotents in J. A nilpotent idempotent is zero, so e=ef=f.

Ordered orthogonal idempotents lifting an ordered decomposition remain orthogonal: their pairwise products are idempotents reducing to zero. Their sum is the unique lift of1, so is1. In a finite locally free algebra, the factors therefore lift the factor ranks. A rank-one unital algebra is the base ring itself. Locally choose a module basis v, write1=c v and v²=d v; the unit law gives cd=1, so the unit is a basis and the unit map is an algebra isomorphism. Thus an ordered split finite étale algebra over a nilpotent quotient lifts uniquely as an ordered split algebra.

The construction is unique, hence its local lifts glue without an additional descent assumption.

### A.4.3. The formal split-cover lemma

**Lemma A.4.3.** Let A be as in §A.4.1, let B=A[[x₁,…,x_d]] with d≥1, and assume explicitly that B is a Noetherian integrally closed domain. Put I=(x₁,…,x_d), V=Spec(B)×_{Spec(A)}U. Let C be a finite étale algebra sheaf on V. If its zero-section restriction has a specified ordered splitting O_Uʳ, then C≅O_Vʳ, extending that splitting.

**Proof.** V is a nonempty open in an integral scheme, so is connected. The finite locally free rank of C is the same r everywhere. Let K=Frac(B) and let L be its generic algebra. Lemma A.2.3 gives the finite integral closure N of B in L. Section A.3 shows that N restricts to C on V: check on each principal affine chart of V, where that section identifies the finite étale algebra with the same integral closure; localization in Lemma A.2.3 identifies its source.

For n≥1 let V_n=V×_{Spec(B)}Spec(B/Iⁿ). Its reduction at I is U. Section A.4.2 lifts the prescribed splitting uniquely to

\[
C|_{V_n}=\mathcal O_{V_n}^{\,r}.
\]

The liftings are compatible as n decreases. Since B/Iⁿ is a finite free A-module with basis the monomials of total degree below n, §A.4.1 gives

\[
\Gamma(V_n,\mathcal O)=A[x_1,\ldots,x_d]/I^n=B/I^n.
\]

Explicitly, the affine projection to U identifies its sheaf of functions with that finite direct sum of copies of O_U; sections act coordinate by coordinate. Inverse limit over n is B by the definition of formal power series.

Every element z∈N restricts to C, and then to its ordered components on every V_n. Taking these component sections and their compatible limits defines a B-algebra map

\[
\alpha:N\longrightarrow B^r.
\]

It is an algebra map because each finite-level component map is one, and all equations are preserved by inverse limit. Its multiplication trace satisfies

\[
\operatorname{Tr}_{L/K}(z)=\sum_i\alpha_i(z).\tag{A.4.1}
\]

To verify the equality rather than assume it, the left side belongs to B by §A.2.3. On V it is the trace of the finite locally free algebra C; trace commutes with reduction of a finite free multiplication matrix. On V_n the ordered splitting identifies that trace with the displayed sum modulo Iⁿ. The sections equality above therefore makes the two elements equal in B/Iⁿ for every n. Their difference is zero in B, since a formal power series in every Iⁿ has all coefficients zero.

Extend α to K. If z lies in its kernel, equation(A.4.1) applied to zw gives Tr(zw)=0 for all w∈L. Here N spans L over K, by the integral-basis construction in Lemma A.2.3, so extending (A.4.1) indeed permits every w. Nondegeneracy in §A.2.2 forces z=0. Source and target have the same K-dimension r; hence α_K is an algebra isomorphism.

Finally α carries integral closure to integral closure. The integral closure of the diagonal B in Kʳ is Bʳ: any integral tuple has every coordinate integral over B, hence in B by normality; a tuple of B-elements satisfies the product of their monic linear polynomials. Thus α(N)=Bʳ. Restriction to V proves C=O_Vʳ, with the specified zero-section ordering. □

![The formal restriction maps build alpha; trace nondegeneracy proves it is an isomorphism.](assets/finite-cover-formal-splitting.png)

*Figure 1. The actual algebra maps of Lemma A.4.3. The lower row is the compatible finite-level ordered splitting, not an assumed global splitting. Equation(A.4.1) makes the generic map injective by the nondegenerate separable trace pairing; normality then identifies N with Bʳ. Proof locators: §§A.4.2–4.3. Free human-source comparison: [Stacks, Lemma 58.26.1](https://stacks.math.columbia.edu/tag/0EY9). Reproducible SVG.*

### A.4.4. Trace and the group order

The splitting argument is independent of the numerical group order. Nondegeneracy of the trace pairing concerns a separable algebra; it does not require Tr(1) to be a unit. In contrast, the averaging and invariant projections in §A.11.4 and §A.12 use an explicitly invertible group order.

### A.4.5. Noetherianity of the power-series ring

The Noetherianity hypothesis on B in Lemma A.4.3 follows from that on A, with the following direct proof. First a polynomial ring over a Noetherian ring is Noetherian. For an ideal J⊂A[t], let J_n be the ideal of coefficients of tⁿ in elements of J of degree at most n. Multiplication by t makes J_n⊂J_{n+1}. This chain stabilizes, say at N, and every J_n is finitely generated. Choose polynomial representatives for finite generating lists at n=0,…,N. For a polynomial in J of degree k≥N, use the representatives at N, multiplied by t^{k−N}, to subtract its leading coefficient and reduce its degree. At k<N use the representatives at k. Finite downward induction expresses it in the ideal generated by the finitely many chosen representatives. Repeating one variable at a time proves the multivariable assertion.

For an ideal H⊂A[[x₁,…,x_d]], take the homogeneous initial forms of its nonzero elements in the polynomial ring A[x₁,…,x_d], with the order given by least total degree. The ideal generated by these forms has a finite generating sublist of the actual initial forms: first choose finite generators in the ideal, and then take the finitely many initial forms occurring in their finite expressions. Choose corresponding series h₁,…,h_s∈H, of respective orders e_i.

For h∈H of order k, its homogeneous degree-k initial form is a sum of the initial forms of h_i with homogeneous polynomial coefficients of degrees k−e_i (coefficients for negative degrees are zero). Subtract that sum using the series h_i. The remainder is zero or has strictly greater order. Repeat on the remainder. The coefficients attached to a fixed h_i now have orders tending to infinity, so their sum is a well-defined formal series b_i. In each finite degree only finitely many subtractions occur, hence coefficientwise

\[
h=\sum_i b_ih_i.
\]

Thus H is finitely generated and B is Noetherian. No assertion that H was already closed is needed: the equality itself is established in every coefficient. The integral-closedness hypothesis is supplied next.

### A.4.6. Normality by the actual coefficient bound

**Lemma A.4.6.** If A is a Noetherian normal domain, A[[t₁,…,t_d]] is a Noetherian normal domain.

**Proof.** Noetherianity is §A.4.5; products of nonzero initial homogeneous polynomials give the domain assertion. For one variable set B=A[[t]], F=Frac(A). An integral w≠0 in Frac(B) has B[w] finite, so some nonzero h∈B clears every power wʲ. Inside F((t)), write initial terms w=c tⁿ+… and h=b tᵐ+…. Then hwʲ∈B forces m+jn≥0 and bcʲ∈A for all j≥0. Hence n≥0, and Lemma A.2.4 and normality give c∈A. Subtract c tⁿ; the remainder is integral by §A.2.1. Repeating determines every coefficient in A, proving w∈B; zero already belongs to B. Iteration gives all d: iterated and multivariable formal series are the same coefficient arrays, with finite sums defining each product coefficient. □

The Laurent expansion used here is obtained by factoring a nonzero denominator as tᵏ times a series with nonzero constant term in F, and recursively inverting that series. Thus no completeness of A and no identification between localized and completed series rings is assumed. Free human-source comparison: [Stacks, Lemma 10.37.9](https://stacks.math.columbia.edu/tag/0BI0); the proof used is fully written here.

### A.4.7. The formal splitting statement in the required base scope

**Corollary A.4.7.** Let (A,m) be a normal Noetherian local domain with dim(A)≥2, B=A[[x₁,…,x_d]], d≥1, and V=Spec(B)×_{Spec(A)}(Spec(A)−{m}). Every finite étale cover of V with a specified ordered split zero-section restriction is split on V, with that ordering.

**Proof.** The earlier programme proof Discrete valuation rings, normal rings and Serre's criterion, Proposition 3.4 constructs a regular pair in A: choose nonzero a∈m; the associated primes of A/aA are height one by its Theorem 3.2, so finite prime avoidance chooses b∈m outside them. Multiplication by b on A/aA is injective. The needed regular sequence is therefore present. Lemma A.4.6 supplies normal Noetherian B. All hypotheses of Lemma A.4.3 hold, giving the assertion. □

### A.4.8. A single ordered factor also lifts

The same mechanism lifts a specified rank-one factor, without requiring the whole zero-section cover to be split. Suppose C|U=O_U×D with specified projection to O_U. Section A.4.2 uniquely lifts its idempotent on every V_n; the lifted rank-one factor is O_{V_n}. Component sections of N therefore give a B-algebra map α:N→B extending that projection.

After passage to K=Frac(B), α_K maps the finite product of separable fields L to K. The orthogonal coordinate idempotents map to orthogonal idempotents summing to1 in a field, so exactly one goes to1. Its field factor maps injectively to K as a K-algebra and therefore is K itself. N is the product of the integral closures in these field factors: their idempotents are integral, and each tuple of integral elements is integral by §A.2.1. The selected factor of N is thus B, by normality. Projection to it restricts on V to the required rank-one factor and retains the original zero-section projection. Its finite-level restrictions agree by the uniqueness in §A.4.2.

This proves existence of the lifted section in algebraic factor form. It makes no assertion that an arbitrary morphism functor has already been represented or that all cover comparisons have been completed.

## A.5. An elementary finite-module freeness step

**Lemma A.5.1.** Let (R,m) be Noetherian local, x∈m, and M a finite R-module. If x acts injectively on M and M/xM is finite free over R/xR, then M is free over R, of that same rank.

**Proof.** Lift a basis and form φ:Rʳ→M. Its finite cokernel Q satisfies Q=xQ, so Q=0. The needed local Nakayama argument is explicit: if generators q_i satisfy q_i=xΣ_j a_ij q_j, multiply by the adjugate of1−x(a_ij). Its determinant is1 modulo m, so is a unit and every q_i is zero.

The kernel K of φ is finite, since R is Noetherian. A vector k∈K has zero reduction because the reduced basis map is an isomorphism, so k=xv for v∈Rʳ. Then xφ(v)=0, whence φ(v)=0 by injectivity of x on M. Thus K=xK, and the same local Nakayama argument gives K=0. Therefore φ is an isomorphism. □

This supplies the algebraic lifting step when a finite cover's extended module is known to have the required regular-sequence depth. That depth and the étaleness of the resulting algebra still require their own proofs; finite module freeness is not being used to skip them.

### A.5.2. Explicit module Hartogs and flat passage

**Lemma A.5.2.** Let (R,m) be Noetherian local, M finite, and a,b∈m an M-regular pair. For any open W⊂Spec(R) containing D(a)∪D(b), the map M→Γ(W,M~) is an isomorphism.

**Proof.** First b acts injectively on M itself. If bz=0, regularity modulo a gives z=a z₁. Cancel a to obtain bz₁=0 and repeat; z∈∩_n aⁿM=0. The last equality is the proved Krull intersection theorem, Noetherian and Artinian rings, Theorem 6.1, for the finite module M and (a)⊂m.

Regularity of b on M/aⁿM follows by induction exactly as in §A.4.1, canceling a at each step. Injections by a and b permit the localizations M_a and M_b to be viewed inside M_ab. If z/aⁿ=z'/bʳ, cross multiplication gives bʳz=aⁿz'. The just-proved injectivity modulo aⁿ forces z=aⁿz₀, so the common fraction belongs to M. Consequently

\[
M_a\cap M_b=M\quad\text{inside }M_{ab}.
\]

The two restrictions of a section on W therefore come from one z₀∈M. On any principal affine D(s)⊂W its difference from z₀ vanishes in M_as. Multiplication by a remains injective on M_s, so M_s→M_as is injective, and the difference is zero there. Principal opens cover W, proving both existence and uniqueness. □

If R→S is flat, tensoring the two defining injective sequences preserves regularity of a,b on M⊗_R S. When S is Noetherian local and their images remain in its maximal ideal, Lemma A.5.2 applies over S. Thus, for a finite algebra extended with this module depth, a split restriction on the indicated punctured open identifies the whole algebra with the split algebra: its multiplication and unit are determined on that open as well. This supplies the uniqueness step needed to compare an extended algebra after the formal flat passage. It does not presume that normalization commutes with completion.

### A.5.3. Generating bundles on an open affine subscheme

Let W be a quasi-compact open of Spec(R), and E a finite locally free sheaf on W. On a finite principal-open cover, sections of E are the equalizer of sections on the cover and its pairwise intersections. These intersections are affine principal opens. Localizing this finite equalizer at s commutes with it, because localization is exact; affine quasi-coherent module sections localize. Hence

\[
\Gamma(W,E)_s=\Gamma(W\cap D(s),E).
\]

Choose a finite principal cover D(s_j)⊂W on which E is free. Each local basis is represented after this localization by a global section divided by a power of s_j. Its global numerator is a basis up to units on D(s_j). The finitely many resulting global sections generate E everywhere. They give a surjection O_Wʳ→E, split locally. Apply the same argument to E\*: dualizing its split surjection gives an embedding E→O_Wˢ with locally free cokernel. These assertions require no normality of R.

### A.5.4. The formal comparison for finite bundles over a depth-two base

Let (A,m) be any Noetherian local ring with a regular pair a,b∈m, not necessarily reduced or normal. Set B=A[[x₁,…,x_d]], I=(x₁,…,x_d), U=Spec(A)−{m}, V=Spec(B)×_A U, and V_n=V×_B Spec(B/Iⁿ). The ring B is Noetherian by §A.4.5 and is local: a series is a unit exactly when its constant coefficient is a unit in A, as recursive inversion shows. Coefficientwise injection shows that a,b are a B-regular pair. Lemma A.5.2 with M=A and M=B therefore gives

\[
\Gamma(U,\mathcal O)=A,\qquad\Gamma(V,\mathcal O)=B,\qquad\Gamma(V_n,\mathcal O)=B/I^n.
\]

The third equality uses the finite monomial basis over A exactly as in §A.4.3.

For a bundle E on V, §A.5.3 first embeds E→O_Vʳ with locally free cokernel Q, and then embeds Q→O_Vˢ. Thus

\[
0\longrightarrow E\longrightarrow\mathcal O_V^{\,r}\longrightarrow\mathcal O_V^{\,s}
\]

is exact at its first two terms and remains so under any base change: both constituent short sequences split locally. Taking sections and inverse limits identifies both Γ(V,E) and lim_n Γ(V_n,E|V_n) with the kernel of the same matrix Bʳ→Bˢ. Inverse limit is left exact, directly from its compatible-coordinate definition. Applying this result to Hom(E,F)=E\*⊗F proves that compatible formal morphisms of finite bundles are exactly the actual morphisms on V. Their compositions agree by restriction and uniqueness.

![The universally exact presentation computes both actual and completed bundle sections by the same matrix kernel.](assets/finite-cover-formal-matrices.png)

*Figure 2. Section A.5.4 uses the actual locally split presentation, so restriction to V_n retains its kernel. Each lower kernel is computed over B/Iⁿ, and their inverse limit is the upper kernel over B. Applying this to E\*⊗F gives full faithfulness, including compatibility with compositions. Free human-source comparison: [Stacks, Lemma 52.15.1](https://stacks.math.columbia.edu/tag/0EKP), quasi-affine case; the global generators and matrix-kernel proof required here are written in §§A.5.3–5.4. Reproducible SVG.*

### A.5.5. Trace idempotents over an arbitrary finite-étale base

For a finite locally free algebra C with finite separable geometric fibres, its trace pairing is perfect over every base ring: in a local free basis its determinant is a unit at every maximal ideal by §A.2.2. Let e=Σ_i c_i⊗c_i∨ in C⊗C for trace-dual bases. This tensor is basis-independent because it represents the identity under

\[
C\otimes C\longrightarrow\operatorname{End}(C),\qquad u\otimes v\longmapsto(z\longmapsto u\operatorname{Tr}(vz)).
\]

Commutativity of multiplication and trace gives (c⊗1)e=(1⊗c)e for every c. Also μ(e)=1: for every z,

\[
\operatorname{Tr}(\mu(e)z)=\sum_i\operatorname{Tr}(c_i^\vee zc_i)=\operatorname{Tr}(m_z)=\operatorname{Tr}(z),
\]

where the middle sum is the diagonal sum of the multiplication matrix in the c_i basis. Perfectness of the pairing gives the equality. These two identities imply e²=e by multiplying e by its displayed expansion. All identities are tensor identities over the base, not equalities tested only on residue fields; nilpotents in the base cause no problem.

For an algebra map ψ:C→R, set f=(id⊗ψ)(e). Then cf=ψ(c)f and ψ(f)=1, so f²=f and fC=Rf. Hence C=Rf×(1−f)C, and ψ is its rank-one projection. This proves the algebraic split-factor description of a section over any base.

### A.5.6. Lifting algebra maps across a nilpotent ideal

Let J⊂R be nilpotent, and C,D finite étale R-algebras. An algebra map C/JC→D/JD gives a rank-one projection of the finite étale D/JD-algebra (C/JC)⊗(D/JD) to D/JD. Section A.5.5 supplies its idempotent. Section A.4.2 lifts it uniquely to C⊗_R D; its finite locally free factor has rank one because nilpotent reduction has the same prime points. That factor is D by the rank-one unit argument of §A.4.2. Its projection gives a unique D-algebra map C⊗D→D, hence an R-algebra map C→D, lifting the given one. Conversely any lift has exactly this idempotent, by §A.5.5 and uniqueness of the idempotent lifting, so is the same map.

The construction is unique on overlaps and hence glues for algebra sheaves on nilpotent thickenings. Given inverse maps modulo J, their lifted composites are identities by uniqueness. This proves all nilpotent rigidity used next, rather than importing an equivalence theorem for an étale site.

### A.5.7. Every finite formal cover comes from its zero-section restriction

In the depth-two setting of §A.5.4, let C be a finite étale algebra on V and C₀ its zero-section restriction on U. Projection p:V→U exists by the definition of V. Set D=p\*C₀. On V_n the identity of their common zero restriction lifts uniquely, by §A.5.6, to an isomorphism C|V_n≅D|V_n. Its inverse and compatibility between different n follow from the same uniqueness.

Section A.5.4 gives an actual module isomorphism C→D. It respects multiplication and unit: their compatibility is equality of two actual maps between finite locally free sheaves, verified at every V_n and then forced by faithfulness in §A.5.4. The actual inverse has its prescribed inverse completions, so both composites are identities. The same argument lifts any algebra map between two zero-section restrictions. Consequently

\[
\operatorname{FEt}(V)\simeq\operatorname{FEt}(U),
\]

with inverse given by p*. This now holds for a possibly nonnormal, nonreduced depth-two Noetherian local A. It covers exactly V=p⁻¹U, the open needed in the cover-extension argument, and does not assert the same description for unrelated larger opens.

Free human-source comparison: [Stacks, Lemma 58.26.1](https://stacks.math.columbia.edu/tag/0EY9) and [Lemma 58.17.1](https://stacks.math.columbia.edu/tag/0EL8). Sections A.5.3–A.5.6 supply the actual finite-bundle, trace-idempotent and nilpotent-map proofs, including the unit and multiplication checks.

### A.5.8. The finite algebra across a depth-two base puncture

Let A,U be as in §A.5.4 and E a finite locally free algebra on U. Section A.5.3 embeds E→O_Uʳ. Since Γ(U,O)=A, its algebra of global sections M embeds in Aʳ and is finite by Noetherianity. Localization in §A.5.3 identifies M~|U=E. Its unit and multiplication come from those on E.

For M=0 the extension and uniqueness assertions are immediate. Otherwise the regular pair a,b of A is also M-regular. Multiplication by a is injective on every locally free E chart and hence on global sections. If bz=az' in M, local freeness and regularity modulo a express z=a t on every chart; injectivity of a makes the t unique and they glue. Thus z∈aM, proving regularity of b modulo a. Finite nonzero M cannot have M/(a,b)M=0 because (a,b)⊂m and the Nakayama argument in Lemma A.5.1 applies. Lemma A.5.2 now says that M is the unique finite extension with this regular pair: every other such module is recovered from its restriction by the same sections calculation. Algebra identities are likewise determined on U.

This proves the finite extension and uniqueness over a base puncture. Section A.7.2 checks the corresponding regular-pair depth for the finite global cover algebra on the smooth total space; section7.6 applies that check to the formal comparison of §A.5.7.

## A.6. What the formal comparison controls

The two formal arguments have distinct hypotheses. Section A.4 identifies a split finite cover by its component maps and the separable trace pairing over a normal ring. Section A.5.4 instead identifies all compatible formal maps of bundles by an actual matrix kernel, allowing a nonnormal and nonreduced base with a regular pair. Section A.5.7 applies that full faithfulness to multiplication and units, so it compares finite étale algebras as algebras.

In both arguments, V is the inverse image of the punctured base inside Spec(A[[x₁,…,x_d]]). Its formal reductions are V_n, and their functions are B/Iⁿ. Localization of B is not identified with the completion of a localization. The global matrix and compatible component maps are what make the inverse-limit calculation valid on this particular open.

## A.7. Global depth and dense-fibre purity over the required normal base

This section proves the following bounded statement. Let (A,m) be a normal Noetherian local domain of dimension at least two, U=Spec(A)−{m}, and X→Spec(A) a smooth finite-type map with nonempty geometrically connected fibres. Let L be a finite separable algebra over the function field of X, and N its normalization algebra on X. Suppose N is finite étale over X_U and at the generic point of the closed fibre X_s. Then N is finite étale on all of X. A section of X over A is not required for this statement: §A.7.3 produces a section after a controlled faithfully flat local change at a hypothetical bad point.

The mathematical arguments are written below. The free human-source comparison for the geometric statement is [Stacks, Lemma 58.26.3](https://stacks.math.columbia.edu/tag/0EYB). We use the actual proofs in earlier AG-CA lessons, with exact theorem locators; no bibliography entry takes the place of any of those arguments.

### A.7.1. Normality of the smooth total space

First a polynomial ring over a normal Noetherian domain A is normal. Put F=Frac(A). The Euclidean algorithm proves F[t] is integrally closed: write an integral fraction f/g in coprime form. Clearing a monic equation shows g divides a power of f, and the Bézout identity for f,g forces g to be a unit. Thus an element w integral over A[t] is a polynomial in F[t]. By §A.2.4 some nonzero h∈A[t] clears every power wⁿ. If b,c are the leading coefficients of h,w, respectively, then bcⁿ∈A for every n. Section A.2.4 and normality give c∈A. Subtract the leading term c t^d; integrality is preserved by §A.2.1, and downward induction on degree puts every coefficient in A. Iteration handles several variables. Noetherianity is proved in §A.4.5, and localization of integral closure is §A.2.3, also valid with L=F.

Next an étale algebra C of finite presentation over a normal Noetherian ring R is normal. At q∈Spec(C), with contraction p, the flat local map R_p→C_q has a finite separable field as its local closed fibre. Flatness and the fibre description are proved in Smooth algebras and the Jacobian criterion, Theorem 6.1 and Corollary 6.2 and Formally smooth, unramified and étale maps, Theorem 7.2 and Corollary 7.3. The local dimension formula, Dimension theory, Theorem 5.1, gives dim(C_q)=dim(R_p).

If that dimension is zero, C_q is its field fibre. In dimension one, R_p is a DVR and its uniformizer generates the maximal ideal of C_q, since the quotient is the local field fibre. Thus C_q is regular. In dimension at least two, the regular pair in R_p supplied by Normal rings, Proposition 3.4 stays regular after flat local passage to C_q. The quotients are proper because the pair remains in the local maximal ideal. Hence C satisfies (R₁) and (S₂); the fully proved Serre criterion, Theorem 4.4 of that lesson, makes C normal. The argument is local on R, so includes a normal ring with several disjoint components.

The local standard form in the formally smooth lesson, Theorem 5.1, makes a smooth chart étale over a polynomial algebra in its free coordinates. Indeed, after choosing the invertible Jacobian block of the dependent coordinates, a lift through a square-zero ideal is obtained by solving the linear error equation with that block. The solution is unique when the free coordinates are fixed. Iterating handles nilpotent ideals; finite presentation gives the asserted étale map. The polynomial and étale arguments above therefore prove normality of X and of every geometric fibre.

A connected normal Noetherian scheme is integral: its irreducible components are disjoint open and closed components, by the normal-ring component proof in the normal lesson, Lemma A.4.3. Thus each geometric fibre here is integral. Every component of X dominates Spec(A). On an affine smooth chart, multiplication by a nonzero element of A is injective by flatness, whereas a minimal prime is associated and cannot contain a nonzerodivisor. Its contraction to A is therefore zero. The integral generic fibre meets every component, so there is only one. Consequently X is integral. Section A.2.3 now constructs its finite normalization N on affine charts; localization makes those algebras agree on overlaps. In a product separable generic algebra, N is a product of normal domains. This is the only normalization used in this section.

### A.7.2. A base regular pair stays regular on the cover algebra

Choose nonzero a∈m and b∈m outside the associated primes of A/aA, as in the normal lesson, Proposition 3.4. Then a,b is an A-regular pair. In particular b avoids every height-one prime containing a: these are precisely the minimal primes over (a), and all are associated to A/aA by the same lesson's Theorem 3.2 and the minimal-support theorem.

Let R be an affine normal smooth chart of X and N_R its finite normalization. Multiplication by a is injective on N_R because it injects into the product of generic fields. For each factor of N_R, every associated prime Q of its quotient by a has height one, by Normal rings, Theorem 3.2. Going down over the normal domain R, proved in Integral extensions, Theorem 4.3, shows that P=Q∩R has height at most one. It contains the nonzero element a, so has height one. Flat going down for A→R, proved in Tor and flat modules, Theorem 6.3, then shows that p=P∩A has height at most one. Again it contains a≠0, so has height one. Therefore b∉p, and hence b∉Q.

The zero-divisor description by associated primes makes b injective on N_R/aN_R. Thus the same pair is regular on every nonzero local module of N above the closed fibre. Its quotients are proper by finite-module Nakayama, since a,b are in that point's maximal ideal. Flat base change preserves the two injections, as well as the quotient that defines the second one. This applies even when the new base is nonnormal or nonreduced. We have proved exactly the global-cover depth needed in §§A.5.2 andA.5.8; normality after an arbitrary base change is neither asserted nor needed.

### A.7.3. A residue-field extension and an actual section

Let z be a closed point of X_s, let κ=A/m, and put κ'=κ(z). This is a finite extension, by the fully proved Weak Nullstellensatz, Theorem 2.1. It may be inseparable.

Choose a finite tower κ=κ₀⊂κ₁⊂⋯⊂κ_l=κ', each obtained by adjoining one element. Starting with A₀=A, lift the monic minimal polynomial at each step to A_i[t] and form A_{i+1}=A_i[t]/(lifted polynomial). Division by the monic polynomial gives a free basis 1,t,…,t^{e−1}; thus every step is finite free. Its quotient by the preceding maximal ideal is exactly the field κ_{i+1}. Since a maximal ideal in a finite integral algebra contracts to a maximal ideal (Integral extensions, Theorem 3.3), there is just one maximal ideal upstairs. The ring A_{i+1} is local, and its maximal ideal is the extension of the preceding one. The resulting A'=A_l is a faithfully flat finite free local A-algebra with

\[
A'/\mathfrak mA'=\kappa',\qquad\mathfrak mA'=\mathfrak m_{A'}.
\]

This construction uses no separability assumption and no completion or henselian base. The diagonal multiplication map κ(z)⊗_κ κ'→κ' gives a κ'-rational point z' of X_{A'} over z. Choose an étale coordinate chart X_{A'}→affine d-space over A' at z', as in §A.7.1. Lift the coordinates of z' to A'. Pulling the chart back along this constant coordinate section gives an étale A'-scheme T with a κ'-rational point t. Set A''=O_{T,t}. This is Noetherian and flat local, hence faithfully flat over A'. Its local closed fibre is the field κ', so

\[
\mathfrak mA''=\mathfrak m_{A'}A''=\mathfrak m_{A''}.\tag{A.7.1}
\]

The map Spec(A'')→T→X_{A'} gives an actual section of X_{A''}→Spec(A'') through the selected point. Every nonmaximal prime of A'' contracts to a nonmaximal prime of A: a prime over m would contain mA''=m_{A''} and therefore be maximal. Consequently the original cover, already étale over X_U, remains étale over the entire inverse image of the puncture U''=Spec(A'')−{m_{A''}}.

Write R₀=O_{X,z} and R=O_{X_{A''},z''} at this section's closed point. The map R₀→R is flat local and faithfully flat, because A→A'' is flat. Section A.7.2's pair remains regular on M=N_{z}⊗_{R₀}R. The section factors through Spec(R): every denominator outside z'' restricts to an element outside m_{A''}, hence a unit. It therefore gives a local A''-algebra retraction σ:R→A''.

### A.7.4. Constructing the formal coordinates and the dense point

Put I=ker(σ). The coordinate chart makes R formally étale over P=A''[t₁,…,t_d], with σ(t_i)=c_i. Essential localization preserves formal étaleness: an element invertible in the nilpotent quotient has an invertible lift, so every lifted algebra map factors uniquely through the same localization.

Set B=A''[[x₁,…,x_d]]. Give B/(x)ⁿ the P-algebra map t_i↦c_i+x_i. Formal étaleness uniquely lifts σ to maps R→B/(x)ⁿ. They are compatible by uniqueness, and their limit is a map R→B sending I into (x). In the other direction, x_i↦t_i−c_i defines a continuous map B→R-hat_I: a formal series is evaluated by its compatible finite truncations in the I-adic completion. The two maps are inverse. Their composite on B fixes A'' and every x_i, so fixes each truncation and its limit. On R-hat_I, reduce the other composite modulo Iⁿ. It agrees on P with the canonical R→R/Iⁿ and reduces to σ modulo I; uniqueness of the formally étale lift gives equality on R, hence on its completion. Thus

\[
\widehat R_I=B.\tag{A.7.2}
\]

This constructs the isomorphism rather than importing a smooth-completion statement. Noetherian completeness and the quotient identities used here are proved in Completion, Theorem 3.3. Since I is contained in the local maximal ideal, Completion, Theorem 3.2, makes R→B faithfully flat. Smooth flatness of R over A'' then makes B flat over A''.

Let p=m_{A''}B. The finite generation of m_{A''} gives

\[
B/\mathfrak p=\kappa'[[x_1,\ldots,x_d]],
\]

coefficientwise, so p is prime. Its contraction to R is m_{A''}R. To check this precisely, apply the exact finite-module completion theorem to R/m_{A''}R. Formula(A.7.2) identifies its completion with B/p, and I becomes the maximal ideal of its local closed fibre: σ is a κ'-rational closed point. That fibre is a local domain, since the geometric closed fibre of X is integral. Its maximal-ideal completion is faithfully flat and injective by Completion, Theorem 3.2. Thus the kernel of R→B/p is exactly m_{A''}R, which is the generic point of this local closed fibre.

This point maps to the generic point of X_s. Indeed, the closed fibre after κ→κ' is integral, and field extension is faithfully flat. The contraction of its zero prime is zero on any nonempty affine integral chart of X_s. Therefore the assumed étaleness at the generic point of X_s persists at p after base change and completion. Finally A''→B_p is a flat local map, with maximal ideal contracting to m_{A''}; it is faithfully flat. This is the dense-fibre test ring, whereas R→B is the faithful completion used at the selected closed point. They serve different purposes.

### A.7.5. The finite algebra tests used in descent

A finite flat module M over a Noetherian local ring D is free. Lift a basis of M/m_DM to a map D^r→M. Its finite cokernel is zero by Nakayama, giving a surjection with finite kernel K. Tensor with D/m_D. Flatness of M makes K/m_DK inject into (D/m_D)^r, and the chosen basis makes its image zero. Thus K=0 by Nakayama. These exactness assertions are proved in the earlier Tor lesson, Theorem 6.1.

Flatness descends along a faithfully flat D→E. For an injection of D-modules, its tensor map with M becomes injective after tensoring further with E if M⊗_D E is flat over E. Since E is flat, it tensors the original kernel to this zero kernel; faithfulness then makes that original kernel zero. This is the defining injection criterion for flatness.

Suppose a finite free commutative D-algebra C has perfect multiplication trace pairing. In each geometric fibre over an algebraically closed field k, a nilpotent u would satisfy Tr(uv)=0 for every v: multiplication by uv is nilpotent, and a basis adapted to its kernel-power filtration makes its matrix strictly triangular. Perfectness therefore forces u=0. A finite-dimensional reduced commutative k-algebra is a product of copies of k. Every prime quotient is a finite-dimensional domain, hence a field; each element is algebraic over k, so this field is k. There are only finitely many maximal ideals, because the Chinese remainder surjection to k^n bounds their number by the vector-space dimension. Their intersection is the nilradical, and the Chinese remainder theorem now gives the product decomposition. Thus the geometric fibres have zero differential module. The module Ω_{C/D} is finite, and its residue fibres at every prime of C vanish; local Nakayama makes it zero. Differential base change here follows directly from the universal property of derivations, or from its proved presentation in the earlier Kähler-differentials lesson.

Consequently C is flat, finitely presented and unramified, hence étale by the completely proved Smooth algebras, Theorem 6.2. Conversely a finite étale algebra is finite locally free and has perfect trace, as in §A.3. In particular, over a local base a finite free algebra is étale exactly when its trace determinant is a unit. This criterion does not require the rank to be invertible.

For a finite algebra, étaleness descends along a faithfully flat base map: flatness descends as just proved; differential base change and faithful detection descend Ω=0; and finite presentation holds over the Noetherian base. The same Theorem 6.2 applies. Its étale locus on the base is open: a finite free basis at a point extends to a neighborhood by clearing the finitely many kernel and cokernel generators of its basis map, and vanishing of the finite differential module likewise persists on a principal neighborhood. The complement is closed. These are the only openness and descent statements needed below.

### A.7.6. Proof of dense-fibre purity

Assume, for contradiction, that N fails to be étale somewhere on X. Its nonétale locus is closed by §A.7.5 and lies in X_s, because it is étale on X_U. A nonempty affine part of this locus has a closed point z with finite residue extension κ'/κ, by the weak Nullstellensatz. Carry out §§A.7.3–A.7.4 at z. We obtain A'', its puncture U'', R and B as above, and the finite B-algebra

\[
\widehat M=N_z\otimes_{R_0}B.
\]

The pair a,b is regular on M-hat by §A.7.2 and flatness. On V=Spec(B)×_{A''}U'', its restriction C is finite étale, by (A.7.1). Let C₀ be the zero-section restriction of C to U''. Section A.5.8 supplies the finite A''-algebra M₀=Γ(U'',C₀), with the same regular pair; section5.7 gives the actual algebra isomorphism

\[
C=p_V^*C_0,
\]

where p_V:V→U'' is projection. Since B is flat over A'', M₀⊗_{A''}B also has the regular pair a,b. Section A.5.2 recovers both finite B-modules from their sections on V. Their identified restrictions therefore give an actual algebra isomorphism

\[
\widehat M=M_0\otimes_{A''}B.\tag{A.7.3}
\]

Multiplication and units agree because they agree on V and the modules inject into their sections there. This argument never assumes that normalization commutes with completion or with A→A''.

At the prime p=m_{A''}B, the algebra M-hat_p is finite étale by the original generic-closed-fibre hypothesis and §A.7.4. Thus M₀⊗_{A''}B_p is finite free. The faithfully flat map A''→B_p descends flatness, and §A.7.5 makes M₀ free over the local ring A''. Choose a basis and let Δ∈A'' be its multiplication-trace determinant. Trace commutes with base change because the matrices of multiplication do. Equation(A.7.3) and étaleness over B_p show that the image of Δ is a unit in B_p. The map is local, so Δ is outside m_{A''} and is a unit already in A''. Section A.7.5 gives that M₀ is finite étale.

It follows from (A.7.3) that M-hat is finite étale over B. Faithfully flat descent first along R→B, then along R₀→R, makes N_z finite étale over R₀. This contradicts the choice of z. Hence N is finite étale everywhere on X. □

In relative dimension zero the selected closed fibre is already its generic point, and the bad-point contradiction is immediate; the same proof can also be read with no x variables and B=A''. In positive relative dimension the prime p is not the section's closed point: it is precisely the formal generic closed-fibre point used to descend freeness and then the trace determinant.

### A.7.7. Why the descent tests detect étaleness

The finite field extension in §A.7.3 may be inseparable; no separable-point assumption enters. Equation(A.7.1) is essential: without equality of the extended maximal ideal, the cover need not remain étale over the new base's entire puncture. Normality is used before base change to obtain the regular pair on the global cover algebra. The later formal equivalence works on a possibly nonnormal or nonreduced A'', as proved in §A.5.7. The completed cover is compared with the finite section algebra by module Hartogs, rather than an unproved compatibility of integral closure with completion.

The trace criterion is applied only after faithful flatness makes M₀ free. Perfect generic trace alone does not prove this, and trace tested merely on closed fibres would not eliminate nilpotents in arbitrary matrix entries. Here the determinant becomes a unit in a flat local test ring, hence a unit on A''. This supplies the required actual étale algebra and its descent.

## A.8. Extension over a normal base after the curve trait case

**Proposition A.8.1 (relative-curve reduction).** Assume the curve trait assertion of Theorem A.13.1. Then a generic finite étale G-torsor of invertible order, split at the generic section, extends uniquely over a smooth finite-type relative curve X→S with nonempty geometrically connected fibres and a section, where S is normal integral Noetherian. The argument applies in every base dimension. Only the trait step uses the numerical group-order hypothesis.

**Proof.** Section A.7.1 makes X normal and integral; §A.2.3 gives the finite normalization N of its generic Galois cover. It is étale over some nonempty base open. Here is the required spreading argument. Take a finite affine cover of X and on each chart choose a finite free presentation of N and a finite generating set of its differential module. Over the generic base field, the module is finite projective and the differentials vanish. A section of the presentation over that field has finitely many matrix entries and relations. Clear their base denominators, and then the finitely many denominators killing the differences from a genuine splitting; do the same for the differential generators. A common nonzero base element for the finitely many charts makes N finite locally free and unramified on its inverse image. The criterion in §A.7.5 makes it finite étale there.

Let W be the union of base opens over which N is étale everywhere. Suppose W≠S and choose a generic point s of an irreducible component of the closed complement. Every proper generization of s lies in W. Localizing the base gives the normal local domain A=O_{S,s}, whose puncture U is therefore entirely in W. Its dimension is positive. If it is one, A is a DVR by Normal rings, Theorem 1.2, and the assumed trait statement extends the generic cover. Section A.3 identifies this finite étale extension with the existing normalization N. Thus N is étale over X_A in this case.

If dim(A)≥2, restrict N to the section over U. Its generic algebra is the specified split algebra Frac(A)^r. Section A.3, applied on every normal affine chart of U, identifies its finite étale algebra with O_U^r, preserving the generic ordering. At the section's closed point, construct the completion B=A[[x₁,…,x_d]] by §A.7.4 without the residue-field change, since this is already an A-section. Section A.7.2 gives a regular base pair on the completed finite algebra. Its restriction to the inverse image V of U is split by §A.5.7. Module Hartogs, §A.5.2, then identifies the whole completed algebra with B^r, including unit and multiplication. Faithfully flat descent along the local completion shows N is étale at the section's closed point. Étaleness is open on X, and the closed fibre is integral; this open therefore contains its generic point. Theorem A.7.6 now makes N étale over all of X_A.

In both cases the same finite-presentation spreading argument used in the first paragraph works with denominators in O_S(S) outside the prime of s, rather than outside zero. On each affine chart, the finite projective presentation over A splits; clear the finitely many section entries, their relations and the differential generators. A common denominator gives a base neighborhood of s over which N is étale everywhere. This enlarges W to include s, a contradiction. Hence W=S.

The generic G-action preserves each integral closure and thus extends to N. The torsor map is an isomorphism: both of its finite algebras over X are finite étale, and generically the map is the Galois torsor isomorphism. By §A.3 both are the integral closure in that same generic algebra, so the generic isomorphism and its inverse extend. Uniqueness of the extension follows by the same normalization identification. This finishes the asserted reduction. □

For a general normal Noetherian base, apply the affine statement on base charts and glue by uniqueness. For a smooth map only locally of finite type, the argument can be applied around each chosen point to a quasi-compact open containing that point and the section over the affine base: the section image is quasi-compact, so finitely many affine neighborhoods suffice. Each fibre of this open is a nonempty open in an integral geometric fibre, hence remains integral. This gives the same local reduction. The curve trait premise is proved in Theorem A.13.1.

## A.9. Purity for the regular surfaces needed by the curve trait case

**Lemma A.9.1.** Let R be a Noetherian regular local domain of dimension two, let L be a finite separable Frac(R)-algebra, and N the integral closure of R in L. If N is finite étale over every height-one localization of R, it is finite étale over R.

**Proof.** R is normal by the fully proved Normal rings, Corollary 4.5, so N is finite by §A.2.3. Choose a regular system of parameters x,y. The regular-local lesson, Theorem 1.1 and its parameter quotient argument, makes x,y an R-regular sequence and D=R/xR a regular local ring of dimension one, hence a DVR with uniformizer the image of y.

Multiplication by x is injective on N. In each normal factor of N, an associated prime Q of N/xN has height one. Going down over normal R contracts it to a height-one prime P containing x. This prime cannot contain y, since (x,y) is the dimension-two maximal ideal. Thus y avoids every such Q and is injective on N/xN. Every nonzero element of D is a unit times a power of y, so N/xN is torsion-free over D.

A finite torsion-free module over a DVR is free, with the following direct module proof. Inject it into its finite-dimensional fraction-field vector space, choose coordinates there, and clear the finitely many generators' denominators to embed it in D^r. A submodule H⊂D^r is free by induction on r: its projection to the first coordinate is a principal ideal, choose an element of H mapping to its generator, and split off its free span. The kernel is a submodule of D^{r−1}. A zero projected ideal simply leaves that kernel. This induction proves the assertion, including zero modules. Hence N/xN is free over D. The lifting lemma5.1, using injectivity of x, makes N free over R.

Its multiplication-trace determinant Δ is nonzero because its generic algebra is separable, by §A.2.2. The height-one étaleness hypothesis makes Δ a unit in R_P at every height-one prime P. If Δ were a nonunit in R, the nonzero finite module R/ΔR would have an associated prime, and Normal rings, Theorem 3.2, would make that prime height one. It contains Δ, contradicting the localized unit. Therefore Δ is a unit in R. Section A.7.5's trace criterion makes N finite étale. □

In dimension one, the corresponding assertion is already the height-one hypothesis; in dimension zero it is separability of the generic algebra. For a smooth relative curve over a DVR, local rings of closed-fibre closed points are regular of dimension two. To verify regularity, use the étale coordinates from §A.7.1. The polynomial ring over the regular DVR is regular by Regular local rings, Proposition 3.3, whose proof includes inseparable residue fields. An étale local map has field closed fibre, so its maximal ideal is generated by the image of the base maximal ideal, and its dimension equals the base dimension by the flat local dimension formula. Minimal parameter generators therefore give regularity upstairs. At a closed point of the relative curve's closed fibre, that same flat dimension formula gives 1+1=2. Lemma A.9.1 supplies the surface-purity step in §§A.12–A.13 after the explicit DVR root extension of §A.11 removes the vertical tame ramification.

## A.10. The henselian and normalization passages actually used

The earlier programme lesson Henselian local rings and henselization proves the needed assertions: Theorem 2.2 lifts finite-algebra idempotents and decomposes a finite algebra into local factors; Proposition 3.1 makes each finite local algebra henselian; Theorems4.2 and5.1 construct the two faithfully flat henselizations with their local universal properties; Theorems6.3 and6.4 prove Noetherianity and dimension, including the noncircular completion argument. These proofs supply the local ring properties used below.

In particular, the strict henselization of a Noetherian DVR is a Noetherian DVR: its maximal ideal is still generated by the original uniformizer, it is flat, and its dimension is one. The regular-local and DVR proofs then apply. The strict henselization of a regular local ring of dimension two is again regular of dimension two: the two maximal-ideal generators still generate, the dimension is unchanged, and the embedding-dimension bound gives regularity. Its residue field is the chosen separable closure.

We also need to prove the normalization passage, rather than assume it. Let R be Noetherian normal, and let C be a Noetherian ind-étale R-algebra, meaning a filtered colimit of étale algebras, with essential localizations allowed. Then C is normal. The map is flat. At q∈Spec(C), with contraction p, the closed fibre of R_p→C_q is a field. Indeed, the unlocalized fibre is a filtered colimit of finite products of finite separable fields. If an element of its localization belongs to the selected maximal ideal, represent it at a stage and select the field factor specified by the contracted prime. Its coordinate in that factor is zero; multiplying by that factor's idempotent kills it, while that idempotent is invertible in the localization. Thus every maximal-ideal element is zero. The same argument covers localizations of the stages. The flat local dimension formula gives dim(C_q)=dim(R_p). The (R₁) and (S₂) proof in §A.7.1 now applies verbatim: the dimension-one maximal ideal is generated by the DVR parameter, and in dimension at least two a base regular pair stays regular. Serre's proved criterion makes C normal.

Let R be a normal Noetherian domain, L a finite separable generic algebra, and N its finite normalization. Suppose R→S is a flat ind-étale map with S a Noetherian domain, as for the strict henselizations just described. Then N⊗_R S is normal by the preceding argument, since it is Noetherian, finite over S, and ind-étale over N. The trace lattice of §A.2.3 embeds N in a finite free R-module; flatness embeds N⊗S in the corresponding free S-module. Thus it injects into its generic algebra L⊗_{Frac(R)}Frac(S). Its minimal primes dominate S, since nonzero elements of S act injectively. This generic algebra is its total quotient algebra. Any generic element integral over S is also integral over N⊗S; normality therefore puts it in N⊗S. Consequently

\[
\operatorname{Nor}_S\bigl(L\otimes_{\operatorname{Frac}(R)}\operatorname{Frac}(S)\bigr)=N\otimes_RS.\tag{A.10.1}
\]

This proves exactly the passage used below. It makes no analogous assertion for arbitrary completion or arbitrary flat base change.

A finite étale algebra over a strictly henselian local ring H is split. Its closed fibre is a product of finite separable extensions of the separably closed residue field, hence a product of that field. Theorem 2.2 lifts their orthogonal idempotents. Each factor is finite free over local H with residue rank one, so its unit is a basis by §A.4.2. The factors are copies of H. This derives the splitting statement from the earlier finite-algebra proof, without importing a separate finite-étale equivalence theorem.

## A.11. Removing prime-to-characteristic ramification over a DVR

### A.11.1. The degree of a field factor of a G-torsor

Let a finite separable algebra over a field be a G-torsor of rank n=|G|. After a separable closure it is a product with n coordinates on which G acts simply transitively. The embeddings of one field factor are a single orbit of the field Galois action; this action commutes with G. Hence G permutes the field-factor orbits transitively. The stabilizer H of a selected factor acts simply transitively on its embeddings: a group element taking one embedding to another in that orbit preserves the whole orbit, since it commutes with the field action. Therefore

\[
[L_i:K]=|H|\mid n.\tag{A.11.1}
\]

The |H| distinct automorphisms exhaust its embeddings. All conjugates stay in that field, so the selected extension is Galois. For the elementary conjugate argument, an embedding of a generated subfield into a separable closure extends through a finite algebraic generating tower by choosing a root of each transported minimal polynomial. Thus every root of a separable minimal polynomial occurs under an embedding of the whole field. This also proves that the elements fixed by all its automorphisms form exactly the base field. The argument works after any field extension, since the torsor identity and the simply transitive coordinate action survive tensoring. It uses no averaging.

### A.11.2. A finite extension of a strictly henselian DVR

Let A be a strictly henselian Noetherian DVR, π a uniformizer, K its fraction field, and L/K a finite Galois field extension of degree r invertible in A. Its normalization D is finite by §A.2.3 and torsion-free, hence free over A by the DVR module proof in Lemma A.9.1. It is a domain. Henselian finite-algebra decomposition makes it local, and normality and integral dimension make it a DVR. Denote its uniformizer by z, residue field by k_D, and write π=u z^e with u a unit. Put f=[k_D:k_A].

The free rank and the filtration of D/πD give

\[
r=\dim_{k_A}(D/\pi D)=ef.\tag{A.11.2}
\]

Each successive quotient z^jD/z^{j+1}D is k_D, by multiplication by z^j, for 0≤j<e. This proves the equality, rather than invoking a defect assertion. The explicit averaging-and-orbit argument in §A.11.4 proves that k_D/k_A is separable, using the Galois group and the invertibility of r. Since k_A is separably closed, f=1 and e=r. No inseparable-residue-field classification theorem is being left as an input.

The finite local algebra D is henselian. The residue of u has an r-th root in k_D, since r is invertible and the polynomial T^r−u is separable with nonzero constant term. The simple-root property lifts this root to a unit v∈D. Then τ=vz satisfies τ^r=π. The elements 1,τ,…,τ^{r−1} are K-linearly independent: their nonzero K-coefficient terms have valuations congruent to distinct integers modulo r, so the least valuation occurs only once and cannot cancel. Since [L:K]=r, they are a basis and L=K(τ).

Moreover D=A[τ]. This monic algebra is finite free, local with residue k_A and maximal ideal (τ), since π=τ^r. It has dimension one and is regular, hence is a normal DVR. Its generic field is L, so it already contains every element of L integral over A. We have proved the actual normalization, including its ring structure.

### A.11.3. Adjoining the n-th root removes the ramification

Let A be any Noetherian DVR, π its uniformizer, and let L be a finite separable generic G-torsor algebra of rank n invertible in A. Set

\[
A'=A[t]/(t^n-\pi).
\]

This is a Noetherian DVR: it is finite free, its sole closed-fibre point has maximal ideal (t), t is regular because t^n=π and π is regular on the free module, and its dimension is one. Hence it is regular local and normal. Let N' be its finite normalization in the base-changed generic algebra.

Pass from A to its strict henselization H. The ring H'=H[t]/(t^n−π) is a finite local algebra over strictly henselian H, hence henselian, with separably closed residue field. It is a DVR with uniformizer t. Also A'→H' is flat local, faithfully flat and ind-étale, being the base change of A→H.

By (A.11.1), each field factor of L⊗_K Frac(H) has degree r dividing n. Section A.11.2 makes it Frac(H)(π^{1/r}). The field Frac(H') contains all these roots, since t^{n/r} has r-th power π. It also contains every r-th root of unity: the separably closed residue field has them and Hensel lifts the simple roots of T^r−1. Thus every factor splits over Frac(H'), and the whole generic algebra is Frac(H')^n. Formula(A.10.1) identifies N'⊗_{A'}H' with its normalization, namely H'^n. Faithfully flat descent, §A.7.5, makes N' finite étale over A'. This is the required DVR ramification-removal statement.

### A.11.4. Explicit residue separability for the Galois factors

The Galois group H of order r acts on the finite local normalization D. If α∈k_D is fixed by the induced action, choose any lift a∈D and average it:

\[
a_0=\frac1r\sum_{g\in H}g(a).
\]

This belongs to D, is H-invariant and has residue α. Section A.11.1's fixed-field argument makes a₀ belong to K. Since D∩K=A by normality of A, it belongs to A. Thus the residue-field invariants are exactly k_A.

For any α∈k_D, take its distinct orbit under the induced finite group. The product ∏(T−g(α)), with duplicates omitted, is group-invariant, so its coefficients belong to k_A by the just-proved fixed-field statement. Its roots are distinct, and it annihilates α. Every α is therefore separable over k_A. Since k_A is separably closed, k_D=k_A. This proves f=1 directly for every Galois field factor used in §A.11.3. Averaging occurs here only because r is explicitly a unit; it does not replace the separable-trace argument in §A.2.

## A.12. The tame surface normal form, with its normalization checked

Let R be a Noetherian regular local ring of dimension two, let π be a member of a regular system of parameters, and let a finite étale G-torsor of order n invertible in R be given on Spec(R[1/π]). Write S=R^{sh}. It is strictly henselian regular local of dimension two by §A.10. Its quotient S/πS is a regular local domain of dimension one. The generic cover after this base change is a finite separable G-torsor algebra L over K=Frac(S). Let N_S be its finite normalization; (A.10.1) identifies it with the base change of the original normalization.

Form S'=S[t]/(t^n−π). It is finite free and local, with residue the same separably closed field. The element t is regular, and S'/tS'=S/πS is regular of dimension one. The proved lifting-regularity criterion, Regular local rings, Proposition 1.3, makes S' regular local of dimension two, hence a normal domain. It is strictly henselian because it is finite local over S. Put K'=Frac(S') and let N' be the finite normalization in L⊗_K K'.

N' is étale at every height-one prime of S'. Away from t this follows from the given étale cover and §A.3. The only height-one prime containing t is (t), since S'/tS' is a domain. Its contraction is (π). The local map

\[
S_{(\pi)}\longrightarrow S'_{(t)}=S_{(\pi)}[t]/(t^n-\pi)
\]

is exactly the DVR root extension of §A.11.3. The ring on the right is local, since its closed fibre has just the point t=0; this verifies the displayed localization identity. The generic G-torsor therefore has finite étale normalization there by §A.11.3. Lemma A.9.1 now makes N' finite étale over the whole surface S'. Section A.10 makes it split over strictly henselian S'. Hence every field factor L_i of L embeds in K'.

We determine each such factor explicitly. The residue field has a primitive n-th root of unity. To verify this elementary fact, its n distinct n-th roots form a finite subgroup. For each prime power p^a dividing n, some root has p-primary order p^a; otherwise every root would satisfy T^{n/p}=1, contradicting the bound on the number of roots. Raising such roots to eliminate the other primary components and multiplying the resulting elements gives one of order n. Hensel lifts it to ζ∈S with the same order. The n substitutions t↦ζ^j t are distinct K-automorphisms of K', and [K':K]=n because S' is a rank-n finite domain over S. Thus K'/K is cyclic Galois with these automorphisms.

By (A.11.1), L_i/K is Galois, so it is preserved by these automorphisms after its embedding in K'. On the K-basis 1,t,…,t^{n−1}, the operators

\[
P_k=\frac1n\sum_{j=0}^{n-1}\zeta^{-jk}\sigma_j
\]

project to the t^k coordinate. Indeed the geometric sum is n for equal exponents modulo n and zero otherwise. They preserve L_i. Thus L_i is the span of a subset of these monomials. Its exponent subset is a subgroup of Z/nZ: it contains zero, is closed under multiplication and inverses, and t^n=π is a nonzero K-scalar. Every subgroup is the multiples of a divisor d of n, by the division algorithm for its smallest positive exponent. Hence

\[
L_i=K(t^d),\qquad r_i=n/d,\qquad(t^d)^{r_i}=\pi.
\]

The normalization of S in L_i is exactly S[z]/(z^{r_i}−π). To check the ring, rather than omit this step, it is finite free, local with unique closed point, z is regular, and its quotient by z is the regular DVR S/πS. Proposition 1.3 makes it regular of dimension two, so it is a normal domain. Its generic field is L_i and has degree r_i, by the displayed monomial basis. Any element of L_i integral over S is integral over this normal algebra and belongs to it. Therefore

\[
N_S=\prod_iS[z_i]/(z_i^{r_i}-\pi),\qquad r_i\mid n.\tag{A.12.1}
\]

This proves the needed strict-local surface normal form and all of its normalization assertions. Free human-source comparison: [Stacks, Lemma 58.31.6](https://stacks.math.columbia.edu/tag/0EYH). The present proof uses the explicit DVR root extension and Lemma A.9.1; it does not import purity in higher-dimensional regular local rings. The invariant projections are legitimate because n is a unit.

## A.13. Split sections eliminate the remaining trait ramification

**Theorem A.13.1, relative-curve trait case.** Let A be a Noetherian DVR with fraction field K and uniformizer π. Let X→Spec(A) be a smooth finite-type relative curve with nonempty geometrically connected fibres and a section σ. A finite étale generic G-torsor of order n invertible in A, split over σ(K), extends uniquely to a finite étale G-torsor on X.

**Proof.** X is normal and integral by §A.7.1; its finite generic normalization N exists by §A.2.3. Let x=σ(s) for the closed base point s. Then R=O_{X,x} is regular local of dimension two by the end of §A.9, with π a parameter: π is regular by smooth flatness, and R/πR is regular of dimension one. Set S=R^{sh}, using the residue closure of k_A. Set T=A^{sh} with that same chosen residue closure. The section R→A→T and the local universal property, Henselian local rings, Theorem 5.1, give a local map S→T fixing π. T is a DVR with v_T(π)=1.

Formula(A.10.1) identifies N_R⊗_R S with the normalization in the strict-local generic cover, and (A.12.1) gives its product Kummer description. After π is inverted, restriction along S→Frac(T) is the original generic section fibre after extension K→Frac(T), so it is split. For every factor in (A.12.1), this gives a root of z_i^{r_i}=π in Frac(T): its positive-rank factor of the split algebra has a projection to Frac(T). If r_i>1, the valuation equation r_i v_T(z_i)=1 is impossible because the value group is Z. Hence every r_i=1, and N_R⊗S=S^n. Faithful flatness of R→S and §A.7.5 make N étale at x. This proof uses a map S[1/π]→Frac(T), not a nonexistent field embedding Frac(S)→Frac(T).

The étale locus on X is open and contains x, hence also the generic point η_s of its integral closed fibre. At every other closed point z of that fibre, O_{X,z} is a regular local surface. Every height-one prime not containing π lies on the generic fibre, where the original cover is étale. The only height-one prime containing π is the generic closed-fibre prime, where étaleness was just proved. Lemma A.9.1 makes N étale at z. Any remaining nonétale locus would be a nonempty closed subset of a finite-type curve over k_A and would have a closed point, by the weak Nullstellensatz. There is none. Thus N is finite étale on all X. The generic G-action, torsor identity and uniqueness extend exactly as in the last paragraph of §A.8. □

Free human-source comparison for the transverse section mechanism: [Stacks, Lemma 58.31.7](https://stacks.math.columbia.edu/tag/0EYI). Here the valuation, normalization, surface-purity and faithful-flat steps have each been proved explicitly.

**Corollary A.13.2, the cover extension actually used in smooth base change.** Let S be normal integral Noetherian and let X→S be a smooth relative curve with nonempty geometrically connected fibres and a section. A generic finite étale G-torsor of invertible order, split at the generic section, extends uniquely over X.

**Proof.** Apply the argument of Proposition A.8.1 to this relative curve. Its dimension-one local-base step is now Theorem A.13.1, and its higher-dimensional base step is Theorem A.7.6 with the split formal section algebra. These are actual proved inputs, so no conditional trait premise remains for this corollary. The affine-base arguments glue by uniqueness; the quasi-compact open argument at the end of §A.8 covers a smooth curve only locally of finite type. □

## A.14. The initial arithmetic normalizations are finite

We prove the arithmetic finiteness assertion: a finite-type domain over Z has finite integral closure in any finite extension of its fraction field. This includes finite-type Z[1/n]-models, their reduced irreducible components, closures of images and the subsequent finite function-field extensions. No general stability theorem for all Nagata rings is assumed.

### A.14.1. Finite-type algebras over a field

Let R be a finite-type domain over a field k and E a finite extension of Frac(R). The completely written Noether normalization, Corollary 3.2 gives a polynomial subring P=k[t₁,…,t_d] over which R is finite. Put F=Frac(P). Then E/F is finite. Integral closure of P and of R in E agree: an equation over P is an equation over R, and for the converse transitivity follows from §A.2.1. Explicitly, the finitely many coefficients of an equation over R lie in a finite P-algebra; adjoining its root gives a finite module over that algebra, hence over P, and the determinant argument gives integrality over P.

In characteristic zero E/F is separable, so §A.2.3 makes this common closure finite over P, hence over R. In characteristic p>0, choose finitely many field generators α_j of E/F. Their irreducible monic minimal polynomials have the form

\[
f_j(T)=h_j(T^{q_j}),\qquad q_j\text{ a power of }p,
\]

where h_j is separable. Divide all exponents by p as long as the derivative is zero; the process ends at a polynomial with nonzero derivative. That polynomial is irreducible, since a factorization would factor f_j, and therefore is separable by the Euclidean gcd test with its derivative. Choose a common p-power q divisible by the q_j. Only finitely many coefficients of k occur in the numerators and denominators of the coefficients of the h_j. Adjoin their q-th roots to k, in a fixed algebraic closure, obtaining a finite extension k'/k. Set

\[
P'=k'[t_1^{1/q},\ldots,t_d^{1/q}],\qquad F'=\operatorname{Frac}(P').
\]

Every coefficient of h_j has a q_j-th root in F': take roots coefficientwise in its numerator and denominator, using the root variables. If h_j(T)=Σ a_lT^l, the polynomial Σ a_l^{1/q_j}T^l has q_j-th power f_j(T). It is separable: Frobenius is injective in the algebraic closure, so its roots correspond bijectively to the distinct roots of h_j. Thus each α_j is separable over F', and E'=EF' is finite separable over F'.

The ring P' is a normal Noetherian polynomial ring by §A.7.1. It is finite over P: a finite k-basis of k' and root-variable monomials with exponents below q give a finite generating list. Section A.2.3 makes its integral closure C' in E' finite over P', hence over P. The integral closure C of P in E embeds in C', since every integral equation over P remains valid over P'. It is a P-submodule of this finite module and is therefore finite. Since C is also the closure of R and P⊂R, the same generators make it finite over R.

This proves the field case, including imperfect fields and inseparable E/Frac(R). An earlier programme proof is Normalization, Theorem 5.1; the needed trace and polynomial-normality inputs are independently supplied in §§A.2 andA.7.1 here.

### A.14.2. Finite-type domains over Z

**Theorem A.14.2.** If R is a finite-type domain over Z and E is a finite extension of Frac(R), its integral closure N in E is finite over R.

**Proof.** If char(R)=p>0, R is a finite-type F_p-domain and §A.14.1 applies. Suppose char(R)=0. Over Q, use Noether normalization on R_Q. Lift its finitely many polynomial parameters to R[1/m] for a nonzero integer m. Enlarge m to clear the coefficients of monic equations for a fixed finite list of Z-algebra generators of R. Then

\[
B=\mathbb Z[1/m][t_1,\ldots,t_d]\subset R[1/m]
\]

is a finite inclusion. The parameters are independent over Q, so the displayed base map is injective. Z[1/m] is normal: a rational number integral over Z[1/m], written in coprime numerator-denominator form, has no denominator prime outside m, as clearing its monic equation shows. It is Noetherian; §A.7.1 makes B normal Noetherian. The extension E/Frac(B) is finite and separable in characteristic zero. Section A.2.3 makes the integral closure of B in E finite; transitivity identifies it with the integral closure of R[1/m]. Thus N[1/m] is finite over R[1/m]. The localization assertion uses the equation-scaling proof in §A.2.3, which needs no normality of the original R.

It remains to work at a point x of V_R(m). Its contraction to Z is (p), for a prime p dividing m. The ring R/pR is nonzero. Corollary 3.2 of the Noether-normalization lesson applies to any nonzero finite-type F_p-algebra, including this possibly nonreduced and reducible one. Choose its polynomial normalization F_p[u₁,…,u_e] and lift the u_i to R. Put

\[
B_x=\mathbb Z[u_1,\ldots,u_e].
\]

These lifts are algebraically independent over Z. If an integer-coefficient polynomial evaluates to zero in R, reduction modulo p makes all its coefficients divisible by p, by independence in R/pR. Divide the relation by p, which is permissible because R has characteristic zero and is a domain. Repeat. A polynomial whose integer coefficients are divisible by every power of p is zero. Hence B_x is indeed a polynomial subring of R and is normal Noetherian by §A.7.1.

The point x is quasi-finite for Spec(R)→Spec(B_x). Every fibre over a point of Spec(B_x) above p is the fibre of the finite algebra R/pR over F_p[u₁,…,u_e], so is finite-dimensional over that point's residue field. The actual pointwise criterion is proved in Quasi-finite morphisms, Theorem 1.1.

Apply the written algebraic Zariski Main Theorem, Theorem 1.1. If C⊂R is the algebra of elements integral over B_x, it supplies g∈C outside x with

\[
C_g=R_g.\tag{A.14.1}
\]

This is the affine algebraic theorem, whose conductor and finite intermediate-algebra induction are proved in that lesson. Its complete earlier programme support includes the conductor-coefficient proof and the reduced strongly-transcendental proof. Only this affine theorem is used, not a nonaffine finite-factorization assertion.

Equation(A.14.1) makes Frac(R)=Frac(C) algebraic over Frac(B_x), because every element of C is integral over B_x. It is also finitely generated as a field over Frac(B_x), since R is a finite-type B_x-algebra. Therefore this field extension is finite. E/Frac(B_x) is finite separable. Let D be the finite normalization of B_x in E, supplied by §A.2.3. It contains C, and the same finite B_x-generators make D finite over C. Transitivity says D is also the integral closure of C in E. Localizing (A.14.1), D_g is exactly the integral closure of R_g in E, and is finite over R_g. Thus N is finite on a principal neighborhood of x.

The open D_R(m), together with these neighborhoods of points of V_R(m), covers Spec(R). The latter closed set is quasi-compact because R is Noetherian, so finitely many neighborhoods suffice. Integral closure localizes by the same monic-equation scaling argument. On each of this finite principal-open cover choose finite generators of N_s, represent them by numerators in N, and collect their numerators into one finite R-submodule M⊂N. Then M_s=N_s on every covering open. The quotient N/M is zero: an element vanishing after each of finitely many localizations is killed by powers of all the covering elements; their powers still generate the unit ideal, so that element is zero. This argument does not assume the quotient is finite. Hence M=N, proving finiteness. □

### A.14.3. The actual finite replacements now supplied

For a reduced finite-type Z-algebra R, its total quotient algebra is the product of the fraction fields of its finitely many minimal-prime quotients, as proved in Normal rings, Lemma A.4.3. The integral closure is the product of their integral closures. One inclusion projects every monic equation. For the other, lift a monic equation for each coordinate to R and multiply these finitely many equations: the product annihilates the tuple in every coordinate. Theorem A.14.2 makes this product finite over R. For a nonreduced model, first pass to R_red; that quotient is itself a finite R-module and has the same points. The finite normalization of its components is therefore a finite surjective replacement of the original model. Normalization is surjective by lying over.

The same theorem applies to every finite function-field extension used in the curve reductions. On a scheme's affine charts it gives finite algebras, and the monic-equation localization proof makes them agree on overlaps, yielding a finite normalization morphism. If a normal integral T maps dominantly to an integral image closure S₀, it factors through the normalization of S₀ in its own function field: pull an integral element into K(T); its equation makes it integral over each local ring of T, and normality puts it in that ring. These local maps agree in K(T) and glue. Thus normalizing the image closure gives precisely the finite base replacement used there.

In particular every finite-type Z-algebra is Nagata in the following precise sense: it is Noetherian, and each prime quotient is a finite-type domain to which Theorem A.14.2 applies in every finite fraction-field extension. This conclusion proves the stated finiteness property; it uses no general theorem about arbitrary Nagata bases.

## A.15. Smooth connected neighborhoods with a section

Every point of a smooth map X→S has an affine étale neighborhood U→X factoring as U→V→S, where V→S is affine étale and U→V is affine smooth with a section and nonempty geometrically connected fibres. We prove this over arbitrary bases by constructing the section component on an arithmetic model and retaining the originally selected point.

### A.15.1. A rational component and extension of its field

A connected finite-type scheme W over an algebraically closed field remains connected after any field extension. Suppose otherwise, and write the nontrivial global idempotent on the extension on a finite affine cover of W. Its coefficients and the compatibility equations on a finite affine cover of the overlaps involve only finitely many elements of the extension. They belong to a finite-type coefficient algebra R over the original field. Choose finite linearly independent coefficient lists on charts where the idempotent and its complement are nonzero, and invert one nonzero coefficient from each list. The equations already hold over R: tensoring a vector space with the injection R→the extension is injective. A closed point of this localized coefficient algebra has residue the original algebraically closed field by the Nullstellensatz. Specialization therefore gives a global idempotent on W; the inverted coefficients ensure that it and its complement remain nonzero. This contradicts connectedness. The finite-cover compatibility argument includes a nonaffine W.

Over an arbitrary field F, a connected finite-type W with an F-rational point is geometrically connected. The finitely many component idempotents over an algebraic closure descend to a finite separable extension. In characteristic p, raise their finite coefficient expressions to a common p-power until the algebraic coefficients become separable; an idempotent equals that power of itself. In characteristic zero no raising is needed. Enlarge to a finite Galois extension. Its group permutes the component idempotents transitively: a sum over an orbit is invariant and descends to a global idempotent on W. Descent is checked chartwise on finite F-linearly independent coefficient lists, then on their overlaps. A proper orbit would disconnect W.

Evaluation at the F-point is one on exactly one component idempotent and zero on the others. This component is fixed by the Galois group, so transitivity leaves just one component. The algebraically closed argument above handles all further field extensions. Applied to the connected component containing a rational point, this proves that it is geometrically connected. It also proves compatibility of this component with every field extension: its inverse image is connected and contains the extended point, while all other component inverse images are disjoint clopen subsets. For smooth W, the component is geometrically integral by §A.7.1.

### A.15.2. A discrete trait through an arithmetic specialization

For a nontrivial specialization z'→z in a finite-type Z-scheme, give the closure of z' its reduced structure and put D=O_{closure(z'),z}, K=κ(z'). This is a nonfield Noetherian local domain essentially of finite type over Z. The full Zorn-and-local-subring proof of Valuation rings and separatedness, Theorem 2.1 supplies a valuation ring of K dominating D.

Choose nonzero generators a₁,…,a_l of m_D with a₁ of least valuation. Then

\[
D_1=D[a_2/a_1,\ldots,a_l/a_1]\subset K
\]

lies in that valuation ring, and m_DD₁=(a₁). Its valuation centre contains a₁. Choose a prime minimal over (a₁) inside that centre. It has height one by the principal ideal theorem, and contracts to m_D because it contains all a_i and is inside the valuation centre. Localizing gives a one-dimensional local domain dominating D. It is essentially of finite type over Z. Its normalization in K is finite by Theorem A.14.2 and localization. A maximal localization of that finite normalization is a normal Noetherian local domain of dimension one, hence a DVR, with fraction field K. Thus it gives a trait whose generic and closed points map to z',z. This extends the earlier field-model construction without assuming a general discrete-domination theorem.

### A.15.3. Constructibility of the section component on a smooth model

Let S be affine of finite type over Z, let V→S be affine smooth of finite presentation, and let σ:S→V be a section. Define V⁰ to contain, in every fibre V_s, the connected component containing σ(s). By §A.15.1 these components are geometrically integral and compatible with field extension.

We use the actual smooth generic-integrality proof AG-RG-S02, Lemma 4.2. It applies to a Noetherian domain in any characteristic, not only a base containing a fixed field. Its proof writes the generic function field by étale coordinates and a primitive element, makes the resulting absolutely irreducible polynomial monic by triangular variable substitutions, and excludes each possible positive-degree factorization by a finite coefficient-equation algebra whose generic fibre is zero. Inverting finitely many base elements excludes those factorizations on every geometric fibre. Generic freeness makes a common principal open dense in every smooth fibre, completing the integral-fibre argument.

For any irreducible closed Z⊂V, let z be its generic point and s its base image. Restrict the base to the reduced closure T of s. This is integral affine of finite type over Z. The section component of the generic fibre V_{κ(s)} is clopen, hence given by an idempotent. Clear its base denominators and its idempotency equation to extend that decomposition over a nonempty principal open of T. The section is in the chosen factor there: its idempotent evaluation has generic value one and hence equals one on the integral base.

This chosen factor is affine smooth and has geometrically integral generic fibre. Lemma 4.2 makes all its fibres geometrically integral and nonempty after another principal shrink. Consequently V⁰ over this retained base open equals that clopen factor. The inverse image of the base open in Z is nonempty, open and irreducible, since it contains z. Its intersection with V⁰ is clopen, so is either the whole open or empty. Thus V⁰∩Z contains a nonempty open of Z, or is not dense in Z. The proved Noetherian constructibility criterion, Theorem 3.1 makes V⁰ constructible.

### A.15.4. Openness and arbitrary base rings

On the preceding Noetherian model, V⁰ is stable under generization. Take z∈V⁰ and a proper generization z'. Section A.15.2 gives a DVR trait in V through these two points. Pull back V and its section to this trait. There are two sections: the pulled-back σ and the tautological section coming from the trait in V. Their closed points lie in the same connected component of the special fibre, by §A.15.1. That fibre is smooth and reduced.

Remove its other components, which are a closed subset of the closed special fibre. The resulting Noetherian open U contains both sections and has connected reduced special fibre. Its connected component U₁ containing σ contains the entire special fibre and the other section as well: the image of a connected trait is connected. The generic fibre of U₁ is connected. To verify this last assertion, extend any generic idempotent on every affine chart. Write it z₀/π^r with r≥0 minimal. Flatness makes π a nonzerodivisor, so idempotency gives z₀²=π^r z₀ in that chart's ring. If r>0, reducedness modulo π gives z₀∈πR, contradicting minimality. It therefore extends without a denominator. The extensions agree on overlaps by π-injectivity, and hence give a global idempotent on connected U₁. It must be trivial. This proves connectedness of its generic fibre.

That generic fibre contains both section points. Section A.15.1 makes its rational-point component geometrically connected, so the tautological generic point belongs to the same component as σ. Field-extension compatibility then puts z' in V⁰. Thus all generizations of z remain in the constructible subset V⁰. Such a subset is open: if its constructible complement had z in its closure, a generic point of the closure of one of its finitely many locally closed pieces would lie in that piece and specialize to z, contradicting the just-proved generization property. This proves openness on the arithmetic model.

Now let S=Spec(A) be arbitrary and V affine smooth of finite presentation with section. Descend its finite presentation, section and finitely many standard smooth principal charts to a finite-type Z-subalgebra A₀⊂A. This descent can be checked from the equations: the chart isomorphisms, their inverse identities, invertible Jacobian minors and a finite unit-ideal identity for the chart cover involve finitely many coefficients. Include all of them and the images of the section's finitely many algebra generators. All these finite equations then hold on a sufficiently large such subalgebra, giving an affine smooth model with section.

For this model V₀, its component subset V₀⁰ is open by the preceding proof. Fibrewise field-extension compatibility gives

\[
V^0=V\times_{V_0}V_0^0
\]

as subsets. Hence V⁰ is open. It is quasi-compact: the Noetherian affine V₀ has a finite principal-open cover of V₀⁰, and its inverse images give a finite principal-open cover of V⁰. It is of finite presentation over S, flat and smooth, since its principal charts are. Its section factors through it, so every fibre is nonempty; its fibre is exactly the geometrically integral section component. This proves the section-component construction over every affine base, with arbitrary-base-change compatibility.

### A.15.5. The affine étale covering, retaining the originally chosen point

**Theorem A.15.5.** Every point of a smooth map has the affine étale neighborhood described at the start of §A.15.

**Proof.** Let y be any point of a smooth X→S. Restrict to affine neighborhoods W⊂X of y and Spec(A)⊂S of its image s. Choose an algebraically closed extension Ω of κ(y) and an embedding of a separable closure of κ(s) into Ω extending the given κ(s)-map. The geometric point Spec(Ω)→W then lifts y to W over that separable closure; κ(y) itself need not embed in the separable closure. Select the connected fibre component containing this lift. Its clopen idempotent descends to a finite separable extension. In characteristic p this descent follows from the idempotent p-power argument of §A.15.1, so no perfection assumption is made.

The selected smooth component has a point with finite separable residue field. Indeed take an étale coordinate chart in any nonempty open. Its image in affine space is open, by Flat morphisms, Theorem 3.2. Over the infinite separable closure a nonzero polynomial cannot vanish on all coordinate tuples, by induction on the number of variables. Choose a rational tuple in the image. Its nonempty étale fibre has a finite separable field point and hence a rational point over the separably closed field. The finitely many coordinates descend to a finite separable extension of κ(s). This reasoning can be made in the selected component. Enlarge the prior finite extension to make this point x rational; the chosen geometric lift of y also gives a point on the same descended component, by retaining the compatible residue embedding.

Lift the finite separable residue extension to an affine étale base neighborhood S₁→S, using a monic separable minimal polynomial with lifted coefficients and inverted derivative. The primitive-element proof is written in AG-RG-S02 Lemma 4.2, and the standard monic étale construction is proved in AG-CA. At x on W_{S₁}, choose an étale coordinate chart and lift its rational coordinate values to base functions after a principal shrink. Pulling this chart back along that constant coordinate section gives an affine étale S₂→S₁ with a selected point of unchanged residue field, and an actual section of W_{S₂}→S₂ through x.

Section A.15.4 gives the quasi-compact open (W_{S₂})⁰ with geometrically integral fibres. Its selected fibre contains both x and the retained lift of y. Since W_{S₂} is affine, choose a function f vanishing on its closed complement and nonvanishing at both points. Such a function exists by finite prime avoidance: the ideal of the complement is contained in neither point's prime. Then D(f) is an affine open inside (W_{S₂})⁰ containing both points. Restrict S₂ to the affine principal open where the section's evaluation of f is invertible. Put V equal to this restricted base and U=D(f)×_{S₂}V.

U and V are affine, V→S is étale, U→X is étale, and U→V is smooth with its restricted section. Every geometric fibre of U→V is a nonempty open in an integral fibre of (W_{S₂})⁰, so is geometrically connected. The chosen lift of y remains in U. Performing the construction for every y gives the claimed étale covering. □

Keeping the lift of y in the section component and then in the common affine open matters: density of separable closed points alone would not show that the covering contains an inseparable closed point. The argument above retains the original point explicitly. Free human-source comparison: [Stacks, Lemma 37.38.8](https://stacks.math.columbia.edu/tag/0EY4) and [Lemma 37.29.6](https://stacks.math.columbia.edu/tag/055R); the constructibility, arithmetic-trait and component-openness arguments used here are proved in §§A.15.1–15.4.


### A.16. Examples and exercises on the extension mechanisms

**Example A.16.1 (why the split section excludes ramification).** Let \(A\) be a strictly henselian DVR with uniformizer \(\pi\), and suppose \(r>1\) is invertible. The algebra \(A[z]/(z^r-\pi)\) is a regular DVR and has a finite étale generic fibre. It has no generic section over \(\operatorname{Frac}(A)\): a root there would satisfy \(r v(z)=1\), impossible for an integer-valued valuation. This is precisely the obstruction eliminated by the split-section condition in Theorem A.13.1. The same calculation applies to each surface factor in (A.12.1).

**Exercise A.16.2 (easy).** Why does the trace proof of Lemma A.4.3 still work when the characteristic divides the rank of the cover?

**Solution.** Over a separable closure, a rank-\(r\) étale algebra is a product of \(r\) copies of the field. Its trace pairing is \((u,v)\mapsto\sum_i u_iv_i\), whose matrix is the identity. It is nondegenerate in every characteristic, although \(\operatorname{Tr}(1)=r\) may vanish. The proof tests \(\operatorname{Tr}(zw)\) for every \(w\), and never divides by \(r\). Averaging in §A.11.4 is a different step and explicitly assumes an invertible group order.

**Exercise A.16.3 (medium).** In the matrix-kernel comparison of §A.5.4, explain why the presentation remains exact after restriction to every \(V_n\). Why would an arbitrary presentation be insufficient?

**Solution.** First embed \(E\) into a finite free bundle with locally free quotient \(Q\); then embed \(Q\) into a second finite free bundle with locally free quotient. Both short exact sequences split locally. Tensoring any such split sequence preserves exactness, so the composite presentation still computes \(E|_{V_n}\) as a kernel. An arbitrary injection need not remain injective after quotienting by \(I^n\). For example multiplication by \(t\) on \(A[[t]]\) is injective, but becomes the zero map modulo \(t\).

**Exercise A.16.4 (hard).** Suppose \(y\) in Theorem A.15.5 has inseparable residue field over its base point. Explain why the construction still covers \(y\).

**Solution.** Choose an algebraic closure \(\Omega\) containing its residue field and a compatible separable closure of the base residue field. The point over \(\Omega\) selects a component over the latter closure; it does not require an embedding of the inseparable residue extension into a separable one. Descend that component, then choose a separable closed point \(x\) in it. The étale base neighborhood supplies a section through \(x\) with the selected residue field unchanged. Both \(x\) and the retained lift of \(y\) lie in the section component. Prime avoidance chooses one principal open containing both. Restricting the base where the section value is a unit retains both selected points. Thus the covering contains a lift of the original \(y\), even though separable closed points alone would not have established that assertion.


## Appendix B. Continuity, smooth base change and field extensions

Appendix A provides the geometry required by the torsion comparison. We now prove cohomological continuity, the canonical comparison on curves, smooth base change and the sheaf comparison for every extension of fields. The continuity theorem permits arbitrary abelian sheaves. In the smooth theorem, the annihilator \(n\) is invertible on the base; filtered admissible torsion and bounded-below complexes are treated in §B.3.6. The field and separably closed invariance theorems use those same coefficient conditions.

## B.1. Cohomological continuity with varying coefficients

### B.1.1. The finite hypercover presentation

**Theorem B.1.1 (continuity).** Let T=lim_i T_i be a directed inverse system of quasi-compact quasi-separated schemes with affine transition maps. Let F_i be abelian étale sheaves with compatible maps u_{ji}^{-1}F_i→F_j, and set F=colim_i p_i^{-1}F_i. We prove the canonical isomorphism

\[
\operatorname*{colim}_i H^q(T_i,F_i)\xrightarrow{\sim}H^q(T,F),\qquad q\ge0.\tag{B.1.1}
\]

We use the actual earlier programme Hypercoverings, Theorems 3.3,4.1,6.1,7.1 and its split basis-refinement construction in §9. These proofs resolve the free augmented hypercover complex by local finite cones, construct its injective double complex, equalize parallel refinement maps by a finite-prism homotopy and identify the filtered cohomology colimit by an effaceable delta-functor. Consequently every cohomology class is represented by a hypercover cocycle, and equality of two classes is witnessed by a common refinement and a coboundary. This is a proved cohomology comparison, not an assertion that one fixed hypercover computes all coefficients.

Only finitely many levels matter for degree q: a q-cochain, its cocycle equation and a degree q−1 coboundary use levels through q+1. We may refine those levels to finite families of affine étale objects of finite presentation. Start with a finite affine étale cover of T. After finite lower levels have been chosen, each matching component is a finite limit of quasi-compact quasi-separated étale objects, hence is quasi-compact and quasi-separated. Pull back the next matching cover of the original hypercover, take a finite affine étale subcover on each of its finitely many components, and adjoin the finitely many degeneracies of lower levels. The split matching construction supplies the face-degeneracy identities and a map to the original hypercover. It can be continued in every degree. Each fixed prefix is finite even though the full simplicial object has infinitely many levels.

For this refinement L, put C=cosk_{q+1}(L_{≤q+1}). Below and through q+1 it has exactly those levels. Above that degree its matching maps are isomorphisms, so C is a hypercover. There is a natural map L→C, and their section complexes agree through q+1. Their degree-q cohomology and its maps to H^q(T,F) therefore agree by naturality of the earlier comparison. A map from C to the original hypercover is unnecessary; it need not exist. This coskeleton argument retains the represented class while reducing its construction to a finite prefix.

### B.1.2. Descent of sections, objects and covering conditions

Affinely, a finite-presentation étale algebra is given by finitely many generators, equations, chart isomorphisms, inverse equations and inverted Jacobian minors. They descend to one ring stage. Maps and their finitely many equality conditions descend for the same reason. An affine finite-presentation étale object on the limit can therefore be descended. For nonaffine quasi-compact quasi-separated objects use finite affine charts, finite overlap charts and their finite gluing maps. This is the same finite-presentation descent proved in Limits and Noetherian approximation; the chart argument shows the specific scope used here.

Finite étale covering families also descend as coverings after increasing the stage. The images of their finite-presentation étale maps are quasi-compact opens, and these images commute with base change: a fibre is nonempty exactly when it remains nonempty after a field extension. On finitely many affine charts the opens are finite unions of principal opens. If they cover on the limit, the equation putting one in the ideal of their defining functions holds at a later stage. Hence their common complement is already empty there. The same check applies to every one of the finitely many matching covers in a prefix.

Sections have an equally finite descent. A section of F on a quasi-compact quasi-separated étale object is locally a representative of some p_i^{-1}F_i, by the filtered colimit and sheafification definitions. Choose finitely many representative charts. Quasi-separatedness permits finitely many charts on their overlaps; the finitely many matching equalities, including any additional cover witnessing equality after sheafification, hold at one common later stage. Sheaf gluing then gives a section of that F_i on the descended object. Equality of two such sections is detected by the same finite choice. This proves the degree-zero case of (B.1.1), including the varying-coefficient case. No local constancy or constructibility is required.

### B.1.3. Classes and zero relations descend

Represent a class on T by the finite-prefix coskeleton of §B.1.1. Descend its objects, faces, degeneracies, matching covers and finitely many section values to a common stage by §B.1.2. Its simplicial identities and cocycle equation hold there after a further increase. The coskeleton of that descended prefix is a hypercover at the stage. Its cocycle gives a class in H^q(T_i,F_i) whose restriction is the original class. This proves surjectivity of (B.1.1).

For injectivity, first represent a stage class by a finite-prefix coskeleton at that stage. If its restriction is zero on T, the hypercover theorem supplies a refinement and a degree q−1 cochain whose differential is its restricted cocycle. Replace that refinement by a finite affine prefix as above. Its coskeleton maps to the original coskeleton: a map of prefixes into a coskeleton extends by the defining right-adjoint property. Thus its finite maps, cochain and boundary equality descend to one later stage. At that stage the original class is zero by the same hypercover comparison. A difference of classes gives equality detection. In degree zero use the section argument instead of a degree −1 cochain. This proves (B.1.1) with its canonical restriction maps.

A constant inverse system of schemes gives, in particular, commutation of H^q with filtered colimits of abelian étale sheaves on every quasi-compact quasi-separated scheme. For complexes from a fixed stage, or compatible complexes with one common lower cohomology bound, compare the cohomology-sheaf spectral sequences. In each total degree their pairs (p,r), with p≥0 and r above that fixed bound, are finite. Exact filtered colimits and (B.1.1) identify the pages and abutments. This proves bounded-below derived continuity; arbitrary systems without a common lower bound are not included.

### B.1.4. Relative images, stage recovery and scalar forgetting

In a compatible inverse system g_i:Y_i→X_i of quasi-compact quasi-separated maps with affine transitions and cartesian squares, let g:Y→X be the limit map. For coefficients as above, the relative canonical comparison is

\[
\operatorname*{colim}_i p_i^{-1}R^qg_{i,*}F_i\xrightarrow{\sim}R^qg_*F.\tag{B.1.2}
\]

It is an isomorphism. At a chosen geometric point of X, the stalk on the left is a filtered colimit of H^q over Y_i pulled back to pointed affine étale neighborhoods of the corresponding X_i point. Such objects, their point choices and their finite matching conditions descend to stages. The pairs consisting of a stage and a pointed neighborhood form a filtered system; its affine limit is the strict-local base of X at the chosen point. Apply (B.1.1) to its pulled-back schemes, which are quasi-compact quasi-separated because each g_i is. The result is the same cohomology and the same restriction map that computes the stalk on the right. Geometric stalks detect the isomorphism. This also proves the strict-local higher-direct-image formula from the sheafification of the cohomology presheaf, without assuming smooth base change.

For an arbitrary sheaf I on a scheme T=lim T_i, write π_i:T→T_i and I_i=π_{i,*}I. There is a canonical isomorphism

\[
\operatorname*{colim}_i\pi_i^{-1}I_i=I.\tag{B.1.3}
\]

Indeed an affine étale object and any finite section compatibility condition descend to a stage. On such an object, I_i is evaluated by sections on its pullback to T. The adjunction maps therefore recover every local representative of I; matching and equality descend on finite charts as in §B.1.2. Sheafification gives both surjectivity and injectivity of (B.1.3). This stage recovery applies to arbitrary sheaves.

The cohomology comparison is also valid after forgetting a constant coefficient ring Λ. Here is a direct check. The free-Λ augmented sheaf complex of a hypercover is exact: its local finite-cone contraction is the same contraction as for free abelian groups. Applying Hom_Λ into an injective Λ-module sheaf gives an exact augmented section complex. Hence positive hypercover cohomology of its underlying abelian sheaf is zero. The hypercover theorem makes that underlying sheaf acyclic on every étale object. An injective Λ-module resolution is therefore an acyclic abelian-sheaf resolution after forgetting scalars. Both compute the same section complex, with the same canonical maps. This avoids a false assumption that a Λ-module injective must be injective as an abelian sheaf, or that Λ is flat over Z.

All statements here use only finite-presentation descent and the actual earlier hypercover proof. Free comparison sources are [Stacks, Theorem 59.51.3](https://stacks.math.columbia.edu/tag/09YQ) for the general continuity theorem, [Lemma 59.51.4](https://stacks.math.columbia.edu/tag/03Q5) for filtered coefficients on one scheme, and [Lemma 59.51.5](https://stacks.math.columbia.edu/tag/03Q6) for affine base limits; the proofs needed here are supplied in §§B.1.1–B.1.4.

## B.2. Canonical curve comparison

### B.2.1. The projective finite-fibre assertion needed here

Let k be algebraically closed and let f:Y→Z be projective between finite-type k-schemes, with finite fibres. Then f is finite. This restricted assertion suffices for the invertible multiplication map on a projective abelian variety; it avoids using a nonaffine Zariski Main Theorem as an unproved intermediate step.

First an affine proper map Spec(B)→Spec(R), with R Noetherian and B of finite type over R, is finite. For b∈B, consider its map to the relative projective line, by the affine coordinate b. This map is proper: its graph is closed since the projective line is separated, and projection is the base change of the given proper map. Its image is a closed subset Z_b of P¹_R disjoint from infinity. Represent this closed subset by a finitely generated homogeneous ideal I⊂R[X₀,X₁]. Restrict homogeneous generators F_i to infinity X₀=0. Their coefficients a_i of X₁^{deg(F_i)} generate the unit ideal, since their common zero set in Spec(R) is empty. Choose Σr_i a_i=1 and an integer N at least their degrees. Then

\[
F=\sum_i r_iX_1^{N-\deg(F_i)}F_i
\]

is homogeneous, vanishes on the image and has coefficient one on X₁^N. Thus F(1,T) is monic, and F(1,b) lies in every prime of B. It is nilpotent, so a power of this monic polynomial annihilates b. Apply this to a finite algebra generating list of B. Section A.2.1 makes B a finite R-module. Empty sources give the zero finite module and cause no exception.

Now embed Y in P^r_Z. At a closed point z∈Z, its fibre has finitely many k-points. Choose a k-hyperplane avoiding them; a finite collection of proper linear conditions cannot exhaust the coefficient space over the infinite field k. The closed intersection of Y with this hyperplane has closed image in Z by properness, missing z. Choose an affine neighborhood V of z avoiding that image. Then Y_V is closed in the affine hyperplane complement, hence affine over V, and remains proper. The preceding paragraph makes it finite over V. Such neighborhoods cover every closed point of Z; their open union covers all of Z, since a nonempty closed complement in a finite-type k-scheme has a closed point. Finiteness is local on the target, proving the assertion.

### B.2.2. Invertible torsion on the represented Jacobian

For a smooth projective geometrically connected curve C over algebraically closed k, the earlier programme Picard functor of a curve proves the actual all-test-scheme statements used here. Theorem 2.1 identifies Picard classes with bundles normalized along a rational point. Proposition 5.1 constructs the nonspecial open chart from the symmetric power. Theorem 6.2 glues its translates to represent the Picard functor, and Theorem 7.2 proves that its degree-zero part J is a proper geometrically integral smooth group variety. Its projectivity follows from the fully written Abelian varieties, Proposition 1.2, using the preceding group quasi-projectivity proof and properness.

Let d be invertible in k. The differential of [d]:J→J at the identity is d times the identity: the tangent group law is addition, and induction gives the integer formula. Translations transport this differential to every geometric point. Thus [d] is étale. Here is the local lifting justification. For a map between smooth k-algebras whose cotangent map is an isomorphism, lift a given square-zero test map first as a k-map using formal smoothness. Its discrepancy on the target algebra is a derivation into the square-zero ideal. The cotangent isomorphism extends that derivation uniquely to the source, so correcting the lift makes it a target-algebra map. The same isomorphism gives uniqueness. Finite presentation gives étaleness. The cotangent map is an isomorphism on all charts because it is so on every geometric fibre between equal-rank bundles.

[d] is proper and projective, since J is projective and separated. Its étale fibres are finite zero-dimensional schemes; §B.2.1 makes it finite. Its image is open by étaleness and closed by properness, and contains the identity. Connectedness of J makes the image all of J. Thus [d] is finite étale and surjective. Its kernel J[d] is finite étale over k and hence a finite disjoint union of k-points. In dimension zero J is Spec(k), and the same assertion is immediate. The exact rank d^{2g}, when required, is proved by the cube formula and Hilbert-polynomial leading coefficient in Abelian varieties, Theorem 6.1; the finite projective-map step in that argument has just been supplied explicitly here.

If k'/k is algebraically closed, J_{k'} represents the degree-zero functor for C_{k'}. This is the base restriction of the same represented functor. Degree is preserved: coherent field base change on an affine Čech complex preserves Euler characteristic and genus, so deg(L)=χ(L)−1+g is unchanged. Therefore pullback on torsion bundles is the actual map

\
J[d\longrightarrow Jd.
\]

A finite étale scheme split over k has exactly the same labelled points after extension. This map is an isomorphism, not merely a comparison of cardinalities.

### B.2.3. The constant-coefficient curve calculation is canonical

Choose a primitive d-th root of unity in k and retain it in k'; it identifies the constant Z/d sheaf with μ_d on both fields. The Kummer sequence proved in the programme identifies

\[
H^1(C,\mu_d)=\operatorname{Pic}(C)[d]=Jd.
\]

The units quotient is zero because k is algebraically closed, and torsion bundles have degree zero. Section B.2.2 proves that the actual field-extension map on this group is an isomorphism. Degree zero is the identical group μ_d(k)=μ_d(k'). In degree two, the proved projective-curve calculation Multiplicative group on a curve, Theorem 6.2 identifies H²(C,μ_d) with Z/d by the degree of a Kummer Chern class. A rational point c gives the degree-one bundle O_C(c); its pullback is the degree-one bundle O_{C_{k'}}(c_{k'}). Naturality of Kummer sends the generator to that generator, so the comparison is the identity under the degree identifications. Higher groups vanish by that same proved calculation.

For a smooth affine connected curve A=C−S, its smooth projective completion exists by projective closure, finite normalization from §A.14.1 and the normal one-dimensional regular-local argument over the perfect field k. Its boundary S is finite and consists of k-points. The actual earlier divisor/Kummer proof, Multiplicative group on a curve, Proposition 7.2, gives

\[
\begin{gathered}0\longrightarrow H^1(C,\mu_d)\longrightarrow H^1(A,\mu_d)\longrightarrow V_S\longrightarrow0,\\V_S=\ker\bigl((\mathbb Z/d)^S\xrightarrow{\sum}\mathbb Z/d\bigr).\end{gathered}
\]

and Proposition 7.1 gives vanishing above degree one. The residue coordinates in this sequence are unchanged by extension. A base-field uniformizer at a boundary point still generates the maximal ideal of the local ring of its extended point: quotienting by it gives the field k', while that local ring is a regular curve local ring. Thus it still has valuation one, and the divisor orders of the normalized Kummer line bundles give the same coordinates. The first and last comparison maps in the short exact sequence are isomorphisms, so the middle is too. Points and finite disjoint unions give the remaining smooth finite-type curve cases.

This supplies the canonical constant-coefficient comparison used in Torsion sheaves on curves, Proposition 4.1. Its later exact-sequence, finite-cover/Sylow and filtered-colimit arguments are written in §§5–8 of that lesson. The Brauer/Tsen and units-cohomology providers used in the earlier curve calculation are the actual earlier programme proofs identified in §B.2.4.

### B.2.4. The curve reduction uses finite normalization

The finite compactification in the Sylow argument can be obtained directly from §14.1. Let X be a reduced separated finite-type curve over an algebraically closed field, let U be a smooth connected dense open in one irreducible component X₀ and disjoint from the other components, and let V→U be a connected finite étale cover. Both U and V are normal integral curves, by §7.1. Let L be the function field of V. Normalize X₀ in L. Section A.14.1 and its localization argument give a finite morphism h:Y→X₀→X, with Y normal and integral. Section A.3, applied on every affine chart of U, identifies Y×_X U with V, preserving its given finite étale map. Thus V is an open in a finite X-scheme. If X is affine, Y is affine; if X is proper, Y is proper. This proves the exact compactification assertion needed here without a nonaffine Zariski Main Theorem.

For a finite locally constant F_ℓ-sheaf M on U, choose a finite monodromy group G and an ℓ-Sylow subgroup H. The finite étale cover V→U corresponding to G/H has degree d=[G:H] prime to ℓ. Its pulled-back representation factors through H and has a filtration with trivial F_ℓ quotients. Indeed orbit counting on the nonzero finite vector space gives a nonzero H-fixed vector; its fixed line and induction on dimension give the filtration. The restriction and trace maps on M have composite d. Choosing a with ad=1 in F_ℓ gives a sheaf retraction, not just a numerical relation on a cohomology group.

If j:U→X and j':V→Y, exact finite pushforward and its geometric-stalk formula give

\[
j_!f_*f^{-1}M=h_*j'_!f^{-1}M.
\]

Over U the comparison is the identity by finite base change. Away from U every stalk on the right is a sum of zero extension-by-zero stalks. The adjunction map is therefore an isomorphism. The retraction above makes j_!M a direct summand of this sheaf. Exact j'_! applies to the representation filtration. Its quotients are extensions by zero of constants, so the constant curve calculation and the finite-boundary exact sequence transfer their vanishing and canonical field comparison to j_!M.

For a singular curve, first normalize each reduced component using §14.1. Over a dense smooth open this finite normalization is an isomorphism, and its omitted set is finite. Finite direct image and the boundary sequence

\[
0\longrightarrow j_!j^{-1}F\longrightarrow F\longrightarrow i_*i^{-1}F\longrightarrow0
\]

transfer the constant calculation to a constant sheaf and its open extensions on the singular curve. A sheaf on the finite boundary has no positive cohomology: each geometric point over the algebraically closed field has an exact sections functor, and finite pushforward is exact. The boundary exact sequence consequently controls degrees zero and one and identifies all degrees at least two. Its maps commute with field extension, including the identical boundary stalk groups.

These steps give the complete prime-coefficient curve reduction. A constructible ℓ-primary sheaf is reduced to F_ℓ-sheaves by its finite ℓ-power filtration, and a constructible torsion sheaf by primary decomposition. The Noetherian constructible-subsheaf theorem in Constructible sheaves and extension by zero expresses an arbitrary torsion sheaf on the curve as a filtered union of constructible subsheaves. Section A.17 below proves that cohomology commutes with this union. Exact inverse image and naturality then transfer the canonical field comparison. In particular on a smooth affine curve over an algebraically closed field every prime-to-characteristic torsion sheaf has zero cohomology in degrees greater than one, and every such sheaf has canonical invariance under algebraically closed extension.

The remaining all-degree units input has an actual earlier proof. Brauer groups and Tsen's theorem, Theorem 5.1, uses a field basis over k(t), one common denominator and the strict inequality between the numbers of scalar variables and homogeneous equations. It applies to all transcendence-degree-one extensions of algebraically closed k by a finite-coefficient argument. Its Theorems 3.1 and 4.4 identify the Brauer group with degree-two units cohomology and annihilate it by the reduced-norm form; its Corollary 6.1 uses the fully written continuous-module dimension tests in Galois cohomology, §§2–5. The latter proofs include continuous coinduction, restriction to a Sylow pro-ℓ subgroup, finite trivial-quotient filtrations and dimension shifting. For the nontorsion units module, Corollary 6.1 uses its torsion subgroup and rationalization to prove vanishing above degree two, then Brauer vanishing and Hilbert 90 for degrees two and one. Thus it does not apply a torsion-module dimension bound directly to a nontorsion group. Their continuity input is proved in §B.1.

## B.3. Smooth base change from the curve and continuity proofs

**Theorem B.3.1 (smooth base change).** For the cartesian square

\[
\begin{array}{ccc}Y=X\times_ST&\xrightarrow{e}&T\\h\downarrow&&\downarrow g\\X&\xrightarrow{f}&S\end{array}
\]

assume g is quasi-compact and quasi-separated and f is smooth. The diagram fixes all four maps used below; for a free human-source comparison see [Stacks, Theorem 59.89.2](https://stacks.math.columbia.edu/tag/0EYU). Fix a positive integer n invertible on S and a sheaf F of Z/n-modules on T. We prove that the canonical adjunction comparison

\[
f^{-1}R^qg_*F\xrightarrow{\sim}R^qh_*e^{-1}F.\tag{B.3.1}
\]

is an isomorphism for every q≥0. Sections B.3.2–B.3.5 first treat smooth relative curves in every degree. Only after that proof do we compose relative affine-line projections to handle an arbitrary smooth relative dimension. This proof order avoids requiring an unproved higher-degree comparison during the coordinate reduction.

### B.3.1. Degree zero using the actual section

Let a:U→V be a smooth affine map with a section σ and nonempty geometrically connected fibres, as constructed in Theorem A.15.5. For any étale sheaf of sets A on V, pullback induces

\[
\Gamma(V,A)\xrightarrow{\sim}\Gamma(U,a^{-1}A).\tag{B.3.2}
\]

Its left inverse is restriction along σ. For a section b on U, let c=σ^{-1}b. At a geometric point v of V, the restriction of a^{-1}A to U_v is the constant sheaf with value A_v. A section of a constant sheaf on a connected scheme has one value: its local values define a partition into open and closed subsets indexed by that set, so connectedness leaves just one nonempty subset. Thus b|_{U_v} has its value at σ(v), namely c_v. Pullback of c and b agree on every geometric fibre, hence at every geometric point of U; they are equal by the enough-points theorem. This proves both inverse identities in (B.3.2). It uses the section and requires no descent theorem for arbitrary sheaves along a faithfully flat map.

Apply Theorem A.15.5 to an étale object of X. It gives a covering by U→X factoring U→V→S with V affine étale and a as above. The base-changed map U×_S T→V×_S T has its inherited section and geometrically connected fibres. Apply (B.3.2) to g_*F on V and to F on V×_S T. The sections of the two sides of (B.3.1) in degree zero are then both Γ(V×_S T,F). These identifications are pullback maps and commute with the adjunction maps, so they identify the canonical comparison. The covering detects the sheaf isomorphism. The argument holds for sheaves of sets, without a torsion hypothesis.

### B.3.2. Pointed affine-curve effacement

Let C be a smooth geometrically connected affine curve over a field k with a point x∈C(k). Let K/k be any field extension, M an étale Z/n-module on Spec(K), and ξ∈H^q(C_K,M) with q>0. There are compatible finite extensions k'/k, K'/K and a finite étale Galois cover D→C_{k'}, of group order dividing a power of n, split at x_{k'}, on which ξ becomes zero after extension to K'.

Choose compatible algebraic closures k̄⊂K̄. If q>1, the affine-curve vanishing of §B.2.4 kills ξ over K̄. Section B.1.3 descends its zero relation to a finite extension K'/K. Take k'=k and the identity cover.

If q=1, M corresponds to a discrete continuous Galois module. Its finite orbits generate finite stable subgroups: finitely many generators killed by n generate a finite group. Hence it is a filtered union of finite submodules. By §B.1.3 the class comes from one of them. A finite separable extension of K trivializes its finite action. Denote the resulting constant finite abelian group by A. Its order divides a power of n. To prove this without a classification theorem, filter A by successively adjoining one generator. Each cyclic quotient has order dividing n, since A is killed by n, and the multiplication of the finite quotient orders gives the assertion.

Canonical algebraically closed curve invariance, §§B.2.3–B.2.4, writes the A-class over K̄ as the pullback of a class over k̄. Represent that class by its finite étale A-torsor P→C_{k̄}, using the proved degree-one torsor classification and effective descent of finite étale algebras. A connected component D₀ is a Galois torsor under its stabilizer subgroup H⊂A. Here A is transitive on components, and H acts simply transitively on the fibres of D₀. The component maps onto the connected base because a finite étale image is open and closed. Pulling P back to D₀ gives a section, so kills its class. Its group order divides |A|, hence a power of n.

Descend D₀, its action, its torsor map and the comparison to P to a finite extension k'/k by their finite presentations. Enlarge k' so a selected point above x is rational; the group action then splits the entire fibre at x. Embed k' into K̄ by the selected compatible closure. The class vanishes on D_{K̄}; §B.1.3 makes it vanish over a finite extension K'/K containing k'. This gives the required single cover and proves the assertion.

### B.3.3. Injectives, finite models and finite replacements

Fix q>0 and assume (B.3.1) in all lower degrees for smooth relative curves. It suffices to prove

\[
R^qh_*e^{-1}I=0.\tag{B.3.3}
\]

for every injective Z/n-module sheaf I on T. Indeed embed F→I and put Q=I/F. Compare the long exact sequences. The two groups in degree q−1 for I and Q are identified by the induction hypothesis. Their cokernels identify f^{-1}R^qg_*F and R^qh_*e^{-1}F once (B.3.3) holds, since R^qg_*I=0. Section B.1.4 justifies computing these derived images on underlying abelian sheaves.

We may take S,X,T affine. The claim is local for the étale topology on X and S. To remove an arbitrary quasi-compact quasi-separated T, use the relative Mayer–Vietoris triangle on a finite affine cover. In degree q its exact sequence uses comparison in degree q−1 on the intersection and in degree q on the two opens and their intersection; it needs no degree q+1 theorem. First prove the reduction for a quasi-compact open in an affine scheme: it is a finite union of principal opens. Induct on that number; the intersection with the last principal open is a union with one fewer principal opens. Then induct on the number of affines in a general finite cover; its intersection with the last affine is a quasi-compact open in that affine and has just been handled. This gives the reduction without a circular induction on an arbitrary number of intersection charts. Restrictions of a module injective to an open remain injective, since exact extension by zero is left adjoint.

For affine S=Spec(A), T=Spec(B), the map A→B and the smooth affine curve are a filtered limit of maps A_i→B_i and smooth affine curves over finite-type Z[1/n]-algebras. The finite equations, inverse charts, Jacobian units and covering identities descend as in §B.1.2. For π_i:T→T_i put I_i=π_{i,*}I. These are injective, because π_i^{-1} is exact. Equation(B.1.3) recovers I, and (B.1.2) identifies (B.3.3) with the filtered colimit of the vanishing assertions for I_i. Thus it suffices to prove (B.3.3) for the finite models, where dimension induction is available.

For those models, two finite replacements preserve the assertion. If π:T'→T is finite surjective, embed π^{-1}I into an injective I' on T'. The adjoint I→π_*I' is injective on geometric stalks because π is surjective. It splits since I is injective. Exact finite pushforward and finite base change make H^q(Y,e^{-1}I) a direct summand of H^q(Y',e'^{-1}I'), compatibly with every étale localization on X. Vanishing after the replacement therefore implies the required vanishing before it. A finite surjective map preserves dimension. If T→S factors through a finite S'→S, replace X by X×_S S'. The map to X is finite, and exact finite direct image identifies the desired higher image with the finite pushforward of the higher image on that replacement. Its vanishing suffices. The section and geometric fibre hypotheses are preserved by this base change.

### B.3.4. The generic class and its extension

On the finite models prove (B.3.3) by induction on dim(T), starting with the empty scheme. A local section of its higher direct image is represented, after an étale localization of X, by ξ∈H^q(Y,e^{-1}I): higher images are the sheafification of that cohomology presheaf. Use Theorem A.15.5 to give the localized affine smooth curve a section and geometrically connected fibres, after an affine étale base neighborhood. The corresponding étale replacement of T has dimension no greater than before. Its inverse image preserves injectives: restriction along an étale map is right adjoint to exact étale extension by zero, whose stalks are direct sums over the geometric lifts. The construction and exactness of that left adjoint are proved in Constructible sheaves and extension by zero, §1.

Use Theorem A.14.2 and §A.14.3 to replace T by the finite disjoint normalizations of its reduced components. Treat those components separately; their coefficient and image functors are finite direct sums. Normalize the reduced closure of the image of a chosen component in S, and factor its normal map through that finite normalization by §14.3. The finite replacements of §B.3.3 are legitimate. We now have normal integral T and S with T→S dominant. Write t,s for their generic points and K,k for their function fields.

Apply §B.3.2 on Y_t. Normalize T and S in the resulting finite field extensions K'/K and k'/k. Theorems 14.2 and14.3 make these replacements finite and give the required factorization T'→S'. The injective-sheaf replacements still apply. We obtain a generic finite étale Galois cover D→X_s whose group order divides a power of n, split along the section, on which the generic class dies after the compatible source extension.

Corollary A.13.2 extends this cover uniquely to a finite étale cover U→X: its normal Noetherian base, smooth relative-curve fibres, section, splitting and invertible group order are precisely the hypotheses proved there. Replace X by this covering and Y accordingly. We no longer require a section or connected fibres on that cover. The generic class is now zero. The generic point t is the affine inverse limit of nonempty principal opens of T. Equation(B.1.1) descends this zero relation to a nonempty open V⊂T, so

\[
\xi|_{Y_V}=0.\tag{B.3.4}
\]

### B.3.5. The two inductions finish the curve theorem

Put Z=T−V with its reduced closed structure and write j:V→T, i:Z→T and j',i' for their pullbacks to Y. Choose an injective J on Z containing i^{-1}I. The adjunction maps give a split monomorphism

\[
I\hookrightarrow j_*(I|_V)\oplus i_*J.\tag{B.3.5}
\]

It is injective because the first component is the identity on V and the second is the chosen injection on Z; geometric stalks detect this. Injectivity of I gives a retraction. It suffices to kill the two images of ξ after inverse image on Y.

The map e:Y→T remains smooth of relative dimension one, even after the finite étale covering of X. Degree-zero smooth base change from §B.3.1 and exact finite base change give

\[
\begin{aligned}e^{-1}j_*(I|_V)&=j'_*e_V^{-1}(I|_V),\\e^{-1}i_*J&=i'_*e_Z^{-1}J.\end{aligned}\tag{B.3.6}
\]

The restriction I|_V is injective. By induction on cohomological degree, applied to the relative-curve map e,

\[
R^aj'_*e_V^{-1}(I|_V)=e^{-1}R^aj_*(I|_V)=0,\qquad1\le a<q.\tag{B.3.7}
\]

The Leray spectral sequence for j' therefore has an injective edge map from H^q(Y,j'_*e_V^{-1}I|_V) to H^q(Y_V,e_V^{-1}I|_V). No differential leaves its term (q,0). A possible incoming differential has source (q−r,r−1); if its first index is nonnegative, its second is between1 and q−1 and is zero by (B.3.7). Thus the edge is injective, including q=1. Equation(B.3.4) kills the class in this open summand.

For the closed summand, exact finite pushforward identifies its cohomology with H^q(Y_Z,e_Z^{-1}J). The closed subset Z has dimension strictly smaller than T, because T was integral Noetherian of finite dimension and V was nonempty. The dimension induction in (B.3.3), for the same q and injective J, makes this class vanish after an étale covering of X. Refine that covering with the earlier ones. The retraction of (B.3.5) then kills ξ. This proves (B.3.3) in dimension dim(T).

Dimension induction proves it for every finite model. Section B.3.3 removes the model assumption and obtains comparison in degree q for relative curves. Induction on q, starting with §B.3.1, proves (B.3.1) for relative curves in all degrees. The two inductions have distinct uses:

| Induction | Input it supplies | Place used |
| --- | --- | --- |
| Cohomological degree below q | Vanishing of R^a j'_* for 1≤a<q | The injective open-summand edge map |
| Base dimension below dim(T) | Vanishing for the injective coefficient J on Z | The closed summand |

Neither uses a higher cohomological degree or the dimension currently being proved.

### B.3.6. Arbitrary smooth maps and bounded-below complexes

For the complete relative-curve theorem, compare cohomology-sheaf spectral sequences to get the canonical derived comparison on every bounded-below complex E of Z/n-sheaves. Exact inverse image commutes with H^r(E), and the proved sheaf theorem identifies every E₂ term. In a fixed total degree p+r, p≥0 and r has one lower bound, so only finitely many pairs occur and the filtered abutments are identified. All maps are the adjunction comparisons, and hence paste under composition.

An arbitrary smooth map has, étale-locally, an étale map to A^r_S. The affine-space projection factors into r relative affine-line projections. Apply the complete derived relative-curve comparison successively and paste its maps; étale change of base is localization of the étale site and has the formal comparison. This proves the canonical smooth base-change theorem in arbitrary relative dimension, for E∈D^+(T_et,Z/n), with g quasi-compact quasi-separated. For sheaves filtered by allowed invertible annihilators, exact inverse image and §B.1.3 extend the sheaf theorem by filtered colimits. The same finite-diagonal argument gives the bounded-below complex statement whose cohomology has those admissible torsion stalks.

The proof's algebraic prerequisites are the completed relative-curve assertion, arithmetic finiteness and local covering, not the stronger arbitrary-relative-dimension trait cover-extension statement. A geometric point, a strict localization or a singular source scheme is allowed in this theorem; the smoothness requirement belongs to the change of base f.

## B.4. All field extensions and their canonical comparison

### B.4.1. Smooth finite models over a perfect field

Let L/K be any extension with K perfect. Every finite set of elements of L is contained in a smooth finite-type K-subalgebra of L. We prove the field assertion needed for this statement, rather than assuming the existence of a separating transcendence basis in positive characteristic.

Take a finitely generated subfield E/K containing the set, of transcendence degree d. In characteristic zero, E is finite separable over a rational function field in any transcendence basis. Differentiating the separable minimal polynomials extends every base derivation uniquely, so dim_E Ω_{E/K}=d; the field differential proof is Kähler differentials, Lemma 6.1 and Theorem 6.2.

In characteristic p choose any transcendence basis and put F=K(t₁,…,t_d). Write h=[E:F]. Frobenius identifies E/F with E^p/F^p as abstract field extensions, so [E^p:F^p]=h. The root monomials with exponents below p give [F:F^p]=p^d, since K is perfect. The tower formula therefore gives

\[
[E:E^p]=p^d.\tag{B.4.1}
\]

Successively adjoin elements z_i of E not in the previously generated field over E^p. Every step has degree p: the new element has its p-th power in E^p, and its minimal polynomial is purely inseparable of degree either1 or p. The process takes exactly d steps by (B.4.1). The monomials ∏z_i^{e_i}, 0≤e_i<p, are a basis over E^p. Every coefficient in E^p has derivative zero, and K⊂E^p. Differentiating the unique basis expressions makes dz₁,…,dz_d span Ω_{E/K}. Their independence follows from the coordinate derivations: the presentation by z_i with relations z_i^p∈E^p has those relations of derivative zero, so the derivations taking z_i to the coordinate unit vectors are well-defined. Thus dim_E Ω_{E/K}=d also in this characteristic.

Choose a finite-type K-domain A⊂E with fraction field E containing the original finite set. At its generic point, this differential dimension is the smoothness criterion of Smooth algebras over a field and the Jacobian criterion, Theorem 2.1. Concretely the relation Jacobian has rank equal to the codimension; an invertible minor and a finite list of relation generators give a standard smooth chart after inverting one nonzero element of A. Its open-locus proof makes A_s smooth for some s≠0. This ring contains the finite set.

The resulting smooth subalgebras are filtered. Given two, include their finite lists of algebra generators in one finite subset and apply the construction; the new smooth algebra contains both. Their union is L. Hence Spec(L) is an affine inverse limit of smooth K-schemes of finite presentation. This proof allows E itself to be nonperfect and uses perfectness only for the base K.

### B.4.2. The comparison of sheaf images for every field extension

**Proposition B.4.2.** Let L/K be any field extension, g:T→S a quasi-compact quasi-separated morphism of K-schemes, and E∈D^+(T_et) with cohomology torsion of allowed orders invertible in K. Then the canonical map is an isomorphism:

\[
(S_L\to S)^{-1}Rg_*E\xrightarrow{\sim}Rg_{L,*}(E|_{T_L}).\tag{B.4.2}
\]

First suppose K is perfect. By §B.4.1, Spec(L) is an inverse limit of smooth affine finite-type K-schemes. Apply the smooth theorem of §B.3.6 at each stage and relative continuity (B.1.2). For a sheaf this gives the canonical comparison in every degree. For E use the same finite-diagonal cohomology-sheaf spectral sequences, with its fixed lower bound. This proves (B.4.2) in the perfect-base case.

For arbitrary characteristic-p K, choose compatible perfect closures K^perf⊂L^perf inside compatible algebraic closures. The maps Spec(K^perf)→Spec(K) and Spec(L^perf)→Spec(L) are integral radicial surjections and remain so after every base change. The fully written topological-invariance proof in Pushforward, pullback and finite morphisms, §§6–7 identifies their étale topoi. Its strict-local and inverse-limit steps have their continuity supplied by §17. Inverse image along either map is therefore an exact equivalence, with exact inverse direct image.

Base change along such an equivalence has the formal canonical comparison: apply its exact inverse and use composition of the two direct-image right adjoints; their identification has the adjunction unit and counit as its comparison maps. Thus both purely inseparable sides of the field diagram give isomorphisms. The comparison from K^perf to L^perf is the perfect-base case already proved. Pasting identifies the comparison from K to L^perf as an isomorphism. Factoring it through L gives the pullback of (B.4.2) along the exact faithful equivalence from L^perf to L. That pullback is an isomorphism, so (B.4.2) is an isomorphism. In characteristic zero every field is perfect, and the first case applies directly. This proves the proposition for all field extensions, including transcendental and inseparable ones.

### B.4.3. Cohomology and the unit over separably closed fields

**Theorem B.4.3.** If k'/k is an extension of separably closed fields, X is quasi-compact quasi-separated over k and E∈D^+(X_et) has prime-to-characteristic torsion cohomology, the actual pullback and adjunction unit are isomorphisms:

\[
\begin{gathered}H^q(X,E)\xrightarrow{\sim}H^q(X_{k'},E|_{X_{k'}}),\\E\xrightarrow{\sim}R\pi_*\pi^{-1}E,\qquad\pi:X_{k'}\to X.\end{gathered}\tag{B.4.3}
\]

Apply Proposition B.4.2 to X→Spec(k). The étale topos of a separably closed field is the category of sets, or abelian groups for abelian sheaves: every finite separable field extension is trivial and the affine étale objects split into copies of its spectrum. Its sections functor is exact, and inverse image to the other separably closed field sends a group to the same group. Thus the higher-image comparison gives precisely the first isomorphism of (B.4.3). This includes imperfect separably closed fields through the purely inseparable step of §B.4.2.

For the unit restrict to a quasi-compact quasi-separated étale U→X. The first comparison gives RΓ(U,E)→RΓ(U_{k'},π^{-1}E) as the actual pullback isomorphism. These are the hypercohomology presheaves of E and Rπ_*π^{-1}E. Their sheafifications in every degree are the cohomology sheaves, by the higher-image presheaf formula and its complex version. The unit is therefore an isomorphism on cohomology sheaves on this covering basis, hence an isomorphism. Every map used above is restriction or an adjunction map, so the result is canonical and compatible with coefficient maps, open restriction and composition of field extensions. It applies to singular schemes and nonconstructible admissible coefficients.


### B.5. Exercises with solutions

**Exercise B.5.1 (easy).** In §B.3.1, write the inverse to pullback on global sections. Explain why it recovers every section on \(U\).

**Solution.** The inverse is restriction along the given section \(\sigma:V\to U\). The composite in one direction is the identity because \(a\sigma=1\). In the other direction, on every geometric fibre a pulled-back sheaf is constant. The connected fibre forces a section to have just one value, which is its value at \(\sigma\). The original section and the pullback of its restriction therefore have the same geometric germs, so are equal.

**Exercise B.5.2 (medium).** Show precisely why no differential enters the term \((q,0)\) of the open-summand Leray sequence in §B.3.5.

**Solution.** A differential on page \(r\ge2\) entering \((q,0)\) starts at \((q-r,r-1)\). If \(q-r<0\), that term is absent in the first quadrant. Otherwise \(1\le r-1\le q-1\), and its higher direct-image row is zero by (B.3.7). Every outgoing differential has negative second target index and is absent. Thus \(E_2^{q,0}=E_\infty^{q,0}\). It is the last, embedded filtration piece of total degree \(q\), giving the injective edge map used to kill the class. For \(q=1\) all possible incoming terms already have negative first index.

**Exercise B.5.3 (hard).** In the continuity proof, explain why a finite-prefix coskeleton retains a represented degree-\(q\) class although it need not map to the original hypercover. Then explain why a zero relation still descends.

**Solution.** A finite affine refinement \(L\to K\) has the same represented class as \(K\). Put \(C=\operatorname{cosk}_{q+1}(L_{\le q+1})\). The natural map \(L\to C\) identifies the cochain complexes through degree \(q+1\), so identifies degree-\(q\) cohomology. Naturality of the comparison with derived cohomology identifies the represented classes. For injectivity start with a stage class on such a coskeleton. A refinement witnessing its zero relation has a finite prefix mapping to that coskeleton. The right-adjoint property extends this prefix map to a map of coskeleta. Its finite maps, cochain and boundary equation descend to a later stage, where the class is already zero. No map from \(C\) to the initial arbitrary \(K\) is used.

**Exercise B.5.4 (medium).** Explain why Proposition B.4.2 does not identify cohomology groups over two arbitrary fields. Give an example in degree one.

**Solution.** The proposition identifies higher direct images after inverse image; global sections over the two field topoi also involve their Galois actions. Let \(k\) be algebraically closed, \(K=k(t)\), \(L=\overline K\), and \(\ell\ne\operatorname{char}k\). Kummer gives \(H^1(K,\mu_\ell)=K^\times/K^{\times\ell}\). The class of \(t\) is nonzero because its valuation at zero is one, whereas an \(\ell\)-th power has valuation divisible by \(\ell\). Over \(L\) every nonzero element has an \(\ell\)-th root, so \(H^1(L,\mu_\ell)=0\). Theorem B.4.3 identifies groups when both fields are separably closed, exactly as its statement requires.


## References

- I. Mirković and K. Vilonen, [*Geometric Langlands duality and representations of algebraic groups over commutative rings*](https://arxiv.org/abs/math/0401222), freely accessible arXiv text, §§3–4 for semi-infinite geometry and weight functors.
- T. Braden, [*Hyperbolic localization of intersection cohomology*](https://arxiv.org/abs/math/0202251), freely accessible arXiv text, Theorem 1 and §6.
- T. Richarz, [*Spaces with \(\mathbb G_m\)-action, hyperbolic localization and nearby cycles*](https://arxiv.org/abs/1611.01669), freely accessible arXiv text, §2 for the contraction and localization diagrams.




- The Stacks Project, free online proofs: [formal cover splitting](https://stacks.math.columbia.edu/tag/0EY9), [formal bundle comparison](https://stacks.math.columbia.edu/tag/0EKP), [tame surface form](https://stacks.math.columbia.edu/tag/0EYH), [transverse section](https://stacks.math.columbia.edu/tag/0EYI), and [smooth neighborhoods](https://stacks.math.columbia.edu/tag/0EY4). Appendix A gives the required arguments and exact earlier programme proof locators.
