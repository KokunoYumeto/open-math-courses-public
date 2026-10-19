# Permutation symmetry and Powers factors

*Mathematical exposition by GPT-6.1 Sol and GPT-6 Astra (OpenAI). Original programme text: CC0-1.0. The stated prerequisite theorems determine the scope of the classification conclusion.*

## Introduction

A two-level system with unequal probabilities has a simple modular action: the two off-diagonal matrix entries rotate at opposite frequencies. Repeating that system infinitely often produces a factor whose type remembers the ratio of those probabilities. Finite coordinate permutations explain why the centralizer is a factor, and coordinate flips give a concrete measurable model of the same algebra.

We construct the Powers factor, calculate its modular spectrum, and prove that its centralizer is an approximately finite factor of type \({\rm II}_1\). We then identify the diagonal algebra and the flip action, including the conditional expectation required to recognize the crossed product. The final section applies the classification theorem for injective factors with the same parameter.

The construction targets are [Takesaki III], Theorem XVIII.1.1, Lemmas XVIII.1.2–1.3 and Theorem XVIII.1.4(i), printed pages 297–300. In particular, the permutation argument in Section 3 follows the mathematical mechanism of Lemma XVIII.1.2; its implementing unitaries and approximation estimates are written out here. The local eigenbasis, finite centralizer blocks, normal diagonal identification and full conditional-expectation check organize the construction before the uniqueness application. [Connes] supplies the spectral theorem. [Powers] gives the historical source for the family; the linked edition is A. G. Stepin's Russian translation. The proof construction used here is credited to [Takesaki III], while [Takesaki II] supplies modular background. We assume standard form, the Tomita operator and the KMS identity for a faithful normal state. For the type calculation we use Connes's factorial-centralizer spectral theorem, stated precisely in Section 4 and proved for arbitrary faithful normal semifinite weights in [Theorem PC8.1 of the crossed-product companion](../foundations/crossed-product-and-injective-core-foundations.md#pc8). For crossed-product recognition we use [Theorem PC2.1 of the crossed-product companion](../foundations/crossed-product-and-injective-core-foundations.md#pc2). The classification consequence also uses discrete decomposition, [Trace scaling on the hyperfinite semifinite factor](trace-scaling-on-the-hyperfinite-semifinite-factor.md), and the injective-factor results specified in Section 6.

For the bounded representation steps, use [Bounded topology and tracial representations, Section 3A](bounded-topology-and-tracial-representations.md#3a-faithful-state-tests-and-ordinary-extraction), the [bounded-topology companion](../foundations/bounded-topology-foundations.md), and [Normal tensor tests and tracial GNS identifications](../foundations/normal-tensor-and-tracial-product-foundations.md). TF0 supplies the Hilbert tensor operations on the finite reference spaces. The pointed nontracial product is constructed directly in Section 1; it is not inferred from the tracial scope of TF2. TF3 will be applied only to the abelian diagonal algebras, where the faithful states are traces. The full modular-weight and normal-filter foundations used by PC8, discrete decomposition and relation–factor type correspondence remain separate prerequisites.

Fix \(0<\lambda<1\), and write
\[
 \begin{gathered}
 a=\frac1{1+\lambda},\qquad b=\frac\lambda{1+\lambda},\\
 h=\begin{pmatrix}a&0\\0&b\end{pmatrix}.
 \end{gathered}
\tag{0.1}
\]
The matrix trace \(\operatorname{Tr}\) is unnormalized, so \(\operatorname{Tr}(h)=1\). On \(M_2(\mathbb C)\) put \(\omega_0(x)=\operatorname{Tr}(hx)\). We index its matrix entries by \(0,1\).

## 1. Building the product representation

Use the Hilbert space \(H_0=M_2(\mathbb C)\) with Hilbert–Schmidt norm and reference vector \(\xi_0=h^{1/2}\). Left multiplication represents \(M_2(\mathbb C)\) on \(H_0\), and
\[
 \langle x\xi_0,\xi_0\rangle
 =\operatorname{Tr}(hx)=\omega_0(x).
\tag{1.1}
\]
Since \(h\) is invertible, both the left multiples and the right multiples of \(\xi_0\) span \(H_0\).

Let \(H\) be the incomplete infinite tensor product of copies of \((H_0,\xi_0)\): it is the completion of tensors in which only finitely many entries differ from \(\xi_0\). Let \(\xi\) be the tensor of all reference vectors. The algebra
\[
 A_n=M_2(\mathbb C)^{\otimes n}\otimes1
\tag{1.2}
\]
acts by left multiplication on the first \(n\) factors. Define
\[
 R_\lambda=\left(\bigcup_{n\ge1}A_n\right)'',
 \qquad
 \omega(x)=\langle x\xi,\xi\rangle.
\tag{1.3}
\]
Thus \(\omega\) is normal, and its restriction to each \(A_n\) has density \(h^{\otimes n}\).

**Proposition 1.1.** The vector \(\xi\) is cyclic and separating for \(R_\lambda\). The state \(\omega\) is faithful. The algebra is approximately finite dimensional and has separable predual.

*Proof.* Local left multiples of \(\xi\) span every finite tensor space, so they are dense in \(H\). This proves cyclicity. Local right multiplications commute with every local left multiplication, and hence with \(R_\lambda\). Their multiples of \(\xi\) are also dense. If \(x\xi=0\) for \(x\in R_\lambda\), then \(x\) vanishes on that dense set of right multiples and therefore vanishes. This proves separation. If \(x\ge0\) and \(\omega(x)=0\), then \(x^{1/2}\xi=0\), so \(x=0\).

The increasing finite-dimensional algebras \(A_n\) generate \(R_\lambda\), which proves approximate finite dimensionality. A countable basis of finite-excitation tensors makes \(H\) separable. The predual of a von Neumann algebra on a separable Hilbert space is a quotient of the separable trace-class space, so it is separable. \(\square\)

For bounded approximations we use
\[
 \begin{aligned}
 \|x\|_\omega^2&=\omega(x^*x),\\
 \|x\|_\omega^{\sharp\,2}&=\omega(x^*x)+\omega(xx^*).
 \end{aligned}
\tag{1.4}
\]
Kaplansky density gives local approximations with the same operator-norm bound and with sharp error tending to zero. Faithfulness makes sharp convergence on bounded sets equivalent to strong-star convergence in this representation.

## 2. Modular frequencies and finite centralizer blocks

On one Hilbert–Schmidt space the modular operator and conjugation are
\[
 \Delta_0(X)=hXh^{-1},\qquad J_0(X)=X^*.
\tag{2.1}
\]
Indeed, for \(X=xh^{1/2}\),
\[
 J_0\Delta_0^{1/2}(X)
 =h^{-1/2}X^*h^{1/2}=x^*h^{1/2}.
\tag{2.2}
\]
This is the defining Tomita operation on \(x\xi_0\).

Choose the following orthonormal basis of \(H_0\):
\[
 \begin{gathered}
 \xi_0=\sqrt a\,e_{00}+\sqrt b\,e_{11},\\
 \eta_0=\sqrt b\,e_{00}-\sqrt a\,e_{11},\\
 e_{01},\ e_{10}.
 \end{gathered}
\tag{2.3}
\]
The first two vectors have modular eigenvalue \(1\); the last two have eigenvalues \(\lambda^{-1}\) and \(\lambda\), respectively. Finite-excitation tensors of these four vectors form an orthonormal basis of \(H\).

**Proposition 2.1.** The modular operator \(\Delta_\omega\) is diagonal on this basis, with all eigenvalues \(\lambda^k\), \(k\in\mathbb Z\). Its spectrum is
\[
 \operatorname{Sp}(\Delta_\omega)
 =\{0\}\cup\{\lambda^k:k\in\mathbb Z\}.
\tag{2.4}
\]
Its kernel is zero. The modular action on a local entry is
\[
 \begin{aligned}
 \sigma_t^\omega(e_{01})&=\lambda^{-it}e_{01},\\
 \sigma_t^\omega(e_{10})&=\lambda^{it}e_{10}.
 \end{aligned}
\tag{2.5}
\]
The least positive period of this action is
\[
 P=\frac{2\pi}{|\log\lambda|}.
\tag{2.6}
\]

*Proof.* On each finite tensor space the Tomita operation is the tensor product of the operations in (2.2). The tensor products of \(J_0\) define an antiunitary \(J\) on \(H\), because \(J_0\xi_0=\xi_0\). Define a positive diagonal operator \(D\) on the finite-excitation basis by multiplying its local modular eigenvalues. Finite linear combinations of basis vectors are a core for \(D^{1/2}\), and on that core the Tomita operation is \(JD^{1/2}\).

This core also gives the full Tomita closure. For \(x\in R_\lambda\), bounded local approximations \(x_n\) give both \(x_n\xi\to x\xi\) and \(x_n^*\xi\to x^*\xi\). Hence the graph of the Tomita operation on all \(x\xi\) lies in the closure of its local graph. The reverse inclusion follows because local elements belong to \(R_\lambda\). Thus \(\Delta_\omega=D\).

Every basis eigenvalue is an integer power of \(\lambda\), and every such power occurs by placing finitely many \(e_{10}\)'s or \(e_{01}\)'s in distinct coordinates. A diagonal self-adjoint operator has spectrum the closure of its diagonal values. These values have no positive finite accumulation point; their only finite accumulation point is \(0\). No basis eigenvalue is zero, so the kernel is zero even though \(0\) belongs to the spectrum.

Conjugation by \(\Delta_\omega^{it}\) acts on a local matrix by conjugation with \(h^{it}\), which gives (2.5). At time \(P\), both off-diagonal rotations equal one and every local element is fixed, so the whole algebra is fixed. Conversely, fixing the nonzero first-coordinate entry \(e_{01}\) requires \(t\log\lambda\in2\pi\mathbb Z\). This proves the asserted least period. \(\square\)

Let
\[
 \begin{gathered}
 F=(R_\lambda)_\omega,\qquad F_n=A_n\cap F,\\
 F=\{x:\sigma_t^\omega(x)=x\text{ for all }t\}.
 \end{gathered}
\tag{2.7}
\]
For a binary word \(s=(s_1,\ldots,s_n)\), write \(|s|=\sum_j s_j\). The vector indexed by \(s\) in \((\mathbb C^2)^{\otimes n}\) has density value \(a^{n-|s|}b^{|s|}\). These values are distinct for different \(|s|\), because \(b/a=\lambda\ne1\). Therefore
\[
 F_n\cong\bigoplus_{k=0}^n M_{\binom nk}(\mathbb C).
\tag{2.8}
\]
The state is scalar on each density block and hence tracial on \(F_n\). If \(\tau_k\) is the normalized trace of the block indexed by \(k\), then
\[
 \begin{gathered}
 \omega|_{F_n}=\sum_{k=0}^n p_{n,k}\tau_k,\\
 p_{n,k}=\binom nk a^{n-k}b^k.
 \end{gathered}
\tag{2.9}
\]
The numbers \(p_{n,k}\) sum to one. The individual block densities and the total probabilities of the blocks are different quantities.

For example, take \(\lambda=1/3\) and \(n=3\). The four blocks have the following sizes and total probabilities.

| Number of ones \(k\) | Matrix size | Block probability |
| --- | --- | --- |
| \(0\) | \(1\) | \(27/64\) |
| \(1\) | \(3\) | \(27/64\) |
| \(2\) | \(3\) | \(9/64\) |
| \(3\) | \(1\) | \(1/64\) |

**Proposition 2.2.** The finite-dimensional algebras \(F_n\) increase and generate \(F\). The restriction \(\omega|_F\) is a faithful normal tracial state.

*Proof.* Average the periodic modular action:
\[
 E_F(x)=\frac1P\int_0^P\sigma_t^\omega(x)\,dt.
\tag{2.10}
\]
Haar averaging is a normal completely positive unital projection onto \(F\), is \(F\)-bimodular, and preserves \(\omega\). Here are the continuity and normality details also used in Section 5. The strongly continuous implementing unitaries send a vector-functional test to one whose two vectors vary in norm. The coefficient estimate in TF1, followed by the norm-convergent vector-series representation CP06, proves norm continuity on every predual test. Its Bochner integral over the compact group defines a bounded predual operator; the adjoint of that operator is the displayed average, so the average is normal on the whole algebra. Positivity at every matrix level follows by averaging the positive quadratic forms of the amplified automorphisms. Haar invariance proves the projection property, and fixed elements can be moved through the integral to prove bimodularity. Positivity and \(\omega E_F=\omega\) make it faithful. Kadison's inequality applied to \(x\) and \(x^*\) gives
\[
 \|E_F(x)\|_\omega^\sharp\le\|x\|_\omega^\sharp.
\tag{2.11}
\]
The modular action preserves each \(A_n\), so \(E_F(A_n)=F_n\). For \(x\in F\), apply \(E_F\) to bounded local sharp approximations of \(x\). Equation (2.11) gives bounded strong-star approximations from the \(F_n\). Thus their union generates \(F\). The inclusions \(F_n\subset F_{n+1}\) also follow from \(h^{\otimes(n+1)}=h^{\otimes n}\otimes h\).

Faithfulness and normality of the restriction follow from Proposition 1.1. A fixed element is entire analytic for the modular action. The KMS identity consequently gives \(\omega(xy)=\omega(yx)\) for \(x,y\in F\), proving traciality. \(\square\)

## 3. Permutations force a factorial centralizer

A finite permutation \(g\) of the coordinates is implemented by a permutation matrix in some \(A_N\). This matrix commutes with \(h^{\otimes N}\), since all coordinate densities are identical. Its implementing unitary \(u_g\) therefore belongs to \(F_N\subset F\). Write \(\alpha_g=\operatorname{Ad}u_g\).

Let \(g_n\) interchange the blocks \(1,\ldots,n\) and \(n+1,\ldots,2n\), fixing the later coordinates. Put \(\alpha_n=\alpha_{g_n}\). These automorphisms preserve \(\omega\).

**Lemma 3.1.** For all \(x,y\in R_\lambda\),
\[
 \omega(\alpha_n(x)y)\longrightarrow\omega(x)\omega(y).
\tag{3.1}
\]

*Proof.* If \(x_0,y_0\in A_m\) and \(n>m\), the supports of \(\alpha_n(x_0)\) and \(y_0\) are disjoint. Product independence gives
\[
 \omega(\alpha_n(x_0)y_0)=\omega(x_0)\omega(y_0).
\tag{3.2}
\]
For general \(x,y\), choose \(x_0,y_0\in A_m\) with norms at most \(\|x\|,\|y\|\) and sharp errors less than \(\varepsilon\). Cauchy–Schwarz and state invariance give
\[
 \begin{aligned}
 |\omega(\alpha_n(x-x_0)y)|
 &\le\varepsilon\|y\|,\\
 |\omega(\alpha_n(x_0)(y-y_0))|
 &\le\varepsilon\|x\|.
 \end{aligned}
\tag{3.3}
\]
For the first estimate the relevant square norm is \(\omega((x-x_0)(x-x_0)^*)^{1/2}\); for the second it is \(\omega((y-y_0)^*(y-y_0))^{1/2}\). Both are controlled by the sharp errors. The scalar product of the means changes by at most \(\varepsilon(\|x\|+\|y\|)\). Thus for \(n>m\),
\[
 \begin{aligned}
 &|\omega(\alpha_n(x)y)-\omega(x)\omega(y)|\\
 &\hspace{1em}\le2\varepsilon(\|x\|+\|y\|).
 \end{aligned}
\tag{3.4}
\]
Letting \(\varepsilon\) tend to zero proves (3.1). \(\square\)

**Theorem 3.2.** We have
\[
 F'\cap R_\lambda=\mathbb C1.
\tag{3.5}
\]
Consequently \(R_\lambda\) is a factor, and \(F\) is an approximately finite factor of type \({\rm II}_1\).

*Proof.* If \(x\in F'\cap R_\lambda\), every \(u_{g_n}\in F\) commutes with \(x\), so \(\alpha_n(x)=x\). Lemma 3.1 gives
\[
 \omega(xy)=\omega(x)\omega(y)
 \qquad(y\in R_\lambda).
\tag{3.6}
\]
Put \(z=x-\omega(x)1\) and use \(y=z^*\). Then \(\omega(zz^*)=0\), so faithfulness gives \(z=0\). This proves (3.5).

Both \(Z(R_\lambda)\) and \(Z(F)\) are contained in \(F'\cap R_\lambda\). They are therefore scalar, so both algebras are factors. Proposition 2.2 gives a faithful tracial state and a finite-dimensional filtration of \(F\). Finally, \(F\) contains all diagonal matrices in every \(A_n\), including \(2^n\) nonzero mutually orthogonal projections. It is infinite dimensional, so this finite factor has type \({\rm II}_1\). \(\square\)

This argument depends on the identical coordinate densities. A permutation of unequal densities need not lie in the centralizer of the product state.

## 4. The state spectrum determines the type

For a factor \(M\), Connes's invariant is
\[
 S(M)=\bigcap_\varphi\operatorname{Sp}(\Delta_\varphi),
\tag{4.1}
\]
where \(\varphi\) ranges over the faithful normal semifinite weights. A factor is of type \({\rm III}_\lambda\), \(0<\lambda<1\), when this invariant is \(\{0\}\cup\lambda^{\mathbb Z}\). The intersection over weights is essential: the spectrum of one state is not in general an invariant of the algebra.

The spectral theorem we use says that if \(M\) is a factor and the centralizer of a faithful normal semifinite weight \(\varphi\) is a factor, then
\[
 S(M)=\operatorname{Sp}(\Delta_\varphi).
\tag{4.2}
\]
*Reference:* [Connes, Corollary 3.2.7(a), pp. 192–193]. [Theorem PC8.1](../foundations/crossed-product-and-injective-core-foundations.md#pc8) supplies the programme proof at full faithful normal semifinite weight scope. It proves fixed-corner spectral equality from factoriality, applies MG-0–MG-3 to compare all weights, and treats zero by closedness of their spectra. Its stated modular and normal-filter foundations remain explicit. The factorial-centralizer hypothesis for the product state is proved here.

**Theorem 4.1.** The algebra \(R_\lambda\) is an approximately finite factor of type \({\rm III}_\lambda\), and
\[
 S(R_\lambda)=\{0\}\cup\lambda^{\mathbb Z}.
\tag{4.3}
\]

*Proof.* Proposition 1.1 supplies the faithful normal state and approximate finite dimensionality. Theorem 3.2 supplies factoriality of both the algebra and the centralizer. Thus (4.2) applies, and Proposition 2.1 gives (4.3).

One can also keep track of zero separately. The central fixed-corner form of the spectral theorem gives the positive part \(\lambda^{\mathbb Z}\). Because \(\lambda^n\to0\) and \(S(R_\lambda)\) is closed, zero belongs to the invariant. The reverse inclusion already follows by including \(\omega\) among the weights in (4.1). No prior assumption that the algebra has type III is needed. \(\square\)

In particular, the period in (2.6) does not establish the type on its own. The centralizer calculation makes that periodic spectrum survive the weight intersection.

**Corollary 4.2.** If \(0<\lambda,\mu<1\), then \(R_\lambda\cong R_\mu\) implies \(\lambda=\mu\).

*Proof.* Isomorphisms preserve \(S\), so \(\lambda^{\mathbb Z}=\mu^{\mathbb Z}\). The greatest member of \(\lambda^{\mathbb Z}\) strictly below one is \(\lambda\), and likewise for \(\mu\). They must agree. \(\square\)

## 5. A diagonal algebra and finite coordinate flips

Let
\[
 \begin{gathered}
 X=\{0,1\}^{\mathbb N},\\
 \mu=\bigotimes_{j\ge1}(a\delta_0+b\delta_1),\\
 G=\bigoplus_{j\ge1}\mathbb Z/2\mathbb Z.
 \end{gathered}
\tag{5.1}
\]
The group acts by flipping the coordinates in the finite support of \(g\). The derivative convention is
\((\mu\circ g)(A)=\mu(gA)\); here \(g^{-1}=g\).

**Proposition 5.1.** This action is nonsingular, free and ergodic. If \(J=\operatorname{supp}(g)\), then
\[
 \frac{d(\mu\circ g)}{d\mu}(x)
 =\lambda^{\sum_{j\in J}(1-2x_j)}.
\tag{5.2}
\]
Its orbit relation is an increasing union of finite equivalence relations.

*Proof.* On a cylinder containing \(J\), the probability ratio is the product of \(b/a=\lambda\) for each flipped zero and \(a/b=\lambda^{-1}\) for each flipped one. The tail probabilities cancel. This proves (5.2). The derivative lies between \(\lambda^{|J|}\) and \(\lambda^{-|J|}\), so the transformed measure is equivalent to \(\mu\). If \(g\ne0\), at least one coordinate changes at every point. Thus the action is free everywhere.

Let \(f\in L^\infty(X,\mu)\) be invariant modulo null sets under all finite flips. Fix \(m\). There are only finitely many flips on the first \(m\) coordinates, and every one of the \(2^m\) finite atoms has positive probability. Fubini's theorem therefore makes \(f\) constant on almost every finite fiber over the tail after \(m\). Hence \(f\) is measurable with respect to that tail. Independence gives
\[
 \mathbb E_\mu(f\mid x_1,\ldots,x_m)=\int_X f\,d\mu.
\tag{5.3}
\]
The increasing finite-coordinate sigma algebras generate the whole measurable space. Their conditional expectations converge to \(f\) in \(L^2\), so \(f\) is constant. This proves ergodicity.

Let \(G_m\) consist of flips on the first \(m\) coordinates. Every \(G_m\)-orbit has \(2^m\) points. These orbit relations increase, and every element of \(G\) belongs to some \(G_m\). Their union is the full orbit relation. \(\square\)

Let \(D_n\) be the diagonal algebra in \(A_n\), and put \(D=(\bigcup_nD_n)''\). Its product state identifies
\[
 (D,\omega|_D)\cong(L^\infty(X,\mu),\mu).
\tag{5.4}
\]
To prove the normal identification, send each diagonal projection indexed by a binary word to its cylinder indicator. This gives compatible bijective unital *-algebra maps from the finite diagonal algebras to the finite-coordinate function algebras. Their union preserves the product probabilities and hence the two faithful tracial states. The first union is ultraweakly dense in \(D\) by definition; the cylinder functions are ultraweakly dense in \(L^\infty(X,\mu)\), since they generate the product sigma algebra. TF3 therefore extends the union map to a state-preserving normal *-isomorphism with normal inverse, giving (5.4). This supplies the normal extension, in addition to agreement on the finite cylinders. The measure is nonatomic: every cylinder of length \(n\) has probability at most \(a^n\), which tends to zero.

Here is a direct construction of the diagonal conditional expectation. For
\(z=(z_j)\in K=\mathbb T^{\mathbb N}\), conjugate each coordinate by
\(\operatorname{diag}(1,z_j)\). On \(H_0\) this conjugation is a unitary fixing \(\xi_0\). Its infinite product defines a unitary fixing \(\xi\), and finite-excitation vectors show that the representation of \(K\) is strongly continuous. It gives a normal action \(\gamma\) on \(R_\lambda\) preserving \(\omega\).

Average over the normalized Haar measure of \(K\):
\[
 E_D(x)=\int_K\gamma_z(x)\,dz.
\tag{5.5}
\]
As in (2.10), this is a faithful normal state-preserving conditional expectation onto the fixed algebra. On \(A_n\) the average removes every off-diagonal entry and has range \(D_n\). A bounded local sharp approximation of a fixed element remains an approximation after averaging, by the same Kadison inequality as (2.11). Thus the fixed algebra is exactly \(D\), justifying the notation in (5.5).

The algebra \(D\) is also maximal abelian. An element commuting with \(D\) commutes with all finite-coordinate diagonal phase unitaries, so it is fixed by their conjugations. The finite-support elements are dense in \(K\); continuity then makes the element fixed by all \(\gamma_z\), and hence a member of \(D\).

In coordinate \(j\), let
\[
 \begin{gathered}
 u_j=e_{01}^{(j)}+e_{10}^{(j)},\\
 u_g=\prod_{j\in\operatorname{supp}(g)}u_j.
 \end{gathered}
\tag{5.6}
\]
These commuting involutions give a unitary representation of \(G\). They normalize \(D\), with
\[
 u_g f u_g^*=f\circ g^{-1},\qquad f\in D.
\tag{5.7}
\]
If \(g\ne0\), averaging at one flipped coordinate gives zero, so
\[
 E_D(u_g)=0\qquad(g\ne0).
\tag{5.8}
\]
This is an algebra-valued expectation statement.

**Theorem 5.2.** In the covariance convention (5.7),
\[
 R_\lambda\cong L^\infty(X,\mu)\rtimes G.
\tag{5.9}
\]
The diagonal is maximal abelian, has a faithful normal conditional expectation, and its normalizing unitaries generate \(R_\lambda\).

*Proof.* We have established the faithful normal expectation, the group representation, covariance and (5.8). The diagonal projections and \(u_j\) generate the \(j\)-th copy of \(M_2\), because
\[
 \begin{aligned}
 e_{00}^{(j)}u_j&=e_{01}^{(j)},\\
 e_{11}^{(j)}u_j&=e_{10}^{(j)}.
 \end{aligned}
\tag{5.10}
\]
Thus \(D\) and the \(u_g\) generate the entire algebra. Theorem PC2.1 of the linked crossed-product companion now applies with \(B=R_\lambda\), \(Q=D\), \(\chi=\omega|_D\), \(F=E_D\) and \(v_g=u_g\). Its proof identifies the coefficient *-algebras by the faithful states \(\chi\circ F\) and the corresponding canonical expectation, then extends the resulting isometry to their GNS Hilbert spaces. Conjugation by that onto unitary gives the normal isomorphism (5.9), with exactly the specified images of functions and group unitaries. This uses the faithful normal GNS and image arguments in Lemma 3A.3 and Theorem 3.1 of the bounded-topology lesson; no trace on \(R_\lambda\) is asserted. The remaining assertions were proved above. \(\square\)

Consequently the binary action has a factor of type \({\rm III}_\lambda\) as its associated crossed product. To call the measured orbit relation itself type \({\rm III}_\lambda\), we use the general relation–factor type correspondence: for a free ergodic countable nonsingular action on a standard measure space, the relation and its associated factor have the same type and the same type-III parameter. With that prerequisite, Proposition 5.1 and Theorems 4.1 and 5.2 give an approximately finite ergodic relation of type \({\rm III}_\lambda\). The classification of arbitrary measured relations requires further groupoid results.

## 6. Applying the uniqueness theorem

[Theorem PC6.1 in the crossed-product companion](../foundations/crossed-product-and-injective-core-foundations.md#pc6) has a stronger hypothesis range than we need: every injective factor of type \({\rm III}_\lambda\) with separable predual is isomorphic to \(R_\lambda\). We use that theorem with its discrete-decomposition and automorphism prerequisites.

The discrete-decomposition theorem is needed in the following precise form. For a factor \(M\) of type \({\rm III}_\lambda\) with separable predual, there are a type \({\rm II}_\infty\) factor \(N\) with separable predual, a faithful normal semifinite trace \(\tau\), and an automorphism \(\theta\) such that
\[
 \begin{gathered}
 M\cong N\rtimes_\theta\mathbb Z,\\
 \tau\circ\theta=\lambda\tau.
 \end{gathered}
\tag{6.1}
\]
With the crossed-product unitary chosen to satisfy \(UxU^*=\theta(x)\), the dual weight has \(\sigma_t(U)=\lambda^{it}U\). Replacing \(U\) by \(U^*\) replaces \(\theta\) by \(\theta^{-1}\) and the trace multiplier by \(\lambda^{-1}\). We choose (6.1) throughout. [Discrete decomposition, DD-0–DD-5](../../OA-FLOW/OA-FLOW-DD.html#oa-flow.dd.0), supplies this precise presentation, including the normal expectation, the onto regular representation, and the same multiplier. Its modular and spectral prerequisite chain is separate from the local construction here.

The crossed-product companion proves that approximately finite algebras are injective and that an injective type \({\rm II}_\infty\) factor with separable predual is
\(R\overline\otimes B(\ell^2)\). Its PC5 proof uses Lemma PC5.1 for crossed products under conjugacy and inner perturbation, and Lemma PC5.2 for inheritance of injectivity by the expected core. The inner-perturbation step is algebra-valued: replacing \(U\) by \(vU\) leaves every nonzero Fourier coefficient expectation zero. Theorem PC4.3 identifies the injective semifinite core through a finite injective corner and countable amplification. [Theorems PC9.1–PC9.2](../foundations/crossed-product-and-injective-core-foundations.md#pc9) prove that the norm-one projections used in these arguments are completely positive and bimodular and give the representation-independent injectivity criterion. The exact commutant theorem and its standard-pair foundations are identified there. [Theorem PC10.1](../foundations/crossed-product-and-injective-core-foundations.md#pc10) proves the invariant-state finite classification through finite densities, trace-preserving matrix maps, balanced couplings and dyadic uniqueness. [Theorem PC11.1 and Corollary PC11.2](../foundations/crossed-product-and-injective-core-foundations.md#pc11) supply its tracial quotient, normal constant embedding, bounded expectations and unitary lifting with arbitrary center and without a separability assumption. [TF2–TF3 and TF5–TF6 of the tensor companion](../foundations/normal-tensor-and-tracial-product-foundations.md#tf5) give the tracial GNS identification and normal tensor maps in arbitrary faithful normal representations. The modular foundations retain their stated scope. The remaining automorphism input says that two automorphisms of this hyperfinite semifinite factor with trace multiplier \(\lambda\) are outer conjugate. [Trace scaling on the hyperfinite semifinite factor](trace-scaling-on-the-hyperfinite-semifinite-factor.md) proves the stronger conjugacy assertion under its stated prerequisites.

**Corollary 6.1.** With these prerequisites, every approximately finite factor of type \({\rm III}_\lambda\) with separable predual is isomorphic to \(R_\lambda\).

*Proof.* The approximately finite factor is injective, so it satisfies the hypotheses of the cited Theorem PC6.1. The Powers model in that theorem uses exactly the density (0.1); Theorem 4.1 verifies its type and Proposition 1.1 verifies its separable predual. The discrete-decomposition normalization is exactly (6.1), and the required same-multiplier outer-conjugacy assertion is provided by the trace-scaling theorem. Thus the cited uniqueness theorem applies with the same \(\lambda\) and gives the required isomorphism. \(\square\)

This explains the two roles of the finite and infinite centralizers. The product state's centralizer is finite and supplies the spectral calculation. A discrete decomposition uses an infinite semifinite core and supplies the trace-scaling automorphism used in uniqueness.

## 7. Exercises with complete solutions

**Exercise 7.1 (basic: block sizes and block probabilities).** Prove
\(\dim F_n=\binom{2n}{n}\). For \(n=3\), \(\lambda=1/3\), find the density value on each block and recover the four block probabilities in the table.

*Solution.* The algebra \(M_d\) has vector-space dimension \(d^2\). Thus (2.8) gives
\[
 \dim F_n=\sum_{k=0}^n\binom nk^2=\binom{2n}{n}.
\]
The last equality is the coefficient of \(t^n\) in
\((1+t)^n(1+t)^n\), since \(\binom n{n-k}=\binom nk\).
Here \(a=3/4\), \(b=1/4\). The density values are
\(27/64,9/64,3/64,1/64\) for \(k=0,1,2,3\). Multiplying by the block sizes \(1,3,3,1\) gives \(27/64,27/64,9/64,1/64\). The centralizer dimension is \(1+9+9+1=20=\binom63\).

**Exercise 7.2 (intermediate: all finite modular multiplicities).** On the Hilbert–Schmidt space of \(A_n\), show that the eigenvalue \(\lambda^r\) has multiplicity \(\binom{2n}{n+r}\) for \(-n\le r\le n\). List the multiplicities when \(n=2\), and explain why the infinite modular operator has zero in its spectrum but no zero eigenvector.

*Solution.* One coordinate contributes two basis vectors of exponent zero, one of exponent one, and one of exponent minus one. Hence the multiplicity-generating Laurent polynomial is
\[
 (2+z+z^{-1})^n=z^{-n}(1+z)^{2n}.
\]
The coefficient of \(z^r\) is \(\binom{2n}{n+r}\). For \(n=2\), the exponents \(-2,-1,0,1,2\) have multiplicities \(1,4,6,4,1\), summing to \(16=\dim M_4\).

In the infinite space, a normalized basis vector of eigenvalue \(\lambda^n\) gives \(\|\Delta_\omega v_n\|=\lambda^n\to0\), so \(\Delta_\omega\) has no bounded inverse and zero lies in its spectrum. An element of its kernel would have every coordinate zero in the complete eigenbasis, because all diagonal eigenvalues are positive. Therefore its kernel is zero.

**Exercise 7.3 (intermediate: a permutation changes correlations).** In four coordinates, let \(x=e_{01}^{(1)}\), \(y=e_{10}^{(1)}\), and let \(\alpha_2\) interchange the first two coordinates with the last two. Compute \(\omega(xy)\) and \(\omega(\alpha_2(x)y)\). Verify that the implementing permutation unitary belongs to the centralizer.

*Solution.* Since \(xy=e_{00}^{(1)}\), the first value is \(a\). The moved entry is \(\alpha_2(x)=e_{01}^{(3)}\). Product independence gives
\[
 \omega(e_{01}^{(3)}e_{10}^{(1)})
 =\omega_0(e_{01})\omega_0(e_{10})=0.
\]
The permutation matrix sends a binary basis word to a word with the same number of ones. The density \(h^{\otimes4}\) is scalar on each such set of words, so the matrix commutes with that density. Its modular action is consequently trivial, and it lies in \(F_4\).

**Exercise 7.4 (intermediate: the derivative integrates to one).** For a flip of the first two coordinates, list the derivative values on \(00,01,10,11\). Check their mean is one. Do the arithmetic explicitly for \(\lambda=1/3\).

*Solution.* Formula (5.2) gives \(\lambda^2,1,1,\lambda^{-2}\). Their probabilities are \(a^2,ab,ab,b^2\), so their mean is
\[
 a^2\lambda^2+2ab+b^2\lambda^{-2}
 =b^2+2ab+a^2=1.
\]
For \(\lambda=1/3\), the probabilities are \(9/16,3/16,3/16,1/16\) and the derivative values are \(1/9,1,1,9\). The weighted sum is \((1+3+3+9)/16=1\). The tail coordinates contribute a probability factor of one.

**Exercise 7.5 (advanced: why scalar means do not recognize a crossed product).** On \(B=Q=M_2(\mathbb C)\), take the faithful diagonal state with density \(h\), and let the nonidentity element of \(\mathbb Z/2\mathbb Z\) be represented by \(u=e_{01}+e_{10}\). Show that \(\omega_0(u)=0\) does not satisfy the expectation hypothesis of the recognition lemma. Show that \(Q\rtimes_{\operatorname{Ad}u}\mathbb Z/2\mathbb Z\) is not isomorphic to \(Q\).

*Solution.* The unitary \(u\) normalizes \(Q\), has square one, and has scalar mean zero. A conditional expectation from \(B\) onto \(Q=B\) is the identity, so it sends \(u\) to \(u\ne0\). Thus the expectation hypothesis fails.

In the crossed product let \(V\) be the group unitary. The element \(W=uV\) commutes with \(Q\), has square one, and commutes with \(V\), because \(\operatorname{Ad}u\) fixes \(u\). The crossed product is generated by \(Q\) and this central involution. Its canonical expectation sends \(W\) to zero, so both central projections \((1\pm W)/2\) are nonzero: if either were zero, \(W\) would be a scalar \(\pm1\), contradicting that expectation value. The crossed product therefore has nontrivial center, while \(M_2\) is a factor. They are not isomorphic. This is why (5.8) was proved for the diagonal conditional expectation.

**Exercise 7.6 (advanced: the equal-probability endpoint).** Repeat the product construction at \(\lambda=1\). Determine the modular operator, centralizer and factor type. Explain what changes in (2.8) and (2.6).

*Solution.* Now \(h=\tfrac12 I\), so the product state is tracial and every local modular operator is the identity. The complete finite-excitation basis therefore makes \(\Delta_\omega=1\), with spectrum \(\{1\}\). The entire algebra is its centralizer. The permutation mixing proof still gives factoriality, and the diagonal projections make the algebra infinite dimensional. It is an approximately finite factor with a faithful tracial state, hence the hyperfinite factor of type \({\rm II}_1\).

All finite density eigenvalues coincide, so their blocks merge: \(F_n=A_n\cong M_{2^n}\). Formula (2.8), which used \(\lambda\ne1\), does not apply. The modular action is the identity at every real time and has no least positive period; dividing by \(|\log\lambda|\) in (2.6) is therefore unavailable. The binary product measure is the fair measure, and the coordinate flips preserve it.

## References

[Connes] Alain Connes, *Une classification des facteurs de type III*, Annales scientifiques de l'École Normale Supérieure, series 4, 6 (1973), 133–252. [Open article](https://www.numdam.org/item/ASENS_1973_4_6_2_133_0/).

[Powers] Robert T. Powers, *Representations of uniformly hyperfinite algebras and their associated von Neumann rings*, Russian translation by A. G. Stepin, *Matematika* 13(4) (1969), 94–124. [Freely readable translation and original-publication record](https://www.mathnet.ru/eng/mat520). Originally published in *Annals of Mathematics* 86(1) (1967), 138–171, DOI 10.2307/1970364. Historical source for the family; the construction used in this lesson is credited to [Takesaki III].

[Takesaki II] Masamichi Takesaki, *Theory of Operator Algebras II*, Encyclopaedia of Mathematical Sciences 125, Springer, 2003. Modular background. [Publisher record](https://doi.org/10.1007/978-3-662-10451-4).

[Takesaki III] Masamichi Takesaki, *Theory of Operator Algebras III*, Encyclopaedia of Mathematical Sciences 127, Springer, 2003, XVIII.1.1–XVIII.1.4(i), pp. 297–300. Product construction, permutation centralizer argument, binary model and classification targets. [Publisher record](https://doi.org/10.1007/978-3-662-10453-8).
