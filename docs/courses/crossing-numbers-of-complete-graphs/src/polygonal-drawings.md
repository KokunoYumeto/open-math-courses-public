# Polygonal drawings

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Edges of a drawing are arbitrary simple arcs, which may wind and wiggle in complicated ways. This lesson shows that a drawing can be replaced by a polygonal one, straight near every vertex and every crossing point, in which edges with a common endpoint do not cross, without increasing the number of crossing points [OpenAI-B, Lemma A.1], [OpenAI-C, Lemma A.1]. Every lower bound of the course is proved for such *normal* drawings, and by Corollary 4.3 this suffices. The tools are compactness, polygonal paths in open sets, and the removal of loops from polygonal walks.

- Normal drawings (Section 1).
- Polygonal paths (Section 2).
- From arcs to polygons (Section 3).
- Removing crossings of adjacent edges (Section 4).

## 1. Normal drawings

A *polygonal arc* is a simple arc that is a finite union of straight segments. A drawing (Definition 1.1 of [Drawings and crossing numbers](drawings-and-crossing-numbers.md)) is *polygonal* if all its edges are polygonal arcs. The vertices and the crossing points of a drawing are its *marks*; there are finitely many.

**Definition 1.1.** A drawing is *normal* if

1. it is polygonal;
2. every mark \(x\) has a closed disc around it, the *disc of \(x\)*, that meets only the edges through \(x\), and meets each of them in a straight segment through \(x\): a segment ending at \(x\) for an edge with endpoint \(x\), and a segment with \(x\) in its interior for an edge crossing at \(x\);
3. no two edges with a common endpoint cross.

So in a normal drawing the edges at a vertex leave it along straight *spokes*, and two edges cross along straight segments through the crossing point. Two straight segments through a point, not on one line, cross properly there (Section 1 of [Drawings and crossing numbers](drawings-and-crossing-numbers.md)). Independent edges, without common endpoint, may cross several times.

The main result of the lesson is the following.

**Theorem 1.2** (normalization; [OpenAI-B, Lemma A.1], [OpenAI-C, Lemma A.1]). For every drawing \(D\) of a graph \(G\) there is a normal drawing \(D'\) of \(G\) with \(c(D')\le c(D)\). In particular \(\operatorname{cr}(G)\) is attained by a normal drawing.

The proof has two parts: Section 3 makes the drawing polygonal and straight near its marks, and Section 4 removes the crossings of adjacent edges one at a time.

## 2. Polygonal paths

A *polygonal walk* is a finite sequence of points \(p_0,p_1,\ldots,p_k\) together with the segments \([p_{i-1},p_i]\), traversed in order; it runs from \(p_0\) to \(p_k\), and its image is the union of the segments.

**Lemma 2.1** (polygonal paths in open sets). Let \(O\subseteq\mathbb R^2\) be open and \(c:[0,1]\to O\) continuous. Then there is a polygonal walk from \(c(0)\) to \(c(1)\) with image in \(O\).

*Proof.* The open discs contained in \(O\) cover \(O\), so their preimages under \(c\) form an open cover of the compact interval \([0,1]\). By the Lebesgue covering lemma [Lebl, Lemma 7.4.10] there is \(\delta>0\) such that every subinterval of length less than \(\delta\) lies in the preimage of one disc. Choose \(0=s_0<s_1<\cdots<s_k=1\) with \(s_i-s_{i-1}<\delta\). Then \(c(s_{i-1})\) and \(c(s_i)\) lie in one open disc contained in \(O\), and so does the segment between them, as discs are convex. \(\square\)

**Lemma 2.2** (removing loops). Let \(W\) be a polygonal walk from \(p\) to \(q\ne p\). Then there is a polygonal arc from \(p\) to \(q\) contained in the image of \(W\). If \(p\) and \(q\) each occur only at the ends of \(W\), the interior of the arc avoids \(p\) and \(q\).

