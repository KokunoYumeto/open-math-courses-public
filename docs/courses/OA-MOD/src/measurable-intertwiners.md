# Measurable operators between representations

**Self-checked by the writing AI.**

A trace lets us discard a small part of an operator's domain and measure the norm on what remains. This construction also works for an operator between two different representations. The essential normalization is that the initial and final supports of an intertwiner have the same trace. Once that normalization is established, a linking algebra supplies the completion and its actual closed operators. Positive vector densities then identify the square-integrable intertwiners with the original Hilbert space.

Throughout, \(M\subseteq B(H)\) is a von Neumann algebra with a faithful normal semifinite trace \(\tau\). Other representations are normal and unital; where a double commutant is identified with the original concrete \(M\), the representation on \(H\) is the given faithful one. No countability assumption is made. Inner products are linear in the first variable. Products of measurable operators mean closed products, unless an ordinary domain is specified.

We use the complete earlier proofs of trace integration TI06–15, the modular commutant MF05, module trace normalization TM01, and measure completion MT02–11. The vector-density argument below is a second route to the square-integrable column identification already proved in TM02; that earlier matrix argument remains available. The same results are treated in Takesaki, *Theory of Operator Algebras II*, Chapter IX, §2, Exercise 8, p. 185, together with Theorems 2.2 and 2.5, pp. 168–171. We develop the topology and domain mechanisms explicitly rather than leaving their transfer to a hint.

## Opposite traces and positive vector densities

Put \(L=L^2(M,\tau)\), with left action \(\lambda\). For bounded \(b\in M\), let \(r_b\) be right multiplication on \(L\). TI15 proves its boundedness and its adjoint formula. The trace GNS involution sends \(\Lambda_\tau(x)\) to \(\Lambda_\tau(x^*)\); traciality makes this an isometry on its dense domain, so its closure is the everywhere defined antiunitary \(J\). Its modular operator is therefore \(1\). The remaining Hilbert algebra axioms and its generated algebra are proved in WH09. Applying MF05 to this GNS Hilbert algebra gives

\[
 \begin{gathered}
 N:=\lambda(M)',\\
 N=r(M),\\
 r_b=J\lambda(b^*)J,\\
 r_b r_c=r_{cb}.
 \end{gathered}
 \tag{MR.1}
\]

Consequently \(b^{\mathrm{op}}\mapsto r_b\) is a normal faithful star isomorphism from \(M^{\mathrm{op}}\) onto \(N\). Normality also follows directly from bounded monotone convergence acting on each \(L^2\) vector, as proved in TI11. Define \(\tau_N(r_b)=\tau(b)\) for \(b\geq0\). The isomorphism transfers positivity, increasing suprema and finite trace ideals, so this is a faithful normal semifinite trace. This is the opposite trace, with its scale fixed.

For \(\xi\in H\), the normal positive functional \(\omega_\xi(x)=\langle x\xi,\xi\rangle\) has a unique density \(a_\xi\in L^1(M,\tau)_+\) by TI06. Spectral calculus and TI09 give \(h_\xi=a_\xi^{1/2}\in L^2(M,\tau)_+\). The tracial pairing of two \(L^2\) elements, proved by bounded approximation in TI10, gives

\[
 \begin{gathered}
 \langle x\xi,\xi\rangle
       =\langle xh_\xi,h_\xi\rangle,\\
 \|h_\xi\|_2^2=\|\xi\|^2 .
 \end{gathered}
 \tag{MR.2}
\]

Indeed the right pairing is \(\tau(h_\xi xh_\xi)=\tau(a_\xi x)\). A second positive implementing vector has the same squared \(L^1\) density by TI06 and hence the same positive square root. This proves uniqueness, including \(\xi=0\).

