# Spectral cuts and localized intertwiners

Two almost commuting projections can have a join that moves abruptly. For local arguments in a standard form, a spectral projection of their sum is a useful replacement: it retains most of each projection, while its vector commutators are controlled simultaneously. We use this replacement to place an approximate intertwiner inside a pair of corresponding corners without losing its mass.

Let \((M,H,J,P)\) be a standard form. The inner product is linear in the first variable, and the right action is \(\eta a=Ja^*J\eta\). For \(\theta\in\operatorname{Aut}(M)\), write \(U_\theta\) for its canonical standard-form unitary and abbreviate \(U_\theta\xi\) to \(\theta\xi\). Thus


\[
\theta(a\xi b)=\theta(a)(\theta\xi)\theta(b),
\qquad U_\theta J=JU_\theta.
\]


These statements, including transport between arbitrary standard forms, are proved in canonical implementation and standard-form comparison. We use the bounded Borel spectral calculus, the joint left/right spectral measure, and its polar-cut integral estimate. The matrix form and its diagonal positive vectors are constructed in standard amplification.

Sections 1–5 apply to arbitrary von Neumann algebras and nonfaithful positive vectors. The fixed-corner argument in Section 6 states its projection-equivalence hypothesis explicitly.

## 1. The small spectral part of a sum of projections

Let \(e,f\in M\) be projections, put \(h=e+f\), and for \(0<t<1\) set


\[
E_t=1_{[t,\infty)}(h),\qquad r_t=1-E_t.
\]


**Lemma 1.1.** These projections satisfy


\[
\begin{gathered}
E_t\leq t^{-1}(e+f),\\
e(1-E_t)e\leq \frac t2 e,
\qquad f(1-E_t)f\leq \frac t2 f.
\end{gathered}
\tag{1}
\]


If \(e+f\ne0\), then \(E_t\ne0\).

**Proof.** Put \(k=e-f\). Multiplication using \(e^2=e\) and \(f^2=f\) gives


\[
kh=(2-h)k.
\tag{2}
\]


Consequently \(k p(h)=p(2-h)k\) for every polynomial \(p\). Uniform approximation extends this equality to continuous functions on \([0,2]\). Bounded monotone approximation in the spectral calculus then gives it for the characteristic function of \([0,t)\): explicitly, bounded continuous functions converging pointwise to this characteristic function converge strongly under either calculus, so multiplication by the fixed bounded operator \(k\) preserves the limits. Hence


\[
kr_t=1_{(2-t,2]}(h)k,
\qquad r_tkr_t=0.
\]


The two spectral intervals are disjoint since \(t<1\). As \(e=(h+k)/2\) and \(f=(h-k)/2\),


\[
r_ter_t=r_tfr_t=\tfrac12 hr_t\leq\tfrac t2 r_t.
\tag{3}
\]


Now \(\|er_te\|=\|r_te\|^2=\|r_ter_t\|\leq t/2\). The positive operator \(er_te\) is supported on \(e\), so it is at most \((t/2)e\). The same argument treats \(f\). The first inequality in (1) is the scalar spectral inequality \(1_{[t,\infty)}(s)\leq s/t\) for \(s\geq0\).

Finally, a nonzero one of \(e,f\) gives \(\|h\|\geq1\), since \(h\geq e,f\). If \(E_t=0\), the spectrum of \(h\) would be contained in \([0,t]\), giving \(\|h\|\leq t<1\). This contradiction proves nonvanishing. \(\square\)

This proof works directly with the spectral calculus of \(e+f\); it does not require a direct-integral normal form for a pair of projections.

## 2. One cut for a finite family of vectors

**Theorem 2.1.** For projections \(e,f\in M\) and \(\xi_1,\ldots,\xi_n\in P\), there is a projection \(E\in M\) such that, with \(c=200\),


\[
\begin{gathered}
E\leq c(e+f),\\
e(1-E)e\leq\tfrac19e,
\qquad f(1-E)f\leq\tfrac19f,\\
\sum_j\|[E,\xi_j]\|^2
\leq c\sum_j\|[e+f,\xi_j]\|\,\|(e+f)\xi_j\|.
\end{gathered}
\tag{4}
\]


