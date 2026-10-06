# The de Rham functor

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A connection gives a differential on forms with coefficients. Its horizontal sections are the first part of that complex, but a singular differential system can also contribute higher cohomology. The de Rham functor retains the whole complex. We compute it at a puncture, prove its compatibility with proper direct images, and distinguish the information retained by ordinary sheaves from the information lost at an irregular boundary.

Our algebraic varieties are smooth and separated, with pure dimension $d_X$, over a field of characteristic zero. Analytic assertions use $k=\mathbb C$. Modules are left $\mathcal D_X$-modules, quasi-coherent over $\mathcal O_X$. Write $\mathbb D_X$ for D-module duality and $\mathbf D_X$ for Verdier duality on $X^{an}$. The map operations have the conventions of Adjunctions, base change and the projection formula; their preservation of holonomicity was proved in Preservation of holonomicity and minimal extensions. Cohomological shifts satisfy $\mathcal H^q(K[r])=\mathcal H^{q+r}(K)$.

## 1. Two de Rham complexes and one normalization

For a module $M$, its unshifted algebraic complex is
\[
\operatorname{DR}^0_{alg,X}(M)=
\bigl[M\xrightarrow{\nabla}\Omega_X^1\otimes M
\longrightarrow\cdots\longrightarrow\Omega_X^{d_X}\otimes M\bigr],
\tag{1.1}
\]
in degrees $0,\ldots,d_X$. Tensor products here are over $\mathcal O_X$. For a local form $\alpha$,
\[
d_M(\alpha\otimes m)
=d\alpha\otimes m+\sum_a dx_a\wedge\alpha\otimes\partial_a m.
\tag{1.2}
\]
The Leibniz rule makes this well defined, and commuting coordinate derivatives give $d_M^2=0$. The intrinsic connection formula shows independence of coordinates. These differentials are $k$-linear, usually not $\mathcal O_X$-linear. Thus the complex is a complex of sheaves of $k$-vector spaces.

Set
\[
\operatorname{DR}_{alg,X}(M)=\operatorname{DR}^0_{alg,X}(M)[d_X].
\tag{1.3}
\]
For a bounded complex, take its total complex with the usual Koszul signs. Analytification is
\[
M^{an}=\mathcal D_{X^{an}}\otimes_{\iota^{-1}\mathcal D_X}\iota^{-1}M
\simeq \mathcal O_{X^{an}}\otimes_{\iota^{-1}\mathcal O_X}\iota^{-1}M.
\tag{1.4}
\]
It is exact: the analytic local rings are flat over the algebraic local rings, and the order filtration identifies the two descriptions. The *analytic* de Rham functor used below is
\[
\operatorname{DR}_X(M)
=\operatorname{DR}^0_{X^{an}}(M^{an})[d_X].
\tag{1.5}
\]
It takes values in complexes of sheaves of $\mathbb C$-vector spaces on the analytic topology.

**Proposition 1.1.** In either setting, with $\omega_X$ carrying its canonical right D-action,
\[
\operatorname{DR}_{alg,X}(M)\simeq
\omega_X\otimes_{\mathcal D_X}^{L}M.
\tag{1.6}
\]
The analogous formula holds analytically.

**Proof.** The right Spencer complex has terms $\Omega_X^p\otimes_{\mathcal O_X}\mathcal D_X$ in degree $p-d_X$, and augments to $\omega_X$ by its right action. In coordinates its differential is $(-1)^{d_X}$ times the expression (1.2), with $m$ replaced by $P\in\mathcal D_X$. This common sign fixes the shift convention in (1.3). It is right D-linear; for instance differentiating a coefficient moved between the two tensor factors gives the same Leibniz term.

Filter its degree-$p$ term by operators of order at most $a+p$. The associated graded differential is exterior multiplication by $\sum dx_a\,\xi_a$. This is the cochain Koszul complex for the regular sequence $\xi_1,\ldots,\xi_{d_X}$ in $\operatorname{Sym}T_X$. Its only augmented cohomology is the top exterior form with all $\xi_a$ set to zero. Exactness of the filtered complex follows by successively lowering the finite order of a representative; its filtration is bounded below in each term. Its terms are locally free right D-modules. Tensoring this resolution with $M$ gives exactly (1.1) with shift (1.3). The same symbol calculation works for holomorphic coefficients. $\square$

