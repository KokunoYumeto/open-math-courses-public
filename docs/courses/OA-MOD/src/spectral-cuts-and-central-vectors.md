# Spectral cuts and irreducible centralizers



A spectral projection can retain a vector's displacement while greatly reducing its effect on a reference state. We first quantify this for real spectra and for the unit circle. In a type III factor, a suitable projection can then be included in a matrix algebra that nearly centralizes the reference vector. Iterating these matrix algebras leaves exactly one central vector. Its support corner produces a faithful state with irreducible centralizer.

The earlier proofs used below are scalar averaging and the unitary tests for the bicentralizer, QA01–03, cone vectors and their norm inequality, SF07 and SF10–11, standard forms of corners, SE01–03 and SE06, and the joint spectral measure and functional commutator estimate, NC20–21. For the type III applications we use the complete earlier proofs of state homogeneity, HC1–7, projection comparison, PC5 and PC7–8, and normal-isomorphism and corner invariance, CT1–2.

Write a standard form as \((M,H,J,P)\), with inner products linear in the first variable. The right action is \(\zeta a=Ja^*J\zeta\), and \([a,\zeta]=a\zeta-\zeta a\). If \(\xi\in P\) is a cyclic separating unit vector, put \(\varphi=\omega_\xi\). We use the functional convention \((a\varphi)(x)=\varphi(xa)\). Thus

\[
 d_\varphi(u)=\|u\varphi-\varphi u\|
 =\|u\varphi u^*-\varphi\|,\qquad
 \|[u,\xi]\|^2\le d_\varphi(u).
 \tag{SCV.1}
\]

Indeed, \(u\xi u^*\in P\) represents \(u\varphi u^*\), so SF07 gives the inequality. Here \(B_\varphi\) denotes the bicentralizer defined and characterized in QA01–03. All assertions concerning type \(\mathrm{III}_1\) below assume separable predual. The first three sections and the matrix calculation in Section 6 do not require this assumption.

## Real spectral cuts

Let \(b=b^*\in M\) be bounded, and put \(e_t=1_{(-\infty,t]}(b)\). For every \(\zeta\in H\), the commuting selfadjoint operators \(L_b\) and \(R_b\) have the joint vector measure used in NC20. Its construction there, by the spectral measure of the normal operator \(L_b+iR_b\), works for an arbitrary vector: positivity of that vector is not needed to define the measure. Write it as \(\mu_\zeta\). Its mass is \(\|\zeta\|^2\), and bounded Borel functional calculus gives

\[
 \|[b,\zeta]\|^2=\int(s-t)^2\,d\mu_\zeta(s,t),\qquad
 \|[e_\lambda,\zeta]\|^2
 =\int|1_{s\le\lambda}-1_{t\le\lambda}|^2\,d\mu_\zeta(s,t).
 \tag{SCV.2}
\]

The spectral cut operators in the second formula are precisely left and right multiplication by \(e_\lambda\), by the one-variable marginals of that joint calculus.

Tonelli therefore gives

\[
 I_b(\zeta):=\int_{\mathbb R}\|[e_\lambda,\zeta]\|^2|\lambda|\,d\lambda
 =\int K(s,t)\,d\mu_\zeta(s,t),\qquad
 K(s,t)=\tfrac12\big|t|t|-s|s|\big|.
 \tag{SCV.3}
\]

To see the kernel, the two indicators differ exactly between \(s\) and \(t\), apart from endpoints of Lebesgue measure zero. If \(s,t\) have the same sign, \(K=|s-t|(|s|+|t|)/2\). If they have opposite signs, \(K=(s^2+t^2)/2\). The elementary inequalities \((|s|+|t|)^2\le2(s^2+t^2)\) and \(|s-t|\le|s|+|t|\) now show

\[
 \tfrac14(s-t)^2\le K(s,t)
 \le\tfrac12|s-t|(|s|+|t|).
\]

Cauchy–Schwarz, followed by \((|s|+|t|)^2\le2(s^2+t^2)\), proves

\[
 \tfrac14\|[b,\zeta]\|^2\le I_b(\zeta)
 \le\frac1{\sqrt2}\|[b,\zeta]\|
       \big(\|b\zeta\|^2+\|\zeta b\|^2\big)^{1/2}.
 \tag{SCV.4}
\]

