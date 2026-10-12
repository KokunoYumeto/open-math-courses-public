# The reference lists

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The interpolation system of [Gaussian damping and Fourier pairs](gaussian-damping-and-fourier-pairs.md) is a linear system with infinitely many unknowns, the entries of two coefficient lists. This lesson constructs, for every parameter \(k\), two explicit lists with finitely many nonzero entries that solve the system up to a very small error: the *reference lists*. They are obtained from a matrix with \(168\) rows by finitely many matrix operations. A later step of the proof corrects them to an exact solution.

- On lists that vanish beyond the node \(168\), the jet operator is a matrix. Replacing the spectral integrals by the quadrature rule changes its entries by less than \(2\cdot10^{-31}\) (Lemma 1.1).
- The target of the interpolation system is described by ten numbers depending on \(k\), and the six extra entries of the two lists are fixed as explicit functions of \(k\) (Section 2).
- The reference lists are given by two matrices \(X_1,X_2\) with ten columns. They solve a finite form of the system up to a term that contains the power \(\mathbf D^{512}\) of the matrix (Lemma 3.1).
- The sizes of the matrices are bounded: \(\|\mathbf D^{64}\|<0.004\), and the reference lists have total size less than \(4.8\) for \(k\ge2.36\) (Proposition 4.1, Corollary 4.2).

Proposition 4.1 is a statement about finitely many explicitly defined numbers. It is established by a computation with rigorous error bounds. Section 5 describes the computation and prints the program, so that it can be repeated.

The lesson follows [OpenAI-T, Section 3, the parts on the transformed jets, the target data and the finite reference columns, and the bounds for norms in the finite certificate].

## 1. Finite lists and the matrix of the jet operator

Let \(M=168\) and let \(\mathcal F\) be the set of the nodes \(n\in\mathcal N\) with \(n\le M\). Each of the fourteen blocks of twelve consecutive integers from \(1\) to \(168\) contains six nodes, so \(\mathcal F\) has \(84\) elements. A *finite list* is a coefficient list with \(c_n=d_n=0\) for \(n>M\). It has \(171\) entries, which we order as follows: first the \(c_n\) for \(n\in\mathcal F\) in increasing order, then the \(d_n\) for \(n\in\mathcal F\), then the extra entries \(c_0,d_0,C\). The first \(168\) entries are the positive part.

For a vector \(v\) let \(\|v\|_1\) be the sum of the absolute values of its entries. For a matrix \(A\) with columns \(A_j\) let \(\|A\|\) be the largest of the numbers \(\|A_j\|_1\). Then \(\|Av\|_1\le\|A\|\,\|v\|_1\) and \(\|AB\|\le\|A\|\,\|B\|\) (Exercise 6.1).

