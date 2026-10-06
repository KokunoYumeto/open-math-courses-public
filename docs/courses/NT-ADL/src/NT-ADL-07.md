# Tate's local theory at the finite places

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A local zeta integral is a multiplicative integral of an additive test function. Fourier transformation exchanges its character with the inverse character multiplied by the norm. The extra norm comes from additive change of variables. At an unramified place this gives a ratio of two geometric series; at a ramified place a finite Gauss sum supplies the factor.

Let \(F\) be any finite extension of \(\mathbb Q_p\). Write \(\mathcal O\) for its integral ring, \(\mathfrak p=\pi\mathcal O\) for its maximal ideal, \(q=|\mathcal O/\mathfrak p|\), and \(|\pi|=q^{-1}\). The classification and conductor of its quasi-characters come from [Quasi-characters and Hecke characters](NT-ADL-06.md). The local Fourier inversion and indicator transforms come from [Additive characters, self-dual measures and Poisson summation on the adèles](NT-ADL-05.md). Our formulas apply to every such \(F\), including its ramified extensions, rather than only to the rational completions.

## The measures and the test space

Let \(\psi:F\to\mathbb T\) be a nontrivial additive character. Define its conductor integer by
\[
 n=n(\psi)=\max\{r\in\mathbb Z:
                      \psi(\pi^{-r}\mathcal O)=1\}.
 \tag{1}
\]
Thus \(\pi^{-n}\mathcal O\) is the largest fractional ideal on which it is trivial. The integer \(n\) may be negative. For the number-field character \(\psi_F=\psi_{\mathbb Q_p}\circ\operatorname{Tr}_{F/\mathbb Q_p}\), it is the exponent \(d\) of the different \(\mathfrak D_F=\pi^d\mathcal O\).

We begin with the self-dual additive measure \(dx_\psi\), and write \(dx=\lambda dx_\psi\) for a general positive Haar measure, where \(\lambda>0\). Put \(m=\operatorname{vol}_{dx}(\mathcal O)\). These are the conventions throughout:

| Object | Normalization |
|---|---|
| Absolute value | \(\lvert\pi\rvert=q^{-1}\) |
| Basic rational character | \(\psi_{\mathbb Q_p}(x)=\exp(2\pi i\{x\}_p)\) |
| Number-field character | \(\psi_F=\psi_{\mathbb Q_p}\circ\operatorname{Tr}_{F/\mathbb Q_p}\), with \(n=d\) |
| Self-dual additive measure | \(\operatorname{vol}(\mathcal O)=q^{-n/2}\) |
| General additive measure | \(dx=\lambda dx_\psi\), hence \(m=\lambda q^{-n/2}\) |
| Multiplicative measure | \(d^\times x=\kappa\,dx/\lvert x\rvert\), where \(\kappa=[m(1-q^{-1})]^{-1}\); thus \(\operatorname{vol}(\mathcal O^\times)=1\) |
| Fourier transformation | \(\widehat f(y)=\int_F f(x)\psi(xy)\,dx\) |
| Dual quasi-character | \(\check c=c^{-1}\lvert\cdot\rvert\) |

To check the measure entry for arbitrary \(\psi\), local self-duality expresses it as \(\psi_F(ax)\) for some \(a\in F^\times\). Its conductor is \(n=d+\operatorname{ord}(a)\), and its self-dual measure is \(|a|^{1/2}dx_{\psi_F}\), of integral-ring mass \(q^{-n/2}\). The multiplicative normalization follows from \(\operatorname{vol}_{dx}(\mathcal O^\times)=m(1-q^{-1})\). Multiplying \(d^\times x\) by a constant multiplies both zeta integrals by that constant and leaves their ratio unchanged.

