# Square-zero modular intertwiners

An operator can almost intertwine a positive vector with a scalar multiple of itself without being a partial isometry. Spectral truncation repairs the latter defect, but costs a square root in the error. When the scalar lies strictly between zero and one, a further support separation produces a square-zero operator. A second truncation then gives a square-zero partial isometry.

We prove this procedure with explicit tolerances. We also distinguish a nonzero operator from one with positive functional mass. That distinction matters whenever the positive functionals are not faithful.

Our inputs are the standard-form axioms and positive vectors, the matrix standard form, bounded spectral calculus, bounded polar decomposition, and the proved layer-cake commutator estimate. No factoriality or separability is needed for the main extraction theorem.

## 1. The defect and its two masses

Let \((M,H,J,P)\) be a standard form, let \(n\geq1\), and fix normal positive functionals \(\varphi_1,\ldots,\varphi_n\). Write


\[
\xi_j=\xi_{\varphi_j},\qquad
\Phi=\sum_{j=1}^n\varphi_j,\qquad 0<c<1.
\]


Right multiplication means \(\eta x=Jx^*J\eta\). For \(x\in M\), set


\[
\begin{aligned}
A(x)^2&=\sum_j\|x\xi_j\|^2=\Phi(x^*x),\\
B(x)^2&=\sum_j\|\xi_jx\|^2=\Phi(xx^*),\\
D(x)^2&=\sum_j\|\xi_jx-cx\xi_j\|^2.
\end{aligned}
\tag{1}
\]


The identity for \(B\) follows from \(J\xi_j=\xi_j\) and \(J(\xi_jx)=x^*\xi_j\). The reverse triangle inequality in \(H^{\oplus n}\) gives


\[
|B(x)-cA(x)|\leq D(x).
\tag{2}
\]


Both masses and the defect are homogeneous in \(x\). Scaling all the functionals by \(t\geq0\) multiplies \(A,B,D\) by \(\sqrt t\). In particular, an estimate \(D(x)^2\leq\varepsilon\Phi(x^*x)\) respects this scaling.

We will keep \(A(x)>0\) explicit. Faithfulness of \(\Phi\) implies it whenever \(x\ne0\); without faithfulness that implication fails.

## 2. One cutoff for all the functionals

Write \(x=v|x|\) and, for \(a>0\), define the partial isometry


\[
w_a=v1_{[\sqrt a,\infty)}(|x|),\qquad
m_a=c^2A(w_a)^2+B(w_a)^2.
\]


Put \(S=c^2A(x)^2+B(x)^2\). We claim


\[
\begin{aligned}
\int_0^\infty m_a\,da&=S,\\
\int_0^\infty D(w_a)^2\,da
&\leq\sqrt2\,D(x)\sqrt S.
\end{aligned}
\tag{3}
\]


**Proof.** In the standard form of \(M_2(M)\), use the positive vector


\[
\Xi_j=\begin{pmatrix}\xi_j&0\\0&c\xi_j\end{pmatrix},
\qquad
Y=\begin{pmatrix}0&x\\0&0\end{pmatrix}.
\]


The matrix-cone construction cited above proves positivity of this diagonal vector and identifies both matrix actions. Its functional is


\[
\rho_j([b_{kl}])=\varphi_j(b_{11})+c^2\varphi_j(b_{22}).
\]


Consequently


\[
\begin{aligned}
\|[Y,\Xi_j]\|&=\|\xi_jx-cx\xi_j\|,\\
\rho_j(Y^*Y+YY^*)&=c^2\|x\xi_j\|^2+\|\xi_jx\|^2.
\end{aligned}
\]


The polar cutoff of \(Y\) is \(w_a\otimes e_{12}\), so the same identities hold for its cutoff with \(x\) replaced by \(w_a\). Apply the layer-cake commutator estimate separately to each \(\rho_j\). Summing and applying the finite-dimensional Cauchy–Schwarz inequality gives


\[
\begin{aligned}
\int_0^\infty D(w_a)^2\,da
&\leq\sqrt2\sum_j
\|\xi_jx-cx\xi_j\|
\bigl(c^2\|x\xi_j\|^2+\|\xi_jx\|^2\bigr)^{1/2}\\
&\leq\sqrt2\,D(x)\sqrt S.
\end{aligned}
\]


