# From automorphic functions to automorphic sheaves

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Draft under mathematical proof repair; full proof closure pending. Public domain (CC0).*

This lesson remains under proof repair. Every cited theorem used as a mathematical input needs a complete proof here or an exact matching earlier programme proof. The historical self-check did not certify that full dependency closure.

An unramified Hecke operator changes a bundle at one point and adds the values of a function over the possible changes. This description makes sense algebraically. It also suggests how to replace the function by a sheaf: pull it to the space of changes, then push it to the space of bundles. The purpose of this lesson is to establish that connection precisely.

We first work out a single modification. We then reconstruct a bundle from all its local lattices, including the step that turns formal lattices into an algebraic sheaf. The rank-one case makes the eigenvalue condition explicit. Finally we explain what traces retain, and what they lose, when a Hecke eigensheaf produces a Hecke eigenfunction.

The algebraic background is vector bundles and divisors on smooth curves. The relevant core courses are [Algebraic Geometry Bridge](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D100) and [Category Theory and Homological Methods](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D80). We assume the construction of the étale fundamental group, the compact-support trace formula, and the normalized spherical Satake isomorphism. Their exact uses are stated below. Basic references are [Frenkel], [Zhu], and [Ben-Zvi].

## 1. A bundle changed at one point

Until the last section, let \(X\) be a smooth projective geometrically connected curve over \(\mathbb F_q\). Write \(F=\mathbb F_q(X)\). For a closed point \(x\), put

\[
R_x=\mathcal O_{X,x},\qquad O_x=\widehat{R_x},\qquad
F_x=\operatorname{Frac}(O_x),\qquad q_x=\#k(x).
\]

Both \(R_x\) and \(O_x\) are discrete valuation rings. We write \(\pi_x\) for a uniformizer. A lattice in \(F_x^n\) means a free \(O_x\)-submodule of rank \(n\) spanning \(F_x^n\).

Fix a rank \(n\) bundle \(E\). A downward elementary modification of type \(i\), where \(0\leq i\leq n\), is an inclusion

\[
E'\hookrightarrow E,\qquad E/E'\simeq k(x)^i.
\]

The quotient here is a skyscraper sheaf. It is annihilated by the maximal ideal of \(R_x\). In particular, specifying its length alone would be insufficient: a cyclic quotient \(R_x/(\pi_x^i)\) is a different modification when \(i>1\).

**Proposition 1.1.** Such modifications are classified by the \(i\)-dimensional quotients of \(E\otimes k(x)\). Their parameter space is the Grassmannian of those quotients. In a trivialization of the completed stalk \(L=\widehat E_x\), their lattices satisfy

