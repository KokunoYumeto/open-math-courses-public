# Weil's proof for curves and what is missing over the integers

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October revision links the AI Integrated Stacks Project citations and is self-checked by the writing AI. The October revision also corrects points found by GPT-6 Astra (OpenAI), Ultra, in a separate review session, and adds the proof of the Hodge index theorem in Section 3.1. Public domain (CC0).*

## Introduction

Let \(C\) be a curve over a finite field \(\mathbb F_q\). Its zeta function counts the points of \(C\) over the fields \(\mathbb F_{q^r}\). André Weil proved that all zeros of this zeta function lie on the line \(\operatorname{Re}s=\tfrac12\). This is the Riemann hypothesis for curves.

The ring of integers behaves like the ring of functions on a curve, and the Riemann zeta function, completed by a factor at infinity, behaves like the zeta function of that curve. So one asks whether Weil's proof can be repeated for the integers. It cannot be repeated as it stands, because several objects that the proof uses do not exist for the integers. The search for these objects is one of the two origins of geometry over the field with one element. The other origin is the subject of the lesson *Counting over finite fields and the limit q → 1*.

This lesson does three things.

1. Sections 1 to 3 prove the Riemann hypothesis for curves in full. The zeta function, its rationality and its functional equation come from the Riemann–Roch theorem. The Riemann hypothesis comes from the surface \(C\times C\). The graphs of the powers of the Frobenius map are curves on this surface. Their intersection numbers are the point counts, and the Hodge index theorem bounds these numbers.
2. Sections 4 and 5 set up the dictionary between a curve and the integers: places, the completed zeta function, the explicit formula. Section 5 determines the counting function that a curve \(\overline{\operatorname{Spec}\mathbb Z}\) would have, in the sense of [Connes–Consani 2010]. It is a distribution, not a function. The lesson proves its two descriptions, one through the primes and one through the zeros.
3. Section 6 lists, with exact statements, what is missing over the integers: the complete curve and its base field, the product \(\operatorname{Spec}\mathbb Z\times\operatorname{Spec}\mathbb Z\), the Frobenius correspondences, and the positivity.

**What is assumed.** Algebraic curves and the Riemann–Roch theorem, in the language of schemes. The facts that are used are recalled in Section 1. Basic complex analysis is also assumed: holomorphic functions, infinite products, the Gamma function. Intersection theory on surfaces is not assumed. Section 3.1 states the three facts about surfaces that the proof uses and cites each of them. The facts about the Riemann zeta function that are used are stated and cited in Section 4.2.

**Relation to the course.** The lesson *Counting over finite fields and the limit q → 1* treats point counts that are polynomials in \(q\). For a curve of positive genus the point counts are not polynomials, and the correction terms are governed by the zeros of the zeta function. The lesson *What a unified theory must contain* tests each approach of the course against the list of Section 6.

**References.** Basic references are [Stacks] and [Vakil 2024] for curves and surfaces, [Milne 2015] for Weil's proof and its history, the course on the Riemann zeta function (from [Poisson summation, theta, and the functional equation](course:NT-ZETA/NT-ZETA-04) on) and [Bombieri 2000] for the Riemann zeta function, and [Manin 1995], [Connes–Consani–Marcolli 2009a], [Connes–Consani 2010] and [Lorscheid 2018b] for the comparison with the integers.

**Conventions.** Rings are commutative with 1. We write \(d^{\times}u=du/u\) for the invariant measure on the positive real numbers.

## 1. Curves over a finite field

### 1.1 Points

Let \(k=\mathbb F_q\) be a finite field with \(q\) elements. Fix an algebraic closure \(\bar k\), and for \(r\ge 1\) let \(\mathbb F_{q^r}\) be the subfield of \(\bar k\) with \(q^r\) elements.

Throughout Sections 1 to 3, \(C\) is a scheme of dimension one that is smooth and projective over \(k\) and geometrically irreducible. The last condition means that \(C\otimes_k\bar k\) is irreducible. We call \(C\) a *curve over* \(k\). Such a \(C\) is integral, it stays integral after every extension of the base field, and \(H^0(C,\mathcal O_C)=k\) [Stacks, Tag [0BUG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-proper-geometrically-reduced-global-sections)]. Its function field is denoted by \(K\).

A closed point \(x\) of \(C\) has a residue field \(k(x)\), which is a finite extension of \(k\). The *degree* of \(x\) is \(\deg x=[k(x):k]\), and its *norm* is \(\mathrm N x=q^{\deg x}\), the number of elements of \(k(x)\). For \(r\ge 1\) let \(C(\mathbb F_{q^r})\) be the set of morphisms of \(k\)-schemes \(\operatorname{Spec}\mathbb F_{q^r}\to C\). Put

\[ N_r=\#\,C(\mathbb F_{q^r}),\qquad a_d=\#\{x\in C \text{ closed}:\ \deg x=d\}. \]

**Lemma 1.1.** The numbers \(a_d\) and \(N_r\) are finite, and \(N_r=\sum_{d\mid r}d\,a_d\) for all \(r\ge 1\).

**Proof.** A morphism \(\operatorname{Spec}\mathbb F_{q^r}\to C\) over \(k\) is the same as a point \(x\) of \(C\) together with a homomorphism of \(k\)-algebras \(k(x)\to\mathbb F_{q^r}\). Such a point \(x\) is closed, because its residue field is finite over \(k\) [Stacks, Tag [01TE](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-algebraic-residue-field-extension-closed-point-fibre)]. The field \(k(x)\) has \(q^d\) elements, where \(d=\deg x\). It embeds into \(\mathbb F_{q^r}\) if and only if \(d\) divides \(r\). In that case there are exactly \(d\) embeddings, because two embeddings differ by an element of the Galois group of \(k(x)\) over \(k\), which has order \(d\). This gives the formula. For the finiteness, cover \(C\) by finitely many affine open subschemes \(\operatorname{Spec}A_i\), where \(A_i\) is a quotient of a polynomial ring \(k[t_1,\dots,t_n]\). A homomorphism \(A_i\to\mathbb F_{q^r}\) is determined by the images of \(t_1,\dots,t_n\), so there are at most \(q^{rn}\) of them. Hence \(N_r\) is finite, and \(a_r\le N_r/r\). ∎

### 1.2 Divisors and the Riemann–Roch theorem

A *divisor* on \(C\) is a finite formal sum \(D=\sum_x n_x\,x\) of closed points with integer coefficients. Its *degree* is \(\deg D=\sum_x n_x\deg x\). The divisor is *effective*, written \(D\ge 0\), if all \(n_x\) are \(\ge 0\). For a nonzero function \(f\in K\) let \(v_x(f)\) be the order of \(f\) at the closed point \(x\). The divisor of \(f\) is \(\operatorname{div}f=\sum_x v_x(f)\,x\). Two divisors \(D\) and \(D'\) are *linearly equivalent* if \(D'-D=\operatorname{div}f\) for some \(f\). The classes form the group \(\operatorname{Pic}(C)\). This is also the group of invertible sheaves on \(C\) up to isomorphism: the class of \(D\) corresponds to \(\mathcal O_C(D)\). For a divisor \(D\) put

\[ L(D)=\{f\in K^{\times}:\ \operatorname{div}f+D\ge 0\}\cup\{0\}=H^0(C,\mathcal O_C(D)),\qquad \ell(D)=\dim_k L(D). \]

We use the following facts.

- **(R1)** \(\deg\operatorname{div}f=0\) for every \(f\in K^{\times}\). So the degree is defined on \(\operatorname{Pic}(C)\).
- **(R2)** The number \(\ell(D)\) is finite and depends only on the class of \(D\). If \(\deg D<0\), then \(\ell(D)=0\). Moreover \(L(0)=k\).
- **(R3)** (Riemann–Roch.) There are an integer \(g\ge 0\), the *genus* of \(C\), and a divisor \(K_C\) of degree \(2g-2\), such that for every divisor \(D\)

\[ \ell(D)-\ell(K_C-D)=\deg D+1-g. \]

A reference is [Stacks, Tag [0BS6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-lemma-rr)], with [Stacks, Tag [0BY7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-definition-genus)] for the genus and [Stacks, Tag [0C1A](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-lemma-genus-smooth)] for the degree of \(K_C\). Here \(\mathcal O_C(K_C)\) is the sheaf of differentials \(\Omega_{C/k}\). Two consequences are used all the time.

- **(R4)** \(\ell(D)\ge\deg D+1-g\) for all \(D\), with equality if \(\deg D>2g-2\). Indeed \(\ell(K_C-D)\ge 0\), and \(\ell(K_C-D)=0\) when \(\deg(K_C-D)<0\).
- **(R5)** Let \(\deg D=0\). Then \(\ell(D)=1\) if \(D\) is principal, and \(\ell(D)=0\) otherwise. Indeed, if \(f\ne 0\) lies in \(L(D)\), then \(\operatorname{div}f+D\) is effective of degree 0, hence zero, so \(D=\operatorname{div}(f^{-1})\). And \(L(\operatorname{div}h)=h^{-1}L(0)=h^{-1}k\).

**Lemma 1.2.** Let \(D\) be a divisor on \(C\). The number of effective divisors that are linearly equivalent to \(D\) is \((q^{\ell(D)}-1)/(q-1)\).

**Proof.** The effective divisors equivalent to \(D\) are the divisors \(D+\operatorname{div}f\) with \(f\in L(D)\), \(f\ne 0\). Two functions \(f,f'\) give the same divisor if and only if \(\operatorname{div}(f/f')=0\). A function with divisor zero has no poles, so it lies in \(H^0(C,\mathcal O_C)=k\). Hence the effective divisors equivalent to \(D\) correspond to the orbits of \(k^{\times}\) on \(L(D)\smallsetminus\{0\}\). There are \((q^{\ell(D)}-1)/(q-1)\) orbits. ∎

## 2. The zeta function: rationality and the functional equation

**Definition 2.1.** The *zeta function* of \(C\) is the power series

\[ Z(C,T)=\exp\Big(\sum_{r\ge 1}N_r\,\frac{T^r}{r}\Big)\in\mathbb Q[[T]], \]

and \(\zeta_C(s)=Z(C,q^{-s})\).

**Proposition 2.2 (Euler product).** In \(\mathbb Z[[T]]\) one has

\[ Z(C,T)=\prod_{x}\big(1-T^{\deg x}\big)^{-1}=\sum_{D\ge 0}T^{\deg D}, \]

where \(x\) runs over the closed points of \(C\) and \(D\) over the effective divisors.

**Proof.** There are finitely many closed points of each degree, so the product converges in \(\mathbb Z[[T]]\). Its logarithm is

\[ \sum_x\sum_{m\ge 1}\frac{T^{m\deg x}}{m}=\sum_{r\ge 1}\frac{T^r}{r}\sum_{d\mid r}d\,a_d=\sum_{r\ge 1}N_r\,\frac{T^r}{r} \]

by Lemma 1.1. This proves the first equality. Expanding each factor as a geometric series gives the second one, because an effective divisor is a sum of closed points in exactly one way. ∎

In the variable \(s\) the proposition reads \(\zeta_C(s)=\prod_x(1-\mathrm N x^{-s})^{-1}=\sum_{D\ge 0}\mathrm N D^{-s}\), with \(\mathrm N D=q^{\deg D}\).

For an integer \(n\) let \(\operatorname{Pic}^n(C)\) be the set of divisor classes of degree \(n\). For a class \(c\) we write \(\ell(c)\) for \(\ell(D)\), where \(D\) is any divisor in \(c\).

**Theorem 2.3 (rationality).**

1. The group \(\operatorname{Pic}^0(C)\) is finite. Let \(h\) be its order.
2. There is a divisor of degree 1 on \(C\).
3. There is a polynomial \(P(T)\in\mathbb Z[T]\) of degree at most \(2g\), with \(P(0)=1\) and \(P(1)=h\), such that

\[ Z(C,T)=\frac{P(T)}{(1-T)(1-qT)}. \]

*Reference:* due to F. K. Schmidt.

**Proof.** *Step 1.* The image of \(\deg\colon\operatorname{Div}(C)\to\mathbb Z\) is a nonzero subgroup, say \(d\mathbb Z\) with \(d\ge 1\). If \(d\) divides \(n\), adding a fixed divisor of degree \(n\) gives a bijection \(\operatorname{Pic}^0(C)\to\operatorname{Pic}^n(C)\). If \(d\) does not divide \(n\), then \(\operatorname{Pic}^n(C)\) is empty.

*Step 2.* Choose \(n\ge g\) divisible by \(d\). By (R4) every class of degree \(n\) has \(\ell\ge n+1-g\ge 1\), so it contains an effective divisor. By Lemma 1.1 there are only finitely many effective divisors of degree \(n\). So \(\operatorname{Pic}^n(C)\) is finite, and \(\operatorname{Pic}^0(C)\) is finite by Step 1. This proves part 1.

*Step 3.* By Proposition 2.2 and Lemma 1.2,

\[ (q-1)\,Z(C,T)=\sum_{n\ge 0,\ d\mid n}\ \sum_{c\in\operatorname{Pic}^n(C)}\big(q^{\ell(c)}-1\big)T^n. \]

If \(n>2g-2\), then \(\ell(c)=n+1-g\) by (R4), and \(\operatorname{Pic}^n(C)\) has \(h\) elements. Let \(n_0\) be the least multiple of \(d\) with \(n_0\ge 0\) and \(n_0>2g-2\). Then

\[ (q-1)\,Z(C,T)=A(T)+h\,q^{1-g}\frac{(qT)^{n_0}}{1-(qT)^d}-\frac{h}{1-T^d},\qquad A(T)=\sum_{0\le n\le 2g-2,\ d\mid n}\ \sum_{c\in\operatorname{Pic}^n(C)}q^{\ell(c)}T^n. \]

Here \(A\) is a polynomial. So \(Z(C,T)\) is a rational function. The first two terms on the right are holomorphic at \(T=1\), because \(q^d\ne 1\). The third term has a simple pole at \(T=1\). Hence \(Z(C,T)\) has a simple pole at \(T=1\). This holds for every curve over every finite field.

*Step 4.* We show \(d=1\). Let \(C_d=C\otimes_k\mathbb F_{q^d}\). It is a curve over \(\mathbb F_{q^d}\) in the sense of Section 1.1, and \(C_d(\mathbb F_{q^{dm}})=C(\mathbb F_{q^{dm}})\) by the universal property of the base change. So the number of points of \(C_d\) over the extension of degree \(m\) of \(\mathbb F_{q^d}\) is \(N_{dm}\). Let \(\zeta\) run over the \(d\)-th roots of unity. Then

\[ \sum_{\zeta}\log Z(C,\zeta T)=\sum_{r\ge 1}N_r\frac{T^r}{r}\sum_{\zeta}\zeta^r=\sum_{m\ge 1}N_{dm}\frac{T^{dm}}{m}=\log Z(C_d,T^d). \]

By Proposition 2.2 the series \(Z(C,T)\) contains only powers of \(T^d\), so \(Z(C,\zeta T)=Z(C,T)\) for each \(\zeta\). Hence \(Z(C_d,T^d)=Z(C,T)^d\), which has a pole of order \(d\) at \(T=1\) by Step 3. By Step 3 applied to \(C_d\), the function \(U\mapsto Z(C_d,U)\) has a simple pole at \(U=1\), so \(Z(C_d,T^d)\) has a simple pole at \(T=1\). Therefore \(d=1\). This proves part 2.

*Step 5.* With \(d=1\), Step 3 gives for \(g\ge 1\)

\[ (q-1)\,Z(C,T)=A(T)+h\,\frac{q^{g}T^{2g-1}}{1-qT}-\frac{h}{1-T},\qquad A(T)=\sum_{n=0}^{2g-2}\ \sum_{c\in\operatorname{Pic}^n(C)}q^{\ell(c)}T^n, \tag{2.1} \]

and for \(g=0\)

\[ (q-1)\,Z(C,T)=\frac{hq}{1-qT}-\frac{h}{1-T}. \tag{2.2} \]

Put \(P(T)=(1-T)(1-qT)Z(C,T)\). By (2.1) and (2.2) it is a polynomial with rational coefficients of degree at most \(2g\). It lies in \(\mathbb Z[[T]]\) because \(Z(C,T)\) does, so \(P\in\mathbb Z[T]\). Clearly \(P(0)=Z(C,0)=1\). Multiply (2.1) or (2.2) by \((1-T)(1-qT)\) and put \(T=1\): this gives \((q-1)P(1)=-h(1-q)\), so \(P(1)=h\). ∎

**Theorem 2.4 (functional equation).**

\[ Z\Big(C,\frac{1}{qT}\Big)=q^{1-g}\,T^{2-2g}\,Z(C,T). \]

Equivalently \(\zeta_C(1-s)=q^{(g-1)(2s-1)}\zeta_C(s)\). Equivalently the function \(q^{(g-1)s}\zeta_C(s)\) is invariant under \(s\mapsto 1-s\).

*Reference:* [Lorscheid 2018b, Section 1.2] states the functional equation as \(\zeta(1-s)=\pm q^{(2g-2)(1-s)}\zeta(s)\); this fails for the projective line, where \(\zeta(1-s)=q^{1-2s}\zeta(s)\) by Example 2.9, so we prove the form above.

**Proof.** Let \(g\ge 1\) and write (2.1) as \((q-1)Z(C,T)=A(T)+B(T)\), where \(B(T)=h\,q^gT^{2g-1}/(1-qT)-h/(1-T)\). We show that \(A\) and \(B\) each satisfy the functional equation.

For \(B\), a direct computation gives

\[ B\Big(\frac{1}{qT}\Big)=h\Big(\frac{qT}{1-qT}-\frac{q^{1-g}T^{2-2g}}{1-T}\Big)=q^{1-g}T^{2-2g}B(T). \]

For \(A\), let \(\kappa\) be the class of \(K_C\). The map \(c\mapsto\kappa-c\) is an involution of the set of classes of degree between \(0\) and \(2g-2\), and \(\deg(\kappa-c)=2g-2-\deg c\). By (R3), \(\ell(c)=\ell(\kappa-c)+\deg c+1-g\). Therefore

\[ A\Big(\frac{1}{qT}\Big)=\sum_c q^{\ell(c)-\deg c}\,T^{-\deg c}=q^{1-g}\,T^{2-2g}\sum_c q^{\ell(\kappa-c)}\,T^{\deg(\kappa-c)}=q^{1-g}\,T^{2-2g}A(T). \]

For \(g=0\) we have \(h=1\): a divisor \(D\) of degree 0 has \(\ell(D)=1\) by (R4), so it is principal by (R5). Then (2.2) gives \(Z(C,T)=1/((1-T)(1-qT))\), and the functional equation is checked directly. The statement in the variable \(s\) follows with \(T=q^{-s}\), since \(1/(qT)=q^{-(1-s)}\). ∎

**Corollary 2.5 (the inverse roots).** The polynomial \(P\) has degree exactly \(2g\) and leading coefficient \(q^g\). Write

\[ P(T)=\prod_{j=1}^{2g}(1-\alpha_jT),\qquad \alpha_j\in\mathbb C. \]

1. The \(\alpha_j\) are algebraic integers, and \(\prod_j\alpha_j=q^g\).
2. The family \((\alpha_j)\) is stable, with multiplicities, under \(\alpha\mapsto q/\alpha\) and under complex conjugation.
3. For all \(r\ge 1\): \(N_r=q^r+1-\sum_{j}\alpha_j^r\).
4. \(1\le\lvert\alpha_j\rvert\le q\) for all \(j\).

**Proof.** From Theorem 2.4 and the definition of \(P\) one gets \(P(T)=q^gT^{2g}P(1/(qT))\). Write \(P(T)=\sum_i b_iT^i\). Comparing coefficients gives \(b_{2g-i}=q^{g-i}b_i\). In particular \(b_{2g}=q^gb_0=q^g\). So \(P\) has degree \(2g\) and the \(\alpha_j\) are nonzero. They are the roots of the monic integer polynomial \(T^{2g}P(1/T)\), so they are algebraic integers, and they are stable under conjugation. Their product is the constant term \(b_{2g}=q^g\) of this polynomial. Next,

\[ P(T)=q^gT^{2g}\prod_j\Big(1-\frac{\alpha_j}{qT}\Big)=q^{-g}\prod_j\alpha_j\cdot\prod_j\Big(1-\frac{q}{\alpha_j}T\Big)=\prod_j\Big(1-\frac{q}{\alpha_j}T\Big), \]

which proves part 2. Part 3 follows by taking the logarithm of \(Z(C,T)=\prod_j(1-\alpha_jT)/((1-T)(1-qT))\) and comparing coefficients with Definition 2.1.

For part 4, note that \(P(1/q)=q^{-g}P(1)=q^{-g}h\ne 0\). So \(Z(C,T)\) has a pole at \(T=1/q\) and no pole of smaller absolute value, and the power series \(\sum_{D\ge 0}T^{\deg D}\) converges for \(\lvert T\rvert<1/q\). Its coefficients are \(\ge 0\). So \(\sum_x\lvert T\rvert^{\deg x}\) is finite for \(\lvert T\rvert<1/q\), the product of Proposition 2.2 converges absolutely there, and it does not vanish. Hence \(P\) has no zero with \(\lvert T\rvert<1/q\), that is, \(\lvert\alpha_j\rvert\le q\). By part 2 also \(\lvert q/\alpha_j\rvert\le q\). ∎

In the variable \(s\), part 4 says that the zeros of \(\zeta_C\) lie in the strip \(0\le\operatorname{Re}s\le 1\). The function \(\zeta_C\) has period \(2\pi i/\log q\). Its poles are simple and lie at \(s=0\) and \(s=1\) up to periods.

**Definition 2.6.** The *Riemann hypothesis for* \(C\) is the statement \(\lvert\alpha_j\rvert=\sqrt q\) for all \(j\).

**Lemma 2.7.** Let \(\beta_1,\dots,\beta_n\) be nonzero complex numbers and let \(A,B>0\). If \(\lvert\sum_j\beta_j^r\rvert\le AB^r\) for all \(r\ge 1\), then \(\lvert\beta_j\rvert\le B\) for all \(j\).

**Proof.** The power series \(\sum_{r\ge 1}(\sum_j\beta_j^r)T^r\) converges for \(\lvert T\rvert<1/B\). It is the expansion of the rational function \(\sum_j\beta_jT/(1-\beta_jT)\). Collect equal \(\beta_j\). Then this function has a pole at \(T=1/\beta\) for every value \(\beta\) that occurs, because distinct values give distinct poles and nothing cancels. A convergent power series has no pole in its disc of convergence. So \(1/\lvert\beta\rvert\ge 1/B\). ∎

