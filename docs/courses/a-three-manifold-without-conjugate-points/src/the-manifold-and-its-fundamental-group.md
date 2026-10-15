# The manifold and its fundamental group

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson builds the closed three-manifold \(M\) of Theorem 3.1 of [Conjugate points and index forms](conjugate-points-and-index-forms.md) and computes the part of its fundamental group that the obstruction uses. The manifold consists of two pieces \(\Sigma\times S^1\), where \(\Sigma\) is a torus with a hole, joined through a collar \([0,1]\times T^2\). In the fundamental group, each circle factor commutes with everything coming from its piece, each surface boundary is a commutator, and the gluing identifies the boundary classes of the two pieces in a twisted way. A normal form theorem for amalgamated products shows that none of these elements collapses.

- The pieces and the gluing (Section 1).
- Fundamental groups of the pieces (Section 2).
- Normal forms in amalgamated products (Section 3).
- The fundamental group of \(M\) (Section 4).

## 1. The pieces and the gluing

**Tori with a hole.** Let \(c>0\), let \(F_c=\mathbb R^2/(c\mathbb Z)^2\) be the flat torus, \(\pi\colon\mathbb R^2\to F_c\) the quotient map, and \(0<\rho<c/2\). The *torus with a hole* \(\Sigma_{c,\rho}=F_c\setminus\pi(D_\rho)\), where \(D_\rho\) is the open disc of radius \(\rho\) about the origin, is a compact connected orientable surface whose boundary is the circle \(\pi(\partial D_\rho)\). In this lesson a *holed torus* is a compact surface \(\Sigma\) together with a diffeomorphism onto some \(\Sigma_{c,\rho}\), and a *collar* of \(\Sigma\) of period \(B>0\) is an embedding of \((-1,0]\times\mathbb R/B\mathbb Z\) onto a neighbourhood of \(\partial\Sigma\), sending \(\{0\}\times\mathbb R/B\mathbb Z\) onto \(\partial\Sigma\). We write \((\tau,y_1)\) for the collar coordinates. The surfaces of [A concave cometric and convex collars](a-concave-cometric-and-convex-collars.md) are holed tori with collars.

**The gluing data.** Fix \(B_1,B_2>0\), put \(\epsilon=B_1/B_2\), and let
\[
T=\mathbb R^2/\Lambda,\qquad\Lambda=\mathbb ZB_1e_1+\mathbb ZB_2e_2,
\]
where \(e_1,e_2\) is the standard basis. Let \(\Sigma_1,\Sigma_2\) be holed tori with collars of periods \(B_1\) and \(B_2\) respectively, and put
\[
\begin{aligned}
N_1&=\Sigma_1\times\mathbb R/B_2\mathbb Z,\\
N_2&=\Sigma_2\times\mathbb R/B_1\mathbb Z,
\end{aligned}
\]
with circle coordinate \(y_2\). Near its boundary, \(N_i\) has coordinates \((\tau,y_1,y_2)\) with \(\tau\in(-1,0]\). Define the linear maps \(T_1,T_2\colon\mathbb R^2\to\mathbb R^2\) by
\[
\begin{aligned}
T_1y&=y_1e_1+y_2e_2,\\
T_2y&=y_1(e_2+\epsilon e_1)+y_2e_1 .
\end{aligned} \tag{1.1}
\]
\(T_1\) maps \(B_1\mathbb Z\times B_2\mathbb Z\) onto \(\Lambda\). \(T_2\) maps \((B_2m,B_1n)\) to \((m+n)B_1e_1+mB_2e_2\), because \(\epsilon B_2=B_1\); since the integer matrix \(\bigl(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\bigr)\) has determinant \(-1\), \(T_2\) maps \(B_2\mathbb Z\times B_1\mathbb Z\) onto \(\Lambda\). So \(T_1\) induces a diffeomorphism \(\mathbb R/B_1\mathbb Z\times\mathbb R/B_2\mathbb Z\to T\), and \(T_2\) a diffeomorphism \(\mathbb R/B_2\mathbb Z\times\mathbb R/B_1\mathbb Z\to T\).

