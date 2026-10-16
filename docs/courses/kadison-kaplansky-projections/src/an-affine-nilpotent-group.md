# An affine nilpotent group

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The voltages of the cover lie in a torsion-free nilpotent group \(F\) built from an affine group \(E\): the semidirect product of the affine functions on the strictly upper triangular matrices by the unitriangular group acting through \(x\mapsto b(1+x)-1\). The constants form the center of \(E\), and the quotient \(\bar E\) carries a real-valued cocycle. Fourier transformation in the central coordinate decomposes the regular representation of \(F\) into a field of *twisted* representations of \(\bar E_{\mathbb Z}\times\bar E_{\mathbb Z}\), indexed by a point \(t\) of the circle. The later lessons build projections of small trace in these fibers. This lesson sets up the group, its grading and Haar measure, the deck group, and the fiber decomposition [OpenAI-KK, Sections 8.2 and 8.3].

- The affine group and its cocycle (Section 1).
- Grading, Haar measure and integer points (Section 2).
- The deck group (Section 3).
- Fields over the circle (Section 4).
- Twisted representations in the fibers (Section 5).

We write \(\mathbf e(v)=e^{2\pi iv}\). All discrete Hilbert spaces carry counting measure, and traces over auxiliary matrix indices are ordinary sums, not normalized.

## 1. The affine group and its cocycle

