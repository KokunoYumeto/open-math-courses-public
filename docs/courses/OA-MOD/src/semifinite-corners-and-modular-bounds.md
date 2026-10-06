# Semifinite corners and bounded modular operators

**Self-checked by the writing AI.**

The literal corner restriction in Takesaki II, Exercise VIII.3(5) can fail to be semifinite. We first give a complete counterexample. We then prove an explicit corrected criterion: every nonzero projection has a nonzero subcorner on which a partial-isometry transport of the given weight has a bounded modular operator. This retains arbitrary faithful normal semifinite weights and the full projection quantifier. The transport is an actual change to the statement, not a reinterpretation of an unchanged restriction. Exercise VIII.3(9) retains its separate solution obligation.

The inputs are WG-008/013/014's finite domains, BK-07's bounded polar decomposition, SK's full spectral calculus, MF's modular data, PT-08's all-positive trace densities, CZ-10's bounded density perturbation, VR-01/02's trace recognition and continuous inner implementation, and FT-01's trace-to-finite-projection argument. Inner products are linear in their first variable. Positive weight identities retain infinite values.

Two structural inputs remain explicit. **MB-DEP-INNER-DERIVATION** says that a bounded complex-linear derivation of a von Neumann algebra is implemented by a bounded element of that algebra. It is the exact bounded consequence of [Shôichirô Sakai, *Derivations of W*-Algebras*, Theorem 1 (1966), printed 273](https://www.math.uci.edu/~brusso/sakai66.pdf); its full bounded contract is now proved by the programme spectral-tail construction, with the bounded algebraic and analytic inputs. **MB-DEP-SEMIFINITE-TRACE** says that a von Neumann algebra without a type III central component admits a faithful normal semifinite trace. Its primary locator is Takesaki I, Theorem V.2.15. The exact existing programme trace-existence proof is imported at The programme arbitrary-algebra trace-existence theorem through Exact theorem owners and the FT/MB applications, including the normal corner extension and central gluing. The complete existing affine group proof is reproduced with attribution at TE-14–16. TE-01 identifies the written unrestricted predual compactness proof and its Banach foundations. The general-algebra argument below uses this full contract.

## The literal source statement has a corner-domain obstruction

Let \(M=B(\ell^2(\mathbb N))\), with orthonormal basis \((u_n)_{n\geq1}\), and define

\[
 \varphi(a)=\sum_{n\geq1}n^2\langle au_n,u_n\rangle,
 \qquad a\in M_+.
 \tag{MB.1}
\]

This is a normal weight: positivity and nonnegative sums give additivity and homogeneity, and a bounded increasing positive net has increasing diagonal coefficients. The supremum over that net commutes with the supremum of finite partial sums. It is faithful because \(\varphi(a)=0\) forces \(a^{1/2}u_n=0\) for every \(n\). The finite-rank projections \(r_N\) onto \(u_1,\ldots,u_N\) increase strongly to 1 and have finite weight \(\sum_{n\leq N}n^2\). WG-008 therefore proves semifiniteness. This is the full normal semifinite weight from WG-013, not a finite-dimensional approximation.

The algebra also has its canonical faithful normal semifinite trace
\(\tau(a)=\sum_n\langle au_n,u_n\rangle\).
Normality, faithfulness and semifiniteness follow by the same diagonal and cutoff arguments. Its trace identity on every bounded \(x\) follows because both \(\tau(x^*x)\) and \(\tau(xx^*)\) are the nonnegative double sum of the squared matrix coefficients of \(x\), including infinity.

Set

\[
 c=\left(\sum_{n\geq1}n^{-2}\right)^{-1/2},\qquad
 v=\sum_{n\geq1}\frac c n u_n,\qquad e\xi=\langle\xi,v\rangle v.
 \tag{MB.2}
\]

The scalar sum lies in \([1,2]\): for \(n\geq2\), compare \(n^{-2}\) with \(1/[n(n-1)]\) and telescope. Thus \(v\) is a unit vector and \(e\) is a nonzero rank-one projection. Direct evaluation gives

\[
 \varphi(e)=\sum_{n\geq1}n^2\frac{c^2}{n^2}=\infty.
 \tag{MB.3}
\]

Every nonzero projection \(f\leq e\) is \(e\) itself. The corner is \(eMe=\mathbb Ce\), and the literal restriction of \(\varphi\) is infinite on each nonzero positive scalar multiple of \(e\). Its finite cone, finite left ideal and finite linear domain are all \(\{0\}\). It is not semifinite on this nonzero corner, so it has no modular operator in the faithful normal semifinite framework of Chapter VIII. Its zero GNS representation, described in WG-014 Problem 1, is not a faithful modular implementation of the nonzero corner.

Hence trace existence does not imply the printed condition with an unchanged restriction \(\varphi|_{fMf}\) below every prescribed \(e\). The defect occurs even for a type I factor and a normal weight. Adding normality alone does not repair it.

We will change the corner condition explicitly. Projections \(g,f\) are equivalent when there is \(w\in M\) with \(w^*w=g\) and \(ww^*=f\). For such \(w\), the transported corner weight is

\[
 \psi_{g,w}(x)=\varphi(wxw^*),\qquad x\in(gMg)_+.
 \tag{MB.4}
\]

The corrected condition permits this transport on a nonzero \(g\leq e\). It does not claim that \(\psi_{g,w}\) is the original restriction to \(gMg\).

## A bounded modular operator gives a trace

Let \(N\ne0\) carry a faithful normal semifinite weight \(\rho\), whose modular operator \(\Delta_\rho\) is bounded on its full GNS space. Put \(C=\|\Delta_\rho\|\). The closed-operator identity \(J_\rho\Delta_\rho J_\rho=\Delta_\rho^{-1}\) makes the inverse bounded as well, with the same norm. Since the GNS space is nonzero, \(C\geq1\), and

\[
 C^{-1}I\leq\Delta_\rho\leq CI,\qquad
 A=\log\Delta_\rho\in B(H_\rho),\qquad \|A\|\leq\log C.
 \tag{MB.5}
\]

All three operators are defined on the whole Hilbert space. In its faithful GNS representation, identify \(N\) with its represented algebra. The modular flow is \(\sigma_t^\rho(x)=e^{itA}xe^{-itA}\). Its norm derivative at zero is

\[
 D(x)=i[A,x]\in N,\qquad \|D\|\leq2\|A\|.
 \tag{MB.6}
\]

Membership in \(N\) follows from its norm closedness and the difference quotients. Direct multiplication proves the derivation law and \(D(x^*)=D(x)^*\).

Apply the bounded innerness theorem, the provider of **MB-DEP-INNER-DERIVATION**, to obtain \(a\in N\) with \(D(x)=[a,x]\). The *-law gives \([a+a^*,x]=0\). Thus \(k=(a-a^*)/(2i)\) is a bounded self-adjoint element of \(N\) and \(D(x)=i[k,x]\). The two norm-differentiable groups \(\sigma_t^\rho\) and \(x\mapsto e^{itk}xe^{-itk}\) have the same bounded generator. Uniqueness here is elementary: differentiating \(e^{-tD}\sigma_t^\rho(x)\), with the norm-convergent exponential series for the bounded map \(D\), gives zero. Applying the same calculation to the other group identifies both with \(e^{tD}\). Consequently

\[
 \sigma_t^\rho=\operatorname{Ad}(e^{itk}),\qquad t\in\mathbb R.
 \tag{MB.7}
\]

This is one actual norm-continuous unitary group, rather than unrelated inner implementers at separate times. VR-02 now gives a faithful normal semifinite trace on \(N\). More explicitly, \(k\) is fixed by the flow, \(h=e^{-k}\) is a bounded invertible positive element of \(N_\rho\), and CZ-10 gives

\[
 \sigma_t^{\rho_h}
   =\operatorname{Ad}(e^{-itk})\sigma_t^\rho
   =\operatorname{id}.
 \tag{MB.8}
\]

VR-01 identifies \(\rho_h\) as a trace on all positives. The derivation's structural innerness is the named open input; none of the differentiation, domain or group steps is imported implicitly.

## Bounded spectral bands control any subcorner in the band

Suppose \(\tau\) is a faithful normal semifinite trace on \(M\). Its restriction \(\tau_f\) to an arbitrary projection corner \(fMf\) is faithful normal semifinite. Indeed finite positive contractions \(q_i\uparrow1\) give \(f q_i f\uparrow f\), and the trace identity yields

\[
 \tau(fq_if)=\tau(q_i^{1/2}f q_i^{1/2})\leq\tau(q_i)<\infty.
 \tag{MB.9}
\]

WG-008 applies within the corner. Unlike an arbitrary weight, a trace has precisely the compression estimate needed here.

Write a faithful normal semifinite \(\varphi\) as \(\tau_h\), using PT-08, where \(h\) is positive, injective, self-adjoint and affiliated. Let \(p_n=1_{[1/n,n]}(h)\), \(n\geq1\), and take any nonzero \(f\leq p_n\). The subspace \(fH\) lies in \(D(h)\). The compression

\[
 H_f=f(hp_n)f\in fMf,\qquad
 n^{-1}f\leq H_f\leq nf
 \tag{MB.10}
\]

is bounded and invertible on the whole corner Hilbert space. This does not assume that \(f\) commutes with \(h\).

For \(x\in(fMf)_+\), the all-positive trace-density formula in PT-08 gives

\[
 \varphi(x)
 =\sup_{\varepsilon>0}\tau(x^{1/2}h_\varepsilon x^{1/2})
 =\tau_f(x^{1/2}H_f x^{1/2})
 = (\tau_f)_{H_f}(x).
 \tag{MB.11}
\]

For the middle equality, \(f h_\varepsilon f\uparrow H_f\) as bounded positive operators in the corner: the spectral regularizations converge uniformly on the bounded band, and the compressions preserve order. Normality of the trace passes this monotone limit even when its value is infinite. Trace cyclicity and the same bounded regularizations give the last equality. In particular

\[
 n^{-1}\tau_f(x)\leq\varphi(x)\leq n\tau_f(x).
 \tag{MB.12}
\]

The restriction \(\varphi_f\) is faithful, normal and semifinite, by (MB.12) and the finite contraction criterion.

The precise modular bound is

\[
 n^{-2}I\leq\Delta_{\varphi_f}\leq n^2I,\qquad
 D(\Delta_{\varphi_f})=H_{\varphi_f}.
 \tag{MB.13}
\]

To see the full operator, use CZ-10's unitary identification
\(U\Lambda_{\varphi_f}(a)=\Lambda_{\tau_f}(aH_f^{1/2})\).
Bounded invertibility and (MB.12) identify the finite left ideals and give dense, onto GNS transport. Since the reference trace has modular operator \(I\), the closed Tomita graph calculation in CZ-10 gives

\[
 U\Delta_{\varphi_f}U^*
     =\pi_{\tau_f}(H_f)
       \bigl(J_{\tau_f}\pi_{\tau_f}(H_f)J_{\tau_f}\bigr)^{-1}.
 \tag{MB.14}
\]

Both positive factors are bounded, commute as elements of the algebra and its commutant, and have bounds \([n^{-1},n]\). Their product therefore has bounds \([n^{-2},n^2]\) on the entire Hilbert space. This proves (MB.13), including its domain; it is not a calculation only on a finite GNS core.

## The corrected criterion retains every projection

**Corrected local criterion, at the two declared structural inputs.** For an arbitrary von Neumann algebra \(M\) and a faithful normal semifinite weight \(\varphi\), the following are equivalent:

1. \(M\) admits a faithful normal semifinite trace.
2. For every nonzero projection \(e\in M\), there are a nonzero projection \(g\leq e\) and a partial isometry \(w\in M\), with \(w^*w=g\), such that the transported weight \(\psi_{g,w}\) from (MB.4) is faithful normal semifinite on \(gMg\) and its modular operator is bounded.
3. For every nonzero projection \(e\in M\), there is a nonzero projection \(f\) equivalent to a subprojection of \(e\), such that the literal restriction \(\varphi_f\) is faithful normal semifinite and its modular operator is bounded.

Conditions 2 and 3 change the printed condition explicitly by allowing equivalence transport. They retain the same ambient weight and every nonzero projection, with no state, separability, finite-trace or centralizer hypothesis.

**Proof of \(1\Rightarrow3\).** Choose \(\tau\) and \(h\) as in MB-03. The bounded spectral projections \(p_n\uparrow1\), because \(h\) is injective. Given \(e\ne0\), some \(p_ne\ne0\). Its bounded polar decomposition has the exact supports

\[
 p_ne=w|p_ne|,\qquad
 g=w^*w=s(ep_ne)\leq e,\qquad
 f=ww^*=s(p_nep_n)\leq p_n.
 \tag{MB.15}
\]

Both supports are nonzero. MB-03 proves that \(\varphi_f\) is faithful normal semifinite with \(\|\Delta_{\varphi_f}\|\leq n^2\). This proves condition 3, without presuming that \(e\) or \(f\) commutes with the density.

**Equivalence of 2 and 3, with modular domains.** For any such \(w\), the map
\(\beta:gMg\to fMf\), \(\beta(x)=wxw^*\), is a normal unital *-isomorphism, with inverse \(y\mapsto w^*yw\). Hence \(\psi_{g,w}=\varphi_f\circ\beta\). The finite left ideals and finite-star domains are carried bijectively by \(\beta\). The GNS map

\[
 V\Lambda_{\psi_{g,w}}(x)=\Lambda_{\varphi_f}(\beta(x))
 \tag{MB.16}
\]

is an onto isometry and extends to a unitary. On their full initial finite-star domains it intertwines the two Tomita operators. Closure, adjoints and uniqueness of polar decomposition give

\[
 V\Delta_{\psi_{g,w}}V^*=\Delta_{\varphi_f},\qquad
 V D(\Delta_{\psi_{g,w}})=D(\Delta_{\varphi_f}).
 \tag{MB.17}
\]

Thus normality, faithfulness, semifiniteness and boundedness of the modular operator transport in either direction. This proves \(2\Leftrightarrow3\).

**Proof of \(3\Rightarrow1\).** Take the supplied \(f\) and its corner weight. MB-02 produces a faithful normal semifinite trace on \(fMf\). FT-01, applied inside that corner, gives a nonzero finite projection \(p\leq f\). It is finite also in \(M\): a partial isometry with initial \(p\) and final projection dominated by \(p\) lies in \(pMp\subseteq fMf\).

If \(w^*w=g\leq e\) and \(ww^*=f\), put

\[
 q=w^*pw\leq g\leq e,\qquad z=pw,\qquad
 z^*z=q,\quad zz^*=p.
 \tag{MB.18}
\]

The projection \(q\) is nonzero and finite. Indeed, if \(v^*v=q\) and \(vv^*=r\leq q\), the partial isometry \(zvz^*\) has initial \(p\) and final \(zrz^*\leq p\). Finiteness of \(p\) forces \(zrz^*=p\), hence \(r=q\). Thus every nonzero projection of \(M\) dominates a nonzero finite projection. A nonzero type III central summand would contradict this assertion by taking its identity projection as \(e\). There is therefore no type III component. Apply the exact **MB-DEP-SEMIFINITE-TRACE** input to obtain the required faithful normal semifinite trace on \(M\). \(\square\)

For \(M=0\), the projection conditions are vacuous and the zero weight is its faithful normal semifinite trace, so the equivalence still holds. The argument uses only a countable spectral exhaustion of one injective density; it imposes no countable decomposition of \(M\). Its two structural inputs, described at the start of the lesson, are not proved here.

## Exact tests of transport and modular bounds

**Transport repairs the singular rank-one corner.** In MB-01, define

\[
 H_N=\sum_{n=1}^N n^{-2},\qquad
 v_N=H_N^{-1/2}\sum_{n=1}^N n^{-1}u_n,\qquad
 f_N\xi=\langle\xi,v_N\rangle v_N,\qquad
 w_N\xi=\langle\xi,v\rangle v_N.
 \tag{MB.19}
\]

Then \(w_N^*w_N=e\) and \(w_Nw_N^*=f_N\), whereas \(f_N\not\leq e\), since \(v_N\) is not parallel to \(v\). On the original corner the transported weight is now

\[
 \psi_{e,w_N}(\lambda e)=\lambda\,\frac N{H_N},\qquad
 \Delta_{\psi_{e,w_N}}=I,\qquad \lambda\geq0.
 \tag{MB.20}
\]

Its mass is finite for every \(N\), though \(N/H_N\to\infty\). The original restriction still has infinite mass. The modular bound 1 follows because this one-dimensional finite weight is a trace; it is independent of its nonzero mass.

**The band bound \(n^2\) is sharp.** For \(n>1\), take \(M_2(\mathbb C)\), \(\tau=\operatorname{Tr}\), and \(h=\operatorname{diag}(n^{-1},n)\). In the trace GNS realization, the modular operator for \(\tau_h\) is \(b\mapsto hbh^{-1}\). Its values on the four matrix-unit directions are

\[
 E_{11}\mapsto E_{11},\quad E_{22}\mapsto E_{22},\quad
 E_{12}\mapsto n^{-2}E_{12},\quad
 E_{21}\mapsto n^2E_{21}.
 \tag{MB.21}
\]

Thus the lower and upper bounds in (MB.13) are both attained. This also fixes the numerator/denominator order in (MB.14).

**A bounded modular operator does not make the whole corner finite.** The canonical trace on \(B(\ell^2)\) has \(\Delta=I\), while its identity projection is infinite: the unilateral shift \(S u_n=u_{n+1}\) has \(S^*S=1\) and \(SS^*=1-E_{11}<1\). MB-04 therefore extracts a finite subprojection after producing a trace; it does not incorrectly declare the supplied \(f\) finite merely because its modular operator is bounded.

The accompanying original figure depicts the exact projection and weight maps, the rank-one domain obstruction and its transported repair, and the sharp matrix modular eigenvalues. Proof locators are MB-01 and MB-03–05. Human-source locators are Masamichi Takesaki, *Theory of Operator Algebras II*, Exercise VIII.3(5); *Theory of Operator Algebras I*, Theorem V.2.15; and Shôichirô Sakai, Theorem 1, printed 273 in the cited 1966 paper.
