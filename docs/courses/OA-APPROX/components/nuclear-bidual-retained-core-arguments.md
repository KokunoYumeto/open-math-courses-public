# Retained core arguments for nuclear biduals

*Programme expression: CC0-1.0 to the extent of rights held. Human publications retain their own rights.*

These complete proof arguments supply the bounded-strip, pointwise-graph, entire finite-domain and modular-uniqueness inputs used in the nuclear-bidual lesson. Each section keeps its original hypotheses and conventions. Hilbert products in the graph and weight sections are linear in the first variable. The consuming lesson uses the corresponding conjugate convention where stated.

## Bounded-strip maximum

<a id="retained-as"></a>

Let \(h>0\), and let \(f\) be scalar, continuous on \(-h\leq\operatorname{Im}z\leq0\), holomorphic inside, with a finite bound \(M\) on the entire strip. If both boundary lines have modulus at most \(C\), then

<a id="equation-as1"></a>

\[
 |f(z)|\leq C\qquad(-h\leq\operatorname{Im}z\leq0).                 \tag{AS1}
\]
Indeed, multiply by \(e^{-\varepsilon z^2}\), not by a function growing in the horizontal direction. On the horizontal sides of the rectangle \([-R,R]\times[-h,0]\) the modulus is at most \(Ce^{\varepsilon h^2}\); on the vertical sides it is at most \(Me^{-\varepsilon R^2+\varepsilon h^2}\). [SF4](../../OA-FLOW/src/OA-FLOW-SF.md#oa-flow.sf.sf4) maximum modulus, followed by \(R\to\infty\), gives
\[
 |f(z)e^{-\varepsilon z^2}|\leq Ce^{\varepsilon h^2}.
\]
Now let \(\varepsilon\downarrow0\). Translation gives the same statement on every horizontal strip. This argument needs the finite bound on the whole strip; a bound on the two edges alone is not the premise.



## Pointwise closed graphs and the full adjoint

<a id="retained-gdw"></a>

The pointwise graph argument below is applied to the real-line regular Hilbert space with its complete scalar Radon integration and compact-cutoff proofs. No countability condition on the Hilbert space or field is imposed.

For completeness, the closed-graph step used below can be checked directly. If graph pairs converge in the two L2 norms, choose a subsequence whose errors to the two limits are at most \(2^{-2n}\). Chebyshev bounds the measure where a point error exceeds \(2^{-n}\) by a summable geometric series. Outside the null limsup set both coordinates converge pointwise. Remove also the countable union of the pointwise graph exceptional sets; each closed point graph contains the limiting pair. This proves that the maximal L2 graph is closed, and gives the full summable-error step mentioned below.


<a id="gdw-4"></a>

## GDW4. Compact graph approximation without a countable field hypothesis

We prove the local field fact needed for the *entire* graph. Let \(T_t:H\supset D(T_t)\to H\) be closed anti-linear operators. Suppose a family of continuous sections of their graphs spans a graph-dense subspace at every point. Treat a graph as a complex closed subspace of \(H\oplus\overline H\). Define \(\mathfrak T\) on \(L^2(G,H)\) by the maximal condition: \(h(t)\in D(T_t)\) almost everywhere, and \(T_th(t)\) has a strongly measurable \(L^2\) representative. Its graph is closed. Indeed, take summable-error subsequences from any pair of \(L^2\) convergences, and use each closed point graph as in GDW3.

The compact continuous graph sections are a graph core. Here are the regularity details that prevent an uncountable exceptional-set shortcut. A strongly measurable \(L^2\) field \(v\) in any Hilbert space has, for every positive error, a compact subset \(K\) of a finite-measure carrier on which it is bounded and continuous, and the squared-norm integral outside \(K\) is arbitrarily small. To prove this, first truncate its norm and choose a compact carrier with small squared-norm tail, using HR's finite-exponent Radon convention. On that finite-measure set, measurable simple approximants converge uniformly outside a set of arbitrarily small measure: choose the approximants with errors exceeding \(2^{-n}\) on sets of measure at most \(\varepsilon2^{-n}\), and discard their union. Replace each of their finitely many level sets by disjoint compact subsets with total discarded measure at most \(\varepsilon2^{-n}\). On the intersection of these compact unions, each simple approximant is continuous in the relative topology; uniform convergence makes \(v\) continuous there. Boundedness turns the discarded measure into a squared-norm estimate. This proves the stated Lusin assertion from scalar regularity, without metrizability of \(G\).

Apply it to \(v(t)=(h(t),\overline{T_th(t)})\). At each point of \(K\), a finite linear combination of the given graph sections approximates \(v(t)\). Continuity on \(K\) and of that combination gives an open relative neighbourhood with the same error bound. Finitely many suffice by compactness. Fix a precompact open neighbourhood \(O_0\) of \(K\), small enough that the finitely many chosen sections remain bounded there. Outer regularity gives an open \(O\), \(K\subset O\subset O_0\), with \(\mu(O\setminus K)\) arbitrarily small. H0's compact finite partition supplies scalar continuous cutoffs supported in \(O\) and in the selected neighbourhoods, whose sum is one on \(K\) and is at most one everywhere. Their combination of the sections approximates \(v\) uniformly on \(K\). Its bound on \(O\setminus K\), the arbitrarily small measure of that set, and the original squared-norm tail give graph-norm approximation. No countable fundamental sequence of the whole Hilbert space or all point graphs is assumed.

The adjoint is also the maximal pointwise adjoint. To see the difficult direction, a vector field \(w\) orthogonal to the global graph pairs is orthogonal almost everywhere to each compact scalar multiple of each continuous graph section, by scalar test-function uniqueness from HR/L24. Take countably many Lusin compact subsets on which \(w\) is continuous, covering its finite-exponent carrier up to a null set. On one such \(K\), each pairing with a continuous graph section is continuous. Since it vanishes \(\mu|_K\)-almost everywhere, it vanishes at every point of the measure support of \(\mu|_K\): a nonzero value there would persist on a relative open set of positive measure. The complement of this support is null, by Radon regularity and finite covers of compact subsets of that open complement. Thus at every point of one *common* conull subset of \(K\), all section pairings vanish, even if the family is uncountable. Their pointwise graph density proves orthogonality to the entire point graph. The ordinary graph-orthogonal-complement formula now identifies \(\mathfrak T^*\) with the maximal pointwise \(T_t^*\), including its \(L^2\) domain. The converse follows by integration and Cauchy–Schwarz. This proves the field fact locally.



## Entire modular elements on the whole finite ideal

<a id="retained-ma"></a>

# Entire modular elements and a finite-domain strip criterion

*CC0-1.0 to the extent of rights held.*

Let \(\varphi\) be a faithful normal semifinite weight on an arbitrary von Neumann algebra \(M\). All Hilbert inner products are linear in the first variable. Write \(N=\mathfrak n_\varphi\), \(m=\mathfrak m_\varphi\), \(A=N\cap N^*\), and \((H,\pi,\Lambda)\) for its faithful normal GNS representation. Put \(S=J\Delta^{1/2}\), \(F=S^*=J\Delta^{-1/2}\), and \(U_t=\Delta^{it}\).


<a id="oa-flow.ma.1"></a>

<a id="ma-1"></a>

## MA1. The actual common core

Let \(\mathcal T\subset A\) be [KT-4](../../OA-FLOW/src/OA-FLOW-KT.md#oa-flow.kt.4)'s algebra generated by Gaussian regularizations, and put \(\mathcal H_0=\Lambda(\mathcal T)\). [KT17](../../OA-FLOW/src/OA-FLOW-KT.md#oa-flow.kt.4) gives

<a id="equation-ma1"></a>

\[
 \Delta^r\Lambda(x)=\Lambda(\sigma_{-ir}^\varphi(x))
 \quad(x\in\mathcal T,\ r\in\mathbb R),                            \tag{MA1}
\]
with full spectral domains, and says that \(\mathcal H_0\) is a graph core for every \(\Delta^r\). Its vectors have norm-entire \(U_t\)-orbits. It is preserved by \(S\), because \(\mathcal T\) is a \*-algebra. [CI](../../OA-FLOW/src/OA-FLOW-CI.md#oa-flow.ci.3)'s reciprocal-power identities give \(J=\Delta^{1/2}S\) on \(D(S)\); hence

<a id="equation-ma2"></a>

\[
 J\Lambda(x)=\Delta^{1/2}\Lambda(x^*)
            =\Lambda(\sigma_{-i/2}^\varphi(x^*))\in\mathcal H_0.    \tag{MA2}
\]
Thus \(J\), \(F=J\Delta^{-1/2}\), and every complex power in ([MA1](#equation-ma1)) preserve \(\mathcal H_0\). In particular \(FS=\Delta\), \(SF=\Delta^{-1}\), \(S^2=F^2=1\), when applied to these vectors. These assertions concern genuine operator domains, rather than formal products of unbounded operators.

<a id="oa-flow.ma.2"></a>

<a id="ma-2"></a>

## MA2. Entire elements act on the full finite ideal on the right

Suppose \(a\in M\) has a norm-entire modular orbit \(a(z)\), with \(a(t)=\sigma_t^\varphi(a)\). Scalar identity and the real group law give \(a(z+t)=\sigma_t^\varphi(a(z))\). Write \(\sigma_z^\varphi(a)=a(z)\). Each horizontal band has a finite bound on \(\|a(z)\|\), since real translations are isometries and the imaginary parameter ranges over a compact interval.

For every real \(r\) and \(\xi\in\mathcal H_0\),

<a id="equation-ma3"></a>

\[
 \pi(a)\xi\in D(\Delta^r),\qquad
 \Delta^r\pi(a)\xi
   =\pi(\sigma_{-ir}^\varphi(a))\Delta^r\xi.                       \tag{MA3}
\]
Here is the domain proof. Put \(L=\log\Delta\) and \(p_k=1_{[-k,k]}(L)\). The real covariance from [MW](../../OA-FLOW/src/OA-FLOW-MW.md#oa-flow.mw.3) says
\[
 p_k\Delta^{it}\pi(a)\xi
   =p_k\pi(a(t))\Delta^{it}\xi.
\]
Both sides are entire in \(t\) replaced by \(z\): on the left \(p_k\Delta^{iz}\) is a bounded entire multiplier, and on the right \(\Delta^{iz}\xi\) is the entire core orbit. Scalar identity extends the equality to \(z=-ir\). Thus
\[
 p_k\Delta^r\pi(a)\xi
   =p_k\pi(a(-ir))\Delta^r\xi.
\]
The notation on the left is the bounded compact-spectral multiplier. The right sides converge in norm. The spectral domain criterion therefore puts \(\pi(a)\xi\) in \(D(\Delta^r)\) and proves ([MA3](#equation-ma3)). For an arbitrary \(\xi\in D(\Delta^{1/2})\), approximate in graph norm by \(\mathcal H_0\); boundedness of \(\pi(a)\) and \(\pi(a(-i/2))\), followed by closedness of \(\Delta^{1/2}\), proves ([MA3](#equation-ma3)) also on that whole domain when \(r=1/2\).

Put \(c=\sigma_{-i/2}^\varphi(a)\). If \(x\in A\), then \(\Lambda(x^*)\in D(\Delta^{1/2})\), so \(\pi(a)\Lambda(x^*)\) is in that domain. It is also left bounded, with multiplier \(\pi(ax^*)\), because \(ax^*\in N\). [WR-4](../../OA-FLOW/src/OA-FLOW-WR.md#oa-flow.wr.4)'s exact identity
\[
 B_l\cap D(S)=\Lambda(A)
\]
now shows \(ax^*\in A\), and identifies its \(S\)-image. Applying ([MA3](#equation-ma3)) and \(S=J\Delta^{1/2}\) yields

<a id="equation-ma4"></a>

\[
 \Lambda(xa^*)=J\pi(c)J\Lambda(x)\qquad(x\in A).                  \tag{MA4}
\]

If \(h\in M_+\) and \(\varphi(h)<\infty\), then \(h^{1/2}\in A\), so ([MA4](#equation-ma4)) gives

<a id="equation-ma5"></a>

\[
 \varphi(aha^*)\leq \|c\|^2\varphi(h).                            \tag{MA5}
\]
For every \(h\geq0\), including infinite values, the same inequality holds with any fixed \(k\geq\max(1,\|c\|)\) replacing \(\|c\|\). In particular \(Na^*\subset N\), and right multiplication by \(a^*\) induces a bounded operator on the GNS space. Formula ([MA4](#equation-ma4)) holds on all of \(N\): if \(u_i\) are [GW](../../OA-FLOW/src/OA-FLOW-GW.md#oa-flow.gw.4)'s finite positive contractions increasing to \(1\), then \(u_ix\in m\subset A\), \(\Lambda(u_ix)\to\Lambda(x)\), and
\[
 \Lambda((u_ix)a^*)=\Lambda(u_i(xa^*))\longrightarrow\Lambda(xa^*).
\]
Taking limits in ([MA4](#equation-ma4)) proves this assertion without presupposing continuity of the unbounded GNS map in an operator topology.

Let \(b=\sigma_{-i}^\varphi(a)\). Identity on the real line, followed by holomorphic continuation, gives
\[
 \sigma_{-i/2}^\varphi(b^*)=c^*.
\]
Applying the preceding result to \(b^*\) shows that right multiplication by \(b\) on \(N\) has GNS operator \(J\pi(c^*)J=(J\pi(c)J)^*\). Therefore, for \(x,y\in N\),

<a id="equation-ma6"></a>

\[
 \begin{split}
 \varphi_0(ay^*x)
 &=\langle\Lambda(x),\Lambda(ya^*)\rangle\\
 &=\langle(J\pi(c)J)^*\Lambda(x),\Lambda(y)\rangle
 =\varphi_0(y^*xb).                                             \tag{MA6}
 \end{split}
\]
All products in this calculation belong to \(m\): \(ay^*x=(ya^*)^*x\) and \(y^*xb=y^*(xb)\), with all four factors in \(N\). Since \(m=\operatorname{span}N^*N\), we have proved

<a id="equation-ma7"></a>

\[
 Na^*\subset N,\quad Nb\subset N,\quad
 \varphi_0(az)=\varphi_0(zb)\quad(z\in m).                         \tag{MA7}
\]



## Finite-domain modular uniqueness

<a id="retained-ku"></a>

# Uniqueness of the modular group from the finite-star KMS condition

*CC0-1.0 to the extent of rights held.*

Let \(\varphi\) be a faithful normal semifinite weight on an arbitrary von Neumann algebra \(M\). Suppose \((\alpha_t)_{t\in\mathbb R}\) is a group of normal \*-automorphisms, pointwise ultraweakly continuous, preserving \(\varphi\) on \(M_+\). Assume the following KMS condition on the entire algebra \(A=\mathfrak n_\varphi\cap\mathfrak n_\varphi^*\): for every \(a,b\in A\) there is a bounded continuous function on \(0\leq\operatorname{Im}z\leq1\), holomorphic inside, with boundary values
\[
K^\alpha_{a,b}(t)=\varphi_0(\alpha_t(a)b),\qquad
K^\alpha_{a,b}(t+i)=\varphi_0(b\alpha_t(a)).
\tag{KU1}
\]
We prove \(\alpha_t=\sigma_t^\varphi\) for every real \(t\). For a faithful normal state, invariance follows from (KU1), as proved in [KU-4](#ku-4); it need not be separately assumed in that case.

Actual inputs are [GW-1–5](../../OA-FLOW/src/OA-FLOW-GW.md#oa-flow.gw.1), [WR-1–4](../../OA-FLOW/src/OA-FLOW-WR.md#wr-3), [MW-4](../../OA-FLOW/src/OA-FLOW-MW.md#mw-4), [EW-2–3](../../OA-FLOW/src/OA-FLOW-EW.md#ew-2) with [the required normality hypothesis](../../OA-FLOW/src/OA-FLOW-EW.md#ew-2), [CP01–06](../../OA-FLOW/src/OA-FLOW-CP.md#oa-flow.cp.1), [SF-3–4](../../OA-FLOW/src/OA-FLOW-SF.md#oa-flow.sf.sf0), [FF-1](../../OA-FLOW/src/OA-FLOW-FF.md#oa-flow.ff.2), and the complete local [KT-1–4](../../OA-FLOW/src/OA-FLOW-KT.md#kt-1). The free author context is [Hiai, §2.2, printed pp.17–19, and §7.1(C), p.64](https://arxiv.org/pdf/2004.02383v1). The periodic scalar-pairing idea is used here with all arbitrary-weight GNS, integral and finite-domain steps proved; no Stone theorem, three-lines theorem, Schwarz reflection theorem or unproved uniqueness theorem is imported.

Actual earlier proof ranges: [OA-FLOW.GW.1](../../OA-FLOW/src/OA-FLOW-GW.md#oa-flow.gw.1), [OA-FLOW.GW.2](../../OA-FLOW/src/OA-FLOW-GW.md#oa-flow.gw.2), [OA-FLOW.GW.3](../../OA-FLOW/src/OA-FLOW-GW.md#oa-flow.gw.3), [OA-FLOW.GW.4](../../OA-FLOW/src/OA-FLOW-GW.md#oa-flow.gw.4), [OA-FLOW.GW.5](../../OA-FLOW/src/OA-FLOW-GW.md#oa-flow.gw.5), [OA-FLOW.WR.1](../../OA-FLOW/src/OA-FLOW-WR.md#oa-flow.wr.1), [OA-FLOW.WR.2](../../OA-FLOW/src/OA-FLOW-WR.md#oa-flow.wr.2), [OA-FLOW.WR.3](../../OA-FLOW/src/OA-FLOW-WR.md#oa-flow.wr.3), [OA-FLOW.WR.4](../../OA-FLOW/src/OA-FLOW-WR.md#oa-flow.wr.4), [OA-FLOW.WR.5](../../OA-FLOW/src/OA-FLOW-WR.md#oa-flow.wr.5), [OA-FLOW.MW.4](../../OA-FLOW/src/OA-FLOW-MW.md#oa-flow.mw.4), [OA-FLOW.NF.5](../../OA-FLOW/src/OA-FLOW-NF.md#oa-flow.nf.5), [OA-FLOW.EW.2](../../OA-FLOW/src/OA-FLOW-EW.md#oa-flow.ew.2), [OA-FLOW.EW.3](../../OA-FLOW/src/OA-FLOW-EW.md#oa-flow.ew.3), [OA-FLOW.EW.5](../../OA-FLOW/src/OA-FLOW-EW.md#oa-flow.ew.5), [OA-FLOW.CP.1](../../OA-FLOW/src/OA-FLOW-CP.md#oa-flow.cp.1), [OA-FLOW.CP.2](../../OA-FLOW/src/OA-FLOW-CP.md#oa-flow.cp.2), [OA-FLOW.CP.3](../../OA-FLOW/src/OA-FLOW-CP.md#oa-flow.cp.3), [OA-FLOW.CP.4](../../OA-FLOW/src/OA-FLOW-CP.md#oa-flow.cp.4), [OA-FLOW.CP.5](../../OA-FLOW/src/OA-FLOW-CP.md#oa-flow.cp.5), [OA-FLOW.CP.6](../../OA-FLOW/src/OA-FLOW-CP.md#oa-flow.cp.6), [OA-FLOW.SF.SF0](../../OA-FLOW/src/OA-FLOW-SF.md#oa-flow.sf.sf0), [OA-FLOW.SF.SB0](../../OA-FLOW/src/OA-FLOW-SF.md#oa-flow.sf.sb0), [OA-FLOW.SF.SB1](../../OA-FLOW/src/OA-FLOW-SF.md#oa-flow.sf.sb1), [OA-FLOW.SF.SB2](../../OA-FLOW/src/OA-FLOW-SF.md#oa-flow.sf.sb2), [OA-FLOW.SF.SB3](../../OA-FLOW/src/OA-FLOW-SF.md#oa-flow.sf.sb3), [OA-FLOW.SF.SB4](../../OA-FLOW/src/OA-FLOW-SF.md#oa-flow.sf.sb4), [OA-FLOW.SF.SB5](../../OA-FLOW/src/OA-FLOW-SF.md#oa-flow.sf.sb5), [OA-FLOW.SF.SB6](../../OA-FLOW/src/OA-FLOW-SF.md#oa-flow.sf.sb6), [OA-FLOW.SF.SF3](../../OA-FLOW/src/OA-FLOW-SF.md#oa-flow.sf.sf3), [OA-FLOW.SF.SF4](../../OA-FLOW/src/OA-FLOW-SF.md#oa-flow.sf.sf4), [OA-FLOW.FF.1](../../OA-FLOW/src/OA-FLOW-FF.md#oa-flow.ff.1), [OA-FLOW.FF.2](../../OA-FLOW/src/OA-FLOW-FF.md#oa-flow.ff.2), [OA-FLOW.CF.1](../../OA-FLOW/src/OA-FLOW-CF.md#oa-flow.cf.1), [OA-FLOW.CF.6](../../OA-FLOW/src/OA-FLOW-CF.md#oa-flow.cf.6), [OA-FLOW.CF.7](../../OA-FLOW/src/OA-FLOW-CF.md#oa-flow.cf.7), [OA-FLOW.CF.8](../../OA-FLOW/src/OA-FLOW-CF.md#oa-flow.cf.8), [OA-FLOW.SC.4](../../OA-FLOW/src/OA-FLOW-SC.md#sc-04), [OA-FLOW.SC.5](../../OA-FLOW/src/OA-FLOW-SC.md#sc-05), [OA-FLOW.SC.8](../../OA-FLOW/src/OA-FLOW-SC.md#sc-08), [OA-FLOW.SC.9](../../OA-FLOW/src/OA-FLOW-SC.md#sc-09), [OA-FLOW.KT.1](../../OA-FLOW/src/OA-FLOW-KT.md#kt-1), [OA-FLOW.KT.2](../../OA-FLOW/src/OA-FLOW-KT.md#kt-2), [OA-FLOW.KT.3](../../OA-FLOW/src/OA-FLOW-KT.md#kt-3), [OA-FLOW.KT.4](../../OA-FLOW/src/OA-FLOW-KT.md#kt-4). The spectral domains, continuous-vector integrals, Gaussian scalar interchange and rectangle/circle complex-analysis arguments are complete in those earlier readers.

<a id="oa-flow.ku.1"></a>

<a id="ku-1"></a>

## KU-1. The implementing group is strongly continuous on the full GNS space

Invariance implies \(\alpha_t(N)=N\), \(\alpha_t(A)=A\), and
\[
V_t\Lambda(x)=\Lambda(\alpha_t(x))\qquad(x\in N)
\tag{KU2}
\]
defines a unitary group on the GNS completion. It implements \(\alpha_t\):
\[
V_t\pi(a)V_{-t}=\pi(\alpha_t(a))\qquad(a\in M).
\tag{KU3}
\]
Indeed both sides applied to \(\Lambda(x)\) give \(\Lambda(\alpha_t(a)x)\). The GNS range is dense, so this proves the operator identity.

Pointwise ultraweak continuity of \(\alpha_t\) does not by itself allow application of the unbounded map \(\Lambda\). Here is the required independent continuity argument. [WR-1](../../OA-FLOW/src/OA-FLOW-WR.md#oa-flow.wr.1)–2 supplies vectors \(\eta_j\) with bounded right multipliers \(R_{\eta_j}\), where
\[
R_{\eta_j}\Lambda(x)=\pi(x)\eta_j\quad(x\in N),\qquad
R_{\eta_j}\to I\text{ strongly},
\]
and the \(R_{\eta_j}\) are positive contractions. For every \(x\in N\) and \(v\in H_\varphi\),
\[
\langle V_t\Lambda(x),R_{\eta_j}^*v\rangle
=\langle\pi(\alpha_t(x))\eta_j,v\rangle
\tag{KU4}
\]
is continuous in \(t\), because \(\pi\) is normal. The linear span of these test vectors is dense: each \(v\) is the norm limit of \(R_{\eta_j}^*v=R_{\eta_j}v\). Unitary uniform boundedness extends continuity first to every test vector, then from \(\Lambda(N)\) to every initial vector. Thus \(V_t\) is weakly continuous. The identity
\[
\|(V_t-V_s)\xi\|^2
=2\|\xi\|^2-2\operatorname{Re}\langle V_{t-s}\xi,\xi\rangle
\]
makes it strongly continuous, without a spectral theorem for arbitrary unitary groups.

The action \(\alpha_t\) is also pointwise strongly* continuous in a concrete representation. At zero expand
\[
(\alpha_t(a)-a)^*(\alpha_t(a)-a)
=\alpha_t(a^*a)-\alpha_t(a)^*a-a^*\alpha_t(a)+a^*a.
\]
Every vector evaluation tends to zero by ultraweak continuity, since multiplication by a fixed bounded operator preserves vector-coefficient continuity. Apply the same argument to \(a^*\), and use the group property at other real parameters.

<a id="oa-flow.ku.2"></a>

<a id="ku-2"></a>

## KU-2. Entire elements for the competing action stay in the finite-star domain

For \(x\in A\), define
\[
a_{n,x}(z)=\sqrt{\frac n\pi}
 \int_{\mathbb R}e^{-n(t-z)^2}\alpha_t(x)\,dt
\tag{KU5}
\]
as the CP ultraweak integral. The operator norm bound, norm-entire dependence, real-translation rule and adjoint rule are exactly the scalar-kernel arguments of [KT-3](../../OA-FLOW/src/OA-FLOW-KT.md#kt-3), applied now to the pointwise strongly* continuous action \(\alpha\):
\[
\|a_{n,x}(z)\|\leq e^{n(\operatorname{Im}z)^2}\|x\|,\qquad
\alpha_s(a_{n,x}(z))=a_{n,x}(z+s),\qquad
a_{n,x}(z)^*=a_{n,x^*}(\bar z).
\tag{KU6}
\]
That argument uses only the explicit Gaussian kernel and normality of the maps, not modularity.

[KU-1](#ku-1) gives the previously missing continuous GNS integrand. The bounded-graph argument of [KT-3](../../OA-FLOW/src/OA-FLOW-KT.md#kt-3), with \(V_t\) replacing \(U_t\), proves
\[
a_{n,x}(z)\in A,\qquad
\Lambda(a_{n,x}(z))
=\sqrt{\frac n\pi}\int_{\mathbb R}e^{-n(t-z)^2}V_t\Lambda(x)\,dt.
\tag{KU7}
\]
The same assertion for \(x^*\), together with (KU6), proves the star-domain part. Compact Riemann sums stay uniformly bounded in operator norm; their GNS vectors converge in norm; [EW-3](../../OA-FLOW/src/OA-FLOW-EW.md#oa-flow.ew.3) identifies their limit. Thus no boundedness of \(\Lambda\) on an operator ball is presumed.

The right side is entire as a Hilbert-valued function: the first two kernel derivatives have an integrable local bound, so the same integral remainder estimate used in [KT-3](../../OA-FLOW/src/OA-FLOW-KT.md#kt-3) works in Hilbert norm. Moreover
\[
\|\Lambda(a_{n,x}(z))\|
\leq e^{n(\operatorname{Im}z)^2}\|\Lambda(x)\|.
\tag{KU8}
\]
At \(z=0\), these vectors converge to \(\Lambda(x)\); their star vectors converge to \(\Lambda(x^*)\), by the Gaussian approximate identity and strong continuity of \(V_t\).

For \(a=a_{n,x}(0)\), use \(\alpha_z(a)=a_{n,x}(z)\) for its entire orbit. This is consistent with complex shifts by (KU6) and the scalar identity theorem. The spaces spanned by \(\Lambda(a)\) and by \(\Lambda(a^*)\), as \(x\in A,n\geq1\) vary, are dense in \(H_\varphi\), since \(\Lambda(A)\) is dense and the preceding limits hold. We need no unproved analytic-vector theorem for a generator of \(V_t\).

<a id="oa-flow.ku.3"></a>

<a id="ku-3"></a>

## KU-3. A bounded periodic entire pairing identifies the two groups

Choose \(a\) of the Gaussian type from [KU-2](#ku-2) and \(b\) of the Gaussian type for \(\sigma\) from [KT-3](../../OA-FLOW/src/OA-FLOW-KT.md#kt-3). Define
\[
f(z)=\varphi_0(\alpha_z(a)\sigma_z(b))
=\langle\Lambda(\sigma_z(b)),\Lambda(\alpha_z(a)^*)\rangle.
\tag{KU9}
\]
The product belongs to the finite algebra for every \(z\), because each factor lies in \(A\). The first GNS vector is entire, and the second is anti-entire, by the exact adjoint rules. With the linear-first convention, their inner product is entire. This follows directly from their norm difference quotients and the bounded bilinear estimate.

We record the analytic shift identity with all domains checked. For fixed \(c\in A\), the function
\(h(z)=\varphi_0(\alpha_z(a)c)\)
is entire by the same GNS pairing. On the real edge it agrees with \(K^\alpha_{a,c}\). [KT-1](../../OA-FLOW/src/OA-FLOW-KT.md#kt-1)'s local zero-edge uniqueness identifies the two on the upper strip; equivalently reflect the variable in its lower-strip statement. Consequently
\[
\varphi_0(\alpha_{t+i}(a)c)=\varphi_0(c\alpha_t(a))
\qquad(t\in\mathbb R).
\]
Both sides have entire continuations in \(t\); the identity theorem yields
\[
\varphi_0(\alpha_z(a)c)=\varphi_0(c\alpha_{z-i}(a))
\qquad(z\in\mathbb C,\ c\in A).
\tag{KU10}
\]
The same argument, using KT's already proved KMS condition, gives
\[
\varphi_0(\sigma_z(b)d)=\varphi_0(d\sigma_{z-i}(b))
\qquad(z\in\mathbb C,\ d\in A).
\tag{KU11}
\]
In (KU10) put \(c=\sigma_t(b)\), then in (KU11) put \(d=\alpha_{t-i}(a)\). Both belong to \(A\). For real \(t\),
\[
f(t)=\varphi_0(\sigma_t(b)\alpha_{t-i}(a))
=\varphi_0(\alpha_{t-i}(a)\sigma_{t-i}(b))
=f(t-i).
\]
The identity theorem makes \(f(z)=f(z-i)\) on the entire plane.

This periodic entire function is bounded. Indeed write \(z=t+is\), \(0\leq s\leq1\). Real invariance of both weights and the real-translation rules give
\[
|f(t+is)|
\leq
\|\Lambda(\sigma_{is}(b))\|
\|\Lambda(\alpha_{-is}(a^*))\|.
\tag{KU12}
\]
The right side is continuous and finite on the compact interval of \(s\), by [KT-3](../../OA-FLOW/src/OA-FLOW-KT.md#kt-3) and [KU-2](#ku-2), independently of \(t\). Periodicity therefore bounds the function on every horizontal strip, with one common bound. [SF-4](../../OA-FLOW/src/OA-FLOW-SF.md#oa-flow.sf.sf4)'s circle Cauchy coefficient estimate proves Liouville's conclusion directly: at any center the derivative has modulus at most this bound divided by any radius \(R\); letting \(R\to\infty\) makes it zero. Hence \(f\) is constant.

For real \(t\), constancy and (KU9) say
\[
\langle U_t\Lambda(b),V_t\Lambda(a^*)\rangle
=\langle\Lambda(b),\Lambda(a^*)\rangle.
\tag{KU13}
\]
The two vector families are independently dense by [KT-3](../../OA-FLOW/src/OA-FLOW-KT.md#kt-3) and [KU-2](#ku-2). Boundedness extends the identity to all pairs of Hilbert vectors, so \(V_t^*U_t=I\), or \(V_t=U_t\). Formula (KU3), MW's implementation formula, and faithfulness of \(\pi\) now give
\[
\alpha_t=\sigma_t^\varphi\qquad(t\in\mathbb R).
\tag{KU14}
\]
This proves uniqueness for the stated arbitrary faithful normal semifinite weight, without a countability reduction.

<a id="oa-flow.ku.4"></a>

<a id="ku-4"></a>

## KU-4. For a faithful normal state, KMS alone forces invariance

Let \(\omega\) be a faithful normal state satisfying (KU1) for a pointwise ultraweakly continuous normal automorphism group, without assuming invariance. Here \(A=M\), so take \(b=1\). The two boundary values of \(K^\alpha_{a,1}\) are the same scalar function \(t\mapsto\omega(\alpha_t(a))\).

Translate this closed-strip function vertically by integer multiples of \(i\), identifying its equal values on the seams. This defines a continuous bounded function \(H\) on \(\mathbb C\), holomorphic away from the horizontal integer lines. It is holomorphic across each seam as well: for a small rectangle crossing just one seam, cut at distance \(\varepsilon\) on either side. The two rectangle integrals vanish by [SF-4](../../OA-FLOW/src/OA-FLOW-SF.md#oa-flow.sf.sf4)'s Cauchy theorem; the intervening parallel-edge integrals cancel in the limit by continuity, and the short joining edges tend to zero. Thus the full rectangle integral is zero. The local rectangular Morera criterion makes \(H\) holomorphic across the seam.

The same elementary Liouville argument as [KU-3](#ku-3) makes \(H\) constant. In particular
\(\omega(\alpha_t(a))=\omega(a)\) for every \(a\in M\). [KU-1](#ku-1)–3 then apply and give \(\alpha_t=\sigma_t^\omega\). The argument also works for a nonzero faithful finite normal positive functional after rescaling.

The arbitrary-weight theorem above includes weight invariance among its hypotheses, exactly as stated at the start. Nothing in this proof drops faithfulness, identifies a natural cone, or asserts an operator-valued weight theorem. Those are separate obligations.



## Source versions and terms

The arguments above are programme proofs retained at their reviewed versions. The scalar and spectral, Gaussian integral, predual, GNS, finite-weight and modular graph prerequisites remain the exact linked programme proofs. The nuclear-bidual source record gives every dependency and version. The general-weight theorem in the last section explicitly assumes weight invariance. The faithful finite-state argument proves invariance separately. No human prose or PDF is redistributed, and free reading access to human sources gives no adaptation permission.
