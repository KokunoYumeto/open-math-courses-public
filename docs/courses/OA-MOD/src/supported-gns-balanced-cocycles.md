# Supported GNS representations and the balanced cocycle

**Self-checked by the writing AI.**

A support projection cuts a corner out of the algebra. Its GNS representation must then be extended by the whole algebra if it is to represent the original weight. We first construct that extension by a matrix of inner products. Next, a weight on two-by-two matrices puts two modular groups on the diagonal and their comparison in an off-diagonal entry. The mixed strip condition and its exact uniqueness argument follow from this construction.

The source antecedents are Takesaki, *Theory of Operator Algebras II*, VIII.3, Theorem 3.2, Theorem 3.3, Definition 3.4 and Lemma 3.5. The balanced-weight input is Lemma 3.1. Hilbert spaces, index sets and normal semifinite weights have arbitrary cardinality; the zero algebra and zero numerator weight are allowed where stated. Inner products are linear in the first variable.

Exact previously written inputs are WF-04 for normal semicyclic representations; WS-04–06 for null and support projections; WG-008 for finite positive contraction nets; WH-09–11 for the full finite-star Hilbert algebra; MF-06–09 for modular covariance and the maximal entire algebra; SF-05 and SE-03/10/11 for weight standard forms, arbitrary supported corners, equivalence and normal-functional representatives; TC-04–05 for the closed involution and its adjoint; SK-05/08 for spectral powers and transported domains; and MA-08/14 for bounded strips, uniqueness and vector holomorphy. These are named proof inputs; their proofs and foundations are not given here.

## The supported corner inside a semicyclic representation

Let \(\varphi\) be a faithful normal semifinite weight on \(M\), and identify \(M\) with its faithful normal GNS image on \(H=H_\varphi\). Write its standard form as \((M,H,J,P)\). Let \(\psi\) be any normal semifinite weight and let \(e=s(\psi)\). The support identities of WS give

\[
\psi(a)=\psi(eae)\quad(a\in M_+),\qquad
N_\psi=M(1-e),\qquad
\Lambda_\psi(x)=\Lambda_\psi(xe)\quad(x\in\mathfrak n_\psi).
\tag{GC.1}
\]

The restriction \(\psi_e\) to \(eMe\) is faithful, normal and semifinite. This last assertion uses semifiniteness of \(\psi\); a general normal weight's faithful restriction need not be semifinite.

Put \(p=\pi_\psi(e)\). Inclusion of the finite ideal of the corner induces a unitary

\[
I:H_{\psi_e}\longrightarrow pH_\psi,\qquad
I\Lambda_{\psi_e}(b)=\Lambda_\psi(b)\quad(b\in\mathfrak n_{\psi_e}).
\tag{GC.2}
\]

It intertwines the representations of \(eMe\).

**Proof.** Norms and inner products agree because the restricted weight agrees on corner products. Every vector \(p\Lambda_\psi(x)=\Lambda_\psi(ex)\) equals \(\Lambda_\psi(exe)\) by (GC.1). The element \(exe\) is in \(\mathfrak n_{\psi_e}\): \(ex\) is finite by the left-ideal property, and its difference from \(exe\) is null. Thus the image of the initial isometry is dense in \(pH_\psi\), proving the onto extension. Multiplication proves intertwining. When \(e=0\), both spaces are zero. \(\square\)

SE-03 makes

\[
f=JeJ\in M',\qquad K_e=efH,
\tag{GC.3}
\]

a faithful standard-form space for \(eMe\). SF-05 and SE-10 therefore supply a unitary \(V_e:H_{\psi_e}\to K_e\) intertwining \(eMe\) and transporting the corner cone and conjugation. Define \(T_e=V_e I^{-1}\) on \(pH_\psi\). Its domain and target are supported *corner* spaces, not yet the whole GNS module.

## Extending the corner map by an exact Gram identity

The prescription

\[
U\left(\sum_{j=1}^n\pi_\psi(a_j)\zeta_j\right)
 =\sum_{j=1}^n a_jT_e\zeta_j,
\qquad a_j\in M,\quad\zeta_j\in pH_\psi,
\tag{GC.4}
\]

extends uniquely to an isometry from \(H_\psi\) onto \(fH\). It intertwines every element of \(M\). Thus, with

