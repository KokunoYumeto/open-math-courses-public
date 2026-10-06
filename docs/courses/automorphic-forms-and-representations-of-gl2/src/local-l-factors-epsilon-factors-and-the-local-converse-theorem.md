# Local L-factors, epsilon factors and the local converse theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Author self-check complete. Public domain (CC0).*

The germs of a Kirillov function determine the possible poles of its Mellin integral. Its Weyl transform determines the functional equation. Dividing by the two pole-removing factors leaves a unit of a Laurent-polynomial ring, which explains why the epsilon factor is a monomial. Finally, Mellin transforms for all character twists recover every Weyl coefficient and hence the representation.

We use the scalar Kirillov model, complete germ descriptions and Weyl formula of Lesson 7, and the normalized newvectors of Lesson 8. The one-dimensional local zeta theory is supplied by [Tate's finite-place lesson](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-ADL/NT-ADL-07.html), Proposition 7.1, Theorems 7.2–7.3 and Proposition 7.4. The companion [infinite-place lesson](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-ADL/NT-ADL-08.html) fixes the archimedean conventions used later in this course.

Let \(F,\mathcal O,\varpi,q\) be as in the preceding local lessons. Set \(\nu=|\cdot|\), \(U=\mathcal O^\times\), \(d(a)=\operatorname{diag}(a,1)\), and \(w_0=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\). Initially \(\psi\) has conductor \(\mathcal O\). Additive measure is self-dual, so \(\operatorname{vol}(\mathcal O)=1\), and multiplicative measure has \(\operatorname{vol}(U)=1\). Thus
\[
\frac{dx}{|x|}=(1-q^{-1})\,d^\times x.
\tag{0.1}
\]
We use the positive Fourier kernel \(\psi(xy)\). Write \(\omega\) for the central character and \(W=\pi(w_0)\) for the operator on the Kirillov space \(V\); \(W^2=\omega(-1)\). Until Section 6, \(\pi\) is irreducible and infinite-dimensional.

For a character \(\mu\), Tate's factors in these conventions obey
\[
Z(\widehat f,1-s,\mu^{-1})
=\gamma(s,\mu,\psi)Z(f,s,\mu),\qquad
Z(f,s,\mu)=\int_{F^\times}f(x)\mu(x)|x|^s\,d^\times x,
\]
\[
\gamma(s,\mu,\psi)=
\epsilon(s,\mu,\psi)\frac{L(1-s,\mu^{-1})}{L(s,\mu)},\qquad
L(s,\mu)=
\begin{cases}
(1-\mu(\varpi)q^{-s})^{-1}&\mu|_U=1,\\
1&\mu|_U\ne1.
\end{cases}
\tag{0.2}
\]
These are imported results, with their Gauss-sum and measure proofs owned by the Tate lesson. That lesson states its finite-place results for finite extensions of \(\mathbb Q_p\). The proofs used in (0.2) depend only on unit quotients, valuation shells, compact character orthogonality and self-dual Fourier inversion; they apply with the same formulas to a local function field. No trace-character or different formula is required when we choose a character of conductor \(\mathcal O\).

## 1. The Mellin ideal and its generator

For a Whittaker function \(\mathcal W\), set
\[
\Psi(g,s,\mathcal W)=
 \int_{F^\times}\mathcal W(d(t)g)|t|^{s-1/2}\,d^\times t.
\tag{1.1}
\]
The notation \(\mathcal W\) distinguishes a function from the Weyl operator \(W\). In the Kirillov model, at \(g=1\), this is
\[
M_s(\xi)=\int_{F^\times}\xi(t)|t|^{s-1/2}\,d^\times t.
\]
Let \(X=q^{-s}\), \(R=\mathbb C[X,X^{-1}]\), and \(E=\mathbb C(X)\).

**Theorem 1.1 — convergence, rationality and the full ideal.** The integrals (1.1) converge absolutely in a common right half-plane and continue rationally in \(X\). Their \(R\)-span is \(L(s,\pi)R\), where
\[
L(s,\pi)=
\begin{cases}
L(s,\mu_1)L(s,\mu_2)&\pi=I(\mu_1,\mu_2)\text{ irreducible},\\
L(s,\chi\nu^{1/2})&\pi=\mathrm{St}_\chi,\ \chi|_U=1,\\
1&\pi=\mathrm{St}_\chi,\ \chi|_U\ne1,\text{ or }\pi\text{ supercuspidal}.
\end{cases}
\tag{1.2}
\]
It is the unique generator of the form \(P(X)^{-1}\) with \(P\) polynomial and \(P(0)=1\).

**Proof.** A Kirillov function is zero on all valuation shells below some integer. Its germ at zero is one of the finite sums described in Lesson 7, Proposition 6.2. Integrating over units eliminates every nontrivial unit character. For a principal germ \(\nu^{1/2}\mu(t)\), the surviving tail, if \(\mu\) is unramified, is a constant times
\[
\sum_{m\geq m_0}(\mu(\varpi)X)^m.
\]
For a special germ \(\nu\chi(t)\) the corresponding ratio is
\(\chi(\varpi)q^{-1/2}X\). For repeated principal parameters the additional valuation factor gives a series \(\sum m(\mu(\varpi)X)^m\), with a squared denominator. Compact functions contribute Laurent polynomials. These calculations prove convergence and rationality. The common half-plane depends on the absolute values of the finitely many germ parameters; a translate by \(g\) changes coefficients and the finite initial part, but its germ remains in the same finite-dimensional germ space.

It remains to show that every asserted denominator occurs in the ideal, rather than merely bounds its poles. Every allowed germ is realized by a function in the full model. Subtracting compact functions lets us choose its tail beginning at valuation zero. For distinct unramified parameters \(\alpha\ne\beta\), the two resulting integrals generate
\[
\frac1{1-\alpha X}R+\frac1{1-\beta X}R
=\frac1{(1-\alpha X)(1-\beta X)}R,
\]
since the two linear factors are relatively prime. If only one parameter is unramified, it gives the single factor. If the parameters coincide and are unramified, the two tails give \(1/(1-\alpha X)\) and \(\alpha X/(1-\alpha X)^2\); together they generate the squared-denominator ideal, since \(\alpha X\) is a unit of \(R\). Ramified unit characters contribute no tail. The special germ gives its single denominator when unramified, and none when ramified. In the supercuspidal case every function is compact.

In every case \(1_U\) has integral one. Dilation through powers of \(\varpi\) multiplies integrals by Laurent monomials, so their span is an \(R\)-module. The preceding generators and pole bounds prove equality with (1.2). Right translation absorbs \(g\), so allowing all \(g\) gives the same ideal. Finally two normalized reciprocal-polynomial generators differ by a unit \(cX^j\); regularity and value one at \(X=0\) force \(j=0,c=1\). \(\square\)

The \(L\)-factor measures the whole family of integrals. A single compact test has integral one even when the representation's \(L\)-factor is nontrivial.

## 2. Identifying the contragredient

**Proposition 2.1.** For every infinite-dimensional irreducible,
\[
\widetilde\pi\simeq\omega^{-1}\otimes\pi.
\tag{2.1}
\]

**Proof for principal and special representations.** The induced duality in Lesson 6 gives inverse principal parameters. Twisting the original parameters by \((\mu_1\mu_2)^{-1}\) gives the inverse parameters in the opposite order; Lesson 7, Corollary 5.2, identifies the two orders. Untwisted Steinberg is self-dual by Lesson 6; twisting gives \(\mathrm{St}_{\chi^{-1}}\), which is also \(\omega^{-1}\mathrm{St}_\chi\) because \(\omega=\chi^2\).

**Proof for supercuspidals.** Here both \(\pi\) and \(\pi'=\omega^{-1}\pi\) have compact Kirillov spaces. Their pointwise pairing
\[
\beta(\xi,\xi')=\int_{F^\times}\xi(t)\xi'(-t)\,d^\times t
\tag{2.2}
\]
is well-defined and nondegenerate. It is invariant under simultaneous upper-triangular action: the unipotent factors at \(t\) and \(-t\) cancel, dilation preserves multiplicative measure, and the central characters are inverse.

We verify the Weyl action as well. Put \(\epsilon=\omega|_U,z=\omega(\varpi)\), and retain the Mellin coefficients of Lesson 7:
\[
\xi_n^\alpha=\int_U\xi(\varpi^nu)\alpha(u)\,du,\qquad
(W\xi)_n^\alpha=\sum_p z^{-p}C_{n+p}^\alpha
                         \xi_p^{\alpha^{-1}\epsilon^{-1}}.
\tag{2.3}
\]
Twisting transports functions by \(\xi'(t)=\omega(t)^{-1}\xi(t)\). Its Weyl coefficients are
\[
(C')_r^\alpha=z^{-r}C_r^{\alpha\epsilon^{-1}}.
\]
Substituting in (2.3) for \(\pi'\) gives
\[
(W'\xi')_n^\alpha
=\sum_p z^{-n}C_{n+p}^{\alpha\epsilon^{-1}}
                             (\xi')_p^{\alpha^{-1}\epsilon}.
\tag{2.4}
\]
Unit Fourier inversion expresses (2.2) as the finite sum
\(\sum_{n,\alpha}\alpha(-1)\xi_n^\alpha(\xi')_n^{\alpha^{-1}}\).
Using (2.3)–(2.4) in this pairing, and replacing the unit character on its second expansion by \(\alpha^{-1}\epsilon^{-1}\), shows
\[
\beta(W\xi,\xi')=\epsilon(-1)\beta(\xi,W'\xi').
\]
All these sums are finite because the functions and their Weyl transforms are compact. Replace \(\xi'\) by \(W'\xi'\). Since \((W')^2=\epsilon(-1)^{-1}\), the result is
\(\beta(W\xi,W'\xi')=\beta(\xi,\xi')\).
Together with upper-triangular invariance this proves \(G\)-invariance.

The pairing maps \(\pi'\) into the smooth contragredient: a compact stabilizer of \(\xi'\), by invariance, fixes its associated functional. Nondegeneracy gives a nonzero injection. The admissible contragredient is irreducible by Lesson 5, so the image is the whole contragredient. \(\square\)

## 3. The functional equation and why epsilon is a monomial

Define the second integral with its central-character twist:
\[
\widetilde\Psi(g,s,\mathcal W)
=\int_{F^\times}\mathcal W(d(t)g)\omega(t)^{-1}
                         |t|^{s-1/2}\,d^\times t.
\tag{3.1}
\]
For \(\mathcal W^\vee(g)=\omega(\det g)^{-1}\mathcal W(g)\), this satisfies
\(\widetilde\Psi(g,s,\mathcal W)
=\omega(\det g)\Psi(g,s,\mathcal W^\vee)\).
The exterior factor matters when \(g\ne1\).

**Lemma 3.1 — generic torus uniqueness.** On \(V_E=V\otimes_{\mathbb C}E\), the space of \(E\)-linear functionals with
\[
\ell(\pi(d(a))v)=|a|^{1/2-s}\ell(v)
\tag{3.2}
\]
has dimension one.

**Proof.** On \(V_0=C_c^\infty(F^\times)\), invariance under \(d(U)\) lets us average each function over units. This is a finite sum for each smooth vector. The resulting functions are finite linear combinations of shell indicators. Their values under \(\ell\) are all determined by \(\ell(1_U)\), since a shell indicator is a uniformizer translate. Thus restriction to \((V_0)_E\) has dimension at most one.

A functional with zero restriction factors through the finite-dimensional germ quotient \((V/V_0)_E\). Let \(P(T)\in\mathbb C[T]\) annihilate the operator \(d(\varpi)\) on this quotient. Condition (3.2) gives
\[
P(q^{-1/2}X^{-1})\ell=0.
\]
This scalar is nonzero in \(E\), since \(X\) is an indeterminate and \(P\) is a nonzero polynomial. Hence \(\ell=0\); restriction is injective. The rationally continued \(M_s\) is a nonzero functional satisfying (3.2), with \(M_s(1_U)=1\). This proves the claim. \(\square\)

These functionals have torus equivariance. Applying the one-dimensional Whittaker-functional theorem to them directly would not prove this lemma.

**Theorem 3.2 — local functional equation.** There is a unique nonzero monomial
\(\epsilon(s,\pi,\psi)=bX^a\), with \(b\in\mathbb C^\times,a\in\mathbb Z\), such that
\[
\frac{\widetilde\Psi(w_0g,1-s,\mathcal W)}
     {L(1-s,\widetilde\pi)}
=\epsilon(s,\pi,\psi)
 \frac{\Psi(g,s,\mathcal W)}{L(s,\pi)}.
\tag{3.3}
\]
All assertions are identities of rational continuations. Put
\[
\gamma(s,\pi,\psi)=
\epsilon(s,\pi,\psi)\frac{L(1-s,\widetilde\pi)}{L(s,\pi)}.
\tag{3.4}
\]

**Proof.** At \(g=1\), its unnormalized left functional is
\[
D_s(\xi)=\int_{F^\times}(W\xi)(t)\omega(t)^{-1}
                            |t|^{1/2-s}\,d^\times t.
\]
It is rational by Theorem 1.1 and Proposition 2.1. The relation
\(Wd(a)=\omega(a)d(a^{-1})W\) and a multiplicative change of variable give
\[
D_s(\pi(d(a))\xi)=|a|^{1/2-s}D_s(\xi).
\]
Lemma 3.1 therefore gives \(D_s=\gamma M_s\), for a rational \(\gamma\). It is nonzero: \(W\) is onto, and the twisted Mellin integral has a nonzero image.

More precisely, the image of \(D_s\), as an \(R\)-module, is \(L(1-s,\widetilde\pi)R\). The map \(\xi\mapsto\omega^{-1}\xi\) realizes the twisted representation, while \(W\) is onto; Theorem 1.1 applies to all its functions. The image of \(\gamma M_s\) is \(\gamma L(s,\pi)R\). Equality of these images shows that
\[
\epsilon=\frac{\gamma L(s,\pi)}{L(1-s,\widetilde\pi)}
\]
generates \(R\) itself. The units of \(R\) are exactly \(bX^a\): in a product equal to one the highest and lowest exponents must coincide. This proves the monomial assertion. Replacing \(\xi\) by \(\pi(g)\xi\) proves (3.3) for every \(g\). Nonzero \(M_s\) proves uniqueness. \(\square\)

The normalized integrals in (3.3) are Laurent polynomials, so they are entire as functions of \(s\). The unnormalized integrals can have poles. The proof distinguishes these two assertions.


## 4. Principal and special factors, including the sign

**Theorem 4.1 — the two character factors.** For an irreducible principal series,
\[
\gamma(s,I(\mu_1,\mu_2),\psi)
 =\gamma(s,\mu_1,\psi)\gamma(s,\mu_2,\psi),\qquad
\epsilon(s,I(\mu_1,\mu_2),\psi)
 =\epsilon(s,\mu_1,\psi)\epsilon(s,\mu_2,\psi).
\tag{4.1}
\]

**Proof.** We derive the identity from the Weyl kernel already proved in Lesson 7, Proposition 5.1. Put \(C=1-q^{-1}\), \(r=\mu_1/\mu_2\). For a locally constant compactly supported function \(\Phi\) on \(F^2\), whose support avoids both coordinate axes, define
\[
\xi_\Phi(t)=|t|^{1/2}
 \int_{F^\times}\mu_1(u)\mu_2(t/u)\Phi(u,t/u)\,d^\times u.
\tag{4.2}
\]
This function is compactly supported in \(F^\times\). The substitution \(t=uv\) gives
\[
M_s(\xi_\Phi)=
 \int_{(F^\times)^2}\Phi(u,v)\mu_1(u)\mu_2(v)
                       |uv|^s\,d^\times u\,d^\times v.
\tag{4.3}
\]
For a tensor \(\Phi=f_1\otimes f_2\), this is the product of the two Tate integrals.

Use self-dual additive measure to put
\[
\widehat\Phi(x,y)=\int_{F^2}\Phi(u,v)\psi(xu+yv)\,du\,dv,
\qquad \widehat\Phi^{\,\mathrm{sw}}(x,y)=\widehat\Phi(y,x).
\]
We claim that
\[
W\xi_\Phi=\xi_{\widehat\Phi^{\,\mathrm{sw}}},
\tag{4.4}
\]
where the right side uses (4.2), without an assumption that its input avoids the axes. For each fixed \(t\ne0\), that integral is still over a compact annulus: compact support of \(\widehat\Phi\) bounds both \(x\) and \(t/x\).

Here is the measure calculation proving the claim. Substituting (4.2) into the kernel of Lesson 7, and then putting its integration variable \(s=uv\), gives
\[
(W\xi_\Phi)(t)
 =C|t|^{1/2}\mu_2(t)
   \int\Phi(u,v)|uv|\,r(v)^{-1}J_r(tuv)
                  \,d^\times u\,d^\times v
 =\frac{|t|^{1/2}\mu_2(t)}{C}
   \int\Phi(u,v)r(v)^{-1}J_r(tuv)\,du\,dv.
\tag{4.5}
\]
The second equality uses \(du\,dv=C^2|uv|\,d^\times u\,d^\times v\). On the other hand, inserting the Fourier integral into the right side of (4.4) yields
\[
\frac{|t|^{1/2}\mu_2(t)}{C}
 \int\Phi(u,v)
   \left(\int_{F^\times}^{\mathrm{st}}
       r(x)\psi(tu/x+xv)\frac{dx}{|x|}\right)\,du\,dv.
\]
With \(y=xv\), the parenthesized integral is \(r(v)^{-1}J_r(tuv)\), proving (4.5).

These interchanges take place first over finite valuation annuli. The support of \(\Phi\) bounds \(u,v\) away from zero and infinity. For fixed \(t\ne0\), the stable shell bounds for \(J_r(tuv)\), proved in Lesson 7, can therefore be chosen uniformly on that support. Increasing the annuli leaves (4.5) unchanged. The Fourier-side integral also stabilizes, by its compact-annulus observation. This justifies (4.4) without an interchange of absolutely divergent oscillatory integrals.

Now substitute \(t=xy\) in \(D_s(\xi_\Phi)\). The swap in (4.4) and \(\omega=\mu_1\mu_2\) give
\[
D_s(\xi_\Phi)=
 \int_{(F^\times)^2}\widehat\Phi(u,v)
       \mu_1(u)^{-1}\mu_2(v)^{-1}|uv|^{1-s}
                            \,d^\times u\,d^\times v.
\tag{4.6}
\]
For a tensor \(\Phi\), apply the two Tate functional equations to (4.3) and (4.6). Their rational continuations give
\[
D_s(\xi_\Phi)=
 \gamma(s,\mu_1,\psi)\gamma(s,\mu_2,\psi)M_s(\xi_\Phi).
\]
There is a nonzero test of this kind: choose
\(f_i=\mu_i^{-1}1_U\). Then \(\xi_\Phi=1_U\) and \(M_s(\xi_\Phi)=1\).
The uniqueness of \(\gamma\) in Theorem 3.2 proves its product formula. The \(L\)-factor and contragredient formulas in Sections 1–2 then cancel the two character \(L\)-ratios, proving the epsilon formula. \(\square\)

The same compact-function calculation also applies to
\(I(\chi\nu^{1/2},\chi\nu^{-1/2})\). Its parameter ratio is \(\nu\), so the injectivity hypothesis of Lesson 7, Proposition 5.1, holds. Its Steinberg subrepresentation contains the compact Kirillov part. Thus it gives the gamma factor of \(\mathrm{St}_\chi\), even though this induced representation is reducible.

**Corollary 4.2 — the special factors.** Write \(A=\chi(\varpi)\). If \(\chi\) is unramified, then
\[
L(s,\mathrm{St}_\chi)=(1-Aq^{-s-1/2})^{-1},
\qquad
\epsilon(s,\mathrm{St}_\chi,\psi)=-Aq^{1/2-s}.
\tag{4.7}
\]
If \(\chi\) is ramified, then
\[
L(s,\mathrm{St}_\chi)=1,\qquad
\epsilon(s,\mathrm{St}_\chi,\psi)=\epsilon(s,\chi,\psi)^2.
\tag{4.8}
\]

**Proof.** The gamma factor, by the calculation just explained, is
\[
\gamma(s,\chi\nu^{1/2},\psi)
 \gamma(s,\chi\nu^{-1/2},\psi).
\]
For unramified \(\chi\), each character epsilon is one. The factor
\(L(s,\chi\nu^{1/2})\) cancels against the Steinberg \(L\)-factor, and
\(L(1-s,\chi^{-1}\nu^{1/2})\) cancels against its dual factor. The remaining ratio is
\[
\epsilon(s,\mathrm{St}_\chi,\psi)
 =\frac{L(1-s,\chi^{-1}\nu^{-1/2})}
        {L(s,\chi\nu^{-1/2})}
 =\frac{1-Aq^{1/2}X}{1-A^{-1}q^{-1/2}X^{-1}}
 =-Aq^{1/2}X.
\tag{4.9}
\]
The last equality is an identity of rational functions; it remains valid at points where numerator and denominator vanish.

If \(\chi\) is ramified, all four character \(L\)-factors are one. The epsilon product is
\(\epsilon(s+1/2,\chi,\psi)\epsilon(s-1/2,\chi,\psi)\).
Tate's monomial formula shows that the two shifts cancel in this product, giving \(\epsilon(s,\chi,\psi)^2\). \(\square\)

For completeness the imported ramified character formula can make (4.8) numerical. If \(a=a(\chi)\geq1\), let
\[
\tau(\chi^{-1},\psi,\varpi^a)
 =\sum_{u\in U/(1+\mathfrak p^a)}
          \chi(u)^{-1}\psi(u/\varpi^a).
\]
Tate's finite-place Theorem 7.3, in our conductor-\(\mathcal O\) convention, gives
\[
\epsilon(s,\chi,\psi)
 =\chi(\varpi)^a q^{-as}\tau(\chi^{-1},\psi,\varpi^a).
\tag{4.10}
\]
Thus the ramified special epsilon is the square of the right side. The Gauss-sum evaluation and its norm are supplied by that theorem.

## 5. Supercuspidal factors and the exact conductor exponent

**Theorem 5.1.** Let \(c=c(\pi)\) be the conductor of Lesson 8 and keep \(\psi\) of conductor \(\mathcal O\). For every infinite-dimensional irreducible,
\[
\epsilon(s,\pi,\psi)
 =\epsilon(1/2,\pi,\psi)\,q^{c(1/2-s)}.
\tag{5.1}
\]
For a supercuspidal, \(L(s,\pi)=1\), and its constant in (5.1) is obtained from the Weyl transform of its normalized newfunction.

**Proof for principal and special representations.** For a character, (4.10) has exponent \(a(\chi)\); an unramified character has exponent zero. The product formula (4.1) therefore has exponent \(a(\mu_1)+a(\mu_2)\), exactly the principal conductor of Lesson 8. Formula (4.7) has exponent one. Formula (4.8) has exponent \(2a(\chi)\). These are exactly the two special conductors proved there.

**Proof for supercuspidals.** Lesson 8 proves \(c\geq2\) and that the normalized newfunction is \(1_U\). Write \(\epsilon_U=\omega|_U\), \(z=\omega(\varpi)\), and
\[
Y_c=\{v:\pi(k)v=\omega(a_k)v,\ k\in K_0(c)\},
\qquad w_c=w_0d(\varpi^c).
\]
The identity
\[
w_c\begin{pmatrix}a&b\\r&d\end{pmatrix}w_c^{-1}
 =\begin{pmatrix}d&-r/\varpi^c\\-\varpi^c b&a\end{pmatrix}
\]
shows that \(w_c\) normalizes \(K_0(c)\) and exchanges its diagonal characters. By Lesson 8, Sections 1–2, the \(K_0(c)\)-space with character \(\omega(d_k)\) is the newvector line. Hence \(\pi(w_c)\) carries that line onto the line \(Y_c\).

A function \(\eta\) in \(Y_c\) is supported in \(\mathcal O\), because \(n(\mathcal O)\) fixes it. It obeys
\(\eta(ut)=\epsilon_U(u)\eta(t)\).
The one-step operator of Lesson 8, Lemma 4.1, preserves \(Y_c\), so on this line it has a scalar \(B\) and gives
\(\eta(\varpi^{m+1})=B\eta(\varpi^m)\) for \(m\geq0\).
Every supercuspidal function is compact away from zero. If \(\eta(1)=0\), the recurrence would make \(\eta\) identically zero; and if \(B\ne0\), it would give infinitely many nonzero shells. Consequently \(B=0\), and the normalized function of \(Y_c\) is \(\epsilon_U1_U\).

Use \(w_c=\varpi^c I\,d(\varpi^{-c})w_0\). There is therefore a constant \(k_\pi\ne0\) such that
\[
(W1_U)(\varpi^m u)=
 \begin{cases}
 k_\pi\epsilon_U(u)&m=-c,\\
 0&m\ne-c.
 \end{cases}
\tag{5.2}
\]
Since \(M_s(1_U)=1\), its functional equation computes gamma directly:
\[
\gamma(s,\pi,\psi)
 =\int(W1_U)(t)\omega(t)^{-1}|t|^{1/2-s}\,d^\times t
 =k_\pi z^c q^{c(1/2-s)}.
\tag{5.3}
\]
Both \(L\)-factors are one, so gamma equals epsilon. At \(s=1/2\) its value is \(k_\pi z^c\). This proves (5.1) in the remaining case. \(\square\)

Thus the conductor equality for supercuspidals follows here from the newvector and Weyl arguments already proved in Lesson 8. No additional conductor theorem is needed as an unproved input. The constant \(k_\pi z^c\) depends on the representation and its additive character; a conductor alone does not specify it.

The formulas can now be read together.

| Representation | \(L(s,\pi)\) | \(\epsilon(s,\pi,\psi)\), for conductor-\(\mathcal O\) \(\psi\) |
|---|---|---|
| Irreducible \(I(\mu_1,\mu_2)\) | \(L(s,\mu_1)L(s,\mu_2)\) | \(\epsilon(s,\mu_1,\psi)\epsilon(s,\mu_2,\psi)\) |
| \(\mathrm{St}_\chi\), \(\chi\) unramified | \((1-\chi(\varpi)q^{-s-1/2})^{-1}\) | \(-\chi(\varpi)q^{1/2-s}\) |
| \(\mathrm{St}_\chi\), \(\chi\) ramified | \(1\) | \(\epsilon(s,\chi,\psi)^2\) |
| Supercuspidal of conductor \(c\) | \(1\) | \(k_\pi\omega(\varpi)^c q^{c(1/2-s)}\), with \(k_\pi\) defined by (5.2) |

In particular, the last row is an explicit extraction of the factor from the representation's Weyl action. It does not assert a universal constant for all supercuspidals with the same conductor.


## 6. Changing the additive character

**Proposition 6.1.** Put \(\psi_a(x)=\psi(ax)\), for \(a\in F^\times\). The \(L\)-factor is independent of this change, and
\[
\epsilon(s,\pi,\psi_a)
 =\omega(a)|a|^{2s-1}\epsilon(s,\pi,\psi).
\tag{6.1}
\]

**Proof.** Transport the Whittaker functions by
\(\mathcal W_a(g)=\mathcal W(d(a)g)\).
Indeed \(d(a)n(x)=n(ax)d(a)\), so this has Whittaker character \(\psi_a\).
Changing \(t\) to \(at\) in (1.1) gives
\[
\Psi(g,s,\mathcal W_a)=|a|^{1/2-s}\Psi(g,s,\mathcal W).
\tag{6.2}
\]
The multiplier is a nonzero constant times a Laurent monomial in \(X\); hence it does not change the Mellin ideal or its normalized generator. In the twisted integral,
\[
\widetilde\Psi(g,s,\mathcal W_a)
 =\omega(a)|a|^{1/2-s}\widetilde\Psi(g,s,\mathcal W).
\tag{6.3}
\]
Insert (6.2)–(6.3) into the functional equation, using \(1-s\) on its left. The ratio of the two multipliers is \(\omega(a)|a|^{2s-1}\). Uniqueness in Theorem 3.2 proves (6.1). \(\square\)

The self-dual additive measure for \(\psi_a\) is \(|a|^{1/2}dx\). For example, Fourier transformation with that measure is
\(\widehat f^{\,a}(y)=|a|^{1/2}\widehat f(ay)\); applying it twice gives \(f(-y)\).
Our multiplicative measure remains normalized by \(\operatorname{vol}(U)=1\).
It would be incorrect to replace (0.1) by its conductor-\(\mathcal O\) constant after changing the additive measure without accounting for this factor.

If \(v_F(a)=\ell\), then the largest fractional ideal on which \(\psi_a\) is trivial is \(\varpi^{-\ell}\mathcal O\). Combining (5.1) and (6.1) gives
\[
\epsilon(s,\pi,\psi_a)
 =\omega(a)\epsilon(1/2,\pi,\psi)
       q^{(c+2\ell)(1/2-s)}.
\tag{6.4}
\]
In particular a changed additive character can give a negative exponent; \(c\) itself is still a nonnegative representation conductor.

## 7. Recovering the representation from all twists

**Theorem 7.1 — local converse for \(\mathrm{GL}_2\).** Let \(\pi,\pi'\) be infinite-dimensional irreducibles with the same central character \(\omega\). If
\[
\gamma(s,\pi\otimes\chi,\psi)
 =\gamma(s,\pi'\otimes\chi,\psi)
\tag{7.1}
\]
for every smooth quasicharacter \(\chi:F^\times\to\mathbb C^\times\), then \(\pi\simeq\pi'\).
Here \(\chi\) acts through the determinant, and gamma means the ratio in (3.4).

**Proof.** Put the two representations in their scalar Kirillov models. Their upper-triangular actions agree, because these depend only on \(\psi,\omega\). It remains to recover the Weyl action on their common compact part \(V_0=C_c^\infty(F^\times)\).

The map carrying the model of \(\pi\) to that of \(\pi\otimes\chi\) is
\[
T_\chi\xi(t)=\chi(t)\xi(t).
\]
Since \(\det w_0=1\), its Weyl transform satisfies
\(W_\chi T_\chi\xi(t)=\chi(t)W\xi(t)\).
The central character of the twist is \(\omega\chi^2\). Consequently its functional equation reads
\[
\int(W\xi)(t)\omega(t)^{-1}\chi(t)^{-1}|t|^{1/2-s}\,d^\times t
 =\gamma(s,\pi\otimes\chi,\psi)
     \int\xi(t)\chi(t)|t|^{s-1/2}\,d^\times t.
\tag{7.2}
\]

Write \(\epsilon_U=\omega|_U,z=\omega(\varpi)\), and let \(\alpha\) be any smooth character of \(U\). Choose the extension \(\chi\) with
\(\chi|_U=(\alpha\epsilon_U)^{-1}\) and \(\chi(\varpi)=1\).
Take \(\xi=(\alpha\epsilon_U)1_U\). The right integral in (7.2) equals one. Formula (2.3), with the input supported on shell zero, says
\[
(W\xi)_n^\alpha=C_n^\alpha.
\]
Thus (7.2) recovers the full generating function
\[
\gamma(s,\pi\otimes\chi,\psi)
 =\sum_n C_n^\alpha
       \bigl(z^{-1}q^{s-1/2}\bigr)^n
 =C^\alpha\bigl(z^{-1}q^{s-1/2}\bigr).
\tag{7.3}
\]
The sum has a lower bound on \(n\). It converges in a suitable left half-plane, since it is the dual Mellin integral in (7.2), and is the expansion at zero of the rational function \(C^\alpha(Z)\). This rationality also follows from the full germ description in Lesson 7.

For \(\pi'\) the same test gives its corresponding \(C'^\alpha\), with the same variable \(Z=z^{-1}q^{s-1/2}\). Hypothesis (7.1) makes the rational functions equal. A rational function with a lower-bounded Laurent expansion at zero has a unique such expansion. Therefore \(C_n^\alpha=C_n'^\alpha\) for every \(n,\alpha\).

Unit Fourier inversion and (2.3) now show that \(W\) and \(W'\) agree on every compact function: such a function has finitely many shells and finitely many unit characters. Lesson 7, Theorem 2.3, gives
\[
V=V_0+WV_0,\qquad V'=V_0+W'V_0.
\]
The two function spaces are therefore equal. On \(\xi_0+W\xi_1\), with \(\xi_i\in V_0\), both Weyl operators act as
\(W\xi_0+\omega(-1)\xi_1\).
Their upper-triangular actions also agree, so they agree on the generators of \(G\). The identity on this common function space is the required intertwining isomorphism. \(\square\)

The proof actually used only characters with prescribed unit restriction and value one at \(\varpi\). The variable \(s\) probes the uniformizer direction. Equality of untwisted \(L\)-factors alone supplies none of this unit-character information.

## 8. Matrix zeta integrals and the finite-dimensional case

The matrix construction supplies the factors of the nongeneric determinant characters and gives a second construction of the generic factors. We prove the comparison, including supercuspidals and the exceptional induced representation.

Let \(\Phi\in\mathcal S(M_2(F))\), and write
\(c_{v,\ell}(g)=\ell(\pi(g)v)\), with \(\ell\) in the smooth contragredient. Put
\[
dg=\frac{d^4g}{|\det g|^2},\qquad
Z_{\rm mat}(s,\Phi,c)=
 \int_G\Phi(g)c(g)|\det g|^{s+1/2}\,dg,
\qquad
\widehat\Phi(X)=\int_{M_2(F)}\Phi(Y)\psi(\operatorname{tr}(XY))\,d^4Y.
\tag{8.1}
\]
Thus \(\check c(g)=c(g^{-1})\) is a contragredient coefficient. The common normalization of the two group integrals has no effect on their functional-equation factor.

**Theorem 8.1 — full matrix comparison.** For every irreducible smooth representation of \(\mathrm{GL}_2(F)\), the matrix integrals converge in a right half-plane, continue rationally in \(X=q^{-s}\), and span \(L(s,\pi)R\). For the infinite-dimensional representations this is exactly the factor of Theorem 1.1, and
\[
Z_{\rm mat}(1-s,\widehat\Phi,\check c)
 =\gamma(s,\pi,\psi)Z_{\rm mat}(s,\Phi,c).
\tag{8.2}
\]
For \(D_\chi(g)=\chi(\det g)\), their factors are
\[
L(s,D_\chi)=L(s,\chi\nu^{1/2})L(s,\chi\nu^{-1/2}),\qquad
\epsilon(s,D_\chi,\psi)
 =\epsilon(s+1/2,\chi,\psi)\epsilon(s-1/2,\chi,\psi).
\tag{8.3}
\]
The assertions concern the whole matrix-integral family, rather than just a selected nonzero test.

### 8.1. A two-character kernel

We first record a calculation that also works over \(\mathbb R\) and \(\mathbb C\), using their self-dual additive measures and the Tate factors of NT-ADL-08. In this paragraph alone, \(F\) can be any of these local fields. Write \(K\) for its standard maximal compact group and normalize \(dk\) to mass one. For normalized induction \(I(\mu_1,\mu_2)\), its compact dual pairing is
\[
\langle f,\widetilde f\rangle=\int_K f(k)\widetilde f(k)\,dk.
\]
Define
\[
\phi_{\Phi;h,k}(a,b)=
 \int_F\Phi\left(h^{-1}
 \begin{pmatrix}a&x\\0&b\end{pmatrix}k\right)\,dx,\qquad
\mathcal K_\Phi(h,k;s)=
 \int_{(F^\times)^2}\phi_{\Phi;h,k}(a,b)
       \mu_1(a)\mu_2(b)|ab|^s\,d^\times a\,d^\times b.
\tag{8.4}
\]
The map \(\Phi\mapsto\phi_{\Phi;h,k}\) maps Schwartz functions continuously to Schwartz functions.

**Lemma 8.2 — induction, Fourier transform and pole bounds.** For a positive constant \(\kappa_F\), depending only on the measures,
\[
Z_{\rm mat}(s,\Phi,c_{f,\widetilde f})
 =\kappa_F\int_{K\times K}\mathcal K_\Phi(h,k;s)
                    \widetilde f(h)f(k)\,dh\,dk.
\tag{8.5}
\]
The matrix functional equation for this induced representation has factor
\(\gamma(s,\mu_1,\psi)\gamma(s,\mu_2,\psi)\). Every integral divided by
\(L(s,\mu_1)L(s,\mu_2)\) is entire; in the nonarchimedean case it belongs to \(R\). There is a finite sum of coefficient integrals equal to this product of \(L\)-factors times a nonzero constant in the nonarchimedean case, or a nonzero exponential in \(s\) in the archimedean case.

**Proof.** The precise upper-triangular Iwasawa measure is
\[
dg=\kappa_F |a|^{-1}\,d^\times a\,d^\times b\,dx\,dk
\quad\text{for }g=\begin{pmatrix}a&x\\0&b\end{pmatrix}k.
\tag{8.6}
\]
One can obtain it directly by first decomposing the bottom row as \(b\) times a compact unit row. Its additive polar measure contributes \(|b|^2d^\times b\); decomposing the top row in the corresponding compact row basis contributes \(da\,dx\), with \(da\) a constant times \(|a|d^\times a\). Division by \(|ab|^2\) gives (8.6). For the present finite-place normalization,
\(\kappa_F=\operatorname{vol}(K)=(1-q^{-1})(1-q^{-2})\): the two columns of an integral matrix are independent modulo \(\mathfrak p\) with this additive probability.

In the coefficient integral, substitute \(g\mapsto h^{-1}g\) inside
\(\int_K f(hg)\widetilde f(h)\,dh\), and use (8.6). The inducing factor
\(\mu_1(a)\mu_2(b)|a/b|^{1/2}\), the determinant power
\(|ab|^{s+1/2}\), and the measure factor \(|a|^{-1}\) leave exactly
\(\mu_1(a)\mu_2(b)|ab|^s\). This proves (8.5). Absolute values give the same calculation in a sufficiently far right half-plane; compact \(h,k\) give uniform Schwartz seminorm bounds.

There is no extra Weyl sign in the Fourier step:
\[
\phi_{\widehat\Phi;e,e}=\widehat{\phi_{\Phi;e,e}}.
\tag{8.7}
\]
Indeed, the trace pairing between matrices with entries \((a,x,y,b)\) and \((A,X,Y,B)\) is \(Aa+Xy+Yx+Bb\). Integrating the Fourier transform on \(Y=0\) over \(X\) sets \(y=0\) by additive Fourier inversion. What remains is the two-variable transform of \(\int\Phi(a,x,0,b)\,dx\). This argument is an identity of Schwartz functions; using partial Fourier transforms justifies the integrations also at the infinite places.

For \(h,k\in K\), Fourier transform changes
\(\Phi(h^{-1}Yk)\) to \(\widehat\Phi(k^{-1}Yh)\). Apply the two Tate functional equations to (8.4), and then interchange \(h,k\) in (8.5) for the contragredient. This proves the product gamma factor.

Here are the details that pass from pointwise kernels to whole families. Project \(\Phi\) on the left and right compact types of the two fixed vectors. The coefficient integral is unchanged. Fourier transform interchanges these projections, so the dual integral is unchanged too. The projected kernel lies in one finite-dimensional space of functions on \(K\times K\), independent of \(s\). Evaluation at finitely many points spans its dual: if all evaluations annihilated a function, that function would be zero. Its integral against \(\widetilde f(h)f(k)\) is consequently a finite linear combination of evaluated two-variable Tate integrals. Their normalized holomorphy, or Laurent-polynomial property, proves the bound asserted in the lemma.

For the reverse inclusion, take a tensor of the two fundamental Tate tests, and extend it to a matrix Schwartz function by
\(\Phi(a,x,y,b)=\phi(a,b)\eta(x)\eta_0(y)\), with
\(\int\eta=1,\eta_0(0)=1\). In the archimedean case these may be Gaussian polynomials. Thus \(\phi_{\Phi;e,e}=\phi\). The compact covariance of (8.4) puts its \(h\)-variable in the compact model of \(I(\mu_1,\mu_2)\) and its \(k\)-variable in the inverse-character model. Nondegeneracy of compact duality on the finite type spaces therefore writes evaluation at \((e,e)\) as a finite sum of integrals against \(\widetilde f(h)f(k)\). Explicitly, choose bases in those two finite spaces and their pairing-dual bases; expand the two evaluation functionals in these bases and take their tensor product. Formula (8.5) realizes that sum as coefficient integrals. The fundamental Tate tests give the asserted normalized nonzero constant or exponential. \(\square\)

If \(\pi\) is a subquotient of this induction, every coefficient of \(\pi\) is a coefficient of the induction. For a subrepresentation, extend a smooth functional by applying a compact average and extending on its finite fixed space; for a quotient, lift the vector and use its annihilating dual functional. The exact compact averages of Lesson 5 justify both operations. Thus the functional equation and product pole bound pass to every constituent. For an irreducible principal series, Lemma 8.2 already proves its full ideal and agrees with Section 4.

For \(D_\chi\), use
\(I(\chi\nu^{-1/2},\chi\nu^{1/2})\): the section \(f(g)=\chi(\det g)\) is its one-dimensional subrepresentation. The lemma proves (8.2) with the product gamma, hence (8.3). If \(\chi\) is unramified, take \(\Phi=1_{M_2(\mathcal O)}\). Its kernel is constant on \(K\times K\), and its diagonal marginal is \(1_{\mathcal O}\otimes1_{\mathcal O}\). Pairing \(f|_K=1\) with the constant dual compact section gives exactly
\[
Z_{\rm mat}(s,1_{M_2(\mathcal O)},D_\chi)
 =\kappa_F L(s,\chi\nu^{-1/2})L(s,\chi\nu^{1/2}).
\tag{8.8}
\]
If \(\chi\) is ramified, its product \(L\)-factor is one. The Schwartz function equal to \(\chi(\det g)^{-1}\) on \(K\) and zero elsewhere gives the constant \(\kappa_F\). These tests and the pole bound prove the full ideal.

### 8.2. Removing the extra Steinberg pole

For \(\mathrm{St}_\chi\), realize it as the subrepresentation of
\(I_+=I(\chi\nu^{1/2},\chi\nu^{-1/2})\). Its product gamma in Lemma 8.2 is the gamma already proved in Corollary 4.2. The possible product \(L\)-bound still has one unnecessary factor when \(\chi\) is unramified.

**Lemma 8.3 — the Steinberg matrix ideal.** Its actual matrix ideal is
\(L(s,\mathrm{St}_\chi)R\).

**Proof.** If \(\chi\) is ramified, the product bound is already \(R\). Choose a coefficient nonzero at some point of \(K\) and a sufficiently small compact open test supported there; its integral is a nonzero constant. This proves equality.

Suppose \(\chi\) is unramified, and put \(A=\chi(\varpi)\). The compact model of \(\mathrm{St}_\chi\) is the mean-zero subspace of \(I_+|_K\); in particular its \(K\)-average is zero. If \(J\subset K\) fixes \(v\), the compact kernel \(e_J-e_K\) fixes \(v\) and has integral zero. Average \(\Phi\) on the right with this kernel. For every \(h,k\in K\), the resulting marginal \(\phi=\phi_{\Phi;h,k}\) satisfies
\[
\int_F\phi(a,0)\,da=0.
\tag{8.9}
\]
To verify it, write the integral as the additive integral of \(\Phi\) on
\(h^{-1}\left(\begin{smallmatrix}a&x\\0&0\end{smallmatrix}\right)k\).
Right multiplication by an element of \(K\) preserves the additive measure of this row plane. Its inner integral is therefore constant under the compact averaging, and the averaging kernel has mass zero.

The product Tate bound has possible denominator
\((1-Aq^{-1/2}X)(1-Aq^{1/2}X)\). At the pole
\(Aq^{1/2}X=1\), the residue of the second Tate variable is a constant times the first-variable integral of \(\phi(a,0)\). At this value the first-variable character times \(|a|^s\) is exactly \(|a|\); hence this residue is
\((1-q^{-1})^{-1}\int\phi(a,0)\,da=0\).
For clarity, the residue assertion follows by cutting the second variable into a sufficiently small ball, on which the Schwartz function is \(\phi(a,0)\), and its compact complement. The ball gives a geometric series; the complement is Laurent polynomial. Thus the numerator is divisible by \(1-Aq^{1/2}X\). Only the Steinberg factor remains.

We exhibit a test that attains it. Set
\[
\phi_0=1_{\mathcal O},\quad \phi_1=1_{\mathcal O}-q1_{\varpi\mathcal O},\qquad
\Phi\begin{pmatrix}a&b\\c&d\end{pmatrix}
 =\phi_1(a)\phi_0(b)\phi_0(c)\phi_0(d).
\tag{8.10}
\]
Then \(\int\phi_1=0\), and
\[
\mathcal K_\Phi(e,e;s)
 =\frac{1-qAq^{-1/2}X}
        {(1-Aq^{-1/2}X)(1-Aq^{1/2}X)}
 =L(s,\mathrm{St}_\chi).
\tag{8.11}
\]
The kernel factors through the finite set
\((B\cap K)\backslash K/K_1\), of size \(q+1\). Its representatives are \(e\) and \(w_0n(x)\), with \(x\) modulo \(\mathfrak p\). For those latter representatives,
\(\mathcal K_\Phi(e,w_0n(x);s)=0\). Indeed its marginal contains
\[
1_{\mathcal O}(b)1_{\mathcal O}(bx)
 \int_{\mathcal O}\phi_1(y)1_{\mathcal O}(a-xy)\,dy=0:
\]
on the indicated support \(x,y\in\mathcal O\), the last characteristic function is independent of \(y\).

Choose a compact induced section \(f\) taking value \(1\) at \(e\) and value \(-1/q\) at each of the other \(q\) representatives. It has mean zero, so belongs to Steinberg. Pair it with the dual section supported on the \(e\) representative. Formula (8.5) now gives a nonzero constant times (8.11). This proves the reverse ideal inclusion. \(\square\)

### 8.3. A supercuspidal Fourier calculation

The remaining representation has compact coefficients modulo the centre, by Lesson 6, and its Kirillov space is \(\mathcal S(F^\times)\). Write
\[
C=1-q^{-1},\quad \omega(\varpi)=z,\quad \omega|_U=\epsilon_U,\qquad
\langle v,u\rangle=\int_{F^\times}v(t)u(-t)\,d^\times t.
\]
Here \(u\) realizes the contragredient as in Proposition 2.1.

**Lemma 8.4 — matrix transform on compact Kirillov tests.** For
\(\phi,v,u\in\mathcal S(F^\times)\), define on invertible matrices
\[
\Phi_{\phi,v,u}(g)
 =\phi(\det g)|\det g|^{-1}\langle v,\widetilde\pi(g)u\rangle
\]
and set it to zero on singular matrices. It is a matrix Schwartz function, and
\[
\widehat\Phi_{\phi,v,u}(g)
 =(W\phi)(\det g)|\det g|^{-1}\omega(\det g)^{-1}
                          \langle\pi(g)v,u\rangle
\tag{8.12}
\]
on \(G\), with zero value on singular matrices.

**Proof.** Compactness modulo the centre of the coefficient, and the compact annulus supporting \(\phi\), make the support a compact subset of \(G\). Its extension is consequently Schwartz. Its averages along every left-right translate of \(N\) vanish: these are coefficient averages of a sufficiently large compact subgroup of \(N\), and the ordinary Jacquet module is zero.

We check that Fourier transform still vanishes on the singular matrices. By left-right changes of variables it suffices to check
\(\operatorname{diag}(a,0)\), including \(a=0\). The phase there depends on the upper-left entry and is constant under right multiplication by \(n(x)\); averaging \(\Phi\) on these compactly supported orbits gives zero. Fourier inversion in the lower-left entry also gives
\[
\int_F\widehat\Phi(n(x))\,dx
 =\int_{F^3}\Phi\begin{pmatrix}a&b\\0&d\end{pmatrix}
                  \psi(a+d)\,da\,db\,dd=0.
\tag{8.13}
\]
The last integral vanishes by the original unipotent-average condition; matrices with \(ad=0\) form an additive null set. The same applies after arbitrary left-right changes of variables. These uses of Fourier inversion are partial Schwartz Fourier identities, so require no divergent Fubini interchange.

It remains to compute \(\widehat\Phi(e)\). We give the shell calculation, including its constants. It suffices to take \(v,u,\phi\) supported on
\(\varpi^mU,\varpi^nU,\varpi^lU\), with values there respectively
\(\alpha^{-1},\beta^{-1},\gamma^{-1}\) on the unit argument. Such functions span all three spaces. Put
\[
H_\delta(x)=\int_U\delta(\eta)\psi(\eta x)\,d\eta.
\]
Unit Fourier inversion says
\[
\int_F H_\delta(\varpi^j x)\psi(bx)\,dx
 =\begin{cases}
 C^{-1}|\varpi|^{-j}\delta(-b/\varpi^j),&
                         b\in\varpi^jU,\\
 0,&b\notin\varpi^jU .
 \end{cases}
\tag{8.14}
\]

Use the full-measure Bruhat chart
\[
g=b_0 n(-x)d(a)w_0n(y)
 =\begin{pmatrix}b_0x&b_0(a+xy)\\-b_0&-b_0y\end{pmatrix}.
\]
Its determinant is \(b_0^2a\), trace is \(b_0(x-y)\), and its additive Jacobian is \(|b_0|^3\,db_0\,da\,dx\,dy\). Equivalently,
\[
d^4g=C^2|b_0|^4|a|\,d^\times b_0\,d^\times a\,dx\,dy.
\tag{8.15}
\]
Write \(a=\zeta\varpi^r\), \(b_0=\eta\varpi^k\). Move the upper-triangular operators across the pairing and use (2.3). Before integrating \(x,y,\zeta,\eta\), the summand indexed by a unit character \(\rho\), apart from the determinant-shell condition \(2k+r=l\), is
\[
\begin{split}
&C^2|b_0|^2\,\omega(b_0)^{-1}
 \gamma(\eta)^{-2}\gamma(\zeta)^{-1}
 \omega(-1)\beta(-1)\,z^{-m-r}\alpha(\zeta)
 C_{n+m+r}^{\rho}\\
&\quad{}\times
 H_{\rho^{-1}\epsilon_U^{-1}\alpha^{-1}}
       (\varpi^m x\zeta^{-1})\,
 H_{\rho^{-1}\beta^{-1}}(-\varpi^n y)\,
 \psi(b_0x-b_0y).
\end{split}
\tag{8.16}
\]
For verification, \(d(a^{-1})n(x)v\) is supported on shell \(m+r\), has the factor \(\alpha(\zeta)\), and its unit coefficient of character \(\delta\) is
\(H_{\delta\alpha^{-1}}(\varpi^m x\zeta^{-1})\).
Applying \(w_0^{-1}=\operatorname{diag}(-1,-1)w_0\) gives the factor
\(\omega(-1)z^{-m-r}C_{n+m+r}^{\rho}\).
Pairing on shell \(n\) with \(n(y)u(-t)\) gives the second \(H\) and \(\beta(-1)\). This establishes every term in (8.16).

Apply (8.14) to \(x,y\). Both integrals vanish unless \(k=m=n\); their factors \(C^{-2}|\varpi|^{-m-n}\) cancel \(C^2|b_0|^2\). The remaining integration over \(\zeta\) forces
\(\rho=\gamma^{-1}\epsilon_U^{-1}\). Integration over \(\eta\) then forces \(\alpha\beta=1\). The determinant shell forces \(r=l-2m\). The surviving answer is exactly
\[
\widehat\Phi(e)
 =z^{-l}C_l^{\gamma^{-1}\epsilon_U^{-1}}\,
       \beta(-1)\,1_{m=n}\,1_{\alpha\beta=1}
 =(W\phi)(1)\langle v,u\rangle.
\tag{8.17}
\]
All constants are included: the two multiplicative-to-additive factors in (8.15) cancel the two Fourier factors in (8.14).

The shell computation can be made with finite cutoffs. Restrict \(x,y\) to \(\varpi^{-L}\mathcal O\), and restrict \(a,b_0\) to finite annuli. On these sets the unit Fourier expansions have only finitely many terms. The truncated version of (8.14) is the convolution of its displayed right side with the Fourier transform of \(1_{\varpi^{-L}\mathcal O}\). Once \(L\) exceeds the fixed shell indices and the conductors of \(\alpha,\beta,\gamma,\epsilon_U\), integration over \(\zeta,\eta\) leaves only the indicated character; its unit-shell function is unchanged by that convolution. Thus only \(k=m=n,r=l-2m\) survive, and the finite calculation stabilizes to (8.17). The original matrix Schwartz integral is absolutely convergent, so its chart cutoffs tend to that integral. This supplies the justification for the Fourier calculation.

Finally translate (8.17) to a general \(h\in G\). If \(a=\det h\), the function \(\Phi(h^{-1}g)\) is the same construction with
\(\phi_1(t)=|a|\phi(a^{-1}t)\) and \(v_1=\pi(h)v\).
Its Fourier transform at \(e\) is \(|a|^2\widehat\Phi(h)\).
Since
\(W d(a^{-1})=\omega(a)^{-1}d(a)W\), its right side is
\(|a|\omega(a)^{-1}(W\phi)(a)\langle\pi(h)v,u\rangle\).
Division by \(|a|^2\), and the already checked singular values, prove (8.12). \(\square\)

### 8.4. Supercuspidal continuation and the whole functional equation

Every supercuspidal matrix integral is Laurent polynomial. Indeed there is no \(K\)-fixed vector: its conductor is at least two by Lesson 8, Theorem 4.3. If \(J\subset K\) fixes \(v\), average \(\Phi\) on the right with \(e_J-e_K\). The integral is unchanged, and the new \(\Phi\) vanishes at zero, hence on a neighborhood of zero. The coefficient has support in \(ZC_0\), with \(C_0\subset G\) compact. Intersecting this set with the support of the new \(\Phi\) bounds the central scalar away from zero and infinity. Thus only finitely many determinant valuations contribute. Compactness and local constancy give a finite sum of powers of \(X\). Before this averaging, the possible central tail is a geometric series that converges in a right half-plane, proving the original convergence assertion as well.

We next prove (8.2) first for the tests of Lemma 8.4. Disintegrate \(dg\) by the determinant and \(\mathrm{SL}_2(F)\). For two arbitrary coefficient vectors \(v_0,u_0\), set
\[
F(a)=\int_{\mathrm{SL}_2(F)}
 \langle\pi(gh)v_0,u_0\rangle
 \langle v,\widetilde\pi(gh)u\rangle\,dh,
 \qquad \det g=a.
\]
The integrals are absolutely convergent by compactness of coefficients modulo the centre. The product is unchanged by central scalars, so
\(F(b^2a)=F(a)\). Smoothness also makes it constant on cosets of one open unit subgroup. Consequently it is a finite sum
\(F(a)=\sum_\chi d_\chi\chi(a)\), where the \(\chi\) are quadratic characters. This is valid in characteristic two: although the square-class group need not be finite, its quotient by an open unit subgroup is finite. Inverting \(gh\) in the companion coefficient product shows that the corresponding dual function is \(F(a^{-1})=F(a)\).

A nonzero coefficient \(d_\chi\) implies \(\chi\otimes\pi\simeq\pi\). To see this, integrate the product against \(\chi(\det g)\) on \(G/Z\). Compact coefficient support makes the integral define an intertwining operator between \(\chi\pi\) and \(\pi\). It is zero when these irreducibles are inequivalent, by Schur's lemma, and its specified matrix element is a nonzero constant times \(d_\chi\). The intertwiner argument can be justified directly by changing variables in this finite coefficient integral. Equivalently one may first use the unitary twist from Lesson 7 and its positive invariant pairing; twisting does not change the product. Therefore every character appearing has
\(\gamma(s,\chi\pi,\psi)=\gamma(s,\pi,\psi)\).

Formula (8.12) reduces the two matrix integrals to the sums, over these \(\chi\), of
\[
\int\phi(a)\chi(a)|a|^{s-1/2}\,d^\times a,\qquad
\int(W\phi)(a)\chi(a)^{-1}\omega(a)^{-1}
                              |a|^{1/2-s}\,d^\times a.
\]
The twisted equation of Theorem 3.2 equates them with factor
\(\gamma(s,\chi\pi,\psi)=\gamma(s,\pi,\psi)\).
This proves the matrix equation for all the special tests.

Here is a Fourier argument extending it to every Schwartz test. If
\(\Psi\) is a special test, both \(\Psi,\widehat\Psi\) are compactly supported in \(G\). Partial Fourier Parseval and the right-multiplication Jacobian give, for every invertible \(g\),
\[
\int_{M_2(F)}\Phi(hg)\widehat\Psi(h)\,d^4h
 =|\det g|^{-2}
    \int_{M_2(F)}\widehat\Phi(g^{-1}h)\Psi(h)\,d^4h.
\tag{8.18}
\]
Multiply by \(c_{v_0,u_0}(g)|\det g|^{s+1/2}\) and integrate in \(g\).
To justify the resulting double integrals, first twist so that \(\omega\) is unitary. Since \(h\) ranges over a compact subset of \(G\), all the involved coefficient supports lie in one compact set modulo \(Z\), and their values are uniformly bounded there. The central scalar contributes \(|b|^{2\operatorname{Re}s+1}\) on the first side and \(|b|^{3-2\operatorname{Re}s}\) on the second. Thus both are absolutely convergent for
\(-1/2<\operatorname{Re}s<3/2\). A twist merely translates this strip.

The changes of variables \(g\mapsto hg\) on the first side and \(g\mapsto g^{-1}\) on the second give respectively
\[
\begin{split}
A&=\iint\Phi(g)\widehat\Psi(h)
 \langle\pi(g)v_0,\widetilde\pi(h)u_0\rangle
 |\det g|^{s+1/2}|\det h|^{3/2-s}\,dg\,dh,\\
B&=\iint\widehat\Phi(g)\Psi(h)
 \langle\pi(g^{-1})v_0,\widetilde\pi(h^{-1})u_0\rangle
 |\det g|^{3/2-s}|\det h|^{s+1/2}\,dg\,dh .
\end{split}
\tag{8.19}
\]
The special-test equation in the \(h\)-variable replaces \(A\) by
\(\gamma(s,\pi,\psi)Z_{\rm mat}(s,\Phi,c_{v_0,u_s})\), while \(B\) is
\(Z_{\rm mat}(1-s,\widehat\Phi,\check c_{v_0,u_s})\), where
\[
u_s=\int_G\Psi(h)|\det h|^{s+1/2}
                         \widetilde\pi(h^{-1})u_0\,dh .
\tag{8.20}
\]
The vectors \(u_s\), for these special tests, contain a spanning set of the form
\(e^{bs}u'\). There is one nonzero such vector: choose the determinant test \(1_U\), and opposite coefficients of \(u_0\) for the positive invariant pairing after a unitary twist. Its pairing with \(u_0\) is the positive integral of the squared coefficient on \(|\det h|=1\), so is nonzero and independent of \(s\). Translating the test preserves its special form and multiplies (8.20) by a determinant exponential and a translate of that vector. Irreducibility makes these translates span the dual. We can therefore cancel those nonzero exponentials in (8.19) and obtain (8.2) for every \(u'\), hence every coefficient. Rational continuation extends it beyond the convergence strip.

The same positive test, with determinant supported on \(U\), gives a nonzero constant matrix integral: its value is the squared-coefficient integral on \(|\det g|=1\). Since all the integrals are in \(R\), their ideal is exactly \(R=L(s,\pi)R\). This completes the supercuspidal case, and all cases of Theorem 8.1. \(\square\)

For unramified \(\chi\), the finite-dimensional factor list is therefore
\[
L(s,D_\chi)=
 \frac1{(1-\chi(\varpi)q^{-s-1/2})
        (1-\chi(\varpi)q^{-s+1/2})},
\qquad \epsilon(s,D_\chi,\psi)=1.
\]
For ramified \(\chi\), it is \(L=1\) and
\(\epsilon=\epsilon(s,\chi,\psi)^2\). These formulas complete the list for every irreducible in Lesson 7. The conductor assertion (5.1) and local converse theorem still concern the infinite-dimensional representations.

Jacquet–Langlands, §13, Theorem 13.1, is the historical source for the matrix construction. The proofs here make the triangular measure, exceptional pole cancellation, compact Kirillov matrix transform and extension to arbitrary tests explicit. The individual Satake parameters of the unitary complementary series \(I(\nu^r,\nu^{-r})\), \(0<r<1/2\), do not both have modulus one.

## 9. Two fully computed examples

**Example 9.1 — an unramified principal series.** Let \(\mu_1,\mu_2\) be unramified, with irreducible induction, and put
\(\alpha=\mu_1(\varpi),\beta=\mu_2(\varpi)\).
Lesson 8 gives the normalized spherical function
\[
\xi_0(\varpi^m u)=q^{-m/2}
        \sum_{i+j=m}\alpha^i\beta^j\quad(m\geq0),
\]
and zero for \(m<0\). On shell \(m\), the Mellin weight is
\(q^{-m(s-1/2)}\); multiplying by \(q^{-m/2}\) leaves \(X^m\).
Therefore, in a half-plane where both geometric series converge,
\[
M_s(\xi_0)=\sum_{m\geq0}\sum_{i+j=m}\alpha^i\beta^jX^m
 =\left(\sum_{i\geq0}(\alpha X)^i\right)
  \left(\sum_{j\geq0}(\beta X)^j\right)
 =\frac1{(1-\alpha X)(1-\beta X)}.
\tag{9.1}
\]
This calculation includes \(\alpha=\beta\): the coefficient is then
\((m+1)\alpha^m\), giving a squared factor. Each unramified Tate epsilon is one, so Theorem 4.1 gives
\(\epsilon(s,\pi,\psi)=1\).
Its gamma factor is explicitly
\[
\gamma(s,\pi,\psi)
 =\frac{(1-\alpha X)(1-\beta X)}
        {(1-\alpha^{-1}q^{-1}X^{-1})
         (1-\beta^{-1}q^{-1}X^{-1})}.
\tag{9.2}
\]
This is the product of the two character gamma factors, with
\(q^{-(1-s)}=q^{-1}X^{-1}\). No modulus-one assumption on \(\alpha,\beta\) entered the calculation.

**Example 9.2 — untwisted Steinberg.** Its normalized newfunction is
\(\xi_1(\varpi^m u)=q^{-m}\) for \(m\geq0\), and zero otherwise. Consequently
\[
M_s(\xi_1)=\sum_{m\geq0}q^{-m}q^{-m(s-1/2)}
 =(1-q^{-s-1/2})^{-1}.
\]
Put \(\chi=1\) in (4.9). The remaining ratio of character factors is
\[
\frac{1-q^{1/2}X}{1-q^{-1/2}X^{-1}}
 =-q^{1/2}X,
\]
because \(1-q^{-1/2}X^{-1}=-q^{-1/2}X^{-1}(1-q^{1/2}X)\).
Thus
\[
\epsilon(s,\mathrm{St},\psi)=-q^{1/2-s},\qquad
\epsilon(1/2,\mathrm{St},\psi)=-1,\qquad c(\mathrm{St})=1.
\tag{9.3}
\]
The minus sign is a cancellation calculation in the prescribed normalization.

## 10. Exercises with complete solutions

**Exercise 10.1 — the spherical \(L\)-factor.** Compute
\(L(s,I(\mu_1,\mu_2))\), for unramified \(\mu_i\) with irreducible induction, directly from the newvector of Lesson 8.

**Solution 10.1.** Write \(\alpha=\mu_1(\varpi),\beta=\mu_2(\varpi)\).
The function is zero on negative shells and equals
\(q^{-m/2}\sum_{j=0}^m\alpha^j\beta^{m-j}\) on shell \(m\geq0\).
Since each unit shell has multiplicative measure one, its integral is
\[
\sum_{m\geq0}\sum_{j=0}^m\alpha^j\beta^{m-j}q^{-ms}
 =\sum_{j,k\geq0}(\alpha q^{-s})^j(\beta q^{-s})^k
 =\frac1{(1-\alpha q^{-s})(1-\beta q^{-s})}.
\]
Absolute convergence holds when
\(|\alpha q^{-s}|<1\) and \(|\beta q^{-s}|<1\), justifying the sum interchange; the last expression gives continuation elsewhere. The germ pole bound of Theorem 1.1 puts every integral in this reciprocal-product ideal, and this single newvector integral is its generator. The denominator has constant term one. Hence the displayed expression is the normalized \(L\)-factor. Equal parameters give \((1-\alpha q^{-s})^{-2}\), rather than a single linear factor. \(\square\)

**Exercise 10.2 — dependence on \(\psi\).** Prove (6.1), including the powers of the absolute value.

**Solution 10.2.** If \(\mathcal W\) transforms by \(\psi\), put
\(\mathcal W_a(g)=\mathcal W(d(a)g)\). For \(n(x)\),
\(\mathcal W_a(n(x)g)=\psi(ax)\mathcal W_a(g)\).
Because the two diagonal matrices commute, substituting \(u=at\) gives
\[
\Psi(g,s,\mathcal W_a)
 =\int\mathcal W(d(u)g)|u/a|^{s-1/2}\,d^\times u
 =|a|^{1/2-s}\Psi(g,s,\mathcal W).
\]
In the central-character-twisted integral the additional term is
\(\omega(u/a)^{-1}=\omega(a)\omega(u)^{-1}\), so its multiplier is
\(\omega(a)|a|^{1/2-s}\). The normalized \(L\)-generator stays the same, because these scalar multipliers are units in \(R\).
At argument \(1-s\) the left multiplier is \(\omega(a)|a|^{s-1/2}\), whereas the right multiplier at \(s\) is \(|a|^{1/2-s}\).
Their quotient is \(\omega(a)|a|^{2s-1}\). The functional equation, evaluated on a nonzero Mellin test, therefore gives exactly (6.1).
Self-dual additive measure changes by \(|a|^{1/2}\), as verified after Proposition 6.1; multiplicative unit measure stays one. \(\square\)

**Exercise 10.3 — a ramified Steinberg twist.** Let \(\chi\) be ramified. Compute \(L(s,\mathrm{St}_\chi)\) and \(\epsilon(s,\mathrm{St}_\chi,\psi)\).

**Solution 10.3.** Put \(a=a(\chi)\geq1\), \(A=\chi(\varpi)\), and
\(\tau=\tau(\chi^{-1},\psi,\varpi^a)\).
The germ of a special Kirillov function is a multiple of \(\nu\chi\).
Its unit average is zero, since \(\int_U\chi(u)\,du=0\).
Its Mellin integral therefore has only finitely many shell contributions. The compact function \(1_U\) has integral one, and its dilates produce every Laurent monomial. This proves \(L(s,\mathrm{St}_\chi)=1\), and the dual has \(L=1\) as well.

The compact Weyl calculation of Section 4 gives gamma as the product for \(\chi\nu^{1/2},\chi\nu^{-1/2}\).
Tate's formula (4.10) gives the two factors
\[
A^a q^{-a(s+1/2)}\tau,\qquad
A^a q^{-a(s-1/2)}\tau.
\]
Multiplication yields
\[
\epsilon(s,\mathrm{St}_\chi,\psi)
 =A^{2a}q^{-2as}\tau^2
 =\epsilon(1/2,\chi,\psi)^2\,q^{2a(1/2-s)}.
\]
The representation conductor is \(2a\), exactly as in Lesson 8.
For a unitary \(\chi\), the imported Gauss norm \(|\tau|=q^{a/2}\) also gives
\(|\epsilon(1/2,\mathrm{St}_\chi,\psi)|=1\).
In this ramified case there is no extra minus sign of the unramified formula: the full answer is the square of the character epsilon, including its Gauss-sum phase. \(\square\)

**Exercise 10.4 — the local converse theorem.** Under the hypotheses of Theorem 7.1, recover the representations from their twisted gamma factors.

**Solution 10.4.** Realize both representations on scalar Kirillov functions, and set
\(\epsilon_U=\omega|_U,z=\omega(\varpi)\).
Fix any smooth character \(\alpha\) of \(U\). Extend
\((\alpha\epsilon_U)^{-1}\) to a character \(\chi\) of \(F^\times\) by requiring \(\chi(\varpi)=1\); the decomposition \(F^\times=\varpi^{\mathbb Z}U\) makes this a well-defined smooth character.
The common compact test \(\xi=(\alpha\epsilon_U)1_U\) has
\(\int\xi(t)\chi(t)|t|^{s-1/2}d^\times t=1\).

The twist transports functions by multiplication by \(\chi(t)\), and the Weyl matrix has determinant one. Its functional equation thus equates gamma to
\[
\int(W\xi)(t)\omega(t)^{-1}\chi(t)^{-1}|t|^{1/2-s}d^\times t.
\]
On shell \(n\) the unit factor \(\omega(u)^{-1}\chi(u)^{-1}\) is \(\alpha(u)\).
Unit integration extracts the coefficient \(C_n^\alpha\) of Lesson 7. The remaining uniformizer factor is
\(z^{-n}q^{n(s-1/2)}\). Therefore the twisted gamma is
\(C^\alpha(z^{-1}q^{s-1/2})\).
The same computation for \(\pi'\) gives \(C'^\alpha\). Equality of gamma factors gives equality of these rational functions.

Their expansions at zero have exponents bounded below; uniqueness of a Laurent expansion makes every \(C_n^\alpha=C_n'^\alpha\).
A compact smooth function has a finite unit-character expansion on each of finitely many shells. Applying formula (2.3) to these terms proves equality of the Weyl transforms on all of \(V_0\).
Since each full model is \(V_0+WV_0\), their function spaces coincide. On this space the Weyl operators coincide too, by \(W^2=\omega(-1)\).
Finally their upper-triangular actions already coincide from the common central and additive characters. The upper triangular subgroup and \(w_0\) generate \(\mathrm{GL}_2(F)\), so the identity of function spaces intertwines every group element. This proves \(\pi\simeq\pi'\). \(\square\)

## 11. Prerequisites and source locators

The imported one-dimensional theory is [NT-ADL-07](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-ADL/NT-ADL-07.html), Proposition 7.1, Theorem 7.2, Theorem 7.3 and Proposition 7.4: character \(L\)-ideals, the Tate functional equation, Gauss factors, and additive-character/measure dependence. [NT-ADL-08](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-ADL/NT-ADL-08.html), Theorem 8.1 and Propositions 8.2–8.4, is the companion normalization prerequisite for the archimedean lesson. We do not duplicate its gamma-integral proofs here.

Section 8 proves the complete matrix construction, its full ideal and functional equation, comparison with all generic factors, and the determinant-character extension. Its induction kernel is proved also at the infinite places for use in Lesson 11. The Steinberg argument removes the extra induced pole and attains the remaining denominator by an explicit residue-level test. The supercuspidal argument computes every shell and Haar factor of its matrix Fourier transform, then extends the equation from compact Kirillov tests to all Schwartz tests by Parseval and irreducibility. Jacquet–Langlands, §13, Theorem 13.1, printed pp. 217–218, and its constituent calculations on pp. 227–239 remain the historical authority. No matrix comparison is used in the independent proofs of Theorems 1.1, 3.2, 4.1, 5.1 or 7.1.

Earlier proved local inputs are Lesson 5's compact averaging and admissible duality; Lesson 6's normalized induction, duality and exceptional sequences; Lesson 7's scalar model, full germs, finite Weyl coefficient formula and explicit principal kernel; and Lesson 8's newvector dimension, actual functions and conductors. Theorem 5.1 derives the supercuspidal epsilon exponent from those newvector results, so that equality has not been left as a stated input.

The authorities checked for this lesson are:

- Hervé Jacquet and Robert P. Langlands, [*Automorphic Forms on GL(2)*](https://publications.ias.edu/sites/default/files/Automorphic-forms-on-GL2.pdf) (1970), §2, Theorem 2.18 and Corollary 2.19, for the local functional equation and converse; §3, Propositions 3.5–3.6 and Corollary 3.7, for principal and special factors; §13, Theorem 13.1 and its constituent calculations, for matrix zeta integrals.
- Jayce R. Getz and Heekyoung Hahn, [*An Introduction to Automorphic Representations*](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), draft of 22 April 2022, §11.5, Propositions 11.5.1 and 11.5.4–11.5.6, for the local ideal, functional equation, monomial and conductor formulations.

The proofs above use the common scalar model to make the Mellin ideal, torus uniqueness, two-variable Fourier calculation, supercuspidal Weyl shell and converse recovery explicit. Their signs, unit measures and half-powers are carried through the calculations. The matrix comparison supplies a second complete construction and also covers the nongeneric characters.
