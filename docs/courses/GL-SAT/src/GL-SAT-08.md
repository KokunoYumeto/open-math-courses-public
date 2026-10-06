# Fusion and the commutativity constraint

*Written by GPT-6.1 Sol (OpenAI), October 2026. Public domain (CC0).*

Two modifications at different points are independent. When their points collide, their common endpoint remembers convolution. We prove that the global sheaf connecting these situations is uniquely determined by its restriction to different points. Exchanging those points therefore constructs commutativity. Its action on cohomology includes the usual signs of graded tensor products; a component sign converts it to the symmetry of ordinary vector spaces.

Let \(G/\mathbb C\) be connected reductive and let \(\Lambda\) be a field of characteristic zero. All perverse sheaves have finite Schubert support. Write \(\mathcal S_G\) for the classical Satake heart, \(O_\lambda=\operatorname{Gr}^{\lambda}\), \(Z_\lambda=\overline{O_\lambda}_{\mathrm{red}}\), and \(d_\lambda=\langle2\rho,\lambda\rangle\). The affine Grassmannian itself retains its full scheme structure; reduced Schubert supports are the varieties on which these classical sheaves live.

We use Beauville–Laszlo gluing and the moduli interpretation, §§1–3 and Theorem 8.1, for arbitrary-base moving modifications; Convolution and rigidity, §§1–6 and 9, for the bounded correspondences, semismallness and monoidal cohomology; and The Satake category, equations (2.4) and (6.1), for descent over contractible parameters and exact faithful cohomology. General IC parity and semisimplicity are not used. The strict extension criterion is proved in Intermediate extensions and intersection complexes, §1.

## 1. The moving endpoint functor and finite targets

For a smooth curve \(X\), the functor \(\operatorname{Gr}_{X^r}\) classifies ordered sections \(x_1,\ldots,x_r\), a \(G\)-bundle on \(X\), and a trivialization away from their graphs. Isomorphisms must respect that trivialization. A sum of graphs is a relative Cartier divisor, even when sections coincide or the parameter ring has nilpotents: in an étale coordinate its equation is a product of monic linear factors, each a nonzerodivisor. This is the moving-equation check in Lesson 3, §3.

On the locus of distinct sections, completed neighbourhoods split by the Chinese remainder theorem. Restrict the bundle and its trivialization to each neighbourhood; conversely glue these independent disc modifications to the trivial bundle on the common complement. The proved gluing equivalence makes these constructions inverse on every parameter algebra. Hence
\[
\operatorname{Gr}_{X^r}|_{U_r}
 =\prod_{i=1}^r\operatorname{Gr}_X|_{U_r}.                \tag{1.1}
\]
Here \(U_r\subset X^r\) is the all-distinct locus. On a partial diagonal, retain one section for each collision block. Repeated multiplicities leave the complement unchanged, and the completion filtrations of \(f\) and \(f^m\) are cofinal. The same moduli functor is therefore the Grassmannian for those distinct blocks. In particular the full diagonal of \(\operatorname{Gr}_{X^2}\) is \(\operatorname{Gr}_X\), not a two-step chain space. A global convolution space supplies the intermediate bundle separately.

We explain finite representability needed for its proper image. On \(X=\mathbb A^1_t\), with base \(B_r=\mathbb A^r\) and points \(a_i\), put
\[
f(t)=\prod_i(t-a_i),\quad A=R[t],\quad
\widehat A=\varprojlim A/f^qA.
\]
Monic division gives
\[
\widehat A=R[[u]][t]/(f(t)-u),\qquad u=f(t).             \tag{1.2}
\]
Precisely, divide a polynomial successively by the monic polynomial \(f\); its remainders have degree less than \(r\). Completeness then gives a unique expansion \(\sum_{q\ge0}f^q b_q(t)\), \(\deg b_q<r\). This proves (1.2), including over arbitrary rings. Thus \(\widehat A\) is finite free over \(R[[u]]\), with basis \(1,t,\ldots,t^{r-1}\), and \(u\) acts injectively.

For \(H=\operatorname{GL}(V)\), a bounded modification is a projective \(\widehat A\)-lattice \(L\) between \(f^M\widehat A^d\) and \(f^{-M}\widehat A^d\). Its finite quotient is projective over \(R\). Indeed regard these as lattices over \(R[[u]]\) of rank \(rd\), and apply the full splitting proof of Loop groups and the affine Grassmannian, Lemma 2.1. Encode the quotient in the ordinary finite Grassmannian of
\[
f^{-M}\widehat A^d/f^M\widehat A^d.
\]
Stability under multiplication by \(t\) is a closed matrix condition and gives stability under the whole algebra (1.2). Conversely, let \(Q\) be such a finite projective quotient, with \(t\)-operator \(T\). It satisfies \(f(T)^{2M}=0\). The monic operator resolution
\[
0\to R[t]\otimes_R Q\xrightarrow{t-T}
R[t]\otimes_R Q\to Q\to0                              \tag{1.3}
\]
is exact: highest coefficients prove injectivity and division by \(t-T\) proves its cokernel. Schanuel's argument from Lemma 2.1 makes the inverse-image kernel a projective \(R[t]\)-module. Completion preserves this particular resolution without any blanket flat-completion assertion. In fact multiplication by \(u-f(T)\) on \(\widehat A\otimes_RQ\) is injective, by coefficient recurrence and nilpotence of \(f(T)\). Since
\(f(t)-f(T)=(t-T)S(t,T)\), multiplication by \(t-T\) is injective too. Its cokernel evaluates \(t\) at \(T\) and \(u\) at \(f(T)\); the latter evaluation is finite on each formal series. It is exactly \(Q\). This proves the completed kernel is the desired projective lattice. We have constructed finite projective lattice stages over \(B_r\).

