# Integral homology and Picard–Lefschetz transvections

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The cyclic cover \(C_m\to E\) of degree \(m\) carries an action of its deck group \(\Gamma_m=\mu_m\). This lesson shows that its first integral homology is free of rank two over the integral group ring \(\mathbb Z[\Gamma_m]\), by cutting the torus along a slit and gluing \(m\) copies. The same basis is then followed into the nodal degeneration of the previous lesson, where the vanishing cycles are differences of adjacent sheets. The Picard–Lefschetz formula turns them into two monodromy transformations whose off-diagonal entries are \(\pm(2-u-u^{-1})\), where \(u\) generates the deck group. Freeness over the group ring, rather than over the cyclotomic integers, is what later allows congruences at primes dividing \(m\); the two transformations later give residual irreducibility.

**Prerequisites.** [*Cyclic covers of an elliptic curve with two branch points*](cyclic-covers-of-an-elliptic-curve-with-two-branch-points.md) and [*Two degenerations and a Jacobian of compact type*](two-degenerations-and-a-jacobian-of-compact-type.md). From *Galois representations*: [*Galois representations of weight-two newforms*](course:LG-GAL/galois-representations-of-weight-two-newforms), Lemma 2.0 (the period uniformization of the Jacobian of a complex curve and its naturality). From *The Lefschetz trace formula*: [*Lefschetz pencils and vanishing cycles*](course:AG-LTF/lefschetz-pencils-and-vanishing-cycles), Proposition PL.C (the local variation at a node).

**Conventions.** In this lesson everything is over \(\mathbb C\). The curve \(E(\mathbb C)\) is identified with \(\mathbb C/(\mathbb Za+\mathbb Zb)\) for an oriented period basis \(a,b\), and the underlying torus with \((\mathbb R/\mathbb Z)^2\), with \(a\) horizontal and \(b\) vertical. We write \(\Gamma_m=\mu_m\) and let \(u\) be the deck transformation \((Z,Y)\mapsto(Z,e^{2\pi i/m}Y)\), a generator of \(\Gamma_m\). Throughout, \(\mathbb Z[\Gamma_m]\) is the *group ring*, free of rank \(m\) over \(\mathbb Z\), not the ring of cyclotomic integers. Intersection numbers \(\langle\ ,\ \rangle\) on the first homology of a closed oriented surface are taken with the complex orientation.

## 1. Homology and Tate modules

The course defines \(H^1\) of a curve through the Tate module of its Jacobian. Over \(\mathbb C\) this is the integral homology of the Riemann surface.

**Proposition 1.1.** Let \(C\) be a smooth projective connected curve over a subfield \(F\) of \(\mathbb C\), with Jacobian \(J\), and let \(\Lambda=H_1(C(\mathbb C),\mathbb Z)\). For every prime \(\ell\) there are isomorphisms
\[
\begin{gathered}
T_\ell J\cong\Lambda\otimes\mathbb Z_\ell,\\
H^1(C,\mathbb Z_\ell)\cong\operatorname{Hom}(\Lambda,\mathbb Z)\otimes\mathbb Z_\ell,
\end{gathered}
\]
compatible with every automorphism \(\alpha\) of \(C\) defined over \(F\), acting by \(\alpha_*\) on \(T_\ell J\) and \(\Lambda\), and by \(\alpha^*\) on \(H^1(C,\mathbb Z_\ell)\) and \(\operatorname{Hom}(\Lambda,\mathbb Z)\).

