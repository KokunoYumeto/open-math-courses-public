# Two inequalities for polynomial multiplication

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Fix a character \(\lambda\). This lesson measures the polynomial multiplication tensors \(C(a,b)\) by a symmetrized profile \(P(a,b)\) of the values of \(\lambda\) and its leg permutations, and proves two inequalities for it: discrete concavity in each argument (Lemma 4.3) and shifted tripling (Lemma 4.4). Both come from degenerations of \(C(a,b)\), or of \(C(a,b)\otimes B_X(2)\), into sums with a shared \(X\)-leg and matched sectors, to which the entropy inequality of [Separating a shared leg](separating-a-shared-leg.md) applies. The constructions are OpenAI's [OpenAI-MM, Section 4].

## 1. The symmetrized profile

Let \(t=t(\lambda)\); by Lemma 2.5, \(t\ge\frac13\). For positive integers \(a,b\) put
\[
P(a,b)=\Bigl(\prod_\pi\lambda_\pi(C(a,b))\Bigr)^{1/(6t)},
\]
the product taken over the six permutations \(\pi\) of the legs, with \(\lambda_\pi(A)=\lambda(\pi A)\) as in Section 4 of [Characters and degenerations](characters-and-degenerations.md).

**Lemma 4.1.** \(P(a,b)=P(b,a)>0\), \(P(1,b)=b\), and \(P(a,b)\le(a+b-1)^{1/t}\).

**Proof.** Let \(\tau\) exchange the \(X\)-leg and the \(Y\)-leg. By Lemma 1.8(b), \(\tau C(a,b)\cong C(b,a)\), so \(\lambda_\pi(C(b,a))=\lambda(\pi\tau C(a,b))\), which is \(\lambda_{\pi\tau}(C(a,b))\); as \(\pi\) runs through the six permutations, so does \(\pi\tau\). Positivity holds because \(\lambda_\pi(C(a,b))\ge1\) by Lemma 2.2. Since \(C(1,b)\cong B_X(b)\), Lemma 2.4 for \(\lambda_\pi\) and Lemma 2.11 give
\[
\prod_\pi\lambda_\pi(C(1,b))=b^{\sum_\pi p_X(\lambda_\pi)}=b^{6t}.
\]
Finally \(\lambda_\pi(C(a,b))\le R(C(a,b))=a+b-1\) by Lemma 2.2 and Lemma 1.8(a). \(\square\)

## 2. A determinant filtration

Let \(V_e\) be the space of homogeneous polynomials of degree \(e\) in two variables \(u,v\) over \(F\), with the monomial basis \(u^{e-i}v^i\), \(0\le i\le e\). Then \(C(a,b)\) is the tensor of the multiplication \(V_{a-1}\times V_{b-1}\to V_{a+b-2}\) in the monomial bases, the monomial \(u^{e-i}v^i\) corresponding to the index \(i\). Let \(W\) be the span of two further variables \(s,w\); then \(V_e\otimes W\) is the space of polynomials of degree \(e\) in \(u,v\) and degree \(1\) in \(s,w\), with the basis \(u^{e-i}v^is\), \(u^{e-i}v^iw\). Put
\[
D=uw-vs .
\]

**Lemma 4.2.** Let \(e\ge1\), and let \(\delta:V_e\otimes W\to V_{e+1}\) be the substitution \(s=u\), \(w=v\).

(a) \(\delta\) is surjective, and its kernel is \(DV_{e-1}=\{Dg:g\in V_{e-1}\}\), of dimension \(e\).

(b) The elements \(q_i=u^{e-i}v^is\) for \(0\le i\le e\), \(q_{e+1}=v^ew\), and \(k_j=Du^{e-1-j}v^j\) for \(0\le j\le e-1\) form a basis of \(V_e\otimes W\). The map \(\delta\) sends \(q_0,\dots,q_{e+1}\) to the monomial basis \(u^{e+1-i}v^i\) of \(V_{e+1}\), and the \(k_j\) are \(D\) times the monomial basis of \(V_{e-1}\).

**Proof.** (a) The images \(\delta(q_i)\) are all the monomials of degree \(e+1\), so \(\delta\) is surjective. Since \(\delta(D)=uv-vu=0\) and \(\delta\) is multiplicative, \(DV_{e-1}\) lies in the kernel. Multiplication by \(D\) is injective, because the polynomial ring is an integral domain, so \(\dim DV_{e-1}=e\). The kernel has dimension \(2(e+1)-(e+2)=e\), and the two spaces coincide.