If \(e+f\ne0\), the chosen \(E\) is nonzero. In fact the proof gives constants \(9\) in the first line and \(54\) in the last line.

**Proof.** For \(h=e+f\), the positive-operator case of NC22, display NC.10, says


\[
\int_0^\infty
 \|[1_{[\sqrt a,\infty)}(h),\xi_j]\|^2\,da
\leq2\|[h,\xi_j]\|\,\|h\xi_j\|.
\tag{5}
\]


For clarity, its scalar integral is \(|s^2-t^2|\) on the nonnegative joint spectrum. Cauchy–Schwarz bounds its integral by the product of the \(L^2\) norms of \(s-t\) and \(s+t\). Both marginal second moments equal \(\|h\xi_j\|^2\), since \(J\xi_j=\xi_j\), giving the factor two. This explains why no trace or faithful state is needed.

Sum (5) and restrict the integration to


\[
I=[1/81,4/81],\qquad |I|=1/27.
\]


Averaging gives an \(a\in I\) for which the sum of squared commutators is at most \(54\sum_j\|[h,\xi_j]\|\|h\xi_j\|\). All functions are measurable by the strong measurability of the spectral cuts, proved in NC22. This averaging argument also works when the right side is zero.

Take \(E=E_{\sqrt a}\). Here \(1/9\leq\sqrt a\leq2/9\). Lemma 1.1 gives \(E\leq9h\) and both compression estimates in (4), together with nonvanishing if required. Enlarging the constants to \(c=200\) proves the stated version. \(\square\)

The same cut serves every vector. Choosing a different cut for each commutator would not give (4).

## 3. Polar cuts for a twisted vector relation

Fix \(\theta\in\operatorname{Aut}(M)\) and a finite family \(\xi_j\in P\). For \(x\in M\), define


\[
\begin{aligned}
A(x)^2&=\sum_j\|x\xi_j\|^2,\\
B(x)^2&=\sum_j\|(\theta\xi_j)x\|^2,\\
D(x)^2&=\sum_j\|x\xi_j-(\theta\xi_j)x\|^2.
\end{aligned}
\tag{6}
\]


The triangle inequality in the direct sum of \(n\) copies of \(H\) gives \(|A(x)-B(x)|\leq D(x)\).

Write \(x=v|x|\) and \(w_a=v1_{[\sqrt a,\infty)}(|x|)\), for \(a>0\). These are partial isometries. The layer-cake identities and estimates are


\[
\begin{aligned}
\int_0^\infty A(w_a)^2\,da&=A(x)^2,\\
\int_0^\infty D(w_a)^2\,da
&\leq\sqrt2 D(x)\bigl(A(x)^2+B(x)^2\bigr)^{1/2}.
\end{aligned}
\tag{7}
\]


**Proof.** The first line is NC22's positive layer-cake identity, applied to each functional \(\omega_{\xi_j}\) and \(x^*x\). For the second line use the standard matrix amplification and put


\[
Y=\begin{pmatrix}0&x^*\\x&0\end{pmatrix},
\qquad Z_j=\begin{pmatrix}\xi_j&0\\0&\theta\xi_j\end{pmatrix}.
\]


Each \(Z_j\) belongs to the amplified natural cone by PX06. If \(d_j=x\xi_j-(\theta\xi_j)x\), its two off-diagonal commutator entries are \(d_j\) and \(-Jd_j\). Therefore


\[
\begin{aligned}
\|[Y,Z_j]\|^2&=2\|d_j\|^2,\\
\|YZ_j\|^2&=\|x\xi_j\|^2+\|(\theta\xi_j)x\|^2.
\end{aligned}
\]


The polar cut of \(Y\) has off-diagonal entries \(w_a,w_a^*\). Apply the self-adjoint estimate NC.10 to \(Y,Z_j\), divide by two, sum over \(j\), and use the finite Cauchy–Schwarz inequality. This gives (7). \(\square\)

**Corollary 3.1.** Suppose \(x\ne0\), \(0<\gamma\leq1\), and \(D(x)\leq\gamma A(x)\). There is a nonzero partial isometry \(u\in M\) such that


