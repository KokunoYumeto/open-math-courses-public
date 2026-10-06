# Idempotents, projections and their equivalences

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

An idempotent records a direct-sum decomposition. A projection records one with an orthogonal complement. Operator K-theory begins by deciding when two such decompositions describe the same object. There are several answers: compare their ranges algebraically, change coordinates, or deform one continuously into the other. These answers differ in a fixed algebra. They agree once we allow extra zero matrix blocks.

We develop the distinction before using stabilization to remove it. We also give two practical constructions: an explicit projection associated to an idempotent, and an exact idempotent associated to an approximate one. The latter explains why small errors in multiplication can be repaired.

We assume Functional Analysis, [Banach algebras, spectrum, holomorphic functional calculus and Gelfand theory][BN], and [C*-algebras: continuous functional calculus, automatic continuity, positive cones, approximate identities and quotients][CF]. The precise background facts used without proof are listed near the end. The freely accessible equivalence comparison is [Blackadar 1998, §§4.1–4.6]; [AF-algebras] supplies the exact background stated below.

## 1. Decompositions and the matrix setting

Unless stated otherwise, \(A\) is a nonzero complex unital Banach algebra. We use a submultiplicative norm with \(\|1\|=1\). An equivalent such norm exists by [Banach algebras, Proposition 3.1][BN]. Estimates always refer to the chosen norm. The zero algebra has only the zero idempotent and can be treated separately.

An **idempotent** is an element \(e\) satisfying \(e^2=e\). On any module on which \(e\) acts, a vector \(\xi\) splits as

\[
\xi=e\xi+(1-e)\xi,\qquad e(1-e)=(1-e)e=0.
\]

Thus \(e\) selects one summand and \(1-e\) the other. In a C*-algebra a **projection** is an idempotent with \(e=e^*\). For projections acting on a Hilbert space the two summands are orthogonal.

The algebra \(M_n(A)\) consists of \(n\)-by-\(n\) matrices with entries in \(A\). In the Banach case we choose a submultiplicative complete norm equivalent to the maximum of the entry norms, normalized at the identity. In the C*-case we use its C*-norm. The embeddings

\[
M_n(A)\longrightarrow M_{n+1}(A),\qquad a\longmapsto
\begin{pmatrix}a&0\\0&0\end{pmatrix}
\]

preserve multiplication but do not preserve the identities. Their algebraic union \(M_\infty(A)\) consists of matrices with finitely many nonzero entries. It is not a completed matrix algebra. All homotopies in this lesson take place in one specified finite matrix algebra; a homotopy after stabilization means that such a finite stage exists.

The **orthogonal sum** is \(e\oplus f=\operatorname{diag}(e,f)\). Its square is \(\operatorname{diag}(e^2,f^2)\), so it is an idempotent whenever \(e,f\) are. Even when \(e,f\) are not self-adjoint, the two block summands annihilate each other. For projections their sum is a projection.

For any algebra, including an already unital one, we fix the **external unitization**

\[
A^+=A\oplus\mathbb C,\qquad
(a,\lambda)(b,\mu)=(ab+\lambda b+\mu a,\lambda\mu).
\]

Its new identity is \((0,1)\), its augmentation is \(\epsilon(a,\lambda)=\lambda\), and \(A\) embeds as the ideal \(A\oplus0\). For Banach algebras the sum norm gives a Banach algebra. For C*-algebras we use the C*-unitization norm. If \(A\) already has identity \(1_A\), the map \((a,\lambda)\mapsto(a+\lambda1_A,\lambda)\) identifies \(A^+\) with the product C*-algebra \(A\times\mathbb C\); the norm is then \(\max(\|a+\lambda1_A\|,|\lambda|)\). These background constructions are [Banach algebras, Construction 3.2 and Propositions 3.3–3.4][BN].

When \(A\) is nonunital, complements, invertible conjugators and unitaries are taken in \(A^+\). The idempotents and their homotopies remain in \(A\). Matrix complements use the identity of the ambient \(M_n(A^+)\).

## 2. Changing coordinates and following a deformation

**Definition 2.1.** For idempotents in a common unital algebra, write

\[
\begin{aligned}
e\sim_a f&\quad\text{if }e=xy,\ f=yx\text{ for some }x,y,\\
e\sim_s f&\quad\text{if }f=zez^{-1}\text{ for some invertible }z,\\
e\sim_h f&\quad\text{if a norm-continuous idempotent path joins }e\text{ to }f.
\end{aligned}
\]

In a nonunital algebra the witnesses \(x,y\) are in \(A\) and the similarity is implemented in \(A^+\). Algebraic equivalence compares the selected summands. Similarity compares both selected and complementary summands. Homotopy adds a condition on the continuous change of coordinates.

**Lemma 2.2.** Algebraic witnesses can be chosen with

\[
x=exf,\qquad y=fye.
\]

Similarity implies algebraic equivalence.

**Proof.** Start with \(xy=e,\ yx=f\). Associativity gives \(ex=xf\) and \(fy=ye\). Replacing the witnesses by \(x'=exf\), \(y'=fye\) gives