(b) The \(2e+2\) elements span \(V_e\otimes W\) by (a). If \(\sum_i\alpha_iq_i+\sum_j\beta_jk_j=0\), applying \(\delta\) gives \(\alpha=0\), and then \(D\sum_j\beta_ju^{e-1-j}v^j=0\) gives \(\beta=0\). \(\square\)

**Lemma 4.3** (discrete concavity). For \(a\ge1\) and \(b\ge2\),
\[
2P(a,b)\ge P(a,b+1)+P(a,b-1).
\]
By Lemma 4.1 the same holds with the roles of the two arguments exchanged.

**Proof.** *Step 1: a tensor of multiplication.* The tensor \(B_X(2)\) is the tensor of the scalar multiplication \(F\times W\to W\) in the bases \((1)\), \((s,w)\), \((s,w)\). By Lemma 1.3(b), \(C(a,b)\otimes B_X(2)\) is the tensor of the bilinear map
\[
\begin{aligned}
V_{a-1}\times(V_{b-1}\otimes W)&\to V_{a+b-2}\otimes W,\\
(f,G)&\mapsto fG,
\end{aligned}
\]
in the monomial bases. By Lemma 1.3(a) it is equivalent to the tensor \(A^\circ\) of the same map in the bases of Lemma 4.2, with \(e=b-1\) on the input side and \(e'=a+b-2\) on the output side; both degrees are at least \(1\). Write \(q_i,k_j\) for the input basis and \(q'_{i'},k'_{j'}\) for the output basis.

*Step 2: the blocks.* For \(f\in V_{a-1}\), multiplication by \(f\) commutes with \(\delta\), and \(f\cdot Dg=D\,(fg)\). Hence:

- \(f\cdot k_j=D\,(f\,u^{b-2-j}v^j)\) has no component on the \(q'\), and its components on the \(k'\) are the monomial coordinates of \(f\,u^{b-2-j}v^j\in V_{a+b-3}\);
- the components of \(f\cdot q_i\) on the \(q'\) are the monomial coordinates of \(\delta(f\cdot q_i)=f\,\delta(q_i)\in V_{a+b-1}\), because \(\delta(k')=0\) and the \(\delta(q')\) are the monomials.

Let \(f\) run through the monomial basis of \(V_{a-1}\). The terms of \(A^\circ\) with a \(Y\)-variable of a \(q_i\) and a \(Z\)-variable of a \(q'_{i'}\) form the tensor of \(V_{a-1}\times V_b\to V_{a+b-1}\) in monomial bases, that is, a copy \(A_+\) of \(C(a,b+1)\). The terms with a \(Y\)-variable of a \(k_j\) and a \(Z\)-variable of a \(k'_{j'}\) form a copy \(A_-\) of \(C(a,b-1)\). The remaining terms \(A_\ast\) have a \(Y\)-variable of a \(q_i\) and a \(Z\)-variable of a \(k'_{j'}\); there are no terms with a \(Y\)-variable of a \(k_j\) and a \(Z\)-variable of a \(q'_{i'}\).

