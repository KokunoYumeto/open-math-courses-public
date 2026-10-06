# The Riemann-Hilbert correspondence

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The Riemann-Hilbert correspondence turns regular differential equations into constructible topology. At a nonsingular point a connection becomes a local system. Across a singular point, the topology also remembers how that local system attaches to the point. On the affine line this extra information can be calculated with two vector spaces and two arrows.

We state the general correspondence, then prove its integer-monodromic affine-line case. The proof computes the actual de Rham attaching map; an abstract equivalence between two diagram categories would not by itself identify the de Rham functor.

We keep left D-modules and the normalization $\operatorname{DR}(\mathcal O_X)=\mathbb C_{X^{\rm an}}[d_X]$ from [The de Rham functor](the-de-rham-functor.md). Algebraic regularity includes infinity, as in [Regular singularities](regular-singularities.md). The Weyl-algebra classification works over a characteristic-zero field $k$; the de Rham comparison uses $k=\mathbb C$. We use the perverse heart of The perverse t-structure and the independently proved two-stratum diagram equivalence in Nearby and vanishing cycles, Theorem 3.1.

## 1. The general theorem and its precise target

Write $D^b_{c,\rm alg}(X^{\rm an},\mathbb C)$ for bounded complexes with finite-dimensional stalks, constructible with respect to a finite algebraic stratification of $X$. The strata are smooth locally closed algebraic subvarieties. The qualifier matters: an arbitrary locally finite analytic stratification can have infinitely many singular points on $\mathbb A^1$ and need not come from algebraic data.

**Theorem 1.1 (Riemann-Hilbert; statement).** For a smooth separated complex algebraic variety $X$, analytification followed by normalized de Rham gives an equivalence
\[
\operatorname{DR}_X:
D^b_{\rm rh}(\mathcal D_X)
\ \simeq\ D^b_{c,\rm alg}(X^{\rm an},\mathbb C).                 \tag{1.1}
\]
It identifies the standard D-module t-structure with the middle perverse t-structure. Hence
\[
\operatorname{DR}_X(\mathcal H^qM)
\simeq{}^p\mathcal H^q(\operatorname{DR}_X M),\qquad
\operatorname{Mod}_{\rm rh}(\mathcal D_X)
\simeq\operatorname{Perv}_{\rm alg}(X^{\rm an},\mathbb C).        \tag{1.2}
\]
For every algebraic morphism $f:X\to Y$ it commutes with the four map operations $f_*,f_!,f^!,f^*$, with holonomic/Verdier duality, and with external products. Here sheaf $f^*$ means inverse image; D-module $f^*$ is the dual-defined functor fixed in [Adjunctions, base change and the projection formula](adjunctions-base-change-and-the-projection-formula.md).

