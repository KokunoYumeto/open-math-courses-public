# Tate's local theory at the infinite places

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

At an infinite place, a Gaussian replaces the characteristic function of the integral ring. A polynomial attached to the angular character then selects the correct Gamma factor. Fourier transformation turns that polynomial into its opposite angular type, with a phase that records the degree. We will compute this phase as well as prove the functional equation for every Schwartz function.

We retain the quotient convention of [Tate's local theory at the finite places](NT-ADL-07.md): the Fourier-transformed integral is the factor times the original integral. The local characters are those classified in [Quasi-characters and Hecke characters](NT-ADL-06.md). For a real place write
\[
 c_{\epsilon,s}(x)=\operatorname{sgn}(x)^\epsilon |x|^s,
 \qquad \epsilon\in\{0,1\},\quad s\in\mathbb C;
 \tag{1}
\]
for a complex place write
\[
 c_{n,s}(z)=(z/|z|)^n |z|_{\mathbb C}^s,
 \qquad n\in\mathbb Z,\quad |z|_{\mathbb C}=z\bar z.
 \tag{2}
\]
Here the unadorned \(|z|\) in the angular part is the ordinary radius. In both cases \(\sigma(c)=\operatorname{Re}s\), and \(\check c=c^{-1}|\cdot|_F\). Thus the dual parameters are \((\epsilon,1-s)\) over \(\mathbb R\) and \((-n,1-s)\) over \(\mathbb C\).

## A common normalization

For \(F=\mathbb R\) or \(\mathbb C\), define
\[
 \widehat f(y)=\int_F f(x)\psi_F(xy)\,dx,
 \qquad Z(f,c)=\int_{F^\times}f(x)c(x)\,d^\times x.
 \tag{3}
\]
The choices are fixed in the following table. Write \(z=u+iv\) at a complex place.

| Object | Real place | Complex place |
|---|---|---|
| Normalized norm | \(\lvert x\rvert\) | \(\lvert z\rvert_{\mathbb C}=z\bar z\) |
| Additive character | \(e^{-2\pi i x}\) | \(e^{-2\pi i(z+\bar z)}\) |
| Self-dual additive measure \(dx\) | \(dx\), ordinary Lebesgue measure | \(2\,du\,dv\) |
| Multiplicative measure | \(dx/\lvert x\rvert\) | \(dx/(\pi\lvert z\rvert_{\mathbb C})\) |
| Gamma factor | \(\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2)\) | \(\Gamma_{\mathbb C}(s)=2(2\pi)^{-s}\Gamma(s)\) |

The complex additive pairing is bilinear multiplication, not the Hermitian pairing: if \(y=a+ib\), its kernel is \(e^{-4\pi i(ua-vb)}\). The measure \(2\,du\,dv\) and the reversal in the second coordinate give the inversion formula \(\widehat{\widehat f}(x)=f(-x)\). These additive Fourier conventions and inversion are established in Propositions 5.1–5.2 of [Additive characters, self-dual measures and Poisson summation on the adèles](NT-ADL-05.md).

In polar coordinates, the chosen complex multiplicative measure is
\[
 d^\times z=4\,\frac{dr}{r}\frac{d\theta}{2\pi}
       =2\,\frac{dt}{t}\frac{d\theta}{2\pi},\qquad t=r^2.
 \tag{4}
\]
Thus the angular group has mass two when the norm coordinate has measure \(dt/t\). The alternative \(dx/(2\pi|z|_{\mathbb C})\) has half this mass, and gives half our Gaussian zeta integral. It gives the same \(\rho\) and epsilon factor, because a multiplicative measure constant cancels in their defining ratio. This explicit choice accounts for the factor two in \(\Gamma_{\mathbb C}\).

The space \(\mathcal S(F)\) consists of smooth functions on the underlying real vector space for which every derivative, multiplied by every polynomial, is bounded. Differentiating a Fourier integral inserts polynomial factors; integrating by parts transfers powers of the Fourier variable to derivatives. All these integrals are absolutely convergent for a Schwartz function. Consequently \(\widehat f\in\mathcal S(F)\). For example the bound for \(y^\alpha\partial_y^\beta\widehat f\) follows from the \(L^1\)-norm of the corresponding derivative of \(x^\beta f\), with fixed powers of \(2\pi\) or \(4\pi\). This also justifies the differential identities used below.