For the first identity of (3), the initial projection is \(w_a^*w_a=1_{[a,\infty)}(x^*x)\). The final projection is \(w_aw_a^*=1_{[a,\infty)}(xx^*)\). The latter equality follows by conjugating the positive spectral projections through \(v\), on the support of \(|x|\). Integrating these two projections and applying \(\Phi\) gives \(A(x)^2\) and \(B(x)^2\), respectively. All scalar integrands are measurable by the strong measurability of the spectral families, and vanish above \(\|x\|^2\). This proves (3). \(\square\)

This argument uses a single cutoff parameter for the whole family. Choosing unrelated cutoffs for the different functionals would not give that conclusion.

## 3. Selecting a cutoff of positive mass

For \(t>0\), define


\[
\delta_c(t)=\frac{c}{2\sqrt2}
\left(\frac{t}{2c+t}\right)^2.
\tag{4}
\]


**Cutoff lemma.** If \(A(x)>0\) and


\[
D(x)\leq\delta_c(t)A(x),
\]


some polar cutoff \(u=w_a\) satisfies


\[
A(u)>0,\qquad D(u)\leq tA(u).
\tag{5}
\]


**Proof.** Put \(k=t/(2c+t)\), so \(0<k<1\). Since \(S\geq c^2A(x)^2>0\), (3) implies


\[
\int D(w_a)^2\,da
\leq\frac{\sqrt2\,\delta_c(t)}c S
=\frac{k^2}{2}S,
\qquad \int m_a\,da=S.
\]


There is therefore an \(a>0\) with


\[
m_a>0,\qquad D(w_a)^2\leq k^2m_a.
\tag{6}
\]


Indeed, if every parameter with \(m_a>0\) violated the second inequality, integration over that measurable set would give \(\int D(w_a)^2\,da\geq k^2S\), contradicting the preceding upper bound. The set has positive measure because its integral of \(m_a\) is \(S>0\).

For \(u=w_a\), (2) and (6) give


\[
\begin{aligned}
D(u)&\leq k\sqrt{c^2A(u)^2+B(u)^2}\\
&\leq k\bigl(cA(u)+B(u)\bigr)\\
&\leq k\bigl(2cA(u)+D(u)\bigr).
\end{aligned}
\]


Thus \(D(u)\leq 2ck(1-k)^{-1}A(u)=tA(u)\). If \(A(u)=0\), this forces \(D(u)=0\), and (2) forces \(B(u)=0\), contradicting \(m_a>0\). Hence \(A(u)>0\), which also proves \(u\ne0\). \(\square\)

For small \(t\), the sufficient input tolerance \(\delta_c(t)\) is quadratic in \(t\). This is the square-root loss of polar truncation. No linear error estimate is used.

## 4. Separating the initial and final supports

**Support-separation lemma.** Suppose that \(u\) is a partial isometry, \(A(u)>0\), and


\[
D(u)\leq\alpha A(u),\qquad 0<\alpha<1-c.
\]


Set \(e=u^*u\), \(f=uu^*\), and \(z=u(1-f)\). Then


\[
\begin{aligned}
z&=fz(1-f),\qquad z^2=0,\\
A(z)&\geq(1-c-\alpha)A(u)>0,\\
D(z)&\leq(1+2c)D(u).
\end{aligned}
\tag{7}
\]


**Proof.** Since \(fu=u\), the support identity is immediate; multiplication of that identity twice gives \(z^2=0\). By (2),


\[
\sqrt{\Phi(f)}=B(u)\leq(c+\alpha)A(u).
\]


The Cauchy–Schwarz inequality for the positive functional \(\Phi\) gives


\[
\begin{aligned}
|\Phi(e(1-f))|
&\geq\Phi(e)-|\Phi(ef)|\\
&\geq\Phi(e)-\sqrt{\Phi(e)\Phi(f)}\\
&\geq(1-c-\alpha)A(u)^2.
\end{aligned}
\]


Applying the same inequality to \(e^*e(1-f)\) gives


\[
|\Phi(e(1-f))|
\leq\sqrt{\Phi(e)}
\sqrt{\Phi((1-f)e(1-f))}
=A(u)A(z).
\]


Division by the positive number \(A(u)\) proves the mass estimate. Notice that \(e\) and \(f\) need not commute.