When \(J\zeta=\zeta\), the two marginal norms coincide. The upper bound then becomes \(\|b\zeta\|\|[b,\zeta]\|\). The integrals are finite because the spectrum of \(b\) is bounded; outside its convex hull the commutator integrands vanish.

## A conditional projection-transfer estimate

For \(\lambda<0\) put \(f_\lambda=e_\lambda\), and for \(\lambda\ge0\) put \(f_\lambda=1-e_\lambda\). These choices measure the part of the spectrum beyond \(\lambda\) away from zero. The left marginal measure gives, for every vector \(\zeta\),

\[
 \int_{\mathbb R}\|f_\lambda\zeta\|^2|\lambda|\,d\lambda
 =\tfrac12\|b\zeta\|^2.
 \tag{SCV.5}
\]

For a scalar spectral value \(s\), the inner integral is \(\int_0^{|s|}t\,dt=s^2/2\); this proves the formula by Tonelli. Also \(\|[f_\lambda,\zeta]\|=\|[e_\lambda,\zeta]\|\).

Suppose \(\xi,\eta\) are \(J\)-real, \(\xi\) is separating, \(K>0\), \(\delta>0\), and a selfadjoint \(b\) satisfies, with \(D=\|[b,\eta]\|>0\),

\[
 \|b\xi\|^2+\|b\eta\|^2<KD^2,\qquad
 \|[b,\xi]\|^2<\frac{\delta^2}{64K}D^2.
 \tag{SCV.6}
\]

Then some nonzero projection \(p\in M\) satisfies

\[
 \|p\xi\|^2+\|p\eta\|^2<4K\|[p,\eta]\|^2,\qquad
 \|[p,\xi]\|^2<\delta\|[p,\eta]\|^2.
 \tag{SCV.7}
\]

In fact, (SCV.5) makes the integral of the first mass expression less than \(KD^2/2\). The real-vector upper bound in (SCV.4) gives

\[
 \frac{4K}{\delta}I_b(\xi)
 \le\frac{4K}{\delta}\|b\xi\|\|[b,\xi]\|
 <\frac K2D^2.
\]

The sum of these two integrals is thus strictly less than \(KD^2\), whereas \(4K I_b(\eta)\ge KD^2\). Hence for some \(\lambda\),

\[
 \|f_\lambda\xi\|^2+\|f_\lambda\eta\|^2
 +\frac{4K}{\delta}\|[f_\lambda,\xi]\|^2
 <4K\|[f_\lambda,\eta]\|^2.
\]

Taking \(p=f_\lambda\) gives the first strict inequality in (SCV.7). Since a nonzero projection cannot kill the separating vector, the positive mass term also makes the second strict. The displayed strict inequality itself excludes \(p=0\).

This is a conditional transfer: it does not assert the existence of \(b\) in (SCV.6). For the constant \(K=32\), it explains the projection constant \(128\). The weight in all these integrals is \(|\lambda|\), not \(|\lambda|^2\). Already \(b=2\) on a one-dimensional Hilbert space gives \(\int_0^2\lambda\,d\lambda=2=\|b1\|^2/2\), while the squared weight gives \(8/3\).

## Semicircles on the unitary spectrum

Let \(u\in M\) be unitary. For \(\theta\) modulo \(2\pi\), let \(p_\theta\) be the spectral projection of \(u\) on the half-open arc \([\theta,\theta+\pi)\). For every \(\zeta\in H\),

\[
 \|[u,\zeta]\|^2
 \le\int_0^{2\pi}\|[p_\theta,\zeta]\|^2\,d\theta
 \le\pi\|\zeta\|\|[u,\zeta]\|.
 \tag{SCV.8}
\]

Here is a direct joint-measure proof that also handles spectral atoms at the cut endpoints. Take the bounded Borel argument \(h=\operatorname{Arg}(u)\), so \(u=e^{ih}\). Apply NC20's joint construction to left and right \(h\), then push its finite vector measure forward under \((s,t)\mapsto(e^{is},e^{it})\). The resulting measure \(\nu_\zeta\) has mass \(\|\zeta\|^2\) and integrates \(|z-w|^2\) to \(\|[u,\zeta]\|^2\).