## Mellin continuation without a functional equation

First define \(\Gamma(w)=\int_0^\infty e^{-t}t^{w-1}\,dt\) for \(\operatorname{Re}w>0\). Integration by parts gives \(\Gamma(w+1)=w\Gamma(w)\), so this continues meromorphically, with simple poles at \(0,-1,-2,\ldots\). We will also use its absence of zeros; the following elementary argument fixes precisely that fact.

Repeated integration by parts gives
\[
 \int_0^1 t^{w-1}(1-t)^Ndt
      =\frac{N!}{w(w+1)\cdots(w+N)}.
 \tag{5}
\]
After \(u=Nt\), the left side multiplied by \(N^w\) tends to \(\Gamma(w)\). Indeed \((1-u/N)^N\leq e^{-u}\) on \([0,N]\), and dominated convergence applies to \(u^{w-1}\), uniformly on compact subsets of \(\operatorname{Re}w>0\). The limit of the reciprocals of (5) is therefore
\[
 \frac1{\Gamma(w)}
   =w e^{\gamma w}\prod_{k=1}^\infty(1+w/k)e^{-w/k},
 \qquad \gamma=\lim_{N\to\infty}
                 \left(\sum_{k=1}^N\frac1k-\log N\right).
 \tag{6}
\]
The harmonic-sum limit exists by comparison with the integral of \(1/t\). On a fixed compact set, all sufficiently large factors have logarithm \(O(k^{-2})\), uniformly there. Thus the product defines an entire function and is nonzero away from the displayed linear-factor zeros. At \(0,-1,-2,\ldots\) exactly one such factor vanishes simply. Equality initially holds in the right half-plane and then agrees with the reciprocal of the recurrence continuation. In particular \(\Gamma\) has no zeros and has exactly the asserted simple poles.

**Mellin lemma.** For every \(f\in\mathcal S(F)\), \(Z(f,c)\) is absolutely convergent for \(\operatorname{Re}s>0\), locally uniformly there. It has meromorphic continuation to all \(s\). Its possible poles are simple, at
\[
 s=-\epsilon-2j\quad(F=\mathbb R),\qquad
 s=-|n|/2-j\quad(F=\mathbb C),\qquad j\geq0.
 \tag{7}
\]
Moreover \(Z(f,c_{\epsilon,s})/\Gamma_{\mathbb R}(s+\epsilon)\) and \(Z(f,c_{n,s})/\Gamma_{\mathbb C}(s+|n|/2)\) are entire.

*Proof.* Over \(\mathbb R\), split the integral into its two signs:
\[
 Z(f,c_{\epsilon,s})=\int_0^\infty
       [f(r)+(-1)^\epsilon f(-r)]r^{s-1}\,dr.
 \tag{8}
\]
Boundedness near zero and rapid decay at infinity prove convergence. For a compact set of parameters, the same bounds work with the smallest real part at zero and the largest at infinity. They also absorb every power of \(\log r\), proving holomorphy under differentiation in \(s\).

The integral on \([1,\infty)\) is entire by rapid decay. On \((0,1)\), Taylor expansion to arbitrary order \(M\) gives
\[
 f(r)+(-1)^\epsilon f(-r)
   =2\!\sum_{\substack{0\leq k\leq M\\ k\equiv\epsilon\ (2)}}
        \frac{f^{(k)}(0)}{k!}r^k+O(r^{M+1}).
 \tag{9}
\]
Each displayed term integrates to a constant divided by \(s+k\). The remainder is holomorphic for \(\operatorname{Re}s>-M-1\). Increasing \(M\) gives the continuation and its poles in (7). All are among the simple poles of \(\Gamma_{\mathbb R}(s+\epsilon)\).

