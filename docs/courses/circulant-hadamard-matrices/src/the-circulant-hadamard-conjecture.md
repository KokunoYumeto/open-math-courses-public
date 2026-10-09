# The circulant Hadamard conjecture

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves OpenAI's theorem [OpenAI-H, Section 5]:

**Theorem 2.1** (OpenAI). A real circulant Hadamard matrix of order \(n\) exists if and only if \(n\in\{1,4\}\).

Suppose the first row \(h\) of a circulant Hadamard matrix of order \(4u^2\), \(u>1\) odd, existed. Splitting \(C_{4u^2}=C_4\times P\) with \(P=C_{u^2}\), the evaluations of \(h\) at the four characters of \(C_4\), halved, give three elements \(c,d,g\) of \(\mathbb Z[i][P]\) with norm \(u^2\). By [Alternating character products](alternating-character-products.md), the quotients \(R=\Delta(d)/\Delta(c)\) and \(W=\Delta(g)/\Delta(c)\) are roots of unity of odd order. Because all coefficients of \(h\) are signs, \(d\equiv c\) modulo \(2\) and \(g\equiv c\) modulo \(1+i\), up to an explicit term involving \(J=\sum_{z\in P}z\). Reducing modulo a prime above \(2\), odd order forces \(R=W=1\); the first-order terms of these two exact equalities add up to a multiple of the trivial character value \(u^2\) of \(J\), which is a unit there. That is the contradiction.

We use [Circulant Hadamard matrices and group rings](circulant-hadamard-matrices-and-group-rings.md), Proposition 4.1 and Lemma 1.1 of [Local rings of cyclotomic integers](local-rings-of-cyclotomic-integers.md), and Lemma 2.1, Proposition 3.1 and the notation of Section 3 of [Alternating character products](alternating-character-products.md).

## 1. First-order terms

**Lemma 1.1.** Let \(O\) be a local domain with maximal ideal \(\mathfrak n\) and residue field \(k=O/\mathfrak n\), and let \(0\neq t\in\mathfrak n\). Then \(1+tO\) is a subgroup of the unit group \(O^\times\), and \(\lambda_t(1+tL)=L\bmod\mathfrak n\) defines a homomorphism \(\lambda_t:1+tO\to(k,+)\).

**Proof.** An element \(1+tL\) has residue \(1\), so it is a unit, and \(L\) is determined by it because \(O\) is a domain. The identities
\[
\frac{(1+tL)(1+tM)-1}t=L+M+tLM,\qquad\frac{(1+tL)^{-1}-1}t=-\frac L{1+tL}
\]
show closure under products and inverses; reducing them modulo \(\mathfrak n\) gives \(\lambda_t(xy)=\lambda_t(x)+\lambda_t(y)\). \(\square\)

## 2. Proof of the theorem

**Proof of Theorem 2.1.** For \(n=1\) and \(n=4\) examples were given in Section 2 of [Circulant Hadamard matrices and group rings](circulant-hadamard-matrices-and-group-rings.md). Suppose a circulant Hadamard matrix of some other order \(n>1\) exists. By Proposition 4.1 of [Local rings of cyclotomic integers](local-rings-of-cyclotomic-integers.md), \(n=4u^2\) with \(u\) odd, and \(u>1\).

*Three elements of norm \(u^2\).* Write \(C_n=C_4\times P\) with \(P=C_{u^2}\) and a generator \(Z\) of \(C_4\), and the first row as
\[
h=H_0+ZH_1+Z^2H_2+Z^3H_3,\qquad H_j\in\mathbb Z[P];
\]
every coefficient of every \(H_j\) is a sign. Put
\[
c=\tfrac12(H_0+H_1+H_2+H_3),\qquad d=\tfrac12(H_0-H_1+H_2-H_3),\qquad g=\tfrac12(H_0-H_2)+\tfrac i2(H_1-H_3),
\]
the halved evaluations of \(h\) at \(Z=1,-1,i\). Their coefficients are integers, being halves of sums or differences of an even number of signs; so \(c,d\in\mathbb Z[P]\) and \(g\in\mathbb Z[i][P]\). Evaluation of \(Z\) at a fourth root of unity commutes with the involution, so \(hh^*=4u^2\) gives
\[
cc^*=dd^*=gg^*=u^2.
\]