\[
\eta(x)=U\Lambda_\psi(x),
\tag{GC.5}
\]

one has

\[
\eta(ax)=a\eta(x),\qquad
\langle\eta(x),\eta(y)\rangle=\psi(y^*x),\qquad
\overline{\eta(\mathfrak n_\psi)}=JeJH.
\tag{GC.6}
\]

If \(\psi\) is faithful, \(e=1\), so \(U\) is an onto unitary to \(H_\varphi\). Every \(\omega\in M_*^+\) is represented by a vector in \(H_\varphi\); in fact SE-11 chooses its unique representative in \(P\), of squared norm \(\omega(1)\).

**Proof of well-definedness.** Let \(A\) be the row with entries \(a_j\), and let \(B\) be the matrix with entries \(ea_i^*a_je\). It is positive. For vectors in the corner, its quadratic form computes the squared norm of the corresponding row sum. The direct sum of \(T_e\)'s intertwines every entry of \(B\). Consequently

\[
\left\|\sum_j\pi_\psi(a_j)\zeta_j\right\|^2
 =\sum_{i,j}\langle\pi_\psi(ea_i^*a_je)\zeta_j,\zeta_i\rangle
 =\left\|\sum_j a_jT_e\zeta_j\right\|^2.
\tag{GC.7}
\]

Zero row sums therefore have zero image. This proves both well-definedness and the isometry, with no choice of a countable decomposition.

**Proof of density and the exact range.** The central support \(c(e)\) is the join of \(ueu^*\) over all unitaries \(u\in M\). To verify this description, that join is invariant under all unitary conjugations, hence central, and is the least central projection dominating \(e\). A self-adjoint contraction is the real part of a unitary, so invariance under all unitaries indeed implies centrality. The closed span of \(M(eL)\) in any normal representation on \(L\) is therefore the range of the represented \(c(e)\).

On \(H_\psi\), \(\pi_\psi(1-c(e))=0\): for a finite \(x\), centrality and (GC.1) give \(\Lambda_\psi((1-c(e))x)=0\). Normality of \(\pi_\psi\) sends the join just described to the join of the represented projections. Thus the finite sums in (GC.4) are dense in \(H_\psi\).

On the target, \(f\) commutes with \(M\), and

\[
\overline{M(efH)}=c(e)fH=fH.
\tag{GC.8}
\]

The last equality follows from \(e\le c(e)\) and the standard-form central identity \(Jc(e)J=c(e)\), which imply \(f\le c(e)\). Hence the completed isometry has exactly the asserted range. Left multiplication in (GC.4) proves algebra intertwining first on finite sums and then everywhere. The covariance and inner-product identities in (GC.6) follow from the original semicyclic representation. This proves every assertion of VIII.3.2, including its nonfaithful case and the functional-vector conclusion. \(\square\)

## A balanced weight and its four exact domains

Now let both \(\varphi\) and \(\psi\) be faithful normal semifinite. On \(N=M_2(M)\) put

\[
\Omega(X)=\varphi(X_{11})+\psi(X_{22})\quad(X\in N_+).
\tag{GC.9}
\]

This is faithful, normal and semifinite. Its finite left ideal and finite-star algebra have the entrywise descriptions

\[
\begin{aligned}
X\in\mathfrak n_\Omega
&\iff X_{i1}\in\mathfrak n_\varphi,
       \ X_{i2}\in\mathfrak n_\psi\quad(i=1,2),\\
\mathfrak a_\Omega
&=\begin{pmatrix}
\mathfrak a_\varphi&I\\
I^*&\mathfrak a_\psi
\end{pmatrix},\qquad
I=\mathfrak n_\varphi^*\cap\mathfrak n_\psi.
\end{aligned}
\tag{GC.10}
\]

These are statements about vector spaces of matrices; no assertion that the off-diagonal space is a two-sided ideal is intended.

**Proof.** Additivity, homogeneity and increasing-net normality follow from the two diagonal weights. If a positive matrix has zero weight, both diagonal entries vanish by faithfulness, so its positive square root has both columns zero and the matrix is zero. Finite positive contraction nets \(r_i\) and \(s_j\) for the two weights give \(\operatorname{diag}(r_i,s_j)\uparrow1_N\) with finite \(\Omega\)-value. WG-008 proves semifiniteness, including the possible infinite value at \(1_N\). Finally

