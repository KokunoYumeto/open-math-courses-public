# Relation weights and change of measure

A measure on the objects of a countable relation puts a weight on its operator algebra. Changing that measure leaves the algebra unchanged, but changes the GNS norm, the modular operator and the comparison between two weights. The two coordinates of an arrow have different jobs: the source coordinate determines the GNS norm, whereas the Radon–Nikodym cocycle acts at the range coordinate. Keeping those jobs separate gives formulas valid for unbounded densities and infinite weights.

Throughout, a countable group \(\Gamma\) acts nonsingularly on a standard Borel space \(X\) with a nonzero sigma-finite measure \(\mu\). The action need not be free or ergodic. Its orbit relation is \(R=\{(y,x):y\in\Gamma x\}\), with arrow \((y,x):x\to y\). All identities are understood on the common invariant conull space specified below.

The earlier programme proofs used here are Relation kernels and modular coordinates, Sections 1–4 and 6, especially Proposition 6.0 and Theorem 6.2; the balanced GNS blocks, Four GNS corners and their finite ideals through A commutant flip gives the GNS unitary; the canonical cone comparison, Canonical comparison of the positive cones and One Hilbert space for all n.s.f. GNS maps; and the relative-flow implementation, The same flow in either GNS column through Three balanced corners and ordered composition. The relation lesson proves the analytic kernel construction and the exact sigma-finite weight model. The present lesson proves the comparison of different measures, including the closed mixed graphs.

## 1. Counting arrows and fixing the derivative

Write \(\nu_s,\nu_r\) for source and range counting:

\[
 \int_R f\,d\nu_s=\int_X\sum_{y\sim x}f(y,x)\,d\mu(x),
 \qquad
 \int_R f\,d\nu_r=\int_X\sum_{x\sim y}f(y,x)\,d\mu(y).
 \tag{RWT.1}
\]

These are equivalent sigma-finite measures. Here is the counting argument. Enumerate the group and retain the part of each graph not in an earlier graph. Each retained piece is the graph of a group element restricted to a Borel domain; its source and range projections are Borel. Counting a Borel set along a fibre is therefore a countable sum of measurable indicators. Intersect each piece with the inverse image, under the source projection, of a finite-measure base set. These intersections give a countable finite-\(\nu_s\)-measure cover. Reversing coordinates proves sigma-finiteness of \(\nu_r\).

For a Borel arrow set \(C\), its source-counting measure is zero exactly when \(\mu(s(C))=0\), and similarly for the range. Each endpoint set is contained in the saturation of the other. Nonsingularity and countability make the saturation of a null set null, proving equivalence of the two measures. Conversely, if these counting measures are equivalent, apply them to \(s^{-1}(N)\) for a null base set \(N\). Its range is the saturation of \(N\), which must be null. Every presenting group element and its inverse then preserve null sets. This proves the equivalence as well as the implication needed here.

Their derivative

\[
 \delta(y,x)=\frac{d\nu_r}{d\nu_s}(y,x)>0
 \tag{RWT.2}
\]

has a finite Borel representative satisfying

\[
 \delta(z,x)=\delta(z,y)\delta(y,x),\qquad
 \delta(x,x)=1,\qquad \delta(x,y)=\delta(y,x)^{-1}.
 \tag{RWT.3}
\]

The complete derivative and cocycle proof is the relation lesson, Lemma 1.1 and its sigma-finite extension preceding Proposition 6.0. Change of variables on a graph proves the derivative identity; removing the exceptional sets of the countably many group identities and their saturations makes (RWT.3) simultaneous. In particular a partial orbit bijection \(\theta:D\to E\) satisfies

\[
 \mu(\theta A)=\int_A\delta(\theta x,x)\,d\mu(x).
 \tag{RWT.4}
\]

Thus (RWT.2) uses the measure of the image of a set, rather than the density of the inverse pushforward.

Put \(H_\mu=L^2(R,\nu_s)\). For a kernel \(a\), left multiplication means

\[
 (L(a)\xi)(y,x)=\sum_{z\sim x}a(y,z)\xi(z,x).
 \tag{RWT.5}
\]

