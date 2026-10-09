# Analytic forcing without global analytic solutions

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

An analytic right-hand side does not always have an analytic solution on the whole real space. Local analytic solvability leaves room for a global obstruction. We give one explicit forcing that defeats both the heat operator with two spatial variables and the two-variable Laplacian acting with an additional parameter.

Basic references are E. De Giorgi's *Solutions analytiques des équations aux dérivées partielles à coefficients constants*, L. C. Piccinini's *Non surjectivity of the Cauchy–Riemann operator on the space of the analytic functions in real space: generalization to parabolic operators*, and Compact Fourier division and multiplicity-sensitive annihilators. Credit for the counterexamples and the localized-frequency argument belongs to De Giorgi, Lamberto Cattabriga and Piccinini. Every argument needed here is proved below. We use a diagonal integer enumeration to separate the frequencies and give a direct localized heat-kernel proof of the homogeneous-solution estimate.

All functions may be complex valued. Analytic on real space means locally represented by a convergent power series, or equivalently locally extended holomorphically to complex variables. No common complex neighborhood radius over the whole space is assumed.

## 1. A single forcing for two operators

For \(\varepsilon\in\{0,1\}\), write
\[
 P_\varepsilon=\partial_x^2+\partial_y^2+\varepsilon\partial_t
       \quad\text{on }\mathbb R^3.
 \tag{1.1}
\]
The variable \(t\) is a parameter when \(\varepsilon=0\). When \(\varepsilon=1\), replacing \(t\) by \(-t\) gives the forward heat sign.

**Theorem 1.1.** There is a function \(f\), analytic on all of \(\mathbb R^3\), such that neither equation \(P_\varepsilon u=f\), \(\varepsilon=0,1\), has a global analytic solution. Each equation does have a global smooth solution. At least one of the three real analytic forcings \(\operatorname{Re}f,\operatorname{Im}f,\operatorname{Re}f+\operatorname{Im}f\) has no global analytic solution for either operator.

Here is the forcing. For positive integers \(h,k\), let
\[
 d_{hk}=h+k-2,\qquad
 n_{hk}=3+\frac{d_{hk}(d_{hk}+1)}2+h,\qquad
 q_{hk}=(n_{hk}!)!.
 \tag{1.2}
\]
The integers \(n_{hk}\) enumerate every integer at least four exactly once. For a fixed \(h\), they tend to infinity with \(k\). Set
\[
 f_{hk}(x,y,t)
   =\exp\!\bigl(q_{hk}[ix+ih^2t-(y-h)^2-1]\bigr),
 \qquad f=\sum_{h,k\ge1}f_{hk}.
 \tag{1.3}
\]
The sum and its real derivatives converge locally. Its global analyticity follows from the stronger complex convergence proved next. Sections 3–6 prove the theorem.

## 2. Lacunarity and analyticity of the forcing

**Lemma 2.1.** Put \(q_n=(n!)!\), \(n\ge4\). Then
\[
 q_n\ge n^2,\qquad
 q_n\ge q_{n-1}^{\,n}\ (n\ge5),\qquad
 q_{n+1}\ge q_n^{\,n+1}.
 \tag{2.1}
\]
Consequently, as \(n\to\infty\),
\[
 \log q_{n-1}-\log q_n\longrightarrow-\infty,\qquad
 q_{n+1}/q_n\longrightarrow+\infty.
 \tag{2.2}
\]

**Proof.** The diagonals \(d=h+k-2\) contain \(d+1\) pairs. Their consecutive labels before adding three are \(d(d+1)/2+1,\ldots,(d+1)(d+2)/2\), so (1.2) is a bijection. Also \(h\le n_{hk}\).

The factorial inequality \((am)!\ge(m!)^a\) holds for positive integers \(a,m\): its ratio is the positive integer multinomial coefficient for \(a\) blocks of size \(m\). Apply it with \(a=n,m=(n-1)!\), and then with \(a=n+1,m=n!\). Finally \(n!\ge n^2\) for \(n\ge4\), by the base case \(24\ge16\) and induction, so \(q_n\ge n^2\). Equation (2.2) follows from \(\log q_{n-1}\le(\log q_n)/n\) and \(q_{n+1}\ge q_n^{n+1}\). \(\square\)