\[
x'y'=exfye=e(xyxy)e=e^4=e,\qquad
y'x'=fyexf=f(yxyx)f=f^4=f.
\]

The required corner identities follow by multiplying by \(e\) or \(f\). If \(f=zez^{-1}\), take \(x=ez^{-1}\), \(y=ze\); then \(xy=e\), \(yx=f\). In the nonunital case these witnesses lie in the ideal \(A\). \(\square\)

**Theorem 2.3 (Nearby idempotents).** If

\[
\|e-f\|<\frac1{\|2e-1\|},
\]

then

\[
z=ef+(1-e)(1-f)
\]

is invertible, \(ez=zf\), and \(f=z^{-1}ez\). Moreover \(z\) is connected to \(1\) through invertibles.

**Proof.** Expand rather than commute factors:

\[
z=1-e-f+2ef,\qquad
z-1=(2e-1)(f-e),\qquad ez=ef=zf.
\]

The hypothesis gives \(\|z-1\|<1\), so the Neumann-series criterion makes \(z\) invertible. The same criterion applies to \(z_t=1+t(z-1)\), since \(\|z_t-1\|<1\) for \(0\leq t\leq1\). Hence \(z_t^{-1}ez_t\) is an idempotent path from \(e\) to \(f\). \(\square\)

The factor \(\|2e-1\|\) matters: idempotents need not have norm one. The formula also gives a continuous local choice of conjugator in the direction \(e\mapsto f\), namely \(w_e(f)=z^{-1}\).

**Theorem 2.4 (Homotopy and the identity component).** Two idempotents are homotopic if and only if they are conjugate by an element of \(\mathrm{GL}(A)_0\), the connected component of \(1\) in the invertible group.

**Proof.** Small balls in \(\mathrm{GL}(A)\) are path-connected: near an invertible \(g\), write an element as \(g(1+h)\) with \(\|h\|<1\), and use \(g(1+th)\). Therefore the invertible group is locally path-connected; its connected components are its path components. A path \(g_t\) from \(1\) to \(g\) gives the idempotent path \(g_teg_t^{-1}\).

Conversely, let \(e_t\) be an idempotent path with \(e_0=e\). Compactness gives a bound \(K\geq\|2e_t-1\|\) for all \(t\). Choose a partition \(0=t_0<\cdots<t_m=1\) fine enough that \(\|e_t-e_{t_i}\|<1/K\) on each subinterval. Define

\[
z_i(t)=e_{t_i}e_t+(1-e_{t_i})(1-e_t).
\]

It starts at \(1\), stays invertible, and satisfies \(z_i(t)^{-1}e_{t_i}z_i(t)=e_t\). Set \(Z_0=1\) and, successively,

\[
Z(t)=Z_i z_i(t)\quad(t_i\leq t\leq t_{i+1}),\qquad
Z_{i+1}=Z_i z_i(t_{i+1}).
\]

The pieces match. Induction gives \(Z(t)^{-1}eZ(t)=e_t\); indeed the inverse of \(Z_i z_i(t)\) is \(z_i(t)^{-1}Z_i^{-1}\). Thus \(Z(1)^{-1}\in\mathrm{GL}(A)_0\) implements the desired conjugation. The order of these products is essential. \(\square\)

**Corollary 2.5 (Orbits).** The set \(\operatorname{Idem}(A)\) is closed. Each similarity class is both open and closed in it. Its path components are precisely the conjugation orbits of \(\mathrm{GL}(A)_0\).

**Proof.** The map \(a\mapsto a^2-a\) is continuous, so its zero set is closed. Theorem 2.3 supplies a relative neighbourhood of every idempotent inside its similarity class. Every other class is open as well, so the complement of any one class is open. The last assertion is Theorem 2.4. \(\square\)

An open and closed similarity class may contain several path components. Local deformation and unrestricted coordinate change are different questions.

**Proposition 2.6 (The complementary summand).** Idempotents \(e,f\) are similar if and only if \(e\sim_a f\) and \(1-e\sim_a1-f\).

**Proof.** Similarity conjugates both the idempotent and its complement; apply Lemma 2.2 to each. Conversely take normalized witnesses \(xy=e,\ yx=f\) and \(ab=1-e,\ ba=1-f\). The corner conditions make \(xb=ay=ya=bx=0\). Thus \(z=x+a\) has inverse \(y+b\), since their products are \(e+(1-e)=1\) and \(f+(1-f)=1\). Also \(ez=x=zf\). Consequently \(zfz^{-1}=e\), or \(z^{-1}ez=f\). \(\square\)

## 3. Why an extra block removes the difference

**Theorem 3.1 (Algebraic equivalence after stabilization).** Suppose \(e=xy,\ f=yx\), with \(x=exf,\ y=fye\). Put

\[
Z=\begin{pmatrix}x&1-e\\1-f&y\end{pmatrix},\qquad
W=\begin{pmatrix}y&1-f\\1-e&x\end{pmatrix}.
\]

Then \(ZW=WZ=1\) and \(Z(f\oplus0)Z^{-1}=e\oplus0\). Also \(e\oplus0\) and \(f\oplus0\) are homotopic in \(M_2(A)\).

**Proof.** The four entries of \(ZW\) are

