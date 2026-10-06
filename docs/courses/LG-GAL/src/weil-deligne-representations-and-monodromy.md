# Weil–Deligne representations and Grothendieck’s monodromy theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A continuous representation can have infinite inertia image even when its coefficient characteristic differs from the residue characteristic. The infinite part is remarkably rigid: on a sufficiently small subgroup, one nilpotent matrix controls everything. A Weil–Deligne representation records that matrix separately from the representation with finite inertia image. This makes local factors and comparison between coefficient fields algebraic.

## 1. Conventions and the two kinds of representation

Let \(F\) be a nonarchimedean local field with residue characteristic \(p\) and residue field of size \(q\). Write \(I\) and \(P\) for inertia and wild inertia. A geometric Frobenius lift \(\Phi\in W_F\) gives
\[
W_F=I\rtimes\langle\Phi\rangle,
\qquad v(\Phi)=1,
\qquad \|w\|=q^{-v(w)}.
\tag{1}
\]
Here \(I\) has its profinite topology and \(W_F/I=\mathbf Z\) has the discrete topology. The local-field structure needed below is
\[
P\text{ is pro-}p,
\qquad I/P\simeq\prod_{r\ne p}\mathbf Z_r(1),
\qquad t_\ell(w\sigma w^{-1})=\|w\|t_\ell(\sigma).
\tag{2}
\]
Choose a basis of \(\mathbf Z_\ell(1)\), so that the \(\ell\)-component of the tame character is written \(t_\ell:I\to\mathbf Z_\ell\). Throughout \(\ell\ne p\).

The Weil topology and splitting in (1) are Proposition 1.1 of the earlier lesson *Representations of Weil groups*. We now prove (2), using the finite-extension, Hensel and unramified-field proofs of §§0D–0F in the first lesson. No ramification structure theorem is left as an external citation.

**Proposition 1.0 (wild and tame inertia).** Let \(F^{\mathrm{ur}}\) be the unramified union and \(\varpi\) a uniformizer of \(F\). The maximal tame extension is
\[
F^t=\bigcup_{(m,p)=1}F^{\mathrm{ur}}(\varpi^{1/m}).
\]
Its inertia group is canonically \(\varprojlim_{(m,p)=1}\mu_m\), with power transition maps. The kernel \(P=\operatorname{Gal}(F^{\mathrm{sep}}/F^t)\) is pro-\(p\). In this tame quotient arithmetic Frobenius conjugates by the \(q\)-th power, and geometric Frobenius by its inverse. These assertions imply (2).

**Proof.** We first establish the finite ramification assertions used to identify this kernel. In a finite Galois extension \(L/F\), let \(L_0\) be the maximal unramified subfield. The first lesson constructs \(L_0\) by lifting a primitive residue element and proves that its degree is the residue degree. Thus \(L/L_0\) is totally ramified of degree \(e\), its inertia group \(G_0\) fixes \(L_0\), and \(|G_0|=e\).

If \(\pi\) is an upper uniformizer, then \(1,\pi,\ldots,\pi^{e-1}\) are linearly independent over \(L_0\): the nonzero terms in such a relation have distinct valuations modulo \(e\), so their minimum cannot cancel. There are \(e\) of them, hence they are a basis. An integral element expressed in this basis has coefficients in \(\mathcal O_{L_0}\), by the same distinct-valuation argument. Consequently \(\mathcal O_L=\mathcal O_{L_0}[\pi]\).

For \(j\ge0\), define \(G_j\) to be the automorphisms acting trivially on \(\mathcal O_L/\pi^{j+1}\mathcal O_L\). The definition of \(G_0\) agrees with inertia. These are normal subgroups, because conjugation preserves the integral ring and valuation; they eventually become trivial, because each nonidentity automorphism moves some integral element and the group is finite. For \(\sigma\in G_0\), the polynomial identity \(f(Y)-f(X)=(Y-X)g(X,Y)\) and the preceding integral basis show
\[
\sigma\in G_j\quad\Longleftrightarrow\quad
v_L(\sigma\pi-\pi)\ge j+1.
\]
Reduction of \(\sigma\pi/\pi\) is therefore an injective homomorphism \(G_0/G_1\to k_L^\times\). For \(j\ge1\), its class in
\((1+\pi^j\mathcal O_L)/(1+\pi^{j+1}\mathcal O_L)\)
is an injective homomorphism from \(G_j/G_{j+1}\). Indeed, if \(c_\sigma=\sigma\pi/\pi\), then
\(c_{\sigma\tau}=\sigma(c_\tau)c_\sigma\); elements of \(G_1\) act trivially on this unit quotient. The latter quotient is the additive group of \(k_L\), via \(1+a\pi^j\mapsto\bar a\), since the product term has valuation at least \(j+1\).

It follows that \(G_1\) is a \(p\)-group and that \(G_0/G_1\) has order prime to \(p\). Thus \(G_1\) is the unique Sylow \(p\)-subgroup of inertia. In particular \(L^{G_1}/F\) is tame. Conversely, a Galois tame subextension has inertia of order prime to \(p\), so the image of \(G_1\) in it is trivial. This identifies the largest tame subextension of \(L/F\) as \(L^{G_1}\), once the tame union is constructed.

Now suppose \(L/F\) is finite and tame, with maximal unramified subfield \(L_0\). In its totally ramified part choose an upper uniformizer \(\pi\) and write \(\pi^e=\varpi u\), with \(u\) an upper unit and \((e,p)=1\). Choose a unit \(u_0\in L_0\) with the same residue. Simple-root Hensel applied to \(X^e-u/u_0\) gives \(b\equiv1\pmod\pi\) with \(b^e=u/u_0\). Hence \(\gamma=\pi/b\) satisfies \(\gamma^e=\varpi u_0\) and still generates \(L/L_0\) by the uniformizer basis argument.

Every unit of \(F^{\mathrm{ur}}\) has an \(m\)-th root there if \((m,p)=1\). To prove this, put the unit in a complete finite unramified level, choose an \(m\)-th root of its residue in a finite residue extension, and lift its simple root by Hensel in the corresponding complete unramified field. This also puts \(\mu_m\) in \(F^{\mathrm{ur}}\). Applying it to \(u_0\) shows that \(L\) lies in \(F^{\mathrm{ur}}(\varpi^{1/e})\).

Conversely, any finite set in \(F^{\mathrm{ur}}(\varpi^{1/m})\) lies in \(F_r(\varpi^{1/m})\), where \(F_r/F\) is finite unramified and may be enlarged to contain \(\mu_m\). Distinct valuation classes show that the radical extension has degree and ramification index \(m\). Its intermediate fields therefore have ramification indices dividing \(m\), so are tame; their residue fields are finite and hence separable. These radical fields are Galois over \(F\) after including \(\mu_m\), since every conjugate radical is a root-of-unity multiple of the original. Their union is consequently Galois and is exactly the maximal tame field displayed in the statement.

For the finite Galois \(L/F\) above, this proves \(L\cap F^t=L^{G_1}\). The image of \(P\) in its finite Galois group is thus \(G_1\), a \(p\)-group. Finite Galois quotients detect the topology of \(P\) by the first lesson's inverse-limit proof, so \(P\) is pro-\(p\).

Choose compatible radicals \(\varpi_n^{n/m}=\varpi_m\). Such choices exist along a cofinal sequence of indices, each dividing the next, by successively taking roots. Over \(F^{\mathrm{ur}}\), the powers \(1,\varpi_m,\ldots,\varpi_m^{m-1}\) have distinct valuations modulo \(\mathbb Z\), so the radical has degree \(m\). Its conjugates are all \(\zeta\varpi_m\), with \(\zeta\in\mu_m\), and the action ratio
\[
\sigma\longmapsto\frac{\sigma(\varpi_m)}{\varpi_m}
\]
identifies its Galois group with \(\mu_m\). Compatibility of radicals identifies restriction with the power map. Inverse limits give the asserted tame inertia group. Changing a radical multiplies it by a root of unity in the unramified field; changing \(\varpi\) multiplies the radicals by prime-to-\(p\) roots of a unit there. Inertia fixes these ratios, so the identification is independent of both changes. Decomposing each finite cyclic root group into its primary components gives \(\prod_{r\ne p}\mathbb Z_r(1)\).

Extend arithmetic Frobenius on \(F^{\mathrm{ur}}\) by fixing the compatible radicals. Unique coefficient expansions in each radical basis define this automorphism, and the extensions agree through the tower. It raises the prime-to-\(p\) roots of unity to their \(q\)-th powers: this holds on residues and simple-root Hensel gives equality of the lifts. Conjugating an inertia automorphism therefore raises each action ratio to its \(q\)-th power. Every other Frobenius lift gives the same action, since tame inertia is abelian. Taking the inverse lift gives \(q^{-1}\), and an element \(w=i\Phi^n\) consequently acts on the \(\ell\)-component by \(q^{-n}=\|w\|\). This proves (2). \(\square\)

A continuous \(\ell\)-adic representation will initially have coefficients in a finite extension \(E/\mathbf Q_\ell\). Statements over \(\overline{\mathbf Q}_\ell\) mean scalar extensions of such representations. The finite-field-of-definition condition prevents a topology on the algebraic closure from silently changing the category.