*Proof.* The image of \(W\) is a finite union of segments. Subdivide them at all their endpoints and at all points where two of them meet, and where two of them overlap along a segment, at the ends of the overlap, identifying coinciding pieces. This gives finitely many points, the *nodes*, and finitely many segments, the *links*, any two of which meet at most in a common node; the images of \(p\) and \(q\) are nodes, and the walk \(W\) becomes a sequence of nodes in which consecutive nodes are joined by links. Among all such sequences from \(p\) to \(q\), take one with the fewest links. It has no repeated node, since the part between two occurrences of a node could be removed. Its links therefore form a polygonal arc from \(p\) to \(q\): distinct links of it meet only in a common node, and only consecutive links share a node. The nodes visited are among those of \(W\), and \(p\) and \(q\) occur only at the ends. \(\square\)

## 3. From arcs to polygons

**Proposition 3.1.** For every drawing \(D\) there is a polygonal drawing \(D_1\) of the same graph with \(c(D_1)\le c(D)\) satisfying condition 2 of Definition 1.1.

*Proof.* *Discs around the marks.* Fix for each edge \(e\) an injective continuous parametrization \(\gamma_e:[0,1]\to\mathbb R^2\). A mark \(w\) on \(e\) is \(\gamma_e(t_w)\) for exactly one parameter \(t_w\), with \(t_w\in\{0,1\}\) if \(w\) is an endpoint of \(e\) and \(t_w\in(0,1)\) if \(w\) is a crossing point on \(e\). Choose open parameter intervals \(N_{e,w}\ni t_w\), relatively open in \([0,1]\), with pairwise disjoint closures for the different marks on \(e\). The set \(\gamma_e([0,1]\setminus N_{e,w})\) is the continuous image of a closed bounded set, hence compact [Lebl, Theorem 7.4.14 and Lemma 7.5.5], and it does not contain \(w\), by injectivity; an edge that does not pass through a mark \(w\) is a compact set not containing \(w\). The distance from a point to a compact set not containing it is positive, being the minimum of a positive continuous function [Lebl, Theorem 7.5.6]. Hence there is \(r>0\), smaller than the distance from each mark \(w\) to all these compact sets and smaller than half the distance between any two marks, such that the closed discs \(B_w\) of radius \(r\) around the marks are pairwise disjoint, an edge not passing through \(w\) does not meet \(B_w\), and an edge \(e\) through \(w\) meets \(B_w\) only at parameters in \(N_{e,w}\). Put \(\Omega=\mathbb R^2\setminus\bigcup_wB_w\), an open set.