If \(d\in[0,\pi]\) is the shorter angular distance between \(z,w\), the set of semicircle starting points that contain exactly one of them has length \(2d\). For example, rotate the first point to angle zero and put the second at \(d\); the two sets of starting points are length-\(\pi\) arcs whose symmetric difference has two intervals of length \(d\). The antipodal and coincident cases follow by the same interval calculation. Endpoint choices affect finitely many starting points for each pair. Tonelli removes those null sets even when the spectral measure has atoms.

With \(c=|z-w|=2\sin(d/2)\), elementary sine bounds give

\[
 c^2\le2c\le2d\le\pi c.
\]

Indeed \(\sin x\le x\) and concavity gives \(\sin x\ge2x/\pi\) on \([0,\pi/2]\). Integrating \(2d\) gives the middle expression of (SCV.8). Its lower bound follows by integrating \(c^2\); its upper bound follows from Cauchy–Schwarz applied to \(\int c\,d\nu_\zeta\). This proves both inequalities, including \(\zeta=0\).

## A projection that moves an orthogonal vector

Assume \(B_\varphi=\mathbb C1\). For \(\eta\perp\xi\) and every \(\varepsilon>0\), there is a unitary \(u\) such that

\[
 \|[u,\xi]\|^2<\varepsilon,\qquad
 \|[u,\eta]\|^2\ge\tfrac12\|\eta\|^2.
 \tag{SCV.9}
\]

For \(\eta=0\), take \(u=1\). First consider a nonzero vector \(a\xi\) with \(\varphi(a)=0\). QA03 says that zero belongs to the ultraweakly closed convex hull of \(\{u^*au:d_\varphi(u)<\tau\}\), for every \(\tau>0\). Its image on \(\xi\) is weakly continuous on the bounded set. If every \(\|(a-u^*au)\xi\|\) were less than \(7\|a\xi\|/8\), all convex combinations and their weak limits would lie in the weakly closed ball of that radius about \(a\xi\). Zero does not lie in that ball. Thus some such \(u\) has

\[
 \|(ua-au)\xi\|\ge\tfrac78\|a\xi\|.
\]

Choose \(\tau<\varepsilon\) and \(\|a\|\sqrt\tau\le\|a\xi\|/8\). Right multiplication by \(u\) is unitary, and

\[
 [u,a\xi]=(ua-au)\xi+a[u,\xi].
\]

Consequently \(\|[u,a\xi]\|\ge3\|a\xi\|/4\). The estimate is homogeneous in \(a\xi\), with unsquared norms on both sides.

For general nonzero \(\eta\perp\xi\), cyclicity gives \(b\) with \(\|b\xi-\eta\|<\|\eta\|/200\). Set \(a=b-\varphi(b)1\). Orthogonality implies \(|\varphi(b)|<\|\eta\|/200\), so \(\|a\xi-\eta\|<\|\eta\|/100\). The preceding construction and the norm bound \(\|L_u-R_u\|\le2\) yield

\[
 \|[u,\eta]\|
 >\left(\tfrac34\tfrac{99}{100}-\tfrac2{100}\right)\|\eta\|
 =\tfrac{289}{400}\|\eta\|>\tfrac1{\sqrt2}\|\eta\|.
\]

This proves (SCV.9).

It follows that, for every \(\delta>0\), some nonzero projection \(p\) satisfies

\[
 \|[p,\xi]\|^2<\delta,\qquad
 \|[p,\eta]\|^2\ge\tfrac1{32}\|\eta\|^2.
 \tag{SCV.10}
\]

For \(\eta=0\), take \(p=1\). Otherwise normalize \(\eta\) and choose (SCV.9) with
\(\varepsilon<(\delta/(16\pi))^2\). Write \(I_\zeta=\int_0^{2\pi}\|[p_\theta,\zeta]\|^2d\theta\). By (SCV.8), \(I_\xi<\delta/16\) and \(I_\eta\ge1/2\). Thus