For general \(G\), take the faithful embedding \(G\subset H\) and equivariant open affine hull \(H/G\subset C\) proved in Lesson 2, Lemma 7.2. A reduction of an \(H\)-bundle is a section of its associated \(H/G\)-bundle. The given off-divisor trivialization prescribes that section after inverting \(f\). On an affine chart, extending it into the affine hull is exactly the vanishing of the finitely many negative \(u\)-coefficients of its finitely many coordinate series in the basis (1.2). Evaluation of its equations remains valid because \(u\) is a nonzerodivisor. This is the proof of Lemma 4.4, with that finite basis included.

The extension lands in the open quotient exactly when it does so modulo \(f\). If the pullback complement ideal is \(J\), the latter condition says \(J+(f)\) is the unit ideal. Thus \(J\) contains \(1-fb\), which is a unit by its geometric series, and the whole formal neighbourhood misses the complement. The modulo-\(f\) neighbourhood is finite over the parameter base. Its intersection with the complement has a finitely presented finite coordinate module. Take a finite presentation \(R^b\xrightarrow{D}R^a\to Q\to0\) of that coordinate module. It vanishes after a parameter change exactly where the size-\(a\) minors of \(D\) generate the unit ideal: over each local ring surjectivity is equivalent to full residue-field rank, and an invertible full minor gives a right inverse by row reduction. These minors define an open condition commuting with arbitrary base change. Hence reductions cut out a locally closed finite scheme in each lattice stage. The uniqueness of an extended section identifies these schemes on overlaps. They are separated and represent the bounded endpoint functor, with all nilpotents retained. This suffices below; properness will come from the bounded chain source.

Étale curve coordinates transport this construction to a neighbourhood of any finite collection of sections. The gluing equivalence identifies the resulting endpoint schemes on overlaps. Their maps are unique because the off-divisor trivialization is fixed. Thus the finite targets and the factorization maps are actual scheme constructions.

## 2. The proper moving chain

First take \(X=\mathbb A^1\). Fix supports \(X_i\), each a finite closed Schubert union containing the support of \(P_i\in\mathcal S_G\). A chain modifies the trivial bundle first at \(a_1\), then at \(a_2\), and so on, retaining all intermediate bundles and their relative off-point identifications.

The first support is \(X_1\times B_r\), using translation of the formal parameter. Restrict its universal bundle to a sufficiently deep finite disc around \(a_2\). Its frame scheme is a smooth finite jet torsor: smooth lifting modulo successive disc powers is the proof in Lesson 2, Lemma 4.1. Associate \(X_2\) to that torsor. Repeat with the resulting universal bundle at \(a_3\), and continue. This constructs a finite scheme \(\mathcal Y_r\) over \(B_r\). Each step is projective: the finite-stage Plücker embedding is jet-equivariant, and its representation descends to a vector bundle through the frame torsor. The associated closed support embeds in that projective bundle. Therefore
\[
\tau_r:\mathcal Y_r\to B_r
\quad\text{is proper}.                                \tag{2.1}
\]
Forgetting the intermediates gives \(m_r:\mathcal Y_r\to\operatorname{Gr}_{X^r}\). If the relative lattice bounds are \(N_i\), both bounds of the final lattice use the denominator \(\prod_i(t-a_i)^{N_i}\). Taking \(M\ge\sum_iN_i\) gives a symmetric \(f\)-bound. Thus \(m_r\) lands in one finite separated target of §1. Its graph in the product over \(B_r\) is closed; projecting that graph from the proper source proves \(m_r\) proper. This is also the graph/projection proof in AG-RG-S01, Corollary 7.B.

