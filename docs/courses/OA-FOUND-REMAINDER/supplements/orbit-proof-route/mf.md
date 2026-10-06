<span id="the-modular-group-and-its-analytic-algebra"></span>
# The modular group and its analytic algebra

<span id="oa-mod-mf-01--starting-data-full-completion-and-exact-inputs"></span>
<span id="OA-MOD-MF-01"></span>
<span id="oa-mod-mf-01"></span>
## OA-MOD-MF-01 — Starting data, full completion and exact inputs

Start with any left Hilbert algebra \(\mathcal C\subseteq H\). Use WH-03–04 to replace it by its full left completion \(\mathcal A\), without changing its closed involution \(S\), generated algebra \(M\), or full right algebra \(\mathcal D\). Thus
\[
M=\lambda(\mathcal A)'',\qquad
M'=R(\mathcal D)'',\qquad
F=S^*,
\]
\[
\mathcal A=\mathcal B_l\cap D(S),\qquad
\mathcal D=\mathcal B_r\cap D(F).
\tag{MF.1}
\]
The spaces \(\mathcal B_l,\mathcal B_r\) and their injective operators \(\lambda_\xi,R_\eta\) are the exact bounded-vector spaces of WH. In particular,
\[
\lambda_\xi\eta=R_\eta\xi
\quad(\xi\in\mathcal B_l,\ \eta\in\mathcal B_r).
\tag{MF.2}
\]
Write \(\xi^\sharp=S\xi\) on \(\mathcal A\), and \(\eta^\flat=F\eta\) on \(\mathcal D\). Products and their order are those of HA and WH:
\(\xi\zeta=\lambda_\xi\zeta\) on the left algebra and
\(\eta\theta=R_\theta\eta\) on the right algebra.

The closed-involution polar theorem gives
\[
\Delta=FS,\qquad S=J\Delta^{1/2},\qquad
F=J\Delta^{-1/2},\qquad J^2=I,\qquad J\Delta J=\Delta^{-1}.
\tag{MF.3}
\]
Every equality includes its operator domain; \(\Delta\) is injective, positive and self-adjoint, and \(J\) is antiunitary. Put \(U_t=\Delta^{it}\). Spectral transport gives
\[
J\Delta^zJ=\Delta^{-\overline z},\qquad JU_t=U_tJ
\quad(z\in\mathbb C,\ t\in\mathbb R),
\tag{MF.4}
\]
on the transported domains. The conjugation of the scalar exponent in (MF.4) is part of the formula.

The exact inputs are HA, RD and WH for all multiplication, affiliation and graph-core statements; TC for (MF.3); SK-05, SK-07–09 for spectral domains, cutoffs, powers, transport and dominated convergence; and MA-04, MA-06–09, MA-14–16 for Fourier uniqueness, the resolvent kernel, weak operator equations, bounded strips, spectral-domain recognition, vector contour identities and Gaussian entire vectors. The Gaussian transform also uses MA-03. These results are used at the stated domain, graph-core and spectral levels.

For clarity, the following consequence of RD will be used without strengthening it. If \(\xi\in D(S)\), close the densely defined operator
\[
T_\xi^0:\mathcal D\longrightarrow H,\qquad
T_\xi^0\eta=R_\eta\xi.
\]
The closed operator \(T_\xi\) is affiliated with \(M\), and
\[
\mathcal D\subseteq D(T_\xi^*),\qquad
T_\xi^*\eta=R_\eta S\xi.
\tag{MF.5}
\]
This is RD applied to the opposite right Hilbert algebra. It does not assert that \(\mathcal D\) is a core for \(T_\xi^*\). With the polar notation
\[
T_\xi=uh=ku,\quad h=(T_\xi^*T_\xi)^{1/2},
\quad k=(T_\xi T_\xi^*)^{1/2},
\]
one has \(u\in M\) and the spectral projections of \(h,k\) in \(M\). For real \(f\in C_c(0,\infty)\), extended by zero at zero, RD-03 gives
\[
\begin{aligned}
f(k)\xi&\in\mathcal A,&
\lambda_{f(k)\xi}&=kf(k)u,\\
f(h)S\xi&\in\mathcal A,&
\lambda_{f(h)S\xi}&=hf(h)u^*,\\
S(f(k)\xi)&=f(h)S\xi.
\end{aligned}
\tag{MF.6}
\]
All operators displayed on the right are bounded extensions. No commutation between \(\Delta\) and \(h\) or \(k\) is assumed.

<span id="oa-mod-mf-02--the-resolvent-creates-bounded-multiplication"></span>
<span id="OA-MOD-MF-02"></span>
<span id="oa-mod-mf-02"></span>
## OA-MOD-MF-02 — The resolvent creates bounded multiplication