**Definition 1.1.** Over a characteristic-zero field \(E\), a Weil–Deligne representation is a pair \((r,N)\) on a finite-dimensional vector space \(V\), where \(r:W_F\to\mathrm{GL}(V)\) is smooth and
\[
r(w)Nr(w)^{-1}=\|w\|N.
\tag{3}
\]
Smooth means that the restriction to \(I\) is trivial on an open subgroup. A morphism intertwines \(r\) and commutes with \(N\). One ordinarily includes nilpotence in the definition; the following observation makes it redundant.

**Lemma 1.2.** Relation (3) forces \(N\) to be nilpotent.

*Proof.* Over an algebraic closure, conjugate matrices have the same finite multiset of eigenvalues. Relation (3) for \(\Phi\) therefore says that the spectrum of \(N\) is invariant under multiplication by \(q^{-1}\). A nonzero eigenvalue would have an infinite orbit, since \(q\) is not a root of unity in characteristic zero. Thus every eigenvalue is zero. Cayley–Hamilton gives \(N^{\dim V}=0\). ∎

Define \(\mathrm{Sp}(n)\), for \(n\ge1\), by the basis \(e_0,\ldots,e_{n-1}\) and
\[
r(w)e_j=\|w\|^j e_j,
\qquad Ne_j=e_{j+1}\ (j<n-1),
\qquad Ne_{n-1}=0.
\tag{4}
\]
The kernel is the last line, with character \(\|\cdot\|^{n-1}\). This direction of the shift will determine every factor below.

## 2. A full monodromy proof

The issue is compact inertia, rather than compactness of the entire Weil-group image. The latter can fail: the unramified character sending \(\Phi\) to \(\ell\) is continuous on \(W_F\).

We first isolate the compact-group argument needed to choose a subgroup invariant under every conjugation coming from \(W_F\).

We also record the linear algebra used by the choice and semisimplification arguments, including its descent to the original coefficient field.

**Lemma 2.0 (primary spaces and Jordan components).** If \(A\) is an invertible operator over a characteristic-zero field \(E\), its vector space is the direct sum of the kernels of the primary factors of its minimal polynomial. It has unique commuting factors \(A=SU\), where \(S\) is semisimple and \(U\) unipotent, and both factors are polynomials in \(A\) over \(E\). The additive version \(B=B_s+B_n\), with commuting semisimple and nilpotent parts, has the same properties. On \(\operatorname{End}_E(V)\), the Jordan components of \(\operatorname{Ad}(A)\) are \(\operatorname{Ad}(S)\) and \(\operatorname{Ad}(U)\).

**Proof.** Factor the minimal polynomial as \(\prod_f f^{a_f}\) with distinct monic irreducible factors. The Euclidean algorithm makes these factors pairwise coprime. Its Chinese-remainder idempotents are polynomials in \(A\), add to one, multiply pairwise to zero, and have images \(\ker f(A)^{a_f}\). To verify the image assertion, use the congruences modulo each primary factor; the annihilating minimal polynomial then makes the polynomial identities hold on the vector space. This proves the primary decomposition over \(E\).

Take a finite Galois splitting field \(K/E\) of the minimal polynomial. Its irreducible factors are separable in characteristic zero. The preceding argument over \(K\) gives generalized eigenspaces \(V_\lambda\). Define \(S\) to be multiplication by \(\lambda\) on \(V_\lambda\). A polynomial with congruences
\(s(X)\equiv\lambda\pmod{(X-\lambda)^{a_\lambda}}\)
exists by the same Euclidean algorithm. Its unique remainder of degree below the minimal polynomial is fixed by \(\operatorname{Gal}(K/E)\), because those automorphisms permute these congruences. It therefore has coefficients in \(E\). This constructs \(S=s(A)\) over \(E\). On \(V_\lambda\), \(A=\lambda1+D_\lambda\) with \(D_\lambda\) nilpotent, so \(U=S^{-1}A=1+\lambda^{-1}D_\lambda\) is unipotent. The Euclidean algorithm also expresses \(S^{-1}\) as a polynomial in \(S\), since all eigenvalues are nonzero. Thus \(U\) is a polynomial in \(A\), and the factors commute.

For uniqueness, any commuting semisimple and unipotent factors preserve the generalized eigenspaces of their product. Inside each simultaneous eigenspace of the semisimple factor, that product has the same unique eigenvalue as the semisimple factor. On \(V_\lambda\) that factor must consequently be \(\lambda1\). The other factor is forced by division. This proves uniqueness over \(K\) and hence over \(E\). Defining \(B_s\) to be the scalar \(\lambda\) on each generalized eigenspace of an arbitrary \(B\), without requiring nonzero eigenvalues, gives the additive assertion by the same polynomial construction and uniqueness argument.

After splitting \(S\), the spaces \(\operatorname{Hom}(V_\lambda,V_\mu)\) show that \(\operatorname{Ad}(S)\) is semisimple, with eigenvalues \(\mu/\lambda\). Left multiplication by \(U\) and right multiplication by \(U^{-1}\) are commuting unipotent operators; their product is unipotent, since sums and products of their commuting nilpotent differences from one are nilpotent. Therefore \(\operatorname{Ad}(U)\) is unipotent. They commute and multiply to \(\operatorname{Ad}(A)\). Uniqueness proves the last assertion. The same reasoning shows that any positive power of an invertible semisimple operator is semisimple, and that an invertible operator with a semisimple positive power is semisimple: on a generalized eigenspace, the linear coefficient of \((\lambda+D)^m\) in \(D\) is \(m\lambda^{m-1}\ne0\), so a nonzero nilpotent part cannot disappear. \(\square\)

**Lemma 2.1.** Let \(H\subset\mathrm{GL}_d(E)\) be compact. Suppose \(B\triangleleft H\) is the image of a pro-\(p\) group and \(H/B\) is abelian. Then \(B\) is finite, and \(H\) has a characteristic open abelian pro-\(\ell\) subgroup contained in any prescribed sufficiently small congruence subgroup.

*Proof.* By the stable-lattice argument of the first lesson, conjugate \(H\) into \(\mathrm{GL}(T)\), where \(T\) is an \(\mathcal O_E\)-lattice. For sufficiently large \(m\), the group
\[
U_m=1+\ell^m\mathrm{End}_{\mathcal O_E}(T)
\tag{5}
\]
is pro-\(\ell\), and logarithm and exponential are inverse on the corresponding matrix neighborhoods. We can take any integer \(m>1/(\ell-1)\); increasing it meets a prescribed congruence neighborhood. These assertions follow directly from the series: the valuations of \(X^k/k\) and \(X^k/k!\) tend to infinity for \(X\in\ell^m\mathrm{End}(T)\), and the formal inverse identities hold by convergence. The finite successive congruence quotients are \(\ell\)-groups, proving the pro-\(\ell\) assertion.

The group \(B\cap U_m\) is both pro-\(p\) and pro-\(\ell\), so it is trivial. Consequently \(B\) injects into a finite congruence quotient and is finite. Put \(J_0=H\cap U_m\). Commutators in \(J_0\) lie in \(B\), because \(H/B\) is abelian; they also lie in \(J_0\). Hence \(J_0\) is abelian.

Logarithm identifies \(J_0\) with a closed additive subgroup of \(\ell^m\mathrm{End}(T)\). Commuting matrices satisfy \(\log(xy)=\log x+\log y\). Closed additive subgroups are \(\mathbf Z_\ell\)-submodules, since integer multiplication extends by continuity. This module is finitely generated over \(\mathbf Z_\ell\), being a submodule of a finite free module. Thus \(J_0\), and then its finite extension \(H\), are topologically finitely generated.

Let \(a=[H:J_0]\). A topologically finitely generated profinite group has only finitely many open subgroups of index \(a\): each such subgroup is a point stabilizer in a continuous action on \(a\) letters, and finitely many choices for the images of a fixed finite generating set give finitely many homomorphisms to \(S_a\). The intersection \(J\) of all these subgroups is open and characteristic. Since \(J_0\) occurs in the intersection, \(J\subset J_0\). It is abelian, pro-\(\ell\), and lies in the desired matrix neighborhood. ∎

**Theorem 2.2 (Grothendieck’s monodromy theorem).** If \(\rho:W_F\to\mathrm{GL}(V)\) is continuous and \(\ell\ne p\), there are an open subgroup \(I_1\subset I\) and a unique nilpotent endomorphism \(N\) such that
\[
\rho(\sigma)=\exp(t_\ell(\sigma)N)
\qquad(\sigma\in I_1).
\tag{6}
\]
Moreover \(\rho(w)N\rho(w)^{-1}=\|w\|N\) for every \(w\in W_F\).

*Proof.* Apply Lemma 2.1 to \(H=\rho(I)\) and \(B=\rho(P)\). Compactness follows from compactness of \(I\); the quotient is abelian by (2). Take the characteristic subgroup \(J\) in a logarithm neighborhood, and let \(I_1\) be its inverse image. Conjugation by \(\rho(W_F)\) preserves \(H\), so it preserves \(J\). Thus \(I_1\) is normal in \(W_F\).

