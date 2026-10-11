# Extended center-valued traces

A scalar trace assigns a size to a positive operator. When the algebra has a center, one can retain the size on every central part at once. The resulting value can be unbounded, and can also be infinite on a central summand. These two possibilities must be distinguished to recognize finite projections.

Let \(M\) be a von Neumann algebra and \(Z=Z(M)\). There is no countability or separability assumption. We include the zero algebra, for which all assertions have their unique empty or zero interpretation. Scalar arithmetic in \([0,\infty]\) uses \(0\cdot\infty=0\). Products of central extended positives will be defined by order limits.

## The center's extended positive cone and its spectrum

Use the extended positive cone of \(Z\): its elements are additive, nonnegatively homogeneous, norm lower semicontinuous functions on \(Z_*^+\), with value zero at zero. Its order is pointwise on these normal functionals. The spectral description and bounded resolvent from CW-09–10 write each element uniquely as
\[
 \begin{gathered}
 H=h+\infty p,\\
 R_H=\\
 (1+h)^{-1}(1-p).
 \end{gathered}
 \tag{EC.1}
\]
Here \(p\in Z\) is a projection and \(h\) is a positive densely defined self-adjoint operator on \((1-p)\mathcal H\), affiliated with \(Z(1-p)\). The coordinate \(R_H\) ranges over all positive contractions of \(Z\), and reverses order. Write \(H\wedge n=\min(h,n)(1-p)+np\). These bounded elements increase to \(H\).

Let \(\Omega\) be the character space of \(Z\). The exact earlier programme commutative Gelfand theorem, Theorem 2.1 identifies \(Z\) with \(C(\Omega)\). Thus
\[
 \begin{gathered}
 f_H(\omega)=\\
 R_H(\omega)^{-1}-1,\\
 0^{-1}=\infty
 \end{gathered}
 \tag{EC.2}
\]
is an order-preserving bijection from \(\widehat Z_+\) to the continuous functions \(\Omega\to[0,\infty]\). The topology on the target interval is the one obtained from \(t\mapsto(1+t)^{-1}\). Conversely this transformation of any such continuous function gives a positive contraction, so (EC.2) is onto. We freely identify \(H\) with \(f_H\).

We record the needed topology, including the difference between operator support and pointwise positivity. Projections correspond to clopen subsets of \(\Omega\). These subsets form a base. Indeed a basic neighborhood of a character is specified by finitely many inequalities \(|a_j(\omega)-a_j(\omega_0)|<\delta_j\). The product of the positive continuous functions \((\delta_j-|a_j-a_j(\omega_0)|)_+\) is positive at \(\omega_0\) and zero outside that neighborhood. Call it \(b\). Choose \(0<\varepsilon<b(\omega_0)\) and take its spectral projection \(q=1_{[\varepsilon,\infty)}(b)\). The inequalities \(b\leq\varepsilon 1+\|b\|q\) and \(bq\geq\varepsilon q\) show respectively that \(q(\omega_0)=1\) and that the clopen set of \(q\) is contained in the neighborhood. These projections are supplied by bounded Borel spectral calculus. More explicitly, bounded continuous functions decreasing to \(1_{[\varepsilon,\infty)}\) give operators in \(Z\) by continuous calculus; their strong limit is \(q\), which belongs to \(Z\) because \(Z\) is strongly closed.

For any family of projections \(q_i\), the clopen set of \(q=\bigvee_iq_i\) is the closure of the union of their clopen sets. The union is contained in that of \(q\). If a point of the latter were outside its closure, the clopen base would give a nonzero projection \(r\leq q\) orthogonal to all \(q_i\); then \(r q=0\), a contradiction. To construct the join, for each finite subset \(F\) of indices put \(q_F=1-\prod_{i\in F}(1-q_i)\), with \(q_{\varnothing}=0\). Commutativity makes this a projection, and these projections increase with \(F\). Their strong supremum \(q\in Z\) exists by bounded monotone convergence. Bounded strong convergence gives \(q_F^2\to q^2\) strongly, so \(q^2=q\); any projection dominating all \(q_i\) dominates every \(q_F\) and therefore \(q\). Thus \(q\) is the required join. Every open set is a union of clopen sets, so its closure is open. This is the Stonean property needed below.

