# Carriers, trimming and constant extraction

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The analytic part of the proof realizes, in the reduced group algebra of \(\Gamma\), bounded families of Bott profiles indexed by the heights of the tower, and the homotopies that move them from height to height. This lesson builds the model of these families and the maps that carry the model into the regular representation of \(\Gamma\). The model space has one summand for each height, the spread carrier of that height's Bott profile; it embeds in the sum of the sheets as normalized constant vectors on the \(\mathscr B\)-side of each layer. Compressing to the disjoint domains costs little because the carriers have tiny trace and the removed balls are small; and products of the expanding incidences isolate the constant vectors, so that finite words in the mean incidence blocks reproduce any prescribed band profile on the model [OpenAI-BCI, Sections 8.1-8.3, Lemmas 8.1-8.3].

- Bott profiles and carriers (Section 1).
- The model space and the four patterns (Section 2).
- Trimming and synthesis (Section 3).
- Deleted vertices and constant extraction (Section 4).

The setting of the preceding lessons is in force, in particular [Compact Bott projections and spreading](compact-bott-projections-and-spreading.md), [Polynomial avoidance, norm tests and moments](polynomial-avoidance-norm-tests-and-moments.md) (the types, the incidences \(U_{\tau,ik}\) and Proposition 1.1), and [Cycle coordinates and disjoint domains](cycle-coordinates-and-disjoint-domains.md) (the domains \(D_Q\), Proposition 2.1 and Lemma 3.1).

## 1. Bott profiles and carriers

On \(\ell^2(\Gamma)\) put \(R(g)\delta_h=\delta_{hg^{-1}}\), so that \(R(g)R(k)=R(gk)\); the unitary \(I\delta_h=\delta_{h^{-1}}\) satisfies \(IR(g)I=\lambda(g)\), so the closure of the right regular group algebra is a copy of \(C^*_r(\Gamma)\), with the same group elements. In the coordinates \(j(v,f)=ft_v\) of the embedded cover (Proposition 5.1 of [The private completion and the graphical group](the-private-completion-and-the-graphical-group.md)), a positive old edge from \(v\) to \(w\) with label \(\sigma\) and voltage \(h_e\) satisfies
\[
\begin{gathered}
t_v\sigma=h_et_w,\\
R(\sigma)\delta_{ft_w}=\delta_{fh_e^{-1}t_v} .
\end{gathered}\tag{1.1}
\]
So the block of \(R(\sigma)\) from the \(\mathscr B\)-vertex \(w\) to the \(\mathscr A\)-vertex \(v\) is the deck operator \(R_{\mathsf H}(h_e)\), which is the sampled operator \(\rho(h_e)\) of the lesson on polynomial avoidance.

Use the compact Bott projection \(p\) of Lemma 2.1 of the lesson on compact Bott projections, with \(e=\operatorname{diag}(0,1)\) and \(a=p-e\). In the torus coordinates \((\vartheta,\xi)\) of \((z,x)\) put
\[
a_i(\vartheta,\xi)=a\bigl(Z_i(\vartheta-\alpha),N_i\xi\bigr),
\]
with \(Z_i=2^{500H_i}\), \(N_i=2^{200H_i}\), supported in a small chart. Each \(e+a_i\) is a projection in \(M_2(C(\mathbb T^2))\), and by Lemma 3.1 of that lesson
\[
\begin{gathered}
[e+a_i]-[e]=\beta\\
\text{in }K_0(C(\mathbb T^2))
\end{gathered}\tag{1.2}
\]
for one fixed class \(\beta\), independent of \(i\). The *rescaling path*
\[
\begin{aligned}
a_{i,t}(\vartheta,\xi)&=a\bigl(2^{500bt}Z_i(\vartheta-\alpha),\\
&\qquad2^{200bt}N_i\xi\bigr),\qquad0\le t\le1,
\end{aligned}
\]
joins \(a_i\) to \(a_{i+1}\) through projections \(e+a_{i,t}\), with one modulus of norm continuity independent of \(i\) and of the construction, since \(b\) is fixed.

