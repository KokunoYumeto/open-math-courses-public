# Tate's global theory: continuation and functional equation

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The global functional equation comes from Poisson summation on the additive adèles. To apply it to a multiplicative integral, first sum the test function over the nonzero elements of the number field. This turns the integral into one over the idèle class group. Its compact norm-one fibres make the large-norm part entire; the two terms at additive zero account for every possible pole.

Throughout, \(K\) is an arbitrary number field of degree \(d\), \(\mathbb A_K\) its adèle ring, \(J_K=\mathbb A_K^\times\), and \(C_K=J_K/K^\times\). We import the compactness of \(C_K^1=\ker(|\cdot|:C_K\to\mathbb R_{>0})\) from Theorem 3.3 of [Idèles and the idèle class group](NT-ADL-03.md), and the product formula and additive Poisson summation from [Additive characters, self-dual measures and Poisson summation on the adèles](NT-ADL-05.md). Its additive measure has \(\operatorname{vol}(\mathbb A_K/K)=1\).

Fix a unitary character \(\omega:C_K\to\mathbb T\), viewed also as a character of \(J_K\) trivial on \(K^\times\), and let
\[
 c_s(x)=\omega(x)|x|^s,\qquad
 \check c_s(x)=\omega(x)^{-1}|x|^{1-s}.
 \tag{1}
\]
Every global quasi-character belongs to such a family by Proposition 6.2 of [Quasi-characters and Hecke characters](NT-ADL-06.md). The Fourier transform uses the fixed global additive character and self-dual measure of the additive lesson, so \(\widehat{\widehat f}(x)=f(-x)\).

## Multiplicative measures and norm fibres

