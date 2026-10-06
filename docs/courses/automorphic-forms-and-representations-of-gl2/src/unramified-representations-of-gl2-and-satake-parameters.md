# Unramified representations of GL₂(F) and Satake parameters

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Author self-check complete. Public domain (CC0).*

A spherical vector records an irreducible local representation through two numbers: the eigenvalues of a nearest-neighbor Hecke operator and of a central translation. The Satake transform turns these into an unordered pair of nonzero complex numbers. We will identify the representation belonging to every pair, including the exceptional pairs for which the induced representation is reducible, and derive the precise comparison with a classical Fourier coefficient.

Let \(F\) be a nonarchimedean local field, \(\mathcal O\) its ring of integers, \(\varpi\) a uniformizer, and \(q=\#(\mathcal O/\varpi\mathcal O)\). Put
\[
G=\mathrm{GL}_2(F),\qquad K=\mathrm{GL}_2(\mathcal O),\qquad
\nu=|\cdot|,\qquad \nu(\varpi)=q^{-1}.
\]
Haar measure on \(G\) gives \(K\) volume one. Representations are smooth complex representations. An irreducible representation is **unramified** when its \(K\)-fixed space is nonzero. This definition does not require its central character to be trivial.

We use the normalized induction of Lesson 6:
\[
I(\mu_1,\mu_2)=
\left\{F:G\longrightarrow\mathbf C:
F\left(\begin{pmatrix}a&x\\0&d\end{pmatrix}g\right)
=|a/d|^{1/2}\mu_1(a)\mu_2(d)F(g)\right\},
\tag{0.1}
\]
with smooth right translation. Here the \(\mu_i\) are smooth quasicharacters of \(F^\times\). A quasicharacter is unramified if it is trivial on \(\mathcal O^\times\). Its value \(c\in\mathbf C^\times\) on \(\varpi\) determines it:
\[
\mu_c(\varpi^n u)=c^n\qquad(n\in\mathbf Z,\ u\in\mathcal O^\times).
\tag{0.2}
\]
No choice of a complex logarithm is needed.

## 1. The exact spherical algebra being imported

The local-lattice prerequisites supply the decompositions and the algebra:

- NT-ADL-11, Theorem 11.2 and Proposition 11.4, give Cartan decomposition and \(G=BK\), with \(B\) the upper triangular subgroup.
- NT-ADL-12, Theorems 12.2–12.4, give the commutative spherical convolution algebra
\[
\mathcal H(G,K)=\mathbf C[T,R,R^{-1}],
\quad
T=1_{K\operatorname{diag}(\varpi,1)K},
\quad R=1_{\varpi I_2K},
\tag{1.1}
\]
and its normalized Satake isomorphism
\[
\mathcal S:\mathcal H(G,K)
 \xrightarrow{\ \sim\ }
\mathbf C[X_1^{\pm1},X_2^{\pm1}]^{S_2},
\quad
\mathcal S(T)=q^{1/2}(X_1+X_2),
\quad
\mathcal S(R)=X_1X_2.
\tag{1.2}
\]

The normalization in that prerequisite is
\[
(\mathcal Sf)(t)=\delta_B(t)^{1/2}
 \int_F f\left(t\begin{pmatrix}1&u\\0&1\end{pmatrix}\right)\,du,
\qquad \operatorname{vol}(\mathcal O,du)=1,
\tag{1.3}
\]
viewed as a Laurent polynomial on the diagonal valuation lattice. For \(t=\operatorname{diag}(\varpi^a,\varpi^b)\),
\(\delta_B(t)^{1/2}=q^{(b-a)/2}\). The order \(tn(u)\) and the positive square root in (1.3) fix the powers of \(q\).

We do not repeat the proofs of (1.1)–(1.3). We will calculate the action of their generators on actual representation vectors. In particular, the trivial representation must have \(T\)-eigenvalue \(q+1\); Section 5 verifies this check.

## 2. Spherical vectors and their eigenvalues

**Theorem 2.1 — the spherical line in a principal series.**
\[
\dim I(\mu_1,\mu_2)^K=
\begin{cases}
1,&\mu_1,\mu_2\text{ unramified},\\
0,&\text{otherwise}.
\end{cases}
\tag{2.1}
\]

**Proof.** A right \(K\)-invariant function is constant on \(K\). Since \(G=BK\), its value at one and the transformation law (0.1) determine every value. Thus the fixed space has dimension at most one.

Suppose its value \(c\) at one is nonzero. For \(a,d\in\mathcal O^\times\), the diagonal matrix \(\operatorname{diag}(a,d)\) belongs to both \(B\) and \(K\). Right invariance and (0.1) give
\(c=\mu_1(a)\mu_2(d)c\), because \(|a/d|=1\). Taking \(d=1\) and then \(a=1\) makes each \(\mu_i\) trivial on \(\mathcal O^\times\).

Conversely, assume both are unramified. Define
\[
F_0(bk)=\delta_B(b)^{1/2}\mu_1(a_b)\mu_2(d_b),
\qquad F_0(1)=1.
\tag{2.2}
\]
If \(bk=b'k'\), then \(b'^{-1}b\in B\cap K\). Its two diagonal entries are units, so the multiplier on the right of (2.2) is one there. The definition is therefore independent of the decomposition. It satisfies (0.1), is right \(K\)-invariant and hence locally constant, and is nonzero. This proves existence and the asserted dimension. \(\square\)

Write
\[
\alpha=\mu_1(\varpi),\qquad \beta=\mu_2(\varpi).
\]

**Theorem 2.2 — the exact Hecke eigenvalues.** On \(\mathbf C F_0\),
\[
I(T)F_0=q^{1/2}(\alpha+\beta)F_0,\qquad
I(R)F_0=\alpha\beta F_0.
\tag{2.3}
\]
More generally, \(h\in\mathcal H(G,K)\) acts by \((\mathcal Sh)(\alpha,\beta)\).

**Proof.** The double coset for \(T\) has the following right cosets:
\[
K\begin{pmatrix}\varpi&0\\0&1\end{pmatrix}K=
\bigsqcup_{u\in\mathcal O/\varpi\mathcal O}
 \begin{pmatrix}\varpi&u\\0&1\end{pmatrix}K
\ \sqcup\
 \begin{pmatrix}1&0\\0&\varpi\end{pmatrix}K.
\tag{2.4}
\]
Here is a verification of completeness as well as distinctness. A right coset \(gK\) determines the lattice \(g\mathcal O^2\). A lattice in this double coset is precisely an index-\(q\) sublattice of \(\mathcal O^2\), by Cartan decomposition. Such lattices contain \(\varpi\mathcal O^2\) and correspond to the one-dimensional subspaces of the two-dimensional residue space. The first lattices in (2.4) reduce to the lines spanned by \((\bar u,1)\); the last reduces to the line spanned by \((1,0)\). These are all \(q+1\) lines, with no repetition.

Every right coset has volume one. Evaluate the convolution at one. Equation (0.1) gives
\[
F_0\left(\begin{pmatrix}\varpi&u\\0&1\end{pmatrix}\right)
=q^{-1/2}\alpha,\qquad
F_0\left(\begin{pmatrix}1&0\\0&\varpi\end{pmatrix}\right)
=q^{1/2}\beta.
\]
Consequently
\[
(I(T)F_0)(1)=q\,q^{-1/2}\alpha+q^{1/2}\beta
=q^{1/2}(\alpha+\beta).
\]
The output is \(K\)-fixed because the kernel is left \(K\)-invariant. Theorem 2.1 then identifies it as the first scalar multiple in (2.3).

The central double coset \(\varpi I_2K\) is a single right coset, also of volume one. Its central multiplier is \(\mu_1(\varpi)\mu_2(\varpi)\), giving the second formula. Finally (1.1) says that \(T,R,R^{-1}\) generate the algebra; (1.2) and the two computed eigenvalues therefore prove the formula for every \(h\). \(\square\)

The product \(\alpha\beta\) is also the value of the central character at \(\varpi\), since a scalar \(zI_2\) acts in (0.1) by \(\mu_1(z)\mu_2(z)\).

## 3. From a spherical character to its irreducible representation

We need to distinguish the full induced representation from its spherical constituent. We import the principal-series criterion already proved in Lesson 7, Theorem 4.2: \(I(\mu_1,\mu_2)\) is irreducible unless \(\mu_1/\mu_2=\nu^{\pm1}\). At either exceptional ratio it has the following two irreducible factors:
\[
0\longrightarrow\mathrm{St}_\chi
 \longrightarrow I(\chi\nu^{1/2},\chi\nu^{-1/2})
 \longrightarrow D_\chi\longrightarrow0,
\tag{3.1}
\]
\[
0\longrightarrow D_\chi
 \longrightarrow I(\chi\nu^{-1/2},\chi\nu^{1/2})
 \longrightarrow\mathrm{St}_\chi\longrightarrow0,
\quad D_\chi=\chi\circ\det.
\tag{3.2}
\]
In particular, every principal series has finite length.

**Lemma 3.1 — the unique spherical constituent.** An unramified principal series has exactly one irreducible constituent with nonzero \(K\)-invariants, counted with multiplicity. That constituent has a one-dimensional fixed space carrying the character in (2.3).

**Proof.** Compact averaging makes \(K\)-invariants exact. Explicitly, in a surjection of smooth representations, a lift \(v\) of a \(K\)-fixed vector can be replaced by
\(\int_K \pi(k)v\,dk\); its image is the original vector. The integral is a finite sum on each smooth vector. Injections and kernels commute with fixed spaces directly.

Apply this exact functor to a composition series of the principal series. The dimensions of the fixed spaces of its irreducible factors sum to one, by Theorem 2.1. Exactly one summand is one and all others are zero. The nonzero fixed-space map identifies that line with the line of the principal series, including its spherical Hecke action. \(\square\)

**Theorem 3.2 — unramified classification.** The assignment
\[
\pi\longmapsto\{\alpha,\beta\}
\tag{3.3}
\]
is a bijection from isomorphism classes of irreducible unramified representations of \(G\) to unordered pairs of nonzero complex numbers, with repetitions allowed. It is characterized by
\[
\begin{aligned}
T|_{\pi^K}&=q^{1/2}(\alpha+\beta),\\
R|_{\pi^K}&=\alpha\beta.
\end{aligned}
\tag{3.4}
\]
For the pair \(\{\alpha,\beta\}\), take \(\mu_\alpha,\mu_\beta\) from (0.2). If
\(\alpha/\beta\notin\{q,q^{-1}\}\), its representation is the entire irreducible \(I(\mu_\alpha,\mu_\beta)\). If \(\alpha/\beta\in\{q,q^{-1}\}\), it is \(D_\chi\), where
\[
\{\alpha,\beta\}=
\{\chi(\varpi)q^{1/2},\chi(\varpi)q^{-1/2}\}.
\tag{3.5}
\]
The latter \(\chi\) is unramified. No Steinberg representation is spherical.

**Proof.** Put \(\mathcal H=C_c^\infty(G)\) and \(e=1_K\). The smooth Hecke dictionary and simple-corner result of Lesson 5, Theorem 3.1, say that for a simple \(\mathcal H\)-module \(V\) with \(eV\ne0\), the corner \(eV\) is simple over \(e\mathcal He=\mathcal H(G,K)\), and it determines \(V\) uniquely up to isomorphism. This uniqueness does not require \(e\) to be a full idempotent.

An irreducible smooth \(G\)-representation is admissible by Lesson 6, Theorem 5.4, so \(V^K=eV\) is finite-dimensional. As the corner is commutative, it has a common eigenvector for \(T\) and \(R\): take an eigenspace of \(T\), preserved by \(R\), and then an eigenvector of \(R\) in it. Since \(R\) is invertible, that eigenvalue is nonzero. Their common line is stable under the whole algebra (1.1); simplicity makes it all of \(V^K\). Let \(t,r\) be its eigenvalues, with \(r\ne0\). The two roots of
\[
Z^2-q^{-1/2}tZ+r=0
\tag{3.6}
\]
are nonzero, and their unordered pair is unique.

Conversely, for any such pair form \(I(\mu_\alpha,\mu_\beta)\) and take its unique spherical constituent \(J(\alpha,\beta)\) from Lemma 3.1. Theorem 2.2 identifies its corner character with the character having values \(t=q^{1/2}(\alpha+\beta)\), \(r=\alpha\beta\). The simple-corner uniqueness gives
\(V\simeq J(\alpha,\beta)\) for the original representation \(V\). It also proves that two resulting representations are isomorphic precisely when their pairs agree: an isomorphism identifies the two corner characters, while equal characters have the same unique simple extension. This proves both directions of the bijection and independence of the ordering.

For unramified quasicharacters, equality of their ratio with \(\nu\) or \(\nu^{-1}\) is equivalent to equality at \(\varpi\), namely \(\alpha/\beta=q^{-1}\) or \(q\). Lesson 7's criterion therefore proves the stated irreducibility condition.

At an exceptional pair, order the roots so that \(\alpha/\beta=q^{-1}\), and set \(c=\alpha q^{1/2}=\beta q^{-1/2}\). This uniquely defines the unramified \(\chi\) with \(\chi(\varpi)=c\) and proves (3.5). The character \(D_\chi\) is trivial on \(K\), since \(\det K=\mathcal O^\times\). Thus its fixed space has dimension one. Exactness applied to (3.1) or (3.2) and Theorem 2.1 forces
\(\mathrm{St}_\chi^K=0\), proving that \(D_\chi\) is the unique spherical factor there.

For a ramified \(\chi\), Theorem 2.1 gives zero fixed space in both induced representations in (3.1)–(3.2); exactness forces zero in \(\mathrm{St}_\chi\) as well. Hence no Steinberg twist is spherical. \(\square\)

There are two useful consequences.

First, every spherical irreducible has nonzero Jacquet module. In the principal-series case this follows from Lesson 6, Theorem 4.1; for \(D_\chi\) the ordinary Jacquet module is the character itself, because the unipotent acts trivially. Its normalized torus character is
\((\chi\nu^{-1/2})\otimes(\chi\nu^{1/2})\).
Lesson 6, Theorems 3.1 and 5.1, then recover an embedding into a principal series by Frobenius reciprocity. The classification above supplies unramified inducing characters and also excludes supercuspidals from the spherical class. We used the simple corner to establish this exclusion, rather than assuming that a Jacquet module is nonzero merely because a vector is spherical.

Second, the pair corresponds to the semisimple conjugacy class of
\[
s(\pi)=\begin{pmatrix}\alpha&0\\0&\beta\end{pmatrix}
\quad\text{in }\mathrm{GL}_2(\mathbf C).
\tag{3.7}
\]
A semisimple complex matrix is diagonalizable, and two such matrices are conjugate exactly when their eigenvalue pairs agree with multiplicity. Thus (3.7) is an elementary restatement of (3.3). This describes the unramified Satake parameter; it does not use the ramified local Langlands correspondence.

The associated standard Euler factor is
\[
L(s,\pi)
=\det(1-s(\pi)q^{-s})^{-1}
=\frac1{(1-\alpha q^{-s})(1-\beta q^{-s})}.
\tag{3.8}
\]
For an irreducible principal series, this agrees with the local zeta factor proved in Lesson 9, Theorem 1.1. For \(D_\chi\), its agreement with the matrix zeta definition is the explicitly stated input in Lesson 9, Section 8:
\[
L(s,D_\chi)=L(s,\chi\nu^{1/2})L(s,\chi\nu^{-1/2}).
\]
Formula (3.5) gives exactly (3.8). The generic special representation has instead the single factor
\(L(s,\mathrm{St}_\chi)=(1-\chi(\varpi)q^{-s-1/2})^{-1}\) when \(\chi\) is unramified; it has no spherical line and is not the representation assigned to the exceptional pair.

## 4. Classical coefficients and the two normalizations

Let \(f=\sum_{n\ge1}a_n e^{2\pi inz}\) be a normalized holomorphic cuspidal newform of weight \(k\), level \(N\), and Dirichlet character \(\chi\). Use the lift \(\phi_f\) of Lesson 2, with its positive real central character trivial. Its finite compact character uses \(\overline\chi\) on the lower-right entry. Nevertheless, at \(p\nmid N\) its central character satisfies
\[
\omega_p(p)=\chi(p)
\tag{4.1}
\]
by Lesson 2, Proposition 1.1.

One can establish the good-prime dictionary before proving the uniqueness of the global representation associated with a newform. Indeed, the nonzero cuspidal lift has a nonzero projection onto at least one irreducible Hilbert constituent by Lesson 3 and Lesson 4. Such projections commute with right translation and bounded finite Hecke sums, so they retain the \(K_p\)-invariance, central character and good-prime eigenvalues of the lift. The tensor-product theorem of Lesson 12, Theorem 6.1, supplies the local factor \(\pi_p\) of each such constituent. At \(p\nmid N\) it is spherical. All the constituents with nonzero projection have the same good-prime parameters by the following computation. The separate global newform and multiplicity-one assertion remains the subject of Lesson 15.

**Theorem 4.1 — the classical dictionary.** In the normalization above, the pair of \(\pi_p\), for \(p\nmid N\), satisfies
\[
a_p=p^{(k-1)/2}(\alpha_p+\beta_p),
\qquad
\alpha_p\beta_p=\chi(p).
\tag{4.2}
\]

**Proof.** Denote the classical operator by \(T_p^{\mathrm{cl}}\) and the spherical convolution at \(p\) by \(\mathcal H_p\), to avoid identifying two differently scaled operators. The exact comparison of Lesson 2, Section 5, is
\[
\phi_{T_p^{\mathrm{cl}}f}
=p^{k/2-1}\mathcal H_p\phi_f.
\tag{4.3}
\]
Since \(T_p^{\mathrm{cl}}f=a_pf\), the convolution eigenvalue is \(a_pp^{1-k/2}\). It remains this value on a nonzero constituent projection. Theorem 2.2 gives its other expression
\(p^{1/2}(\alpha_p+\beta_p)\). Equating the two and multiplying by \(p^{k/2-1}\) proves the first equality of (4.2). The central operator \(R_p\) acts by \(\omega_p(p)\). Equations (2.3) and (4.1) prove the second. \(\square\)

Define the **arithmetic parameters** by
\[
A_p=p^{(k-1)/2}\alpha_p,\qquad
B_p=p^{(k-1)/2}\beta_p.
\]
They are the two roots, with multiplicity, of
\[
X^2-a_pX+\chi(p)p^{k-1},
\qquad A_pB_p=\chi(p)p^{k-1}.
\tag{4.4}
\]
Our \(\alpha_p,\beta_p\) are the parameters in **unitary normalization**. This phrase specifies the scaling; it is not a claim that every unitary local representation has both parameters of modulus one. With a classical complex variable \(w\), the good Euler factors obey
\[
L_p^{\mathrm{cl}}(w,f)
=\frac1{1-a_pp^{-w}+\chi(p)p^{k-1-2w}}
=L\left(w-\frac{k-1}{2},\pi_p\right).
\tag{4.5}
\]
The translation of the variable as well as the rescaling of the roots is necessary.

**Ramanujan at an unramified place.** For a unitary cuspidal automorphic representation of \(\mathrm{GL}_2\), the unramified local Ramanujan conjecture is
\[
|\alpha_v|=|\beta_v|=1.
\tag{4.6}
\]
The tempered classification proved in Lesson 7, Theorem 7.2, makes this equivalent to temperedness of that spherical factor: the spherical tempered cases are precisely principal series induced from unitary unramified characters.

For holomorphic primitive forms of weight \(k\ge2\), Deligne's purity theorem supplies
\[
|\sigma(A_p)|=|\sigma(B_p)|=p^{(k-1)/2}
\quad(p\nmid N)
\tag{4.7}
\]
under every complex embedding of their splitting field. We import the precise assertion from LG-GAL-12, Section 4, equation (22), and Theorem 4.3; its primary source is Deligne, *La conjecture de Weil. I*, Theorem (8.2), p. 302. Dividing by the positive real scale proves (4.6), and the triangle inequality gives
\[
|\sigma(a_p)|\le2p^{(k-1)/2}.
\tag{4.8}
\]
The deep purity theorem is stated here, not proved. Its use gives both root moduli, which is stronger than an isolated upper bound on their sum when the character is arbitrary.

## 5. Computed examples and a unitarity distinction

**Example 5.1 — the trivial and determinant representations.** On \(D_\eta=\eta\circ\det\), for an unramified \(\eta\) with \(c=\eta(\varpi)\), every coset in (2.4) acts by \(c\). Therefore
\[
T=(q+1)c,\qquad R=c^2.
\]
Its polynomial (3.6) factors as
\[
Z^2-(q^{1/2}+q^{-1/2})cZ+c^2
=(Z-cq^{1/2})(Z-cq^{-1/2}).
\tag{5.1}
\]
Thus its Satake parameter is \(\{cq^{1/2},cq^{-1/2}\}\). For the trivial representation \(c=1\), this proves
\[
q^{1/2}(q^{1/2}+q^{-1/2})=q+1,
\]
checking the normalization against the mass of the actual double coset. Its Euler factor is
\((1-q^{1/2-s})^{-1}(1-q^{-1/2-s})^{-1}\).

The trivial representation is unitary, while neither root in (5.1) has modulus one when \(c=1\). Infinite-dimensional examples also exist: the complementary series
\[
I(\nu^r,\nu^{-r}),\qquad 0<r<\tfrac12,
\]
is irreducible and unitarizable by Lesson 7, Theorem 7.1. Its pair is \(\{q^{-r},q^r\}\), with product one and unequal moduli. At \(r=1/2\) the induction becomes reducible and its spherical constituent is the trivial representation. Unitarity alone therefore does not prove (4.6). The cuspidal Ramanujan assertion imposes the stronger tempered condition.

**Example 5.2 — the discriminant form at two primes.** For the level-one weight-twelve form
\[
\Delta(z)=q_z\prod_{n\ge1}(1-q_z^n)^{24}
=\sum_{n\ge1}\tau(n)q_z^n,\qquad q_z=e^{2\pi iz},
\]
the first needed coefficients are \(\tau(2)=-24\), \(\tau(3)=252\). They can be computed without approximation: through degree two after removing the leading \(q_z\), the product is
\[
(1-q_z)^{24}(1-q_z^2)^{24}
=1-24q_z+\left(\binom{24}{2}-24\right)q_z^2+O(q_z^3)
=1-24q_z+252q_z^2+O(q_z^3).
\]
The general dictionary gives
\[
\alpha_p+\beta_p=\tau(p)p^{-11/2},\qquad
\alpha_p\beta_p=1,\qquad
\mathcal H_p=\tau(p)p^{-5}.
\tag{5.2}
\]
The constituent of \(\Delta\) was identified in Lesson 3, Section 6, and its tensor factorization was computed in Lesson 12, Section 7.

At \(p=2\),
\[
\mathcal H_2=-\frac34,\qquad
\{\alpha_2,\beta_2\}
=\left\{\frac{-3+i\sqrt{119}}{8\sqrt2},
             \frac{-3-i\sqrt{119}}{8\sqrt2}\right\}.
\tag{5.3}
\]
The sum is \(-3/(4\sqrt2)=-24/2^{11/2}\), and the product and each squared modulus are
\((9+119)/128=1\). The arithmetic roots are \(-12\pm4i\sqrt{119}\), whose sum is \(-24\) and product \(2048=2^{11}\).

At \(p=3\),
\[
\mathcal H_3=\frac{28}{27},\qquad
\{\alpha_3,\beta_3\}
=\left\{\frac{14+i\sqrt{1991}}{27\sqrt3},
             \frac{14-i\sqrt{1991}}{27\sqrt3}\right\}.
\tag{5.4}
\]
Their sum is \(28/(27\sqrt3)=252/3^{11/2}\), and each squared modulus is
\((196+1991)/(729\cdot3)=1\). Their arithmetic roots are
\(126\pm9i\sqrt{1991}\), with sum \(252\) and product
\(15876+161271=177147=3^{11}\). Both local principal series are irreducible, since the ratio of their two roots has modulus one and cannot equal \(p\) or \(p^{-1}\).

The two factors are consequently
\[
\begin{aligned}
L(s,\pi_2)&=
\frac1{1+\dfrac{3}{4\sqrt2}2^{-s}+2^{-2s}},\\
L(s,\pi_3)&=
\frac1{1-\dfrac{28}{27\sqrt3}3^{-s}+3^{-2s}}.
\end{aligned}
\tag{5.5}
\]
The exact quadratic computations prove the root-modulus assertion at these two primes. Deligne's theorem supplies it at every prime, giving
\(|\tau(p)|\le2p^{11/2}\) and temperedness of every finite factor of this level-one representation.

## 6. Exercises with complete solutions

**Exercise 6.1 — determinant twists (easy).** For an unramified \(\eta\), find the Satake parameter and standard Euler factor of \(\eta\circ\det\), including the trivial case.

**Solution 6.1.** Set \(c=\eta(\varpi)\ne0\). Its \(K\)-fixed space is its whole one-dimensional space. The determinant of every representative in (2.4) has valuation one, so each acts by \(c\); the central representative \(\varpi I_2\) acts by \(c^2\). Thus \(t=(q+1)c\), \(r=c^2\). The unique unordered roots of (3.6) are \(cq^{1/2}\), \(cq^{-1/2}\), by the factorization (5.1). Formula (3.8), with its nongeneric matrix interpretation, gives
\[
L(s,\eta\circ\det)
=(1-cq^{1/2-s})^{-1}(1-cq^{-1/2-s})^{-1}.
\]
At \(c=1\), \(T\) has eigenvalue \(q+1\), \(R\) has eigenvalue one, and this is the factor of the trivial representation. \(\square\)

**Exercise 6.2 — uniqueness and the obstruction (medium).** Prove that a spherical vector in \(I(\mu_1,\mu_2)\) is unique up to scalar, and determine exactly when a nonzero one exists.

**Solution 6.2.** Its restriction to \(K\) is constant, equal to its value at one. Iwasawa decomposition and (0.1) then determine the function on all of \(G\), proving uniqueness. If that value is nonzero, comparison at \(\operatorname{diag}(u,1)\) and \(\operatorname{diag}(1,u)\), for every unit \(u\), forces \(\mu_1(u)=\mu_2(u)=1\). If the value is zero, the whole function is zero.

Conversely, triviality on units makes the inducing multiplier trivial on \(B\cap K\). Hence the formula (2.2) is independent of the choice of \(bk\), satisfies the inducing law, and is fixed on the right by \(K\). It has value one at the identity. Thus the fixed space is precisely \(\mathbf C F_0\) in the unramified case and zero otherwise. \(\square\)

**Exercise 6.3 — all \(q+1\) cosets (medium).** Derive the \(T\)-eigenvalue by an actual right-coset sum, with the square-root factors visible.

**Solution 6.3.** The lattices of index \(q\) in \(\mathcal O^2\) correspond to residue lines. The lines \((\bar u,1)\) give the \(q\) representatives
\(g_u=\begin{pmatrix}\varpi&u\\0&1\end{pmatrix}\), and the line \((1,0)\) gives
\(g_\infty=\operatorname{diag}(1,\varpi)\). This proves both the count and decomposition (2.4). Their cosets all have volume one under the fixed Haar measure.

For the normalized vector \(F_0\), the inducing law gives
\(F_0(g_u)=q^{-1/2}\mu_1(\varpi)\), independently of \(u\), and
\(F_0(g_\infty)=q^{1/2}\mu_2(\varpi)\). Summing these \(q+1\) values gives
\[
q\,q^{-1/2}\alpha+q^{1/2}\beta
=q^{1/2}(\alpha+\beta).
\]
The convolution lies on the unique fixed line and \(F_0(1)=1\), so this is its eigenvalue. Omitting the modulus multiplier would replace the first computation by \(q\alpha+\beta\), which is a different induction convention. \(\square\)

**Exercise 6.4 — derive the classical constant (hard).** Derive (4.2) from the classical and adelic operators, and verify the change of Euler-factor variable.

**Solution 6.4.** On the positive real section of the lift, the adelic cosets from (2.4), after rational left multiplication by their inverses, give the classical function
\[
p^{-k/2}\sum_{b=0}^{p-1}f\left(\frac{z-b}{p}\right)
+\chi(p)p^{k/2}f(pz).
\tag{6.1}
\]
These are exactly the evaluated cosets of Lesson 2, equation (5.5). The first representatives have no finite character multiplier. The last has lower-right entry \(p^{-1}\) at the other finite places, yielding
\(\overline{\chi(p^{-1})}=\chi(p)\).

The classical operator in that lesson is
\[
T_p^{\mathrm{cl}}f(z)
=\frac1p\sum_{b=0}^{p-1}f\left(\frac{z+b}{p}\right)
+\chi(p)p^{k-1}f(pz).
\]
Residues \(b\) and \(-b\) give the same sum because \(f(z+1)=f(z)\). Multiplication of (6.1) by \(p^{k/2-1}\) gives coefficient \(p^{-1}\) in its first term and \(p^{k-1}\) in its second. Thus the same multiplier works for the entire operator, proving (4.3). A normalized eigenform has classical eigenvalue \(a_p\), so
\(p^{1/2}(\alpha_p+\beta_p)=a_pp^{1-k/2}\). This yields the first formula in (4.2); the central-character computation (4.1) yields the second.

Finally substitute \(s=w-(k-1)/2\) in (3.8). Then
\(\alpha_pp^{-s}=A_pp^{-w}\) and
\(\beta_pp^{-s}=B_pp^{-w}\). Their sum and product in (4.4) turn the denominator into
\(1-a_pp^{-w}+\chi(p)p^{k-1-2w}\), proving (4.5) with its exact shift. \(\square\)

## 7. What this lesson does not prove

The four assigned representation and dictionary results have been proved above. The external inputs used in those proofs are the following.

- Cartan and Iwasawa decompositions are NT-ADL-11, Theorem 11.2 and Proposition 11.4. The spherical algebra and normalized Satake isomorphism are NT-ADL-12, Theorems 12.2–12.4. The latter already proves the normalization of (1.2); our coset computation checks its representation-theoretic interpretation.
- Smooth Hecke modules, compact averages and uniqueness of a simple module from a nonzero simple corner are Lesson 5, Propositions 1.1 and 2.1 and Theorem 3.1. Admissibility of irreducible smooth \(\mathrm{GL}_2(F)\)-representations is proved in Lesson 6, Theorem 5.4; Getz–Hahn, Theorem 5.3.4, is the original reference.
- The principal-series criterion, two exceptional sequences and Steinberg irreducibility are Lesson 7, Theorem 4.2. Normalized reciprocity, the principal Jacquet calculation and the noncuspidal embedding are Lesson 6, Theorems 3.1, 4.1 and 5.1. Their full proofs are not repeated here.
- The generic standard \(L\)-factor is Lesson 9, Theorem 1.1. The agreement of determinant-character factors with matrix zeta integrals is its Section 8, the stated Jacquet–Langlands §13 input. We have kept that distinction in (3.8).
- The classical lift, central-character convention and exact Hecke factor are Lesson 2, Proposition 1.1 and Section 5. The cuspidal Hilbert decomposition and constituent projections are Lessons 3–4; the tensor-product theorem is Lesson 12, Theorem 6.1. Good-prime equality of parameters does not itself prove the global uniqueness assertion assigned to Lesson 15.
- The unitary and tempered classifications are proved in Lesson 7, Theorems 7.1–7.2, with Tadić's Theorem D and §7.5 and Getz–Hahn, Theorem 8.4.5, retained as original authorities. Deligne's purity assertion is LG-GAL-12, Section 4, equation (22), based on Deligne 1974, Theorem (8.2). We prove its scaling and triangle-inequality deductions here.

The general Satake isomorphism for unramified reductive groups and the general construction of the dual group belong to the global Langlands prerequisite. Only the explicit \(\mathrm{GL}_2\) isomorphism is used in this lesson.

For comparison, Getz–Hahn, §§7.1–7.3 and 7.6, separates the Hecke character, its dual-group interpretation and its unique principal-series constituent. Gross, §§3 and 6–8, emphasizes the difference between the raw Satake parameter and further arithmetic normalizations; his weight-two Hecke normalization is not the weight-\(k\) scaling in (4.4). Satake, Chapter II, and Getz–Hahn, §7.5, treat the general unramified case and its spherical functions. Chenevier–Lannes, Chapter VI, §2, presents the transform through the normalized Jacquet action and representation ring. Our proofs use the previously established rank-two algebra, exact compact invariants and simple-corner uniqueness, with both reducible orders handled explicitly.

## References

- J. R. Getz and H. Hahn, *An Introduction to Automorphic Representations*, draft of 22 April 2022, §§7.1–7.3 and 7.5–7.6; Proposition 7.1.1, Corollary 7.2.2, Lemmas 7.6.3 and 7.6.5, Theorem 7.6.7 and Proposition 7.6.8. [Author's text page](https://sites.duke.edu/jgetz/graduate-text/).
- B. H. Gross, [*On the Satake isomorphism*](https://people.math.harvard.edu/~gross/preprints/sat.pdf), in A. J. Scholl and R. L. Taylor, eds., *Galois Representations in Arithmetic Algebraic Geometry*, LMS Lecture Note Series 254 (1998), pp. 223–237; §§3, 6, 7 and 8, especially formulas (3.14), (6.7) and (8.5)–(8.8).
- I. Satake, [*Theory of spherical functions on reductive algebraic groups over p-adic fields*](https://www.numdam.org/item/PMIHES_1963__18__5_0/), Publications Mathématiques de l'IHÉS **18** (1963), 5–69, Chapter II.
- G. Chenevier and J. Lannes, [*Formes automorphes et voisins de Kneser des réseaux de Niemeier*](https://arxiv.org/abs/1409.7616v2), arXiv:1409.7616v2, Chapter VI, §2, particularly Scholie 2.2 and Exemple 2.3.
- M. Tadić, [*Classification of unitary representations in irreducible representations of general linear group (non-Archimedean case)*](https://www.numdam.org/item/ASENS_1986_4_19_3_335_0/), Annales scientifiques de l'École normale supérieure **19** (1986), 335–382.
- P. Deligne, [*La conjecture de Weil. I*](https://www.numdam.org/item/PMIHES_1974__43__273_0/), Publications Mathématiques de l'IHÉS **43** (1974), Theorem (8.2), p. 302, used through the exact LG-GAL-12 prerequisite statement.