\[
D(u)^2\leq4\gamma A(u)^2.
\tag{8}
\]


If \(A(x)>0\), one can require \(A(u)>0\).

**Proof.** For positive \(A(x)\), (7) and \(B(x)\leq(1+\gamma)A(x)\) imply


\[
\int D(w_a)^2\,da
\leq\sqrt{10}\gamma A(x)^2
<4\gamma\int A(w_a)^2\,da.
\]


Some cut with positive \(A(w_a)^2\) must satisfy (8); otherwise integration over the set of positive mass contradicts the strict inequality. If \(A(x)=0\), the hypothesis gives \(D(x)=B(x)=0\). Both nonnegative integrands in (7) then vanish almost everywhere. Every \(0<a<\|x\|^2\) has \(w_a\ne0\), so choosing a point of this interval outside the exceptional null set gives (8). No division by zero mass occurs. \(\square\)

## 4. A local condition and its partial-isometry witnesses

Call \(\theta\) **locally approximately inner** when, for every finite nonempty family \(\xi_1,\ldots,\xi_n\in P\) and every \(s>0\), some nonzero \(x\in M\) satisfies


\[
D(x)\leq sA(x).
\tag{9}
\]


This is equivalent to asking, for every \(\varepsilon>0\), for a common nonzero \(x\) satisfying the individual inequalities


\[
\|x\xi_j-(\theta\xi_j)x\|^2
\leq\varepsilon\sum_k\|x\xi_k\|^2
\quad(1\leq j\leq n).
\tag{10}
\]


Indeed, (9) with \(s=\sqrt\varepsilon\) gives (10). Conversely apply (10) with \(\varepsilon=s^2/n\) and sum over \(j\).

**Proposition 4.1.** If \(\theta\) is locally approximately inner, then for each finite family and each \(\delta>0\) it has a nonzero partial-isometry witness \(u\) with


\[
D(u)\leq\delta A(u).
\tag{11}
\]


**Proof.** In (9) choose \(s=\min(1,\delta^2/4)\) and apply Corollary 3.1. If \(\delta\geq2\), the resulting bound \(D(u)\leq2A(u)\) is sufficient; otherwise it is exactly the desired bound. \(\square\)

**Proposition 4.2.** Every approximately inner automorphism is locally approximately inner, without a separability assumption.

**Proof.** Approximate innerness means membership in the closure of the inner automorphisms for pointwise predual-norm convergence. Choose a net \(\operatorname{Ad}(u_i)\to\theta\) in that topology. Canonical standard-form implementation is strongly continuous by SF12; one-sided predual convergence also gives convergence of the inverses, since composing a functional with an automorphism is isometric. Thus


\[
\|u_i\xi_j u_i^*-\theta\xi_j\|\longrightarrow0.
\]


Right multiplication by \(u_i\) is isometric, so the left side equals \(\|u_i\xi_j-(\theta\xi_j)u_i\|\). Meanwhile \(A(u_i)^2=\sum_j\|\xi_j\|^2\). If this number is positive, a sufficiently late member of the net satisfies (9). If it is zero, all the vectors vanish and \(x=1\) works. Only finitely many convergence conditions are imposed, so no sequence or countable cofinal subset is needed. \(\square\)

## 5. Compression that retains a definite share of the mass

Put \(\Phi=\sum_j\omega_{\xi_j}\) and retain \(c=200\).

**Theorem 5.1.** If \(\theta\) is locally approximately inner, then for every finite nonempty family \(\xi_j\in P\) and \(\varepsilon>0\) there are a nonzero projection \(E\in M\) and \(x\in M\) such that


\[
\begin{gathered}
\|x\|\leq1,\qquad x=\theta(E)xE,\\
A(x)^2\geq\frac1{64c}\Phi(E),\\
\sum_j\|[E,\xi_j]\|^2\leq\varepsilon^2\Phi(E),\\
D(x)^2\leq\varepsilon^2 A(x)^2.
\end{gathered}
\tag{12}
\]


When \(\Phi\) is faithful, \(A(x)>0\), in particular \(x\ne0\). Without faithfulness the theorem asserts \(E\ne0\), and allows \(x=0\) if \(\Phi(E)=0\).

