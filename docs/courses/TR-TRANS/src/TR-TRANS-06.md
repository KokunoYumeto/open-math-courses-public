# Gelfond–Schneider and Hilbert's seventh problem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol at Ultra. Public domain (CC0).*

An algebraic base raised to a rational exponent remains algebraic. What happens for an algebraic irrational exponent? Hilbert made this his seventh problem in 1900. Gelfond proved the imaginary-quadratic case in 1929, including the transcendence of \(e^\pi\); Kuzmin obtained the real-quadratic case in 1930. Gelfond and Schneider independently resolved the general problem in 1934. Waldschmidt's *Auxiliary functions in transcendence proofs*, §§2.3 and 3.1.2, recounts this history.

We use Heights of algebraic numbers, particularly its polynomial-value inequality, and Siegel's lemma and the six exponentials theorem, particularly Schwarz's estimate. The latter lesson made a function small by prescribing many zeros. Here we make a determinant small because its rows become dependent to high order when all evaluation points move towards the origin. A separate polynomial argument guarantees that one of these determinants is nonzero. Laurent's interpolation determinants provide the method; Waldschmidt's *Linear Independence of Logarithms of Algebraic Numbers*, Chapters 2 and 4, develops it, including a zero estimate for the real case of the Gelfond–Schneider theorem. We begin by calculating what a small determinant means, then prove that the grid supplies a nonzero one.

For \(\alpha\ne0\), fix a complex logarithm \(A\) with \(e^A=\alpha\), and define the corresponding value of \(\alpha^\beta\) to be \(e^{\beta A}\). We will keep this same \(A\) throughout the proof. This convention treats each possible value of the power, rather than quietly restricting to a principal branch.

### Theorem 6.1. Gelfond–Schneider

If \(\alpha,\beta\) are algebraic numbers, \(\alpha\notin\{0,1\}\) and \(\beta\notin\mathbb Q\), then every value of \(\alpha^\beta\) is transcendental.

The proof is completed in Section 5. Its only arithmetic inequality is already proved in the height lesson; the required rank and analytic determinant estimates are proved here.

## 1. Read the matrix before estimating it

For two functions \(1,e^{Az}\) at the points \(0,h\), the interpolation determinant is

\[
 \det\begin{pmatrix}1&1\\1&e^{Ah}\end{pmatrix}=e^{Ah}-1.
\]

As \(h\to0\), its two columns approach one another and the determinant has leading term \(Ah\). Smallness comes from this coincidence, not from either function being small. Nonvanishing is a different question: if \(Ah\) is a nonzero multiple of \(2\pi i\), the determinant is exactly zero. For the large matrix we will likewise prove a size bound for every choice of points and a separate existence statement for a nonzero choice.

Write

\[
 \alpha_1=e^A=\alpha,\qquad \alpha_2=e^{\beta A},
 \qquad z_{r,s}=r+s\beta,\qquad
 b_{r,s}=\alpha_1^r\alpha_2^s.
\]

Because \(\beta\notin\mathbb Q\), different integer pairs \((r,s)\) give different \(z_{r,s}\). Indeed, equality gives \(r-r'=-(s-s')\beta\); if \(s\ne s'\), this would express \(\beta\) as a rational number, and otherwise \(r=r'\).

For an integer \(N\) sufficiently large, set

\[
 K=\lfloor N\log N\rfloor,\qquad
 L=\left\lfloor\frac N{\log N}\right\rfloor,\qquad
 M=KL.
 \tag{6.4}
\]

All three are positive integers. The two floor choices imply

\[
 M\leq N^2,\qquad \frac M{N^2}\longrightarrow1,
 \qquad L<N.
 \tag{6.5}
\]

The interpolation matrix has rows indexed by \(0\leq r,s<2N\), columns indexed by \(0\leq u<K,0\leq v<L\), and entries

\[
 \mathcal A_{(r,s),(u,v)}
 =(r+s\beta)^u(\alpha_1^r\alpha_2^s)^v.
 \tag{6.6}
\]

As usual the zeroth power is \(1\), including at \(r=s=0\). The matrix has \(4N^2\) rows and \(M\) columns.


The entry in (6.6) can also be read as \(f_{u,v}(z_{r,s})\), where \(f_{u,v}(z)=z^ue^{vAz}\). Choose any \(M\) rows and call the square determinant \(\Delta\). The analytic estimate below applies to every such choice; its logarithmic formulation concerns the choices with \(\Delta\ne0\). Section 4 will prove that these choices exist.

Why use different sizes for \(K\) and \(L\)? On a circle of radius proportional to \(N\), the polynomial part costs \(K\log N\) and the exponential part costs \(LN\). With (6.4), both costs are \(o(N^2)\), while there are \(M\sim N^2\) columns. Thus the coincidence of columns can supply order \(M^2\sim N^4\) without growth of the functions consuming it. This is the first estimate to check before attempting the proof.

