# Finite centers and one common multiplicity

For an actual core whose smaller center is finite-dimensional, relative Følner projections can be rounded to one integer multiplicity on a nonzero common central block. No commutation of the entire smaller center with the ambient algebra is assumed. The proof first controls distance to the intersection of the two centers, then cuts by a canonical lift in the larger center. That lift commutes with every ambient unitary. A common matrix deletion finally makes an exact integer cut inexpensive.

Our precise local inputs are [49.2](relative-hypertraces-and-folner-projections.md) (relative Følner projections inside the expected smaller algebra), [51.5](transporting-a-core-through-a-tensor-factor.md) (common matrix deletion still gives an actual core), [52.2–52.4](canonical-core-traces-and-integer-rounding.md) (canonical central lifts, exact squared matrix scaling and central prescription), [68.2–68.5](core-central-transition-bounds.md) (both weight marginals, the center bound and prior finite stationarity tests), and [83.3–83.5](normal-central-hypertraces-and-localization.md) (bounded-density localization and central-normal cost annihilation). Tracial expectations, their Hilbert-space adjointness and finite-dimensional self-adjoint diagonalization are the declared programme prerequisites. We give the spectral-gap calculation, all quantitative choices and the projection-cut estimate below.

Human-source context is Sorin Popa, *Classification of amenable subfactors of type II*, DOI 10.1007/BF02392646, Theorem 4.2.2, printed pp.213–214. Our conclusion proves the common integer projection form under the additional finite-center hypothesis. The unrestricted source theorem, bounded physical frames on a prescribed common support, and the full generating construction remain separate course obligations.

## The actual pair and a finite joint center

Let \(N\subset M\) be a proper finite-index inclusion of II₁ factors, with \(d=[M:N]>1\), and let \(S\subset R\) be an actual core in the sense of Lesson 52. Put

\[
\begin{gathered}
e=e_R^M,\quad A=\langle N,e\rangle,\\
B=\langle M,e\rangle,\\
U=Z(S),\quad V=Z(R),\\
D_0=U\vee V,\quad W=U\cap V,\\
P=E_V|_{D_0},\quad Q=E_U|_{D_0}.
\end{gathered}
\tag{84.1}
\]

The inherited probability trace on \(R\) is \(\tau\); the canonical semifinite trace on \(B\) is \(\operatorname{Tr}\), normalized by \(\operatorname{Tr}(e)=1\). The abelian algebras in (84.1) are physical algebras inside \(R\). Their represented central lifts inside \(B\) are denoted by hats. In particular a physical element of \(W\) need not commute with \(M\), whereas its canonical lift belongs to \(Z(A)\cap Z(B)\) and does commute with \(M\). This distinction is essential.

Assume \(U\) has finitely many atoms \(u_1,\ldots,u_r\). Define

\[
\begin{gathered}
m_i=\tau(u_i)>0,\quad \sum_i m_i=1,\\
a=\min_i m_i>0,\qquad H=1/a.
\end{gathered}
\tag{84.2}
\]

**Lemma 84.1 — the joint algebra is finite as well.** Under this hypothesis,

\[
\dim D_0\leq r\lfloor d\rfloor.
\tag{84.3}
\]

**Proof.** The actual bound \(x\leq dQ(x)\) in (68.9) holds for every positive \(x\in D_0\). For any nonzero projection \(q\leq u_i\) in \(D_0\), expectation onto the atom \(u_i\) gives \(Q(q)=\tau(q)u_i/m_i\). On the nonzero support of \(q\), the bound therefore says \(1\leq d\tau(q)/m_i\). Thus \(\tau(q)\geq m_i/d\). Any orthogonal nonzero projection family under \(u_i\) has at most \(\lfloor d\rfloor\) members.

Start with the one-element partition of \(u_i\). Whenever one member is not an atom of \(D_0\), split it into two nonzero subprojections. Each split increases the number of members, so the preceding integer bound forces the process to stop after finitely many splits. Its final partition consists of atoms of \(D_0\), with at most \(\lfloor d\rfloor\) atoms. A corner of an abelian von Neumann algebra under an atom is scalar: a nonscalar self-adjoint element would have a nontrivial spectral projection there. These finitely many scalar corners exhaust \(u_iD_0\). Sum over \(i\). \(\square\)