In particular, for bounded \(b\in Z_+\), the closure of \(\{b>0\}\) is the clopen set of \(s(b)\): use the projections \(1_{[1/n,\infty)}(b)\), their join, and the two preceding spectral inequalities. Applying this fact to \(R_H\) and \(1-R_H\) gives
\[
 \begin{gathered}
 p=0\\
 \Longleftrightarrow\\
 \{f_H<\infty\}\\
 \text{is dense},\\
 \ker h=0\text{ and }p=0\\
 \Longleftrightarrow\\
 \{0<f_H<\infty\}\\
 \text{is dense}.
 \end{gathered}
 \tag{EC.3}
\]
In the last equivalence the kernel is on \((1-p)\mathcal H\). Both sets displayed are open. For the second equivalence, the two open sets \(\{f_H<\infty\}\) and \(\{f_H>0\}\) must both be dense; their intersection is then dense. The kernel of \(1-R_H\) is exactly the zero spectral part of \(h\).

Addition and nonnegative scalar multiplication correspond to pointwise addition and scalar multiplication of continuous extended functions. For addition, \((H\wedge n)+(K\wedge n)\uparrow H+K\) by CW-09, and the pointwise supremum \(f_H+f_K\) is itself continuous and hence is their least upper bound. The same argument proves scaling; scalar zero gives the zero function. An arbitrary increasing supremum is instead the least continuous upper bound, and need not be the pointwise supremum on \(\Omega\).

For \(a\in Z_+\), define
\[
 aH=\sup_n a(H\wedge n).
 \tag{EC.4}
\]
This is the congruence \(a^{1/2}Ha^{1/2}\) of CW-09. Consequently it is additive, associative for bounded central factors, and preserves increasing suprema in \(H\). It also preserves bounded increasing suprema in \(a\): first check this against every normal functional for bounded \(H\wedge n\), then interchange the two nonnegative suprema. On an open set where \(f_H\) is bounded it is ordinary multiplication. To see this, restrict to each clopen subset there and use a sufficiently large cutoff in (EC.4); the clopen base covers the set. Where \(a>0\) and \(f_H=\infty\), its value is infinity, by the same local argument with \(a\) bounded below. At a point where \(a=0\) and \(f_H=\infty\), a separate pointwise convention need not give the continuous answer. EC-06 gives an explicit example.

## Scalar tests on the center

There is a faithful normal semifinite trace \(\mu\) on the abelian algebra \(Z\). Here is a construction that does not assume a faithful normal state. Positive normal functionals separate positive elements by CP-07. Their support projections and faithful restrictions are given by TB-03, since every positive functional on an abelian algebra is tracial. Choose a maximal family of normal states \(\mu_j\) with orthogonal nonzero supports \(z_j\). If the join of the supports were not one, separation on the complementary summand would supply another such state. Thus \(\sum_jz_j=1\).

Set \(\mu(a)=\sum_j\mu_j(a)\) for \(a\in Z_+\), with arbitrary sums interpreted as suprema of finite subsums. This is a normal weight: directed increasing limits commute with finite sums and with the supremum over finite subsets. It is faithful because each state is faithful on its support. The central projections \(q_F=\sum_{j\in F}z_j\), for finite \(F\), increase to one and satisfy \(\mu(q_F)=|F|\). Thus \(q_Fa\uparrow a\), with \(\mu(q_Fa)\leq |F|\|a\|\), which proves semifiniteness. This construction also supplies finite-\(\mu\) central cutoffs for later use.

Extend \(\mu\) to \(\widehat Z_+\) by CW-03; write the extension simply as \(\mu(H)\). It preserves addition, scaling and increasing suprema, and is faithful: \(\mu(H)=0\) forces \(\mu(H\wedge n)=0\), hence every cutoff and then \(H\) to be zero.

**Central density theorem.** Every normal weight \(\nu\) on \(Z\), including weights which are not semifinite, has a unique \(H\in\widehat Z_+\) such that
\[
 \begin{gathered}
 \nu(a)=\mu(aH),\\
 a\in Z_+.
 \end{gathered}
 \tag{EC.5}
\]
This correspondence is additive, order preserving and order reflecting, and preserves increasing suprema.

