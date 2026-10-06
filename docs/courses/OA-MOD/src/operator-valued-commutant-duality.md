# Commutant duality for operator-valued weights

A faithful normal semifinite operator-valued weight on a concrete inclusion has a dual weight on the reversed commutant inclusion. The clean description uses spatial derivatives: the same positive self-adjoint operator represents the original scalar composite and the dual scalar composite, with numerator and denominator exchanged. This identity constructs the dual, proves that dualizing twice returns the starting weight, and fixes the order of the cocycle formula.

Throughout,

\[
N\subseteq M\subseteq B(H)
\tag{OD.1}
\]

is a unital concrete inclusion of arbitrary von Neumann algebras. Its commutant inclusion is \(M'\subseteq N'\), and the common relative commutant is

\[
N^c=N'\cap M=M\cap N'.
\tag{OD.2}
\]

All scalar and operator-valued weights in this lesson are faithful, normal and semifinite. We write \(\varphi\circ T\) for the scalar weight obtained by evaluating the extended-positive output of \(T\) with the normal extension of \(\varphi\).

## The spatial characterization of the dual

For every \(T\in\mathcal W_0(M,N)\), there is a unique

\[
T'\in\mathcal W_0(N',M')
\tag{OD.3}
\]

such that, for every \(\varphi\in\mathcal W_0(N)\) and \(\psi\in\mathcal W_0(M')\),

\[
\boxed{
\frac{d\varphi}{d(\psi\circ T')}
=
\frac{d(\varphi\circ T)}{d\psi}.}
\tag{OD.4}
\]

Both sides are positive injective self-adjoint operators on the given Hilbert space \(H\). Equation (OD.4) is stronger than a comparison of modular automorphisms: it includes the scale of both weights and determines their full spatial quadratic forms.

The assignment \(T\mapsto T'\) is an involutive bijection

\[
\begin{aligned}
T&\longmapsto T',\\
T&\in\mathcal W_0(M,N),\\
T'&\in\mathcal W_0(N',M').
\end{aligned}
\tag{OD.5}
\]

On \(N^c\), its modular data satisfy

\[
\sigma_t^{T'}=\sigma_{-t}^{T},
\tag{OD.6}
\]

and, for \(T_1,T_2\in\mathcal W_0(M,N)\),

\[
\boxed{
\begin{aligned}
&(DT_1:DT_2)_t\\
&\qquad=(DT_1':DT_2')_{-t}.
\end{aligned}}
\tag{OD.7}
\]

The indices in (OD.7) remain in the same order. OD-05 explains why the reversed index order printed in Takesaki II IX.4.24–25 cannot be correct.

## Constructing the dual from one pair of references

Fix \(T\in\mathcal W_0(M,N)\). Choose

\[
\begin{aligned}
\varphi&\in\mathcal W_0(N),\\
\psi&\in\mathcal W_0(M'),\\
\omega&\in\mathcal W_0(N').
\end{aligned}
\tag{OD.8}
\]

Such reference weights exist by the weight-existence theorem. Put

\[
\begin{aligned}
H_0&=\frac{d(\varphi\circ T)}{d\psi},\\
K&=\frac{d\varphi}{d\omega}.
\end{aligned}
\tag{OD.9}
\]

The two spatial modular actions, together with the forward modular restriction used in Lifting scalar modular flows and cocycles, say that both conjugations below equal \(\sigma_t^\varphi(n)\) for \(n\in N\). In particular,

\[
\begin{aligned}
&H_0^{it}nH_0^{-it}\\
&\qquad=K^{it}nK^{-it}.
\end{aligned}
\tag{OD.10}
\]

Therefore

\[
u_t=H_0^{-it}K^{it}
\tag{OD.11}
\]

commutes with \(N\), so \(u_t\in N'\). On \(N'\), the denominator part of the same spatial theorem says

\[
\sigma_s^\omega(y)=K^{-is}yK^{is}.
\tag{OD.12}
\]

Consequently

\[
u_s\sigma_s^\omega(u_t)
=u_{s+t}.
\tag{OD.13}
\]

Indeed, substitution of (OD.11–12) cancels the adjacent factors \(K^{is}K^{-is}\) and leaves \(H_0^{-i(s+t)}K^{i(s+t)}\), without commuting \(H_0\) past \(K\). Thus \(u\) is a strongly continuous unitary modular cocycle for \(\sigma^\omega\). The cocycle reconstruction theorem produces a unique \(\widetilde\psi\in\mathcal W_0(N')\) with

\[
[D\widetilde\psi:D\omega]_t=u_t.
\tag{OD.14}
\]

We now identify this reconstructed weight without guessing its scale. Let

\[
A=\frac{d\widetilde\psi}{d\varphi}.
\tag{OD.15}
\]

Spatial reciprocity gives \(d\omega/d\varphi=K^{-1}\). The spatial cocycle formula therefore turns (OD.14) into

\[
\begin{aligned}
u_t&=A^{it}(K^{-1})^{-it}\\
&=A^{it}K^{it}.
\end{aligned}
\tag{OD.16}
\]

Comparison with (OD.11), followed by right multiplication by \(K^{-it}\), gives

\[
A^{it}=H_0^{-it}\quad(t\in\mathbb R).
\tag{OD.17}
\]

The unitary group determines its positive injective generator, hence

\[
\begin{aligned}
\frac{d\widetilde\psi}{d\varphi}
&=H_0^{-1},\\
\frac{d\varphi}{d\widetilde\psi}
&=H_0.
\end{aligned}
\tag{OD.18}
\]

For \(y\in M'\), equations (OD.9), (OD.18), and the two spatial modular actions give

\[
\begin{aligned}
\sigma_t^{\widetilde\psi}(y)
&=H_0^{-it}yH_0^{it}\\
&=\sigma_t^\psi(y).
\end{aligned}
\tag{OD.19}
\]

The pair \((\psi,\widetilde\psi)\) is therefore modularly compatible for the inclusion \(M'\subseteq N'\). The compatible-pair reconstruction, at its explicitly stated conditional boundary, supplies a unique

\[
\begin{aligned}
T'&\in\mathcal W_0(N',M'),\\
\widetilde\psi&=\psi\circ T'.
\end{aligned}
\tag{OD.20}
\]

Equations (OD.9), (OD.18), and (OD.20) prove (OD.4) for the references chosen in (OD.8).

## Removing both reference choices

The operator-valued weight \(T'\) just constructed does not depend on \(\omega\), \(\varphi\), or \(\psi\). It is enough to prove that (OD.4) holds for every pair of scalar references; uniqueness in (OD.20), or uniqueness from one scalar composite, then removes every construction choice.

First keep \(\psi\) fixed and replace \(\varphi\) by \(\alpha\in\mathcal W_0(N)\). Write

\[
\begin{aligned}
H_\gamma&=\frac{d(\gamma\circ T)}{d\psi},\\
A_\gamma&=\frac{d\gamma}{d(\psi\circ T')},\\
&\hspace{-2em}(\gamma=\varphi,\alpha).
\end{aligned}
\tag{OD.21}
\]

The spatial cocycle formula and the scalar-cocycle preservation of Lifting scalar modular flows and cocycles give the following chain, with \(\Phi_\gamma=\gamma\circ T\):

\[
\begin{aligned}
H_\alpha^{it}H_\varphi^{-it}
&=[D\Phi_\alpha:D\Phi_\varphi]_t\\
&=[D\alpha:D\varphi]_t\\
&=A_\alpha^{it}A_\varphi^{-it}.
\end{aligned}
\tag{OD.22}
\]

The chosen-reference case says \(H_\varphi=A_\varphi\). Cancelling their imaginary powers in the displayed order yields \(H_\alpha^{it}=A_\alpha^{it}\) for every \(t\), and hence \(H_\alpha=A_\alpha\).

Now fix \(\alpha\) and replace \(\psi\) by \(\beta\in\mathcal W_0(M')\). Put

\[
\begin{aligned}
H_\eta&=\frac{d(\alpha\circ T)}{d\eta},\\
A_\eta&=\frac{d\alpha}{d(\eta\circ T')},\\
&\hspace{-2em}(\eta=\psi,\beta).
\end{aligned}
\tag{OD.23}
\]

Reciprocity and the spatial cocycle formula, now on \(M'\) and \(N'\), give the following identities, where \(\Psi_\eta=\eta\circ T'\):

\[
\begin{aligned}
[D\beta:D\psi]_t
&=H_\beta^{-it}H_\psi^{it},\\
[D\Psi_\beta:D\Psi_\psi]_t
&=A_\beta^{-it}A_\psi^{it}.
\end{aligned}
\tag{OD.24}
\]

OM-01 applied to \(T'\) says the two left sides agree. The first part of the argument gives \(H_\psi=A_\psi\), so cancellation yields \(H_\beta^{-it}=A_\beta^{-it}\) for every \(t\). Thus \(H_\beta=A_\beta\), proving (OD.4) for all \(\alpha,\beta\).

This calculation also records exactly where the conditional public dependencies enter: the spatial identities come from SI, cocycle reconstruction from CX, compatible-pair reconstruction from OE, and scalar-cocycle preservation from OM through OR. No standard-form identification, separability assumption, or choice of a state is hidden in the reference change.

## Dualizing twice and reversing modular time

Apply the same construction to \(T'\in\mathcal W_0(N',M')\), and call its dual \(T''\in\mathcal W_0(M,N)\). Its spatial identity is

\[
\frac{d\psi}{d(\varphi\circ T'')}
=
\frac{d(\psi\circ T')}{d\varphi}.
\tag{OD.25}
\]

Write \(H_0=d(\varphi\circ T)/d\psi=d\varphi/d(\psi\circ T')\). Reciprocity and (OD.4) turn the right side into

\[
\begin{aligned}
\frac{d(\psi\circ T')}{d\varphi}
&=H_0^{-1}\\
&=\frac{d\psi}{d(\varphi\circ T)}.
\end{aligned}
\tag{OD.26}
\]

Reciprocating (OD.25–26) gives equal spatial derivatives of \(\varphi\circ T''\) and \(\varphi\circ T\) relative to the fixed denominator \(\psi\). Injectivity of the spatial construction gives

\[
\varphi\circ T''=\varphi\circ T.
\tag{OD.27}
\]

OR-02 then yields \(T''=T\). Thus dualization is involutive, which proves both injectivity and surjectivity in (OD.5).

For modular time, fix \(\varphi,\psi\) and denote the common operator in (OD.4) by \(H_0\). If \(x\in N^c\), then the intrinsic definitions and the two sides of the spatial action theorem give

\[
\begin{aligned}
\sigma_t^T(x)
&=H_0^{it}xH_0^{-it},\\
\sigma_{-t}^{T'}(x)
&=H_0^{it}xH_0^{-it}.
\end{aligned}
\tag{OD.28}
\]

This proves (OD.6) on the entire common relative commutant.

## The cocycle order and a two-dimensional check

Let \(T_1,T_2\in\mathcal W_0(M,N)\), and use the same \(\varphi,\psi\) for both. For \(j=1,2\), set

\[
\begin{aligned}
H_j
&=\frac{d(\varphi\circ T_j)}{d\psi}\\
&=\frac{d\varphi}{d(\psi\circ T_j')}.
\end{aligned}
\tag{OD.29}
\]

The definition of the intrinsic operator-valued cocycle and the spatial cocycle formula give

\[
(DT_1:DT_2)_t=H_1^{it}H_2^{-it}.
\tag{OD.30}
\]

Reciprocity says

\[
\frac{d(\psi\circ T_j')}{d\varphi}=H_j^{-1}.
\tag{OD.31}
\]

Therefore

\[
\begin{aligned}
&(DT_1':DT_2')_{-t}\\
&\quad=(H_1^{-1})^{-it}(H_2^{-1})^{it}\\
&=H_1^{it}H_2^{-it}\\
&=(DT_1:DT_2)_t,
\end{aligned}
\tag{OD.32}
\]

which proves the same-index formula (OD.7).

There is a small matrix test that distinguishes (OD.7) from the swapped-index formula in the printed source. Take

\[
\begin{aligned}
\mathbb C1&\subset M_2(\mathbb C),\\
\rho_1&=\begin{pmatrix}2&0\\0&1\end{pmatrix},\\
\rho_2&=I,
\end{aligned}
\tag{OD.33}
\]

and let \(\varphi_j(x)=\operatorname{Tr}(\rho_jx)\). Under commutant duality, the dual scalar weights have densities \(\rho_j^{-1}\). Hence

\[
\begin{aligned}
&(D\varphi_1:D\varphi_2)_t\\
&\quad=\begin{pmatrix}2^{it}&0\\0&1\end{pmatrix}.
\end{aligned}
\tag{OD.34}
\]

The same-index dual expression at time \(-t\) gives the same matrix. The printed swapped-index expression gives

\[
\begin{pmatrix}2^{-it}&0\\0&1\end{pmatrix},
\tag{OD.35}
\]

which differs for generic \(t\). This is a mathematical correction, not a change of cocycle convention: the convention is fixed by the balanced-matrix formula used throughout SI and OM.

## Scalar weights and the type-I trace formula

Set \(N=\mathbb C1\) in (OD.1). A member \(\varphi\in\mathcal W_0(M)\) is then a faithful normal semifinite operator-valued weight \(M\to\mathbb C1\). Its dual is

\[
T_\varphi\in\mathcal W_0(B(H),M').
\tag{OD.36}
\]

The involution above gives a bijection from \(\mathcal W_0(M)\) onto \(\mathcal W_0(B(H),M')\). Its forward map is

\[
\varphi\longmapsto T_\varphi.
\tag{OD.37}
\]

Equations (OD.6–7) specialize to

\[
\begin{aligned}
\sigma_t^\varphi
&=\sigma_{-t}^{T_\varphi},\\
&(D\varphi:D\chi)_t\\
&\qquad=(DT_\varphi:DT_\chi)_{-t}.
\end{aligned}
\tag{OD.38}
\]

Let \(\epsilon(\lambda1)=\lambda\) be the canonical scalar weight on \(\mathbb C1\), and fix \(\psi\in\mathcal W_0(M')\). Equation (OD.4) and reciprocity give

\[
\frac{d(\psi\circ T_\varphi)}{d\epsilon}
=\frac{d\psi}{d\varphi}
=:h.
\tag{OD.39}
\]

The operator \(h\) is positive, injective, self-adjoint, and affiliated with \(B(H)\). Let \(\operatorname{Tr}\) be the canonical trace on \(B(H)\), and use the affiliated-density construction to define

\[
\begin{aligned}
\operatorname{Tr}_h(x)
&=\operatorname{Tr}(h^{1/2}xh^{1/2}),\\
&\hspace{-2em}x\in B(H)_+,
\end{aligned}
\tag{OD.40}
\]

with the value understood by increasing bounded regularization when necessary.

For completeness, its spatial derivative relative to \(\epsilon\) is exactly \(h\). Every vector \(\xi\in H\) is \(\epsilon\)-bounded, and its coefficient is the rank-one operator \(|\xi\rangle\langle\xi|\). Therefore the initial spatial energy is

\[
\operatorname{Tr}_h(|\xi\rangle\langle\xi|)
=\|h^{1/2}\xi\|^2,
\tag{OD.41}
\]

finite exactly on \(D(h^{1/2})\). This is the closed quadratic form represented by \(h\), so closed-form representation and spatial injectivity identify the weight in (OD.39):

\[
\boxed{
\psi\circ T_\varphi
=\operatorname{Tr}_{\,d\psi/d\varphi}.}
\tag{OD.42}
\]

The source antecedents are Takesaki II IX.4.24–25, printed pp. 232–233 / PDF pp. 252–253. The construction above remains conditional on the explicitly open providers inherited from OE, OR, OM, CX, SI, CZ, SC, and WH. It is an original proof relative to those providers.