Choose real smooth cutoffs \(\chi_i\), \(0\le\chi_i\le1\), equal to one on the supports of all profiles used at level \(i\), including the \(a_{i-1,t}\), and supported in fixed enlargements of the rectangle of level \(i\) (depending only on \(b\)); and a slightly larger Borel rectangle projection \(e_i^{\rm car}\) containing \(\operatorname{supp}\chi_i\). The choices can be made so that every function of a block \((i,k)\), \(|i-k|\le1\), is supported where \(\chi_i=\chi_k=1\), because successive widths have the fixed ratios \(2^{500b}\) and \(2^{200b}\). In the right regular representation the spreading operators of Lemma 5.1 of the lesson on compact Bott projections are
\[
\begin{gathered}
T_i=\sum_ja_{ij}R(y)^j,\\
e_i^{\rm car}T_i^*T_ie_i^{\rm car}=e_i^{\rm car},
\end{gathered}
\]
and their *carriers*
\[
P_i=T_ie_i^{\rm car}T_i^*\tag{1.3}
\]
are projections commuting with the left translations, with
\[
\begin{gathered}
\tau_{\mathsf H}(P_i)=\tau_{\mathsf H}(e_i^{\rm car})\\
\le C_\nu2^{-700H_i},
\end{gathered}\tag{1.4}
\]
by Lemma 5.1 of the lesson on compact Bott projections, applied to the enlarged rectangle.
These Borel carriers serve only Hilbert space estimates; group algebra formulas use continuous functions and the finite sums \(T_i\).

## 2. The model space and the four patterns

Put \(\mathscr L=\ell^2(\Gamma)\), and let \(e_i^{\rm car}\) act on it through the right regular operators of \(\mathsf H\). The *model space* is
\[
\mathscr K=\bigoplus_{i\ge0}e_i^{\rm car}\mathscr L .\tag{2.1}
\]
A *band profile* \(f=(f_{ik})_{|i-k|\le1}\) of profile functions acts on \(\mathscr K\) from the \(k\)-th to the \(i\)-th summand by the torus function \(f_{ik}\); supports in both carriers make each block well defined, and uniformly bounded blocks of width one give a bounded operator \(f^{\rm mod}\). All cosets of \(\mathsf H\) carry the same profile. Four diagonal patterns are needed:
\[
\begin{array}{c|ccccc}
&0&1&2&3&\cdots\\\hline
\mathrm{ev}&a_0&0&a_2&0&\cdots\\
\mathrm{od}&0&a_1&0&a_3&\cdots\\
\mathrm{ev},+&0&0&a_2&0&\cdots\\
0&a_0&0&0&0&\cdots
\end{array}
\]
Each entry is a compactly supported difference from the scalar projection \(e\); a zero entry keeps the scalar part. Rotating within the disjoint pairs \((0,1),(2,3),\ldots\) and then rescaling moves the even pattern to the odd one; the pairs \((1,2),(3,4),\ldots\) move the odd pattern to the positive-even one; and the even pattern splits into the initial and the positive-even patterns. The last lesson turns this into the vanishing of the initial term.

## 3. Trimming and synthesis

Fix one construction. Let \(\mathscr H_{\rm abs}=\bigoplus_Q\ell^2(Q)\) be the abstract orthogonal sum over the sheets; a fixed matrix factor can be tensored on throughout. At an old vertex of height \(i\) of a sheet, use the carrier \(P_i\) in its deck coordinate; let \(E_{Q,i}\) be the sum of these over the old base vertices of both sides of height \(i\) in \(Q\), and
\[
E_i=\bigoplus_QE_{Q,i},\qquad E=\bigoplus_{i\ge0}E_i ;
\]
they vanish on private coordinates. Let \(D\) be the restriction to the domains \(D_Q\) of Proposition 2.1 of the lesson on cycle coordinates. Their images in \(\Gamma\) are disjoint, so coordinate inclusion is a partial isometry
\[
U:\mathscr H_{\rm abs}\to\ell^2(\Gamma),\qquad U^*U=D .
\]

**Lemma 3.1** (uniform trimming; [OpenAI-BCI, Lemma 8.1]). For each construction,
\[
\begin{gathered}
\|(1-D_Q)E_{Q,i}\|^2\\
\le C_\nu2^{-690H_i},\\
\delta_\nu:=\|(1-D)E\|\\
\le C_\nu2^{-345H_0}.
\end{gathered}\tag{3.1}
\]
In particular \(H_{0,\nu}\) can be chosen so that \(\delta_\nu\to0\). If \(A=EAE\), \(B=EBE\) and \(\Psi_\nu(A)=UDADU^*\), then
\[
\begin{gathered}
\|\Psi_\nu(A)\Psi_\nu(B)-\Psi_\nu(AB)\|\\
\le\delta_\nu^2\|A\|\|B\| .
\end{gathered}\tag{3.2}
\]