Over \(\mathbb C\), put
\[
 P_n f(r)=\int_0^{2\pi}f(re^{i\theta})e^{in\theta}
                                  \frac{d\theta}{2\pi}.
 \tag{10}
\]
For \(\operatorname{Re}s>0\), polar coordinates and absolute Fubini give \(Z(f,c_{n,s})=4\int_0^\infty P_n f(r)r^{2s-1}\,dr\). The real Taylor polynomial of \(f(u+iv)\) can equally be written as a sum of monomials \(z^a\bar z^b\). Angular integration retains exactly those with \(a-b=-n\). Their total degrees are \(|n|+2j\). The Taylor remainder is uniformly \(O(r^{M+1})\) on the circle. Hence
\[
 P_n f(r)=\sum_{|n|+2j\leq M}b_jr^{|n|+2j}
                                      +O(r^{M+1}).
 \tag{11}
\]
Integration on \((0,1)\) produces denominators \(2s+|n|+2j\); the remainder converges for \(2\operatorname{Re}s+M+1>0\). Infinity again gives an entire integral. This proves the complex assertion. Finally (6) shows that division by either Gamma factor cancels the possible simple poles and introduces no new ones. The resulting functions are entire. ∎

### Absolute convergence and angular cancellation

The angular projection controls the poles and can improve convergence of the projected radial expression. It does not by itself improve absolute convergence of the original integral (3), because the angular character has modulus one. The identities obtained by first integrating over angles or signs hold initially in the common half-plane \(\operatorname{Re}s>0\). Beyond it, a convergent projected expression represents the continuation and need not be an absolutely convergent original integral.

For example, take \(f(z)=e^{-2\pi|z|^2}\) and \(n=1\). Then \(P_1f(r)=0\) for every \(r\), so its projected radial integral is zero for every \(s\). At \(s=0\), however, the original absolute integral is

\[
\int_{\mathbb C^\times}|f(z)c_{1,0}(z)|\,d^\times z
=4\int_0^\infty e^{-2\pi r^2}\frac{dr}{r}=\infty.
\]

On \((0,1)\) the Gaussian is at least \(e^{-2\pi}\), giving logarithmic divergence. More generally, this original integral converges exactly for \(\operatorname{Re}s>0\), independently of \(n\). Over \(\mathbb R\), the even Gaussian and \(\epsilon=1\) give the same distinction: \(f(r)-f(-r)=0\), but its absolute integral is \(2\int_0^\infty e^{-\pi r^2}r^{\operatorname{Re}s-1}\,dr\).

The original absolute domain extends left when the test itself vanishes at zero. Suppose its first nonzero Taylor degree is \(k\). Over \(\mathbb R\), with leading coefficient \(a_k\ne0\), Taylor's theorem and \(\bigl||a+b|-|a|\bigr|\leq|b|\) give

\[
|f(r)|+|f(-r)|=2|a_k|r^k+O(r^{k+1}).
\]

Thus the original integral converges at zero exactly when \(\operatorname{Re}s>-k\). Over \(\mathbb C\), write the leading real homogeneous Taylor polynomial as \(P_k\). The Taylor remainder is uniform on the unit circle, so

\[
\int_0^{2\pi}|f(re^{i\theta})|\frac{d\theta}{2\pi}
=r^k\bigl(A+O(r)\bigr),\qquad
A=\int_0^{2\pi}|P_k(e^{i\theta})|\frac{d\theta}{2\pi}>0.
\]

The positivity follows because a nonzero homogeneous polynomial is nonzero somewhere on the unit circle and hence on an open arc. With the measure \(4\,dr/r\,d\theta/(2\pi)\) of (4), integrability is therefore exactly \(2\operatorname{Re}s+k>0\). At either boundary the leading term produces logarithmic divergence. Rapid Schwartz decay handles infinity for every fixed parameter and uniformly on compact parameter sets.

If \(f\) is flat at zero, Taylor's remainder is \(O(r^M)\) for every \(M\). The original integral is then absolutely convergent for every \(s\); these bounds also absorb logarithmic powers, so differentiation under the integral proves it entire. The common half-plane in the Mellin lemma is sufficient for every Schwartz test. The larger domains for the polynomial Gaussian tests below come from their actual polynomial vanishing, not merely angular cancellation.

## Tests that detect the angular type

Define the real tests
\[
 g_0(x)=e^{-\pi x^2},\qquad g_1(x)=xe^{-\pi x^2},
 \tag{12}
\]
and, for \(N=|n|\), the complex tests
\[
 h_n(z)=
 \begin{cases}
 \bar z^n e^{-2\pi z\bar z},&n\geq0,\\
 z^{-n}e^{-2\pi z\bar z},&n<0.
 \end{cases}
 \tag{13}
\]
The exponents here are nonnegative integers. In particular the second case is a polynomial, not a singular function.

