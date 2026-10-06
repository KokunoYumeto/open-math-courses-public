# Loop groups and the affine Grassmannian

*Written by GPT-6.1 Sol (OpenAI), October 2026. Public domain (CC0).*

A lattice over a field is easy to recognize. A family of lattices must also behave correctly under base change. The difference is decisive: a nilpotent parameter can move a lattice even when every ordinary point appears stationary. We will construct the affine Grassmannian by finite-dimensional Grassmannians, prove the needed projectivity for arbitrary base rings, and calculate this infinitesimal motion for a torus.

We assume the functor of points, finite projective modules, Grassmannians, and faithfully flat descent. Basic references are Zhu, *An introduction to affine Grassmannians and the geometric Satake equivalence*, §1.1–1.3, and Beauville–Laszlo, *Un lemme de descente*. Bhatt–Scholze's *Projectivity of the Witt vector affine Grassmannian*, §8–9, treats a related mixed-characteristic problem; this lesson uses ordinary power series throughout. Spherical Hecke algebras as functions on the affine Grassmannian explains why the points of the space matter.

## 1. Arcs and loops remember coefficients

Let \(k\) be an algebraically closed field. For a \(k\)-algebra \(R\), put \(O_R=R[[t]]\) and \(F_R=R[[t]][1/t]\). Thus a Laurent series has only finitely many negative coefficients. For an affine algebraic group \(G\), define

\[
L^+G(R)=G(O_R),\qquad LG(R)=G(F_R).
\]

An ind-scheme here is a filtered union of schemes with closed transition embeddings. The positive loop group is a scheme, generally not of finite type; the loop group is an ind-scheme.

**Proposition 1.1.** If \(G\) is affine of finite type over \(k\), then \(L^+G\) is an affine group scheme and \(LG\) is an ind-affine group ind-scheme.

*Proof.* Choose a closed embedding \(G\hookrightarrow\mathbb A^m\), described by polynomial equations \(f_1,\ldots,f_s\). For arcs, write each coordinate as \(x_i(t)=\sum_{j\geq0}x_{ij}t^j\). The coefficient of each power of \(t\) in each \(f_a(x_1(t),\ldots,x_m(t))\) is a polynomial in finitely many \(x_{ij}\). The quotient of \(k[x_{ij}:j\geq0]\) by all these coefficient equations represents \(L^+G\). Equivalently it is the inverse limit of the affine jet schemes

\[
G_m(R)=G(R[t]/t^m).
\]

For loops, impose a common lower bound \(-N\) on the coordinates and use the variables \(x_{ij}\), \(j\geq-N\). The same coefficient equations define an affine scheme. Increasing \(N\) gives closed embeddings by setting the new lowest coefficients to zero. Every Laurent point occurs at some bound. Group multiplication and inverse are induced by those of \(G\); each sends any fixed bounded stage into another bounded stage because its coordinate functions are polynomials. They therefore define the asserted group structure on the ind-scheme. ∎

For \(G=GL_n\), use matrix entries and an extra coordinate \(u\) with \(u\det A=1\). Bounding both the entries and \(u\) is essential: an invertible Laurent matrix can have a determinant whose inverse has a larger pole than its entries.

## 2. What a lattice family is

A lattice in \(F_R^n\) is a finite projective \(O_R\)-submodule \(\Lambda\) whose localization at \(t\) is all of \(F_R^n\). Necessarily, for some \(N\),

\[
t^NO_R^n\subset\Lambda\subset t^{-N}O_R^n.
\tag{2.1}
\]

Indeed a finite set of generators gives the upper bound, and expressions for each standard basis vector in the localized module give the lower bound. The integer \(N\) can be chosen simultaneously for all generators and basis vectors.

To encode (2.1), define

\[
V_N=t^{-N}O_R^n/t^NO_R^n\simeq R^{2Nn}.
\]

Multiplication by \(t\) induces a fixed nilpotent operator \(\Phi\) on this module. A putative lattice determines \(W=\Lambda/t^NO_R^n\subset V_N\), or equivalently the quotient \(Q=V_N/W\). A point of an ordinary Grassmannian requires \(Q\) to be a finite projective \(R\)-module. We must prove that this condition is exactly the right one.

**Lemma 2.1 (finite quotients).** If \(\Lambda\) is a lattice satisfying (2.1), then \(Q=t^{-N}O_R^n/\Lambda\) is finite projective over \(R\). Conversely, if a quotient \(V_N\twoheadrightarrow Q\) is finite projective over \(R\) and respects multiplication by \(t\), then its inverse-image kernel in \(t^{-N}O_R^n\) is a lattice.

*Proof of the first direction.* Since \(\Lambda\) is finite projective, \(\Lambda/t\Lambda\) is finite projective over \(R\). The filtration of \(F_R^n/\Lambda\) by \(t^{-j}\Lambda/\Lambda\) has successive quotients isomorphic to \(\Lambda/t\Lambda\). Its short exact sequences split over \(R\), so its union is \(R\)-projective, a direct sum of those quotients after choosing splittings. The same argument for the standard lattice shows that \(F_R^n/t^{-N}O_R^n\) is \(R\)-projective. Hence the exact sequence

\[
0\longrightarrow Q\longrightarrow F_R^n/\Lambda
\longrightarrow F_R^n/t^{-N}O_R^n\longrightarrow0
\]

splits over \(R\). Thus \(Q\) is projective. It is finite because it is a quotient of \(V_N\).

*Proof of the converse.* Regard \(Q\) as an \(R[t]\)-module on which \(t\) acts by a nilpotent endomorphism \(\Phi_Q\), with \(\Phi_Q^{2N}=0\). Put \(P=R[t]\otimes_RQ\), a finite projective \(R[t]\)-module. There is a projective resolution

\[
0\longrightarrow P\xrightarrow{t-\Phi_Q}P\longrightarrow Q\longrightarrow0.
\tag{2.2}
\]

The last map sends \(t^j\otimes q\) to \(\Phi_Q^jq\). The first map is injective by comparing the highest nonzero coefficient of a polynomial. Division by the monic operator \(t-\Phi_Q\) proves exactness in the middle.

Let \(M\) be the kernel of \(t^{-N}R[t]^n\twoheadrightarrow Q\). Comparing this presentation with (2.2), Schanuel's lemma gives

\[
M\oplus P\simeq t^{-N}R[t]^n\oplus P.
\]

Therefore \(M\) is finite projective over \(R[t]\). Tensor (2.2) with \(R[[t]]\). The operator \(t-\Phi_Q\) is still injective: if the coefficients of a formal series \(p\) satisfy \(p_{j-1}=\Phi_Qp_j\), nilpotence implies \(p_j=\Phi_Q^{2N}p_{j+2N}=0\). Its cokernel is still \(Q\), since evaluation at the nilpotent \(\Phi_Q\) is a finite sum. Consequently the tensor of the kernel sequence for \(M\) remains exact. Its kernel is precisely

\[
\Lambda=M\otimes_{R[t]}R[[t]].
\]

This is finite projective over \(O_R\), and its localization is \(F_R^n\), since \(t^{2N}Q=0\). This proves the converse without assuming that \(R\) is noetherian or that an arbitrary completion map is flat. ∎

## 3. The projective stages

**Theorem 3.1.** The lattice functor is represented by an ind-projective ind-scheme \(\operatorname{Gr}_{GL_n}\).

*Proof.* Take the disjoint union of the ordinary quotient Grassmannians of \(V_N\simeq k^{2Nn}\), one for each possible rank of \(Q\). Let \(\mathcal W\) and \(\mathcal Q\) be the universal kernel and quotient. The condition \(\Phi(\mathcal W)\subset\mathcal W\) is the vanishing of

\[
\mathcal W\hookrightarrow V_N\xrightarrow{\Phi}V_N\twoheadrightarrow\mathcal Q.
\]

It is therefore closed. By Lemma 2.1 the resulting projective scheme \(Z_N\) represents exactly the lattices satisfying (2.1). The transition \(Z_N\to Z_{N+1}\) imposes the further inclusions \(t^NO_R^n\subset\Lambda\subset t^{-N}O_R^n\) in the larger finite quotient. Both are closed incidence conditions, so this is a closed embedding. Every lattice is bounded, and the union of the \(Z_N\) represents the entire functor. ∎

The \(Z_N\) need not be reduced. Replacing them by reduced varieties preserves their geometric points but changes the functor on rings with nilpotents.

For \(n=2,N=1\), the module \(V_1\) has basis \(t^{-1}e_1,t^{-1}e_2,e_1,e_2\), and \(\Phi\) sends the first two vectors to the last two and kills the last two. Bounded lattices correspond to \(\Phi\)-stable subspaces, with the corresponding incidence equations for families. For example, lattices \(tO^2\subset\Lambda\subset O^2\) with quotient rank one correspond to lines in \(k^2\); they form \(\mathbb P^1\) and have elementary divisors \((1,0)\).

## 4. Why the sheaf quotient gives the same space

The ordinary quotient set \(LG(R)/L^+G(R)\) can miss lattices over \(R\), because a finite projective lattice need not have a global basis. The affine Grassmannian uses its étale sheafification.

