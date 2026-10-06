# Hecke L-functions and the Dedekind zeta function

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The global integral has already been continued. We now choose its test function so that the integral is exactly an Euler product with Gamma factors. This identifies the conductor in the functional equation. A separate computation of the multiplicative quotient measure then turns the two residues of the integral into arithmetic formulas.

Throughout, \(K\) is a number field, \(D=|d_K|\), and \(r_1,r_2\) are its real and complex place counts. Write \(m=r_1+r_2\), \(h=h_K\), and \(w=w_K\). The regulator \(R=R_K\) uses the weighted logarithms \(\log|u|_v\), with \(|z|_v=|z|^2\) at a complex place, and the determinant obtained by deleting one coordinate. Set \(R=1\) when \(m=1\). The unit-lattice theorem and the finiteness of the class group were proved in *Idèles and the idèle class group*.

## Two completions and the standard test

Let \(\omega:C_K\to S^1\) be a continuous unitary Hecke character. At a finite place its conductor exponent \(a_v\) is zero if \(\omega_v\) is trivial on \(\mathcal O_v^\times\), and otherwise is the least positive integer for which it is trivial on \(1+\mathfrak p_v^{a_v}\). There are only finitely many positive exponents. Define the intrinsic conductor and its analytic scale by

\[
\mathfrak f=\prod_{v<\infty}\mathfrak p_v^{a_v},\qquad
Q=D\,N\mathfrak f.
\tag{1}
\]

This conductor belongs to the character itself. Describing the same character with a larger ray modulus does not change (1).

At real places write \(\omega_v(x)=\operatorname{sgn}(x)^{\epsilon_v}|x|^{it_v}\), where \(\epsilon_v\in\{0,1\}\). At complex places write \(\omega_v(z)=(z/|z|)^{n_v}|z|_v^{it_v}\), where \(n_v\in\mathbb Z\). Put

\[
\begin{aligned}
L(s,\omega)&=\prod_{\substack{v<\infty\\a_v=0}}
 (1-\omega_v(\pi_v)q_v^{-s})^{-1},\\
\Gamma_\infty(s,\omega)&=
 \prod_{v\text{ real}}\Gamma_{\mathbb R}(s+it_v+\epsilon_v)
 \prod_{v\text{ complex}}\Gamma_{\mathbb C}(s+it_v+|n_v|/2),\\
L^*(s,\omega)&=\Gamma_\infty(s,\omega)L(s,\omega),\qquad
\Lambda(s,\omega)=Q^{s/2}L^*(s,\omega).
\end{aligned}
\tag{2}
\]

Here \(\Gamma_{\mathbb R}(z)=\pi^{-z/2}\Gamma(z/2)\) and \(\Gamma_{\mathbb C}(z)=2(2\pi)^{-z}\Gamma(z)\). Distinguishing \(L^*\) from \(\Lambda\) fixes where the power of \(Q\) appears.

Keep the global trace additive character of *Additive characters, self-dual measures and Poisson summation on the adèles*. Its real component has negative exponential sign. Finite additive measures are self-dual; finite multiplicative unit groups have mass one. The infinite multiplicative measures are \(dx/|x|\) and \(2\,du\,dv/(\pi|z|^2)\).

Choose the following local functions. If \(a_v=0\), use \(f_v=1_{\mathcal O_v}\). If \(a_v>0\), set \(\eta_v=\omega_v|_{\mathcal O_v^\times}\) and use \(f_v=\eta_v^{-1}1_{\mathcal O_v^\times}\). At a real place use \(x^{\epsilon_v}e^{-\pi x^2}\). At a complex place use \(\bar z^{n_v}e^{-2\pi|z|^2}\) for \(n_v\geq0\), and \(z^{-n_v}e^{-2\pi|z|^2}\) for \(n_v<0\). Their product is a global Schwartz function. The finite local theory gives respectively the Euler factor and one; the infinite local theory gives the Gamma factors in (2). Absolute Euler factorization in \(\Re s>1\) therefore gives the exact equality

\[
Z(f,\omega,s)=L^*(s,\omega).
\tag{3}
\]

There is no unspecified constant or exponential in this normalization.

## The conductor and the root number

