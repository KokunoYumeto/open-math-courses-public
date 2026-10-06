# Pure test degrees and strong Morse inequalities

A pure sheaf has one local test degree at each regular transverse intersection with a differential graph. The geometric shift alone does not give that degree: the ambient dimension and an ordered inertia index also enter. These local tests determine the global Euler number. The finite Morse filtration gives more information, because its connecting maps record how neighbouring cohomological degrees cancel.

*Written by GPT-6.1 Sol (OpenAI), Ultra, 2 October 2026. Author self-check recorded; not independently reviewed. New original text is public domain (CC0).*

Use Pure and simple sheaves from directional tests for normalized type, its integral shift and the complete transverse-test comparison. Differential sections and proper-below Euler indices proves finiteness and the global ordinary index. Isolated phases and local characteristic-cycle indices proves the local closed-test index.

The exact preceding Morse proof is SH-02, Local jumps and finite Morse data and A finite filtration by local tests, including the proper support, endpoint, localization and connecting-map arguments. We use that written filtration, with its exact maps. Its earlier sheaf foundations and this course's subanalytic foundations retain their recorded proof obligations.

## The geometric shift gives an integral local degree

Let \(X\) be a real analytic Hausdorff manifold, countable at infinity and of dimension \(n\), with the standing uniform finite dimension bound. Let \(k\) be a field of characteristic zero and
\(F\in D^b_{\mathbb R\text{-c}}(k_X)\) have perfect stalks. Put

\[
A=\operatorname{SS}(F),\qquad D=\operatorname{supp}(F)=\pi_XA,
\qquad L_\varphi=\{(x;d\varphi_x):x\in X\},
\qquad\text{(1)}
\]

where \(\varphi:X\to\mathbb R\) is real analytic. Support in (1) is the closed support, including its zero-stalk boundary points. Assume

\[
D\cap\{\varphi\leq t\}\text{ is compact for every }t\in\mathbb R,
\qquad L_\varphi\cap A=\{p_1,\ldots,p_N\}\subset A_{\mathrm{reg}},
\qquad\text{(2)}
\]

and every intersection in (2) is transverse. Here \(A_{\mathrm{reg}}\) consists of points at which \(A\) is locally a smooth conic Lagrangian. Write \(x_i=\pi_X(p_i)\), \(c_i=\varphi(x_i)\), and

\[
V_i=T_{p_i}\pi_X^{-1}(x_i),\qquad
A_i=T_{p_i}A,\qquad B_i=T_{p_i}L_\varphi,\qquad
\tau_i=\tau(V_i,A_i,B_i).
\qquad\text{(3)}
\]

The first plane is the vertical cotangent plane. The index uses the displayed order and the symplectic form \(d\xi\wedge dx\), as in the pure-sheaf lesson.

Suppose \(F\) is pure of shift \(d_i\) and finite multiplicity \(m_i\) at \(p_i\). Thus its normalized type is a vector space \(M_i\) in degree zero, with \(\dim_kM_i=m_i\). The local closed test is

\[
J_i=\bigl(R\Gamma_{\{\varphi\geq c_i\}}F\bigr)_{x_i}.
\qquad\text{(4)}
\]

Subtracting \(c_i\) from the function makes this precisely the normalized test used in the earlier definition of type. Put

\[
e_i=d_i-\frac n2-\frac{\tau_i}{2},
\qquad
\mu_i=-e_i=\frac n2+\frac{\tau_i}{2}-d_i.
\qquad\text{(5)}
\]

Then

\[
J_i\simeq M_i[e_i]=M_i[-\mu_i],
\qquad
H^j(J_i)=0\ (j\ne\mu_i),\qquad
\dim H^{\mu_i}(J_i)=m_i.
\qquad\text{(6)}
\]

**Proof.** The defining type isomorphism is
\(J_i[-d_i+n/2+\tau_i/2]\simeq M_i\).
Solving for \(J_i\) gives (6).

