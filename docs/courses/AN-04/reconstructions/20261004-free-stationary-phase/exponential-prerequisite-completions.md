# Exponentials, circle coordinates and the Gaussian branch

Prerequisite companion. It follows Jiří Lebl's freely accessible *Basic Analysis*, version 6.3, [author edition](https://www.jirka.org/ra/). Original text: public domain (CC0).
The exact sources are §§2.6.4, 3.3.2, 5.4, 11.1 and 11.4.
Complete programme proofs are retained through exact statement and proof
locators. The additions below supply the exercises and intermediate steps
actually needed by Q1–Q9, the Gaussian example and the smooth cutoffs in the
full stationary-phase lesson. No general complex identity theorem, improper
integration theorem, area formula or arc-length theorem is assumed here.

The earlier topology, differential and compact-integral chains supply the
ordered complete real field, finite-dimensional Euclidean spaces, derivatives,
compact Riemann integrals, inverse functions and integral Taylor formula.
Identify \(\mathbb C\) with \(\mathbb R^2\), with operations defined in
Lebl §11.1. A series means the limit of its finite partial sums; \(0!=1\)
and \((n+1)!=(n+1)n!\). These are definitions, not additional theorem imports.

## P13. The complex-number exercises used below

### P13.1. Field operations, modulus and differential rules

For \(z=a+ib\), set
\[
 T_z=\begin{pmatrix}a&-b\\b&a\end{pmatrix}.
\]
Direct multiplication gives \(T_zT_w=T_{zw}\), while addition gives
\(T_z+T_w=T_{z+w}\). The first column recovers \(z\), so this map is
injective. Associativity and distributivity therefore follow from the finite
matrix rules: the \((j,k)\) entries of \((AB)C\) and \(A(BC)\) are
both \(\sum_{l,r}A_{jl}B_{lr}C_{rk}\), with finite sums freely regrouped.
The displayed complex multiplication is commutative; \(1\) is its identity.
For \(z\ne0\),
\[
 z\bar z=a^2+b^2>0,\qquad
 z^{-1}=\frac{a-ib}{a^2+b^2}.
\]
These formulas prove the field assertion left as Exercise 11.1.1. Expanding
real and imaginary components also gives
\(\overline{zw}=\bar z\bar w\) and
\(\overline{z+w}=\bar z+\bar w\). Consequently
\[
 |zw|^2=zw\overline{zw}=|z|^2|w|^2,
 \qquad |zw|=|z||w|.
\]
The last equality uses the unique nonnegative square root (P8), so it also
covers zero factors. This completes Exercise 11.1.2.