Descend the external product of the \(P_i\) using these finite frame torsors and their spherical equivariance. Denote its unshifted fibre normalization by \(\mathcal A_r\). Each pair of frame pullbacks has the same smooth shift; they cancel exactly as in Lesson 7, equation (2.1). On a local frame chart this complex is
\[
(P_1\boxtimes\cdots\boxtimes P_r)\boxtimes\Lambda_{B_r}.
\]
Consequently \(\mathcal A_r[r]\) is perverse on the total source and
\[
D\bigl(\mathcal A_r[r]\bigr)
 =\mathcal A_r(DP_1,\ldots,DP_r)[r].                    \tag{2.2}
\]
The source strata are their relative orbit indices \((\alpha_1,\ldots,\alpha_r)\). Frame charts make their dimensions \(\sum_i d_{\alpha_i}+r\), and their ordinary sheaf degrees in \(\mathcal A_r[r]\) are at most the negative of that number. Those charts also make the source stratification Whitney and each stratum smooth over \(B_r\), by the product and orbit argument in Lesson 7, §4.

On \(U_r\), disjoint gluing makes the endpoint map an isomorphism on this support, and
\[
(m_r,\mathcal A_r)|_{U_r}
 =\bigl(\mathrm{id},P_1\boxtimes\cdots\boxtimes P_r\bigr)
   \times U_r.                                        \tag{2.3}
\]
On the full diagonal the chain is the local convolution chain. Its proper image is the iterated convolution with the associativity proved in Lesson 7, §6.

## 3. Strict bounds at every collision

We first extend the local semismall estimate to an \(r\)-step chain. For fixed source indices and target type \(\nu\), it is
\[
2\dim F_\nu\le\sum_i d_{\alpha_i}-d_\nu.               \tag{3.1}
\]
Induct on \(r\). Partition the penultimate endpoint into its finitely many orbit types \(\delta\). The last two-endpoint fibre has dimension at most \((d_\delta+d_{\alpha_r}-d_\nu)/2\), by Lesson 7, equation (4.1). Over each of its first endpoints the prior-chain fibre has dimension at most \((\sum_{i<r}d_{\alpha_i}-d_\delta)/2\), by induction. The finite partition and fibre-dimension estimate bound that entire piece by their sum. Taking the maximum cancels \(d_\delta\) and proves (3.1). The identical argument works for every source-stratum closure and its open pieces.

Suppose a partial diagonal has \(b\) distinct collision blocks. Its base dimension is \(b\), and its codimension in \(B_r\) is \(c=r-b\). Factorization breaks the fibre into one local chain for each block, preserving the relative order within that block. For endpoint types \(\nu_1,\ldots,\nu_b\), (3.1) gives
\[
2\dim F\le\sum_i d_{\alpha_i}-\sum_jd_{\nu_j}.          \tag{3.2}
\]
The target orbit-product stratum has dimension
\(s=\sum_jd_{\nu_j}+b\).

Let
\[
\mathcal F_r(P_1,\ldots,P_r)
 =Rm_{r*}\bigl(\mathcal A_r[r]\bigr).                  \tag{3.3}
\]
On a fibre piece in the indicated source stratum, compact-support cohomological dimension is at most twice its dimension. The ordinary-degree bound of §2 and (3.2) therefore give
\[
H^k\bigl(\mathcal F_r(P_1,\ldots,P_r)_z\bigr)=0
\quad\text{for }k>-\sum_jd_{\nu_j}-r=-s-c.             \tag{3.4}
\]
As in Lesson 7, §5, use compact supports on each possibly nonproper piece, assemble by the finite closed filtration of source indices, and only then replace compact by ordinary cohomology on the full proper fibre. Proper base change proves (3.4) for the actual stalk. Applying the same proof to (2.2) proves the dual bound. Thus \(\mathcal F_r\) is perverse. Over any collision, \(c\ge1\), and both its stalk and costalk bounds are strict relative to the boundary stratum.

These assertions may be tested on a finite Whitney refinement. A refinement lowers a stratum's dimension, so (3.4) remains at least as strong as the required upper bound; the same argument applies to its dual. Local constructibility on the orbit-product strata follows from factorization and the finite jet orbit charts. The resulting strict support tests are exactly the closed perverse inequalities excluding a boundary quotient and a boundary subobject. The extension construction and uniqueness in GL-PERV's intermediate-extensions lesson, equations (1.2)–(1.4), now give
\[
\mathcal F_r(P_1,\ldots,P_r)
 =j_{r!*}\bigl((P_1\boxtimes\cdots\boxtimes P_r)
                \boxtimes\Lambda_{U_r}[r]\bigr).       \tag{3.5}
\]
No decomposition theorem has been used. The extra strict degree comes from the positive collision codimension.

For \(r=2\), let \(i\) be the diagonal inclusion. Ordinary proper base change, with the shifts left visible, gives
\[
i^*\mathcal F_2(P,Q)[-1]
 =(P*Q)\boxtimes\Lambda_{\mathbb A^1}[1].              \tag{3.6}
\]
At a selected diagonal point, ordinary restriction followed by \([-2]\) is \(P*Q\). These are the fibre and diagonal normalizations of fusion.

