# Scalar defects and hyperfinite gluing

*Exposition, constructions, figures and exercises by GPT-6.1 Sol (OpenAI); source attribution and prerequisite exposition by GPT-6 Astra (OpenAI). Original programme expression: CC0-1.0.*

## Introduction

An automorphism can be implemented by a unitary without determining that unitary's scalar phase. When several automorphisms form an action, arbitrary implementers need not multiply as a cocycle. Their failure to do so is a scalar two-cocycle.

Finite equivalence classes allow an exact correction: choose a root in each class and compare every arrow with the arrow to that root. For an increasing sequence of finite relations, we adjust each new correction to preserve the preceding one. Every individual arrow then receives a final value after finitely many steps. There is no convergence estimate to prove.

We give the construction and apply it to actions on fields of factors. We also prove a relative version when all isotropy acts by inner automorphisms and the full characteristic data agree. The matching data are essential: a finite Pauli action gives a scalar obstruction even when the orbit relation consists of one point.

The unitary and characteristic conventions are related to [Periodic cocycles and the characteristic square](periodic-cocycles-and-the-characteristic-square.md), Sections 3–4, and [Common gauge invariants and outer conjugacy](common-gauge-invariants-and-outer-conjugacy.md), Section 4. The present proofs use only the definitions below, factor centrality, and a specified finite-relation exhaustion with Borel root maps. Basic human references are [Feldman–Moore], [Sutherland] and [Sutherland–Takesaki].

The finite-root construction belongs to the classical cohomology of equivalence relations. [Feldman–Moore] proves higher cohomology vanishing by reducing the aperiodic relation to an integer action. [Sutherland], Lemmas 5.6–5.7, uses finite-class roots and extensions preserving earlier cocycle values in a more general Polish-group comparison. Sections 2–3 below give the scalar formulas directly for the supplied exhaustion, with exact stabilization on each arrow.

## 1. A scalar multiplication defect

Let \(X\) be a standard Borel space and let \(E\subset X\times X\) be a countable Borel equivalence relation. The pair \((x,y)\) is an arrow from \(y\) to \(x\). Thus
\[
(x,y)(y,z)=(x,z).
\tag{1.1}
\]
Write \(\mathbb T=\{\zeta\in\mathbb C:|\zeta|=1\}\). A normalized scalar two-cocycle is a Borel function \(c(x,y,z)\in\mathbb T\) on triples in one \(E\)-class, satisfying
\[
\begin{aligned}
c(x,y,z)c(x,z,t)
&=c(y,z,t)c(x,y,t),\\
c(x,x,y)&=c(x,y,y)=1.
\end{aligned}
\tag{1.2}
\]
A normalized scalar cochain \(a:E\to\mathbb T\) has \(a(x,x)=1\). Its coboundary is
\[
(\delta a)(x,y,z)
=a(x,y)a(y,z)a(x,z)^{-1}.
\tag{1.3}
\]

For motivation, let \(F_x\) be factors, let \(B_{xy}:F_y\to F_x\) be normal isomorphisms with \(B_{xy}B_{yz}=B_{xz}\), and choose unitaries \(v_{xy}\in F_x\). Suppose the automorphisms implemented by these unitaries respect composition:
\[
\operatorname{Ad}\!\bigl(v_{xy}B_{xy}(v_{yz})\bigr)
=\operatorname{Ad}v_{xz}.
\tag{1.4}
\]
The two implementing unitaries differ by a central unitary of \(F_x\), hence by a scalar. Define \(c\) by
\[
v_{xy}B_{xy}(v_{yz})=c(x,y,z)v_{xz}.
\tag{1.5}
\]
Associating the product of three implementers in the two ways gives (1.2). If \(v_{xx}=1\), the defect is normalized. Multiplying \(v_{xy}\) by \(a(x,y)^{-1}\) removes the defect exactly when \(\delta a=c\).

## 2. A root corrects a finite class

Suppose every \(E\)-class is finite and a Borel root map \(r:X\to X\) has been specified. This means \(r(x)\,E\,x\), and \(r(x)=r(y)\) whenever \(x\,E\,y\).

**Lemma 2.1.** Every normalized \(c\) as in (1.2) has the normalized Borel trivialization
\[
a_r(x,y)=c(x,y,r(x)).
\tag{2.1}
\]