**Lemma 4.1 (trivializing on the disc).** A torsor under a smooth affine algebraic group \(G\) on \(\operatorname{Spec}R[[t]]\) becomes trivial after an étale covering of \(\operatorname{Spec}R\).

*Proof.* Its restriction at \(t=0\) is a smooth \(G\)-torsor over \(R\), so it has a section étale locally. After that base change, lift the section successively over \(R[t]/t^m\). Smoothness supplies local lifts; their differences form the vector bundle obtained from \(\operatorname{Lie}G\otimes(t^m/t^{m+1})\). Its first cohomology on an affine base is zero, so these lifts join to a global lift. The compatible sections give a section over \(R[[t]]\), since an affine scheme of finite presentation is determined on this complete ring by its values modulo all powers of \(t\). ∎

**Proposition 4.2.** For \(GL_n\), the étale sheaf quotient \(LG/L^+G\) is the lattice functor.

*Proof.* Send \(g\) to \(gO_R^n\). Right multiplication by \(GL_n(O_R)\) leaves this lattice fixed. Its fibre is the sheaf of bases of the lattice, an \(L^+GL_n\)-torsor. Lemma 4.1 supplies bases étale locally, and two bases differ by exactly one element of \(L^+GL_n\). Lattices and their inclusions descend: one can use the projective quotient \(Q\) in Lemma 2.1 and its finite-dimensional Grassmannian description. Hence the lattice functor is already a sheaf and has precisely this local quotient presentation. ∎

The same argument proves that \(L^+G\)-torsors on affine \(k\)-schemes are étale locally trivial when \(G\) is smooth. Work with the compatible finite jet quotients of the torsor. The kernel of \(G_{m+1}\to G_m\) is the additive group of \(\operatorname{Lie}G\otimes t^m/t^{m+1}\). After trivializing the level-one torsor, the successive vector-group torsors lift that trivialization on the affine base. The inverse limit recovers the original torsor, as is checked after a faithfully flat cover on which it is trivial.

### Faithful representations and the affine-quotient bridge

There are two different assertions to establish. An affine algebraic group has a faithful closed representation. The homogeneous quotient for a chosen representation need not be affine. We prove the first assertion and the complete implication from the second assertion to ind-projectivity, then give a direct proof for general reductive groups in §7.

**Proposition 4.3 (a faithful closed representation).** Every affine group scheme \(G\) of finite type over a field has a finite-dimensional representation \(\rho:G\hookrightarrow GL(V)\) that is a closed immersion. No smoothness or characteristic assumption is needed.

*Proof.* Write \(A=k[G]\), with comultiplication \(\Delta\) and counit \(\varepsilon\). Every \(f\in A\) lies in a finite-dimensional subspace \(W_f\) with \(\Delta(W_f)\subset W_f\otimes A\). Indeed, write

\[
\Delta(f)=\sum_{i=1}^{r}a_i\otimes b_i
\]

with the \(b_i\) linearly independent, and let \(W_f\) be the span of the \(a_i\). Applying the counit to the second factor puts \(f\) in \(W_f\). Coassociativity gives

\[
\sum_i\Delta(a_i)\otimes b_i
=\sum_i a_i\otimes\Delta(b_i).
\]

Project the first tensor factor to \(A/W_f\). The right side vanishes; linear independence of the \(b_i\) makes each \(\Delta(a_i)\) belong to \(W_f\otimes A\).

Choose finitely many algebra generators of \(A\), and let \(V\) be the sum of their spaces \(W_f\). In a basis \(v_1,\ldots,v_d\), write

\[
\Delta(v_j)=\sum_i v_i\otimes c_{ij}.
\]

The coalgebra identities say
\(\Delta(c_{ij})=\sum_l c_{il}\otimes c_{lj}\) and
\(\varepsilon(c_{ij})=\delta_{ij}\). The antipode provides the inverse of the matrix \((c_{ij})\). Thus these entries give a representation on \(V\). Applying the counit to the first factor gives

\[
v_j=\sum_i\varepsilon(v_i)c_{ij}.
\]

Consequently the matrix coefficients generate \(A\) as an algebra, because \(V\) contains the chosen algebra generators. The induced map
\(k[GL_d]\to A\) is surjective, which is precisely the affine criterion for a closed immersion. ∎

For a smooth affine \(G\), write \(\operatorname{Gr}_G\) for the sheaf of pairs \((P,\beta)\), where \(P\) is a \(G\)-torsor on \(\operatorname{Spec}O_R\) and
\(\beta:P|_{\operatorname{Spec}F_R}\simeq G_{F_R}\) is a trivialization. Lemma 4.1 identifies this sheaf with the étale sheafification of \(LG/L^+G\): a disc trivialization supplies a loop, and changing that trivialization multiplies the loop on the right by an arc. Isomorphisms between two such pairs are required to respect \(\beta\). A disc automorphism that is the identity after inverting \(t\) is the identity, since \(O_R\to F_R\) is injective; hence this is a sheaf of sets.

