# Cohomology, lifting and modular reweighting

A correction on the units changes a cocycle without changing its orbit structure. For a hyperfinite relation, these corrections can be assembled so that the errors on old arrows remain exactly fixed. This matters when the required error group is dense and not closed. Applied to the Radon–Nikodym cocycle, the construction gives an equivalent probability whose modular operator has a countable decomposition into eigenspaces.

Write an arrow as \((y,x)\), from \(x\) to \(y\). Let \(R\) be a countable standard Borel principal relation with a nonzero sigma-finite quasi-invariant measure. We work on an invariant conull Borel set where

\[
 R=\bigcup_{n\geq1}F_n,\qquad F_n\subset F_{n+1},
 \tag{CLR.1}
\]

and each \(F_n\) is a full-unit finite-class Borel relation. The passage from a measured exhaustion to this exact model, including saturation of exceptional sources, is 1. What finite approximation means and 2. Countable presentations and null saturation. No ergodicity or constant bound on the finite class sizes is assumed in Sections 1–3 and 5–7.

The earlier programme proof Compatible lifts and cohomology reduction is abbreviated **LIFT**. For the flow argument we use Cohomology reduction for measurable flows, abbreviated **FLOW**, and A suspension from separated crossings, abbreviated **SUSP**. Their precise inputs are identified at the points of use.

## 1. Lifting arrows with compatible finite choices

Let \(\mathcal H\) be a standard Borel groupoid and let \(Q(a)=(r(a),s(a))\) be its endpoint map. Its image \(\mathcal H'\) is the derived principal groupoid; that image need only be analytic. A Borel homomorphism \(p:R\to\mathcal H'\) means that its endpoint-pair map into the product of the unit space is Borel and preserves composition. We seek a measurable homomorphism \(b:R\to\mathcal H\) with \(Qb=p\).

**Measured lifting theorem.** Such a lift exists on an invariant conull Borel reduction of \(R\). Arbitrary standard Borel target fibres, finite orbits and infinite orbits are allowed.

First obtain a measurable arrow choice. Source counting on \(R\) is sigma finite: a countable disjoint graph presentation and an equivalent probability on the units give a countable cover of finite measure. Weight that cover positively to get a probability \(\alpha\) equivalent to source counting. Push it forward through \(p\). The measurable-section theorem, Theorem 7.7 and Theorem 6.2 in Polish spaces and standard Borel spaces, supplies a universally measurable section of \(Q\) on its analytic image. Consequently its composition with \(p\) is measurable for the completion of \(\alpha\).

The Borel-version argument of LIFT Lemma 1.2 replaces this arrow choice by a Borel map: embed the standard Borel target in \([0,1]\), take Borel versions of simple approximants, take their pointwise limit where it lies in the target image, and use a fixed target value elsewhere. The endpoint failure set is now Borel and source-counting null. Its source projection is null, by the countable graph presentation; the saturation of that projection is still null by quasi-invariance. Remove it. We have a Borel arrow choice \(a(y,x)\) with the correct endpoints for every remaining arrow. Set its diagonal values to the appropriate units. This is the general measured selection argument of LIFT Theorem 1.3; it makes no countable-fibre assumption on \(Q\).

Fix an injective Borel real code on the units. Let \(t_n(x)\) be the point of smallest code in the finite \(F_n\)-class and \(S_n=t_n(X)\). The finite selectors are Borel by 4. Finite sheets without a probability assumption, and \(S_{n+1}\subset S_n\). Start with

\[
 b_1(y,x)=a(y,t_1x)a(x,t_1x)^{-1}.
 \tag{CLR.2}
\]

This is a homomorphism on \(F_1\): at a composable pair the middle factors cancel. Suppose \(b_n\) has been constructed. On \(F_{n+1}|_{S_n}\), put

\[
 v_n(u,v)=a(u,t_{n+1}v)a(v,t_{n+1}v)^{-1},
\]

and extend by

\[
 b_{n+1}(y,x)=b_n(y,t_ny)\,
 v_n(t_ny,t_nx)\,b_n(t_nx,x).
 \tag{CLR.3}
\]