**Theorem 10.1.** Both completions in (2) continue meromorphically, and

\[
\begin{aligned}
L^*(s,\omega)&=W(\omega)Q^{1/2-s}L^*(1-s,\bar\omega),\\
\Lambda(s,\omega)&=W(\omega)\Lambda(1-s,\bar\omega),
\qquad |W(\omega)|=1.
\end{aligned}
\tag{4}
\]

They are entire unless \(\omega=|\cdot|^{i\tau}\) for some real \(\tau\). In that exceptional case their only poles are simple poles at \(-i\tau\) and \(1-i\tau\).

**Proof.** Let \(d_v\) be the local different exponent. The finite local formula in *Tate's local theory at the finite places*, applied to \(c_v=\omega_v|\cdot|_v^s\), reads

\[
\varepsilon_v(c_v)=W_vq_v^{(a_v+d_v)(1/2-s)}.
\tag{5}
\]

For an unramified place take any generator \(\delta_v\) of the different and put \(W_v=\omega_v(\delta_v)\). For a ramified place choose \(b_v\) of valuation \(a_v+d_v\). With representatives of the unit classes modulo \(\mathfrak p_v^{a_v}\), the formula is

\[
W_v=\omega_v(b_v)q_v^{-a_v/2}
 \sum_{u\in(\mathcal O_v/\mathfrak p_v^{a_v})^\times}
 \eta_v(u)^{-1}\psi_v(u/b_v).
\tag{6}
\]

The sum is well-defined because \(\psi_v\) is trivial on \(\mathfrak p_v^{-d_v}\). The local proof establishes independence of the choices, and gives its absolute value \(q_v^{a_v/2}\). Thus \(|W_v|=1\). Formula (5) follows directly from the self-dual additive volume \(q_v^{-d_v/2}\): its unramified expression is \(q_v^{-d_v/2}q_v^{d_v}c_v(\delta_v)\); its ramified expression is the same initial scalar times \(c_v(b_v)\) times the sum in (6). This checks the exponent and the inverse unit character without a convention change.

At infinity the corresponding constants, for our negative trace character, are

\[
W_v=(-i)^{\epsilon_v}\quad(v\text{ real}),\qquad
W_v=(-i)^{|n_v|}\quad(v\text{ complex}).
\tag{7}
\]

Imaginary norm twists replace \(s\) by \(s+it_v\) in the local Gamma factors; the phases (7) remain the same. All but finitely many constants (5) are one. Since the norm of the different is \(D\), multiplication gives

\[
\prod_v\varepsilon_v(c_v)=W(\omega)Q^{1/2-s},
\qquad W(\omega)=\prod_vW_v.
\tag{8}
\]

The global factor in (8) is independent of rescaling the trace character by a diagonal \(a\in K^\times\). Replace \(\psi_v(x)\) by \(\psi_v(ax)\) and its self-dual measure by \(|a|_v^{1/2}dx_v\). The transformed test is then \(|a|_v^{1/2}\widehat f_v(ay)\). Substitution in its local zeta integral, or Proposition 7.4 at finite places, multiplies the local epsilon factor by \(\omega_v(a)|a|_v^{s-1/2}\). Their product is one: \(\omega(a)=1\) and \(\prod_v|a|_v=1\). Thus the global factor, including \(W(\omega)\), is unchanged. This connects the local dependence on auxiliary choices to the global character and product formula.

The local functional equations and (3) yield
\(Z(\widehat f,\bar\omega,1-s)=W(\omega)Q^{1/2-s}L^*(1-s,\bar\omega)\).
One can first factor the left-hand integral in \(\Re s<0\), where it converges absolutely, and then use the meromorphic local identities. The global functional equation identifies its continuation with \(Z(f,\omega,s)\). There is no assumption that the two original global convergence regions overlap. This proves the first line of (4); multiplication by \(Q^{s/2}\) proves the second.

The global pole criterion says that \(Z(f,\omega,s)\) is entire if \(\omega\) is nontrivial on \(C_K^1\). Characters trivial there are exactly the pure norm twists. This proves the claimed entireness by (3). Actual poles in the exceptional case will follow from the positive arithmetic volume below. For later comparison, a pure norm twist has \(\mathfrak f=\mathcal O_K\), \(W(\omega)=D^{-i\tau}\), and

