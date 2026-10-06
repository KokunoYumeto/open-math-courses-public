# Closed positive forms: representation and the exact square-root domain

*Programme exposition: OpenAI Codex (AI). Course selection and prerequisite bindings: GPT-6.1 Sol (OpenAI), Ultra. Integration and bounded proof check: GPT-6 Astra (OpenAI), Ultra, October 2026.*

A closed positive form specifies an energy and its finite-energy domain. This lesson recovers its nonnegative self-adjoint operator, proves that the energy domain is exactly the square-root domain, and identifies which vectors have an operator value. Hilbert spaces may have arbitrary dimension, including zero.

Barry Simon treats the form-space construction in [*A canonical decomposition for quadratic forms with applications to monotone convergence theorems*](https://math.caltech.edu/SimonPapers/81.pdf). Zoltán Sebestyén and Zsigmond Tarcsay give a complementary treatment of representation and operator domains in [*Basic representation theorems of forms*](https://arxiv.org/html/2505.09588v1). The proof here uses a bounded energy resolvent and a common dense subspace of two Hilbert spaces of finite-energy vectors.

<a id="OA-MOD-QF-01"></a>
## Prerequisites and conventions

Inner products are linear in the first variable. A positive operator means a nonnegative operator; injectivity is an additional condition. Operator equalities include equality of domains.

- [Hilbert spaces and compact operators, Sections 1–3](../../foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators.html#oa-fnd-hs-01), proves completion, orthogonal projection, the Riesz representation theorem, bounded forms and adjoints. These statements impose no separability condition.
- [Spectral calculus, the bounded and unbounded constructions](../reader/supplements/spectral-calculus-kernel.html#OA-MOD-SK-04), supplies the bounded Borel calculus and the closedness, adjoint and product rules for measurable functions. [Powers and actual ranges](../reader/supplements/spectral-calculus-kernel.html#OA-MOD-SK-07) proves the inverse-domain and square-root identities used below. These proofs do not use closed-form representation or polar decomposition.
- [Integration and convergence, Theorems 2.1–2.2](../../harmonic-analysis-on-locally-compact-groups/reader/measure-and-hilbert-space-tools.html#2-integration-and-convergence-without-countability-assumptions), supplies scalar monotone and dominated convergence. Only sequential scalar convergence is used here.

For completeness, the bounded adjoint works between different Hilbert spaces. If \(T:V\to H\) is bounded, Riesz representation on \(V\) gives the unique \(T^*y\in V\) such that \(\langle Tx,y\rangle_H=\langle x,T^*y\rangle_V\) for all \(x\in V\). Uniqueness makes \(T^*\) linear, and Cauchy–Schwarz gives \(\|T^*y\|\leq\|T\|\|y\|\). Taking the supremum of the same pairing over unit balls gives \(\|T^*\|=\|T\|\); this also holds for zero spaces. Reversing the pairing gives \(T^{**}=T\). Moreover, a vector \(y\) is orthogonal to \(\operatorname{ran}T\) exactly when \(T^*y=0\). Orthogonal projection therefore gives \(\overline{\operatorname{ran}T}=(\ker T^*)^\perp\). Applying this identity to \(T^*\) gives \(\overline{\operatorname{ran}T^*}=(\ker T)^\perp\).

<a id="OA-MOD-QF-02"></a>
## A form includes its domain

A nonnegative sesquilinear form on \(H\) consists of a linear subspace \(D(q)\subseteq H\) and a sesquilinear map \(q:D(q)\times D(q)\to\mathbb C\), linear in the first variable, with \(q[x]:=q(x,x)\geq0\). The reality of \(q[x+y]\) and \(q[x+iy]\), after expansion, gives \(q(y,x)=\overline{q(x,y)}\). Positivity then gives

\[
|q(x,y)|^2\leq q[x]q[y].
\]

Indeed, apply positivity to \(q[x+t y]\); when \(q[y]>0\), minimizing over \(t\in\mathbb C\) proves the inequality, and when \(q[y]=0\), an arbitrarily large scalar with a suitable phase forces the cross term to vanish. The same expansion determines the form from its diagonal by

\[
q(x,y)=\frac14\sum_{k=0}^3 i^k q[x+i^k y].
\]

Conversely, the diagonal axioms already contain the whole sesquilinear form. Let
\(D\) be a complex vector space and suppose that \(Q:D\to[0,\infty)\) satisfies

\[
Q(\lambda x)=|\lambda|^2Q(x),\qquad
Q(x+y)+Q(x-y)=2Q(x)+2Q(y).
\tag{QF.1}
\]

Define first the real polarization

\[
B(x,y)=\frac14\bigl(Q(x+y)-Q(x-y)\bigr).
\tag{QF.2}
\]

This map is symmetric. Two uses of the parallelogram identity give

\[
B(x+z,y)+B(x-z,y)=2B(x,y),
\qquad B(2x,y)=2B(x,y).
\]

Putting \(u=x+z\), \(v=x-z\) in the first identity and using the second shows
\(B(u+v,y)=B(u,y)+B(v,y)\). Thus \(B\) is additive in each variable. For rational
\(r\), it follows that \(B(rx,y)=rB(x,y)\). Positivity of

\[
Q(x+r y)=Q(x)+2rB(x,y)+r^2Q(y)
\]

for rational \(r\) yields

\[
|B(x,y)|^2\leq Q(x)Q(y).
\tag{QF.3}
\]

If \(r_n\in\mathbb Q\) tends to a real number \(t\), additivity, (QF.3), and the
first identity in (QF.1) give

\[
|B(tx,y)-r_nB(x,y)|
=|B((t-r_n)x,y)|
\leq |t-r_n|Q(x)^{1/2}Q(y)^{1/2}.
\]

Hence \(B(tx,y)=tB(x,y)\), so \(B\) is real bilinear. The invariance
\(Q(ix)=Q(x)\) implies

\[
B(ix,iy)=B(x,y),\qquad B(ix,y)=-B(x,iy).
\]

Therefore

\[
s(x,y)=B(x,y)-iB(ix,y)
=\frac14\sum_{k=0}^3 i^kQ(x+i^ky)
\tag{QF.4}
\]

is complex linear in its first variable, conjugate linear in its second, and
Hermitian. Moreover \(B(ix,x)=0\), so \(s(x,x)=Q(x)\). Thus \(s\) is the unique
positive sesquilinear form with diagonal \(Q\). The argument is algebraic: no
topology or density assumption on \(D\) is hidden in the polarization step.

The same statement covers an extended-valued diagonal on a larger vector space.
If \(Q:V\to[0,\infty]\) satisfies (QF.1), with \(0\cdot\infty=0\), then

\[
D(Q)=\{x\in V:Q(x)<\infty\}
\]

is a complex subspace. Indeed, homogeneity handles scalar multiples, while the
parallelogram identity shows that \(Q(x+y)<\infty\) whenever \(Q(x)\) and \(Q(y)\)
are finite. Formula (QF.4) then gives the associated sesquilinear form on this
exact finite-value domain.

The form norm and its inner product are

\[
\|x\|_q^2=\|x\|^2+q[x],\qquad
\langle x,y\rangle_q=\langle x,y\rangle+q(x,y).
\]

The form is **closed** if \(D(q)\) is complete for this norm. It is **densely defined** if \(\overline{D(q)}=H\). These conditions are independent.

It is useful to extend the diagonal by

\[
\widetilde q[x]=
\begin{cases}q[x],&x\in D(q),\\+\infty,&x\notin D(q).\end{cases}
\]

For two forms, \(q_1\leq q_2\) means \(\widetilde q_1[x]\leq\widetilde q_2[x]\) for every \(x\in H\). Equivalently,

\[
D(q_2)\subseteq D(q_1),\qquad q_1[x]\leq q_2[x]\quad(x\in D(q_2)).
\]

Thus an increasing family of forms can have decreasing domains. Statements about this order never mean only an inequality on an unspecified common core.

<a id="OA-MOD-QF-03"></a>
## Representation with the exact square-root domain

**Theorem.** For each densely defined closed nonnegative form \(q\) on \(H\), there is a unique nonnegative self-adjoint operator \(A\) on \(H\) such that

\[
D(q)=D(A^{1/2}),\qquad
q(x,y)=\langle A^{1/2}x,A^{1/2}y\rangle.
\]

Moreover,

\[
\begin{aligned}
D(A)=\{x\in D(q):{}&\text{there exists }y\in H\text{ with }\\
&q(x,v)=\langle y,v\rangle\text{ for every }v\in D(q)\},
\end{aligned}
\]

and the vector \(y\) in this formula equals \(Ax\). Conversely, every nonnegative self-adjoint \(A\) gives a densely defined closed form by these formulas.

**Proof.** Equip \(V=D(q)\) with the energy inner product
\[
\langle x,v\rangle_V=\langle x,v\rangle_H+q(x,v).
\]
Closedness makes \(V\) a Hilbert space. The inclusion \(j:V\to H\) is an injective contraction with dense range. Its bounded adjoint exists by the Hilbert-space argument above. Set \(B=jj^*\). For \(f\in H\),
\[
0\leq\langle Bf,f\rangle_H=\|j^*f\|_V^2\leq\|f\|^2.
\tag{QF.R1}
\]
If \(Bf=0\), this identity gives \(j^*f=0\); density of \(jV\) then gives \(f=0\). Thus \(B\) is an injective positive contraction. In particular its spectral projection at zero is zero, even if zero belongs to its spectrum.

For \(u=Bf\), its preimage in \(V\) is \(j^*f\). The adjoint identity gives, for every \(v\in V\),
\[
\langle u,v\rangle_H+q(u,v)=\langle f,v\rangle_H.
\tag{QF.R2}
\]
The spectral calculus of \(B\) defines
\[
A=B^{-1}-I,\qquad a(t)=t^{-1}-1\quad(0<t\leq1).
\tag{QF.R3}
\]
This is a nonnegative self-adjoint operator. Its domain is exactly \(\operatorname{ran}B\): the inverse-domain assertion is proved in SK-07, and the inequalities
\[
(t^{-1}-1)^2\leq t^{-2}\leq 2(t^{-1}-1)^2+2
\]
show that the two square-integrability conditions coincide. Equation (QF.R2) already proves \(q(u,v)=\langle Au,v\rangle\) for \(u\in D(A)\), \(v\in V\).

We now recover the entire form domain. Put \(W=D(B^{-1/2})\), with norm \(\|x\|_W=\|B^{-1/2}x\|\). It dominates the Hilbert norm because \(0<B\leq I\). It is complete: if \(x_n\) is Cauchy in this norm, then \(x_n\to x\) in \(H\) and \(B^{-1/2}x_n\to y\) in \(H\); closedness of the spectral operator gives \(x\in W\) and \(B^{-1/2}x=y\).

The common subspace \(D(A)=\operatorname{ran}B\) is dense in each of \(V\) and \(W\), with the same norm on that subspace. Indeed, \(\operatorname{ran}j^*\) is dense in \(V\), since its orthogonal complement is \(\ker j=0\). Its image under \(j\) is \(\operatorname{ran}B\), and for \(x=Bf\),
\[
\|x\|_V^2=\|j^*f\|_V^2
=\langle Bf,f\rangle
=\|B^{1/2}f\|^2
=\|B^{-1/2}x\|^2=\|x\|_W^2.
\tag{QF.R4}
\]
For density in \(W\), take \(P_n=E_B([1/n,1])\). If \(x\in W\), then \(x_n=P_nx\in\operatorname{ran}B\), because \(t^{-1}\mathbf1_{[1/n,1]}(t)\) is bounded. Moreover
\[
\|x-x_n\|_W^2
=\int_{(0,1/n)}t^{-1}\,d\langle E_B(t)x,x\rangle\longrightarrow0.
\tag{QF.R5}
\]
This is dominated convergence for the finite integral defining \(W\).

For clarity, density and equal norms here give equality of actual subsets of \(H\). Approximate any \(x\in V\) by a sequence in \(\operatorname{ran}B\) in its \(V\)-norm. The sequence is Cauchy in \(W\), hence has a limit there, and both limits equal \(x\) in \(H\). Thus \(V\subseteq W\). Conversely the spectral approximants in (QF.R5) are Cauchy in \(V\); completeness and their Hilbert-space limit put \(x\in W\) in \(V\). Their limiting norms agree. No countable basis or cofinal subset of a later directed set is involved.

Consequently,
\[
D(q)=D(B^{-1/2}),\qquad
\|x\|^2+q[x]=\int_{(0,1]}t^{-1}\,d\langle E_B(t)x,x\rangle.
\tag{QF.R6}
\]
Since the scalar spectral measure is finite, subtracting \(\|x\|^2\) gives
\[
D(q)=D(A^{1/2}),\qquad q[x]=\|A^{1/2}x\|^2.
\tag{QF.R7}
\]
Polarization proves the sesquilinear identity in the theorem.

For the converse graph criterion, suppose \(x\in V\) and \(q(x,v)=\langle y,v\rangle\) for all \(v\in V\). Then
\[
\langle x,v\rangle_V=\langle x+y,jv\rangle_H
=\langle j^*(x+y),v\rangle_V.
\]
Riesz uniqueness in \(V\) gives \(x=j^*(x+y)\) there. Applying \(j\) gives \(x=B(x+y)\), so \(x\in D(A)\) and \(Ax=y\). Density makes \(y\) unique. This proves the exact graph formula in both directions.

If a nonnegative self-adjoint \(C\) represents the same form, the spectral form-pairing identity in SK-07 gives \(q(x,v)=\langle Cx,v\rangle\) for \(x\in D(C)\), \(v\in D(q)\). The graph criterion therefore gives \(C\subseteq A\). Adjoints reverse this inclusion: if \(z\in D(A^*)\), then the identity \(\langle Ax,z\rangle=\langle x,A^*z\rangle\) restricts to \(D(C)\), so \(z\in D(C^*)\) with the same value. Hence \(A=A^*\subseteq C^*=C\), and \(A=C\).

Finally, a nonnegative self-adjoint \(A\) has a closed densely defined square root by SK-05–SK-07. The graph map \(x\mapsto(x,A^{1/2}x)\) identifies the form norm with the norm on its closed graph in \(H\oplus H\), which is complete. This gives the converse form and finishes the proof. \(\square\)

The operator domain requires a Hilbert-space vector representing the form functional; the square-root domain requires only finite energy. Equation (QF.R4) also proves that the operator domain is dense in the form norm.
