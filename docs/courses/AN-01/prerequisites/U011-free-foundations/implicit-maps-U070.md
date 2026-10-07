# Smooth inverse and implicit maps

*Selected AN-03 programme proof; CC0 1.0. Original ownership is retained. See [licence](https://creativecommons.org/publicdomain/zero/1.0/), [rights](notices/RIGHTS.md), and selection history.*

The [scalar calculus and topology](metric-foundation-bridges.md), §§12–13, [finite algebra](stable-prerequisite-bridges.md), §§10.1–10.6, and [integration proofs](banach-foundation-bridges.md), §§15.0–15.1 and 16, supply the stated foundational inputs.

### 16.4. Constructing the inverse without changing the map or norms

Let \(E,F\) be the original real finite-dimensional normed coordinate spaces of the same dimension \(n\geq1\), with their original norms \(\|\cdot\|_E,\|\cdot\|_F\). Let \(f:O\subset E\to F\) be \(C^r\), \(1\leq r\leq\infty\), on the original open set, and let \(a\in O\) have the actual invertible derivative \(A=Df(a):E\to F\). We keep \(f,A,a,f(a)\) and both norms, and never replace \(A\) by an identity or \(f\) by a changed coordinate expression.

Choose \(0<\theta<1\). Continuity of the actual derivative gives \(R>0\) such that the original closed ball \(\overline B_E(a,R)\) is inside \(O\) and

\[
 \sup_{x\in\overline B_E(a,R)}
       \|I_E-A^{-1}Df(x)\|_{E\to E}\leq\theta .
 \tag{IV1}
\]

The closed ball is complete in the original norm by the existing finite-coordinate completeness proof. For \(y\in F\), use the actual correction map

\[
 T_y(x)=x+A^{-1}(y-f(x)),\qquad
 \varepsilon=\frac{(1-\theta)R}{\|A^{-1}\|_{F\to E}},\qquad
 V=B_F(f(a),\varepsilon).
 \tag{IV2}
\]

The denominator is positive for \(n\geq1\). The full segment fundamental theorem gives
\(\|T_y(x)-T_y(z)\|_E\leq\theta\|x-z\|_E\) for \(x,z\) in the original closed ball. Also
\(\|T_y(x)-a\|_E\leq\theta R+\|A^{-1}\|_{F\to E}\|y-f(a)\|_F<R\) for \(y\in V\). Thus the whole original closed ball maps into itself.

Start \(x_0=a\), \(x_{m+1}=T_y(x_m)\). All iterates remain in that ball. The entire contraction estimate is

\[
 \begin{aligned}
 \|x_{m+1}-x_m\|_E
   &\leq\theta^m\|A^{-1}(y-f(a))\|_E,\\
 \|x_{m+k}-x_m\|_E
   &\leq\|A^{-1}(y-f(a))\|_E
                         \sum_{\nu=m}^{m+k-1}\theta^\nu .
 \end{aligned}
 \tag{IV3}
\]

The finite sum and its convergent geometric tail prove that the sequence is Cauchy. Completeness gives its limit \(h(y)\) in the original closed ball. Continuity gives \(T_y(h(y))=h(y)\), hence \(f(h(y))=y\). Letting \(k\) tend to infinity in IV3 retains the exact tail bound
\(\|h(y)-x_m\|_E\leq\theta^m(1-\theta)^{-1}\|A^{-1}(y-f(a))\|_E\).
At a fixed point,
\(\|h(y)-a\|_E\leq(1-\theta)^{-1}\|A^{-1}(y-f(a))\|_E<R\).
If two fixed points existed, their distance would be at most \(\theta\) times itself; since \(1-\theta>0\), they agree. These arguments prove every existence and uniqueness step of the contraction construction.

For any \(x,z\) in the original closed ball, the same full segment formula gives

\[
 \begin{aligned}
 A^{-1}(f(x)-f(z))
 &=x-z+\int_0^1
      A^{-1}\bigl(Df(z+t(x-z))-A\bigr)(x-z)\,dt,\\
 \|f(x)-f(z)\|_F
 &\geq\frac{1-\theta}{\|A^{-1}\|_{F\to E}}\|x-z\|_E .
 \end{aligned}
 \tag{IV4}
\]

Every ordered matrix factor and the entire integral remain. The reverse triangle inequality proves the second line. Put \(U=B_E(a,R)\cap f^{-1}(V)\), an original open neighborhood of \(a\). The map \(f:U\to V\) is injective by IV4 and surjective by the constructed interior fixed points. Thus \(h\) is its actual inverse, and IV4 gives its precise Lipschitz bound \(\|A^{-1}\|_{F\to E}/(1-\theta)\). In particular both maps are continuous.

For \(x\) in the ball set \(B_x=I_E-A^{-1}Df(x)\). Retain both finite product identities
\((I_E-B_x)\sum_{m=0}^N B_x^m=I_E-B_x^{N+1}
=\bigl(\sum_{m=0}^N B_x^m\bigr)(I_E-B_x)\).
The full operator-norm tail is at most \(\theta^{N+1}/(1-\theta)\). Operator completeness therefore gives both actual inverse products and

\[
 Df(x)^{-1}=\left(\sum_{m=0}^{\infty}B_x^m\right)A^{-1},
 \qquad
 \|Df(x)^{-1}\|_{F\to E}
       \leq\frac{\|A^{-1}\|_{F\to E}}{1-\theta}.
 \tag{IV5}
\]

The rightmost original inverse factor has not been absorbed into a changed derivative. The uniformly convergent series also proves continuous dependence on \(x\), since every finite matrix power is continuous.

For \(y,y+k\in V\), write \(x=h(y)\), \(v=h(y+k)-h(y)\). The original differentiability remainder gives

\[
 \begin{aligned}
 k&=Df(x)v+r_x(v),\qquad
          \frac{\|r_x(v)\|_F}{\|v\|_E}\longrightarrow0,\\
 v&=Df(x)^{-1}k-Df(x)^{-1}r_x(v).
 \end{aligned}
 \tag{IV6}
\]

The remainder is zero at \(v=0\). IV4 bounds \(\|v\|_E\) by
\(\|A^{-1}\|_{F\to E}(1-\theta)^{-1}\|k\|_F\);
IV5 then makes the last remainder \(o(\|k\|_F)\).
Consequently \(Dh(y)=Df(h(y))^{-1}\), and its continuity follows from IV5 and continuity of \(h\). This proves \(C^1\) regularity of the actual inverse before any higher smoothness is used.

### 16.5. Every higher inverse derivative and the implicit map

Matrix inversion is smooth on the original invertible matrices: the full cofactor inverse proved in Polynomial and contour tools Section10 is a matrix of polynomial entries divided by its actual nonzero determinant. The proved finite product, reciprocal and chain rules therefore apply at every available order. Differentiating both original inverse products gives \(D(M^{-1})[v]=-M^{-1}DM[v]M^{-1}\). For every integer \(N\geq1\), iteration retains every ordered factor:

\[
 D^N(M^{-1})[v_1,\ldots,v_N]
 =\sum_{k=1}^N(-1)^k
   \sum_{\substack{(I_1,\ldots,I_k)\ {\rm ordered}\\
                   I_j\ne\varnothing,\ 
                   I_1\sqcup\cdots\sqcup I_k=\{1,\ldots,N\}}}
 M^{-1}D_{I_1}M\,M^{-1}\cdots
             D_{I_k}M\,M^{-1}.
 \tag{IV7}
\]

Each differentiation either adds its label to one existing derivative block or inserts a singleton block at one of the inverse factors. The sign changes precisely in the latter case. Every ordered partition of the new label set has one such predecessor, proving IV7 by induction with no commutation of matrix factors. Repeated equal directions keep all labeled multiplicities.

Starting from the proved \(C^1\) inverse, the identity \(Dh=(Df\circ h)^{-1}\) and this smooth inversion map prove \(h\in C^r\) by induction. Precisely, if \(h\in C^s\) with \(s<r\), then \(Df\) is \(C^{r-1}\), so the right side is \(C^s\); hence \(Dh\) is \(C^s\) and \(h\) is \(C^{s+1}\). This covers every finite order and all orders when \(r=\infty\).

For \(2\leq N\leq r\), set \(D_Bh(y)=D^{|B|}h(y)[v_b:b\in B]\) with every original direction label retained, and differentiate the exact composition \(f(h(y))=y\) by the full higher chain rule. The partition with one block is \(Df(h(y))D^Nh\); all other partitions keep their original derivatives. Thus the complete inverse derivative is

\[
 D^Nh(y)[v_1,\ldots,v_N]
 =-Df(h(y))^{-1}
   \sum_{\substack{\Pi\in\mathfrak P(\{1,\ldots,N\})\\|\Pi|\geq2}}
 D^{|\Pi|}f(h(y))
       [D_Bh(y):B\in\Pi].
 \tag{IV8}
\]

The full higher chain rule itself follows by the same labeled-partition induction: differentiating a block derivative adds the new label to that block, while differentiating the outer derivative creates its singleton block. This accounts for every partition once. The derivatives of the outer map are symmetric multilinear maps, so the bracket order across blocks can be read in increasing least-label order without changing a matrix product. All lower inverse derivatives, repeated-direction multiplicities and the original left inverse matrix remain in IV8.

For the actual implicit problem \(f(s,x)=y\), where \(s\) lies in its original finite-coordinate parameter space and \(D_xf(s_0,x_0)=A\) is invertible, apply the just proved inverse construction to the unchanged augmented map \(L(s,x)=(s,f(s,x))\). At the original point its two block matrices are

\[
 DL=\begin{pmatrix}I&0\\ B&A\end{pmatrix},
 \qquad
 (DL)^{-1}=\begin{pmatrix}I&0\\-A^{-1}B&A^{-1}\end{pmatrix},
 \qquad B=D_sf(s_0,x_0).
 \tag{IV9}
\]

Multiplying in both orders proves the inverse, including the lower-left term. Use the original product norm and an open product contained in the constructed image neighborhood. The first component of \(L^{-1}(s,y)\) must be exactly \(s\), because \(L\)'s first component is \(s\). Its second component \(H(s,y)\) is therefore the unique local solution of the actual original implicit equation. It has the proved \(C^r\) regularity and

\[
 D_yH=(D_xf)^{-1},\qquad
 D_sH=-(D_xf)^{-1}D_sf,
 \tag{IV10}
\]

with every derivative of \(f\) evaluated at the original \((s,H(s,y))\). All higher derivatives are IV8 applied to the entire augmented map and then its second projection; this retains its full parameter blocks and ordered inverse factors. No implicit-function theorem was assumed in constructing this map.

If the solved coordinate dimension is zero, its original domain and range are the singleton spaces and the local inverse is the identity there; the implicit augmented map is exactly the identity on its parameter component. Its empty matrix determinant is one, and no division by the zero operator norm is made. Empty open domains have no base point and make no local assertion.