The Riemann–Hilbert correspondence is due to Kashiwara and to Mebkhout; for statements see M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §9.2, and V. Ginzburg, [*Lectures on D-modules*](https://math.berkeley.edu/~nadler/ginzburg.dmodules.pdf). Bhatt–Blickle–Lyubeznik–Singh–Zhang, §2, the covariant Riemann-Hilbert theorem, states the same normalization and specifies algebraic constructibility before the theorem. We use these as statements, not as a proof of (1.1).

Tensor compatibility uses the tensor convention already fixed:
\[
M\otimes^!N=\Delta_X^!(M\boxtimes N)
\simeq(M\otimes_{\mathcal O_X}^L N)[-d_X].
\]
On sheaves it is $\Delta_{X^{\rm an}}^!(F\boxtimes G)$. Thus it follows from external-product and inverse-image compatibility. The unit $\mathcal O_X[d_X]$ becomes the dualizing sheaf $\mathbb C_X[2d_X]$. Taking the dual tensor gives compatibility with the corresponding Hom operation. One should not replace these operations by an unshifted ordinary tensor without changing the normalization.

The theorem sends a minimal extension of an irreducible regular connection $E$ on a smooth $U$ to
\[
\operatorname{DR}(j_{!*}E)=j_{!*}(L[d_U])=\operatorname{IC}(L),  \tag{1.3}
\]
where $L$ is its horizontal local system, with closed extension to the ambient support understood. Indeed an exact equivalence preserves the image defining intermediate extension and preserves simplicity. The local system must be irreducible for the IC to be simple.

The contravariant solution functor satisfies
$\operatorname{Sol}(M)=\operatorname{DR}(\mathbb D M)$ with the normalized shifts used here. For a connection it sees the dual local system, so its monodromy is the inverse transpose of de Rham monodromy. This distinction is visible in the calculation below.

## 2. The integer block of the Weyl algebra

Let $A=k\langle x,\partial\rangle/(\partial x-x\partial-1)$ and $\theta=x\partial$. Call an $A$-module **monodromic** if every vector lies in a finite-dimensional $\theta$-stable subspace. In the integer block its generalized eigenvalues belong to $\mathbb Z\subset k$.

Local finiteness gives the direct sum
\[
M=\bigoplus_{n\in\mathbb Z}M^n,\qquad
M^n=\{m:(\theta-n)^q m=0\text{ for some }q\}.                  \tag{2.1}
\]
This follows by decomposing the finite-dimensional $\theta$-span of each vector; polynomial spectral projectors separate its distinct integer eigenvalues. The commutators
$[\theta,x]=x$, $[\theta,\partial]=-\partial$ show that $x:M^n\to M^{n+1}$ and $\partial:M^n\to M^{n-1}$.

The identities
\[
x\partial=\theta,\qquad \partial x=\theta+1                  \tag{2.2}
\]
make $x:M^n\to M^{n+1}$ invertible unless $n=-1$, and $\partial:M^n\to M^{n-1}$ invertible unless $n=0$. For example a nonzero scalar plus a locally nilpotent operator has inverse given on each vector by its terminating geometric series. Applying (2.2) on both weight spaces supplies both a left and a right inverse.

Only the two arrows across these exceptional weights remain:
\[
V_0=M^0,\quad V_1=M^{-1},\quad
a=x:V_1\to V_0,\quad b=\partial:V_0\to V_1.
\]
Put $N_0=ab$, $N_1=ba$. They are respectively $\theta|_{M^0}$ and $(\theta+1)|_{M^{-1}}$, and are locally nilpotent.

**Theorem 2.1 (two-space classification).** Integer-block monodromic $A$-modules are equivalent to quadruples $(V_0,V_1,a,b)$ with $ab$ locally nilpotent. For finitely generated modules the two spaces are finite-dimensional and the composites are nilpotent. In this category a module is holonomic if and only if both spaces are finite-dimensional.

The local qualification in the unrestricted statement is necessary. A direct sum of nilpotent Jordan blocks of all sizes is locally nilpotent without a common nilpotence exponent. For finite-dimensional spaces local nilpotence is nilpotence. Also
$(ba)^{q+1}=b(ab)^q a$ proves local nilpotence of $ba$ from that of $ab$.

**Proof: reconstruction.** Make one copy of $V_0$ for each weight $n\geq0$, and one copy of $V_1$ for each $n\leq-1$, and take their algebraic direct sum. Define the operators between those copies by
\[
\begin{array}{c|c|c}
\text{weight of the input}&x&\partial\\ \hline
n\geq1&I&nI+N_0\\
n=0&I&b\\
n=-1&a&I\\
n\leq-2&(n+1)I+N_1&I .
\end{array}                                                   \tag{2.3}
\]
Each entry lands in the adjacent weight. In the first row $x$ lands at weight $n+1$, while $\partial$ lands at $n-1$.

For $n\geq1$, $\partial x-x\partial=(n+1+N_0)-(n+N_0)=I$. At weight zero it is $(1+N_0)-ab=I$; at weight minus one it is $ba-(-1+N_1)=I$; and in all lower weights it is again the difference of two consecutive scalars. Thus (2.3) is an $A$-module. Its $\theta$ is $n+N_0$ on the nonnegative copies and $n+N_1$ on the negative copies. Local nilpotence makes this action locally finite and gives exactly the prescribed generalized eigenspaces.

Starting with $M$, identify $M^n$ for $n\geq0$ with $M^0$ by powers of $x$, and $M^n$ for $n\leq-1$ with $M^{-1}$ by powers of $\partial$. These maps are invertible by (2.2). The resulting actions are exactly (2.3); no choices beyond those two initial spaces are required. A pair of linear maps commuting with $a,b$ extends on every copy to an $A$-linear map. Conversely an $A$-map preserves generalized weights and is determined by the initial two spaces. The constructions are inverse on objects and morphisms.

**Proof: finiteness and holonomicity.** If both spaces are finite, bases of the weight-zero and weight-minus-one copies generate every other copy. Let $F_p$ be the Bernstein filtration generated by their span. A word of length at most $p$ reaches only weights between $-1-p$ and $p$; each has dimension at most $\dim V_0+\dim V_1$. Thus $\dim F_p=O(p)$. A nonzero finitely generated Weyl module of this growth is holonomic, by the Bernstein inequality and dimension criterion proved earlier.

Conversely take finitely many generators of a monodromic module. Enlarge them to a finite-dimensional $\theta$-stable space and separate its finitely many weights; this still gives finitely many generators. The degree-$q$ part of $A$ for $\deg x=1$, $\deg\partial=-1$ is $x^qk[\theta]$ for $q\geq0$, and $\partial^{-q}k[\theta]$ for $q<0$. This follows by reducing each fixed-degree PBW monomial with $x^j\partial^j=\theta(\theta-1)\cdots(\theta-j+1)$. On each generator, $k[\theta]$ has finite-dimensional image. For any fixed target weight, only one degree from each generator weight can contribute. Hence every $M^n$, in particular $M^0,M^{-1}$, is finite-dimensional. A holonomic module is finitely generated, so this proves the remaining implication. $\square$

Every finite object here is algebraically regular. On $\mathbb G_m$, localization identifies it with the connection
\[
\mathcal O_{\mathbb G_m}\otimes V_0,\qquad
\partial(v)=x^{-1}N_0v.                                      \tag{2.4}
\]
To see the negative weights, the vector $w\in V_1$ at weight $-1$ localizes to $x^{-1}aw$; further negative weights follow by differentiating this identity. The zero-space case includes modules supported at zero. Connection (2.4) has logarithmic lattices at both zero and infinity. A simple factor meeting $\mathbb G_m$ therefore has a regular generic connection, and a simple factor supported at zero is a delta module. The regularity definition proves the assertion.

## 3. The elementary extension dictionary

Here $j:\mathbb G_m\hookrightarrow\mathbb A^1$ and $\delta_0=A/Ax$. The following table lists $(V_0,V_1,a,b)$:

| D-module | $V_0$ | $V_1$ | $a=x$ | $b=\partial$ |
| --- | --- | --- | --- | --- |
| $\mathcal O_{\mathbb A^1}$ | $k$ | $0$ | $0$ | $0$ |
| $\delta_0$ | $0$ | $k$ | $0$ | $0$ |
| $j_*\mathcal O_{\mathbb G_m}=k[x,x^{-1}]$ | $k$ | $k$ | $1$ | $0$ |
| $j_!\mathcal O_{\mathbb G_m}=A/A(x\partial)$ | $k$ | $k$ | $0$ | $1$ |
| $j_{!*}\mathcal O_{\mathbb G_m}$ | $k$ | $0$ | $0$ | $0$ |

For polynomials, $\theta x^n=nx^n$ and only nonnegative weights occur. For $\delta_0$, the vectors $\partial^q\delta$ have weights $-1-q$, and $x\partial\delta=-\delta$. For Laurent polynomials the exceptional spaces are generated by $1$ and $x^{-1}$, with $x(x^{-1})=1$, $\partial1=0$.

For the shriek extension use the generator $u$ with $x\partial u=0$. The vectors $x^q u$ and $\partial^{q+1}u$ form the nonnegative and negative weight strings. They are independent and nonzero by the reconstructed module (2.3) with $a=0,b=1$; conversely the relation and PBW span this module, so the presentation is exact. Its identification with $j_!\mathcal O$ was proved by duality in [Holonomic D-modules and duality](holonomic-d-modules-and-duality.md). The canonical map $j_!\mathcal O\to j_*\mathcal O$ is $(1,0)$ on the two spaces; its image is $(k,0)$, proving the final row.

More generally the logarithmic connection (2.4) has star extension
$(V,V,I,N)$ and shriek extension $(V,V,N,I)$. The Laurent connection gives the star row directly. Here is an adjunction check for the shriek row. A morphism from $(V,V,N,I)$ to $(V_0',V_1',a',b')$ is uniquely determined by $f_0:V\to V_0'$ with $f_0N=N_0'f_0$, since its other component must be $f_1=b'f_0$. These are exactly connection maps on $\mathbb G_m$, so this diagram represents shriek adjunction in the monodromic category. The actual $j_!E$ belongs to that category: a nilpotent-residue connection has a finite flag with trivial connection quotients; $j_!$ on such connections is exact by duality and exact Laurent localization, so $j_!E$ is an extension of copies of the already computed $j_!\mathcal O$. Local finiteness with integer spectrum is preserved under extensions, since an annihilating polynomial for a quotient vector followed by one for its lift in the submodule annihilates the original vector. Thus Theorem 2.1 applies to $j_!E$, and adjunction identifies the diagram. In Section 4 we identify both extensions by their actual sheaf attaching maps.

For a Jordan example choose $V_0=V_1=k^2$, $a=I$ and
\[
b=N=\begin{pmatrix}0&1\\0&0\end{pmatrix}.                       \tag{3.1}
\]
It is the star extension of the rank-two logarithmic connection with residue $N$. The powers in (2.3) describe the whole Weyl module, not just its fiber. The shriek version instead has $a=N,b=I$.

## 4. Computing de Rham and its attaching map

Work over $\mathbb C$. The sheaf prerequisite gives diagrams
\[
V\xrightarrow{u}W\xrightarrow{v}V,\qquad I+vu\text{ invertible},
\]
where $V=\Psi_xK$, $W=\Phi_xK$, $u=\mathrm{can}$, $v=\mathrm{var}$, with convention
$vu=T_V-I$. For such a diagram,
\[
i^*K=[V\xrightarrow{u}W]\quad(-1,0),\qquad
i^!K=[W\xrightarrow{v}V]\quad(0,1).                           \tag{4.1}
\]
It reconstructs $K$ from its local system on the puncture and the attaching map
\[
(I,v):[V\xrightarrow{u}W]\longrightarrow
[V\xrightarrow{T_V-I}V].                                    \tag{4.2}
\]
The general sheaf diagram theorem is used as a prerequisite, already proved by gluing; we now compute these data for a D-module.

**Lemma 4.1 (analytic stalk).** For a finite quadruple, the normalized de Rham stalk at zero is naturally homotopy equivalent to
\[
[V_0\xrightarrow{b}V_1]\quad\text{in degrees }-1,0.            \tag{4.3}
\]

**Proof.** Analytification of the weight presentation replaces the nonnegative polynomial tail by a convergent power-series tail with coefficients in $V_0$, while negative weights remain finite sums of vectors from the $V_1$ copies. One can verify this normal form directly by Taylor division: for a negative-weight vector and a holomorphic multiplier, repeatedly separate its constant term and divide the remainder by $x$ until multiplication reaches the nonnegative part. The finite relations in (2.3) then determine the convergent tail. Conversely these formulas define the holomorphic multiplication action on this normal-form space and invert the map from $\mathcal O^{\rm an}_0\otimes_{\mathbb C[x]}M$.

The unshifted de Rham differential is $\partial$, with target tensored by $dx$. On all negative inputs it carries each weight copy identically to the next lower target copy. On positive inputs of weight $n\geq1$ it is $nI+N_0$, and its only exceptional component is $b$ from weight zero to target weight minus one. All other components are isomorphisms. Their inverses preserve convergence: for nilpotent $N_0$,
\[
(nI+N_0)^{-1}
=\sum_{q\geq0}(-1)^q n^{-q-1}N_0^q                           \tag{4.4}
\]
is a fixed finite sum, uniformly $O(n^{-1})$ for $n\geq1$. Negative tails remain finite. Contract those pairs. The remaining differential is $b$, and normalization by $[1]$ gives the displayed degrees. All contractions commute with morphisms of quadruples. $\square$

The punctured local system has fiber $V_0$ and positive monodromy
\[
T_0=e^{-2\pi iN_0}.                                          \tag{4.5}
\]
Its boundary circle complex is $[V_0\xrightarrow{T_0-I}V_0]$ in degrees $-1,0$.

Define the power series, evaluated as a finite polynomial on a nilpotent operator,
\[
h(z)=\frac{e^{-2\pi iz}-1}{z}
=\sum_{q\geq0}\frac{(-2\pi i)^{q+1}}{(q+1)!}z^q,
\qquad h(0)=-2\pi i.                                        \tag{4.6}
\]
Thus $h(N_0)$ is invertible, including when $N_0=0$.

**Lemma 4.2 (the actual boundary comparison).** In the contractions of Lemma 4.1, restriction to the puncture gives the attaching map
\[
(I,h(N_0)a):
[V_0\xrightarrow{b}V_1]\longrightarrow
[V_0\xrightarrow{T_0-I}V_0].                                \tag{4.7}
\]

**Proof.** The degree-minus-one representative is the constant coefficient $v_0$ in the logarithmic frame. Evaluate it at a chosen point of a small circle to identify the fiber with $V_0$; this gives $I$.

A representative $w\in V_1$ in the remaining degree-zero term is the one-form whose coefficient has weight minus one. On localization it is $x^{-1}aw\,dx$ by (2.4). Parameterize the circle by $x=r e^{i\vartheta}$, $0\leq\vartheta\leq2\pi$. Parallel transport back to the initial frame multiplies coefficients by $e^{i\vartheta N_0}$.

With the cellular cochain differential chosen as $T_0-I$, the map on one-forms is minus $T_0$ times the transported integral. This sign and factor can be checked on every single-valued section $s(\vartheta)$:
\[
-T_0\int_0^{2\pi}e^{i\vartheta N_0}
\bigl(s'(\vartheta)+iN_0s(\vartheta)\bigr)\,d\vartheta
=(T_0-I)s(0).                                                \tag{4.8}
\]
Indeed the integral before multiplication is
$e^{2\pi iN_0}s(2\pi)-s(0)$, and $s(2\pi)=s(0)$.
For our form the integral is
$\int_0^{2\pi}e^{i\vartheta N_0}i\,aw\,d\vartheta$.
Its product with $-T_0$ is $h(N_0)aw$, by the finite power-series identity. The calculation holds on each sufficiently small circle and commutes with restriction of germs. The contracted acyclic weight pairs merely give the associated chain homotopies. This proves (4.7), not just its effect on dimensions. Its chain-map equation is also visible directly:
$h(N_0)ab=h(N_0)N_0=T_0-I$. $\square$

**Theorem 4.3 (the monodromic correspondence, proved).** The normalized de Rham functor is an equivalence between finite integer-block monodromic D-modules on $\mathbb A^1$ and perverse sheaves on $\mathbb C$ constructible for $\mathbb C^*,\{0\}$ with unipotent nearby monodromy. On diagrams it is
\[
(V_0,V_1,a,b)\longmapsto
(V=V_0,W=V_1,u=b,v=h(N_0)a).                                 \tag{4.9}
\]

**Proof.** The stalk and attaching map were computed in Lemmas 4.1–4.2. On the open stratum, the analytic Poincaré lemma for a flat connection identifies de Rham with its horizontal local system shifted by $[1]$. Gluing along the point therefore gives exactly the diagram (4.9). Its two composites are
\[
vu=e^{-2\pi iN_0}-I,\qquad uv=e^{-2\pi iN_1}-I,                \tag{4.10}
\]
using $b\,p(N_0)=p(N_1)b$ and $p(N_0)a=a\,p(N_1)$ for every polynomial $p$. Both monodromies are unipotent. Formula (4.1), or the proved sheaf diagram theorem, shows that this gluing is perverse; no use of the general correspondence is required.

Conversely, given a finite sheaf diagram with $I+vu$ unipotent, put
\[
N_0=-\frac1{2\pi i}\log(I+vu),\quad
N_1=-\frac1{2\pi i}\log(I+uv),\quad
b=u,\quad a=h(N_0)^{-1}v.                                   \tag{4.11}
\]
The logarithms are finite nilpotent series. Nilpotence of $vu$ implies that of $uv$ by $(uv)^{q+1}=u(vu)^qv$. Polynomial intertwining gives $ab=N_0$ and $ba=N_1$, because $h(N_j)N_j=e^{-2\pi iN_j}-I$. Thus Theorem 2.1 reconstructs a finite, regular holonomic D-module. Equations (4.9) and (4.11) are inverse.

A morphism of either kind is a pair commuting with its two arrows. Such a pair commutes with all the displayed polynomial functions of their composites. It therefore commutes with the arrows on the other side as well. The transformations are inverse on morphisms, and preserve composition. This proves full faithfulness and essential surjectivity for the actual de Rham functor. $\square$

In particular $a$ by itself is not the variation arrow with our monodromy normalization. The invertible correction $h(N_0)$ is essential.

For the elementary modules this gives
\[
\begin{array}{c|c}
\mathcal O_{\mathbb A^1}&\mathbb C_{\mathbb C}[1]\\
\delta_0&\mathbb C_{\{0\}}\\
j_*\mathcal O_{\mathbb G_m}&Rj_*\mathbb C_{\mathbb C^*}[1]\\
j_!\mathcal O_{\mathbb G_m}&j_!\mathbb C_{\mathbb C^*}[1]\\
j_{!*}\mathcal O_{\mathbb G_m}&\mathbb C_{\mathbb C}[1].
\end{array}                                                   \tag{4.12}
\]
For the star row, (4.9) has $u=0,v=-2\pi iI$; rescale the vanishing space to get the usual $u=0,v=I$. The shriek row already has $u=I,v=0$. The smooth and point rows fix which of the two spaces is nearby and which is vanishing.

For the Jordan example (3.1),
\[
T_0=I-2\pi iN,\quad
u=N,\quad v=-2\pi iI-2\pi^2N.                                \tag{4.13}
\]
The invertible change on the vanishing space $h(N)$ puts this into the standard star diagram $u=T_0-I,v=I$. Its stalk groups are $\ker N$ in degree $-1$ and $\operatorname{coker}N$ in degree zero, each one-dimensional. The shriek version has zero stalk. Intermediate extension instead has vanishing space $\operatorname{im}N$, of dimension one, rather than the two-dimensional vanishing space of either full extension.

## 5. Nonintegral blocks and the role of regularity

Let $\lambda\notin\mathbb Z$. The Laurent connection
\[
E_\lambda=\mathbb C[x,x^{-1}]e,\qquad
\partial e=\lambda x^{-1}e                                  \tag{5.1}
\]
has weights $\lambda+\mathbb Z$, so it does not belong to Theorem 2.1's integer block. Its monodromy is $e^{-2\pi i\lambda}$.

More generally on a finite space $V$ take residue $\lambda I+N$ with $N$ nilpotent. On the copy of $V$ of weight $\lambda+n$, define $x=I$ to the next copy and $\partial=(\lambda+n)I+N$ to the previous one. The Weyl relation holds by subtracting consecutive scalars. Every such scalar-plus-nilpotent operator is invertible, so both exceptional-arrow analogues are invertible. The module is the Laurent connection with that residue.

The same analytic contraction as in Lemma 4.1 now contracts **every** weight pair, since there is no zero scalar. It has zero de Rham stalk at zero, while the punctured local system has
$T=e^{-2\pi i(\lambda I+N)}$ with $T-I$ invertible. The circle complex is acyclic, so the extension is simultaneously $j_!L[1]$ and $Rj_*L[1]$. This proves the nonresonant star/shriek equality on the line directly.

This also completes the heart correspondence for **all** finitely generated monodromic modules over $\mathbb C$, not just the integer block. Their finitely many eigenvalues modulo $\mathbb Z$ separate them into blocks, because $x,\partial$ preserve those classes. In a nonintegral block every $x$ and $\partial$ transition is invertible by (2.2). Identify all weights with one finite space through $x$; the module is exactly the Laurent model above. Maps are constant residue intertwiners.

On the sheaf side decompose nearby and vanishing spaces into the generalized eigenspaces of their invertible monodromies. The two arrows preserve these decompositions. Away from eigenvalue one, both composites are invertible, so both arrows are invertible and give the unique common star/shriek extension. Every such $T$ is realized by a residue $\lambda I+N$ using the finite logarithm on its generalized eigenblock, as in the preceding lesson. Normalized residues in one representative of each class modulo integers have exactly the same intertwiners as their exponentials. Eigenvalue one is Theorem 4.3's block; point-supported contributions belong there too. These decompositions are functorial, so combining the proved block equivalences gives the full monodromic heart equivalence on the two-stratum line.

There is no nonzero analogue with both $a$ and $b$ invertible in the nilpotent integer-block diagram: then $ab$ would be both invertible and nilpotent. This elementary obstruction is why the nonintegral block must be specified.

Finally, the regularity hypothesis in (1.1) cannot be removed. The trivial connection and $\mathcal O.e^x$ on $\mathbb A^1$ both have analytically trivial rank-one horizontal local systems, but they are not algebraically isomorphic. An algebraic connection map between them would require a nonzero polynomial solution of $g'+g=0$ or $g'-g=0$, impossible by comparing the highest degree. The exponential is irregular at infinity. Their zero-section characteristic varieties do not separate them.

Even the algebraic Fourier transform need not preserve regularity. In the convention $x_{\rm new}=\partial_{\rm old}$, $\partial_{\rm new}=-x_{\rm old}$, the regular delta module at $c\neq0$ becomes the connection with $\partial_{\rm new}e=-c e$. It is irregular at infinity by the rank-one test. The Fourier operation is still an equivalence of holonomic categories; it requires the broader differential-equation category.

## 6. Where the correspondence enters geometric Langlands

For a smooth complete complex curve and a connected reductive group $G$, Gaitsgory–Raskin, [*Proof of the geometric Langlands conjecture I: construction of the functor*, introduction and §4.2](https://arxiv.org/abs/2405.03599), compares the restricted de Rham and restricted Betti settings through Riemann-Hilbert. The automorphic categories use half-twisted objects on $\operatorname{Bun}_G$ with nilpotent singular support.

The regularity input is substantial: §4.2 invokes Arinkin–Gaitsgory–Kazhdan–Raskin–Rozenblyum–Varshavsky, Corollary 16.5.6, to identify that D-module category with its regular-singular part. The stack formulation first takes ind-completions on affine schemes and then limits over affine maps to the stack. It is not the bounded finite-dimensional theorem applied directly to one infinite-dimensional space.

Riemann-Hilbert also identifies the restricted local-system prestacks through their Tannakian input. The commuting square of restricted Langlands functors in §4.2 then transfers equivalence between the two settings. Full-formulation comparison uses further arguments there. We state these applications; no geometric Langlands theorem or stack extension is proved here.

## 7. Exercises with complete solutions

**Exercise 14.1 (easy).** Compute the quadruples of $\mathcal O$, $\delta_0$, $j_*\mathcal O$ and $j_!\mathcal O$.

**Solution.** The weight-zero and weight-minus-one spaces in polynomials are $k,0$; in delta they are $0,k$. In Laurent polynomials they are generated by $1,x^{-1}$, with $a(x^{-1})=1$ and $b(1)=0$, giving $(k,k,1,0)$. For $A/A(x\partial)$ they are generated by $u,\partial u$, with $a(\partial u)=0$ and $b(u)=\partial u$, giving $(k,k,0,1)$. Their entire modules are recovered by (2.3), so no further extension parameter is hidden.

**Exercise 14.2 (easy).** Show that $j_{!*}\mathcal O_{\mathbb G_m}$ has quadruple $(k,0)$.

**Solution.** The canonical map from the shriek diagram $(k,k,0,1)$ to the star diagram $(k,k,1,0)$ is $(1,0)$. It commutes with both arrows, and its open restriction is the identity. Intermediate extension is its image; kernels and images of this equivalence are computed on the two vector spaces. The image is $(k,0)$, the polynomial module.

**Exercise 14.3 (medium).** Reconstruct the module from a nilpotent quadruple and prove the equivalence.

**Solution.** Place $V_0$ in every nonnegative integer weight and $V_1$ in every negative one, and use (2.3). At the two boundary weights the Weyl commutator is respectively $(I+ab)-ab=I$ and $ba-(-I+ba)=I$; elsewhere it is the difference of consecutive integers. Its $\theta$ eigenvalues and nilpotent parts are the desired ones. Starting from any integer-block module, the invertible $x$ and $\partial$ arrows away from weights $-1,0$ identify it with this reconstruction. Every morphism is determined by the two initial weight maps, and the commuting equations with $a,b$ extend those maps uniquely to all other weights. The two functors are inverse. For unrestricted infinite spaces replace nilpotence by local nilpotence as in Theorem 2.1.

**Exercise 14.4 (medium).** Identify the de Rham images of the four elementary modules as perverse sheaves on the line.

**Solution.** Apply (4.9). Polynomials give nearby $\mathbb C$ and vanishing zero, hence $\mathbb C[1]$; delta gives nearby zero and vanishing $\mathbb C$, hence the point sheaf in degree zero. The Laurent module gives $u=0,v=-2\pi i$, isomorphic by rescaling to the star diagram, hence $Rj_*\mathbb C[1]$. The shriek module gives $u=1,v=0$, hence $j_!\mathbb C[1]$. Their stalks are respectively $\mathbb C[1]$, $\mathbb C$ in degree zero, one copy in each of degrees $-1,0$, and zero. These degrees agree with (4.3).

**Exercise 14.5 (hard; corrected scope).** Can a nonzero nilpotent quadruple have both arrows invertible? Prove the intended equality $j_*L[1]=j_!L[1]$ in a nonintegral block.

**Solution.** If both arrows were invertible, $ab$ would be invertible. If $(ab)^q=0$, multiplying by its inverse $q$ times gives $I=0$, so both spaces must be zero. Thus the assertion for nonzero integer-block nilpotent quadruples would be false.

For the intended nonresonant assertion take residue $\lambda I+N$, $\lambda\notin\mathbb Z$, $N$ nilpotent. Every transition $(\lambda+n)I+N$ is invertible by its terminating inverse series. The resulting module is a Laurent logarithmic connection, regular at both ends. Analytic de Rham contracts every weight pair at zero; its stalk is zero. Its local monodromy has sole eigenvalue $e^{-2\pi i\lambda}\neq1$, so the complex $[V\xrightarrow{T-I}V]$ is acyclic. The localization triangle identifies $j_!L[1]\to Rj_*L[1]$ as an isomorphism, and the computed de Rham extension is this common object. Direct sums give the same conclusion for all finite local systems whose monodromy has no eigenvalue one.

## What this lesson does not prove

We state the general algebraic Riemann-Hilbert equivalence, its perverse t-exactness and the full map/duality/external-product compatibility with the precise locators in Section 1. The normalized tensor statement is a consequence of those compatibilities. The independent two-stratum sheaf diagram theorem is a prerequisite from *Nearby and vanishing cycles*; its proof is not repeated here. We use the nonsingular analytic flat-connection Poincaré lemma already proved in this course.

The affine-line integer-monodromic correspondence, including reconstruction, finiteness, actual boundary comparison, exponential correction and inverse diagram functor, is proved here. We do not deduce a derived equivalence on this subcategory solely from the heart calculation. The stack regularity input, ind-completion and restricted geometric Langlands comparison in Section 6 are stated applications of Gaitsgory–Raskin, not new proofs.

## References

- M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), §§9.2 and 9.5, and V. Ginzburg, [*Lectures on D-modules*](https://math.berkeley.edu/~nadler/ginzburg.dmodules.pdf): the Riemann–Hilbert correspondence, perverse sheaves and intermediate extensions. The irreducible IC assertion is used only for an irreducible local system.
- Bhatt, Blickle, Lyubeznik, Singh and Zhang, [*Applications of perverse sheaves in commutative algebra*](https://arxiv.org/abs/2308.03155), §2, covariant Riemann-Hilbert theorem and its properties; the sketch's §1 locator is corrected to §2.
- M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), Chapter 9: perversity of normalized holonomic solution complexes, with solution/de Rham duality as in the preceding lessons.
- *Nearby and vanishing cycles*, Theorem 3.1 and Section 4, for the perverse diagram theorem, attaching maps and extension dictionary used here.
- Gaitsgory and Raskin, *Proof of the geometric Langlands conjecture I: construction of the functor*, arXiv:2405.03599, introduction and §4.2, “Applications of Riemann-Hilbert”; the regularity result cited there is Arinkin–Gaitsgory–Kazhdan–Raskin–Rozenblyum–Varshavsky, Corollary 16.5.6.
