# Small centralizer defects and scalar averaging

A unitary which nearly preserves a state need not commute with a prescribed operator. The bicentralizer measures the operators on which all such unitaries eventually act almost trivially. We prove that a trivial bicentralizer is equivalent to a scalar averaging property, first for operators and then in the norm of the predual. We also construct one average for finitely many functionals and use it to obtain almost modular-invariant normal states on \(B(H)\).

Throughout, \(M\ne0\) is a von Neumann algebra with a faithful normal state \(\varphi\). No separability or factor assumption is needed for the equivalences. Use the standard form \((M,H,J,P)\) constructed from \(\varphi\), and let \(\xi=\xi_\varphi\in P\) be its cyclic separating unit vector. Write

\[
\|a\|_\varphi=\|a\xi\|,\qquad
(x\psi)(a)=\psi(ax),\qquad
(\psi x)(a)=\psi(xa).
\]

In particular \(u\psi u^*=\psi\circ\operatorname{Ad}(u)^{-1}\).

The prerequisites are the [concrete predual and its duality with \(M\)](OA-MOD-CP.html#oa-mod-cp-06), dual-ball compactness, convex separation, and the standard-form norm inequality. The last application also uses the polar decomposition of the faithful-state Tomita operator from FS.

## 1. The asymptotic centralizer and its unitary tests

Set

\[
d_\varphi(u)=\|u\varphi-\varphi u\|,
\qquad
\mathcal U_\delta=\{u\in\mathcal U(M):d_\varphi(u)<\delta\}
\quad(\delta>0).
\tag{1}
\]

The module identities give

\[
d_\varphi(u^*)=d_\varphi(u),\qquad
d_\varphi(uv)\le d_\varphi(u)+d_\varphi(v),
\qquad
\|u\varphi u^*-\varphi\|=d_\varphi(u).
\tag{2}
\]

Thus \(\mathcal U_\delta\) is closed under adjoints but is not being treated as a group.

The *asymptotic centralizer* and *bicentralizer* are

\[
\begin{aligned}
\mathrm{AC}(\varphi)
 &=\{(x_n)\in\ell^\infty(M):\|x_n\varphi-\varphi x_n\|\to0\},\\
\mathrm B(\varphi)
 &=\{a\in M:\|[a,x_n]\|_\varphi\to0
                    \text{ for every }(x_n)\in\mathrm{AC}(\varphi)\}.
\end{aligned}
\tag{3}
\]

The product rule

\[
[xy,\varphi]=x[y,\varphi]+[x,\varphi]y
\tag{4}
\]

and the adjoint rule show that \(\mathrm{AC}(\varphi)\) is a unital C*-algebra. Norm closure follows from
\(\|[x-y,\varphi]\|\le2\|x-y\|\).
Its unitaries are exactly the unitary sequences satisfying (3)'s first condition.

Every element of a unital C*-algebra is a linear combination of four unitaries. Here is the construction in the form needed for sequences. Split an element into its self-adjoint real and imaginary parts and scale each to a self-adjoint contraction \(h\). Continuous functional calculus gives the unitary

\[
v=h+i(1-h^2)^{1/2},\qquad h=(v+v^*)/2.
\tag{5}
\]

Applying this inside \(\mathrm{AC}(\varphi)\) proves the assertion with unitaries of that algebra.

**Lemma 1.1.** An element \(a\in M\) belongs to \(\mathrm B(\varphi)\) if and only if

\[
\lim_{\delta\downarrow0}
  \sup_{u\in\mathcal U_\delta}\|u^*au-a\|_\varphi=0.
\tag{6}
\]


**Proof.** If (6) fails, choose \(\varepsilon>0\) and \(u_n\in\mathcal U_{1/n}\) with
\(\|u_n^*au_n-a\|_\varphi\ge\varepsilon\).
Since left multiplication by \(u_n\) is isometric,

\[
\|u_n^*au_n-a\|_\varphi=\|[a,u_n]\|_\varphi.
\]

This contradicts (3). Conversely, (6) makes the commutators vanish for every unitary sequence in \(\mathrm{AC}(\varphi)\), and the four-unitary decomposition (5) gives the conclusion for every element of that algebra. \(\square\)

We will also use the faithful-state metric fact: a bounded sequence \(z_n\) with \(\|z_n\xi\|\to0\) tends strongly to zero. Indeed, \(\xi\) is separating for \(M\), hence cyclic for \(M'\): the projection onto \(\overline{M'\xi}\) belongs to \(M\) and fixes \(\xi\), so faithfulness makes it \(1\). For \(b'\in M'\), \(z_nb'\xi=b'z_n\xi\to0\). Density and the uniform norm bound give convergence on all of \(H\). By CP08, this is also convergence for every positive normal-functional seminorm.