We normalize the contravariant solution functor as
\[
\operatorname{Sol}_X(M)=
R\mathcal Hom_{\mathcal D_{X^{an}}}(M^{an},\mathcal O_{X^{an}})[d_X].
\tag{1.7}
\]
For bounded D-coherent complexes,
\[
\operatorname{Sol}_X(M)\simeq\operatorname{DR}_X(\mathbb D_XM).
\tag{1.8}
\]
Here is the algebra behind the identity. Locally resolve $M$ by a bounded finite projective D-complex $P$. Put $Q=\mathcal Hom_{\mathcal D}(P,\mathcal D)$, a right D-complex. Duality is the left side change of $Q[d_X]$. The side-change identity
\[
\omega_X\otimes_{\mathcal D}^{L}
(\omega_X^{-1}\otimes_{\mathcal O} Q)
\simeq Q\otimes_{\mathcal D}^{L}\mathcal O_X
\]
is checked using the negative Lie-derivative action on $\omega_X$. Since $P$ is finite projective, the last tensor is $\mathcal Hom_{\mathcal D}(P,\mathcal O_X)$. This proves (1.8), including its shift. Finite projective resolutions and coherent biduality are the prerequisites established in *Holonomic D-modules and duality*. Flat analytification commutes with this calculation.

**Proposition 1.2, holomorphic Poincaré lemma.**
\[
\operatorname{DR}_X(\mathcal O_X)=\mathbb C_{X^{an}}[d_X].
\tag{1.9}
\]
More generally, for a finite flat bundle $E$ with horizontal local system $L$, $\operatorname{DR}_X(E)=L[d_X]$.

**Proof.** Work in a star-shaped coordinate polydisc centered at zero. For a holomorphic $p$-form with $p>0$, define
\[
(H\alpha)_z(v_1,\ldots,v_{p-1})
=\int_0^1 t^{p-1}\alpha_{tz}(z,v_1,\ldots,v_{p-1})\,dt.
\tag{1.10}
\]
Differentiation under the integral, or the identity for dilation and contraction by the radial vector field, gives $dH+Hd=1$ in positive degree. In degree zero it gives $Hd(f)=f-f(0)$. The integral is holomorphic, as follows either from uniformly convergent power series on smaller polydiscs or differentiation under the integral. Hence the only cohomology sheaf of the unshifted complex is the constant sheaf in degree zero. A flat bundle has a horizontal analytic frame by the local flat-connection theorem proved in *D-modules, flat connections and local systems*. In that frame its differential is $d\otimes1_L$, so the same homotopy proves the assertion. $\square$

## 2. Calculations at an ordinary puncture

Write $A=\mathbb C\langle x,\partial\rangle$, $\theta=x\partial$, and let $j:\mathbb C^*\hookrightarrow\mathbb C$. On the line the normalized de Rham complex is $[M\xrightarrow{\partial}M\,dx][1]$, with terms in degrees $-1,0$.

The point module $\delta_0=A/Ax$ has basis $1,\partial,\partial^2,\ldots$. Its analytic sheaf is supported at zero, where this basis still describes its finite normal derivatives. Multiplication by $\partial$ is injective and has one-dimensional cokernel. Therefore
\[
\operatorname{DR}_{\mathbb A^1}(\delta_0)=\mathbb C_0,
\tag{2.1}
\]
with no extra shift.

The algebraic direct image $j_*\mathcal O_{\mathbb G_m}$ is the Laurent module $L=\mathbb C[x,x^{-1}]$ with ordinary differentiation. Its analytification near zero is $\mathcal O^{an}(*0)$, consisting of holomorphic germs with a finite-order pole. If $g=\sum_{n\ge-N}a_nx^n$, differentiation kills precisely the constants; a meromorphic one-form has a meromorphic primitive precisely when its residue is zero. Dividing its other Laurent coefficients by $n+1$ preserves convergence and finite pole order. Thus its stalk de Rham cohomology is $\mathbb C$ in degrees $-1$ and $0$.

