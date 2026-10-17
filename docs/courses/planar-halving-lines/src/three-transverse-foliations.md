# Three transverse foliations

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A bijection of the plane that maps lines of three fixed directions onto lines of the same directions is affine, up to the way the three families are matched; affine maps are rigid in this sense, a classical theme revisited in [AS]. This lesson proves the compactness version that the halving-line argument needs [OpenAI-HL, Section 5]: homeomorphisms \(F_j\) that are monotone along three families of parallel lines and whose limits map those lines into lines of the same directions converge, after normalization, to \(\pm\) the identity, together with their inverses. No limit map is assumed to exist in advance, and collapse is ruled out at the scale where the maps are normalized. In [The zoom at a rank point](the-zoom-at-a-rank-point.md) the maps \(F_j\) are rank coordinates seen through a zoom.

The topological input is Brouwer's fixed-point theorem, Theorem 30.1 of the core course [Algebraic Topology](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D60): every continuous map of the closed disk \(D^2\) to itself has a fixed point. It holds for the square \([-1,1]^2\) as well, because \(y\mapsto(\|y\|_\infty/|y|)\,y\), with \(0\mapsto0\), is a homeomorphism of the square onto \(D^2\), with inverse \(x\mapsto(|x|/\|x\|_\infty)\,x\); both factors lie between \(1/\sqrt2\) and \(\sqrt2\), so both maps are continuous at \(0\). It gives the two facts of planar topology used: two paths crossing a rectangle in transverse directions meet, and a map close to \(\pm\) the identity on a disk covers a smaller disk.

## 1. Two consequences of Brouwer's theorem

**Lemma 1.1** (opposite sides). Let \(\alpha,\beta:[0,1]\to[-1,1]^2\) be continuous, with \(\alpha(0)\) on the left side \(\{x=-1\}\), \(\alpha(1)\) on the right side \(\{x=1\}\), \(\beta(0)\) on the bottom \(\{y=-1\}\) and \(\beta(1)\) on the top \(\{y=1\}\). Then \(\alpha(s)=\beta(t)\) for some \(s,t\). The same holds for any parallelogram, with its two pairs of opposite sides.

*Proof.* Suppose not. Then
\[
\begin{aligned}
n(s,t)=\max\bigl({}&|\alpha_1(s)-\beta_1(t)|,\\
&|\alpha_2(s)-\beta_2(t)|\bigr)>0,
\end{aligned}
\]
and
\[
\begin{gathered}
\Phi(u,v)=\frac1{n(s,t)}\begin{pmatrix}\beta_1(t)-\alpha_1(s)\\\alpha_2(s)-\beta_2(t)\end{pmatrix},\\
s=\tfrac{u+1}2,\qquad t=\tfrac{v+1}2,
\end{gathered}
\]
is a continuous map of \([-1,1]^2\) to the boundary of the square. By Brouwer's theorem it has a fixed point \((u,v)\), which lies on the boundary. If \(u=1\), then \(s=1\) and \(\alpha_1(1)=1\), so the first coordinate of \(\Phi(u,v)\) is \((\beta_1(t)-1)/n\le0\ne1\). If \(u=-1\), then \(\alpha_1(0)=-1\) and the first coordinate is \((\beta_1(t)+1)/n\ge0\ne-1\). If \(v=1\), then \(\beta_2(1)=1\) and the second coordinate is \((\alpha_2(s)-1)/n\le0\ne1\); if \(v=-1\), it is \((\alpha_2(s)+1)/n\ge0\ne-1\). Each case contradicts \(\Phi(u,v)=(u,v)\). An affine bijection carries a parallelogram to the square. \(\square\)

**Lemma 1.2** (covering a disk). Let \(\rho>\delta>0\), \(\sigma\in\{-1,1\}\), and let \(F\) be a continuous map of the closed disk \(\bar B(0,\rho)\) into \(\mathbb R^2\) with \(|F(x)-\sigma x|\le\delta\). Then \(F(\bar B(0,\rho))\supseteq\bar B(0,\rho-\delta)\).

*Proof.* For \(|y|\le\rho-\delta\), the map \(G(x)=x-\sigma(F(x)-y)\) satisfies \(|G(x)|\le|x-\sigma F(x)|+|y|\le\delta+\rho-\delta\), so it maps the disk into itself. A fixed point has \(F(x)=y\). \(\square\)

## 2. The compactness theorem

Put \(v_1=(1,0)\), \(v_2=(0,1)\), \(v_3=(1,1)\). A line *of type \(i\)* is a line parallel to \(v_i\).

**Theorem 2.1** (three foliations; OpenAI). Let \(\Omega_j\subseteq\mathbb R^2\) be open sets such that every compact set lies in \(\Omega_j\) for all large \(j\), and let \(F_j:\mathbb R^2\to\Omega_j\) be homeomorphisms. Suppose:

1. there is a fixed invertible matrix \(P\) such that each coordinate of \(PF_j\) is monotone along each line of each type, with a sign depending only on the coordinate and the type;
2. along every subsequence, if \(x_j\) and \(y_j\) lie on one line of type \(i\) and \(F_j(x_j)\to a\), \(F_j(y_j)\to b\), then \(b-a\in\mathbb Rv_i\); the points and their line may depend on \(j\);
3. \(F_j(0)=0\) and \(|F_j(v_1)|=1\).

