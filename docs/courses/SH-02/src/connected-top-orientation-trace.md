# The top orientation class on a connected manifold

*Written by GPT-6.1 Sol (OpenAI). Self-checked by the writing AI. CC0 1.0.*

<a id="SH02-MD-CONNECTED-TOP"></a>

## The actual top-degree trace

Let \(X\) be a nonempty connected Hausdorff real manifold of finite dimension \(n\geq0\), without boundary and countable at infinity. The coefficient field is \(\mathbb C\). Let \(o_X\) be its complexified integral orientation sign line and \(\omega_X=o_X[n]\). The actual exceptional counit for \(a:X\to\{\mathrm{pt}\}\) gives an isomorphism

\[
\int_X:H_c^n(X;o_X)\xrightarrow{\sim}\mathbb C.
\tag{TOP1}
\]

Compactness and orientability are not required. In particular the coefficient line in TOP1 cannot be replaced by the constant sheaf without an orientation trivialization.

Put \(C=R\Gamma_c(X;\omega_X)\), and write \(\tau:C\to\mathbb C\) for the counit. The finite manifold compact-support bound makes \(C\) bounded. The actual internal exceptional adjunction gives

\[
\begin{gathered}
R\operatorname{Hom}_{\mathbb C}(C,\mathbb C)\\
\simeq R\Gamma\bigl(X;R\mathcal Hom(\omega_X,\omega_X)\bigr)\\
\simeq R\Gamma(X;\mathbb C_X).
\end{gathered}
\tag{TOP2}
\]

The last identification uses the specified tensor inverse of the shifted sign line. It sends the identity endomorphism to the constant section \(1\); it is not an identification of an arbitrary sheaf with its double dual.

<a id="TOP-DUAL"></a>

Under TOP2 the dual of \(\tau\) sends a scalar \(\lambda\) to \(\lambda\operatorname{id}_{\omega_X}\), hence to its constant section. This is exactly the identity-transpose normalization of EX.21. On degree-zero cohomology the map is therefore

\[
\begin{gathered}
\mathbb C\longrightarrow\operatorname{Hom}_{\mathbb C}(H^0(C),\mathbb C)\\
\simeq\Gamma(X;\mathbb C_X)=\mathbb C,\\
\lambda\longmapsto\lambda.
\end{gathered}
\tag{TOP3}
\]

Here algebraic dual is exact over the field, so degree-zero derived dual equals the dual of \(H^0(C)\). Connectedness and nonemptiness give the final constant-section equality. Thus the algebraic dual of \(H^0(\tau)\) is an isomorphism. Algebraic dual over a field detects isomorphisms even for infinite-dimensional vector spaces: apply the exact dual to the kernel and cokernel, and use that every nonzero vector space admits a nonzero linear functional. No finite-dimensionality assumption on cohomology is needed. Consequently \(H^0(\tau)\) is an isomorphism. Since \(H^0(C)=H_c^n(X;o_X)\), this is TOP1.

This argument uses connectedness only in degree zero. It does not assert that \(R\Gamma(X;\mathbb C_X)\) has no higher cohomology or that the entire derived trace \(C\to\mathbb C\) is invertible. A connected sphere, for example, has higher ordinary cohomology. For \(n=0\), a nonempty connected manifold is a point and TOP1 is the identity.

If \(X\) is smooth, the twisted de Rham resolution identifies TOP1 with integration of compactly supported top densities. MD M37 fixes its sign: on an increasing interval the endpoint class \((0,1)\) is represented by \(du\) with integral \(1\); ordered exterior products give the coordinate-ball generator with integral \(1\). Stokes's theorem makes exact compactly supported forms integrate to zero. A finite partition of unity on the compact support reduces arbitrary densities to chart-supported ones, while both trace and analytic integration commute with open extension. Thus analytic integration equals the actual trace and is nonzero, including on nonorientable smooth manifolds. Smoothness is needed only for this analytic interpretation.

[Manifold orientation, duality and trace](../../sheaf-proof-readings/SH02-manifold-duality.html#SH02-MD-TRACE) supplies the orientation object, trace and its positive interval normalization. [Exceptional inverse image and internal adjunction](../../sheaf-proof-readings/SH02-exceptional-operations.html#SH02-EX-INTERNAL) supplies the actual dual-sections map. The constant-section identity in [the manifold trace test](../../sheaf-proof-readings/SH02-manifold-duality.html#SH02-MD-ACYCLIC-SUBMERSION) gives TOP3. Those prerequisite lessons retain the human mathematical antecedents and their precise source locators. The argument above gives the connected top-degree consequence in full.
