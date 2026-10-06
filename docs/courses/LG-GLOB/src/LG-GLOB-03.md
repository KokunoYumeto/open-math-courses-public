# Automorphic representations and automorphic L-functions

*Draft lesson. Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Public domain (CC0).*

An automorphic representation assembles local representations into an object that occurs in a space of functions on an arithmetic quotient. At almost every place, a spherical vector lets the Hecke algebra detect a semisimple Satake parameter. The eigenvalues of that parameter give an Euler factor. Multiplying these factors is straightforward in a sufficiently far right half-plane. Extending the product beyond that half-plane is a separate, deep problem.

This lesson constructs the partial products, proves global cuspidal genericity for every general linear group and the convergence deductions needed later, and computes the degree-one, symmetric-square and adjoint examples. It also explains what the analytic conjectures say and which methods establish particular cases. The prerequisites are *The Satake isomorphism for unramified groups and unramified L-factors* and *Restricted tensor products and the tensor product theorem*. The analytic theory for general linear groups is developed further in the following lesson.

## 1. From automorphic forms to local components

Let \(F\) be a number field, \(\mathbb A=\mathbb A_F\) its ring of adèles, and \(G\) a connected reductive group over \(F\). Fix a maximal compact subgroup \(K_\infty\subset G(F\otimes_{\mathbb Q}\mathbb R)\). Write \(\mathfrak g\) for the complexified Lie algebra at infinity and \(Z(\mathfrak g)\) for the center of its universal enveloping algebra.

An **automorphic form** is a function on \(G(\mathbb A)\) that is left \(G(F)\)-invariant, smooth at infinity, locally constant and right invariant under some compact open subgroup at the finite places, of moderate growth, and finite under both \(K_\infty\) and \(Z(\mathfrak g)\). Moderate growth means a polynomial bound in a fixed adelic height. Finiteness under \(Z(\mathfrak g)\) means that the translates by this commutative algebra span a finite-dimensional space. Denote the space of such forms by \(\mathcal A(G)\).

An **automorphic representation** is an irreducible admissible

\[
(\mathfrak g,K_\infty)\times G(\mathbb A_f)
\]

module that occurs as a subquotient of \(\mathcal A(G)\). This formulation matters: an arbitrary real group element need not preserve the subspace of \(K_\infty\)-finite vectors. When discussing a representation of the full adelic group, one uses a smooth globalization or a unitary Hilbert realization when it is available. A subquotient of all automorphic forms need not be a discrete constituent of an \(L^2\) space. These definitions follow [Getz–Hahn 2022, (6.5)–(6.6)].

For a proper \(F\)-parabolic \(P=MN\), define the constant term

\[
f_P(g)=\int_{N(F)\backslash N(\mathbb A)}f(ng)\,dn.
\tag{1.1}
\]

The unipotent quotient is compact. A form is **cuspidal** if every such constant term is zero. A cuspidal automorphic representation occurs in the cuspidal subspace \(\mathcal A_{\mathrm{cusp}}(G)\). Fixing a unitary central character, or quotienting by a split central real subgroup on which the character is trivial, gives the usual cuspidal \(L^2\) realization. The equality between the algebraic and Hilbert descriptions of cuspidal constituents is a theorem, not part of the elementary definition [Getz–Hahn 2022, Theorem 6.5.1]. Later uses of unitarity will say so explicitly.

**Lemma 1.0 (the domain of a constant term).** If \(N\) is a smooth connected unipotent group over a number field, then \(N(F)\backslash N(\mathbb A)\) is compact.

**Proof.** We first establish the algebraic structure needed for the adelic argument. A faithful representation of an affine algebraic group exists by *Group schemes, actions and Hopf algebras*, Theorem 5.13. Over an algebraic closure, every representation of a unipotent group has a full flag with trivial quotients, by *Maximal tori and their conjugacy*, Lemma 2.A. Fixed vectors are kernels of linear equations over \(F\), so their formation commutes with field extension. A nonzero geometric fixed space therefore gives a nonzero \(F\)-fixed vector. Repeating on the quotient gives an \(F\)-rational flag. In a basis adapted to it, the faithful representation embeds \(N\) into upper unitriangular matrices over \(F\).

In matrix size \(d\), the polynomials

\[
\log(1+A)=\sum_{j=1}^{d-1}(-1)^{j+1}A^j/j,
\qquad \exp X=\sum_{j=0}^{d-1}X^j/j!
\]

are inverse maps between the ambient unitriangular group and the space of strictly upper triangular matrices. The identities follow by substituting in the formal one-variable identities modulo \(z^d\). If \(u\in N(\overline F)\), put \(X=\log u\). Every defining equation of \(N\), evaluated on the polynomial curve \(\exp(tX)\), vanishes at every nonnegative integer \(t\), because \(\exp(mX)=u^m\). It therefore vanishes identically. Taking the tangent at zero gives \(X\in\mathfrak n=\operatorname{Lie}N\). Thus \(\log N\) is a reduced closed subvariety of \(\mathfrak n\). Its dimension is \(\dim N=\dim\mathfrak n\), by smoothness, and a proper closed subset of a vector space has smaller dimension. Hence \(\log N=\mathfrak n\); descent gives this polynomial isomorphism over \(F\).

The Lie algebra \(\mathfrak n\) is nilpotent: brackets of matrices whose entries start at distances \(a,b\) above the diagonal start at distance \(a+b\). If \(N\ne1\), the last nonzero term of its Lie lower central series contains a nonzero \(F\)-vector \(X\) commuting with \(\mathfrak n\). The closed subgroup \(C=\exp(FX)\) is central and isomorphic to \(\mathbf G_a\): commuting matrices satisfy \(\exp(Y+tX)=\exp Y\exp(tX)\). The affine quotient \(Q=N/C\) and its \(C\)-torsor map exist by *Quotients and torsors*, Theorems 11.1b and 11.1d. It is smooth connected, has dimension one less than \(N\), and is unipotent. Indeed, pull any representation of \(Q\) back to \(N\); its trivial-quotient flag descends along the faithfully flat quotient map. Applying this to a faithful representation of \(Q\) gives a unitriangular embedding.

The quotient map \(p:N\to Q\) has an algebraic section as a map of varieties. To see this explicitly, its tangent map \(dp:\mathfrak n\to\operatorname{Lie}Q\) is onto, since a \(\mathbf G_a\)-torsor is smooth. Choose an \(F\)-linear right inverse \(\ell\) and set

\[
s(q)=\exp_N\bigl(\ell(\log_Q q)\bigr).
\]