Both \(V\) and \(W\) are consequently finite-dimensional. This deduction uses the actual core bound, not just finiteness of one subalgebra in an arbitrary commutative model.

## Uniform density control and an unweighted spectral gap

Let \(p\in A\) be a nonzero finite-trace projection. Its smaller central dimension has physical label \(\zeta=C_A(p)\in U_+\). Set

\[
\begin{gathered}
c=\operatorname{Tr}(p)=\tau(\zeta)>0,\\
f=\zeta/c,\quad \tau(f)=1,\\
0\leq f\leq H1.
\end{gathered}
\tag{84.4}
\]

The last inequality follows atom by atom: \(m_i f(u_i)\leq\tau(f)=1\). Finite-dimensionality has supplied a common operator bound for every normalized actual projection dimension.

Choose the common partial basis containing \(1\) from 68.1. With \(g=\sum_j a_j^*a_j\), set

\[
\begin{gathered}
\kappa=d^{-1}E_{D_0}(g),\\
Q(\kappa)=P(\kappa)=1,\\
Tf=Q(\kappa Pf),\\
\delta=\|f-Tf\|_1\leq\Gamma_p.
\end{gathered}
\tag{84.5}
\]

Here \(\Gamma_p\) is exactly the bound (68.13), obtained from one finite set of ambient unitary tests selected before \(p\). It can be made as small as desired together with all prescribed ambient commutator defects by 49.2 and 68.5.

By (83.8), the full joint quadratic error satisfies

\[
\begin{gathered}
\mathcal E(f):=\|f-Pf\|_2^2,\\
\mathcal E(f)\leq2H\delta\leq2H\Gamma_p.
\end{gathered}
\tag{84.6}
\]

For clarity, in this bounded case the proof is only squared Jensen. Positivity, unitality and the two marginals give \(\tau((Tf)^2)\leq\tau((Pf)^2)\leq\tau(f^2)\). Expectation adjointness gives \(\|f-Pf\|_2^2=\tau(f^2)-\tau((Pf)^2)\). Since \(f,Tf\leq H\), this difference is at most \(|\tau(f^2)-\tau((Tf)^2)|\leq2H\|f-Tf\|_1\).

The next operator is unweighted:

\[
\begin{gathered}
R_0=QP|_U=(P|_U)^*(P|_U),\\
\langle h,(1-R_0)h\rangle_\tau
=\|h-Ph\|_2^2.
\end{gathered}
\tag{84.7}
\]

Expectation adjointness proves the first identity on \(L^2(U,\tau)\). Therefore \(R_0\) is self-adjoint, positive and contractive. Its fixed space is exactly \(W\). Indeed the second identity shows that a fixed vector has \(h=Ph\), hence belongs to \(U\cap V\). Conversely \(h\in W\) is fixed by both expectations. This assertion holds for complex vectors as well.

**Lemma 84.2 — a gap gives uniform distance to the common center.** If \(W\neq U\), let \(\gamma>0\) be the least positive eigenvalue of \(1-R_0\) on \(W^\perp\). If \(W=U\), set \(\gamma=1\). With \(f_0=E_W(f)\), in either case

\[
\begin{gathered}
\|f-f_0\|_2^2\leq \mathcal E(f)/\gamma,\\
\|f-f_0\|_\infty\leq\eta_p,\\
\eta_p=\sqrt{\frac{2\Gamma_p}{\gamma a^2}}.
\end{gathered}
\tag{84.8}
\]

**Proof.** For \(W\neq U\), the finite-dimensional self-adjoint operator \(1-R_0\) has zero eigenspace \(W\), so its finitely many other eigenvalues are strictly positive. Expand \(f-f_0\) in an orthonormal eigenbasis of \(W^\perp\). Since \(f_0\) lies in the kernel, (84.7) yields \(\mathcal E(f)\geq\gamma\|f-f_0\|_2^2\). Expectation \(E_W\) is the orthogonal projection onto \(W\), by trace adjointness. If \(W=U\), then \(f=f_0\) and the first inequality is immediate. Finally any \(h\in U\) satisfies \(a\|h\|_\infty^2\leq\sum_i m_i|h(u_i)|^2=\|h\|_2^2\). Combine this with (84.6) and \(H=1/a\). \(\square\)

We have not asserted that the weighted operator \(T\) is self-adjoint. The weighted operator provides stationarity and the Jensen bound; the unweighted operator provides the gap.

## Select a block that commutes with every ambient unitary

