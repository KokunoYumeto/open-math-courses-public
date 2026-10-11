# Measurable corners and modular spectra

*Original exposition by the OA-MOD course project; CC0-1.0.*

A modular operator for one weight can have spectral values that disappear when the weight changes. For a countable measured relation, the values that survive **every** weight are detected by restricting the relation to **every** positive-measure subset. We prove this identification, including zero, and give an elementary description through partial returns. All base measures below may be sigma-finite with infinite total mass.

## 1. The two intersections and their proof inputs

Let a countable group \(\Gamma\) act nonsingularly by Borel bijections on a nonzero standard Borel sigma-finite measure space \((X,\mu)\). Freeness is not assumed. Write

\[
 R=\{(y,x):y\in\Gamma x\},\qquad
 R_B=R\cap(B\times B),\qquad
 \delta(y,x)=\frac{d\nu_r}{d\nu_s}(y,x).
 \tag{RMS.1}
\]

Arrows run from source \(x\) to range \(y\); the source counting measure is

\[
 \int_R F\,d\nu_s
   =\int_X\sum_{y\in[x]_R}F(y,x)\,d\mu(x).
 \tag{RMS.2}
\]

Each endpoint pair is counted once, irrespective of stabilizers. RWT01 constructs the sigma-finite equivalent counting measures and a positive finite cocycle representative on an invariant conull set. In particular,

\[
 \begin{gathered}
 \delta(z,x)=\delta(z,y)\delta(y,x),\qquad \delta(x,x)=1,\\
 d_g(x):=\delta(gx,x),\qquad \mu(gC)=\int_Cd_g\,d\mu.
 \end{gathered}
 \tag{RMS.3}
\]

All pointwise cocycle formulas in this lesson are on that conull relation.

For a positive finite measurable function \(a\) on a sigma-finite space, its essential range in \([0,\infty)\) consists of those finite \(\lambda\geq0\) for which every neighborhood of \(\lambda\) has positive-measure inverse image. This definition permits zero as a limit of positive values. It does not adjoin infinity. Define

\[
 r_\infty(R,\mu)
  =\bigcap_{\mu(B)>0}\operatorname{ess\,ran}_{R_B}\delta.
 \tag{RMS.4}
\]

The intersection is over Borel sets, with no finite-measure restriction.

Put

\[
 M=\mathcal M(R,\mu),\quad A=L^\infty(X,\mu)\subset M,\quad
 \varphi(T)=\int_XE(T)\,d\mu\quad(T\geq0).
 \tag{RMS.5}
\]

