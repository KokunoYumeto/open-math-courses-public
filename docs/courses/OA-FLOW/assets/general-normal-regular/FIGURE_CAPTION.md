# What the two operator pictures prove

The upper panel illustrates NR4 of NORMAL_REGULAR_FOUNDATION_PACKET.md. It is a commuting-algebra schematic, not a finite-dimensional model or a dimension comparison. The Hilbert spaces and index set \(I\) can be arbitrary. The initial faithful normal representation on \(K\) is unitarily a reducing compression of the standard representation amplified on \(H^{(I)}\):
\[
 W:K\longrightarrow EH^{(I)},\qquad
 N=(M\otimes1_I)',\qquad E=\operatorname{diag}(q_i)\in N.
\]
The canonical cone vectors for the cyclic normal functionals construct \(W\), using current CR8 and MC1. The projection onto \(\overline{NEH^{(I)}}\) belongs to both \(N\) and \(N'\). It therefore equals \(z\otimes1_I\) for a central projection \(z\in M\). Since this projection contains \(E\), its complementary central projection is killed by the original faithful representation. Hence \(z=1\).

On \(L^2(G)\otimes H^{(I)}\), the constant algebra \(1\otimes N\) commutes with the regular coefficients and with translations. Thus an operator \(T\) in the amplified regular algebra which vanishes on \(\mathcal E=1\otimes E\) vanishes on the dense span \((1\otimes N)\mathcal E(L^2(G)\otimes H^{(I)})\). Therefore \(T=0\). This proves the faithfulness of compression. Full normality is proved separately in NR3–4 by vector-series tests and ST12; the image is the entire regular algebra by bounded density. The picture must not be read as asserting that two arbitrary faithful initial representations have a unitary between their original spaces.

The lower panel is an exact finite example explaining the map's C2.IMP qualification. Let \(G=\mathbb Z/2\), \(H=\{e\}\), and induce the one-dimensional representation of \(H\). On \(\mathbb C^2\) with the two cosets as the ordered basis, the nonidentity group element acts by
\[
 S=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
For a matrix \(T=\begin{pmatrix}a&b\\c&d\end{pmatrix}\), the equation \(TS=ST\) is exactly \(d=a,c=b\). Thus the group commutant is
\[
 \{S\}'=\{aI+bS:a,b\in\mathbb C\},
\]
of complex dimension two. The coset algebra acts by every diagonal matrix. In particular commutation with \(P=\operatorname{diag}(1,0)\) forces \(b=c=0\). Combining this with commutation with \(S\) leaves precisely \(T=aI\). The full system commutant is therefore one-dimensional, as is the intertwiner space of the original one-dimensional \(H\)-representation.

This calculation does not refute imprimitivity. It shows why its morphisms must preserve the coset multiplication action as well as the group action. Rieffel, [*Induced representations of C\*-algebras*](https://math.berkeley.edu/~rieffel/papers/rieffel-C-induced.pdf) (1974), Theorem 7.18, and Green, [*The local structure of twisted covariance algebras*](https://projecteuclid.org/euclid.acta/1485889984), Acta Math. 140 (1978), Theorem 6, provide context; neither is being substituted for the missing local inverse-module proof.

The new diagram and this explanation are CC0-1.0 to the extent of rights held. Run render_c2_foundation.py with Python and matplotlib. It writes PNG, deterministic SVG and the exact diagram data beside this caption. The renderer uses fixed coordinates, a stable SVG hash salt, no SVG Date metadata, UTF-8 and LF newlines.