\[
xy+(1-e)^2=1,\quad x(1-f)+(1-e)x=0,\quad
(1-f)y+y(1-e)=0,\quad (1-f)^2+yx=1.
\]

Those of \(WZ\) are, respectively,

\[
yx+(1-f)^2=1,\quad y(1-e)+(1-f)y=0,\quad
(1-e)x+x(1-f)=0,\quad (1-e)^2+xy=1.
\]

Finally,

\[
Z(f\oplus0)=\begin{pmatrix}x&0\\0&0\end{pmatrix}
=(e\oplus0)Z,
\]

which proves the conjugation identity.

For a homotopy in the same two-block algebra, write \(c=\cos\theta,\ s=\sin\theta\), and set

\[
E_\theta=\begin{pmatrix}c^2e&csx\\csy&s^2f\end{pmatrix},\qquad
0\leq\theta\leq\frac\pi2.
\]

The entries of its square are

\[
c^4e+c^2s^2xy=c^2e,\quad c^3sex+cs^3xf=csx,
\]
\[
c^3sye+cs^3fy=csy,\quad c^2s^2yx+s^4f=s^2f.
\]

Thus the path joins \(e\oplus0\) to \(0\oplus f\). Now conjugate \(0\oplus f\) by the scalar rotation

\[
R_\theta=\begin{pmatrix}c&-s\\s&c\end{pmatrix}.
\]

Its inverse is \(\begin{pmatrix}c&s\\-s&c\end{pmatrix}\); in both orders their products have entries \(c^2+s^2,0,0,c^2+s^2\). Entrywise multiplication gives

\[
R_\theta(0\oplus f)R_\theta^{-1}
=\begin{pmatrix}s^2f&-scf\\-scf&c^2f\end{pmatrix},
\]

a path from \(0\oplus f\) to \(f\oplus0\). Concatenate the paths. For nonunital \(A\), all entries of both idempotent paths remain in \(A\), while the conjugators are in its unitization. \(\square\)

**Theorem 3.2 (A rotation for similar idempotents).** If \(f=zez^{-1}\), then \(e\oplus0\sim_h f\oplus0\) in \(M_2(A)\).

**Proof.** Here is a direct coordinate-change path, useful beyond this theorem:

\[
H_\theta=\operatorname{diag}(z,1)\,R_\theta\,
 \operatorname{diag}(1,z^{-1})\,R_\theta^{-1}.
\]

Every factor is invertible. Multiplying the four entries gives

\[
H_\theta=\begin{pmatrix}
c^2z+s^2&cs(z-1)\\cs(1-z^{-1})&s^2+c^2z^{-1}
\end{pmatrix}.
\]

It joins \(\operatorname{diag}(z,z^{-1})\) at \(\theta=0\) to \(1\) at \(\theta=\pi/2\). Reversing it and conjugating \(e\oplus0\) gives a path ending at \(f\oplus0\). If \(z\) is unitary, every \(H_\theta\) is unitary. \(\square\)

**Corollary 3.3.** In a fixed algebra,

\[
e\sim_h f\ \Longrightarrow\ e\sim_s f\ \Longrightarrow\ e\sim_a f.
\]

For \(e,f\in M_n(A)\), algebraic equivalence implies that \(e\oplus0_n\) and \(f\oplus0_n\) are both similar and homotopic in \(M_{2n}(A)\). Consequently the three relations agree on \(M_\infty(A)\) when similarity and homotopy are allowed in a larger finite stage.

There is no assumption about a topology on an infinite matrix completion in this assertion. Conversely, algebraic equivalence in a larger finite stage can be compressed to the common original stage: corner-normalized witnesses \(x=exf,\ y=fye\) have no entries outside that stage. Algebraic equivalence is unchanged by adding zeros.

The addition of classes by block sum gives the monoid used later for \(K_0\). In the C*-case we use the existing notation \(V(A)\) from [AF-algebras, Definition 7.4][AF]; we do not need its AF-specific dimension-group theory here.

## 4. Replacing idempotents by projections

Let \(A\) now be a C*-algebra. An element \(v\) with \(v^*v=p,\ vv^*=q\) for projections \(p,q\) is a **partial isometry from \(p\) to \(q\)**. We write \(p\sim q\) for this Murray–von Neumann equivalence, and \(p\sim_u q\) if \(q=upu^*\) for a unitary in the ambient unital algebra.

The identities \(v=vp=qv\) follow from the C*-identity. For example,

\[
\|v(1-p)\|^2=\|(1-p)v^*v(1-p)\|=0;
\]

the corresponding computation with \((1-q)v\) gives the other identity.

**Theorem 4.1 (The range projection).** For any idempotent \(e\), set

\[
D=1+(e-e^*)(e^*-e)=1-(e-e^*)^2,\qquad P(e)=ee^*D^{-1}.
\]

Then \(P(e)\) is a projection, \(eP(e)=P(e)\), and \(P(e)e=e\). The invertible element \(1+e-P(e)\) conjugates \(e\) to \(P(e)\), and \(e\) is homotopic to \(P(e)\). The map \(P\) is continuous and fixes every projection.

