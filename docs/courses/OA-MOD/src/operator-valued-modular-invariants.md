# Modular invariants of operator-valued weights

An operator-valued weight has modular data that lives on the relative commutant and does not depend on the scalar weight used to expose it. The mechanism is exact: scalar modular flows lift through the operator-valued weight, and a cocycle comparing two such weights commutes with the target algebra. Throughout, \(N\subseteq M\) is a unital inclusion of arbitrary von Neumann algebras and

\[
N^c=N'\cap M.
\tag{OM.1}
\]

## Lifting scalar modular flows and cocycles

Let \(T\in\mathcal W_0(M,N)\) be a faithful normal semifinite operator-valued weight. For \(\varphi,\psi\in\mathcal W_0(N)\), set

\[
\Phi=\widehat\varphi\circ T,
\qquad
\Psi=\widehat\psi\circ T.
\tag{OM.2}
\]

The composition theorem makes \(\Phi\) and \(\Psi\) faithful normal semifinite weights on \(M\). The forward modular graph transfer, relative to its three stated component contracts, gives

\[
\sigma_t^\Phi(n)=\sigma_t^\varphi(n).
\tag{OM.3}
\]

Here \(n\in N\) and \(t\in\mathbb R\). It also gives the stronger cocycle identity

\[
[D\Psi:D\Phi]_t=[D\psi:D\varphi]_t.
\tag{OM.4}
\]

The common value belongs to \(N\).

The cocycle order matters: the numerator \(\Psi\) corresponds to \(\psi\), and the denominator \(\Phi\) to \(\varphi\). Equation (OM.4) follows by evaluating the equality of the two mixed isometric groups at \(1\); it is not inferred merely from (OM.3). This proves clauses (i) and (ii) of Takesaki II IX.4.22 at the same conditional public-proof boundary as OR-03.

## Comparing two operator-valued weights

Let \(S,T\in\mathcal W_0(M,N)\), fix \(\varphi\in\mathcal W_0(N)\), and abbreviate

\[
\begin{aligned}
\Phi_T&=\widehat\varphi\circ T,\\
\Phi_S&=\widehat\varphi\circ S,\\
u_t&=[D\Phi_T:D\Phi_S]_t.
\end{aligned}
\tag{OM.5}
\]

Thus \(u_t\in M\).
The ordinary modular implementation formula says

\[
\sigma_t^{\Phi_T}
=\operatorname{Ad}(u_t)\circ
 \sigma_t^{\Phi_S}.
\tag{OM.6}
\]

Apply this identity to \(n\in N\). By (OM.3), both sides restrict to \(\sigma_t^\varphi(n)\), so

\[
u_t\,\sigma_t^\varphi(n)\,u_t^*
=\sigma_t^\varphi(n).
\tag{OM.7}
\]