The map \(I_1\to J\) kills \(I_1\cap P\): its image is both pro-\(p\) and pro-\(\ell\). It therefore factors through the open subgroup \(I_1P/P\) of tame inertia. A continuous homomorphism from that subgroup to a pro-\(\ell\) group kills its prime-to-\(\ell\) components. Equivalently, it factors through
\[
t_\ell(I_1)=\ell^b\mathbf Z_\ell
\tag{7}
\]
for some \(b\ge0\). To see the component assertion explicitly, an open subgroup of the procyclic product in (2) is a product of open subgroups of its prime components; a pro-\(r\) component with \(r\ne\ell\) has trivial image in every finite \(\ell\)-quotient.

Choose \(\tau\in I_1\) with \(t_\ell(\tau)=\ell^b\), and set \(N=\ell^{-b}\log\rho(\tau)\). The additive logarithm homomorphism on (7) is determined by its value at the topological generator \(\ell^b\). Thus
\[
\log\rho(\sigma)=t_\ell(\sigma)N
\qquad(\sigma\in I_1).
\tag{8}
\]
Conjugate (8) by \(\rho(w)\). Both inertia elements remain in \(I_1\), and logarithm commutes with conjugation by its convergent power series. Equation (2) gives
\[
\rho(w)N\rho(w)^{-1}=\|w\|N.
\tag{9}
\]
Lemma 1.2 makes \(N\) nilpotent. Exponentiating (8) proves (6), now with a finite polynomial exponential.

For uniqueness, intersect two proposed open subgroups. Its tame image still contains \(\ell^c\mathbf Z_\ell\) for some \(c\). At an element with tame value \(\ell^c\), apply the polynomial logarithm of a unipotent matrix to (6). It gives \(\ell^cN=\ell^cN'\), hence \(N=N'\). ∎

This proof establishes quasi-unipotence of inertia: each \(\rho(\sigma)\) has a positive power in the unipotent subgroup \(\rho(I_1)\). It does not require eigenvalues of \(\rho(\Phi)\) to be \(\ell\)-adic units.

## 3. Removing and recovering monodromy

Write \(w=i\Phi^{v(w)}\), and define \(c(w)=t_\ell(i)\). The tame conjugation relation gives the cocycle identity
\[
c(ww')=c(w)+\|w\|c(w').
\tag{10}
\]
This identity fixes the order of the exponential in the construction.

**Theorem 3.1.** For fixed \(\Phi\) and \(t_\ell\), the rules
\[
r(w)=\exp(-c(w)N)\rho(w),
\qquad
\rho(w)=\exp(c(w)N)r(w)
\tag{11}
\]
give inverse equivalences between continuous \(E\)-linear representations of \(W_F\) and \(E\)-linear Weil–Deligne representations.