There are also coherent partial-fusion comparisons. For three points, let \(i_{12}\) impose \(a_1=a_2\). Collapse those first two modifications and take a sufficiently deep frame of their common endpoint. On that cover the collapse is the first local convolution map times the unchanged third support. Proper base change and projection formula identify its coefficient image with \((P*Q)\widetilde\boxtimes R\). Spherical equivariance of \(P*Q\) and finite frame descent make this identification global. Its total shift changes from \([3]\) to \([2]\), giving
\[
i_{12}^*\mathcal F_3(P,Q,R)[-1]=\mathcal F_2(P*Q,R).
\tag{3.7}
\]
The same argument on the last two relative modifications gives \(i_{23}^*\mathcal F_3(P,Q,R)[-1]=\mathcal F_2(P,Q*R)\). These identities hold over the whole partial diagonal, including its further collision. Repeated-divisor bounds can be placed in one common finite stage because the repeated polynomial divides a sufficiently large power of the distinct-block polynomial; the resulting lattice conditions are closed incidences, and Lesson 3, equation (8.2), identifies their full endpoint functors. Restrict both comparisons again to the full diagonal. Their identifications are the associator of Lesson 7, since both are proper composition on the same three-step chain and the same external-product maps. Thus fusion's binary grouping agrees with the already constructed convolution associator.

## 4. Local acyclicity in this family

We give the classical local acyclicity argument, including its compatibility with base change. It does not use general nearby-cycle t-exactness.

The source \(\mathcal Y_r\to B_r\) is proper and Whitney stratified, with every source stratum smooth over the base. The controlled-flow proof in Constructible complexes on algebraic varieties, Appendix I.6, makes it a stratum-preserving product over each sufficiently small base ball. Lesson 6, equation (2.4), descends the entire complex in that product, including its attaching maps. Locally the pair is therefore
\[
(\mathcal Y_r,\mathcal A_r)=
(Y_0,A_0)\times B_0.                                  \tag{4.1}
\]
Pulling the base back preserves this product and its coefficient description.

Here local acyclicity means that specialization to a nearby parameter changes no local coefficient complex; universally means the same after every algebraic parameter base change, on the associated analytic spaces. To check it explicitly, test an analytic disc in such a changed base. Nearby cycles are computed by lifting its punctured disc to its universal cover and taking neighbourhood cochains. In the product (4.1), the lifted parameter is contractible and the complex is pulled back from \(Y_0\). The cochain comparison is the identity on the fibre coefficient complex. Taking the filtered colimit over fibre neighbourhoods gives its stalk. Thus specialization is an isomorphism, monodromy is the identity, and its cone of vanishing cycles is zero. The same calculation works around every point and after every base change. This proves universal local acyclicity for \(\mathcal A_r\) in this classical family.

It passes through this proper endpoint map. Here is the needed proof, rather than a general cycle citation. Write nearby cycles as \(i^*R(jp)_*p^*j^*\), where \(p\) is the pulled-back punctured-disc cover. Proper base change moves the proper image past \(p^*\) and past the special-fibre restriction \(i^*\). Composition of direct images moves it past \(R(jp)_*\). These are equalities of the actual maps of sheaf resolutions; hence
\[
R\psi\, Rm_{r*}K=Rm_{r,0*}R\psi K
\]
with the specialization maps identified. Taking their cones gives the identical equality for \(R\phi\). Properness remains true after the parameter change. Apply this to (4.1): the source vanishing complex is zero, so the endpoint vanishing complex is zero too. Consequently (3.5) is the universally locally acyclic extension used for fusion. Its diagonal specialization is ordinary restriction, with the shifts in (3.6). General cycle constructibility or t-exactness is not an additional input to this calculation.

## 5. Exchanging points constructs commutativity

Let \(\sigma(a,b)=(b,a)\). The endpoint moduli problem depends on the union of its graphs, so it has an involution covering \(\sigma\). Over the distinct-point locus it interchanges the two factors. Equation (3.5) for \(r=2\) uniquely extends the derived external-product symmetry to an isomorphism
\[
\mathcal F_2(P,Q)\longrightarrow\sigma^*\mathcal F_2(Q,P).
\tag{5.1}
\]
Our normalization on that open locus is
\((P\boxtimes Q)\boxtimes\Lambda_U[2]\).
The map in (5.1) exchanges \(P,Q\) and uses the identity on the single constant base factor, pulled back by \(\sigma\). This convention matters: exchanging two separately shifted degree-one base factors would insert an extra minus sign, including for the unit. Using the one base factor gives the unit its identity symmetry.

Restrict (5.1) to a diagonal point and shift by \([-2]\). By (3.6) this is
\[
c_{P,Q}:P*Q\xrightarrow{\sim}Q*P.                      \tag{5.2}
\]
It is natural in both objects. Enlarging supports or jet bounds extends the same open map; uniqueness of intermediate extension and proper base change identify the same diagonal map. Therefore (5.2) is defined on the entire bounded heart.