\[
\Lambda(s,|\cdot|^{i\tau})=D^{-i\tau/2}\Lambda_K(s+i\tau).
\tag{9}
\]

Indeed its finite central constants multiply to \(\prod_vq_v^{-it_vd_v}=D^{-i\tau}\), with \(t_v=\tau\), and its infinite phases are one. \(\square\)

Deleting additional Euler factors produces an imprimitive function. Each deletion multiplies (2) by \(1-\omega_v(\pi_v)q_v^{-s}\); these polynomials must themselves be transformed in a functional equation. The unchanged primitive equation (4) does not apply to that altered product.

## Computing the norm-one volume

Write \(\kappa=\operatorname{vol}(C_K^1)\) for the measure obtained by quotienting the fixed idèle measure by counting measure on \(K^\times\), and then dividing the norm direction by \(dt/t\). The section independence of this measure was established in *Tate's global theory: continuation and functional equation*.

**Proposition 10.3.** With precisely these measures,

\[
\kappa=\frac{2^{r_1+r_2}hR}{w}.
\tag{10}
\]

**Proof.** The valuation map from idèles to fractional ideals induces a surjection \(C_K\to\mathrm{Cl}_K\). Its kernel is
\((K_\infty^\times\times\widehat{\mathcal O}_K^\times)/\mathcal O_K^\times\): a principal finite ideal can be removed by a field element, and the field elements preserving finite units are exactly global units. Intersecting with norm one gives the exact sequence

\[
1\longrightarrow B^1\longrightarrow C_K^1
 \longrightarrow\mathrm{Cl}_K\longrightarrow1.
\tag{11}
\]

Surjectivity still holds because an arbitrary class representative can be multiplied by an infinite positive scalar of prescribed norm. The subgroup \(B^1\) is open and has index \(h\), so its volume, multiplied by \(h\), is \(\kappa\).

For \(x\in K_\infty^\times\) use the logarithmic coordinates \(\ell_v=\log|x_v|_v\). At a real place each sign has counting mass one and \(dr/r=d\ell_v\). At a complex place, polar coordinates in the fixed measure give

\[
\frac{2\,du\,dv}{\pi|z|^2}
 =4\frac{dr}{r}\frac{d\theta}{2\pi}
 =2\,d\ell_v\frac{d\theta}{2\pi}.
\tag{12}
\]

Thus the angular group has total mass \(2^m\), and the finite unit group has mass one. The logarithm of the idèle norm is \(T=\sum_v\ell_v\). The linear coordinate change
\((\ell_1,\ldots,\ell_m)\mapsto(\ell_1,\ldots,\ell_{m-1},T)\)
has determinant one. Consequently the measure on the hyperplane \(H:T=0\) is deleted-coordinate Lebesgue measure. This conclusion holds also for the balanced norm section: translating each fibre preserves that measure.

Choose units whose logarithms form a basis of the full unit lattice in \(H\). Its half-open parallelepiped has volume \(R\). These units freely generate a subgroup \(E\) of \(\mathcal O_K^\times\), and \(\mathcal O_K^\times=\mu_K\times E\): any unit can have its logarithm removed by an element of \(E\), leaving an element of the logarithmic kernel \(\mu_K\). Angular and finite-unit translations preserve measure. A domain consisting of the parallelepiped times the angular and finite-unit groups therefore gives volume \(2^mR\) after quotienting by \(E\). The remaining group \(\mu_K\), of order \(w\), acts freely. Quotient Haar measure for counting measure on a finite free subgroup divides the volume by \(w\). This can be checked on disjoint translates of an injective quotient neighbourhood and then by a measurable partition. Hence
\(\operatorname{vol}(B^1)=2^mR/w\), proving (10). When \(m=1\), \(H\) is the zero vector space with mass one, so the same argument uses \(R=1\). \(\square\)

In particular, \(\kappa\) is positive. It differs from the zeta residue because that residue also contains the finite additive different volumes and the infinite Gamma values.

## The Dedekind equation and both residues

**Theorem 10.2.** The function

