# Fourier fields for a smaller unitary

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let a unitary \(V\) on \(\mathbb C^d\) have the block form of [A contracting block](a-contracting-block.md), Proposition 2.1, with a small internal block \(D\). Feeding the internal output of \(V\) back into its internal input through a diagonal phase \(Z\) leaves a unitary \(F\) on the ports (Lemma 1.1). This lesson attaches to \(V\) a family of such unitaries \(F(z)\), indexed by a phase label \(z\), and two maps \(\mathcal E_L\) and \(\mathcal R_L\) from \(\mathbb C^d\) into port-valued functions of \(z\). They are nearly isometric and intertwine \(V\) with the controlled application of \(F(z)\) (Proposition 2.1), and in Fourier coordinates every row of their matrices has at most \(L\) nonzero entries (Proposition 3.2). The next lesson implements them with slots.

- Closing the internal coordinates (Lemma 1.1).
- Truncation and averaging (Proposition 2.1).
- Few input indices at each frequency (Lemma 3.1, Proposition 3.2).

The lesson follows [OpenAI-US, Section 4].

Throughout, \(d=k+s\le2^n\) with \(k,s\ge1\), and
\[
\begin{gathered}
V=\begin{pmatrix}A&B\\C&D\end{pmatrix}\in U(d),\\
\|D\|\le r<1 .
\end{gathered}
\]
The first \(k\) coordinates are the ports, the last \(s\) the internal coordinates. Since \(V\) is unitary, \(VV^*=I\) and \(V^*V=I\) give
\[
\begin{gathered}
CC^*+DD^*=I_s,\\
B^*B+D^*D=I_s ,
\end{gathered}
\]
and every block of \(V\) has norm at most \(1\).

## 1. Closing the internal coordinates

Let \(Z\) be a diagonal unitary of order \(s\). For a port input \(u\in\mathbb C^k\), feed the internal output \(x\in\mathbb C^s\) back into the internal input through \(Z\): the equation \(V(u,Zx)=(y,x)\) reads
\[
y=Au+BZx,\qquad x=Cu+DZx .
\]
As \(\|DZ\|\le r<1\), the second equation has the unique solution \(x=Xu\), and then \(y=Fu\), where
\[
X=(I-DZ)^{-1}C,\qquad F=A+BZX .
\]
Put
\[
E=\begin{pmatrix}I_k\\ ZX\end{pmatrix},\qquad O=\begin{pmatrix}F\\ X\end{pmatrix},
\]
the full input and output of \(V\) after the internal coordinates are closed. For a scalar phase \(Z=zI\), \(F\) is the transfer function of the unitary block matrix.

**Lemma 1.1** ([OpenAI-US, Lemma 4.1]). The matrix \(F\) is unitary. With
\[
Y=XF^*,\qquad R=OF^*=\begin{pmatrix}I_k\\ Y\end{pmatrix},
\]
we have
\[
\begin{gathered}
FE^*=R^*V,\\
Y=(I-Z^*D^*)^{-1}Z^*B^* .
\end{gathered}
\]

*Proof.* By definition \(VE=O\): its lower block is \(C+DZX=(I-DZ)X+DZX=X\). As \(V\) is unitary,
\[
\begin{aligned}
I_k+X^*X&=E^*E=O^*O\\
&=F^*F+X^*X ,
\end{aligned}
\]
so \(F^*F=I_k\), and the square matrix \(F\) is unitary. Then \(OF^*\) has the upper block \(FF^*=I_k\), and \(V^*R=V^*OF^*=EF^*\); taking adjoints gives \(FE^*=R^*V\). The lower blocks of \(V^*R=EF^*\) give \(B^*+D^*Y=ZY\). Multiplying by \(Z^*\) and using \(\|Z^*D^*\|\le r<1\) gives the formula for \(Y\). \(\blacksquare\)

## 2. Truncation and averaging

Fix an integer *truncation length* \(L\ge1\) and put
\[
\begin{gathered}
b=nL+\lceil\log_2(L+1)\rceil,\\
\mathcal G=(\mathbb Z/2^b)^{L+1}.
\end{gathered}
\]
For \(w,z\in\mathcal G\) write \(\chi_w(z)=\exp(2\pi i\,w\cdot z/2^b)\). Number the internal coordinates \(i=1,\dots,s\), and put
\[
v_i=(1,i,i^2,\dots,i^L)\in\mathcal G,
\]
\[
Z(z)=\operatorname{diag}\bigl(\chi_{v_1}(z),\dots,\chi_{v_s}(z)\bigr).
\]
The constant first coordinate of the \(v_i\) gives all diagonal entries of \(Z(z)\) a common phase when the first coordinate of \(z\) varies; averaging this phase separates terms of different lengths below. The other coordinates record power sums, so that a frequency remembers a multiset of internal indices (Lemma 3.1).