There is no fractional shift functor here. If
\(r_i=\dim(V_i\cap A_i)\), the allowed geometric shift satisfies
\(d_i-r_i/2\in\mathbb Z\). The graph plane is transverse both to \(A_i\), by (2), and to \(V_i\), because it projects isomorphically to the base. The proved inertia parity is
\(\tau_i\equiv n+r_i\pmod2\). Therefore \(n/2+\tau_i/2-d_i\) is an integer. This proves integrality in (5), including when \(d_i\) is a half-integer. \(\square\)

Our convention is \(H^j(K[s])=H^{j+s}(K)\). Accordingly, \(e_i\) is the shift exponent, whereas \(\mu_i\) is the degree of the nonzero local cohomology. They have the same parity. The local degree can be negative for a shifted sheaf.

## The finite intersections give the global Euler sum

The local and global index theorems give

\[
\#\bigl([\sigma_\varphi]\cap\operatorname{CC}(F)\bigr)_{p_i}
=\chi(J_i)=(-1)^{\mu_i}m_i=(-1)^{e_i}m_i,
\qquad\text{(7)}
\]

and

\[
\chi(X;F)=\sum_{i=1}^N(-1)^{\mu_i}m_i.
\qquad\text{(8)}
\]

**Proof.** Transversality isolates each graph intersection in a sufficiently small cotangent neighbourhood. Apply the local closed-test theorem to (4), and use (6) to compute its Euler number.

The full graph intersection in (2) is finite, hence compact. The first condition of (2) is exactly the proper-below support hypothesis of the ordinary global index theorem. That theorem proves bounded finite-dimensional ordinary cohomology and identifies its Euler characteristic with the ordered global intersection.

To pass from that supported intersection to the sum, choose disjoint small neighbourhoods of the \(p_i\). The supported cup class restricts to a class in each neighbourhood; finite closed-support excision identifies its supported cohomology with the direct sum of these local groups. The dualizing point trace is additive on this direct sum. Thus its global number is the sum of the numbers in (7), proving (8). This is localization of the actual supported class; no intersection orientation is replaced by an unsigned count. \(\square\)

The case \(N=0\) is included. The global index has empty support and number zero. The Morse filtration below proves the stronger conclusion \(R\Gamma(X;F)=0\) under the same proper-below hypothesis.

## Conormal tests recover the usual Morse index

Let \(Y\subset X\) be a closed smooth submanifold for which the sheaf in question is \(\mathbb R\)-constructible. Write \(\ell=\dim Y\), \(c=n-\ell\), and consider a locally constant coefficient sheaf of rank \(m\) on \(Y\), extended to \(X\) and shifted by \([s]\), with \(s\in\mathbb Z\).

At a critical point of \(\varphi|_Y\) with nondegenerate restricted Hessian, let \(q\) be the number of its negative eigenvalues. The exact conormal calculation gives

\[
d=s+\frac c2,\qquad
\tau=2q-\ell,\qquad
\mu=\frac n2+\frac{2q-\ell}{2}
       -\left(s+\frac{n-\ell}{2}\right)=q-s.
\qquad\text{(9)}
\]

Thus the raw test is \(k^m[s-q]\), up to the locally chosen negative-direction orientation line, and its local number is
\((-1)^{q-s}m\). The orientation line has rank one and does not change this dimension calculation. Its local trivialization is not a global orientation choice.

For an unshifted constant sheaf on \(X\), (9) reduces to \(\mu=q\). For a submanifold sheaf, the codimension part of the geometric shift cancels the ambient dimension correction. Replacing the vertical plane in (3) with a zero-section tangent would destroy this calculation.

## The Morse filtration retains the attaching maps

Here is the exact preceding filtration in the form needed for our local tests. Its coefficient field may have any characteristic. Let \(F\in D^b(k_X)\), let \(\varphi:X\to\mathbb R\) be smooth, assume compact closed sublevels on the closed support, and assume that \(L_\varphi\cap\operatorname{SS}(F)\) is finite. Require each \(J_i\) in (4) to have bounded finite-dimensional cohomology. Regularity, transversality, purity and analytic constructibility are not required for this filtration statement.

