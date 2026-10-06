# Tensor completion, injectivity and state domination

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text: public domain (CC0).* 

The [symmetric tensor norm](symmetric-tensor-norms-and-rademacher-truncation.md) already gives small projective lifts of self-adjoint tensors. To control every bounded bilinear form, those lifts must be unique. A normalized-functional argument rules out the kernel, and a compact convex separation argument then produces fixed states dominating the form.

Besides that preceding lesson, we use Hahn–Banach, Banach–Alaoglu, elementary Bochner integration and C*-algebra state/functional-calculus facts. The numerical-range step is proved here, rather than treating a Banach algebra as a C*-algebra. All algebras may be nonseparable.

## 1. Normalized bilinear forms

Suppose initially that \(A,B\) are unital and \(V:A\times B\to\mathbb C\) is bilinear, with \(\|V\|=V(1,1)=1\). Its marginals \(\varphi(x)=V(x,1)\), \(\psi(y)=V(1,y)\) are states. Indeed, a functional \(f\) on a unital C*-algebra with \(\|f\|=f(1)=1\) is positive: expanding \(f(e^{ith})\) for self-adjoint \(h\), the bound \(|f(e^{ith})|\le1\) for both signs of \(t\) makes \(f(h)\) real. If \(0\le h\le1\), then \(|1-f(h)|\le\|1-h\|\le1\), so \(f(h)\ge0\). Scaling gives positivity on the whole cone.

**Lemma 1.1.** For self-adjoint \(a,b\),
\[
|\operatorname{Re}V(a,b)|\le\varphi(a^2)^{1/2}\psi(b^2)^{1/2}.
\tag{1}
\]

**Proof.** Taylor expansion in norm gives
\[
\operatorname{Re}V(e^{ita},e^{itb})
=1-t^2\big[\tfrac12\varphi(a^2)+\tfrac12\psi(b^2)
+\operatorname{Re}V(a,b)\big]+O(|t|^3).
\tag{2}
\]
The left side is at most \(1\), so the bracket is nonnegative. Replace \(a\) by \(-a\) to get \(|\operatorname{Re}V(a,b)|\le[\varphi(a^2)+\psi(b^2)]/2\). Replace \(a,b\) by \(t a,t^{-1}b\) and minimize over \(t>0\). If either quadratic value is zero, take the corresponding limit; otherwise the minimizing bound is their geometric mean. \(\square\)

Write \(V^*(x,y)=\overline{V(x^*,y^*)}\). If also \(V=V^*\), its values on self-adjoint pairs are real. For arbitrary \(x=a+ic,y=b+id\), rotate \(x\) by a scalar phase so that \(V(x,y)\) is real. Then
\[
|V(x,y)|=|V(a,b)-V(c,d)|
\le\varphi(a^2+c^2)^{1/2}\psi(b^2+d^2)^{1/2}
=\varphi(q(x))^{1/2}\psi(q(y))^{1/2}.
\tag{3}
\]
The phase does not change \(q(x)\). Summing (3) and applying scalar Cauchy–Schwarz proves that this normalized self-adjoint functional on \(A\widehat\otimes_\pi B\) is \(\sigma\)-continuous, with dual norm at most \(1\).

## 2. A Banach algebra kernel test

For a unital complex Banach algebra \(C\), assume \(\|1\|=1\). Its normalized functionals are
\[
\mathcal S_C=\{F\in C^*: \|F\|=F(1)=1\}.
\]
They need not be positive on any involution. Call \(h\) numerical-real if every \(F\in\mathcal S_C\) takes a real value at \(h\).

**Lemma 2.1.** If \(h\) and \(ih^2\) are numerical-real, then \(h=0\).

**Proof.** We first show that a numerical-real \(k\) satisfies \(\|e^{itk}\|=1\) for every real \(t\). For any \(a\in C\),
\[
\lim_{s\downarrow0}\frac{\|1+sa\|-1}{s}
=\sup_{F\in\mathcal S_C}\operatorname{Re}F(a).
\tag{4}
\]
The lower bound follows by evaluating at each normalized functional. For the upper bound choose a norm-one functional \(F_s\) norming \(1+sa\), with its value real and positive. Any weak-* cluster point as \(s\downarrow0\) has value \(1\) at the identity, because \(F_s(1+sa)=\|1+sa\|\to1\). Also
\((\|1+sa\|-1)/s\le\operatorname{Re}F_s(a)\). Compactness yields the asserted upper bound, proving (4).

Apply (4) to \(a=\pm ik\). Its right side is zero. The exponential limit \((1+itk/n)^n\to e^{itk}\) then gives \(\|e^{itk}\|\le1\). Applying this to \(-t\) and multiplying the inverse elements gives equality. Left multiplication by \(e^{itk}\) is an isometry, since both it and its inverse are contractions.

For \(t>0\) put \(g_t(s)=(4\pi t)^{-1/2}e^{-s^2/(4t)}\). Norm-convergent Gaussian integration of the exponential series gives
\[
e^{-th^2}=\int_{\mathbb R}g_t(s)e^{ish}\,ds.
\tag{5}
\]
Termwise integration is justified by the integrable bound \(g_t(s)e^{|s|\|h\|}\); its even moments give the exponential on the left. Integration by parts, with vanishing boundary terms, gives
\[
h e^{-th^2}=i\int_{\mathbb R}g_t'(s)e^{ish}\,ds,
\qquad \|h e^{-th^2}\|\le\int|g_t'|=\frac1{\sqrt{\pi t}}.
\tag{6}
\]
Numerical-reality of \(ih^2\) makes \(e^{\pm th^2}\) contractions by the preceding argument. Multiplication by \(e^{-th^2}\) is therefore an isometry. Thus (6) bounds \(\|h\|\) by \(1/\sqrt{\pi t}\) for every \(t>0\), forcing \(h=0\). \(\square\)