**Proof.** This is CW-11 for the reference trace \(\mu\). A faithful semifinite trace has identity modular operator: on its tracial GNS core the map \(\Lambda(x)\mapsto\Lambda(x^*)\) is an isometry, so its closure is antiunitary and its polar positive part is one. This is the trace specialization also used in PT-08. Thus every normal weight on \(Z\) is invariant under the reference modular group. CW-11 includes the infinite spectral part and proves both existence and order reflection. In this abelian algebra its bounded sandwich formula is \(\mu(aH_\varepsilon)\). Taking increasing limits, (EC.4) and CW-03 identify that formula with (EC.5). Additivity follows from addition of extended positives and the additivity of \(\mu\). Preservation of increasing suprema is CW-11, or follows by interchanging the two suprema. \(\square\)

In particular, all scalar tests in (EC.5) may be used to prove equality or order of central extended positives. If \(\mu(H)<\infty\), its infinite projection is zero: a nonzero infinite projection \(p\) would give \(H\geq np\) for every \(n\) and \(\mu(p)>0\). Its remaining affiliated operator can still be unbounded.

## Definition, finite ideal, and existence

An **extended center-valued trace** is a map \(T:M_+\to\widehat Z_+\) which is additive and satisfies
\[
 \begin{gathered}
 T(ax)=aT(x),\\
 a\in Z_+,\\
 T(v^*v)=T(vv^*),\\
 v\in M.
 \end{gathered}
 \tag{EC.6}
\]
It is **faithful** if \(T(v^*v)=0\) implies \(v=0\), and **normal** if it preserves bounded increasing positive suprema. It is **semifinite** if
\[
 \begin{gathered}
 \mathcal N_T=\{v\in M:\\
 T(v^*v)\in Z_+\}
 \end{gathered}
 \tag{EC.7}
\]
is ultraweakly dense in \(M\). Membership in \(Z_+\) here means bounded, not merely finite on an open dense subset. Taking the central scalar zero in (EC.6) gives \(T(0)=0\). Additivity therefore implies order preservation.

**Finite ideal.** The set \(\mathcal N_T\) is a linear, self-adjoint, two-sided ideal. Indeed \((v+w)^*(v+w)\leq2(v^*v+w^*w)\) proves closure under addition; scalar homogeneity proves closure under scaling. The trace identity proves closure under adjoints. For \(b\in M\),
\[
 \begin{gathered}
 T((bv)^*(bv))\\
 \leq\|b\|^2T(v^*v),\\
 T((vb)^*(vb))\\
 =T(vbb^*v^*)\\
 \leq\|b\|^2T(vv^*).
 \end{gathered}
 \tag{EC.8}
\]
An extended positive bounded above by a bounded positive is bounded, by either (EC.2) or its spectral cutoffs. Thus both products remain in \(\mathcal N_T\).

**Existence theorem.** The algebra \(M\) is semifinite if and only if it has a faithful normal semifinite extended center-valued trace.

**Construction from a scalar trace.** For semifinite \(M\), TE-11 supplies a faithful normal semifinite scalar trace \(\tau\). Choose \(\mu\) on \(Z\) as in EC-02. For \(x\in M_+\), the formula \(\nu_x(a)=\tau(ax)\) defines a normal weight on \(Z\). Centrality makes the product positive and additive in \(a\); bounded increasing nets are preserved by multiplication by \(x\) and normality of \(\tau\). Define \(T(x)\) to be its unique density:
\[
 \begin{gathered}
 \mu(aT(x))\\
 =\tau(ax),\\
 a\in Z_+,\\
 \tau(x)=\mu(T(x)).
 \end{gathered}
 \tag{EC.9}
\]
The scalar tests prove additivity of \(T\) and its central module identity. For the trace identity apply the scalar trace identity to \(va^{1/2}\), obtaining \(\tau(av^*v)=\tau(avv^*)\). If \(x_i\uparrow x\), these same tests and EC-02 give \(T(x_i)\uparrow T(x)\). Faithfulness follows from (EC.9) and that of \(\tau\). This verifies every axiom, including normality at infinite values.

