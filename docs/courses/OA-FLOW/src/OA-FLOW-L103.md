# Faithful ergodic actions of the circle

A point-ultraweakly continuous circle action with scalar fixed algebra has one-dimensional nonzero spectral fibers. If the action is faithful, one degree-one unitary generates the algebra, and the entire system is circle translation on \(L^\infty(\mathbb T)\). We construct the normal isomorphism on the whole algebra, including its measure class.

*Original expression: CC0-1.0 to the extent of rights held.*

<a id="oa-flow.ergcircle.fejer"></a>

## Recovering an element from its spectral fibers

Let \(M\ne0\) be a von Neumann algebra and let
\(\alpha:\mathbb T\to\operatorname{Aut}(M)\) be point-ultraweakly continuous. Define
\[
 M_n=\{x:\alpha_t(x)=e^{2\pi int}x\text{ for all }t\},\qquad
 P_nx=\int_{\mathbb T}e^{-2\pi int}\alpha_t(x)\,dt.
 \tag{E1}
\]
[AT5](OA-FLOW-AT.md#oa-flow.at.5) constructs these normal contractions. Substitution in the scalar integral gives
\(\alpha_sP_n=e^{2\pi ins}P_n\), while integration of a character shows \(P_nx=x\) for \(x\in M_n\) and \(P_nx=0\) for \(x\in M_k\), \(k\ne n\).

With \(F_N\) as in [CC0](OA-FLOW-CC.md#oa-flow.cc.0), set
\[
 Q_Nx=\int_{\mathbb T}F_N(t)\alpha_t(x)\,dt
 =\sum_{|n|<N}\left(1-\frac{|n|}{N}\right)P_nx.
 \tag{E2}
\]
Positivity and mass one give \(\|Q_Nx\|\leq\|x\|\). For any normal functional \(\omega\), the function \(h(t)=\omega(\alpha_t(x)-x)\) is continuous and vanishes at zero. Split \(\int F_Nh\) into a small neighborhood of zero and its complement. The first contribution is bounded by the supremum of \(|h|\) on that neighborhood; the second tends to zero by concentration of the Fejér kernels. Therefore
\[
 Q_Nx\longrightarrow x\quad\hbox{ultraweakly}.
 \tag{E3}
\]
In particular the spectral fibers span an ultraweakly dense subspace of \(M\). This statement uses bounded averages, not convergence of ordinary Fourier partial sums.

<a id="oa-flow.ergcircle.degrees"></a>

## Scalar fixed points force unitary fibers

Assume now \(M^\alpha=\mathbb C1\). If \(0\ne x\in M_n\), both \(x^*x\) and \(xx^*\) belong to \(M^\alpha\). The C*-identity implies that their scalar values are \(\|x\|^2\). Hence \(v=x/\|x\|\) satisfies \(v^*v=vv^*=1\). If \(y\in M_n\), then \(v^*y\in M^\alpha\), and \(y=v(v^*y)\). Thus
\[
 M_n\ne0\quad\Longrightarrow\quad M_n=\mathbb Cv_n
 \quad\hbox{for a unitary }v_n.
 \tag{E4}
\]
Products and adjoints of eigenvectors have degrees \(n+m\) and \(-n\). Products of the unitary choices are nonzero, so
\[
 J=\{n:M_n\ne0\}
 \tag{E5}
\]
is a subgroup of \(\mathbb Z\). If \(J\ne\{0\}\), its positive part has a least element \(d\). Division with remainder shows every \(n\in J\) is a multiple of \(d\), since its remainder is in \(J\) and lies between zero and \(d-1\). Hence \(J=d\mathbb Z\); we use \(d=0\) for the subgroup \(\{0\}\).

The action's kernel is exactly
\[
 \ker\alpha=\{t:e^{2\pi int}=1\text{ for every }n\in J\}.
 \tag{E6}
\]
One inclusion follows by testing a nonzero vector in each fiber. Conversely, if those phases are all one, \(\alpha_t\) fixes every \(Q_Nx\); normality and (E3) imply that it fixes every \(x\). For \(d\geq1\), (E6) is \(\{j/d:0\leq j<d\}\) modulo one. For \(d=0\), it is all of \(\mathbb T\), and (E3) also gives \(M=\mathbb C1\). Therefore a faithful action necessarily has \(d=1\).

Choose a unitary \(u\in M_1\). Its integer powers are nonzero and have the corresponding degrees, including negative degrees via adjoints. Equation (E4) gives
\[
 M_n=\mathbb Cu^n,\qquad M=W^*(u).
 \tag{E7}
\]
The last equality follows from (E2)–(E3); the right side is ultraweakly closed and contains every approximant. In particular \(M\) is abelian: the polynomials in the unitary \(u\) and its adjoint commute, and applying separate ultraweak continuity of multiplication first in one variable and then the other extends this identity to their ultraweak closure. Separate continuity follows by moving a fixed factor onto a vector in the normal vector-series tests of CP4. No choice of compatible phases in all the fibers is needed: choosing \(u\) fixes them by its powers.

<a id="oa-flow.ergcircle.model"></a>

## The normal isomorphism and Haar measure

Continue under the faithfulness assumption. Averaging gives a normal positive unital map
\[
 E(x)=\int_{\mathbb T}\alpha_t(x)\,dt=\varphi(x)1.
 \tag{E8}
\]
Its range is the fixed algebra, by Haar invariance; composing it with any normal state on \(M\) proves that the scalar \(\varphi\) is a normal state. A normal state exists by restricting a unit vector functional in any nonzero concrete representation. Haar substitution also proves \(\varphi\circ\alpha_t=\varphi\).

This state is faithful. If \(x\geq0\) and \(\varphi(x)=0\), then for every positive normal vector functional \(\omega\), the nonnegative continuous function \(\omega(\alpha_t(x))\) has integral zero. Such a function is identically zero: positivity at a point gives positivity on a nonempty open neighborhood, which has positive Haar measure by CC0. Evaluating at zero gives \(\omega(x)=0\) for every such \(\omega\), hence \(x=0\) by the concrete positivity criterion of [CF8](OA-FLOW-CF.md#oa-flow.cf.8). Invariance and a nontrivial phase yield
\[
 \varphi(u^k)=0\ (k\ne0),\qquad \varphi(1)=1.
 \tag{E9}
\]

Use [GW3](OA-FLOW-GW.md#oa-flow.gw.3) to form the GNS representation \(\pi\), with \(\Omega=\Lambda(1)\). It is faithful: \(\pi(x)=0\) implies \(\Lambda(x)=0\), so \(\varphi(x^*x)=0\), hence \(x=0\). It is normal by [NF5](OA-FLOW-NF.md#oa-flow.nf.5), and [ST2](OA-FLOW-ST12.md#oa-flow.st.2) proves that its image is a von Neumann algebra and its inverse on that image is normal.

The vectors \(\Lambda(u^n)\) are orthonormal by (E9). They are complete. If \(\eta\) is perpendicular to all of them, the normal functional
\(x\mapsto\langle\pi(x)\Omega,\eta\rangle\) vanishes on every trigonometric polynomial in \(u\), hence on \(M\) by (E2)–(E3). It therefore vanishes on the dense subspace \(\Lambda(M)\), so \(\eta=0\).

CC0 supplies the complete orthonormal basis \(z^n(s)=e^{2\pi ins}\) of \(L^2(\mathbb T)\). There is consequently a unitary
\[
 W:H_\varphi\longrightarrow L^2(\mathbb T),\qquad
 W\Lambda(u^n)=z^n,\qquad W\Omega=1.
 \tag{E10}
\]
Checking on this basis gives \(W\pi(u)W^*=M_z\). Equation (E7), normality of \(\pi\), and (E3) give
\[
 W\pi(M)W^*=W^*(M_z)
          =\{M_f:f\in L^\infty(\mathbb T)\}.
 \tag{E11}
\]
The last equality is proved in [the multiplication-algebra argument](OA-FLOW-L102.md#oa-flow.circle.multipliers); it includes surjectivity, not only an embedding of continuous functions.

Define
\[
 \Theta(f)=\pi^{-1}(W^*M_fW).
 \tag{E12}
\]
The multiplication representation and its inverse are normal by the \(L^1\) coefficient calculation in L102. Thus \(\Theta\) is a normal unital *-isomorphism, with normal inverse, and \(\Theta(z)=u\). Moreover
\[
 \varphi(\Theta(f))=\langle M_f1,1\rangle
                  =\int_{\mathbb T}f(s)\,ds.
 \tag{E13}
\]
This identifies the measure class as Haar measure: in particular \(\Theta(1_A)=0\) exactly when \(A\) is Haar null. It also specifies the bounded measurable functional calculus of \(u\) on the whole \(L^\infty\) space.

Let \((\beta_t f)(s)=f(s+t)\). Both maps \(\alpha_t\Theta\) and \(\Theta\beta_t\) are normal and agree on every \(z^n\), since both give \(e^{2\pi int}u^n\). The bounded ultraweak density proved in L102 therefore yields
\[
 \alpha_t\Theta(f)=\Theta(\beta_t f)
 \quad(f\in L^\infty(\mathbb T),\ t\in\mathbb T).
 \tag{E14}
\]
This is the required conjugacy of the complete systems. Replacing \(u\) by \(e^{2\pi ia}u\) replaces \(\Theta\) by \(\Theta\beta_a\).

<a id="oa-flow.ergcircle.nonfaithful"></a>

## Why the kernel assumption is necessary

For an integer \(d\geq1\), let
\[
 (\gamma_t f)(s)=f(s+dt)
 \quad\hbox{on }L^\infty(\mathbb T).
 \tag{E15}
\]
As \(dt\) ranges over the circle, the fixed algebra remains the scalars, by L102. Each \(z^k\) has degree \(dk\). If \(\gamma_t f=e^{2\pi int}f\), Fourier covariance gives \(\widehat f(k)=0\) unless \(dk=n\); completeness then gives
\[
 M_n^\gamma=
 \begin{cases}\mathbb Cz^{n/d},&d\mid n,\\
 \{0\},&d\nmid n.\end{cases}
 \tag{E16}
\]
Its kernel is exactly the \(d\)-th roots of zero modulo one, as can be tested on \(z\). For \(d>1\) the action is ergodic and has no degree-one unitary. Thus faithfulness is the exact hypothesis used to pass from a subgroup of frequencies to every integer frequency.

The translation system in part (f) of the source exercise is the preceding Exercise XI.1.2; its printed reference to Problem 1 does not identify that model.

The classification addressed here is Takesaki, *Theory of Operator Algebras II*, Exercise XI.1.3, p.330.