## 2. Coalescing points and the analytic gain

### Lemma 6.6. Analytic interpolation determinant estimate

Suppose \(R>\rho>0\), \(|\xi_j|\leq\rho\) for \(1\leq j\leq M\), and \(f_1,\ldots,f_M\) are analytic on a neighbourhood of \(|z|\leq R\), with \(|f_i|_R\leq S\). Then

\[
 \left|\det(f_i(\xi_j))_{i,j}\right|
 \leq M!\left(\frac\rho R\right)^{M(M-1)/2}S^M.
 \tag{6.7}
\]

**Proof.** Consider the analytic function of a single scaling variable

\[
 H(t)=\det(f_i(t\xi_j))_{i,j},
 \qquad |t|\leq R/\rho.
\]

We claim that it has a zero of order at least

\[
 T=0+1+\cdots+(M-1)=M(M-1)/2
\]

at \(t=0\). Expand each row using the Taylor series of its function at \(0\). In a term obtained by selecting row degrees \(k_1,\ldots,k_M\), the determinant contains the rows \((\xi_j^{k_i})_j\) and a factor \(t^{k_1+\cdots+k_M}\). If two degrees coincide, those two rows are identical and that term vanishes. If all degrees are distinct nonnegative integers, their sum is at least \(T\). For a coefficient of degree less than \(T\), only finitely many Taylor terms participate; the determinant expansion therefore justifies this cancellation coefficient by coefficient. The assertion also covers \(M=1\), when \(T=0\).

On \(|t|=R/\rho\), all \(t\xi_j\) lie in the disc \(|z|\leq R\). Maximum modulus and the determinant expansion bound \(|H(t)|\) by \(M!S^M\). Schwarz's estimate from Lemma 5.4, with outer radius \(R/\rho\) and inner radius \(1\), gives

\[
 |H(1)|\leq(\rho/R)^T M!S^M.
\]

This is (6.7). The scaling variable has outer radius \(R/\rho\), not \(R\); keeping the two radii distinct accounts for the factor in the estimate. \(\square\)

### Proposition 6.7. The analytic upper bound

For the nonzero minor of (6.6), with the fixed logarithm \(A\),

\[
 \log|\Delta|\leq-N^4
 \tag{6.8}
\]

for all sufficiently large \(N\).

**Proof.** Use the \(M\) functions

\[
 f_{u,v}(z)=z^ue^{vAz}
 \qquad(0\leq u<K,\ 0\leq v<L)
\]

at the selected points \(\xi_{r,s}=r+s\beta\). Their values are exactly the entries (6.6), because

\[
 e^{vA(r+s\beta)}=(\alpha_1^r\alpha_2^s)^v.
\]

Put

\[
 \rho=2N(1+|\beta|),\qquad R=e^5\rho.
\]

Every selected point is in \(|z|\leq\rho\). For large \(N\), \(R>1\), and

\[
 \log|f_{u,v}|_R\leq K\log R+LR|A|=o(N^2).
 \tag{6.9}
\]

Indeed, \(R\) is a fixed multiple of \(N\), so the first term is \(O(N(\log N)^2)\), and the second is \(O(N^2/\log N)\). Their ratios to \(N^2\) tend to zero. These elementary limits follow, for example, by putting \(t=\log N\) and using the exponential series to show \(t^k/e^t\to0\) for every fixed integer \(k\).

Thus \(S=e^{N^2}\) is an admissible bound for all the functions, for sufficiently large \(N\). Lemma 6.6 gives

\[
 \log|\Delta|
 \leq\log(M!)-\tfrac52M(M-1)+MN^2.
\]

Divide by \(N^4\). By (6.5), the negative term tends to \(-5/2\), the last term tends to \(1\), and the factorial term tends to zero, since

\[
 \log(M!)\leq M\log M\leq2N^2\log N.
\]

The right side divided by \(N^4\) therefore tends to \(-3/2\), and is at most \(-1\) for all sufficiently large \(N\). This proves (6.8). \(\square\)

The analytic gain is uniform over the minors. We now establish nonvanishing before using algebraicity to bound a chosen nonzero minor from below.

## 3. A translated grid supplies a nonzero value

**Worked failure of an arbitrary evaluation choice.** The independent polynomials \(1,Y^2\) give determinant zero at \(Y=1,-1\), but determinant \(3\) at \(Y=1,2\). Independence of functions does not certify every square evaluation matrix. A set containing three distinct points does certify that some two columns work: a nonzero polynomial of degree at most two cannot vanish on all three. Lemma 6.3 formalizes exactly this freedom of choice. The translation argument in Lemma 6.4 then turns that evaluation certificate into a degree contradiction in the additive coordinate.

### Lemma 6.2. At least one multiplicative generator has infinite order

