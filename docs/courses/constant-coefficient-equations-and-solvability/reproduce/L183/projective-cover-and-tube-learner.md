# Finite covers and normal circles in projective complements

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A small normal circle around a hyperplane carries homological information about that hyperplane. To show that this information survives in the complement, we need one homology group of the ambient projective complement to vanish. A concrete finite cover provides that vanishing.

Basic references are Allen Hatcher's *Algebraic Topology* [H], Arthur Sard's critical-value paper [S], and Atiyah, Bott and Gårding's projective-cycle methods [A]. The complete proof below gives the covering, simplex lifting, chain transfer and homology deduction. The preceding [Rational top forms detect cycles in a hypersurface complement](../../AN02-L182.html) supplies the exact critical-value and semialgebraic finiteness lemmas, as well as the rational period theorem. [Ordinary finite-chain Morse handles](../../AN02-L125.html) supplies the relative sublevel proof. The oriented normal bundle and Thom/excision map are constructed in [Projective exhaustion and the finite-chain tube receiver](../../AN02-L124.html#tp6-the-included-normal-bundle-argument-and-the-tube-deduction).

## 1. The two spaces and the missing homology group

Let \(F\) be a nonzero homogeneous polynomial of degree \(m\geq1\) in \(d+1\) complex variables, \(d\geq1\). We compare
\[
 U=\mathbb P^d\setminus\{F=0\},\qquad
 X=\{Z\in\mathbb C^{d+1}:F(Z)=1\}.
 \tag{1}
\]
The removed zero set may have singular points or repeated factors. The affine level \(X\) is smooth. Euler's identity gives
\[
 \sum_{j=0}^d Z_jF_{Z_j}=mF=m\ne0\quad\hbox{on }X,
 \tag{2}
\]
so its differential cannot vanish there. The map
\[
 p:X\longrightarrow U,\qquad Z\longmapsto[Z]
 \tag{3}
\]
has \(m\) points in each fiber: on a projective line the equation is \(\lambda^mF(Z)=1\). Local logarithms of the nonzero value of \(F\) give the \(m\) distinct holomorphic branches. Thus (3) is an \(m\)-sheeted covering, possibly disconnected, with a specified cyclic action by the \(m\)-th roots of unity.

A generic squared distance \(\rho_a(Z)=|Z-a|^2\) on \(X\) is proper, strictly plurisubharmonic and Morse. Its polynomial critical equations have only finitely many solutions. The equal-dimensional critical-value proof gives nondegeneracy, and semialgebraic projection turns discreteness into finiteness. The Morse indices are at most the complex dimension \(d\). The finite-chain handle argument therefore gives
\[
 H_j(X;R)=0\quad(j>d)
 \tag{4}
\]
for any coefficient ring \(R\), and finite-dimensional groups in every degree over a field.

To descend (4), lift each singular simplex in \(U\) in all \(m\) possible ways and sum those lifts. This defines the chain transfer
\[
 \operatorname{tr}:C_j(U;R)\longrightarrow C_j(X;R),
 \qquad p_\#\operatorname{tr}=mI.
 \tag{5}
\]
Restriction of all lifts to a face gives all lifts of that face, each once; hence the transfer commutes with the boundary. Over the rationals we can divide by \(m\), so its homology map is injective and
\[
 H_j(U;\mathbb Q)=0\quad(j>d).
 \tag{6}
\]
The same conclusion holds for any coefficient ring in which \(m\) is invertible. For integral coefficients the displayed transfer argument gives only \(mH_j(U;\mathbb Z)=0\) above \(d\). This is a limit of that inference, not an assertion that those particular integral groups must be nonzero.

## 2. The normal disc and its boundary

For a nonzero linear form \(L\), put
\[
 Y=U\cap\{L=0\},\qquad V=U\setminus Y
                         =\mathbb P^d\setminus\{FL=0\}.
 \tag{7}
\]
The hyperplane section \(Y\) is a closed smooth complex hypersurface of \(U\). It is allowed to be empty. Its real rank-two normal bundle has a canonical complex orientation.