Let \(\mathcal S(F)\) be the space of locally constant complex functions of compact support. Every member is a finite linear combination of indicators of cosets of some \(\pi^r\mathcal O\): a compact support can be covered by finitely many constant neighborhoods, and these neighborhoods may all be shrunk to the same open additive subgroup. Character orthogonality gives
\[
 \widehat{\mathbf1_{a+\pi^r\mathcal O}}(y)
   =m q^{-r}\psi(ay)
                         \mathbf1_{\pi^{-r-n}\mathcal O}(y).
 \tag{2}
\]
The right side is again locally constant and compactly supported. Thus Fourier transformation preserves \(\mathcal S(F)\), and the inversion theorem gives
\[
 \widehat{\widehat f}(x)=\lambda^2 f(-x).
 \tag{3}
\]
In particular the self-dual convention has \(\lambda=1\).

## A finite part and a geometric tail

For a quasi-character \(c\), set \(A=c(\pi)\), \(\eta=c|_{\mathcal O^\times}\), and \(\sigma=\sigma(c)\). Thus \(|A|=q^{-\sigma}\) and \(\eta\) is a finite-image unitary character. Define
\[
 Z(f,c)=\int_{F^\times}f(x)c(x)\,d^\times x.
 \tag{4}
\]

**Proposition 7.1.** The integral (4) is absolutely convergent for \(\sigma(c)>0\). Fixing \(\eta\) and varying \(A\in\mathbb C^\times\), its continuation is a rational function of \(A\). In a family \(c=c_0|\cdot|^s\), it is therefore rational in \(q^{-s}\). More precisely, define
\[
 L(c)=
 \begin{cases}
 (1-A)^{-1},&\eta=1,\\
 1,&\eta\ne1.
 \end{cases}
 \tag{5}
\]
Then \(Z(f,c)/L(c)\) is a Laurent polynomial in \(A\), and all such integrals generate \(L(c)\mathbb C[A,A^{-1}]\) as a module over \(\mathbb C[A,A^{-1}]\).

*Proof.* Write \(F^\times=\coprod_{j\in\mathbb Z}\pi^j\mathcal O^\times\). Each shell has multiplicative volume one. Compact support makes \(f\) zero on all shells below some \(j_0\), and local constancy at zero gives \(f(\pi^j u)=f(0)\) for all units \(u\) and all sufficiently large \(j\geq J\). Therefore
\[
 Z(f,c)=\sum_{j=j_0}^{J-1}A^j
       \int_{\mathcal O^\times}f(\pi^j u)\eta(u)\,d^\times u
       +f(0)\sum_{j\geq J}A^j
                     \int_{\mathcal O^\times}\eta(u)\,d^\times u.
 \tag{6}
\]
The absolute value of the tail is bounded by a constant times \(\sum_{j\geq J}|A|^j\), convergent for \(\sigma>0\). The last unit integral is one if \(\eta=1\) and zero otherwise: translate by a unit where a nontrivial \(\eta\) differs from one. In the first case the tail is \(f(0)A^J/(1-A)\); in the second it vanishes. This proves continuation and the Laurent-polynomial assertion.

If \(\eta=1\), the test \(f=\mathbf1_{\mathcal O}\) has \(Z(f,c)=L(c)\). If \(\eta\ne1\), the function equal to \(\eta^{-1}\) on \(\mathcal O^\times\) and zero elsewhere has integral one. Dilating a test function through integral powers of \(\pi\) multiplies its zeta integral by integral powers of \(A\). These observations prove the module assertion in both cases. ∎

All assertions about rational families below refer to this continuation. In particular an integral with nonpositive \(\sigma\) is not silently interpreted as an absolutely convergent integral at zero. For the dual character,
\[
 \check c(\pi)=q^{-1}A^{-1},\qquad
 \sigma(\check c)=1-\sigma(c),\qquad \check{\check c}=c.
 \tag{7}
\]

## The Fourier exchange inside the convergence strip

**Theorem 7.2 (local functional equation).** For \(0<\sigma(c)<1\) and \(f,g\in\mathcal S(F)\),
\[
 Z(f,c)Z(\widehat g,\check c)
       =Z(\widehat f,\check c)Z(g,c).
 \tag{8}
\]
It extends as an identity of rational families. There is a nonzero meromorphic factor \(\rho(c,\psi,dx)\), independent of the test function, such that
\[
 Z(\widehat f,\check c)=\rho(c,\psi,dx)Z(f,c)
                  \quad(f\in\mathcal S(F)).
 \tag{9}
\]
Ratios of individual integrals give this factor wherever their denominators are nonzero; equation (9) states it without that restriction.

