# Values of Dirichlet L-functions at s = 1

*Written and self-checked by GPT-6.1 Sol (OpenAI) in Codex at Ultra, October 2026. Original material is public domain (CC0).*

The infinite series defining \(L(1,\chi)\) can be replaced by a finite sum. For even characters that sum involves real logarithms; for odd characters the arguments of complex logarithms produce a linear sum of character values. Keeping the logarithm's branch is essential. We then compare the real-character values with quadratic class numbers and give a separate analytic lower bound that uses no class-number formula.

We use the primitive Gauss identities from *Gauss sums*, nonvanishing and convergence at 1 from *Dirichlet's theorem on primes in arithmetic progressions*, and the functional equation and generalized Bernoulli values from the preceding lesson. The Pólya–Vinogradov interval bound is used only for the analytic lower bound in Section 4.

## 1. A finite formula with its logarithm fixed

Let \(\chi\) be primitive of conductor \(q>1\). Finite Fourier inversion says

\[
\chi(n)=\frac{\tau(\chi)}q
\sum_{b=1}^{q-1}\overline{\chi(b)}e(-bn/q).
\]

For \(0<r<1\), absolutely convergent summation gives

\[
\sum_{n\ge1}\frac{\chi(n)r^n}n
=-\frac{\tau(\chi)}q\sum_{b=1}^{q-1}
\overline{\chi(b)}\log(1-r e(-b/q)).
\tag{1.1}
\]

Here the logarithm is the branch with real part \(\log|z|\) and argument in \((-\pi,\pi)\). Each \(1-r e(-b/q)\) has positive real part, so this branch is continuous throughout the limiting path. The power series \(-\log(1-z)=\sum_{n\ge1}z^n/n\) on \(|z|<1\) follows by integrating the geometric series from zero to \(z\).

The series \(\sum_n\chi(n)/n\) converges by periodic cancellation and partial summation. Its Abel limit as \(r\uparrow1\) equals its sum. For completeness, if \(a_n=\chi(n)/n\) and \(A_m=\sum_{n\le m}a_n\to A\), then
\(\sum_n a_n r^n=(1-r)\sum_{m\ge1}A_m r^m\).
The contribution of any fixed finite set of \(m\) tends to zero after multiplication by \(1-r\), and the tail differs from \(A(1-r)\sum r^m\) by arbitrarily little once \(A_m\) is close to \(A\). This proves the assertion.

**Theorem 1.1 (general finite formula).** With this logarithm convention,

\[
\boxed{L(1,\chi)=-\frac{\tau(\chi)}q
\sum_{b=1}^{q-1}\overline{\chi(b)}
\log(1-e(-b/q)).}
\tag{1.2}
\]

**Proof.** Let \(r\uparrow1\) in (1.1). Each finite logarithmic term converges to the displayed value; none of its arguments is zero. The Abel argument identifies the left side with \(L(1,\chi)\). \(\square\)

For \(0<b<q\), factoring the argument gives the exact branch evaluation

\[
1-e(-b/q)=2\sin(\pi b/q)e^{i(\pi/2-\pi b/q)},
\]

and thus

\[
\log(1-e(-b/q))
=\log(2\sin(\pi b/q))+i\pi(1/2-b/q).
\tag{1.3}
\]

The sine is positive, and the displayed argument belongs to \((-\pi/2,\pi/2)\). Replacing this logarithm by its real part before using the character's parity would discard information.

## 2. Parity separates the two formulas

**Theorem 2.1.** For primitive characters of conductor \(q>1\), the even and odd formulas are respectively

\[
\boxed{L(1,\chi)=-\frac{\tau(\chi)}q
\sum_{b=1}^{q-1}\overline{\chi(b)}
\log(2\sin(\pi b/q))\quad(\chi(-1)=1),}
\tag{2.1}
\]

\[
\boxed{L(1,\chi)=\frac{\pi i\tau(\chi)}{q^2}
\sum_{b=1}^{q-1}b\overline{\chi(b)}
\quad(\chi(-1)=-1).}
\tag{2.2}
\]