At every finite place normalize \(d^\times x_v\) so that \(\operatorname{vol}(\mathcal O_v^\times)=1\). At real and complex places use the multiplicative measures of [Tate's local theory at the infinite places](NT-ADL-08.md). They give respectively \(dx/|x|\) and \(2\,du\,dv/(\pi|z|_{\mathbb C})\). Their restricted product is a Haar measure \(d^\times x\) on \(J_K\); this means the product measure on each finite-place chart, with its compact unit tail of mass one. No infinite product of local additive-to-multiplicative constants is needed.

Give the discrete subgroup \(K^\times\) counting measure. The quotient Haar measure \(d^\times\bar x\) on \(C_K\) is specified by Weil's integration formula
\[
 \int_{J_K}H(x)d^\times x
   =\int_{C_K}\sum_{\alpha\in K^\times}H(\alpha x)
                                                d^\times\bar x.
 \tag{2}
\]
It holds for nonnegative measurable \(H\), allowing infinite values, and hence for integrable complex \(H\). This is the quotient Haar integration result used in the restricted-product lesson; it also follows by partitioning into neighbourhoods on which the discrete quotient map is injective, and then applying countable additivity.

We choose a particularly useful continuous homomorphic section of the norm. Let \(a(t)\) have finite components one and every infinite component the positive real scalar \(t^{1/d}\). A real place contributes one power and a complex place two, so
\[
 |a(t)|=t,\qquad
 C_K\simeq C_K^1\times\mathbb R_{>0},\quad
 (u,t)\longmapsto u\bar a(t).
 \tag{3}
\]
There is a unique Haar measure \(du\) on \(C_K^1\) for which \(d^\times\bar x=du\,dt/t\) under (3). Put
\[
 \kappa=\int_{C_K^1}du.
 \tag{4}
\]
It is finite and positive because this group is compact. The chosen multiplicative local measures determine \(\kappa\); its arithmetic value will be computed in the next lesson. Replacing the section \(a(t)\) by another norm section only translates each fibre by an element of \(C_K^1\). Translation preserves \(du\), so \(\kappa\) is independent of that change when \(dt/t\) and the original quotient measure are fixed.

To compare quotient volumes with Poonen, §5.9, and Leahy, §4.9, their finite unit masses contribute \(|d_K|^{-1/2}\), and their complex multiplicative measures contribute \(\pi^{r_2}\), relative to ours. Their global measure and norm-one volume are therefore multiplied by \(\lambda=\pi^{r_2}|d_K|^{-1/2}\). The zeta integral and both residues in (21) are multiplied by this same scalar. Here \(\kappa\) always denotes the volume for (1)–(3), so the continuation proof carries its own measure without suppressing a discriminant or complex-place constant.

## Convergence on the idèles

For \(f\in\mathcal S(\mathbb A_K)\), define
\[
 Z(f,\omega,s)=\int_{J_K}f(x)\omega(x)|x|^s d^\times x.
 \tag{5}
\]
The test space is the finite algebraic tensor product of locally constant compactly supported functions on the finite adèles with the Schwartz space on \(K_\infty\). A Schwartz function on \(K_\infty\) need not be a finite sum of products over the infinite places. The following domination includes this case.

**Proposition 9.1.** The integral (5) converges absolutely for \(\operatorname{Re}s>1\), locally uniformly there, and defines a holomorphic function. If \(f=\bigotimes_v f_v\) is a product over individual places, with \(f_v=\mathbf1_{\mathcal O_v}\) almost everywhere at finite places, then
\[
 Z(f,\omega,s)=\prod_v Z(f_v,\omega_v|\cdot|_v^s)
 \tag{6}
\]
in that half-plane. Both its integral and its product are absolutely convergent.

*Proof.* A compactly supported locally constant function on the finite adèles is a finite sum of product-rectangle indicators, with the standard integral-ring factors outside a finite set. Thus it suffices to treat \(f=f_{\mathrm{fin}}f_\infty\), where its finite factor is a bounded product with compact local supports. Enlarge the finite exceptional set \(S\) to include every ramified component of \(\omega\). These are finitely many by Proposition 6.2.

Write \(r_v\) for the ordinary real radius at an infinite place. For any chosen \(M\), the Schwartz estimates on the whole real vector space \(K_\infty\) imply
\[
 |f_\infty(x_\infty)|
       \leq A_M\prod_{v\mid\infty}(1+r_v)^{-M}.
 \tag{7}
\]
Indeed the product of \((1+r_v)^M\) is bounded by a fixed power of \(1+\|x_\infty\|\). Each resulting local multiplicative integral converges at zero for \(\sigma=\operatorname{Re}s>0\); at infinity it converges if \(M>2\sigma\), which suffices at both kinds of infinite place. Every exceptional finite local integral is finite for \(\sigma>0\) by Proposition 7.1, applied to a bounding compact indicator.

At a remaining finite place, unitary unramified \(\omega_v\) has absolute value one. The integral of the positive majorant is
\[
 \int_{K_v^\times}\mathbf1_{\mathcal O_v}(x)|x|_v^\sigma
                    d^\times x=(1-q_v^{-\sigma})^{-1}.
 \tag{8}
\]
The product of these numbers converges for \(\sigma>1\), without assuming a Dedekind zeta continuation. Above any rational prime \(p\) there are at most \(d\) prime ideals and their norms are \(p^e\) with \(e\geq1\). Hence every finite partial product is bounded by
\[
 \prod_p(1-p^{-\sigma})^{-d}
                   =\left(\sum_{m\geq1}m^{-\sigma}\right)^d<\infty.
 \tag{9}
\]
The elementary rational Euler product here follows by expanding finite products and unique factorization, with the convergent positive series bounding them.

Exhaust the restricted-product idèles by the charts allowing arbitrary components at an increasing finite set of places and units elsewhere. Tonelli on each chart gives the product of the positive local integrals. Monotone convergence and (9) prove the global absolute bound for (7), hence for \(f\). This proves convergence for every finite sum in the test space. If \(f\) itself is a product over all places, ordinary Fubini on the charts followed by this absolute bound gives (6).

On a compact parameter set in \(\operatorname{Re}s>1\), choose \(1<\sigma_0\leq\operatorname{Re}s\leq\sigma_1\). Split according to \(|x|\leq1\) and \(|x|\geq1\) and use the majorants at \(\sigma_0\) and \(\sigma_1\). Slightly enlarging this closed interval still within \(\operatorname{Re}s>1\) absorbs every power of \(|\log|x||\). Differentiation under the integral is justified, proving local uniform convergence and holomorphy. ∎

By (2), in the initial half-plane the same integral is
\[
 Z(f,\omega,s)=\int_{C_K}E_f(x)\omega(x)|x|^s d^\times\bar x,
 \qquad E_f(x)=\sum_{\alpha\in K^\times}f(\alpha x).
 \tag{10}
\]
The absolute convergence just proved justifies unfolding this complex integral. For a nonnegative integrand, (2) permits the same unfolding before finiteness is known.

## Uniform control of the nonzero theta sum

**Theta lemma.** The series defining \(E_f\) converges absolutely and locally uniformly on \(C_K\). For every \(B>0\), there is a constant \(A_B\) such that
\[
 \sum_{\alpha\in K^\times}|f(\alpha x)|
                  \leq A_B |x|^{-B}\qquad(|x|\geq1).
 \tag{11}
\]
Consequently
\[
 G(f,\omega,s):=\int_{|x|\geq1}E_f(x)\omega(x)|x|^s
                                                d^\times\bar x
 \tag{12}
\]
is entire. The original idèlic integral (5) restricted to \(|x|\geq1\) is entire as well, and equals (12).

*Proof.* First choose a compact set of lifts of the compact group \(C_K^1\) inside \(J_K^1\). Such a set exists: since \(K^\times\) is discrete, each point of the quotient has a neighbourhood lifted injectively from a relatively compact neighbourhood in \(J_K^1\). Finitely many such neighbourhoods cover \(C_K^1\); the union of their closures gives the required compact lift \(H\).

Treat \(f=f_{\mathrm{fin}}f_\infty\); finite sums follow by addition. Let \(D\) be the compact support of its finite factor. As \(h\) ranges over \(H\), the sets \(h_{\mathrm{fin}}^{-1}D\) lie in a single compact subset of \(\mathbb A_{K,\mathrm{fin}}\), by continuity of multiplication and inversion on the idèles. This subset lies in \(m^{-1}\widehat{\mathcal O_K}\) for some positive integer \(m\). Thus every \(\alpha\) contributing to \(f(\alpha h a(t))\) belongs to the fixed fractional-ideal lattice
\[
 I=m^{-1}\mathcal O_K\subset K_\infty.
 \tag{13}
\]
The lattice property is Proposition 2.4 of the adèle-ring lesson. Compactness of \(H\) also bounds the infinite multiplication operators \(h_\infty\) uniformly away from singularity: for some \(b>0\), \(\|h_\infty y\|\geq b\|y\|\) for all \(h\in H\).

Put \(\lambda=t^{1/d}\). The finite factor is bounded, and the Schwartz estimates give, uniformly in \(h\),
\[
 |f(\alpha h a(t))|\leq A_N(1+b\lambda\|\alpha\|)^{-N}.
 \tag{14}
\]
A lattice has \(O(R^d)\) points in a ball of radius \(R\): disjoint small balls around its points fit inside a slightly larger ball. Its nonzero points also have norms bounded away from zero. Splitting into dyadic annuli therefore shows \(\sum_{0\ne\alpha\in I}\|\alpha\|^{-N}<\infty\) for \(N>d\). For \(t\geq1\), summing (14) is consequently bounded by a constant times \(\lambda^{-N}=t^{-N/d}\). Taking \(N>\max(d,dB)\) proves (11).

The same bound proves locally uniform convergence when \(t\) stays in any compact subinterval of \((0,\infty)\), since \(\lambda\) then has a positive lower bound. Hence \(E_f\) is continuous on the quotient. For (12), use (3), \(|\omega|=1\), and (11): on any compact parameter set it is bounded by \(\kappa A_B\int_1^\infty t^{\operatorname{Re}s-B}dt/t\), with \(B\) as large as needed. Powers of \(\log t\) are absorbed by increasing \(B\), so parameter differentiation gives an entire function. Applying the nonnegative version of (2) to \(|f|\mathbf1_{|x|\geq1}\) gives exactly the same finite bound for the original idèlic large-norm integral. It can therefore be unfolded for every parameter, with the same holomorphy argument. ∎

The balancing in \(a(t)\) expands every infinite coordinate at the same ordinary rate \(t^{1/d}\). Compactness absorbs the unit and class-group directions into \(H\), and then a single fractional-ideal lattice suffices. This is the number-field input needed beyond a calculation over \(\mathbb Q\).

## Compact averaging and the two correction terms

**Lemma 9.3.** With the measure in (4),
\[
 \int_{C_K^1}\omega(u)du=
 \begin{cases}
 \kappa,&\omega|_{C_K^1}=1,\\
 0,&\omega|_{C_K^1}\ne1.
 \end{cases}
 \tag{15}
\]

*Proof.* The first case is the integral of the constant function one. In the second choose \(v\in C_K^1\) with \(\omega(v)\ne1\). Translation invariance makes the integral equal to its product with \(\omega(v)\); it is finite, so it must vanish. ∎

For an idèle \(x\), Poisson summation on \(K\subset\mathbb A_K\), applied to \(y\mapsto f(xy)\), gives
\[
 E_f(x)=|x|^{-1}E_{\widehat f}(x^{-1})
                       +|x|^{-1}\widehat f(0)-f(0).
 \tag{16}
\]
The Fourier transform of that scaled test is \(|x|^{-1}\widehat f(y/x)\), by additive change of variables. Removing its term at zero gives (16); this is also the adèlic Riemann–Roch identity of Theorem 5.5. Notice that it is the nonzero sum \(E_f\) that decays in (11). The sum including zero tends to \(f(0)\).

If \(\omega|_{C_K^1}=1\), the character factors through the norm and has the form
\[
 \omega(x)=|x|^{i\tau},\qquad \tau\in\mathbb R,
 \tag{17}
\]
by the classification of characters of \(\mathbb R_{>0}\). Define a meromorphic correction
\[
 P(f,\omega,s)=
 \begin{cases}
 \displaystyle\kappa\left(
 \frac{\widehat f(0)}{s+i\tau-1}-\frac{f(0)}{s+i\tau}\right),
                       &\omega=|\cdot|^{i\tau},\\[4pt]
 0,&\omega|_{C_K^1}\ne1.
 \end{cases}
 \tag{18}
\]

**Theorem 9.2 (Tate).** For every \(f\in\mathcal S(\mathbb A_K)\), the integral (5) has meromorphic continuation to all \(s\), given by
\[
 Z(f,\omega,s)=G(f,\omega,s)
                +G(\widehat f,\omega^{-1},1-s)+P(f,\omega,s).
 \tag{19}
\]
It satisfies
\[
 Z(f,\omega,s)=Z(\widehat f,\omega^{-1},1-s).
 \tag{20}
\]
If \(\omega\) is nontrivial on \(C_K^1\), the continuation is entire. Otherwise it has at most simple poles at \(s=-i\tau\) and \(s=1-i\tau\), with respective residues
\[
 -\kappa f(0),\qquad \kappa\widehat f(0).
 \tag{21}
\]
A pole is absent when its stated residue is zero.

*Proof.* Start in \(\operatorname{Re}s>1\), where unfolding is justified by Proposition 9.1. Split the quotient integral (10) at norm one. The norm-one fibre itself has measure zero, since the norm coordinate has measure \(dt/t\). The large part is (12). Apply (16) to the small part. Its nonzero transformed-sum term becomes
\[
 \int_{|x|<1}E_{\widehat f}(x^{-1})\omega(x)|x|^{s-1}
                                          d^\times\bar x
             =G(\widehat f,\omega^{-1},1-s),
 \tag{22}
\]
by inversion on \(C_K\), which preserves Haar measure. All these integrals are absolutely convergent: the transformed sum is bounded by (11) after inversion, and the zero terms are integrable at \(t=0\) when \(\operatorname{Re}s>1\).

Integrate the correction terms on the fibres in (3). If \(\omega|_{C_K^1}\ne1\), Lemma 9.3 gives zero. Otherwise (17) gives the two elementary integrals
\[
 \kappa\widehat f(0)\int_0^1t^{s+i\tau-1}\frac{dt}{t}
   -\kappa f(0)\int_0^1t^{s+i\tau}\frac{dt}{t},
 \tag{23}
\]
which evaluate to (18). This proves (19) in the initial half-plane. Both \(G\)-terms are entire by the theta lemma, so (19) gives the asserted continuation and all possible residues.

To prove (20), apply (19) to \(\widehat f,\omega^{-1},1-s\). Its two \(G\)-terms interchange, because \(\widehat{\widehat f}(y)=f(-y)\) and \(E_{f(-\cdot)}=E_f\) by reindexing \(\alpha\mapsto-\alpha\). If the character is nontrivial on \(C_K^1\), both correction terms vanish. In the other case put \(z=s+i\tau\); the transformed correction is
\[
 \kappa\left(\frac{f(0)}{-z}
                       -\frac{\widehat f(0)}{1-z}\right)
   =\kappa\left(\frac{\widehat f(0)}{z-1}
                       -\frac{f(0)}{z}\right),
 \tag{24}
\]
the original correction. This proves the functional equation meromorphically everywhere. ∎

The initial global convergence regions for the two sides of (20) do not overlap: they are \(\operatorname{Re}s>1\) and \(\operatorname{Re}s<0\). Equation (19) constructs their common continuation. Thus (20) equates meromorphic continuations, with the integral interpretation available in each side's own initial region.

## The rational Gaussian and the completed zeta function

Take \(K=\mathbb Q\), \(\omega=1\), and
\[
 f(x)=e^{-\pi x_\infty^2}\mathbf1_{\widehat{\mathbb Z}}
                                      (x_{\mathrm{fin}}).
 \tag{25}
\]
It is self-dual, by Propositions 5.2 and 7.1 with the standard rational characters. The description \(C_{\mathbb Q}\simeq\widehat{\mathbb Z}^{\times}\times\mathbb R_{>0}\) in Proposition 3.6 also checks the quotient measure: \(\widehat{\mathbb Z}^{\times}\times\mathbb R_{>0}\) is a fundamental set for the discrete rational multiplicative action. Its finite units have mass one and its positive real coordinate has measure \(dt/t\). Therefore \(\kappa=1\).

Proposition 9.1 and the local Gaussian and shell calculations give
\[
 Z(f,1,s)=\Gamma_{\mathbb R}(s)\zeta(s)=:\Lambda(s)
                       \qquad(\operatorname{Re}s>1).
 \tag{26}
\]
Here \(f(0)=\widehat f(0)=1\). If
\[
 A(s)=\int_1^\infty
       2\sum_{m\geq1}e^{-\pi m^2t^2}\,t^s\frac{dt}{t},
 \tag{27}
\]
then \(A\) is entire, and (19) becomes
\[
 \Lambda(s)=A(s)+A(1-s)+\frac1{s-1}-\frac1s.
 \tag{28}
\]
Thus \(\Lambda(s)=\Lambda(1-s)\), with simple poles of residues \(-1\) and \(+1\) at zero and one. The commonly used entire xi function is
\[
 \xi(s)=\tfrac12s(s-1)\Lambda(s).
 \tag{29}
\]
It satisfies the same symmetry and has \(\xi(0)=\xi(1)=1/2\). Formula (28) makes the distinction between the meromorphic completion and the entire xi function explicit.

The finite-adèlic integral appearing in the Bost–Connes construction is another application of Proposition 9.1's Euler-product bound. With finite multiplicative unit volume one,
\[
 \int_{\mathbb A_{\mathbb Q,\mathrm{fin}}^\times}
 \mathbf1_{\widehat{\mathbb Z}}(j)|j|^\beta d^\times j
                                      =\zeta(\beta),\qquad\beta>1.
 \tag{30}
\]
Division by \(\zeta(\beta)\) therefore normalizes its mass on \(\widehat{\mathbb Z}\) to one. The extension of that normalized finite-adèlic measure to other temperatures and its positivity are part of the Bost–Connes measure theory; they are not consequences merely of the global meromorphic identity (20). This is the zeta-integral connection described in [Bost–Connes 1995, §3].

## Exercises

1. **Easy.** Carry out the rational Gaussian example, determine both residues, and explain why the usual \(\xi\) function is entire.
2. **Medium.** Prove that the original idèlic integral over \(|x|\geq1\) is entire for every Schwartz test. Justify both its unfolding and differentiation in \(s\).
3. **Medium.** Prove Lemma 9.3, then deduce the precise exceptional unitary characters that can produce poles in Theorem 9.2.
4. **Hard.** Prove absolute convergence for an arbitrary \(f\in\mathcal S(\mathbb A_K)\) when \(\operatorname{Re}s>1\), allowing its infinite factor to be a general Schwartz function on \(K_\infty\). Establish locally uniform convergence and the factorization statement for individual-place product tests.

## Solutions

**Solution 1.** At every finite rational place the standard integral-ring test has integral \((1-p^{-s})^{-1}\); at infinity the Gaussian integral is \(\pi^{-s/2}\Gamma(s/2)\). Proposition 9.1 justifies multiplication of these integrals for \(\operatorname{Re}s>1\), proving (26). The Fourier transform of each local test is itself, and \(\kappa=1\) by the rational quotient measure above. The nonzero rational theta sum on a positive norm representative \(t\) is \(2\sum_{m\geq1}e^{-\pi m^2t^2}\), independent of its finite unit component. Unfolding the large part gives (27), so (19) proves (28). The two entire terms add no poles. The rational terms have residues \(-1\) at zero and \(+1\) at one. Multiplication by \(s(s-1)/2\) cancels both simple poles, and the resulting limits at both endpoints are \(1/2\). The product is entire elsewhere already, and \(s(s-1)\) is unchanged under \(s\mapsto1-s\). Thus \(\xi\) is entire and symmetric.

**Solution 2.** Apply the nonnegative quotient formula (2) to \(H(x)=|f(x)|\mathbf1_{|x|\geq1}|x|^\sigma\). It gives an equality, possibly infinite at first, with the quotient integral of the absolute theta sum. For arbitrary real \(\sigma\), (11) bounds the latter by \(\kappa A_B\int_1^\infty t^{\sigma-B}dt/t<\infty\) when \(B>\sigma\). Hence the original restricted integral is absolutely convergent for every parameter and can be unfolded to (12). For any compact set of complex parameters choose one \(B\) larger than their largest real part by a positive margin. Each parameter derivative introduces \((\log t)^m\), which is integrable against \(t^{\sigma-B}dt/t\); one can increase \(B\) for any desired derivative. The same nonnegative unfolding bounds these derivatives before exchanging them with the original idèlic integral. Dominated differentiation proves that both expressions are entire. This argument uses compact norm fibres and the uniform bound, not just pointwise decay on \(J_K\).

**Solution 3.** If \(\omega\) is trivial on \(C_K^1\), its integral is \(\kappa\). Otherwise choose \(v\) on which it has value different from one. Haar translation gives \(I=\omega(v)I\); finiteness of \(I\) forces \(I=0\). Triviality on the kernel of the norm makes \(\omega\) factor continuously through \(C_K/C_K^1\simeq\mathbb R_{>0}\). Pull back by the exponential map: every continuous unitary character of the additive real line is \(t\mapsto e^{i\tau t}\), so \(\omega(x)=|x|^{i\tau}\). Conversely every such character is trivial on \(C_K^1\). Exactly these characters allow the correction (18), with possible poles at \(-i\tau\) and \(1-i\tau\). If \(f(0)=0\) or \(\widehat f(0)=0\), the corresponding possible pole disappears; for other unitary characters the entire terms are the whole continuation.

**Solution 4.** Express the finite factor as a finite sum of compact product-rectangle indicators. It is enough to bound one such term times a general \(f_\infty\in\mathcal S(K_\infty)\). For any sufficiently large \(M\), the Schwartz seminorm with a power larger than \(M\) times the number of infinite places gives (7). Its local infinite integrals are bounded at zero by \(\int_0^1r^{\sigma-1}dr\) at a real place and by a constant times \(\int_0^1r^{2\sigma-1}dr\) at a complex place; the decay in (7) makes infinity integrable for \(M>2\sigma\). At the finitely many exceptional finite places, compact-support shell sums converge for \(\sigma>0\). At every other place their value is (8).

For the tail, group prime ideals over rational primes. There are at most \(d\) over \(p\), each with norm at least \(p\), giving the convergent majorant (9) when \(\sigma>1\). Positive Fubini on an increasing exhaustion by finite-place idèle charts and monotone convergence now bound the full integral of the majorant. This proves absolute convergence for the chosen term and then for every finite sum. On a compact parameter set choose real bounds \(1<\sigma_0\leq\operatorname{Re}s\leq\sigma_1\); the two integrable weights at these endpoints dominate after splitting at norm one. Choose endpoints a little wider to absorb powers of the norm logarithm, establishing locally uniform holomorphy. Finally, when the test is a product at individual places, Fubini on the same charts computes each partial product. The absolute majorant permits passage to the full product and proves (6). The proof does not assume an algebraic tensor decomposition of a general infinite-place Schwartz function.

## Prerequisites and further directions

- Compactness of \(C_K^1\), the norm decomposition, and the rational class normalization are imported from Theorem 3.3 and Propositions 3.5–3.6. The fractional-ideal lattice property is Proposition 2.4. The compact lifts and uniform lattice estimates needed here are explained in the theta lemma.
- Additive self-duality, preservation of the global Schwartz space under Fourier transformation, and Poisson summation with covolume one are imported from Propositions 5.1–5.3 and Theorems 5.4–5.5. Local quasi-character factorization is Proposition 6.2; finite shell convergence is Proposition 7.1, and the infinite tests and measures are Proposition 8.2 and its normalization table.
- Quotient Haar integration with discrete counting measure is Theorem 4.1 of Subgroups, quotients and annihilators, applied to \(K^\times\subset J_K\). Tonelli's theorem and dominated differentiation are measure-theory prerequisites. All global convergence, uniform theta bounds, meromorphic continuation, averaging, and residues asserted in this lesson are proved above.
- The arithmetic evaluation of \(\kappa\), completed general Hecke L-functions, conductor and root numbers, and the Dedekind class-number formula belong to the next lesson. Weil's explicit formulas and the positivity of the continued Bost–Connes measures are separate results, located in the references but not imported as proofs of Theorem 9.2.

## References

- Bjorn Poonen, [*Tate’s Thesis*, MIT 18.786, Spring 2015](https://math.mit.edu/~poonen/786/notes.pdf), §§5.9–5.10, Theorem 5.16, PDF pages 34–37; and James-Michael Leahy, [*An introduction to Tate’s Thesis* (2010)](https://www.math.mcgill.ca/darmon/theses/leahy/thesis.pdf), §4.9, Theorem 4.9.2, PDF pages 169–176: quotient measures, continuation and the functional equation. The compact-lift and balanced-scaling proof here gives the uniform estimate for the whole archimedean Schwartz space of every number field; a possible pole is absent when its stated residue is zero.
- E. Hecke, [*Eine neue Art von Zetafunktionen und ihre Beziehungen zur Verteilung der Primzahlen (Zweite Mitteilung)*](https://gdz.sub.uni-goettingen.de/download/pdf/PPN266833020_0006/LOG_0008.pdf), Mathematische Zeitschrift 6 (1920), 11–51, §§4–6: the number-field theta method for Größencharaktere, with Gauss-type sums, the theta transformation formula and averaging over the units. We use the directly proved adèlic identity (19).
- J. R. Getz and H. Hahn, [*An Introduction to Automorphic Representations*, April 22, 2022 draft](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), Appendix B §§B.1–B.3, PDF pages 501–505, especially the whole archimedean block in §B.3 and Theorem B.3.2.
- A. Connes and M. Marcolli, [*Noncommutative Geometry, Quantum Fields and Motives*, author version](https://alainconnes.org/wp-content/uploads/bookwebfinal-2.pdf), Chapter 2, §§8.1–8.4, (2.274)–(2.283) and (2.297)–(2.305), PDF pages 364–367: characters and the Fourier–Mellin transform on the idèle class group. The principal-value explicit formula in §8.2 is a further theorem.
- J.-B. Bost and A. Connes, [*Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, author scan](https://alainconnes.org/wp-content/uploads/bostconnesscan.pdf), 1995, §3, (11) PDF page 15: the normalized finite-adèlic integral. Its ordinary integral interpretation is for \(\beta>1\); continued positivity requires the separate measure theory indicated above.
