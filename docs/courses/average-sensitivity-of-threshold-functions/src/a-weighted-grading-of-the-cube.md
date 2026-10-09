# A weighted grading of the cube

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson builds, for an arbitrary positive weight \(w\) on the cube \(\Omega=\{-1,1\}^n\), a self-adjoint operator \(M\) on the functions on \(\Omega\) [OpenAI-G, Sections 3 and 4]. Its eigenvalues are \(k-\frac n2\) with multiplicity \(\binom nk\), whatever \(w\) is; for \(w\equiv1\) it is \(-\frac12\) times the adjacency matrix of the cube, and in general its matrix entries depend on \(w\). Two properties survive for every weight: the total squared size of the entries is fixed, and multiplication by a coordinate connects only equal or adjacent eigenspaces. From these, Lemma 3.1 shows that the anticommutator of \(M\) with multiplication by a sign function \(h\) detects the edges of the cube on which \(h\) is constant. In [The Gotsman–Linial bound](the-gotsman-linial-bound.md), \(w=|p|\) for a polynomial \(p\), and these edges are the sensitive edges of \(\operatorname{sgn}p\).

We use the notation of [Threshold functions and a one-sided coupling](threshold-functions-and-a-one-sided-coupling.md), and orthogonal projections and adjoints in finite-dimensional complex inner product spaces, as in Theorem 2.2 and Section 3 of [Hilbert spaces and compact operators](course:foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators).

## 1. Operators on functions on the cube

Let \(N=2^n\) and \(\mathcal H=\mathbb C^\Omega\) with \(\langle a,b\rangle=\sum_x\overline{a(x)}b(x)\); the point masses \(\delta_x\) form an orthonormal basis. For an operator \(B\) on \(\mathcal H\) let \(B_{xy}=\langle\delta_x,B\delta_y\rangle\), let \(\|B\|_{\rm op}\) be its operator norm, and let
\[
\|B\|_{\rm HS}^2=\sum_{x,y}|B_{xy}|^2
\]
(the *Hilbert–Schmidt norm*).

**Lemma 1.1.** (a) For every orthonormal basis \((e_\alpha)\) of \(\mathcal H\), \(\|B\|_{\rm HS}^2=\sum_\alpha\|Be_\alpha\|^2\).

(b) \(|B_{xy}|\le\|B\|_{\rm op}\), and \(\|UBU^*\|_{\rm op}=\|B\|_{\rm op}\) for every unitary \(U\).

(c) If \(\mathcal H=E_0\oplus\dots\oplus E_n\) is an orthogonal decomposition with orthogonal projections \(\Pi_k\) onto \(E_k\), then \(\|B\|_{\rm HS}^2=\sum_{r,s}\|\Pi_sB\Pi_r\|_{\rm HS}^2\).

**Proof.** (a) By Parseval's identity in the two bases, \(\sum_\alpha\|Be_\alpha\|^2=\sum_\alpha\sum_x|\langle B^*\delta_x,e_\alpha\rangle|^2=\sum_x\|B^*\delta_x\|^2=\sum_{x,y}|\langle\delta_y,B^*\delta_x\rangle|^2=\sum_{x,y}|B_{xy}|^2\).

(b) \(|B_{xy}|\le\|B\delta_y\|\le\|B\|_{\rm op}\), and \(\|UBU^*\xi\|=\|BU^*\xi\|\) with \(\|U^*\xi\|=\|\xi\|\).