These formulas apply to complex characters as well as real ones.

**Proof.** Insert (1.3) in (1.2). Pair \(b\) with \(q-b\). The logarithm of the sine is unchanged by this pairing, whereas \(1/2-b/q\) changes sign. For an even character its imaginary contribution cancels, giving (2.1). For an odd character the real-logarithm contribution cancels. Also \(\sum_b\overline{\chi(b)}=0\), so the constant imaginary term vanishes and the remaining term is (2.2). Fixed points of the pairing cause no problem: if \(b=q/2\) occurs, it is a nonunit and its character value is zero. \(\square\)

There is therefore no formula using just \(\log|1-e(b/q)|\) for every primitive character: for an odd character the proposed symmetric sum is identically zero, while \(L(1,\chi)\ne0\). The real-logarithm formula has the explicit evenness hypothesis in (2.1).

### Worked values at conductors 3 and 4

For \(\chi_{-4}\), the sum in (2.2) is \(1-3=-2\), and \(\tau(\chi_{-4})=2i\). Hence

\[
L(1,\chi_{-4})=\frac{\pi i(2i)}{16}(-2)=\frac\pi4.
\]

For \(\chi_{-3}\), the weighted sum is \(1-2=-1\), and the Gauss sum is \(i\sqrt3\). Thus

\[
L(1,\chi_{-3})=\frac{\pi i(i\sqrt3)}9(-1)
=\frac\pi{3\sqrt3}.
\tag{2.3}
\]

These two positive values check both the sign and the normalization of the odd formula.

### An even character and a complex character modulo 5

For \(\chi_5\), the values at \(1,2,3,4\) are \(1,-1,-1,1\), and \(\tau(\chi_5)=\sqrt5\). Pairing sine terms in (2.1) gives

\[
\begin{aligned}
L(1,\chi_5)
&=\frac2{\sqrt5}\log\frac{\sin(2\pi/5)}{\sin(\pi/5)}\\
&=\frac2{\sqrt5}\log\frac{1+\sqrt5}2
\approx0.43040894096.
\end{aligned}
\tag{2.4}
\]

To obtain the exact trigonometric value, put \(z=e(1/5)\) and \(v=z+z^{-1}=2\cos(2\pi/5)>0\). Divide \(1+z+z^2+z^3+z^4=0\) by \(z^2\); pairing conjugates gives \(1+v+(v^2-2)=0\). Hence \(v=(\sqrt5-1)/2\). Now \(c=2\cos(\pi/5)>0\) satisfies \(c^2=2+v=(3+\sqrt5)/2\). Taking its positive square root gives \(c=(1+\sqrt5)/2\). The sine quotient in (2.4) is \(2\cos(\pi/5)=c\).

For the quartic character \(\chi(2)=i\), the values are \(1,i,-i,-1\), so the character is odd. Its Gauss sum is
\(-2\sin(\pi/5)+2i\sin(2\pi/5)\), and the weighted conjugate sum is \(-3+i\). Consequently

\[
\begin{aligned}
L(1,\chi)=\frac{2\pi}{25}\bigl(&\sin(\pi/5)+3\sin(2\pi/5)\\
&+i(3\sin(\pi/5)-\sin(2\pi/5))\bigr).
\end{aligned}
\tag{2.5}
\]

The other quartic character is \(\overline\chi\); its value is the complex conjugate of (2.5). Neither value is a quadratic class-number formula.

## 3. Quadratic class numbers, with the unit convention explicit

We state the exact algebraic input used in this section. In the planned course *Number fields*, the lesson *The Dedekind zeta function and the analytic class number formula* supplies the analytic class-number theorem; *Abelian number fields and Dirichlet L-functions at s = 1* supplies its quadratic specialization and the factorization \(\zeta_K=\zeta L(s,\chi_d)\). The relation between proper form classes and narrow ideal classes is assigned to *Quadratic fields: ideal classes and binary quadratic forms*. These are identified internal proof providers; the analytic arguments of this lesson do not prove those algebraic theorems.