**Proof.** Choose a positive \(\delta\) such that


\[
\delta\leq\min\left\{
\frac1{48\sqrt n},\frac1{6912cn},
\frac{\varepsilon^2}{3072cn},\frac\varepsilon8
\right\}.
\tag{13}
\]


Take \(u\ne0\) as in Proposition 4.1, and put


\[
e=u^*u,\quad f=\theta^{-1}(uu^*),
\quad\eta=A(u),\quad d_j=u\xi_j-(\theta\xi_j)u.
\]


Thus \(\|d_j\|\leq\delta\eta\). Applying \(J\) gives \(Jd_j=\xi_j u^*-u^*(\theta\xi_j)\). Direct multiplication shows


\[
[e,\xi_j]=u^*d_j-(Jd_j)u.
\]


The corresponding computation for \(uu^*\) and \(\theta\xi_j\), transported by \(U_\theta^*\), gives


\[
\|[e,\xi_j]\|,\ \|[f,\xi_j]\|
\leq2\delta\eta.
\tag{14}
\]


Also \(\|e\xi_j\|=\|u\xi_j\|=:a_j\), and


\[
\|f\xi_j\|=\|u^*(\theta\xi_j)\|
\leq a_j+\delta\eta.
\tag{15}
\]


Here the equality uses \(uu^*\) as the range projection of \(u\), and \(\|\xi_j u^*\|=\|u\xi_j\|\). In particular


\[
\Phi(f)^{1/2}\leq(1+\sqrt n\delta)\eta.
\tag{16}
\]


Apply Theorem 2.1 to \(e,f\), and set \(q_j=\|[E,\xi_j]\|\). The projection \(E\) is nonzero because \(u\ne0\). Equations (14)–(15) yield


\[
\begin{aligned}
\sum_jq_j^2
&\leq4c\delta\eta\sum_j(2a_j+\delta\eta)\\
&\leq12cn\delta\eta^2=\beta^2\eta^2,
\qquad\beta=\sqrt{12cn\delta}.
\end{aligned}
\tag{17}
\]


In the second line we used \(\sum_j a_j\leq\sqrt n\eta\), \(n\geq1\), and \(\delta\leq1\).

First suppose \(\eta>0\) and define \(x=\theta(E)uE\). We estimate the two losses when compressing \(u\). Since \(u=\theta(f)u\), the \(f\)-compression inequality in (4) gives


\[
\|(1-\theta(E))u\xi_j\|\leq a_j/3.
\tag{18}
\]


For the other loss, the product commutator identity and (14) give


\[
\|[e(1-E),\xi_j]\|\leq q_j+2\delta\eta.
\]


Applying \(J\) and the \(e\)-compression inequality in (4) shows
\(\|\xi_j e(1-E)\|=\|(1-E)e\xi_j\|\leq a_j/3\). Since \(u=ue\), it follows that


\[
\|u(1-E)\xi_j\|
\leq a_j/3+q_j+2\delta\eta.
\tag{19}
\]


Subtract \(x\xi_j\) from \(u\xi_j\), insert the two losses (18)–(19), and use the triangle inequality in \(H^n\). This gives


\[
A(x)\geq
\bigl(\tfrac13-\beta-2\sqrt n\delta\bigr)\eta
\geq\eta/4.
\tag{20}
\]


Indeed, (13) gives \(\beta\leq1/24\) and \(2\sqrt n\delta\leq1/24\). This direct-sum estimate does not square individual lower bounds that could be negative.

The support and contraction statements in (12) follow immediately from the definition of \(x\). By (4), (16), and \(\sqrt n\delta\leq1/2\),


\[
\Phi(E)\leq c\bigl(\Phi(e)+\Phi(f)\bigr)
\leq4c\eta^2.
\]


Together with (20) this proves the mass bound in (12). Also \(x^*x\leq E\), so \(A(x)\leq\Phi(E)^{1/2}\). As \(\beta\leq\varepsilon/16\), (17)–(20) give the asserted commutator bound.

Finally, expanding the twisted defect gives exactly