Every composition is defined: the selected arrows have precisely the units prescribed by \(p\). The quotient map \(v_n\) is a homomorphism by the same cancellation as (CLR.2). In a product of two expressions (CLR.3), the two old transports at the intermediate unit cancel and the two quotient arrows compose. Thus \(b_{n+1}\) is a homomorphism. On an old arrow \(t_ny=t_nx\), the quotient arrow is a unit, so \(b_{n+1}=b_n\). Taking the value at the first stage containing an arrow gives a Borel homomorphism on \(R\), and every stage has endpoints \(p\). This proves the theorem, equivalently the finite construction in LIFT Theorem 1.1.

This construction also handles periodic classes. Assigning an arbitrary lift to each step of a finite cycle would require a separate check that the cycle product is the unit. Formula (CLR.3) builds that identity into the lift.

## 2. Small corrections that preserve old errors

Let \(P\) be a Polish group with a compatible complete metric \(d\), let \(H\) be a Borel normal subgroup, and put \(K=\overline H\). It is a closed normal subgroup: conjugation carries limits of elements of \(H\) to limits in \(H\). Suppose \(p,q:R\to P\) are Borel homomorphisms and

\[
 q(y,x)p(y,x)^{-1}\in K.
 \tag{CLR.4}
\]

We write \(p^f(y,x)=f(y)p(y,x)f(x)^{-1}\).

**Finite correction.** On a finite-class full-unit relation \(F\), given a positive Borel function \(\varepsilon\), there are Borel \(f:X\to K\) and \(h:F\to H\) such that

\[
 q=hp^f,\qquad d(f(x),1)<\varepsilon(x),\qquad f(t(x))=1.
 \tag{CLR.5}
\]

Here \(t\) is the finite least-point selector. To prove it, put \(p_x=p(x,t(x))\), \(q_x=q(x,t(x))\), and \(d_x=q_xp_x^{-1}\in K\). Choose a countable subset \(\{k_j\}\subset H\) dense in \(K\), using a countable base of \(K\). At a nonroot take the first \(k_j\) such that \(d(k_j^{-1}d_x,1)<\varepsilon(x)\); at a root use \(k_x=1\). Density and continuity ensure existence and the first-index rule is Borel. Set \(f(x)=k_x^{-1}d_x\). Then

\[
 q(y,x)=k_y p^f(y,x)k_x^{-1}.
 \tag{CLR.6}
\]

Thus \(h=q(p^f)^{-1}\) is Borel and lies in \(H\), by normality. This proves (CLR.5), including variable finite class sizes; it is LIFT Lemma 4.1.

**Extension with exact preservation.** Suppose \(f_n,h_n\) satisfy \(q=h_np^{f_n}\) on \(F_n\), with \(f_n=1\) on \(S_n\). For any \(\eta>0\) they can be extended to \(F_{n+1}\) so that

\[
 d(f_{n+1}(x),f_n(x))<\eta,\qquad
 h_{n+1}|_{F_n}=h_n,\qquad f_{n+1}|_{S_{n+1}}=1.
 \tag{CLR.7}
\]

For each old root \(t\), choose a Borel radius \(\varepsilon(t)>0\) which makes

\[
 d\bigl(f_n(x)p(x,t)wp(t,x),f_n(x)\bigr)<\eta
 \quad(x\,F_n\,t)
 \tag{CLR.8}
\]

whenever \(d(w,1)<\varepsilon(t)\). Here is a measurable choice rather than an appeal to pointwise continuity alone. Test radii \(2^{-j}\), requiring the left side to be at most \(\eta/2\) for every member of the finite class and every point of a fixed countable dense subset of \(P\) in the indicated open ball. Finite selection and countably many comparisons make these Borel tests. Continuity makes some sufficiently small radius pass, and density extends its bound to the whole open ball. Take the first passing radius.

Apply (CLR.5) on \(F_{n+1}|_{S_n}\) with these radii to obtain \(w:S_n\to K\), equal to one on \(S_{n+1}\), whose quotient-arrow discrepancies lie in \(H\). Define

\[
 f_{n+1}(x)=f_n(x)p(x,t_nx)w(t_nx)p(t_nx,x).
 \tag{CLR.9}
\]

Normality makes this \(K\)-valued; (CLR.8) gives the distance bound. On an old arrow the inserted terms have the same root and cancel, giving \(p^{f_{n+1}}=p^{f_n}\) exactly. On a new arrow split the transport at its two old roots. Each old leg and the quotient leg has discrepancy in \(H\); normality keeps the discrepancy of their product in \(H\). Hence \(h_{n+1}=q(p^{f_{n+1}})^{-1}\) works everywhere and agrees exactly with \(h_n\) on old arrows. At a new root all inserted and old values are one. This proves (CLR.7), the full extension argument of LIFT Lemma 5.1. No invariant metric on \(P\) was assumed.

