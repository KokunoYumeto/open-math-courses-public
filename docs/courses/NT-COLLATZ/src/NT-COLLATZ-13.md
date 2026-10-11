# Logarithmic sampling and first-passage distributions

*Written by GPT-6 Astra, Ultra reasoning, in Codex, October 2026. Self-checked by the writing AI. Original exposition, proofs and exercises: CC0 1.0.*

A distributional estimate becomes useful for dynamics only after we identify the experiment to which it applies. Independent random words are not individual integer orbits. Moreover, observing an orbit at its first entrance into a set is different from observing it after a prescribed number of steps. The entrance time depends on the trajectory itself.

This lesson connects these two descriptions. Logarithmic sampling of starting integers gives an accurate finite model for their valuation words. Looking a fixed number of steps before an entrance then exposes an exact arithmetic inverse. Its harmonic weights form a bounded function on a finite residue group. The fine-scale mixing theorem can act on that function, and the resulting main term no longer depends on which of two neighbouring logarithmic shells supplied the starting integer.

The conclusion is Tao's first-passage stabilization theorem, with failure to enter retained as a separate state. It is the analytic input needed for the transport arguments of [First passage and transport across scales](NT-COLLATZ-04.md). Its proof uses [the exact valuation cylinder and finite sampling comparison](NT-COLLATZ-06.md#how-much-information-a-residue-class-provides), [geometric concentration](NT-COLLATZ-06.md#an-exponential-estimate-with-explicit-constants), and [fine-scale mixing](NT-COLLATZ-12.md#mixing-while-preserving-a-coarse-observation). Basic references are Terence Tao's *Almost all orbits of the Collatz map attain almost bounded values*, Sections 4–6, and the treatment of probability transport in [Pushforward measures and logarithmic sampling](NT-COLLATZ-03.md). All further arguments are given below.

## The entrance law and the sampling experiment

Write \(\mathbb O=\{1,3,5,\ldots\}\). For \(N\in\mathbb O\), let

\[
S(N)=\frac{3N+1}{2^{\nu_2(3N+1)}}.
\]

For a real threshold \(x\geq1\), define

\[
\begin{aligned}
\tau_x(N)&=\inf\{j\geq0:S^j(N)\leq x\},\\
p_x(N)&=S^{\tau_x(N)}(N)\quad\text{if }\tau_x(N)<\infty.
\end{aligned}
\tag{1}
\]

If no such time exists, set \(\tau_x(N)=\infty\) and \(p_x(N)=\dagger\). The symbol \(\dagger\) is a new state, not an integer. Thus \(p_x\) maps \(\mathbb O\) into the finite set \(E_x=(\mathbb O\cap[1,x])\cup\{\dagger\}\). The time starts at zero: a starting integer already at most \(x\) is its own entrance location.

Throughout the lesson fix

\[
\alpha=\frac{1001}{1000},\qquad d=\log(4/3),\qquad L=\log x.
\]

For large \(y\), let \(N_y\) be sampled from the odd integers in \([y,y^\alpha]\) with probabilities

\[
\begin{aligned}
\mathbb P(N_y=N)&=\frac1{H_yN},\\
H_y&=\sum_{N\in\mathbb O\cap[y,y^\alpha]}\frac1N.
\end{aligned}
\tag{2}
\]

Endpoints are real; only integers in the displayed interval are sampled. Equal lengths on the logarithmic axis have approximately equal mass under this law. Write \(P_y=\mathcal L(p_x(N_y))\) for the resulting entrance law at the fixed threshold \(x\).

**Theorem 1 (Stabilization of entrance distributions).** There are absolute constants \(C,x_*\) such that, for every \(x\geq x_*\) and \(y\in\{x^\alpha,x^{\alpha^2}\}\),

\[
\begin{aligned}
\mathbb P(\tau_x(N_y)=\infty)&\leq Cx^{-1/20000},\\
\|P_{x^\alpha}-P_{x^{\alpha^2}}\|_1
&\leq C(\log x)^{-1/5}.
\end{aligned}
\tag{3}
\]

The norm is the sum of absolute differences of masses on \(E_x\), without a factor of one half. Constants are not optimized. The result compares these two specified shells; it does not assert uniform sampling inside \([1,x]\), or convergence of every orbit to one.

*Reference:* Tao, Proposition 1.11 and Section 5. We retain a separate failure state and display exponents sufficient for the argument.

We first establish the sampling and arithmetic facts. The final section of the proof will join them to mixing.

## Harmonic mass in arithmetic progressions