Let
\[
a_1<\cdots<a_r
\qquad\text{(10)}
\]
be the distinct critical values \(c_i\). There are bounded finite-dimensional complexes \(B_0,\ldots,B_r\) and exact triangles

\[
B_0=0,\qquad B_r\simeq R\Gamma(X;F),\qquad
L_\nu\longrightarrow B_\nu\longrightarrow B_{\nu-1}
\xrightarrow{\delta_\nu}L_\nu[1],
\qquad
L_\nu\simeq\bigoplus_{c_i=a_\nu}J_i.
\qquad\text{(11)}
\]

The maps \(B_\nu\to B_{\nu-1}\) are ordinary restrictions from a sublevel above \(a_\nu\) to one below it. Points at the same critical value contribute in one \(L_\nu\); one need not perturb their values or impose an artificial ordering on them.

To clarify the hypotheses used by the earlier proof, the support is bounded below when it is nonempty: choose \(t_0\) with \(K=D\cap\{\varphi\leq t_0\}\ne\varnothing\). The compact set \(K\) has a minimum value \(a\), and every point of \(D\setminus K\) has value greater than \(t_0\geq a\). Thus \(a\) is a global lower bound on \(D\). Also \(\varphi|_D\) is proper, since the inverse image of a compact interval is closed in a compact sublevel.

The finite-band positive-covector comparison consequently propagates the zero sublevel complex to just below \(a_1\), identifies levels between successive \(a_\nu\), and identifies the eventual upper sublevel with the global complex by the open-union comparison. Above the last value the restriction system is constant, so its inverse limit and derived-limit comparison introduce no extra cohomology.

For the local term, proper base change and supported localization for \(H=R\varphi_*F\) give

\[
\bigl(R\Gamma_{[a_\nu,\infty)}H\bigr)_{a_\nu}
\simeq
R\Gamma\left(\{\varphi=a_\nu\};
\left.R\Gamma_{\{\varphi\geq a_\nu\}}F\right|_{\{\varphi=a_\nu\}}\right).
\qquad\text{(12)}
\]

The fibre is compact on coefficient support. At its points outside the \(x_i\) with \(c_i=a_\nu\), the displayed local supported test vanishes by the defining microsupport test. A complex on this fibre supported at finitely many points has cohomology equal to the direct sum of its stalk complexes. Hence (12) gives precisely \(L_\nu\) in (11). The full preceding Morse proof supplies the endpoint continuity and localization triangle producing the actual arrows in (11). Bounded finiteness then follows by induction in these triangles.

For the analytic constructible input of (1)–(2), the local tests are perfect: they are stalks of the constructible internal Hom with the constructible closed-test sheaf. In the pure situation this is already explicit in (6). Thus our index hypotheses satisfy all the filtration hypotheses.

## Adjacent ranks give the exact Morse defect

In the general filtration (11), put

\[
b_j=\dim_kH^j(X;F),\qquad
m_j=\sum_i\dim_kH^j(J_i),\qquad
r_{\nu,j}=\operatorname{rank}
\bigl(H^j(B_{\nu-1})\xrightarrow{H^j(\delta_\nu)}
H^{j+1}(L_\nu)\bigr),
\qquad q_j=\sum_{\nu=1}^r r_{\nu,j}.
\qquad\text{(13)}
\]

All these sequences have finite support, and \(q_j\geq0\). Exactness proves the stronger identity

\[
m_j-b_j=q_{j-1}+q_j.
\qquad\text{(14)}
\]

**Proof.** In the long exact sequence of the \(\nu\)-th triangle, the image entering \(H^j(L_\nu)\) has dimension \(r_{\nu,j-1}\). The image of \(H^j(B_\nu)\) in \(H^j(B_{\nu-1})\) is the kernel of its connecting map, of dimension
\(\dim H^j(B_{\nu-1})-r_{\nu,j}\). The short exact sequence between these two images therefore gives

