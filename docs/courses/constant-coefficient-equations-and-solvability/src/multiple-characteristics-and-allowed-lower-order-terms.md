# Multiple characteristics and allowed lower order terms

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Multiple roots constrain lower order terms through more than their degree. They force vanishing at characteristic points, but the resulting multiplicity condition can still be too weak. We derive the exact condition from polynomial strength, identify when every lower order completion is allowed, and compare repeated, tangent and transverse Lorentz cones.

Read [Hyperbolicity and lower order terms](hyperbolicity-and-lower-order-terms.md), especially its eight equivalent criteria and shifted derivative estimate, and [Rescaled symbols and stable strength](rescaled-symbols-and-stable-strength.md). We use their full proofs, product comparison, and principal-type criterion. Throughout \(P=\sum_{j=0}^mP_j\), \(P_j\) is homogeneous of degree \(j\), and all coefficients may be complex. Hyperbolicity refers to a nonzero real \(N\), a nonzero principal value \(P_m(N)\), and a negative imaginary root barrier for the full polynomial.

## Which directions the full equation ignores

Let \(A(F)=\{\eta\in\mathbb R^n\colon\partial_\eta F\equiv0\}\). If \(\eta\in A(P_m)\), condition 1 in the comparison theorem gives, for every fixed real \(\xi\),
\[
|P(\xi+iN+s\eta)|\le C|P_m(\xi+iN)|\qquad(s\in\mathbb R).
\]
The left side is the absolute value of a polynomial in \(s\). A polynomial bounded on the full real line is constant; hence \(\partial_\eta P(\xi+iN)=0\) for every real \(\xi\). A complex polynomial vanishing on a real affine translate is identically zero: successively fix all but one real coordinate, apply the one-variable identity principle, and continue. Thus \(\eta\in A(P)\). Conversely \(\partial_\eta P=0\) forces its highest homogeneous component \(\partial_\eta P_m=0\). Therefore \(A(P)=A(P_m)\).

## Vanishing at multiple characteristics

Suppose \(\xi\) is real and not proportional to \(N\), and \(t_0\) is a root of \(t\mapsto P_m(\xi+tN)\) of multiplicity \(\mu\). Set \(v=\xi+t_0N\); the principal-part proof makes \(t_0\) real, and \(v\ne0\). Then
\[
\partial_N^kP_m(v)=0\quad(k<\mu).
\]
The finite Taylor expansion in the \(iN\) direction gives, for large positive \(s\),
\[
\begin{aligned}
P_m(sv+iN)&=
\sum_{k=\mu}^{m}\frac{i^k}{k!}s^{m-k}\partial_N^kP_m(v)\\
&=O(s^{m-\mu}).
\end{aligned}
\]
Condition 4, fixed-shift comparison and the shifted derivative estimate in the comparison theorem imply
\[
|\partial^\alpha P_{m-j}(sv)|\le C_\alpha |P_m(sv+iN)|.
\]
But the left side equals \(s^{m-j-|\alpha|}|\partial^\alpha P_{m-j}(v)|\) when \(|\alpha|\le m-j\). If \(|\alpha|<\mu-j\), its exponent exceeds \(m-\mu\), so that derivative at \(v\) must be zero. Hence \(P_{m-j}\) has multivariable vanishing order at least \(\mu-j\) at \(v\), for \(0\le j<m\); a nonpositive requested order imposes no condition. Proportional \(\xi\) is excluded exactly as in its statement.

## Strict hyperbolicity

For \(m\ge 1\), the following are equivalent for the fixed homogeneous principal part \(F=P_m\):

- \(F\) is hyperbolic with respect to \(N\), and \(\nabla F(v)\ne0\) at every nonzero real \(v\).
- \(F(N)\ne0\), and \(F(\xi+tN)\) has only simple real roots for every real \(\xi\) not proportional to \(N\).
- Every polynomial \(F+Q\), \(\deg Q<m\), is hyperbolic with respect to \(N\).

