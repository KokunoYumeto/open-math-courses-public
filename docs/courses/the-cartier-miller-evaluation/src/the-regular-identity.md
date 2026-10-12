# The regular identity

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(f\) be a polynomial of degree three or four over \(\mathbb F_p\) without repeated root and with \(f(0)=1\), and let \(S_f(\lambda)\) be the truncated coefficient sum of [Truncated powers and points of a curve](truncated-powers-and-points-of-a-curve.md). This lesson proves the identity that expresses \(S_f(\lambda)\) through a function on the curve \(v^2=f(w)\).

Let \(Q^+\) and \(Q^-\) be the two points of the curve over \(w=1/\lambda\), and suppose \(F\) is a function whose only zero is at \(Q^+\) and whose only pole is at \(Q^-\), both of order \(M\). Let \(\Psi\) be the value at the point \(O=(0,1)\) of the logarithmic derivative of \(F\) with respect to the differential \(\omega=dw/v\). Then (Theorem 5.1), for \(\lambda\) in \(\mathbb F_p\),
\[
M\,(S_f(\lambda)-H)=(H-\chi)\,r\,\Psi ,
\]
where \(H\) is the coefficient of \(w^{p-1}\) in \(f^{(p-1)/2}\), \(\chi=\pm1\) is the quadratic character of \(f(1/\lambda)\), and \(r=1/(\lambda v_0)\) with \(v_0^2=f(1/\lambda)\). When \(M\) is not divisible by \(p\), this determines \(S_f(\lambda)\). For \(M\equiv1-\chi H\) modulo \(p\) and \(H\ne\chi\) it becomes \(S_f(\lambda)=H-\chi r\Psi\), the formula of [Jordan, Theorem 1] in its regular case.

The proof follows [Jordan, Proposition 2]: the differential \(dw/((1-\lambda w)v)\) and the logarithmic differential \(dF/F\) have the same poles, a suitable combination has none and is therefore a multiple of \(\omega\), and the Cartier operator is known on all three. It uses [The Cartier operator](the-cartier-operator.md) and [Points, orders and residues](points-orders-and-residues.md).

Whether a function \(F\) with the required zero and pole exists for a given \(M\) is a question about the group of divisor classes of the curve. It is not treated in this lesson: \(F\) is part of the data. Example 3.2 gives a case in which \(F\) can be written down.

## 1. The setting

Let \(p\) be an odd prime, \(h=(p-1)/2\), and \(k\) an algebraic closure of \(\mathbb F_p\). Let \(f\in\mathbb F_p[w]\) have degree three or four, no repeated root in \(k\), and \(f(0)=1\). We use, over the field \(k\):

- the field \(K\) of functions \(A+Bv\), its derivative \(D\), differentials, and the Cartier operator \(\mathcal C\) (lesson on the Cartier operator);
- the points of the curve, the expansions \(\iota_P\), orders, values and residues (lesson on points, orders and residues);
- the point \(O=(0,1)\), the differentials \(\omega=dw/v\) and \(\theta_\lambda=dw/((1-\lambda w)v)\), the coefficients \(c_m\) of \(f^h\), \(H=c_{p-1}\in\mathbb F_p\), and \(S_f(\lambda)=\sum_{m\le p-1}c_m\lambda^{p-1-m}\) for \(\lambda\in k\).

For a function \(g\) that is regular at \(O\) we write \(g(O)\) for its value, and for a differential \(\eta=g\,\omega\) we write \((\eta/\omega)(O)=g(O)\). The map \(g\mapsto g(O)\) is a homomorphism from the ring of functions regular at \(O\) to \(k\).

From the lesson on the Cartier operator (Theorem 6.1), since \(H\in\mathbb F_p\):
\[
\begin{gathered}
\mathcal C(\omega)=H\omega,\\
\mathcal C(\theta_\lambda)=u_\lambda\omega,\\
u_\lambda(O)^p=S_f(\lambda).
\end{gathered}
\]

## 2. The poles of the differential

Let \(\lambda\in k\), \(\lambda\ne0\), \(\mu=1/\lambda\), and suppose \(d=f(\mu)\ne0\). Choose \(v_0\in k\) with \(v_0^2=d\), and let
\[
\begin{gathered}
Q^+=(\mu,v_0),\qquad Q^-=(\mu,-v_0),\\
r=\frac1{\lambda v_0}.
\end{gathered}
\]
These are two different ordinary points, and neither is \(O\), because \(\mu\ne0\).