Then there are a subsequence and \(\sigma\in\{-1,1\}\) such that \(F_j\to\sigma\,\mathrm{id}\) and \(F_j^{-1}\to\sigma\,\mathrm{id}\) uniformly on compact sets.

The monotonicity in the first hypothesis is imposed on \(PF_j\), not on \(F_j\): in the application, \(P\) undoes a linear change of target coordinates, after which the coordinates are rank coordinates.

*Proof.* *Step 1: images of lines.* Fix a type \(i\), and orient lines of type \(i\) by \(v_i\). By the first hypothesis, if \(x'\) follows \(x\) on such a line, \(P(F_j(x')-F_j(x))\) lies in a fixed closed quadrant; so \(F_j(x')-F_j(x)\) lies in the closed cone \(Q_i\), the image of that quadrant under \(P^{-1}\). This cone is pointed, so there is a linear functional \(\ell_i\) positive on \(Q_i\setminus\{0\}\), and a constant \(m_i\) with \(|q|\le m_i\ell_i(q)\) for \(q\in Q_i\).

Let \(x_j\) be points with \(a_j=F_j(x_j)\to a\). On the line of type \(i\) through \(x_j\), the function \(s=\ell_i(F_j(x)-a_j)\) is continuous and strictly increasing, since \(F_j\) is injective and differences lie in \(Q_i\setminus\{0\}\); in this parameter, the image \(\gamma_j(s)\) of the line is \(m_i\)-Lipschitz. The parameter takes all real values as \(x\) runs over the line: for fixed \(R\) the closed disk of radius \(m_iR+1\) about \(a_j\) lies in \(\Omega_j\) for large \(j\), its preimage is compact, so the line leaves it in both directions, at points with \(|F_j(x)-a_j|>m_iR\) and hence \(|s|>R\).

The vectors \(\gamma_j(1)-a_j\) have length at most \(m_i\); a subsequence converges to a vector in \(Q_i\), in \(\mathbb Rv_i\) by the second hypothesis, with \(\ell_i\)-value \(1\). So \(Q_i\cap\mathbb Rv_i\) contains a ray, and since \(Q_i\) is pointed it contains exactly one; let \(d_i\) be its unit vector. Every subsequential limit of \(\gamma_j(s)\) has the form \(a+\theta d_i\) with \(\ell_i(\theta d_i)=s\), so
\[
\gamma_j(s)\longrightarrow a+\frac{s}{\ell_i(d_i)}\,d_i
\]
for every \(s\), along the full sequence; by the uniform Lipschitz bound the convergence is uniform for \(s\) in compact sets. The image of the line converges to the whole line \(a+\mathbb Rd_i\).

*Step 2: intersections.* Let lines of different types \(i\ne k\) pass through points \(x_j\) and \(x'_j\) with \(F_j(x_j)\to a\) and \(F_j(x'_j)\to b\), where \(a=b\) is allowed. The limit lines \(a+\mathbb Rd_i\) and \(b+\mathbb Rd_k\) meet in one point \(c\). Let \(\Pi\) be the parallelogram \(\{c+\alpha d_i+\beta d_k:|\alpha|,|\beta|\le\epsilon\}\). By Step 1, for large \(j\) the image of the first line contains an arc inside \(\Pi\) joining its two sides \(\alpha=\pm\epsilon\): take the part of \(\gamma_j\) between its last point with \(\alpha\le-\epsilon\) and its next point with \(\alpha\ge\epsilon\), which stays within \(\epsilon/2\) of the limit line. Likewise the image of the second line contains an arc inside \(\Pi\) joining the sides \(\beta=\pm\epsilon\). By Lemma 1.1 the arcs meet. The two lines in the domain meet in exactly one point \(x^*_j\), and since \(F_j\) is injective, their images meet exactly at \(F_j(x^*_j)\). So \(F_j(x^*_j)\in\Pi\) for large \(j\), for every \(\epsilon\): \(F_j(x^*_j)\to c\).

*Step 3: lattices.* Pass to a subsequence with \(F_j(v_1)\) convergent. By the second and third hypotheses its limit is \(\sigma v_1\), \(\sigma=\pm1\). The limit lines through limits of images are parallel to the corresponding lines in the domain, so Step 2 says: if \(F_j(x)\to\kappa x\) and \(F_j(x')\to\kappa x'\) for a constant \(\kappa\), then \(F_j(x^*)\to\kappa x^*\) at the intersection \(x^*\) of a line of type \(i\) through \(x\) and a line of type \(k\ne i\) through \(x'\). From a horizontal pair \(u,u+v_1\) such intersections give \(u+v_1+v_2\) (vertical through \(u+v_1\), diagonal through \(u\)), then \(u+v_2\) (vertical through \(u\), horizontal through \(u+v_1+v_2\)); symmetrically \(u-v_2\) and \(u+v_1-v_2\); and \(u+2v_1\) (horizontal through \(u\), diagonal through \(u+v_1-v_2\)) and \(u-v_1\) (horizontal through \(u\), diagonal through \(u+v_2\)). Starting from \(0,v_1\), induction gives \(F_j(z)\to\sigma z\) for every \(z\in\mathbb Z^2\).

Fix \(m\ge2\). On the horizontal line from \(0\) to \(v_1\), each coordinate of \(PF_j\) is monotone, so \(PF_j(v_1/m)\) lies in the rectangle with corners \(0\) and \(PF_j(v_1)\), and is bounded. Every subsequential limit of \(F_j(v_1/m)\) is \(bv_1\) for some \(b\), by the second hypothesis. The same constructions, scaled by \(1/m\) and starting from \(0,v_1/m\), reach \(v_1\) and give \(F_j(v_1)\to mbv_1\) along that subsequence; this holds also if \(b=0\), since the rule of Step 2 needs only lines of different types. So \(mb=\sigma\), and \(F_j(v_1/m)\to\sigma v_1/m\) along the full sequence. As above, \(F_j(z)\to\sigma z\) for all \(z\in(m^{-1}\mathbb Z)^2\), and so for all rational points.

*Step 4: uniform convergence.* Let \(L\) be compact and \(m\ge1\). Each point \(x\) of \(L\) lies in a closed square of the grid \((m^{-1}\mathbb Z)^2\). By the first hypothesis for types \(1\) and \(2\), each coordinate of \(PF_j(x)\) lies between the values of that coordinate at two corners of the square, the corners chosen according to the signs. These corner values converge to those of \(\sigma Px\) at the corners, which differ from \(\sigma Px\) by at most \(\|P\|\sqrt2/m\). Finitely many squares cover \(L\), so \(\limsup_j\sup_L|PF_j-\sigma P|\le2\|P\|\sqrt2/m\) for every \(m\), and \(F_j\to\sigma\,\mathrm{id}\) uniformly on \(L\).

*Step 5: inverses.* Let \(\rho>1\) and \(j\) be large with \(|F_j(x)-\sigma x|\le\delta_j\to0\) on \(\bar B(0,\rho)\). By Lemma 1.2, \(F_j(\bar B(0,\rho))\supseteq\bar B(0,\rho-1)\) once \(\delta_j\le1\); since \(F_j\) is injective on the plane, \(F_j^{-1}\) maps \(\bar B(0,\rho-1)\) into \(\bar B(0,\rho)\). For \(y\) in the smaller disk and \(x=F_j^{-1}(y)\), \(|x-\sigma y|=|\sigma x-F_j(x)|\le\delta_j\). \(\square\)

## 3. Exercises

**3.1** (easy). Show that a linear map of the plane that maps lines of the three types onto lines of the same types is a multiple of the identity.

**3.2** (medium). Show that the maps \(F_j(x)=jx\) and \(F_j(x)=x/j\) satisfy the first two hypotheses and \(F_j(0)=0\). What goes wrong in each case, and which step of the proof uses \(|F_j(v_1)|=1\)?

**3.3** (easy). Where does the proof use that the three types are pairwise transverse, and where that there are three of them rather than two?

## 4. Solutions

**3.1.** The map fixes the three lines \(\mathbb Rv_1\), \(\mathbb Rv_2\), \(\mathbb Rv_3\), so \(v_1\) and \(v_2\) are eigenvectors, with eigenvalues \(\lambda_1,\lambda_2\), and \(v_1+v_2\) is an eigenvector, which forces \(\lambda_1=\lambda_2\).

**3.2.** Both are homeomorphisms of the plane with \(P=I\): each coordinate is monotone along lines of every type. If \(x_j,y_j\) lie on a line of type \(i\), then \(F_j(y_j)-F_j(x_j)\) is a multiple of \(y_j-x_j\), hence lies in the closed line \(\mathbb Rv_i\), and so does any limit. For \(F_j(x)=jx\) the images of all points except \(0\) escape, and there is no limit; for \(F_j(x)=x/j\) everything collapses to \(0\). The normalization \(|F_j(v_1)|=1\) is used in Step 3: it gives a limit \(\sigma v_1\) of length one, which fixes the scale of the lattice constructions and excludes both behaviours.

**3.3.** Transversality makes the limit lines of Step 2 meet in one point. Two families alone allow every map \((x,y)\mapsto(\phi(x),\psi(y))\) with increasing \(\phi,\psi\); the third family, through the constructions of Step 3, ties the scales of the two coordinates together and gives \(F_j(v_1/m)\to\sigma v_1/m\).

## References

- [AS] S. Artstein-Avidan and B. A. Slomka, *The fundamental theorems of affine and projective geometry revisited*, Communications in Contemporary Mathematics 19 (2017); arXiv:1604.01762. https://arxiv.org/abs/1604.01762
- [OpenAI-HL] OpenAI, *A power saving for planar halving lines*, OpenAI Math Release preprint, 25 September 2026, Section 5. https://github.com/openai/math/tree/main/preprints/A-power-saving-for-planar-halving-lines-September-25-2026