Here \(A\) acts on the range coordinate. RWT02–RWT03 construct the faithful normal semifinite weight \(\varphi\), its full modular operators and equivalent-measure transport. RWT07 identifies every diagonal corner on its two-endpoint Hilbert space. EDT05–EDT07 prove the complete trace/invariant-measure correspondence and its density conventions. The maximal-diagonal and center proof, Theorem 4.2 and Corollary 4.3 gives \(A'\cap M=A\) and makes \(M\) a factor exactly when the action is ergodic.

For a nonzero factor, the invariant to be identified is

\[
 S(M)=\bigcap_{\psi\ {\rm faithful\ normal\ semifinite}}
                 \operatorname{Sp}(\Delta_\psi).
 \tag{RMS.6}
\]

These are the complete modular operators of weights on the same algebra \(M\). The definition is not an intersection over states alone or over weights on varying corners.

The exact general spectral inputs are:

- MG0–MG1 prove the full finite-ideal GNS filter identity and
  \(\operatorname{Sp}(\sigma^\psi)=\operatorname{Sp}(\log\Delta_\psi)\) for every faithful normal semifinite weight. MG2, in the same lesson, proves normal semifinite restriction to every fixed corner.
- GCC, central support and central fixed corners prove that central projections of the fixed algebra suffice in the intersection defining the Connes spectrum, for arbitrary von Neumann algebras.
- MIV2, equation MIV2.h proves
  \(S(M)\cap(0,\infty)=\exp\Gamma(\sigma^\psi)\) for every factor and every faithful normal semifinite reference weight. Its proof compares all weights using normalized cocycle reconstruction and the full cocycle spectral intersection.
- MIV3 proves \(0\in\operatorname{Sp}(\Delta_\psi)\) for every such weight on every nonzero type III algebra. It uses the complete reciprocal domains, the bounded-derivation implementer theorem and a centralizer density that would otherwise produce a trace.
- L18, Section 6, through L18.6.k constructs the largest central summand carrying a faithful normal semifinite trace. Thus a factor either carries such a trace or has no nonzero finite projections.

These are earlier programme proofs at their stated hypotheses. SK05 and SK07 provide the unbounded multiplication calculus, including the logarithm's actual domain. The return arguments in Sections 3–5 below require no general spectral theorem.

## 2. The full spectrum in every measurable corner

Let \(B\subset X\) have positive measure and put \(e=M_{1_B}\). RWT07 identifies the standard corner space as

\[
 H_B=eJeJH=L^2(R_B,\nu_s|_{R_B}).
 \tag{RMS.7}
\]

It is usually smaller than \(eH\), which restricts only the range endpoint. The restriction \(\varphi_B=\varphi|_{eMe}\) is faithful normal semifinite even if \(\mu(B)=\infty\). Its full modular operator is

\[
 \Delta_B\xi=\delta\xi,\qquad
 D(\Delta_B)=
 \left\{\xi\in H_B:\int_{R_B}\delta^2|\xi|^2\,d\nu_s<\infty\right\}.
 \tag{RMS.8}
\]

The logarithm is multiplication by \(\log\delta\) on

\[
 D(\log\Delta_B)=
 \left\{\xi\in H_B:\int_{R_B}|\log\delta|^2|\xi|^2\,d\nu_s<\infty\right\}.
 \tag{RMS.9}
\]


**Lemma.** With these complete domains,

\[
 \operatorname{Sp}(\Delta_B)=\operatorname{ess\,ran}_{R_B}\delta,
 \qquad
 \operatorname{Sp}(\log\Delta_B)
   =\log\bigl(\operatorname{ess\,ran}_{R_B}\delta\cap(0,\infty)\bigr).
 \tag{RMS.10}
\]


**Proof.** We give the resolvent argument for any real measurable multiplier \(a\) with its maximal square-integrability domain. It is self-adjoint by SK05. If \(z\notin\mathbb R\), both \(1/(a-z)\) and \(a/(a-z)=1+z/(a-z)\) are bounded. Thus multiplication by \(1/(a-z)\) maps the entire Hilbert space into the domain of \(a\), and the two pointwise products prove both inverse identities. The nonreal points lie in the resolvent.

If a real \(\lambda\) is absent from the essential range, some \(\varepsilon>0\) satisfies \(|a-\lambda|\geq\varepsilon\) almost everywhere. The same bounded reciprocal and product argument gives an everywhere-defined bounded inverse for \(a-\lambda\).

Conversely, suppose \(\lambda\) is in the essential range. Each set
\(F_n=\{|a-\lambda|<1/n\}\) has positive measure. Sigma-finiteness supplies a measurable subset \(C_n\subset F_n\) of finite positive measure. The vectors

\[
 \xi_n=\frac{1_{C_n}}{\nu_s(C_n)^{1/2}}
 \tag{RMS.11}
\]

have norm one, lie in the multiplier domain because \(a\) is bounded on \(C_n\), and satisfy \(\|(a-\lambda)\xi_n\|\leq1/n\). A bounded inverse would force
\(1\leq\|(a-\lambda)^{-1}\|/n\) for every \(n\), a contradiction. Apply this to \(a=\delta\) and \(a=\log\delta\). For each finite \(s\in\mathbb R\), continuity of the mutually inverse scalar maps \(\log,\exp\) identifies the nonnull neighborhood tests at \(s\) and \(e^s\). This proves (RMS.10). \(\square\)

In particular, zero lies in \(\operatorname{Sp}(\Delta_B)\) exactly when every set \(\{(y,x)\in R_B:\delta(y,x)<\varepsilon\}\) has positive measure. It is never an eigenvalue, because \(\delta>0\) almost everywhere. Zero is not a finite spectral value of \(\log\Delta_B\).

The corner modular action is the restriction of \(\sigma^\varphi\): both multiply a kernel by \(\delta^{it}\), and the equality extends normally from the generating kernels. Alternatively MG2 gives the same conclusion with its full weight-domain proof. No normalization by \(\mu(B)\) has been used.

## 3. Return witnesses and the multiplicative subgroup

**Return criterion.** A finite \(\lambda\geq0\) belongs to \(r_\infty(R,\mu)\) exactly when, for every positive-measure Borel \(B\) and every \(\varepsilon>0\), there are \(g\in\Gamma\) and a Borel \(D\) such that

\[
 \begin{gathered}
 D\subset B,\quad gD\subset B,\quad
 0<\mu(D)<\infty,\quad \mu(gD)<\infty,\\
 |d_g(x)-\lambda|<\varepsilon\quad(x\in D).
 \end{gathered}
 \tag{RMS.12}
\]

after removal of a null set.

**Proof.** The arrow set in \(R_B\) on which \(|\delta-\lambda|<\varepsilon\) is a countable union of pieces of group graphs. Its source counting measure is positive if and only if at least one such graph piece has a positive-measure domain. Intersect that domain with a finite-measure exhaustion \(X_n\) and with \(g^{-1}X_m\); some pair still has positive measure. This gives (RMS.12). Conversely such a graph piece has source counting measure \(\mu(D)>0\), so it proves the essential-range test. \(\square\)

**Proposition.** The set \(r_\infty\) is closed in \([0,\infty)\), contains \(1\), and its positive part

\[
 G_R=r_\infty(R,\mu)\cap(0,\infty)
 \tag{RMS.13}
\]

is a closed multiplicative subgroup of \((0,\infty)\). These assertions do not require ergodicity.

**Proof.** Essential ranges are closed: failure of the defining test gives an open interval disjoint from the essential range. Their intersection is therefore closed. The diagonal of each \(R_B\) has positive counting measure and derivative \(1\), so \(1\in r_\infty\).

Let \(\lambda>0\) belong to \(r_\infty\). Given \(B,\varepsilon\), choose
\(0<\rho<\lambda/2\) with \(2\rho/\lambda^2<\varepsilon\), and use (RMS.12) near \(\lambda\). On \(gD\), the inverse return has derivative

\[
 d_{g^{-1}}(gx)=d_g(x)^{-1},\qquad
 |d_g(x)^{-1}-\lambda^{-1}|
 \leq\frac{2|d_g(x)-\lambda|}{\lambda^2}<\varepsilon.
 \tag{RMS.14}
\]

Nonsingularity makes \(\mu(gD)>0\). Thus the return criterion proves \(\lambda^{-1}\in r_\infty\).

Let \(\lambda,\kappa>0\) belong to \(r_\infty\). Choose \(0<\rho<1\) with
\((\lambda+\kappa+1)\rho<\varepsilon\). First choose a return
\(g:D_0\to gD_0\) inside \(B\) whose derivative differs from \(\kappa\) by less than \(\rho\). Apply the \(\lambda\)-return criterion inside the positive set \(D_0\), obtaining
\(h:D_1\to hD_1\subset D_0\). The composition \(gh\) has source and range in \(B\), and

\[
 d_{gh}(x)=d_g(hx)d_h(x),\qquad
 |d_{gh}(x)-\kappa\lambda|
 <(\kappa+\lambda)\rho+\rho^2<\varepsilon.
 \tag{RMS.15}
\]

Its source has positive measure. If necessary, intersect it with a finite-measure range cutoff as in the return criterion. Thus \(\kappa\lambda\in r_\infty\). Relative closedness in \((0,\infty)\) follows from the already proved closedness in \([0,\infty)\). \(\square\)

The second return must be taken inside the first return's **domain**. Choosing two unrelated returns inside \(B\) would not ensure that their composition is defined on a positive-measure set.

## 4. Changing an arbitrary positive density

Let \(d\mu'=q\,d\mu\), where \(0<q<\infty\) almost everywhere. This measure is sigma-finite: intersect a finite-\(\mu\) cover with the sets \(\{q\leq n\}\). RWT03 gives

\[
 d\nu_s'=q(x)\,d\nu_s,\qquad
 \delta'(y,x)=\frac{q(y)}{q(x)}\delta(y,x).
 \tag{RMS.16}
\]


**Theorem.** Without ergodicity,

\[
 r_\infty(R,\mu')=r_\infty(R,\mu).
 \tag{RMS.17}
\]


**Proof.** Fix \(\lambda\in r_\infty(R,\mu)\), a positive-measure set \(B\) and \(\varepsilon>0\). If \(\lambda>0\), choose \(\eta>0\) and \(\rho>0\) such that

\[
 \eta\lambda<\varepsilon/2,\qquad
 (1+\eta)\rho<\varepsilon/2.
 \tag{RMS.18}
\]

Some intersection of \(B\) with a density band
\(\{a\leq q<(1+\eta)a\}\), \(a=(1+\eta)^k\), \(k\in\mathbb Z\), has positive measure; these bands countably cover \(\{0<q<\infty\}\). Call it \(C\). On \(R_C\),

\[
 (1+\eta)^{-1}\leq q(y)/q(x)\leq1+\eta.
 \tag{RMS.19}
\]

There is a positive counting-measure set of arrows in \(R_C\) with
\(|\delta-\lambda|<\rho\). On it,

\[
 |\delta'-\lambda|
 \leq(1+\eta)|\delta-\lambda|+\eta\lambda<\varepsilon.
 \tag{RMS.20}
\]

The new counting measure is equivalent to the old one, so this witnesses the required new essential range in \(R_B\).

For \(\lambda=0\), choose a positive part of \(B\) in a dyadic band of \(q\). The quotient in (RMS.16) is at most \(2\) there, and the positive-measure arrow set where \(\delta<\varepsilon/2\) gives \(\delta'<\varepsilon\). This includes zero in the new ratio set. Apply the same reasoning with density \(q^{-1}\) for the reverse inclusion. \(\square\)

The density may be unbounded and may approach zero. The proof bounds it only on a newly chosen positive subset of each test set. A global upper or lower bound is not assumed.

## 5. Every positive reduction of an ergodic relation

Assume now that the action is ergodic: every invariant measurable set is null or conull.

**Theorem.** For every positive-measure Borel \(B\),

\[
 r_\infty(R_B,\mu|_B)=r_\infty(R,\mu).
 \tag{RMS.21}
\]

On the left the definition tests all positive-measure subsets of \(B\), using the restricted relation.

**Proof.** Every test subset of \(B\) is also a test subset of \(X\), so the right side is contained in the left side. For the reverse inclusion, let \(\lambda\) belong to the left side, and fix an arbitrary positive-measure \(C\subset X\). The saturation \(\bigcup_{g\in\Gamma}g^{-1}B\) is invariant and contains \(B\), hence is conull. Countability gives \(g\) such that

\[
 C_0=C\cap g^{-1}B
 \tag{RMS.22}
\]

has positive measure.

Shrink \(C_0\) to a positive-measure \(C_1\) on which \(d_g\) lies in a band \([a,(1+\eta)a)\). Put \(D=gC_1\subset B\). The simultaneous cocycle identity gives

\[
 \delta(gy,gx)=\frac{d_g(y)}{d_g(x)}\delta(y,x)
 \qquad((y,x)\in R_{C_1}).
 \tag{RMS.23}
\]

To verify the counting-measure issue explicitly, for every nonnegative Borel \(F\) on \(R_D\), reindex the orbit count and use (RMS.3):

\[
 \int_{R_D}F\,d\nu_s
 =\int_{C_1}d_g(x)
      \sum_{y\in C_1\cap[x]_R}F(gy,gx)\,d\mu(x).
 \tag{RMS.24}
\]

Thus the arrow bijection \((y,x)\mapsto(gy,gx)\) preserves null sets in both directions.

For \(\lambda>0\), choose \(\eta,\rho\) as in (RMS.18). Since \(\lambda\) survives every reduction inside \(B\), the set in \(R_D\) where
\(|\delta-\lambda|<\rho\) has positive measure. Pull it back by (RMS.24). Solving (RMS.23) for \(\delta(y,x)\) multiplies by \(d_g(x)/d_g(y)\), which obeys the same bounds as (RMS.19). Estimate (RMS.20) therefore puts the pulled-back derivative within \(\varepsilon\) of \(\lambda\). It is a positive-measure arrow set inside \(R_C\).

For \(\lambda=0\), use a dyadic band for \(d_g\) and the bound \(2\), exactly as in RMS04. In both cases \(\lambda\) lies in the essential range on \(R_C\). Since \(C,\varepsilon\) were arbitrary, it lies in the global ratio set. \(\square\)

This argument controls the derivative of the map transporting one reduction to another. Ergodicity alone gives a nonnull transport domain; it does not make that transport measure preserving.

## 6. The diagonal detects the entire Connes spectrum

For a point-ultraweakly continuous real automorphism group \(\alpha\), use the positive Fourier convention

\[
 \widehat f(s)=\int_{\mathbb R}f(t)e^{its}\,dt,\qquad
 T_f^\alpha(x)=\int_{\mathbb R}f(t)\alpha_t(x)\,dt.
 \tag{RMS.25}
\]

Its spectrum is the common zero set of all \(\widehat f\) for which \(T_f^\alpha=0\). If \(N=M^\alpha\), its Connes spectrum is

\[
 \Gamma(\alpha)=\bigcap_{0\ne p\in\operatorname{Proj}(N)}
                         \operatorname{Sp}(\alpha^p).
 \tag{RMS.26}
\]

The normal integrated maps and their full-domain spectral meaning are the MG proofs cited in RMS01.

**Theorem.** For every relation in RMS01, including nonergodic ones,

\[
 \Gamma(\sigma^\varphi)
 =\bigcap_{\mu(B)>0}\operatorname{Sp}
             \bigl((\sigma^\varphi)^{M_{1_B}}\bigr)
 =\log\bigl(r_\infty(R,\mu)\cap(0,\infty)\bigr).
 \tag{RMS.27}
\]


**Proof.** The explicit kernel action fixes \(A\) pointwise. With
\(N=M_\varphi\), maximal abelianness gives

\[
 A\subset N,\qquad Z(N)\subset A.
 \tag{RMS.28}
\]

The GCC central-support theorem says

\[
 \Gamma(\sigma^\varphi)
 =\bigcap_{0\ne z\in\operatorname{Proj}(Z(N))}
                     \operatorname{Sp}((\sigma^\varphi)^z).
 \tag{RMS.29}
\]

Here is its exact mechanism: the central support of \(p\in N\) is the join of \(vpv^*\), \(v\) unitary in \(N\). A nonzero spectrally localized element in the central-support corner has a nonzero sandwich \(pv^*xwp\) for some fixed unitaries \(v,w\). Otherwise the support joins annihilate it on both sides. Fixed multipliers retain its spectral support. Local Fourier detection consequently makes the spectra of the \(p\)-corner and its central-support corner identical. GCC proves the local detection and join arguments in full; it does not assume \(N\) is a factor.

Every projection of \(A\) is \(M_{1_B}\) modulo null sets, and it is nonzero exactly when \(\mu(B)>0\). Inclusions (RMS.28) therefore sandwich the middle intersection of (RMS.27) between (RMS.26) and (RMS.29). They coincide.

GCC uses negative Fourier labels in its general-group presentation. This does not change the whole action spectra used here. In detail, changing the transform sign reflects labels \(s\mapsto-s\). For a star action,
\(T_{\bar f}(x^*)=T_f(x)^*\), and
\(\widehat{\bar f}(s)=\overline{\widehat f(-s)}\), so its action-annihilator hull is symmetric under reflection. The same is true on each fixed corner. Thus the central-corner equality has precisely the convention (RMS.25); no claim that individual vector spectra keep their sign is needed.

For each \(B\), RMS02 and MG1–MG2 give

\[
 \operatorname{Sp}((\sigma^\varphi)^{M_{1_B}})
 =\operatorname{Sp}(\log\Delta_B)
 =\log\bigl(\operatorname{ess\,ran}_{R_B}\delta
                                      \cap(0,\infty)\bigr).
 \tag{RMS.30}
\]

The scalar logarithm is a bijection on \((0,\infty)\), so it commutes with this intersection. Equation (RMS.4) now gives (RMS.27). \(\square\)

The Hilbert space in (RMS.30) is always (RMS.7). This proof keeps the original sigma-finite measure and the full corner weight; it does not pass to a state to identify the corner spectrum.

## 7. All weights on the factor, including zero

**Theorem.** If the countable nonsingular action is ergodic, then

\[
 \boxed{\quad
 S\bigl(\mathcal M(R,\mu)\bigr)=r_\infty(R,\mu).
 \quad}
 \tag{RMS.31}
\]

The hypotheses allow infinite \(\mu(X)\), nonfree actions and unbounded derivatives.

**Proof.** The center formula from RMS01 makes \(M\) a nonzero factor. MIV2.h applies to the faithful normal semifinite reference \(\varphi\) and gives

\[
 S(M)\cap(0,\infty)=\exp\Gamma(\sigma^\varphi).
 \tag{RMS.32}
\]

Together with RMS06, this identifies the positive parts of both sides of (RMS.31). The MIV2 proof includes every faithful normal semifinite weight: normalized relative cocycles give one direction, realization of every strongly continuous unitary cocycle as a weight gives the other. It is not an assertion that the spectra of all weights are equal.

It remains to decide zero. The trace-existence proof in L18.6.k makes the factor either trace-semifinite or type III.

In the trace-semifinite case, EDT05 supplies an equivalent sigma-finite invariant measure \(\eta\). For this measure \(\delta_\eta=1\), and every positive reduction has a positive-measure diagonal. Hence

\[
 r_\infty(R,\eta)=\{1\},\qquad
 r_\infty(R,\mu)=\{1\}
 \tag{RMS.33}
\]

by RMS04. A faithful normal semifinite trace \(\tau\) has modular operator \(I\): on the dense finite-star GNS domain its involution is isometric by
\(\tau(x^*x)=\tau(xx^*)\), and its square is the identity there. Its extension is consequently an onto antiunitary, and its adjoint product is \(I\). Thus \(S(M)\subset\{1\}\). For any faithful normal semifinite \(\psi\), a filter annihilating the action satisfies

\[
 0=T_f^{\sigma^\psi}(1)=\left(\int f(t)\,dt\right)1.
 \tag{RMS.34}
\]

So \(0\in\operatorname{Sp}(\sigma^\psi)\), and MG1 puts \(1\) in \(\operatorname{Sp}(\Delta_\psi)\). Therefore \(S(M)=\{1\}\), as required.

In the type III case, MIV3 proves \(0\in S(M)\). For every positive-measure \(B\), its nonzero corner \(eMe\) also has no nonzero finite projections. Indeed a projection below \(e\) is finite in \(eMe\) exactly when it is finite in \(M\): any partial isometry witnessing an equivalence to a smaller subprojection has both supports below \(e\), hence belongs to \(eMe\). Apply MIV3 to this corner and its faithful normal semifinite weight \(\varphi_B\). It gives

\[
 0\in\operatorname{Sp}(\Delta_B)
   =\operatorname{ess\,ran}_{R_B}\delta.
 \tag{RMS.35}
\]

This holds for every \(B\), so \(0\in r_\infty(R,\mu)\). With the equality of positive parts, this proves (RMS.31). \(\square\)

The argument at zero applies a theorem to each complete corner operator. Taking the closure of an already intersected positive set would be insufficient: the positive part \(\{1\}\) occurs both for the semifinite case and for type \(\mathrm{III}_0\).

## 8. The spectral alternatives

By RMS03, the set

\[
 L=\log\bigl(r_\infty(R,\mu)\cap(0,\infty)\bigr)
 \tag{RMS.36}
\]

is a closed additive subgroup of \(\mathbb R\), even without ergodicity. We classify it directly. If it has no positive member, symmetry gives \(L=\{0\}\). Otherwise put \(a=\inf(L\cap(0,\infty))\). If \(a>0\), closedness puts \(a\) in \(L\). For each \(s\in L\), division with remainder gives \(s=na+r\), \(0\leq r<a\), and the definition of \(a\) forces \(r=0\). Thus \(L=a\mathbb Z\). If \(a=0\), choose \(a_n\in L\) with \(0<a_n<1/n\). Integer multiples of \(a_n\) approximate every real number with error at most \(a_n\). Closedness then gives \(L=\mathbb R\).

Whenever \(L\ne\{0\}\), the positive ratio set contains a number less than \(1\) and all of its positive integral powers. Closedness of \(r_\infty\) in \([0,\infty)\) therefore includes zero. Thus the only possible full ratio sets are

\[
 \{1\},\qquad \{0,1\},\qquad
 \{0\}\cup\lambda^{\mathbb Z}\ (0<\lambda<1),\qquad
 [0,\infty).
 \tag{RMS.37}
\]

For an ergodic relation, RMS07 identifies these with the following modular classifications:

| Measured ratio set | Conclusion for the relation factor |
| --- | --- |
| \(\{1\}\) | It admits a faithful normal semifinite trace. |
| \(\{0,1\}\) | It is of type \(\mathrm{III}_0\). |
| \(\{0\}\cup\lambda^{\mathbb Z}\), \(0<\lambda<1\) | It is of type \(\mathrm{III}_\lambda\). |
| \([0,\infty)\) | It is of type \(\mathrm{III}_1\). |

Here the type III subtype names are defined by their displayed \(S\)-invariants. The first row follows in both directions from RMS07 and its zero proof. It does not distinguish types I, \(\mathrm{II}_1\) and \(\mathrm{II}_\infty\). The other rows do not assert isomorphism classification within a subtype or existence of a relation realizing every row.

Ergodicity is essential to these **factor** conclusions. For example, the identity relation on two positive-mass points has ratio set \(\{1\}\) and algebra \(\mathbb C\oplus\mathbb C\), whose two diagonal central projections explicitly show that it is not a factor.

## 9. Complete calculations and a zero-spectrum test

**Finite weights retain extra frequencies.** On the complete relation on \(\{1,2\}\), take masses \(p_1=1/3\), \(p_2=2/3\). On the normalized arrow vectors
\(f_{ij}=1_{\{(i,j)\}}/\sqrt{p_j}\), the modular multiplier has eigenvalues \(p_i/p_j\). Thus

\[
 \operatorname{Sp}(\Delta_\varphi)=\{1/2,1,2\},\qquad
 \operatorname{Sp}(\log\Delta_\varphi)=\{-\log2,0,\log2\}.
 \tag{RMS.38}
\]

Both singleton reductions have spectrum \(\{1\}\). Every positive reduction contains a diagonal arrow of derivative \(1\), so

\[
 r_\infty=\{1\},\qquad \Gamma(\sigma^\varphi)=\{0\},
 \qquad S(M_2(\mathbb C))=\{1\}.
 \tag{RMS.39}
\]

The modular centralizer is the diagonal algebra, since its two density eigenvalues are distinct. It is not a factor. This checks why RMS06 used central projections of the centralizer rather than assuming that centralizer factorial.

**Zero in one modular spectrum is not intrinsic.** On
\(X=\{1,2,\ldots\}\), take the complete relation presented by the countable group of finite permutations and the probability masses \(p_n=2^{-n}\). The relation algebra is \(B(\ell^2(X))\): the partial single-point orbit maps give all matrix units, their finite compressions converge strongly to any bounded matrix, and the orbit representation is its faithful row representation. On the normalized arrow basis,

\[
 \Delta_\varphi f_{ij}=2^{j-i}f_{ij},\qquad
 \operatorname{Sp}(\Delta_\varphi)=\{0\}\cup2^{\mathbb Z}.
 \tag{RMS.40}
\]

Every integer power occurs. Their only finite accumulation point outside the powers is zero, and RMS02's resolvent characterization proves that this is the full spectrum. The unit vectors \(f_{n1}\) satisfy

\[
 \|\Delta_\varphi f_{n1}\|=2^{1-n}\longrightarrow0,
 \qquad \ker\Delta_\varphi=\{0\}.
 \tag{RMS.41}
\]

The maximal domain is the set of arrow coefficient families with
\(\sum_{i,j}2^{2(j-i)}|\xi_{ij}|^2<\infty\).
Nevertheless a singleton reduction has modular operator \(1\); hence
\(r_\infty=\{1\}\). Counting measure is equivalent and invariant, and EDT05 gives the usual semifinite matrix trace. Therefore \(S(B(\ell^2(X)))=\{1\}\). This is a semifinite factor with a state whose modular spectrum contains zero.

**Changing the measure changes one spectrum.** In the same infinite example the density taking \(\mu\) to counting measure is \(q_n=2^n\). Formula (RMS.16) gives

\[
 \delta'(i,j)=\frac{2^i}{2^j}\,2^{j-i}=1.
 \tag{RMS.42}
\]

Thus the counting-weight modular spectrum is \(\{1\}\), whereas the probability-weight spectrum is (RMS.40). RMS04 correctly asserts equality only of the intersections over all positive reductions.

**A one-sided corner is the wrong space.** Return to the two-point masses and take \(B=\{1\}\). The space \(eH\) contains both \(f_{11}\) and \(f_{12}\), with modular multiplier eigenvalues \(1\) and \(1/2\). The standard corner space \(eJeJH\) contains only \(f_{11}\). Its spectrum is \(\{1\}\), exactly as required by the scalar corner algebra \(eMe=\mathbb C e\). The extra value \(1/2\) is an artifact of cutting only one endpoint.

The construction source is Masamichi Takesaki, *Theory of Operator Algebras III*, Chapter XIII, Definition 2.12 and Theorem 2.13, printed page 23. The earlier programme lesson Ratio sets and intrinsic modular spectra proves the relation-specific intersection by passing to an equivalent probability. The present argument keeps the original sigma-finite corner domains, supplies explicit return witnesses and reduction transport, and binds the current complete general spectral proofs at the exact locators in RMS01.

