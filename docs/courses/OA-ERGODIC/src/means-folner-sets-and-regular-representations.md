# Means, Følner sets, and regular representations

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. New original text is public domain (CC0).*

## Introduction

An infinite group usually has no invariant probability measure on its points. It may still admit an invariant average of bounded functions. The average need not be countably additive. Amenability asks for precisely this weaker averaging operation.

We will turn such an average into finitely supported probabilities, then into finite sets with small translation boundaries. The same finite sets produce almost invariant vectors in the regular representation. A final argument explains why they make the full and reduced group operator norms agree.

The prerequisites are Hahn–Banach separation, weak-star compactness of the unit ball of a dual space, and basic unitary representations and \(C^*\)-algebras. The measure-space applications continue in [Invariant means on measured relations](invariant-means-on-measured-relations.md). We use discrete groups throughout this lesson. The locally compact version also requires Haar measure and uniform control over compact sets; it is discussed in [Takesaki].

Let \(\Gamma\) be a countable discrete group. For bounded functions and summable functions, use the same left translation convention:

\[
(L_sf)(t)=f(s^{-1}t),\qquad s,t\in\Gamma.
\tag{0.1}
\]

## 1. Invariant averaging

A **mean** on \(\ell^\infty(\Gamma)\) is a positive linear functional \(m\) with \(m(1)=1\). Positivity implies \(\|m\|=1\). It is **left invariant** if \(m(L_sf)=m(f)\) for every \(s\) and \(f\). The group is **amenable** when such a mean exists.

Finite groups have the mean \(|\Gamma|^{-1}\sum_t f(t)\). On an infinite group, a left invariant mean gives every singleton mass zero: all singleton masses agree, and finite additivity bounds \(N\) times their common value by one for every \(N\). Thus an invariant mean on an infinite countable group cannot be countably additive.

**Proposition 1.1.** A left invariant mean yields a mean invariant under both left and right translations.

*Proof.* Inversion turns a left invariant mean \(m_L\) into a right invariant mean \(m_R\), by \(m_R(f)=m_L(t\mapsto f(t^{-1}))\). Define

\[
m(f)=m_L\bigl(g\mapsto m_R(h\mapsto f(gh))\bigr).
\tag{1.1}
\]

The inner value is a bounded function of \(g\); no assertion about interchanging two integrals is involved. Positivity and normalization follow twice. Left translation of \(f\) translates the outer \(g\)-function on the left. Right translation of \(f\) translates the inner \(h\)-function on the right. Both leave (1.1) unchanged. \(\square\)

## 2. Turning a mean into probabilities

Write \(\mathcal P_f(\Gamma)\) for the finitely supported functions \(p\geq0\) with \(\sum_t p(t)=1\).

**Theorem 2.1.** The following conditions are equivalent:

1. \(\Gamma\) is amenable.
2. For every finite \(S\subset\Gamma\) and \(\varepsilon>0\), there is \(p\in\mathcal P_f(\Gamma)\) with
   \[
   \sum_{s\in S}\|L_sp-p\|_1<\varepsilon.
   \tag{2.1}
   \]
3. There is a sequence \(p_n\in\mathcal P_f(\Gamma)\) such that \(\|L_sp_n-p_n\|_1\to0\) for every \(s\).

*Proof.* Assume a left invariant mean exists. Fix \(S\). In the real Banach space \(\bigoplus_{s\in S}\ell^1(\Gamma;\mathbb R)\), with sum norm, consider the convex set

\[
\mathcal C=\{(L_sp-p)_{s\in S}:p\in\mathcal P_f(\Gamma)\}.
\]

If zero were outside its norm closure, Hahn–Banach separation would give bounded real functions \(f_s\) and a number \(a>0\) such that

\[
\sum_{s\in S}\sum_t f_s(t)(L_sp(t)-p(t))\geq a
\tag{2.2}
\]

for every \(p\in\mathcal P_f(\Gamma)\). Taking \(p\) to be the point mass at \(u\) gives

\[
\sum_{s\in S}\bigl(f_s(su)-f_s(u)\bigr)\geq a
\quad\text{for every }u.
\tag{2.3}
\]

Apply \(m\). Each summand has mean zero by left invariance, contradicting \(0\geq a\). Therefore zero belongs to the norm closure of \(\mathcal C\), which is exactly (2.1).

Enumerate \(\Gamma\), apply (2.1) to the first \(n\) elements with error \(1/n\), and obtain condition 3.

Conversely, each \(p_n\) defines a mean \(m_n(f)=\sum_t p_n(t)f(t)\). A weak-star convergent subnet exists because the state space is weak-star compact. Its limit is positive, normalized, and satisfies