**Proof.** By Lemma 2.0 of [*Galois representations of weight-two newforms*](course:LG-GAL/galois-representations-of-weight-two-newforms), \(J(\mathbb C)=\operatorname{Pic}^0(C(\mathbb C))\)\(=H^1(C,\mathcal O_C)/H^1(C(\mathbb C),\mathbb Z)\), naturally for pullback. For an automorphism \(\alpha\), the endomorphism \(\alpha_*\) of \(J\) (pushforward of divisors) equals the pullback \((\alpha^{-1})^*\). Poincaré duality \(H^1(C(\mathbb C),\mathbb Z)\cong\Lambda\) intertwines \((\alpha^{-1})^*\) with \(\alpha_*\), because \(\alpha\) is an orientation-preserving homeomorphism. Hence \(J[\ell^k](\mathbb C)\cong H^1(C(\mathbb C),\mathbb Z)/\ell^k\cong\Lambda/\ell^k\Lambda\), compatibly with \(\alpha_*\) and with the maps \(\ell\colon J[\ell^{k+1}]\to J[\ell^k]\). The group scheme \(J[\ell^k]\) is finite étale over \(F\), because \(\ell^k\) is invertible, so its points over \(\overline F\subset\mathbb C\) are all its complex points. Passing to the limit gives \(T_\ell J\cong\Lambda\otimes\mathbb Z_\ell\). Dualizing gives the second isomorphism; an automorphism acting by \(\alpha_*\) on \(\Lambda\) acts on the dual by \(x\mapsto x\circ\alpha_*\), which is \(\alpha^*\) in the convention of Lesson 1. \(\square\)

The isomorphisms are not Galois-equivariant; they only identify the underlying \(\mathbb Z_\ell[\operatorname{Aut}]\)-modules. That is all this lesson needs.

## 2. Cutting the torus along a slit

Consider the parameters
\[
R_s=\frac sn\,a,\qquad0<s<\tfrac12 .
\tag{2.1}
\]
The branch points of \(C_{m,R_s}\to E\) are \(\pm[n]R_s=\pm sa\). Let \(I_s\) be the horizontal arc from \(-sa\) to \(sa\) through \(O\); it has length \(2s<1\), so it does not close up. Each \(R_s\) lies in \(E^\circ\): the points \(O,\pm R_s,\pm sa\) are pairwise distinct for \(0<s<\frac12\), since \(n\ge3\).

**Lemma 2.1 (the slit model).** For every \(s\in(0,\frac12)\), the cover \(C_{m,R_s}\to E\) is trivial over \(E\setminus I_s\). It is obtained from \(m\) copies of \(E\) cut along \(I_s\) by gluing each bank of the cut on one sheet to the opposite bank on an adjacent sheet, cyclically. With a suitable indexing of the sheets by \(\mathbb Z/m\mathbb Z\), crossing the slit upwards raises the sheet index by \(1\).

**Proof.** First let \(s\) be small. Let \(D\) be a small closed disc around \(O\), containing \(I_s\). By Proposition 2.3 of the previous lesson, the family of covers degenerates at \(R=O\) to a curve whose part over \(E\setminus D\) consists of \(m\) disjoint copies of \(E\setminus D\), the components \(E_\zeta\). Over \((E\setminus\operatorname{int}D)\times N\), for a small neighbourhood \(N\) of \(O\) in the parameter curve, the model is a finite étale cover, hence a covering space, and it is trivial over the fibre \(R=O\); by the homotopy lifting property it is trivial over every fibre with \(R\in N\). The inclusion \(E\setminus\operatorname{int}D\hookrightarrow E\setminus I_s\) is a homotopy equivalence: both deformation retract onto the complement of a disc. So the unramified cover over \(E\setminus I_s\) is trivial for small \(s\). As \(s\) increases in \((0,\frac12)\), the slits \(I_s\) move by an isotopy of the torus, and the family of restricted covers over \(\{(Z,s):Z\notin I_s\}\) is a covering space over a space that retracts to any of its fibres, so triviality persists for all \(s\in(0,\frac12)\).

A small loop around \(sa\) crosses \(I_s\) exactly once, and the monodromy of the cover along it is a generator of \(\Gamma_m\), because \(f_{R_s}\) has a simple zero there. Index the sheets so that the monodromy of an upward crossing is \(u\); since \(u\) moves the sheet \(Y\) to \(e^{2\pi i/m}Y\), this is a cyclic indexing in which the crossing raises the index by \(1\). \(\square\)

On the sheet \(i\in\mathbb Z/m\mathbb Z\), let \(a_i\) be the horizontal loop at vertical coordinate \(\frac12\) and \(b_i\) the vertical loop at horizontal coordinate \(\frac12\). Both avoid the slit: \(I_s\) lies at vertical coordinate \(0\), and its horizontal extent \((-s,s)\) does not contain \(\frac12\). They meet in one point on their common sheet and not at all on different sheets, so with suitable orientations
\[
\begin{gathered}
\langle a_i,b_j\rangle=\delta_{ij},\\
\langle a_i,a_j\rangle=\langle b_i,b_j\rangle=0 .\quad(2.2)
\end{gathered}
\]
The deck transformation \(u\) maps sheet \(i\) to sheet \(i+1\), so \(u_*a_i=a_{i+1}\) and \(u_*b_i=b_{i+1}\).