\[
\begin{aligned}
x\xi_j-(\theta\xi_j)x
={}&\theta(E)d_jE+\theta(E)u[E,\xi_j]\\
 &+[\theta(E),\theta\xi_j]uE.
\end{aligned}
\]


The last commutator has norm \(q_j\). The direct-sum norm therefore satisfies


\[
\begin{aligned}
D(x)&\leq D(u)+2\Bigl(\sum_jq_j^2\Bigr)^{1/2}\\
&\leq(\delta+2\beta)\eta
\leq4(\delta+2\beta)A(x)
\leq\varepsilon A(x),
\end{aligned}
\]


using \(\delta\leq\varepsilon/8\) and \(\beta\leq\varepsilon/16\).

If \(\eta=0\), then \(d_j=0\), and (15) gives \(e\xi_j=f\xi_j=0\) for every \(j\). Hence \(\Phi(E)=0\) by \(E\leq c(e+f)\), and \(E\xi_j=\xi_jE=0\). Keep this nonzero \(E\) and take \(x=0\); all of (12) hold. If \(\Phi\) is faithful this case is impossible, and the mass bound with \(E\ne0\) forces \(A(x)>0\). \(\square\)

## 6. Inner perturbations and fixed corners

**Proposition 6.1.** Local approximate innerness is invariant under conjugating the algebra by a normal isomorphism. If \(\theta\) has this property and \(w\in\mathcal U(M)\), then \(\operatorname{Ad}(w)\circ\theta\) also has it.

**Proof.** The canonical standard-form unitary of an isomorphism transports both actions, the cone, and all the norms in (9), and transports a nonzero operator to a nonzero operator. For the second assertion set \(\alpha=\operatorname{Ad}(w)\circ\theta\). Its cone action is \(\alpha\xi=w(\theta\xi)w^*\). The witness \(wx\) satisfies


\[
(wx)\xi_j-(\alpha\xi_j)(wx)
=w\bigl(x\xi_j-(\theta\xi_j)x\bigr),
\]


and \(A(wx)=A(x)\). These are exact norm equalities. \(\square\)

**Proposition 6.2.** Suppose \(\theta\) is locally approximately inner, \(\theta(e)=e\), and \(e\sim1-e\). Then the restriction \(\theta_e\in\operatorname{Aut}(eMe)\) is locally approximately inner in its standard form. The same conclusion is immediate when \(e=1\).

**Proof.** Choose \(v\) with \(v^*v=e\) and \(vv^*=1-e\), and put


\[
w=e+v\theta(v^*),\qquad
\alpha=\operatorname{Ad}(w)\circ\theta.
\]


Both \(v\theta(v^*)\) and its adjoint act on the \(1-e\) corner; their products in either order equal \(1-e\). Thus \(w\) is unitary, \(we=e\), and \(w\theta(v)=v\). Consequently \(\alpha\) fixes the matrix units
\(e_{11}=e,e_{22}=1-e,e_{21}=v,e_{12}=v^*\), and \(\alpha_e=\theta_e\).

