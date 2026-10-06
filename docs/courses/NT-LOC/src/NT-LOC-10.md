# Herbrand's function and the upper numbering

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Independent full-lesson AI review is not yet recorded. Public domain (CC0).*

Lower ramification numbers measure motion in the upper field's normalized valuation. They behave well when we restrict to a subgroup. Passing to a quotient changes that upper field and its valuation scale, so the same indices no longer work. Herbrand's function makes the required change of variable. The resulting upper numbering is compatible with every Galois quotient and therefore with infinite Galois extensions.

Let \(L/K\) be finite Galois, with both fields nonarchimedean local fields in either characteristic, and put \(G=\operatorname{Gal}(L/K)\). We use the results of **Ramification groups and the different of a local extension**:
\[
i_G(\sigma)=\min_{x\in\mathcal O_L}v_L(\sigma x-x),
\quad
G_i=\{\sigma:i_G(\sigma)\geq i+1\},
\quad
G_u=G_{\lceil u\rceil}\quad(u\geq-1).
\]
Here \(v_L\) is normalized to have value group \(\mathbf Z\), and \(i_G(1)=+\infty\). In particular \(G_0\) is inertia and \(e=|G_0|\).

## 1. Rescaling the lower index

Define
\[
\varphi_{L/K}(u)=
\begin{cases}
u,&-1\leq u\leq0,\\
\displaystyle\int_0^u\frac{|G_t|}{|G_0|}\,dt,&u\geq0.
\end{cases}
\tag{1.1}
\]
Write \(\psi_{L/K}\) for its inverse.

**Proposition 1.1.** The function \(\varphi\) is a continuous, strictly increasing, piecewise linear, concave bijection from \([-1,\infty)\) to itself. Its inverse \(\psi\) is continuous, strictly increasing, piecewise linear and convex. For every \(u\geq-1\),
\[
\varphi_{L/K}(u)
=\frac1e\sum_{\sigma\in G}\min\{i_G(\sigma),u+1\}-1.
\tag{1.2}
\]

*Proof.* For \(t>0\), the integrand is a positive step function. Its values decrease as the lower groups decrease, and lie between \(1/e\) and \(1\). Thus the integral is continuous, strictly increasing and piecewise linear, with nonincreasing slopes. It joins the slope-one segment on \([-1,0]\), so is concave on the whole domain. It tends to infinity because its slope is at least \(1/e\). This proves bijectivity; inverting each linear segment proves the assertions about \(\psi\).

For (1.2), denote its right side by \(F(u)\). A noninertial automorphism has \(i_G(\sigma)=0\), and every inertial one has \(i_G(\sigma)\geq1\). Hence on \([-1,0]\) the sum is \(e(u+1)\), giving \(F(u)=u\). Both \(F\) and \(\varphi\) are continuous and piecewise linear. If \(m<u<m+1\), with integral \(m\geq0\), the terms of \(F\) with positive slope are exactly those with
\[
i_G(\sigma)\geq m+2,
\]
because the finite motion numbers are integers. There are \(|G_{m+1}|\) such terms, including identity. Thus
\(F'(u)=|G_{m+1}|/e=\varphi'(u)\).
Equality at zero and equality of slopes on every open segment prove (1.2), including all endpoints. \(\square\)

The **upper ramification groups** are
\[
G^v=G_{\psi_{L/K}(v)}\qquad(v\geq-1).
\tag{1.3}
\]
If \(b\) is a lower jump, the corresponding upper jump is \(\varphi(b)\). Our groups retain their value at the jump and decrease immediately after it.

For any finite tame Galois extension, put \(e=|G_0|\). Every positive lower group is trivial, so
\[
\varphi(u)=u/e,\quad\psi(v)=ev\qquad(u,v\geq0).
\tag{1.4}
\]
The upper groups are \(G\) at \(v=-1\), inertia \(G_0\) on \(-1<v\leq0\), and identity for \(v>0\). Consequently \(-1\) is a jump exactly when the residue degree \(f>1\), and zero is a jump exactly when \(e>1\). The formula includes unramified extensions and the trivial extension.

## 2. A quotient averages motion over its fibers