*Proof.* All four integrals in (8) converge absolutely by Proposition 7.1 and (7). Since \(d^\times x=\kappa dx/|x|\), their first product equals
\[
 \kappa^2\int_{F^\times}\int_{F^\times}
 f(x)\widehat g(y)c(x)c(y)^{-1}\frac{dx}{|x|}\,dy.
 \tag{10}
\]
For each \(x\ne0\), change \(y=xz\). The additive factor \(dy=|x|dz\) cancels \(1/|x|\), and the character factors become \(c(z)^{-1}\). Hence (10) is
\[
 \kappa^2\int_{F^\times}c(z)^{-1}
                    \left(\int_F f(x)\widehat g(zx)\,dx\right)dz.
 \tag{11}
\]
This double integral is absolutely convergent: undoing the change of variables in its absolute-value integral gives the product of the absolute-value integrals in (10). The point zero has additive measure zero, since \(\operatorname{vol}(\pi^r\mathcal O)=mq^{-r}\to0\).

For each fixed \(z\), ordinary Fubini on the compact supports of \(f\) and \(g\) gives
\[
 \int_F f(x)\widehat g(zx)\,dx
  =\int_F\int_F f(x)g(t)\psi(zxt)\,dt\,dx
  =\int_F\widehat f(zt)g(t)\,dt.
 \tag{12}
\]
Substitute this identity in (11). The resulting double integral is again absolutely convergent, by the same argument with \(g,\widehat f\). Now change \(y=zt\) for \(t\ne0\). This produces \(Z(g,c)Z(\widehat f,\check c)\), proving (8). The argument uses Fubini for two absolutely integrable double integrals and for (12) at fixed \(z\); it does not interchange an unbounded oscillatory triple integral.

To obtain (9), choose \(g=\eta^{-1}\mathbf1_{\mathcal O^\times}\), whose integral is identically one in the family. Set \(\rho=Z(\widehat g,\check c)\). Then (8) proves (9) in the strip, and rationality extends it to every \(A\in\mathbb C^\times\) meromorphically. Finally apply (9) twice and use (3):
\[
 \rho(c,\psi,dx)\rho(\check c,\psi,dx)
                     =\lambda^2 c(-1).
 \tag{13}
\]
For example the equality follows by taking a test with zeta integral identically one. The right side is nonzero, so \(\rho\) is not the zero meromorphic function. ∎

The multiplicative substitution is the reason for the norm in \(\check c\). Replacing it by \(c^{-1}\) would leave an uncanceled additive scaling factor; Exercise 3 gives a counterexample with all four integrals convergent.

## The unramified factor and the primitive Gauss sum

Define \(\epsilon\) by
\[
 \rho(c,\psi,dx)=\epsilon(c,\psi,dx)
                                  \frac{L(\check c)}{L(c)}.
 \tag{14}
\]
It is this precise quotient convention that fixes every sign and conductor power below.

For \(a=a(c)\geq1\), choose any \(b\in F^\times\) with \(\operatorname{ord}(b)=a+n\). Define
\[
 \tau(\eta^{-1},\psi,b)
    =\sum_{u\in(\mathcal O/\mathfrak p^a)^\times}
                            \eta(u)^{-1}\psi(u/b).
 \tag{15}
\]
Here unit lifts can be chosen arbitrarily: both factors are unchanged upon replacing a lift by another congruent modulo \(\mathfrak p^a\). The induced additive character of \(\mathcal O/\mathfrak p^a\) is primitive because \(n\) is maximal in (1).

**Theorem 7.3.** With the preceding normalization,
\[
 \epsilon(c,\psi,dx)=
 \begin{cases}
 m q^n A^n,&a(c)=0,\\
 m q^n c(b)\tau(\eta^{-1},\psi,b),&a(c)=a\geq1.
 \end{cases}
 \tag{16}
\]
Consequently (14) gives \(\rho\); in the ramified case \(L(c)=L(\check c)=1\), so \(\rho=\epsilon\). The second expression is independent of the allowed choice of \(b\).