We verify all coherence, using the faithful monoidal functor already proved in Lesson 7, §9. Its construction transports cohomology in the proper source family \(\mathcal Y_2\) over the contractible base \(\mathbb A^2\). Proper composition identifies source cohomology with endpoint cohomology. On the distinct-point locus, (5.1) is exactly the derived tensor exchange. Thus, under that monoidal identification,
\[
H(c_{P,Q})(v\otimes w)=(-1)^{ab}w\otimes v,
\quad v\in H^a(P),\ w\in H^b(Q).                      \tag{5.3}
\]
The endpoint map (5.1) induces a map between the constant cohomology systems over the whole base; equality on the nonempty distinct locus proves equality everywhere. There is no chosen path or spectral-sequence splitting in (5.3).

The graded exchange squares to one because \(ab+ba\) is even. The two hexagons are the identities of signs
\(a(b+c)=ab+ac\) and \((a+b)c=ac+bc\), with the usual tensor associator. The degree-zero unit has identity exchange. Lesson 7's cohomology comparisons respect the associator and unit. Hence applying \(H\) to the two sides of each categorical coherence diagram gives equal maps. Its faithfulness on heart morphisms makes the original maps equal. This proves symmetry, both hexagons and the unit identities for (5.2), with the given convolution associator. In particular \((\mathcal S_G,*,\mathbf1,c)\) is a rigid symmetric monoidal category, and graded cohomology is a symmetric monoidal functor with graded tensor signs.

## 6. Formal coordinates and arbitrary smooth curves

We prove the coordinate equivariance required to make the construction intrinsic. Let \(Y\) be a proper finite Schubert union with faithful lattice bound \(A\). Put
\[
\mathscr A_r=\operatorname{Aut}(\mathbb C[t]/t^{r+1},(t))
 =\{t\mapsto a_1t+\cdots+a_rt^r:\ a_1\ne0\}.
\]
As a variety it is \(\mathbb G_m\times\mathbb A^{r-1}\), so connected and smooth. If a formal substitution is the identity modulo \(t^{r+1}\), then for every integer \(j\ge-A\)
\[
\phi(t)^j-t^j\in t^{j+r}R[[t]].
\]
For negative integers this follows from the integral-coefficient binomial expansion of \((1+t^r b)^j\). Thus for \(r\ge2A\) substitution is the identity on \(t^{-A}V_O/t^AV_O\). Its action on the bounded stage factors through \(\mathscr A_r\), over every parameter ring.

It preserves spherical orbit indices: \(\phi(t^\lambda)=t^\lambda\lambda(\phi(t)/t)\), with the second factor integral, and substitution preserves integral loops. Choose sufficiently large \(m\) for the spherical action and \(r\ge m\). The finite semidirect group
\(S=J_mG\rtimes\mathscr A_r\)
is smooth and connected, acts on \(Y\), and preserves its orbit stratification.

For any \(P\) in our heart, parameter descent in Lesson 6, equation (2.4), gives local transport of the complexes \(s^*P\) on contractible coordinate balls in \(S\). This transports attaching maps as well as orbit local systems. We show that all its loop monodromy is trivial, including a possible extension automorphism. Let \(\pi:S\times Y\to S\), \(a(s,y)=sy\) and \(p(s,y)=y\). Before choosing any equivariance, the homeomorphism
\[
\Phi(s,y)=(s,sy),\qquad\pi\Phi=\pi,
\]
and proper product base change give a canonical identification
\[
R\pi_*a^*P=R\pi_*p^*P
 =\underline{R\Gamma(Y,P)}_S.                          \tag{6.1}
\]
On a parameter ball, normalized transport induces a map between these constant cohomology systems; its normalization is the identity, so it is the identity throughout that ball. Transport around a loop at the identity therefore gives a perverse automorphism \(b:P\to P\) with \(H^*(b)=1\). It is a morphism in the spherical heart, by the full-faithfulness assertion of Lesson 6, §2. Faithfulness in §6 forces \(b=1\). This controls all loops, including the infinite winding subgroup of \(\mathscr A_r\); an argument using only stalks would not exclude extension automorphisms.

The transports from the identity are consequently path independent and glue to \(p^*P\simeq a^*P\). Connected-group full faithfulness in GL-PERV's equivariant lesson, Theorem 1.1, gives uniqueness after this identity normalization. On \(S\times S\), the two composite structures have that same normalization, so uniqueness proves the cocycle; it also proves compatibility with every morphism. Its restriction to \(J_mG\) is the existing spherical structure. Increasing \(r,m\) gives the identical structure by uniqueness. We have proved automatic formal-coordinate equivariance without semisimplicity.

For a smooth curve \(C\), the \(r\)-jets of formal parameters along the diagonal form a \(\mathscr A_r\)-torsor. An étale coordinate \(z\) supplies the parameter \(z(y)-z(x)\). Changes of coordinate are exactly the substitutions above. Use the proved structure to glue
\(P\boxtimes\Lambda_C[1]\)
in these charts. This constructs a normalized spread \(P_C\) on \(\operatorname{Gr}_C\), independent of parameters and jet level. Its fibre cohomology transitions are identities by (6.1), even if the curve is not simply connected. The finite frame construction of §2, using these spreads, now makes the global convolution sheaf on any smooth curve.

