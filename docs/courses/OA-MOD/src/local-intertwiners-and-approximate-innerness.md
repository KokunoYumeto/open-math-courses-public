# From local intertwiners to approximately inner automorphisms

Small intertwining errors initially give contractions with neither full initial support nor full final support. We will pass to a finite algebra of sequences, compare its two diagonal projections, and then replace representatives of their equivalence by actual unitaries.

Let \(M\) be a type III factor with separable predual, let \((M,H,J,P)\) be its standard form, and let \(\theta\in\operatorname{Aut}(M)\). Write

\[
\theta\varphi=\varphi\circ\theta^{-1},\qquad
\theta\xi=U_\theta\xi,\qquad
\xi x=Jx^*J\xi .
\]

The predual module convention is \((x\varphi)(a)=\varphi(ax)\) and \((\varphi x)(a)=\varphi(xa)\). The canonical implementation satisfies \(U_\theta(a\xi b)=\theta(a)(U_\theta\xi)\theta(b)\), as proved in SE11.

We use three earlier arguments with their precise scopes:

- GI05 constructs a uniformly nonvanishing sequence of contractions from the local criterion.
- AI04 converts a vanishing functional intertwining defect into a vanishing standard-form vector defect on any fixed operator-norm ball.
- Ultraproducts and the asymptotic centralizer, Sections 1, 2 and 5 prove the faithful-state metric criterion, the trace-norm completeness criterion, and the single-state finite quotient. Section 2 below supplies the additional proof needed for a simultaneous family of states.

Projection comparison is Theorem 5.5 of the projection lesson. We also use its Corollary 13.5 and Proposition 15.2: a nonzero projection in a countably decomposable type III factor splits into infinitely many nonzero orthogonal projections, and any two nonzero projections in that factor are equivalent.

## 1. A fixed faithful state and the local hypothesis

A separable predual provides a faithful normal state. Indeed, choose a sequence \((\rho_j)\) dense in the positive part of its unit ball and put \(\rho=\sum_{j\ge1}2^{-j}\rho_j\). If \(a\ge0\) and \(\rho(a)=0\), every \(\rho_j(a)=0\), and norm density gives \(\psi(a)=0\) for every positive normal functional \(\psi\). Vector states separate positive operators, so \(a=0\). After normalization, write this state as \(\varphi_0\).

Assume the following local condition: for every finite family \(\xi_1,\ldots,\xi_m\in P\) and every \(\varepsilon>0\), there is \(x\ne0\) in \(M\) such that

\[
\sum_{j=1}^m\|x\xi_j-(\theta\xi_j)x\|^2
\le \varepsilon^2\sum_{j=1}^m\|x\xi_j\|^2 .
\tag{1}
\]

By GI05 there are contractions \(y_k\in M\) satisfying

\[
\begin{aligned}
\|y_k\varphi-(\theta\varphi)y_k\|&\longrightarrow0
&&(\varphi\in M_*),\\
\varphi_0(y_k^*y_k)&\ge\delta,\qquad
\delta=\frac1{38400}.
\end{aligned}
\tag{2}
\]

The second assertion is a lower bound for one fixed faithful state, uniform in \(k\). Merely asking that each \(y_k\) be nonzero would not suffice.

Fix a free ultrafilter \(\omega\) on \(\mathbb N\). All quotients below use bounded sequences; strong and strong* convergence along \(\omega\) mean convergence of the corresponding normal-functional seminorms. For example,

\[
x_n\longrightarrow0\ \hbox{strongly along }\omega
\quad\Longleftrightarrow\quad
\lim_\omega\varphi_0(x_n^*x_n)=0
\tag{3}
\]

on any fixed norm ball. This is the faithful-state criterion proved in Section 1 of the ultraproduct lesson. It applies equally to a different faithful normal state and to adjoints.

## 2. The simultaneous finite quotient

Put \(N=M_2(M)\), and for \(\varphi\in M_*^+\) define

\[
\Psi_\varphi(A)=\varphi(A_{11})+(\theta\varphi)(A_{22}),
\qquad
\psi_0=\frac12\Psi_{\varphi_0}.
\tag{4}
\]

