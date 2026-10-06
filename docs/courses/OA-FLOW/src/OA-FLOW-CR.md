# Projection corners and canonical positive-functional vectors

*Fresh local proof, GPT-6 Astra (OpenAI), Ultra, 2026-10-04. CC0-1.0 to the extent of rights held.*

Let \((M,H,J,P)\) be any standard form: \(JMJ=M'\), \(JzJ=z^*\) on the center, \(J\) fixes the self-dual closed cone \(P\), and \(xJxJ\) preserves \(P\). The preceding [NC-1–5](OA-FLOW-NC.md) constructs it from an arbitrary faithful n.s.f. weight. We use no faithful-state hypothesis on \(M\). Write \(j(x)=JxJ\) and \(\omega_\xi(a)=\langle a\xi,\xi\rangle\), with the linear-first convention.

Additional exact local inputs are PC-1's polar partial isometry, the maximal principle in CF-1, [CP](OA-FLOW-CP.md#oa-flow.cp.1) and ST-1/2 for predual/topology/compactness, [EP-1](OA-FLOW-EP.md#oa-flow.ep.1)'s positive vector series, WR/MW for the full faithful-state graphs, and the exact cosh integral in [MF scalar SB-2](OA-FLOW-MF-SB.md#oa-flow.mf-sb.3). All remaining steps, including the projection commutant and center statements, are proved here.

The free human route is [Hiai, Propositions 3.7–3.10 and Lemmas 3.14–3.19, printed pp.23–31](https://arxiv.org/pdf/2004.02383v1#page=23). We supply the arbitrary-algebra corner reduction and full form/domain arguments explicitly.

<a id="oa-flow.cr.1"></a><a id="cr-1"></a>

Exact additional locators: ST-2 faithful normal transport, [HA-R7 right graph core](OA-FLOW-HA-R.md#oa-flow.ha-r.7), [EP-2 vector-functional norm bound](OA-FLOW-EP.md#oa-flow.ep.2), [MF scalar SB-2 cosh proof](OA-FLOW-MF-SB.md#oa-flow.mf-sb.3).

## CR-1. Cone geometry and vector supports

Self-duality makes \(P\) pointed: if \(\xi,-\xi\in P\), then \(-\|\xi\|^2\geq0\). If \(Jv=v\), the closest point \(v_+\) of \(P\) to \(v\) exists. To recall the elementary proof, a minimizing sequence is Cauchy by the parallelogram identity and convexity; its limit lies in the closed cone. The same identity proves uniqueness. Put \(v_-=v_+-v\). Variations \(v_++t\eta\), \(t\geq0,\eta\in P\), show \(\langle v_-,\eta\rangle\geq0\): these inner products are real because both vectors are \(J\)-fixed. Hence \(v_-\in P\). Variations \((1-t)v_+\) show \(\langle v_-,v_+\rangle\leq0\); self-duality gives equality. Thus

<a id="equation-cr1"></a>

\[
 v=v_+-v_-,\qquad v_\pm\in P,\qquad v_+\perp v_-.
 \tag{CR1}
\]
If also \(v=w_+-w_-\) is such a decomposition, then
\(\|v_+-w_+\|^2=-\langle v_+,w_-\rangle-\langle w_+,v_-\rangle\leq0\).
Splitting any vector into its \(J\)-real and \(J\)-imaginary parts proves that the complex span of \(P\) is all \(H\).

For any \(\xi\in H\), let \(p_\xi\) be the projection onto \(\overline{M'\xi}\). This subspace is reducing for \(M'\), so \(p_\xi\in M\). It is the least projection in \(M\) fixing \(\xi\). Indeed, any such projection commutes with \(M'\) and fixes \(M'\xi\). For a projection \(e\in M\),
\(\omega_\xi(e)=0\) is equivalent to \(e\xi=0\), and then \(ep_\xi=0\). Consequently

<a id="equation-cr2"></a>

\[
 p_\xi=s(\omega_\xi).
 \tag{CR2}
\]
The restriction of \(\omega_\xi\) to \(p_\xi M p_\xi\) is faithful: if \(a\geq0\) there and \(a^{1/2}\xi=0\), then \(a^{1/2}M'\xi=0\), forcing \(a=0\).

For \(\xi\in P\), \(j(p_\xi)\) is the projection onto \(\overline{M\xi}\), by applying \(J\). Thus

<a id="equation-cr3"></a>

\[
 \xi=p_\xi j(p_\xi)\xi.
 \tag{CR3}
\]
Two further support facts will prevent a hidden faithfulness assumption in the norm estimate.

First, if \(e\in M\) is a projection and \(ej(e)\xi=0\) for \(\xi\in P\), then \(e\xi=0\). Put \(r=1-e\). For real \(t\), cone invariance gives
\[
 (e+tr)j(e+tr)\xi
 =t\{ej(r)+rj(e)\}\xi+t^2rj(r)\xi\in P.
\]
Divide by \(|t|\) and approach zero from both sides. Pointedness implies
\(\{ej(r)+rj(e)\}\xi=0\).
Its two terms are in orthogonal projection ranges, so each vanishes; hence \(e\xi=0\).
It follows that \(0\leq_P\xi\leq_P\zeta\) implies \(p_\xi\leq p_\zeta\). Apply \(rj(r)\), \(r=1-p_\zeta\), to \(\xi\) and \(\zeta-\xi\). Their images are in \(P\) and sum to zero; the just proved fact then gives \(r\xi=0\). In particular

<a id="equation-cr4"></a>

\[
 p_{\xi+\eta}=p_\xi\vee p_\eta\quad(\xi,\eta\in P).
 \tag{CR4}
\]

Second, if \(\xi,\eta\in P\) and \(\langle\xi,\eta\rangle=0\), positivity of
\(\langle(1+ta)j(1+ta)\xi,\eta\rangle\)
for every complex \(t\) forces its linear coefficient to vanish. Since \(J\xi=\xi,J\eta=\eta\), that coefficient is \(2\operatorname{Re}(t\langle a\xi,\eta\rangle)\). Hence \(\langle a\xi,\eta\rangle=0\) for every \(a\in M\). Thus \(j(p_\xi)\eta=0\), and applying \(J\) gives \(p_\xi\eta=0\). Formula ([CR2](OA-FLOW-CR.md#equation-cr2)) yields

<a id="equation-cr5"></a>

\[
 \xi\perp\eta\quad\Longleftrightarrow\quad p_\xi p_\eta=0
 \qquad(\xi,\eta\in P).
 \tag{CR5}
\]
The reverse implication is immediate from their left supports.

<a id="oa-flow.cr.2"></a><a id="cr-2"></a>

## CR-2. The projection commutant and center, proved locally

For an arbitrary concrete von Neumann algebra \(L\) and projection \(e\in L\), the central support \(c(e)\) is the projection onto \(\overline{\operatorname{span}LeH}\). This subspace is invariant under \(L,L^*,L',L'^*\); hence \(c(e)\in Z(L)\), and it is the least central projection majorizing \(e\).

Choose a maximal family \(v_i\in L\) of partial isometries with \(v_i^*v_i\leq e\), pairwise orthogonal final projections \(q_i=v_iv_i^*\), and include \(v_0=e\) when \(e\ne0\). Then

<a id="equation-cr6"></a>

\[
 \sum_iq_i=c(e).
 \tag{CR6}
\]
If the residual projection \(r\leq c(e)\) were nonzero, \(rLe\ne0\); otherwise \(r\) annihilates \(LeH\) and hence \(c(e)H\). A nonzero polar partial isometry of \(rxe\) has initial projection at most \(e\), final projection at most \(r\), and enlarges the family, a contradiction. Orthogonal sums mean strong limits over finite subsets.

If \(b\) is in the commutant of \(eLe\) on \(eH\), define \(B=\sum_i v_i b v_i^*\) on \(c(e)H\), and zero on its complement. These are orthogonal diagonal blocks of norm at most \(\|b\|\), so the sum exists strongly and is bounded. Each \(v_i^*v_i\in eLe\) commutes with \(b\). For \(x\in L\), the matrix coefficients of \(Bx\) and \(xB\) between the ranges of \(q_i,q_j\) agree because \(v_i^*xv_j\in eLe\) commutes with \(b\). Equation ([CR6](OA-FLOW-CR.md#equation-cr6)) and centrality of \(c(e)\) give \(B\in L'\). Also \(B|_{eH}=b\), using \(v_0=e\). Therefore

<a id="equation-cr7"></a>

\[
 (eLe)'_{\,eH}=eL'.
 \tag{CR7}
\]
If \(b\in Z(eLe)\), the same bounded strong sum belongs to \(L\) as well, hence to \(Z(L)\). Thus

<a id="equation-cr8"></a>

\[
 Z(eLe)=eZ(L).
 \tag{CR8}
\]
Zero projections are included separately with the zero Hilbert space.

Apply ([CR7](OA-FLOW-CR.md#equation-cr7)) a second time to the commutant algebra. If \(q\in L'\), it gives
\((qL'q)'_{qH}=Lq\).
Taking commutants proves that \(Lq\) is a von Neumann algebra on \(qH\), with commutant \(qL'q\). This justifies reduction by a commuting projection without presuming that an arbitrary compressed image is closed.

<a id="oa-flow.cr.3"></a><a id="cr-3"></a>

## CR-3. Every projection corner is a standard form

Let \(p\in M\), \(q=pj(p)\). The map

<a id="equation-cr9"></a>

\[
 pMp\longrightarrow B:=qMq,\qquad a\longmapsto aq
 \tag{CR9}
\]
is a faithful normal \(*\)-isomorphism onto a von Neumann algebra on \(qH\). To check faithfulness, if \(a\in pMp\) and \(aq=0\), then \(aj(p)=0\). The operator \(a\), commuting with \(M'\), annihilates \(\overline{M'j(p)H}\). Its projection is \(c_{M'}(j(p))=Jc_M(p)J=c_M(p)\), by the central axiom. Since \(a=ap\) and \(p\leq c_M(p)\), we get \(a=0\). Normality is concrete vector-series continuity; ST-2 gives the normal inverse.

For the algebra/commutant assertion, first use ([CR7](OA-FLOW-CR.md#equation-cr7)) on \(pH\), then reduce by \(q\in(pMp)'=pM'\) as proved after ([CR8](OA-FLOW-CR.md#equation-cr8)). This gives

<a id="equation-cr10"></a>

\[
 B'=qM'q=J_q B J_q,\qquad J_q=J|_{qH}.
 \tag{CR10}
\]
Here \(qJ=Jq\) because \(p,j(p)\) commute. Also

<a id="equation-cr11"></a>

\[
 P_q=qP=P\cap qH
 \tag{CR11}
\]
is self-dual on \(qH\): \(qP\subseteq P\) by cone invariance, and for \(\eta\in qH\) positivity against \(qP\) is exactly positivity against \(P\). This also proves its closedness. \(J_q\) fixes it. By ([CR8](OA-FLOW-CR.md#equation-cr8))/([CR9](OA-FLOW-CR.md#equation-cr9)), every central element of \(B\) is \(zq\) for a central \(z\in M\); thus \(J_q(zq)J_q=z^*q\). Finally for \(a\in pMp\), the operator \((aq)J_q(aq)J_q\) on \(qH\) is the restriction of \(aj(a)\), which preserves \(P_q\). Hence

<a id="equation-cr12"></a>

\[
 (B,qH,J_q,P_q)
 \tag{CR12}
\]
is a standard form of \(pMp\), for every projection \(p\), without a modular-invariance assumption.

If \(\xi\in P\) and \(p=p_\xi\), then \(\xi\in qH\) is cyclic and separating for this corner algebra. Indeed \(\overline{M'\xi}=pH\), and projecting onto \(qH\) gives \(\overline{qM'q\,\xi}=qH\). Thus it is cyclic for \(B'\) and separating for \(B\). Applying \(J_q\), which fixes \(\xi\), makes it cyclic for \(B\) as well.

<a id="oa-flow.cr.4"></a><a id="cr-4"></a>

## CR-4. A faithful cone vector gives exactly the existing conjugation and cone

In any standard form suppose \(\Omega\in P\) is cyclic and separating. Its vector functional is faithful and normal, and its GNS map \(a\mapsto a\Omega\) is onto the given Hilbert completion. Apply the already proved faithful-weight construction to obtain \(S_\Omega\) and \(F_\Omega=S_\Omega^*\). Their full cores are respectively \(M\Omega\) and \(M'\Omega\), with actions \(a\Omega\mapsto a^*\Omega\) and \(b\Omega\mapsto b^*\Omega\). Here the right-core assertion follows from the full right algebra: \(R_{b\Omega}=b\) for every \(b\in M'\), the full adjoint-intersection criterion puts \(b\Omega\) in \(D(F_\Omega)\), and the unit \(\Omega\) makes its product algebra a graph core, by [HA-R7](OA-FLOW-HA-R.md#oa-flow.ha-r.7)/WH-04.

Since \(J\Omega=\Omega\), conjugating the right core by \(J\) gives the left core with exactly its involution. Thus \(JF_\Omega J=S_\Omega\) on their full closed domains. It follows that \(JS_\Omega\) is self-adjoint:
\[
 (JS_\Omega)^*=F_\Omega J=JS_\Omega.
\]
It is positive. On its core \(M\Omega\),

<a id="equation-cr13"></a>

\[
 \langle JS_\Omega a\Omega,a\Omega\rangle
 =\langle a^*j(a^*)\Omega,\Omega\rangle\geq0
 \tag{CR13}
\]
by the cone action and self-duality. Graph approximation extends positivity to its full domain. Uniqueness of the polar decomposition of the closed conjugate-linear involution therefore gives \(J_\Omega=J\) and \(JS_\Omega=\Delta_\Omega^{1/2}\).

[NC-5](OA-FLOW-NC.md#oa-flow.nc.5) constructs \(P_\Omega=\overline{\{aj(a)\Omega:a\in M\}}\), which is contained in \(P\). Both cones are self-dual, so inclusion reverses on taking duals and they are equal. We have proved

<a id="equation-cr14"></a>

\[
 J_\Omega=J,\qquad P_\Omega=P
 \tag{CR14}
\]
with equality of the full \(S,F,\Delta\) domains supplied by the faithful GNS construction. By [CR-3](OA-FLOW-CR.md#oa-flow.cr.3) this statement applies in particular to every supported cone vector on its support corner.

<a id="oa-flow.cr.5"></a><a id="cr-5"></a>

## CR-5. The faithful-vector order interval

Keep the hypotheses of [CR-4](OA-FLOW-CR.md#oa-flow.cr.4) and put \(D=\Delta_\Omega\). The map

<a id="equation-cr15"></a>

\[
 A(x)=D^{1/4}x\Omega,\qquad x=x^*\in M,
 \tag{CR15}
\]
is an order isomorphism onto the \(P\)-order-bounded real vectors
\(\{\eta:J\eta=\eta,\ -c\Omega\leq_P\eta\leq_P c\Omega\text{ for some }c\}\).
Positivity preservation follows from [NC-5](OA-FLOW-NC.md#oa-flow.nc.5). It is reflected: if \(A(x)\in P\), then for \(y'\in M'\),
\[
 \langle xy'\Omega,y'\Omega\rangle
 =\langle D^{1/4}x\Omega,D^{-1/4}y'^*y'\Omega\rangle\geq0,
\]
by [NC-3](OA-FLOW-NC.md#oa-flow.nc.3), since the second vector is in \(P\). Density of \(M'\Omega\) gives \(x\geq0\). The map is injective by the spectral inverse and separation of \(\Omega\).

For surjectivity it suffices to consider \(0\leq_P\eta\leq_P\Omega\). Let \(G_n\) be [NC-3](OA-FLOW-NC.md#oa-flow.nc.3)'s positive Gaussian. Then \(0\leq_P G_n\eta\leq_P\Omega\), since \(G_n\Omega=\Omega\). Set \(\zeta_n=D^{-1/4}G_n\eta\). Testing against \(C_r\) by moving the negative quarter power to its other argument and using [NC-3](OA-FLOW-NC.md#oa-flow.nc.3) shows
\[
 \zeta_n\in C_l,\qquad \Omega-\zeta_n\in C_l.
\]
On \(M'\Omega\), the rule \(T_n(y'\Omega)=y'\zeta_n\) has quadratic values between zero and \(\|y'\Omega\|^2\), by the mutual duality of \(C_l,C_r\). Polarization and Cauchy–Schwarz for this positive form imply \(\|T_n v\|\leq\|v\|\) on that dense domain. Its extension is a positive contraction \(c_n\in M\), since it commutes with all right unitaries on the initial domain. Thus \(c_n\Omega=\zeta_n\) and \(A(c_n)=G_n\eta\).

The map \(A\) is ultraweak-to-weak continuous on \(M_{\rm sa}\). Its exact bounded formula is

<a id="equation-cr16"></a>

\[
 A(x)=D^{1/4}(1+D^{1/2})^{-1}(x\Omega+Jx^*\Omega).
 \tag{CR16}
\]
The scalar multiplier is bounded by \(1/2\), and the two vector coefficients are ultraweakly continuous by CP. The positive contraction interval is ultraweakly compact by ST-1/CF/CP, so its image under \(A\) is weakly compact and closed. As \(G_n\eta\to\eta\), this proves \(A(c)=\eta\) for some \(0\leq c\leq1\). Translation and scaling give the asserted whole order interval, in particular

<a id="equation-cr17"></a>

\[
 -\Omega\leq_P\eta\leq_P\Omega
 \ \Longrightarrow\ \eta=D^{1/4}x\Omega
 \text{ for some }x=x^*,\ \|x\|\leq1.
 \tag{CR17}
\]

<a id="oa-flow.cr.6"></a><a id="cr-6"></a>

## CR-6. The exact square-root estimate, with nonfaithful supports

For all \(\xi,\eta\in P\),

<a id="equation-cr18"></a>

\[
 \|\xi-\eta\|^2\leq\|\omega_\xi-\omega_\eta\|
 \leq\|\xi-\eta\|\,\|\xi+\eta\|.
 \tag{CR18}
\]
The upper bound follows by expanding the difference as half the sum of the two mixed coefficients of \(\delta=\xi-\eta\) and \(\zeta=\xi+\eta\). For the lower bound, take \(p=p_\zeta\). By [CR-1](OA-FLOW-CR.md#oa-flow.cr.1), both \(\xi,\eta\) belong to \(qH\), \(q=pj(p)\), where \(\zeta\) is cyclic and separating for the standard corner ([CR-3](OA-FLOW-CR.md#oa-flow.cr.3)). The zero case is immediate. Apply ([CR17](OA-FLOW-CR.md#equation-cr17)) there to \(\delta\), obtaining a self-adjoint contraction \(x\in pMp\) with \(\delta=D^{1/4}x\zeta\), where \(D\) is that corner's modular operator. In particular \(\delta\in D(D^{-1/4})\). Since \(J_q\delta=\delta\), reciprocal spectral transport also puts it in \(D(D^{1/4})\), with equal real quadratic values of these two powers. Hence

<a id="equation-cr19"></a>

\[
 \begin{split}
 \|\omega_\xi-\omega_\eta\|
 &\geq(\omega_\xi-\omega_\eta)(x)
  =\operatorname{Re}\langle x\zeta,\delta\rangle\\
 &=\tfrac12\langle(D^{-1/4}+D^{1/4})\delta,\delta\rangle
 \geq\|\delta\|^2.
 \end{split}
 \tag{CR19}
\]
The last inequality is the pointwise scalar inequality
\((t^{-1/4}+t^{1/4})/2\geq1\), integrated on the two already verified domains. Testing the original functional on \(x\in pMp\subset M\) gives the original norm bound. No faithful approximation of the two input functionals is needed.

It follows that \(\xi\mapsto\omega_\xi\) is injective and a homeomorphism onto a norm-closed subset of \(M_*^+\). Indeed a norm-Cauchy sequence of its functionals gives a Hilbert-Cauchy sequence of cone vectors by the first inequality, and the second inequality identifies its limit.

<a id="oa-flow.cr.7"></a><a id="cr-7"></a>

## CR-7. Every functional below a cone functional has a cone vector

First assume \(\Omega\in P\) is cyclic and separating, and \(0\leq\psi\leq\omega_\Omega\). The bounded form
\(\psi(b^*a)\) on \(M\Omega\) gives a positive contraction \(B\in M'\) with
\(\psi(a)=\langle a\Omega,B\Omega\rangle\). This is the direct GNS domination argument: positive-functional Cauchy–Schwarz bounds the form by the two Hilbert norms, Riesz represents it, and moving a left multiplier across the form proves commutation.

Put \(D=\Delta_\Omega\). Since \(B\Omega,(1-B)\Omega\in C_r\), the vector
\(\theta=D^{-1/4}B\Omega\) satisfies \(0\leq_P\theta\leq_P\Omega\).
Define

<a id="equation-cr20"></a>

\[
 \eta=2(1+D^{1/2})^{-1}B\Omega
      =f(\log D)\theta,\qquad f(t)=\frac{2}{e^{t/4}+e^{-t/4}}.
 \tag{CR20}
\]
The exact positive Fourier kernel is

<a id="equation-cr21"></a>

\[
 f(t)=\int_{\mathbb R}\frac{2}{\cosh(2\pi s)}\,e^{ist}\,ds.
 \tag{CR21}
\]
This follows by substituting \(u=2s\) in MF scalar (SB.3),
\(\int e^{ixu}/(2\cosh(\pi u))\,du=1/(2\cosh(x/2))\).
In particular the kernel in ([CR21](OA-FLOW-CR.md#equation-cr21)) has integral one. The vectorwise integral of \(D^{is}\) therefore preserves \(P\) and fixes \(\Omega\), so \(0\leq_P\eta\leq_P\Omega\).

The first expression in ([CR20](OA-FLOW-CR.md#equation-cr20)) shows \(\eta\in D(D^{1/2})\). Since \(J\eta=\eta\), reciprocal transport puts it in \(D(D^{-1/2})\) too, and \(F_\Omega\eta=D^{1/2}\eta\). Thus \(B\Omega=(\eta+F_\Omega\eta)/2\). The full anti-linear adjoint identity paired with \(a\Omega\in D(S_\Omega)\) gives

<a id="equation-cr22"></a>

\[
 \psi(a)=\tfrac12\{\langle a\Omega,\eta\rangle+
                         \langle a\eta,\Omega\rangle\},\qquad a\in M.
 \tag{CR22}
\]
For \(\Omega=0\), the dominated functional and required vector are zero. For a general nonzero \(\Omega\in P\), apply this proof in its support corner from [CR-3](OA-FLOW-CR.md#oa-flow.cr.3). If \(\psi\leq\omega_\Omega\), then \(\psi(1-p_\Omega)=0\); positive-functional Cauchy–Schwarz proves
\(\psi(a)=\psi(p_\Omega a p_\Omega)\). Thus the corner formula ([CR22](OA-FLOW-CR.md#equation-cr22)) is the same formula for every \(a\in M\), with \(0\leq_P\eta\leq_P\Omega\).

Now fix \(\psi\leq\omega_{\xi_0}\), \(\xi_0\in P\). Apply ([CR22](OA-FLOW-CR.md#equation-cr22)) to the defect \(\omega_{\xi_0}-\psi\), and divide its resulting cone vector by two. Obtain \(0\leq_P\eta_0\leq_P\xi_0/2\) such that, putting \(\xi_1=\xi_0-\eta_0\),

<a id="equation-cr23"></a>

\[
 \omega_{\xi_1}-\psi=\omega_{\eta_0},\qquad
 \|\omega_{\xi_1}-\psi\|=\|\eta_0\|^2
 \leq\tfrac12\langle\eta_0,\xi_0\rangle
 =\tfrac14\|\omega_{\xi_0}-\psi\|.
 \tag{CR23}
\]
All inner products used for the inequality are between ordered cone vectors. Repeat this step. The errors tend geometrically to zero, and [CR-6](OA-FLOW-CR.md#oa-flow.cr.6)'s closed-image assertion gives a cone vector \(\xi_\psi\) with \(\omega_{\xi_\psi}=\psi\).

<a id="oa-flow.cr.8"></a><a id="cr-8"></a>

## CR-8. Surjectivity on all normal positive functionals

Let \(f\in M_*^+\), \(p=s(f)\). Its support exists directly from [EP-1](OA-FLOW-EP.md#oa-flow.ep.1): write \(f=\sum_n\omega_{\zeta_n}\) and take \(p=\bigvee_n p_{\zeta_n}\). The positive series shows that \(f\) vanishes on \(1-p\), is compressed by \(p\), and is faithful on \(pMp\). Treat \(f=0\) separately by the zero vector.

We first construct some cyclic separating cone vector for this corner. Work in its standard form \(qH\), \(q=pj(p)\), from [CR-3](OA-FLOW-CR.md#oa-flow.cr.3). Take a maximal family of nonzero cone vectors \(\eta_i\in P_q\) with pairwise orthogonal supports \(p_i\leq p\). Their supports sum to \(p\): otherwise the nonzero residual corner has, by [CR-3](OA-FLOW-CR.md#oa-flow.cr.3) and [CR-1](OA-FLOW-CR.md#oa-flow.cr.1), a nonzero cone vector, which enlarges the family. The family is countable, because \(f(p_i)>0\), while every finite sum is at most \(f(p)<\infty\). Explicitly, for each positive integer \(n\) only finitely many \(i\) can have \(f(p_i)\geq1/n\), and the union of these finite sets contains all indices.

Choose strictly positive \(c_i\) with \(\sum_i c_i\|\eta_i\|<\infty\). Then
\(\Omega=\sum_i c_i\eta_i\in P_q\).
The right supports \(j(p_i)\) are orthogonal and commute with every \(a\in M\), so all mixed coefficients between distinct summands vanish. Consequently
\(\omega_\Omega=\sum_i c_i^2\omega_{\eta_i}\), and its support is \(p\). [CR-3](OA-FLOW-CR.md#oa-flow.cr.3) makes \(\Omega\) cyclic and separating on \(qH\).

Every positive normal functional of the corner can be approximated in norm by ones dominated by \(C\omega_\Omega\) for finite \(C\). In fact [EP-1](OA-FLOW-EP.md#oa-flow.ep.1) supplies a summable positive vector series on \(qH\). Truncate that series, and approximate its finitely many vectors by \(b_i'\Omega\), \(b_i'\in B'\), using the cyclicity of \(\Omega\) for the commutant. The vector-functional norm estimate in [EP-2](OA-FLOW-EP.md#oa-flow.ep.2) gives the required convergence, while

<a id="equation-cr24"></a>

\[
 \sum_{i=1}^k\omega_{b_i'\Omega}(a)
 \leq\left(\sum_{i=1}^k\|b_i'\|^2\right)\omega_\Omega(a)
 \qquad(a\geq0).
 \tag{CR24}
\]
[CR-7](OA-FLOW-CR.md#oa-flow.cr.7) applies after scaling \(\Omega\). Thus all approximating functionals have cone vectors. Their norm limit has a cone vector by [CR-6](OA-FLOW-CR.md#oa-flow.cr.6). Apply this to the faithful corner restriction of \(f\), and regard the resulting vector in \(P_q\subseteq P\). Compression of \(f\) proves that it represents \(f\) on every element of \(M\).

We have proved existence and uniqueness for all \(f\in M_*^+\), with

<a id="equation-cr25"></a>

\[
 \|\xi_f\|^2=f(1),\quad p_{\xi_f}=s(f),\quad
 \xi_f\in s(f)j(s(f))H,\quad
 \|\xi_f-\xi_g\|^2\leq\|f-g\|.
 \tag{CR25}
\]
Its support-corner functional is faithful, its corner vector is cyclic and separating, and [CR-4](OA-FLOW-CR.md#oa-flow.cr.4) identifies its full Tomita polar data with the restricted \(J\) and cone. Nonfaithful and zero functionals are included.

<a id="oa-flow.cr.9"></a><a id="cr-9"></a>

## CR-9. Every von Neumann algebra has a faithful n.s.f. weight

For completeness, the initial weight hypothesis of NC does not restrict the algebras covered by existence of a standard form. In any concrete \(M\), choose a maximal orthogonal family \(p_i\) of supports of normal states \(f_i\), each supported on \(p_i\). They sum to \(1\): a nonzero residual projection contains a nonzero Hilbert vector, whose normalized vector functional has nonzero support beneath that projection. The weight

<a id="equation-cr26"></a>

\[
 \varphi(a)=\sum_i f_i(a),\qquad a\in M_+,
 \tag{CR26}
\]
is normal, additive and homogeneous by interchanging the suprema over finite subsums and bounded increasing positive nets. It is faithful because each \(f_i\) is faithful on its support corner. More explicitly, zero value at \(a\geq0\) implies \(a^{1/2}p_i=0\) for all \(i\), hence \(a=0\). Finally \(\varphi(p_i)=1\), so their finite sums are finite-weight projections increasing strongly to \(1\); GW-4 proves semifiniteness. NC therefore supplies a standard form for every von Neumann algebra, on an arbitrary Hilbert space.