**Lemma 2 (Reciprocal sums).** For real \(1\leq A<B\), an integer \(q\geq1\), and a residue \(h\pmod q\),

\[
\left|\sum_{\substack{A\leq N\leq B\\N\equiv h\ (q)}}\frac1N
       -\frac1q\log\frac BA\right|\leq\frac1A.
\tag{4}
\]

**Proof.** If the progression contributes \(t_0<\cdots<t_s\), its spacing is \(q\). Since \(1/t\) decreases,

\[
\begin{aligned}
\sum_{i=0}^s\frac1{t_i}
&\leq\frac1{t_0}+\frac1q\int_{t_0}^{t_s}\frac{dt}{t},\\
\sum_{i=0}^s\frac1{t_i}
&\geq\frac1q\int_{t_0}^{t_s+q}\frac{dt}{t}.
\end{aligned}
\]

The first line is at most \(A^{-1}+q^{-1}\log(B/A)\). In the second, \(t_s+q>B\) and \(0\leq t_0-A<q\), so the missing lower integral is at most \(q^{-1}\log(t_0/A)\leq A^{-1}\). If there is no point, \(B-A<q\), and \(q^{-1}\log(B/A)\leq(B-A)/(qA)<A^{-1}\). ∎

For an even \(q\), put \(J=\log(B/A)\) and let \(W_h\) denote the reciprocal sum for an odd residue. There are \(q/2\) such residues. Consequently,

\[
\sum_{h\text{ odd }(q)}|W_h-J/q|\leq\frac q{2A},
\qquad |H-J/2|\leq\frac q{2A},
\]

where \(H=\sum_hW_h\). When \(AJ\geq2q\), this gives \(H\geq J/4\) and

\[
\sum_{h\text{ odd }(q)}\left|\frac{W_h}{H}-\frac2q\right|
\leq\frac{4q}{AJ}.
\tag{5}
\]

To verify the normalization, insert and subtract \(J/(qH)\); the sum of the resulting normalization errors is \(|H-J/2|/H\). The uniform probability of an odd class is \(2/q\), not \(1/q\).

In particular, applying (4) with \(q=2\) gives

\[
H_y=\frac{\alpha-1}{2}\log y+O(y^{-1}).
\tag{6}
\]

Here and below \(O(g)\) denotes a quantity of absolute value at most a constant times \(g\). Unless explicitly indexed, the constants are absolute and uniform over the two choices of \(y\), all entrance events, and all other displayed indices.

## Finite words sampled from integers

For a word \(a=(a_1,\ldots,a_k)\) of positive integers, set

\[
\begin{aligned}
A_0&=0,\qquad A_i=a_1+\cdots+a_i,\\
C_k(a)&=\sum_{i=1}^k3^{k-i}2^{A_{i-1}},\\
F_k(a)&=2^{-A_k}C_k(a).
\end{aligned}
\tag{7}
\]

The actual word of \(N\) is \(V_k(N)=(\nu_2(3S^{i-1}(N)+1))_{i=1}^k\). Iterating its affine branches gives

\[
S^k(N)=3^k2^{-A_k}N+F_k(a),\qquad a=V_k(N).
\tag{8}
\]

Every suffix exponent in \(F_k\) is positive. Hence \(0<F_k<\sum_{i=1}^k3^{k-i}<3^k\). Set \(F_0=0\).

Choose the two integer lengths

\[
n_0=\left\lfloor\frac{L}{10\log2}\right\rfloor,
\qquad m=\left\lfloor\frac{L}{100000}\right\rfloor.
\tag{9}
\]