**The manifold.** Let \(M\) be obtained from \(N_1\), the *neck* \([0,1]\times T\) with coordinates \((t,x)\), and \(N_2\) by identifying a point \((\tau,y)\) of \(\partial N_i\) with the point \((t,x)\) of the neck given by
\[
\begin{aligned}
(t,x)&=(0,T_1y)\quad(i=1),\\
(t,x)&=(1,T_2y)\quad(i=2).
\end{aligned} \tag{1.2}
\]
The collars make \(M\) a smooth manifold: the coordinates \(t=\tau\) on the collar of \(N_1\) and \(t\) on the neck combine into one chart domain \((-1,1)\times T\) with \(x=T_1y\) for \(t\le0\), and likewise \(t=1-\tau\), \(x=T_2y\) near the second torus. In the first case \(\tau\) increases into the neck; in the second, \(\tau=1-t\) does. \(M\) is a union of three compact sets, so it is compact; each point has a neighbourhood in one of the chart domains just described or in the interior of a piece, so \(M\) has no boundary; it is connected. It is Hausdorff: the open sets \(N_1\cup\{t<1/2\}\) and \(N_2\cup\{t>1/2\}\) separate a point of \(N_1\) from a point of \(N_2\), and any other two points lie in one of the manifolds \(N_1\cup\{t<1\}\) and \(N_2\cup\{t>0\}\). We call \(\{0\}\times T\) and \(\{1\}\times T\) the *boundary tori* and \(U=(0,1)\times T\) the *open neck*.

**Orientation.** Orient \(\Sigma_i\) so that \((\partial_\tau,\partial_{y_1})\) is positive in its collar, \(N_i\) by \((\partial_\tau,\partial_{y_1},\partial_{y_2})\), and the neck by \((\partial_t,e_1,e_2)\). At the first torus the identification maps \((\partial_\tau,\partial_{y_1},\partial_{y_2})\) to \((\partial_t,e_1,e_2)\). At the second it maps them to \((-\partial_t,\ e_2+\epsilon e_1,\ e_1)\); the matrix of \((e_2+\epsilon e_1,e_1)\) in the basis \((e_1,e_2)\) has determinant \(-1\), and reversing \(\partial_t\) contributes another sign, so this frame is also positive. The three orientations agree on the overlaps, so **\(M\) is a closed connected orientable smooth three-manifold.**

**Boundary classes.** In \(\partial N_i\), with base point \(\tau=0\), \(y=0\), let \(h_i\) be the loop \(y_1\mapsto(0,y_1,0)\), \(0\le y_1\le B_i\), which runs once along \(\partial\Sigma_i\), and \(f_i\) the loop \(y_2\mapsto(0,0,y_2)\), which runs once along the circle factor. Under (1.2) these loops are the straight loops in \(T\) with displacement vectors
\[
\begin{aligned}
h_1&:\ B_1e_1,\\
f_1&:\ B_2e_2,\\
h_2&:\ B_1e_1+B_2e_2,\\
f_2&:\ B_1e_1 ;
\end{aligned} \tag{1.3}
\]
for \(h_2\) the displacement is \(T_2(B_2,0)=B_2(e_2+\epsilon e_1)\), which equals \(B_1e_1+B_2e_2\) because \(\epsilon B_2=B_1\). In the lattice \(\Lambda\), which is the fundamental group of \(T\) (Section 2), the list (1.3) says \(h_2=h_1+f_1\) and \(f_2=h_1\), the gluing (3.1) of the first lesson.

## 2. Fundamental groups of the pieces