**Proposition 2.8 (equivalent forms).** The following are equivalent.

1. The Riemann hypothesis for \(C\).
2. Every zero of \(\zeta_C(s)\) has real part \(\tfrac12\).
3. \(\lvert N_r-q^r-1\rvert\le 2g\,q^{r/2}\) for all \(r\ge 1\).
4. There is a constant \(A\) with \(\lvert N_r-q^r-1\rvert\le A\,q^{r/2}\) for all \(r\ge 1\).

**Proof.** The zeros of \(\zeta_C\) are the \(s\) with \(q^s=\alpha_j\) for some \(j\), and then \(\operatorname{Re}s=\log\lvert\alpha_j\rvert/\log q\). So 1 and 2 are equivalent. By Corollary 2.5, \(N_r-q^r-1=-\sum_j\alpha_j^r\). So 1 implies 3, and 3 implies 4. Assume 4. Lemma 2.7 with \(B=\sqrt q\) gives \(\lvert\alpha_j\rvert\le\sqrt q\) for all \(j\). Since \(q/\alpha_j\) is again one of the \(\alpha\)'s, also \(\lvert\alpha_j\rvert\ge\sqrt q\). ∎

**Example 2.9 (genus zero).** Let \(g=0\). The proof of Theorem 2.4 showed \(h=1\) and

\[ Z(C,T)=\frac{1}{(1-T)(1-qT)},\qquad N_r=q^r+1. \]

There are no zeros, and the Riemann hypothesis is an empty statement. The functional equation is \(\zeta_C(1-s)=q^{1-2s}\zeta_C(s)\). Note what was proved on the way: every curve of genus zero over a finite field has exactly \(q+1\) rational points. No rational point was assumed. For instance, the conic \(x^2+y^2+z^2=0\) in the projective plane over \(\mathbb F_3\) is smooth, because its partial derivatives \(2x,2y,2z\) have no common zero. It is geometrically irreducible, because two components of a plane curve meet, and a meeting point would be singular. Its genus is zero [Stacks, Tag [0BYD](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-lemma-genus-plane-curve)]. It has the four points \((1:1:1)\), \((1:1:2)\), \((1:2:1)\), \((1:2:2)\), and \(q+1=4\).

**Example 2.10 (an elliptic curve over the field with two elements).** Let \(E\) be the projective closure of \(y^2+y=x^3+x\) over \(\mathbb F_2\), that is, the plane cubic \(y^2z+yz^2=x^3+xz^2\). Its partial derivatives are \(x^2+z^2\), \(z^2\) and \(y^2\). They have no common zero except \(x=y=z=0\), over any extension of \(\mathbb F_2\). So \(E\) is a smooth plane cubic. It is geometrically irreducible for the same reason as the conic of Example 2.9. Its genus is 1 [Stacks, Tag [0BYD](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-lemma-genus-plane-curve)].

Over \(\mathbb F_2\) the affine points are \((0,0),(0,1),(1,0),(1,1)\), and there is one point at infinity, \((0:1:0)\). So \(N_1=5\). By Corollary 2.5, \(P(T)=1-(\alpha_1+\alpha_2)T+\alpha_1\alpha_2T^2\) with \(\alpha_1\alpha_2=2\) and \(\alpha_1+\alpha_2=q+1-N_1=-2\). Hence

\[ P(T)=1+2T+2T^2,\qquad \alpha_{1,2}=-1\pm i,\qquad \lvert\alpha_{1,2}\rvert=\sqrt 2. \]

The Riemann hypothesis holds for \(E\). Corollary 2.5 predicts \(N_2=5-2\operatorname{Re}(-1+i)^2=5\), \(N_3=9-2\operatorname{Re}(-1+i)^3=5\) and \(N_4=17-2\operatorname{Re}(-1+i)^4=25\). Here is a direct check of \(N_2\). Write \(\mathbb F_4=\{0,1,\omega,\omega+1\}\) with \(\omega^2=\omega+1\). The map \(y\mapsto y^2+y\) sends \(0,1\) to \(0\) and \(\omega,\omega+1\) to \(1\). The map \(x\mapsto x^3+x\) sends \(0,1\) to \(0\), sends \(\omega\) to \(\omega+1\), and sends \(\omega+1\) to \(\omega\). So there are four affine points, all with \(x\in\{0,1\}\), and one point at infinity: \(N_2=5\).

The class number is \(h=P(1)=5\). The bound of Proposition 2.8 reads \(\lvert N_1-3\rvert\le 2\sqrt 2\). It is attained as far as integers allow: \(N_1=5\) is the largest number of points that a curve of genus 1 over \(\mathbb F_2\) can have.

*Reference:* [Lorscheid 2018b, Section 1.2] states the Riemann hypothesis in genus one as the bound \(q-2\sqrt q\le N_1\le q+2\sqrt q\); this fails for \(E\), where \(q=2\) and \(N_1=5\), and the interval must be centred at \(q+1\) as in Proposition 2.8.

**Example 2.11 (why geometric irreducibility is assumed).** Let \(X\) be the projective line over \(\mathbb F_{q^2}\), regarded as a scheme over \(k=\mathbb F_q\). It is smooth, projective and irreducible over \(k\), but \(X\otimes_k\bar k\) has two components, and \(H^0(X,\mathcal O_X)=\mathbb F_{q^2}\). A morphism \(\operatorname{Spec}\mathbb F_{q^r}\to X\) over \(k\) induces an embedding of \(\mathbb F_{q^2}\) into \(\mathbb F_{q^r}\). So \(N_r=0\) for odd \(r\). For even \(r\) there are two embeddings and \(N_r=2(q^r+1)\). Therefore

\[ Z(X,T)=\exp\Big(\sum_{m\ge 1}\big(q^{2m}+1\big)\frac{T^{2m}}{m}\Big)=\frac{1}{(1-T^2)(1-q^2T^2)}. \]

This is not of the form of Theorem 2.3: there are poles at \(T=-1\) and \(T=-1/q\), and every divisor has even degree. In Sections 1 and 2 the hypothesis of geometric irreducibility enters in two places. The facts (R2) and (R3) and Lemma 1.2 use \(H^0(C,\mathcal O_C)=k\). Step 4 of the proof of Theorem 2.3 uses that the base change of a curve is again a curve; the base change of \(X\) to \(\mathbb F_{q^2}\) is not irreducible.

## 3. The surface \(C\times C\) and the Riemann hypothesis

### 3.1 The surface, and the facts about surfaces that are used

Let \(S=C\times_kC\), with the projections \(p_1,p_2\colon S\to C\). The scheme \(S\) is smooth of dimension two over \(k\) [Stacks, Tags [01VB](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-base-change-smooth) and [01VA](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-composition-smooth)], and it is projective over \(k\). It is irreducible, because \(C\) is geometrically irreducible [Stacks, Tag [038F](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-bijection-irreducible-components)]. So \(S\) is a regular integral projective surface [Stacks, Tag [056S](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-smooth-regular)]. Let \(\delta=(\mathrm{id},\mathrm{id})\colon C\to S\) be the diagonal morphism. Its image \(\Delta\) is the *diagonal*.

We write \(\operatorname{Pic}(S)\) for the group of invertible sheaves on \(S\) up to isomorphism, and we write it additively: \(L+M\) means \(L\otimes M\). If \(D\subset S\) is an effective Cartier divisor, we also write \(D\) for the class of \(\mathcal O_S(D)\). A divisor on \(S\), or its class in \(\operatorname{Pic}(S)\), is called a *correspondence* on \(C\).

The proof uses three facts about surfaces.

**(S1) Intersection numbers.** Let \(L\) and \(M\) be invertible sheaves on \(S\). The function \((m,n)\mapsto\chi(S,L^{\otimes m}\otimes M^{\otimes n})\) is a polynomial in \((m,n)\) of total degree at most 2 [Stacks, Tag [0BEM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-numerical-polynomial-from-euler)]. The *intersection number* \((L\cdot M)\) is the coefficient of \(mn\) [Stacks, Tag [0BEP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-definition-intersection-number)]. It is an integer [Stacks, Tag [0BEQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-intersection-number-integer)]. It is symmetric in \(L\) and \(M\) by definition, and it is additive in each variable [Stacks, Tag [0BER](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-intersection-number-additive)].

**(S2) Restriction to a curve.** Let \(D\subset S\) be an effective Cartier divisor. Then \(D\) is a proper scheme over \(k\) of dimension one if it is nonempty (the empty divisor, \(\mathcal O_S(D)=\mathcal O_S\), has degree \(0\) on both sides below), and for every invertible sheaf \(L\) on \(S\)

\[ (L\cdot\mathcal O_S(D))=\deg(L\vert_D) \]

[Stacks, Tags [0BEU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-numerical-intersection-effective-Cartier-divisor) and [0BEY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-intersection-numbers-and-degrees-on-curves)]. Here the degree of an invertible sheaf \(M\) on \(D\) is \(\deg M=\chi(D,M)-\chi(D,\mathcal O_D)\) [Stacks, Tag [0AYR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-definition-degree-invertible-sheaf)].

**(S3) The Hodge index theorem.** Let \(L\) and \(H\) be invertible sheaves on \(S\) with \((H\cdot H)>0\) and \((L\cdot H)=0\). Then \((L\cdot L)\le 0\). If moreover \((L\cdot L)=0\), then \(L\) is *numerically trivial*: \((L\cdot M)=0\) for every invertible sheaf \(M\). It is proved at the end of this section; see also [Vakil 2024, Theorem 20.2.13].

The proof also uses four facts about degrees on curves. Let \(X\) and \(Y\) be integral proper schemes of dimension one over \(k\).