The state \(\psi_0\) is faithful. In fact, if a positive matrix \(A=B^*B\) has both diagonal entries zero, then every entry of \(B\) is zero. Faithfulness of the two states on the diagonal therefore detects every nonzero positive \(A\).

Let \(I\) be the bounded strong*-null sequences in \(N\), and set

\[
\begin{aligned}
A_0&=\{(X_n):\lim_\omega\|[X_n,\psi_0]\|=0\},\\
A_D&=\{(X_n):\lim_\omega\|[X_n,\Psi_\varphi]\|=0
                     \text{ for every }\varphi\in M_*^+\}.
\end{aligned}
\tag{5}
\]

The module product rule and adjoint rule make \(A_D\) a norm-closed unital *-algebra contained in \(A_0\). Cauchy–Schwarz gives, for every positive normal functional \(\Psi\),

\[
\|[X,\Psi]\|
\le \Psi(1)^{1/2}
 \bigl(\Psi(X^*X)^{1/2}+\Psi(XX^*)^{1/2}\bigr).
\tag{6}
\]

Consequently \(I\subset A_D\).

The single-state quotient theorem shows that \(I\) is an ideal of \(A_0\), and

\[
R_0=A_0/I,\qquad
\tau([X_n])=\lim_\omega\psi_0(X_n)
\tag{7}
\]

is a finite von Neumann algebra with faithful normal tracial state. Thus \(I\) is also an ideal of \(A_D\), and \(Q=A_D/I\) is an isometric C*-subalgebra of \(R_0\).

**Proposition 2.1.** The unit ball of \(Q\) is closed in the trace norm of \(R_0\). In particular \(Q\) is a finite von Neumann algebra, with faithful normal tracial state \(\tau|_Q\).

**Proof.** Suppose \(T_j\in Q\), \(\|T_j\|\le1\), and \(T_j\to T\) in \(\|\cdot\|_{2,\tau}\), where \(T\) is in the unit ball of \(R_0\). Choose representatives \(X\in A_0\) of \(T\) and \(Y^{(j)}\in A_D\) of \(T_j\), all of norm at most \(2\), using the quotient norm.

First consider \(\varphi\le C\varphi_0\). Then \(\Psi_\varphi\le2C\psi_0\). Applying (6) to a representative \(Z\in A_0\) gives

\[
\begin{aligned}
\lim_\omega\|[Z_n,\Psi_\varphi]\|
&\le 2\sqrt{2C\Psi_\varphi(1)}\,\|[Z]\|_{2,\tau}.
\end{aligned}
\tag{8}
\]

Here the two quadratic limits agree because \(\tau\) is a trace. Use \(Z=X-Y^{(j)}\) and the vanishing defect of \(Y^{(j)}\). Letting \(j\to\infty\) shows
\(\lim_\omega\|[X_n,\Psi_\varphi]\|=0\) for every such \(\varphi\).

By GI04, these dominated positive functionals are norm dense in \(M_*^+\). Moreover

\[
\|\Psi_\varphi-\Psi_\rho\|\le2\|\varphi-\rho\|,
\qquad
\|[X_n,\Psi_\varphi-\Psi_\rho]\|\le8\|\varphi-\rho\|.
\tag{9}
\]

Approximation by dominated \(\rho\) now gives the same vanishing limit for every \(\varphi\in M_*^+\). Thus \(X\in A_D\), so \(T\in Q\).

The unit ball of \(R_0\) is complete in its trace norm; the closed unit ball of \(Q\) is therefore complete too. Proposition 2.1 of the ultraproduct lesson applies to the C*-algebra \(Q\) and its faithful tracial state. Its proof represents \(Q\) on its trace GNS space, uses Kaplansky density and trace-norm completeness to identify the bicommutant with \(Q\), and identifies the trace as a normal vector state. This proves the assertion. \(\square\)

Let

\[
E=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad F=1-E
\tag{10}
\]

also denote their constant-sequence classes in \(Q\). They commute with every \(\Psi_\varphi\), so they belong to \(Q\).

## 3. A nonzero link between corresponding corners

Write