For \(z\in\mathbb C\setminus[0,\infty)\), define
\[
\gamma(z)=\frac1{\sqrt{\,2(|z|-\operatorname{Re}z)\,}}.
\tag{MF.7}
\]
Its denominator is strictly positive.

**Theorem.** For \(\eta\in\mathcal D\),
\[
\xi=(\Delta-z)^{-1}\eta\in\mathcal A,\qquad
\|\lambda_\xi\|\leq\gamma(z)\|R_\eta\|.
\tag{MF.8}
\]
Symmetrically, for \(\xi\in\mathcal A\),
\[
(\Delta^{-1}-z)^{-1}\xi\in\mathcal D,\qquad
\bigl\|R_{(\Delta^{-1}-z)^{-1}\xi}\bigr\|
\leq\gamma(z)\|\lambda_\xi\|.
\tag{MF.9}
\]

**Proof.** The spectral resolvent has range in \(D(\Delta)\subseteq D(S)\), so the operator and cutoffs of (MF.5–6) are available for \(\xi=(\Delta-z)^{-1}\eta\). Fix real \(f\in C_c(0,\infty)\). Applying the last equation of (MF.6) to the function \(g(t)=t^2f(t)^2\) gives
\[
v=k^2f(k)^2\xi\in D(S),\qquad
Sv=h^2f(h)^2S\xi.
\]
Since \(\xi\in D(\Delta)\), the adjoint pairing for \(F=S^*\) yields
\[
E:=\langle\Delta\xi,v\rangle
=\langle Sv,S\xi\rangle
=\|hf(h)S\xi\|^2\geq0.
\tag{MF.10}
\]
The bounded self-adjoint operator \(B=kf(k)\) also gives
\(E=\langle B\Delta\xi,B\xi\rangle\). Cauchy–Schwarz and
\(2ab\leq a^2+b^2\) imply
\[
\begin{aligned}
2(|z|-\operatorname{Re}z)E
&\leq\|B\Delta\xi\|^2+|z|^2\|B\xi\|^2
       -2\operatorname{Re}z\,E\\
&=\|B(\Delta-z)\xi\|^2
=\|kf(k)\eta\|^2.
\end{aligned}
\tag{MF.11}
\]
The reality of \(E\), established in (MF.10), justifies the complex cross term. This step never moves a cutoff through \(\Delta\).

Polar transport and (MF.6) give
\[
kf(k)=u\,hf(h)u^*=u\lambda_{f(h)S\xi}.
\]
Using (MF.2) at the algebra vector \(f(h)S\xi\),
\[
\|kf(k)\eta\|
=\|uR_\eta f(h)S\xi\|
\leq\|R_\eta\|\|f(h)S\xi\|.
\]
Thus, with \(c=\gamma(z)\|R_\eta\|\),
\[
\|hf(h)S\xi\|^2\leq c^2\|f(h)S\xi\|^2
\quad(f\in C_c(0,\infty),\ f\text{ real}).
\tag{MF.12}
\]

Let \(\mu\) be the finite spectral measure of \(h\) at \(S\xi\).
Equation (MF.12) says
\(\int(t^2-c^2)f(t)^2\,d\mu(t)\leq0\).
Real compactly supported tests inside \((c,\infty)\) imply that this interval has measure zero: a nonnegative cutoff equal to one on each compact subinterval forces its measure to vanish, and a countable increasing union covers the interval. Therefore
\[
P S\xi=S\xi,\qquad P=1_{[0,c]}(h)\in M.
\tag{MF.13}
\]
The possible spectral mass at zero is included in \(P\).

For \(\theta\in\mathcal D\), affiliation puts \(P\) in the commutant of \(R_\theta\). Equation (MF.5) therefore gives
\[
R_\theta S\xi
=P R_\theta S\xi
=P T_\xi^*\theta
=P h u^*\theta.
\]
Since \(Ph\) is bounded with norm at most \(c\), this proves
\(\|R_\theta S\xi\|\leq c\|\theta\|\). Hence
\(S\xi\in\mathcal B_l\). It already lies in \(D(S)\), since \(S\) is an involution. Thus \(S\xi\in\mathcal A\), with
\(\|\lambda_{S\xi}\|\leq c\). Fullness and the adjoint identity give
\(\xi=S(S\xi)\in\mathcal A\) and
\(\|\lambda_\xi\|=\|\lambda_{S\xi}\|\leq c\), proving (MF.8).

Apply this proved statement to the opposite right Hilbert algebra \(\mathcal D^{\mathrm{op}}\). Its closed involution is \(F\), whose modulus squared is \(SF=\Delta^{-1}\), and its two bounded multiplication maps are \(R\) and \(\lambda\). This gives precisely (MF.9). \(\square\)

In particular, for \(s>0\), \(\gamma(-s)=1/(2\sqrt s)\). The estimate controls the multiplication norm as well as the Hilbert vector.

