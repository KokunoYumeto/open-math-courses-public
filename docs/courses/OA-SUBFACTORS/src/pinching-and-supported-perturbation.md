# Pinching errors and completing supported frames

Two operations will turn the bounded relative frames of the preceding lesson into small finite-dimensional corners. **Pinching** removes off-diagonal blocks by refining a projection partition. **Supported perturbation** replaces an approximate frame by partial isometries with exactly orthogonal ranges. This lesson proves both operations, including the support and trace conditions needed for the second one.

The full local quantization theorem, which produces a projection with small *relative* compression errors and arbitrary small trace, is proved in Theorem 55.7 of [Finite Fourier bases produce one small quantized corner](finite-phase-local-quantization.md) and Theorem 56.5 of [Central dimensions and a common quantized corner](central-dimensions-and-local-quantization.md). Proposition 54.6 below isolates how the relative compression estimate supplies the trace capacity needed here. [Supported frames give local approximation corners](actual-supported-local-approximation.md), Theorem 57.2, uses these proved operations on the actual support.

We use polar decomposition, continuous functional calculus, the tracial expectation theorem, and finite-factor projection comparison. The trace comparison and central-support facts are the specializations of Theorem 5.2, Corollary 5.4 and Lemma 6.1 in Traces on von Neumann algebras. The least-norm orbit mechanism was proved in Proposition 15.2 of [Detecting a generating tunnel](detecting-a-generating-tunnel.md). We spell out its simultaneous use below. These relative proofs keep the course's general transitive prerequisites separate.

All inclusions are unital. Traces are faithful, normal and normalized; \(\|x\|_2^2=\tau(x^*x)\). Inner products are linear in the second variable.

## Polar completion with a prescribed range

**Lemma 54.1.** Let \(M\) be a finite factor and \(p,q\in M\) projections with \(\tau(p)\geq\tau(q)\). If \(y\in pMq\), there is a partial isometry \(v\in pMq\) such that
\[
\begin{gathered}
v^*v=q,\qquad vv^*\leq p,\\
\|v-y\|_2\leq\|y^*y-q\|_2.
\end{gathered}
\tag{54.1}
\]

**Proof.** Write \(h=y^*y\in qMq\) and \(y=wh^{1/2}\). The initial projection of \(w\) is \(s=s(h)\leq q\), and \(ww^*\leq p\). The available range has trace
\[
\begin{aligned}
\tau(p-ww^*)&=\tau(p)-\tau(s)\\
&\geq\tau(q-s).
\end{aligned}
\tag{54.2}
\]
Projection comparison supplies \(w_1\) with initial projection \(q-s\) and final projection below \(p-ww^*\). If \(q=s\), take \(w_1=0\). The initial and final supports of \(w,w_1\) are orthogonal, so \(v=w+w_1\) has the required supports.

The two summands of \(v-y=w(s-h^{1/2})+w_1\) are orthogonal in \(L^2\). Consequently
\[
\begin{aligned}
\|v-y\|_2^2
&=\tau((s-h^{1/2})^2)\\
&\quad+\tau(q-s)\\
&=\tau((q-h^{1/2})^2).
\end{aligned}
\tag{54.3}
\]
For every \(\lambda\geq0\),
\[
|\sqrt{\lambda}-1|\leq|\lambda-1|.
\tag{54.4}
\]
Apply functional calculus in the corner with unit \(q\), including the zero part \(q-s\), and then the positive trace. This gives (54.1). The constant one is sharp: if \(y=0\) and \(q\ne0\), both sides are \(\sqrt{\tau(q)}\). \(\square\)

The zero spectral part is completed rather than discarded. The estimate therefore concerns the original \(q\), not a smaller spectral support.

## A bounded approximate frame has an exact supported replacement