\[
\Lambda_K(s)=D^{s/2}\Gamma_{\mathbb R}(s)^{r_1}
 \Gamma_{\mathbb C}(s)^{r_2}\zeta_K(s)
\tag{13}
\]

continues meromorphically, satisfies \(\Lambda_K(s)=\Lambda_K(1-s)\), and has exactly two poles, simple, at zero and one. Their residues are respectively \(-\kappa\) and \(\kappa\).

**Proof.** For the trivial character, (3) uses the integral-ring indicators at every finite place and the ordinary infinite Gaussians. Ideal factorization identifies its Euler product with \(\zeta_K\) in \(\Re s>1\). All central constants in (6)–(7) are one, proving the equation by (4).

The value of this test at zero is one. Its Fourier transform at zero is its additive integral. Every infinite Gaussian has integral one in the self-dual measures, whereas the finite indicator has integral \(q_v^{-d_v/2}\). Therefore

\[
f(0)=1,\qquad \widehat f(0)=D^{-1/2}.
\tag{14}
\]

The global residue formula gives residues \(-\kappa\) and \(\kappa D^{-1/2}\) for \(L_K^*\). Multiplying by the entire nonzero factor \(D^{s/2}\) gives the stated residues for (13). Positivity of (10) proves that neither pole cancels. The global theorem permits no others. This also completes the exceptional-pole assertion in Theorem 10.1 by (9). \(\square\)

**Corollary 10.4.** The arithmetic residue and the leading term at zero are

\[
\operatorname*{Res}_{s=1}\zeta_K(s)
 =\frac{2^{r_1}(2\pi)^{r_2}hR}{w\sqrt D},
\qquad
\zeta_K(s)=-\frac{hR}{w}s^{m-1}+O(s^m).
\tag{15}
\]

**Proof.** The Gamma values are \(\Gamma_{\mathbb R}(1)=1\) and \(\Gamma_{\mathbb C}(1)=1/\pi\). Dividing the residue at one in (13) by \(\sqrt D\,\pi^{-r_2}\), and using (10), proves the first formula. At zero, each Gamma factor equals \(2/s+O(1)\). Hence (13) and its residue \(-\kappa\) imply
\(\zeta_K(s)=-\kappa s^{m-1}/2^m+O(s^m)\), proving the second. The leading coefficient is nonzero, so the zero order is exactly \(m-1\). When \(m=1\) the order is zero: the zeta value is nonzero. \(\square\)

## Primitive Dirichlet characters and their phases

Let \(\chi\) be primitive modulo \(M\), and \(\chi(-1)=(-1)^\epsilon\). The idèlic character constructed in *Quasi-characters and Hecke characters* has finite unit restriction \(\chi_p^{-1}\), not \(\chi_p\). Its ideal character is \(\chi\), and its real parity is \(\epsilon\). For \(p^{a_p}\Vert M\), its uniformizer value is

\[
\omega_p(p)=\prod_{r\mid M,\ r\ne p}\chi_r(p).
\tag{16}
\]

The standard rational finite additive character evaluates \(u/p^{a_p}\) as \(e^{2\pi iu/p^{a_p}}\). Thus its ramified factor (6) is
\(\omega_p(p)^{a_p}\tau(\chi_p)/\sqrt{p^{a_p}}\), where \(\tau(\chi_p)=\sum_{u\bmod p^{a_p}}\chi_p(u)e^{2\pi iu/p^{a_p}}\), with \(\chi_p\) zero on nonunits.

To multiply the phases, put \(M_p=M/p^{a_p}\) and choose \(t_pM_p\equiv1\pmod{p^{a_p}}\). CRT represents a residue as \(u=\sum_p M_pt_pu_p\). Substituting this expression in the global Gauss sum, and replacing \(t_pu_p\) by a new local variable, gives

\[
\tau(\chi)=\prod_{p\mid M}\chi_p(M_p)\tau(\chi_p).
\tag{17}
\]

Meanwhile (16) gives
\(\prod_p\omega_p(p)^{a_p}=\prod_p\chi_p(M_p)\), by interchanging the two finite products. Multiplication with the real factor \((-i)^\epsilon\) proves