It changes the range coordinate and keeps the source coordinate fixed. We denote the relation algebra by \(M\) and its diagonal by \(D=L^\infty(X,\mu)\), represented as

\[
 (M_f\xi)(y,x)=f(y)\xi(y,x).
\]

The notation \(N_f\xi(y,x)=f(x)\xi(y,x)\) denotes the commuting source multiplication. These two multipliers need not agree.

## 2. The weight model at infinite mass

The relation lesson, Theorem 4.1 and Section 6, identifies \(M\) with the measurable essentially bounded orbit fields \(T_x\in B(\ell^2([x]_R))\) satisfying \(T_x=T_y\) on each orbit. Its diagonal expectation is

\[
 E(T)(x)=\langle T_x e_x,e_x\rangle.
\]

In particular \(E(T^*T)(x)=\|T_xe_x\|^2\). Theorem 6.2 there proves that

\[
 \varphi_\mu(T)=\int_X E(T)(x)\,d\mu(x),\qquad T\in M_+,
 \tag{RWT.6}
\]

is faithful, normal and semifinite, with

\[
 \Lambda_\mu(T)(y,x)=\langle T_xe_x,e_y\rangle,\qquad
 \|\Lambda_\mu(T)\|^2=\varphi_\mu(T^*T).
 \tag{RWT.7}
\]

The convention on inner products is linearity in the first variable.

For specificity, the analytic kernels used in that proof are

\[
 \mathcal C_\mu=
 \{a:\delta^n a\in L^2(\nu_s),\
       \|\delta^n a\|_{\rm Sch}<\infty\text{ for every }n\in\mathbb Z\},
\]

where the Schur norm is the maximum of the uniform absolute row and column sums. The involution is \(a^\sharp(y,x)=\overline{a(x,y)}\). Proposition 6.0 proves density, the dense-product axiom and generation of \(M\), including when the diagonal identity is not a Hilbert vector. Its closed involution and polar factors are

\[
 \begin{split}
 (S_\mu\xi)(y,x)&=\overline{\xi(x,y)},&
 D(S_\mu)&=\{\xi\in H_\mu:\delta^{1/2}\xi\in H_\mu\},\\
 (J_\mu\xi)(y,x)&=\delta(y,x)^{1/2}\overline{\xi(x,y)},&
 (\Delta_\mu\xi)(y,x)&=\delta(y,x)\xi(y,x),\\
 D(\Delta_\mu)&=\{\xi\in H_\mu:\delta\xi\in H_\mu\}.&&
 \end{split} \tag{RWT.8}
\]

These are equalities on the maximal domains, not just on bounded kernels.

For \(g,h\in\mathcal C_\mu\), Corollary 6.3 of the same lesson gives

\[
 \varphi_\mu(L(g)L(h))
 =\int_X\sum_{y\sim x}g(x,y)h(y,x)\,d\mu(x).
 \tag{RWT.9}
\]

The value is the linear extension of the weight on its finite definition algebra. Absolute integrability follows from

\[
 \int_R |g(x,y)h(y,x)|\,d\nu_s(y,x)
 \leq\|g^\sharp\|_2\|h\|_2.
\]

Thus this formula covers arbitrary kernel products, not only positive ones.

The modular formula is

\[
 \sigma_t^\mu(L(a))=L(\delta^{it}a),\qquad
 \sigma_t^\mu(M_f)=M_f.
 \tag{RWT.10}
\]

It holds on every bounded Schur-kernel operator: conjugate (RWT.5) by the unitary multiplier \(\delta^{it}\) and use (RWT.3). In particular all bounded diagonal multipliers are in the centralizer. Infinite \(\mu(X)\) causes no difficulty: finite-measure diagonal projections increase to one and give the finite-square domain, as proved in Theorem 6.2. The vector \(\mathbf1_{\mathrm{diag}}\) is used only when its squared norm \(\mu(X)\) is finite.

## 3. Unitary transport between equivalent measures

