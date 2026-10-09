# Doubling spaces and coloured strips

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A metric space \((X,d)\) is *doubling with constant at most \(\lambda\)* if every ball of radius \(t\) in \(X\) is covered by at most \(\lambda\) balls of radius \(t/2\) with centres in \(X\). Every subset of a Euclidean space \(\mathbb R^k\) is doubling (Proposition 1.2), with a constant depending on \(k\). A map \(f:X\to\mathbb R^k\) is a *bi-Lipschitz embedding with distortion at most \(D\)* if for some scale \(a>0\)
\[
a\,d(x,y)\le\|f(x)-f(y)\|\le Da\,d(x,y)\qquad(x,y\in X).
\]
A bi-Lipschitz image of a doubling space is again doubling (Exercise 5.3). Lang and Plaut asked in 2001 whether, conversely, every doubling subset of Hilbert space admits a bi-Lipschitz embedding into some \(\mathbb R^k\), for some finite \(k\) and \(D\); Gupta, Krauthgamer and Lee asked the same question in connection with dimension reduction in algorithms. Assouad proved that every doubling space embeds bi-Lipschitzly into some \(\mathbb R^k\) after the distance \(d\) is replaced by \(d^\alpha\), for any \(0<\alpha<1\) [Assouad], and Naor and Neiman showed that for \(\alpha\) close to \(1\) the dimension \(k\) can be bounded in terms of the doubling constant alone [NN]; the distortion still depends on \(\alpha\). For subsets of \(L_p\) with \(p>2\), Lafforgue and Naor found doubling sets with no such embedding [LN]. OpenAI answered the Hilbert space question negatively in September 2026 [OpenAI-L]:

**Theorem** (OpenAI). There is a subset \(S\) of the real Hilbert space \(\ell^2\), with the induced distance, whose doubling constant is at most \(76800\) and which admits no bi-Lipschitz embedding into any \(\mathbb R^k\), for any \(k\) and any distortion.

This course proves the theorem. The present lesson constructs \(S\) and proves the doubling bound (Proposition 3.1). The set lies over the plane \(\mathbb R^2\): above a point \(p\) of the plane it has finitely many extra coordinates, one at each of infinitely many scales \(r_j=1000^{-j}\), and the coordinate at scale \(r_j\) may take the value \(r_je_{j,i}\) only when \(p\) lies in a horizontal or vertical strip of colour \(i\) at that scale. The lessons [Lipschitz sheets and a lexicographic maximum](lipschitz-sheets-and-a-lexicographic-maximum.md), [Two energy estimates](two-energy-estimates.md) and [Crossings and the Lang–Plaut problem](crossings-and-the-lang-plaut-problem.md) show that an embedding would have to place many points far apart in a bounded ball of \(\mathbb R^k\).

We use from the core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10) that Lebesgue measure \(\mu\) on \(\mathbb R^k\) is translation invariant (Fremlin, *Measure Theory*, Volume 1, 134A) and satisfies \(\mu(tE)=t^k\mu(E)\) for \(t>0\) (Volume 2, 263A), and that open balls have finite positive measure.

## 1. Packing in Euclidean space

Balls are open unless said otherwise: \(B(x,t)=\{y:d(x,y)<t\}\).

**Lemma 1.1** (packing). If \(z_1,\dots,z_N\in\mathbb R^k\) lie in a closed ball of radius \(R\) and \(\|z_i-z_m\|\ge s>0\) for \(i\neq m\), then \(N\le(1+2R/s)^k\).

**Proof.** Let the closed ball have centre \(c\). The open balls \(B(z_i,s/2)\) are pairwise disjoint, by the triangle inequality, and contained in \(B(c,R+s/2)\). By translation invariance and scaling, \(\mu(B(z_i,s/2))=(s/2)^k\mu(B(0,1))\) and \(\mu(B(c,R+s/2))=(R+s/2)^k\mu(B(0,1))\), so \(N(s/2)^k\le(R+s/2)^k\). \(\square\)

**Proposition 1.2.** Every subset \(X\) of \(\mathbb R^k\) is doubling with constant at most \(5^k\).

**Proof.** Let \(x\in X\) and \(t>0\). A set \(Y\subseteq B_X(x,t)\) whose points have pairwise distances at least \(t/2\) has at most \(5^k\) points, by Lemma 1.1 with \(R=t\) and \(s=t/2\). Choose such a \(Y\) with the largest number of points. Every \(z\in B_X(x,t)\) has distance less than \(t/2\) from some point of \(Y\), since otherwise \(Y\cup\{z\}\) would be a larger such set; so the balls \(B_X(y,t/2)\), \(y\in Y\), cover \(B_X(x,t)\). \(\square\)

