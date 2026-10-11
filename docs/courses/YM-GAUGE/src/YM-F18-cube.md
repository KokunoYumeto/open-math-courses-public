# Six outward faces of a cube: exact U(1) holonomy and probability

This finite example keeps the eight vertices, twelve links, six outward
faces and three physical lengths of one rectangular cube. It proves the
complete edge-to-face map, its gauge kernel, its Haar pushforward, and the
probability law obtained by putting the specified circle heat factor on
each of its six faces. Every face time remains an independently specified
positive number. A rectangular planar graph with all boundary links
integrated is constructed separately and compared by explicit maps.

The cube boundary is itself a closed two-dimensional cellulated surface.
Its relation is therefore already a closed-surface effect. The same six
faces occur around a three-dimensional lattice cell; their relation shows
why assigning independent variables to all faces of such cells does not
repeat the free-boundary planar calculation. This example establishes no
four-dimensional continuum measure or assertion about the Wilson-action
continuum limit.

Complete companion to [Unit 18](../established-approaches-and-open-problems.html). Proof labels CF.1–CF.18 and equations C1–C49 locate the complete arguments below.

## CF.1. Physical cube, all vertices and all oriented edges

Fix three physical lengths \(L_1,L_2,L_3>0\). The cell is
\(Q=[0,L_1]\times[0,L_2]\times[0,L_3]\), with orientation
\(dx^1\wedge dx^2\wedge dx^3\). Its vertices are

\[
v_{ijk}=(iL_1,jL_2,kL_3),\qquad i,j,k\in\{0,1\}.
\tag{C1}
\]

The ordered vertex list is
\(000,100,010,110,001,101,011,111\). The twelve designated edges are

\[
x_{jk}:v_{0jk}\longrightarrow v_{1jk},\qquad
y_{ik}:v_{i0k}\longrightarrow v_{i1k},\qquad
z_{ij}:v_{ij0}\longrightarrow v_{ij1}.
\tag{C2}
\]

Their ordered list is

\[
(x_{00},x_{10},x_{01},x_{11},
  y_{00},y_{10},y_{01},y_{11},
  z_{00},z_{10},z_{01},z_{11}).
\tag{C3}
\]

Each designated edge has its indicated physical length \(L_1,L_2,L_3\).
A reversed edge is the same geometric edge with reversed direction; it
is not a thirteenth integration variable. A link configuration is
\(U\in\mathbb T^{12}\), where
\(\mathbb T=U(1)=\{e^{i\theta}:\theta\in\mathbb R/(2\pi\mathbb Z)\}\).
Write \(U_{e^{-1}}=U_e^{-1}\). For a path traversing
\(e_1^{\epsilon_1},\ldots,e_r^{\epsilon_r}\), its transport is
\(U_{e_r}^{\epsilon_r}\cdots U_{e_1}^{\epsilon_1}\), as in the course's
source-to-target convention. Commutativity of U(1), used explicitly in
the following calculations, permits collecting equal edge factors.

## CF.2. Six outward faces and their complete signed boundaries

The outward-first boundary orientation is fixed as follows. On
\(X_-:\{x^1=0\}\) it is \(-dx^2\wedge dx^3\), on
\(X_+:\{x^1=L_1\}\) it is \(+dx^2\wedge dx^3\); on
\(Y_-:\{x^2=0\}\) it is \(+dx^1\wedge dx^3\), on
\(Y_+:\{x^2=L_2\}\) it is \(-dx^1\wedge dx^3\); on
\(Z_-:\{x^3=0\}\) it is \(-dx^1\wedge dx^2\), on
\(Z_+:\{x^3=L_3\}\) it is \(+dx^1\wedge dx^2\).

These signs follow directly by contracting the oriented volume form
with the indicated outward coordinate normal. The table specifies a
starting vertex and the traversal order, so it also fixes the complete
path, not just its underlying square.

| Face | Start | Boundary path in traversal order | Signed cellular boundary |
|---|---|---|---|
| \(X_-\) | \(000\) | \(z_{00},y_{01},z_{01}^{-1},y_{00}^{-1}\) | \(z_{00}+y_{01}-z_{01}-y_{00}\) |
| \(X_+\) | \(100\) | \(y_{10},z_{11},y_{11}^{-1},z_{10}^{-1}\) | \(y_{10}+z_{11}-y_{11}-z_{10}\) |
| \(Y_-\) | \(000\) | \(x_{00},z_{10},x_{01}^{-1},z_{00}^{-1}\) | \(x_{00}+z_{10}-x_{01}-z_{00}\) |
| \(Y_+\) | \(010\) | \(z_{01},x_{11},z_{11}^{-1},x_{10}^{-1}\) | \(z_{01}+x_{11}-z_{11}-x_{10}\) |
| \(Z_-\) | \(000\) | \(y_{00},x_{10},y_{10}^{-1},x_{00}^{-1}\) | \(y_{00}+x_{10}-y_{10}-x_{00}\) |
| \(Z_+\) | \(001\) | \(x_{01},y_{11},x_{11}^{-1},y_{01}^{-1}\) | \(x_{01}+y_{11}-x_{11}-y_{01}\) |

For example the first path is
\(000\to001\to011\to010\to000\), and has the required
\(dx^3\wedge dx^2=-dx^2\wedge dx^3\) orientation. The other five
paths likewise follow their displayed positive first and second tangent
directions; reversal on their last two edges closes each square.

In the edge order C3 and face order
\((X_-,X_+,Y_-,Y_+,Z_-,Z_+)\), the face-circulation matrix is

\[
B=\begin{pmatrix}
0&0&0&0&-1&0&1&0&1&0&-1&0\\
0&0&0&0&0&1&0&-1&0&-1&0&1\\
1&0&-1&0&0&0&0&0&-1&1&0&0\\
0&-1&0&1&0&0&0&0&0&0&1&-1\\
-1&1&0&0&1&-1&0&0&0&0&0&0\\
0&0&1&-1&0&0&-1&1&0&0&0&0
\end{pmatrix}.
\tag{C4}
\]

Thus the edge-to-face holonomy homomorphism is exactly

\[
\Phi:\mathbb T^{12}\longrightarrow\mathbb T^6,
\qquad H_f=\Phi(U)_f=\prod_{e\text{ in C3}}U_e^{B_{fe}}.
\tag{C5}
\]

If real representatives \(\theta_e\) are chosen with
\(U_e=e^{i\theta_e}\), this says \(H_f=e^{i(B\theta)_f}\).
Changing a representative by \(2\pi\) times an integer leaves C5 unchanged.