The first implies the third because Theorem 4.2 in *Rescaled symbols and stable strength* makes every such \(Q\) dominated by \(F\), and the comparison theorem applies. The third includes \(Q=0\), giving homogeneous hyperbolicity. If a real \(N\)-line not proportional to \(N\) had a multiple root at \(v\ne0\), choose a homogeneous polynomial \(Q\) of degree \(m-1\) with \(Q(v)\ne0\). Such a polynomial exists by taking a real linear functional nonzero at \(v\) to the \((m-1)\)-st power, times any nonzero complex constant. Hyperbolicity of \(F+Q\) contradicts the multiplicity result with \(\mu\ge 2,j=1\). Thus the third implies the second.

The second gives homogeneous hyperbolicity also on proportional lines, where \(F(aN+tN)=F(N)(a+t)^m\) has only real roots. At any nonzero characteristic \(v\), \(v\) is not proportional to \(N\); the simple zero at \(t=0\) of \(F(v+tN)\) makes \(\partial_NF(v)\ne0\). At a noncharacteristic \(v\), Euler's identity \(v\cdot\nabla F(v)=mF(v)\ne0\) also gives \(\nabla F(v)\ne0\). Therefore the second implies the first. The argument proves the equivalence without assuming directional simplicity from gradient nonvanishing.

A polynomial is called **strictly hyperbolic** in direction \(N\) when its principal part satisfies these equivalent conditions. The statement concerns \(m\ge 1\); nonzero constants retain their separate trivial hyperbolicity convention. In one dimension every \(\xi\) is proportional to \(N\), so the simple-root test has an empty test set. A nonzero univariate homogeneous monomial has nonzero gradient away from zero, and every univariate completion has finitely many roots and is hyperbolic. The convention is therefore consistent.