For self-dual \(dx\), write \(c=c_0|\cdot|^s\) with \(c_0\) unitary and take \(b=\pi^{a+n}\). These formulas become
\[
 \epsilon(c,\psi,dx_\psi)=
 \begin{cases}
 c_0(\pi)^n q^{n(1/2-s)},&a=0,\\
 W(c_0,\psi)q^{(a+n)(1/2-s)},&a\geq1,
 \end{cases}
 \tag{17}
\]
where
\[
 W(c_0,\psi)=c_0(b)q^{-a/2}
                                     \tau(\eta^{-1},\psi,b).
 \tag{18}
\]
The primitive sum satisfies \(|\tau|=q^{a/2}\), and hence \(|W|=1\).

*Proof of the formulas.* If \(a=0\), take \(f=\mathbf1_{\mathcal O}\). Proposition 7.1 gives \(Z(f,c)=L(c)\), while (2) gives \(\widehat f=m\mathbf1_{\pi^{-n}\mathcal O}\). Summing its shells for \(\check c\) gives
\[
 Z(\widehat f,\check c)
   =m(q^{-1}A^{-1})^{-n}L(\check c)
   =mq^n A^nL(\check c).
 \tag{19}
\]
Equations (14) and (19) prove the first case of (16), including negative \(n\).

Now let \(a\geq1\) and put \(f=\eta^{-1}\mathbf1_{\mathcal O^\times}\). Its zeta integral is one. It is invariant under translation by \(\mathfrak p^a\): on each unit residue class modulo \(\mathfrak p^a\) the character is constant, and translation by that ideal also preserves the nonunit complement. By (2), its transform is supported in \(\pi^{-a-n}\mathcal O\).

We claim that the transform vanishes unless \(\operatorname{ord}(y)=-a-n\). For \(a\geq2\), minimality of the conductor gives a unit \(v\in1+\mathfrak p^{a-1}\) with \(\eta(v)\ne1\). If \(\operatorname{ord}(y)>-a-n\), then \(yu(v-1)\in\pi^{-n}\mathcal O\) for every unit \(u\). Changing \(u\) to \(vu\) in the Fourier integral therefore leaves its additive character unchanged and multiplies its multiplicative factor by \(\eta(v)^{-1}\). The integral must be zero. For \(a=1\), the same range is \(y\in\pi^{-n}\mathcal O\); here \(\psi(uy)=1\) for every unit and ordinary orthogonality of the nontrivial \(\eta\) gives zero. This also covers \(y=0\).

For \(y=w/b\) with \(w\in\mathcal O^\times\), change \(t=uw\) in its Fourier integral. Splitting the units into additive residue classes of mass \(mq^{-a}\) yields
\[
 \widehat f(w/b)=mq^{-a}\eta(w)
                                     \tau(\eta^{-1},\psi,b).
 \tag{20}
\]
On this shell, \(\check c(w/b)=c(b)|b|^{-1}\eta(w)^{-1}\). The shell has multiplicative volume one, so
\[
 Z(\widehat f,\check c)
   =mq^{-a}c(b)|b|^{-1}\tau(\eta^{-1},\psi,b)
   =mq^n c(b)\tau(\eta^{-1},\psi,b).
 \tag{21}
\]
This proves the second case. Replacing \(b\) by \(vb\), with \(v\) a unit, multiplies \(c(b)\) by \(\eta(v)\) and the Gauss sum by \(\eta(v)^{-1}\), proving independence. Substituting \(m=q^{-n/2}\) and \(c(b)=c_0(b)q^{-s(a+n)}\) proves (17)–(18).