**Proposition 8.2.** For the measures in the table,
\[
 Z(g_\epsilon,c_{\epsilon,s})=\Gamma_{\mathbb R}(s+\epsilon),
 \qquad \widehat g_\epsilon=(-i)^\epsilon g_\epsilon,
 \tag{14}
\]
and
\[
 Z(h_n,c_{n,s})=\Gamma_{\mathbb C}(s+N/2),
 \qquad \widehat h_n=(-i)^N h_{-n}.
 \tag{15}
\]
The integral formulas converge respectively for \(\operatorname{Re}s>-\epsilon\) and \(\operatorname{Re}s>-N/2\), and then hold meromorphically everywhere.

*Proof.* The character's sign cancels the polynomial's sign in (12). The real integral is therefore
\[
 2\int_0^\infty e^{-\pi r^2}r^{s+\epsilon-1}\,dr
       =\pi^{-(s+\epsilon)/2}\Gamma((s+\epsilon)/2),
 \tag{16}
\]
by \(t=\pi r^2\). At a complex place the angular factors in \(h_n c_{n,s}\) cancel. Equation (4) gives
\[
 4\int_0^\infty e^{-2\pi r^2}r^{2s+N-1}\,dr
     =2(2\pi)^{-(s+N/2)}\Gamma(s+N/2).
 \tag{17}
\]
These substitutions also give the exact convergence conditions.

The Gaussian Fourier transforms are already computed with these measures in Proposition 5.2. For the real polynomial, differentiation under the integral gives
\[
 \widehat{xf}(y)=-\frac1{2\pi i}\frac{d}{dy}\widehat f(y).
 \tag{18}
\]
Applying this to \(g_0\) gives \(\widehat g_1=-iyg_0(y)=-ig_1(y)\).

For the complex calculation let \(w=a+ib\) and \(G(w)=e^{-2\pi w\bar w}\). Direct differentiation of the bilinear kernel gives
\[
 \widehat{\bar z f}
    =-\frac1{4\pi i}(\partial_a+i\partial_b)\widehat f,
 \qquad
 \widehat{zf}
    =-\frac1{4\pi i}(\partial_a-i\partial_b)\widehat f.
 \tag{19}
\]
Put \(D_+=\partial_a+i\partial_b\). Then \(D_+w=0\) and \(D_+G=-4\pi wG\). Induction consequently gives \(D_+^N G=(-4\pi)^N w^N G\), with no additional lower-degree terms. Since \(\widehat G=G\), (19) gives \(\widehat{\bar z^N G}=(-i)^Nw^NG\). Similarly \(D_-\bar w=0\) and \(D_-G=-4\pi\bar wG\), so \(\widehat{z^NG}=(-i)^N\bar w^NG\). These are exactly (15), for both signs of \(n\). ∎

The normalization of a test function and that of the multiplicative measure should be compared together. With the complex measure \(dx/|z|_{\mathbb C}\) used by Poonen and Leahy, the same unscaled polynomial Gaussian \(h_n\) has zeta integral \(\pi\Gamma_{\mathbb C}(s+|n|/2)\), since that measure is \(\pi\) times (3). Poonen’s \(\pi^{-1}h_n\) therefore gives our \(\Gamma_{\mathbb C}\); Leahy’s \((2\pi)^{-1}h_n\), equation (4.10), gives half of it. These scalar changes multiply both sides of a local zeta-integral identity equally. The phases for our negative basic character are fixed by the differentiated Fourier transforms (14)–(15).

## The functional equation for all tests

**Theorem 8.1.** For \(0<\operatorname{Re}s<1\) and \(f,g\in\mathcal S(F)\),
\[
 Z(f,c)Z(\widehat g,\check c)
                     =Z(g,c)Z(\widehat f,\check c).
 \tag{20}
\]
There is a nonzero meromorphic function \(\rho(c,\psi_F,dx)\), independent of \(f\), such that
\[
 Z(\widehat f,\check c)=\rho(c,\psi_F,dx)Z(f,c)
 \tag{21}
\]
as meromorphic functions of \(s\), for every Schwartz function \(f\).