## 2. The set

Fix once and for all a sequence \((N_j,W_j)_{j\ge1}\) of pairs of positive integers in which every pair occurs infinitely often; for instance, list \(\{1,\dots,m\}^2\) for \(m=1,2,3,\dots\) one after the other. Put \(r_j=1000^{-j}\), and let
\[
\mathcal H=\mathbb R^2\oplus\bigoplus_{j\ge1}\mathbb R^{N_j}
\]
be the Hilbert space direct sum, with coordinate vectors \(e_{j,i}\), \(1\le i\le N_j\), in its \(j\)-th summand. It is a separable infinite-dimensional real Hilbert space, isometric to \(\ell^2\).

At level \(j\), colour the horizontal strip \(\{(x,y):qr_j<y<(q+1)r_j\}\), \(q\in\mathbb Z\), with the colour \(i\in\{1,\dots,N_j\}\) for which \(q\equiv i-1\pmod{N_j}\), and colour the vertical strip \(\{(x,y):qW_jr_j<x<(q+1)W_jr_j\}\) in the same way. Let \(H_{j,i}\) and \(V_{j,i}\) be the unions of the horizontal and the vertical strips of colour \(i\), and \(U_{j,i}=H_{j,i}\cup V_{j,i}\), an open subset of the plane.

Let \(S\subseteq\mathcal H\) be the set of points \((p,w)\) with \(p\in\mathbb R^2\) and \(w=(w_j)_{j\ge1}\) such that \(w_j\neq0\) for only finitely many \(j\), and for each \(j\)
\[
w_j=0\quad\text{or}\quad w_j=r_je_{j,i}\ \text{ for some }i\text{ with }p\in U_{j,i}.
\]
The value \(w_j=0\) is always allowed, also on the boundaries of the strips. The distance on \(S\) is \(\|z-z'\|\), the norm of \(\mathcal H\). Distinct values of one coordinate \(w_j\) differ by \(r_j\) or by \(\sqrt2\,r_j\), so they have distance at least \(r_j\).

## 3. The doubling bound

**Proposition 3.1** (OpenAI). \(S\) is doubling with constant at most \(300\cdot16^2=76800\).

**Proof.** Let \(c\in S\) and \(t>0\), and let \(Z=B_S(c,t)\).

*Coarse levels.* If \(r_j\ge t\), every \(z\in Z\) has the same coordinate \(w_j\) as \(c\), since the two values differ by at most \(\|z-c\|<t\).

*One intermediate level.* Since consecutive scales differ by the factor \(1000>64\), at most one level \(j\) satisfies \(t/64<r_j<t\). For that level, the base points of \(Z\) lie in a square of side \(2t\) around the base point of \(c\). An interval of length \(2t\) meets at most \(\lfloor2t/r_j\rfloor+2\le129\) open strips of width \(r_j\), and at most as many of the wider vertical strips. A point is allowed only the colours of its horizontal and its vertical strip, so the coordinates \(w_j\) of points of \(Z\) take at most \(2\cdot129+1<300\) values, \(0\) included.

*Fine levels.* For \(z,z'\in Z\),
\[
\sum_{r_j\le t/64}\|w_j-w'_j\|^2\le2\sum_{r_j\le t/64}r_j^2\le\frac2{1-10^{-6}}\Bigl(\frac t{64}\Bigr)^2<\Bigl(\frac t{32}\Bigr)^2.\tag{3.1}
\]

*Grouping.* Cut the square of side \(2t\) containing the base points into \(16^2\) cells of side \(t/8\), with the boundaries assigned to one cell each, and group the points of \(Z\) by their cell and their intermediate coordinate (if there is an intermediate level). There are at most \(76800\) nonempty groups. Two points of one group agree at the coarse and intermediate levels, their base points are at distance at most \(\sqrt2\,t/8\), and by (3.1) the rest contributes less than \((t/32)^2\) to the squared distance; so their distance is less than
\[
t\sqrt{\tfrac2{64}+\tfrac1{1024}}=\tfrac{\sqrt{33}}{32}\,t<\tfrac t2.
\]
Hence each nonempty group lies in the ball \(B_S(z_0,t/2)\) around any of its points \(z_0\), and these balls cover \(Z\). \(\square\)

The doubling constant is uniform although the number of colours \(N_j\) is unbounded: at each radius, only one level can distinguish points at that radius without being frozen by it.

## 4. Sheets

For a sequence \(w\) as above, with \(w_j=r_je_{j,i_j}\) at its nonzero levels, let
\[
\Omega_w=\{p\in\mathbb R^2:(p,w)\in S\}=\bigcap_{j:\,w_j\neq0}U_{j,i_j},
\]
an open set (the plane if \(w=0\)). Over \(\Omega_w\), the points \((p,w)\) form a copy of \(\Omega_w\): \(\|(p,w)-(p',w)\|=\|p-p'\|\). The proof of the theorem looks at an embedding on these copies, which the next lesson calls *sheets*. Adding one coordinate \(r_je_{j,i}\) at a level \(j\) where \(w_j=0\) moves a point by exactly \(r_j\), and two different such additions at the same level and the same base point give points at distance \(\sqrt2\,r_j\); the domain of the new sheet is \(\Omega_w\cap U_{j,i}\), which contains both the horizontal and the vertical strips of colour \(i\) inside \(\Omega_w\).

## 5. Exercises

**Exercise 5.1** (easy). Show that \(\ell^2\) is not doubling. *Hint:* consider the coordinate vectors.

**Exercise 5.2** (easy). Show that \(\mathbb R\), with the usual distance, is doubling with constant at most \(3\).

**Exercise 5.3** (medium). Let \(f:X\to Y\) be a bi-Lipschitz embedding of metric spaces with distortion at most \(D\), and let \(X\) be doubling with constant at most \(\lambda\). Show that \(f(X)\) is doubling with constant at most \(\lambda^m\), where \(m\) is an integer with \(2^{m-1}\ge2D\).

**Exercise 5.4** (easy). Check the inequalities \(\lfloor2t/r\rfloor+2\le129\) for \(t/64<r\), and \(2/(1-10^{-6})<4\), used in the proof of Proposition 3.1.

## 6. Solutions

**5.1.** The coordinate vectors \(e_1,e_2,\dots\) lie in \(B(0,2)\) and have pairwise distance \(\sqrt2\). If \(\ell^2\) were doubling with constant \(\lambda\), two halvings would cover \(B(0,2)\) by \(\lambda^2\) balls of radius \(1/2\), each of diameter at most \(1<\sqrt2\) and so containing at most one \(e_i\).

**5.2.** The ball \((x-t,x+t)\) is covered by the three intervals of radius \(t/2\) centred at \(x-t/2\), \(x\) and \(x+t/2\); the endpoints \(x\pm t\) are not in the ball.

**5.3.** We may take the scale \(a=1\). Let \(y=f(x)\) and \(t>0\). The preimage \(E\) of \(B_{f(X)}(y,t)\) lies in \(B_X(x,t)\), since \(d(x,x')\le\|f(x)-f(x')\|<t\). By \(m\) halvings, \(B_X(x,t)\) is covered by at most \(\lambda^m\) balls of radius \(2^{-m}t\). For each one meeting \(E\), choose \(x_0\) in it and in \(E\); every other point \(x'\) of \(E\) in it has \(\|f(x')-f(x_0)\|\le D\,d(x',x_0)<2^{1-m}Dt\le t/2\). So the balls \(B_{f(X)}(f(x_0),t/2)\) cover.

**5.4.** \(2t/r<128\), so \(\lfloor2t/r\rfloor\le127\). And \(2/(1-10^{-6})<2/(1/2)=4\), so \(\frac2{1-10^{-6}}(t/64)^2<4(t/64)^2=(t/32)^2\).

## References

- [Assouad] P. Assouad, *Plongements lipschitziens dans \(\mathbb R^n\)*, Bull. Soc. Math. France 111 (1983), 429–448. https://www.numdam.org/item/?id=BSMF_1983__111__429_0
- [LN] V. Lafforgue and A. Naor, *A doubling subset of \(L_p\) for \(p>2\) that is inherently infinite dimensional*, Geom. Dedicata 172 (2014); arXiv:1308.4554. https://arxiv.org/abs/1308.4554
- [NN] A. Naor and O. Neiman, *Assouad's theorem with dimension independent of the snowflaking*, Rev. Mat. Iberoam. 28 (2012); arXiv:1012.2307. https://arxiv.org/abs/1012.2307
- [OpenAI-L] OpenAI, *A doubling Hilbert subset with no finite-dimensional bi-Lipschitz embedding*, OpenAI Math Release preprint, 25 September 2026, Sections 1–2. https://github.com/openai/math/tree/main/preprints/A-doubling-Hilbert-subset-with-no-finite-dimensional-bi-Lipschitz-embedding-September-25-2026
