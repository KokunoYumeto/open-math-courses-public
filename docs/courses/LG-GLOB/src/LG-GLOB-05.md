# The principle of functoriality

*Draft lesson. Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Public domain (CC0).*

A homomorphism of L-groups acts on local parameters. Functoriality predicts that the resulting family of parameters comes from automorphic representations. Its simplest visible consequence is an identity of Euler factors. Its deeper consequences depend on the kind of automorphic representation obtained and on the places at which the parameters agree.

We make these distinctions explicit, compute quadratic induction and the symmetric square of a dihedral representation, and prove the deductions toward Ramanujan and Selberg. The prerequisites are *L-functions for GL_n: Godement–Jacquet and Rankin–Selberg* and *Beyond GL_n: L-parameters, L-packets and the local Langlands conjecture for reductive groups*. The uniqueness and analytic deductions retain the local and global analytic hypotheses and the isobaric existence statements whose general proofs are still missing in the preceding lesson.

## 1. Local parameters and a global conjecture

Let \(F\) be a number field. Fix an algebraic closure and write \(\Gamma_F=\operatorname{Gal}(\overline F/F)\). For a quasi-split connected reductive group \(H/F\), use

\[
{}^LH=\widehat H\rtimes\Gamma_F.
\tag{1.1}
\]

The Galois action is the pinned action on the dual group. One can instead pull this extension back to the Weil group. We use the same choice of Frobenius and reciprocity normalization for every group and every local L-factor. In the convention of the preceding lessons, an unramified character \(\chi_v\) has Satake eigenvalue \(\chi_v(\varpi_v)\), with \(|\varpi_v|_v=q_v^{-1}\).

An **L-homomorphism**

\[
\phi:{}^LH\longrightarrow{}^LG
\tag{1.2}
\]

commutes with projection to \(\Gamma_F\), is continuous, and restricts to an algebraic homomorphism \(\widehat H\to\widehat G\). We require the usual semisimplicity condition, so that composition takes admissible local parameters to admissible parameters. L-homomorphisms are considered up to \(\widehat G\)-conjugacy. The phrase “over \(F\)” includes the Galois factor in (1.2); a homomorphism of the connected dual groups alone need not define an L-homomorphism.