\[
\Omega(X^*X)
 =\sum_i\varphi(X_{i1}^*X_{i1})
  +\sum_i\psi(X_{i2}^*X_{i2}).
\tag{GC.11}
\]

The column criterion and its intersection with the adjoint criterion give (GC.10). \(\square\)

Let \(\alpha_t=\sigma_t^\Omega\) and let \(E_{ij}\) denote the matrix units with entry \(1_M\). Then

\[
\alpha_t(E_{ii})=E_{ii},\qquad
\alpha_t(xE_{11})=\sigma_t^\varphi(x)E_{11},\qquad
\alpha_t(xE_{22})=\sigma_t^\psi(x)E_{22}.
\tag{GC.12}
\]

Here is a domain proof of the diagonal identities. The four GNS entry spaces are mutually orthogonal by (GC.11). The initial involution sends the \(ij\) entry space to the \(ji\) entry space, with its exact domain from (GC.10). Orthogonal entry projections preserve its graph; after graph closure the same decomposition holds for \(S_\Omega\) and its antilinear adjoint. Hence \(\Delta_\Omega=S_\Omega^*S_\Omega\) and its spectral powers preserve each entry space. The two diagonal blocks are exactly the closed involutions and modular operators of \(\varphi\) and \(\psi\). The GNS left projection associated with \(E_{ii}\) is the sum of the two row projections and commutes with these powers. Modular implementation and faithfulness of \(\pi_\Omega\) prove (GC.12). The diagonal restrictions follow from the corresponding diagonal blocks and the same faithfulness. This uses graph invariance, not just Hilbert-space density of the entries.

## Reading a unitary cocycle from one matrix unit

Because \(\alpha_t\) fixes the diagonal matrix units, there is a unique \(u_t\in M\) with

\[
\alpha_t(E_{12})=u_tE_{12}.
\tag{GC.13}
\]

Multiplication of this identity with its adjoint gives \(u_tu_t^*=u_t^*u_t=1\). Define the off-diagonal map \(\tau_t\) by \(\alpha_t(xE_{12})=\tau_t(x)E_{12}\). Factoring the matrix in its two possible ways gives

\[
\tau_t(x)=u_t\sigma_t^\psi(x)=\sigma_t^\varphi(x)u_t.
\tag{GC.14}
\]

The group identity for \(\alpha\), applied to \(E_{12}\), now gives

\[
u_0=1,\qquad u_{s+t}=u_s\sigma_s^\psi(u_t),\qquad
\sigma_t^\varphi(x)=u_t\sigma_t^\psi(x)u_t^*.
\tag{GC.15}
\]

The family \(u\) is pointwise sigma-strong* continuous: \(\alpha\) has that continuity, and extracting a fixed matrix entry is a normal bounded corner operation. It is therefore also sigma-strong continuous as stated in VIII.3.3. Invariance of \(\mathfrak a_\Omega\) gives the exact mixed-domain equality

\[
u_t\sigma_t^\psi(I)=I.
\tag{GC.16}
\]

The reverse inclusion follows by applying \(\alpha_{-t}\) to the same entry, rather than from a density argument.

## The mixed strip has finite values at both boundaries

For \(x\in I^*=\mathfrak n_\varphi\cap\mathfrak n_\psi^*\) and \(y\in I\), there is a bounded continuous scalar \(F_{x,y}\) on \(0\le\operatorname{Im}z\le1\), holomorphic in its interior, with

\[
\begin{aligned}
F_{x,y}(t)&=\varphi(u_t\sigma_t^\psi(y)x),\\
F_{x,y}(t+i)&=\psi(xu_t\sigma_t^\psi(y)).
\end{aligned}
\tag{GC.17}
\]

Each complex weight value denotes its finite linear extension on its own definition algebra.

**Proof.** Apply KM-02 to the balanced weight and to \(A=yE_{12}\), \(B=xE_{21}\), which are in \(\mathfrak a_\Omega\) by (GC.10). The products \(\alpha_t(A)B\) and \(B\alpha_t(A)\) have only the \(11\) and \(22\) entries respectively, so the two KMS boundaries are exactly (GC.17). Condition (GC.16) also checks their finite domains directly. The uniform bound is

