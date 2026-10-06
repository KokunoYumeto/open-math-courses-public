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

## References

- I. Mirković and K. Vilonen, [*Geometric Langlands duality and representations of algebraic groups over commutative rings*](https://arxiv.org/abs/math/0401222), freely accessible arXiv text, §§3–4 for semi-infinite geometry and weight functors.
- T. Braden, [*Hyperbolic localization of intersection cohomology*](https://arxiv.org/abs/math/0202251), freely accessible arXiv text, Theorem 1 and §6.
- T. Richarz, [*Spaces with \(\mathbb G_m\)-action, hyperbolic localization and nearby cycles*](https://arxiv.org/abs/1611.01669), freely accessible arXiv text, §2 for the contraction and localization diagrams.

