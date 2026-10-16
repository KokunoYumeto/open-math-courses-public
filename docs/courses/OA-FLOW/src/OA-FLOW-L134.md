# The Weyl-plane action and its continuous part

Translations and modulations on $L^2(\mathbb R)$ form a projective
representation of the phase plane.  Scalar projective multipliers disappear
under conjugation, producing an honest action on all bounded operators.  The
same Weyl relations compute its integrability, Connes spectrum, centralizer,
and invariant von Neumann subalgebras.

For a first reading, follow the Weyl relations and orthogonality in
(Y1)–(Y13), then the continuous part in (Y28)–(Y37). The centralizer
calculation (Y14)–(Y17) is a short matrix-unit application. The longer
subgroup correspondence (Y18)–(Y27) can be read separately after the
trace-class convolution, Fourier localization and synthesis arguments.

The norm-continuous part contains the identity and every Weyl unitary, so it strictly contains the compact operators. We characterize it by $L^1$ convolution and explain the discrepancy with the source exercise in the final sections.

The earlier inputs are [the concrete predual construction](OA-FLOW-CP.md#oa-flow.cp.1), [scalar integration and Fourier analysis](OA-FLOW-FF.md#oa-flow.ff.1), [smooth filters](OA-FLOW-L35.md#oa-flow.gi.fourier), [smooth Fourier cutoffs and inversion](OA-FLOW-RF.md#oa-flow.rf.1), [normal integrated actions](OA-FLOW-AT.md#oa-flow.at.5), [the concrete Weyl commutant calculation](OA-FLOW-ND.md#nd-weyl-proof), and [the action and Connes spectra](OA-FLOW-L115.md#oa-flow.connes.centerkernel). The trace-class realization and Euclidean subgroup synthesis are proved below.

Let $\mathcal H=L^2(\mathbb R)$, with Lebesgue measure, and define

$$
(U_s\xi)(r)=\xi(r+s),
\qquad
(V_t\xi)(r)=e^{irt}\xi(r),
\qquad
W(s,t)=U_sV_t.
\tag{Y1}
$$

We identify the dual of $\mathbb R^2$ by
$\chi_{(p,q)}(s,t)=e^{i(sp+tq)}$ and use Lebesgue measure $ds\,dt$.

*Original lesson exposition: CC0-1.0 to the extent of rights held. Cited works retain their own terms.*

<a id="weylplane-action"></a>

## The projective Weyl pair gives an honest plane action

Direct calculation gives

$$
U_sV_t=e^{ist}V_tU_s
\tag{Y2}
$$

and therefore

$$
W(s,t)W(a,b)=e^{-iat}W(s+a,t+b).
\tag{Y3}
$$

Thus $W$ is a strongly continuous projective unitary representation with
multiplier $m((s,t),(a,b))=e^{-iat}$.  Define

$$
\alpha_{(s,t)}=\operatorname{Ad}W(s,t)
\quad\text{on }B(\mathcal H).
\tag{Y4}
$$

The two multipliers in a product of inner automorphisms cancel, so

$$
\alpha_z\alpha_w=\alpha_{z+w}
\qquad(z,w\in\mathbb R^2).
\tag{Y5}
$$

Translations are strongly continuous on $L^2(\mathbb R)$ by [FF-1](OA-FLOW-FF.md#oa-flow.ff.2); modulation continuity follows by dominated convergence, since $|e^{irt}-1|^2|\xi(r)|^2\le4|\xi(r)|^2$. Splitting a product difference proves joint strong continuity of $W(s,t)$. The adjoints are strongly continuous too, by the group formulas. For fixed $x$ and $\xi$, split
\[
 (W(z)xW(z)^*-W(z_0)xW(z_0)^*)\xi
 =W(z)x(W(z)^*-W(z_0)^*)\xi
 +(W(z)-W(z_0))xW(z_0)^*\xi .
\]
Both terms tend to zero; replacing $x$ by $x^*$ proves strong-star continuity. Every normal functional is a summable vector series by CP-04. The uniform bound $2\|x\|$ controls its tail, so finite vector tests prove point-ultraweak continuity on the whole predual. Thus (Y4) is a continuous action despite the multiplier in (Y3).

The commutator phase will be used repeatedly.  If
$z=(s,t)$ and $w=(a,b)$, then

$$
\alpha_z(W(w))
=e^{i\omega(z,w)}W(w),
\qquad
\omega(z,w)=sb-at.
\tag{Y6}
$$

The alternating form $\omega$ is nondegenerate.

<a id="weylplane-integrable"></a>

## Phase-space orthogonality proves integrability

For $\xi,\eta\in\mathcal H$, Fubini and scalar Plancherel give the exact
orthogonality identity

$$
\int_{\mathbb R^2}
|\langle\eta,W(s,t)\xi\rangle|^2\,ds\,dt
=2\pi\|\xi\|^2\|\eta\|^2.
\tag{Y7}
$$

For fixed $s$, the product $h_s(u)=\xi(u)\overline{\eta(u-s)}$ is integrable by Cauchy–Schwarz. Tonelli gives
\[
 \int_{\mathbb R}\int_{\mathbb R}|h_s(u)|^2\,du\,ds
 =\|\xi\|^2\|\eta\|^2,
\]
so $h_s\in L^1\cap L^2$ for almost every $s$. After the change $u=r+s$, the coefficient in (Y7) is $\overline{\int h_s(u)e^{itu}\,du}$. Its modulus is therefore the modulus of the ordinary Fourier transform of $h_s$. The full $L^1\cap L^2$ compatibility and Plancherel theorem of [FF-2](OA-FLOW-FF.md#oa-flow.ff.3) therefore give the factor $2\pi$ for almost every $s$. A second application of Tonelli proves (Y7) for all $\xi,\eta\in L^2$, with no boundedness or smoothness hypothesis on the vectors.

Write $\Theta_{\xi,\xi}$ for the positive rank-one operator
$\zeta\mapsto\langle\zeta,\xi\rangle\xi$, using the course convention that
the inner product is linear in the first variable.  For every $\eta$,
(Y7) says

$$
\int_{\mathbb R^2}
\langle\alpha_z(\Theta_{\xi,\xi})\eta,\eta\rangle\,dz
=2\pi\|\xi\|^2\|\eta\|^2.
\tag{Y8}
$$

The increasing net of compact positive orbit integrals therefore has the
bounded ultraweak supremum

$$
\int_{\mathbb R^2}\alpha_z(\Theta_{\xi,\xi})\,dz
=2\pi\|\xi\|^2 1.
\tag{Y9}
$$

Positive finite-rank operators are finite positive sums of such rank-one
operators, so they all belong to the bounded positive integrability domain.
For every $x\ge0$, the operators $x^{1/2}P_Fx^{1/2}$, where $P_F$ ranges over the projections onto finite-dimensional subspaces, are positive finite-rank operators bounded by $x$ and increase strongly to $x$. Their values under every positive normal functional increase to its value at $x$, and all normal-functional values converge, by the vector-series description. Thus the positive bounded-integral domain is order dense, as well as having ultraweakly dense linear span. The positive action integral is semifinite:

$$
\boxed{\alpha\text{ is an integrable action of }\mathbb R^2.}
\tag{Y10}
$$

No operator-norm integral over the whole plane is asserted in (Y8)–(Y9).

<a id="weylplane-connes"></a>

## The Connes spectrum is the whole dual plane

An operator fixed by every $\alpha_z$ commutes with every translation and
every modulation.  Commutation with all $V_t$ makes it a multiplication
operator, and commutation with all $U_s$ makes its multiplier translation
invariant.  The multiplier and translation-invariant-class steps, including almost-everywhere equivalence, are the full [ND Weyl proof](OA-FLOW-ND.md#nd-weyl-proof). Thus

$$
B(\mathcal H)^\alpha=\mathbb C1.
\tag{Y11}
$$

Formula (Y6) says that $W(a,b)$ is an eigenunitary for the dual frequency

$$
(p,q)=(b,-a).
\tag{Y12}
$$

As $(a,b)$ ranges over the plane, so does $(p,q)$. If an integrated kernel annihilates the entire action, applying it to $W(a,b)$ makes its Fourier transform vanish at every such frequency. Consequently the hull defining the action spectrum contains every $(p,q)$; equivalently each displayed eigenunitary contributes its own frequency. Thus the point spectrum and action spectrum both fill $\mathbb R^2$.  The only nonzero
projection in the fixed algebra (Y11) is $1$, so the intersection defining
the Connes spectrum has only the unreduced action as a term.  Consequently

$$
\boxed{\Gamma(\alpha)=\operatorname{Sp}(\alpha)=\mathbb R^2.}
\tag{Y13}
$$

The same calculation proves that every eigenspace is one dimensional.  If
$x$ has the character in (Y12), then $W(a,b)^*x$ is fixed by $\alpha$ and
therefore scalar by (Y11).

<a id="weylplane-centralizer"></a>

## Every commuting automorphism is a Weyl translation

Let $\beta\in\operatorname{Aut}(B(\mathcal H))$ commute with every
$\alpha_z$. A star automorphism of a von Neumann algebra is normal: it and its inverse preserve order, hence every existing least upper bound of a bounded increasing net. The equivalence with ultraweak normality is the [automatic normality proof](OA-FLOW-L123.md#oa-flow.l123.ic0). Here is its inner implementation in this setting.
Choose an orthonormal basis $(\xi_i)$ and its matrix units $e_{ij}$,
with one distinguished index $0$. The image $\beta(e_{00})$ is a
minimal projection of $B(\mathcal H)$ and therefore has rank one:
a projection of larger rank has a nontrivial rank-one subprojection.
Choose a unit vector $\eta_0$ in its range and set
$\eta_i=\beta(e_{i0})\eta_0$. The matrix-unit relations make these
vectors orthonormal. Normality of $\beta$ gives
$\sum_i\beta(e_{ii})=1$, so they form a basis. The unitary
$T\xi_i=\eta_i$ implements $\beta$ on every matrix unit. Finite
matrix compressions converge strongly on the bounded unit ball,
and hence ultraweakly; normality extends the identity to every
operator. Thus $\beta=\operatorname{Ad}T$. Commutation of the two inner
automorphisms implies

$$
TW(z)T^*W(z)^*\in\mathbb T1.
\tag{Y14}
$$

Hence there is a scalar function $c$ with

$$
TW(z)T^*=c(z)W(z).
\tag{Y15}
$$

Strong continuity makes $c$ continuous.  Applying (Y15) to the product law
(Y3) shows $c(z+w)=c(z)c(w)$, so

$$
c(s,t)=e^{i(ps+qt)}
\tag{Y16}
$$

for unique $p,q\in\mathbb R$. Here the elementary character assertion can be seen without a duality theorem. For a continuous character $d:\mathbb R\to\mathbb T$, choose a neighborhood of zero on which $d(t)=e^{i\phi(t)}$ with continuous $|\phi(t)|<\pi/4$ and $\phi(0)=0$. The character law makes $\phi(s+t)-\phi(s)-\phi(t)$ an integer multiple of $2\pi$; when all three arguments are in that neighborhood its absolute value is less than $3\pi/4$, hence it is zero. Fix a positive $a$ in a smaller interval. Subdivision and repeated local addition show $\phi(ra)=r\phi(a)$ for rational $r$ with $ra$ in that smaller interval. Continuity extends this to real $r$, so $\phi(t)=pt$ there. Writing any $t$ as a sufficiently large integer multiple of a small argument gives $d(t)=e^{ipt}$ everywhere. Apply this to $c(s,0)$ and $c(0,t)$ and use $c(s,t)=c(s,0)c(0,t)$. Equality of two slopes at every sufficiently small real argument forces them equal. By (Y6), conjugation by $W(q,-p)$ has exactly
the same effect (Y16) on every $W(s,t)$.  Therefore
$W(q,-p)^*T$ commutes with the irreducible Weyl family and is scalar.  We
obtain

$$
\boxed{
\{\beta\in\operatorname{Aut}(B(\mathcal H)):
\beta\alpha_z=\alpha_z\beta\ \forall z\}
=\alpha(\mathbb R^2).}
\tag{Y17}
$$

Faithfulness follows at the same time: nondegeneracy of $\omega$ makes
$\alpha_z=\operatorname{id}$ possible only for $z=0$.

<a id="weylplane-subgroups"></a>

## Closed subgroups classify invariant von Neumann subalgebras

For $E\subseteq\mathbb R^2$, define its symplectic annihilator by

$$
E^{\perp_\omega}
=\{z\in\mathbb R^2:e^{i\omega(z,e)}=1\text{ for every }e\in E\}.
\tag{Y18}
$$

An eigenoperator calculation alone does not prove this classification.
We supply the extra argument below: trace-class convolutions give a
Gaussian correspondence with classical ideals, and closed subgroups of
the Euclidean plane are synthesis sets.

<a id="weylplane-trace"></a>

### Trace-class operators from the concrete predual

Let $E_{\mathcal H}$ be the completed projective tensor space constructed in [CP-01–04](OA-FLOW-CP.md#oa-flow.cp.1). On algebraic tensors define
\[
 \iota(\xi\otimes\overline\eta)=\Theta_{\xi,\eta},
 \qquad \Theta_{\xi,\eta}\zeta=\langle\zeta,\eta\rangle\xi .
 \tag{TC1}
\]
The bound $\|\Theta_{\xi,\eta}\|=\|\xi\|\|\eta\|$ makes $\iota$ contractive into $B(\mathcal H)$, so it extends to the completion. This extension is injective. Indeed, for a finite-rank orthogonal projection $P$, the tensor map $C_P=P\otimes\overline P$ is contractive and
$\iota(C_Pu)=P\iota(u)P$. As $P$ increases over all finite-dimensional subspaces, $C_Pu\to u$ in the projective norm: this is immediate for a finite tensor sum and follows for the completion by contraction and approximation. The range of $C_P$ is the finite-dimensional tensor space $P\mathcal H\otimes\overline{P\mathcal H}$, and its rank-one matrix units are linearly independent as operators. Thus $\iota(u)=0$ makes every $C_Pu=0$, and the limit makes $u=0$.

Define $\mathcal T(\mathcal H)=\iota(E_{\mathcal H})$ and $\|S\|_1=\|\iota^{-1}S\|$. This is a Banach space and finite-rank operators are dense. CP-03 gives its complete dual:
\[
 \langle S,x\rangle=\operatorname{Tr}(Sx),\qquad
 \operatorname{Tr}(\Theta_{\xi,\eta}x)=\langle x\xi,\eta\rangle,
 \qquad \mathcal T(\mathcal H)^*=B(\mathcal H).
 \tag{TC2}
\]
Here the trace is defined by pairing with $1$. It agrees with the ordinary finite matrix trace on finite-rank operators. In particular
$|\operatorname{Tr}(Sx)|\le\|S\|_1\|x\|$ and
$\|\Theta_{\xi,\eta}\|_1=\|\xi\|\|\eta\|$ by CP-02.

For $a,b\in B(\mathcal H)$,
$a\Theta_{\xi,\eta}b=\Theta_{a\xi,b^*\eta}$. Taking the infimum over finite tensor representations, then passing to the completion, proves
$\|aSb\|_1\le\|a\|\|S\|_1\|b\|$.
Finite-rank calculation gives $\operatorname{Tr}(Sx)=\operatorname{Tr}(xS)$; both sides are trace-norm continuous, so this holds for every $S\in\mathcal T$. Conjugation by a unitary is a trace-norm isometry, since its inverse is also contractive. CP-04 represents every $S$ by an absolutely summable series of rank-one operators. The equality of the induced dual topology with the ultraweak topology and the annihilator identity for every ultraweakly closed linear subspace are [CP-04–05](OA-FLOW-CP.md#oa-flow.cp.4). Thus
\[
 N=(N_\perp)^\perp,\qquad
 N_\perp=\{S:\operatorname{Tr}(Sx)=0\text{ for every }x\in N\}.
 \tag{TC3}
\]

For completeness, the Hilbert–Schmidt completion used below also embeds faithfully in operators. On finite-rank operators put
$\|S\|_{\mathrm{HS}}^2=\sum_j\|Se_j\|^2$ for an orthonormal basis. Parseval on the finite-dimensional range makes this basis independent and gives its Hilbert inner product. Rank-one operators identify this space with the algebraic Hilbert tensor product $\mathcal H\otimes\overline{\mathcal H}$. The inequality $\|S\|\le\|S\|_{\mathrm{HS}}$ gives a bounded operator associated to every vector of the completion. If that operator is zero, its inner products with all rank-one tensors vanish, because these are its matrix coefficients; density forces the Hilbert tensor vector to be zero. Moreover the triangle inequality and
$\|\Theta_{\xi,\eta}\|_{\mathrm{HS}}=\|\xi\|\|\eta\|$
give $\|S\|_{\mathrm{HS}}\le\|S\|_1$ first on finite sums and then on all of $\mathcal T$. Hence trace-norm convergence implies Hilbert–Schmidt convergence with the same resulting operator.

These arguments supply precisely the trace-class, normal-functional and Hilbert–Schmidt facts needed here. No singular-value expansion is required. Rank-one operators with Schwartz vectors are trace-norm dense: approximate each vector in a finite sum in $L^2$ and use the rank-one norm bound.

<a id="weylplane-fourier"></a>

### The scalar Fourier and ideal conventions

The earlier [FF-1–2](OA-FLOW-FF.md#oa-flow.ff.2), [smooth-filter proof](OA-FLOW-L35.md#oa-flow.gi.fourier) and [RF-1](OA-FLOW-RF.md#oa-flow.rf.1) give Gaussian integration, Fourier inversion, scalar Plancherel, smooth cutoffs and the required $L^1$ compatibility. In two variables apply the one-variable transforms successively; integrable majorants justify Fubini on Schwartz functions, and the $L^2$ isometries extend the resulting identities by density. Repeated differentiation under the integral and integration by parts show that Fourier transform and inverse preserve the Schwartz seminorms. In particular, multiplying a Schwartz transform by a smooth cutoff equal to one on expanding balls converges in all Schwartz seminorms, as do the inverse transforms. Schwartz density in $L^1$ and $L^2$ follows by approximating by compact continuous functions and convolving with smooth compact approximate identities; uniform convergence on a common compact set gives the claimed norms. These are also the scalar approximation constructions of the linked Fourier lessons.

The vector integrals use [FF-3](OA-FLOW-FF.md#oa-flow.ff.4). For $m=1,2$, write $A(\mathbb R^m)=\{Fa:a\in L^1(\mathbb R^m)\}$ with the positive Fourier convention below. Its norm is $\|Fa\|_A=\|a\|_1$. Fourier injectivity makes the norm well-defined, and convolution makes it a Banach algebra. For a closed set $E$ put
\[
 I(E)=\{f\in A:f|_E=0\},\qquad
 j(E)=\overline{\{f\in A:\operatorname{supp}f\text{ is compact and disjoint from }E\}}^{\,\|\cdot\|_A}.
 \tag{TC4}
\]
For a closed ideal $J$, its hull is $h(J)=\{p:f(p)=0\text{ for every }f\in J\}$. These are the ideals in the local division and synthesis arguments below; no synthesis theorem is assumed.

<a id="weylplane-division"></a>

**Euclidean local division.** Use the ordinary positive-sign
transform $Fa(p)=\int a(t)e^{it\cdot p}\,dt$ on $\mathbb R^m$,
$m=1,2$, and the norm $\|Fa\|_A=\|a\|_1$. Smooth compact
functions are in this algebra by Schwartz inversion. Its compact
Fourier functions are dense: multiplying $Fa$ by
$\eta(p/R)$, where $\eta\in C_c^\infty$ is one near zero,
convolves $a$ with a bounded $L^1$ approximate identity.
Translation continuity proves convergence in $L^1$.
Fourier injectivity follows from the preceding Plancherel
argument, and vanishing at infinity follows by $L^1$
approximation from Schwartz kernels.

Let $f=Fa$ and $f(p_0)=c\ne0$. Choose
$\chi\in C_c^\infty$, equal to one near zero, and write
$\chi_\varepsilon(p)=\chi((p-p_0)/\varepsilon)$.
If $b_\varepsilon$ is the inverse transform of
$\chi(p/\varepsilon)$, then
$b_\varepsilon(t)=\varepsilon^m b(\varepsilon t)$.
Its $L^1$ norm is constant, and
$\|\tau_y b_\varepsilon-b_\varepsilon\|_1\to0$
for every fixed $y$. The inverse kernel of
$(f-c)\chi_\varepsilon$ is a modulation of

$$
\int a(y)e^{iy\cdot p_0}
       (\tau_y b_\varepsilon-b_\varepsilon)\,dy .
\tag{Y18a}
$$

This is an $L^1$ Bochner integral. Dominated convergence,
with bound $2\|b\|_1|a(y)|$, makes its norm tend to zero.
Choose $\varepsilon$ with
$\|(f-c)\chi_\varepsilon\|_A<|c|$. In the unitized Fourier
algebra, $d=c1+(f-c)\chi_\varepsilon$ has the inverse given by
its convergent Neumann series. On a neighborhood of $p_0$,
$d=f$. Multiply $d^{-1}$ by a smooth compact cutoff that is
one on a smaller neighborhood. The result lies in $A$ and
is a local inverse of $f$ there.

For a compact set on which $f$ has no zeros, choose finitely
many such neighborhoods and smooth cutoffs $c_i$ supported
inside them and equal to one on a smaller covering.
The functions $q_1=c_1$,
$q_i=c_i\prod_{k<i}(1-c_k)$ sum to one near that compact set.
Multiplying each local inverse by $q_i$ and summing proves
the compact local inverse assertion. It also proves the
local ideal inclusion used below: if $J$ is a closed ideal,
a compact Fourier function supported outside its common
zero set has a finite decomposition $h=\sum_i hq_i$ with
$hq_i=f_i(v_i hq_i)\in J$, where $f_i\in J$ is nonzero on
the supporting neighborhood and $v_i$ is its local inverse.
Taking norm closure gives $j(h(J))\subset J\subset I(h(J))$.
This supplies the Euclidean instance directly; no local
inverse theorem for an arbitrary LCA group is needed here.

<a id="weylplane-synthesis"></a>

**Weyl synthesis lemma.** Let $N\subseteq B(\mathcal H)$ be a unital von
Neumann algebra satisfying $\alpha_z(N)=N$ for every $z$.  Then

$$
L_N=\{w\in\mathbb R^2:W(w)\in N\}
\tag{Y19}
$$

is a closed subgroup and

$$
N=\{W(w):w\in L_N\}''.
\tag{Y20}
$$

Moreover, for every closed subgroup $L$,

$$
\{W(w):w\in L\}'
=\{W(z):z\in L^{\perp_\omega}\}''.
\tag{Y21}
$$

For trace-class $S$, its Fourier–Wigner
transform

$$
\mathcal W_S(w)=\operatorname{Tr}(S W(w)^*)
\tag{Y22}
$$

is continuous, vanishes at infinity, and separates trace-class operators.
Here is the norm argument needed for the last assertion. Polarizing (Y7)
in both vector variables and summing the resulting rank-one pairings gives,
for every finite-rank $S$,

$$
\int_{\mathbb R^2}|\mathcal W_S(w)|^2\,dw
=2\pi\|S\|_{\mathrm{HS}}^2.
\tag{Y22a}
$$

Take finite-rank $S_n$ converging to an arbitrary trace-class $S$ in trace
norm. They also converge in Hilbert--Schmidt norm, so (Y22a) gives an
$L^2$ limit of their transforms. Meanwhile
$\|\mathcal W_{S_n}-\mathcal W_S\|_\infty\leq\|S_n-S\|_1$.
On each compact set this uniform convergence is also $L^2$ convergence.
Hence the $L^2$ limit is $\mathcal W_S$ almost everywhere, and (Y22a)
holds for $S$. In particular, $\mathcal W_S=0$ implies $S=0$.
Injectivity is proved by this norm identity, rather than inferred from
injectivity on the finite-rank subspace alone.

For continuity and vanishing at infinity, approximate $S$ in trace norm
by finite-rank operators formed from Schwartz vectors. Their transforms
are Schwartz functions: explicitly,

$$
\mathcal W_{\Theta_{\xi,\eta}}(s,t)
=\int e^{-irt}\xi(r-s)\overline{\eta(r)}\,dr.
\tag{Y22b}
$$

This is a partial Fourier transform of a Schwartz function of $(r,s)$.
The same uniform bound makes $\mathcal W_S$ a uniform limit in $C_0$.
Conjugating $S$ by
$W(z)$ multiplies (Y22) by the character $w\mapsto e^{i\omega(z,w)}$.
Consequently $N_\perp$ is invariant under conjugation by Weyl operators.
The common zero set of its transforms is exactly $L_N$: by the
preannihilator separation theorem, $\mathcal W_S(w)=0$ for every
$S\in N_\perp$ if and only if $W(w)^*\in N$, equivalently $W(w)\in N$.
The multiplication and adjoint formulas (Y3) make $L_N$ a subgroup.
Strong continuity of $W$ and weak-star closedness of $N$ make it closed.

**Trace-class convolution.** For this proof only, use the normalized
measure $d\mu(z)=ds\,dt/(2\pi)$ and symmetric Weyl operators

$$
D(s,t)=e^{-ist/2}W(s,t),\qquad
Q_S(w)=\operatorname{Tr}(S D(w)^*),\qquad
(J\xi)(r)=\xi(-r).
\tag{Y22c}
$$

Thus $D(z)^*=D(-z)$, $JD(z)J=D(-z)$, and
$Q_S(a,b)=e^{iab/2}\mathcal W_S(a,b)$. Neither the zero sets nor the
generated algebras change. For $f\in L^1(d\mu)$ and trace-class $T,S$, set

$$
\begin{aligned}
f*T&=\int f(z)\alpha_z(T)\,d\mu(z),\\
(T*S)(z)&=\operatorname{Tr}\bigl(T\alpha_z(JSJ)\bigr),\\
F_\omega f(w)&=\int f(z)e^{i\omega(z,w)}\,d\mu(z).
\end{aligned}
\tag{Y22d}
$$

We also write $T*f=f*T$.
The first integral converges in trace norm: rank-one approximation and
strong continuity of $D$ make trace-class orbits norm continuous. It
satisfies $\|f*T\|_1\leq\|f\|_{L^1}\|T\|_1$. For two rank-one operators,
the integrand defining $T*S$ is a product of two Weyl coefficients.
Cauchy--Schwarz and (Y7), with the normalized measure, bound its
$L^1$ norm by the product of the four vector norms. Apply this bound to finite sums of rank-one operators and take the infimum over both projective tensor representations. Trace-norm completion and completeness of $L^1$ then give

$$
\|T*S\|_{L^1}\leq\|T\|_1\|S\|_1,\qquad
F_\omega(T*S)=Q_TQ_S,\qquad
Q_{f*T}=(F_\omega f)Q_T.
\tag{Y22e}
$$

Here is a direct sign and normalization check for the middle identity.
For finite-rank Schwartz operators with kernels $K_T,K_S$, the
convolution is

$$
(T*S)(s,t)=\int_{\mathbb R^2}
 K_T(r,u)e^{it(u-r)}K_S(-u-s,-r-s)\,dr\,du.
\tag{Y22f}
$$

For fixed $s$, write (Y22f) as $\int H_s(v)e^{itv}\,dv$, where
$H_s(v)=\int K_T(r,r+v)K_S(-r-v-s,-r-s)\,dr$.
This is a Schwartz function of $(s,v)$. Taking $F_\omega$ at $(a,b)$,
one-dimensional Fourier inversion evaluates $H_s$ at $a$; this
justifies $u=r+a$ without exchanging a nonintegrable oscillatory
integrand by Fubini. Put $v=-r-s$ in the remaining integral. The result
is the product

$$
\left(\int K_T(r,r+a)e^{-ib(r+a/2)}\,dr\right)
\left(\int K_S(v-a,v)e^{-ib(v-a/2)}\,dv\right)
=Q_T(a,b)Q_S(a,b).
\tag{Y22g}
$$

All the functions in this calculation are Schwartz, so inversion is
valid before the trace-norm approximation. The norm bound in (Y22e)
and the uniform bound for $Q$ extend the identity to arbitrary
trace-class operators. The last identity in (Y22e) follows directly
by pairing the trace-norm integral with $D(w)^*$.

Classical Fourier injectivity and (Y22a) now prove associativity of
these convolutions: both parenthesizations of three trace-class factors
have transform $Q_TQ_SQ_R$. The same verification covers mixed
classical and trace-class factors. Also $T*S=S*T$; cyclicity of trace
and $JD(z)J=D(-z)$ give this directly.

**A Gaussian recovers the trace-class subspace.** Let
$g_0(r)=\pi^{-1/4}e^{-r^2/2}$ and $G=\Theta_{g_0,g_0}$. Completing
the square in (Y22b) gives

$$
Q_G(w)=e^{-|w|^2/4},\qquad
F_\omega(G*G)(w)=e^{-|w|^2/2}.
\tag{Y22h}
$$

The classical ideal $(G*G)*L^1$ is dense in $L^1$. To prove this
specific assertion, take a Schwartz function $h$ whose Fourier
transform is smooth and compactly supported. Dividing that transform
by the nowhere-zero Gaussian in (Y22h) gives another smooth compactly
supported function; its inverse transform $b$ is Schwartz, and
$h=(G*G)*b$. Such $h$ are dense in $L^1$: first approximate by
Schwartz functions, then multiply their Schwartz transforms by smooth
cutoffs equal to one on expanding balls. The inverse transforms
converge in the Schwartz topology, hence in $L^1$. No unrestricted
spectral-synthesis or Wiener-density assertion is used here.

Let $\mathcal M$ be a norm-closed conjugation-invariant trace-class
subspace, and define

$$
\mathcal I_{\mathcal M}
=\overline{\operatorname{span}\{T*S:
       T\text{ trace class},\ S\in\mathcal M\}}^{L^1}.
\tag{Y22i}
$$

Covariance makes this a closed translation-invariant classical
subspace. It is an ideal: convolution by a classical kernel is a
Bochner integral of translates, hence preserves it. Likewise
$f*S\in\mathcal M$ for $S\in\mathcal M$. Associativity gives
$T*(R*S)=(T*R)*S\in\mathcal M$, so

$$
\overline{\operatorname{span}
   \{T*f:T\text{ trace class},\ f\in\mathcal I_{\mathcal M}\}}^{\|\cdot\|_1}
=\mathcal M.
\tag{Y22j}
$$

For the reverse inclusion, approximate a classical approximate
identity in $L^1$ by kernels $(G*G)*b$. Acting on $S\in\mathcal M$,
these kernels approach $S$ in trace norm. Their actions equal
$G*(G*(b*S))$, whose inner classical factor is in
$\mathcal I_{\mathcal M}$. This proves the missing inclusion in
(Y22j). Formula (Y22e) and the nonvanishing $Q_G$ also show that the
common Fourier zero set of $\mathcal I_{\mathcal M}$ is exactly the
common zero set of the $Q_S$ for $S\in\mathcal M$.

**Classical closed-subgroup synthesis.** We prove
$j(L)=I(L)$ in the Euclidean Fourier algebra for every closed
subgroup $L\leq\mathbb R^2$, using the ideals of lesson 17.
The symplectic Fourier transform differs from the ordinary one by
an invertible linear change of frequency coordinates, which
preserves this assertion.

First a point is a synthesis set in $\mathbb R^m$; the case $m=0$
has zero vanishing ideal and is immediate.
Choose $\chi\in C_c^\infty(\mathbb R^m)$ equal to one near zero,
and let $b_\varepsilon$ be the inverse transform of
$\chi(\,\cdot/\varepsilon)$. Scaling gives uniformly bounded
$L^1$ norms and
$\|\tau_yb_\varepsilon-b_\varepsilon\|_1\to0$ for every fixed $y$.
For a mean-zero $a\in L^1$, its convolution is the actual
$L^1$ Bochner integral

$$
a*b_\varepsilon
=\int a(y)(\tau_yb_\varepsilon-b_\varepsilon)\,dy
\longrightarrow0\quad\text{in }L^1.
\tag{Y22k}
$$

The convergence follows by dominated convergence and the uniform
norm bound. Consequently $(Fa)(1-\chi(\,\cdot/\varepsilon))$
approaches $Fa$ in Fourier-algebra norm and vanishes near zero.
Multiplication by smooth expanding Fourier cutoffs then makes each
approximant compactly supported without losing that vanishing.
Modulation shifts the same proof to any point.

Every affine plane $V\times\{\lambda\}$ in
$\mathbb R^d\times\mathbb R^m$ is therefore a synthesis set.
Indeed, restriction of a Fourier transform to that plane is the
Fourier transform of the bounded map

$$
r_\lambda a(u)=\int a(u,v)e^{iv\cdot\lambda}\,dv.
\tag{Y22l}
$$

Choose $\rho\in L^1(\mathbb R^m)$ with
$\int\rho(v)e^{iv\cdot\lambda}\,dv=1$.
The map $a\mapsto(r_\lambda a)\otimes\rho$ is a bounded
projection. Approximate an element of $\ker r_\lambda$ by finite
separated sums in $L^1(\mathbb R^{d+m})$, then apply one minus this
projection. The resulting sums have transverse factors of zero
$\lambda$-evaluation. The point-synthesis proof approximates each
such factor by a compact Fourier function vanishing near
$\lambda$; compact Fourier approximation of the other factors
completes the affine-plane synthesis proof. Fourier injectivity
identifies $\ker r_\lambda$ with the full vanishing ideal of the
plane. The cases $d=0$ and $m=0$ are included, with the latter
full-plane vanishing ideal equal to zero.

To handle $L$, choose a vector subspace $V\subset L$ of maximal
dimension. Orthogonal projection gives
$L=V+\Lambda$, where $\Lambda=L\cap V^\perp$ is closed and
discrete. For if nonzero $\lambda_n\in\Lambda$ tended to zero,
a subsequence of their unit directions would converge to a unit
vector $v\in V^\perp$. For every real $t$, suitable integer
multiples of $\lambda_n$ converge to $tv$, so closedness would
put the line $\mathbb Rv$ in $L$, contradicting maximality.

Write the frequency coordinates as $(u,v)\in V\times V^\perp$.
Every smooth compact cutoff in just one coordinate block acts as
a bounded Fourier-algebra multiplier, because it convolves the
inverse kernel in that block with an $L^1$ kernel. Thus the
expressions $1\otimes\eta_R$ and $1\otimes u_\lambda$ below do not
require the constant function to belong to the full Fourier algebra.
For $f\in I(L)$, multiply in the transverse variable by smooth
compact cutoffs $\eta_R(v)=\eta(v/R)$ with $\eta=1$ near zero.
Their inverse kernels are an approximate identity in that
variable, so $f_R=(1\otimes\eta_R)f\to f$ in Fourier-algebra
norm. Only finitely many points of $\Lambda$ meet
$\operatorname{supp}\eta_R$.

Choose disjoint smooth transverse cutoffs $u_\lambda$, equal to
one near these finitely many points and supported in neighborhoods
containing no other lattice points. Each
$(1\otimes u_\lambda)f_R$ vanishes on
$V\times\{\lambda\}$. Approximate it by the affine-plane result,
then multiply the approximants by a slightly larger cutoff equal
to one on $\operatorname{supp}u_\lambda$ and still avoiding all
other lattice points. They are compact Fourier functions whose
supports miss the whole of $L$. Hence each localized piece is in
$j(L)$. The remainder
$(1-\sum_\lambda1\otimes u_\lambda)f_R$ has compact transverse
support disjoint from $\Lambda$. Expanding compact cutoffs in the
$V$ variable approximate it in norm by compact Fourier functions
with supports disjoint from $L$, so it too belongs to $j(L)$.
Thus $f_R\in j(L)$, and closedness gives $f\in j(L)$.
This proves subgroup synthesis.

**Finish the Weyl synthesis proof.** Take
$\mathcal M=N_\perp$. Its classical ideal has common zero set
$L_N$. The Euclidean local ideal inclusion just proved,
together with the preceding subgroup proof and the definitions (TC4), implies that its Fourier image is exactly $I(L_N)$.
If a trace-class $S$ has $Q_S|_{L_N}=0$, then
$G*S\in\mathcal I_{\mathcal M}$ by (Y22e).
Approximate a classical approximate identity by $(G*G)*b$ once
again. Its action on $S$ equals
$G*(b*(G*S))$, which lies in $\mathcal M$ by (Y22j).
Taking the trace-norm limit puts $S$ in $\mathcal M$.
The opposite inclusion is the definition of the common zero set.
Since $Q_S$ and $\mathcal W_S$ have identical zeros, we obtain

$$
N_\perp
=\{S\in\mathcal T(\mathcal H):
\mathcal W_S(w)=0\text{ for every }w\in L_N\}.
\tag{Y23}
$$

This Gaussian argument supplies the exact correspondence and subgroup
synthesis needed in
[Werner's Corollary 4.4(1), (4), (5)](https://wiki.math.ntnu.no/_media/ma8107/2024h/werner_-_quantuysis_on_phase_spacem_harmonic_anal.pdf),
printed page 1409. The trace-class convolution identities correspond to
Propositions 3.2 and 3.4, printed pages 1405–1407. Its proof uses
classical Wiener approximation; the proof here uses explicit Gaussian
division on compact smooth Fourier supports. The Euclidean subgroup
argument above supplies the synthesis step directly.

Taking annihilators in (Y23) gives (Y20). To prove (Y21), set
$C=\{W(w):w\in L\}'$. The character formula (Y6) makes $C$
$\alpha$-invariant. It also shows that $W(z)\in C$ holds exactly when
$z\in L^{\perp_\omega}$. Applying (Y20) to $C$ proves (Y21).
The same synthesis argument applies to this commutant because it is a unital ultraweakly closed algebra invariant under every $\alpha_z$.

**Euclidean double annihilators.** The remaining subgroup identity can
also be proved here. For the decomposition $L=V+\Lambda$ obtained above,
put $E=\operatorname{span}_{\mathbb R}\Lambda\subset V^\perp$.
The discrete subgroup $\Lambda$ has a lattice basis in $E$.
We give the argument in the dimensions at issue, rather than importing
an arbitrary-group duality theorem.

If $\Lambda\ne\{0\}$, choose a shortest nonzero $\lambda_1\in\Lambda$.
It exists because a closed discrete subset has finite intersection with
every compact set. On the line $\mathbb R\lambda_1$, subtracting an
integer multiple of $\lambda_1$ leaves a multiple with coefficient in
$[0,1)$; minimal length makes that remainder zero. Thus
$\Lambda\cap\mathbb R\lambda_1=\mathbb Z\lambda_1$. This settles
$\dim E=1$.

If $\dim E=2$, project $\Lambda$ onto the line perpendicular to
$\lambda_1$ within $E$. Zero is isolated in the projected subgroup.
Otherwise choose nonzero projected values tending to zero, and
subtract integer multiples of $\lambda_1$ from their lifts so that
their coordinates along $\lambda_1$ lie in $[0,\|\lambda_1\|)$.
The reduced lifts lie in a fixed compact rectangle. Its intersection
with $\Lambda$ is finite, which is incompatible with those nonzero
projected values tending to zero. A nonzero subgroup of $\mathbb R$
with zero isolated is $d\mathbb Z$ for a least positive $d$:
distinct elements are separated by a fixed positive distance, so
there are only finitely many in any bounded interval; division by
the least positive element leaves zero remainder.
Choose $\lambda_2\in\Lambda$ with projection $d$.
For every $\lambda\in\Lambda$, subtract an integer multiple of
$\lambda_2$ to remove that projection, then an integer multiple of
$\lambda_1$. This proves
$\Lambda=\mathbb Z\lambda_1+\mathbb Z\lambda_2$.
The case $E=\{0\}$ requires no basis.

Let $x\notin L$ and write $x=x_V+x_{V^\perp}$. If
$x_{V^\perp}\notin E$, its nonzero component perpendicular to $E$
gives a vector $p\in V^\perp\cap E^\perp$ with $p\cdot x=\pi$.
This $p$ pairs to zero with $L$. If $x_{V^\perp}\in E$, express it
in the lattice basis. Some coefficient $a_j$ is not an integer.
The dual vector $p_j\in E$ satisfying
$p_j\cdot\lambda_i=2\pi\delta_{ji}$ pairs with every member of $L$
in $2\pi\mathbb Z$, while $p_j\cdot x=2\pi a_j\notin2\pi\mathbb Z$.
Thus in every case an ordinary Euclidean character separates $x$
from $L$.

For the symplectic convention (Y6), set $J_0(s,t)=(-t,s)$, a
rotation of the plane distinct from the parity operator $J$ in
(Y22c). Then $\omega(z,w)=J_0z\cdot w$. If $p$ is a separating
vector just found, $w=J_0^{-1}p$ belongs to $L^{\perp_\omega}$ and
$\omega(x,w)=-p\cdot x\notin2\pi\mathbb Z$. Alternation gives the
opposite inclusion for elements of $L$. We have therefore proved

$$
(L^{\perp_\omega})^{\perp_\omega}=L
\quad\text{for every closed }L\le\mathbb R^2.
\tag{Y23a}
$$

Now let $H\le\mathbb R^2$ be closed.  By (Y21),

$$
B(\mathcal H)^{\alpha|_H}
=\{W(h):h\in H\}'
=\{W(w):w\in H^{\perp_\omega}\}''.
\tag{Y24}
$$

Conversely, if $N$ is invariant, put $H=L_N^{\perp_\omega}$. The locally
proved identity (Y23a) and (Y20) give

$$
N=\{W(w):w\in L_N\}''
=B(\mathcal H)^{\alpha|_H}.
\tag{Y25}
$$

The subgroup is recovered exactly as

$$
H=\{z:\alpha_z(x)=x\text{ for every }x\in N\},
\tag{Y26}
$$

because (Y6) and $L_N^{\perp_\omega}=H$ test every Weyl generator of $N$.
Thus

$$
\boxed{
H\longmapsto B(\mathcal H)^{\alpha|_H}
\text{ is an order-reversing bijection}}
\tag{Y27}
$$

from closed subgroups of $\mathbb R^2$ to unital $\alpha$-invariant von
Neumann subalgebras.

<a id="weylplane-continuous"></a>

## The printed compact-operator equality is false

Let

$$
B(\mathcal H)_c
=\{x\in B(\mathcal H):
\|\alpha_z(x)-x\|\longrightarrow0\text{ as }z\to0\}.
\tag{Y28}
$$

The proposed equality $B(\mathcal H)_c=K(\mathcal H)$ cannot hold.  First,

$$
1\in B(\mathcal H)_c\setminus K(\mathcal H).
\tag{Y29}
$$

More structurally, (Y6) gives

$$
\|\alpha_z(W(w))-W(w)\|
=|e^{i\omega(z,w)}-1|\longrightarrow0.
\tag{Y30}
$$

Every $W(w)$ is therefore in the continuous part, while a unitary on the
infinite-dimensional space $L^2(\mathbb R)$ is not compact.  These
examples disprove the equality in Takesaki's Exercise XI.2.5(e). The strict inclusion and convolution characterization below describe the continuous part.

<a id="weylplane-convolution"></a>

## Convolution exactly characterizes the continuous part

For $f\in L^1(\mathbb R^2)$ and $x\in B(\mathcal H)$, define the ultraweak
integral

$$
\alpha_f(x)=\int_{\mathbb R^2}f(z)\alpha_z(x)\,dz.
\tag{Y31}
$$

Normal-functional testing gives
$\|\alpha_f(x)\|\le\|f\|_1\|x\|$.  If
$(\tau_hf)(z)=f(z-h)$, invariance of Haar measure gives

$$
\alpha_h(\alpha_f(x))=\alpha_{\tau_hf}(x),
\qquad
\|\alpha_h(\alpha_f(x))-\alpha_f(x)\|
\le\|\tau_hf-f\|_1\|x\|.
\tag{Y32}
$$

Translation is norm continuous on $L^1$, so every convolution in (Y31)
belongs to $B(\mathcal H)_c$.  Conversely, let $(k_i)$ be a nonnegative
$C_c(\mathbb R^2)$ approximate identity with integral one and supports
shrinking to $0$.  For $x\in B(\mathcal H)_c$,

$$
\|\alpha_{k_i}(x)-x\|
\le\int k_i(z)\|\alpha_z(x)-x\|\,dz
\longrightarrow0.
\tag{Y33}
$$

We obtain the characterization

$$
\boxed{
B(\mathcal H)_c
=\operatorname{cl}_{\|\cdot\|}
\{\alpha_f(x):f\in C_c(\mathbb R^2),\ x\in B(\mathcal H)\}.}
\tag{Y34}
$$

Finally, the valid compact-operator inclusion follows directly.  For rank-one
operators,

$$
\alpha_z(\Theta_{\xi,\eta})
=\Theta_{W(z)\xi,W(z)\eta}
\tag{Y35}
$$

and

$$
\|\Theta_{\xi,\eta}-\Theta_{\xi',\eta'}\|
\le
\|\xi-\xi'\|\,\|\eta\|
+\|\xi'\|\,\|\eta-\eta'\|.
\tag{Y36}
$$

Strong continuity of $W$ makes every finite-rank orbit norm continuous.
Automorphisms are isometric, so norm closure gives

$$
\boxed{K(\mathcal H)\subsetneq B(\mathcal H)_c.}
\tag{Y37}
$$

**Problem.** Why does point-strong continuity of $z\mapsto W(z)$ not make
$z\mapsto\alpha_z(x)$ norm continuous for every $x\in B(\mathcal H)$?

**Solution.** Strong convergence of unitaries is uniform on each fixed
finite-dimensional range, which proves (Y35) for finite-rank operators, but
it is not uniform on the unit ball of an infinite-dimensional Hilbert space.
For an explicit example, let $P$ be multiplication by $1_{[0,\infty)}$.
Modulations commute with $P$, whereas $\alpha_{(s,0)}(P)$ is multiplication
by $1_{[-s,\infty)}$. For every $s\ne0$ the two indicator functions differ
by absolute value $1$ on an interval of positive measure, so
$\|\alpha_{(s,0)}(P)-P\|=1$, although $U_s\to1$ strongly as $s\to0$.
The $L^1$ regularization in (Y31)–(Y34) identifies exactly the operators for
which norm continuity does hold. $\square$

The source locator is Takesaki, *Theory of Operator Algebras II*, Exercise
XI.2.5, on printed page 351. Equations (Y1)–(Y17) prove clauses
(a)–(c); (Y18)–(Y27), including the Gaussian correspondence and
Euclidean subgroup proof (Y22c)–(Y22l), derive clause (d).
Equations (Y28)–(Y30) diagnose clause (e) as printed, while (Y31)–(Y37) give
the exact continuous-part replacement and retain the valid compact-operator
inclusion. The trace-class facts used in the subgroup proof are constructed in (TC1)–(TC3), and its Fourier ideal conventions are (TC4).