We use the fundamental group of the circle, \(\pi_1(S^1)\cong\mathbb Z\) generated by the loop going once around (Theorem 6 of Roberts's notes in the core course [Algebraic Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D60)), and the gluing theorem for two open sets ([Integral monodromy and the fundamental group, Lemma 3.1](course:CG-S6/CG-S6-06)): if a space is the union of path-connected open sets \(U,V\) with path-connected nonempty intersection, then, with a base point in \(U\cap V\), its fundamental group is generated by the images of \(\pi_1(U)\) and \(\pi_1(V)\), subject exactly to their own relations and to the equality of the two images of every loop in \(U\cap V\).

**Lemma 2.1** (products). For path-connected spaces \(X,Y\), the projections induce an isomorphism from \(\pi_1(X\times Y,(x,y))\) to \(\pi_1(X,x)\times\pi_1(Y,y)\).

*Proof.* A loop in \(X\times Y\) is a pair of loops, and a based homotopy of loops in \(X\times Y\) is a pair of based homotopies. So \([(\alpha,\beta)]\mapsto([\alpha],[\beta])\) is well defined and injective, and it is surjective because any pair of loops forms a loop in the product. \(\square\)

In particular \(\pi_1(T)\cong\mathbb Z^2\), generated by the straight loops with displacements \(B_1e_1\) and \(B_2e_2\); we identify \(\pi_1(T)\) with \(\Lambda\), a straight loop corresponding to its displacement vector.

The *free product* \(G_1*G_2\) of two groups is the group generated by the elements of \(G_1\) and \(G_2\) subject to the relations of \(G_1\) and of \(G_2\); its normal forms are described in Section 3.

**Lemma 2.2** (holed tori). Let \(\Sigma\) be a holed torus and \(p\) a point of \(\Sigma\). Then \(\pi_1(\Sigma,p)\) is a free product \(\langle a\rangle*\langle b\rangle\) of two infinite cyclic groups, and every loop running once along \(\partial\Sigma\), joined to \(p\) by a path, represents a conjugate of \(a^{-1}b^{-1}ab\) or of its inverse.

*Proof.* We may take \(\Sigma=\Sigma_{c,\rho}\), since a diffeomorphism induces an isomorphism of fundamental groups and maps the boundary to the boundary. Let \(Q=[-c/2,c/2]^2\) and \(\|x\|_\infty=\max(|x_1|,|x_2|)\). The map \(H\), defined for \(x\in Q\setminus D_\rho\) and \(0\le s\le1\) by
\[
H(x,s)=(1-s)\,x+s\,\frac{c}{2}\,\frac{x}{\|x\|_\infty},
\]
fixes every point of \(\partial Q\), so it is compatible with the identification of opposite sides of \(Q\) and descends to a deformation retraction of \(\Sigma\) onto \(W=\pi(\partial Q)\); the quotient map \(Q\setminus D_\rho\to\Sigma\) is closed, so the descended map is continuous. The set \(W\) is the union of two circles \(a=\pi([-c/2,c/2]\times\{c/2\})\) and \(b=\pi(\{c/2\}\times[-c/2,c/2])\), oriented by \(e_1\) and \(e_2\), which meet at the single point \(w=\pi(c/2,c/2)\).

Remove from \(W\) one point of \(b\) other than \(w\) to obtain \(U_W\), and one point of \(a\) other than \(w\) to obtain \(V_W\). Then \(U_W\) deformation retracts onto the circle \(a\), \(V_W\) onto \(b\), and \(U_W\cap V_W\) is a union of four arcs meeting at \(w\), which is contractible. The gluing theorem gives \(\pi_1(W,w)=\langle a\rangle*\langle b\rangle\), each factor infinite cyclic. Since \(\Sigma\) deformation retracts onto \(W\), the inclusion induces \(\pi_1(W,w)\cong\pi_1(\Sigma,w)\), and changing the base point to \(p\) along a path is an isomorphism.

The boundary circle \(u\mapsto\rho(\cos2\pi u,\sin2\pi u)\) is homotopic through \(H\) to the loop that runs once counterclockwise around \(\partial Q\). Starting at the corner \((c/2,c/2)\) this loop runs along the top side in direction \(-e_1\), the left side in direction \(-e_2\), the bottom side in direction \(e_1\) and the right side in direction \(e_2\); after the identifications it is the based loop \(a^{-1}b^{-1}ab\). A free homotopy of loops changes based classes by conjugation by the path traced by the base point, and reversing the direction of the boundary circle inverts the class. \(\square\)

So for each piece \(N_i=\Sigma_i\times S^1\) of Section 1, with base point \(q_i\) at \(\tau=0\), \(y=0\), Lemmas 2.1 and 2.2 give
\[
\begin{aligned}
G_i&:=\pi_1(N_i,q_i)\\
&\cong\bigl(\langle a_i\rangle*\langle b_i\rangle\bigr)\times\langle f_i\rangle,
\end{aligned} \tag{2.1}
\]
in which \(f_i\) generates the second factor and the boundary class \(h_i\) lies in the first factor and is conjugate there to \((a_i^{-1}b_i^{-1}a_ib_i)^{\pm1}\). In particular, with \(Z(G_i)\) the centre of \(G_i\),
\[
\begin{aligned}
&f_i\in Z(G_i),\\
&h_i\in[G_i,G_i],
\end{aligned} \tag{2.2}
\]
because a conjugate of a commutator is a commutator.

## 3. Normal forms in amalgamated products

Let \(A\) be a group and \(\iota_k\colon A\to G_k\) injective homomorphisms, \(k=1,2\); we identify \(A\) with its images. The *amalgamated product* \(P=G_1*_AG_2\) is the group generated by the elements of \(G_1\) and of \(G_2\), subject to the relations of \(G_1\), the relations of \(G_2\), and \(\iota_1(a)=\iota_2(a)\) for \(a\in A\). By construction, homomorphisms \(\phi_k\colon G_k\to H\) that agree on \(A\) extend to a unique homomorphism \(P\to H\). For \(A=\{1\}\) this is the free product.

For \(k=1,2\) choose a set \(S_k\subseteq G_k\) of representatives of the right cosets \(Ag\), \(g\in G_k\), with \(1\in S_k\) representing \(A\). A *normal form* is a sequence \((a;s_1,\dots,s_n)\) with \(a\in A\), \(n\ge0\), each \(s_j\in S_{k_j}\setminus\{1\}\), and \(k_j\ne k_{j+1}\) for \(1\le j<n\). Let \(\Omega\) be the set of normal forms.

**Theorem 3.1** (normal forms). Every element of \(P\) equals \(a\,s_1s_2\cdots s_n\) for exactly one normal form \((a;s_1,\dots,s_n)\).

*Proof.* *Existence.* The set of elements of \(P\) that are products \(as_1\cdots s_n\) of a normal form contains \(1\) and is stable under left multiplication by every \(g\in G_k\): if \(n=0\) or \(k_1\ne k\), write \(ga=a's\) with \(a'\in A\), \(s\in S_k\), so that \(g\,as_1\cdots s_n=a'ss_1\cdots s_n\), where \(s\) is dropped if \(s=1\); if \(k_1=k\), write \(gas_1=a's\) instead, so that the product becomes \(a'ss_2\cdots s_n\). In each case the result is the product of a normal form. Since \(P\) is generated by \(G_1\cup G_2\), every element is such a product.

*Uniqueness.* Fix \(k\), and let \(\Omega_k'\) be the set of sequences \((s_1,\dots,s_n)\) that occur in normal forms with \(n=0\) or \(k_1\ne k\). The map
\[
\begin{aligned}
&\Theta_k\colon G_k\times\Omega_k'\to\Omega,\\
&\Theta_k(g,(s_1,\dots,s_n))\\
&\quad=\begin{cases}(a;s,s_1,\dots,s_n),&s\ne1,\\ (a;s_1,\dots,s_n),&s=1,\end{cases}
\end{aligned}
\]
where \(g=as\) with \(a\in A\) and \(s\in S_k\), is a bijection: a normal form \((a;t_1,\dots,t_m)\) is \(\Theta_k(at_1,(t_2,\dots,t_m))\) if \(m\ge1\) and \(k_1=k\), and \(\Theta_k(a,(t_1,\dots,t_m))\) otherwise, and these are the only preimages. Left multiplication on the first factor therefore defines an action of \(G_k\) on \(\Omega\): \(g'\cdot\Theta_k(g,\sigma)=\Theta_k(g'g,\sigma)\). For \(b\in A\), both actions send \((a;s_1,\dots,s_n)\) to \((ba;s_1,\dots,s_n)\), because \(b\,as\) decomposes as \((ba)\,s\). By the universal property they combine into an action of \(P\) on \(\Omega\).

Let \(p=as_1\cdots s_n\) for a normal form. By induction from the right,
\[
\begin{aligned}
&s_j\cdot(1;s_{j+1},\dots,s_n)\\
&\quad=\Theta_{k_j}(s_j,(s_{j+1},\dots,s_n))\\
&\quad=(1;s_j,\dots,s_n),
\end{aligned}
\]
because \((1;s_{j+1},\dots,s_n)=\Theta_{k_j}(1,(s_{j+1},\dots,s_n))\) as \(k_{j+1}\ne k_j\); finally \(a\cdot(1;s_1,\dots,s_n)=(a;s_1,\dots,s_n)\). So \(p\cdot(1;\,)=(a;s_1,\dots,s_n)\), and the normal form is determined by \(p\). \(\square\)

**Corollary 3.2.** (1) Each \(G_k\to P\) is injective. (2) If \(n\ge1\) and \(g_1,\dots,g_n\) lie alternately in \(G_1\setminus A\) and \(G_2\setminus A\), then \(g_1\cdots g_n\notin A\); in particular \(g_1\cdots g_n\ne1\).

*Proof.* (1) For \(g=as\in G_k\), the normal form of its image is \((a;s)\), or \((a;\,)\) if \(s=1\); if the image is \(1\), uniqueness gives \(a=1\), \(s=1\). (2) By induction on \(n\) the normal form of \(g_1\cdots g_n\) has exactly \(n\) letters \(s_j\), the first in the factor of \(g_1\): for \(n=1\) because \(g_1\notin A\); for the step, if \(g_2\cdots g_n=a's_2\cdots s_n\) with \(s_2\) in the other factor, then \(g_1a'\notin A\), so \(g_1a'=a''s\) with \(s\ne1\), and \(g_1\cdots g_n=a''ss_2\cdots s_n\). Elements of \(A\) have normal forms without letters. \(\square\)

**Corollary 3.3.** In \(\langle a\rangle*\langle b\rangle\) with \(a,b\) of infinite order, \((a^{-1}b^{-1}ab)^m\ne1\) for every \(m\ne0\). Hence every conjugate of \(a^{-1}b^{-1}ab\) has infinite order.

*Proof.* For \(m>0\) the power is the alternating product of \(4m\) factors \(a^{-1},b^{-1},a,b,\dots\), none equal to \(1\); apply Corollary 3.2(2) with \(A=\{1\}\). For \(m<0\) take inverses. \(\square\)

## 4. The fundamental group of \(M\)

**Proposition 4.1.** Let \(\Gamma=\pi_1(M,x_*)\) with \(x_*=(1/2,0)\) in the neck, and transport the classes of Section 2 to \(x_*\) along the segments \(t\mapsto(t,0)\). Then:

1. \(\Gamma=G_1*_\Lambda G_2\), where \(\Lambda=\pi_1(T)\) maps to \(G_1\) by \(B_1e_1\mapsto h_1\), \(B_2e_2\mapsto f_1\), and to \(G_2\) by \(B_1e_1+B_2e_2\mapsto h_2\), \(B_1e_1\mapsto f_2\); both maps are injective.
2. \(G_1\) and \(G_2\) embed in \(\Gamma\). In \(\Gamma\),
\[
\begin{aligned}
h_1f_1&=f_1h_1,\\
f_2&=h_1,\\
h_2&=h_1f_1,
\end{aligned} \tag{4.1}
\]
and \(h_1\), \(f_1\) generate a subgroup isomorphic to \(\mathbb Z^2\); in particular they have infinite order.
3. For \(i=1,2\), let \(C_\Gamma(f_i)\) be the centralizer of \(f_i\) in \(\Gamma\). Then \(G_i\subseteq C_\Gamma(f_i)\) and \(h_i\) lies in the commutator subgroup \([C_\Gamma(f_i),C_\Gamma(f_i)]\).

*Proof.* (1) Let \(U'\) be the union of \(N_1\) and \(\{t<2/3\}\), and \(V'\) the union of \(N_2\) and \(\{t>1/3\}\). They are open and path connected, and \(U'\cap V'=(1/3,2/3)\times T\) is path connected and contains \(x_*\). The neck part of \(U'\) retracts onto \(\{0\}\times T=\partial N_1\) along \(t\), so \(U'\) deformation retracts onto \(N_1\), and \(\pi_1(U',x_*)\cong G_1\) through the segment from \(x_*\) to \(q_1\); likewise for \(V'\). A straight loop in \(\{1/2\}\times T\) with displacement \(v\in\Lambda\) is homotopic, by moving it along \(t\), to the straight loop with the same displacement in a boundary torus, which by (1.3) is \(h_1^mf_1^n\) for \(v=mB_1e_1+nB_2e_2\) in the first torus and \(h_2^mf_2^n\) for \(v=m(B_1e_1+B_2e_2)+nB_1e_1\) in the second. The gluing theorem therefore presents \(\Gamma\) as \(G_1*_\Lambda G_2\) with the stated maps. The map \(\Lambda\to G_1\) sends \(mB_1e_1+nB_2e_2\) to \((h_1^m,f_1^n)\) in the decomposition (2.1); it is injective because \(h_1\) has infinite order by Corollary 3.3. The same argument applies to \(G_2\), since \((B_1e_1+B_2e_2,B_1e_1)\) is also a basis of \(\Lambda\).

(2) The embeddings are Corollary 3.2(1). The relations (4.1) are the identifications of (1). The subgroup generated by \(h_1,f_1\) is the image of \(\Lambda\), which embeds.

(3) By (2.2), \(f_i\) commutes with every element of \(G_i\), so \(G_i\subseteq C_\Gamma(f_i)\), and \(h_i\in[G_i,G_i]\subseteq[C_\Gamma(f_i),C_\Gamma(f_i)]\). \(\square\)

These are all the properties of \(M\) used by the obstruction in [Axes, shifts and the two-piece obstruction](axes-shifts-and-the-two-piece-obstruction.md). They do not depend on \(B_1\), \(B_2\) or on the particular holed tori. The manifold is a graph manifold with two Seifert pieces, and the gluing is an instance of the examples of Leeb [Leeb, Section 4.1, Example 4.1]; Ivanov and Kapovitch ask about such gluings in [IK, Section 8].

## 5. Exercises

**5.1.** Show directly that the matrix of \(T_2\) relative to the bases \((B_2e_1,B_1e_2)\) of \(B_2\mathbb Z\times B_1\mathbb Z\) and \((B_1e_1,B_2e_2)\) of \(\Lambda\) is \(\bigl(\begin{smallmatrix}1&1\\1&0\end{smallmatrix}\bigr)\).

**5.2.** Show that the centre of \(\langle a\rangle*\langle b\rangle\) is trivial, and deduce that the centre of \(G_i\) in (2.1) is \(\langle f_i\rangle\).

**5.3.** Compute the abelianization of \(\Gamma\) and show that \(h_1\), \(f_1\), \(h_2\) and \(f_2\) all map to \(0\) in it. Conclude that their infinite order cannot be detected by a homomorphism to an abelian group.

**5.4.** Show that \(G_1*_AG_2\) is generated by \(G_1\cup G_2\) and that, in Corollary 3.2(2), the hypothesis that the factors alternate cannot be dropped.

**5.5.** Show that the frame \((-\partial_t,\ e_2+\epsilon e_1,\ e_1)\) is positive for the orientation \((\partial_t,e_1,e_2)\) of the neck, and that the frame \((-\partial_t,\ e_1,\ e_2+\epsilon e_1)\) is not.

## 6. Solutions

**5.1.** \(T_2(B_2,0)=B_2e_2+\epsilon B_2e_1\), which is \(B_1e_1+B_2e_2\), and \(T_2(0,B_1)=B_1e_1\), so the columns are \((1,1)\) and \((1,0)\).

**5.2.** Here \(A=\{1\}\) and the letters of a normal form are nontrivial elements of \(\langle a\rangle\) and \(\langle b\rangle\), alternating. Let \(z=s_1\cdots s_n\) with \(n\ge1\), and suppose \(s_1\in\langle a\rangle\). Then \(bz\) has a normal form with \(n+1\) letters beginning with \(b\). If \(s_n\in\langle a\rangle\), then \(zb\) has \(n+1\) letters beginning with \(s_1\in\langle a\rangle\); if \(s_n\in\langle b\rangle\), then \(zb\) has \(n\) letters if \(s_nb\ne1\) and \(n-1\) letters if \(s_nb=1\). In every case \(zb\ne bz\) by uniqueness of normal forms. If \(s_1\in\langle b\rangle\), use \(a\) instead. So the centre is trivial. In the product (2.1), \((u,f^m)\) is central exactly when \(u\) is central in the free product, so the centre is \(\langle f_i\rangle\).

**5.3.** \(G_i^{\rm ab}=\mathbb Z^3\) with basis \(a_i,b_i,f_i\), and \(h_i\mapsto0\). The relations \(f_2=h_1\) and \(h_2=h_1f_1\) give \(f_2=0\) and \(f_1=0\) in the abelianization, so \(\Gamma^{\rm ab}\cong\mathbb Z^4\) with basis \(a_1,b_1,a_2,b_2\), and all four classes vanish.

**5.4.** Every generator of the presentation lies in \(G_1\cup G_2\). The product \(g\,g^{-1}\) with \(g\in G_1\setminus A\) is \(1\).

**5.5.** In the coordinates \((t,x_1,x_2)\) the first frame has the columns \((-1,0,0)\), \((0,\epsilon,1)\), \((0,1,0)\), with determinant \(-1\cdot(\epsilon\cdot0-1\cdot1)=1>0\). The second has the columns \((-1,0,0)\), \((0,1,0)\), \((0,\epsilon,1)\), with determinant \(-1\cdot1=-1<0\).

## References

- [OpenAI-NC] OpenAI, *A Three-Manifold Without Conjugate Points and Without a Nonpositively Curved Metric*, OpenAI Math Release preprint, 24 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/A-Three-Manifold-Without-Conjugate-Points-and-Without-a-Nonpositively-Curved-Metric-September-24-2026
- [Leeb] B. Leeb, *3-manifolds with(out) metrics of nonpositive curvature*, arXiv:dg-ga/9410002, Section 4.1, Example 4.1. https://arxiv.org/abs/dg-ga/9410002
- [IK] S. Ivanov and V. Kapovitch, *Manifolds without conjugate points and their fundamental groups*, arXiv:1205.4455, Section 8. https://arxiv.org/abs/1205.4455
- D. M. Roberts, *Algebraic Topology*, lecture notes, 2019 (core course Algebraic Topology), Theorem 6. https://github.com/DavidMichaelRoberts/AlgebraicTopology2019