\[
C=\{(a_n):\lim_\omega\|[a_n,\varphi]\|=0
                   \text{ for all }\varphi\in M_*^+\}
/\{\text{bounded strong*-null sequences in }M\}.
\tag{11}
\]

Embedding a sequence in the upper diagonal entry identifies \(C\) with \(EQE\). Embedding it in the lower diagonal entry identifies \(C\) with \(FQF\), since \(\theta\) permutes all positive normal functionals. Coordinatewise application of \(\theta\) preserves both the numerator and the denominator, and induces an automorphism \(\bar\theta\) of \(C\). Let \(\iota_1,\iota_2\) denote the two embeddings.

**Projection representatives.** Every projection \(e\in C\) has a representing sequence of projections \(e_n\in M\). To see this, choose any lift, take its self-adjoint part, and apply the continuous function \(t\mapsto\max(0,\min(1,t))\); this gives positive contractions \(a_n\) representing \(e\). Then \(a_n-a_n^2\) is strong*-null. For

\[
e_n=1_{[1/2,1]}(a_n)
\]

scalar functional calculus gives

\[
|e_n-a_n|\le2(a_n-a_n^2).
\tag{12}
\]

The squared inequality and (3) show that \(e_n-a_n\) is strong*-null. This null sequence centralizes every positive functional by (6), so \(e_n\) remains in the numerator of (11).

**Lemma 3.1.** If \(e\ne0\) is a projection in \(C\), then

\[
\iota_2(\bar\theta(e))\,Q\,\iota_1(e)\ne\{0\}.
\tag{13}
\]


**Proof.** Use the sequence \(y_k\) from (2). Put \(b_k=y_k^*y_k\). For \(\varphi\ge0\), the exact identity

\[
b_k\varphi-\varphi b_k
=y_k^*\bigl(y_k\varphi-(\theta\varphi)y_k\bigr)
 +\bigl(y_k^*(\theta\varphi)-\varphi y_k^*\bigr)y_k
\tag{14}
\]

shows that \(b_k\) asymptotically centralizes every positive normal functional; the second defect is the adjoint of the first. The same follows for all normal functionals by their decomposition into four positive ones.

Define \(b\in M=(M_*)^*\) by
\(\varphi(b)=\lim_{k\to\omega}\varphi(b_k)\).
This is a positive contraction. For fixed \(a\in M\), passing (14) to the limit gives \(\varphi(ab-ba)=0\) for all \(\varphi\). Hence \(b\) is central. Factoriality and (2) give

\[
b=\lambda1,\qquad \lambda\ge\delta>0.
\tag{15}
\]


By AI04 and (2),

\[
\|y_k\xi-(\theta\xi)y_k\|\longrightarrow0\qquad(\xi\in P).
\tag{16}
\]

The complex span of the self-dual cone \(P\) is dense in \(H\), and both operators on the two sides have norm at most one. Thus (16) holds for every \(\xi\in H\). Apply it to \(a\xi\) and to \(\xi\), and use \(U_\theta(a\xi)=\theta(a)U_\theta\xi\). Subtracting gives

\[
(y_ka-\theta(a)y_k)\xi\longrightarrow0
\qquad(a\in M,\ \xi\in H).
\tag{17}
\]

Only the operator \(a\) is fixed in this assertion.

Choose projection representatives \(e_n\) for \(e\). Faithfulness of \(\tau\) on \(EQE\) gives

\[
t=\lim_{n\to\omega}\varphi_0(e_n)>0.
\tag{18}
\]

For each fixed \(n\), (15) gives

\[
\lim_{k\to\omega}\varphi_0(e_ny_k^*y_ke_n)
=\lambda\varphi_0(e_n),
\tag{19}
\]

while (17) with \(a=e_n\) gives
\(\|(1-\theta(e_n))y_ke_n\xi_{\varphi_0}\|\to0\) as \(k\to\infty\).
The relevant sets in the free ultrafilter meet every sufficiently late tail. We can therefore choose an integer \(k(n)\ge n\) with