*Proof.* For a projection \(P\) and a finite set \(B_0\) of coordinates, \(\|1_{B_0}P\|^2\le\|1_{B_0}P\|_{\rm HS}^2\), and \(\|1_{B_0}P\|_{\rm HS}^2=\sum_{u\in B_0}\langle P\delta_u,\delta_u\rangle\), summed also over the matrix basis in an amplification. The diagonal entries of \(P_i\) are all equal to \(\tau_{\mathsf H}(P_i)\), since \(P_i\) commutes with left translations. If the removed set of \(Q\) is an old-centered ball meeting height \(i\), it has at most \(2^{10H_i}\) elements (Proposition 2.1 of the lesson on cycle coordinates), and (1.4) gives the first estimate, with repeated deck lifts counted separately. Empty removed sets cost nothing, and private singletons cost nothing because \(E_{Q,i}\) vanishes on private coordinates; this concerns indexed sheet coordinates, even if the same vertex is old in another sheet. Both \(D\) and \(E\) preserve the decomposition by sheets and heights, and the norm of an orthogonal sum is the supremum of the norms of the blocks, which gives \(\delta_\nu\). Finally, using \(U^*U=D\),
\[
\begin{aligned}
&\Psi_\nu(A)\Psi_\nu(B)-\Psi_\nu(AB)\\
&\qquad=UDA(D-1)BDU^*,
\end{aligned}
\]
of norm at most \(\|A\|\|B\|\|E(1-D)E\|\), which is \(\|A\|\|B\|\|(1-D)E\|^2\). \(\square\)

Let \(\mathcal J\) be the map summing finitely supported vectors of finitely many abstract sheets into their vertex coordinates in \(\Gamma\); no boundedness of untrimmed summation is assumed.

**Lemma 3.2** (synthesis on the active carriers; [OpenAI-BCI, Lemma 8.2]). Let \(n_i\) be the number of surviving old base vertices on both sides of height \(i\). Then
\[
\begin{gathered}
\|\mathcal J(1-D)E_i\|^2\\
\le n_i\sup_Q\|(1-D_Q)E_{Q,i}\|^2\\
\le C_\nu2^{-689H_i}.
\end{gathered}\tag{3.3}
\]
Consequently \(\mathcal JE\) extends to a bounded operator, and
\[
\begin{aligned}
&\|\mathcal JE-UDE\|\\
&\quad\le C_\nu\sum_{i\ge0}2^{-344.5H_i}\\
&\quad=C_\nu\frac{2^{-344.5H_0}}{1-2^{-344.5b}} .
\end{aligned}\tag{3.4}
\]

*Proof.* For a vertex \(u\in\Gamma\) and an old base vertex \(v\), only one sheet contains \(u\) with base type \(v\), by Lemma 3.1 of the lesson on cycle coordinates; so at height \(i\) every vertex receives at most \(n_i\) indexed coordinates, and the Cauchy–Schwarz inequality at each vertex gives the first inequality of (3.3) on the dense domain. Since \(n_i\le C_s2^{H_i}\), (3.1) gives the second. The bounds are summable over the heights in operator norm, because \(H_i=H_0+bi\). On the common dense domain \(\mathcal JE=UDE+\mathcal J(1-D)E\), since \(\mathcal J\) agrees with \(U\) on vectors supported in the disjoint domains. \(\square\)

## 4. Deleted vertices and constant extraction

For a pair \(|i-k|\le1\) of a type, let \(U^0_{ik}:\ell^2(\mathscr B_k)\to\ell^2(\mathscr A_i)\) be the normalized incidence before the deletions; it sends normalized constants to normalized constants, so does its adjoint, and its centered norm is at most \(\rho<1\) (Proposition 6.1 of [Expansion and the sequential law](expansion-and-the-sequential-law.md)). Let \(U_{ik}\) be its compression to the surviving vertices; the deleted fraction is at most \(\varepsilon_{\rm del}\) on each side and layer. Constants are normalized with the actual surviving counts.

**Lemma 4.1** (deleting a small fraction of vertices; [OpenAI-BCI, Lemma 8.3]). There are contractions \(\widehat U_{ik}\) on the surviving spaces that send normalized constants to normalized constants in both directions, have centered norm at most \(\rho\), and satisfy
\[
\|U_{ik}-\widehat U_{ik}\|\le C\sqrt{\varepsilon_{\rm del}},
\]
with \(C\) independent of the height and the type.