\[
W(\chi)=\frac{\tau(\chi)}{i^\epsilon\sqrt M},\qquad
|\tau(\chi)|=\sqrt M.
\tag{18}
\]

The absolute-value assertion follows also directly by multiplying the local Gauss-sum absolute values proved in the finite local theory. Primitivity ensures that each nontrivial local conductor is exactly \(p^{a_p}\); the argument includes powers of two. For \(M=1\) use the empty product and \(\tau=1\).

Our completion is \(M^{s/2}\Gamma_{\mathbb R}(s+\epsilon)L(s,\chi)\). The commonly used expression

\[
\Lambda_D(s,\chi)=(M/\pi)^{s/2}
 \Gamma((s+\epsilon)/2)L(s,\chi)
\tag{19}
\]

is \(\pi^{\epsilon/2}\) times ours. The constant is the same for \(\chi\) and \(\bar\chi\), so its functional equation has the same root number (18).

## Rational and Gaussian examples

For \(K=\mathbb Q\), \(h=R=1\), \(w=2\), and \(D=1\). Thus \(\kappa=1\), and \(\Gamma_{\mathbb R}(s)\zeta(s)\) has residues \(-1,+1\) and satisfies the Riemann equation. Formula (15) gives \(\operatorname{Res}_1\zeta=1\) and \(\zeta(0)=-1/2\).

For \(K=\mathbb Q(i)\), the earlier Euclidean calculation gives \(h=1\), \(w=4\), \(R=1\), and \(D=4\). A prime \(p\equiv1\pmod4\) splits, a prime \(p\equiv3\pmod4\) is inert, and two ramifies. Indeed for odd \(p\), reduction of \(X^2+1\) decides splitting; the quadratic character of \(-1\) computed in the character lesson is \((-1)^{(p-1)/2}\). Comparing every Euler factor therefore proves

\[
\zeta_{\mathbb Q(i)}(s)=\zeta(s)L(s,\chi_{-4})
\tag{20}
\]

initially in \(\Re s>1\), and then meromorphically. The duplication identity \(\Gamma_{\mathbb C}(s)=\Gamma_{\mathbb R}(s)\Gamma_{\mathbb R}(s+1)\) shows that its discriminant-completed function is the product of our rational completion and our conductor-completed \(\chi_{-4}\) function. Its Gauss sum is \(i-(-i)=2i\); the finite factor at two is \(i\), the real factor is \(-i\), and the global root is one. Finally,

\[
\kappa_{\mathbb Q(i)}=1/2,\qquad
\operatorname{Res}_1\zeta_{\mathbb Q(i)}=\pi/4,\qquad
\zeta_{\mathbb Q(i)}(0)=-1/4.
\tag{21}
\]

These unequal volume and residue values give a useful test of the measures.

## Nonvanishing on the boundary

The functional equation alone does not rule out zeros on the line \(\Re s=1\). The Euler product supplies the missing positivity.

**Lemma 10.5.** Let a nonnegative ideal Dirichlet series \(F(s)=\sum_{\mathfrak a}c_{\mathfrak a}(N\mathfrak a)^{-s}\), with \(c_{\mathfrak a}\geq0\), converge absolutely for \(\Re s>1\). If \(c_{\mathfrak b^2}\geq1\) for every integral ideal \(\mathfrak b\), then \(F\) cannot extend to an entire function.

**Proof.** Suppose it were entire. Absolute convergence in a neighbourhood of \(s=2\) permits termwise differentiation of every order: powers of \(\log N\mathfrak a\) are bounded by an arbitrarily small positive power of \(N\mathfrak a\). Its Taylor expansion at \(2\), evaluated at \(1/2\), is

\[
F(1/2)=\sum_{j\geq0}\frac{(3/2)^j}{j!}
 \sum_{\mathfrak a}c_{\mathfrak a}
 (\log N\mathfrak a)^j(N\mathfrak a)^{-2}
 =\sum_{\mathfrak a}c_{\mathfrak a}(N\mathfrak a)^{-1/2}.
\]

