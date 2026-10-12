# Positivity on the half-gaps

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

[Quotients on the half-gaps](quotients-on-the-half-gaps.md) reduces the two sign conditions on the interval \([0,89.5]\) to the following: for each of the \(91\) half-gaps, for \(i=1,2\), and for every \(k\ge2.36\), the polynomial \(\Phi_i(x;k)\) of degree \(40\) is at least \(0.001\) for \(0\le x\le1\). This lesson proves it. The coefficients of \(\Phi_i\) depend on \(k\), which runs through an unbounded interval, and on \(x\). Both dependences are removed by exact inequalities, and what remains is a finite list of \(37310\) inequalities between explicitly defined numbers.

- A linear expression in the ten numbers \(q(k)\) is bounded below, for all \(k\) between two consecutive endpoints, by its smallest value at the corners of a box that contains the curve \(q(k)\) (Lemma 1.1).
- A polynomial on \([0,1]\) is at least the smallest of its Bernstein coefficients (Lemma 2.1).
- The resulting lower bounds for the Bernstein coefficients of \(\Phi_i\) are all larger than \(0.001\) (Proposition 3.1). This is established by a computation with rigorous error bounds, and Section 4 prints the program.
- Hence \(T_k-H_1\ge0\) and \(H_2\ge0\) on \([0,89.5]\) for every \(k\ge2.36\) (Theorem 3.2).

The lesson follows [OpenAI-T, Section 3, the parts on parameter boxes and polynomial rows and the first set of inequalities of the finite certificate, and Section 5, the lemma on the signs on the half-gaps].

## 1. Parameter boxes

Recall the column \(q(k)\) of the lesson on the reference lists: with \(n_1,\dots,n_5=1,3,4,7,9\) and \(v_j=e^{-k(n_j-1)}\), its entries are \(v_1,\dots,v_5,v_1/k,\dots,v_5/k\), and \(v_1=1\). A *row* is a list \(l=(a_1,\dots,a_5,b_1,\dots,b_5)\) of ten real numbers, and
\[
\begin{aligned}
l\,q(k)={}&a_1+\frac{b_1}k\\
&+\sum_{j=2}^5\Bigl(a_j+\frac{b_j}k\Bigr)e^{-k(n_j-1)} .
\end{aligned}
\]
The *endpoints* are \(2.36\), \(2.65\), \(3.2\), \(4\), \(6\), \(\infty\). For consecutive endpoints \(K<J\) and a real number \(x\) let
\[
\begin{gathered}
G_l(x)=a_1+b_1x+\sum_{j=2}^5\mu_j(x),\\
\mu_j(x)=\min_{H=K,\,J}\ (a_j+b_jx)\,e^{-H(n_j-1)},
\end{gathered}
\]
and
\[
[l]_{K,J}=\min\bigl(G_l(1/K),\ G_l(1/J)\bigr).
\]
For \(J=\infty\) the conventions are \(1/J=0\) and \(e^{-J(n_j-1)}=0\).

**Lemma 1.1.** Let \(K<J\) be consecutive endpoints and \(K\le k\le J\), or \(k\ge K\) if \(J=\infty\). Then for every row \(l\)
\[
l\,q(k)\ge[l]_{K,J} .
\]

**Proof.** Let \(x=1/k\) and \(w_j=e^{-k(n_j-1)}\) for \(2\le j\le5\). Then \(x\) lies between \(1/J\) and \(1/K\), and \(w_j\) lies between \(e^{-J(n_j-1)}\) and \(e^{-K(n_j-1)}\). For a fixed number \(\alpha\), the product \(\alpha w\) on an interval of values \(w\) is smallest at one of the two ends. With \(\alpha=a_j+b_jx\) this gives \((a_j+b_jx)w_j\ge\mu_j(x)\), so \(l\,q(k)\ge G_l(x)\).

Each \(\mu_j\) is the minimum of two functions of \(x\) of the form \(\alpha+\beta x\), hence a concave function, and \(G_l\) is a sum of such functions and of \(a_1+b_1x\), hence concave. A concave function on an interval is at least the smaller of its values at the two ends. So \(G_l(x)\ge[l]_{K,J}\). \(\blacksquare\)

The curve \(k\mapsto q(k)\) is enclosed in a box of the variables \(x,w_2,\dots,w_5\), and the lower bound is taken over the whole box. The bound is exact arithmetic with finitely many numbers; no values of \(k\) are sampled.

## 2. Bernstein coefficients

For \(0\le d\le40\) let
\[
B_d(x)=\binom{40}d\,x^d\,(1-x)^{40-d}.
\]
On \([0,1]\) these polynomials are nonnegative, and \(\sum_dB_d(x)=(x+(1-x))^{40}=1\).