(c) Choose an orthonormal basis of each \(E_k\); together they form an orthonormal basis of \(\mathcal H\). For \(e_\alpha\in E_r\), \(\|Be_\alpha\|^2=\sum_s\|\Pi_sBe_\alpha\|^2=\sum_s\|\Pi_sB\Pi_re_\alpha\|^2\), while \(\Pi_sB\Pi_{r'}e_\alpha=0\) for \(r'\neq r\). Sum over \(\alpha\) and use (a) for each \(\Pi_sB\Pi_r\). \(\square\)

## 2. The weighted grading

For \(0\le k\le n\) let \(V_k\) be the span of the characters \(\chi_S\) with \(|S|\le k\), the functions of Fourier degree at most \(k\). If \(a\in V_r\) and \(b\in V_s\), then \(\overline b\,a\in V_{r+s}\), because \(\chi_S\chi_T=\chi_{S\triangle T}\) and \(|S\triangle T|\le|S|+|T|\).

Fix \(w:\Omega\to(0,\infty)\), let \(D\) be multiplication by \(\sqrt w\), and put
\[
K_k=DV_k,\qquad K_{-1}=\{0\},\qquad E_k=K_k\cap K_{k-1}^\perp\quad(0\le k\le n),
\]
with orthogonal projections \(\Pi_k\) onto \(E_k\). Define
\[
L=\sum_{k=0}^nk\,\Pi_k,\qquad M=L-\frac n2\,\mathrm{Id}.
\]
For \(i\in[n]\) let \(Z_i\) be multiplication by the coordinate \(x_i\), a self-adjoint unitary that commutes with \(D\).

**Lemma 2.1** (the grading). (a) \(\mathcal H=E_0\oplus\dots\oplus E_n\) orthogonally, and \(\dim E_k=\binom nk\).

(b) \(M\) is self-adjoint and \(\|M\|_{\rm HS}^2=\frac{nN}4\).

(c) \(\Pi_sZ_i\Pi_r=0\) whenever \(|s-r|>1\).

**Proof.** (a) The characters are a basis of \(\mathcal H\), so \(\dim V_k=\sum_{j\le k}\binom nj\); \(D\) is invertible, so \(\dim K_k\) is the same, and \(K_n=\mathcal H\). The spaces \(K_k\) increase, and by the projection theorem \(K_k=K_{k-1}\oplus E_k\), so \(\dim E_k=\binom nk\). For \(l<k\), \(E_l\subseteq K_l\subseteq K_{k-1}\perp E_k\). The dimensions add up to \(N\).

(b) In an orthonormal basis adapted to (a), \(M\) is diagonal with real entries \(k-\frac n2\), each \(\binom nk\) times; so by Lemma 1.1(a),
\[
\|M\|_{\rm HS}^2=\sum_{k=0}^n\binom nk\Bigl(k-\frac n2\Bigr)^2=\frac{nN}4,
\]
using \(\sum_k\binom nkk=n2^{n-1}\) and \(\sum_k\binom nkk(k-1)=n(n-1)2^{n-2}\).

(c) Multiplication by \(x_i\) maps \(V_r\) into \(V_{r+1}\) and commutes with \(D\), so \(Z_iK_r\subseteq K_{r+1}\). If \(s>r+1\), then \(K_{r+1}\subseteq K_{s-1}\perp E_s\), so \(\Pi_sZ_i\Pi_r=0\). Taking adjoints, \((\Pi_sZ_i\Pi_r)^*=\Pi_rZ_i\Pi_s\), which gives the case \(r>s+1\). \(\square\)

For \(w\equiv1\), \(E_k\) is spanned by the characters with \(|S|=k\) and \(M\chi_S=(|S|-\frac n2)\chi_S\), so \(M\) is \(-\frac12\) times the adjacency matrix of the cube (Exercise 4.1). For a general weight, the entries of \(M\) between adjacent vertices may be smaller than \(\frac12\) and entries between distant vertices may appear; the next lemma controls both.

## 3. Recovering edges

Write \(\rho(x,y)\) for the Hamming distance, the number of coordinates where \(x\) and \(y\) differ. Pairs of vertices are ordered.

**Lemma 3.1** (edges from the anticommutator; OpenAI). Let \(h\colon\Omega\to\{-1,1\}\), \(H\) the multiplication by \(h\), and
\[
\mathcal E_h=\{(x,y)\in\Omega^2:\rho(x,y)=1,\ h(x)=h(y)\}.
\]
Then \(|\mathcal E_h|\le2\|MH+HM\|_{\rm HS}^2\).

**Proof.** *Each entry.* Let \(C_i=LZ_i-Z_iL=MZ_i-Z_iM\). Its blocks are \(\Pi_sC_i\Pi_r=(s-r)\Pi_sZ_i\Pi_r\), which vanish unless \(|s-r|=1\), by Lemma 2.1(c). Let
\[
J=\sum_k(-1)^k\Pi_k,\qquad W=\sum_k\mathrm i^k\Pi_k,\qquad O_i=\tfrac12(Z_i-JZ_iJ),
\]
where \(J\) and \(W\) are unitary. Then \(\|O_i\|_{\rm op}\le1\), and the \((s,r)\) block of \(O_i\) is \(\frac12(1-(-1)^{s+r})\Pi_sZ_i\Pi_r\), which is \(\Pi_sZ_i\Pi_r\) if \(|s-r|=1\) and \(0\) otherwise. Conjugation by \(W\) multiplies the \((s,r)\) block by \(\mathrm i^{s-r}=\mathrm i(s-r)\) when \(|s-r|=1\). Hence \(WO_iW^*=\mathrm iC_i\) and \(\|C_i\|_{\rm op}\le1\) by Lemma 1.1(b). In the point basis \((C_i)_{xy}=(y_i-x_i)M_{xy}\), since \(Z_i\delta_y=y_i\delta_y\). For \(x\neq y\), choosing \(i\) with \(x_i\neq y_i\) gives \(2|M_{xy}|=|(C_i)_{xy}|\le1\); so
\[
|M_{xy}|^2\le\tfrac14\qquad(x\neq y).\tag{3.1}
\]

*Distant entries.* By Lemma 1.1(c) and Lemma 2.1(c), \(\|C_i\|_{\rm HS}^2=\sum_{r,s}(s-r)^2\|\Pi_sZ_i\Pi_r\|_{\rm HS}^2\le\|Z_i\|_{\rm HS}^2=N\). Summing \(|(C_i)_{xy}|^2=|y_i-x_i|^2|M_{xy}|^2\) over \(i\),
\[
\sum_{x,y}\rho(x,y)|M_{xy}|^2=\frac14\sum_{i=1}^n\|C_i\|_{\rm HS}^2\le\frac{nN}4=\sum_{x,y}|M_{xy}|^2,
\]
by Lemma 2.1(b). Let \(A_0=\sum_x|M_{xx}|^2\) and \(F=\sum_{\rho(x,y)\ge2}|M_{xy}|^2\). Subtracting the right side from the left gives \(-A_0+\sum_{\rho(x,y)\ge2}(\rho(x,y)-1)|M_{xy}|^2\le0\), so \(F\le A_0\).

*The deficit on edges.* There are \(nN\) ordered adjacent pairs, so by Lemma 2.1(b)
\[
\sum_{\rho(x,y)=1}\Bigl(\frac14-|M_{xy}|^2\Bigr)=\frac{nN}4-\sum_{\rho(x,y)=1}|M_{xy}|^2=A_0+F\le2A_0,
\]
and each term is nonnegative by (3.1).

*Equal-sign edges.* Let \(A_h=\sum_{(x,y)\in\mathcal E_h}|M_{xy}|^2\). Summing the nonnegative deficits over \(\mathcal E_h\) only,
\[
\frac{|\mathcal E_h|}4\le A_h+2A_0\le2(A_h+A_0).
\]
Finally \(T=MH+HM\) has \(T_{xy}=(h(x)+h(y))M_{xy}\), and \((h(x)+h(y))^2=4\) on the diagonal and on \(\mathcal E_h\); so \(4(A_0+A_h)\le\|T\|_{\rm HS}^2\), and \(|\mathcal E_h|\le8(A_h+A_0)\le2\|T\|_{\rm HS}^2\). \(\square\)

The anticommutator erases the entries of \(M\) between vertices of opposite signs and doubles the others; the fixed total size of \(M\) prevents the weight from hiding edges in distant entries.

## 4. Exercises

**Exercise 4.1** (easy). For \(w\equiv1\), show that \(E_k\) is spanned by the \(\chi_S\) with \(|S|=k\), and that \(M=-\frac12A\), where \(A_{xy}=1\) if \(\rho(x,y)=1\) and \(0\) otherwise.

**Exercise 4.2** (easy). For \(w\equiv1\) and any \(h\), compute \(\|MH+HM\|_{\rm HS}^2\) and compare with \(|\mathcal E_h|\).

**Exercise 4.3** (medium). Show that \(\sum_kk\binom nk=n2^{n-1}\) and \(\sum_kk(k-1)\binom nk=n(n-1)2^{n-2}\), and deduce \(\sum_k\binom nk(k-\frac n2)^2=n2^{n-2}\).

**Exercise 4.4** (medium). For \(n=1\), \(\Omega=\{-1,1\}\) and the weight \(w(1)=\alpha\), \(w(-1)=\beta\), compute \(E_0,E_1\) and the matrix of \(M\) in the point basis, and check (3.1) and \(F\le A_0\).

## 5. Solutions

**4.1.** With \(w\equiv1\), \(K_k=V_k\), and the characters with \(|S|=k\) are orthogonal to \(V_{k-1}\) and span a complement of it in \(V_k\). Then \(M\chi_S=(|S|-\frac n2)\chi_S\), while \((A\chi_S)(x)=\sum_i\chi_S(x^{\oplus i})=(n-2|S|)\chi_S(x)\). The two operators agree on a basis.

**4.2.** \(M_{xy}=-\frac12\) for adjacent \(x,y\) and \(0\) otherwise, so \(T_{xy}=-\frac12(h(x)+h(y))\) on edges and \(0\) elsewhere, and \(\|T\|_{\rm HS}^2=|\mathcal E_h|\). Lemma 3.1 loses a factor \(2\) here.

**4.3.** \(k\binom nk=n\binom{n-1}{k-1}\) and \(k(k-1)\binom nk=n(n-1)\binom{n-2}{k-2}\); sum over \(k\). Then \(\sum\binom nkk^2=n(n+1)2^{n-2}\), and \(\sum\binom nk(k-\frac n2)^2=n(n+1)2^{n-2}-n\cdot n2^{n-1}+\frac{n^2}42^n=n2^{n-2}\).

**4.4.** \(K_0=E_0\) is spanned by \(\sqrt w\), that is by \((\sqrt\alpha,\sqrt\beta)\), and \(E_1\) by \((\sqrt\beta,-\sqrt\alpha)\). With \(s=\alpha+\beta\), \(M=\frac12(\Pi_1-\Pi_0)\) has entries \(M_{11}=\frac{\beta-\alpha}{2s}=-M_{-1,-1}\) and \(M_{1,-1}=M_{-1,1}=-\frac{\sqrt{\alpha\beta}}s\). Then \(|M_{1,-1}|^2=\frac{\alpha\beta}{s^2}\le\frac14\), with deficit \(\frac14-\frac{\alpha\beta}{s^2}=\frac{(\alpha-\beta)^2}{4s^2}=|M_{11}|^2\), and \(F=0\).

## References

- [OpenAI-G] OpenAI, *Average sensitivity of polynomial threshold functions*, OpenAI Math Release preprint, 25 September 2026, Sections 3 and 4. https://github.com/openai/math/tree/main/preprints/Average-Sensitivity-of-Polynomial-Threshold-Functions-September-25-2026
