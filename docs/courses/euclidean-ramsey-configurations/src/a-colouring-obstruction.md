# A colouring obstruction

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson proves the easier half of the classification theorem of [Ramsey sets and the tensor criterion](ramsey-sets-and-the-tensor-criterion.md): if the tensor condition fails, a fixed finite number of colours suffices, in every dimension, to colour space without a monochromatic congruent copy of the set. The colouring is built from \(\mathbb Q\)-linear functionals on real tensors, chosen with Zorn's lemma; it is not measurable, and it does not need to be. The strategy of an invariant that takes a fixed value on every copy, followed by a colouring modulo an integer, goes back to Erdős, Graham, Montgomery, Rothschild, Spencer and Straus [EGMRSS], who used real quadratic invariants.

The notation of the first lesson is kept: \(A=\{a_1,\dots,a_s\}\subset\mathbb R^d\) with \(s\ge2\) and affine span \(\mathbb R^d\); \(W=\mathbb R\times\mathbb R^d\) as a vector space over \(\mathbb Q\); the evaluations \(e_i(v,u)=v+a_i\cdot u\); the symmetric tensors \(\mathcal T(W)\); and the gradient map \(G:\mathcal T(W)\to\mathrm{Sym}_d(\mathbb R)\).

## 1. Congruent copies are images of isometries

**Lemma 1.1.** Let \(b_1,\dots,b_s\) be points of \(\mathbb R^D\) with \(\|b_i-b_j\|=\|a_i-a_j\|\) for all \(i,j\). Then there are a linear map \(R:\mathbb R^d\to\mathbb R^D\) with \(R^{\mathsf T}R=I_d\) and a vector \(t\in\mathbb R^D\) such that \(b_i=t+Ra_i\) for every \(i\).

*Proof.* Put \(x_i=a_i-a_1\) and \(y_i=b_i-b_1\). By the polarization identity
\[
2\langle x_i,x_j\rangle=\|x_i\|^2+\|x_j\|^2-\|x_i-x_j\|^2 ,
\]
and the same for the \(y_i\), the Gram matrices of \((x_i)\) and \((y_i)\) agree. If \(\sum_ic_ix_i=0\), then
\[
\begin{aligned}
\Bigl\|\sum_ic_iy_i\Bigr\|^2&=\sum_{i,j}c_ic_j\langle y_i,y_j\rangle\\
&=\Bigl\|\sum_ic_ix_i\Bigr\|^2=0 .
\end{aligned}
\]
So \(\sum c_ix_i\mapsto\sum c_iy_i\) is a well-defined linear map on the span of the \(x_i\), which is \(\mathbb R^d\) because \(A\) affinely spans \(\mathbb R^d\). It preserves inner products, so as a map \(R:\mathbb R^d\to\mathbb R^D\) it satisfies \(R^{\mathsf T}R=I_d\). With \(t=b_1-Ra_1\), we get \(b_i=b_1+Rx_i=t+Ra_i\). \(\square\)

In particular, two copies of \(A\) in \(\mathbb R^d\) that both span \(\mathbb R^d\) differ by an orthogonal map and a translation, as used in Remark 2.2 of the first lesson.

## 2. The obstruction

**Proposition 2.1.** If the tensor condition fails for \(A\), then with \(r_0=(2s+1)^s\) colours, every \(\mathbb R^D\) has a colouring without a monochromatic congruent copy of \(A\). In particular, every Ramsey set with at least two points satisfies the tensor condition, and hence the matrix condition of the classification theorem.