*Proof.* Write \(d^\times x=\kappa dx/|x|_F\), where \(\kappa=1\) over \(\mathbb R\) and \(\kappa=1/\pi\) over \(\mathbb C\). The Mellin lemma and preservation of the Schwartz space show that all four factors in (20) converge absolutely in the strip. Thus their first product is
\[
 \kappa^2\int_{F^\times}\int_{F^\times}
 f(x)\widehat g(y)c(x)c(y)^{-1}\frac{dx}{|x|_F}\,dy.
 \tag{22}
\]
Change \(y=xz\). Additive measure scales by \(|x|_F\), so this equals
\[
 \kappa^2\int_{F^\times}c(z)^{-1}
                   \left(\int_F f(x)\widehat g(zx)dx\right)dz.
 \tag{23}
\]
The absolute-value double integral is finite by undoing that substitution in (22). For each fixed \(z\), the integral of \(|f(x)g(t)|\) is finite, since both functions are integrable on the additive space. Therefore Fubini at this fixed parameter gives
\[
 \int_F f(x)\widehat g(zx)dx
              =\int_F\widehat f(zt)g(t)dt.
 \tag{24}
\]
Insert (24) in (23). The absolute-value double integral of the new expression is finite as well: reversing the change \(y=zt\) gives the product of the two convergent absolute zeta integrals for \(g\) and \(\widehat f\). That same substitution now evaluates it as the right side of (20). A singleton has additive measure zero over either field, so the inserted or removed points at zero do not affect these steps.

Take \(g=g_\epsilon\) or \(h_n\). Its zeta integral is the nonzero Gamma function from Proposition 8.2; it has neither poles nor zeros in the strip. Dividing (20) by this integral proves (21) there. The Mellin lemma continues all its integrals, and the explicit Gamma ratio from (14) or (15) continues \(\rho\). The identity theorem proves (21) throughout the plane meromorphically. Fourier inversion applied twice also gives \(\rho(c)\rho(\check c)=c(-1)\), so the factor is not identically zero. ∎

The two-variable proof has the same algebra as Theorem 7.2, but its convergence here comes from Schwartz bounds. The proof justifies the fixed-parameter Fourier interchange separately from the two absolutely convergent double integrals; it requires no absolutely convergent oscillatory triple integral.

## Gamma factors and epsilon phases

**Proposition 8.3.** Define \(L_\infty\) and epsilon using the same quotient direction as at finite places:
\[
 \rho(c)=\epsilon(c)\frac{L_\infty(\check c)}{L_\infty(c)}.
 \tag{25}
\]
For our additive characters and self-dual measures their values are
\[
 \begin{array}{c|c|c|c}
 F&c&L_\infty(c)&\epsilon(c)\\\hline
 \mathbb R&\operatorname{sgn}^{\epsilon}|\cdot|^s
       &\Gamma_{\mathbb R}(s+\epsilon)&(-i)^\epsilon\\
 \mathbb C&(z/|z|)^n|z|_{\mathbb C}^s
       &\Gamma_{\mathbb C}(s+|n|/2)&(-i)^{|n|}.
 \end{array}
 \tag{26}
\]
In particular
\[
 \rho(c_{\epsilon,s})=(-i)^\epsilon
   \frac{\Gamma_{\mathbb R}(1-s+\epsilon)}
        {\Gamma_{\mathbb R}(s+\epsilon)},\qquad
 \rho(c_{n,s})=(-i)^{|n|}
   \frac{\Gamma_{\mathbb C}(1-s+|n|/2)}
        {\Gamma_{\mathbb C}(s+|n|/2)}.
 \tag{27}
\]
These are meromorphic identities; at poles one uses continuation rather than ratios of divergent integrals.

*Proof.* Evaluate (21) on the tests of Proposition 8.2. The real Fourier transform has the scalar \((-i)^\epsilon\). The complex transform has scalar \((-i)^{|n|}\) and the opposite angular polynomial, which is precisely the test for \(\check c=c_{-n,1-s}\). Equations (14)–(15) consequently give (27), hence (26). The Mellin lemma shows that these \(L\)-factors remove every possible pole of a test integral; the selected tests have normalized integral one. Thus the factors account for the full family of local integrals, rather than for the selected Gaussians alone. ∎