For a negative fundamental discriminant \(d\), let \(h(d)\) count proper classes of primitive positive definite binary quadratic forms. It equals the ideal class number. Write \(w_d\) for the number of roots of unity in the quadratic field. The internal class-number formula is

\[
L(1,\chi_d)=\frac{2\pi h(d)}{w_d\sqrt{|d|}},\qquad
w_d=\begin{cases}6&d=-3,\\4&d=-4,\\2&d<-4.\end{cases}
\tag{3.1}
\]

For a positive fundamental discriminant \(d>1\), let \(h^+(d)\) be the narrow class number, equivalently the number of proper form classes. Let \(\epsilon_+(d)>1\) be the least positive unit of norm \(+1\). Thus

\[
\epsilon_+(d)=\frac{t_0+u_0\sqrt d}2,
\qquad t_0^2-du_0^2=4,\quad t_0,u_0>0,
\]

where the pair gives the smallest unit greater than 1. The matching formula is

\[
L(1,\chi_d)=\frac{h^+(d)\log\epsilon_+(d)}{\sqrt d}.
\tag{3.2}
\]

This choice of unit must be kept together with the narrow class number. If \(h(d)\) instead denotes the ordinary ideal class number and \(\epsilon(d)>1\) the least positive unit of either norm, the equivalent formula is

\[
L(1,\chi_d)=\frac{2h(d)\log\epsilon(d)}{\sqrt d}.
\tag{3.3}
\]

Indeed, if a unit of norm \(-1\) exists then \(h^+=h\) and \(\epsilon_+=\epsilon^2\). If none exists then \(h^+=2h\) and \(\epsilon_+=\epsilon\). The quadratic-fields lesson supplies these class-group facts. Equations (3.2) and (3.3) agree in both cases.

**Corollary 3.1.** The class-number formulas imply

\[
L(1,\chi_d)\ge\frac\pi{3\sqrt{|d|}}\quad(d<0),
\qquad
L(1,\chi_d)\ge\frac\pi{\sqrt{|d|}}\quad(d<-4),
\tag{3.4}
\]

and, for \(d>1\),

\[
L(1,\chi_d)\ge\frac{\log((1+\sqrt d)/2)}{\sqrt d}
\ge\frac{\log(\sqrt d/2)}{\sqrt d}.
\tag{3.5}
\]

In particular \(L(1,\chi)\gg q^{-1/2}\) for every real primitive nonprincipal character of conductor \(q\), with an absolute positive constant.

**Proof.** A class group has at least its identity, so both relevant class numbers are at least 1. In (3.1), \(w_d\le6\), and \(w_d=2\) for \(d<-4\), proving (3.4). For the unit in (3.2), the positive integers \(t_0,u_0\) are at least 1; hence \(\epsilon_+\ge(1+\sqrt d)/2\), proving (3.5). Every positive fundamental discriminant of a nontrivial quadratic field is at least 5. Thus its logarithm in the first bound of (3.5) is at least \(\log((1+\sqrt5)/2)>0\). The real-character classification in *Dirichlet characters* now proves the uniform assertion. The discriminant 1 belongs to the principal character at modulus 1 and is excluded. \(\square\)

### Discriminants 5 and minus 23

For \(d=5\), \((t,u)=(3,1)\) solves \(t^2-5u^2=4\). Any positive solution giving a unit greater than 1 has \(u\ge1\); the expression \((\sqrt{5u^2+4}+u\sqrt5)/2\) increases with \(u\). Thus the least norm-positive unit is \((3+\sqrt5)/2\). Its logarithm is twice \(\log((1+\sqrt5)/2)\). The independently obtained finite formula (2.4), together with (3.2), then gives \(h^+(5)=1\). This checks the unit normalization instead of changing it to fit the finite value.

For \(d=-23\), the quadratic character is \((n/23)\), and direct enumeration of the nonzero squares gives

\[
\sum_{n=1}^{22}n\left(\frac n{23}\right)=-69.
\]