The prescription \(xh_\xi\mapsto x\xi\), for \(x\in M\), is an isometry between cyclic subspaces: apply (MR.2) to \(x^*x\), and to differences to check well-definedness. Extend it by continuity and by zero on the orthogonal complement of \(\overline{Mh_\xi}\). It is a bounded partial isometry \(u_\xi:L\to H\) intertwining the left actions, and \(u_\xi h_\xi=\xi\). Both cyclic subspaces reduce their left actions, which proves the intertwining assertion also on their complements.

Let \(s=s(h_\xi)\in M\). The initial projection is exactly

\[
 \begin{gathered}
 u_\xi^*u_\xi=r_s,\\
 \overline{Mh_\xi}=L s .
 \end{gathered}
 \tag{MR.3}
\]

The inclusion into \(L s\) follows from \(h_\xi s=h_\xi\). For the reverse inclusion put \(e_n=1_{[1/n,n]}(h_\xi)\). For every \(a\in M\cap L^2\), the bounded element \(a e_n h_\xi^{-1}\), with inverse zero off \(e_n\), multiplied by \(h_\xi\) equals \(a e_n\). These vectors belong to \(Mh_\xi\). First let \(n\) increase, using TI11, and then use density of \(M\cap L^2\) in \(L\). They are dense in \(L s\), proving (MR.3).

## Compatible traces on all commutants