## 2. Compact convex orbits as the defect shrinks

For \(a\in M\) and \(\delta>0\), let

\[
C_\delta(a)=
 \overline{\operatorname{conv}}^{\,\sigma(M,M_*)}
       \{u^*au:u\in\mathcal U_\delta\},
\qquad
C(a)=\bigcap_{\delta>0}C_\delta(a).
\tag{7}
\]

Every \(C_\delta(a)\) is a nonempty ultraweakly compact convex subset of the ball of radius \(\|a\|\). They are nested as \(\delta\) decreases, so compactness makes \(C(a)\) nonempty and compact too.

For \(u\in\mathcal U_\delta\),

\[
|\varphi(u^*au)-\varphi(a)|\le\delta\|a\|.
\]

By continuity and convexity, this inequality holds on \(C_\delta(a)\). Therefore

\[
\varphi(c)=\varphi(a)\qquad(c\in C(a)).
\tag{8}
\]


Two further facts will be used repeatedly. First, for \(b\in C_s(a)\),

\[
C_t(b)\subset C_{s+t}(a).
\tag{9}
\]

For \(v\in\mathcal U_t\), conjugation \(b\mapsto v^*bv\) is ultraweakly continuous. The conjugate of \(u^*au\), with \(u\in\mathcal U_s\), is \((uv)^*a(uv)\); its defect is less than \(s+t\) by (2). Taking both closed convex hulls proves (9). In particular,

\[
b\in C(a)\quad\Longrightarrow\quad C(b)\subset C(a).
\tag{10}
\]


Second, the map \(c\mapsto c\xi\) is ultraweak-to-weak continuous, since each coordinate \(\langle c\xi,\eta\rangle\) is a normal functional. Its image of a compact set is weakly compact. For \(v\in\mathcal U_t\),

\[
\|v^*bv\xi\|^2
 =\varphi(v^*b^*bv)
 \le\|b\xi\|^2+t\|b\|^2.
\]

The closed Hilbert ball is weakly closed, so the same bound holds for \(c\in C_t(b)\). Intersecting in \(t\) yields

\[
\|c\xi\|\le\|b\xi\|\qquad(c\in C(b)).
\tag{11}
\]


**Lemma 2.1.** We have \(a\in\mathrm B(\varphi)\) if and only if \(C(a)=\{a\}\).

**Proof.** If \(a\in\mathrm B(\varphi)\), (6) bounds all orbit vectors \(u^*au\xi\) within a ball of radius tending to zero about \(a\xi\). Convexity and weak closedness of this ball give the same bound on \(C_\delta(a)\). Thus \(c\xi=a\xi\) for \(c\in C(a)\), and faithfulness gives \(c=a\).

Conversely, suppose \(C(a)=\{a\}\), and take unitaries \(u_n\) with \(d_\varphi(u_n)\to0\). Put \(a_n=u_n^*au_n\). Every ultraweak cluster point of this bounded sequence belongs to every \(C_\delta(a)\), hence equals \(a\). Compactness then implies \(a_n\to a\) ultraweakly: a subnet outside an open neighbourhood of \(a\) would have a cluster point in its closed complement, contradicting uniqueness of the cluster point. Thus \(a_n\xi\to a\xi\) weakly. Moreover