## CF.3. Cellular boundary, curl and all cancellation signs

Let \(C_0,C_1,C_2,C_3\) be the free integer groups on the eight vertices,
twelve designated edges, six outward faces, and the oriented cube,
respectively. The boundary of an edge is target minus source. Define
\(\partial_2 f\) by the table and

\[
\partial_3 Q=X_-+X_++Y_-+Y_++Z_-+Z_+.
\tag{C6}
\]

Each four-edge path is closed, so summing its four target-minus-source
terms gives zero at every vertex: \(\partial_1\partial_2=0\).
The table also shows every edge exactly twice, with opposite coefficients.
For instance \(x_{00}\) has coefficient \(+1\) in \(Y_-\) and
\(-1\) in \(Z_-\); \(y_{01}\) has \(+1\) in \(X_-\) and
\(-1\) in \(Z_+\); \(z_{11}\) has \(+1\) in \(X_+\) and
\(-1\) in \(Y_+\). C4 gives the remaining nine cancellations without
an orientation convention left implicit. Consequently

\[
\partial_2\partial_3=0,
\qquad (1,1,1,1,1,1)B=0,
\qquad \prod_f H_f=1.
\tag{C7}
\]

For any integer face chain \(c=\sum_f c_f f\), the more general exact
identity is

\[
\prod_f H_f^{c_f}=\prod_e U_e^{(B^{\mathsf T}c)_e}.
\tag{C8}
\]

Indeed C5 substitutes into the left side, and the exponent of each
individual edge is \(\sum_f B_{fe}c_f\). This proves the map from a
face chain to its boundary observable, including all internal and
external boundary factors. C7 is C8 with \(c=\partial_3 Q\).

Here is also its exact differential-calculus relation, with the physical
lengths retained. For a real \(C^2\) one-form
\(a=a_1dx^1+a_2dx^2+a_3dx^3\), set

\[
b_1=\partial_2a_3-\partial_3a_2,\quad
b_2=\partial_3a_1-\partial_1a_3,\quad
b_3=\partial_1a_2-\partial_2a_1.
\tag{C9}
\]

The positive \((x^2,x^3)\) circulation at fixed \(x^1\) equals
\(\int_0^{L_2}\int_0^{L_3}b_1\,dx^3dx^2\): integrate
\(\partial_2a_3\) in \(x^2\), integrate \(-\partial_3a_2\) in
\(x^3\), and the resulting four integrals are exactly the four edge
integrals. The same calculation in positive \((x^3,x^1)\) coordinates
gives \(b_2\); in positive \((x^1,x^2)\) coordinates it gives \(b_3\).
Thus if \(\bar b_1(s)\) is the area average over the face \(x^1=s\),
and \(\bar b_2(s),\bar b_3(s)\) are the respective analogous averages,
the six signed face circulations obey

\[
L_2L_3[\bar b_1(L_1)-\bar b_1(0)]
+L_3L_1[\bar b_2(L_2)-\bar b_2(0)]
+L_1L_2[\bar b_3(L_3)-\bar b_3(0)]=0.
\tag{C10}
\]

This follows either from the twelve exact edge cancellations or from
integrating the following six-term identity:

\[
\partial_1b_1+\partial_2b_2+\partial_3b_3
=\partial_1\partial_2a_3-\partial_1\partial_3a_2
+\partial_2\partial_3a_1-\partial_2\partial_1a_3
+\partial_3\partial_1a_2-\partial_3\partial_2a_1=0.
\tag{C11}
\]