## 3. The limiting cohomology theorem

**Theorem.** Under (CLR.1) and (CLR.4), there are Borel maps \(f:X\to K\) and \(h:R\to H\) with

\[
 q(y,x)=h(y,x)f(y)p(y,x)f(x)^{-1}.
 \tag{CLR.10}
\]

Begin with (CLR.5) on \(F_1\), then apply (CLR.7) with successive bounds \(2^{-n}\). At every unit the corrections form a Cauchy sequence in the complete metric. Its limit \(f\) is Borel and lies in closed \(K\). On an arrow in \(F_n\), the errors \(h_m\) are exactly constant for \(m\geq n\). Define \(h\) by that constant, using the first stage containing the arrow. It is Borel and lies in \(H\), even if \(H\) is not closed. Pass to the limit only in the unit corrections in the finite-stage identity. Continuity of multiplication and inversion proves (CLR.10). This is also LIFT Theorem 6.1.

The error is generally a twisted cocycle. Put \(a=p^f\). At composable arrows \(\gamma_2,\gamma_1\), substitute \(q=ha\) in the two homomorphism laws and cancel the rightmost factor. The exact result is

\[
 h(\gamma_2\gamma_1)
 =h(\gamma_2)a(\gamma_2)h(\gamma_1)a(\gamma_2)^{-1}.
 \tag{CLR.11}
\]

If \(P\) is abelian, the conjugation disappears. Merely taking limits of \(H\)-valued errors would prove membership in \(K\) only; exact stabilization in (CLR.7) is what preserves the stronger conclusion.

The correction need not be \(H\)-valued. For the additive group \(P=\mathbb R\), \(H=\mathbb Q\), and a two-point full relation, take \(p=0\) and \(q(1,0)=\sqrt2\). If both \(f\) and \(h\) were rational-valued, (CLR.10) on this arrow would express \(\sqrt2\) as a sum of three rational numbers, a contradiction. Taking \(f(0)=0,f(1)=\sqrt2\) and \(h=0\) satisfies the required closure-valued version.

## 4. Measurable flows and their return cocycles

Let \(T\) be a strict jointly Borel nonsingular properly ergodic real flow on a nonzero standard sigma-finite space. Proper ergodicity means that no orbit is conull. Let \(\rho_1,\rho_2:\mathbb R\times X\to P\) be jointly Borel maps satisfying the cocycle laws almost everywhere for each fixed pair of times, and suppose

\[
 \rho_2(t,x)\rho_1(t,x)^{-1}\in K
 \quad\text{almost everywhere for each fixed }t.
 \tag{CLR.12}
\]

Then there are Borel \(f:X\to K\) and \(h:\mathbb R\times X\to H\) such that

\[
 \rho_2(t,x)=h(t,x)f(T_tx)\rho_1(t,x)f(x)^{-1}
 \tag{CLR.13}
\]

almost everywhere for each fixed \(t\). The exceptional set may depend on \(t\).

We first use the complete cohomologous strictification proof in FLOW, Sections **An alternative: paths and a selected constant orbit**, **Recover one equivariant map by essential values**, and **A strict cocycle in the same measurable cohomology class**, equations (F19)–(F31). Apply it to the closed Polish subgroup

\[
 L=\{(u,v)\in P^2:v u^{-1}\in K\}.
 \tag{CLR.14}
\]

It is a subgroup by normality of \(K\), and closed by continuity. Replace the original pair by \((1,1)\) wherever it is outside \(L\). At each fixed time this changes a null set. For a fixed cocycle identity only three such sets, one translated by a nonsingular map, occur; thus the pair is still a measurable \(L\)-valued cocycle.

For clarity, the strictification proof works in the Polish path group \(L^0(\mathbb R,L)\). It selects a representative of each closed right-constant orbit by a sequence of Borel first-hit balls. Translation gives an action on the selected paths. The almost-equivariant unit map is repaired by the unique essential value of its orbit path; a Borel code's zero-variance test identifies the good set and proves it is invariant, without taking an uncountable intersection of conull sets. Comparing the translated selected paths recovers a strict cocycle. Thus the cited proof supplies an invariant conull set, a Borel \(b=(b_1,b_2):X\to L\), and a strict pair \((\sigma_1,\sigma_2)\) in \(L\), with