Each summand of the double series is nonnegative, so exchanging the two sums is justified even before finiteness is known. The Taylor series is finite because its radius is infinite. But the last sum is at least \(\sum_{\mathfrak b}(N\mathfrak b)^{-1}\): ideal squaring is injective by unique prime-ideal factorization. That series diverges, since convergence would, by domination as real \(s\downarrow1\), contradict the positive pole of \(\zeta_K(s)\) in Corollary 10.4. This contradiction proves the lemma. \(\square\)

**Theorem 10.6.** For every unitary Hecke character \(\omega\) and real \(t\), the finite \(L\)-function has no zero at \(1+it\). It is holomorphic and nonzero there unless \(\omega=|\cdot|^{-it}\), in which case it has a simple pole.

**Proof.** Put \(\mu=\omega|\cdot|^{it}\). The finite Euler products give \(L(s,\mu)=L(s+it,\omega)\), first absolutely and then meromorphically. Thus it suffices to analyse \(L(1,\mu)\).

The reciprocal Gamma factors are entire, and the archimedean factors in this course are finite and nonzero on \(\Re s=1\). Theorem 10.1 therefore shows that \(L(s,\nu)\) can have a pole at \(s=1\) only if \(\nu=1\); the norm-twist identity reduces every exceptional case to the unique pole of \(\zeta_K\). In particular \(L(s,\mu)\) is entire when \(\mu\) is a nontrivial quadratic character: a finite-order norm character is trivial, because the norm maps onto \(\mathbb R_{>0}\).

For this quadratic case, expand \(F(s)=\zeta_K(s)L(s,\mu)\) into its ideal Euler product. At an unramified prime its factor is \((1-T)^{-2}\) if \(\mu(\pi)=1\), and \((1-T^2)^{-1}\) if \(\mu(\pi)=-1\), where \(T=(N\mathfrak p)^{-s}\). At a ramified prime the factor is \((1-T)^{-1}\). All coefficients are nonnegative, and every squared ideal has coefficient at least one. If \(L(1,\mu)=0\), this zero cancels the only pole of \(\zeta_K\), making \(F\) entire. There are no other poles: Theorem 10.2 permits only zero and one in the completed function, and Corollary 10.4 shows that the finite zeta function is regular at zero. Lemma 10.5 forbids that, so \(L(1,\mu)\ne0\).

Now suppose \(\mu^2\ne1\). Remove a finite set \(S\) of primes containing the conductor primes of \(\mu\), and use the same omitted primes in all three Euler products. Write \(\zeta_{K,S}\) and \(L_S\) for them. For real \(\sigma>1\), logarithmic expansion gives

\[
\log\!\left(\zeta_{K,S}(\sigma)^3
 |L_S(\sigma,\mu)|^4|L_S(\sigma,\mu^2)|\right)
 =\sum_{\mathfrak p\notin S}\sum_{j\geq1}
 \frac{3+4\Re(\mu(\pi_{\mathfrak p})^j)
       +\Re(\mu(\pi_{\mathfrak p})^{2j})}
 {j(N\mathfrak p)^{j\sigma}}\geq0.
\]

Indeed, writing the unit-modulus value as \(e^{i\theta}\), the numerator is \(3+4\cos\theta+\cos2\theta=2(1+\cos\theta)^2\). The expansions are absolutely convergent, so all products and logarithms used here are justified. Their displayed product is consequently at least one.

If \(L(1,\mu)\) vanished to order \(k\geq1\), the finite omitted Euler factors would preserve that order: none vanish on \(\Re s=1\). Meanwhile \(L_S(s,\mu^2)\) is bounded near \(1\), because \(\mu^2\ne1\), and \(\zeta_{K,S}\) has a simple pole. The displayed product would then be \(O((\sigma-1)^{4k-3})\), tending to zero as \(\sigma\downarrow1\). This contradicts its lower bound one.

The remaining case \(\mu=1\) is exactly the simple pole of \(\zeta_K\). Together with the quadratic case this exhausts all unitary characters. Twisting back proves the stated exception and all boundary nonvanishing. \(\square\)

## Exercises and complete solutions