## 3. Injectivity of the canonical map

**Theorem 3.1.** For any C*-algebras \(A,B\), the canonical map
\[
I:A\widehat\otimes_\pi B\longrightarrow A\widehat\otimes_\sigma B
\tag{7}
\]
is injective.

**Proof.** First assume both algebras unital, and put \(C=A\widehat\otimes_\pi B\). This is a unital Banach algebra with isometric involution and \(\|1\otimes1\|_\pi=1\). The product estimate in the preceding lesson makes (7) an algebra homomorphism, so its kernel \(K\) is a closed, involution-invariant ideal.

For \(F\in\mathcal S_C\), the functional \(G=(F+F^*)/2\) is self-adjoint, has value \(1\) at the identity and norm \(1\). Section 1 makes it \(\sigma\)-continuous. Hence \(G\) vanishes on \(K\). If \(v=v^*\in K\), this says \(\operatorname{Re}F(v)=0\) for every normalized \(F\). Consequently \(h=iv\) is numerical-real. Since \(v^2\in K\) is self-adjoint, \(ih^2=-iv^2\) is also numerical-real. Lemma 2.1 gives \(v=0\). For general \(u\in K\), apply this to \(u+u^*\) and \(i(u-u^*)\); both are self-adjoint elements of \(K\). Thus \(u=0\).

For nonunital algebras, use forced C*-unitizations \(\widetilde A,\widetilde B\). The coefficient projection \(P_A(a+\lambda1)=a\) is bounded by \(2\), because the quotient character bounds \(|\lambda|\) by \(\|a+\lambda1\|\); similarly for \(P_B\). Their projective tensor product is a bounded left inverse to the projective inclusion. That inclusion is therefore injective. The algebraic inclusion is \(\sigma\)-contractive, since all square-sum norms are preserved. The commuting square of the two canonical maps shows that an element in the kernel of (7) maps to the kernel for the unitizations. The unital result and projective injectivity of the inclusion make it zero. \(\square\)

## 4. The real norm comparison