Lemma 1.1 at each \(z\) gives \(F(z)\), \(E(z)\) and \(R(z)\). Truncate the two series
\[
\begin{gathered}
ZX=\sum_{\ell\ge0}Z(DZ)^\ell C,\\
Y=\sum_{\ell\ge0}(Z^*D^*)^\ell Z^*B^*
\end{gathered}
\]
after \(L\) terms: let \(E_L(z)\) and \(R_L(z)\) have the upper block \(I_k\) and the lower blocks
\[
\sum_{\ell=0}^{L-1}Z(DZ)^\ell C,\qquad\sum_{\ell=0}^{L-1}(Z^*D^*)^\ell Z^*B^*,
\]
all factors evaluated at the same \(z\). As \(\|D\|\le r\) and \(\|B\|,\|C\|\le1\),
\[
\begin{gathered}
\|E_L(z)-E(z)\|\le\tau,\\
\|R_L(z)-R(z)\|\le\tau,
\end{gathered}
\]
with \(\tau=r^L/(1-r)\). The *field maps* \(\mathcal E_L,\mathcal R_L\colon\mathbb C^d\to\mathbb C^{\mathcal G}\otimes\mathbb C^k\) are
\[
\mathcal E_Lx=\frac1{\sqrt{|\mathcal G|}}\sum_{z\in\mathcal G}|z\rangle\otimes E_L(z)^*x,
\]
\[
\mathcal R_Lx=\frac1{\sqrt{|\mathcal G|}}\sum_{z\in\mathcal G}|z\rangle\otimes R_L(z)^*x .
\]
Let \(\widetilde F=\sum_z|z\rangle\langle z|\otimes F(z)\) apply \(F(z)\) to the port register, controlled by the phase label \(z\).

**Proposition 2.1** ([OpenAI-US, Proposition 4.2]). For \(\mathcal T=\mathcal E_L\) and for \(\mathcal T=\mathcal R_L\),
\[
(1-r^{2L})I_d\le\mathcal T^*\mathcal T\le I_d ,
\]
and
\[
\|\widetilde F\mathcal E_L-\mathcal R_LV\|\le2\tau .
\]

*Proof.* *The Gram matrix of \(\mathcal E_L\)* is \(\mathcal E_L^*\mathcal E_L=|\mathcal G|^{-1}\sum_zE_L(z)E_L(z)^*\). Fix all coordinates of \(z\) but the first, and let the first run through \(\mathbb Z/2^b\). Then \(Z(z)=\omega Z'\), where \(\omega=e^{2\pi iz_0/2^b}\) runs uniformly through the \(2^b\)-th roots of unity and \(Z'\) is fixed. With \(W=DZ'\), the lower block of \(E_L(z)\) is
\[
S=\sum_{\ell=0}^{L-1}\omega^{\ell+1}Z'W^\ell C .
\]
The average of \(\omega^p\) over the roots of unity is \(0\) unless \(2^b\) divides \(p\). The degrees in \(S\) lie between \(1\) and \(L<2^b\), and those in \(SS^*\) are differences \(\ell-\ell'\) with \(|\ell-\ell'|<L\). So the average of \(E_LE_L^*\) over \(\omega\) is block diagonal, with the upper block \(I_k\) and the lower block
\[
Z'\Bigl(\sum_{\ell=0}^{L-1}W^\ell CC^*(W^*)^\ell\Bigr)(Z')^* .
\]
Now \(CC^*=I-DD^*=I-WW^*\), and the sum telescopes:
\[
\begin{aligned}
&\sum_{\ell=0}^{L-1}W^\ell(I-WW^*)(W^*)^\ell\\
&\quad=I-W^L(W^*)^L .
\end{aligned}
\]
As \(\|W\|\le r\), the lower block lies between \((1-r^{2L})I_s\) and \(I_s\). Averaging over the remaining coordinates of \(z\) keeps these bounds.