*Proof.* The root is the same for \(x,y,z\) in one class. Apply (1.2) to \(x,y,z,r(x)\):
\[
\begin{aligned}
&c(x,y,z)c(x,z,r(x))\\
&\qquad=c(y,z,r(x))c(x,y,r(x)).
\end{aligned}
\tag{2.2}
\]
Dividing gives \(\delta a_r=c\). Normalization gives \(a_r(x,x)=1\). Composition of Borel functions gives measurability. \(\square\)

The same proof works on any relation with a Borel root map. Finiteness matters for the exhaustion in the next section; an arbitrary countable relation need not admit a Borel root for every full class.

**Lemma 2.2.** If \(a\) and \(b\) both satisfy \(\delta a=\delta b=c\) on a relation with root map \(r\), then
\[
\begin{gathered}
d(x,y):=a(x,y)b(x,y)^{-1},\\
f(x):=d(x,r(x)),\\
d(x,y)=f(x)f(y)^{-1}.
\end{gathered}
\tag{2.3}
\]

*Proof.* Dividing the two coboundary equations gives \(d(x,y)d(y,z)=d(x,z)\). Set \(z=r(x)=r(y)\) and solve for \(d(x,y)\). \(\square\)

For example, on three points numbered \(0,1,2\), put \(b(j,k)=\exp(\pi i\,jk/5)\) for \(j\ne k\), and \(b(j,j)=1\). Define \(c=\delta b\). Choosing any one of the three roots gives \(a_r\). Equation (2.3) specifies the exact change between \(b\) and \(a_r\); neither cochain needs to equal the other.

## 3. Keep every old correction

Assume that the following data are given:
\[
\begin{gathered}
E_0=\{(x,x):x\in X\},\\
E_0\subset E_1\subset E_2\subset\cdots,\\
E=\bigcup_{n\ge0}E_n,
\end{gathered}
\tag{3.1}
\]
where each \(E_n\) is a finite Borel equivalence relation, with a specified Borel root map \(r_n\). This is the form of a hyperfinite exhaustion used here. No bound on the class sizes is required.

**Theorem 3.1.** Every normalized Borel scalar two-cocycle \(c\) on \(E\) is a Borel coboundary. One can construct normalized cochains \(a_n\) with
\[
\delta a_n=c|_{E_n},\qquad
a_{n+1}|_{E_n}=a_n.
\tag{3.2}
\]

*Proof.* Start with \(a_0(x,x)=1\). Suppose \(a_n\) is constructed. The root formula supplies
\[
\begin{gathered}
b_{n+1}(x,y)=c(x,y,r_{n+1}(x)),\\
(x,y)\in E_{n+1}.
\end{gathered}
\tag{3.3}
\]
On \(E_n\), both \(a_n\) and \(b_{n+1}\) trivialize \(c\). Define
\[
\begin{aligned}
d_n(x,y)&=a_n(x,y)b_{n+1}(x,y)^{-1},\\
f_n(x)&=d_n(x,r_n(x)).
\end{aligned}
\tag{3.4}
\]
Lemma 2.2 says \(d_n(x,y)=f_n(x)f_n(y)^{-1}\) on \(E_n\). The function \(f_n\) is defined at every point of \(X\), so we may set, on all of \(E_{n+1}\),
\[
a_{n+1}(x,y)
=b_{n+1}(x,y)f_n(x)f_n(y)^{-1}.
\tag{3.5}
\]
The last two factors form a one-cocycle, whose coboundary is one. Therefore \(\delta a_{n+1}=c\). On \(E_n\), (3.5) equals \(a_n\). It is Borel and normalized.

For an arrow \((x,y)\in E\), choose any \(n\) with \((x,y)\in E_n\), and define \(a(x,y)=a_n(x,y)\). Compatibility makes this independent of \(n\). Borel measurability follows by using \(a_n\) on the Borel layers \(E_n\setminus E_{n-1}\). Any triple \(x,y,z\) in one \(E\)-class belongs to one \(E_n\), because its finitely many arrows do. Its coboundary equation is consequently the equation for \(a_n\). Thus \(\delta a=c\). \(\square\)

Changing roots without the factor in (3.5) can change a previously assigned arrow infinitely often. The compatible construction avoids that problem: it stabilizes each arrow exactly at its first stage.

## 4. From implementers to a genuine unitary cocycle

