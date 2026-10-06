# Adding spatial energies and changing the reference weight

**Self-checked by the writing AI.**

Adding the coefficient energies of two weights is immediate on bounded vectors. Identifying the resulting closed form requires more: those vectors must approximate the joint energy domain. This unit proves a simultaneous approximation theorem and uses it to obtain arbitrary sums, increasing limits and bounded changes of weights, with every finite-energy domain specified.

The source addition assertion is Takesaki, *Theory of Operator Algebras II*, IX.3, Proposition 3.10(ii), for bounded normal positive functionals. The spectral-cutoff method has a further mathematical antecedent in [Hiai, *Concise lectures on selected topics of von Neumann algebras*, arXiv:2004.02383v1, Section 13](https://arxiv.org/abs/2004.02383v1), especially items 13.7–13.14. Here the argument is developed from the existing SC closed forms, scalar normal observations and an explicit form-Cauchy calculation. No source prose or proof text is imported.

## Which objects are being added?

Fix \(M\subseteq B(H)\), put \(N=M'\), and let \(\psi\) be a normal semifinite faithful weight on \(N\). The Hilbert space is arbitrary. Inner products are linear in the first variable. Use the GNS notation \((H_\psi,\pi_\psi,\Lambda_\psi)\) and the bounded-vector space \(D_\psi\) of Conventions and the actual prerequisites. For \(\xi\in D_\psi\),

\[
R_\psi(\xi)\Lambda_\psi(x)=x\xi,
\qquad
\theta_\psi(\xi,\eta)=R_\psi(\xi)R_\psi(\eta)^*,
\quad x\in\mathfrak n_\psi.
\]

For any normal numerator \(\varphi\) on \(M\), SC constructs a closed form \(q_\varphi^\psi\) with domain \(V_\varphi^\psi\). Its Hilbert-space domain closure is \(e_\varphi H\), its null space is \(f_\varphi H\), and

\[
E_\varphi^\psi=D_\psi\cap V_\varphi^\psi
\]

is the exact finite coefficient domain and a form core. Write

\[
Q_\varphi^\psi(\xi)=
\begin{cases}
q_\varphi^\psi[\xi],&\xi\in V_\varphi^\psi,\\
+\infty,&\xi\notin V_\varphi^\psi.
\end{cases}
\tag{SS.1}
\]

Thus \(Q\) is an extended diagonal defined on all of \(H\), whereas \(q\) is a sesquilinear form on its stated linear domain. When the denominator is fixed, suppress its superscript.

The exact inputs are the completed arguments of **SC-02–10**, including positive normal vector-series implementation, bounded-vector density and the initial form's canonical closure; **NW-11**, recovery of a normal weight from dominated normal positive functionals; **WS-02–06**, finite-domain and null projections; and the GNS and bounded-intertwiner facts in WG and SD. The completion test and canonical closure through Cores determine the domain, not just a dense set of vectors supply closure, lower semicontinuity and core criteria. Representation with the exact square-root domain through Nondense forms, lower semicontinuity, and symmetry supply closed-form representation and unitary symmetry. The arbitrary-dimensional spectral calculus used by QF is supplied by **SK-04–09**; bounded polar decomposition is supplied by **BK-07**. These providers retain their explicitly recorded scalar and Hilbert-space inputs. QF-06–08 are used only for the later convergence corollaries. The denominator order comparison uses Comparing two weights and the precise target space.

All these inputs depend on their own foundational prerequisites, which are not proved here. We do not assume a decomposition of an arbitrary normal weight as a sum of vector functionals, a general extended-positive-cone calculus, standard forms, or modular covariance. Only individual bounded normal functionals are decomposed into vector sums, by SC-02.

## Testing an arbitrary vector by an adjoint

For an arbitrary \(\xi\in H\), define a linear operator

\[
T_\xi:\Lambda_\psi(\mathfrak n_\psi)\subseteq H_\psi\longrightarrow H,
\qquad T_\xi\Lambda_\psi(x)=x\xi.
\tag{SS.2}
\]

This domain is dense. Faithfulness of \(\psi\) makes the rule well-defined: if \(\Lambda_\psi(x)=\Lambda_\psi(y)\), then \(\psi((x-y)^*(x-y))=0\), hence \(x=y\). We do not assume that \(T_\xi\) is bounded or closable.

Its adjoint has the precise domain

\[
\begin{split}
D(T_\xi^*)=\{v\in H:\ &\text{there exists }w\in H_\psi\text{ such that}\\
&\langle x\xi,v\rangle=\langle\Lambda_\psi(x),w\rangle
\quad(x\in\mathfrak n_\psi)\},
\end{split}
\tag{SS.3}
\]

and \(T_\xi^*v=w\). Density of the GNS domain makes \(w\) unique. The adjoint is closed: if \(v_n\to v\) and \(T_\xi^*v_n\to w\), passage to the limit in (SS.3) verifies membership and value for \(v\). Its domain can have a proper Hilbert closure. Put

\[
p_\xi=P_{\overline{D(T_\xi^*)}}.
\tag{SS.4}
\]

**Lemma.** The projection \(p_\xi\) belongs to \(M\). On its domain,

\[
T_\xi^*u=\pi_\psi(u)T_\xi^*
\qquad(u\text{ unitary in }N),
\tag{SS.5}
\]

with \(uD(T_\xi^*)=D(T_\xi^*)\). For every \(a\in M\), there is also the exact domain identity

\[
T_{a\xi}^*=T_\xi^*a^*,
\qquad
D(T_{a\xi}^*)=\{v:a^*v\in D(T_\xi^*)\}.
\tag{SS.6}
\]

**Proof.** The finite left ideal is invariant under multiplication by \(N\), so
\(T_\xi\pi_\psi(y)=yT_\xi\) on its initial domain. If \(v\in D(T_\xi^*)\) and \(u\in N\) is unitary, then

\[
\begin{aligned}
\langle x\xi,uv\rangle
&=\langle u^*x\xi,v\rangle\\
&=\langle\pi_\psi(u^*)\Lambda_\psi(x),T_\xi^*v\rangle
=\langle\Lambda_\psi(x),\pi_\psi(u)T_\xi^*v\rangle.
\end{aligned}
\]

This proves (SS.5) and invariance under \(u\); applying it to \(u^*\) gives equality of the domains. Their closure therefore reduces every unitary in \(N\), and hence all of \(N\), since its elements are linear combinations of unitaries. Thus \(p_\xi\in N'=M\).

For \(a\in M\), commutation with \(x\in N\) gives \(T_{a\xi}=aT_\xi\) on exactly the same initial domain. The adjoint test for \(v\) then reads \(\langle T_\xi z,a^*v\rangle=\langle z,w\rangle\). This is precisely the test for \(a^*v\in D(T_\xi^*)\), with the same representing vector. It proves (SS.6), including its domain. ∎

The adjoint is always closed, even though its initial operator need not be closable. Replacing its possibly nondense domain by all of \(H\) would discard the infinite-energy term needed below.

## Bounded coefficients obtained by spectral truncation

Fix \(\xi\), and abbreviate \(p=p_\xi\). On \(pH\), the form

\[
t_\xi(v,w)=\langle T_\xi^*v,T_\xi^*w\rangle,
\qquad v,w\in D(T_\xi^*)
\]

is densely defined and closed: its form norm is the graph norm of the closed adjoint. QF-03 gives a nonnegative self-adjoint operator \(B_\xi\) on \(pH\) with

\[
D(B_\xi^{1/2})=D(T_\xi^*),
\qquad \|B_\xi^{1/2}v\|=\|T_\xi^*v\|.
\tag{SS.7}
\]

This definition does not form an untyped product of operators with nondense domains.

Equation (SS.5) makes the form invariant under every restricted unitary of \(N\). Uniqueness in closed-form representation gives the same invariance of \(B_\xi\) and its spectral projections. Extended by zero on \((1-p)H\), those projections commute with \(N\) and belong to \(M\). Define, for positive integers \(n\),

\[
P_n=1_{[0,n]}(B_\xi),\qquad B_n=B_\xi P_n,
\tag{SS.8}
\]

both extended by zero outside \(pH\). Then \(P_n\in M\), \(P_n\uparrow p\) strongly, \(B_n\in M_+\), and \(0\le B_n\le n1\). The sequence \(B_n\) is increasing but need not be norm bounded.

**Lemma.** For each \(n\), \(P_n\xi\in D_\psi\) and

\[
R_\psi(P_n\xi)=(T_\xi^*P_n)^*,
\qquad \theta_\psi(P_n\xi,P_n\xi)=B_n.
\tag{SS.9}
\]

If \(n\ge m\), then

\[
\theta_\psi((P_n-P_m)\xi,(P_n-P_m)\xi)=B_n-B_m.
\tag{SS.10}
\]

**Proof.** The spectral domain theorem gives \(P_nH\subseteq D(T_\xi^*)\) and
\(\|T_\xi^*P_nv\|^2=\langle B_nv,v\rangle\le n\|v\|^2\).
Thus \(T_\xi^*P_n:H\to H_\psi\) is bounded. For \(x\in\mathfrak n_\psi\) and \(v\in H\),

\[
\langle xP_n\xi,v\rangle
=\langle x\xi,P_nv\rangle
=\langle\Lambda_\psi(x),T_\xi^*P_nv\rangle.
\]

Its bounded adjoint therefore extends the initial map for \(P_n\xi\); this proves boundedness of that vector and the first identity in (SS.9). The squared norm identity for \(T_\xi^*P_n\), applied to every \(v\), identifies its bounded adjoint-product with \(B_n\), proving the second identity.

The same argument applies to \(P_n-P_m\). These are commuting spectral projections, and

\[
(P_n-P_m)B_\xi(P_n-P_m)=B_\xi(P_n-P_m)=B_n-B_m.
\]

This proves (SS.10). ∎

If \(\xi\in D_\psi\) already, then \(T_\xi\) extends to \(R_\psi(\xi)\). Its adjoint is defined on all of \(H\), so \(p=1\) and \(B_\xi=\theta_\psi(\xi,\xi)\) is bounded. The new coefficients then stabilize at that bounded coefficient once \(n\ge\|B_\xi\|\).

## Energy tests on every Hilbert-space vector

Define the zero-or-infinity function

\[
\delta(t)=\begin{cases}0,&t=0,\\+\infty,&t>0,
\end{cases}
\qquad t\in[0,\infty].
\]

For a normal numerator \(\varphi\), use the projection and coefficients associated with \(\xi\) to set

\[
G_\varphi(\xi)=\sup_n\varphi(B_n)+\delta(\varphi(1-p_\xi)).
\tag{SS.11}
\]

The definition uses only bounded positive elements of \(M\) and ordinary weight values. In particular, no prior extension of a weight to a generalized positive cone is required.

**Proposition.** The function \(G_\varphi\) is lower semicontinuous on all of \(H\), and it agrees with \(\varphi(\theta_\psi(\xi,\xi))\) on \(D_\psi\).

**Proof for a bounded normal functional.** Write \(\omega=\sum_j\omega_{v_j}\) as in SC-02. For fixed \(v\in H\), the adjoint test and the Hilbert variational formula give

\[
g_v(\xi):=
\sup_{x\in\mathfrak n_\psi}
\left(2\operatorname{Re}\langle v,x\xi\rangle
-\|\Lambda_\psi(x)\|^2\right)
=
\begin{cases}
\|T_\xi^*v\|^2,&v\in D(T_\xi^*),\\
+\infty,&v\notin D(T_\xi^*).
\end{cases}
\tag{SS.12}
\]

For completeness, finiteness of the supremum bounds the functional \(\Lambda_\psi(x)\mapsto\langle x\xi,v\rangle\): optimize after multiplying \(x\) by a complex scalar to obtain its squared modulus bounded by the supremum times \(\|\Lambda_\psi(x)\|^2\). Extension and Riesz representation give exactly (SS.3). If the adjoint value exists, completing the square and using density of GNS vectors gives the displayed squared norm. Each test in the supremum is norm continuous in \(\xi\), so \(g_v\) is lower semicontinuous.

We claim

\[
G_\omega(\xi)=\sum_j g_{v_j}(\xi).
\tag{SS.13}
\]

If \(\omega(1-p)>0\), some \(v_j\) has a nonzero component outside \(pH\). That vector cannot belong to \(D(T_\xi^*)\), so both sides are infinite. Otherwise all \(v_j\in pH\). Spectral monotone convergence and (SS.7) give

\[
\sup_n\omega(B_n)
=\sup_n\sum_j\|T_\xi^*P_nv_j\|^2
=\sum_j\sup_n\|T_\xi^*P_nv_j\|^2
=\sum_j g_{v_j}(\xi).
\]

The last equality includes vectors outside the square-root domain by the exact spectral integrability criterion. The interchange uses nonnegative increasing scalar quantities. This proves (SS.13), including representation independence, since its left side uses only \(\omega\). A sum of nonnegative lower semicontinuous functions is the supremum of its finite partial sums, hence is lower semicontinuous.

**Passage to a normal weight.** NW-11 implies

\[
G_\varphi(\xi)=
\sup_{\substack{\omega\in M_*^+\\\omega\le\varphi}}G_\omega(\xi).
\tag{SS.14}
\]

If \(\varphi(1-p)>0\), some dominated normal functional is positive there, making the right side infinite. If \(\varphi(1-p)=0\), all those functionals vanish there, and (SS.14) follows by interchanging \(\sup_n\) with the dominated-functionals supremum at \(B_n\). No directedness of that family is needed. Thus \(G_\varphi\) is lower semicontinuous.

Finally, on \(D_\psi\) we have \(p=1\) and eventual equality \(B_n=\theta_\psi(\xi,\xi)\), by SS-03. This proves agreement with the original energy. ∎

## One approximation works for every normal weight

**Theorem.** For every normal numerator \(\varphi\) and every \(\xi\in H\),

\[
Q_\varphi(\xi)=G_\varphi(\xi).
\tag{SS.15}
\]

For a fixed \(\xi\), choose any sequence \(\zeta_n\in D_\psi\) with \(\zeta_n\to\xi\), and put

\[
\xi_n=P_n\xi+(1-p_\xi)\zeta_n.
\tag{SS.16}
\]

Then \(\xi_n\in D_\psi\), \(\xi_n\to\xi\), and

\[
Q_\varphi(\xi_n)\longrightarrow Q_\varphi(\xi)
\tag{SS.17}
\]

for every normal \(\varphi\). Whenever \(Q_\varphi(\xi)<\infty\), every \(\xi_n\in E_\varphi\) and the convergence is in the \(q_\varphi\)-form norm. The sequence depends only on \(\xi\), the denominator and the chosen Hilbert approximation, not on the numerator.

**Proof.** First take \(\xi\in V_\varphi\). Its SC core supplies \(\eta_k\in E_\varphi\) converging to it in form norm. SS-04 and agreement on bounded vectors give

\[
G_\varphi(\xi)
\le\liminf_k G_\varphi(\eta_k)
=\lim_k q_\varphi[\eta_k]=q_\varphi[\xi].
\tag{SS.18}
\]

Thus the inequality \(G_\varphi\le Q_\varphi\) holds everywhere, with the assertion outside \(V_\varphi\) automatic.

Now assume \(G_\varphi(\xi)=L<\infty\), and abbreviate \(p=p_\xi\). Then \(\varphi(1-p)=0\). Null compression gives

\[
\varphi(a)=\varphi(pap)\qquad(a\in M_+).
\tag{SS.19}
\]

Indeed, the largest null projection \(f_\varphi\) dominates \(1-p\), so \(r=1-f_\varphi\le p\). WS-05 applied to \(a\) and to \(pap\) gives the same value \(\varphi(rar)\), proving (SS.19) even when that value is infinite.

Density of \(D_\psi\) supplies \(\zeta_n\). SS-03 makes \(P_n\xi\) bounded, and invariance under \(M\) makes \((1-p)\zeta_n\) bounded. The sequence in (SS.16) is therefore bounded-vector valued and tends in \(H\) to \(p\xi+(1-p)\xi=\xi\).

Compressing its coefficient by \(p\) removes the complement term. Equations (SS.9)–(SS.10), together with (SS.19), yield

\[
q_\varphi^0[\xi_n]=\varphi(B_n)<\infty,
\tag{SS.20}
\]

and, when \(n\ge m\),

\[
q_\varphi^0[\xi_n-\xi_m]
=\varphi(B_n-B_m)
=\varphi(B_n)-\varphi(B_m).
\tag{SS.21}
\]

The last subtraction is between finite numbers; it follows from weight additivity on \(B_n=B_m+(B_n-B_m)\). The increasing numbers \(\varphi(B_n)\) have finite limit \(L\). Consequently (SS.21) tends to zero as \(n,m\to\infty\). The sequence is Cauchy in the initial form norm. SC's canonical completion puts its Hilbert limit \(\xi\) in \(V_\varphi\), with form-norm convergence and
\(q_\varphi[\xi]=\lim_n\varphi(B_n)=G_\varphi(\xi)\).
Together with (SS.18), this proves (SS.15).

The same construction was independent of \(\varphi\), so it gives the finite-energy claim simultaneously for every normal numerator. If instead \(Q_\varphi(\xi)=\infty\), lower semicontinuity of the SC extended form gives \(\liminf_n Q_\varphi(\xi_n)=\infty\); this is exactly convergence to infinity in (SS.17). ∎

For finite energy, the scalar energies of this particular approximation increase to the limit by (SS.20). We do not assert an order on the vectors \(\xi_n\), or monotonicity of every energy sequence when the limiting energy is infinite.

## Sums of normal weights with arbitrary index sets

Let \((\varphi_i)_{i\in I}\) be any family of normal weights on \(M\). Define

\[
\varphi(a)=\sum_{i\in I}\varphi_i(a)
:=\sup_{F\subseteq I,\ F\text{ finite}}
       \sum_{i\in F}\varphi_i(a),\qquad a\in M_+.
\tag{SS.22}
\]

The empty sum is zero, and all scalar sums have nonnegative extended values.

**Proposition.** The function \(\varphi\) is a normal weight. No boundedness or summability hypothesis on the family is required. Its largest null projection is

\[
f_\varphi=\bigwedge_{i\in I}f_{\varphi_i}.
\tag{SS.23}
\]

For an empty family this meet is \(1\).

**Proof.** For two nonnegative scalar families \((a_i),(b_i)\), finite subsums show
\(\sum_i(a_i+b_i)=\sum_i a_i+\sum_i b_i\).
For the nontrivial lower inequality, choose any two finite subsets for the separate sums and pass to their union. Suprema over those subsets give the result, including infinity. Applying this to \(a_i=\varphi_i(a)\), \(b_i=\varphi_i(b)\) proves additivity. Positive homogeneity for positive scalars follows by rescaling each finite subsum; the zero scalar is handled by the weight convention \(0\cdot\infty=0\).

If \(a_\alpha\uparrow a\) is bounded in \(M_+\), then for each finite \(F\), directedness of \(\alpha\) gives

\[
\sum_{i\in F}\varphi_i(a)
=\sum_{i\in F}\sup_\alpha\varphi_i(a_\alpha)
=\sup_\alpha\sum_{i\in F}\varphi_i(a_\alpha).
\]

To verify the last equality when some limit is infinite, require that term to exceed any prescribed finite bound; when all are finite, approximate each within a chosen positive tolerance and use one common upper index. Interchanging \(\sup_F\) and \(\sup_\alpha\) proves normality of (SS.22).

A projection has zero \(\varphi\)-weight exactly when every \(\varphi_i\) vanishes on it, equivalently when it lies below every \(f_{\varphi_i}\). The projection onto the intersection of these ranges belongs to \(M\), since that intersection reduces \(M'\), and is their meet. This proves (SS.23). ∎

Semifiniteness does not follow merely because all the summands are semifinite. The finite-total-energy condition in the next theorem is necessary.

## The full spatial sum theorem and its joint core

**Theorem.** With the common denominator \(\psi\) and the sum weight (SS.22),

\[
Q_\varphi(\xi)=\sum_{i\in I}Q_{\varphi_i}(\xi)
\qquad(\xi\in H).
\tag{SS.24}
\]

Consequently

\[
V_\varphi=
\left\{\xi\in\bigcap_{i\in I}V_{\varphi_i}:
\sum_{i\in I}q_{\varphi_i}[\xi]<\infty\right\},
\tag{SS.25}
\]

and on that domain

\[
q_\varphi(\xi,\eta)=\sum_{i\in I}q_{\varphi_i}(\xi,\eta).
\tag{SS.26}
\]

The series in (SS.26) is absolutely summable. Its domain with this form is closed, even if its Hilbert closure is proper. The bounded-vector intersection \(D_\psi\cap V_\varphi\) is a form core for this complete sum. For finite families the domain is simply the intersection of the individual form domains.

**Proof.** Fix \(\xi\), and use its common \(p_\xi,B_n\). If some \(\varphi_i(1-p_\xi)>0\), both sides of (SS.24) are infinite by SS-05. Otherwise all these values vanish, and so does their sum. In this case

\[
\begin{aligned}
Q_\varphi(\xi)
&=\sup_n\sum_{i\in I}\varphi_i(B_n)\\
&=\sum_{i\in I}\sup_n\varphi_i(B_n)
=\sum_{i\in I}Q_{\varphi_i}(\xi).
\end{aligned}
\]

The middle interchange follows by first taking finite subsets of \(I\), then using the increasing scalar sequence in \(n\) for each finite subset, and finally interchanging suprema. This proves (SS.24) in every extended-value case, including an empty family.

Finiteness of the two sides gives (SS.25). For \(\xi,\eta\) in that domain, form Cauchy–Schwarz and scalar Cauchy–Schwarz for finite subsums give

\[
\sum_i|q_{\varphi_i}(\xi,\eta)|
\le\left(\sum_i q_{\varphi_i}[\xi]\right)^{1/2}
    \left(\sum_i q_{\varphi_i}[\eta]\right)^{1/2}<\infty.
\]

Thus their sum is a sesquilinear form with the diagonal in (SS.24); polarization identifies it with \(q_\varphi\). It is closed because the identified SC form is closed. SC-07 already makes its bounded-vector intersection a core. More concretely, SS-05 applied to the single normal weight \(\varphi=\sum_i\varphi_i\) makes (SS.16) converge in the total form norm for every vector in (SS.25). This is the required joint approximation. ∎

When the sum weight is semifinite, the theorem identifies its spatial derivative with the self-adjoint operator representing the sum form. The notation

\[
\frac{d(\varphi_1+\varphi_2)}{d\psi}
=\frac{d\varphi_1}{d\psi}
 \mathbin{\dot+}\frac{d\varphi_2}{d\psi}
\]

means that form sum, with form domain \(V_{\varphi_1}\cap V_{\varphi_2}\). It does not assert equality with an algebraic operator sum on \(D(A_1)\cap D(A_2)\). For a nonsemifinite sum, the represented operator lives on \(e_\varphi H\) as in SC-09. Formula (SS.24), rather than an untyped operator sum on all of \(H\), remains valid without a density assumption.

## Scalar multiples and pointwise suprema

For \(c>0\), the spectral formula immediately gives

\[
Q_{c\varphi}=cQ_\varphi,
\qquad V_{c\varphi}=V_\varphi,
\qquad A_{c\varphi}=cA_\varphi
\text{ on }e_\varphi H.
\tag{SS.27}
\]

The zero scalar is different at the domain level: \(0\varphi\) is the zero weight, its form is zero on all of \(H\), and its representing operator is the everywhere-defined zero operator. Multiplying the values of a form by zero while retaining a proper old domain would not give this result.

**Supremum principle.** Suppose a family of normal weights \((\chi_j)\) has a pointwise supremum on \(M_+\) which is itself a normal weight \(\chi\). Then, without requiring the family to be directed,

\[
Q_\chi(\xi)=\sup_j Q_{\chi_j}(\xi)
\qquad(\xi\in H).
\tag{SS.28}
\]

For an empty family interpret both suprema as zero.

**Proof.** Fix \(\xi\). If \(\chi(1-p_\xi)>0\), some family member has positive value there; both sides of (SS.28) are infinite. Otherwise they all vanish there. The assertion then follows from

\[
\sup_n\chi(B_n)=\sup_n\sup_j\chi_j(B_n)
=\sup_j\sup_n\chi_j(B_n)
\]

and SS-05. ∎

The premise that the pointwise supremum is a weight matters. An arbitrary supremum of additive positive functions need not be additive. The next case verifies that premise, rather than assuming it.

## Increasing weights, finite energy and resolvents

Let \((\varphi_i)_{i\in I}\) be an increasing net of normal weights, where \(I\) is an arbitrary nonempty directed set. Define \(\varphi(a)=\sup_i\varphi_i(a)\) for \(a\ge0\).

**Theorem.** The function \(\varphi\) is a normal weight and

\[
Q_\varphi=\sup_i Q_{\varphi_i},\qquad
V_\varphi=
\left\{\xi\in\bigcap_iV_{\varphi_i}:
                  \sup_i q_{\varphi_i}[\xi]<\infty\right\}.
\tag{SS.29}
\]

**Proof.** Directedness gives
\(\sup_i(\varphi_i(a)+\varphi_i(b))=\sup_i\varphi_i(a)+\sup_i\varphi_i(b)\): approximate the two separate suprema and choose a common upper index, including the cases with infinity. This proves additivity; homogeneity is immediate with the zero-scalar convention. For a bounded increasing positive net \(a_\alpha\uparrow a\), normality follows by commuting the two suprema \(\sup_i\sup_\alpha\varphi_i(a_\alpha)\). The supremum principle proves the first identity in (SS.29), and its finite values give the second. ∎

**Resolvent consequence.** Suppose each \(\varphi_i\) is semifinite, so its derivative \(A_i\) is self-adjoint on \(H\). Let \(K=e_\varphi H\), and let \(A_K\) represent the limit form there. For every \(z\in\mathbb C\setminus[0,\infty)\),

\[
(A_i-zI)^{-1}\longrightarrow(A_K-zI_K)^{-1}P_K
\quad\text{strongly on }H.
\tag{SS.30}
\]

Indeed SC-10 orders the forms, (SS.29) identifies their exact finite-energy supremum, and QF-07 applies to precisely that domain. If \(\varphi\) is semifinite, then \(K=H\) and this is strong resolvent convergence to its spatial derivative. If \(K\ne H\), the right side is a generalized resolvent, not a resolvent of a densely defined operator on all of \(H\).

If \(\varphi\) is semifinite and one \(\varphi_{i_0}\) is faithful, then SC-09 makes \(A_{i_0}\) injective, and QF-08 gives, on the tail \(i\ge i_0\), strong resolvent convergence of \(\log A_i\) to \(\log A\), and

\[
\sup_{|t|\le T}\|A_i^{it}\xi-A^{it}\xi\|\longrightarrow0
\qquad(\xi\in H,\ 0\le T<\infty).
\tag{SS.31}
\]

These are statements about the spatial operators and their spectral powers. Identifying their conjugations with modular automorphisms remains a separate theorem; (SS.31) does not by itself claim convergence in an automorphism-group topology.

## Any bounded change of the numerator

Let \(b\in M\), without assuming invertibility, and set

\[
\varphi_b(a)=\varphi(b^*ab),\qquad a\in M_+.
\tag{SS.32}
\]

Conjugation preserves positive addition and bounded increasing positive suprema, so this is a normal weight.

**Theorem.** On all of \(H\),

\[
Q_{\varphi_b}(\xi)=Q_\varphi(b^*\xi),
\qquad
V_{\varphi_b}=\{\xi:b^*\xi\in V_\varphi\}.
\tag{SS.33}
\]

On its finite domain the sesquilinear form is
\(q_{\varphi_b}(\xi,\eta)=q_\varphi(b^*\xi,b^*\eta)\).

**Proof.** If \(\omega=\sum_j\omega_{v_j}\) is bounded and normal, then \(\omega_b=\sum_j\omega_{bv_j}\). The variational tests satisfy

\[
g_{bv}(\xi)=g_v(b^*\xi),
\]

because \(\langle bv,x\xi\rangle=\langle v,b^*x\xi\rangle=\langle v,xb^*\xi\rangle\) for every \(x\in N\). Equations (SS.13) and (SS.15) therefore give \(Q_{\omega_b}(\xi)=Q_\omega(b^*\xi)\).

For a general normal weight, NW-11 gives the pointwise identity

\[
\varphi_b=\sup_{\substack{\omega\in M_*^+\\\omega\le\varphi}}\omega_b
\quad\text{on }M_+.
\]

Its supremum is the already verified normal weight \(\varphi_b\), so (SS.28) applies even though the family need not be directed. Together with (SS.14)–(SS.15), it gives

\[
Q_{\varphi_b}(\xi)
=\sup_{\omega\le\varphi}Q_{\omega_b}(\xi)
=\sup_{\omega\le\varphi}Q_\omega(b^*\xi)
=Q_\varphi(b^*\xi).
\]

The finite domain follows; polarization gives the sesquilinear identity. ∎

For a singular \(b\), neither semifiniteness of \(\varphi_b\) nor a literal operator-product formula follows. Its Hilbert space is the closure of \(\{\xi:b^*\xi\in V_\varphi\}\), which need not equal the preimage of \(\overline{V_\varphi}\). The examples below exhibit both failures. When \(b\) is invertible and \(\varphi\) is semifinite, SC-11 gives the stronger operator statement \(A_{\varphi_b}=bA_\varphi b^*\) on the exact domain \((b^*)^{-1}D(A_\varphi)\).

## Bounded invertible change of the denominator

Now let \(b\in N=M'\) be bounded and invertible, and define

\[
\psi_b(x)=\psi(b^*xb),\qquad x\in N_+.
\tag{SS.34}
\]

**Theorem.** The weight \(\psi_b\) is normal, semifinite and faithful. There is a unitary

\[
U_b:H_{\psi_b}\to H_\psi,
\qquad U_b\Lambda_{\psi_b}(x)=\Lambda_\psi(xb),
\tag{SS.35}
\]

and the following are exact identities:

\[
D_{\psi_b}=bD_\psi,
\qquad R_{\psi_b}(\xi)=R_\psi(b^{-1}\xi)U_b,
\tag{SS.36}
\]

\[
Q_\varphi^{\psi_b}(\xi)=Q_\varphi^\psi(b^{-1}\xi),
\qquad V_\varphi^{\psi_b}=bV_\varphi^\psi.
\tag{SS.37}
\]

For any normal numerator, both represented operators act on \(K=e_\varphi H\), and on that Hilbert space

\[
A_\varphi^{\psi_b}=b^{-*}A_\varphi^\psi b^{-1},
\qquad D(A_\varphi^{\psi_b})=bD(A_\varphi^\psi),
\tag{SS.38}
\]

where \(b^{-*}=(b^{-1})^*\), and all bounded maps are restricted to \(K\).

**Proof.** Normality follows from the same positive-supremum argument as for (SS.32). If \(\psi_b(x)=0\), faithfulness of \(\psi\) gives \(b^*xb=0\), hence \(x=0\). To check semifiniteness directly, for every finite positive \(a\) of \(\psi\), the positive element \(b^{-*}ab^{-1}\) is finite for \(\psi_b\). Its support range is the closure of \(b^{-*}\operatorname{ran}a^{1/2}\). Since these original ranges span the representation Hilbert space by semifiniteness and \(b^{-*}\) is invertible, the transformed ranges also span it. WS-02 applied on \(N\) gives finite-domain projection one, proving semifiniteness.

The finite left ideals satisfy \(\mathfrak n_{\psi_b}=\mathfrak n_\psi b^{-1}\). Their GNS norms obey \(\|\Lambda_{\psi_b}(x)\|^2=\psi((xb)^*(xb))\). Right multiplication by \(b\) bijects these domains, so (SS.35) extends to an onto isometry. In the bounded-vector estimate, substitute \(y=xb\). Then \(x\xi=y b^{-1}\xi\), proving the equality of bounded-vector sets. Evaluation on the dense GNS domain gives the operator formula in (SS.36), and unitarity of \(U_b\) gives

\[
\theta_{\psi_b}(\xi,\xi)
=\theta_\psi(b^{-1}\xi,b^{-1}\xi).
\]

The corresponding initial finite domains and energies thus transform by \(b^{-1}\). Bounded invertibility makes the original and transformed graph norms equivalent. Their canonical closures therefore satisfy (SS.37), exactly as in the completion proof of SC-11.

Because \(b\in M'\), it commutes with \(e_\varphi\) and preserves \(K\), as do its adjoint and inverse. Put \(C=b^{-1}|_K\). This is an invertible bounded map of \(K\). The transformed form is \(q_\varphi^\psi(C\xi,C\eta)\). By the graph characterization of a represented form, its operator is \(C^*A_\varphi^\psi C\) on \(C^{-1}D(A_\varphi^\psi)\): substitution \(\zeta=C\eta\) in the representing-vector identity proves both the domain and the value. This is precisely (SS.38). ∎

For \(b=\sqrt c\,1\), \(c>0\), these formulas give

\[
Q_\varphi^{c\psi}=c^{-1}Q_\varphi^\psi,
\qquad A_\varphi^{c\psi}=c^{-1}A_\varphi^\psi
\tag{SS.39}
\]

with unchanged domains. If \(b=u\) is unitary in \(N\), the operator formula becomes \(A_\varphi^{\psi_u}=uA_\varphi^\psi u^*\). These are fixed bounded changes of the denominator; no time-dependent cocycle is being constructed.

## Ordering the denominator reverses energy order

Let \(\psi_1,\psi_2\) be normal semifinite faithful weights on \(N\), with \(\psi_1\le\psi_2\).

**Proposition.** For any normal numerator \(\varphi\),

\[
q_\varphi^{\psi_2}\le q_\varphi^{\psi_1}
\quad\text{as closed forms},
\tag{SS.40}
\]

so \(V_\varphi^{\psi_1}\subseteq V_\varphi^{\psi_2}\) and the energy for \(\psi_2\) is no larger on that domain.

**Proof.** The estimate defining a \(\psi_1\)-bounded vector also proves it \(\psi_2\)-bounded, since \(\mathfrak n_{\psi_2}\subseteq\mathfrak n_{\psi_1}\) and \(\psi_1(x^*x)\le\psi_2(x^*x)\). DW-04 supplies a contraction

\[
C:H_{\psi_2}\to H_{\psi_1},
\qquad C\Lambda_{\psi_2}(x)=\Lambda_{\psi_1}(x)
\quad(x\in\mathfrak n_{\psi_2}).
\]

On \(D_{\psi_1}\), the dense-domain identities give \(R_{\psi_2}(\xi)=R_{\psi_1}(\xi)C\). Therefore

\[
\theta_{\psi_2}(\xi,\xi)
=R_{\psi_1}(\xi)CC^*R_{\psi_1}(\xi)^*
\le\theta_{\psi_1}(\xi,\xi).
\]

Applying the weight gives inclusion of the initial finite domains and the same energy inequality there. Approximate a vector in \(V_\varphi^{\psi_1}\) in its initial form core. The inequality on differences makes the sequence Cauchy for the closed \(\psi_2\)-form norm. Completeness and agreement of Hilbert limits give domain inclusion and the energy inequality after taking limits, proving (SS.40). ∎

If \(0<c\le C<\infty\) and
\(c\psi_1\le\psi_2\le C\psi_1\), then the bounded-vector sets are equal, the finite form domains are equal, and

\[
C^{-1}q_\varphi^{\psi_1}
\le q_\varphi^{\psi_2}
\le c^{-1}q_\varphi^{\psi_1}.
\tag{SS.41}
\]

The vector-set equality follows directly by comparing their defining estimates; the form assertions follow from (SS.39)–(SS.40) in both directions. These are scalar comparison assumptions on whole weights, not an assumption that unbounded spatial derivatives commute.

## Why separate core assertions would not have sufficed

Consider \(H=\ell^2(\mathbb N)\) and the closed diagonal forms

\[
q_1[x]=\sum_n a_n|x_n|^2,\qquad
q_2[x]=\sum_n b_n|x_n|^2,
\]

on their maximal finite-energy domains, where

\[
a_n=\begin{cases}n^2,&n\text{ odd},\\1,&n\text{ even},\end{cases}
\qquad
b_n=\begin{cases}1,&n\text{ odd},\\n^2,&n\text{ even}.\end{cases}
\]

Put \(D=\{x\in c_{00}:\sum_n x_n=0\}\).

**Claim.** The subspace \(D\) is a form core for each \(q_j\), but not for their closed sum.

**Proof.** Finite-coordinate truncations are a core for either weighted diagonal form. Given a finite-support vector \(x\), let \(s=\sum_nx_n\). Choose \(m\) new even coordinates and let \(h_m\) equal \(s/m\) on those coordinates and zero elsewhere. Then \(x-h_m\in D\), while its squared \(q_1\)-form-norm error is \(2|s|^2/m\). This tends to zero, proving that \(D\) is a \(q_1\)-core. Using new odd coordinates proves the \(q_2\)-core assertion.

The sum form has squared graph norm

\[
\|x\|^2+q_1[x]+q_2[x]=\sum_n(n^2+2)|x_n|^2.
\]

The functional \(\ell(x)=\sum_nx_n\) is continuous for this norm, since weighted Cauchy–Schwarz bounds its absolute value by that norm times \((\sum_n(n^2+2)^{-1})^{1/2}\). Thus \(D\) lies in the proper closed kernel of \(\ell\), and cannot be a core for the sum. In fact its sum-form closure is that kernel: truncate a vector in the kernel and subtract its residual coordinate sum times the first basis vector. The truncations converge in sum-form norm, and continuity of \(\ell\) makes the correction tend to zero. ∎

This example does not contradict the spatial sum theorem. It shows the missing implication that SS-02–05 had to replace with a specific simultaneous approximation. An individual core statement for each spatial derivative would not, by itself, prove (SS.24).

## Problems with complete solutions

**1. An uncountable sum with finite energy.** On \(H=\ell^2(I)\), with arbitrary \(I\), let \(M=N=\ell^\infty(I)\), let \(\psi\) be counting weight, and let \(\varphi_i(a)=a_i\). Determine all the spatial derivatives and their sum.

**Solution.** SC-12 gives \(D_\psi=H\), since square-summable vectors are bounded. The derivative of \(\varphi_i\) is the coordinate projection \(P_i\), with form \(|\xi_i|^2\). Their normal-weight sum is \(\psi\), and the sum energy is \(\sum_i|\xi_i|^2=\|\xi\|^2\) on all \(H\). The resulting derivative is the identity. Finite partial sums of the projections converge strongly along the directed set of finite subsets of \(I\). No countable cofinal subset is needed.

**2. Finite summands with no nonzero finite-energy vector in the infinite sum.** Let \(M=N=\mathbb C\) act on \(H=\mathbb C\), let \(\psi(t)=t\), and take \(\varphi_n(t)=t\) for every positive integer \(n\). Describe the sum and the increasing partial-sum limit.

**Solution.** Every summand is a bounded normal faithful weight and has derivative \(I\). The total weight is zero at zero and infinity at every positive nonzero scalar. Its finite-energy domain is \(\{0\}\), although every individual domain is \(H\). Each partial-sum derivative is \(mI\), and \((mI+\lambda I)^{-1}\to0\) for \(\lambda>0\). The limit is the generalized resolvent on the zero Hilbert subspace. It is not the resolvent of the zero operator on \(H\), whose resolvent would be \(\lambda^{-1}I\).

**3. A bounded numerator change can destroy semifiniteness.** On \(H=\ell^2(\mathbb N)\), set \(M=B(H)\), \(N=\mathbb C1\), and \(\psi(\lambda1)=\lambda\). Define

\[
\varphi(a)=\sum_{n\ge1}n^2\langle ae_n,e_n\rangle,
\qquad a\in M_+.
\]

Let \(v_n=1/n\), and choose the bounded rank-one map \(b^*\xi=\langle\xi,e_1\rangle v\). Determine \(\varphi_b\) and its finite-energy domain.

**Solution.** The sum theorem for weights makes \(\varphi\) normal. It is faithful because zero diagonal values for a positive operator force \(a^{1/2}e_n=0\) for all \(n\), and hence \(a=0\). Finite-coordinate projections have finite weight and increase strongly to one, so WG-008 gives semifiniteness. With the scalar denominator, every vector is bounded and its coefficient is its rank-one positive operator. Therefore

\[
Q_\varphi(\xi)=\sum_n n^2|\xi_n|^2,
\qquad A_\varphi=\operatorname{diag}(n^2).
\]

The chosen \(v\) is in \(H\) but has infinite form energy. Since \(b\eta=\langle\eta,v\rangle e_1\), one has \(b^*ab=\langle ae_1,e_1\rangle\,\theta_v\), where \(\theta_v\eta=\langle\eta,v\rangle v\). Hence

\[
\varphi_b(a)=\begin{cases}0,&\langle ae_1,e_1\rangle=0,\\
+\infty,&\langle ae_1,e_1\rangle>0.
\end{cases}
\]

Its closed form is zero on \(e_1^\perp\) and infinite outside. Thus \(e_{\varphi_b}=f_{\varphi_b}=1-P_1\), and the changed numerator is not semifinite. Taking a preimage of the closure \(\overline{V_\varphi}=H\) would incorrectly predict the whole space as its finite-domain closure.

**4. A form identity need not be a literal operator-product identity.** Keep the preceding model, but take \(v_n=1/n^2\) in the definition of \(b^*\). Compare the new spatial operator with the algebraic product \(bA_\varphi b^*\).

**Solution.** Now \(v\in D(A_\varphi^{1/2})\) because \(c:=\sum_n n^2|v_n|^2=\sum_n n^{-2}<\infty\), but \(v\notin D(A_\varphi)\) because \(\sum_n n^4|v_n|^2=\infty\). Equation (SS.33) gives \(Q_{\varphi_b}(\xi)=c|\langle\xi,e_1\rangle|^2\) on all \(H\). Its represented operator is the bounded operator \(cP_1\) with domain \(H\).

The literal product requires \(b^*\xi\in D(A_\varphi)\). Since no nonzero multiple of \(v\) belongs to that domain, its domain is only \(e_1^\perp\), and its value there is zero. It is therefore different from the represented operator. Bounded invertibility in the stronger SC-11 operator formula cannot be dropped by retaining the same algebraic product interpretation.

**5. Comparing equivalent denominators.** In the arbitrary-coordinate model of SC-12, let denominator coefficients \(v_i,w_i\) satisfy \(0<cv_i\le w_i\le Cv_i<\infty\). Verify (SS.41), including zero and infinite numerator coordinates.

**Solution.** The energies have coefficients \(r_i/v_i\) and \(r_i/w_i\), where \(r_i\in[0,\infty]\) are the numerator coefficients. For finite \(r_i\),
\(C^{-1}r_i/v_i\le r_i/w_i\le c^{-1}r_i/v_i\).
Zero coefficients give zero in both forms. Infinite coefficients require the same coordinate to vanish in both domains. Summing the finite-coordinate inequalities proves identical finite-energy domains and (SS.41). This is a direct check of domain equivalence, not just an inequality on finitely supported vectors.

## Source correspondence and remaining dynamic assertions

SS-05 supplies a full simultaneous bounded-vector approximation, including the graph-norm statement for every finite normal-weight energy. SS-07 proves the finite-functional addition asserted in Takesaki IX.3, Proposition 3.10(ii), and strengthens it to arbitrary normal sums with the exact finite-total-energy domain. SS-09 proves the form and resolvent part of the increasing-weight passage relevant to Corollary 3.13, with a directed-net version and an explicit nonsemifinite limit. Its spectral-power consequence retains QF-08's hypotheses. The source's modular-automorphism convergence still needs the modular identification and its stated automorphism topology.

SS-10 extends bounded invertible numerator covariance to all bounded multipliers as a closed-form identity. SS-11–12 prove the indicated algebraic denominator transports and order comparisons. These do not establish the weight cocycle, inverse-cocycle or centralizer-affiliation assertions of Chapter VIII, Section 3. Those source statements concern faithful normal semifinite weights, strongly continuous unitary cocycles, mixed analytic domains and modular groups; they remain independently assigned results.

The direct spatial construction's identification with the source relative-modular operator and the direct/opposite convention dictionary retain their recorded boundaries. This unit does not construct the whole generalized positive cone, claim a new license for an antecedent text, or close those source correspondences through notation. It proves the stated analytic identities from the already constructed forms and their exact prerequisites.
