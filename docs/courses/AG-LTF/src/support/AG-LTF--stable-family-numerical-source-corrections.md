# Numerical models and corrected weighted calculations

Independent teaching exposition, CC0 1.0. AI author: GPT-6.1 Sol, Ultra. Self-checked by the writing AI.

This reading supplies the geometric numerical statements used in Section S.3 of the stable pointed-family extension. Its mathematical references are the Stacks project authors' [model genus formula](https://stacks.math.columbia.edu/tag/0CA3), [numerical type of a model](https://stacks.math.columbia.edu/tag/0CA4), [minimality comparison](https://stacks.math.columbia.edu/tag/0CA6), [genus after reduction](https://stacks.math.columbia.edu/tag/0CE9), [comparison with geometric genus](https://stacks.math.columbia.edu/tag/0CEA), and [Picard torsion](https://stacks.math.columbia.edu/tag/0CAD). The matrix, heart, classification and \(768g\) proofs are in [Numerical completion NS.11a](AG-LTF--numerical-completion-NS11a.md).

<a id="g-model-type"></a>

## G.1. From a regular model to its numerical type

Let \(R\) be a discrete valuation ring, with uniformizer \(\pi\), fraction field \(K\), and residue field \(k\). Let \(C/K\) be a smooth projective geometrically connected curve of genus \(G\), and let \(X/R\) be a regular proper flat model. Write
\[
 F=X_k=\sum_{i=1}^n m_iC_i,\quad
 \kappa_i=H^0(C_i,\mathcal O_{C_i}),\quad
 w_i=[\kappa_i:k],\quad
 g_i=\dim_{\kappa_i}H^1(C_i,\mathcal O_{C_i}).
\tag{G.1}
\]
The integral curves \(C_i\) are Cartier divisors, since regular surface local rings are factorial. The fibre \(F\) is the principal Cartier divisor of \(\pi\). Properness makes each \(\kappa_i\) finite over \(k\).

Set \(a_{ij}=\deg_k(\mathcal O_X(C_j)|_{C_i})\). For \(i\ne j\), this is the \(k\)-length of the finite intersection \(C_i\cap C_j\). It is symmetric, positive when the curves meet, and zero otherwise. Each degree is a multiple of \(w_i\), because the Euler characteristics defining it are dimensions of \(\kappa_i\)-vector spaces. The triviality of \(\mathcal O_X(F)\) gives \(Am=0\). The special fibre is connected: \(H^0(X,\mathcal O_X)=R\), since this finite \(R\)-algebra is contained in \(H^0(C,\mathcal O_C)=K\) and \(R\) is integrally closed; Stein factorization then gives connected fibres. Thus (G.1), with the intersection matrix, satisfies every numerical-type condition.