**Lemma 2.1.** Let \(\Phi(x)=\sum_{r=0}^{40}c_rx^r\). Then
\[
\begin{gathered}
\Phi(x)=\sum_{d=0}^{40}\widehat c_d\,B_d(x),\\
\widehat c_d=\sum_{r=0}^d\omega_{dr}\,c_r,\\
\omega_{dr}=\binom dr\Big/\binom{40}r .
\end{gathered}
\]
Consequently \(\Phi(x)\ge\min_d\widehat c_d\) for \(0\le x\le1\).

**Proof.** For \(0\le r\le40\),
\[
\begin{aligned}
x^r&=x^r\,(x+(1-x))^{40-r}\\
&=\sum_{d=r}^{40}\binom{40-r}{d-r}\,x^d\,(1-x)^{40-d}.
\end{aligned}
\]
Both \(\binom{40}d\binom dr\) and \(\binom{40}r\binom{40-r}{d-r}\) are equal to \(\tfrac{40!}{r!\,(d-r)!\,(40-d)!}\). So \(\binom{40-r}{d-r}=\omega_{dr}\binom{40}d\), and \(x^r=\sum_{d\ge r}\omega_{dr}B_d(x)\). Inserting this into \(\Phi\) and collecting the terms with \(B_d\) gives the formula. The last statement holds because \(\Phi(x)\) is an average of the numbers \(\widehat c_d\) with the weights \(B_d(x)\). \(\blacksquare\)

The numbers \(\widehat c_d\) are the *Bernstein coefficients* of \(\Phi\) of degree \(40\). They depend linearly on the coefficients \(c_r\).

## 3. The inequalities

Fix a half-gap, with centre \(m\) and number \(y\), an index \(i\in\{1,2\}\), and consecutive endpoints \(K<J\). Recall from the lesson on the quotients the rows \(l_{i,r}\), the numbers \(a_r^*\), and
\[
\Phi_i(x;k)=\sum_{r=0}^{40}\bigl(l_{i,r}\,q(k)+\delta_i\,a_r^*\bigr)\,x^r,
\]
with \(\delta_1=1\), \(\delta_2=0\). Define for \(0\le d\le40\) the rows
\[
L_{i,d}=\sum_{r=0}^d\omega_{dr}\,l_{i,r} .
\]
By Lemma 2.1 the Bernstein coefficients of \(\Phi_i(\,\cdot\,;k)\) are
\[
L_{i,d}\,q(k)+\delta_i\sum_{r=0}^d\omega_{dr}\,a_r^* .
\]

**Proposition 3.1.** For each of the \(91\) half-gaps, for \(i=1,2\), for each of the five pairs of consecutive endpoints \(K<J\), and for \(0\le d\le40\),
\[
[L_{i,d}]_{K,J}+\delta_i\sum_{r=0}^d\omega_{dr}\,a_r^*>0.001 .
\]

**Verification.** These are \(91\cdot2\cdot5\cdot41=37310\) inequalities. The left side of each is a finite expression in rational numbers, \(\pi\), \(\sqrt3\), and values of the exponential function and of sine and cosine: the rows \(l_{i,r}\) are obtained from the matrices \(X_1,X_2\) of the lesson on the reference lists and from the quadrature forms of scaled derivatives, the numbers \(\omega_{dr}\) are rational, and the brackets \([\,\cdot\,]_{K,J}\) are minima of finitely many such expressions. As for the norms in the lesson on the reference lists, the inequalities were established by a computation in ball arithmetic with \(256\) binary digits, in which an inequality is accepted only if it holds for all numbers of the intervals concerned. All \(37310\) inequalities hold. The smallest values of the left side, rounded downwards, are:

- for \(K=2.36\): \(0.3378\) at the centre \(0\), \(0.02046\) at the centre \(1\), \(0.003472\) at the centres \(3\) and \(4\), \(0.001206\) at the centres from \(7\) to \(88\);
- for \(K=2.65\): \(0.3487\), \(0.01815\), \(0.003882\), \(0.001932\);
- for \(K=3.2\): \(0.3629\), \(0.03408\), \(0.006369\), \(0.002715\);
- for \(K=4\): \(0.3768\), \(0.03754\), \(0.008766\), \(0.003295\);
- for \(K=6\): \(0.3955\), \(0.01200\), \(0.01076\), \(0.003956\).

The smallest value of all, \(0.001206\), occurs for \(K=2.36\) on the half-gap from \(15\) towards \(16\), for \(i=2\) and \(d=40\). Section 4 prints a program for this computation. \(\blacksquare\)