\[
\|a_n\xi\|^2
 =\varphi(u_n^*a^*au_n)\longrightarrow\varphi(a^*a)=\|a\xi\|^2.
\]

Expanding the Hilbert norm of \(a_n\xi-a\xi\) proves norm convergence. This holds for every such unitary sequence; the contrapositive selection used in Lemma 1.1 gives (6). \(\square\)

## 3. The minimum-norm point and scalar operator averages

**Proposition 3.1.** For each \(a\in M\), the set \(C(a)\) contains an element of \(\mathrm B(\varphi)\).

**Proof.** The weakly compact convex set \(C(a)\xi\) has a point of minimum norm, because the norm is weakly lower semicontinuous. It is unique: the parallelogram identity makes the midpoint of two distinct minimizers have strictly smaller norm. Write this point as \(b\xi\) with \(b\in C(a)\); faithfulness makes \(b\) unique too.

By (10), \(C(b)\subset C(a)\). By (11), every \(c\in C(b)\) has \(\|c\xi\|\le\|b\xi\|\). Minimality and uniqueness imply \(c=b\). Thus \(C(b)=\{b\}\), and Lemma 2.1 gives \(b\in\mathrm B(\varphi)\). \(\square\)

**Corollary 3.2.** The following conditions are equivalent:

\[
\begin{array}{ll}
\text{(a)}&\mathrm B(\varphi)=\mathbb C1,\\
\text{(b)}&C_\delta(a)\cap\mathbb C1\ne\varnothing
                    \quad(a\in M,\ \delta>0),\\
\text{(c)}&\varphi(a)1\in C_\delta(a)
                    \quad(a\in M,\ \delta>0).
\end{array}
\tag{12}
\]


**Proof.** If (a) holds, Proposition 3.1 supplies a scalar in \(C(a)\), and (8) identifies it as \(\varphi(a)1\). This proves (c), which implies (b).

Assume (b). For a fixed \(a\), the nonempty compact sets \(C_\delta(a)\cap\mathbb C1\) are nested; their intersection contains a scalar. By (8), it is \(\varphi(a)1\), proving (c). If \(a\in\mathrm B(\varphi)\), then \(C(a)=\{a\}\) by Lemma 2.1, and (c) forces \(a=\varphi(a)1\). Scalars always belong to the bicentralizer, so (a) follows. \(\square\)

The compactness used here is compactness of an operator ball in its predual weak topology. No weak compactness of a predual norm ball is asserted.

## 4. Dual averaging and asymptotically commuting functionals

**Theorem 4.1.** Each condition in (12) is equivalent to each of the following conditions:

1. For every \(\psi\in M_*\) and \(\delta>0\),

\[
\psi(1)\varphi\in
 \overline{\operatorname{conv}}^{\,\|\cdot\|}
       \{u\psi u^*:u\in\mathcal U_\delta\}.
\tag{13}
\]

2. If \(\psi\in M_*\) satisfies

\[
\|x_n\psi-\psi x_n\|\longrightarrow0
\quad\text{for every }(x_n)\in\mathrm{AC}(\varphi),
\tag{14}
\]

then \(\psi=\psi(1)\varphi\).

**Proof.** Suppose (12)(c) holds. If (13) failed, real Hahn–Banach separation in \(M_*\), together with \((M_*)^*=M\), would give \(a\in M\) such that

\[
\operatorname{Re}\bigl(\psi(1)\varphi(a)\bigr)
>
\sup_{u\in\mathcal U_\delta}
  \operatorname{Re}(u\psi u^*)(a).
\tag{15}
\]

Every continuous real linear functional on the complex predual is the real part of a continuous complex linear functional, so this is the full separation alternative. But
\((u\psi u^*)(a)=\psi(u^*au)\), and \(\varphi(a)1\in C_\delta(a)\). Applying the ultraweakly continuous real functional \(\operatorname{Re}\psi\) contradicts (15). Thus (13) holds, also for nonpositive and non-Hermitian \(\psi\).