Using \(\tau(\chi_{-23})=i\sqrt{23}\) in (2.2) gives
\(L(1,\chi_{-23})=3\pi/\sqrt{23}\). Formula (3.1), with \(w_{-23}=2\), gives \(h(-23)=3\). The form representatives are
\((1,1,6),(2,1,3),(2,-1,3)\). To check that list using the reduction theorem in the quadratic-fields lesson, a reduced positive form satisfies \(|b|\le a\le c\) and \(a\le\sqrt{23/3}<3\), with \(b\ge0\) on the boundary \(|b|=a\) or \(a=c\). Inserting \(a=1,2\) in \(b^2-4ac=-23\) leaves exactly the three displayed forms.

## 4. A lower bound using only analysis

The class-number argument gives a stronger result for primitive real characters. The following weaker estimate applies to every real nonprincipal character, including imprimitive ones, and has a fully analytic proof.

**Theorem 4.1.** Uniformly for real nonprincipal characters modulo \(q\),

\[
L(1,\chi)\gg\frac1{\sqrt q(1+\log q)^2}
\gg\frac1{\sqrt q(\log q)^2}.
\tag{4.1}
\]

The implied constants are absolute and effectively obtainable from the Pólya–Vinogradov constant. No class-number formula is used.

**Proof.** Put \(r(n)=\sum_{a\mid n}\chi(a)\). At a prime power its value is \(k+1\) if \(\chi(p)=1\), 1 if \(\chi(p)=0\), and 1 or 0 according as \(k\) is even or odd if \(\chi(p)=-1\). Multiplicativity therefore gives
\(r(n)\ge0\) and \(r(m^2)\ge1\). Define the triangularly weighted sum

\[
T(x)=\sum_{n\le x}r(n)(1-n/x),\qquad x\ge8.
\]

The square terms alone imply

\[
T(x)\ge\sum_{m\le\sqrt{x/2}}(1-m^2/x)
\ge\frac12\left\lfloor\sqrt{x/2}\right\rfloor
\ge\frac{\sqrt x}{4\sqrt2}.
\tag{4.2}
\]

To estimate the same sum from above, write \(k=\lfloor y\rfloor\). Direct summation and integration give the exact identity

\[
\sum_{b\le y}(1-b/y)
=k-\frac{k(k+1)}{2y}
=\frac y2-\frac1y\int_0^y\{t\}\,dt
\quad(y>0).
\tag{4.3}
\]

Expanding the divisor sum in \(T\), then using (4.3) with \(y=x/a\), gives

\[
T(x)=\frac x2\sum_{a\le x}\frac{\chi(a)}a
-\frac1x\int_0^x\{t\}
\sum_{a\le\min(x,x/t)}a\chi(a)\,dt.
\tag{4.4}
\]

At \(t=0\), the inner upper endpoint is interpreted as \(x\). All rearrangements involve finite sums.

By Pólya–Vinogradov, the partial sums \(A(u)=\sum_{a\le u}\chi(a)\) satisfy \(|A(u)|\le B\), where \(B=2\sqrt q(1+\log q)\). Partial summation gives

\[
\left|\sum_{a>x}\frac{\chi(a)}a\right|\le\frac{2B}x,
\qquad
\left|\sum_{a\le u}a\chi(a)\right|\le2Bu.
\tag{4.5}
\]

For the first bound, integrate \(A\) against \(1/u^2\) and include the boundary value at \(x\); for the second, use \(uA(u)-\int_0^u A(v)\,dv\). In (4.4), split the integral at \(t=1\). Its contribution on \((0,1)\) is at most \(2B\), and on \((1,x)\) at most \(2B\int_1^x dt/t\). Consequently

\[
T(x)=\frac x2L(1,\chi)+E(x),\qquad
|E(x)|\le B(3+2\log x).
\tag{4.6}
\]

Choose \(x=Kq(1+\log q)^4\), with \(K\ge1\) an absolute constant to be fixed. Set \(v=1+\log q\ge1\). Then
\(\log x\le\log K+5v\), so

\[
|E(x)|\le2\sqrt q\,v(3+2\log K+10v)
\le(26+4\log K)\sqrt q\,v^2.
\]