Let \(\gamma_k\) denote the law of \(k\) independent positive geometric variables with \(\mathbb P(a_i=b)=2^{-b}\). With \(q=2^{3n_0}\), the floor gives \(x^{3/10}/8\leq q\leq x^{3/10}\). Apply (5) to \([y,y^\alpha]\), then the finite sampling comparison in [Theorem 5 of Geometric waiting times and controlled conditioning](NT-COLLATZ-06.md#how-much-information-a-residue-class-provides). Its modulus exponent is \(3n_0\), so

\[
\begin{aligned}
&\|\mathcal L(V_{n_0}(N_y))-\gamma_{n_0}\|_1\\
&\qquad\leq\frac{4q}{y(\alpha-1)\log y}+2e^{-n_0/12}\\
&\qquad=O(x^{-1/20000}).
\end{aligned}
\tag{10}
\]

The last estimate follows from \(y\geq x^\alpha\), \(n_0\geq L/(10\log2)-1\), and \(\log2<1\). No infinite-orbit independence is being assumed.

**Lemma 3 (Descent by a finite time).** The first estimate in (3) holds even with the event \(\{\tau_x(N_y)>n_0\}\) in place of failure forever.

**Proof.** The lower-tail concentration bound for a geometric sum gives
\(\gamma_{n_0}(A_{n_0}\leq1.9n_0)\leq e^{-n_0/1200}\). Indeed, the quadratic exponent at deviation \(n_0/10\) is \(n_0/1200\), and the linear exponent is larger because \(d>1/4\). Equation (10) transfers this bound to the actual word, with total error \(O(x^{-1/20000})\).

Outside that event, (8) yields

\[
S^{n_0}(N_y)\leq 3^{n_0}2^{-1.9n_0}x^{\alpha^3}+3^{n_0}.
\]

The elementary integer inequality \(3^5<2^8\) gives \(\log_2 3<8/5\). Since \(\alpha^3<1.004\), retaining the floor in the term with negative exponent gives

\[
3^{n_0}2^{-1.9n_0}x^{\alpha^3}
\leq\frac{2^{1.9}}3 x^{\alpha^3+(\log_2 3-1.9)/10}
<2x^{0.974}.
\]

The other term is at most \(x^{4/25}\). For sufficiently large \(x\), their sum is less than \(x\). Thus entry has occurred by \(n_0\). ∎

## Locating the passage time on a logarithmic scale

We need more than a terminal bound: all prefixes must stay near their mean exponent. Define

\[
\begin{gathered}
\mathcal A_k=\left\{a\in\mathbb Z_{>0}^k:
 \begin{array}{l}|A_j-2j|<L^{3/5}\\\text{for all }0\leq j\leq k\end{array}\right\},\\
G=\{V_{n_0}(N_y)\in\mathcal A_{n_0}\}.
\end{gathered}
\tag{11}
\]

Concentration at each of the at most \(n_0=O(L)\) prefixes, followed by a union bound, gives

\[
\begin{aligned}
\gamma_k(\mathcal A_k^c)&=O(L^{-10})\quad(k\leq n_0),\\
\mathbb P(G^c)&=O(L^{-10}).
\end{aligned}
\tag{12}
\]

For completeness, the quadratic exponent is at least a positive constant times \(L^{1/5}\), uniformly for \(1\leq j\leq n_0\); the linear exponent is of order \(L^{3/5}\). Thus the union bound is \(O(L e^{-cL^{1/5}})\), smaller than \(L^{-10}\) for sufficiently large \(L\). Equation (10) adds a smaller error for actual words.

**Lemma 4 (Orbit and time bounds).** On \(G\), there are absolute constants \(K,K'\) such that

\[
\begin{gathered}
|\log S^j(N_y)-\log N_y+jd|\leq K L^{3/5},\\
0\leq j\leq n_0,\\
\left|\tau_x(N_y)-\frac{\log(N_y/x)}d\right|
\leq K'L^{3/5}.
\end{gathered}
\tag{13}
\]

**Proof.** In (8), the main term is \((3/4)^jN_y\exp(-(A_j-2j)\log2)\). It is at least
\(x^{\alpha-d/(10\log2)}\exp(-L^{3/5}\log2)\), which exceeds \(x^{9/10}\) eventually because \(d<\log2\) and \(\alpha>1\). The nonnegative offset is at most \(3^{n_0}\leq x^{4/25}\). Its ratio to the main term tends to zero uniformly. Taking logarithms proves the first line.

At \(j=n_0\), the log of the orbit value divided by \(x\) is at most
\((\alpha^3-1)L-dn_0+KL^{3/5}\). It is negative eventually: \(\alpha^3-1<1/250\), whereas \(d/(10\log2)>1/40\). The inequalities \(d>1/4\) and \(\log2<1\) follow by integrating \(1/t\). Thus \(1\leq t=\tau_x(N_y)\leq n_0\). Applying the first line at \(t\) and \(t-1\), using \(S^t(N_y)\leq x<S^{t-1}(N_y)\), proves the second line, with the additional one step absorbed into \(K'L^{3/5}\). ∎

Define the interval of possible comparison times

\[
I_y=\left[
 \frac{\log(y/x)}d+L^{4/5},\quad
 \frac{\log(y^\alpha/x)}d-L^{4/5}
\right].
\tag{14}
\]

For large \(x\), it is nonempty and lies in \([2m,n_0]\). For the lower endpoint use \(d<1\) and \(\log(y/x)\geq L/1000\); for the upper endpoint use \((\alpha^3-1)/d<4/250<1/10\), whereas \(n_0\geq L/10-1\). The length is a positive constant times \(L\), minus \(2L^{4/5}\).

**Lemma 5 (The interior time window).**
\(\mathbb P(\tau_x(N_y)\notin I_y)=O(L^{-1/5})\).

**Proof.** Restrict the start to
\([y e^{L^{4/5}},y^\alpha e^{-L^{4/5}}]\). Its predicted time \(\log(N_y/x)/d\) has distance at least \((1/d-1)L^{4/5}\) from either endpoint of \(I_y\). This dominates the error in (13). By (4) with modulus two and (6), the two removed intervals have combined probability \(O(L^{4/5}/L)=O(L^{-1/5})\). Add (12).

The restriction is multiplicative in the original coordinate because time is proportional to its logarithm. An additive deletion of width \(L^{4/5}\) would give a log margin at most \(L^{4/5}/y\) at the lower endpoint, not the required margin of order \(L^{4/5}\). ∎

## Moving a fixed distance back from the entrance

Fix any event \(E\subseteq\mathbb O\cap[1,x]\), and define the finite set

\[
\begin{split}
E' = \{M\in\mathbb O:\;&\tau_x(M)=m,\ p_x(M)\in E,\\
&e^{-L^{7/10}}e^{md}x\leq M\leq e^{L^{7/10}}e^{md}x\}.
\end{split}
\tag{15}
\]

This set depends on \(x,E\), not on \(y\). For an integer \(n\in I_y\), put \(r=n-m\). Then \(m\leq r\leq n_0-m\).

**Lemma 6 (Replacing entrance by an earlier observation).** On \(G\), the following events are equal:

\[
\{\tau_x(N_y)=n,\ p_x(N_y)\in E\}
=\{S^r(N_y)\in E'\}.
\tag{16}
\]

**Proof.** Suppose first that entry occurs at \(n\), and put \(Y_j=S^j(N_y)\). Then \(\tau_x(Y_r)=m\) and its entrance location is \(Y_n\). By (13), the change between the two adjacent log coordinates at \(n-1,n\) has absolute size at most \(d+2KL^{3/5}\). Since \(Y_{n-1}>x\geq Y_n\),
\(\log Y_n=L+O(L^{3/5})\). Subtracting the two bounds (13) at \(r,n\) gives \(\log Y_r=L+md+O(L^{3/5})\). For large \(L\), this lies within the window (15).

Conversely, if \(Y_r\in E'\), the signed lower bound obtained by subtracting (13) at \(j,r\) is

\[
\begin{aligned}
Y_j&\geq e^{-2KL^{3/5}}e^{(r-j)d}Y_r\\
&\geq x\exp((n-j)d-2KL^{3/5}-L^{7/10}),\\
&\qquad 0\leq j\leq r.
\end{aligned}
\tag{17}
\]

At \(j=r\), the exponent is \(md-2KL^{3/5}-L^{7/10}\), which tends to infinity because \(m=\lfloor L/100000\rfloor\). It is larger for earlier \(j\). No entry has therefore occurred by time \(r\); the next first entry is exactly \(m\) steps later, as required by (15). ∎

The events \(\{\tau_x=n\}\) are disjoint. Sum (16) over the integer times in \(I_y\), use Lemma 5, and then replace the full good event by its prefix of length \(r\). The latter replacement changes each probability by at most \(\mathbb P(G^c)\), because the full good event implies the prefix event. There are \(O(L)\) times. Define

\[
Q_{n,y}=\mathbb P\left(
\begin{gathered}
S^{n-m}(N_y)\in E',\\
V_{n-m}(N_y)\in\mathcal A_{n-m}
\end{gathered}\right).
\]

We obtain

\[
\mathbb P(p_x(N_y)\in E)
=\sum_{n\in I_y\cap\mathbb Z}Q_{n,y}+O(L^{-1/5}).
\tag{18}
\]

The smaller accumulated error \(O(L^{-9})\) is included in the displayed error. This step is why a single fixed look-back length is useful: every comparison time uses the same target set \(E'\).

## Reconstructing the starting integer

For \(a\in\mathcal A_r\), abbreviate \(A=A_r\). Write \(C=C_r(a)\) and \(F=F_r(a)\). Solving the affine equation with endpoint \(M\) gives

\[
\Phi_r(a,M)=\frac{2^AM-C}{3^r}
=\frac{2^A(M-F)}{3^r}.
\tag{19}
\]

**Proposition 7 (Exact inverse and its mass).** For \(M\in E'\) and \(n\in I_y\cap\mathbb Z\), with \(r=n-m\), there is a start \(N\in\mathbb O\cap[y,y^\alpha]\) having word \(a\) and endpoint \(S^r(N)=M\) if and only if

\[
M\equiv F_r(a)\pmod {3^r}.
\tag{20}
\]

Dyadic denominators in this congruence are reduced by inverting two modulo \(3^r\). When the start exists it is unique and equals (19). Its probability under (2) is

\[
\frac1{H_y\Phi_r(a,M)}
=\frac{1+O(x^{-7/10})}{H_y}\,\frac{2^{-A}3^r}{M}.
\tag{21}
\]

**Proof.** Necessity and uniqueness follow from (8). Conversely, (20) says precisely that the integer \(2^AM-C\) is divisible by \(3^r\). Since \(C\) is odd and \(2^AM\) even, the resulting integer is odd.

It also lies in the sampling interval. Indeed, \(F\leq3^r\leq x^{4/25}\), while \(M\geq x\exp(-L^{7/10})\). Thus \(0\leq F/M\leq x^{-7/10}<1/2\) eventually. Write \(A=2r+\delta\) and \(M=xe^{md+\eta}\); then \(|\delta|<L^{3/5}\), \(|\eta|\leq L^{7/10}\), and

\[
\begin{aligned}
\log\Phi_r={}&L+nd+\delta\log2+\eta\\
&+\log(1-F/M).
\end{aligned}
\tag{22}
\]

The last three terms have absolute value at most \(2L^{7/10}\) eventually. The margins in (14), multiplied by \(d\), are \(dL^{4/5}\), which are larger. This proves positivity and \(y\leq\Phi_r\leq y^\alpha\).

It remains to check that the prescribed word really occurs. The equality \(3^rN+C=2^AM\), with \(M\) odd, implies
\(3^rN+C\equiv2^A\pmod {2^{A+1}}\). This is exactly the residue class in Proposition 4 of [the valuation-cylinder lesson](NT-COLLATZ-06.md#how-much-information-a-residue-class-provides). That proposition proves that every positive start in the class has the stated word. Substitution in (8) then gives endpoint \(M\).

Finally, \(1/\Phi_r=2^{-A}3^r/(M-F)\). The bound on \(F/M\) proves (21). ∎

More explicitly, (19) is the inverse of the map

\[
N\longmapsto(V_r(N),S^r(N))
\]

from starts in \([y,y^\alpha]\) with good prefix and endpoint in \(E'\), onto the pairs in \(\mathcal A_r\times E'\) satisfying (20). Both compositions are identities, and every fibre is a singleton. Merely keeping the endpoint would instead lose the word coordinate; the inverse formula uses both.

For a small exact example, take \(a=(1,2,3)\). Then \(A=6\), \(C=23\), and \(F=23/64\). Condition (20) becomes \(M\equiv5\pmod {27}\). At \(M=5\), formula (19) gives \(N=11\), whose orbit is \(11\mapsto17\mapsto13\mapsto5\). More generally the positive odd endpoints in that class are \(M=5+54k\), \(k\geq0\), and the starts are \(N=11+128k\). The arithmetic bijection is exact; restrictions to large logarithmic windows are needed only for the uniform asymptotic estimates.

## A bounded harmonic function on the residue group

For \(r=n-m\), introduce the function

\[
c_n(X)=3^r\sum_{\substack{M\in E'\\M\equiv X\ (3^r)}}\frac1M,
\qquad X\in\mathbb Z/3^r\mathbb Z.
\tag{23}
\]

The factor \(3^r\) compensates for the spacing of the residue class. A uniform bound is essential: a small error between probability laws controls their expectations against a bounded function, not against arbitrarily large weights.

**Lemma 8 (Uniform harmonic bound).** There is an absolute constant \(C_0\) such that \(0\leq c_n(X)\leq C_0\), uniformly in the event \(E\), both shells, their comparison times, and the residue \(X\), for sufficiently large \(x\).

**Proof.** Partition the summands by the length-\(m\) actual word of \(M\). For such a word put \(A=a_1+\cdots+a_m\) and \(b=a_m\). Entry at exactly \(m\) implies

\[
\begin{aligned}
3^m2^{-A}M+F_m&\leq x,\\
x&<3^{m-1}2^{-(A-b)}M+F_{m-1}.
\end{aligned}
\tag{24}
\]

Since \(F_{m-1}\leq3^{m-1}=o(x)\), every contributing \(M\) lies between

\[
M_0=3^{-m}2^{A-b}x,
\qquad M_1=3^{-m}2^Ax.
\tag{25}
\]

For the lower bound, it suffices that \(x-F_{m-1}>x/3\), which holds uniformly for large \(x\). The word also forces one residue class modulo \(2^{A+1}\), by the exact valuation cylinder. Intersecting it with \(X\pmod{3^r}\) gives one class modulo
\(q=2^{A+1}3^r\).

Here is the required elementary Chinese remainder argument. For coprime positive integers \(u,v\), the Euclidean algorithm gives integers \(s,t\) with \(su+tv=1\). The integer \(h_vsu+h_utv\) has residues \(h_u\pmod u\), \(h_v\pmod v\). Two solutions differ by a multiple of both \(u,v\), hence by a multiple of \(uv\); the latter assertion follows by multiplying the identity \(su+tv=1\) after dividing out one modulus. This proves existence and uniqueness of the combined class. Apply it to the displayed powers of two and three.

Let \(c_{n,a}(X)\) be the contribution of this word to (23). By Lemma 2,

\[
c_{n,a}(X)\leq3^r\left(\frac1{M_0}
                  +\frac1q\log\frac{M_1}{M_0}\right).
\tag{26}
\]

If \(2^A\leq x^{1/2}\), then

\[
\frac q{M_0}=\frac{2^{b+1}3^n}{x}
\leq2x^{-17/50}<1,
\]

because \(b\leq A\) and \(3^n\leq x^{4/25}\). Since \(M_1/M_0=2^b\), (26) now gives
\(c_{n,a}(X)\leq C b2^{-A}\).

For \(2^A>x^{1/2}\), a second lower bound handles the possible first point of the progression. Write
\(H=3^{m-1}2^{-(A-b)}M\). The right inequality in (24) gives \(H>x-F_{m-1}\), so \(F_{m-1}=o(H)\). Also \(2^b\) divides the positive integer \(3(H+F_{m-1})+1\), by the last valuation. Therefore

\[
\begin{aligned}
2^b&\leq3(H+F_{m-1})+1\leq5H,\\
M&\geq\frac15 3^{1-m}2^A.
\end{aligned}
\tag{27}
\]

for sufficiently large \(x\). Use the larger of this bound and \(M_0\) in the first term of (26); the logarithmic term can only decrease. If the resulting interval is empty its contribution is zero. Otherwise,

\[
c_{n,a}(X)\leq C(3^n2^{-A}+b2^{-A}).
\tag{28}
\]

Both branches are summable uniformly in \(m\). The terms involving the last valuation have the exact total

\[
\begin{aligned}
\sum_{a_1,\ldots,a_m\geq1}b2^{-A}
&=\left(\sum_{a\geq1}2^{-a}\right)^{m-1}
 \sum_{b\geq1}b2^{-b}\\
&=2.
\end{aligned}
\tag{29}
\]

On the second branch alone,

\[
\begin{aligned}
&3^n\sum_{2^A>x^{1/2}}2^{-A}\\
&\quad\leq3^nx^{-1/4}\sum_{a_1,\ldots,a_m\geq1}2^{-A/2}\\
&\quad=3^nx^{-1/4}(1+\sqrt2)^m\\
&\quad\leq x^{-8999/100000}.
\end{aligned}
\tag{30}
\]

The last inequality uses \(m\leq L/100000\) and \(\log(1+\sqrt2)<1\); for example \(1+\sqrt2<5/2<1+1+1/2+1/6<e\). All sums here have nonnegative terms, so they may be regrouped by finite partial sums and increasing limits. Equations (29)–(30) prove the uniform bound. ∎

The separate treatments of a progression's first point and its integral part explain the split. Keeping \(b2^{-A}\) is important: replacing it everywhere by a multiple of \(2^{-A/2}\) would leave the growing sum \((1+\sqrt2)^m\).

## Applying mixing and cancelling the shell dependence

Let \(\mu_r\) be the offset law from the preceding lesson. Its random variable is
\(T_r=\sum_{j=1}^r3^{j-1}2^{-(a_1+\cdots+a_j)}\pmod{3^r}\) for independent geometric \(a_i\). The offset \(F_r(a)\) in (7) equals \(T_r(a_r,\ldots,a_1)\). Reversal preserves the independent product law. Hence \(F_r\pmod{3^r}\) also has law \(\mu_r\). This equality concerns the unrestricted random word; no reversal invariance of the good-prefix event is needed.

Set

\[
B_{n,E}=\sum_{a\in\mathcal A_r}2^{-A_r}c_n(F_r(a)\bmod3^r).
\tag{31}
\]

Proposition 7 and (18), using nonnegative summands to keep the relative error uniform, give

\[
\begin{aligned}
\mathbb P(p_x(N_y)\in E)
={}&\frac1{H_y}\sum_{n\in I_y\cap\mathbb Z}B_{n,E}\\
&+O(L^{-1/5})\\
&+O(x^{-7/10})\frac{\sum_nB_{n,E}}{H_y}.
\end{aligned}
\tag{32}
\]

By Lemma 8, every \(B_{n,E}\leq C_0\), while the number of times and \(H_y\) are both of order \(L\). Thus the last term in (32) is \(O(x^{-7/10})\), uniformly in \(E\).

The independent-word bound (12) and Lemma 8 allow removal of the good-prefix restriction in (31), with error \(O(L^{-10})\). Apply Theorem 1 of [Arithmetic separation and fine-scale mixing](NT-COLLATZ-12.md#mixing-while-preserving-a-coarse-observation) at levels \(m\leq r\), with exponent 12. For a bounded function, its expectation error is at most its supremum times the \(\ell^1\) distance. Consequently,

\[
\begin{aligned}
B_{n,E}
={}&\sum_{X\bmod3^r}c_n(X)3^{m-r}\mu_m(X\bmod3^m)\\
&+O(L^{-10}).
\end{aligned}
\tag{33}
\]

Here \(m\geq L/200000\) for sufficiently large \(L\), so \(m^{-12}=O(L^{-12})\). Substitution of (23) into this finite sum cancels its apparent dependence on \(n\) exactly:

\[
\begin{aligned}
Z_E&=\sum_{M\in E'}\frac{3^m}{M}\mu_m(M\bmod3^m),\\
B_{n,E}&=Z_E+O(L^{-10}).
\end{aligned}
\tag{34}
\]

Each \(M\) has exactly one residue \(X\pmod{3^r}\), and \(3^r3^{m-r}=3^m\). This proves (34) without an additional estimate. Moreover \(Z_E\leq C_0\): it is the expectation of \(c_n\) under the probability law \(U_{m,r}\mu_m\). Thus its uniform bound does not depend on first proving the final probability formula.

Finally, if \(a_y,b_y\) are the real endpoints of \(I_y\), the exact number of integer times is

\[
\begin{aligned}
\#(I_y\cap\mathbb Z)
&=\lfloor b_y\rfloor-\lceil a_y\rceil+1\\
&=\frac{\alpha-1}{d}\log y-2L^{4/5}+\varepsilon_y,\\
&\qquad -1<\varepsilon_y\leq1.
\end{aligned}
\tag{35}
\]

Divide by (6). The ratio is \(2/d+O(L^{-1/5})\). In (32)–(34), the \(O(L)\) number of terms is balanced by \(H_y\asymp L\). We conclude, uniformly over all events \(E\), that

\[
\mathbb P(p_x(N_y)\in E)=\frac2d Z_E+O(L^{-1/5}).
\tag{36}
\]

Both \(E'\) and \(\mu_m\) are independent of the choice of shell. Subtract (36) for the two shells. For an event in \(E_x\) containing \(\dagger\), use its complement, which does not contain \(\dagger\); differences of total masses are zero. Thus the same bound holds for every event in \(E_x\). If \(P,Q\) are two probability mass functions, summing \(P-Q\) over its positive coordinates shows
\(\|P-Q\|_1=2\sup_E|P(E)-Q(E)|\). This proves the second estimate in (3). Lemma 3 proves the first. ∎

## What the comparison makes possible

The argument has now passed from binary valuation information to ternary residue mixing and then back to integer trajectories. Logarithmic weights make the inverse affine branches carry the geometric factors \(2^{-A}\). First passage restricts their endpoints strongly enough to keep the harmonic test functions uniformly bounded. Mixing removes the comparison time from the main term, and the logarithmic length of the time window cancels the sampling normalization.

The resulting entrance maps can be composed across thresholds. Their adjacent-scale discrepancies are summable along the sequence \(x,x^\alpha,x^{\alpha^2},\ldots\), since \((\log x^{\alpha^j})^{-1/5}=\alpha^{-j/5}(\log x)^{-1/5}\). This is the connection to probability transport: one can compare many scales without paying an error proportional to their number. [Compatible entrance laws and weighted orbit minima](NT-COLLATZ-14.md) supplies that further transport argument and its quantitative orbit-minimum conclusion, without assuming that every integer follows an independent random word.

## Exercises with solutions

### 1 Recover an orbit from two valuations

Take the word \((3,1)\). Find its affine offset, the allowed positive odd endpoints, and the corresponding positive starts. Verify the smallest example directly.

**Solution.** Here \(A=4\), \(C=3+8=11\), and \(F=11/16\). Modulo nine, \(16^{-1}=4\), so \(M\equiv8\pmod9\). The positive odd endpoints are \(M=17+18k\), \(k\geq0\). Formula (19) gives \(N=29+32k\). At \(k=0\), \(3\cdot29+1=88=8\cdot11\) and \(3\cdot11+1=34=2\cdot17\), giving \(29\mapsto11\mapsto17\). The starts form one odd residue class modulo \(2^{4+1}=32\).

### 2 A later crossing need not be the first

For threshold \(x=7\), start at \(N=9\). Compute the orbit through time five. Put \(n=5,m=2,r=3\). Does \(\tau_7(S^r(N))=m\) imply \(\tau_7(N)=n\)? Explain which part of Lemma 6 prevents this error in the theorem.

**Solution.** The orbit is
\(9\mapsto7\mapsto11\mapsto17\mapsto13\mapsto5\).
Thus \(\tau_7(9)=1\), but \(\tau_7(17)=2\). The displayed implication is false by itself. In Lemma 6, membership in \(E'\), together with the signed bound (17), proves that every iterate through time \(r\) is strictly above \(x\). The later entry is then the first. This argument uses the large-\(x\) inequalities and is not a claim about the small example.

### 3 Keep the summable factor

For positive words of length \(m\), set \(A=\sum_i a_i\), \(b=a_m\). Evaluate \(\sum b2^{-A}\) and \(\sum2^{-A/2}\). Also prove, for any real \(R>0\), that
\(\sum_{2^A>R}2^{-A}\leq R^{-1/2}(1+\sqrt2)^m\).

**Solution.** The first sum factors into \(m-1\) sums equal to one and the sum \(\sum_{b\geq1}b2^{-b}=2\). For the second, \(\sum_{a\geq1}2^{-a/2}=1/(\sqrt2-1)=1+\sqrt2\), so the product is \((1+\sqrt2)^m\). On the restricted set, \(2^{-A/2}<R^{-1/2}\); multiply this by the other factor \(2^{-A/2}\) and sum. The first total is uniform in length, while the second alone is not.

### 4 Calculate the exact collapse of a lifted law

Let \(m=1,r=2\), and let \(\mu_1\) be the law of \(2^{-a}\pmod3\) for \(\mathbb P(a=k)=2^{-k}\). Use the toy endpoint set \(D=\{5,7,11\}\) and define \(c(X)=9\sum_{M\in D,\,M\equiv X\ (9)}1/M\). Calculate its expectation under the uniform lift of \(\mu_1\) to \(\mathbb Z/9\mathbb Z\), both directly and by collapse. No first-passage property of \(D\) is assumed.

**Solution.** Even positive exponents have mass \(1/3\) and give residue one; odd exponents have mass \(2/3\) and give residue two. Thus \(\mu_1(0)=0\), \(\mu_1(1)=1/3\), \(\mu_1(2)=2/3\). The lifted masses on those fibres are respectively \(0,1/9,2/9\). The nonzero values of \(c\) are \(c(5)=9/5\), \(c(7)=9/7\), \(c(2)=9/11\). Their expectation is

\[
\frac25+\frac17+\frac2{11}=\frac{279}{385}.
\]

The collapsed expression \(\sum_{M\in D}3\mu_1(M\bmod3)/M\) gives the same three terms. This identity needs no assumption on how the finite endpoint set was obtained. First passage was used earlier to bound the corresponding function uniformly as the parameters grow.

## References

- Terence Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Forum of Mathematics, Pi 10 (2022), e12; [arXiv:1909.03562, version 7](https://arxiv.org/abs/1909.03562v7). The first-passage theorem and its logarithmic sampling, look-back and mixing mechanism are due to Tao. Sections 4–6 are the relevant arguments.
- [Geometric waiting times and controlled conditioning](NT-COLLATZ-06.md), especially the geometric concentration theorem, valuation-cylinder proposition and finite sampling comparison.
- [Arithmetic separation and fine-scale mixing](NT-COLLATZ-12.md), especially its fine-scale theorem with exact uniform lifting.
- [First passage and transport across scales](NT-COLLATZ-04.md), for the entrance-map composition and summable-scale transport framework.