To prove semifiniteness, take \(v\) in the scalar finite ideal \(\mathfrak n_\tau\). Then \(\mu(T(v^*v))=\tau(v^*v)<\infty\), so EC-02 shows that \(T(v^*v)\) has no infinite part. Let \(z_n=1_{[0,n]}(T(v^*v))\). These central projections increase strongly to one. The module identity gives \(T((z_nv)^*(z_nv))\leq nz_n\), hence \(z_nv\in\mathcal N_T\) and \(z_nv\to v\) strongly, with a uniform norm bound. The scalar ideal \(\mathfrak n_\tau\) is ultraweakly dense by TB-02. Therefore \(\mathcal N_T\) is ultraweakly dense as well. Bounded strong convergence implies ultraweak convergence by CP-06.

**Composition and converse.** Conversely, let \(T\) have the three asserted properties and choose \(\mu\) from EC-02. The composition \(\tau(x)=\mu(T(x))\) is a faithful normal scalar trace, by the extended additivity and normality of \(\mu\). It is semifinite. Indeed for \(v\in\mathcal N_T\) put \(C=\|T(v^*v)\|\). The finite-\(\mu\) projections \(q_F\uparrow1\) from EC-02 satisfy
\[
 \begin{gathered}
 \tau((q_Fv)^*(q_Fv))\\
 =\mu(q_FT(v^*v))\\
 \leq C\mu(q_F)<\infty.
 \end{gathered}
\]
Thus every \(v\in\mathcal N_T\) is in the ultraweak closure of \(\mathfrak n_\tau\), which is consequently dense in \(M\). TB-02 proves semifiniteness of \(\tau\), and TE-11 gives semifiniteness of \(M\). This also proves, for later use, that composition with this faithful central reference is always faithful normal semifinite. \(\square\)

## Uniqueness up to an invertible central density

If \(c\) is a densely defined positive self-adjoint operator affiliated with \(Z\) and has zero kernel, define
\[
 \begin{gathered}
 cH=\\
 \sup_n(c\wedge n)H.
 \end{gathered}
 \tag{EC.10}
\]
This product is an order automorphism of \(\widehat Z_+\), with inverse multiplication by \(c^{-1}\). To check every assertion, cut by \(z_n=1_{[1/n,n]}(c)\uparrow1\). On each such central summand both factors \(c\) and \(c^{-1}\) are bounded and mutually inverse. The bounded calculus (EC.4) proves the identities there. Equality on all these summands implies equality globally, since \(z_nH\uparrow H\), by the normality in the central factor proved in EC-01. The same cutoffs prove additivity and preservation of increasing suprema. On the open dense set \(\{0<c<\infty\}\), this operation agrees with pointwise multiplication, including an infinite value of \(H\); locally bound \(c\) and its inverse and use clopen restrictions.

**Comparison theorem.** If \(T_1,T_2\) are faithful normal semifinite extended center-valued traces, there is a unique such \(c\) with
\[
 \begin{gathered}
 T_2(x)=cT_1(x),\\
 x\in M_+.
 \end{gathered}
 \tag{EC.11}
\]
Equivalently, \(c\) is a continuous extended central function with \(0<c<\infty\) on an open dense subset of \(\Omega\). Conversely multiplication by any such \(c\) produces another faithful normal semifinite extended center-valued trace.

**Proof of comparison.** Fix the same \(\mu\) for both traces. By EC-03 the scalar traces \(\tau_j=\mu\circ T_j\) are faithful normal semifinite. The central density theorem for scalar traces, using PT-08, gives a unique positive densely defined affiliated density \(c\) of \(\tau_2\) relative to \(\tau_1\). Its spectral projections are central. Its support is one by faithfulness of \(\tau_2\), so it has zero kernel.