\[
|m_n(L_sf)-m_n(f)|
\leq\|f\|_\infty\|L_{s^{-1}}p_n-p_n\|_1\longrightarrow0.
\]

It is a left invariant mean. \(\square\)

Condition (2.1) is the discrete **Reiter condition**. The probabilities distribute mass almost equally before and after each prescribed translation.

## 3. A level set with a small boundary

A **Følner sequence** consists of nonempty finite sets \(F_n\subset\Gamma\) such that

\[
\frac{|sF_n\mathbin{\triangle}F_n|}{|F_n|}
\longrightarrow0
\quad\text{for every }s\in\Gamma.
\tag{3.1}
\]

**Theorem 3.1.** A countable discrete group is amenable exactly when it has a Følner sequence.

*Proof.* For \(p\in\mathcal P_f(\Gamma)\), put \(F_a=\{t:p(t)>a\}\), \(a>0\). The scalar identity

\[
|u-v|=\int_0^\infty
|\mathbf1_{\{u>a\}}-\mathbf1_{\{v>a\}}|\,da,
\qquad u,v\geq0,
\tag{3.2}
\]

and finite summation give

\[
\int_0^\infty |F_a|\,da=1,\qquad
\int_0^\infty |sF_a\mathbin{\triangle}F_a|\,da
=\|L_sp-p\|_1.
\tag{3.3}
\]

Choose \(p\) satisfying (2.1). If every nonempty \(F_a\) had
\(\sum_{s\in S}|sF_a\triangle F_a|\geq\varepsilon|F_a|\), integration would contradict (2.1). Thus one level gives a nonempty finite set with total relative boundary below \(\varepsilon\). Enumerating the group produces (3.1).

Conversely, \(p_n=|F_n|^{-1}\mathbf1_{F_n}\) satisfies

\[
\|L_sp_n-p_n\|_1
=\frac{|sF_n\triangle F_n|}{|F_n|}.
\]

Theorem 2.1 applies. \(\square\)

**Example 3.2.** For \(\mathbb Z^d\), the boxes \(F_N=\{-N,\ldots,N\}^d\) are Følner. Translation by a fixed vector changes only a fixed-width collection of boundary slabs. Their cardinalities grow at most as a constant times \(N^{d-1}\), whereas \(|F_N|=(2N+1)^d\).

## 4. Fixed points and permanence

**Theorem 4.1.** Amenability is equivalent to the following fixed-point property: every continuous affine action of \(\Gamma\) on a nonempty compact convex subset \(K\) of a Hausdorff locally convex real vector space has a fixed point.

*Proof.* Let \(p_n\) be as in Theorem 2.1 and choose \(x\in K\). Finite convex combinations give

\[
x_n=\sum_g p_n(g)\,g x\in K.
\]

For any continuous real linear functional \(\ell\),

\[
|\ell(sx_n-x_n)|
\leq \sup_{z\in K}|\ell(z)|\,\|L_sp_n-p_n\|_1.
\tag{4.1}
\]

Take a convergent subnet in the compact space \(K\). Continuity of the action and (4.1) imply that every continuous linear functional vanishes on \(sx_\infty-x_\infty\). These functionals separate points, so the limit is fixed.

For the reverse implication, let \(K\) be the weak-star compact convex space of means on \(\ell^\infty(\Gamma)\). Precomposition by \(L_{s^{-1}}\) defines a continuous affine action. A fixed point is an invariant mean. \(\square\)

**Proposition 4.2.** Subgroups, quotients, extensions, and increasing unions of amenable countable discrete groups are amenable.

