# A ball from a holomorphic zero

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(f\) be a holomorphic map with a single zero, at the origin, of order at least \(k\). This lesson shows that the sublevel set \(\{|f|^2<1\}\), with the symplectic form of the potential \(|z|^2+|f|^2\), contains balls of every capacity below \(\pi k\) (Theorem 4.1). The order of vanishing gives the logarithmic potential \(\log|f|^2\) a slope \(k\) near zero; replacing that singularity by a smooth radial potential exposes a ball, and Moser's method transports the ball back to the original form. The theorem and its proof are OpenAI's [OpenAI-SB, Section 2]. The tools are those of [Forms, flows and Moser's method](forms-flows-and-moser-s-method.md) and [Plurisubharmonic potentials](plurisubharmonic-potentials.md); the radial coordinate is the radial case of a construction of Loi and Zuddas [LZ].

## 1. The theorem

**Theorem 4.1.** Let \(n,m\ge1\), let \(\Omega\subseteq\mathbf C^n\) be an open set containing \(0\), and let \(f=(f_1,\dots,f_m):\Omega\to\mathbf C^m\) be holomorphic. Suppose that for some integer \(k\ge1\):

1. \(f^{-1}(0)=\{0\}\), and \(|f(z)|\le C_0|z|^k\) for some constant \(C_0\) and all \(z\) near \(0\);
2. for every \(0<s<1\), the set \(\{z\in\Omega:|f(z)|^2\le s\}\) is compact.

Put \(\tau=|f|^2\), \(V=\{z\in\Omega:\tau(z)<1\}\) and \(\omega=dd^c(|z|^2+\tau)\). Then \(\omega\) is a symplectic form on \(V\), and for every \(0<c<\pi k\) there is an injective smooth map \(E:B^{2n}(c)\to V\) with \(E^*\omega=\omega_0\); it is a diffeomorphism onto an open subset of \(V\).

The form \(\omega\) is symplectic by Lemmas 3.5 and 3.4. The compactness in condition 2 concerns closed sublevel sets strictly below \(1\); nothing is assumed about the boundary of \(V\), which need not be connected or smooth.

## 2. The proof

Fix \(0<a<k\); we construct \(E\) on \(B^{2n}(\pi a)\). Choose numbers \(b\) and \(\mu\) with
\[
\frac ak<b<1,\qquad a<\mu<bk.
\]

*Step 1: a logarithmic potential with slope \(b\).* Choose \(\log b<t_-<t_+<0\) and a smooth nondecreasing function \(\beta:\mathbf R\to[0,1]\) with \(\beta=0\) on \((-\infty,t_-]\) and \(\beta=1\) on \([t_+,\infty)\). Let \(\chi\) be the function on \((-\infty,0)\) with
\[
\chi'(t)=b+\beta(t)\bigl(e^t-b\bigr)
\]
and \(\chi(t)=e^t\) for \(t\ge t_+\); this is consistent because \(\chi'=e^t\) there. Where \(\beta(t)>0\) we have \(t>t_-\), so \(e^t>b\); hence \(\chi'\ge b>0\) and
\[
\chi''(t)=\beta'(t)\bigl(e^t-b\bigr)+\beta(t)e^t\ge0.
\]
On \((-\infty,t_-]\), \(\chi\) is affine with slope \(b\): \(\chi(t)=bt+c_-\) for a constant \(c_-\).

On \(V\setminus\{0\}\) we have \(0<\tau<1\), and \(\log\tau\) is plurisubharmonic by Lemma 3.5. By Lemma 3.6 with \(\Gamma=\chi\), the smooth function
\[
H=\chi(\log\tau)
\]
is plurisubharmonic on \(V\setminus\{0\}\), and \(H=\tau\) wherever \(\tau\ge s_0:=e^{t_+}\). Near \(0\), condition 1 gives \(\log\tau\le\log C_0^2+k\log|z|^2\), which is below \(t_-\) for small \(z\ne0\); there \(H=b\log\tau+c_-\), so there is a constant \(C_1\) with
\[
\begin{aligned}
&H(z)\le bk\log|z|^2+C_1\\
&\text{for all small }z\ne0.
\end{aligned} \tag{4.1}
\]

*Step 2: smoothing the singularity without changing the form near the boundary.* Write \(B_r=\{|z|<r\}\) and choose \(r_2>0\) with \(\overline{B_{r_2}}\subset V\). For \(0<\delta\le1\) put
\[
P_\delta(z)=\mu\log(|z|^2+\delta)-M.
\]
These functions are plurisubharmonic on \(\mathbf C^n\) (Exercise 3.2). The function \(H\) is continuous on the sphere \(|z|=r_2\), where \(f\ne0\); choose
\[
M>\mu\log(r_2^2+1)-\min_{|z|=r_2}H+2.
\]
Since \(P_\delta(z)\le\mu\log(|z|^2+1)-M\), the strict inequality \(P_\delta<H-2\) holds on the sphere and, by continuity of the bound \(\mu\log(|z|^2+1)-M\) and of \(H\), on a neighbourhood \(A\) of the sphere, for every \(0<\delta\le1\). On the other hand, \(\log(|z|^2+\delta)\ge\log|z|^2\) and (4.1) give
\[
\begin{aligned}
P_\delta(z)-H(z)&\ge(\mu-bk)\log|z|^2\\
&\quad-M-C_1,
\end{aligned}
\]
which tends to \(+\infty\) as \(z\to0\), uniformly in \(\delta\), because \(\mu<bk\). Fix \(0<r_1<r_2\) such that
\[
\begin{aligned}
&P_\delta>H+2\\
&\text{on }0<|z|\le r_1,\\
&\text{for every }0<\delta\le1,
\end{aligned} \tag{4.2}
\]
and then fix one \(\delta\) with
\[
\begin{aligned}
&0<\delta\\
&<\min\{1,\,r_1^2(\mu/a-1)\};
\end{aligned} \tag{4.3}
\]
the right side is positive because \(\mu>a\).

Let \(\operatorname{rmax}\) be the smooth maximum of Lemma 3.7, and define \(\widetilde H\) on \(V\) by
\[
\widetilde H=\begin{cases}\operatorname{rmax}(H,P_\delta)&\text{on }B_{r_2}\setminus\{0\},\\ H&\text{on }V\setminus B_{r_2},\\ P_\delta(0)&\text{at }0.\end{cases}
\]
On \(A\cap B_{r_2}\) the two functions differ by more than \(1\), so \(\operatorname{rmax}(H,P_\delta)=H\) there; on \(B_{r_1}\setminus\{0\}\), by (4.2), \(\operatorname{rmax}(H,P_\delta)=P_\delta\). Hence \(\widetilde H\) is smooth on \(V\), equal to \(H\) near the sphere \(|z|=r_2\) and to \(P_\delta\) on \(B_{r_1}\), and plurisubharmonic by Lemmas 3.6 and 3.7.

The difference \(\widetilde H-\tau\) vanishes outside a compact subset of \(V\). Indeed, put \(s_2=\max_{\overline{B_{r_2}}}\tau<1\), choose \(\max(s_0,s_2)<\sigma<1\), and let
\[
C=\{z\in\Omega:\ \tau(z)\le\sigma\},
\]
a compact subset of \(V\) by condition 2. A point of \(V\) outside \(C\) has \(\tau>\sigma\ge s_0\), so \(H=\tau\) there, and it lies outside \(\overline{B_{r_2}}\), where \(\widetilde H=H\).

*Step 3: transport by Moser's method.* Let \(\sigma_0:\mathbf R\to[0,1]\) be smooth and nondecreasing with \(\sigma_0=0\) on \((-\infty,0]\) and \(\sigma_0=1\) on \([1,\infty)\), and put
\[
\begin{aligned}
\Omega_s&=dd^c\bigl(|z|^2+(1-\sigma_0(s))\tau\\
&\qquad+\sigma_0(s)\widetilde H\bigr)\qquad(s\in\mathbf R).
\end{aligned}
\]
A convex combination of plurisubharmonic functions is plurisubharmonic, so each \(\Omega_s\) is symplectic by Lemma 3.4. Moreover \(\partial_s\Omega_s=d\gamma_s\) with
\[
\gamma_s=\sigma_0'(s)\,d^c\bigl(\widetilde H-\tau\bigr),
\]
and all these one-forms vanish outside \(C\). By Theorem 2.8 there is a diffeomorphism \(\varphi\) of \(V\) onto itself with \(\varphi^*\widetilde\omega=\omega\), where \(\widetilde\omega=\Omega_1=dd^c(|z|^2+\widetilde H)\) and \(\Omega_0=\omega\). Thus \((\varphi^{-1})^*\omega=\widetilde\omega\).

*Step 4: the ball in the radial model.* On \(B_{r_1}\) the potential of \(\widetilde\omega\) is \(|z|^2+P_\delta=\Psi(|z|^2)-M\), with
\[
\Psi(t)=t+\mu\log(t+\delta),
\]
and constants do not change \(dd^c\). The function \(\Psi\) satisfies the hypotheses of Lemma 3.9 (Exercise 3.4), so the map \(R(z)=\sqrt{\Psi'(|z|^2)}\,z\) is a diffeomorphism of \(B_{r_1}\) onto \(B^{2n}(\pi Q_\delta)\) with \(R^*\omega_0=\widetilde\omega\) on \(B_{r_1}\), where
\[
Q_\delta=r_1^2\Psi'(r_1^2)=r_1^2+\frac{\mu r_1^2}{r_1^2+\delta}.
\]
By (4.3), \(r_1^2+\delta<\mu r_1^2/a\), so \(Q_\delta>r_1^2+a>a\). Let \(\iota:B_{r_1}\to V\) be the inclusion and put
\[
E=\varphi^{-1}\circ\iota\circ R^{-1}\quad\text{on }B^{2n}(\pi a).
\]
It is an injective smooth map, a diffeomorphism onto an open subset of \(V\), and
\[
\begin{aligned}
E^*\omega&=(R^{-1})^*\,\iota^*(\varphi^{-1})^*\omega\\
&=(R^{-1})^*\bigl(\widetilde\omega|_{B_{r_1}}\bigr)=\omega_0.
\end{aligned}
\]
Since \(a\in(0,k)\) was arbitrary, this proves Theorem 4.1. \(\square\)

## 3. Remarks

The proof never uses a ball of capacity \(\pi k\) itself: the strict inequalities \(a<\mu<bk\) leave room for the smoothing in Step 2. The capacity \(\pi a\) is visible in the radial model, where the potential \(\mu\log(|z|^2+\delta)\) contributes the term \(\mu r_1^2/(r_1^2+\delta)\), close to \(\mu\), to the squared radius; the order of vanishing enters only through (4.1), which allows \(P_\delta\) to dominate \(H\) near the origin.

For \(f(z)=z_1^k\) on \(\Omega=\{|z_1|<1,\ |z_2|<1\}\subset\mathbf C^2\), condition 1 fails because \(f\) vanishes on the line \(z_1=0\); the hypothesis that \(0\) is the only zero cannot be dropped from the argument, since \(\log\tau\) must be defined on \(V\setminus\{0\}\).

## 4. Exercises

**4.1** (easy). Check that \(\chi\) is convex and that \(\chi(t)=bt+c_-\) for \(t\le t_-\), and compute \(c_-\) when \(\beta\) is replaced by the indicator of \([t_+,\infty)\) (a nonsmooth model).

**4.2** (medium). Let \(n=m=1\), \(\Omega=\{|z|<1\}\) and \(f(z)=z^k\). Show that the hypotheses of Theorem 4.1 hold, that \(V=\Omega\), and that \((V,\omega)\) has area \(\pi(1+k)\). Explain why balls of capacity below \(\pi k\) fit, in accordance with the theorem.

**4.3** (easy). Show that the condition \(\delta<r_1^2(\mu/a-1)\) is equivalent to \(\mu r_1^2/(r_1^2+\delta)>a\).

## 5. Solutions

**4.1.** \(\chi''=\beta'(e^t-b)+\beta e^t\ge0\) as in Step 1, and \(\chi'=b\) on \((-\infty,t_-]\). For the indicator model, \(\chi'=b\) for \(t<t_+\) and \(\chi(t)=e^t\) for \(t\ge t_+\), so \(\chi(t)=b(t-t_+)+e^{t_+}\) for \(t<t_+\) and \(c_-=e^{t_+}-bt_+\).

**4.2.** \(f\) vanishes only at \(0\), \(|f(z)|=|z|^k\), and \(\{|z|^{2k}\le s\}\) is a closed disc inside \(\Omega\) for \(s<1\); \(V=\{|z|^{2k}<1\}=\Omega\). By Lemma 3.2, \(\omega=(1+k^2|z|^{2k-2})\,du\wedge dx\), whose integral over the disc is \(\pi+\int_0^12\pi r\,k^2r^{2k-2}\,dr=\pi+\pi k\). A disc of capacity \(c\) has area \(c\), and the theorem gives every \(c<\pi k\), within the total area \(\pi(1+k)\).

**4.3.** Both are equivalent to \(r_1^2+\delta<\mu r_1^2/a\).

## References

- [OpenAI-SB] OpenAI, *Symplectic balls in symmetric polar products*, OpenAI Math Release preprint, 22 September 2026, Section 2, Theorem 2.1. https://github.com/openai/math/tree/main/preprints/Symplectic-Balls-in-Symmetric-Polar-Products-September-22-2026
- [LZ] A. Loi and F. Zuddas, *Symplectic maps of complex domains into complex space forms*, Journal of Geometry and Physics 58 (2008), 888–899; arXiv:0803.3532. https://arxiv.org/abs/0803.3532