Let \(N=\{e_{ij}\}'\cap M\). The explicit finite-matrix decomposition in TS01 identifies \(M\) normally with \(M_2(N)\), and \(N\to eMe\), \(a\mapsto ae\), is a normal isomorphism. The automorphism \(\alpha\) acts entrywise by its restriction \(\gamma\) to \(N\). Under standard-form comparison and PX06, its action on vector matrices is entrywise \(U_\gamma\). One can check cone preservation in the weight construction of PX06: transport the weight and all its finite-star matrix generators by \(\gamma\); canonical comparison acts on each of the four slots. Uniqueness of standard-form implementation then identifies this action with \(U_\alpha\).

For \(\eta_1,\ldots,\eta_n\) in the cone of \(N\), use the positive vector matrices \(Z_j=\operatorname{diag}(\eta_j,\eta_j)\). Proposition 6.1 makes \(\alpha\) locally approximately inner. Apply its aggregate condition (9) to the \(Z_j\) and a prescribed \(s>0\). Write its nonzero witness as \(X=(x_{ab})\). Matrix multiplication gives


\[
\sum_{a,b}\sum_j
\|x_{ab}\eta_j-(\gamma\eta_j)x_{ab}\|^2
\leq s^2\sum_{a,b}\sum_j\|x_{ab}\eta_j\|^2.
\tag{21}
\]


If the right-hand mass is positive, at least one entry of positive mass satisfies the same aggregate inequality for that entry. Otherwise summing the strictly opposite inequalities over all positive-mass entries contradicts (21). Entries of zero mass contribute nonnegative error and cannot repair that contradiction. If the total mass is zero, (21) makes all errors zero, and any nonzero entry of \(X\) works. Thus \(\gamma\) satisfies (9) for the entire family at once. Transporting through \(N\cong eMe\) proves the proposition. \(\square\)

In a countably decomposable type III factor, every nonzero projection is equivalent to the identity, by the projection-equivalence result used and explained in OH06. Hence \(e\sim1-e\) whenever \(e\ne0,1\), and every nonzero \(\theta\)-fixed corner inherits local approximate innerness. In particular this applies to type III factors with separable predual. For an arbitrary algebra, Proposition 6.2 requires its stated equivalence hypothesis.

## 7. Three checks on the construction

**Problem 1.** Exhibit a norm-discontinuous join of projections, and compare it with the cuts of Section 1.

**Solution.** On \(\mathbb C^2\), let \(e\) project onto the first coordinate and let \(f_\alpha\) project onto \((\cos\alpha,\sin\alpha)\). Then \(f_\alpha\to e\) in norm as \(\alpha\to0\), but \(e\vee f_\alpha=1\) for \(0<\alpha<\pi/2\), whereas \(e\vee f_0=e\). The eigenvalues of \(e+f_\alpha\) are \(1\pm\cos\alpha\). For a fixed \(0<t<1\) and sufficiently small positive \(\alpha\), the cut \(E_t\) is the rank-one projection onto \((\cos(\alpha/2),\sin(\alpha/2))\). It converges in norm to \(e\), and


\[
e(1-E_t)e=\sin^2(\alpha/2)e
=\frac{1-\cos\alpha}{2}e<\frac t2 e.
\]


This verifies the compression constant on this two-dimensional model. The averaging in Section 2 selects the cut while also controlling the commutators.

**Problem 2.** Why must the matrix-entry argument use the sum over all test vectors before choosing an entry?

**Solution.** Let two entries have masses \(1,1\) and two tests have error squares \((0,2)\) and \((2,0)\), respectively. For each test the total error is at most the total mass, but no entry has both of its individual errors at most its own mass. Aggregate selection avoids this problem: (21) is one inequality on the sum of every test error. It selects a single entry satisfying that aggregate inequality, which then bounds every individual error. Starting from individual inequalities instead requires first dividing the tolerance by the number of tests and summing, as in Section 4.

**Problem 3.** Explain why nonzero mass cannot be inserted into Corollary 3.1 without a further hypothesis.

**Solution.** In the Hilbert–Schmidt standard form of \(M_2(\mathbb C)\), take \(\theta=\mathrm{id}\), \(\xi=e_{11}\), and \(x=e_{22}\). Then \(x\ne0\) but \(x\xi=\xi x=0\). Every nonzero polar cut of \(x\) is again \(e_{22}\), with zero mass. In Theorem 5.1 the resulting projection may lie in precisely such a common null corner. A faithful sum \(\Phi\) excludes it because \(E\ne0\) implies \(\Phi(E)>0\). This is the exact point at which faithfulness supplies a nonzero compressed intertwiner.

The local condition gives the controlled corner witnesses proved here. Turning those witnesses into unitaries approximating an automorphism on all normal functionals requires a further global assembly argument; none of the spectral-cut statements asserts that conclusion by itself.

**Reference.** M. Takesaki, *Theory of Operator Algebras III*, Chapter XVIII, Section 4, Theorem 4.7 and Lemmas 4.8–4.10, printed pp.371–377. The arguments above give the spectral compression estimate directly from the identity \((e-f)(e+f)=(2-e-f)(e-f)\), use the already proved layer-cake estimate, and supply an explicit tolerance for retaining mass. The fixed-corner statement records the projection-equivalence hypothesis used in its matrix proof, and the forward implication of approximate innerness uses nets.
