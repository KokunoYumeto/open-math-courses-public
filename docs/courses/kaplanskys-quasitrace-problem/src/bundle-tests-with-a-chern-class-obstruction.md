# Bundle tests with a Chern class obstruction

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The algebra of the course is built from a sequence of Hermitian vector bundles \(E_0,E_1,\dots\) over a compact manifold and \(24\) maps between successive bundles that satisfy
\[
\sum_iX_i^*X_i=I,\qquad\sum_iX_iX_i^*\le\tfrac23\,I .
\]
This lesson constructs such a sequence for every matrix size \(m\) and every degree bound \(R\), with \(E_0\) trivial of rank \(d_0\), together with an obstruction: the sum of \(m\) copies of \(E_0\oplus\dots\oplus E_R\) contains no trivial subbundle of rank \(2md_0\). In [Weighted shifts and the construction](weighted-shifts-and-the-construction.md) a pair of isometries with orthogonal ranges in \(M_m(B)\) is turned into exactly such a subbundle. The obstruction is a Chern class; the maps come from the two lemmas of [Expanding maps and a continuous normalization](expanding-maps-and-a-continuous-normalization.md).

- Subbundles and orthogonal complements (Lemma 1.1).
- Chern classes, products of projective spaces (Lemma 2.1), and an obstruction for sums of line bundles (Proposition 2.2).
- The ranks and multiplicities (Lemma 3.1) and the bundles (Section 4).
- Maps that double dimensions: sixteen for small subspaces, eight for large ones (Lemma 5.1).
- The bundle tests (Theorem 6.1), and seven maps in place of twenty-four (Remark 6.2).

The lesson follows [OpenAI-QT, Section 4]. Obstructions of this kind, by characteristic classes of vector bundles, were used by Villadsen [V, Section 3], over products of projective spaces, to construct simple C\*-algebras of every stable rank, and by Rørdam [R, Section 3], over products of two-spheres, to construct a simple C\*-algebra with a finite and an infinite projection. The Chern classes are taken from the lessons [Chern classes and the integral universal ring](course:DG-CHAR/DG-CHAR-09) and [The Gysin sequence and projective splitting](course:DG-CHAR/DG-CHAR-08) (course *Characteristic classes*). The maps use Lemmas 4.1 and 6.1 of [Expanding maps and a continuous normalization](expanding-maps-and-a-continuous-normalization.md), and through Lemma 4.1 the hypothesis (SM) on smooth manifolds stated there.

## 1. Subbundles and complements

The conventions are those of Section 1 of [Expanding maps and a continuous normalization](expanding-maps-and-a-continuous-normalization.md): vector bundles are complex, of finite rank, over a compact Hausdorff space, with Hermitian metrics, and a *subbundle* is a family of subspaces of the fibers whose orthogonal projections form a bundle map. A *trivial subbundle of rank \(k\)* is a subbundle that is isomorphic to the trivial bundle \(Y\times\mathbb C^k\).

**Lemma 1.1.** Let \(G\) be a Hermitian vector bundle over a compact Hausdorff space \(Y\), and \(p\) a bundle map of \(G\) such that every \(p(y)\) is an orthogonal projection. Then the images of the \(p(y)\) form a vector bundle \(\operatorname{ran}p\), the images of the \(I-p(y)\) form a vector bundle \(\operatorname{ran}(I-p)\), and \((u,w)\mapsto u+w\) is an isomorphism \(\operatorname{ran}p\oplus\operatorname{ran}(I-p)\to G\).

**Proof.** The rank of \(p(y)\) is its trace, a continuous function with integer values, hence locally constant. Fix \(y_0\), let \(k\) be the rank of \(p(y_0)\), and let \(\sigma_1,\dots,\sigma_n\) be a local frame of \(G\) near \(y_0\). The vectors \(p(y_0)\sigma_l(y_0)\) span the image of \(p(y_0)\); choose \(k\) of them that form a basis. The corresponding sections \(p\sigma_l\) of \(\operatorname{ran}p\) are continuous, and their Gram determinant is continuous and nonzero at \(y_0\). So they are linearly independent near \(y_0\), and where the rank is \(k\) they span the image of \(p(y)\). The coefficients of a vector of \(\operatorname{ran}p\) in this frame are obtained from its inner products with the frame by the inverse Gram matrix, so they are continuous. Hence \(\operatorname{ran}p\) is a vector bundle. The same applies to \(I-p\). The map \((u,w)\mapsto u+w\) is a continuous bundle map, bijective in each fiber because \(G_y\) is the orthogonal sum of the two images, with the continuous inverse \(v\mapsto(pv,(I-p)v)\). \(\blacksquare\)