\[
\|F_{x,y}\|_\infty\le
\max\{\varphi(yy^*)^{1/2}\varphi(x^*x)^{1/2},
        \psi(y^*y)^{1/2}\psi(xx^*)^{1/2}\}.
\tag{GC.18}
\]

For the first boundary use (GC.14), so \(\varphi(\tau_t(y)\tau_t(y)^*)=\varphi(yy^*)\); for the second, unitarity gives \(\psi(\tau_t(y)^*\tau_t(y))=\psi(y^*y)\). Cauchy–Schwarz and MA-08 give (GC.18). No finite mass at the identity has been assumed. \(\square\)

## A bounded-energy strip identifies a modular trajectory

Let \(\theta\) be a faithful normal semifinite weight, and let \(y(t)\in\mathfrak a_\theta\) be sigma-weakly continuous, with

\[
\sup_{t\in\mathbb R}\{
 \theta(y(t)^*y(t))+\theta(y(t)y(t)^*)\}<\infty.
\tag{GC.19}
\]

Suppose that for every \(x\in\mathfrak a_\theta\) a bounded continuous holomorphic strip function has boundaries

\[
F_x(t)=\theta(y(t)x),\qquad F_x(t+i)=\theta(xy(t)).
\tag{GC.20}
\]

Then \(y(t)=\sigma_t^\theta(y(0))\) for every real \(t\).

**The imaginary shift.** Write \(S=J\Delta^{1/2}\), \(F=S^*=J\Delta^{-1/2}\), and let \(a\) belong to the maximal entire algebra of MF-07. For any \(b\in\mathfrak a_\theta\), the antilinear adjoint identity gives

\[
\begin{aligned}
\theta(b\sigma_{-i}^\theta(a))
 &=\langle\Delta\Lambda(a),S\Lambda(b)\rangle\\
 &=\langle\Lambda(b),F\Delta\Lambda(a)\rangle
  =\langle\Lambda(b),S\Lambda(a)\rangle
  =\theta(ab).
\end{aligned}
\tag{GC.21}
\]

All powers are defined because \(\Lambda(a)\) has every spectral-power domain. In particular the shift is \(-i\), with the upper-strip convention used here.

**Bounded dependence on the test vector.** Put \(C^2\) equal to the supremum in (GC.19). Cauchy–Schwarz at the two boundaries gives

\[
|F_x(t)|\le C\|\Lambda(x)\|,\qquad
|F_x(t+i)|\le C\|S\Lambda(x)\|.
\tag{GC.22}
\]

Boundary uniqueness makes \(x\mapsto F_x\) linear. The maximum principle therefore extends it to a bounded linear map from the graph-norm completion of \(\Lambda(\mathfrak a_\theta)\), which is \(D(\Delta^{1/2})\) by WH-10–11, into the Banach space of bounded continuous holomorphic strip functions. Uniform limits in this space retain holomorphy by MA-14's scalar uniform-limit argument.

**Moving the test rather than the unknown curve.** Fix an entire \(a\). The map \(z\mapsto\Delta^{iz}\Lambda(a)\) is entire in the graph norm of \(\Delta^{1/2}\) and uniformly bounded on each finite horizontal strip, by MF-07. Consequently

\[
f(z)=F_{\sigma_z^\theta(a)}(z)
\tag{GC.23}
\]

is holomorphic inside the strip, continuous on it and bounded there. To justify the diagonal evaluation, the preceding bounded linear map makes the test dependence holomorphic in the supremum norm; local Cauchy estimates for its values make evaluation at the same parameter holomorphic. Its two boundaries agree, because (GC.21) gives

\[
f(t+i)=\theta(\sigma_{t+i}^\theta(a)y(t))
       =\theta(y(t)\sigma_t^\theta(a))=f(t).
\tag{GC.24}
\]

Glue translated strips along their equal continuous edges. Morera's theorem gives an entire function; the strip bound and imaginary periodicity give a global bound. Liouville's theorem makes it constant. Weight invariance on the finite linear domain yields

\[
\theta((\sigma_{-t}^\theta(y(t))-y(0))a)=0
\quad\text{for every entire }a.
\tag{GC.25}
\]

