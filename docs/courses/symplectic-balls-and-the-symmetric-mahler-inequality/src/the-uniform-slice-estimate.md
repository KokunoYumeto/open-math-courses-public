# The uniform slice estimate

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(F:\mathbb D\to D\) and its inverse \(g\) be the maps of [A planar conformal map](a-planar-conformal-map.md). For an integer \(k\ge2\) and \(v+it\in D\), put
\[
\begin{aligned}
J_k(v,t)=k^2\int_0^v&|g(h+it)|^{2k-2}\\
&\cdot|g'(h+it)|^2\,dh ,
\end{aligned}
\]
the integral along the horizontal segment from \(it\) to \(v+it\), which lies in \(D\) by Theorem 5.2(d). These signed integrals will be momentum coordinates in the last lesson. This lesson proves that \(|J_k|/k\) is at most \(\frac\pi4|g|^{2k}\) plus an error that tends to \(0\) uniformly on \(D\) (Proposition 6.1). The constant \(\pi/4\) comes from the bound \(A<2/\pi\) of Theorem 5.2(b); the difficulty is near the tips \(\pm i\) of \(D\), where the slices are short and the height may approach \(\pm1\) as \(k\) grows. The estimate is OpenAI's [OpenAI-SB, Proposition 3.2].

## 1. The statement

**Proposition 6.1.** Each \(J_k\) is smooth on \(D\), odd in \(v\), and
\[
\begin{aligned}
&\partial_vJ_k(v,t)\\
&\quad=k^2|g(v+it)|^{2k-2}|g'(v+it)|^2\ge0.
\end{aligned}
\]
There are numbers \(\varepsilon_k\ge0\), depending only on \(F\), with \(\varepsilon_k\to0\), such that for every \(k\ge2\) and every \(v+it\in D\),
\[
\frac{|J_k(v,t)|}k\le\frac\pi4\,|g(v+it)|^{2k}+\varepsilon_k .
\]

## 2. Two elementary bounds

**Lemma 6.2.** For every \(X>0\), \(\dfrac1{\arctan X}-\dfrac2\pi\le\dfrac2X\).

**Proof.** For \(0<X\le1\), concavity of \(\arctan\) on \([0,1]\) gives \(\arctan X\ge\frac\pi4X\ge\frac X2\), so \(1/\arctan X\le2/X\). For \(X\ge1\), \(\frac\pi2-\arctan X=\arctan\frac1X\le\frac1X\) and \(\arctan X\ge\frac\pi4\), so
\[
\begin{aligned}
\frac1{\arctan X}-\frac2\pi&=\frac{\frac\pi2-\arctan X}{\frac\pi2\arctan X}\\
&\le\frac{8}{\pi^2X}\le\frac2X.\qquad\square
\end{aligned}
\]

**Lemma 6.3.** For integers \(k\ge1\) and \(0\le r_a<1\),
\[
\begin{aligned}
I(k,r_a)&=k\int_{r_a}^1r^{2k-1}\sqrt{\frac{1-r}{r-r_a}}\,dr\\
&\le1+\frac\pi e .
\end{aligned}
\]

**Proof.** Substitute \(y=k(1-r)\) and put \(H=k(1-r_a)\); then
\[
\begin{aligned}
&I(k,r_a)\\
&\quad=\int_0^H\Bigl(1-\frac yk\Bigr)^{2k-1}\sqrt{\frac y{H-y}}\,dy\\
&\quad\le\int_0^He^{-y}\sqrt{\frac y{H-y}}\,dy,
\end{aligned}
\]
because \(0\le1-y/k\le1\), \(2k-1\ge k\) and \(\log(1-x)\le-x\). On \([0,H/2]\) the square root is at most \(1\), which contributes at most \(\int_0^\infty e^{-y}dy=1\). On \([H/2,H]\) bound \(e^{-y}\) by \(e^{-H/2}\) and use \(\int_0^H\sqrt{y/(H-y)}\,dy=\frac{\pi H}2\) (substitute \(y=H\sin^2\phi\)); this contributes at most \(\frac{\pi H}2e^{-H/2}\le\frac\pi e\), since \(xe^{-x}\le e^{-1}\). \(\square\)

## 3. The proof