**Proof.** The element \(D=1+(e-e^*)(e-e^*)^*\) is positive and at least \(1\), hence invertible. Expanding gives

\[
D=1-e-e^*+ee^*+e^*e,\qquad
De=eD=ee^*e.
\]

Taking adjoints shows that \(D\) also commutes with \(e^*\). Consequently \(ee^*D^{-1}\) is self-adjoint. Since \((ee^*)^2=Dee^*\), its square equals itself:

\[
P(e)^2=(ee^*)^2D^{-2}=ee^*D^{-1}=P(e).
\]

Also \(eP(e)=P(e)\) and \(P(e)e=ee^*eD^{-1}=DeD^{-1}=e\).

Put \(p=P(e)\), \(n=e-p\). The four terms in

\[
n^2=e^2-ep-pe+p^2=e-p-e+p=0
\]

show that \(1+tn\) has inverse \(1-tn\). Since \(ne=0\) and \(en=n\),

\[
(1+tn)e(1-tn)=e-tn=(1-t)e+tp.
\]

This proves both the conjugation formula and a homotopy already inside \(A\). Continuity follows from continuity of multiplication, involution and inversion. If \(e=p=p^*\), then \(D=1\) and \(P(p)=p\). \(\square\)

In a representation on a Hilbert space, \(ep=p\) and \(pe=e\) imply that \(e\) and \(p\) have the same range. This explains the name without requiring a polar decomposition in a larger operator algebra.

**Theorem 4.2 (Relations for projections).** Algebraic equivalence of projections is Murray–von Neumann equivalence. Similarity of projections is unitary equivalence. Two projections are homotopic as idempotents if and only if a projection path joins them; equivalently, they are conjugate by a unitary in \(U(A)_0\). Unitization is understood for nonunital \(A\).

**Proof.** If \(v^*v=p,\ vv^*=q\), take \(x=v^*,y=v\) to obtain algebraic witnesses. Conversely normalize \(p=xy,\ q=yx\), with \(x=pxq,\ y=qyp\). If \(p=0\), the corner identities give \(x=y=q=0\). Otherwise

\[
p=(xy)^*(xy)=y^*x^*xy\leq\|x\|^2y^*y.
\]

Thus \(y^*y\) is positive and invertible in the unital corner \(pAp\). Let \(h=(y^*y)^{-1/2}\) in that corner and \(v=yh\). Then \(v^*v=p\) and \(qv=v\). The projection \(r=vv^*\) satisfies

\[
ry=yh^2y^*y=y,\qquad rq=ryx=yx=q.
\]

On the other hand \(qr=r\), and taking adjoints gives \(rq=r\). Hence \(r=q\).

If \(q=zpz^{-1}\), then \(zp=qz\) and \(pz^*=z^*q\). These give

\[
pz^*z=z^*qz=z^*zp.
\]

Continuous functional calculus makes \((z^*z)^{-1/2}\) commute with \(p\). Therefore

\[
u=z(z^*z)^{-1/2}
\]

is unitary and \(up=qu\). Here \(u^*u=1\), and \(u\) is invertible, so \(uu^*=1\). The converse is immediate.

For a path of idempotents \(e_t\) with projection endpoints, Theorem 4.1 makes \(P(e_t)\) a projection path with the same endpoints. Apply Theorem 2.4 to this path to obtain an invertible path \(z_t\), starting at \(1\), with \(z_tpz_t^{-1}=P(e_t)\). Taking the polar unitaries \(u_t=z_t(z_t^*z_t)^{-1/2}\) gives a continuous unitary path with the same conjugations and \(u_0=1\). Continuity uses continuous functional calculus on positive invertibles. Conversely a unitary path produces a projection path by conjugation.

Unitary path components are open: if \(u,w\) are sufficiently close unitaries, the segment \((1-t)u+tw\) is invertible, and its polar unitaries give a path from \(u\) to \(w\). Thus connected and path components of the unitary group agree, justifying the notation \(U(A)_0\). \(\square\)

**Theorem 4.3 (Stable projection equivalence).** If \(p\sim q\), then \(p\oplus0\) and \(q\oplus0\) are unitarily equivalent and homotopic through projections in \(M_2(A^+)\), with the projection path contained in \(M_2(A)\).

**Proof.** The unitary

\[
U=\begin{pmatrix}v&1-q\\1-p&v^*\end{pmatrix}
\]

implements the equivalence; all entries of \(UU^*\), \(U^*U\), and the conjugation are computed in Exercise 3. For the homotopy use Theorem 3.1 with \(e=p,\ f=q,\ x=v^*,y=v\). Its path

\[
\begin{pmatrix}c^2p&csv^*\\csv&s^2q\end{pmatrix}
\]

is self-adjoint as well as idempotent. Its second rotation path is also self-adjoint. \(\square\)

We will use the following existing result without another proof: if \(\|p-q\|<1\), then \(p\sim_u q\), by [AF-algebras, Lemma 7.1][AF]. Its hypotheses concern arbitrary C*-algebras, not just AF-algebras. The projection version of the bound has radius \(1\) because \(2p-1\) is a self-adjoint unitary. Theorems 2.3 and 4.2 also show that such projections are homotopic.

## 5. Examples that separate the relations