Let \(H\triangleleft G\), put \(L'=L^H\), and write \(Q=G/H=\operatorname{Gal}(L'/K)\). Set \(e_H=e(L/L')=|H_0|\).

**Lemma 2.1 (coset motion formula).** For \(s\in Q\),
\[
i_Q(s)=\frac1{e_H}\sum_{\sigma\mapsto s}i_G(\sigma).
\tag{2.1}
\]
For \(s=1\), both sides are \(+\infty\).

*Proof.* Choose integral generators \(\mathcal O_L=\mathcal O_K[\alpha]\) and \(\mathcal O_{L'}=\mathcal O_K[\beta]\). Then also \(\mathcal O_L=\mathcal O_{L'}[\alpha]\). Let \(f\in\mathcal O_{L'}[X]\) be the monic minimal polynomial of \(\alpha\) over \(L'\). Fix a lift \(\sigma\) of a nonidentity \(s\). Put
\[
a=s\beta-\beta,\qquad
b=(\sigma f)(\alpha)
 =\prod_{h\in H}(\alpha-\sigma h\alpha).
\]
We show that \(a,b\) generate the same ideal in \(\mathcal O_L\).

Each coefficient \(c\) of \(f\) is a polynomial in \(\beta\) with coefficients in \(\mathcal O_K\). The difference \(sc-c\) is therefore divisible by \(a\). As \(f(\alpha)=0\), this proves that
\(b=(\sigma f-f)(\alpha)\) is divisible by \(a\).

Conversely, write \(\beta=P(\alpha)\), with \(P\in\mathcal O_K[X]\). Divide \(P(X)-\beta\) by the monic \(f\); the remainder has degree less than \(\deg f\) and vanishes at \(\alpha\), so it is zero. Thus
\[
P(X)-\beta=f(X)R(X),\qquad R\in\mathcal O_{L'}[X].
\]
Apply \(\sigma\) to coefficients and evaluate at \(\alpha\). The left side is \(\beta-s\beta=-a\); the right side is \(b(\sigma R)(\alpha)\). Hence \(a\) is divisible by \(b\). Neither is zero, since \(s\ne1\) and \(\alpha\) generates \(L\). Their equal values now give
\[
e_H i_Q(s)
=v_L(s\beta-\beta)
=\sum_{h\in H}v_L(\alpha-\sigma h\alpha)
=\sum_{\sigma'\mapsto s}i_G(\sigma').
\]
The first equality uses \(v_L|_{L'}=e_H v_{L'}\). If \(s=1\), the fiber contains identity, so the sum and \(i_Q(1)\) are both infinite. \(\square\)

This identity includes the ramification scale \(e_H\), even when the intermediate extension has a nontrivial unramified part.

## 3. Herbrand's theorem

**Theorem 3.1 (quotients and towers).** For \(u\geq-1\),
\[
G_uH/H=Q_{\varphi_{L/L'}(u)}.
\tag{3.1}
\]
The functions satisfy
\[
\varphi_{L/K}=\varphi_{L'/K}\circ\varphi_{L/L'},
\qquad
\psi_{L/K}=\psi_{L/L'}\circ\psi_{L'/K}.
\tag{3.2}
\]
Consequently, for every \(v\geq-1\),
\[
G^vH/H=Q^v.
\tag{3.3}
\]

*Proof.* First observe that
\[
i_G(\sigma\tau)\geq\min\{i_G(\sigma),i_G(\tau)\},
\tag{3.4}
\]
with equality if the two finite motion numbers differ. To check this, apply
\(\sigma\tau\alpha-\alpha=\sigma(\tau\alpha-\alpha)+(\sigma\alpha-\alpha)\).
The two summands have the stated values, and unequal values cannot cancel.

For a nonidentity coset \(s\in Q\), choose a lift \(\sigma\) whose motion number \(m=i_G(\sigma)\) is maximal among that finite fiber. For each \(h\in H\), (3.4) gives
\[
i_G(\sigma h)=\min\{m,i_G(h)\}.
\tag{3.5}
\]
Indeed, if \(i_G(h)<m\), equality follows from unequal values. If \(i_G(h)\geq m\), the value is at least \(m\) and cannot exceed \(m\) by maximality.

Lower numbering respects subgroups, so \(i_H(h)=i_G(h)\). Lemma 2.1 and (1.2) applied to \(L/L'\) therefore give
\[
i_Q(s)-1
=\frac1{e_H}\sum_{h\in H}\min\{m,i_H(h)\}-1
=\varphi_{L/L'}(m-1).
\tag{3.6}
\]
Here \(m\geq0\), so \(m-1\geq-1\) is in the domain.

The coset \(s\) occurs in \(G_uH/H\) exactly when its maximal motion number satisfies \(m-1\geq u\). Strict increase of \(\varphi_{L/L'}\) and (3.6) make this equivalent to
\(i_Q(s)-1\geq\varphi_{L/L'}(u)\), precisely membership in the right side of (3.1). Identity belongs to both sides. This proves (3.1), including real indices and their endpoints.

Let \(t=\varphi_{L/L'}(u)\). The kernel on \(G_u\) is \(H_u\), so (3.1) yields
\[
|G_u|=|H_u|\,|Q_t|.
\tag{3.7}
\]
Ramification indices multiply in towers: \(e_G=e_H e_Q\). Away from the finitely many breakpoints on any bounded interval, (3.7) gives
\[
\varphi'_{L/K}(u)
=\frac{|G_u|}{e_G}
=\frac{|H_u|}{e_H}\frac{|Q_t|}{e_Q}
=\bigl(\varphi_{L'/K}\circ\varphi_{L/L'}\bigr)'(u).
\]
For negative indices all functions are identity. For nonnegative indices the two continuous piecewise linear functions agree at zero and on the slope of every common linear segment. This proves the first formula in (3.2); inversion gives the second.

Finally choose \(u=\psi_{L/K}(v)\). Equation (3.2) says that \(\varphi_{L/L'}(u)=\psi_{L'/K}(v)\). Substitution into (3.1) gives (3.3). \(\square\)

The order of composition in (3.2) is essential. The first rescaling removes the upper extension \(L/L'\); the second removes \(L'/K\). Inverse rescalings act in the reverse order.

## 4. Infinite Galois extensions

**Proposition 4.1.** Let \(M/K\) be an algebraic Galois extension, possibly infinite. For real \(v\geq-1\), define
\[
\operatorname{Gal}(M/K)^v
=\{\sigma : \sigma|_L\in\operatorname{Gal}(L/K)^v
       \text{ for every finite Galois }L/K\text{ in }M\}.
\tag{4.1}
\]
These are closed normal decreasing subgroups, and
\[
\operatorname{Gal}(M/K)^v
\simeq\varprojlim_L\operatorname{Gal}(L/K)^v.
\tag{4.2}
\]
Restriction onto each finite upper group is surjective. A cofinal family of finite Galois subextensions gives the same groups.

*Proof.* Finite Galois subextensions form a directed system under compositum. The finite quotient theorem says that restriction between their upper groups at this fixed \(v\) is surjective. Thus they form an inverse system of finite groups.

The usual Galois inverse-limit identification turns (4.1) exactly into (4.2). Each condition in (4.1) is the inverse image of a normal subgroup in a finite discrete group, so is closed and normal. Intersections preserve these properties; decrease follows at every finite level.

For surjectivity onto one finite level, fix an element of its upper group. In the product of the finite groups, impose compatibility and that fixed coordinate. Every finite set of these conditions can be solved at a common larger finite Galois level, using the surjective restriction maps. They are closed conditions in a compact product of finite spaces. The finite intersection property gives a compatible point solving all of them. This proves surjectivity.

A cofinal family determines all other coordinates by restriction; Herbrand's theorem carries its upper-group conditions down to every smaller level. Conversely any full inverse-limit element satisfies the cofinal conditions. Hence the choice of cofinal family changes nothing. \(\square\)

This definition concerns the algebraic extension \(M\). It does not replace \(M\) by its valuation completion.

**Hasse–Arf theorem, stated without proof here.** For a finite abelian extension of local fields, every upper jump is an integer. Here a jump \(v\) means \(G^v\ne G^{v+\epsilon}\) for every \(\epsilon>0\). Its programme proof provider is *Class field theory*, lesson 10, **Abelian ramification, conductors and Hasse–Arf**, Corollary 10.3. That provider is written. This names its exact proof; its own preceding reciprocity and existence dependencies are separate programme results. The quotient theorem proved above does not require Hasse–Arf. Section 7 gives a nonabelian jump at \(1/2\).

## 5. Cyclotomic upper numbering

Let \(L_n=\mathbf Q_p(\zeta_{p^n})\) and \(G_n=(\mathbf Z/p^n\mathbf Z)^\times\).

**Proposition 5.1.** For \(-1\leq v\leq0\), \(G_n^v=G_n\). For \(v>0\),
\[
G_n^v=
\{a\in G_n:a\equiv1\pmod{p^{\lceil v\rceil}}\}.
\tag{5.1}
\]
A congruence exponent at least \(n\) means the trivial subgroup. The positive upper jumps are exactly \(1,\ldots,n-1\). Zero is also a jump when \(p>2\), and is not a jump when \(p=2\).

For \(L_\infty=\bigcup_n L_n\),
\[
\operatorname{Gal}(L_\infty/\mathbf Q_p)=\mathbf Z_p^\times,
\qquad
\operatorname{Gal}(L_\infty/\mathbf Q_p)^v
=1+p^{\lceil v\rceil}\mathbf Z_p\quad(v>0),
\tag{5.2}
\]
with the full group for \(-1\leq v\leq0\).

*Proof.* Put \(b_k=p^k-1\), so \(b_0=0\), and \(N=(p-1)p^{n-1}\). The lower computation in **Ramification groups and the different of a local extension** gives, for \(1\leq k<n\), a group of order \(p^{n-k}\) on
\[
b_{k-1}<u\leq b_k.
\]
The slope of \(\varphi\) there is
\[
\frac{p^{n-k}}N=\frac1{(p-1)p^{k-1}},
\]
and the interval length is \((p-1)p^{k-1}\). Each interval therefore contributes exactly \(1\) to \(\varphi\). Thus \(\varphi(b_k)=k\), with
\[
\varphi(u)=
(k-1)+\frac{u-b_{k-1}}{(p-1)p^{k-1}}
\quad(b_{k-1}\leq u\leq b_k).
\tag{5.3}
\]
Beyond the last lower break,
\[
\varphi(u)=n-1+\frac{u-b_{n-1}}N.
\tag{5.4}
\]
For \(n=1\), (5.4) is the entire nonnegative formula.

These linear changes carry the lower congruence subgroup of level \(k\) to \(k-1<v\leq k\). That is (5.1), including the jump endpoints. Consecutive positive congruence groups have index \(p\) until they become trivial. At zero the quotient has order \(p-1\), so a jump is present exactly when \(p>2\). This also covers the trivial \(p=2,n=1\) extension.

At finite levels the automorphisms are compatible unit exponents modulo \(p^n\). Their inverse limit is \(\mathbf Z_p^\times\). For fixed \(v>0\), the conditions (5.1) at all levels say exactly that this unit is \(1\) modulo \(p^{\lceil v\rceil}\). Proposition 4.1 then gives (5.2). \(\square\)

## 6. Two quadratic rescalings

**Example 6.1.** For \(\mathbf Q_2(i)/\mathbf Q_2\), the lower groups are \(G_0=G_1=G\), followed by identity. Hence
\[
\varphi(u)=
\begin{cases}
u,&-1\leq u\leq1,\\
1+(u-1)/2,&u\geq1,
\end{cases}
\qquad
\psi(v)=
\begin{cases}
v,&-1\leq v\leq1,\\
1+2(v-1),&v\geq1.
\end{cases}
\]
The upper group is the order-two group through \(v=1\), and trivial for \(v>1\).

**Example 6.2.** For \(\mathbf Q_2(\sqrt2)/\mathbf Q_2\), the lower group remains the order-two group through index \(2\). Thus
\[
\varphi(u)=
\begin{cases}
u,&-1\leq u\leq2,\\
2+(u-2)/2,&u\geq2,
\end{cases}
\qquad
\psi(v)=
\begin{cases}
v,&-1\leq v\leq2,\\
2+2(v-2),&v\geq2.
\end{cases}
\]
Its unique upper jump is \(2\). Both examples satisfy the integral-jump conclusion of Hasse–Arf.

## 7. Exercises

1. Compute \(\varphi\) and the upper groups for \(\mathbf Q_2(i)/\mathbf Q_2\).

2. Prove the closed formula (1.2), including negative indices and jump endpoints.

3. Verify the quotient and tower formulas for
\(\mathbf Q_p(\zeta_{p^2})\supseteq\mathbf Q_p(\zeta_p)\supseteq\mathbf Q_p\).

4. Compute the lower and upper groups of the splitting field of \(X^3-2\) over \(\mathbf Q_3\). Prove its group is \(S_3\), and check Herbrand's theorem on the quotient \(\mathbf Q_3(\sqrt{-3})\).

## 8. Complete solutions

**Solution 1.** The uniformizer \(i-1\) moves by \(-2i\) under conjugation, of normalized value \(2\). Thus \(G_u=G\) for \(-1\leq u\leq1\), and \(G_u=1\) for \(u>1\). The slope \(|G_u|/|G_0|\) is \(1\) up to \(1\), then \(1/2\). Integrating gives the formula in Example 6.1. Inversion doubles the distance beyond the break: \(\psi(v)=1+2(v-1)\) for \(v\geq1\). Therefore \(G^v=G\) through \(v=1\), followed by identity.

**Solution 2.** A noninertial automorphism has motion zero, while each of the \(e\) inertial automorphisms has motion at least one. For \(-1\leq u\leq0\), the capped sum in (1.2) is thus \(e(u+1)\), giving \(u\). On an open positive interval \(m<u<m+1\), its derivative counts exactly the motion numbers at least \(m+2\). These are the elements of \(G_{m+1}=G_u\), so the derivative is \(|G_u|/e\). Both sides equal zero at zero and are continuous. Equality on each open linear segment therefore extends to every integer endpoint. Identity contributes the finite cap \(u+1\), so its infinite motion number causes no divergent summand.

**Solution 3.** Write \(L_2,L_1,K\) for the three fields and \(H=\operatorname{Gal}(L_2/L_1)\). Their degrees are \(p(p-1),p-1,1\), so \(H\) has order \(p\). The full lower groups of \(L_2/K\) are \(G_0=G\), \(G_i=H\) for \(1\leq i\leq p-1\), and identity for \(i\geq p\). Subgroup intersection gives \(H_i=H\) through \(i=p-1\), then identity. Thus, for \(u\geq0\),
\[
\varphi_{L_2/L_1}(u)=
\begin{cases}
u,&u\leq p-1,\\
p-1+(u-p+1)/p,&u\geq p-1.
\end{cases}
\]
The tame quotient \(L_1/K\) has function \(t/(p-1)\). Composing gives
\[
\varphi_{L_2/K}(u)=
\begin{cases}
u/(p-1),&u\leq p-1,\\
1+(u-p+1)/(p(p-1)),&u\geq p-1,
\end{cases}
\]
exactly the integral of the full lower group sizes. All three functions are identity on \([-1,0]\).

For \(u\leq0\), the lower image is the full quotient. For \(u>0\), it is trivial; the rescaled index \(\varphi_{L_2/L_1}(u)\) is positive, where the tame quotient is also trivial. This verifies (3.1). The full upper group is \(H\) on \(0<v\leq1\), then identity, whose positive-index images in the quotient are trivial. At nonpositive indices its image is the full quotient. This verifies (3.3) and, by inversion of the displayed functions, both tower identities. When \(p=2\), \(L_1=K\), the quotient is trivial, and the same formulas hold with \(p-1=1\).

**Solution 4.** Let \(\alpha^3=2\), \(\zeta^3=1\) with \(\zeta\ne1\), and \(L=\mathbf Q_3(\alpha,\zeta)\). The element \(\beta=\alpha+1\) satisfies
\[
\beta^3-3\beta^2+3\beta-3=0,
\]
an Eisenstein polynomial at \(3\). Hence \(M=\mathbf Q_3(\alpha)\) is totally ramified of degree \(3\), with uniformizer \(\beta\). The field \(T=\mathbf Q_3(\zeta)=\mathbf Q_3(\sqrt{-3})\) is a totally ramified quadratic field: \(2\zeta+1\) has square \(-3\). Its uniformizer \(\lambda=\zeta-1\) satisfies \(Y^2+3Y+3=0\).

The degrees \(3\) and \(2\) give \([L : \mathbf Q_3]=6\). All three cubic roots \(\alpha,\zeta\alpha,\zeta^2\alpha\) lie in \(L\), so it is the splitting field and is Galois. Its action on the three roots embeds its group in \(S_3\); order \(6\) proves equality. Its ramification index is divisible by both \(3\) and \(2\), hence is \(6\); the extension is totally ramified.

In the normalized valuation of \(L\), \(v_L(\beta)=2\) and \(v_L(\lambda)=3\). Therefore
\[
\pi=\lambda/\beta
\]
is a uniformizer, and integral uniformizer generation permits the motion calculation with \(\pi\).

Let \(\sigma(\alpha)=\zeta\alpha\), \(\sigma(\zeta)=\zeta\), an order-three element. Then \(\sigma\beta-\beta=\lambda\alpha\), and
\[
\sigma\pi-\pi
=-\frac{\lambda^2\alpha}{\beta\,\sigma\beta}.
\]
The value is \(6-2-2=2\), since \(\alpha\) is a unit and \(\sigma\beta\) has the same value as \(\beta\). The inverse order-three element has the same motion number, either by the intrinsic inverse rule or by the same calculation.

Let \(\tau\) fix \(\alpha\) and send \(\zeta\) to \(\zeta^2\). It is an involution and satisfies \(\tau\pi/\pi=\zeta+1\). The residue of this ratio is \(2\) in \(\mathbf F_3\), so \(v_L(\tau\pi-\pi)=1\). All three involutions are conjugate in \(S_3\), and intrinsic motion is conjugation invariant, so they all have motion \(1\).

It follows that
\[
G_{-1}=G_0=S_3,\qquad G_1=A_3,\qquad G_2=1.
\]
For real positive indices, \(G_u=A_3\) on \(0<u\leq1\), and identity beyond \(1\). Thus
\[
\varphi_{L/\mathbf Q_3}(u)=
\begin{cases}
u,&-1\leq u\leq0,\\
u/2,&0\leq u\leq1,\\
1/2+(u-1)/6,&u\geq1.
\end{cases}
\]
The upper groups are \(S_3\) for \(-1\leq v\leq0\), \(A_3\) for \(0<v\leq1/2\), and identity for \(v>1/2\). The positive upper jump \(1/2\) is nonintegral.

For the quotient field \(T\), \(H=A_3\). Its subgroup lower groups are \(H_0=H_1=H\), followed by identity, so
\[
\varphi_{L/T}(u)=u\ (0\leq u\leq1),
\qquad
\varphi_{L/T}(u)=1+(u-1)/3\ (u\geq1).
\]
The quotient \(T/\mathbf Q_3\) is tame quadratic and has \(\varphi_{T/\mathbf Q_3}(t)=t/2\) for \(t\geq0\). Composing gives exactly the displayed full \(\varphi\). Every positive lower group of \(G\) maps trivially to \(G/H\), matching the quotient's trivial lower group at the positive rescaled index. The upper image is likewise full at nonpositive indices and trivial at every positive index. This checks Herbrand's theorem explicitly.

This also attains the sharp wild bound in [**Ramification groups and the different of a local extension**, Theorem 3.1](NT-LOC-09.md): \(e=6\), \(|G_1|=p=3\), and \(G_2=1\), so \(d=e+p-2=7\). As a different check, Hilbert's formula gives \(d(L/\mathbf Q_3)=(6-1)+(3-1)=7\). The cubic Eisenstein field has different exponent \(v_M(3\alpha^2)=3\). The extension \(L/M\) is tame quadratic with different exponent \(1\); the tower formula gives \(2\cdot3+1=7\) again.

## 9. What this lesson does not prove

- The intrinsic motion formula, integral monogenicity, inertia order, subgroup compatibility and cyclotomic lower groups are Proposition 1.1, Section 2 and Proposition 5.1 of **Ramification groups and the different of a local extension**. Its Theorem 3.1 is Hilbert's different formula. Integral uniformizer generation and multiplication of ramification indices are supplied by **Unramified and totally ramified extensions**, Theorem 5.1 and Section 1.
- A Galois group of an algebraic normal separable extension is the inverse limit of its finite Galois quotient groups, with the Krull topology. Compactness of a product of finite discrete spaces is the compact-product theorem. Proposition 4.1 proves the additional compatibility and surjectivity needed for upper groups.
- Hasse–Arf is stated in Section 4 and used only to compare the abelian examples with its conclusion. The exact written internal provider is *Class field theory*, lesson 10, **Abelian ramification, conductors and Hasse–Arf**, Corollary 10.3.
- In the final different check, transitivity means \(\mathfrak D_{L/K}=\mathfrak D_{L/M}\mathfrak D_{M/K}\mathcal O_L\), hence \(d(L/K)=d(L/M)+e(L/M)d(M/K)\). The written programme proof is *Number fields*, lesson 14, **The different and the discriminant**, Proposition 14.1 for finite separable towers over a Dedekind base with finite integral closures. Its Proposition 14.2 proves the derivative formula for a monogenic full integral closure. The ramification filtrations themselves were computed without either tower calculation.

## References
J. S. Milne, [*Algebraic Number Theory*](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Chapter 7, “Ramification groups,” for the lower filtration used here.