For every bounded positive \(y\), its scalar density formula can be written \(\tau_2(y)=\sup_n\tau_1((c\wedge n)y)\). The bounded regularizations in TR-01 and these truncations increase to the same extended positive \(c\); CW-03 gives equality of the two evaluations. Hence for \(a\in Z_+\),
\[
 \begin{aligned}
 \mu(aT_2(x))
 &=\tau_2(ax)\\
 &=\sup_n\tau_1(a(c\wedge n)x)\\
 &=\sup_n\mu(a(c\wedge n)T_1(x))\\
 &=\mu(acT_1(x)).
 \end{aligned}
\]
The central tests in EC-02 now prove (EC.11). If another density \(d\) gave the same identity, composition with \(\mu\) would make \(\tau_{1,d}=\tau_2\); the uniqueness in PT-08 gives \(d=c\), including equality of domains. The spectral characterization in (EC.3) proves the stated open dense formulation.

**Proof of the converse.** The order automorphism (EC.10) preserves the defining identities, faithfulness and normality. For semifiniteness, if \(v\in\mathcal N_{T_1}\), then \(z_nv\in\mathcal N_{cT_1}\), because \(cz_n\leq nz_n\) and \(T_1(v^*v)\) is bounded. The bounded net \(z_nv\) converges strongly to \(v\), and the density of \(\mathcal N_{T_1}\) finishes the proof. \(\square\)

The orientation in (EC.11) is fixed: \(c\) is the density of the second scalar trace relative to the first. Reversing the equation uses \(c^{-1}\). Neither density is required to be bounded or trace measurable.

## Detecting finite projections