Because \(\sigma_t^\varphi(N)=N\), equation (OM.7) gives \(u_t\in N'\). The scalar cocycle already lies in \(M\), hence

\[
u_t\in N'\cap M=N^c.
\tag{OM.8}
\]

This proves the membership assertion of IX.4.22(iii) without a matrix amplification. It uses the full faithfulness assumptions: they make every cocycle above a whole-algebra unitary.

The same argument also shows that \(N^c\) is globally invariant under every \(\sigma_t^{\widehat\varphi\circ T}\). Indeed, (OM.3) maps \(N\) onto itself, and an automorphism preserving \(N\) preserves \(N'\cap M\).

## Independence of the scalar reference

Choose another \(\psi\in\mathcal W_0(N)\), and put
\(\Psi_T=\widehat\psi\circ T\) and
\(\Psi_S=\widehat\psi\circ S\).
Use (OM.4) separately for \(T\) and \(S\), and abbreviate

\[
\begin{aligned}
a_t&:=[D\Psi_T:D\Phi_T]_t,\\
a_t&=[D\psi:D\varphi]_t,\\
b_t&:=[D\Phi_S:D\Psi_S]_t,\\
b_t&=[D\varphi:D\psi]_t.
\end{aligned}
\tag{OM.9}
\]

Apply the ordered cocycle chain rule twice, inserting the two \(\varphi\)-composites between the \(\psi\)-composites:

\[
[D\Psi_T:D\Psi_S]_t=a_tu_tb_t.
\tag{OM.10}
\]

The first and last factors lie in \(N\), while \(u_t\in N^c\). They therefore commute with \(u_t\). The reverse-cocycle identity cancels the outer factors in their displayed order, and (OM.9) becomes

\[
[D\Psi_T:D\Psi_S]_t=u_t.
\tag{OM.11}
\]

Thus the cocycle comparing \(T\) and \(S\) is independent of the faithful scalar reference. No two arbitrary cocycles were commuted; only the relative-commutant element \(u_t\) was moved past elements of \(N\).

The modular restriction is reference-independent as well. From (OM.4) and modular implementation,

\[
\begin{aligned}
\sigma_t^{\Psi_T}
&=\operatorname{Ad}(a_t)\\
&\quad{}\circ\sigma_t^{\Phi_T}.
\end{aligned}
\tag{OM.12}
\]

For \(x\in N^c\), the first factor belongs to \(N\) and commutes with \(\sigma_t^{\widehat\varphi\circ T}(x)\in N^c\). Hence the two modular actions agree on \(N^c\).

For \(T_j\), write
\(\Phi_{T_j}=\widehat\varphi\circ T_j\), and abbreviate
\(\delta_{12}(t)=(DT_1:DT_2)_t\). We may therefore make the intrinsic definitions

\[
\sigma_t^T
 :=\left.\sigma_t^{\Phi_T}\right|_{N^c}.
\tag{OM.13a}
\]

\[
\begin{aligned}
\delta_{12}(t)
&:=[D\Phi_{T_1}:\\
&\qquad D\Phi_{T_2}]_t.
\end{aligned}
\tag{OM.13b}
\]

The first is the modular automorphism group of \(T\) on \(N^c\); the second is the cocycle derivative of \(T_1\) relative to \(T_2\), an element of \(N^c\). The scalar reference in (OM.13) is any member of \(\mathcal W_0(N)\). In the printed first clause of IX.4.23 the base algebra appears as \(M\), but the displayed composite, the second clause, and IX.4.22 require a weight on \(N\); (OM.13) records the type-correct quantifier.

## Intrinsic laws and the exact boundary

All ordinary faithful cocycle identities descend to the relative commutant. If \(T_1,T_2,T_3\in\mathcal W_0(M,N)\), write
\(\delta_{ij}(t)=(DT_i:DT_j)_t\). Then

\[
\delta_{31}(t)=\delta_{32}(t)\delta_{21}(t).
\tag{OM.14a}
\]

\[
\delta_{12}(t)^*=\delta_{21}(t).
\tag{OM.14b}
\]

\[
\begin{aligned}
\sigma_t^{T_1}
&=\operatorname{Ad}(\delta_{12}(t))\\
&\quad{}\circ\sigma_t^{T_2}.
\end{aligned}
\tag{OM.14c}
\]

Writing \(v_t=(DT_1:DT_2)_t\), its cocycle law is

\[
v_{s+t}=v_s\,\sigma_s^{T_2}(v_t).
\tag{OM.15}
\]

Here \(s,t\in\mathbb R\).
These formulas are obtained by fixing one faithful \(\varphi\in\mathcal W_0(N)\), applying the usual scalar identities to \(\widehat\varphi\circ T_j\), and then using (OM.13). They introduce no additional source assumption.

The human antecedents are Takesaki II IX.4.22–23, printed pp. 230–232 / PDF pp. 250–252. This proof is conditional on OR-03's mixed-graph, finite-matrix and analytic-generator contracts and on the provider closure of the faithful ordered chain rule. The adjacent commutant-duality bijection IX.4.24 and the scalar-weight/\(B(H)\) correspondence IX.4.25 require separate construction and proof. The stated dependencies are not proved here.