For the defect estimate write \(d_j=\xi_ju-cu\xi_j\). Applying \(J\) gives \(Jd_j=u^*\xi_j-c\xi_ju^*\), and direct multiplication gives


\[
\xi_jf-f\xi_j=d_ju^*-uJd_j.
\]


Both actions of \(u\) are contractions, so
\(\|\xi_jf-f\xi_j\|\leq2\|d_j\|\). Finally,


\[
\xi_jz-cz\xi_j
=d_j(1-f)+cu\bigl(\xi_j(1-f)-(1-f)\xi_j\bigr).
\]


Its norm is at most \((1+2c)\|d_j\|\). Square and sum over \(j\) to obtain the last line of (7). \(\square\)

## 5. The square-zero extraction theorem

**Theorem.** For the fixed family of functionals and \(0<c<1\), suppose that for every \(\eta>0\) there is an \(x\in M\) satisfying


\[
A(x)>0,\qquad D(x)\leq\eta A(x).
\tag{8}
\]


For every \(\varepsilon>0\) there is a partial isometry \(w\in M\) such that


\[
\begin{gathered}
w^2=0,\qquad \Phi(w^*w)>0,\\
\sum_j\|\xi_jw-cw\xi_j\|^2
\leq\varepsilon\Phi(w^*w).
\end{gathered}
\tag{9}
\]


Conversely, (9) for every \(\varepsilon>0\) implies (8).

**Proof with explicit tolerances.** Set


\[
\begin{aligned}
\beta&=\sqrt\varepsilon,\qquad b=\delta_c(\beta),\\
\alpha&=\min\left\{
\frac{1-c}{2},\frac{b(1-c)}{2(1+2c)}
\right\},\qquad \eta=\delta_c(\alpha).
\end{aligned}
\tag{10}
\]


All these numbers are strictly positive, and \(\alpha<1-c\). Choose \(x\) from (8) for this \(\eta\). The first cutoff lemma gives a partial isometry \(u\) with \(A(u)>0\) and \(D(u)\leq\alpha A(u)\). The support-separation lemma gives \(z=u(1-uu^*)\), with \(A(z)>0\) and


\[
\frac{D(z)}{A(z)}
\leq\frac{(1+2c)\alpha}{1-c-\alpha}
\leq\frac{2(1+2c)\alpha}{1-c}
\leq b.
\]


Apply the cutoff lemma again, now to \(z\) with target tolerance \(\beta\). It gives a partial isometry \(w\) with \(A(w)>0\) and \(D(w)\leq\beta A(w)\).

It remains to preserve the square-zero property in this last step. Write \(f=uu^*\). Since \(z=fz(1-f)\), its initial support lies below \(1-f\), and its final support lies below \(f\). The polar partial isometry of \(z\), and every positive spectral cutoff of it, consequently belong to \(fM(1-f)\). Thus \(w=fw(1-f)\), so \(w^2=0\). Squaring the defect estimate proves (9).

For the converse, take \(\varepsilon=\eta^2\) and \(x=w\). \(\square\)

In particular, the proof needs only one operator with the specific tolerance \(\eta\) in (10). The hypothesis for all tolerances is a convenient way to state the conclusion for every \(\varepsilon\).

## 6. Nonfaithful functionals and the zero-mass alternative

Suppose \(M\ne0\) has no nonzero abelian projection; that is, every nonzero corner \(qMq\) is noncommutative. Assume the weaker hypothesis that for every \(\eta>0\) there is an \(x\ne0\) with


\[
D(x)\leq\eta A(x).
\tag{11}
\]


Then for each \(\varepsilon>0\) there is a **nonzero** partial isometry \(w\) with \(w^2=0\) and the squared defect estimate in (9). In this statement \(\Phi(w^*w)\) is allowed to vanish.

**Proof.** If \(\Phi\) is faithful, nonzero \(x\) has \(A(x)>0\), and the extraction theorem applies.

Otherwise put \(q=1-s(\Phi)\ne0\), where the functional support is described in Supports of positive vectors. Since \(0\leq\varphi_j\leq\Phi\), we have \(\varphi_j(q)=0\). Hence \(q\xi_j=0\), and applying \(J\) also gives \(\xi_jq=0\).

