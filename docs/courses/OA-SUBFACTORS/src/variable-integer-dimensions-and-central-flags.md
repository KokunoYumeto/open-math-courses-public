# Rounding the whole projection with variable integer dimension

A scalar integer multiple of one central support is a strong rounding requirement. There is a weaker, unconditional conclusion for an arbitrary actual core: the entire Følner projection can be perturbed to have a bounded integer-valued central dimension. That integer may vary over the center. Its cyclic summands have a finite nested flag of central supports. We prove this conclusion and convert its columns into bounded finite-stage frames with a nested flag, preserving their total energy.

The proofs use the actual core changes and central prescription in 52.3–52.4, the relative Følner criterion [49.2](relative-hypertraces-and-folner-projections.md), finite-stage expectations and column estimates 53.1–53.3, and finite matrix functional calculus. General trace, expectation and projection-comparison prerequisites retain their exact programme scopes. We do not invoke a new averaging theorem. The original rounding target has human-source credit to Sorin Popa, Theorem 4.2.2, printed pp. 213–214, [DOI 10.1007/BF02392646](https://doi.org/10.1007/BF02392646). The common-support conclusion of that theorem remains a further requirement.

Let \(N\subset M\) be a proper finite-index II₁ inclusion, with an actual core \(S\subset R\). Write

\[
\begin{gathered}
e=e_R^M,\qquad A=\langle N,e\rangle,\\
B=\langle M,e\rangle,\\
C_A(e)=1,\qquad \operatorname{Tr}(e)=1,\\
C=Z(A)\cong Z(S).
\end{gathered}
\tag{73.1}
\]

The finite measure \(\nu\) on this center is \(\nu(z)=\operatorname{Tr}(ez)\); thus \(\nu(1)=1\). Center functions and their smaller-core labels are identified through the full corner, as in 52.2. No assumption that \(C\) commutes with \(M\) is made.

## Global rounding does not require selecting a spectral bin

**Theorem 73.1 — bounded variable integer rounding.** Fix a nonzero finite projection \(p\in A\), put \(c=\operatorname{Tr}(p)>0\), and let \(\zeta=C_A(p)\). For every integer \(K\geq1\) and every \(0<r<1\), some deletion of a finite matrix factor from the core gives canonical algebras \(\widetilde A\subset\widetilde B\), with the old algebras embedded as in 52.3, and a projection \(q\leq p\) in \(\widetilde A\), such that the following hold. Write \(c'=\widetilde{\operatorname{Tr}}(p)\). The function \(k\) takes values in \(\{0,K,K+1,\ldots,L\}\).

\[
\begin{gathered}
C_{\widetilde A}(q)=k,\\
k\in L^\infty(C,\nu),\\
\widetilde{\operatorname{Tr}}(q)
>(1-r)c',\\
\widetilde{\operatorname{Tr}}(p-q)
<rc'.
\end{gathered}
\tag{73.2}
\]

Here \(L\geq K\) is a finite integer, and \(q\ne0\). For any finite family \(u_1,\ldots,u_m\in\mathcal U(M)\), let

\[
\begin{gathered}
D_U(a)^2=\sum_{j=1}^m
\|u_ja u_j^*-a\|_2^2,\\
\delta_U(p)=D_U(p)/\sqrt c
\end{gathered}
\tag{73.3}
\]

in the old trace. Then the new trace satisfies

\[
\frac{D_U(q)}{\sqrt{\widetilde{\operatorname{Tr}}(q)}}
<\frac{\delta_U(p)+2\sqrt{mr}}{\sqrt{1-r}}.
\tag{73.4}
\]

**Proof.** The integrable density \(\zeta\) is nonnegative and finite almost everywhere, and \(\int\zeta\,d\nu=c\). As \(n\to\infty\), dominated convergence gives

\[
\int \zeta\,1_{\{n^2\zeta<K\}}\,d\nu\longrightarrow0.
\tag{73.5}
\]

At points where \(\zeta=0\), the integrand is zero. At every point where \(\zeta>0\), it eventually vanishes. Choose an integer \(n\geq2\) such that the integral in (73.5) is less than \(rc/3\) and \(1/(n^2c)<r/3\). Choose a unital \(M_n\) in \(S\) using 50.5, and realize its complement as an actual core by 51.5. Theorem 52.3 identifies the smaller centers as the same operators, preserves \(\nu\), and gives

\[
\begin{gathered}
f=n^2\zeta=C_{\widetilde A}(p),\\
c'=\widetilde{\operatorname{Tr}}(p)=n^2c,\\
\int f\,1_{\{f<K\}}\,d\nu<rc'/3.
\end{gathered}
\tag{73.6}
\]

Since \(f\) is integrable, choose a finite real \(H\geq K\) with \(\int f1_{\{f>H\}}d\nu<rc'/3\). Set

\[
\begin{gathered}
z=1_{[K,H]}(f),\\
k=\lfloor f\rfloor z,\qquad L=\lfloor H\rfloor.
\end{gathered}
\tag{73.7}
\]

The floor is ordinary Borel spectral calculus on the abelian center. It is zero off \(z\) and lies between \(K\) and \(L\) on \(z\). Since \(0\leq k\leq f\), central prescription 52.4 supplies \(q\leq p\) with dimension \(k\). In particular \(q\leq pz\): the dimension of \(q(1-z)\) is zero, and trace faithfulness kills that projection.

The total loss, in the new trace, is

\[
\begin{aligned}
\ell&=\int(f-k)\,d\nu\\
&=\int_{\{f<K\}}f\,d\nu
+\int_{\{f>H\}}f\,d\nu\\
&\quad+\int_z(f-\lfloor f\rfloor)\,d\nu\\
&<2rc'/3+1<rc'.
\end{aligned}
\tag{73.8}
\]

The third integral is at most \(\nu(z)\leq1\). The last strict inequality uses \(1/c'<r/3\). Thus the three global losses are controlled before any individual central piece is selected. This proves (73.2), including nonzeroness.

Because \(q\leq p\), the difference \(p-q\) is a projection and has squared \(L^2\) norm \(\ell\). In the direct sum of the \(m\) trace Hilbert spaces, the triangle inequality gives

\[
D_U(q)\leq D_U(p)+2\sqrt m\sqrt\ell.
\tag{73.9}
\]

The trace change multiplies both \(D_U(p)\) and \(\sqrt c\) by \(n\), so its normalized defect stays \(\delta_U(p)\). Divide (73.9) by \(\sqrt{c'-\ell}>\sqrt{(1-r)c'}\) to obtain (73.4). All unitaries still act on the same \(L^2(M)\), inside \(\widetilde B\). No commutation with a spectral projection was used. \(\square\)

**Corollary 73.2 — unconditional flag input from relative Følner.** If the relative Følner criterion holds for one actual core, then for every finite nonempty \(U\subset\mathcal U(M)\), \(\varepsilon>0\) and integer \(K\geq1\), some actual core admits a nonzero finite projection \(q\) with bounded integer central dimension, at least \(K\) on its support, and

\[
D_U(q)<\varepsilon\sqrt{\operatorname{Tr}(q)}.
\tag{73.10}
\]

**Proof.** Write \(m=|U|\). Criterion 49.2 supplies \(p\) with \(\delta_U(p)<\varepsilon/4\), by using tolerance \(\varepsilon/(4\sqrt m)\) for each unitary. Choose

\[
\begin{gathered}
0<r\leq1/16,\\
r\leq\varepsilon^2/(256m).
\end{gathered}
\tag{73.11}
\]

Then \(2\sqrt{mr}\leq\varepsilon/8\) and \(\sqrt{1-r}>3/4\). Formula (73.4) is therefore less than \(\varepsilon/2\), which suffices. Apply Theorem 73.1 with the prescribed \(K\). \(\square\)

## The summands form a finite central flag

**Proposition 73.3 — exact flag columns.** Let \(q\) in the smaller canonical algebra have a nonzero bounded integer central dimension \(k\), with maximum \(L\). In the smaller-core labeling put

\[
\begin{gathered}
z_i=1_{\{k\geq i\}}\in Z(S),\\
1\leq i\leq L.
\end{gathered}
\tag{73.12}
\]

Then \(z_1\geq\cdots\geq z_L\), \(k=\sum_i z_i\), and there are orthogonal projections \(q_i\) and partial isometries \(v_i\in Ae\) such that

\[
\begin{gathered}
q=\sum_i q_i,\qquad C_A(q_i)=z_i,\\
q_i=v_iv_i^*,\qquad
v_i^*v_j=\delta_{ij}ez_i.
\end{gathered}
\tag{73.13}
\]

Zero supports and zero columns are allowed. Put \(\xi_i=v_i\widehat1\). Then \(\xi_i\in L^2(N)z_i\), \(\|\xi_i\|_2^2=\tau(z_i)\), and their bounded right-\(R\) columns have coefficients

\[
\begin{gathered}
C_R(\xi_i,\xi_j)=\delta_{ij}z_i,\\
b_{ij}(u)e=v_i^*uv_j,\\
b_{ij}(u)\in z_iRz_j,\\
c_q=\operatorname{Tr}(q)=\sum_i\tau(z_i),\\
\|uqu^*-q\|_2^2\\
=2c_q-2\sum_{i,j}\|b_{ij}(u)\|_2^2.
\end{gathered}
\tag{73.14}
\]

If \(k\geq K\) on its support, then \(z_1=\cdots=z_K\).

**Proof.** For each integer value \(h\) of \(k\), precisely the first \(h\) indicators in (73.12) equal 1. This proves their sum and nesting by spectral calculus. Prescribe \(q_1\leq q\) with dimension \(z_1\). In the remainder prescribe \(q_2\) with dimension \(z_2\), and continue. At step \(i\), the remaining dimension is \((k-i+1)_+\), which is at least \(z_i\). Thus 52.4 applies at every step. After \(L\) steps the remainder has dimension zero and vanishes. The same lemma makes \(q_i\) equivalent to \(ez_i\), so choose the stated partial isometries. Orthogonal final projections give every off-diagonal product in (73.13) equal to zero.

Both \(N\) and \(e\) preserve \(L^2(N)\), by the core square 52.1. Thus the whole algebra \(A\) preserves it, and the vectors belong to \(L^2(N)\). The right-\(R\) column property and corner coefficients are those in 53.3. On \(eH\), the initial projection \(ez_i\) acts by the smaller-core element \(z_i\); hence \(\xi_i z_i=\xi_i\). The initial trace gives their squared norms. Finally expand the overlap \(\operatorname{Tr}(ququ^*)\) using \(q=\sum_i v_iv_i^*\), and move the finite column products into their \(e\)-corners by trace-class cyclicity. It equals \(\sum_{i,j}\|b_{ij}(u)\|_2^2\). Expanding the difference of two projections with the same trace proves the last line of (73.14). The claim about the first \(K\) supports is immediate from (73.12). \(\square\)

## A fixed finite algebra permits unequal supports

**Lemma 73.4 — bounded normalization in a diagonal support corner.** Let \(F\subset M\) be finite dimensional, put \(F_N=F\cap N\), and assume \(E_F(N)\subset F_N\). Let \(f_i\in F_N\) be projections, with zeros allowed. Suppose \(\eta_i\in L^2(N)f_i\) satisfy

\[
E_F(\eta_i^*\eta_j)=\delta_{ij}f_i.
\tag{73.15}
\]

There are bounded \(a_i\in Nf_i\), arbitrarily close to these vectors in \(L^2\), with the same Gram matrix. For every fixed finite family of contractions \(u\in M\), all \(F\)-coefficients converge in operator norm. No equality among the \(f_i\) is required.

**Proof.** Put \(P=\operatorname{diag}(f_1,\ldots,f_L)\in M_L(F_N)\). If \(P=0\), all vectors are zero and the assertion holds with \(a_i=0\). Otherwise choose bounded \(y_i\in Nf_i\) with maximum \(L^2\) error \(t\to0\). Their positive Gram matrix \(G=(E_F(y_i^*y_j))\) belongs to \(PM_L(F_N)P\), whose unit is \(P\). Positivity follows by applying the positive expectation to \((\sum_i y_ic_i)^*(\sum_j y_jc_j)\) for matrix-block coefficients. Bimodularity gives \(G=PGP\).

The finite coefficient bound 53.2 gives \(\gamma=\|G-P\|\to0\), since \(F\) and \(L\) are fixed. For \(\gamma<1/2\), \(G\) is invertible in that corner. Let \(Y=(y_1,\ldots,y_L)\) and set

\[
\begin{gathered}
(a_1,\ldots,a_L)=YG^{-1/2},\\
G^{-1/2}GG^{-1/2}=P,\\
\|G^{-1/2}-P\|\leq2\gamma.
\end{gathered}
\tag{73.16}
\]

Each entry of the inverse square root is in \(f_iF_Nf_j\), so \(a_j=a_jf_j\) and every entry remains in \(N\). Bimodularity proves its exact Gram matrix \(P\). If \(T=\max_i\|\eta_i\|_2\), then

\[
\begin{gathered}
\max_j\|a_j-\eta_j\|_2\\
\leq t+2\gamma L(T+t)\\
\longrightarrow0.
\end{gathered}
\tag{73.17}
\]

Indeed each column difference has at most \(L\) terms, with coefficient norms at most \(2\gamma\). The final coefficient assertion follows from 53.2 at this fixed \(F\). Functional calculus uses the diagonal projection as unit; it never completes a missing support to \(1\). \(\square\)

## Finite-stage central flags preserve the total energy

For the tunnel of the core containing \(q\), put \(A_m=N_m'\cap M\), \(B_m=N_m'\cap N\), as in (53.1).

**Theorem 73.5 — bounded finite-stage flag frames.** Let \(q\) and its columns be as in 73.3. Fix finitely many \(M\)-unitaries \(U\). For every \(a>0\), some stage \(m\) admits nested central projections \(f_1\geq\cdots\geq f_L\) in \(Z(B_m)\), bounded \(a_i\in Nf_i\), and

\[
\begin{gathered}
\sum_i\|f_i-z_i\|_2^2<a^2c_q,\\
E_{B_m}(a_i^*a_j)=\delta_{ij}f_i,\\
s_f=\sum_i\tau(f_i)>0,\\
\mathcal E_m(a,u)\\
=2s_f-2\sum_{i,j}\\
\|E_{A_m}(a_i^*ua_j)\|_2^2\geq0,\\
\left|\begin{gathered}
\frac{\mathcal E_m(a,u)}{s_f}\\
-\frac{\|uqu^*-q\|_2^2}{c_q}
\end{gathered}\right|<a,\\
u\in U.
\end{gathered}
\tag{73.18}
\]

If the first \(K\) supports \(z_i\) agree, the first \(K\) projections \(f_i\) agree as well. In particular relative Følner implies bounded flag frames with arbitrarily small normalized energies and arbitrarily small aggregate central-support error.

**Proof.** The expectations \(E_{B_m}\) converge to \(E_S\) in \(L^2\), by 53.1. Set

\[
\begin{gathered}
\lambda_{i,m}=E_{B_m}(z_i)\in Z(B_m),\\
f_{i,m}=1_{[1/2,1]}(\lambda_{i,m}),\\
\lambda_{i,m}\geq\lambda_{i+1,m}.
\end{gathered}
\tag{73.19}
\]

Centrality follows because \(z_i\) commutes with \(B_m\). The expectations are ordered; their central spectral projections are therefore nested. Equal \(z_i\) give equal \(\lambda_{i,m}\) and equal \(f_{i,m}\). Also \(z_i\) and \(\lambda_{i,m}\) commute, since \(\lambda_{i,m}\in S\) and \(z_i\in Z(S)\). On the disagreement between the two projections \(z_i\) and \(f_{i,m}\), the absolute difference \(|z_i-\lambda_{i,m}|\) is at least \(1/2\). Hence

\[
\begin{gathered}
\|z_i-f_{i,m}\|_2\\
\leq2\|z_i-\lambda_{i,m}\|_2\\
\longrightarrow0.
\end{gathered}
\tag{73.20}
\]

Inverses below are taken only on \(f_{i,m}\), with zero elsewhere. Define columns and vectors by right multiplication:

\[
\eta_{i,m}=\xi_i f_{i,m}\lambda_{i,m}^{-1/2}.
\tag{73.21}
\]

The multiplier is in \(S\), has norm at most \(\sqrt2\), and the associated bounded right-\(R\) column is \(v_i f_{i,m}\lambda_{i,m}^{-1/2}e\). Multiplying a column on the right here means composing its map on \(L^2(R)\) with left multiplication by that element. It remains in \(Be\), has norm at most \(\sqrt2\), and sends \(\widehat1\) to (73.21). We do not identify this map with right multiplication on all of \(L^2(M)\).

The coefficient identity (53.9), its bimodularity and \(E_{A_m}|_N=E_{B_m}\) show

\[
E_{A_m}(\eta_{i,m}^*\eta_{j,m})
=\delta_{ij}f_{i,m}.
\tag{73.22}
\]

Indeed the uncut coefficient is \(\delta_{ij}E_{A_m}(z_i)=\delta_{ij}\lambda_{i,m}\). Thus the vector Gram matrix is exact at this stage. For each vector, its right-\(S\) norm pairing is determined by \(z_i\). Expectation adjointness, with \(f_{i,m}\) and the inverse in \(B_m\), gives the precise error

\[
\begin{gathered}
\|\eta_{i,m}-\xi_i\|_2^2\\
=\tau(z_i(1-f_{i,m}))\\
+\tau\bigl(f_{i,m}(1-\sqrt{\lambda_{i,m}})^2\bigr)\\
\leq\tau(z_i(1-f_{i,m}))\\
+\tau(f_{i,m}(1-z_i))\\
=\|z_i-f_{i,m}\|_2^2\\
\longrightarrow0.
\end{gathered}
\tag{73.23}
\]

The scalar inequality used is \((1-\sqrt t)^2\leq1-t\) for \(0\leq t\leq1\). Thus the column norms stay uniformly bounded while their vector norms converge.

Put \(d_{ij,m}(u)=E_{A_m}(\eta_{i,m}^*u\eta_{j,m})\). The dimension-independent column estimate 53.3 and \(L^2\) contraction of expectations give

\[
\begin{gathered}
\|d_{ij,m}(u)-b_{ij}(u)\|_2\\
\leq\sqrt2\|\eta_{i,m}-\xi_i\|_2\\
+\|\eta_{j,m}-\xi_j\|_2\\
+\|E_{A_m}(b_{ij})-b_{ij}\|_2\\
\longrightarrow0.
\end{gathered}
\tag{73.24}
\]

In the last line the argument \(u\) of \(b_{ij}\) is suppressed. For the first term keep the second column \(\eta_{j,m}\), whose norm is at most \(\sqrt2\). For the second keep the first column \(\xi_i\), whose norm is at most 1, and use the adjoint estimate. The last term tends to zero because \(b_{ij}(u)\in R\) and the \(A_m\) have dense union there. All finitely many indices and unitaries can be handled at the same stage. Together with \(\sum_i\tau(f_{i,m})\to c_q\), (73.14) proves convergence of the vector energies divided by their total mass to the desired ratios.

Choose a sufficiently late stage with positive total mass, aggregate support error below \(a^2c_q\), and normalized energy differences strictly below \(a/2\). Now fix that stage; apply Lemma 73.4 with \(F=A_m\), \(F_N=B_m\) and vectors \(\eta_{i,m}\). Choose its bounded approximants sufficiently close that each normalized energy changes by less than \(a/2\). Restriction (53.2) identifies the exact Gram matrix with the one in (73.18). No finite-dimensional coefficient constant is used while the stage is changing.

For completeness, these bounded energies are nonnegative. Put \(P=\operatorname{diag}(f_i)\) and \(C_u=(E_{A_m}(a_i^*ua_j))\). The Gram matrix of the doubled row \((a_1,\ldots,a_L,ua_1,\ldots,ua_L)\) is

\[
\begin{gathered}
\begin{pmatrix}P&C_u\\ C_u^*&P\end{pmatrix}\geq0,\\
C_u=PC_uP.
\end{gathered}
\tag{73.25}
\]

In the corner with unit \(P\), positivity tested on \((-C_ut,t)\) gives \(C_u^*C_u\leq P\). Applying the unnormalized matrix trace tensored with \(\tau\) gives \(\sum_{i,j}\|E_{A_m}(a_i^*ua_j)\|_2^2\leq s_f\). This proves nonnegativity and finishes (73.18).

Finally use 73.2 with a smaller tolerance, then 73.5 with \(a\) small enough. Formula (73.14) supplies the small original energy, and (73.18) preserves it to any prescribed accuracy. This proves the stated unconditional bounded-flag consequence. \(\square\)

## Exact arithmetic and the common-support boundary

For a finite central arithmetic example, take three base atoms of measures \(1/2,1/3,1/6\), and initial dimensions \(5/4,7/3,13/5\). A square amplification by 4 gives dimensions

\[
\begin{gathered}
f=(5,28/3,52/5),\\
k=(5,9,10),\\
\int f\,d\nu=661/90,\\
\int k\,d\nu=43/6,\\
\int(f-k)\,d\nu=8/45,\\
\frac{\int(f-k)\,d\nu}{\int f\,d\nu}=16/661.
\end{gathered}
\tag{73.26}
\]

The first five flag projections are \((1,1,1)\), the next four are \((0,1,1)\), and the tenth is \((0,0,1)\). Their measures sum to \(5+4/2+1/6=43/6\). This is central arithmetic, not a claimed model of an actual Jones core.

It is still invalid to split the total Følner estimate into separate estimates on the level sets of \(k\). Here is an exact finite matrix warning. Fix a positive integer \(k\). On \(\mathbb C^{k+1}\oplus\mathbb C^{k+1}\), take the block diagonal algebra, use scalar trace one half of ordinary matrix trace, put \(p=I_{k+1}\oplus(I_k\oplus0)\), and let \(u\) interchange the two blocks. Then

\[
\begin{gathered}
\operatorname{Tr}(p)=(2k+1)/2,\\
\|upu^*-p\|_2^2=1,\\
\frac{\|upu^*-p\|_2^2}{\operatorname{Tr}(p)}=\frac2{2k+1},\\
\sum_{j=1}^2\|u(pz_j)u^*-pz_j\|_2^2\\
=2k+1.
\end{gathered}
\tag{73.27}
\]

Here \(z_1,z_2\) are the two disjoint block-center projections, rather than the nested flag projections. The two localized squared-defect ratios are both 2. They do not inherit the small whole-projection ratio. The example is finite dimensional and is not an actual-core counterexample. Indeed deleting the one extra rank gives the commuting projection \(I_k\oplus I_k\); the example does not refute constant-multiplicity rounding.

Theorems 73.1–73.5 therefore provide a bounded integer function and bounded central-flag frames from unrestricted relative Følner. They do **not** supply a scalar integer multiple of one support, the common-support bounded-frame property BF in 57, or the general conclusion of Popa 4.2.2. Passing from these flags to a sufficient general local approximation theorem remains a mathematical obligation. The averaging hypothesis 72.12 and controlled-band hypothesis 71.14 are not asserted here.

## Exercises with complete solutions

### Exercise 73.1 — a zero density region (basic)

Why does dominated convergence in (73.5) work even if \(\zeta\) vanishes on a set of positive measure? Why can one impose \(K\geq1\) without losing all of \(p\)?

**Solution.** The integrand is zero wherever \(\zeta=0\). Where \(\zeta>0\), the inequality \(n^2\zeta<K\) eventually fails. The integrands are bounded by the integrable function \(\zeta\), so their integrals tend to zero. The three losses in (73.8) are less than \(rc'\), with \(r<1\); hence the retained projection has positive trace. Amplification raises the positive dimensions before the minimum is imposed.

### Exercise 73.2 — one perturbation controls all tests (intermediate)

Let \(m=4\), \(\varepsilon=1/10\), \(\delta_U(p)<\varepsilon/4\), and choose \(r=1/102400\). Verify the bound in (73.4) is less than \(\varepsilon/2\).

**Solution.** This is \(r=\varepsilon^2/(256m)\). Thus \(\sqrt{mr}=1/160\), and the numerator is strictly less than \(1/40+1/80=3/80\). The denominator is greater than \(3/4\), so the ratio is strictly less than \((3/80)/(3/4)=1/20=\varepsilon/2\). The estimate uses the direct-sum norm, so it controls all four tests at once.

### Exercise 73.3 — the central flag (basic)

Compute the nested flag and its total mass for (73.26). Is the integer dimension a scalar multiple of its support?

**Solution.** For \(1\leq i\leq5\), \(z_i=(1,1,1)\). For \(6\leq i\leq9\), \(z_i=(0,1,1)\). Finally \(z_{10}=(0,0,1)\). Their measures are respectively 1, \(1/2\) and \(1/6\); the sum is \(5+4/2+1/6=43/6\). All three atoms are in the support, but the values of the integer dimension there are 5, 9 and 10, so no one scalar integer works.

### Exercise 73.4 — normalize unequal supports (intermediate)

Let \(f_1=1\), \(f_2=z\), \(f_3=0\) in a finite algebra, where \(z\) is a projection. What is the unit of the Gram-matrix corner in 73.4? Why must its inverse square root be taken there?

**Solution.** The unit is \(P=\operatorname{diag}(1,z,0)\). The Gram matrix vanishes on \(1-P\), so it cannot be invertible in the full three-by-three algebra. If \(\|G-P\|<1/2\), it is invertible on \(P\), which is precisely the support needed. The normalized row has second entry supported on \(z\) and third entry zero. Treating the full identity as its unit would introduce unsupported coordinates and would not prove the desired Gram identity.

### Exercise 73.5 — threshold and vector error (advanced)

Explain why the stage thresholds in (73.19) preserve nesting. Derive the inequality in (73.23), rather than assuming \(L^2\) continuity of inverse square roots at zero.

**Solution.** The ordered expectations are central in \(B_m\), so they commute. On every central spectral value, thresholding two ordered numbers at the same value \(1/2\) preserves their order. The inverse square root is used only where the expectation is at least \(1/2\). Off that support, the squared vector loss is \(\tau(z_i(1-f_i))\). On it, expectation adjointness turns the squared multiplier error into \(\tau(f_i(1-\sqrt{\lambda_i})^2)\). Since \((1-\sqrt t)^2\leq1-t\) on \([0,1]\), that is at most \(\tau(f_i(1-\lambda_i))=\tau(f_i(1-z_i))\). Adding both terms gives \(\|z_i-f_i\|_2^2\). No inverse is taken near zero.

### Exercise 73.6 — what the finite matrix warning says (advanced)

Prove (73.27), find a commuting projection close to \(p\), and identify the remaining general theorem after 73.5.

**Solution.** The two projections \(p,upu^*\) differ on exactly two coordinate lines, so their squared difference has trace 1 in the stated trace. The trace of \(p\) is \((2k+1)/2\). Each block cut has an image under \(u\) orthogonal to itself; its squared defect is twice its trace, giving localized ratios 2 and summed defect \(2\operatorname{Tr}(p)=2k+1\). The projection \(q=I_k\oplus I_k\), using the first \(k\) coordinates in both blocks, commutes with \(u\) and is below \(p\). Its loss is \(1/2\), a fraction \(1/(2k+1)\) of the original trace. The warning therefore rejects an automatic spectral-piece estimate, not constant-multiplicity rounding itself. In the general course argument one still needs common-support rounding/BF or a proved local-approximation route that can use the unequal central flag. 73.5 proves the flag input only.

![Whole projection rounding and a variable central support flag](figures/variable-integer-dimensions-and-central-flags.svg)

**Figure 73.1.** The three central atoms have measures \(1/2,1/3,1/6\). Their amplified dimensions, floors, fractional losses and nested supports are the exact values in (73.26) and Exercise 73.3. The solid arrows are the proved implications 73.1–73.5. The dashed arrow to a common support is an unresolved additional implication. The drawing shows central arithmetic, not actual core geometry. [Editable source](figures/variable-integer-dimensions-and-central-flags.py).

Author self-check. The full course goal remains active and incomplete.