Restriction followed by the Poincaré quasi-isomorphism defines a comparison
\[
\operatorname{DR}_{\mathbb A^1}(L)\longrightarrow Rj_*\mathbb C_{\mathbb C^*}[1].
\tag{2.2}
\]
Off zero it is an isomorphism. At zero, a punctured disc retracts onto a circle, so the right side has the same two cohomology groups. The constant class maps to the constant class; the class of $dx/x$ maps to a nonzero circle class, with period $2\pi i$. Consequently (2.2) is a quasi-isomorphism. This proves this particular nonproper comparison directly.

Consider now
\[
Q_\lambda=A/A(\theta-\lambda).
\tag{2.3}
\]
Its connection off zero has $\partial e=\lambda x^{-1}e$. Horizontal sections are $x^{-\lambda}e$; the corresponding rank-one local system $L_\lambda$ has monodromy
\[
T_\lambda=e^{-2\pi i\lambda}.
\tag{2.4}
\]
Solutions of the *defining scalar equation* $\theta u=\lambda u$ instead have monodromy $e^{2\pi i\lambda}$. This is the contravariant solution convention.

Right multiplication by $\theta-\lambda$ gives a free D-resolution of $Q_\lambda$. Formal adjoint sends this operator to $-(\theta+\lambda+1)$. By (1.8), its analytic de Rham complex is consequently represented by
\[
\bigl[\mathcal O^{an}\xrightarrow{\theta+\lambda+1}\mathcal O^{an}\bigr][1].
\tag{2.5}
\]
On a convergent Taylor series the displayed operator multiplies $x^n$ by $n+\lambda+1$. If $-\lambda-1$ is not a nonnegative integer, every multiplier is nonzero, and their reciprocals grow at most polynomially; the inverse therefore preserves holomorphic germs. If $-\lambda-1=m\ge0$, both kernel and cokernel at zero are spanned by $x^m$. This determines the stalks, but we also determine the gluing:
\[
\operatorname{DR}(Q_\lambda)\simeq
\begin{cases}
j_!L_\lambda[1]\simeq Rj_*L_\lambda[1],
 &\lambda\notin\mathbb Z,\\
Rj_*\mathbb C_{\mathbb C^*}[1],
 &\lambda\in\mathbb Z_{<0},\\
j_!\mathbb C_{\mathbb C^*}[1],
 &\lambda\in\mathbb Z_{\ge0}.
\end{cases}
\tag{2.6}
\]
For the first case, punctured-disc cohomology is computed by $[\mathbb C\xrightarrow{T_\lambda-1}\mathbb C]$ and vanishes. Thus the natural $j_!\to Rj_*$ map is an isomorphism, and (2.5) identifies the extension by its zero stalk at the origin. For negative integral $\lambda$, the algebraic identification $Q_\lambda\simeq L$ from *Holonomic D-modules and duality* and (2.2) prove the second case. For nonnegative integral $\lambda$, (2.5) has zero origin stalk and the trivial local system elsewhere. The adjunction map from $j_!\mathbb C[1]$ is a quasi-isomorphism on every stalk, proving the third.

In particular, integral residues do not make all cyclic presentations the same module. $L=A/A(\partial x)$ and $J=A/A(x\partial)$ have different boundary extensions; their de Rham complexes are respectively the star and shriek extensions in (2.6).

## 3. Closed embeddings and proper direct images

**Proposition 3.1.** For a closed embedding $i:Z\hookrightarrow X$ and a bounded D-coherent complex $M$,
\[
\operatorname{DR}_X(i_*M)\simeq Ri_*\,\operatorname{DR}_Z(M).
\tag{3.1}
\]
The same assertion holds for the algebraic complexes as sheaves of $k$-vector spaces.