\[
 \int_0^{2\pi}\left(\frac1{2\pi}
       +\frac{16}{\delta}\|[p_\theta,\xi]\|^2\right)d\theta
 <2\le4I_\eta.
\]

For some \(\theta\) the integrand on the left is smaller than \(4\|[p_\theta,\eta]\|^2\). It follows that \(\|[p_\theta,\eta]\|^2>1/(8\pi)>1/32\), while \(\|[p_\theta,\xi]\|^2<\delta\|[p_\theta,\eta]\|^2/4\le\delta\). The last step uses \(\|L_p-R_p\|\le2\). Positive displacement excludes both zero and the identity. The squared tolerance for the unitary is essential because the upper semicircle estimate is linear in \(\|[u,\xi]\|\).

## Changing the faithful state

Let \(M\) be a type \(\mathrm{III}_1\) factor with separable predual. If \(B_\varphi=\mathbb C1\) for one faithful normal state, then \(B_\psi=\mathbb C1\) for every faithful normal state \(\psi\).

For clarity, put

\[
 C_\rho(a,t)=\overline{\operatorname{co}}^{\,uw}
 \{u^*au:d_\rho(u)<t\}.
\]

The bicentralizer and QA03's scalar-averaging criterion are transported by a normal star isomorphism: pullback preserves predual norms, unitary conjugation, ultraweak closure, and the state norm \(\|a\|_\rho\). In particular every unitary conjugate \(\omega\) of \(\varphi\) has trivial bicentralizer. By HC1, choose such \(\omega\) with \(\|\omega-\psi\|<t/4\). The module norm inequality gives

\[
 d_\psi(u)\le d_\omega(u)+2\|\omega-\psi\|.
\]

Hence \(C_\omega(a,t/2)\subset C_\psi(a,t)\). The first set contains a scalar by QA03. This holds for every \(a\) and \(t>0\); the converse in QA03 proves the assertion for \(\psi\).

Every nonzero corner of \(M\) is normally isomorphic to \(M\). Indeed PC8 supplies \(v^*v=1\), \(vv^*=e\); the maps \(x\mapsto vxv^*\) and \(y\mapsto v^*yv\) are inverse normal star isomorphisms. CT1–2 proves that type \(\mathrm{III}_1\) and the required modular spectra are preserved. The corner's predual is separable, either through this isomorphism or as the image of the normal compression on \(M_*\). Thus the same state-independent bicentralizer property holds in every nonzero corner.

## Central vectors of a finite matrix algebra

Let \(F\subset M\) be a unital copy of \(M_d(\mathbb C)\) with matrix units \(e_{ij}\), and let

\[
 H^F=\{\zeta:a\zeta=\zeta a\text{ for all }a\in F\},\quad
 e=e_{11},\quad A=F'\cap M.
\]

The orthogonal projection onto \(H^F\) and a useful partial isometry are

\[
 Q_F\zeta=\frac1d\sum_{i,j}e_{ij}\zeta e_{ji},\qquad
 W\zeta=\frac1{\sqrt d}\sum_i e_{i1}\zeta e_{1i}.
 \tag{SCV.11}
\]

Left and right multiplication commute. Multiplying the matrix units gives

\[
 W^*\zeta=\frac1{\sqrt d}\sum_i e_{1i}\zeta e_{i1},\qquad
 W^*W=L_eR_e,\qquad WW^*=Q_F.
 \tag{SCV.12}
\]

For example in \(W^*W\), \(e_{1i}e_{j1}=\delta_{ij}e\) on both sides, giving \(d\) equal terms divided by \(d\). In \(WW^*\), the products give \(e_{ij}\) and \(e_{ji}\). The range of \(W\) centralizes every \(e_{kl}\), as multiplication makes both resulting sums equal \(d^{-1/2}e_{k1}\zeta e_{1l}\). Conversely, a central vector satisfies
\(Q_F\zeta=d^{-1}\sum_{ij}\zeta e_{ij}e_{ji}=\zeta\).
These facts prove the asserted range and projection identities.

The maps

\[
 \Theta:eMe\longrightarrow A,\quad
 \Theta(x)=\sum_i e_{i1}xe_{1i},\qquad
 \Theta^{-1}(y)=ye
 \tag{SCV.13}
\]