Let \(F_x\) be a Borel field of factors. Let \(A_{xy},B_{xy}:F_y\to F_x\) be Borel actions by normal isomorphisms. Assume normalized Borel unitaries \(v_{xy}\in F_x\) are already given with
\[
A_{xy}=\operatorname{Ad}v_{xy}\circ B_{xy}.
\tag{4.1}
\]
The fields and operations are understood in their specified Borel structures. A Borel field of normal states is also specified. Measurability of the initial implementers is a hypothesis.

**Corollary 4.1.** Under (3.1), there is a normalized Borel unitary \(B\)-cocycle \(w\) implementing (4.1):
\[
\begin{gathered}
w_{xy}B_{xy}(w_{yz})=w_{xz},\\
A_{xy}=\operatorname{Ad}w_{xy}\circ B_{xy}.
\end{gathered}
\tag{4.2}
\]

*Proof.* The action identities give (1.4), hence the normalized scalar defect (1.5). It is Borel: the central unitary in (1.5) is Borel, and its scalar value can be read with a specified Borel field of normal states. Theorem 3.1 gives \(a\) with \(\delta a=c\). Set \(w_{xy}=a(x,y)^{-1}v_{xy}\). Normal isomorphisms fix scalar multiples of one, so
\[
\begin{aligned}
w_{xy}B_{xy}(w_{yz})
&=a(x,y)^{-1}a(y,z)^{-1}\\
&\quad{}\cdot c(x,y,z)v_{xz}\\
&=a(x,z)^{-1}v_{xz}=w_{xz}.
\end{aligned}
\tag{4.3}
\]
The scalar correction has no effect on \(\operatorname{Ad}v_{xy}\). \(\square\)

This proves the phase correction after normal isomorphisms and Borel implementers have been found. It does not construct the initial comparison (4.1).

## 5. Descent through inner isotropy

Let \(\mathcal G\) be a countable Borel groupoid with object space \(X\). For an arrow \(\gamma:y\to x\), write \(s(\gamma)=y\) and \(r(\gamma)=x\). Its isotropy groups are
\[
I_x=\{n\in\mathcal G:s(n)=r(n)=x\}.
\tag{5.1}
\]
Let \(q:\mathcal G\to E\) send \(\gamma:y\to x\) to \((x,y)\). Thus \(E\) is the orbit relation and \(q\) identifies all arrows with the same endpoints. Suppose a Borel section \(s_E:E\to\mathcal G\), normalized on units, is specified.

Let \(A,B\) be Borel actions on the factor field \(F_x\), with a specified Borel field of normal states. Assume every isotropy automorphism is inner, with normalized Borel implementers
\[
A_n=\operatorname{Ad}u_n,\qquad
B_n=\operatorname{Ad}U_n
\quad(n\in I_x).
\tag{5.2}
\]
Require equality of the following actual scalar data:
\[
\begin{aligned}
u_nu_m&=\mu(n,m)u_{nm},\\
U_nU_m&=\mu(n,m)U_{nm}.
\end{aligned}
\tag{5.3}
\]
For every \(\gamma:y\to x\), \(n\in I_x\), and \(m=\gamma^{-1}n\gamma\in I_y\), also require
\[
\begin{aligned}
A_\gamma(u_m)&=\lambda(n,\gamma)u_n,\\
B_\gamma(U_m)&=\lambda(n,\gamma)U_n.
\end{aligned}
\tag{5.4}
\]
Equality of characteristic classes can be used here only after implementing the gauges which make (5.3) and (5.4) equal simultaneously.

Finally, suppose Borel unitaries \(v_s\) have been specified for the section arrows \(s=s_E(x,y)\), with \(v_{1_x}=1\) and
\[
A_s=\operatorname{Ad}v_s\circ B_s.
\tag{5.5}
\]

**Theorem 5.1.** If \(E\) has the exhaustion (3.1), assumptions (5.2)–(5.5) supply a normalized Borel genuine unitary \(B\)-cocycle on all of \(\mathcal G\) implementing \(A_\gamma\).

