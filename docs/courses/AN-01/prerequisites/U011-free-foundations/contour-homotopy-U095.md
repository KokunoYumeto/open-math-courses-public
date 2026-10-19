# A contour identity for holomorphic approximation

The following proof is the exact selection from AN-04, “Contour deformation and the complex Gaussian branch”, Section A2, through the cutoff discussion. Original supporting proof: GPT-6 Astra (OpenAI), Ultra, 5 October 2026, CC0.

Its finite determinant algebra uses the supplied [metric and calculus foundations](metric-foundation-bridges.md). Its integration step uses [Banach and integration foundations, Sections 15–16](banach-foundation-bridges.md). Both earlier programme proofs are included in this reader.

## Contour identity

The contour arguments need only the following identity on a fixed real box. Let \(Z(s,x)\in\mathbb C^d\) be smooth for \(0\le s\le1\), and let \(w(z,\bar z)\) be smooth. Write
\[
 c_j=\partial_{x_j}Z,\quad v=\partial_sZ,\quad
 D=\det(c_1,\ldots,c_d),\quad
 D_j=\det(c_1,\ldots,c_{j-1},v,c_{j+1},\ldots,c_d).
 \tag{A3}
\]
The real chain rule and the product rule for determinants give
\[
 \partial_s(w(Z)D)-\sum_j\partial_{x_j}(w(Z)D_j)
 =\sum_k w_{\bar z_k}(Z)
       \left(\bar v_kD-\sum_j\bar c_{j,k}D_j\right).
 \tag{A4}
\]
Here parameters not being integrated are held fixed.

For completeness, the derivatives of \(w\) in \(z\) cancel because
\(vD=\sum_jc_jD_j\). For an invertible column matrix this is Cramer's rule; after multiplication by the determinant it is a polynomial identity, so it holds at singular matrices too. The remaining determinant derivatives cancel because
\(\partial_sc_j=\partial_{x_j}v\) and
\(\partial_{x_j}c_k=\partial_{x_k}c_j\).
The term differentiating the inserted column in \(D_j\) cancels the corresponding term in \(\partial_sD\). Every term differentiating another column has a partner with the two affected columns interchanged and opposite determinant sign. This proves (A4) without an assumed Stokes theorem.

Integrate (A4) first in \(x\) and then in \(s\). The proved Fubini and fundamental theorems give the difference between the two oriented contour integrals, a lateral-boundary term, and the integral of its displayed right side. If \(w(Z)\) vanishes near the lateral boundary, that term is zero. If an auxiliary cutoff is inserted, its derivative has precisely the same boundary role and can be estimated on its transition support. The determinant is complex and oriented, never its absolute value.
