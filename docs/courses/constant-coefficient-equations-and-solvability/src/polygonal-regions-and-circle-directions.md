# Polygonal regions and the directions on a circle

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October 2026. Self-checked by GPT-6.1 Sol (OpenAI). Public domain (CC0).*

Connectedness turns local planar information into a global geometric constraint. We prove polygonal connectivity, describe the arcs left by finitely many marked directions, and prove that a simple finite polygon has one bounded region and one exterior region.

We use finite-dimensional calculus, compactness and interval connectedness. The scalar factorization theorem in [Polynomial and contour interfaces for stable boundary models](../prerequisites/stable-prerequisite-bridges.html), Sections 9.1–9.4, supplies finite roots for the homogeneous directional polynomial. [Planar domains and directional solvability](planar-domains-and-directional-solvability.md) applies the geometry.

Erickson’s notes give an elementary account of polygon separation, and Seidel’s course develops polygonal winding numbers. The proof below uses the index jump and connected strips along the edges.

## Paths in an open set and arcs on a circle

**Lemma 1.1 (polygonal connectedness).** A connected open subset \(U\subset\mathbb R^d\) is polygonally connected.

**Proof.** Fix \(p\in U\), and let \(A\) be the set of points reachable from \(p\) by finitely many straight segments lying in \(U\). At each \(q\in U\) there is a ball \(B(q,r)\subset U\). If \(q\in A\), every point of this ball is reachable by appending the segment from \(q\); hence \(A\) is relatively open. If \(q\notin A\), no point of this ball can lie in \(A\), since its segment to \(q\) would otherwise make \(q\) reachable. Thus the complement is relatively open as well. Connectedness and \(p\in A\) force \(A=U\). An empty open set has no pairs to connect; dimension zero has at most one point. \(\square\)

For later use, any finite polygonal path can be replaced by a simple polygonal path with the same distinct endpoints and image contained in the original path. Subdivide at all pairwise segment intersections and endpoints of overlapping collinear segments. There are finitely many such points; overlapping segments become common subdivided edges. The path is a walk in the resulting finite geometric graph. If a vertex is visited twice, delete the walk between those visits. Repeating this finite deletion leaves a walk with distinct vertices. Its geometric edges meet only at common endpoints by construction, so its image is simple.

**Lemma 1.2 (the complementary arcs).** Removing a nonempty finite set of \(k\) distinct points from \(S^1\) leaves exactly \(k\) connected components, each an open arc. For \(k=1\) its one arc has angular length \(2\pi\). Every connected subset of this complement lies in one such arc.

**Proof.** Rotate the circle so that one removed point is 1. The map \(t\mapsto e^{it}\), \(0<t<2\pi\), is a homeomorphism onto \(S^1\setminus\{1\}\). Its inverse is the continuously chosen angle on the cut circle: the ordinary local inverse angle functions on semicircles agree after adding the uniquely chosen multiple of \(2\pi\). Order the other removed points' angles. The complement is the disjoint union of the \(k\) open intervals between consecutive ordered angles, including 0 and \(2\pi\) as the cut endpoints. Each interval is connected by interval connectedness, and is both open and closed relative to the complement. No connected subset can meet two of them. Their images are the asserted components and arcs. In particular an open arc of length at most \(\pi\) with initial endpoint \(r\) cannot contain \(-r\), whose forward angular distance from that endpoint is \(\pi\). \(\square\)

The actual polynomial factorization theorem says that a nonzero univariate polynomial of degree \(m\) has at most \(m\) distinct roots. For a nonzero homogeneous polynomial \(H(x,y)\) in two variables, its zeros on \(S^1\) are therefore finite. Indeed, on \(y\ne0\), the equation is \(y^mH(x/y,1)=0\). The polynomial \(H(t,1)\) is nonzero because its coefficients are the homogeneous coefficients of \(H\), so only finitely many slopes occur. Each slope contributes at most two circle points; the two points with \(y=0\) are considered separately. A nonzero constant has no zeros. Homogeneity matters: a general nonhomogeneous polynomial can vanish on the whole circle.

## The index of a closed polygon

Let \(P\) be the image of a simple closed polygonal curve \(\gamma\) in an oriented Euclidean plane, identified with \(\mathbb C\). “Simple” means that its cyclic vertices are distinct, adjacent edges meet only at their shared endpoint, and nonadjacent edges do not meet. Degenerate zero-length edges are deleted. Consecutive straight edges may be merged. A consecutive reversal on the same line would overlap adjacent interiors and is excluded by simplicity.

For \(a\notin P\), define

\[
I(a)=\frac1{2\pi i}\int_\gamma\frac{dz}{z-a}.
\tag{1}
\]