Let \(q:X\to(0,\infty)\) be measurable and finite almost everywhere, and put \(\mu_q=q\mu\). This is sigma-finite: if \(X_n\uparrow X\) have finite \(\mu\)-measure, the sets \(X_n\cap\{q\leq n\}\) form a finite-\(\mu_q\)-measure exhaustion. Null sets and their saturations are unchanged.

The two counting measures acquire densities \(q(x)\) and \(q(y)\). Consequently

\[
 \delta_q(y,x)=\frac{q(y)}{q(x)}\delta(y,x).
 \tag{RWT.11}
\]

For any finite list of densities we remove the saturations of their exceptional sets once. All densities and their reciprocals are then finite at both endpoints of every remaining arrow.

Define

\[
 V_q:H_{\mu_q}\longrightarrow H_\mu,\qquad
 (V_q\xi)(y,x)=q(x)^{1/2}\xi(y,x).
 \tag{RWT.12}
\]

The norm identity follows directly from \(d\nu_s^{\mu_q}=q(x)d\nu_s\); division by \(q(x)^{1/2}\) is its everywhere defined inverse between the indicated spaces. Thus \(V_q\) is unitary, even when multiplication by \(q(x)^{1/2}\) on the single space \(H_\mu\) would be unbounded.

Equation (RWT.5) shows \(V_qL_{\mu_q}(a)V_q^*=L_\mu(a)\). These operators generate their relation algebras, so this is an onto normal isomorphism with normal inverse. We henceforth use it to identify both algebras with \(M\). Their diagonal expectations agree, by the orbit-field formula, and the second weight becomes

\[
 \varphi_q(T)=\int_Xq(x)E(T)(x)\,d\mu(x).
 \tag{RWT.13}
\]

Its GNS map in the common coordinates is

\[
 \Lambda_q^0(T)(y,x)=q(x)^{1/2}\langle T_xe_x,e_y\rangle.
 \tag{RWT.14}
\]

A superscript \(0\) temporarily indicates only this unitary transport; its canonical standard-form meaning will be proved in Section 5.

Combining (RWT.8), (RWT.11) and (RWT.12) gives

\[
 V_qJ_{\mu_q}V_q^*=J_\mu,\qquad
 V_q\Delta_{\mu_q}V_q^*=m_{\delta_q},
 \tag{RWT.15}
\]

where \(m_b\) denotes multiplication by \(b\) on its maximal domain. For example the coefficient in the first identity is
\(q(x)^{1/2}\delta_q(y,x)^{1/2}q(y)^{-1/2}=\delta(y,x)^{1/2}\).
This verifies the square-root positions before any comparison of relative operators.

## 4. The mixed graph and its full domain

Fix two such densities \(q_1,q_2\), and write \(\varphi_i=\varphi_{q_i}\). In the transported coordinates, the initial mixed Tomita map is

\[
 A_{21}^0\Lambda_1^0(T)=\Lambda_2^0(T^*),
 \qquad T\in\mathfrak n_{\varphi_1}\cap\mathfrak n_{\varphi_2}^*.
 \tag{RWT.16}
\]

Define the positive finite arrow multiplier

\[
 \kappa_{21}(y,x)=\frac{q_2(y)}{q_1(x)}\delta(y,x).
 \tag{RWT.17}
\]

Then the exact closure of (RWT.16) is

\[
 \begin{split}
 (A_{21}\xi)(y,x)
     &=\left(\frac{q_2(x)}{q_1(y)}\right)^{1/2}
                         \overline{\xi(x,y)},\\
 D(A_{21})&=\{\xi\in H_\mu:\kappa_{21}^{1/2}\xi\in H_\mu\},\\
 A_{21}&=J_\mu m_{\kappa_{21}}^{1/2}.
 \end{split} \tag{RWT.18}
\]


**Proof of both graph inclusions.** The field of \(T^*\) is the adjoint of the common orbit matrix of \(T\). Its kernel is therefore the flip-conjugate of the kernel of \(T\). Substituting (RWT.14) proves the first formula on the initial domain. Changing coordinates using \(d\nu_r=\delta\,d\nu_s\) gives

