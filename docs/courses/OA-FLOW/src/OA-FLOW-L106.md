# Spectral unitaries from twisted matrix fixed points

A spectral fiber can have ranges spanning the whole Hilbert space without containing an invertible operator. Encoding that fiber as an off-diagonal matrix corner makes the obstruction precise: a unitary in the fiber is exactly an equivalence of the two diagonal projections. We prove that proper infiniteness and countable decomposability supply this equivalence, then use countable amplification to obtain a second proof of compact centralizer rigidity.

*Original expression: CC0-1.0 to the extent of rights held.*

<a id="oa-flow.matrix.supports"></a>

## The support information needed from homogeneity

Let \(M\ne0\) be a von Neumann algebra and let \(G\) be compact Hausdorff abelian. All automorphisms below are normal. Let \(\alpha:G\to\operatorname{Aut}(M)\) be point-ultraweakly continuous, and put
\[
 A=M^\alpha,\qquad
 M_p=\{x:\alpha_s(x)=p(s)x\ (s\in G)\}\quad(p\in\widehat G).
 \tag{MU1}
\]
More generally than requiring the full commuting-automorphism group to act ergodically, suppose a subgroup \(\Gamma\subset\operatorname{Aut}(M)\) commutes with \(\alpha\) and has \(M^\Gamma=\mathbb C1\). We will use this precise subgroup formulation in the amplification.

