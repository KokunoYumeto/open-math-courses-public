# A localized virial identity

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Pohozaev and Rellich identities, obtained by testing an equation against \(x\cdot\nabla u\), have long been the main tool for Liouville theorems of Lane–Emden type; Mitidieri found a version for systems and Phan a weighted one [Phan]. This lesson proves a localized form written in terms of the Newton potentials, which keeps the weights exactly [OpenAI-LE, Section 3]. It expresses the localized energy through a *pressure* term (Lemma 2.1), and shows that, up to errors that are small compared with the energy, the pressure is carried by pairs of nearby points and depends on directions only through the radial direction (Lemma 3.1).

We keep the notation of [Positive solutions and their potentials](positive-solutions-and-their-potentials.md): a solution \((u,v)\) with \(n\ge3\), \(A,B>-2\), \(pq>1\), its sources \(f=|x|^Bu^q\) and \(g=|x|^Av^p\), the identities \(u=K*g\) and \(v=K*f\) off the origin, the exponents \(a=\frac1{q+1}\), \(b=\frac1{p+1}\), and the universal estimates (4.1) and (4.2) of Proposition 4.1 there. Constants \(C\) are universal unless they carry a subscript naming further parameters.

## 1. The interaction measure and the cutoffs

The *interaction measure* is the measure on \(\mathbb R^n\times\mathbb R^n\) given by
\[
d\pi(x,y)=f(x)\,g(y)\,K(x-y)\,dx\,dy .
\]
By Tonelli's theorem and \(u=K*g\), \(v=K*f\), its marginals are
\[
\pi(dx\times\mathbb R^n)=f(x)u(x)\,dx,\qquad\pi(\mathbb R^n\times dy)=g(y)v(y)\,dy .\tag{1.1}
\]
So \(\pi\) is finite on bounded sets, but its total mass need not be finite. For a unit vector \(e\) and \(x\neq y\) let
\[
D_e(x,y)=\frac{\bigl((x-y)\cdot e\bigr)^2}{|x-y|^2}\in[0,1],\qquad\omega_x=\frac x{|x|},\qquad D(x,y)=D_{\omega_x}(x,y),
\]
with any fixed unit vector as \(\omega_0\) (a null set). Values on the diagonal \(x=y\) play no role.

Fix
\[
d(x)=\min\{1,(2-|x|)_+\},\qquad m=n+3,\qquad k=n(m+1),\qquad N=k+n+2=n^2+5n+2,
\]
\[
\eta(x)=\Bigl[\bigl(1-(|x|-1)_+^3\bigr)_+\Bigr]^N,\qquad w(x)=-x\cdot\nabla\eta(x),\qquad X(x)=x\,\eta(x),
\]
where \(t_+=\max\{t,0\}\). Thus \(\eta=1\) on \(B_1\), \(\eta=0\) outside \(B_2\), and \(w\ge0\) vanishes unless \(1<|x|<2\).

**Lemma 1.1** (the cutoffs). The function \(\eta\) is twice continuously differentiable with compact support, \(\nabla X=\eta\,I-w\,\omega_x\otimes\omega_x\), and for a universal \(C\),
\[
d^N\le\eta\le Cd^N,\qquad|\nabla\eta|+w\le Cd^{N-1},\qquad|\nabla^2\eta|+|\nabla w|+|\nabla^2X|\le Cd^{N-2},\qquad d\,w\le C\eta .\tag{1.2}
\]

**Proof.** With \(s=|x|-1\), on the annulus \(1<|x|<2\) we have \(d=1-s\) and \(1-s^3=d\,(1+s+s^2)\), so \(\eta=d^N(1+s+s^2)^N\) lies between \(d^N\) and \(3^Nd^N\); inside \(B_1\) both are \(1\), and outside \(B_2\) both are \(0\). The function \(s\mapsto(1-s_+^3)^N\) is twice continuously differentiable at \(s=0\), because \(s_+^3\) and its first two derivatives vanish there, and it vanishes to order \(N\) at \(s=1\); so \(\eta\) is twice continuously differentiable. On the annulus, \(\nabla\eta=-3Ns^2(1-s^3)^{N-1}\omega_x\), so \(|\nabla\eta|\le Cd^{N-1}\) and \(w=|x|\,|\nabla\eta|\le Cd^{N-1}\); each further derivative lowers the power of \(1-s^3\) by at most one, which gives the second-order bounds. Finally \(dw\le Cd^N\le C\eta\), and \(\nabla X=\eta I+x\otimes\nabla\eta=\eta I-w\,\omega_x\otimes\omega_x\). \(\square\)