*Pieces.* Let \(e\) be an edge from \(u\) to \(v\) whose crossing points are \(w_1,\ldots,w_k\) in the order of their parameters. The parameters of \(e\) in \(B_w\) form a closed subset of \(N_{e,w}\); let \(\alpha_w\) and \(\beta_w\) be its least and greatest elements. For an endpoint use \(\beta_u\) (the last visit to \(B_u\)) and \(\alpha_v\) (the first visit to \(B_v\)). The *pieces* of \(e\) are the arcs
\[
\begin{gathered}
\gamma_e\bigl([\beta_u,\alpha_{w_1}]\bigr),\ \gamma_e\bigl([\beta_{w_1},\alpha_{w_2}]\bigr),\\
\ldots,\ \gamma_e\bigl([\beta_{w_k},\alpha_v]\bigr).
\end{gathered}
\]
At \(\beta_w\) the edge lies in \(B_w\) and just after it does not, so \(\gamma_e(\beta_w)\) lies on the boundary circle of \(B_w\); likewise for \(\alpha_w\). Let \([\beta_w,\alpha_{w'}]\) be the parameter interval of a piece, \(w\) and \(w'\) consecutive marks on \(e\). For \(t\) strictly inside it, \(\gamma_e(t)\) is not in \(B_w\), being after the last visit, nor in \(B_{w'}\), being before the first visit, nor in the disc of any other mark \(w''\): the edge meets that disc only at parameters in \(N_{e,w''}\), an interval that contains \(t_{w''}\) and is disjoint from \(N_{e,w}\ni t_w\) and \(N_{e,w'}\ni t_{w'}\), hence lies entirely before \(t_w\) or entirely after \(t_{w'}\). Hence every piece is a simple arc with its endpoints on two boundary circles and its interior in \(\Omega\). Two pieces are disjoint: pieces of one edge have disjoint parameter intervals, since \(\alpha_w<t_w<\beta_w\) for a crossing point \(w\) (the centre of \(B_w\) is not on its boundary), and pieces of different edges could only meet at a common point of two edges outside all discs, but such points are marks.

*Polygonal pieces.* The pieces are finitely many disjoint compact sets, so there are pairwise disjoint open sets \(U_P\supseteq P\), for instance the points at distance less than a third of the least distance between two pieces. Let \(P\) be a piece with endpoints \(x\in\partial B_w\) and \(y\in\partial B_{w'}\). Near \(x\), the set
\[
\begin{aligned}
C_x=\{&w+\rho(\cos\phi,\sin\phi):\\
&r<\rho<r+\epsilon,\ |\phi-\phi_x|<\epsilon\},
\end{aligned}
\]
with \(\phi_x\) the angle of \(x\) seen from \(w\), lies in \(U_P\cap\Omega\) for small \(\epsilon>0\), and it is path-connected. Points of \(P\) close to \(x\) other than \(x\) lie in \(C_x\), being outside \(B_w\); so is the end \(x'=x+\frac\epsilon2\,(x-w)/r\) of the outward radial segment \([x,x']\). Choose such a point \(x''\) of \(P\), and similarly \(y'\) and \(y''\) near \(y\). Following a path in \(C_x\) from \(x'\) to \(x''\), then \(P\) from \(x''\) to \(y''\), then a path in \(C_y\) from \(y''\) to \(y'\), gives a continuous path in the open set \(U_P\cap\Omega\), which Lemma 2.1 replaces by a polygonal walk there. Prefixing the segment \([x,x']\) and appending \([y',y]\) gives a polygonal walk from \(x\) to \(y\) inside \(U_P\) whose points other than \(x\) and \(y\) lie in \(\Omega\). By Lemma 2.2 it contains a polygonal arc \(P'\) from \(x\) to \(y\) with interior in \(U_P\cap\Omega\). Different pieces give disjoint arcs, since the sets \(U_P\) are disjoint. Near \(x\) the arc \(P'\) is the radial segment \([x,x']\): the rest of the walk is a compact subset of \(\Omega\), hence at positive distance from \(x\).

*Filling the discs.* If \(w\) is a crossing point of the edges \(e\) and \(f\), the circle \(\partial B_w\) carries exactly four endpoints of pieces, two of \(e\) and two of \(f\), all distinct. Join the two of \(e\) by a straight chord and the two of \(f\) by a straight chord. A chord between distinct points of a circle lies inside the disc with its interior in the open disc, and the two chords lie on distinct lines, as a line meets a circle in at most two points; so they meet in at most one point, interior to both, where they cross properly. If \(v\) is a vertex, the circle \(\partial B_v\) carries one endpoint of a piece for each edge at \(v\). Choose a new position \(v'\) for the vertex in the open disc, outside the finitely many lines through two of these endpoints, and join \(v'\) to each endpoint by a straight *spoke*. Two spokes meet only in \(v'\), since otherwise \(v'\) would lie on the line through their outer ends.

*The new drawing.* Each edge \(e\) of \(G\), from \(u\) to \(v\), becomes the spoke from \(u'\), the polygonal arcs \(P'\) of its pieces in order, the chords in the discs of its crossing points, and the spoke to \(v'\). This is a polygonal arc: its parts lie in disjoint discs or in disjoint sets \(U_P\), it passes through each disc at most once, and consecutive parts meet only at their common endpoint on a circle. No edge interior contains a vertex, since the vertices lie inside their discs, which contain only spokes. Outside the discs no two edges meet; inside a vertex disc the spokes meet only at the vertex; inside the disc of a former crossing point only the two chords meet, at most once and properly. So \(D_1\) is a polygonal drawing whose crossing points correspond to some of the crossing points of \(D\), and \(c(D_1)\le c(D)\). Each new vertex and each new crossing point lies in the interior of one of the discs \(B_v\) or \(B_w\), which contains only spokes or two chords; a small disc around it inside that disc satisfies condition 2 of Definition 1.1. \(\square\)

## 4. Removing crossings of adjacent edges

**Proposition 4.1** (one exchange). Let \(D\) be a polygonal drawing satisfying condition 2 of Definition 1.1, and let \(e\) and \(f\) be edges with a common endpoint \(v\) that cross at a point \(x\). Then there is a polygonal drawing \(D'\) of the same graph satisfying condition 2 with \(c(D')<c(D)\).

*Proof.* Let \(e\) run from \(v\) to \(u\) and \(f\) from \(v\) to \(w\); as \(G\) is simple, \(u\ne w\). Let \(B\) be a closed disc around \(x\) that meets only the two straight segments of \(e\) and \(f\) through \(x\), contains no other mark and no point where an edge bends. The segment of \(e\) through \(x\) is a diameter of \(B\), entering at \(e_-\) and leaving at \(e_+\) in the direction from \(v\) to \(u\); likewise \(f\) enters at \(f_-\) and leaves at \(f_+\). Since the two diameters cross, the four points alternate around the circle: \(e_-,f_\mp,e_+,f_\pm\) in this cyclic order. Hence \(f_-\) and \(e_+\) are adjacent on the circle, and so are \(e_-\) and \(f_+\), and the chords \([f_-,e_+]\) and \([e_-,f_+]\) are disjoint.

Form two polygonal walks: \(e^*\) follows \(f\) from \(v\) to \(f_-\), the chord \([f_-,e_+]\), and \(e\) from \(e_+\) to \(u\); and \(f^*\) follows \(e\) from \(v\) to \(e_-\), the chord \([e_-,f_+]\), and \(f\) from \(f_+\) to \(w\). Outside \(B\), every point of \(e\) or \(f\) other than \(v\) is used by exactly one of the two walks, once. The walk \(e^*\) passes through \(v\) only at its start, through \(u\) only at its end, and not through \(w\); similarly for \(f^*\). By Lemma 2.2, \(e^*\) contains a polygonal arc \(e'\) from \(v\) to \(u\), and \(f^*\) a polygonal arc \(f'\) from \(v\) to \(w\). Replace \(e,f\) by \(e',f'\).

We check that the result \(D'\) is a drawing with fewer crossings. The interiors of \(e'\) and \(f'\) contain no vertex. The two chords are disjoint and lie in \(B\), where no other edge passes, so the crossing at \(x\) is gone. Every other point of \(e'\cup f'\) lies on \(e\) or \(f\). Let \(y\ne x\) be a point of \(e'\cap g\) for a third edge \(g\), or of \(e'\cap f'\), lying in an edge interior. In the first case \(y\) was a crossing point of \(g\) with \(e\) or \(f\), through which exactly one of the walks passes, once and straight; the arc that keeps it crosses \(g\) there properly. In the second case \(y\) was a crossing of \(e\) and \(f\); if its two straight strands went to different walks and both arcs kept them, \(y\) is a proper crossing of \(e'\) and \(f'\). A self-intersection of \(e^*\) at such a point (both strands in \(e^*\)) is removed or reduced to a single passage by Lemma 2.2; a single passage of one arc through \(y\), possibly turning there, meets no other edge at \(y\). No point is used by three edges, since \(D\) had no such point. Hence \(D'\) is a polygonal drawing; its crossing points form a subset of those of \(D\) without \(x\), so \(c(D')<c(D)\). Near the remaining crossing points the edges are still the old straight strands, and near \(v\) the arcs \(e'\) and \(f'\) begin along the old spokes of \(f\) and \(e\); so condition 2 holds for small discs. \(\square\)

**Proof of Theorem 1.2.** Proposition 3.1 gives a polygonal drawing \(D_1\) with condition 2 and \(c(D_1)\le c(D)\). While two adjacent edges cross, apply Proposition 4.1; each step lowers the number of crossing points, a nonnegative integer, so after finitely many steps no two adjacent edges cross, and the drawing is normal. If \(D\) attains \(\operatorname{cr}(G)\), so does the final drawing, since its crossing number cannot be smaller. \(\square\)

**Corollary 4.2.** In a normal drawing every crossing point lies on two edges with four distinct endpoints.

**Corollary 4.3.** To prove \(\operatorname{cr}(G)\ge N\) it suffices to show \(c(D)\ge N\) for every normal drawing \(D\) of \(G\) attaining \(\operatorname{cr}(G)\).

*Proof.* By Theorem 1.2 some normal drawing \(D\) attains \(\operatorname{cr}(G)\). \(\square\)

**Remark 4.4.** The exchange of Proposition 4.1 changes the cyclic order of the edges at \(v\), and it may change which pairs of independent edges cross. Removing adjacent crossings is a standard step for the crossing number counted by points; for variants that count pairs or parities, adjacent crossings can matter [FPSS].

## 5. Exercises

**5.1.** Show that in a normal drawing two edges can cross at most finitely many times, and give a normal drawing of \(K_4\) in which two independent edges cross three times.

**5.2.** In Proposition 4.1, suppose \(e\) and \(f\) cross only at \(x\). Show that \(e^*\) and \(f^*\) are already arcs, and that \(c(D')=c(D)-1\).

**5.3.** Let \(D\) be a normal drawing and \(v\) a vertex. Show that the cyclic order of the spokes at \(v\) does not depend on the radius of the disc of \(v\) used to read it.

## 6. Solutions

**5.1.** Crossing points are finitely many by Definition 1.1 of [Drawings and crossing numbers](drawings-and-crossing-numbers.md). For \(K_4\) put the vertices \(1,2,3,4\) at \((0,0),(1,0),(1,1),(0,1)\), draw the four sides and the diagonal \(13\) straight, and draw the diagonal \(24\) as the polygonal arc through \((1,0)\), \((0.35,0.55)\), \((0.6,0.45)\), \((0,1)\). Its three segments run inside the open square, so they meet no side; the sign of \(y-x\) at the four points is \(-,+,-,+\), so each segment crosses the diagonal \(y=x\) once; and the first and third segments do not meet (solving for a common point gives a parameter outside \([0,1]\)). The edges \(13\) and \(24\) are independent and cross three times, with signs \(+,-,+\) or \(-,+,-\).

**5.2.** Then \(f\) from \(v\) to \(f_-\) and \(e\) from \(e_+\) to \(u\) do not meet (their common points would be crossings of \(e\) and \(f\) other than \(x\), or the vertex \(v\), which the second part does not contain), and together with the chord they form an arc; similarly for \(f^*\). All crossings other than \(x\) are kept, so exactly one is lost.

**5.3.** Inside the disc of \(v\) the edges at \(v\) are straight spokes; a smaller concentric circle meets each spoke once, on the same ray from \(v\), so the cyclic order of the meeting points is the cyclic order of the directions of the spokes.

## References

- [FPSS] R. Fulek, M. J. Pelsmajer, M. Schaefer, D. Štefankovič, *Adjacent crossings do matter*, J. Graph Algorithms Appl. 16 (2012) 759–782, on the journal's page. https://jgaa.info/index.php/jgaa/article/view/paper266
- [Lebl] J. Lebl, *Basic Analysis I & II*, version 6.3, Lemma 7.4.10 (Lebesgue covering lemma), Theorem 7.4.14 (Heine–Borel), Lemma 7.5.5 and Theorem 7.5.6; the text of the core courses [Real Analysis I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C10) and [Real Analysis II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C20). https://www.jirka.org/ra/html/sec_metcompact.html#ms_lebesgue, https://www.jirka.org/ra/html/sec_metcont.html#lemma_continuouscompact
- [OpenAI-B] OpenAI, *The crossing number of complete bipartite graphs*, OpenAI Math Release preprint, 23 September 2026, Appendix A, Lemma A.1. https://github.com/openai/math/tree/main/preprints/The-crossing-number-of-complete-bipartite-graphs-September-23-2026
- [OpenAI-C] OpenAI, *The crossing number of complete graphs*, OpenAI Math Release preprint, 23 September 2026, Appendix A, Lemma A.1. https://github.com/openai/math/tree/main/preprints/The-crossing-number-of-complete-graphs-September-23-2026