*Proof.* First put \(v_n=u_nU_n^*\). The shared multiplier in (5.3) cancels:
\[
\begin{aligned}
v_nB_n(v_m)
&=u_nu_mU_m^*U_n^*\\
&=v_{nm}.
\end{aligned}
\tag{5.6}
\]
For a section arrow \(s:y\to x\), (5.4) and (5.5) give
\[
\begin{aligned}
v_sB_s(v_m)
&=\lambda(n,s)u_nv_s\,
  \overline{\lambda(n,s)}U_n^*\\
&=u_nv_sU_n^*\\
&=v_nB_n(v_s),
\qquad n=sms^{-1}.
\end{aligned}
\tag{5.7}
\]
All unitaries in this equation lie in \(F_x\); the scalar phases cancel on the two sides of the implementer.

Every arrow has a unique expression \(\gamma=ns_E(q\gamma)\) with \(n\in I_{r(\gamma)}\). Define
\[
v_\gamma=v_nB_n(v_{s_E(q\gamma)}).
\tag{5.8}
\]
This is Borel, implements \(A_\gamma\), and agrees with \(v_n\) on isotropy. Equations (5.6)–(5.7) imply both mixed identities
\[
\begin{aligned}
v_{n\gamma}&=v_nB_n(v_\gamma),\\
v_{\gamma m}&=v_\gamma B_\gamma(v_m).
\end{aligned}
\tag{5.9}
\]
For the first identity combine the two left isotropy factors using (5.6). For the second write \(\gamma=ns\), use (5.7) to move \(m\) through \(s\), and then combine \(n\) with \(sms^{-1}\) using (5.6).

Let \(c(\gamma,\eta)\) be the scalar defect
\[
v_\gamma B_\gamma(v_\eta)
=c(\gamma,\eta)v_{\gamma\eta}.
\tag{5.10}
\]
Associativity gives the scalar two-cocycle identity. Equation (5.9) says \(c(n,\gamma)=c(\gamma,m)=1\). Applying the two-cocycle identity to \((n,\gamma,\eta)\), then to \((\gamma,m,\eta)\), gives
\[
\begin{aligned}
c(n\gamma,\eta)&=c(\gamma,\eta),\\
c(\gamma,m\eta)&=c(\gamma m,\eta)
                 =c(\gamma,\eta).
\end{aligned}
\tag{5.11}
\]
In the last equality, \(\gamma m=(\gamma m\gamma^{-1})\gamma\), so the first identity applies. Any change of an arrow with fixed endpoints is multiplication on the left by isotropy. Therefore \(c\) depends only on \(q\gamma,q\eta\).

Define its Borel descent by evaluating on the section:
\[
\bar c(e,f)=c(s_E(e),s_E(f)).
\tag{5.12}
\]
Independence of lifts makes \(\bar c\) a normalized two-cocycle on \(E\), even though the section need not preserve multiplication. Theorem 3.1 supplies \(a:E\to\mathbb T\) with \(\delta a=\bar c\). Then
\[
w_\gamma=a(q\gamma)^{-1}v_\gamma
\tag{5.13}
\]
has zero multiplication defect by the calculation in (4.3). Its inner automorphism remains that of \(v_\gamma\). \(\square\)

The proof is valid on a specified invariant conull object set in a measured groupoid, provided all its hypotheses hold there. It uses a countable return groupoid and does not assert a strictification theorem for an uncountable real-flow action.

## 6. Isotropy phases cannot be skipped

Let \(H=(\mathbb Z/2\mathbb Z)^2\) act on the single factor \(M_2(\mathbb C)\). Put
\[
X=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
\tag{6.1}
\]
For \(g=(a,b)\in H\), let \(v_g=X^aZ^b\) and \(A_g=\operatorname{Ad}v_g\). The scalar sign in multiplication disappears under \(\operatorname{Ad}\), so \(A\) is a genuine action. Compare it with the trivial action \(B\). For \(h=(c,d)\),
\[
v_gv_h=(-1)^{bc}v_{g+h}.
\tag{6.2}
\]
This defect cannot be a scalar coboundary. A coboundary on an abelian group is symmetric in \(g,h\), whereas (6.2) takes values \(1\) and \(-1\) in the two orders of \((1,0),(0,1)\). Thus no scalar rephasing of these implementers gives a genuine \(B\)-cocycle.

The orbit relation has one point and is finite. All the obstruction lies in isotropy. Here the multipliers for \(u_g=v_g\) and \(U_g=1\) differ, so (5.3) fails. Theorem 3.1 concerns the principal orbit relation; Theorem 5.1 first uses the characteristic identities to descend the defect to that relation.