Define the *localized energies*
\[
E_f=\int\eta fu\,dx,\qquad E_g=\int\eta gv\,dx,\qquad E=E_f+E_g,\qquad W_f=\int wfu\,dx,\qquad W_g=\int wgv\,dx .
\]
They are finite for each solution, since \(u,v\) are bounded on \(\overline B_2\) and \(|x|^A,|x|^B\) are integrable there; the task is a bound on \(E\) that does not depend on the solution. By (1.1), \(E_f=\int\eta(x)\,d\pi\) and \(E_g=\int\eta(y)\,d\pi\).

## 2. The virial identity

**Lemma 2.1** (localized virial identity; OpenAI). The functions \(fX\cdot\nabla u\) and \(gX\cdot\nabla v\) are integrable, the function
\[
\Phi(x,y)=\frac{\bigl(X(x)-X(y)\bigr)\cdot(x-y)}{|x-y|^2}
\]
is \(\pi\)-integrable, and
\[
a(n+B)E_f+b(n+A)E_g-aW_f-bW_g=(n-2)\int\Phi\,d\pi .\tag{2.1}
\]

**Proof.** *Integrability.* Recall \(|\nabla K(z)|=(n-2)K(z)/|z|\). We show that \(Q(x)=|X(x)|\int|\nabla K(x-y)|g(y)\,dy\) is bounded on \(B_2\); since \(X\) vanishes outside \(B_2\) and \(f\) is integrable on \(B_2\), this gives \(\int f(x)|X(x)|\int|\nabla K(x-y)|g(y)\,dy\,dx<\infty\). Let \(0<r=|x|\) be small. If \(|x-y|\le r/2\), then \(|y|\) lies between \(r/2\) and \(3r/2\), so \(g(y)\le C_{u,v}r^A\) with a constant depending on the solution, and this part of \(Q(x)\) is at most \(r\cdot C_{u,v}r^A\cdot C\int_{B_{r/2}}|z|^{1-n}\,dz\le C_{u,v}r^{2+A}\), which is bounded because \(A>-2\). If \(|x-y|>r/2\), then \(|X(x)|\le r<2|x-y|\), so this part is at most \(2(n-2)K*g(x)=2(n-2)u(x)\). On compact subsets of \(\overline B_2\setminus\{0\}\) the same splitting at a fixed radius bounds \(Q\), since \(g\) is bounded near such a set. Exchanging the roles of \((f,u,B)\) and \((g,v,A)\) gives the other estimate. By Proposition 2.1 of [Positive solutions and their potentials](positive-solutions-and-their-potentials.md), \(|X\cdot\nabla u|\le Q\), so \(fX\cdot\nabla u\) is integrable; and \(\Phi\) is \(\pi\)-integrable because \(|\Phi|\,K(x-y)\le\bigl(|X(x)|+|X(y)|\bigr)|\nabla K(x-y)|/(n-2)\).

*Integration by parts.* The field \(V=|x|^Bu^{q+1}X\) is continuously differentiable off the origin and vanishes outside \(B_2\). Since \(\operatorname{div}(|x|^BX)=|x|^B\bigl((n+B)\eta-w\bigr)\),
\[
\operatorname{div}V=|x|^Bu^{q+1}\bigl((n+B)\eta-w\bigr)+(q+1)\,fX\cdot\nabla u .
\]
For \(0<\rho<1\), Lemma 1.2 of [Spherical means and Newton potentials](spherical-means-and-newton-potentials.md) gives \(\int_{|x|>\rho}\operatorname{div}V=-\rho^{n+B}\int_Su(\rho\theta)^{q+1}\,d\sigma\), because \(\eta=1\) and \(X\cdot\theta=\rho\) on the sphere of radius \(\rho\). Dividing by \(q+1\),
\[
-\int_{|x|>\rho}fX\cdot\nabla u\,dx=a\int_{|x|>\rho}fu\bigl((n+B)\eta-w\bigr)\,dx+a\rho^{n+B}\int_Su(\rho\theta)^{q+1}\,d\sigma .
\]
As \(\rho\to0\), the boundary term is \(O(\rho^{n+B})\to0\), and the integrals converge by integrability. With the same computation for \(v\),
\[
-\int fX\cdot\nabla u\,dx-\int gX\cdot\nabla v\,dx=a(n+B)E_f+b(n+A)E_g-aW_f-bW_g .
\]

