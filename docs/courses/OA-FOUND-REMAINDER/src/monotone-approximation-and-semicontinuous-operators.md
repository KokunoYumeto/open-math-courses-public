# Monotone approximation and semicontinuous operators

*Written by GPT-6.1 Sol (OpenAI), Ultra, September–October 2026. Self-checked by the writing AI. Original text: CC0 1.0.*

Lower semicontinuity on the quasi-state space has an operator interpretation: the element is a norm limit of bounded increasing limits from the original algebra. More precisely, every positive scalar shift of it is already one such increasing limit. The scalar shift matters for a nonunital algebra, where negative multiples of the bidual identity need not have this property.

We prove this characterization, its positive version, and the corresponding result after adjoining the bidual identity. We also prove the resolvent estimates that turn one-sided weak approximation into strong approximation, and identify a natural closed Jordan algebra of differences of semicontinuous elements.

Use [Affine approximation and quasi-state spaces](../reader/affine-approximation-and-quasi-state-spaces.html#1-supporting-affine-functions), particularly Theorem 1.2, and its [evaluation model](../reader/affine-approximation-and-quasi-state-spaces.html#3-the-compact-space-of-positive-functionals), Theorems 3.1–3.2. The bidual, normal positive functionals and bounded monotone convergence are the prerequisites in [The universal enveloping von Neumann algebra](../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html#oa-fnd-wa-03), in its faithful nondegenerate universal representation. For the directed approximate identity consisting of all positive elements in the open unit ball, we use the complete proof of Theorem 11.4 and Corollary 11.5 of [C*-algebras and continuous functional calculus](../../foundations-of-von-neumann-algebras/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html#OA-FND-CF-19). Continuous functional calculus is used throughout. Brown’s freely readable *Semicontinuity and closed faces of C*-algebras* treats the same semicontinuity and scalar-shift characterizations. The proofs below include the directedness estimates and the strong resolvent argument.

## 1. Order limits and rational functions

The zero algebra satisfies all the assertions immediately. Below fix a nonzero C*-algebra \(A\), and identify it with its canonical image in \(M=A^{**}\). Put
\[
A_1=A+\mathbb C1\subset M.
\]
Here \(1\) is the identity of \(M\). Thus \(A_1=A\) when \(A\) is unital. If \(A\) is nonunital, \(A_1\) is its unitization inside \(M\).

For a subset \(V\subset M_{\mathrm{sa}}\), write \(V^\uparrow\) for all limits of norm-bounded increasing nets in \(V\), and \(V^\downarrow\) for the analogous decreasing limits. Bounded monotone convergence gives the same limit strongly, sigma strongly and ultraweakly. Define
\[
C=\overline{A_{\mathrm{sa}}^\uparrow}^{\|\cdot\|},
\qquad C_+=\overline{A_+^\uparrow}^{\|\cdot\|}.
\tag{1.1}
\]
The upper closure of a real linear space is additive and invariant under positive scalars: use the product directed set to add two bounded increasing nets. Also \(A_{\mathrm{sa}}^\downarrow=-A_{\mathrm{sa}}^\uparrow\).

We will use elementary inverse order. If \(0<B\le D\), with both elements positive and invertible, then
\[
D^{-1}\le B^{-1}.
\tag{1.2}
\]
Indeed \(B^{-1/2}DB^{-1/2}\ge1\); its inverse is at most one by functional calculus. Conjugating back proves (1.2).

For \(\alpha>0\), define
\[
f_\alpha(t)=\frac{t}{1+\alpha t},\qquad t>-1/\alpha.
\tag{1.3}
\]
Since \(f_\alpha(x)=\alpha^{-1}(1-(1+\alpha x)^{-1})\), inverse order proves that \(f_\alpha\) is operator monotone on this domain. It vanishes at zero, so \(f_\alpha(a)\in A\) for \(a\in A_{\mathrm{sa}}\) with spectrum in the domain; it preserves positivity as well.

On a bounded spectral interval in the domain, continuous functional calculus preserves strong convergence of uniformly bounded self-adjoint nets. To see this, approximate the continuous function uniformly by polynomials on that interval. Products preserve strong convergence for uniformly bounded families, and the uniform error bounds apply to every operator and vector. In particular a bounded increasing net \(x_i\uparrow x\) with a common strict lower bound above \(-1/\alpha\) has \(f_\alpha(x_i)\uparrow f_\alpha(x)\) strongly.

## 2. Lower semicontinuity on the quasi-state space

For \(x\in M_{\mathrm{sa}}\), write \(\widehat x(\varphi)=\varphi(x)\) on \(Q(A)\). The pairing uses the unique normal extension of \(\varphi\) to \(M\).

**Theorem 2.1.** The following conditions are equivalent:

1. \(x\in C\).
2. \(\widehat x\) is lower semicontinuous on \(Q(A)\).
3. There is a norm-bounded increasing net \(b_i=a_i+\alpha_i1\in(A_1)_{\mathrm{sa}}\) with limit \(x\), where \(a_i\in A_{\mathrm{sa}}\) and \(\alpha_i\uparrow0\).
4. \(x+\delta1\in A_{\mathrm{sa}}^\uparrow\) for every \(\delta>0\).

**Proof.** If \(x\in A_{\mathrm{sa}}^\uparrow\), normality gives
\[
\widehat x(\varphi)=\sup_i\varphi(a_i),\qquad\varphi\in Q(A).
\]
This is a supremum of continuous functions and hence lower semicontinuous. Norm convergence implies uniform convergence of the evaluation functions; uniform limits preserve lower semicontinuity. Thus 1 implies 2.

Assume 2. The increasing affine-support theorem gives continuous ambient affine functions
\[
g_i(\varphi)=\varphi(a_i)+\alpha_i\uparrow\widehat x(\varphi).
\tag{2.1}
\]
Evaluation at zero gives \(\alpha_i\uparrow0\). On states, the functions in (2.1) are evaluations at \(b_i=a_i+\alpha_i1\). State norming therefore makes \(b_i\) increasing and \(b_i\le x\).

We can take a cofinal part of the affine-support family lying above the constant function \(-R\), where \(R=\|x\|+1\). This is a strict affine minorant on all of \(Q(A)\). Consequently
\[
-R1\le b_i\le x,
\tag{2.2}
\]
so the net is norm bounded. Its supremum has the same value as \(x\) on every normal state, by (2.1), hence equals \(x\). This proves 3, with the useful lower bound (2.2).

Assume 3 and fix \(\delta>0\). Choose \(b>0\) with \(3b<\delta\), and pass to a tail on which \(\alpha_i>-b\). Let
\[
\mathcal U=\{u\in A_+:\|u\|<1\},
\]
ordered by operator order. The stated approximate-identity theorem says this set is directed and its net increases strongly to \(1\) in \(M\). Consider the elements
\[
y_{i,r,u}=a_i+(\alpha_i+r)u\in A_{\mathrm{sa}},
\qquad 3b<r<\delta,\quad u\in\mathcal U.
\tag{2.3}
\]
We order this family by the order of its elements, rather than by a product order on its parameters. We will prove it is directed.

Given \(y_{i,r,u}\) and \(y_{j,s,v}\), choose \(k\ge i,j\) and \(t\) with \(\max(r,s)<t<\delta\). Put \(d=a_k-a_i\), \(\beta=\alpha_k-\alpha_i\ge0\), and \(q=t-r>0\). Increasingness of \(b_i\) gives \(d+\beta1\ge0\). Functional calculus gives a strict positive contraction
\[
w_i=\frac{|d|}{q+|d|}\in\mathcal U.
\]
Choose \(w\in\mathcal U\) dominating \(u,v,w_i\), and also the corresponding cutoff for \(a_k-a_j\) with \(t-s\). The coefficient \(\alpha_i+r\) is positive. Therefore
\[
y_{k,t,w}-y_{i,r,u}
\ge d+(\beta+q)w
\ge d+(\beta+q)\frac{|d|}{q+|d|}.
\]
The last expression is
\[
\frac{q(d+|d|)+(d+\beta1)|d|}{q+|d|}\ge0.
\tag{2.4}
\]
All factors in this expression commute, and both numerator terms are positive. The same computation for \(j\) shows \(y_{k,t,w}\) dominates both given elements.

This directed family is norm bounded. If \(b_i\ge-R1\), then \(a_i=b_i-\alpha_i1\ge-R1\), since \(\alpha_i\le0\). Thus
\[
-R1\le y_{i,r,u}\le a_i+(\alpha_i+r)1
=b_i+r1\le x+\delta1.
\tag{2.5}
\]
For fixed \(i,r\), its strong limit as \(u\uparrow1\) is \(b_i+r1\). Any upper bound for the whole family therefore majorizes all \(b_i+r1\), then \(x+r1\), and finally \(x+\delta1\) as \(r\uparrow\delta\). In view of (2.5), its supremum is \(x+\delta1\). This proves 4.

Finally, 4 implies 1 because \(\|x+\delta1-x\|=\delta\) and \(\delta\downarrow0\). \(\square\)

**Remark 2.2 — a uniform lower bound.** For every \(\delta>0\), the construction from condition 2 may use the same \(R=\|x\|+1\) in (2.5). Only the tail on which \(\alpha_i>-b\) depends on \(\delta\). This observation will ensure that rational functions can be applied on a common spectral domain.

## 3. Positive approximants

**Proposition 3.1.** If \(x\in C\) and \(x\ge0\), then
\[
x+\delta1\in A_+^\uparrow\quad(\delta>0).
\tag{3.1}
\]
Consequently \(C\cap M_+=C_+\).

**Proof.** Use the construction above, with \(0<b<\delta/3\) and \(\alpha_i>-b\). The functions
\[
\varphi\longmapsto\varphi(a_i)+(\alpha_i+b)\|\varphi\|
=\widehat{b_i+b1}(\varphi)
\tag{3.2}
\]
are lower semicontinuous on \(Q(A)\): their first term is continuous and their second is a positive multiple of the lower semicontinuous norm. They increase pointwise to \(\widehat{x+b1}\), which is nonnegative.

The closed sets on which (3.2) is at most \(-b\) are compact and decreasing, with empty intersection. Compactness implies one is empty, and all later ones are empty. Evaluation on states then gives
\[
a_i+(\alpha_i+2b)1\ge0
\tag{3.3}
\]
on a tail.

In (2.3) restrict to that tail, and require in addition
\[
u\ge\frac{|a_i|}{b+|a_i|}.
\tag{3.4}
\]
The restricted family remains directed and cofinal: when choosing an upper element, impose its additional cutoff together with the finitely many previous cutoffs. For its members, \(r>3b\) and \(\alpha_i+r>0\) give
\[
y_{i,r,u}
\ge a_i+(\alpha_i+3b)\frac{|a_i|}{b+|a_i|}
=\frac{b(a_i+|a_i|)+(a_i+(\alpha_i+2b)1)|a_i|}{b+|a_i|}
\ge0.
\]
Again the products commute and (3.3) makes them positive. The family is bounded and has supremum \(x+\delta1\), proving (3.1).

Letting \(\delta\downarrow0\) proves \(C\cap M_+\subset C_+\). The reverse inclusion follows because positive elements remain positive under monotone and norm limits, and \(A_+^\uparrow\subset A_{\mathrm{sa}}^\uparrow\). \(\square\)

**Corollary 3.2 — rational stability.** If \(x\in C\), then \(f_\alpha(x)\in C\) for all sufficiently small \(\alpha>0\). If \(x\in C_+\), then \(f_\alpha(x)\in C_+\) for every \(\alpha>0\).

**Proof.** For the first assertion use Remark 2.2 and choose \(\alpha R<1\). For each small \(\delta>0\), the bounded increasing approximants to \(x+\delta1\) have common lower bound \(-R1\). Applying \(f_\alpha\) therefore gives a bounded increasing net in \(A_{\mathrm{sa}}\) with limit \(f_\alpha(x+\delta1)\). As \(\delta\downarrow0\), those limits converge in norm to \(f_\alpha(x)\), proving membership in \(C\).

For positive \(x\), Proposition 3.1 gives positive approximants. The rational function is positive and bounded by \(1/\alpha\) on \([0,\infty)\), so no smallness condition on \(\alpha\) is needed. Their limits and the final norm limit belong to \(C_+\). \(\square\)

## 4. What adjoining the identity changes

**Theorem 4.1.** For \(x\in M_{\mathrm{sa}}\), the following are equivalent:

1. \(x\in(A_1)_{\mathrm{sa}}^\uparrow\).
2. \(x\in\mathbb R1+C\).
3. \(\widehat x|_{S(A)}\) has a bounded lower semicontinuous affine extension to \(Q(A)\).

The extension in condition 3 is not required to vanish at zero.

**Proof.** Suppose first that \(A\) is nonunital, and let
\(a_i+\alpha_i1\uparrow x\) be a norm-bounded net. The quotient character
\(\varepsilon:A_1\to\mathbb C\), \(\varepsilon(a+\alpha1)=\alpha\), is positive and contractive. Thus \(\alpha_i\) is bounded increasing, with a finite limit \(\alpha\). The net
\[
a_i+(\alpha_i-\alpha)1\uparrow x-\alpha1
\]
satisfies condition 3 of Theorem 2.1, so \(x-\alpha1\in C\). This proves 1 implies 2. In the unital case, condition 1 already implies \(x\in C\).

If \(x=\alpha1+y\), \(y\in C\), the function
\[
\varphi\longmapsto\widehat y(\varphi)+\alpha
\]
is a bounded lower semicontinuous affine extension of \(\widehat x\) from the states. Thus 2 implies 3.

Conversely, approximate the extension in condition 3 increasingly by continuous ambient affine functions
\(g_i(\varphi)=\varphi(a_i)+\alpha_i\), using the affine-support theorem. On states these are the evaluations of \(a_i+\alpha_i1\). They are increasing and at most \(\widehat x\). Restricting to a cofinal family above a constant strict minorant gives a uniform operator lower bound, just as in (2.2). Hence these elements form a norm-bounded increasing net in \((A_1)_{\mathrm{sa}}\). Its supremum has the values of \(x\) on all normal states, so it equals \(x\). This proves 3 implies 1.

For completeness, membership in condition 2 also directly gives condition 1: Theorem 2.1 gives \(y+1\in A_{\mathrm{sa}}^\uparrow\), and subtracting \(1\), then adding \(\alpha1\), preserves increasingness and places the approximants in \((A_1)_{\mathrm{sa}}\). \(\square\)

Define the norm-closed real space
\[
J=\overline{A_{\mathrm{sa}}^\uparrow-A_{\mathrm{sa}}^\uparrow}^{\|\cdot\|}.
\tag{4.1}
\]
An increasing positive contractive approximate identity gives \(1\in A_{\mathrm{sa}}^\uparrow\), so \(J\) contains \(\mathbb R1\) and \(C\). Theorem 4.1 therefore gives
\[
J=\overline{(A_1)_{\mathrm{sa}}^\uparrow-(A_1)_{\mathrm{sa}}^\uparrow}^{\|\cdot\|}.
\tag{4.2}
\]
The inclusion from left to right is immediate; for the other inclusion both upper-limit terms belong to \(\mathbb R1+C\subset J\).

## 5. Strong resolvent estimates

The following estimate needs no uniform norm bound on the original net.

**Lemma 5.1.** Let \(x_i,x\) be bounded self-adjoint operators on a Hilbert space, and suppose \(x_i\to x\) weakly as operators.

1. If \(x_i\le x\) and \(1-\alpha x\ge\varepsilon1\) for some \(\alpha,\varepsilon>0\), then
\[
(1-\alpha x_i)^{-1}\longrightarrow(1-\alpha x)^{-1}
\quad\text{strongly}.
\tag{5.1}
\]
2. If \(x_i\ge x\ge0\) and \(\alpha>0\), then
\[
f_\alpha(x_i)\longrightarrow f_\alpha(x)
\quad\text{strongly}.
\tag{5.2}
\]

Each \(x_i\) is an operator of finite norm; the norms of the family may be unbounded.

**Proof.** We prove a common estimate. Let \(D_i\ge D\ge\varepsilon1\) be positive invertible operators with \(D_i\to D\) weakly. Set
\[
B=D^{-1},\qquad B_i=D_i^{-1},\qquad T_i=D_i-D\ge0.
\]
Inverse order gives \(0\le B_i\le B\). The resolvent identity and an elementary positive bound give
\[
B-B_i=B_iT_iB,
\qquad B_iT_iB_i=B_i-B_iDB_i\le B_i\le B.
\]
Thus, for every vector \(\xi\),
\[
\begin{aligned}
\|(B-B_i)\xi\|^2
&=\|B_iT_i^{1/2}T_i^{1/2}B\xi\|^2\\
&\le\|B_iT_i^{1/2}\|^2\langle T_iB\xi,B\xi\rangle\\
&\le\|B\|\langle T_iB\xi,B\xi\rangle\longrightarrow0.
\end{aligned}
\tag{5.3}
\]
The last limit uses weak operator convergence on the fixed vector \(B\xi\); the bound uses \(\|B_iT_i^{1/2}\|^2=\|B_iT_iB_i\|\le\|B\|\).

For part 1 take \(D_i=1-\alpha x_i\), \(D=1-\alpha x\). For part 2 take \(D_i=1+\alpha x_i\), \(D=1+\alpha x\), and then use
\(f_\alpha(x_i)=\alpha^{-1}(1-D_i^{-1})\). \(\square\)

## 6. The Jordan algebra of differences

**Theorem 6.1.** The space \(J\) in (4.1) is a norm-closed real Jordan algebra: it is closed under
\[
x\circ y=\tfrac12(xy+yx).
\tag{6.1}
\]
For each \(x\in J\), the self-adjoint part of the unital C*-algebra generated by \(x\) lies in \(J\).

**Proof.** It is already a closed real linear space containing \(1\). If \(x\in A_{\mathrm{sa}}^\uparrow\), then \(x\in C\), and Corollary 3.2 puts \(f_\alpha(x)\in C\subset J\) for small \(\alpha>0\). Therefore
\[
\frac{x-f_\alpha(x)}{\alpha}
=x^2(1+\alpha x)^{-1}\longrightarrow x^2
\quad\text{in norm},
\]
so \(x^2\in J\).

If \(x=y-z\) with \(y,z\in A_{\mathrm{sa}}^\uparrow\), then \(y+z\) is also in that cone. The identity
\[
(y-z)^2=2y^2+2z^2-(y+z)^2
\]
proves \(x^2\in J\). Norm continuity of squaring extends this conclusion to all \(x\in J\). Polarization now gives
\[
xy+yx=(x+y)^2-x^2-y^2\in J,
\]
which proves (6.1).

Since powers of one self-adjoint \(x\) commute, \(x\circ x^n=x^{n+1}\). Thus \(J\) contains all real polynomials in \(x\) and \(1\). Uniform polynomial approximation on the real compact spectrum of \(x\) puts \(g(x)\in J\) for every real continuous \(g\). This is precisely the self-adjoint part of its generated unital C*-algebra. \(\square\)

**Example 6.2 — a scalar that belongs to one closure but not the other.** For \(A=c_0\), the positive identity of \(A^{**}=\ell^\infty\) is an increasing limit of finite-support positive contractions, so \(1\in A_+^\uparrow\). But \(-1\notin C\): along the weak* convergent point masses \(\delta_n\to0\),
\[
\widehat{-1}(\delta_n)=-1<0=\widehat{-1}(0),
\]
violating lower semicontinuity. Nevertheless \(-1\in(A_1)_{\mathrm{sa}}\), and \(-1\in J\). The separate roles of \(C\), adjoining constants, and taking differences are visible even in this commutative example.

## 7. Graded exercises with solutions

**Exercise 7.1 — introductory: all three spaces for \(c_0\).** For a bounded real sequence \(x=(x_n)\), prove
\[
x\in C\quad\Longleftrightarrow\quad\liminf_{n\to\infty}x_n\ge0.
\]
Show that \(C=A_{\mathrm{sa}}^\uparrow\) in this case, whereas \((A_1)_{\mathrm{sa}}^\uparrow=J=\ell^\infty_{\mathrm{sa}}\).

**Solution.** If \(x\in C\), Theorem 2.1 gives lower semicontinuity of \(\widehat x\) at zero. Since \(\delta_n\to0\) weak*, this forces \(0\le\liminf x_n\).

Conversely, this liminf condition says the negative part \(x_-\) belongs to \(c_0\). Let \(p_N\) be the indicator of the first \(N\) coordinates, and put
\[
a_N=p_Nx_+-x_-\in c_0.
\]
This is a uniformly bounded increasing sequence, with coordinatewise supremum \(x\), hence strong supremum in \(\ell^\infty\). Thus \(x\in A_{\mathrm{sa}}^\uparrow\subset C\), proving both assertions about \(C\).

Every bounded real \(x\) can be written \(x=-\|x\|1+(x+\|x\|1)\), with its second term positive and in \(C\). Theorem 4.1 gives \(x\in(A_1)_{\mathrm{sa}}^\uparrow\). Similarly \(x=x_+-x_-\) is a difference of two bounded positive sequences, each in \(A_+^\uparrow\). Thus \(J\) is the whole self-adjoint bidual here.

**Exercise 7.2 — intermediate: a convergent net with unbounded tails.** On an infinite-dimensional Hilbert space \(H\), direct pairs \((F,t)\) by inclusion of finite-dimensional subspaces \(F\) and increasing \(t>0\). Let \(P_F\) be the projection onto \(F\), and put
\[
x_{F,t}=t(1-P_F).
\]
Show that \(x_{F,t}\to0\) strongly, while the operator norms are unbounded on every tail. Compute \(f_\alpha(x_{F,t})\) and its strong limit. Explain why the resolvent estimate can be used without assuming a bounded original family.

**Solution.** Given \(\xi\in H\), once \(F\) contains the one-dimensional span of \(\xi\), every later \(x_{F,t}\) annihilates \(\xi\). This proves strong convergence. On the other hand, after any fixed pair \((F_0,t_0)\), the pairs \((F_0,t)\), \(t\ge t_0\), remain in its tail. Since \(H\) is infinite dimensional, \(1-P_{F_0}\ne0\), and \(\|x_{F_0,t}\|=t\) is unbounded.

Functional calculus on the two spectral values gives
\[
f_\alpha(x_{F,t})=\frac{t}{1+\alpha t}(1-P_F).
\]
This family is bounded by \(1/\alpha\) and converges strongly to zero, again because each fixed vector is eventually annihilated. Here \(x_{F,t}\ge0\) and weak operator convergence also holds, so Lemma 5.1 applies. A convergent net may have an unbounded family, even on every tail; the uniform bound in that lemma comes from the inverses, not from such an assumption on \(x_i\).

**Exercise 7.3 — advanced: compact operators and their bidual.** Let \(A=\mathcal K(H)\) for an infinite-dimensional Hilbert space, so \(A^{**}=B(H)\). Show that every positive \(x\in B(H)\) belongs to \(A_+^\uparrow\), and deduce \(J=B(H)_{\mathrm{sa}}\). Prove that \(-1\notin C\), despite \(J\) being this large.

**Solution.** Direct the finite-dimensional subspaces of \(H\) by inclusion. The finite-rank operators
\[
a_F=x^{1/2}P_Fx^{1/2}\in\mathcal K(H)_+
\]
increase, are bounded by \(x\), and converge strongly to \(x\) since \(P_F\uparrow1\). Thus every positive element is in \(A_+^\uparrow\). Every self-adjoint element of \(B(H)\) is a difference of two positive elements, so (4.1) gives \(J=B(H)_{\mathrm{sa}}\).

Choose an orthonormal sequence \((\xi_n)\), and let \(\varphi_n(a)=\langle a\xi_n,\xi_n\rangle\). These are norm-one positive functionals on \(\mathcal K(H)\). They converge weak* to zero: finite-rank operators send the orthonormal sequence to norm-null vectors, and norm approximation gives the same conclusion for every compact operator. Their normal extensions satisfy \(\varphi_n(-1)=-1\). Thus \(\widehat{-1}\) is not lower semicontinuous at zero on \(Q(A)\). Theorem 2.1 excludes \(-1\) from \(C\).

## References

[Brown] Lawrence G. Brown, [*Semicontinuity and closed faces of C*-algebras*](https://arxiv.org/abs/1312.3624v2), arXiv:1312.3624v2, 11 July 2014.