**Proof.** In adapted coordinates $(z,t_1,\ldots,t_c)$, the transfer description from *Kashiwara's equivalence and singular spaces* gives
\[
i_*M\simeq i_*\bigl(M\otimes_k k[u_1,\ldots,u_c]\bigr),
\qquad u_a=\partial_{t_a}.
\tag{3.2}
\]
Normal differentiation acts by multiplication by $u_a$, while the tangential differential is that of $M$. The normal de Rham factor is the Koszul cochain complex
\[
\bigl[k[u]\longrightarrow\cdots
\longrightarrow k[u]\,dt_1\wedge\cdots\wedge dt_c\bigr].
\]
Its cohomology is $k$ only in degree $c$: successively divide a polynomial by each variable $u_a$, or tensor the one-variable injective complexes with cokernel $k$. Total de Rham normalization shifts by $d_X=d_Z+c$, so the normal degree $c$ cancels, leaving the shift $d_Z$.

The surviving normal top form contracts with the conormal determinant in the transfer module. This is why the local quotient is canonically the complex on $Z$, rather than that complex tensored with a coordinate-dependent line. Coordinate changes respect the transfer action, this contraction and the Spencer differential, so the identifications glue. Closed sheaf pushforward is exact. The bounded totalization proves the result for complexes as well as modules. Holomorphic coefficients give the identical argument; (3.2) also shows that algebraic and analytic closed D-pushforward commute. $\square$

We use the following algebraic-geometry comparison prerequisite. For a proper complex algebraic morphism $h$ and a quasi-coherent sheaf $F$,
\[
(Rh_*F)^{an}\simeq Rh^{an}_*(F^{an}).
\tag{3.3}
\]
This is the quasi-coherent extension of relative GAGA, not just the comparison for finite flat bundles. A precise formulation is Liu, *Quasi-coherent GAGA*, Proposition 3.1. The coherent case is relative GAGA; the extension writes $F$ as a filtered union of coherent subsheaves and uses commutation of higher direct images with filtered colimits on the algebraic side and for proper analytic maps. We use these comparison and sheaf-cohomology prerequisites, rather than assuming a D-coherent module is $\mathcal O$-coherent.

**Lemma 3.2, comparison with proper support.** Let $p:W\to Y$ be an algebraic morphism and $S\subset W$ a closed subset proper over $Y$. For a quasi-coherent $F$ supported on $S$, (3.3) holds with $p$ in place of $h$.

**Proof.** Write $F=\varinjlim F_a$ with $F_a$ coherent. On the noetherian, quasi-compact scheme $W$, a power of the ideal of $S$ annihilates each $F_a$, since its support lies in $S$. Thus each is a coherent sheaf on a finite thickening of $S$, still proper over $Y$. Relative GAGA applies there. Algebraic higher pushforward commutes with this union by a finite affine Čech computation.

On the analytic side all the underlying sheaves have support in the same proper closed set. Identify them with their closed pushforwards from $S^{an}$ as sheaves of abelian groups. Higher direct image on that support commutes with filtered colimits for a proper map: proper base change reduces the claim stalkwise to cohomology on a compact fiber, where finite covers and their refinements compute the filtered-colimit comparison. Applying this to $F_a^{an}$, and using exact analytification, identifies the colimits of the coherent GAGA isomorphisms with the claimed isomorphism. Bounded cohomological dimension gives the corresponding derived assertion. $\square$

**Theorem 3.3.** For a proper morphism $f:X\to Y$ of smooth separated complex algebraic varieties and $M\in D^b_{\mathrm{coh}}(\mathcal D_X)$,
\[
\operatorname{DR}_Y(f_*M)\simeq
Rf^{an}_*\,\operatorname{DR}_X(M).
\tag{3.4}
\]
In particular this holds for all holonomic complexes, without regularity.

**Proof.** Factor $f$ as its closed graph $\gamma:X\hookrightarrow X\times Y$ followed by the projection $p:X\times Y\to Y$, and put $N=\gamma_*M$. The graph is proper over $Y$ because $f$ is proper. Composition of D-direct images identifies $f_*M=p_*N$.