\[
 \|A_{21}\xi\|^2=\int_R\kappa_{21}(y,x)|\xi(y,x)|^2\,d\nu_s(y,x).
 \tag{RWT.19}
\]

The expression \(J_\mu m_{\kappa_{21}}^{1/2}\) gives precisely the displayed coefficient and domain. It is closed because the positive multiplication operator is closed and \(J_\mu\) is antiunitary. Thus the initial graph is contained in the asserted closed graph.

For the reverse inclusion we exhibit a core inside the initial graph. Choose \(X_m\uparrow X\) of finite \(\mu\)-measure. Let \(F_m\) be the union of the first \(m\) presenting group graphs and their inverse graphs. For \(\xi\in D(A_{21})\), cut \(\xi\) down to the set

\[
 \begin{gathered}
 (y,x)\in F_m\cap(X_m\times X_m),\qquad |\xi(y,x)|\leq m,\\
 m^{-1}\leq\delta(y,x)\leq m,\qquad
 m^{-1}\leq q_i(x),q_i(y)\leq m\quad(i=1,2).
 \end{gathered} \tag{RWT.20}
\]

Call the resulting vector \(\xi_m\). These increasing sets exhaust the relation. Dominated convergence for the integrable function
\((1+\kappa_{21})|\xi|^2\) proves convergence in the graph norm in (RWT.19).

Put \(a_m(y,x)=q_1(x)^{-1/2}\xi_m(y,x)\). This kernel is bounded and supported on finitely many graphs, so its row and column Schur bounds are finite. Both its endpoints have finite base measure and bounded \(q_i\); its modulus is bounded above and below. The same is true after any fixed integer power of either \(\delta_{q_i}\). Thus \(a_m\in\mathcal C_{\mu_{q_1}}\cap\mathcal C_{\mu_{q_2}}\), and the same statement holds for its flip-conjugate. The kernel weight theorem places \(T_m=L(a_m)\) in the mixed ideal of (RWT.16). Equation (RWT.14) gives \(\Lambda_1^0(T_m)=\xi_m\). Therefore the whole maximal graph is the closure of the initial graph. This proves (RWT.18).

In particular

\[
 A_{21}^*A_{21}=m_{\kappa_{21}},\qquad
 D(A_{21}^*A_{21})=\{\xi:\kappa_{21}\xi\in H_\mu\}.
 \tag{RWT.21}
\]

Indeed for \(K=m_{\kappa_{21}}^{1/2}\), the adjoint of \(J_\mu K\) is \(KJ_\mu\), with its transported domain. The product is \(K^2\); its domain is the maximal multiplier domain in (RWT.21). The inequality \(\kappa_{21}\leq1+\kappa_{21}^2\) checks the extra square-root integrability in the product domain. This argument does not multiply unbounded operators on an unspecified common domain.

## 5. Canonical standard forms and relative operators

The maps \(V_q\) in (RWT.12) are the canonical standard-form identifications, not merely algebra intertwiners.

To see this, apply BT-01–03 to the pair \(\varphi_1,\varphi_2\). Its mixed polar factors are antiunitaries between the two original GNS spaces. In the transported coordinates, (RWT.18) and positivity of \(m_{\kappa_{21}}^{1/2}\) show that the first polar factor is exactly \(J_\mu\). Its inverse, the second mixed polar factor, is also \(J_\mu\). The individual modular conjugations are \(J_\mu\) by (RWT.15). BT-03 constructs the comparison unitary as the product of an individual modular conjugation and the reverse mixed polar factor. In these coordinates that product is \(J_\mu J_\mu=1\). Thus the constructed unitary from \(H_{\mu_{q_2}}\) to \(H_{\mu_{q_1}}\) is exactly

\[
 I_{1\leftarrow2}=V_{q_1}^*V_{q_2}.
 \tag{RWT.22}
\]

SF-09 proves that this same comparison unitary carries the natural cone onto the natural cone. It follows that \(\Lambda_q^0\) in (RWT.14) is the canonical GNS map in the fixed standard form. We now omit its superscript.