*Proof.* Let \(a,b\) be the old normalized constants, \(P_A,P_B\) the surviving coordinate projections, and \(a',b'\) the normalized restrictions; \(\|P_Aa\|^2\ge1-\varepsilon_{\rm del}\), so \(\|a'-a\|\le C\sqrt{\varepsilon_{\rm del}}\), and likewise for \(b\). Put \(Q_A=1-|a'\rangle\langle a'|\), \(Q_B=1-|b'\rangle\langle b'|\) on the surviving spaces and
\[
\widehat U=|a'\rangle\langle b'|+Q_AU_{ik}Q_B .
\]
Write \(U^0_{ik}=|a\rangle\langle b|+U_0\) with \(\|U_0\|\le\rho\). Since \(Q_AP_Aa=0\) and \(\langle b|P_BQ_B=0\), \(Q_AU_{ik}Q_B=Q_AP_AU_0P_BQ_B\) has norm at most \(\rho\). The two summands of \(\widehat U\) have orthogonal sources and orthogonal ranges, which gives the norm, the centered norm and the action on constants. The estimates \(\|U_{ik}b'-a'\|+\|U_{ik}^*a'-b'\|\le C\sqrt{\varepsilon_{\rm del}}\) bound the three remaining blocks of \(U_{ik}-\widehat U\). \(\square\)

**The model embedding.** The subgroup operators preserve \(\mathscr L=\bigoplus_{h\mathsf H}\ell^2(h\mathsf H)\). For a coset \(h\mathsf H\), the sheet \(hj(\widetilde X)\) has coordinates \(hft_v\); map a vector \(\eta\) of \(e_i^{\rm car}\ell^2(h\mathsf H)\), written as a function of \(f\in\mathsf H\), to the vector \(b'_i\otimes T_i\eta\) of that sheet, where \(b'_i\) is the normalized constant on the surviving \(\mathscr B_i\)-vertices. Changing the representative of the coset changes both sides by a left deck translation, which commutes with the right regular operators and \(T_i\). This defines an isometry
\[
\begin{gathered}
\mathcal I:\mathscr K\to\mathscr H_{\rm abs},\\
\mathcal I\mathcal I^*\le E ,
\end{gathered}\tag{4.1}
\]
isometric because \(e_i^{\rm car}T_i^*T_ie_i^{\rm car}=e_i^{\rm car}\).

**Routes through constants.** The \(\mathscr A_i\)-coordinates connect the chosen \(\mathscr B_i\)-constants. On \(\mathscr H_{\rm abs}\) consider the mean blocks
\[
\begin{gathered}
V_i=U_{ii}\otimes T_i\chi_iT_i^*,\\
W_{ik}(f)=U_{ik}\otimes T_if_{ik}T_k^*,
\end{gathered}
\]
the same on every sheet; \(V_i\) maps the \(\mathscr B_i\)-side to the \(\mathscr A_i\)-side, and \(f_{ik}\) is supported where \(\chi_i=\chi_k=1\). Matrix values in a fixed size are allowed. Let \(V=\bigoplus_iV_i\), and let \(W(f)\) be the band operator with blocks \(W_{ik}(f)\). Both are supported on \(E\) and uniformly bounded by the Schur test. For \(k\ge1\) put
\[
\begin{aligned}
\mathcal R_k(f)&=(V^*V)^kV^*W(f)\\
&\quad\times(V^*V)^k .
\end{aligned}\tag{4.2}
\]
Its block from the \(\mathscr B_j\)-side to the \(\mathscr B_i\)-side has the incidence factor
\[
(U_{ii}^*U_{ii})^kU_{ii}^*U_{ij}(U_{jj}^*U_{jj})^k
\]
and the function factor exactly \(T_if_{ij}T_j^*\), because every extra cutoff equals one on \(\operatorname{supp}f_{ij}\) and Lemma 5.1 of the lesson on compact Bott projections multiplies the spread symbols.

**Proposition 4.2** (constant extraction). For every band profile \(f\) of the fixed families,
\[
\begin{gathered}
\bigl\|\mathcal R_k(f)-\mathcal If^{\rm mod}\mathcal I^*\bigr\|\\
\le C_f\bigl(\rho^{2k}+k\sqrt{\varepsilon_{\rm del}}\bigr).
\end{gathered}\tag{4.3}
\]

*Proof.* Replace every incidence by its hatted version of Lemma 4.1; this changes the product by at most \(C_fk\sqrt{\varepsilon_{\rm del}}\). Let \(\Pi_i\) be the projection onto the normalized constants \(b'_i\) of the surviving \(\mathscr B_i\)-space. Then \(\widehat U_{ii}^*\widehat U_{ii}=\Pi_i+C_i\) with \(\Pi_iC_i=C_i\Pi_i=0\) and \(\|C_i\|\le\rho^2\), so \((\widehat U_{ii}^*\widehat U_{ii})^k=\Pi_i+C_i^k\) with \(\|C_i^k\|\le\rho^{2k}\). The middle factor \(\widehat U_{ii}^*\widehat U_{ij}\) maps \(b'_j\) to \(b'_i\) and the orthogonal complements to each other. So the hatted incidence factor is \(|b'_i\rangle\langle b'_j|\) plus a term of norm at most \(C\rho^{4k}\). The term \(|b'_i\rangle\langle b'_j|\otimes T_if_{ij}T_j^*\) is exactly the block of \(\mathcal If^{\rm mod}\mathcal I^*\). A band operator of width one has norm at most three times the supremum of its block norms, which gives (4.3), in the full operator norm, including all nonconstant modes. \(\square\)

So finite words in the mean blocks extract any prescribed band profile on the model coordinates and suppress the other incidence modes, with an error made small by choosing \(k\) first and \(\varepsilon_{\rm del}\) after.

## 5. Exercises

**Exercise 5.1.** Verify (1.1): from \(j(v,f)\sigma=j(w,fh_e)\) deduce \(t_v\sigma=h_et_w\), and compute \(R(\sigma)\delta_{ft_w}\).

**Exercise 5.2.** Why does the trimming estimate (3.1) need the trace bound \(2^{-700H_i}\) to beat the ball size \(2^{10H_i}\) by a wide margin, while the synthesis estimate (3.3) needs it to beat also the number \(n_i\le C_s2^{H_i}\) of base vertices?

**Exercise 5.3.** Show that \(\widehat U_{ii}^*\widehat U_{ii}\) restricted to \(b_i'^{\perp}\) has norm at most \(\rho^2\).

**Exercise 5.4.** In (4.2), what goes wrong if one takes \(k=0\)?

## 6. Solutions

**5.1.** The edge of the cover over \(e\) from \((v,f)\) goes to \((w,fh_e)\), so \(j(v,f)\sigma=j(w,fh_e)\), that is \(ft_v\sigma=fh_et_w\), hence \(t_v\sigma=h_et_w\). Then \(R(\sigma)\delta_{ft_w}=\delta_{ft_w\sigma^{-1}}\) and \(t_w\sigma^{-1}=h_e^{-1}t_v\), so it is \(\delta_{fh_e^{-1}t_v}\).

**5.2.** Trimming a single sheet removes at most \(2^{10H_i}\) coordinates of height \(i\), each costing \(\tau(P_i)\le C2^{-700H_i}\). Synthesis sums over sheets into one vertex, which receives up to \(n_i\) coordinates of height \(i\), and Cauchy–Schwarz costs the factor \(n_i\); \(2^{H_i}\cdot2^{10H_i}\cdot2^{-700H_i}\) is still tiny.

**5.3.** \(\widehat U_{ii}\) maps \(b_i'^\perp\) into \(a_i'^\perp\) by the summand \(Q_AU_{ii}Q_B\), of norm at most \(\rho\); so on \(b_i'^\perp\), \(\widehat U_{ii}^*\widehat U_{ii}=(Q_AU_{ii}Q_B)^*(Q_AU_{ii}Q_B)\), of norm at most \(\rho^2\).

**5.4.** With \(k=0\), \(\mathcal R_0(f)=V^*W(f)\) keeps all nonconstant modes of the incidences, whose contribution has norm of order one; the flanking powers are what suppress them, at the rate \(\rho^{2k}\).

## References

- [OpenAI-BCI] OpenAI, *A torsion-free counterexample to reduced Baum–Connes injectivity*, OpenAI Math Release preprint, 23 September 2026, Sections 8.1-8.3, Lemmas 8.1-8.3. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-Reduced-Baum-Connes-Injectivity-September-23-2026