**Example 5.1 (An oblique decomposition).** In \(M_2(\mathbb C)\), let

\[
e_t=\begin{pmatrix}1&t\\0&0\end{pmatrix},\qquad t\in\mathbb C.
\]

Its square equals itself. It is self-adjoint exactly when \(t=0\). The path \(e_{st}\), \(0\leq s\leq1\), joins \(e_0\) to \(e_t\); the change of coordinates

\[
\begin{pmatrix}1&-t\\0&1\end{pmatrix}
\begin{pmatrix}1&0\\0&0\end{pmatrix}
\begin{pmatrix}1&t\\0&1\end{pmatrix}
=e_t
\]

also proves similarity. The range-projection formula gives

\[
(e_t-e_t^*)^2=-|t|^2I,\quad
e_te_t^*=\begin{pmatrix}1+|t|^2&0\\0&0\end{pmatrix},\quad
P(e_t)=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]

**Example 5.2 (Losing one direction).** On \(H=\ell^2(\mathbb N)\), let \(S\) be the shift \(S\xi_j=\xi_{j+1}\). Then \(S^*S=1\) and \(SS^*=1-P_0\), where \(P_0\) projects onto \(\mathbb C\xi_0\). Thus \(1\sim SS^*\) in \(B(H)\). But conjugation by any invertible, in particular by any unitary, fixes \(1\); since \(SS^*\neq1\), these projections are neither similar nor homotopic. Explicitly,

\[
\begin{pmatrix}S&P_0\\0&S^*\end{pmatrix}
\]

is a unitary conjugating \(1\oplus0\) to \(SS^*\oplus0\), by Theorem 4.3.