By SF-13, the closed graph (RWT.16) is the relative Tomita graph. We have therefore proved

\[
 \Delta_{\varphi_2,\varphi_1}=m_{\kappa_{21}},
 \qquad
 \Delta_{\varphi_i}=m_{\kappa_{ii}},
 \qquad
 \kappa_{ii}(y,x)=\frac{q_i(y)}{q_i(x)}\delta(y,x).
 \tag{RWT.23}
\]

For every real \(a\), the real power has the precise domain

\[
 D(\Delta_{\varphi_2,\varphi_1}^{\,a})
     =\{\xi:\kappa_{21}^{a}\xi\in H_\mu\}.
 \tag{RWT.24}
\]

All imaginary powers are everywhere defined unitary multipliers. Their strong continuity follows by dominated convergence, since their scalar modulus is one.

The exchanged map is the inverse closed map:

\[
 A_{12}=A_{21}^{-1},\qquad
 \operatorname{ran}A_{21}=D(A_{12}).
 \tag{RWT.25}
\]

One may either apply BT-02 or verify the assertion here: the two flip coefficients multiply to one, and
\(\kappa_{12}(x,y)=\kappa_{21}(y,x)^{-1}\). If \(\eta=A_{21}\xi\), the inverse expression equals \(\xi\), so it is square integrable and \(\eta\) is in the inverse domain; the converse is identical. Neither range is asserted to be the whole Hilbert space.

## 6. The normalized cocycle and modular action

In the numerator-first convention the cocycle is

\[
 [D\varphi_2:D\varphi_1]_t
      =M_{(q_2/q_1)^{it}}.
 \tag{RWT.26}
\]

This is the actual normalized weight cocycle. To prove that assertion, BF-02 identifies its represented value with

\[
 \Delta_{\varphi_2,\varphi_1}^{it}
                 \Delta_{\varphi_1}^{-it}.
\]

Both factors are bounded unitaries. Substitution of (RWT.23) cancels the source factor and the reference modulus:

\[
 \frac{\kappa_{21}(y,x)}{\kappa_{11}(y,x)}
          =\frac{q_2(y)}{q_1(y)}.
\]

This proves (RWT.26) through the balanced-weight definition, which fixes the scalar normalization. A modular intertwining identity alone would not fix it.

Every \(M_{(q_2/q_1)^{it}}\) lies in the diagonal centralizer of \(\varphi_1\). Its ordinary unitary group law is therefore also its \(\sigma^{\varphi_1}\)-cocycle law. Strong* continuity follows from dominated convergence on \(H_\mu\), also for the adjoints. No boundedness of \(\log(q_2/q_1)\) is required. For three densities,

\[
 [D\varphi_3:D\varphi_1]_t
 =[D\varphi_3:D\varphi_2]_t[D\varphi_2:D\varphi_1]_t;
 \tag{RWT.27}
\]

here this follows by multiplying their positive scalar ratios, and agrees with BF-03's ordered general chain rule.

The individual action on any Schur kernel is

\[
 \sigma_t^{\varphi_q}(L(a))
   =L\left(\left[\frac{q(y)}{q(x)}\delta(y,x)\right]^{it}a(y,x)\right).
 \tag{RWT.28}
\]

Equivalently,

\[
 \sigma_t^{\varphi_2}(T)
   =M_{(q_2/q_1)^{it}}\sigma_t^{\varphi_1}(T)
                         M_{(q_2/q_1)^{-it}}
 \quad(T\in M).
 \tag{RWT.29}
\]

Equation (RWT.28) follows by conjugating the kernel action with the individual modular multiplier; (RWT.29) follows on the generators and then everywhere by normality. Multiplication by a phase preserves the Schur bound, so all the displayed kernel operators are bounded. The formulas retain the separate row and column factors in the individual modular operator.

## 7. Reduction to a measurable subset

Let \(B\subset X\) have positive measure, put \(e=M_{\mathbf1_B}\), and let \(R_B=R\cap(B\times B)\). In the common standard form,