**Theorem 54.2.** Let \(M\) be a \(\mathrm{II}_1\) factor, \(q\ne0\) a projection, and \(n\geq1\). Suppose
\[
n\tau(q)\leq1,\qquad y_i=y_iq\in M.
\tag{54.5}
\]
Put \(L=\max(1,\max_i\|y_i\|)\). If \(\eta\geq0\) and
\[
\begin{gathered}
\|y_i^*y_j-\delta_{ij}q\|_2
\leq\eta\sqrt{\tau(q)},\\
1\leq i,j\leq n,
\end{gathered}
\tag{54.6}
\]
there are \(v_i\in Mq\) with
\[
v_i^*v_j=\delta_{ij}q.
\tag{54.7}
\]
Writing \(A=L^2+2L+3\), they satisfy
\[
\max_i\|v_i-y_i\|_2
\leq A^{n-1}\eta\sqrt{\tau(q)}.
\tag{54.8}
\]
For every contraction \(u\in M\), also
\[
\begin{gathered}
\|v_i^*uv_j-y_i^*uy_j\|_2\\
\leq(1+L)A^{n-1}\eta\sqrt{\tau(q)}.
\end{gathered}
\tag{54.9}
\]

**Proof.** Lemma 54.1 with \(p=1\) gives \(v_1\) and error constant \(c_1=1\). Suppose \(v_1,\ldots,v_k\) have been chosen with (54.7) and
\[
\|v_j-y_j\|_2\leq c_j\eta\sqrt{\tau(q)}.
\]
For \(y=y_{k+1}\), put
\[
\begin{gathered}
P=\sum_{j=1}^k v_jv_j^*,\\
p=1-P,\qquad \widetilde y=py.
\end{gathered}
\tag{54.10}
\]
The summands of \(P\) are orthogonal projections. Thus
\[
\begin{aligned}
\tau(p)&=1-k\tau(q)\\
&\geq(n-k)\tau(q)\geq\tau(q).
\end{aligned}
\tag{54.11}
\]
This is exactly the range capacity required by Lemma 54.1.

Set \(t=\eta\sqrt{\tau(q)}\). Since \(j\ne k+1\), the input and the previous error bound imply
\[
\begin{aligned}
\|v_j^*y\|_2
&\leq\|y_j^*y\|_2\\
&\quad+\|(v_j-y_j)^*y\|_2\\
&\leq(1+Lc_j)t.
\end{aligned}
\tag{54.12}
\]
Let \(S_k=\sum_{j=1}^k c_j\). Since \(\|y^*v_j\|\leq L\), write
\[
G_k=\|\widetilde y^*\widetilde y-q\|_2.
\]
Then
\[
\begin{aligned}
G_k&\leq\|y^*y-q\|_2\\
&\quad+\|y^*Py\|_2\\
&\leq(1+kL+L^2S_k)t.
\end{aligned}
\tag{54.13}
\]
Here we expanded \(y^*Py=\sum_j(y^*v_j)(v_j^*y)\) and used \(\|ab\|_2\leq\|a\|\|b\|_2\) term by term.

Apply Lemma 54.1 to \(\widetilde y\in pMq\). Its output \(v_{k+1}\) has initial projection \(q\) and range orthogonal to the preceding ranges. Also, orthogonality of those ranges gives
\[
\begin{aligned}
\|Py\|_2^2&=\sum_j\|v_j^*y\|_2^2,\\
\|Py\|_2&\leq(k+LS_k)t.
\end{aligned}
\]
The triangle inequality now proves the induction with
\[
\begin{aligned}
c_{k+1}&=1+k(L+1)\\
&\quad+(L^2+L)S_k.
\end{aligned}
\tag{54.14}
\]
All \(c_j\geq1\). Hence \(1+k(L+1)\leq(L+2)S_k\), and
\[
c_{k+1}\leq(A-1)S_k.
\tag{54.15}
\]
Inductively \(c_j\leq A^{j-1}\): the geometric sum yields
\[
\begin{aligned}
c_{k+1}
&\leq(A-1)\sum_{j=1}^k A^{j-1}\\
&=A^k-1<A^k.
\end{aligned}
\]
This proves (54.8), including \(\eta=0\). Finally expand
\[
\begin{aligned}
v_i^*uv_j-y_i^*uy_j
&=(v_i-y_i)^*uv_j\\
&\quad+y_i^*u(v_j-y_j).
\end{aligned}
\]
The bounds \(\|v_j\|=1\), \(\|u\|\leq1\), \(\|y_i\|\leq L\) and (54.8) give (54.9). \(\square\)