*Step 3: the degeneration.* Give weight \(0\) to the \(X\)-variables and to the \(Y\)- and \(Z\)-variables of the \(q\) and \(q'\), weight \(-1\) to the \(Y\)-variables of the \(k_j\), and weight \(+1\) to the \(Z\)-variables of the \(k'_{j'}\). The terms of \(A_+\) and \(A_-\) have weight \(0\), those of \(A_\ast\) weight \(+1\). Hence
\[
C(a,b)\otimes B_X(2)\;\rightsquigarrow\;A_++A_-,
\]
a sum with a shared \(X\)-leg and matched sectors \(A_+\cong C(a,b+1)\) and \(A_-\cong C(a,b-1)\), both nonzero.

*Step 4: characters.* Let \(\pi\) be a permutation of the legs and \(q=(q_+,q_-)\) a probability vector. By Lemma 2.4, Lemma 2.9 and Corollary 3.4, applied to the character \(\lambda_\pi\),
\[
\begin{aligned}
&2^{p_X(\lambda_\pi)}\lambda_\pi(C(a,b))\\
&\quad\ge e^{p_X(\lambda_\pi)H(q)}\lambda_\pi(C(a,b+1))^{q_+}\\
&\qquad\cdot\lambda_\pi(C(a,b-1))^{q_-}.
\end{aligned}
\]
Multiply the six inequalities, use \(\sum_\pi p_X(\lambda_\pi)=6t\) (Lemma 2.11), and take the power \(1/(6t)\). With \(P_\pm=P(a,b\pm1)\) this gives
\[
2P(a,b)\ge e^{H(q)}P_+^{q_+}P_-^{q_-}.
\]
Choose \(q\) proportional to \((P_+,P_-)\); by the equality case of Lemma 3.5 the right side is \(P_++P_-\). \(\square\)

## 3. Three sectors

**Lemma 4.4** (shifted tripling). For all positive integers \(a\) and \(h\),
\[
P(a,3h+a-1)\ge3P(a,h).
\]

**Proof.** Put \(B=3h+a-1\). The terms of \(C(a,B)\) are \(x_iy_jz_{i+j}\) with \(0\le i\le a-1\) and \(0\le j\le B-1\). Split the \(Y\)-indices and the \(Z\)-indices into three intervals each:

- \(Y\)-left \([0,h-1]\), \(Y\)-middle \([h,\,2h+a-2]\), \(Y\)-right \([2h+a-1,\,3h+a-2]\);
- \(Z\)-left \([0,h+a-2]\), \(Z\)-middle \([h+a-1,\,2h+a-2]\), \(Z\)-right \([2h+a-1,\,3h+2a-3]\).

Give weight \(+1\) to the middle \(Y\)-variables, weight \(-1\) to the middle \(Z\)-variables, and weight \(0\) to all other variables. If \(j\) is a left index, then \(i+j\le h+a-2\) is a left index; if \(j\) is a right index, then \(i+j\ge2h+a-1\) is a right index. So the terms with a left or right \(Y\)-variable have weight \(0\), and a term with a middle \(Y\)-variable has weight \(1\), \(0\) or \(1\) according as its \(Z\)-variable is left, middle or right. No term has negative weight, and the terms of weight zero form three sectors, left–left, middle–middle and right–right, with the shared \(X\)-variables and disjoint \(Y\)- and \(Z\)-variables.

The left sector is \(\sum_{i<a,\,j<h}x_iy_jz_{i+j}=C(a,h)\). In the right sector, \(j=2h+a-1+j'\) with \(0\le j'<h\), and shifting both indices by \(2h+a-1\) identifies it with \(C(a,h)\). In the middle sector the \(Z\)-index is \(h+a-1+r\) with \(0\le r\le h-1\), and with \(i'=a-1-i\) the \(Y\)-index is \(h+i'+r\); the sector is
\[
\sum_{i'=0}^{a-1}\sum_{r=0}^{h-1}x_{a-1-i'}\,y_{h+i'+r}\,z_{h+a-1+r}.
\]
Let \(\sigma\) exchange the \(Y\)-leg and the \(Z\)-leg. Then \(\sigma C(a,h)\cong\sum_{i<a,\,j<h}x_i\,y_{i+j}\,z_j\): the old \(Z\)-variables \(z_{i+j}\) move to the \(Y\)-leg and the old \(Y\)-variables \(y_j\) to the \(Z\)-leg. Renaming \(x_{a-1-i'}\) as \(x_{i'}\) and shifting the \(Y\)-indices by \(h\) and the \(Z\)-indices by \(h+a-1\) shows that the middle sector is isomorphic to \(\sigma C(a,h)\), with \((i',r)\) in the role of \((i,j)\). The renaming concerns this sector alone and is used only to compute its value under characters.

Apply Lemma 2.9 and Corollary 3.4, with the uniform vector \(q=(\frac13,\frac13,\frac13)\), to each character \(\lambda_\pi\):
\[
\begin{aligned}
\lambda_\pi(C(a,B))&\ge3^{p_X(\lambda_\pi)}\lambda_\pi(C(a,h))^{2/3}\\
&\qquad\cdot\lambda_\pi(\sigma C(a,h))^{1/3}.
\end{aligned}
\]
Since \(\lambda_\pi(\sigma C(a,h))=\lambda_{\pi\sigma}(C(a,h))\) and \(\pi\sigma\) runs through all permutations with \(\pi\), the product over \(\pi\) of the last factors equals \(\prod_\pi\lambda_\pi(C(a,h))\). Multiplying the six inequalities and taking the power \(1/(6t)\) gives \(P(a,B)\ge3P(a,h)\). \(\square\)

## 4. Exercises

**4.1** (easy). For \(\lambda=\rho_X\), show that \(P(a,b)=\sqrt{ab(a+b-1)}\).

**4.2** (medium). Check Lemmas 4.3 and 4.4 directly for the profile of Exercise 4.1.

**4.3** (medium). Let \(a=b=2\). Write the bases of Lemma 4.2 for \(e=1\) and \(e=2\), compute \(f\cdot q_i\) and \(f\cdot k_0\) in the output basis for \(f=u\) and \(f=v\), and identify the blocks \(A_+\), \(A_-\), \(A_\ast\).

**4.4** (easy). For \(a=2\) and \(h=1\), list the eight terms of \(C(2,4)\), their sectors and their weights in the proof of Lemma 4.4.

## 5. Solutions

**4.1.** By Lemma 1.8(a), the three flattening ranks of \(C(a,b)\) are \(a\), \(b\) and \(a+b-1\). The six values \(\rho_X(\pi C(a,b))\) are these three numbers, each twice, since \(\rho_X(\pi A)\) is the flattening rank of \(A\) at the leg \(\pi^{-1}(X)\). With \(t(\rho_X)=\frac23\) (Example 2.6), \(P(a,b)=(ab(a+b-1))^{2/4}\).

**4.2.** For fixed \(a\), \(P(a,b)^2=a(b^2+(a-1)b)\), and \(b\mapsto\sqrt{a(b^2+(a-1)b)}\) has second derivative \(-\frac14a^{1/2}(a-1)^2(b^2+(a-1)b)^{-3/2}\le0\) for \(b>0\); a concave function satisfies \(2g(b)\ge g(b+1)+g(b-1)\). For tripling, with \(B=3h+a-1\),
\[
\frac{P(a,B)^2}a=(3h+a-1)(3h+2a-2),
\]
and the right side equals \(9h^2+9h(a-1)+2(a-1)^2\), which is at least \(9h(a+h-1)=9P(a,h)^2/a\).

**4.3.** For \(e=1\): \(q_0=us\), \(q_1=vs\), \(q_2=vw\), \(k_0=D\). For \(e=2\): \(q'_0=u^2s\), \(q'_1=uvs\), \(q'_2=v^2s\), \(q'_3=v^2w\), \(k'_0=Du\), \(k'_1=Dv\). Since \(uw=D+vs\),
\[
u\cdot q_2=uvw=v^2s+vD=q'_2+k'_1,
\]
and \(u\cdot q_0=q'_0\), \(u\cdot q_1=q'_1\), \(u\cdot k_0=k'_0\); further \(v\cdot q_0=q'_1\), \(v\cdot q_1=q'_2\), \(v\cdot q_2=q'_3\), \(v\cdot k_0=k'_1\). The \(q\)-to-\(q'\) entries are multiplication by \(u\) and \(v\) from \(V_2\) to \(V_3\) (the block \(A_+\cong C(2,3)\)), the \(k\)-to-\(k'\) entries are multiplication from \(V_0\) to \(V_1\) (the block \(A_-\cong C(2,1)\)), and \(A_\ast\) is the single term given by the component \(k'_1\) of \(u\cdot q_2\).

**4.4.** The \(Y\)-intervals are \(\{0\}\), \(\{1,2\}\), \(\{3\}\), and the \(Z\)-intervals are \(\{0,1\}\), \(\{2\}\), \(\{3,4\}\). The terms \(x_0y_0z_0\) and \(x_1y_0z_1\) are left–left; \(x_0y_1z_1\) has weight \(1\); \(x_1y_1z_2\) and \(x_0y_2z_2\) are middle–middle; \(x_1y_2z_3\) has weight \(1\); \(x_0y_3z_3\) and \(x_1y_3z_4\) are right–right. The middle sector \(x_1y_1z_2+x_0y_2z_2\) is \(\sigma C(2,1)\) with the \(X\)-variables in reversed order.

## References

- [OpenAI-MM] OpenAI, *An upper bound of 9/4 for the matrix multiplication exponent*, OpenAI Math Release preprint, 2 October 2026, Section 4. https://github.com/openai/math/tree/main/preprints/Matrix-Multiplication-Nine-Fourths-October-2-2026