For a representation on \(E\), write \(C_E=\pi_E(M)'\), and let \(I_M(E,F)\) be the bounded operators \(y:E\to F\) satisfying \(y\pi_E(x)=\pi_F(x)y\) for every \(x\in M\). There is a unique faithful normal semifinite trace \(\tau_E\) on \(C_E\) such that, for every \(y\in I_M(L,E)\),

\[
 \tau_E(yy^*)=\tau_N(y^*y).
 \tag{MR.4}
\]

Infinite values are allowed.

Here is the exact transfer from TM01. Regard a left \(M\)-module as a right \(Q=M^{\mathrm{op}}\)-module by \(\eta\cdot x^{\mathrm{op}}=\pi_E(x)\eta\). Equip \(Q\) with \(\tau_Q(x^{\mathrm{op}})=\tau(x)\). The linear map

\[
 \begin{gathered}
 L^2(Q,\tau_Q)\to L,\\
 \Lambda_{\tau_Q}(a^{\mathrm{op}})
           \mapsto\Lambda_\tau(a)
 \end{gathered}
 \tag{MR.5}
\]

is an onto isometry because the squared norms are \(\tau(aa^*)=\tau(a^*a)\). Right multiplication by \(x^{\mathrm{op}}\) becomes \(\lambda(x)\), whereas left multiplication by \(b^{\mathrm{op}}\) becomes \(r_b\). Thus TM01's endomorphism algebra is precisely \(C_E\), its columns are precisely \(I_M(L,E)\), and its reference trace is precisely \(\tau_N\). Its existence, semifiniteness and uniqueness proofs establish (MR.4) without an additional scalar choice. They allow arbitrary cyclic decompositions and even a zero module.

For any finite collection of representations take \(V=L\oplus E\oplus F\oplus G\), omitting unused summands, and put \(B=\pi_V(M)'\). Its canonical trace \(\Theta\) has corner restriction \(\tau_E\) on \(p_E Bp_E=C_E\). To check this restriction, TM01 shows it is faithful normal semifinite, and traciality applied to every column from \(L\) gives (MR.4); uniqueness identifies it. The same applies to every summand, with \(\tau_L=\tau_N\). Since \(I_M(E,F)=p_F Bp_E\), traciality in \(B\) proves, for every \(y\in I_M(E,F)\),

\[
 \tau_E(y^*y)=\tau_F(yy^*).
 \tag{MR.6}
\]

In particular the polar initial and final projections of a bounded intertwiner have equal traces. Adding further representations changes none of these normalizations.

## Measure neighborhoods respect rectangular corners

For \(\epsilon,\delta>0\), define \(U_{E,F}(\epsilon,\delta)\) to consist of the \(y\in I_M(E,F)\) for which a projection \(q\in C_E\) satisfies \(\|yq\|<\epsilon\) and \(\tau_E(1_E-q)<\delta\). Define \(V_E(\epsilon,\delta)\) to consist of the \(\eta\in E\) for which a projection \(q\in C_E\) satisfies \(\|q\eta\|<\epsilon\) and the same trace inequality. These are the operator and vector measure neighborhoods. The vector topology uses the commutant trace \(\tau_E\).

They are exactly the restrictions of the neighborhoods in MT03 for \((B,V,\Theta)\). For one direction replace \(q\) by the ambient projection

\[
 \begin{gathered}
 Q=q+(1-p_E),\\
 \Theta(1-Q)\\ =\tau_E(p_E-q).
 \end{gathered}
 \tag{MR.7}
\]

Then \(yQ=yq\), and \(Q\eta=q\eta\) when \(\eta\in E\). Conversely, if an ambient projection \(r\in B\) is a witness, put \(q=p_E\wedge r\). Projection comparison MT02 gives

\[
 \begin{gathered}
 \Theta(p_E-q)\\ \leq\Theta(1-r),\\
 \|yq\|\leq\|yr\|,\\
 \|q\eta\|\leq\|r\eta\|.
 \end{gathered}
 \tag{MR.8}
\]

For the trace inequality, \((p_E-q)\wedge r=0\), so \(p_E-q\) is subequivalent to \(1-r\). The norm inequalities follow from \(q\leq r\). No commuting-projection assumption enters this comparison.

For readability abbreviate \(U_{E,F}(\epsilon_i,\delta_i)\) by \(U^i_{E,F}\), and similarly for \(V^i_E\). Put \(\sigma=\epsilon_1+\epsilon_2\), \(\rho=\epsilon_1\epsilon_2\) and \(d=\delta_1+\delta_2\). The five estimates transferred from MT03 are

\[
 \begin{gathered}
 U_{E,F}(\epsilon,\delta)^*\\
        =U_{F,E}(\epsilon,\delta),\\
 U^1_{E,F}+U^2_{E,F}\\
        \subseteq U_{E,F}(\sigma,d),\\
 U^1_{F,G}U^2_{E,F}\\
        \subseteq U_{E,G}(\rho,d).
 \end{gathered}
 \tag{MR.9}
\]

\[
 \begin{gathered}
 V^1_E+V^2_E\\
        \subseteq V_E(\sigma,d),\\
 U^1_{E,F}V^2_E\\
        \subseteq V_F(\rho,d).
 \end{gathered}
 \tag{MR.10}
\]

Each product here has matching intermediate space. To see explicitly why the transferred estimates apply, extend each bounded intertwiner by zero to \(V\). Its adjoint, sum, composable product and action on a vector are exactly the ambient operations, with their indicated corner supports. Equations (MR.7)–(MR.8) identify both the input and output neighborhoods. Apply the corresponding MT03 estimate in \(B\), and restrict back to that output corner. Its adjoint estimate, based on spectral cutoffs and polar supports, even preserves \(\delta\).

The resulting topological vector spaces are Hausdorff by MT04 and the subspace identifications. They have countable neighborhood bases, obtained with both parameters \(2^{-n}\). A set is bounded in measure precisely when, for every \(\delta>0\), it lies in some \(U_{E,F}(R,\delta)\) or \(V_E(R,\delta)\) with finite \(R\). Thus corner boundedness is exactly ambient boundedness. MT04 now proves joint continuity and uniform continuity on products of bounded sets for composition and action; star and the two additions are uniformly continuous everywhere.

Let \(\mathcal S_M(E,F)\) and \(\widehat E\) be the respective Hausdorff completions. All five operations extend uniquely, with the same continuity properties. Composition has domain \(\mathcal S_M(F,G)\times\mathcal S_M(E,F)\) and target \(\mathcal S_M(E,G)\). The action has domain \(\mathcal S_M(E,F)\times\widehat E\) and target \(\widehat F\). Their formulas are

\[
 \begin{gathered}
 (c,a)\longmapsto ca,\\
 (a,\eta)\longmapsto a\eta.
 \end{gathered}
 \tag{MR.11}
\]

For completeness of the transfer, the continuous idempotents \(b\mapsto p_Fbp_E\) on the complete ambient algebra \(S(B,\Theta)\), and \(v\mapsto p_Ev\) on \(\widehat V\), have closed ranges. Applying these idempotents to bounded approximants proves that the original corners are dense in those ranges. Hence their ranges are exactly the asserted completions. MT05 proves the extensions on Cauchy representatives and their uniform estimates for completed bounded sets; the established equality of topologies and bounded sets transfers these conclusions too. Density makes every extension unique. These arguments treat arbitrary Cauchy nets, not only norm-bounded sequences.

## The completion consists of actual closed intertwiners

The preceding identifications give

\[
 \begin{gathered}
 \mathcal S_M(E,F)\\
       =p_F S(B,\Theta)p_E.
 \end{gathered}
 \tag{MR.12}
\]

For \(a\) in this corner define its ordinary operator from \(E\) to \(F\) on the domain \(D(T_a)=\{\eta\in E:a\eta\in F\}\), with action

\[
 T_a\eta=a\eta.
 \tag{MR.13}
\]

Here membership in \(F\) is tested inside its injective embedding in \(\widehat F\). This operator is closed, densely defined, and intertwines \(M\): its domain is invariant under every \(\pi_E(u)\), \(u\) a unitary in \(M\), and \(T_a\pi_E(u)=\pi_F(u)T_a\) on that domain. It has no proper closed intertwining extension. Every such measurable closed operator determines exactly one \(a\).

These assertions require a domain check. In the ambient construction MT08, \(a=ap_E=p_Fa\) implies that its realized operator vanishes on \(E^\perp\), that its domain is \(D(T_a)\oplus E^\perp\), and that its range lies in \(F\). This follows directly from the test in (MR.13) and the identities in the completed module. Thus its restriction is a closed densely defined rectangular operator. Affiliation with \(B\) gives the indicated intertwining because \(\pi_V(M)\subseteq B'\).

Conversely, extend any densely defined closed intertwiner \(T:E\to F\) by zero on \(E^\perp\). Its graph is reducing for each diagonal \(\pi_V(u)\) on \(V\oplus V\). The entries of its graph projection consequently lie in \(B\). They commute with every element of \(B'\), so the graph is invariant under diagonal unitaries from \(B'\); this is precisely affiliation of the zero extension with \(B\). This argument does not assume a new assertion about closure of a representation's image.

The zero extension is \(\Theta\)-measurable exactly when, for every \(\delta>0\), some \(q\in C_E\) has \(\tau_E(1_E-q)<\delta\) and \(qE\subseteq D(T)\). Indeed (MR.7)–(MR.8) transfer the trace-dense domain criterion MT11 in both directions. The closed graph theorem makes \(Tq\) bounded; domain invariance and commutation of \(q\) with the left action make it a bounded intertwiner. Equivalently the spectral tails of \(|T|\), computed in \(C_E\), tend to zero in \(\tau_E\). MT08 now proves uniqueness of the completion element. A proper closed intertwining extension would give a proper closed affiliated extension of its zero extension, forbidden by MT08; the larger extension need not itself have been assumed measurable.

For \(a,b\in\mathcal S_M(E,F)\) and \(c\in\mathcal S_M(F,G)\), the exact operator laws are

\[
 \begin{gathered}
 T_{a^*}=T_a^*,\\
 T_{a+b}=\overline{T_a+T_b},\\
 T_{ca}=\overline{T_cT_a}.
 \end{gathered}
 \tag{MR.14}
\]

The sum's ordinary domain is \(D(T_a)\cap D(T_b)\). The composition's ordinary domain is the set of \(\eta\in D(T_a)\) with \(T_a\eta\in D(T_c)\). Both domains are dense and their operators are closable. Apply MT09 to their zero extensions: the ordinary ambient sum and product have these domains plus \(E^\perp\), on which they are zero. Taking graph closures commutes with this orthogonal zero summand, giving exactly (MR.14). The same observation identifies the adjoint rectangular block. Associativity of closed composable products follows from the completed ambient algebra, not from unrestricted multiplication of unbounded operators.

There is also a full increasing-domain version. Suppose \(q_n\in C_E\) increases, \(\tau_E(1_E-q_n)\to0\), and a single linear map \(A:\bigcup_n q_nE\to F\) has bounded intertwining compressions \(Aq_n\). Then for a unique \(a\in\mathcal S_M(E,F)\),

\[
 \overline A=T_a.
 \tag{MR.15}
\]

Extend \(A\) by zero on \(E^\perp\) and use the increasing projections \(q_n+(1-p_E)\). Their trace defects tend to zero and all compressions belong to \(B\). MT10 gives the unique affiliated closure; its supports remain \(p_F,p_E\), because all bounded compressions have these supports and multiplication by fixed projections is continuous. Restriction proves (MR.15), including that the displayed union is a graph core. This proves all domain and maximality statements, not just an abstract completeness assertion.

## Every vector is a square-integrable intertwiner

For a positive \(h\in L^2(M,\tau)\), define the positive operator \(r_h\) on \(L\) by transporting its spectral projections under the normal opposite isomorphism (MR.1). Its spectral integral is well defined by SK05; its high tails have trace at most \(t^{-2}\|h\|_2^2\). It is therefore \(\tau_N\)-measurable. For every \(x\in\mathfrak n_\tau=M\cap L^2\),

\[
 \begin{gathered}
 \Lambda_\tau(x)\in D(r_h),\\
 r_h\Lambda_\tau(x)=xh,\\
 \tau_N(r_h^2)=\tau(h^2).
 \end{gathered}
 \tag{MR.16}
\]

To prove the domain assertion, let \(h_n=h1_{[0,n]}(h)\). The spectral truncations satisfy \(r_{h_n}\Lambda_\tau(x)=xh_n\). TI10's bounded multiplier estimate gives \(xh_n\to xh\) in \(L^2\). The exact spectral domain criterion SK05 then puts \(\Lambda_\tau(x)\) in \(D(r_h)\) with the stated value. The trace equality follows first for positive simple spectral functions from the definition of \(\tau_N\), and then by monotone convergence.

The subspace \(\Lambda_\tau(\mathfrak n_\tau)\) is a graph core for \(r_h\). Its spectral truncations are \(r_{e_n}\), with \(e_n=1_{[0,n]}(h)\). They approximate every vector in the graph norm of \(r_h\). For each fixed \(n\), approximate a vector in \(L\) by \(\Lambda_\tau(x_j)\), \(x_j\in\mathfrak n_\tau\), and apply \(r_{e_n}\). The resulting vectors are \(\Lambda_\tau(x_j e_n)\), still in that ideal, and \(r_h r_{e_n}\) is bounded. This approximates each truncated graph and proves the core assertion.

Using MR01, set \(R_\xi=u_\xi r_{h_\xi}\) on \(D(r_{h_\xi})\). This ordinary composition is already closed: the range of \(r_{h_\xi}\) is in \(r_sL\), and \(u_\xi\) is an isometry there. Thus convergence of \(R_\xi\eta_n\) is equivalent, after applying \(u_\xi^*\), to convergence of \(r_{h_\xi}\eta_n\). Closedness of the latter gives closedness of the former. Its modulus is \(r_{h_\xi}\), it intertwines \(M\), and its spectral tails prove measurability by MR04. Equation (MR.16) and the intertwining of \(u_\xi\) show

\[
 \begin{gathered}
 R_\xi\Lambda_\tau(x)=x\xi,\\
 R_\xi^*R_\xi=r_{h_\xi}^2,\\
 \tau_N(R_\xi^*R_\xi)\\ =\|\xi\|^2.
 \end{gathered}
 \tag{MR.17}
\]

In particular the squared modulus belongs to \(L^1(N,\tau_N)\). The same graph core works after the isometry \(u_\xi\). Hence the initially defined map \(\Lambda_\tau(x)\mapsto x\xi\) is closable and its closure is precisely \(R_\xi\). This supplies its whole domain, not just some closed extension.

Conversely take \(T\in\mathcal S_M(L,H)\) with \(\tau_N(T^*T)<\infty\). Its polar decomposition has a bounded intertwining partial isometry \(v:L\to H\); its modulus is affiliated with \(N\). Transfer the spectral projections of \(|T|\) back through (MR.1) to obtain a unique positive affiliated \(h\) on the original representation of \(M\). Spectral integration gives \(|T|=r_h\) and \(\tau(h^2)=\tau_N(T^*T)<\infty\). The same tail estimate makes \(h\) measurable, so \(h\in L^2(M,\tau)_+\). The initial projection of \(v\) is \(r_{s(h)}\). Define the actual vector \(\xi=vh\in H\). For every \(x\in\mathfrak n_\tau\),

\[
 \begin{gathered}
 T\Lambda_\tau(x)=v(xh),\\
 v(xh)=x\xi .
 \end{gathered}
 \tag{MR.18}
\]

The core argument for \(r_h\), and isometry of \(v\) on its support, show that this ideal is also a core for \(T\). Therefore \(T=R_\xi\). Uniqueness of \(\xi\) can be checked without a formal vector \(\Lambda_\tau(1)\): equality of the operators gives \(e\xi=e\eta\) for every finite-trace projection \(e\in M\), and these projections increase strongly to one by TI01 and normality of the representation. Thus \(\xi=\eta\).

Define \(\mathcal L_M^2(H)\) as these square-integrable intertwiners, with the closed sum and scalar operations. Corner restriction of TI09–10 gives its Hilbert pairing \(\langle T,S\rangle_2=\tau_N(S^*T)\). Then

\[
 \begin{gathered}
 H\longrightarrow\mathcal L_M^2(H),\\
 \xi\longmapsto R_\xi,\\
 \langle R_\xi,R_\eta\rangle_2\\
             =\langle\xi,\eta\rangle
 \end{gathered}
 \tag{MR.19}
\]

is an onto linear isometry. Surjectivity and the norm identity were proved above. For linearity, the closed sum of two \(L^2\) columns is again an \(L^2\) column by TI09 and the corner identification. On the common initial ideal it takes the value \(x(\xi+\eta)\). Its surjectivity representation and the uniqueness test just given identify it with \(R_{\xi+\eta}\); the scalar argument is identical. Polarization gives the pairing identity and also proves completeness from that of \(H\).

For \(a'\in C_H\) and \(b\in M\), bounded multiplication on these columns satisfies

\[
 \begin{gathered}
 a'R_\xi=R_{a'\xi},\\
 R_\xi r_b=R_{b\xi},\\
 \|a'T\|_2\\ \leq\|a'\|\|T\|_2,\\
 \|T r_b\|_2\\ \leq\|b\|\|T\|_2 .
 \end{gathered}
 \tag{MR.20}
\]

The estimates are TI10's bounded multiplier inequalities in the linking algebra. For the first identity use \(a'x\xi=xa'\xi\) on the initial ideal, followed by the preceding uniqueness argument. For the second, \(xb\in\mathfrak n_\tau\), and the ordinary product gives \(R_\xi r_b\Lambda_\tau(x)=xb\xi\). Its closed extension is the measurable product by MR04 and is an \(L^2\) column; surjectivity and uniqueness prove the identity. These are commuting normal left \(C_H\)- and right \(N\)-actions. Normality follows by transporting them through (MR.19) to the given normal actions on \(H\); for the right action use the normal opposite identification (MR.1). The order reversal in \(r_b r_c=r_{cb}\) is essential for this right module convention.

Finally perform the same construction with \((C_H,\tau_H)\) acting on \(H\). Its commutant is the original concrete \(M\). There is an onto isometry

\[
 H\longrightarrow\mathcal L_{C_H}^2(H)
 \tag{MR.21}
\]

whose target consists of measurable operators from \(L^2(C_H,\tau_H)\) to \(H\). Left multiplication by \(x\in M\) corresponds to the original vector action of \(x\) on \(H\), by (MR.20) for this new algebra. All hypotheses hold because MR02 proved \(\tau_H\) faithful normal semifinite. Thus the reciprocal construction retains the specified original action rather than only producing an abstract isomorphic Hilbert space.

## Scale, orientation and domain checks

**A scalar algebra with arbitrary multiplicity.** Let \(M=\mathbb C\), \(\tau(z)=cz\) for \(z\geq0\), with \(c>0\), acting on any Hilbert space \(H\). Then \(L=\mathbb C\) with \(\|z\|_L^2=c|z|^2\), and \(C_H=B(H)\). The normalization is

\[
 \begin{gathered}
 \tau_H=c\operatorname{Tr}_H,\\
 R_\xi(z)=z\xi .
 \end{gathered}
 \tag{MR.22}
\]

Indeed \(R_\xi^*R_\xi\) is the scalar \(\|\xi\|^2/c\), whereas \(R_\xi R_\xi^*\) is \(c^{-1}\) times the rank-one operator with vector \(\xi\). Both normalized traces equal \(\|\xi\|^2\). Rank-one columns and monotone finite sums force the stated trace on all of \(B(H)_+\), also for nonseparable \(H\). Every nonzero projection has trace at least \(c\), so a defect smaller than \(c\) must be zero. All these measure topologies are consequently norm topologies, and the operator completions introduce no unbounded operators. This is compatible with every vector giving a bounded map out of the one-dimensional reference space.

**Multiplication on a finite measure space.** In the representation of MM01–03, take \(M=L^\infty(X,\mu)\), \(H=L^2(X,\mu)\), \(\tau(f)=\int f\,d\mu\), and \(\mu(X)<\infty\). The commutants agree with \(M\), and the canonical trace is the same integral: testing bounded multiplication columns in (MR.4) verifies its normalization and MR02 gives uniqueness. Here \(R_\xi\) is the maximal multiplication operator by \(\xi\), whose domain consists of those \(f\in L^2\) for which \(f\xi\in L^2\), and whose action is

\[
 R_\xi f=f\xi.
 \tag{MR.23}
\]

MM02 proves this maximal domain is closed. Equation (MR.17) gives \(\|R_\xi\|_2=\|\xi\|_{L^2}\). A vector need not be an essentially bounded function; its column is nevertheless measurable and has the whole stated domain.

**Why a bounded left factor still needs closure.** The ordinary composition \(a'R_\xi\) need not be closed when \(a'\) has a kernel. For example, use \(X=(0,1)\), \(\xi(t)=t^{-1/4}\) and \(a'=0\). The domain is dense but proper, since \(\xi\in L^2\) whereas \(\xi^2\notin L^2\), and therefore is not a closed subspace. The ordinary product is zero only on that proper dense domain. Its closure is the everywhere defined zero operator, as required by (MR.20). Our construction \(u_\xi r_{h_\xi}\) is already closed for the separate reason that \(u_\xi\) is isometric on the entire range of \(r_{h_\xi}\).

**Why the initial ideal replaces a unit vector.** If \(\tau(1)=\infty\), there is no trace GNS vector \(\Lambda_\tau(1)\). To recover a vector from its column, use finite-trace projections and the equalities \(R_\xi\Lambda_\tau(e)=e\xi\); normality gives \(e\xi\to\xi\). This is exactly the injectivity argument in MR05 and requires neither a countable exhaustion nor a cyclic representation.

All eleven source clauses are represented: positive implementing vectors and their initial operators, uniquely normalized commutant traces and cross-representation compatibility, both measure topologies and all five extended operations, closed-operator maximality and increasing-domain realization, the full square-integrable column correspondence, and its two actions and reciprocal construction.