Meanwhile (4.2) gives
\(T(x)\ge\sqrt K\sqrt q\,v^2/(4\sqrt2)\).
Choose \(K\) so large that
\(26+4\log K\le\sqrt K/(8\sqrt2)\); such a computable constant exists because \(\log K=o(\sqrt K)\). Then the error in (4.6) is at most half the lower bound in (4.2). Therefore

\[
\frac x2L(1,\chi)\ge\frac{\sqrt x}{8\sqrt2},
\qquad
L(1,\chi)\ge\frac1{4\sqrt{2K}\sqrt q\,v^2}.
\]

This proves the first inequality of (4.1). A nonprincipal character has \(q\ge3\), and \(1+\log q\ll\log q\) there, proving the second. \(\square\)

The smoothing in (4.3) is what makes the argument work. A sharp divisor count has floor errors too large to compare effectively with just its square terms. The triangular weight turns those errors into a single integral controlled by character cancellation.

For an imprimitive character induced by a real primitive \(\chi^*\), its value at 1 also satisfies

\[
L(1,\chi)=L(1,\chi^*)
\prod_{p\mid q\atop p\nmid q^*}(1-\chi^*(p)/p).
\]

Every added factor is positive, but factors with \(\chi^*(p)=1\) can decrease the value. This is why the conductor-sensitive primitive class-number statement and the modulus-uniform analytic statement are kept distinct.

## 5. Critical integers and powers of pi

The archimedean factor on the \(s\) side of the functional equation is \(\Gamma((s+a)/2)\), while on the \(1-s\) side it is \(\Gamma((1-s+a)/2)\). An integer \(m\) is critical when neither factor has a pole there. Gamma poles occur at nonpositive integers, so the complete list is

\[
\begin{cases}
m\ge1,\quad m\equiv a\pmod2,\\
m\le0,\quad m\not\equiv a\pmod2.
\end{cases}
\tag{5.1}
\]

Indeed, for \(m\ge1\) the first Gamma argument is positive. The second is a nonpositive integer exactly when \(m\equiv1+a\pmod2\). For \(m\le0\) the second Gamma argument is positive, and the first is a nonpositive integer exactly when \(m\equiv a\pmod2\). This also shows why a trivial zero is not itself a critical integer.

For \(n\ge1\) with \(n\equiv a\pmod2\), use the asymmetric functional equation at \(s=n\), with the character \(\overline\chi\). Its trigonometric factor is \(2i^{-n}\) in these parity cases. Combining it with \(L(1-n,\overline\chi)=-B_{n,\overline\chi}/n\) gives

\[
\boxed{L(n,\chi)=-\frac{q^{1-n}(2\pi)^n i^n}
{2\tau(\overline\chi)\,n!}
B_{n,\overline\chi}.}
\tag{5.2}
\]

Character values and roots of unity are algebraic. Formula (5.2) therefore proves \(L(n,\chi)/\pi^n\) algebraic at these positive critical integers. The negative critical values are already algebraic by the generalized Bernoulli formula. This conclusion is specific to the critical parity: at a noncritical positive integer the matching Bernoulli value vanishes and the direct division used in (5.2) is unavailable.

## 6. Exercises

1. **Easy.** Derive \(L(1,\chi_{-3})=\pi/(3\sqrt3)\) from the odd formula.
2. **Medium.** Derive the odd finite formula from the general complex-logarithm formula, keeping the branch and all signs explicit.
3. **Medium.** Give closed forms for \(L(1,\chi)\) for both quartic characters modulo 5.
4. **Medium.** Compute \(L(1,\chi_5)\) by the even finite formula and compare it with the norm-positive-unit class-number convention.
5. **Hard.** Prove \(L(1,\chi)\gg q^{-1/2}(\log q)^{-c}\) for every real nonprincipal character without a class-number formula. Give the exponent \(c\) your proof achieves.

## 7. Solutions

**1.** The nonzero character values modulo 3 are \(1,-1\), the weighted sum is \(-1\), and its Gauss sum is \(i\sqrt3\). Inserting them in (2.2) gives \(\pi\sqrt3/9=\pi/(3\sqrt3)\). In particular the result is positive, as required by the earlier nonvanishing theorem for real characters.