For the Lorentz form \(F(x_0,x')=x_0^2-|x'|^2\), its gradient is nonzero away from the origin. If \(F(N)>0\), the discriminant of \(F(\xi+tN)\) is
\[
4\bigl((N_0\xi_0-N'\cdot\xi')^2-F(N)F(\xi)\bigr).
\]
It is positive whenever \(\xi\) is not proportional to the timelike \(N\). To verify this directly, let \(B(v,w)=v_0w_0-v'\cdot w'\) and write \(\xi=aN+w\), \(a=B(N,\xi)/F(N)\). Then \(B(N,w)=0\), so \(w_0=N'\cdot w'/N_0\), and
\[
F(w)\le-\frac{F(N)}{N_0^2}|w'|^2.
\]
Here \(N_0\ne0\); \(w\ne0\) implies \(w'\ne0\). The expression inside the discriminant is \(-F(N)F(w)>0\). Thus every timelike direction is strictly hyperbolic, including both orientations.

## Three quartic examples

Use real coordinates \((x,y,z)\) and time direction \(N=e_x\); all lower-order coefficients may be complex. Let \(P=P_4+P_3+P_2+P_1+P_0\), with each part homogeneous. In every example below, the restriction stated on \(P_3\) is both necessary and sufficient; the parts of degree at most two are arbitrary.

Each Lorentz quadratic \(Q=x^2-a y^2-b z^2\), \(a,b>0\), is hyperbolic in direction \(e_x\), is of principal type, and satisfies \(S_Q(\xi, 1)\ge c(1+|\xi|)\) by its gradient and nonzero second derivatives. The product comparison therefore gives
\[
S_{Q_1Q_2}(\xi, 1)\ge c'(1+|\xi|)^2.
\tag{1}
\]
Consequently every degree-at-most-two polynomial is weaker than the quartic product. Every linear form is weaker than either quadratic, so \(Q_1L\prec Q_1Q_2\) and \(Q_2L\prec Q_1Q_2\). These observations justify all the sufficiency claims rather than dropping the quadratic and smaller parts.

**(a) A repeated Lorentz cone.** Put \(Q=x^2-y^2-z^2\), \(P_4=Q^2\). At every nonzero null point \(Q(v)=0\), the \(e_x\)-root is simple for \(Q\), since \(x\ne0\), so it has multiplicity two for \(Q^2\). The multiplicity result requires \(P_3(v)=0\) on the full null cone. Divide the cubic by the monic polynomial \(Q\) in \(x\):
\[
P_3=QL+x\,a(y,z)+b(y,z),
\]
where \(L\) is homogeneous linear, \(a\) homogeneous quadratic and \(b\) homogeneous cubic. At both null values \(x=\pm\sqrt{y^2+z^2}\), for \((y,z)\ne(0,0)\), subtraction and addition give \(a(y,z)=b(y,z)=0\). Polynomial identity then makes both remainders zero. Thus the necessary condition is exactly \(P_3=QL\). Conversely every such cubic is weaker than \(Q^2\), since \(L\prec Q\), and (1) covers all smaller parts. The comparison theorem proves sufficiency. 

**(b) Two tangential cones.** Let
\[
\begin{gathered}
A=x^2-y^2,\\
Q_1=A-z^2,\quad Q_2=A-2z^2,\\
P_4=Q_1Q_2.
\end{gathered}
\]
The common nonzero null points have \(z=0,x^2=y^2\). The multiplicity result only initially requires \(P_3\) to vanish on these two lines. Restricting a homogeneous cubic to \(z=0\), its binary polynomial is divisible by both \(x-y\) and \(x+y\). Hence
\[
P_3=A L+zq(x,y,z)
\]
for a linear \(L\) and quadratic \(q\). This is the weaker multiplicity condition.

The linear-cubic products \(A L\) and \(z^2L\) are weaker than \(P_4\), because \(A=2Q_1-Q_2\) and \(z^2=Q_1-Q_2\), and each \(Q_jL\) is weaker. Write \(q=q_0(x,y)+zL'\). If \(P\) is hyperbolic, the comparison theorem gives \(P_3\prec P_4\). Subtracting the already weaker \(AL\) and \(z^2L'\) gives \(zq_0\prec P_4\).

Fix real \(x,y\) with \(x^2=y^2\), \(x\ne0\), and any real \(z\). Evaluate this comparison at \((sx,sy,z)\) and let \(s\to+\infty\). The numerator \(|zq_0(sx,sy)|\) is \(s^2|zq_0(x,y)|\). For each \(Q_j\), the undifferentiated value there is \(-jz^2\); its first derivatives grow in \(s\) only as \(2sx,-2sy\), and the second derivatives are constants. Thus \(S_{Q_j}(sx,sy,z)/s\to\sqrt{8}\,|x|\), independently of the fixed \(z\). Product comparability proves
\[
|zq_0(x,y)|\le C x^2,
\]
with one comparison constant independent of \(z\). Since \(z\) is arbitrary, \(q_0(x,y)=0\) on both lines \(x=\pm y\). A binary homogeneous quadratic vanishing there is a scalar multiple of \(A\). Absorb \(zq_0\) into \(AL\). The full necessary condition is therefore
\[
P_3=(x^2-y^2)L_1+z^2L_2.
\tag{2}
\]
Conversely these two cubic terms are weaker by the relations above; smaller degrees are covered by (1), and the comparison theorem gives hyperbolicity. The cubic \(zx^2\) meets the initial multiplicity condition but fails (2), so that weaker condition is not sufficient. 

**(c) Two transverse cones.** Let
\[
\begin{gathered}
Q_1=x^2-2y^2-z^2,\\
Q_2=x^2-y^2-2z^2,\\
P_4=Q_1Q_2.
\end{gathered}
\]
Their common null points have \(y^2=z^2,x^2=3y^2\). Divide any homogeneous cubic by \(Q_1\) in \(x\):
\[
P_3=Q_1L+x\,a(y,z)+b(y,z),
\]
with the same degrees as in (a). The multiplicity result requires vanishing at both signs \(x=\pm\sqrt 3\,|y|\), with \(z=\pm y\), \(y\ne0\). Addition/subtraction make both \(a,b\) vanish on \(y=z\) and \(y=-z\). Their binary polynomials are therefore divisible by \(y^2-z^2\). Thus
\[
P_3=Q_1L_1+(y^2-z^2)L_2.
\tag{3}
\]
Since \(y^2-z^2=Q_2-Q_1\), every such cubic is weaker than \(P_4\). Equation (1) covers all smaller terms; the comparison theorem gives sufficiency. Here the multiplicity condition already gives the full allowed cubic form, unlike the tangential example.

## Exercises with complete solutions

**Exercise 1 (intermediate).** Find a lower-order completion of \(F=x^2\) on \(\mathbb R^2\) that fails hyperbolicity in direction \(e_x\), although \(F\) is homogeneous hyperbolic.

**Solution.** Take \(P(x,y)=x^2+y\). Along \((0,y)+z e_x\), the roots are \(z=\pm i\sqrt y\) for \(y>0\). Their negative imaginary parts are unbounded, so no barrier exists. At \(v=(0, 1)\), the principal part has a double \(e_x\)-root but the first-order part \(y\) does not vanish, violating the multiplicity result. The lower term is also not weaker than \(x^2\), whose derivative norm is bounded along this ray.

**Exercise 2 (advanced).** Let \(P_4=(x^2-y^2-z^2)(x^2-y^2-2z^2)\). Compare the cubics \(zx^2\) and \(z^2x\) as possible lower parts, and decide whether an arbitrary complex quadratic may be added in each allowed case.

**Solution.** Both cubics vanish on the common null lines \(z=0,x=\pm y\), so the multiplicity condition alone cannot separate them. The second is \(z^2L_2\) with \(L_2=x\), and the tangential-cone example permits it. The first has residual \(zq_0\) with \(q_0=x^2\), which is nonzero on those lines, so the large-\(s\) comparison in the tangential-cone example forbids it. Every complex quadratic and smaller term is weaker than \(P_4\) by (1), so any of them may be added when the cubic is allowed. They cannot repair the forbidden cubic because each homogeneous component must itself be weaker by the comparison theorem.

**Exercise 3 (advanced).** A homogeneous hyperbolic \(F\) depends only on a proper subspace of \(\mathbb R^n\). Prove that any hyperbolic completion \(P\) with this principal part must be independent of every inactive direction of \(F\). Show why merely having smaller degree does not suffice for such a completion.

**Solution.** The inactive-space result gives \(A(P)=A(F)\), so every inactive directional derivative of \(P\) vanishes identically. For a concrete obstruction, take \(F(x,y)=x^2\), whose \(y\)-direction is inactive, and add \(y\). Exercise 1 proves the resulting polynomial nonhyperbolic. More generally the bounded shifted ratio in the comparison theorem is constant in an inactive principal direction in its denominator, and would grow polynomially if the numerator retained any nontrivial dependence on that direction.

**Exercise 4 (advanced).** Let \(P(x,y)=x^2-y^2+iay\), \(a\in\mathbb R\). Prove a two-sided imaginary root bound in the \(e_x\) direction and determine its sharp value.

**Solution.** For a real spatial coordinate \(y\), a time root \(z=u+iv\) satisfies \(u^2-v^2=y^2\) and \(2uv=-ay\). Therefore \(4v^2(y^2+v^2)=a^2y^2\). For \(y\ne0\), this gives \(|v|\le |a|/2\); for \(y=0\), the root is zero and the same bound holds. More explicitly,
\[
v^2=\frac{\sqrt{y^4+a^2y^2}-y^2}{2}
\longrightarrow\frac{a^2}{4}\quad(|y|\to\infty).
\]
Thus \(|a|/2\) is the sharp uniform strip width; it is zero when \(a=0\). For a general real time coordinate \(x\), roots of \(P((x,y)+z e_x)\) are real translates of these roots, so the same bound applies. The principal value at \(e_x\) is one, and any barrier below \(-|a|/2\) proves hyperbolicity. This concrete complex lower-order completion illustrates the positive-order strict theorem, whose Lorentz principal part has a nonzero gradient away from zero.

## References

The strength comparisons used here are proved in [Rescaled symbols and stable strength](rescaled-symbols-and-stable-strength.md). The projection, convergent Puiseux and compact selection lemmas are proved in [Symbols at infinity](symbols-at-infinity.md), Lemmas 2.1 and 3.1 and Corollary 3.3. The uniform shifted derivative estimate uses [Hypoellipticity and complex zeros](hypoellipticity-and-complex-zeros.md), Lemma 1.1. The two additional analytic entries are stated with their precise hypotheses at the start of the first lesson.