\[
\begin{aligned}
\varphi_0(e_ny_{k(n)}^*y_{k(n)}e_n)
   &\ge\lambda\varphi_0(e_n)-1/n,\\
\|(1-\theta(e_n))y_{k(n)}e_n\xi_{\varphi_0}\|&<1/n .
\end{aligned}
\tag{20}
\]

Set \(z_n=\theta(e_n)y_{k(n)}e_n\). The two vectors \(z_n\xi_{\varphi_0}\) and \(y_{k(n)}e_n\xi_{\varphi_0}\) have norm at most one and differ by less than \(1/n\). Consequently

\[
\varphi_0(z_n^*z_n)\ge\lambda\varphi_0(e_n)-3/n,
\qquad
\lim_\omega\varphi_0(z_n^*z_n)\ge\lambda t>0.
\tag{21}
\]

For each \(\varphi\in M_*^+\), the bimodule product rules also give

\[
\|z_n\varphi-(\theta\varphi)z_n\|
\le 2\|[e_n,\varphi]\|
  +\|y_{k(n)}\varphi-(\theta\varphi)y_{k(n)}\|.
\tag{22}
\]

The first term tends to zero along \(\omega\), and the second tends to zero ordinarily because \(k(n)\ge n\).

The lower off-diagonal matrix with entry \(z_n\) therefore belongs to \(A_D\): its commutator with \(\Psi_\varphi\) has exactly the norm of the defect in (22), by testing the upper off-diagonal entry of the argument matrix. Its class lies in the corner in (13), and (21) makes the class nonzero. \(\square\)

## 4. Equality on every central cut

**Lemma 4.1.** Every central projection \(Z\) of \(Q\) has the form

\[
Z=\iota_1(a)+\iota_2(\bar\theta(a))
\tag{23}
\]

for a central projection \(a\) of \(C\).

**Proof.** Commuting with \(E\) eliminates the off-diagonal entries, so write \(Z=\iota_1(a)+\iota_2(b)\). Commuting with the two diagonal corners makes \(a,b\) central projections of \(C\).

If \(e=a(1-\bar\theta^{-1}(b))\ne0\), Lemma 3.1 supplies a nonzero
\(W\in\iota_2(\bar\theta(e))Q\iota_1(e)\).
Here \(WZ=W\), because \(e\le a\), whereas \(ZW=0\), because \(\bar\theta(e)\le1-b\). This contradicts centrality. If \(e=(1-a)\bar\theta^{-1}(b)\ne0\), the same lemma gives \(WZ=0\) and \(ZW=W\), again a contradiction. Both projections must vanish, and \(b=\bar\theta(a)\). \(\square\)

For projection representatives \(a_n\) of \(a\), equations (4), (7) and (23) give

\[
\tau(ZE)=\frac12\lim_\omega\varphi_0(a_n)
       =\frac12\lim_\omega(\theta\varphi_0)(\theta(a_n))
       =\tau(ZF).
\tag{24}
\]


**Proposition 4.2.** The projections \(E\) and \(F\) are equivalent in \(Q\).

**Proof.** By the comparison theorem there is a central projection \(Z\) such that \(ZE\precsim ZF\) and \((1-Z)F\precsim(1-Z)E\). On the first summand choose a partial isometry \(V_1\) with

\[
V_1^*V_1=ZE,\qquad V_1V_1^*\le ZF.
\]

The trace property and (24) show
\(\tau(ZF-V_1V_1^*)=0\). Faithfulness gives \(V_1V_1^*=ZF\).
On the other summand apply the same argument in the reverse direction, then take the adjoint of the resulting partial isometry. Adding the two centrally orthogonal pieces gives

\[
V\in FQE,\qquad V^*V=E,\qquad VV^*=F.
\tag{25}
\]

\(\square\)

The equalities on all central cuts are essential. Equality of the two scalar traces alone would not prove equivalence in an arbitrary finite von Neumann algebra.

## 5. Replacing representatives by unitaries

Lift \(V\) to \(S\in F A_D E\). We may make this lift contractive: replace \(S\) by

\[
Sg(S^*S),\qquad
g(t)=
\begin{cases}1,&0\le t\le1,\\t^{-1/2},&t\ge1.\end{cases}
\tag{26}
\]