*Proof.* For a subgroup \(H\leq\Gamma\), choose one representative \(t\) of each right coset \(Ht\), an orbit of left multiplication by \(H\). Every \(g\) has a unique form \(ht\). Set \(r(ht)=h\). Then \(r(h'g)=h'r(g)\). If \(m_\Gamma\) is a left invariant mean, \(f\mapsto m_\Gamma(f\circ r)\) is a left invariant mean on \(H\).

For a quotient, pull bounded functions back along the quotient map and restrict a mean.

For an extension \(1\to H\to\Gamma\to Q\to1\), suppose \(H,Q\) are amenable. Choose representatives \(t_q\in\Gamma\). Given \(f\in\ell^\infty(\Gamma)\), define

\[
F_f(q)=m_H(h\mapsto f(t_qh)),\qquad
m_\Gamma(f)=m_Q(F_f).
\tag{4.2}
\]

For \(a\in\Gamma\), with quotient \(\bar a\), write \(a t_q=t_{\bar a q}c(a,q)\), where \(c(a,q)\in H\). Left invariance of \(m_H\) shows \(F_{t\mapsto f(at)}(q)=F_f(\bar a q)\). Left invariance of \(m_Q\) finishes the proof.

Finally, if every finite subset of \(\Gamma\) is contained in an amenable subgroup, choose a probability in that subgroup satisfying (2.1) for the given finite \(S\). Extend it by zero. Its translation errors in \(\Gamma\) are unchanged. \(\square\)

**Corollary 4.3.** Every countable abelian group and every countable solvable group is amenable.

*Proof.* A finitely generated abelian group is a quotient of some \(\mathbb Z^d\). Every finite subset of a countable abelian group lies in a finitely generated subgroup. Apply Proposition 4.2 and Example 3.2. A finite derived series of a solvable group then gives the result by repeated extension. \(\square\)

**Example 4.4.** The free group on two generators \(a,b\) is not amenable. Let \(A_+,A_-,B_+,B_-\) be the sets of reduced words beginning respectively with \(a,a^{-1},b,b^{-1}\). They, together with the identity, partition the group. Reduced-word cancellation gives

\[
aA_-=\Gamma\setminus A_+,\qquad
bB_-=\Gamma\setminus B_+.
\]

An invariant mean would consequently satisfy \(m(A_-)+m(A_+)=1\) and \(m(B_-)+m(B_+)=1\). Their sum is two. The partition and the zero mass of a singleton say that the same sum is one. This contradiction proves the assertion.

## 5. Almost invariant vectors

Let \(\lambda_s\) be the left regular unitary on \(\ell^2(\Gamma)\).

**Theorem 5.1.** Amenability is equivalent to the existence of unit vectors \(\xi_n\in\ell^2(\Gamma)\) with \(\|\lambda_s\xi_n-\xi_n\|_2\to0\) for every \(s\).

*Proof.* A Følner sequence gives \(\xi_n=|F_n|^{-1/2}\mathbf1_{F_n}\), and

\[
\|\lambda_s\xi_n-\xi_n\|_2^2
=\frac{|sF_n\triangle F_n|}{|F_n|}.
\tag{5.1}
\]

Conversely, put \(p_n(t)=|\xi_n(t)|^2\). By Cauchy–Schwarz,

\[
\begin{aligned}
\|L_sp_n-p_n\|_1
&\leq\sum_t|\xi_n(s^{-1}t)-\xi_n(t)|
\bigl(|\xi_n(s^{-1}t)|+|\xi_n(t)|\bigr)\\
&\leq2\|\lambda_s\xi_n-\xi_n\|_2.
\end{aligned}
\tag{5.2}
\]

Although \(p_n\) need not be finitely supported, it can be approximated in \(\ell^1\) by finitely supported probabilities. Translation is isometric, so these approximations give (2.1). \(\square\)

Equivalently, the coefficients \(\langle\lambda_s\xi_n,\xi_n\rangle\) converge to one on every finite subset. Indeed,
\(\|\lambda_s\xi-\xi\|^2=2-2\operatorname{Re}\langle\lambda_s\xi,\xi\rangle\).

## 6. The full and reduced operator norms

For a finite sum \(f=\sum_s f(s)s\) in the complex group algebra, define

\[
\|f\|_{\max}=\sup_\pi\left\|\sum_s f(s)\pi(s)\right\|,
\qquad
\|f\|_r=\left\|\sum_s f(s)\lambda_s\right\|.
\tag{6.1}
\]

The supremum runs over unitary representations. Their completions are \(C^*(\Gamma)\) and \(C_r^*(\Gamma)\).

**Theorem 6.1.** A countable discrete group is amenable exactly when \(\|f\|_{\max}=\|f\|_r\) for every finite group-algebra sum. Equivalently, the canonical map \(C^*(\Gamma)\to C_r^*(\Gamma)\) is faithful.

*Proof.* Assume amenability, and take almost invariant unit vectors \(\xi_n\). Let \(\pi\) act on \(K\). On \(\ell^2(\Gamma)\otimes K\), the unitary

\[
W(\delta_t\otimes v)=\delta_t\otimes\pi(t)^{-1}v
\tag{6.2}
\]

satisfies \(W(\lambda_s\otimes\pi(s))W^*=\lambda_s\otimes1\). This follows directly from \(\pi(st)^{-1}\pi(s)=\pi(t)^{-1}\).

The isometry \(J_n v=\xi_n\otimes v\) gives

\[
J_n^*(\lambda_s\otimes\pi(s))J_n
=\langle\lambda_s\xi_n,\xi_n\rangle\,\pi(s).
\tag{6.3}
\]

For a finite sum \(f\), these compressions converge in operator norm to \(\pi(f)\). By (6.2), each has norm at most \(\|\lambda(f)\|\). Thus \(\|\pi(f)\|\leq\|\lambda(f)\|\) for every \(\pi\). The reverse inequality is part of the definition of \(\|\cdot\|_{\max}\).

Conversely, equality of norms makes the trivial representation
\(\epsilon(\lambda(f))=\sum_s f(s)\) a state on \(C_r^*(\Gamma)\). Hahn–Banach extends it to a norm-one functional \(\psi\) on \(B(\ell^2(\Gamma))\), with \(\psi(1)=1\). Such a functional is positive. To check this last assertion, for self-adjoint \(A\) use
\[
|1+it\psi(A)|\leq\|1+itA\|
\leq(1+t^2\|A\|^2)^{1/2}
\]
for both signs of small \(t\); it forces \(\psi(A)\) to be real. If \(0\leq A\leq1\), the bound \(|\psi(1-A)|\leq1\) then gives \(\psi(A)\geq0\).

Because \(\psi(\lambda_s)=1\),
\[
\psi((\lambda_s-1)^*(\lambda_s-1))=0.
\]
The Cauchy–Schwarz inequality for a positive functional implies \(\psi(B(\lambda_s-1))=0\) and \(\psi((\lambda_s-1)B)=0\) for all \(B\). Hence
\(\psi(\lambda_sB\lambda_s^*)=\psi(B)\).

For \(f\in\ell^\infty(\Gamma)\), let \(M_f\) be diagonal multiplication. The functional \(m(f)=\psi(M_f)\) is a mean. Since
\(\lambda_sM_f\lambda_s^*=M_{L_sf}\), it is left invariant. \(\square\)

## 7. Exercises with solutions

Level 1 asks for a computation or a direct application. Level 2 asks for a proof using the lesson’s framework. Level 3 combines results or examines a hypothesis whose failure changes the conclusion.

**Exercise 7.1 (an exact boundary).** *Level 1.* For \(F_N=\{-N,\ldots,N\}^2\subset\mathbb Z^2\), compute the relative symmetric difference for translation by \((1,0)\).

*Solution.* One vertical column leaves and one enters, each containing \(2N+1\) points. The ratio is \(2(2N+1)/(2N+1)^2=2/(2N+1)\). The squared regular-vector error has exactly the same value by (5.1).

**Exercise 7.2 (finite versus countable additivity).** *Level 2.* Prove that an invariant mean on an infinite countable group vanishes on every finite set but cannot vanish on all bounded functions supported on an arbitrary countable set.

*Solution.* The singleton argument in Section 1 and finite additivity give zero on finite sets. The entire group is itself countable and its indicator is one, whose mean is one. Countable additivity would incorrectly turn this value into a sum of zero singleton masses.

**Exercise 7.3 (a nonabelian Følner sequence).** *Level 3.* In the infinite dihedral group
\(\langle r,t:t^2=1,\;trt=r^{-1}\rangle\), use
\[
F_N=\{r^k,r^kt:-N\leq k\leq N\}.
\]
Compute the errors for the generators.

*Solution.* The \(2(2N+1)\) displayed elements are distinct. Left multiplication by \(t\) interchanges the two families and replaces \(k\) by \(-k\), so \(tF_N=F_N\). Left multiplication by \(r\) shifts both exponent intervals by one; its symmetric difference has four elements. The relative error is \(2/(2N+1)\). Any fixed word in the generators has error bounded by the sum of the errors of its letters, using
\(|uvF\triangle F|\leq|uF\triangle F|+|vF\triangle F|\). Thus these sets are Følner.

**Exercise 7.4 (why convexity matters).** *Level 2.* Identify where convexity is used in Theorems 2.1 and 4.1.

*Solution.* The difference vectors in Theorem 2.1 form a convex set because probabilities can be mixed. Hahn–Banach then supplies a single separating functional if zero is outside the norm closure. In Theorem 4.1, the finite weighted averages \(x_n\) remain in \(K\) because \(K\) is convex. Compactness alone would not give that inclusion.

**Exercise 7.5 (a uniform representation estimate).** *Level 2.* Let \(f\) have finite support and let \(\xi\) be a unit vector. Bound the error between \(\pi(f)\) and its compression in (6.3).

*Solution.* The error is at most
\[
\sum_{s\in\operatorname{supp}f}|f(s)|
\,|1-\langle\lambda_s\xi,\xi\rangle|.
\]
This bound is independent of the representation \(\pi\). It tends to zero for the vectors in Theorem 5.1, which justifies taking the supremum over all \(\pi\) in Theorem 6.1.

## References

[Takesaki] Masamichi Takesaki, *Theory of Operator Algebras III*, Encyclopaedia of Mathematical Sciences 127, Springer, 2003. [Publisher record](https://doi.org/10.1007/978-3-662-10453-8). The amenability results there include locally compact groups.