*Step 1: smoothness and the radial form.* For fixed \(v+it\in D\), the segment from \(it\) to \(v+it\) is a compact subset of the open set \(D\), and so are the segments for all nearby endpoints. Writing
\[
\begin{aligned}
J_k(v,t)=k^2v\int_0^1&|g(av+it)|^{2k-2}\\
&\cdot|g'(av+it)|^2\,da,
\end{aligned}
\]
the integrand is smooth in \((a,v,t)\), because \(|g|^{2k-2}=(g\bar g)^{k-1}\) with \(k\) an integer; differentiation under the integral sign (core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10); [Fremlin, *Measure Theory*, Volume 1, 123D](https://www1.essex.ac.uk/maths/people/fremlin/cont12.htm)) shows that \(J_k\) is smooth, and the fundamental theorem of calculus gives \(\partial_vJ_k\). By Theorem 5.2(d), \(g(-h+it)=-\overline{g(h+it)}\); differentiating \(F(-\bar w)=-\overline{F(w)}\) gives \(|F'(-\bar w)|=|F'(w)|\), hence \(|g'(-h+it)|=|g'(h+it)|\) by \(g'=1/F'(g)\). So the integrand is even in \(h\), and \(J_k\) is odd in \(v\). It suffices to treat \(v>0\).

Fix \(v>0\) with \(v+it\in D\), and put \(R=|g(v+it)|\) and \(r_0=T^{-1}(|t|)\). By Theorem 5.2(e), the positive half of the slice at height \(t\) is the image of the arc \(r\mapsto re^{i\theta(r,t)}\), \(r_0<r<1\), with \(h=v(r,t)\); along it \(|g|=r\), \(|g'|=1/|F'(w)|\), and \(dh=\frac{|wF'(w)|^2}{rA}\,dr\) with \(A=A(r,\theta(r,t))\). Since \(|wF'(w)|^2=r^2|F'(w)|^2\),
\[
|g|^{2k-2}|g'|^2\,dh=\frac{r^{2k-1}}A\,dr,
\]
\[
\begin{aligned}
&\frac{J_k(v,t)}k\\
&\quad=k\int_{r_0}^R\frac{r^{2k-1}}{A(r,\theta(r,t))}\,dr.
\end{aligned} \tag{6.1}
\]
The change of variables is made on segments \([h_1,v]\) with \(h_1>0\) and then \(h_1\downarrow0\); both integrands are nonnegative and the limit is the same. Since \(0<A<2/\pi\), write \(\frac1A=\frac\pi2+\bigl(\frac1A-\frac\pi2\bigr)\) with a nonnegative second term; the constant part of (6.1) contributes \(\frac\pi4(R^{2k}-r_0^{2k})\le\frac\pi4R^{2k}\). It remains to bound the contribution of the excess uniformly.

*Step 2: the excess near the tips.* Let \(\frac12\le r<1\) and \(w=re^{i\theta}\) with \(|\theta|<\pi/2\); put \(s=\frac\pi2-|\theta|\) and \(X=\frac{2r\sin s}{1-r^2}\), so that \(A=\frac4{\pi^2}\arctan X\). By Lemma 6.2, \(\sin s\ge2s/\pi\) and \((1+r)/r\le3\),
\[
\begin{aligned}
\frac1A&\le\frac{\pi^2}4\Bigl(\frac2\pi+\frac2X\Bigr)\\
&=\frac\pi2+\frac{\pi^2(1-r)(1+r)}{4r\sin s},
\end{aligned}
\]
so that
\[
\frac1A\le\frac\pi2+\frac{3\pi^3}8\,\frac{1-r}s. \tag{6.2}
\]
On the other hand, the gap between \(|\operatorname{Im}F(w)|\) and the endpoint value \(T(r)\) is, by (5.1) and \(\cos(\frac\pi2-\xi)=\sin\xi\),
\[
\begin{aligned}
\Delta&=T(r)-|\operatorname{Im}F(w)|\\
&=\int_0^s\frac4{\pi^2}\arctan\frac{2r\sin\xi}{1-r^2}\,d\xi\\
&\le\frac{4r\,s^2}{\pi^2(1-r^2)}\le\frac2{\pi^2}\,\frac{s^2}{1-r},
\end{aligned}
\]
using \(\arctan y\le y\), \(\sin\xi\le\xi\) and \(2r\le1+r\). Hence \(s\ge\frac\pi{\sqrt2}\sqrt{\Delta(1-r)}\), and (6.2) becomes, with \(C_0=3\sqrt2\pi^2/8\),
\[
\frac1A\le\frac\pi2+C_0\sqrt{\frac{1-r}{\Delta}}. \tag{6.3}
\]
On the slice at height \(t\), \(w=re^{i\theta(r,t)}\) and \(\Delta=T(r)-|t|\).

*Step 3: a compact part and a tip part.* Fix \(r_*\in(\frac12,1)\). Along the positive slice the radius \(|g|\) increases, so the points with \(|g|\le r_*\) form an initial segment of \([0,v]\), of length at most the diameter of \(D\). On it \(|g'|=1/|F'(g)|\le\max_{|w|\le r_*}|F'(w)|^{-1}\), so its contribution to \(J_k/k\) is at most
\[
\begin{gathered}
C_*\,k\,r_*^{2k-2},\\
C_*=\operatorname{diam}(D)\max_{|w|\le r_*}|F'(w)|^{-2}.
\end{gathered}
\]
If \(R>r_a=\max(r_0,r_*)\), the remaining contribution is the part of (6.1) with \(r_a<r<R\). Let \(L_*=\inf_{r_*\le r<1}T'(r)>0\). Since \(T(r_a)\ge T(r_0)=|t|\), the mean value theorem gives \(T(r)-|t|\ge L_*(r-r_a)\) for \(r>r_a\). By (6.3), the remaining contribution is at most
\[
\begin{aligned}
&\frac\pi4\bigl(R^{2k}-r_a^{2k}\bigr)+\frac{C_0}{\sqrt{L_*}}\,I(k,r_a)\\
&\quad\le\frac\pi4R^{2k}+\frac{C_0}{\sqrt{L_*}}\Bigl(1+\frac\pi e\Bigr),
\end{aligned}
\]
where the integral up to \(R\) was enlarged to the integral up to \(1\) and Lemma 6.3 was used. In all cases,
\[
\begin{aligned}
&\frac{|J_k(v,t)|}k-\frac\pi4|g(v+it)|^{2k}\\
&\quad\le C_*k\,r_*^{2k-2}\\
&\qquad+\frac{C_0(1+\pi/e)}{\sqrt{L_*}}.
\end{aligned} \tag{6.4}
\]

*Step 4: uniformity.* Define
\[
\begin{aligned}
&\varepsilon_k=\max\Bigl\{0,\ \sup_{v+it\in D}\Bigl(\frac{|J_k(v,t)|}k\\
&\qquad\qquad-\frac\pi4|g(v+it)|^{2k}\Bigr)\Bigr\},
\end{aligned}
\]
finite by (6.4). By Theorem 5.2(c), \(T'(r)\ge\frac8{\pi^2}\operatorname{arctanh}r\), so \(L_*\ge\frac8{\pi^2}\operatorname{arctanh}r_*\to\infty\) as \(r_*\to1\). Given \(\varepsilon>0\), first choose \(r_*\) with \(C_0(1+\pi/e)/\sqrt{L_*}<\varepsilon/2\), and then \(N\) with \(C_*k\,r_*^{2k-2}<\varepsilon/2\) for \(k\ge N\). Then \(\varepsilon_k<\varepsilon\) for \(k\ge N\). \(\square\)

The height \(t\), the lower radius \(r_0\) and the upper radius \(R\) may all depend on \(k\); the bound (6.4) does not depend on them, which is why the error is uniform up to the tips.

## 4. Exercises

**6.1** (easy). Show that \(J_k(v,t)/k\ge\frac\pi4\bigl(|g(v+it)|^{2k}-r_0^{2k}\bigr)\) for \(v>0\), so the constant \(\pi/4\) in Proposition 6.1 cannot be lowered along slices with \(r_0\) small.

**6.2** (medium). For \(t=0\), show that \(J_k(v,0)/k=k\int_0^R r^{2k-1}/A(r,0)\,dr\) with \(A(r,0)=\frac4{\pi^2}\arctan\frac{2r}{1-r^2}\), and that \(J_k(v,0)/k-\frac\pi4R^{2k}\to0\) as \(k\to\infty\), uniformly in \(R\le1\).

**6.3** (easy). Verify \(\int_0^H\sqrt{y/(H-y)}\,dy=\pi H/2\).

## 5. Solutions

**6.1.** In (6.1), \(1/A>\pi/2\).

**6.2.** At height \(0\), \(\theta(r,0)=0\) and \(r_0=0\). For \(r<1\), \(\frac{2r}{1-r^2}=\tan(2\arctan r)\), so \(A(r,0)=\frac8{\pi^2}\arctan r\) and \(\frac1A-\frac\pi2=\frac{\pi^2}8\bigl(\frac1{\arctan r}-\frac4\pi\bigr)\ge0\), which is bounded near \(r=1\) and at most \(c/r\) near \(0\). The excess \(k\int_0^Rr^{2k-1}(\frac1A-\frac\pi2)\,dr\) is at most \(k\int_0^1r^{2k-1}\cdot c'(1-r+r^{-1}\mathbf 1_{r<1/2})\,dr\), which tends to \(0\): the term \(k\int_0^1r^{2k-1}(1-r)\,dr=\frac k{2k(2k+1)}\) and the term \(k\int_0^{1/2}r^{2k-2}dr\) both tend to \(0\). Here \(\frac1{\arctan r}-\frac4\pi\le c''(1-r)\) on \([\frac12,1]\) because the function vanishes at \(r=1\) and has bounded derivative there.

**6.3.** With \(y=H\sin^2\phi\), \(dy=2H\sin\phi\cos\phi\,d\phi\) and \(\sqrt{y/(H-y)}=\tan\phi\); the integral becomes \(\int_0^{\pi/2}2H\sin^2\phi\,d\phi=\frac{\pi H}2\).

## References

- [OpenAI-SB] OpenAI, *Symplectic balls in symmetric polar products*, OpenAI Math Release preprint, 22 September 2026, Section 3, Proposition 3.2. https://github.com/openai/math/tree/main/preprints/Symplectic-Balls-in-Symmetric-Polar-Products-September-22-2026