The exact homological Thom/excision construction gives an isomorphism
\[
 \Theta:H_{d-1}(Y;\mathbb Q)
             \xrightarrow{\ \cong\ }H_{d+1}(U,V;\mathbb Q).
 \tag{8}
\]
Locally it crosses a base cycle with a positive normal two-disc, disc first. The relative boundary is its positive normal circle, circle first:
\[
 \tau=\partial_{U,V}\Theta:
          H_{d-1}(Y;\mathbb Q)\longrightarrow H_d(V;\mathbb Q).
 \tag{9}
\]
The exact sequence of the pair has the segment
\[
 H_{d+1}(U;\mathbb Q)\longrightarrow H_{d+1}(U,V;\mathbb Q)
                          \longrightarrow H_d(V;\mathbb Q).
 \tag{10}
\]
The first group vanishes by (6). Therefore the second arrow is injective, and so is the tube (9).

The cover degree and the local tube coefficient are different quantities. The cover has degree \(m\), used in the homology transfer. A positive normal disc has boundary one positive normal circle. Its local tube coefficient is one, independent of \(m\). Interchanging the normal circle with a base cycle of dimension \(d-1\) changes the orientation by \((-1)^{d-1}\).

Combining this injection with the preceding rational period theorem gives an exact test. In coordinates \(Z_0=L,Z_1,\ldots,Z_d\), let
\[
 \omega=\sum_{j=0}^d(-1)^jZ_j\,dZ_0\wedge\cdots
                   \wedge\widehat{dZ_j}\wedge\cdots\wedge dZ_d.
 \tag{11}
\]
If the tube of \(\beta\in H_{d-1}(Y;\mathbb Q)\) has zero period against every
\[
 \frac{P\omega}{F^kL^s},\qquad k,s\geq1,\qquad
               \deg P=mk+s-d-1,
 \tag{12}
\]
then \(\beta=0\). Indeed those forms detect its tube class in \(H_d(V;\mathbb Q)\), and the tube map is injective. A specified affine cycle must still be compared with this precise projective map; neither the cover nor the period test determines that comparison's sign or multiplicity on its own.

## 3. Four worked examples

### Example 1. A repeated factor and a disconnected cover