This value is \(\langle\Lambda(a),S\Lambda(\sigma_{-t}(y(t))-y(0))\rangle\). Entire vectors are dense by MF-08–09, so the second vector is zero. The closed involution has zero kernel by TC-05; faithfulness of \(\theta\) then makes the algebra element zero. This proves the assertion, including all domains and the source's sigma-weak continuity hypothesis. No operator-norm bound on \(y(t)\) was inferred from (GC.19). \(\square\)

## Mixed trajectory recognition and uniqueness

Let \(y(t)\in I\) be sigma-strongly continuous, with

\[
\sup_t\varphi(y(t)y(t)^*)<\infty,\qquad
\sup_t\psi(y(t)^*y(t))<\infty.
\tag{GC.26}
\]

If each \(x\in I^*\) has a bounded holomorphic strip function with lower boundary \(\varphi(y(t)x)\) and upper boundary \(\psi(xy(t))\), then

\[
y(t)=\tau_t(y(0))=u_t\sigma_t^\psi(y(0)).
\tag{GC.27}
\]

**Proof.** Set \(Y(t)=y(t)E_{12}\) in \(N\). It is in \(\mathfrak a_\Omega\) and satisfies (GC.19), with its two energies exactly the two in (GC.26). For an arbitrary \(X\in\mathfrak a_\Omega\), the diagonal values of \(Y(t)X\) and \(XY(t)\) use only \(X_{21}\in I^*\). Thus the assumed mixed functions give (GC.20) for every such \(X\), not merely a selected matrix corner. Apply GC-06 and then (GC.14). \(\square\)

This is both parts of VIII.3.5, with the normal semifinite setting in which the modular groups are defined. It also proves uniqueness of the cocycle satisfying all four conditions (GC.15–17). Indeed, let \(v_t\) be another continuous unitary family with those conditions. Its cocycle law forces \(v_0=1\). For a fixed \(y\in I\), put \(y_v(t)=v_t\sigma_t^\psi(y)\). The mixed-domain condition puts it in \(I\), and its energies are constant:

\[
\psi(y_v(t)^*y_v(t))=\psi(y^*y),\qquad
\varphi(y_v(t)y_v(t)^*)=\varphi(yy^*).
\tag{GC.28}
\]

The second identity uses the competing family's modular-intertwining condition. Its mixed boundary condition and GC-07 now give \(v_t\sigma_t^\psi(y)=u_t\sigma_t^\psi(y)\).

The space \(I\) is sigma-strong* dense: for the finite positive contraction nets of GC-03, \(r_i a s_j\in I\) and these bounded elements converge sigma-strong* to \(a\), for every \(a\in M\). Thus equality on \(I\) implies \(v_t=u_t\). This proves uniqueness in the full class specified by the theorem. It does not discard its finite-domain or normalization conditions.

## The derivative theorem and its normalization

For two faithful normal semifinite weights on an arbitrary \(M\), GC-03–07 construct the unique sigma-strongly continuous unitary family satisfying the cocycle law relative to \(\sigma^\psi\), preservation of \(I\), the mixed upper-strip condition (GC.17), and modular intertwining (GC.15). In the numerator-first convention of VIII.3.4, write

\[
(D\varphi:D\psi)_t=u_t.
\tag{GC.29}
\]

The numerator specifies the target modular group; the denominator specifies the group in the cocycle law. The displayed identities hold for every real parameter, not only on analytic algebra elements.

The source says that the mixed condition determines the family. This must be read within the theorem's class of families. The bare strip identity, without the normalization forced by the cocycle law, does not determine a unitary family: in \(M=\mathbb C\) with \(\varphi=\psi\) the usual scalar weight, every constant phase \(v_t=c\), \(|c|=1\), has the bounded constant strip function \(F_{x,y}(z)=cxy\). Only \(c=1\) satisfies the cocycle law. GC-07 proves uniqueness with every stated condition retained; it makes explicit where the finite-energy bounds and the initial value come from. No assertion that two modular groups alone determine a normalized cocycle is used.

## Noncommuting densities give a cocycle, not a unitary group

For \(M=M_2(\mathbb C)\), take