The positive common-center density \(f_0\) has \(\tau(f_0)=1\). Write it as constants on the finitely many atoms of \(W\). At least one such atom \(z\) has value \(\alpha\geq1\), since the trace-weighted average of those values is 1. It satisfies

\[
\begin{gathered}
0\neq z\in W,\quad f_0z=\alpha z,\\
\alpha\geq1,\quad \tau(z)\geq a,\\
\widehat z\in Z(A)\cap Z(B).
\end{gathered}
\tag{84.9}
\]

Each atom of \(W\) is a nonempty sum of \(U\)-atoms, proving the trace bound. The last membership is the full-corner lift of 52.2 and 68.2. It is an equality of actual represented central operators.

Take \(q=p\widehat z\). For an ambient unitary \(u\), use the canonical trace norm and abbreviate its relative defect by \(\delta_u(p)=\|[p,u]\|_2/\sqrt c\). Then

\[
\begin{gathered}
C_A(q)=c fz,\\
\operatorname{Tr}(q)=c\alpha\tau(z),\\
\delta_u(q)\leq\delta_u(p)/\sqrt a.
\end{gathered}
\tag{84.10}
\]

**Proof.** Since \(\widehat z\) is central in \(A\), \(q\) is a projection and its dimension is \(\zeta z\). Trace adjointness with \(z\in W\) gives \(\tau(fz)=\tau(f_0z)=\alpha\tau(z)\). Thus \(q\) is nonzero and finite. Since \(\widehat z\in Z(B)\), it commutes with \(u\); consequently \([q,u]=[p,u]\widehat z\) and \(\|[q,u]\|_2\leq\|[p,u]\|_2\). Divide by \(\sqrt{\operatorname{Tr}(q)}\), and use \(\alpha\geq1\), \(\tau(z)\geq a\). \(\square\)

If \(\eta_p<1/2\), (84.8) gives an everywhere positive lower dimension on this block:

\[
\begin{gathered}
c(\alpha-\eta_p)z\leq C_A(q),\\
C_A(q)\leq c(\alpha+\eta_p)z.
\end{gathered}
\tag{84.11}
\]

No spectral cut of a central algebra failing to commute with \(u\) has occurred. The common-center cut in (84.10) is exact, and its commutation is proved before using it.

## Amplify, then prescribe the exact integer

Delete a common matrix factor \(F\cong M_n(\mathbb C)\) inside \(S\). Such a unital factor exists for every positive integer \(n\): the core contains its II₁ cup factor \(K_1\), and equal-trace projection division and comparison inside \(K_1\) produce \(n\) matrix units summing to \(1\). Put \(S^0=S\cap F'\), \(R^0=R\cap F'\). By 51.5 this is again an actual core for the original inclusion. Define

\[
\begin{gathered}
e^0=e_{R^0}^M,\\
\widetilde A=\langle N,e^0\rangle,\quad
\widetilde B=\langle M,e^0\rangle.
\end{gathered}
\tag{84.12}
\]

Theorem 52.3 identifies the old centers with the new centers as actual operators, multiplies the old scalar and central dimensions by \(n^2\), and preserves old relative commutator defects. The physical center labels are also the same, by the product decompositions with \(F\). In particular \(z\in Z(S^0)\cap Z(R^0)\) and \(\widehat z\in Z(\widetilde A)\cap Z(\widetilde B)\).