\[
 eJ_\mu eJ_\mu H_\mu=L^2(R_B,\nu_s|_{R_B}).
 \tag{RWT.30}
\]

Indeed \(J_\mu M_{\mathbf1_B}J_\mu=N_{\mathbf1_B}\) by the flip formula. The product of the two projections cuts down both endpoints. The larger space \(eH_\mu\) cuts down only the range endpoint.

The faithful representation of \(eMe\) on (RWT.30) is its relation representation for \(R_B\). The orbit-field proof of Proposition 6.1 in the relation lesson establishes faithfulness: if a compressed field vanishes over \(B\), its orbit invariance and null saturation make it vanish on every orbit meeting \(B\); on other orbits the corner is already zero. Restricted partial orbit maps and diagonal functions generate the reduced algebra.

The restrictions of both weights to \(eMe\) are exactly the diagonal weights of \(q_i\mu|_B\). They are faithful normal semifinite by the same finite-measure exhaustion used in Section 2. Apply Sections 3–6 to this restricted measure and its restricted countable graph presentation. The closed relative operator is multiplication by \(\kappa_{21}|_{R_B}\), on the maximal domain in that Hilbert space, and the cocycle is

\[
 [D(\varphi_2|_{eMe}):D(\varphi_1|_{eMe})]_t
    =eM_{(q_2/q_1)^{it}}e.
 \tag{RWT.31}
\]

This proof does not require either weight to be finite on \(e\).

If \(B_n\uparrow X\), the projections cutting both endpoints increase strongly to one and commute with every multiplication operator in (RWT.23–24). For \(\xi\) in any of the displayed real-power domains, dominated convergence of
\((1+\kappa_{21}^{2a})|\xi|^2\) proves convergence of these cutdowns in that graph norm. One can choose \(B_n\) of finite \(\mu\)-measure with both densities and their reciprocals bounded there. These are actual graph approximations, not an assertion that the unbounded density is bounded globally.

## 8. An infinite example with two proper mixed domains

Take the complete relation on \(\mathbb N=\{1,2,\ldots\}\), with counting measure. It is presented by the countable group of finite permutations. Then

\[
 M=B(\ell^2(\mathbb N)),\qquad
 H_\mu=\ell^2(\mathbb N\times\mathbb N),\qquad \delta=1.
\]

The algebra acts on rows. The common Hilbert space is the Hilbert–Schmidt matrix space. Put

\[
 q_1(n)=1,\qquad q_2(n)=r_n=\exp((-1)^n n).
\]

The weights are \(\varphi_1(T)=\operatorname{Tr}(T)\) and
\(\varphi_2(T)=\sum_n r_n\langle Te_n,e_n\rangle\) for \(T\geq0\). Both are faithful normal semifinite and infinite at the identity. On matrix coordinates,

\[
 \begin{split}
 \Delta_{\varphi_2,\varphi_1}E_{ij}&=r_iE_{ij},&
 \Delta_{\varphi_1,\varphi_2}E_{ij}&=r_j^{-1}E_{ij},\\
 \Delta_{\varphi_2}E_{ij}&=(r_i/r_j)E_{ij},&
 [D\varphi_2:D\varphi_1]_tE_{ij}&=r_i^{it}E_{ij}.
 \end{split} \tag{RWT.32}
\]

The last expression is the action of the represented cocycle on a Hilbert vector. It is different from conjugation of an algebra element by that cocycle.

For a vector with \(\xi(2k,1)=e^{-k}/\sqrt{k}\) and other entries zero,

\[
 \|\xi\|^2=\sum_{k\geq1}e^{-2k}/k<\infty,\qquad
 \|A_{21}\xi\|^2=\sum_{k\geq1}1/k=\infty.
\]

Thus \(D(A_{21})\) is proper. For a vector with
\(\eta(1,2k-1)=e^{-(2k-1)/2}/\sqrt{k}\) and other entries zero,

\[
 \|\eta\|^2<\infty,\qquad
 \|A_{12}\eta\|^2=\sum_{k\geq1}1/k=\infty.
\]