## 2. Chern classes and products of projective spaces

Cohomology is singular cohomology with integer coefficients and the cup product. The lesson [Chern classes and the integral universal ring](course:DG-CHAR/DG-CHAR-09) (course *Characteristic classes*) constructs, for a complex vector bundle \(V\) of rank \(r\) over a Hausdorff space \(B\), Chern classes \(c_k(V)\in H^{2k}(B;\mathbb Z)\) for \(k\ge0\), with \(c_0(V)=1\) and total class \(c(V)=c_0(V)+c_1(V)+\dots\). We use:

- **(C1)** \(c_k(V)=0\) for \(k>r\), and \(c_1(L)=e(L_{\mathbb R})\) for a line bundle \(L\), the Euler class of the underlying oriented real plane bundle (definition (1.2) there);
- **(C2)** the classes are natural under pullbacks and isomorphisms, and \(c(V\oplus\varepsilon^k)=c(V)\) for the trivial bundle \(\varepsilon^k=B\times\mathbb C^k\) (Proposition 1.1 there); in particular \(c(\varepsilon^k)=1\);
- **(C3)** \(c(V\oplus W)=c(V)\,c(W)\) when \(B\) is paracompact Hausdorff, for instance compact Hausdorff (Theorem 2.2 there).

Let \(\mathbb{CP}^K\) be the space of complex lines in \(\mathbb C^{K+1}\), and \(\gamma_K\subseteq\mathbb{CP}^K\times\mathbb C^{K+1}\) the tautological line bundle, whose fiber at a line \(\ell\) is \(\ell\). The lesson [The Gysin sequence and projective splitting](course:DG-CHAR/DG-CHAR-08) (same course) proves the following, with \(x=-e((\gamma_K)_{\mathbb R})=-c_1(\gamma_K)\).

- \(H^*(\mathbb{CP}^K;\mathbb Z)=\mathbb Z[x]/(x^{K+1})\) (Theorem 3.2 there).
- *Projective-bundle module theorem* (Theorem 4.1 there). Let \(V\) be a complex vector bundle of rank \(n\ge1\) over a Hausdorff space \(B\), \(p\colon P(V)\to B\) its bundle of lines, and \(S\subseteq p^*V\) the tautological line. Every class in \(H^*(P(V);\mathbb Z)\) can be written uniquely as \(\sum_{k=0}^{n-1}p^*(b_k)\,z^k\) with \(b_k\in H^*(B;\mathbb Z)\), where \(z=-e(S_{\mathbb R})\).

**Lemma 2.1.** Let \(K_1,\dots,K_R\ge1\), \(Y=\mathbb{CP}^{K_1}\times\dots\times\mathbb{CP}^{K_R}\) with the projections \(\mathrm{pr}_i\colon Y\to\mathbb{CP}^{K_i}\), \(L_i=\mathrm{pr}_i^*\gamma_{K_i}\), and \(x_i=-c_1(L_i)\). Then the monomials \(x_1^{e_1}\cdots x_R^{e_R}\) with \(0\le e_i\le K_i\) form a basis of the abelian group \(H^*(Y;\mathbb Z)\). In particular \(x_1^{K_1}\cdots x_R^{K_R}\ne0\).

**Proof.** Induction on \(R\), starting with \(R=0\), where \(Y\) is a point and \(H^*(Y;\mathbb Z)=\mathbb Z\) has the basis \(1\). Let \(R\ge1\), let \(B\) be the product of the first \(R-1\) factors, and \(V=B\times\mathbb C^{K_R+1}\). Its bundle of lines is \(B\times\mathbb{CP}^{K_R}=Y\), with \(p\) the projection to \(B\), and its tautological line is \(L_R\). So \(z=-c_1(L_R)=x_R\), and every class on \(Y\) is uniquely \(\sum_{k=0}^{K_R}p^*(b_k)\,x_R^k\). By induction, each \(b_k\) is uniquely an integer combination of the monomials in the classes \(x_1,\dots,x_{R-1}\) formed on \(B\). The line bundles \(L_1,\dots,L_{R-1}\) on \(Y\) are the pullbacks along \(p\) of the corresponding line bundles on \(B\), so by (C2) and because \(p^*\) is a ring homomorphism, \(p^*\) maps these monomials to the monomials in \(x_1,\dots,x_{R-1}\) on \(Y\). Existence and uniqueness of the expansion in the monomials on \(Y\) follow. \(\blacksquare\)