\[
h=\begin{pmatrix}1&0\\0&4\end{pmatrix},\qquad
k=\begin{pmatrix}5&-3\\-3&5\end{pmatrix},\qquad
\varphi(a)=\operatorname{Tr}(ha),\quad
\psi(a)=\operatorname{Tr}(ka).
\tag{GC.30}
\]

The eigenvalues of \(k\) are \(2\) and \(8\), so both weights are faithful. Here every finite ideal is all of \(M\). The family

\[
u_t=h^{it}k^{-it},\qquad
\tau_t(y)=h^{it}yk^{-it}
\tag{GC.31}
\]

satisfies the cocycle law and modular intertwining by direct bounded-matrix multiplication. Its mixed function is

\[
F_{x,y}(z)=\operatorname{Tr}(h^{1+iz}yk^{-iz}x).
\tag{GC.32}
\]

Spectral powers make it entire and bounded on the closed upper strip. At \(z=t+i\), the powers become \(h^{it}\) and \(k^{1-it}\); cyclicity of the finite trace gives the upper boundary \(\operatorname{Tr}(kx h^{it}yk^{-it})\). The lower boundary is the other expression in (GC.17). Uniqueness therefore identifies (GC.31) with the intrinsic cocycle (GC.29).

It is not an ordinary unitary group. Put \(H=\log h\), \(K=\log k\). Then

\[
H=\begin{pmatrix}0&0\\0&\log4\end{pmatrix},\qquad
K=\begin{pmatrix}\log4&-\log2\\ -\log2&\log4\end{pmatrix},\qquad
[H,K]=\begin{pmatrix}0&(\log4)(\log2)\\ -(\log4)(\log2)&0\end{pmatrix}\ne0.
\tag{GC.33}
\]

The first derivative of \(u_t\) at zero is \(i(H-K)\). Its second derivative is \(-H^2-K^2+2HK\), whereas the group with that generator has second derivative \(-H^2-K^2+HK+KH\). Their difference is the nonzero commutator in (GC.33). The twist by \(\sigma^\psi\) in the cocycle law is therefore necessary even in dimension two.

## Three domain and normalization problems

**Problem 1: a corner is smaller than its induced module.** Let \(M=M_2(\mathbb C)\), \(\varphi=\operatorname{Tr}\), and \(\psi(a)=a_{11}\) on positive matrices. Identify the spaces and map in GC-01–02.

**Solution.** The trace standard form is the Hilbert-Schmidt space, with \(JZ=Z^*\) and left multiplication by \(M\). The support is \(e=E_{11}\). The full GNS space of \(\psi\) is \(\mathbb C^2\), by \(\Lambda_\psi(a)=a e_1\), whereas the corner GNS space is one-dimensional. The corner standard-form space is \(eJeJH=\mathbb C E_{11}\). The extension sends a column vector \(v\) to the matrix \(v e_1^*\), isometrically onto \(JeJH=H e\). Left multiplication intertwines the original matrix algebra. Replacing the range by the one-dimensional corner would fail to represent that algebra.

**Problem 2: test the phrase “determined by the strip.”** In the scalar equal-weight model, verify the constant-phase example of GC-08 and isolate the condition that removes it.

**Solution.** Both products have scalar value \(cxy\), so the constant function has the required two boundaries. The cocycle law reduces to \(c=c^2\); unitarity then forces \(c=1\). In particular the initial value is a mathematical condition, not a notational choice that may be omitted when proving uniqueness.

**Problem 3: check the imaginary sign.** For an entire finite-star \(a\) and a finite-star \(b\), verify (GC.21) and explain why replacing \(-i\) by \(+i\) breaks the proof.

**Solution.** The continuation \(\sigma_{-i}(a)\) has GNS vector \(\Delta\Lambda(a)\). The closed antilinear adjoint gives \(F\Delta\Lambda(a)=S\Lambda(a)\), because \(F=J\Delta^{-1/2}\) and \(S=J\Delta^{1/2}\). This proves \(\theta(ab)=\theta(b\sigma_{-i}(a))\). With \(+i\), the vector would be \(\Delta^{-1}\Lambda(a)\), and applying \(F\) would give \(J\Delta^{-3/2}\Lambda(a)\); it is not \(S\Lambda(a)\) in general. The matching edges in (GC.24) require the exact negative imaginary shift.
