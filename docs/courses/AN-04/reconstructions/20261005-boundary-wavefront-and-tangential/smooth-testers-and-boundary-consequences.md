# Smooth testers and boundary wave-front consequences

Original source: AN03-U034, *Global boundary operators, compressed wave fronts, and normal extension*, written by Codex, September 2026, CC0. Current complete proof connections and clarifications: AN-04 course-writing task and OpenAI Codex, 5 October 2026, CC0. All original mathematical displays in the selected sections remain unchanged.

Use \(D=-i\partial\), forward Fourier exponential \(e^{-ix\cdot\xi}\) and inverse factor \((2\pi)^{-n}\), on smooth Hausdorff second-countable manifolds with boundary and finite-rank bundles. The [global geometry](../20261005-global-boundary-operators/stretched-kernels-and-compressed-geometry.md) and [complete operator calculus](../20261005-global-boundary-operators/global-boundary-operator-calculus.md) prove (GL1)–(GL24), (GC1)–(GC14), (GA1)–(GA5), (GD13)–(GD14) and (GW1)–(GW5), including exact proper support, residual receiving and ordered elliptic parametrices. The [conormal test spaces](../20261005-conormal-test-foundations/conormal-amplitudes-and-test-spaces.md), dual distributions and intrinsic jets, and [full conormal intersection proof](../20261005-conormal-test-foundations/conormal-duality-implies-smoothness.md) supply (C1)–(C17), (GD1)–(GD12), and (SP1)–(SP15). A smooth boundary function is represented by its zero extension when paired with ambient supported distributions.

The exact [local boundary action](../20261005-local-boundary-calculus/boundary-tests-and-lacunary-symbols.md) and [distributional calculus](../20261005-local-boundary-calculus/boundary-adjoints-composition-and-distributions.md) supply all commutators, boundary jets and weak approximation, including distributions supported entirely on the boundary. The [ordinary wave-front proof](../20261004-free-intrinsic-graph/prerequisites/coordinate-and-wavefront-localization.md) and [conic parametrices](../20261004-free-intrinsic-graph/prerequisites/conic-parametrices-and-localization.md) give the interior and tangential boundary calculus. The [locally finite partition PS5](../20261004-free-intrinsic-graph/prerequisites/global-principal-symbol.md), [Fourier](../20261004-free-intrinsic-graph/prerequisites/fourier-l2.md), and [measure proofs](../20261004-free-intrinsic-graph/prerequisites/measure-and-l2.md) supply the remaining foundations. Source credit: the approved Hörmander III, 2007 eBook, ISBN 978-3-540-49938-1, Section 18.3. Its use and ordinary citation are valid; the mathematical arguments and exact prerequisites are included.

## Exact receiving results

This component retains Section 9, with its full local/global conormal distinction. The [compressed wave-front proof](compressed-wavefront-and-differential-action.md) gives (GW6)–(GW16) and the common finite-sum tester. The [normal and tangential companion](normal-extension-and-tangential-action.md) gives \(\mathcal N\), (GE21)–(GE26) and (GT1)–(GT15), including every topology estimate and the necessary pure-normal interior exception. The full intersection theorem (SP15) is proved in the earlier conormal-duality component; it is not inferred from conormality alone.

## 9. Smooth testers and boundary consequences

### 9.1. Smooth testers in the compressed definition