At a finite place, a local parameter has domain the Weil–Deligne group, or equivalently the Weil group together with an \(SL_2(\mathbb C)\)-factor in the usual parametrization. At an archimedean place its domain is the local Weil group. Denote either domain by \(W'_v\). Local functoriality is the operation

\[
\rho_v:W'_v\longrightarrow{}^LH_v
\quad\longmapsto\quad
\phi_v\circ\rho_v:W'_v\longrightarrow{}^LG_v.
\tag{1.3}
\]

The local Langlands conjecture asks for a correspondence attaching a packet to each parameter. For \(GL_N\), its packet contains one irreducible admissible representation; we use this correspondence where it is proved earlier or explicitly assumed. For a general \(G\), (1.3) gives a target packet under the conjectural correspondence; it does not specify a preferred member for every member of the source packet. Internal packet parametrizations and the global multiplicity conditions are additional data.

At an unramified place, normalized Satake theory already makes (1.3) concrete. The class \(c_v(\pi)\) lies in the Frobenius coset of \({}^LH_v\). Its image \(\phi_v(c_v(\pi))\) is a semisimple class in the corresponding coset of \({}^LG_v\), and hence determines an unramified representation of \(G(F_v)\). This is the meaning of \(\phi_*(\pi_v)\) at a good place. In a nonsplit group it is a coset conjugacy class, rather than an ordinary conjugacy class in \(\widehat H\).

**Definition 1.1 (weak and strong transfer).** A weak transfer of an automorphic representation \(\pi\) of \(H(\mathbb A_F)\) with respect to \(\phi\) is an automorphic representation \(\Pi\) of \(G(\mathbb A_F)\) such that

\[
c_v(\Pi)=\phi_v(c_v(\pi))\qquad(v\notin S)
\tag{1.4}
\]

for some finite set \(S\) containing the archimedean places and all relevant ramified places. A strong transfer has parameter \(\phi_v\circ\rho_{\pi_v}\) at every place, including the ramified and archimedean places, whenever the local correspondence is available. For general groups this condition specifies membership in the corresponding packets. For \(GL_N\) it specifies the local representation itself. When the target is \(GL_N\), we will explicitly require a weak transfer to be isobaric when using its uniqueness.

**Conjecture 1.2 (Langlands, 1967–1970; weak functoriality).** For quasi-split \(H,G\) and an admissible L-homomorphism (1.2), every automorphic representation \(\pi\) of \(H(\mathbb A_F)\) should have an automorphic weak transfer satisfying (1.4). A general-linear target is expected to admit an isobaric transfer. Even for unitary cuspidal \(\pi\), the transfer need not be cuspidal, and this statement alone does not say that all its isobaric constituents are unitary cuspidal representations.

This is the formulation in terms of almost all Satake classes [Langlands 1997, §3, pp.5–7; Arthur, June 2020 author draft, pp.14–15]. To state strong functoriality precisely for general groups, one must include the packet and multiplicity conditions rather than demand that every choice of local packet members be automorphic. One particularly clean formulation is the following.

**Conjecture 1.3 (tempered transfer to a general linear group).** Assume the local Langlands correspondences for \(H(F_v)\) at every place. Let \(\pi\) be an everywhere tempered cuspidal automorphic representation of \(H(\mathbb A_F)\), and let \(\phi:{}^LH\to{}^LGL_N\) be an L-homomorphism. The restricted tensor product of the unique local representations with parameters \(\phi_v\circ\rho_{\pi_v}\) is automorphic. This is [Getz–Hahn, 22 April 2022 draft, Conjecture 12.6.1, p.295], with its extension field taken to be \(F\). Its local formulation gives a tempered target.

The tempered hypothesis in Conjecture 1.3 is unsuitable as a hypothesis for a proof of Ramanujan: it would assume the desired property of the source. The argument in §5 instead states the stronger transfer hypotheses needed for a possibly nontempered cusp form. Arthur parameters describe the additional phenomena that occur outside the tempered spectrum; the final lesson returns to them.

**Proposition 1.4 (uniqueness and composition).** Isobaric weak transfers to \(GL_N\), when they exist, are unique. If \(\Pi\) is a weak transfer of \(\pi\) for \(\phi\), and \(\Omega\) is a weak transfer of \(\Pi\) for \(\psi:{}^LG\to{}^LK\), then \(\Omega\) is a weak transfer of \(\pi\) for \(\psi\circ\phi\).

**Proof.** Two isobaric transfers have the same unramified local representations outside the union of their finite exceptional sets. Isobaric strong multiplicity one, proved in the preceding lesson, identifies them, including their constituents, twists and multiplicities. For composition, outside the union of the two exceptional sets,

\[
c_v(\Omega)=\psi_v(c_v(\Pi))
=\psi_v\phi_v(c_v(\pi)).
\]

This is (1.4) for the composite. No statement about the omitted places follows from this argument. ∎

## 2. The L-function identity

Let \(r:{}^LG\to GL(V)\) be a finite-dimensional representation, algebraic on the dual group and admissible for defining Langlands L-factors. For a sufficiently large \(S\), the unramified factors are

\[
L_v(s,\Pi,r)=\det(1-q_v^{-s}r(c_v(\Pi)))^{-1}.
\tag{2.1}
\]

**Proposition 2.1 (functorial identity of partial L-functions).** If \(\Pi\) is a weak transfer of \(\pi\) for \(\phi\), then

\[
L^S(s,\Pi,r)=L^S(s,\pi,r\circ\phi).
\tag{2.2}
\]

This is an identity of local Euler factors and formal Euler products. It is an identity of analytic functions wherever the products converge absolutely. If both sides have meromorphic continuations, they agree by continuation.

**Proof.** At each \(v\notin S\), choose representatives so that \(c_v(\Pi)\) is conjugate to \(\phi_v(c_v(\pi))\). Applying \(r\) preserves conjugacy, and therefore

\[
\begin{aligned}
\det(1-q_v^{-s}r(c_v(\Pi)))
&=\det(1-q_v^{-s}r(\phi_v(c_v(\pi))))\\
&=\det(1-q_v^{-s}(r\circ\phi_v)(c_v(\pi))).
\end{aligned}
\tag{2.3}
\]

Taking reciprocals gives equality of the local factors. Their expansions at \(q_v^{-s}=0\) consequently have identical coefficients, so multiplying gives the formal identity. In any common half-plane of absolute convergence, products of the same factors give the same analytic function. The identity theorem then gives the asserted equality of meromorphic continuations. ∎

For the split general-linear instances below, existence of an initial common half-plane can also be checked directly. The preceding lessons give a bound \(|\alpha_{i,v}|\le q_v^C\) with \(C\) independent of \(v\), for the finitely many fixed cuspidal constituents and norm twists involved. A fixed tensor or symmetric-power construction replaces this by a bound of the same form, with a larger constant. The logarithmic Euler-product estimate from *Automorphic representations and automorphic L-functions*, Proposition 2.1, gives absolute convergence far enough to the right. No claim about the optimal half-plane is needed for (2.2).

Weak transfer proves neither equality of the factors at \(v\in S\) nor equality of conductors, epsilon factors or archimedean gamma factors. Strong transfer and a local correspondence compatible with the relevant factors give those further identities. Even in the strong case, an analytic property of the full product need not follow from an unproved analytic property of a different L-function; the standard \(GL_N\) analytic theorem is the usable input.

## 3. Basic instances

### Direct sums, symmetric powers and tensor products

The block diagonal embedding

\[
\prod_i GL_{n_i}(\mathbb C)\longrightarrow GL_{\sum_i n_i}(\mathbb C)
\tag{3.1}
\]

corresponds to isobaric addition \(\boxplus_i\pi_i\). Its Satake eigenvalues are the union, with multiplicity, of the eigenvalues of the \(\pi_i\), and its standard L-factor is their product. This case comes from Eisenstein series and normalized parabolic induction [Getz–Hahn, 22 April 2022 draft, §13.2, p.306]. The automorphic existence and identification of the chosen isobaric subquotient are stated inputs in §6 of the preceding lesson; their general proof is still required. The union of Satake eigenvalues and the determinant calculation do not construct that global representation.

For symmetric powers, extend the algebraic representation

\[
\operatorname{Sym}^r:GL_2(\mathbb C)\longrightarrow GL_{r+1}(\mathbb C)
\tag{3.2}
\]

by the identity on \(\Gamma_F\). If \(c_v(\pi)=\operatorname{diag}(\alpha_v,\beta_v)\), its action on the basis \(e_1^{r-j}e_2^j\), \(0\le j\le r\), gives

\[
\operatorname{Sym}^r c_v(\pi)
=\operatorname{diag}(\alpha_v^r,\alpha_v^{r-1}\beta_v,
\ldots,\beta_v^r).
\tag{3.3}
\]

Thus a symmetric-power transfer has local factor

\[
L_v(s,\operatorname{Sym}^r\pi)
=\prod_{j=0}^r
(1-\alpha_v^{r-j}\beta_v^j q_v^{-s})^{-1}.
\tag{3.4}
\]

The determinant is \((\alpha_v\beta_v)^{r(r+1)/2}\): each exponent has sum \(0+1+\cdots+r\). At a place of strong compatibility, its central character is therefore \(\omega_{\pi_v}^{r(r+1)/2}\).

The tensor-product map is

\[
GL_n(\mathbb C)\times GL_m(\mathbb C)\longrightarrow GL_{nm}(\mathbb C),
\qquad(A,B)\longmapsto A\otimes B.
\tag{3.5}
\]

For diagonalizable \(A,B\), tensoring eigenvectors gives eigenvalues \(\alpha_i\beta_j\), one for every ordered pair. Consequently

\[
\begin{aligned}
L_v(s,\pi\boxtimes\pi')&=
\prod_{i=1}^n\prod_{j=1}^m(1-\alpha_{i,v}\beta_{j,v}q_v^{-s})^{-1},\\
\det(A\otimes B)&=(\det A)^m(\det B)^n.
\end{aligned}
\tag{3.6}
\]

The local expression is the unramified Rankin–Selberg factor. Rankin–Selberg theory constructs and studies that L-function without, by itself, constructing a global automorphic tensor-product representation. Functorial tensor-product automorphy is a further assertion. The next lesson discusses proved cases.

### Reciprocity and Artin L-functions

For the trivial group, \({}^L\{1\}=\Gamma_F\). A finite-image complex representation \(\rho:\Gamma_F\to GL_N(\mathbb C)\) gives

\[
\phi_\rho:\Gamma_F\longrightarrow GL_N(\mathbb C)\times\Gamma_F,
\qquad\gamma\longmapsto(\rho(\gamma),\gamma).
\tag{3.7}
\]

The source has one automorphic representation, the trivial one. At an unramified place its transfer should have Satake class \(\rho(\operatorname{Frob}_v)\). Proposition 2.1 gives

\[
L^S(s,\Pi)=L^S(s,\rho).
\tag{3.8}
\]

The Galois factor in (3.7) is essential: the L-group of the trivial group is not trivial. Finite-image \(\rho\) is unitary after choosing an invariant Hermitian form. Indeed, average any positive definite form over its finite image; the average is positive definite and invariant.

The **strong Artin conjecture** asks that an irreducible \(\rho\) correspond to a cuspidal \(\Pi\) on \(GL_N\), with matching local factors at every place. For \(N\ge2\), the Godement–Jacquet theorem then makes the complete Artin L-function entire. The finite Artin product is also entire: it is the complete product multiplied by the reciprocal archimedean factors, which are entire. In dimension one, class field theory gives the Hecke character, and the nontrivial finite-order characters have entire completed L-functions by Tate's theorem. The trivial character is the exception: its completed Dedekind zeta function has poles at zero and one. Almost-all-place agreement (3.8), without control of the removed factors, is not the entire strong Artin assertion. See [Arthur, June 2020 author draft, pp.14–15; Taylor 2004, §5.3.2, pp.108–110].

More general Weil-group representations extend this picture. Geometric \(\ell\)-adic representations and motives require additional hypotheses, coefficient comparisons and normalization choices. They are the subject of *Global reciprocity for GL_n: conjectures and known cases*.

### Base change

For a finite Galois extension \(E/F\) of degree \(d\),

\[
{}^L\operatorname{Res}_{E/F}GL_n
=GL_n(\mathbb C)^d\rtimes\Gamma_F,
\tag{3.9}
\]

where \(\Gamma_F\) permutes the factors through \(\operatorname{Gal}(E/F)\). The diagonal embedding \(A\mapsto(A,\ldots,A)\), together with the identity on \(\Gamma_F\), is an L-homomorphism from \({}^LGL_n\) to (3.9). It corresponds locally to restriction of a parameter to the Weil groups of \(E_w\), and globally to base change from \(GL_n(\mathbb A_F)\) to \(GL_n(\mathbb A_E)\). The same construction works for a group defined over \(F\) and its base extension to \(E\), with the relevant dual action included.

If \(v\) and \(w\mid v\) are unramified and the residue degree is \(f\), then \(q_w=q_v^f\) and the compatible Frobenius at \(w\) maps to the \(f\)-th power of the one at \(v\). Hence the base-changed eigenvalues are \(\alpha_{i,v}^f\) and

\[
L_w(s,\pi_E)=\prod_i(1-\alpha_{i,v}^f q_w^{-s})^{-1}.
\tag{3.10}
\]

For a quadratic extension with associated character \(\varepsilon_{E/F}\), this gives, at every unramified place of both the extension and \(\pi\),

\[
\prod_{w\mid v}L_w(s,\pi_E)
=L_v(s,\pi)L_v(s,\pi\otimes\varepsilon_{E/F}).
\tag{3.11}
\]

At a split place there are two identical factors and \(\varepsilon_v(\varpi_v)=1\). At an inert place there is one factor with \(f=2\), and \(\varepsilon_v(\varpi_v)=-1\). For each eigenvalue, the required identity is \((1-\alpha X)(1+\alpha X)=1-\alpha^2X^2\), with \(X=q_v^{-s}\). This proves (3.11) in both cases. The existence of base change is a global theorem for cyclic extensions, rather than a consequence of the polynomial calculation [Getz–Hahn, 22 April 2022 draft, §13.5, pp.310–312; Taylor 2004, §5.2, pp.106–107].

### Automorphic induction

There is an L-homomorphism in the opposite direction,

\[
{}^L\operatorname{Res}_{E/F}GL_n\longrightarrow{}^LGL_{nd}.
\tag{3.12}
\]

Its \(nd\)-dimensional representation acts on a direct sum of \(d\) copies of \(\mathbb C^n\): the \(d\) dual factors act block diagonally and the Galois group permutes the blocks. For a concrete convention, index them by \(\tau\in\operatorname{Gal}(E/F)\), let \(D(A)\) act by \(A_\tau\) on the \(\tau\)-block, and let \(P_\gamma\) send that block to the \(\gamma\tau\)-block. Then

\[
P_\gamma D(B)P_\gamma^{-1}=D(\gamma\cdot B),
\quad (\gamma\cdot B)_\tau=B_{\gamma^{-1}\tau}.
\tag{3.13}
\]

Thus \((A,\gamma)\mapsto(D(A)P_\gamma,\gamma)\) is a homomorphism of the semidirect products. Locally it is induction of Weil–Deligne parameters. Globally the predicted transfer is

\[
\operatorname{AI}_{E/F}:GL_n(\mathbb A_E)
\longrightarrow GL_{nd}(\mathbb A_F).
\tag{3.14}
\]

The dual representation uses all the dual factors in (3.9). Only after restriction to the diagonal subgroup does its description reduce to the standard \(GL_n\) representation tensored with the permutation representation of the Galois group. Confusing that restriction with the full L-map loses the independent blocks.

### Classical groups and endoscopy

For split classical groups, the standard dual embeddings give the following instances.

| Source group \(H\) | Dual group \(\widehat H\) | Target for the standard transfer |
|---|---|---|
| \(Sp_{2n}\) | \(SO_{2n+1}(\mathbb C)\) | \(GL_{2n+1}\) |
| \(SO_{2n+1}\) | \(Sp_{2n}(\mathbb C)\) | \(GL_{2n}\) |
| Split \(SO_{2n}\) | \(SO_{2n}(\mathbb C)\) | \(GL_{2n}\) |

The homomorphism is the defining matrix representation of the listed dual group, extended over \(\Gamma_F\). The symplectic and orthogonal groups exchange roles under duality. For nonsplit groups the Galois action must also be matched. In particular, a unitary group's dual \(GL_n(\mathbb C)\) has a nontrivial Galois action; its familiar degree-\(n\) transfer is base change to the quadratic extension, not the same formula as a split \(GL_n/F\) embedding. These constructions and their generic cases are discussed in [Getz–Hahn, 22 April 2022 draft, §13.7, pp.315–316]. We do not assert temperedness of every cuspidal representation of a classical group: nontempered cuspidal packets are part of the theory.

An endoscopic datum supplies an endoscopic group and a suitable L-embedding into the original L-group, together with the data needed for transfer identities. It generally does not arise from an embedding of the original algebraic groups over \(F\). The local packet structure and the global multiplicity formula are essential. The final lesson explains this instance and the role of Arthur parameters.

## 4. Quadratic induction and a dihedral symmetric square

Let \(E/F\) be quadratic, write \(\tau\) for its nonidentity automorphism, and let \(\theta\) be a unitary Hecke character of \(E\). We use the following existence theorem.

**Theorem 4.1 (quadratic automorphic induction).** The induction \(\pi=\operatorname{AI}_{E/F}(\theta)\) is an isobaric automorphic representation of \(GL_2(\mathbb A_F)\), with the induced local Weil parameters at every place. It is cuspidal if and only if \(\theta\ne\theta^\tau\). If \(\theta=\mu\circ N_{E/F}\), then \(\pi=\mu\boxplus\mu\varepsilon_{E/F}\).

These are the degree-one quadratic cases of [Getz–Hahn, 22 April 2022 draft, Theorem 13.5.2, pp.311–312], with the inducing representation correctly taken over \(E\); compatibility with local parameters is discussed immediately after that theorem.

The noninvariant case is proved in Dihedral forms, examples, and the Ramanujan conjecture for GL₂, Theorem 2.1 and §2.1, over every number field. That proof uses the earlier local quadratic models, identifies all complete Hecke twists, proves their entire continuation and strip estimates, and applies the proved all-field converse, Theorem 4.5 of the earlier converse lesson. Proposition 1.2 of the dihedral lesson proves that invariance is equivalent to being a norm pullback: extend the invariant character to the two open cosets of the relative Weil group, then use its topological abelianization to obtain the base Hecke character. The induced parameter is then the sum of the two extensions. Proposition 4.1a below constructs the invariant case's global automorphic sum directly by an Eisenstein series over every number field. If the inducing character is unitary, its two extensions are unitary: choose the square root on the unit circle in the two-coset extension argument.

### The invariant character: an Eisenstein construction over every number field

The invariant case of Theorem 4.1 can be constructed without assuming general isobaric existence. We give the argument because splitting a parameter by itself does not produce an automorphic representation.

**Proposition 4.1a.** Let \(F\) be any number field, let \(\varepsilon\) be a nontrivial quadratic Hecke character of \(F\), and let \(\mu\) be a unitary Hecke character. The restricted tensor product of the normalized local inductions

\[
I_v=\operatorname{Ind}_{B(F_v)}^{GL_2(F_v)}
(\mu_v\otimes\mu_v\varepsilon_v)
\tag{4.1a}
\]

has an injective realization in automorphic forms by Eisenstein series at the unitary parameter. It is irreducible and noncuspidal. This realizes the particular isobaric sum \(\mu\boxplus\mu\varepsilon\) over \(F\).

**Proof.** Write \(C_F=F^\times\backslash\mathbb A_F^\times\), \(d=[F:\mathbb Q]\), and \(u=s+1/2\). A flat section has a fixed compact-model restriction and satisfies

\[
f_s\left(\begin{pmatrix}a&b\\0&c\end{pmatrix}g\right)
=\mu(a)\mu\varepsilon(c)|a/c|^{s+1/2}f_s(g).
\tag{4.1b}
\]

Here the compact group is \(O(2)\) at a real place, \(U(2)\) at a complex place, and \(GL_2(\mathcal O_v)\) at a finite place. The local Iwasawa decompositions used for this model are proved in the preceding Satake lesson for \(GL_2\), and at infinity follow from orthogonalizing the two rows.

For \(\Phi\in\mathcal S(\mathbb A_F^2)\), initially in \(\Re u>1\), put

\[
f_{\Phi,s}(g)=\mu(\det g)|\det g|^u
\int_{\mathbb A_F^\times}
\Phi((0,t)g)\varepsilon(t)|t|^{2u}\,d^\times t.
\tag{4.1c}
\]

The multiplicative measures have finite unit groups of volume one. Changing \(t\) to \(ct\) verifies (4.1b): the character multiplier is
\(\mu(ac)\varepsilon(c)^{-1}=\mu(a)\mu\varepsilon(c)\), and the norm multiplier is \(|ac|^u|c|^{-2u}=|a/c|^u\). Convergence of this rank-one integral in the initial region is Proposition 9.1 of Tate's global theory: continuation and functional equation.

The cosets \(B(F)\backslash GL_2(F)\) are the rational bottom-row lines. Splitting each nonzero row into its line and a scalar in \(F^\times\) therefore unfolds the Eisenstein sum to

\[
\begin{aligned}
E(g,f_{\Phi,s})&=\mu(\det g)|\det g|^u J_g(u),\\
J_g(u)&=\int_{C_F}
\left(\sum_{v\in F^2}\Phi(tv g)-\Phi(0)\right)
\varepsilon(t)|t|^{2u}\,d^\times t.
\end{aligned}
\tag{4.1d}
\]

We justify the convergence and continuation uniformly in the number field. The norm-one class group \(C_F^1\) is compact by Theorem 3.3 of Idèles and the idèle class group. Its proof and the compact-lift argument in the theta lemma of NT-ADL-09 give a compact set of idèle representatives. Choose the norm splitting \(t_\lambda\) with component \(\lambda^{1/d}\) at every infinite place and component one at every finite place. It has idèle norm \(\lambda\). Haar measure on the quotient is a positive constant times \(d\lambda/\lambda\) times Haar measure on \(C_F^1\); the harmless constant need not be normalized to one.

For fixed \(g\), and uniformly for \(g\) in a compact set and representatives \(y\) in that compact lift, the finite support of \(\Phi\) confines contributing rows to a fixed fractional-ideal lattice in \(F^2\). In its Minkowski embedding this is a lattice of real rank \(2d\). The archimedean factors of \(y\) and their inverses are bounded. If \(R=\lambda^{1/d}\ge1\), Schwartz estimates give

\[
\left|\sum_{v\ne0}\Phi(t_\lambda yv g)\right|
\le C_N\sum_{v\in\Lambda\setminus\{0\}}(1+cR\|v\|)^{-N}
=O(\lambda^{-N/d})\qquad(N>2d).
\tag{4.1e}
\]

To verify the summability here, disjoint balls smaller than the lattice's minimum separation bound the number of points of norm at most \(T\) by \(C(1+T)^{2d}\). Dyadic shells then show \(\sum_{v\ne0}\|v\|^{-N}<\infty\) for \(N>2d\). Choosing \(N\) arbitrarily large proves the rapid decay claimed in (4.1e). The same estimate holds after any fixed archimedean derivative, since differentiating a Schwartz function produces another Schwartz function multiplied by a polynomial.

Use the self-dual additive measure from NT-ADL-09. The Poisson formula of Additive characters, self-dual measures and Poisson summation on the adèles, Theorems 5.4–5.5, applies on \(\mathbb A_F^2\) by applying it in each coordinate. Partial Fourier transforms preserve the Schwartz space. The lattice-counting estimate above, applied to each partial transform, gives absolute convergence of the successive sums, so they may be exchanged; this proves the product formula also for Schwartz functions that do not separate into coordinate tensors. Change of variables gives

\[
\sum_{v\in F^2}\Phi(tv g)
=|t|^{-2}|\det g|^{-1}
\sum_{v\in F^2}\widehat\Phi(t^{-1}v g^{-t}).
\tag{4.1f}
\]

Split (4.1d) at \(\lambda=1\), use (4.1f) in the small-norm integral, and invert the idèle there. The resulting nonzero dual theta sum is integrated over norm at least one, with weight \(|t|^{2-2u}\) and character \(\varepsilon^{-1}=\varepsilon\). Both nonzero-sum tails are entire in \(u\), locally uniformly with all group derivatives, by (4.1e). The two zero terms before inversion are

\[
|t|^{-2}|\det g|^{-1}\widehat\Phi(0)-\Phi(0).
\tag{4.1g}
\]

Their averages over \(C_F^1\) are zero. Indeed, \(\varepsilon\) is nontrivial on \(C_F^1\): otherwise it would factor through the connected norm group \(\mathbb R_{>0}\), whose continuous finite-image characters are trivial. The integral of a nontrivial character on a compact group is zero, since translation by an element on which its value differs from one multiplies that integral by this value. Also \(\varepsilon(t_\lambda)=1\) by connectedness. Thus (4.1d) continues to an entire function for every \(\Phi\).

Every flat finite-level, archimedean compact-group-finite section is a finite sum of pure local sections. We recover each such section near \(s=0\). At an exceptional finite place its compact-model function, after removing \(\mu_v(\det k)\), is a locally constant function of the primitive bottom row. Independence of the chosen top row follows from upper-triangular compact covariance in (4.1b). Scaling that row by a unit multiplies this function by \(\varepsilon_v^{-1}\). Extend it to \(F_v^2\) using the unit radial shell and zero outside that shell. The integral in (4.1c) at \(k\in K_v\) then reproduces the prescribed compact-model function times a nonzero constant.

At a real or complex place do the same on the unit sphere, and multiply the smooth angular function by a smooth radial bump supported in a sufficiently narrow annulus about radius one. Integration over the scalar unit group cancels the angular covariance. The radial Mellin integral \(a_v(s)\) is entire and nonzero at zero when the bump is chosen narrow enough; its phase then varies by less than any fixed small angle. Angular compact finiteness is preserved by this construction. At each remaining finite place choose \(\Phi_v=\mathbf1_{\mathcal O_v^2}\). The compact restriction of its scalar integral is the geometric series
\(L_v(1+2s,\varepsilon_v)\). Consequently (4.1c) has compact restriction \(a(s)f_s|_K\), where

\[
a(s)=L^S(1+2s,\varepsilon)\prod_{v\in S}a_v(s).
\tag{4.1h}
\]

Here \(S\) includes the infinite places and all exceptional finite places, and \(L^S\) is the finite Euler product with those finite factors omitted. Theorem 10.6 of Hecke L-functions and the Dedekind zeta function proves that \(L(1,\varepsilon)\) is finite and nonzero over every number field. Its quadratic-case proof uses the nonnegative coefficients of \(\zeta_F(s)L(s,\varepsilon)\), including the squared-ideal coefficients, and its proved positive-pole and Landau lemmas. Each omitted Euler factor is finite and nonzero at one. Hence \(a\) is holomorphic and nonzero near zero.

In the initial convergence region the equality of compact restrictions and Iwasawa covariance give \(f_{\Phi,s}=a(s)f_s\). The absolutely convergent theta unfolding proves convergence of the Eisenstein sum there. Dividing its entire continuation by \(a(s)\) gives a holomorphic Eisenstein family for every flat section near zero. This continuation is automorphic: rational left invariance, the central character and right equivariance hold initially and extend by the identity theorem.

For clarity, these functions have moderate growth, not just pointwise continuation. Fix the finite component of \(g\), put \(H=1+\|g_\infty\|+\|g_\infty^{-1}\|\), and use the same lattice as above. The least singular value is at least \(H^{-1}\). For \(\lambda\ge1\) the nonzero theta sum is bounded by
\(C_N\sum_{v\ne0}(1+c\lambda^{1/d}\|v\|/H)^{-N}\). On \(1\le\lambda\le H^d\), lattice counting bounds this by \(CH^{2d}\); on \(\lambda\ge H^d\), it is at most \(C_NH^N\lambda^{-N/d}\). Integrating either bound against a fixed power of \(\lambda\) yields a polynomial in \(H\), by taking \(N\) larger than that power times \(d\). The dual tail obeys the same bounds with \(g^{-t}\); its determinant factor and the prefactor in (4.1d) are bounded by further powers of \(H\). This also proves moderate growth after every fixed derivative. Uniform adelic height bounds follow by clearing the finite denominators: the possible rows lie in \(M^{-1}\mathcal O_F^2\), where the positive rational integer \(M\) can be bounded by a fixed power of the product of the finite matrix norms of \(g\) and \(g^{-1}\). Such an \(M\) is obtained by multiplying the underlying rational prime powers needed to clear the finitely many denominator ideals. Rescaling the fixed Minkowski lattice by \(M\) inserts only further polynomial factors into the same estimates. Finite level and compact finiteness are preserved by right equivariance. The infinitesimal centers act through those of the fixed local principal series, so the functions are also infinitesimal-character finite.

It remains to show that the map at zero does not collapse. Normalize the compact additive quotient \(F\backslash\mathbb A_F\) to volume one. Bruhat decomposition unfolds the constant term in the initial region to

\[
E_N(g,f_s)=f_s(g)+M_s f_s(g),\qquad
M_s f_s(g)=\int_{\mathbb A_F}f_s(w n(x)g)\,dx.
\tag{4.1i}
\]

The first Bruhat cell gives \(f_s\); the second is indexed by \(x\in F\), and unfolding its sum over the additive quotient gives the displayed adelic integral. Changing its integration variable proves that the second term has covariance
\(\mu\varepsilon(a)\mu(c)|a/c|^{1/2-s}\). Near zero it is holomorphic because it equals \(E_N-f_s\), and integration of the continued family over the compact additive quotient preserves holomorphy. Its covariance therefore continues too.

Choose \(y\in C_F^1\) with \(\varepsilon(y)=-1\). At \(s=0\), left multiplication by \(\operatorname{diag}(y,1)\) multiplies the two terms of (4.1i) by the opposite scalars \(\mu(y)\) and \(-\mu(y)\). If \(E(g,f_0)\) vanished identically, its constant term and its value at this translate would both vanish. Adding and subtracting those two equations would give \(f_0=0\). Thus the Eisenstein map is injective, and every nonzero image has a nonzero constant term.

Finally each local module (4.1a) is simple. At a finite place the ratio is quadratic or trivial, and cannot be \(|\cdot|_v^{\pm1}\); the irreducibility proof is Theorem 4.2 of Whittaker models, Kirillov models and the local classification. At a real place the exponent difference is zero. Theorem 3.2 of Real and complex representations: weights, gamma factors and classical forms proves full-group irreducibility also for the odd-parity limit: reflection exchanges its two connected half-ladders. At a complex place the quadratic character is trivial; the finite-head-and-infinite-tail lemma of that lesson, §8, excludes reducibility at ratio one. Theorem 5.2 of Restricted tensor products and the tensor product theorem, with its number-field extension in §6, proves irreducibility of the restricted tensor product. Its proof uses finite interpolation to isolate a pure tensor and then generates every finite tensor stage. The injective, right-equivariant Eisenstein map realizes this module automorphically. Its nonzero constant terms establish noncuspidality. ∎

For \(\theta=\mu\circ N_{E/F}\), the two extended characters are \(\mu\) and \(\mu\varepsilon_{E/F}\). Their direct sum is the induced parameter. At nonsplit finite places the norm-factor proof of Theorem 6.4 and the complete factor identity of Theorem 6.5 in Supercuspidal representations from compact induction identify the model with precisely this principal series. At split places the two inducing characters give the direct-sum model. The real and complex classification just used identifies the archimedean models, including the real odd-parity limit. These are the explicit rank-two models for the split induced parameter, rather than an appeal to an unproved general local correspondence. Proposition 4.1a therefore supplies the invariant branch of Theorem 4.1 over every number field. The rank-three isobaric construction in Proposition 4.2 below still requires its separate existence hypothesis.

Here are the local calculations. At a split finite place, the two characters \(\theta_{w_1},\theta_{w_2}\) give eigenvalues

\[
u_1=\theta_{w_1}(\varpi_{w_1}),\qquad
u_2=\theta_{w_2}(\varpi_{w_2}),
\quad
L_v(s,\pi)=(1-u_1q_v^{-s})^{-1}(1-u_2q_v^{-s})^{-1}.
\tag{4.1}
\]

At an inert unramified place there is one \(w\), with \(q_w=q_v^2\). Write \(u=\theta_w(\operatorname{Frob}_w)\), with the reciprocity convention of §1. The induced Frobenius has a basis in which its matrix is

\[
\begin{pmatrix}0&u\\1&0\end{pmatrix}.
\tag{4.2}
\]

It has characteristic polynomial \(T^2-u\), eigenvalues \(\sqrt u,-\sqrt u\), and determinant \(-u\). Consequently

\[
L_v(s,\pi)=(1-uq_v^{-2s})^{-1}=L_w(s,\theta).
\tag{4.3}
\]

Either square root gives the same unordered eigenvalues. Since \(\theta\) is unitary, \(|u|=1\), and both eigenvalues have absolute value one. The same assertion follows from (4.1) at a split place. This computes the good-place Ramanujan property for this induction directly.

Now suppose \(\theta\ne\theta^\tau\), so that \(\pi\) is a dihedral cusp form. We compute its symmetric square before making an automorphic assertion. Write \(\rho=\operatorname{Ind}_{W_E}^{W_F}\theta\). Let \(t\in W_F\setminus W_E\). On restriction to \(W_E\), \(\rho\) is \(\theta\oplus\theta^\tau\). Choose a basis such that

\[
\rho(t)e_1=e_2,\qquad \rho(t)e_2=a e_1,
\quad a=\theta(t^2).
\tag{4.4}
\]

This is the usual index-two induced representation. The two eigenspaces for \(W_E\) are distinct and \(t\) interchanges them, so no one-dimensional subspace is \(W_F\)-stable; hence \(\rho\) is irreducible.

In \(\operatorname{Sym}^2\rho\), the span of \(e_1^2,e_2^2\) restricts to \(\theta^2\oplus(\theta^\tau)^2\). The element \(t\) sends \(e_1^2\) to \(e_2^2\) and \(e_2^2\) to \(a^2e_1^2\); this two-dimensional summand is \(\operatorname{Ind}\theta^2\). The remaining line is spanned by \(e_1e_2\). On \(W_E\) its character is \(\theta\theta^\tau=\det\rho\). On \(t\), its eigenvalue is \(a\), whereas \(\det\rho(t)=-a\). The quadratic character \(\varepsilon_{E/F}\) is trivial on \(W_E\) and has value \(-1\) on \(t\). Therefore

\[
\operatorname{Sym}^2\rho
\simeq\operatorname{Ind}_{W_E}^{W_F}\theta^2
\oplus(\det\rho)\varepsilon_{E/F}.
\tag{4.5}
\]

**Proposition 4.2 (dihedral symmetric square, under isobaric existence).** A weak symmetric-square transfer of \(\pi\) is

\[
\operatorname{Sym}^2\pi
=\operatorname{AI}_{E/F}(\theta^2)
\boxplus\omega_\pi\varepsilon_{E/F}.
\tag{4.6}
\]

It is not cuspidal. In particular, the existence of a symmetric-square transfer does not imply its cuspidality.

**Proof.** Theorem 4.1 constructs the degree-two summand, and class field theory supplies the character \(\omega_\pi\varepsilon_{E/F}\). Isobaric addition constructs their automorphic sum. At every good place (4.5) identifies its Satake parameter with the symmetric square of the parameter of \(\pi\). It is therefore a weak transfer. Its isobaric decomposition contains a rank-one constituent. Isobaric uniqueness from Proposition 1.4 precludes its being a rank-three cuspidal representation: the latter would have a single rank-three cuspidal constituent. ∎

There are two possibilities for the rank-two term. If \(\theta^2\ne(\theta^\tau)^2\), it is cuspidal. If \(\theta^2=(\theta^\tau)^2\), the character extends from \(W_E\) to \(W_F\). To see this, choose \(b\) with \(b^2=\theta^2(t^2)\), let an extension take value \(b\) on \(t\), and take value \(\theta^2\) on \(W_E\). Invariance ensures compatibility with conjugation by \(t\), and the square condition ensures compatibility with \(t^2\). These relations define a continuous character because \(W_E\) is open of index two. There are exactly two extensions, differing by \(\varepsilon_{E/F}\). Under class field theory they give \(\mu\) and \(\mu\varepsilon_{E/F}\), with \(\theta^2=\mu\circ N_{E/F}\). Thus (4.6) has three rank-one constituents in this case. Both cases establish noncuspidality.

### A CM holomorphic form

For a concrete archimedean type, take \(F=\mathbb Q\), an imaginary quadratic \(E\), and a Hecke character whose algebraic infinity type gives a holomorphic theta series of weight \(k\ge2\). Write \(\theta\) for its unitary normalization, so that

\[
\theta_\infty(z)=(z/|z|)^{-(k-1)}.
\tag{4.7}
\]

The negative exponent in (4.7) is the idelic unitary normalization of an ideal character of type \(z^{k-1}\); triviality on diagonal elements forces this inverse infinity character. The holomorphic theta-series realization is proved in Dihedral forms, examples, and the Ramanujan conjecture for GL₂, Theorem 3.1. Conjugation replaces this infinity character by its inverse. Their squares are distinct because \(k-1>0\); hence \(\operatorname{AI}(\theta^2)\) in (4.6) is a cusp form, while the rank-three symmetric square is not.

Let \(p\) be a good prime and put \(w_p=\omega_\pi(p)\). At a split prime, write the normalized roots as \(\alpha,\beta\). Then \(\alpha\beta=w_p\), and the rank-two and rank-one constituents of (4.6) have roots \(\alpha^2,\beta^2\) and \(w_p\), respectively. Their local denominators multiply to

\[
(1-\alpha^2X)(1-w_pX)(1-\beta^2X),\qquad X=p^{-s}.
\tag{4.8}
\]

At an inert prime, (4.2) gives \(\beta=-\alpha\), \(\alpha^2=u\), and \(w_p=-u\). The symmetric-square roots are \(u,-u,u\). The induction of \(\theta^2\) has roots \(u,-u\), and the character \(\omega_\pi\varepsilon\) has value \((-u)(-1)=u\). This again gives exactly the three roots. If \(w_p=1\), then \(u=-1\), the three roots are \(-1,1,-1\), and the denominator is \((1+X)^2(1-X)\).

These calculations use unitary roots. The classical roots of the weight-\(k\) form are \(p^{(k-1)/2}\alpha,p^{(k-1)/2}\beta\); their symmetric squares are obtained by multiplying each of the three roots above by \(p^{k-1}\). Mixing these two normalizations would give an incorrect Ramanujan statement.

## 5. Langlands' argument for Ramanujan

Fix a unitary cuspidal representation \(\pi\) of \(GL_2(\mathbb A_F)\) and a finite unramified place \(v\), with normalized roots \(\alpha,\beta\). Unitarity of the central character gives

\[
|\alpha\beta|=1.
\tag{5.1}
\]

We say that an isobaric sum has **unitary cuspidal constituents** if it is \(\sigma_1\boxplus\cdots\boxplus\sigma_a\) with each \(\sigma_i\) unitary cuspidal, without any nonunitary real norm twists. This property is stronger than saying that an automorphic representation is unitary.

**Theorem 5.1 (Langlands' symmetric-power deduction).** Use Corollary 4.5 of the preceding lesson, with its stated local and global analytic hypotheses. Suppose there is an unbounded set of positive integers \(r\) for which an isobaric automorphic representation \(\Pi_r\) on \(GL_{r+1}(\mathbb A_F)\) has unitary cuspidal constituents and is compatible at the fixed place \(v\) with \(\operatorname{Sym}^r\pi_v\). Then

\[
|\alpha|=|\beta|=1.
\tag{5.2}
\]

In particular, symmetric-power transfers for every \(r\), with these constituent and local-compatibility properties at every unramified place of \(\pi\), imply unramified Ramanujan. The deduction is Langlands' argument [Langlands 1997, §3, p.7; Sarnak 2005, §1, pp.663–664]; we give its complete proof with the analytic hypotheses exposed.

**Proof.** Since \(\Pi_{r,v}\) is unramified, its constituent parameters are unramified. Indeed, its parameter is their direct sum: trivial inertia and trivial monodromy on a direct sum imply the same properties on every summand. The Satake eigenvalues of each \(\sigma_{i,v}\) obey the Jacquet–Shalika bound \(|\gamma|<q_v^{1/2}\), by Corollary 4.5 of the preceding lesson. Taking their union gives that bound for every root of \(\Pi_{r,v}\). Formula (3.3) includes \(\alpha^r\) and \(\beta^r\), so

\[
|\alpha|^r<q_v^{1/2},\qquad
|\beta|^r<q_v^{1/2}.
\tag{5.3}
\]

For arbitrarily large \(r\), taking \(r\)-th roots gives \(|\alpha|,|\beta|\le1\), because \(q_v^{1/(2r)}\to1\). Equation (5.1) forces both to be one. Normalized unramified Satake theory then identifies \(\pi_v\) as tempered. ∎

The argument only needs a bound \(|\gamma|\le q_v^C\) with \(C\) independent of \(r\). The strict bound from the preceding lesson supplies \(C=1/2\). At a fixed finite stage (5.3) yields a bound tending to temperedness as \(r\) grows; it does not already give equality.

Two logical limitations are essential. First, a separate weak transfer for every \(r\) may have exceptional set \(S_r\) depending on \(r\). A fixed \(v\) could belong to every \(S_r\); even the union of finite sets \(S_r\) need not be finite. Thus those weak transfers alone do not establish the hypothesis at every unramified \(v\). Strong local compatibility, a uniform exceptional set, or an unbounded compatible family at each place resolves this issue.

Second, arbitrary automorphy does not supply the needed cuspidal bound. The trivial automorphic representation of \(GL_2\) is unitary and has roots \(q_v^{1/2},q_v^{-1/2}\). Their \(r\)-th symmetric power has roots

\[
q_v^{r/2},q_v^{(r-2)/2},\ldots,q_v^{-r/2},
\tag{5.4}
\]

which are the Satake roots of the trivial automorphic representation of \(GL_{r+1}\), equivalently the residual representation \(\operatorname{Speh}(1,r+1)\). All these representations are unitary automorphic. Their isobaric constituents are real norm twists of characters, rather than unitary characters, and the roots in (5.4) violate the desired bound when \(r\) is large. The source in this example is not cuspidal, so it is not a counterexample to Ramanujan for cusp forms. It demonstrates precisely why the inference “automorphic, therefore Jacquet–Shalika applies” is invalid. Theorem 5.1 states the correct sufficient hypotheses.

## 6. The real place and Selberg's eigenvalue conjecture

For a congruence subgroup \(\Gamma\subset SL_2(\mathbb Z)\), give the upper half-plane the metric \((dx^2+dy^2)/y^2\), and use the nonnegative Laplacian

\[
\Delta=-y^2(\partial_x^2+\partial_y^2).
\tag{6.1}
\]

**Conjecture 6.1 (Selberg).** A Maass cusp form for a congruence subgroup has no eigenvalue in \((0,1/4)\). Equivalently, all its Laplace eigenvalues are at least \(1/4\). See [Sarnak 2005, §1, p.663, Remark 3] for its representation-theoretic formulation.

**Lemma 6.1a (the Maass realization and its normalization).** If a congruence Maass cusp form has \(0<\lambda<1/4\), there is a unitary cuspidal representation of \(GL_2(\mathbb A_{\mathbb Q})\), with a weight-zero real vector of that eigenvalue, whose real parameter is

\[
\rho_\infty=
\operatorname{sgn}^{\epsilon}|\cdot|^t
\oplus\operatorname{sgn}^{\epsilon}|\cdot|^{-t},
\quad 0<t<1/2,\quad\epsilon\in\{0,1\},
\qquad\lambda=\frac14-t^2.
\tag{6.2}
\]

**Proof.** Choose \(N\) with \(\Gamma(N)\subset\Gamma\). The principal-level decomposition proved in Adèles for GL₂ and strong approximation, §4, equation (4.5) and the following principal-level calculation, identifies the adelic quotient by \(K(N)\), the real center and \(SO(2)\) with finitely many copies of \(\Gamma(N)\backslash\mathfrak H\). Put the given form on one copy and zero on the others. This defines its smooth adelic lift. All its unipotent constant terms vanish: on each component the compact adelic unipotent integral is a sum of integrals over the classical cusp periods; these are zero by cuspidality. This is the unfolding used in From modular forms to adelic functions, §4, without the holomorphic differential condition.

The Fourier argument in Non-holomorphic Eisenstein series and Maass forms, Proposition 4.1 and Corollary 4.2, applies with each cusp's width replacing one: the zero mode is absent, polynomial growth excludes the increasing Bessel solution, and the remaining modes decay exponentially. Thus the lift is square integrable. Its central translates span a finite-dimensional space, because the real center acts trivially and the compact finite center acts through a finite quotient modulo \(K(N)\). Averaging over this finite abelian quotient decomposes it into unitary central characters. At least one component is nonzero; averaging preserves its Laplace eigenvalue, rotation weight zero and cusp integrals.

For that central character, Why the cuspidal spectrum is discrete, Theorem 5.2, gives a Hilbert sum of irreducible unitary cuspidal constituents. Project the nonzero lifted vector onto a nonzero summand. The projection commutes with rotations and the real group, hence with the closed Laplacian and its eigenprojections. The projected vector still has weight zero and eigenvalue \(\lambda\). The finite-vector and Hilbert cuspidal comparison in Automorphic forms, modules and Hilbert constituents, Theorems 3.2 and 4.1, supplies the corresponding cuspidal automorphic representation. Its positive real center is trivial.

The real classification in Real and complex representations: weights, gamma factors and classical forms, Theorem 3.2 and Proposition 4.1, now forces a complementary principal series: discrete-series ladders have no weight zero, and the one-dimensional cases have eigenvalue zero. In that lesson's notation the inducing difference is \(2t\), the central exponent is zero, and unitarity gives \(0<2t<1\). Weight zero makes the two sign exponents equal. Its Casimir formula (1.2) gives \(\lambda=(1-(2t)^2)/4\), and §7 gives the parameter (6.2). The sign character is interpreted through real local reciprocity. ∎

The same normalization is visible in the Fourier term \(y^{1/2}K_t(2\pi|n|y)e^{2\pi inx}\). Put \(a=2\pi|n|\) and \(F(y)=y^{1/2}K_t(ay)\). The Bessel equation

\[
z^2K_t''(z)+zK_t'(z)-(z^2+t^2)K_t(z)=0
\]

gives \(F''-a^2F=(t^2-1/4)y^{-2}F\). Applying (6.1) gives exactly \(\lambda=1/4-t^2\).

Write \(\nu=|\cdot|\) for the character of \(W_{\mathbb R}\) obtained from real reciprocity. For the following deduction use a real local correspondence satisfying

\[
\rho_{\widetilde\sigma}=\rho_\sigma^\vee,
\qquad
\rho_{\overline\sigma}=\overline{\rho_\sigma},
\qquad
\rho_{\boxplus_a\sigma_a}=\bigoplus_a\rho_{\sigma_a},
\qquad
L_\infty(s,\sigma\times\tau)=L(s,\rho_\sigma\otimes\rho_\tau).
\tag{6.3a}
\]

These are explicit local compatibility hypotheses. An almost-all-place transfer assertion supplies none of them. The parameter factor of a one-dimensional real character \(\operatorname{sgn}^{e}\nu^b\), \(e\in\{0,1\}\), is \(\Gamma_{\mathbb R}(s+b+e)\), as proved in Archimedean local zeta integrals and gamma factors, Proposition 8.2. A direct sum gives a product of these factors.

**Lemma 6.1b (a real line in a unitary parameter).** Under the duality and complex-conjugation compatibilities in (6.3a), if the real parameter of a unitary admissible representation \(\sigma\) contains the character \(\operatorname{sgn}^{e}\nu^{-b}\), with \(b\) real, then it also contains \(\operatorname{sgn}^{e}\nu^{b}\). Its self-pairing parameter consequently contains \(\nu^{-2b}\).

**Proof.** Unitarity identifies \(\widetilde\sigma\) with \(\overline\sigma\). To see the identification, make the invariant Hermitian product linear in its first variable; then
\(\overline v\mapsto[w\mapsto\langle w,v\rangle]\)
is a linear equivariant map from the conjugate representation to the contragredient. On compact finite vectors it is onto: each compact type is finite dimensional, its Hermitian product identifies its conjugate with its dual, and a compact finite functional is supported on finitely many types. Thus (6.3a) gives \(\rho_\sigma^\vee\simeq\overline{\rho_\sigma}\).

The character \(\operatorname{sgn}^{e}\nu^{-b}\) has real values, so conjugating its matrices leaves it unchanged. It therefore occurs in \(\overline{\rho_\sigma}\), hence in \(\rho_\sigma^\vee\). Dualizing shows that its inverse \(\operatorname{sgn}^{e}\nu^b\) occurs in \(\rho_\sigma\). Tensor the original line in \(\rho_\sigma\) with the same line in \(\rho_\sigma^\vee\): their product is \(\operatorname{sgn}^{2e}\nu^{-2b}=\nu^{-2b}\). This is a direct summand of the self-pairing parameter. ∎

**Theorem 6.2 (conditional deduction of Selberg).** Use the local compatibilities (6.3a) and the real self-pairing regularity of L-functions for GL_n: Godement–Jacquet and Rankin–Selberg, Corollary 4.5. Suppose that for each unitary cuspidal \(\pi\) arising from a congruence Maass form and for arbitrarily large \(r\):

1. A symmetric-power transfer \(\Pi_r\) has parameter \(\operatorname{Sym}^r\rho_{\pi_\infty}\) at infinity.
2. A tensor-product transfer \(\Xi_r\) of \(\Pi_r\) and \(\widetilde\Pi_r\) has parameter \(\operatorname{Sym}^r\rho_{\pi_\infty}\otimes(\operatorname{Sym}^r\rho_{\pi_\infty})^\vee\) at infinity and is an isobaric sum of unitary cuspidal representations.

Then Selberg's conjecture holds. In particular, strong symmetric-power and tensor-product functoriality with these spectral properties implies it. Corollary 4.5 uses the local factor identification and the complete global Rankin–Selberg pole theorem stated in that lesson; the deduction here retains those analytic hypotheses.

**Proof.** Suppose an exceptional eigenvalue occurs. Lemma 6.1a gives (6.2) with \(t>0\). On the monomial basis the characters in \(\operatorname{Sym}^r\rho_\infty\) are

\[
\operatorname{sgn}^{r\epsilon}\nu^{(r-2j)t},
\qquad 0\le j\le r.
\tag{6.3}
\]

Tensoring with the dual gives characters \(\nu^{2(k-j)t}\), \(0\le j,k\le r\). Every sign is trivial. Hence the tensor transfer has parameter factor

\[
L_\infty(s,\Xi_r)=
\prod_{j,k=0}^r\Gamma_{\mathbb R}(s+2(k-j)t).
\tag{6.4}
\]

In particular, the parameter contains \(\nu^{-2rt}\), from \(j=r,k=0\). Write \(\Xi_r=\boxplus_a\sigma_a\), with each \(\sigma_a\) unitary cuspidal. Its parameter is the direct sum of their parameters, so at least one constituent, say \(\sigma_a\), contains this line. This uses only a multiset assertion about semisimple direct sums; it imposes no rank restriction on \(\sigma_a\).

Lemma 6.1b, with \(e=0\) and \(b=2rt\), gives a second line \(\nu^{2rt}\) in \(\rho_{\sigma_{a,\infty}}\), and the self-pairing parameter contains \(\nu^{-4rt}\). Thus

\[
L_\infty(s,\sigma_a\times\widetilde\sigma_a)
\quad\text{contains the factor}\quad
\Gamma_{\mathbb R}(s-4rt).
\tag{6.5}
\]

At \(s=4rt\) this gamma factor has a pole. Every other real or complex Weil factor is a gamma factor and has no zeros, so the remaining factors cannot cancel the pole. The entire reciprocal and the pole at zero were proved in the preceding lesson, Lemma 2.2; equivalently the recurrence \(\Gamma(z+1)=z\Gamma(z)\) and \(\Gamma(1)=1\) give the pole at zero.

Choose a compatible \(r\) with \(4rt\ge1\). Corollary 4.5 of the preceding lesson says that every local self-pairing factor of a unitary cusp, including this real factor, is holomorphic and nonzero at every real \(s\ge1\). This contradicts (6.5). Therefore no exceptional eigenvalue occurs. Lemma 6.1a applies to every congruence cusp eigenfunction, so the conclusion is not restricted to a previously chosen Hecke eigenbasis. ∎

There is also a useful weaker transfer hypothesis. If \(\Pi_r\) itself has unitary cuspidal constituents and the stated real parameter, choose a constituent containing \(\operatorname{sgn}^{r\epsilon}\nu^{-rt}\). Lemma 6.1b makes its self-pairing contain \(\nu^{-2rt}\), whose factor \(\Gamma_{\mathbb R}(s-2rt)\) has a real pole at \(2rt\ge1\) for sufficiently large \(r\). The same Corollary 4.5 contradicts this. This variant needs no tensor-product transfer; Theorem 6.2 proves the original two-transfer assertion without assuming that \(\Pi_r\) has unitary cuspidal constituents.

For the full \(L^2\) spectrum over \(\mathbb Q\), Eisenstein series on GL₂(A) and the continuous spectrum, Theorem 6.1 and §6.5, proves the spectral decomposition and residual exhaustion at every finite level. The continuous Casimir is multiplication by \(1/4+u^2\), \(u\in\mathbb R\), and its parameter measure has no atoms. The noncuspidal discrete lines are \(\chi\circ\det\); on \(SL_2\) their vectors are constant and have eigenvalue zero. These proved rank-two statements imply that excluding the cuspidal interval \((0,1/4)\) also excludes every positive discrete eigenvalue in that interval. This passage does not require the arbitrary-rank residual classification. Weak agreement at almost all finite primes cannot replace the real compatibility in (6.3a)–(6.4).

## 7. Exercises and complete solutions

**Exercise 7.1.** Compute the symmetric-square map on an unramified Satake class \(\operatorname{diag}(\alpha,\beta)\), its trace and determinant, and the local L-factor.

**Solution.** On \(e_1^2,e_1e_2,e_2^2\), the action is diagonal with eigenvalues \(\alpha^2,\alpha\beta,\beta^2\). Its trace is \(\alpha^2+\alpha\beta+\beta^2=(\alpha+\beta)^2-\alpha\beta\). Its determinant is \(\alpha^3\beta^3=(\alpha\beta)^3\). The local factor is

\[
\bigl((1-\alpha^2q_v^{-s})(1-\alpha\beta q_v^{-s})
(1-\beta^2q_v^{-s})\bigr)^{-1}.
\]

The middle root occurs once: the antisymmetric line belongs to \(\wedge^2\), not to \(\operatorname{Sym}^2\). If numerical roots coincide, the indexed factors still retain their multiplicities. ∎

**Exercise 7.2.** Prove unramified Ramanujan from symmetric-power transfers. State precisely the hypotheses on the transfers and on the fixed place that your argument uses.

**Solution.** Let \(v\) be unramified for a unitary cusp \(\pi\), and suppose an unbounded family of \(r\) has transfers with unitary cuspidal constituents and Satake agreement at this \(v\). The constituent parameters are unramified because their direct sum is. The local bound from the preceding lesson gives \(|\alpha|^r,|\beta|^r<q_v^{1/2}\). If \(|\alpha|>1\), choose a compatible \(r>(\log q_v)/(2\log|\alpha|)\); the first inequality fails. Thus \(|\alpha|\le1\), and the same argument gives \(|\beta|\le1\). Unitarity gives \(|\alpha\beta|=1\), hence both are one. This proves temperedness of the unramified local component. Applying it at each unramified \(v\) proves unramified Ramanujan.

The mere existence of an automorphic transfer does not justify the constituent bound: the residual example (5.4) shows why. Also, a transfer asserted only outside a finite set that varies with \(r\) may never match at the chosen \(v\). These are additional requirements, not consequences proved by this solution. ∎

**Exercise 7.3.** Show that the symmetric square of a dihedral cusp form is not cuspidal. Include the quadratic twist in the one-dimensional summand and handle the case in which the rank-two summand splits.

**Solution.** Retain the isobaric existence hypothesis of Proposition 4.2. Write \(\pi=\operatorname{AI}_{E/F}\theta\), with \(\theta\ne\theta^\tau\). In the induced basis of (4.4), \(e_1^2,e_2^2\) form \(\operatorname{Ind}\theta^2\), and \(e_1e_2\) is a line of character \((\det\rho)\varepsilon_{E/F}\). The twist is forced by the opposite signs of \(\det\rho(t)=-a\) and the eigenvalue \(a\) on that line. Quadratic induction, class field theory and the assumed automorphic isobaric construction therefore give the transfer (4.6). If \(\theta^2\ne(\theta^\tau)^2\), its decomposition has a rank-two cusp and a rank-one character. If \(\theta^2\) is invariant, extend it by either square root of its value on \(t^2\); the two extensions differ by \(\varepsilon_{E/F}\), and the induction is their sum. The transfer then has three rank-one constituents. In either case it has more than one constituent, so isobaric uniqueness rules out a rank-three cusp form with the same almost-all Satake classes. ∎

**Exercise 7.4.** Assuming symmetric-power and tensor-product functoriality, deduce the Selberg eigenvalue conjecture for congruence subgroups. Specify the local and spectral properties needed beyond weak transfer.

**Solution.** Use the transfer hypotheses of Theorem 6.2, the local duality, complex-conjugation, direct-sum and Rankin–Selberg compatibilities (6.3a), and the analytic hypotheses of the preceding lesson's Corollary 4.5. If \(0<\lambda<1/4\), Lemma 6.1a supplies a unitary cusp with the real parameter (6.2), where \(t=\sqrt{1/4-\lambda}>0\). Its \(r\)-th symmetric power has characters (6.3). Tensoring with the dual gives the characters \(\nu^{2(k-j)t}\), with trivial parity; the character \(\nu^{-2rt}\) occurs.

Choose a unitary cuspidal constituent \(\sigma_a\) of the tensor transfer whose real parameter contains that character. Unitarity identifies its contragredient with its complex conjugate, as proved in Lemma 6.1b. The local compatibilities therefore force \(\nu^{2rt}\) to occur in the same constituent. Its self-pairing parameter contains \(\nu^{-4rt}\), so its real Rankin–Selberg factor contains \(\Gamma_{\mathbb R}(s-4rt)\). Choose a compatible \(r\ge1/(4t)\). This factor has a pole at the real point \(s=4rt\ge1\), and the other gamma factors have no zeros that could cancel it. Corollary 4.5 says that this self-pairing factor is holomorphic and nonzero at that real point, a contradiction.

Thus \(\lambda\ge1/4\) for every congruence cusp form. The proved rank-two spectral decomposition cited at the end of §6 puts the continuous spectrum at and above \(1/4\), while the residual determinant characters contribute zero. Hence no positive discrete eigenvalue lies below \(1/4\).

Real-place agreement supplies the line \(\nu^{-2rt}\); the unitary cuspidal decomposition lets us apply the self-pairing regularity theorem to a constituent. Weak agreement at almost all finite places supplies neither property. The deduction retains the complete global pole and local factor-identification hypotheses needed for Corollary 4.5. ∎

## 8. Proof dependencies and the remaining conjectures

The local determinant identities, composition, good-place quadratic calculations and symmetric-square splitting are direct proofs in this lesson. Theorems 5.1 and 6.2 prove their conditional deductions with the original transfer scope. The general transfer conjectures, including arbitrary symmetric powers, tensor products, base change and induction, are not established by those calculations.

The following distinctions specify the mathematical inputs to the deductions.

- **General-linear analytic theory.** Corollary 4.5 of the preceding lesson proves real self-pairing regularity and the strict unramified Satake bound from its stated local factor theorem, Theorem 2.1, and complete global Rankin–Selberg theorem, Theorem 3.1. The positivity and Landau arguments are written out there. The arbitrary-rank local integral construction and the global continuation, functional equation and exact simple-pole theorem remain unproved foundations of that lesson. They are needed here; a source citation does not replace them. The general-rank standard analytic theorem, its Theorem 1.1, is also needed for the strong-Artin entireness deduction. Degree one has the actual Tate proof in Tate's global theory: continuation and functional equation, Theorem 9.2; the preceding lesson identifies the separate rational rank-two Whittaker proof.
- **Isobaric existence and classification.** The preceding lesson, §6, states the local construction, global automorphic existence and unitary cuspidal normalization, but does not prove them in general rank over every number field. Its Theorem 6.1 proves multiset uniqueness under those existence and analytic inputs. The general direct-sum transfer and the rank-three automorphic realization of (4.6) retain that existence requirement. The specific rank-two sum of the invariant-character case is constructed in Proposition 4.1a here. Free statement locators are [Getz–Hahn, 22 April 2022 draft, Theorems 10.5.1–10.5.2, (10.21), and Theorem 10.6.5, pp.246–251].
- **Quadratic induction.** For a noninvariant inducing character the all-number-field automorphy proof is in Dihedral forms, examples, and the Ramanujan conjecture for GL₂, Theorem 2.1 and §2.1. Its Propositions 1.2–1.3 prove norm, transfer and invariant-character compatibility; its Lemma 2.2 supplies the number-field Hecke strip estimates; the all-field converse is proved in Multiplicity one, strong multiplicity one and the converse theorem, Theorem 4.5. The invariant-character parameter splits by the extension argument in §4 here, and Proposition 4.1a realizes the resulting rank-two sum automorphically by an all-number-field theta integral. Its continuation, section generation, moderate growth, injectivity and noncuspidality are proved there using the actual adelic Poisson and Hecke nonvanishing proofs and the proved local principal-series classification. The earlier dihedral lesson, Theorem 3.1, also proves the CM theta realization used in the holomorphic example.
- **Local correspondence.** The symmetric-power and tensor-product deductions use direct sums of local general-linear parameters. For Theorem 6.2 the precise additional requirements are (6.3a): compatibility with contragredients, complex conjugation, isobaric sums and analytic Rankin–Selberg factors. The real-character factor is proved in NT-ADL-08, Proposition 8.2; the rank-two real classification used in Lemma 6.1a is proved in the named real-representation lesson, Theorem 3.2 and Proposition 4.1. This does not supply a general-rank proof of all of (6.3a), which remain hypotheses here. General reductive-group packets and their global multiplicity conditions are also outside these proofs.
- **The congruence spectrum.** Lemma 6.1a gives the Maass realization from the proved principal-level quotient and cuspidal Hilbert decomposition. The rational rank-two Eisenstein lesson, Theorem 6.1 and §6.5, proves full spectral completeness and residual exhaustion at every finite level. Thus the passage from cusp forms to all positive discrete eigenvalues uses that earlier proof, rather than an unproved arbitrary-rank residual classification. The latter is still a separate theorem in the preceding lesson.

The existence of a transfer, its cuspidality, unitary normalization of each constituent, and its compatibility at a specified place are separate assertions. Keeping them separate is what makes the Ramanujan and Selberg implications precise. The free sources below locate the conjectures and the stated foundational theorems; they are not being used as a list of all currently known cases.

## References

- J. Arthur, [“An introduction to Langlands functoriality”](https://www.math.toronto.edu/arthur/pdf/Introduction_to_Langlands_Functoriality_June29.pdf), freely accessible author draft, June 2020, pp.14–15, for the trivial-group L-group and the local and global functoriality questions.
- J. R. Getz and H. Hahn, [*An Introduction to Automorphic Representations, with a View toward Trace Formulae*](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), freely accessible author draft dated 22 April 2022. All locators in this lesson refer to this draft: §§10.5–10.7, Conjecture 12.6.1, §§13.2, 13.5 and 13.7.
- R. P. Langlands, [“Where stands functoriality today?”](https://publications.ias.edu/sites/default/files/where-stands-functoriality-today_rpl_7.pdf), 1997, freely accessible IAS author edition, §3, pp.5–7.
- P. Sarnak, [“Notes on the generalized Ramanujan conjectures”](https://publications.ias.edu/sites/default/files/FieldNotesCurrent.pdf), freely accessible IAS author notes, 2005, §1, pp.661–664; p.663, Remark 3, relates real-place temperedness to Selberg's conjecture. The sign convention for its archimedean shifts differs from (6.2).
- R. Taylor, [“Galois representations”](https://www.numdam.org/item/AFST_2004_6_13_1_73_0.pdf), freely accessible article, *Annales de la Faculté des Sciences de Toulouse* 13 (2004), 73–119, especially §5.2, pp.106–107, and §5.3.2, pp.108–110.