## 3. A free module over the group ring

**Proposition 3.1.** The classes \(a_i,b_i\), \(i\in\mathbb Z/m\mathbb Z\), form a symplectic basis of \(H_1(C_{m,R_s},\mathbb Z)\). Consequently, for every \(t\in U(\mathbb C)\) and every \(R\in E^\circ(\mathbb C)\),
\[
\begin{gathered}
H_1(C_{m,t},\mathbb Z)\cong\mathbb Z[\Gamma_m]^2,\\
H^1(C_{m,t},\mathbb Z)\cong\mathbb Z[\Gamma_m]^2\quad(3.1)
\end{gathered}
\]
as \(\mathbb Z[\Gamma_m]\)-modules, and the same holds for \(C_{m,R}\).

**Proof.** The curve has genus \(m\), so \(H_1\) is free of rank \(2m\). By (2.2) the \(2m\) classes span a sublattice \(\Lambda'\) on which the intersection form has determinant \(1\). The intersection form on \(H_1\) is unimodular, by Poincaré duality. If \(\Lambda'\) had index \(d\) in \(H_1\), its determinant would be \(d^2\) times that of \(H_1\), so \(d^2=1\) and \(\Lambda'=H_1\). The elements \(a_0\) and \(b_0\) generate \(H_1\) freely over \(\mathbb Z[\Gamma_m]\), because \(u^ia_0=a_i\) and \(u^ib_0=b_i\). This gives the first isomorphism for \(C_{m,R_s}\).

For the cohomology, \(g\in\Gamma_m\) acts on \(\operatorname{Hom}(H_1,\mathbb Z)\) by pullback, \(\phi\mapsto\phi\circ g_*\). The coefficient-of-identity pairing
\[
\begin{gathered}
\mathbb Z[\Gamma_m]\times\mathbb Z[\Gamma_m]\longrightarrow\mathbb Z,\\
(x,y)\longmapsto\text{coefficient of }1\text{ in }xy,
\end{gathered}
\]
is perfect: the basis \(\{g\}\) has the dual basis \(\{g^{-1}\}\). The map \(y\mapsto\phi_y\), \(\phi_y(x)=\) coefficient of \(1\) in \(xy\), is therefore a bijection \(\mathbb Z[\Gamma_m]\to\operatorname{Hom}_{\mathbb Z}(\mathbb Z[\Gamma_m],\mathbb Z)\), and it is \(\Gamma_m\)-equivariant for the pullback action, because \(\phi_y(gx)=\phi_{gy}(x)\). So the dual of a free module of rank two is free of rank two, with no division by \(m\).

The families \(\mathcal C^E_m\to E^\circ\) and \(\mathcal C_m\to U\) are smooth and proper, so by Ehresmann's theorem the fibres form locally trivial fibre bundles over the connected manifolds \(E^\circ(\mathbb C)\) and \(U(\mathbb C)\), and the deck group acts fibrewise. Parallel transport along a path therefore gives \(\Gamma_m\)-equivariant isomorphisms between the homology of any two fibres. Proposition 6.1 of Lesson 2 identifies \(C_{m,t}\) with \(C_{m,R}\) for \(x(R)=t\), equivariantly. \(\square\)

**Corollary 3.2.** Let \(F\subset\mathbb C\) be a field containing \(\mu_m\) and \(t\in U(F)\). For every prime \(\ell\), including \(\ell\mid m\), the module \(H^1(C_{m,t},\mathbb Z_\ell)\) is free of rank two over \(\mathbb Z_\ell[\Gamma_m]\).

**Proof.** Combine Proposition 3.1 with Proposition 1.1. \(\square\)

**Remark 3.3.** The degeneration at the origin explains the integral statement as well. There the Jacobian specializes to \(\prod_{\zeta}E_\zeta\), on which \(\Gamma_m\) permutes the factors simply transitively (Corollary 2.6 of the previous lesson), so the integral homology of the special fibre is the regular module \(\mathbb Z[\Gamma_m]\otimes H_1(E,\mathbb Z)\), free of rank two. The slit model makes this concrete: the loops \(a_i,b_i\) on sheet \(i\) are the standard cycles of the factor \(E_{\zeta^i}\), carried to the nearby smooth fibres.

## 4. Vanishing cycles

Let \(s\) increase to \(\frac12\) in (2.1). The two branch points \(\pm sa\) approach \(Q=a/2\) from both sides, and the slit \(I_s\) fills the horizontal circle except for a small gap around \(Q\). At \(s=\frac12\) the parameter is \(R_*=a/(2n)\), the second degeneration of the previous lesson. Choose a small disc \(\Delta\) around \(Q\) containing both branch points. Its boundary circle \(\partial\Delta\) avoids the branch points and has \(m\) closed lifts \(\delta_0,\ldots,\delta_{m-1}\) to \(C_{m,R_s}\): the total monodromy of the cover around \(\partial\Delta\) is trivial, since the branch points carry inverse monodromies. By Lemma 3.1 of the previous lesson, these \(m\) circles are the neck circles of the \(m\) nodes of the fibre over \(R_*\): they are the vanishing cycles.

**Lemma 4.1.** The lifts can be numbered \(\delta_i\), \(i\in\mathbb Z/m\mathbb Z\), so that
\[
\begin{gathered}
[\delta_i]=\epsilon\,(a_i-a_{i+1}),\\
i\in\mathbb Z/m\mathbb Z,\quad(4.1)
\end{gathered}
\]
with one sign \(\epsilon\in\{1,-1\}\) for all \(i\).

**Proof.** Arrange \(\partial\Delta\) to cross the horizontal line of the slit once to the left of \(Q\) and once to the right, both times inside \(I_s\); this is possible because \(\Delta\) contains both branch points, which lie at distance less than the radius from \(Q\). The slit divides \(\partial\Delta\) into an upper arc and a lower arc. A lift of \(\partial\Delta\) runs along the lower arc on some sheet \(i\); crossing the slit upwards, it continues along the upper arc on sheet \(i+1\), by Lemma 2.1, and crossing back downwards it returns to sheet \(i\). Call this lift \(\delta_i\).

The circle \(\partial\Delta\) is small and lies near vertical coordinate \(0\), so it is disjoint from the loops \(a_j\) at vertical coordinate \(\frac12\). It meets the vertical line at horizontal coordinate \(\frac12\), the line through \(Q\), twice: once on the upper arc and once on the lower arc, crossing it in opposite directions. So \(\delta_i\) meets \(b_i\) once and \(b_{i+1}\) once, with opposite signs, and meets no other \(b_j\) and no \(a_j\). In the symplectic basis of Proposition 3.1, a class \(\gamma\) with \(\langle\gamma,a_j\rangle=0\) for all \(j\) equals \(\sum_j\langle\gamma,b_j\rangle a_j\), by (2.2). Hence \([\delta_i]=\epsilon(a_i-a_{i+1})\), where \(\epsilon=\pm1\) is the intersection sign of the lower arc with \(b_i\), the same for all \(i\). \(\square\)

Only the set of classes \(\pm[\delta_i]\) enters the Picard–Lefschetz formula below, and it is symmetric under \(i\mapsto-i\); so the direction in which the sheets are numbered plays no role.

## 5. The two transvections

**Theorem 5.1.** In the integral basis \(a_i,b_i\) of Proposition 3.1, the monodromy group of the family \(\mathcal C^E_m\to E^\circ\) on \(H_1(C_{m,R_s},\mathbb Z)\) contains transformations \(T_a\) and \(T_b\) with
\[
\begin{array}{r}
\begin{aligned}
T_a(a_j)&=a_j,\\
T_a(b_j)&=b_j+\sigma_a(2a_j-a_{j-1}-a_{j+1}),\\
T_b(b_j)&=b_j,\\
T_b(a_j)&=a_j+\sigma_b(2b_j-b_{j-1}-b_{j+1}),
\end{aligned}\\
(5.1)
\end{array}
\]
for all \(j\), where \(\sigma_a,\sigma_b\in\{1,-1\}\) do not depend on \(j\). Equivalently, in the basis \(a_0,b_0\) of the free \(\mathbb Z[\Gamma_m]\)-module, the off-diagonal entries of \(T_a\) and \(T_b\) are \(\sigma_a(2-u-u^{-1})\) and \(\sigma_b(2-u-u^{-1})\). The monodromy group of the family \(\mathcal C_m\to U\) contains the same transformations, under the identification of Proposition 6.1 of Lesson 2.

**Proof.** Let \(T_a\) be the monodromy along a small positively oriented loop in \(E^\circ\) around the parameter \(R_*=a/(2n)\), based at a parameter \(R_s\) with \(s\) close to \(\frac12\). By Lemma 3.1 of the previous lesson, the family near \(R_*\) has \(m\) nodes in its special fibre, each with local equation \(XU=-2nt\), and is smooth elsewhere. Away from small neighbourhoods of the nodes the family is a locally trivial bundle over a disc around \(R_*\) (Ehresmann's theorem for the proper submersion obtained by removing these neighbourhoods), so the monodromy is supported in the neighbourhoods of the nodes. Near each node, the smoothing parameter \(-2nt\) winds once around \(0\) as \(t\) does, so Proposition PL.C of [*Lefschetz pencils and vanishing cycles*](course:AG-LTF/lefschetz-pencils-and-vanishing-cycles), in relative dimension one, gives a local variation equal to one Dehn twist along the vanishing circle. The vanishing circles \(\delta_i\) are pairwise disjoint, so the local contributions commute and add, and
\[
T_a(\gamma)=\gamma+\sigma\sum_{i}\langle\gamma,\delta_i\rangle[\delta_i]\quad(5.2)
\]
with one sign \(\sigma\) fixed by the orientation conventions. By (4.1), \(\langle a_j,\delta_i\rangle=0\), so \(T_a(a_j)=a_j\), and
\[
\begin{aligned}
&\sum_i\langle b_j,\delta_i\rangle[\delta_i]\\
&\quad=\epsilon^2\bigl(-(a_j-a_{j+1})+(a_{j-1}-a_j)\bigr)\\
&\quad=-(2a_j-a_{j-1}-a_{j+1}),
\end{aligned}
\]
using \(\langle b_j,a_i-a_{i+1}\rangle=-\delta_{ij}+\delta_{i+1,j}\). This proves the formulas for \(T_a\) in (5.1) with \(\sigma_a=-\sigma\). In the group ring, \(T_a(b_0)=b_0+\sigma_a(2-u-u^{-1})a_0\).

Replacing the horizontal path (2.1) by the vertical path \(R_s=(s/n)b\), with a vertical slit through \(O\) and the collision at \(b/2\), gives the formulas for \(T_b\), at first in the basis built from the vertical slit. The loops \(a_i\) at vertical coordinate \(\frac12\) and \(b_i\) at horizontal coordinate \(\frac12\) avoid the vertical slit as well, and the vanishing classes are \(\pm(b_i-b_{i+1})\), by the proof of Lemma 4.1 with the roles of the coordinates exchanged.

It remains to see that the two bases are the same, which matters: two triangular matrices in unrelated bases would give no information about the group they generate. Choose the starting parameters \(\frac sn a\) and \(\frac sn b\) of the two paths very close to \(O\). Both slits then lie in a small disc \(D\) around \(O\), and both families of loops avoid \(D\). Over \((E\setminus\operatorname{int}D)\times N\), with \(N\) a small disc around \(O\) in the parameter curve, the cover is the trivial \(m\)-sheeted covering, as in the proof of Lemma 2.1, and its triviality extends across the parameter \(R=O\) itself. Label the sheets over this whole region once and for all. Parallel transport between the two starting parameters inside \(N\setminus\{O\}\) then carries the loops \(a_i,b_i\) of one model to the loops with the same labels in the other, independently of the path, because the labelling extends over \(R=O\). A different initial labelling changes all indices by the same cyclic shift, which leaves (5.1) unchanged.

Finally, the family \(\mathcal C^E_m\to E^\circ\) is the pullback of \(\mathcal C_m\to U\) along the finite étale double cover \(x\colon E^\circ\to U\) (Proposition 6.1 of Lesson 2), so every monodromy transformation of the first family is one of the second. Removing finitely many further points from \(U\) gives a surjection on fundamental groups and removes none of these transformations. \(\square\)

The element \(2-u-u^{-1}=-(u-1)^2u^{-1}\) is the cyclic second difference operator: it comes from the vanishing classes \(a_i-a_{i+1}\), each a difference of adjacent sheets. Lesson 7 evaluates it on the character spaces of the deck group.

## 6. Exercises

**6.1.** Let \(m=3\). Write the matrix of \(T_a\) on \(H_1(C_{3,R_s},\mathbb Z)\cong\mathbb Z^6\) in the basis \(a_0,a_1,a_2,b_0,b_1,b_2\), and check that it preserves the intersection form (2.2).

**6.2.** Show that the vanishing classes satisfy \(\sum_i[\delta_i]=0\), and explain this from the topology of the fibre over \(R_*\): the \(m\) neck circles together bound the preimage of a disc.

**6.3.** Let \(\chi\colon\Gamma_m\to\mathbb C^\times\) be a character with \(\chi(u)=\lambda\). On the two-dimensional \(\chi\)-eigenspace of \(H_1(C_{m,R_s},\mathbb C)\), spanned by the projections of \(a_0\) and \(b_0\), write \(T_a\) and \(T_b\) as \(2\times2\) matrices.

**6.4.** Show that for \(\lambda=1\) both matrices of Exercise 6.3 are the identity, and explain why: the trivial eigenspace is the pullback of \(H_1(E)\), on which the monodromy of the constant family is trivial.

## 7. Solutions

**6.1.** By (5.1), \(T_a\) fixes \(a_0,a_1,a_2\) and maps \(b_j\) to \(b_j+\sigma_a(2a_j-a_{j-1}-a_{j+1})\). With indices mod \(3\), \(a_{j-1}+a_{j+1}\) is the sum of the two other \(a\)'s. In block form \(T_a=\begin{pmatrix}I&\sigma_aM\\0&I\end{pmatrix}\) with
\[
M=\begin{pmatrix}2&-1&-1\\-1&2&-1\\-1&-1&2\end{pmatrix},
\]
whose columns are the coefficients of \(T_a(b_j)-b_j\). The intersection matrix in this basis is \(\Omega=\begin{pmatrix}0&I\\-I&0\end{pmatrix}\). The condition \(T_a^{\mathsf T}\Omega T_a=\Omega\) reduces to \(\sigma_a(M-M^{\mathsf T})=0\), which holds because \(M\) is symmetric.

**6.2.** \(\sum_i(a_i-a_{i+1})=0\) since the indices run over \(\mathbb Z/m\mathbb Z\). Topologically, the preimage of the disc \(\Delta\) is a connected surface (it contains the totally ramified points), whose oriented boundary is the union of the \(m\) circles \(\delta_i\); a boundary is null-homologous.

**6.3.** The projection onto the \(\chi\)-eigenspace sends \(a_i=u^ia_0\) to \(\lambda^i\bar a\) and \(b_i\) to \(\lambda^i\bar b\), where \(\bar a,\bar b\) are the projections of \(a_0,b_0\). Then \(T_a\bar b=\bar b+\sigma_a(2-\lambda-\lambda^{-1})\bar a\) and \(T_a\bar a=\bar a\), and similarly for \(T_b\). In the basis \(\bar a,\bar b\),
\[
\begin{gathered}
T_a=\begin{pmatrix}1&\sigma_ac_\lambda\\0&1\end{pmatrix},\quad
T_b=\begin{pmatrix}1&0\\\sigma_bc_\lambda&1\end{pmatrix},\\
c_\lambda=2-\lambda-\lambda^{-1}.
\end{gathered}
\]

**6.4.** For \(\lambda=1\), \(c_\lambda=0\). The \(\Gamma_m\)-invariant part of \(H_1(C_m,\mathbb Q)\) maps isomorphically to \(H_1(E,\mathbb Q)\) under the projection to \(E\). In the constant family the base curve \(E\) does not move, so monodromy acts trivially on \(H_1(E)\), and therefore on the invariant part.

## Sources

- [OpenAI-030] OpenAI, *Modularity of elliptic curves over imaginary quadratic fields*, OpenAI Math Release preprint, 4 October 2026, Section 4 (integral homology and explicit monodromy). https://github.com/openai/math/tree/main/preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026
