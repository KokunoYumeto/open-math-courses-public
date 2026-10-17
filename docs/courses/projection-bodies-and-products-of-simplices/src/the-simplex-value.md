# The simplex value

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson computes \(R_d\) for simplices, following OpenAI [OpenAI-PB, Section 3]. By Cauchy's formula (Proposition 2.3 of [Projection bodies of polytopes](projection-bodies-of-polytopes.md)), the projection body of the standard simplex is the sum of \(d+1\) segments. Up to a translation and a factor, it is the unit cube plus one diagonal segment, and its volume follows from a fibre count. All simplices of one dimension have the same value, by affine invariance.

Throughout, \(d\ge2\), \(e_1,\dots,e_d\) is the standard basis, \(w=e_1+\dots+e_d\), and
\[
\begin{aligned}
T_d=\{x\in\mathbb R^d:{}&x_i\ge0,\\
&x_1+\dots+x_d\le1\}.
\end{aligned}
\]
Measure-theoretic facts are cited from the text of Fremlin [Fremlin] by number.

## 1. Volume and facets of the simplex

**Lemma 1.1.** \(|T_d|=1/d!\), and the \((d-1)\)-dimensional simplex \(\{x\in\mathbb R^{d-1}:x_i\ge0,\ \sum x_i\le1\}\) has volume \(1/(d-1)!\).

*Proof.* For \(d=1\), \(T_1=[0,1]\). For \(d\ge2\), the section of \(T_d\) at \(x_d=t\in[0,1]\) is \((1-t)T_{d-1}\), of volume \((1-t)^{d-1}|T_{d-1}|\) [Fremlin, 263A]. By Fubini's theorem [Fremlin, 251N and 252B], \(|T_d|=|T_{d-1}|\int_0^1(1-t)^{d-1}dt=|T_{d-1}|/d\). \(\square\)

**Lemma 1.2.** \(T_d\) is a polytope in the sense of [Projection bodies of polytopes](projection-bodies-of-polytopes.md), with \(d+1\) facets:
\[
\begin{gathered}
F_i=T_d\cap\{x_i=0\}\quad(1\le i\le d),\\
F_0=T_d\cap\{x_1+\dots+x_d=1\}.
\end{gathered}
\]
The outward unit normal of \(F_i\) is \(-e_i\) and its area is \(1/(d-1)!\); the outward unit normal of \(F_0\) is \(w/\sqrt d\) and its area is \(\sqrt d/(d-1)!\). So the vectors \(s_ja_j\) are
\[
-\frac{e_i}{(d-1)!}\quad(1\le i\le d),\qquad\frac w{(d-1)!}.
\]

*Proof.* The inequalities are \(\langle-e_i,x\rangle\le0\) and \(\langle w/\sqrt d,x\rangle\le1/\sqrt d\). Each \(F_i\) is a copy of the \((d-1)\)-dimensional simplex in the coordinate hyperplane, of area \(1/(d-1)!\) by Lemma 1.1. None of the inequalities can be omitted: each set \(F_j\) contains a relatively open subset of its hyperplane, hence a point outside the other hyperplanes, where the other inequalities are strict; moving from it a little in the direction of the outward normal violates inequality \(j\) only. The projection of \(F_0\) along \(e_d\) onto the hyperplane \(\{x_d=0\}\) is the \((d-1)\)-dimensional simplex. By Lemma 2.2 of [Projection bodies of polytopes](projection-bodies-of-polytopes.md), its area \(1/(d-1)!\) equals the area of \(F_0\) times \(|\langle w/\sqrt d,e_d\rangle|=1/\sqrt d\). \(\square\)

## 2. The projection body of the simplex