For each of the \(171\) entries \(\kappa\) let \(K_\kappa\) be the transformed function of the list in which the entry \(\kappa\) is \(1\) and all other entries are \(0\). Let \(S_{\mathcal F}\) be the matrix with \(171\) columns and \(168\) rows, the rows indexed like a positive part by \((c,n)\) and \((d,n)\) with \(n\in\mathcal F\), and with the entries
\[
\begin{gathered}
(S_{\mathcal F})_{(c,n),\kappa}=-\frac{K_\kappa(n)}{Q_n},\\
(S_{\mathcal F})_{(d,n),\kappa}=-\frac{K_\kappa'(n)-D_nK_\kappa(n)}{Q_n}.
\end{gathered}
\]
By the definition of the jet operator \(S\) and by linearity, for a finite list \(\mathbf a\), written as a column of \(171\) numbers, the column \(S_{\mathcal F}\mathbf a\) consists of the entries of \(S\mathbf a\) at the nodes of \(\mathcal F\).

Let \(\widetilde S\) be the matrix obtained when \(K_\kappa(n)\) and \(K_\kappa'(n)\) are replaced by their quadrature forms ([A positive quadrature rule](a-positive-quadrature-rule.md), Section 3, with \(a=0\) and \(a=1\), \(y=1\), \(s=n\)). Its entries are finite sums of explicit terms.

**Lemma 1.1.** Every entry of \(S_{\mathcal F}-\widetilde S\) has absolute value less than \(2\cdot10^{-31}\).

**Proof.** By Theorem 3.3 of the lesson on the quadrature rule, \(K_\kappa(n)\) and \(K_\kappa'(n)\) differ from their quadrature forms by less than \(10^{-31}\). In the row \((c,n)\) the difference is divided by \(Q_n>7/4\). In the row \((d,n)\) the two differences are multiplied by at most \(|D_n|/Q_n\) and \(1/Q_n\), and \((1+|D_n|)/Q_n<3.12/1.75<2\). \(\blacksquare\)

Write \(\widetilde S=(\mathbf D,\widetilde S_e)\), where \(\mathbf D\) consists of the first \(168\) columns and \(\widetilde S_e\) of the last three. The square matrix \(\mathbf D\) describes, up to the quadrature error, how the positive part of a finite list acts through \(S\) on the jets at the nodes of \(\mathcal F\). It is not to be confused with the numbers \(D_n\).

## 2. The target and the extra entries

Let \(n_1,\dots,n_5\) be the first five positive nodes \(1,3,4,7,9\). For \(k>0\) let \(v_j=e^{-k(n_j-1)}\), that is
\[
\begin{gathered}
v_1=1,\quad v_2=e^{-2k},\quad v_3=e^{-3k},\\
v_4=e^{-6k},\quad v_5=e^{-8k},
\end{gathered}
\]
and let \(q(k)\) be the column with the ten entries
\[
v_1,\ \dots,\ v_5,\ \frac{v_1}k,\ \dots,\ \frac{v_5}k .
\]
Since \(T_k(s)=k^{-1}e^{-k(s-1)}\), we have \(T_k(n_j)=v_j/k\) and \(T_k'(n_j)=-v_j\). Let \(Y\) be the matrix with \(168\) rows, indexed like a positive part, and ten columns, whose only nonzero entries are, for \(1\le j\le5\) and \(n=n_j\),
\[
\begin{gathered}
Y_{(d,n),\,j}=-\frac1{Q_n},\\
Y_{(c,n),\,5+j}=\frac1{Q_n},\\
Y_{(d,n),\,5+j}=-\frac{D_n}{Q_n}.
\end{gathered}
\]
Then \(Yq(k)\) has the entries \(T_k(n)/Q_n\) and \((T_k'(n)-D_nT_k(n))/Q_n\) at the five nodes \(n=n_j\), and \(0\) at the other nodes of \(\mathcal F\). So \(Yq(k)\) is the jet list \(\mathcal JT_k\), restricted to \(\mathcal F\), with the entries at the nodes \(n\ge12\) replaced by \(0\). These entries are small, of the order \(e^{-11k}\).

The extra entries of the two lists are chosen as follows. Let \(E_1\) and \(E_2\) be the matrices with three rows, for \(c_0,d_0,C\) in this order, and ten columns, of which only the first and the sixth are different from zero:

- \(E_1\): first column \((0.567,\ 0.250,\ -0.0074)\), sixth column \((-0.976,\ 0.408,\ 0.0115)\);
- \(E_2\): first column \((0,\ -0.209,\ 0.0096)\), sixth column \((1,\ 0.938,\ -0.017)\).

Since the first and sixth entries of \(q(k)\) are \(1\) and \(1/k\), the column \(E_iq(k)\) is the first column plus \(1/k\) times the sixth. These twelve decimal numbers are a choice made in [OpenAI-T]. Nothing has to be proved about how they were found; what matters is that the bounds below, and later the sign conditions, hold for them.

## 3. The reference columns

Suppose two lists are sought whose positive parts vanish beyond \(M\), given by matrices \(A_1,A_2\) with \(168\) rows and ten columns as \(A_1q(k)\) and \(A_2q(k)\), and whose extra entries are \(E_1q(k)\) and \(E_2q(k)\). The interpolation system, restricted to the nodes of \(\mathcal F\), with \(S\) replaced by \(\widetilde S\) and the target by \(Yq(k)\), holds for all \(k\) if
\[
\begin{gathered}
A_1-\mathbf DA_2=g_1,\\
A_2-\mathbf DA_1=g_2,
\end{gathered}
\]
where
\[
g_1=Y+\widetilde S_eE_2,\qquad g_2=\widetilde S_eE_1 .
\]
Each right side contains the extra entries of the other list, because the transformed function in \(H_i\) comes from the other list. Adding and subtracting the two equations gives
\[
\begin{gathered}
(I-\mathbf D)(A_1+A_2)=g_1+g_2,\\
(I+\mathbf D)(A_1-A_2)=g_1-g_2 .
\end{gathered}
\]
In place of the inverses of \(I-\mathbf D\) and \(I+\mathbf D\) we use finite geometric sums. Let
\[
\begin{gathered}
V_+=\sum_{j=0}^{511}\mathbf D^j,\\
V_-=\sum_{j=0}^{511}(-\mathbf D)^j,
\end{gathered}
\]
so that
\[
(I-\mathbf D)V_+=(I+\mathbf D)V_-=I-\mathbf D^{512}.
\]
Define the matrices with \(168\) rows and ten columns
\[
\begin{gathered}
\sigma=V_+(g_1+g_2),\qquad\delta=V_-(g_1-g_2),\\
X_1^+=\tfrac12(\sigma+\delta),\qquad X_2^+=\tfrac12(\sigma-\delta),
\end{gathered}
\]
and let \(X_i\) be the matrix with \(171\) rows that consists of \(X_i^+\) and, below it, the three rows of \(E_i\).

**Lemma 3.1.**
\[
\begin{gathered}
X_1^+-\mathbf DX_2^+=g_1-\mathbf D^{512}g_1,\\
X_2^+-\mathbf DX_1^+=g_2-\mathbf D^{512}g_2 .
\end{gathered}
\]

**Proof.** By the identity for \(V_+\) and \(V_-\),
\[
\begin{gathered}
(I-\mathbf D)\sigma=(I-\mathbf D^{512})(g_1+g_2),\\
(I+\mathbf D)\delta=(I-\mathbf D^{512})(g_1-g_2).
\end{gathered}
\]
Hence
\[
\begin{aligned}
X_1^+-\mathbf DX_2^+&=\tfrac12(I-\mathbf D)\sigma+\tfrac12(I+\mathbf D)\delta\\
&=(I-\mathbf D^{512})g_1,\\
X_2^+-\mathbf DX_1^+&=\tfrac12(I-\mathbf D)\sigma-\tfrac12(I+\mathbf D)\delta\\
&=(I-\mathbf D^{512})g_2 .
\end{aligned}
\]
\(\blacksquare\)

For \(k>0\) the *reference lists* are the finite lists
\[
\ell_1^{\mathrm{ref}}=X_1q(k),\qquad\ell_2^{\mathrm{ref}}=X_2q(k).
\]
Their extra entries are \(E_1q(k)\) and \(E_2q(k)\). By Lemma 3.1 they solve the finite form of the interpolation system up to the columns \(\mathbf D^{512}g_iq(k)\). The matrices \(X_1,X_2\) do not depend on \(k\).

## 4. The sizes of the matrices

**Proposition 4.1.**

1. \(\|\mathbf D^{64}\|<0.004\).
2. \(\|V_+\|+\|V_-\|<36\).
3. For the columns \((X_i)_j\) of \(X_1\) and \(X_2\): \(\|(X_1)_j\|_1+\|(X_2)_j\|_1\) is less than \(2.3\) for \(1\le j\le5\) and less than \(5.6\) for \(6\le j\le10\).

**Verification.** Every entry of \(\mathbf D\), \(\widetilde S_e\), \(Y\), \(E_1\), \(E_2\) is a finite expression in rational numbers, \(\pi\), \(\sqrt3\), and values of the exponential function and of sine and cosine, given by the formulas of this lesson and of the lessons on cardinal functions, Gaussian damping and the quadrature rule. The matrices \(\mathbf D^{64}\), \(V_\pm\), \(X_i\) are obtained from them by finitely many additions and multiplications. So the three statements are inequalities between explicitly defined real numbers.

They were established by a computation in *ball arithmetic*: every real number is represented by a midpoint and a radius such that the number lies in the interval they describe; every arithmetic operation and every evaluation of a function returns an interval that contains the exact result; and an inequality is accepted only if it holds for all numbers of the intervals concerned. The computation used midpoints with \(256\) binary digits. The powers are formed by squaring, \(U_0=\mathbf D\) and \(U_{r+1}=U_r^2\), so that \(U_r=\mathbf D^{2^r}\), and
\[
\begin{gathered}
V_+=\prod_{r=0}^8(I+U_r),\\
V_-=(I-U_0)\prod_{r=1}^8(I+U_r)
\end{gathered}
\]
(Exercise 6.2). The results, with the numbers rounded upwards in the last digit:

- \(\|\mathbf D^{2^r}\|\) for \(r=0,\dots,8\): \(1.7258\), \(2.0769\), \(2.2537\), \(1.7389\), \(0.7391\), \(0.1178\), \(0.002957\), \(1.864\cdot10^{-6}\), \(7.4\cdot10^{-13}\);
- \(\|V_+\|\le32.1015\) and \(\|V_-\|\le1.8438\);
- the sums \(\|(X_1)_j\|_1+\|(X_2)_j\|_1\) for \(j=1,\dots,10\): \(1.8003\), \(2.1656\), \(1.1033\), \(0.1595\), \(0.0785\), \(5.3427\), \(5.1525\), \(2.1923\), \(0.1744\), \(0.0630\).

The inequalities certified by the computation are \(\|\mathbf D^{64}\|<0.0031\), \(\|V_+\|<32.12\), \(\|V_-\|<1.85\), and the bounds \(2.20\) and \(5.40\) for the column sums; they imply the three statements. Section 5 prints a program for this computation. \(\blacksquare\)

The matrix \(\mathbf D\) has norm larger than \(1\), and its powers first grow. So the interpolation system cannot be solved by a simple iteration; but the high powers of \(\mathbf D\) are very small.

**Corollary 4.2.**

1. \(\|\mathbf D^{512}\|<\eta\), where \(\eta=0.004^8<6.6\cdot10^{-20}\).
2. For \(k\ge2.36\), \(\|\ell_1^{\mathrm{ref}}\|_1+\|\ell_2^{\mathrm{ref}}\|_1<4.8\).
3. For \(k\ge2.36\), the entries \(C\) of the two reference lists satisfy \(|C_1|+|C_2|<0.02\).

**Proof.** (1) \(\mathbf D^{512}=(\mathbf D^{64})^8\), and \(0.004^8=65536\cdot10^{-24}\).

(2) The entries of \(q(k)\) are positive, so \(\|X_iq(k)\|_1\le\sum_jq_j(k)\,\|(X_i)_j\|_1\). By Proposition 4.1(3) the sum for \(i=1,2\) is at most
\[
\begin{aligned}
&\Bigl(2.3+\frac{5.6}k\Bigr)\\
&\quad\cdot\bigl(1+e^{-2k}+e^{-3k}+e^{-6k}+e^{-8k}\bigr).
\end{aligned}
\]
This decreases in \(k\). At \(k=2.36\) the first factor is less than \(4.673\), and \(e^{-4.72}<0.009\), \(e^{-7.08}<0.001\), \(e^{-14.16}+e^{-18.88}<10^{-6}\), so the second factor is less than \(1.0101\). The product is less than \(4.73\).

(3) \(C_1=-0.0074+0.0115/k\) and \(C_2=0.0096-0.017/k\). For \(k\ge2.36\), \(0.0115/k<0.0049\) and \(0.017/k<0.0073\). So \(C_1\) is negative with \(|C_1|<0.0074\), and \(C_2\) is positive with \(C_2<0.0096\). \(\blacksquare\)

## 5. The program

The following program in the language Python carries out the computation of Proposition 4.1. It uses the package python-flint, which gives access to the ball arithmetic of the library Arb of F. Johansson. The names follow the lesson. The array `W` contains, for each frequency point `t[r]` and each of the 171 entries, the weight with which the exponential of that frequency occurs in the quadrature form: for the entries \(c_n\) and \(d_n\) it is \(o_v/6\) times twice the value of the density \(m_n''\) or \(m_n'\) at the point \(\tau_{jv}\), and for the entry \(C\) it is \(P_0\) at the frequency \(0\) and \(2P_l\) at the frequencies \(t_l\), \(1\le l\le6\). The quadrature form of \(K_\kappa(n)\) is then the real part of the sum of \(\lambda(t_r)e^{i\pi z(t_r)n}\) times the weights, and for \(K_\kappa'(n)\) each term has the additional factor \(i\pi z(t_r)\).

```
# The matrix D, the sums V+ and V-, and the reference columns X1, X2,
# with rigorous bounds for their norms. Needs python-flint (Arb balls).
from fractions import Fraction
from flint import arb, acb, arb_mat, acb_mat, fmpq, ctx

ctx.prec = 256
PI, I = arb.pi(), acb(0, 1)
b, h, B = arb(3).sqrt() / 2, arb(fmpq(2, 5)), arb(fmpq(4, 3))
RES = [0, 1, 3, 4, 7, 9]
P = [acb(5), acb(arb(-1), 2 * b), acb(arb(1), 2 * b), acb(-2),
     acb(arb(fmpq(-1, 2)), b), acb(arb(-1), -2 * b), acb(1)]


def node_constants(a):
    # Q_n and D_n for a node n congruent to a modulo 12
    Q, D = (PI / 6) ** 2, arb(0)
    for d in RES:
        if d != a:
            x = PI * arb(fmpq(a - d, 12))
            Q, D = Q * (2 * x.sin()) ** 2, D + x.cos() / x.sin()
    return Q, D * PI / 6


QD = {a: node_constants(a) for a in RES}
F = [n for n in range(1, 169) if n % 12 in RES]
col_c = {n: i for i, n in enumerate(F)}
col_d = {n: 84 + i for i, n in enumerate(F)}
col_c[0], col_d[0], COL_C = 168, 169, 170

# the rule with N = 384 points on each of the six frequency intervals
N = 384
theta = [PI * arb(fmpq(2 * v + 1, 2 * N)) for v in range(N)]
o = [(1 - 2 * sum(((2 * a * th).cos() / (4 * a * a - 1)
                   for a in range(1, N // 2)), arb(0))) / N
     for th in theta]
t = [(2 * j - 1 + th.cos()) / 12 for j in range(1, 7) for th in theta]
t += [arb(fmpq(j, 6)) for j in range(7)]
lam = [1 / (b * (h - I * x)) for x in t]
z = [I * B / (h - I * x) - I * h for x in t]

# W[r, c]: weight of the frequency t[r] for the list with entry c equal to 1
W = acb_mat(len(t), 171)
for n in [0] + F:
    pi_l = [P[l] * (I * PI * n * l / 6).exp() for l in range(7)]
    for j in range(1, 7):
        s0 = sum(pi_l[j:], acb(0))
        s1 = sum((pi_l[l] * l / 6 for l in range(j, 7)), acb(0))
        for v in range(N):
            r = (j - 1) * N + v
            e = (-I * PI * t[r] * n).exp() * o[v] / 6
            W[r, col_c[n]] = -2 * PI ** 2 * e * (s1 - t[r] * s0)
            W[r, col_d[n]] = 2 * PI * I * e * s0
for j in range(7):
    W[6 * N + j, COL_C] = (1 if j == 0 else 2) * P[j]

# quadrature forms of K(n) and K'(n) for the 84 nodes and the 171 entries
G0, G1 = acb_mat(84, len(t)), acb_mat(84, len(t))
for i, n in enumerate(F):
    for r in range(len(t)):
        G0[i, r] = lam[r] * (I * PI * z[r] * n).exp()
        G1[i, r] = G0[i, r] * I * PI * z[r]
K0, K1 = (G0 * W).real, (G1 * W).real
S = arb_mat(168, 171)
for i, n in enumerate(F):
    Q, Dn = QD[n % 12]
    for c in range(171):
        S[i, c] = -K0[i, c] / Q
        S[84 + i, c] = (Dn * K0[i, c] - K1[i, c]) / Q


def block(A, rows, cols):
    R = arb_mat(len(rows), len(cols))
    for i, r in enumerate(rows):
        for j, c in enumerate(cols):
            R[i, j] = A[r, c]
    return R


def dec(s):
    # the exact rational number with the decimal expansion s
    f = Fraction(s)
    return arb(fmpq(f.numerator, f.denominator))


def column_sums(A):
    return [sum((abs(A[r, c]) for r in range(A.nrows())), arb(0))
            for c in range(A.ncols())]


def below(A, cut):
    # True only if every column sum is certainly less than cut
    sums = column_sums(A)
    return all(x < dec(cut) for x in sums), max(float(x.mid()) for x in sums)


D = block(S, range(168), range(168))
Se = block(S, range(168), range(168, 171))

# target data and extra entries
E1, E2, Y = arb_mat(3, 10), arb_mat(3, 10), arb_mat(168, 10)
for r in range(3):
    E1[r, 0] = dec(["0.567", "0.250", "-0.0074"][r])
    E1[r, 5] = dec(["-0.976", "0.408", "0.0115"][r])
    E2[r, 0] = dec(["0", "-0.209", "0.0096"][r])
    E2[r, 5] = dec(["1", "0.938", "-0.017"][r])
for j, n in enumerate([1, 3, 4, 7, 9]):
    Q, Dn = QD[n % 12]
    Y[col_d[n], j] = -1 / Q
    Y[col_c[n], j + 5] = 1 / Q
    Y[col_d[n], j + 5] = -Dn / Q
g1, g2 = Y + Se * E2, Se * E1

# powers of D by squaring, V+ and V- by nine multiplications
Id = arb_mat(168, 168)
for i in range(168):
    Id[i, i] = 1
CUTS = [("1.74", "2.74", "2.1"), ("2.09", "6.94", "2.2"),
        ("2.27", "15.32", "2.13"), ("1.75", "25.3", "1.97"),
        ("0.75", "31.1", "1.88"), ("0.12", "32.09", "1.85"),
        ("0.0031", "32.12", "1.85"), ("0.000002", "32.12", "1.85"),
        ("0.000000000001", "32.12", "1.85")]
U, Vp, Vm = D, Id, Id
for r in range(9):
    u = below(U, CUTS[r][0])
    Vp = Vp * (Id + U)
    Vm = Vm * (Id - U if r == 0 else Id + U)
    print(r, u, below(Vp, CUTS[r][1]), below(Vm, CUTS[r][2]))
    U = U * U

# the reference columns; rows 168 to 170 are the extra entries
sm, df = Vp * (g1 + g2), Vm * (g1 - g2)
X1, X2 = arb_mat(171, 10), arb_mat(171, 10)
for c in range(10):
    for r in range(168):
        X1[r, c] = (sm[r, c] + df[r, c]) / 2
        X2[r, c] = (sm[r, c] - df[r, c]) / 2
    for r in range(3):
        X1[168 + r, c], X2[168 + r, c] = E1[r, c], E2[r, c]
both = [x + y for x, y in zip(column_sums(X1), column_sums(X2))]
print(all(x < dec("2.20") for x in both[:5]),
      all(x < dec("5.40") for x in both[5:]),
      [round(float(x.mid()), 4) for x in both])
```

A comparison `x < cut` between two balls is true only if every number of the ball `x` is smaller than every number of the ball `cut`. For \(r=0,\dots,8\) the program prints the result of the comparisons for \(\|U_r\|\), \(\|V_+\|\) and \(\|V_-\|\) after the step \(r\), each with the midpoint of the largest column sum, and in the last line the two comparisons for the column sums of \(X_1\) and \(X_2\) with their ten midpoints. All comparisons give `True`. On a current computer the program runs for about ten seconds.

## 6. Exercises

**6.1.** Show \(\|Av\|_1\le\|A\|\,\|v\|_1\) and \(\|AB\|\le\|A\|\,\|B\|\) for the norms of Section 1.

**6.2.** Let \(\mathbf D\) be a square matrix and \(U_r=\mathbf D^{2^r}\). Prove the two product formulas for \(V_+\) and \(V_-\) of Section 4.

**6.3.** Write the six extra entries of the two reference lists as functions of \(k\), and give their limits for \(k\to\infty\).

**6.4.** Show that for every node \(n\) and every \(k>0\)
\[
\begin{gathered}
\Bigl|\frac{T_k(n)}{Q_n}\Bigr|+\Bigl|\frac{T_k'(n)-D_nT_k(n)}{Q_n}\Bigr|\\
\le\frac{1+3.12/k}{1.75}\,e^{-k(n-1)}.
\end{gathered}
\]

## 7. Solutions

**6.1.** \(Av=\sum_jv_jA_j\), so \(\|Av\|_1\le\sum_j|v_j|\,\|A_j\|_1\le\|A\|\,\|v\|_1\). The columns of \(AB\) are the vectors \(AB_j\), and \(\|AB_j\|_1\le\|A\|\,\|B_j\|_1\le\|A\|\,\|B\|\).

**6.2.** Multiplying out \(\prod_{r=0}^8(I+\mathbf D^{2^r})\) gives the sum of the powers \(\mathbf D^j\), where \(j\) runs through the sums of the subsets of \(\{1,2,4,\dots,256\}\). Every integer \(j\) with \(0\le j\le511\) is such a sum in exactly one way, by its binary expansion. In the same way \(\prod_{r=1}^8(I+\mathbf D^{2^r})\) is the sum of the powers \(\mathbf D^{2i}\) with \(0\le i\le255\). Multiplying by \(I-\mathbf D\) gives
\[
\sum_{i=0}^{255}(\mathbf D^{2i}-\mathbf D^{2i+1})=\sum_{j=0}^{511}(-\mathbf D)^j .
\]

**6.3.** For the first list \(c_0=0.567-0.976/k\), \(d_0=0.250+0.408/k\), \(C=-0.0074+0.0115/k\). For the second list \(c_0=1/k\), \(d_0=-0.209+0.938/k\), \(C=0.0096-0.017/k\). The limits are \((0.567,0.250,-0.0074)\) and \((0,-0.209,0.0096)\).

**6.4.** \(T_k(n)=k^{-1}e^{-k(n-1)}\) and \(T_k'(n)=-e^{-k(n-1)}\). With \(Q_n>1.75\) and \(|D_n|<2.12\), the first term is at most \(e^{-k(n-1)}/(1.75\,k)\) and the second at most \((1+2.12/k)\,e^{-k(n-1)}/1.75\).

## References

- [OpenAI-T] OpenAI, *Universal optimality of the triangular lattice*, OpenAI Math Release preprint, 23 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/Universal-optimality-of-the-triangular-lattice-September-23-2026
- [Arb] F. Johansson, *Arb: efficient arbitrary-precision midpoint-radius interval arithmetic*, IEEE Transactions on Computers 66 (2017). https://arxiv.org/abs/1611.02831
