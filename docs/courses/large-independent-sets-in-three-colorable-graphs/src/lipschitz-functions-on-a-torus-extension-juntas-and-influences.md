# Lipschitz functions on a torus: extension, juntas and influences

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The proof of [OpenAI-I] turns an independent set of the graph of the first lesson into functions on the sets \(\mathbb T^M\) of families of phases. These functions have values in \([-1,1]\), they are Lipschitz for the sup distance with a constant that does not depend on the number of the phases, and they change their sign under the half shift. This lesson proves what the course needs about such functions, and states a theorem of T. Austin that is proved in another course: a Lipschitz function of many variables is close to a function of a bounded number of them.

- Extension of a Lipschitz function from a finite set (Lemma 1.1).
- The mean over one coordinate, and the decomposition of a function (Lemmas 2.1 to 2.3).
- Functions of few coordinates and Theorem (J) (Section 3).
- Influences: a coordinate with a large influence exists, and there are few of them (Proposition 4.1).

The lesson follows [OpenAI-I, Section 2]; the extension formula is used in [OpenAI-I, Section 4]. It uses the notation of [Label Cover and the graph of the reduction](label-cover-and-the-graph-of-the-reduction.md) for phases and families of phases. It needs the Lebesgue integral on a cube and Fubini's theorem ([core course *Measure and Integration*](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10)).

## 1. Lipschitz functions and their extension

Let \(M\) be a finite nonempty set. A real function \(f\) on a subset \(S\) of \(\mathbb T^M\) is *\(L\)-Lipschitz*, for a number \(L\ge0\), if for all \(x,y\in S\)
\[
|f(x)-f(y)|\le L\,d_\infty(x,y).
\]
If the half shift \(T\) maps \(S\) to itself, \(f\) is *odd* if \(f(Tx)=-f(x)\) for all \(x\in S\).

**Lemma 1.1** (extension). Let \(S\subset\mathbb T^M\) be a finite nonempty set with \(T(S)=S\), and let \(f:S\to[-1,1]\) be \(L\)-Lipschitz and odd. Then there is a function \(F:\mathbb T^M\to[-1,1]\) that is \(L\)-Lipschitz and odd and agrees with \(f\) on \(S\).