For example, the characters with \(n=1\) and \(n=-1\) both have epsilon \(-i\); those with \(n=2\) and \(n=-2\) both have epsilon \(-1\). Replacing \(|n|\) by \(n\) in the phase would fail for negative odd \(n\). The dual-product check is
\[
 \epsilon(c)\epsilon(\check c)=
 \begin{cases}
 (-1)^\epsilon,&F=\mathbb R,\\
 (-1)^{|n|},&F=\mathbb C,
 \end{cases}
 =c(-1),
 \tag{28}
\]
in agreement with Fourier inversion. Each epsilon has absolute value one for these basic characters, for every \(s\); in particular it has absolute value one for a unitary character times \(|\cdot|_F^{1/2}\).

The dependence on the additive data has a useful uniform form. If \(dx\) is multiplied by \(a>0\), Fourier transformation and epsilon are multiplied by \(a\). If \(\psi_F\) is replaced by \(\psi_F(rx)\) while \(dx\) is held fixed, the change of variable \(y\mapsto ry\) in the dual zeta integral gives
\[
 \epsilon(c,\psi_{F,r},dx)
      =c(r)|r|_F^{-1}\epsilon(c,\psi_F,dx).
 \tag{29}
\]
The measure that remains self-dual for this new character is \(|r|_F^{1/2}dx\), so the combined factor is \(c(r)|r|_F^{-1/2}\). These statements follow from (3) and (21), exactly as in Proposition 7.4.

In particular replacing the negative character in our table by the positive one is \(r=-1\), with no change of self-dual measure. It multiplies epsilon by \((-1)^\epsilon\) or \((-1)^n\), producing \(i^\epsilon\) and \(i^{|n|}\). This is the convention in [Deligne 1973, (3.4.1)–(3.4.2)]; its displayed characters are inverse powers of the real or complex embedding, whose angular parameters give the same parity or absolute degree. The difference in phase is fully accounted for by the additive character.

## Duplication and the two complex embeddings

**Proposition 8.4.** As meromorphic functions,
\[
 \Gamma_{\mathbb C}(s)
             =\Gamma_{\mathbb R}(s)\Gamma_{\mathbb R}(s+1).
 \tag{30}
\]

*Proof.* For \(\operatorname{Re}u,\operatorname{Re}v>0\), change variables \((x,y)=(rt,r(1-t))\) in the absolutely convergent product of two Euler Gamma integrals. The Jacobian is \(r\), which proves
\[
 B(u,v):=\int_0^1t^{u-1}(1-t)^{v-1}dt
                  =\frac{\Gamma(u)\Gamma(v)}{\Gamma(u+v)}.
 \tag{31}
\]
For \(\operatorname{Re}z>0\), the substitution \(t=(1+a)/2\), followed by symmetry and \(b=a^2\), gives
\[
 B(z,z)=2^{1-2z}\int_{-1}^1(1-a^2)^{z-1}da
                         =2^{1-2z}B(1/2,z).
 \tag{32}
\]
Use (31), cancel the nonzero \(\Gamma(z)\), and rearrange:
\[
 \Gamma(z)\Gamma(z+1/2)
                      =2^{1-2z}\Gamma(1/2)\Gamma(2z).
 \tag{33}
\]
The real Gaussian integral in Proposition 5.2, together with \(t=\pi r^2\), gives \(\Gamma(1/2)=\sqrt\pi\). Put \(z=s/2\) in (33) and multiply by \(\pi^{-s-1/2}\). Its right side becomes \(2^{1-s}\pi^{-s}\Gamma(s)=2(2\pi)^{-s}\Gamma(s)\), while its left side becomes \(\Gamma_{\mathbb R}(s)\Gamma_{\mathbb R}(s+1)\). This proves (30) in a half-plane; meromorphic continuation proves it everywhere. ∎

The shift by one is essential. The complex Gamma factor is a product of an even real factor and an odd real factor, both with the same variable \(s\). It is not the square of the even factor. The identity also explains why the two real types together naturally supply the conventional factor two at a complex place.

## Examples and exercises