*Proof.* For \(\rho\), take \(N\) from Theorem 2.2. Relation (9) and (10) show
\[
\begin{aligned}
r(w)r(w')
&=\exp\bigl(-(c(w)+\|w\|c(w'))N\bigr)\rho(ww')\\
&=r(ww').
\end{aligned}
\tag{12}
\]
On \(I_1\), (6) makes \(r=1\), so \(r\) is smooth. Multiplying by an exponential in \(N\) does not change its conjugation action on \(N\), proving (3).

Conversely, begin with \((r,N)\). Relation (3) and (10) prove multiplicativity of the second rule in (11). Its restriction to \(I\) is continuous, because \(r|_I\) is locally constant and the nilpotent exponential is a polynomial in the continuous tame character. The other components \(I\Phi^n\) are open, proving continuity on \(W_F\). On an open subgroup killing \(r\), its inertia action is (6), so its monodromy is precisely \(N\). Both constructions are inverse.

An intertwiner of continuous representations intertwines their monodromy: on a common open subgroup, intertwine (6) and apply the polynomial logarithm at a nonzero tame value. It then intertwines \(r\) by (11). Conversely, a map intertwining \(r\) and \(N\) intertwines \(\rho\). This proves full faithfulness as well as essential surjectivity. ∎

In the alternative decomposition \(w=\Phi^n\sigma\), (11) reads
\[
r(\Phi^n\sigma)=\rho(\Phi^n\sigma)\exp(-t_\ell(\sigma)N).
\tag{13}
\]
Indeed \(c(\Phi^n\sigma)=q^{-n}t_\ell(\sigma)\). Moving the exponential from one side to the other without this factor would produce the wrong formula.

There is a domain error in the displayed parametrization in Blasius's **arXiv version 1**, submitted November 1, 2005, §1.3. With that version's geometric convention \(\|\Phi\|=q^{-1}\), its argument of \(t_\ell\) uses \(\Phi^{-\log_q\|w\|}w\); at \(w=\Phi\) this is \(\Phi^2\), which is outside inertia. The required inertia element is \(\Phi^{\log_q\|w\|}w\). Writing it as \(\sigma\) gives (13). This comparison concerns that arXiv version; it makes no assertion about the published version.

**Proposition 3.2 (independence of choices).** The isomorphism class of the associated Weil–Deligne representation is independent of \(\Phi\) and of the basis used for the tame character.

*Proof.* First let \(\Phi'=a\Phi\) with \(a\in I\). Both cocycles restrict to \(t_\ell\) on \(I\). Their difference factors through \(\mathbf Z\); it is determined by its value on \(\Phi\) using (10). With
\[
b=\frac{t_\ell(a)}{1-q^{-1}},
\qquad c'(w)=c(w)+(\|w\|-1)b,
\tag{14}
\]
the cocycle on the right vanishes at \(\Phi'\), so it is the new cocycle. Thus \(r'(w)=h r(w)h^{-1}\), where \(h=\exp(bN)\); also \(hNh^{-1}=N\).

Now replace \(t_\ell\) by \(u t_\ell\), where \(u\in\mathbf Z_\ell^\times\). Equations (6) and (11) replace \(N\) by \(u^{-1}N\) and leave \(r\) unchanged. We prove that \((r,N)\simeq(r,dN)\) for every \(d\in E^\times\), even when \(r(\Phi)\) is not semisimple.

Choose \(m>0\) such that \(T=r(\Phi)^m\) centralizes the finite group \(r(I)\). It then centralizes \(r(W_F)\). Decompose \(V\) into primary spaces \(V_f\) of \(T\), indexed by monic irreducible polynomials \(f\in E[X]\) with nonzero roots. They are \(r(W_F)\)-stable. Relation \(TN=q^{-m}NT\) sends the primary space with roots \(A\) into the primary space with roots \(q^{-m}A\). The corresponding operation on irreducible polynomials is
\[
f(X)\longmapsto q^{-m\deg f}f(q^mX).
\tag{15}
\]
Its orbits have no cycles: a cycle would make a finite nonzero root set invariant under a nontrivial power of \(q^{-m}\). Label each orbit by integers so that (15) raises the label by one. On the space with label \(j\), let \(h\) be the scalar \(d^j\). Then \(h\) commutes with \(r\) and \(hNh^{-1}=dN\). This proves the desired isomorphism over \(E\) itself. ∎

The fixed-choice functors are equivalences. Changing Frobenius gives the displayed natural conjugation; rescaling the tame character gives the same isomorphism classes, with an isomorphism supplied by the primary decomposition. No canonical choice of the latter grading is asserted.

**Proposition 3.3 (extension to \(G_F\)).** A continuous representation of \(W_F\) extends continuously to \(G_F\) if and only if every eigenvalue of \(\rho(\Phi)=r(\Phi)\) is an \(\ell\)-adic unit.

*Proof.* Necessity follows from a \(G_F\)-stable lattice: Frobenius and its inverse preserve it, so its eigenvalues and their inverses are integral. For sufficiency, the characteristic polynomial of \(A=\rho(\Phi)\) is integral and has unit constant term. Cayley–Hamilton implies that the algebra \(\mathcal O_E[A,A^{-1}]\) is finite over \(\mathcal O_E\). Applying this algebra to any lattice constructs a lattice preserved by \(A\) and \(A^{-1}\). Thus \(\{A^n:n\in\mathbf Z\}\) is bounded. The set \(\rho(I)\) is compact, so \(\rho(W_F)=\rho(I)\{A^n\}\) is bounded and has compact closure. A stable lattice for that closure identifies \(\rho\) with compatible continuous homomorphisms into finite congruence quotients. The profinite completion of \(W_F\) is \(G_F\), so these homomorphisms extend uniquely; their inverse limit gives the extension. ∎

For example \(r(\Phi)=\ell\), \(r(I)=1\), \(N=0\) is a valid one-dimensional Weil–Deligne representation. It corresponds to a continuous Weil-group character, but cannot extend to \(G_F\). Thus the commutation relation alone characterizes the Weil-group equivalence, rather than the Galois-group extension. Blasius's arXiv version 1, §1.3, omits this additional unit condition when asserting extension to the Galois group. Proposition 3.3 supplies it.

## 4. Frobenius semisimplification retains \(N\)

The earlier Weil-group lesson proved its semisimplicity criterion over \(\mathbf C\). We need the following coefficient-field extension of that proof.

**Lemma 4.0 (the coefficient-field bridge).** For a smooth representation \(r\) over any characteristic-zero field \(E\), the representation \(r\) is semisimple if and only if \(r(\Phi)\) is semisimple as a matrix.

*Proof.* Let \(H=r(I)\), a finite group, and \(A=r(\Phi)\). Since conjugation by \(A\) permutes \(H\), some \(m>0\) makes \(T=A^m\) centralize \(H\). It also commutes with \(A\), so it centralizes \(r(W_F)\).

Suppose first that \(A\) is semisimple. Choose a finite Galois extension \(K/E\) containing all eigenvalues \(\lambda\) of \(T\) and elements \(c_\lambda\) with \(c_\lambda^m=\lambda\). These eigenvalues are nonzero. Over \(K\), decompose \(V_K\) into the eigenspaces \(V_\lambda\) of \(T\). Each is stable under \(H\) and \(A\). On it put \(B_\lambda=c_\lambda^{-1}A\). Then \(B_\lambda^m=1\), and \(B_\lambda\) normalizes the image of \(H\). The group generated by those two images is finite: each of its elements is \(hB_\lambda^j\), with \(h\in H\) and \(0\le j<m\).

Let \(U\subset V\) be a \(W_F\)-stable \(E\)-subspace. The spectral projectors of \(T\) preserve \(U_K\), so \(U_K=\bigoplus_\lambda(U_K\cap V_\lambda)\). On each \(V_\lambda\), average an arbitrary projection onto \(U_K\cap V_\lambda\) over the finite group just constructed. Division by its order is valid in characteristic zero. The resulting projection commutes with \(H\) and \(B_\lambda\), and hence with \(A\). Their direct sum is a \(W_F\)-equivariant \(K\)-linear projection \(p:V_K\to U_K\).

For \(\gamma\in\operatorname{Gal}(K/E)\), conjugate the coefficients of \(p\). Since \(r\) and \(U\) are defined over \(E\), every \(\gamma(p)\) remains equivariant, has image in \(U_K\), and restricts to the identity on \(U_K\). Therefore
\[
p_E=\frac{1}{[K:E]}\sum_{\gamma\in\operatorname{Gal}(K/E)}\gamma(p)
\]
has coefficients in \(E\), has image in \(U\), and is identity on \(U\). It is a projection, whose kernel is an invariant complement. Every invariant subspace has such a complement, proving semisimplicity over \(E\).

Conversely, suppose that \(r\) is irreducible over \(E\). The central operator \(T\) belongs to the division algebra \(\operatorname{End}_{W_F}(V)\). Its finite-dimensional commutative subalgebra \(E[T]\) has no zero divisors and is a field: multiplication by any nonzero element is injective, hence surjective. Thus the minimal polynomial \(f\) of \(T\) is irreducible and separable over \(E\). It has no zero root because \(T\) is invertible. The polynomial \(f(X^m)\) annihilates \(A\) and is separable: at a root \(x\), both \(x\ne0\) and \(f'(x^m)\ne0\), so its derivative \(mx^{m-1}f'(x^m)\) is nonzero. Hence \(A\) is semisimple. Apply this to each irreducible summand when \(r\) is semisimple. ∎

Let \(A=r(\Phi)=S U\) be its multiplicative Jordan decomposition: \(S\) is semisimple, \(U\) unipotent, and they commute. Lemma 2.0 proves that the components are polynomials in \(A\) over the characteristic-zero coefficient field.

**Proposition 4.1.** The unipotent component \(U\) centralizes \(r(W_F)\) and commutes with \(N\). The rule
\[
r^{\mathrm{F\!ss}}(w)=r(w)U^{-v(w)}
\tag{16}
\]
defines a smooth semisimple representation and a Weil–Deligne pair \((r^{\mathrm{F\!ss}},N)\). Its isomorphism class is independent of the Frobenius lift.

*Proof.* Some power \(A^m\) centralizes \(r(I)\). Its unipotent component is \(U^m\), so \(U^m\), a polynomial in \(A^m\), centralizes \(r(I)\). Its unique unipotent \(m\)-th root is a polynomial in \(U^m\), obtained from the finite logarithm and exponential. Hence \(U\) centralizes \(r(I)\) and also \(A\).

On \(\mathrm{End}(V)\), the Jordan components of \(\mathrm{Ad}(A)\) are \(\mathrm{Ad}(S)\) and \(\mathrm{Ad}(U)\). Relation (3) makes \(N\) an eigenvector with eigenvalue \(q^{-1}\), so the unipotent component acts trivially on \(N\). Therefore \(UN=NU\). Formula (16) is consequently multiplicative and preserves (3). Its Frobenius is \(S\); Lemma 4.0 proves semisimplicity of its underlying representation over the original field \(E\).

For a different lift \(\Phi'=i\Phi\), write \(r(\Phi')=r(i)S U\). The matrix \(r(i)S\) is semisimple: some positive power lies in the group generated by a central semisimple power of \(S\) and a finite-order inertia element, and can be made a semisimple power of \(S\). An invertible matrix with a semisimple positive power is semisimple in characteristic zero. Since \(U\) commutes with \(r(i)S\), it remains the unipotent Jordan component of \(r(\Phi')\). Thus (16) is unchanged. The conjugations in Proposition 3.2 also conjugate Jordan components, giving the assertion for the pair attached to \(\rho\). ∎

Here is a worked example. Let \(M=E^2\), let inertia act trivially, and put
\[
A_M=\begin{pmatrix}1&1\\0&1\end{pmatrix},
\qquad (r,N)=M\otimes\mathrm{Sp}(2),
\qquad r(\Phi)=A_M\otimes\operatorname{diag}(1,q^{-1}),
\quad N=1\otimes N_2.
\tag{17}
\]
The Jordan components are \(S=1\otimes\operatorname{diag}(1,q^{-1})\) and \(U=A_M\otimes1\). Equation (16) gives \(\mathrm{Sp}(2)\oplus\mathrm{Sp}(2)\), with \(N\) still of rank two. In contrast, the ordinary semisimplification as a representation of the whole Weil–Deligne group has \(N=0\) and characters \(1,1,\|\cdot\|,\|\cdot\|\). Frobenius semisimplification preserves the monodromy information needed by local factors.

## 5. Classification by graded nilpotent chains

**Theorem 5.1.** Every Frobenius-semisimple Weil–Deligne representation over a characteristic-zero field \(E\) is a direct sum of pairs
\[
\tau\otimes\mathrm{Sp}(n),
\qquad \tau\text{ irreducible smooth},\quad n\ge1.
\tag{18}
\]
Each such pair is indecomposable. The multiset of pairs is unique up to isomorphism and permutation.

*Proof.* The underlying \(r\) is semisimple by Lemma 4.0. Group its irreducible types into orbits under \(\tau\mapsto\tau\|\cdot\|\). There are no nontrivial self-twists of this form: if \(\tau\simeq\tau\|\cdot\|^j\), taking determinants at \(\Phi\) gives \(q^{-j\dim\tau}=1\), hence \(j=0\).

Fix an orbit representative \(\tau\), and write its isotypic spaces as \(V_j\), of type \(\tau\|\cdot\|^j\). Relation (3) implies
\[
N V_j\subset V_{j+1}.
\tag{19}
\]
Indeed applying \(N\) to an intertwining copy of \(\tau\|\cdot\|^j\) gives an intertwining map from \(\tau\|\cdot\|^{j+1}\); zero is allowed. Distinct orbits therefore form direct summands of the pair.

Over an algebraically closed field, write \(V_j=\tau\|\cdot\|^j\otimes M_j\). Schur’s lemma expresses \(N\) as the identity on \(\tau\) times a linear map \(M_j\to M_{j+1}\). We must classify a finite-dimensional graded vector space \(M=\bigoplus_j M_j\) with a nilpotent operator raising degree by one.

Let \(n\) be the largest length of a nonzero chain. Choose a homogeneous \(x\in M_a\) with \(N^{n-1}x\ne0\); then \(N^n=0\) on all of \(M\). Choose a functional \(f\) supported in degree \(a+n-1\), with \(f(N^{n-1}x)=1\). Define
\[
\pi(y)=\sum_{k=0}^{n-1}f(N^{n-1-k}y)N^k x.
\tag{20}
\]
For homogeneous \(y\) of degree \(d\), the only possible nonzero term has \(k=d-a\), so \(\pi\) preserves degrees. It is the identity on each \(N^k x\): the matching term is one, and all other terms vanish by degree. Finally \(\pi N=N\pi\); shifting the sum proves this, with the extra end terms zero because \(N^n=0\). Thus the chain generated by \(x\) has the graded, \(N\)-stable complement \(\ker\pi\). Induction on dimension splits \(M\) into chains. A chain from degrees \(a\) through \(b\) yields \(\tau\|\cdot\|^a\otimes\mathrm{Sp}(b-a+1)\).

For uniqueness, set \(R_{a,b}=\operatorname{rank}(N^{b-a}:M_a\to M_b)\) for \(a\le b\). In a chain decomposition, it counts the intervals covering every degree from \(a\) to \(b\). Therefore the number of chains beginning exactly at \(a\) and ending exactly at \(b\) is
\[
R_{a,b}-R_{a-1,b}-R_{a,b+1}+R_{a-1,b+1}.
\tag{21}
\]
These numbers are determined by the pair itself. A single chain has exactly one interval and admits no nontrivial direct-sum decomposition, proving indecomposability and uniqueness.

For a general characteristic-zero field, let \(D=\mathrm{End}_{W_F}(\tau)\), a finite-dimensional division algebra over \(E\). The multiplicity spaces \(M_j=\mathrm{Hom}_{W_F}(\tau\|\cdot\|^j,V_j)\) are right \(D\)-vector spaces, and evaluation identifies \(V_j=M_j\otimes_D\tau\|\cdot\|^j\). Equation (19) induces right \(D\)-linear maps between them. The same chain proof applies: choose a right \(D\)-linear \(f\), and write the projection as \(\sum_k(N^k x)f(N^{n-1-k}y)\). Every computation in (20) is unchanged. Use ranks over \(D\) in (21). This supplies the decomposition and uniqueness over \(E\), without a descent assumption. ∎

For an unramified pair over an algebraically closed field, every \(\tau\) is a character determined by a nonzero scalar \(c=\tau(\Phi)\). Its blocks have Frobenius eigenvalues \(c,cq^{-1},\ldots,cq^{-(n-1)}\), linked in that order by \(N\). Listing the eigenvalues alone does not specify which chains occur; the ranks in (21) provide the missing information.

## 6. Factors and explicit blocks

For a complex Weil–Deligne representation, set \(K_N=(\ker N)^I\). The local factors are
\[
\begin{aligned}
L(s,(r,N))&=\det(1-q^{-s}r(\Phi)\mid K_N)^{-1},\\
\epsilon(s,(r,N),\psi,dx)
&=\epsilon(s,r,\psi,dx)\,
\det(-q^{-s}r(\Phi)\mid V^I/K_N),\\
a(r,N)&=a(r)+\dim V^I-\dim K_N.
\end{aligned}
\tag{22}
\]
The epsilon factor on the right is the smooth factor from the preceding lesson, with \(\epsilon(s,r)=\epsilon(r\|\cdot\|^s)\). Determinants on zero-dimensional spaces are one. The subspace \(K_N\) is Frobenius-stable by (3). A change of Frobenius multiplies by an inertia element, which acts trivially on these invariant spaces; the factors are therefore independent of its lift. Conjugating the pair or multiplying \(N\) by a nonzero scalar preserves them. Direct sums give products, and conductors add.

**Lemma 6.0 (an abstract coefficient-field isomorphism).** The fields \(\overline{\mathbb Q}_\ell\) and \(\mathbb C\) are isomorphic as abstract fields. Such an isomorphism is a choice of algebraic field structure; the construction makes no assertion about the two topologies.

**Proof.** Write \(\mathfrak c=2^{\aleph_0}\). The digit expansion of \(\mathbb Q_\ell\) gives cardinality \(\mathfrak c\): its elements are determined by a countable sequence from a finite digit set and an integer valuation, and the sequences using only the digits zero and one give \(\mathfrak c\) distinct elements of \(\mathbb Z_\ell\). Adjoining roots of all polynomials does not change this infinite cardinality: there are \(\mathfrak c\) finite coefficient tuples and each polynomial has finitely many roots. Thus \(|\overline{\mathbb Q}_\ell|=\mathfrak c\). The real binary expansions, with the two expansions of a dyadic number identified, give \(|\mathbb R|=\mathfrak c\); taking pairs gives \(|\mathbb C|=\mathfrak c\).

In either algebraically closed field, choose a maximal algebraically independent subset \(S\) over \(\mathbb Q\), by applying Zorn's lemma to the independent subsets ordered by inclusion. Its union along any chain is independent because a polynomial relation uses finitely many elements, contained in one member of that chain. Maximality implies that the entire field is algebraic over \(\mathbb Q(S)\): an element transcendental over it could be adjoined to the independent set. The rational function field \(\mathbb Q(S)\), and its algebraic closure, have cardinality \(\max(\aleph_0,|S|)\), by counting finite tuples, polynomials and their finite root sets. Since \(\mathfrak c>\aleph_0\), the preceding cardinalities force \(|S|=\mathfrak c\) in both fields.

A bijection of these two bases induces an isomorphism of their rational function fields fixing \(\mathbb Q\). Extend it to the algebraic closures by maximal extension of embeddings: if an algebraic element is missing from the domain, a root of the image of its minimal polynomial in the algebraically closed target extends the embedding, contradicting maximality. The resulting embedding is onto as well. Its image is algebraically closed, and the target is algebraic over that image because it is algebraic over the image rational function field; an algebraic extension of an algebraically closed field is trivial. This proves the isomorphism. \(\square\)

For \(\ell\)-adic coefficients choose a field isomorphism supplied by Lemma 6.0, \(\overline{\mathbf Q}_\ell\simeq\mathbf C\) and transport the algebraic pair, not its \(\ell\)-adic topology. Its inertia image is finite, so the transported smooth representation is continuous in the complex topology. The isomorphism is a choice; independence across coefficient places requires compatibility, the topic of a later lesson.

**Theorem 6.1.** Let \(\chi\) be unramified, let \(c=\chi(\Phi)\), and let \(n\ge1\) denote a block length. Then
\[
L(s,\chi\otimes\mathrm{Sp}(n))
=\frac1{1-cq^{-s-(n-1)}}
=L(s,\chi\|\cdot\|^{n-1}),
\qquad a(\chi\otimes\mathrm{Sp}(n))=n-1.
\tag{23}
\]
Let \(h=n(\psi)\) denote the additive-character conductor convention of the preceding lesson: \(\psi\) is trivial on \(\varpi^{-h}\mathcal O_F\) and nontrivial on \(\varpi^{-h-1}\mathcal O_F\). Put \(e_\chi=\epsilon(\chi,\psi,dx)\). Then
\[
\epsilon(s,\chi\otimes\mathrm{Sp}(n),\psi,dx)
=e_\chi^n(-c)^{n-1}
q^{-h n(n-1)/2-(n-1)(n-2)/2}
q^{-(nh+n-1)s}.
\tag{24}
\]

*Proof.* The kernel of \(N\) is \(Ee_{n-1}\), on which Frobenius is \(cq^{-(n-1)}\), proving (23). All inertia acts trivially, so the correction to the smooth conductor is \(n-1\). The underlying smooth representation is \(\bigoplus_{j=0}^{n-1}\chi\|\cdot\|^j\). The unramified twist formula of the preceding lesson gives its epsilon factor
\[
e_\chi^n q^{-h n(n-1)/2}q^{-nhs}.
\tag{25}
\]
The quotient in (22) has basis the classes of \(e_0,\ldots,e_{n-2}\), so its determinant is \((-c)^{n-1}q^{-(n-1)(n-2)/2}q^{-(n-1)s}\). Multiply to obtain (24). ∎

For the common normalization \(h=0\), \(\operatorname{vol}(\mathcal O_F)=1\), the unramified formula gives \(e_\chi=1\), and (24) becomes
\[
(-c)^{n-1}q^{-(n-1)(n-2)/2}q^{-(n-1)s}.
\tag{26}
\]
In particular,
\[
L(s,\mathrm{Sp}(2))=(1-q^{-s-1})^{-1},
\qquad \epsilon(s,\mathrm{Sp}(2))=-q^{-s}.
\tag{27}
\]
Twisting by \(\|\cdot\|^{-1/2}\) replaces \(s\) by \(s-1/2\). Thus the normalized block has
\[
L(s,\mathrm{Sp}(2)\|\cdot\|^{-1/2})=(1-q^{-s-1/2})^{-1},
\qquad \epsilon(s)=-q^{1/2-s}.
\tag{28}
\]
Its root number at \(s=1/2\) is \(-1\). This is the block normalization used for the Steinberg parameter.

If \(\chi\) is ramified, all invariant spaces in (22) vanish. Consequently the block has \(L=1\), conductor \(n a(\chi)\), and epsilon factor
\[
e_\chi^n q^{-(a(\chi)+h)n(n-1)/2}
q^{-n(a(\chi)+h)s}.
\tag{29}
\]
This follows by the same product calculation, with no monodromy determinant correction.

### 6A. The geometric Tate identification before use

Let \(Q\in F^\times\) have positive valuation \(m\), and continue to assume \(\ell\ne p\). We prove the uniformization and its Galois-module consequence here before identifying the block with an elliptic curve. The constructions work in both characteristics. The earlier Tate-module lesson supplies the already proved cubic group law and its divisor interpretation; the valuation, Hensel and tame-character facts are proved in the first lesson and Proposition 1.0 above.

Put
\[
S_r(Q)=\sum_{n\ge1}\frac{n^rQ^n}{1-Q^n},\quad
A_4=-5S_3(Q),\quad A_6=-\frac{5S_3(Q)+7S_5(Q)}{12}.
\tag{6T8a}
\]
The coefficients of \(A_6\) are integers: \(12\mid5n^3+7n^5\), because \(n^3(n^2-1)\) is divisible by 12. Thus these are integral convergent power series, even at 2 and 3. Define
\[
\begin{aligned}
X(z)&=\sum_{n\in\mathbf Z}\frac{Q^nz}{(1-Q^nz)^2}-2S_1(Q),\\
Y(z)&=\sum_{n\in\mathbf Z}\frac{(Q^nz)^2}{(1-Q^nz)^3}+S_1(Q).
\end{aligned}
\tag{6T8b}
\]
They converge uniformly on closed annuli avoiding \(Q^{\mathbf Z}\). For negative \(n\), replacing \(Q^nz\) by its reciprocal bounds the summand by a constant times \(|Q|^{-n}\); for positive \(n\) the bound is a constant times \(|Q|^n\). Rearrangement gives
\[
X(Qz)=X(z)=X(z^{-1}),\quad
Y(Qz)=Y(z),\quad Y(z^{-1})=-X(z)-Y(z).
\tag{6T8c}
\]

**Lemma 6.2 (the split Tate uniformization, in either characteristic).** The equation
\[
E_Q:\quad y^2+xy=x^3+A_4x+A_6
\tag{6T8d}
\]
is an elliptic curve. Sending \(z\notin Q^{\mathbf Z}\) to \((X(z),Y(z))\) and \(Q^{\mathbf Z}\) to its origin induces a Galois-equivariant group isomorphism
\[
E_Q(\bar F)\simeq\bar F^\times/Q^{\mathbf Z}.
\tag{6T8}
\]
*Proof.* Put \(b_2=1,b_4=2A_4,b_6=4A_6,b_8=A_6-A_4^2\). The polynomial \(\Delta=-b_2^2b_8-8b_4^3-27b_6^2+9b_2b_4b_6\) detects a singular affine point. Here is the elimination in every characteristic. Write \(a=A_4,b=A_6\). The derivative equations force \(y=3x^2+a\) and \(S=6x^2+x+2a=0\); substitution in the cubic gives \(T=9x^4+2x^3+6ax^2+a^2-b=0\). In characteristic two these conditions reduce to \(x=0,y=a,a^2-b=0\); in characteristic three they reduce to \(x=a,y=a,-a^3+a^2-b=0\). Those last expressions are exactly \(\Delta\) in the respective characteristics. Otherwise, writing \(r_1,r_2\) for the two roots of \(S\), counted with multiplicity, expansion gives \(6^4T(r_1)T(r_2)=-3\Delta\). Thus a common root exists exactly when \(\Delta=0\). The origin at infinity is smooth by its nonzero homogeneous \(Z\)-derivative. Substituting (6T8a) now gives the integer series \(\Delta=Q+O(Q^2)\). For the complex argument restrict \(Q\) to a sufficiently small punctured disc on which \(\Delta\ne0\); the cubic is therefore smooth before its group law is used. This open set suffices to establish the universal coefficient identities. Put \(z=e^u\) and \(\Lambda=2\pi i\mathbf Z+\log(Q)\mathbf Z\). The function \(L(u)=X(e^u)+1/12\) is periodic for this lattice, and has only double poles at its points. Expanding the geometric series in (6T8b) gives
\[
L(u)=u^{-2}+\left(\frac1{240}+S_3(Q)\right)u^2
       +\left(-\frac1{6048}+\frac{S_5(Q)}{12}\right)u^4+O(u^6).
\]
Its derivative is \(H(u)=X(e^u)+2Y(e^u)\). With
\(g_2=1/12+20S_3(Q)\), \(g_3=-1/216+(7/3)S_5(Q)\), the periodic function
\(H^2-4L^3+g_2L+g_3\) has no poles: the displayed Laurent coefficients cancel its terms of degrees \(-6,-2,0\). It is bounded on a compact period parallelogram and therefore on the plane, and hence constant. Here is the complex-analysis proof needed for that implication and for the following contour calculation. Every analytic function used here is locally a convergent power series, by expanding the denominators of (6T8b) on a sufficiently small disc avoiding their poles; their geometric bounds allow coefficient summation and convergence on that disc. Such a series has a local primitive by termwise integration. Subdivide a compact region avoiding poles into sufficiently small cells lying in these power-series discs; integrals around each cell vanish, and cancellation of common edges proves the contour theorem for that region. Removing a small disc about \(a\) and applying it to \(F(u)/(u-a)\) gives
\[
F(a)=\frac1{2\pi i}\int_{|u-a|=R}\frac{F(u)}{u-a}\,du.
\]
Expanding the denominator for a variable point near \(a\) gives its Taylor coefficient formula and the bound \(|c_n|\le \sup_{|u-a|=R}|F(u)|/R^n\). If \(F\) is entire and bounded, let \(R\to\infty\); every positive-degree coefficient vanishes. It is constant. Applying this to the periodic expression above, its constant Laurent coefficient is zero, so it vanishes. Expanding gives exactly (6T8d).

We also justify its addition law without assuming an analytic uniformization theorem. For a meromorphic \(\Lambda\)-periodic function, its zeros and poles, counted with multiplicities, have equal number and the sum of their locations differs by a lattice point. Indeed near a zero or pole write \(f(u)=(u-a)^m h(u)\), with \(h\) nonvanishing. Its logarithmic derivative has residue \(m\), and \(u f'/f\) has residue \(ma\). The just-proved contour theorem, after removing small circles about these points, shows that their boundary integrals are \(2\pi i\sum m\) and \(2\pi i\sum ma\). For \(f'/f\), opposite sides of a period parallelogram cancel. For \(u f'/f\), pairing them gives a period times the integral of \(f'/f\) along each of the other two sides. Such a side integral is \(2\pi i\) times an integer: if \(J(t)\) is its integral up to time \(t\), differentiating \(e^{-J(t)}f(u(t))\) makes it constant, and equality of the endpoint values of \(f\) gives \(e^{J(1)}=1\). Since the kernel of the complex exponential is \(2\pi i\mathbf Z\), the weighted integral belongs to \(2\pi i\Lambda\). These facts prove both assertions. Choose the parallelogram to avoid its finitely many zeros and poles on the boundary; isolated zeros follow from the first nonzero Taylor coefficient, so such a choice exists.

The function \(Y(e^u)-\lambda X(e^u)-\nu\) has a triple pole at the lattice origin and no other poles. Its three intersection parameters therefore sum to zero modulo \(\Lambda\). They give the three cubic intersection points for a generic line: \(X-c\) has just two zeros, since its only pole has order two, and these are the parameters \(u,-u\) by (6T8c). Their \(Y\)-values are opposite and distinct away from the finitely many zeros of \(H=X+2Y\). Thus the parametrization is generically injective, so those three generic line zeros represent three distinct intersections. The divisor form of the cubic group law, proved in §1 of the earlier Tate-module lesson, and (6T8c) now show that multiplication of \(z\)'s is addition of points. Equivalently, for generic \(z_1,z_2\), set
\[
\lambda=\frac{Y(z_2)-Y(z_1)}{X(z_2)-X(z_1)},\quad
\nu=Y(z_1)-\lambda X(z_1),\quad
x_3=\lambda^2+\lambda-X(z_1)-X(z_2).
\]
The identities are \(X(z_1z_2)=x_3\) and \(Y(z_1z_2)=-(\lambda+1)x_3-\nu\).

These are universal identities, rather than assertions restricted to complex points. Write (6T8b) as power series in \(Q\); every coefficient is a rational function with integer coefficients in \(z,z^{-1},(1-z)^{-1}\). After clearing the displayed denominators, each coefficient of the curve and addition identities is a rational function that vanishes on an open set of complex parameters. Its numerator polynomial is therefore identically zero. Specializing their convergent series proves the identities over every complete nonarchimedean field here.

The already computed integer series \(\Delta=Q+O(Q^2)\) has \(v(\Delta)=m\) in the nonarchimedean field, so the cubic is smooth. Its reduction is \(y^2+xy=x^3\), whose two tangent lines \(y=0,y=-x\) are distinct even in characteristic 2. The map \(\phi\) defined by (6T8b) is periodic, and its preimage of the origin is exactly \(Q^{\mathbf Z}\), since its other values have finite affine coordinates.

The generic addition identities extend to every pair. To see this without dividing by a vanishing slope denominator, observe that the image is infinite: at \(z=1+Q^h\), for sufficiently large positive integers \(h\), the term \(z/(1-z)^2\) uniquely dominates \(X(z)\), and \(|X(z)|=|Q|^{-2h}\). Given \(a,b\), choose \(w\) so that the three additions involving \((w,a),(wa,b),(w,ab)\) all have distinct affine \(x\)-coordinates. Only finitely many image points are excluded: for the middle pair use the already valid identity \(\phi(wa)=\phi(w)+\phi(a)\). Such a \(w\) exists by the infinite image. Comparing \(\phi(wab)\) by those identities and cancelling \(\phi(w)\) proves \(\phi(ab)=\phi(a)+\phi(b)\). Identity or inverse cases are covered by (6T8c) and the same auxiliary-point argument. This proves the homomorphism and its kernel.

For surjectivity we need a power-series fact, whose proof is useful here. If
\(f(T)=T+\sum_{h\ge1}c_hT^{h+1}\) with \(|c_h|\le\rho^h\), formal recursive solution of \(f(g(T))=T\) gives
\(g(T)=T+\sum_{h\ge1}d_hT^{h+1}\) with \(|d_h|\le\rho^h\). At each step the new coefficient is a sum of integer multiples of products of earlier coefficients with total weight \(h\); the ultrametric inequality gives this bound by induction. Both series converge on \(|T|<\rho^{-1}\), their correction terms have smaller norm than \(T\), and formal composition converges there. Thus \(f\) bijects that disc with itself, with inverse \(g\).

Let \((x,y)\in E_Q(L)\), where \(L/F\) is any finite extension. Set \(\rho=|Q|^{1/2}<1\). First suppose \(|x|>\rho\). Put \(r=z+z^{-1}-2\). The integer polynomials
\(F_n(r)=z^n+z^{-n}-2\) satisfy
\[
F_0=0,\quad F_1=r,\quad
F_{n+1}=(r+2)F_n-F_{n-1}+2r;
\]
they have degree \(n\), zero constant term and integer coefficients. Expansion of (6T8b) consequently gives
\[
X(z)=r^{-1}+\sum_{h\ge1}a_h r^h,\qquad |a_h|\le|Q|^h.
\]
Its reciprocal is \(r+\sum_{h\ge1}c_h r^{h+1}\), with \(|c_h|\le\rho^h\): the denominator terms have weights \(h+1\) and norms at most \(|Q|^h\le\rho^{h+1}\). The inverse fact uniquely solves \(1/x=1/X\) for \(|r|<\rho^{-1}\). A root of \(z^2-(r+2)z+1=0\) lies in an extension of degree at most two. Both roots have norms between \(\rho\) and \(\rho^{-1}\), or both have norm one, by comparing the three terms of the quadratic. Thus the series expansions used are valid and give \(X(z)=x\).

Second suppose \(|x|<1\). Put \(s=z+Q/z\). The polynomials \(G_n(s,Q)=z^n+(Q/z)^n\) satisfy
\(G_0=2,G_1=s,G_{n+1}=sG_n-QG_{n-1}\). On \(|Q|<|z|<1\), (6T8b) becomes
\[
X(z)=-2S_1(Q)+\sum_{n\ge1}\frac{n}{1-Q^n}G_n(s,Q)
     =c_0+c_1s+\sum_{h\ge2}c_hs^h.
\]
The recurrence gives \(|c_0|<1\), \(c_1\in1+Q\mathcal O_L\), and \(|c_h|\le1\). Apply the inverse fact with \(\rho=1\) after subtracting \(c_0\) and dividing by \(c_1\). It supplies \(|s|<1\) with this value \(x\). The roots of \(z^2-sz+Q=0\) both have norm less than one: otherwise its quadratic term would uniquely dominate. Their product is \(Q\), so each also has norm greater than \(|Q|\). Hence this expansion applies and again \(X(z)=x\). The two cases cover every \(x\), since \(\rho<1\).

The two points \(\phi(z),\phi(z^{-1})\) have the same \(x\)-coordinate and are negatives by (6T8c); they are precisely the roots of the quadratic equation for \(y\). Replace \(z\) by its inverse if necessary to obtain \((x,y)\). The quadratics used are separable, except for repeated roots already in \(L\) and one case if one also applies this construction to a complete field of characteristic 2: the second quadratic with \(s=0\), namely \(z^2=Q\). That case has direct descent. Periodicity gives \(\phi(z^{-1})=\phi(z)\), since \(z^{-1}=z/Q\); (6T8c) therefore forces \(x=0\), and (6T8d) gives \(y^2=A_6(Q)\). In characteristic 2 separate the even and odd coefficients of its integer series to write
\[
A_6(Q)=c(Q)^2+Q b(Q)^2,
\qquad b(Q)\in1+Q\mathbf F_2[[Q]],\quad c(Q)\in Q\mathbf F_2[[Q]].
\]
Indeed each prime-field coefficient is its own square, and the coefficient of \(Q\) in \(A_6\) is one. The convergent series \(b,c\) belong to \(L\), and
\(z=(y+c(Q))/b(Q)\in L\), by uniqueness of a square root in characteristic 2. Thus no inseparable descent assertion is used.

In all the remaining cases \(z\) lies in a finite separable extension of \(L\). For any automorphism \(\sigma\) of its Galois closure over \(L\), equivariance and the kernel imply \(\sigma(z)/z=Q^a\). An automorphism of a finite extension of a complete valued field preserves its unique extended absolute value, so \(a=0\). Thus \(z\in L\). This proves surjectivity over every finite \(L/F\), and taking their union proves (6T8). All series coefficients lie in \(F\), proving Galois equivariance.

∎

This proof reconstructs the actual constructions in Tate's freely accessible *A review of non-Archimedean elliptic functions*, first part, pp.2–12, including both inverse-series arguments. The formal identities, kernel and surjectivity have all been established above; the source link supplies a primary account, not an omitted implication.

**Proposition 6.3 (the Galois extension and its Kummer cocycle).** There is a short exact sequence
\[
0\longrightarrow\mathbf Z_\ell(1)
\longrightarrow T_\ell E_Q
\longrightarrow\mathbf Z_\ell
\longrightarrow0,
\tag{6T9}
\]
whose class is the Kummer class \(\kappa(Q)\in H^1(G_F,\mathbf Z_\ell(1))\). On inertia it satisfies
\[
\kappa(Q)(\sigma)=m\,t_\ell(\sigma).
\tag{6T10}
\]
Consequently the rational extension is nonsplit on inertia and the inertia image is infinite.

*Proof.* A class \([z]\) in (6T8) is killed by \(\ell^n\) exactly when \(z^{\ell^n}=Q^b\) for some integer \(b\). Send it to \(b\bmod\ell^n\). Replacing \(z\) by \(zQ^a\) changes \(b\) by \(a\ell^n\), so this is well defined. Its kernel is the group of \(\ell^n\)-th roots of unity, and it is surjective by choosing a root of \(Q\). Thus
\[
0\to\mu_{\ell^n}\to E_Q[\ell^n]\to\mathbf Z/\ell^n\to0.
\tag{6T11}
\]
Choose compatible roots \(Q_n\) with \(Q_n^{\ell^n}=Q\), and compatible primitive roots \(\zeta_n\). They form a basis of (6T11); multiplication by \(\ell\) gives the compatible bases at the previous level. Taking the inverse limit proves (6T9) directly, including surjectivity from the compatible choices. With the first basis vector denoted \(e_1\) and the second \(e_2\), write
\[
g(Q_n)/Q_n=\zeta_n^{\kappa_n(g)}.
\]
Then
\[
\rho(g)=\begin{pmatrix}\chi_\ell(g)&\kappa(Q)(g)\\0&1\end{pmatrix},
\qquad
\kappa(Q)(gg')=\kappa(Q)(g)+\chi_\ell(g)\kappa(Q)(g').
\tag{6T12}
\]
Changing the compatible roots adds a coboundary. This is precisely the Kummer cocycle and hence the extension class.

Write \(Q=\varpi^m u\), with \(u\in\mathcal O_F^\times\). Every \(\ell^n\)-th root of \(u\) can be chosen in the maximal unramified extension: choose its residue root in \(\bar k\) and lift by Hensel’s lemma, whose derivative is a unit because \(\ell\ne p\). Compatible choices give trivial inertia action on these roots. The cocycle for \(\varpi\) on inertia is the tame character, and the cocycle for \(\varpi^m\) is its \(m\)-fold multiple. This proves (6T10). Inertia also acts trivially on \(\mu_{\ell^n}\).

Thus inertia has matrices \(1+m t_\ell(\sigma)E_{12}\). Since \(m\ne0\) and \(t_\ell(I)=\mathbf Z_\ell\), their image is infinite. A split extension over \(\mathbf Q_\ell\) would have trivial inertia, because both endpoint characters are trivial there. Hence it is nonsplit. ∎

The integral and residual conclusions differ. Reduction of (6T12) modulo \(\ell\) has nontrivial inertia exactly when \(\ell\nmid m\). If \(\ell\mid m\), its inertia matrices are identity even though the rational inertia image is infinite. This distinction will matter for residual representations.

**Corollary 6.4 (the covariant Tate-module pair).** The Weil–Deligne pair of \(V_\ell E_Q\) is \(\mathrm{Sp}(2)\).

**Proof.** Proposition 6.3 gives \(\rho(\sigma)=1+m t_\ell(\sigma)E_{12}\) on inertia, with \(m=v(Q)>0\). Thus the monodromy is \(N=mE_{12}\) in its displayed basis. The geometric Frobenius matrix is \(\left(\begin{smallmatrix}q^{-1}&b\\0&1\end{smallmatrix}\right)\), since the cyclotomic action on geometric Frobenius is \(q^{-1}\), by the local calculation in the first lesson. The two eigenvalues differ. Replacing the quotient lift \(e_2\) by \(e_2+d e_1\) with \(d=-b/(q^{-1}-1)\) makes Frobenius diagonal and leaves \(N(e_2)=m e_1\). After replacing the cyclotomic vector by \(m e_1\), and ordering the basis as \(e_2,m e_1\), we have \(Ne_0=e_1,Ne_1=0\) and Frobenius eigenvalues \(1,q^{-1}\). The smooth inertia action in the equivalence of Theorem 3.1 is trivial, because its exponential monodromy factor removes exactly the displayed inertia matrices. This is the pair \(\mathrm{Sp}(2)\) defined in §5. \(\square\)

Corollary 6.4 proves that the split Tate curve has covariant Tate-module pair \(\mathrm{Sp}(2)\). Its dual is isomorphic to \(\|\cdot\|^{-1}\mathrm{Sp}(2)\): dualize the two basis lines and reverse their order, rescaling one vector to absorb the sign of the dual monodromy. Its kernel has Frobenius eigenvalue one and hence factor \((1-q^{-s})^{-1}\). This explains why the usual elliptic-curve factor belongs to the dual, cohomological convention when geometric Frobenius is used. The uniformization, geometric identification, block and dual calculations are therefore proved here before use.

## 7. What this lesson does not prove

Proposition 1.0 proves (2), including the pro-\(p\) wild kernel, the entire tame radical tower and its Frobenius action, from the first lesson’s already proved Hensel, finite-extension and unramified-field facts. The profinite completion used in Proposition 3.3 is proved in Proposition 1.1 of the earlier Weil-group lesson. The free source [Milne, ANT, Chapter 7] supplies comparison ramification proofs; its citation does not replace Proposition 1.0.

Stable lattices for compact matrix groups were proved in the first lesson. The complex smooth semisimplicity criterion was proved in the Weil-group lesson; Lemma 4.0 proves its extension to every characteristic-zero coefficient field, including nonsplit irreducibles. Lemma 2.0 proves primary decomposition, the polynomial construction and uniqueness of both Jordan decompositions over the original field, the conjugation components on endomorphisms, and the positive-power criterion. Those arguments supply the linear algebra used in Propositions 3.2 and 4.1.

The smooth epsilon factors in (22) are supplied by the preceding lesson’s Theorem 3.0, whose §§3A–3D prove existence and Brauer-relation independence, followed by its uniqueness and transformation proofs. Formula (22) is the definition of the extension to Weil–Deligne pairs, matching Deligne, §8.12. Lemma 6.2, Proposition 6.3 and Corollary 6.4 supply the Tate-curve uniformization, its Galois extension and its Weil–Deligne identification locally. The \(p\)-adic construction from potentially semistable representations, described in Berger, §II.5.2, uses period rings and lies outside the hypothesis \(\ell\ne p\) of this monodromy proof.

The theorem, equivalence, choice independence, classification and all block calculations required here have been proved above. Grothendieck’s theorem is recorded in Deligne, Theorem 8.2; Deligne’s §§8.3–8.6 supply the intrinsic and explicit parametrizations. Blasius's arXiv version 1, §§1.3–1.7, provides another organization of these objects, with a centered block convention differing by an unramified twist. The two corrections to its §1.3 used here are identified in §3 above.

## 8. Graded exercises with complete solutions

**Exercise 8.1 (easy).** Suppose \(A N A^{-1}=q^{-1}N\) over a characteristic-zero field. Prove that \(N\) is nilpotent. Explain what fails if the scaling scalar is a root of unity.

*Solution.* After extending scalars, the spectrum is a finite multiset invariant under multiplication by \(q^{-1}\). A nonzero eigenvalue would generate infinitely many distinct eigenvalues, so the spectrum consists of zero. Cayley–Hamilton gives nilpotence. If the scalar is one, \(A=N=1\) is a counterexample. More generally, for a root of unity \(z\) of order \(m\), take an invertible diagonal matrix with eigenvalues \(1,z,\ldots,z^{m-1}\) and a cyclic permutation matrix conjugating it to \(z\) times itself. Finite nonzero scaling orbits are then possible.

**Exercise 8.2 (medium).** Prove choice independence in both steps of (11), including a representation with nonsemisimple Frobenius. State precisely the integrality condition for extending to \(G_F\).

*Solution.* With \(\Phi'=a\Phi\), the difference between the cocycles is \((\|w\|-1)t_\ell(a)/(1-q^{-1})\), by their values on inertia and the new Frobenius. Formula (11) gives conjugation by \(\exp(t_\ell(a)N/(1-q^{-1}))\). Rescaling \(t_\ell\) by \(u\) gives \((r,u^{-1}N)\). Use primary spaces of the central operator \(r(\Phi)^m\), not just eigenspaces: label its irreducible-polynomial orbits under (15), and act on label \(j\) by \(u^{-j}\). This intertwines the pairs even with nontrivial Jordan blocks. The eigenvalues of \(r(\Phi)\) must all be \(\ell\)-adic units for a Galois extension; sufficiency and necessity are Proposition 3.3. The unramified value \(\ell\) shows that this condition cannot be omitted.

**Exercise 8.3 (medium).** Compute the Frobenius semisimplification, ordinary semisimplification, conductor and \(L\)-factor of (17).

*Solution.* Its unipotent Frobenius component is \(A_M\otimes1\), so removing it gives two copies of \(\mathrm{Sp}(2)\), with the same rank-two \(N\). Ordinary semisimplification has four one-dimensional characters \(1,1,\|\cdot\|,\|\cdot\|\) and zero monodromy. Inertia is trivial for the original pair, while \(\ker N=M\otimes Ee_1\) has dimension two. Thus (22) gives conductor \(4-2=2\). On that kernel, Frobenius is \(q^{-1}A_M\), with characteristic polynomial \((X-q^{-1})^2\), hence \(L(s)=(1-q^{-s-1})^{-2}\). Frobenius semisimplification has the same values. Ordinary semisimplification instead has conductor zero and factor \((1-q^{-s})^{-2}(1-q^{-s-1})^{-2}\).

**Exercise 8.4 (hard).** Prove the indecomposable classification. Then classify an unramified pair with graded multiplicity dimensions \((1,2,1)\) in degrees \(0,1,2\), whose two successive maps have rank one. Assume the composite has rank one.

*Solution.* Decompose the semisimple underlying representation into orbits of distinct twists \(\tau\|\cdot\|^j\). Relation (3) makes \(N\) a degree-one map on the multiplicity spaces. For a longest homogeneous chain, choose a functional at its last vector and construct (20); it is a graded projection commuting with \(N\). Its kernel allows induction, giving interval chains. Formula (21) recovers every interval multiplicity from ranks, proving uniqueness; a single chain cannot split. For general coefficients use right vector spaces over \(\mathrm{End}_{W_F}(\tau)\), with the same projection and ranks. This proves the full classification rather than only an unramified special case.

In the stated example, the rank-one composite forces one chain covering \([0,2]\). It uses dimensions \((1,1,1)\), leaving a one-dimensional chain in degree one. If the degree-zero character has value \(c\), the pair is \(\chi_c\otimes\mathrm{Sp}(3)\oplus\chi_c\|\cdot\|\). The two blocks give
\[
L(s)=\frac1{(1-cq^{-s-2})(1-cq^{-s-1})},
\qquad a=2.
\tag{30}
\]
If instead the composite were zero with the same successive ranks, (21) would give intervals \([0,1]\) and \([1,2]\). This demonstrates why dimensions and individual ranks alone need not identify a pair.

## References and next reading

- J. Tate, [*A review of non-Archimedean elliptic functions*, free author-site copy](https://web.ma.utexas.edu/users/voloch/Preprints/nonarch-ams.pdf), first part, pp.2–12. Lemma 6.2 and Proposition 6.3 reconstruct the uniformization and Galois-module arguments before use.
- P. Deligne, [*Les constantes des équations fonctionnelles des fonctions L*, free author-institution copy](https://publications.ias.edu/sites/default/files/Number20.pdf), 1973, §§2.1–2.2, 8.1–8.6 and 8.12.
- D. Blasius, *Hilbert modular forms and the Ramanujan conjecture*, arXiv math/0511007v1, submitted November 1, 2005, §§1.1–1.7; [version 1 manuscript](https://arxiv.org/abs/math/0511007v1).
- J. R. Getz and H. Hahn, [*An Introduction to Automorphic Representations, with a View toward Trace Formulae*, free author draft of 22 April 2022](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), §12.2, for comparison with parameters using an algebraic \(\mathrm{SL}_2\).
- R. Taylor, *Galois representations*, Annales de la Faculté des Sciences de Toulouse (6) **13** (2004), §1; [published article](https://www.numdam.org/item/AFST_2004_6_13_1_73_0/).
- L. Berger, [*An introduction to the theory of p-adic representations*, free author preprint](https://arxiv.org/abs/math/0210184), §II.5.2, for the distinct construction using potentially semistable \(p\)-adic representations.
- J. S. Milne, [*Algebraic Number Theory*, free author notes](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Chapter 7, especially Remark 7.56, Lemma 7.57, Theorem 7.58 and Corollary 7.59. Proposition 1.0 contains the tame and wild proofs used here.

Continue with *Elliptic curves over local fields and their Weil–Deligne representations*: the abstract nilpotent chain will become the extension defined by a Tate parameter.