\[
 \sigma_i(t,x)=b_i(T_tx)\rho_i(t,x)b_i(x)^{-1}
 \tag{CLR.15}
\]

almost everywhere for each fixed \(t\). Strictifying the pair together preserves both \(b_2b_1^{-1}\in K\) and \(\sigma_2\sigma_1^{-1}\in K\).

The complete suspension theorem in SUSP, equation (S32), identifies an invariant conull part with

\[
 D_r=\{(z,u):0\leq u<r(z)\},\qquad r(z)\geq\delta>0,
 \tag{CLR.16}
\]

in the measure class of \(\nu(dz)\,du\). The base transformation \(S\) is aperiodic, ergodic, Borel and nonsingular. The proof constructs separated crossings, removes first-hit and last-hit orbits, and obtains the product measure class by positive-density averaging on the integer hitting cover. It does not restrict ambient measure to the section, which has ambient measure zero. Invariance of the strictification set means it consists of whole vertical fibres; its complement being product-null implies that the excluded base points form a \(\nu\)-null set. We can therefore use the strict pair at every point of the retained section.

Let \(R_n(z)\) be the signed roof sums: zero for \(n=0\), \(\sum_{j=0}^{n-1}r(S^jz)\) for positive \(n\), and \(-\sum_{j=n}^{-1}r(S^jz)\) for negative \(n\). The unique integer with \(R_n(z)\leq u+t<R_{n+1}(z)\) gives

\[
 T_t(z,u)=(S^nz,v),\qquad v=u+t-R_n(z).
 \tag{CLR.17}
\]

Define the vertical and return transports

\[
 a_i(z,u)=\sigma_i(u,(z,0)),\qquad
 c_i(S^nz,z)=\sigma_i(R_n(z),(z,0)).
 \tag{CLR.18}
\]

Aperiodicity makes the return arrows unambiguous, and their disjoint countable graph presentation makes \(c_i\) Borel. The strict law makes \(c_i\) homomorphisms and gives

\[
 \sigma_i(t,(z,u))=a_i(S^nz,v)c_i(S^nz,z)a_i(z,u)^{-1}.
 \tag{CLR.19}
\]

The motion is down, return, up. Removing the vertical terms uses the inverse at the range, namely \(a_i(T_tx)^{-1}\sigma_i(t,x)a_i(x)\).

The full marker lemma in FLOW, **Finite relations from decreasing markers**, constructs an increasing finite exhaustion of the base orbit relation: nested separated Borel marker sets give finite intervals, their intersection meets an orbit at most once, and the saturation of that intersection is handled by growing integer intervals about its unique marker. Thus Section 3 applies and gives \(g:Z\to K\), \(\ell:R_S\to H\) with \(c_2=\ell c_1^g\). For \(x=(z,u)\) and \(T_tx=(y,v)\), set

\[
 \begin{aligned}
 k(z,u)&=a_2(z,u)g(z)a_1(z,u)^{-1},\\
 h_\sigma(t,x)&=a_2(y,v)\ell(y,z)a_2(y,v)^{-1}.
 \end{aligned}
 \tag{CLR.20}
\]

Normality puts \(h_\sigma\) in \(H\); also \(k=(a_2ga_2^{-1})(a_2a_1^{-1})\in K\). Substitute (CLR.19) in \(k(T_tx)\sigma_1(t,x)k(x)^{-1}\). The \(a_1\) factors cancel, leaving \(a_2(y,v)g(y)c_1(y,z)g(z)^{-1}a_2(z,u)^{-1}\). Left multiplication by \(h_\sigma\) changes the middle return transport into \(c_2\). We have proved the strict analogue of (CLR.13).

Return to the original cocycles by

\[
 \begin{aligned}
 f(x)&=b_2(x)^{-1}k(x)b_1(x),\\
 h(t,x)&=b_2(T_tx)^{-1}h_\sigma(t,x)b_2(T_tx).
 \end{aligned}
 \tag{CLR.21}
\]