Take \(F=Z_0^m\). Then \(U=\{Z_0\ne0\}\cong\mathbb C^d\), with coordinates \(u_j=Z_j/Z_0\). Upstairs,
\[
 X=\bigcup_{\zeta^m=1}\{Z_0=\zeta\},
 \tag{13}
\]
the disjoint union of \(m\) affine \(d\)-planes. On the component \(Z_0=\zeta\), the map sends
\((\zeta,Z_1,\ldots,Z_d)\) to \(u_j=Z_j/\zeta\).
For a simplex \(\sigma\) with chart coordinates \(\sigma_j\), its transfer is
\[
 \operatorname{tr}\sigma=
       \sum_{\zeta^m=1}
          \bigl(y\longmapsto(\zeta,\zeta\sigma_1(y),\ldots,
                                             \zeta\sigma_d(y))\bigr).
 \tag{14}
\]
Each summand projects to exactly \(\sigma\), giving \(p_\#\operatorname{tr}\sigma=m\sigma\) on chains.

Repeated factors cause no smoothness problem on \(F=1\). They can make the cover disconnected. In this example permutations of the \(m\) components also give deck transformations, so the specified cyclic root action need not be the entire deck group. Its free transitive action on each fiber is all the transfer calculation requires.

### Example 2. A loop whose individual lifts are not loops

Take \(d=1\), \(F=Z_0Z_1\), \(m=2\). The affine level is \(zw=1\), parametrized by \(z\in\mathbb C^*\), \(w=1/z\). On \(U\), use the coordinate \(u=Z_0/Z_1\). Then
\[
 p(z)=z^2.
 \tag{15}
\]
The positively oriented base loop \(\gamma(t)=e^{2\pi it}\), \(0\leq t\leq1\), has two lifts
\[
 \widetilde\gamma_+(t)=e^{\pi it},\qquad
 \widetilde\gamma_-(t)=-e^{\pi it}.
 \tag{16}
\]
The first runs from \(1\) to \(-1\), and the second from \(-1\) to \(1\). Neither is individually a cycle, but their boundaries cancel:
\[
 \partial(\widetilde\gamma_++\widetilde\gamma_-)
          =([-1]-[1])+([1]-[-1])=0.
 \tag{17}
\]
The transfer is the positive full circle upstairs. Projecting it yields \(2\gamma\), because each parametrized half-circle projects to the same whole base loop.

The normalized upstairs period is
\[
 \int_{\operatorname{tr}\gamma}\frac{dz}{2\pi iz}
         =\tfrac12+\tfrac12=1.
 \tag{18}
\]
Meanwhile \(p^*(du/u)=2\,dz/z\). Thus the pulled-back base period on the transferred chain is two, in agreement with (5). Confusing (18) with the period of the pulled-back base form would lose the factor two.

![A whole loop in the base and its two half-circle lifts, whose endpoints cancel in the transfer.](figures/double-cover-loop-transfer.png)

*Figure 1. The base coordinate is \(u=e^{2\pi it}\), while the two upstairs coordinates are \(z=e^{\pi it}\) and \(z=-e^{\pi it}\), with \(w=1/z\) on \(X=\{zw=1\}\). The diagram shows the base plane and the upstairs \(z\)-projection, rather than all four real coordinates of \(X\). Equal parameter labels have the same base image. Arrows use increasing \(t\); the two half-circle endpoints cancel exactly as in (17). The transfer projects to twice the base loop but has the upstairs period (18). Formal Proposition 4.1 fixes both chain identities. Original coordinate diagram, CC0; transfer method context [H].*

### Example 3. A point, a normal disc and one circle

Take \(d=1\), \(F=Z_0^m\), \(L=Z_1\). In the affine coordinate \(v=Z_1/Z_0\),
\[
 U=\mathbb C,\qquad Y=\{0\},\qquad V=\mathbb C^*.
 \tag{19}
\]
The positive generator \([0]\) of ordinary \(H_0(Y;\mathbb Q)\) transfers under the Thom map to the relative class of a positively oriented small disc in \(U\). Its relative boundary is
\[
 v=\varepsilon e^{i\theta},\qquad0\leq\theta\leq2\pi,
 \tag{20}
\]
with coefficient one. Its period of \(dv/(2\pi iv)\) is one, proving directly that the tube is nonzero and injective.

The degree \(m\) of the separate affine covering in Example 1 does not appear in this normal boundary. Also, the source here is ordinary \(H_0\) of a point, not its reduced homology. A two-point affine equator with total coefficient zero is a different degree-zero cycle; its relation to a projective point must be computed in the specific geometric comparison.

### Example 4. Normal circle first on an exact product

Take \(d=2\), \(F=Z_0Z_1\), \(L=Z_2\). In the chart \(Z_0=1\), set \(a=Z_1/Z_0\), \(b=Z_2/Z_0\). Then
\[
 U=\mathbb C^*\times\mathbb C,\quad
 Y=\mathbb C^*\times\{0\},\quad
 V=(\mathbb C^*)^2.
 \tag{21}
\]
For the positive base loop \(a=e^{i\varphi}\), its normal-circle-first tube is
\[
 T(\theta,\varphi)=(e^{i\varphi},\varepsilon e^{i\theta}),
       \qquad0\leq\theta,\varphi\leq2\pi,
 \tag{22}
\]
oriented by the parameter order \((\theta,\varphi)\). It is the boundary of a normal-disc-first relative chain; the base circle is closed, so the product boundary gives it with coefficient one.

For the normal-first rational form,
\[
 T^*\!\left(\frac{db}{b}\wedge\frac{da}{a}\right)
      =(i\,d\theta)\wedge(i\,d\varphi)
                      =-\,d\theta\wedge d\varphi,
 \tag{23}
\]
and hence
\[
 \int_T\frac{db}{b}\wedge\frac{da}{a}
                  =-4\pi^2=(2\pi i)^2.
 \tag{24}
\]
The normalized form \((2\pi i)^{-2}(db/b)\wedge(da/a)\) has period one. Reversing the order of the two circle coordinates, or the wedge order alone, changes the sign. Reversing both preserves it.

![The normal and base angular parameter rectangle, with the normal-first two-form and its exact period.](figures/normal-first-parameter-square.png)

*Figure 2. The plotted square is the parameter domain of the exact map (22). Opposite edges are identified with the same angular orientation; the map's domain order is \((\theta,\varphi)\), normal angle first. The displayed tangent directions and ordered differential \(d\theta\wedge d\varphi\) give the orientation. The pullback coefficient is \(-1\), so integrating over the full square gives (24). This is a parameter diagram of a torus in \(\mathbb C^2\), not a spatial embedding of the ambient four-dimensional space. Formal (29) gives the positive normal boundary coefficient, and Proposition 4.1 keeps that coefficient distinct from the covering degree. Original exact diagram, CC0; normal-tube method context [A].*

## 4. Exercises, 100 points

1. **Homogeneity and smoothness, 10 points.** Derive Euler's identity by monomials. Apply it to \(F(Z)=Z_0^2Z_1^2\) to prove that \(F=1\) is smooth, despite the repeated factors. Show that this affine level has two components, while its cover of the projective complement has four points in each fiber.
2. **Three lifts and one transferred cycle, 12 points.** For \(q:\mathbb C^*\to\mathbb C^*\), \(q(z)=z^3\), write all lifts of the positive unit loop. Compute their endpoints, show the sum is a cycle, and compute its period of \(dz/(2\pi iz)\) and of \(q^*(du/(2\pi iu))\).
3. **The transfer on a face, 12 points.** Prove that restrictions of all lifts of a singular two-simplex to any selected edge give all lifts of that edge, each exactly once. Use this to verify the signs in the transfer's boundary identity. Explain why selecting just one lift is insufficient for a chain map without additional choices.
4. **The polynomial normal equations, 14 points.** Write the equations defining the critical pairs of \(|Z-a|^2\) on \(F=1\). Derive the tangent Hessian formula and show why a regular value of the normal-parameter map makes it nonsingular. Explain why its domain and target have equal real dimension.
5. **What division by the degree proves, 12 points.** Suppose \(q:E\to B\) has degree six and \(H_j(E;R)=0\). Use the transfer to determine what is proved about \(H_j(B;R)\) for \(R=\mathbb Q,\mathbb F_5,\mathbb F_2,\mathbb Z\). Distinguish absence of an implication from evidence of a nonzero group.
6. **The normal-first sign, 12 points.** In a trivial normal bundle over a two-dimensional cycle, compute the boundary of \(D^2\times c\). What sign appears on moving the normal circle after that cycle? Repeat for a three-dimensional cycle. Explain why the two-disc's order gives a different sign calculation from the circle's order.
7. **One point and two points, 12 points.** In Example 3 compute ordinary and reduced \(H_0(Y;\mathbb Q)\). Compare it with the reduced class \([p_+]-[p_-]\) in a two-point space. If both points are mapped to the same projective point, compute the image of that class. Explain why this simple map does not settle a deformed affine equator's geometric comparison.
8. **From periods to a zero base class, 16 points.** Let \(\beta\in H_{d-1}(Y;\mathbb Q)\) have tube with zero periods against all forms (12). Give the complete deduction of \(\beta=0\), citing the exact preceding theorem and the coefficient comparison where needed. For Example 4, compute the normalized period if only the normal-circle orientation is reversed. State the further data needed before applying this receiver to a separately specified affine cycle.

## 5. Complete solutions

### Solution 1

For a monomial \(Z^\alpha\) of total degree \(m\), differentiation gives
\(\sum_jZ_j\partial_{Z_j}Z^\alpha=\sum_j\alpha_jZ^\alpha=mZ^\alpha\).
Summing over its coefficients gives \(\sum_jZ_jF_{Z_j}=mF\). On \(F=1\) the right side is nonzero, so at least one derivative is nonzero. **4 points.**

For \(F=Z_0^2Z_1^2\), \(m=4\); on the level both coordinates are nonzero, and directly \(F_{Z_0}=2Z_0Z_1^2\ne0\). The equation is
\((Z_0Z_1)^2=1\), so the level is the disjoint union of \(Z_0Z_1=1\) and \(Z_0Z_1=-1\), each isomorphic to \(\mathbb C^*\) by its first coordinate. These are the two connected components. **3 points.** In each projective line not meeting the removed divisor, \(\lambda^4F(Z)=1\) has four distinct roots. The cover therefore has degree four, with two points in each of the two components over every base point. Component count and sheet count are distinct. **3 points.**

### Solution 2

Let \(\zeta=e^{2\pi i/3}\). The lifts are
\[
 \widetilde\gamma_j(t)=\zeta^j e^{2\pi it/3},
                     \qquad j=0,1,2.
 \tag{25}
\]
They start at \(\zeta^j\) and end at \(\zeta^{j+1}\), with indices modulo three. Their boundaries sum to
\(\sum_j([\zeta^{j+1}]-[\zeta^j])=0\).
This is a cycle, though none of its three arcs is closed alone. **5 points.**

On every arc, \(dz/z=(2\pi i/3)\,dt\), so its normalized period is \(1/3\). The sum has period one. **3 points.** The pulled-back normalized base form is
\[
 q^*\!\left(\frac{du}{2\pi iu}\right)
                   =3\,\frac{dz}{2\pi iz}.
 \tag{26}
\]
Its transferred period is therefore three. On chains \(q_\#\operatorname{tr}\gamma=3\gamma\), which has the same base period. **4 points.**

### Solution 3

Fix a point on the selected edge. Evaluation there bijects all lifts of the two-simplex with the covering fiber, by Lemma 3.1. It also bijects all lifts of the edge simplex with that same fiber. Restriction preserves the value at this point. Hence the restriction correspondence is a bijection, and every edge lift appears exactly once. This does not require the originally chosen vertex to lie on that edge. **5 points.**

For ordered vertices \(v_0,v_1,v_2\), the simplex boundary is
\([v_1,v_2]-[v_0,v_2]+[v_0,v_1]\).
Each restricted collection is precisely its edge transfer; the alternating signs are unchanged by lifting. Therefore
\[
 \partial\operatorname{tr}\sigma
   =\operatorname{tr}(\sigma|_{12})
        -\operatorname{tr}(\sigma|_{02})
        +\operatorname{tr}(\sigma|_{01})
   =\operatorname{tr}\partial\sigma.
 \tag{27}
\]
**4 points.** A single lift depends on a chosen point of a fiber. Independently chosen lifts on faces need not be its restrictions. The once-traversed loop in Example 2 already shows a selected lift can have nonzero boundary although the base chain has zero boundary. Summing all lifts cancels that choice and yields the canonical chain map. **3 points.**

### Solution 4

With \(g_1=\operatorname{Re}F-1\), \(g_2=\operatorname{Im}F\), the critical pairs satisfy
\[
 g_1=g_2=0,\qquad
 Z-a=\lambda_1\nabla g_1+\lambda_2\nabla g_2.
 \tag{28}
\]
The gradients span the normal space, so this is exactly the vanishing of the tangent derivative of \(|Z-a|^2\). **3 points.**

For a curve \(Z(s)\) in the level with tangent \(v\), twice differentiating \(g_j(Z(s))=0\) gives
\(\nabla g_j\cdot Z''=-v\cdot\operatorname{Hess}g_jv\).
Consequently the restricted Hessian is
\[
 B(v,t)=2v\cdot
       \left(I-\sum_{j=1}^2\lambda_j\operatorname{Hess}g_j\right)t .
 \tag{29}
\]
The diagonal calculation follows from the second derivative of the distance; polarization gives the displayed bilinear form. **5 points.**

The domain of the normal-parameter map is \(X\times\mathbb R^2\), of dimension \(2d+2\), the same as the ambient target. Its differential is \(Av-\sum_j\mu_j\nabla g_j\). Tangent projection is \(P_TAv\). A tangent kernel vector can be completed by \(\mu\) to a kernel of the full differential, because its \(Av\) is normal; conversely full invertibility gives tangent invertibility. Regularity of the chosen center therefore makes the tangent Hessian nonsingular. **6 points.**

### Solution 5

The identity on homology is \(q_*\operatorname{tr}_*=6I\). If the upstairs group in this degree is zero, its transfer is zero, so \(6h=0\) for every base class. **3 points.**

Over \(\mathbb Q\), six is invertible, so \(h=0\). Over \(\mathbb F_5\), six equals one, and the same argument gives \(h=0\). **3 points.** Over \(\mathbb F_2\), six equals zero; \(6h=0\) imposes no new restriction. Over \(\mathbb Z\), the proved conclusion is annihilation by six, which does not exclude nonzero torsion. **4 points.** These last two deductions do not assert a nonzero group exists. They state the information supplied by this transfer identity alone; a separate geometric argument could prove more. **2 points.**

### Solution 6

For a cycle \(c\), \(\partial c=0\), and the product boundary identity gives
\[
 \partial(D^2\times c)
       =(\partial D^2)\times c+(-1)^2D^2\times\partial c
       =S^1\times c.
 \tag{30}
\]
The positive normal circle is first, with coefficient one. **4 points.** If \(\dim c=2\), moving that one-dimensional circle after \(c\) changes the orientation by \((-1)^{1\cdot2}=+1\). If \(\dim c=3\), the sign is \((-1)^3=-1\). **4 points.** Moving the two-disc instead gives \((-1)^{2\dim c}=+1\) in both cases. The relative disc product can therefore agree with a fiber-last Thom convention while the circle order on its boundary carries a nontrivial sign. The dimensions of the factors, rather than their descriptive names, determine the signs. **4 points.**

### Solution 7

For the one-point space \(Y\), ordinary \(H_0(Y;\mathbb Q)=\mathbb Q\), generated by its positive point. The augmentation is the identity, so reduced \(H_0(Y;\mathbb Q)=0\). The ordinary point nevertheless maps to the nonzero circle in Example 3. **4 points.**

A two-point space has ordinary \(H_0=\mathbb Q^2\) and reduced \(H_0=\{(a,b):a+b=0\}\cong\mathbb Q\), generated by \([p_+]-[p_-]\). Mapping both points to the same point sends that generator to \([p]-[p]=0\) in ordinary \(H_0(Y)\). **4 points.** A deformed affine equator may project to different points, may use a specified inherited orientation, and participates in an actual normal-tube comparison. Its relevant projective class is determined by that full map and cycle, not by replacing its domain with an undeformed two-point set whose images were chosen equal. Those maps and orientations must be computed before applying the receiver. **4 points.**

### Solution 8

The exact preceding Corollary 8.1 in *Rational top forms detect cycles in a hypersurface complement* proves that (12) detects ordinary rational \(d\)-cycle homology on \(V\). It includes the singular and repeated divisor cases and the positive pole exponents. Thus the vanished periods give \(\tau\beta=0\) in \(H_d(V;\mathbb Q)\). One may express the same deduction through complex de Rham detection and then use the faithful map \(H_d(V;\mathbb Q)\to H_d(V;\mathbb C)\), proved in *When zero smooth periods mean that a cycle bounds*. **6 points.**

The affine-level Morse argument and the transfer give \(H_{d+1}(U;\mathbb Q)=0\). The pair sequence therefore makes its relative boundary injective. The exact complex-oriented Thom/excision map is an isomorphism, so its composition with that relative boundary, namely \(\tau\), is injective. Hence \(\beta=0\). **5 points.**

In Example 4, reversing only the normal circle changes the orientation of the tube by \(-1\). Its normalized period becomes \(-1\). **2 points.** To apply the conclusion to another affine cycle, one needs the actual projectivization of that cycle, its relation to the normal-tube map, the inherited orientation, any hemisphere multiplicity or scalar, the coefficient convention and any reduced degree-zero interpretation. The projective receiver supplies none of those identifications automatically. **3 points.**

## 6. What the geometric application still needs

The projective homology bound and the normal-tube injection have now been proved over the coefficient field used by the rational period theorem. The full proof below also supplies the simplex lifting, including why a lift varies continuously with its endpoint.

The next geometric application must identify its actual affine equator with the specified projective class and tube. It must retain orientation and multiplicity, especially in the two-point case. A component argument additionally needs the analytic continuation and all-powers conclusions appropriate to that application. The result here supplies the general projective receiver at its exact internal Thom and finite-chain foundations.

## References

[H] Allen Hatcher, *Algebraic Topology*, Cambridge University Press (2002), §3.G, “Transfer Homomorphisms”. [Author's freely readable text](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf). The transfer required here is proved in full.

[S] Arthur Sard, *The measure of the critical values of differentiable maps*, Bulletin of the American Mathematical Society **48** (1942), 883–890. [Original article](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/sard.pdf). The exact equal-dimensional case has a complete preceding internal proof.

[A] Michael Atiyah, Raoul Bott and Lars Gårding, *Lacunas for hyperbolic differential operators with constant coefficients, II*, Acta Mathematica **131** (1973), 145–206. [Primary article](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6156-11511_2006_Article_BF02392039.pdf). Historical context for the projective tube method; the required homology and transfer arguments are supplied here.

Original exposition and diagrams are CC0-1.0. The linked historical works retain their own rights and are not reproduced.