First, relative Spencer gives
\[
p_*N=Rp_*\bigl[\Omega_X^\bullet\boxtimes\mathcal O_Y
\otimes_{\mathcal O_{X\times Y}}N\bigr][d_X].
\tag{3.5}
\]
Every term is quasi-coherent and has support in the graph. Lemma 3.2 applies term by term. Its comparisons commute with the relative differential: the latter is a finite-order differential operator over the base, obtained from the algebraic D-action by the Leibniz rule, and analytic extension gives exactly that same operator on analytic coefficients. Equivalently, factor each such operator through its finite principal-parts sheaf, whose formation commutes with analytification. Resolve pushforward, filter the finite relative complex by degree, and compare its terms; the resulting morphism of spectral sequences proves
\[
(p_*N)^{an}\simeq p^{an}_*(N^{an})
\tag{3.6}
\]
as D-complexes. Horizontal vector fields also commute with the comparison, so this is a comparison of D-actions, not only vector spaces.

Second, on $X^{an}\times Y^{an}$, absolute forms split into horizontal and vertical forms. The absolute de Rham differential is the total differential of the corresponding double complex: commuting X- and Y-vector fields give the anticommutation after the Koszul sign. Applying the Y-de Rham functor to the analytic version of (3.5) therefore gives
\[
\operatorname{DR}_{Y^{an}}(p^{an}_*N^{an})
\simeq Rp^{an}_*\operatorname{DR}_{X^{an}\times Y^{an}}(N^{an}).
\tag{3.7}
\]
To check the derived exchange explicitly, trivialize the finitely many locally free bundles $\Omega_Y^a$ on a coordinate open set and move their finite tensor factors through $Rp^{an}_*$. Take an acyclic resolution for pushforward and totalize. The horizontal derivative on that resolution is induced by the Y-action in (3.5); its differential is the horizontal part of the absolute connection. The total shift is $d_X+d_Y$, precisely the absolute de Rham normalization. This proves (3.7) and its compatibility on overlaps.

Finally (3.1) and the closed analytification comparison give
\[
Rp^{an}_*\operatorname{DR}(N^{an})
\simeq Rp^{an}_*R\gamma^{an}_*\operatorname{DR}_X(M)
=Rf^{an}_*\operatorname{DR}_X(M).
\]
Combine this with (3.6) and (3.7). Bounded complexes follow by finite truncation triangles. Proper coherence of $f_*M$, used to stay in the D-coherent category, is the theorem recorded in the preceding adjunction lesson. The argument itself never factors a general proper morphism through projective space. $\square$

This is the de Rham form of the comparison between algebraic and analytic direct images along a proper map. Properness is used in the comparison (3.6). Analytic direct image along a nonproper map can contain holomorphic functions with essential singularities which are absent from the analytification of algebraic direct image.

## 4. Constructibility, perversity and the limits of compatibility

The analytic theorems used here have the following exact form.

**Kashiwara's constructibility and perversity theorem, stated.** If $M$ is holonomic on a complex manifold of dimension $d$, then $R\mathcal Hom_{\mathcal D}(M,\mathcal O)[d]$ is a constructible perverse complex. See M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §§9.2 and 9.5. For algebraic holonomic modules their analytic de Rham and solution complexes are constructible with respect to an algebraic stratification. Exact holonomic duality and (1.8) give
\[
\operatorname{DR}_X(M)\in\operatorname{Perv}(X^{an}).
\tag{4.1}
\]
This is an assertion for a module in degree zero. A bounded complex with holonomic cohomology has a bounded constructible de Rham complex, and its standard module cohomology corresponds to perverse cohomology by truncation triangles.

Recall the middle-perversity conditions from The perverse t-structure. On a smooth complex stratum $S$ of dimension $s$, a perverse complex $K$ satisfies
\[
\mathcal H^q(i_S^*K)=0\quad(q>-s),\qquad
\mathcal H^q(i_S^!K)=0\quad(q<-s).
\tag{4.2}
\]
For instance, on the line $\mathbb C[1]$ has a point stalk in degree $-1$ and point costalk $\mathbb C[-1]$ in degree $1$; both inequalities hold. The point sheaf $\mathbb C_0$ has stalk and costalk in degree zero. These explain why (1.9) and (2.1) use different shifts.