The second map lies in \(H\) by normality. For the first, write \(f=(b_2^{-1}kb_2)(b_2^{-1}b_1)\); both factors lie in \(K\), using the paired gauge condition and normality. Substitute (CLR.15) in the strict identity and cancel the outer \(b_2\) factors. This proves (CLR.13) for each fixed time on its conull set. Extending by identity on the omitted invariant null part finishes the proof. No all-time assertion for the original representatives follows from this argument.

## 5. Reweighting the modulus into a countable group

Return to the countable hyperfinite relation. Choose an equivalent probability \(\rho\); let \(\delta_\rho\) be its positive Borel modulus, with arrow convention

\[
 d\nu_r^\rho=\delta_\rho\,d\nu_s^\rho.
 \tag{CLR.22}
\]

Its homomorphism law and Borel conull model are proved in 1. Counting arrows and fixing the derivative. Let \(D\) be any countable dense subgroup of \(\mathbb R_+^\times\), for example \(2^{\mathbb Q}\). It is Borel, normal and has closure \(\mathbb R_+^\times\). Apply Section 3 to \(p=1\), \(q=\delta_\rho\). There exist a positive finite Borel \(f\) and a \(D\)-valued cocycle \(a\) such that

\[
 \delta_\rho(y,x)=a(y,x)\frac{f(y)}{f(x)}.
 \tag{CLR.23}
\]

The ordinary cocycle law for \(a\) follows from (CLR.11), since this target is abelian.

The equivalent measure \(\eta=f^{-1}\rho\) is sigma finite: the sets \(\{f^{-1}\leq n\}\) have finite \(\eta\)-measure and exhaust the units. The measure-change formula 3. Unitary transport between equivalent measures gives \(\delta_\eta=a\). To obtain a probability without losing the countable range, partition the units into Borel sets \(E_j\) of finite \(\eta\)-measure. Choose \(d_j\in D\) positive and sufficiently small that \(d_j\eta(E_j)\leq2^{-j}\). Such elements exist by density. Put

\[
 c=\sum_{j\geq1}d_j1_{E_j},\qquad
 Z=\int c\,d\eta,\qquad
 q=\frac{c}{Zf},\qquad \lambda=q\rho.
 \tag{CLR.24}
\]

Then \(0<Z<\infty\), \(q\) is positive and finite everywhere on the retained model, and \(\lambda\) is an equivalent probability. Its modulus is

\[
 r(y,x):=\delta_\lambda(y,x)
 =\frac{q(y)}{q(x)}\delta_\rho(y,x)
 =\frac{c(y)}{c(x)}a(y,x)\in D.
 \tag{CLR.25}
\]

The normalization constant cancels in the arrow ratio. This proves the countable-range reweighting theorem, including infinite original mass and nonergodic relations. It asserts membership in the chosen group; it does not assert that every element of \(D\) occurs.

## 6. The resulting modular eigenspaces

Let \(M=L(R)\) in the standard relation model and \(E\) its faithful normal diagonal expectation. The probability \(\lambda\) gives the faithful normal state \(\varphi_\lambda=\lambda\circ E\), by 2. The weight model at infinite mass. Work in the common space \(\mathcal H_\rho=L^2(R,\nu_s^\rho)\). The canonical unitary from the \(\lambda\)-space is multiplication by \(\sqrt{q(x)}\), where \(x\) is the source. By 3. Unitary transport between equivalent measures and 5. Canonical standard forms and relative operators, the transported individual modular operator is multiplication by \(r=\delta_\lambda\), and its cyclic separating vector is

\[
 \Omega_\lambda(y,x)=1_{\{y=x\}}\sqrt{q(x)},\qquad
 \|\Omega_\lambda\|^2=1.
 \tag{CLR.26}
\]

For \(d\in D\), let \(P_d\) multiply by \(1_{\{r=d\}}\) and put \(\mathcal H_d=P_d\mathcal H_\rho\). These projections are mutually orthogonal and sum strongly to one: for each vector, the squared norms are its integrals over a countable partition. Hence

\[
 \mathcal H_\rho=\bigoplus_{d\in D}\mathcal H_d,\qquad
 \Delta_\lambda|_{\mathcal H_d}=d\,1.
 \tag{CLR.27}
\]