*Proof.* *A separating functional.* Consider the \(\mathbb Q\)-vector space
\[
\mathcal Y=(\mathbb R\otimes\mathbb R)^s\oplus\mathrm{Sym}_d(\mathbb R)
\]
and the \(\mathbb Q\)-linear map
\[
\begin{aligned}
&\Phi:\mathcal T(W)\to\mathcal Y,\\
&\Phi(T)=\bigl((e_i\otimes e_i)(T)\bigr)_{i=1}^s\\
&\qquad\oplus G(T).
\end{aligned}
\]
The failure of the tensor condition says that \(y_0=(0,\dots,0,I_d)\) is not in the image of \(\Phi\). So its class in the quotient space \(\mathcal Y/\mathrm{im}\,\Phi\) is nonzero. By Lemma 1.1 of the first lesson, extend this class to a basis of the quotient, and let \(\ell\) be the \(\mathbb Q\)-linear functional on \(\mathcal Y\) that vanishes on \(\mathrm{im}\,\Phi\), takes the value \(1\) at \(y_0\), and takes the value \(0\) on representatives of the other basis classes. So
\[
\ell\circ\Phi=0,\qquad\ell(y_0)=1 .
\]
Write \(\ell\) by components as \(\ell_i:\mathbb R\otimes\mathbb R\to\mathbb Q\subset\mathbb R\) and \(L:\mathrm{Sym}_d(\mathbb R)\to\mathbb R\), and put \(h_i(x)=\ell_i(x\otimes x)\) for \(x\in\mathbb R\). For \(w=(v,u)\in W\), the tensor \(w\otimes w\) is symmetric, and \(\ell(\Phi(w\otimes w))=0\) reads
\[
\begin{gathered}
\sum_{i=1}^sh_i(v+a_i\cdot u)+L(uu^{\mathsf T})=0,\\
L(I_d)=1 .
\end{gathered}
\]
With \(u=0\) this gives
\[
\sum_{i=1}^sh_i(x)=0\qquad(x\in\mathbb R).
\]

*An invariant of congruent copies.* Fix \(D\) and put \(H_i(z)=\sum_{j=1}^Dh_i(z_j)\) for \(z\in\mathbb R^D\). Let \((b_1,\dots,b_s)\) be an ordered congruent copy of \(A\), that is, \(\|b_i-b_j\|=\|a_i-a_j\|\) for all \(i,j\). By Lemma 1.1, \(b_i=t+Ra_i\) with \(R^{\mathsf T}R=I_d\). If \(u_j^{\mathsf T}\) is the \(j\)th row of \(R\), then
\[
\begin{gathered}
(b_i)_j=t_j+a_i\cdot u_j,\\
\sum_{j=1}^Du_ju_j^{\mathsf T}=R^{\mathsf T}R=I_d .
\end{gathered}
\]
Apply the displayed identity to \((v,u)=(t_j,u_j)\) and sum over \(j\). Since \(L\) is additive,
\[
\sum_{i=1}^sH_i(b_i)=-L(I_d)=-1 .
\]
On the other hand, \(\sum_iH_i(z)=0\) for every single point \(z\), by the identity with \(u=0\) applied to each coordinate.

*The colouring.* Put \(K=2s+1\) and divide \([0,2)\) into \(K\) half-open intervals of length \(2/K\). Colour \(z\in\mathbb R^D\) by the \(s\)-tuple whose \(i\)th entry is the interval containing the representative of \(H_i(z)\) modulo \(2\) in \([0,2)\). This uses at most \(K^s=r_0\) colours, whatever \(D\) is. If the copy \((b_1,\dots,b_s)\) were monochromatic, then for each \(i\) the numbers \(H_i(b_i)\) and \(H_i(b_1)\) would have representatives in the same interval, so
\[
\begin{gathered}
H_i(b_i)-H_i(b_1)=2n_i+\varepsilon_i,\\
n_i\in\mathbb Z,\qquad|\varepsilon_i|<\frac2K .
\end{gathered}
\]
Summing over \(i\) and using \(\sum_iH_i(b_i)=-1\) and \(\sum_iH_i(b_1)=0\),
\[
\begin{gathered}
-1=2\sum_in_i+\sum_i\varepsilon_i,\\
\Bigl|\sum_i\varepsilon_i\Bigr|<\frac{2s}{2s+1}<1 .
\end{gathered}
\]
The first identity makes \(\sum_i\varepsilon_i\) an odd integer, which contradicts the second. So the colouring has no monochromatic copy, and \(A\) is not Ramsey. The last assertion follows from Proposition 2.1 of the first lesson. \(\square\)

**Corollary 2.2** (Erdős, Graham, Montgomery, Rothschild, Spencer and Straus [EGMRSS]). Every Ramsey set lies on a sphere.