\[
\dim H^j(B_\nu)=\dim H^j(L_\nu)
 +\dim H^j(B_{\nu-1})-r_{\nu,j-1}-r_{\nu,j}.
\qquad\text{(15)}
\]

Sum (15) over \(\nu\), using \(B_0=0\), \(B_r\simeq R\Gamma(X;F)\), and the direct sums in (11). The intermediate \(B_\nu\) dimensions cancel, yielding (14). \(\square\)

The loss is paired in adjacent degrees because a connecting map runs from degree \(j\) to degree \(j+1\). Knowing only an Euler number loses every \(q_j\).

With finite Laurent polynomials

\[
M(t)=\sum_jm_jt^j,\qquad P(t)=\sum_jb_jt^j,\qquad
Q(t)=\sum_jq_jt^j,
\qquad\text{(16)}
\]

equation (14) is

\[
M(t)-P(t)=(1+t)Q(t),\qquad Q(t)\text{ has nonnegative integer coefficients}.
\qquad\text{(17)}
\]

Laurent polynomials are needed for shifted sheaves; there is no assumption that all cohomological degrees are nonnegative.

## Strong inequalities and the equality case

For every integer \(h\), (14) gives

\[
\sum_{j\leq h}(-1)^{h-j}m_j
-
\sum_{j\leq h}(-1)^{h-j}b_j=q_h\geq0.
\qquad\text{(18)}
\]

Indeed the \(q_j\) terms telescope: the coefficient of every \(q_j\) with \(j<h\) is
\((-1)^{h-j}+(-1)^{h-j-1}=0\), leaving \(q_h\).
These are the strong Morse inequalities. Equation (14) also gives the weak inequalities \(b_j\leq m_j\). Taking the full alternating sum, or putting \(t=-1\) in (17), gives

\[
\chi(X;F)=\sum_i\chi(J_i).
\qquad\text{(19)}
\]

In the pure transverse situation,

\[
m_j=\sum_{\mu_i=j}m_i,\qquad
M(t)=\sum_i m_i t^{\mu_i}.
\qquad\text{(20)}
\]

Thus (19) recovers (8), while (18) counts the local tests in their actual degrees \(\mu_i\). The general filtration proof of (18)–(19) works over an arbitrary field with finite local tests; it does not need the characteristic-zero cycle construction.

Equality in the strong inequality at \(h\) is equivalent to \(q_h=0\). Equality \(m_j=b_j\) in every degree is equivalent to every \(q_j=0\), hence to every connecting map in (11) having zero cohomological rank.

In this last case the triangles split, giving an isomorphism

\[
R\Gamma(X;F)\simeq\bigoplus_\nu L_\nu
\simeq\bigoplus_iJ_i,
\qquad\text{(21)}
\]

without a preferred choice of splitting. To check that zero rank suffices, a bounded complex of vector spaces is the direct sum of its cohomology complex with contractible two-term summands: choose complements of boundaries in cycles and of cycles in each term. Thus, in \(D^b(k)\), a morphism inducing zero maps on every cohomology group is zero. Each \(\delta_\nu\) is consequently zero, and its exact triangle splits. Conversely, (14) and nonnegativity force all the \(q_j\), and then all the individual ranks, to vanish if the dimensions agree. Euler equality alone does not imply (21).

## Examples and exercises with solutions

### A shifted conormal has a negative test degree

*Difficulty: Introductory.*

Let \(\dim X=5\), let \(Y\) have dimension three, and let \(F=k_Y^4[2]\). At a transverse test, the restricted Hessian has one negative eigenvalue. Find the geometric shift, ordered index, test degree and local Euler contribution.