\[
\pi_xL\subset L'\subset L,\qquad
\dim_{k(x)}(L/L')=i.
\]

**Proof.** A quotient \(E\otimes k(x)\twoheadrightarrow Q\) defines \(E'\) as the kernel of \(E\to Q_x\). Away from \(x\) this kernel is \(E\). At \(x\), choose a basis of the residue vector space in which the quotient is projection onto the first \(i\) coordinates. Lift the basis to the free \(R_x\)-module \(E_x\); the lift is a basis because its determinant is a unit. The kernel has basis

\[
\pi_xe_1,\ldots,\pi_xe_i,e_{i+1},\ldots,e_n.
\]

It is therefore locally free. Conversely, a modification with the stated quotient gives this residue quotient, and taking its kernel recovers the modification. The same argument applies to families of locally free quotients, which is the defining moduli property of the Grassmannian. Completing the displayed basis gives the lattice description. \(\square\)

Consequently

\[
\deg E'=\deg E-i\deg x.
\]

For \(n=2,i=1\), the fibre is the projective line of quotient lines of \(E\otimes k(x)\). It has \(q_x+1\) rational points. These are different inclusions into the fixed bundle, even when some kernels are isomorphic as abstract bundles.

For example, at a rational point of \(\mathbb P^1\), every modification of \(\mathcal O^2\) of this type has kernel isomorphic to \(\mathcal O\oplus\mathcal O(-1)\). Constant matrices act transitively on the quotient lines, so all kernels are isomorphic. Thus the operator on functions must retain a multiplicity of \(q+1\), rather than count a single isomorphism class once.

## 2. Recovering an algebraic bundle from formal lattices

Define the adèles and integral adèles by

\[
\mathbb A=\prod_{x\in|X|}'F_x,\qquad
\mathbb O=\prod_{x\in|X|}O_x.
\]

The restriction in the product says that an element is integral at all but finitely many points. For invertible matrices it says

\[
GL_n(\mathbb A)=\prod_x'GL_n(F_x)
\quad\text{with respect to }GL_n(O_x).
\]

Thus both a matrix and its inverse are integral almost everywhere. Put \(K=GL_n(\mathbb O)\).

The formal-to-algebraic step is small but essential. It cannot be replaced by choosing analytic discs over a finite field.

**Lemma 2.1.** Let \(R\) be a discrete valuation ring with fraction field \(F\), completion \(O\), and completed fraction field \(F_x\). If \(L\subset F_x^n\) is an \(O\)-lattice, then

\[
M=L\cap F^n
\]

is an \(R\)-lattice and \(M\otimes_R O=L\).

**Proof.** Choose \(N\geq0\) with

\[
\pi^NO^n\subset L\subset\pi^{-N}O^n.
\]

Reduction identifies

\[
\pi^{-N}R^n/\pi^NR^n
\simeq\pi^{-N}O^n/\pi^NO^n,
\]

because \(R/(\pi^{2N})\simeq O/(\pi^{2N})\). Under this identification take the inverse image in \(\pi^{-N}R^n\) of \(L/\pi^NO^n\). This inverse image is exactly \(M\): membership in \(L\) is determined by the displayed residue class. It lies between \(\pi^NR^n\) and \(\pi^{-N}R^n\), so it is finitely generated, torsion free, and of rank \(n\). A finitely generated torsion-free module over a discrete valuation ring is free, by elementary divisor reduction. Completion of the same inverse-image description gives \(L\). \(\square\)

**Theorem 2.2 (Weil's dictionary).** There is a bijection

\[
GL_n(F)\backslash GL_n(\mathbb A)/K
\simeq\{\text{rank }n\text{ bundles on }X\}/\simeq.
\]

The proof works for a smooth projective integral curve over any field, using all its closed points.

**Proof.** For \(a=(a_x)\), prescribe \(L_x=a_xO_x^n\). These are the standard lattices outside a finite set \(S\). Lemma 2.1 gives \(R_x\)-lattices \(M_x=L_x\cap F^n\).

Choose an effective divisor \(D\), supported on \(S\), sufficiently large that at every point

\[
\mathcal O_X(-D)_x^n\subset M_x
\subset\mathcal O_X(D)_x^n.
\]

For each \(x\in S\), the quotient

\[
Q_x=\mathcal O_X(D)_x^n/M_x
\]

has finite length. Regard it as a coherent sheaf supported at \(x\). The natural map to its stalk quotient gives a morphism \(\mathcal O_X(D)^n\to Q_x\). Define

\[
E(a)=\ker\left(\mathcal O_X(D)^n\longrightarrow
\bigoplus_{x\in S}Q_x\right).
\]

This is a coherent sheaf with stalk \(M_x\) at \(x\in S\), and with stalk \(R_x^n\) elsewhere. The kernel is torsion free, and its stalks are free of rank \(n\) over the discrete valuation rings. It is therefore a vector bundle. Its generic fibre is \(F^n\), and its completed stalks are exactly \(L_x\). The description by those stalks shows that a larger choice of \(D\) produces the same subsheaf of rational sections.

Multiplication of \(a\) on the right by \(k\in K\) leaves every lattice unchanged. Multiplication on the left by \(b\in GL_n(F)\) carries every lattice, and hence the algebraic bundle, isomorphically to the one prescribed by \(ba\). This defines the map from double cosets.

Conversely, choose a basis of the generic fibre of a bundle \(E\). The basis identifies it with \(F^n\), so its completed stalk at each \(x\) is a lattice \(L_x\subset F_x^n\). The generic basis extends to a frame on a nonempty open subset: extend its finitely many rational sections and the inverse determinant after removing their poles and zeros. The complement is finite. Thus \(L_x=O_x^n\) almost everywhere. Choose a basis of each lattice, giving matrices \(a_x\). They form an adèlic matrix. A different lattice basis changes \(a\) on the right by \(K\), and a different generic basis changes it on the left by \(GL_n(F)\).

The kernel construction recovers \(E\), since it recovers each of its stalks inside its generic fibre. Finally an isomorphism \(E(a)\simeq E(a')\) induces a generic matrix \(b\in GL_n(F)\) satisfying \(bL_x=L'_x\) for every \(x\). Hence \((a'_x)^{-1}ba_x\in GL_n(O_x)\) for every \(x\), or \(a'=bak\) for some \(k\in K\). This proves injectivity as well as surjectivity. \(\square\)

*Reference:* [Frenkel, §3.2, Weil's lemma].

The proof also identifies automorphisms:

\[
\operatorname{Aut}(E(a))
=GL_n(F)\cap aKa^{-1}.
\]

Indeed, a generic matrix is a bundle automorphism precisely when it preserves every local lattice. Thus the quotient groupoid remembers more than its set of double cosets. The moduli stack \(\operatorname{Bun}_n\) retains these automorphisms and retains families of bundles, which the set of classes cannot describe.

For a connected reductive group \(G\), the analogous adèlic construction initially parametrizes bundles whose generic \(G\)-torsor is trivial. Identifying it with every bundle requires a generic-triviality theorem for the group and field in question. It is not an automatic consequence of the vector-bundle proof. Later uniformization results will state their group hypotheses explicitly.

## 3. Hecke convolution is a sum over modifications

For a fixed \(x\), let \(\mathcal H_{i,x}\) classify the modifications of Proposition 1.1. Write

\[
p(E'\subset E)=E,\qquad r(E'\subset E)=E'.
\]

Our direction convention is

\[
(T_{i,x}f)(E)=\sum_{E'\subset E\,\text{of type }i}f(E')
=(p_*r^*f)(E).
\]

The sum runs over subbundles with their inclusion into the fixed \(E\). Its fibre is a finite set of Grassmannian rational points. It is therefore defined for every function, without a support restriction. Cuspidality and central characters are additional conditions when we study automorphic representations.

**Theorem 3.1.** Under Theorem 2.2 this operator is right Hecke convolution by the characteristic function of

\[
K_xt_iK_x,\qquad K_x=GL_n(O_x),\qquad
t_i=\operatorname{diag}(\underbrace{\pi_x,\ldots,\pi_x}_{i},1,\ldots,1),
\]

with Haar measure normalized by \(\operatorname{vol}(K_x)=1\).

**Proof.** In the completed lattice \(a_xO_x^n\), the modifications are \(a_xL'\), where

\[
\pi_xO_x^n\subset L'\subset O_x^n,
\qquad O_x^n/L'\simeq k(x)^i.
\]

The lifted-basis argument of Proposition 1.1 says exactly that \(L'=hO_x^n\) for \(h\in K_xt_iK_x\). Two matrices give the same lattice if and only if they differ by right multiplication by \(K_x\). Thus the modification fibre is \(K_xt_iK_x/K_x\). Choose right coset representatives \(h_j\), and view them as adèles supported at \(x\). Theorem 2.2 identifies the modified bundle with \([ah_j]\). Every coset \(h_jK_x\) has measure one, and \(f\) is right \(K\)-invariant. Consequently

\[
\int_{K_xt_iK_x}f([ah])\,dh
=\sum_jf([ah_j]),
\]

which is the required sum. Replacing the representative \(a\) by \(bak\) only permutes these lattices and changes their generic frame, so the formula is well defined on double cosets. \(\square\)

In particular

\[
T_{1,x}\mathbf1=(1+q_x+\cdots+q_x^{n-1})\mathbf1,
\qquad
T_{n,x}f(E)=f(E(-x)).
\]

The first formula counts quotient lines. The second follows because the only type \(n\) lattice is \(\pi_xL\).

There is no division by \(\#\operatorname{Aut}(E)\) in this fixed-bundle fibre sum. For an absolute sum over a stack's isomorphism classes, the groupoid measure does involve automorphism weights. These are different sums. The morphism \(p\) is representable: after fixing \(E\), it gives the Grassmannian itself, with no automorphisms of an inclusion inducing the identity on \(E\).

## 4. The rank-one calculation and its arithmetic condition

For an idèle \(a=(a_x)\), define

\[
\operatorname{div}(a)=\sum_xv_x(a_x)[x].
\]

It is a finite sum, and the map \(\mathbb A^\times\to\operatorname{Div}(X)\) is onto: a uniformizer at one place, and units elsewhere, realizes the corresponding point divisor. Its kernel is \(\mathbb O^\times\). A rational function gives its principal divisor. Every line bundle has a rational nonzero section and hence comes from a divisor. Therefore

\[
F^\times\backslash\mathbb A^\times/\mathbb O^\times
\simeq\operatorname{Div}(X)/\operatorname{Prin}(X)
=\operatorname{Pic}(X).
\]

Here \(\operatorname{Pic}(X)\) denotes line bundles defined over \(\mathbb F_q\), up to isomorphism. The direct lattice construction sends \(a\) to \(\mathcal O_X(-\operatorname{div}(a))\), since its stalk is \(\pi_x^{v_x(a_x)}R_x\). This differs by inversion from the displayed divisor map; both are bijections, and the sign is now explicit.

There is one downward modification of a line bundle:

\[
T_xf(L)=f(L(-x)).
\]

If \(\chi:\operatorname{Pic}(X)\to C^\times\) is a character over a coefficient field \(C\), then

\[
T_x\chi=\chi(\mathcal O_X(-x))\chi.
\]

Conversely, suppose a nonzero function satisfies \(T_xf=\lambda_xf\) for every closed point. Since \(T_x\) is invertible, every \(\lambda_x\) is nonzero. The translations by \(\mathcal O(-x)\) generate the Picard group. Thus all values are determined by \(f(\mathcal O)\), which must be nonzero. A relation between divisors forces the corresponding relation between the \(\lambda_x\). It follows that \(f/f(\mathcal O)\) is the character with \(\chi(\mathcal O(-x))=\lambda_x\). This proves that simultaneous nonzero eigenfunctions are precisely scalar multiples of characters.

Unramified class field theory supplies the arithmetic comparison. With reciprocity normalized so that \(\mathcal O(-x)\) corresponds to geometric Frobenius at \(x\), a continuous rank-one étale local system \(\mathcal E\) produces the character satisfying

\[
\chi_{\mathcal E}(\mathcal O(-x))
=\operatorname{Tr}(\operatorname{Fr}_x,\mathcal E_{\bar x}).
\]

This is the rank-one reciprocity theorem [Frenkel, §4.2], using inversion to match our downward modification convention. For finite-order characters it is the finite unramified class-field correspondence. Continuous characters with infinite arithmetic monodromy require the corresponding continuity condition. The next calculation shows why that condition matters.

### The projective line

Every line bundle on \(\mathbb P^1_{\mathbb F_q}\) is \(\mathcal O(d)\), and its class is determined by \(d\). For completeness, use the two affine charts, on which a line bundle is free because \(\mathbb F_q[t]\) and \(\mathbb F_q[t^{-1}]\) are principal ideal domains. The transition function is a unit of \(\mathbb F_q[t,t^{-1}]\), hence is \(ct^d\). A change of frame removes \(c\), leaving the integer \(d\). Thus \(\operatorname{Pic}(\mathbb P^1)=\mathbb Z\).

Let a rank-one local system on the ground field have geometric Frobenius eigenvalue \(\alpha\), and pull it to \(\mathbb P^1\). At a degree \(e\) point its trace is \(\alpha^e\). The character and eigenfunction are

\[
\chi_\alpha(\mathcal O(d))=\alpha^{-d},\qquad
T_x\chi_\alpha(\mathcal O(d))
=\alpha^{\deg x}\chi_\alpha(\mathcal O(d)).
\]

On the degree \(d\) Picard point, take the rank-one Weil sheaf with Frobenius \(\alpha^{-d}\). Its pullback along \(y\mapsto\mathcal O(-y)\), the negative Abel map consistent with our Hecke direction, has Frobenius \(\alpha\). Its trace is exactly this character. Tensor product of line bundles adds degrees, so these Weil sheaves are multiplicative. The positive Abel map would instead give the local system with eigenvalue \(\alpha^{-1}\).

Every finite étale connected cover of \(\mathbb P^1_{\overline{\mathbb F}_q}\) has degree one. Indeed the separable Riemann–Hurwitz formula for an étale cover \(Y\to\mathbb P^1\) of degree \(m\) gives \(2g(Y)-2=-2m\), and \(g(Y)\geq0\) forces \(m=1\). Hence the geometric étale fundamental group is trivial. A rank-one étale local system on \(\mathbb P^1_{\mathbb F_q}\) therefore comes from the ground field.

If \(\alpha\) lies in a finite extension \(C\) of \(\mathbb Q_\ell\), it defines a continuous representation of \(\widehat{\mathbb Z}\) exactly when \(\alpha\) is an \(\ell\)-adic unit. Necessity follows from compactness: valuation maps a compact subgroup of \(C^\times\) to a finite subgroup of \(\mathbb Z\), hence to zero. Conversely \(\mathcal O_C^\times\) is profinite, so the homomorphism from \(\mathbb Z\) sending the geometric Frobenius generator to \(\alpha\) extends to its profinite completion. A Weil local system only asks for an invertible Frobenius operator and permits any \(\alpha\ne0\). The finite-determinant arithmetic theorem in rank one further restricts \(\alpha\) to a root of unity.

## 5. From a correspondence of functions to one of sheaves

Fix \(\ell\ne\operatorname{char}(\mathbb F_q)\). A bounded constructible Weil complex \(\mathcal K\) on a finite-type space \(Y\) has trace function

\[
t_{\mathcal K}(y)=\sum_j(-1)^j
\operatorname{Tr}(\operatorname{Fr}_y,H^j(\mathcal K_{\bar y})).
\]

All Frobenius operators here are geometric. Pullback pulls back this function; tensor product multiplies functions. For a finite-type morphism \(u:Z\to Y\), the compact-support trace formula gives

\[
t_{u_!\mathcal K}(y)
=\sum_{z\in Z_y(\mathbb F_q)}t_{\mathcal K}(z).
\]

For the modification correspondence, one can apply this formula after fixing a bundle: the fibre is the proper Grassmannian of Proposition 1.1. Thus \(p_!=p_*\) on this correspondence, and

\[
\mathsf H^{\mathrm{raw}}_{i,x}=p_!r^*,\qquad
t_{\mathsf H^{\mathrm{raw}}_{i,x}\mathcal K}
=T_{i,x}t_{\mathcal K}.
\]

This uses the trace formula as a prerequisite. The identification of the actual fibre and of its Hecke convolution has been proved above.

**Proposition 5.1.** For integers \(s,m\),

\[
t_{\mathcal K[s](m)}(y)=(-1)^s q^{-m}t_{\mathcal K}(y)
\quad(y\in Y(\mathbb F_q)).
\]

At a degree \(e\) point, replace \(q\) by \(q^e\).

**Proof.** By the cohomological convention \(H^j(\mathcal K[s])=H^{j+s}(\mathcal K)\). Reindexing the alternating sum gives the sign \((-1)^s\). Geometric Frobenius on \(\mathbb Q_\ell(1)\) is multiplication by \(q^{-1}\), giving the second factor. \(\square\)

*Reference:* [Frenkel, §3.8] attributes a power of \(q_x\) to a cohomological shift. The shift supplies only the sign above; a Tate twist supplies the power.

If a normalization uses a half Tate twist, choose the square root of \(q\) and its Weil structure explicitly. For \(d_i=i(n-i)\), the kernel normalization \([d_i](d_i/2)\) changes the raw trace operator to

\[
(-1)^{d_i}q_x^{-d_i/2}T_{i,x}.
\]

This statement fixes the trace normalization of that kernel. The full tensor-compatible Satake convention, including its commutativity constraint, belongs to the lesson on Hecke functors. Keeping the raw operator here prevents a hidden shift or sign from entering the arithmetic examples.

The eigencondition is an isomorphism of sheaves over the moving-point correspondence, together with tensor and symmetry compatibility. Applying trace at a point to such an isomorphism gives an eigenvalue equation. The converse does not follow from traces. For instance \(\mathcal K\oplus\mathcal K[1]\) has identically zero trace but need not be zero. Even on a point, distinct two-dimensional Frobenius representations can have the same trace: eigenvalues \((1,3)\) and \((2,2)\) both give trace four. Traces over extension fields reveal more, but an equality of functions still does not specify coherent eigenisomorphisms.

## 6. What the arithmetic theorem contributes

The normalized spherical Satake isomorphism associates a semisimple dual-group parameter to a spherical eigencharacter. In the convention where \(t_i\) is sent to \(q_x^{i(n-i)/2}\) times the character of \(\bigwedge^i\mathrm{std}\), a parameter with eigenvalues \(z_1,\ldots,z_n\) gives

\[
T_{i,x}f=q_x^{i(n-i)/2}
e_i(z_1,\ldots,z_n)f.
\]

The minuscule coweight determines this power; Proposition 5.1 separately determines the sign and twist when a sheaf kernel is used. Inverting the correspondence replaces the dual representation and its parameter by their inverse conventions.

The unramified instance of the Drinfeld–Lafforgue theorem says the following. Irreducible continuous rank \(n\) representations of \(\pi_1(X)\) over \(\overline{\mathbb Q}_\ell\), defined over a finite coefficient extension and with finite-order determinant, correspond to everywhere unramified irreducible cuspidal automorphic representations of \(GL_n(\mathbb A)\) with finite-order central character. After fixing coefficient comparison, their normalized Satake parameters are the eigenvalues of geometric Frobenius, with the reciprocity direction chosen consistently. The spherical vector is determined up to nonzero scalar. The theorem is a bijection of these classes; it is not a bijection from all functions on all bundles to all local systems.

*Reference:* [Frenkel, §§2.2–2.4, Theorem on the Langlands correspondence].

For general reductive groups, V. Lafforgue's excursion-operator construction associates semisimple global parameters to cuspidal automorphic data. It does not provide a universal inverse correspondence between individual representations and parameters. This distinction is discussed in [Zhu, §2.2].

The geometric theorem for irreducible \(GL_n\)-local systems constructs Hecke eigensheaves. Its construction is taught later through the averaging and vanishing arguments. The role of the present lesson is the dictionary it requires: the bundle space, its actual modification fibres, the induced operator, and the trace implication.

Over an algebraically closed field \(k\) of characteristic zero, we continue to study algebraic bundles and their Hecke correspondences, but use de Rham local systems and D-modules. There is no ground-field Frobenius trace construction in this setting. The categorical theorem concerns the specific functor

\[
\mathbb L_G:
D\operatorname{-mod}_{1/2}(\operatorname{Bun}_G)
\longrightarrow
\operatorname{IndCoh}_{\mathrm{Nilp}}
(\operatorname{LocSys}_{\check G}^{\mathrm{dR}}).
\]

It is an equivalence for the unramified characteristic-zero setting. The half twist, derived local systems, and nilpotent singular-support condition are essential parts of its statement. The later lessons construct these categories and prove the formal deductions in the five-paper proof. A trace calculation by itself neither establishes nor verifies this equivalence.

## 7. Exercises

**Exercise 7.1 (easy).** An idèle has valuation \(2\) at a degree-three point \(x\), valuation \(-1\) at a rational point \(y\), and valuation zero elsewhere. Compute the degree of its line bundle under the lattice convention. Explain what changes when the idèle is multiplied by a rational function.

**Exercise 7.2 (easy).** For \(E\) of rank two at a degree-two point, compute the number of downward elementary modifications. Deduce the value of \(T_{1,x}\mathbf1\). Explain why this answer does not require the kernels to be pairwise nonisomorphic.

**Exercise 7.3 (medium).** Prescribe an arbitrary lattice \(L_x\subset F_x^3\) at one point and the standard lattice elsewhere. Give an algebraic kernel construction of its bundle and prove that no choice of a matrix whose coefficients are rational functions is needed. Show that changing the generic frame induces the left quotient in Weil's dictionary.

**Exercise 7.4 (medium).** On \(\operatorname{Pic}(\mathbb P^1)=\mathbb Z\), solve the equation \(T_yf=af\) at a rational point for \(a\ne0\). Determine the eigenvalue at a degree-three point. Compute the trace effect of replacing the corresponding Weil sheaf by its shift \([1](2)\).

**Exercise 7.5 (hard).** Fix a finite extension of \(\mathbb Q_\ell\) containing \(\alpha\ne0\). Compare the eigenfunction \(d\mapsto\alpha^{-d}\), the multiplicative Weil sheaf on the Picard points, and a continuous rank-one étale local system on \(\mathbb P^1_{\mathbb F_q}\). Prove exactly when the last object exists. Treat \(\alpha=\ell\) and a root of unity of order prime to \(\ell\).

## 8. Solutions

**Solution 7.1.** The divisor is \(2x-y\), of degree \(2\cdot3-1=5\). The lattice convention gives \(\mathcal O(-2x+y)\), of degree \(-5\). Multiplication by \(b\in F^\times\) adds \(\operatorname{div}(b)\); multiplication by \(b\) is an isomorphism between the lattice bundles. Principal divisors have degree zero, so the degree remains \(-5\). Integral units change neither valuations nor lattices. This also verifies the two quotients in the rank-one dictionary directly.

**Solution 7.2.** The residue field has \(q^2\) elements. Nonzero linear functionals on a two-dimensional vector space number \(q^4-1\). Two functionals define the same kernel precisely when they differ by a nonzero scalar, so the number is

\[
(q^4-1)/(q^2-1)=q^2+1.
\]

Every inclusion contributes the value one to the sum, hence \(T_{1,x}\mathbf1=q^2+1\). Different inclusions are different points of the modification fibre. An abstract isomorphism of kernels does not identify those points.

**Solution 7.3.** Choose \(N\) with \(\pi_x^NO_x^3\subset L_x\subset\pi_x^{-N}O_x^3\). Let \(M_x=L_x\cap F^3\), constructed through the finite quotient in Lemma 2.1, and put \(D=Nx\). The required bundle is

\[
\ker\left(\mathcal O(D)^3\to
(\mathcal O(D)_x^3/M_x)_x\right).
\]

Its stalk at \(x\) is \(M_x\); all other stalks are standard. Completion yields \(L_x\), and the kernel is locally free by the discrete valuation ring argument. The quotient only uses finitely many residue coefficients of the lattice, so no rational matrix representing the whole formal lattice is required. A generic frame change is a single element \(b\in GL_3(F)\) acting on every lattice at once. The isomorphism identifies the prescribed bundle with that of \(bL_x\) and the transformed other lattices. This is exactly the left action; local frame changes are the right integral action. Applying the same construction to every bundle and the isomorphism argument of Theorem 2.2 proves both directions of the general dictionary.

**Solution 7.4.** At a rational point, \(T_yf(d)=f(d-1)\). Hence \(f(d-1)=af(d)\) and iteration in both directions gives \(f(d)=c a^{-d}\), for an arbitrary scalar \(c\). A degree-three point gives \(f(d-3)=a^3f(d)\). Taking the Weil sheaf whose Frobenius on component \(d\) is \(a^{-d}\) realizes the normalized character \(c=1\). Its shift \([1](2)\) has trace \(-q^{-2}a^{-d}\) on an \(\mathbb F_q\)-point of Picard degree \(d\). At points defined over \(\mathbb F_{q^e}\) the multiplier is \(-q^{-2e}\). The shift changes the sign and the twist changes the power; their effects are independent.

**Solution 7.5.** The eigenfunction exists for every \(\alpha\ne0\), and the Weil sheaf exists because an invertible Frobenius operator defines a rank-one Weil object on each Picard point. Their tensor compatibility follows from \(\alpha^{-(d+d')}=\alpha^{-d}\alpha^{-d'}\). A rank-one étale local system on the projective line has trivial geometric monodromy by the étale-cover argument in section 4. It is therefore the same as a continuous character of \(\operatorname{Gal}(\overline{\mathbb F}_q/\mathbb F_q)=\widehat{\mathbb Z}\) with geometric Frobenius value \(\alpha\). The compactness argument and profinite-unit construction in section 4 prove that this exists precisely when \(\alpha\) is a unit. For \(\alpha=\ell\) it does not exist, although the function and Weil sheaf still exist. A root of unity gives a character of a finite cyclic quotient, so it exists and has finite-order determinant. Its trace at a degree \(e\) point is \(\alpha^e\), which equals the eigenvalue of the character at that point's modification. This checks the rank-one arithmetic correspondence on \(\mathbb P^1\), including continuity and Frobenius direction.

## What this lesson does not prove

The imported arithmetic input is the Drinfeld–Lafforgue theorem with the finite-determinant and cuspidality conditions stated in section 6 [Frenkel, §§2.2–2.4]. Unramified rank-one reciprocity for a general curve is also an input [Frenkel, §4.2]; the projective-line comparison is proved here. The compact-support trace formula is used in the form stated in section 5 [Frenkel, §3.3]. The normalized spherical Satake isomorphism is used only for the eigenvalue interpretation [Frenkel, §5.2]. The étale case of Riemann–Hurwitz is a background result [Stacks, Tag 0C1B]. The geometric \(GL_n\) construction and the categorical characteristic-zero equivalence are later course topics; their mention here is a preview, not their proof. No counting conjecture about local systems is assumed.

## References

- [Frenkel] E. Frenkel, *Lectures on the Langlands program and conformal field theory*, [freely accessible author preprint, arXiv:hep-th/0512172](https://arxiv.org/abs/hep-th/0512172). Sections 2.2–2.4, 3.2–3.3, 3.7–3.8, 4.2, and 5.2.
- [Zhu] X. Zhu, *Arithmetic and geometric Langlands program*. [Open preprint](https://arxiv.org/abs/2504.07502). Section 2.2.
- [Ben-Zvi] D. Ben-Zvi, *What is the geometric Langlands correspondence about?* [Open survey](https://arxiv.org/abs/2605.23167). Sections 1–2.
- [Gaitsgory–Raskin] D. Gaitsgory and S. Raskin, *Proof of the geometric Langlands conjecture V: the multiplicity one theorem*. [Open preprint](https://arxiv.org/abs/2409.09856). Introduction and statement of the main theorem.
- [Stacks] The [Stacks project](https://stacks.math.columbia.edu/), Tag 0C1B, Riemann–Hurwitz. The text used here is the [AI Integrated Stacks Project English edition](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/curves.html#section-riemann-hurewitz), which retains these tags and includes AI-proposed corrections and AI-written additions. Those additions are not reviewed by the Stacks project's maintainers. No text from either edition is reproduced here.