**Lemma 2.2.** The function \(f\) in (1.3) extends holomorphically to a neighborhood of every real compact set. In particular it is globally real analytic.

**Proof.** It suffices to consider a compact real box with \(|y|\le M\). Enlarge its real \(y\) range to \(|\operatorname{Re}y|\le M+1\), and choose an integer \(H\ge4(M+2)\). Restrict the imaginary coordinates by
\[
 |\operatorname{Im}x|<\frac18,\qquad
 |\operatorname{Im}y|<\frac18,\qquad
 |\operatorname{Im}t|<\frac1{8H^2}.
 \tag{2.3}
\]
The real part of the bracket in (1.3) is
\[
 -\operatorname{Im}x-h^2\operatorname{Im}t
       -(\operatorname{Re}y-h)^2+(\operatorname{Im}y)^2-1.
 \tag{2.4}
\]
For \(h\le H\), discard the nonpositive square. The remaining upper bound is \(-1+1/8+1/8+1/64<-1/2\). For \(h>H\), \(|\operatorname{Re}y-h|\ge3h/4\), and the positive time term is at most \(h^2/8\). This also makes (2.4) less than \(-1/2\).

Thus \(|f_{hk}|\le e^{-q_{hk}/2}\) on this complex neighborhood. The bijection and \(q_n\ge n\) imply summability. The series converges uniformly on compact subsets there. Its sum is holomorphic: integrate the uniformly convergent sums on small coordinate circles to pass their Cauchy formulas to the limit, obtaining convergent local power series. The same formulas justify local termwise differentiation. \(\square\)

## 3. Smooth particular solutions and their distant tails

For a pair with frequency \(q=q_{hk}\), define the square root with positive real part
\[
 \kappa=\sqrt{q^2-i\varepsilon h^2q},\qquad
 W_{h,q}^{\varepsilon}(y)
   =-\frac{e^{-q}}{2\kappa}
      \int_{\mathbb R}e^{-\kappa|y-s|}e^{-q(s-h)^2}\,ds,
 \qquad
 w_{hk}^{\varepsilon}(x,y,t)
   =e^{iqx+ih^2qt}W_{h,q}^{\varepsilon}(y).
 \tag{3.1}
\]
Since \(h^2\le q\),
\[
 \operatorname{Re}\kappa\ge q,\qquad
 q\le|\kappa|\le 2^{1/4}q.
 \tag{3.2}
\]

**Lemma 3.1.** The series \(w^\varepsilon=\sum_{h,k}w_{hk}^\varepsilon\) converges with all real derivatives, uniformly on real space for each fixed derivative order. It is a global smooth solution of \(P_\varepsilon w^\varepsilon=f\). Each summand satisfies
\[
 |W_{h,q}^{\varepsilon}(y)|\le e^{-q}q^{-2}
       \quad(y\in\mathbb R).
 \tag{3.3}
\]

**Proof.** The real part and modulus identities for the square root give (3.2). The function \(-e^{-\kappa|y|}/(2\kappa)\) has derivative jump 1 at zero. Thus its distributional second derivative minus \(\kappa^2\) times itself is \(\delta_0\). Convolution with the Gaussian gives
\[
 (W_{h,q}^{\varepsilon})''-\kappa^2W_{h,q}^{\varepsilon}
          =e^{-q}e^{-q(y-h)^2}.
 \tag{3.4}
\]
The integral and its first derivative are continuous. Equation (3.4) and the smooth right side show successively that \(W\) is smooth. Multiplying it by the exponential in (3.1), with \(\kappa^2=q^2-i\varepsilon h^2q\), proves the particular equation.

