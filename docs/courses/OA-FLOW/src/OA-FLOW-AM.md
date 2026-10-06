# Fourier densities identify the whole dual-action average

*Independent proof: GPT-6 Astra (OpenAI), Ultra, 5 October 2026. New expression is dedicated under CC0 to the extent of rights held.*

This proof compares two already defined objects: the directed Schur-map weight of [GDA3–5](OA-FLOW-GDA.md#gda-3), and integration of an abelian dual action. It proves equality on the entire positive cone. It uses no inference from equality of modular automorphism groups and no arbitrary modular-cocycle realization theorem.

Let \(G\) be an arbitrary locally compact Hausdorff abelian group, \(\Gamma=\widehat G\), with the paired Haar measures of [SP3–4](OA-FLOW-PLANCHEREL.md#scalar-plancherel-p3) and [H3–4](OA-FLOW-HARMONIC-LATE.md#l138-h3). Put

<a id="equation-am1"></a>

\[
 \mathcal Ff(\chi)=\int_G\overline{\chi(s)}f(s)\,ds.
 \tag{AM1}
\]
Use completed locally determined Haar classes, as in [HR8–9](OA-FLOW-HR.md#hr-08) and [L24 Sections 2–4](OA-FLOW-L24.md#oa-flow.grp.haarconventions). Every finite-exponent integrable function has a sigma compact carrier; no such carrier for the whole group is assumed. The scalar normal group weight \(\Omega\), its strict normal minorants \(\mathcal F_\Omega^\circ\), and their coefficient functions \(\mathcal P^\circ\) are the actual constructions in GDA1–3. In particular GDA3 proves, on the whole cone,

<a id="equation-am2"></a>

\[
 p\preccurlyeq c\delta_e
 \quad\Longleftrightarrow\quad
 \omega_p\in L(G)_*^+,\quad \omega_p\leq c\Omega,
 \qquad \omega_p(\lambda_s)=p(s),
 \tag{AM2}
\]
where the left side means
\(\int p(t)(f^\#*f)(t)\,dt\leq c\|f\|_2^2\) for all \(f\in C_c(G)\). Here \(f^\#(s)=\overline{f(-s)}\). The notation \(\delta_e\) is the identity distribution, not a scalar Haar density.

<a id="am-1"></a>

## AM1. Strict minorants and their exact Fourier densities

The partial Fourier formula on compact vectors, extended by unitarity, gives

<a id="equation-am3"></a>

\[
 \mathcal F\lambda_s\mathcal F^*=M_{\overline{\chi(s)}}.
 \tag{AM3}
\]
The multiplier/predual lemma in [ND](OA-FLOW-ND.md#nd-multiplication), applied to \(\Gamma\), and H3 biduality show that these characters generate the whole sectionwise multiplication algebra \(L^\infty(\Gamma)\). Thus (AM3) is a normal isomorphism of \(L(G)\) onto that algebra. Unitary conjugation is normal on all nets by CP vector-series tests. The same ND lemma identifies its full concrete predual isometrically with \(L^1(\Gamma)\); no unproved global Radon–Nikodym theorem is required.

Consequently every positive normal functional \(\omega_p\) has a unique \(k\in L^1(\Gamma)_+\) with

<a id="equation-am4"></a>

\[
 \omega_p(\mathcal F^*M_a\mathcal F)=\int_\Gamma k(\chi)a(\chi)\,d\chi,
 \qquad p(s)=\int_\Gamma k(\chi)\overline{\chi(s)}\,d\chi.
 \tag{AM4}
\]
Positivity of \(k\) follows by testing characteristic functions of its finite-measure level sets; those tests are in the sectionwise multiplication algebra. Suppose \(\omega_p\leq c\Omega\). Applying this to \(\lambda(f)^*\lambda(f)\), and using GDA1's exact finite formula and scalar Plancherel, gives

<a id="equation-am5"></a>

\[
 \int_\Gamma k|\mathcal Ff|^2\,d\chi\leq c\|f\|_2^2
       =c\|\mathcal Ff\|_2^2 \quad(f\in C_c(G)).
 \tag{AM5}
\]
We show carefully that \(k\leq c\) locally almost everywhere. For any measurable finite-measure \(E\subseteq\Gamma\), onto Plancherel and density of \(C_c(G)\) supply a sequence \(f_n\in C_c(G)\) with \(\mathcal Ff_n\to1_E\) in \(L^2\). Pass to a subsequence for which the squared errors are summable. Scalar monotone convergence makes the sum of squared pointwise errors finite almost everywhere, so the subsequence converges to \(1_E\). This argument takes place on the union of the countably many finite-exponent carriers. Fatou's inequality, obtained from the monotone-convergence theorem applied to infima of tails, now gives

<a id="equation-am6"></a>

\[
 \int_E k\,d\chi\leq c|E|. \tag{AM6}
\]
If \(k>c\) on a nonnull set, a set \(\{k>c+1/n\}\) has positive measure for some \(n\). It has finite measure because \(k\in L^1\), and (AM6) is a contradiction. Thus \(k\leq c\). The zero case is included.

Conversely take \(k\in L^1(\Gamma)_+\) with \(k\leq c\). Define \(p\) by (AM4). It is continuous: restrict the finite measure \(k\,d\chi\) to a compact set, use uniform continuity of character evaluation there at the given group point, and bound the omitted part by twice its mass. Its positive-definiteness is the integral of the scalar positive matrices \([\overline{\chi(s_i-s_j)}]\). The interchange against \(f^\#*f\in L^1(G)\) is justified by the product of its L1 norm and \(\|k\|_1\); HR5/L24 provide this actual finite-carrier interchange. It gives

<a id="equation-am7"></a>

\[
 \int_Gp(t)(f^\#*f)(t)\,dt
       =\int_\Gamma k|\mathcal Ff|^2\,d\chi\leq c\|f\|_2^2.
 \tag{AM7}
\]
For \(c>0\), apply (AM2) to \(p/c\); for \(c=0\), both functions are zero. The functional constructed by (AM2) equals the normal functional in (AM4), because they agree on \(\lambda(G)\), whose linear span is ultraweakly dense. This proves the exact correspondence

<a id="equation-am8"></a>

\[
 \mathcal P^\circ\ \longleftrightarrow\ 
 \mathcal D=\{k\in L^1(\Gamma)_+:k\leq c\text{ for some }0\leq c<1\}.
 \tag{AM8}
\]
It proves both directions without first assuming that \(\Omega\) is Haar integration on the whole multiplier cone.

<a id="am-2"></a>

## AM2. A normal Schur map is a normal weighted orbit integral

Let \(N=M\rtimes_\alpha G\) in any faithful normal regular model, and let \(\theta_\chi(\lambda_s\pi(a))=\overline{\chi(s)}\lambda_s\pi(a)\). ND constructs this point-ultraweakly continuous normal action; [AT3](OA-FLOW-AT.md#oa-flow.at.3) gives norm-continuous predual orbits. For \(k\in L^1(\Gamma)\), set

<a id="equation-am9"></a>

\[
 B_k\omega=\int_\Gamma k(\chi)\,\omega\circ\theta_\chi\,d\chi,
 \qquad H_k=B_k^*:N\to N.
 \tag{AM9}
\]
This is a genuine Bochner integral in \(N_*\). On the sigma compact carrier of \(k\), the continuous orbit has separable image on each compact piece; their countable union has separable closed linear span. Scalar measurable approximation and the norm bound \(|k(\chi)|\|\omega\|\) give strong measurability and integrability. L24's Bochner construction therefore gives \(\|B_k\|\leq\|k\|_1\), its adjoint is normal, and for \(k\geq0\) it is positive.

If \(k\) corresponds to \(p\) in (AM4), normality and the generator formula give

<a id="equation-am10"></a>

\[
 H_k(\lambda_s\pi(a))=p(s)\lambda_s\pi(a)=E_p(\lambda_s\pi(a)).
 \tag{AM10}
\]
Here \(E_p\) is the actual GDA4–5 Schur map on \(N\). The linear span of these generators is a unital star algebra: covariance rewrites a product as \(\lambda_{s+t}\pi(\alpha_{-t}(a)b)\), and rewrites adjoints in the same form. BD's bounded density theorem and CP's bounded-strong-to-ultraweak tests make that span ultraweakly dense in \(N\). Since both maps are normal on their entire spaces, (AM10) proves \(H_k=E_p\) everywhere. Equality on generators is being used for bounded normal maps, not for extended weights.

<a id="am-3"></a>

## AM3. Equality of the complete extended-positive maps

For \(X\in N_+\) define the ambient extended-positive average by

<a id="equation-am11"></a>

\[
 A(X)(\omega)=\sup_{K\subseteq\Gamma\ \mathrm{compact}}
                 \int_K\omega(\theta_\chi(X))\,d\chi,
 \qquad \omega\in N_*^+.
 \tag{AM11}
\]
Each compact average is the adjoint construction (AM9) with \(k=1_K\). Compact sets are directed by finite unions. Therefore (AM11) is additive and positively homogeneous in \(\omega\), with the convention \(0\cdot\infty=0\), and is norm lower semicontinuous as a supremum of bounded continuous evaluations. [EP2–3](OA-FLOW-EP.md#ep-2) give its actual extended-positive element, including any nondense finite form domain and infinite part. Haar regularity identifies the supremum with the nonnegative integral of this continuous function.

The GDA weight is, on each entire positive element,

<a id="equation-am12"></a>

\[
 T(X)(\omega)=\sup_{p\in\mathcal P^\circ}\omega(E_p(X))
             =\sup_{k\in\mathcal D}\int_\Gamma k(\chi)\omega(\theta_\chi(X))\,d\chi.
 \tag{AM12}
\]
The second equality is AM1–2. Every \(k\in\mathcal D\) is at most one, so (AM12) is at most (AM11). Conversely, for every compact \(K\) and \(0<\varepsilon<1\), the density \((1-\varepsilon)1_K\) belongs to \(\mathcal D\). Thus (AM12) is at least \((1-\varepsilon)\int_K\omega(\theta_\chi(X))\,d\chi\). First let \(\varepsilon\downarrow0\) for this compact set, then take the supremum over all \(K\). This proves

<a id="equation-am13"></a>

\[
                  A(X)=T(X)\quad(X\in N_+). \tag{AM13}
\]
Every comparison is a comparison of extended nonnegative numbers. In particular an infinite supremum is retained; no density, core, or finite-value uniqueness shortcut is used. EP1–4 transport this equality faithfully into \(\widehat{\pi(M)}_+\), where GDA5 has already located the whole value of \(T\). GDA6 supplies faithfulness, normality and semifiniteness, and GDA8–9 supplies full scalar composition and normalized two-weight comparison. These conclusions do not supply an arbitrary-cocycle realization theorem or invariant-weight recognition.

The analytic context is Haagerup, [*On the dual weights for crossed products of von Neumann algebras II*](https://journals.msp.org/mscand/article/view/1878), Math. Scand. 43 (1978), Theorem 1.1, together with the general Schur/minorant construction proved in GDA. The present proof identifies its strict minorants with actual Fourier densities before taking the whole extended supremum. It imports no external theorem in place of the cited programme bodies.