For the size of the sum one can use finite Fourier inversion directly. With the same \(f\), apply Fourier transformation again to (20) and evaluate at one. Substitution \(y=w/b\) gives
\[
 \widehat{\widehat f}(1)
   =m^2q^{n-a}\tau(\eta^{-1},\psi,b)
                            \tau(\eta,\psi,b).
 \tag{22}
\]
For self-dual measure, (3) and \(m^2=q^{-n}\) make this the identity
\[
 \tau(\eta^{-1},\psi,b)\tau(\eta,\psi,b)
                                  =\eta(-1)q^a.
 \tag{23}
\]
Conjugating the first sum and replacing \(u\) by \(-u\) gives
\(\overline{\tau(\eta^{-1},\psi,b)}=\eta(-1)\tau(\eta,\psi,b)\). Since \(\eta(-1)^2=1\), (23) implies \(|\tau|^2=q^a\). It proves nonvanishing as well as the asserted size. ∎

A single unit coset gives the same factor. Let \(h=|\mathcal O^\times/U^{(a)}|=(q-1)q^{a-1}\) and take \(f_1=h\mathbf1_{1+\mathfrak p^a}\). Then \(Z(f_1,c)=1\), and
\[
 \widehat f_1(y)=h mq^{-a}\psi(y)
                         \mathbf1_{\pi^{-a-n}\mathcal O}(y).
 \tag{24}
\]
In its dual zeta integral, unit orthogonality kills every shell above \(-a-n\), by the same conductor argument used for (20). On the remaining shell the unit average is \(h^{-1}\tau(\eta^{-1},\psi,b)\). Equation (21) follows again. Thus both a unit-character test and a translated principal-unit test recover the identical Gauss factor.

For the trace character of a number-field completion, \(n=d\), so the unramified formula is specifically
\[
 \rho(c_0|\cdot|^s)=
 c_0(\delta)N(\mathfrak D_F)^{1/2-s}
                             \frac{L(\check c)}{L(c)},
 \tag{25}
\]
where \(\delta\) is any generator of \(\mathfrak D_F\) and \(c_0\) is unramified. The exponent is \(1/2-s\) under definition (9). Reversing the ratio defining \(\rho\) reverses that exponent as well. In the ramified formula the summed unit character is \(\eta^{-1}\), as specified in (15); this matters for nonquadratic characters.

For a direct comparison with Poonen, §4.9, take \(n=0\), additive integral-ring mass \(m=1\), and \(c_0(\pi)=1\). His multiplicative measure \(dx/|x|\) gives each unit residue class modulo \(\mathfrak p^a\) mass \(q^{-a}\). Hence his integral Gauss sum is \(g=q^{-a}\tau(\eta^{-1},\psi,\pi^a)\), and the factor \(q^{a(1-s)}g\) equals \(q^{-as}\tau\), precisely (21) in these choices. Giving the whole unit group mass one rescales both zeta integrals equally and leaves their ratio unchanged. Equations (16)–(18) retain arbitrary additive conductor, uniformizer value and self-dual measure.

## Dependence on the auxiliary choices

**Proposition 7.4.** The factor defined by (14) satisfies, for \(t>0\), \(r\in F^\times\), and \(\psi_r(x)=\psi(rx)\),
\[
 \epsilon(c,\psi,t\,dx)=t\,\epsilon(c,\psi,dx),
 \tag{26}
\]
\[
 \epsilon(c,\psi_r,dx)=c(r)|r|^{-1}
                                      \epsilon(c,\psi,dx).
 \tag{27}
\]
For self-dual \(dx\),
\[
 \epsilon(c,\psi,dx)\epsilon(\check c,\psi,dx)=c(-1),
 \tag{28}
\]
and, for unitary \(c_0\),
\[
 \big|\epsilon(c_0|\cdot|^{1/2},\psi,dx)\big|=1.
 \tag{29}
\]

*Proof.* Scaling the additive measure scales every Fourier transform by \(t\). Keep the multiplicative measure normalized to unit volume on \(\mathcal O^\times\); (9) then scales \(\rho\) by \(t\). The \(L\)-factors are unchanged, proving (26). If a fixed multiple of the multiplicative measure is used instead, it still cancels from the ratio.

