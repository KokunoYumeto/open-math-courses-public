# A module, its standard corner and its double

**Self-checked by the writing AI.**

Every normal right module has a canonical first-column realization in a standard form. Doubling it by its conjugate gives the standard form of its endomorphism algebra, including the positive cone and its conjugation. The distinction between a column, a diagonal corner and the whole standard Hilbert space matters throughout.

All Hilbert spaces and index sets may have arbitrary cardinality. A right action is a normal unital antirepresentation. It may have a kernel. Inner products are linear in the first variable; sums over an arbitrary set mean suprema of finite nonnegative subsums or the corresponding Hilbert limits. All intertwiners are bounded and everywhere defined.

The free research antecedent is Jean-Luc Sauvageot, [*Sur le produit tensoriel relatif d'espaces de Hilbert*](https://jot.theta.ro/jot/archive/1983-009-002/1983-009-002-002.pdf), Journal of Operator Theory 9 (1983), 237–252, especially Proposition 3.1 and Remark 3.2. Those complete pages and the preceding printed 248 were actually inspected. The proof below uses matrix amplification instead of the paper's reduction by algebra type. No source expression is imported. Takesaki II IX.3(5–8) supplies the private topic checklist; the printed conjugate-column formula in (7) requires the diagonal-corner correction explained below.

The exact existing inputs are the cone-vector theorem SF10–11, the natural-cone generators SF04, standard corners and their unique comparisons SE02–03, SE10, faithful normal semifinite weights WH13, full finite-energy GNS recovery WH11, and the complete fusion construction FU01–04, FU12. These are written providers at their stated contracts; this application does not certify their full transitive closure.

## The polar vector gives a canonical column

Let \(H\) be a right \(N\)-module. Fix a standard form \((N,L,J_N,P_N)\), with faithful normal left action \(\lambda\) and right action

\[
 \rho(b)=J_N\lambda(b^*)J_N.
 \tag{DK.1}
\]

Put \(V=L\oplus H\), let \(e,f\) be its coordinate projections, and let \(R=\operatorname{End}_{N^{\mathrm{op}}}(V)\). Thus \(eRe=\lambda(N)\), \(fRf=\operatorname{End}_{N^{\mathrm{op}}}(H)\), and \(fRe=\operatorname{Hom}_{N^{\mathrm{op}}}(L,H)\).

For any \(\xi\in V\), the functional \(\omega_\xi(b)=\langle \xi b,\xi\rangle\) is positive and normal. Positivity follows from \(\rho_V(b)\geq0\) for \(b\geq0\); normality follows by applying the normal antirepresentation to increasing bounded positive nets and then the vector functional. SF10 gives a unique \(v_\xi\in P_N\) representing \(\omega_\xi\). Its right functional agrees with its left functional because \(J_Nv_\xi=v_\xi\).

For \(b,c\in N\),

\[
 \begin{aligned}
 \langle v_\xi b,v_\xi c\rangle
   &=\omega_\xi(bc^*),\\
 \langle \xi b,\xi c\rangle
   &=\omega_\xi(bc^*).
 \end{aligned}
 \tag{DK.2}
\]

Consequently \(v_\xi b\mapsto\xi b\) is well-defined and isometric on the cyclic right subspaces. Those subspaces reduce the right actions. Extend the isometry by zero on the orthogonal complement of \(\overline{v_\xi N}\) in \(L\). As an operator on \(V\), it is a partial isometry \(u_\xi\in Re\), with

\[
 \begin{gathered}
 u_\xi v_\xi=\xi,\\
 u_\xi^*u_\xi
   =\operatorname{proj}_{\overline{v_\xi N}}.
 \end{gathered}
 \tag{DK.3}
\]

Uniqueness here includes the prescribed initial space: the value at \(v_\xi\) forces every value at \(v_\xi b\), and the operator vanishes on its initial orthogonal complement. The positive vector is unique separately. For \(\xi=0\), both are zero.

Let \(E=L^2(R)\) be a standard form, with conjugation \(J_R\) and cone \(P_R\). By SE03 and SE10, the corner \(eEe\) is canonically the standard form of \(N\); denote this unitary by \(U_e:L\to eEe\). Here \(aEb\) means the joint range of left multiplication by the projection \(a\) and right multiplication by the projection \(b\).

For bounded right intertwiners \(T_i:L\to V\), write \(t_i\in Re\) for their blocks. Prescribe

\[
 U\!\left(\sum_iT_i\zeta_i\right)
      =\sum_i t_i U_e\zeta_i.
 \tag{DK.4}
\]

Every cross coefficient \(T_j^*T_i\) is the same represented element of \(N\) as \(t_j^*t_i\). Expanding both squared norms therefore proves equality, including all cross terms. It proves that (DK.4) is well-defined, linear and isometric. The cyclic construction above makes its domain span all of \(V\).

The projection \(e\) has central support one in \(R\): a central projection dominating \(e\) contains every \(Re\) range, and those ranges contain every vector by (DK.3). FU01's full-projection density proof then gives \(\overline{\operatorname{span}Re(eEe)}=Ee\). Thus \(U:V\to Ee\) is onto. It intertwines both full actions, and

\[
 \begin{aligned}
 U\xi&=u_\xi U_ev_\xi,\\
 U(L)&=eEe,\qquad U(H)=fEe.
 \end{aligned}
 \tag{DK.5}
\]

The polar formula is therefore the value of one linear unitary, despite its vector-dependent factors. It is not a separately chosen nonlinear embedding.

Define the linear unitary on the conjugate module by \(U_{\overline H}(C_H\xi)=J_RU\xi\), where \(C_H:H\to\overline H\) is the canonical antiunitary. Then

\[
 \begin{gathered}
 J_R(U_e\zeta+U\xi)
   =U_eJ_N\zeta+U_{\overline H}C_H\xi,\\
 J_R(Ee)=eE=eEe\oplus eEf.
 \end{gathered}
 \tag{DK.6}
\]

The first row has diagonal summand \(L^2(N)\), represented by \(eEe\). It does not have the whole \(L^2(R)\) as its diagonal summand. Canonical standard-form comparisons preserve \(J_R\), \(U_e\), all block actions and (DK.4); hence they preserve this embedding without a choice of a weight on \(N\).

## The bounded-vector operator is exactly its rectangular block

Choose a faithful normal semifinite weight \(\psi\) on \(N\), use its standard GNS coordinates \(L=H_\psi\), and retain the preceding linking algebra. For \(x\in\mathfrak n_\psi^*\), put \(\Lambda'_\psi(x)=J_N\Lambda_\psi(x^*)\). A vector \(\xi\in H\) is right \(\psi\)-bounded exactly when a bounded operator \(T=L_\psi(\xi):L\to H\) satisfies

\[
 T\Lambda'_\psi(x)=\xi x
 \quad(x\in\mathfrak n_\psi^*).
 \tag{DK.7}
\]

FU03 proves that this operator is a right intertwiner and is unique. FU12 proves the complete converse finite-energy dictionary:

\[
 \begin{gathered}
 D(H,\psi)
 \longleftrightarrow
 \{T\in fRe:\psi(T^*T)<\infty\},\\
 \|\xi\|^2=\psi(T^*T).
 \end{gathered}
 \tag{DK.8}
\]

The coefficient \(T^*T\in eRe\) is identified with its element of \(N\) in this formula. In particular the block is supported on precisely the two indicated sides, \(T=fTe\). A vector-domain condition alone would not identify all finite blocks.

To check the ambient multiplication statement, choose any faithful normal semifinite weight \(\phi\) on \(fRf\) and form the faithful diagonal weight

\[
 \Phi(z)=\psi(eze)+\phi(fzf)
 \quad(z\in R_+).
 \tag{DK.9}
\]

FU04 proves, on the full bounded-vector domain, that the canonical first-column vector \(\widetilde\xi\in fH_\Phi e\) is \(\Lambda_\Phi(T)\) and has ambient left Hilbert-algebra multiplier \(T\). Here is the domain check behind that assertion. For an ambient right-bounded vector \(\theta\) with right operator \(r_c\), and blocks \(A\in eRf\), \(B\in Re\), the vector \(e\theta B\) is left \(\psi\)-bounded with right multiplier \(ecB\). The middle-corner mixed identity gives

\[
 \begin{aligned}
 A T\theta B
  &=(AT)(e\theta B)\\
  &=(A\widetilde\xi)(ecB)
   =A\widetilde\xi cB.
 \end{aligned}
 \tag{DK.10}
\]

The full-projection separation argument FU04 applies first to all \(A\) and then to all \(B\), and yields \(T\theta=r_c\widetilde\xi\). This is precisely the test defining an ambient left-bounded vector. WH11 recovers \(\widetilde\xi=\Lambda_\Phi(T)\) on the whole finite left ideal. No finite-star or analytic domain for \(\xi\) was inserted.

It follows that the ambient multiplier is \(fTe\), and its restriction to \(eH_\Phi e=L\) is the original \(L_\psi(\xi)\). This supplies both operator equalities, with their domains, for the concrete bimodule obtained by taking \(N=(M')^{\mathrm{op}}\) on a faithful concrete representation \(M\subset B(H)\). Auxiliary \(\phi\) changes only GNS coordinates; the standard-form comparison fixes the actual block and every first-column vector.

## Doubling includes the full natural cone

For any right \(N\)-module \(H\), let \(M=\operatorname{End}_{N^{\mathrm{op}}}(H)\). Give \(\overline H\) its conjugate left \(N\)-action and right \(M\)-action. Fix faithful normal semifinite \(\psi\) on \(N\), and write \(F_\psi=H\otimes_\psi\overline H\). There is a canonical \(M\)-\(M\) bimodule unitary

\[
 \begin{gathered}
 W_\psi:F_\psi\longrightarrow L^2(M),\\
 W_\psi J_{\rm d}=J_MW_\psi,\\
 W_\psi C_{\rm d}=P_M.
 \end{gathered}
 \tag{DK.11}
\]

On the dense common bounded domain its conjugation is

\[
 J_{\rm d}(\xi\otimes_\psi C_H\eta)
              =\eta\otimes_\psi C_H\xi,
 \tag{DK.12}
\]

and \(C_{\rm d}\) is the closed convex cone generated by \(\xi\otimes_\psi C_H\xi\), \(\xi\in D(H,\psi)\). In particular this cone is self-dual. We prove the cone equality as well as the underlying Hilbert-space unitary.

**A module is a projection of standard columns.** Use Zorn's lemma to split \(H\) into mutually orthogonal cyclic reducing right submodules: if their sum is not all of \(H\), a nonzero vector in its reducing orthogonal complement adds another. DK01 identifies each cyclic summand with \(p_iL\) for a projection \(p_i\in N\), by its cone vector and cyclic partial isometry. Thus, as a right module,

\[
 H\cong pL^I,\qquad
 A=\operatorname{End}_{N^{\mathrm{op}}}(L^I)
   =B(\ell^2(I))\overline\otimes N,\qquad
 M\cong pAp.
 \tag{DK.13}
\]

The chosen representation of \(p\) may be diagonal. The proof below works for every projection \(p\in A\). To verify the middle equality, take the coordinate compression of an operator commuting with the right action: every matrix entry commutes with \(\rho(N)\), hence lies in \(\lambda(N)\). Conversely bounded matrices of those entries commute with the right action. Finite matrix compressions converge strongly, so these are exactly the spatial tensor product. SE02's commutant compression proves the last equality. No countable cyclic family is asserted.

**The standard matrix Hilbert space.** Realize a standard form of \(A\) on the Hilbert space of arrays \((\zeta_{ij})\) whose squared norms have finite sum:

\[
 \begin{gathered}
 E_A=\ell^2(I\times I,L),\\
 (J_A\zeta)_{ij}=J_N\zeta_{ji}.
 \end{gathered}
 \tag{DK.14}
\]

For completeness this is an actual GNS standard form. The diagonal sum
\(\Psi(a)=\sum_i\psi(a_{ii})\) on \(A_+\) is a faithful normal semifinite weight. Addition and increasing-net normality follow by interchanging the suprema over finite subsums and increasing nets. If every diagonal value is zero, faithfulness of \(\psi\) annihilates every diagonal compression; positivity then annihilates every column of \(a^{1/2}\), so \(a=0\). Finite diagonal matrices of finite positive \(\psi\)-contractions form a net increasing strongly to one and have finite \(\Psi\)-value. WG008 proves semifiniteness.

For \(b\in\mathfrak n_\Psi\), normality gives the exact identity

\[
 \begin{gathered}
 \Psi(b^*b)
       =\sum_{i,j}\psi(b_{ij}^*b_{ij}),\\
 \Lambda_\Psi(b)_{ij}=\Lambda_\psi(b_{ij}).
 \end{gathered}
 \tag{DK.15}
\]

This isometry has dense range because single finite-energy matrix entries are dense. Left GNS multiplication is the usual matrix left action. On the finite-star domain, adjunction transposes the entries and applies the closed \(S_N\). The resulting entrywise closed antilinear operator has domain given by finiteness of the sum of the entry graph norms. Finite-coordinate arrays with entries in the original finite-star GNS domain are a graph core: truncate the finite sum of graph norms and approximate the retained entries in their graph norms. Those arrays come from finite-star matrices in \(A\). Conversely every finite-star matrix gives the stated entrywise graph, by (DK.15) for \(b\) and \(b^*\). The closed GNS involution is therefore exactly this operator. Its polar decomposition gives (DK.14) and entrywise \(\Delta_N\).

SF04–05 now constructs \(P_A\) on this actual standard form. Its complete generating set can be taken to be \(q(\Lambda_\Psi(b))=bJ_A\Lambda_\Psi(b)\) for finite-star matrices \(b\). Let \(P_F\) be the finite-coordinate projection. The vectors of \(P_FbP_F\) are the corresponding row-and-column truncations of (DK.15), and converge to \(\Lambda_\Psi(b)\); their adjoint vectors also converge. Their multipliers converge strongly to \(b\), with norm at most \(\|b\|\). Hence their \(q\)-vectors converge. In particular finite matrices with finite-star entries generate the whole cone.

We will also need positivity for every finite left-ideal vector, without a finite-star assumption. If \(b\in\mathfrak n_\Psi\), let \(h_\alpha\) be finite positive \(\Psi\)-contractions converging strongly to one. Then \(h_\alpha b\in\mathfrak n_\Psi\cap\mathfrak n_\Psi^*\), since

\[
 \begin{aligned}
 \Psi(b^*h_\alpha^2b)&\leq\Psi(b^*b),\\
 \Psi(h_\alpha bb^*h_\alpha)
       &\leq\|b\|^2\Psi(h_\alpha^2).
 \end{aligned}
 \tag{DK.16}
\]

Their GNS vectors converge to \(\Lambda_\Psi(b)\), and their multipliers converge strongly to \(b\) with a common bound. Therefore \(bJ_A\Lambda_\Psi(b)\in P_A\). This argument supplies the full domain extension needed when \(p\) does not centralize \(\Psi\).

**The fusion unitary in coordinates.** Start with \(H=L^I\). FU03's full standard-module dictionary and FU12 show that \(\xi\in D(L^I,\psi)\) has unique entries \(\xi_i=\Lambda_\psi(a_i)\), where the column \((\lambda(a_i))_i:L\to L^I\) is bounded and

\[
 \begin{gathered}
 s=\sum_i a_i^*a_i\in N_+,\qquad
 \psi(s)=\sum_i\|\xi_i\|^2<\infty,\\
 L_\psi(\xi)\zeta=(\lambda(a_i)\zeta)_i.
 \end{gathered}
 \tag{DK.17}
\]

Boundedness of a column is equivalent to boundedness of its finite positive coefficient subsums. They have a strong supremum by monotone convergence. Coordinate application of FU20 gives the entries, and normality of \(\psi\) gives the energy equality. Conversely these conditions define a vector and a bounded intertwiner satisfying the exact test (DK.7). They prove the dictionary in both directions.

For arbitrary \(\eta\in L^I\), let \(w=W(\xi\otimes_\psi C_H\eta)\) be the array prescribed by

\[
 w_{ij}=\lambda(a_i)J_N\eta_j.
 \tag{DK.18}
\]

This array is square summable: its squared norm is
\(\sum_j\langle\lambda(s)J_N\eta_j,J_N\eta_j\rangle\leq\|s\|\|\eta\|^2\).
For two columns, the same calculation with the coefficient \(\sum_i b_i^*a_i\) gives exactly FU02's fusion pairing. More precisely, the left action on the conjugate module is \(C_H\rho(c^*)C_H^{-1}\), so its pairing equals the pairing of \(\lambda(c)\) on the \(J_N\)-transformed entries. Expanding all finite-sum cross terms proves isometry on the whole radical quotient.

The image is dense. An intertwiner supported on one row, with coefficient a finite positive \(\psi\)-contraction, and an arbitrary vector on one column, gives a single entry of the form \(aJ_N\eta\). Those entries approximate every vector of \(L\) as \(a\to1\) strongly. Thus the isometry is onto \(E_A\).

When \(\eta_j=\Lambda_\psi(b_j)\) is also bounded, FU18 gives
\(J_N\lambda(a_j)J_N\Lambda_\psi(b_i)=\lambda(b_i)J_N\Lambda_\psi(a_j)\).
Applying (DK.14) to (DK.18) therefore gives the interchange (DK.12). It defines an antiunitary involution on the completion. The common bounded tensor domain is dense by FU03's vector and coefficient saturation, so the prescription determines it uniquely.

**The cone is onto.** For a bounded column \(\xi\), place \((a_i)\) in one column of a matrix \(t\in A\), with all other columns zero. Equation (DK.17) gives \(t\in\mathfrak n_\Psi\). Its \(q\)-vector has entries \(a_iJ_N\Lambda_\psi(a_j)\), which are exactly (DK.18) with \(\eta=\xi\). The preceding full-domain positivity argument puts it in \(P_A\).

Conversely take a finite matrix \(b\) with finite-star entries. For each of its finitely many nonzero columns \(k\), let \(\xi^k=(\Lambda_\psi(b_{ik}))_i\). Each is right bounded with finite energy. Set \(Q(b)=bJ_A\Lambda_\Psi(b)\) and \(d_k=W(\xi^k\otimes_\psi C_H\xi^k)\). Direct matrix multiplication gives

\[
 Q(b)=\sum_k d_k.
 \tag{DK.19}
\]

These \(q\)-vectors generate all of \(P_A\), as proved above. Closedness and convexity give equality between \(P_A\) and the image of the generated cone. This proves the missing surjectivity of the cone, not only positivity of individual generators.

**Compression and canonicity.** For \(H=pL^I\), the projection \(p\otimes\overline p\) on the fusion completion corresponds under (DK.18) to \(Q_p=pJ_ApJ_A\). This follows by intertwining the left matrix action and then its conjugate right action. Its range is \(pE_Ap\), the standard form of \(pAp\) by SE03. Right boundedness is preserved by \(p\); conversely every bounded vector in \(pL^I\) is a bounded vector in \(L^I\). Thus the compressed diagonal generators are exactly those for \(H\). SE03 gives \(Q_pP_A=P_A\cap pE_Ap\). Compressing (DK.19) proves equality of the full compressed cones. The compressed \(J_A\) still interchanges the two bounded symbols.

Finally identify \(pAp\) with \(M\). A cone-preserving unitary between two standard forms for this fixed algebra is unique by SE01 and SE10. The resulting \(W_\psi\) is therefore independent of the cyclic decomposition, matrix realization and auxiliary standard coordinates. Its agreement with the intrinsic fusion map can also be checked on generators: adjoin one copy of \(L\) to \(L^I\), use the standard matrix form for \(B(\ell^2(\{0\}\sqcup I))\overline\otimes N\), and compress to the \(0\)-corner and the \(p\)-corner. DK01's conjugate-column map sends \(C_H\eta\) to the row with entries \(J_N\eta_j\); multiplying by the block column \((a_i)\) gives exactly (DK.18). Thus this is FU04's specified corner map, not another bimodule unitary with an undetermined central phase. FU09's canonical comparison between two reference weights consequently intertwines the maps (DK.11); one cannot keep all vector symbols unchanged across the two bounded domains. If \(H=0\), both standard forms and both cones are zero and all maps have their unique zero-space meaning.

## Weight-free fusion has the specified comparison map

Let \(H\) be any right \(N\)-module and \(K\) any left \(N\)-module. Form \(V=L^2(N)\oplus H\oplus\overline K\) and \(R=\operatorname{End}_{N^{\mathrm{op}}}(V)\), with coordinate projections \(e,f,g\). DK01 and its conjugate identify

\[
 \begin{gathered}
 L^2(N)=eL^2(R)e,\\
 H=fL^2(R)e,\qquad K=eL^2(R)g.
 \end{gathered}
 \tag{DK.20}
\]

The intrinsic fusion is the corner \(fL^2(R)g\), with outer algebras \(fRf=\operatorname{End}_{N^{\mathrm{op}}}(H)\) and \(gRg=\operatorname{End}_N(K)^{\mathrm{op}}\). These are actual endomorphism algebras, including the opposite on the second side.

For faithful normal semifinite \(\psi\), DK02 identifies \(L_\psi(\xi)\) with its unique block \(t_\xi\in fRe\) for \(\xi\in D(H,\psi)\). The comparison on the original bounded tensor domain is

\[
 \begin{gathered}
 W_{H,K}^\psi(\xi\otimes_\psi\eta)
             =t_\xi U_K\eta,\qquad \eta\in K,\\
 W_{H,K}^\psi:H\otimes_\psi K
                  \longrightarrow fL^2(R)g.
 \end{gathered}
 \tag{DK.21}
\]

Here \(U_K\) is the specified conjugate of the column embedding in DK01. Every finite pairing on the right is the coefficient pairing of the two blocks, so it agrees with FU02 and kills exactly the entire radical. The resulting map is isometric.

To prove surjectivity on this particular domain, take an arbitrary bounded right intertwiner \(T:L\to H\). FU03's finite \(\psi\)-contractions give \(\xi_\alpha=T\Lambda_\psi(h_\alpha)\) with \(L_\psi(\xi_\alpha)=T\lambda(h_\alpha)\), uniformly bounded and converging strongly*. The coefficient formula makes their tensor symbols converge in fusion norm for every fixed \(\eta\). Full-projection density gives the dense span of all \(tU_K\eta\) in \(fL^2(R)g\). Hence (DK.21) is onto, including when this corner is zero.

Multiplication of the left block and the inherited right action prove that (DK.21) intertwines both complete outer actions. Comparing two faithful reference weights through their maps to this same corner gives the unique canonical unitary satisfying the FU09 bounded-test diagram and chain law. Changing the standard form of \(R\) applies its unique cone-preserving comparison, which preserves every displayed block and map. Thus the intrinsic construction eliminates the weight choice while retaining an explicit comparison with every eligible weighted completion. It does not assert that a nonfaithful or zero middle weight supplies such a completion.

## Two complete checks

**A nontracial matrix weight.** Let \(N=M_2(\mathbb C)\), \(\psi(x)=\operatorname{Tr}(Dx)\), \(D=\operatorname{diag}(1,4)\), and \(H=\mathrm{HS}_2^m\) with componentwise right matrix multiplication. Identify \(M=\operatorname{End}_{N^{\mathrm{op}}}(H)=M_m(N)\). Write \(\xi_i=a_iD^{1/2}\) and \(\eta_j=b_jD^{1/2}\). Find the doubling map, its conjugation and its whole cone, and check how a reference-weight change acts on tensor symbols.

**Solution.** Every vector is bounded here. Its right intertwiner is the column of left multipliers \(a_i\), rather than the column of matrices \(\xi_i\). For \(w=W_\psi(\xi\otimes_\psi C_H\eta)\), equation (DK.18) reads

\[
 \begin{gathered}
 w_{ij}=a_iD^{1/2}b_j^*,\\
 w_{ij}=\xi_iD^{-1/2}\eta_j^*.
 \end{gathered}
 \tag{DK.22}
\]

Conjugation is the block-matrix adjoint. A diagonal generator is the positive block matrix \(\xi D^{-1/2}\xi^*\). Conversely every positive \(Q\in M_{2m}(\mathbb C)\) is a sum of finitely many rank-one positive matrices \(zz^*\), by its orthonormal spectral decomposition. Regard each \(z\) as a \(2m\)-by-2 matrix with zero second column, and set \(\xi=zD^{1/4}\). Then \(\xi D^{-1/2}\xi^*=zz^*\). The whole positive Hilbert–Schmidt cone is therefore obtained by finite sums of the stipulated diagonal symbols.

For \(m=1\), take \(\xi=E_{12}\), \(\eta=E_{22}\). Their image is \(\tfrac12E_{12}\); using weight \(D'=I_2\) with unchanged symbols gives \(E_{12}\). Let \(\tau\) be the actual comparison to weight \(\psi'\) with any other positive invertible density \(D'\). Write \(t=\xi\otimes_\psi C_H\eta\) and \(t'=\xi'\otimes_{\psi'} C_H\eta\). Its formula is

\[
 \begin{gathered}
 \xi'=\xi D^{-1/2}(D')^{1/2},\\
 \tau t=t'.
 \end{gathered}
 \tag{DK.23}
\]

Equation (DK.22) verifies its image under \(W_{\psi'}\) equals its image under \(W_\psi\) on every finite sum. Hence it preserves the complete pairing, descends to the radical quotient and extends onto; the reversed density formula is its inverse. This explicitly checks the change in symbols.

**An arbitrary-cardinality multiplicity.** Let \(N=\mathbb C\), \(\psi(1)=c>0\), and \(H=\ell^2(I)\) for any set \(I\). Determine its double and show why the conjugate-column correction cannot be replaced by a Hilbert-dimension argument.

**Solution.** The standard GNS coordinate is \(\Lambda(z)=\sqrt c\,z\), so \(L_\psi(\xi)z=c^{-1/2}\xi z\). For \(t=\xi\otimes_\psi C_H\eta\), denote the rank-one operator by \(R_{\xi,\eta}=|\xi\rangle\langle\eta|\). The exact doubling map is

\[
 \begin{gathered}
 W_\psi:F_\psi\longrightarrow\mathrm{HS}(H),\\
 W_\psi t=c^{-1/2}R_{\xi,\eta}.
 \end{gathered}
 \tag{DK.24}
\]

The squared Hilbert–Schmidt norm of this rank-one image is \(c^{-1}\|\xi\|^2\|\eta\|^2\), precisely the fusion coefficient norm. Cross terms verify the same on all finite sums. Finite-rank operators are dense in \(\mathrm{HS}(H)\): approximate finitely many retained matrix coordinates in its square sum, using the net of finite subsets of \(I\times I\). Thus the map is onto even for nonseparable \(H\). Conjugation is adjunction. For a positive Hilbert–Schmidt operator \(T\), let \(P_F\) project onto a finite set of coordinates. Then \(P_FTP_F\geq0\) and \(P_FTP_F\to T\) in Hilbert–Schmidt norm, by the same square-sum truncation. Each finite positive matrix is a finite sum of positive rank-one operators by its finite spectral decomposition, hence an image of positive multiples of diagonal symbols. This checks the entire cone without a countable coordinate assumption.

For the first-column embedding use \(V=\mathbb C\oplus H\), \(R=B(V)\), \(E=\mathrm{HS}(V)\), and \(e\) the scalar-summand projection. Then \(Ee\cong V\), \(J_R(Ee)=eE\cong\mathbb C\oplus\overline H\), and \(eEe\cong\mathbb C=L^2(N)\). If \(\dim H=m<\infty\), the column and row each have dimension \(m+1\), whereas \(E\) has dimension \((m+1)^2\). The specified blocks and actions remain decisive when all underlying Hilbert dimensions happen to coincide in an infinite-dimensional case.

The argument proves the canonical embedding, its full bounded-operator dictionary, the complete standard-form double and the weight-free fusion comparison. Construction of arbitrary nontracial \(L^p(M)\), the tracial measurable-operator realization, automorphism-twist composition and the corrected limits of full-bimodule classification remain distinct topics.
