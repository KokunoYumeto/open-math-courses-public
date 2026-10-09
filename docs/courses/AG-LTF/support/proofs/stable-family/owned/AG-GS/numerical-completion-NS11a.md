# Numerical types, weighted chains and the semistable-reduction bound

Independent teaching exposition, CC0 1.0. AI author: GPT-6.1 Sol, Ultra. Includes the AG-GS numerical completion NS.11a by GPT-6.1 Sol, Ultra, with its complete numerical inputs. Self-checked by the writing AI.

The mathematical references are the Stacks project authors' results on [numerical types](https://stacks.math.columbia.edu/tag/0C7C), [connected rational subgraphs](https://stacks.math.columbia.edu/tag/0C8Q), [bounds on the heart](https://stacks.math.columbia.edu/tag/0C9V), [the constant 768](https://stacks.math.columbia.edu/tag/0C9W), and [numerical Picard torsion](https://stacks.math.columbia.edu/tag/0C9X). The proofs below establish the statements used in the stable-family argument, including both orientations of the weighted chains and the fork.

<a id="n-matrix"></a>

## N.1. The matrix and its positive kernel

A numerical type, as defined in [Stacks 0C6Z](https://stacks.math.columbia.edu/tag/0C6Z), consists of a finite connected graph on vertices \(1,\ldots,n\), positive integers \(m_i,w_i\), integers \(g_i\ge0\), and a symmetric integral matrix \(A=(a_{ij})\). An edge \(ij\) is present exactly when \(i\ne j\) and \(a_{ij}>0\); other off-diagonal entries vanish. The requirements are
\[
 Am=0,\qquad w_i\mid a_{ij}\quad\text{for every }i,j.
\tag{N.1}
\]
Define the numerical genus and the graph genus by
\[
 g=1+\sum_i m_i\left(w_i(g_i-1)-\frac{a_{ii}}2\right),
 \qquad b=e-n+1,
\tag{N.2}
\]
where \(e\) counts unordered edges, without counting their weights. A spanning tree gives \(b\ge0\).

For any real vector \(z\), the row equations in (N.1) yield the identity
\[
 -z^{\mathsf t}Az
 =\sum_{i<j}a_{ij}m_im_j
       \left(\frac{z_i}{m_i}-\frac{z_j}{m_j}\right)^2.
\tag{N.3}
\]
This is the negative-definiteness calculation corresponding to [Stacks 0C5X](https://stacks.math.columbia.edu/tag/0C5X). Expand the right side: the coefficient of \(z_i^2\) is
\(\sum_{j\ne i}a_{ij}m_j/m_i=-a_{ii}\), and the mixed coefficient is \(-2a_{ij}\). Thus (N.3) follows directly. Connectedness implies that equality occurs exactly for \(z=qm\). Consequently \(A\) has rank \(n-1\), with kernel \(\mathbf Qm\) over \(\mathbf Q\), and every principal matrix on a nonempty proper vertex set is negative definite. Indeed, extend a vector on that set by zero; equality in (N.3) would make it a multiple of the everywhere positive vector \(m\), hence zero.

If \(n>1\), each vertex has a neighbour and
\[
 -a_{ii}m_i=\sum_{j\ne i}a_{ij}m_j>0.
\tag{N.4}
\]
In particular, all diagonal entries are negative. The genus in (N.2) is integral: reducing \(m^{\mathsf t}Am=0\) modulo two gives
\(\sum_i a_{ii}m_i\equiv\sum_i a_{ii}m_i^2\equiv0\pmod2\).

Call a vertex exceptional when \(g_i=0\) and \(a_{ii}=-w_i\). The type is minimal when it has no exceptional vertex. For a minimal type with \(n>1\), put
\[
 \Phi_i=m_i\left(w_i(g_i-1)-a_{ii}/2\right).
\]
Since \(-a_{ii}/w_i\) is a positive integer, \(\Phi_i\ge0\); it vanishes precisely when \(g_i=0\) and \(a_{ii}=-2w_i\). These will be called rational \((-2)\)-vertices. It follows that a minimal type with several vertices has \(g\ge1\). If every vertex is a rational \((-2)\)-vertex, then every summand vanishes and **\(g=1\)**. This also applies when the matrix on the full graph is singular. The one-vertex case has \(A=0\) and \(g=1+m_1w_1(g_1-1)\).

<a id="n-genus"></a>

## N.2. Why the graph genus cannot exceed the numerical genus

For a minimal type with \(n>1\), we prove \(b\le g\), the result of [Stacks 0C7C](https://stacks.math.columbia.edu/tag/0C7C). Let \(d_i\) be the ordinary graph degree, \(q_i=\sum_{j\ne i}a_{ij}/w_i\), and \(x_i=m_iw_i\). Summing (N.4) and using symmetry expresses the difference as
\[
 g-b=\sum_i\Psi_i,\qquad
 \Psi_i=x_i(g_i-1+q_i/2)+1-d_i/2.
\tag{N.5}
\]
Here \(q_i\ge d_i\). The only negative terms are rational leaves with \(q_i=1\) and \(x_i>1\); for such a leaf \(i\), \(\Psi_i=(1-x_i)/2\). Indeed, if \(g_i-1+q_i/2\ge0\), multiplying by \(x_i\ge1\) and comparing with \(-1+d_i/2\) gives \(\Psi_i\ge0\). A negative value inside the parentheses requires \(g_i=0,q_i=1\), and connectedness then gives \(d_i=1\).

If \(b=0\), the inequality follows already from \(g\ge1\). Suppose \(b>0\). Starting at each negative leaf, follow the unique path through rational vertices of degree two whose two incident edges both equal their vertex weight. These degree-two vertices have \(\Psi=0\). The path must end at a vertex \(k\) outside this class and outside the negative leaves: a path ending at another such leaf would constitute the entire connected graph and have \(b=0\). Interiors of these paths are disjoint.

The edge weight is constant along each of these paths, including its last edge to \(k\); denote it by \(c\). Minimality at the initial leaf gives \(m_{\mathrm{next}}\ge2m_{\mathrm{leaf}}\). At every interior vertex, its equation is
\(\kappa m_j=m_{\mathrm{prev}}+m_{\mathrm{next}}\) for an integer \(\kappa\ge2\). The positive initial increase in multiplicity therefore persists along the path. In particular,
\[
 m_k\ge2m_{\mathrm{leaf}}.
\tag{N.6}
\]

Group all \(t\ge1\) paths ending at a fixed \(k\). Write \(r\) for its number of other neighbours, \(\rho_s=c_s/w_k\ge1\) for the integral weight ratio of path \(s\), and \(Q\) for the sum of the ratios \(a_{kj}/w_k\) on the other edges. Since \(b>0\), \(r\ge1\): otherwise the entire graph would be the union of the paths and their common endpoint, a tree. Adding the negative leaf terms to \(\Psi_k\) gives exactly
\[
 E_k=x_k(g_k-1)+\frac12\sum_{s=1}^t
           (x_k\rho_s-x_{\mathrm{leaf},s})
       +\frac{x_kQ}{2}+1-\frac r2.
\tag{N.7}
\]
By (N.6), \(x_{\mathrm{leaf},s}\le x_k\rho_s/2\); also \(Q\ge r\). If \(t\ge2\), or if some \(\rho_s\ge2\), these estimates give
\[
 E_k\ge x_k(r-1)/2+1-r/2\ge1/2.
\]
For the remaining possibility \(t=1,\rho_1=1\), they give
\(E_k\ge x_k(g_k-3/4+Q/2)+1-r/2\).
This is nonnegative if \(g_k\ge1\), or \(r\ge2\), or \(Q\ge2\). The only case left is \(g_k=0,r=1,Q=1\); it would make \(k\) another degree-two vertex of the class through which the path was continued, contrary to the stopping rule. All grouped terms are nonnegative, and every ungrouped \(\Psi_i\) is nonnegative. This proves \(g-b\ge0\).

<a id="n-heart"></a>

## N.3. The heart and the first bound on a neighbour

Assume the type is minimal, \(g\ge2\), and \(n>1\). Let \(J\) consist of the vertices that are not rational \((-2)\)-vertices. These are exactly the positive contributions to \(g-1=\sum\Phi_i\); each contribution is a positive half-integer. Thus
\[
 0<|J|\le2g-2.
\tag{N.8}
\]
For \(j\in J\), the strict inequality \(\Phi_j>m_jw_j(g_j-1)\) gives \(g_j<g\). If \(g_j\ge1\), then \(\Phi_j\ge m_j|a_{jj}|/2\). If \(g_j=0\), write \(-a_{jj}=kw_j\) with \(k\ge3\); then
\[
 m_j|a_{jj}|=\frac{2k}{k-2}\Phi_j\le6\Phi_j.
\]
Both cases prove
\[
 m_j|a_{jj}|\le6(g-1)\quad(j\in J).
\tag{N.9}
\]
Whenever \(a_{ij}>0\), taking one summand from (N.4) and using \(a_{ij}\ge w_i\) gives
\[
 m_i a_{ij}\le m_j|a_{jj}|,\qquad
 m_iw_i\le m_j|a_{jj}|.
\tag{N.10}
\]
These are the heart and neighbour results of [Stacks 0C9V](https://stacks.math.columbia.edu/tag/0C9V) and [0C9U](https://stacks.math.columbia.edu/tag/0C9U). A rational \((-2)\)-vertex meeting \(J\) therefore satisfies \(m_iw_i\le6(g-1)\).

<a id="n-classification"></a>

## N.4. Enumerating the connected rational subgraphs

Let \(I\) be a connected proper set of rational \((-2)\)-vertices. Write \(W=\operatorname{diag}(w_i:i\in I)\) and
\[
 H=-W^{-1/2}A_IW^{-1/2}.
\]
By (N.3), \(H\) is positive definite. Its diagonal is two. At an edge its off-diagonal entry is \(-\sqrt{r_{ij}}\), where
\[
 r_{ij}=\frac{a_{ij}^2}{w_iw_j}
       =\frac{a_{ij}}{w_i}\frac{a_{ij}}{w_j}
       \in\{1,2,3\}.
\tag{N.11}
\]
Integrality follows from the two divisibilities; the upper limit follows from the determinant of the corresponding two-vertex principal matrix. An edge with \(r=1\) has equal endpoint weights and edge weight equal to that common value. For \(r=2\) or \(3\), the endpoint weights differ by that factor and the edge weight equals the larger endpoint weight.

We give the finite enumeration needed for [Stacks 0C8Q](https://stacks.math.columbia.edu/tag/0C8Q). It uses only positive definiteness and the preceding three possible edge entries.

The graph has no cycle: put the value one on the vertices of a cycle and zero elsewhere. The quadratic form is at most \(2s-2s=0\) for a cycle of length \(s\). A vertex of degree at least four is also impossible. On that vertex and four neighbours, assign the central value two and the four neighbouring values one. For ordinary edges the quadratic form is zero; larger or additional edges only lower it. These test vectors contradict positive definiteness.

There cannot be two trivalent vertices. Choose a shortest path between two of them and one vertex on each of their two branches away from the path. Give every path vertex value two and the four end leaves value one. With ordinary edges the matrix annihilates this vector, and larger edge entries again make its quadratic value nonpositive.

An edge with \(r>1\) will be called heavy. There cannot be two heavy edges. Take the path between them, retaining their two outer endpoints. Replace both heavy entries by \(-\sqrt2\); give the outer endpoints value \(\sqrt2\) and every intervening vertex value two. The resulting principal matrix annihilates the vector. Increasing either heavy entry to \(-\sqrt3\) gives a negative quadratic value. A heavy edge and a trivalent vertex are likewise incompatible: take the path from the vertex to the heavy edge, retain two additional neighbours of the trivalent vertex, and assign values two along the path, one to those two neighbours, and \(\sqrt2\) to the outer endpoint of the heavy edge. This gives zero for a double edge, and a nonpositive value for a triple edge.

Thus a graph containing a heavy edge is a path with exactly one such edge. A triple edge cannot have an adjacent edge: the determinant of a three-vertex path with squared entries three and one is \(2(4-3-1)=0\). Its graph therefore has two vertices. For a double edge, let \(p,q\) count the vertices on its two sides, including its endpoints. The ordinary path matrix of size \(p\) has determinant \(p+1\) and its endpoint entry in the inverse is \(p/(p+1)\). Both formulas follow from the recurrence \(D_t=2D_{t-1}-D_{t-2}\), with \(D_0=1,D_1=2\), and the cofactor formula. The Schur complement across the double edge is positive exactly when
\[
 1-\frac{2pq}{(p+1)(q+1)}>0
 \quad\Longleftrightarrow\quad (p-1)(q-1)<2.
\tag{N.12}
\]
Hence either the double edge is terminal, with arbitrary path length and either orientation of the weight ratio, or \(p=q=2\), giving a four-vertex path with its double edge in the middle.

It remains to enumerate ordinary trees. Those without a trivalent vertex are ordinary paths. A tree with one trivalent vertex has three arms of lengths \(p\le q\le r\), counted beyond that vertex. Eliminating the arm matrices leaves the scalar
\[
 \sigma=2-\frac p{p+1}-\frac q{q+1}-\frac r{r+1}
       =\frac1{p+1}+\frac1{q+1}+\frac1{r+1}-1.
\tag{N.13}
\]
It must be positive. If \(p\ge2\), it is nonpositive. For \(p=1\), either \(q=1\), with \(r\) arbitrary, or \(q=2\), with \(r=2,3,4\); \(q\ge3\) is impossible. These are the long forks and the three exceptional trees with arm lengths \((1,2,2),(1,2,3),(1,2,4)\), traditionally called \(E_6,E_7,E_8\).

Conversely, the path recurrence and the positive Schur complements just computed show that every matrix on this list is positive definite. The vertex inequalities in each case are exactly
\[
 2w_i m_i\ge\sum_{j\in I\setminus\{i\}}a_{ij}m_j,
\tag{N.14}
\]
with equality at \(i\) precisely when there is no edge from \(i\) to a vertex outside \(I\). This specifies all multiplicity restrictions that we need.

The list is exhausted: ordinary paths; terminally doubled paths in either orientation; ordinary forks with two short arms of length one; the four-vertex path with its central double edge; the two-vertex triple edge; and \(E_6,E_7,E_8\). The last five possibilities have diameter at most six. This enumeration concerns proper subgraphs; a full all-\((-2)\) type instead has genus one by N.1.

<a id="ns11a"></a>

## NS.11a. Completing the bound on every long chain and fork

**Theorem.** If a numerical type is minimal and has genus \(g\ge2\), then
\[
 m_i|a_{ij}|\le768g\qquad\text{for all }i,j.
\tag{NS.11a}
\]
For a type with one vertex this follows from \(A=0\). For several vertices, set \(B=6(g-1)\). By (N.9) all vertices in \(J\) have \(m_j|a_{jj}|\le B\). Each connected component \(I\) of the complement of \(J\) has an edge to \(J\). At an attached vertex, (N.10) gives \(m_iw_i\le B\), hence \(m_i|a_{ii}|\le2B\). Crossing another edge inside \(I\) multiplies this diagonal bound by at most two. If \(I\) is one of the bounded-size cases in N.4, every vertex is within six edges of an attached vertex. Its diagonal bound is consequently at most \(2^7B\le768g\).

We now prove bounds independent of length in every remaining case. Call a vertex attached if it meets \(J\). Its weighted multiplicity \(w_im_i\) is at most \(B\). A component with just one vertex is attached, so is already bounded; the following path arguments use \(t\ge2\).

**Ordinary path.** Number the vertices \(1,\ldots,t\). All vertex and edge weights equal \(w\). At an internal vertex,
\[
 2m_i-m_{i-1}-m_{i+1}\ge0,
\]
and the difference is positive exactly when the vertex is attached. If a maximum occurs away from the endpoints, a boundary of its plateau has a strictly smaller neighbour unless the entire path is the plateau. Such a boundary is attached. A maximum at an endpoint has positive residual \(2m_1-m_2\ge m_1\), or \(2m_t-m_{t-1}\ge m_t\), and is attached as well. Therefore some attached vertex realizes the maximum, and \(wm_i\le B\) everywhere.

**The doubled terminal weight.** Here \(w_1=\cdots=w_{t-1}=w\), \(w_t=2w\), with ordinary edge weights \(w\) and final edge weight \(2w\). Define \(x_i=m_i\) for \(i<t\) and \(x_t=2m_t\). The weighted multiplicities are \(wx_i\). The internal inequalities become
\[
 2x_i\ge x_{i-1}+x_{i+1},\qquad x_t\ge x_{t-1}.
\tag{N.15}
\]
The last inequality comes from the terminal row, not an ordinary endpoint equation. Its strictness means that the terminal vertex is attached. If the terminal vertex realizes a maximum and is unattached, \(x_t=x_{t-1}\). Continue through that maximum plateau: either its left boundary has a smaller neighbour, producing an attached maximum, or it reaches the first endpoint, which is attached by its positive residual. A maximum elsewhere is handled by the same plateau boundary argument. Thus \(w_im_i\le B\) throughout.

**The halved terminal weight.** Now \(w_1=\cdots=w_{t-1}=2w\), \(w_t=w\), and every edge has weight \(2w\). The \(m_i\) satisfy ordinary internal concavity and the terminal row says
\[
 m_t\ge m_{t-1}.
\tag{N.16}
\]
Equality means that the terminal vertex is unattached. The argument for (N.15), applied to \(m\), gives an attached maximum. If that maximum is at an ordinary vertex, \(2w\max_i m_i\le B\). If it is at \(t\), \(w\max_i m_i\le B\). Thus \(w_im_i\le2B\) everywhere and \(m_i|a_{ii}|\le4B\).

**The long fork.** All weights equal \(w\). Take the long path \(1,\ldots,t-1\), and let \(t,t+1\) be the two leaves meeting its last vertex. Set \(s=m_t+m_{t+1}\). The path followed by \(s\) satisfies internal concavity, because
\[
 2m_{t-1}\ge m_{t-2}+s,\qquad s\ge m_{t-1}.
\tag{N.17}
\]
The second inequality is the sum of the two leaf rows. If the path maximum is larger than \(s\), a plateau boundary, or its first endpoint, is an attached maximum, so the path maximum is at most \(B/w\). Suppose instead that \(s\) is a maximum. If both leaves are unattached, each has multiplicity \(m_{t-1}/2\), so \(s=m_{t-1}\). The plateau then either reaches an attached path boundary or reaches the first endpoint, which is attached. Thus \(ws\le B\). If both leaves are attached, \(ws\le2B\). If only one is attached, say \(t\), then \(m_{t+1}=m_{t-1}/2\), and \(s\ge m_{t-1}\) gives \(m_t\ge m_{t-1}/2\). Consequently \(s\le2m_t\) and again \(ws\le2B\). In all cases every path or leaf multiplicity has weighted value at most \(2B\), so its diagonal bound is at most \(4B\).

This covers the entire list in N.4 and proves the diagonal part of (NS.11a). For an off-diagonal entry, (N.10) bounds \(m_i a_{ij}\) by the already bounded diagonal at \(j\). The corrected five-vertex instances and exceptional determinants are calculated in [the accompanying numerical-model reading](../../numerical-source-corrections.md#g-corrections). \(\square\)

<a id="n-picard"></a>

## N.5. Numerical Picard torsion

Let \(D_w=\operatorname{diag}(w_i)\), and define
\[
 P(T)=\operatorname{coker}(D_w^{-1}A:\mathbf Z^n\longrightarrow\mathbf Z^n).
\]
The matrix is integral by (N.1), and (N.3) shows that \(P(T)\) has rank one. Multiplication by \(D_w\) gives an injection
\[
 P(T)\hookrightarrow\operatorname{coker}A.
\tag{N.18}
\]
For if \(D_wz=Ay\), then \(z=D_w^{-1}Ay\), a relation in \(P(T)\).

We prove the matrix torsion estimate of [Stacks 0C6X](https://stacks.math.columbia.edu/tag/0C6X) directly over a finite field. Let \(\ell\) be a prime dividing none of the \(m_i\) or positive edge entries \(a_{ij}\). Orient the edges arbitrarily and let \(B_E\) be the incidence matrix, with row \(ij\) equal to \(e_i^{\mathsf t}-e_j^{\mathsf t}\). Put \(c_{ij}=a_{ij}m_im_j\). Over \(\mathbf F_\ell\),
\[
 -D_mAD_m=B_E^{\mathsf t}\operatorname{diag}(c_{ij})B_E,
 \qquad D_m=\operatorname{diag}(m_i).
\tag{N.19}
\]
This is the matrix form of (N.3). Connectedness gives \(\ker B_E=\mathbf F_\ell(1,\ldots,1)\) and \(\dim\ker B_E^{\mathsf t}=e-n+1=b\). The map
\[
 \frac{\ker(B_E^{\mathsf t}\operatorname{diag}(c)B_E)}
      {\mathbf F_\ell(1,\ldots,1)}
 \longrightarrow\ker B_E^{\mathsf t},\qquad
 [z]\longmapsto\operatorname{diag}(c)B_Ez
\]
is injective: its kernel is zero since every \(c_{ij}\) is a unit. Thus the nullity of \(A\) modulo \(\ell\) is at most \(b+1\). Smith normal form says that this nullity is one plus the dimension of \((\operatorname{coker}A)[\ell]\), since the rational nullity is one. We have proved
\[
 \dim_{\mathbf F_\ell}P(T)[\ell]\le b.
\tag{N.20}
\]

For a minimal type of genus \(g\ge2\), choose \(\ell>768g\). If \(n>1\), (NS.11a) bounds each positive \(a_{ij}\) and each \(m_i\) by \(768g\): use \(|a_{ii}|\ge1\) for the latter. Hence the required divisibilities by \(\ell\) do not occur. For \(n=1\), \(P(T)=\mathbf Z\) and there is no torsion. Together with N.2 this proves
\[
 \dim_{\mathbf F_\ell}P(T)[\ell]\le b\le g.
\tag{N.21}
\]

<a id="n-contraction"></a>

## N.6. Contracting exceptional numerical vertices

The estimate \(\dim P(T)[\ell]\le g\) also holds for a nonminimal type of genus \(g\ge2\), as in [Stacks 0C9X](https://stacks.math.columbia.edu/tag/0C9X). We prove the contraction and its effect on Picard groups, corresponding to [0C77](https://stacks.math.columbia.edu/tag/0C77) and [0C7J](https://stacks.math.columbia.edu/tag/0C7J).

Suppose vertex \(n\) is exceptional. For \(i<n\), put \(b_i=a_{in}/w_n\), \(c_i=a_{in}/w_i\), and choose \(w'_i=w_i/2\) if \(b_i\) is even and \(c_i\) is odd; otherwise put \(w'_i=w_i\). In the halved case \(w_i\) is even: the equality \(w_ic_i=w_nb_i\) proves this. Set
\[
 \begin{aligned}
 m'_i&=m_i,&
 a'_{ij}&=a_{ij}+\frac{a_{in}a_{jn}}{w_n},\\
 g'_i&=\frac{w_i}{w'_i}(g_i-1)+1
       +\frac{a_{in}^2-w_na_{in}}{2w'_iw_n}.
 \end{aligned}
\tag{N.22}
\]
The new off-diagonal entries are nonnegative and symmetric; each is divisible by \(w'_i\). The equation \(\sum_{i<n}a_{in}m_i=w_nm_n\) shows \(A'm'=0\). Eliminating \(n\) connects any two of its neighbours, so a disconnection in the new graph would give a disconnection in the old one.

To check \(g'_i\in\mathbf Z_{\ge0}\), write \(r_i=w_i/w'_i\in\{1,2\}\). Formula (N.22) becomes
\[
 g'_i=r_i(g_i-1)+1+r_ic_i(b_i-1)/2.
\]
If \(a_{in}=0\), this is \(g_i\). If \(r_i=1\) and \(a_{in}>0\), it is \(g_i+c_i(b_i-1)/2\), a nonnegative integer; the only odd numerator would have triggered the halved case. If \(r_i=2\), then \(b_i\ge2,c_i\ge1\), and \(2g_i-1+c_i(b_i-1)\) is nonnegative and integral.

The new genus equals the old genus. The contribution at \(i<n\) changes by \(-m_i a_{in}/2\), whose sum is \(-m_nw_n/2\), exactly the old contribution at the deleted exceptional vertex.

Let \(q:\mathbf Z^n\to\mathbf Z^{n-1}\) delete the last coordinate, and define \(p\) on the target free group by
\[
 p(e_i)=r_ie'_i\ (i<n),\qquad
 p(e_n)=\sum_{i<n}\frac{a_{in}}{w'_i}e'_i.
\]
Substitution in each column gives
\(p(D_w^{-1}A)=D_{w'}^{-1}A'q\), so \(p\) induces \(P(T)\to P(T')\). If a class represented by \(z\) maps to zero, lift its new relation through the surjective \(q\) and subtract the corresponding old relation. We may assume \(p(z)=0\). Its coordinates give \(z_i=-z_na_{in}/w_i\) for \(i<n\); hence \(z=-z_nD_w^{-1}Ae_n\), an old relation. The induced map is injective. Its cokernel is killed by two because \(r_i\) is one or two.

Repeated contractions decrease the vertex count, preserve \(g\), and inject each old Picard group into the next. They end at a minimal type. Apply (N.21) there to obtain \(\dim P(T)[\ell]\le g\) for the original type. The sharper graph bound in (N.21) refers to the original graph when that original type is minimal. \(\square\)