We first prove the corner fact required to use the comparison theorem. If \(e\) is a projection and \(z\) its central carrier, then
\[
 \begin{gathered}
 \theta:Zz\\
 \longrightarrow Z(eMe),\\
 \theta(a)=ae
 \end{gathered}
 \tag{EC.12}
\]
is a normal unital star isomorphism. To construct the carrier, the closed space \(\overline{Me\mathcal H}\) is invariant under \(M\) and \(M'\), including their adjoints. Its orthogonal projection \(z\) is central, contains \(e\), and is contained in every central projection containing \(e\).

Injectivity of \(\theta\) follows because a central \(a=az\) with \(ae=0\) vanishes on the dense space \(Me\mathcal H\) in \(z\mathcal H\). For surjectivity, let \(b\in Z(eMe)\). On that dense linear space define
\[
 B\Bigl(\sum_i x_i e\xi_i\Bigr)
 =\sum_i x_i b\xi_i.
\]
This is well defined and bounded by \(\|b\|\). Indeed the positive matrix \(C=(e x_i^*x_j e)_{ij}\) acting on \((e\mathcal H)^n\) commutes with the diagonal operator \(D=\operatorname{diag}(b,\ldots,b)\). Thus \(D^*CD\leq\|b\|^2C\); evaluating this inequality at \((e\xi_i)_i\) is precisely the squared norm bound. Extend \(B\) by zero off \(z\mathcal H\). Its defining equation shows that it commutes with \(M\), and it commutes with \(M'\) since all \(x_i,b,e\) do. Hence \(B\in Zz\), and \(Be=b\). This proves surjectivity. Multiplication, adjoints and the unit are preserved by \(\theta\), and its inverse follows the same identities by injectivity. The map is normal since multiplication by \(e\) preserves bounded increasing suprema. Its inverse is normal too: lift a bounded increasing positive net, take its supremum in \(Zz\), and apply \(\theta\) and uniqueness. These operations extend to the extended cones by their bounded resolvent coordinates, preserving infinite projections and boundedness.

**Finite-projection criterion.** Let \(T\) be a faithful normal semifinite extended center-valued trace on \(M\). A projection \(e\) is finite if and only if \(T(e)\) is finite on an open dense subset of \(\Omega\).

**A finite extended value forces finiteness.** Suppose \(T(e)\) has no infinite projection, equivalently the open dense property in (EC.3). Put \(z_n=1_{[0,n]}(T(e))\uparrow1\). If \(v^*v=e\) and \(vv^*=f\leq e\), the trace identity gives \(T(f)=T(e)\). Additivity gives
\[
 z_nT(e)=z_nT(f)+z_nT(e-f).
\]
The first two terms are equal bounded positives, so their cancellation gives \(T(z_n(e-f))=0\). The element \(z_n(e-f)\) is a projection; faithfulness makes it zero. Taking the increasing supremum gives \(e=f\). This is the definition of finiteness. Cancellation has been used only after the values are bounded.

**Finiteness forces a finite extended value.** The case \(e=0\) is immediate. Otherwise let \(z\) be its carrier and use (EC.12). For \(x\in(eMe)_+\), the module identity gives \((1-z)T(x)=0\). Define \(T_e(x)=\theta(T(x))\), using the extended-cone isomorphism on the supported value. This is a faithful normal extended center-valued trace on \(eMe\). It is semifinite: \(e\mathcal N_Te\subseteq\mathcal N_T\) by the two-sided ideal property, its images have bounded \(T_e\)-squares, and it is ultraweakly dense in \(eMe\), since compression is ultraweakly continuous, the corner carries the inherited ultraweak topology by the ultraweak topology of corners, and \(\mathcal N_T\) is dense in \(M\).

Because \(e\) is finite, CT-03–04 supplies the canonical faithful normal center-valued trace \(S\) on \(eMe\), with \(S(e)=e\). Its values are bounded, so its finite ideal is the whole corner. Apply EC-04 in \(eMe\), obtaining \(T_e=cS\) with \(c\) positive, injective and densely defined. In particular \(T_e(e)=c\) has no infinite projection. Transport back by \(\theta\): \(T(e)\) has no infinite part on \(z\), and is zero on \(1-z\). Formula (EC.3) proves the required open dense property on all of \(\Omega\). \(\square\)

## Three checks at infinity

**An unbounded value on a finite unit.** Take \(M=Z=\ell^\infty(\mathbb N)\), acting diagonally on \(\ell^2(\mathbb N)\). Let \(c\) have diagonal entries \(n\), with domain consisting of the vectors \(\xi\) for which \(\sum_n n^2|\xi_n|^2<\infty\), and put \(T(a)=ca\), with product defined by (EC.10). This is a densely defined positive self-adjoint operator with zero kernel, by diagonal spectral calculus. The identity map is a faithful normal finite center-valued trace, so EC-04 proves that \(T\) is faithful normal semifinite. The unit is finite because in an abelian algebra \(v^*v=vv^*\). Yet \(T(1)=c\) is unbounded. Every coordinate projection is a clopen point in the spectrum, and their union is dense by EC-01. The function \(c\) is finite on those points and infinite at every remaining character: \((1+c)^{-1}\) is a sequence tending to zero, hence is a norm limit of finite-coordinate sequences and vanishes at all such characters. There are remaining characters, since an infinite discrete set of clopen points cannot by itself be compact. Thus the finite-projection criterion cannot replace “finite on an open dense subset” by “bounded” or by “finite everywhere.”

**Why the central product needs order limits.** In the same example take the bounded sequence \(b_n=1/n\). On each coordinate, \(bc=1\), and the projections onto the first \(n\) coordinates increase to one, so (EC.4) gives \(bc=1\) globally. At every remaining character \(b=0\) and \(c=\infty\). A pointwise prescription \(0\cdot\infty=0\) there would contradict both continuity and the operator product. The scalar convention remains valid; it does not replace the definition of multiplying central functions with singular boundary values.

**Why semifiniteness cannot be omitted.** On \(M=\mathbb C\) define \(T(0)=0\) and \(T(t)=\infty\) for \(t>0\). The central module identity and trace identity hold, and this map is faithful. It is normal: a positive increasing net with positive supremum has a positive member; at supremum zero all members vanish. But \(\mathcal N_T=\{0\}\), so it is not semifinite. Its finite unit has infinite value on the one-point spectrum. This is exactly the hypothesis used in the reverse implication of EC-05 and in the comparison theorem.

The mathematical antecedent is Masamichi Takesaki, *Theory of Operator Algebras I*, V.2, Definition 2.33, Theorem 2.34 and Proposition 2.35, printed pages 330–332, with the extended central cone introduced on page 329. The proofs here use the earlier extended-positive density theorem, explicit central spectral cutoffs, and a direct proof of the corner-center isomorphism. They include the finite-ideal and composition arguments, the zero corner, arbitrary central decompositions and infinite scalar evaluations.