For semifinite factors, scalar correction also preserves every trace-scaling constant already present in a comparison. If \(\tau_x\) is a normal semifinite trace and \(v\in F_x\) is unitary, then \(\tau_x\circ\operatorname{Ad}v=\tau_x\). Equations (4.1) and (4.2) consequently have identical trace behavior. Constructing the initial factor comparisons, matching the full characteristic data, and handling outer isotropy are further mathematical steps. The action comparison used in [Common gauge invariants and outer conjugacy](common-gauge-invariants-and-outer-conjugacy.md), Section 5, includes those steps.

## 7. Exercises with complete solutions

**Exercise 7.1. Check associativity. Level 1.** Starting from (1.5), compute the scalar coefficient of \(v_{xt}\) in each association of three consecutive implementers.

*Solution.* The left association gives \(c(x,y,z)c(x,z,t)\). The right association gives \(c(y,z,t)c(x,y,t)\), because \(B_{xy}\) fixes the scalar \(c(y,z,t)\). Equality gives (1.2).

**Exercise 7.2. Two roots on three points. Level 2.** On the example in Section 2, compare \(a_0(1,2)\) and \(a_1(1,2)\), where the subscript specifies the root.

*Solution.* With root zero, both \(b(2,0)\) and \(b(1,0)\) equal one, so \(a_0(1,2)=b(1,2)=\exp(2\pi i/5)\). With root one,
\[
\begin{aligned}
a_1(1,2)
&=b(1,2)b(2,1)b(1,1)^{-1}\\
&=\exp(4\pi i/5).
\end{aligned}
\tag{7.1}
\]
Their ratio is \(\exp(2\pi i/5)\). Each trivializes the same two-cocycle. Different roots can change an old arrow, which is why (3.5) is needed.

**Exercise 7.3. Verify the extension factor. Level 2.** Show directly that \(f(x)f(y)^{-1}\) has coboundary one. What happens if its inverse is used in (3.5)?

*Solution.* In a triple product the values at \(y\) cancel, and division by the \(x,z\) factor cancels the remaining values at \(x,z\). Either orientation has coboundary one. Only the stated orientation preserves \(a_n\): on \(E_n\) it multiplies \(b_{n+1}\) by \(d_n=a_n/b_{n+1}\). The inverse instead gives \(b_{n+1}^2/a_n\), which need not equal \(a_n\).

**Exercise 7.4. Why no limit estimate? Level 1.** For fixed \(x,y,z\) in one \(E\)-class, explain why the proof of \(\delta a=c\) uses a finite stage rather than a limiting multiplication argument.

*Solution.* Each of the three arrows appears at some finite stage. Take the maximum of those stages. All three cochain values equal their final values there and at every subsequent stage, by (3.2). The exact finite-stage coboundary equation is already the final equation.

**Exercise 7.5. Preserve a previous conjugacy. Level 2.** Suppose the initial comparison is \(\pi_xA_{xy}\pi_y^{-1}=\operatorname{Ad}v_{xy}\circ B_{xy}\), for specified normal isomorphisms \(\pi_x\). Apply Corollary 4.1 without changing any \(\pi_x\).

*Solution.* Replace \(A\) in Section 4 by the action \(A'_{xy}=\pi_xA_{xy}\pi_y^{-1}\). Its action law follows by canceling \(\pi_y^{-1}\pi_y\). The scalar correction gives \(w\) with \(A'_{xy}=\operatorname{Ad}w_{xy}\circ B_{xy}\). Thus the same normal isomorphisms \(\pi_x\) work, and \(w\) is a genuine \(B\)-cocycle.

**Exercise 7.6. Keep the common characteristic gauge. Level 3.** Replace both isotropy implementer families by \(u'_n=t_nu_n\), \(U'_n=t_nU_n\), where \(t_n\in\mathbb T\) is a normalized Borel cochain. Find the new multipliers and transport phases, and show that \(v_n\) is unchanged.

*Solution.* The common new multiplier is
\[
\mu'(n,m)
=t_nt_mt_{nm}^{-1}\mu(n,m).
\tag{7.2}
\]
For \(m=\gamma^{-1}n\gamma\), the common transport phase is \(t_mt_n^{-1}\lambda(n,\gamma)\), because normal isomorphisms fix scalars. Finally \(u'_n(U'_n)^*=u_nU_n^*\). Independent rephasings require checking both resulting data; equality of just the new multipliers does not establish (5.4).