**Proposition 2.2.** Let \(Y\), \(L_i\) and \(x_i\) be as in Lemma 2.1, \(L_0=Y\times\mathbb C\), \(h_0\ge0\), and let \(G\) be a Hermitian vector bundle over \(Y\) isomorphic to
\[
L_0^{\oplus h_0}\oplus L_1^{\oplus K_1}\oplus\dots\oplus L_R^{\oplus K_R} .
\]
Then \(G\) contains no trivial subbundle of rank greater than \(h_0\).

**Proof.** Put \(\kappa=K_1+\dots+K_R\). By (C1), (C2) and (C3),
\[
c(G)=\prod_{i=1}^R(1-x_i)^{K_i} .
\]
Expanding the product gives integer multiples of monomials \(x_1^{e_1}\cdots x_R^{e_R}\) with \(0\le e_i\le K_i\), of degree \(2(e_1+\dots+e_R)\). The degree is \(2\kappa\) only if every \(e_i=K_i\), so
\[
c_\kappa(G)=(-1)^\kappa\,x_1^{K_1}\cdots x_R^{K_R}\ne0
\]
by Lemma 2.1. Suppose that \(T\subseteq G\) is a subbundle isomorphic to \(\varepsilon^k\) with \(k>h_0\). By Lemma 1.1, applied to the orthogonal projection onto \(T\), \(G\) is isomorphic to \(T\oplus T'\), where \(T'\) is the orthogonal complement, of rank \(h_0+\kappa-k<\kappa\). By (C2) and (C3), \(c(G)=c(T)\,c(T')=c(T')\), so \(c_\kappa(G)=c_\kappa(T')=0\) by (C1). This contradicts \(c_\kappa(G)\ne0\). \(\blacksquare\)

The subbundle \(T\) may lie in any position relative to the line summands. The bundle \(G\) has rank \(h_0+\kappa\) and contains the trivial summand \(L_0^{\oplus h_0}\), but no trivial subbundle of larger rank: the top Chern class of \(G\) is the class of the top degree of \(Y\).

## 3. Ranks and multiplicities

Fix integers \(m,R\ge1\). Put
\[
d_0=64m4^R,\qquad d_j=4^jd_0
\]
for \(0\le j\le R\), the multiplicities
\[
\begin{gathered}
a_{0,j}=64m4^{R-j},\\
a_{i,j}=960m4^{R+2i-j-2}
\end{gathered}
\]
for \(0\le j\le R\) and \(1\le i\le j\le R\), and the numbers
\[
\begin{aligned}
K_i&=m\sum_{j=i}^Ra_{i,j}&&(1\le i\le R),\\
h_0&=m\sum_{j=0}^Ra_{0,j},\\
\eta_j&=K_1+\dots+K_{j+1}&&(0\le j<R).
\end{aligned}
\]
In passing from level \(j\) to level \(j+1\), every multiplicity \(a_{i,j}\) with \(i\le j\) is divided by four, \(a_{i,j+1}=a_{i,j}/4\), and a new multiplicity \(a_{j+1,j+1}=960m4^{R+j-1}=\tfrac{15}4d_j\) appears.

**Lemma 3.1.**

1. All \(a_{i,j}\) are positive integers. For \(j<R\) and \(i\le j\), \(a_{i,j}\) is divisible by \(4\) and at least \(256m\).
2. \(a_{0,j}+a_{1,j}+\dots+a_{j,j}=d_j\) for \(0\le j\le R\).
3. \(K_i=320m^24^{2i-2}\bigl(4^{R-i+1}-1\bigr)\), a positive integer.
4. \(h_0=\tfrac43md_0\bigl(1-4^{-(R+1)}\bigr)<2md_0\).
5. \(\eta_j<\tfrac53md_0\bigl(4^{j+1}-1\bigr)<\tfrac{20}3md_j\) for \(0\le j<R\).

**Proof.** *Part 1.* The exponent \(R-j\) is nonnegative, and \(R+2i-j-2\ge R+2-R-2=0\) for \(i\ge1\) and \(j\le R\). For \(j\le R-1\) the exponents are at least \(1\), so \(a_{0,j}\ge256m\) and \(a_{i,j}\ge3840m\); both are divisible by \(4\), since \(64\) and \(960\) are.

*Part 2.* For \(j=0\) the sum is \(a_{0,0}=64m4^R=d_0\). If the sum is \(d_j\) at level \(j<R\), then at level \(j+1\) it is \(\tfrac14d_j+\tfrac{15}4d_j=4d_j=d_{j+1}\).

*Part 3.*
\[
\begin{aligned}
\sum_{j=i}^R4^{R+2i-j-2}&=4^{2i-2}\sum_{j=i}^R4^{R-j}\\
&=4^{2i-2}\bigl(4^{R-i+1}-1\bigr)/3 ;
\end{aligned}
\]
multiply by \(960m^2\).

*Part 4.*
\[
\begin{aligned}
\sum_{j=0}^R64m4^{R-j}&=d_0\sum_{j=0}^R4^{-j}\\
&=\tfrac43d_0\bigl(1-4^{-(R+1)}\bigr) ;
\end{aligned}
\]
multiply by \(m\).

*Part 5.* \(a_{i,j}=a_{i,i}4^{-(j-i)}\), so \(K_i<\tfrac43ma_{i,i}=5md_{i-1}\), and
\[
\begin{aligned}
\eta_j&<5m\bigl(d_0+\dots+d_j\bigr)\\
&=\tfrac53md_0\bigl(4^{j+1}-1\bigr)\\
&<\tfrac53md_04^{j+1}=\tfrac{20}3md_j .
\end{aligned}
\]
\(\blacksquare\)

## 4. The bundles

Let \(Y=\mathbb{CP}^{K_1}\times\dots\times\mathbb{CP}^{K_R}\), \(L_0=Y\times\mathbb C\), and \(L_i=\mathrm{pr}_i^*\gamma_{K_i}\) with the Hermitian metric of \(\mathbb C^{K_i+1}\). For \(0\le j\le R\) let
\[
E_j=\bigoplus_{i=0}^jL_i^{\oplus a_{i,j}} ,
\]
an orthogonal direct sum. By Lemma 3.1, \(E_j\) has rank \(d_j\), and \(E_0=L_0^{\oplus d_0}\) is trivial of rank \(d_0\). The line bundle \(L_i\) occurs in \(E_j\) with multiplicity \(a_{i,j}\) for \(i\le j\), so in
\[
G=\bigl(E_0\oplus\dots\oplus E_R\bigr)^{\oplus m}
\]
it occurs \(K_i\) times for \(i\ge1\) and \(h_0\) times for \(i=0\). By Proposition 2.2 and part 4 of Lemma 3.1, \(G\) contains no trivial subbundle of rank \(2md_0\).

The numbers \(K_i\) are chosen as the total multiplicities of the \(L_i\) in \(G\), so that the top Chern class of \(G\) is the top class of \(Y\). The trivial line \(L_0\) occurs only \(h_0<2md_0\) times in \(G\), because its multiplicity is divided by four at every level, although the \(m\) copies of \(E_0\) alone contain \(md_0\) trivial lines.

*Smooth structure.* The sets \(U_k\) of the lines \(\mathbb Cz\) with \(z_k\ne0\) are open and cover \(\mathbb{CP}^K\), and \(\mathbb Cz\mapsto(z_l/z_k)_{l\ne k}\) identifies \(U_k\) with \(\mathbb C^K\); the changes of charts are smooth. Over \(U_k\), \(\mathbb Cz\mapsto z/z_k\) is a nowhere-zero section of \(\gamma_K\) whose coordinates are the chart coordinates and \(1\). So \(\mathbb{CP}^K\) is a compact smooth manifold of real dimension \(2K\), \(\gamma_K\) is a smooth line subbundle of \(\mathbb{CP}^K\times\mathbb C^{K+1}\), and the metric of \(\mathbb C^{K+1}\) is smooth on it. Products, pullbacks along the smooth projections and orthogonal direct sums preserve smoothness. So \(Y\) is a compact smooth manifold and the \(E_j\) are smooth Hermitian bundles.

*Smaller bases.* For \(0\le j<R\) let \(Y_{j+1}=\mathbb{CP}^{K_1}\times\dots\times\mathbb{CP}^{K_{j+1}}\), of complex dimension \(\eta_j\). The bundles \(E_j\) and \(E_{j+1}\) involve only \(L_0,\dots,L_{j+1}\), so they are the pullbacks along the projection \(Y\to Y_{j+1}\) of the bundles defined by the same formulas on \(Y_{j+1}\); these are denoted by the same letters.

## 5. Maps that double dimensions

**Lemma 5.1.** Let \(0\le j<R\). There are continuous bundle maps \(X_1,\dots,X_{24}\colon E_j\to E_{j+1}\) over \(Y\) with
\[
\begin{gathered}
\sum_{i=1}^{24}X_i^*X_i=I_{E_j},\\
\sum_{i=1}^{24}X_iX_i^*\le\tfrac23\,I_{E_{j+1}} .
\end{gathered}
\]

**Proof.** We work over \(Y_{j+1}\) and write \(d=d_j\). Decompose \(E_{j+1}=F_{\mathrm{old}}\oplus F_{\mathrm{new}}\) with
\[
\begin{gathered}
F_{\mathrm{old}}=\bigoplus_{i=0}^jL_i^{\oplus a_{i,j}/4},\\
F_{\mathrm{new}}=L_{j+1}^{\oplus a_{j+1,j+1}} ,
\end{gathered}
\]
of ranks \(d/4\) and \(\tfrac{15}4d\).

*Sixteen maps for small subspaces.* Fix \(i\le j\) and put \(D=a_{i,j}\), which is divisible by \(4\) and at least \(256m\) by Lemma 3.1. Apply Lemma 4.1 of [Expanding maps and a continuous normalization](expanding-maps-and-a-continuous-normalization.md) over a point, with \(q=16\), source \(\mathbb C^D\), target \(\mathbb C^{D/4}\) and the pairs \((s,2s)\) for \(1\le s\le m\). Here \(2s\le2m<D/4\), and, using \(D\ge64m\) and \(s\le m\),
\[
\begin{aligned}
&(16s-2s)\bigl(\tfrac D4-2s\bigr)-s(D-s)\\
&\quad=\tfrac52sD-27s^2\\
&\quad\ge160ms-27ms=133ms>0 .
\end{aligned}
\]
So there are linear maps \(A^{(i)}_1,\dots,A^{(i)}_{16}\colon\mathbb C^D\to\mathbb C^{D/4}\) such that for every subspace \(S\) with \(1\le\dim S\le m\) the images \(A^{(i)}_kS\) span a space of dimension greater than \(2\dim S\). Since \(L_i^{\oplus D}=L_i\otimes\mathbb C^D\), the maps \(\mathrm{id}\otimes A^{(i)}_k\colon L_i^{\oplus D}\to L_i^{\oplus D/4}\) are smooth bundle maps; in a fiber, a nonzero vector of the line identifies them with the \(A^{(i)}_k\). For \(1\le k\le16\) let \(T_k\colon E_j\to E_{j+1}\) be the block diagonal map with the blocks \(\mathrm{id}\otimes A^{(i)}_k\), \(0\le i\le j\), into \(F_{\mathrm{old}}\), and with zero component in \(F_{\mathrm{new}}\).

*The flag argument.* We show that \(\dim\sum_{k=1}^{16}T_kS\ge2\dim S\) for every subspace \(S\) of a fiber of \(E_j\) with \(\dim S\le m\). Write the fiber of \(E_j\) as \(V_0\oplus\dots\oplus V_j\) and the fiber of \(F_{\mathrm{old}}\) as \(F_0\oplus\dots\oplus F_j\), following the line bundles, and \(T_k=\bigoplus_iT_{k,i}\) with \(T_{k,i}\colon V_i\to F_i\). Put \(V_{\le i}=V_0\oplus\dots\oplus V_i\) and \(F_{\le i}=F_0\oplus\dots\oplus F_i\), both zero for \(i=-1\), and
\[
\begin{gathered}
W=\sum_{k=1}^{16}T_kS,\\
S_i=S\cap V_{\le i},\qquad W_i=W\cap F_{\le i} .
\end{gathered}
\]
Let \(\pi_i\colon V_{\le i}\to V_i\) and \(\pi_i'\colon F_{\le i}\to F_i\) be the projections onto the last summand. The kernel of \(\pi_i\) on \(S_i\) is \(S_{i-1}\), so \(\dim\pi_i(S_i)=\dim S_i-\dim S_{i-1}\); likewise \(\dim\pi_i'(W_i)=\dim W_i-\dim W_{i-1}\). Since \(T_k\) is block diagonal, \(T_kS_i\subseteq W\cap F_{\le i}=W_i\) and \(\pi_i'T_k=T_{k,i}\pi_i\) on \(V_{\le i}\). Hence
\[
\begin{aligned}
\sum_{k=1}^{16}T_{k,i}\bigl(\pi_iS_i\bigr)&=\pi_i'\Bigl(\sum_{k=1}^{16}T_kS_i\Bigr)\\
&\subseteq\pi_i'(W_i) .
\end{aligned}
\]
The subspace \(\pi_i(S_i)\) of \(V_i\) has dimension at most \(\dim S\le m\), so the left side has dimension at least \(2\dim\pi_i(S_i)\). As \(W\subseteq F_{\le j}\), summing over \(i\) gives
\[
\begin{aligned}
\dim W&=\sum_{i=0}^j\bigl(\dim W_i-\dim W_{i-1}\bigr)\\
&\ge2\sum_{i=0}^j\bigl(\dim S_i-\dim S_{i-1}\bigr)\\
&=2\dim S .
\end{aligned}
\]

*Eight maps for large subspaces.* Apply Lemma 4.1 of [Expanding maps and a continuous normalization](expanding-maps-and-a-continuous-normalization.md) over \(Y_{j+1}\), of real dimension \(2\eta_j\), to the bundles \(E_j\) and \(F_{\mathrm{new}}\), of ranks \(d\) and \(\tfrac{15}4d\), with \(q=8\) and the pairs \((s,2s)\) for \(m<s\le d\). Here \(2s\le2d<\tfrac{15}4d\), and, using \(s\le d\), \(s>m\) and part 5 of Lemma 3.1,
\[
\begin{aligned}
&(8s-2s)\bigl(\tfrac{15}4d-2s\bigr)-s(d-s)\\
&\quad=\tfrac{43}2sd-11s^2\\
&\quad\ge\tfrac{21}2sd>\tfrac{20}3md>\eta_j .
\end{aligned}
\]
This gives smooth bundle maps \(T_{17},\dots,T_{24}\colon E_j\to F_{\mathrm{new}}\subseteq E_{j+1}\) such that \(\dim\sum_{k=17}^{24}T_kS>2\dim S\) for every subspace \(S\) of a fiber with \(m<\dim S\le d\).

*Normalization.* Adding maps does not decrease the span of the images. So \(\dim\sum_{k=1}^{24}T_kS\ge2\dim S\) for every subspace \(S\) of every fiber of \(E_j\): the first sixteen maps suffice when \(\dim S\le m\), the last eight when \(\dim S>m\). Lemma 6.1 of [Expanding maps and a continuous normalization](expanding-maps-and-a-continuous-normalization.md), over \(Y_{j+1}\), gives bundle maps \(X_1,\dots,X_{24}\colon E_j\to E_{j+1}\) with the two relations. Their pullbacks to \(Y\) have the same relations. \(\blacksquare\)

The two lists have different tasks. Large subspaces cannot be doubled inside \(F_{\mathrm{old}}\), whose rank \(d/4\) is less than \(2\dim S\) as soon as \(\dim S>d/8\). Small subspaces cannot be treated by the incidence lemma over the large base \(Y_{j+1}\): for a line, \(s=1\), and \(q\) maps into \(F_{\mathrm{new}}\) its expression is \(\bigl(\tfrac{15}4(q-2)-1\bigr)d-(2q-5)\), while for \(j=0\) the base has complex dimension \(\eta_0=K_1=5md_0\bigl(1-4^{-R}\bigr)\), which grows with \(m\). The number of maps has to be the same for all \(m\), because the algebra of [Weighted shifts and the construction](weighted-shifts-and-the-construction.md) has a fixed number of generators. So small subspaces are handled by maps that are constant on each block, for which the dimension count takes place over a point.

## 6. The bundle tests

**Theorem 6.1** (bundle tests; [OpenAI-QT, Section 4]). Let \(m,R\ge1\) and \(d_0=64m4^R\). There are a compact smooth manifold \(Y\), Hermitian vector bundles \(E_j\) over \(Y\) for \(j\ge0\), and continuous bundle maps \(X_i^{(j)}\colon E_j\to E_{j+1}\) for \(1\le i\le24\) and \(j\ge0\), with the following three properties. (1) \(E_0\) is trivial of rank \(d_0\). (2) For every \(j\ge0\),
\[
\begin{gathered}
\sum_{i=1}^{24}X_i^{(j)*}X_i^{(j)}=I_{E_j},\\
\sum_{i=1}^{24}X_i^{(j)}X_i^{(j)*}\le\tfrac23\,I_{E_{j+1}} .
\end{gathered}
\]
(3) \(\bigl(E_0\oplus\dots\oplus E_R\bigr)^{\oplus m}\) contains no trivial subbundle of rank \(2md_0\).

**Proof.** Take \(Y\) and \(E_0,\dots,E_R\) from Section 4; parts 1 and 3 were shown there. For \(j<R\) take the maps of Lemma 5.1. For \(j\ge R\) put \(E_{j+1}=E_j\oplus E_j\), with the two inclusions \(\iota_1,\iota_2\), and
\[
\begin{gathered}
X_1^{(j)}=2^{-1/2}\iota_1,\qquad X_2^{(j)}=2^{-1/2}\iota_2,\\
X_i^{(j)}=0\quad(3\le i\le24) .
\end{gathered}
\]
Then \(\sum_iX_i^{(j)*}X_i^{(j)}=\tfrac12\bigl(\iota_1^*\iota_1+\iota_2^*\iota_2\bigr)=I_{E_j}\) and \(\sum_iX_i^{(j)}X_i^{(j)*}=\tfrac12\bigl(\iota_1\iota_1^*+\iota_2\iota_2^*\bigr)=\tfrac12I_{E_{j+1}}\). The bundles beyond level \(R\) do not enter part 3. \(\blacksquare\)

In [Weighted shifts and the construction](weighted-shifts-and-the-construction.md) the test with parameters \((m,R)\) is used as follows: words of length at most \(R\) in the maps and their adjoints, applied to \(E_0\), stay in \(E_0\oplus\dots\oplus E_R\). So a pair of isometries with orthogonal ranges in \(M_m(B)\), approximated by matrices of polynomials of degree at most \(R\), would produce a trivial subbundle of rank \(2md_0\) in \(\bigl(E_0\oplus\dots\oplus E_R\bigr)^{\oplus m}\).

**Remark 6.2** (seven maps). Theorem 6.1 holds with seven maps in place of twenty-four. First, seven maps suffice in each list of Lemma 5.1. Over a point, with \(D\ge64m\) and \(1\le s\le m\),
\[
\begin{aligned}
&(7s-2s)\bigl(\tfrac D4-2s\bigr)-s(D-s)\\
&\quad=\tfrac14sD-9s^2\\
&\quad\ge16ms-9ms=7ms>0 ,
\end{aligned}
\]
and over \(Y_{j+1}\), with \(m<s\le d\),
\[
\begin{aligned}
&(7s-2s)\bigl(\tfrac{15}4d-2s\bigr)-s(d-s)\\
&\quad=\tfrac{71}4sd-9s^2\\
&\quad\ge\tfrac{35}4sd>\tfrac{20}3md>\eta_j .
\end{aligned}
\]
Second, the two lists can be merged. Let \(A_1,\dots,A_7\colon E_j\to F_{\mathrm{old}}\) be block diagonal maps as in the first list and \(B_1,\dots,B_7\colon E_j\to F_{\mathrm{new}}\) maps as in the second, and put \(T_k=A_k+B_k\colon E_j\to F_{\mathrm{old}}\oplus F_{\mathrm{new}}\). For a subspace \(S\) of a fiber, the projection of \(\sum_kT_kS\) to \(F_{\mathrm{old}}\) is \(\sum_kA_kS\), and its projection to \(F_{\mathrm{new}}\) is \(\sum_kB_kS\). A subspace is at least as large as each of its projections. So \(\dim\sum_kT_kS\ge2\dim S\) for every \(S\), by the flag argument when \(\dim S\le m\) and by the second list when \(\dim S>m\), and Lemma 6.1 of [Expanding maps and a continuous normalization](expanding-maps-and-a-continuous-normalization.md) applies to \(T_1,\dots,T_7\). The continuation beyond level \(R\) uses two maps. The consequence for the additivity defect is drawn at the end of [Weighted shifts and the construction](weighted-shifts-and-the-construction.md).

Six maps would not be enough for this dimension count: for \(q=6\) the expression over a point is \(4s\bigl(\tfrac D4-2s\bigr)-s(D-s)=-7s^2<0\) (Exercise 7.4).

## 7. Exercises

**7.1.** For \(m=R=1\), compute \(d_0\), \(d_1\), the multiplicities, \(K_1\), \(h_0\) and \(\eta_0\), and describe \(Y\), \(E_0\), \(E_1\) and \(G\).

**7.2.** Let \(\gamma_K^\perp\subseteq\mathbb{CP}^K\times\mathbb C^{K+1}\), \(K\ge1\), be the orthogonal complement of the tautological line bundle. Show that \(c(\gamma_K^\perp)=1+x+\dots+x^K\), and conclude that \(\gamma_K^\perp\) has no nowhere-zero continuous section.

**7.3.** Over a point, let \(V=V_1\oplus V_2\) and \(F=F_1\oplus F_2\), and let \(A_k=A_k^{(1)}\oplus A_k^{(2)}\), \(1\le k\le q\), be block diagonal maps \(V\to F\) such that for \(b=1,2\) the maps \(A_k^{(b)}\) send every nonzero vector of \(V_b\) to vectors spanning a space of dimension at least \(2\). Show directly that the maps \(A_k\) send every nonzero vector of \(V\) to vectors spanning a space of dimension at least \(2\).

**7.4.** Verify the identities
\[
\begin{aligned}
&(16s-2s)\bigl(\tfrac D4-2s\bigr)-s(D-s)\\
&\qquad=\tfrac52sD-27s^2,\\
&(8s-2s)\bigl(\tfrac{15}4d-2s\bigr)-s(d-s)\\
&\qquad=\tfrac{43}2sd-11s^2,
\end{aligned}
\]
and show that the first expression with \(16\) replaced by \(6\) is negative for every \(s\ge1\).

**7.5.** Suppose that the multiplicity of \(L_0\) were not divided by four, that is, \(a_{0,j}=d_0\) for all \(j\). Show that then \(G\) would contain a trivial subbundle of rank \(2md_0\).

## 8. Solutions

**7.1.** \(d_0=256\), \(d_1=1024\); \(a_{0,0}=256\), \(a_{0,1}=64\), \(a_{1,1}=960\); \(K_1=960\), \(h_0=320\) and \(\eta_0=960\), which is less than \(\tfrac{20}3\cdot256\). So \(Y=\mathbb{CP}^{960}\), \(E_0=L_0^{\oplus256}\), \(E_1=L_0^{\oplus64}\oplus L_1^{\oplus960}\), and \(G=E_0\oplus E_1\cong L_0^{\oplus320}\oplus L_1^{\oplus960}\), of rank \(1280\). By Proposition 2.2 it contains no trivial subbundle of rank greater than \(320\), in particular none of rank \(2md_0=512\).

**7.2.** By Lemma 1.1, \(\gamma_K\oplus\gamma_K^\perp\) is isomorphic to the trivial bundle of rank \(K+1\). By (C1), (C2) and (C3), \((1-x)\,c(\gamma_K^\perp)=1\), and in \(\mathbb Z[x]/(x^{K+1})\) the inverse of \(1-x\) is \(1+x+\dots+x^K\). So \(c_K(\gamma_K^\perp)=x^K\ne0\). A nowhere-zero section \(\sigma\) spans a trivial line subbundle: its projections \(\sigma\sigma^*/\|\sigma\|^2\) are continuous, and \((y,\lambda)\mapsto\lambda\sigma(y)\) is an isomorphism from the trivial line bundle. Its orthogonal complement in \(\gamma_K^\perp\) has rank \(K-1\), and as in the proof of Proposition 2.2 this would force \(c_K(\gamma_K^\perp)=0\).

**7.3.** Let \(v=v_1+v_2\ne0\) and \(W\) the span of the \(A_kv\). If \(v_2\ne0\), the projection of \(W\) to \(F_2\) is the span of the \(A_k^{(2)}v_2\), of dimension at least \(2\), and \(W\) is at least as large as its projection. If \(v_2=0\), \(W\) is the span of the \(A_k^{(1)}v_1\). This is the flag argument of Lemma 5.1 for lines.

**7.4.** Expanding the products,
\[
\begin{aligned}
&14s\cdot\tfrac D4-28s^2-sD+s^2\\
&\qquad=\tfrac52sD-27s^2,\\
&6s\cdot\tfrac{15}4d-12s^2-sd+s^2\\
&\qquad=\tfrac{43}2sd-11s^2 .
\end{aligned}
\]
With \(6\) in place of \(16\): \(4s\cdot\tfrac D4-8s^2-sD+s^2=-7s^2\).

**7.5.** Then \(L_0\) occurs \(m(R+1)d_0\ge2md_0\) times in \(G\), and \(L_0^{\oplus2md_0}\) is itself a trivial subbundle of rank \(2md_0\).

## References

- [OpenAI-QT] OpenAI, *A counterexample to Kaplansky's quasitrace conjecture*, OpenAI Math Release preprint, 23 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/A-counterexample-to-Kaplanskys-quasitrace-conjecture-September-23-2026
- [R] M. Rørdam, *A simple C\*-algebra with a finite and an infinite projection*, Acta Math. 191 (2003), 109–142. https://arxiv.org/abs/math/0204339
- [V] J. Villadsen, *On the stable rank of simple C\*-algebras*, J. Amer. Math. Soc. 12 (1999), 1091–1102. https://doi.org/10.1090/S0894-0347-99-00314-8
