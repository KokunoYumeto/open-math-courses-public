# Operator strength and local inverses

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026.  Public domain (CC0).*

The degree of a polynomial does not by itself measure the regularity of its equation. The operators with symbols \(\xi_1^2+i\xi_2\) and \(\xi_1^2+\xi_2^2\) both have degree two, but they control different derivatives. The relevant comparison uses all derivatives of the symbols. We develop that comparison, prove that it is forced by solvability with regularity, and build an inverse on a bounded open set without a boundary smoothness assumption.

The prerequisites are [Regular kernels and changes in the equation](regular-kernels-and-parameter-changes.md), [Measuring regularity with weighted Fourier spaces](weighted-fourier-spaces.md), and [Local regularity, sharp embeddings, and compactness](local-regularity-and-compactness.md). We use Plancherel's theorem to identify \(B_{2,1}\) with \(L^2\). Basic references are Grubb's open notes [Grubb], Melrose's open differential-analysis course [Melrose], and Malgrange's existence and approximation paper [Malgrange]. For singularity directions, we use the Fourier definition and cutoff lemma in [Wavefronts of regular kernels](wavefronts-of-regular-kernels.md#cutoffs-and-the-projection-onto-singular-support).

Throughout, \(P\ne0\), \(D=-i\partial\), and
\[
S_P(\xi)=\left(\sum_\alpha|\partial^\alpha P(\xi)|^2\right)^{1/2}.
\]
We write \(\mathcal E'(X)\) for distributions whose support is a compact subset of the open set \(X\). Such distributions extend by zero to \(\mathbb R^n\). A function with support merely in \(\overline X\) need not belong to \(\mathcal E'(X)\).

## Comparing what two equations control

We say that \(Q\) is **weaker than** \(P\), and write \(Q\prec P\), if
\[
S_Q(\xi)\leq C S_P(\xi)\qquad(\xi\in\mathbb R^n).
\tag{1}
\]
The zero polynomial is weaker than every nonzero polynomial. Two nonzero polynomials have **equal strength** if each is weaker than the other. The resulting comparison is transitive, and equal strength is an equivalence relation.

**Lemma 1.1.** A polynomial \(Q\) is weaker than \(P\) if and only if
\[
|Q(\xi)|\leq C S_P(\xi)\qquad(\xi\in\mathbb R^n).
\tag{2}
\]
Every polynomial weaker than a polynomial of degree \(m\) has degree at most \(m\). The set of weaker polynomials is a finite-dimensional complex vector space.

**Proof.** The zero polynomial satisfies both conditions. For a nonzero polynomial, equation (1) immediately implies (2). Conversely, let \(d=\deg Q\). On the finite-dimensional space of polynomials of degree at most \(d\), the supremum over the real unit ball is a norm: if the supremum is zero, the polynomial vanishes on an open set and all its coefficients vanish. Equivalence of finite-dimensional norms gives
\[
\left(\sum_\alpha|\partial^\alpha q(0)|^2\right)^{1/2}
\leq C_d\sup_{|h|\leq1}|q(h)|.
\]
Apply this to \(q(h)=Q(\xi+h)\). Using (2) and the moderate shift estimate for \(S_P\),
\[
S_Q(\xi)\leq C_d\sup_{|h|\leq1}|Q(\xi+h)|
\leq C'\sup_{|h|\leq1}S_P(\xi+h)
\leq C''S_P(\xi).
\]
This proves (1).

The polynomial derivative norm satisfies \(S_P(\xi)\leq C_P(1+|\xi|)^m\). If \(Q\) had degree \(d>m\), choose a real vector \(a\) on which its highest homogeneous part is nonzero. Then \(|Q(ta)|\) grows like \(|t|^d\), contradicting (2). Thus every weaker polynomial belongs to the finite-dimensional space of degree at most \(m\). That set is closed under addition and scalar multiplication by the triangle inequality for its derivative vector, so it is a vector subspace. \(\square\)

**Example 1.2.** Every derivative polynomial \(\partial^\alpha P\) is weaker than \(P\): its derivative vector consists of some of the entries already present in the derivative vector of \(P\). Lower degree alone is insufficient. For \(P(\xi_1,\xi_2)=\xi_1\), the polynomial \(Q=\xi_2\) is not weaker, since \(S_P(0,t)=1\) while \(|Q(0,t)|=|t|\).

**Example 1.3.** Let \(P(\xi_1,\xi_2)=\xi_1^2+i\xi_2\). Its derivative norm is
\[
S_P^2=\xi_1^4+\xi_2^2+4\xi_1^2+5.
\]
The weaker polynomials are exactly
\[
Q=a\xi_1^2+b\xi_2+c\xi_1+d,
\qquad a,b,c,d\in\mathbb C.
\tag{3}
\]
Each displayed term is bounded by a constant multiple of \(S_P\), so these polynomials are weaker. For the converse, Lemma 1.1 reduces \(Q\) to degree at most two. Along \(\xi_1=0\), the bound (2) excludes its \(\xi_2^2\) coefficient. If its \(\xi_1\xi_2\) coefficient were nonzero, set \(\xi_1=t\), \(\xi_2=t^2\). That term grows like \(t^3\), while the remaining terms and \(S_P\) grow at most like \(t^2\). Its coefficient must therefore vanish as well. This leaves (3).

## The exact gain for compact data

Fix a regular fundamental solution \(E\) of \(P(D)\). For every compactly supported distribution \(f\), the convolution \(E*f\) exists and satisfies \(P(D)(E*f)=f\).

**Theorem 2.1.** If \(f\in\mathcal E'(\mathbb R^n)\cap B_{p,k}\), where \(k\) is moderate and \(1\leq p\leq\infty\), then
\[
u=E*f\in B_{p,kS_P}^{\mathrm{loc}}(\mathbb R^n).
\tag{4}
\]
For fixed compact data support and a fixed output cutoff, the map in (4) is bounded. If \(Q\prec P\), then
\[
Q(D)u\in B_{p,k}^{\mathrm{loc}}.
\tag{5}
\]

**Proof.** For an output cutoff \(\chi\), choose \(\psi\in C_c^\infty\) equal to one on a neighborhood of \(\operatorname{supp}\chi-\operatorname{supp}f\). On a neighborhood of \(\operatorname{supp}\chi\),
\[
E*f=(\psi E)*f.
\]
The compact kernel \(\psi E\) belongs to \(B_{\infty,S_P}\). The weighted convolution estimate yields
\[
\|(\psi E)*f\|_{p,kS_P}
\leq\|\psi E\|_{\infty,S_P}\|f\|_{p,k}.
\]
Multiplication by \(\chi\) is bounded in this weighted space. This proves (4), including the stated continuity. The differential-operator estimate then places \(Q(D)u\) in \(B_{p,kS_P/S_Q}^{\mathrm{loc}}\) for \(Q\ne0\). Under (1) that space continuously embeds in \(B_{p,k}^{\mathrm{loc}}\). The zero operator is immediate. \(\square\)

**Theorem 2.2.** For \(u\in\mathcal E'(\mathbb R^n)\),
\[
u\in B_{p,kS_P}
\quad\Longleftrightarrow\quad
P(D)u\in B_{p,k}.
\tag{6}
\]
Consequently, if \(P(D)u\in B_{p,k}\), then
\[
P(D)(\chi u)\in B_{p,k}\qquad(\chi\in C_c^\infty).
\tag{7}
\]

**Proof.** The forward implication is the differential-operator estimate. For the reverse implication, the compact convolution identities give
\[
E*P(D)u=P(D)E*u=\delta_0*u=u.
\]
Apply Theorem 2.1 to \(f=P(D)u\). This puts \(u\) in the local space in (4). Since its support is compact, its local and global weighted memberships agree, proving (6). For (7), first use (6), then the cutoff estimate in \(B_{p,kS_P}\), and then the forward implication of (6). \(\square\)

Compact support is a real hypothesis here. A homogeneous solution can be irregular in uncontrolled directions, as the final exercises of the regular-kernels lesson show. Equation (6) should not be applied to an arbitrary global distributional solution.

### Which singularities a convolution can carry

The gain in Theorem 2.1 has the best possible weight in the same scale. Indeed, for any solution \(v\in B_{p,kS_P}^{\mathrm{loc}}\), the local differential-operator estimate gives \(P(D)v\in B_{p,k}^{\mathrm{loc}}\). If that right-hand side has compact support, its local and global memberships agree. Thus the condition on the datum in Theorem 2.1 is also necessary for a solution in that scale. This does not force every solution to have that regularity.

The wavefront estimate has a different character: it is an upper bound and can be strict.

**Theorem 2.3.** If \(u\in\mathcal D'(\mathbb R^n)\) and \(f\in\mathcal E'(\mathbb R^n)\), their convolution satisfies
\[
 \operatorname{WF}(u*f)\subseteq
 \{(a+b,\xi):(a,\xi)\in\operatorname{WF}(u),\
                    (b,\xi)\in\operatorname{WF}(f)\}.
 \tag{WF1}
\]
Every covector in this formula is nonzero. In particular, for the averaging fundamental solution \(E_\rho(P)\),
\[
 \operatorname{WF}(E_\rho(P)*f)\subseteq
 \{(a+b,\xi):(a,\xi)\in\mathcal F_P,\
                    (b,\xi)\in\operatorname{WF}(f)\},
 \tag{WF2}
\]
where \(\mathcal F_P\) is the closed localization carrier in [Wavefronts of regular kernels](wavefronts-of-regular-kernels.md#the-canonical-upper-bound). Both formulas allow compact distributions of arbitrary finite order.

**Proof for compact factors.** First let \(u\) also have compact support. Write \(A=\operatorname{supp}u\), \(B=\operatorname{supp}f\). Empty support gives zero convolution. Fix \((x_0,\xi_0)\) outside the right side of (WF1).

For each \((a,b)\in A\times B\) with \(a+b=x_0\), at least one of \((a,\xi_0)\), \((b,\xi_0)\) is regular for its corresponding distribution. Choose product neighborhoods \(U\times V\) of that pair so small that the regular factor has a cutoff equal to one on a neighborhood of the appropriate closure, and its localized transform decreases rapidly on a cone about \(\xi_0\). If \(a+b\ne x_0\), choose bounded product neighborhoods whose closed sums avoid a neighborhood of \(x_0\).

These product rectangles cover the compact set \(A\times B\). Choose a finite subcover and a positive number \(\delta\) such that the radius-\(\delta\) ball about every point of \(A\times B\) lies in one of the chosen rectangles. Here is the elementary compactness argument: around each point first choose a ball whose fourfold enlargement lies in a cover rectangle; take a finite cover by the smaller balls, and let \(\delta\) be the minimum of their radii. A point in one smaller ball has its radius-\(\delta\) ball inside that ball's doubled enlargement.

Choose finite smooth partitions \(\rho_l\) and \(\sigma_m\), each summing to one near \(A\) and \(B\) respectively, with supports in balls of radius less than \(\delta/10\), centered in those compact sets. Such partitions follow by choosing finitely many bump functions positive on a cover, dividing by their positive sum near the compact set, and multiplying by a compact cutoff equal to one there. Each product of two supports then lies in one of the chosen rectangles. Bilinearity gives the finite sum
\[
                     u*f=\sum_{l,m}(\rho_lu)*(\sigma_mf).
 \tag{WF3}
\]
For the rectangles whose closed sums avoid \(x_0\), choose one common open neighborhood \(W\) of \(x_0\) avoiding all those finitely many sums. Their convolution terms vanish on \(W\), by the support rule for compact convolution.

For every other rectangle, one localized factor is rapidly decreasing in a cone about \(\xi_0\). The cutoff lemma in [Wavefronts of regular kernels](wavefronts-of-regular-kernels.md#cutoffs-and-the-projection-onto-singular-support) shows that its further multiplication by \(\rho_l\) or \(\sigma_m\) retains rapid decrease on a smaller cone. Choose one cone about \(\xi_0\) with unit-sphere closure inside all the finitely many such cones.

For compact factors the Fourier transform of convolution is the product:
\[
       \widehat{(\rho_lu)*(\sigma_mf)}
                           =\widehat{\rho_lu}\,\widehat{\sigma_mf}.
 \tag{WF4}
\]
Indeed, evaluate the compact convolution pairing on an exponential, inserting cutoffs equal to one near the two supports. Its factorization into the two exponential pairings gives (WF4). The definition and differentiation identities for this compact convolution are proved in [Proper convolution and compact support](../prerequisites/proper-convolution-and-compact-support.html).

Each factor has a smooth Fourier transform of polynomial growth. One factor has arbitrary decay on the common cone, so their product does too. Multiply (WF3) by a compact smooth \(\chi\), supported in \(W\) and equal to one near \(x_0\). The vanishing terms disappear; the cutoff lemma preserves rapid decrease for every remaining term on a still smaller cone. The sum is finite, so \(\widehat{\chi(u*f)}\) decreases rapidly there. This proves (WF1) for compact factors.

**Localizing the unrestricted factor.** For the general \(u\), fix a relatively compact neighborhood \(W_0\) of \(x_0\). Choose \(\psi\in C_c^\infty\) equal to one near the compact set \(\overline W_0-B\). On \(W_0\) one has
\[
                             u*f=(\psi u)*f.
\]
The compact-factor result applies to \(\psi u\). The same cutoff lemma gives \(\operatorname{WF}(\psi u)\subseteq\operatorname{WF}(u)\), so (WF1) follows near \(x_0\), hence everywhere. This uses no growth condition on \(u\). For (WF2), Theorem 2.1 of the wavefront lesson gives \(\operatorname{WF}(E_\rho(P))\subseteq\mathcal F_P\); substitute it in (WF1). \(\square\)

**Example 2.4 (a strict wavefront bound).** In two variables let \(P(\xi)=\xi_1\) and \(f=D_1\delta_0\). For any fundamental solution \(E\),
\[
                          E*f=D_1E=\delta_0. \tag{WF5}
\]
The wavefront of \(f\) consists of every nonzero covector over zero. Its localized transform is \(\xi_1\); every open cone contains a ray on which that polynomial grows, so no direction is rapidly decreasing. The actual solution in (WF5) has only the same base point zero in its wavefront.

For this \(P\), the computation (W1) in the wavefront lesson gives
\[
 \mathcal F_P=(\{0\}\times(\mathbb R^2\setminus\{0\}))
                 \cup((\mathbb R e_1)\times(\mathbb R^*e_2)).
 \tag{WF6}
\]
Thus the right side of (WF2) also contains vertical covectors over nonzero points of the horizontal axis. They are absent from the actual solution delta. This proves that the wavefront upper bound can be strict even for the particular averaging inverse. A shifted point datum \(f=\delta_b\), by contrast, gives \(E*f=E(\cdot-b)\) and exactly translates its wavefront, as follows directly from the translated cutoff Fourier transform.

## Why weaker operators are necessary

The previous results provide regular solutions. Their converses do not require a common solution operator or a uniform estimate assumed in advance.

**Theorem 3.1.** Let \(X\subset\mathbb R^n\) be nonempty and open. Fix one moderate weight \(k\) and one \(p\in[1,\infty]\). The following are equivalent:

1. \(Q\prec P\).
2. For every \(f\in\mathcal E'(X)\cap B_{p,k}\), there is \(u\in\mathcal D'(X)\) satisfying \(P(D)u=f\) and \(Q(D)u\in B_{p,k}^{\mathrm{loc}}(X)\).
3. Every \(u\in\mathcal E'(X)\) with \(P(D)u\in B_{p,k}\) also satisfies \(Q(D)u\in B_{p,k}\).

**Proof.** The zero polynomial \(Q\) satisfies all three assertions. Assume \(Q\ne0\). Theorem 2.1 proves that (1) implies (2), by restricting \(E*f\) to \(X\). Theorem 2.2 and the differential-operator estimate show that (1) implies (3).

Assume (2). In \(X\), commutation gives
\[
Q(D)f=P(D)Q(D)u\in B_{p,k/S_P}^{\mathrm{loc}}(X).
\]
The left side has compact support in \(X\), so it belongs globally to \(B_{p,k/S_P}\). Apply Theorem 2.2 with \(Q\) in place of \(P\), and \(k/S_P\) in place of \(k\). We conclude that every \(f\in\mathcal E'(X)\cap B_{p,k}\) lies in \(B_{p,kS_Q/S_P}\). The sharp weight-inclusion criterion of the local-regularity lesson forces
\[
k(\xi)\frac{S_Q(\xi)}{S_P(\xi)}\leq Ck(\xi).
\]
Since \(k>0\), this is (1).

Assume (3). By Theorem 2.2 its premise is equivalent to \(u\in B_{p,kS_P}\), and its conclusion is equivalent to \(u\in B_{p,kS_Q}\). Thus (3) is a compact-support membership inclusion between these two weighted spaces on the nonempty open set \(X\). The same weight criterion gives \(kS_Q\leq CkS_P\), again proving (1). \(\square\)

The criterion is independent of the chosen \(p\) and \(k\). Those choices describe the desired regularity, but the obstruction to preserving it is the polynomial comparison itself. The necessity argument uses only existence for each datum; it does not assume that the solutions were chosen linearly.

## A bounded inverse on an arbitrary bounded open set

Let \(X\) now be bounded and open. Its boundary may be irregular and it may have several connected components. Extend \(f\in L^2(X)\) by zero to \(f_0\in L^2(\mathbb R^n)\), and define
\[
Tf=(E*f_0)|_X.
\tag{8}
\]
The support of \(f_0\) lies in the compact set \(\overline X\), so this convolution is defined.

**Theorem 4.1.** The map \(T:L^2(X)\to L^2(X)\) is bounded and satisfies
\[
P(D)Tf=f\quad\hbox{in }\mathcal D'(X).
\tag{9}
\]
For every \(Q\prec P\), \(Q(D)T\) is a bounded operator on \(L^2(X)\). Moreover,
\[
TP(D)u=u
\quad\hbox{if }u\in\mathcal E'(X)\hbox{ and }P(D)u\in L^2(X).
\tag{10}
\]
More precisely, one may choose a constant \(C_X\), depending on the chosen regular kernel and a cutoff, such that
\[
\|Q(D)Tf\|_{L^2(X)}
\leq C_X\sup_{\xi\in\mathbb R^n}
\frac{|Q(\xi)|}{S_P(\xi)}\,\|f\|_{L^2(X)}.
\tag{11}
\]

**Proof.** Choose \(\psi\in C_c^\infty(\mathbb R^n)\) equal to one near the compact set \(\overline X-\overline X\), and put \(F=\psi E\). On \(X\), \(E*f_0=F*f_0\). Regularity gives \(F\in B_{\infty,S_P}\), hence
\[
\sup_\xi |Q(\xi)\widehat F(\xi)|
\leq\|F\|_{\infty,S_P}
\sup_\xi\frac{|Q(\xi)|}{S_P(\xi)}.
\]
By Plancherel, convolution by \(Q(D)F\) is an \(L^2\) Fourier multiplier with the displayed bound. Restriction to \(X\) and zero extension from \(X\) both have norm at most one. This proves (11) with \(C_X=\|F\|_{\infty,S_P}\). The polynomial \(1\) is weaker than \(P\), since \(S_P\) has a positive global lower bound. Taking \(Q=1\) proves boundedness of \(T\) itself.

Using the original expression (8), the fundamental-solution identity gives (9). For (10), extend \(u\) by zero. Because its support is a compact subset of \(X\), this extension commutes with differentiation, and the zero extension of \(P(D)u\) is exactly \(P(D)\) of the extended distribution. Thus
\[
E*(P(D)u)_0=E*P(D)u_0=u_0.
\]
Restrict to \(X\). Theorem 2.2 also ensures that this \(u\) lies in \(L^2\), so the equality is in the claimed space. \(\square\)

The inverse has no prescribed boundary values. It solves the equation on \(X\) and recovers compactly supported inputs through (10). To impose a boundary condition requires a separate problem and additional compatibility or geometric hypotheses.

The quantitative bound (11) is useful when perturbing coefficients. For example, if
\[
R(x,D)=\sum_{\nu=1}^N b_\nu(x)Q_\nu(D),
\qquad Q_\nu\prec P,
\]
with bounded measurable \(b_\nu\), then
\[
\|RT\|_{L^2(X)\to L^2(X)}
\leq C_X\sum_\nu\|b_\nu\|_\infty
\sup_\xi\frac{|Q_\nu(\xi)|}{S_P(\xi)}.
\tag{12}
\]
Each \(Q_\nu(D)Tf\) is an \(L^2\) function, so the multiplication in this formula is defined. If the right side is less than one, the Neumann series for \((I+RT)^{-1}\) converges in operator norm, and
\[
T_R=T(I+RT)^{-1}
\]
satisfies \((P(D)+R(x,D))T_Rf=f\). This gives a right inverse for a sufficiently small perturbation on the chosen set. It asserts no constant-strength conclusion for large perturbations.

## Exercises with solutions

**Exercise 1 (entry).** Classify all polynomials weaker than \(P(\xi)=iv\cdot\xi+c\), where \(v\ne0\) is real and \(c\) is complex.

**Solution.** Lemma 1.1 gives degree at most one. Write \(Q(\xi)=a\cdot\xi+b\) with \(a\in\mathbb C^n\). On every real line \(\xi=t\eta\) with \(v\cdot\eta=0\), the weight \(S_P\) is constant. The bound for \(Q\) forces \(a\cdot\eta=0\). Both the real and imaginary parts of \(a\) are therefore real multiples of \(v\), so \(a=\lambda v\) with \(\lambda\in\mathbb C\). Conversely, every \(Q=\lambda v\cdot\xi+b\) is bounded by a constant multiple of \(1+|v\cdot\xi|\), which is comparable to \(S_P\). These are exactly the weaker polynomials.

**Exercise 2 (intermediate).** Compare the strengths of \(P(\xi_1,\xi_2)=\xi_1^2+i\xi_2\) and \(R(\xi_1,\xi_2)=\xi_1^2+\xi_2^2\). Give a frequency sequence that proves a strict comparison.

**Solution.** We have \(S_R\geq c(1+|\xi|^2)\), while \(S_P\leq C(1+|\xi|^2)\). Thus \(P\prec R\). Along \((0,t)\), \(S_R\) grows like \(t^2\) and \(S_P\) grows like \(|t|\), so \(S_R/S_P\to\infty\). Hence \(R\not\prec P\). Equal degrees do not give equal strength.

**Exercise 3 (intermediate).** Let \(X\) be any bounded open set, \(P\ne0\), and \(Q_1,\ldots,Q_N\prec P\). Show that for every \(f\in L^2(X)\), one can solve \(P(D)u=f\) so that every \(Q_\nu(D)u\) belongs to \(L^2(X)\). Does the theorem give a uniqueness statement?

**Solution.** Set \(u=Tf\). Equation (9) solves the equation, and (11) gives every requested derivative with its quantitative bound. Uniqueness is not claimed: one may add any \(L^2\) homogeneous solution having the indicated derivatives. For the transport equation on a rectangle, constants in the transport direction give elementary examples when its zero-order coefficient vanishes. In these transport examples, boundary or normalization conditions would be needed to select a unique solution.

**Exercise 4 (advanced).** For \(P(D)=D_1^2+iD_2\) on a bounded open \(X\subset\mathbb R^2\), consider
\[
A=P(D)+b_1(x)D_1^2+b_2(x)D_2+b_3(x)D_1+b_4(x).
\]
Give an explicit sufficient condition, in terms of (11), for an \(L^2\) right inverse. If the domain is nonempty, explain why the same argument does not admit an arbitrary term \(b_5(x)D_2^2\).

**Solution.** Put \(Q_1=\xi_1^2\), \(Q_2=\xi_2\), \(Q_3=\xi_1\), \(Q_4=1\), and
\(M_\nu=\sup|Q_\nu|/S_P<\infty\). A sufficient condition is
\[
C_X\sum_{\nu=1}^4M_\nu\|b_\nu\|_\infty<1.
\]
Then (12) gives a convergent Neumann series and the right inverse \(T(I+RT)^{-1}\). The polynomial \(\xi_2^2\) is not weaker than \(P\); along \((0,t)\), its ratio to \(S_P\) tends to infinity. On a nonempty domain, Theorem 3.1 shows that one cannot obtain the required derivative for every compact \(L^2\) datum under this equation. On such a domain, making \(b_5\) small does not supply the missing bounded multiplier estimate for \(D_2^2T\). For the empty domain, all the relevant function spaces are zero, and the sufficient condition above still applies.

## References

- [Grubb] Gerd Grubb, *Distributions and Operators*, open lecture-note versions, 2007–2008, sections on Fourier transformation and convolution. [Author's lecture-note index](https://web.math.ku.dk/~grubb/distribution.htm).
- [Melrose] Richard Melrose, *Differential Analysis*, MIT OpenCourseWare, Fall 2004, sections on constant-coefficient operators and Sobolev estimates. [Open course](https://ocw.mit.edu/courses/18-155-differential-analysis-fall-2004/).
- [Malgrange] Bernard Malgrange, *Existence et approximation des solutions des équations aux dérivées partielles et des équations de convolution*, Annales de l'Institut Fourier **6** (1956), 271–355. [Original article](https://aif.centre-mersenne.org/articles/10.5802/aif.65/).
- [Hörmander II] Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983; 2005 reprint. Regular fundamental solutions, comparison of operators and local solvability.