*Proof.* A singleton does. A Ramsey set with at least two points, taken in its affine span, satisfies the matrix condition by Proposition 2.1, and lies on a sphere by Proposition 3.1 of the first lesson. \(\square\)

The functionals \(h_i\) in the proof are \(\mathbb Q\)-linear in the tensor \(x\otimes x\) and arbitrary otherwise. When the failure of the tensor condition is already visible after multiplication, they can be chosen as real quadratic polynomials, and the colouring becomes explicit (Exercises 3.1 and 3.2).

## 3. Exercises

**3.1** (medium). Let \(A=\{0,1,2\}\subset\mathbb R\). Show that \(h_1(x)=-\frac{x^2}2\), \(h_2(x)=x^2\), \(h_3(x)=-\frac{x^2}2\) and \(L(m)=m\) satisfy \(\sum_ih_i(v+a_iu)+L(u^2)=0\) and \(\sum_ih_i(x)=0\). Deduce that three equally spaced points on a line do not form a Ramsey set.

**3.2** (medium). Using Exercise 3.1, describe an explicit colouring of \(\mathbb R^D\) with \(7^3\) colours, in terms of \(\|z\|^2\), that has no three monochromatic points \(b_1,b_2,b_3\) on a line with \(b_2-b_1=b_3-b_2\) of length one.

**3.3** (easy). Where does the proof of Proposition 2.1 use that the functional \(L\) is additive, and why is no continuity needed?

**3.4** (medium). Let \(A\) be a set with at least two points that does not lie on a sphere. Show directly from the definitions, without Proposition 2.1, that the tensor condition fails.

## 4. Solutions

**3.1.** With \(a=(0,1,2)\), the sum is \(-\frac{v^2}2+(v+u)^2-\frac{(v+2u)^2}2+u^2\), and expanding gives
\[
\begin{aligned}
&-\tfrac{v^2}2+v^2+2uv+u^2\\
&\quad-\tfrac{v^2}2-2uv-2u^2+u^2=0 .
\end{aligned}
\]
Also \(-\frac{x^2}2+x^2-\frac{x^2}2=0\). These are exactly the two identities used after the separating functional in the proof of Proposition 2.1; that proof then applies word for word with these \(h_i\) and \(L\), which satisfy \(L(I_1)=1\), and gives a colouring with \(7^3\) colours in every dimension.

**3.2.** Here \(H_1(z)=-\frac{\|z\|^2}2\), \(H_2(z)=\|z\|^2\) and \(H_3(z)=-\frac{\|z\|^2}2\). Colour \(z\) by the triple of intervals of length \(2/7\) in \([0,2)\) containing \(-\frac{\|z\|^2}2\), \(\|z\|^2\) and \(-\frac{\|z\|^2}2\) modulo \(2\). For an equally spaced triple with spacing one, \(\|b_1\|^2-2\|b_2\|^2+\|b_3\|^2=2\) by the parallelogram identity, so \(\sum_iH_i(b_i)=-1\), and the argument of the proof excludes a monochromatic triple.

**3.3.** It is used once, in \(\sum_jL(u_ju_j^{\mathsf T})=L(\sum_ju_ju_j^{\mathsf T})=L(I_d)\), a finite sum. Only finitely many points of a copy are coloured, and the colouring compares finitely many values, so no limit of values of \(L\) or of \(h_i\) occurs.

**3.4.** If the tensor condition held, Proposition 2.1 of the first lesson would give the matrix condition, and Proposition 3.1 of the first lesson would put \(A\) on a sphere.

## References

- [OpenAI-ER] OpenAI, *A classification of finite Euclidean Ramsey configurations*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/A-classification-of-finite-Euclidean-Ramsey-configurations-September-23-2026
- [EGMRSS] P. Erdős, R. L. Graham, P. Montgomery, B. L. Rothschild, J. Spencer and E. G. Straus, *Euclidean Ramsey theorems I*, Journal of Combinatorial Theory, Series A 14 (1973), 341–363. https://doi.org/10.1016/0097-3165(73)90011-3