**Lemma 4.4 (extending an affine section).** Let \(Y\to\operatorname{Spec}O_R\) be affine of finite presentation, and let \(s\) be a section over \(\operatorname{Spec}F_R\). The functor on \(R\)-algebras that asks whether the coefficientwise base change of \(s\) extends to a section over \(\operatorname{Spec}R'[[t]]\) is represented by a closed subscheme of \(\operatorname{Spec}R\). When the extension exists, it is unique.

*Proof.* Choose a presentation

\[
Y=\operatorname{Spec}
O_R[x_1,\ldots,x_a]/(f_1,\ldots,f_b).
\]

The section is given by Laurent series
\(s_i(t)=\sum_{j\geq-M_i}s_{ij}t^j\). Let \(I\subset R\) be the ideal generated by all \(s_{ij}\) with \(j<0\). There are only finitely many such coefficients. For a map \(R\to R'\), the series \(s_i\) lie in \(R'[[t]]\) exactly when that map kills \(I\). Their values then satisfy the equations \(f_l\): evaluation in \(R'[[t]]\) becomes zero after inverting \(t\), and multiplication by \(t\) is injective on every power-series ring, including a ring with nilpotents. Thus they define an extension. Conversely every extension must have these coordinates, by the same injectivity, and therefore kills \(I\). The representing scheme is \(\operatorname{Spec}(R/I)\).

All base changes here use the coefficientwise homomorphism
\(R[[t]]\to R'[[t]]\). The proof does not identify the latter ring with \(R'\otimes_R R[[t]]\), an identification that is generally false. ∎

**Theorem 4.5 (the affine-quotient implication).** Let \(G\) be a smooth affine algebraic group over \(k\), and let \(\rho:G\hookrightarrow H=GL(V)\) be a closed immersion. Suppose the fppf quotient \(X=H/G\) is represented by an affine \(k\)-scheme of finite presentation. Then

\[
\operatorname{Gr}_G\longrightarrow\operatorname{Gr}_H
\]

is represented by closed immersions, and \(\operatorname{Gr}_G\) is an ind-projective ind-scheme.

*Proof.* First justify the interpretation of a reduction. Since \(X\) is the fppf quotient, \(H\to X\) has sections fppf locally on the target. Two such sections with the same image differ by a unique element of \(G\); this statement is local by the quotient definition, and uniqueness descends since \(G\hookrightarrow H\) is a monomorphism. Thus

\[
H\times G\simeq H\times_XH,
\]

and \(H\to X\) is a \(G\)-torsor. In particular it is smooth and surjective.

For an \(H\)-torsor \(E\) on \(\operatorname{Spec}O_R\), form
\(Y=E\times^H X\). On an fppf cover trivializing \(E\), this is the affine scheme \(X\) over that cover; the transition maps are the left \(H\)-action on \(X\). Faithfully flat descent for affine schemes and finite presentation therefore makes \(Y\to\operatorname{Spec}O_R\) affine of finite presentation. A section \(s\) of \(Y\) pulls back \(E\to Y\) to a \(G\)-torsor \(P\), and its extension of structure group is \(E\). Conversely a reduction \(P\subset E\) supplies this section. These constructions are inverse, as can be checked on the same trivializing cover.

Now fix a pair \((E,\beta)\) representing a map
\(\operatorname{Spec}R\to\operatorname{Gr}_H\). On the punctured disc, \(\beta\) identifies \(E\) with the trivial \(H\)-torsor. The identity coset \(G\in H/G\) supplies a section \(s_\beta\) of \(Y\) there. A lift of \((E,\beta)\) to \(\operatorname{Gr}_G\) is exactly an extension of \(s_\beta\) over the disc. The section gives the reduction, and over the punctured disc its pullback is the standard \(G\)-torsor, with the required trivialization. Lemma 4.4 represents these extensions by a closed subscheme of \(\operatorname{Spec}R\), and proves uniqueness. Hence the asserted map is represented by closed immersions on every affine test scheme. Uniqueness identifies these ideals on overlaps, so the same conclusion holds for all scheme tests.

Let \(Z_N\) be the projective lattice stages of Theorem 3.1 for \(H\). Set

\[
Y_N=Z_N\times_{\operatorname{Gr}_H}\operatorname{Gr}_G.
\]

Each \(Y_N\) is a closed subscheme of \(Z_N\), hence projective over \(k\). The transition maps are closed immersions, since they are the base changes of \(Z_N\hookrightarrow Z_{N+1}\). Every pair in \(\operatorname{Gr}_G(R)\) has an associated finite projective \(O_R\)-lattice in \(F_R\otimes_kV\), bounded by one \(N\) as in (2.1). It therefore belongs to \(Y_N(R)\). It follows that \(\operatorname{Gr}_G=\varinjlim_NY_N\) as a sheaf. This constructs the ind-projective representing ind-scheme with its full functor on arbitrary \(k\)-algebras. ∎

**Proposition 4.6 (special linear groups, in every characteristic).** The standard embedding \(SL_n\hookrightarrow GL_n\) has affine quotient \(\mathbb G_m\). Thus \(\operatorname{Gr}_{SL_n}\) is ind-projective over every field.

*Proof.* The determinant has kernel \(SL_n\) and the section
\(u\mapsto\operatorname{diag}(u,1,\ldots,1)\). More explicitly, the scheme map

\[
\mathbb G_m\times SL_n\longrightarrow GL_n,\qquad
(u,h)\longmapsto\operatorname{diag}(u,1,\ldots,1)h
\]

has inverse
\(g\mapsto(\det g,\operatorname{diag}((\det g)^{-1},1,\ldots,1)g)\).
It identifies determinant fibres with right \(SL_n\)-torsors on all test rings, so determinant represents the fppf quotient. To verify the smoothness hypothesis of Theorem 4.5, on the open where the upper-left \((n-1)\)-minor is invertible, the equation \(\det g=1\) solves uniquely for the bottom-right entry. This gives an open affine-space chart with \(n^2-1\) parameters near the identity. Over an algebraic closure, translation provides such a smooth neighbourhood at every closed point. The complement of the smooth locus, if nonempty, would have a closed point, so is empty. Smoothness descends through the field extension. The case \(n=1\) is the trivial group. Theorem 4.5 now applies. ∎

**Proposition 4.7 (symplectic groups, including characteristic two).** Let \(V=k^{2n}\), and let \(J\) be the matrix of the standard alternating form. The quotient \(GL_{2n}/Sp_{2n}\) is the affine scheme of nondegenerate alternating forms on \(V\). Consequently \(\operatorname{Gr}_{Sp_{2n}}\) is ind-projective in every characteristic.

*Proof.* An alternating form over an arbitrary \(k\)-algebra \(R\) has a matrix \(B\) with \(B_{ii}=0\) and \(B_{ji}=-B_{ij}\). These conditions mean \(b(v,v)=0\) for every vector, also in characteristic two. The scheme of such forms is the affine space with coordinates \(B_{ij}\), \(i<j\); its nondegenerate locus is the principal affine open \(\det B\ne0\). Define

\[
q:GL_{2n}\longrightarrow X,\qquad q(g)=g^{-\mathsf T}Jg^{-1}.
\]

This is constant on right \(Sp_{2n}\)-cosets, and two matrices have the same image exactly when their quotient lies in \(Sp_{2n}\).

Every nondegenerate alternating form admits a symplectic basis Zariski locally. To prove this, work over a local ring. An invertible matrix has an entry that is a unit. A diagonal entry of \(B\) is zero, so choose distinct basis vectors \(p,q\) with \(b(p,q)\) a unit, and rescale \(q\) to make \(b(p,q)=1\). The span of \(p,q\) is a direct summand. For any \(x\),

\[
x'=x-b(x,q)p+b(x,p)q
\]

is perpendicular to both \(p\) and \(q\), and this formula splits \(V_R\) into their span and its perpendicular complement. The complement is finite projective, and the restricted form on it is nondegenerate: a vector in its radical is perpendicular to the whole module and therefore zero. Over the local ring the complement is free. Induction constructs a symplectic basis. The choices use finitely many unit inversions and matrix entries, so they extend to a Zariski neighbourhood of each prime of \(R\).

Thus \(q\) has sections Zariski locally on every scheme test of \(X\), and the equality of its fibres with the right cosets identifies \(X\) with the fppf quotient. Its affine presentation was explicit.

Here is also the smoothness check required in Theorem 4.5. Use
\(J=\begin{pmatrix}0&I\\-I&0\end{pmatrix}\), and consider a symplectic matrix with upper-left block \(A\) invertible. It has the unique factorization

\[
\begin{pmatrix}I&0\\S&I\end{pmatrix}
\begin{pmatrix}A&0\\0&A^{-\mathsf T}\end{pmatrix}
\begin{pmatrix}I&T\\0&I\end{pmatrix},
\qquad S=S^{\mathsf T},\quad T=T^{\mathsf T}.
\]

Indeed each displayed factor preserves \(J\). Conversely the equations
\(g^{\mathsf T}Jg=J\) give
\(S=CA^{-1}\) and \(T=A^{-1}B\) symmetric and
\(D=SAT+A^{-\mathsf T}\), where \(B,C,D\) are the other blocks. These identities hold over every ring, including characteristic two. This open neighbourhood of the identity is
\(GL_n\times\operatorname{Sym}_n\times\operatorname{Sym}_n\), a smooth scheme. Translation over an algebraic closure and descent, as in Proposition 4.6, prove that \(Sp_{2n}\) is smooth. Applying Theorem 4.5 proves the conclusion. For \(n=0\) both groups are trivial. ∎

**Proposition 4.8 (split tori, in every characteristic).** For the diagonal embedding \(T=(\mathbb G_m)^r\hookrightarrow GL_r\), the fppf quotient \(GL_r/T\) is affine. Hence \(\operatorname{Gr}_T\) is ind-projective.

*Proof.* For \(r>0\), the quotient parameterizes ordered lines
\((L_1,\ldots,L_r)\) in \(k^r\) whose direct sum is \(k^r\). In families a line is a rank-one direct summand, and the direct-sum map must be an isomorphism. These conditions define the determinant-nonvanishing open \(D\) in
\((\mathbb P^{r-1})^r\). Sending a matrix to its column lines gives \(GL_r\to D\). Local generators of the line bundles give sections on a Zariski cover, and changing the generators multiplies the matrix on the right by a unique diagonal unit matrix. Thus \(D\) represents the fppf quotient on arbitrary test rings.

To check affineness, use the Segre coordinates
\(z_{i_1\cdots i_r}=x_{i_1,1}\cdots x_{i_r,r}\). They realize the product of projective spaces as a closed subscheme of one projective space. One can verify this directly: the equations that exchange an index between two factors are the two-by-two flattening minors; on a chart \(z_{a_1\cdots a_r}\ne0\), they express every normalized coordinate as the product of the coordinates in which just one index differs from \((a_1,\ldots,a_r)\). These are precisely the usual affine charts of the product, and the chart inverses agree. This proves the claimed closed Segre realization as a scheme.

The determinant is the linear form

\[
\sum_{\sigma\in S_r}\operatorname{sgn}(\sigma)
z_{\sigma(1)\cdots\sigma(r)}
\]

in that projective space. Its nonvanishing locus is an affine-space chart after a linear change of coordinates. The scheme \(D\) is closed in this affine chart, hence affine. Theorem 4.5 applies. For \(r=0\) the torus is trivial and its Grassmannian is a point. ∎

For a general reductive group, the construction in §7 proves ind-projectivity using an equivariant quasi-affine homogeneous quotient and rank-one projective schemes. The stronger assertion that a suitable homogeneous quotient is affine is not needed for that construction.

## 5. A torus moves infinitesimally

Let \(R=k[\epsilon]/(\epsilon^2)\). Reduction of a Laurent unit gives \(t^m u_0(t)\), where \(m\in\mathbb Z\) and \(u_0\in k[[t]]^\times\). Divide by a lift of \(u_0\); the remaining series is \(t^m(1+\epsilon h(t))\). A power-series unit removes the nonnegative powers of \(h\). Every coset therefore has a unique representative

\[
t^m\left(1+\epsilon\sum_{j=1}^{M}a_jt^{-j}\right),
\qquad m\in\mathbb Z,
\tag{5.1}
\]

where only finitely many \(a_j\in k\) are nonzero. Uniqueness follows by reducing a quotient modulo \(\epsilon\), then comparing negative coefficients. At a fixed \(m\), multiplication adds the negative polynomials since \(\epsilon^2=0\).

In particular \(1+\epsilon t^{-1}\) gives a nonconstant infinitesimal lattice at \(O_R\). Its inverse is \(1-\epsilon t^{-1}\) in \(F_R\), but it is not a power-series unit.

This motion is visible in the smallest bounded stage. In \(V_1=t^{-1}O_R/tO_R\), write a line near \(R\cdot1\) as \(R(1+a t^{-1})\). Stability under multiplication by \(t\) requires

\[
a=a(1+a t^{-1}),\qquad\text{hence }a^2=0.
\]

The chart is \(\operatorname{Spec}k[a]/(a^2)\), visibly nonreduced.

**Proposition 5.1.** \(\operatorname{Gr}_{\mathbb G_m}\) is nonreduced, and its reduced ind-scheme is the discrete set \(\mathbb Z\).

*Proof.* Over any field extension of \(k\), a Laurent unit is \(t^m\) times a power-series unit. Thus a bounded rank-one stage \(Z_N\) has exactly the finitely many geometric points \(m=-N,\ldots,N\). Its reduction is a finite reduced \(k\)-scheme with those points, hence a disjoint union of copies of \(\operatorname{Spec}k\). The transition inclusions produce the discrete reduced ind-scheme indexed by all integers. The class \(1+\epsilon t^{-1}\) does not factor through that reduction: over the local ring of dual numbers any map to this discrete scheme is constant, whereas this class differs from \(1\) modulo \(L^+\mathbb G_m\), at every larger bounded stage as well. Hence the full ind-scheme is nonreduced. The chart above displays the motion concretely. ∎

Constructible sheaves in the theories used later are insensitive to these nilpotent thickenings. The moduli functor is not. This explains why a torus has a simple Satake category although its full affine Grassmannian is not discrete and reduced.

## 6. Exercises with solutions

**Exercise 6.1 (easy).** Describe \(\operatorname{Gr}_{\mathbb G_m}(k[\epsilon]/\epsilon^2)\) and its tangent space at \(t^m\).

*Solution.* Formula (5.1) is a disjoint union, indexed by \(m\), of the vector space \(t^{-1}k[t^{-1}]\). The tangent space at every \(t^m\) is \(k((t))/k[[t]]=t^{-1}k[t^{-1}]\). It is infinite-dimensional, although the reduced space has isolated points. ∎

**Exercise 6.2 (easy).** Describe lattices \(tO^n\subset\Lambda\subset O^n\).

*Solution.* Reduction gives a subspace \(W=\Lambda/tO^n\subset k^n\); inverse image is the inverse construction. If \(\dim W=r\), the parameter space is \(\operatorname{Gr}(r,n)\). In families require \(W\) and \(k^n/W\) to be locally free over the base. No further stability equation is needed, since \(t\) is zero on \(O^n/tO^n\). ∎

**Exercise 6.3 (medium).** Give closed equations for bounded lattice families and explain why their solutions really are lattices.

*Solution.* On the quotient Grassmannian of \(V_N\), set the map \(\mathcal W\to\mathcal Q\) induced by \(\Phi\) equal to zero. Its vanishing makes \(Q\) an \(R[t]\)-module. Nilpotence gives resolution (2.2); Schanuel's lemma makes the kernel of \(t^{-N}R[t]^n\to Q\) finite projective, and extension to formal series produces the lattice. The Grassmannian condition supplies the required flatness in families. ∎

**Exercise 6.4 (medium).** Prove étale local triviality of an \(L^+G\)-torsor for smooth affine \(G\).

*Solution.* Quotient by the congruence kernels to obtain compatible \(G_m\)-torsors. At level one smoothness gives a section on an étale covering. Each lift is a torsor under the twisted Lie algebra, a vector bundle on that affine covering. Its first cohomology vanishes, so choose compatible sections at all levels. Their limit is an \(L^+G\)-section. Effectivity and its identification with the original torsor can be tested after a faithfully flat trivializing cover, where both assertions reduce to \(G(R[[t]])=\lim_mG(R[t]/t^m)\). ∎

**Exercise 6.5 (hard).** Prove that the étale sheafification of \(LGL_n/L^+GL_n\) is the lattice functor, including lattices without global bases.

*Solution.* A finite projective lattice has a frame torsor on the formal disc. Its reduction at \(t=0\) has a basis locally on the base; Lemma 4.1 lifts it to a formal basis. Localization makes the basis an invertible Laurent matrix. Two choices differ by a power-series invertible matrix. Conversely a cocycle of such matrices descends a finite projective disc module with its punctured-disc identification. Lemma 2.1's bounded quotient description verifies that it is a lattice and that the construction commutes with base change. The constructions are inverse on an étale cover and hence inverse as sheaves. ∎

## 7. General reductive groups

Let \(G\) be connected reductive over the algebraically closed field \(k\). The affine-quotient implication in §4 gives a short proof in several matrix cases. We now construct finite projective stages for every such \(G\), in every characteristic.

**Theorem 7.1 (general ind-projectivity).** The full torsor-and-trivialization sheaf \(\operatorname{Gr}_G\) is represented by an ind-projective ind-scheme. There is a faithful closed representation \(G\hookrightarrow H=GL(V)\) for which \(\operatorname{Gr}_G\to\operatorname{Gr}_H\) is a closed immersion of ind-schemes.

The proof has two parts. First, an equivariant affine hull constructs the bounded moduli schemes as locally closed subschemes of lattice Grassmannians. Second, projective rank-one constructions show that their supports are closed; this makes those same schemes closed, with their nilpotents retained.

We use the ordered affine-root coordinates, reflection geometry and Cartan decomposition proved in Spherical Hecke algebras as functions on the affine Grassmannian, Theorem 2.C. The root groups, rank-one centralizer and \(SL_2\) homomorphisms are proved in Roots and reductive groups of rank one, §§1–3 and Theorem 7.1. Their polynomial commutators are proved in Root data, Weyl chambers and the Bruhat decomposition, §5. These identities hold on arbitrary test algebras.

For the algebraic quotient step, Flat quotient bootstrap over an arbitrary base, Theorem 8.2 and Corollary 8.3, proves the flat quotient and torsor as algebraic spaces. The scheme-neighbourhood argument in Quotients and torsors, Theorem 11.1b, makes a homogeneous quotient over a field a finite-type scheme. Theorem 7.13 of Group schemes over a field, with its generic immersion Lemma 7.12, then identifies a schematic orbit with an open subscheme of its affine schematic closure. We use precisely these proved steps below.

### 7.1. An equivariant affine hull of a quasi-affine homogeneous quotient

We first establish representability by locally closed finite stages. This step applies to any smooth affine finite-type group over \(k\).

**Lemma 7.2.** There is a faithful closed embedding \(G\hookrightarrow H=GL(V)\) such that \(X=H/G\) is an \(H\)-stable open subscheme of an affine finite-type \(H\)-scheme \(A\).

*Proof.* Choose a closed embedding \(G\subset GL_d\), and let \(\mathfrak a\subset k[GL_d]\) be its ideal. Put finitely many ideal generators into a finite-dimensional subspace \(W_0\) stable under the right regular \(GL_d\)-action, using the coefficient-coalgebra argument of Proposition 4.3. Let \(W_1=\mathfrak a\cap W_0\). It contains the chosen generators. A matrix stabilizes \(W_1\) exactly when its right translation preserves \(\mathfrak a\), which is exactly the condition of belonging to \(G\). These assertions hold after tensoring with every \(k\)-algebra: vector-space intersections commute with this tensoring, and the ideal-generation condition remains true. The Plücker immersion identifies the stabilizer of \(W_1\) with that of the line

\[
L=\bigwedge^{\dim W_1}W_1
\subset W=\bigwedge^{\dim W_1}W_0.
\]

Choose \(0\ne w\in L\). Its scalar action on \(G\) gives a character \(\chi:G\to\mathbb G_m\). In \(H_0=GL_d\times\mathbb G_m\), embed \(G\) by \(g\mapsto(g,\chi(g))\), and let \((h,z)\) act on \(W\) by \(z^{-1}h\). The schematic stabilizer of the vector \(w\) is precisely this graph: fixing \(w\) first forces \(h\) to preserve \(L\), hence to lie in \(G\), and then forces \(z=\chi(h)\).

By the schematic orbit theorem, Theorem 7.13 of Group schemes over a field, \(O=H_0/G\) is an open subscheme of its affine schematic orbit closure \(C\subset W\). The action preserves \(C\) and \(O\) schematically. In particular the orbit map \(H_0\to O\) is its actual fppf \(G\)-torsor.

Embed \(H_0\) block diagonally in \(H=GL_{d+1}\). Its quotient is the affine scheme \(D\) of idempotents of rank \(d\) in \(\operatorname{End}(k^{d+1})\). Here is a scheme proof. An idempotent splits the trivial module into its image and kernel, both finite projective. Their ranks are locally constant. Each rank stratum is closed: its characteristic polynomial is exactly \(X^{d+1-r}(X-1)^r\), an identity checked after choosing local bases of the summands. Conversely this characteristic-polynomial identity forces rank \(r\) at every prime, since the factors \(X\) and \(X-1\) are distinct over every residue field. Thus these finitely many rank strata are also open. The rank-\(d\) stratum is affine of finite presentation. Local bases of image and kernel supply Zariski-local lifts to \(H\), and two such bases differ by \(H_0\). Hence \(H\to D\) is an \(H_0\)-torsor and \(D=H/H_0\) on all scheme tests.

Descend \(W\) through this torsor. The associated vector bundle \(E=H\times^{H_0}W\) is affine over affine \(D\), and therefore affine over \(k\). Descending the invariant closed ideal of \(C\) gives the affine finite-type closed subscheme

\[
A=H\times^{H_0}C\subset E.
\]

Descending its invariant open \(O\) gives

\[
X=H\times^{H_0}O\subset A.
\]

The map \(H\to X\), \(h\mapsto[h,w]\), is an fppf \(G\)-torsor: after trivializing \(H\to D\), this is the already proved torsor \(H_0\to O\). Thus \(X\) represents \(H/G\). Left multiplication by \(H\) preserves the displayed affine hull and its open subscheme. The graph embedding of \(G\) in \(H_0\), followed by its block embedding in \(H\), is closed and faithful. ∎

No finite-generation statement about \(k[H]^G\) or about all global sections of \(X\) is used in this construction.

**Lemma 7.3.** For this embedding, \(\operatorname{Gr}_G\to\operatorname{Gr}_H\) is represented by locally closed immersions. For the projective lattice stages \(Z_N\) of \(\operatorname{Gr}_H\), the fibre products

\[
Y_N=Z_N\times_{\operatorname{Gr}_H}\operatorname{Gr}_G
\]

are finite-type locally closed schemes, and their union is the full sheaf \(\operatorname{Gr}_G\).

*Proof.* Take an \(H\)-torsor \(\mathcal E\) on \(\operatorname{Spec}O_R\), with its punctured-disc trivialization \(\beta\). Its reductions to \(G\) are sections of \(\mathcal E\times^H X\), by the torsor/section inverse constructions in Theorem 4.5. This scheme is open in \(\mathcal E\times^H A\), which is affine of finite presentation by affine descent. The identity coset and \(\beta\) supply a specified section on the punctured disc.

Lemma 4.4 represents extensions to that affine hull by a closed subscheme \(S\subset\operatorname{Spec}R\). The extension is unique. Its reduction modulo \(t\) supplies a map from \(S\) to the closed-disc fibre of the hull. Let \(U\subset S\) be the inverse image of the open homogeneous-quotient bundle under this map. We claim that \(U\) represents extensions to the homogeneous quotient itself.

Indeed, after any coefficientwise base change to \(R'\), the closed complement pulls back under the extended section to a closed subset \(V(J)\) of \(\operatorname{Spec}R'[[t]]\). If the section at \(t=0\) misses that complement, then \(J+(t)=R'[[t]]\). Write \(1=j+tb\). The element \(j=1-tb\) is a unit, with inverse given by its formal geometric series. Thus \(J\) is the unit ideal and the whole disc misses the complement. The converse follows by restricting a disc section to \(t=0\). This proves the claim on arbitrary rings, including rings with nilpotents.

Thus the fibre of \(\operatorname{Gr}_G\to\operatorname{Gr}_H\) is open in a closed subscheme on every affine test. Uniqueness identifies the local representing schemes on overlaps. Each \(Y_N\) is consequently locally closed in \(Z_N\); since \(Z_N\) is Noetherian of finite type, so is \(Y_N\). Its transition maps are closed immersions, being base changes of those between the \(Z_N\).

Every \(G\)-pair over \(R\) has an associated finite projective \(O_R\)-lattice in \(F_R\otimes V\). Its finite generators and expressions for the standard basis after localization give one common bound \(N\), as in (2.1). It therefore defines a point of \(Y_N(R)\). Conversely these fibre products represent exactly those pairs. This proves the union assertion with the complete functor, rather than only its geometric points. ∎

### 7.2. The affine wall and its schematic kernel

Affine wall reflections supply the rank-one projective quotients used in the compactification. A positive real affine root is \(b=\beta+m\delta\), where \(m\ge r(\beta)\), with \(r(\beta)=0\) for a positive finite root and \(r(\beta)=1\) for a negative one. Here \(\delta\) is the constant affine function one. Its one-coefficient root group is

\[
x_b(c)=u_\beta(ct^m).
\]

Let \(a=\alpha+n\delta\) be the positive root of a wall of the fundamental alcove, and let \(F\) be the relative interior of that wall. Then \(n=r(\alpha)\). Indeed all positive finite roots have values strictly between zero and one on the alcove; a positive affine root of higher level has strictly positive value on its closure and cannot cut out a wall.

**Wall sign observation.** Every positive real affine root \(b\ne a\) is strictly positive on \(F\). Any real affine root

\[
c=jb-ia,\qquad i,j>0,
\]

is therefore positive and different from \(a\): on \(F\) it has value \(j b>0\), whereas \(a\) has value zero. The sign of any real root is constant on the alcove. Also \(-a+\ell\delta\) is positive and different from \(a\) for every \(\ell\ge1\). This argument uses a face of the actual affine-root hyperplane arrangement, so it does not assume a classification of affine Dynkin diagrams or a list of highest roots.

The integral big-cell test of the preceding spherical lesson, Theorem 2.C, applied over \(R[[t]]\), gives a unique ordered factorization of \(I(R)\) into the finite negative-root factors with parameters in \(tR[[t]]\), a torus arc, and the positive-root factors with parameters in \(R[[t]]\). It applies on every ring: the big-cell defining function reduces on \(B\) to a unit torus character, and \(t\) is in the Jacobson radical of \(R[[t]]\). Put the torus factor last, rescaling the positive-root parameters as necessary.

Let \(\tau_0\in T(R)\) be the constant term of this torus factor. Let \(c_a\in R\) be the coefficient of \(t^n\) of the \(\alpha\)-root factor in this torus-last order. Define

\[
\pi_a:I\longrightarrow B_{PGL_2},\qquad
\pi_a(i)=\overline{x(c_a)\operatorname{diag}(\alpha(\tau_0),1)}.
\tag{7.1}
\]

Here \(x(c)=\begin{pmatrix}1&c\\0&1\end{pmatrix}\), and the overline means its projective matrix class.

**Lemma 7.4.** Formula (7.1) is a morphism of group schemes, is fppf surjective, and its schematic kernel \(J_a\) consists exactly of the points satisfying \(c_a=0\) and \(\alpha(\tau_0)=1\).

*Proof.* We check multiplication in the finite coefficients that occur in (7.1). Commuting two positive real affine root factors which are not opposite finite roots produces only real roots that are positive sums of their affine roots, by the polynomial commutator formula. Such a sum cannot be the wall root \(a\): on the wall every summand other than \(a\) is strictly positive, while multiples of the one root \(a\) do not produce another finite root in a reduced system. For opposite finite roots, their positive affine levels have positive sum; the rank-one exchange uses a denominator \(1+t^\ell uv\), \(\ell\ge1\). Its torus factor has constant term one, and all its changes in the exchanged root parameters occur at higher affine levels. It changes neither the constant torus term nor the wall coefficient. Positive torus congruences also cannot change that lowest wall coefficient.

One can make the truncation literal by taking a rational point of the alcove very close to \(F\). The value of \(a\) is then smaller than the values of every other positive real affine root and of \(\delta\); this is possible because there are only finitely many finite roots and higher levels increase values by integers. Clear denominators to get the positive integer height filtration used in Theorem 2.C. At the height of \(a\), only this one root coefficient remains. Its commutator corrections occur at larger height. The finite-jet coordinate multiplication and its inverse in that theorem work on arbitrary rings, so this coefficient calculation is a scheme calculation.

Consequently multiplication gives

\[
(q,c)(q',c')=(qq',c+q c'),\qquad q=\alpha(\tau_0),
\]

exactly the multiplication of \(x(c)\operatorname{diag}(q,1)\) in the upper triangular subgroup of \(PGL_2\). The torus-arc constant term is a group map because reduction to \(B\) followed by \(B\to T\) is one. The wall coefficient is a polynomial in the indicated finite jets, with the constant torus units inverted, so (7.1) is a scheme morphism.

The character \(\alpha:T\to\mathbb G_m\) is fppf surjective even if it is not primitive. To check this explicitly, choose coordinates so \(\alpha\) is the \(d\)-th power of a primitive character. The primitive coordinate is freely chosen; adjoining a root of a given unit through \(R[z]/(z^d-q)\) is finite free and faithfully flat, and \(z\) is a unit. This holds when the characteristic divides \(d\). The wall-root parameter supplies arbitrary \(c\), so (7.1) is fppf surjective. Its displayed equations define its schematic fibre over the identity on every algebra, giving the kernel assertion. ∎

In the ordered coordinates, every point of \(J_a(R)\) is a product of the other root-series factors, the \(\alpha\)-series factor with its lowest coefficient zero, and torus arcs satisfying \(\alpha(\tau_0)=1\). Thus these are actual generators of the functor \(J_a\), not just generators of its field-valued points.

### 7.3. Normalization, including opposite roots and torus congruences

Let \(G_\alpha=C_G(T_\alpha)\). Use its proved central torsor

\[
q_\alpha:G_\alpha\longrightarrow PGL_2,
\qquad\ker q_\alpha=Z_\alpha=\ker\alpha\subset T.
\]

Conjugation on \(G_\alpha\) factors through \(PGL_2\): fppf-locally lift an adjoint point, conjugate by that lift, and use centrality to make the result independent of the lift. Morphism descent gives the action over the original base. Conjugation by the adjoint point \(\operatorname{diag}(t^n,1)\) therefore gives an automorphism \(\delta_a\) of \((G_\alpha)_{k[t,t^{-1}]}\), with

\[
\delta_a(u_\alpha(c))=u_\alpha(ct^n),\quad
\delta_a(u_{-\alpha}(c))=u_{-\alpha}(ct^{-n}),\quad
\delta_a(\tau)=\tau\quad(\tau\in T).
\]

Let \(R_a\subset LG\) be the image of the constant \(G_\alpha\) under this automorphism. It is isomorphic to \(G_\alpha\) as a sheaf: inclusion of constant points into Laurent points is injective, and \(\delta_a\) is an automorphism. Let \(\varphi_a:SL_2\to R_a\) be the scaled rank-one homomorphism. Write its lower unipotent as

\[
y_a(z)=u_{-\alpha}(zt^{-n}).
\]

**Lemma 7.5.** The subgroup \(R_a\) normalizes \(J_a\), on arbitrary \(k\)-algebras.

*Proof.* Constant torus points belong to \(I\) and normalize its kernel \(J_a\). The upper root \(x_a(z)\) also belongs to \(I\), so it normalizes that kernel. It remains to check conjugation by \(y_a(z)\) on the explicit generators of \(J_a(R)\).

For a root-series factor \(u_\beta(t^m v(t))\), with \(\beta\ne\pm\alpha\), conjugation uses the commutator formula. Every additional factor has finite root \(-i\alpha+j\beta\) and parameter a constant times

\[
z^i v(t)^j t^{-in+jm},\qquad i,j>0.
\]

Its lowest real affine root is \(j(\beta+m\delta)-ia\). Since \(\beta+m\delta\) is positive and different from \(a\), the wall sign observation says that every such root is positive and different from \(a\). Higher coefficients add nonnegative multiples of \(\delta\) and preserve this conclusion. The factors therefore lie in \(I\), have zero wall coefficient, and have torus constant term one; they lie in \(J_a\). This covers every non-opposite root string, including the terms with \(j>1\) in non-simply-laced systems. A vanishing structure constant in small characteristic causes no problem; no constant is divided out.

For the \(\alpha\)-factor of a kernel point, write its scaled parameter as \(u\in tR[[t]]\). Direct multiplication in \(SL_2(R[[t]])\) gives

\[
y(z)x(u)y(-z)
=y\left(\frac{-z^2u}{1-zu}\right)
 h(1-zu)
 x\left(\frac{u}{1-zu}\right),
\tag{7.2}
\]

where \(h(r)=\operatorname{diag}(r,r^{-1})\). The denominator belongs to \(1+tR[[t]]\), hence is a unit over every ring. Apply the scaled homomorphism. The upper parameters are still in \(tR[[t]]\), so their affine roots are \(a+\ell\delta\), \(\ell\ge1\). The lower parameters are in \(tR[[t]]\), so their affine roots are \(-a+\ell\delta\), \(\ell\ge1\). These all belong to the kernel. The torus factor is a positive congruence, with constant term one. Thus (7.2) is an equality of kernel points also in characteristic two and over rings with nilpotents.

For a \(-\alpha\)-root factor already in \(I\), its parameter relative to \(y_a\) lies in \(tR[[t]]\): the exponent is \(m+n\ge r(-\alpha)+r(\alpha)=1\). It commutes with \(y_a(z)\), so stays in the kernel.

Finally a torus kernel point splits as a constant \(\tau_0\in\ker\alpha(R)\) and an arc \(\tau_1\) with constant term one. The first is central in \(R_a\). For the second, the root/torus relation gives

\[
y_a(z)\tau_1 y_a(-z)
=y_a\bigl(z(1-\alpha(\tau_1)^{-1})\bigr)\tau_1.
\tag{7.3}
\]

The lower parameter in parentheses is in \(tR[[t]]\), because \(\alpha(\tau_1)\in1+tR[[t]]\). Its affine roots are therefore \(-a+\ell\delta\), \(\ell\ge1\), and it belongs to the kernel. This proves normalization for positive torus congruences of every order, rather than only for their tangent vectors.

The same arguments with \(-z\) prove the reverse inclusion, hence actual equality under conjugation. They apply to the finite ordered root-series factorization of every kernel point. The scaled \(SL_2\) is generated locally by its two root groups and its torus: for a matrix its first-column entries generate the unit ideal, so the opens where the upper or lower entry is a unit give the usual Gauss factorizations, with the Weyl matrix itself a product of root matrices. Thus the verification proves normalization by every \(SL_2\)-point after a Zariski cover, and then by descent.

Every \(G_\alpha\)-point is fppf-locally a product of a central point and a point lifted from \(SL_2\). Indeed the composite \(SL_2\to G_\alpha\to PGL_2\) is the standard central fppf quotient, and the remaining ratio lies in \(Z_\alpha\). Central points are already covered by the torus check. This proves normalization by all of \(R_a\). ∎

### 7.4. Establishing the wall quotient and its two charts

**Lemma 7.6.** Scheme-theoretically,

\[
I\cap R_a=B_\alpha,\qquad J_a\cap R_a=Z_\alpha,
\tag{7.4}
\]

where \(B_\alpha=T U_\alpha\) is understood through the scaled constant embedding. Moreover

\[
\varphi_a^{-1}(J_a)=\mu_2\subset SL_2
\]

on every test algebra, including characteristic two.

*Proof.* A point of \(R_a\) centralizes the constant split torus \(T_\alpha\). If it also lies in \(I\), put it into the unique ambient integral big-cell coordinates. Conjugation by \(T_\alpha\) scales each root coordinate by that root's character restricted to \(T_\alpha\). Uniqueness and the independence of torus characters force every coordinate outside \(\pm\alpha\) to be zero. This is a comodule identity, so it works on arbitrary rings without using density of ordinary points.

Undo \(\delta_a\). The \(\alpha\)-coordinate now has nonnegative level, the \(-\alpha\)-coordinate has level at least one, and the torus arc remains integral. Depending on the original sign of \(\alpha\), the two root factors occur in one or the other big-cell order; either order reduces at \(t=0\) to \(B_\alpha\). The unscaled point was constant, so this reduction is that point itself. It therefore lies in \(B_\alpha\). Conversely every constant \(B_\alpha\)-point scales into \(I\), since \(n=r(\alpha)\). This proves the first equality as functors.

On this Borel, (7.1) is exactly the already proved central quotient \(B_\alpha\to B_{PGL_2}\): it takes the upper root parameter to the same upper parameter and the torus to \(\alpha(\tau)\). Its schematic kernel is \(Z_\alpha\), proving the second equality.

For completeness the preimage under \(SL_2\) is also explicit. The composite to \(PGL_2\) is its ordinary projective-matrix quotient. A matrix in its kernel is a scalar matrix \(rI\) with \(r^2=1\). Equivalently in the upper triangular coordinates, vanishing of the upper parameter gives \(\operatorname{diag}(r,r^{-1})\), and the adjoint torus coordinate is \(r^2\). Thus the kernel is the scheme \(\mu_2\). In characteristic two the equation is \((r-1)^2=0\); it is not replaced by the single reduced identity point. ∎

The same intersection proves \(\varphi_a^{-1}(I)=B_{SL_2}\) schematically. Its composite projective matrix preserves the first coordinate line exactly when the lower-left matrix entry is zero. For a determinant-one matrix this forces both diagonal entries to be units, which is precisely the upper triangular \(SL_2\)-Borel on every algebra. This is an equality of subgroup schemes, with the entire central \(\mu_2\) contained in that Borel.

**Proposition 7.7 (the affine-wall quotient).** There is a subgroup sheaf \(P_a\subset LG\), represented by a scheme, such that \(I\subset P_a\), and

\[
P_a/J_a\simeq PGL_2,\qquad P_a/I\simeq\mathbb P^1.
\]

The second quotient is an \(I\)-torsor with explicit Zariski-local sections.

*Proof.* Define \(P_a\) to be the fppf sheaf of products \(J_a R_a\) in \(LG\). Lemma 7.5 makes it a subgroup. Lemma 7.6 makes its quotient by the normal subgroup \(J_a\) the actual sheaf quotient

\[
R_a/(J_a\cap R_a)=G_\alpha/Z_\alpha=PGL_2.
\]

More explicitly, a local product \(jr\) is sent to \(q_\alpha(r)\). If \(jr=j'r'\), then \(r(r')^{-1}\) lies in \(R_a\cap J_a=Z_\alpha\), so the image is independent of the product presentation. Presentations on overlaps therefore descend. The map is fppf surjective because \(R_a\to PGL_2\) is, and its kernel is exactly \(J_a\). This establishes the quotient assertion rather than assuming it.

The map \(B_\alpha\to B_{PGL_2}\) is fppf surjective with kernel \(Z_\alpha\). Consequently every \(i\in I\) is fppf-locally of the form \(jb\), \(j\in J_a\), \(b\in B_\alpha\): lift \(\pi_a(i)\) to \(b\), and take \(j=ib^{-1}\). Thus \(I\subset P_a\), and its image in the constructed \(PGL_2\)-quotient is exactly the upper triangular Borel. The inverse image of that Borel is exactly \(I\), by the same lifting argument. It follows that \(P_a/I=PGL_2/B_{PGL_2}\).

There is also a direct check using only the scaled \(SL_2\) image for this last quotient. The map \(B_{SL_2}\to B_{PGL_2}\) is fppf surjective: lift its unit torus coordinate \(q\) by adjoining \(r\) with \(r^2=q\), and lift its arbitrary upper parameter by the upper root group. The algebra \(R[r]/(r^2-q)\) is finite free faithfully flat, also in characteristic two. Hence \(I=J_a\varphi_a(B_{SL_2})\) fppf locally. The central-times-\(SL_2\) lifting in Lemma 7.5 and \(Z_\alpha\subset J_a\) likewise give \(P_a=J_a\varphi_a(SL_2)\). The schematic preimage equality just proved identifies the quotient directly with \(SL_2/B_{SL_2}\), on all test schemes. Its equality relation retains the central kernel; it does not divide by a reduced substitute for \(\mu_2\).

The latter quotient is \(\mathbb P^1\) on arbitrary schemes: send a projective matrix to the line of its first column. Local generators of the line and a complementary vector give local matrix lifts; their ratios are upper triangular. One can even use determinant-one lifts on the two standard charts. Put

\[
w=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\quad
h(r)=\operatorname{diag}(r,r^{-1}),\quad n_a=\varphi_a(w).
\]

For a line \([1:z]\), use

\[
s_0(z)=\varphi_a\begin{pmatrix}1&0\\z&1\end{pmatrix}
=u_{-\alpha}(zt^{-n}).
\]

For a line \([v:1]\), use

\[
s_\infty(v)=\varphi_a\begin{pmatrix}v&-1\\1&0\end{pmatrix}
=x_a(v)n_a.
\]

On the overlap \(v=z^{-1}\), direct multiplication gives

\[
s_\infty(z^{-1})^{-1}s_0(z)
=\varphi_a\begin{pmatrix}z&1\\0&z^{-1}\end{pmatrix}
=\alpha^\vee(z)x_a(z^{-1})\in I.
\tag{7.5}
\]

These are identities of scheme maps, with only the indicated chart unit \(z\) inverted. They work in every characteristic. Each chart identifies its inverse image in \(P_a\) with \(\mathbb A^1\times I\) by \((z,i)\mapsto s_0(z)i\), or the corresponding infinity formula. Uniqueness follows from the quotient equality relation. Gluing these two products by (7.5) represents the sheaf \(P_a\) by a scheme and represents its \(I\)-torsor. Its group structure is the represented subgroup structure already constructed. Left multiplication by \(I\) on its quotient is the upper triangular action obtained from \(\pi_a\). ∎

The normalizer element \(n_a\) is the reflection representative \(t^{n\alpha^\vee}n_{s_\alpha}\), up to a constant torus element. Thus this quotient uses exactly the wall reflections and sign convention of Theorem 2.C.

### 7.5. Projective Bott–Samelson schemes, constructed from these quotients

Algebra and sheaf cohomology before reductive groups, Lemma 7.A and Corollary 7.B, proves properness of projective space, its stability under closed immersions and composition, and properness of a map from a proper scheme to a separated scheme. Its Proposition 8.2, Lemma 8.3 and Theorem 8.5 prove global generation after a sufficiently large twist on a projective scheme. We use these results to construct ample line bundles on the iterated rank-one quotients.

**Lemma 7.8.** For a word \(s_1\cdots s_m\) in affine wall reflections, the contracted product

\[
\mathcal B(s_1,\ldots,s_m)
=P_{a_1}\times^I\cdots\times^I P_{a_m}/I
\tag{7.6}
\]

is a smooth projective integral \(k\)-scheme. It has a dense open affine chart \(\mathbb A^m\) with local loop representative

\[
x_{a_1}(c_1)n_{s_1}\cdots x_{a_m}(c_m)n_{s_m}.
\tag{7.7}
\]

Its final principal \(I\)-bundle is Zariski locally trivial.

*Proof.* Start with \(\mathcal B_0=\operatorname{Spec}k\) and its trivial right \(I\)-torsor \(\mathcal E_0=I\). Inductively define

\[
\mathcal B_j=\mathcal E_{j-1}\times^I(P_{a_j}/I),
\qquad
\mathcal E_j=\mathcal E_{j-1}\times^I P_{a_j}.
\]

The action in both contracted products is \((e,p)\cdot i=(ei,i^{-1}p)\). Trivialize \(\mathcal E_{j-1}\) on a Zariski cover. On this cover the first expression is \(U\times\mathbb P^1\), and the second is \(U\times P_{a_j}\), by Proposition 7.7. The transition functions are the left \(I\)-action on the second factor. These scheme maps satisfy the cocycle condition and glue actual schemes. The two sections in §7.4, combined with these trivializations, make \(\mathcal E_j\to\mathcal B_j\) a Zariski-locally trivial right \(I\)-torsor. Thus \(\mathcal B_j\to\mathcal B_{j-1}\) is a Zariski-locally trivial \(\mathbb P^1\)-bundle, smooth and of finite presentation.

Here is a projectivity argument which supplies the line bundle rather than assuming that every such bundle is projective. Every automorphism of \(\mathbb P^1\) acts canonically on its tangent line bundle \(T_{\mathbb P^1}\simeq\mathcal O(2)\), by its differential. This action is an actual linearization, including in characteristic two: for a fractional linear transformation its derivative is the unit determinant divided by the square of the chart denominator. Consequently the transition functions of the \(\mathbb P^1\)-bundle descend this line bundle to a line bundle \(\mathcal L_j\) on \(\mathcal B_j\). On the same cover its three sections are the degree-two monomials, and the linearization gives invertible linear transition maps on their free rank-three section modules. Descend these modules to a rank-three vector bundle \(\mathcal F_j\) on \(\mathcal B_{j-1}\). Their evaluation maps descend to

\[
f_j^*\mathcal F_j\twoheadrightarrow\mathcal L_j.
\]

The resulting morphism \(\mathcal B_j\to\mathbb P(\mathcal F_j)\), using the quotient convention for the projective bundle, is a closed immersion. Locally it is exactly

\[
[u:v]\longmapsto[u^2:uv:v^2],\qquad XZ-Y^2=0.
\]

This is a scheme-theoretic closed immersion over every ring. On the chart \(X\ne0\) the equation gives coordinates \(Y/X=z\), \(Z/X=z^2\); on \(Z\ne0\) it gives the other affine chart. These charts cover the conic, since the simultaneous vanishing of \(X,Z\) would force \(Y\) nilpotent and hence leave no projective point. The overlap is the usual ratio transition. The calculation uses the middle monomial \(uv\), so it remains an immersion in characteristic two. Closed immersion is local on the target, proving the global claim.

Inductively suppose \(\mathcal B_{j-1}\) is projective over \(k\), with hyperplane line bundle \(\mathcal A\). The verified global-generation theorem gives a finite surjection

\[
\mathcal O^{q+1}\twoheadrightarrow
\mathcal F_j\otimes\mathcal A^{r}
\]

for some \(r\). The line-quotient construction of AG-RG-03, Lemma 5.A, makes \(\mathbb P(\mathcal F_j\otimes\mathcal A^r)\) a closed subscheme of \(\mathcal B_{j-1}\times\mathbb P^q\): the quotient must annihilate the kernel of the displayed surjection, which gives its closed equations on each projective chart. Tensoring with the line bundle \(\mathcal A^r\) identifies this projective bundle with \(\mathbb P(\mathcal F_j)\). The product of a projective scheme and projective space is projective, by the Segre immersion; its chart ratios and equations \(z_{ij}z_{kl}=z_{il}z_{kj}\) prove the closed immersion over every ring. Thus \(\mathcal B_j\) is projective over \(k\). This proves the induction, with \(\mathcal B_0\) as its base.

For the affine chart, start at \(\mathcal B_0\) and always choose the section \(s_\infty(c)=x_a(c)n_a\). Over the previously chosen chart the torsor is trivialized by the product of these sections; choosing the next infinity chart gives \(\mathbb A^j\) and the next product representative. It is open and dense. Indeed it is dense in the inverse image of the preceding dense chart, and this inverse image is dense because the locally trivial bundle projection is open. The bundle is integral by induction: over every integral base chart its product with \(\mathbb P^1\) is integral, and these opens overlap over the integral base. Smoothness was proved above. This gives (7.7) and completes the construction. ∎

**Lemma 7.9.** For each \(w\in\widetilde W\), there is a smooth projective integral scheme \(\mathcal B_w\) and a morphism

\[
q_w:\mathcal B_w\longrightarrow\operatorname{Gr}_G
\]

whose dense affine chart maps onto the Iwahori orbit \(In_wK/K\) on every field. On that chart the loop representative belongs to \(In_wI\) on arbitrary rings.

*Proof.* Write \(w=s_1\cdots s_m\omega\), with the affine word reduced and \(\omega\in\Omega\). Take \(\mathcal B_w\) from Lemma 7.8 and choose a representative \(n_\omega\) normalizing \(I\), as proved in Theorem 2.C. Multiplication of the local representatives gives a map \(\mathcal E_m\to LG\). The contraction relations preserve this product, and its final right \(I\)-action is right multiplication. Multiply the product by \(n_\omega\) and pass to \(LG/K\). This descends through the torsor: \(i n_\omega=n_\omega(n_\omega^{-1} i n_\omega)\), and the conjugated factor lies in \(I\subset K\). Equivalently these local representatives give trivial disc torsors and punctured trivializations whose changes are integral \(G\)-matrices, so they glue the asserted morphism to the full torsor sheaf.

On the dense chart, move the normalizer representatives to the right in (7.7). The result is

\[
x_{b_1}(\epsilon_1c_1)\cdots
x_{b_m}(\epsilon_mc_m)n_w,
\qquad
b_j=s_1\cdots s_{j-1}(a_j),
\tag{7.8}
\]

up to the harmless constant torus representative choices. The \(\epsilon_j\) are nonzero root-coordinate constants. For a reduced gallery, the \(b_j\) are precisely its distinct positive inversion roots, by the affine reflection geometry of Theorem 2.C. Its ordered inversion-root coordinate proof then identifies (7.8) with the affine cell \(In_wI/I\), on arbitrary rings. In particular its image in the Grassmannian is the indicated Iwahori orbit on each field. When \(m=0\), this is the point with representative \(n_\omega\); central torus directions cause no exception. ∎

### 7.6. Closed finite stages with their nilpotents intact

Let \(G\hookrightarrow H=GL(V)\) be the embedding of Lemma 7.2, and let \(\gamma_1,\ldots,\gamma_d\in X^*(T)\) be the weights of \(V\), with multiplicity.

**Lemma 7.10.** The weights generate \(X^*(T)\). For each \(N\), only finitely many dominant coweights \(\lambda\) can occur among geometric points of \(Y_N\), namely those satisfying

\[
-N\le\langle\gamma_i,\lambda\rangle\le N
\quad(1\le i\le d).
\tag{7.9}
\]

*Proof.* Restriction of the closed representation to \(T\) is still a closed immersion. In a weight basis, pullback of the coordinate algebra of \(GL(V)\) is generated by the weight characters and the inverse determinant character. Every character appearing in this subalgebra belongs to the lattice generated by the \(\gamma_i\). Surjectivity onto \(k[T]=k[X^*(T)]\), together with the linear independence of its character basis, forces this lattice to be all of \(X^*(T)\). This argument detects finite non-smooth torus kernels as well; it is stronger than merely spanning over \(\mathbb Q\).

Over any algebraically closed extension field \(L/k\), Theorem 2.C writes a Grassmannian point as \(k_1t^\lambda K\). The associated matrix of \(k_1\) and its inverse are integral, so they preserve the two bounding standard lattices \(t^{N}O_L^d\) and \(t^{-N}O_L^d\). In a weight basis, the lattice of \(t^\lambda\) is the direct sum of \(t^{\langle\gamma_i,\lambda\rangle}O_L\). Its bounds are exactly (7.9). Since the weights generate the character lattice, the map \(X_*(T)\to\mathbb Z^d\) given by their pairings is injective. A bounded integral box is finite, proving the assertion. ∎

**Lemma 7.11.** If \(w\in Wt^\lambda W\) for a coweight satisfying (7.9), the entire morphism \(q_w\) of Lemma 7.9 factors through \(Y_N\), with its given scheme structure.

*Proof.* First give the composite \(\mathcal B_w\to\operatorname{Gr}_H\) a finite bound \(M\). The final \(I\)-torsor of Lemma 7.8 is Zariski locally trivial. Refine its trivializing cover of the quasi-compact finite-type scheme \(\mathcal B_w\) to a finite affine cover \(\operatorname{Spec}R_j\). On each member a section supplies a matrix \(g_j\in GL(V)(R_j((t)))\) and its inverse. Their finitely many matrix entries have a common denominator bound \(t^{M_j}\). Thus the corresponding lattice has both bounds \(t^{M_j}O_{R_j}^d\subset\Lambda_j\subset t^{-M_j}O_{R_j}^d\). Take \(M\ge N,M_j\) for all \(j\). The lattice-stage universal property identifies the local morphisms to \(Z_M\) on overlaps, so the whole map factors through \(Z_M\). This is a uniform scheme bound, including nilpotent base changes.

On the dense affine chart, (7.8) is a product of an element of \(I\subset K\) and \(n_w\). Since \(w\in Wt^\lambda W\), its representative is an integral normalizer matrix on each side of \(t^\lambda\). All these integral factors and their inverses preserve the bounding standard lattices, over every test ring. The weight inequalities (7.9) consequently show that this entire chart, with its scheme structure, maps to the closed substage \(Z_N\subset Z_M\).

Pull back the defining ideal of \(Z_N\) to \(\mathcal B_w\). It vanishes on the dense chart. It therefore vanishes everywhere: an integral scheme has injective restriction of regular functions to every dense open, as follows on an affine open from injection of its domain into its fraction field. Apply this to local sections of the pulled-back ideal. The scheme \(\mathcal B_w\) is integral by Lemma 7.8, so the whole map factors through \(Z_N\). It was already a map to \(\operatorname{Gr}_G\), and the fibre-product definition of \(Y_N\) now gives the required factorization. This argument imposes the complete ideal, not just its radical. ∎

**Lemma 7.12 (the finite-stage nilpotent argument).** Each locally closed immersion \(Y_N\hookrightarrow Z_N\) is a closed immersion with its original, possibly nonreduced, scheme structure.

*Proof.* There are finitely many \(\lambda\) of Lemma 7.10. For each, there are finitely many \(w\in Wt^\lambda W\). Form the corresponding finite family of maps \(\mathcal B_w\to Y_N\to Z_N\). Their images are closed in \(Z_N\): the sources are projective over \(k\), the target is projective and hence separated, and the graph/projection argument of AG-RG-S01, Corollary 7.B, proves the maps proper. Their finite union is therefore a closed subset \(C\subset |Z_N|\), contained in \(|Y_N|\).

It equals \(|Y_N|\). Indeed take a geometric point of \(Y_N\). Its Cartan coweight is in the finite list by Lemma 7.10. The refined Cartan equality from Theorem 2.C,

\[
Kt^\lambda K=\bigcup_{w\in Wt^\lambda W}In_wI,
\]

puts it in one of the Iwahori orbits covered by the dense charts of Lemma 7.9. It is therefore in \(C\). Every point of a scheme is the image of a geometric point over an algebraic closure of its residue field, so this establishes equality of the full underlying subsets, not only of their closed rational points. Thus \(|Y_N|\) is closed in \(|Z_N|\).

Finally a locally closed immersion with closed underlying image is a closed immersion, retaining its whole structure sheaf. To check this directly on a target neighbourhood, write it as an open subscheme \(Y_N\cap U\) of a closed subscheme \(D\subset U\). Its underlying open subset is also closed in \(D\), because it is closed in \(U\). A clopen subset of a scheme is a closed subscheme with the restricted structure sheaf: locally its open-and-closed decomposition is the decomposition by an idempotent, so the restriction is a quotient by the complementary idempotent. Therefore \(Y_N\cap U\hookrightarrow D\hookrightarrow U\) is a closed immersion. The quotient ideals agree on overlaps, yielding the global closed immersion. No reduction of \(Y_N\) has been taken at any point. ∎

The theorem now follows. Each \(Y_N\) is a closed subscheme of the projective scheme \(Z_N\), hence projective. Their transitions are closed immersions by Lemma 7.3, and their union represents the full Grassmannian sheaf by that same lemma. The embeddings \(Y_N\hookrightarrow Z_N\) give the asserted closed immersion of ind-schemes into \(\operatorname{Gr}_{GL(V)}\).

It would be incorrect to replace the last argument by the assertion that Bott–Samelson images exhaust all families. Already for \(G=\mathbb G_m\), the unit \(1+\epsilon t^{-1}\), with \(\epsilon^2=0\), gives a Grassmannian point which is trivial after reduction but cannot be removed by an integral unit. The reduced point sources do not supply this nilpotent family. Here Lemma 7.3 first constructs the entire locally closed scheme \(Y_N\), and Lemma 7.12 promotes precisely that scheme to a closed subscheme using its closed support. Its nilpotents survive this promotion.

## References

- X. Zhu, [*An introduction to affine Grassmannians and the geometric Satake equivalence*](https://arxiv.org/abs/1603.05593v2), freely accessible lecture notes, §§1.1–1.3.
- A. Beauville and Y. Laszlo, [*Un lemme de descente*](https://math.univ-cotedazur.fr/u/beauvill/pubs/descente.pdf), freely accessible author version.
- B. Bhatt and P. Scholze, [*Projectivity of the Witt vector affine Grassmannian*](https://arxiv.org/abs/1507.06490), freely accessible preprint, §§8–9, for comparison with the mixed-characteristic problem.
