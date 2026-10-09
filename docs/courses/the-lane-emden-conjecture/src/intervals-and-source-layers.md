# Intervals and source layers

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The estimate (4.1) of [A localized virial identity](a-localized-virial-identity.md) compares the boundary energies \(W_f,W_g\) with the radial pressure \(\int w(x)D(x,y)\,d\pi\). OpenAI's proof [OpenAI-LE, Sections 4 and 5] slices space into lines parallel to a direction \(e\), and splits the sources on each line into the intervals where they exceed a level \(t\) (the *layers*). This lesson prepares the three ingredients: an inequality for the Newton kernel on two parallel lines (Section 1), weights that restrict the direction \(e\) to a small cap around the radial direction (Section 2), and weights on the layer intervals together with an estimate of what they lose (Section 3). The next lesson, [Pressure and the energy bound](pressure-and-the-energy-bound.md), combines them.

We keep the notation of the two previous lessons: a solution with \(n\ge3\), \(A,B>-2\), \(pq>1\); its sources \(f,g\); \(u=K*g\) and \(v=K*f\); the interaction measure \(\pi\); the functions \(d,\eta,w\) and the exponents \(m=n+3\), \(k=n(m+1)\), \(N=k+n+2\); the energies \(E=E_f+E_g\); for close pairs, \(\ell(z)=\delta d(z)^m\). We write \(\mathbb E_e\) and \(\mathbb P_e\) for the average and the probability over \(e\) with respect to the normalized surface measure \(\sigma/|S|\) on the unit sphere \(S\).

## 1. Two parallel lines