The real projective space embeds in the complex projective space. To see this without assuming a tensor-inclusion theorem, expand any complex decomposition of a self-adjoint tensor as in (6) of the [preceding lesson](symmetric-tensor-norms-and-rademacher-truncation.md#proposition-1-1). It costs at most twice the original projective cost, since
\(\|\operatorname{Re}x\|^2+\|\operatorname{Im}x\|^2\le2\|x\|^2\). Thus
\[
\|u\|_\pi\le\|u\|_{\pi_{\mathbb R}}\le2\|u\|_\pi
\tag{8}
\]
on the algebraic real tensor space, and the inclusion of its completion is injective. Its image is the self-adjoint part of the complex completion: symmetrized algebraic approximants are Cauchy by (8).

**Theorem 4.1.** On the completed real self-adjoint tensor space,
\[
\|u\|_\sigma\le\|u\|_{\pi_{\mathbb R}}
\le\frac{81}{16}\|u\|_\sigma.
\tag{9}
\]
Every bounded real bilinear form \(W\) on \(A_{\rm sa}\times B_{\rm sa}\) therefore has \(\sigma\)-dual norm at most \((81/16)\|W\|\).

**Proof.** The first inequality was already established. Surjectivity and approximate lifting bounds come from the preceding lesson. By Theorem 3.1 and (8), the real lift is unique. Bounds \(\|u\|_{\pi_{\mathbb R}}\le(81/16)\|u\|_\sigma+\varepsilon\) for every \(\varepsilon>0\) now apply to that same lift. Taking the infimum over \(\varepsilon\) proves (9). The dual assertion follows by evaluating \(W\) on algebraic tensors and using (9). \(\square\)

## 5. Fixed states from compact affine inequalities

We record the separation argument explicitly. Suppose \(Q\) is compact and convex and \(\mathcal F\) is a family of continuous real affine functions. If every finite nonnegative combination of functions in \(\mathcal F\) has nonnegative maximum on \(Q\), there exists \(q\in Q\) with \(F(q)\ge0\) for every \(F\in\mathcal F\). Indeed, for finitely many \(F_1,\ldots,F_m\), their image of \(Q\) is compact convex. If it misses the positive orthant, finite-dimensional separation gives nonnegative coefficients \(\lambda_i\), not all zero, with \(\sup_Q\sum\lambda_iF_i<0\), a contradiction. The corresponding closed subsets of \(Q\) have the finite intersection property; compactness completes the argument. This works without metrizability or a countable list of tests.

**Lemma 5.1.** For a real \(\sigma\)-continuous bilinear form \(W\) on self-adjoint pairs in unital \(A,B\), there are states \(\varphi,\psi\) with
\[
|W(a,b)|\le c\varphi(a^2)^{1/2}\psi(b^2)^{1/2},
\qquad c=\|W\|_{\sigma^*}.
\tag{10}
\]

**Proof.** For \(c=0\) the form is zero and arbitrary states suffice. Otherwise take \(Q=S(A)\times S(B)\) and the functions
\[
F_{a,b}(\varphi,\psi)=\tfrac c2[\varphi(a^2)+\psi(b^2)]-W(a,b).
\tag{11}
\]
A finite nonnegative combination is obtained by replacing its pairs by \((\sqrt{\lambda_j}a_j,\sqrt{\lambda_j}b_j)\). Choose states separately norming the two positive square sums. At this pair the value of the combined function is at least
\[
\tfrac c2(S_A+S_B)-c\sqrt{S_A S_B}\ge0,
\quad S_A=\|\sum a_j^2\|,\ S_B=\|\sum b_j^2\|,
\]
using the defining tensor bound. The compact affine argument gives one pair satisfying every (11). Changing the sign of \(a\) yields an absolute-value additive bound. Rescaling \((a,b)\) to \((t a,t^{-1}b)\) and minimizing yields (10), including zero quadratic values by limits. \(\square\)

## 6. An initial complex domination bound

**Theorem 6.1.** For unital C*-algebras and any bounded complex bilinear form \(V\), there are states \(\varphi,\psi\) such that
\[
|V(x,y)|\le\frac{81}{16}\|V\|
\varphi(x^*x+xx^*)^{1/2}\psi(y^*y+yy^*)^{1/2}.
\tag{12}
\]

**Proof.** Put \(V_1=(V+V^*)/2\), \(V_2=(V-V^*)/(2i)\). Each is self-adjoint and has norm at most \(\|V\|\). Its real restriction is \(\sigma\)-continuous by Theorem 4.1. Lemma 5.1 gives states \(\varphi_i,\psi_i\) with constant \(K\|V\|\), where \(K=81/16\). Expanding \(x=a+ic,y=b+id\) and taking real parts gives the same two-term estimate as (3). Rotating \(x\) then gives
\[
|V_i(x,y)|\le K\|V\|\varphi_i(q(x))^{1/2}\psi_i(q(y))^{1/2}.
\]
Sum the bounds for \(V_1,V_2\), apply Cauchy–Schwarz to this two-term sum, and set \(\varphi=(\varphi_1+\varphi_2)/2\), \(\psi=(\psi_1+\psi_2)/2\). The result is \(2K\|V\|\sqrt{\varphi(q(x))\psi(q(y))}\), which equals the right side of (12). \(\square\)

This finite universal constant is the input to the [sharp inequality](sharp-noncommutative-bilinear-inequality.md). Its existence, rather than its preliminary numerical size, is what the improvement argument needs.

## 7. Exercises with complete solutions

**Exercise 1.** Determine the sign of the second-order bracket in (2).

*Solution.* Subtract \(1\), divide by \(t^2>0\) and let \(t\to0\). Since the left side before subtraction is at most \(1\), the negative of the bracket is at most zero. The bracket is therefore nonnegative. Replacing \(a\) by \(-a\) then bounds both signs of \(\operatorname{Re}V(a,b)\).

**Exercise 2.** Minimize \((t^2\alpha+t^{-2}\beta)/2\), including the cases \(\alpha\beta=0\).

*Solution.* For positive \(\alpha,\beta\), equality in arithmetic–geometric mean occurs at \(t^4=\beta/\alpha\), giving \(\sqrt{\alpha\beta}\). If \(\alpha=0\), let \(t\to\infty\); if \(\beta=0\), let \(t\downarrow0\). If both vanish every bound is zero.

**Exercise 3.** Why is \((F+F^*)/2\) normalized when \(F\in\mathcal S_C\)?

*Solution.* Isometry of the involution gives \(\|F^*\|=\|F\|=1\), so the average has norm at most one. Its value at the identity is \((1+\overline1)/2=1\), and \(\|1\|=1\), so its norm is at least one. It is self-adjoint by construction.

**Exercise 4.** Explain the compactness step in (4) when \(C\) is nonseparable.

*Solution.* Banach–Alaoglu makes the unit dual ball weak-* compact. A net of norming functionals has a convergent subnet; a sequence need not have a convergent subsequence. The limiting functional has value one at \(1\), hence is normalized. The limsup estimate follows along a subnet realizing the directional limsup. No countable compactness assertion is used.

**Exercise 5.** Compute \(\int|g_t'|\) in (6).

*Solution.* Since \(g_t'(s)=-s g_t(s)/(2t)\), symmetry gives \(\int|g_t'|=(1/t)\int_0^\infty s(4\pi t)^{-1/2}e^{-s^2/(4t)}ds\). The integral of \(s e^{-s^2/(4t)}\) is \(2t\), so the result is \(1/\sqrt{\pi t}\).

**Exercise 6.** Why are both numerical-reality hypotheses needed in the Gaussian proof?

*Solution.* Numerical-reality of \(h\) bounds \(e^{ish}\), allowing the derivative integral estimate. Numerical-reality of \(ih^2\) bounds both \(e^{-th^2}\) and its inverse, so multiplication by the former preserves \(\|h\|\). Without that inverse bound, (6) only controls a damped element and does not force \(h=0\); a nonzero self-adjoint matrix supplies such a damped example.

**Exercise 7.** Prove the factor \(2\) upper bound in (8).

*Solution.* Symmetrizing \(\sum x_j\otimes y_j\) gives \(\sum(a_j\otimes b_j-c_j\otimes d_j)\). Its real projective cost is at most \(\sum(\|a_j\|\|b_j\|+\|c_j\|\|d_j\|)\). Termwise Cauchy–Schwarz bounds each summand by \(\sqrt{\|a_j\|^2+\|c_j\|^2}\sqrt{\|b_j\|^2+\|d_j\|^2}\le2\|x_j\|\|y_j\|\). Take the projective infimum.

**Exercise 8.** Why does approximate lifting become an exact norm bound after injectivity?

*Solution.* For every positive tolerance there is a lift with the stated approximate bound. Injectivity says all these lifts are the same element. Its fixed norm is therefore below the exact bound plus every positive tolerance, and hence below the exact bound. No compactness of a projective ball or attainment of a tensor decomposition is required.

**Exercise 9.** Explain the nonnegative coefficients in the compact affine separation argument.

*Solution.* A functional separating a compact set from the positive orthant must be nonnegative on that orthant. If one of its coordinate coefficients were negative, its values on the corresponding positive coordinate ray would tend to minus infinity, contradicting a lower bound on the orthant. The orthant contains zero, so strict separation gives a strictly negative maximum on the compact set after this orientation.

**Exercise 10.** Check that passing from two self-adjoint forms to (12) does not lose another factor of two.

*Solution.* The sum of the two bounds is at most \(K\|V\|\sqrt{(\varphi_1+\varphi_2)(q(x))}\sqrt{(\psi_1+\psi_2)(q(y))}=2K\|V\|\sqrt{\varphi(q(x))\psi(q(y))}\). Each \(q\) is half the unsymmetrized sum, so their product of square roots contributes \(1/2\). The coefficient in (12) is therefore \(K\), not \(2K\).

## 8. An elementary Gaussian proof

This is an additional proof of Lemma 2.1. Scalar compactness on the at-most-two-dimensional space \(\operatorname{span}\{1,a\}\) gives the directional norm derivative. The argument in Section 2 and Exercise 4 retain their Banach–Alaoglu route.

The real and complex norming-functional method is compared with Jacob Shapiro, [*Functional Analysis, Princeton University MAT520 Lecture Notes*, last typeset 10 December 2025](https://web.math.princeton.edu/~shapiro/PDFs/teaching/MAT520_fall_2025/MAT520_Lecture_Notes.pdf#page=36), Theorems 4.4–4.5, printed/PDF pp.36–37. Both extension signs and the chain-union details are given below. The source is not claimed to contain the Gaussian lemma.

The underlying foundations are ZFC (including Zorn’s lemma), real and complex scalar completeness, elementary linear algebra, elementary real differentiation and Riemann integration, and the definition of a Banach algebra. The needed consequences are proved explicitly.

The programme interface for norm-preserving real and complex extension and scalar norm detection is *Banach estimates, quotient spaces and compact parameter arguments*, AN03-P004 / AN03-BFD-005. Section 8.1 retains an independently written alternative to that interface. Its full argument is given here; the directional derivative, exponential and Gaussian arguments in Sections 8.2–8.6 are the present application.

### 8.1. The precise norming-functional input

Let \(E\) be a real normed vector space, let \(D\subset E\) be a linear subspace, let \(f:D\to\mathbb R\) be linear, and let \(L\ge0\) satisfy \(|f(y)|\le L\|y\|\) on \(D\). If \(L=0\), the zero functional is an extension. Otherwise divide \(f\) by \(L\), so that \(L=1\). For \(z\notin D\), a real number \(c\) can be chosen between

\[
\sup_{y\in D}\{f(y)-\|y-z\|\}
\quad\hbox{and}\quad
\inf_{y\in D}\{\|y+z\|-f(y)\}.
\tag{A1}
\]

Indeed for \(y,w\in D\),

\[
f(y)+f(w)=f(y+w)\le\|y+w\|
\le\|y-z\|+\|w+z\|.
\]

Every member of the set in the supremum is therefore at most every member of the set in the infimum. Taking \(y=w=0\) in the comparison also supplies finite upper and lower bounds. Real completeness supplies \(c\). Define

\[
f_1(y+a z)=f(y)+a c,\qquad a\in\mathbb R.
\]

The representation is unique because \(z\notin D\), so \(f_1\) is linear. If \(a>0\), the upper inequality in (A1), applied to \(y/a\), gives \(f_1(y+a z)\le\|y+a z\|\). If \(a<0\), put \(b=-a>0\) and apply the lower inequality in (A1) to \(y/b\); it gives \(f(y)-b c\le\|y-b z\|\). The case \(a=0\) is the old bound. Applying the same upper bound to the negative vector gives \(|f_1(x)|\le\|x\|\). Thus extension by one real dimension preserves the bound.

Partially order all such extensions by extension of both domain and functional. In a chain, the union of the domains is a vector subspace: any two vectors lie together in one of the comparable domains. The union functional is unambiguous and linear for the same reason, extends \(f\), and obeys the same bound at each vector. Thus every chain has an upper bound. Zorn's lemma gives a maximal extension; if its domain were not \(E\), the one-dimensional construction would enlarge it. The domain is therefore \(E\). Rescaling gives the assertion for any \(L\).

For a complex normed space \(E\), let \(D\subset E\) be a complex linear subspace and let \(f:D\to\mathbb C\) be complex linear with \(|f(y)|\le L\|y\|\), \(L\ge0\). Apply the real assertion to \(u=\operatorname{Re}f\) on the underlying real space and obtain a real-linear \(U\) with \(|U(x)|\le L\|x\|\). Set

\[
F(x)=U(x)-iU(ix).
\tag{A2}
\]

Then \(F(ix)=iF(x)\), so \(F\) is complex linear. On the original complex subspace, \(u(ix)=-\operatorname{Im}f(x)\), hence \(F=f\). If \(F(x)\ne0\), choose \(|\lambda|=1\) with \(\lambda F(x)=|F(x)|\). It follows that

\[
|F(x)|=\operatorname{Re}F(\lambda x)=U(\lambda x)
\le L\|\lambda x\|=L\|x\|.
\]

For \(F(x)=0\) the inequality is immediate. This proves exactly the complex Hahn-Banach input used below. In particular, for \(x\ne0\), extend the functional \(\alpha x\mapsto\alpha\|x\|\) on \(\mathbb Cx\). The extension has norm one and takes the real positive value \(\|x\|\) at \(x\).

### 8.2. Directional norm derivative using only two-dimensional compactness

Let \(C\) be a unital complex Banach algebra with \(\|1\|=1\), and define

\[
\mathcal S_C=\{F\in C^*: \|F\|=F(1)=1\}.
\]

The norming-functional assertion at \(1\) makes this set nonempty. For \(a\in C\), set

\[
D_s=\frac{\|1+s a\|-1}{s},\qquad s>0.
\]

The map \(s\mapsto\|1+s a\|\) is convex, so \(D_s\le D_t\) for \(0<s<t\). Also \(|D_s|\le\|a\|\). Thus \(D=\lim_{s\downarrow0}D_s\) exists and is finite. Evaluating a member of \(\mathcal S_C\) gives

\[
D_s\ge\operatorname{Re}F(a),
\quad\hbox{so}\quad
D\ge\sup_{F\in\mathcal S_C}\operatorname{Re}F(a).
\tag{B1}
\]

Choose \(s_j\downarrow0\), small enough that \(1+s_j a\ne0\), and a norm-one \(F_j\in C^*\) with \(F_j(1+s_j a)=\|1+s_j a\|\). This is the norming consequence proved in Section 8.1. Restrict these functionals to \(E=\operatorname{span}_{\mathbb C}\{1,a\}\). Their values at a fixed basis of \(E\) are bounded, because \(|F_j(x)|\le\|x\|\). A subsequence converges coordinatewise: repeatedly bisect a bounded interval containing each of their finitely many real and imaginary coordinates, retain a subinterval containing infinitely many indices, and then take a diagonal increasing subsequence. The nested lengths tend to zero, so real completeness gives convergence in every coordinate. This is the only compactness argument needed.

The limiting functional \(f:E\to\mathbb C\) is linear and satisfies \(|f(x)|\le\|x\|\) for every fixed \(x\in E\). Moreover,

\[
F_j(1)=\|1+s_j a\|-s_j F_j(a)\longrightarrow1,
\]

so \(f(1)=1\). Apply Section 8.1 to extend \(f\) to \(F\in C^*\) with norm at most one; its value at \(1\) forces its norm to be exactly one. Hence \(F\in\mathcal S_C\). Finally,

\[
D_{s_j}
=\frac{\operatorname{Re}F_j(1)-1}{s_j}
 +\operatorname{Re}F_j(a)
\le\operatorname{Re}F_j(a).
\]

Passing along the coordinate-convergent subsequence gives \(D\le\operatorname{Re}F(a)\). Together with (B1), this proves

\[
\lim_{s\downarrow0}\frac{\|1+s a\|-1}{s}
=\sup_{F\in\mathcal S_C}\operatorname{Re}F(a).
\tag{B2}
\]

This proof applies even when \(C\) is nonseparable. It uses finite-dimensional scalar subsequence compactness and Hahn-Banach, without the weak-* compactness of the full dual ball.

### 8.3. Numerical reality gives an isometric exponential group

Call \(k\in C\) numerical-real if \(F(k)\in\mathbb R\) for all \(F\in\mathcal S_C\). Formula (B2), applied to \(a=\pm ik\), gives

\[
\|1+s(\pm ik)\|=1+o(s),\qquad s\downarrow0.
\tag{C1}
\]

The exponential \(e^a=\sum_{m\ge0}a^m/m!\) converges in norm, since \(\|a^m\|\le\|a\|^m\) and the scalar exponential series converges. Also

\[
(1+a/n)^n\longrightarrow e^a.
\tag{C2}
\]

To see this directly, the coefficient of \(a^m\), for \(m\le n\), is \(\binom nm/n^m\), which tends to \(1/m!\) and is at most \(1/m!\). The norm of the tail above any fixed \(m_0\), uniformly in \(n\), is bounded by \(\sum_{m>m_0}\|a\|^m/m!\), which tends to zero. The finite initial segment converges coefficientwise.

Fix \(t\in\mathbb R\). With \(a=itk\), (C1) and submultiplicativity give

\[
\|e^{itk}\|
\le\limsup_n\|1+itk/n\|^n=1.
\]

For the last equality, writing the base as \(1+o(1/n)\) and using \(\log(1+v)=v+o(v)\) gives a logarithm tending to zero. Absolute convergence of the exponential series permits their Cauchy product; the binomial identity then gives \(e^{itk}e^{-itk}=1\). Both factors are contractions and \(\|1\|=1\), so both have norm one. For every \(x\in C\),

\[
\|x\|=\|e^{-itk}(e^{itk}x)\|\le\|e^{itk}x\|\le\|x\|,
\]

and therefore left multiplication by \(e^{itk}\) is an isometry. The analogous right assertion follows by the same calculation.

### 8.4. The scalar Gaussian facts and the vector integral

The scalar improper integral \(I=\int_{\mathbb R}e^{-u^2}\,du\) exists: outside \([-1,1]\), \(e^{-u^2}\le e^{-|u|}\). Its normalization can be checked using only compact Riemann integrals. If \(I_R=\int_{-R}^R e^{-u^2}\,du\), the double Riemann integral over the square equals \(I_R^2\), by rectangular product sums. That square contains the disk of radius \(R\) and lies inside the disk of radius \(\sqrt2 R\). For a continuous radial function on a disk, upper and lower sums on concentric annuli, whose areas are \(\pi(r_j^2-r_{j-1}^2)\), give the radial integral \(\int_0^R2\pi r f(r)\,dr\). Uniform continuity makes the difference of the two sums tend to zero. Applying this to \(f(r)=e^{-r^2}\) gives

\[
\pi(1-e^{-R^2})\le I_R^2\le\pi(1-e^{-2R^2}).
\]

Hence \(I^2=\pi\), and positivity gives \(I=\sqrt\pi\). Scalar substitution now shows that for \(t>0\),

\[
g_t(s)=(4\pi t)^{-1/2}e^{-s^2/(4t)}
\quad\hbox{satisfies}\quad
\int_{\mathbb R}g_t(s)\,ds=1.
\tag{D1}
\]

For a norm-continuous Banach-space-valued function on a compact interval, Riemann sums converge in norm. Uniform continuity bounds the difference between a sum and any refinement by interval length times the modulus of continuity at the mesh. Comparing two sums through a common refinement makes the sums Cauchy, and Banach completeness gives their limit. The triangle inequality on sums yields

\[
\left\|\int_a^b v(s)\,ds\right\|\le\int_a^b\|v(s)\|\,ds.
\tag{D2}
\]

If a continuous scalar integrable envelope \(b(s)\ge\|v(s)\|\) has vanishing tails on \(\mathbb R\), (D2) makes the integrals over \([-R,R]\) Cauchy as \(R\to\infty\). Their limit is the improper norm integral, and (D2) holds on the line. Bounded linear maps, including multiplication by a fixed algebra element, commute with these integrals by passage from Riemann sums. For continuously differentiable vector functions the fundamental theorem follows from telescoping increments and the modulus of continuity of the derivative; the product rule then gives integration by parts on compact intervals. Thus the only vector integration facts used here have been constructed directly.

### 8.5. The heat identity, with all exchanges justified

Let \(h\in C\). The series for \(e^{ish}\) converges uniformly on every compact \(s\)-interval, so it may be integrated there termwise. For the full-line integral, its absolute series has scalar envelope

\[
g_t(s)\sum_{m\ge0}\frac{|s|^m\|h\|^m}{m!}
=g_t(s)e^{|s|\|h\|}.
\]

This is integrable, since with \(A=\|h\|\),

\[
-s^2/(4t)+A|s|\le -s^2/(8t)+2t A^2.
\]

Fix a large compact interval; uniform convergence gives termwise integration there. Outside the interval, the same integrable envelope controls every partial sum and the full sum. Its tail tends to zero. These two observations justify interchange of the series and the improper norm integral, without appealing to an unproved general Bochner dominated-convergence theorem.

Odd Gaussian moments vanish by symmetry. Integration by parts for the even moments uses \(g_t'=-s g_t/(2t)\); polynomial times \(g_t\) tends to zero at both endpoints. For \(m\ge1\),

\[
\int s^{2m}g_t(s)\,ds
=2t(2m-1)\int s^{2m-2}g_t(s)\,ds
=\frac{(2m)!}{m!}t^m.
\tag{E1}
\]

The last equality follows inductively from (D1). Consequently,

\[
\int_{\mathbb R}g_t(s)e^{ish}\,ds
=\sum_{m\ge0}\frac{(-1)^m h^{2m}}{(2m)!}
   \frac{(2m)!}{m!}t^m
=e^{-t h^2}.
\tag{E2}
\]

### 8.6. Derivative estimate and the kernel conclusion

Now assume \(h\) and \(ih^2\) are numerical-real. Section 8.3 gives \(\|e^{ish}\|=1\). Uniform differentiation of the exponential series on compact intervals gives \((e^{ish})'=ih e^{ish}\). Integration by parts on \([-R,R]\), and then passage to the limit, gives

\[
\int_{\mathbb R}g_t'(s)e^{ish}\,ds
=-ih\int_{\mathbb R}g_t(s)e^{ish}\,ds.
\]

The endpoint terms vanish because \(g_t(\pm R)\to0\) and \(\|e^{\pm iRh}\|=1\); both integrals have scalar integrable envelopes. Thus (E2) yields

\[
h e^{-t h^2}=i\int_{\mathbb R}g_t'(s)e^{ish}\,ds,
\qquad
\|h e^{-t h^2}\|\le\int_{\mathbb R}|g_t'(s)|\,ds.
\tag{F1}
\]

The Gaussian is even and decreasing on the positive half-line, so scalar integration gives

\[
\int_{\mathbb R}|g_t'|=2g_t(0)=\frac1{\sqrt{\pi t}}.
\tag{F2}
\]

Numerical reality of \(ih^2\) and Section 8.3 make both \(e^{t h^2}\) and \(e^{-t h^2}\) contractions: these are \(e^{ir(ih^2)}\) for the two real values \(r=-t,t\). Hence right multiplication by \(e^{-t h^2}\) is an isometry. Equations (F1)-(F2) give

\[
\|h\|=\|h e^{-t h^2}\|\le\frac1{\sqrt{\pi t}}
\qquad(t>0).
\]

Letting \(t\to\infty\) gives \(h=0\), as required. Both numerical-reality hypotheses are used, and the sign in (F1) is \(+i\int g_t'e^{ish}\).

## 9. Weak-star compactness for arbitrary normed spaces

This supplies the general Banach–Alaoglu input of Section 2 and Exercise 4. The closed unit dual ball is compact in the weak-star topology for every real or complex normed space; separability and completeness of the original space are unnecessary. The foundation boundary is ZFC, including Zorn’s lemma, scalar completeness and topology, and the definitions of a norm, a product topology and a weak-star topology. The needed arbitrary product step is proved here.

The product embedding and closed-linearity method are compared with Jacob Shapiro, [*Functional Analysis, Princeton University MAT520 Lecture Notes*, last typeset 10 December 2025](https://web.math.princeton.edu/~shapiro/PDFs/teaching/MAT520_fall_2025/MAT520_Lecture_Notes.pdf#page=44), Theorem 5.18, printed/PDF pp.44–45. A bounded linear function has norm at most one in that proof, correcting its norm-equals-one sentence. The disk-product construction and the explicit subnet below are independently written.

The programme interfaces for arbitrary compact products, real and complex dual-ball compactness, and a convergent compact-net subnet are *Weak compactness and second adjoints*, OA-MOD-AB-04 and OA-MOD-AB-05, in the OA-MOD course. Sections 9.1–9.5 retain independently written alternatives to those interfaces; Section 9.2 supplies the scalar-disk construction used here, and Section 9.6 applies the resulting compactness to the Gaussian argument. These references identify the programme interfaces; every proof used by this local route is supplied below.

### 9.1. Proper filters and maximal extensions

A proper filter on a nonempty set \(S\) is a family of subsets containing \(S\), excluding the empty set, closed under finite intersections and upward inclusion. A family with the finite intersection property generates a proper filter by taking all supersets of its finite intersections. Order proper filters extending a fixed proper filter by inclusion. For a nonempty chain of proper filters extending the fixed filter, their union again contains the fixed filter and excludes the empty set. Any finite list of members of the union lies in a single filter of the chain: choose a filter containing each member and use the total ordering by inclusion to take the largest of the finitely many selected filters. Their intersection therefore belongs to the union and is nonempty. Upward closure also passes to the union. The fixed filter itself is an upper bound for the empty chain. Thus every chain has an upper bound in the ordered family, and Zorn's lemma gives a maximal proper extension. The maximal extension is denoted \(\mathcal U\).

For any \(A\subset S\), either \(A\in\mathcal U\) or \(S\setminus A\in\mathcal U\). Indeed, if adjoining \(A\) produced a proper filter, maximality would put \(A\) in \(\mathcal U\). Otherwise some \(F\in\mathcal U\) has \(F\cap A=\varnothing\), so \(F\subset S\setminus A\), and upward inclusion puts the complement in \(\mathcal U\). Such a maximal filter is an ultrafilter. If finitely many subsets cover a member of \(\mathcal U\), one of them is in \(\mathcal U\): otherwise all their complements would be in it, contradicting the nonempty-intersection requirement.

### 9.2. Every ultrafilter on a closed scalar disk converges

Let \(D_r=\{z\in\mathbb C:|z|\le r\}\), where \(r\ge0\), and let \(\mathcal U\) be an ultrafilter on \(D_r\). For \(r=0\), the disk is a singleton. For \(r>0\), begin with the closed square \([-r,r]^2\) and divide both coordinate intervals into halves. Its four closed subsquares cover the disk, so the preceding finite-cover argument selects a subsquare \(Q_1\) for which \(D_r\cap Q_1\in\mathcal U\). Continue within that square. This gives nested closed squares \(Q_n\), with \(D_r\cap Q_n\in\mathcal U\), and diameters tending to zero.

Write either coordinate interval of \(Q_n\) as \([a_n,b_n]\). The left endpoints increase, the right endpoints decrease, and \(b_n-a_n\to0\). By real completeness, \(c=\sup_n a_n\) exists. Nestedness gives \(a_n\le c\le b_n\) for every \(n\); the vanishing lengths make \(c\) the only point in every interval. Applying this to both coordinates gives a unique point \(z\) in every square. The proper-filter condition makes every \(D_r\cap Q_n\) nonempty. Choose \(w_n\) there; then \(|w_n-z|\le\operatorname{diam}(Q_n)\to0\), so the reverse triangle inequality gives \(|z|\le r\). Every disk neighborhood of \(z\) contains \(D_r\cap Q_n\) for all sufficiently large \(n\), hence belongs to the ultrafilter. This proves convergence. In the real case there is only one coordinate interval.

### 9.3. Arbitrary products of these disks are compact

Let \(P=\prod_{i\in I}D_{r_i}\), with its product topology; the point whose every coordinate is zero shows \(P\ne\varnothing\). If \(\mathcal U\) is an ultrafilter on \(P\), its image under a coordinate projection is an ultrafilter on the corresponding disk: a subset belongs to that image filter precisely when its inverse image belongs to \(\mathcal U\). The filter and complement rules pass through inverse images. Each image ultrafilter converges to a coordinate \(z_i\). These coordinates define \(z\in P\).

A basic neighborhood of \(z\) restricts only finitely many coordinates. Each inverse image of a restricted-coordinate neighborhood belongs to \(\mathcal U\); their finite intersection does as well. Every neighborhood contains such a basic neighborhood, so \(\mathcal U\) converges to \(z\).

Now suppose an open cover of \(P\) had no finite subcover. The complements of its members would have the finite intersection property. Extend their generated proper filter to an ultrafilter and let it converge to \(z\). A cover member containing \(z\) is a neighborhood and therefore belongs to the ultrafilter. Its complement belongs to it by construction, a contradiction. Thus every open cover has a finite subcover. This proves the precise arbitrary-product compactness needed here.

### 9.4. The dual ball is a closed subspace of the product

Let \(X\) be a complex normed space and set

\[
P_X=\prod_{x\in X}\{z\in\mathbb C:|z|\le\|x\|\}.
\]

An element \(b\in P_X\) is a scalar-valued function on \(X\) with \(|b(x)|\le\|x\|\). For each \(x,y\in X\) and \(\lambda\in\mathbb C\), the function

\[
b\longmapsto b(x+\lambda y)-b(x)-\lambda b(y)
\]

is continuous, since coordinate evaluations and finite scalar linear combinations are continuous. Its zero set is closed. Intersect all these zero sets. The intersection consists exactly of complex-linear functions satisfying the displayed bound: taking \(x=y=0\) first gives \(b(0)=0\), and the equations then give additivity and homogeneity. Such a function is continuous, because \(|b(x)-b(y)|\le\|x-y\|\), and has functional norm at most one. Conversely every functional of norm at most one belongs to this intersection.

Thus the closed unit ball of \(X^*\) is a closed subset of the compact space \(P_X\). A closed subset of a compact space is compact: extend any relative open cover to an ambient open cover by adding its open complement, take a finite subcover, then discard the complement. The restricted product topology is exactly the weak-star topology, because both are the topology generated by the evaluations \(f\mapsto f(x)\). This proves the required compactness. For real \(X\), use real intervals and real coefficients.

### 9.5. Cluster points for the preserved Gaussian proof

Let \((x_a)_{a\in A}\) be a net in a compact space \(K\), where \(A\) is directed and nonempty. For each \(a\), let \(T_a=\{x_b:b\ge a\}\). The closed sets \(\overline{T_a}\) have the finite intersection property: an index dominating a finite list of indices has its entire nonempty tail in all those tails. Their total intersection is nonempty, since otherwise their open complements would cover \(K\), and a finite subcover would contradict the finite intersection property. Fix \(p\) in that intersection. For every neighborhood \(U\) of \(p\) and every \(a\in A\), there is \(b\ge a\) with \(x_b\in U\).

To obtain an actual subnet, form the directed set

\[
B=\{(a,U,b):a,b\in A,\ U\text{ is a neighborhood of }p,
                  \ b\ge a,\ x_b\in U\}.
\]

Order it by

\[
(a,U,b)\preceq(a',U',b')
\quad\Longleftrightarrow\quad
a\le a',\quad U'\subseteq U,\quad b\le b'.
\]

For two triples choose \(c\) dominating their two tail indices and their two selected indices. The cluster property supplies \(b\ge c\) with \(x_b\in U\cap U'\); the triple \((c,U\cap U',b)\) dominates both. The map \(\phi:B\to A\), \(\phi(a,U,b)=b\), is order preserving. For any \(a_0\in A\), the triple \((a_0,K,a_0)\) belongs to \(B\), and every later triple has \(\phi\ge a_0\). Thus \(\phi\) is cofinal in the eventual sense required for a subnet. Finally, given a neighborhood \(V\) of \(p\), choose a triple whose neighborhood is \(V\). Every later triple has neighborhood contained in \(V\), so its selected term lies in \(V\). Hence \((x_{\phi(d)})_{d\in B}\) is a convergent subnet. This applies to the weak-star compact dual ball without separability or metrizability.

### 9.6. The directional limit for the original route

For the application in formula (4), set

\[
q(s)=\frac{\|1+sa\|-1}{s},\qquad s>0.
\]

The triangle inequality and its reverse give \(|q(s)|\le\|a\|\). Thus the finite real number \(L=\limsup_{s\downarrow0}q(s)\) exists by scalar completeness. Choose strictly decreasing \(s_n\downarrow0\) such that \(q(s_n)\to L\). Explicitly, for each \(n\) choose \(\delta_n>0\) with \(\sup_{0<s<\delta_n}q(s)<L+1/n\), and then choose \(s_n<\min\{\delta_n,1/n,s_{n-1}/2\}\) with \(q(s_n)>L-1/n\), omitting the final constraint for \(n=1\). Such a choice exists because the supremum on every interval \((0,\delta)\) is at least \(L\).

After discarding finitely many terms, \(1+s_na\ne0\). Use the norming-functional input already proved in Section 8.1 to choose \(F_n\in C^*\) with \(\|F_n\|=1\) and \(F_n(1+s_na)=\|1+s_na\|\). The dual-ball result and the preceding construction give a weak-star convergent subnet, with limit \(F\). For all \(n\),

\[
|F_n(1)-1|\le |\|1+s_na\|-1|+s_n|F_n(a)|
             \le2s_n\|a\|.
\]

Consequently \(F(1)=1\). The limit is still in the unit dual ball, so \(\|F\|\le1\); since \(\|1\|=1\), its value at \(1\) also gives \(\|F\|\ge1\). Thus \(F\) is normalized. Further,

\[
q(s_n)\le\operatorname{Re}F_n(a),
\]

because \(\operatorname{Re}F_n(1)\le1\). Passage along the convergent subnet gives

\[
L\le\operatorname{Re}F(a)
\le M:=\sup_{G\in\mathcal S_C}\operatorname{Re}G(a).
\]

For every normalized \(G\), evaluating \(1+sa\) gives \(q(s)\ge\operatorname{Re}G(a)\), hence \(\liminf_{s\downarrow0}q(s)\ge M\). Therefore

\[
M\le\liminf q\le\limsup q=L\le M,
\]

which proves the limit in (4) and the precise limsup assertion in Exercise 4. Compactness was used to take a subnet of the bounded functional sequence; no convergent functional subsequence was asserted.

This supplies compactness only. Positivity, functional calculus, state norming, separation and the other operator-algebra inputs of later results remain their own proof scopes.

## References

Gilles Pisier, [*Grothendieck's Theorem, past and present*, expanded UNCUT author version, 21 August 2013](https://webusers.imj-prg.fr/~gilles.pisier/grothendieck.UNCUT.pdf), Appendix 23, Lemma 23.1 and Proposition 23.2, printed pp.78–80 (PDF pp.80–82), supplies the fully read separation, state selection and rescaling method. The corresponding full method was also read in [arXiv:1101.4195v3](https://arxiv.org/pdf/1101.4195v3), printed pp.73–75 (PDF pp.75–77).

The normalized bilinear-functional estimate, Banach algebra Gaussian kernel test, nonunital coefficient projections and unique completed real lift are proved fully in Sections 1–4 here. The survey is not claimed to contain those kernel proofs. Section 5 gives the compact affine argument for arbitrary families, and Section 6 obtains the preliminary 81/16 complex bound. Sections 8–9 supply the complete elementary Gaussian argument and arbitrary-space dual-ball compactness at their stated scalar-calculus and ZFC boundary. Other operator-algebra inputs used by later results retain their separately declared prerequisite scopes. No general Banach algebra normalized functional is assumed positive.