For the trivial character of \(\mathbb R^\times\), the Gaussian gives \(L_\infty(s)=\pi^{-s/2}\Gamma(s/2)\) and epsilon one. This is the factor in the completed Riemann zeta function. At each finite rational place the standard integral-ring test gives \((1-p^{-s})^{-1}\), by Proposition 7.1. Thus the product test supplies \(\Gamma_{\mathbb R}(s)\prod_p(1-p^{-s})^{-1}\) in \(\operatorname{Re}s>1\). Its global continuation and functional equation require the global argument of the next lesson; they do not follow from a single local factor.

For a Gaussian-integer Hecke character whose actual complex component is \((z/|z|)^4\), Proposition 8.3 gives \(\Gamma_{\mathbb C}(s+2)\) and epsilon \((-i)^4=1\). The ideal-type inverse discussed in Theorem 6.3 may instead give angular exponent \(-4\). Its Gamma factor and epsilon are identical, since both depend on the absolute degree, although its actual character and dual are different.

1. **Easy.** Evaluate \(\int_{\mathbb R^\times}e^{-\pi x^2}|x|^s\,dx/|x|\), giving its domain of absolute convergence and all its poles after continuation.
2. **Medium.** Compute the Fourier transform of \(xe^{-\pi x^2}\) with the negative real additive character. Also state the transform for the positive character and verify the Fourier-square identity on this odd test.
3. **Medium.** Prove \(\Gamma_{\mathbb C}(s)=\Gamma_{\mathbb R}(s)\Gamma_{\mathbb R}(s+1)\) from the Euler integrals, including every constant.
4. **Hard.** Compute the complex epsilon factor for every integer angular exponent \(n\), including negative \(n\). Verify its dual-product identity. Determine its change for \(\psi_{\mathbb C}(rz)\), first with the old additive measure and then with the new self-dual measure; explain the effect of halving \(d^\times z\).

## Solutions

**Solution 1.** Splitting the signs gives \(2\int_0^\infty e^{-\pi r^2}r^{s-1}dr\). With \(t=\pi r^2\), one has \(dr/r=dt/(2t)\), so the result is \(\pi^{-s/2}\Gamma(s/2)\). At zero absolute integrability is exactly \(\operatorname{Re}s>0\); the Gaussian handles infinity for every parameter. The recurrence and product (6) show simple poles precisely at \(s=0,-2,-4,\ldots\). At \(s=-2j\) their residues are \(2(-1)^j\pi^j/j!\): the residue of \(\Gamma(w)\) at \(-j\) is \((-1)^j/j!\), and the change \(w=s/2\) contributes the factor two. There are no other poles.

