# Nonvanishing at prime scales

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The arithmetic lower bound of [Denominators at the odd primes](denominators-at-the-odd-primes.md) concerns determinants \(\Delta_N\) that are not zero; a vanishing determinant gives no information. This lesson proves, still under the hypothesis that Catalan's constant \(G\) is rational, that \(\Delta_p\ne0\) for every sufficiently large prime \(p\), with the exact valuation

\[
v_p(\Delta_p)=-96p.
\]

The determinants are mixed and signed, so there is no positivity to exploit. Instead the proof is arithmetic. When the scale \(N\) equals the prime \(p\), Frobenius identifies the reduction modulo \(p\) of the scaled \(48p\times48p\) matrix with a Kronecker product built from a fixed rational \(49\times48\) matrix and a \(p\times p\) change of basis between two families of palindromic polynomials. The determinant then factors into powers of three fixed \(48\times48\) determinants, and a finite computation shows that these are nonzero.

We use the leading layer, Proposition 4.1 of [Denominators at the odd primes](denominators-at-the-odd-primes.md), and the rows and arrays of [Chebyshev rows and mixed moments](chebyshev-rows-and-mixed-moments.md). A basic reference is [OpenAI-Catalan].

## 1. The statement

**Proposition 1.1** (nonvanishing). Assume \(G\) is rational. For every sufficiently large prime \(p\), the determinant with scale \(N=p\) satisfies \(v_p(\Delta_p)=-96p\). In particular \(\Delta_p\ne0\).

Underlined rows are the rows of scale \(N=1\): \(\underline P_r\) and \(\underline D_r\) are formed with

\[
n_0=48,\quad b_0=7,\quad q_0=g_0=4,\quad h_0=2,\quad L_0=59,\quad C_0=63,\quad H_0=65,
\]

for \(0\le r\le48\); the **auxiliary row** \(r=48\) is defined by the same formulas (3.1) of the rows lesson, although it is not a row of the scale-one determinant. For \(0\le r\le48\) and \(0\le k<48\) put

\[
\mathcal B(r,k)=\sum_{j=0}^4(-1)^j\binom4j\Bigl\{M^0(\underline P_r,7+k+j)-\frac32Z^0(\underline D_r,7+k+j)\Bigr\},
\tag{1.1}
\]

a fixed rational \(49\times48\) matrix, and

\[
\mathcal B_0=\bigl(\mathcal B(r,k)\bigr)_{0\le r,k<48},\qquad\mathcal B_1=\bigl(\mathcal B(r+1,k)\bigr)_{0\le r,k<48}.
\]

**Proposition 1.2** (the fixed certificate). \(\det\mathcal B_0\ne0\), \(\det(\mathcal B_0+\mathcal B_1)\ne0\) and \(\det(\mathcal B_0-\mathcal B_1)\ne0\).

Section 5 gives the finite computation proving Proposition 1.2. Sections 2–4 show that it implies Proposition 1.1.

## 2. Two palindromic bases

Let \(p\) be an odd prime and work over \(\mathbf F_p\). The space

\[
\mathcal P_p=\{Q\in\mathbf F_p[w]:\ \deg Q\le2p-2,\ w^{2p-2}Q(1/w)=Q(w)\}
\]

of palindromic polynomials has dimension \(p\): the coefficients of \(w^0,\dots,w^{p-1}\) determine the rest. For \(0\le\ell,i<p\) put

\[
U_\ell(w)=(2w)^\ell(1+w^2)^{p-1-\ell},\qquad Q_i(w)=w^i\sum_{j=0}^{p-1-i}w^{2j}.
\]

Both lie in \(\mathcal P_p\), and their lowest terms are \(2^\ell w^\ell\) and \(w^i\). By triangularity each family is a basis, and the matrix \(\mathbf a=(a_{\ell i})\) defined by \(Q_i=\sum_\ell a_{\ell i}U_\ell\) satisfies

\[
a_{\ell i}=0\ (\ell<i),\qquad a_{ii}=2^{-i},\qquad\det\mathbf a=2^{-p(p-1)/2}\ne0.
\tag{2.1}
\]