Homomorphisms commute with these exponentials. For verification, a polynomial matrix homomorphism \(R:\mathbf G_a\to\mathrm{UT}\) obeys \(R(t+u)=R(t)R(u)\). Differentiation in \(u\) at zero gives \(R'(t)=R(t)R'(0)\), whose coefficient recurrence gives \(R(t)=\exp(tR'(0))\). Apply this to \(p\circ\exp_N(tY)\). It follows that \(p\circ s=1\). These polynomial maps, with coefficients in \(F\), also give continuous adelic maps; they preserve integral points outside finitely many places, after clearing their finitely many denominators.

Now induct on \(\dim N\). The additive base case \(F\backslash\mathbb A\) is compact by *The adèle ring*, Theorem 2.2. By induction choose a compact set \(D_Q\subset Q(\mathbb A)\) representing every class modulo \(Q(F)\). Such a set exists for a compact quotient: the open quotient map sends relatively compact neighbourhoods to an open cover, from which one takes a finite subcover and the union of the compact closures. Choose similarly a compact representative set \(D_C\subset C(\mathbb A)\) modulo \(C(F)\).

For \(n\in N(\mathbb A)\), choose \(q_0\in Q(F)\) with \(q_0^{-1}p(n)\in D_Q\). The section lifts \(q_0\) to \(s(q_0)\in N(F)\). Write

\[
s(q_0)^{-1}n=c\,s(q),\qquad c\in C(\mathbb A),\quad q\in D_Q.
\]

Left multiplication by an element of \(C(F)\) puts \(c\) in \(D_C\). Consequently the compact set \(D_Cs(D_Q)\) represents every adelic class of \(N\). This proves compactness and justifies the finite integral in (1.1). \(\square\)

**Integral models outside finitely many places.** A connected reductive group over a global field has a reductive model away from finitely many places. Here is the construction needed for the restricted product. Choose a geometrically maximal \(F\)-torus by *Tori, maximal tori and their conjugacy*, Theorem 4.2, and split it over a finite Galois extension \(E/F\). Then \(G_E\) is split. A choice of pinning and *Pinnings and the classification of split reductive groups*, Theorem 10.1 give a pinned split integral group \(H\); Theorem 5.1 identifies \(G_E\) with \(H_E\). Transport the finite Galois descent datum to this model.

Let \(A\) be a ring of integers with finitely many primes inverted; in a function field take a nonempty affine open of the smooth complete curve. Its normalization \(B\) in \(E\) is a finite étale Galois cover after further localization. To verify this finite-exception assertion, choose a primitive element \(\beta\), clear its monic-polynomial denominators, and let \(\Delta\ne0\) be the discriminant of its power basis. For every integral \(x\in B\), the traces \(\operatorname{Tr}(x\beta^j)\) are integral and in \(F\), hence in the integrally closed ring \(A\). Cramer's rule puts \(B\) inside \(\Delta^{-1}A[\beta]\); Noetherianity makes it finite. After inverting \(\Delta\), the same argument gives \(B=A[\beta]\) and the polynomial derivative is a unit, so this finite free algebra is étale. The map

\[
B\otimes_A B\longrightarrow\prod_{\gamma\in\operatorname{Gal}(E/F)}B,
\qquad b\otimes c\longmapsto\bigl(b\gamma(c)\bigr)_\gamma
\]

is an isomorphism over \(F\). Its finite torsion kernel and cokernel vanish after inverting finitely many further elements of \(A\). This gives the asserted cover, without averaging by its degree.

The split model's Hopf algebra has finitely many algebra generators. Each semilinear descent map and its inverse is determined by their images. Invert the finitely many denominators in these images, together with their Galois conjugates. The defining relations, inverse identities, Hopf identities and cocycle identities now hold over \(B\): the model's Hopf algebra and its tensor powers are \(B\)-flat and inject into their generic fibres, where all the identities hold. This is an actual affine descent datum. The effective affine descent proved in *Quotients and torsors*, the opening affine-descent corollary descends the group and all its structure maps to \(A\). Finite presentation and smoothness descend by *Descending properties of schemes and morphisms*, Theorem 2.1. Each geometric fibre is, after lifting through the étale cover, a fibre of \(H\), hence connected reductive. We have obtained a reductive model with generic fibre \(G\).

At each remaining place its \(\mathcal O_v\)-points give the hyperspecial compact open subgroup \(K_v\). Compactness and openness follow in affine coordinates: the integral points are a closed subset of a finite product of the compact ring \(\mathcal O_v\), and each integrality condition is open in the local-field topology. This also establishes the finite set of model exceptions used in the following proof. \(\square\)

**Theorem 1.1 (Flath, 1979; local factorization).** An irreducible admissible automorphic module over a number field factors as

\[
\pi\simeq
\left(\bigotimes_{v\mid\infty}\pi_v\right)
\otimes\left(\bigotimes_{v\nmid\infty}'\pi_v\right).
\tag{1.2}
\]

At infinity, \(\pi_v\) is an irreducible admissible Harish-Chandra module; at a finite place it is an irreducible smooth admissible representation of \(G(F_v)\). For almost every finite \(v\), the group has an unramified integral model with hyperspecial subgroup \(K_v\), and \(\pi_v^{K_v}\ne0\). The restricted product is taken with respect to chosen nonzero vectors in these fixed spaces. The isomorphism class of every local factor is uniquely determined.

**Proof.** We use the algebraic factorization lemma proved in *Restricted tensor products and the tensor product theorem*, Theorem 4.1. Its statement concerns arbitrary algebras with local units, and does not impose a \(GL_2\) hypothesis: a simple nondegenerate module for \(A\otimes B\), with every idempotent corner \((e\otimes f)V\) finite-dimensional, factors uniquely as a tensor product of simple admissible local modules. The finite interpolation argument and idempotent reconstruction are proved there in Lemmas 3.1–3.2.

Let \(\mathcal H_v\) be the compactly supported locally constant convolution algebra at a finite place. Its local units are the normalized characteristic functions of compact open subgroups. At an infinite place use the algebra of compact-type finite convolution distributions generated by \(U(\mathfrak g_v)\) and \(K_v\); its local units are the sums of the Peter–Weyl projections onto finite sets of compact types. The construction in Section 2 of the same prerequisite works for these algebras for any \(G\): compact support at finite level has only finitely many deviations from the integral subgroups, and each finite sum of compact types has its corresponding projection. Thus the global algebra can be regrouped as \(\mathcal H_v\otimes\mathcal H^{v}\). Admissibility gives the finite-corner hypothesis. Theorem 4.1 extracts one unique simple admissible module \(\pi_v\) at each place; as a module for that place alone, \(\pi\) is a direct sum of copies of \(\pi_v\).

Choose \(0\ne w\in\pi\). Its finite stabilizer contains \(U=\prod_{v\in S_0}U_v\times\prod_{v\notin S_0}K_v\), for a finite set \(S_0\) containing the places without the chosen unramified model. Choose a finite compact-type projector \(e_E\) at infinity fixing \(w\), and let \(p=e_E\otimes e_U\). Global admissibility makes \(D=\dim p\pi\) finite and positive. For any finite set \(T\) outside \(S_0\), repeated application of the two-algebra theorem gives

\[
\pi\simeq\left(\bigotimes_{v\in T}\pi_v\right)\otimes\pi^T,
\qquad
p\pi\simeq\left(\bigotimes_{v\in T}\pi_v^{K_v}\right)\otimes p^T\pi^T.
\]

All factors on the right are nonzero, since \(p\pi\) contains \(w\). Thus

\[
\prod_{v\in T}\dim\pi_v^{K_v}\le D.
\]

There are at most \(\lfloor\log_2D\rfloor\) places outside \(S_0\) where the fixed space has dimension at least two: otherwise take \(T\) consisting of more such places. Enlarge \(S_0\) by this finite set. At each remaining place the fixed space is a line; choose a nonzero \(\xi_v\) on it. This argument uses admissibility and the algebraic tensor theorem alone.

For finite \(S\) containing \(S_0\) and all infinite places, put \(V_S=\pi^{K^S}\), where \(K^S=\prod_{v\notin S}K_v\). Averaging over \(K^S\) defines a projection \(P^S\); it is a finite sum on each smooth vector. Every tail algebra \(e_v\mathcal H_ve_v\) acts scalarly on \(e_v\pi\), because in \(\pi_v\otimes\pi^v\) it acts on the line \(e_v\pi_v\). Hence the compressed global algebra \(P^S\mathcal H P^S\) acts on \(V_S\) through the finite tensor algebra \(\mathcal H_S\), with scalar tail factors. If \(0\ne U\subset V_S\) is an \(\mathcal H_S\)-submodule, simplicity gives \(\mathcal H U=\pi\), and applying \(P^S\) gives \(\mathcal H_SU=V_S\). Thus \(V_S\) is simple. Repeated finite factorization gives \(V_S\simeq\bigotimes_{v\in S}\pi_v\); the factors agree with those already extracted, by projecting a nonzero embedded simple local module onto one of the copies of \(\pi_v\).

Enumerate the remaining places and add them one at a time. At a newly added place \(v\), the fixed subspace of the new finite tensor is the old tensor times \(\mathbb C\xi_v\), and \(V_{S\cup\{v\}}^{K_v}=V_S\). An isomorphism at the new stage therefore restricts to an isomorphism at the old stage. Its ratio with the old chosen isomorphism is a scalar, by the finite-corner Schur lemma proved in Lemma 3.2 of the prerequisite. Rescaling makes the two maps agree. Their direct limit is (1.2), since every vector is fixed by \(K^S\) for sufficiently large \(S\). Any operator acts at a sufficiently large finite stage, so the limit map respects the whole mixed action. Finally, restriction to one place is a direct sum of copies of its local factor; a nonzero coordinate projection between two such factorizations identifies their simple factors. This proves uniqueness. \(\square\)

Thus a vector is a finite sum of tensors \(\bigotimes_v x_v\), each of which equals a chosen spherical vector outside a finite set. The exceptional set can vary with the vector; the local representations themselves are fixed. The proof gives \(\dim\pi_v^{K_v}=1\) outside one finite set. Given the spherical classification formulated in the preceding lesson, the Hecke character on this line defines a Satake class \(c_v\). The general Satake proof obligations concern this identification, rather than the tensor factorization just proved.

Over a global function field the archimedean factor is absent. One works with smooth admissible representations occurring in the corresponding space of automorphic functions, and the same restricted factorization holds: omit the infinite-place algebra in the proof just given. The separate lesson *The function-field case: Drinfeld and L. Lafforgue* supplies the geometric formulation. We keep the number-field hypothesis below unless another field is specified.

### Fourier coefficients and global genericity for general linear groups

We now prove the existence of the Whittaker coefficients used in the next lesson. Put \(G=GL_n\), and let \(N=N_n\) be its upper unitriangular subgroup. Fix the nontrivial character \(\psi:F\backslash\mathbb A\to\mathbb C^\times\) and self-dual additive measures constructed in *Additive characters, self-dual measures and Poisson summation on the adèles*, Propositions 5.1–5.3 and Theorem 5.4. That theorem proves, in particular,

\[
\widehat{\mathbb A^m/F^m}=F^m,
\qquad x\longmapsto\psi(\xi x),\quad \xi\in F^m,
\qquad \operatorname{vol}(\mathbb A^m/F^m)=1.
\tag{1.3}
\]

Here \(x\) is a column, \(\xi\) a row, and \(\xi x\) their scalar product. On \(N\) use the character

\[
\psi_N(u)=\psi\left(\sum_{i=1}^{n-1}u_{i,i+1}\right).
\tag{1.4}
\]

Adjacent entries add under matrix multiplication, so (1.4) is a character. Each simple-root restriction is nontrivial at every place, by the local character construction in the same prerequisite. This is the meaning of a **nondegenerate** character here. All unipotent quotient measures below have total mass one. In upper triangular matrix coordinates, multiplication is triangular with diagonal Jacobian one. Product additive measures therefore give both left and right Haar measure. Successive vector-group quotients, each with the normalization (1.3), give the asserted quotient normalization.

**Lemma 1.2 (Fourier expansion on a compact adelic vector quotient).** Let \(h\) be a function on \(\mathbb A^m/F^m\), smooth in the entire real vector space \(F_\infty^m\), and invariant under translation by a compact open subgroup \(B\subset\mathbb A_f^m\). Then

\[
h(x)=\sum_{\xi\in F^m}\widehat h(\xi)\psi(\xi x),
\qquad
\widehat h(\xi)=\int_{\mathbb A^m/F^m}h(y)\psi(-\xi y)\,dy.
\tag{1.5}
\]

The series converges absolutely and uniformly, together with every archimedean derivative. For a smooth family with one such \(B\) and uniformly bounded derivatives on a compact parameter set, the convergence is uniform on that set as well. In particular, a nonzero \(h\) has a nonzero Fourier coefficient.

**Proof.** Shrinking \(B\) if necessary, take it to be a product of local additive lattices. The additive approximation proof in *The adèle ring of a number field*, Theorem 2.3, projected from a quotient omitting one infinite place onto the finite adèles, gives \(\mathbb A_f^m=F^m+B\). More explicitly, clear the finitely many denominators of the prescribed finite coordinates, solve the finitely many resulting integral congruences by Chinese remainders, and divide by the chosen denominator. Thus

\[
\mathbb A^m/(F^m+B)\simeq F_\infty^m/L,
\qquad L=\{a\in F^m:a_f\in B\}.
\]

For some positive integer \(M\), the lattice \(L\) lies between \(M\mathcal O_F^m\) and \(M^{-1}\mathcal O_F^m\). The integral-basis and Minkowski-lattice calculation in the same adèle lesson, equations (10)–(14) and Proposition 2.4, shows that \(L\) is a full lattice in the real space of dimension \(d=m[F:\mathbb Q]\). The displayed map is a topological isomorphism: it is a continuous bijection from a compact torus to a Hausdorff quotient. Both sides carry their probability Haar measure.

Translation by \(b\in B\) in the coefficient integral shows that \(\widehat h(\xi)=0\) unless \(\psi(\xi b)=1\) for all \(b\in B\). By (1.3), the remaining characters are exactly the characters of this real torus. In real linear coordinates their frequency vectors form the dual lattice \(L^*\). Integration by parts on a fundamental parallelepiped, with opposite boundary faces cancelling by periodicity, gives

\[
|\widehat h(\lambda)|
\le C_j(1+4\pi^2\|\lambda\|^2)^{-j}
\quad(\lambda\in L^*)
\]

by applying \((1-\Delta)^j\) to \(h\). A full lattice has \(O((1+R)^d)\) points in a ball of radius \(R\), by comparison with \(\mathbb Z^d\). Taking \(2j>d\) proves absolute uniform convergence. Taking larger \(j\) absorbs the polynomial frequency factors introduced by any prescribed derivative. The same estimates are uniform for the stated families.

For completeness, these coefficients reconstruct the function, rather than just a convergent series. Periodize a real Gaussian of mass one over \(L\), normalizing the kernel to have integral one on the torus. The Poisson formula proved in *Additive characters, self-dual measures and Poisson summation on the adèles*, Theorem 5.5, applied to that whole-space Gaussian times \(\mathbf1_B\), gives its Fourier series with coefficients \(e^{-4\pi^2t\|\lambda\|^2}\), for \(t>0\). The normalization agrees because the additive covolume is one. These nonnegative kernels form an approximate identity: their mass outside any fixed torus neighbourhood of zero tends to zero by Gaussian tail decay. Convolution with \(h\) therefore tends uniformly to \(h\). Absolute convergence permits termwise convolution, and dominated convergence in the already absolutely summable coefficient series proves (1.5). This also proves the nonvanishing assertion. \(\square\)

**Theorem 1.3 (global cuspidal genericity for \(GL_n\)).** Let \(F\) be any number field and \(n\ge1\). Suppose \(f\ne0\) is a smooth cuspidal function on \(GL_n(F)\backslash GL_n(\mathbb A)\), right invariant under a compact open subgroup at the finite places. Then its Whittaker transform

\[
W_f(g)=\int_{N(F)\backslash N(\mathbb A)}
f(ug)\psi_N(u)^{-1}\,du
\tag{1.6}
\]

is not identically zero. No growth assumption or square-integrability assumption is needed for this conclusion. In particular, the Whittaker transform is injective on the space of such cuspidal functions, and is nonzero on every nonzero cuspidal module realized in that space.

*Reference:* [Getz–Hahn 2022, Theorem 11.3.3] states the stronger full Whittaker expansion. We prove the existence assertion in all ranks directly.

**Proof.** For \(1\le r\le n\), let

\[
H_r=\left\{\begin{pmatrix}I_r&X\\0&u\end{pmatrix}:
u\in N_{n-r}\right\},
\qquad
\psi_r(h)=\psi\left(\sum_{i=r}^{n-1}h_{i,i+1}\right),
\]

and define

\[
C_r(g)=\int_{H_r(F)\backslash H_r(\mathbb A)}
f(hg)\psi_r(h)^{-1}\,dh.
\tag{1.7}
\]

The empty sums and trivial groups give \(C_n=f\) and \(C_1=W_f\). Lemma 1.0 makes every integration domain compact. Thus these integrals converge absolutely and define smooth functions; differentiation is justified by boundedness of each derivative on compact representative sets.

For \(r\ge2\), put

\[
v_r(x)=I_n+\sum_{i=1}^{r-1}x_iE_{i,r},
\qquad V_r=\{v_r(x):x\in\mathbb A^{r-1}\}.
\]

This is the vector subgroup in the mirabolic group of the leading \(r\times r\) block. It normalizes \(H_r\) and preserves \(\psi_r\): conjugation leaves its \((r,r+1)\) entry and all later adjacent entries unchanged. Consequently \(x\mapsto C_r(v_r(x)g)\) is periodic modulo \(F^{r-1}\), by left \(GL_n(F)\)-invariance of \(f\) and a change of variable in \(H_r\).

This periodic function satisfies exactly the hypotheses of Lemma 1.2. Indeed, if \(U\subset GL_n(\mathbb A_f)\) fixes \(f\), choose a compact open additive \(B_g\) with \(g_f^{-1}v_r(B_g)g_f\subset U\). Then right \(U\)-invariance gives invariance under \(x\mapsto x+b\), independently of the integration variable \(h\). A compact set of \(g\)'s admits one common \(B_g\), by continuity of conjugation and a finite subcover. Compact representative sets for \(H_r\) and the vector quotient bound all archimedean derivatives uniformly on that set. Hence the Fourier expansion at this stage is absolutely and locally uniformly convergent, with derivatives. Write its coefficients as

\[
C_{r,\xi}(g)=\int_{F^{r-1}\backslash\mathbb A^{r-1}}
C_r(v_r(x)g)\psi(-\xi x)\,dx.
\tag{1.8}
\]

We require two quotient integration identities. The multiplication map gives \(H_{r-1}=H_r\rtimes V_r\). More generally, put \(R_{r-1}\) equal to the unipotent radical of the two-block parabolic of type \((r-1,n-r+1)\). Then

\[
H_{r-1}=R_{r-1}\rtimes
\operatorname{diag}(I_{r-1},N_{n-r+1}).
\tag{1.9}
\]

In either decomposition the action on the normal factor has Jacobian one: it is triangular unipotent on its matrix coordinates. Choose measurable additive fundamental domains, and build fundamental domains for the normal factor by its successive vector-group decompositions. A representative for the quotient of a semidirect product is then \(hv\), with \(v\) in the outer fundamental domain and \(h\) in the inner one. To verify this, first reduce the projection of an arbitrary element by a rational \(v_0\), and then reduce its remaining normal component by a rational \(h_0\). Uniqueness holds away from the chosen boundary sets; conjugation by a rational outer element preserves the inner Haar measure. The coordinate product therefore gives the quotient integral as the iterated integral, with no scaling factor. Compactness makes absolute Fubini applicable to every integrand used here, including the characters.

The coefficient \(C_{r,0}\) is zero. Using the first decomposition, it is the integral over \(H_{r-1}\) weighted by the character \(\psi_r\) extended trivially across \(V_r\). In the second decomposition this character is trivial on \(R_{r-1}\) and equals the standard character on the trailing \(N_{n-r+1}\). The inner integral is therefore

\[
\int_{R_{r-1}(F)\backslash R_{r-1}(\mathbb A)}
f(a t g)\,da=0
\]

by cuspidality for that proper two-block parabolic. This proves \(C_{r,0}=0\) for every \(r\ge2\), including \(r=n\).

Now assume \(C_r\) is not identically zero. Choose \(g\) with \(C_r(g)\ne0\). Its periodic vector-group function is nonzero at zero, so Lemma 1.2 supplies a nonzero coefficient \(C_{r,\xi}(g)\). The zero coefficient vanishes, so \(\xi\ne0\). The group \(GL_{r-1}(F)\) acts transitively on nonzero row vectors: extend any such row to a basis to obtain a matrix \(a\) whose last row is \(\xi\). Write \(A_a=\operatorname{diag}(a,1,I_{n-r})\), and let \(e\) be the last coordinate row in \(F^{r-1}\).

Conjugation by \(A_a\) preserves \(H_r\) and \(\psi_r\). On its rectangular \(X\)-block the determinant is \((\det a)^{n-r}\); on the trailing unitriangular block it is the identity. The product formula proved in *Places of number fields in extensions and the product formula*, Theorem 5.2 therefore makes its adelic Jacobian one. Thus \(C_r(A_a z)=C_r(z)\). Since \(v_r(x)A_a=A_a v_r(a^{-1}x)\), the substitution \(x=ay\), again of adelic Jacobian one, gives

\[
C_{r,e}(A_a g)=C_{r,ea}(g)=C_{r,\xi}(g)\ne0.
\tag{1.10}
\]

The coefficient \(C_{r,e}\) is exactly \(C_{r-1}\): in the first decomposition above, its new character is \(\psi(x_{r-1})\), and together with \(\psi_r\) this is \(\psi_{r-1}\). The quotient Fubini identity proves the equality, with the normalizations already fixed. Hence nonvanishing at stage \(r\) implies nonvanishing at stage \(r-1\).

Start with \(C_n=f\ne0\) and repeat this finite argument through \(r=2\). It yields \(C_1=W_f\ne0\), for every \(n\). For \(n=1\) the integral is simply \(f\). Each stage uses one absolutely convergent Fourier expansion; no rearrangement of an infinite iterated sum is involved.

The same conclusion holds for every nondegenerate character of \(N(\mathbb A)\) trivial on \(N(F)\). Such a character has compact image by Lemma 1.0, hence is unitary: its modulus is a compact subgroup of \(\mathbb R_{>0}\), which can only be \(\{1\}\). The adjacent entries identify the abelianization of \(N\) with \(\mathbf G_a^{n-1}\): a non-adjacent elementary root group is a commutator, since \([I+aE_{ij},I+bE_{jk}]=I+abE_{ik}\) for \(i<j<k\). Equation (1.3) then writes any such character as \(\psi(\sum_i m_i u_{i,i+1})\), with \(m_i\in F\); nondegeneracy means all \(m_i\ne0\). Choose \(t=\operatorname{diag}(t_1,\ldots,t_n)\in GL_n(F)\) with \(t_n=1\) and \(t_i/t_{i+1}=m_i\). Conjugation and the product formula give \(W_{f,\psi_m}(g)=W_{f,\psi_N}(tg)\), so it too is nonzero. Any \(F\)-rational complete flag has an \(F\)-basis, giving the same assertion for its Borel subgroup. \(\square\)

**Corollary 1.4 (local existence from a cuspidal smooth realization).** Let \(\pi\) be an irreducible admissible cuspidal module as in Theorem 1.1, with a smooth cuspidal realization \(V\). Precisely, \(V\) carries the full right \(GL_n(\mathbb A)\)-action; at each fixed finite level it is a Fréchet smooth representation of moderate growth, its inclusion in the space of smooth automorphic functions is continuous for uniform convergence of every derivative on compact sets, and its \(K_\infty\)-finite core is \(\pi\). Differentiation and compact averaging are continuous in this topology. Then every local component \(\pi_v\) has a nonzero \(\psi_{N,v}\)-Whittaker functional. At a finite place this is a linear functional on its smooth module; at an infinite place it is continuous on a Fréchet smooth local realization of moderate growth with Harish-Chandra core \(\pi_v\).

**Proof.** The functional

\[
\Lambda(f)=W_f(1)
\]

is continuous on each finite level: the compact representative set for \(N(F)\backslash N(\mathbb A)\) bounds its absolute value by a compact supremum seminorm. Right invariance of quotient measure and the character identity give

\[
\Lambda(R(u)f)=\psi_N(u)\Lambda(f),\qquad u\in N(\mathbb A).
\]

Theorem 1.3 supplies \(f\in\pi\) and \(g\) with \(W_f(g)\ne0\). The smooth vector \(R(g)f\in V\) therefore has nonzero \(\Lambda\).

We first ensure that \(\Lambda\) is nonzero on the mixed core itself. At fixed finite level that core is dense. Here is the topological argument: choose continuous probability kernels on \(K_\infty\) supported in shrinking identity neighbourhoods. Their averages tend to a given vector in every seminorm, by continuity of its compact orbit. Approximate each kernel uniformly by a finite sum of matrix coefficients, using *Matrix coefficients and the Peter–Weyl theorem*, Theorem 4.1. The convolution error in a seminorm \(p\) is at most the uniform kernel error times \(\sup_{k\in K_\infty}p(R(k)f)\). Those finite-coefficient averages are \(K_\infty\)-finite and belong to the same finite level. Taking successive approximations for finitely many seminorms proves density. Continuity of \(\Lambda\) now makes its restriction to \(\pi\) nonzero.

Apply the actual factorization (1.2), and write a vector with nonzero \(\Lambda\) as a finite sum of pure restricted tensors. At least one pure tensor \(x=\bigotimes_w x_w\) has \(\Lambda(x)\ne0\). For a finite \(v\), fixing all the other factors gives

\[
\lambda_v(y)=\Lambda\left(y\otimes\bigotimes_{w\ne v}x_w\right),
\qquad y\in\pi_v.
\]

It is nonzero and satisfies \(\lambda_v(\pi_v(u)y)=\psi_{N,v}(u)\lambda_v(y)\), since this is a single-place instance of the displayed global equivariance. With the locally convex direct-limit topology on the smooth admissible module, it is continuous: every compact-open fixed space is finite dimensional, and its restriction there is continuous. This argument uses existence of a nonzero tensor value, and uses no local uniqueness theorem.

At an infinite \(v\), an algebraic tensor alone would not justify continuity or the full \(N(F_v)\)-action. We construct the required smooth local realization inside \(V\). In every other factor choose a local-unit projection fixing \(x_w\): a compact-open average at finite places, and a finite compact-type projection at other infinite places. Outside a finite set use the tail \(K_w\)-averages. Denote their product by \(e^{v}\). It is a continuous projection on \(V\), commuting with \(GL_n(F_v)\), and (1.2) identifies its mixed core with

\[
e^{v}\pi=\pi_v\otimes T,
\qquad
T=\bigotimes_{w\ne v}e_w\pi_w.
\]

The tensor on the right is finite dimensional: each active corner is finite dimensional by local admissibility, and each tail corner is the fixed line proved in Theorem 1.1. It contains \(t=\bigotimes_{w\ne v}x_w\ne0\). The finite interpolation lemma and corner argument in *Restricted tensor products and the tensor product theorem*, Lemmas 3.1–3.2 and Theorem 4.1 identify the image of the other-place corner algebra with \(\operatorname{End}(T)\). Choose in it a rank-one idempotent with image \(\mathbb Ct\) fixing \(t\), and represent it by an operator \(Q=e^{v}Qe^{v}\) using those other-place algebras.

Finite-place convolutions, compact-type projections and finite-order differential operators at the other infinite places are continuous on \(V\). Thus \(Q\) is continuous and commutes with the full group at \(v\). Its identity \(Q^2=Q\), known on the dense mixed core, holds on \(V\). Its image \(V_v=QV\) is closed in the complete fixed-finite-level space containing it, is invariant under \(GL_n(F_v)\), and has \(K_v\)-finite core exactly \(\pi_v\otimes\mathbb Ct\). Indeed, the other compact projections and finite averages already impose all remaining compact types and finite levels, so a \(K_v\)-finite vector in the image is a global mixed-core vector. Compact averaging as above makes this local core dense in \(V_v\).

The image inherits smoothness and moderate growth under the group at \(v\), with its closed-subspace Fréchet topology. This local realization is irreducible: a nonzero closed invariant subspace contains a nonzero compact-finite vector by the same approximation argument; its core is stable under the local Lie algebra and compact group, so simplicity of \(\pi_v\) gives the entire core, and density gives \(V_v\). The restriction \(\lambda_v=\Lambda|_{V_v}\) is continuous, is nonzero at \(x_v\otimes t\), and has the required \(N(F_v)\)-equivariance. This proves local existence also at infinity. \(\square\)

Theorem 1.3 applies to cuspidal functions themselves, regardless of whether a Hilbert realization has been constructed. Corollary 1.4 makes the smooth-realization hypothesis explicit when passing to continuous archimedean functionals. It does not establish the general algebraic/Hilbert comparison mentioned at the start of the section. Local Whittaker uniqueness is a further theorem; it is not needed for the existence proof just given.

## 2. Partial Euler products and a convergence proof

Choose a finite Galois quotient \(\Gamma\) through which the pinned action on \(\widehat G\) factors. For this lesson a representation of the global L-group means

\[
r:\widehat G\rtimes\Gamma\longrightarrow GL(V),
\tag{2.1}
\]

finite-dimensional over \(\mathbb C\) and algebraic on \(\widehat G\). Enlarging \(\Gamma\) permits additional finite Galois data. This hypothesis prevents an arbitrary representation of an unrestricted global Weil group from silently entering the convergence statement.

Let \(S\) contain the archimedean places and all places where \(G\), \(\pi\), or the Galois data in \(r\) are ramified. At \(v\notin S\), write \(c_v=(g_v,\operatorname{Fr}_v)\) for the unramified Satake class in the relevant Frobenius coset. Its equivalence is twisted conjugacy when the group is nonsplit. Set

\[
L_v(s,\pi,r)=\det\bigl(1-q_v^{-s}r(c_v)\mid V\bigr)^{-1},
\qquad
L^S(s,\pi,r)=\prod_{v\notin S}L_v(s,\pi,r).
\tag{2.2}
\]

Here \(q_v\) is the residue-field cardinality and \(q_v^{-s}=\exp(-s\log q_v)\). Conjugating \(c_v\) conjugates its image under \(r\), so the determinant is well defined. The normalized Satake convention is the one fixed in the preceding lesson: for an unramified character \(\chi\) of \(GL_1(F_v)\), its parameter is \(\chi(\varpi_v)\).

Direct sums and tensor products can be read directly from eigenvalues. In particular,

\[
L_v(s,\pi,r_1\oplus r_2)
=L_v(s,\pi,r_1)L_v(s,\pi,r_2).
\tag{2.3}
\]

For \(G=GL_n\) and the standard representation, a representative is

\[
c_v=\operatorname{diag}(\alpha_{1,v},\ldots,\alpha_{n,v}),
\qquad
L_v(s,\pi)=\prod_{i=1}^n(1-\alpha_{i,v}q_v^{-s})^{-1}.
\tag{2.4}
\]

The parameters are unordered and nonzero. No choice of ordering enters the product.

We first isolate the elementary estimate on the places. Put \(d=[F:\mathbb Q]\). Above a rational prime \(p\) there are at most \(d\) places, each with \(q_v=p^{f_v}\), \(f_v\ge1\). Hence, for real \(t>1\),

\[
\sum_{v\nmid\infty}q_v^{-t}
\le d\sum_p p^{-t}
\le d\sum_{m=2}^{\infty}m^{-t}<\infty.
\tag{2.5}
\]

This also shows that there are finitely many places of bounded norm.

**Proposition 2.1 (a uniform Euler-product criterion).** Suppose that at every \(v\notin S\) a local factor has the form

\[
L_v(s)=\prod_{j=1}^{D}(1-\beta_{j,v}q_v^{-s})^{-1},
\qquad |\beta_{j,v}|\le q_v^A
\tag{2.6}
\]

for a fixed real \(A\) and fixed integer \(D\). Then the Euler product converges absolutely and locally uniformly on \(\operatorname{Re}s>1+A\). It is holomorphic and has no zeros there. Its expansion as a Dirichlet series indexed by integral ideals also converges absolutely in this half-plane.

**Proof.** Fix \(\sigma_0>1+A\) and put \(t=\sigma_0-A>1\). On \(\operatorname{Re}s\ge\sigma_0\),

\[
|\beta_{j,v}q_v^{-s}|\le q_v^{-t}\le2^{-t}<1.
\]

Use the power series \(-\log(1-z)=\sum_{m\ge1}z^m/m\), with the branch that is zero at \(z=0\). The absolute sum of the proposed logarithms is bounded by

\[
\begin{aligned}
\sum_{v\notin S}\sum_{j=1}^{D}\sum_{m\ge1}
\frac{|\beta_{j,v}|^m q_v^{-m\sigma_0}}{m}
&\le D\sum_v\sum_{m\ge1}q_v^{-mt}\\
&\le\frac{D}{1-2^{-t}}\sum_v q_v^{-t}<\infty.
\end{aligned}
\tag{2.7}
\]

The bound is uniform in the closed half-plane. In particular the logarithm series converges locally uniformly and defines a holomorphic function there. Its exponential agrees with finite Euler products in the limit, is holomorphic, and is never zero. Since every compact subset of \(\operatorname{Re}s>1+A\) lies in one such closed half-plane, this proves the assertion throughout that open region.

For the Dirichlet-series assertion, expand each factor geometrically. The sum of the absolute values of all resulting monomials is at most

\[
\prod_{v\notin S}\prod_{j=1}^{D}
(1-|\beta_{j,v}|q_v^{-\sigma_0})^{-1}<\infty.
\]

Unique factorization of integral ideals groups the monomials by ideal. The displayed positive majorant justifies that grouping and bounds the resulting absolute Dirichlet series. This proves the last assertion. \(\square\)

**Corollary 2.2 (the assigned convergence bound for \(GL_n\)).** If

\[
|\alpha_{i,v}|\le q_v^\theta
\quad\text{for every }v\notin S\text{ and }1\le i\le n,
\tag{2.8}
\]

with a fixed \(\theta<1/2\), then \(L^S(s,\pi)\) converges absolutely and is holomorphic and nonvanishing for \(\operatorname{Re}s>1+\theta\).

**Proof.** Apply Proposition 2.1 with \(D=n\), \(A=\theta\), and the factors (2.4). \(\square\)

The proof itself works for any real \(\theta\). The condition \(\theta<1/2\) expresses the useful strength of the assumed automorphic bound, rather than a restriction in the elementary estimate. If the bound has an extra fixed constant \(C\ge1\), replacing \(A\) by \(A+\log_2 C\) absorbs it because \(q_v\ge2\).

**Theorem 2.3 (Langlands; statement with proof not yet supplied).** Let \(G\) be a connected reductive group over a number field, and let \(\pi\) be an irreducible unitary admissible representation of \(G(\mathbb A)\), unramified at almost every place. For \(r\) as in (2.1) and \(S\) as above, \(L^S(s,\pi,r)\) converges absolutely when \(\operatorname{Re}s\) is sufficiently large. The statement is recorded in the [Getz–Hahn author draft, §12.7, p.300](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf); the split-group argument appears in [Langlands's free IAS text, *Euler Products*, §§2–3](https://publications.ias.edu/sites/default/files/euler-products_rpl_2.pdf). The missing step here is a uniform polynomial bound on the spherical parameters for every such group. Proposition 2.1 proves convergence whenever that bound has been established. The computations below require only its explicitly stated bound hypotheses.

**Lemma 2.4 (a proved convergence bound for general linear groups).** For fixed \(n\), let \(\pi_v\) be a unitary spherical representation of \(GL_n(F_v)\), with Satake roots \(\alpha_{i,v}\). Put \(C_n=n^2+1\). Then

\[
|\alpha_{i,v}|\le q_v^{C_n},\qquad
|\alpha_{i,v}|^{-1}\le q_v^{(n-1)C_n}.
\]

Consequently, for any fixed algebraic representation \(r\) of \(GL_n(\mathbb C)\), the corresponding good-place Euler product converges absolutely and is nonzero in a right half-plane.

**Proof.** Give \(K_v=GL_n(\mathcal O_v)\) volume one. For \(1\le j\le n\), let \(T_j\) be the characteristic function of \(K_v\operatorname{diag}(\varpi_v I_j,I_{n-j})K_v\). Its right cosets correspond to lattices between \(\varpi_v\mathcal O_v^n\) and \(\mathcal O_v^n\), whose reductions are \((n-j)\)-dimensional subspaces of \(k_v^n\). Every such subspace has a spanning list of at most \(n\) vectors, so there are at most \(q_v^{n^2}\) of them. A unitary action therefore gives

\[
\|\pi_v(T_j)\|\le\int T_j(g)\,dg\le q_v^{n^2}.
\]

The general-linear decomposition and triangular Satake transform were proved in *The Satake isomorphism for unramified groups and unramified L-factors*, Proposition 1.1 and §4. For the dominant cocharacter \((1^j,0^{n-j})\), there is no smaller dominant integral cocharacter of the same coordinate sum: dominance forces the largest coordinate to be at most one and the smallest to be at least zero. Thus its transform has only its Weyl orbit, with leading coefficient \(q_v^{j(n-j)/2}\). Its scalar action is consequently \(q_v^{j(n-j)/2}e_j(\alpha_v)\). The norm bound implies \(|e_j(\alpha_v)|\le q_v^{n^2}\).

The roots \(\alpha_i\) satisfy the monic polynomial with coefficients \((-1)^je_j\). If those coefficients have absolute value at most \(M\) and \(|z|>1+M\), then

\[
M\sum_{j=1}^n|z|^{n-j}
=M\frac{|z|^n-1}{|z|-1}<|z|^n;
\]

such a \(z\) cannot be a root. Hence \(|\alpha_i|\le1+q_v^{n^2}\le q_v^{C_n}\). The scalar central double coset \(\varpi_v I_n\) acts unitarily and has transform \(e_n\), so \(|\prod_i\alpha_i|=1\). It follows that \(|\alpha_i|^{-1}=\prod_{h\ne i}|\alpha_h|\le q_v^{(n-1)C_n}\).

Restrict \(r\) to the diagonal torus. Every eigenvalue of \(r(c_v)\) is a Laurent monomial \(\prod_i\alpha_{i,v}^{m_i}\) from a finite weight list. Its absolute value is at most

\[
q_v^{C_n\left(\sum_{m_i\ge0}m_i+(n-1)\sum_{m_i<0}(-m_i)\right)}.
\]

Take the largest exponent over that list and apply Proposition 2.1. This proves the assertion, without the sharper bound that follows. \(\square\)

A particularly useful sharper bound for a **unitary cuspidal** representation of \(GL_n(\mathbb A)\) is the Jacquet–Shalika bound

\[
q_v^{-1/2}<|\alpha_{i,v}|<q_v^{1/2}
\quad(v\notin S).
\tag{2.9}
\]

The strict bound is recorded in [Sarnak's free notes, §1, equation (12), p.664](https://publications.ias.edu/sites/default/files/FieldNotesCurrent.pdf). Its proof is not supplied at this point. The next lesson gives a positivity proof conditional on the complete Rankin–Selberg continuation and pole theorem. Here the deduction is conditional on (2.9): Proposition 2.1 with \(A=1/2\) gives convergence and nonvanishing for \(\operatorname{Re}s>3/2\). Strict inequalities at individual places do not supply a single improved exponent \(\theta<1/2\) uniformly over all places. For example, the purely numerical sequence \(q^{1/2-1/\log q}=e^{-1}q^{1/2}\) satisfies the strict upper inequality but eventually exceeds \(q^\theta\) for every fixed \(\theta<1/2\). Nor does (2.7) establish convergence on the boundary line \(\operatorname{Re}s=3/2\).

There is also an elementary extension to an arbitrary algebraic representation \(r\) of \(GL_n(\mathbb C)\), with trivial Galois action. Restrict \(r\) to the diagonal torus. Its finitely many weights are monomials

\[
(z_1,\ldots,z_n)\longmapsto z_1^{m_1}\cdots z_n^{m_n},
\qquad m_i\in\mathbb Z.
\]

Assuming both inequalities in (2.9), the corresponding eigenvalue has absolute value at most \(q_v^{\frac12\sum_i|m_i|}\). Taking the largest of these finitely many exponents and applying Proposition 2.1 proves convergence in a right half-plane for this \(r\). Negative weights explain why a lower bound on \(|\alpha_{i,v}|\) is needed for this argument.

## 3. What the analytic conjecture asks for

The partial product only uses spherical representations. To complete it, one needs local data at every place. Suppose that local Langlands parameters for \(\pi_v\) are available, with the usual relevance and admissibility conditions, and compose them with \(r\). At a finite place the resulting Weil–Deligne representation is a pair \((\rho_v,N_v)\) on \(V\). Its local factor is

\[
L_v(s,\pi,r)
=\det\left(1-q_v^{-s}\rho_v(\operatorname{Fr}_v)
\mid (\ker N_v)^{I_v}\right)^{-1}.
\tag{3.1}
\]

The Frobenius and reciprocity convention must match the unramified convention in (2.2). Frobenius preserves this invariant subspace, and changing its lift by inertia does not change the operator on that subspace. At an unramified place \(N_v=0\), and (3.1) recovers (2.2). Ramification can change the dimension of the space in (3.1); it cannot in general be handled by applying the full unramified determinant to an arbitrary matrix.

At the archimedean places, the parameters give gamma factors. Write

\[
\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2),
\qquad
\Gamma_{\mathbb C}(s)=2(2\pi)^{-s}\Gamma(s).
\tag{3.2}
\]

Let \(L_{\mathrm{all}}(s,\pi,r)=\prod_v L_v(s,\pi,r)\), including these factors, initially in a right half-plane. Local epsilon factors require a nontrivial additive character \(\psi:F\backslash\mathbb A\to\mathbb C^\times\) and compatible measures. Their product is denoted \(\varepsilon(s,\pi,r)\). The dual local data are \((r\circ\phi_v)^\vee\); equivalently one may keep \(\pi\) and replace \(r\) by its dual \(r^\vee\). For the standard representation of \(GL_n\) they are the data of the contragredient \(\widetilde\pi\).

**Conjecture 3.1 (analytic properties of automorphic L-functions).** For automorphic \(\pi\) and the L-group representation \(r\) under consideration, the complete local factors should define a meromorphic function on \(\mathbb C\), satisfy appropriate bounds in vertical strips away from poles, and obey

\[
L_{\mathrm{all}}(s,\pi,r)
=\varepsilon(s,\pi,r)
L_{\mathrm{all}}(1-s,\pi,r^\vee).
\tag{3.3}
\]

This is the parameter-dual formulation of [Langlands 1970, §7, Questions 1 and 4] and [Getz–Hahn 2022, Conjecture 12.7.1]. The latter uses the contragredient formulation, together with the expected compatibility of local correspondence and duality. The meaning of a strip bound includes excluding neighborhoods of poles, or removing the specified poles first. A meromorphic function with a pole is never bounded on a strip containing that pole without such a qualification.

In the unitary cases where the global epsilon factor has the form

\[
\varepsilon(s,\pi,r)=W(\pi,r)A(\pi,r)^{1/2-s},
\qquad A(\pi,r)>0,
\]

one can instead use \(\Lambda(s,\pi,r)=A(\pi,r)^{s/2}L_{\mathrm{all}}(s,\pi,r)\). The dual has the same conductor, and (3.3) becomes

\[
\Lambda(s,\pi,r)=W(\pi,r)\Lambda(1-s,\pi,r^\vee).
\tag{3.4}
\]

This moves the conductor power from the functional equation into the completed function. The two conventions should not be mixed.

Cuspidality does not predict entireness for every \(r\). The trivial representation of the L-group already gives a zeta factor, and tensor products with contragredients have an invariant line. A claim of entireness must exclude or account for these phenomena. Likewise, a functional equation for a complete L-function does not imply the same functional equation for \(L^S\): the missing finite and archimedean factors intervene.

## 4. Three methods and the cases they reach

The methods below construct special integrals or operators whose unramified computations produce the determinants in (2.2). Their analytic continuation then supplies information that the Euler product alone cannot provide. We state their precise analytic conclusions below. Their general proofs are not yet supplied here; the determinant calculations are separate algebraic assertions.

### 4.1 Rankin–Selberg integrals

For general linear groups, the nonzero Whittaker coefficients proved in Theorem 1.3 lead to integral representations for the tensor-product L-function of \(\pi\) on \(GL_n\) and \(\pi'\) on \(GL_m\). If their parameters at \(v\) are \(\alpha_{i,v}\) and \(\beta_{j,v}\), respectively, the unramified computation gives

\[
L_v(s,\pi\times\pi')
=\prod_{i=1}^n\prod_{j=1}^m
(1-\alpha_{i,v}\beta_{j,v}q_v^{-s})^{-1}.
\tag{4.1}
\]

Corollary 1.4 supplies local Whittaker existence in a cuspidal smooth realization. One unfolds the global integral, factors it into local integrals by the further theorem of uniqueness of Whittaker models, and uses an Eisenstein-series functional equation in the equal-rank case. The ramified local theory is part of the construction, not inferred from (4.1).

**Theorem 4.1 (Jacquet–Shalika, 1981; Jacquet–Piatetski-Shapiro–Shalika, 1983; statement with proof not yet supplied).** Let \(\pi\) and \(\pi'\) be cuspidal automorphic representations of \(GL_n(\mathbb A_F)\) and \(GL_m(\mathbb A_F)\), normalized to be trivial on the connected positive real split central subgroups \(A_{GL_n}\) and \(A_{GL_m}\). Their complete Rankin–Selberg L-function has meromorphic continuation, and the functional equation relating it to \(\widetilde\pi\times\widetilde{\pi'}\). It is entire unless \(m=n\) and \(\pi'\simeq\widetilde\pi\); in that exceptional case its only poles are simple poles at \(0\) and \(1\). We use [Getz–Hahn 2022, Theorem 11.7.1], with the normalization stipulated at the start of that section. Without this normalization, imaginary norm twists can shift the exceptional poles. The next lesson states the unrestricted form and examines the standard L-function.

### 4.2 Doubling integrals

**Theorem 4.2 (Cai–Friedberg–Ginzburg–Kaplan, 2018; statement with proof not yet supplied).** For a number field, \(G=Sp_{2n}\) or split \(SO_{2n}\), a cuspidal automorphic \(\pi\) on \(G(\mathbb A)\), and a cuspidal automorphic \(\tau\) on \(GL_k(\mathbb A)\), generalized doubling integrals represent the partial standard tensor-product L-function and give its meromorphic continuation. Global genericity of \(\pi\) is unnecessary. This is [Cai–Friedberg–Ginzburg–Kaplan, Theorem A, (3.1), Theorems 29–30].

The integral uses an Eisenstein series on a larger group and two cusp forms on two copies of \(G\). Here is its full spherical normalization. Put

\[
(a,\delta_G)=
\begin{cases}
(2kn+1,1),&G=Sp_{2n},\\
(2kn-1,0),&G=SO_{2n}\text{ split}.
\end{cases}
\]

At the local place, assume \(\pi_v\) irreducible and unramified, and \(\tau_v\) an unramified twist of an irreducible unitary generic unramified representation. Take the spherical matrix coefficient of \(\pi_v^\vee\) and the spherical section both with value \(1\) at the identity. Extend the section in the convention \(\operatorname{Ind}_{P}^{H}(W_c(\tau_v)\delta_P^s)\), where \(\delta_P\) is the parabolic modulus and \(W_c(\tau_v)\) is the inducing model used in the construction. In this variable, [Cai–Friedberg–Ginzburg–Kaplan, **arXiv version 2**, §3.5, Theorem 29, pp.29–30] gives

\[
\begin{aligned}
Z_v(s)&=\frac{L_v(as+1/2,\pi_v\times\tau_v)}{D_v(s,\tau_v)},\\
D_v(s,\tau_v)&=L_v(as+n+1/2,\tau_v)^{\delta_G}\\
&\quad\cdot\prod_{j=1}^{n}
L_v(2as+2j,\tau_v,\wedge^2)
L_v(2as+2j-1,\tau_v,\operatorname{Sym}^2).
\end{aligned}
\]

All the shifts and the indicator matter. For roots \(b_1,\ldots,b_k\) of \(\tau_v\), the three types of factor are respectively

\[
\begin{aligned}
L_v(t,\tau_v)&=\prod_i(1-b_iq_v^{-t})^{-1},\\
L_v(t,\tau_v,\wedge^2)&=\prod_{i<h}(1-b_ib_hq_v^{-t})^{-1},\\
L_v(t,\tau_v,\operatorname{Sym}^2)&=\prod_{i\leq h}(1-b_ib_hq_v^{-t})^{-1}.
\end{aligned}
\]

The last two formulas follow from the bases \(e_i\wedge e_h\), \(i<h\), and \(e_ie_h\), \(i\leq h\): their eigenvalues are \(b_ib_h\). Thus diagonal symmetric factors remain even when the exterior square is zero-dimensional. For \(n=k=1\), \(G=Sp_2\), and \(\tau_v=1\), we have \(a=3\), \(\delta_G=1\) and

\[
\begin{aligned}
D_v(s,1)&=(1-q_v^{-3s-3/2})^{-1}(1-q_v^{-6s-1})^{-1},\\
Z_v(s)&=L_v(3s+1/2,\pi_v)
(1-q_v^{-3s-3/2})(1-q_v^{-6s-1}).
\end{aligned}
\]

Here the exterior-square product is empty and the dual standard representation has dimension \(3\). The two extra factors depend on \(s\). Representing an L-function therefore includes these normalizing factors and the displayed change of variable. [Cai–Friedberg–Ginzburg–Kaplan, v2](https://arxiv.org/abs/1710.00905v2).

### 4.3 The Langlands–Shahidi method

Let \(H\) be a quasi-split connected reductive group over \(F\), and \(P=MN\) a maximal \(F\)-parabolic. On the dual side, the adjoint action of \({}^LM\) on the Lie algebra of the dual unipotent radical decomposes as

\[
\operatorname{Ad}|_{\operatorname{Lie}\widehat N}
=r_1\oplus\cdots\oplus r_t.
\tag{4.2}
\]

These particular representations \(r_i\) are the ones the method produces. Starting from a globally generic cuspidal representation \(\sigma\) of \(M(\mathbb A)\), one forms Eisenstein series on \(H\). Constant terms involve intertwining operators. Comparing Whittaker functionals before and after these operators produces local coefficients, and from them local gamma, L- and epsilon factors. The global comparison separates the factors corresponding to (4.2).

**Theorem 4.3 (Shahidi, 1990; functional equations; statement with proof not yet supplied).** Fix a nontrivial additive character of \(F\backslash\mathbb A\), a compatible splitting of \(H\), and hence a nondegenerate character of its maximal unipotent subgroup. Let \(\sigma\) be a globally generic cuspidal automorphic representation of \(M(\mathbb A)\) for the induced character on \(M\). For each constituent \(r_i\) in (4.2), the Langlands–Shahidi local factors give a complete meromorphic L-function satisfying

\[
L_{\mathrm{all}}(s,\sigma,r_i)
=\varepsilon(s,\sigma,r_i)
L_{\mathrm{all}}(1-s,\sigma,r_i^\vee).
\tag{4.3}
\]

The complete equation and the local-factor construction are stated in [Shahidi, *Automorphic L-functions and Functoriality*, §4, Theorem 4.4(a), equations (4.1)–(4.3)](https://arxiv.org/abs/math/0304329v1). Propositions 4.1 and 4.3 explain the reduction to individual constituents. The earlier [free author survey, §3.2](https://www.math.purdue.edu/~fshahidi/articles/Shahidi%20%5B1990%2C%2023pp%5D---Automorphic%20L-functions%2C%20a%20survey.pdf) distinguishes partial equations from complete ones. A proof here would require Eisenstein-series continuation, local Whittaker uniqueness and the local-coefficient construction; those arguments have not yet been supplied. The statement asserts meromorphy and a functional equation, rather than entireness for every constituent.

Examples include standard L-functions for \(GL_n\), tensor products for \(GL_n\times GL_m\), symmetric and exterior squares for \(GL_n\), and certain representations of classical and exceptional dual groups. Their degrees are, respectively, \(n\), \(nm\), \(n(n+1)/2\), and \(n(n-1)/2\).

The twist in the exceptional \(G_2\) example can be checked directly. Work in the dual root system, with short simple root \(\alpha\), long simple root \(\beta\), and Levi root \(\alpha\). The radical roots are

\[
\beta,\ \alpha+\beta,\ 2\alpha+\beta,\ 3\alpha+\beta,
\qquad 3\alpha+2\beta.
\]

Identify the Levi torus with \(\operatorname{diag}(x,y)\in GL_2(\mathbb C)\) by \(\alpha=x/y\), \(\beta=y^2/x\). These two characters form a lattice basis, since their exponent matrix has determinant one. The first four root spaces have characters \(y^2/x,y,x,x^2/y\), precisely the weights of \(\operatorname{Sym}^3\otimes\det^{-1}\); the remaining root space has character \(xy=\det\). To check the representations, and not just their torus weights, use the root-string brackets proved in *Root data, Weyl chambers and the Bruhat decomposition*, §5. Bracketing successively with a Levi raising root vector carries the four first-grade lines to one another with nonzero coefficients. Their \(\alpha^\vee\)-weights are \(-3,-1,1,3\). Rescale the four basis vectors so the raising operator has the usual degree-three polynomial coefficients; the relation \([E,F]=H\) then forces the corresponding lowering coefficients. This identifies the Levi Lie-algebra action with the cubic-polynomial action. The torus characters agree, and the root-group actions are exponentials of these nilpotent operators, so the connected Levi action agrees too. The second grade is one-dimensional. Thus the two constituents are \(\operatorname{Sym}^3\otimes\det^{-1}\) and \(\det\). Central twisting relates this construction to symmetric-cube L-functions.

This list is restricted by (4.2) and by global genericity. See [Gelbart's freely accessible paper, pp.4–8](https://www.claymath.org/library/proceedings/cmip013c.pdf#page=13) for the local coefficients, the separation of constituents and the complete functional equation.

## 5. Degree one: Hecke characters and the complete factors

An **idele class character** is a continuous character

\[
\chi:F^\times\backslash\mathbb A^\times\longrightarrow\mathbb C^\times.
\]

Assume first that it is unitary. The function \(f(g)=\chi(g)\) is left \(F^\times\)-invariant and obeys

\[
(R(h)f)(g)=f(gh)=\chi(h)f(g).
\]

Its one-dimensional span is the automorphic representation \(\pi_\chi\). The usual degree-one smoothness, compact finiteness and infinitesimal-character conditions hold for the local characters described below; boundedness gives moderate growth. There is no proper parabolic subgroup of \(GL_1\), so cuspidality is vacuous. With fixed central character, the quotient by the center is a point, which accounts for the degree-one unitary cuspidal realization.

Let \(\mathfrak f_\chi\) be the finite conductor. At a finite place, the conductor exponent is the least \(a\ge0\) for which \(\chi_v\) is trivial on the unit group when \(a=0\), or on \(1+\mathfrak p_v^a\) when \(a>0\). At a prime not dividing the conductor,

\[
\chi(\mathfrak p_v):=\chi_v(\varpi_v)
\]

is independent of the choice of uniformizer. Extend multiplicatively to fractional ideals prime to \(\mathfrak f_\chi\). This is the ideal character of Hecke theory. If \(a\in F^\times\) is a unit at the conductor primes and is congruent to \(1\) there to the required depths, then

\[
\chi((a))=\chi_\infty(a)^{-1}.
\tag{5.1}
\]

Indeed, the product of all local values on the diagonal element \(a\) is one, the conductor-prime values are one, and every remaining finite value is its uniformizer value to the valuation of \(a\). Equation (5.1) is the principal-ideal compatibility between the ideal character and the infinity type. It is why a general Hecke character is more than an arbitrary multiplicative function on ideals.

**Proposition 5.1 (Hecke L-functions are automorphic L-functions).** In the normalized Satake convention,

\[
L_f(s,\pi_\chi)
=\prod_{\mathfrak p\nmid\mathfrak f_\chi}
(1-\chi(\mathfrak p)N\mathfrak p^{-s})^{-1}
=\sum_{\substack{0\ne\mathfrak a\subset\mathcal O_F\\
(\mathfrak a,\mathfrak f_\chi)=1}}
\chi(\mathfrak a)N\mathfrak a^{-s}.
\tag{5.2}
\]

The series and product converge absolutely for \(\operatorname{Re}s>1\). The ramified finite local factor is \(1\). At a real place write

\[
\chi_v(x)=\operatorname{sgn}(x)^{e_v}|x|^{u_v},
\qquad e_v\in\{0,1\},
\]

and at a complex place write

\[
\chi_v(z)=(z/|z|)^{k_v}|z|_v^{u_v},
\qquad k_v\in\mathbb Z,\qquad |z|_v=|z|^2.
\]

For a unitary character \(u_v\in i\mathbb R\). The corresponding archimedean factors are

\[
L_v(s,\chi)=
\begin{cases}
\Gamma_{\mathbb R}(s+u_v+e_v),&F_v=\mathbb R,\\
\Gamma_{\mathbb C}(s+u_v+|k_v|/2),&F_v=\mathbb C.
\end{cases}
\tag{5.3}
\]

Consequently, with \(D_F\) the discriminant and \(A_\chi=|D_F|N\mathfrak f_\chi\), the automorphic completion is the Hecke completion

\[
\Lambda(s,\chi)=A_\chi^{s/2}
\prod_{v\mid\infty}L_v(s,\chi)\,L_f(s,\chi).
\tag{5.4}
\]

**Proof.** At an unramified finite place the Satake parameter is precisely \(\chi_v(\varpi_v)\). Its one-dimensional determinant gives the factor in (5.2). Expanding each factor geometrically and using unique factorization of ideals gives the displayed series. Since \(\chi\) is unitary, the roots have absolute value one; Proposition 2.1 proves absolute convergence and legitimizes the expansion. At a ramified place, the one-dimensional inertia representation is nontrivial and has zero invariant space, so (3.1) is the determinant on a zero-dimensional space, namely \(1\).

The real and complex characters have the forms stated because the real multiplicative group is \(\{\pm1\}\times\mathbb R_{>0}\) and the complex multiplicative group is \(S^1\times\mathbb R_{>0}\). A continuous character of the circle has integral exponent, and a continuous character of the positive real group is a complex power after applying the logarithm.

The gamma factors can be computed by elementary local zeta integrals. Over \(\mathbb R\), take \(f_v(x)=x^{e_v}e^{-\pi x^2}\) and \(d^\times x=dx/|x|\). In its initial domain of convergence,

\[
\begin{aligned}
\int_{\mathbb R^\times}f_v(x)\chi_v(x)|x|^s\,d^\times x
&=2\int_0^\infty e^{-\pi x^2}x^{s+u_v+e_v}\frac{dx}{x}\\
&=\pi^{-(s+u_v+e_v)/2}
\Gamma\bigl((s+u_v+e_v)/2\bigr).
\end{aligned}
\tag{5.5}
\]

For \(z=re^{i\vartheta}\in\mathbb C\), take

\[
f_v(z)=r^{|k_v|}e^{-ik_v\vartheta}e^{-2\pi r^2},
\qquad d^\times z=\frac{2}{\pi}\frac{dr}{r}\,d\vartheta.
\]

The polynomial angular factor is \(\bar z^{k_v}\) for \(k_v\ge0\) and \(z^{-k_v}\) for \(k_v<0\), so this is a Schwartz function. The angular characters cancel. Setting \(w=s+u_v+|k_v|/2\), the integral is

\[
4\int_0^\infty r^{2w}e^{-2\pi r^2}\frac{dr}{r}
=2(2\pi)^{-w}\Gamma(w)=\Gamma_{\mathbb C}(w).
\tag{5.6}
\]

The choices of multiplicative measures fix the constants in (3.2); rescaling them only rescales a chosen test integral.

Equations (5.2) and (5.3) identify every local factor with the classical Hecke factor. The finite conductor is the same character conductor in both descriptions, and the degree is one, so the discriminant-conductor normalization is \(A_\chi^{s/2}\). This proves the claimed identification of completions. It does not yet prove their analytic continuation. \(\square\)

**Theorem 5.2 (Hecke; Tate's adelic proof, 1950).** For a unitary idele class character \(\chi\) of a number field, (5.4) extends meromorphically and satisfies

\[
\Lambda(s,\chi)=W(\chi)\Lambda(1-s,\chi^{-1}),
\qquad |W(\chi)|=1.
\tag{5.7}
\]

It is entire unless \(\chi=|\cdot|_{\mathbb A}^{it}\) for a real \(t\). In that exceptional case its only poles are simple poles at \(s=-it\) and \(s=1-it\).

**Proof.** The global argument, including its convergence and uniform estimates over an arbitrary number field, was proved in *Tate's global theory: continuation and functional equation*, Proposition 9.1, the theta lemma, and Theorem 9.2. We explain its application to the completion (5.4). Choose the canonical trace additive character and self-dual additive measures. Normalize finite multiplicative measures by \(\operatorname{vol}(\mathcal O_v^\times)=1\), use the displayed real and complex multiplicative measures, and give \(F^\times\) counting measure when forming the quotient. Put \(C_F=F^\times\backslash\mathbb A^\times\), \(C_F^1=\ker|\cdot|\), and \(\kappa=\operatorname{vol}(C_F^1)>0\). Compactness of \(C_F^1\) and the decomposition into this group and the norm coordinate were proved in *Idèles and the idèle class group*, Theorem 3.3 and Proposition 3.5. For a Schwartz–Bruhat function \(f\), define

\[
E_f(x)=\sum_{a\in F^\times}f(ax),\qquad
G(f,\chi,s)=\int_{|x|\ge1}E_f(x)\chi(x)|x|^s\,d^\times\bar x.
\]

The theta lemma gives \(E_f(x)=O_B(|x|^{-B})\) uniformly on the norm-one directions for every \(B>0\); it follows that \(G\) is entire. The proof uses compact lifts of \(C_F^1\), a single fractional-ideal lattice containing all contributing \(a\), and balanced expansion of every infinite coordinate. Thus no compactness or decay at infinity is assumed without a proof.

Poisson summation, proved in *Additive characters, self-dual measures and Poisson summation on the adèles*, gives

\[
E_f(x)=|x|^{-1}E_{\widehat f}(x^{-1})
+|x|^{-1}\widehat f(0)-f(0).
\]

Unfold the global zeta integral in \(\operatorname{Re}s>1\), split it at norm one, and use this identity on the small-norm part. Inversion changes its nonzero transformed sum into \(G(\widehat f,\chi^{-1},1-s)\). Averaging the two zero terms over \(C_F^1\) gives zero unless \(\chi\) is trivial there: translation by a point where \(\chi\ne1\) multiplies a finite average by that value, forcing the average to vanish. In the exceptional case \(\chi=|\cdot|^{it}\), their norm integrals are elementary. Consequently

\[
Z(f,\chi,s)=G(f,\chi,s)+G(\widehat f,\chi^{-1},1-s)
+\begin{cases}
\displaystyle\kappa\left(\frac{\widehat f(0)}{s+it-1}
-\frac{f(0)}{s+it}\right),&\chi=|\cdot|^{it},\\[4pt]
0,&\chi|_{C_F^1}\ne1.
\end{cases}
\]

This is a meromorphic continuation with just the stated possible poles. Applying the formula to \(\widehat f,\chi^{-1},1-s\) interchanges its two entire terms and leaves its rational term unchanged; Fourier inversion gives \(\widehat{\widehat f}(a)=f(-a)\), and reindexing by \(-1\in F^\times\) preserves \(E_f\). This proves the global zeta-integral functional equation.

Choose \(f_v=1_{\mathcal O_v}\) at each unramified finite place, and \(f_v=\chi_v^{-1}1_{\mathcal O_v^\times}\) at a ramified place. At infinity choose the polynomial Gaussians used in (5.5)–(5.6). The finite local calculations and these gamma integrals give, in the initial half-plane,

\[
Z(f,\chi,s)=L^*(s,\chi),\qquad
L^*(s,\chi)=\prod_{v\mid\infty}L_v(s,\chi)L_f(s,\chi).
\]

The local functional equations and their Gauss-sum computations were proved in *Tate's local theory at the finite places* and *Tate's local theory at the infinite places*. Their product, computed explicitly in *Hecke L-functions and the Dedekind zeta function*, Theorem 10.1, is

\[
\prod_v\varepsilon_v(s,\chi_v)=W(\chi)A_\chi^{1/2-s},
\qquad |W(\chi)|=1.
\]

Here the finite exponent at \(v\) is \((a_v+d_v)(1/2-s)\), where \(a_v\) is the character conductor exponent and \(d_v\) the different exponent. Their norms multiply to \(A_\chi=|D_F|N\mathfrak f_\chi\); the normalized Gauss sums and infinite phases all have modulus one. Global rescaling of the additive character contributes \(\prod_v\chi_v(a)|a|_v^{s-1/2}=1\) for \(a\in F^\times\). Thus the result is independent of that auxiliary choice. Combining the local equations with the global equation gives

\[
L^*(s,\chi)=W(\chi)A_\chi^{1/2-s}L^*(1-s,\chi^{-1}).
\]

Multiplication by \(A_\chi^{s/2}\) proves (5.7). This comparison uses meromorphic continuations: the original integrals on the two sides converge in the disjoint half-planes \(\operatorname{Re}s>1\) and \(\operatorname{Re}s<0\).

If \(\chi\) is not a pure norm twist, the correction term vanishes, so the standard test gives an entire \(L^*\), and hence an entire \(\Lambda\). For a pure twist the standard test has \(f(0)=1\) and \(\widehat f(0)=|D_F|^{-1/2}>0\). The two residues in the continuation formula are therefore nonzero. Multiplication by the nowhere-zero exponential \(A_\chi^{s/2}\) preserves both simple poles. This finishes the proof. \(\square\)

For a nonunitary quasicharacter obtained by a norm twist, the same factor calculation holds and the analytic variable shifts accordingly. For example, \(\chi=\chi_0|\cdot|_{\mathbb A}^{u}\) has \(L_f(s,\chi)=L_f(s+u,\chi_0)\). One must shift the gamma factors too.

As a check, \(F=\mathbb Q\) and \(\chi=1\) give

\[
\Lambda(s,1)=\pi^{-s/2}\Gamma(s/2)\zeta(s),
\]

with the functional equation \(\Lambda(s,1)=\Lambda(1-s,1)\) and poles at \(0,1\). A primitive Dirichlet character of conductor \(N\) and parity \(e\) gives \(N^{s/2}\Gamma_{\mathbb R}(s+e)L(s,\chi)\). The common classical expression \((N/\pi)^{(s+e)/2}\Gamma((s+e)/2)L(s,\chi)\) differs by the constant \(N^{e/2}\), independent of \(s\). This harmless constant does not alter the functional equation relating the two inverse characters, whose conductors and parities agree.

## 6. Symmetric-square, adjoint and Artin examples

Let \(\pi_v\) be unramified on \(GL_2(F_v)\), with parameter \(\operatorname{diag}(\alpha,\beta)\). On homogeneous degree-two polynomials, the basis \(x^2,xy,y^2\) has eigenvalues \(\alpha^2,\alpha\beta,\beta^2\). Therefore

\[
L_v(s,\pi,\operatorname{Sym}^2)
=\frac{1}{(1-\alpha^2q_v^{-s})
(1-\alpha\beta q_v^{-s})(1-\beta^2q_v^{-s})}.
\tag{6.1}
\]

The same argument in degree \(m\) gives all \(m+1\) eigenvalues \(\alpha^{m-j}\beta^j\), for \(0\le j\le m\). Both endpoints occur.

The adjoint representation is conjugation on the trace-zero endomorphisms. In the basis \(E_{12},\operatorname{diag}(1,-1),E_{21}\), its eigenvalues are \(\alpha/\beta,1,\beta/\alpha\). Thus

\[
L_v(s,\pi,\operatorname{Ad})
=\frac{1}{(1-(\alpha/\beta)q_v^{-s})
(1-q_v^{-s})(1-(\beta/\alpha)q_v^{-s})}.
\tag{6.2}
\]

These also show that \(\operatorname{Ad}\simeq\operatorname{Sym}^2\otimes\det^{-1}\) on \(GL_2(\mathbb C)\): dividing each symmetric-square eigenvalue by \(\alpha\beta\) gives the displayed adjoint eigenvalues. More intrinsically, \(V^*\simeq V\otimes\det(V)^{-1}\) for a two-dimensional space; the decomposition \(V\otimes V=\operatorname{Sym}^2V\oplus\bigwedge^2V\) identifies the trace-zero summand of \(V\otimes V^*\) with \(\operatorname{Sym}^2V\otimes\det(V)^{-1}\). Consequently the adjoint factor is a symmetric-square factor with an inverse-central-character twist, not generally the untwisted symmetric-square factor.

Now consider finite Galois data. If \(G=\{1\}\), the dual group is trivial but the Weil or Galois part of its L-group remains. A finite-image continuous representation

\[
\rho:\operatorname{Gal}(\overline F/F)\longrightarrow GL(V)
\]

therefore gives, on this reciprocity side, the **Artin L-function**

\[
L(s,\rho)=\prod_{v\nmid\infty}
\det\left(1-q_v^{-s}\rho(\operatorname{Fr}_v)
\mid V^{I_v}\right)^{-1}.
\tag{6.3}
\]

Choose Frobenius consistently with the reciprocity convention. Outside its finite ramification set, the determinant acts on all of \(V\). The finite-image hypothesis makes every eigenvalue a root of unity, so Proposition 2.1 proves absolute convergence and nonvanishing for \(\operatorname{Re}s>1\). At ramified places the same conclusion holds for the finitely many factors on \(V^{I_v}\): their eigenvalues also have absolute value one.

There is only one ordinary automorphic representation of the trivial group. The extra \(\rho\) is Galois input to \(r\), not an extra automorphic representation of that group. The **Artin holomorphy conjecture** [Getz–Hahn 2022, Conjecture 13.4.1] says that an irreducible nontrivial finite-image \(\rho\) has an entire Artin L-function. This is a conjecture, not a consequence of convergence. The stronger automorphic expectation [Getz–Hahn 2022, Conjecture 13.4.2] seeks a cuspidal representation of \(GL_{\dim V}(\mathbb A_F)\) with these unramified standard factors. The lesson *The Artin conjecture for two-dimensional representations: the Langlands–Tunnell theorem* gives precise known cases and the parity conditions in the classical modular-form setting.

## 7. Exercises with complete solutions

### Exercise 7.1 — The standard Euler product

Write \(L^S(s,\pi,\mathrm{std})\) for an automorphic representation of \(GL_n(\mathbb A_F)\) in terms of its Satake parameters.

**Solution.** The standard representation acts on a diagonal representative by its diagonal entries. Its determinant is

\[
\det(1-q_v^{-s}c_v)=\prod_{i=1}^n(1-\alpha_{i,v}q_v^{-s}).
\]

Hence

\[
L^S(s,\pi,\mathrm{std})
=\prod_{v\notin S}\prod_{i=1}^n
(1-\alpha_{i,v}q_v^{-s})^{-1}.
\]

Permuting the parameters leaves the product unchanged. The formula initially denotes an analytic function in a half-plane of absolute convergence, rather than an automatically continued function everywhere.

### Exercise 7.2 — Convergence from a uniform exponent

Assume \(|\alpha_{i,v}|\le q_v^\theta\) with one fixed \(\theta<1/2\). Prove absolute convergence for \(\operatorname{Re}s>1+\theta\), including the justification for multiplying infinitely many local factors.

**Solution.** Fix \(\sigma_0>1+\theta\) and set \(t=\sigma_0-\theta>1\). Each geometric ratio has absolute value at most \(q_v^{-t}\). Its logarithm is absolutely bounded by \(q_v^{-t}/(1-2^{-t})\). Summing over the \(n\) parameters and all places gives

\[
\sum_{v\notin S}\sum_{i=1}^n
\bigl|\log(1-\alpha_{i,v}q_v^{-s})\bigr|
\le\frac{n}{1-2^{-t}}\sum_vq_v^{-t}<\infty
\]

uniformly for \(\operatorname{Re}s\ge\sigma_0\), by (2.5). Exponentiating the locally uniformly convergent negative logarithm series gives the limit of the finite products and proves both holomorphy and nonvanishing. The positive geometric majorant in Proposition 2.1 also proves absolute convergence of the ideal Dirichlet series. As \(\sigma_0\) can approach \(1+\theta\) from above, the conclusion holds throughout the required open half-plane.

### Exercise 7.3 — A zeta factor in the self-pairing

For \(\pi\) on \(GL_2\), prove the unramified identity

\[
L_v(s,\pi\times\widetilde\pi)
=\zeta_v(s)L_v(s,\pi,\operatorname{Ad}),
\]

and explain its partial global form.

**Solution.** The dual parameter has eigenvalues \(\alpha^{-1},\beta^{-1}\). Tensoring produces \(1,\alpha/\beta,\beta/\alpha,1\), with two copies of \(1\). Therefore

\[
L_v(s,\pi\times\widetilde\pi)
=\frac{1}{(1-q_v^{-s})^2
(1-(\alpha/\beta)q_v^{-s})(1-(\beta/\alpha)q_v^{-s})}.
\]

One of the two factors \((1-q_v^{-s})^{-1}\) is \(\zeta_v(s)\); the other belongs to the adjoint factor (6.2). Representation-theoretically,

\[
\operatorname{End}(\mathbb C^2)
=\mathbb C\operatorname{id}\oplus\operatorname{End}^0(\mathbb C^2),
\]

and the two summands are the trivial and adjoint representations. Multiplying at the unramified places gives

\[
L^S(s,\pi\times\widetilde\pi)
=\zeta_F^S(s)L^S(s,\pi,\operatorname{Ad})
\]

in a common half-plane of absolute convergence. If continuations of all the factors are available, the identity extends by analytic continuation. An assertion involving the full zeta function and complete L-functions additionally needs the corresponding identities at the omitted places; the unramified computation alone proves the partial identity.

### Exercise 7.4 — The Jacquet–Shalika bound

Show that \(|\alpha_{i,v}|<q_v^{1/2}\) implies absolute convergence and nonvanishing of \(L^S(s,\pi)\) for \(\operatorname{Re}s>3/2\).

**Solution.** A strict upper bound implies the weak uniform bound \(|\alpha_{i,v}|\le q_v^{1/2}\). Take \(A=1/2\) in Proposition 2.1. For any \(\sigma_0>3/2\), the estimate uses \(t=\sigma_0-1/2>1\), and the absolute logarithm sum is at most

\[
\frac{n}{1-2^{-(\sigma_0-1/2)}}
\sum_v q_v^{-(\sigma_0-1/2)}<\infty.
\]

The limit is the exponential of a holomorphic function, so it has no zeros. This proves the assertion. It supplies neither a uniform exponent below \(1/2\) nor a boundary-line conclusion. Those stronger statements require additional information.

## Scope of the proofs

Lemma 1.0 proves compactness of the unipotent integration domain. Theorem 1.1 proves restricted factorization using the arbitrary-algebra tensor theorem in the linked prerequisite; global admissibility supplies its one-dimensional fixed lines. Lemma 1.2 proves the absolutely convergent smooth vector-group Fourier expansions used in Theorem 1.3, which proves nonvanishing of the global Whittaker transform for every nonzero smooth cuspidal function on GL_n over every number field. Corollary 1.4 proves local Whittaker existence from the specified smooth realization, including continuity at infinity via an explicit other-place rank-one projection. The convergence criterion, weight deductions under their stated bounds, determinant examples and exercise solutions are proved here. Theorem 5.2 gives the full degree-one continuation and functional equation by applying the actual earlier adèle lessons, including their Poisson and local epsilon-factor proofs.

The proofs of the general spherical-parameter bound in Theorem 2.3 and the analytic integral theorems in §4 are still missing. Their statements are kept explicit, and the deductions using (2.9) are conditional on that bound. Admissibility of automorphic spaces and the general cuspidal algebraic/Hilbert comparison also require proofs before they can supply hypotheses for arbitrary cuspidal representations. Theorem 1.1 itself assumes irreducibility and admissibility. The interpretation of the spherical Hecke characters as Satake classes inherits the general Satake proof obligations identified in the preceding lesson.

Where a general reductive local correspondence is unavailable, §3 is a formulation conditional on the stated local parameters and their compatibility. Conjecture 3.1 and the general Artin holomorphy and reciprocity assertions remain conjectures. None of these statements is inferred from absolute convergence.

## References

- J. R. Getz and H. Hahn, [*An Introduction to Automorphic Representations, with a View toward Trace Formulae*](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), author draft of 22 April 2022; §§6.3–6.5, 11.3, 11.7 and 12.7; Definitions 11.2–11.4 and Theorem 11.3.3 for Whittaker functionals and the global expansion.
- R. P. Langlands, [*Problems in the theory of automorphic forms*](https://publications.ias.edu/sites/default/files/problems-in-the-theory-of-automorphic-forms_rpl_8.pdf), free IAS re-typeset text; §7, Questions 1 and 4.
- R. P. Langlands, [*Euler Products*](https://publications.ias.edu/sites/default/files/euler-products_rpl_2.pdf), free IAS text of the Yale lectures; §§2–3.
- F. Shahidi, [*Automorphic L-functions, a survey*](https://www.math.purdue.edu/~fshahidi/articles/Shahidi%20%5B1990%2C%2023pp%5D---Automorphic%20L-functions%2C%20a%20survey.pdf), free author text, 1990; §3.2.
- F. Shahidi, [*Automorphic L-functions and Functoriality*](https://arxiv.org/abs/math/0304329v1), free 2003 preprint; §4, especially Theorem 4.4(a).
- S. Gelbart, [*Shahidi's Work “On Certain L-functions”: A Short History of Langlands–Shahidi Theory*](https://www.claymath.org/library/proceedings/cmip013c.pdf#page=10), freely accessible paper, 2011, pp.1–18; pp.4–8 for the analytic methods.
- P. Sarnak, [*Notes on the generalized Ramanujan conjectures*](https://publications.ias.edu/sites/default/files/FieldNotesCurrent.pdf), free author text, 2005; §1, pp.659–664.
- J. Binder, [*Tate's thesis on zeta functions on number fields*](https://math.uchicago.edu/~may/VIGRE/VIGRE2009/REUPapers/Binder.pdf), free exposition, 2009; §5.4. The degree-one proof used here is in the linked programme lessons.
- Y. Cai, S. Friedberg, D. Ginzburg and E. Kaplan, [*Doubling constructions and tensor product L-functions: the linear case*](https://arxiv.org/abs/1710.00905v2), free 2018 preprint, version 2; Theorems A, 29–30 and §3.5, pp.29–30.