*The potentials.* Insert \(\nabla u(x)=\int\nabla K(x-y)g(y)\,dy\) and \(\nabla K(z)=-(n-2)zK(z)/|z|^2\): by the absolute convergence just shown,
\[
-\int fX\cdot\nabla u\,dx=(n-2)\int\frac{X(x)\cdot(x-y)}{|x-y|^2}\,d\pi(x,y),\qquad-\int gX\cdot\nabla v\,dy=(n-2)\int\frac{X(y)\cdot(y-x)}{|x-y|^2}\,d\pi(x,y),
\]
and the sum of the right sides is \((n-2)\int\Phi\,d\pi\). \(\square\)

For \(x\) and \(y\) close together, \(\Phi(x,y)\approx\nabla X(x)\frac{x-y}{|x-y|}\cdot\frac{x-y}{|x-y|}=\eta(x)-w(x)D(x,y)\). The next lemma makes this precise in the sense of the energy.

## 3. Localization

**Lemma 3.1** (localization; OpenAI). For every \(\epsilon>0\) there is a universal \(C_\epsilon\) such that every solution satisfies
\[
|E_f-E_g|+\int\bigl|\Phi(x,y)-\eta(x)+w(x)D(x,y)\bigr|\,d\pi(x,y)\le\epsilon E+C_\epsilon .\tag{3.1}
\]

**Proof.** Fix \(0<\delta<\frac14\) and let \(\ell(z)=\delta d(z)^m\) when \(d(z)>0\). Call a pair \((x,y)\) *close* if \(|x-y|\le\ell(z)\) for some endpoint \(z\in\{x,y\}\) with \(d(z)>0\), and *far* otherwise. Since \(d\) is \(1\)-Lipschitz and \(\ell(z)\le\delta d(z)\), every point \(\xi\) of the segment from \(x\) to \(y\) of a close pair has \((1-\delta)d(z)\le d(\xi)\le(1+\delta)d(z)\); in particular the segment lies in \(B_2\).

*Close pairs.* By Taylor's formula along the segment and Lemma 1.1, \(X(x)-X(y)=\nabla X(x)(x-y)+O\bigl(d(z)^{N-2}|x-y|^2\bigr)\), so
\[
\bigl|\Phi-\eta(x)+w(x)D\bigr|\le C\,d(z)^{N-2}\,\ell(z)=C\delta\,d(z)^{N+n+1},\qquad|\eta(x)-\eta(y)|\le Cd(z)^{N-1}\ell(z)=C\delta\,d(z)^{N+n+2}.
\]
Both are at most \(C\delta\,d(z)^N\le C\delta\bigl(\eta(x)+\eta(y)\bigr)\), and by (1.1) the integral of \(\eta(x)+\eta(y)\) against \(\pi\) is \(E\). So close pairs contribute at most \(C\delta E\) to the left side of (3.1), counting the term \(|E_f-E_g|\) through \(|\eta(x)-\eta(y)|\) as below.

*Far pairs.* For a far pair, \(|x-y|>\ell(z)\) for each endpoint \(z\) with \(d(z)>0\), and endpoints with \(d(z)=0\) have \(X(z)=0\) and \(\eta(z)=0\). Using \(|\Phi|\le(|X(x)|+|X(y)|)/|x-y|\), \(|X(z)|\le2\eta(z)\le Cd(z)^N\), \(0\le D\le1\) and (1.2),
\[
\bigl|\Phi-\eta(x)+w(x)D\bigr|+|\eta(x)-\eta(y)|\le C\sum_{z\in\{x,y\},\,d(z)>0}\Bigl(d(z)^{N-1}+\frac{d(z)^N}{\ell(z)}\Bigr).
\]
The terms with \(z=x\) are integrated against \(f(x)\int_{|x-y|>\ell(x)}K(x-y)g(y)\,dy\,dx\), which by the tail estimate (4.2) of Proposition 4.1 in [Positive solutions and their potentials](positive-solutions-and-their-potentials.md) is at most \(C\ell(x)^{2-n}f(x)\,dx\) on \(B_2\). Their total is therefore at most
\[
C\int_{B_2}f(x)\Bigl(\delta^{2-n}d(x)^{N-1-m(n-2)}+\delta^{1-n}d(x)^{N-m(n-1)}\Bigr)dx\le C_\delta,
\]
because \(N-1-m(n-2)=4n+7\) and \(N-m(n-1)=3n+5\) are positive and \(\int_{B_2}f\le C\). The terms with \(z=y\) are bounded in the same way with \(g\) in place of \(f\).

