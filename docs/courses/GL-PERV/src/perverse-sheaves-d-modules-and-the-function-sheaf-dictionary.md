# Perverse sheaves, D-modules and the function-sheaf dictionary

*Exposition reconstructed by GPT-6 Astra (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

There are several ways to extract numbers from a perverse sheaf. A Frobenius operator gives a trace. A normal slice gives an Euler characteristic. A resolution replaces a singular stalk by the cohomology of a fibre. We will calculate what each procedure preserves, and what it loses, before relating differential equations and Hecke correspondences to the same objects.

The elementary calculations use constructible complexes, [the perverse heart](the-perverse-t-structure.md), [intermediate extension](intermediate-extensions-and-intersection-complexes.md), the [small-map calculation](semismall-maps-and-small-resolutions.md), and the explicit disc diagrams of nearby and vanishing cycles. Each use retains the exact prerequisite obligations of those lessons. The freely accessible sources at the end supply the mathematical statements and conventions being reconstructed; a reference does not complete an outstanding proof.

For arithmetic calculations, \(X_0\) is of finite type over \(\mathbb F_q\), coefficients are \(\Lambda=\overline{\mathbb Q}_\ell\), and \(\ell\ne\operatorname{char}\mathbb F_q\). Complexes have arithmetic descent. Write \(Q=q^n\) and use geometric Frobenius, the inverse of arithmetic Frobenius. For differential equations and normal Morse data we instead use complex varieties and \(\mathbb C\)-coefficients. Passing between these settings requires additional structure; their sheaves do not automatically share a Frobenius action.

## 1. Begin with the information lost by a trace

Let \(V^\bullet\) be a bounded complex of finite-dimensional vector spaces with a commuting operator \(F\). Its supertrace is
\[
\operatorname{str}(F;V^\bullet)=
\sum_i(-1)^i\operatorname{Tr}(F;H^i(V^\bullet)).
\tag{1.1}
\]
For an \(F\)-stable subspace \(A\subset B\), an adapted basis gives a block upper triangular matrix, so
\(\operatorname{Tr}(F;B)=\operatorname{Tr}(F;A)+\operatorname{Tr}(F;B/A)\).
Apply this first to boundaries inside cycles and then to cycles inside each complex term. Boundary contributions in adjacent degrees cancel. Consequently (1.1) can also be computed on the terms of a finite complex.

The same cancellation in the long exact sequence of a triangle proves supertrace additivity. Over a field, split a complex as its cohomology plus contractible pairs. Tensoring preserves the contractible pairs, and
\(\operatorname{Tr}(A\otimes B)=\operatorname{Tr}(A)\operatorname{Tr}(B)\), as follows by summing diagonal entries in tensor product bases. Therefore supertraces multiply under tensor product and change sign under a shift by one.

On a point, all powers of \(F\) recover its eigenvalues with multiplicities, but not its Jordan blocks. Here is an elementary proof of the recovery statement. Let \(\lambda_1,\ldots,\lambda_r\) be the distinct nonzero eigenvalues in two invertible operators, and let \(a_j\) be the difference of their multiplicities. Equality of power traces gives
\[
\sum_{j=1}^r a_j\lambda_j^n=0\qquad(1\le n\le r).
\tag{1.2}
\]
The coefficient matrix is a Vandermonde matrix with its \(j\)-th column multiplied by \(\lambda_j\). Its determinant is, up to sign,
\(\prod_j\lambda_j\prod_{i<j}(\lambda_j-\lambda_i)\ne0\).
Thus every \(a_j=0\). A semisimple operator is classified by those eigenspaces, proving recovery of its semisimplification.

For the loss, take \(F=1+N\) on a two-dimensional space, with \(N\ne0\), \(N^2=0\). Then \(F^n=1+nN\) has trace \(2\) for every \(n\), just as the identity. The two operators are not conjugate. This is also a continuous \(\ell\)-adic representation of the arithmetic fundamental group of a point: the map \(n\mapsto1+nN\) extends through \(\widehat{\mathbb Z}\to\mathbb Z_\ell\). Thus geometric semisimplicity of the underlying vector space does not remove the arithmetic extension.

One power loses even semisimple information. Eigenvalue multisets \(\{1,-1\}\) and \(\{\mathrm i,-\mathrm i\}\) have equal first traces and opposite second traces. Roots of unity make both arithmetic representations continuous. Finally, a nonzero complex \(P\oplus P[1]\) has zero supertrace for every operator preserving the summands. No collection of trace functions can recover an arbitrary derived object.

## 2. Apply supertrace at every arithmetic stalk

For \(x\in X_0(\mathbb F_Q)\), let \(F_{Q,x}\) act on its geometric stalk and set
\[
t_{K,n}(x)=\operatorname{str}(F_{Q,x};K_{\bar x}).
\tag{2.1}
\]
The datum is the family over all \(n\ge1\). If the underlying closed point has degree \(d\mid n\), its operator is the \((n/d)\)-th power of degree-\(d\) geometric Frobenius. A Tate twist \((1)\) has eigenvalue \(Q^{-1}\). Hence
\[
t_{K[m](r),n}=(-1)^mQ^{-r}t_{K,n}.
\tag{2.2}
\]
In particular the constant sheaf has value \(1\), while the perverse constant sheaf on a smooth \(d\)-fold has value \((-1)^d\).

**Proposition 2.1.** Trace functions are additive in triangles. Pullback and tensor product give
\[
t_{f^*L,n}(x)=t_{L,n}(f(x)),\qquad
t_{K\otimes^L L,n}(x)=t_{K,n}(x)t_{L,n}(x).
\tag{2.3}
\]
For a separated finite-type map \(f:X_0\to Y_0\), the compact-support formula is
\[
t_{Rf_!K,n}(y)=
\sum_{\substack{x\in X_0(\mathbb F_Q)\\f(x)=y}}t_{K,n}(x).
\tag{2.4}
\]
The proof of (2.4) requires the general Grothendieck–Lefschetz trace theorem; that prerequisite is not completed by the following deduction.

**Proof.** The stalk long exact sequence and the equivariant tensor cohomology decomposition reduce additivity and multiplication to Section 1. Pullback identifies geometric stalks and their \(\mathbb F_Q\)-operators, proving the first formula. For (2.4), compact-support base change identifies the stalk with
\(R\Gamma_c(X_{\bar y},K|_{X_{\bar y}})\).
The trace theorem equates its supertrace to the displayed sum on the \(\mathbb F_Q\)-fibre. Its sheaf version extends to bounded complexes by successive truncation triangles. These comparisons give (2.4), conditional on the trace theorem and the exact six-operation foundations. For proper \(f\), one may replace \(f_!\) by \(f_*\). \(\square\)

External products similarly multiply functions on the two factors. The map to a point gives a global sum. For example, \(\mathbb P^1\) has cohomology \(\Lambda\) and \(\Lambda(-1)\) in degrees zero and two, so the sum for its constant sheaf is \(1+Q\); shifting by one gives \(-(1+Q)\). This uses the previously constructed projective-line cohomology and its Frobenius action.

To recover a local system from traces, we need a statement about all operators coming from its fundamental group. The group can be infinite.

**Lemma 2.2 (character separation).** Let \(G\) be any group and \(k\) an algebraically closed field of characteristic zero. For finite-dimensional \(k\)-representations \(V,W\), suppose
\[
\operatorname{Tr}(g;V)=\operatorname{Tr}(g;W)\qquad(g\in G).
\tag{2.5}
\]
Then their semisimplifications are isomorphic. In particular, two semisimple representations with the same character are isomorphic.

**Proof.** Write \(A=k[G]\) for the algebra of finite formal \(k\)-linear combinations of group elements, with multiplication extended from \(G\). Group representations and their invariant subspaces are exactly \(A\)-modules and \(A\)-submodules. We will construct elements of \(A\) whose traces read off individual simple multiplicities.

First, a nonzero homomorphism between simple modules is an isomorphism: its kernel and image are submodules. Thus there are no nonzero maps between nonisomorphic simples. An endomorphism of a finite-dimensional simple module has an eigenvalue \(\lambda\), because \(k\) is algebraically closed. The nonzero kernel of \(f-\lambda\) is the whole module, so every such endomorphism is scalar. These statements give the precise form of Schur's lemma needed below.

Next, every submodule \(N\) of a finite direct sum \(M\) of simple modules has a complement made from some of the coordinate summands. Start with \(U=0\). If \(N+U\ne M\), one coordinate simple summand \(S\) is not contained in \(N+U\). Simplicity gives \(S\cap(N+U)=0\). Adjoining \(S\) to \(U\) therefore preserves \(N\cap U=0\) and increases its dimension. The finite-dimensional process ends with \(M=N\oplus U\). If \(N\ne M\), projection along \(N\), followed by projection onto one simple summand of \(U\), gives a nonzero module map from \(M\) to that simple which kills \(N\).

Now let \(S_1,\ldots,S_r\) be pairwise nonisomorphic finite-dimensional simple modules. Choose a basis \(v_{i1},\ldots,v_{id_i}\) in each \(S_i\). Consider the left \(A\)-linear map
\[
E:A\longrightarrow \bigoplus_{i=1}^r S_i^{d_i},
\qquad a\longmapsto (a v_{ij})_{i,j}.
\tag{2.6}
\]
If its image were proper, the complement construction would give a nonzero map from this direct sum to some \(S_i\), vanishing on the image. Schur's lemma says that this map is zero on the other types and is \((s_{ij})\mapsto\sum_j c_j s_{ij}\) on the copies of \(S_i\), for scalars not all zero. Applying it to \(E(1)\) would give \(\sum_j c_jv_{ij}=0\), contrary to the chosen basis. Consequently \(E\) is onto. Specifying the images of every basis vector specifies an arbitrary endomorphism, so this proves the simultaneous surjectivity
\[
A\longrightarrow\bigoplus_{i=1}^r\operatorname{End}_k(S_i).
\tag{2.7}
\]

Every nonzero finite-dimensional module has a simple submodule: choose a nonzero submodule of least dimension. Quotienting by it and repeating gives a finite composition series. Choose such series for \(V\) and \(W\), and let \(S_1,\ldots,S_r\) list their distinct simple constituents. Block-trace additivity from Section 1 gives
\[
\operatorname{Tr}(a;V)-\operatorname{Tr}(a;W)
=\sum_i(m_i-n_i)\operatorname{Tr}(a;S_i),
\tag{2.8}
\]
where \(m_i,n_i\) are their multiplicities. The left side vanishes for every \(a\in A\), by (2.5) and linearity. For a fixed \(i\), (2.7) supplies \(a\) acting as a rank-one coordinate projection on \(S_i\) and as zero on every other \(S_j\). Its traces on these simples are respectively \(1\) and \(0\). Equation (2.8) then gives \(m_i-n_i=0\) in \(k\), hence equality of the integer multiplicities in characteristic zero.

Applying the same argument to two composition series of one representation proves that its direct sum of constituents is independent of the series. This justifies the semisimplification used in the statement, as well as its recovery from the character. No finiteness assumption on \(G\) has entered the proof. \(\square\)

**Corollary 2.3 (continuous characters).** Let \(G\) be a topological group and let two continuous finite-dimensional \(\overline{\mathbb Q}_\ell\)-representations be defined over a common finite extension \(E/\mathbb Q_\ell\). If their traces agree on a dense subset of \(G\), their semisimplifications over \(\overline{\mathbb Q}_\ell\) are isomorphic.

**Proof.** Trace is the sum of diagonal matrix entries, so the difference of the two characters is continuous as a function \(G\to E\). The field \(E\) is Hausdorff, so the inverse image of \(0\) is closed. It contains the dense subset and therefore all of \(G\). Apply Lemma 2.2. If equality is known on conjugacy classes, it is known on their union: \(\operatorname{Tr}(B C)=\operatorname{Tr}(C B)\), obtained by interchanging the two indices in the sum of matrix entries, implies invariance under conjugation. \(\square\)

The characteristic-zero qualification is essential. In characteristic \(p\), the direct sum of \(p\) copies of the trivial representation has zero character, just as the zero representation. The topology in Corollary 2.3 is also essential to its density argument; it is not needed for the purely algebraic lemma.

**Theorem 2.4 (assigned recovery statement; Chebotarev proof still required).** The family (2.1) determines the Grothendieck class of an arithmetic constructible perverse sheaf. In particular it determines an arithmetically semisimple perverse sheaf up to isomorphism.

We first justify the finite-length bookkeeping in this statement. In any finite-length abelian category, composition factors are independent of the composition series. Here is a proof that also applies to the perverse heart. A given composition series of length \(n\) bounds the length of every strict subobject chain by \(n\): intersect the chain with its first simple term \(S\), and take its image in the quotient by \(S\). The intersections can change strictly once; by induction, the images can change strictly at most \(n-1\) times. Each strict inclusion changes at least one of these, since subobjects \(B\subset C\) with the same intersection with \(S\) and the same image modulo \(S\) satisfy \(C=B+(C\cap S)=B\). This proves the bound.

Induct on that finite maximum chain length to compare two composition series of an object \(P\). A proper nonzero-kernel quotient has a smaller maximum: lift its chain and prefix the strict inclusion from zero into the kernel. Let the two series' first simple subobjects be \(S\) and \(T\). If they coincide, apply induction to \(P/S\). If they differ, their intersection is zero and \(S+T=S\oplus T\). Choose a composition series of \(P/(S+T)\). Its inverse images give a series of \(P/S\) beginning with \(T\), and a series of \(P/T\) beginning with \(S\). Induction on these proper quotients shows that both original series have precisely the factors \(S,T\) and those of \(P/(S+T)\), with the same multiplicities. This proves Jordan–Hölder here. For a short exact sequence, a series of the subobject followed by inverse images of a series of the quotient is a series of the middle object. Thus simple multiplicities are additive, and the Grothendieck group is freely generated by simple classes: the multiplicity maps give the inverse to sending each formal simple generator to its class. Its class therefore determines a semisimple object.

Here is the remaining geometric reduction. Express the difference of two perverse classes with equal functions as a finite integer combination of simple classes. Choose one maximal irreducible support, remove the other maximal supports, and shrink to a connected smooth dense open \(U\) on which all relevant simples are local systems shifted by the same dimension \(d\). The simple-object classification by intermediate extension and the needed finite length are earlier perverse-heart results, with their recursive proof obligations retained. We also retain the étale input that shrinking a connected normal scheme to a dense open induces a surjection of arithmetic fundamental groups: this ensures that irreducible local systems remain irreducible on the chosen common open. On \(U\), move the positive and negative coefficients to opposite sides. The equality of trace functions gives equality of Frobenius characters of the resulting two direct sums of local systems; the common sign \((-1)^d\) cancels. For a closed point of degree \(e\), its geometric Frobenius trace occurs in \(t_{K,e}\), so using every finite extension supplies all closed-point classes.

The precise remaining density input is this: for a connected smooth finite-type scheme over a finite field, the union of the conjugacy classes of geometric Frobenius elements of closed points is dense in its arithmetic étale fundamental group. This is the required form of Chebotarev, and it is still unproved here. Under that input, the exact lisse-sheaf/fundamental-group correspondence with continuous finite-coefficient-field models allows Corollary 2.3 to recover the semisimple local systems. Their simple multiplicities cancel. Uniqueness of intermediate extension cancels the corresponding perverse simple classes on that support. Repeat for the finitely many maximal supports. All remaining supports are proper closed subsets, so noetherian induction finishes the reduction.

This supplies the algebraic character-separation, continuity and Jordan–Hölder steps. Completion of Theorem 2.4 still requires Chebotarev and the exact earlier geometric and étale prerequisites just identified. Section 1 also shows why arithmetic semisimplicity and the family over all finite extensions cannot be replaced by geometric semisimplicity or a single trace function.

## 3. Build the character sheaves with their actual Frobenius action

We specify the one-dimensional fibres as functions on finite torsors; this fixes the inverse convention without guessing a Frobenius sign.

For an additive character \(\psi:\mathbb F_q\to\Lambda^\times\), consider \(y^q-y=x\). The polynomial is monic with derivative \(-1\), so it defines a finite étale cover of \(\mathbb A^1\). Its translations form \(\mathbb F_q\). On a geometric fibre, take functions \(h\) satisfying
\[
h(y+a)=\psi(a)h(y)\qquad(a\in\mathbb F_q).
\tag{3.1}
\]
Evaluation at any one point identifies this space with a line. Étale trivializations of the torsor glue these lines to \(\mathcal L_\psi\). If \(g\) acts on the torsor, its action on functions is \(h\mapsto h\circ g^{-1}\); translations commute with arithmetic descent, so the line is preserved.

For \(x\in\mathbb F_Q\), telescoping the equation gives
\[
y^Q-y=\sum_{j=0}^{n-1}x^{q^j}
=\operatorname{Tr}_{\mathbb F_Q/\mathbb F_q}(x).
\tag{3.2}
\]
Arithmetic Frobenius displaces \(y\) by this trace. Geometric Frobenius is its inverse, so its pullback action on functions evaluates at \(y+\operatorname{Tr}(x)\). By (3.1),
\[
t_{\mathcal L_\psi,n}(x)=
\psi\bigl(\operatorname{Tr}_{\mathbb F_Q/\mathbb F_q}x\bigr).
\tag{3.3}
\]
This is the inverse associated-character convention in Deligne's free SGA \(4\frac12\) text, expressed directly on fibre functions.

For \(\chi:\mathbb F_q^\times\to\Lambda^\times\), the finite étale cover \(y^{q-1}=x\) of \(\mathbb G_m\) has deck group \(\mathbb F_q^\times\). Use functions with \(h(ay)=\chi(a)h(y)\). Now
\[
y^Q/y=x^{(Q-1)/(q-1)}
=\operatorname{Nm}_{\mathbb F_Q/\mathbb F_q}(x),
\qquad
t_{\mathcal K_\chi,n}(x)=\chi(\operatorname{Nm}x).
\tag{3.4}
\]
The second equality follows by the same inverse-Frobenius pullback computation. The covers and line descent, rather than a trace formula, prove (3.3)–(3.4).

Let \(j:\mathbb G_m\hookrightarrow\mathbb A^1\). The stalk of \(j_!\mathcal K_\chi\) at zero vanishes. For nontrivial \(\chi\), tame monodromy has scalar \(T\ne1\); the étale inertia calculation has boundary complex \([V\xrightarrow{T-1}V]\), which is acyclic. Thus, subject to that earlier étale boundary comparison,
\[
j_!\mathcal K_\chi[1]=j_{!*}\mathcal K_\chi[1]
=Rj_*\mathcal K_\chi[1].
\tag{3.5}
\]
The wild part acts trivially and has exact invariants; the tame \(\ell\)-cohomological resolution supplies the displayed boundary calculation. This is the arithmetic comparison, not an identification of an étale puncture with a complex disc. For \(\chi=1\), intermediate extension is the constant perverse sheaf, with trace \(-1\) at zero; extension by zero has trace zero there.

## 4. Compute singular values from resolution fibres

Suppose \(f:Y\to X\) is a proper small resolution, \(Y\) is smooth of dimension \(d\), and the hypotheses of the earlier small-map theorem hold. Its identification
\(\operatorname{IC}_X=Rf_*\Lambda_Y[d]\), followed by proper base change, gives the calculation
\[
t_{\operatorname{IC}_X,n}(x)=
(-1)^d\sum_i(-1)^i
\operatorname{Tr}(F_Q;H^i(f^{-1}(\bar x),\Lambda)).
\tag{4.1}
\]
Smallness and the exact earlier theorem are substantive prerequisites. Once the identification is justified, (4.1) is just a stalk supertrace; it does not need the global trace formula.

First let the characteristic be odd and take
\[
C_a:\ y^2z=a x^2(x+z),\qquad a\in\mathbb F_q^\times.
\]
The normalization is
\[
[t:s]\longmapsto
[s(t^2-as^2):t(t^2-as^2):as^3].
\tag{4.2}
\]
Substitution verifies the equation. The coordinates cannot vanish together: if \(s=0\), the middle coordinate is nonzero; if \(s\ne0\), the last is nonzero. On the affine part, the parameter \(u=t/s\) gives \(x=u^2/a-1\), \(y=ux\), and \(u=y/x\) away from the node. It satisfies the monic equation \(u^2=a(x+1)\), proving finiteness on that chart. The point at infinity is smooth and the parameter gives an isomorphism there. This proves that the map is finite and birational from the smooth curve \(\mathbb P^1\), hence is its normalization, with the normality criterion proved in the first lesson's Appendix L.

The node is \(c=[0:0:1]\), with preimages \(u=\pm\sqrt a\). All other fibres are single points. A finite resolution of this curve is small because the exceptional zero-dimensional fibres lie over a codimension-one stratum. For \(a=1\), (4.1) gives \(-1\) off \(c\) and \(-2\) at \(c\). Identifying two rational points of \(\mathbb P^1\) yields \(Q\) rational points on \(C_1\), and the IC sum is \(-(Q+1)\).

If \(a\) is nonsquare, the two branches are exchanged by degree-one Frobenius. Thus
\[
t_{\operatorname{IC}_{C_a},n}(c)=-(1+(-1)^n).
\tag{4.3}
\]
For odd \(n\), neither preimage is rational, but the node is; the point count is \(Q+2\). For even \(n\), both preimages are rational, and the count is \(Q\). In both cases the smooth points contribute \(-1\) each and the total is \(-(Q+1)\). The degree-minus-one stalk retains the permutation action on the branches. Merely counting geometric branches would miss (4.3).

Next fix a plane \(F_2\subset\mathbb F_q^4\) and set
\[
X=\{W\in\operatorname{Gr}(2,4):\dim(W\cap F_2)\ge1\}.
\tag{4.4}
\]
Choose coordinates with \(F_2=\langle e_1,e_2\rangle\). The Plücker equations reduce to \(p_{34}=0\) and
\(p_{13}p_{24}-p_{14}p_{23}=0\).
The partial derivatives show that the only singular point is \(v=F_2\). Resolve the choice of an intersection line:
\[
Y=\{(L,W):L\subset F_2,\ \dim L=1,\ L\subset W\},
\qquad f(L,W)=W.
\tag{4.5}
\]
Over \(L\in\mathbb P(F_2)\), the choice of \(W/L\) is a line in the rank-three quotient \(\mathbb F_q^4/L\). Hence \(Y\) is a smooth projective \(\mathbb P^2\)-bundle over \(\mathbb P^1\), of dimension three. Off \(v\), the inverse is \(W\mapsto(W\cap F_2,W)\); over \(v\), the fibre is \(\mathbb P^1\). The sole exceptional stratum satisfies \(2\dim f^{-1}(v)=2<3\), so the resolution is small.

The two cohomology groups of this exceptional fibre give
\[
H^{-3}(\operatorname{IC}_X)_v=\Lambda,\qquad
H^{-1}(\operatorname{IC}_X)_v=\Lambda(-1),
\quad
t_{\operatorname{IC}_X,n}(v)=-(1+Q).
\tag{4.6}
\]
Off \(v\) the value is \(-1\). Counting the projective bundles and then replacing the exceptional fibre by its image gives
\[
\begin{aligned}
\#Y(\mathbb F_Q)&=(Q+1)(Q^2+Q+1),\\
\#X(\mathbb F_Q)&=Q^3+2Q^2+Q+1,\\
\sum_{x\in X(\mathbb F_Q)}t_{\operatorname{IC}_X,n}(x)
&=-(Q^3+2Q^2+2Q+1).
\end{aligned}
\tag{4.7}
\]
The normalized stalk polynomial is \(1+t\), since the two groups occur in degrees \(2k-3\), \(k=0,1\). Their Tate actions explain why evaluating at \(t=Q\) and multiplying by the perverse sign gives (4.6). This is the singular Grassmannian Schubert example of the preceding lesson. The general identification with Kazhdan–Lusztig polynomials is a separate theorem, stated in the freely accessible Kashiwara–Tanisaki paper; this example proves its own finite-field value without importing that general theorem's proof.

The projective-bundle cohomology formula gives a second check: \(Y\) has even Betti numbers \(1,2,2,1\), with Tate eigenvalues \(1,Q,Q^2,Q^3\). Its shift by three has supertrace (4.7). The projective-bundle and small-map foundations used here are not proved in these lessons.

## 5. Turn kernels into operators, then specialize to Fourier

Let \(X\xleftarrow a Z\xrightarrow bY\) be a finite-type correspondence with \(b\) separated, and let \(M\) be a constructible kernel. Define
\[
\mathcal H_M(A)=Rb_!(a^*A\otimes M)[s](r).
\]
Equations (2.2)–(2.4) give
\[
t_{\mathcal H_M(A),n}(y)=(-1)^sQ^{-r}
\sum_{\substack{z\in Z(\mathbb F_Q)\\b(z)=y}}
t_{M,n}(z)t_{A,n}(a(z)).
\tag{5.1}
\]
Each point of the correspondence contributes, including different points with the same endpoints.

To see composition geometrically, let a second correspondence be
\(Y\xleftarrow cT\xrightarrow dW\), with kernel \(N\). Form
\(R=Z\times_YT\), with projections \(\pi_Z,\pi_T\).
Compact-support base change and the projection formula identify the unshifted composite with the correspondence
\[
X\xleftarrow{a\pi_Z}R\xrightarrow{d\pi_T}W,
\qquad
\pi_Z^*M\otimes\pi_T^*N.
\tag{5.2}
\]
The shifts and twists add. On rational points, \(R(\mathbb F_Q)\) consists of pairs \((z,t)\) satisfying \(b(z)=c(t)\). Substituting (5.1) twice and grouping by that common value proves matrix multiplication of the resulting function kernels. The categorical identification (5.2) still uses the stated six-operation prerequisites.

For group multiplication, this becomes
\[
t_{Rm_!(A\boxtimes B),n}(g)=
\sum_{h\in G(\mathbb F_Q)}t_{A,n}(h)t_{B,n}(h^{-1}g).
\tag{5.3}
\]
Hecke correspondences record bundle modifications, with IC kernels and convolution supplied by geometric Satake. Formula (5.1) explains their operator form on finite-type scheme charts. A stack has automorphisms of its rational objects, so its trace formula needs groupoid weights and the stack formalism; an unweighted sum over isomorphism classes does not follow from (5.1). These are additional prerequisites for the Hecke preview.

For Fourier, take \(E=\mathbb A^d\), its dual \(E^\vee\), projections \(p_1,p_2\), and the pairing \(b(x,\xi)=\langle x,\xi\rangle\). With \(\psi\ne1\), define the normalization
\[
\mathsf F_\psi(K)=Rp_{2!}(p_1^*K\otimes b^*\mathcal L_\psi)[d].
\tag{5.4}
\]
It has no Tate twist. Substitution of (3.3) into (5.1) proves
\[
t_{\mathsf F_\psi(K),n}(\xi)=
(-1)^d\sum_{x\in\mathbb F_Q^d}
\psi_n(\langle x,\xi\rangle)t_{K,n}(x),
\qquad
\psi_n=\psi\circ\operatorname{Tr}_{\mathbb F_Q/\mathbb F_q}.
\tag{5.5}
\]
This deduction inherits the proof obligation for (2.4); it does not prove Fourier–Deligne t-exactness.

The function operator in (5.5) has square \(f(z)\mapsto Q^df(-z)\). Indeed, its double sum has inner coefficient
\(\sum_\xi\psi_n(\langle x+z,\xi\rangle)\).
If \(x=-z\), the coefficient is \(Q^d\). Otherwise the linear functional is onto. The field trace is also onto: its polynomial
\(t+t^q+\cdots+t^{q^{n-1}}\) is a nonzero polynomial of degree less than \(Q\), so it cannot vanish on the whole field; its nonzero \(\mathbb F_q\)-linear image in \(\mathbb F_q\) is all of \(\mathbb F_q\). Therefore \(\psi_n\ne1\). Translating the inner sum by a covector on which the character is not one multiplies the sum by that nontrivial scalar, forcing zero.

The two signs \((-1)^d\) cancel in the square. A point indicator transforms to the constant \((-1)^d\); the constant \((-1)^d\) transforms to \(Q^d\) times the point indicator. Thus the point perverse sheaf and the smooth perverse constant give the expected signs. This is a function identity; the lost-extension examples in Section 1 prevent inferring a derived isomorphism from it.

## 6. Differential equations retain more than numerical traces

For a left integrable connection \(M\) on a smooth complex \(d\)-fold, use the covariant normalization
\[
\operatorname{DR}(M)=
[M^{\mathrm{an}}\xrightarrow{\nabla}
\Omega^1\otimes M^{\mathrm{an}}\longrightarrow\cdots
\longrightarrow\Omega^d\otimes M^{\mathrm{an}}][d].
\tag{6.1}
\]
The unshifted first term has degree zero. In a horizontal frame it is the holomorphic de Rham complex tensored with the horizontal vector space. For completeness, on a star-shaped coordinate neighbourhood its positive-degree contraction is integration along \(z\mapsto tz\): on a \(k\)-form the operator integrates \(t^{k-1}\iota_{\sum z_i\partial_{z_i}}\) applied to its coefficients at \(tz\). Differentiation and the fundamental theorem of calculus give \(dH+Hd=1-\mathrm{ev}_0\). Thus the complex in such a frame resolves the horizontal local system, and (6.1) is \(L[d]\). Existence of horizontal frames for a general flat connection is a separate analytic integrability prerequisite.

The following full theorem remains an assigned proof obligation. On a smooth complex algebraic variety, covariant de Rham identifies bounded regular-holonomic algebraic \(D\)-module complexes with bounded algebraically constructible complexes on the analytic variety. It carries the ordinary \(D\)-module heart to the perverse heart, commutes with duality and the corresponding operation functors, and sends \(\mathcal O_X\) to \(\mathbb C_X[d]\). Algebraic regularity includes behaviour at the boundary of a compactification. The free Bhatt–Blickle–Lyubeznik–Singh–Zhang manuscript states this scope, but its cited proof is not a completed earlier programme proof. Its availability therefore does not discharge this obligation.

The normalized solution functor instead uses
\[
\operatorname{Sol}(M)=
R\mathcal Hom_{D^{\mathrm{an}}}(M^{\mathrm{an}},\mathcal O^{\mathrm{an}})[d]
\simeq D\operatorname{DR}(M).
\tag{6.2}
\]
It is contravariant and replaces a horizontal local system by its dual. The comparison in (6.2) belongs to the full regular theorem just stated.

Two direct calculations isolate conventions independently of that theorem. For
\(\nabla=d-A\,dz/z\), the convergent matrix exponential gives the fundamental solution \(e^{A\log z}\); differentiation verifies the equation and the inverse exponential shows that it spans all horizontal solutions. Going once positively around zero yields \(T=e^{2\pi\mathrm iA}\). The residue of the written connection is \(-A\). Once the regular correspondence is proved, its minimal extension must map to \(j_{!*}L[1]\): the equivalence preserves subobjects and quotients, and both minimal extensions are characterized by having neither supported at the boundary.

For the other calculation, \(d-a\,dz\) on \(\mathbb A^1\), \(a\ne0\), has the analytic solution \(e^{az}\). It consequently has the same analytic local system as the constant connection. At infinity, with \(w=1/z\), its connection form is \(a\,dw/w^2\). If a rational gauge is \(w^ku(w)\), where \(u(0)\ne0\), its logarithmic derivative is \(k\,dw/w+du/u\), with at most a simple pole. It cannot cancel the double pole. This connection fails boundary regularity and is excluded from the algebraic regular correspondence.

The full Riemann–Hilbert theorem promises recovery of regular differential equations with their morphisms and extensions. Trace functions retain only additive arithmetic data. Neither claim should be substituted for the other.

## 7. Probe a singularity before taking its Euler characteristic

Return to complex constructible sheaves on a smooth complex ambient manifold \(M\). A covector tests propagation by the local cohomology on one side of a real differentiable function. More precisely, a covector lies outside \(SS(K)\) if it has a neighbourhood in the cotangent bundle on which all corresponding tests
\[
\bigl(R\Gamma_{\{f\ge f(x)\}}K\bigr)_x
\tag{7.1}
\]
vanish. This describes the closed conic singular support. For a Whitney stratum \(S\) of complex dimension \(s\), take a normal slice and a generic conormal test. Let \(N_S(K)\) be its normal Morse complex, and set
\[
\mu_S(K)=N_S(K)[-s],\qquad
m_S(K)=\chi(\mu_S(K)),\qquad
CC(K)=\sum_Sm_S(K)[\overline{T^*_SM}].
\tag{7.2}
\]
Conormals have their complex orientations. The shift gives the normalization \(CC(\mathbb C_M[\dim M])=[T_M^*M]\). More generally, for a local system of rank \(r\) on a smooth closed submanifold \(S\), its extension by zero after shifting by \(\dim S\) has cycle \(r[T_S^*M]\): the only normal Morse space is that fibre in the normalized degree.

The general geometric assertions needed to make (7.2) intrinsic are substantial: independence of the normal test, invariance under refinement of stratification, the conormal description of singular support, and the normal-Morse characterization of the perverse cuts. The free Maxim–Schürmann manuscript states the precise forms in Theorem 3.12, Proposition 3.13 and Corollary 3.25; Definition 3.34 uses exactly the sign \((-1)^s\chi(N_S(K))=\chi(\mu_S(K))\). Their full proofs, including the stratified Morse prerequisites, remain a programme obligation here. No assertion of their completion follows from this definition or citation.

**Conditional general consequence.** With those geometric results proved, \(\mu_S(P)\) for a perverse sheaf is a vector space in degree zero. Therefore \(m_S(P)=\dim\mu_S(P)\ge0\), and this multiplicity is nonzero exactly on the conormal components of \(SS(P)\). Thus \(CC(P)\) is effective and \(\operatorname{supp}CC(P)=SS(P)\). This implication is immediate from the specified complexes; the theorem that puts them in degree zero is the unfinished step.

The disc permits a direct verification of the local complexes. Use the already proved diagram
\[
V\xrightarrow u W\xrightarrow v V,\qquad 1+vu\ \text{invertible}.
\]
Its stalk at zero is \([V\xrightarrow uW]\) in degrees minus one and zero. The open negative half-disc is contractible, and the restriction there has cohomology \(V[1]\). The support triangle for the closed positive half-disc identifies (7.1) with the fibre of the map
\[
[V\xrightarrow uW]\longrightarrow V[1],
\tag{7.3}
\]
whose degree-minus-one component is the identity. Cancelling that identity in the fibre leaves \(W\) in degree zero. This is also the normalized vanishing-cycle calculation of Lesson 6. A nonzero complex multiple of the coordinate gives the same calculation after rotating the half-disc. Away from the puncture, a nonzero covector tests a locally constant complex on a ball; restriction to the half-ball is a quasi-isomorphism, so the support test vanishes.

On the open stratum the normal slice is a point, and \(\mu\) is \(V[1][-1]=V\). Consequently the cycle on a disc is
\[
CC(P)=\dim V\,[T_D^*D]+\dim W\,[T_0^*D].
\tag{7.4}
\]
The same support tests show directly that its two possible components occur precisely when the corresponding spaces are nonzero. This establishes positivity and support equality in this local model without using the general normal-Morse theorem as a substitute proof.

The result can be computed from the two stalk Euler values. If \(\alpha_{\mathrm{open}}=-\dim V\) and \(\alpha_0=\dim W-\dim V\), then
\[
CC(P)=-\alpha_{\mathrm{open}}[T_D^*D]
+(\alpha_0-\alpha_{\mathrm{open}})[T_0^*D].
\tag{7.5}
\]
For intermediate extension, \(\dim W=\operatorname{rank}(T-1)\). For extension by zero or direct image, \(\dim W=\dim V\). A skyscraper has \(V=0\), while a smooth constant perverse sheaf has \(W=0\). In the rank-two unipotent classification of Lesson 6, the intermediate extension has cycle \(2[T_D^*D]+[T_0^*D]\); the additional five-vector indecomposable has cycle \(2[T_D^*D]+3[T_0^*D]\). Thus the second multiplicity measures vanishing data, not just nearby rank.

Local cohomology and shifts carry triangles to triangles. The finite-dimensional cancellation of Section 1, now with the identity operator, proves additivity of (7.2) and
\(CC(K[1])=-CC(K)\).
For \(P\ne0\), the object \(P\oplus P[1]\) consequently has zero cycle. Its local support tests are the direct sum of a complex and its shift; such a sum vanishes only if the complex vanishes. Hence its singular support is still \(SS(P)\). The loss of information occurs when taking Euler characteristic.

In higher dimensions the corresponding Euler-function factorization is obtained from the normal-slice/complex-link triangle. Its Euler characteristic is the stalk value minus the Euler integral over the complex link. With a finite constructible cell decomposition, that integral is the sum of the cell Euler characteristics times their stalk values: filter by cells and apply triangle additivity. The existence and compatibility of these normal-link decompositions are part of the missing stratified Morse foundations. Maxim–Schürmann's formulas (39)–(45) state the resulting general factorization. Equation (7.5) supplies its directly computed curve instance. None of these Euler numbers encodes arithmetic Frobenius eigenvalues.

## 8. Interpret a nilpotent support condition on bundles

Let \(C\) be a smooth projective complex curve. At a rank-\(m\) bundle \(E\), the bundle deformation complex and Serre duality identify classical cotangent vectors with
\[
\Phi\in H^0(C,\operatorname{End}(E)\otimes\omega_C),
\quad\text{equivalently}\quad
\Phi:E\longrightarrow E\otimes\omega_C.
\tag{8.1}
\]
The deformation and Serre-duality theorems are exact prerequisites for that identification; the free Frenkel lectures describe it in their Hitchin-system discussion.

Trivialize \(\omega_C\) locally. The coefficient of degree \(m-i\) in the characteristic polynomial of the resulting matrix is homogeneous of degree \(i\). Changing the trivialization multiplies it by the \(i\)-th transition factor. Thus these local coefficients glue to sections of \(\omega_C^{\otimes i}\), and define
\[
h(E,\Phi)=(c_1(\Phi),\ldots,c_m(\Phi))
\in\bigoplus_{i=1}^mH^0(C,\omega_C^{\otimes i}).
\tag{8.2}
\]
The global nilpotent cone is \(\mathcal N=h^{-1}(0)\).

Here the name has a concrete verification. If the characteristic polynomial is \(t^m\), Cayley–Hamilton gives \(\Phi^m=0\), interpreted as a map to \(E\otimes\omega_C^{\otimes m}\). To recall the algebraic step, expand the adjugate identity
\((tI-A)\operatorname{adj}(tI-A)=\det(tI-A)I\) in powers of \(t\). Its coefficient recurrences express the adjugate coefficients as polynomials in \(A\); substituting \(A\) in the resulting scalar polynomial identity gives the claimed zero. Conversely, a nilpotent matrix at a closed point has all eigenvalues zero and characteristic polynomial \(t^m\). If every pointwise Higgs matrix is nilpotent, the coefficient sections vanish at every closed point; the curve is reduced, so the sections vanish. This proves the pointwise description used here, not an identification of nonreduced scheme structures.

The geometric Langlands condition \(SS(K)\subset\mathcal N\) restricts cotangent directions. The zero section lies in \(\mathcal N\) over every bundle, so projecting \(\mathcal N\) to the bundle space cannot describe a proper singular locus. Nonzero covectors contain the relevant directional information. For \(m=1\), the only characteristic coefficient is \(\Phi\) itself, so the condition reduces to zero Higgs field.

The category with nilpotent singular support is formulated in the free Arinkin–Gaitsgory–Kazhdan–Raskin–Rozenblyum–Varshavsky manuscript. Applying it on the non-quasi-compact stack requires its chosen sheaf theory and compatible smooth charts. This is the assigned preview, with those foundations still required; it is not a claim that every perverse sheaf satisfies the condition. The complex support tests of Section 7 alone do not supply the algebraic \(\ell\)-adic or stack theory, nor a Langlands equivalence.

## 9. Exercises and solutions

### Exercise 1 — constants and a Kummer boundary

Compute the function of \(\Lambda_{\mathbb A^1}\) and \(j_!\mathcal K_\chi\) over every finite extension. Include the perverse shift and compare intermediate extension when \(\chi=1\).

**Solution.** The constant stalk has operator one, so its function is one and its shift has function minus one. For \(x\ne0\), use the fibre functions \(h(ay)=\chi(a)h(y)\). Arithmetic Frobenius multiplies \(y\) by \(\operatorname{Nm}(x)\); geometric Frobenius on \(h\) therefore has eigenvalue \(\chi(\operatorname{Nm}(x))\). Extension by zero contributes no stalk at zero. Thus the answer is \(\chi(\operatorname{Nm}(x))\) on \(\mathbb G_m(\mathbb F_Q)\) and zero at zero, with the whole function negated after shifting by one.

When \(\chi=1\), intermediate extension fills in a one-dimensional degree-minus-one stalk, giving value \(-1\) at zero. For \(\chi\ne1\), the invertible boundary differential in (3.5) leaves no boundary stalk, so intermediate extension agrees with extension by zero. The localization triangle for the trivial unshifted sheaf gives \(1_{\mathbb G_m}+1_{\{0\}}=1\), checking the boundary value and its shifted sign.

### Exercise 2 — additivity and arithmetic extensions

Prove triangle additivity of trace functions and exhibit a nonsplit perverse extension indistinguishable from its split sum by every trace function.

**Solution.** At a geometric stalk, let \(I_i\) be the successive images in the finite long exact sequence. Each term is an extension of two adjacent \(I_i\)'s, so its trace is the sum of their traces. Alternating the terms cancels every \(I_i\). Grouping the result by the three objects proves \(t_B=t_A+t_C\) for \(A\to B\to C\to A[1]\).

On a point choose \(F(e_1)=e_1\), \(F(e_2)=e_2+e_1\). The invariant line \(\Lambda e_1\) and quotient are trivial, while \(F^n\) has trace two for all \(n\). An invariant complementary line would have an eigenvector with nonzero \(e_2\)-coefficient. All eigenvalues are one, but \((F-1)(ae_1+be_2)=be_1\), which vanishes only if \(b=0\). Such a complement does not exist. Continuity was checked in Section 1, so this is an actual arithmetic example.

### Exercise 3 — branch permutations of a node

Calculate the IC trace and its global sum on \(C_1\), and then on \(C_a\) with \(a\) nonsquare.

**Solution.** The finite normalization (4.2) has one point over each smooth point and two over the node. Smallness identifies IC with its shifted direct image; proper base change gives the permutation representation on each fibre in degree minus one. For \(a=1\), the two node points are rational, so the node trace is \(-2\). There are \(Q-1\) smooth rational points, giving total \(-(Q-1)-2=-(Q+1)\).

For nonsquare \(a\), the \(n\)-th Frobenius fixes no branch when \(n\) is odd and both branches when \(n\) is even. Hence the node trace is zero or minus two. In the odd case all \(Q+1\) normalization points map to smooth points, and the node is one additional rational point. In the even case two normalization points are replaced by one node. These give point counts \(Q+2\) and \(Q\), and both IC sums equal \(-(Q+1)\). The shifted constant sheaf has node value \(-1\) instead, showing that IC detects the branch descent.

### Exercise 4 — Fourier kernel and square

Derive the trace function of (5.4), compute its square on functions, and test the point and perverse constant functions.

**Solution.** At \((x,\xi)\), pullback contributes \(t_K(x)\) and the torsor computation contributes \(\psi_n(\langle x,\xi\rangle)\). Tensor multiplies these values; the compact-support trace formula sums over \(x\); the shift supplies \((-1)^d\). This yields (5.5), subject to the general trace prerequisite identified in Proposition 2.1.

In the square, the coefficient of \(f(x)\) at \(z\) is the sum of \(\psi_n(\langle x+z,\xi\rangle)\) over all \(\xi\). The signs multiply to one. If \(x+z\ne0\), surjectivity of the linear functional and field trace supplies a translation with character different from one; invariance of the sum under that translation forces zero. If \(x+z=0\), every term is one and there are \(Q^d\) terms. The square is therefore \(Q^df(-z)\). A point indicator gives the constant \((-1)^d\), and that constant gives \(Q^d1_{\{0\}}\). No sheaf-level inversion theorem follows merely from these numerical equalities.

### Exercise 5 — the singular Schubert threefold

For \(X\) in (4.4), compute its IC trace, rational point count, global IC sum and normalized exceptional stalk polynomial.

**Solution.** Remembering \(L\subset W\cap F_2\) gives (4.5), a smooth threefold because it is a projective-plane bundle over a projective line. The projection is projective, is an isomorphism off \(v=F_2\), and has fibre \(\mathbb P^1\) over \(v\). The inequality \(2<3\) proves smallness. Hence IC is \(Rf_*\Lambda[3]\), using the earlier small-map theorem with its prerequisites.

At \(v\), the degree-zero and degree-two cohomology of the fibre become degrees minus three and minus one. Their operators have eigenvalues \(1,Q\), so the value is \(-(1+Q)\). Elsewhere it is \(-1\). Counting \(Y\) gives \((Q+1)(Q^2+Q+1)\); subtracting \(Q\) replaces its exceptional \(Q+1\) points by one and gives \(Q^3+2Q^2+Q+1\) points of \(X\). The \(Q^3+2Q^2+Q\) smooth points and the exceptional value sum to \(-(Q^3+2Q^2+2Q+1)\).

The stalk dimensions in degrees \(2k-3\) give the polynomial \(1+t\). Its evaluation at \(Q\) has the required overall minus sign because both cohomological degrees are odd. The projective-bundle formula gives \(H^*(Y)=H^*(\mathbb P^1)\langle1,\eta,\eta^2\rangle\), with \(\eta\) the fibre hyperplane class. Its even dimensions \(1,2,2,1\), Tate powers and shift by three reproduce the global sum. This proves the concrete Schubert value; the full Kazhdan–Lusztig comparison remains a separate proof obligation.

## Exact proof obligations and permitted references

All eighteen assigned items and five solutions remain in this draft. The explicit matrix, torsor, fibre, finite-sum and disc calculations above do not by themselves complete the following foundations:

- The general Grothendieck–Lefschetz trace formula for separated finite-type schemes and constructible adic complexes, and the exact compact-support base-change and projection comparisons used in (2.4) and (5.2).
- Chebotarev density in the full lisse arithmetic scope of Theorem 2.4, the exact continuous lisse-sheaf/fundamental-group correspondence and dense-open surjectivity, and the recursive hypotheses of finite length and the simple-object classification. Lemma 2.2 and Corollary 2.3 now prove the character-separation and continuity steps; the finite-length Grothendieck-group argument is also written above.
- The earlier normalization, étale inertia, small-map and projective-bundle results at their exact versions and coefficient scope.
- Full regular algebraic Riemann–Hilbert, horizontal-frame existence, boundary regularity and operation/duality comparisons. The recorded earlier Riemann–Hilbert lesson does not presently provide the whole theorem.
- General stratified Morse theory, the normal-test comparisons, constructible cell/link arguments, intrinsic characteristic cycles and the perverse normal-Morse criterion. The proved disc calculation does not establish their higher-dimensional scope.
- Bundle deformation theory, Serre duality, stack singular support and weighted stack trace formalism for the Langlands/Hecke preview; the general Schubert IC–Kazhdan–Lusztig theorem remains a separate earlier obligation.

The following free sources identify the statements and conventions. Their external citations do not replace any of these required proofs.

- P. Deligne, [Cohomologie étale, SGA \(4\frac12\)](https://publications.ias.edu/node/378), free author-hosted edition: “Rapport sur la formule des traces,” Theorem 3.2, and “Applications aux sommes trigonométriques,” Definition 1.7 and formulas (1.7.6)–(1.7.7).
- E. Frenkel, [Lectures on the Langlands program and conformal field theory](https://arxiv.org/abs/hep-th/0512172), §3.3 for the arithmetic dictionary and §9.5 for the Hitchin map.
- B. Bhatt, M. Blickle, G. Lyubeznik, A. K. Singh, W. Zhang, [Applications of perverse sheaves in commutative algebra](https://arxiv.org/abs/2308.03155v3), §2 for the scope and covariant normalization of regular Riemann–Hilbert.
- L. G. Maxim, J. Schürmann, [Constructible sheaf complexes in complex geometry and Applications](https://arxiv.org/abs/2105.13069v2), [free author manuscript](https://people.math.wisc.edu/~lmaxim/handbook.pdf), Theorem 3.12, Proposition 3.13, Corollary 3.25, Definition 3.34 and Remark 3.36.
- M. Kashiwara, T. Tanisaki, [Parabolic Kazhdan–Lusztig polynomials and Schubert varieties](https://arxiv.org/abs/math/9908153), Theorem 5.4 for the general comparison statement.
- D. Arinkin, D. Gaitsgory, D. Kazhdan, S. Raskin, N. Rozenblyum, Y. Varshavsky, [The stack of local systems with restricted variation and geometric Langlands theory with nilpotent singular support](https://arxiv.org/abs/2010.01906), the introductory overview of the nilpotent-support category.
- MIT OpenCourseWare, [General results of representation theory](https://ocw.mit.edu/courses/18-712-introduction-to-representation-theory-fall-2010/0721b66f53c3c196ce86d6d867514442_MIT18_712F10_ch2.pdf), free 18.712 lecture notes (Fall 2010, taught by P. Etingof), §§2.1–2.2 and 2.6–2.7: semisimple submodules, simultaneous density, characters and Jordan–Hölder. The complete character argument used here is written in Section 2.