**Example 5.3 (Topology inside one similarity class).** There exist similar idempotents in \(M_2(C(S^3))\) which are not homotopic as idempotents. Blackadar [1998, §4.4] records this phenomenon. This is a forward illustration, not an input to the projection or stabilization proofs above. The construction and obstruction proof are [Topological K-theory, Proposition 4.2](KT-OPK-12.md#an-explicit-unstable-projection-example): an explicit two-by-two unitary on the three-sphere conjugates a constant rank-one projection to a projection with no projection or idempotent homotopy back to it.

It also supplies a projection example, with no further topological assertion needed. Choose such idempotents \(e,f\), and set \(p=P(e),q=P(f)\). They are similar by transitivity and Theorem 4.1, hence unitarily equivalent by Theorem 4.2. If \(p,q\) had a projection homotopy, concatenate it with the homotopies \(e\sim_h p\) and \(q\sim_h f\), contradicting the choice of \(e,f\).

Consequently, for projections in a fixed algebra the complete implication pattern is

\[
\sim_h\ \Longrightarrow\ (\sim_s\ \Longleftrightarrow\ \sim_u)
\ \Longrightarrow\ (\sim_a\ \Longleftrightarrow\ \sim).
\]

Example 5.2 disproves every implication from the rightmost pair to either of the preceding groups. Example 5.3 disproves the implication from the middle pair to homotopy. Transitivity supplies every other forward implication. After stabilization, all five relations coincide.

**Example 5.4 (Scalar functions).** For compact Hausdorff \(X\), an idempotent \(f\in C(X)\) has values in \(\{0,1\}\); continuity makes \(U=f^{-1}(1)\) clopen. Conversely \(1_U\) is a continuous idempotent for every clopen \(U\). In a commutative algebra algebraic witnesses obey \(xy=yx\), so algebraically equivalent scalar idempotents are equal. A scalar idempotent homotopy also stays constant pointwise, since a continuous path in \(\{0,1\}\) is constant. In \(C_0(\mathbb R)\), connectedness makes an idempotent constant and vanishing at infinity rules out the constant \(1\). Hence its only idempotent is \(0\).

**Example 5.5 (The Bott projection).** On \(S^2=\{(a,b,c):a^2+b^2+c^2=1\}\), put

\[
B(a,b,c)=\frac12
\begin{pmatrix}1+c&a-ib\\a+ib&1-c\end{pmatrix}.
\]

The four entries of \(4B^2\) are \(2(1+c),\,2(a-ib),\,2(a+ib),\,2(1-c)\); here \(a^2+b^2=1-c^2\). Thus \(B=B^*=B^2\). It has rank one at every point, but \(B\not\sim\operatorname{diag}(1,0)\).

To prove this last assertion, on the northern and southern closed hemispheres choose unit sections of its range:

\[
n=\frac{(1+c,a+ib)^T}{\sqrt{2(1+c)}},\qquad
s=\frac{(a-ib,1-c)^T}{\sqrt{2(1-c)}}.
\]

Their denominators do not vanish on their respective hemispheres. The entries of \(nn^*\) are

\[
\frac{1+c}{2},\quad\frac{a-ib}{2},\quad
\frac{a+ib}{2},\quad\frac{a^2+b^2}{2(1+c)}=\frac{1-c}{2}.
\]

Those of \(ss^*\) are

\[
\frac{a^2+b^2}{2(1-c)}=\frac{1+c}{2},\quad
\frac{a-ib}{2},\quad\frac{a+ib}{2},\quad\frac{1-c}{2}.
\]

Thus both products equal \(B\) wherever defined. On the equator \(a+ib=e^{i\phi}\), they satisfy \(n=e^{i\phi}s\).

An equivalence with \(\operatorname{diag}(1,0)\) would supply a continuous unit vector \(w\) in the range of \(B\): take the first column of the implementing partial isometry. Write \(w=n\alpha_N=s\alpha_S\) on the two hemispheres, where \(\alpha_N,\alpha_S\) are continuous circle-valued functions. Their equatorial loops satisfy

\[
\alpha_S(e^{i\phi})=e^{i\phi}\alpha_N(e^{i\phi}).
\]

Each loop extends over a disk, so each has winding number zero. Their winding numbers therefore cannot differ by one.

For completeness, the elementary winding facts needed here follow by choosing a continuous argument for a loop on successive short intervals. The total argument change divided by \(2\pi\) is an integer; multiplication adds these integers. A sufficiently small uniform perturbation has the same integer, since its quotient with the original loop has a continuous argument of total change zero. Subdivide a homotopy into such perturbations to get invariance. A disk extension contracts its boundary loop radially to a constant, whose integer is zero, whereas \(e^{i\phi}\) has integer one. This proves the obstruction. \(\square\)

Thus pointwise rank does not classify continuous matrix-valued projections. The lessons on vector bundles and on topological K-theory develop what the varying ranges retain.

## 6. Repairing an approximate idempotent

Let \(\delta=x^2-x\) and \(\eta=\|\delta\|\). The useful threshold is \(1/4\), because on the line \(\operatorname{Re}\lambda=1/2\),

\[
\left|\lambda^2-\lambda\right|=\frac14+(\operatorname{Im}\lambda)^2.
\]

**Theorem 6.1 (Riesz correction with a quantitative bound).** If \(\eta<1/4\), the spectrum of \(x\) misses that line. Let \(\chi\) be the holomorphic function which is \(0\) near the part of the spectrum in the left half-plane and \(1\) near the part in the right half-plane. Then \(p=\chi(x)\) is an idempotent, and, with \(r=\sqrt{1-4\eta}\),

\[
\|p-x\|\leq
\frac{2(2\|x\|+1)}{r(1+r)}\,\eta.
\tag{6.1}
\]

In particular, if \(\eta\leq1/8\), then

\[
\|p-x\|\leq2(2\|x\|+1)\eta.
\tag{6.2}
\]

It lies in any subalgebra containing \(x\) and closed under holomorphic functional calculus in \(A\).

**Proof.** Spectral mapping gives \(|\lambda^2-\lambda|\leq\eta\) for \(\lambda\in\sigma(x)\). This excludes the displayed line. The two spectral pieces are compact and separated, so the function \(\chi\) is holomorphic on their disjoint neighbourhoods. Since \(\chi^2=\chi\), the calculus gives \(p^2=p\). Equivalently \(p\) is the Riesz integral

\[
p=\frac1{2\pi i}\int_{\Gamma_1}(\lambda-x)^{-1}\,d\lambda,
\]

where a surrounding cycle has index one on the right spectral piece and zero on the left.

For the estimate, put \(a=2x-1\), so \(a^2=1+4\delta\). The norm-convergent binomial series

\[
T=(1+4\delta)^{-1/2}
=\sum_{k=0}^{\infty}(-1)^k\binom{2k}{k}\delta^k
\]

commutes with \(a\) and satisfies \(a^2T^2=1\). Hence \((1+aT)/2\) is idempotent. It is precisely \(p\): for a spectral value \(\lambda\), the principal square root of \((2\lambda-1)^2=1+4(\lambda^2-\lambda)\) equals \(2\lambda-1\) in the right half-plane and its negative in the left. The scalar formula \((1+(2\lambda-1)/\sqrt{1+4(\lambda^2-\lambda)})/2\) therefore agrees with \(\chi\) on a neighbourhood of the spectrum, and the composition property of the calculus gives the asserted equality.

The series majorant yields

\[
\|T-1\|\leq\sum_{k\geq1}\binom{2k}{k}\eta^k
=(1-4\eta)^{-1/2}-1=\frac{4\eta}{r(1+r)}.
\]

Since \(p-x=a(T-1)/2\) and \(\|a\|\leq2\|x\|+1\), this is (6.1). For \(\eta\leq1/8\), \(r\geq1/\sqrt2\) and \(r(1+r)\geq1\), giving (6.2). Closure under the calculus gives the subalgebra assertion. For a nonunital subalgebra, apply its external unitization and use \(\chi(0)=0\), so the result has zero augmentation. \(\square\)

**Example 6.2 (Why a margin is necessary).** A constant depending only on \(\|x\|\) cannot work uniformly for every \(\eta<1/4\). In \(M_2(\mathbb C)\) with the maximum row-sum norm take

\[
x_t=\begin{pmatrix}\frac12+t&\frac12-t\\0&\frac12-t\end{pmatrix},
\qquad 0<t<\frac12.
\]

Here \(\|x_t\|=1\), and direct multiplication gives \(x_t^2-x_t=-(1/4-t^2)I\). The Riesz correction is

\[
p_t=\frac{x_t-(\frac12-t)I}{2t}
=\begin{pmatrix}1&\dfrac{\frac12-t}{2t}\\0&0\end{pmatrix}.
\]

Its upper-right entry diverges as \(t\downarrow0\), so \(\|p_t-x_t\|\) is unbounded while \(\|x_t\|=1\) and \(\|x_t^2-x_t\|<1/4\). Formula (6.1) states the estimate on the entire permitted interval; formula (6.2) gives the uniform small-error estimate.

For example, if \(x\to e\) for an exact idempotent \(e\), then

\[
\|x^2-x\|\leq(\|x\|+\|e\|+1)\|x-e\|\longrightarrow0.
\]

The corrected idempotents approach \(e\), and Theorem 2.3 eventually makes them similar to \(e\). If the approximants lie in a subalgebra closed under the calculus, so do their corrections. This is the local mechanism later used for continuity and dense subalgebras.

## 7. Exercises with complete solutions

**Exercise 1 (Basic).** Check \(ZW=1,\ WZ=1\), and \(Z(f\oplus0)=(e\oplus0)Z\) in Theorem 3.1. Prove that \(\sim_a\) is an equivalence relation on the idempotents of \(M_\infty(A)\).

**Solution.** The eight entries of the two products and the four entries of the intertwining identity are displayed in Theorem 3.1; each zero follows from \(ex=x=xf,\ fy=y=ye\), and each diagonal identity uses \(xy=e,\ yx=f\).

For reflexivity take \(x=y=e\). Symmetry exchanges the two witnesses. For transitivity work in a common finite stage and normalize witnesses for \(e=xy,\ f=yx=ab,\ g=ba\), with \(x=exf,\ y=fye,\ a=fag,\ b=gbf\). Then

\[
(xa)(by)=x(ab)y=xfy=xy=e,\qquad
(by)(xa)=b(yx)a=bfa=ba=g.
\]

This proves transitivity, and adding zero corners puts any finite collection of witnesses in a common stage.

**Exercise 2 (Basic).** Show that Murray–von Neumann equivalence and unitary equivalence coincide in a finite-dimensional C*-algebra.

**Solution.** By [AF-algebras, Theorem 2.4][AF], the algebra is a finite direct sum \(\bigoplus_jM_{d_j}(\mathbb C)\). A partial isometry from \(p_j\) to \(q_j\) is an isometric bijection of their ranges, so the ranks agree in each summand. Choose orthonormal bases of each range and its orthogonal complement. The complements also have equal dimension, namely \(d_j-\operatorname{rank}p_j\). Sending these two pairs of bases to their counterparts gives a unitary \(u_j\) with \(u_jp_ju_j^*=q_j\). The tuple \((u_j)_j\) is the required unitary. Conversely \(q=upu^*\) gives the partial isometry \(v=up\). The zero algebra is immediate.

**Exercise 3 (Intermediate).** For \(v^*v=p,\ vv^*=q\), verify that

\[
U=\begin{pmatrix}v&1-q\\1-p&v^*\end{pmatrix}
\]

is unitary and \(U(p\oplus0)U^*=q\oplus0\). Determine whether it must be self-adjoint.

**Solution.** The adjoint is

\[
U^*=\begin{pmatrix}v^*&1-p\\1-q&v\end{pmatrix}.
\]

The four entries of \(UU^*\) are

\[
vv^*+(1-q)^2=1,\quad v(1-p)+(1-q)v=0,
\]
\[
(1-p)v^*+v^*(1-q)=0,\quad (1-p)^2+v^*v=1.
\]

The four entries of \(U^*U\) are

\[
v^*v+(1-p)^2=1,\quad v^*(1-q)+(1-p)v^*=0,
\]
\[
(1-q)v+v(1-p)=0,\quad (1-q)^2+vv^*=1.
\]

Moreover \(U(p\oplus0)=\begin{pmatrix}v&0\\0&0\end{pmatrix}\), whose product with \(U^*\) has entries \(q,0,0,0\), because \(v(1-p)=0\). Self-adjointness fails even in \(\mathbb C\): take \(v=i,\ p=q=1\); then \(U=\operatorname{diag}(i,-i)\). Thus the matrix is a unitary, but need not be a self-adjoint unitary.

**Exercise 4 (Intermediate).** Prove that the idempotents form a closed set and that every similarity class is relatively open.

**Solution.** If \(e_n\to e\) and \(e_n^2=e_n\), then

\[
\|e_n^2-e^2\|\leq(\|e_n\|+\|e\|)\|e_n-e\|\longrightarrow0,
\]

so \(e^2=e\). For a fixed idempotent \(e\), every idempotent in the ball of radius \(\|2e-1\|^{-1}\) around it is similar to it by Theorem 2.3. Apply the same argument at each member of the class. This is openness in the set of idempotents, not openness in the whole algebra. Its relative complement is a union of open classes, proving relative closedness too.

**Exercise 5 (Advanced).** In the Toeplitz algebra \(\mathcal T=C^*(S)\), show that \(1\) and \(SS^*\) are algebraically equivalent but not similar. Find the least \(n\geq0\) for which \(\operatorname{diag}(1,0_n)\) and \(\operatorname{diag}(SS^*,0_n)\) are similar.

**Solution.** Take \(x=S^*,y=S\). Then \(xy=1\) and \(yx=SS^*=1-P_0\neq1\). Any invertible conjugation fixes the identity, so similarity fails for \(n=0\). Since \(P_0=1-SS^*\in\mathcal T\), the matrix

\[
U=\begin{pmatrix}S&P_0\\0&S^*\end{pmatrix}\in M_2(\mathcal T)
\]

belongs to the algebra. Its products with \(U^*\) have diagonal entries \(SS^*+P_0=1,\ S^*S=1\) in one order and \(S^*S=1,\ P_0+SS^*=1\) in the other; the off-diagonal entries vanish because \(P_0S=0,\ S^*P_0=0\). Also \(U(1\oplus0)U^*=SS^*\oplus0\). Hence \(n=1\) works and is least. No quotient description of the Toeplitz algebra or index theorem is needed.

## What this lesson does not prove

The general analytic background is used in the following exact forms:

- The Neumann-series criterion: \(\|h\|<1\) implies that \(1-h\) is invertible. The equivalent normalization of a unital Banach-algebra norm and the external-unitization construction are also assumed. See [Banach algebras, Sections 2–3][BN].
- Holomorphic functional calculus is a unital homomorphism, obeys spectral mapping and composition, and evaluates functions defined near separated spectral pieces by surrounding-cycle integrals. See [Banach algebras, Definition 6.4, Theorem 6.7, Theorem 6.10 and Example 6.12][BN].
- Continuous functional calculus for a normal element is an isometric unital *-homomorphism with spectral mapping, commutation, and composition properties. The inverse square root depends continuously on a positive invertible element. See [C*-algebras, Theorems 5.1 and 6.1][CF].
- Positive elements form a closed cone; \(x^*x\geq0\), \(x^*x\leq\|x\|^2 1\), order is preserved by \(a\mapsto c^*ac\), and a positive element at least \(\varepsilon1\), with \(\varepsilon>0\), is invertible. Positive square roots exist. See [C*-algebras, Theorem 8.2 and Proposition 8.5][CF], also [Blackadar 2006, II.3.1.2–II.3.1.9].
- Projections of distance less than \(1\) are unitarily equivalent in the unitization; finite-dimensional C*-algebras are finite direct sums of full matrix algebras. See [AF-algebras, Lemma 7.1 and Theorem 2.4][AF]. The definition of \(V(A)\) is [AF-algebras, Definition 7.4][AF].
- The full construction for Example 5.3 in \(M_2(C(S^3))\) is [Topological K-theory, Proposition 4.2](KT-OPK-12.md#an-explicit-unstable-projection-example), using the projection retraction and stable homotopy proved above together with the suspension and Bott results developed in that lesson. Blackadar [1998, §4.4] retains credit for the qualitative example. The range-replacement deduction of a projection counterexample is also proved here.

The Grothendieck-group construction, projective-module classification and Bott periodicity are subjects of subsequent lessons. The Bott projection's non-equivalence in Example 5.5 uses only the elementary winding argument supplied there.

## References

- [Banach algebras] *Banach algebras, spectrum, holomorphic functional calculus and Gelfand theory*, in the open course *Foundations of von Neumann algebras*.
- [C*-algebras] *C*-algebras: continuous functional calculus, automatic continuity, positive cones, approximate identities and quotients*, in the open course *Foundations of von Neumann algebras*.
- [AF-algebras] *AF-algebras*, in the open course *Foundations of von Neumann algebras*.
- [Blackadar 1998] B. Blackadar, *K-Theory for Operator Algebras*, second edition, MSRI Publications 5, Cambridge University Press, 1998. [Author's corrected second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf). Sections 4.1–4.6, especially Propositions 4.2.2, 4.2.5, 4.3.1–4.3.3, 4.4.1 and 4.6.2–4.6.7, printed pp. 20–24 (PDF pp. 34–38), give the corner and stable-equivalence comparisons. The complete finite-matrix proofs and quantitative correction bound are written in this lesson; Example 5.3 uses the explicit obstruction proof in Lesson 12, Proposition 4.2.
- [Blackadar 2006] B. Blackadar, *Operator Algebras: Theory of C*-Algebras and von Neumann Algebras*, Encyclopaedia of Mathematical Sciences 122, Springer, 2006.
- [Emerson 2024] H. Emerson, *An Introduction to C*-Algebras and Noncommutative Geometry*, Birkhäuser Advanced Texts, 2024.

[BN]: https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/banach-algebras-spectrum-holomorphic-functional-calculus-and-gelfand-theory.html
[CF]: https://kokunoyumeto.github.io/open-math-courses-public/courses/NCG-FOLIATIONS/companions/c-star-algebras-continuous-functional-calculus-automatic-continuity-positive-cones.html
[AF]: https://kokunoyumeto.github.io/open-math-courses-public/courses/NCG-FOLIATIONS/companions/af-algebras.html
[AF-algebras]: https://kokunoyumeto.github.io/open-math-courses-public/courses/NCG-FOLIATIONS/companions/af-algebras.html