Let \(\mathfrak n\) be the space of strictly upper triangular real \(m\times m\) matrices, of dimension \(n_{\mathrm f}=m(m-1)/2\), and \(U=1+\mathfrak n\) the unitriangular group, with \(m\) fixed in the previous lesson. For \(b\in U\) put
\[
\begin{gathered}
A_b(x)=b(1+x)-1,\quad L_b(x)=bx\\
(x\in\mathfrak n) .
\end{gathered}
\]
Then \(A_bA_{b'}=A_{bb'}\), an affine action of \(U\) on \(\mathfrak n\). An affine function on \(\mathfrak n\) is \(x\mapsto z+\lambda(x)\) with \(z\in\mathbb R\) and \(\lambda\in\mathfrak n^*\). Let \(E\) be the semidirect product of the additive group of affine functions by \(U\), acting by \(f\mapsto f\circ A_{b^{-1}}\). In the coordinates \((\lambda,b,z)\),
\[
\begin{aligned}
&(\lambda,b,z)(\mu,b',w)\\
&\quad=\bigl(\lambda+\mu\circ L_{b^{-1}},\,bb',\\
&\qquad z+w+\mu(b^{-1}-1)\bigr),\\
&(\lambda,b,z)^{-1}\\
&\quad=\bigl(-\lambda\circ L_b,\,b^{-1},\\
&\qquad-z-\lambda(b-1)\bigr),
\end{aligned}\tag{1.1}
\]
because \((w+\mu)(A_{b^{-1}}x)\) is \(w+\mu(b^{-1}-1)+\mu(b^{-1}x)\). The constants \((0,1,z)\) are central. The quotient \(\bar E\) by the constants has coordinates \(\gamma=(\lambda,b)\) and a section \(\sigma(\gamma)=(\lambda,b,0)\). For \(\eta=(\mu,b')\) put
\[
\begin{gathered}
\gamma\eta=(\lambda+\mu\circ L_{b^{-1}},bb'),\\
c(\gamma,\eta)=\mu(b^{-1}-1) .
\end{gathered}
\]
Then \(\sigma(\gamma)\sigma(\eta)=(0,1,c(\gamma,\eta))\,\sigma(\gamma\eta)\), and associativity gives the cocycle identity
\[
\begin{gathered}
c(\gamma,\eta)+c(\gamma\eta,\zeta)\\
=c(\eta,\zeta)+c(\gamma,\eta\zeta) .
\end{gathered}\tag{1.2}
\]
The cocycle vanishes when either argument is the identity, and \(c(\gamma,\gamma^{-1})=c(\gamma^{-1},\gamma)=\lambda(b-1)\).

## 2. Grading, Haar measure and integer points

**Lemma 2.1** (grading, Haar measure, integer points; [OpenAI-KK, Lemma 8.3]). The group laws (1.1) are polynomials with integer coefficients in the coordinates \((\lambda,b-1,z)\). Give the coordinates the weights
\[
\begin{gathered}
\operatorname{wt}(b-1)_{ij}=j-i,\\
\operatorname{wt}\lambda_{ij}=m-(j-i),\qquad\operatorname{wt}z=m .
\end{gathered}
\]

1. For \(y>0\), multiplying each coordinate of weight \(a\) by \(y^a\) is an automorphism \(\Delta_y\) of \(E\) and of \(\bar E\), and \(c(\Delta_y\gamma,\Delta_y\eta)=y^mc(\gamma,\eta)\).
2. Lebesgue measure in these coordinates is a left and right Haar measure on \(E\) and on \(\bar E\), preserved by inversion; the Jacobian of \(\Delta_y\) on \(\bar E\) is \(y^{mn_{\mathrm f}}\).
3. The points with integer coordinates form subgroups \(E_{\mathbb Z}\) and \(\bar E_{\mathbb Z}\), which are countable, nilpotent and torsion-free.

*Proof.* The inverse \(b^{-1}=\sum_{h=0}^{m-1}(1-b)^h\) is an integer polynomial in \(b-1\), which gives the first statement.

(1) Let \(\delta_y(b)=T^{-1}bT\) with \(T=\operatorname{diag}(y,y^2,\ldots,y^m)\), so that \(\delta_y\) multiplies the entry \((i,j)\) by \(y^{j-i}\); it is an automorphism of \(U\), and \(\delta_y(A_b(x))=A_{\delta_yb}(\delta_yx)\). On affine functions put \(f\mapsto y^mf\circ\delta_{y^{-1}}\): it multiplies \(z\) by \(y^m\) and \(\lambda_{ij}\) by \(y^{m-(j-i)}\). These two maps intertwine the action, so together they are the automorphism \(\Delta_y\) of \(E\); it preserves the center and acts on the central coordinate by \(y^m\), which gives the homogeneity of \(c\).

(2) Order the entries of \(b-1\) by their distance from the diagonal. Left and right multiplications on \(U\) are then triangular coordinate changes with ones on the diagonal, of determinant one, and so is \(L_b\) on \(\mathfrak n\), which acts on each column by a unitriangular block of \(b\). For a fixed left factor in (1.1), the coordinates \(\mu\) change by the transpose of \(L_{b^{-1}}\), \(b'\) by a left multiplication and \(w\) by a translation; for a fixed right factor, \(\lambda\) and \(z\) are translated by functions of \(b\), and \(b\) is multiplied on the right. In both cases the Jacobian is one, also after omitting \(z\). Inversion exchanges two Haar measures normalized in the same way, so it preserves Lebesgue measure. The pairs \((\lambda_{ij},(b-1)_{ij})\) have total weight \(m\), and there are \(n_{\mathrm f}\) of them.

(3) Integer coefficients make the integer points a subgroup. By (1), every monomial of the product in a coordinate of weight \(a\), other than the sum of the two coordinates themselves, is homogeneous of weight \(a\) and involves coordinates of both factors, so each of its coordinates has weight less than \(a\). Hence the elements whose coordinates of weight less than \(a\) vanish form normal subgroups \(E_{\ge a}\), with \([E,E_{\ge a}]\subseteq E_{\ge a+1}\), and \(E\) is nilpotent because all weights are at most \(m\). If an element has first nonzero weight \(a\), its \(k\)-th power, \(k\ge1\), has weight-\(a\) coordinates \(k\) times its own, so it is not the identity. The same holds for \(\bar E\) and the integer points. \(\square\)

## 3. The deck group

Let
\[
\begin{aligned}
F&=(E_{\mathbb Z}\times E_{\mathbb Z})\\
&\quad\big/\bigl\{((0,1,k),(0,1,-k)):k\in\mathbb Z\bigr\} .
\end{aligned}
\]
Summing the two central integers identifies \(F\) with the set of triples \((\gamma_X,\gamma_Y,z)\in\bar E_{\mathbb Z}\times\bar E_{\mathbb Z}\times\mathbb Z\) with the law
\[
\begin{aligned}
&(\gamma_X,\gamma_Y,z)(\eta_X,\eta_Y,w)\\
&\quad=\bigl(\gamma_X\eta_X,\gamma_Y\eta_Y,\\
&\qquad z+w+c(\gamma_X,\eta_X)+c(\gamma_Y,\eta_Y)\bigr) .
\end{aligned}
\]
The two factors are called \(X\) and \(Y\); they are names, unrelated to the graphs. The grading of Lemma 2.1, with weight \(m\) for \(z\), shows as there that \(F\) is countable, nilpotent and torsion-free. The projection to the unitriangular coordinate \(b\) of either factor is a surjective homomorphism onto \(U_{\mathbb Z}\). Write \(z_0\) for the central element \((1,1,1)\), with the identity of \(\bar E_{\mathbb Z}\) in the first two places, and \(\sigma_X,\sigma_Y\) for the two sections \(\bar E_{\mathbb Z}\to F\).

## 4. Fields over the circle

Let \(\mathbb T=\mathbb R/\mathbb Z\) with Lebesgue probability measure and \(\mathcal K\) a separable Hilbert space. A *bounded measurable field* is a map \(t\mapsto B(t)\) into the bounded operators on \(\mathcal K\), with \(t\mapsto\langle B(t)\xi,\zeta\rangle\) measurable for all \(\xi,\zeta\) and \(\sup_t\|B(t)\|<\infty\). It acts on \(L^2(\mathbb T;\mathcal K)\) by \((B\Xi)(t)=B(t)\Xi(t)\).

**Lemma 4.1** (fields). The operator norm of \(B\) is the essential supremum of \(\|B(t)\|\). Products and adjoints are computed pointwise. If every \(B(t)\) is self-adjoint and \(\phi\) is continuous on an interval containing all their spectra, then \(\phi(B)\) is the field \(t\mapsto\phi(B(t))\).

*Proof.* \(\|B\Xi\|^2=\int\|B(t)\Xi(t)\|^2dt\) gives \(\|B\|\le\operatorname{ess\,sup}\|B(t)\|\). Conversely, if \(\|B(t)\|>c\) on a set of positive measure, then for a countable dense set of unit vectors \(\xi_k\), some \(\{t:\|B(t)\xi_k\|>c\}\) has positive measure \(\nu\); the field equal to \(\xi_k\) on that set, with norm \(\nu^{1/2}\), is mapped to a field of norm greater than \(c\nu^{1/2}\). Products and adjoints are pointwise by definition. For a polynomial \(\phi\) the last statement is clear; a continuous \(\phi\) is a uniform limit of polynomials on the interval, and by the norm formula the corresponding fields converge in norm. \(\square\)

## 5. Twisted representations in the fibers

Let \(\rho\) be the right regular representation, \((\rho(g)\xi)(f)=\xi(fg)\), on \(\ell^2(F)\). The unitary \((\mathcal I\xi)(f)=\xi(f^{-1})\) satisfies \(\mathcal I\rho(g)\mathcal I=\lambda(g)\), the left regular representation, and fixes \(\delta_1\). Write elements of \(F\) as \(\sigma_X(\eta_X)\sigma_Y(\eta_Y)z_0^j\), that is, as \((\eta_X,\eta_Y,j)\), and Fourier transform the central coordinate, \(\delta_j\mapsto(t\mapsto\mathbf e(tj))\):
\[
\begin{aligned}
&\ell^2(F)\\
&\cong L^2\bigl(\mathbb T;\\
&\qquad\ell^2(\bar E_{\mathbb Z})\otimes\ell^2(\bar E_{\mathbb Z})\bigr) .
\end{aligned}\tag{5.1}
\]

**Lemma 5.1** (the fiber representations). Under (5.1), \(\lambda(z_0)\) acts by \(\mathbf e(t)\), and \(\lambda(\sigma_X(\gamma))\), \(\lambda(\sigma_Y(\gamma))\) act in the fiber at \(t\) by \(u_t(\gamma)\otimes1\) and \(1\otimes u_t(\gamma)\), where
\[
u_t(\gamma)\delta_\eta=\mathbf e\bigl(t\,c(\gamma,\eta)\bigr)\delta_{\gamma\eta} .
\]
These unitaries satisfy \(u_t(\gamma)u_t(\eta)=\mathbf e(t\,c(\gamma,\eta))u_t(\gamma\eta)\) and \(u_t(\gamma)^*=\mathbf e(-t\,c(\gamma^{-1},\gamma))u_t(\gamma^{-1})\). The operators
\[
v_t(k)\delta_\eta=\mathbf e\bigl(t\,c(\eta,k)\bigr)\delta_{\eta k}
\]
commute with all \(u_t(\gamma)\), and in each factor they are the fiber images of the right translations by the section elements.

*Proof.* In \(F\), \(\sigma_X(\gamma)\cdot(\eta_X,\eta_Y,j)\) is \((\gamma\eta_X,\eta_Y,j+c(\gamma,\eta_X))\), so \(\lambda(\sigma_X(\gamma))\delta_{(\eta_X,\eta_Y,j)}=\delta_{(\gamma\eta_X,\eta_Y,j+c(\gamma,\eta_X))}\), whose transform is \(\mathbf e(tc(\gamma,\eta_X))\mathbf e(tj)\,\delta_{\gamma\eta_X}\otimes\delta_{\eta_Y}\). The second factor is the same. The multiplier formula follows from (1.2), and the adjoint formula from it and \(c(\gamma,1)=0\). The cocycle identity (1.2) with the arguments \(\gamma,\eta,k\) gives \(u_t(\gamma)v_t(k)=v_t(k)u_t(\gamma)\). Right multiplication of \((\eta_X,\eta_Y,j)\) by \(\sigma_X(k)\) gives \((\eta_Xk,\eta_Y,j+c(\eta_X,k))\), whose transform is \(v_t(k)\) in the first factor. \(\square\)

The right operators \(v_t(k)\otimes v_t(k')\), \(k,k'\in\bar E_{\mathbb Z}\), form a right phase action of \(\bar E_{\mathbb Z}\times\bar E_{\mathbb Z}\) in the sense of [Separated bands and equivariant traces](separated-bands-and-equivariant-traces.md), Section 2. An operator of the form \(u_t(\gamma)\otimes u_t(\gamma')\), and every norm limit of linear combinations of such operators tensored with matrices, is equivariant, and Lemma 2.1 of that lesson applies to its identity trace in each fiber.

**Lemma 5.2** (traces of fields). Let \(B\ge0\) be an operator on \(\ell^2(F)\otimes\mathbb C^N\) that commutes with the right translations and is decomposed by (5.1) into a bounded measurable field \(B(t)\) of equivariant operators. Then
\[
\operatorname{Tr}(B)=\int_{\mathbb T}\operatorname{Tr}\bigl(B(t)\bigr)\,dt ,
\]
where on the left the identity trace is taken at the identity of \(F\), and on the right at the identity of \(\bar E_{\mathbb Z}\times\bar E_{\mathbb Z}\), both summed over the \(N\) matrix indices.

*Proof.* The vector \(\delta_1\otimes e_j\) corresponds to the constant field \(t\mapsto\delta_{(1,1)}\otimes e_j\), and
\[
\begin{aligned}
&\langle B(\delta_1\otimes e_j),\delta_1\otimes e_j\rangle\\
&\quad=\int\langle B(t)(\delta_{(1,1)}\otimes e_j),\delta_{(1,1)}\otimes e_j\rangle\,dt .
\end{aligned}
\]
Sum over \(j\). \(\square\)

## 6. Exercises

**6.1** (easy). For \(m=2\), \(\mathfrak n\) is one-dimensional. Write the group law of \(E\) in coordinates \((\lambda,b,z)\in\mathbb R^3\), and identify \(E\) with the Heisenberg group.

**6.2** (easy). Check that \(c(\gamma,\eta)=\mu(b^{-1}-1)\) satisfies the cocycle identity (1.2) for \(m=2\).

**6.3** (medium). For \(m=2\), compute \(u_t(\gamma)\) on \(\ell^2(\bar E_{\mathbb Z})=\ell^2(\mathbb Z^2)\) and show that the operators \(u_t(1,0)\) and \(u_t(0,b)\) commute up to the factor \(\mathbf e(\pm t)\): they generate a rotation algebra.

**6.4** (medium). Show that in \(F\) the element \(\sigma_X(\gamma)\) has infinite order for every \(\gamma\ne1\), directly from the grading.

## 7. Solutions

**6.1.** With \(b=1+\beta\), \(b^{-1}=1-\beta\), \(L_{b^{-1}}\) is the identity on the one-dimensional \(\mathfrak n\) (since \((1-\beta)x=x\) for \(x\) strictly upper triangular of size two), and the product \((\lambda,\beta,z)(\mu,\beta',w)\) is \((\lambda+\mu,\beta+\beta',z+w-\mu\beta)\), a Heisenberg group law.

**6.2.** For \(m=2\), \(c((\lambda,\beta),(\mu,\beta'))=-\mu\beta\). Both sides of (1.2) with a third element \((\nu,\beta'')\) equal \(-\mu\beta-\nu(\beta+\beta')\).

**6.3.** \(u_t(\gamma)\delta_{(\mu,\beta')}=\mathbf e(-t\mu\beta)\delta_{\gamma(\mu,\beta')}\). For \(U_1=u_t(1,0)\) and \(U_2=u_t(0,1)\): 
\[
\begin{aligned}
U_1U_2&=\mathbf e(t\,c((1,0),(0,1)))u_t(1,1)\\
&=u_t(1,1),\\
U_2U_1&=\mathbf e(t\,c((0,1),(1,0)))u_t(1,1)\\
&=\mathbf e(-t)u_t(1,1),
\end{aligned}
\]
so \(U_2U_1=\mathbf e(-t)U_1U_2\).

**6.4.** If the first nonzero coordinate of \(\gamma\) has weight \(a\), then \(\sigma_X(\gamma)^k\) has weight-\(a\) coordinates \(k\) times those of \(\gamma\), by the proof of Lemma 2.1(3), so \(\sigma_X(\gamma)^k\ne1\) for \(k\ge1\).

## References

- [OpenAI-KK] OpenAI, *A torsion-free counterexample to the Kadison–Kaplansky projection conjecture*, OpenAI Math Release preprint, 23 September 2026, Sections 8.2 and 8.3, Lemmas 8.3 and 8.4. https://github.com/openai/math/tree/main/preprints/A-Torsion-Free-Counterexample-to-the-Kadison-Kaplansky-Projection-Conjecture-September-23-2026