Now suppose (13) and (14) hold. Condition (14) implies

\[
\lim_{\delta\downarrow0}
 \sup_{u\in\mathcal U_\delta}\|u\psi-\psi u\|=0:
\tag{16}
\]

otherwise one could select a counterexample \(u_n\in\mathcal U_{1/n}\) with defect bounded below. By (13) and the triangle inequality for convex combinations,

\[
\|\psi-\psi(1)\varphi\|
\le
\sup_{u\in\mathcal U_\delta}\|\psi-u\psi u^*\|
=
\sup_{u\in\mathcal U_\delta}\|u\psi-\psi u\|.
\tag{17}
\]

Let \(\delta\downarrow0\). This proves condition 2.

Finally, assume condition 2, take \(a\in\mathrm B(\varphi)\), and put \(\psi=a\varphi\). For \((x_n)\in\mathrm{AC}(\varphi)\),

\[
[x_n,a\varphi]=[x_n,a]\varphi+a[x_n,\varphi].
\tag{18}
\]

The second term tends to zero in norm. Cauchy–Schwarz gives
\(\|z\varphi\|\le\|z\xi\|\), so the first tends to zero by the definition of the bicentralizer. Condition 2 gives \(a\varphi=\varphi(a)\varphi\). Evaluating this identity at \((a-\varphi(a)1)^*\) yields

\[
\varphi\bigl((a-\varphi(a)1)^*(a-\varphi(a)1)\bigr)=0.
\]

Faithfulness makes \(a\) a scalar, proving (12)(a). \(\square\)

Equivalently, the closed convex set in (13) may be required merely to meet \(\mathbb C\varphi\). Evaluation at \(1\) already forces the coefficient of that scalar multiple to be \(\psi(1)\). Thus no compactness argument on the predual is needed to identify it.

## 5. One finite average for finitely many functionals

Assume \(\mathrm B(\varphi)=\mathbb C1\).

**Theorem 5.1.** Given \(\psi_1,\ldots,\psi_m\in M_*\), \(\delta>0\) and \(\varepsilon>0\), there are unitaries \(u_1,\ldots,u_r\in\mathcal U_\delta\) and numbers \(\lambda_j\ge0\), \(\sum_j\lambda_j=1\), such that

\[
\left\|\sum_{j=1}^r\lambda_j u_j\psi_k u_j^*
       -\psi_k(1)\varphi\right\|<\varepsilon
\qquad(1\le k\le m).
\tag{19}
\]

In particular one finite convex combination \(T\) of the maps \(\operatorname{Ad}(u)\), \(u\in\mathcal U_\delta\), can satisfy

\[
\|\psi_k\circ T-\psi_k(1)\varphi\|<\varepsilon
\qquad(1\le k\le m).
\tag{20}
\]


**Proof.** The case \(m=0\) allows the identity. Otherwise set \(c_k=\psi_k(1)\), \(C=\max_k|c_k|\), and choose

\[
0<\eta<
\min\left\{\frac{\delta}{m},
           \frac{\varepsilon}{2m(1+C)}\right\}.
\tag{21}
\]

Write \(R_u\psi=u\psi u^*\). Each \(R_u\) is an isometry of \(M_*\), preserves evaluation at \(1\), and satisfies
\(\|R_u\varphi-\varphi\|<\eta\) when \(u\in\mathcal U_\eta\).

Construct successively finite convex averages \(S_1,\ldots,S_m\) of such \(R_u\). Let \(R^{(0)}\) be the identity. Once \(R^{(j-1)}=S_{j-1}\cdots S_1\) is chosen, (13), applied to \(R^{(j-1)}\psi_j\), gives \(S_j\) with

\[
\|S_jR^{(j-1)}\psi_j-c_j\varphi\|<\varepsilon/2.
\tag{22}
\]

Previously treated functionals remain close, because

\[
\|S_j\rho-c\varphi\|
\le\|\rho-c\varphi\|+|c|\eta .
\tag{23}
\]