Dropping the Gaussian in the absolute integral gives (3.3), since \(\int e^{-q|r|}dr=2/q\). Differentiating the kernel once gives \(|W'|\le e^{-q}/q\). Each fixed Gaussian derivative of order \(a\) is bounded by \(C_aq^{a/2}\): differentiate after the change of variable \(\sqrt q(y-h)\), and use boundedness of each fixed polynomial times \(e^{-r^2}\).

Differentiate (3.4) repeatedly. From the bounds on \(W,W'\), on \(\kappa\), and on the Gaussian derivatives, induction gives \(|W^{(a)}|\le C_a e^{-q}q^a\), a sufficiently loose bound for every \(a\). An \(x\) derivative contributes \(q\), and a \(t\) derivative contributes \(h^2q\le q^2\). Every fixed mixed derivative is therefore bounded by \(C e^{-q}q^L\) for some fixed integer \(L\). Its sum over the distinct increasing integers \(q_n\) converges, being at most a constant times \(\sum_{j\ge1}e^{-j}j^L\). Uniform convergence proves smoothness and the termwise equation. \(\square\)

**Lemma 3.2.** Fix \(h\ge1\) and \(\varepsilon\in\{0,1\}\). As the real frequency \(q\to\infty\),
\[
 W_{h,q}^{\varepsilon}(0)
 =-\frac{\sqrt\pi}{2q^{3/2}}
       e^{-q(h+3/4)}
       e^{i\varepsilon(h^3/2-h^2/4)}
       (1+o(1)).
 \tag{3.5}
\]
In particular this value is nonzero for all sufficiently large \(q\).

**Proof.** Taylor expansion of the square root at 1 gives, for this fixed \(h\),
\[
 \kappa=q-i\varepsilon h^2/2+O_h(q^{-1}).
 \tag{3.6}
\]
The full Gaussian integral, with no absolute value in the linear exponent, is
\[
 J=\int_{\mathbb R}e^{-\kappa s-q(s-h)^2}\,ds
       =\sqrt{\pi/q}\,e^{-\kappa h+\kappa^2/(4q)}.
 \tag{3.7}
\]
For real \(\kappa\) this is completion of the square and the Gaussian integral. Both sides are entire in \(\kappa\); uniform domination on each compact set permits complex differentiation under the integral. Equality for real \(\kappa\) therefore proves the complex identity by its power series identity theorem.

Let \(I\) be the integral with \(e^{-\kappa|s|}\) in (3.1), at \(y=0\). The two negative-half-line integrals distinguish it from \(J\). Their absolute values are bounded respectively by
\[
 \frac{e^{-qh^2}}{2qh+\operatorname{Re}\kappa},
 \qquad
 \frac{e^{-qh^2}}{2qh-\operatorname{Re}\kappa}.
 \tag{3.8}
\]
The second denominator is positive for all large \(q\), by (3.6) and \(h\ge1\). To obtain these bounds set \(s=-r\), \(r\ge0\), and discard the nonpositive term \(-qr^2\). Consequently \(I-J=O_h(q^{-1}e^{-qh^2})\).

Meanwhile \(|J|=\sqrt{\pi/q}\exp(-q(h-1/4)+O_h(q^{-1}))\). The error relative to \(J\) tends to zero, because \(h^2-h+1/4=(h-1/2)^2>0\). Finally
\[
 -q-\kappa h+\kappa^2/(4q)
   =-q(h+3/4)+i\varepsilon(h^3/2-h^2/4)+O_h(q^{-1}),
 \tag{3.9}
\]
and \(\kappa/q\to1\). Insert these identities into (3.1) to prove (3.5). \(\square\)

![Gaussian forcing profiles and their longer particular-solution tails, with the corresponding complex-time growth scales](figures/gaussian-sources-and-distant-tails.png)

**Figure 1.** The left panel gives exact single-mode profiles at \(x=t=0\), for \(\varepsilon=0,q=32,h=1,3\). These finite parameter examples belong to the resolvent family (3.1); they are not the full lacunary sum (1.3). The ordinate is the actual logarithm of the absolute mode value divided by \(q\). The Gaussian forcing decays quadratically away from its center, whereas the particular solution has a longer tail. At \(y=0,t=-i\sigma\), the forcing's exponential rate changes sign at \(\sigma=(h^2+1)/h^2\). By Lemma 3.2, the tail's leading rate changes sign at \(\sigma=(h+3/4)/h^2\) as \(q\to\infty\). The right panel gives these exact rates. They explain the obstruction, but growth of individual modes alone does not exclude a different analytic solution. Lemma 4.1 and the functionals of Section 5 supply that exclusion. [Full-size image](figures/gaussian-sources-and-distant-tails.png), [vector drawing](figures/gaussian-sources-and-distant-tails.svg).

## 4. Global homogeneous solutions are entire in a spatial coordinate

**Lemma 4.1.** Suppose \(v\) is smooth on all of \(\mathbb R^3\), with \(P_\varepsilon v=0\). For every \(p>0,R>0\), there is a constant \(C_{p,R}\) such that
\[
 |\partial_x^a v(0,0,t)|
       \le C_{p,R}\,a!\,R^{-a}
       \quad(a\ge0,\ -p\le t\le p).
 \tag{4.1}
\]
No boundedness or growth condition at spatial infinity is needed.

**Proof for the Laplacian.** At each real \(t\), the function in the two spatial variables is harmonic. On the circle of radius \(2R\), let \(M_{p,R}\) be the maximum of its modulus over that circle and \([-p,p]\). It is finite by continuity on a compact set. The Poisson formula, restricted to the real \(x\) axis, is
\[
 v(x,0,t)=\frac1{2\pi}\int_0^{2\pi}
      v(2R\cos\theta,2R\sin\theta,t)
      \frac{4R^2-x^2}{4R^2-4Rx\cos\theta+x^2}\,d\theta
      \quad(|x|<2R).
 \tag{4.2}
\]
For completeness, the Poisson kernel on the disc has expansion
\(1+2\sum_{m\ge1}(r/(2R))^m\cos(m(\theta-\varphi))\), for \(r<2R\). Each term is harmonic and the sum converges uniformly on smaller discs. The positive kernel has integral \(2\pi\); away from a given boundary angle it tends uniformly to zero as \(r\uparrow2R\). Integration against continuous boundary data therefore gives their boundary values. Uniqueness follows from the maximum principle, for real and imaginary parts separately. That principle follows by adding a positive multiple of the squared radius: a strictly positive Laplacian prevents a positive interior maximum, then the multiple tends to zero. These facts prove (4.2).

Replace \(x\) by the complex coordinate \(z\). The denominator factors as \((2Re^{i\theta}-z)(2Re^{-i\theta}-z)\). On \(|z|\le R\) its modulus is at least \(R^2\), while the numerator modulus is at most \(5R^2\). Thus (4.2) extends holomorphically to \(|z|<2R\) and is bounded by \(5M_{p,R}\) on \(|z|\le R\). Cauchy's coefficient formula gives (4.1).

**Proof for the heat operator.** Reverse time: \(V(X,s)=v(X,-s)\), \(X=(x,y)\), satisfies \((\partial_s-\Delta_X)V=0\). Take a smooth spatial cutoff \(\chi\), equal to 1 on \(|X|\le4R\), supported in \(|X|<5R\). Such a cutoff is a fixed smooth function of \(|X|^2/R^2\). Put
\[
 A=\chi V,\qquad
 Q=(\partial_s-\Delta_X)A
      =-2\nabla\chi\cdot\nabla V-(\Delta_X\chi)V.
 \tag{4.3}
\]
The support of \(Q\) in space is contained in \(4R\le|X|\le5R\). Both \(A\) and \(Q\) are uniformly bounded on their spatial supports for \(-p-1\le s\le p\).

The heat kernel and the compactly supported Duhamel identity are
\[
 G_\tau(Z)=(4\pi\tau)^{-1}
       \exp(-(Z_1^2+Z_2^2)/(4\tau)),\qquad
 A(X,s)=(G_1*A(\,\cdot,s-1))(X)
       +\int_0^1(G_\tau*Q(\,\cdot,s-\tau))(X)\,d\tau.
 \tag{4.4}
\]
Here the squares are bilinear complex squares. To prove the real identity, the Gaussian has integral 1, satisfies \(\partial_\tau G_\tau=\Delta G_\tau\), and is an approximate identity as \(\tau\downarrow0\). These statements follow by differentiation, the one-dimensional Gaussian integral in each coordinate, and splitting the mass into a small ball and its exponentially small complement. Differentiate \(G_{s-\sigma}*A(\,\cdot,\sigma)\) in \(\sigma<s\). Compact support permits integration by parts, so its derivative is \(G_{s-\sigma}*Q(\,\cdot,\sigma)\). Integrate from \(s-1\) to \(s\), using the approximate-identity limit. This proves (4.4).

At \(X=(z,0)\), the first term of (4.4) is entire in \(z\). On \(|z|\le R\) and the support of \(Q(Y,\cdot)\),
\[
 \operatorname{Re}((z-Y_1)^2+Y_2^2)
   =(\operatorname{Re}z-Y_1)^2+Y_2^2-(\operatorname{Im}z)^2
   \ge(4R-R)^2-R^2=8R^2.
 \tag{4.5}
\]
The absolute heat kernel is consequently at most \((4\pi\tau)^{-1}e^{-2R^2/\tau}\), an integrable function of \(0<\tau\le1\). Spatial compactness and the bound on \(Q\) give uniform domination, also uniformly for real \(-p\le s\le p\). On smaller complex neighborhoods each derivative has the same exponential domination with an additional finite power of \(1/\tau\). The integral term is holomorphic and uniformly bounded on \(|z|\le R\). Equivalently its coordinate Cauchy formulas pass under the dominated integral.

For real \(|x|\le R\), \(A(x,0,s)=V(x,0,s)\). Thus (4.4) gives a uniformly bounded holomorphic extension of that restriction to a neighborhood of \(|z|\le R\). Cauchy's formula gives (4.1) and reversing \(s\) gives its original \(t\) interval. The bounds use only compact real space-time sets; no estimate at infinity was invoked. \(\square\)

Since \(R\) is arbitrary, the compatible extensions along this spatial coordinate are entire. We only need their derivative bounds, uniform on a fixed real time interval.

## 5. Functionals that detect one tail

Fix \(p>0\). At frequency \(q=q_{hk}\), define
\[
 B_{h,q}(a)=\int_{-p}^{p}\partial_x^q a(0,0,t)
       \exp\!\left(-h^2q\left(\frac{t^2}{2p}+it\right)\right)\,dt.
 \tag{5.1}
\]
All these functionals are defined on global smooth functions. Write \(\log0=-\infty\) in the limiting estimates.

**Lemma 5.1 (the selected tail).** For fixed \(h\) and either \(\varepsilon\), as \(k\to\infty\),
\[
 \frac{\log|B_{h,q}(w_{hk}^{\varepsilon})|}{q}-\log q
        \longrightarrow-(h+3/4).
 \tag{5.2}
\]

**Proof.** The \(t\) phases cancel for this summand, so
\[
 B_{h,q}(w_{hk}^{\varepsilon})
   =(iq)^qW_{h,q}^{\varepsilon}(0)
           \int_{-p}^{p}e^{-h^2qt^2/(2p)}\,dt.
 \tag{5.3}
\]
After changing variable \(r=h\sqrt{q/(2p)}\,t\), the last integral is asymptotic to \(\sqrt{2\pi p/(h^2q)}\). The omitted Gaussian tails tend to zero by the elementary bound \(\int_L^\infty e^{-r^2}dr\le e^{-L^2}/(2L)\). Lemma 3.2 now proves (5.2), because the powers and fixed constants outside the exponential have logarithms \(O(\log q)\). \(\square\)

**Lemma 5.2 (all other tails).** For fixed \(h\),
\[
 \limsup_{k\to\infty}
 \left(\frac{\log|B_{h,q}(w^\varepsilon-w_{hk}^\varepsilon)|}{q}
                  -\log q\right)=-\infty.
 \tag{5.4}
\]

**Proof.** Differentiated uniform convergence in Lemma 3.1 permits the sum in the functional. For a summand with different frequency \(\lambda\), its absolute contribution is at most
\[
 2p\,\lambda^q e^{-\lambda}\lambda^{-2}.
 \tag{5.5}
\]
The time weight has modulus at most 1 on the real interval. Suppose \(q=q_n\). Every smaller frequency is at most \(q_{n-1}\). Their total is bounded by \(C_p q_{n-1}^q\), because \(\sum_\lambda e^{-\lambda}\lambda^{-2}\) is finite. Its normalized logarithm minus \(\log q\) tends to \(-\infty\) by Lemma 2.1.

For larger frequencies \(\lambda\ge q_{n+1}\ge q^2\), we have \(q\log\lambda\le\lambda/2\). Indeed \((\log r)/r\) decreases for \(r>e\), and at \(r=q^2\) the desired bound follows from \(2\log q/q<1/2\); all our \(q\)'s are at least \(24!\). Thus their total is bounded by
\[
 2p\sum_{\lambda\ge q_{n+1}}e^{-\lambda/2}
       \le C_p e^{-q_{n+1}/2}.
 \tag{5.6}
\]
The last estimate enlarges the sum to all integer frequencies, a geometric series. Its normalized logarithm also tends to \(-\infty\), since \(q_{n+1}/q\to\infty\). Adding the two bounds proves (5.4). \(\square\)

**Lemma 5.3 (homogeneous solutions).** If \(P_\varepsilon v=0\) globally and \(v\) is smooth, then for each fixed \(h\),
\[
 \limsup_{k\to\infty}
 \left(\frac{\log|B_{h,q}(v)|}{q}-\log q\right)=-\infty.
 \tag{5.7}
\]

**Proof.** Lemma 4.1 and the modulus bound of the real time weight give
\[
 |B_{h,q}(v)|\le2p\,C_{p,R}\,q!\,R^{-q}
       \quad\text{for every }R>0.
 \tag{5.8}
\]
The elementary factorial asymptotic is \((\log q!)/q-\log q\to-1\). One proof compares \(\sum_{j=1}^q\log j\) with \(\int_1^q\log s\,ds=q\log q-q+1\); the difference is at most \(\log q\). Hence the left upper limit in (5.7) is at most \(-1-\log R\). Let \(R\to\infty\). Each constant is fixed before taking \(k\to\infty\), so these inequalities prove (5.7). \(\square\)

**Lemma 5.4 (a locally analytic candidate).** If \(u\) is analytic near the origin, choose \(p>0\) so that its holomorphic extension is bounded by \(M\) on a neighborhood of
\[
 \{|x|\le p,\ y=0,\ |\operatorname{Re}t|\le p,\
                       -p\le\operatorname{Im}t\le0\}.
 \tag{5.9}
\]
Such a positive \(p\) exists. Then
\[
 |B_{h,q}(u)|\le4pM\,q!\,p^{-q}e^{-h^2qp/2},
 \qquad
 \limsup_{k\to\infty}
 \left(\frac{\log|B_{h,q}(u)|}{q}-\log q\right)
       \le-1-\log p-h^2p/2.
 \tag{5.10}
\]

**Proof.** Cauchy's formula in \(x\) bounds \(|\partial_x^q u(0,0,t)|\) by \(Mq!p^{-q}\), uniformly on the indicated complex time rectangle. Move the real integration segment in (5.1) to the other three sides of that rectangle. The integrand is holomorphic in \(t\). On the lower side \(t=s-ip\),
\[
 \operatorname{Re}\left(\frac{t^2}{2p}+it\right)
       =\frac{s^2}{2p}+\frac p2.
 \tag{5.11}
\]
On either vertical side \(t=\pm p-i\sigma\), \(0\le\sigma\le p\), the same real part is
\[
 \frac p2+\sigma-\frac{\sigma^2}{2p}\ge\frac p2.
 \tag{5.12}
\]
The three side lengths total \(4p\). Their common exponential bound proves the first inequality, regardless of their orientations. The factorial estimate in Lemma 5.3 proves the second. \(\square\)

## 6. Contradiction and the real-valued conclusion

**Proof of Theorem 1.1.** The forcing is analytic by Lemma 2.2, and Lemma 3.1 provides its global smooth particular solution for each operator.

Suppose a global analytic solution \(u\) existed for one of the two operators. Then \(v=w^\varepsilon-u\) is a global smooth homogeneous solution. Fix the positive \(p\) supplied by Lemma 5.4. Choose an integer \(h\) so large that
\[
 1+\log p+h^2p/2>h+3/4.
 \tag{6.1}
\]
This is possible since the positive quadratic term dominates the linear term. At each frequency \(q=q_{hk}\), the exact decomposition gives
\[
 B_{h,q}(w_{hk}^{\varepsilon})
   =B_{h,q}(u)+B_{h,q}(v)
             -B_{h,q}(w^\varepsilon-w_{hk}^{\varepsilon}).
 \tag{6.2}
\]
By Lemma 5.1 the normalized logarithm of the left side tends to \(-(h+3/4)\). By Lemma 5.4 and (6.1), the upper limit for the first term on the right is strictly smaller. Lemmas 5.2 and 5.3 give upper limit \(-\infty\) for the other terms. The triangle inequality contradicts (6.2): choose a fixed exponent strictly between the first right upper bound and the left limit; the three right terms are eventually bounded by \(3q^qe^{-cq}\) at a larger decay exponent than the left. Thus no global analytic solution exists.

Both operators have real coefficients. Put \(a=\operatorname{Re}f,b=\operatorname{Im}f\). For a fixed operator, at most one of \(a,b,a+b\) can have an analytic solution: solutions for any two give solutions for both \(a\) and \(b\) by addition or subtraction, and then a complex linear combination solves the already excluded forcing \(f\). For two operators, at most two of the three candidates can be solvable for at least one of them. At least one candidate therefore fails for both. If real-valued solutions are desired, real parts of solutions of a real forcing give such solutions, so the same conclusion applies. Real or imaginary parts, or their sum, of the respective \(w^\varepsilon\) provide smooth solutions for each candidate. \(\square\)

The operator and its dimension matter. The heat example has two spatial variables and one time variable. It supplies no negative result for a heat operator in only two total real variables. The partial Laplacian acts in two variables on functions of three variables; the parameter is part of the analytic requirement.

**Corollary 6.1.** For either operator, the same failure holds on \(\mathbb R^{3+\ell}\), \(\ell\ge0\), when it acts only in the displayed three variables.

**Proof.** Keep the forcing independent of the additional variables. Restricting any hypothetical analytic solution to the additional variables equal to zero would give a global analytic solution on \(\mathbb R^3\), which has just been excluded. The smooth particular solution extends by independence of those variables. \(\square\)

## References

- Compact Fourier division and multiplicity-sensitive annihilators, comparison with distributional solvability; its Fourier theorem is not a substitute for analytic solvability.
- E. De Giorgi, *Solutions analytiques des équations aux dérivées partielles à coefficients constants*, Séminaire Goulaouic–Schwartz (1971–1972), exposé 29. [Author's seminar](https://www.numdam.org/item/SEDP_1971-1972____A29_0/). Credit for the heat counterexample and its frequency-isolating argument.
- L. C. Piccinini, *Non surjectivity of the two-variable Laplacian as an operator on the space of analytic functions on three-dimensional real space*, Summer College on Global Analysis, Trieste (1972). Credit for the partial-Laplacian counterexample.
- L. C. Piccinini, *Non surjectivity of the Cauchy–Riemann operator on the space of the analytic functions in real space: generalization to parabolic operators*, Bollettino dell'Unione Matematica Italiana (4), 7 (1973). Credit for the global analytic nonsurjectivity phenomenon. The complete arguments required for the two operators treated here are supplied above.