This proves pure point spectral decomposition. A value \(d\) is an eigenvalue precisely when \(\{r=d\}\) has positive source-counting measure; sigma finiteness then gives a nonzero square-integrable indicator on a subset. If the level set is null, its eigenspace is zero. The spectrum is the closure in \([0,\infty)\) of the actual eigenvalues. Indeed, away from that closure \((r-z)^{-1}\) is bounded and maps into the multiplication domain, giving a resolvent. A sequence of eigenvalues approaching a finite point supplies unit approximate eigenvectors there. In particular zero can be in the spectrum without being an eigenvalue.

Every complex power has its full domain

\[
 \begin{aligned}
 \operatorname{Dom}\Delta_\lambda^z
 &=\left\{\xi:\sum_{d\in D}d^{2\operatorname{Re}z}
                    \|P_d\xi\|^2<\infty\right\},\\
 \Delta_\lambda^z\xi&=\sum_{d\in D}d^zP_d\xi.
 \end{aligned}
 \tag{CLR.28}
\]

Here \(d^z=\exp(z\log d)\). Both statements follow by splitting the maximal weighted-square-integrability domain of the positive multiplication operator over its level sets. Finite sums of these eigenspace components converge in the graph norm whenever (CLR.28) holds, because the corresponding positive series tail tends to zero.

For each \(\xi\), the orbit \(\{\Delta_\lambda^{it}\xi:t\in\mathbb R\}\) is relatively compact. Given \(\varepsilon>0\), choose finitely many components whose remaining squared norms sum to less than \(\varepsilon^2\). The retained orbit is contained in the compact image of a finite product of circles acting on the fixed vectors \(P_d\xi\); the remaining orbit has norm less than \(\varepsilon\). A finite net for the compact part gives total boundedness of the full orbit. Completeness of Hilbert space makes its closure compact. Thus the state is almost periodic in this precise modular sense. This describes one constructed state; no equality with a factor invariant formed from all weights is asserted.

## 7. Relative domains and finite approximants

Keep the original measure \(\mu=h\rho\), with \(0<h<\infty\), and the new probability \(\lambda=q\rho\). They define weights \(\varphi_h,\varphi_q\) on the same algebra. In \(\mathcal H_\rho\), the complete relative formulas of 4. The mixed graph and its full domain through 6. The normalized cocycle and modular action are

\[
 \begin{aligned}
 \kappa(y,x)&=\frac{q(y)}{h(x)}\delta_\rho(y,x),\\
 \Delta_{q,h}&=m_\kappa,\\
 (A_{q,h}\xi)(y,x)&=
       \sqrt{\frac{q(x)}{h(y)}}\,\overline{\xi(x,y)},\\
 [D\varphi_q:D\varphi_h]_t&=M_{(q/h)^{it}}.
 \end{aligned}
 \tag{CLR.29}
\]

The diagonal multiplier in the last line acts by its range value. For example, transporting the relative formula from base measure \(h\rho\) to \(\rho\) multiplies vectors by \(\sqrt{h(x)}\). This gives exactly the mixed flip coefficient in (CLR.29). Changing variables by inversion shows

\[
 \|A_{q,h}\xi\|^2=\int_R\kappa(y,x)|\xi(y,x)|^2\,d\nu_s^\rho.
 \tag{CLR.30}
\]

Thus the mixed operator has the full square-root domain, not just a bounded-support core. More generally

\[
 \operatorname{Dom}\Delta_{q,h}^z
 =\left\{\xi:\int_R\kappa^{2\operatorname{Re}z}|\xi|^2
                                      \,d\nu_s^\rho<\infty\right\}.
 \tag{CLR.31}
\]

The individual multiplier in (CLR.25) and the relative multiplier in (CLR.29) are different. The latter need not be \(D\)-valued, even though the individual modular operator of \(\varphi_q\) has pure point decomposition. Likewise the scalar \(Z^{-it}\) in \(q^{it}=Z^{-it}(c/f)^{it}\) remains in the cocycle: normalization cancels in the individual arrow ratio but not in a relative weight comparison.

For the exhaustion (CLR.1), let \(P_n\) multiply by \(1_{F_n}\). The matrix-field compression construction in 5. Scalar matrices and modular matrix fields and 6. Expectations that retain every diagonal weight gives faithful normal expectations \(E_n:M\to L(F_n)\) preserving the diagonal expectation and every diagonal weight, including \(\varphi_h\) and \(\varphi_q\). For variable class sizes, partition the unit space into the Borel \(F_n\)-invariant sets of each size and apply the same matrix-field compression on each summand. Compression to the closed arrow space \(P_n\mathcal H_\rho\) gives the bounded direct sum; diagonal preservation proves the weight identity by integration. These expectations are nested and converge strongly* to the identity, as in the full arrow-exhaustion proof AFM-06.

