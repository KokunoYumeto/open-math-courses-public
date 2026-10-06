# Cyclic cohomology: traces, differentials and symmetry

*Written by GPT-6.1 Sol (OpenAI), September 2026, at Ultra. Not yet reviewed. Public domain (CC0).*

A trace ignores where a circular product starts: \(\tau(ab)=\tau(ba)\). A higher trace must also remember differentials. Its arguments acquire a sign when their starting point moves. Cyclic cohomology combines these two requirements into a complex. The cyclic category explains why the resulting theory has a derived-functor interpretation and a degree-two periodicity operator.

We start with traces and a concrete differential, then connect differential forms to cyclic cocycles. After that we describe the category that records circular order. This order of ideas makes the algebra visible before the categorical machinery.

We assume associative algebras, tensor products and elementary chain complexes. The basic cochain constructions work over a commutative ring \(k\). When averaging over a finite cyclic group is used, we explicitly require \(k\) to contain \(\mathbb Q\). Algebraic duals mean all \(k\)-linear maps; no continuity is implicit. The examples of smooth functions use complex coefficients and elementary integration. Basic references are [Khalkhali 2007] and [Connes 1983].

## 1. What a higher trace must satisfy

For an associative \(k\)-algebra \(A\), put

\[
C^n(A)=\operatorname{Hom}_k(A^{\otimes_k(n+1)},k),\qquad n\geq0.
\]

The algebra need not be unital in this section. Define

\[
\begin{aligned}
(b\varphi)(a_0,\ldots,a_{n+1})
={}&\sum_{i=0}^{n}(-1)^i
 \varphi(a_0,\ldots,a_i a_{i+1},\ldots,a_{n+1})\\
 &+(-1)^{n+1}\varphi(a_{n+1}a_0,a_1,\ldots,a_n),\\
(\lambda_n\varphi)(a_0,\ldots,a_n)
={}&(-1)^n\varphi(a_n,a_0,\ldots,a_{n-1}).
\end{aligned} \tag{1.1}
\]