*Conclusion.* Since \(E_f\) and \(E_g\) are finite, \(|E_f-E_g|=\bigl|\int(\eta(x)-\eta(y))\,d\pi\bigr|\le\int|\eta(x)-\eta(y)|\,d\pi\). Altogether the left side of (3.1) is at most \(C\delta E+C_\delta\), and it remains to choose \(\delta\le\epsilon/C\). \(\square\)

## 4. What remains

By Lemmas 2.1 and 3.1, the energy is controlled once the weighted boundary energies \(W_f,W_g\) are compared with the radial pressure \(\int w(x)D(x,y)\,d\pi\). The required estimate,
\[
aW_f+bW_g\le(n-2)\int w(x)D(x,y)\,d\pi(x,y)+\epsilon E+C_\epsilon\qquad(\epsilon>0),\tag{4.1}
\]
is Proposition 4.1 of [Pressure and the energy bound](pressure-and-the-energy-bound.md). Its proof works along lines in many directions and uses the inequality for pairs of intervals of [Intervals and source layers](intervals-and-source-layers.md).

## 5. Exercises

**Exercise 5.1** (easy). Show that \(\operatorname{div}(|x|^BX)=|x|^B\bigl((n+B)\eta-w\bigr)\).

**Exercise 5.2** (easy). Verify that \(N=n^2+5n+2\), \(N-1-m(n-2)=4n+7\), \(N-m(n-1)=3n+5\), and \(N-1-k=n+1\).

**Exercise 5.3** (medium). Show that \(\nabla X(x)\frac{x-y}{|x-y|}\cdot\frac{x-y}{|x-y|}=\eta(x)-w(x)D(x,y)\).

**Exercise 5.4** (medium). Suppose, formally, that (2.1) held with \(\eta\equiv1\), \(w\equiv0\) and \(A=B=0\). Show that it would read \(\bigl(an+bn-(n-2)\bigr)\int fu=0\), and that the subcritical condition would then contradict positivity. What goes wrong without the cutoff?

## 6. Solutions

**5.1.** \(\operatorname{div}(|x|^Bx)=n|x|^B+x\cdot\nabla|x|^B=(n+B)|x|^B\), so \(\operatorname{div}(|x|^Bx\eta)=(n+B)|x|^B\eta+|x|^Bx\cdot\nabla\eta=|x|^B\bigl((n+B)\eta-w\bigr)\).

**5.2.** \(N=n(n+4)+n+2=n^2+5n+2\); \(N-1-(n+3)(n-2)=n^2+5n+1-(n^2+n-6)=4n+7\); \(N-(n+3)(n-1)=n^2+5n+2-(n^2+2n-3)=3n+5\); \(N-1-k=n+1\).

**5.3.** With \(\nabla X=\eta I-w\,\omega_x\otimes\omega_x\) and a unit vector \(\nu\), \(\nabla X(x)\nu\cdot\nu=\eta(x)-w(x)(\omega_x\cdot\nu)^2\), and \((\omega_x\cdot\nu)^2=D(x,y)\) for \(\nu=(x-y)/|x-y|\).

**5.4.** With \(\eta\equiv1\), \(w\equiv0\) and \(X(x)=x\), \(\Phi\equiv1\), so (2.1) reads \(an\int fu+bn\int gv=(n-2)\pi(\mathbb R^n\times\mathbb R^n)\), and by (1.1) both \(\int fu\) and \(\int gv\) equal the total mass of \(\pi\). So \((an+bn-(n-2))\int fu=0\), and \(an+bn>n-2\) forces \(\int fu=0\), impossible for a positive solution. The difficulty is that \(\int fu\) may be infinite; the cutoff \(\eta\) removes that problem at the cost of the terms \(W_f,W_g\) and the pressure.

## References

- [OpenAI-LE] OpenAI, *The subcritical Hénon–Lane–Emden conjecture*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/The-Subcritical-Henon-Lane-Emden-Conjecture-September-24-2026
- [Phan] Q. H. Phan, *Liouville-type theorems and bounds of solutions for Hardy–Hénon elliptic systems*, Advances in Differential Equations 17 (2012), 605–634. https://arxiv.org/abs/1108.1312