Equality of the paired mixed partial derivatives proves the last step.
No length, area or face contribution has been absorbed into another
quantity. With the course's skew-Hermitian connection \(A=ia\) and
transport equation \(U'=-A(\dot\gamma)U\), direct differentiation gives
\(U_e=\exp(-i\int_e a)\). Hence C5 is
\(H_f=\exp(-i\int_f da)\) with these orientations. The minus sign is
fixed by that transport equation.

For arbitrary lattice links, C7 is a group identity even without a
chosen smooth form. For any simultaneous real lifts of edge angles,
\(\sum_f(B\theta)_f=0\) exactly in \(\mathbb R\). If instead each face
angle is separately replaced by a principal argument \(\phi_f\), the
correct conclusion is \(\sum_f\phi_f\in2\pi\mathbb Z\), not the
unsupported real equation \(\sum_f\phi_f=0\). These statements follow
by subtracting the six integer multiples of \(2\pi\) introduced by
that face-by-face branch selection.

## CF.4. A seven-edge tree and the full gauge coordinate map

Take the root \(v_{000}\) and tree

\[
\mathcal T=\{x_{00},x_{10},x_{01},x_{11},y_{00},y_{01},z_{00}\}.
\tag{C12}
\]

Within each fixed \(k\), the two x edges are joined by \(y_{0k}\) to
form a tree on that layer's four vertices. The edge \(z_{00}\) joins
the two trees. Hence the graph is connected and has no cycle, with
seven edges. Write \(g_v\) for the transport along its unique path
from the root to \(v\). Explicitly,

\[
\begin{array}{c|cccccccc}
v&000&100&010&110&001&101&011&111\\\hline
g_v&1&U_{x_{00}}&U_{y_{00}}&U_{x_{10}}U_{y_{00}}&
U_{z_{00}}&U_{x_{01}}U_{z_{00}}&U_{y_{01}}U_{z_{00}}&
U_{x_{11}}U_{y_{01}}U_{z_{00}}
\end{array}.
\tag{C13}
\]

For a vertex field \(h\), the active gauge action is
\((h\cdot U)_e=h_{t(e)}U_eh_{s(e)}^{-1}\). Along a path, the internal
vertex factors cancel; the path holonomy changes by its target factor
on the left and inverse source factor on the right. For a closed path
they cancel in U(1), proving invariance of each C5.

Apply \(h_v=g_v^{-1}\) and define
\(V_e=g_{t(e)}^{-1}U_eg_{s(e)}\). Each tree link is now 1. Denote the
other five links by

\[
A=V_{y_{10}},\quad B_0=V_{y_{11}},\quad C=V_{z_{10}},
\quad D=V_{z_{01}},\quad E=V_{z_{11}}.
\tag{C14}
\]

The symbol \(B_0\) is a link variable, distinct from matrix \(B\).
The exact inverse to this coordinate change is

\[
U_e=g_{t(e)}V_eg_{s(e)}^{-1},\qquad
g_{000}=1,\quad V_e=1\ (e\in\mathcal T).
\tag{C15}
\]

Indeed it reconstructs all original links. Conversely, the tree
transport of links C15 is \(g_v\), because all successive internal
\(g\) factors cancel, and the root is 1. Thus C15 also recovers each
given non-tree \(V_e\). We have a genuine continuous group isomorphism
\(\mathbb T^{12}\simeq\mathbb T^7\times\mathbb T^5\), with both
directions explicitly specified, not a formal quotient prescription.

## CF.5. Full image, full kernel and inverse on the face torus

Substitution of the tree links into the six signed boundaries gives

\[
(H_{X_-},H_{X_+},H_{Y_-},H_{Y_+},H_{Z_-},H_{Z_+})
=(D^{-1},\ AEB_0^{-1}C^{-1},\ C,\ DE^{-1},\ A^{-1},\ B_0).
\tag{C16}
\]

Let

\[
K=\{h\in\mathbb T^6:
h_{X_-}h_{X_+}h_{Y_-}h_{Y_+}h_{Z_-}h_{Z_+}=1\}.
\tag{C17}
\]

For any \(h\in K\), put all tree links equal to 1 and set

\[
A=h_{Z_-}^{-1},\quad B_0=h_{Z_+},\quad C=h_{Y_-},\quad
D=h_{X_-}^{-1},\quad E=h_{X_-}^{-1}h_{Y_+}^{-1}.
\tag{C18}
\]

The first, third, fourth, fifth and sixth entries of C16 are precisely
the specified entries of \(h\). The remaining entry is
\((h_{X_-}h_{Y_-}h_{Y_+}h_{Z_-}h_{Z_+})^{-1}=h_{X_+}\) by C17.
Thus every point of K occurs. C7 proves that no other point occurs.
The five specified entries also determine A, \(B_0\), C, D and E
uniquely, so C18 is the full tree-gauge inverse.

In particular \(\Phi(U)=1\) forces all five non-tree variables to be
1. By C15 its full kernel is

\[
\ker\Phi
=\{U_e=g_{t(e)}g_{s(e)}^{-1}:g\in\mathbb T^8\}
\simeq\mathbb T^8/\mathbb T_{\rm diagonal}\simeq\mathbb T^7.
\tag{C19}
\]

If two such vertex fields give the same links, their ratio is constant
along each edge, and therefore at all eight vertices by connectivity.
This proves exactly the displayed diagonal kernel, including the
absence of additional discrete components. Fixing the root value to 1
removes precisely that freedom. Every fiber of \(\Phi\) is a coset of
C19: if \(\Phi(U)=\Phi(U')\), the linkwise ratio lies in the kernel.
Equivalently the gauge quotient is exactly K, not merely a space of the
same dimension.

Projection to \((X_-,Y_-,Y_+,Z_-,Z_+)\) identifies K with
\(\mathbb T^5\), with the missing \(X_+\) coordinate determined by
C17. It follows directly that K is connected and five-dimensional.
All formulas C13–C18 use integer exponents and have integer-exponent
inverses. The same formulas with multiplication replaced by addition
and inversion by minus therefore prove the exact integer cochain
sequence

\[
0\longrightarrow\mathbb Z\xrightarrow{\rm diagonal}\mathbb Z^8
\xrightarrow{d_0}\mathbb Z^{12}\xrightarrow{B}\mathbb Z^6
\xrightarrow{\Sigma}\mathbb Z\longrightarrow0,
\quad (d_0g)_e=g_{t(e)}-g_{s(e)},\quad \Sigma c=\sum_f c_f.
\tag{C20}
\]

For completeness: the kernel of \(d_0\) consists of constants by
connectivity; every B-flat edge vector is its tree potential plus a
zero non-tree vector by the additive C16–C18; every six-vector of
sum zero is the additive C16 image using C18; and \(\Sigma\) is onto
by setting just one coordinate to an arbitrary integer. These prove
each exactness assertion without using dimension counts to discard
possible integer torsion. The same proof works over \(\mathbb R\),
over \(\mathbb R/(2\pi\mathbb Z)\), and over \(\mathbb Z/q\mathbb Z\)
for every integer \(q\geq2\).

## CF.6. Exact Haar pushforward, including every gauge coordinate

On \(\mathbb T\) use probability Haar measure
\(dm(e^{i\theta})=d\theta/(2\pi)\). Translation and inversion preserve
this measure by ordinary one-variable substitution modulo \(2\pi\).
Choose a tree order with each parent before its child. Conditional on
the earlier vertices, replacing the link to a child by \(g_v\) is a
translation of one circle variable; its measure stays \(dm\).
After all seven replacements, C15 replaces each remaining original
link by a translation of its V variable. Successive integration proves

\[
\prod_{e\in\mathrm{C3}}dm(U_e)
=\prod_{v\ne000}dm(g_v)\,dm(A)dm(B_0)dm(C)dm(D)dm(E)
\tag{C21}
\]

as a change-of-variables identity for every bounded Borel integrand.
Here and below such product identities mean equality of the integrals
under the displayed bijections.

Change from D to \(h_{X_-}=D^{-1}\), from C to \(h_{Y_-}=C\),
from E to \(h_{Y_+}=DE^{-1}\) after D is fixed, from A to
\(h_{Z_-}=A^{-1}\), and from \(B_0\) to \(h_{Z_+}=B_0\).
Each step is an inversion or a translation followed by inversion and
preserves the appropriate conditional circle probability. Thus the
five displayed h variables are independent Haar before any density
is imposed. Define \(q:\mathbb T^5\to K\) by adjoining their inverse
product as \(h_{X_+}\), and set \(\lambda_K=q_*m^{\otimes5}\).
It follows from C21 that

\[
\Phi_*m^{\otimes12}=\lambda_K,
\qquad
\mathbb T^{12}\simeq\mathbb T^7\times K
\text{ carries }m^{\otimes7}\otimes\lambda_K.
\tag{C22}
\]

The measure \(\lambda_K\) is Haar probability on K: q is an onto
group homomorphism and circle product Haar is invariant under every
translation, so its pushforward is invariant under every translation
in K. Uniqueness can also be proved here. For another invariant
probability \(\eta\) and any continuous f, integrate \(f(xy)\) against
\(\lambda_K(dx)\eta(dy)\) in the two orders. Translation invariance
of \(\lambda_K\) gives \(\int f\,d\lambda_K\), and invariance of
\(\eta\) gives \(\int f\,d\eta\). Hence the two probabilities agree
(continuous functions determine finite Borel measures on this compact
torus; alternatively apply the same averaging to Borel indicators).

Any other five face coordinates give the same product Haar
description: permute which coordinate is omitted in the definition of
q. That map is again a group isomorphism and gives an invariant
probability, which must equal \(\lambda_K\). There is no extra
Jacobian constant and no uncomputed gauge-volume factor in C22.

Finally, for integers \(k_f\), parametrization by any five coordinates
gives the exact character integral

\[
\int_K\prod_f h_f^{k_f}\,d\lambda_K(h)
=\begin{cases}1,&k_{X_-}=k_{X_+}=k_{Y_-}=k_{Y_+}=k_{Z_-}=k_{Z_+},\\
0,&\text{otherwise}.
\end{cases}
\tag{C23}
\]

Indeed omission of \(X_+\) leaves powers \(k_f-k_{X_+}\) of five
independent Haar variables, whose integrals vanish unless each power
is zero. Thus the complete integer annihilator of K is
\(\mathbb Z(1,1,1,1,1,1)\).

## CF.7. The prescribed circle heat factor and convergence

For the circle with angle coordinate \(\theta\) and operator
\(\partial_\theta^2\), define, for each \(t>0\),

\[
p_t(\theta)=\sum_{n\in\mathbb Z}e^{-tn^2}e^{in\theta}
=1+2\sum_{n=1}^{\infty}e^{-tn^2}\cos(n\theta).
\tag{C24}
\]

This is the requested factor relative to \(d\theta/(2\pi)\), with no
rescaling of its angle, operator or time. For any integer \(N\geq0\),
its truncation at \(|n|\leq N\) has uniform error at most

\[
\varepsilon_N(t)=
\frac{2e^{-t(N+1)^2}}{1-e^{-t(2N+3)}}.
\tag{C25}
\]

To prove it, write \(n=N+1+j\), \(j\geq0\), and use
\(n^2\geq(N+1)^2+(2N+3)j\). The geometric sum of these bounds is C25.
Absolute uniform convergence follows. Multiplying a term by any fixed
power of n preserves summability: for large \(|n|\),
\(|n|^r\leq C_{r,t}e^{tn^2/2}\), because the continuous function
\(x^re^{-tx^2/2}\) is bounded on \([0,\infty)\).
The same bounds uniformly on \(t\geq\tau>0\) justify every finite
number of angle and time derivatives. Hence \(p_t\) is smooth and
\(\partial_t p_t=\partial_\theta^2p_t\). It is real, even and
\(2\pi\)-periodic. Termwise integration gives \(\int p_t\,dm=1\).

## CF.8. Gaussian image formula, strict positivity and convolution

The exact image formula, including its Haar-relative multiplier, is

\[
p_t(\theta)=\sqrt{\frac{\pi}{t}}
\sum_{k\in\mathbb Z}
\exp\!\left[-\frac{(\theta+2\pi k)^2}{4t}\right].
\tag{C26}
\]

Here is a proof without assuming positivity of the Fourier series.
For \(\theta\in[-\pi,\pi]\), the terms with \(|k|\geq1\) are bounded
by \(\exp[-\pi^2(2|k|-1)^2/(4t)]\). Thus the image series converges
uniformly to a continuous periodic function. Its n-th Fourier
coefficient, after shifting each integration interval by \(2\pi k\), is

\[
\frac{\sqrt{\pi/t}}{2\pi}
\int_{\mathbb R}e^{-x^2/(4t)}e^{-inx}\,dx=e^{-tn^2}.
\]

The exchange of sum and integral is justified by the integrable
Gaussian absolute value. To verify the Gaussian integral explicitly,
let \(F(b)=\int_{\mathbb R}e^{-x^2/(4t)}e^{-ibx}\,dx\).
Differentiating in b and integrating by parts, with zero Gaussian
boundary terms, gives \(F'(b)=-2tbF(b)\). Thus
\(F(b)=F(0)e^{-tb^2}\). Squaring the positive real integral and
using polar coordinates in \(\mathbb R^2\) gives
\(F(0)^2=4\pi t\), so \(F(0)=2\sqrt{\pi t}\). This proves the
coefficient and every multiplier in the displayed equality.

For the Fourier uniqueness used in this argument, the Fejér kernel
\(F_N(u)=(N+1)^{-1}|\sum_{j=0}^N e^{iju}|^2\) is nonnegative,
has Haar integral 1, and has only finitely many Fourier coefficients.
For \(\delta\leq|u|\leq\pi\) it is at most
\(1/[(N+1)\sin^2(\delta/2)]\), by summing the finite geometric
series. Uniform continuity of a continuous circle function then
splits its convolution error into \(|u|<\delta\), where the function
changes uniformly little, and the complementary part, whose mass
tends to zero by that bound. Thus Fejér convolution tends uniformly
to the function. A continuous function with all Fourier coefficients
zero has all those convolutions zero, and is zero. Apply this to the
difference between C24 and C26 to prove equality.

Choose a representative with \(|\theta|\leq\pi\); the \(k=0\) summand
in C26 proves the global bound

\[
0<\sqrt{\frac{\pi}{t}}e^{-\pi^2/(4t)}\leq p_t(\theta)
\leq 1+2\sum_{n=1}^{\infty}e^{-tn^2}<\infty.
\tag{C27}
\]

This proves strict positivity for all positive times, including angles
where cancellation of Fourier terms is substantial. The Gaussian
formula also verifies the initial heat point mass: for continuous
periodic f,


\[
\int f(\theta)p_t(\theta)dm
=(4\pi t)^{-1/2}\int_{\mathbb R}f(x)e^{-x^2/(4t)}dx
\]

.
The change \(x=2\sqrt t\,y\) gives
\(\pi^{-1/2}\int f(2\sqrt t\,y)e^{-y^2}dy\), which tends to f(0)
by bounded convergence and the Gaussian integral just proved.

Lastly, expanding both absolutely summable Fourier series and
integrating each term proves

\[
\int_{\mathbb T}p_s(\theta-u)p_t(u)\,dm(u)=p_{s+t}(\theta),
\qquad s,t>0.
\tag{C28}
\]

Only equal Fourier indices survive, with coefficient
\(e^{-sn^2}e^{-tn^2}=e^{-(s+t)n^2}\). This proves all convolution
identities used below, including their signs and time sums.

## CF.9. Six individual times and the full cube partition function

Assign the six independently specified positive numbers

\[
t_{X_-},t_{X_+},t_{Y_-},t_{Y_+},t_{Z_-},t_{Z_+}>0.
\]

They need not coincide; none is set equal to another. For shorter
displayed sums only, write
\(T=t_{X_-}+t_{X_+}+t_{Y_-}+t_{Y_+}+t_{Z_-}+t_{Z_+}\).
This abbreviation does not replace the individual factors in the
original measure

\[
d\mu_{\mathbf t}(U)=\frac1{Z_{\mathbf t}}
\prod_{f\in\{X_-,X_+,Y_-,Y_+,Z_-,Z_+\}}p_{t_f}(\arg H_f(U))
\prod_{e\in\mathrm{C3}}dm(U_e).
\tag{C29}
\]

Periodicity makes the argument choice immaterial. C27 bounds the
product above and below by positive finite constants on the compact
space, so its mass exists and is strictly positive. C22 sends this to
independent Haar gauge coordinates and the face law

\[
d\nu_{\mathbf t}(h)=\frac{\prod_f p_{t_f}(\arg h_f)}{Z_{\mathbf t}}
d\lambda_K(h),\qquad
Z_{\mathbf t}=
\sum_{n\in\mathbb Z}
e^{-t_{X_-}n^2}e^{-t_{X_+}n^2}
e^{-t_{Y_-}n^2}e^{-t_{Y_+}n^2}
e^{-t_{Z_-}n^2}e^{-t_{Z_+}n^2}
=p_T(0).
\tag{C30}
\]

To prove the partition identity, expand the six heat factors. The sum
of the absolute values of all terms is
\(\prod_f\sum_n e^{-t_fn^2}<\infty\), independent of h, so Fubini
and termwise integration are valid. C23 retains exactly the terms
whose six indices equal a common n. That is the six-factor sum C30.
In particular \(Z_{\mathbf t}=1+2\sum_{n\geq1}e^{-Tn^2}>1\) for
every finite choice of these times. Its truncation has error at most
\(\varepsilon_N(T)\). The smooth strictly positive probability law
on K and all independent Haar gauge factors have now been constructed.
Gauge invariance follows from CF.4; no gauge coordinates were removed
from the original link integration.

## CF.10. Every joint Fourier moment, with a convergent error bound

For every integer six-vector \(k=(k_f)\), define
\(M_{\mathbf t}(k)=\mathbb E_{\nu_{\mathbf t}}\prod_f H_f^{k_f}\).
The exact answer is

\[
M_{\mathbf t}(k)
=\frac{\displaystyle\sum_{n\in\mathbb Z}
\exp\!\left[-\sum_f t_f(n-k_f)^2\right]}
{\displaystyle\sum_{n\in\mathbb Z}\exp\!\left[-\sum_f t_fn^2\right]}.
\tag{C31}
\]

In expanded form the numerator exponent contains separately



\[
-t_{X_-}(n-k_{X_-})^2,-t_{X_+}(n-k_{X_+})^2,
-t_{Y_-}(n-k_{Y_-})^2,-t_{Y_+}(n-k_{Y_+})^2,
-t_{Z_-}(n-k_{Z_-})^2,-t_{Z_+}(n-k_{Z_+})^2
\]


.
Indeed after expansion of the original six factors the character
integral is nonzero exactly when all six integers \(n_f+k_f\) equal
one integer n, so \(n_f=n-k_f\). Absolute convergence is inherited
from the six-series product; alternatively the positive quadratic
terms give a direct Gaussian majorant. Every numerator summand is
positive. Inversion of all six face variables preserves both K and
the density, so these expectations are real and
\(M_{\mathbf t}(-k)=M_{\mathbf t}(k)\). Also
\(M_{\mathbf t}(k+r\mathbf1)=M_{\mathbf t}(k)\) by changing n to
n+r, exactly as the constraint requires.

An explicit tail is useful for reproducible calculations. Put
\(K_0=\max_f|k_f|\), choose an integer \(N\geq K_0\), and set
\(J=N+1-K_0\geq1\). For \(|n|\geq N+1\),
\(\sum_f t_f(n-k_f)^2\geq T(|n|-K_0)^2\). Therefore the omitted
numerator tail is at most

\[
R_N(k)=\frac{2e^{-TJ^2}}{1-e^{-T(2J+1)}}.
\tag{C32}
\]

This is the same geometric-square estimate as CF.7. If \(A_N\) and
\(D_N\) are the numerator and denominator truncated to \(|n|\leq N\),
then \(D_N\geq1\), and

\[
\left|M_{\mathbf t}(k)-\frac{A_N}{D_N}\right|
\leq R_N(k)+A_N\varepsilon_N(T).
\tag{C33}
\]

Indeed, split the fraction difference into the omitted numerator over
the full denominator and the retained numerator times the reciprocal
denominator difference; both denominators are at least 1.

For any two integer vectors k and l, C31 gives both full correlations
\(\mathbb E[\chi_k\chi_l]=M_{\mathbf t}(k+l)\) and
\(\mathbb E[\chi_k\overline{\chi_l}]=M_{\mathbf t}(k-l)\),
where \(\chi_k=\prod_f H_f^{k_f}\). Subtracting the respective
products of the means gives either covariance convention. Finite
linear combinations supply all trigonometric polynomial observables.
They determine the entire probability: pull back to the five angle
coordinates of K and apply the product of the five Fejér kernels.
The one-coordinate uniform approximation proof in CF.8, performed
successively in each coordinate, uniformly approximates every
continuous function on K. Thus C31 really specifies all joint laws,
not only a selected collection of expectations.

## CF.11. Every proper face marginal and its exact density

Let \(S\) be any nonempty proper subset of the six faces, and write
\(R=F\setminus S\), \(T_S=\sum_{f\in S}t_f\),
\(T_R=\sum_{f\in R}t_f>0\). Its face marginal is the following
strictly positive density relative to independent Haar on
\(\mathbb T^{|S|}\):

\[
\frac{d(\nu_{\mathbf t})_S}{\prod_{f\in S}dm(h_f)}
=\frac{\displaystyle
\left[\prod_{f\in S}p_{t_f}(\theta_f)\right]
p_{T_R}\!\left(-\sum_{f\in S}\theta_f\right)}{p_T(0)}.
\tag{C34}
\]

In particular this retains every original factor in S and the exact
integrated contribution of all omitted faces. To prove it, omit one
coordinate \(r_0\in R\) in the Haar parametrization of K. Its angle
is \(-\sum_{f\ne r_0}\theta_f\) modulo \(2\pi\). Integrate the
other \(|R|-1\) variables in R. Each such integral is C28, with
the accumulated negative sum as its argument, and adds exactly the
time of the integrated factor. After all these integrations it is
\(p_{T_R}(-\sum_{S}\theta_f)\). No integration is needed when R is
a singleton, and that same expression is then immediate. This
proves C34. Its integral is 1 because integrating S by the same
convolution leaves \(p_T(0)/p_T(0)\).

For a single face f, the formula is

\[
d(\nu_{\mathbf t})_f(e^{i\theta})
=\frac{p_{t_f}(\theta)p_{\sum_{g\ne f}t_g}(-\theta)}{p_T(0)}
\frac{d\theta}{2\pi}.
\tag{C35}
\]

For two distinct faces f,g, with \(a=t_f,b=t_g\) and
\(r=\sum_{u\ne f,g}t_u>0\), it is

\[
d(\nu_{\mathbf t})_{f,g}(e^{ix},e^{iy})
=\frac{p_a(x)p_b(y)p_r(-x-y)}{p_{a+b+r}(0)}
\frac{dx\,dy}{(2\pi)^2}.
\tag{C36}
\]

For five faces, C34 contains the sixth original factor evaluated at
their negative sum. Their unweighted Haar coordinates are independent
by CF.6; their weighted law C34 is different.

There is also an exact law for the product of any proper nonempty set
of face holonomies. If \(Y_S=\prod_{f\in S}H_f=e^{i\phi}\), then

\[
d\mathcal L(Y_S)(e^{i\phi})
=\frac{p_{T_S}(\phi)p_{T_R}(-\phi)}{p_T(0)}\frac{d\phi}{2\pi},
\quad
\mathbb E(Y_S^m)
=\frac{\sum_{n\in\mathbb Z}e^{-T_S(n-m)^2-T_Rn^2}}{p_T(0)}.
\tag{C37}
\]

To see the density, use the same successive translation substitution
that proves convolution: the product of independent variables with
densities \(p_{t_f}\) for \(f\in S\) has density \(p_{T_S}\).
In C34 the extra factor depends on those variables only through their
product, so it is carried unchanged to \(p_{T_R}(-\phi)\).
The moment follows from C31 with k equal to m on S and zero on R,
or from two Fourier series in the displayed density. The empty
product and the product of all six faces are both 1; C37's positive
time densities are claimed only for nonempty proper S.

## CF.12. Concrete strict correlations between every pair of faces

Let \(\phi_f\) be any angle for \(H_f\); sine and cosine are
branch-independent. Inversion symmetry gives
\(\mathbb E\sin\phi_f=0\). For distinct f,g, let \(a=t_f>0\),
\(b=t_g>0\), retain \(T=\sum_u t_u\), and let \(e_f,e_g\) be the
integer coordinate vectors. Expanding the full exponent in C31,
without omitting any term, gives

\[
M_{\mathbf t}(e_f-e_g)
=\frac{e^{-a-b}}{p_T(0)}
\sum_{n\in\mathbb Z}e^{-Tn^2+2n(a-b)},\qquad
M_{\mathbf t}(e_f+e_g)
=\frac{e^{-a-b}}{p_T(0)}
\sum_{n\in\mathbb Z}e^{-Tn^2+2n(a+b)}.
\tag{C38}
\]

These are exact rearrangements of C31 with the same original times.
Pairing n with −n and using
\(\sin x\sin y=[\cos(x-y)-\cos(x+y)]/2\) proves

\[
\operatorname{Cov}(\sin\phi_f,\sin\phi_g)
=-\frac{2e^{-a-b}}{p_T(0)}
\sum_{n=1}^{\infty}e^{-Tn^2}\sinh(2na)\sinh(2nb)<0.
\tag{C39}
\]

The identity
\(\cosh(u-v)-\cosh(u+v)=-2\sinh u\sinh v\) follows by writing
both hyperbolic functions in exponentials. Every summand on the
right of C39 before the minus sign is positive, and at least its
n=1 term is nonzero. Convergence follows from the Gaussian factor
times at most \(e^{2n(a+b)}\). Thus every pair of distinct outward
face holonomies is dependent for all six finite positive times.
Reversing one face orientation negates its sine observable and hence
the sign of this covariance; the statement C39 refers to the
specified outward orientations.

The effect also appears in a one-face mean. C31 gives

\[
\mathbb E\cos\phi_f
=e^{-t_f}\frac{1+2\sum_{n\geq1}e^{-Tn^2}\cosh(2nt_f)}
{1+2\sum_{n\geq1}e^{-Tn^2}}
\quad\text{and hence}\quad
e^{-t_f}<\mathbb E\cos\phi_f<1.
\tag{C40}
\]

The first strict inequality follows term by term from
\(\cosh(2nt_f)>1\). For the second, C35 is a strictly positive
density on the circle, and \(1-\cos\theta\) is positive on a set
of positive Haar measure, so its expectation is positive. Both
inequalities are established at finite times, without a limiting
Gaussian approximation to the constrained angles.

## CF.13. Quantitative comparison with six independent heat variables

Let \(\rho_{\mathbf t}=\bigotimes_f[p_{t_f}dm]\) on \(\mathbb T^6\).
This fully specified comparison measure has mass 1 by CF.7, joint
moments \(\exp[-\sum_f t_fk_f^2]\), and independent components.
Their product has density \(p_T\) by C28. Under the cube measure,
the same product is exactly 1, whose m-th moment is 1; under
\(\rho_{\mathbf t}\) that moment is \(e^{-Tm^2}<1\) for any
nonzero integer m. The cube partition is C30, whereas the independent
six-face product has partition 1.

There is a stronger exact distinction for the full six-face laws.
The set K has ambient \(m^{\otimes6}\)-measure zero: fixing any five
coordinates leaves one specified point in the sixth circle, of Haar
measure zero, and Fubini applies. Since \(\rho_{\mathbf t}\) has a
continuous density with respect to that ambient measure,
\(\rho_{\mathbf t}(K)=0\), while \(\nu_{\mathbf t}(K)=1\).
They are mutually singular and their total variation distance,
defined as \(\sup_A|\nu(A)-\rho(A)|\), is exactly 1.

Proper marginals nevertheless admit an explicit comparison. Define
\(E(s)=2\sum_{n\geq1}e^{-sn^2}\), so
\(E(s)\leq2e^{-s}/(1-e^{-3s})\) by C25 with N=0. From C34,

\[
\frac{d(\nu_{\mathbf t})_S}{d(\rho_{\mathbf t})_S}
=\frac{p_{T_R}(-\sum_{f\in S}\theta_f)}{1+E(T)},\qquad
\left|\frac{d(\nu_{\mathbf t})_S}{d(\rho_{\mathbf t})_S}-1\right|
\leq\frac{E(T_R)+E(T)}{1+E(T)}.
\tag{C41}
\]

The bound follows from \(|p_s-1|\leq E(s)\) and the triangle
inequality, with its denominator retained. Integrating this bound
against the probability \((\rho_{\mathbf t})_S\) and using the
one-half L1 formula for two densities gives

\[
\| (\nu_{\mathbf t})_S-(\rho_{\mathbf t})_S\|_{\rm TV}
\leq\min\left\{1,\frac{E(T_R)+E(T)}{2[1+E(T)]}\right\}.
\tag{C42}
\]

The one-half formula follows by splitting the signed density
difference into its positive and negative parts; its integral is
zero, so those two parts have equal integral, and the positive set
attains the supremum. In particular, if the times in S are fixed
while the sum of omitted times tends to infinity, the proper marginal
tends in total variation to the independent heat variables on S.
The full six-face singularity proved above persists for every finite
choice of times. No conditioning of an ambient law on a probability
zero event was used to define the cube probability.

## CF.14. Removing one face factor and the exact retained-coordinate map

Keep the twelve links and the same seven-edge tree, and include heat
factors only on \(F\setminus\{X_+\}\). Equations C18 and C22 prove
that those five face variables range independently over all of
\(\mathbb T^5\), with product Haar before weighting. Their weighted
partition is therefore exactly 1 and their joint law is the product
of their five individual heat laws. The omitted holonomy, if still
measured along its boundary path, remains their inverse product and
has heat law \(p_{\sum_{f\ne X_+}t_f}\,dm\), by convolution and
evenness. Adding the sixth heat factor changes this product law by
multiplication by
\(p_{t_{X_+}}(-\sum_{f\ne X_+}\theta_f)\), and division by the
exact resulting mass C30. Thus the change from five free face
coordinates to the six-factor constrained law is an actual
specified probability operation. The same statement holds with
any one face omitted, by CF.6.

It also follows directly as a limit: let \(t_{X_+}\to\infty\) while
the other five times stay fixed. C25 implies uniform
\(p_{t_{X_+}}\to1\) and \(p_T(0)\to1\); hence C34 tends uniformly
in density, and in total variation, to their product law. The other
five faces and all original link coordinates remain the same objects.

## CF.15. The actual planar rectangular graph with free boundary

Fix \(L_1,L_2>0\) and integers \(N_1,N_2\geq1\). Its vertices are
\(w_{ij}=(iL_1/N_1,jL_2/N_2)\),
\(0\leq i\leq N_1,\ 0\leq j\leq N_2\). Let \(h_{ij}\) be the
east edge from \(w_{ij}\) to \(w_{i+1,j}\), and \(v_{ij}\) the
north edge from \(w_{ij}\) to \(w_{i,j+1}\). The respective edge
ranges are \(0\leq i<N_1,0\leq j\leq N_2\) and
\(0\leq i\leq N_1,0\leq j<N_2\). Every such edge, including
each outer boundary edge, is integrated with circle Haar probability.
This is what free boundary means here.

For each cell \((i,j)\), with \(0\leq i<N_1,0\leq j<N_2\),
the positive boundary travels east, north, west, south. Its holonomy is

\[
P_{ij}=U_{v_{ij}}^{-1}U_{h_{i,j+1}}^{-1}
U_{v_{i+1,j}}U_{h_{ij}}.
\tag{C43}
\]

Choose all horizontal edges and all left-column vertical edges
\(v_{0j}\) as tree, rooted at \(w_{00}\). Each horizontal row is
a chain attached once to the left-column chain, so this is a tree.
Its edge number is \(N_1(N_2+1)+N_2=|V|-1\); the other
\(N_1N_2\) links are vertical \(v_{ij}\) with \(i\geq1\).
Use its root transports and the gauge change of CF.4. Set
\(V_{0j}=1\); the other gauge-transformed vertical links are
\(V_{ij}\in\mathbb T\). All horizontal links equal 1, so C43 becomes

\[
P_{ij}=V_{i+1,j}V_{ij}^{-1},\qquad
V_{ij}=\prod_{r=0}^{i-1}P_{rj}\quad(1\leq i\leq N_1).
\tag{C44}
\]

The product for \(i=0\) is empty and equals 1. Multiplying the first
formula for successive r telescopes to the second, and inserting
the second into the first recovers each \(P_{ij}\). This proves
that the full planar face map is onto \(\mathbb T^{N_1N_2}\).
Its kernel consists exactly of the tree gauge fields: if every
P is 1, C44 makes every V equal 1, and the inverse C15 gives the
vertex difference links. Their kernel on vertex fields is precisely
the constant diagonal, by connectivity.

The tree substitution preserves Haar by the proof of CF.6. Within
each row j, change \(V_{1j}\) to \(P_{0j}\), then \(V_{2j}\) to
\(P_{1j}\), successively: the preceding V is already determined,
so every step is a translation of the next Haar circle. It follows
that all the P variables are independent Haar. For any individually
specified face times \(s_{ij}>0\), the full link density
\(\prod_{ij}p_{s_{ij}}(P_{ij})\) has partition exactly 1, and the
face law is exactly

\[
\bigotimes_{0\leq i<N_1,\,0\leq j<N_2}
\left[p_{s_{ij}}(\theta_{ij})\frac{d\theta_{ij}}{2\pi}\right],
\tag{C45}
\]

independently of every Haar tree coordinate. This proves the
free-boundary planar product calculation from its original links,
not by assuming that the face variables were independent to start.

## CF.16. The exact boundary map relating the planar and cube cases

The sum of all positive rectangular cells has boundary equal to
the positively oriented outer perimeter. Each internal edge occurs
once in each direction and cancels; each perimeter edge occurs just
once with its induced sign. The same exponent collection as in C8
therefore gives the exact equality

\[
H_{\partial R}=\prod_{i=0}^{N_1-1}\prod_{j=0}^{N_2-1}P_{ij}.
\tag{C46}
\]

This is an equality of circle-valued observables. Its law under C45
is \(p_{\sum_{ij}s_{ij}}dm\), and its m-th expectation is
\(e^{-m^2\sum_{ij}s_{ij}}\), by CF.8. Thus the right side is not
required to equal 1 when all perimeter links are integrated. If a
boundary holonomy were prescribed, it would impose a different
probability problem; that is not the free-boundary graph defined
in CF.15.

For the cube, all six faces together have zero edge boundary, by C7,
so the same map C8 sends their total to the identity observable.
For its five faces other than \(X_+\), their total edge boundary
is \(-\partial_2X_+\). Hence their holonomy product is precisely
\(H_{X_+}^{-1}\). This is the exact morphism that relates the free
five coordinates to the closed six-face constraint. More generally,
C8 applies to every subset with its full signed boundary. The
change in independence is accounted for by that boundary map and
the included density factors, while keeping every original edge
and face observable identifiable.

The cube calculation uses U(1) essentially when edge factors are
collected in C8. For a non-Abelian group a six-fold product of raw
untransported face matrices does not follow from this Abelian
cancellation proof. The full SU(2) planar tree map in the [SU(2) graph chapter](../two-dimensional-holonomy-probability.html) has its own ordered products and based paths; this
finite U(1) comparison makes no replacement of those maps.

## CF.17. Separate exact check with the retained Wilson factors

The preceding heat measure remains C29. To keep its relation to the
course's original action explicit, the same geometric map can also
be evaluated for a separately specified U(1) Wilson action

\[
S_W(U)=\hbar\sum_f\beta_f[1-\operatorname{Re}H_f(U)],
\qquad \beta_f\geq0,
\quad e^{-S_W/\hbar}=e^{-\sum_f\beta_f}\prod_f e^{\beta_f\cos\phi_f}.
\tag{C47}
\]

Here \(\hbar>0\), all \(\beta_f\) are dimensionless, and the
constant \(e^{-\sum_f\beta_f}\) remains in the partition. Define

\[
I_n(\beta)=\sum_{r=0}^{\infty}
\frac{(\beta/2)^{2r+|n|}}{r!(r+|n|)!}.
\tag{C48}
\]

Expanding
\(e^{\beta\cos\theta}=e^{(\beta/2)e^{i\theta}}
e^{(\beta/2)e^{-i\theta}}\) gives an absolutely summable double
series of absolute total \(e^\beta\). Collecting the exponent n
gives C48 and
\(e^{\beta\cos\theta}=\sum_{n\in\mathbb Z}I_n(\beta)e^{in\theta}\).
Thus C23 proves, with all original constant terms retained,

\[
Z_{W,\rm cube}=e^{-\sum_f\beta_f}\sum_{n\in\mathbb Z}\prod_f I_n(\beta_f),
\quad
\mathbb E_W\prod_f H_f^{k_f}
=\frac{\sum_{n\in\mathbb Z}\prod_f I_{n-k_f}(\beta_f)}
{\sum_{n\in\mathbb Z}\prod_f I_n(\beta_f)}.
\tag{C49}
\]

The Fourier product is absolutely integrable since its absolute sum
is at most \(\prod_f e^{\beta_f}\), and the denominator is positive
because its n=0 term is positive. In the free-boundary planar graph
CF.15 the exact partition is instead
\(\prod_{ij}e^{-\beta_{ij}}I_0(\beta_{ij})\), with independent
face densities \(e^{\beta_{ij}\cos\theta}/I_0(\beta_{ij})\).
This proves the same geometric distinction for that separately
retained action. No identification of C47 with C29, no equality
between their Fourier factors, and no change to a continuum action
is part of this calculation.

## CF.18. Human-source comparison and scope of the derivation

The source-to-target and tree constructions are also developed in the
[SU(2) graph chapter](../two-dimensional-holonomy-probability.html),
GP.1–GP.7, and the U(1) Wilson calculation in
[Unit 15](../strong-coupling-simulations-errors.html), SC.1–SC.8.
The present chapter rederives every finite claim used here.

The relevant original-author context is Thierry Lévy,
[*Yang-Mills measure on compact surfaces*, math/0101239v1](https://arxiv.org/abs/math/0101239v1),
original `chap1.tex`, lines 224–352. Lines 269–294 give the gauge
variable j and reverse path-product order. Their conversion to our
active gauge convention is exactly \(j_v=h_v^{-1}\); the edge formula
\(j_{t(e)}^{-1}U_ej_{s(e)}\) then becomes our
\(h_{t(e)}U_eh_{s(e)}^{-1}\). Lines 323–347 define the heat-density
construction and its partition factor. The source uses the half-Laplacian
heat equation. To make the metric factor explicit, a circle of
circumference \(\ell>0\) in this same angle coordinate has metric
\((\ell/2\pi)^2d\theta^2\), arclength measure
\((\ell/2\pi)d\theta\), and Laplacian
\(\Delta_\ell=(2\pi/\ell)^2\partial_\theta^2\). Its Haar probability
is still \(d\theta/(2\pi)\). The half-Laplacian equation therefore
has Fourier coefficients
\(\exp[-(s_f/2)(2\pi/\ell)^2n^2]\). Its exact comparison to C24 is
\(t_f=(s_f/2)(2\pi/\ell)^2\), separately on every face.
For the identical angle metric \(d\theta^2\), one has \(\ell=2\pi\)
and \(s_f=2t_f\). The source's stated unit Riemannian-volume convention,
when applied to the circle itself, has \(\ell=1\) and instead
\(s_f=t_f/(2\pi^2)\). These are distinct metric conventions with
their complete conversion, retaining the circumference factor.
No physical coupling value is inferred from the heat-time notation.

The original source `chap1.tex` line 585 prints a convolution of
\(p_s\) with \(p_t\) equal to \(p_t\). For the heat factors as
printed, the right time is \(s+t\), as C28 proves directly; the
display could alternatively use \(p_{t-s}\) for its second factor
when \(0<s<t\). This is the same source correction already noted
by the retained F18 provider. It is not a newly attributed error
in the course's correctly added heat times.

The original-source body comparison was limited to
`chap1.tex` lines 9–76, 224–352 and 575–645, from the preserved
math/0101239v1 author-source archive. No PDF was read, and no later
all-path or bundle-sector theorem was imported. In particular the
elementary cube links above do not identify a principal-argument
integer with a continuum Chern class; CF.3 states exactly the
branch information actually proved. The source archive identity, bounded reading coverage and correction record appear in the lesson provenance. This is an established
finite teaching example, with no novelty claim.