**Duality compatibility, stated.** For $M\in D^b_h(\mathcal D_X)$,
\[
\operatorname{DR}_X(\mathbb D_XM)
\simeq \mathbf D_X\operatorname{DR}_X(M).
\tag{4.3}
\]
For this statement see V. Ginzburg, [*Lectures on D-modules*](https://math.berkeley.edu/~nadler/ginzburg.dmodules.pdf), on duality for holonomic modules. Here $\mathbf D_XK=R\mathcal Hom_{\mathbb C}(K,\mathbb C[2d_X])$ uses the canonical complex orientation. Verdier duality is developed in [Microlocal sheaves](https://kokunoyumeto.github.io/open-math-courses-public/courses/SH-02/).

**Inverse-image compatibility, stated with its hypothesis.** For every morphism of smooth algebraic varieties and every *regular holonomic* complex $N$,
\[
\operatorname{DR}_X(f^!N)
\simeq (f^{an})^!\operatorname{DR}_Y(N).
\tag{4.4}
\]
This is part of the Riemann–Hilbert correspondence for regular holonomic complexes, which gives both direct-image and both inverse-image comparisons; see M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §9.2. For an arbitrary coherent module with non-characteristic $f$, Cauchy–Kowalevski–Kashiwara gives the more restricted comparison
\[
\operatorname{DR}_X(Lf^*N)
\simeq (f^{an})^{-1}\operatorname{DR}_Y(N)[d_X-d_Y].
\tag{4.5}
\]
See Proposition 4.7.6 and Kashiwara–Schapira, Theorem 11.3.5, the latter expressed using unshifted solutions. Since $f^!=Lf^*[d_X-d_Y]$, (4.5) has total shift $2(d_X-d_Y)$ when written for $f^!$. For smooth $f$ this matches the oriented real relative dimension in sheaf $f^!$. Formula (4.4) at an arbitrary characteristic embedding cannot be inferred from (4.5) by dropping non-characteristicness.

Regular singularities and the full Riemann–Hilbert correspondence are the subjects of the next two lessons. The analytic constructibility proof belongs to analytic sheaf theory, specifically Kashiwara–Schapira, Chapter XI. None of these stated analytic theorems is substituted for the proper direct-image proof in Section 3.

## 5. Algebraic cohomology and an exponential warning

Algebraic de Rham cohomology has its unshifted convention
\[
H^q_{dR}(X/k)=
\mathbb H^q(X,\Omega_X^\bullet).
\tag{5.1}
\]
See [Stacks, Tag 0FL6](https://stacks.math.columbia.edu/tag/0FL6); on an affine scheme it is the cohomology of global algebraic forms [Stacks, Tag 0FLW]. Thus
\[
H^qR\Gamma(X,\operatorname{DR}_{alg,X}(\mathcal O_X))
=H^{q+d_X}_{dR}(X/k).
\tag{5.2}
\]

**Grothendieck's algebraic de Rham comparison, stated.** For smooth separated $X$ of finite type over $\mathbb C$, the natural analytic comparison induces functorial isomorphisms
\[
H^q_{dR}(X/\mathbb C)\simeq
H^q(X^{an},\mathbb C).
\tag{5.3}
\]
See Grothendieck, *On the de Rham cohomology of algebraic varieties*, Theorems 1 and 1′, pp. 95–96. The affine assertion is Theorem 1; Theorem 1′ states the hypercohomology form. For proper smooth $X$, (5.3) follows already from coherent GAGA on the finitely many form bundles and Proposition 1.2. The general nonproper comparison is the additional theorem.

It concerns $\mathcal O_X$ with its trivial connection. It does not say that arbitrary irregular coefficients have the same algebraic and analytic cohomology. Let
\[
E=\mathcal O_{\mathbb A^1}e,\qquad \partial e=e.
\tag{5.4}
\]
Thus the coefficient differential is $g\mapsto g'+g$. The everywhere nonzero holomorphic section $e^{-x}e$ is horizontal, giving
\[
\operatorname{DR}_{\mathbb A^1}(E)=\mathbb C_{\mathbb C}[1].
\tag{5.5}
\]
Algebraically, $1+\partial$ is bijective on $\mathbb C[x]$, with inverse on each polynomial given by the finite sum $\sum_{a\ge0}(-\partial)^a$. Hence its algebraic de Rham cohomology is zero in every degree.

In particular, for $p:\mathbb A^1\to\mathrm{pt}$,
\[
\operatorname{DR}_{\mathrm{pt}}(p_*E)=0,\qquad
Rp^{an}_*\operatorname{DR}_{\mathbb A^1}(E)=\mathbb C[1].
\tag{5.6}
\]
This is an explicit failure of nonproper direct-image compatibility on all holonomic modules. $E$ is an algebraic flat bundle and is holonomic. At infinity, with $y=1/x$, its connection coefficient is $-dy/y^2$, an irregular pole. Ordinary de Rham sheaves on the affine line do not record that boundary behavior.

## 6. Exercises

**Exercise 12.1, easy.** Compute $H^*_{dR}(\mathbb G_m)$ using algebraic forms, including a representative of its nonzero degree-one class.

**Exercise 12.2, easy.** Compute $\operatorname{DR}(\delta_0)$ on $\mathbb A^n$ and explain why its degree does not depend on $n$.

**Exercise 12.3, medium.** Prove (2.2) by a stalk calculation, and explain why agreement of dimensions alone would be insufficient.

**Exercise 12.4, medium.** Determine the analytic de Rham complex of $Q_\lambda$ for every complex $\lambda$, including the sign of its monodromy and the distinction between negative and nonnegative integral parameters.

**Exercise 12.5, hard.** Prove that $E$ in (5.4) and $\mathcal O_{\mathbb A^1}$ are nonisomorphic algebraic D-modules with isomorphic de Rham complexes. Determine the algebraic Hom spaces in both directions and deduce that de Rham is not fully faithful on all holonomic modules.

## 7. Solutions

**12.1.** Affine acyclicity reduces the answer to
\[
\mathbb C[x,x^{-1}]\xrightarrow{d}
\mathbb C[x,x^{-1}]\,dx.
\]
Here $d(x^m)=m x^{m-1}dx$. The kernel consists of constants, and every monomial one-form is a derivative except $x^{-1}dx$. Consequently $H^0=\mathbb C$, $H^1=\mathbb C[dx/x]$, and all other groups vanish. Under (5.3), $(2\pi i)^{-1}dx/x$ has circle period one.

**12.2.** The normal PBW basis identifies $\delta_0$ with $\mathbb C[u_1,\ldots,u_n]$, where $\partial_a$ acts as $u_a$. Its unshifted de Rham complex is the Koszul cochain complex for the sequence $u_1,\ldots,u_n$. Each one-variable factor has zero kernel and cokernel $\mathbb C$ in degree one. Tensoring these exact calculations over a field gives only top cohomology $\mathbb C$ in degree $n$. The normalization $[n]$ puts it in degree zero. Its support is the origin, so the result is the point sheaf $\mathbb C_0$. This also follows by (3.1) from de Rham on a point.

**12.3.** Near zero the analytic algebraic direct image consists of meromorphic germs with finite principal part, not arbitrary punctured-disc holomorphic germs. For a Laurent series, termwise integration converges for every nonresidue term and retains a finite principal part. Thus the de Rham kernel is constants and the cokernel is residue. The restriction comparison to punctured-disc cohomology sends $1$ to $1$ and $dx/x$ to a class whose period is $2\pi i$. Both induced maps are isomorphisms. Off zero the comparison is the Poincaré quasi-isomorphism, so it is a quasi-isomorphism everywhere. Two arbitrary complexes with stalk cohomology of equal dimension need not have the same restriction maps or gluing; the explicitly nonzero residue comparison supplies the required morphism.

**12.4.** Resolve by right multiplication with $\theta-\lambda$. Its formal adjoint is $-\theta-\lambda-1$, so the dual-resolution computation gives (2.5). For a germ $\sum a_nx^n$, a preimage has coefficients $a_n/(n+\lambda+1)$ except at a possible resonant index. For nonintegral $\lambda$ there is no resonant nonnegative index, and this series converges on each smaller disc. The origin stalk is zero. Off zero, solving the connection equation gives $x^{-\lambda}e$, hence monodromy $e^{-2\pi i\lambda}$. The local circle complex has invertible $T_\lambda-1$, so $j_!L_\lambda[1]=Rj_*L_\lambda[1]$.

For $\lambda\ge0$ integral there is still no resonant index; the stalk is zero and the punctured local system is trivial. Adjunction from its shriek extension gives the desired global isomorphism. For $\lambda<0$ integral, put $m=-\lambda-1\ge0$. Kernel and cokernel of (2.5) at zero are both the class $x^m$. The already proved cyclic-module identification with $L$ and the nonzero residue map in 12.3 identify its gluing with $Rj_*\mathbb C[1]$. These are precisely the three cases in (2.6). In the Laurent connection model, horizontal and residue representatives are respectively $x^{-\lambda}e$ and $x^{-\lambda-1}e\,dx$; their exponents differ because the second represents a one-form.

**12.5.** An algebraic D-map $\mathcal O\to E$ sends $1$ to $g(x)e$ with $g'+g=0$. A nonzero polynomial cannot satisfy this equation: its highest-degree term survives in $g$ and has no cancellation in $g'$. Thus this Hom space is zero. A D-map $E\to\mathcal O$ sends $e$ to $h(x)$ and requires $h'=h$; the same degree argument makes it zero. In particular no algebraic isomorphism exists.

Analytically, multiplication by the horizontal section $e^{-x}e$ identifies the two flat bundles, so Proposition 1.2 gives both de Rham complexes as $\mathbb C[1]$. Their sheaf-complex Hom space contains the nonzero identity of $\mathbb C[1]$, while the corresponding algebraic D-Hom space is zero. Therefore the de Rham functor is not full, and hence not fully faithful, on all holonomic modules. This argument does not claim that it sends a nonzero algebraic module to zero: the lost datum here is an algebraic morphism and the irregular behavior at infinity.

## What this lesson does not prove

The analytic Cauchy–Kowalevski–Kashiwara theorem, constructibility and perversity theorem, and Verdier-duality comparison are stated with their locators. Arbitrary inverse-image and nonproper direct-image compatibility are stated for regular holonomic complexes, not for every holonomic complex. Grothendieck's nonproper algebraic de Rham comparison and the relative GAGA and proper sheaf-cohomology prerequisites in Section 3 are used as external algebraic-geometry and sheaf-theory results. The Spencer identification, holomorphic Poincaré lemma, all singular-point computations, closed and proper direct-image comparisons, and all five exercises are proved here.

## References

- M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §§9.2, 9.5 and 10.2: constructibility and perversity of solution complexes, and non-characteristic systems.
- V. Ginzburg, [*Lectures on D-modules*](https://math.berkeley.edu/~nadler/ginzburg.dmodules.pdf): de Rham and solution functors, holonomic duality and the comparison theorems.
- Bhatt–Blickle–Lyubeznik–Singh–Zhang, [*Applications of perverse sheaves in commutative algebra*](https://arxiv.org/abs/2308.03155), Section 2, theorem labeled “RH,” parts (1)–(3): the regular holonomic correspondence and normalization.
- Frenkel, [*Lectures on the Langlands program and conformal field theory*](https://arxiv.org/abs/hep-th/0512172), Sections 3.4–3.6: systems, Euler examples and the two functor conventions.
- Grothendieck, [*On the de Rham cohomology of algebraic varieties*](https://pmihes.centre-mersenne.org/articles/10.1007/BF02684807/), Theorems 1 and 1′, pp. 95–96.
- Liu, [*Quasi-coherent GAGA*](https://irma.math.unistra.fr/~liu/qchGAGA.pdf), Proposition 3.1: relative comparison for quasi-coherent coefficients.
- [Stacks, Tag 0FL6](https://stacks.math.columbia.edu/tag/0FL6) and [Tag 0FLW](https://stacks.math.columbia.edu/tag/0FLW): algebraic de Rham cohomology and its affine computation.