After all \(m\) steps the error for \(\psi_k\) is less than
\(\varepsilon/2+(m-k)|c_k|\eta<\varepsilon\).

The composition \(R^{(m)}\) is a finite convex average of \(R_{v_m\cdots v_1}\) with \(v_j\in\mathcal U_\eta\). Formula (2) gives
\(d_\varphi(v_m\cdots v_1)<m\eta<\delta\).
This proves (19). Its adjoint map on \(M\) is an average of \(\operatorname{Ad}(u_j^*)\), and \(\mathcal U_\delta\) is closed under adjoints; hence it also proves (20). \(\square\)

Directing finite subsets of \(M_*\) by inclusion and taking tolerances and defect budgets to zero gives a net of finite inner averages \(T_i\) such that

\[
\|\psi\circ T_i-\psi(1)\varphi\|\longrightarrow0
\qquad(\psi\in M_*),
\tag{24}
\]

with every unitary used at index \(i\) having defect below that index's budget. If the predual is separable, testing the first \(n\) elements of a dense sequence and choosing both budgets \(1/n\) gives a sequence with (24). The extension from dense tests uses \(\|T_i\|=1\) and

\[
\|(\psi-\rho)\circ T_i-(\psi-\rho)(1)\varphi\|
\le2\|\psi-\rho\|.
\]

Pointwise norm convergence on the predual in (24) is the property established here; no unproved strong convergence of \(T_i(a)\) is used below.

## 6. Almost modular-invariant normal product states

Let \(\Delta=\Delta_\varphi\). Thus \(\Delta^{it}\xi=\xi\), and the closure of \(a\xi\mapsto a^*\xi\) is \(J\Delta^{1/2}\).

**Lemma 6.1.** For \(u\in\mathcal U(M)\) and \(t\in\mathbb R\),

\[
\|(\Delta^{it}-1)u^*\xi\|
 \le4\max(1,|t|)\,d_\varphi(u)^{1/2}.
\tag{25}
\]


**Proof.** The vector \(u^*\xi\) belongs to the Tomita domain, and
\(\Delta^{1/2}u^*\xi=\xi u^*\).
The positive cone vector \(u\xi u^*\) represents \(u\varphi u^*\). The standard-form inequality therefore gives

\[
\begin{aligned}
\|(\Delta^{1/2}-1)u^*\xi\|^2
 &=\|\xi u^*-u^*\xi\|^2\\
 &=\|u\xi u^*-\xi\|^2\\
 &\le\|u\varphi u^*-\varphi\|=d_\varphi(u).
\end{aligned}
\tag{26}
\]

For \(s>0\),

\[
|s^{2it}-1|\le4\max(1,|t|)\,|s-1|.
\tag{27}
\]

If \(|s-1|\ge1/2\), this follows from the bound \(2\) on the left. Otherwise \(s>1/2\), so \(|\log s|\le2|s-1|\) and
\(|e^{2it\log s}-1|\le2|t|\,|\log s|\).
Apply the spectral calculus with \(s=\Delta^{1/2}\), square and integrate against the spectral measure of \(u^*\xi\). The modular operator has zero kernel, and (26) makes the right-hand integral finite. This proves (25). \(\square\)