1. **Easy.** Verify both residue formulas for \(\mathbb Q(i)\) and \(\mathbb Q(\sqrt2)\). Determine the latter's ring of integers, class number and regulator rather than assuming them.
2. **Medium.** Compute the root number from local factors for the quadratic characters \(\chi_{-4}\) and \(\chi_8\), including the finite and infinite phases separately.
3. **Medium.** Evaluate \(\zeta_K(0)\) for every imaginary quadratic field.
4. **Hard.** Reconstruct the norm-one volume from the unit lattice. Explain precisely the angular factor, the quotient by roots of unity, and the determinant used on the norm hyperplane.

**Solution 1.** The Gaussian case is (21). For the real quadratic case, an integral \(a+b\sqrt2\), with rational \(a,b\), has integral trace \(A=2a\), integral norm, and hence integral discriminant \(8b^2\). Writing \(b\) in lowest terms shows that its denominator divides two; write \(b=B/2\). Integrality of \((A^2-2B^2)/4\) forces \(B\) even, since odd \(B\) makes the numerator two or three modulo four; then it forces \(A\) even. Consequently the ring is \(\mathbb Z[\sqrt2]\). Its trace matrix in the basis \(1,\sqrt2\) is \(\operatorname{diag}(2,4)\), giving discriminant eight.

