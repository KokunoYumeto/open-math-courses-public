# The geometry of KMS states and their central densities

A convex decomposition of an equilibrium state cannot be read off from an arbitrary commutant operator. The boundary condition imposes an additional constraint: a dominated equilibrium state has a density in the center of the equilibrium state's GNS von Neumann algebra. We establish that constraint and use it to characterize extreme equilibrium states.

Throughout, \(A\) is a nonzero unital C*-algebra and \(\alpha:\mathbb R\to\operatorname{Aut}(A)\) is pointwise norm continuous. No separability hypothesis is imposed. The free [LMU notes, *Equilibrium: KMS states*](https://www.math.lmu.de/~cuenin/MSP2017/KMS.pdf), Theorem24 and Proposition25, give the analytic-test approach; Theorem37 gives the geometric characterization. We develop those ideas with full boundary-limit and central-density proofs, using exact previously written course providers. The notes' proof sketch of Theorem37 does not supply its whole argument; the converse extremality proof below is explicit. Its physical time convention is converted below. The mathematical topic antecedents also include Takesaki II, VIII.1 Exercises3–4.

## Fix the strip and build its analytic tests

Use the modular convention of The finite products and the strip convention and The same condition on a C*-algebra and its time convention. A state \(\omega\) belongs to \(K_\alpha\) if it is \(\alpha\)-invariant and for every \(a,b\in A\) there is a bounded continuous scalar function on

\[
 \overline{\mathcal S}=\{z:0\leq\operatorname{Im}z\leq1\},
 \qquad \mathcal S=\{z:0<\operatorname{Im}z<1\},
 \tag{KG.1}
\]

holomorphic on \(\mathcal S\), with

\[
 \begin{aligned}
 F^\omega_{a,b}(t)&=\omega(\alpha_t(a)b),\\
 F^\omega_{a,b}(t+i)&=\omega(b\alpha_t(a)).
 \end{aligned}
 \tag{KG.2}
\]

All products are in \(A\): a state is finite on every positive element, so its finite left ideal and finite-star algebra are all of \(A\). Boundary uniqueness and the bounded-strip maximum principle are Two facts about closed strips. They also give

\[
 \|F^\omega_{a,b}\|_\infty\leq\|a\|\|b\|.
 \tag{KG.3}
\]

For \(r>0\), form a Bochner norm integral

\[
 g_r(w)=\sqrt{r/\pi}\,e^{-rw^2},\qquad
 a_r=\int_{\mathbb R}g_r(t)\alpha_t(a)\,dt.
 \tag{KG.4}
\]

The norm continuity of the real orbit makes this integral meaningful. Define its entire continuation by

\[
 a_r(z)=\int_{\mathbb R}g_r(t-z)\alpha_t(a)\,dt.
 \tag{KG.5}
\]

The scalar identity

\[
 |g_r(t-x-iy)|=e^{ry^2}g_r(t-x)
 \tag{KG.6}
\]

proves \(\|a_r(z)\|\leq e^{r(\operatorname{Im}z)^2}\|a\|\). On each compact set of complex parameters the kernel and its derivative have an integrable bound of the form \(C(1+|t|)e^{-rt^2/2}\). Thus differentiation under the norm integral proves that (KG.5) is norm entire. This is the Banach-space version of the explicit Gaussian argument in Gaussian continuation of bounded real orbits.

A change of real integration variable gives

\[
 \alpha_s(a_r(z))=a_r(z+s),\qquad
 a_r\longrightarrow a\ \text{in norm as }r\longrightarrow\infty.
 \tag{KG.7}
\]

For the limit, split the integral of \(\alpha_t(a)-a\) into a small interval about zero and its complement. Continuity controls the first part; the bound \(2\|a\|\) and the vanishing Gaussian tail control the second. In particular the collection of all \(a_r\) is norm dense and stable under real translations.

Notation such as \(\alpha_i(a_r)\) means \(a_r(i)\). It does not assert that the automorphism \(\alpha_i\) exists on arbitrary elements of \(A\). If \(\tau_t\) denotes physical time with the convention that the lower edge is \(\omega(b\tau_t(a))\) and the upper edge interchanges those factors at height \(\beta>0\), then the modular flow used here is \(\alpha_t=\tau_{-\beta t}\), exactly as in KM-07.

## Replace the strip by exact linear equations

**Criterion.** An \(\alpha\)-invariant state \(\omega\) lies in \(K_\alpha\) if and only if the following identity holds for every \(a,b\in A\) and \(r>0\):

\[
 \omega(a_r(i)b)=\omega(ba_r).
 \tag{KG.8}
\]

**Necessity.** For the analytic element \(a_r\), the scalar function

\[
 z\longmapsto\omega(a_r(z)b)
 \tag{KG.9}
\]

is continuous and holomorphic, bounded on the closed strip by (KG.6), and has the lower edge of \(F^\omega_{a_r,b}\). Boundary uniqueness identifies the two functions. Their upper values at \(i\) give (KG.8).

**Sufficiency.** Assume (KG.8). Since \(\alpha_t(a_r)=(\alpha_t(a))_r\), applying the same equation with \(\alpha_t(a)\) in place of \(a\) gives the upper edge in (KG.2) for the function (KG.9). Thus every Gaussian test has a strip function.

Fix arbitrary \(a,b\in A\) and use \(a_n\), \(n\in\mathbb N\), from (KG.4). For two indices \(n,m\), both boundary lines of the difference of their strip functions are bounded by \(\|a_n-a_m\|\|b\|\). The maximum principle therefore gives

\[
 \|F^\omega_{a_n,b}-F^\omega_{a_m,b}\|_\infty
 \leq\|a_n-a_m\|\|b\|.
 \tag{KG.10}
\]

The functions converge uniformly on the entire closed strip. Their limit is bounded and continuous; uniform convergence on compact subsets of the interior preserves holomorphy, for example by Morera's theorem. Norm convergence \(a_n\to a\) gives both edges of (KG.2). This proves the criterion. \(\square\)

The same argument applies to every bounded positive functional \(\nu\), with the edge bound \(\|\nu\|\|a\|\|b\|\). Zero functionals are allowed. Invariance is included explicitly in this criterion; For a finite weight, the two edges force invariance also proves that the full two-edge condition for a finite functional forces invariance. The continuation and uniform-limit arguments expand the freely readable proof of LMU Theorem24 and Proposition25, PDF2–3/printed16–17. The positive exponential in (KG.6) follows directly from the complex square; it is the estimate needed on the strip.

## The KMS set is weak-star compact and convex

**Theorem.** \(K_\alpha\) is a weak-star closed convex subset of the state space \(S(A)\), and hence is weak-star compact. It may be empty.

**Proof.** By The compact state set and its polar inequalities, \(S(A)\) is weak-star compact and convex. Within that space the preceding criterion describes \(K_\alpha\) exactly as the simultaneous solutions of

\[
 \begin{aligned}
  \omega(\alpha_t(a)-a)&=0,\\
  \omega(a_r(i)b-ba_r)&=0.
 \end{aligned}
 \tag{KG.11}
\]

The first equation holds for every \(a\in A\), \(t\in\mathbb R\), and the second for every \(a,b\in A\), \(r>0\). Each expression evaluates \(\omega\) at one fixed element of \(A\). Its zero set is weak-star closed and affine. Their intersection is therefore weak-star closed and convex. A closed subset of \(S(A)\) is compact. This argument treats arbitrary nets and requires no countable dense subset of \(A\). \(\square\)

One can also see convexity directly. If \(\omega_1,\omega_2\in K_\alpha\) and \(0\leq s\leq1\), the invariant state \(s\omega_1+(1-s)\omega_2\) has strip function \(sF^{\omega_1}_{a,b}+(1-s)F^{\omega_2}_{a,b}\). For closedness, however, (KG.11) avoids choosing a convergent subnet of separately supplied strip functions.

## Domination transfers the boundary to the GNS algebra

Fix \(\omega\in K_\alpha\), and let

\[
 \begin{aligned}
 (H,\pi,\Omega)&=(H_\omega,\pi_\omega,\Omega_\omega),\\
 M&=\pi(A)'',\\
 \varphi(x)&=\langle x\Omega,\Omega\rangle\quad(x\in M).
 \end{aligned}
 \tag{KG.12}
\]

Inner products are linear in the first variable. The original state \(\omega\) can be nonfaithful, so we first construct the faithful quotient required by The C*-to-von-Neumann modular extension theorem. Its GNS null set is

\[
 N_\omega=\{x\in A:\omega(x^*x)=0\}.
\]

It is a norm-closed left ideal: linearity of the GNS map proves closure under addition, its norm is at most \(\|x\|\), and
\(\omega((ax)^*(ax))\leq\|a\|^2\omega(x^*x)\) proves the left-ideal property.

The KMS condition also makes it a right ideal. Fix \(x\in N_\omega\) and a Gaussian entire element \(b\). Set \(c=\alpha_{-i}(b^*)\), interpreted through the Gaussian entire continuation of \(b^*\). Its entire real orbit is bounded on the closed upper strip, since its imaginary parameter ranges between \(-1\) and \(0\). The boundary-uniqueness argument of KG-02 therefore applies to this shifted Gaussian with second argument \(x^*xb\); its value at \(i\) gives

\[
 \omega(b^*x^*xb)=\omega(x^*xbc).
\]

Cauchy–Schwarz, applied to \(x\) and \(xbc\), gives

\[
 \begin{gathered}
 |\omega(x^*xbc)|^2\\
 \leq\omega(x^*x)\omega((xbc)^*(xbc))\\
 =0.
 \end{gathered}
\]

Thus \(xb\in N_\omega\). Gaussian elements are norm dense, and \(N_\omega\) is norm closed, so \(xa\in N_\omega\) for every \(a\in A\).

This right-ideal property identifies the null set with the representation kernel. If \(x\in N_\omega\), then
\(\pi(x)\pi(a)\Omega=\pi(xa)\Omega=0\) for all \(a\); cyclicity gives \(\pi(x)=0\). Conversely \(\pi(x)=0\) implies \(\omega(x^*x)=\|\pi(x)\Omega\|^2=0\). Hence \(N_\omega=\ker\pi\), a closed two-sided *-ideal. Invariance preserves it. The state and flow consequently descend to \(A/N_\omega\); the state is faithful, and the flow remains pointwise norm continuous, since the quotient norm contracts the original orbit errors. The same strip functions give the quotient KMS condition. Its GNS triple identifies isometrically with (KG.12).

Apply KL-07 to this faithful quotient, whose finite domain is the whole quotient algebra. Its faithful normal extension agrees with \(\omega\) on \(\pi(A)_+\). Since \(\pi(1)=I\), that extension has mass one. Its bounded linear extension and the vector state \(\varphi\) are normal and agree on the ultraweakly dense algebra \(\pi(A)\); they are equal. Consequently \(\varphi\) is a faithful normal state, \(\Omega\) is cyclic and separating, and

\[
 \sigma_t^\varphi(\pi(a))=\pi(\alpha_t(a)).
 \tag{KG.13}
\]

The implementing unitaries \(U_t=\Delta_\varphi^{it}\) are strongly continuous.

Let \(\nu\) be a positive functional on \(A\) with

\[
 0\leq\nu\leq c\omega,\qquad c<\infty.
 \tag{KG.14}
\]

The bounded-form proof in The commutant correspondence, applied to the cyclic GNS algebra \(\pi(A)\), gives a unique \(T\in\pi(A)'=M'\) with \(0\leq T\leq cI\) and

\[
 \nu(b^*a)=
 \langle T\pi(a)\Omega,\pi(b)\Omega\rangle.
 \tag{KG.15}
\]

Indeed, Cauchy–Schwarz and (KG.14) bound this form by \(c\|\pi(a)\Omega\|\|\pi(b)\Omega\|\), including its null representatives. Associativity gives commutation with every \(\pi(a)\); density gives uniqueness. Define

\[
 \widetilde\nu(x)=
 \langle xT^{1/2}\Omega,T^{1/2}\Omega\rangle
 \quad(x\in M).
 \tag{KG.16}
\]

This is normal, positive and agrees with \(\nu\) on \(\pi(A)\). Since \(T\) commutes with \(x^{1/2}\) for \(x\geq0\), it satisfies \(0\leq\widetilde\nu\leq c\varphi\) on all of \(M_+\). Agreement on the ultraweakly dense algebra also proves uniqueness of the normal extension. No faithfulness of \(\nu\) is needed.

**Transfer lemma.** If \(\nu\) is invariant and has the modular KMS boundary for \(\alpha\), then \(\widetilde\nu\) has that boundary for \(\sigma^\varphi\) on all of \(M\).

**Proof.** Invariance follows first: the two normal functionals \(\widetilde\nu\circ\sigma_t^\varphi\) and \(\widetilde\nu\) agree on \(\pi(A)\) by (KG.13), and therefore on \(M\).

Here is the analytic passage with its net topology explicit. For \(x\in M\), put

\[
 x_r(z)=\int_{\mathbb R}g_r(t-z)\sigma_t^\varphi(x)\,dt.
 \tag{KG.17}
\]

These vectorwise strong integrals belong to \(M\), are norm entire in \(z\), and satisfy the bound and real covariance from MA-16. Also \(x_r(0)\to x\) strongly*. The adjoint of the real Gaussian average is the average of \(x^*\).

By Contractive approximation from a nonunital algebra, choose a net \(a_\lambda\in\pi(A)\) of uniformly bounded norm with \(a_\lambda\to x\) strongly*. For each fixed \(r,z\),

\[
 (a_\lambda)_r(z)\longrightarrow x_r(z).
 \tag{KG.18}
\]

To justify (KG.18), write the real orbit error as
\(U_t(a_\lambda-x)U_t^*\xi\). On a compact real interval the vectors \(U_t^*\xi\) form a compact subset of \(H\). A uniformly bounded strongly convergent net converges uniformly on a compact set of vectors: cover that set by finitely many small norm balls and test their centers. Thus the error is uniformly small on the interval. The Gaussian tail, with its scalar absolute-value bound (KG.6), controls its complement uniformly in \(\lambda\). The identical argument for adjoints proves strong* convergence. This argument uses no dominated-convergence theorem for arbitrary nets.

For \(b\in\pi(A)\), (KG.8) and agreement of the functionals give

\[
 \widetilde\nu((a_\lambda)_r(i)b)
 =\widetilde\nu(b(a_\lambda)_r(0)).
 \tag{KG.19}
\]

The bounds in (KG.6) are uniform in \(\lambda\). Passing to the strong* limit in the vector functional (KG.16) gives this identity with \(x_r\). Next approximate any \(y\in M\) strongly* by a bounded net in \(\pi(A)\), again using HAP-05, and obtain

\[
 \widetilde\nu(x_r(i)y)=\widetilde\nu(yx_r(0))
 \quad(x,y\in M,\ r>0).
 \tag{KG.20}
\]

Multiplication by a fixed bounded operator preserves the required strong limits, and (KG.16) is a vector functional, so both limit passages are justified directly.

Real translates of \(x_r\) give both strip edges for the entire function \(z\mapsto\widetilde\nu(x_r(z)y)\). Finally \(x_n(0)\to x\) strongly* with \(\|x_n(0)\|\leq\|x\|\). The edge differences tend to zero **uniformly in real time**, although the original modular orbit need not be norm continuous. For \(d=x_n(0)-x_m(0)\), commutation of \(T\) with \(M\), Cauchy–Schwarz and \(\widetilde\nu\leq c\varphi\) give

\[
 \begin{gathered}
 |\widetilde\nu(\sigma_t^\varphi(d)y)|^2\\
   \leq\widetilde\nu(dd^*)\widetilde\nu(y^*y),\\
 |\widetilde\nu(y\sigma_t^\varphi(d))|^2\\
   \leq\widetilde\nu(yy^*)\widetilde\nu(d^*d).
 \end{gathered}
 \tag{KG.21}
\]

Invariance removed \(t\) from the two energy factors in these bounds. Strong* convergence and the domination bound make those factors tend to zero. The strip maximum principle makes the entire functions uniformly Cauchy on the closed strip. Their limit has the desired edges for \(x,y\), is bounded and continuous, and is holomorphic inside. This proves the transfer lemma. \(\square\)

The distinction in this proof matters: Gaussian tests are norm entire, while their unsmoothed von Neumann algebra limits converge strongly*. Norm convergence of the limits was not asserted.

## A dominated normal KMS functional has a central density

**Theorem.** Let \(\varphi\) be a faithful normal state on \(M\). For every normal positive functional \(\rho\) satisfying the modular KMS condition for \(\sigma^\varphi\) and \(0\leq\rho\leq c\varphi\), there is a unique

\[
 \begin{gathered}
 d\in Z(M)_+,\\
 0\leq d\leq cI,\\
 \rho(x)=\varphi(dx)\quad(x\in M).
 \end{gathered}
 \tag{KG.22}
\]

Conversely each such central \(d\) defines a normal positive KMS functional dominated by \(c\varphi\).

**The center is fixed.** We first verify that every central projection \(p\) is fixed by \(\sigma^\varphi\). On the finite-state Tomita core \(M\Omega\),

\[
 S_0(p x\Omega)=(px)^*\Omega
   =p x^*\Omega=pS_0(x\Omega).
 \tag{KG.23}
\]

Both \(p\) and \(1-p\) preserve this core. Closing the graphs shows that they reduce the closed involution \(S\), and its adjoint is reduced by the same orthogonal decomposition. Hence \(S^*S=\Delta_\varphi\) is reduced by \(p\). Spectral calculus, with the polar-domain interface in The closed involution and what its polar data say, gives commutation with every \(\Delta_\varphi^{it}\). Thus \(\sigma_t^\varphi(p)=p\). The spectral projections of a central self-adjoint element are central; step approximation proves that the flow fixes all of \(Z(M)\).

**Existence.** Put \(\theta=\varphi+\rho\). It is a faithful normal finite positive functional, and

\[
 \varphi\leq\theta\leq(1+c)\varphi.
 \tag{KG.24}
\]

Linearity of the strip functions and invariance make \(\sigma^\varphi\) a modular KMS group for \(\theta\). The faithful uniqueness theorem Uniqueness by an imaginary shift and periodicity therefore gives \(\sigma^\theta=\sigma^\varphi\).

By the faithful invariant-density theorem The faithful invariant-weight equivalence, there is a positive injective self-adjoint \(h\), affiliated with \(M_\varphi\), such that \(\theta=\varphi_h\). The supported modular formula Recover modular time on the support now reads

\[
 \begin{aligned}
 h^{it}\sigma_t^\varphi(x)h^{-it}&=\sigma_t^\theta(x),\\
 \sigma_t^\theta(x)&=\sigma_t^\varphi(x).
 \end{aligned}
 \tag{KG.25}
\]

Surjectivity of each automorphism gives \(h^{it}\in Z(M)\) for every \(t\). The group is strongly continuous. Apply the affiliation and uniqueness lemma A unitary group inside the fixed algebra has a unique density to this group inside \(Z(M)\). Its unique positive injective generator is \(h\); consequently all spectral projections of \(h\) are central.

We must still prove that this affiliated density is bounded. For a nonzero spectral projection \(e=1_{(1+c+\varepsilon,\infty)}(h)\), centralizer spectral evaluation gives
\(\theta(e)=\varphi_h(e)\geq(1+c+\varepsilon)\varphi(e)\). This contradicts the upper bound in (KG.24), since \(\varphi(e)>0\). Thus those projections vanish. For \(0<\varepsilon<1\), a nonzero \(f=1_{(0,1-\varepsilon)}(h)\) would instead give \(\theta(f)\leq(1-\varepsilon)\varphi(f)\), contradicting the lower bound. Injectivity excludes a spectral atom at zero. Taking countably many \(\varepsilon\downarrow0\) gives

\[
 I\leq h\leq(1+c)I.
 \tag{KG.26}
\]

The spectral evaluations follow directly from the increasing regularizations in the definition of \(\varphi_h\); no unbounded product is assigned a finite value without that definition.

Now \(h\) is bounded and central, so \(\theta(x)=\varphi(hx)\) for all \(x\). Set \(d=h-I\). Subtracting the two bounded linear functionals yields (KG.22).

**Uniqueness.** If two central self-adjoint densities \(d,e\) give the same functional, let \(q\) be any spectral projection on which \(d-e\geq\varepsilon I\), \(\varepsilon>0\). Equality tested at \(q\) gives
\(0=\varphi((d-e)q)\geq\varepsilon\varphi(q)\), so \(q=0\). Apply the same argument to \(e-d\). Spectral calculus gives \(d=e\).

**Converse.** Bounded multiplication shows normality of \(\varphi_d(x)=\varphi(dx)\). Centrality gives positivity via \(d^{1/2}xd^{1/2}\), and \(0\leq d\leq cI\) gives domination. The fixed-center argument gives invariance. For \(x,y\in M\), use the \(\varphi\)-strip function with arguments \(x,dy\). Its lower and upper edges are exactly

\[
 \varphi_d(\sigma_t^\varphi(x)y),\qquad
 \varphi_d(y\sigma_t^\varphi(x)),
 \tag{KG.27}
\]

because \(d\) is central. This proves the full KMS boundary. \(\square\)

Combining KG-04 and this theorem identifies the dominated KMS positive functionals on \(A\) with the bounded positive central densities of \(M=\pi_\omega(A)''\). In (KG.15) the commutant operator is then precisely the represented central operator \(d\). The bounded-form correspondence alone did not supply this centrality.

## Extreme equilibrium states are exactly primary states

A state is **primary** if its GNS von Neumann algebra is a factor, that is, if its center consists of scalar multiples of the identity. A point \(\omega\) of a convex set is extreme if every decomposition

\[
 \omega=s\omega_1+(1-s)\omega_2,\qquad
 0<s<1,\quad\omega_1,\omega_2\in K_\alpha
 \tag{KG.28}
\]

has \(\omega_1=\omega_2=\omega\).

**Theorem.** For \(\omega\in K_\alpha\),

\[
 \omega\text{ is extreme in }K_\alpha
 \quad\Longleftrightarrow\quad
 \pi_\omega(A)''\text{ is a factor}.
 \tag{KG.29}
\]

**Proof when the center is nontrivial.** Set \(M,\varphi\) as in KG-04. A nontrivial center has a projection \(p\) with \(0<p<I\): choose a nonscalar central self-adjoint element and a proper nonzero spectral cut. Faithfulness gives \(s=\varphi(p)\in(0,1)\). Define states on \(A\) by

\[
 \begin{gathered}
 \omega_1(a)=s^{-1}\varphi(p\pi(a)),\\
 \omega_2(a)\\
   =\frac{\varphi((I-p)\pi(a))}{1-s}.
 \end{gathered}
 \tag{KG.30}
\]

The converse in KG-05 proves their KMS property on \(M\), hence on \(A\) by (KG.13). They give (KG.28). They are distinct: their normal extensions take the values one and zero, respectively, at \(p\). If their restrictions to \(A\) were equal, ultraweak density and normality would make those extensions equal, a contradiction. Thus \(\omega\) is not extreme.

**Proof when \(M\) is a factor.** In any decomposition (KG.28), positivity gives

\[
 \begin{aligned}
 0\leq\omega_1&\leq s^{-1}\omega,\\
 0\leq\omega_2&\leq(1-s)^{-1}\omega.
 \end{aligned}
 \tag{KG.31}
\]

KG-04 extends both states to normal KMS states on \(M\). KG-05 writes their extensions as \(\varphi(d_j\,\cdot)\) with bounded positive \(d_j\in Z(M)\). Factoriality gives \(d_j=\lambda_j I\). Each extension has mass one, while \(\varphi(I)=1\), so \(\lambda_j=1\). Restriction to \(A\) yields \(\omega_1=\omega_2=\omega\). This proves extremality. \(\square\)

The proof does not assume that the component states are faithful on \(A\) or on \(M\). Adding the faithful reference state before applying modular uniqueness was the step that handled that issue. It also does not confuse extremality in \(K_\alpha\) with extremality in the full state space.

## Solved models separating purity, central mixing and domination

**Model 1: a mixed density can give an extreme KMS state.** Let \(A=M_2(\mathbb C)\), choose \(D=\operatorname{diag}(1/3,2/3)\), and put

\[
 \begin{aligned}
 \omega_D(a)&=\operatorname{Tr}(Da),\\
 \alpha_t(a)&=D^{it}aD^{-it}.
 \end{aligned}
 \tag{KG.32}
\]

By An injective trace-class density and its exact modular group, this is the modular group of the faithful state. Its GNS von Neumann algebra is a faithful copy of \(M_2(\mathbb C)\), hence a factor. KG-06 proves that \(\omega_D\) is extreme in \(K_\alpha\).

It is not pure as a state on \(A\): it is the nontrivial convex combination of the two diagonal vector states. Those vector states fail the KMS boundary for this fixed flow. For example, with \(a=E_{12}\), \(b=E_{21}\),

\[
 \begin{aligned}
 \alpha_i(E_{12})&=2E_{12},\\
 \omega_D(\alpha_i(a)b)&=2/3,\\
 \omega_D(ba)&=2/3.
 \end{aligned}
 \tag{KG.33}
\]

The first diagonal vector state instead gives the two sides \(2\) and \(0\); the second gives \(0\) and \(1\). Thus a decomposition in \(S(A)\) need not be a decomposition in \(K_\alpha\).

**Model 2: the center supplies the actual equilibrium mixture.** Let \(A=M_2(\mathbb C)\oplus M_2(\mathbb C)\), take two faithful states with modular flows on their respective blocks, and let \(\alpha\) act blockwise. For \(0<s<1\), the state

\[
 \begin{aligned}
 \omega(a_1,a_2)&=s\operatorname{Tr}(D_1a_1)\\
 &\quad+(1-s)\operatorname{Tr}(D_2a_2).
 \end{aligned}
 \tag{KG.34}
\]

has both blocks in its GNS algebra. The central projection \(p=(I,0)\) has mass \(s\); (KG.30) gives exactly the two block states. A central density \(d=(d_1I,d_2I)\), \(d_j\geq0\), gives a normalized dominated KMS state precisely when \(sd_1+(1-s)d_2=1\).

**Model 3: invariance and domination do not alone force centrality.** In Model1, set \(H=\operatorname{diag}(2,1/2)\) and \(\rho(a)=\operatorname{Tr}(DHa)\). Its mass is one, it is \(\alpha\)-invariant, and \(0\leq\rho\leq2\omega_D\). But its density \(H\) is nonscalar in the factor. The analytic test from (KG.33) gives

\[
 \begin{aligned}
 \rho(\alpha_i(E_{12})E_{21})&=4/3,\\
 \rho(E_{21}E_{12})&=1/3.
 \end{aligned}
 \tag{KG.35}
\]

Thus \(\rho\) fails the KMS condition. KG-05 uses the boundary condition as well as invariance.

**Model 4: compactness does not assert existence.** Let \(A=B(\ell^2(\mathbb N_0))\) and \(\alpha_t=\mathrm{id}\). A KMS state would satisfy \(\omega(ab)=\omega(ba)\) by (KG.8), so would be tracial. Choose the two isometries sending \(e_j\) to \(e_{2j}\) and \(e_{2j+1}\). Their range projections are orthogonal and sum to \(I\). A tracial state gives each range projection the same mass as its initial projection \(I\), namely one. Additivity would give \(\omega(I)=2\), contradicting normalization. Hence \(K_\alpha=\varnothing\) in this example.

**Model 5: a nonfaithful state has a faithful GNS quotient.** Take \(A=\mathbb C\oplus\mathbb C\), identity time, and \(\omega(a,b)=a\). This state satisfies KMS by commutativity but vanishes on the nonzero positive element \((0,1)\). Its GNS kernel is \(0\oplus\mathbb C\); the quotient is \(\mathbb C\) with its faithful scalar state, and its GNS von Neumann algebra is the same \(\mathbb C\). The original-state faithfulness hypothesis of the extension theorem is satisfied on this quotient. This example also shows why the quotient step in KG-04 is necessary.

KG-01–03 and KG-04–06 give complete original arguments for the two specified source exercises, relative to the exact named providers. The C*-normal/singular decomposition, strict-semifiniteness equivalences, strip-multiplier criterion, and general simplex/disjoint-temperature exercises are not treated in this lesson. No general Choquet representation theorem is used or claimed here.