**Theorem 6.2.** Suppose \(\mathrm B(\varphi)=\mathbb C1\). For every finite family \(a_1,\ldots,a_m\in M\), \(b_1,\ldots,b_m\in M'\), and every \(T\ge0\), \(\varepsilon>0\), there is a normal state \(\Psi\) on \(B(H)\) such that

\[
\begin{aligned}
|\Psi(a_jb_j)-\varphi(a_j)\langle b_j\xi,\xi\rangle|
   &<\varepsilon &&(1\le j\le m),\\
|\Psi(\Delta^{it})-1|&<\varepsilon &&(|t|\le T).
\end{aligned}
\tag{28}
\]


**Proof.** Choose \(\delta>0\) with
\(4\max(1,T)\sqrt\delta<\varepsilon\), and put
\(A=1+\max(0,\|a_1\|,\ldots,\|a_m\|)\).
The normal functionals

\[
\rho_j(a)=\langle ab_j\xi,\xi\rangle
\]

satisfy \(\rho_j(1)=\langle b_j\xi,\xi\rangle\).
By (20), choose \(T_0=\sum_{\ell=1}^r\lambda_\ell\operatorname{Ad}(u_\ell)\), with \(u_\ell\in\mathcal U_\delta\), such that

\[
\|\rho_j\circ T_0-\rho_j(1)\varphi\|<\varepsilon/A
\qquad(1\le j\le m).
\tag{29}
\]

For \(m=0\) one may instead take \(u_1=1\).

Define the finite sum of vector states

\[
\Psi(X)=\sum_{\ell=1}^r
 \lambda_\ell\langle Xu_\ell^*\xi,u_\ell^*\xi\rangle
\qquad(X\in B(H)).
\tag{30}
\]

It is positive and normal and has value \(1\) at \(1\). Since \(u_\ell\) commutes with \(b_j\),

\[
\Psi(a_jb_j)
=\langle T_0(a_j)b_j\xi,\xi\rangle
=\rho_j(T_0(a_j)).
\tag{31}
\]

Inequality (29) proves the first line of (28). Lemma 6.1 and Cauchy–Schwarz give, uniformly for \(|t|\le T\),

\[
\begin{aligned}
|\Psi(\Delta^{it})-1|
&\le\sum_\ell\lambda_\ell
  \|(\Delta^{it}-1)u_\ell^*\xi\|\\
&<4\max(1,T)\sqrt\delta<\varepsilon .
\end{aligned}
\tag{32}
\]

This proves the second line. \(\square\)

The construction uses exactly the bicentralizer hypothesis. It applies whenever that hypothesis has been proved; it does not by itself prove triviality of the bicentralizer for a specified class of factors.

## 7. A finite matrix model

Take \(M=M_2(\mathbb C)\), \(\varphi=\tau=\operatorname{Tr}/2\), and use the Hilbert space \(L^2(M,\tau)\) with \(\xi=1\). Every unitary has zero state defect. The four unitaries

\[
u_0=1,\quad
u_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
u_2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
u_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}
\]

give the exact average

\[
\frac14\sum_{j=0}^3u_jau_j^*=\tau(a)1.
\tag{33}
\]

Indeed, \(1,u_1,u_2,u_3\) form a linear basis; conjugation fixes \(1\), while each of the three other basis elements is fixed by two of these conjugations and negated by the other two. Formula (33) follows by linearity.

The same four vectors \(u_j^*\xi=u_j\) form an orthonormal basis of \(L^2(M,\tau)\). Hence the state in (30) is the normalized trace on its four-dimensional operator algebra. For \(L_a\) and \(R_b\) denoting left and right multiplication,

\[
\Psi(L_aR_b)=\tau(a)\tau(b).
\tag{34}
\]

This follows directly from (31) and (33). Also \(\Delta_\tau=1\), so \(\Psi(\Delta_\tau^{it})=1\) exactly.

The model illustrates the simultaneous nature of the construction: the same four unitaries work for every functional and every pair \(a,b\). In the general argument, the number of unitaries may depend on the finite list of tests, and (21) keeps the accumulated state defect below the prescribed bound.

**References.** M. Takesaki, *Theory of Operator Algebras III*, Chapter XVIII, Section 3, Proposition 3.4, printed pp.331–333, is the four-way equivalence proved in Sections 1–4. Section 5 supplies simultaneous finite averaging with explicit defect control. Section 6 proves the normal-state approximation in Section 4, Lemma 4.13(ii), printed pp.381–383, under its bicentralizer-triviality input, and gives a spectral estimate uniform on a prescribed compact time interval. The tensor-vector approximation of Lemma 4.13(i) and the subsequent modular-automorphism theorem require additional arguments.