are inverse normal unital star isomorphisms. Multiplication and adjoints follow from the matrix-unit relations. To check surjectivity, if \(y\) commutes with every matrix unit, then \(\Theta(ye)=\sum_i ye_{ii}=y\); the reverse composite is equally direct. On \(eHe=L_eR_eH\),
\(W(x\zeta)=\Theta(x)W\zeta\).
Moreover \(W\) and \(W^*\) commute with \(J\), because each summand is \(aJaJ\) for an appropriate \(a\), with a positive real coefficient. Each such summand preserves \(P\). Thus

\[
 W(P\cap eHe)=P\cap H^F.
 \tag{SCV.14}
\]

One inclusion follows from positivity of \(W\); for the other apply \(W^*\) to a cone vector in \(H^F\) and use \(WW^*=Q_F\). SE01–03 gives the corner standard form on \(eHe\), so (SCV.12)–(SCV.14) transport it to the standard form \((A,H^F,J|_{H^F},P\cap H^F)\). In particular \(Q_FP\subset P\).

If \(\xi\in P\) is cyclic and separating for \(M\), then \(Q_F\xi\) is cyclic and separating for \(A\) on \(H^F\). To prove faithfulness rather than assume it survives projection, write

\[
 W^*\xi=\frac1{\sqrt d}\sum_i e_{1i}\xi e_{i1}
 \ \ge_P\ \frac1{\sqrt d}e\xi e.
 \tag{SCV.15}
\]

If a projection \(z\in eMe\) kills \(W^*\xi\), compress this positive-cone sum by \(z\) on both sides. The sum is zero. A selfdual cone is pointed, and a finite sum of its vectors can be zero only when each is zero: pair the sum with each summand, whose pairings with all others are nonnegative. Hence \(z\xi z=0\). The block-zero implication in SE03 gives \(z\xi=0\), so \(z=0\). The support of \(\omega_{W^*\xi}\) is therefore \(e\); SF10–11 and SE06 give cyclicity and separation. Transport by \(W\) proves the claim. The coefficient \(d^{-1/2}\) in (SCV.15) cannot be omitted.

## From a projection to a matrix algebra

Assume that \(M\) is as in Section 5 and has trivial bicentralizers. For a positive cyclic separating unit vector \(\xi\), a vector \(\eta\perp\xi\), and \(\delta>0\), there is a unital matrix factor \(F\subset M\) such that

\[
 \|\xi-Q_F\xi\|^2<\delta,\qquad
 \|Q_F\eta\|^2\le\tfrac{31}{32}\|\eta\|^2.
 \tag{SCV.16}
\]