Rounding both coefficients of a quotient gives a remainder \(x+y\sqrt2\) with \(|x|,|y|\leq1/2\), and
\(|x^2-2y^2|\leq1/2<1\). The absolute norm is therefore Euclidean, so \(h=1\). The only roots of unity in a real field are \(\pm1\), giving \(w=2\). Let \(e=1+\sqrt2\), a unit of norm \(-1\). There is no positive unit \(u\) with \(1<u<e\): writing its conjugate as \(u'=\pm u^{-1}\), the integer \(a=(u+u')/2\) is positive and less than two, so is one; the integer \(b=(u-u')/(2\sqrt2)\) is positive, and \(a^2-2b^2=\pm1\) then forces \(b=1\), giving the excluded endpoint \(e\). Dividing any positive unit by a suitable power of \(e\) puts it in \([1,e)\), so it equals that power. Negative units are its negatives. Thus \(R=\log e\). Formulas (10) and (15) yield

\[
\kappa_{\mathbb Q(\sqrt2)}=2\log(1+\sqrt2),\quad
\operatorname{Res}_1\zeta_{\mathbb Q(\sqrt2)}
 =\frac{\log(1+\sqrt2)}{\sqrt2},\quad
\zeta_{\mathbb Q(\sqrt2)}(s)
 =-\frac{\log(1+\sqrt2)}2s+O(s^2).
\tag{22}
\]

**Solution 2.** Modulo four the nonzero character values at one and three are one and minus one. They give \(\tau=2i\), so the two-adic factor is \(\tau/\sqrt4=i\). Its real parity is odd, giving \(-i\); their product is one. Modulo eight, \(\chi_8\) has values \(1,-1,-1,1\) at \(1,3,5,7\). These define a multiplicative character on the unit group; it is primitive because the values at one and five differ although those residues agree modulo four. Its parity is even. Direct summation gives
\(e^{\pi i/4}-e^{3\pi i/4}-e^{5\pi i/4}+e^{7\pi i/4}=2\sqrt2\).
Thus its two-adic factor is \(2\sqrt2/\sqrt8=1\), its real factor is one, and again \(W=1\). Both uniformizer values are one because there is only one ramified prime in (16).

**Solution 3.** An imaginary quadratic field has \(r_1=0\), \(r_2=1\), and unit rank zero. With \(R=1\), (15) has exponent zero and gives \(\zeta_K(0)=-h_K/w_K\). In particular it is a value rather than a positive-order zero. Its discriminant affects the residue at one, but cancels from this value at zero.

**Solution 4.** Represent the identity ideal class by \(K_\infty^\times\times\widehat{\mathcal O}_K^\times\), whose intersection with the diagonal field is the unit group. Pass to norm one. In weighted logarithms the norm is their sum, and deleting the last logarithm while retaining this sum has determinant one. The norm-one logarithmic measure is therefore exactly the measure defining \(R\). Real signs each have mass one; each complex circle has mass two by (12); their total is \(2^{r_1+r_2}\). The finite units have mass one. A logarithmic fundamental parallelepiped for a lifted free unit basis contributes \(R\), despite any angular or finite-unit translations in those lifts. Quotient by the remaining \(w\) roots of unity divides this mass by \(w\), because the action is free and the subgroup uses counting measure. Finally (11) gives \(h\) disjoint cosets of equal mass. This proves (10), including unit rank zero. It also explains why replacing (10) by the analytic residue would insert factors absent from the actual multiplicative measure.

## Sources and scope

The mathematical inputs from this course are the character construction, the two local functional equations, global continuation with its exact residues, and the ideal-class and unit-lattice results. Their applications and every displayed assertion above are proved here. A. V. Sutherland, [*The analytic class number formula*](https://ocw.mit.edu/courses/18-785-number-theory-i-fall-2021/mit18_785f21_lec19.pdf), MIT 18.785, Lecture 19, Theorem 19.12, gives the ideal-theoretic class-number comparison, and E. Hecke, [*Eine neue Art von Zetafunktionen und ihre Beziehungen zur Verteilung der Primzahlen (Zweite Mitteilung)*](https://gdz.sub.uni-goettingen.de/download/pdf/PPN266833020_0006/LOG_0008.pdf), Mathematische Zeitschrift 6 (1920), §6, gives the Hecke-series comparison. Bjorn Poonen, [*Tate’s Thesis*, MIT 18.786, Spring 2015](https://math.mit.edu/~poonen/786/notes.pdf), §5.11, Theorem 5.22, gives the Tate-integral comparison.

The classical theta method developed by Hecke offers a useful second way to organize the same mathematics. In Hecke's paper, §4 treats primitive residue-class characters and their Gauss-type sums, §5 proves the transformation formula of the corresponding theta series, and §6 averages over a logarithmic fundamental domain of the units before taking a Mellin transform. The transformation and the two parts of the Mellin integral, split at \(u=1\), give the functional equation (44) there, with analytic scale \(D\,N(\mathfrak f)\). This comparison treats arbitrary number fields and keeps the complex embeddings and unit contribution; the complete adèlic proof (4) remains the one used here.

P. Deligne, [*Les constantes des équations fonctionnelles des fonctions L*, IAS edition](https://publications.ias.edu/sites/default/files/Number20.pdf), §§3.3–3.4, 3.11 and 5.3–5.9 532 and 548–550, provides the rank-one local-constant and global product comparison. Its positive infinite basic-character convention requires the conversion used in (7). Poonen, Remark 5.21, and James-Michael Leahy, [*An introduction to Tate’s Thesis* (2010)](https://www.math.mcgill.ca/darmon/theses/leahy/thesis.pdf), Proposition 4.6.1 and the proof of Theorem 4.10.4, distinguish Haar scaling from character rescaling. For the full local character \(c=\omega_v|\cdot|_v^s\), the multiplier at fixed additive measure is \(c(a)|a|_v^{-1}=\omega_v(a)|a|_v^{s-1}\). Updating that measure to remain self-dual contributes \(|a|_v^{1/2}\), giving \(\omega_v(a)|a|_v^{s-1/2}\). The product over a diagonal \(a\in K^\times\) is one by diagonal triviality and the product formula, as proved above.

The boundary statement is proved in Theorem 10.6, using Euler-product positivity in addition to analytic continuation. Sutherland, Lecture 19, Theorem 19.16, gives the narrower Dirichlet nonvanishing assertion at one. The positive-coefficient argument in Lemma 10.5 is Landau’s argument: a Taylor expansion at a regular boundary point, followed by positivity and monotone summation, would force convergence to the left of the abscissa. The full ideal-series argument and the unitary-character boundary proof are supplied here. Higher-dimensional local constants, an explicit formula, and an Artin–Hecke comparison remain further directions.

Leahy, §4.10, Theorem 4.10.4, and §4.11, Theorem 4.11.3 give another local-to-global and quotient-volume comparison. With the multiplicative measures displayed by Poonen and Leahy, the corresponding norm-one volume is \(\pi^{r_2}\kappa/\sqrt D\). Leahy’s complex \(L\)-factor in (4.10) is half of our \(\Gamma_{\mathbb C}\); the constant \(2^{r_2}\) relating completions cancels from their functional equations. Formula (10) and both Dedekind residues above retain our measure and Gamma normalization.