**Lemma 2.1 (integer index and a local jump).** The value \(I(a)\) is an integer and is continuous, hence locally constant, on \(\mathbb C\setminus P\). Across any oriented open edge the value on its left side minus the value on its right side is 1, for sufficiently close points on those sides.

**Proof.** The continuous nonzero path \(\gamma(t)-a\), \(0\le t\le1\), has a continuous argument lift. To construct it, divide the compact parameter interval into finitely many subintervals such that the normalized values on each lie in an open semicircle. This is possible by uniform continuity; for example a sufficiently small chord distance from the value at the subinterval's initial point makes its rotated real part positive. On that semicircle use the real arctangent of imaginary part divided by positive real part, after rotation. At successive endpoints add a multiple of \(2\pi\) to make the values agree. The resulting argument \(\theta(t)\) is continuous, and is C¹ on each subdivided polygonal segment. On each such segment,

\[
\frac{\gamma'(t)}{\gamma(t)-a}
=\frac{d}{dt}\log|\gamma(t)-a|+i\theta'(t).
\tag{2}
\]

Integration telescopes. The logarithms at 0 and 1 agree, whereas the arguments differ by \(2\pi k\) for an integer \(k\), since the complex endpoint values agree. This proves \(I(a)=k\). If \(a\) ranges in a small ball disjoint from \(P\), the integrand is continuous with a common positive denominator bound and finitely many compact segment parameters. Thus its integral is continuous in \(a\). An integer-valued continuous function is locally constant.

For the jump choose an interior point of one edge, translate it to 0, and rotate so that the oriented edge points along the positive real axis. Take a symmetric subsegment \([-c,c]\) around 0. The rest of the polygon is a compact path not containing 0. Its integrals for \(a=i\varepsilon\) and \(a=-i\varepsilon\) have the same limit as \(\varepsilon\downarrow0\). On the chosen subsegment the odd real term in \(1/(t-i\varepsilon)\) integrates to zero, and its index contribution is

\[
\begin{gathered}
\frac1{2\pi i}\int_{-c}^{c}\frac{dt}{t-i\varepsilon}
=\frac1\pi\arctan(c/\varepsilon)
\\
\quad(\varepsilon>0).
\end{gathered}
\tag{3}
\]

For \(a=-i\varepsilon\) the contribution is its negative. Their difference tends to 1. The total index difference is an integer; therefore it equals 1 for all sufficiently small \(\varepsilon>0\). This proves the jump. The same values extend within the two small half-neighborhoods by local constancy. \(\square\)

This proof uses no prior Jordan theorem, no description of an “inside” and no argument principle for arbitrary topological cycles.

## The two regions of a polygon

**Theorem 3.1 (polygonal Jordan separation).** The complement of a finite simple closed polygon in its affine plane has exactly two connected components: one bounded and one unbounded. Both components are open, polygonally connected, and have the entire polygon as their boundary. The closure of the bounded component is compact.

**Proof.** We first show that there can be at most two components by explicitly connecting all local left sides, and likewise all local right sides.

Choose small disjoint disks about the finitely many vertices. Each disk meets only the two edges incident to that vertex, and those edges are radial segments in it; make its radius smaller than half the length of either incident edge. This is possible because each vertex has positive distance from the compact union of the nonincident edges, and distinct vertices have positive separation.

At a vertex let \(u\) be the unit incoming direction and \(v\) the unit outgoing direction. The two radial edges point from the vertex along \(-u\) and \(v\); these rays are distinct by simplicity. They divide the punctured disk into two connected open sectors. The sector reached by turning counterclockwise from \(v\) to \(-u\) contains the local left sides of both oriented edges. To check this explicitly, outgoing points \(rv+tJv\), \(r>0,t>0\) small, have angle just counterclockwise from \(v\); incoming points \(-ru+tJu\) have angle just clockwise from \(-u\), since \(Ju=-J(-u)\). Here \(J\) is the positive right-angle rotation. Both therefore lie in that same sector. The other sector contains the two local right sides. This remains true at a straight vertex; the two sectors are then half-disks.

Along the portion of each edge between the half-radius vertex neighborhoods, take a sufficiently thin open strip on its left and another on its right. Choose their widths small enough that they avoid all other edges and join their corresponding vertex sectors. There are only finitely many edges; the portions outside the vertex disks are compact and disjoint from every other edge, so their separations have a positive minimum. Near the strip ends the sector angle has a positive gap to the other radial edge, so another finite reduction of the width keeps each strip in its intended sector. The strips extend into the full-radius vertex disks and hence overlap the sectors at both ends.

The union \(L\) of all left strips and left vertex sectors is connected: the cyclic succession of strips and sectors has nonempty overlaps. It lies in the complement of the polygon. The corresponding right union \(R\) is connected and also lies in the complement. Every polygon point has nearby points in both unions; central edge points are approached through their strips, and points nearer a vertex are approached through the indicated sectors.

Now let \(q\notin P\). Compactness of \(P\) gives a nearest point \(p\in P\). Every point on the segment from \(q\) to \(p\), except \(p\), is outside \(P\): an earlier intersection would be closer to \(q\) than \(p\). This segment belongs to the same connected component as \(q\). Near \(p\) it meets \(L\) or \(R\). If \(p\) is central on an edge, the segment approaches through one of its two sides, inside its thin strip when sufficiently close; a tangent approach through an interior edge point would lie on the edge and is impossible. If \(p\) lies in a vertex neighborhood, the nearby segment is in one of the two sectors, or in a side-neighborhood of an incident edge there. An approach along one of the actual radial edge segments would again contradict avoidance of \(P\). Thus every component meets \(L\) or \(R\). Since these sets are each connected, the complement has at most two components.

Lemma 2.1 supplies two different index values on close left and right points of any one edge. A continuous integer-valued function is constant on each connected component, so these two points cannot belong to the same component. There are therefore exactly two, containing \(L\) and \(R\), respectively.

Choose a closed disk containing the polygon in its interior. The complement of that disk is connected: join any two of its points radially to a larger circle, and use an arc on that circle to join them. It lies in one of the two polygon-complement components, which is unbounded. The other component has no point outside that disk and is bounded. The components are open, since at each complement point a small ball disjoint from the polygon is connected and hence belongs to its component. Lemma 1.1 makes each component polygonally connected.

Every point of \(P\) is approached from both \(L\) and \(R\), so it is in both component boundaries. No point of the complement is in either boundary: its open component provides either an interior neighborhood or a neighborhood disjoint from the other component. Thus both boundaries are exactly \(P\). The closure of the bounded component is its union with \(P\), and is closed and bounded, hence compact. Orthogonal coordinates on an arbitrary affine plane transfer the entire proof to that plane. \(\square\)

The proof also gives the precise planar region needed by [Planar domains and directional solvability](planar-domains-and-directional-solvability.md), Lemma 1.1. If the polygon is contained in a closed halfplane, its bounded component is contained there: the opposite open halfplane is connected, unbounded and disjoint from the polygon, so belongs to the exterior component. If one edge lies on the boundary line and the remainder of the polygon lies on its upper side, then locally along that edge the lower half-neighborhood is exterior, and the upper half-neighborhood is interior by the two-side proof. The closed bounded region therefore occupies the upper side there. Its height maximum cannot occur in its open interior, because an interior ball would contain a higher point. These facts justify the top-slice and bottom-edge passages in that lesson without a smooth-boundary hypothesis on the ambient domain.

## Exercises with complete solutions

**Exercise 1 (basic: orientation).** Reverse the traversal of a simple polygon. How do the index, local jump and two regions change?

**Solution 1.** Reversing the contour multiplies the integral (1) by \(-1\). It also exchanges the names of its local left and right strips and sectors. The new left-minus-right difference is still 1: it equals \((-I_{\rm right})-(-I_{\rm left})\). The underlying curve and its complement do not change, so the same bounded and unbounded regions remain. The designation “left” alone does not define the bounded region without fixing the polygon's orientation.

**Exercise 2 (intermediate: the angular endpoint).** Let a connected subset of the circle avoid finitely many marked directions and lie in one complementary open arc \(J\) with initial endpoint \(r\). Suppose it contains \(-r\). Show that the closed complementary arc has length less than \(\pi\), except for the one-marked-point case, where it is a single point.

**Solution 2.** For at least two marked points, Lemma 1.2 identifies \(J\) with an open angular interval starting at \(r\). The forward angular distance from \(r\) to \(-r\) is \(\pi\), and containment in the open interval forces its length to exceed \(\pi\). Its closed complement therefore has length \(2\pi-\operatorname{length}(J)<\pi\). For one marked point the open arc has length \(2\pi\), and its closed complement is that point. This is exactly the angular endpoint distinction used in [Planar domains and directional solvability](planar-domains-and-directional-solvability.md), Lemma 2.1.

## References

- Jeff Erickson, *One-Dimensional Computational Topology Notes*, Fall 2020, “Simple Polygons.” [Notes](https://jeffe.cs.illinois.edu/teaching/comptop/2020/notes/01-simple-polygons.html).
- Paul Seidel, *Geometry and Topology in the Plane*, MIT OpenCourseWare, Spring 2023, Chapter I: Polygons. [Open course](https://ocw.mit.edu/courses/18-900-geometry-and-topology-in-the-plane-spring-2023/pages/chapter-i-polygons/).
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II: Differential Operators with Constant Coefficients*, Springer, 1983. Used for the equation-theoretic context.