- **(C1)** \(\deg(M\otimes M')=\deg M+\deg M'\) for invertible sheaves \(M,M'\) on \(X\) [Stacks, Tag [0AYX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-degree-tensor-product)].
- **(C2)** If \(E\subset X\) is an effective Cartier divisor, then \(\deg\mathcal O_X(E)=\dim_k\Gamma(E,\mathcal O_E)\) [Stacks, Tag [0AYY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-degree-effective-Cartier-divisor)]. For \(X=C\) and \(E\) a closed point \(x\), this number is \(\deg x\).
- **(C3)** If \(f\colon X\to Y\) is a nonconstant morphism over \(k\) and \(M\) is an invertible sheaf on \(Y\), then \(\deg f^{\ast}M=\deg(f)\,\deg M\). Here \(\deg(f)\) is the degree of the extension of function fields [Stacks, Tags [0AYZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-degree-pullback-map-proper-curves) and [02NY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-definition-degree)].
- **(C4)** The conormal sheaf of an effective Cartier divisor \(D\) in a scheme \(X\) is \(\mathcal O_X(-D)\vert_D\) [Stacks, Tag [0B3P](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-conormal-effective-Cartier-divisor)]. The conormal sheaf of the diagonal \(\Delta\) in \(S\) is \(\Omega_{C/k}\) [Stacks, Tag [08S2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-differentials-diagonal)]. The degree of \(\Omega_{C/k}\) is \(2g-2\) [Stacks, Tag [0C1A](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-lemma-genus-smooth)].

Nothing else about surfaces is used. The proof of (S3) uses, besides (S1) and (S2), only Serre duality and basic facts on ample invertible sheaves; neither the adjunction formula nor the Riemann–Roch theorem for surfaces is needed.

**Proof of (S3).** Besides (S1) and (S2) we use the following facts, valid over every field.

**(D1) Serre duality.** The surface \(S\) is regular, hence Cohen–Macaulay and Gorenstein [Stacks, Tags [00NQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-regular-ring-CM) and [0AWX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dualizing.html#dualizing-lemma-regular-gorenstein)], and it is proper and equidimensional of dimension \(2\). So its dualizing module \(\omega_S\) is invertible, and for every invertible sheaf \(L\)
\[ \dim_kH^2(S,L)=\dim_k\operatorname{Hom}(L,\omega_S)=\dim_kH^0(S,\omega_S\otimes L^{\otimes-1}) \]
[Stacks, Tags [0FVZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/duality.html#duality-lemma-duality-proper-over-field-CM), part (3) with \(K=L\) and \(i=-2\), and [0BFQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/duality.html#duality-lemma-gorenstein)]. The groups \(H^i(S,L)\) are finite dimensional and vanish for \(i>2\) [Stacks, Tags [02O6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-proper-over-affine-cohomology-finite) and [02UZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-proposition-vanishing-Noetherian)], so \(\chi(S,L)\le\dim_kH^0(S,L)+\dim_kH^2(S,L)\).

**(D2) Sections.** Let \(s\neq0\) be a global section of an invertible sheaf \(L\) on \(S\). If \(s\) vanished on a nonempty open subset, then on every affine open \(U=\operatorname{Spec}R\) on which \(L\) is trivial, \(s\) would be an element of the domain \(R\) whose image in the function field is zero, so \(s=0\). Hence on each such \(U\) the section \(s\) is a nonzero element of a domain, a nonzerodivisor, and the ideal sheaf \(s\,L^{\otimes-1}\subset\mathcal O_S\) is locally generated by one nonzerodivisor. It defines an effective Cartier divisor \(E\) with \(\mathcal O_S(E)\cong L\) [Stacks, Definitions [01WR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-definition-effective-Cartier-divisor) and [01WX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-definition-invertible-sheaf-effective-Cartier-divisor)].

**(D3) Positivity.** If \(A\) is ample, then \((A\cdot A)>0\), and \((A\cdot\mathcal O_S(E))=\deg(A\vert_E)>0\) for every nonempty effective Cartier divisor \(E\), which is a proper scheme of dimension one [Stacks, Tag [0BEV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-ample-positive); (S2)].

**(D4) Twisting.** If \(A\) is ample and \(D\) is invertible, then \(D\otimes A^{\otimes m}\) is globally generated for some \(m\ge1\) [Stacks, Tag [01Q3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/properties.html#properties-proposition-characterize-ample)], so \(D\otimes A^{\otimes(m+1)}\) is ample [Stacks, Tag [0890](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/properties.html#properties-lemma-ample-tensor-globally-generated)].

*Step 1.* For an invertible sheaf \(D\), the function \(n\mapsto\chi(S,D^{\otimes n})\) is a polynomial of degree at most 2 whose coefficient of \(n^2\) is \((D\cdot D)/2\). Indeed, by (S1) with \(L=M=D\), \(Q(m,n)=\chi(S,D^{\otimes(m+n)})\) is a polynomial of total degree at most 2. So \(P(t)=Q(t,0)\) is a polynomial \(at^2+bt+c\), and \(Q(m,n)=P(m+n)\) on \(\mathbb Z^2\), hence as polynomials. The coefficient of \(mn\) in \(P(m+n)\) is \(2a\), so \((D\cdot D)=2a\).

*Step 2.* Let \(D\) be invertible with \((D\cdot D)>0\), and let \(A'\) be ample with \((D\cdot A')>0\). Then \(H^0(S,D^{\otimes n})\neq0\) for all large \(n\). Indeed, if \(H^0(S,\omega_S\otimes D^{\otimes-n})\neq0\), then by (D2) \(\omega_S\otimes D^{\otimes-n}\cong\mathcal O_S(E)\) with \(E\) effective, and by (S1) and (D3)
\[ (\omega_S\cdot A')-n\,(D\cdot A')=(\mathcal O_S(E)\cdot A')\ \ge\ 0 \]
(the right side is \(0\) if \(E\) is empty). So \(H^0(S,\omega_S\otimes D^{\otimes-n})=0\) for \(n>(\omega_S\cdot A')/(D\cdot A')\), and then \(H^2(S,D^{\otimes n})=0\) by (D1). By (D1) and Step 1, \(\dim_kH^0(S,D^{\otimes n})\ge\chi(S,D^{\otimes n})=\tfrac12(D\cdot D)n^2+bn+c\), which is positive for large \(n\).

*Step 3 (an ample class).* If \(A\) is ample and \((D\cdot A)=0\), then \((D\cdot D)\le0\). Suppose instead \((D\cdot D)>0\). By (D4), \(A'=D\otimes A^{\otimes(m+1)}\) is ample, and \((D\cdot A')=(D\cdot D)+(m+1)(D\cdot A)=(D\cdot D)>0\). By Step 2 and (D2) there are \(n\ge1\) and an effective Cartier divisor \(E\) with \(D^{\otimes n}\cong\mathcal O_S(E)\). The divisor \(E\) is not empty, since otherwise \(n^2(D\cdot D)=(\mathcal O_S\cdot\mathcal O_S)=0\). By (D3), \(n(D\cdot A)=(\mathcal O_S(E)\cdot A)>0\), a contradiction.

*Step 4 (no positive plane).* Extend the intersection number bilinearly to \(V=\operatorname{Pic}(S)\otimes_{\mathbb Z}\mathbb R\), put \(q(x)=(x\cdot x)\), and fix an ample \(A\) (\(S\) is projective). Let \(W\subset V\) be spanned by finitely many classes of invertible sheaves, one of them \(A\). Then \(W\) has no two-dimensional subspace on which \(q\) is positive definite. Indeed, let \(K\subset W\) be the kernel of \(x\mapsto(x\cdot A)\), a hyperplane because \((A\cdot A)>0\). This linear form has integer values on the spanning classes, so the combinations of them with rational coefficients that lie in \(K\) are dense in \(K\). For such a combination \(x\), some multiple \(Nx\) with \(N\ge1\) is the class of an invertible sheaf \(D\) with \((D\cdot A)=0\), so \(q(x)=(D\cdot D)/N^2\le0\) by Step 3. By continuity, \(q\le0\) on \(K\). Every two-dimensional subspace of \(W\) meets the hyperplane \(K\) in a nonzero vector, so \(q\) is not positive definite on it.

*Step 5.* Let \((H\cdot H)>0\) and \((L\cdot H)=0\), and let \(W\) be spanned by \(A\), \(H\) and \(L\). If \((L\cdot L)>0\), then \(H\) and \(L\) are linearly independent in \(W\) (if \(L=cH\), then \(c(H\cdot H)=(L\cdot H)=0\), so \(c=0\) and \((L\cdot L)=0\)), and \(q(\alpha H+\beta L)=\alpha^2(H\cdot H)+\beta^2(L\cdot L)>0\) for \((\alpha,\beta)\neq(0,0)\). This contradicts Step 4, so \((L\cdot L)\le0\). Suppose now that \((L\cdot L)=0\) and \((L\cdot M)\neq0\) for some invertible \(M\). Let \(W\) be spanned by \(A\), \(H\), \(L\) and \(M\), and put \(M'=M-\tfrac{(M\cdot H)}{(H\cdot H)}H\). Then \((M'\cdot H)=0\) and \((L\cdot M')=(L\cdot M)\). For real \(t\), the vector \(N=L+tM'\) satisfies \((N\cdot H)=0\) and \(q(N)=2t(L\cdot M)+t^2q(M')\), which is positive for small \(t\neq0\) of the same sign as \((L\cdot M)\). Then \(H\) and \(N\) span a plane on which \(q\) is positive definite, as before, contradicting Step 4. So \(L\) is numerically trivial. ∎

### 3.2 Curves on the surface and their two degrees

**Lemma 3.1 (pull-back of a divisor).** Let \(f\colon X'\to X\) be a morphism of schemes and let \(D\subset X\) be an effective Cartier divisor. Suppose that the closed subscheme \(D'=f^{-1}(D)\) of \(X'\) is an effective Cartier divisor. Then \(f^{\ast}\mathcal O_X(D)\cong\mathcal O_{X'}(D')\).

The hypothesis holds if \(f\) is flat, and it holds if \(X'\) is integral and its generic point is not mapped into \(D\) [Stacks, Tag [02OO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-pullback-effective-Cartier-defined)].

**Proof.** Let \(\mathcal I\subset\mathcal O_X\) and \(\mathcal I'\subset\mathcal O_{X'}\) be the ideal sheaves of \(D\) and \(D'\). By definition of the inverse image, \(\mathcal I'\) is the image of \(f^{\ast}\mathcal I\to\mathcal O_{X'}\). So there is a surjection \(f^{\ast}\mathcal I\to\mathcal I'\) of invertible sheaves. A surjection of invertible sheaves is an isomorphism. Since \(\mathcal I=\mathcal O_X(-D)\) and \(\mathcal I'=\mathcal O_{X'}(-D')\), the claim follows by taking duals. ∎

**Lemma 3.2 (the curves that we use).**

1. Let \(x\) be a closed point of \(C\). Then \(E_x=p_1^{-1}(x)\) is an effective Cartier divisor on \(S\), and \(\mathcal O_S(E_x)\cong p_1^{\ast}\mathcal O_C(x)\). The scheme \(E_x\) is integral, and \(p_2\) restricts to a morphism \(E_x\to C\) of degree \(\deg x\).
2. Let \(\varphi\colon C\to C\) be a finite morphism of \(k\)-schemes. Then \(\gamma_\varphi=(\mathrm{id},\varphi)\colon C\to S\) is a closed immersion, its image \(\Gamma_\varphi\) is an effective Cartier divisor on \(S\), and \(\mathcal O_S(\Gamma_\varphi)\cong(\varphi\times\mathrm{id})^{\ast}\mathcal O_S(\Delta)\). In particular \(\Delta=\Gamma_{\mathrm{id}}\) is an effective Cartier divisor.

**Proof.** 1. The morphism \(p_1\) is flat, so Lemma 3.1 applies to the divisor \(x\) on \(C\). The scheme \(E_x\) is \(C\otimes_kk(x)\). It is integral because \(C\) is geometrically integral. Its function field is \(K\otimes_kk(x)\), which has degree \(\deg x\) over \(K\).

2. The morphism \(\gamma_\varphi\) is a section of \(p_1\). A section of a separated morphism is a closed immersion [Stacks, Tag [01KT](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-section-immersion)], and a section of a smooth morphism is a regular immersion [Stacks, Tag [067R](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-section-smooth-regular-immersion)]. So the ideal of \(\Gamma_\varphi\) is locally generated by a regular sequence. Its length is one, because \(\Gamma_\varphi\cong C\) has dimension one and \(S\) has dimension two. So the ideal is locally generated by one nonzerodivisor, which means that \(\Gamma_\varphi\) is an effective Cartier divisor. Next, the inverse image of \(\Delta\) under \(\varphi\times\mathrm{id}\colon S\to S\) is \(\Gamma_\varphi\). Indeed, for a test scheme \(T\), a point \((a,b)\in S(T)\) is mapped into \(\Delta\) if and only if \(\varphi(a)=b\), that is, if and only if \((a,b)=\gamma_\varphi(a)\). Now apply Lemma 3.1. ∎

**Lemma 3.3 (fibres).** Let \(A\) and \(B\) be invertible sheaves on \(C\). Then

\[ (p_1^{\ast}A\cdot p_1^{\ast}B)=0,\qquad (p_2^{\ast}A\cdot p_2^{\ast}B)=0,\qquad (p_1^{\ast}A\cdot p_2^{\ast}B)=\deg A\,\deg B. \]

**Proof.** Every invertible sheaf on \(C\) is of the form \(\mathcal O_C(D)\) for a divisor \(D\). By (S1) it suffices to treat \(A=\mathcal O_C(x)\) for a closed point \(x\). By Lemma 3.2 and (S2), for every invertible sheaf \(M\) on \(S\),

\[ (p_1^{\ast}\mathcal O_C(x)\cdot M)=\deg(M\vert_{E_x}). \]

Let \(M=p_1^{\ast}B\). The restriction of \(p_1\) to \(E_x\) factors through \(\operatorname{Spec}k(x)\), and every invertible sheaf on \(\operatorname{Spec}k(x)\) is trivial. So \(M\vert_{E_x}\) is trivial and has degree 0. Let \(M=p_2^{\ast}B\). Then \(M\vert_{E_x}\) is the pull-back of \(B\) under the morphism \(E_x\to C\) of degree \(\deg x\). By (C3) and (C2) its degree is \(\deg x\,\deg B=\deg\mathcal O_C(x)\,\deg B\). The statement for \(p_2\) follows by symmetry. ∎

**Lemma 3.4 (the two degrees of a correspondence).** There are unique homomorphisms \(d_1,d_2\colon\operatorname{Pic}(S)\to\mathbb Z\) such that for all \(L\in\operatorname{Pic}(S)\) and all invertible sheaves \(B\) on \(C\)

\[ (L\cdot p_1^{\ast}B)=d_1(L)\,\deg B,\qquad (L\cdot p_2^{\ast}B)=d_2(L)\,\deg B. \]

They satisfy \(d_1(p_1^{\ast}A)=0\), \(d_2(p_1^{\ast}A)=\deg A\), \(d_1(p_2^{\ast}A)=\deg A\), \(d_2(p_2^{\ast}A)=0\). If \(D\subset S\) is an effective Cartier divisor that is an integral scheme, then \(d_i(D)\) is the degree of the morphism \(p_i\vert_D\colon D\to C\), to be read as 0 if this morphism is constant.

**Proof.** Fix \(L\) and \(i\). By (S1) the map \(B\mapsto(L\cdot p_i^{\ast}B)\) is a homomorphism \(\operatorname{Pic}(C)\to\mathbb Z\). It vanishes on \(\operatorname{Pic}^0(C)\), because this group is finite by Theorem 2.3 and \(\mathbb Z\) has no torsion. The degree \(\operatorname{Pic}(C)\to\mathbb Z\) is surjective by Theorem 2.3, with kernel \(\operatorname{Pic}^0(C)\). So the map is a multiple of the degree, and this defines the integer \(d_i(L)\). It is additive in \(L\) by (S1). The values on \(p_j^{\ast}A\) are Lemma 3.3. For the last statement use (S2): \((D\cdot p_i^{\ast}B)\) is the degree of the pull-back of \(B\) under \(p_i\vert_D\). If \(p_i\vert_D\) is not constant, this is \(\deg(p_i\vert_D)\deg B\) by (C3). If it is constant, it factors through \(\operatorname{Spec}k(x)\) for a closed point \(x\), and the pull-back is trivial. ∎

So \(d_1(L)\) is the intersection number of \(L\) with a fibre \(\{x\}\times C\), divided by \(\deg x\), and \(d_2(L)\) is the same for the fibres \(C\times\{x\}\). In [Connes–Consani–Marcolli 2009a, (2.19)] these are the degree \(d\) and the codegree \(d'\) of a correspondence.

Fix an invertible sheaf \(B_1\) of degree 1 on \(C\), which exists by Theorem 2.3, and put

\[ V=p_1^{\ast}B_1,\qquad W=p_2^{\ast}B_1. \]

Then \((V\cdot V)=(W\cdot W)=0\) and \((V\cdot W)=1\) by Lemma 3.3, and \(d_1(L)=(L\cdot V)\), \(d_2(L)=(L\cdot W)\) for all \(L\).

### 3.3 The Frobenius correspondences

The *Frobenius morphism* \(F\colon C\to C\) is the identity on the underlying topological space and the map \(a\mapsto a^q\) on the structure sheaf. For \(r\ge 0\) put

\[ \gamma_r=(\mathrm{id},F^r)\colon C\to S,\qquad \Gamma_r=\gamma_r(C). \]

So \(\Gamma_0=\Delta\). We call \(\Gamma_r\) the \(r\)-th *Frobenius correspondence*. On the points of \(C\) with values in \(\bar k\), the map \(F^r\) raises the coordinates to the power \(q^r\), and its fixed points are the points with values in \(\mathbb F_{q^r}\). Lemma 3.6 is the precise form of this statement.

**Lemma 3.5.** The morphism \(F\) is a morphism of \(k\)-schemes. It is finite, and \(F^r\) has degree \(q^r\).

**Proof.** We have \(a^q=a\) for \(a\in k\), so \(F\) commutes with the structure morphism to \(\operatorname{Spec}k\). It is finite, because every local section \(a\) is a root of the monic polynomial \(X^q-a^q\) over the image of \(F\), and \(C\) is of finite type. On the function field, \(F^r\) induces \(a\mapsto a^{q^r}\), with image \(K^{q^r}\). So \(\deg F^r=[K:K^{q^r}]\). The map \(a\mapsto a^{q}\) is an isomorphism from \(K\) onto \(K^q\) that carries \(K^{q^{i}}\) onto \(K^{q^{i+1}}\). Hence \([K^{q^i}:K^{q^{i+1}}]=[K:K^q]\) for all \(i\), and it suffices to prove \([K:K^q]=q\).

Choose \(t\in K\) transcendental over \(k\), and let \(n=[K:k(t)]\), which is finite. The isomorphism \(K\to K^q\) carries \(k(t)\) onto \(k(t^q)\), because every element of \(k\) is a \(q\)-th power. So \([K^q:k(t^q)]=n\). Also \([k(t):k(t^q)]=q\): the element \(t\) is a root of \(X^q-t^q\), which is irreducible over \(k(t^q)\) by Eisenstein's criterion for the prime element \(t^q\) of \(k[t^q]\). Computing \([K:k(t^q)]\) in two ways gives \(n\,q=[K:K^q]\,n\). ∎

**Lemma 3.6 (fixed points of Frobenius).** Let \(r\ge 1\) and let \(\Phi_r=\delta^{-1}(\Gamma_r)\), a closed subscheme of \(C\). Then \(\Phi_r\) is the disjoint union of the schemes \(\operatorname{Spec}k(x)\), where \(x\) runs over the closed points of \(C\) whose degree divides \(r\). It is an effective Cartier divisor on \(C\), and

\[ \dim_k\Gamma(\Phi_r,\mathcal O_{\Phi_r})=N_r. \]

**Proof.** A point \(a\) of \(C\) with values in a scheme \(T\) lies in \(\Phi_r\) if and only if \((a,a)=\gamma_r(b)\) for some \(b\), that is, if and only if \(F^r(a)=a\). So \(\Phi_r\) is the largest closed subscheme of \(C\) on which \(F^r\) and the identity agree. Let \(U=\operatorname{Spec}A\) be an affine open subscheme of \(C\). Since \(F^r\) is the identity on points, it maps \(U\) to \(U\), and it is given by \(a\mapsto a^{q^r}\) on \(A\). Hence \(\Phi_r\cap U=\operatorname{Spec}B\) with

\[ B=A/I,\qquad I=\big(a^{q^r}-a:\ a\in A\big). \]

Every \(b\in B\) satisfies \(b^{q^r}=b\). So \(B\) is reduced: if \(b^m=0\), then \(b=b^{q^{rj}}=0\) as soon as \(q^{rj}\ge m\). If \(\mathfrak p\) is a prime ideal of \(B\), then \(B/\mathfrak p\) is a domain in which every element is a root of \(X^{q^r}-X\). So \(B/\mathfrak p\) is a finite field, and \(\mathfrak p\) is maximal. A reduced Noetherian ring in which every prime ideal is maximal is a finite product of fields. So \(B\) is the product of its residue fields.

The maximal ideals of \(B\) are the maximal ideals \(\mathfrak m\) of \(A\) that contain \(I\). These are the closed points \(x\in U\) such that every element of \(k(x)\) is a root of \(X^{q^r}-X\), that is, such that \(k(x)\) embeds into \(\mathbb F_{q^r}\). This happens if and only if \(\deg x\) divides \(r\). So \(\Phi_r\) is as described, and by Lemma 1.1

\[ \dim_k\Gamma(\Phi_r,\mathcal O_{\Phi_r})=\sum_{\deg x\,\mid\, r}\deg x=\sum_{d\mid r}d\,a_d=N_r. \]

Finally, \(\Phi_r\) is a finite set of reduced closed points of the regular curve \(C\). Near each of them its ideal is generated by a uniformizer. So \(\Phi_r\) is an effective Cartier divisor. ∎

The fixed-point scheme is reduced. This is the algebraic form of the statement that the graph of Frobenius meets the diagonal transversally, which holds because the differential of \(F\) is zero.

**Proposition 3.7 (intersection numbers of Frobenius correspondences).** Put \(N_0=2-2g\). For all \(r,s\ge 0\),

\[ d_1(\Gamma_r)=1,\qquad d_2(\Gamma_r)=q^r,\qquad (\Gamma_r\cdot\Gamma_s)=q^{\min(r,s)}\,N_{\lvert r-s\rvert}. \]

**Proof.** The morphism \(\gamma_r\colon C\to\Gamma_r\) is an isomorphism. So by (S2), \((L\cdot\Gamma_r)=\deg\gamma_r^{\ast}L\) for every invertible sheaf \(L\) on \(S\).

*The degrees.* For an invertible sheaf \(B\) on \(C\) we have \(\gamma_r^{\ast}p_1^{\ast}B=B\) and \(\gamma_r^{\ast}p_2^{\ast}B=(F^r)^{\ast}B\), which has degree \(q^r\deg B\) by (C3) and Lemma 3.5. So \(d_1(\Gamma_r)=1\) and \(d_2(\Gamma_r)=q^r\).

*Reduction to the diagonal.* Let \(r\le s\). By Lemma 3.2, \(\mathcal O_S(\Gamma_s)\cong(F^s\times\mathrm{id})^{\ast}\mathcal O_S(\Delta)\). The composite \((F^s\times\mathrm{id})\circ\gamma_r\) is \((F^s,F^r)=\tau\circ\gamma_{s-r}\circ F^r\), where \(\tau\) exchanges the two factors of \(S\). Since \(\tau^{-1}(\Delta)=\Delta\), Lemma 3.1 gives \(\tau^{\ast}\mathcal O_S(\Delta)\cong\mathcal O_S(\Delta)\). Hence

\[ \gamma_r^{\ast}\mathcal O_S(\Gamma_s)\cong(F^r)^{\ast}\,\gamma_{s-r}^{\ast}\mathcal O_S(\Delta), \]

and by (C3) and (S2)

\[ (\Gamma_r\cdot\Gamma_s)=q^r\,\deg\gamma_{s-r}^{\ast}\mathcal O_S(\Delta)=q^r\,(\Delta\cdot\Gamma_{s-r}). \]

*The diagonal and a Frobenius graph.* Let \(m\ge 1\). By (S2) applied to \(D=\Delta\), \((\Gamma_m\cdot\Delta)=\deg\delta^{\ast}\mathcal O_S(\Gamma_m)\). The generic point of \(\Delta\) does not lie on \(\Gamma_m\), because \(\Phi_m=\delta^{-1}(\Gamma_m)\) is not all of \(C\). So Lemma 3.1 applies and gives \(\delta^{\ast}\mathcal O_S(\Gamma_m)\cong\mathcal O_C(\Phi_m)\). By (C2) and Lemma 3.6 its degree is \(N_m\).

*The self-intersection of the diagonal.* By (S2), \((\Delta\cdot\Delta)=\deg\delta^{\ast}\mathcal O_S(\Delta)\). By (C4) the sheaf \(\delta^{\ast}\mathcal O_S(-\Delta)\) is the conormal sheaf of \(\Delta\), which is \(\Omega_{C/k}\), of degree \(2g-2\). By (C1), \((\Delta\cdot\Delta)=2-2g=N_0\). ∎

The convention \(N_0=2-2g\) is natural: the formula \(N_r=q^r+1-\sum_j\alpha_j^r\) of Corollary 2.5 gives \(2-2g\) at \(r=0\). The self-intersection of the diagonal is the Euler characteristic of the curve.

### 3.4 The trace formula

**Definition 3.8.** For \(L,M\in\operatorname{Pic}(S)\) put

\[ \langle L,M\rangle=d_1(L)\,d_2(M)+d_2(L)\,d_1(M)-(L\cdot M),\qquad \operatorname{Tr}(L)=\langle L,\Delta\rangle=d_1(L)+d_2(L)-(L\cdot\Delta). \]

The form \(\langle\ ,\ \rangle\) is symmetric and bilinear, with values in \(\mathbb Z\). [Milne 2015, Section 1] attributes it to Severi. The number \(\operatorname{Tr}(L)\) is the *trace* of the correspondence \(L\); this is the definition of [Connes–Consani–Marcolli 2009a, (2.25)].

The form vanishes on the correspondences that come from one factor. Indeed, by Lemma 3.4, \(\langle p_1^{\ast}A,M\rangle=0+\deg A\cdot d_1(M)-d_1(M)\deg A=0\), and in the same way \(\langle p_2^{\ast}A,M\rangle=0\). These are the *trivial correspondences*.

**Theorem 3.9 (trace formula).** Let \(S_m=\sum_{j=1}^{2g}\alpha_j^m\) for \(m\ge 0\). For all \(r,s\ge 0\),

\[ \langle\Gamma_r,\Gamma_s\rangle=q^{\min(r,s)}\,S_{\lvert r-s\rvert}. \]

In particular \(\operatorname{Tr}(\Gamma_r)=\sum_j\alpha_j^r\), and

\[ N_r=(\Gamma_r\cdot\Delta)=d_1(\Gamma_r)+d_2(\Gamma_r)-\operatorname{Tr}(\Gamma_r)\qquad(r\ge 1). \]

**Proof.** Let \(r\le s\). By Proposition 3.7,

\[ \langle\Gamma_r,\Gamma_s\rangle=q^s+q^r-q^rN_{s-r}=q^r\big(q^{s-r}+1-N_{s-r}\big). \]

For \(s>r\) this is \(q^rS_{s-r}\) by Corollary 2.5. For \(s=r\) it is \(q^r\cdot 2g=q^rS_0\). ∎

The number of fixed points of \(F^r\) is an intersection number on \(S\), and it is the sum of two degrees minus a trace. In [Manin 1995, (1.3)] the same count is written as \(N_r=\sum_{w=0}^{2}(-1)^w\operatorname{Tr}(F^r\mid H^w)\), with the \(\ell\)-adic cohomology groups \(H^w\) of \(C\). The degrees \(d_1(\Gamma_r)=1\) and \(d_2(\Gamma_r)=q^r\) take the place of the traces on \(H^0\) and \(H^2\), and \(\operatorname{Tr}(\Gamma_r)\) takes the place of the trace on \(H^1\). No cohomology theory is used in this lesson.

### 3.5 The inequality that follows from the Hodge index theorem

**Theorem 3.10 (inequality of Castelnuovo–Severi).** For every \(L\in\operatorname{Pic}(S)\),

\[ (L\cdot L)\le 2\,d_1(L)\,d_2(L),\qquad\text{that is,}\qquad\langle L,L\rangle\ge 0. \]

Equality holds if and only if \(L-d_2(L)V-d_1(L)W\) is numerically trivial.

**Proof.** Let \(H=V+W\). Then \((H\cdot H)=2(V\cdot W)=2>0\). Let \(L'=L-d_2(L)V-d_1(L)W\). Since \((V\cdot V)=(W\cdot W)=0\) and \((V\cdot W)=1\),

\[ (L'\cdot V)=d_1(L)-d_1(L)=0,\qquad (L'\cdot W)=d_2(L)-d_2(L)=0. \]

So \((L'\cdot H)=0\), and (S3) gives \((L'\cdot L')\le 0\). Expanding,

\[ (L'\cdot L')=(L\cdot L)-2d_2(L)(L\cdot V)-2d_1(L)(L\cdot W)+2d_1(L)d_2(L)(V\cdot W)=(L\cdot L)-2d_1(L)d_2(L). \]

This proves the inequality. If equality holds, then \((L'\cdot L')=0\) and \(L'\) is numerically trivial by (S3). Conversely, a numerically trivial \(L'\) has \((L'\cdot L')=0\). ∎

*Reference:* [Milne 2015, Theorem 1.5], where the inequality carries the names of Castelnuovo and Severi. Mattuck and Tate proved the inequality from the Riemann–Roch theorem for surfaces, and Grothendieck deduced it from the Hodge index theorem.

In [Connes–Consani–Marcolli 2009a, Section 2] correspondences are composed, the transpose of \(Z\) is written \(Z'\), and the positivity is stated in (2.35) there as \(\operatorname{Tr}(Z\star Z')>0\) for every correspondence \(Z\) whose class modulo linear equivalence and trivial correspondences is not zero. The number \(\operatorname{Tr}(Z\star Z')\) is our \(\langle Z,Z\rangle\) [Milne 2015, Section 1]. We do not use composition and do not prove this identity. For \(Z=m\Delta+n\Gamma_1\), Theorem 3.9 gives \(\langle Z,Z\rangle=2g\,m^2+2(1+q-N_1)mn+2gq\,n^2\), which is the value in [Connes–Consani–Marcolli 2009a, (2.48)].

*Reference:* [Connes–Consani–Marcolli 2009a, (2.43) and (2.46)] bound \(\operatorname{Tr}(Z\star Z')\) from below by \(2d'(Z)\) for an effective correspondence \(Z\) with \(d(Z)=g\); this fails for \(Z=\Delta+\Gamma_1+\Gamma_{\iota\circ F}\) on a curve of genus 3 with an involution \(\iota\) whose fixed-point scheme has degree 8, where \(d(Z)=3\), \(d'(Z)=1+2q\) and \(\langle Z,Z\rangle=6\) (Exercise 4), so we prove \(\langle Z,Z\rangle\ge 0\) from (S3).

**Corollary 3.11 (Cauchy–Schwarz).** For all \(L,M\in\operatorname{Pic}(S)\): \(\langle L,M\rangle^2\le\langle L,L\rangle\,\langle M,M\rangle\).

**Proof.** For integers \(m,n\), Theorem 3.10 gives

\[ 0\le\langle mL+nM,mL+nM\rangle=m^2\langle L,L\rangle+2mn\langle L,M\rangle+n^2\langle M,M\rangle. \]

A real binary quadratic form that is \(\ge 0\) at all integer points is \(\ge 0\) at all rational points by homogeneity, and at all real points by continuity. So its discriminant is \(\le 0\). ∎

### 3.6 The Riemann hypothesis

**Theorem 3.12 (Weil).** For all \(r\ge 1\),

\[ \lvert N_r-q^r-1\rvert\le 2g\,q^{r/2}. \]

Hence the Riemann hypothesis holds for \(C\): \(\lvert\alpha_j\rvert=\sqrt q\) for all \(j\), and every zero of \(\zeta_C\) has real part \(\tfrac12\).

*Reference:* due to Weil; for \(g=1\), to Hasse.

**Proof.** By Theorem 3.9, \(\langle\Delta,\Gamma_r\rangle=q^r+1-N_r\), \(\langle\Delta,\Delta\rangle=2g\) and \(\langle\Gamma_r,\Gamma_r\rangle=2g\,q^r\). Corollary 3.11 gives \((q^r+1-N_r)^2\le 4g^2q^r\). Now apply Proposition 2.8. ∎

The proof used the finiteness of \(\operatorname{Pic}^0(C)\) and the divisor of degree one (in Lemma 3.4), the functional equation (in Proposition 2.8), the count of fixed points (Lemma 3.6), and the sign of the intersection form (S3). The next theorem shows that the sign is exactly what is needed.

**Theorem 3.13 (the positivity is equivalent to the Riemann hypothesis).** For integers \(c_0,\dots,c_n\) put \(Z_c=\sum_rc_r\Gamma_r\in\operatorname{Pic}(S)\) and \(c(T)=\sum_rc_rT^r\).

1. \(\displaystyle\langle Z_c,Z_c\rangle=\sum_{r,s=0}^{n}c_rc_s\,q^{\min(r,s)}S_{\lvert r-s\rvert}=\sum_{j=1}^{2g}\lvert c(\alpha_j)\rvert^2\).
2. Conversely, let \(\beta_1,\dots,\beta_{2g}\) be nonzero complex numbers, stable with multiplicities under \(\beta\mapsto q/\beta\) and under complex conjugation, and let \(\tilde S_m=\sum_j\beta_j^m\). If \(\sum_{r,s}c_rc_s\,q^{\min(r,s)}\tilde S_{\lvert r-s\rvert}\ge 0\) for all \(n\) and all integers \(c_0,\dots,c_n\), then \(\lvert\beta_j\rvert=\sqrt q\) for all \(j\).

**Proof.** 1. The first equality is Theorem 3.9 and bilinearity. For the second, use \(\alpha_j\bar\alpha_j=q\) from Theorem 3.12. If \(r\le s\), then \(q^r\alpha_j^{s-r}=\bar\alpha_j^{\,r}\alpha_j^{s}\). If \(r>s\), then \(q^s\alpha_j^{r-s}=\alpha_j^{r}\bar\alpha_j^{\,s}\), and the sum of these terms over \(j\) equals the sum of \(\bar\alpha_j^{\,r}\alpha_j^{s}\) over \(j\), because the family \((\alpha_j)\) is stable under conjugation. So the double sum equals \(\sum_j\sum_{r,s}c_rc_s\bar\alpha_j^{\,r}\alpha_j^{s}=\sum_j\lvert c(\alpha_j)\rvert^2\).

2. Take \(c_0=m\), \(c_r=n\) and all other coefficients zero, with \(r\ge 1\). The hypothesis gives \(2g\,m^2+2mn\,\tilde S_r+2g\,q^r\,n^2\ge 0\) for all integers \(m,n\). The number \(\tilde S_r\) is real. As in Corollary 3.11 it follows that \(\tilde S_r^2\le 4g^2q^r\). Lemma 2.7 gives \(\lvert\beta_j\rvert\le\sqrt q\), and the stability under \(\beta\mapsto q/\beta\) gives equality. ∎

So the inequality \(\langle Z,Z\rangle\ge 0\), restricted to the Frobenius correspondences, is a statement about the numbers \(N_r\) alone, and it is equivalent to the Riemann hypothesis for \(C\). The surface and the Hodge index theorem are what proves it.

**Corollary 3.14 (the characteristic polynomial of Frobenius).** Write \(T^{2g}P(1/T)=\prod_j(T-\alpha_j)=\sum_{r=0}^{2g}b_rT^r\). Then the correspondence

\[ \sum_{r=0}^{2g}b_r\Gamma_r-h\,q^g\,V-h\,W \]

is numerically trivial.

**Proof.** The polynomial \(c(T)=\sum_rb_rT^r\) vanishes at every \(\alpha_j\). By Theorem 3.13, \(\langle Z_b,Z_b\rangle=0\). By Proposition 3.7, \(d_1(Z_b)=\sum_rb_r=\prod_j(1-\alpha_j)=P(1)=h\) and \(d_2(Z_b)=\sum_rb_rq^r=q^{2g}P(1/q)=q^gh\). Now apply the case of equality in Theorem 3.10. ∎

This is the form that the Cayley–Hamilton theorem for the Frobenius map takes on the surface.

**Example 3.15 (the projective line).** Let \(g=0\). Then \(S_m=0\) for all \(m\), and \(\langle\Gamma_r,\Gamma_s\rangle=0\). By the case of equality in Theorem 3.10, \(\Gamma_r-q^rV-W\) is numerically trivial. This agrees with Proposition 3.7: \((q^rV+W)\cdot(q^sV+W)=q^r+q^s=q^{\min(r,s)}(q^{\lvert r-s\rvert}+1)\) for \(r\ne s\), and \(2q^r=q^rN_0\) for \(r=s\). In genus zero the form \(\langle\ ,\ \rangle\) carries no information.

**Example 3.16 (the curve of Example 2.10).** For \(E\) over \(\mathbb F_2\) we have \(g=1\), \(\alpha=-1\pm i\), and \(S_0=2\), \(S_1=-2\), \(S_2=0\). The matrix of \(\langle\ ,\ \rangle\) on \(\Delta,\Gamma_1,\Gamma_2\) has the rows

\[ (2,\,-2,\,0),\qquad(-2,\,4,\,-4),\qquad(0,\,-4,\,8). \]

It is positive semidefinite by Theorem 3.13. Its leading minors are \(2\), \(4\) and \(0\), so its rank is \(2=2g\). Its kernel is spanned by \((2,2,1)\), which is the vector of coefficients of \(T^2P(1/T)=T^2+2T+2\). This is Corollary 3.14: the correspondence \(\Gamma_2+2\Gamma_1+2\Delta-10V-5W\) is numerically trivial. Here \(h=5\) and \(d_2=2\cdot 1+2\cdot 2+1\cdot 4=10\).

## 4. The dictionary between a curve and the integers

### 4.1 Places and the product formula

An *absolute value* on a field \(L\) is a map \(a\mapsto\lVert a\rVert\) from \(L\) to the real numbers \(\ge 0\) such that \(\lVert a\rVert=0\) only for \(a=0\), \(\lVert ab\rVert=\lVert a\rVert\lVert b\rVert\), and \(\lVert a+b\rVert\le\lVert a\rVert+\lVert b\rVert\). It is *trivial* if \(\lVert a\rVert=1\) for all \(a\ne 0\). Two absolute values are *equivalent* if one is a power of the other with an exponent \(t>0\). A *place* of \(L\) is an equivalence class of nontrivial absolute values.

On \(\mathbb Q\) there is the usual absolute value \(\lvert a\rvert_\infty\), and for every prime \(p\) the absolute value \(\lvert a\rvert_p=p^{-v_p(a)}\), where \(v_p(a)\) is the exponent of \(p\) in \(a\). On the function field \(K\) of the curve \(C\) every closed point \(x\) gives the absolute value \(\lvert f\rvert_x=\mathrm Nx^{-v_x(f)}\).

**Theorem 4.1 (Ostrowski).** Every nontrivial absolute value on \(\mathbb Q\) is equivalent to \(\lvert\ \rvert_\infty\) or to \(\lvert\ \rvert_p\) for exactly one prime \(p\). So the places of \(\mathbb Q\) are the primes and \(\infty\).

**Proof.** Let \(\lVert\ \rVert\) be a nontrivial absolute value on \(\mathbb Q\). The triangle inequality gives \(\lVert n\rVert\le n\) for every positive integer \(n\).

*Case 1:* \(\lVert n\rVert\le 1\) for all positive integers \(n\). For \(a,b\in\mathbb Q\) and \(m\ge 1\) the binomial formula gives \(\lVert a+b\rVert^m\le(m+1)\max(\lVert a\rVert,\lVert b\rVert)^m\). Taking \(m\)-th roots and letting \(m\to\infty\) gives \(\lVert a+b\rVert\le\max(\lVert a\rVert,\lVert b\rVert)\). So the set of integers \(n\) with \(\lVert n\rVert<1\) is an ideal of \(\mathbb Z\). It is a prime ideal, and it is not zero because the absolute value is nontrivial. So it is \(p\mathbb Z\) for a prime \(p\), and \(\lVert n\rVert=1\) for \(n\) prime to \(p\). Hence \(\lVert a\rVert=\lVert p\rVert^{v_p(a)}\), which is a power of \(\lvert a\rvert_p\).

*Case 2:* \(\lVert n_0\rVert>1\) for some integer \(n_0>1\). Let \(m,n>1\) be integers and \(j\ge 1\). Write \(m^j\) in base \(n\): \(m^j=\sum_{i=0}^{e}a_in^i\) with \(0\le a_i<n\) and \(e\le j\log m/\log n\). Then

\[ \lVert m\rVert^j\le\sum_{i=0}^{e}\lVert a_i\rVert\,\lVert n\rVert^i\le n\,(e+1)\,\max(1,\lVert n\rVert)^{e}\le n\Big(1+j\frac{\log m}{\log n}\Big)\max(1,\lVert n\rVert)^{j\log m/\log n}. \]

Taking \(j\)-th roots and letting \(j\to\infty\) gives \(\lVert m\rVert\le\max(1,\lVert n\rVert)^{\log m/\log n}\). With \(m=n_0\) this shows \(\lVert n\rVert>1\) for every \(n>1\). Then \(\lVert m\rVert^{1/\log m}\le\lVert n\rVert^{1/\log n}\) for all \(m,n>1\), and by symmetry equality holds. So there is \(t>0\) with \(\lVert n\rVert=n^t\) for all \(n\ge 1\), and \(\lVert a\rVert=\lvert a\rvert_\infty^t\) on \(\mathbb Q\).

Finally the listed absolute values are pairwise inequivalent: \(\lvert p\rvert_p<1\), while \(\lvert p\rvert_\ell=1\) for a prime \(\ell\ne p\) and \(\lvert p\rvert_\infty>1\). ∎

**Proposition 4.2 (places of a function field).** The absolute values \(\lvert\ \rvert_x\), for \(x\) a closed point of \(C\), represent all places of \(K\), each exactly once.

**Proof.** Let \(\lVert\ \rVert\) be a nontrivial absolute value on \(K\). Every nonzero element of \(k\) is a root of unity, so it has absolute value 1. In particular \(\lVert n\cdot 1\rVert\le 1\) for all integers \(n\), and the argument of Case 1 above gives \(\lVert f+g\rVert\le\max(\lVert f\rVert,\lVert g\rVert)\). So \(R=\{f: \lVert f\rVert\le 1\}\) is a subring of \(K\) that contains \(k\), with the maximal ideal \(\mathfrak m_R=\{f: \lVert f\rVert<1\}\ne 0\). If \(f\notin R\), then \(1/f\in\mathfrak m_R\). So \(R\) is a valuation ring of \(K\), and \(R\ne K\).

By the valuative criterion of properness [Stacks, Tag [0BX5](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-characterize-proper)], the morphism \(\operatorname{Spec}K\to C\) extends to a morphism \(\operatorname{Spec}R\to C\). Let \(x\) be the image of the closed point. Then \(\mathcal O_{C,x}\subset R\) and \(\mathfrak m_R\cap\mathcal O_{C,x}\) is the maximal ideal \(\mathfrak m_x\). The point \(x\) is closed, since otherwise \(\mathcal O_{C,x}=K\subset R\). So \(\mathcal O_{C,x}\) is a discrete valuation ring. If \(f\in R\) and \(f\notin\mathcal O_{C,x}\), then \(1/f\in\mathfrak m_x\subset\mathfrak m_R\), which contradicts \(f\in R\). Hence \(R=\mathcal O_{C,x}\). Let \(\pi\) be a uniformizer at \(x\). Every \(f\in K^{\times}\) is \(\pi^{v_x(f)}\) times an invertible element of \(R\), and the invertible elements of \(R\) have absolute value 1. So \(\lVert f\rVert=\lVert\pi\rVert^{v_x(f)}\), which is a power of \(\lvert f\rvert_x\). Different closed points have different local rings, so they give inequivalent absolute values. ∎

**Proposition 4.3 (product formula).**

1. For every \(f\in K^{\times}\): \(\prod_x\lvert f\rvert_x=1\).
2. For every \(a\in\mathbb Q^{\times}\): \(\lvert a\rvert_\infty\prod_p\lvert a\rvert_p=1\).
3. Put \(v_\infty(a)=-\log\lvert a\rvert_\infty\). Then \(\sum_pv_p(a)\log p+v_\infty(a)=0\) for all \(a\in\mathbb Q^{\times}\). Up to a common factor, the weights \(\log p\) and \(1\) are the only real numbers \(w_p\), \(w_\infty\) with \(\sum_pv_p(a)\,w_p+v_\infty(a)\,w_\infty=0\) for all \(a\).

**Proof.** 1. The product is \(q^{-\deg\operatorname{div}f}\), which is 1 by (R1). 2. Write \(a=\pm\prod_pp^{v_p(a)}\). 3. Take the logarithm in part 2. For the uniqueness take \(a=p\): this gives \(w_p=w_\infty\log p\). ∎

So a closed point \(x\) of a curve corresponds to a prime \(p\), and the number \(\log\mathrm Nx=\deg x\cdot\log q\) corresponds to \(\log p\). On the same scale the place \(\infty\) has degree 1. This normalization, \(\deg[p]=\log p\) and \(\deg[\infty]=1\), is the one of [Smirnov 1992, Section 2.1]; see also [Jarra 2023b, Introduction].

**Proposition 4.4 (constants).**

1. The set of \(f\in K\) with \(\lvert f\rvert_x\le 1\) for all closed points \(x\) is the field \(k=\mathbb F_q\).
2. The set of \(a\in\mathbb Q\) with \(\lvert a\rvert_v\le 1\) for all places \(v\) is \(\{0,1,-1\}\). It is closed under multiplication and not under addition.
3. The set of \(a\in\mathbb Q\) with \(\lvert a\rvert_p\le 1\) for all primes \(p\) is \(\mathbb Z\). The set of \(a\in\mathbb Q\) with \(\lvert a\rvert_\infty\le 1\) is closed under multiplication and not under addition.

**Proof.** 1. Such an \(f\) has no pole, so \(f\in H^0(C,\mathcal O_C)=k\). 3. Write \(a=m/n\) in lowest terms. If a prime \(p\) divides \(n\), then \(\lvert a\rvert_p>1\). The second set is \(\mathbb Q\cap[-1,1]\), which contains 1 and not \(1+1\). 2. By part 3 such an \(a\) is an integer with \(\lvert a\rvert_\infty\le 1\). And \(1+1=2\) is not in the set. ∎

In the conventions of this course, \(\{0,1,-1\}=\{0\}\cup\mu_2\) is the monoid \(\mathbb F_{1^2}\). So the constants of \(\mathbb Q\) form a monoid and not a field. The ring \(\mathbb Z\) corresponds to the ring of functions on a curve with one point removed, that is, to an affine curve. The place \(\infty\) is the missing point. Its local ring would be \(\mathbb Q\cap[-1,1]\), and this is not a ring.

### 4.2 The completed zeta function

The Riemann zeta function is \(\zeta(s)=\sum_{n\ge 1}n^{-s}=\prod_p(1-p^{-s})^{-1}\) for \(\operatorname{Re}s>1\). The factor at \(p\) has the same form as the factor \((1-\mathrm Nx^{-s})^{-1}\) of \(\zeta_C\) at a closed point. The *completed zeta function* is

\[ \zeta_{\mathbb Q}(s)=\pi^{-s/2}\,\Gamma\Big(\frac s2\Big)\,\zeta(s). \]

The factor \(\pi^{-s/2}\Gamma(s/2)\) is the factor of the place \(\infty\). The zeros of \(\zeta_{\mathbb Q}\) are the *nontrivial zeros* of \(\zeta\). We denote them by \(\rho\) and count them with multiplicity. We use two facts.

**(Z1)** The function \(\zeta_{\mathbb Q}\) extends to a meromorphic function on the complex plane. It is holomorphic except for simple poles at \(s=0\) and \(s=1\), with residues \(-1\) and \(1\). It satisfies \(\zeta_{\mathbb Q}(1-s)=\zeta_{\mathbb Q}(s)\). 

*Remark.* The two poles belong to \(\zeta_{\mathbb Q}\), not to \(\zeta\): near \(s=0\) we have \(\Gamma(s/2)=2/s+O(1)\), so the residue \(-1\) of \(\zeta_{\mathbb Q}\) at \(0\) gives \(\zeta(0)=-\tfrac12\).

**(Z2)** Let \(\xi(s)=\tfrac12s(s-1)\zeta_{\mathbb Q}(s)\). This is an entire function whose zeros are the \(\rho\). They satisfy \(\sum_\rho\lvert\rho\rvert^{-1-\varepsilon}<\infty\) for every \(\varepsilon>0\). For every \(s\) that is not a zero,

\[ \frac{\xi'(s)}{\xi(s)}=\lim_{T\to\infty}\ \sum_{\lvert\operatorname{Im}\rho\rvert<T}\frac{1}{s-\rho}. \]



Some consequences are immediate. By (Z1), \(s(s-1)\zeta_{\mathbb Q}(s)\) tends to 1 as \(s\to 0\), so \(\xi(0)=\tfrac12\) and \(\rho\ne 0\). The Euler product shows that \(\zeta_{\mathbb Q}\) has no zero with \(\operatorname{Re}s>1\), and then the functional equation shows that it has none with \(\operatorname{Re}s<0\). So \(0\le\operatorname{Re}\rho\le 1\). The set of zeros is stable under \(\rho\mapsto 1-\rho\) by (Z1), and under \(\rho\mapsto\bar\rho\) because \(\zeta_{\mathbb Q}\) is real on the real axis. Hence it is stable under \(\rho\mapsto 1-\bar\rho\), the reflection in the line \(\operatorname{Re}s=\tfrac12\). The *Riemann hypothesis* is the statement \(\operatorname{Re}\rho=\tfrac12\) for all \(\rho\).

**Proposition 4.5 (the product form).** The limit

\[ \Pi(s)=\lim_{T\to\infty}\ \prod_{\lvert\operatorname{Im}\rho\rvert<T}\Big(1-\frac{s}{\rho}\Big) \]

exists locally uniformly in \(s\). It is an entire function with the zeros \(\rho\), and

\[ \zeta_{\mathbb Q}(s)=\frac{\Pi(s)}{s(s-1)}. \]

**Proof.** A nonzero entire function has finitely many zeros in a bounded set, so there are finitely many real zeros. For a zero \(\rho\) with \(\operatorname{Im}\rho>0\) the conjugate \(\bar\rho\) is a zero of the same multiplicity, and

\[ \Big(1-\frac s\rho\Big)\Big(1-\frac s{\bar\rho}\Big)=1-\frac{2s\operatorname{Re}\rho}{\lvert\rho\rvert^2}+\frac{s^2}{\lvert\rho\rvert^2}. \]

Since \(0\le\operatorname{Re}\rho\le 1\) and \(\sum\lvert\rho\rvert^{-2}<\infty\), the product over these pairs converges absolutely and locally uniformly. So \(\Pi\) is entire, with the zeros \(\rho\). Its logarithmic derivative is obtained term by term, so it equals \(\xi'/\xi\) by (Z2). Hence \(\xi/\Pi\) is an entire function without zeros and with logarithmic derivative zero. It is constant, equal to \(\xi(0)/\Pi(0)=\tfrac12\). So \(\zeta_{\mathbb Q}(s)=2\xi(s)/(s(s-1))=\Pi(s)/(s(s-1))\). ∎

Compare this with Corollary 2.5:

\[ \zeta_C(s)=\frac{P(q^{-s})}{(1-q^{-s})(1-q^{1-s})},\qquad\zeta_{\mathbb Q}(s)=\frac{\Pi(s)}{s\,(s-1)}. \]

In both cases the zeta function is the zeta function of a projective line, times an entire function that carries the zeros. For the curve the projective line is the one over \(\mathbb F_q\) (Example 2.9). For \(\mathbb Q\) the factor \(1/(s(s-1))\) is the zeta function of the projective line over \(\mathbb F_1\), in the convention of [Connes–Consani 2010, Section 2]; see Example 5.2.

**Remark 4.6 (the determinant form).** A reference for this remark is [Manin 1995, Section 1.1]. For the curve, formula (1.4) there reads \(\zeta_C(s)=\prod_{w=0}^{2}\det(1-Fq^{-s}\mid H^w)^{(-1)^{w-1}}\): the three factors are characteristic polynomials of the Frobenius map on the three \(\ell\)-adic cohomology groups, and the factor of weight \(w\) has its zeros on the line \(\operatorname{Re}s=w/2\). For the integers, formula (1.5) there reads

\[ 2^{-1/2}\,\zeta_{\mathbb Q}(s)=\frac{\prod_\rho\frac{s-\rho}{2\pi}}{\frac{s}{2\pi}\cdot\frac{s-1}{2\pi}}\ \overset{?}{=}\ \prod_{\omega=0}^{2}\operatorname{DET}\Big(\frac{s-\Phi}{2\pi}\ \Big\vert\ H^{\omega}\Big)^{(-1)^{\omega-1}}. \]

The product over \(\rho\) and the symbol DET are zeta-regularized: by (1.6) there, the regularized product of numbers \(\lambda_i\) is \(\exp(-\tfrac{d}{dz}\sum_i\lambda_i^{-z})\) at \(z=0\). The two equalities have a different status, and [Manin 1995] says so. The first one is a theorem for \(\operatorname{Re}s>1\): it is [Deninger 1992, Theorem 3.3], proved in Section 4 there from an explicit formula. By [Deninger 1992, Remark 3.4(1)], Soulé extended it to every \(s\) that is not of the form \(\rho-\lambda\) with \(\lambda\ge0\), and [Manin 1995, Section 2.11] calls the formula due to Deninger and Soulé. The second one is not a theorem. It postulates a cohomology theory \(H^{\omega}\) for \(\overline{\operatorname{Spec}\mathbb Z}\) with an operator \(\Phi\). [Deninger 1992, Section 3] states it as a speculation, in a section with the title "An arithmetic site?", and [Manin 1995, Section 1.3] calls this theory unknown. For the formula, [Manin 1995, Section 1.1] cites work of Deninger, which writes the \(\Gamma\)-factors of motives at the infinite places as regularized determinants. Comparing the two sides, the factors \(s/2\pi\) and \((s-1)/2\pi\) would come from \(H^0\) and \(H^2\), and the zeros \(\rho\) would be the eigenvalues of \(\Phi\) on an infinite-dimensional \(H^1\). In [Manin 1995, Section 1.6] the same decomposition is written as \(\mathbb T^0\oplus\mathbb H^1\oplus\mathbb T\), where the absolute point \(\mathbb T^0\) has the zeta function \(s/2\pi\) and the absolute Tate motive \(\mathbb T\) has the zeta function \((s-1)/2\pi\). In [Manin 1995] the zeta function of a motive is a determinant, and these two functions are the two factors in the denominator of the formula above. Up to the factor \(2\pi\) they are the reciprocals of the functions \(1/s\) and \(1/(s-1)\) that Example 5.2 attaches to a point and to the affine line. Proposition 4.5 is the elementary counterpart of the first equality, with a convergent product in place of the regularized one.

**Remark 4.7 (the genus is infinite).** The function \(\zeta_C\) has \(2g\) zeros in each period, that is, on average \(g\log q/\pi\) zeros in a strip of height 1. The number of zeros \(\rho\) with \(0<\operatorname{Im}\rho<T\) is \(\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+O(\log T)\) ([The Riemann–von Mangoldt formula, Theorem 2.1](course:NT-ZETA/NT-ZETA-10)). So the average number of zeros in a strip of height 1 near height \(T\) grows like \(\frac{1}{2\pi}\log T\). In this sense a curve \(\overline{\operatorname{Spec}\mathbb Z}\) has infinite genus. The polynomial \(P\) of degree \(2g\) is replaced by the entire function \(\Pi\).

### 4.3 The dictionary

| | Curve \(C\) over \(\mathbb F_q\) | The integers |
|---|---|---|
| Field of functions | \(K\) | \(\mathbb Q\) |
| Places | closed points \(x\) (Proposition 4.2) | primes \(p\), and \(\infty\) (Theorem 4.1) |
| Degree of a place | \(\log\mathrm Nx=\deg x\cdot\log q\) | \(\log p\), and 1 for \(\infty\) |
| Product formula | \(\deg\operatorname{div}f=0\) | Proposition 4.3 |
| Constants | the field \(\mathbb F_q\) | the monoid \(\{0,1,-1\}\) |
| Local factor | \((1-\mathrm Nx^{-s})^{-1}\) | \((1-p^{-s})^{-1}\), and \(\pi^{-s/2}\Gamma(s/2)\) at \(\infty\) |
| Zeta function | \(\zeta_C(s)\) | \(\zeta_{\mathbb Q}(s)\) |
| Sum over effective divisors | \(\zeta_C(s)=\sum_{D\ge 0}\mathrm ND^{-s}\) | [Manin 1995, Section 1.3] records that no analogue was known |
| Poles | simple, at \(s=0\) and \(s=1\) up to periods | simple, at \(s=0\) and \(s=1\) |
| Functional equation | \(q^{(g-1)s}\zeta_C(s)\) is invariant under \(s\mapsto 1-s\) | \(\zeta_{\mathbb Q}(s)\) is invariant under \(s\mapsto 1-s\) |
| Where it comes from | the Riemann–Roch theorem (Theorem 2.4) | Poisson summation for a theta function (*Poisson summation, theta, and the functional equation*) |
| Product form | \(P(q^{-s})/((1-q^{-s})(1-q^{1-s}))\) | \(\Pi(s)/(s(s-1))\) (Proposition 4.5) |
| Zeros | \(2g\) in each period | infinitely many (Remark 4.7) |
| Point counts | \(N_r=q^r+1-\sum_j\alpha_j^r\) | \(N(u)=u+1-\sum_\rho u^\rho\) (Theorem 5.10) |
| Explicit formula | Proposition 4.8 | Theorem 5.10 and Corollary 5.13 |
| Riemann hypothesis | Theorem 3.12 | open |
| Tools of the proof | \(C\times C\), the \(\Gamma_r\), and (S3) | see Section 6 |

### 4.4 The explicit formula of a curve

**Proposition 4.8.** Let \(f\) be a complex function on the set \(\{q,q^2,q^3,\dots\}\) with \(f(q^r)=O(q^{-\sigma r})\) for some \(\sigma>1\). For a complex number \(z\) with \(\operatorname{Re}z\le 1\) put \(\widehat f(z)=\log q\sum_{r\ge 1}f(q^r)\,q^{rz}\). Choose \(\rho_1,\dots,\rho_{2g}\) with \(q^{\rho_j}=\alpha_j\). Then

\[ \sum_x\ \sum_{m\ge 1}\log(\mathrm Nx)\,f(\mathrm Nx^m)=\widehat f(1)+\widehat f(0)-\sum_{j=1}^{2g}\widehat f(\rho_j), \]

where \(x\) runs over the closed points of \(C\).

**Proof.** A closed point \(x\) and an integer \(m\) with \(m\deg x=r\) contribute \(\deg x\cdot\log q\cdot f(q^r)\). By Lemma 1.1 the left side is \(\log q\sum_{r\ge 1}N_rf(q^r)\). Now insert \(N_r=q^r+1-\sum_jq^{r\rho_j}\) from Corollary 2.5. All sums converge absolutely, because \(\lvert\alpha_j\rvert\le q\). ∎

The left side runs over the places of \(K\). The right side runs over the poles \(1,0\) and the zeros \(\rho_j\) of \(\zeta_C\) in one period, and \(\operatorname{Re}\rho_j=\tfrac12\) by Theorem 3.12. Theorem 5.10 is the same formula for the integers.

## 5. The counting function of the compactification of \(\operatorname{Spec}\mathbb Z\)

A reference for this section is [Connes–Consani 2010, Section 2].

### 5.1 From counting functions to zeta functions

For the curve \(C\), Definition 2.1 gives \(-\zeta_C'(s)/\zeta_C(s)=\log q\sum_{r\ge 1}N_rq^{-rs}\). So the logarithmic derivative of the zeta function is a transform of the point counts. This relation still makes sense when the counting function is defined for all real numbers \(u\ge 1\), and then one can let \(q\) tend to 1.

**Proposition 5.1 (the integral formula).** Let \(N\colon[1,\infty)\to\mathbb C\) be Riemann integrable on every bounded interval, with \(\lvert N(u)\rvert\le A\,u^{a}\) for constants \(A\) and \(a\ge 0\). For a real number \(q>1\) and \(\operatorname{Re}s>a\) put

\[ F(q,s)=\log q\,\sum_{r\ge 1}N(q^r)\,q^{-rs}. \]

Then

\[ \lim_{q\to 1}F(q,s)=\int_1^\infty N(u)\,u^{-s}\,d^{\times}u, \]

uniformly for \(s\) in compact subsets of the half-plane \(\operatorname{Re}s>a\).

*Reference:* [Connes–Consani 2010, Lemma 2.1], for continuous \(N\).

**Proof.** Put \(\eta=\log q\) and \(g(t)=N(e^t)\) for \(t\ge 0\). Then \(F(q,s)=\eta\sum_{r\ge 1}g(r\eta)e^{-sr\eta}\), and the integral is \(\int_0^\infty g(t)e^{-st}dt\). Let \(K\) be a compact subset of the half-plane. There are \(\delta>0\) and \(b\) with \(\operatorname{Re}s\ge a+\delta\) and \(\lvert s\rvert\le b\) for \(s\in K\). Fix \(\tau>1\) and let \(\eta\le 1\).

*Tails.* Since \(\lvert g(t)e^{-st}\rvert\le Ae^{-\delta t}\) and \(e^{-\delta t}\) decreases,

\[ \Big\lvert\eta\sum_{r\eta>\tau}g(r\eta)e^{-sr\eta}\Big\rvert\le A\int_{\tau-\eta}^\infty e^{-\delta t}dt\le\frac{A}{\delta}e^{-\delta(\tau-1)},\qquad\Big\lvert\int_\tau^\infty g(t)e^{-st}dt\Big\rvert\le\frac A\delta e^{-\delta\tau}. \]

*The bounded part.* Let \(n\) be the largest integer with \(n\eta\le\tau\). For \((r-1)\eta\le t\le r\eta\) we have \(\lvert e^{-sr\eta}-e^{-st}\rvert\le b\,\eta\), and \(\lvert e^{-st}\rvert\le 1\). So

\[ \Big\lvert\eta\sum_{r=1}^{n}g(r\eta)e^{-sr\eta}-\int_0^{n\eta}g(t)e^{-st}dt\Big\rvert\le\sum_{r=1}^{n}\int_{(r-1)\eta}^{r\eta}\lvert g(r\eta)-g(t)\rvert\,dt+b\,\eta\,\tau\,\sup_{[0,\tau]}\lvert g\rvert. \]

The first term on the right is at most the difference between the upper and lower Darboux sums of the real and imaginary parts of \(g\) for the subdivision of \([0,\tau]\) with step \(\eta\). It tends to 0 with \(\eta\), because \(g\) is Riemann integrable on \([0,\tau]\). The remaining piece \(\int_{n\eta}^{\tau}\) is at most \(\eta\sup_{[0,\tau]}\lvert g\rvert\). None of these bounds depends on \(s\in K\). Let first \(\eta\to 0\) and then \(\tau\to\infty\). ∎

Let \(Z_N(q,T)=\exp(\sum_{r\ge 1}N(q^r)T^r/r)\), as in Definition 2.1. Then \(F(q,s)=-\partial_s\log Z_N(q,q^{-s})\). Suppose that for some constant \(\chi\) the functions \((q-1)^{\chi}Z_N(q,q^{-s})\) converge, as \(q\to 1\), to a function \(\zeta_N(s)\) without zeros, locally uniformly on the half-plane. Then Proposition 5.1 gives

\[ -\frac{\zeta_N'(s)}{\zeta_N(s)}=\int_1^\infty N(u)\,u^{-s}\,d^{\times}u. \]

**Example 5.2 (polynomial counting functions).** Let \(N(u)=\sum_{j=0}^{n}a_ju^j\) with integers \(a_j\). Then \(Z_N(q,T)=\prod_j(1-q^jT)^{-a_j}\), and with \(\chi=N(1)=\sum_ja_j\)

\[ (q-1)^{N(1)}\,Z_N(q,q^{-s})=\prod_{j=0}^{n}\Big(\frac{1-q^{j-s}}{q-1}\Big)^{-a_j}\ \longrightarrow\ \zeta_N(s)=\prod_{j=0}^{n}(s-j)^{-a_j}\qquad(q\to 1), \]

because \((1-q^{j-s})/(q-1)\to s-j\). This limit is the zeta function over \(\mathbb F_1\) in the convention of [Connes–Consani 2010, Section 2], and this lesson uses this convention throughout. [Soulé 2004, Section 6, Lemme 1] uses the reciprocal convention, \(\lim_{q\to 1}Z_N(q,q^{-s})^{-1}(q-1)^{-N(1)}=\prod_j(s-j)^{a_j}=1/\zeta_N(s)\). So a formula in one convention becomes a formula in the other by taking the reciprocal. The lesson *Varieties over the field with one element after Soulé and Connes–Consani* treats both. The function \(\zeta_N\) of this lesson satisfies \(-\zeta_N'(s)/\zeta_N(s)=\sum_ja_j/(s-j)=\int_1^\infty N(u)u^{-s}d^{\times}u\) for \(\operatorname{Re}s>n\), as it must by Proposition 5.1. Three cases: a point has \(N=1\) and \(\zeta_N(s)=1/s\). The affine line has \(N=u\) and \(\zeta_N(s)=1/(s-1)\). The projective line has \(N=u+1\) and

\[ \zeta_N(s)=\frac{1}{s(s-1)}. \]

This is the factor in front of \(\Pi(s)\) in Proposition 4.5.

**Proposition 5.3 (the counting measure of a curve).** For the curve \(C\) over \(\mathbb F_q\) and \(\operatorname{Re}s>1\),

\[ -\frac{\zeta_C'(s)}{\zeta_C(s)}=\int_1^\infty u^{-s}\,d\mu_C(u),\qquad\mu_C=\sum_{r\ge 1}N_r\log q\cdot\delta_{q^r}=\sum_x\sum_{m\ge 1}\log(\mathrm Nx)\cdot\delta_{\mathrm Nx^m}, \]

where \(\delta_a\) is the point mass 1 at \(a\) and \(x\) runs over the closed points.

**Proof.** Differentiate \(\log\zeta_C(s)=\sum_rN_rq^{-rs}/r\). The second expression for \(\mu_C\) follows from Lemma 1.1. ∎

So for a curve the transform of \(-\zeta_C'/\zeta_C\) is a positive measure. Each closed point \(x\) contributes the mass \(\log\mathrm Nx\) at every power of its norm.

**The question.** [Connes–Consani 2010, Section 1], following [Manin 1995, Sections 1.1 and 1.6], asks for a curve \(\overline{\operatorname{Spec}\mathbb Z}\) over \(\mathbb F_1\) whose zeta function is \(\zeta_{\mathbb Q}\). No such curve is defined in this lesson. But Propositions 5.1 and 5.3 say what its counting function would be: a function, or a generalized function, \(N\) on \([1,\infty)\) with

\[ \int_1^\infty N(u)\,u^{-s}\,d^{\times}u=-\frac{\zeta_{\mathbb Q}'(s)}{\zeta_{\mathbb Q}(s)}\qquad(\operatorname{Re}s>1). \tag{5.1} \]

A constant factor in front of \(\zeta_{\mathbb Q}\), such as the factor \(2^{-1/2}\) of Remark 4.6, does not change (5.1).

### 5.2 Test functions and distributions on the half-line

Let \(\theta\) be the operator \(u\,\frac{d}{du}\).

**Definition 5.4.**

1. \(\mathcal T\) is the space of twice continuously differentiable functions \(f\colon[1,\infty)\to\mathbb C\) such that \(f\), \(\theta f\) and \(\theta^2f\) are \(O(u^{-\sigma})\) for some \(\sigma>1\), which may depend on \(f\).
2. For \(f\in\mathcal T\) and a complex number \(z\) with \(\operatorname{Re}z\le 1\), put \(\widehat f(z)=\int_1^\infty f(u)\,u^z\,d^{\times}u\).
3. In this lesson, a *distribution on* \([1,\infty)\) is a linear map \(L\colon\mathcal T\to\mathbb C\) of the form

\[ L(f)=\int_1^\infty G(u)\,(\theta^2f)(u)\,d^{\times}u, \]

where \(G\colon[1,\infty)\to\mathbb C\) is continuous and \(G(u)=O(u\,(1+\log u)^m)\) for some \(m\).

4. A distribution \(L\) is *positive on* \((1,\infty)\) if \(L(f)\ge 0\) for every \(f\in\mathcal T\) with \(f\ge 0\) that vanishes near \(u=1\). It is *positive on* \([1,\infty)\) if \(L(f)\ge 0\) for every \(f\in\mathcal T\) with \(f\ge 0\).

The functions \(u^{-s}\) with \(\operatorname{Re}s>1\) lie in \(\mathcal T\), and \(\theta^2u^{-s}=s^2u^{-s}\).

**Lemma 5.5.** Let \(f\in\mathcal T\).

1. For \(a\ge 1\): \(f(a)=\int_a^\infty\log(u/a)\,(\theta^2f)(u)\,d^{\times}u\).
2. For \(\operatorname{Re}z\le 1\): \(\widehat f(z)=\int_1^\infty G_z(u)\,(\theta^2f)(u)\,d^{\times}u\), where \(G_z(u)=(u^z-1-z\log u)/z^2\) for \(z\ne 0\) and \(G_0(u)=\tfrac12(\log u)^2\).

So \(f\mapsto f(a)\) and \(f\mapsto\widehat f(z)\) are distributions on \([1,\infty)\).

**Proof.** Put \(u=e^t\) and \(g(t)=f(e^t)\). Then \(\theta f\) and \(\theta^2f\) become \(g'\) and \(g''\), the measure \(d^{\times}u\) becomes \(dt\), and \(g,g',g''\) are \(O(e^{-\sigma t})\). For part 1, with \(t_0=\log a\),

\[ \int_{t_0}^\infty(t-t_0)\,g''(t)\,dt=-\int_{t_0}^\infty g'(t)\,dt=g(t_0), \]

because the boundary term \((t-t_0)g'(t)\) vanishes at \(t=t_0\) and at infinity.

For part 2, the function \(G(t)=G_z(e^t)\) satisfies \(G(0)=G'(0)=0\) and \(G''(t)=e^{zt}\). Since \(\lvert e^{z\tau}\rvert\le e^{\tau}\) for \(\tau\ge 0\), we get \(\lvert G'(t)\rvert\le te^t\) and \(\lvert G(t)\rvert\le t^2e^t\). Two integrations by parts give

\[ \int_0^\infty G\,g''\,dt=-\int_0^\infty G'\,g'\,dt=\int_0^\infty G''\,g\,dt=\int_0^\infty e^{zt}g(t)\,dt=\widehat f(z). \]

The boundary terms \(G\,g'\) and \(G'\,g\) vanish at \(t=0\) because \(G(0)=G'(0)=0\), and at infinity because \(\sigma>1\). ∎

**Lemma 5.6 (uniqueness).** Let \(L\) be a distribution on \([1,\infty)\) with \(L(u^{-s})=0\) for all integers \(s\ge 3\). Then \(L=0\).

**Proof.** Let \(G\) be as in Definition 5.4. Then \(L(u^{-s})=s^2\int_1^\infty G(u)u^{-s}d^{\times}u\). The substitution \(u=1/x\) gives \(\int_0^1\phi(x)\,x^n\,dx=0\) for all \(n\ge 0\), where \(\phi(x)=x^2G(1/x)\). By the growth condition, \(\lvert\phi(x)\rvert\le A\,x\,(1+\lvert\log x\rvert)^m\). So \(\phi\) extends to a continuous function on \([0,1]\). It is orthogonal to all polynomials. By the Weierstrass approximation theorem ([The Stone–Weierstrass theorem for functions vanishing at infinity, Theorem 10.1](course:function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity), applied to the polynomials with complex coefficients on \([0,1]\)) there are polynomials \(p_n\) that converge to \(\bar\phi\) uniformly on \([0,1]\). Hence \(\int_0^1\lvert\phi\rvert^2dx=\lim_n\int_0^1p_n\phi\,dx=0\), so \(\phi=0\), \(G=0\) and \(L=0\). ∎

In the variable \(t=\log u\) this is Lerch's theorem on the uniqueness of the Laplace transform. The proof shows more: the function \(G\) of a distribution is determined by the distribution.

**Lemma 5.7 (Gauss's formula).** Let \(\psi=\Gamma'/\Gamma\), and let \(\gamma\) be Euler's constant. For real \(s>0\),

\[ \psi\Big(\frac s2\Big)=-\gamma+2\int_1^\infty\frac{1-u^{2-s}}{u^2-1}\,d^{\times}u. \]

Moreover \(\psi(z+1)=\psi(z)+1/z\), \(\psi(\tfrac12)=-\gamma-2\log 2\), and \(\psi(z)=-1/z-\gamma+O(z)\) as \(z\to 0\).

**Proof.** The Weierstrass product \(1/\Gamma(z)=z\,e^{\gamma z}\prod_{n\ge 1}(1+z/n)e^{-z/n}\) ([The Gamma function and Stirling's formula, Theorem 1.2](course:NT-ZETA/NT-ZETA-03)) gives, by logarithmic differentiation,

\[ \psi(z)=-\gamma-\frac1z+\sum_{n\ge 1}\Big(\frac1n-\frac{1}{n+z}\Big)=-\gamma+\sum_{n\ge 0}\Big(\frac{1}{n+1}-\frac{1}{n+z}\Big). \]

The first expression gives the behaviour at \(z=0\), and the second gives \(\psi(z+1)-\psi(z)=1/z\). Let \(x>0\) be real. For \(0<y<1\) we have \((1-y^{x-1})/(1-y)=\sum_{n\ge 0}(y^n-y^{n+x-1})\), and all terms have the sign of \(x-1\). By monotone convergence,

\[ \int_0^1\frac{1-y^{x-1}}{1-y}\,dy=\sum_{n\ge 0}\Big(\frac{1}{n+1}-\frac{1}{n+x}\Big)=\psi(x)+\gamma. \]

Now put \(x=s/2\) and \(y=u^{-2}\). Then \(y^{x-1}=u^{2-s}\) and \(dy/(1-y)=-2\,d^{\times}u/(u^2-1)\). This gives the formula. For \(s=1\) it reads \(\psi(\tfrac12)=-\gamma-2\int_1^\infty du/(u(u+1))=-\gamma-2\log 2\). ∎

### 5.3 The counting distribution through the primes

Let \(\Lambda\) be the von Mangoldt function: \(\Lambda(n)=\log p\) if \(n\) is a power \(p^m\) of a prime with \(m\ge 1\), and \(\Lambda(n)=0\) otherwise. The logarithmic derivative of the Euler product gives \(-\zeta'(s)/\zeta(s)=\sum_n\Lambda(n)n^{-s}\) for \(\operatorname{Re}s>1\).

**Theorem 5.8 (the counting distribution).** Let \(c=\tfrac12(\log\pi+\gamma)\). For \(f\in\mathcal T\) put

\[ \langle N,f\rangle=\sum_{n\ge 2}\Lambda(n)\,f(n)+\int_1^\infty\frac{u^2f(u)-f(1)}{u^2-1}\,d^{\times}u+c\,f(1). \]

1. \(N\) is a distribution on \([1,\infty)\) in the sense of Definition 5.4.
2. \(\langle N,u^{-s}\rangle=-\zeta_{\mathbb Q}'(s)/\zeta_{\mathbb Q}(s)\) for \(\operatorname{Re}s>1\). So \(N\) solves (5.1), and it is the only distribution on \([1,\infty)\) that does.
3. \(N\) is positive on \((1,\infty)\). On the functions \(f\in\mathcal T\) with \(f(1)=0\) it is the positive measure

\[ \sum_p\sum_{m\ge 1}\log p\cdot\delta_{p^m}\ +\ \frac{u^2}{u^2-1}\,d^{\times}u. \]

We write \(\langle N,f\rangle=\int_1^\infty N(u)f(u)\,d^{\times}u\), and we call \(N\) the *counting distribution of* \(\overline{\operatorname{Spec}\mathbb Z}\).

*Reference:* [Connes–Consani 2010, formula (15) and Theorem 2.2].

**Proof.** The sum converges because \(f(n)=O(n^{-\sigma})\). The integrand is continuous at \(u=1\), and it is \(O(u^{-\sigma})+O(u^{-2})\) at infinity. So \(\langle N,f\rangle\) is defined.

*Part 1.* By Lemma 5.5,

\[ \sum_n\Lambda(n)f(n)=\int_1^\infty G_\Lambda(u)\,(\theta^2f)(u)\,d^{\times}u,\qquad G_\Lambda(u)=\sum_{n\le u}\Lambda(n)\log\frac un. \]

The exchange of sum and integral is allowed, because \(\int_n^\infty\log(u/n)\,u^{-\sigma}d^{\times}u=n^{-\sigma}/\sigma^2\) and \(\sum_n\Lambda(n)n^{-\sigma}<\infty\). The function \(G_\Lambda\) is continuous, and \(G_\Lambda(u)\le u(\log u)^2\).

For \(u>1\) we have \(1/(u^2-1)=\sum_{j\ge 1}u^{-2j}\), hence

\[ \frac{u^2f(u)-f(1)}{u^2-1}=f(u)+\sum_{j\ge 1}u^{-2j}\big(f(u)-f(1)\big). \]

Since \(f\) is bounded and \(\lvert f(u)-f(1)\rvert\le A'\log u\), we get \(\sum_j\int_1^\infty u^{-2j}\lvert f(u)-f(1)\rvert d^{\times}u\le A'\sum_j1/(4j^2)<\infty\). So we may integrate term by term:

\[ \int_1^\infty\frac{u^2f(u)-f(1)}{u^2-1}\,d^{\times}u=\widehat f(0)+\sum_{j\ge 1}\Big(\widehat f(-2j)-\frac{f(1)}{2j}\Big). \]

By Lemma 5.5, \(f(1)=\int_1^\infty\log u\,(\theta^2f)\,d^{\times}u\) and \(\widehat f(-2j)-f(1)/(2j)=\int_1^\infty\frac{u^{-2j}-1}{4j^2}(\theta^2f)\,d^{\times}u\). Summing over \(j\), which is allowed because \(\lvert u^{-2j}-1\rvert\le 1\), we find that \(N\) is the distribution with the function

\[ G_N(u)=\sum_{n\le u}\Lambda(n)\log\frac un+\frac12(\log u)^2+c\,\log u+H(u),\qquad H(u)=\sum_{j\ge 1}\frac{u^{-2j}-1}{4j^2}. \tag{5.2} \]

*Part 2.* Let \(s>1\) be real. By Lemma 5.7,

\[ \langle N,u^{-s}\rangle=\sum_n\Lambda(n)n^{-s}+\int_1^\infty\frac{u^{2-s}-1}{u^2-1}\,d^{\times}u+c=-\frac{\zeta'(s)}{\zeta(s)}-\frac12\psi\Big(\frac s2\Big)+\frac12\log\pi. \]

This is \(-\frac{d}{ds}\log\big(\pi^{-s/2}\Gamma(s/2)\zeta(s)\big)\). Both sides of the claimed identity are holomorphic for \(\operatorname{Re}s>1\), so they agree there. If \(N'\) is another distribution that solves (5.1), then \(N-N'\) vanishes on all \(u^{-s}\), and \(N=N'\) by Lemma 5.6.

*Part 3.* If \(f(1)=0\), then \(\langle N,f\rangle=\sum_n\Lambda(n)f(n)+\int_1^\infty\frac{u^2}{u^2-1}f(u)\,d^{\times}u\). This is \(\ge 0\) if \(f\ge 0\). ∎

Compare with Proposition 5.3. A prime \(p\) contributes the mass \(\log p\) at every power of \(p\), exactly as a closed point \(x\) of a curve contributes \(\log\mathrm Nx\) at every power of \(\mathrm Nx\). The place \(\infty\) contributes the density \(u^2/(u^2-1)=\sum_{j\ge 0}u^{-2j}\), together with a correction at the point \(u=1\). The exponents \(0,-2,-4,\dots\) are the zeros of \(1/\Gamma(s/2)\). This matches the regularized product \(\Gamma_{\mathbb R}(s)^{-1}=\prod_{n\ge 0}\frac{s+2n}{2\pi}\) of [Manin 1995, (1.33)], where \(\Gamma_{\mathbb R}(s)=2^{-1/2}\pi^{-s/2}\Gamma(s/2)\) as in (1.15) there.

**Proposition 5.9 (the point \(u=1\)).** The distribution \(N\) is not positive on \([1,\infty)\). More precisely, let \(\chi\colon[0,\infty)\to[0,1]\) be twice continuously differentiable with \(\chi=1\) on \([0,1]\) and \(\chi=0\) on \([2,\infty)\). For \(0<\varepsilon\le\tfrac14\) let \(f_\varepsilon(u)=\chi((u-1)/\varepsilon)\). Then \(f_\varepsilon\in\mathcal T\), \(0\le f_\varepsilon\le 1\), \(f_\varepsilon(1)=1\), and

\[ \langle N,f_\varepsilon\rangle\le\frac12\log\big(4\varepsilon(1+\varepsilon)\big)+c\ \longrightarrow\ -\infty\qquad(\varepsilon\to 0). \]

**Proof.** The function \(f_\varepsilon\) vanishes for \(u\ge 1+2\varepsilon\), and \(1+2\varepsilon<2\). So the sum over \(n\) is zero. For \(u\le 1+2\varepsilon\) we have \(u^2f_\varepsilon(u)-1\le u^2-1\), and for \(u\ge 1+2\varepsilon\) we have \(u^2f_\varepsilon(u)-1=-1\). Hence the integral is at most

\[ \int_1^{1+2\varepsilon}d^{\times}u-\int_{1+2\varepsilon}^\infty\frac{d^{\times}u}{u^2-1}=\log(1+2\varepsilon)+\frac12\log\Big(1-\frac{1}{(1+2\varepsilon)^2}\Big)=\frac12\log\big(4\varepsilon(1+\varepsilon)\big). \]

∎

So \(N\) carries an infinite negative mass at \(u=1\), which balances the divergence of the density \(u^2/(u^2-1)\) there. [Connes–Consani 2010, Remark 2.3] writes this as \(N(1)=-\infty\) and reads \(N(1)\) as the Euler characteristic of \(\overline{\operatorname{Spec}\mathbb Z}\). For a curve the corresponding number is \(N_0=2-2g\), by Proposition 3.7. This agrees with Remark 4.7: the genus is infinite.

### 5.4 The counting distribution through the zeros

**Theorem 5.10 (spectral form).** For every \(f\in\mathcal T\) the limit below exists, and

\[ \langle N,f\rangle=\widehat f(1)+\widehat f(0)-\lim_{T\to\infty}\ \sum_{\lvert\operatorname{Im}\rho\rvert<T}\widehat f(\rho). \]

In words: \(N(u)=u+1-\sum_\rho u^\rho\) as distributions on \([1,\infty)\), where the sum over the zeros is taken symmetrically.

*Reference:* [Connes–Consani 2010, formula (1) and Theorem 2.2]. Compare Corollary 2.5 and Proposition 4.8.

**Proof.** *Step 1: the sum over the zeros is a distribution.* By Lemma 5.5, \(\widehat f(\rho)=\int_1^\infty G_\rho\,(\theta^2f)\,d^{\times}u\) with \(G_\rho(u)=(u^\rho-1)/\rho^2-(\log u)/\rho\). Since \(0\le\operatorname{Re}\rho\le 1\), we have \(\lvert u^\rho-1\rvert\le u+1\). Since \(\sum_\rho\lvert\rho\rvert^{-2}<\infty\) by (Z2), the series

\[ E(u)=\sum_\rho\frac{u^\rho-1}{\rho^2} \]

converges absolutely and uniformly on bounded sets. So \(E\) is continuous, and \(\lvert E(u)\rvert\le A(u+1)\). By (Z2) at \(s=0\), the partial sums \(b_T=\sum_{\lvert\operatorname{Im}\rho\rvert<T}1/\rho\) converge to \(b=-\xi'(0)/\xi(0)\). In particular they are bounded. Let \(E_T\) be the partial sum of \(E\) over \(\lvert\operatorname{Im}\rho\rvert<T\). Then

\[ \sum_{\lvert\operatorname{Im}\rho\rvert<T}\widehat f(\rho)=\int_1^\infty\big(E_T(u)-b_T\log u\big)\,(\theta^2f)(u)\,d^{\times}u, \]

and the integrand is dominated by a constant times \((u+1+\log u)\,u^{-\sigma}\) with \(\sigma>1\). By dominated convergence the limit exists and equals \(\int_1^\infty G_Z\,(\theta^2f)\,d^{\times}u\) with

\[ G_Z(u)=E(u)-b\,\log u. \]

*Step 2: the difference vanishes.* By Theorem 5.8, Lemma 5.5 and Step 1,

\[ L(f)=\langle N,f\rangle-\widehat f(1)-\widehat f(0)+\lim_{T\to\infty}\sum_{\lvert\operatorname{Im}\rho\rvert<T}\widehat f(\rho) \]

is a distribution on \([1,\infty)\). Let \(f=u^{-s}\) with a real \(s>1\). Then \(\widehat f(z)=1/(s-z)\) for \(\operatorname{Re}z\le 1\), and by Theorem 5.8 and (Z2)

\[ L(u^{-s})=-\frac{\zeta_{\mathbb Q}'(s)}{\zeta_{\mathbb Q}(s)}-\frac{1}{s-1}-\frac1s+\frac{\xi'(s)}{\xi(s)}=0, \]

because \(\xi(s)=\tfrac12s(s-1)\zeta_{\mathbb Q}(s)\). By Lemma 5.6, \(L=0\). ∎

The function \(G\) of the distribution \(L\) is \(G_N-G_1-G_0+G_Z\). Since \(L=0\), this function is zero. Written out, this is a classical formula.

**Corollary 5.11 (an explicit formula with absolutely convergent sums).** For all \(x\ge 1\),

\[ \sum_{n\le x}\Lambda(n)\log\frac xn=x-1-\frac{\zeta'(0)}{\zeta(0)}\log x-\sum_{j\ge 1}\frac{x^{-2j}-1}{4j^2}-\sum_\rho\frac{x^\rho-1}{\rho^2}. \]

**Proof.** By (5.2), Lemma 5.5 and Step 1 above, the identity \(G_N-G_1-G_0+G_Z=0\) reads

\[ \sum_{n\le x}\Lambda(n)\log\frac xn=x-1-(1+c-b)\log x-H(x)-E(x). \]

It remains to compute \(b\). From \(\xi'/\xi=1/s+1/(s-1)-\tfrac12\log\pi+\tfrac12\psi(s/2)+\zeta'/\zeta\) and \(\tfrac12\psi(s/2)=-1/s-\gamma/2+O(s)\) we get \(\xi'(0)/\xi(0)=-1-c+\zeta'(0)/\zeta(0)\). So \(1+c-b=\zeta'(0)/\zeta(0)\). ∎

The value of the constant is \(\zeta'(0)/\zeta(0)=\log 2\pi\) ([Poisson summation, theta, and the functional equation, Theorem 4.2](course:NT-ZETA/NT-ZETA-04)).

**Corollary 5.12 (the form of Connes and Consani).**

1. The series \(\Omega(u)=\sum_\rho\frac{u^{\rho+2}}{(\rho+1)(\rho+2)}\) converges absolutely, uniformly on bounded subsets of \([1,\infty)\). The limit \(\omega_1=\lim_{T\to\infty}\sum_{\lvert\operatorname{Im}\rho\rvert<T}\frac{1}{\rho+1}\) exists, and

\[ \omega_1=-\frac{\xi'(-1)}{\xi(-1)}=\frac12+\frac\gamma2+\frac12\log 4\pi-\frac{\zeta'(-1)}{\zeta(-1)}. \]

2. Let \(h\colon[1,\infty)\to\mathbb C\) be twice continuously differentiable with \(h=O(u^{-2-\delta})\), \(h'=O(u^{-3-\delta})\) and \(h''=O(u^{-4-\delta})\) for some \(\delta>0\). Then \(uh\in\mathcal T\), and

\[ \int_1^\infty N(u)\,h(u)\,du=\int_1^\infty(u+1)\,h(u)\,du-\Big(\int_1^\infty\Omega(u)\,h''(u)\,du+\Omega(1)\,h'(1)-\omega_1\,h(1)\Big), \]

where the left side means \(\langle N,uh\rangle\).

3. For \(u>1\) let

\[ \omega(u)=\frac{u^2}{2}-\sum_{n<u}n\,\Lambda(n)+\frac12\log\frac{u+1}{u-1}-\frac{\zeta'(-1)}{\zeta(-1)}. \]

This function is integrable on bounded intervals, and \(\Omega(u)=\Omega(1)+\int_1^u\omega(v)\,dv\) for all \(u\ge 1\).

*Reference:* [Connes–Consani 2010, Theorem 2.2].

Here is how to read the statement. The functions \(h(u)=u^{-s-1}\) with \(\operatorname{Re}s>1\), which are the test functions used in [Connes–Consani 2010], satisfy the hypothesis of part 2. By part 3, \(\omega\) is the derivative of \(\Omega\), so \(\omega(u)\) is the sum of the series \(\sum_\rho u^{\rho+1}/(\rho+1)\) in the sense of distributions. For a continuously differentiable function \(\omega_0\) on \([1,\infty)\) with primitive \(\Omega_0\), two integrations by parts give \(\int_1^\infty\omega_0'\,h\,du=-\omega_0(1)h(1)+\Omega_0(1)h'(1)+\int_1^\infty\Omega_0\,h''\,du\). So part 2 says

\[ N(u)=u-\frac{d}{du}\,\omega(u)+1, \]

where the derivative is taken in the sense of distributions on the half-line, with the boundary value \(\omega_1\) at \(u=1\). The boundary value is the symmetric sum of the series at \(u=1\). It is not a limit of \(\omega(u)\): by part 3, \(\omega(u)\to+\infty\) as \(u\to 1\).

**Proof.** *Part 1.* We have \(\lvert u^{\rho+2}\rvert\le u^3\), and \(\lvert\rho+1\rvert\ge\lvert\rho\rvert\), \(\lvert\rho+2\rvert\ge\lvert\rho\rvert\) because \(\operatorname{Re}\rho\ge 0\). So the series converges by (Z2). The point \(s=-1\) is not a zero, and (Z2) gives \(\xi'(-1)/\xi(-1)=-\omega_1\). From the formula for \(\xi'/\xi\) in the proof of Corollary 5.11,

\[ \frac{\xi'(-1)}{\xi(-1)}=-1-\frac12-\frac12\log\pi+\frac12\psi\Big(-\frac12\Big)+\frac{\zeta'(-1)}{\zeta(-1)}. \]

By Lemma 5.7, \(\psi(-\tfrac12)=\psi(\tfrac12)+2=2-\gamma-2\log 2\). This gives the value of \(\omega_1\).

*Part 2.* One checks that \(\theta(uh)=uh+u^2h'\) and \(\theta^2(uh)=uh+3u^2h'+u^3h''\). So \(f=uh\) lies in \(\mathcal T\), and \(\widehat f(z)=\int_1^\infty h(u)\,u^z\,du\). Two integrations by parts give, for a zero \(\rho\),

\[ \widehat f(\rho)=-\frac{h(1)}{\rho+1}+\frac{h'(1)}{(\rho+1)(\rho+2)}+\int_1^\infty\frac{u^{\rho+2}}{(\rho+1)(\rho+2)}\,h''(u)\,du. \]

Sum over \(\lvert\operatorname{Im}\rho\rvert<T\) and let \(T\to\infty\). By part 1 and dominated convergence the limit is \(-\omega_1h(1)+\Omega(1)h'(1)+\int_1^\infty\Omega\,h''\,du\). Now apply Theorem 5.10.

*Part 3.* The function \(\omega\) is bounded on bounded intervals away from 1, and it has a logarithmic singularity at 1. So it is integrable on bounded intervals. We first prove, for \(h\) as in part 2 and with bounded support,

\[ \langle N,uh\rangle=\int_1^\infty(u+1)\,h\,du+\int_1^\infty\omega(u)\,h'(u)\,du+\omega_1\,h(1). \tag{5.3} \]

By definition, \(\langle N,uh\rangle=\sum_nn\Lambda(n)h(n)+\int_1^\infty\frac{u^3h(u)-h(1)}{u(u^2-1)}\,du+c\,h(1)\). On the other side, integration by parts gives

\[ \int_1^\infty\frac{u^2}{2}h'\,du=-\frac{h(1)}{2}-\int_1^\infty u\,h\,du,\qquad-\int_1^\infty\Big(\sum_{n<u}n\Lambda(n)\Big)h'\,du=\sum_nn\Lambda(n)h(n), \]

\[ \int_1^\infty\frac12\log\frac{u+1}{u-1}\,h'(u)\,du=\int_1^\infty\frac{h(u)-h(1)}{u^2-1}\,du. \]

In the last formula we used the primitive \(h(u)-h(1)\) of \(h'\), and the derivative \(-1/(u^2-1)\) of \(\tfrac12\log\frac{u+1}{u-1}\). Put \(a_0=\zeta'(-1)/\zeta(-1)\). The difference of the two sides of (5.3) is therefore

\[ \int_1^\infty\Big(\frac{u^3h(u)-h(1)}{u(u^2-1)}-h(u)-\frac{h(u)-h(1)}{u^2-1}\Big)du+\Big(c-\omega_1-a_0+\frac12\Big)h(1). \]

The integrand is \(h(1)/(u(u+1))\), and \(\int_1^\infty du/(u(u+1))=\log 2\). By part 1, \(\omega_1+a_0-\tfrac12=\tfrac\gamma2+\tfrac12\log 4\pi=c+\log 2\). So the difference is zero, and (5.3) holds.

Now compare (5.3) with part 2: \(\int_1^\infty\omega\,h'\,du=-\int_1^\infty\Omega\,h''\,du-\Omega(1)h'(1)\). Let \(\Omega_0(u)=\Omega(1)+\int_1^u\omega(v)\,dv\). Integration by parts gives \(\int_1^\infty\omega\,h'\,du=-\Omega(1)h'(1)-\int_1^\infty\Omega_0\,h''\,du\). Hence \(\int_1^\infty(\Omega-\Omega_0)\,h''\,du=0\) for all such \(h\). Every continuous function \(\kappa\) with bounded support in \([1,\infty)\) is of the form \(h''\): take \(h(u)=\int_u^\infty(v-u)\kappa(v)\,dv\). So the continuous function \(\Omega-\Omega_0\) is orthogonal to all continuous functions with bounded support. It is zero. ∎

[Connes–Consani 2010, formula (16)] states, with a reference to Ingham, that the series \(\sum_\rho u^{\rho+1}/(\rho+1)\), summed symmetrically, converges to \(\omega(u)\) at every \(u>1\) that is not a prime power. We do not use this pointwise statement. Part 3 is its integrated form.

**Corollary 5.13 (the explicit formula on the whole line).** Let \(h\colon(0,\infty)\to\mathbb C\) be twice continuously differentiable, and let \(k(u)=u^{-1}h(u^{-1})\). Suppose that the restrictions \(h_{+}\) and \(k_{+}\) of \(h\) and \(k\) to \([1,\infty)\) lie in \(\mathcal T\). For \(0\le\operatorname{Re}z\le 1\) put \(\widehat h(z)=\int_0^\infty h(u)\,u^z\,d^{\times}u\). Then

\[ \lim_{T\to\infty}\sum_{\lvert\operatorname{Im}\rho\rvert<T}\widehat h(\rho)=\widehat h(0)+\widehat h(1)-\langle N,h_{+}\rangle-\langle N,k_{+}\rangle. \]

Explicitly,

\[ \langle N,h_{+}\rangle+\langle N,k_{+}\rangle=\sum_{n\ge 2}\Lambda(n)\Big(h(n)+\frac1nh\Big(\frac1n\Big)\Big)+\int_1^\infty\frac{u^2h(u)+u\,h(1/u)-2h(1)}{u^2-1}\,d^{\times}u+(\log\pi+\gamma)\,h(1). \]

**Proof.** Split the integral for \(\widehat h(z)\) at \(u=1\) and substitute \(u\mapsto 1/u\) in the part from 0 to 1. This gives \(\widehat h(z)=\widehat{h_{+}}(z)+\widehat{k_{+}}(1-z)\), where the hats on the right are those of Definition 5.4. The zeros are stable under \(\rho\mapsto 1-\rho\), and this map preserves \(\lvert\operatorname{Im}\rho\rvert\). So \(\sum\widehat h(\rho)=\sum\widehat{h_{+}}(\rho)+\sum\widehat{k_{+}}(\rho)\) for the sums over \(\lvert\operatorname{Im}\rho\rvert<T\). Apply Theorem 5.10 to \(h_{+}\) and to \(k_{+}\), add, and use \(\widehat h(1)=\widehat{h_{+}}(1)+\widehat{k_{+}}(0)\) and \(\widehat h(0)=\widehat{h_{+}}(0)+\widehat{k_{+}}(1)\). The explicit form follows from the definition of \(N\), with \(k(1)=h(1)\) and \(u^2k(u)=u\,h(1/u)\). ∎

*Reference:* due to Weil. In [Bombieri 2000, Section V] the same formula is written with the constant \(\log 4\pi+\gamma\) and the integrand \((u\,h(u)+h(1/u)-2h(1))/(u^2-1)\) against \(du\); the two forms agree because \(\int_1^\infty\frac{2(1-1/u)}{u^2-1}\,du=2\log 2\).

So the counting distribution of Theorem 5.8, applied to \(h\) and to its reflection \(k\), is the arithmetic side of Weil's explicit formula. In the other direction, let \(f\in\mathcal T\), and let \(h\) be the function that equals \(f\) on \((1,\infty)\), vanishes on \((0,1)\) and has the value \(\tfrac12f(1)\) at \(u=1\). For this \(h\), which has a jump at \(u=1\), the explicit formula in the form of [Bombieri 2000, Section V] is the statement of Theorem 5.10. Here one uses \(\int_1^\infty\frac{(1-1/u)\,du}{u^2-1}=\log 2\) as above.

## 6. What is missing over the integers

The proof of Sections 2 and 3 used four things: a complete curve over a base field, the product of the curve with itself, the Frobenius correspondences, and the sign of the intersection form. This section takes them one by one. For each of them it says where the proof used it, what exists for the integers, and what would be needed. The paragraphs marked *Required* state requirements. They are not theorems.

### 6.1 The complete curve and its base field

*For the curve.* The curve \(C\) is projective over the field \(k=\mathbb F_q\). Completeness is what makes (R1) to (R3) true. The base field enters through Lemma 1.2: the effective divisors in a class are the points of a projective space over \(k\), and their number is what makes \(Z(C,T)\) a rational function with the functional equation.

*For the integers.* The closed points of \(\operatorname{Spec}\mathbb Z\) are the primes. The place \(\infty\) is not a point of \(\operatorname{Spec}\mathbb Z\). By Proposition 4.4 its local ring would be \(\mathbb Q\cap[-1,1]\), which is not a ring, and the constants are \(\{0,1,-1\}\), which is not a field. Moreover there is nothing below \(\operatorname{Spec}\mathbb Z\):

**Proposition 6.1.** There is no ring homomorphism from a field to \(\mathbb Z\). Every scheme has exactly one morphism to \(\operatorname{Spec}\mathbb Z\).

**Proof.** A ring homomorphism from a field \(L\) is injective. If \(L\) has characteristic \(p>0\), then \(p=0\) in the image, which is false in \(\mathbb Z\). If \(L\) has characteristic 0, then the image of \(\tfrac12\) is an integer \(x\) with \(2x=1\), which does not exist. For the second statement, a morphism from a scheme \(X\) to \(\operatorname{Spec}\mathbb Z\) is the same as a ring homomorphism \(\mathbb Z\to\Gamma(X,\mathcal O_X)\) [Stacks, Tag [01I1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-morphism-into-affine)], and there is exactly one. ∎

So \(\operatorname{Spec}\mathbb Z\) is not a scheme over any field, and it is the final object of the category of schemes.

*Required.* A category of geometric objects with a final object \(\operatorname{Spec}\mathbb F_1\), a functor of base change from this category to schemes, and an object \(\overline{\operatorname{Spec}\mathbb Z}\) over \(\operatorname{Spec}\mathbb F_1\) that is not final. Its points should be the places of \(\mathbb Q\) (Theorem 4.1), its zeta function should be \(\zeta_{\mathbb Q}\), and so its counting function must be the distribution \(N\) of Theorem 5.8. This is the programme described in [Manin 1995, Section 1.6] and [Lorscheid 2018b, Section 1.2]. Theorem 5.8 and Proposition 5.9 add two constraints: \(N\) is positive on \((1,\infty)\), as a count of points should be, and it has an infinite negative mass at \(u=1\).

### 6.2 The product

*For the curve.* The surface \(S=C\times_kC\) is the product over the base field. The diagonal is a curve on \(S\), different from \(S\), and its self-intersection is \(2-2g\) (Proposition 3.7).

*For the integers.*

**Proposition 6.2.** In the category of schemes the product of \(\operatorname{Spec}\mathbb Z\) with itself is \(\operatorname{Spec}\mathbb Z\), and the diagonal morphism is an isomorphism.

**Proof.** By Proposition 6.1, \(\operatorname{Spec}\mathbb Z\) is the final object. So the product of two schemes is their fibre product over \(\operatorname{Spec}\mathbb Z\), and \(\operatorname{Spec}\mathbb Z\times_{\operatorname{Spec}\mathbb Z}\operatorname{Spec}\mathbb Z=\operatorname{Spec}(\mathbb Z\otimes_{\mathbb Z}\mathbb Z)=\operatorname{Spec}\mathbb Z\) [Stacks, Tags [01I4](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-fibre-product-affine-schemes) and [01JQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-fibre-product-affines)]. ∎

So the product has dimension one, and the diagonal is everything. The same happens in every category in which the object that stands for the integers is final.

*Required.* A product \(\overline{\operatorname{Spec}\mathbb Z}\times_{\mathbb F_1}\overline{\operatorname{Spec}\mathbb Z}\) that is a two-dimensional object, in which the diagonal is a divisor, with a theory of divisors and intersection numbers satisfying the analogues of (S1) and (S2). [Manin 1995, Introduction] puts this as the central question: whether there is a category in which absolute powers \(\operatorname{Spec}\mathbb Z\times\dots\times\operatorname{Spec}\mathbb Z\) can be defined. [Manin 1995, Section 1.3, item C′] states that the approach to absolute motives through correspondences is out of reach because there is no absolute direct product of schemes over \(\mathbb Z\). The lesson *Generalized rings* computes the tensor product of \(\mathbb Z\) with itself over \(\mathbb F_1\) in one of the theories of this course.

### 6.3 The Frobenius correspondences

*For the curve.* The Frobenius morphism \(F\) is an endomorphism of \(C\) over \(k\). It is the identity on the points of the scheme and \(a\mapsto a^q\) on functions. The graphs \(\Gamma_r\) of its powers are curves on \(S\) with \(d_1(\Gamma_r)=1\), \(d_2(\Gamma_r)=q^r\) and \((\Gamma_r\cdot\Delta)=N_r\) (Proposition 3.7).

*For the integers.*

**Proposition 6.3.** The only ring endomorphism of \(\mathbb Z\) is the identity. For a prime \(p\), the map \(a\mapsto a^p\) is a ring endomorphism of \(\mathbb Z/p\mathbb Z\), and it is the identity.

**Proof.** A ring endomorphism fixes 1, hence every integer. In characteristic \(p\) the binomial formula gives \((a+b)^p=a^p+b^p\), and \(a^p=a\) in \(\mathbb Z/p\mathbb Z\) by Fermat's theorem. ∎

So \(\operatorname{Spec}\mathbb Z\) has no endomorphism other than the identity, and the graph of the identity is the diagonal. The map \(a\mapsto a^p\) is a ring homomorphism of every ring of characteristic \(p\), with a different exponent for each prime, and on \(\mathbb Z/p\mathbb Z\) itself it is the identity; on \(\mathbb Z\) it is not additive. No endomorphism of \(\operatorname{Spec}\mathbb Z\) can play the role of \(F\).

*Required.* A family of correspondences \(\Psi_u\) on the product of 6.2, indexed by the real numbers \(u\ge 1\) and not only by the powers of one number \(q\), with \(\Psi_1=\Delta\), \(d_1(\Psi_u)=1\) and \(d_2(\Psi_u)=u\). For a test function \(f\in\mathcal T\) the correspondence \(\Psi(f)=\int_1^\infty f(u)\Psi_u\,d^{\times}u\) should then have \(d_1=\widehat f(0)\) and \(d_2=\widehat f(1)\), and its intersection number with the diagonal should be the counting distribution:

\[ (\Psi(f)\cdot\Delta)=\langle N,f\rangle. \]

By Theorem 5.10 the trace \(d_1+d_2-(\Psi(f)\cdot\Delta)\) would then be \(\lim_T\sum_{\lvert\operatorname{Im}\rho\rvert<T}\widehat f(\rho)\). This is Theorem 3.9 transcribed by the dictionary. In cohomological terms the requirement is the operator \(\Phi\) of Remark 4.6, whose eigenvalues on \(H^1\) are the zeros.

Proposals exist. In [Connes–Consani–Marcolli 2009a, Section 7.1] the correspondences are the graphs \(Z_g\) of the multiplication by idèle classes \(g\) on the adèle class space of a global field. Definition 7.1 there sets the degree and codegree of \(Z(f)=\int f(g)Z_g\,d^{\times}g\) equal to \(\widehat f(1)\) and \(\widehat f(0)\). Theorem 4.16 there states that a test function \(f\) acts on a space \(H^1\), which is defined there, by a trace class operator whose trace is the sum of \(\widehat f\) over the zeros of the \(L\)-functions with Grössencharakter. The lesson *The arithmetic site* treats Frobenius correspondences indexed by positive real numbers, and the lesson *The scaling site* treats an action of the group of positive real numbers by automorphisms that are semilinear over Frobenius automorphisms. None of these constructions provides the fourth ingredient.

### 6.4 The positivity

*For the curve.* The Hodge index theorem (S3) gives \(\langle Z,Z\rangle\ge 0\) for every correspondence \(Z\) (Theorem 3.10). On the Frobenius correspondences this inequality is equivalent to the Riemann hypothesis (Theorem 3.13).

*For the integers.* The quadratic form of Theorem 3.13 has an exact analogue. Let \(\mathcal G\) be the space of functions \(f\colon(0,\infty)\to\mathbb C\) such that \(g(t)=f(e^t)\) is infinitely differentiable and \(e^{a\lvert t\rvert}g^{(n)}(t)\) is bounded for every \(a>0\) and every \(n\ge 0\). For \(f\in\mathcal G\) the function \(\widehat f(z)=\int_0^\infty f(u)\,u^z\,d^{\times}u\) is entire. Two integrations by parts give \(\lvert\widehat f(z)\rvert\le A_f\,\lvert z\rvert^{-2}\) for \(0\le\operatorname{Re}z\le 1\). So by (Z2) the sum

\[ W(f)=\sum_\rho\widehat f(\rho)\,\overline{\widehat f(1-\bar\rho)} \]

converges absolutely. It is a real number, because the involution \(\rho\mapsto 1-\bar\rho\) of the set of zeros replaces each term by its complex conjugate.

**Theorem 6.4 (Weil's criterion).** The Riemann hypothesis holds if and only if \(W(f)\ge 0\) for all \(f\in\mathcal G\).

*Reference:* due to Weil. See also [Bombieri 2000, Section V], and [Connes–Consani–Marcolli 2009a, Proposition 6.2 and Corollary 6.3] for all \(L\)-functions with Grössencharakter of a global field.

**Proof.** If the Riemann hypothesis holds, then \(1-\bar\rho=\rho\) for every zero, and \(W(f)=\sum_\rho\lvert\widehat f(\rho)\rvert^2\ge 0\).

Conversely, let \(\rho_0=\beta_0+i\gamma_0\) be a zero with \(\beta_0\ne\tfrac12\), of multiplicity \(m\). Then \(\rho_0'=1-\bar\rho_0=1-\beta_0+i\gamma_0\) is a different zero of multiplicity \(m\). Let \(R\) be the set of the zeros \(\rho\ne\rho_0,\rho_0'\) with \(\lvert\operatorname{Im}\rho-\gamma_0\rvert\le 2\), each taken once. It is finite, and it is stable under \(\rho\mapsto 1-\bar\rho\). Put

\[ Q(s)=\prod_{\rho\in R}(s-\rho),\qquad w=s-\tfrac12-i\gamma_0,\qquad\sigma(s)=1+2i\gamma_0-s,\qquad\Phi_A(s)=w\,Q(s)\,Q(\sigma(s))\,e^{Aw^2}\quad(A\ge 1). \]

*Step 1: \(\Phi_A=\widehat{f_A}\) for some \(f_A\in\mathcal G\).* We have \(\Phi_A=P_0(w)e^{Aw^2}\) for a polynomial \(P_0\) that does not depend on \(A\). Let \(k_A(t)=(4\pi A)^{-1/2}e^{-t^2/(4A)}\). Then \(\int_{\mathbb R}k_A(t)e^{wt}dt=e^{Aw^2}\) for all complex \(w\), and integration by parts gives \(\int_{\mathbb R}\big((-\tfrac{d}{dt})^nk_A\big)(t)\,e^{wt}dt=w^ne^{Aw^2}\). So the function \(g_A(t)=e^{-(\frac12+i\gamma_0)t}\,\big(P_0(-\tfrac{d}{dt})k_A\big)(t)\) satisfies \(\int_{\mathbb R}g_A(t)e^{st}dt=P_0(w)e^{Aw^2}\). Put \(f_A(u)=g_A(\log u)\). It lies in \(\mathcal G\), because \(g_A\) is a polynomial times a Gaussian times an exponential.

*Step 2: \(\overline{\Phi_A(1-\bar s)}=-\Phi_A(s)\).* The map \(s\mapsto 1-\bar s\) sends \(w\) to \(-\bar w\). So it turns the factor \(w\) into \(-w\) after conjugation, and it leaves \(e^{Aw^2}\) unchanged. Since \(R\) is stable under \(\rho\mapsto 1-\bar\rho\),

\[ \overline{Q(1-\bar s)}=\prod_{\rho\in R}(1-s-\bar\rho)=(-1)^{\lvert R\rvert}Q(s),\qquad\overline{Q(\sigma(1-\bar s))}=\prod_{\rho\in R}(s-2i\gamma_0-\bar\rho)=(-1)^{\lvert R\rvert}Q(\sigma(s)). \]

The two signs cancel, and the claim follows. Hence

\[ W(f_A)=-\sum_\rho\Phi_A(\rho)^2. \]

*Step 3: the terms.* If \(\rho\in R\), then \(\Phi_A(\rho)=0\). At \(\rho_0\) we have \(w=\beta_0-\tfrac12\) and \(\sigma(\rho_0)=\rho_0'\). By Step 2, \(Q(\rho_0')=(-1)^{\lvert R\rvert}\overline{Q(\rho_0)}\). So \(\Phi_A(\rho_0)=(-1)^{\lvert R\rvert}(\beta_0-\tfrac12)\lvert Q(\rho_0)\rvert^2e^{A(\beta_0-\frac12)^2}\), a nonzero real number, and in the same way \(\Phi_A(\rho_0')=-\Phi_A(\rho_0)\). These two zeros contribute

\[ -2m\,\big(\beta_0-\tfrac12\big)^2\,\lvert Q(\rho_0)\rvert^4\,e^{2A(\beta_0-\frac12)^2}\le-\lambda,\qquad\lambda=2m\,\big(\beta_0-\tfrac12\big)^2\,\lvert Q(\rho_0)\rvert^4>0. \]

For every other zero, \(\lvert\operatorname{Im}\rho-\gamma_0\rvert>2\), so \(\operatorname{Re}(w^2)=(\operatorname{Re}\rho-\tfrac12)^2-(\operatorname{Im}\rho-\gamma_0)^2<-\tfrac{15}{4}\) and

\[ \lvert\Phi_A(\rho)^2\rvert=\lvert P_0(w)\rvert^2e^{2A\operatorname{Re}(w^2)}\le e^{-\frac{15}{4}(2A-1)}\,\lvert P_0(w)\rvert^2e^{\operatorname{Re}(w^2)}. \]

The sum \(\Sigma_0\) of \(\lvert P_0(w)\rvert^2e^{\operatorname{Re}(w^2)}\) over these zeros is finite: the number of zeros with \(\lvert\rho\rvert\le r\) is at most \(r^2\sum_\rho\lvert\rho\rvert^{-2}\), while the terms decay like \(e^{-(\operatorname{Im}\rho-\gamma_0)^2}\). Therefore

\[ W(f_A)\le-\lambda+e^{-\frac{15}{4}(2A-1)}\,\Sigma_0, \]

which is negative for large \(A\). ∎

**Remark 6.5 (the arithmetic form of the positivity).** For \(f,k\in\mathcal G\) let \((f\star k)(u)=\int_0^\infty f(u/v)k(v)\,d^{\times}v\) and \(f^{\sharp}(u)=u^{-1}\overline{f(u^{-1})}\). In the variable \(t=\log u\) the product \(\star\) is the convolution, so \(f\star k\in\mathcal G\) and \(\widehat{f\star k}=\widehat f\,\widehat k\). Also \(\widehat{f^{\sharp}}(z)=\overline{\widehat f(1-\bar z)}\). So \(h=f\star f^{\sharp}\) has \(\widehat h(\rho)=\widehat f(\rho)\overline{\widehat f(1-\bar\rho)}\), and \(W(f)=\sum_\rho\widehat h(\rho)\). Moreover \(u^{-1}h(u^{-1})=\overline{h(u)}\). Corollary 5.13 now gives

\[ W(f)=2\operatorname{Re}\Big(\widehat f(0)\,\overline{\widehat f(1)}-\langle N,h_{+}\rangle\Big),\qquad h=f\star f^{\sharp}. \]

Compare this with \(\langle Z,Z\rangle=2\,d_1(Z)\,d_2(Z)-(Z\cdot Z)\). The numbers \(\widehat f(0)\) and \(\widehat f(1)\) are the two degrees, and \(\langle N,h_{+}\rangle\), which is a sum over the primes plus a term for the place \(\infty\), stands for the self-intersection. So the Riemann hypothesis is equivalent to an inequality between the primes and the place \(\infty\) on one side and two degrees on the other side. For a curve the corresponding inequality is Theorem 3.10.

*Required.* A reason for the inequality \(W(f)\ge 0\): an analogue of the Hodge index theorem (S3) for the product of 6.2, applied to the correspondences \(\Psi(f)\) of 6.3. By Theorem 6.4 any proof of this positivity is a proof of the Riemann hypothesis. In [Connes–Consani–Marcolli 2009a] the positivity is not proved: Proposition 7.2 there restates it as an estimate for an intersection number and shows that the estimate is equivalent to the Riemann hypothesis for the \(L\)-functions with Grössencharakter.

### 6.5 A Hurwitz inequality

There is a second use of the same dictionary, which needs a morphism and not a product. For a finite separable morphism of curves the Riemann–Hurwitz formula bounds the total ramification. [Smirnov 1992] proposes an analogue for the integers. The projective line over the field of constants is replaced by a set with the points \([0]\), \([\infty]\) and \([n]\) for \(n\ge 1\), of degrees \(\deg[0]=\deg[\infty]=1\) and \(\deg[n]=\phi(n)\), where \(\phi\) is Euler's function [Smirnov 1992, Section 2.3]. The points of degree 1 of this set are \([0]\), \([\infty]\), \([1]\) and \([2]\). Every rational number \(a\) other than \(0\), \(1\) and \(-1\) defines a map \(\tau_a\) from the set of places of \(\mathbb Q\) to this set [Smirnov 1992, Section 2.5]. With the degrees \(\deg[p]=\log p\) and \(\deg[\infty]=1\) of Proposition 4.3, the map has a degree \(\deg\tau_a\), and every place \(x\) that \(\tau_a\) maps to a point of degree 1 has a ramification index \(e_x\) and a defect \(\delta_x=(e_x-1)\deg(x)/\deg\tau_a\) [Smirnov 1992, Sections 2.6 and 3.2].

The *conjecture* is [Smirnov 1992, Sections 3.5 and 3.6]: for every \(\varepsilon>0\) there is a constant \(A_\varepsilon\) such that, for every rational number \(a\) other than \(0\), \(1\) and \(-1\), the sum of the defects \(\delta_x\) over all places \(x\) that \(\tau_a\) maps to a point of degree 1 is at most \(2+\varepsilon+A_\varepsilon/\deg\tau_a\). The *theorem* is [Smirnov 1992, Section 5.1, Theorem 1]: this conjecture implies the ABC conjecture. The conjecture itself is not proved. [Jarra 2023b] proves that Smirnov's set is the set of non-generic points of the strong congruence space of the monoid scheme \(\mathbb P^1\) over \(\mathbb F_1\), and that each map \(\tau_a\) extends to a continuous map into this space from a space \(\overline{\operatorname{Spec}\mathbb Z}\) whose non-generic points are the places of \(\mathbb Q\). The lesson *The projective line over F_1 and the ABC conjecture* treats this in full.

### 6.6 Summary

Weil's proof for a curve uses the following objects. For the integers the first three are not defined in the category of schemes, and the fourth is equivalent to the Riemann hypothesis.

1. **A base and a complete curve.** A final object \(\operatorname{Spec}\mathbb F_1\) below \(\operatorname{Spec}\mathbb Z\), and a complete curve \(\overline{\operatorname{Spec}\mathbb Z}\) over it that contains the place \(\infty\) as a point, with counting distribution \(N\) (Theorem 5.8). Obstruction: Propositions 4.4 and 6.1.
2. **The product.** A two-dimensional object \(\overline{\operatorname{Spec}\mathbb Z}\times_{\mathbb F_1}\overline{\operatorname{Spec}\mathbb Z}\) with intersection numbers, in which the diagonal is a divisor. Obstruction: Proposition 6.2.
3. **The Frobenius correspondences.** Divisors \(\Psi_u\) on the product, for real \(u\ge 1\), with degrees \(1\) and \(u\), whose intersection with the diagonal is \(N\). Obstruction: Proposition 6.3.
4. **The positivity.** The inequality \(\langle Z,Z\rangle\ge 0\) for the correspondences \(Z=\Psi(f)\), that is, \(W(f)\ge 0\). By Theorem 6.4 this is the Riemann hypothesis itself.

Items 1 to 3 ask for objects. Item 4 asks for a theorem about them. Objects as in items 1 to 3 give a geometric reading of the explicit formula (Corollary 5.13). Without item 4 they give no information on the zeros.

## 7. Exercises

**Exercise 1 (a second curve of genus one).** Let \(E'\) be the projective closure of \(y^2+y=x^3\) over \(\mathbb F_2\).

1. Show that \(E'\) is a curve of genus 1 in the sense of Section 1.1, and compute \(N_1\).
2. Find \(P(T)\), the numbers \(\alpha_j\) and the class number \(h\). Check the Riemann hypothesis.
3. Compute \(N_2\) and \(N_3\) from Corollary 2.5, and check \(N_2\) by a direct count.
4. For which \(r\le 3\) is the bound of Theorem 3.12 an equality?

**Solution.** 1. The cubic is \(y^2z+yz^2=x^3\). In characteristic 2 its partial derivatives are \(x^2\), \(z^2\) and \(y^2\), which have no common zero. So \(E'\) is a smooth plane cubic. It is geometrically irreducible and of genus 1, as in Example 2.10. Over \(\mathbb F_2\): for \(x=0\) we get \(y\in\{0,1\}\); for \(x=1\) the equation \(y^2+y=1\) has no solution; and there is one point at infinity, \((0:1:0)\). So \(N_1=3\).

2. \(\alpha_1+\alpha_2=q+1-N_1=0\) and \(\alpha_1\alpha_2=2\). So \(P(T)=1+2T^2\), \(\alpha_{1,2}=\pm i\sqrt2\), and \(\lvert\alpha_j\rvert=\sqrt2\). The class number is \(h=P(1)=3\).

3. \(\alpha_1^2+\alpha_2^2=-4\), so \(N_2=4+1+4=9\). \(\alpha_1^3+\alpha_2^3=0\), so \(N_3=8+1=9\). Direct count over \(\mathbb F_4\): the expression \(y^2+y\) is \(0\) for \(y\in\{0,1\}\) and \(1\) for the two other elements. The cube \(x^3\) is \(0\) for \(x=0\) and \(1\) for the three other elements. So every \(x\) gives two points. With the point at infinity, \(N_2=8+1=9\).

4. The bound is \(\lvert N_r-2^r-1\rvert\le 2\cdot 2^{r/2}\). For \(r=1\) and \(r=3\) the left side is 0. For \(r=2\) it is \(4=2\cdot 2\): equality. Over \(\mathbb F_4\) this curve has the largest number of points that a curve of genus 1 can have.

**Exercise 2 (genus one).** Let \(g=1\) and \(a=q+1-N_1\).

1. Show, without using Section 3, that the Riemann hypothesis for \(C\) is equivalent to \(a^2\le 4q\).
2. Deduce that it is equivalent to \(q+1-2\sqrt q\le N_1\le q+1+2\sqrt q\), and show that \(N_1\) need not lie in the interval from \(q-2\sqrt q\) to \(q+2\sqrt q\).

**Solution.** 1. By Corollary 2.5, \(P(T)=1-aT+qT^2\), and \(\alpha_1,\alpha_2\) are the roots of \(X^2-aX+q\). If \(a^2\le 4q\), the roots are complex conjugates of each other, or equal, and their product is \(q\). So \(\lvert\alpha_j\rvert^2=q\). If \(a^2>4q\), the roots are real and distinct with product \(q\). Two distinct real numbers of absolute value \(\sqrt q\) have product \(-q\). So they do not both have absolute value \(\sqrt q\).

2. \(a^2\le 4q\) means \(\lvert N_1-q-1\rvert\le 2\sqrt q\). For the curve of Example 2.10, \(q=2\) and \(N_1=5\), while \(q+2\sqrt q<4.83\).

**Exercise 3 (the explicit formula of a curve on both sides).** Let \(c\colon\mathbb Z\to\mathbb C\) be a function with finite support, written \(r\mapsto c_r\), and let \(\widehat c(z)=\sum_{r\in\mathbb Z}c_rq^{rz}\). Choose \(\rho_j\) with \(q^{\rho_j}=\alpha_j\). Show that

\[ \sum_{j=1}^{2g}\widehat c(\rho_j)=\widehat c(0)+\widehat c(1)+(2g-2)\,c_0-\sum_x\sum_{m\ge 1}\deg x\,\Big(c_{m\deg x}+q^{-m\deg x}\,c_{-m\deg x}\Big), \]

and compare with Corollary 5.13.

**Solution.** We have \(\sum_j\widehat c(\rho_j)=\sum_rc_rS_r\) with \(S_r=\sum_j\alpha_j^r\) for all integers \(r\). For \(r\ge 1\), \(S_r=q^r+1-N_r\). For \(r=0\), \(S_0=2g\). For \(r=-m<0\), the stability of the \(\alpha_j\) under \(\alpha\mapsto q/\alpha\) gives \(S_{-m}=q^{-m}S_m=1+q^{-m}-q^{-m}N_m\). Hence

\[ \sum_rc_rS_r=\sum_rc_r(1+q^r)+(2g-2)c_0-\sum_{m\ge 1}N_m\big(c_m+q^{-m}c_{-m}\big). \]

By Lemma 1.1, \(N_m=\sum_{\deg x\mid m}\deg x\), which gives the last sum of the statement. In Corollary 5.13 the terms \(\Lambda(n)h(n)\) and \(\Lambda(n)n^{-1}h(1/n)\) correspond to \(\deg x\cdot c_{m\deg x}\) and \(\deg x\cdot q^{-m\deg x}c_{-m\deg x}\), and \(\widehat h(0)+\widehat h(1)\) corresponds to \(\widehat c(0)+\widehat c(1)\). The term \((2g-2)c_0=-N_0c_0\) is the contribution of \(r=0\). Its counterpart is the behaviour of \(N\) at the point \(u=1\) described in Proposition 5.9.

**Exercise 4 (involutions and the case of equality).** Let \(\iota\colon C\to C\) be an automorphism over \(k\) with \(\iota\circ\iota=\mathrm{id}\) and \(\iota\ne\mathrm{id}\). Let \(C^{\iota}=\delta^{-1}(\Gamma_\iota)\) be its fixed-point scheme and \(n_\iota=\dim_k\Gamma(C^{\iota},\mathcal O_{C^{\iota}})\).

1. Show that \(d_1(\Gamma_\iota)=d_2(\Gamma_\iota)=1\), \((\Gamma_\iota\cdot\Gamma_\iota)=2-2g\) and \((\Gamma_\iota\cdot\Delta)=n_\iota\).
2. Deduce that \(n_\iota\le 2g+2\), with equality if and only if \(\Delta+\Gamma_\iota-2V-2W\) is numerically trivial.
3. Let \(C\) be the smooth projective curve over \(\mathbb F_3\) with the affine equation \(y^2=x^5+1\), and let \(\iota(x,y)=(x,-y)\). Show that \(g=2\) and \(n_\iota=6\).
4. Conclude that for the curve of part 3 the effective divisor \(Z=\Delta+\Gamma_\iota\) has \(d_1(Z)=g\), \(d_2(Z)=2\) and \(\langle Z,Z\rangle=0\).
5. Let \(g\ge 2\) and suppose that \(n_\iota=2g+2\). For \(r\ge 0\) let \(\varphi=\iota\circ F^r\) and \(T_r=\Gamma_r+\Gamma_\varphi\). Show that \(\langle T_r,M\rangle=0\) for all \(M\in\operatorname{Pic}(S)\). Deduce that the effective divisor \(Z_r=(g-2)\Delta+T_r\) has \(d_1(Z_r)=g\), \(d_2(Z_r)=g-2+2q^r\) and \(\langle Z_r,Z_r\rangle=2g(g-2)^2\).
6. Let \(C\) be the smooth projective curve over \(\mathbb F_3\) with the affine equation \(y^2=x^7+1\), and let \(\iota(x,y)=(x,-y)\). Show that \(g=3\) and \(n_\iota=8\). Conclude that \(Z_1=\Delta+\Gamma_1+\Gamma_{\iota\circ F}\) has \(d_1(Z_1)=g\), \(d_2(Z_1)=7\) and \(\langle Z_1,Z_1\rangle=6\).

**Solution.** 1. Lemma 3.2 applies to \(\varphi=\iota\). As in the proof of Proposition 3.7, \((L\cdot\Gamma_\iota)=\deg\gamma_\iota^{\ast}L\). We have \(\gamma_\iota^{\ast}p_1^{\ast}B=B\) and \(\gamma_\iota^{\ast}p_2^{\ast}B=\iota^{\ast}B\), of degree \(\deg B\) by (C3). So both degrees are 1. Next, \(\gamma_\iota^{\ast}\mathcal O_S(\Gamma_\iota)=\gamma_\iota^{\ast}(\iota\times\mathrm{id})^{\ast}\mathcal O_S(\Delta)=(\iota,\iota)^{\ast}\mathcal O_S(\Delta)=\iota^{\ast}\delta^{\ast}\mathcal O_S(\Delta)\), of degree \(2-2g\). Finally \(C^{\iota}\ne C\) because \(\iota\ne\mathrm{id}\). So \(C^{\iota}\) is an effective Cartier divisor on \(C\) [Stacks, Tag [02OO](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-pullback-effective-Cartier-defined)], Lemma 3.1 gives \(\delta^{\ast}\mathcal O_S(\Gamma_\iota)\cong\mathcal O_C(C^{\iota})\), and its degree is \(n_\iota\) by (C2).

2. Let \(Z=\Delta+\Gamma_\iota\). Then \(d_1(Z)=d_2(Z)=2\) and \((Z\cdot Z)=(2-2g)+2n_\iota+(2-2g)\). So \(\langle Z,Z\rangle=8-(Z\cdot Z)=4g+4-2n_\iota\). Theorem 3.10 gives \(n_\iota\le 2g+2\), and its case of equality gives the rest. Parts 1 and 2 did not use \(\iota\circ\iota=\mathrm{id}\). So for every automorphism \(\iota\ne\mathrm{id}\) of \(C\) over \(k\) the fixed-point scheme has degree at most \(2g+2\).

3. Let \(A=\mathbb F_3[x,y]/(y^2-x^5-1)\) and \(U=\operatorname{Spec}A\). The partial derivatives of \(y^2-x^5-1\) are \(x^4\) and \(2y\). A common zero has \(x=y=0\), which is not on the curve. So \(U\) is smooth. The polynomial \(x^5+1\) has odd degree, so it is not a square in the field of rational functions over an algebraic closure of \(\mathbb F_3\), and \(U\) is geometrically irreducible. Let \(K\) be its function field and let \(v\) be a place of \(K\) with \(v(x)<0\). Then \(2v(y)=5v(x)\), so \(v(x)\) is even. So the place is ramified over the place \(x=\infty\) of \(\mathbb F_3(x)\), and since \([K:\mathbb F_3(x)]=2\) there is exactly one such place. It has degree 1, with \(v(x)=-2\) and \(v(y)=-5\). So \(C=U\cup\{\infty\}\), and \(t=x^2/y\) is a uniformizer at \(\infty\).

The morphism \(x\colon C\to\mathbb P^1\) has degree 2. It is ramified at the zeros of \(y\), which form the divisor of degree 5 given by \(x^5+1=0\), and at \(\infty\). Each ramification index is 2, which is prime to the characteristic. The Riemann–Hurwitz formula [Stacks, Tags [0C1D](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-lemma-rh) and [0C1F](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-lemma-rhe)] gives \(2g-2=2\cdot(-2)+5+1=2\). So \(g=2\).

The map \(\iota\) fixes \(x\) and sends \(y\) to \(-y\). Every \(a\in A\) is \(a_0(x)+a_1(x)y\), and \(\iota(a)-a=-2a_1y=a_1y\). So the ideal of \(C^{\iota}\cap U\) is \((y)\), and \(C^{\iota}\cap U=\operatorname{Spec}\mathbb F_3[x]/(x^5+1)\), of dimension 5. At \(\infty\) the map \(\iota\) acts trivially on the residue field, so \(\iota(a)-a\) lies in the maximal ideal \((t)\) for every \(a\) in the local ring, and \(\iota(t)-t=-2t=t\). So the ideal of \(C^{\iota}\) at \(\infty\) is \((t)\), which contributes 1. Hence \(n_\iota=6=2g+2\).

4. This follows from parts 1 to 3. Note that \(d_2(Z)=2>0\) although \(\langle Z,Z\rangle=0\).

5. The morphism \(\varphi\) is finite of degree \(q^r\), by Lemma 3.5. So Lemma 3.2 applies to it, and \((L\cdot\Gamma_\varphi)=\deg\gamma_\varphi^{\ast}L\) for every invertible sheaf \(L\) on \(S\). As in the proof of Proposition 3.7, \(d_1(\Gamma_\varphi)=1\) and \(d_2(\Gamma_\varphi)=q^r\). Since \((\varphi\times\mathrm{id})\circ\gamma_\varphi=(\varphi,\varphi)=\delta\circ\varphi\), we get \((\Gamma_\varphi\cdot\Gamma_\varphi)=\deg\varphi^{\ast}\delta^{\ast}\mathcal O_S(\Delta)=q^r(2-2g)\). Since \((\varphi\times\mathrm{id})\circ\gamma_r=(\iota\circ F^r,F^r)=\tau\circ\gamma_\iota\circ F^r\) and \(\tau^{\ast}\mathcal O_S(\Delta)\cong\mathcal O_S(\Delta)\), we get \((\Gamma_r\cdot\Gamma_\varphi)=\deg\,(F^r)^{\ast}\gamma_\iota^{\ast}\mathcal O_S(\Delta)=q^r\,(\Delta\cdot\Gamma_\iota)=q^r\,n_\iota\). Hence

\[ \langle\Gamma_\varphi,\Gamma_\varphi\rangle=2q^r-q^r(2-2g)=2g\,q^r,\qquad\langle\Gamma_r,\Gamma_\varphi\rangle=2q^r-q^r\,n_\iota=-2g\,q^r. \]

Theorem 3.9 gives \(\langle\Gamma_r,\Gamma_r\rangle=2g\,q^r\). So \(\langle T_r,T_r\rangle=2g\,q^r-4g\,q^r+2g\,q^r=0\), and Corollary 3.11 gives \(\langle T_r,M\rangle^2\le\langle T_r,T_r\rangle\,\langle M,M\rangle=0\) for all \(M\). Therefore \(\langle Z_r,Z_r\rangle=(g-2)^2\langle\Delta,\Delta\rangle=2g(g-2)^2\). The degrees are \(d_1(Z_r)=(g-2)+1+1\) and \(d_2(Z_r)=(g-2)+q^r+q^r\). The hypothesis \(\iota\circ\iota=\mathrm{id}\) was not used. For \(r=0\) and \(g=2\) this is part 4.

6. The solution of part 3 applies with 7 in place of 5. The partial derivatives of \(y^2-x^7-1\) are \(2x^6\) and \(2y\), and their only common zero \(x=y=0\) is not on the curve. A place \(v\) with \(v(x)<0\) has \(2v(y)=7v(x)\). So there is exactly one such place \(\infty\). It has degree 1, with \(v(x)=-2\) and \(v(y)=-7\), and \(t=x^3/y\) is a uniformizer at \(\infty\). The morphism \(x\colon C\to\mathbb P^1\) has degree 2 and is ramified at the zeros of \(y\), which form a divisor of degree 7, and at \(\infty\). So \(2g-2=-4+7+1=4\) and \(g=3\). The ideal of \(C^{\iota}\cap U\) is \((y)\), with \(\mathbb F_3[x]/(x^7+1)\) of dimension 7, and \(\iota(t)-t=-2t=t\) at \(\infty\). So \(n_\iota=8=2g+2\). Part 5 with \(r=1\) and \(q=3\) gives \(d_1(Z_1)=3\), \(d_2(Z_1)=7\) and \(\langle Z_1,Z_1\rangle=6\). So \(\langle Z,Z\rangle\ge 2d_2(Z)\) fails for this effective divisor with \(d_1(Z)=g\), and \(Z_1\) is not in the kernel of the form.

**Exercise 5 (projective spaces over \(\mathbb F_1\)).** Let \(N(u)=1+u+\dots+u^n\).

1. Compute \(F(q,s)\) of Proposition 5.1 in closed form, and check its limit for \(q\to 1\) directly.
2. Find \(\zeta_N\).
3. What is \(N(1)\), and where does it enter in Example 5.2?

**Solution.** 1. \(F(q,s)=\log q\sum_{j=0}^{n}\sum_{r\ge 1}q^{r(j-s)}=\sum_{j=0}^{n}\frac{\log q\cdot q^{j-s}}{1-q^{j-s}}\). With \(\eta=\log q\) each term is \(\eta e^{-(s-j)\eta}/(1-e^{-(s-j)\eta})\), which tends to \(1/(s-j)\) as \(\eta\to 0\). And \(\int_1^\infty u^{j-s}d^{\times}u=1/(s-j)\) for \(\operatorname{Re}s>j\). So both sides of Proposition 5.1 are \(\sum_j1/(s-j)\).

2. By Example 5.2, \(\zeta_N(s)=\prod_{j=0}^{n}(s-j)^{-1}\).

3. \(N(1)=n+1\). It is the exponent of \(q-1\) that makes the limit in Example 5.2 finite, and it is the number of poles of \(\zeta_N\). It is also the number of elements of the set that the lesson *Counting over finite fields and the limit q → 1* takes as the projective space of dimension \(n\) over \(\mathbb F_1\). For \(\overline{\operatorname{Spec}\mathbb Z}\) the corresponding value is \(-\infty\) (Proposition 5.9), and \(\Pi\) has infinitely many zeros.

**Exercise 6 (the affine line \(\operatorname{Spec}\mathbb Z\) and the trivial zeros).** Let \(f\in\mathcal T\) vanish on \([1,1+\varepsilon]\) for some \(\varepsilon>0\). Show that

\[ \sum_n\Lambda(n)f(n)=\widehat f(1)-\lim_{T\to\infty}\sum_{\lvert\operatorname{Im}\rho\rvert<T}\widehat f(\rho)-\sum_{j\ge 1}\widehat f(-2j), \]

and explain the exponents that occur.

**Solution.** By Theorems 5.8 and 5.10,

\[ \sum_n\Lambda(n)f(n)+\int_1^\infty\frac{u^2}{u^2-1}f(u)\,d^{\times}u=\widehat f(1)+\widehat f(0)-\lim_{T\to\infty}\sum_{\lvert\operatorname{Im}\rho\rvert<T}\widehat f(\rho). \]

For \(u\ge 1+\varepsilon\) we have \(u^2/(u^2-1)=\sum_{j\ge 0}u^{-2j}\), and \(\sum_ju^{-2j}\lvert f(u)\rvert\le\lvert f(u)\rvert/(1-(1+\varepsilon)^{-2})\), which is integrable. So the integral is \(\sum_{j\ge 0}\widehat f(-2j)\). Subtract \(\widehat f(0)\).

The exponents on the right are the pole \(1\) of \(\zeta\), its nontrivial zeros \(\rho\), and the numbers \(-2,-4,\dots\). The latter are the trivial zeros of \(\zeta\): the function \(\Gamma(s/2)\) has poles there, and \(\zeta_{\mathbb Q}\) has none, by (Z1). So the primes alone have the counting distribution \(u-\sum u^{\omega}\) on \((1,\infty)\), where \(\omega\) runs over all zeros of \(\zeta\). This is von Mangoldt's formula ([Perron's formula and the explicit formula for ψ(x), Theorem 3.1](course:NT-ZETA/NT-ZETA-11)) in differentiated form. Adding the place \(\infty\) adds \(\sum_{j\ge 0}u^{-2j}\). This removes the trivial zeros and adds the term \(1=u^0\), and gives \(N(u)=u+1-\sum_\rho u^\rho\). The same happens for a curve: removing a rational point from \(C\) changes the count \(q^r+1-\sum_j\alpha_j^r\) into \(q^r-\sum_j\alpha_j^r\).

## What this lesson does not prove

The following results are used or quoted without proof.

1. **The Riemann–Roch theorem for curves** and the facts (R1) to (R3) of Section 1.2: [Stacks, Tags [0BS6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-lemma-rr), [0BY7](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-definition-genus), [0C1A](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-lemma-genus-smooth) and [0BUG](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-proper-geometrically-reduced-global-sections)]. These are the prerequisites of the lesson.
2. **Intersection numbers on a surface**, facts (S1) and (S2): [Stacks, Tags [0BEM](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-numerical-polynomial-from-euler), [0BEP](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-definition-intersection-number), [0BEQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-intersection-number-integer), [0BER](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-intersection-number-additive), [0BEU](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-numerical-intersection-effective-Cartier-divisor), [0BEY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-intersection-numbers-and-degrees-on-curves) and [0AYR](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-definition-degree-invertible-sheaf)].
3. **Serre duality and basic facts on ample sheaves**, used in the proof of (S3) in Section 3.1: [Stacks, Tags [00NQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-regular-ring-CM), [0AWX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/dualizing.html#dualizing-lemma-regular-gorenstein), [0FVZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/duality.html#duality-lemma-duality-proper-over-field-CM), [0BFQ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/duality.html#duality-lemma-gorenstein), [02O6](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/coherent.html#coherent-lemma-proper-over-affine-cohomology-finite), [02UZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/cohomology.html#cohomology-proposition-vanishing-Noetherian), [0BEV](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-ample-positive), [01Q3](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/properties.html#properties-proposition-characterize-ample) and [0890](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/properties.html#properties-lemma-ample-tensor-globally-generated)].
4. **Degrees on curves**, facts (C1) to (C4): [Stacks, Tags [0AYX](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-degree-tensor-product), [0AYY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-degree-effective-Cartier-divisor), [0AYZ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/varieties.html#varieties-lemma-degree-pullback-map-proper-curves), [02NY](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-definition-degree), [0B3P](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/divisors.html#divisors-lemma-conormal-effective-Cartier-divisor), [08S2](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/morphisms.html#morphisms-lemma-differentials-diagonal) and [0C1A](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#curves-lemma-genus-smooth)].
5. **Facts about schemes** that are used with a tag: points with a finite residue field are closed [Tag 01TE]; smoothness and irreducibility of \(C\times C\) [Tags 01VB, 01VA, 038F, 056S]; when the inverse image of an effective Cartier divisor is one [Tag 02OO]; sections of separated and of smooth morphisms [Tags 01KT and 067R]; the valuative criterion of properness [Tag 0BX5]; the genus of a plane curve [Tag 0BYD]; the Riemann–Hurwitz formula, in Exercise 4 [Tags 0C1D and 0C1F]; morphisms to an affine scheme and fibre products of affine schemes [Tags 01I1, 01I4 and 01JQ].
6. **The analytic continuation, the functional equation and the Hadamard product of the completed zeta function**, facts (Z1) and (Z2), proved in the course on the Riemann zeta function: [Poisson summation, theta, and the functional equation, Theorem 3.1](course:NT-ZETA/NT-ZETA-04) and [Entire functions of order one and the Hadamard product of ξ, Theorems 4.1 and 5.1](course:NT-ZETA/NT-ZETA-05); historically [Riemann 1859] and [Hadamard 1893]. Also the Weierstrass product of the Gamma function, [The Gamma function and Stirling's formula, Theorem 1.2](course:NT-ZETA/NT-ZETA-03); the number of zeros up to a given height, [The Riemann–von Mangoldt formula, Theorem 2.1](course:NT-ZETA/NT-ZETA-10); and the value \(\zeta'(0)/\zeta(0)=\log 2\pi\), [Poisson summation, theta, and the functional equation, Theorem 4.2](course:NT-ZETA/NT-ZETA-04).
7. **The Weierstrass approximation theorem**, used in Lemma 5.6, proved in [The Stone–Weierstrass theorem for functions vanishing at infinity, Theorem 10.1](course:function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity).
8. **The pointwise convergence** of \(\sum_\rho u^{\rho+1}/(\rho+1)\) to the function \(\omega(u)\) of Corollary 5.12: [Connes–Consani 2010, formula (16)], with a reference there to Ingham. Only the integrated form is proved here.
9. **The composition of correspondences** [Connes–Consani–Marcolli 2009a, Section 2.1] and the identity \(\operatorname{Tr}(Z\star Z')=\langle Z,Z\rangle\) [Milne 2015, Section 1]. They are not used.
10. **The cohomological statements** of Remark 4.6: the description of \(\zeta_C\) by \(\ell\)-adic cohomology [Manin 1995, formulas (1.3) and (1.4)], and the theorem on the regularized product, [Deninger 1992, Theorem 3.3], which is the first equality of [Manin 1995, formula (1.5)].
11. **The results of** [Connes–Consani–Marcolli 2009a] quoted in Section 6: Theorem 4.16, Definition 7.1, Propositions 6.2 and 7.2, Corollary 6.3.
12. **Smirnov's theorem** that the conjectural Hurwitz inequality implies the ABC conjecture [Smirnov 1992, Section 5.1, Theorem 1], and the theorems of [Jarra 2023b] quoted in Section 6.5. See *The projective line over F_1 and the ABC conjecture*.
13. **The explicit formula for functions with jumps**, quoted after Corollary 5.13: [Bombieri 2000, Section V].

## References

- [Stacks] The [Stacks project](https://stacks.math.columbia.edu/), cited by tag. Each tag links to the same place in [AI Integrated Stacks Project](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/), the programme's edition of the Stacks project, which agrees with it modulo corrections made by GPT-6 Astra (OpenAI, Ultra setting) on suggestions of GPT-5.6 Sol (OpenAI, Ultra setting). Of the tags cited in this lesson, Tag 01I1 carries such corrections: wording, notation and small precisions in statements and proofs. None of them changes the results used here.
- [Vakil 2024] R. Vakil, *The Rising Sea: Foundations of Algebraic Geometry*, draft of 27 July 2024; published by Princeton University Press. Free at http://math.stanford.edu/~vakil/216blog/FOAGjul2724public.pdf
- [Connes–Consani–Marcolli 2009a] A. Connes, C. Consani, M. Marcolli, *The Weil proof and the geometry of the adèles class space*, arXiv:math/0703392. Free at https://alainconnes.org/wp-content/uploads/The-Weil-proof-and-the-geometry-2009.pdf
- [Connes–Consani 2010] A. Connes, C. Consani, *Schemes over F_1 and zeta functions*, arXiv:0903.2024. Formula numbers refer to the arXiv version. Free at https://alainconnes.org/wp-content/uploads/schemesF1zeta.pdf
- [Lorscheid 2018b] O. Lorscheid, *F_1 for everyone*, [arXiv:1801.05337](https://arxiv.org/pdf/1801.05337).
- [Soulé 2004] C. Soulé, *Les variétés sur le corps à un élément*, [arXiv:math/0304444](https://arxiv.org/pdf/math/0304444).
- [Milne 2015] J. S. Milne, *The Riemann hypothesis over finite fields: from Weil to the present day*, [arXiv:1509.00797](https://arxiv.org/pdf/1509.00797).
- [Jarra 2023b] M. Jarra, *On Smirnov's approach to the abc conjecture*, [arXiv:2306.16637](https://arxiv.org/pdf/2306.16637).
- [Manin 1995] Yu. Manin, *Lectures on zeta functions and motives (according to Deninger and Kurokawa)*, Astérisque 228 (1995), 121–163. Free at https://www.numdam.org/item/AST_1995__228__121_0/
- [Bombieri 2000] E. Bombieri, *Problems of the Millennium: the Riemann Hypothesis*, problem description of the Clay Mathematics Institute. Free at https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf
- [Deninger 1992] C. Deninger, *Local L-factors of motives and regularized determinants*, Invent. Math. 107 (1992), 135–150. Free at https://eudml.org/doc/143961
- [Smirnov 1992] A. L. Smirnov, *Hurwitz inequalities for number fields*, Algebra i Analiz 4 (1992), no. 2, 186–209 (Russian); English translation in St. Petersburg Math. J. 4 (1993), no. 2, 357–375. Section numbers refer to the Russian original. Free at https://www.mathnet.ru/eng/aa316
- [Riemann 1859] B. Riemann, Ueber die Anzahl der Primzahlen unter einer gegebenen Grösse, *Monatsberichte der Berliner Akademie*, November 1859, 671–680. Free at https://www.maths.tcd.ie/pub/HistMath/People/Riemann/Zeta/ (the original and an English translation by D. R. Wilkins)
- [Hadamard 1893] J. Hadamard, Étude sur les propriétés des fonctions entières et en particulier d'une fonction considérée par Riemann, *J. Math. Pures Appl.* (4) 9 (1893), 171–215. Free at https://www.numdam.org/item/JMPA_1893_4_9__171_0/