The capacity condition is necessary for any output: the \(n\) orthogonal range projections all have trace \(\tau(q)\). Right support is necessary for this linear error estimate. A small Gram error alone can conceal a larger component on \(1-q\).

**Example 54.3 — two missing hypotheses in the printed perturbation lemma.** Let \(W\) be any \(\mathrm{II}_1\) factor. In \(M=M_2(\mathbb C)\bar\otimes W\), suppress tensor units and set
\[
\begin{gathered}
q=E_{11},\\
y=q+\tfrac1{1000}(1-q),\\
\varepsilon=\tfrac1{100000}.
\end{gathered}
\tag{54.16}
\]
Then \(\|y\|=1\), and
\[
\frac{\|y^*y-q\|_2}{\sqrt{\tau(q)}}
=10^{-6}<\varepsilon.
\]
For \(n=1\), the constant printed in Popa's Lemma A.2.1 is
\[
\alpha_0=3,\qquad
\beta_0=\alpha_0^4(\alpha_0^2+1)^{-1}
=\tfrac{81}{10}.
\]
Every \(v\) with \(v^*v=q\) has \(v=vq\). Right multiplication by \(1-q\) is an \(L^2\) contraction, so
\[
\begin{gathered}
\|v-y\|_2\geq10^{-3}\sqrt{\tau(q)},\\
10^{-3}>\tfrac{81}{10}\varepsilon.
\end{gathered}
\tag{54.17}
\]
This contradicts the literal printed distance bound when no right-support hypothesis is imposed.

For an independent capacity obstruction, take \(M=M_{100}(\mathbb C)\bar\otimes W\) and
\[
\begin{gathered}
q=\sum_{j=1}^{51}E_{jj},\qquad y_1=q,\\
y_2=\sum_{j=1}^{51}E_{j+49,j},\qquad
\varepsilon=\tfrac15.
\end{gathered}
\tag{54.18}
\]
Both inputs have right support \(q\). Their diagonal Gram entries are exactly \(q\), and each off-diagonal entry has squared \(L^2\)-norm \(2/100\). Nevertheless
\[
\begin{gathered}
\varepsilon\leq\tfrac12,\\
\tfrac2{100}<\varepsilon^2\tau(q),\\
\varepsilon^2\tau(q)=\tfrac{51}{2500},\\
2\tau(q)=\tfrac{102}{100}>1.
\end{gathered}
\tag{54.19}
\]
The Gram hypothesis is strict, but two orthogonal ranges equivalent to \(q\) cannot exist. These tensor products are \(\mathrm{II}_1\) factors, so the examples lie within the printed algebra type. They refute the unrestricted printed lemma, not the local approximation theorem that uses it: that application starts with \(y_i=a_iq\) and can arrange sufficiently small \(q\). The corrected theorem above supplies the needed version.

## Corner commutants glue even when the smaller algebra has a center

For the pinching argument let \(B\subset M\) be finite von Neumann algebras. They need not be factors. Put
\[
C=B'\cap M,\qquad D=B\vee C.
\tag{54.20}
\]

**Lemma 54.4.** If \(p_1,\ldots,p_r\in B\) are orthogonal projections with sum \(1\), and \(B_{\mathcal P}=\bigoplus_i p_iBp_i\), then
\[
B_{\mathcal P}'\cap M
=\bigoplus_i p_iCp_i\subset D.
\tag{54.21}
\]