**Solution.** The codimension is two, so \(d=2+2/2=3\). Formula (9) gives \(\tau=2-3=-1\), and
\(\mu=5/2-1/2-3=-1\). The raw test is \(k^4[2-1]=k^4[1]\), with rank four in \(H^{-1}\). Its Euler contribution is \(-4\). The shift exponent in (5) is \(e=1\); the cohomological degree is \(-1\), and both give the same Euler sign.

### The height of a circle is a perfect Morse function

*Difficulty: Introductory.*

Let \(X=S^1\), \(F=k_X\), and \(\varphi(x,y)=y\) on the unit circle. Compute the two test degrees, \(M(t)\), \(P(t)\) and \(Q(t)\).

**Solution.** The support is compact. The zero-section microsupport meets \(d\varphi\) only at the bottom and top points, with transverse Hessians of Morse indices zero and one. Here \(d=0\), \(n=1\), and the ordered indices are \(-1\) and \(1\); (5) gives \(\mu=0\) and \(1\). Each multiplicity is one, so \(M(t)=1+t\).

The ordinary cohomology of the circle is \(k\) in degrees zero and one. A direct finite-cover computation uses two arcs with two contractible overlap components: its differential \(k^2\to k^2\) is \((a,b)\mapsto(b-a,b-a)\), of rank one. Its kernel and cokernel each have dimension one. Hence \(P(t)=1+t\) and \(Q(t)=0\). The finite Morse filtration has no cohomological cancellation, and its Euler sum is \(1-1=0\).

### Monodromy makes the same two local tests cancel

*Difficulty: Intermediate.*

On the same circle, replace \(F\) by a rank-one local system with monodromy \(\lambda\in k^\times\), \(\lambda\ne1\). Calculate its global cohomology and every nonzero \(q_j\). Explain why the two local Morse tests do not determine a direct-sum decomposition.

**Solution.** The local system is trivial on a sufficiently small arc around either critical point, so the tests remain \(k\) and \(k[-1]\). Thus \(M(t)=1+t\).

Trivialize on two arcs as above, with transition factors \(1\) and \(\lambda\) on the two overlap components. Their acyclic-cover complex has differential
\((a,b)\mapsto(b-a,b-\lambda a)\).
Its determinant is \(\lambda-1\), up to the harmless order sign, and is nonzero. The complex is acyclic, so \(b_0=b_1=0\) and \(P(t)=0\). Equation (17) gives \(Q(t)=1\), namely \(q_0=1\) and every other \(q_j=0\).

The bottom-stage complex is \(k\). At the top, the connecting map \(H^0(k)\to H^1(k[-1])\) has rank one and cancels both groups. The strong inequality at zero is strict, \(0<1\); the full Euler equality remains \(0=1-1\). Thus equal local test dimensions for two sheaves can accompany different global cohomology.

### Several points can enter at one critical value

*Difficulty: Intermediate.*

Let \(X=\mathbb R\sqcup\mathbb R\), let \(\varphi=t^2\) on each component, and take constant ranks \(a\) and \(b\) on the two components. Describe the first critical jump and the global cohomology. The ranks are finite and nonnegative.

**Solution.** A closed sublevel of the support is a union of at most two compact intervals. The two graph intersections lie at the origins and have the same value zero. Both tests have degree zero and ranks \(a\) and \(b\). There is one distinct critical value, and its term is
\(L_1=k^a\oplus k^b\) in degree zero. The triangle is
\(L_1\to B_1\to0\to L_1[1]\), so \(B_1\simeq L_1\).
Ordinary cohomology of each contractible component is its constant coefficient space in degree zero. Thus \(b_0=m_0=a+b\), all other dimensions vanish, and \(Q(t)=0\). Separating the two critical values is unnecessary.

### A zero cycle still has nonzero Morse data

*Difficulty: Advanced.*

On the circle, take \(F=k_X\oplus k_X[1]\) and the same height. Calculate the local degree counts \(m_j\), the global \(b_j\) and the Euler contributions. Decide whether the pure formula (20) applies to either critical test.