For fixed additive measure, Fourier transformation with \(\psi_r\) gives \(\widehat f_{\psi_r}(y)=\widehat f_\psi(ry)\). The multiplicative substitution \(z=ry\) gives
\[
 Z(\widehat f_{\psi_r},\check c)
     =\check c(r)^{-1}Z(\widehat f_\psi,\check c).
\]
Since \(\check c(r)^{-1}=c(r)|r|^{-1}\), this proves (27). Formula (13) with \(\lambda=1\), together with cancellation of the opposite \(L\)-ratios in (14), proves (28).

For (29), put \(c=c_0|\cdot|^{1/2}\), so \(\overline c=\check c\). Complex conjugation of the defining integrals and their rational continuations gives
\[
 \overline{\epsilon(c,\psi,dx)}
                 =\epsilon(\overline c,\overline\psi,dx).
 \tag{30}
\]
The positive Haar measure is real and \(\overline{L(c)}=L(\overline c)\). Because \(\overline\psi=\psi_{-1}\), (27) turns the right side into \(c(-1)\epsilon(\check c,\psi,dx)\). Multiplying by \(\epsilon(c,\psi,dx)\) and using (28) gives absolute-value square \(c(-1)^2=1\). There are no singularities here: the unramified denominator has \(|A|=q^{-1/2}<1\), and the ramified formula is a nonzero monomial times a primitive Gauss sum. ∎

Equations (26) and (27) specify changes independently. If the measure is adjusted to remain self-dual after replacing \(\psi\) by \(\psi_r\), it is multiplied by \(|r|^{1/2}\), so the combined change is \(c(r)|r|^{-1/2}\). Keeping the old measure and calling it self-dual for the new character would give an incorrect normalization.

## Three computations

For \(F=\mathbb Q_p\), the basic character has \(n=0\) and self-dual integral-ring mass one. For \(c=|\cdot|^s\),
\[
 Z(\mathbf1_{\mathbb Z_p},c)=\frac1{1-p^{-s}},\qquad
 \epsilon(c)=1,\qquad
 \rho(c)=\frac{1-p^{-s}}{1-p^{s-1}}.
 \tag{31}
\]

For a nontrivial residue character \(\eta\) at an odd prime, take \(c(p)=1\). It has \(a=1\), and
\[
 \rho(c)=\epsilon(c)
      =\sum_{u\in\mathbb F_p^\times}\eta(u)^{-1}e^{2\pi i u/p}.
 \tag{32}
\]
Its absolute value is \(\sqrt p\). Twisting this same character by \(|\cdot|^{1/2}\) divides the value by \(\sqrt p\), giving the central unit-modulus factor. For the Dirichlet normalization of Proposition 6.4, \(\eta=\chi_p^{-1}\), so the sum in (32) uses \(\chi_p\), as required for the usual Dirichlet Gauss sum.

As a ramified-field example, let \(F=\mathbb Q_3(\sqrt3)\), \(\pi=\sqrt3\), and use its trace character. The direct trace calculation in Solution 2 of the additive-character lesson gives different exponent one and residue cardinality three. Thus
\[
 \epsilon(|\cdot|^s)=3^{1/2-s},\qquad
 \rho(|\cdot|^s)=3^{1/2-s}
                            \frac{1-3^{-s}}{1-3^{s-1}}.
 \tag{33}
\]
Indeed \(\widehat{\mathbf1_{\mathcal O}}=3^{-1/2}\mathbf1_{\pi^{-1}\mathcal O}\). Summing the dual shells starting at \(-1\) gives the factor \(3^{-1/2}\cdot3^{1-s}\), independently checking the exponent in (33).

## Exercises

1. **Easy.** Compute \(Z(\mathbf1_{\mathbb Z_p},|\cdot|^s)\) with multiplicative unit volume one, and with \(d^\times x=dx/|x|\) for \(\operatorname{vol}_{dx}(\mathbb Z_p)=1\). State the convergence region and the effect on \(\rho\).
2. **Medium.** Let \(c:\mathbb Q_p^\times\to\mathbb T\) be trivial on \(1+p\mathbb Z_p\) and satisfy \(c(p)=1\). Compute \(\rho(c)\) with the basic character and self-dual measure, distinguishing a nontrivial residue character from the trivial one.
3. **Medium.** Give a counterexample to (8) if \(\check c\) is replaced by \(c^{-1}\), choosing test functions for which all four resulting integrals converge for some \(0<\sigma(c)<1\).
4. **Hard.** Prove the product identity (28) and the central absolute-value identity (29). Also verify them directly using the unramified formula and the primitive Gauss sums.