This remains in the same corner of \(A_D\), and its image is \(V\), since \(g(V^*V)=g(E)=1\). Thus its only nonzero entry is a sequence of contractions \(x_n\in M\). Equation (25) implies that \(1-x_n^*x_n\) and \(1-x_nx_n^*\) are strong*-null along \(\omega\). In particular,

\[
\alpha_n=\varphi_0(1-x_n^*x_n)\longrightarrow_\omega0,\qquad
\beta_n=(\theta\varphi_0)(1-x_nx_n^*)\longrightarrow_\omega0.
\tag{27}
\]


**Lemma 5.1.** Let \(\varphi,\psi\) be faithful normal states on a countably decomposable type III factor. If \(x_n\) are contractions and
\(\varphi(1-x_n^*x_n)\to_\omega0\),
\(\psi(1-x_nx_n^*)\to_\omega0\), then there are unitaries \(u_n\) with \(u_n-x_n\to_\omega0\) strong*.

**Proof.** Write \(x=v|x|\), \(p=v^*v\), \(q=vv^*\). Functional calculus on the two supports gives

\[
\begin{aligned}
\|(v-x)\xi_\varphi\|^2&\le\varphi(1-x^*x),\\
\|(v-x)^*\xi_\psi\|^2&\le\psi(1-xx^*),\\
\varphi(1-p)&\le\varphi(1-x^*x),\\
\psi(1-q)&\le\psi(1-xx^*).
\end{aligned}
\tag{28}
\]

For the first two estimates use \((1-t)^2\le1-t^2\) on \(0\le t\le1\), with \(|x|\) on \(pH\) and \(|x^*|\) on \(qH\).

If both \(1-p\) and \(1-q\) are nonzero, their equivalence supplies \(w\) with initial projection \(1-p\) and final projection \(1-q\). Then \(u=v+w\) is unitary,

\[
\|(u-v)\xi_\varphi\|^2=\varphi(1-p),\qquad
\|(u-v)^*\xi_\psi\|^2=\psi(1-q).
\tag{29}
\]

If both complements vanish, take \(u=v\).

There remains the case that exactly one complement vanishes. Now \(p\ne0\). Split \(p\) into infinitely many nonzero orthogonal projections \(r_j\). Normality and finite total mass imply

\[
\varphi(r_j)+\psi(vr_jv^*)\longrightarrow0.
\]