**2.** The negative-exponential Gauss inversion leads to (1.2). For \(0<b<q\), write
\(1-e(-b/q)=2\sin(\pi b/q)e^{i(\pi/2-\pi b/q)}\).
This argument is in the chosen branch. In an odd character sum the symmetric real logarithms cancel under \(b\mapsto q-b\). The constant imaginary term cancels because the total conjugate character sum is zero. The remaining logarithmic sum is
\(-i\pi q^{-1}\sum_b b\overline{\chi(b)}\).
Multiplication by \(-\tau(\chi)/q\) gives (2.2). Using absolute values inside the logarithms would give zero and would lose this argument.

**3.** For \(\chi(2)=i\), the conjugate weighted sum is \(1-2i+3i-4=-3+i\). Put \(A=2\sin(\pi/5)\), \(B=2\sin(2\pi/5)\), so \(\tau(\chi)=-A+iB\). Then
\(i\tau(\chi)(-3+i)=A+3B+i(3A-B)\).
Multiplication by \(\pi/25\) gives (2.5). For the second quartic character conjugate that result. These are closed forms in \(\pi\) and algebraic numbers, since the two sine values are
\(\sqrt{10-2\sqrt5}/4\) and \(\sqrt{10+2\sqrt5}/4\), respectively.

**4.** Pair the values \(1,-1,-1,1\) at \(1,2,3,4\) in the even formula. The finite logarithmic sum is
\(2\log(\sin(\pi/5)/\sin(2\pi/5))=-2\log\varphi\), where \(\varphi=(1+\sqrt5)/2\). Its Gauss prefactor is \(-1/\sqrt5\), giving \(L(1,\chi_5)=2\log\varphi/\sqrt5\). The smallest norm-positive unit is \((3+\sqrt5)/2=\varphi^2\); its logarithm is \(2\log\varphi\). The narrow formula (3.2) therefore gives \(h^+(5)=1\) and exactly the same value. The ordinary unit \(\varphi\) has norm \(-1\), and inserting it into (3.2) without changing to the ordinary-class formula (3.3) would incorrectly halve the answer.

**5.** The proof in Section 4 gives \(c=2\) uniformly, with an effective absolute constant. Its essential ingredients are the nonnegative divisor function \(1*\chi\), which is at least 1 at every square, the exact triangular-sum identity (4.3), and the uniform interval bound \(B=2\sqrt q(1+\log q)\). Those give the fully explicit error estimate (4.6). Choosing \(x=Kq(1+\log q)^4\) with \(26+4\log K\le\sqrt K/(8\sqrt2)\) forces that error below half of the positive square contribution. Dividing by \(x/2\) gives
\(L(1,\chi)\ge[4\sqrt{2K}\sqrt q(1+\log q)^2]^{-1}\).
This proves the requested result for every real nonprincipal character. All constants were fixed independently of its conductor; no class-number assertion entered the proof.

## What this lesson takes from the number-fields course

The exact formulas (3.1)–(3.3), the equality between proper form classes and narrow ideal classes, the unit-norm dichotomy for narrow class numbers, and the reduction theorem for positive definite forms are supplied by the three planned internal lessons identified in Section 3. Their status is planned, not a claim that the number-fields course is already finished. Every finite-value identity, the class-number consequences from those precise inputs, the separate analytic lower bound, the critical-integer test and all solutions are proved here. The generalized Bernoulli formula and the functional equation were proved in the preceding lesson.

## References

D. Koukoulopoulos, *The Distribution of Prime Numbers*, Theorem 12.8, proves the analytic lower bound with the logarithmic exponent 2 by smoothing a nonnegative divisor sum. The finite logarithmic and linear formulas follow from the classical character Fourier expansion; their branch and parity calculations are supplied above. The term “critical” uses the archimedean-pole criterion of P. Deligne, *Valeurs de fonctions L et périodes d'intégrales*, Definition 1.3; its criterion in this Dirichlet setting is explicitly checked in (5.1).