**Proof.** *A Lipschitz extension.* For \(x\in\mathbb T^M\) put
\[
g(x)=\min_{y\in S}\bigl(f(y)+L\,d_\infty(x,y)\bigr).
\]
For \(x,x'\) and every \(y\in S\), the triangle inequality gives
\[
\begin{aligned}
f(y)+L\,d_\infty(x,y)\le{}&f(y)+L\,d_\infty(x',y)\\
&+L\,d_\infty(x,x').
\end{aligned}
\]
Taking the minimum over \(y\) on both sides, \(g(x)\le g(x')+L\,d_\infty(x,x')\). So \(g\) is \(L\)-Lipschitz. For \(x\in S\), the term with \(y=x\) is \(f(x)\), and every term is at least \(f(x)\) because \(f\) is \(L\)-Lipschitz. So \(g=f\) on \(S\).

*Values in \([-1,1]\).* Let \(\tilde g(x)=\max\{-1,\min\{1,g(x)\}\}\). The map \(u\mapsto\max\{-1,\min\{1,u\}\}\) of \(\mathbb R\) does not increase distances and fixes \([-1,1]\). So \(\tilde g\) is \(L\)-Lipschitz, has values in \([-1,1]\) and agrees with \(f\) on \(S\).

*Oddness.* Put
\[
F(x)=\tfrac12\bigl(\tilde g(x)-\tilde g(Tx)\bigr).
\]
Since \(d_\infty(Tx,Ty)=d_\infty(x,y)\), the function \(x\mapsto\tilde g(Tx)\) is \(L\)-Lipschitz, and so is \(F\). Its values lie in \([-1,1]\). From \(T(Tx)=x\) follows \(F(Tx)=-F(x)\). For \(x\in S\) also \(Tx\in S\), and \(F(x)=\tfrac12(f(x)-f(Tx))=f(x)\). \(\blacksquare\)

The formula for \(g\) is due to E. J. McShane. The extension is not unique; the lemma is used with one fixed choice.

## 2. The mean over one coordinate

Let \(n\ge1\). The set \(\mathbb T^n\) of the families \((x_1,\dots,x_n)\) of phases is identified with \([0,1)^n\) by taking representatives, and carries the Lebesgue measure of the cube, which has the total mass \(1\). Let \(\mathcal B_n\) be the space of the bounded Borel functions \(f:[0,1)^n\to\mathbb R\). For \(f,g\in\mathcal B_n\) put
\[
\begin{gathered}
\mathbb E f=\int f,\qquad \langle f,g\rangle=\mathbb E(fg),\\
\|f\|_2=\langle f,f\rangle^{1/2},\qquad \|f\|_1=\mathbb E|f| .
\end{gathered}
\]
A function on the closed cube \([0,1]^n\) is treated in the same way; the boundary has measure \(0\).

**Definition.** Let \(1\le i\le n\) and \(f\in\mathcal B_n\). For a point \(x\) and a number \(w\in[0,1)\) let \(x^{w}\) be the point \(x\) with \(w\) in place of the coordinate \(x_i\). The *mean over the coordinate \(i\)* is
\[
(E_if)(x)=\int_0^1 f(x^{w})\,dw ,
\]
and \(Q_if=f-E_if\). By Fubini's theorem \(E_if\) is again a bounded Borel function. It does not depend on \(x_i\).

**Lemma 2.1.** For \(f,g\in\mathcal B_n\) and coordinates \(i,j\):

1. \(E_iE_if=E_if\) and \(E_iE_jf=E_jE_if\);
2. \(\langle E_if,g\rangle=\langle f,E_ig\rangle\);
3. \(E_iQ_if=Q_iE_if=0\), \(Q_iQ_if=Q_if\), \(\langle Q_if,g\rangle=\langle f,Q_ig\rangle\), and the \(Q_i\) commute with each other and with the \(E_j\);
4. \(\|f\|_2^2=\|E_if\|_2^2+\|Q_if\|_2^2\); in particular \(\|Q_if\|_2\le\|f\|_2\) and \(\|E_if\|_2\le\|f\|_2\).

**Proof.** (1) \(E_if\) does not depend on \(x_i\), so its mean over \(x_i\) is itself. The second equation is Fubini's theorem for the two variables at the positions \(i\) and \(j\). (2) By Fubini's theorem both sides are equal to the integral of \(f(x^{w})\,g(x^{w'})\) over \(w\), \(w'\) and the coordinates of \(x\) other than \(x_i\). (3) follows from (1), (2) and \(Q_i=\mathrm{id}-E_i\). (4) \(\langle E_if,Q_if\rangle=\langle f,E_iQ_if\rangle=0\) by (2) and (3), and \(f=E_if+Q_if\). \(\blacksquare\)

For a set \(S\subset[n]\) let
\[
E_S=\prod_{i\notin S}E_i ,
\]
the mean over all coordinates outside \(S\); the order of the factors does not matter. The function \(E_Sf\) depends only on the coordinates in \(S\). In particular \(E_{[n]}f=f\), and \(E_\varnothing f\) is the constant \(\mathbb Ef\).

**Lemma 2.2** (the nearest function of the coordinates in \(S\)). Let \(f\in\mathcal B_n\) and \(S\subset[n]\). If \(g\in\mathcal B_n\) depends only on the coordinates in \(S\), then
\[
\|f-g\|_2^2=\|f-E_Sf\|_2^2+\|E_Sf-g\|_2^2 .
\]
In particular \(\|f-E_Sf\|_2\le\|f-g\|_2\), and \(\|f\|_2^2=\|E_Sf\|_2^2+\|f-E_Sf\|_2^2\).

**Proof.** By Lemma 2.1, \(E_SE_S=E_S\) and \(\langle E_Sa,b\rangle=\langle a,E_Sb\rangle\) for all \(a,b\). A function \(h\) that depends only on the coordinates in \(S\) satisfies \(E_ih=h\) for \(i\notin S\), so \(E_Sh=h\). For such \(h\),
\[
\begin{aligned}
\langle f-E_Sf,h\rangle&=\langle f-E_Sf,E_Sh\rangle\\
&=\langle E_Sf-E_SE_Sf,h\rangle=0 .
\end{aligned}
\]
Apply this with \(h=E_Sf-g\) and expand \(\|(f-E_Sf)+(E_Sf-g)\|_2^2\). The last statement is the case \(g=0\). \(\blacksquare\)

**Lemma 2.3** (decomposition). For \(f\in\mathcal B_n\) and \(A\subset[n]\) put
\[
f_A=\prod_{i\in A}Q_i\prod_{i\notin A}E_i\,f .
\]

1. \(f=\sum_{A\subset[n]}f_A\), and \(f_\varnothing=\mathbb Ef\).
2. \(\langle f_A,f_{A'}\rangle=0\) for \(A\ne A'\).
3. \(Q_if=\sum_{A\ni i}f_A\) and \(\|Q_if\|_2^2=\sum_{A\ni i}\|f_A\|_2^2\).
4. \(E_Sf=\sum_{A\subset S}f_A\) and \(\|E_Sf\|_2^2=\sum_{A\subset S}\|f_A\|_2^2\).

**Proof.** (1) The product of the operators \(E_i+Q_i=\mathrm{id}\) over all \(i\) is the identity; multiply out, using that all these operators commute. (2) Let \(i\) be in one of the two sets and not in the other, say \(i\in A\), \(i\notin A'\). Then \(f_A=Q_ia\) and \(f_{A'}=E_ib\) for some \(a,b\in\mathcal B_n\), and \(\langle Q_ia,E_ib\rangle=\langle a,Q_iE_ib\rangle=0\). (3) \(Q_if_A=f_A\) if \(i\in A\), since \(Q_iQ_i=Q_i\), and \(Q_if_A=0\) if \(i\notin A\), since \(Q_iE_i=0\). Apply \(Q_i\) to (1); the norm follows from (2). (4) In the same way \(E_if_A=0\) if \(i\in A\) and \(E_if_A=f_A\) if \(i\notin A\). So \(E_S\) keeps the terms with \(A\subset S\) and removes the others. \(\blacksquare\)

**Example 2.4.** Let \(n=2\), \(c_k(x)=\cos(2\pi x_k)\) and \(f=c_1+c_1c_2\). Then \(f_{\{1\}}=c_1\), \(f_{\{1,2\}}=c_1c_2\), and \(f_\varnothing=f_{\{2\}}=0\). So \(\|Q_1f\|_2^2=\tfrac12+\tfrac14\) and \(\|Q_2f\|_2^2=\tfrac14\).

## 3. Functions of few coordinates

A function on \([0,1]^N\) or on \(\mathbb T^n\) that depends only on the coordinates in a set \(S\) is called a *junta on \(S\)*. The following statement says that a function that is Lipschitz for the sup distance is close to a junta on a set whose size is bounded independently of the number of the coordinates.

**Theorem (J)** (T. Austin). For every \(L\ge0\) and every \(\tau>0\) there is an integer \(J(L,\tau)\ge1\) with the following property. Let \(N\ge1\), and let \(f:[0,1]^N\to[-1,1]\) satisfy, for all \(x,y\in[0,1]^N\),
\[
|f(x)-f(y)|\le L\max_{1\le k\le N}|x_k-y_k| .
\]
Then there is a set \(S\subset[N]\) with at most \(J(L,\tau)\) elements such that
\[
\|f-E_Sf\|_2<\tau .
\]

This is the case of the interval \([0,1]\) with the Lebesgue measure, and of functions with a Lipschitz condition, of [Austin, Theorem 1.1]. That theorem gives a set \(S\) of bounded size with \(\|f-E_Sf\|_1<\tau^2/2\); since \(f\) and \(E_Sf\) have values in \([-1,1]\), the difference \(h=f-E_Sf\) satisfies \(|h|\le2\), so \(\|h\|_2^2\le2\,\|h\|_1<\tau^2\).

Theorem (J) is proved, in exactly this form and with an explicit number \(J(L,\tau)\), in the lesson [Lipschitz functions are close to juntas](course:hypercontractivity-on-a-torus-and-juntas/lipschitz-functions-are-close-to-juntas) (Hypercontractivity on a torus and juntas for Lipschitz functions), Theorem 4.1. The proof there uses the heat equation on a torus and a hypercontractive inequality, and it needs nothing from this course. Here the theorem is used as stated.

By Lemma 2.2, \(E_Sf\) is the junta on \(S\) nearest to \(f\). So the conclusion of (J) holds as soon as some junta \(g\) on a set of at most \(J(L,\tau)\) coordinates has \(\|f-g\|_2<\tau\).

The condition is on the sup distance, and the bound does not depend on \(N\). For example, the mean \(\tfrac1N(x_1+\dots+x_N)\) satisfies the condition with \(L=1\); it is close to the constant \(\tfrac12\), a junta on the empty set (Exercise 5.3).

**Lemma 3.1** (Theorem (J) on a torus). Let \(n\ge1\), and let \(H:\mathbb T^n\to[-1,1]\) be \(L\)-Lipschitz for the sup distance. Then for every \(\tau>0\) there is a set \(S\subset[n]\) with at most \(J(L,\tau)\) elements and \(\|H-E_SH\|_2<\tau\).

**Proof.** Let \(f(x)=H(x \bmod 1)\) for \(x\in[0,1]^n\), where \(x\bmod1\) is the family of the phases of the coordinates. For real numbers \(a,b\), \(\|a-b\|\le|a-b|\). So \(d_\infty(x\bmod1,y\bmod1)\le\max_k|x_k-y_k|\), and \(f\) satisfies the condition of (J). On \([0,1)^n\), \(f\) is \(H\) in the identification of this section, and the means over coordinates are the same. \(\blacksquare\)

## 4. Influences

**Definition.** For \(H\in\mathcal B_n\) and a coordinate \(i\), the *influence* of \(i\) on \(H\) is
\[
D_i(H)=\|Q_iH\|_2=\|H-E_iH\|_2 .
\]
It is \(0\) if \(H\) does not depend on \(x_i\).

**Proposition 4.1.** For every \(L\ge0\) and every \(\varepsilon>0\) there are a number \(\beta>0\) and an integer \(K\ge1\), which depend only on \(L\) and \(\varepsilon\), with the following properties for every \(n\ge1\) and every function \(H:\mathbb T^n\to[-1,1]\) that is \(L\)-Lipschitz for the sup distance.

1. If \(\mathbb EH=0\) and \(\mathbb E(H^2)>\varepsilon\), then \(D_i(H)\ge\beta\) for some coordinate \(i\).
2. At most \(K\) coordinates \(i\) have \(D_i(H)\ge\beta/2\).

One can take \(\beta=\sqrt{\varepsilon/(4J)}\) with \(J=J(L,\sqrt\varepsilon/2)\), and \(K=J(L,\beta/2)\).

**Proof.** (1) By Lemma 3.1 there is a set \(S\) with at most \(J\) elements such that \(G=E_SH\) has \(\|H-G\|_2<\sqrt\varepsilon/2\). By Lemma 2.2,
\[
\begin{aligned}
\|G\|_2^2&=\|H\|_2^2-\|H-G\|_2^2\\
&>\varepsilon-\tfrac\varepsilon4=\tfrac{3\varepsilon}4 .
\end{aligned}
\]
By Lemma 2.3(4), \(G=\sum_{A\subset S}H_A\), and \(H_\varnothing=\mathbb EH=0\). Every nonempty \(A\subset S\) contains some \(i\in S\). With Lemma 2.3(3),
\[
\begin{aligned}
\|G\|_2^2&=\sum_{\varnothing\ne A\subset S}\|H_A\|_2^2\\
&\le\sum_{i\in S}\sum_{A\ni i}\|H_A\|_2^2\\
&=\sum_{i\in S}D_i(H)^2 .
\end{aligned}
\]
The left side is positive, so \(S\) is not empty, and some \(i\in S\) has
\[
D_i(H)^2\ge\frac{\|G\|_2^2}{|S|}>\frac{3\varepsilon}{4J}\ge\beta^2 .
\]

(2) By Lemma 3.1 there is a set \(S'\) with at most \(K=J(L,\beta/2)\) elements such that \(G'=E_{S'}H\) has \(\|H-G'\|_2<\beta/2\). For \(i\notin S'\) the function \(G'\) does not depend on \(x_i\), so \(Q_iG'=0\), and by Lemma 2.1(4)
\[
\begin{aligned}
D_i(H)&=\|Q_i(H-G')\|_2\\
&\le\|H-G'\|_2<\tfrac\beta2 .
\end{aligned}
\]
So every coordinate with \(D_i(H)\ge\beta/2\) lies in \(S'\). \(\blacksquare\)

The two numbers do not depend on \(n\). In the last lesson of the course the number of the coordinates is chosen after \(\beta\) and \(K\), and it depends on them.

## 5. Exercises

**5.1.** In the situation of Lemma 1.1 let \(g'(x)=\max_{y\in S}\bigl(f(y)-L\,d_\infty(x,y)\bigr)\). Show that \(g'\) is \(L\)-Lipschitz, agrees with \(f\) on \(S\), and that every \(L\)-Lipschitz function \(e\) on \(\mathbb T^M\) with \(e=f\) on \(S\) satisfies \(g'\le e\le g\).

**5.2.** Let \(f\in\mathcal B_n\). Show that
\[
\begin{aligned}
\sum_{i=1}^nD_i(f)^2&=\sum_A|A|\,\|f_A\|_2^2\\
&\ge\|f\|_2^2-(\mathbb Ef)^2 .
\end{aligned}
\]

**5.3.** Let \(f(x)=\tfrac1N(x_1+\dots+x_N)\) and \(g(x)=\tfrac1{\sqrt N}(x_1+\dots+x_N)\) on \([0,1]^N\). (a) Show that \(|f(x)-f(y)|\le\max_k|x_k-y_k|\) and \(\|f-\tfrac12\|_2^2=\tfrac1{12N}\). (b) Show that \(\|g-E_Sg\|_2^2=\tfrac{N-|S|}{12N}\) for every \(S\subset[N]\), and find the least \(L\) with \(|g(x)-g(y)|\le L\max_k|x_k-y_k|\).

**5.4.** Let \(H(z)=1-4\|z_1\|\) for \(z\in\mathbb T^n\). Show that \(H\) is \(4\)-Lipschitz and odd, and compute \(D_1(H)\) and \(D_i(H)\) for \(i\ne1\).

**5.5.** Show that the function \(E_Sf\) of Theorem (J) has values in \([-1,1]\) and satisfies the same Lipschitz condition as \(f\).

## 6. Solutions

**5.1.** The proofs for \(g'\) are those for \(g\) in Lemma 1.1, with the inequalities reversed and with the distances subtracted: the term for \(y\) at \(x\) is at least the term for \(y\) at \(x'\) minus \(L\,d_\infty(x,x')\), and for \(x\in S\) the term with \(y=x\) is \(f(x)\) and every term is at most \(f(x)\). If \(e\) is \(L\)-Lipschitz with \(e=f\) on \(S\), then for every \(y\in S\)
\[
\begin{aligned}
f(y)-L\,d_\infty(x,y)&\le e(x)\\
&\le f(y)+L\,d_\infty(x,y) ,
\end{aligned}
\]
and the maximum of the left sides is \(g'(x)\), the minimum of the right sides \(g(x)\).

**5.2.** By Lemma 2.3(3), \(D_i(f)^2=\sum_{A\ni i}\|f_A\|_2^2\). In the sum over \(i\), the term \(\|f_A\|_2^2\) occurs once for every \(i\in A\). By Lemma 2.3(1) and (2), \(\|f\|_2^2=\sum_A\|f_A\|_2^2\), and \(\|f_\varnothing\|_2^2=(\mathbb Ef)^2\). Since \(|A|\ge1\) for \(A\ne\varnothing\), the claim follows.

**5.3.** (a) \(|f(x)-f(y)|\le\tfrac1N\sum_k|x_k-y_k|\), and this mean is at most \(\max_k|x_k-y_k|\). The functions \(x_k-\tfrac12\) have the mean \(0\), are orthogonal to each other, and \(\int_0^1(w-\tfrac12)^2dw=\tfrac1{12}\). So \(\|f-\tfrac12\|_2^2=\tfrac1{N^2}\cdot N\cdot\tfrac1{12}\). (b) \(E_i\) replaces \(x_i\) by \(\tfrac12\). So \(g-E_Sg=\tfrac1{\sqrt N}\sum_{k\notin S}(x_k-\tfrac12)\), with the square of the norm \(\tfrac1N(N-|S|)\tfrac1{12}\). For \(x=(1,\dots,1)\), \(y=0\): \(g(x)-g(y)=\sqrt N\) and \(\max_k|x_k-y_k|=1\); and \(|g(x)-g(y)|\le\tfrac1{\sqrt N}\cdot N\max_k|x_k-y_k|\). So the least \(L\) is \(\sqrt N\). The function \(g\) stays far from every junta on a bounded number of coordinates, and its Lipschitz constant for the sup distance is not bounded.

**5.4.** \(|\,\|a\|-\|b\|\,|\le\|a-b\|\), so \(|H(z)-H(z')|\le4\|z_1-z_1'\|\), which is at most \(4\,d_\infty(z,z')\). From \(\|z_1+\tfrac12\|=\tfrac12-\|z_1\|\): \(H(Tz)=1-2+4\|z_1\|=-H(z)\). \(H\) does not depend on \(z_i\) for \(i\ne1\), so \(D_i(H)=0\). \(E_1H=\int_0^1(1-4\|w\|)\,dw\), which is \(1-4\cdot\tfrac14=0\). So \(D_1(H)^2=\|H\|_2^2\), and \(\|H\|_2^2=2\int_0^{1/2}(1-4w)^2dw=\tfrac13\). Hence \(D_1(H)=1/\sqrt3\).

**5.5.** A mean of numbers in \([-1,1]\) lies in \([-1,1]\). For one coordinate,
\[
\begin{aligned}
|E_if(x)&-E_if(y)|\\
&\le\int_0^1|f(x^{w})-f(y^{w})|\,dw\\
&\le L\max_k|x_k-y_k| ,
\end{aligned}
\]
where \(x^w\), \(y^w\) have \(w\) at the position \(i\); the two points \(x^w,y^w\) agree at the position \(i\) and differ elsewhere as \(x\) and \(y\) do. Repeat this for the coordinates outside \(S\).

## References

- [OpenAI-I] OpenAI, *Hardness of finding large independent sets in three-colorable graphs*, OpenAI Math Release preprint, 24 September 2026, Sections 2 and 4. https://github.com/openai/math/tree/main/preprints/Hardness-of-finding-large-independent-sets-in-three-colorable-graphs-September-24-2026
- [Austin] T. Austin, *On the failure of concentration for the \(\ell_\infty\)-ball*, arXiv:1309.3315, version 4, Theorem 1.1 and Section 2. https://arxiv.org/abs/1309.3315