**Solution 2.** The transform of the even Gaussian is itself. Differentiating its Fourier integral gives \(\widehat{xf}=-(2\pi i)^{-1}(\widehat f)'\). Hence \(\widehat{xe^{-\pi x^2}}=-iy e^{-\pi y^2}\). Changing to the positive character replaces the Fourier variable by \(-y\), giving \(+iy e^{-\pi y^2}\). Under the negative convention the transform applied twice multiplies this test by \((-i)^2=-1\), equal to its value at \(-x\). Under the positive convention the multiplier is \(i^2=-1\) as well. The real odd epsilon is correspondingly \(-i\) or \(+i\), not one.

**Solution 3.** The product \(\Gamma(u)\Gamma(v)\) is absolutely integrable for positive real parts. The change \((x,y)=(rt,r(1-t))\), with Jacobian \(r\), gives (31). For \(u=v=z\), substitute \(t=(1+a)/2\) in the beta integral: the prefactor is \(2^{1-2z}\). Integrating the even function on \([-1,1]\) and then putting \(b=a^2\) yields \(B(z,z)=2^{1-2z}B(1/2,z)\). Applying (31) and canceling \(\Gamma(z)\) gives \(\Gamma(z)\Gamma(z+1/2)=2^{1-2z}\sqrt\pi\Gamma(2z)\). Now \(z=s/2\) and the factors \(\pi^{-s/2}\pi^{-(s+1)/2}\) give \(2^{1-s}\pi^{-s}\Gamma(s)=\Gamma_{\mathbb C}(s)\). All cancellations take place in a right half-plane, where (6) guarantees nonvanishing; meromorphic continuation establishes the identity for every parameter.

**Solution 4.** If \(n\geq0\), choose \(h_n=\bar z^nG\). Formula (19), with \(D_+w=0\), gives \(\widehat h_n=(-i)^n w^nG\). The original integral is \(\Gamma_{\mathbb C}(s+n/2)\), and the transformed test integrated against \(c_{-n,1-s}\) gives \((-i)^n\Gamma_{\mathbb C}(1-s+n/2)\). Their ratio proves epsilon \((-i)^n\). If \(n<0\), set \(N=-n\) and choose \(h_n=z^NG\). The operator \(D_-\) gives \(\widehat h_n=(-i)^N\bar w^NG\), and the same division proves epsilon \((-i)^N\). Thus the answer is \((-i)^{|n|}\) in all cases.

The dual has exponent \(-n\), so the epsilon product is \((-i)^{2|n|}=(-1)^n=c_{n,s}(-1)\), as required. Write \(r=Re^{i\alpha}\), with \(R>0\). Holding the old measure \(2\,du\,dv\) fixed, (29) multiplies epsilon by \(e^{in\alpha}R^{2s-2}\). Renormalizing the additive measure to be self-dual multiplies it by an additional \(|r|_{\mathbb C}^{1/2}=R\). The combined factor is therefore \(e^{in\alpha}R^{2s-1}\). If \(s=1/2+it\), this has absolute value one, providing the central normalization check. Halving the multiplicative measure halves both sides of (21) and changes neither rho nor epsilon. With that alternative measure the Gaussian integral is \(\Gamma_{\mathbb C}(s+|n|/2)/2\); doubling the test would restore normalized integral one.

## Prerequisites and further directions

- The classification of real and complex quasi-characters is imported exactly from Proposition 6.1. The additive pairing, its self-dual measures, Fourier inversion, and the Gaussian Fourier transforms are imported from Propositions 5.1–5.2. Preservation of the Schwartz space and the polynomial transforms used here are justified above.
- Basic integration on real Euclidean spaces, Taylor's theorem with remainder, dominated convergence, and the identity theorem for meromorphic functions are used as analysis prerequisites. The needed Gamma continuation, nonvanishing, beta identity, and duplication are proved here.
- The global Poisson argument, the completed Hecke functional equation, and class-number residues are the subjects of the next two lessons. Archimedean Weil-group induction and higher-dimensional constants, discussed in [Deligne 1973, §§3 and 5], are not used to prove the one-dimensional assertions here.

## References

- Bjorn Poonen, [*Tate’s Thesis*, MIT 18.786, Spring 2015](https://math.mit.edu/~poonen/786/notes.pdf), §§4.7–4.9, PDF pages 19–25: local integrability and the real and complex Gaussian tests. The Mellin continuation, original absolute-convergence thresholds and Fourier-interchange proof are given above for every Schwartz test.
- James-Michael Leahy, [*An introduction to Tate’s Thesis* (2010)](https://www.math.mcgill.ca/darmon/theses/leahy/thesis.pdf), §§4.5–4.6, especially (4.6)–(4.11) and Proposition 4.6.1, printed pages 130–134 and 143–145. Its complex \(L\)-factor in (4.10) is half our \(\Gamma_{\mathbb C}\); the measure and test conversion is explained above. The negative-character Fourier phases used here follow from (14)–(15).
- J. Shurman, [*Number field zeta integrals and L-functions*](https://people.reed.edu/~jerry/361/lectures/ait.pdf), Reed College number theory notes, §§2.2–2.3: Gaussian local integrals at the real and complex places, their Gamma normalizations and the duplication identity relating the complex factor to the two real factors; and [*Gamma function symmetry and duplication*](https://people.reed.edu/~jerry/311/gammaiddup.pdf): Legendre's duplication formula through the beta integral.
- P. Deligne, [*Les constantes des équations fonctionnelles des fonctions L*, IAS edition](https://publications.ias.edu/sites/default/files/Number20.pdf), 1973, §§3.2–3.4, printed pages 526–528: archimedean factors and the positive basic-character phases. Changing the sign of the basic character gives the conversion derived above. Higher-dimensional constants are further directions.