**Lemma 2.1.** The differential \(\theta_\lambda\) has simple poles at \(Q^+\) and \(Q^-\) and no other pole. Its residues are
\[
\begin{gathered}
\operatorname{res}_{Q^+}(\theta_\lambda)=-r,\\
\operatorname{res}_{Q^-}(\theta_\lambda)=r .
\end{gathered}
\]

**Proof.** \(\theta_\lambda=(1-\lambda w)^{-1}\omega\) and \(1-\lambda w=-\lambda(w-\mu)\). Since \(\omega\) has order \(0\) everywhere, \(\operatorname{ord}_P(\theta_\lambda)=-\operatorname{ord}_P(w-\mu)\). By Lemma 3.1 of the lesson on points, \(w-\mu\) has order \(1\) at the two ordinary points over \(\mu\), order \(0\) at the other affine points, and negative order at infinity. So \(\theta_\lambda\) has order \(-1\) at \(Q^\pm\), order \(0\) at the other affine points and positive order at infinity. At \(Q^\pm\) the expansion of \(w\) is \(\mu+z\), and that of \(v\) is a series \(v_\pm\) with constant term \(\pm v_0\); so the expansion of \(\theta_\lambda\) is
\[
\frac{dz}{-\lambda z\,v_\pm},
\]
with the coefficient \(-1/(\lambda(\pm v_0))=\mp r\) at \(z^{-1}\). \(\blacksquare\)

## 3. The identity

Let \(M\ge1\) be an integer. We say that a function \(F\) *has divisor \(M(Q^+)-M(Q^-)\)* if
\[
\begin{gathered}
\operatorname{ord}_{Q^+}(F)=M,\\
\operatorname{ord}_{Q^-}(F)=-M,\\
\operatorname{ord}_P(F)=0\quad(P\ne Q^+,Q^-).
\end{gathered}
\]
Such a function is unique up to a constant factor (Corollary 4.3 of the lesson on points), so \(dF/F\) depends only on \(M\) and the two points. By Proposition 5.4 of that lesson, \(dF/F\) has no pole at \(O\). Let
\[
\begin{aligned}
\Psi&=\Bigl(\frac{dF/F}{\omega}\Bigr)(O)\\
&=\Bigl(\frac{v\,D(F)}F\Bigr)(O).
\end{aligned}
\]

**Theorem 3.1.** Let \(\lambda\in k\), \(\lambda\ne0\), with \(f(1/\lambda)\ne0\), and let \(F\) have divisor \(M(Q^+)-M(Q^-)\). Then
\[
M\,(S_f(\lambda)-H)=r\,(H\Psi-\Psi^p).
\]

**Proof.** Let \(\eta=M\theta_\lambda+r\,dF/F\).

*\(\eta\) has no pole.* By Lemma 2.1 and Proposition 5.4 of the lesson on points, both terms have order at least \(-1\) at \(Q^\pm\) and no pole elsewhere. The residue of \(\eta\) is \(M(-r)+rM=0\) at \(Q^+\) and \(Mr+r(-M)=0\) at \(Q^-\). A differential of order at least \(-1\) with residue \(0\) has order at least \(0\).

*So \(\eta=c\,\omega\) with \(c\in k\)* (Corollary 5.3 of the lesson on points). Dividing by \(\omega\) and taking values at \(O\), where \(1/(1-\lambda w)\) has the value \(1\):
\[
c=M+r\Psi .
\]

*Apply \(\mathcal C\).* By Theorem 4.1 of the lesson on the Cartier operator, \(\mathcal C(M\theta_\lambda)=M\,\mathcal C(\theta_\lambda)\), because \(M=M^p\) in \(\mathbb F_p\); and \(\mathcal C(r\,dF/F)=r^{1/p}\,dF/F\), \(\mathcal C(c\,\omega)=c^{1/p}H\omega\). So
\[
Mu_\lambda\,\omega+r^{1/p}\,\frac{dF}F=c^{1/p}H\,\omega .
\]
Dividing by \(\omega\) and taking values at \(O\):
\[
Mu_\lambda(O)+r^{1/p}\Psi=c^{1/p}H .
\]
The \(p\)-th power of this equation is
\[
MS_f(\lambda)+r\Psi^p=cH=(M+r\Psi)H ,
\]
which is the assertion. \(\blacksquare\)