Under the hypotheses above, at least one of \(\alpha_1,\alpha_2\) is not a root of unity.

**Proof.** If \(\alpha_1^m=1\) and \(\alpha_2^n=1\), with \(m,n>0\), then the kernel of the complex exponential gives

\[
 mA=2\pi i k,\qquad n\beta A=2\pi i\ell,
 \qquad k,\ell\in\mathbb Z.
\]

Here \(A\ne0\), since \(\alpha\ne1\), and hence \(k\ne0\). Division yields \(\beta=m\ell/(nk)\in\mathbb Q\), a contradiction. The logarithm is the originally fixed one, so its possible addition of \(2\pi i\) causes no branch exception. \(\square\)

### Lemma 6.3. Independent sparse powers on a finite set

Let \(0\leq k_1<\cdots<k_m<L\), and let \(E\subset\mathbb C^\times\) contain at least \(L\) distinct elements. One can choose \(m\) elements \(b_1,\ldots,b_m\in E\) for which

\[
 \det(b_j^{k_i})_{1\leq i,j\leq m}\ne0.
 \tag{6.1}
\]

**Proof.** Evaluate the \(m\) monomials \(Y^{k_i}\) at any \(L\) distinct elements of \(E\). If the resulting \(m\)-by-\(L\) matrix had dependent rows, some nonzero polynomial \(\sum_i c_iY^{k_i}\) of degree less than \(L\) would have \(L\) distinct roots. Repeated division by its linear root factors rules this out. The matrix has row rank \(m\), so it has a nonzero \(m\)-by-\(m\) minor. Its columns give the required elements. \(\square\)

### Lemma 6.4. A zero estimate for two translated grids

Let \(P\in\mathbb C[X,Y]\) be nonzero, with

\[
 \deg_XP<K,\qquad\deg_YP<L,
 \qquad K,L\geq1.
\]

Let \(R_1,S_1,R_2,S_2\) be positive integers. Assume that

\[
 E=\{\alpha_1^r\alpha_2^s:0\leq r<R_1,\ 0\leq s<S_1\}
\]

has at least \(L\) distinct elements, and that

\[
 Z=\{r+s\beta:0\leq r<R_2,\ 0\leq s<S_2\}
\]

has more than \((K-1)L\) distinct elements. Then at least one value

\[
 P(r+s\beta,\alpha_1^r\alpha_2^s),
 \qquad0\leq r<R_1+R_2-1,\quad
 0\leq s<S_1+S_2-1,
 \tag{6.2}
\]

is nonzero.

**Proof.** Suppose all values in (6.2) were zero. Expand in the powers of \(Y\) whose coefficients are nonzero:

\[
 P(X,Y)=\sum_{i=1}^m Q_i(X)Y^{k_i},
 \quad0\leq k_1<\cdots<k_m<L,
 \quad Q_i\ne0.
\]

In particular \(1\leq m\leq L\) and \(\deg Q_i\leq K-1\). Choose pairs \((r_j,s_j)\) in the first rectangle representing elements

\[
 b_j=\alpha_1^{r_j}\alpha_2^{s_j}
\]

with nonzero determinant (6.1), and put \(a_j=r_j+s_j\beta\). Consider the polynomial matrix

\[
 T(X)=(Q_i(X+a_j)b_j^{k_i})_{1\leq j,i\leq m},
 \qquad D(X)=\det T(X).
\]

If \(Q_i\) has degree \(d_i\) and leading coefficient \(c_i\ne0\), the coefficient of \(X^{d_1+\cdots+d_m}\) in \(D\) is

\[
 \left(\prod_i c_i\right)\det(b_j^{k_i})_{j,i}\ne0.
\]

Consequently

\[
 D\ne0,\qquad \deg D=\sum_i d_i\leq(K-1)m\leq(K-1)L.
 \tag{6.3}
\]

For any pair \((r',s')\) in the second rectangle, set

\[
 a'=r'+s'\beta,\qquad b'=\alpha_1^{r'}\alpha_2^{s'}\ne0.
\]

Each translated polynomial satisfies

\[
 \begin{aligned}
 P(a'+a_j,b_jb')
 &=P((r'+r_j)+(s'+s_j)\beta,
       \alpha_1^{r'+r_j}\alpha_2^{s'+s_j})=0,
 \end{aligned}
\]

because the summed pairs lie in the larger rectangle of (6.2). Thus