We derive its genus rather than assuming it. If \(D'=D+C_i\) is a sum of effective Cartier divisors, the quotient of their ideals gives
\[
 0\longrightarrow\mathcal O_X(-D)|_{C_i}
 \longrightarrow\mathcal O_{D'}
 \longrightarrow\mathcal O_D\longrightarrow0.
\tag{G.2}
\]
Hence the change in Euler characteristic is
\(\chi(C_i,\mathcal O_{C_i})-(D\cdot C_i)\).
Build \(F\) by adding a list of components in which \(C_i\) occurs \(m_i\) times. Summing (G.2) counts the intersection of every pair of distinct occurrences once. Since \(F^2=0\), that sum of pairwise intersections is
\(-\frac12\sum_i m_i a_{ii}\). We obtain
\[
 \chi(F,\mathcal O_F)
 =\sum_i m_iw_i(1-g_i)+\frac12\sum_i m_i a_{ii}.
\]
Euler characteristic is constant in a proper flat curve family, so the left side is \(1-G\). Therefore
\[
 G=1+\sum_i m_i\left(w_i(g_i-1)-\frac{a_{ii}}2\right).
\tag{G.3}
\]
This proves the model and genus assertions of [Stacks 0CA4](https://stacks.math.columbia.edu/tag/0CA4) and [0CA3](https://stacks.math.columbia.edu/tag/0CA3).

A component is exceptional precisely when \(g_i=0\) and \(a_{ii}=-w_i\). In this case \(\mathcal O_X(-C_i)|_{C_i}\) has degree one over \(\kappa_i\). On an integral genus-zero curve a degree-one invertible sheaf has at least two sections by Riemann–Roch. A nonzero section has a Cartier zero scheme of length one, so the exact sequence from that section bounds the dimension of its full space of sections by two. At the unique zero point the local equation generates the maximal ideal, making the curve regular there. The two sections cannot share this zero: otherwise their quotient after removing it would lie in the one-dimensional space of global constants. Thus they give a base-point-free map to \(\mathbf P^1_{\kappa_i}\), finite of degree one. Normality of the target makes it an isomorphism. The normal bundle is consequently \(\mathcal O_{\mathbf P^1}(-1)\), the exceptional-curve criterion. Conversely such a curve has exactly these genus and degree data. Thus a model without exceptional curves has a minimal numerical type, and conversely, as in [Stacks 0CA6](https://stacks.math.columbia.edu/tag/0CA6).

<a id="g-rational-point"></a>

## G.2. A section makes the multiplicity vector primitive

A \(K\)-rational point of \(C\) extends to a section of \(X/R\) by properness, the starting point of [Stacks 0CE8](https://stacks.math.columbia.edu/tag/0CE8). At its special point \(x\), the local homomorphism
\(\mathcal O_{X,x}\to R\) sends \(\pi\) to a uniformizer. Thus \(\pi\) cannot lie in \(\mathfrak m_x^2\). Quotienting the regular surface local ring by this parameter gives a regular curve local ring with residue field \(k\), hence a smooth \(k\)-point of \(F\).

Only one component passes through \(x\). At that component the multiplicity is one, and evaluation at \(x\) embeds its field of constants into \(k\). Consequently
\[
 m_i=w_i=1\quad\text{for that component},\qquad
 d:=\gcd(m_1,\ldots,m_n)=1.
\tag{G.4}
\]
The reduced fibre \(Y=F_{\mathrm{red}}\) is proper, connected and reduced. Its finite ring of global functions is a field; evaluation at \(x\) gives \(H^0(Y,\mathcal O_Y)=k\). These facts supply the hypotheses of the next comparison without any assumption about the other components' constant fields.

<a id="g-reduction-genus"></a>

## G.3. Reduction lowers genus, strictly for a nonreduced minimal fibre

Assume \(d=1\) and \(H^0(Y,\mathcal O_Y)=k\). We construct a filtration from \(Y\) to \(F\) in which all global-function rings remain \(k\). Suppose
\(Z=\sum z_iC_i\), with \(1\le z_i\le m_i\), has been constructed and \(Z\ne F\). The quadratic identity in N.1 gives \(Z^2<0\). Indeed, equality would give \(z_i=qm_i\); integrality of all \(z_i\) and primitivity of \(m\) imply \(q\in\mathbf Z\), impossible with \(0<q<1\). Since \(F\cdot Z=0\),
\[
 (F-Z)\cdot Z=-Z^2>0.
\]
Some component with \(z_i<m_i\) therefore satisfies \(C_i\cdot Z>0\). Add this component to \(Z\). In (G.2) the kernel \(\mathcal O_X(-Z)|_{C_i}\) has negative degree, so has no global section. It follows that
\[
 k\subset H^0(Z+C_i,\mathcal O)\subset H^0(Z,\mathcal O)=k.
\]
The finite procedure ends at \(F\), and all intermediate global-function rings equal \(k\). In particular,
\[
 H^0(F,\mathcal O_F)=k,\qquad
 \dim_kH^1(F,\mathcal O_F)=G.
\tag{G.5}
\]
The filtration is the elementary mechanism behind [Stacks 0C68](https://stacks.math.columbia.edu/tag/0C68).

The map \(H^1(F,\mathcal O_F)\to H^1(Y,\mathcal O_Y)\) is surjective, since the coherent kernel of \(\mathcal O_F\to\mathcal O_Y\) has support of dimension at most one and hence no \(H^2\). Put \(h=\dim_kH^1(Y,\mathcal O_Y)\). We have \(G\ge h\).

Now assume \(X\) is minimal and \(Y\ne F\). In the last step of the filtration, write \(F=Z+C_i\) and \(L=\mathcal O_X(-Z)|_{C_i}\). Since \(F\cdot C_i=0\),
\[
 \deg_kL=a_{ii},\qquad
 \chi(C_i,L)=w_i(1-g_i)+a_{ii}<0.
\tag{G.6}
\]
There is more than one component, since otherwise \(d=1\) would make the fibre reduced. If \(g_i=0\), minimality gives \(a_{ii}\le-2w_i\); if \(g_i\ge1\), the negativity of \(a_{ii}\) gives the same strict sign in (G.6). Thus \(H^1(C_i,L)\ne0\). The two global-function rings of the last step equal \(k\), so its long exact sequence injects this nonzero group into the kernel of \(H^1(F,\mathcal O_F)\to H^1(Z,\mathcal O_Z)\). The subsequent map to \(H^1(Y,\mathcal O_Y)\) is surjective. We conclude
\[
 G>h\quad\text{if a minimal fibre with these hypotheses is nonreduced}.
\tag{G.7}
\]
This proves the strict statement of [Stacks 0CE9](https://stacks.math.columbia.edu/tag/0CE9).

<a id="g-geometric-genus"></a>

## G.4. The lower genus bound and the component equality statement

Assume \(F\) has a smooth \(k\)-rational point \(x\), as in G.2. Let \(b=e-n+1\) be the graph genus, and let \(a_i\) be the sum of the genera of the normalizations of the irreducible components of \((C_i)_{\overline k,\mathrm{red}}\). Write \(a=\sum_i a_i\). Then
\[
 h\ge b+a.
\tag{G.8}
\]
We prove this over an arbitrary residue field, as in [Stacks 0CEA](https://stacks.math.columbia.edu/tag/0CEA).

First note the component estimate
\[
 a_i\le[\kappa_i:k]_{\mathrm s}g_i\le w_ig_i.
\tag{G.9}
\]
There are \([\kappa_i:k]_{\mathrm s}\) embeddings of \(\kappa_i\) into \(\overline k\). The corresponding base changes of \(C_i\) have disjoint underlying supports and each has \(H^1\)-dimension \(g_i\), by flat field base change. For each of them, passing to the reduction surjects on \(H^1\), and passing from the reduction to its finite normalization also surjects on \(H^1\), because the cokernel is supported at finitely many points. The \(H^1\) of that normalization is the sum of its component genera. Summing over the embeddings proves (G.9), the inequality of [Stacks 0CE5](https://stacks.math.columbia.edu/tag/0CE5).

Root a spanning tree of the graph at the component containing \(x\), and order vertices so that a parent precedes its children. The union of every initial segment is connected and contains \(x\). Its global-function field is \(k\), by evaluation at \(x\). The root component is geometrically integral because it has a smooth rational point; its contribution to \(h\) is \(g_i\ge a_i\), while its graph genus is zero.

Add another component \(C_i\) to a preceding union \(D'\). Let \(r\ge1\) count its neighbours already in \(D'\). The union exact sequence, or (G.2), gives
\[
 \Delta h=w_i(g_i-1)+\sum_{C_j\subset D'}a_{ij},\qquad
 \Delta b=r-1,\qquad \Delta a=a_i.
\]
Hence
\[
 \Delta(h-b-a)=
 (w_ig_i-a_i)+
 \sum_{\substack{C_j\subset D'\\a_{ij}>0}}(a_{ij}-1)
 -(w_i-1)\ge0.
\tag{G.10}
\]
The first term is nonnegative by (G.9). Every edge in the sum is a positive multiple of \(w_i\), so the remaining terms are at least
\((r-1)(w_i-1)\ge0\). Induction proves (G.8). The spanning-tree order explicitly avoids any requirement that an arbitrary component be a leaf.

Over an algebraically closed residue field, all \(w_i=1\), and equality \(h=b+a\) forces every component to be smooth. Indeed, every nonnegative contribution in (G.10), together with the root contribution, must vanish; in particular \(g_i=a_i\) for every component. For an integral component over this field, the finite normalization has the same global constants \(k\). Its exact sequence
\[
 0\to\mathcal O_{C_i}\to\nu_*\mathcal O_{C_i^\nu}\to Q_i\to0
\]
therefore gives \(g_i-a_i=\dim_kH^0(Q_i)\). Equality makes \(Q_i=0\), so \(C_i\) is normal, hence regular and smooth over the perfect field \(k\).

The constant-field qualification matters. In the general-field comparison \(w_ig_i\ge[\kappa_i:k]_{\mathrm s}g_i\), equality when \(g_i=0\) says nothing about whether \(\kappa_i/k\) is separable. Thus this particular numerical equality cannot by itself justify the unrestricted separability conclusion printed in [Stacks 0CEE](https://stacks.math.columbia.edu/tag/0CEE). The component-smoothness equality statement just proved is the one used over the algebraically closed residue field in S.3; the inequality (G.8) itself has no such residue-field restriction.

<a id="g-torsion"></a>

## G.5. Vertical divisors, torsion and specialization

For a regular proper model, restriction gives the exact sequence
\[
 0\longrightarrow\mathbf Z
 \xrightarrow{\,1\mapsto m\,}\mathbf Z^n
 \xrightarrow{\,e_i\mapsto\mathcal O_X(C_i)\,}
 \operatorname{Pic}(X)\longrightarrow\operatorname{Pic}(C)
 \longrightarrow0.
\tag{G.11}
\]
To see surjectivity on the right, represent a line bundle on the smooth generic curve by a divisor and close that divisor in the regular surface; its closure is Cartier. A line bundle trivial on \(C\) has a meromorphic trivializing section, whose divisor is a sum of the \(C_i\). Finally, a principal divisor supported on \(F\) comes from a rational function with no zero or pole on \(C\). Such a function is in \(K^*\), and its divisor is an integral multiple of \(F\). These facts prove exactness, the result of [Stacks 0C63](https://stacks.math.columbia.edu/tag/0C63).

Divide the degree on \(C_i\) by \(w_i\). The image of \(\mathcal O_X(C_j)\) is the \(j\)-th column of \(D_w^{-1}A\). This defines
\[
 \operatorname{Pic}(C)\longrightarrow P(T).
\tag{G.12}
\]
A generic line bundle maps to zero precisely when it has an extension to \(X\) of degree zero on every \(C_i\): adjust any extension by a vertical divisor realizing its degree relation.

A degree-zero extension trivial on \(C\) is killed by \(d=\gcd(m_i)\). Indeed, write it as \(\mathcal O_X(\sum z_iC_i)\). Its degrees give \(Az=0\), so N.1 gives \(z=qm\). The integer vector \(m/d\) is primitive, whence \(q\in d^{-1}\mathbf Z\). Multiplying the divisor by \(d\) produces an integral multiple of the principal fibre.

For an integer \(q\ge1\) coprime to \(d\), we obtain
\[
 0\longrightarrow\operatorname{Pic}(X)[q]
 \longrightarrow\operatorname{Pic}(C)[q]
 \longrightarrow P(T)[q].
\tag{G.13}
\]
The vertical group \(\mathbf Z^n/\mathbf Zm\) in (G.11) has torsion \(\mathbf Z/d\mathbf Z\), so contributes no \(q\)-torsion and proves injectivity on the left. For the middle exactness, let \(\xi\in\operatorname{Pic}(C)[q]\) map to zero. Choose its degree-zero extension \(L\). The preceding paragraph says \((L^{\otimes q})^{\otimes d}\) is trivial. Choose \(d'\) with \(dd'\equiv1\pmod q\); then \(L^{\otimes dd'}\) is \(q\)-torsion and restricts to \(\xi\). Conversely, a torsion line bundle on \(X\) has all degrees zero. This proves [Stacks 0CAD](https://stacks.math.columbia.edu/tag/0CAD).

If \(q\) is also prime to the residue characteristic, then
\[
 \operatorname{Pic}(X)[q]\longrightarrow\operatorname{Pic}(Y)[q]
 \quad\text{is injective}.
\tag{G.14}
\]
Here is a proof including the formal compatibility step in [Stacks 0CAE](https://stacks.math.columbia.edu/tag/0CAE). Put \(X_r=X\times_RR/(\pi^r)\). Each \(X_r\) is a finite nilpotent thickening of \(Y\). We justify the prime-to-characteristic torsion comparison, including the possible quotient coming from global units, rather than inferring it solely from the cohomology of a square-zero ideal.

Let \(I\) cut out \(Y\) in \(X_r\), and write \(\mathcal K=1+I\) for the kernel of the restriction on unit sheaves. The \(q\)-th power map is an automorphism of \(\mathcal K\): a unit congruent to one has a unique \(q\)-th root congruent to one, by successive lifting through the nilpotent ideal, since \(q\) is invertible. Thus multiplication by \(q\) is an automorphism on every \(H^j(Y,\mathcal K)\). The unit sequence identifies the kernel of \(\operatorname{Pic}(X_r)\to\operatorname{Pic}(Y)\) with
\[
 H^1(Y,\mathcal K)/D,
 \qquad
 D=\operatorname{im}\left(H^0(Y,\mathcal O_Y^*)
                    \longrightarrow H^1(Y,\mathcal K)\right).
\tag{G.14a}
\]

The proper connected reduced curve \(Y\) has a finite constant field \(\kappa=H^0(Y,\mathcal O_Y)\) over \(k\). Every constant \(v\in\kappa\) separable over \(k\) lifts to a global function on \(X_r\). To prove this, lift the coefficients of its separable minimal polynomial from \(k\) to \(R/(\pi^r)\). Its root \(v\) on \(Y\) has invertible derivative. Nilpotent root lifting therefore gives a unique root reducing to \(v\) on each open set; uniqueness glues these roots globally. When \(v\ne0\), the lift is a unit. In residue characteristic zero every constant is separable, so \(D=0\). In residue characteristic \(p>0\), each \(u\in\kappa^*\) has a power \(u^{p^e}\) separable over \(k\), since the minimal polynomial of \(u\) is a separable polynomial in \(T^{p^e}\). Hence its unit connecting class satisfies \(p^e\delta(u)=0\). The group \(D\) is consequently \(p\)-primary torsion. Multiplication by \(q\), being prime to \(p\), is bijective on \(D\): for a class killed by \(p^e\), its inverse is multiplication by any integer inverse of \(q\) modulo \(p^e\).

It follows that multiplication by \(q\) is bijective on the quotient in (G.14a). Explicitly, if \(qz\in D\), take \(d\in D\) with \(qd=qz\); injectivity on \(H^1(Y,\mathcal K)\) gives \(z=d\). Surjectivity follows from that on \(H^1(Y,\mathcal K)\). Thus this quotient introduces no \(q\)-torsion. The obstruction group \(H^2(Y,\mathcal K)\) also has bijective multiplication by \(q\), so a \(q\)-torsion class on \(Y\) has zero lifting obstruction; correcting any lift by the unique \(q\)-division of its \(q\)-fold multiple in (G.14a) gives a \(q\)-torsion lift. This proves the torsion comparison needed here, corresponding to [Stacks 0C6S](https://stacks.math.columbia.edu/tag/0C6S). In the course application \(H^0(Y,\mathcal O_Y)=k\), every residue constant already lifts from \(R\), and simply \(D=0\). In particular a \(q\)-torsion line bundle \(L\) trivial on \(Y\) is trivial on every \(X_r\).

We need compatible trivializations, not just unrelated triviality at each order. Set \(V_r=H^0(X_r,L|_{X_r})\). For fixed \(r\), the images of \(V_s\to V_r\), \(s\ge r\), stabilize because \(V_r\) has finite length over \(R\). Every such image contains a trivializing section, by restricting a trivialization from \(X_s\). A section on a thickening is a generator exactly when its reduction is a generator, since the underlying point set is unchanged and the ideal is nilpotent. Therefore the images of the sets of trivializing sections stabilize as well. Their stabilized sets map surjectively at successive orders. Choosing in these sets gives compatible trivializations \(t_r\).

The compatible \(t_r\) identify
\(\varprojlim V_r\) with \(\varprojlim H^0(X_r,\mathcal O_{X_r})\). The theorem on formal functions [Stacks 02OC](https://stacks.math.columbia.edu/tag/02OC) identifies these limits with the completions of \(H^0(X,L)\) and \(H^0(X,\mathcal O_X)=R\). Hence \(H^0(X,L)^\wedge\cong\widehat R\). The finite torsion-free \(R\)-module \(H^0(X,L)\) is consequently free of rank one. Its generator restricts to a trivialization on every \(X_r\), since in the completed module it is a unit multiple of the compatible formal generator. Its zero scheme is closed, proper over \(R\), and misses the special fibre. A nonempty closed proper subscheme meeting the generic fibre would have closed image containing the closed point of \(\operatorname{Spec}R\), a contradiction. Thus the generator has no zero anywhere and \(L\) is trivial. This proves (G.14).

In S.3, a section gives \(d=1\), and visibility supplies \(2G\) independent \(\ell\)-torsion classes on \(C\), with \(\ell>768G\) prime to the residue characteristic. N.5 bounds the image of (G.13) by \(b\), so its kernel has at least \(2G-b\) independent classes. By (G.14) these inject into \(\operatorname{Pic}(Y)[\ell]\). Combining this with G.3 and G.4 supplies precisely the numerical-model inequalities
\[
 G\ge h\ge b+a
 \quad\text{and}\quad
 \dim_{\mathbf F_\ell}\operatorname{Pic}(Y)[\ell]\ge2G-b.
\tag{G.15}
\]
Equality \(G=h\) forces a minimal fibre to be reduced; over algebraically closed residue, equality \(h=b+a\) makes its components smooth. The remaining reduced-curve torsion bound and its singularity equality calculation are proved in S.3 of the stable-family reading.

<a id="g-corrections"></a>

## G.6. Corrected chain rows and exceptional determinants

These computations make explicit the corrections needed in the numerical results cited above.

For the five-vertex chain with vertex weights \((w,w,w,w,2w)\), diagonal entries are \((-2w,-2w,-2w,-2w,-4w)\), and successive edge entries are \((w,w,w,2w)\). On a proper rational subgraph, the matrix applied to its multiplicities is nonpositive, by (N.14). Reading rows three, four and five gives
\[
 \boxed{2m_3\ge m_2+m_4,\quad
        2m_4\ge m_3+2m_5,\quad
        2m_5\ge m_4.}
\tag{G.16}
\]
The coefficient two belongs to the final edge in the fourth row. For the opposite orientation, the weights are \((2w,2w,2w,2w,w)\), the first four diagonal entries are \(-4w\), the last is \(-2w\), and all successive edges have weight \(2w\). Its terminal row is
\(-2wm_5+2wm_4\le0\), giving
\[
 \boxed{m_5\ge m_4.}
\tag{G.17}
\]
These are the corrected \(C_5\) and \(B_5\) instances of the two long cases, with their labels as used in [Stacks 0C82](https://stacks.math.columbia.edu/tag/0C82).

The \(E_7\) tree has arm lengths \(1,2,3\). Its normalized positive matrix \(H\) has determinant
\[
 (1+1)(2+1)(3+1)
 \left(\frac12+\frac13+\frac14-1\right)=2,
\]
by the arm elimination in (N.13). Therefore its intersection matrix \(A=-wH\) satisfies
\[
 \boxed{\det A=-2w^7<0.}
\tag{G.18}
\]
It is nonsingular, so the tree in [Stacks 0C8J](https://stacks.math.columbia.edu/tag/0C8J) cannot constitute the full positive-kernel numerical type. For the eight-vertex tree, number the main path \(1,2,3,4,5,6,7\), attaching vertex \(8\) to vertex \(5\). Its complete edge set is
\[
 \boxed{\{12,23,34,45,56,67,58\}.}
\tag{G.19}
\]
This has arm lengths \(1,2,4\), so the same determinant computation gives
\(2\cdot3\cdot5(1/2+1/3+1/5-1)=1\).
All edge entries are \(w\) and all diagonals are \(-2w\). In particular the row at \(5\) is
\(2m_5\ge m_4+m_6+m_8\); the row at \(6\) is
\(2m_6\ge m_5+m_7\). The edge list matches the matrix and supplies the corrected \(E_8\) labelling of [Stacks 0C8L](https://stacks.math.columbia.edu/tag/0C8L).

Finally, the propagated quantity is
\[
 \boxed{m_i|a_{ii}|\le768g.}
\tag{G.20}
\]
The diagonal is negative; the bound includes its absolute value and the vertex multiplicity. It follows from NS.11a for every proper rational component and from the heart bound for the remaining vertices. An all-rational-\((-2)\) full type has genus one by (N.2), rather than genus zero. These signs, coefficients and hypotheses are used in (G.15). \(\square\)