<span id="oa-mod-mf-03--a-common-domain-for-the-two-half-powers"></span>
<span id="OA-MOD-MF-03"></span>
<span id="oa-mod-mf-03"></span>
## OA-MOD-MF-03 — A common domain for the two half powers

Set
\[
V=D(\Delta^{1/2})\cap D(\Delta^{-1/2}),\qquad
\|\zeta\|_V^2=\|\zeta\|^2+\|\Delta^{1/2}\zeta\|^2
                         +\|\Delta^{-1/2}\zeta\|^2.
\tag{MF.14}
\]

**Lemma.** The space \(\mathcal A\cap D(\Delta^{-1/2})\) is dense in \(V\) for this norm.

**Proof.** The positive spectral function
\[
Q=\Delta^{1/2}+\Delta^{-1/2}
\]
has domain exactly \(V\). Indeed the square of its scalar function is
\(t+t^{-1}+2\), so its graph norm is equivalent to (MF.14).
One has \(Q\geq2I\), and \(Q^{-1}\), \(\Delta^{1/2}Q^{-1}\) and
\(\Delta^{-1/2}Q^{-1}\) are bounded, the last two by one.

The subspace \(\Delta^{-1/2}\mathcal D\) is dense in \(H\), because
\(\Delta^{-1/2}=JF\) and \(F\mathcal D=\mathcal D\). Given \(\zeta\in V\), choose \(\eta_n\in\mathcal D\) with
\[
\Delta^{-1/2}\eta_n\longrightarrow Q\zeta.
\]
Put \(\zeta_n=(1+\Delta)^{-1}\eta_n\). MF-02 gives \(\zeta_n\in\mathcal A\). Spectral calculus and \(\eta_n\in D(\Delta^{-1/2})\) give
\[
\zeta_n\in D(\Delta^{-1/2}),\qquad
Q\zeta_n=\Delta^{-1/2}\eta_n.
\]
Applying the three bounded operators listed above proves convergence of \(\zeta_n\), \(\Delta^{1/2}\zeta_n\) and
\(\Delta^{-1/2}\zeta_n\) to their respective targets. \(\square\)

This is a joint graph-core argument, not the inference that two separate cores are automatically a core for the sum of their graph norms.

<span id="oa-mod-mf-04--the-resolvent-satisfies-a-weak-operator-equation"></span>
<span id="OA-MOD-MF-04"></span>
<span id="oa-mod-mf-04"></span>
## OA-MOD-MF-04 — The resolvent satisfies a weak operator equation