By Proposition 2.3 of [Projection bodies of polytopes](projection-bodies-of-polytopes.md) and Lemma 1.2,
\[
\begin{aligned}
\Pi T_d=\frac1{(d-1)!}\Bigl(&\sum_{i=1}^d\bigl[-\tfrac{e_i}2,\tfrac{e_i}2\bigr]\\
&+\bigl[-\tfrac w2,\tfrac w2\bigr]\Bigr),
\end{aligned}
\]
because a segment \([-\frac v2,\frac v2]\) does not change when \(v\) is replaced by \(-v\). Since \([-\frac v2,\frac v2]=[0,v]-\frac v2\), this is a translate of
\[
\frac1{(d-1)!}\bigl(Q+[0,w]\bigr),\qquad Q=[0,1]^d .
\]

**Lemma 2.1** (extrusion). Let \(C\subseteq\mathbb R^d\) be compact and convex and \(v\ne0\). Then, with \(\pi_v\) the orthogonal projection onto \(v^\perp\),
\[
|C+[0,v]|=|C|+|v|\operatorname{vol}_{d-1}(\pi_v[C]).
\]

*Proof.* After an orthogonal change of coordinates [Fremlin, 263A], \(v=|v|e_d\). For \(y\in\mathbb R^{d-1}\) let \(C_y=\{t:(y,t)\in C\}\), a compact interval or empty. A point \((y,t)\) lies in \(C+[0,v]\) exactly when \(t=t'+\theta|v|\) with \(t'\in C_y\) and \(\theta\in[0,1]\), since adding a multiple of \(v\) does not change \(y\). So the fibre of \(C+[0,v]\) over \(y\) is \(C_y+[0,|v|]\), of length \(|C_y|+|v|\) when \(C_y\) is nonempty, that is, when \(y\in\pi_v[C]\), and empty otherwise. Fubini's theorem [Fremlin, 251N and 252B] gives
\[
\begin{aligned}
&|C+[0,v]|\\
&\quad=\int\bigl(|C_y|+|v|\,\mathbf 1_{\pi_v[C]}(y)\bigr)\,dy\\
&\quad=|C|+|v|\operatorname{vol}_{d-1}(\pi_v[C]).\qquad\square
\end{aligned}
\]

**Proposition 2.2** (OpenAI). For \(d\ge2\),
\[
\begin{gathered}
|\Pi T_d|=\frac{d+1}{((d-1)!)^d},\\
R_d(T_d)=c_d=\frac{(d+1)\,d^d}{d!} .
\end{gathered}
\]
Every \(d\)-dimensional simplex has the same value \(c_d\).

*Proof.* By Lemma 2.1 with \(C=Q\) and \(v=w\), and by Proposition 2.3 of [Projection bodies of polytopes](projection-bodies-of-polytopes.md) with homogeneity,
\[
\begin{aligned}
|Q+[0,w]|&=1+|w|\operatorname{vol}_{d-1}(\pi_w[Q])\\
&=1+h_{\Pi Q}(w).
\end{aligned}
\] The cube has two facets with normals \(\pm e_i\) and area \(1\) for each \(i\), so \(h_{\Pi Q}(w)=\frac12\sum_i2|\langle e_i,w\rangle|=d\), and \(|Q+[0,w]|=d+1\). Scaling by \(1/(d-1)!\) multiplies volume by \(((d-1)!)^{-d}\) [Fremlin, 263A], and translation does not change it [Fremlin, 134A]. Then
\[
\begin{aligned}
R_d(T_d)&=\frac{d+1}{((d-1)!)^d}\,(d!)^{d-1}\\
&=\frac{(d+1)\,d^{d-1}}{(d-1)!}=\frac{(d+1)\,d^d}{d!}.
\end{aligned}
\]
A \(d\)-dimensional simplex, the convex hull of \(d+1\) affinely independent points \(p_0,\dots,p_d\), is \(LT_d+p_0\) with \(L\) the matrix of columns \(p_i-p_0\). Proposition 3.1 of [Projection bodies of polytopes](projection-bodies-of-polytopes.md) gives \(R_d(LT_d+p_0)=R_d(T_d)\). \(\square\)

The first values are \(c_2=6\), \(c_3=18\), \(c_4=\frac{160}3\) and \(c_{10}=\frac{17\,187\,500}{567}\approx30\,313.5\). In dimension three the bound \(R_3\le18\) holds for all convex bodies [CFLXX, Theorem 1.2].