Set \(\lambda=n^2c\). For any \(\eta\geq\eta_p\) with \(\eta<1/2\), choose \(n\) large enough that \(k=\lfloor\lambda(\alpha-\eta)\rfloor\geq1\). Central prescription 52.4 supplies a projection \(p'\leq q\) inside \(\widetilde A\) with

\[
\begin{gathered}
k=\lfloor\lambda(\alpha-\eta)\rfloor,\\
C_{\widetilde A}(p')=kz.
\end{gathered}
\tag{84.13}
\]

The prescribed function lies below \(C_{\widetilde A}(q)=\lambda fz\) by (84.11), so every hypothesis of central prescription is met. The exact loss fraction obeys

\[
\begin{gathered}
\ell=\frac{\widetilde{\operatorname{Tr}}(q-p')}
{\widetilde{\operatorname{Tr}}(q)},\\
\ell=1-\frac{k}{\lambda\alpha},\\
0\leq\ell\leq\frac{2\eta}{\alpha}
+\frac1{\lambda\alpha}
\leq2\eta+\frac1\lambda.
\end{gathered}
\tag{84.14}
\]

Indeed \(\widetilde{\operatorname{Tr}}(q)=\lambda\alpha\tau(z)\) and \(\widetilde{\operatorname{Tr}}(p')=k\tau(z)\), which proves the exact formula. Alternatively (84.11) bounds the dimension removed by \((2\lambda\eta+1)z\), giving the displayed upper bound after integration. All these traces are finite. This safe bound suffices; the floor formula also gives the sharper \(\ell\leq\eta/\alpha+1/(\lambda\alpha)\).

**Lemma 84.3 — deletion cost for commutators.** For every \(u\in\mathcal U(M)\), if \(\ell<1\),

\[
\delta_u(p')\leq
\frac{\delta_u(p)/\sqrt a+2\sqrt\ell}
{\sqrt{1-\ell}}.
\tag{84.15}
\]

**Proof.** In the new canonical trace, let \(t=q-p'\), which is a projection since \(p'\leq q\). The triangle inequality gives \(\|[p',u]\|_2\leq\|[q,u]\|_2+\|[t,u]\|_2\). Unitary invariance gives \(\|[t,u]\|_2\leq2\sqrt{\widetilde{\operatorname{Tr}}(t)}\). Divide by \(\sqrt{\widetilde{\operatorname{Tr}}(p')}=\sqrt{(1-\ell)\widetilde{\operatorname{Tr}}(q)}\). The old relative estimate for \(q\) is unchanged by the squared amplification, and (84.10) applies. This proves (84.15). \(\square\)

## The finite-center rounding theorem

**Theorem 84.4 — one scalar multiplicity on a common block.** Suppose the actual core \(S\subset R\) has finite-dimensional \(Z(S)\) and satisfies the relative Følner criterion of 49.2. Given a finite set \(\mathcal F\subset\mathcal U(M)\), \(\varepsilon>0\), and an integer \(k_0\geq1\), there are a common matrix deletion \(S^0\subset R^0\), a nonzero \(z\in Z(S^0)\cap Z(R^0)\), an integer \(k\geq k_0\), and a nonzero finite-trace projection \(p'\in\langle N,e_{R^0}^M\rangle\) such that

\[
\begin{gathered}
\delta_u(p')<\varepsilon\quad(u\in\mathcal F),\\
C_{\widetilde A}(p')=kz,\quad
C_{\widetilde B}(p')=kz.
\end{gathered}
\tag{84.16}
\]

Here the commutator norm and both dimensions use the new canonical traces. The projection \(p'\) is a sum of \(k\) orthogonal projections equivalent inside \(\widetilde A\) to \(e^0\widehat z\).

**Proof.** Replace \(\varepsilon\) by \(\varepsilon_*=\min(\varepsilon,1)\). Choose the following constants before selecting \(p\):

\[
\begin{gathered}
\eta=\varepsilon_*^2/256,\quad
\sigma=\gamma a^2\eta^2/2,\\
\delta_u(p)<\varepsilon_*\sqrt a/4,\\
\Gamma_p<\sigma.
\end{gathered}
\tag{84.17}
\]

The last two requirements are attainable simultaneously. Lemma 68.5 first chooses its cyclic averaging length and expresses the finitely many common basis elements as finite linear combinations of ambient unitaries. Add those unitary tests and averaging powers to \(\mathcal F\). Apply 49.2 to that one prior finite set at the smaller of the required commutator tolerances. Its quantitative calculation then gives \(\Gamma_p<\sigma\). In the integral-index case omit the unused averaging terms exactly as in 68.5. Thus (84.8) gives \(\eta_p<\eta\); all center and gap constants depend on the fixed original core, never on \(p\).

Select \(z,\alpha\) by (84.9), and only now choose \(n\) so large that

\[
\begin{gathered}
\lambda=n^2c\geq128/\varepsilon_*^2,\\
\lambda\geq2(k_0+1),\\
\ell\leq\varepsilon_*^2/64,\\
\delta_u(p')<\varepsilon_*
\quad(u\in\mathcal F).
\end{gathered}
\tag{84.18}
\]

The first two inequalities are the choices of \(n\); the last two are conclusions. To check them, \(\alpha-\eta>1/2\), so \(\lambda(\alpha-\eta)>k_0+1\) and its floor is at least \(k_0\). From (84.14), \(2\eta+1/\lambda\leq\varepsilon_*^2/128+\varepsilon_*^2/128=\varepsilon_*^2/64\). Equation (84.15) is therefore strictly smaller than \((\varepsilon_*/2)/\sqrt{1-\varepsilon_*^2/64}<\varepsilon_*\). This proves the desired commutator bounds, including the case of an empty target set.

The smaller dimension is (84.13). The larger dimension of any finite projection in the new expected smaller algebra is its smaller dimension followed by \(E_{Z(R^0)}\), by (68.12) for this actual new core. Since \(z\in Z(R^0)\), it is also \(kz\). Finally prescribe \(k\) orthogonal pieces with smaller dimension \(z\) inside \(p'\), one at a time. The remaining dimension at each step is an integer multiple of \(z\). The final remainder has zero central dimension and is zero by faithfulness. Each piece and \(e^0\widehat z\) have the same finite central dimension; 52.4 gives their equivalence in \(\widetilde A\). \(\square\)

The theorem does not require \([u,Z(A)]=0\), the extra hypothesis of 52.5. It derives a usable block in \(Z(A)\cap Z(B)\). Its support is nonzero and has the quantitative inherited trace bound \(\tau(z)\geq a\); no trace-near-one claim is made.

## Central cost is also available under this hypothesis

**Corollary 84.5 — compatible states annihilate the canonical cost.** If a compatible \(M\)-central \(E_A\)-invariant state exists and \(Z(S)\) is finite-dimensional, it annihilates the canonical positive central cost of 82.6. Therefore 82.8 supplies arbitrarily good finite projection tests with arbitrarily small positive cost inside \(A\).

**Proof.** The full-corner identification makes \(Z(A)\) finite-dimensional as well. Every linear functional on a finite-dimensional von Neumann algebra is normal: coordinates on its finitely many minimal projections determine the functional, and decreasing positive nets converge to zero in each coordinate and hence in their finite weighted sum. Thus the compatible state's restriction to \(Z(A)\) is normal. Theorem 83.5 applies with every hypothesis verified and gives zero value on the fixed canonical lift of the positive cost. Apply 82.8. The central restriction need not be faithful; its central density can vanish on some atoms. Consequently this argument alone does not identify the joint normal weights everywhere. \(\square\)

The rounding proof used stationarity directly and did not need this corollary. Neither result supplies finite-dimensionality of \(Z(S)\) from unrestricted amenability.

![A finite-center gap, a common central block and the exact integer cut](figures/finite-centers-and-common-multiplicity.svg)

*Figure 84.1. The first panel gives the actual maps, gap and uniform bound (84.6)–(84.8). The middle panel is a finite commutative diagnostic with eight atoms of weight \(1/8\), arranged as two disjoint complete two-by-two blocks. It illustrates a selected atom of \(W\), not a claimed Jones-core realization. The final panel gives exact scalar traces for \(c=3/5\), \(n=10\), \(\alpha=2\), \(\eta=1/100\); rectangle widths there are proportional to those traces. The canonical lift, rather than the physical label, supplies ambient commutation. Proof locators: (84.9)–(84.15) and Theorem 84.4. Original editable source: [finite-centers-and-common-multiplicity.py](figures/finite-centers-and-common-multiplicity.py). Human context: Popa4.2.2, printed pp.213–214.*

## Exercises with complete solutions

### Exercise 84.1 — the uniform bound

The smaller-center atoms have traces \(1/5,3/10,1/2\). Find \(a,H\), and bound each value of a positive normalized density \(f\).

**Solution.** The minimum atom trace is \(a=1/5\), so \(H=5\). The three nonnegative contributions to the unit mass are individually at most 1. Divide those bounds by the respective weights \(1/5,3/10,1/2\). Hence \(f(u_1)\leq5\), \(f(u_2)\leq10/3\), and \(f(u_3)\leq2\). The common bound 5 follows without any assumption that the density is strictly positive on every atom.

### Exercise 84.2 — a nontrivial gap

On four joint atoms use the probability matrix with diagonal weights \(3/8\) and off-diagonal weights \(1/8\). Let \(U,V\) be the row and column algebras. Compute \(R_0\), \(W\) and \(\gamma\).

**Solution.** Both row and column weights are \(1/2\), so the conditional matrix from rows to columns is \(P=\left(\begin{smallmatrix}3/4&1/4\\1/4&3/4\end{smallmatrix}\right)\); its trace adjoint \(Q\) has the same matrix. Thus \(R_0=QP=\left(\begin{smallmatrix}5/8&3/8\\3/8&5/8\end{smallmatrix}\right)\), with eigenvectors \((1,1)\), \((1,-1)\) and eigenvalues 1, \(1/4\), respectively. Every joint weight is positive, so a function constant on rows and columns is constant everywhere; \(W=\mathbb C1\). The nonzero eigenvalue of \(1-R_0\) is \(\gamma=3/4\). This is a finite probability calculation, not an actual core construction.

### Exercise 84.3 — choose a common component

Use the two-component, eight-atom diagnostic of Figure 84.1. Every joint atom has weight \(1/8\); each component has two row labels and two column labels. For row density \(f=(2+h,2-h,0,0)\), \(0\leq h<1/2\), compute \(f_0,z,\alpha\) and the exact uniform error.

**Solution.** All four row atoms have weight \(1/4\), so \(\tau(f)=1\) and \(a=1/4\). A function constant on both rows and columns must be constant within each complete two-by-two component, so \(W\) has exactly two atoms. Conditional expectation onto \(W\) averages the two row values in each component, giving \(f_0=(2,2,0,0)\). Choose its first component \(z\), with \(\tau(z)=1/2\) and \(\alpha=2\). The pointwise difference is \((h,-h,0,0)\), so \(\|f-f_0\|_\infty=h\). Zero density on the second component does not prevent selecting a nonzero common block.

### Exercise 84.4 — exact amplification and floor loss

In the previous diagnostic use \(c=3/5\), \(h=\eta=1/100\), \(n=10\). Compute \(\lambda,k\), the selected amplified trace, the rounded trace and \(\ell\).

**Solution.** We have \(\lambda=n^2c=60\) and \(k=\lfloor60(2-1/100)\rfloor=\lfloor597/5\rfloor=119\). The selected amplified projection has trace \(\lambda\alpha\tau(z)=60\); the exact integer-dimension cut has trace \(k\tau(z)=119/2\). The loss is \(1/2\), so its fraction is \(\ell=(1/2)/60=1/120\). The safe bound in (84.14) is \(2/100+1/60=11/300\), which is larger than \(1/120\). The exact formula and safe estimate agree as inequalities; no unitary commutator is being assigned by this commutative diagnostic.

### Exercise 84.5 — parameter order

For a target \(0<\varepsilon\leq1\), verify that (84.17) and the first two choices in (84.18) imply the target defect, and identify which choices can depend on \(p\).

**Solution.** Choose \(\eta=\varepsilon^2/256\), \(\sigma=\gamma a^2\eta^2/2\) and the target tolerance \(\varepsilon\sqrt a/4\) before \(p\). The prior finite basis and averaging tests give \(\Gamma_p<\sigma\), hence \(\eta_p<\eta\). After obtaining \(p\), its trace \(c\) may be small, so choose \(n\) with \(n^2c\geq128/\varepsilon^2\) and \(n^2c\geq2(k_0+1)\). Then \(\ell\leq\varepsilon^2/64\), and (84.15) is strictly smaller than \((\varepsilon/2)/\sqrt{1-\varepsilon^2/64}\leq4\varepsilon/\sqrt{63}<\varepsilon\). Only the selected block and the matrix size are chosen after \(p\); changing the already fixed finite unitary tests is unnecessary.

### Exercise 84.6 — the two kinds of central support

Explain why finite-dimensionality proves the central-normal cost implication but does not force the state to be faithful on that center or produce a trace-near-one block in Theorem 84.4.

**Solution.** On a finite center a state is a finite sum of coordinate evaluations with nonnegative coefficients of total 1, hence normal. Some coefficients may be zero; for example evaluation on the first atom of \(\mathbb C^2\) is normal and kills the second atom. Thus 83.5 gives cost annihilation weighted by the state density, while its additional faithfulness condition is still needed for an everywhere joint density identity. Separately, the atom selected in (84.9) has \(\alpha\geq1\) and trace at least \(a\), but the two-component diagnostic has only trace \(1/2\) on its positive component. The theorem proves one nonzero common support and one integer multiplicity, and its proof supplies no trace-near-one estimate.

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Public domain (CC0).*