Fix a unit vector \(e\) and two points \(z\neq z'\) of the hyperplane \(e^\perp\), and write points of the two lines as \(x=z+se\), \(y=z'+s'e\). Let \(\lambda=|z-z'|>0\) and \(h=s-s'\). The Newton kernel restricted to the two lines and its directional factor are
\[
\mathcal K(s,s')=K(x-y)=c_n\bigl(\lambda^2+h^2\bigr)^{(2-n)/2},\qquad\mathcal D(s,s')=D_e(x,y)=\frac{h^2}{\lambda^2+h^2}.
\]
For a bounded open interval \(I=(s_-,s_+)\) let \(\overline{\mathcal K}_I(s')=\frac12\bigl(\mathcal K(s_-,s')+\mathcal K(s_+,s')\bigr)\), the average of the kernel at the two endpoints, and define \(\overline{\mathcal K}_J(s)\) for a bounded interval \(J\) of the second line in the same way.

**Lemma 1.1** (interval pairs; OpenAI). Let \(I,J\subseteq\mathbb R\) be nonempty open intervals, possibly unbounded, and let \(c_I,c_J\ge0\), with \(I\) bounded if \(c_I>0\) and \(J\) bounded if \(c_J>0\). Then
\[
\int_{I\times J}(c_I+c_J)\,\mathcal K\,ds\,ds'\le\int_{I\times J}\Bigl[c_I\overline{\mathcal K}_I+c_J\overline{\mathcal K}_J+\bigl((n-2)\min(c_I,c_J)\,\mathcal D+|c_I-c_J|\bigr)\mathcal K\Bigr]ds\,ds',\tag{1.1}
\]
where all terms are nonnegative, the integrals may be infinite, and a term with coefficient \(0\) is \(0\).

**Proof.** If at most one coefficient is positive, then \(|c_I-c_J|=c_I+c_J\), and (1.1) holds pointwise. Let both be positive; then \(I\) and \(J\) are bounded and all integrals are finite. Let \(m_I,m_J\) be the midpoints, \(d_0=m_I-m_J\), and \(L=|I|\), \(M=|J|\). Integration by parts in \(s\) gives
\[
\int_I(\mathcal K-\overline{\mathcal K}_I)\,ds=-\int_I(s-m_I)\,\partial_s\mathcal K\,ds,
\]
because \(\int_I(s-m_I)\partial_s\mathcal K\,ds=\frac L2\bigl(\mathcal K(s_+,s')+\mathcal K(s_-,s')\bigr)-\int_I\mathcal K\,ds\). With \(\partial_s\mathcal K=-(n-2)\frac h{\lambda^2+h^2}\mathcal K=-\partial_{s'}\mathcal K\) and the same identity in \(s'\),
\[
\int_{I\times J}\bigl(2\mathcal K-\overline{\mathcal K}_I-\overline{\mathcal K}_J\bigr)=(n-2)\int_{I\times J}\frac{h^2-d_0h}{\lambda^2+h^2}\,\mathcal K .\tag{1.2}
\]
The image of \(ds\,ds'\) on \(I\times J\) under \(h=s-s'\) has density \(\rho(h)=|I\cap(J+h)|\), the overlap of two intervals of lengths \(L,M\) whose midpoints are \(|h-d_0|\) apart; so \(\rho(h)=F(|h-d_0|)\) with \(F\) nonincreasing. If \(d_0\ge0\) and \(h>0\), then \(|h-d_0|\le|h+d_0|\), so \(\rho(h)\ge\rho(-h)\); the reverse holds if \(d_0\le0\). Since \(h\mapsto h\mathcal K/(\lambda^2+h^2)\) is odd, pairing \(h\) with \(-h\) gives \(d_0\int_{I\times J}\frac h{\lambda^2+h^2}\mathcal K\ge0\). Hence the left side of (1.2) is at most \((n-2)\int_{I\times J}\mathcal D\mathcal K\).

Let \(c=\min(c_I,c_J)\) and multiply this bound by \(c\). Since the endpoint averages are nonnegative, \(\int_{I\times J}(\mathcal K-\overline{\mathcal K}_I)\le\int_{I\times J}\mathcal K\), and likewise for \(J\); multiply these by \(c_I-c\) and \(c_J-c\), whose sum is \(|c_I-c_J|\). Adding the three inequalities and moving the finite endpoint terms to the right gives (1.1). \(\square\)

The formulation without subtraction matters for \(n=3\): there, \(\int\mathcal K\) over an unbounded interval of the other line diverges, and Lemma 1.1 never subtracts such an integral.

## 2. Weights on caps of directions

For \(\theta\in S\) and \(r>0\) let \(C_r(\theta)=\{e\in S:|e-\theta|<r\}\). The surface measure is invariant under orthogonal maps (as Lebesgue measure is), so \(\sigma(C_r(\theta))\) does not depend on \(\theta\).

**Lemma 2.1** (caps). There are \(0<c\le C\), depending only on \(n\), with \(c\,r^{n-1}\le\sigma(C_r(\theta))\le C\,r^{n-1}\) for \(0<r\le1\).

**Proof.** By polar coordinates, the truncated cone \(T_r=\{x:0<|x|<1,\ x/|x|\in C_r(\theta)\}\) has volume \(\sigma(C_r(\theta))/n\). If \(x\in T_r\), the distance from \(x\) to the line \(\mathbb R\theta\) is at most \(|x|\,|x/|x|-\theta|<r\), so \(T_r\) lies in a cylinder of radius \(r\) and length \(2\) around that line, of volume \(Cr^{n-1}\). Conversely, every \(x=s\theta+y\) with \(\frac12\le s\le\frac34\), \(y\perp\theta\) and \(|y|\le r/4\) has \(|x|<1\) and \(|x/|x|-\theta|^2=2-2s/\sqrt{s^2+|y|^2}\le|y|^2/s^2\le r^2/4\); these points form a set of volume \(cr^{n-1}\) inside \(T_r\). \(\square\)

Fix a smooth \(\psi\colon[0,\infty)\to[0,1]\), equal to \(1\) on \([0,\frac12]\) and to \(0\) on \([1,\infty)\), and for \(0<l\le1\) let
\[
Z(l)=\mathbb E_e\,\psi\bigl(|e-\theta|/l\bigr),
\]
which does not depend on \(\theta\). By Lemma 2.1, \(cl^{n-1}\le Z(l)\le Cl^{n-1}\); differentiating under the integral sign, \(|Z'(l)|\le\sup|\psi'|\,l^{-1}\,\mathbb P_e\bigl(C_l(\theta)\bigr)\le Cl^{n-2}\). Fix \(0<\kappa<1\) and define the *cap weights*
\[
h_e(x)=w(x)\,\frac{\psi\bigl(|e-\omega_x|/(\kappa d(x))\bigr)}{Z(\kappa d(x))}\qquad(1<|x|<2),\qquad h_e(x)=0\quad\text{otherwise}.
\]

**Lemma 2.2** (cap weights). For every unit vector \(e\):

1. \(\mathbb E_eh_e(x)=w(x)\) for every \(x\);
2. \(0\le h_e(x)\le C_\kappa d(x)^{N-n}\), and \(h_e(x)>0\) only if \(1<|x|<2\) and \(|e-\omega_x|<\kappa d(x)\);
3. \(h_e\) is continuously differentiable on \(\mathbb R^n\), jointly continuous in \((e,x)\), and \(|\nabla h_e(x)|\le C_\kappa d(x)^{N-n-1}\).

**Proof.** 1 follows from the definition of \(Z\). 2: \(w\le Cd^{N-1}\) and \(Z(\kappa d)\ge c\kappa^{n-1}d^{n-1}\). 3: On the annulus, differentiating the profile costs at most \(C_\kappa/d\) on its support, since \(|\nabla\omega_x|\le1\), \(|\nabla d|=1\), \(|e-\omega_x|\le\kappa d\) there, and the profile is constant where \(|e-\omega_x|<\kappa d/2\); differentiating \(1/Z(\kappa d)\) costs the factor \(\kappa|Z'(\kappa d)|/Z(\kappa d)\le C/d\); and \(|\nabla w|\le Cd^{N-2}\). This gives the bound. Near \(|x|=1\), \(d\) is smooth and \(w\) vanishes to second order, so \(h_e\) and \(\nabla h_e\) tend to \(0\); near \(|x|=2\), \(d^{N-n}\) and \(d^{N-n-1}\) tend to \(0\). So the extension by \(0\) is continuously differentiable. \(\square\)

**Lemma 2.3** (oscillation of the cap weights). Let \(0<\delta<\frac14\). For a close pair \((x,y)\) with endpoint \(z\) (as in Lemma 3.1 of [A localized virial identity](a-localized-virial-identity.md)),
\[
|h_e(x)-h_e(y)|\le C_\kappa\,\delta\,d(z)^{N+2}\le C_\kappa\,\delta\,d(z)^N,\tag{2.1}
\]
and for every solution
\[
\int|h_e(x)-h_e(y)|\,d\pi(x,y)\le C_\kappa\,\delta\,E+C_{\kappa,\delta}.\tag{2.2}
\]

**Proof.** On the segment from \(x\) to \(y\), \(d\) is comparable to \(d(z)\), so Lemma 2.2(3) gives \(|h_e(x)-h_e(y)|\le C_\kappa d(z)^{N-n-1}\ell(z)=C_\kappa\delta d(z)^{N-n-1+m}\), and \(N-n-1+m=N+2\). Integrating against \(\pi\) and using \(d(z)^N\le\eta(x)+\eta(y)\), the close pairs contribute at most \(C_\kappa\delta E\). For far pairs, \(|h_e(x)-h_e(y)|\le h_e(x)+h_e(y)\); the term \(h_e(x)\) is nonzero only if \(d(x)>0\), when \(|x-y|>\ell(x)\), and the tail estimate (4.2) of [Positive solutions and their potentials](positive-solutions-and-their-potentials.md) bounds its integral by
\[
C_\kappa\int_{B_2}f(x)\,d(x)^{N-n}\,\ell(x)^{2-n}\,dx\le C_\kappa\delta^{2-n}\int_{B_2}f\,d^{\,N-n-m(n-2)}\le C_{\kappa,\delta},
\]
since \(N-n-m(n-2)=3n+8>0\). The term \(h_e(y)\) is treated in the same way with \(g\). \(\square\)

**Lemma 2.4** (cap pressure). For every solution,
\[
\mathbb E_e\int h_e(x)D_e(x,y)\,d\pi(x,y)\le\int w(x)D(x,y)\,d\pi(x,y)+C\kappa E,\tag{2.3}
\]
with \(C\) independent of \(\kappa\).

**Proof.** For a unit vector \(\nu\), \(|(\nu\cdot e)^2-(\nu\cdot\omega_x)^2|\le2|e-\omega_x|\), so \(|D_e-D|\le2\kappa d(x)\) where \(h_e(x)>0\). Averaging over \(e\) with Tonelli's theorem and Lemma 2.2(1), the left side of (2.3) is at most \(\int w(x)\bigl(D+2\kappa d(x)\bigr)\,d\pi\), and \(dw\le C\eta\) gives \(2\kappa\int w(x)d(x)\,d\pi\le C\kappa E_f\). \(\square\)

## 3. Layer components and their weights

Fix a unit vector \(e\). With \(f(0)=0\) and \(f\) continuous on \(\mathbb R^n\setminus\{0\}\), the set \(\{f>t\}\) is open for every \(t>0\) and does not contain \(0\). For \(x\neq0\) and \(0<t<f(x)\), let \(I=I_f(e,x,t)\) be the connected component containing \(x\) of the intersection of \(\{f>t\}\) with the line \(x+\mathbb Re\); it is an open interval of that line. Give it the weight
\[
\chi_I=\begin{cases}\inf_Ih_e,&\text{if }I\text{ is bounded and }|I|\le2\delta\inf_Id,\\0,&\text{otherwise},\end{cases}
\]
and write \(\chi_f(e,x,t)=\chi_I\). Define \(J=I_g(e,y,t')\) and \(\chi_g(e,y,t')=\chi_J\) in the same way from \(\{g>t'\}\). Since \(x\in I\), we have \(0\le\chi_f(e,x,t)\le h_e(x)\), and likewise \(0\le\chi_g(e,y,t')\le h_e(y)\).

**Lemma 3.1** (measurability). On \(\{(e,x,t):x\neq0,\ 0<t<f(x)\}\), the two distances from \(x\) to the ends of \(I_f(e,x,t)\) (possibly infinite), the ends themselves when finite, and \(\chi_f\) are Borel functions of \((e,x,t)\). The same holds for \(g\).

**Proof.** The set \(\mathcal L=\{(x,t):x\neq0,\ 0<t<f(x)\}\) is open. The forward distance \(\tau_+(e,x,t)=\sup\{r\ge0:x+se\in\{f>t\}\text{ for }0\le s\le r\}\) exceeds \(r\) exactly when, for some rational \(r'>r\), the compact segment from \(x\) to \(x+r'e\) lies in the open layer; that is an open condition in \((e,x,t)\). So \(\tau_+\) is lower semicontinuous, hence Borel, and so is the backward distance \(\tau_-\). The infima of the continuous functions \(h_e\) and \(d\) over the open interval \(I\) equal their infima over the points \(x+se\) with rational \(s\in(-\tau_-,\tau_+)\), which are countable infima of Borel functions. \(\square\)

For each direction define the *losses*
\[
L_f(e)=\int u(x)\int_0^{f(x)}\bigl(h_e(x)-\chi_f(e,x,t)\bigr)\,dt\,dx,\qquad L_g(e)=\int v(y)\int_0^{g(y)}\bigl(h_e(y)-\chi_g(e,y,t')\bigr)\,dt'\,dy .
\]
They are nonnegative, and finite because \(h_e\) is bounded and vanishes outside the annulus \(1\le|x|\le2\).

**Lemma 3.2** (averaged loss; OpenAI). For every \(P\ge1\) and every solution,
\[
\mathbb E_e\bigl(L_f(e)+L_g(e)\bigr)\le\bigl(C_\kappa\delta+C_{\kappa,\delta}P^{-1}\bigr)E+CP,\tag{3.1}
\]
where \(C_\kappa\) does not depend on \(\delta\) or \(P\), \(C_{\kappa,\delta}\) does not depend on \(P\), and \(C\) does not depend on \(\kappa,\delta,P\).

**Proof.** We treat \(f\); the proof for \(g\) is the same. Only \(1<|x|<2\) contributes. Fix such an \(x\), and let \(d=d(x)\) and \(\ell=\delta d^m\).

*Short components.* If \(|I|\le\ell\), every point of \(I\) is within \(\ell\le\delta d\) of \(x\), so \(\inf_Id\ge(1-\delta)d\) and \(|I|\le\delta d\le2\delta\inf_Id\); thus \(\chi_I=\inf_Ih_e\), and by (2.1) the loss \(h_e(x)-\chi_I\) is at most \(C_\kappa\delta d^N\).

*Long components.* If \(|I|>\ell\), then one of the two parts of \(I\) on either side of \(x\) contains a segment of length \(\ell/2\) starting at \(x\). Let \(F\) be the set of \(\theta\in S\) for which the segment from \(x\) to \(x+(\ell/2)\theta\) lies in \(\{f>t\}\). By polar coordinates about \(x\),
\[
\int_{B_{\ell/2}(x)}f\ge\int_0^{\ell/2}r^{n-1}\int_Ft\,d\sigma\,dr=\frac{|S|}n\,t\Bigl(\frac\ell2\Bigr)^n\,\mathbb P_e(F).
\]
The event \(|I|>\ell\) is contained in \(\{e\in F\}\cup\{-e\in F\}\), and \(B_{\ell/2}(x)\subseteq B_4\), so by (4.2) of [Positive solutions and their potentials](positive-solutions-and-their-potentials.md)
\[
\mathbb P_e\bigl(|I|>\ell\bigr)\le2\,\mathbb P_e(F)\le\frac C{t\,\ell^n}\int_{B_4}f\le\frac C{t\,\ell^n}.\tag{3.2}
\]

*High levels.* Let \(t\ge Pd^{-k}\). On long components the loss is at most \(h_e(x)\le C_\kappa d^{N-n}\), so by (3.2) its average over \(e\) is at most \(C_\kappa d^{N-n}\cdot C\delta^{-n}d^{-mn}P^{-1}d^k=C_{\kappa,\delta}P^{-1}d^N\), because \(k=mn+n\). Adding the short components, the average loss at level \(t\) is at most \((C_\kappa\delta+C_{\kappa,\delta}P^{-1})d^N\). Integrating over these levels, then against \(u(x)\,dx\), and using \(d^N\le\eta\), gives at most \((C_\kappa\delta+C_{\kappa,\delta}P^{-1})E_f\).

*Low levels.* Since \(\mathbb E_eh_e(x)=w(x)\le Cd^{N-1}\),
\[
\int_0^{\min\{f(x),Pd^{-k}\}}\mathbb E_e\bigl(h_e(x)-\chi_f(e,x,t)\bigr)\,dt\le Pd^{-k}w(x)\le CPd^{N-1-k}=CPd^{n+1}\le CP,
\]
and integrating against \(u\) over \(B_2\) gives at most \(CP\) by (4.2) of [Positive solutions and their potentials](positive-solutions-and-their-potentials.md). Averages over \(e\) and integrals over \((x,t)\) were exchanged by Tonelli's theorem, which applies by Lemma 3.1. \(\square\)

## 4. Exercises

**Exercise 4.1** (easy). Check the identity \(\int_I(s-m_I)\,\partial_s\mathcal K\,ds=L\,\overline{\mathcal K}_I-\int_I\mathcal K\,ds\) used in the proof of Lemma 1.1.

**Exercise 4.2** (easy). Show that \(|I\cap(J+h)|=\max\{0,\min\{L,M,\frac{L+M}2-|h-d_0|\}\}\) for intervals of lengths \(L,M\) with midpoint difference \(d_0\).

**Exercise 4.3** (medium). In Lemma 1.1 take \(n=3\), \(c_I=c_J=1\) and \(I=J=(0,1)\). Show that the left side of (1.2) is at most \((n-2)\int\mathcal D\mathcal K\) by computing \(d_0\).

**Exercise 4.4** (medium). Show that \(|(\nu\cdot e)^2-(\nu\cdot\omega)^2|\le2|e-\omega|\) for unit vectors \(\nu,e,\omega\).

## 5. Solutions

**4.1.** Integrate by parts: \(\int_{s_-}^{s_+}(s-m_I)\partial_s\mathcal K\,ds=\bigl[(s-m_I)\mathcal K\bigr]_{s_-}^{s_+}-\int_I\mathcal K\,ds\), and \(s_\pm-m_I=\pm L/2\), so the bracket is \(\frac L2\bigl(\mathcal K(s_+,s')+\mathcal K(s_-,s')\bigr)=L\,\overline{\mathcal K}_I\).

**4.2.** \(I\cap(J+h)\) is the intersection of two intervals of lengths \(L\) and \(M\) whose midpoints are \(m_I\) and \(m_J+h\), at distance \(|d_0-h|\). The intersection is empty when the distance is at least \(\frac{L+M}2\), and otherwise has length \(\frac{L+M}2-|d_0-h|\), capped by the length of the shorter interval.

**4.3.** Here \(d_0=0\), so the term \(d_0h\) in (1.2) vanishes and (1.2) is the claimed bound with equality.

**4.4.** \((\nu\cdot e)^2-(\nu\cdot\omega)^2=\bigl(\nu\cdot(e-\omega)\bigr)\bigl(\nu\cdot(e+\omega)\bigr)\), and \(|\nu\cdot(e-\omega)|\le|e-\omega|\), \(|\nu\cdot(e+\omega)|\le2\).

## References

- [OpenAI-LE] OpenAI, *The subcritical Hénon–Lane–Emden conjecture*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/The-Subcritical-Henon-Lane-Emden-Conjecture-September-24-2026
