# Pressure and the energy bound

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson contains the last steps of OpenAI's proof [OpenAI-LE, Sections 5 and 6]. It proves the pressure estimate (4.1) of [A localized virial identity](a-localized-virial-identity.md) (Proposition 4.1 below), deduces the uniform energy bound, Proposition 5.1 of [Positive solutions and their potentials](positive-solutions-and-their-potentials.md), and with it the nonexistence theorem and the Lane–Emden conjecture.

The idea is to apply the inequality for pairs of intervals, Lemma 1.1 of [Intervals and source layers](intervals-and-source-layers.md), to the layer components of the two sources on every pair of parallel lines, and to integrate over all lines and levels. The left side of that inequality then becomes the energy with weights, the endpoint terms become the values of the potentials at the ends of the layers, which are known exactly because the layers are level sets, and the remaining terms are the pressure and errors. A one-variable identity (3.1) turns the difference into the boundary energies \(aW_f+bW_g\).

We keep the notation of the previous lessons; in particular \(0<\kappa<1\), \(0<\delta<\frac14\), the cap weights \(h_e\), the component weights \(\chi_f,\chi_g\), and the losses \(L_f,L_g\) of [Intervals and source layers](intervals-and-source-layers.md). Let
\[
\begin{gathered}
H_f(e)=\int h_e\,fu\,dx,\\
H_g(e)=\int h_e\,gv\,dy,
\end{gathered}
\]
which are finite since \(h_e\) is bounded and vanishes outside the annulus \(1\le|x|\le2\), and \(\mathbb E_eH_f(e)=W_f\), \(\mathbb E_eH_g(e)=W_g\) by Lemma 2.2 there.

## 1. Values at the ends of the layers

**Lemma 1.1** (OpenAI). Let \(x\neq0\), \(0<t<f(x)\), and suppose \(\chi_I>0\) for the component \(I=I_f(e,x,t)\). Then \(I\) is bounded, its ends \(x_\pm\) lie in the annulus \(1<|x|<2\), \(f(x_\pm)=t\), so that \(u(x_\pm)=(t/|x_\pm|^B)^{1/q}\), and the average \(\overline u_I=\frac12\bigl(u(x_-)+u(x_+)\bigr)\) satisfies
\[
\begin{aligned}
&\bigl|\overline u_I-(t/|x|^B)^{1/q}\bigr|\\
&\quad \le C\delta\,d(x)\,(t/|x|^B)^{1/q}\\
&\quad \le C\delta\,d(x)\,u(x).
\end{aligned}\tag{1.1}
\]
The same holds for a component \(J=I_g(e,y,t')\) with \(\chi_J>0\), its average \(\overline v_J\), and \((t'/|y|^A)^{1/p}\).

**Proof.** By definition of \(\chi_I\), \(I\) is bounded and \(h_e\ge\chi_I>0\) on \(I\), hence at its ends by continuity, so the ends lie in the open annulus, where \(f\) is continuous. As limits of points of \(I\), the ends have \(f(x_\pm)\ge t\); if \(f(x_+)>t\), a neighbourhood of \(x_+\) on the line would lie in \(\{f>t\}\), and \(I\) would not end at \(x_+\). So \(f(x_\pm)=t\), and \(u(x_\pm)^q=t/|x_\pm|^B\). Every \(x\in I\) lies in the annulus, and \(|x_\pm-x|\le|I|\le2\delta\inf_Id\le2\delta d(x)\). The function \(r\mapsto r^{-B/q}\) on \([1,2]\) satisfies \(|r^{-B/q}-r'^{-B/q}|\le C|r-r'|\,r^{-B/q}\), which gives the first inequality of (1.1); the second holds because \(t<f(x)\) means \((t/|x|^B)^{1/q}<u(x)\). \(\square\)

When \(\chi_I=0\), any product of \(\chi_I\) with an end value is set to \(0\) without choosing ends.

## 2. Integration over lines and levels

