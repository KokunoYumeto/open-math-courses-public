# Exact module and branch-point maps

The short exact sequence of abelian groups

\[
0\longrightarrow\mathbb Z/2
\xrightarrow{\,[a]\mapsto[2a]\,}\mathbb Z/4
\xrightarrow{\,[b]\mapsto[b]\,}\mathbb Z/2
\longrightarrow0
\tag{WC20}
\]

does not split. Indeed a section would send the nonzero element of \(\mathbb Z/2\) to an odd class in \(\mathbb Z/4\), whereas both odd classes have order four. Its quotient is nonzero and its middle module is nonzero. This is an algebraic calibration of WC14; no claim is made that this particular extension is a specified geometric Morse pair.

For a geometric check, take \(M=\bigoplus_{j\ge1}\mathbb Z/2\), the constant sheaf \(M_{\mathbb C}\), and \(h(z)=z^2\). The nearby fibre at \(w=1/16\) consists of \(z=\pm1/4\). Its actual specialization and cone are

\[
\begin{gathered}
M\xrightarrow{\,m\mapsto(m,m)\,}M\oplus M,\\
\Phi_h(M_{\mathbb C})_0\simeq M,\qquad
[(a,b)]\longmapsto b-a.
\end{gathered}
\tag{WC21}
\]

The diagonal is injective, and the displayed difference identifies its cokernel with \(M\), so the cone has only degree-zero cohomology. A loop in the value exchanges the roots and induces \(-1\) on that cokernel; here \(-1=1\). The stalk module is not finitely generated and is not perfect over \(\mathbb Z\). The conclusion nevertheless follows from the same unit and cone. For the perverse normalization \(M_{\mathbb C}[1]\), the supported half-plane object is \(M\) in degree zero, in agreement with WC11 and WC14.

Under the finite map \(f(z)=z^2\), the pushforward of \(M_{\mathbb C}\) is locally constant away from zero. The same nonzero vanishing-cycle calculation in every rotated target direction gives the full cotangent fibre at zero, in addition to the zero section. This verifies WC3 at a branch point with coefficients outside the earlier perfect-stalk class.


Proof locators: [WC14, WC20 and WC21](../weak-coefficients.html#WC7). The first panel is an algebraic example, not a claimed realization by a Morse pair. The second panel plots the real section of the complex map at the exact fibre value 1/16. Source, diagram and calculation: CC0 1.0.