Here is the precise étale comparison near collisions. For a separated étale map \(q:U\to V\), restrict \(U^r\) to the open excluding tuples of distinct marked points with the same image. This open contains its full diagonal. In the inverse image of each marked graph on \(V\), its selected graph on \(U\) is open and closed, since it is a section of a separated étale morphism. Remove the other branches. On the resulting neighbourhood of the graphs, the pulled-back sum of divisors is exactly their sum on \(U\). Each thickening of the selected divisor maps étale, universally injectively and surjectively to the target thickening; the étale open-immersion criterion of AG-FSE's étale local-structure lesson, Theorem 4.1, makes it an isomorphism. The completed and punctured neighbourhoods are therefore canonically isomorphic, including over rings with nilpotents.

Restriction to these neighbourhoods, followed by the uniquely effective gluing of Lesson 3, compares the moving endpoint and chain functors. The comparison commutes with partitions, diagonals and permutations, because the formal restriction maps do. It compares the coefficient spreads through their coordinate torsors. Proper base change compares their images. It preserves the strict boundary extension tests, so (3.5) and its maps compare by uniqueness of intermediate extension. Finally diagonal restriction commutes with these comparisons. Étale coordinates compare any pointed smooth curve locally with \(\mathbb A^1\). Their transition substitutions and the just-proved cocycles show that the resulting local fusion constraint is independent of both the coordinate and the curve, under the identification by its formal disc.

## 7. Component parity and the sign modification

The parity
\[
\epsilon(\lambda)=\langle2\rho,\lambda\rangle\pmod2
\]
descends to \(X_*(T)/\mathbb Z\Phi^\vee\). Indeed \(\langle2\rho,\alpha_i^\vee\rangle=2\) for every simple coroot: a simple reflection permutes positive roots other than its own and sends that root to its negative, giving this pairing. Integral coroot combinations therefore pair evenly. The component homomorphism of Lesson 4, §5, identifies this quotient with components and is additive on products. Hence \(\epsilon\) is a component homomorphism and convolution adds it. The dominance order compares only coweights whose difference is an integral positive coroot combination, so comparable types have the same parity.

Every object splits canonically into its even and odd component supports. Its global cohomology has the same parity as its component. This uses global weight concentration, not an IC-stalk parity claim: Lesson 5 proves
\[
H^k(P)=\bigoplus_{\langle2\rho,\nu\rangle=k}F_\nu(P).
\tag{7.1}
\]
If the support has component parity \(e\), a nonzero \(F_\nu(P)\) lies on that same component, so \(k\equiv e\). Formula (7.1) holds for every perverse object by that lesson's proved exactness and concentration.