Let \(Q'_0=0\) and \(Q'_i=Q_{p-i}\) for \(1\le i<p\), and write \(Q'_i=\sum_\ell b_{\ell i}U_\ell\). Then

\[
\mathbf b=\mathbf a\Pi,\qquad \Pi e_0=0,\quad \Pi e_i=e_{p-i}\ (1\le i<p).
\tag{2.2}
\]

**Lemma 2.1.** With \(t=2w/(1+w^2)\), \(f=(1-w^2)/(1+w^2)\) and \(E(t)=(1-t^2)^{(p-1)/2}\), for \(0\le i<p\),

\[
E(t)\,w^i=\sum_{\ell=0}^{p-1}t^\ell\bigl(a_{\ell i}+b_{\ell i}\,w^p\bigr)\qquad\text{in }\mathbf F_p(w).
\]

**Proof.** As rational functions, \(Q_i=w^i(1-w^{2(p-i)})/(1-w^2)\) and \(Q'_i=w^{p-i}(1-w^{2i})/(1-w^2)\) (the latter also for \(i=0\)). Hence

\[
Q_i+w^pQ'_i=w^i\frac{1-w^{2p}}{1-w^2}=w^i\sum_{j=0}^{p-1}w^{2j}=w^i(1-w^2)^{p-1},
\]

because \(\binom{p-1}j\equiv(-1)^j\pmod p\). Divide by \((1+w^2)^{p-1}\): the right side becomes \(w^if^{p-1}=w^iE(t)\), since \(1-t^2=f^2\). On the left, \(U_\ell/(1+w^2)^{p-1}=t^\ell\), so the expansions in the basis \(U_\ell\) give the claim. \(\square\)

## 3. Frobenius

Now take the scale \(N=p\), so \(n=48p\), \(C=63p\), \(h=2p\) and \(g=4p\). Write each row index as \(r=pr_0+i\) with \(0\le r_0<48\), \(0\le i<p\). In \(\mathbf F_p(w)\) put \(t'=t^p\), \(w'=w^p\), \(f'=f^p\); by Frobenius, \(t'=2w'/(1+w'^2)\) and \(f'=(1-w'^2)/(1+w'^2)\), so \(t',w',f'\) are related exactly as \(t,w,f\) are.

**Lemma 3.1** (Frobenius row identities). Over \(\mathbf F_p\), for \(r=pr_0+i\),

\[
tP_r(t)E(t)=\sum_{\ell=0}^{p-1}t^\ell\,t'\bigl(a_{\ell i}\underline P_{r_0}(t')+b_{\ell i}\underline P_{r_0+1}(t')\bigr),\qquad
D_r(t)=\sum_{\ell=0}^{p-1}t^\ell\bigl(a_{\ell i}\underline D_{r_0}(t')+b_{\ell i}\underline D_{r_0+1}(t')\bigr).
\]

**Proof.** In characteristic \(p\), \((1-t)^{2p}=(1-t')^2\), \(t^{63p}=t'^{63}\) and \(w^{pr_0-4p}=w'^{r_0-4}\). So, with \(\underline R_j(t,w)=(1-t)^2t^{62}w^{j-4}\),

\[
tR_rE(t)=(1-t')^2t'^{63}w'^{r_0-4}\,E(t)w^i=\sum_\ell t^\ell\,t'\bigl(a_{\ell i}\underline R_{r_0}(t',w')+b_{\ell i}\underline R_{r_0+1}(t',w')\bigr)
\]

by Lemma 2.1; the factor \(w'\) in the second term produces the successor row \(r_0+1\le48\). Now separate the two parts with respect to the involution \(w\mapsto1/w\), which fixes \(t\) and \(t'\) and negates \(f\) and \(f'\). The field \(\mathbf F_p(w)\) is the direct sum of the fixed field \(\mathbf F_p(t)\) and \(f'\,\mathbf F_p(t)\), since \(f'\ne0\) is anti-invariant and the extension has degree two. From \(R_r=P_r-(f/t)D_r\) and \(fE=f^p=f'\) we get \(tR_rE=tP_rE-f'D_r\), and likewise \(t'\underline R_j=t'\underline P_j-f'\underline D_j\). Comparing invariant parts gives the first identity; comparing anti-invariant parts and cancelling \(-f'\) gives the second. Both are identities of polynomials in \(t\), as the map \(\mathbf F_p[t]\to\mathbf F_p(w)\) is injective. \(\square\)

The auxiliary row is needed only for \(r_0=47\); its polynomials have lowest degrees \(18\) and \(19\), lower than those of the other base rows. This is consistent with the original rows: for \(r=47p+i\) with \(i>0\), the successor contribution starts in degree \(19p+(p-i)=20p-i\), which is also where \(tP_r\) and \(D_r\) start, since \(|r-g|=43p+i\) and \(C-(43p+i)=20p-i\).

## 4. The reduced matrix and its determinant

Fix \(p>260\) with \(p\nmid\operatorname{den}G\). Then \(p>2\sqrt{65p}=2\sqrt H\), so Proposition 4.1 of [Denominators at the odd primes](denominators-at-the-odd-primes.md) applies with this \(p\) and \(N=p\). Every polynomial has a unique expression \(\sum_\ell t^\ell A_\ell(t^p)\); by Lemma 3.1 the extracted vectors of that proposition are

\[
P'_u=[t'^u]\bigl(a_{\ell i}\underline P_{r_0}+b_{\ell i}\underline P_{r_0+1}\bigr),\qquad D'_u=[t'^u]\bigl(a_{\ell i}\underline D_{r_0}+b_{\ell i}\underline D_{r_0+1}\bigr),
\]

with \(P'_{-1}=0\). Therefore, for a raw column \(j=kp+\ell\),

\[
p^2F_{kp+\ell}(pr_0+i)\equiv a_{\ell i}\Bigl\{M^0(\underline P_{r_0},k)-\frac32Z^0(\underline D_{r_0},k)\Bigr\}+b_{\ell i}\Bigl\{M^0(\underline P_{r_0+1},k)-\frac32Z^0(\underline D_{r_0+1},k)\Bigr\}\pmod p.
\tag{4.1}
\]

The base arrays have denominators with prime factors at most \(65\), so their reductions exist.

**Columns.** Write a column index as \(k=\ell+pk_0\) with \(0\le\ell<p\) and \(0\le k_0<48\). In \(\mathbf F_p[s]\),

\[
s^{7p+k}(1-s)^{4p}=s^\ell(s^p)^{7+k_0}(1-s^p)^4.
\]

After multiplying the raw entries by \(p^2\), which makes them \(p\)-integral, differences of filter coefficients divisible by \(p\) contribute zero modulo \(p\). So the scaled filtered entry in row \(pr_0+i\) and column \(\ell+pk_0\) is congruent to \(\sum_{v=0}^4(-1)^v\binom4v\,p^2F_{\ell+p(7+k_0+v)}(pr_0+i)\), and by (4.1) to

\[
a_{\ell i}\,\mathcal B(r_0,k_0)+b_{\ell i}\,\mathcal B(r_0+1,k_0).
\]

**The determinant.** Order rows by \((i,r_0)\) and columns by \((\ell,k_0)\). The reduction of the scaled \(48p\times48p\) matrix \(p^2\mathcal F_p\) of \(\Delta_p\) is then

\[
\mathcal L_p=\mathbf a^T\otimes\mathcal B_0+\mathbf b^T\otimes\mathcal B_1=\bigl(I_p\otimes\mathcal B_0+\Pi^T\otimes\mathcal B_1\bigr)\bigl(\mathbf a^T\otimes I_{48}\bigr),
\]

using \(\mathbf b^T=\Pi^T\mathbf a^T\) and the mixed product rule for Kronecker products. The matrix \(\Pi\) is symmetric. It has the eigenvector \(e_0\) with eigenvalue \(0\), and for each of the \((p-1)/2\) pairs \(\{i,p-i\}\) the eigenvectors \(e_i+e_{p-i}\) (eigenvalue \(1\)) and \(e_i-e_{p-i}\) (eigenvalue \(-1\)); these form a basis because \(2\) is invertible. Conjugating the first factor by this change of basis on the \(p\)-dimensional factor gives a block diagonal matrix, and

\[
\det\mathcal L_p=(\det\mathbf a)^{48}\,\det\mathcal B_0\,\det(\mathcal B_0+\mathcal B_1)^{(p-1)/2}\det(\mathcal B_0-\mathcal B_1)^{(p-1)/2}
\tag{4.2}
\]

over \(\mathbf F_p\). Returning to the original orders of rows and columns changes at most the sign.

**Proof of Proposition 1.1, given Proposition 1.2.** Let \(\mathcal E\) be the finite set consisting of \(2\), the primes dividing \(\operatorname{den}G\), the primes dividing a denominator of an entry of \(\mathcal B\), and the primes dividing the numerator or the denominator of one of the three nonzero rational determinants of Proposition 1.2. For a prime \(p>260\) outside \(\mathcal E\), the three matrices reduce to invertible matrices over \(\mathbf F_p\), and (2.1) and (4.2) give \(\det\mathcal L_p\ne0\). Since \(p^2\mathcal F_p\) has entries in \(\mathbb Z_{(p)}\) and reduces to \(\mathcal L_p\) up to permutations, \(p^{2n}\Delta_p=\det(p^2\mathcal F_p)\) is a unit of \(\mathbb Z_{(p)}\), that is \(v_p(\Delta_p)=-2n=-96p\). \(\square\)

## 5. The certificate

The entries of (1.1) are produced by the following rational arithmetic, which uses only denominators with prime factors at most \(65\).

1. *Moments.* \(m_0=2\), \(m_i=0\) for odd \(i\), and \(m_i=i\,m_{i-2}/(i+1)\) for even \(2\le i\le64\).
2. *Boundary arrays.* \(k^-_0=0\), \(k^-_1=2\), \(k^+_0=k^+_1=0\), and \(k^-_d=\bigl((d-1)k^-_{d-2}+m_{d-2}+m_{d-1}\bigr)/d\) for \(2\le d\le64\), \(k^+_d=\bigl((d-2)k^+_{d-2}+2/(d-1)\bigr)/(d-1)\) for \(2\le d\le58\).
3. *The array \(M^0\).* For \(0\le i\le64\), \(0\le j\le58\): \(Y_{i0}=k^-_i\), \(Y_{0j}=k^+_j\), and \(Y_{ij}=Y_{i-1,j-1}-m_{i-1}/j\) for \(i,j\ge1\). Then \(Y_{ij}=M^0(i,j)\).
4. *The array \(\frac32Z^0\).* With \(B^{(d)}_i=\sum_{u\le i}u^{-d}\): \(J_{ii}=-\frac32B^{(2)}_i\) and \(J_{ij}=\frac32(B^{(1)}_i-B^{(1)}_j)/(i-j)\) for \(i\ne j\).
5. *Rows.* Put \(E_0=t^{62}\), \(E_1=t^{61}\), \(I_0=0\), \(I_1=t^{62}\), and \(S_m=2S_{m-1}/t-S_{m-2}\) for \(2\le m\le44\) and \(S=E,I\); thus \(E_m=t^{62}T_m(1/t)\) and \(I_m=t^{62}U_{m-1}(1/t)\). For \(0\le r\le48\) let \(u=|r-4|\), \(y_r=(1-t)^2E_u\) and \(z_r=\operatorname{sgn}(r-4)(1-t)^2I_u\); these are \(\underline P_r\) and \(\underline D_r\).
6. *Contraction.* For \(7\le j\le58\), \(v_r(j)=\sum_{i=0}^{64}\bigl([t^i]y_r\,Y_{ij}-[t^i]z_r\,J_{ij}\bigr)\). Replace \(v_r\) four times by its consecutive differences \(v(j)-v(j+1)\); the resulting \(48\) numbers form row \(r\) of \(\mathcal B\).

Since \(101\) does not divide any of these denominators, the whole construction can be carried out in \(\mathbf F_{101}\), and gives the reduction of \(\mathcal B\) modulo \(101\).

**Proof of Proposition 1.2.** For \(\sigma\in\{0,1,-1\}\), take the rows \(\mathcal B(i,\cdot)+\sigma\mathcal B(i+1,\cdot)\), \(0\le i<48\), in increasing order, reduced modulo \(101\), and perform Gaussian elimination: at step \(i\), if the entry in column \(i\) of row \(i\) is zero, swap row \(i\) with the first later row having a nonzero entry there; record the pivot and clear column \(i\) below it. For \(\sigma=0\) and \(\sigma=-1\) no swaps occur; for \(\sigma=1\) the only swaps are of rows \(30,31\) and of rows \(45,46\) (counting from \(0\)) at the corresponding steps. The pivots are:

\(\sigma=0\): 60, 68, 62, 79, 47, 32, 69, 57, 30, 72, 35, 66, 43, 20, 85, 48, 88, 4, 77, 54, 60, 79, 26, 68, 83, 39, 40, 65, 1, 68, 78, 24, 15, 98, 32, 22, 94, 9, 99, 10, 15, 75, 4, 2, 25, 53, 90, 79.

\(\sigma=1\): 38, 51, 90, 70, 5, 21, 88, 55, 45, 20, 35, 41, 77, 10, 18, 25, 76, 14, 38, 72, 6, 66, 56, 35, 83, 58, 56, 11, 17, 20, 30, 24, 28, 11, 25, 70, 79, 99, 66, 38, 4, 41, 63, 91, 63, 17, 90, 98.

\(\sigma=-1\): 82, 92, 26, 87, 21, 74, 87, 88, 88, 3, 14, 23, 38, 58, 36, 20, 26, 33, 94, 74, 78, 45, 93, 86, 73, 66, 45, 30, 61, 3, 88, 27, 20, 58, 69, 48, 78, 39, 48, 1, 66, 18, 86, 93, 52, 92, 39, 77.

All pivots are nonzero, so the three matrices are invertible modulo \(101\), hence their rational determinants are nonzero. \(\square\)

The computation is finite and completely specified; any computer algebra system reproduces it in a fraction of a second. The modulus \(101\) plays no role beyond this certificate.

## 6. Exercises

**Exercise 6.1 (easy).** For \(p=3\), write down \(U_0,U_1,U_2\) and \(Q_0,Q_1,Q_2\), and compute the matrix \(\mathbf a\).

**Exercise 6.2 (easy).** Show that \(\Pi\) is symmetric and that \(\Pi^2\) is the identity on the span of \(e_1,\dots,e_{p-1}\).

**Exercise 6.3 (medium).** Prove the mixed product rule \((X\otimes Y)(X'\otimes Y')=XX'\otimes YY'\) and deduce \(\det(X\otimes I_m)=(\det X)^m\) for a \(k\times k\) matrix \(X\).

**Exercise 6.4 (medium).** Explain why Proposition 1.1 gives nonvanishing only along primes \(N=p\), and why that suffices for the final contradiction of the course.

## 7. Solutions

**6.1.** \(U_0=(1+w^2)^2=1+2w^2+w^4\), \(U_1=2w(1+w^2)=2w+2w^3\), \(U_2=4w^2\); \(Q_0=1+w^2+w^4\), \(Q_1=w+w^3\), \(Q_2=w^2\). Modulo \(3\): \(Q_2=4^{-1}U_2=U_2\) (as \(4\equiv1\)), \(Q_1=2^{-1}U_1=2U_1\), and \(Q_0=U_0+aU_1+bU_2\) with \(Q_0-U_0=-w^2\), so \(Q_0=U_0-U_2\). Thus \(\mathbf a=\begin{pmatrix}1&0&0\\0&2&0\\-1&0&1\end{pmatrix}\) with rows indexed by \(\ell\) and columns by \(i\); \(\det\mathbf a=2=2^{-3}\) in \(\mathbf F_3\), as (2.1) predicts.

**6.2.** \(\Pi\) permutes \(e_1,\dots,e_{p-1}\) by the involution \(i\mapsto p-i\) and kills \(e_0\); its matrix has a zero row and column at \(0\) and is the permutation matrix of an involution elsewhere, hence symmetric.

**6.3.** Compare the \((i,i')\) blocks: \(\sum_jX_{ij}X'_{ji'}YY'\). For the determinant, \(X\otimes I_m\) is conjugate, by a permutation of the basis, to \(I_m\otimes X\), which is block diagonal with \(m\) copies of \(X\).

**6.4.** The proof uses the coincidence of the scale \(N=p\) with the prime, through Frobenius. The final argument needs only an infinite sequence of \(N\) with \(\Delta_N\ne0\): the arithmetic lower bound of the odd-prime lesson holds along every such sequence, and the real upper bound of the next lessons holds for all \(N\). Primes form such a sequence.

## References

- [OpenAI-Catalan] OpenAI, Catalan's constant is irrational, preprint, 24 September 2026. https://github.com/openai/math/blob/main/preprints/Catalans-constant-is-irrational-September-24-2026/paper.pdf