The reverse domain is proper too. Nevertheless the imaginary powers in (RWT.32) and the cocycle act on every vector.

On a finite-measure probability base the diagonal vector represents its weight. This example shows why that device cannot replace the sigma-finite graph construction: here the diagonal identity has infinite Hilbert norm, while every finite matrix kernel lies in the required mixed core.

## 9. Checks and solved problems

**Problem 1: two unequal masses.** On the complete two-point relation, give the points masses \(p_1=2,p_2=5\). Take \(q_1=(3,7)\), \(q_2=(11,13)\). Compute the two individual modular multipliers, the relative multiplier and the cocycle on each arrow.

**Solution.** The four formulas, with row \(i\) and column \(j\), are

\[
 \delta(i,j)=p_i/p_j,\qquad
 \kappa_{11}(i,j)=\frac{q_1(i)p_i}{q_1(j)p_j},\qquad
 \kappa_{22}(i,j)=\frac{q_2(i)p_i}{q_2(j)p_j},
\]


\[
 \kappa_{21}(i,j)=\frac{q_2(i)p_i}{q_1(j)p_j},\qquad
 u_t(i,j)=\left(\frac{q_2(i)}{q_1(i)}\right)^{it}.
\]

For example at \((1,2)\) these are \(2/5,\ 6/35,\ 22/65,\ 22/35\) and \((11/3)^{it}\), respectively. At diagonal arrows the individual modular multipliers are one, but the relative multiplier is \(q_2(i)/q_1(i)\). This detects the mistaken substitution of an individual modular operator for a relative one.

**Problem 2: check the polar factor in normalized coordinates.** Set \(f_{ij}=p_j^{-1/2}E_{ij}\) in this finite example. Show that \(J_\mu f_{ij}=f_{ji}\) and

\[
 A_{21}f_{ij}=\kappa_{21}(i,j)^{1/2}f_{ji}.
\]

**Solution.** Flip-conjugation followed by the multiplier in (RWT.8) changes the coefficient \(p_j^{-1/2}\) to \(p_i^{-1/2}\). In (RWT.18) the additional coefficient is \((q_2(i)/q_1(j))^{1/2}\), and converting the output to \(f_{ji}\) contributes \((p_i/p_j)^{1/2}\). Their product is exactly the displayed square root. Squaring in the adjoint product gives \(\kappa_{21}\).

**Problem 3: constant rescaling.** Let \(q_2=cq_1\), \(c>0\). Which formulas change?
**Solution.** The individual modular operators agree because their row and column factors of \(c\) cancel. The relative operator is \(c\Delta_{\varphi_1}\), and the normalized cocycle is \(c^{it}1\). Its conjugation is trivial, but its scalar phase records the change of weight. This is the simplest reason that agreement of modular groups does not determine the normalized cocycle.

**Problem 4: singular densities.** Why was \(q>0\) required almost everywhere?
**Solution.** If \(q\) vanishes on a positive-measure set, the two measures are not equivalent, division in (RWT.12) is no longer an onto unitary, and the ratios in (RWT.17) may be undefined. The nonfaithful construction instead uses the support and the supported module proved in BF-04. It is not obtained by assigning a value to \(0^{it}\). Unboundedness above or lack of a positive lower bound creates no such problem when \(q\) is finite and strictly positive almost everywhere.

## Mathematical sources

Masamichi Takesaki, *Theory of Operator Algebras III*, XIII.2, Lemmas 2.2, 2.4 and 2.6, Corollary 2.5, Theorem 2.7 and Proposition 2.11, develops the relation counting measures, analytic kernel algebra and diagonal weight. The earlier relation lesson contains complete programme proofs at that sigma-finite scope. The mixed-graph construction and comparison used here are the B6 machinery of *Theory of Operator Algebras II*, VIII.3, proved in BT, BF and SF at the exact locators above. Sections 3–8 give the explicit equivalent-measure specialization with its maximal domains, canonical unitary, normalized cocycle and corner restrictions.

New exposition and calculations: OpenAI Codex, GPT-6 Astra, Ultra, October 2026. CC0-1.0.