For homogeneous component objects define
\[
c'_{P,Q}=(-1)^{\epsilon(P)\epsilon(Q)}c_{P,Q},           \tag{7.2}
\]
and extend by their canonical direct-sum decomposition. This still squares to one. Both hexagons hold because component parity adds: the extra exponents satisfy the same bilinear identities as those in §5. Under cohomology the two signs cancel by (7.1), leaving the ordinary exchange \(v\otimes w\mapsto w\otimes v\). Thus
\[
H^*:(\mathcal S_G,*,\mathbf1,c')\longrightarrow
\operatorname{Vect}^{\mathrm{fd}}_\Lambda
\]
is an exact faithful symmetric monoidal functor when its grading is forgotten. Its monoidal maps are precisely those of Lesson 7; only the category's symmetry changed.

The categorical dimension is the trace formed from coevaluation, symmetry and evaluation. Under the naive constraint choose a homogeneous basis of graded cohomology. Coevaluation pairs each basis vector with its dual of opposite degree; the graded exchange contributes \((-1)^k\) to the evaluation of a degree-\(k\) basis vector. Consequently
\[
\dim_c P=\sum_k(-1)^k\dim H^k(P)
 =(-1)^{\epsilon(P)}\dim H^*(P)                         \tag{7.3}
\]
for a homogeneous object. With (7.2) its self-exchange gains \((-1)^{\epsilon(P)}\), and
\[
\dim_{c'}P=\dim H^*(P).                               \tag{7.4}
\]
These are direct trace computations using the rigidity of Lesson 7, not an appeal to a dimension criterion. In particular they apply to \(IC_\lambda\). A nonzero object has nonzero cohomology by faithfulness, so the modified dimensions are positive integers. The sign is required if this same cohomology functor is to preserve the ordinary vector-space symmetry on an odd component.

## 8. Tori and the minuscule examples

For \(G=\mathbb G_m\), the full two-point functor is the line-bundle modification functor of §1. On a formal completed divisor it consists of projective rank-one lattices \(L\subset\widehat A[1/f]\) with a specified punctured identification. The finite stable-quotient description in §1 gives its full bounded schemes. They retain infinitesimal families: over the dual numbers, \((1+\eta f^{-1})\widehat A\), \(\eta^2=0\), is a lattice with inverse generator \(1-\eta f^{-1}\), and is different from the standard lattice because its generator is not an integral unit.

On complex geometric points, distinct points carry integers \((m,n)\), their local line indices. The full diagonal carries one integer \(m+n\). The section for those indices is, over every parameter ring,
\[
L_{m,n}=(t-a)^m(t-b)^n\widehat A.                       \tag{8.1}
\]
Negative exponents are permitted after inverting \(f\). At \(a=b\) it is \((t-a)^{m+n}\widehat A\). Sections with different pairs but the same sum thus meet along the diagonal; the full global ind-scheme is not a disjoint union of copies of the whole base indexed by pairs. For the two skyscrapers, the bounded chain source is the base itself and its sheaf is \(\Lambda_{\mathbb A^2}[2]\). Fusion gives
\[
\delta_m*\delta_n=\delta_{m+n},\qquad c_{m,n}=1.         \tag{8.2}
\]
The scalar factors in (8.1) commute, and each skyscraper has degree-zero cohomology. All torus components have \(\epsilon=0\), so no modification of this symmetry occurs.

For \(\operatorname{PGL}_2\), the primitive positive coweight \(\omega^\vee\) has orbit \(\mathbb P^1\) of dimension one. Its IC is \(P=\Lambda_{\mathbb P^1}[1]\), with one cohomology generator in each degree \(-1,1\). Both are odd, and therefore
\[
\dim_cP=-2,\qquad\dim_{c'}P=2.                         \tag{8.3}
\]
Lesson 7 explicitly constructs \(P*P=IC_{2\omega^\vee}\oplus IC_0\). Its total cohomology has dimensions \(1,2,1\) in degrees \(-2,0,2\); this is consistent with the tensor square and does not require general semisimplicity.

For \(\operatorname{GL}_2\), let \(P=IC_{(1,0)}\) and choose generators \(v_-\in H^{-1}(P)\), \(v_+\in H^1(P)\). The naive symmetry on its tensor square is the negative of the ordinary flip. Explicitly,
\[
\begin{aligned}
c(v_-\otimes v_-)&=-v_-\otimes v_-,&
c(v_+\otimes v_+)&=-v_+\otimes v_+,\\
c(v_-\otimes v_+)&=-v_+\otimes v_-,&
c(v_+\otimes v_-)&=-v_-\otimes v_+.
\end{aligned}                                         \tag{8.4}
\]
The three-dimensional symmetric-tensor subspace is its minus eigenspace; the line \(\Lambda(v_-\otimes v_+-v_+\otimes v_-)\) is its plus eigenspace. Since \(\epsilon(P)=1\), (7.2) reverses both eigenvalues.

The explicit decomposition of Lesson 7 is
\[
P*P=IC_{(2,0)}\oplus IC_{(1,1)}.                       \tag{8.5}
\]
Its two simples have no maps between them, and each simple's endomorphisms are scalars, by restriction to its rank-one open orbit. Thus the exchange is scalar on each summand. Degree \(-2\) belongs to the first summand and (8.4) makes its scalar \(-1\). Its three-dimensional cohomology is consequently the symmetric-tensor subspace; the remaining one-dimensional summand has scalar \(+1\). For \(c'\), the largest IC has scalar \(+1\) and the central point IC has scalar \(-1\). The ordinary antisymmetric line is precisely the latter summand's cohomology. This computation explains the sign on actual geometric summands rather than inferring it merely from their dimensions.

## 9. Exercises with solutions

**Exercise 9.1 (easy).** Describe the two-point Grassmannian for \(\mathbb G_m\), its distinct and coincident geometric fibres, and fusion of two skyscrapers. Include the distinction between the full functor and its geometric points.

*Solution.* The objects are line bundles on the curve with a specified trivialization off the two graphs. By gluing they are projective rank-one lattices in the completed divisor's localized ring. On the affine line use (1.2) and take all symmetric \(f\)-bounds. Each bound is represented by finite Grassmannian quotients stable under the \(t\)-operator, with its scheme equations as in §1; these bounds exhaust the full functor. At distinct complex points the completion is a product of two power-series rings, and a rank-one lattice in each is a parameter power times an integral unit. The two geometric indices are therefore \((m,n)\in\mathbb Z^2\). On the diagonal the completion is one power-series ring, by cofinality of the squared-parameter filtration, and its index is a single integer. Formula (8.1) specializes that integer to \(m+n\). The lattice \((1+\eta f^{-1})\widehat A\) exhibits a nontrivial infinitesimal point, so the geometric description does not replace the full functor. For the skyscrapers the moving chain is \(\mathbb A^2\) and its normalized sheaf is \(\Lambda[2]\); diagonal restriction with \([-2]\) gives \(\delta_{m+n}\). The commutativity map is the identity because the scalar product and degree-zero tensor flip are identities. \(\square\)

**Exercise 9.2 (easy).** Compute both categorical dimensions of the minuscule \(\operatorname{PGL}_2\) IC directly from the trace.

*Solution.* Its graded cohomology has basis \(v_-,v_+\) in degrees \(-1,1\). Its graded dual has the dual basis in the opposite degrees. Coevaluation gives the sum of the two corresponding basis–dual tensors, and evaluation returns one on each after their exchange. The naive exchange contributes \((-1)^{-1}=(-1)^1=-1\) to the two terms, so the trace is \(-2\). The object is in the odd component, and the modified self-exchange multiplies both terms by another \(-1\). The trace becomes \(+2\). The strong monoidal cohomology functor carries the geometric evaluation and coevaluation to these duality maps, so these are the categorical traces. \(\square\)

**Exercise 9.3 (medium).** Compute the exchange eigenvalues on the two \(\operatorname{GL}_2\) summands in (8.5), before and after modification.

*Solution.* Both basis vectors of \(H(P)\) are odd. Thus the naive map is \(-\mathrm{flip}\). Its minus eigenspace has basis \(v_-\otimes v_-\), \(v_-\otimes v_++v_+\otimes v_-\), \(v_+\otimes v_+\); its plus eigenspace is the line generated by \(v_-\otimes v_+-v_+\otimes v_-\). The exchange is scalar on each of the two distinct simples in (8.5). The degree-minus-two vector lies in \(IC_{(2,0)}\), forcing its scalar to \(-1\); all three of that IC's cohomology vectors occupy the minus eigenspace. The point IC occupies the remaining plus line. Multiplication by the odd–odd sign \(-1\) makes their respective eigenvalues \(+1,-1\). This is the ordinary symmetric/antisymmetric decomposition of a two-dimensional vector space. \(\square\)

**Exercise 9.4 (medium).** Prove that comparable coweights have the same parity, and that this parity gives the signs in both hexagons.

*Solution.* If \(\mu\le\lambda\), then \(\lambda-\mu=\sum_i n_i\alpha_i^\vee\), with integral \(n_i\ge0\). Pairing with \(2\rho\) gives \(2\sum_i n_i\), an even integer. The same computation for arbitrary integral coroot combinations makes parity well-defined on the component quotient. Its additivity follows from the component homomorphism. For component parities \(e,f,g\), the sign for exchanging the first object with the other two is \((-1)^{e(f+g)}=(-1)^{ef}(-1)^{eg}\); the other hexagon is \((-1)^{(e+f)g}=(-1)^{eg}(-1)^{fg}\). The double exchange has exponent \(ef+fe\), hence sign one. Since the naive maps already satisfy both hexagons and involutivity, these scalar identities prove them for the modified maps. \(\square\)

**Exercise 9.5 (hard).** Prove that the fusion constraint is independent of the smooth pointed curve and formal coordinate, without assuming general IC parity or semisimplicity.

*Solution.* Choose finite bounds for the objects. The substitution estimate of §6 makes their coordinate actions factor through a finite \(\mathscr A_r\); the finite group \(J_mG\rtimes\mathscr A_r\) is connected and preserves their orbit strata. Parameter descent gives normalized local transport of the whole perverse complex. The proper action homeomorphism identifies its total cohomology system with the constant system, so every transport loop acts trivially on cohomology. Exact faithfulness from Lesson 6 makes its perverse automorphism the identity, including any possible extension automorphism. Thus transport descends to the unique coordinate-equivariant structure and its cocycle, without semisimplicity.

An étale coordinate at the chosen curve point identifies a neighbourhood with selected formal branches of the affine line. For several nearby sections exclude distinct sections with equal coordinate images. The selected section in each inverse-image graph is open and closed; removing other branches makes all divisor thickenings isomorphic to the affine-line thickenings, by the étale open-immersion criterion. This gives a comparison on completed and punctured neighbourhoods over every parameter ring. Gluing with the prescribed trivial complement compares both the endpoint and chain functors. The finite-coordinate structures compare their descended coefficient complexes. Proper base change then compares the global images, whose strict boundary bounds identify them with the same intermediate extension. Their open exchange maps agree, so uniqueness identifies their extensions, and diagonal restriction identifies the local constraint. Two choices of coordinates differ by a coordinate substitution; its proved cocycle identifies those comparisons on overlaps. Two pointed curves compare with the affine line and hence with each other. All comparisons commute with composition, since they are restriction and uniquely effective gluing. This proves the asserted independence. \(\square\)

## References

- I. Mirković and K. Vilonen, [*Geometric Langlands duality and representations of algebraic groups over commutative rings*](https://arxiv.org/abs/math/0401222v5), free corrected preprint, §§5–6 and Appendix A. The classical construction, coordinate descent and coherence used here are proved above.
- X. Zhu, [*An introduction to affine Grassmannians and the geometric Satake equivalence*](https://arxiv.org/abs/1603.05593v2), free lecture notes, the discussion of fusion and commutativity in the geometric Satake section.