*The Gram matrix of \(\mathcal R_L\).* Now put \(W=(Z')^*D^*\) and \(C_0=(Z')^*B^*\); the lower block of \(R_L(z)\) is \(\sum_\ell\omega^{-(\ell+1)}W^\ell C_0\), with degrees between \(-L\) and \(-1\), and
\[
\begin{aligned}
C_0C_0^*&=(Z')^*(I-D^*D)Z'\\
&=I-WW^* .
\end{aligned}
\]
The same computation applies.

*Intertwining.* Put \(\Delta(z)=F(z)E_L(z)^*-R_L(z)^*V\). By Lemma 1.1, \(F(z)E(z)^*=R(z)^*V\), so at each \(z\)
\[
\begin{aligned}
\|\Delta(z)\|&\le\|E_L(z)-E(z)\|\\
&\quad+\|R_L(z)-R(z)\|\le2\tau ,
\end{aligned}
\]
using \(\|F(z)\|=\|V\|=1\). For \(x\in\mathbb C^d\),
\[
\|(\widetilde F\mathcal E_L-\mathcal R_LV)x\|^2=\frac1{|\mathcal G|}\sum_z\|\Delta(z)x\|^2,
\]
which is at most \((2\tau)^2\|x\|^2\). \(\blacksquare\)

In particular both field maps are contractions, although a single matrix \(E_L(z)^*\) need not be one.

## 3. Few input indices at each frequency

Use for the first output register of the field maps the *Fourier basis*
\[
|\widehat w\rangle=\frac1{\sqrt{|\mathcal G|}}\sum_{z\in\mathcal G}\chi_w(z)|z\rangle,\qquad w\in\mathcal G .
\]
A row of the matrix of \(\mathcal E_L\) or \(\mathcal R_L\) in these coordinates is indexed by a frequency \(w\) and a port \(a\in\{1,\dots,k\}\), and its columns are the \(d\) input coordinates; its entries are the Fourier coefficients at \(w\) of the entries of row \(a\) of \(E_L(z)^*\), respectively \(R_L(z)^*\), as functions of \(z\).

**Lemma 3.1** (power sums). Let \(i_1,\dots,i_m\in\{1,\dots,s\}\) with \(1\le m\le L\). The multiset \(\{i_1,\dots,i_m\}\) is determined by the element \(v_{i_1}+\dots+v_{i_m}\) of \(\mathcal G\).

*Proof.* As integers, the coordinates of this sum are \(m\) and the power sums \(p_j=\sum_ti_t^j\), \(1\le j\le L\). They are at most \(L\,s^L\le L\,2^{nL}<2^b\), so they are determined by their residues modulo \(2^b\). The first coordinate gives \(m\). The elementary symmetric functions \(e_j\) of \(i_1,\dots,i_m\), defined by
\[
\prod_{t=1}^m(1+i_tx)=\sum_{j=0}^me_jx^j ,
\]
satisfy, for \(1\le j\le m\), *Newton's identities*
\[
je_j=\sum_{t=1}^j(-1)^{t-1}e_{j-t}\,p_t ,
\]
with \(e_0=1\), so \(e_1,\dots,e_m\) are computed successively from \(p_1,\dots,p_m\). To prove the identities, work with formal power series over \(\mathbb Q\), in which each \(1+i_tx\) is invertible. Logarithmic differentiation of the product gives
\[
\begin{aligned}
\frac{\sum_jje_jx^{j-1}}{\sum_je_jx^j}&=\sum_{t=1}^m\frac{i_t}{1+i_tx}\\
&=\sum_{k\ge0}(-1)^kp_{k+1}x^k ,
\end{aligned}
\]
and comparing the coefficients of \(x^{j-1}\) after multiplying by \(\sum_je_jx^j\) gives the identities. The \(e_j\) determine the polynomial \(\prod_t(T-i_t)\), which equals \(T^m-e_1T^{m-1}+\dots+(-1)^me_m\). A monic polynomial determines the multiset of its roots: if \(\prod_t(T-i_t)=\prod_t(T-i'_t)\), then \(i_1\) is a root of the right side, so \(i_1=i'_t\) for some \(t\), and the two products remain equal after cancelling this factor. \(\blacksquare\)

**Proposition 3.2** ([OpenAI-US, Proposition 4.3]). In these Fourier coordinates, every row of \(\mathcal E_L\) and of \(\mathcal R_L\) has at most \(L\) nonzero entries.

*Proof.* *Port inputs.* The upper block of \(E_L(z)\) and of \(R_L(z)\) is \(I_k\), so an input port \(j\) contributes only to the output port \(j\), at frequency \(0\).

*Internal inputs.* The columns of \(E_L(z)^*\) and \(R_L(z)^*\) at an internal coordinate \(i\) are those of
\[
\sum_{\ell=0}^{L-1}C^*(Z^*D^*)^\ell Z^*,\qquad\sum_{\ell=0}^{L-1}BZ(DZ)^\ell .
\]
In both, the rightmost factor \(Z^*\), respectively \(Z\), acts first on the input \(i\). Expanding the products of matrices entry by entry, each term is a coefficient times \(\chi_{-\sigma}(z)\), respectively \(\chi_\sigma(z)\), where \(\sigma\) is the sum of the \(v_j\) over a multiset of between \(1\) and \(L\) internal indices containing \(i\). For example, in \(BZDZ\) the entry in row \(a\) and column \(i\) is \(\sum_jB_{aj}D_{ji}\chi_{v_j+v_i}(z)\).

*Counting.* Such a term has nonzero frequency, because the first coordinate of \(\pm\sigma\) is \(\pm m\) with \(1\le m\le L<2^b\). Fix a nonzero frequency \(w\) and an output port. For \(\mathcal E_L\) replace \(w\) by \(-w\). By Lemma 3.1, all terms of this frequency come from one multiset \(\mu\) of at most \(L\) internal indices, and an input \(i\) contributes only through terms whose multiset contains \(i\). So the nonzero entries of the row lie in the at most \(L\) columns of \(\mu\); the order of the indices in a term changes its coefficient but not this set of columns. At frequency \(0\) only port inputs contribute, and a row has the single nonzero column of its port. \(\blacksquare\)

So a frequency remembers an unordered list of internal visits, and it allows only a short list of input indices. The next lesson uses this list to erase the input register coherently.

## 4. Exercises

**4.1.** For \(d=2\), \(k=s=1\) and \(V=\left(\begin{smallmatrix}a&b\\c&e\end{smallmatrix}\right)\) unitary with \(|e|<1\), compute \(F\) for \(Z=z\in U(1)\), and check that \(|F|=1\).

**4.2.** Verify Newton's identities for \(m=2\): \(e_1=p_1\) and \(2e_2=e_1p_1-p_2\).

**4.3.** Show that the multisets \(\{1,4\}\) and \(\{2,3\}\) have the same first power sum, and find the smallest \(j\) for which their power sums differ.

**4.4.** Why does the proof of Proposition 2.1 need \(L<2^b\)?

**4.5.** Show that \(\|E_L(z)\|\) can exceed \(1\) for a single \(z\): take \(d=2\), \(k=s=1\), \(L=1\) and \(C\ne0\).

## 5. Solutions

**4.1.** \(F=a+bz(1-ez)^{-1}c\), that is, \(F=(a-(ae-bc)z)/(1-ez)\). The determinant of \(V\) has modulus one, \(ae-bc=\det V\), and unitarity gives \(a=\overline e\det V\); so \(F=\det V\,(\overline e-z)/(1-ez)\), a Blaschke factor at the point \(z\) of the unit circle, of modulus \(1\).

**4.2.** For \(j=1\): \(e_1=e_0p_1=p_1\). For \(j=2\): \(2e_2=e_1p_1-e_0p_2\); with \(e_1=i_1+i_2\), \(p_2=i_1^2+i_2^2\), the right side is \((i_1+i_2)^2-i_1^2-i_2^2=2i_1i_2\).

**4.3.** Both have \(p_1=5\); \(p_2=17\) and \(13\) differ, so \(j=2\).

**4.4.** The averaging over the roots of unity of order \(2^b\) removes exactly the powers \(\omega^p\) with \(2^b\nmid p\); the degrees \(1,\dots,L\) and the differences \(\ell-\ell'\neq0\) must not be multiples of \(2^b\).

**4.5.** For \(L=1\), \(E_L(z)\) is the column \((1,zc)\), of norm \(\sqrt{1+|c|^2}>1\).

## References

- [OpenAI-US] OpenAI, *Polynomial-Time Unitary Synthesis from a Boolean Oracle*, OpenAI Math Release preprint, 5 October 2026, Section 4. https://github.com/openai/math/tree/main/preprints/Polynomial-Time-Unitary-Synthesis-from-a-Boolean-Oracle-October-5-2026