## Solutions

**Solution 1.** Each shell \(p^j\mathbb Z_p^\times\), \(j\geq0\), has multiplicative volume one in the first convention. The integral is therefore \(\sum_{j\geq0}p^{-js}=(1-p^{-s})^{-1}\) for \(\operatorname{Re}s>0\). In the second convention the shell volume is \(1-p^{-1}\), because additive scaling cancels the factor \(|x|^{-1}\). Hence the answer is \((1-p^{-1})/(1-p^{-s})\), with the same region of absolute convergence. Both extend as the stated rational functions. Every zeta integral, including the Fourier-transformed one, changes by the same multiplicative constant, so \(\rho\) is unchanged. It remains the expression in (31), with \(\epsilon=1\).

**Solution 2.** Reduction identifies the unit quotient with \(\mathbb F_p^\times\), so write \(\eta\) for its character. If \(\eta\ne1\), the conductor is one and (32) gives the answer. The sum has size \(\sqrt p\) by (23); no inverse may be dropped unless \(\eta\) is quadratic. If \(\eta=1\), the whole character is trivial because \(c(p)=1\) too. Its integral on \(\mathbb Z_p\) is not convergent, but the meromorphic factor from (31), at \(s=0\), has the regular value \(\rho(1)=0\). This is consistent with a test supported away from zero: for \(f=\mathbf1_{\mathbb Z_p^\times}\), \(Z(f,1)=1\) and \(\widehat f=\mathbf1_{\mathbb Z_p}-p^{-1}\mathbf1_{p^{-1}\mathbb Z_p}\); integrating against \(\check c=|\cdot|\) gives zero. At \(p=2\) the residue group is trivial, so only this latter case occurs.

**Solution 3.** Work over \(\mathbb Q_p\) with the basic character. Let \(c=|\cdot|^s\), \(A=p^{-s}\), and
\[
 f=\mathbf1_{\mathbb Z_p}-p\mathbf1_{p\mathbb Z_p},\qquad
 g(x)=f(x/p).
\]
Their additive integrals vanish, and (2) gives
\[
 \widehat f=-\mathbf1_{p^{-1}\mathbb Z_p^\times},\qquad
 \widehat g(y)=p^{-1}\widehat f(py).
\]
Thus both transforms are supported away from zero, so their integrals against the wrong dual \(c^{-1}\) converge for every \(s\). The original two integrals converge for \(\operatorname{Re}s>0\). Direct shell sums and dilation give
\[
 Z(f,c)=\frac{1-pA}{1-A},\quad Z(g,c)=A Z(f,c),\quad
 Z(\widehat f,c^{-1})=-A,\quad
 Z(\widehat g,c^{-1})=-p^{-1}A^2.
\]
For \(s=1/2\), \(Z(f,c)\ne0\). The proposed left product is \(-p^{-1}A^2Z(f,c)\), while the right product is \(-A^2Z(f,c)\). They differ by \(p^{-1}\), although all four integrals are absolutely convergent. Using \(\check c=c^{-1}|\cdot|\) supplies exactly the missing dilation factor.

**Solution 4.** Apply (9) twice with self-dual measure and use \(\widehat{\widehat f}=f(-\cdot)\). Multiplicative substitution by \(-1\) gives \(Z(f(-\cdot),c)=c(-1)Z(f,c)\). A test with integral identically one permits cancellation as a meromorphic identity. Thus \(\rho(c)\rho(\check c)=c(-1)\); the two \(L\)-ratios cancel to give (28). At the central character \(\overline c=\check c\), conjugate the defining integrals. The additive character becomes \(\psi_{-1}\); formula (27) therefore gives \(\overline{\epsilon(c)}=c(-1)\epsilon(\check c)\). Multiplying and using (28) proves (29).