*Odd roots of unity.* With the notation \(I,B,\chi_S,x_S,\varepsilon_S,\Delta\) of Section 3 of [Alternating character products](alternating-character-products.md), Proposition 3.1 there shows that \(\Delta(c),\Delta(d),\Delta(g)\) are roots of unity of odd order. Hence so are
\[
R=\frac{\Delta(d)}{\Delta(c)}=\prod_{S\subseteq I}r_S^{\varepsilon_S},\qquad W=\frac{\Delta(g)}{\Delta(c)}=\prod_{S\subseteq I}w_S^{\varepsilon_S},\qquad r_S=\frac{d_S}{c_S},\quad w_S=\frac{g_S}{c_S}:
\]
a quotient of roots of unity whose orders divide odd numbers \(m,m'\) has order dividing \(mm'\).

*A prime above \(2\).* Since \(B/2B\neq0\) (Lemma 1.1 of [Local rings of cyclotomic integers](local-rings-of-cyclotomic-integers.md)), choose a maximal ideal \(\mathfrak m\ni2\) of \(B\), and let \(O=B_{\mathfrak m}\), \(\mathfrak n=\mathfrak mO\), \(k=O/\mathfrak n\). Each \(c_S,d_S,g_S\) is a unit of \(O\), since it divides the odd integer \(u^2\). In \(k\), \((i-1)^2=-2i=0\), so \(i\equiv1\); hence \(2\), \(1+i\) and \(1-i\) lie in \(\mathfrak n\), and they are nonzero.

*The sign coefficients.* Let \(b=\frac12(H_1+H_3)\in\mathbb Z[P]\) and \(J=\sum_{z\in P}z\). Direct computation gives
\[
d-c=-2b,\qquad g-c=(i-1)b-(H_2+iH_3).
\]
Every coefficient of \(H_2+iH_3\) has the form \(\alpha+i\beta\) with \(\alpha,\beta\in\{\pm1\}\), and \((\alpha+i\beta)-(1+i)\in2\mathbb Z[i]\); so \(H_2+iH_3=(1+i)J+2U\) with \(U\in\mathbb Z[i][P]\). Using \(i-1=i(1+i)\) and \(2=(1+i)(1-i)\), evaluation at \(\chi_S\) and division by the unit \(c_S\) give
\[
r_S=1+2L_{r,S},\quad L_{r,S}=-\frac{b_S}{c_S};\qquad w_S=1+(1+i)L_{w,S},\quad L_{w,S}=\frac{ib_S-J_S-(1-i)U_S}{c_S},
\]
with \(L_{r,S},L_{w,S}\in O\). Adding, and using \(i\equiv1\), \(1-i\equiv0\) and \(-1\equiv1\) in \(k\),
\[
L_{r,S}+L_{w,S}=-\frac{J_S}{c_S}-(1-i)\frac{b_S+U_S}{c_S}\equiv\frac{J_S}{c_S}\pmod{\mathfrak n}.\tag{2.1}
\]

*Exact equalities.* By Lemma 1.1, \(R\in1+2O\) and \(W\in1+(1+i)O\), so both have residue \(1\). Their orders are odd, so Lemma 2.1(ii) of [Alternating character products](alternating-character-products.md), in residue characteristic \(2\), gives \(R=W=1\). Applying \(\lambda_2\) to \(R\) and \(\lambda_{1+i}\) to \(W\),
\[
\sum_{S\subseteq I}\varepsilon_SL_{r,S}\equiv0,\qquad\sum_{S\subseteq I}\varepsilon_SL_{w,S}\equiv0\pmod{\mathfrak n}.
\]
Adding and using (2.1), \(\sum_S\varepsilon_SJ_S/c_S\equiv0\pmod{\mathfrak n}\).