Let \(b'\) be the sum in the first line, without the final term. A cochain is **cyclic** when \(\lambda_n\varphi=\varphi\). Write \(C_\lambda^n(A)\) for these cochains.

**Proposition 1.1.** The operators satisfy

\[
b^2=0,\qquad (b')^2=0,\qquad
(1-\lambda_{n+1})b=b'(1-\lambda_n). \tag{1.2}
\]

Consequently \(C_\lambda^\bullet(A)\) is a cochain complex.

**Proof.** It is useful to work on tensors first. For \(0\leq i<n\), let \(d_i\) multiply positions \(i,i+1\), and let

\[
d_n(a_0,\ldots,a_n)=(a_na_0,a_1,\ldots,a_{n-1}).
\]

For \(i<j\),

\[
d_i d_j=d_{j-1}d_i. \tag{1.3}
\]

For disjoint multiplications this just compares the positions after one position has disappeared. For adjacent multiplications it is associativity. If \(j=n\), the same check takes place across the end of the list. For example, the case \(i=0,j=n\) compares \((a_na_0)a_1\) with \(a_n(a_0a_1)\); the case \(i=n-1,j=n\) compares \(a_{n-1}(a_na_0)\) with \((a_{n-1}a_n)a_0\).

In \((\sum(-1)^i d_i)^2\), each term \(d_i d_j\), \(i<j\), has sign \((-1)^{i+j}\). Its partner \(d_{j-1}d_i\) has sign \((-1)^{i+j-1}\). They cancel. The same pairing with only the nonwrapping faces proves the assertion for \(b'\), after dualizing.

For the last identity, set \(t_n(a_0,\ldots,a_n)=(a_n,a_0,\ldots,a_{n-1})\) and \(T_n=(-1)^n t_n\). Direct substitution gives

\[
d_0t_n=d_n,\qquad d_it_n=t_{n-1}d_{i-1}\quad(1\leq i\leq n).
\]

Let \(b_n=\sum_{i=0}^n(-1)^i d_i\) and \(b'_n=\sum_{i=0}^{n-1}(-1)^i d_i\). The displayed relations give

\[
b_nT_n=(-1)^n d_n+T_{n-1}b'_n.
\]

Subtracting from \(b_n=b'_n+(-1)^n d_n\) yields
\(b_n(1-T_n)=(1-T_{n-1})b'_n\). Dualization is exactly the third identity in (1.2). If \((1-\lambda_n)\varphi=0\), it follows that \((1-\lambda_{n+1})b\varphi=0\). \(\square\)

**Definition 1.2.** The cohomology of \((C_\lambda^\bullet(A),b)\) is denoted \(H_\lambda^n(A)\). For a \(\mathbb Q\)-algebra this is the cyclic cohomology computed by cyclic cochains. Over other coefficient rings the derived cyclic theory will require the full cyclic resolution; the cyclic-invariant complex alone is not its definition.

In degree zero,

\[
(b\tau)(a_0,a_1)=\tau(a_0a_1)-\tau(a_1a_0).
\]

Thus \(H_\lambda^0(A)\) is exactly the space of traces. There are no incoming coboundaries in degree zero. This remains true over any coefficient ring.

**Example 1.3.** On \(M_r(k)\), every trace is a scalar multiple of the matrix trace. Let \(E_{ij}\) denote the matrix units. For \(i\ne j\),

\[
E_{ij}=[E_{ii},E_{ij}],\qquad
E_{ii}-E_{jj}=[E_{ij},E_{ji}].
\]

A trace vanishes on the first expression and has equal values on all diagonal matrix units. Conversely, the matrix trace satisfies the trace identity because \(k\) is commutative. This proves the assertion without a hypothesis on the characteristic of \(k\).

## 2. Differential forms produce cyclic cocycles

A differential graded algebra \((\Omega,d)\) has an associative graded product and a degree-one map satisfying

\[
d^2=0,\qquad d(\omega\eta)=d\omega\,\eta+(-1)^{\deg\omega}\omega\,d\eta.
\]

We do not require the product to be graded commutative. A **closed graded trace of degree \(n\)** is a linear functional \(\int:\Omega^n\to k\) such that

\[
\int d\zeta=0\quad(\zeta\in\Omega^{n-1}),\qquad
\int\omega\eta=(-1)^{pq}\int\eta\omega
\quad(\deg\omega=p,\deg\eta=q,p+q=n).
\tag{2.1}
\]

When \(n=0\), closedness is vacuous. Let \(\rho:A\to\Omega^0\) be an algebra homomorphism.

**Theorem 2.1.** The cochain

\[
\varphi(a_0,\ldots,a_n)
=\int \rho(a_0)d\rho(a_1)\cdots d\rho(a_n)
\tag{2.2}
\]

is cyclic and satisfies \(b\varphi=0\).

**Proof.** Write \(a_j\) for \(\rho(a_j)\) in this proof. Closedness applied to \(a_n a_0\,da_1\cdots da_{n-1}\) gives

\[
0=\int da_n\,a_0\,da_1\cdots da_{n-1}
 +\int a_n\,da_0\cdots da_{n-1}.
\]

The graded-trace rule moves \(da_n\) past the remaining degree \(n-1\) expression, with sign \((-1)^{n-1}\). Therefore

\[
\int a_n\,da_0\cdots da_{n-1}
=(-1)^n\int a_0\,da_1\cdots da_n.
\]

This is cyclicity. For \(n=0\), cyclicity is automatic and the cocycle assertion is the trace identity.

For \(n>0\), expand each \(d(a_i a_{i+1})=da_i\,a_{i+1}+a_i\,da_{i+1}\) in \(b\varphi\). The term from \(i=0\) cancels the second part from \(i=1\). For \(1\leq i<n\), the first part from \(i\) cancels the second part from \(i+1\). What remains is

\[
(-1)^n\int a_0\,da_1\cdots da_n\,a_{n+1}
 +(-1)^{n+1}\int a_{n+1}a_0\,da_1\cdots da_n.
\]

These cancel by the graded-trace identity with degrees \(n\) and \(0\). No reordering of the individual factors \(a_i\) has been used. \(\square\)

**Example 2.2.** Let \(A=\mathbb C[z,z^{-1}]\). Define a derivation \(\delta(z^m)=mz^m\) and let \(\tau\) extract the coefficient of \(z^0\). Then

\[
\varphi(a_0,a_1)=\tau(a_0\delta(a_1)),\qquad
\varphi(z^p,z^q)=q\,\mathbf1_{p+q=0}.
\tag{2.3}
\]

Since \(\tau\delta=0\), applying \(\delta\) to \(a_0a_1\) shows that \(\varphi\) is antisymmetric. Applying the derivation rule to \(a_1a_2\) proves \(b\varphi=0\). This cocycle is not a cyclic coboundary: on a commutative algebra \(b:C^0\to C^1\) is zero, whereas \(\varphi(z^{-1},z)=1\).

The same construction on smooth functions on the circle uses \(\delta=(1/i)\,d/dt\) and the normalized integral. Its value on \((z^{-1},z)\) is again \(1\). The algebraic example needs no assertion about the cohomology of all smooth functions.

**Example 2.3.** On the two-dimensional torus, use angles \(x,y\) modulo \(2\pi\), the orientation \(dx\wedge dy\), and

\[
\psi(f_0,f_1,f_2)=\frac1{(2\pi i)^2}\int f_0\,df_1\wedge df_2.
\]

Stokes' theorem and graded commutativity verify (2.1), so Theorem 2.1 applies. For \(u=e^{ix}\), \(v=e^{iy}\),

\[
\psi((uv)^{-1},u,v)=1,\qquad
\psi((uv)^{-1},v,u)=-1.
\]

Indeed \((uv)^{-1}du\wedge dv=-dx\wedge dy\), and \((2\pi i)^2=-4\pi^2\). The two minus signs give the first value. This calculation fixes both the orientation and the normalization.

## 3. Averaging is a coefficient-dependent step

The signed rotation satisfies \(\lambda_n^{n+1}=1\), since \(n(n+1)\) is even. Put

\[
N_n=1+\lambda_n+\cdots+\lambda_n^n.
\]

**Lemma 3.1.** Let \(V\) be a \(k\)-module and let \(T^{r}=1\) on \(V\). If \(r\) is invertible in \(k\), the sequence

\[
0\longrightarrow\ker(1-T)\longrightarrow V
 \xrightarrow{1-T}V\xrightarrow{N}V
 \xrightarrow{1-T}V\xrightarrow{N}\cdots,
\qquad N=\sum_{j=0}^{r-1}T^j,
\tag{3.1}
\]

is exact.

**Proof.** Let \(P=N/r\). Then \(P^2=P\), \(TP=P\), and \(P\) is the identity on the invariant submodule. Thus \(\operatorname{im}N=\ker(1-T)\). Also \(N(1-T)=0\), so \(\operatorname{im}(1-T)\subseteq\ker N\). To prove the reverse inclusion, put

\[
Q=-\frac1r\sum_{j=0}^{r-1}jT^j.
\]

Multiplying out gives \((1-T)Q=1-P\). If \(Nv=0\), then \(Pv=0\) and \(v=(1-T)Qv\). The equalities repeat at every position of (3.1). \(\square\)

For all cochain degrees simultaneously, this argument applies when \(k\) contains \(\mathbb Q\). It does not justify deleting the finite-group resolution over \(\mathbb Z\), or in positive characteristic.

**Example 3.2.** Let \(V=\mathbb F_p\), let \(T=1\), and take \(r=p\). Then \(1-T=0\) and \(N=p=0\). Every differential in the unaugmented part of (3.1) is zero. Each positive cohomology group is \(\mathbb F_p\). This is a concrete obstruction to the averaging argument, not an assertion that every algebra in characteristic \(p\) has this cohomology.

## 4. The category of circular order

The category \(\Lambda\) has objects \([n]\), \(n\geq0\). A morphism \([n]\to[m]\) is an equivalence class of nondecreasing functions \(f:\mathbb Z\to\mathbb Z\) satisfying

\[
f(i+n+1)=f(i)+m+1. \tag{4.1}
\]

Two functions represent the same morphism if they differ by an integral multiple of \(m+1\). Composition is composition of functions. Changing a representative in the inner function changes the composition by a period in the outer one, so composition is well-defined.

The simplicial category \(\Delta\) embeds in \(\Lambda\): extend a nondecreasing map \(s:\{0,\ldots,n\}\to\{0,\ldots,m\}\) periodically using (4.1). The extension remains nondecreasing across the boundary because \(s(n)<s(0)+m+1\). Let \(r_n\) be the rotation represented by \(i\mapsto i+1\).

**Theorem 4.1.** Every morphism \([n]\to[m]\) has a unique factorization

\[
f=s\,r_n^a,\qquad s\in\operatorname{Hom}_\Delta([n],[m]),
\quad a\in\mathbb Z/(n+1). \tag{4.2}
\]

The automorphism group of \([n]\) is the cyclic group generated by \(r_n\).

**Proof.** Fix a lift \(f\). Since (4.1) has a positive output period, \(f(i)\) tends to \(\pm\infty\) as \(i\) tends to \(\pm\infty\). Let \(p\) be the first integer such that \(f(p)\geq0\). Then

\[
0\leq f(p)\leq f(p+n)=f(p-1)+m+1\leq m.
\]

Thus \(s(j)=f(p+j)\), \(0\leq j\leq n\), is a simplicial map. Its periodic extension is \(f\circ r_n^p\), giving \(f=s r_n^{-p}\). Replacing \(f\) by \(f+q(m+1)\) replaces \(p\) by \(p-q(n+1)\); it changes neither \(s\) nor \(-p\) modulo \(n+1\).

Conversely, a periodically extended simplicial map has its first nonnegative value at \(0\): \(s(0)\geq0\) and \(s(-1)=s(n)-(m+1)<0\). The first nonnegative position of a lift of \(s r_n^a\) therefore recovers \(-a\) modulo \(n+1\), and then recovers \(s\). This proves uniqueness.

If a class is invertible, the composite of lifts for it and its inverse is a translation by a period. Hence its lift is injective and surjective on \(\mathbb Z\). A nondecreasing bijection of \(\mathbb Z\) is \(i\mapsto i+c\). Formula (4.1) then forces \(m=n\); translations modulo \(n+1\) give exactly the claimed group. \(\square\)

**Corollary 4.2.** There are

\[
\bigl|\operatorname{Hom}_\Lambda([n],[m])\bigr|
=(n+1)\binom{n+m+1}{n+1}
\]

morphisms. In particular, \(\operatorname{Hom}_\Lambda([n],[0])\) has \(n+1\) elements. The object \([0]\) is not terminal.

**Proof.** A nondecreasing list of length \(n+1\) with entries in \(\{0,\ldots,m\}\) is a multiset of that length from \(m+1\) symbols. Counting multiplicities gives the binomial coefficient. Theorem 4.1 contributes the \(n+1\) rotations. \(\square\)

**Theorem 4.3.** The category \(\Lambda\) is isomorphic to its opposite. On lifts an explicit contravariant operation is

\[
D f(j)=\min\{i\in\mathbb Z:f(i)\geq j\}. \tag{4.3}
\]

It satisfies \(D(gf)=Df\,Dg\) and

\[
D^2 f(i)=f(i-1)+1.
\tag{4.4}
\]

Thus its square is naturally isomorphic to the identity, rather than equal to the identity on lifts.

**Proof.** The minimum in (4.3) exists by the limits used in Theorem 4.1. The function \(Df\) is nondecreasing, and

\[
Df(j+m+1)=Df(j)+n+1.
\]

Changing \(f\) by an output period changes \(Df\) by an input period. It therefore defines a morphism \([m]\to[n]\).

The defining equivalence is

\[
Df(j)\leq i\quad\Longleftrightarrow\quad j\leq f(i).
\tag{4.5}
\]

Applying it twice shows that
\(D(gf)(j)\leq i\) exactly when \(Dg(j)\leq f(i)\), and hence exactly when \(Df(Dg(j))\leq i\). This proves the composition rule. The identity lift has \(D(\mathrm{id})=\mathrm{id}\).

For (4.4), the assertion \(Df(j)\geq i\) is equivalent to \(j>f(i-1)\). Its least integer solution is \(f(i-1)+1\). Accordingly

\[
D^2 f=r_m f r_n^{-1}.
\]

Conjugation by the objectwise rotations is an automorphism naturally isomorphic to the identity. Since \(D^2\) is bijective on every morphism set, \(D\) is bijective on every morphism set as well. This proves the isomorphism with the opposite category. \(\square\)

## 5. An algebra as a functor

For this section \(A\) is unital. We use covariant functors from the circular-order category just defined. Self-duality permits an equivalent contravariant convention, but one must also transform the maps when changing conventions.

More generally, a **cyclic object in a category \(\mathcal C\)**, in this convention, is a covariant functor \(\Lambda\to\mathcal C\). Its morphisms are natural transformations. When \(\mathcal C\) is abelian, this functor category is abelian as well: objectwise kernels and cokernels inherit their maps from the universal properties, and objectwise exactness verifies the abelian axioms. This explains where the abelian category needed for Ext comes from.

Let

\[
A^\natural([n])=A^{\otimes_k(n+1)}.
\]

For a lift \(f:[n]\to[m]\), and each residue \(j\) modulo \(m+1\), consider the integer fiber \(f^{-1}(j)\). It is either empty or a finite consecutive list. Multiply the factors \(a_i\), read modulo \(n+1\), in that list's integer order to obtain \(y_j\). Use \(y_j=1\) for an empty fiber. Set

\[
A^\natural(f)(a_0\otimes\cdots\otimes a_n)
=y_0\otimes\cdots\otimes y_m.
\tag{5.1}
\]

Every input residue occurs in exactly one such list. A list has at most \(n+1\) terms, because increasing the input by \(n+1\) increases the output by \(m+1\). Changing the lift by an output period shifts a list by an input period, so (5.1) is independent of the lift.

**Proposition 5.1.** Formula (5.1) defines a covariant functor \(A^\natural:\Lambda\to k\text{-}\mathrm{Mod}\), natural in unital algebra homomorphisms.

**Proof.** The fiber of a composite \(gf\) over an integer \(j\) is the ordered concatenation of the fibers of \(f\) over the consecutive integers in \(g^{-1}(j)\). Multiplying in two stages or in one stage agrees by associativity. Empty intermediate fibers contribute the unit. Thus \(A^\natural(gf)=A^\natural(g)A^\natural(f)\). The identity has single-element fibers and acts as the identity. A unital homomorphism preserves every product and every empty product, proving naturality. \(\square\)

For \(A=k\), all tensor powers canonically identify with \(k\), and every morphism acts as the identity. Denote this constant functor by \(k^\natural\).

**Theorem 5.2.** Natural transformations \(A^\natural\to k^\natural\) are in bijection with traces on \(A\). The transformation associated to \(\tau\) is

\[
\tau_n(a_0\otimes\cdots\otimes a_n)=\tau(a_0\cdots a_n).
\tag{5.2}
\]

**Proof.** The map \([n]\to[0]\) represented by the periodic extension of the constant simplicial map multiplies \(a_0,\ldots,a_n\) in that order. Naturality forces (5.2). For \(n=1\), the other morphism to \([0]\) multiplies \(a_1a_0\). Comparing them forces \(\tau(a_0a_1)=\tau(a_1a_0)\).

Conversely, grouping a circular list into consecutive blocks preserves its product up to a cyclic change of starting point. A trace is invariant under such a change: move the initial block to the end using \(\tau(xy)=\tau(yx)\). Formula (5.2) therefore commutes with every map (5.1). This proves both existence and uniqueness. \(\square\)

The same construction works for a unital ring regarded as a \(\mathbb Z\)-algebra. For a nonunital algebra, one first adjoins a unit and uses the relative theory of the augmentation to \(k\). A statement that uses empty fibers cannot silently omit this step.

**Proposition 5.3.** For a covariant functor \(E:\Lambda\to k\text{-}\mathrm{Mod}\), a natural transformation to \(k^\natural\) is determined by a linear functional \(\ell:E([0])\to k\) that agrees after the two maps \([1]\to[0]\).

**Proof.** Necessity follows from naturality. For sufficiency, the maps \([n]\to[0]\) correspond to the \(n+1\) possible circular cuts. Two neighboring cuts can be obtained by first mapping \([n]\to[1]\), making the single vertex between the cuts one block and the other vertices the second block, and then applying the two maps \([1]\to[0]\). The assumed equality therefore makes \(\ell E(p)\) independent of the chosen \(p:[n]\to[0]\). Use this functional as the degree-\(n\) component. For any \(f:[n]\to[m]\), the composite of a chosen map \([m]\to[0]\) with \(f\) is a map \([n]\to[0]\). Independence of the cut proves naturality. The chosen map \([n]\to[0]\) also forces this component in any natural transformation, proving uniqueness. \(\square\)

## 6. A projective resolution that keeps the integral information

Let \(R\) be a commutative ring. The category of covariant functors \(\Lambda\to R\text{-}\mathrm{Mod}\) is abelian: kernels, images and cokernels are taken at each object. Put

\[
P_q([n])=R[\operatorname{Hom}_\Lambda([q],[n])].
\tag{6.1}
\]

Square brackets here mean the free \(R\)-module on a set. A morphism acts by postcomposition. Evaluation at the identity gives

\[
\operatorname{Hom}_\Lambda(P_q,E)\simeq E([q]).
\tag{6.2}
\]

Indeed the image of a basis vector \(f\) must be \(E(f)x\), where \(x\) is the image of the identity. Since evaluation preserves surjections, each \(P_q\) is projective. Sums of these functors give enough projectives: for each \(x\in E([q])\), use the corresponding map \(P_q\to E\).

Let \(\delta_i:[q-1]\to[q]\) be the simplicial injection omitting \(i\). Precomposition defines

\[
F_i:P_q\to P_{q-1},\qquad F_i(e_f)=e_{f\delta_i}.
\]

On \(P_q\) let \(T_q\) be \((-1)^q\) times precomposition by \(r_q^{-1}\). Set

\[
D_q=1-T_q,\quad N_q=\sum_{j=0}^qT_q^j,\quad
b_q=\sum_{i=0}^q(-1)^iF_i,\quad
b'_q=\sum_{i=0}^{q-1}(-1)^iF_i.
\tag{6.3}
\]

The formulas involving faces apply in positive degree. Put \(b_0=b'_0=0\).

**Lemma 6.1.** These operators satisfy

\[
bD=Db',\qquad b'N=Nb,\qquad DN=ND=0.
\tag{6.4}
\]

For each object, the augmented complex alternating \(D\) and \(N\) is exact over \(R\), with degree-zero quotient \(P_q/DP_q\).

**Proof.** Precomposing by a rotation and then omitting a position gives the same face-rotation relations used in Proposition 1.1. Thus \(bD=Db'\). Also \(T_q^{q+1}=1\), which gives \(DN=ND=0\).

For the norm identity, write \(t_q\) for unsigned rotation on any cyclic chain module. Iterating the face-rotation relations gives

\[
d_i t_q^j=
\begin{cases}
t_{q-1}^j d_{i-j},&i\geq j,\\
t_{q-1}^{j-1}d_{q+1+i-j},&i<j.
\end{cases}
\tag{6.5}
\]

The same formulas hold for the operators \(F_i\). In the expansion of \(b'_qN_q\), fix \(0\leq a\leq q-1\), the power of \(t_{q-1}\). The first case of (6.5), with \(j=a\), contributes faces indexed \(0\leq k\leq q-1-a\). The second case, with \(j=a+1\), contributes \(q-a\leq k\leq q\). Their signs are respectively

\[
(-1)^{k+(q+1)a}=(-1)^{k+(q-1)a},\qquad
(-1)^{k+(q+1)a}=(-1)^{k+(q-1)a}.
\]

Together they give every face in \(T_{q-1}^a b_q\) exactly once. Summing over \(a\) proves \(b'N=Nb\).

For exactness, Theorem 4.1 says that precomposition by the rotations acts freely on the basis of \(P_q([n])\). On an orbit choose the signed basis \(v_j=(-1)^{qj}e_{f r_q^{-j}}\), \(0\leq j\leq q\). The sign is consistent on returning to \(j=0\), since \(q(q+1)\) is even, and \(T_qv_j=v_{j+1}\).

In this basis \(\ker(1-T_q)\) consists of vectors with equal coefficients, and is the image of \(N_q\). The kernel of \(N_q\) consists of vectors whose coefficients sum to zero, and is generated over \(R\) by the differences \(v_j-v_{j+1}\). These are the image of \(1-T_q\). This proof divides by no integer. It works on each orbit and hence on their direct sum. \(\square\)

Form a first-quadrant double complex with \(P_{p,q}=P_q\) for all \(p,q\geq0\). A horizontal boundary lowers \(p\): it is \(D_q\) for odd \(p\), and \(N_q\) for positive even \(p\). A vertical boundary lowers \(q\): it is \(b_q\) for even \(p\), and \(-b'_q\) for odd \(p\). Its total degree is \(p+q\).

**Theorem 6.2.** The total complex, augmented to the constant functor \(R^\natural\), is a projective resolution of \(R^\natural\).

**Proof.** The squares of both boundaries are zero. The mixed terms cancel by (6.4): at odd \(p\) they are \(-Db'+bD\); at positive even \(p\) they are \(Nb-b'N\). Thus the sum of the boundaries squares to zero. Each total term is a finite direct sum of projective functors.

Calculate first in the horizontal direction at a fixed object \([n]\). Lemma 6.1 leaves only the column \(p=0\), with terms \(P_q([n])/DP_q([n])\). The unique factorization in Theorem 4.1 identifies a basis for this quotient with the simplicial maps \([q]\to[n]\). The relation is \([e_{s r_q^{-j}}]=(-1)^{qj}[e_s]\). Since \(s\delta_i\) is again simplicial, the boundary on these basis elements is the ordinary alternating face boundary.

This is the unnormalized chain complex of the ordered simplex with vertices \(0,\ldots,n\). Here is an explicit augmented contraction. To a nondecreasing list \((a_0,\ldots,a_q)\) attach the vertex zero at the start:

\[
h_q(a_0,\ldots,a_q)=(0,a_0,\ldots,a_q),\qquad
h_{-1}(1)=(0).
\]

The first face of \(h_q\) returns the original list. Every other face cancels the corresponding term of \(h_{q-1}\partial\). Thus \(\partial h+h\partial=1\) on the augmented complex. Its homology is \(R\) in degree zero and zero above.

For each total degree there are finitely many positions. Filtering by vertical degree and using the horizontal homology therefore computes total homology by a finite filtration in that degree; no infinite-product or convergence assertion is needed. The result at every object is \(R\) in degree zero. The augmentation sends every basis vector of \(P_0([n])\) to \(1\), and commutes with postcomposition. Its degree-zero homology is consequently the constant functor. Exactness is objectwise, so this proves the theorem. \(\square\)

This resolution preserves the finite-group information over \(\mathbb Z\). It does not replace its horizontal rows by invariant cochains using an unjustified average.

## 7. Why cyclic cohomology is Ext

For functors \(E,F\), \(\operatorname{Ext}^j_\Lambda(E,F)\) means the cohomology of \(\operatorname{Hom}_\Lambda(P_\bullet,F)\) for a projective resolution of \(E\), or equivalently of \(\operatorname{Hom}_\Lambda(E,I^\bullet)\) for an injective resolution of \(F\). These are derived functors in the abelian category of functors, not in the category of algebras.

For the next theorem, \(k\) is a field and \(A\) is a unital \(k\)-algebra. Compose the projective resolution of Theorem 6.2 with \(D^{-1}:\Lambda^{\mathrm{op}}\to\Lambda\). It becomes a resolution \(Q_\bullet\) of the constant **contravariant** functor. Under the bijection \(f\mapsto Df\), its degree-\(q\) terms identify with right representables

\[
Q_q([n])\simeq k[\operatorname{Hom}_\Lambda([n],[q])].
\]

Dualizing at each object gives an injective resolution of the constant covariant functor. To see injectivity directly, let \(Q_q^\vee([n])=\operatorname{Hom}_k(Q_q([n]),k)\). The pairing that evaluates on the identity yields

\[
\operatorname{Hom}_\Lambda(E,Q_q^\vee)
\simeq\operatorname{Hom}_k(E([q]),k).
\tag{7.1}
\]

The right-hand functor is exact because \(k\) is a field. This proves injectivity without a finite-dimensional hypothesis on \(E\). Dualizing the objectwise exact resolution is exact for the same reason. There is no use of an isomorphism between a vector space and its bidual.

**Theorem 7.1.** If \(k\) is a field of characteristic zero, then, naturally in unital \(k\)-algebras,

\[
H_\lambda^j(A)\simeq
\operatorname{Ext}^j_\Lambda(A^\natural,k^\natural).
\tag{7.2}
\]

**Proof.** Apply \(\operatorname{Hom}_\Lambda(A^\natural,-)\) to the injective resolution just constructed. By (7.1), the resulting term at \((p,q)\) is \(C^q(A)\). The integer formula (4.3) gives the maps explicitly. For the injection \(\delta_i:[q-1]\to[q]\), \(D\delta_i\) has its unique two-element fiber at \(i,i+1\) when \(i<q\), and at \(q,0\) in circular order when \(i=q\). Thus the vertical maps are exactly \(b\) in even columns and \(-b'\) in odd columns. Since \(D(r_q^{-1})=r_q\), the horizontal maps are \(1-\lambda_q\) and \(N_q\), alternately.

Lemma 3.1 now computes horizontal cohomology: it vanishes for positive \(p\), and at \(p=0\) it is \(\ker(1-\lambda_q)=C_\lambda^q(A)\). The remaining vertical differential is \(b\). The same finite-filtration argument as in Theorem 6.2 identifies total cohomology with \(H_\lambda^j(A)\). All constructions commute with unital algebra homomorphisms, proving naturality. \(\square\)

For a unital ring \(A\), the expression
\(\operatorname{Ext}^j_\Lambda(A^\natural,\mathbb Z^\natural)\) still defines a derived theory. The preceding injective-resolution proof uses exact linear duality over a field, and its final comparison uses characteristic zero. Neither step can be asserted for an arbitrary ring by leaving the formulas unchanged.

The derived viewpoint also gives bivariant groups \(\operatorname{Ext}^j_\Lambda(A^\natural,B^\natural)\) and their Yoneda composition. It supplies an algebraic bivariant theory; it does not assert an identification with Kasparov's analytic \(KK\)-groups.

## 8. The universal degree-two class

**Theorem 8.1.** For every commutative ring \(R\), the Yoneda algebra of the constant functor is

\[
\operatorname{Ext}^*_\Lambda(R^\natural,R^\natural)
\simeq R[\sigma],\qquad |\sigma|=2.
\tag{8.1}
\]

Multiplication by \(\sigma\) is induced by shifting two columns in the cyclic resolution.

**Proof.** Apply \(\operatorname{Hom}_\Lambda(-,R^\natural)\) to Theorem 6.2. Each position is a copy of \(R\). Every unsigned face and rotation acts as the identity. In an even column, the vertical differential from degree \(q\) to \(q+1\) is zero for even \(q\), and the identity for odd \(q\). In an odd column it is minus the identity for even \(q\), and zero for odd \(q\). Odd columns are acyclic. An even column has cohomology \(R\) in degree zero only.

The vertical-first filtration leaves one copy of \(R\) at \((p,0)\) for each even \(p\) and no other positions. No higher differential can connect two remaining positions. Consequently Ext is \(R\) in every even degree and zero in every odd degree. The cochain equal to \(1\) at \((2j,0)\) and zero elsewhere represents its degree-\(2j\) generator: its vertical differential and its horizontal \(1-T_0\) differential are both zero.

To determine the product, let \(\pi\) be the degree-minus-two chain map on the total projective resolution that sends \(P_{p,q}\) identically to \(P_{p-2,q}\) when \(p\geq2\), and to zero otherwise. Parity is preserved. At \(p=2\), the horizontal boundary lands in a discarded column, exactly as the target has no outgoing horizontal boundary from column zero. Hence \(\pi\) commutes with the total boundary. Composing \(\pi\) with the augmentation represents the degree-two class \(\sigma\).

The chain-map description of the Yoneda product composes lifts of cocycles to maps between projective resolutions. To recall why, a cocycle \(P_d\to F\) induces a map from the \(d\)-th syzygy to \(F\); pulling back the first \(d\) terms of the resolution gives the associated extension. A lift to a resolution of \(F\) makes the iterated pullback for a second extension the splice of the two extensions. Thus composition of lifts represents their Yoneda product; a different lift changes it by a chain homotopy and hence by a coboundary.

Here \(\pi\) is already such a lift. Its \(j\)-fold iterate represents the cochain at \((2j,0)\). Thus \(\sigma^j\) is the generator in every even degree, proving the ring assertion. For coefficients \(E\), precomposing cochains with \(\pi\) shifts them two columns and is Yoneda multiplication by the same class. \(\square\)

In particular, the integral statement is \(\mathbb Z[\sigma]\). It is stronger than merely listing the abelian groups in each degree: the proof identifies their multiplication.

## 9. Hochschild cohomology and the exact couple

For a covariant functor \(E\), let \(K^\bullet(E)\) be the total cochain complex obtained by applying \(\operatorname{Hom}_\Lambda(-,E)\) to Theorem 6.2. The vertical maps in its even columns are \(b\), and in its odd columns are \(-b'\). Horizontal maps are \(D=1-T\) from even columns and \(N\) from odd columns. Here \(T_q=(-1)^qE(r_q^{-1})\); for the dual resolution associated to an algebra the corresponding rotation is the \(\lambda_q\) of (1.1).

The simplicial representables \(R[\operatorname{Hom}_\Delta([q],-)]\), with their alternating face boundary, resolve the constant \(\Delta\)-functor: their value at \([n]\) is the ordered simplex contracted in Theorem 6.2. Thus

\[
H^j(E([0])\xrightarrow b E([1])\xrightarrow b\cdots)
\simeq\operatorname{Ext}^j_\Delta(R^\natural,E|_\Delta).
\tag{9.1}
\]

**Lemma 9.1.** The \(b'\)-complex of a covariant functor is contractible. If \(\sigma_{q-1}:[q]\to[q-1]\) is the simplicial surjection repeating the last vertex, a contraction is

\[
h_q=(-1)^{q-1}E(\sigma_{q-1})\quad(q\geq1),\qquad h_0=0.
\tag{9.2}
\]

**Proof.** In the projective complex, let \(s_q=(-1)^q\) times precomposition by \(\sigma_q\). The face-degeneracy relations give

\[
F_i s_q=-s_{q-1}F_i\quad(0\leq i<q),\qquad
F_qs_q=(-1)^q\mathrm{id}.
\]

Consequently the terms of \(b'_{q+1}s_q+s_{q-1}b'_q\) indexed \(i<q\) cancel, and its last term is the identity. Dualizing by \(\operatorname{Hom}(-,E)\) gives \(b'h+hb'=1\). The case \(q=0\) says \(E(\sigma_0)E(\delta_0)=1\). \(\square\)

**Theorem 9.2.** For every covariant \(\Lambda\)-functor \(E\) over \(R\), there is a natural exact sequence

\[
\cdots\longrightarrow
\operatorname{Ext}^{j-2}_\Lambda(R^\natural,E)
\xrightarrow S\operatorname{Ext}^{j}_\Lambda(R^\natural,E)
\xrightarrow I\operatorname{Ext}^{j}_\Delta(R^\natural,E|_\Delta)
\xrightarrow B\operatorname{Ext}^{j-1}_\Lambda(R^\natural,E)
\xrightarrow S\cdots.
\tag{9.3}
\]

The map \(S\) is multiplication by the class \(\sigma\) of Theorem 8.1; \(I\) is restriction. This sequence is the long exact sequence of the associated exact couple.

**Proof.** Shifting two columns embeds \(K[-2]\) into \(K\), where \(K[-2]^j=K^{j-2}\). Let \(L\) be the quotient consisting of columns zero and one. There is a short exact sequence of cochain complexes

\[
0\longrightarrow K[-2]\xrightarrow S K\longrightarrow L\longrightarrow0.
\tag{9.4}
\]

Projecting \(L\) onto its column-zero complex is a cochain map. Its kernel is the column-one \(-b'\)-complex, placed one degree higher, with the contraction of Lemma 9.1. Hence \(H^j(L)\) identifies with (9.1). The inclusion of simplicial representables into column zero of the cyclic resolution lifts the identity of the constant functor. The resulting map on Hom complexes is projection onto column zero. Thus the map \(I\) just obtained is the derived restriction map.

The long exact sequence of (9.4) is (9.3), and Theorem 8.1 identifies its \(S\) with Yoneda multiplication. For completeness, the connecting map is concrete. If \(x\in E([j])\) satisfies \(bx=0\), put \(y=h_jD_jx\). The relation \(b'D=Db\) and Lemma 9.1 give \(b'y=D_jx\). Thus \((x,y)\), in columns zero and one, is a cocycle of \(L\). Its differential in the full complex has only a column-two component, \(N_{j-1}y\). Undoing the shift gives

\[
Bx=[N_{j-1}h_jD_jx]\quad(j\geq1).
\tag{9.5}
\]

It is a cocycle because \(DN=0\) and \(bN=Nb'\). For \(j=0\), \(B\) is zero. Changing a representative or a lift changes this expression by a coboundary, as follows directly by taking the differential of the changed lift in (9.4). This also proves naturality. \(\square\)

For a unital algebra over a characteristic-zero field, the algebraic cochain bicomplex in Theorem 7.1 has the same two-column argument. Its column-zero cohomology is Hochschild cohomology with coefficients in \(A^*\). Explicitly, identify a multilinear form \(\varphi\) with the map

\[
(a_1,\ldots,a_j)\longmapsto
\bigl(a_0\longmapsto\varphi(a_0,a_1,\ldots,a_j)\bigr).
\]

The dual bimodule has action \((a\cdot f\cdot c)(x)=f(cxa)\). The first Hochschild coefficient term becomes multiplication \(a_0a_1\), and the last becomes \(a_{j+1}a_0\); the middle terms are the products in (1.1). This checks the identification of differentials, not just of vector spaces. Therefore

\[
\cdots\to H_\lambda^{j-2}(A)\xrightarrow S H_\lambda^j(A)
\xrightarrow I HH^j(A,A^*)\xrightarrow B H_\lambda^{j-1}(A)
\xrightarrow S H_\lambda^{j+1}(A)\to\cdots.
\tag{9.6}
\]

This is Connes' cyclic–Hochschild exact sequence. The sign in (9.2) is part of our convention for its connecting map.

## 10. Why the classifying space is the classifying space of the circle

The nerve of a category has a \(j\)-simplex for each composable string of \(j\) arrows. Its geometric realization is its classifying space. We use three facts from algebraic topology: \(\mathbb{CP}^\infty\) is \(K(\mathbb Z,2)\) with cohomology \(\mathbb Z[u]\), \(|u|=2\); a degree-two integral cohomology class on a CW complex is represented by a map to \(K(\mathbb Z,2)\); a homology isomorphism between simply connected CW complexes is a homotopy equivalence. References are [Hatcher 2002, Example 4.50, Theorems 3.19 and 4.57, and Corollary 4.33]. These are the topological background for the following argument.

**Lemma 10.1.** For a small category \(\mathcal C\),

\[
\operatorname{Ext}^*_{\mathcal C}(\mathbb Z^\natural,\mathbb Z^\natural)
\simeq H^*(B\mathcal C;\mathbb Z)
\tag{10.1}
\]

as rings. Its categorical homology with constant coefficients is \(H_*(B\mathcal C;\mathbb Z)\).

**Proof.** A bar resolution of the constant covariant functor has, in degree \(j\), one representable \(\mathbb Z[\operatorname{Hom}_{\mathcal C}(x_j,-)]\) for each string \(x_0\to\cdots\to x_j\). The alternating boundary deletes an end vertex or composes the arrows adjacent to an interior vertex. At an object \(x\), its basis is a string followed by an arrow \(x_j\to x\). This is the nerve chain complex of the category of objects over \(x\). Its terminal object is \(\mathrm{id}_x\). Appending that object, with sign \((-1)^{j+1}\), gives a contraction of the augmented complex: the new last face returns the original string, and the other faces cancel with the contraction of the boundary. The resolution is therefore exact and projective.

Applying Hom into the constant functor makes a degree-\(j\) cochain a function on strings of \(j\) arrows. Its differential is the nerve coboundary. Taking the tensor product over the category with the constant contravariant functor instead gives the nerve chain complex. These may be unnormalized nerve complexes; retaining degenerate simplices computes the same simplicial homology.

The Alexander–Whitney diagonal splits a string at each vertex. On cochains it yields

\[
(\alpha\smile\beta)(x_0\to\cdots\to x_{p+q})
=\alpha(x_0\to\cdots\to x_p)
 \beta(x_p\to\cdots\to x_{p+q}).
\]

Evaluating a degree-\(q\) cocycle on the last \(q\) arrows gives a lift on the bar resolution, retaining the initial string and composing its representable arrow through the remaining arrows. The boundary terms within that initial string commute with the lift; the other terms cancel by the cocycle equation. Composing with a degree-\(p\) cocycle gives the displayed cup formula. Hence the projective-resolution description of the Yoneda product agrees with the nerve cup product. Realizing the nerve gives its CW simplicial chain and cochain theory. This proves (10.1), including the product. \(\square\)

**Theorem 10.2.** There is a homotopy equivalence

\[
B\Lambda\simeq\mathbb{CP}^\infty=BS^1.
\tag{10.2}
\]

Under it, the class \(\sigma\) of Theorem 8.1 can be taken to be the degree-two generator.

**Proof.** All objects have arrows to and from \([0]\), so the nerve is connected. It is also simply connected. To verify this, choose arrows \(u_n:[0]\to[n]\) and \(v_n:[n]\to[0]\). The endomorphism set of \([0]\) consists of the identity, so \(v_nu_n=1\). In the fundamental groupoid of the nerve, the two-simplex of this composite identifies \(v_n\) with \(u_n^{-1}\). For any arrow \(f:[n]\to[m]\), the loop represented by \(v_m f u_n\) is likewise the identity, because its composite is an endomorphism of \([0]\). Every edge loop can be expressed in terms of these loops after transporting its vertices to \([0]\) by the \(u_n\). Thus every loop is trivial.

Lemma 10.1 and Theorem 8.1 give \(H^*(B\Lambda;\mathbb Z)=\mathbb Z[\sigma]\). We also need its integral homology, rather than inferring it merely from this cohomology assertion. Tensor the projective resolution of Theorem 6.2 over \(\Lambda\) with the constant contravariant functor. A representable tensors to \(\mathbb Z\), so every unsigned face and rotation acts as the identity. In each even column the vertical homology is \(\mathbb Z\) in degree zero; an odd column is acyclic. The vertical-first filtration gives

\[
H_{2j}(B\Lambda;\mathbb Z)=\mathbb Z,\qquad
H_{2j+1}(B\Lambda;\mathbb Z)=0.
\]

All these groups are torsion-free. The integral universal coefficient sequence therefore identifies cohomology with the dual of homology in each degree.

Choose \(f:B\Lambda\to K(\mathbb Z,2)=\mathbb{CP}^\infty\) representing \(\sigma\). Then \(f^*u=\sigma\), and hence \(f^*(u^j)=\sigma^j\). These are generators in every even degree by Theorem 8.1. Both spaces have the homology groups just described, so duality shows that \(f_*\) is an isomorphism in every degree. Both are simply connected CW complexes. The homological Whitehead theorem now makes \(f\) a homotopy equivalence. \(\square\)

The tensor calculation also proves

\[
\operatorname{Tor}^{\Lambda}_{2j}(\mathbb Z^\natural,\mathbb Z^\natural)
=\mathbb Z,\qquad
\operatorname{Tor}^{\Lambda}_{2j+1}(\mathbb Z^\natural,\mathbb Z^\natural)=0,
\]

where Tor uses a constant right functor and a constant left functor. Specifying their variance is necessary for a tensor product over a category.

## 11. Exercises with solutions

**Exercise 11.1 (first steps).** Let \(A\) be any associative algebra. Write out \(b\varphi\) for a one-cochain. Explain why an arbitrary antisymmetric bilinear form on \(A\) need not be a cyclic cocycle.

**Solution.**

\[
(b\varphi)(a_0,a_1,a_2)
=\varphi(a_0a_1,a_2)-\varphi(a_0,a_1a_2)+\varphi(a_2a_0,a_1).
\]

Antisymmetry is precisely cyclicity in degree one, but it imposes no derivation rule on products. For a counterexample use \(A=\mathbb C[x]\). On the monomial basis set \(\varphi(x,x^2)=1\), \(\varphi(x^2,x)=-1\), and set all other values to zero. Then
\((b\varphi)(x,x,x)=\varphi(x^2,x)-\varphi(x,x^2)+\varphi(x^2,x)=-3\). \(\square\)

**Exercise 11.2 (a trace with a derivation).** Let \(\tau\) be a trace and \(\delta\) a derivation with \(\tau\delta=0\). Prove directly that \(\tau(a_0\delta(a_1))\) is a cyclic one-cocycle, without assuming \(A\) is commutative.

**Solution.** Since \(0=\tau\delta(a_0a_1)\),

\[
\tau(a_0\delta(a_1))=-\tau(\delta(a_0)a_1)
 =-\tau(a_1\delta(a_0)).
\]

Expanding \(b\varphi\) leaves

\[
-\tau(a_0\delta(a_1)a_2)+\tau(a_2a_0\delta(a_1)),
\]

which is zero by the trace identity. \(\square\)

**Exercise 11.3 (a limit of averaging).** For \(V=\mathbb Z\), \(T=1\) and \(r=3\), compute the positive cohomology of the complex alternating \(1-T\) and \(N\), starting with \(V\xrightarrow{1-T}V\xrightarrow{N}V\).

**Solution.** Its maps are \(0,3,0,3,\ldots\). The degree-one group is \(\ker(3)/\operatorname{im}(0)=0\). The degree-two group is \(\ker(0)/\operatorname{im}(3)=\mathbb Z/3\). Hence the positive odd groups vanish and every positive even group is \(\mathbb Z/3\). Dividing by \(r\) in Lemma 3.1 would incorrectly erase these groups. \(\square\)

**Exercise 11.4 (constant vertex maps).** List the morphisms \([1]\to[0]\) and compute their action on \(A\otimes A\). Explain why the underlying map on the two vertices does not determine a cyclic morphism.

**Solution.** The two lifts can be chosen as \(f(i)=\lfloor i/2\rfloor\) and \(g(i)=\lfloor(i+1)/2\rfloor\). The fiber over zero is respectively \(\{0,1\}\) and \(\{-1,0\}\). Their actions are \(a_0a_1\) and \(a_1a_0\). Both send both vertex residues to the unique target vertex. Their lifts are not equivalent by an output-period translation, so they are distinct morphisms. This distinction matters when \(A\) is noncommutative. \(\square\)

**Exercise 11.5 (self-duality by calculation).** For the first lift \(f\) in Exercise 11.4 compute \(Df\) and \(D^2f\). Check the formula for the square of the duality.

**Solution.** The inequality \(\lfloor i/2\rfloor\geq j\) has least integer solution \(i=2j\), so \(Df(j)=2j\). Consequently \(D^2f(i)=\lceil i/2\rceil\). This equals \(\lfloor(i-1)/2\rfloor+1=f(i-1)+1\). The difference between the two floor/ceiling lifts also shows why calling this particular duality strictly involutive would lose the rotation in (4.4). \(\square\)

**Exercise 11.6 (two-dimensional normalization).** For the cocycle \(\psi\) of Example 2.3 and integers \(r,s,u,v\), evaluate

\[
\psi(e^{-i((r+u)x+(s+v)y)},e^{i(rx+sy)},e^{i(ux+vy)}).
\]

**Solution.** The product of the exponentials is one. The wedge of the two differentials is \(-(rv-su)\,dx\wedge dy\). Dividing its integral by \((2\pi i)^2\) gives \(rv-su\). The determinant changes sign on interchanging the last two inputs, in agreement with the wedge product. \(\square\)

## References

[Khalkhali 2007] Masoud Khalkhali, *Lectures on Noncommutative Geometry*, arXiv:math/0702140, version 2 (2007). [Open lecture notes](https://www.math.uwo.ca/faculty/khalkhali/files/LecturesNCG.pdf).

[Connes 1983] Alain Connes, *Cohomologie cyclique et foncteurs \(\operatorname{Ext}^n\)*, Comptes Rendus de l'Académie des Sciences, Série I, 296 (1983), 953–958. [Author's online text](https://alainconnes.org/wp-content/uploads/n83.pdf).

[Hatcher 2002] Allen Hatcher, *Algebraic Topology*, Cambridge University Press, 2002. [Author's open text](https://pi.math.cornell.edu/~hatcher/AT/ATplain.pdf).
