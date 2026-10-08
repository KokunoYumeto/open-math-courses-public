# Escaping Lagrangians on regular energy surfaces

*Written by GPT-6.1 Sol (OpenAI) and GPT-6 Astra (OpenAI). Self-checked by the writing AI. Original exposition: CC0.*

**Working question: Can an escaping energy family have a single-valued action on a shell with loops?** Local closed one-forms need not be exact on a space with loops. The normalized Hamilton construction provides a global action rather than appealing to local primitives. The family must also be an actual embedded Lagrangian, because a phase description is not useful if different rays project to the same undesired data.

A fixed energy selects the frequencies of a free particle. Its outgoing rays form a normal bundle of that energy surface. We construct the corresponding escaping family for a long-range force, prove that it is embedded, and find a globally normalized action. The action remains single-valued even when the energy surface has loops.

Read [Hamilton trajectories under a long-range force](hamilton-trajectories-under-a-long-range-force.md), including its spatial and mixed time estimates and its local contraction and continuation proofs. The [written coordinate inverse proof, (CI1)–(CI3)](../providers/analysis/coordinate-inverses-and-integration.md#coordinate-inverse) supplies the local inverses and smooth level-set charts; the [finite bump construction](../providers/analysis/coordinate-inverses-and-integration.md#finite-partitions) supplies compact cutoffs. Section 3 below proves the cotangent form convention, Hamilton preservation of the symplectic form and the isotropic dimension criterion for this Lagrangian flowout directly.

The free texts of Teschl [T] and Oh [O] provide background on characteristic flows.

## 1. The free geometry and the initial sheet

Let \(P_0\) be a real polynomial with \(|P_0(\xi)|\to\infty\) as \(|\xi|\to\infty\), and let \(\lambda\) be a regular value. Write

\[
\begin{gathered}
M_\lambda=\{\xi:P_0(\xi)=\lambda\},\\
 v(\xi)=\nabla P_0(\xi),\\ H=P_0+V_L.
\end{gathered}
\tag{1}
\]

The free shell \(M_\lambda\) is compact. The long-range term \(V_L\) is real and smooth, and is a polynomial of any finite order in \(\xi\). Fix an integer \(\kappa\ge2\), \(0<\delta<1/(\kappa+1)\), and assume, on each compact frequency set \(K\),

\[
\begin{gathered}
 |\partial_\xi^\alpha\partial_x^\beta V_L(x,\xi)|
       \le C_{\alpha\beta,K}(1+|x|^2)^{-m(|\beta|)/2},\\
 m(j)=j+\delta\quad(0\le j\le\kappa),\\
 m(j)=1+(\kappa-1+\delta)j/\kappa\quad(j\ge\kappa).
 \end{gathered}
\tag{2}
\]

The formulas agree at \(j=\kappa\). We use \(x'=H_\xi\), \(\xi'=-H_x\), and the frequency-base cotangent form
\(\beta=\sum_jx_j\,d\xi_j\). All derivative estimates use ordinary real derivatives.


For \(V_L=0\), the outgoing family is

\[
\mathcal N_+(M_\lambda)
      =\{(t\,v(\xi),\xi):t>0,\ \xi\in M_\lambda\}.
\tag{3}
\]

Its restriction of \(\beta\) is zero: on tangent directions to the shell it is
\(t\,dP_0=0\), and the frequency is constant along a ray. For
\(P_0(\xi)=|\xi|^2\), \(\lambda>0\), these are the outward normal rays of the sphere of radius \(\sqrt\lambda\).

For the perturbed energy equation, start far along the free graph. It matters which frequency sheet is selected. Choose a small regular energy collar
\(U=\{|P_0-\lambda|<\varepsilon\}\), and define

\[
\begin{gathered}
 M_T=\{\eta\in U:H(Tv(\eta),\eta)=\lambda\},\\
 \Sigma_T=\{(Tv(\eta),\eta):\eta\in M_T\}.
 \end{gathered}
\tag{4}
\]

Only this near-shell sheet is used below. Here is why that restriction is needed.
Take \(n\ge2\), \(P_0=|\xi|^2\), \(\lambda=1\), and a real smooth compactly supported
\(\chi\) that equals one on \(|x|\le1\), vanishes on \(|x|\ge2\), and satisfies \(0\le\chi\le1\). Set \(V_L=\chi(x)\). In \(|\xi|<1/(2T)\), the unrestricted energy equation becomes

\[
|\xi|^2+\chi(2T\xi)-1=|\xi|^2=0.
\tag{5}
\]

Thus its full frequency set has an isolated point at zero. Its sheet near the unit sphere is exactly the sphere for large \(T\). The isolated point starts the stationary Hamilton orbit \((0,0)\). An energy-one orbit in \(|x|\le1\) has \(\xi=0\) and is stationary, so ODE uniqueness prevents other initial orbits from entering that region. The unrestricted flowout has an isolated point and cannot be an \(n\)-dimensional Lagrangian. All decay assumptions hold for this smooth compactly supported potential.

The counterexample shows why an unrestricted initial set is insufficient. The regular-collar construction below retains the required restriction.

<a id="escaping-theorem"></a>

The initial-sheet estimate is Hörmander [H4, Lemma 30.3.4]. The flowout and normalized action correspond to [H4, Theorems 30.3.5–30.3.6], with the initial set restricted to the regular collar as required by the counterexample above.

**Theorem 1.1 (an escaping energy family and its action).** For all sufficiently large \(T\), \(M_T\) is a compact smooth hypersurface diffeomorphic to \(M_\lambda\). Its Hamilton flow exists for every \(t\ge T\), has energy \(\lambda\), and satisfies

\[
\begin{gathered}
\xi(t)-\eta=O(T^{-\delta}),\\
 x(t)=t\bigl(v(\xi(t))+z(t)\bigr),\\
 z(t)=O(t^{-\delta}),\\ c\,t\le|x(t)|\le C\,t.
\end{gathered}
\tag{6}
\]

The constants are uniform over the initial sheet. All future frequencies lie in any prescribed neighborhood of \(M_\lambda\) if \(T\) is sufficiently large. The open future union \(\Lambda_T^+\), with \(t>T\), is an embedded Lagrangian. It has a unique real smooth action \(\psi\), smooth up to its initial boundary, with

\[
d\psi=\beta|_{\Lambda_T^+},\qquad
 \psi(T,\eta)=-T V_L(Tv(\eta),\eta).
\tag{7}
\]

In a fixed chart where \(M_\lambda\) is \(\xi_1=E(\xi')\), the perturbed sheet is \(\xi_1=E_T(\xi')\), and every multiindex satisfies

\[
|\partial_{\xi'}^\alpha(E_T-E)|
       \le C_\alpha T^{|\alpha|-m(|\alpha|)}.
\tag{8}
\]

There is an analogous negative-normal construction. If \(M_\lambda\) is empty, the near-shell sheet and its flowout are empty. The proof is given in Sections 2–5.

<a id="escaping-normal-collar"></a>

## 2. A collar built by the normal flow

If \(M_\lambda\) is empty, the sheet in a sufficiently small compact regular energy band is empty and its flowout is empty. All local chart assertions are vacuous. Assume now \(M_\lambda\ne\varnothing\).

Polynomial properness makes every bounded energy band compact. Since \(\lambda\) is regular, choose \(\varepsilon>0\) so small that
\(\{|P_0-\lambda|\le2\varepsilon\}\) has no critical point.
To justify one such choice, a sequence of critical points with values tending to \(\lambda\) would be confined to a compact band; its convergent subsequence would give a critical point of value \(\lambda\), a contradiction.
There is therefore a uniform positive lower bound for \(|\nabla P_0|\) on this band.

Use the smooth normal field
\[
\nu(\xi)=\frac{\nabla P_0(\xi)}{|\nabla P_0(\xi)|^2}.
\tag{9}
\]
Its flow \(N(u,s)\), starting at \(u\in M_\lambda\), obeys
\(P_0(N(u,s))=\lambda+s\).
The [local existence and smooth dependence proof](hamilton-trajectories-under-a-long-range-force.md#hamilton-local-flow-and-data-derivatives) applies to this smooth field on the noncritical band. Its [compact continuation argument](hamilton-trajectories-under-a-long-range-force.md#hamilton-global-continuation), while the level stays in that band, gives the flow for \(|s|<\varepsilon\).
The map
\[
N:M_\lambda\times(-\varepsilon,\varepsilon)
        \longrightarrow \{|P_0-\lambda|<\varepsilon\}
\tag{10}
\]
is a diffeomorphism. For injectivity, equal image points have equal \(s\) from their energy values; reversing the normal flow recovers the same \(u\).
For surjectivity, start at a point of the energy band and run the field backward for time \(P_0(\xi)-\lambda\); the energy reaches \(\lambda\) and the entire trajectory stays in the compact noncritical band.
This also gives the smooth inverse explicitly.

<a id="escaping-initial-sheet"></a>

On the compact smaller collar, write the perturbed equation as
\[
\begin{gathered}
s+R_T(u,s)=0,\\
 R_T(u,s)=V_L(T\nabla P_0(N(u,s)),N(u,s)).
\end{gathered}
\tag{11}
\]
Each derivative of \(R_T\) of order zero or one is a finite sum with at most one factor \(T\) and one position derivative of \(V_L\). Since \(|Tv|\) is comparable with \(T\), the stated decay bounds give
\(\|R_T\|_{C^1}=O(T^{-\delta})\).
For large \(T\), the map \(s\mapsto-R_T(u,s)\) is a uniform contraction of
\([-\varepsilon/2,\varepsilon/2]\) into itself.
It has a unique smooth root \(s_T(u)\), with \(|s_T|\le CT^{-\delta}\).
Every zero in the open collar has that small \(s\), since its equation itself gives \(|s|\le CT^{-\delta}\); there are no additional zeros within the collar.
Thus
\[
\begin{aligned}
M_T&=\{\xi:H(Tv(\xi),\xi)=\lambda\}\\
   &\cap\{|P_0-\lambda|<\varepsilon\}\\
   &=\{N(u,s_T(u)):u\in M_\lambda\}
\end{aligned}
\tag{12}
\]
is one smooth compact hypersurface, diffeomorphic to \(M_\lambda\).
Section 5 proves every graph derivative estimate on the finite compact chart covering.
This constructs the complete sheet in the regular collar.

<a id="escaping-future-flow"></a>

## 3. Escape makes the flowout embedded

Start only from
\[
\Sigma_T
   =\{(T\nabla P_0(\eta),\eta):
                    \eta\in M_T\}.
\tag{13}
\]
To apply the [uniform spatial flow theorem](hamilton-trajectories-under-a-long-range-force.md#hamilton-uniform-future-flow), choose a relatively compact open frequency neighborhood \(W\) of the smaller regular energy band. Shrink it so that \(|v|\ge c>0\) on its closure. The product tube \(\{|z|<c/2\}\times W\) is preserved by contractions of its first coordinate and satisfies \(|z+v(\xi)|\ge c/2\). All sufficiently large initial sheets lie in a fixed compact subset of \(W\), with initial displacement \(z=0\). These are precisely the theorem’s tube and compact-data hypotheses. It gives a smooth future solution for all \(t\ge T\). The frequency changes by \(O(T^{-\delta})\) and
\(z=O(t^{-\delta})\), since the initial displacement is zero.
The initial sheet is \(O(T^{-\delta})\) from \(M_\lambda\).
Hence all future frequencies stay within any given fixed neighborhood of \(M_\lambda\), once \(T\) is sufficiently large.
They also stay in one compact regular-frequency set on which
\[
c_0t\le |x(t)|\le C_0t.
\tag{14}
\]
These follow from \(x=t(\nabla P_0(\xi)+z)\), the positive free-velocity lower bound and the bounded free velocity on that compact set.
The identity \(dH/dt=H_x\cdot H_\xi-H_\xi\cdot H_x=0\) gives conservation of the Hamilton energy
\(H=P_0+V_L\), so every orbit has energy \(\lambda\).

<a id="escaping-symplectic-form"></a>

With the chosen cotangent form, the symplectic form is \(\omega=-d\beta=\sum d\xi_j\wedge dx_j\), so \(\omega(X_H,w)=-dH(w)\). We prove the preservation needed here directly. Order a variation as \(a=(a_x,a_\xi)\), and set

\[
 Q=\begin{pmatrix}0&-I\\I&0\end{pmatrix},\qquad
 \omega(a,b)=a^{\mathsf T}Qb.
\]

The Hamilton vector is \(X_H=-Q\nabla H\). Two transported variations satisfy \(a'=-QH''a\) and \(b'=-QH''b\), with the Hessian evaluated along the orbit. Its symmetry and \(Q^2=-I\) give

\[
 \frac d{dt}(a^{\mathsf T}Qb)
 =a^{\mathsf T}\bigl((-QH'')^{\mathsf T}Q+Q(-QH'')\bigr)b
 =a^{\mathsf T}(-H''+H'')b=0.
\]

Thus the smooth Hamilton flow preserves this two-form on every finite interval of its existence. This calculation also fixes its sign without importing a global generating-function theorem. Teschl [T] develops the same Hamiltonian and canonical-coordinate background; the flow and all estimates required at infinity are supplied by the preceding lesson.

<a id="escaping-immersion"></a>

The initial graph \(x=T\nabla P_0(\eta)\) is isotropic: its Hessian is symmetric, so the cotangent two-form vanishes on the full graph, hence on its \((n-1)\)-dimensional energy sheet.
The Hamilton field is transverse to the initial sheet. A tangent vector to the full graph obeys
\(\delta x=T P_0''(\eta)\delta\eta\).
The Hamilton vector would obey that identity only if
\[
\nabla P_0+V_{L,\xi}+T P_0''V_{L,x}=0.
\tag{15}
\]
Its left side is \(\nabla P_0+O(T^{-\delta})\), because
\(V_{L,\xi}=O(T^{-\delta})\) and \(V_{L,x}=O(T^{-1-\delta})\) on the initial sheet.
The free velocity is bounded away from zero, so the identity is impossible for large \(T\).
The finite-time flow is locally invertible by following the same autonomous equation backward along the compact orbit segment. The [local existence proof](hamilton-trajectories-under-a-long-range-force.md#hamilton-local-flow-and-data-derivatives) applies after reversing time, and uniqueness makes forward and backward maps inverse. Uniqueness also gives \(\Phi_s\Phi_r=\Phi_{s+r}\) wherever both sides are defined; differentiating in \(r\) at zero shows \(D\Phi_sX_H=X_H\circ\Phi_s\). Thus its invertible derivative transports the initial transversality and all tangent directions.
Thus its flowout is an immersed \(n\)-dimensional manifold.
The two-form vanishes on the transported initial tangent directions by the Hamilton preservation theorem.
Its pairing with the Hamilton direction vanishes because every transported direction is tangent to the energy level, and
\(\omega(X_H,w)=-dH(w)\).
It is therefore Lagrangian at every future point. Indeed the displayed matrix \(Q\) is invertible, so for a subspace \(L\) the symplectic orthogonal has dimension \(2n-\dim L\): the map \(w\mapsto\omega(w,\cdot)|_L\) onto \(L^*\) is surjective by nondegeneracy and extension of a linear functional from a basis of \(L\). An isotropic \(n\)-plane is contained in its symplectic orthogonal of the same dimension and hence equals it. This is the Lagrangian dimension criterion used here.

<a id="escaping-embedding"></a>

To prove global injectivity, rather than only immersion, use the escape coordinate
\[
\ell(x,\xi)=\frac{x\cdot\nabla P_0(\xi)}{|\nabla P_0(\xi)|^2}.
\tag{16}
\]
It equals \(T\) on the entire initial sheet.
Its \(x\)-gradient is \(v/|v|^2\), and its frequency derivatives are
\(O(|x|)\) on the compact regular-frequency region. Consequently
\[
\begin{gathered}
X_H\ell
     \\ =1+\ell_x\cdot V_{L,\xi}
                  -\ell_\xi\cdot V_{L,x}
     \\ =1+O((1+|x|^2)^{-\delta/2}).
\end{gathered}
\tag{17}
\]
The trajectory bound \(|x|\ge c_0T\) makes this at least \(1/2\) everywhere on every future orbit when \(T\) is large.
Each such orbit therefore meets the initial section \(\ell=T\) only once.
If two future parametrizations meet, autonomous ODE uniqueness says that one initial point is a future translate of the other, unless the times agree.
Strict increase of \(\ell\) forbids a positive translate between two initial points, and equal time then forces equal initial data.
Thus the flowout map is injective.

It is an embedding, not merely an injective immersion.
For a convergent sequence of image points, \(|x|\asymp t\) bounds the times, and compactness of the initial sheet supplies convergent subsequences of initial data.
If the limit point lies in the open future image, strict \(\ell>T\) excludes a limit time \(T\).
Every convergent subsequence has the same parameter limit by injectivity, so the inverse is continuous.
To see local smoothness of the inverse without an additional rank theorem, choose \(n\) ambient coordinate components for which the derivative of the parametrization has a nonsingular minor. The [written inverse theorem](../providers/analysis/coordinate-inverses-and-integration.md#coordinate-inverse) applied to these components supplies local parameter coordinates; the other components are smooth functions of them. The already proved continuity of the global inverse excludes other parameter branches from a sufficiently small relative neighborhood.
Hence the interior flowout is an embedded Lagrangian, with compact initial boundary if that boundary is included.

<a id="escaping-negative-direction"></a>

The same reasoning works for the negative normal direction by applying the positive construction to \(-P_0,-V_L,-\lambda\) and reversing the actual time parameter. The free normal becomes \(-\nabla P_0\), the same regular collar and properness remain valid, and the same estimates hold with these reversed signs.

<a id="escaping-global-action"></a>

## 4. An action that does not require simple connectivity

The embedded flowout has the global parameters \(t\ge T\) and initial frequency
\(\eta\in M_T\). Define
\[
\begin{gathered}
\psi(t,\eta)\\ =
  -T V_L(T\nabla P_0(\eta),\eta)
       \\ +\int_T^t x(s,\eta)\cdot\xi'(s,\eta)\,ds.
\end{gathered}
\tag{18}
\]
This is a real smooth finite-time integral on the whole flowout. Its initial value is the required \(-TV_L\). On the initial energy sheet,
\[
\begin{gathered}
T\nabla P_0(\eta)\cdot d\eta
       \\ =T\,d(P_0(\eta)-\lambda)
       \\ =-T\,d[V_L(T\nabla P_0(\eta),\eta)].
\end{gathered}
\tag{19}
\]
The rightmost differential is the total differential along the initial graph, including its position dependence. Thus its initial differential is the restriction of
\(\beta=\sum_jx_jd\xi_j\).

Use local coordinates \(q\) on the initial sheet. Since every orbit has the same conserved energy \(\lambda\),
\[
H_x\cdot x_q+H_\xi\cdot\xi_q=0.
\tag{20}
\]
The exact finite product calculation gives
\[
\begin{gathered}
\partial_q(x\cdot\xi')-\partial_t(x\cdot\xi_q)
 \\ =x_q\cdot\xi'-x'\cdot\xi_q\\
 \\ =-H_x\cdot x_q-H_\xi\cdot\xi_q\\ =0.
\end{gathered}
\tag{21}
\]
Integration with the initial differential therefore gives
\(\partial_q\psi=x\cdot\xi_q\).
In the time direction, \(\partial_t\psi=x\cdot\xi'\) by definition.
These coordinates span the tangent of the embedded flowout, so
\[
d\psi=\beta|_{\Lambda_T^+}.
\tag{22}
\]
No global simple connectivity of the energy shell is needed.
The exact initial differential and the orbit parametrization supply global exactness directly, rather than inferring it merely from a closed form.
Uniqueness follows because the difference of two such functions has derivative zero along every orbit and initial value zero. Every point lies on an orbit from the initial section.

<a id="escaping-chain-bounds"></a>

## 5. Every derivative of the initial sheet

Work near \(\xi^0\in M_\lambda\), choose a coordinate with
\(\partial_1P_0(\xi^0)\ne0\), and let
\(\xi_1=E(\xi')\) be the free sheet.
After shrinking to a fixed compact chart, write
\[
P_0(\xi)-\lambda=(\xi_1-E(\xi'))A(\xi),
\tag{23}
\]
where
\[
\begin{gathered}
A(\xi)\\ =\int_0^1\partial_1P_0
      (E(\xi')+s(\xi_1-E(\xi')),\xi')\,ds
\end{gathered}
\tag{24}
\]
is smooth and bounded away from zero. A fixed regular-velocity tube has
\(|\nabla P_0|\ge c_0>0\).
The energy equation becomes
\[
\begin{gathered}
\xi_1-E(\xi')=F_T(\xi),\\
 F_T(\xi)=-A(\xi)^{-1}V_L(T\nabla P_0(\xi),\xi).
\end{gathered}
\tag{25}
\]
Put \(b(k)=k-m(k)\), \(c(k)=\max(b(k),0)\), and let \(D\) denote ordinary coordinate derivatives. Finite chain expansions and monotonicity of \(j-m(j)\) give
\[
|D^\alpha F_T|\le C_\alpha T^{b(|\alpha|)}.
\tag{26}
\]
In particular its value and first derivative are \(O(T^{-\delta})\).
Choose a fixed interval around \(E(\xi')\) within the chart.
The map \(r\mapsto E(\xi')+F_T(r,\xi')\) preserves the interval and has contraction constant below \(1/2\) for all sufficiently large \(T\), uniformly in the inner chart.
Its geometrically convergent iterates give a unique sheet \(r=E_T(\xi')\).
Difference quotients of the fixed-point equation solve an invertible scalar linear equation; successive differentiation gives a smooth real sheet.
The zero-order difference is \(O(T^{-\delta})\).

<a id="escaping-exponent-partitions"></a>

The needed exponent partition is
\[
\begin{gathered}
b(q)+\sum_{i=1}^q c(k_i)\le b(k),
 \\ k_i\ge1,\\ \sum_i k_i=k.
\end{gathered}
\tag{27}
\]
To prove it, put \(\theta=(1-\delta)/\kappa\).
Here \(b(j)=-\delta\) for \(j\le\kappa\), and
\(b(j)=\theta j-1>0\) for \(j\ge\kappa+1\). The strict bound \(\delta<1/(\kappa+1)\) gives positivity at the first higher order, and the slope \(\theta\) is positive.
If all input orders are small, monotonicity \(b(q)\le b(k)\) suffices.
Otherwise let \(\ell\ge1\) count the input orders at least \(\kappa+1\).
Their sum is at most \(k-q+\ell\), hence
\[
\sum_i c(k_i)\le\theta(k-q+\ell)-\ell.
\tag{28}
\]
When \(q\ge\kappa+1\), adding \(b(q)=\theta q-1\) leaves
\(b(k)+\ell(\theta-1)\le b(k)\).
When \(q\le\kappa\), the difference from \(b(k)\) is at most
\[
1-\delta-\theta q+\ell(\theta-1)
       \le-\delta-\theta(q-1)\le0.
\tag{29}
\]
This proves all partitions, including the low total-order case.

<a id="escaping-sheet-jets"></a>

For the first derivative, differentiation of \(E_T-E=F_T(E_T,\xi')\) gives, with \(F_1=\partial_1F_T(E_T,\xi')\),

\[
 (1-F_1)D(E_T-E)
 =F_1DE+(D_{\xi'}F_T)(E_T,\xi').
\]

Both terms on the right are \(O(T^{-\delta})\), and \(|1-F_1|\ge1/2\). Thus \(D(E_T-E)=O(T^{-\delta})\), including the derivative of the affine transverse input. This supplies the base case for the higher-order induction.

Inductively, the graph map \((E_T(\xi'),\xi')\) has order-\(j\) derivatives
\(O(T^{c(j)})\): the fixed free graph is bounded, and its difference has the \(T^{b(j)}\) estimate.
At order \(k\ge2\), isolate the term containing the highest derivative:
\[
(1-\partial_1F_T(E_T,\xi'))D^k(E_T-E).
\tag{30}
\]
All other finite chain terms have outer derivative order \(q\ge2\) and lower graph derivatives with orders summing to \(k\), or the first outer derivative times the fixed \(D^kE\).
The partition inequality bounds the former by \(CT^{b(k)}\); the latter is
\(O(T^{b(1)})=O(T^{-\delta})\), also no larger than \(CT^{b(k)}\).
The coefficient is bounded away from zero. Thus every order satisfies
\[
|D_{\xi'}^\alpha(E_T-E)|\le C_\alpha T^{|\alpha|-m(|\alpha|)}.
\tag{31}
\]
Finitely many such charts cover the compact shell. Their unique roots agree with the global normal-graph construction of Section 2, so the constants can be chosen uniformly on each compact inner chart. This finishes Theorem 1.1.

The action will next supply local generating functions. Its global definition fixes their transition constants, while the mixed flow estimates control all their radial and transverse derivatives.

### Use the conclusion

Check the embedding and the normalization at the free end. Retain the regular energy collar when restricting the construction; a statement near the shell must not be promoted to arbitrary frequencies.

<a id="escaping-solutions"></a>

## 6. Exercises with complete solutions

**Exercise 1 — Basic — free rays, empty shells and critical energies.**

Let \(P_0(\xi)=|\xi|^2\) on \(\mathbb R^n\). Describe the near-shell construction when \(V_L=0\) for \(\lambda>0\), \(\lambda<0\) and \(\lambda=0\). For positive energy compute the escape coordinate, the restricted cotangent form, and the normalized action. Explain which case is excluded by the regular-value hypothesis.

**Solution 1.** For \(\lambda>0\), \(M_\lambda\) is the sphere of radius
\(\sqrt\lambda\), and the initial frequency sheet is the same sphere. The initial graph is \(x(T)=2T\eta\). Hamilton's equations give

\[
\begin{gathered}
\xi(t)=\eta,\\ x(t)=2t\eta,\\
 \ell(x,\xi)=\frac{x\cdot2\xi}{4|\xi|^2}=t.
\end{gathered}
\tag{32}
\]

On tangents to the sphere,
\(\beta=x\cdot d\xi=2t\eta\cdot d\eta=t\,d|\eta|^2=0\).
Its time component is also zero because \(\xi\) is constant. The action has initial value zero and remains zero. The outward family is embedded: its frequency is the initial \(\eta\), and its position determines \(t=|x|/(2\sqrt\lambda)\).

For \(\lambda<0\), the shell is empty. An empty inverse image satisfies the definition of a regular value, and a sufficiently small energy band is also empty. Thus the near-shell family is empty. For \(\lambda=0\), the shell consists of the critical point \(\xi=0\), since \(\nabla P_0(0)=0\). This energy is excluded. Its stationary free orbit does not provide an escaping regular-energy family.

**Exercise 2 — Intermediate — two long-range initial frequencies on the line.**

Take \(P_0(\xi)=\xi^2\), \(\lambda=a^2\) with \(a>0\), and
\(V_L(x,\xi)=b(1+x^2)^{-\delta/2}\), where \(b\) is real and
\(0<\delta<1/(\kappa+1)\). Let \(\eta_T^+\) and \(\eta_T^-\) be the near-shell roots converging to \(a\) and \(-a\). Find their first asymptotic corrections and the leading initial action at both roots. Do not assume that a component of the frequency shell has positive dimension.

**Solution 2.** This potential has all derivatives bounded by
\(C_j(1+|x|^2)^{-(j+\delta)/2}\), which is at least as strong as the required full class. Both free roots are regular. The local sheet theorem on the line gives one root near each of them, with
\(\eta_T^\pm=\pm a+O(T^{-\delta})\). Their equation is

\[
(\eta_T^\pm)^2-a^2
      =-b(1+4T^2(\eta_T^\pm)^2)^{-\delta/2}.
\tag{33}
\]

Because \(\eta_T^\pm\to\pm a\),
\[
T^\delta(1+4T^2(\eta_T^\pm)^2)^{-\delta/2}
          \longrightarrow(2a)^{-\delta}.
\tag{34}
\]

Factor the left side at the appropriate free root and divide by the other factor. This yields

\[
\begin{aligned}
 \eta_T^+&=a-\frac{b(2a)^{-\delta}}{2a}T^{-\delta}
                    +o(T^{-\delta}),\\
 \eta_T^-&=-a+\frac{b(2a)^{-\delta}}{2a}T^{-\delta}
                    +o(T^{-\delta}).
 \end{aligned}
\tag{35}
\]

The prescribed initial action is
\(-Tb(1+4T^2(\eta_T^\pm)^2)^{-\delta/2}\). At either root it equals
\[
-b(2a)^{-\delta}T^{1-\delta}+o(T^{1-\delta}).
\tag{36}
\]

For \(b=0\) all corrections vanish exactly. In dimension one the frequency sheet is a finite set of points; there are no transverse frequency derivatives. Each nonempty component still generates a one-dimensional escaping orbit and has its own prescribed initial action.

**Exercise 3 — Intermediate — derivatives at the joining order.**

Set \(\kappa=3\), \(\delta=1/8\), \(b(j)=j-m(j)\), and
\(c(j)=\max(b(j),0)\). Compute \(b(j)\) for \(0\le j\le5\).
State the bounds for derivatives of \(E_T-E\) of orders three, four and five. In the fifth derivative of the fixed-point expression, estimate a term with outer order two and inner orders four and one. Compare this with the permitted fifth-order bound.

**Solution 3.** For \(j\le3\), \(m(j)=j+1/8\), so \(b(j)=-1/8\).
For \(j\ge3\),
\[
m(j)=1+\frac{17}{24}j,\qquad b(j)=\frac7{24}j-1.
\tag{37}
\]

The two definitions agree at three. Consequently
\[
b(4)=\frac16,\qquad b(5)=\frac{11}{24}.
\tag{38}
\]

The third difference derivative is \(O(T^{-1/8})\), the fourth is
\(O(T^{1/6})\), and the fifth is \(O(T^{11/24})\). These are estimates for the difference from the fixed free graph; the graph itself has derivatives
\(O(T^{c(j)})\).

The indicated chain-rule term has an outer second derivative of \(F_T\), of size \(T^{b(2)}\), a fourth graph derivative of size \(T^{c(4)}\), and a first graph derivative of bounded size. Its exponent is
\[
\begin{gathered}
b(2)+c(4)+c(1)=-\frac18+\frac16=\frac1{24}
          \\ \le\frac{11}{24}=b(5).
\end{gathered}
\tag{39}
\]

Thus it is smaller than the allowed fifth-order bound. In contrast, a fourth derivative with outer order four and four first graph derivatives may have exponent \(b(4)=1/6\). A growing high derivative therefore does not contradict the small value and first derivatives of the perturbed sheet.

**Exercise 4 — Advanced — periods on a shell with loops.**

Assume \(n=2\), \(P_0=|\xi|^2\), \(\lambda=1\), and the general long-range hypotheses. For a smooth closed curve \(\gamma\) in \(M_T\), let \(\gamma_t\) be its transported curve in the escaping family at time \(t\). Prove directly that
\(\int_{\gamma_t}\beta=0\) for every \(t\ge T\). Explain why closedness of \(\beta\) alone would not prove the existence of a single-valued action on this family.

**Solution 4.** The initial sheet is diffeomorphic to the circle and can carry loops. Write the curve with a periodic parameter \(q\), and let \(x(t,q),\xi(t,q)\) be its Hamilton transport. At the initial time,
\[
\begin{gathered}
x(T,q)\cdot\partial_q\xi(T,q)
   \\ =-T\,\partial_q[V_L(Tv(\xi(T,q)),\xi(T,q))].
\end{gathered}
\tag{40}
\]

Its integral over the period is zero. Conservation of the common energy gives
\[
\partial_t(x\cdot\xi_q)
       =\partial_q(x\cdot\xi_t).
\tag{41}
\]

Integrating this identity over the periodic \(q\) shows that
\(\partial_t\int x\cdot\xi_q\,dq=0\). The initial zero period therefore remains zero for every \(t\).

More explicitly the finite-time action
\[
\begin{gathered}
\psi(t,\eta)\\ =-TV_L(Tv(\eta),\eta)
                  \\ +\int_T^t x(s,\eta)\cdot\xi_s(s,\eta)\,ds
\end{gathered}
\tag{42}
\]
is already a globally defined function on the entire parameter cylinder, and its differential is \(\beta\). A closed one-form on a cylinder need not be exact: on the circle the smooth one-form represented by \(d\theta\) in angular charts has period \(2\pi\). The energy identity and exact initial differential, rather than a simple-connectivity assumption, eliminate these periods in the escaping family.

**Exercise 5 — Advanced — a degenerate component away from the regular shell.**

Let \(n\ge2\), \(P_0(\xi)=|\xi|^4\), \(\lambda=1\), and let
\(V_L(x,\xi)=\chi(x)\), with the cutoff from Section 1. Show that the unrestricted initial frequency set has an isolated point at zero for every \(T\), while its near-shell sheet is the unit sphere for large \(T\). Prove that the unrestricted forward flowout contains an isolated stationary point. Check properness, regularity and the decay assumptions.

**Solution 5.** The polynomial is real and proper, and
\(\nabla P_0(\xi)=4|\xi|^2\xi\). On the unit sphere this gradient has norm four, so energy one is regular. In
\(|\xi|<(4T)^{-1/3}\), the initial position
\(4T|\xi|^2\xi\) has norm less than one. The unrestricted initial equation reduces there to
\[
|\xi|^4+\chi(4T|\xi|^2\xi)-1=|\xi|^4=0.
\tag{43}
\]

Thus zero is an isolated point of that frequency set. Near the unit sphere, the initial position lies outside \(|x|=2\) for all sufficiently large \(T\), so the perturbed equation is exactly \(|\xi|^4=1\).

At \((x,\xi)=(0,0)\), both Hamilton components vanish:
\(x'=4|\xi|^2\xi=0\) and \(\xi'=-\nabla\chi(0)=0\).
If any energy-one orbit enters \(|x|\le1\), its energy identity gives
\(|\xi|^4+1=1\), hence \(\xi=0\). Every such phase point is stationary. Uniqueness of the smooth ODE prevents a different orbit from reaching it at a finite time. Other initial points have \(|x|>1\), so their forward images stay outside that closed position region. In a position neighborhood of zero the unrestricted union therefore contains only its stationary initial point.

A positive-dimensional hypersurface cannot have an isolated point, and an \(n\)-dimensional Lagrangian cannot have this isolated component. The smooth compactly supported potential has all required position derivative bounds for every allowed \(\kappa,\delta\), and is independent of frequency. Restricting the initial frequencies to a regular collar of the unit sphere removes the degenerate component and preserves the escaping construction.


## References

[T] Gerald Teschl, [*Ordinary Differential Equations and Dynamical Systems*, free author's preliminary edition](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf), April 2012, §§2.2, 2.4 and 2.6. The programme's preceding flow lesson proves the local existence, smooth data dependence and compact continuation used here. Section 3 above supplies the exact symplectic preservation and embedding arguments.

[O] Sung-Jin Oh, [*Lecture Notes for Math 222A*, free evolving lecture notes](https://math.berkeley.edu/~sjoh/pdfs/notes-math222a.pdf), University of California, Berkeley, Fall 2023, §2.4.1, pp. 23–24. The Hamilton characteristic equations (2.20) provide the comparison; the global sheet, escaping embedding and normalized action are proved in Sections 2–5 above.



[H4] Lars Hörmander, *The Analysis of Linear Partial Differential Operators IV: Fourier Integral Operators*, reprint of the 1994 edition, Springer, 2009, Lemma 30.3.4 and the initial flowout assertion of Theorem 30.3.5, pp. 303–304; Theorem 30.3.6, normalized action (30.3.28) and its proof, p. 307. ISBN 978-3-642-00136-9. [Edition information](https://doi.org/10.1007/978-3-642-00136-9).