*The contradiction.* By Lemma 1.1 of [Circulant Hadamard matrices and group rings](circulant-hadamard-matrices-and-group-rings.md), \(J_S=0\) for \(S\neq\varnothing\), because \(\chi_S\) is then nontrivial, and \(J_\varnothing=|P|=u^2\). So the sum is \(u^2/c_\varnothing\), a unit of \(O\), whose residue is not \(0\). \(\square\)

The hypothesis \(u>1\) enters through Proposition 3.1 of [Alternating character products](alternating-character-products.md), which needs a prime dividing \(u\) to make the orders odd. For the example \((1,1,1,-1)\) of order \(4\), \(P\) is trivial, \(c=d=1\) and \(g=i\), so \(R=1\) but \(W=i\), of order \(4\): it has residue \(1\) modulo every prime above \(2\) without being \(1\).

## 3. Barker sequences of even length

**Corollary 3.1.** A Barker sequence of even length \(n\) exists only for \(n\in\{2,4\}\).

**Proof.** For \(n>2\), Proposition 3.1 of [Circulant Hadamard matrices and group rings](circulant-hadamard-matrices-and-group-rings.md) gives a circulant Hadamard matrix of order \(n\), so \(n=4\) by Theorem 2.1. The sequences \(++\) and \(+++-\) exist. \(\square\)

With the theorem of Turyn and Storer for odd lengths [SW], which this course does not prove, Barker sequences exist exactly for the lengths \(2,3,4,5,7,11,13\).

## 4. Exercises

**Exercise 4.1** (easy). Check that \(c,d,g\) have integer coefficients and that \(cc^*=u^2\).

**Exercise 4.2** (easy). Show that in a field of characteristic \(2\) containing a square root \(i\) of \(-1\), \(i=1\).

**Exercise 4.3** (medium). Verify the two difference formulas \(d-c=-2b\) and \(g-c=(i-1)b-(H_2+iH_3)\).

**Exercise 4.4** (medium). For the order-\(4\) example, with \(P\) trivial and \(h=1+Z+Z^2-Z^3\), compute \(H_j\), \(c,d,g\), \(b\), \(U\) and the terms \(L_{r,\varnothing}\), \(L_{w,\varnothing}\), and see where the argument stops.

## 5. Solutions

**4.1.** Each coefficient of \(H_0\pm H_1+H_2\pm H_3\) is a sum of four odd numbers, hence even; each coefficient of \(H_0-H_2\) and \(H_1-H_3\) is a difference of two odd numbers. The evaluation \(Z\mapsto1\) maps \(hh^*=4u^2\) to \((2c)(2c)^*=4u^2\).

**4.2.** \((i-1)^2=i^2-2i+1=-2i=0\), and a field has no nonzero nilpotents.

**4.3.** \(d-c=\frac12(-2H_1-2H_3)=-(H_1+H_3)\). For \(g\): \(g-c=-H_2+\frac12\bigl((i-1)H_1-(i+1)H_3\bigr)\), and \((i-1)b-H_2-iH_3=\frac12\bigl((i-1)H_1+(i-1)H_3\bigr)-H_2-iH_3\) is the same.

**4.4.** \(H_0=H_1=H_2=1\) and \(H_3=-1\), so \(c=d=1\), \(g=i\), \(b=0\), and \(H_2+iH_3=1-i=(1+i)+2U\) with \(U=-i\). Then \(L_{r,\varnothing}=0\) and \(L_{w,\varnothing}=-1-(1-i)(-i)=i\), with residue \(1=J_\varnothing/c_\varnothing\), in accordance with (2.1). Here \(I\) is empty and \(R=1\), but \(W=w_\varnothing=i\) has order \(4\); the step \(W=1\) is not available, and indeed \(\lambda_{1+i}(W)=1\neq0\).

## References

- [OpenAI-H] OpenAI, *The circulant Hadamard conjecture*, OpenAI Math Release preprint, 23 September 2026, Sections 5 and 6. https://github.com/openai/math/tree/main/preprints/The-circulant-Hadamard-conjecture-September-23-2026
- [SW] K.-U. Schmidt and J. Willms, *Barker sequences of odd length*, Des. Codes Cryptogr. 80 (2016); arXiv:1501.06035. https://arxiv.org/abs/1501.06035