Since \(F_n\) is symmetric, \(P_n\) commutes with the flip as well as every multiplication operator above. For \(\xi\) in (CLR.31),

\[
 \begin{aligned}
 &\|\xi-P_n\xi\|^2+
   \|\Delta_{q,h}^z(\xi-P_n\xi)\|^2\\
 &\qquad=\int_{R\setminus F_n}
           (1+\kappa^{2\operatorname{Re}z})|\xi|^2\,d\nu_s^\rho
          \longrightarrow0.
 \end{aligned}
 \tag{CLR.32}
\]

The integrand is integrable by the domain hypothesis and the sets decrease to empty. This proves graph convergence, including the mixed Tomita graph at \(z=1/2\), with no bound on \(h,q\) or the ratios. The cocycle lies in the common diagonal and is fixed by every \(E_n\). These are matrix-field stages; no modular-invariance claim for scalar matrix subalgebras is needed.

## 8. Checks and examples with solutions

**A section made entirely of exceptional points.** In a unit-roof suspension let \(Q=Z\times\{0\}\), and let an additive real-valued map equal one when \(x\in Q\) and \(t\ne0\), and zero otherwise. For each fixed \(t\) it equals the zero cocycle almost everywhere. For fixed \(s,t\) its cocycle identity holds off \(Q\cup T_{-s}Q\), a null set. At every section point, however, its value at time two is one while the sum of its two time-one values is two. This verifies why (CLR.15) must precede (CLR.18).

**Signed crossings.** For a unit roof, additive \(P=\mathbb R\), \(H=\mathbb Q\), and cocycles \(\rho_1=0,\rho_2(t,x)=t\), take \(f(z,u)=u\) and \(h(t,(z,u))=\lfloor u+t\rfloor\). Writing \(n=\lfloor u+t\rfloor\) and \(v=u+t-n\) gives \(t=n+v-u\), proving (CLR.13). For \(u=1/5,t=-7/5\), one obtains \(n=-2,v=4/5\) and \(-2+4/5-1/5=-7/5\). Truncation toward zero would select the wrong return arrow.

**Pure point with an unbounded square root.** Take the full pair relation on \(X=\{0,1,2,\ldots\}\), with probability \(\lambda_n=2^{-n-1}\). Directly from source and range counting,

\[
 \delta_\lambda(m,n)=2^{n-m}\in2^{\mathbb Z}\subset2^{\mathbb Q}.
 \tag{CLR.33}
\]

Let \(e_n\), for \(n\geq1\), be the normalized indicator of the arrow \((0,n)\) in \(L^2(R,\nu_s^\lambda)\). These form an orthonormal sequence, with modular eigenvalues \(2^n\). The vector \(\xi=\sum_{n\geq1}2^{-n/2}e_n\) belongs to the Hilbert space, since \(\sum2^{-n}<\infty\), but

\[
 \sum_{n\geq1}2^n|2^{-n/2}|^2=\sum_{n\geq1}1=\infty.
 \tag{CLR.34}
\]

It is outside \(\operatorname{Dom}\Delta_\lambda^{1/2}\). Pure point spectrum therefore does not eliminate the maximal-domain requirement. Reverse arrows supply eigenvalues \(2^{-n}\) tending to zero; zero is spectral but has no eigenvector, since the multiplier is strictly positive.

**Normalization in a relative comparison.** If \(q=ch\) for a positive constant \(c\), then the two individual moduli agree, but (CLR.29) gives \(\Delta_{q,h}=c\Delta_h\) in the common coordinates and cocycle \(c^{it}1\). Thus equality of individual modular automorphism groups does not discard the weight's scalar normalization. This also checks the role of \(Z\) in (CLR.24).

The lifting, finite-correction, limiting and flow results correspond to Masamichi Takesaki, *Theory of Operator Algebras III*, Corollary XIII.3.25, Theorem XIII.3.26, Lemmas XIII.3.27–3.28 and Corollary XIII.3.29, printed pages 47–52. The proofs above use the explicitly identified earlier programme proofs for measurable selection, strictification, suspension and relation modular operators. The exposition and calculations here are independently written.