For \(u\in\mathcal A'(X)\), every properly supported
\(B\in\Psi_b^0\) satisfies \(Bu\in\mathcal A'\) by the
actual transpose action (GD13). Therefore (SP15) gives the
pointwise equivalence of admissible regularity tests
\[
 Bu\in\mathcal A(X)
       \quad\Longleftrightarrow\quad
 Bu\in C^\infty(X).
 \tag{SC1}
\]
Substituting *the same* family of operators and their unchanged
characteristic sets into the defining intersection (GW6)
yields the exact alternative definition
\[
 \operatorname{WF}_b(u)
   =\bigcap_{\substack{B\in\Psi_b^0\text{ proper}\\
                       Bu\in C^\infty(X)}}
                     \operatorname{Char}B
 \quad(u\in\mathcal A').
 \tag{SC2}
\]
No residual operator was asserted to produce a smooth
boundary function on an arbitrary supported distribution;
(SC1) uses both \(Bu\in\mathcal A'\) and the conormal
test result.

The finite cosphere argument (GW7) and (GW8) prove
\(\operatorname{WF}_b(u)=\varnothing\Rightarrow
u\in\mathcal A_{\mathrm{loc}}\) for any supported distribution.
If also \(u\in\mathcal A'\), compact smooth cutoffs preserve that
dual class by (GD13). Each cutoff output is in the original
\(\mathcal A\), so (SP15) makes it smooth. Cutoffs equal to one on
each compact neighborhood therefore prove the exact local comparison

\[
 \mathcal A'(X)\cap\mathcal A_{\mathrm{loc}}(X)
   =C^\infty(X)=\mathcal A'(X)\cap\mathcal A(X).
 \tag{SC2a}
\]

The reverse inclusion follows from (GD1)--(GD3), which place every
smooth boundary function in the single order \(m_0=-(n+2)/4\), with
local seminorm constants. Hence there is no global-order assumption
hidden in this smoothness conclusion. In particular,
\[
 \operatorname{WF}_b(u)=\varnothing,\quad u\in\mathcal A'
        \quad\Longrightarrow\quad u\in C^\infty(X).
 \tag{SC3}
\]
Conversely a smooth boundary function has its supported
representative in \(\mathcal A\) by (GD1)–(GD2), so the
identity operator is an order-zero tester with empty
characteristic set. Thus its compressed wave-front set is
empty. The implication and converse use the original
regularity class at the boundary, not interior-only
smoothness.

### 9.2. The boundary trace wave-front inclusion

Let \(g=u|_{\partial X}\) be the intrinsic trace (GD8) of
\(u\in\mathcal A'\), and let
\(q=(y',0,\eta',0)\) be a nonzero tangential boundary
compressed covector. Suppose \(q\notin\operatorname{WF}_b(u)\).
By the *definition* (GW6), some properly supported
\(B\in\Psi_b^0\) is elliptic at \(q\) and has
\(Bu\in\mathcal A\) on a neighborhood of \(y'\). Its
dual action remains in \(\mathcal A'\), so (SP15)
makes \(Bu\) smooth there. The original boundary jet
formula (GD14) at \(k=0\) gives the exact receiving map
\[
 (Bu)|_{\partial X}=B_0 g,
 \qquad
 \sigma_0(B_0)(y',\eta')
    =\sigma_0(B)(y',0,\eta',0).
 \tag{SC4}
\]
The first equality is initially (GL24) on smooth functions;
both sides are weakly continuous in \(u\) by (GD5),
(GD8), and (GD13), which proves it for the actual dual
distribution. The second equality retains the full
half-density comparison (GL18) and the original
\((2\pi)^{-(n-1)}\) tangential Fourier convention; no
normal factor has been set to one by a change of scale.

The ordinary boundary symbol in (SC4) is invertible at
\((y',\eta')\). Choose a conic cutoff \(\zeta\) there and
construct its ordered inverse symbol by
\(c_{-0}=\zeta\sigma_0(B_0)^{-1}\); at each lower order,
subtract the complete composition defect and multiply
on the correct side by that inverse. The asymptotic sum
gives a proper boundary operator \(C_0\) with
\(C_0B_0=\operatorname{Op}(\zeta)+R\), where \(R\)
is smoothing near \((y',\eta')\). Since \(B_0g\) is
smooth, the localized \(g\) is smooth there. This proves
\[
 \operatorname{WF}(u|_{\partial X})
   \subset
 \operatorname{WF}_b(u)|_{\partial X}
          \cap(T^*\partial X\setminus0).
 \tag{SC5}
\]
The boundary cotangent bundle is embedded by the exact
compressed anchor (GL8); pure normal compressed directions
have not been mistaken for trace covectors.

### 9.3. A tangential smooth tester for every regular boundary covector

Let \(u\in\mathcal N(X)\), and
\(q=(y',0,\eta',0)\ne0\) on the embedded boundary
cotangent bundle. If a properly supported tangential
operator \(B_b=b(x,D')\) is elliptic at
\((y',\eta')\) and \(B_bu\) is smooth on \(X\),
then its boundary wave-front set is empty. The exact
elliptic inclusion (GT14) immediately gives
\(q\notin\operatorname{WF}_b(u)\).

For the converse assume \(q\notin\operatorname{WF}_b(u)\).
Closedness of the boundary wave-front set on the compact
cosphere gives a small tangential base patch \(V\) about
\(y'\) and a conic tangential frequency patch \(\Gamma\)
about \(\eta'\) whose product closure misses
\(\operatorname{WF}_b(u)|_{\partial X}\). Choose an
order-zero tangential symbol \(b(x',t,\xi')\) supported
in that base and cone, with normal cutoff supported in a
small collar, equal to a nonzero scalar or the identity
matrix in a smaller patch about \((y',0,\eta')\), and
properly support its kernel. Its boundary symbol \(b_0\)
is elliptic at \(q\). By the full tangential theorem
(GT11)–(GT12), \(B_bu\in\mathcal N\) and
\[
 \operatorname{WF}_b(B_bu)|_{\partial X}
       \subset\operatorname{WF}_b(u)|_{\partial X}
                    \cap\Gamma=\varnothing
 \quad\text{on the chosen base patch}.
 \tag{SC6}
\]
The operator has output support in that base patch and
normal collar. If a sequence of interior wave-front points
of \(B_bu\) approached its compact boundary output set,
compactness of the cosphere would give a boundary
wave-front limit, contradicting (SC6). After shrinking
the normal cutoff once, the new operator is multiplication
of the old \(B_b\) on the left by a smooth \(t\)-cutoff
equal to one at zero; it remains tangential and elliptic at
\(q\). Its output has empty compressed
wave-front set throughout its support; outside that
support it is zero. The finite cover (GW7) therefore gives
\(B_bu\in\mathcal A\). As \(B_bu\in\mathcal A'\)
by (GT6), (SP15) gives \(B_bu\in C^\infty(X)\).
We have proved the exact equivalence
\[
 q\notin\operatorname{WF}_b(u)
 \quad\Longleftrightarrow\quad
 \exists\,B_b=b(x,D')\text{ proper, elliptic at }q,
             \ B_bu\in C^\infty(X).
 \tag{SC7}
\]
The existence assertion is coordinate independent: (GL10)
preserves the embedded tangential hyperplane, (GW6) is
intrinsic, and in either boundary chart the explicit
cutoff construction above supplies a tester. No assertion
of all-interior pseudolocality at pure normal covectors
is needed; the explicit exception in GT15 remains intact.