**Exercise 7.7. A finite obstruction. Level 2.** Show that no genuine unitary representation of \(H\) can implement the Pauli action in Section 6.

*Solution.* Every implementer of \(A_{(1,0)}\) is a scalar multiple of \(X\), and every implementer of \(A_{(0,1)}\) is a scalar multiple of \(Z\), since the algebra is a factor. These two unitaries anticommute. A representation of the abelian group \(H\) would make them commute. Scalar multiples cannot change that commutator.

**Exercise 7.8. One-cocycles need not vanish. Level 3.** Let \(T(x)=x+\alpha\) on \(\mathbb R/\mathbb Z\), where \(\alpha\) is irrational. Suppose a measurable unitary function \(f\) satisfies \(f(Tx)=\zeta f(x)\). Show that \(\zeta=\exp(2\pi i k\alpha)\) for some integer \(k\).

*Solution.* The unitary function lies in \(L^2\) and is nonzero. Completeness of the Fourier basis gives some nonzero coefficient \(\widehat f(k)\). Translation multiplies that coefficient by \(\exp(2\pi i k\alpha)\). The displayed equation therefore forces \(\zeta\widehat f(k)=\exp(2\pi i k\alpha)\widehat f(k)\), proving the claim. Conversely \(f(x)=\exp(2\pi i kx)\) works. Thus a scalar one-cocycle assigning a constant phase to the generator need not be a coboundary. Theorem 3.1 removes two-cocycles; it does not trivialize every one-cocycle.

Here is the Fourier completeness argument used in Exercise 7.8. For normalized Lebesgue measure on the circle put
\[
K_N(t)=\frac1N\left|\sum_{j=0}^{N-1}e^{2\pi ijt}\right|^2.
\tag{7.3}
\]
This is a nonnegative trigonometric polynomial of integral one. For distance at least \(\delta>0\) from the integers, the geometric-sum formula gives
\[
K_N(t)\le\frac{1}{N\sin^2(\pi\delta)}
\quad(0<\delta\le1/2).
\tag{7.4}
\]
Translations are continuous in \(L^2\): for interval indicators this follows from the measure of their symmetric difference, for finite linear combinations from the triangle inequality, and for arbitrary \(L^2\) functions from density of interval step functions and the translation isometry. The last density is the usual Lebesgue simple-function approximation, followed by approximation of measurable sets by finite unions of intervals. Consequently
\[
\begin{aligned}
&\|K_N*f-f\|_2\\
&\quad\le\int K_N(t)\|f(\,\cdot-t)-f\|_2\,dt\\
&\longrightarrow0.
\end{aligned}
\tag{7.5}
\]
split the integral at distance \(\delta\), use translation continuity on the near part, and (7.4) on the remainder. If all Fourier coefficients of \(f\) vanish, convolution with the finite polynomial \(K_N\) is zero for every \(N\), so (7.5) forces \(f=0\). This supplies the nonzero coefficient used above.

## References

- [Feldman–Moore] Jacob Feldman and Calvin C. Moore, “Ergodic equivalence relations, cohomology, and von Neumann algebras. I,” *Transactions of the American Mathematical Society* **234** (1977), 289–324. [Publisher record](https://doi.org/10.1090/S0002-9947-1977-0578656-4); [full journal text](https://www.ams.org/journals/tran/1977-234-02/S0002-9947-1977-0578656-4/S0002-9947-1977-0578656-4.pdf).
- [Sutherland] Colin E. Sutherland, “A Borel parametrization of Polish groups,” *Publications of the Research Institute for Mathematical Sciences* **21** (1985), 1067–1086. [Publisher text](https://ems.press/content/serial-article-files/42293).
- [Sutherland–Takesaki] Colin E. Sutherland and Masamichi Takesaki, “Actions of discrete amenable groups and groupoids on von Neumann algebras,” *Publications of the Research Institute for Mathematical Sciences* **21** (1985), 1087–1120. [Publisher record](https://www.jstage.jst.go.jp/article/kyotoms1969/21/6/21_6_1087/_article). Section 4 places phase correction after the comparison of isotropy actions. The proofs above give the finite-exhaustion correction and the inner-isotropy descent directly.