**Proof.** We first lift an element \(a\in(pBp)'\cap pMp\) to \(C\). Let \(z=c_B(p)\). Starting with \(u_1=p\), choose a maximal family of partial isometries \(u_j\in B\) whose initial projections \(d_j=u_j^*u_j\) lie below \(p\) and whose final projections are orthogonal. Their strong sum is \(z\). Indeed, a nonzero residual projection \(r\leq z\) has \(rBp\ne0\): otherwise it annihilates the closed span of \(BpH\), whose projection is the central support \(z\). The polar part of a nonzero \(rbp\) could then be added, contradicting maximality. Faithfulness and finiteness of \(\tau\) make the nonzero final projections countable.

Since \(a\) commutes with each \(d_j\), the orthogonal block sum
\[
c=\sum_j u_j a u_j^*
\tag{54.22}
\]
converges strongly and has norm at most \(\|a\|\). It is supported on \(z\). For \(b\in B\), every matrix entry \(u_i^*bu_j\) belongs to \(pBp\), and
\[
u_i^*(cb-bc)u_j
=a(u_i^*bu_j)-(u_i^*bu_j)a=0.
\]
The final projections sum to \(z\); hence the compression of this commutator to \(z\) is zero. Both its off-\(z\) blocks are zero because \(z\in Z(B)\) and \(c=zc\). Therefore \(c\in C\). Since \(u_1=p\) and all other final projections are orthogonal to \(p\), we have \(cp=pc=a\).

An element commuting with \(B_{\mathcal P}\) commutes with every \(p_i\), so is block diagonal. Apply the lifting just proved to each block. This gives the forward inclusion in (54.21). Conversely, \(p_i c p_i\) with \(c\in C\) commutes with the corresponding \(p_iBp_i\) and with all other blocks. Finally \(p_i c p_i=p_i c\in D\), proving the last inclusion. \(\square\)

## One refinement reduces all squared errors together

For a partition \(\mathcal P=(p_i)\) define its pinching map
\[
\Phi_{\mathcal P}(x)=\sum_i p_i x p_i.
\tag{54.23}
\]
It is the \(L^2\) orthogonal projection onto the block diagonal algebra \(\bigoplus_i p_iMp_i\). Refinement therefore cannot increase its \(L^2\)-norm.

**Theorem 54.5 — simultaneous pinching.** Let \(X\subset M\) be finite with \(E_D(x)=0\) for every \(x\in X\). From any prescribed finite partition \(\mathcal P\) in \(B\), and for every \(\eta>0\), there is a finite refinement \(\mathcal Q\) in \(B\) such that
\[
\|\Phi_{\mathcal Q}(x)\|_2<\eta
\quad(x\in X).
\tag{54.24}
\]
If the current total energy is nonzero, one refinement can reduce it by a factor strictly smaller than \(3/4\):
\[
\begin{gathered}
\mathcal E(\mathcal P)=
\sum_{x\in X}\|\Phi_{\mathcal P}(x)\|_2^2,\\
\mathcal E(\mathcal Q)<\tfrac34\mathcal E(\mathcal P).
\end{gathered}
\tag{54.25}
\]

**Proof.** Write \(X_x=\Phi_{\mathcal P}(x)\). Bimodularity of \(E_D\), since \(p_i\in D\), gives \(E_D(X_x)=0\). Consider the tuple \((X_x)_{x\in X}\) in the finite Hilbert direct sum of copies of \(L^2(M)\). Conjugate all its entries by the *same* unitary of \(B_{\mathcal P}\), and take the norm-closed convex hull.

This hull has a unique vector of least norm. Invariance under conjugation makes every component of that vector commute with \(B_{\mathcal P}\). Its components are bounded elements of \(M\): every orbit component and every convex combination has norm at most \(\|X_x\|\); a weak-* convergent subnet and trace pairing identify any \(L^2\) limit with a bounded element having that same bound. Each component also remains in \(\ker E_D\). Lemma 54.4 puts a bounded fixed component in \(D\). It must therefore be zero. Thus the zero tuple belongs to the hull.

Let \(E=\mathcal E(\mathcal P)>0\). Some \(u\in\mathcal U(B_{\mathcal P})\) satisfies
\[
\sum_x\|uX_xu^*-X_x\|_2^2>E.
\tag{54.26}
\]
Otherwise, expanding every displacement gives
\[
\operatorname{Re}\sum_x
\langle X_x,uX_xu^*\rangle\geq E/2
\]
throughout the orbit and its closed convex hull, contradicting the zero tuple.

Approximate \(u\) in operator norm by a finite-spectral unitary
\[
\begin{gathered}
u_0=\sum_{j=1}^{s}\lambda_j e_j\in B_{\mathcal P},\\
|\lambda_j|=1,
\end{gathered}
\tag{54.27}
\]
closely enough to preserve (54.26). Such an approximation follows by partitioning the circle into finitely many short arcs and using their spectral projections. Each \(e_j\) commutes with every old \(p_i\).

The blocks \(e_i X_x e_j\) are mutually orthogonal in \(L^2\). The diagonal ones disappear from the displacement. Set
\[
\begin{gathered}
J_0=\sum_x\|u_0X_xu_0^*-X_x\|_2^2,\\
T_0=\sum_x\left\|\sum_j e_jX_xe_j\right\|_2^2,\\
d_{ij}=|\lambda_i\overline{\lambda_j}-1|^2\leq4.
\end{gathered}
\]
Then
\[
\begin{aligned}
J_0&=\sum_{x,i,j}d_{ij}\|e_iX_xe_j\|_2^2\\
&\leq4(E-T_0).
\end{aligned}
\tag{54.28}
\]
Combining this with the strict lower bound \(E\) proves a \(3E/4\) upper bound for the new energy. The nonzero projections \(e_jp_i\) form a finite refinement \(\mathcal Q\) of \(\mathcal P\), and
\[
\Phi_{\mathcal Q}(x)=\sum_j e_jX_xe_j.
\tag{54.29}
\]
Thus (54.25) follows. If the energy is zero, the current partition already works.

Starting at the prescribed partition, iterate until
\[
(3/4)^k\sum_{x\in X}\|x\|_2^2<\eta^2.
\tag{54.30}
\]
Pinching is contractive, so this bounds the resulting total energy. Every individual norm is then less than \(\eta\). Empty \(X\) needs no refinement. \(\square\)

The norm itself contracts by \(\sqrt{3}/2\), as a valid upper bound, when one treats a single nonzero target. The \(3/4\) estimate is for its **square**, or for the summed energy in (54.25). Popa's Lemma A.1.1, Step 2, initially displays an unsquared \(3/4\) estimate on; the calculation on pages 245–246 supplies the squared estimate used here. The existence conclusion remains valid with this proof.

## How quantization supplies the trace capacity

**Proposition 54.6 — a conditional small-trace refinement.** Suppose \(B\subset M\) are \(\mathrm{II}_1\) factors and the local quantization conclusion has been established: for every finite \(Y\subset M\) and \(\delta>0\), some nonzero \(q\in B\) satisfies
\[
\begin{gathered}
\|qyq-E_C(y)q\|_2<\delta\sqrt{\tau(q)},\\
y\in Y.
\end{gathered}
\tag{54.31}
\]
Then for every \(\eta,t_0>0\) the same conclusion at tolerance \(\eta\) can be obtained with \(0<\tau(q)\leq t_0\).

**Proof.** If \(Y\) is empty, choose any nonzero projection of sufficiently small trace, using the continuous dimension of a \(\mathrm{II}_1\) factor. Otherwise put \(K=|Y|\) and apply (54.31) with \(\delta=\eta/\sqrt K\). For the resulting \(q\), write \(a_y=qyq-E_C(y)q\). Then
\[
\sum_{y\in Y}\|a_y\|_2^2<\eta^2\tau(q).
\tag{54.32}
\]
Split \(q\) inside \(B\) into finitely many equal-trace nonzero projections \(q_j\), each of trace at most \(t_0\). This uses projection dimension and comparison, not quantization. Because \(E_C(y)\) commutes with \(B\),
\[
q_jyq_j-E_C(y)q_j=q_j a_y q_j.
\]
Orthogonal pinching is contractive, giving
\[
\begin{gathered}
\sum_{j,y}\|q_j a_y q_j\|_2^2\\
\leq\sum_y\|a_y\|_2^2
<\eta^2\sum_j\tau(q_j).
\end{gathered}
\tag{54.33}
\]
At least one \(q_j\) has summed target error strictly less than \(\eta^2\tau(q_j)\). Choose that one. Every target individually meets the required bound on this **same** projection. \(\square\)

Taking \(t_0=1/n\) ensures (54.5). In the tunnel application the actual initial projection can be \(fq\), where \(f\ne0\) commutes with the quantizing factor \(B\). Trace pairing gives \(E_B(f)=\tau(f)1\), because that expectation is central in \(B\). Therefore
\[
\tau(fq)=\tau(f)\tau(q).
\tag{54.34}
\]
An input error bounded by \(\delta\sqrt{\tau(q)}\) is consequently bounded by
\(\delta/\sqrt{\tau(f)}\) times \(\sqrt{\tau(fq)}\). Fixing the frame and its nonzero \(f\) before choosing \(\delta\) retains this denominator. The condition \(n\tau(q)\leq1\) also implies \(n\tau(fq)\leq1\).

![Polar completion and simultaneous pinching](figures/supported-frame-pinching.svg)

**Figure 54.1.** The top panel shows the original support, the polar range, and the missing range supplied by (54.2); its matrix example is computed in Exercise 54.1. The middle panel shows why two ranges of trace \(51/100\) cannot fit under the unit, even with small Gram errors. The bottom panel shows the phase displacement, orthogonal blocks, and summed squared-energy decrease of Theorem 54.5. These are support and trace schematics, not a geometric identification of arbitrary factors. [Reproducible figure source](figures/supported-frame-pinching.py). Human source: Sorin Popa, Appendix A.1.1 and A.2.1, printed pages 244–246 and 249–251; the corrected hypotheses and bounds are proved in Lemma 54.1 and Theorem 54.2 above.

## Exercises with complete solutions

**Exercise 54.1 — complete the zero spectral part (introductory).** In \(M_4(\mathbb C)\) with normalized trace, take \(q=E_{11}+E_{22}\), \(p=E_{33}+E_{44}\), and \(y=2E_{31}\). Compute the completion from Lemma 54.1 and both squared errors. Explain why simply taking the polar part does not suffice.

**Solution.** Here \(h=4E_{11}\), \(s=E_{11}\), and \(w=E_{31}\). The missing initial projection is \(E_{22}\) and the available range is \(E_{44}\). Take \(w_1=E_{42}\). Thus \(v=E_{31}+E_{42}\), \(v^*v=q\), and \(vv^*=p\). The errors are
\[
\|v-y\|_2^2=\tfrac24=\tfrac12,\qquad
\|h-q\|_2^2=\tfrac{9+1}{4}=\tfrac52.
\]
The polar part alone has initial projection \(E_{11}\), missing \(E_{22}\). Formula (54.3) counts that missing projection. Setting \(y=0\) instead gives equality in (54.1), demonstrating sharpness of its universal constant.

**Exercise 54.2 — track the induction (intermediate).** For \(L=1,n=3\), compute \(c_1,c_2,c_3\) using (54.14), compare with (54.8), and give the resulting coefficient bound.

**Solution.** The recurrence gives \(c_1=1\), \(c_2=1+2+2=5\), and \(c_3=1+4+2(1+5)=17\). Here \(A=6\), so the convenient common bound is \(A^2=36\). Formula (54.9) gives \(72\eta\sqrt{\tau(q)}\). Retaining the actual common constant \(17\) in the last expansion improves this particular bound to \(34\eta\sqrt{\tau(q)}\). No improvement in the trace capacity follows from an improved error constant.

**Exercise 54.3 — a Gram error can miss right-support leakage (intermediate).** Verify all numerical comparisons in (54.16)–(54.17) and prove that \(v^*v=q\) implies \(v=vq\).

**Solution.** With \(t=1/1000\), \(y^*y-q=t^2(1-q)\); the two projections have equal trace \(1/2\), so its norm divided by \(\sqrt{\tau(q)}\) is \(t^2=1/10^6<1/10^5\). Also
\[
(v(1-q))^*v(1-q)=(1-q)q(1-q)=0.
\]
Hence \(v(1-q)=0\) and \((v-y)(1-q)=-t(1-q)\). The printed proposed bound has relative size
\((81/10)/100000=81/10^6\), whereas the unavoidable distance has relative size \(1000/10^6\). Their strict inequality proves the stated failure. The Gram error is quadratic in the leakage size; the necessary distance is linear in that size.

**Exercise 54.4 — count the two overlapping rows (intermediate).** For (54.18), compute both cross-Gram entries and the trace obstruction.

**Solution.** Since the ranges of \(y_2\) occupy rows \(50,\ldots,100\),
\[
y_1^*y_2=E_{50,1}+E_{51,2},\qquad
y_2^*y_1=E_{1,50}+E_{2,51}.
\]
Their squared \(L^2\)-norms are \(2/100=50/2500<51/2500=\varepsilon^2\tau(q)\). Direct multiplication gives \(y_2^*y_2=q\) and \(y_1^*y_1=q\). Two proposed exact ranges would be orthogonal, with combined trace \(2(51/100)=102/100\), impossible for a subprojection of \(1\). Tensoring with \(W\) changes neither these calculations nor the normalized traces.

**Exercise 54.5 — see the pinching mechanism in two blocks (introductory).** Let \(B\) be the diagonal algebra in \(M=M_2(\mathbb C)\), \(X=\{E_{12},E_{21}\}\), and begin with the partition \(\{1\}\). Use \(u=E_{11}-E_{22}\) to compute the displacement and the refined energy. Check the hypothesis involving \(D\).

**Solution.** Here \(C=B\) and \(D=B\), so both off-diagonal matrix units have \(E_D(x)=0\). Each has squared \(L^2\)-norm \(1/2\), and the total energy is \(E=1\). Conjugation by \(u\) sends each to its negative, giving total squared displacement \(4E=4>E\). The spectral partition of \(u\) is \(\{E_{11},E_{22}\}\); its pinching annihilates both targets. Thus the new energy is zero and (54.28) is equality with displacement \(4\). If instead \(B=M\), then \(D=M\) and these targets would fail the hypothesis.

**Exercise 54.6 — choose one piece for all targets (advanced).** In a \(\mathrm{II}_1\) factor \(B=M\), take orthogonal \(q_1,q_2\) of trace \(1/4\) and \(q=q_1+q_2\). Set
\[
y_i=\tfrac65 q_i-\tfrac35(1-q),\quad i=1,2.
\]
Show that \(q\) satisfies (54.31) at tolerance \(1\), but neither of these two pieces satisfies that tolerance for both targets. Relate this to the choice \(\eta/\sqrt K\) in Proposition 54.6.

**Solution.** Since \(C=\mathbb C1\), \(E_C(y_i)=\tau(y_i)1=0\): the positive and negative trace contributions are \(3/10\) each. We have \(qy_iq=(6/5)q_i\) and
\[
\frac{\|qy_iq\|_2^2}{\tau(q)}
=\frac{9/25}{1/2}=\tfrac{18}{25}<1.
\]
On \(q_i\) the same target has relative error \(6/5>1\); on the other piece it has error zero. Choosing a good piece separately for each target therefore produces different pieces. The summed error on either piece has relative squared size \(36/25>1\), so the given partition supplies no common piece. The stronger initial tolerance \(1/\sqrt2\) used in Proposition 54.6 would require the displayed initial relative square to be less than \(1/2\), which this example does not satisfy. Summing all targets *before* choosing a piece is what proves the proposition.

## Sources and remaining quantization work

Sorin Popa, [Classification of amenable subfactors of type II](https://doi.org/10.1007/BF02392646), *Acta Mathematica* 172 (1994), 163–255: Lemma A.1.1; Theorem A.1.2, pages 246–248; Lemma A.2.1, pages 249–251; local approximation Theorem 4.3.1, pages 217–219.

The literal A.2.1 statement omits both \(y_i=y_iq\) and \(n\tau(q)\leq1\). Its proof begins by replacing an input with its right compression, and later explicitly uses \(\tau(q)<1/n\) when extending ranges. Example 54.3 verifies failures caused by these two omissions separately. Theorem 54.2 proves the supported version with a new explicit constant and permits the capacity endpoint \(n\tau(q)=1\).

Theorem 54.5 proves finite-partition pinching, including a prescribed initial partition and simultaneous targets. Proposition 54.6 derives trace capacity from the relative quantization estimate proved in Theorems 55.7 and 56.5. Theorem 57.2 supplies transport on the actual support, and Theorem 57.4 proves the every-core converse. Theorem 58.7 and Corollary 58.8 of [Full support from a factorial larger core](larger-factor-central-balancing.md) supply the larger-core factorial bridge. General rounded-core input and the remaining unrestricted local/global/generating implications still require their full arguments.