**Example 3.2.** Let \(p=7\) and \(f=1+w^2+3w^3\). In \(\mathbb F_7[w]\),
\[
\begin{aligned}
f^3={}&1+3w^2+2w^3+3w^4+4w^5\\
&+2w^7+6w^8+6w^9 ,
\end{aligned}
\]
so \(H=0\). Take \(\mu=2\), \(\lambda=4\). Then \(d=f(2)=1\), \(v_0=1\), \(Q^\pm=(2,\pm1)\) and \(r=2\). Let
\[
A=5w^2+2w+3,\qquad F=\frac{A+v}{(w-2)^2}.
\]
One checks \(A^2-f=4(w-2)^4\) and \(A(2)=-1\). So \((A+v)(A-v)\) has order \(4\) at each of \(Q^+,Q^-\) and no other zero at affine points; \(A+v\) vanishes at \(Q^+\) and not at \(Q^-\). Hence \(A+v\) has order \(4\) at \(Q^+\) and \(0\) at all other affine points. At the point \(\infty\) its order is \(-4\), that of \(w^2\). Since \(w-2\) has order \(1\) at \(Q^\pm\) and \(-2\) at \(\infty\), \(F\) has divisor \(2(Q^+)-2(Q^-)\): here \(M=2\).

With \(D(v)=f'/(2v)\),
\[
\frac{D(F)}F=\frac{A'+f'/(2v)}{A+v}-\frac2{w-2},
\]
and at \(O\), where \(w=0\) and \(v=1\): \(\Psi=2/4+1=5\). Theorem 3.1 gives \(2S_f(4)=2\cdot(0-5^7)\). Since \(5^7=5\) in \(\mathbb F_7\), \(2S_f(4)=-10=4\) and \(S_f(4)=2\). Directly: \(S_f(4)=T_f(2)\), which is \(1+12+16+48+128=205\), and \(205=2\) in \(\mathbb F_7\).

## 4. Frobenius

For \(A\in k(w)\) let \(A^\sigma\) be the rational function obtained by raising all coefficients to the \(p\)-th power. Since \(f\) has coefficients in \(\mathbb F_p\), the map
\[
\sigma\colon K\to K,\qquad\sigma(A+Bv)=A^\sigma+B^\sigma v
\]
is an automorphism of the field \(K\). It is the \(p\)-th power map on \(k\) and fixes \(w\) and \(v\). For a Laurent series \(\ell=\sum_nb_nz^n\) let \(\ell^\sigma=\sum_nb_n^pz^n\). For a point \(P\) let \(\sigma(P)\) be the point \((a^p,b^p)\) if \(P=(a,b)\) is affine; at infinity, \(\sigma(\infty)=\infty\) for a cubic, and for a quartic \(\sigma\) maps the point with \(t=c\) to the point with \(t=c^p\), where \(c^2=f_4\).

**Lemma 4.1.** For every point \(P\) and every function \(g\):

1. \(\iota_{\sigma(P)}(\sigma(g))=\iota_P(g)^\sigma\);
2. \(\operatorname{ord}_{\sigma(P)}(\sigma(g))=\operatorname{ord}_P(g)\) for \(g\ne0\), and if \(g\) is regular at \(P\), then \(\sigma(g)\) is regular at \(\sigma(P)\) with value \(g(P)^p\);
3. \(D(\sigma(g))=\sigma(D(g))\).

**Proof.** (1) Both sides are homomorphisms of rings \(K\to k((z))\) as functions of \(g\), and both are the \(p\)-th power map on \(k\). So it suffices to see that they agree on \(w\) and \(v\), that is, \(w_{\sigma(P)}=w_P^\sigma\) and \(v_{\sigma(P)}=v_P^\sigma\) for the series of the lesson on points. These series were defined by conditions that determine them: a square root with a given constant term, or the series \(\varphi\) with \(f(a+\varphi(y))=y\) or \(f^*(\varphi(y))=y\). Applying \(\sigma\) to the coefficients turns the conditions for \(P\) into those for \(\sigma(P)\), because \(f\) and \(f^*\) have coefficients in \(\mathbb F_p\). For an ordinary point \((a,b)\), for instance, \(w_P^\sigma=a^p+z\), and \(v_P^\sigma\) is a square root of \(f(a^p+z)\) with constant term \(b^p\).

(2) follows from (1). (3) The map \(\sigma^{-1}\circ D\circ\sigma\) is additive, satisfies the product rule, vanishes on \(k\) and maps \(w\) to \(1\). Such a map is determined on \(k(w)\), and then on \(v\) by \(2v\,\delta(v)=\delta(f)\); so it is \(D\). \(\blacksquare\)

From here on \(\lambda\in\mathbb F_p\). Then \(\mu\) and \(d=f(\mu)\) lie in \(\mathbb F_p\). Let \(\chi=d^h\in\{1,-1\}\), the quadratic character of \(d\). Then
\[
v_0^p=v_0\,(v_0^2)^h=\chi v_0,\qquad r^p=\chi r .
\]
So \(\sigma(Q^+)=Q^+\) and \(\sigma(Q^-)=Q^-\) if \(\chi=1\), and \(\sigma\) exchanges \(Q^+\) and \(Q^-\) if \(\chi=-1\). Also \(\sigma(O)=O\).

**Proposition 4.2.** Let \(\lambda\in\mathbb F_p\), \(\lambda\ne0\), \(f(1/\lambda)\ne0\), and let \(F\) have divisor \(M(Q^+)-M(Q^-)\). Then
\[
\Psi^p=\chi\Psi .
\]
The product \(r\Psi\) lies in \(\mathbb F_p\), and it does not change when \(v_0\) is replaced by \(-v_0\).

**Proof.** By Lemma 4.1(2), \(\sigma(F)\) has order \(M\) at \(\sigma(Q^+)\), order \(-M\) at \(\sigma(Q^-)\) and order \(0\) elsewhere. If \(\chi=1\), these are the orders of \(F\); if \(\chi=-1\), those of \(1/F\). By Corollary 4.3 of the lesson on points, \(\sigma(F)\) is a constant times \(F^\chi\). So \(D(\sigma F)/\sigma F=\chi D(F)/F\), and with Lemma 4.1(3),
\[
\sigma\Bigl(\frac{v\,D(F)}F\Bigr)=\chi\,\frac{v\,D(F)}F .
\]
Taking values at \(O=\sigma(O)\) gives \(\Psi^p=\chi\Psi\), by Lemma 4.1(2). Hence \((r\Psi)^p=\chi r\cdot\chi\Psi=r\Psi\), so \(r\Psi\in\mathbb F_p\). Replacing \(v_0\) by \(-v_0\) exchanges \(Q^+\) and \(Q^-\); then \(1/F\) has the required divisor, and both \(r\) and \(\Psi\) change sign. \(\blacksquare\)

## 5. Arguments in the prime field

**Theorem 5.1.** Let \(\lambda\in\mathbb F_p\), \(\lambda\ne0\), with \(d=f(1/\lambda)\ne0\), and let \(\chi\) be the quadratic character of \(d\). Let \(M\ge1\), and let \(F\) be a function with divisor \(M(Q^+)-M(Q^-)\). Then, in \(\mathbb F_p\),
\[
M\,(S_f(\lambda)-H)=(H-\chi)\,r\,\Psi .
\]

1. If \(p\) does not divide \(M\), then
\[
S_f(\lambda)=H+\frac{(H-\chi)\,r\,\Psi}M .
\]
2. If \(M\equiv1-\chi H\pmod p\) and \(H\ne\chi\), then
\[
S_f(\lambda)=H-\chi\,r\,\Psi .
\]

**Proof.** By Theorem 3.1 and Proposition 4.2, \(M(S_f(\lambda)-H)=r(H\Psi-\chi\Psi)\). (1) is the division by \(M\). (2) Since \(\chi^2=1\), \(1-\chi H=-\chi(H-\chi)\). So \(-\chi(H-\chi)(S_f(\lambda)-H)=(H-\chi)r\Psi\), and division by \(H-\chi\ne0\) and multiplication by \(-\chi\) give the formula. \(\blacksquare\)

In Example 3.2, \(\chi=1\), \(H=0\), \(M=2\), \(r\Psi=10=3\): part (1) gives \(S_f(4)=-3/2=2\).

*The integer \(M\) of [Jordan].* Let \(\tau\) be the trace of the curve, so that \(H=\tau\) in \(\mathbb F_p\) (Theorem 3.1 of the lesson on truncated powers), and let \(M_\chi=p+1-\chi\tau\). Then \(M_\chi\equiv1-\chi H\) modulo \(p\), and part (2) reads
\[
S_f(\lambda)=H-\chi\,r\,\Psi_{M_\chi}\qquad(H\ne\chi),
\]
where \(\Psi_{M_\chi}\) is formed with a function of divisor \(M_\chi(Q^+)-M_\chi(Q^-)\). The number \(M_1=p+1-\tau\) is the number of points of the curve over \(\mathbb F_p\), and \(M_{-1}=p+1+\tau\) is the number of points of the curve \(nv^2=f(w)\) for a non-square \(n\) (count as in the lesson on truncated powers, with \(\varepsilon(f(w)/n)=-\varepsilon(f(w))\)). That a function with divisor \(M_\chi(Q^+)-M_\chi(Q^-)\) exists follows from the group structure on the points of a curve of genus one; this is not proved in this course. Under that statement, part (2) is the theorem of [Jordan] for \(H\ne\chi\).

*The case \(H=\chi\).* Then \(M_\chi\) is divisible by \(p\), the identity of Theorem 5.1 reads \(0=0\), and it says nothing about \(S_f(\lambda)\). The formula \(S_f(\lambda)=H-\chi r\Psi\) is asserted in [Jordan] in this case as well; its proof there uses further tools and is not covered here.

## 6. Exercises

**6.1.** Let \(F\) have divisor \(M(Q^+)-M(Q^-)\) with \(p\) dividing \(M\). Show without Theorem 3.1 that \(dF/F=\Psi\,\omega\) and \(H\Psi=\Psi^p\).

**6.2.** Let \(F\) have divisor \(M(Q^+)-M(Q^-)\) and let \(j\ge1\). Show that \(F^j\) has divisor \(jM(Q^+)-jM(Q^-)\), that the number \(\Psi\) formed with \(F^j\) is \(j\Psi\), and that Theorem 3.1 for \(F^j\) is \(j\) times Theorem 3.1 for \(F\).

**6.3.** In Example 3.2 take \(\mu=4\), \(\lambda=2\). Here \(d=6\) is not a square in \(\mathbb F_7\). Let \(s\in k\) with \(s^2=3\), so that \(v_0=3s\) satisfies \(v_0^2=6\). Let \(A=s(w-2)^2\) and \(F=(A+v)/(w-4)^2\). Check that \(A^2-f=3(w-4)^4\) and \(A(4)=-v_0\), compute \(\Psi\) and \(r\Psi\), and verify Theorem 5.1 with \(S_f(2)=T_f(4)=1\).

## 7. Solutions

**6.1.** By Proposition 5.4 of the lesson on points, the residues \(\pm M\) of \(dF/F\) are zero in \(k\), so \(dF/F\) has no pole and is \(c\,\omega\); the value at \(O\) gives \(c=\Psi\). Applying \(\mathcal C\): \(\Psi\,\omega=\mathcal C(\Psi\,\omega)=\Psi^{1/p}H\,\omega\). So \(\Psi=\Psi^{1/p}H\), and the \(p\)-th power is \(\Psi^p=\Psi H\).

**6.2.** Orders add under multiplication, and \(d(F^j)/F^j=j\,dF/F\). In Theorem 3.1 for \(F^j\) the left side is \(jM(S_f(\lambda)-H)\) and the right side is \(r(Hj\Psi-(j\Psi)^p)=j\,r(H\Psi-\Psi^p)\), because \(j^p=j\) in \(\mathbb F_p\).

**6.3.** \(A^2-f=3(w-2)^4-f\). Expanding, \(3(w-2)^4=3w^4+4w^3+2w^2+2w+6\) in \(\mathbb F_7[w]\), so \(A^2-f=3w^4+w^3+w^2+2w+5\), and \(3(w-4)^4=3w^4+w^3+w^2+2w+5\) as well. \(A(4)=4s=-3s=-v_0\). As in Example 3.2, \(F\) has divisor \(2(Q^+)-2(Q^-)\) with \(Q^\pm=(4,\pm3s)\). Here \(A=s(w^2+3w+4)\), so \(A(0)=4s\), \(A'(0)=3s\), \(f'(0)=0\), and
\[
\Psi=\frac{3s}{4s+1}+\frac24=(3+5s)+4=5s ,
\]
using \(1/(1+4s)=4+5s\); this holds because \((1+4s)(4+5s)\) is \(4+21s+20s^2\), and \(4+60+21s=1\) in \(k\). Further \(r=\mu/v_0=4/(3s)=2s\), since \(3s\cdot2s=18=4\). So \(r\Psi=10s^2=30=2\). With \(\chi=-1\), \(H=0\), \(M=2\): \((H-\chi)r\Psi=2=M(S_f(2)-H)\).

## References

- [Jordan] D. Jordan, *Cartier–Miller evaluation of genus-one coefficient sums*, manuscript, revised 5 October 2026, Theorem 1 and Proposition 2. https://github.com/bbrhuft/Cartier-Miller-evaluation-of-genus-one-coefficient-sums