When \(\eta=0\), use \(F=\mathbb C1\). Otherwise Section 4 provides a proper nonzero projection \(p\) with \(\|[p,\xi]\|<\delta/6\) and the displacement in (SCV.10). Define the faithful pinched state
\(\varphi'=p\varphi p+(1-p)\varphi(1-p)\).
For \(v=2p-1\), it equals \((\varphi+v\varphi v)/2\). NC21 gives

\[
 \|\varphi-\varphi'\|\le\|[v,\xi]\|
 =2\|[p,\xi]\|<\delta/3.
 \tag{SCV.17}
\]

Choose integers \(0<k<d\) with \(|k/d-\varphi(p)|<\delta/6\), and put \(r=k/d\). Proper infiniteness and PC8 split the unit into \(d\) equivalent nonzero projections: repeated halving gives \(d\) nonzero pieces, and PC8 equates them. The associated matrix units identify \(M\) normally with \(M_d(eMe)\). For any faithful normal state \(\rho\) on \(eMe\), the matrix trace state \(\operatorname{tr}_d\otimes\rho\) is faithful and normal and centralizes the matrix factor \(D\). These assertions also follow directly from \(d^{-1}\sum_i\rho(e_{1i}xe_{i1})\): its positivity and normality are termwise, and zero on a positive \(x\) forces every diagonal compression, hence every \(x^{1/2}e_{ii}\), to vanish. The trace calculation proves centralization.

The rank-\(k\) projection \(q\in D\) has state value \(r\). PC8 equates \(q\) with \(p\) and their nonzero complements; adding the two partial isometries gives a unitary carrying \(q\) to \(p\). Transporting the state and \(D\) by it, obtain a faithful normal state \(\theta\) centralizing \(D\), with \(p\in D\) and \(\theta(p)=r\).

Both corners \(pMp\) and \((1-p)M(1-p)\) are type \(\mathrm{III}_1\) with separable predual. HC1 in each corner gives unitaries \(w_1,w_2\) whose conjugations move the normalized corner states of \(\theta\) within \(\delta/3\) of those of \(\varphi'\). The sum \(w=w_1+w_2\) is unitary and commutes with \(p\). Put \(\theta_2=w\theta w^*\) and \(F=wDw^*\). Both states are block diagonal at \(p\). Comparing their two normalized corner states and then their masses yields

\[
 \|\theta_2-\varphi'\|
 <\delta/3+2|r-\varphi(p)|<2\delta/3.
\]

Together with (SCV.17), this gives \(\|\theta_2-\varphi\|<\delta\). The unique cone vector of \(\theta_2\) centralizes \(F\): conjugation by every unitary of \(F\) fixes its functional, hence the cone vector itself. Unitaries linearly span a matrix algebra. SF07 and best approximation by an orthogonal projection give the first inequality in (SCV.16).

Since \(p\in F\), every vector in \(H^F\) centralizes \(p\). The projection onto the latter subspace is
\(T_p=L_pR_p+L_{1-p}R_{1-p}\).
The four left-right block projections are orthogonal, so

\[
 \|\eta-T_p\eta\|^2=\|[p,\eta]\|^2.
 \tag{SCV.18}
\]

Since \(Q_F\le T_p\), (SCV.10) and (SCV.18) give the second inequality in (SCV.16).

## Successive matrix extensions

Under the same hypotheses, for every \(\eta\in H\) and \(\delta,\varepsilon>0\), some matrix factor \(F\) satisfies

\[
 \|\xi-Q_F\xi\|<\delta,\qquad
 \operatorname{dist}(Q_F\eta,\mathbb C Q_F\xi)<\varepsilon.
 \tag{SCV.19}
\]

Start with the scalar factor, whose central-vector projection is the identity. Suppose a matrix factor \(F_n\) has been constructed, and write \(Q_n=Q_{F_n}\), \(\xi_n=Q_n\xi\), \(\eta_n=Q_n\eta\). Section 6 gives the standard form of \(A_n=F_n'\cap M\) on \(H^{F_n}\), and makes \(\xi_n\) a positive cyclic separating vector. By (SCV.13) and Section 5, \(A_n\) is isomorphic to a nonzero corner of \(M\), so it has the same type, countability and bicentralizer property.

Let \(r_n=\eta_n-c_n\xi_n\perp\xi_n\), choosing \(c_n\) by orthogonal projection onto the nonzero line. Apply Section 7 inside \(A_n\), with reference vector \(\xi_n/\|\xi_n\|\) and vector \(r_n\). Choose its error parameter so that the change in \(\xi_n\) has norm less than \(a_n\), where \(a_n>0\) and \(\sum_n a_n<\min(\delta,1/2)\). It supplies a matrix factor \(D_n\subset A_n\). Let \(F_{n+1}=F_n\vee D_n\). The two factors commute and their multiplication map from the finite full matrix tensor product is unital, hence injective: the kernel of a full matrix algebra is either zero or the whole algebra, as multiplication by matrix units shows. Thus \(F_{n+1}\) is again a matrix factor.

On \(H^{F_n}\) its central-vector projection is the projection for \(D_n\) in that standard form. Equivalently the global projections for \(F_n\) and \(D_n\) commute, since every term in their formulas (SCV.11) commutes, and their product is \(Q_{n+1}\). Consequently

\[
 \|\xi_{n+1}-\xi_n\|<a_n,\qquad
 \operatorname{dist}(\eta_{n+1},\mathbb C\xi_{n+1})
 \le\|Q_{n+1}r_n\|
 \le\sqrt{31/32}\,\|r_n\|.
 \tag{SCV.20}
\]

The first estimate keeps \(\|\xi_n\|>1/2\). The second reduces the line distance geometrically; if it is zero we can stop. Otherwise a finite number of steps makes it smaller than \(\varepsilon\). Summing the first estimate proves (SCV.19). The same argument allows an arbitrary prescribed initial matrix factor, by beginning in its relative-commutant standard form and projecting the target vector first.

For \(0<\delta<1\), there is therefore an increasing sequence of matrix factors \(F_n\), with \(N=(\bigcup_nF_n)''\), such that

\[
 \|\xi-Q_N\xi\|<\delta,\qquad
 H^N=\mathbb C Q_N\xi.
 \tag{SCV.21}
\]

Here is the countability and limit argument. The positive part of the separable predual has a countable norm-dense subset: every subset of a separable metric space is separable, by choosing one point from each meeting member of a countable base. SF07 shows that the associated cone vectors are dense in \(P\). The complex linear span of \(P\) is dense in the standard Hilbert space, so \(H\) is separable. Choose a sequence \((h_n)\) in \(H\) every tail of which is dense; repeating the initial segments of a fixed countable dense set supplies one.

At stage \(n\), apply the extension form of (SCV.19) to \(Q_{n-1}h_n\), with distance tolerance \(2^{-n}\), and choose a positive vector-error budget \(a_n\) whose sum is strictly less than \(\delta\). Normalizing the current reference vector only rescales that error budget. We obtain

\[
 \operatorname{dist}(Q_nh_n,\mathbb C Q_n\xi)<2^{-n},
 \qquad\|Q_n\xi-Q_{n-1}\xi\|<a_n.
\]

The decreasing projections \(Q_n\) converge strongly to the projection \(Q\) onto their range intersection: for \(m\ge n\),
\(\|Q_n h-Q_m h\|^2=\|Q_nh\|^2-\|Q_mh\|^2\),
so their values are Cauchy; their limit lies in each closed range and fixes the intersection. This intersection is \(H^N\). Indeed commuting on the union means that the vector functional equations \(a\zeta=\zeta a\) hold on its ultraweak closure: each scalar matrix coefficient of their difference is normal. Thus \(Q=Q_N\).

Applying \(Q\) to each finite-stage distance estimate shows \(\operatorname{dist}(Qh_n,\mathbb C Q\xi)<2^{-n}\). For any \(h\), tail density supplies a subsequence \(h_{n_j}\to h\) with \(n_j\to\infty\). Continuity of \(Q\) and distance to the closed line proves \(Qh\in\mathbb C Q\xi\). Finally \(Q\xi\in P\), since each finite projection preserves the closed cone, and \(\|\xi-Q\xi\|\le\sum a_n<\delta<1\), so it is nonzero. This proves (SCV.21).

## Irreducible centralizers and the converse

For a normal state \(\psi\), write
\(M_\psi=\{a\in M:a\psi=\psi a\}\).
This is a von Neumann subalgebra: the module equations give closure under products, adjoints and ultraweak limits. For its unitaries, \(u\psi u^*=\psi\) is equivalent to \(u\xi_\psi=\xi_\psi u\), by uniqueness of the positive cone vector. Since unitaries linearly span a unital \(C^*\)-algebra, \(M_\psi\) is precisely the algebra centralizing \(\xi_\psi\). We call its centralizer irreducible when \(M_\psi'\cap M=\mathbb C1\).

For a type \(\mathrm{III}_1\) factor with separable predual, the following are equivalent:

1. Every faithful normal state has trivial bicentralizer.
2. There exists a faithful normal state with irreducible centralizer.
3. Faithful normal states with irreducible centralizer are norm dense in the normal state space.

Assume 1, and use (SCV.21). Put \(\zeta=Q_N\xi\ne0\), and let \(e\) be the support of \(\omega_\zeta\). For a unitary \(u\in N\), the equality \(u\zeta u^*=\zeta\) shows that \(u\omega_\zeta u^*=\omega_\zeta\), so uniqueness of its support gives \(ueu^*=e\). Thus \(e\in N'\cap M\). SE06 makes \(\zeta\) cyclic and separating in the standard form of \(eMe\), and
\(\psi=\omega_\zeta/\|\zeta\|^2\) is a faithful normal state there. The compressed algebra \(Ne\) centralizes \(\zeta\), so \(Ne\subset(eMe)_\psi\).

If \(x\in(Ne)'\cap eMe\), then \(x\zeta\in H^N\): for \(a\in N\), use \(xe=ex=x\), \(ae=ea\), \(\zeta=e\zeta=\zeta e\), and the commutation of \(x\) with \(ae\) to obtain \(a(x\zeta)=(x\zeta)a\). By (SCV.21), \(x\zeta=c\zeta\); separation for \(eMe\) gives \(x=ce\). Hence the larger centralizer also has scalar relative commutant. Section 5's corner isomorphism transports \(\psi\) to a faithful normal state on \(M\) with irreducible centralizer. This proves 2.

If 2 holds, every unitary conjugate of that state remains faithful and has conjugate, hence irreducible, centralizer. HC1 says that its unitary orbit is norm dense in all normal states, including nonfaithful ones. Thus 2 implies 3, and 3 trivially implies 2.

It remains to obtain 1 from 2. Let \(\psi\) be as in 2 and \(\xi=\xi_\psi\). For \(a\in M\), take the ultraweakly closed convex hull

\[
 C=\overline{\operatorname{co}}^{\,uw}
       \{u^*au:u\in\mathcal U(M_\psi)\}.
\]

It is a nonempty ultraweakly compact convex subset of the ball of radius \(\|a\|\), by the dual-ball compactness used in QA02. Its image \(C\xi\) is weakly compact, because \(x\mapsto\langle x\xi,h\rangle\) is normal for every \(h\). The norm attains its minimum there: its sublevel sets are weakly closed, and compactness gives a point in the intersection of the nonempty nested sublevels above the infimum. The minimizer is unique by the parallelogram identity. Faithfulness makes \(x\mapsto x\xi\) injective, so it comes from a unique \(b\in C\).

For \(u\in\mathcal U(M_\psi)\), the transformation \(x\xi\mapsto u^*xu\xi=u^*x\xi u\) is isometric and maps \(C\xi\) onto itself. Uniqueness gives \(u^*bu=b\). Unitary spanning implies \(b\in M_\psi'\cap M=\mathbb C1\). Every orbit member has state value \(\psi(a)\), and normality preserves this under convex closure, so \(b=\psi(a)1\). These exact-centralizer unitaries belong to every small-defect set. QA03 therefore gives \(B_\psi=\mathbb C1\), and Section 5 gives 1 for all faithful normal states. All three implications are proved.

## Constants, scope and source comparison

The proof has four quantitative transitions: the real spectral kernel lies between a squared difference divided by four and a product of first powers; semicircle separation has angular measure \(2d\); orthogonal-vector displacement survives with squared constant \(1/32\); and matrix projection therefore contracts the squared orthogonal component by \(31/32\). None of these estimates assumes finite dimension. Matrix models test the formulas but do not establish the type III assertions.

Four corrections are relevant when comparing the calculations with Takesaki, *Theory of Operator Algebras III*, Chapter XVIII, Section 3. In the projection-transfer integrals following Lemma 3.12, printed pp.342–343, the weight must be \(|\lambda|\); (SCV.5) and the scalar example disprove the squared weight. In the proof of Lemma 3.17, printed p.351, the initial displacement inequality compares unsquared vector norms; scaling \(a\) rules out a square on just one side. In the semicircle step of Lemma 3.19, printed p.353, a desired bound on the integral requires a squared tolerance for the preceding squared commutator, as used in Section 4. There is also a normalization correction in the corner map in Lemma 3.20, printed p.355: the lower cone bound for \(W^*\xi\) includes \(d^{-1/2}\), as (SCV.15) records.

The precise source results proved here are Corollary 3.5; Lemma 3.12; Lemmas 3.17–3.23; and the equivalence of conditions (ii) and (iii) of Theorem 3.6. Section 2 proves a conditional estimate, rather than asserting the separate premise that supplies its selfadjoint operator. The dominant-weight condition (i) of Theorem 3.6 and the injective-factor application in Corollary 3.7 require further arguments. The standard-form, projection-comparison and state-homogeneity inputs used here are the earlier programme proofs linked at the beginning.