**Solution.** At the bottom, \(J_{\min}=k\oplus k[1]\), with one dimension in degrees zero and minus one. At the top,
\(J_{\max}=k[-1]\oplus k\), with one dimension in degrees one and zero. Thus
\[
m_{-1}=1,\quad m_0=2,\quad m_1=1.
\]
Global cohomology is
\(R\Gamma(S^1;k)\oplus R\Gamma(S^1;k)[1]\), so it has exactly the same three dimensions. Hence \(Q(t)=0\).

Each local test has Euler characteristic zero, and so does the global complex, although all these complexes are nonzero. Additivity gives
\(\operatorname{CC}(F)=\operatorname{CC}(k_X)-\operatorname{CC}(k_X)=0\), while the full microsupport is still the zero section. Each transverse test has two nonzero cohomology degrees; shifting cannot merge them. Consequently \(F\) is not pure at these intersections and (20) does not apply. The general finite-test formulation (13)–(19) does apply and preserves the nonzero graded data.

### Recover connecting ranks from Laurent Morse data

*Difficulty: Advanced.*

A finite filtration has local counts
\((m_{-2},m_{-1},m_0)=(2,3,1)\) and final Betti counts
\((b_{-2},b_{-1},b_0)=(1,1,0)\), with all other counts zero. Find \(Q(t)\), the defects at degrees minus two, minus one and zero, and a three-stage algebraic filtration realizing these data.

**Solution.** Starting below every nonzero degree, (14) recursively gives
\(q_{-2}=1\), \(q_{-1}=1\), \(q_0=0\), and no other nonzero values. Thus
\[
M(t)-P(t)=t^{-2}+2t^{-1}+1
=(1+t)(t^{-2}+t^{-1}),
\qquad Q(t)=t^{-2}+t^{-1}.
\]
The strong defects at the three requested degrees are respectively one, one and zero. Both Euler sums are zero:
\(2-3+1=1-1\). Equality at the final degree records the Euler equality and does not erase the earlier cancellations.

For a realization, take \(L_1=k^2[2]\), \(L_2=k^3[1]\), \(L_3=k\), and \(B_0=0\). The first triangle gives \(B_1=L_1\). Choose the next connecting map
\(H^{-2}(B_1)\to H^{-1}(L_2)\) to have rank one. Formula (15) gives \(B_2\) dimensions one in degree minus two and two in degree minus one. Choose
\(H^{-1}(B_2)\to H^0(L_3)\) of rank one; the final dimensions are one, one and zero as specified. These choices define actual triangles in \(D^b(k)\): for a morphism \(\delta_\nu:B_{\nu-1}\to L_\nu[1]\), set \(B_\nu=\operatorname{Cone}(\delta_\nu)[-1]\). This is an algebraic filtration example; no geometric realization by a particular sheaf is asserted.

## References and the next step

The strong Morse inequalities for constructible sheaves refine the index theory of M. Kashiwara, [*Index theorem for constructible sheaves*](https://www.numdam.org/item/AST_1985__130__193_0/), Astérisque 130 (1985). The local index and the ordinary global index are taught in the linked preceding lessons; the arbitrary-field finite-test filtration is proved in the linked SH-02 lesson. The distinction between shift exponent and cohomology degree, the adjacent connecting-rank identity, the Laurent-polynomial formulation and the equality analysis are proved here.

For a related computational setting, Adam Brown and Ondřej Draganov, [*Discrete Microlocal Morse Theory*](https://arxiv.org/abs/2209.14993v3), version 3, 10 June 2025, §6.2, prove Morse inequalities for sheaves of finite-dimensional vector spaces on finite posets. Their discrete critical fibres and derived restriction functors differ from the cotangent tests here; the long-exact-sequence dimension argument provides a useful comparison.

The next step is the orientation-valued form of conormal and differential cycles and the ordered transverse intersection convention. It must preserve the same local and global numbers, including every ambient, fibre and cohomological sign.