## 3. Exercises

**3.1** (easy). Draw \(\Pi T_2\): show that it is a hexagon of area \(3\), and that \(R_2(T_2)=6\).

**3.2** (medium). Prove the volume formula for zonotopes: for vectors \(g_1,\dots,g_k\in\mathbb R^d\),
\[
\Bigl|\sum_{i=1}^k[0,g_i]\Bigr|=\sum_{S}|\det(g_i)_{i\in S}|,
\]
the sum over the \(d\)-element subsets \(S\) of \(\{1,\dots,k\}\). Use it to recompute \(|Q+[0,w]|=d+1\).

**3.3** (easy). Show that \(c_d<(d+1)e^d\).

## 4. Solutions

**3.1.** \(\Pi T_2=[-\frac{e_1}2,\frac{e_1}2]+[-\frac{e_2}2,\frac{e_2}2]+[-\frac w2,\frac w2]\), the hexagon with vertices \(\pm(1,1)\), \(\pm(1,0)\) and \(\pm(0,1)\); as a translate of \([0,1]^2+[0,(1,1)]\), its area is \(3\) by Proposition 2.2. With \(|T_2|=\frac12\), \(R_2(T_2)=3/\frac12=6\).

**3.2.** Induction on \(d\), and for fixed \(d\) on \(k\). For \(d=1\) both sides are \(\sum_i|g_i|\). For \(d\ge2\) and \(k<d\) both sides are \(0\) (the zonotope lies in a proper subspace, and there are no \(d\)-element subsets); a generator \(g_k=0\) changes neither side. Let \(Z=\sum_{i<k}[0,g_i]\) and \(g=g_k\ne0\). By Lemma 2.1, \(|Z+[0,g]|=|Z|+|g|\operatorname{vol}_{d-1}(\pi_g[Z])\), and \(\pi_g[Z]=\sum_{i<k}[0,\pi_gg_i]\) is a zonotope in \(g^\perp\). By induction in dimension \(d-1\) (on \(g^\perp\) with an orthonormal basis), \(\operatorname{vol}_{d-1}(\pi_g[Z])\) is the sum of \(|\det|\) of the \((d-1)\)-element families \(\pi_gg_i\), \(i\in S'\subseteq\{1,\dots,k-1\}\). For such a family, \(|g|\,|\det_{g^\perp}(\pi_gg_i)_{i\in S'}|=|\det((g_i)_{i\in S'},g)|\), since subtracting multiples of \(g\) does not change the determinant. The \(d\)-element subsets \(S\) containing \(k\) are exactly \(S'\cup\{k\}\), and those not containing \(k\) are counted in \(|Z|\). For \(g_i=e_i\) and \(g_{d+1}=w\), the \(d\)-subsets are \(\{e_1,\dots,e_d\}\), with determinant \(1\), and the \(d\) sets in which \(w\) replaces one \(e_j\), each with determinant \(\pm1\); the sum is \(d+1\).

**3.3.** The term \(d^d/d!\) is one of the positive terms of \(e^d=\sum_kd^k/k!\).

## References

- [OpenAI-PB] OpenAI, *A product counterexample to the simplex maximum for projection-body volume*, OpenAI Math Release preprint, 24 September 2026, Section 3. https://github.com/openai/math/tree/main/preprints/A-product-counterexample-to-the-simplex-maximum-for-projection-body-volume-September-24-2026
- [CFLXX] S. Chen, Y. Feng, Y. Li, D. Xi and L. Xu, *Petty's conjectured projection inequality in dimension three*, preprint, 2026, MathSciDoc 2608.23001. https://archive.ymsc.tsinghua.edu.cn/pacm_download/741/12780-pettyinequality.pdf
- [Fremlin] D. H. Fremlin, *Measure Theory*, Volumes 1 and 2, 134A, 251N, 252B, 263A; the text of the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10). https://www1.essex.ac.uk/maths/people/fremlin/mt.htm