**Theorem 3.2.** Let \(k\ge2.36\), and let \(H_1,H_2\) be the functions of Corollary 3.2 of the lesson on exact interpolation. Then
\[
H_1(s)\le T_k(s),\qquad H_2(s)\ge0
\]
for all \(s\) with \(0\le s\le89.5\).

**Proof.** Choose consecutive endpoints \(K<J\) with \(K\le k\le J\), or \(k\ge K=6\) if \(k\ge6\). Fix a half-gap and \(i\). By Lemma 1.1, \(L_{i,d}\,q(k)\ge[L_{i,d}]_{K,J}\). So by Proposition 3.1 every Bernstein coefficient of \(\Phi_i(\,\cdot\,;k)\) is larger than \(0.001\), and by Lemma 2.1, \(\Phi_i(x;k)>0.001\) for \(0\le x\le1\). This holds for all half-gaps and both \(i\). By Theorem 3.1 of the lesson on the quotients, \(F_1=T_k-H_1\) and \(F_2=H_2\) are nonnegative on \([0,89.5]\). \(\blacksquare\)

On each half-gap the quotient \(\mathcal D_mF_i\) is in fact larger than \(0.001-0.000112>0.0008\). So \(T_k-H_1\) and \(H_2\) vanish on \([0,89.5]\) only at the nodes, and there exactly to second order.

## 4. The program

The following lines continue the program printed in [The reference lists](the-reference-lists.md), Section 5: they are to be appended to it, and they use its arrays `W`, `X1`, `X2`, `t`, `lam`, `z` and its function `dec`. For each half-gap the arrays `Fm` and `Gm` contain, for the orders \(a=\nu,\dots,\nu+40\), the factors \(e^{i\pi tm}(i\pi yt)^a/a!\) and \(\lambda(t)e^{i\pi z(t)m}(i\pi yz(t))^a/a!\) at all frequency points. The rows \(l_{i,r}\) are then the real parts of the products with the weights of the columns of \(X_i\) and of the other matrix, multiplied by \(\sigma_iy^{-\nu}\). The function `box_low` computes the bracket \([\,\cdot\,]_{K,J}\), and `support` the numbers \(a_r^*\).

```
# Continuation of the program for the reference lists: the Bernstein
# coefficients of the polynomials on the 91 half-gaps, bounded below
# on the five parameter intervals.
from math import comb

WX = [W * acb_mat(X1), W * acb_mat(X2)]
N0 = [n for n in range(200) if n % 12 in RES]
gaps = []
for i, m in enumerate(N0):
    if m <= 88:
        gaps.append((m, N0[i + 1]))
        if m > 0:
            gaps.append((m, N0[i - 1]))
omega = [[arb(fmpq(comb(d, r), comb(40, r))) for r in range(d + 1)]
         for d in range(41)]
ENDS = ["2.36", "2.65", "3.2", "4", "6", None]
FIVE = [1, 3, 4, 7, 9]
EXP = {(H, j): (-dec(H) * (FIVE[j] - 1)).exp()
       for H in ENDS[:5] for j in range(5)}


def box_low(row, K, J):
    # the number [row]_{K,J}, a lower bound for row.q(k) on K <= k <= J
    best = None
    for x in (1 / dec(K), 1 / dec(J) if J else arb(0)):
        val = row[0] + x * row[5]
        for j in range(1, 5):
            c = row[j] + x * row[5 + j]
            val += (c * EXP[K, j]).min(c * EXP[J, j] if J else arb(0))
        best = val if best is None else best.min(val)
    return best


def support(m, y, K, J):
    # the numbers a*_r, r = 0 to 40, of the lower support of the target
    K = dec(K)
    if m == 0:
        return [K.exp() / K * (-K * y) ** r / arb(r).fac()
                for r in range(41)]
    if m == 1:
        return [K * (-K * y) ** r / arb(r + 2).fac() for r in range(41)]
    a = [arb(0)] * 41
    if m == 3 and J:
        a[0] = dec(J) / 2 * (-13 * dec(J) / 6).exp()
    return a


smallest, count, R = {}, 0, range(len(t))
for m, m2 in gaps:
    y, nu = arb(fmpq(m2 - m, 2)), (0 if m == 0 else 2)
    f = [(I * PI * t[r] * m).exp() for r in R]
    g = [lam[r] * (I * PI * z[r] * m).exp() for r in R]
    Fm, Gm = acb_mat(41, len(t)), acb_mat(41, len(t))
    for a in range(nu + 41):
        if a > 0:
            f = [f[r] * I * PI * y * t[r] / a for r in R]
            g = [g[r] * I * PI * y * z[r] / a for r in R]
        if a >= nu:
            for r in R:
                Fm[a - nu, r], Gm[a - nu, r] = f[r], g[r]
    for i in (0, 1):
        sign = (-1 if i == 0 else 1) / y ** nu
        rows = (Fm * WX[i] + Gm * WX[1 - i]).real
        L = [[sign * sum((omega[d][r] * rows[r, c] for r in range(d + 1)),
                         arb(0)) for c in range(10)] for d in range(41)]
        for K, J in zip(ENDS, ENDS[1:]):
            a = support(m, y, K, J) if i == 0 else [arb(0)] * 41
            for d in range(41):
                v = box_low(L[d], K, J) + sum(
                    (omega[d][r] * a[r] for r in range(d + 1)), arb(0))
                assert v > dec("0.001")
                count += 1
                group = [0, 1, 2, 2, 2][m] if m < 5 else 3
                key = (K, group)
                smallest[key] = min(smallest.get(key, 9.0), float(v.mid()))
print(count, "inequalities hold")
for K in ENDS[:5]:
    print(K, [round(smallest[key], 6) for key in sorted(smallest)
              if key[0] == K])
```