\[
 T(a')\begin{pmatrix}(b')^{k_1}\\ \vdots\\(b')^{k_m}\end{pmatrix}=0.
\]

The displayed vector is nonzero, since all its entries are powers of a nonzero number. Therefore \(D(a')=0\). The polynomial \(D\) has a root at every element of \(Z\), more than \((K-1)L\) distinct roots. This contradicts (6.3). \(\square\)

The argument keeps the possibility \(m=L\). No strict inequality between the number of monomials and \(L\) is needed: it is the number of distinct roots that strictly exceeds the degree bound.

## 4. From a nonzero value to a nonzero minor

### Proposition 6.5. Full column rank

The matrix (6.6) has rank \(M\).

**Proof.** A nontrivial linear dependence of its columns would give a nonzero polynomial

\[
 P(X,Y)=\sum_{u<K,v<L}c_{uv}X^uY^v
\]

vanishing at every grid pair in (6.6). Apply Lemma 6.4 with all four rectangle parameters equal to \(N\). By Lemma 6.2, powers of at least one of \(\alpha_1,\alpha_2\) supply \(N\) distinct multiplicative values in the first rectangle; this is more than the required \(L\). Since \(\beta\notin\mathbb Q\), there are \(N^2\) distinct additive values in the second rectangle, and

\[
 N^2\geq KL>(K-1)L.
\]

Lemma 6.4 makes at least one value with \(0\leq r,s<2N-1\) nonzero. Such a pair is included in the larger range \(0\leq r,s<2N\) where all values were assumed zero. This contradiction proves full rank. \(\square\)

Choose \(M\) rows whose square minor is nonzero, and denote its determinant by \(\Delta\). The choice may depend on \(N\). The estimates below will be uniform over every possible choice of these rows.

## 5. Compare the two bounds on the same minor

### Proposition 6.8. The arithmetic lower bound

Suppose \(\alpha_1,\alpha_2,\beta\) are algebraic. There is a constant \(c>0\), depending only on these three numbers, such that every nonzero minor selected above satisfies

\[
 \log|\Delta|\geq-\frac{cN^4}{\log N}
 \geq-\frac12N^4
 \tag{6.10}
\]

for all sufficiently large \(N\).

**Proof.** Using the selected row pairs, form the integer polynomial

\[
 P(X_1,X_2,X_3)
 =\det\bigl((r+sX_3)^u(X_1^rX_2^s)^v\bigr).
\]

It is nonzero, since \(P(\alpha_1,\alpha_2,\beta)=\Delta\ne0\). Let \(\ell(P)\) be its coefficient length, the sum of absolute values of its integer coefficients, and let \(e_j=\deg_{X_j}P\). Each term in the determinant contains exactly one entry from each of its \(M\) columns. Since \(r,s<2N\),

\[
 e_1,e_2\leq2NLM,\qquad e_3\leq KM,
 \qquad \ell(P)\leq M!(4N)^{KM}.
 \tag{6.11}
\]

For the last bound, the length of \((r+sX_3)^u\) is \((r+s)^u\leq(4N)^K\), with the convention that a zeroth power has length \(1\). Multiplication by the other monomial does not change length. Coefficient length is submultiplicative by the triangle inequality, and the determinant has \(M!\) signed product terms. Cancellation only lowers its length.

Let \(F=\mathbb Q(\alpha_1,\alpha_2,\beta)\) and \(d_F=[F:\mathbb Q]\). Theorem 2.8 of the height lesson, with the three fixed logarithmic Weil heights, gives

\[
 \log|\Delta|
 \geq-d_F\left(
 \log\ell(P)+e_1h(\alpha_1)+e_2h(\alpha_2)+e_3h(\beta)
 \right).
 \tag{6.12}
\]

This is the general polynomial-value bound with coefficient exponent \(d_F\); no stronger coefficient exponent is being substituted. From (6.4)–(6.5) and (6.11),

\[
 \begin{aligned}
 e_1,e_2&\leq\frac{2N^4}{\log N},\\
 e_3&\leq N^3\log N,\\
 \log\ell(P)&\leq2N^2\log N+N^3\log N\log(4N).
 \end{aligned}
\]

The last two expressions are \(O(N^4/\log N)\), since every fixed power of \(\log N\) is \(o(N)\). All field degrees and heights in (6.12) are fixed. This proves the first inequality in (6.10) with a fixed \(c\). Taking also \(\log N\geq2c\) gives the second. \(\square\)

**Proof of Theorem 6.1.** Fix any logarithm \(A\) of the stated \(\alpha\). Suppose the resulting \(\alpha_2=e^{\beta A}\) were algebraic. Proposition 6.5 supplies a nonzero minor for every sufficiently large integer \(N\). Proposition 6.7 makes its logarithmic modulus at most \(-N^4\), whereas Proposition 6.8 makes it at least \(-N^4/2\). For positive \(N\), these inequalities are incompatible. This disproves algebraicity of the chosen value. Since the proof did not restrict the chosen logarithm, every value is transcendental. \(\square\)

The sizes can be summarized without hiding either estimate.

| Parameter or quantity | Size and purpose |
|---|---|
| Polynomial degrees | \(K=\lfloor N\log N\rfloor\), \(L=\lfloor N/\log N\rfloor\) |
| Number of columns | \(M=KL\sim N^2\), at most \(N^2\) |
| Number of grid rows | \(4N^2\) |
| Scaling zero order | \(M(M-1)/2\sim N^4/2\) |
| Ratio of radii | \(R/\rho=e^5\), independent of \(N\) |
| Analytic upper estimate | \(\log\lvert\Delta\rvert\leq-N^4\) |
| Arithmetic lower estimate | \(\log\lvert\Delta\rvert\geq-cN^4/\log N\) |

The \(N^4\) analytic gain comes from distinct Taylor degrees in a determinant, rather than from finding \(N^4\) evaluation points. The slower \(N^4/\log N\) arithmetic cost is the reason for the asymmetric degree choices.

## 6. Powers and fixed logarithms

### Corollary 6.9. Independence of two logarithms

Let \(\alpha_1,\alpha_2\) be nonzero algebraic numbers and fix logarithms \(\lambda_1,\lambda_2\). If the logarithms are linearly independent over \(\mathbb Q\), they are linearly independent over the algebraic numbers. Equivalently, if \(\lambda_2\ne0\), then an irrational ratio \(\lambda_1/\lambda_2\) is transcendental. Both formulations are equivalent to Theorem 6.1.

**Proof.** Rational independence makes both logarithms nonzero. The two bases cannot both be \(1\): in that case their logarithms would be integer multiples of \(2\pi i\), hence rationally dependent. Relabel if necessary so that \(\alpha_2\ne1\).

Suppose an algebraic-coefficient relation

\[
 c_1\lambda_1+c_2\lambda_2=0
\]

were nontrivial. Both coefficients must be nonzero, and

\[
 \gamma=\lambda_1/\lambda_2=-c_2/c_1
\]

would be algebraic and irrational. Theorem 6.1, with base \(\alpha_2\), fixed logarithm \(\lambda_2\) and exponent \(\gamma\), would make

\[
 e^{\gamma\lambda_2}=e^{\lambda_1}=\alpha_1
\]

transcendental, a contradiction. This proves independence over the algebraic numbers.

If \(\lambda_2\ne0\), rational dependence of the two logarithms is equivalent to rationality of their ratio. Indeed, a nontrivial rational relation must have a nonzero coefficient of \(\lambda_1\), since a relation involving only \(\lambda_2\) cannot vanish. Thus the irrational ratio case has rationally independent logarithms, and their linear independence over the algebraic numbers forces the ratio to be transcendental.

Conversely, suppose the irrational-ratio assertion is given. If a value \(e^{\beta A}\) in Theorem 6.1 were algebraic, \(A\ne0\) and \(\beta A\) would be fixed logarithms of two nonzero algebraic numbers, with ratio \(\beta\). That ratio is irrational and algebraic, contradicting the assertion. The logarithms formulation follows by the same algebraic relation calculation, so the three forms are equivalent. \(\square\)

This is linear independence, not the unproved general assertion that logarithms of multiplicatively independent algebraic numbers are algebraically independent. The theorem forbids a nontrivial algebraic **linear** relation between two rationally independent logarithms.

**Examples.** With positive real logarithms, \(2^{\sqrt2}\) is transcendental. Taking the fixed logarithm \(\log(-1)=i\pi\) and exponent \(-i\) gives

\[
 (-1)^{-i}=e^\pi,
\]

so \(e^\pi\) is transcendental. The same branch and the algebraic irrational exponent \(-i\sqrt{163}\) give the transcendence of \(e^{\pi\sqrt{163}}\). Its numerical proximity to an integer, explained by complex multiplication in a later lesson, is compatible with this exact conclusion.

The ratio \(\log3/\log2\) is irrational: a rational equality \(p/q\), with \(q>0\), would give \(3^q=2^p\), contrary to prime factorization. Corollary 6.9 therefore makes \(\log_2 3\) transcendental. The reciprocal ratio \(\log2/\log3\) is likewise transcendental, since a nonzero algebraic reciprocal would make the original ratio algebraic.

Finally, let

\[
 t=(\sqrt2)^{\sqrt2}
\]

using its positive real value. It is transcendental, but with the positive real logarithm of \(t\),

\[
 t^{\sqrt2}
 =\exp\bigl(\sqrt2\,(\sqrt2\log\sqrt2)\bigr)=2.
\]

This calculation specifies both logarithms. Iterated power identities with arbitrary unrelated complex branches cannot be used in its place.

## 7. Compare with an auxiliary function

The same grid certificate answers a second construction problem. Instead of choosing a nonzero minor and making it small, choose a nonzero coefficient vector that forces many values of one function to vanish. The number-field Siegel lemma controls that vector; the larger grid then locates a nonzero value. The following proof gives all the estimates for Schneider's construction; Waldschmidt's *Transcendence Methods*, §3.1, presents Schneider's auxiliary function \(P(z,\alpha^z)\) with zeros at the points \(h_1+h_2\beta\).

Track the two quantities separately: the determinant argument gains order \(N^4\) and pays arithmetic cost \(N^4/\log N\); this function argument gains order \(N^2\) and pays \(N^2/\log N\). Both contradictions use a diverging ratio, rather than the absolute size of the exponents. The larger determinant gain therefore does not make the auxiliary function argument incomplete.

Again suppose the three numbers \(\alpha_1,\alpha_2,\beta\) were algebraic, and keep the parameters \(K,L,M\) in (6.4). Put \(T=\lfloor N/2\rfloor\). Seek integral coefficients in their number field \(F\), not all zero, for

\[
 f(z)=\sum_{u<K,v<L}a_{uv}z^ue^{vAz},
 \qquad f(r+s\beta)=0\quad(0\leq r,s<T).
 \tag{6.13}
\]

There are \(T^2\sim N^2/4\) equations in \(M\sim N^2\) unknowns, so

\[
 \frac{T^2}{M-T^2}\longrightarrow\frac13.
\]

Let an integer \(d>0\) clear the denominators of \(\alpha_1,\alpha_2,\beta\), and set

\[
 B=\max(1,\overline{\alpha_1},\overline{\alpha_2}),
 \qquad B_\beta=\max(1,\overline\beta).
\]

Multiplying the equations by \(d^{K+2LT}\) makes their coefficients integral. Their houses are at most

\[
 d^{K+2LT}(2TB_\beta)^K B^{2LT},
\]

whose logarithm is \(O(N^2/\log N)\): the other term \(K\log(2TB_\beta)=O(N(\log N)^2)\) is of that order as well. Lemma 5.2 gives coefficients with

\[
 \log\max(1,\overline{a_{uv}})
 \leq c_1\frac{N^2}{\log N}
 \tag{6.14}
\]

for a fixed \(c_1\) and all sufficiently large \(N\). This follows by taking logarithms in its bound: the Siegel exponent stays bounded, and \(\log(CM)=O(\log N)\).

The associated polynomial \(P(X,Y)=\sum a_{uv}X^uY^v\) is nonzero. Lemma 6.4 with all rectangle parameters \(N\), as in the rank proof, supplies \(0\leq r_0,s_0<2N\) for which

\[
 \delta=f(w)\ne0,\qquad w=r_0+s_0\beta.
\]

In particular \(f\) is not identically zero. Set \(\rho=2N(1+|\beta|)\) and \(R=5\rho\). All the \(T^2\) initial zero points and the point \(w\) have modulus at most \(\rho\); the initial points are distinct. Lemma 5.7 gives

\[
 |\delta|\leq|f|_R\left(\frac{2\rho}{R-\rho}\right)^{T^2}
 =|f|_R\,2^{-T^2}.
\]

On the outer circle, (6.14) and the elementary growth estimate give

\[
 \log|f|_R
 \leq\log M+c_1N^2/\log N+K\log R+LR|A|
 =O(N^2/\log N)=o(N^2).
\]

Since \(T^2/N^2\to1/4\),

\[
 \log|\delta|\leq-\frac1{10}N^2
 \tag{6.15}
\]

for sufficiently large \(N\); the limiting negative coefficient is \(-\log2/4<-1/10\).

On the arithmetic side,

\[
 \Theta=d^{K+4NL}\delta
\]

is a nonzero algebraic integer, because \(r_0+s_0<4N\), \(u<K\) and \(v<L\). For every embedding of \(F\), its modulus is at most

\[
 d^{K+4NL}M\exp(c_1N^2/\log N)
 (4NB_\beta)^K B^{4NL}.
\]

The logarithm of this expression is \(O(N^2/\log N)\). Taking the nonzero integral norm, isolating the chosen embedding, and undoing the denominator as in the six exponentials proof, yields

\[
 \log|\delta|\geq-c_2\frac{N^2}{\log N}
 \tag{6.16}
\]

for a fixed \(c_2\). For \(\log N>10c_2\), (6.15) and (6.16) contradict one another. This completes the auxiliary-function proof too.

Here the polynomial zero estimate chooses a nonzero value in a larger but fixed grid. Laurent's proof instead applies it before constructing the determinant, obtaining a nonzero maximal minor directly. Gelfond's method develops vanishing of auxiliary functions and their derivatives; Baker's later work extends that direction to several logarithms. Schneider's value-grid construction also leads to differential-field transcendence criteria, developed in the next lesson. The historical comparison does not require importing either original 1934 paper as an unproved mathematical input.

## 8. Exercises: test the certificates

1. **Easy — choose evaluation points.** Compute the evaluation determinants for \(1,Y^2\) at \((1,-1)\) and \((1,2)\). Explain why three distinct nonzero evaluation points guarantee a nonzero two-column minor, and why two arbitrary points do not. Which part of Lemma 6.4 uses this choice?

2. **Medium — watch columns coalesce.** For \(1,z,z^2\) at \(t\xi_1,t\xi_2,t\xi_3\), calculate the determinant and its order at \(t=0\) when the \(\xi_j\) are distinct. Then prove the full Lemma 6.6 by the scaling variable, including its outer radius and \(M=1\).

3. **Hard — certify the large minor.** Give the full proof of Proposition 6.5: infinite-order generator, sparse-power evaluation, translated determinant, exact degree, and too many distinct roots. Identify why making the additive grid merely as large as that degree would fail.

4. **Medium — keep track of logarithms.** (a) Prove the equivalence between Theorem 6.1 and transcendence of an irrational ratio of fixed logarithms, including a base equal to \(1\). (b) Specify the branch proving transcendence of \(e^{\pi\sqrt{163}}\), and explain why an almost-integer value changes nothing. (c) Describe every complex solution of \(e^{x\log2}=3\) and prove that none is algebraic.

5. **Hard — compare the construction sizes.** Set instead \(K=L=N\) and keep the determinant radius \(R=e^5\rho\). Does the elementary growth estimate become \(o(N^2)\)? Explain why this loses the uniform argument for arbitrary fixed \(A,\beta\). Recover the two vanishing gains and arithmetic costs for the actual choices in both proofs.

## 9. Solutions

1. The determinants are \((-1)^2-1^2=0\) and \(2^2-1^2=3\). If every two-column minor on a three-point set vanished, the two evaluation rows would be dependent, making a nonzero polynomial \(a+bY^2\) vanish at all three points. Its degree is at most two, a contradiction. Lemma 6.4 uses such a nonsingular evaluation matrix to ensure that the leading coefficient of its translated determinant polynomial is nonzero; it does not assume that an arbitrarily selected matrix works.

2. The Vandermonde determinant is \(t^3\prod_{i<j}(\xi_j-\xi_i)\), of order three, the sum \(0+1+2\). Let \(H(t)=\det(f_i(t\xi_j))\). In its Taylor expansion, a nonzero determinant term must choose different nonnegative degrees from its \(M\) rows; coinciding degrees give identical power rows. The smallest possible sum is \(T=M(M-1)/2\). Every coefficient below this degree is zero; the computation uses only finitely many Taylor coefficients for each total degree. The function is analytic through \(|t|\leq R/\rho\), because \(|t\xi_j|\leq R\) there. On its outer circle the determinant expansion bounds it by \(M!S^M\). Applying Lemma 5.4 from radius \(R/\rho\) to radius \(1\) gives \(|H(1)|\leq(\rho/R)^T M!S^M\). If \(M=1\), then \(T=0\) and the statement is simply the original bound on the one function; no positive-order zero is asserted.

3. If both multiplicative generators were roots of unity, integers \(m,n>0\) would satisfy \(mA=2\pi i k\), \(n\beta A=2\pi i\ell\), with \(k\ne0\); this would force \(\beta=m\ell/(nk)\in\mathbb Q\). Hence at least one generator has infinite order, and its first \(N\) powers give distinct elements of the first multiplicative rectangle. The additive rectangle has \(N^2\) distinct elements because \(\beta\notin\mathbb Q\).

   Suppose the matrix columns were dependent. Their coefficients define a nonzero polynomial \(P(X,Y)\) with degrees less than \(K,L\), vanishing on the full grid. Write \(P=\sum_{i=1}^mQ_i(X)Y^{k_i}\), with \(Q_i\ne0\), distinct \(0\leq k_i<L\), and \(m\leq L\). Evaluation of these monomials at \(L\) distinct nonzero multiplicative values has row rank \(m\): a row relation would give a nonzero polynomial of degree below \(L\) with \(L\) roots. Select \(m\) values \(b_j=\alpha_1^{r_j}\alpha_2^{s_j}\) for which the square evaluation determinant is nonzero, and put \(a_j=r_j+s_j\beta\), with \(0\leq r_j,s_j<N\).

   The polynomial

   \[
   D(X)=\det(Q_i(X+a_j)b_j^{k_i})_{j,i}
   \]

   has leading coefficient equal to the product of the nonzero leading coefficients of the \(Q_i\) times the nonzero selected evaluation determinant. Thus \(D\ne0\) and \(\deg D=\sum_i\deg Q_i\leq(K-1)m\leq(K-1)L\). For every second pair \(0\leq r',s'<N\), let \(a'=r'+s'\beta\) and \(b'=\alpha_1^{r'}\alpha_2^{s'}\). The summed pairs satisfy \(r'+r_j,s'+s_j\leq2N-2\), so the assumed vanishing makes \(((b')^{k_i})_i\) a nonzero vector in the kernel of the matrix defining \(D(a')\). Therefore \(D(a')=0\). This gives \(N^2\geq KL>(K-1)L\) distinct roots of \(D\), contradicting its degree. There was no column relation, and rank is \(KL\). A nonzero polynomial of degree \(D\) can have exactly \(D\) distinct roots; the final contradiction needs strictly more.

4. (a) Rational independence of two logarithms \(\lambda_1,\lambda_2\), with \(\lambda_2\ne0\), is equivalent to irrationality of their ratio. If both bases were \(1\), their logarithms would be \(2\pi i\) times integers, so their ratio, when defined, would be rational. In the irrational case at least one base differs from \(1\); choose its nonzero logarithm as denominator. If the corresponding ratio \(\gamma\) were algebraic irrational, Theorem 6.1 would make the other base \(e^{\gamma\lambda}\) transcendental. If the denominator was changed by exchanging the logarithms, take the reciprocal: a nonzero irrational algebraic ratio has a nonzero irrational algebraic reciprocal. Thus the original ratio is transcendental. Conversely, an assumed algebraic value of \(e^{\beta A}\) under the hypotheses of Theorem 6.1 gives logarithms \(\beta A\) and \(A\ne0\) of algebraic numbers, with irrational algebraic ratio \(\beta\). The ratio assertion rules this out for each fixed logarithm \(A\). A zero numerator simply gives ratio \(0\), so is outside the irrational case.

   (b) Choose \(A=i\pi\), a logarithm of \(-1\), and \(\beta=-i\sqrt{163}\). The base \(-1\) is algebraic and differs from \(0,1\), while \(\beta\) is algebraic, satisfies \(X^2+163=0\), and is not rational. Therefore

   \[
   e^{\beta A}=e^{\pi\sqrt{163}}
   \]

   is transcendental. A numerical approximation by an integer, however close, does not give equality or an algebraic equation. The theorem is an exact statement independent of that approximation.

   (c) The complex exponential equation gives

   \[
   x=\frac{\log3+2\pi i k}{\log2},\qquad k\in\mathbb Z.
   \]

   A rational solution would be real; writing it \(p/q\), \(q>0\), would yield \(2^p=3^q\), which is impossible by prime factorization. If any displayed solution were algebraic, it would therefore be algebraic irrational. Theorem 6.1 with base \(2\) and its fixed real logarithm would then make \(2^x\) transcendental, contradicting \(2^x=3\). This argument includes every integer \(k\), and does not depend on identities for powers with different logarithms.

5. With equal degrees, \(LR|A|/N^2=2e^5(1+|\beta|)|A|\), which does not tend to zero since \(A\ne0\). The bound remains of order \(N^2\) per function and cannot uniformly be absorbed into the fixed negative determinant coefficient for all \(A,\beta\). This shows failure of that estimate, not impossibility of all equal-degree approaches. For the actual degrees, \(K\log R=O(N(\log N)^2)\) and \(LR|A|=O(N^2/\log N)\), both \(o(N^2)\). The determinant has coalescence order \(M(M-1)/2\sim N^4/2\), while its arithmetic logarithmic cost is \(O(N^4/\log N)\). The auxiliary function has \(T^2\sim N^2/4\) prescribed distinct zeros, gives the gain \(T^2\log2\), and has coefficient, growth and norm costs \(O(N^2/\log N)\). In either case their ratio tends to infinity.

## References

- Michel Waldschmidt, [*Linear Independence of Logarithms of Algebraic Numbers*](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/LIL.pdf), IMSc Report 116, The Institute of Mathematical Sciences, Madras, 1992: Theorem 1.2 for the two-logarithm form of the Gelfond–Schneider theorem; Chapter 2 for Schneider's method with interpolation determinants and a zero estimate in the real case; Chapters 4–5 for interpolation determinants and zero estimates in general.
- Michel Waldschmidt, [*Transcendence Methods*](https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/QueensPaper52.pdf), Queen's Papers in Pure and Applied Mathematics 52, Queen's University, Kingston, 1979: §2.1 for Gelfond's solution of Hilbert's seventh problem and §3.1 for Schneider's. Michel Waldschmidt, [*Auxiliary functions in transcendence proofs*](https://arxiv.org/abs/0908.4024), arXiv:0908.4024, 2009, §§2.3 and 3.1.2, for the history from Hilbert's problem to the work of Gelfond, Kuzmin and Schneider.
- J.-H. Evertse, [*Diophantine Approximation*, Chapter 4: Transcendence results](https://pub.math.leidenuniv.nl/~evertsejh/dio19-4.pdf), Leiden course notes, §4.3, Theorem 4.16 and Corollary 4.18, for the theorem and its two-logarithm formulation with arbitrary determinations of the logarithms; §4.4, Theorem 4.21, for Schneider's proof when \(\alpha\) and \(\beta\) are real.