For any \(\eta>0\), choose one \(0<r<p\) with this sum less than \(\eta\). Put \(v'=v(p-r)\). Its two complementary supports

\[
1-p+r,\qquad 1-q+vrv^*
\]

are both nonzero, hence equivalent. Extend \(v'\) using a partial isometry \(w\) between them and set \(u=v'+w\). This is a unitary. The triangle inequality gives

\[
\begin{aligned}
\|(u-v)\xi_\varphi\|
 &\le\sqrt{\varphi(1-p)+\varphi(r)}+\sqrt{\varphi(r)},\\
\|(u-v)^*\xi_\psi\|
 &\le\sqrt{\psi(1-q)+\psi(vrv^*)}+\sqrt{\psi(vrv^*)}.
\end{aligned}
\tag{30}
\]

There is no assumption that the original \(v\) itself extends.

Apply this construction at each \(n\), taking \(\eta=1/n\) in the last case. Combining (28)–(30) with the two deficit hypotheses gives

\[
\|(u_n-x_n)\xi_\varphi\|\longrightarrow_\omega0,\qquad
\|(u_n-x_n)^*\xi_\psi\|\longrightarrow_\omega0.
\tag{31}
\]

The differences have norm at most two. The faithful-state criterion (3), applied separately with \(\varphi\) and \(\psi\), therefore makes them strong*-null. This also covers \(x_n=0\): its polar supports are both zero, so the first case applies; the hypotheses ensure these indices cannot carry a nonzero limiting deficit. \(\square\)

Apply the lemma with \(\varphi=\varphi_0\), \(\psi=\theta\varphi_0\) and (27). We obtain actual unitaries \(u_n\) differing strong*-null from the \(x_n\).

## 6. The approximate-innerness theorem

**Theorem 6.1.** For a type III factor with separable predual, an automorphism \(\theta\) is approximately inner if and only if it satisfies the local condition (1).

**Proof.** Approximate innerness implies (1) by LC04, which uses the continuous standard-form implementation of the automorphism group.

Conversely, assume (1). Sections 1–5 construct the contractions \(x_n\) and unitaries \(u_n\). Membership of their matrix lift in \(A_D\) says

\[
\|x_n\varphi-(\theta\varphi)x_n\|\longrightarrow_\omega0
\qquad(\varphi\in M_*^+).
\tag{32}
\]

For a bounded strong*-null sequence \(d_n\), Cauchy–Schwarz gives

\[
\begin{aligned}
\|d_n\varphi\|&\le
  \varphi(1)^{1/2}\varphi(d_n^*d_n)^{1/2},\\
\|\varphi d_n\|&\le
  \varphi(1)^{1/2}\varphi(d_nd_n^*)^{1/2}.
\end{aligned}
\tag{33}
\]

Use \(d_n=u_n-x_n\) and (31). Equations (32)–(33) give

\[
\|u_n\varphi-(\theta\varphi)u_n\|
\longrightarrow_\omega0 .
\tag{34}
\]

The four-positive-functional decomposition CP07 extends this to every \(\varphi\in M_*\).

Right multiplication of a functional by \(u_n^*\) is isometric. Thus (34) is

\[
\|u_n\varphi u_n^*-\theta\varphi\|
=\|\varphi\circ\operatorname{Ad}(u_n)^{-1}
      -\varphi\circ\theta^{-1}\|
\longrightarrow_\omega0.
\tag{35}
\]

Every neighbourhood in the pointwise norm topology on predual actions specifies finitely many functionals and a positive tolerance. The finitely many corresponding sets of good indices belong to \(\omega\), so their intersection is nonempty. Every such neighbourhood of \(\theta\) therefore contains an inner automorphism. This is approximate innerness.

One can also obtain an ordinary implementing sequence. Choose a norm-dense sequence \((\varphi_j)\) in the predual unit ball. For each \(m\), select \(n(m)\ge m\) such that the first \(m\) defects in (35) are less than \(1/m\). Density and the fact that both predual actions are isometries give ordinary pointwise norm convergence for \(u_{n(m)}\). \(\square\)

The separable-predual hypothesis supplies the sequence (2). This theorem does not silently extend the bare criterion (1) to factors without a faithful normal state: GI06 proves that this criterion is vacuous there.

## 7. Two checks on the comparison and lifting arguments

**Central cuts cannot be omitted.** In the finite algebra \(\mathbb C\oplus\mathbb C\), equip the two coordinates with equal trace weights. The projections \(e=(1,0)\) and \(f=(0,1)\) have equal trace, but they are not equivalent: a partial isometry \((v_1,v_2)\) has identical initial and final support coordinatewise. On the central cut \(z=e\), the traces of \(ze\) and \(zf\) differ. Equation (24) rules out exactly this obstruction.

**A one-sided isometry needs correction.** If \(v^*v=1\) and \(vv^*<1\), a unitary agreeing with \(v\) on its initial space would equal \(v\) everywhere and could not be surjective. In Lemma 5.1, removing \(0<r<1\) changes the initial support to \(1-r\) and the final support to \(vv^*-vrv^*\). Both complements are now nonzero. Their equivalence produces a unitary agreeing with \(v\) on \(1-r\); the two state errors are controlled by \(\varphi(r)\), \(\psi(vrv^*)\), and \(\psi(1-vv^*)\). Thus small defects of the original contractions, together with a small discarded projection, give the required strong* approximation.

**Reference.** M. Takesaki, *Theory of Operator Algebras III*, Chapter XVIII, Section 4, Theorem 4.7, reverse implication, printed pp.379–380. The proof above includes the simultaneous-quotient closure argument, projection representatives, the diagonal selection retaining nonzero mass, central-cut comparison, and the correction needed to lift the quotient equivalence to genuine unitaries. Together with LC04 and GI05 it proves the equivalence at the stated separable-predual scope.