Here are the applicable conclusions of [HCR2–3](OA-FLOW-HCR.md#hc-2), with their subgroup argument made explicit. Write \(\ell(x)\) and \(r(x)\) for the left and right support projections, constructed in [PC1](OA-FLOW-PC.md#oa-flow.pc.1). For a nonzero fiber,
\[
 L_p=\bigvee_{x\in M_p}\ell(x),\qquad
 R_p=\bigvee_{x\in M_p}r(x)
 \tag{MU2}
\]
are nonzero projections fixed by \(\Gamma\). Indeed each member of \(\Gamma\) permutes the fiber and preserves supports and joins, since it is an order isomorphism. Scalarity of its common fixed algebra gives \(L_p=R_p=1\). Each support and its join also belongs to \(A\), since the phases cancel in \(xx^*\) and \(x^*x\).

The appearing characters \(S=\{p:M_p\ne0\}\) form a subgroup. The identity and adjoints give zero and negatives. If \(0\ne y\in M_q\) and every \(x\in M_p\) satisfied \(xy=0\), density of \(yH\) in \(\ell(y)H\) would give \(r(x)\ell(y)=0\) for all \(x\). Taking the join contradicts \(R_p=1\) and \(\ell(y)\ne0\). Some product in \(M_{p+q}\) is therefore nonzero.

HCR3's Fourier-density proof uses only the action: normal Fourier projections, character separation from the earlier biduality theorem, compact polynomial density, and normal functionals separating a closed linear subspace. It gives ultraweak density of the span of the fibers. Consequently \(\ker\alpha=S^\perp\). For a faithful action, HCR3's discrete-quotient character argument gives \(S=\widehat G\). Thus, when the action is faithful,
\[
 M_p\ne0,\qquad L_p=R_p=1
 \quad(p\in\widehat G).
 \tag{MU3}
\]
This also gives the entire dual as the action spectrum. For precision, if the integrated map \(T_f=\int_G f(s)\alpha_s\,ds\) vanishes, testing it on a nonzero element of each \(M_p\) gives \(\int_Gf(s)p(s)\,ds=0\) for every \(p\). These equations make integration against \(f\) vanish on all continuous functions, by compact polynomial density. By [HR3](OA-FLOW-HR.md#hr-03), the positive and negative parts of the real and imaginary parts of \(f\) define finite regular measures. Their integrals against continuous functions agree in pairs. The uniqueness proved in [HR2](OA-FLOW-HR.md#hr-02) identifies each pair; their disjoint positive and negative supports then imply \(f=0\) almost everywhere. Thus the annihilator ideal of the integrated action is zero and its hull is all of \(\widehat G\). Reversing the Fourier sign only reindexes this same set.

No countability assumption has entered (MU3). For the full centralizer
\[
 H_\alpha=\{\beta:\beta\alpha_s=\alpha_s\beta\ (s\in G)\},
\]
the hypothesis \(M^{H_\alpha}=\mathbb C1\) is called homogeneity. Every ergodic abelian action is homogeneous because \(\alpha(G)\subset H_\alpha\).

<a id="oa-flow.matrix.fixed"></a>

## A matrix algebra whose corner is the desired fiber

Fix \(p\in\widehat G\). On \(M_2(M)\), define
\[
 d_p(s)=\begin{pmatrix}p(s)1&0\\0&1\end{pmatrix},\qquad
 \alpha_s^p=\operatorname{Ad}d_p(s)\circ(\alpha_s\otimes\operatorname{id}).
 \tag{MU4}
\]
The matrices \(d_p(s)\) multiply according to the group law and are fixed by every entrywise \(\alpha_t\). Hence \(\alpha^p\) is an action. Normality and point-ultraweak continuity follow entry by entry from those of \(\alpha\) and continuity of \(p\). Its formula is
\[
 \alpha_s^p\begin{pmatrix}a&b\\c&d\end{pmatrix}
 =\begin{pmatrix}
 \alpha_s(a)&p(s)\alpha_s(b)\\
 \overline{p(s)}\alpha_s(c)&\alpha_s(d)
 \end{pmatrix}.
 \tag{MU5}
\]
The fixed algebra is therefore
\[
 N=M_2(M)^{\alpha^p}
   =\begin{pmatrix}A&M_{-p}\\M_p&A\end{pmatrix}.
 \tag{MU6}
\]
This notation specifies the four entry spaces; it asserts no direct-sum algebra multiplication between them. The fixed set is a unital *-algebra, and is ultraweakly closed as the intersection of the kernels of the normal maps \(\alpha_s^p-I\), so it is a von Neumann algebra. In particular
\[
 x\in M_p\quad\Longleftrightarrow\quad x\otimes e_{21}\in N.
 \tag{MU7}
\]

For later use the compact average is a faithful normal conditional expectation onto \(N\). Normality and contractivity follow from [AT5](OA-FLOW-AT.md#oa-flow.at.5) on the finite matrix algebra. Haar invariance gives its range and shows it fixes \(N\). If \(a,b\in N\), moving their fixed factors through the scalar normal integrals gives \(E_N(aXb)=aE_N(X)b\). At every finite matrix level, averaging positive matrices under automorphisms preserves positivity; thus the expectation is completely positive. Faithfulness follows directly: for \(0\ne X\geq0\), choose a positive normal vector functional \(\omega\) with \(\omega(X)>0\). The continuous nonnegative function \(\omega(\alpha_s^p(X))\) is positive near zero, and that neighborhood has positive Haar mass by [HR6](OA-FLOW-HR.md#hr-06). Its integral is positive, so \(E_N(X)\ne0\).

<a id="oa-flow.matrix.carriers"></a>

## Fiber unitaries and the two central carriers

Let \(e=1\otimes e_{11}\) and \(f=1\otimes e_{22}\), both in \(N\). A unitary \(u\in M_p\) gives
\[
 w=u\otimes e_{21}\in N,\qquad w^*w=e,\quad ww^*=f.
 \tag{MU8}
\]
Conversely, if \(w\in N\) implements \(e\sim_N f\), its initial and final support equations imply \(w=fwe\). Its only possible nonzero entry is consequently \(u\) in the lower-left corner. Equation (MU6) gives \(u\in M_p\), and the two equations in (MU8) give \(u^*u=uu^*=1\). Thus
\[
 M_p\cap\mathcal U(M)\ne\varnothing
 \quad\Longleftrightarrow\quad e\sim_N f.
 \tag{MU9}
\]

Assume the full aggregate supports (MU3). The central carrier \(c_N(e)\), whose existence is proved in [PC2](OA-FLOW-PC.md#oa-flow.pc.2), commutes with \(e\) and dominates it. Therefore it has the form \(\operatorname{diag}(1,b)\), with \(b\) a projection in \(A\). Commuting with \(x\otimes e_{21}\), for every \(x\in M_p\), gives \(bx=x\). Thus \(b\geq\ell(x)\) for every such \(x\), and \(b=1\) by (MU3). Similarly \(c_N(f)=\operatorname{diag}(a,1)\) and centrality gives \(xa=x\); hence \(a\geq r(x)\) for all \(x\), so \(a=1\). We have proved
\[
 c_N(e)=c_N(f)=1_N.
 \tag{MU10}
\]
Both support equalities are used: left supports determine the lower diagonal carrier and right supports determine the upper one.

<a id="oa-flow.matrix.unitaries"></a>

## Proper infiniteness supplies the equivalence

Suppose \(M\) is sigma-finite and \(A\) is properly infinite. By [PC7](OA-FLOW-PC.md#oa-flow.pc.7), choose a faithful normal state \(\psi\) on \(M\). The formula
\[
 \psi_2(X)=\tfrac12\bigl(\psi(X_{11})+\psi(X_{22})\bigr)
 \tag{MU11}
\]
is a normal state on \(M_2(M)\). It is faithful: for \(X\geq0\), zero value forces both diagonal entries to vanish. For every \(\xi\in H\), the squared norm of \(X^{1/2}(\xi,0)\) is \(\langle X_{11}\xi,\xi\rangle=0\), and the analogous assertion holds on the second coordinate. Therefore \(X^{1/2}=0\). Restriction gives a faithful normal state on \(N\), so its projections are countably decomposable by PC7.

The corners \(eNe\) and \(fNf\) are each naturally isomorphic to \(A\). Their units \(e,f\) are therefore properly infinite projections in \(N\). Equation (MU10) and the full earlier comparison theorem PC7 imply \(e\sim_N f\): each is subequivalent to the other, and [PC3](OA-FLOW-PC.md#oa-flow.pc.3) gives projection Cantor–Bernstein. Equation (MU9) now supplies a unitary \(u_p\in M_p\).

Multiplication by this unitary identifies the entire fiber:
\[
 M_p=u_pA=Au_p.
 \tag{MU12}
\]
Indeed \(u_p^*x,xu_p^*\in A\) for \(x\in M_p\), while multiplying any fixed element by \(u_p\) gives the required character. Two choices differ by a unique fixed unitary, since \(u_p^*v_p\in\mathcal U(A)\). The comparison proves existence in every fiber under the stated hypotheses; it does not turn an arbitrary nonzero fiber element into a unitary.

<a id="oa-flow.matrix.scalars"></a>

## A fixed-algebra automorphism acts by one scalar per fiber

Retain faithfulness of \(\alpha\), scalar common fixed points for \(\Gamma\), sigma-finiteness of \(M\), and proper infiniteness of \(A\). Suppose a normal automorphism \(\sigma\) preserves every fiber, fixes \(A\) pointwise, and commutes with every member of \(\Gamma\). For a unitary \(u_p\in M_p\), put
\[
 v_p=u_p^*\sigma(u_p)\in\mathcal U(A).
 \tag{MU13}
\]
This element is central in \(A\). For \(a\in A\), also \(u_pau_p^*\in A\), so applying \(\sigma\) to that fixed element gives
\(\sigma(u_p)a\sigma(u_p)^*=u_pau_p^*\). Multiplying on the left by \(u_p^*\) and on the right by \(u_p\) proves \(v_pav_p^*=a\).

For \(\beta\in\Gamma\), write \(\beta(u_p)=u_pb\), with \(b\in\mathcal U(A)\), using (MU12). Commutation of \(\beta\) with \(\sigma\), and fixedness of \(b\), give
\[
 \beta(v_p)=\beta(u_p)^*\sigma(\beta(u_p))
           =b^*u_p^*\sigma(u_p)b
           =b^*v_pb=v_p.
 \tag{MU14}
\]
Scalarity of \(M^\Gamma\) now yields \(v_p=\lambda(p)1\), with \(|\lambda(p)|=1\). Since \(\sigma\) fixes \(A\), (MU12) gives
\[
 \sigma(x)=\lambda(p)x\quad(x\in M_p).
 \tag{MU15}
\]
Products \(u_pu_q\) are nonzero unitaries in \(M_{p+q}\). Applying (MU15) before and after multiplication gives \(\lambda(p+q)=\lambda(p)\lambda(q)\), and \(\lambda(0)=1\). The dual of a compact group is discrete, as proved in HCR3. Biduality, proved in [H3](OA-FLOW-HARMONIC-LATE.md#l138-h3), gives \(s_0\in G\) with \(\lambda(p)=p(s_0)\). Fourier density and normality then imply \(\sigma=\alpha_{s_0}\).

In particular this applies to the original homogeneous centralizer problem with \(\Gamma=H_\alpha\): since \(\alpha(G)\subset H_\alpha\), commutation with \(H_\alpha\) makes \(\sigma\) preserve every fiber. The stronger arbitrary-algebra proof in HCR uses the Gram isometry directly; the argument here records the additional unitary-fiber construction.

<a id="oa-flow.amplify.matrices"></a>

## Countable matrices and normal amplification

We next establish the amplification facts needed to remove proper infiniteness. Represent \(M\) faithfully and nondegenerately on \(H\), let \(K=\ell^2(\mathbb N)\), and put \(\widetilde M=M\overline\otimes B(K)\). Its elements are exactly the bounded operators on \(H\otimes K\) whose matrix entries \(X_{ij}\) lie in \(M\). One inclusion follows by taking entries of the weakly closed tensor algebra. For the converse let \(Q_n=1\otimes\sum_{j=1}^ne_{jj}\). The compressions \(Q_nXQ_n\) are finite matrices over \(M\), belong to the tensor algebra, and converge strongly to \(X\), with norms at most \(\|X\|\).

Every normal automorphism \(\beta\) of \(M\) has a unique normal amplification
\[
 \widetilde\beta(X)_{ij}=\beta(X_{ij}).
 \tag{MU16}
\]
Here is the boundedness and topology argument on the whole algebra. On \(n\)-by-\(n\) matrices the entrywise map is an algebraic *-isomorphism. The C*-norm estimate for *-homomorphisms in [CF6](OA-FLOW-CF.md#oa-flow.cf.6), in both directions, makes it isometric. Consequently the finite matrices \([\beta(X_{ij})]_{i,j\leq n}\) are compatible and bounded by \(\|X\|\). Their sesquilinear forms define a bounded form on finite-support vectors. Completion and [CF8](OA-FLOW-CF.md#oa-flow.cf.8) give the unique bounded operator with these entries. The preceding characterization puts it in \(\widetilde M\).

This map is normal. A vector coefficient with two finite-support vectors is a finite sum of normal functionals \(X\mapsto\omega_{ij}(\beta(X_{ij}))\). Approximation of arbitrary vectors by finite-support vectors, with the common bound \(\|\widetilde\beta(X)\|\leq\|X\|\), gives norm convergence of these functionals. The predual is norm closed by [CP6](OA-FLOW-CP.md#oa-flow.cp.6), so all vector coefficients pull back to normal functionals. The summable vector-series description CP4 then gives the same conclusion for every normal functional.

Adjoints and linear operations are preserved entrywise. For multiplication, \(XQ_nY\to XY\) strongly with a common norm bound. [BD5](OA-FLOW-BD.md#oa-flow.bd.5) gives ultraweak convergence. The finite entry sums and (MU16) show
\(\widetilde\beta(XQ_nY)=\widetilde\beta(X)Q_n\widetilde\beta(Y)\).
Normality of \(\widetilde\beta\) and bounded strong convergence on the right prove multiplicativity. The identical construction for \(\beta^{-1}\) is its inverse. Thus (MU16) is a normal automorphism with normal inverse, without any assertion about infinite entry sums converging in norm.

<a id="oa-flow.amplify.fixed"></a>

## The amplified fixed algebra is properly infinite and sigma-finite

Apply (MU16) to every \(\alpha_s\), giving \(\widetilde\alpha_s=\alpha_s\otimes\operatorname{id}\). The group law is checked on entries. For each \(X\), finite-support vector coefficients are continuous in \(s\); approximation of the test vectors and summable-vector tails, uniformly bounded by \(\|X\|\), gives point-ultraweak continuity. The action is faithful when \(\alpha\) is faithful, by testing \(x\otimes e_{11}\).

The matrix-entry characterization gives
\[
 \widetilde M^{\widetilde\alpha}=A\overline\otimes B(K).
 \tag{MU17}
\]
Indeed fixedness is exactly the requirement that every entry be in \(A\); finite compression proves membership in the indicated tensor algebra. If \(\sigma\) fixes \(A\) pointwise, its normal amplification fixes (MU17) pointwise by the same entry formula.

The algebra \(\widetilde M\) is sigma-finite whenever \(M\) is. With \(\psi\) as above, set
\[
 \widetilde\psi(X)=\sum_{n\geq1}2^{-n}\psi(X_{nn}).
 \tag{MU18}
\]
Each summand is a positive normal functional, and the series converges in functional norm, so CP6 proves normality. It has value one at the identity. If \(X\geq0\) has zero value, faithfulness of \(\psi\) gives \(X_{nn}=0\) for every \(n\). Then \(X^{1/2}\) annihilates every vector \(\xi\otimes e_n\), by the same diagonal quadratic-form argument as in (MU11); density implies \(X=0\). This proves faithfulness and hence sigma-finiteness by PC7.

Finally define isometries on \(K\) by
\[
 s_1e_n=e_{2n-1},\qquad s_2e_n=e_{2n}.
 \tag{MU19}
\]
They have orthogonal ranges with range projections summing to one. The elements \(1\otimes s_1,1\otimes s_2\) lie in the fixed algebra (MU17), have initial projection one, and have orthogonal final projections. Thus its unit is properly infinite.

<a id="oa-flow.amplify.subgroup"></a>

## The subgroup that makes stabilization work

Now let \(\Gamma=H_\alpha\) and assume the original homogeneous centralizer hypotheses: \(\sigma\) commutes with \(H_\alpha\) and fixes \(A\) pointwise. On \(\widetilde M\), let \(\mathcal K\) be the group generated by
\[
 \{\beta\otimes\operatorname{id}:\beta\in H_\alpha\}
 \quad\hbox{and}\quad
 \{\operatorname{id}\otimes\operatorname{Ad}w:w\in\mathcal U(B(K))\}.
 \tag{MU20}
\]
Every generator commutes with \(\widetilde\alpha\), by its entries or its separate tensor leg. The amplified \(\widetilde\sigma\) commutes with the first family by hypothesis and with the second family by its entry formula and the normal extension just proved. It consequently commutes with the generated group.

The common fixed algebra of \(\mathcal K\) is exactly the scalars. To see this directly, suppose \(X\) is fixed by the second family. The diagonal unitary \(1-2e_{nn}\) negates every off-diagonal entry in row or column \(n\), so those entries vanish. A unitary interchanging \(e_i,e_j\) then makes \(X_{ii}=X_{jj}\). Thus \(X=x\otimes1\) for one \(x\in M\). Invariance under the first family gives \(\beta(x)=x\) for every \(\beta\in H_\alpha\), so \(x\) is scalar. Hence
\[
 \widetilde M^{\mathcal K}=\mathbb C1.
 \tag{MU21}
\]
Both families matter. Invariance under the first alone puts every entry in \(M^{H_\alpha}=\mathbb C1\), so its fixed algebra is \(1\otimes B(K)\), as follows from the same bounded-matrix characterization. The second family reduces this to its scalar center.

<a id="oa-flow.amplify.rigidity"></a>

## Centralizer rigidity after stabilization

First assume \(\alpha\) is faithful. Apply the subgroup form (MU3) to \((\widetilde M,G,\widetilde\alpha,\mathcal K)\). Equations (MU17)–(MU19) supply the properly infinite fixed algebra and sigma-finiteness needed for (MU9)–(MU12). There is therefore a unitary in every amplified spectral fiber.

The automorphism \(\widetilde\sigma\) fixes the amplified fixed algebra and commutes with \(\mathcal K\), by the preceding two sections. It preserves the amplified fibers because \(\sigma\) commutes with every \(\alpha_s\). Thus all hypotheses of (MU13)–(MU15) hold for this specified subgroup, and that argument gives
\[
 \widetilde\sigma=\widetilde\alpha_{s_0}
 \quad\hbox{for some }s_0\in G.
 \tag{MU22}
\]
Testing \(x\otimes e_{11}\) yields \(\sigma(x)=\alpha_{s_0}(x)\) for all \(x\in M\).

For a possibly nonfaithful action, its kernel \(K_0\) is closed, as the intersection of the zero sets of the continuous scalar functions \(\omega(\alpha_s(x)-x)\). The compact Hausdorff quotient and induced faithful action are proved in [QF1](OA-FLOW-QF.md#qf-1) and HCR3. Its image, fixed algebra and centralizer are unchanged. The faithful argument gives a coset in \(G/K_0\), any representative of which supplies the required \(s_0\). We have proved
\[
 M\ \hbox{sigma-finite},\quad M^{H_\alpha}=\mathbb C1,\quad
 \sigma|_{M^\alpha}=\operatorname{id},\quad
 \sigma\beta=\beta\sigma\ (\beta\in H_\alpha)
 \quad\Longrightarrow\quad \sigma\in\alpha(G).
 \tag{MU23}
\]
The argument uses commutation with the explicitly constructed \(\mathcal K\); it requires no claim that \(\widetilde\sigma\) commutes with every automorphism in the larger amplified centralizer. HCR proves the same conclusion even without sigma-finiteness, by its Gram-isometry method.

The mathematical source for the twisted-matrix, comparison and stabilization questions is Takesaki, *Theory of Operator Algebras II*, Exercise XI.1.5(d)–(i), printed pages 330–331. The complete comparison and amplification proofs above accompany the support and centralizer arguments in HCR and the compact ergodic-trace theorem in ET.