We construct a nonzero square-zero partial isometry directly in \(qMq\). This corner has a noncentral projection \(p\): otherwise all its projections would be central, and the spectral approximation of self-adjoint elements by finite linear combinations of projections would make the entire corner commutative. Noncentrality implies \(pM(q-p)\ne\{0\}\). Indeed, if this space vanished, its adjoint \((q-p)Mp\) would vanish too, forcing every element of \(qMq\) to commute with \(p\).

Choose \(0\ne y\in pM(q-p)\) and take its polar partial isometry \(w\). Its final support is below \(p\), its initial support is below \(q-p\), and therefore \(w=pw(q-p)\ne0\) and \(w^2=0\). As \(w\in qMq\), both \(w\xi_j\) and \(\xi_jw\) vanish. All terms in (9) are zero. \(\square\)

Every type III von Neumann algebra has the required absence of nonzero abelian projections. To see the relevant implication directly, an abelian projection \(q\) is finite: any partial isometry with initial projection \(q\) and final projection below \(q\) belongs to the commutative algebra \(qMq\), in which \(w^*w=ww^*\). Type III excludes such a nonzero finite projection.

One sometimes states (11) by requiring, for each \(j\),


\[
\|\xi_jx-cx\xi_j\|^2
\leq r\sum_k\|x\xi_k\|^2.
\]


When this holds for every \(r>0\), taking \(r=\eta^2/n\) gives (11) after summation. Conversely, (11) with \(\eta=\sqrt r\) gives each individual inequality. Thus these two qualitative hypotheses agree. The output here is the homogeneous **squared-norm** estimate (9); an unsquared norm bounded by a constant times \(\Phi(w^*w)\) would require an additional argument.

## 7. Exact examples and the functional estimate

**A two-dimensional exact intertwiner.** Let \(\lambda=c^2\in(0,1)\), take \(M=M_2(\mathbb C)\), and let \(\varphi(a)=\operatorname{Tr}(ha)\), where


\[
h=\frac1{1+\lambda}
\begin{pmatrix}\lambda&0\\0&1\end{pmatrix}.
\]


In the Hilbert–Schmidt standard form, the vector is \(\xi=h^{1/2}\). For \(w=e_{12}\),


\[
\xi w=cw\xi,\qquad
w^2=0,\qquad
w^*w=e_{22},\quad ww^*=e_{11}.
\]


Thus \(\varphi(w^*w)=1/(1+\lambda)>0\), while the defect is exactly zero. This also checks the direction of the scalar: the vector relation uses \(\sqrt\lambda\), and the functional relation uses \(\lambda\).

**Why nonzero is not positive mass.** In \(M=\mathbb C\oplus\mathbb C\), put \(\varphi(a,b)=a\) and \(x=(0,1)\). Then \(x\ne0\) and \(A(x)=D(x)=0\) for every \(c\). Nevertheless this algebra contains no nonzero square-zero element, since \((a,b)^2=0\) forces \(a=b=0\). Thus (11) alone does not prove extraction in an arbitrary algebra. Section 6 uses the noncommutative null corner precisely where it is needed.

**Why the strict gap matters.** If \(c=1\), take \(M=\mathbb C\) with its usual state and \(x=1\). The mass is positive and the defect is zero, but again there is no nonzero square-zero element. The factor \(1-c\) in support separation expresses a real obstruction.

**Passing to positive functionals.** Use the conventions \((\varphi w)(a)=\varphi(wa)\) and \((w\varphi)(a)=\varphi(aw)\). The proved two-functional coefficient estimate, applied to \(\varphi_j\) and \(c^2\varphi_j\), gives


\[
\|\varphi_jw-c^2w\varphi_j\|
\leq(1+c)\sqrt{\varphi_j(1)}
\,\|\xi_jw-cw\xi_j\|.
\]


Therefore an extracted \(w\) satisfying (9) also satisfies


\[
\sum_j\|\varphi_jw-c^2w\varphi_j\|^2
\leq(1+c)^2\Phi(1)\varepsilon\Phi(w^*w).
\]


Here we used \(\varphi_j(1)\leq\Phi(1)\) and then summed the squared inequalities. Since \(w^*w\leq1\), this additionally yields absolute errors tending to zero as \(\varepsilon\) tends to zero. The zero-mass construction in Section 6 has both vector and functional defects exactly zero.