The modulus is the Euclidean norm already proved in the topology chain.
Its triangle and reverse-triangle inequalities imply continuity. Conjugation
is an isometry. For \(w\ne0\) and \(|w'-w|<|w|/2\),
\[
 |w'|>|w|/2,\qquad
 |(w')^{-1}-w^{-1}|\leq 2|w'-w|/|w|^2.
\]
Together with the coordinatewise real limit laws this proves all of
Proposition 11.1.3, including its omitted quotient case. Its hypotheses require
nonzero denominators; the estimate proves that they are eventually nonzero
whenever their limit is nonzero.

The real-coordinate polynomial formulas show that addition, multiplication
and conjugation are smooth; the inverse formula and P10 show that inversion
is smooth away from zero. For differentiable complex-valued functions of a
real variable the product rule is
\((fg)'=f'g+fg'\): apply the real product rule to the two displayed
coordinates of the product. The reciprocal rule follows by differentiating
\(f f^{-1}=1\), giving \((f^{-1})'=-f'/f^2\). These arguments apply
to each real parameter coordinate, with higher regularity supplied by P11.1.
Complex integration is exactly the two-component integral of P12.3–P12.4;
its norm bound, fundamental theorem and integral Taylor formula are therefore
already proved. \(\square\)

### P13.2. Series tails and the complex form of Mertens' proof

The metric completeness of \(\mathbb R^2\) (Lebl Proposition 7.4.4)
is the completeness of \(\mathbb C\). If \(s_n=\sum_{j=0}^n z_j\),
then for \(k>n\),
\(s_k-s_n=\sum_{j=n+1}^k z_j\). Thus the tail condition of
Proposition 11.1.4 is precisely the Cauchy condition for \(s_n\);
reverse the two indices for \(n>k\), and use zero for equal indices.
This proves the exercise. If \(\sum |z_j|\) converges, the finite triangle
inequality bounds every such tail by the corresponding real tail. Hence
\(s_n\) is Cauchy and converges, proving Proposition 11.1.5.
Also, a convergent series has terms tending to zero: subtract successive
partial sums. A convergent complex sequence is bounded by P6.1.

Retain the complete proof of Mertens' theorem, Lebl Theorem 2.6.5
(`sec_moreonseries.html`, proof `sec_moreonseries-6-5`). It works for complex
\(a_n,b_n\) without an order on those numbers. All comparisons in that
proof concern their nonnegative moduli. To make this extension explicit, set
\(A_m=\sum_{j=0}^m a_j\), \(B_m=\sum_{j=0}^m b_j\), and suppose
\(A_m\to A\), \(B_m\to B\), \(S=\sum|a_j|<\infty\).
For \(c_n=\sum_{j=0}^n a_jb_{n-j}\), the same finite regrouping gives
\[
 \left|\sum_{n=0}^m c_n-AB\right|
 \leq\sum_{n=0}^m |B_n-B|\,|a_{m-n}|+|B|\,|A_m-A|.
\]
Write \(D=\sup_n|B_n-B|<\infty\). Choose \(K\geq1\) so that,
for all \(m\geq K\), both limit errors are below \(\varepsilon\)
and \(\sum_{n=K}^m|a_n|<\varepsilon\); the latter follows from the
real Cauchy condition for the convergent modulus partial sums. For
\(m\geq2K\), split the first sum at \(m-K\). Its first part is at
most \(D\varepsilon\), since its \(a\)-indices are at least \(K\).
Its second part is at most \(S\varepsilon\), since its \(B\)-indices
are greater than \(K\). The total is at most
\(\varepsilon(D+S+|B|)\). Choosing
\(\varepsilon=\delta/(1+D+S+|B|)\) proves convergence to \(AB\).
If the \(b\)-series is the absolutely convergent one, interchange the two
series; the finite convolution is unchanged. This retains the full
one-absolutely-convergent-factor generality of the human proof. \(\square\)

## P14. The existing real logarithm and exponential proofs

### P14.1. The intermediate-value and logarithm dependencies

Lebl Lemma 3.3.7 and Theorem 3.3.8 contain complete proofs of the intermediate
value theorem. Their bisection sequences use the already bound increasing and
decreasing monotone convergence theorems, the geometric limit
\(2^{-n}\to0\), limit subtraction, continuity along sequences and preservation
of weak inequalities in limits. The source explicitly proves that both
sequences have the same limit and that the root lies strictly between the
endpoints. Thus no root-existence assertion is taken from an exercise.
If a target equals an endpoint value, that endpoint itself supplies the value.

Retain Proposition 5.4.1(i)–(iv) and its proof: define
\[
 L(x)=\int_1^x t^{-1}\,dt\quad(x>0).
\]
The integrand is continuous on each compact positive interval. The oriented
integral convention covers \(x<1\); the proved fundamental theorem gives
\(L'=1/x\). For \(a<b\), the mean value theorem gives
\(L(b)-L(a)=(b-a)/c>0\) for some \(c\in(a,b)\).
The source's positive linear substitution, now justified by the full oriented
one-variable substitution proof, gives \(L(xy)=L(x)+L(y)\).
This identity holds for all \(x,y>0\), including \(x<1\).

For clarity, the onto argument needs only integer powers: induction yields
\(L(2^n)=nL(2)\), where \(L(2)\geq1/2\). Given \(M>0\),
P6.0 supplies \(n\) with \(n/2>M\); the intermediate value theorem
on \([1,2^n]\) produces every target in \([0,M]\).
Since \(L(1/x)=-L(x)\), every negative target is also attained.
Monotonicity proves the two endpoint limits. Uniqueness follows by integrating
the prescribed derivative and value at 1, exactly as in the source.
The unused rational-power assertion (v) is not imported here. \(\square\)

### P14.2. Global inverse and all required real derivatives

Retain Proposition 5.4.2(i)–(iv) and its uniqueness proof. The preceding
bijection defines \(E=L^{-1}:\mathbb R\to(0,\infty)\). The source
uses its one-dimensional inverse theorem; the already proved programme
inverse theorem P3 supplies that exact derivative as well. At each positive
point, \(L'\ne0\), so a smooth local inverse exists. Its values equal the
global inverse by injectivity of \(L\). These local formulas cover the real
line and yield
\[
 E(0)=1,\qquad E'(x)=1/L'(E(x))=E(x).
\]
Here \(L\) is smooth because \(L'=1/x\) is smooth by P10.5.
Thus \(E\) is smooth, and induction gives \(E^{(k)}=E\) for every
\(k\geq0\). Positivity gives strict increase by the mean value theorem.
The source proves its endpoint limits from monotonicity and its full positive
range, and proves \(E(x+y)=E(x)E(y)\) by applying the logarithm law.
In particular \(E(x)E(-x)=1\). Its uniqueness proof differentiates
\(F(x)E(-x)\): if \(F'=F\), \(F(0)=1\), the derivative is zero,
so the product is identically 1 by the proved zero-derivative theorem.
Consequently \(F=E\), even when \(F\) is not assumed positive.
We write \(e^x=E(x)\). The unused rational-power part is again excluded.

For \(u>0\) and \(\alpha\in\mathbb R\), define
\(u^\alpha=\exp(\alpha L(u))\). This agrees with integer powers by
the logarithm law and induction, including negative integers. The chain rule
gives
\[
 (u^\alpha)'=\alpha u^{\alpha-1}.
\]
Indeed the derivative is \(\alpha u^{-1}\exp(\alpha L(u))\), and
\(\exp(-L(u))=u^{-1}\). Iteration gives every derivative, with the
falling product \(\alpha(\alpha-1)\cdots(\alpha-k+1)\), including
zero factors. For \(\alpha=1/2\), positivity and squaring identify this
definition with the previously proved positive square root. \(\square\)

### P14.3. Exponential decay and the flat cutoff function

For \(t\geq0\), apply P12.6 to \(e^t\). Every Taylor coefficient at
zero equals 1 and the integral remainder is nonnegative. Thus, for every
integer \(N\geq0\), \(e^t\geq t^N/N!\).
For \(c>0\) and integer \(m\geq0\), choose \(N=m+1\); for \(t>0\),
\[
 0\leq t^m e^{-ct}\leq \frac{(m+1)!}{c^{m+1}t}\longrightarrow0.
\]
More generally, choosing \(2N>m\) gives
\(r^m e^{-cr^2}\leq N!c^{-N}r^{m-2N}\to0\) as \(r\to\infty\).
The negative integer-power limit follows from P6.0 and the real product laws.
These bounds justify the polynomial times Gaussian boundary limits used in
Q2 and E1; existence of their improper integrals is still an F0-INT question.

Define \(\rho(t)=e^{-1/t}\) for \(t>0\), and \(\rho(t)=0\) for
\(t\leq0\), as in Exercise 5.4.11. Repeated differentiation on \(t>0\)
gives \(\rho^{(k)}(t)=P_k(1/t)e^{-1/t}\) with a polynomial \(P_k\):
\(P_0=1\), and
\(P_{k+1}(u)=u^2(P_k(u)-P'_k(u))\).
The decay estimate shows that every such expression tends to zero at the
origin, even after division by \(t\). Extend each by zero on \(t\leq0\).
The resulting function is continuous at zero and its difference quotient
there tends to zero. Induction therefore proves that \(\rho\) is smooth
on \(\mathbb R\), with every derivative zero at 0.
This proves the used exercise rather than importing it unanswered.
\(\square\)

## P15. The complex exponential with explicit convergence arguments

### P15.1. The series and all real partial derivatives

Use the definition of Lebl §11.4.1,
\[
 \mathcal E(z)=\sum_{k=0}^\infty\frac{z^k}{k!}.
\]
Its convergence and differentiation are justified here at exactly the needed
scope. Fix \(R\geq1\) and choose an integer \(K\) with \(K+1\geq2R\).
For \(k\geq K\), the ratio of successive nonnegative majorants
\(R^k/k!\) is at most \(1/2\). Hence, for \(N\geq K\),
\[
 \sum_{k=N+1}^{M}\frac{|z|^k}{k!}
 \leq\frac{2R^{N+1}}{(N+1)!}\longrightarrow0
 \quad(|z|\leq R,\ M>N).
\]
The convergence to zero follows from the same geometric ratio bound and the
already proved \(2^{-n}\to0\). Thus the series converges absolutely and
uniformly on each closed disk by completeness (P13.2).

Put \(S_N(z)=\sum_{k=0}^N z^k/k!\), and write \(z=x+iy\).
Polynomial differentiation gives, for \(N\geq a+b\),
\[
 \partial_x^a\partial_y^b S_N(z)=i^bS_{N-a-b}(z).
\]
Here \(\partial_x z^k=kz^{k-1}\), \(\partial_y z^k=ikz^{k-1}\)
follow by induction using the complex product rule of P13.1. All these
sequences converge uniformly on each disk to \(i^b\mathcal E\).

The uniform limit is continuous: at a fixed point and for a given
\(\varepsilon>0\), approximate it uniformly by one continuous polynomial
within \(\varepsilon/3\), then bound that polynomial's change by
\(\varepsilon/3\). At any point choose a disk with strictly larger radius,
so sufficiently short coordinate segments stay inside it. For such a segment, the fundamental
theorem applied to each polynomial gives its endpoint difference as the
integral of its coordinate derivative. P12.4 passes the uniform derivative
limit through this compact integral. The resulting identity and the
fundamental theorem show that \(\partial_x\mathcal E=\mathcal E\)
and \(\partial_y\mathcal E=i\mathcal E\). Repeating the same argument
for the displayed derivatives, or differentiating these two identities
inductively, gives every continuous ordered partial. P11.1 then gives
\(\mathcal E\in C^\infty(\mathbb R^2)\).

On the real axis the partial sums, hence their limit, are real;
\(\mathcal E(0)=1\) and \(\mathcal E'=\mathcal E\). The uniqueness
proved in P14.2 identifies this restriction with the real exponential.
We now write \(e^z=\mathcal E(z)\). Its real derivative is multiplication
by \(e^z\): for \(v=u+iw\),
\(De^z[v]=u e^z+w i e^z=e^zv\). In particular, for every smooth
complex-valued path or real-parameter map, the chain rule gives
\(\partial_j e^{f}=e^f\partial_j f\), with all higher derivatives
obtained by the already proved product rules. \(\square\)

### P15.2. Addition, conjugation and modulus

Use the complete Mertens argument retained in P13.2. Both exponential
series converge absolutely. Their convolution coefficient is
\[
 \sum_{j=0}^n\frac{z^jw^{n-j}}{j!(n-j)!}=\frac{(z+w)^n}{n!}.
\]
The finite binomial identity here follows by induction: multiply the formula
for power \(n\) by \(z+w\), group equal monomials and use
\(\binom n{j-1}+\binom n j=\binom{n+1}j\), which follows by putting
the factorial fractions over their common denominator. The endpoint
coefficients are 1 and the induction starts at \(n=0\).
Consequently \(e^{z+w}=e^ze^w\). This uses the human Cauchy-product proof
already in the programme; it supplies the law of exponents without importing
the complex identity theorem used by the alternative proof of Proposition
11.4.1. No claim about that identity theorem's proof closure is made.

Conjugation commutes with each finite sum and with limits by P13.1, giving
\(\overline{e^z}=e^{\bar z}\). Also \(e^ze^{-z}=e^0=1\), so
the exponential never vanishes and its reciprocal is \(e^{-z}\).
For \(z=x+iy\),
\[
 |e^{iy}|^2=e^{iy}e^{-iy}=1,\qquad
 |e^{x+iy}|=e^x.
\]
The second identity uses the real positivity proved in P14.2. These are the
exact modulus and reciprocal identities used in Q1–Q9. \(\square\)

## P16. Trigonometry and the right-half-plane square root

### P16.1. The elementary identities and derivative exercises

Retain Lebl's definitions
\[
 \cos z=(e^{iz}+e^{-iz})/2,\qquad
 \sin z=(e^{iz}-e^{-iz})/(2i).
\]
They immediately give Euler's identity, the values at zero and the even/odd
identities. Combining finite exponential partial sums and taking their limits
gives the series
\[
 \cos z=\sum_{k=0}^\infty\frac{(-1)^kz^{2k}}{(2k)!},\qquad
 \sin z=\sum_{k=0}^\infty\frac{(-1)^kz^{2k+1}}{(2k+1)!}.
\]
Indeed the even coefficients add and the odd ones cancel in the first
formula; the reverse happens in the second. The truncated sums are
subsequences of those combinations, and the omitted last term tends to zero
by P13.2. This completes Exercise 11.4.1 without an infinite rearrangement.

For real \(t\), conjugation gives
\(\cos t=\operatorname{Re}e^{it}\),
\(\sin t=\operatorname{Im}e^{it}\). If \(A=e^{iz}\), \(B=e^{-iz}\),
then \(AB=1\); therefore
\[
 (\cos z)^2+(\sin z)^2=((A+B)^2-(A-B)^2)/4=1.
\]
This proves the complex identity left in Exercise 11.4.6 as well as its real
case. In the real case it implies \(|\sin t|,|\cos t|\leq1\).
P15.1 and the finite product rule give
\[
 \frac{d}{dt}\cos t=(ie^{it}-ie^{-it})/2=-\sin t,\qquad
 \frac{d}{dt}\sin t=(ie^{it}+ie^{-it})/(2i)=\cos t.
\]
Thus the derivative exercise is complete. The derivative of
\(t-\sin t\) is \(1-\cos t\geq0\); the mean value theorem yields
\(\sin t\leq t\) for \(t\geq0\), as in the source.
Finally, substitute the definitions and the exponential addition law into
both sides to obtain, for all complex \(z,w\),
\[
 \cos(z+w)=\cos z\cos w-\sin z\sin w,\qquad
 \sin(z+w)=\sin z\cos w+\cos z\sin w.
\]
For example the first right-hand side simplifies to
\((e^{iz}e^{iw}+e^{-iz}e^{-iw})/2\); the second simplifies to their
difference divided by \(2i\). This completes Exercise 11.4.7.
\(\square\)

### P16.2. Existence of the first zero and the period

Keep the first-zero argument of Proposition 11.4.2, making its supremum step
explicit. Let
\[
 S=\{y>0:\cos t>0\text{ for every }0\leq t<y\}.
\]
Continuity and \(\cos0=1\) make \(S\) nonempty. Choose \(a>0\)
so small that \([0,2a]\) has positive cosine. On that interval sine is
strictly increasing, so \(\sin a>0\). For \(y\in S\), \(y>a\),
the source's mean value estimate gives
\[
 2\geq\cos a-\cos y=(y-a)\sin c\geq(y-a)\sin a
 \quad\text{for some }a<c<y.
\]
Sine is increasing on \([a,y]\), since cosine is positive before \(y\).
Thus every such \(y\) is at most \(a+2/\sin a\); those with \(y\leq a\)
are bounded as well. Set \(b=\sup S\). For \(t<b\), some \(y\in S\)
is greater than \(t\), so \(\cos t>0\) on \([0,b)\).
Continuity gives \(\cos b\geq0\). If it were positive, continuity would
extend positivity past \(b\), contradicting its definition. Hence
\(\cos b=0\), and it is the first positive zero. Define \(\pi=2b\).
Sine is strictly increasing on \([0,b]\), with \(\sin b>0\);
the squared identity implies \(\sin b=1\). Therefore
\(e^{i\pi/2}=i\), \(e^{i\pi}=-1\), \(e^{2\pi i}=1\), and the
addition law gives period \(2\pi\) for the exponential, sine and cosine.

There is no need to assume a smallest positive return in order to prove its
value. Take any \(0<T\leq2\pi\) with \(e^{iT}=1\), and write
\(e^{iT/4}=u+iv\). Because \(0<T/4\leq b\), \(u\geq0\) and
\(v>0\). Its fourth power is 1, whose imaginary part gives
\(4uv(u^2-v^2)=0\). If \(u^2=v^2\), the real part is
\(-4u^4<0\), a contradiction. Thus \(u=0\), forcing \(T/4=b\)
by positivity of cosine before \(b\). Consequently \(T=2\pi\).
For any real \(T\), an integer translate puts \(T\) in \([0,2\pi)\):
by the Archimedean property there are integers above and below
\(T/(2\pi)\), and in that finite integer interval select its greatest
integer not exceeding \(T/(2\pi)\). Periodicity and the preceding result
show that all returns are exactly the integer multiples of \(2\pi\).

If sine alone has positive period \(T\), evaluating at 0 and \(\pi/2\)
gives \(\sin T=0\) and \(\cos T=1\), using its addition formula.
If cosine alone has period \(T\), its value at 0 gives \(\cos T=1\)
and the squared identity gives \(\sin T=0\). Thus both have least
positive period \(2\pi\). This supplies the individual-function step in
the source's joint-period argument. \(\square\)

### P16.3. All quadrants, the angle and the exact root phase

On \([0,b]\), cosine decreases strictly from 1 to 0, so the intermediate
value theorem gives every nonnegative unit vector: for \(u,v\geq0\),
\(u^2+v^2=1\), choose \(t\in[0,b]\) with \(\cos t=u\).
Then \(\sin t=v\), since both are nonnegative and their squares agree.
For an arbitrary unit vector \((u,v)\), first choose such a \(t\) for
\((|u|,|v|)\). According to the signs, the angles
\(t,\ \pi-t,\ \pi+t,\ 2\pi-t\) represent respectively the first,
second, third and fourth closed quadrants, by the addition identities.
Replace an endpoint \(2\pi\) by 0. The axis overlaps give the same point,
so no axis is omitted. If two angles in \([0,2\pi)\) give the same
point, their difference is a return strictly between \(-2\pi\) and
\(2\pi\), hence is zero by P16.2. This completes the source's
unit-circle exercise, including the case \((1,0)\).

On \((-b,b)\), \(\cos t>0\). The quotient rule gives
\[
 (\tan t)'=(\sin t/\cos t)'=1/(\cos t)^2>0.
\]
At its endpoints the numerator tends to \(\pm1\) and the denominator
to zero through positive values; thus its limits are \(\pm\infty\).
The intermediate value theorem and strict increase give a bijection onto
\(\mathbb R\). Its inverse \(\arctan\) is smooth by P3, with derivative
\((\arctan r)'=1/(1+r^2)\): apply the inverse formula and
\(1+\tan^2 t=1/\cos^2t\). These prove the arctangent inputs from
Exercise 11.4.11; its unrelated endpoint series is not used.

For \(z=x+iy\) with \(x>0\), put
\(r=\sqrt{x^2+y^2}>0\) and \(\theta=\arctan(y/x)\in(-b,b)\).
The positive-cosine identity gives \(\cos\theta=x/r\),
\(\sin\theta=y/r\), so \(z=r e^{i\theta}\). These functions are
smooth, and
\[
 s(z)=\sqrt r\,e^{i\theta/2},\qquad s(z)^2=z,\qquad
 \operatorname{Re}s(z)>0.
\]
Any other square root \(w\) satisfies \((w-s)(w+s)=0\) in the proved
field, hence is \(s\) or \(-s\). This proves uniqueness with positive
real part, smoothness on the right half-plane, and, along every differentiable
path there, \(2s s'=z'\). These are exactly Q2's branch claims.

For its boundary phase an algebraic expression is useful:
\[
 s(x+iy)=\sqrt{\frac{r+x}{2}}+
          i\,\frac{y}{2\sqrt{(r+x)/2}}.                 \tag{P16.1}
\]
The real part is positive. Squaring gives imaginary part \(y\) and real
part \((r+x)/2-y^2/(2(r+x))=x\), since \(r^2=x^2+y^2\).
Uniqueness therefore proves (P16.1).
The doubled-angle identity at \(t=\pi/4=b/2\) gives equal positive
sine and cosine, each \(1/\sqrt2\). Hence
\(e^{\pm i\pi/4}=(1\pm i)/\sqrt2\).
For \(h>0\), \(\lambda\ne0\), (P16.1) and continuity of the positive
real root give
\[
 (\varepsilon-i\lambda/h)^{-1/2}
 \longrightarrow
 \sqrt{h/|\lambda|}\,e^{i\pi\operatorname{sgn}(\lambda)/4}
 \quad(\varepsilon\downarrow0).
\]
Indeed the root itself tends to
\(\sqrt{|\lambda|/h}(1-i\operatorname{sgn}\lambda)/\sqrt2\),
whose nonzero reciprocal is the displayed value. This establishes the exact
phase used in Q6, rather than treating a choice of branch as a convention
with unproved consequences. Polar-coordinate integration remains a separate
F0-COV dependency. \(\square\)

The selected exponential and trigonometric arguments above do not establish
global or multidimensional integration, a change-of-variables theorem, or
closure of the full stationary-phase lesson. Those tasks remain explicit in
the main ledger.