Fix \(s>0\), \(\eta\in\mathcal D\), and
\[
\xi=(\Delta+s)^{-1}\eta,\qquad
X=R_\eta,\qquad Y=J\lambda_\xi^*J.
\tag{MF.15}
\]
Both \(X,Y\) are bounded; membership of \(Y\) in \(M'\) is not yet asserted.

**Theorem.** For every \(\zeta_1,\zeta_2\in V\),
\[
\langle X\zeta_1,\zeta_2\rangle
=
\langle Y\Delta^{-1/2}\zeta_1,\Delta^{1/2}\zeta_2\rangle
+s\langle Y\Delta^{1/2}\zeta_1,\Delta^{-1/2}\zeta_2\rangle.
\tag{MF.16}
\]

**Proof.** Begin with \(\zeta_1,\zeta_2\in\mathcal A\cap D(F)\).
All products below then belong to \(\mathcal A\). In particular, put
\(v=(S\zeta_1)\zeta_2\), so \(Sv=(S\zeta_2)\zeta_1\).
By (MF.2) and \((\Delta+s)\xi=\eta\),
\[
\langle X\zeta_1,\zeta_2\rangle
=\langle\eta,v\rangle
=\langle\Delta\xi,v\rangle+s\langle\xi,v\rangle.
\tag{MF.17}
\]

We identify the two terms without formal products of unbounded operators. The antiunitary identity
\(\langle Ju,w\rangle=\langle Jw,u\rangle\), together with
\(S=J\Delta^{1/2}\), \(F=J\Delta^{-1/2}\), gives
\[
\begin{aligned}
\langle Y\Delta^{1/2}\zeta_1,\Delta^{-1/2}\zeta_2\rangle
&=\langle F\zeta_2,\lambda_\xi^*S\zeta_1\rangle\\
&=\langle S(\lambda_\xi^*S\zeta_1),\zeta_2\rangle\\
&=\langle\zeta_1\xi,\zeta_2\rangle
=\langle\xi,v\rangle.
\end{aligned}
\tag{MF.18}
\]
The adjoint-domain step is legitimate since
\(\lambda_\xi^*S\zeta_1=(S\xi)(S\zeta_1)\in\mathcal A\).
Similarly,
\[
\begin{aligned}
\langle Y\Delta^{-1/2}\zeta_1,\Delta^{1/2}\zeta_2\rangle
&=\langle S\zeta_2,\lambda_\xi^*F\zeta_1\rangle\\
&=\langle\lambda_\xi S\zeta_2,F\zeta_1\rangle\\
&=\langle\zeta_1,S(\xi S\zeta_2)\rangle\\
&=\langle(S\zeta_2)\zeta_1,S\xi\rangle
=\langle\Delta\xi,v\rangle.
\end{aligned}
\tag{MF.19}
\]
Here \(\xi S\zeta_2\in\mathcal A\), and the last equality uses
\(\xi\in D(\Delta)\). Equations (MF.17–19) prove (MF.16) on this test space.

Each side of (MF.16) is a continuous sesquilinear form on \(V\times V\) with the norm (MF.14), because \(X,Y\) are bounded. MF-03 provides approximants simultaneously in both half-power graph norms. Passing to their limits proves (MF.16) on all of \(V\). \(\square\)

Both half-power domains are required in the statement. A formula containing \(\Delta^{1/2}\zeta_j\) cannot be asserted merely from membership in \(D(\Delta^{-1/2})\).

<span id="oa-mod-mf-05--fourier-uniqueness-recovers-the-commutant"></span>
<span id="OA-MOD-MF-05"></span>
<span id="oa-mod-mf-05"></span>
## OA-MOD-MF-05 — Fourier uniqueness recovers the commutant

For real \(r\), put
\[
k_r(t)=\frac{e^{-irt}}{e^{\pi t}+e^{-\pi t}},\qquad
\mathcal R_r(x)=\int_{\mathbb R}k_r(t)U_t x U_{-t}\,dt.
\tag{MF.20}
\]
The integral is taken on each Hilbert vector. Strong continuity and
\(\int|k_r|<\infty\) give a bounded operator with norm at most
\(\|x\|\int|k_r|\). Operator-norm continuity of \(t\mapsto U_t xU_{-t}\) is not assumed.

**Theorem.** For every \(\eta\in\mathcal D\) and \(t\in\mathbb R\),
\[
JU_t\eta\in\mathcal A,\qquad
\lambda_{JU_t\eta}=JU_t R_\eta U_{-t}J.
\tag{MF.21}
\]
Consequently
\[
J\mathcal D=\mathcal A,\qquad J\mathcal A=\mathcal D,\qquad
JMJ=M',\qquad JM'J=M.
\tag{MF.22}
\]

**Proof.** Apply the weak-equation theorem MA-07 to (MF.16), with
\(s=e^r\). It gives
\[
\mathcal R_r(R_\eta)
=e^{r/2}J\lambda_{(\Delta+e^r)^{-1}\eta}^*J.
\tag{MF.23}
\]
Fix \(\zeta\in\mathcal D\) and abbreviate
\(\xi_r=(\Delta+e^r)^{-1}\eta\). Applying (MF.23) to \(J\zeta\), using (MF.2), and then using the spectral integral MA-06, gives
\[
\begin{aligned}
\mathcal R_r(R_\eta)J\zeta
&=e^{r/2}J\lambda_{\xi_r}^*\zeta
=e^{r/2}J R_\zeta S\xi_r\\
&=JR_\zeta J\bigl[e^{r/2}\Delta^{1/2}
                    (\Delta+e^r)^{-1}\eta\bigr]\\
&=JR_\zeta J\int_{\mathbb R}k_r(t)U_t\eta\,dt.
\end{aligned}
\tag{MF.24}
\]
The operator \(JR_\zeta J\) in the last line is complex-linear, so the scalar kernel is unchanged when it passes through this operator.

Subtracting the two integral expressions for (MF.24) yields, for every real \(r\),
\[
\int_{\mathbb R}k_r(t)
\bigl[U_tR_\eta U_{-t}J\zeta
      -JR_\zeta J U_t\eta\bigr]\,dt=0.
\tag{MF.25}
\]
The bracket is a continuous bounded \(H\)-valued function of \(t\). After pairing with an arbitrary vector, multiplication by
\((e^{\pi t}+e^{-\pi t})^{-1}\) gives a continuous integrable scalar function. MA-04's Fourier uniqueness therefore makes that function zero at every \(t\). Separation by Hilbert pairings proves
\[
U_tR_\eta U_{-t}J\zeta=JR_\zeta J U_t\eta.
\]
Applying \(J\) to this equality of vectors gives
\[
JU_tR_\eta U_{-t}J\zeta=R_\zeta JU_t\eta.
\tag{MF.26}
\]
Thus \(\zeta\mapsto R_\zeta JU_t\eta\) is bounded on the dense right algebra \(\mathcal D\). By definition,
\(JU_t\eta\in\mathcal B_l\), and its left multiplier is the operator in (MF.21). Also \(U_t\eta\in D(F)\), and
\(JD(F)=D(S)\), by spectral transport in (MF.3–4).
Hence \(JU_t\eta\in\mathcal A\), proving (MF.21).

At \(t=0\) this gives \(J\mathcal D\subseteq\mathcal A\).
Apply the same proved statement to \(\mathcal D^{\mathrm{op}}\), whose modular data are \(\Delta^{-1}\) and \(J\). It gives
\(J\mathcal A\subseteq\mathcal D\). Since \(J^2=I\), both inclusions are equalities. The \(t=0\) operator identity is
\[
\lambda_{J\eta}=JR_\eta J\qquad(\eta\in\mathcal D).
\]
Taking generated von Neumann algebras and using
\(\lambda(\mathcal A)''=M\), \(R(\mathcal D)''=M'\), proves (MF.22). \(\square\)

The Fourier argument is pointwise in each pair of test vectors. It needs no countable family separating the Hilbert space.

<span id="oa-mod-mf-06--the-modular-fundamental-theorem"></span>
<span id="OA-MOD-MF-06"></span>
<span id="oa-mod-mf-06"></span>
## OA-MOD-MF-06 — The modular fundamental theorem

**Theorem.** The strongly continuous unitary group \(U_t=\Delta^{it}\) satisfies
\[
U_t\mathcal A=\mathcal A,\qquad U_t\mathcal D=\mathcal D,
\tag{MF.27}
\]
\[
\lambda_{U_t\xi}=U_t\lambda_\xi U_{-t},\qquad
R_{U_t\eta}=U_tR_\eta U_{-t},
\tag{MF.28}
\]
and consequently
\[
U_t M U_{-t}=M,\qquad U_t M'U_{-t}=M'.
\tag{MF.29}
\]
On each algebra the action is by complex-linear involution-preserving algebra automorphisms. The map \(J\) is a conjugate-linear involution-preserving algebra anti-isomorphism between \(\mathcal A\) and \(\mathcal D\):
\[
J(\xi\zeta)=(J\zeta)(J\xi),\qquad
J(S\xi)=F(J\xi).
\tag{MF.30}
\]
Together with (MF.22), these are the modular fundamental theorem for the original arbitrary left Hilbert algebra \(\mathcal C\). The invariant left algebra is its full completion \(\mathcal A\); the original core \(\mathcal C\) need not itself be invariant.

**Proof.** For \(\xi\in\mathcal A\), write \(\xi=J\eta\) with
\(\eta\in\mathcal D\). Equations (MF.4) and (MF.21) give
\(U_t\xi=JU_t\eta\in\mathcal A\), and
\[
\lambda_{U_t\xi}
=JU_tR_\eta U_{-t}J
=U_t\lambda_\xi U_{-t}.
\]
Applying this also to \(-t\) gives equality of the invariant spaces. The symmetric argument gives the assertions for \(\mathcal D\), proving (MF.27–28). Generated algebras give (MF.29).

Spectral calculus in (MF.3–4) gives
\(S U_t=U_t S\) on \(D(S)\), and \(F U_t=U_t F\) on \(D(F)\). For \(\xi,\zeta\in\mathcal A\),
\[
U_t(\xi\zeta)
=U_t\lambda_\xi\zeta
=\lambda_{U_t\xi}U_t\zeta.
\]
This proves the algebra and involution assertions, and the right case follows with its specified product order.

The identity \(\lambda_{J\eta}=JR_\eta J\) from MF-05 at \(t=0\), applied to \(\eta=J\xi\), gives
\(J\lambda_\xi J=R_{J\xi}\). Therefore
\[
J(\xi\zeta)=R_{J\xi}J\zeta=(J\zeta)(J\xi).
\]
The domain identity \(FJ=JS\) follows from (MF.3–4), proving the second formula of (MF.30). \(\square\)

**Bounded-vector extension.** The same covariance holds for every
\(\xi\in\mathcal B_l\) and \(\eta\in\mathcal B_r\). For example, for
\(\theta\in\mathcal D\),
\[
R_\theta U_t\xi
=U_tR_{U_{-t}\theta}\xi
=U_t\lambda_\xi U_{-t}\theta.
\]
This proves left boundedness of \(U_t\xi\) and identifies its operator; applying \(-t\) gives equality of the spaces. The right proof is symmetric.

**Weight consequence.** Let \(\varphi\) be a faithful normal semifinite weight with the GNS representation and full Hilbert algebra constructed in WH. Its modular automorphisms are
\[
\sigma_t^\varphi(x)
=\pi_\varphi^{-1}\bigl(\Delta_\varphi^{it}
           \pi_\varphi(x)\Delta_\varphi^{-it}\bigr).
\tag{MF.31}
\]
They form a one-parameter group of normal *-automorphisms. For each \(x\), the orbit is sigma-strong* continuous: in the GNS representation it is norm bounded and strongly* continuous, and WH-02 transports the intrinsic topology back to \(M\). The bounded-vector extension and WH-11 give
\[
\sigma_t^\varphi(\mathfrak n_\varphi)=\mathfrak n_\varphi,\qquad
\Lambda_\varphi(\sigma_t^\varphi(x))
=\Delta_\varphi^{it}\Lambda_\varphi(x)
\quad(x\in\mathfrak n_\varphi).
\tag{MF.32}
\]
Thus, for \(a\in M_+\), finiteness of \(\varphi(a)\) is equivalent to finiteness of \(\varphi(\sigma_t^\varphi(a))\), by applying (MF.32) to \(a^{1/2}\) and the inverse automorphism. In the finite case their values are equal Hilbert norms, and otherwise both are infinite. Consequently
\[
\varphi\circ\sigma_t^\varphi=\varphi.
\tag{MF.33}
\]
The full weight KMS characterization and its uniqueness theorem are separate results; invariance alone is not that characterization.

<span id="oa-mod-mf-07--the-maximal-entire-algebra"></span>
<span id="OA-MOD-MF-07"></span>
<span id="oa-mod-mf-07"></span>
## OA-MOD-MF-07 — The maximal entire algebra

Define
\[
\mathcal A_0=\{\xi\in\bigcap_{n\in\mathbb Z}D(\Delta^n):
                     \Delta^n\xi\in\mathcal A\text{ for every }n\in\mathbb Z\}.
\tag{MF.34}
\]
The condition includes negative powers, with their actual spectral domains. Put
\(U_z\xi=\Delta^{iz}\xi\) for \(\xi\in\mathcal A_0\) and \(z\in\mathbb C\).

**Theorem.** The space \(\mathcal A_0\) is a *-subalgebra of \(\mathcal A\), invariant under every \(U_z\) and under \(J\). Each \(U_z\) is an algebra automorphism of \(\mathcal A_0\). The vector map \(z\mapsto U_z\xi\) and the operator map \(z\mapsto\lambda_{U_z\xi}\) are norm-entire. If \(-\operatorname{Im}z\in[n,n+1]\), then
\[
\|\lambda_{U_z\xi}\|
\leq\max\{\|\lambda_{\Delta^n\xi}\|,
               \|\lambda_{\Delta^{n+1}\xi}\|\}.
\tag{MF.35}
\]
In particular both maps are uniformly bounded on each finite horizontal strip, in their respective norms.

**Proof.** The spectral domain criterion SK-05 and MA-09 shows that belonging to all integer-power domains makes \(z\mapsto U_z\xi\) norm-entire and bounded on finite horizontal strips. To prove bounded multiplication at a nonreal parameter, fix \(\eta\in\mathcal D\), \(\zeta\in H\), and consider
\[
f(z)=\langle R_\eta U_z\xi,\zeta\rangle.
\]
On the boundary \(z=t-in\), modular covariance gives
\[
|f(t-in)|\leq
\|\lambda_{\Delta^n\xi}\|\,\|\eta\|\,\|\zeta\|.
\]
The same estimate holds with \(n+1\) on the other boundary. The bounded-strip maximum principle MA-08 gives the maximum of these two constants throughout the strip. Taking the supremum over \(\zeta\) proves that \(U_z\xi\) is left bounded and gives (MF.35). It belongs to \(D(S)=D(\Delta^{1/2})\), so it belongs to \(\mathcal A\). Applying this argument to \(\Delta^m\xi\) for every integer \(m\) proves \(U_z\xi\in\mathcal A_0\).

The identity
\(\lambda_{U_z\xi}\eta=R_\eta U_z\xi\) gives entire vector coefficients on the dense test space \(\mathcal D\). Bound (MF.35) is locally uniform in operator norm. Here is the operator-valued passage explicitly. Approximation of arbitrary test vectors by vectors of \(\mathcal D\), locally uniform under that bound, makes every matrix coefficient entire. Fix a circle of radius \(R\) about any parameter, and let \(M_R\) bound the operator norms on the circle. The scalar Cauchy coefficient of order \(k\), for each pair of test vectors, is a bounded sesquilinear form of norm at most \(M_R R^{-k}\); Hilbert-space representation of that form defines a bounded operator \(A_k\) with this norm bound. The series \(\sum_k A_k w^k\) converges in operator norm for \(|w|<R\), and its matrix coefficients are exactly the scalar Taylor series of the given family. Equality of all coefficients identifies the operator family with this series. This proves operator-norm holomorphy without assuming that the original real orbit is norm continuous.

For \(\xi,\eta\in\mathcal A_0\), the vector function
\[
G(z)=\lambda_{U_z\xi}U_z\eta
\]
is norm-entire and bounded on each finite horizontal strip. On the real axis, MF-06 says \(G(t)=U_t(\xi\eta)\). MA-09 recognizes the spectral continuation: \(\xi\eta\) belongs to every real-power domain and
\[
U_z(\xi\eta)=(U_z\xi)(U_z\eta).
\tag{MF.36}
\]
At \(z=-in\), the right side belongs to \(\mathcal A\); hence \(\xi\eta\in\mathcal A_0\). The spectral product rule also gives
\[
\Delta^nS\xi=S\Delta^{-n}\xi,\qquad
S U_z\xi=U_{\overline z}S\xi.
\tag{MF.37}
\]
These equations have all their domains because \(\xi\) belongs to every power domain. Their first equation and the closure of \(\mathcal A\) under \(S\) show \(S\xi\in\mathcal A_0\). Thus \(\mathcal A_0\) is a *-algebra. The group law and invariance give bijectivity of every \(U_z\). Finally,
\[
J\xi=\Delta^{1/2}S\xi=U_{-i/2}S\xi\in\mathcal A_0.
\]
Since \(J^2=I\), equality \(J\mathcal A_0=\mathcal A_0\) follows. In particular \(\mathcal A_0\subseteq J\mathcal A=\mathcal D\). \(\square\)

<span id="oa-mod-mf-08--gaussian-approximation-with-vector-and-operator-bounds"></span>
<span id="OA-MOD-MF-08"></span>
<span id="oa-mod-mf-08"></span>
## OA-MOD-MF-08 — Gaussian approximation with vector and operator bounds

For \(r>0\) and \(\xi\in\mathcal A\), define the norm-convergent Hilbert-space integral
\[
\xi_r=\sqrt{r/\pi}\int_{\mathbb R}e^{-rt^2}U_t\xi\,dt.
\tag{MF.38}
\]
Then \(\xi_r\in\mathcal A_0\), and for every \(z\in\mathbb C\),
\[
U_z\xi_r=\sqrt{r/\pi}\int_{\mathbb R}
                       e^{-r(t-z)^2}U_t\xi\,dt,
\tag{MF.39}
\]
\[
\begin{aligned}
\|U_z\xi_r\|&\leq e^{r(\operatorname{Im}z)^2}\|\xi\|,\\
\|\lambda_{U_z\xi_r}\|&\leq
           e^{r(\operatorname{Im}z)^2}\|\lambda_\xi\|.
\end{aligned}
\tag{MF.40}
\]
As \(r\to\infty\),
\[
\xi_r\longrightarrow\xi,\qquad S\xi_r\longrightarrow S\xi
\quad\text{in }H,
\tag{MF.41}
\]
\[
\lambda_{\xi_r}\longrightarrow\lambda_\xi
\quad\text{strongly*},\qquad
\|\lambda_{\xi_r}\|\leq\|\lambda_\xi\|.
\tag{MF.42}
\]

**Proof.** The vector Gaussian lemma MA-16 proves (MF.39) and the first bound; it can also be checked by differentiating the Gaussian under its integrable bound on every compact set of parameters. Real translation gives the real orbit, and MA-09 identifies its entire continuation with the spectral powers.

Write the right side of (MF.39) as \(F_r(z)\). For \(\eta\in\mathcal D\), the bounded-vector identity and MF-06 give
\[
R_\eta F_r(z)=\sqrt{r/\pi}\int_{\mathbb R}e^{-r(t-z)^2}
                 U_t\lambda_\xi U_{-t}\eta\,dt.
\tag{MF.43}
\]
The integral is a strong operator integral: its value on each vector is a norm integral, and its norm bound follows from the scalar integral of the absolute Gaussian. This proves left boundedness and the second estimate in (MF.40). The same finite Riemann sums converge in the graph of the closed antilinear operator \(S\), because
\[
S F_r(z)=\sqrt{r/\pi}\int_{\mathbb R}
                   e^{-r(t-\overline z)^2}U_tS\xi\,dt.
\tag{MF.44}
\]
Indeed conjugating each scalar coefficient and using \(SU_t=U_tS\) gives this formula for every sum, and both tails are integrable in Hilbert norm. Thus \(F_r(z)\in\mathcal A\). At \(z=-in\), equation (MF.39) says \(\Delta^n\xi_r=F_r(-in)\in\mathcal A\), proving \(\xi_r\in\mathcal A_0\).

The positive real Gaussian has integral one and concentrates at zero. Strong continuity of \(U_t\) applied to \(\xi\) and \(S\xi\) proves (MF.41). Applying the same approximate-identity estimate to \(U_t\lambda_\xi U_{-t}\) and its adjoint proves strong* convergence and the contraction bound (MF.42). This argument uses strong* continuity on each vector; operator-norm continuity of the real orbit is unnecessary. \(\square\)

<span id="oa-mod-mf-09--the-analytic-algebra-is-a-common-core"></span>
<span id="OA-MOD-MF-09"></span>
<span id="oa-mod-mf-09"></span>
## OA-MOD-MF-09 — The analytic algebra is a common core

The space \(\mathcal A_0\), with \(\sharp=S|_{\mathcal A_0}\), is a left Hilbert algebra. Its closed involution is \(S\), its generated algebra is \(M\), its full right algebra is \(\mathcal D\), and its full left completion is \(\mathcal A\). It is also a right Hilbert algebra with involution \(\flat=F|_{\mathcal A_0}\), closed involution \(F\), and generated right algebra \(M'\). Moreover, \(\mathcal A_0\) is a core for every \(\Delta^a\), \(a\in\mathbb R\), and for both \(S\) and \(F\).

**Proof.** MF-08 makes \(\mathcal A_0\) dense and a graph core for \(S\), since \(\mathcal A\) already is a core. Equation (MF.42) gives
\(\lambda(\mathcal A_0)''=\lambda(\mathcal A)''=M\), and the left representation of \(\mathcal A_0\) is nondegenerate. To check the sometimes missing product-density axiom, suppose \(v\perp\mathcal A_0^2\). The inherited adjoint identity gives \(\lambda_\xi^*v=0\) for every \(\xi\in\mathcal A_0\). Since this algebra is closed under \(\sharp\), all its left operators annihilate \(v\), and nondegeneracy gives \(v=0\). Thus \(\mathcal A_0^2\) is dense. The other Hilbert-algebra axioms restrict from \(\mathcal A\).

The closed involution is exactly \(S\), so its adjoint is \(F\). If a vector \(\eta\in D(F)\) has a bounded right multiplication test on \(\mathcal A_0\), with bound \(c\), then for \(\xi\in\mathcal A\), (MF.41–42) gives
\[
\|\lambda_\xi\eta\|
=\lim_{r\to\infty}\|\lambda_{\xi_r}\eta\|
\leq c\lim_{r\to\infty}\|\xi_r\|=c\|\xi\|.
\]
Hence \(\eta\) is right bounded for \(\mathcal A\). Restriction gives the reverse implication. Its full right algebra is therefore exactly \(\mathcal D\); taking the full left dual gives \(\mathcal A\). The identity \(J\mathcal A_0=\mathcal A_0\) and \(F=JSJ\) now show that \(\mathcal A_0\) is a graph core for \(F\). Conjugating the left multiplication identities by \(J\), which reverses products by MF-06, proves the right Hilbert-algebra axioms and gives generated right algebra \(JMJ=M'\).

For the remaining power-core assertion, the scalar Gaussian transform MA-03 gives
\[
\xi_r=g_r(\Delta)\xi,\qquad
g_r(s)=\exp\bigl(- (\log s)^2/(4r)\bigr),\quad s>0.
\tag{MF.45}
\]
For every real \(a\), both \(g_r\) and \(s^a g_r(s)\) are bounded. Given \(\eta\in D(\Delta^a)\), dominated convergence gives
\(g_r(\Delta)\eta\to\eta\) in the graph norm of \(\Delta^a\). For fixed \(r\), approximate \(\eta\) in \(H\) by vectors \(\xi_j\in\mathcal A\). Boundedness of the two spectral functions gives
\(g_r(\Delta)\xi_j\to g_r(\Delta)\eta\) in that graph norm. Every vector on the left belongs to \(\mathcal A_0\) by MF-08. Choosing successively \(r\) and then \(j\) proves the core assertion. The same proof works for the sum of any finite family of power graph norms. \(\square\)

The algebra just constructed has the following four identities, which will serve as the definition in the converse theorem. For \(\xi,\eta\in\mathcal A_0\),
\[
\begin{aligned}
&z\longmapsto\langle U_z\xi,\eta\rangle\text{ is entire},\\
&(U_z\xi)^\sharp=U_{\overline z}\xi^\sharp,\\
&\langle U_z\xi,\eta\rangle
       =\langle\xi,U_{-\overline z}\eta\rangle,\\
&\langle\xi^\sharp,\eta^\sharp\rangle
       =\langle U_{-i}\eta,\xi\rangle.
\end{aligned}
\tag{MF.46}
\]
The first three follow from spectral calculus and (MF.37); the last is the closed-involution form identity \(\langle S\xi,S\eta\rangle=\langle\Delta\eta,\xi\rangle\). An algebraic group of automorphisms satisfying (MF.46) on a left Hilbert algebra is called a **Tomita algebra**. The four identities specify this terminology; no norm completion of that algebra is implicit.