For a direct check, in the unramified case put \(A=c(\pi)\) and \(\check A=q^{-1}A^{-1}\). Formula (16) for self-dual measure gives product \(q^n(A\check A)^n=1\), equal to \(c(-1)\) because an unramified character kills all units. At the central line \(|A|=q^{-1/2}\), its individual absolute value \(q^{n/2}|A|^n\) is one. In the ramified case, use the same \(b\) for both characters. Their factors in (16) have product
\[
 q^n c(b)\check c(b)
        \tau(\eta^{-1},\psi,b)\tau(\eta,\psi,b)
    =q^{-a}\tau(\eta^{-1},\psi,b)\tau(\eta,\psi,b)
    =\eta(-1).
\]
Here \(c(b)\check c(b)=|b|=q^{-a-n}\), and the last equality is (23), proved by Fourier inversion in (22). On the central line, (16) has absolute value \(q^{n/2}q^{-(a+n)/2}q^{a/2}=1\). This verifies both identities for every conductor and every conductor integer of \(\psi\).

## Prerequisites and further directions

- Local additive self-duality, the trace character's inverse-different conductor, self-dual integral-ring mass, and Fourier inversion are imported from Propositions 5.1–5.2. Formula (2) and its application to the test space are explained here.
- Local quasi-character classification, the definition and finiteness of its conductor, and its unitary/norm decomposition are imported from Proposition 6.1. All zeta continuation, functional-equation, Gauss-sum, and epsilon-factor assertions in Propositions 7.1 and 7.4 and Theorems 7.2–7.3 are proved here.
- Higher-dimensional Weil-group constants and the induction formulas of [Deligne 1973, §5] are outside this lesson. The one-dimensional normalizations are compared with (3.3), (3.4), (5.3)–(5.5), and (5.7)–(5.10) of that work.
- The matrix zeta integrals of [Jacquet–Langlands 1970, §13, Theorem 13.1] are the separate \(\mathrm{GL}_2\) analogue; they are not used to prove this local \(\mathrm{GL}_1\) theory.

## References

- Bjorn Poonen, [*Tate’s Thesis*, MIT 18.786, Spring 2015](https://math.mit.edu/~poonen/786/notes.pdf), §§4.7–4.9, Theorem 4.18 and Proposition 4.21, PDF pages 19–25; and James-Michael Leahy, [*An introduction to Tate’s Thesis* (2010)](https://www.math.mcgill.ca/darmon/theses/leahy/thesis.pdf), §§4.5–4.6, PDF pages 133–152: local continuation, Fourier exchange, Gauss integrals and dependence on auxiliary choices. The two-integral argument above supplies the absolute-convergence justification at each interchange, and keeps arbitrary \(F\), additive conductor and uniformizer value.
- P. Deligne, [*Les constantes des équations fonctionnelles des fonctions L*, IAS edition](https://publications.ias.edu/sites/default/files/Number20.pdf), 1973, §§3.3–3.4 and 5.3–5.9, printed pages 526–528 and 548–550: rank-one local constants, conductor, Haar scaling and the finite Gauss formula. Our quotient direction and the inverse unit character are fixed in (14)–(16).
- A. Connes and M. Marcolli, [*Noncommutative Geometry, Quantum Fields and Motives*, author version](https://alainconnes.org/wp-content/uploads/bookwebfinal-2.pdf), Chapter 2, §8.4.1, (2.312)–(2.314), PDF page 368: the conductor-zero indicator transform. The subsequent principal-value formulas belong to explicit-formula theory.
- H. Jacquet and R. P. Langlands, [*Automorphic Forms on GL(2)*, IAS retyped edition](https://publications.ias.edu/sites/default/files/automorphic-forms-on-gl2_rpl.pdf), 1970, §1, Lemma 1.2, printed pages 2–3: the quadratic conductor and Gauss normalization. The matrix zeta integrals in §13, Theorem 13.1, are the separate \(\mathrm{GL}_2\) analogue mentioned above.