Fix a unit vector \(e\) and write \(x=z+se\) with \(z\in e^\perp\) and \(s\in\mathbb R\), in an orthonormal frame of \(e^\perp\). For levels \(t,t'>0\) and two different lines \(z\neq z'\), apply Lemma 1.1 of [Intervals and source layers](intervals-and-source-layers.md) to every component \(I\) of \(\{f>t\}\) on the first line and every component \(J\) of \(\{g>t'\}\) on the second, with \(c_I=\chi_I\) and \(c_J=\chi_J\). Since \(\min(\chi_I,\chi_J)\le\chi_I\le h_e(x)\) for \(x\in I\), and \(\mathcal K=K(x-y)\), \(\mathcal D=D_e(x,y)\), the inequality (2.1) holds:
\[
\begin{aligned}
&\int_{I\times J}(\chi_I+\chi_J)\mathcal K\\
&\quad\le\int_{I\times J}\Bigl[\chi_I\overline{\mathcal K}_I+\chi_J\overline{\mathcal K}_J\\
&\qquad+\bigl((n-2)h_e(x)D_e(x,y)\\
&\qquad\quad+|\chi_I-\chi_J|\bigr)\mathcal K\Bigr].
\end{aligned}
\]
An open subset of a line has countably many components, and each point \(x\) of the line with \(f(x)>t\) lies in exactly one of them. So summing (2.1) over all components and integrating over \(z,z'\in e^\perp\) and \(t,t'>0\) amounts to integrating over \((x,t)\) with \(0<t<f(x)\) and \((y,t')\) with \(0<t'<g(y)\), the weights being \(\chi_f(e,x,t)\) and \(\chi_g(e,y,t')\); Tonelli's theorem applies by the measurability lemma there, and the pairs on a common line form a null set. Using \(\int_0^{g(y)}dt'=g(y)\), \(\int K(x-y)g(y)\,dy=u(x)\), and the corresponding facts for \(f\) and \(v\), the four groups of terms become:

- the left side: \(U_f(e)+U_g(e)\), where \(U_f(e)\) equals \(\int\int_0^{f(x)}\chi_f(e,x,t)\,u(x)\,dt\,dx\) and \(U_g(e)\) equals \(\int\int_0^{g(y)}\chi_g(e,y,t')\,v(y)\,dt'\,dy\);
- the end terms: \(V_f(e)+V_g(e)\), where \(V_f(e)=\int\int_0^{f(x)}\chi_f(e,x,t)\,\overline u_I\,dt\,dx\) and \(V_g\) is analogous; indeed, for one component \(I\), integrating \(\overline{\mathcal K}_I\) against all layers of \(g\) gives the average of \(K*g\) at the two ends of \(I\), that is \(\overline u_I\), the omitted points on the line of \(I\) forming a null set;
- the pressure: \((n-2)\int h_e(x)D_e(x,y)\,d\pi(x,y)\);
- the mismatch: \(\mathcal M_e\), the integral of \(|\chi_f(e,x,t)-\chi_g(e,y,t')|\,K(x-y)\) over \(0<t<f(x)\), \(0<t'<g(y)\) and \(x,y\).

All of them are finite: \(U_f\le H_f\); \(V_f\le CH_f\) by (1.1); the pressure is at most \((n-2)H_f\); and \(\mathcal M_e\le H_f+H_g\) because \(|\chi_f-\chi_g|\le h_e(x)+h_e(y)\). So no infinite quantity is subtracted below, even when \(n=3\). Subtracting the end terms,
\[
\begin{aligned}
&S_e:=\bigl(U_f-V_f\bigr)+\bigl(U_g-V_g\bigr)\\
&\quad \le(n-2)\int h_eD_e\,d\pi+\mathcal M_e .
\end{aligned}
\]
Finally,
\[
\begin{aligned}
&|\chi_f(e,x,t)-\chi_g(e,y,t')|\\
&\quad\le|h_e(x)-h_e(y)|\\
&\qquad+\bigl(h_e(x)-\chi_f(e,x,t)\bigr)\\
&\qquad+\bigl(h_e(y)-\chi_g(e,y,t')\bigr),
\end{aligned}
\]
and integrating the second term over \((y,t')\) gives \(L_f(e)\), the third gives \(L_g(e)\). Hence the bound (2.2) holds:
\[
\begin{aligned}
&S_e\le(n-2)\int h_e(x)D_e(x,y)\,d\pi\\
&\quad+\int|h_e(x)-h_e(y)|\,d\pi\\
&\quad+L_f(e)+L_g(e).
\end{aligned}
\]
The quantity \(S_e\) need not be nonnegative.

## 3. Recovery of the boundary energies

For \(x\neq0\) the identity (3.1) holds:
\[
\begin{aligned}
&\int_0^{f(x)}\Bigl[u(x)-\bigl(t/|x|^B\bigr)^{1/q}\Bigr]dt\\
&\quad=f(x)u(x)-\frac q{q+1}|x|^{-B/q}f(x)^{1+1/q}\\
&\quad=\frac{f(x)u(x)}{q+1}=a\,f(x)u(x),
\end{aligned}
\]
because \(|x|^{-B/q}f(x)^{1/q}=u(x)\); the same holds for \(g\) with \(b=\frac1{p+1}\). For \(0<t<f(x)\) put \(\tau=(t/|x|^B)^{1/q}\in[0,u(x)]\). Then
\[
\begin{aligned}
&h_e(x)\bigl(u(x)-\tau\bigr)-\chi_f\bigl(u(x)-\overline u_I\bigr)\\
&\quad =\bigl(h_e(x)-\chi_f\bigr)\bigl(u(x)-\tau\bigr)\\
&\quad +\chi_f\bigl(\overline u_I-\tau\bigr)\le\bigl(h_e(x)-\chi_f\bigr)u(x)\\
&\quad +C\delta\,d(x)\,h_e(x)\,u(x),
\end{aligned}
\]
by (1.1) and \(\chi_f\le h_e(x)\), with \(\chi_f=\chi_f(e,x,t)\). Integrating over \(0<t<f(x)\) and over \(x\), and using (3.1),
\[
\begin{aligned}
&aH_f(e)\le\bigl(U_f-V_f\bigr)\\
&\quad +L_f(e)+C\delta\int d\,h_e\,fu\,dx .
\end{aligned}
\]
With the same estimate for \(g\), the bound (3.2) follows:
\[
\begin{aligned}
&aH_f(e)+bH_g(e)\le S_e+L_f(e)+L_g(e)\\
&\quad+C\delta\int d(x)h_e(x)\bigl(f(x)u(x)\\
&\qquad+g(x)v(x)\bigr)\,dx .
\end{aligned}
\]

## 4. The pressure estimate

**Proposition 4.1** (localized pressure; OpenAI). For every \(\epsilon>0\) there is a universal \(C_\epsilon\) such that every solution satisfies
\[
\begin{aligned}
&aW_f+bW_g\\
&\quad \le(n-2)\int w(x)D(x,y)\,d\pi(x,y)\\
&\quad +\epsilon E+C_\epsilon .
\end{aligned}
\]

**Proof.** Combine (3.2) and (2.2), and average over \(e\). This produces two copies of \(L_f+L_g\). By Lemma 2.2(1) of [Intervals and source layers](intervals-and-source-layers.md), the left side becomes \(aW_f+bW_g\), and \(\mathbb E_e\int d\,h_e(fu+gv)=\int d\,w\,(fu+gv)\), which is at most \(CE\) because \(dw\le C\eta\). By (2.3), (2.2) and (3.1) there,
\[
\begin{aligned}
&aW_f+bW_g\le(n-2)\int wD\,d\pi\\
&\quad +\bigl(C\kappa+C_\kappa\delta+C_{\kappa,\delta}P^{-1}\bigr)E+C_{\kappa,\delta,P},
\end{aligned}
\]
where \(C\) does not depend on \(\kappa,\delta,P\), the constant \(C_\kappa\) does not depend on \(\delta,P\), and \(C_{\kappa,\delta}\) does not depend on \(P\). Choose \(\kappa\) with \(C\kappa\le\epsilon/3\), then \(\delta\) with \(C_\kappa\delta\le\epsilon/3\), then \(P\) with \(C_{\kappa,\delta}P^{-1}\le\epsilon/3\). \(\square\)

## 5. The energy bound and the theorem

**Proposition 5.1** (uniform local energy bound; OpenAI). Let \(n\ge3\), \(A,B>-2\), \(pq>1\) and \(\gamma>0\). There is a universal \(C\) such that every solution satisfies
\[
\int_{B_1}\bigl(|x|^Bu^{q+1}+|x|^Av^{p+1}\bigr)\,dx\le E\le C .
\]

**Proof.** Let \(T=\int w(x)D(x,y)\,d\pi\) and \(Q=\int\bigl(\Phi-\eta(x)+w(x)D\bigr)\,d\pi\), both finite. Since \(\int\eta(x)\,d\pi=E_f\), the virial identity (2.1) of [A localized virial identity](a-localized-virial-identity.md) reads
\[
\begin{aligned}
&c_1E_f+c_2E_g=aW_f+bW_g\\
&\quad -(n-2)T+(n-2)Q,\\
&c_1=a(n+B)-(n-2),\quad c_2\\
&\quad =b(n+A).
\end{aligned}
\]
Let \(\epsilon>0\). By Proposition 4.1 and the localization lemma (3.1) there, which bounds \(|Q|\) and \(|E_f-E_g|\) by \(\epsilon E+C_\epsilon\),
\[
c_1E_f+c_2E_g\le(n-1)\epsilon E+C_\epsilon .
\]
Since \(c_1+c_2=\gamma\), we have \(c_1E_f+c_2E_g=\frac\gamma2E+\frac{c_1-c_2}2(E_f-E_g)\), hence
\[
\frac\gamma2E\le\Bigl(n-1+\frac{|c_1-c_2|}2\Bigr)\epsilon E+C_\epsilon .
\]
Choose \(\epsilon\) so that the coefficient on the right is at most \(\gamma/4\); since \(E\) is finite for each solution, \(E\le4C_\epsilon/\gamma\). The first inequality holds because \(\eta=1\) on \(B_1\). \(\square\)

Proposition 5.1, together with the scaling argument in the proof of Theorem 5.2 of [Positive solutions and their potentials](positive-solutions-and-their-potentials.md), gives:

**Theorem 5.2** (OpenAI 2026). Let \(n\ge2\), \(p,q>0\), \(A,B\in\mathbb R\), and \(\frac{n+A}{p+1}+\frac{n+B}{q+1}>n-2\). There are no functions \(u,v\), continuous and positive on \(\mathbb R^n\) and twice continuously differentiable on \(\mathbb R^n\setminus\{0\}\), with \(-\Delta u=|x|^Av^p\) and \(-\Delta v=|x|^Bu^q\) on \(\mathbb R^n\setminus\{0\}\). In particular (\(A=B=0\)) the Lane–Emden conjecture holds.

Indeed, the energy of the rescaled solutions \(u_R,v_R\) on \(B_1\) is \(R^{\alpha+\beta+2-n}\) times the energy of \(u,v\) on \(B_R\), which tends to infinity, while Proposition 5.1 bounds it uniformly.

**Remark 5.3** (the critical hyperbola). For \(n\ge3\) and \(A,B>-2\), Bidaut-Véron and Giacomini proved that radial positive solutions exist when \(\frac{n+A}{p+1}+\frac{n+B}{q+1}\le n-2\) [BVG, Theorem 1.4(i)], as recorded by Phan [Phan, Proposition B]. Together with Theorem 5.2 this gives Phan's conjectured classification: positive solutions exist exactly when the inequality fails. The existence half is not proved in this course; Exercise 6.3 of [Positive solutions and their potentials](positive-solutions-and-their-potentials.md) checks it in the scalar critical case.

**Remark 5.4** (later work). Mei and Wei carried the method of this course, the localized virial identity for an interaction measure and the comparison on pairs of source intervals along lines, from the Newton kernel to the Riesz kernel \(|x|^{2s-n}\), \(0<s<1\). They proved the fractional Lane–Emden conjecture: for \(n\ge2\), \(0<s<1\), \(p,q>0\) and \(\frac1{p+1}+\frac1{q+1}>\frac{n-2s}n\), the system \((-\Delta)^su=v^p\), \((-\Delta)^sv=u^q\) has no strictly positive solution on \(\mathbb R^n\) [MW, Theorem 1.2]. Two nonlocal points need separate treatment: for \(2s\le1\) the two equations must be combined before the diagonal is removed, and for \(2s>n-1\) the kernel restricted to a line is not integrable at infinity [MW, Section 1]. By a different method, with integral bounds derived from a divergence inequality, Lu and Zhang proved the Lane–Emden conjecture (\(A=B=0\)) for \(n\ge3\), \(pq>1\) and exponents in the closed disk \(\bigl(p-\frac2{n-2}\bigr)^2+\bigl(q-\frac2{n-2}\bigr)^2\le\frac{2n^2}{(n-2)^2}\), except at the point \(p=q=\frac{n+2}{n-2}\) where the disk touches the critical hyperbola [LZ]; for \(n\ge5\) the disk contains points not covered by the earlier criteria.

## 6. Exercises

**Exercise 6.1** (easy). Verify (3.1), and the corresponding identity \(\int_0^{g(y)}\bigl[v(y)-(t'/|y|^A)^{1/p}\bigr]dt'=b\,g(y)v(y)\).

**Exercise 6.2** (easy). Check that \(c_1+c_2=\gamma\) and that \(c_1E_f+c_2E_g=\frac\gamma2E+\frac{c_1-c_2}2(E_f-E_g)\).

**Exercise 6.3** (medium). Explain why, in Proposition 4.1, \(\kappa\) has to be chosen before \(\delta\), and \(\delta\) before \(P\).

**Exercise 6.4** (medium). Show that the bound \(V_f\le CH_f\) used in Section 2 follows from (1.1), with \(C\) universal.

## 7. Solutions

**6.1.** \(\int_0^{f}(t/|x|^B)^{1/q}\,dt=|x|^{-B/q}\frac{f^{1+1/q}}{1+1/q}\), which is \(\frac q{q+1}\,f\,(f/|x|^B)^{1/q}=\frac q{q+1}fu\), so the integral is \(fu-\frac q{q+1}fu=\frac{fu}{q+1}\). The identity for \(g\) is the same with \(p\), \(A\) and \(v\).

**6.2.** \(c_1+c_2\) equals \(a(n+B)+b(n+A)-(n-2)\), which is \(\gamma\). Expanding,
\[
\begin{aligned}
&\frac\gamma2(E_f+E_g)+\frac{c_1-c_2}2(E_f-E_g)\\
&\quad=\frac{\gamma+c_1-c_2}2E_f+\frac{\gamma-c_1+c_2}2E_g\\
&\quad=c_1E_f+c_2E_g.
\end{aligned}
\]

**6.3.** The coefficient of \(E\) is \(C\kappa+C_\kappa\delta+C_{\kappa,\delta}P^{-1}\). The constant \(C_\kappa\) grows as \(\kappa\to0\) (the caps get narrower and the weights larger), so \(\delta\) must be small relative to the chosen \(\kappa\); likewise \(C_{\kappa,\delta}\) grows as \(\delta\to0\), so \(P\) is chosen last. Only the additive constant \(C_{\kappa,\delta,P}\) grows, which is harmless.

**6.4.** When \(\chi_f(e,x,t)>0\), (1.1) gives \(\overline u_I\le(1+C\delta d(x))(t/|x|^B)^{1/q}\), which is at most \((1+C)u(x)\), so \(\chi_f\,\overline u_I\le(1+C)h_e(x)u(x)\). Integrating over \(0<t<f(x)\) and \(x\) gives \(V_f\le(1+C)\int h_efu=(1+C)H_f\).

## References

- [OpenAI-LE] OpenAI, *The subcritical Hénon–Lane–Emden conjecture*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/The-Subcritical-Henon-Lane-Emden-Conjecture-September-24-2026
- [BVG] M.-F. Bidaut-Véron and H. Giacomini, *A new dynamical approach of Emden–Fowler equations and systems*, Advances in Differential Equations 15 (2010), 1033–1082. https://arxiv.org/abs/1001.0562
- [Phan] Q. H. Phan, *Liouville-type theorems and bounds of solutions for Hardy–Hénon elliptic systems*, Advances in Differential Equations 17 (2012), 605–634. https://arxiv.org/abs/1108.1312
- [MW] L. Mei and J. Wei, *A proof of the fractional Lane–Emden conjecture*, arXiv:2610.10188 (October 2026). https://arxiv.org/abs/2610.10188
- [LZ] H. Lu and Z. Zhang, *New result on Lane–Emden conjecture with exponents in a disk*, arXiv:2610.09526 (October 2026). https://arxiv.org/abs/2610.09526