The statement `assert` stops the program if one of the inequalities is not certain. The program prints the number of inequalities, \(37310\), and for each \(K\) the four smallest values listed in Section 3. Together with the first part it runs for about two minutes.

## 5. Exercises

**5.1.** Compute the Bernstein coefficients of degree \(2\) of \(\Phi(x)=1-3x+3x^2\), with \(B_d(x)=\binom2dx^d(1-x)^{2-d}\) and \(\omega_{dr}=\binom dr/\binom2r\). What does Lemma 2.1 give, and what is the true minimum of \(\Phi\) on \([0,1]\)?

**5.2.** Let \(l=(0,1,0,0,0,\ 0,0,0,0,0)\), so that \(l\,q(k)=e^{-2k}\). Compute \([l]_{K,J}\) for \(K=2.36\), \(J=2.65\), and compare with the smallest value of \(l\,q(k)\) on \(K\le k\le J\).

**5.3.** Let \(l=(0,0,0,0,0,\ 0,1,0,0,0)\), so that \(l\,q(k)=e^{-2k}/k\). Compute \([l]_{K,J}\) for the same \(K,J\), and compare with the smallest value of \(l\,q(k)\).

**5.4.** Why is it not enough, for Theorem 3.2, to check \(\Phi_i(x;k)>0.001\) at many values of \(x\) and \(k\)?

## 6. Solutions

**5.1.** \(c_0=1\), \(c_1=-3\), \(c_2=3\). The numbers \(\omega_{dr}\) are \(\omega_{00}=\omega_{10}=\omega_{20}=1\), \(\omega_{11}=\tfrac12\), \(\omega_{21}=1\), \(\omega_{22}=1\). So \(\widehat c_0=1\), \(\widehat c_1=1-\tfrac32=-\tfrac12\), \(\widehat c_2=1-3+3=1\). Lemma 2.1 gives \(\Phi\ge-\tfrac12\) on \([0,1]\). The true minimum is \(\Phi(\tfrac12)=\tfrac14\). The bound by Bernstein coefficients is valid but not sharp; it becomes sharper when the degree is raised or the interval is divided.

**5.2.** Only \(a_2=1\) is different from zero, and \(n_2-1=2\). So \(\mu_2(x)=\min(e^{-2K},e^{-2J})=e^{-5.3}\) for every \(x\), and \([l]_{K,J}=e^{-5.3}\), about \(0.00499\). This is the smallest value of \(e^{-2k}\) on the interval, attained at \(k=J\).

**5.3.** Now \(b_2=1\), so \(\mu_2(x)=x\,e^{-5.3}\) for \(x>0\), and \(G_l(x)=x\,e^{-5.3}\). The smaller value at the two ends is \(G_l(1/J)=e^{-5.3}/2.65\), about \(0.00188\). This is again the smallest value of \(e^{-2k}/k\), attained at \(k=J\). In general the bracket can be smaller than the true minimum, because the box contains points that are not on the curve \(q(k)\), for example the corner with \(x=1/K\) and \(w_2=e^{-2J}\).

**5.4.** A polynomial that is positive at many points can be negative between them, and likewise in \(k\). Finitely many evaluations prove nothing about the other points unless they are combined with a bound on the variation. Lemma 2.1 and Lemma 1.1 are such bounds, in a form that needs only finitely many numbers: the Bernstein coefficients control all \(x\) in \([0,1]\), and the boxes control all \(k\) of a parameter interval, including the unbounded interval \(k\ge6\).

## References

- [OpenAI-T] OpenAI, *Universal optimality of the triangular lattice*, OpenAI Math Release preprint, 23 September 2026, Sections 3 and 5. https://github.com/openai/math/tree/main/preprints/Universal-optimality-of-the-triangular-lattice-September-23-2026
