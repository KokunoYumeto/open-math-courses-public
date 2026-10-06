# Counting ideals of bounded norm

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Independent full-lesson AI review is pending. Public domain (CC0).*

The geometry of numbers does more than prove that the class group is finite. Once units identify the repeated generators of a principal ideal, lattice counting gives a common density for every ideal class. The density contains the regulator because a fundamental domain for the logarithms of units controls the size of the region being counted.

Let \(K\) have degree \(n=r_1+2r_2\), absolute discriminant \(|d_K|\), class number \(h_K\), and \(w_K=|\mu_K|\) roots of unity. Put
\[
V=K\otimes_{\mathbf Q}\mathbf R
=\mathbf R^{r_1}\times\mathbf C^{r_2},\qquad
m=r_1+r_2,\quad q=m-1.
\tag{1}
\]
We use ordinary coordinate Lebesgue measure on \(V\), with each complex coordinate contributing its real and imaginary parts. For a nonzero integral ideal \(\mathfrak c\), [*Lattices, Minkowski's theorem and the Minkowski embedding*](lattices-minkowskis-theorem-and-the-minkowski-embedding.md) gives
\[
\operatorname{covol}(\mathfrak c)
=2^{-r_2}\sqrt{|d_K|}\,N(\mathfrak c).
\tag{2}
\]
The finite class group comes from [*Finiteness of the class number*](finiteness-of-the-class-number.md). The units, their weighted logarithms and the regulator convention come from [*Dirichlet's unit theorem*](dirichlets-unit-theorem.md): a complex-place logarithm has weight two, and the regulator is a deleted-row determinant. For unit rank zero, \(R_K=1\).

## A lattice count with a boundary error

Call a bounded subset \(D\subseteq\mathbf R^n\) **Lipschitz bounded** if its topological boundary is covered by finitely many images of Lipschitz maps
\[
\phi_j:[0,1]^{n-1}\longrightarrow\mathbf R^n.
\]
For \(n=1\), the parameter cube is a singleton, so this means that the boundary is finite. Such a boundary has \(n\)-dimensional measure zero: subdividing each parameter cube into \(M^{n-1}\) small cubes covers its image by boxes of diameter \(O(1/M)\) and total \(n\)-volume \(O(1/M)\). In particular \(D\) is Lebesgue measurable, regardless of which boundary points it includes.

**Lemma 15.1 (Lipschitz principle).** If \(\Lambda\) is a full lattice and \(D\) is Lipschitz bounded, then, for \(t\geq1\),
\[
\#(tD\cap\Lambda)
=\frac{\operatorname{vol}(D)}{\operatorname{covol}(\Lambda)}t^n
+O_{D,\Lambda}(t^{n-1}).
\tag{3}
\]

**Proof.** A linear change of variables reduces to \(\Lambda=\mathbf Z^n\), changes volume by the lattice determinant, and preserves finite Lipschitz boundary covers. Partition space into the half-open unit cubes \(\lambda+[0,1)^n\), \(\lambda\in\mathbf Z^n\).

Only cubes meeting \(\partial(tD)\) contribute to the discrepancy between the lattice count and volume. In any other cube, all points lie on the same side of the boundary: connectedness prevents an inside point and an outside point without a boundary point between them. Such a cube contributes either one to both the count and volume or zero to both. Each boundary cube contributes an error of absolute value at most one.

To count the boundary cubes, partition the domain of each \(\phi_j\) into \(M^{n-1}\) cubes, where \(M=\lceil t\rceil\). A scaled image \(t\phi_j\) of one small cube has diameter at most \(tL_j\sqrt{n-1}/M\), uniformly bounded in \(t\). Any set of this bounded diameter meets only a uniformly bounded number of unit cubes: enclose it in a box of fixed side length. Thus at most \(O(t^{n-1})\) cubes meet the boundary. When \(n=1\), each of the finitely many boundary points meets only a bounded number of intervals, giving \(O(1)\). Summing the errors proves (3). \(\square\)

The lemma permits half-open domains. Ownership of their boundary points changes only the boundary-cube error.

## Ideals as orbits of elements

Fix an ideal class \(C\), and choose an integral ideal \(\mathfrak c\) representing \(C^{-1}\). There is a bijection
\[
(\mathfrak c\setminus\{0\})/\mathcal O_K^\times
\longrightarrow
\{\mathfrak a\subseteq\mathcal O_K:\mathfrak a\ne0,\ [\mathfrak a]=C\},
\qquad \alpha\longmapsto(\alpha)\mathfrak c^{-1}.
\tag{4}
\]
For \(\alpha\in\mathfrak c\), the ideal on the right is integral because \(\alpha\mathfrak c^{-1}\subseteq\mathfrak c\mathfrak c^{-1}=\mathcal O_K\). Conversely, an integral ideal in \(C\) makes \(\mathfrak a\mathfrak c\) principal, say \((\alpha)\). The inclusion \(\mathfrak a\mathfrak c\subseteq\mathfrak c\) puts \(\alpha\) in \(\mathfrak c\). Two generators yield the same ideal exactly when they differ by a unit. Norm multiplicativity gives
\[
N(\mathfrak a)=\frac{|N_{K/\mathbf Q}(\alpha)|}{N(\mathfrak c)}.
\tag{5}
\]

We now construct a region that counts these unit orbits. Index the infinite places by \(v=1,\ldots,m\), and give them weights
\[
d_v=\begin{cases}1&v\text{ real},\\2&v\text{ complex}.\end{cases}
\]
For \(z\in V^\times\), meaning that every coordinate is nonzero, set
\[
\ell_v(z)=d_v\log|z_v|,\qquad
|N(z)|=\prod_v|z_v|^{d_v}.
\tag{6}
\]
Choose fundamental units \(\varepsilon_1,\ldots,\varepsilon_q\), and let \(L_j=\ell(\varepsilon_j)\). Their logarithms form a lattice in
\[
H=\{h\in\mathbf R^m:\sum_vh_v=0\}.
\]
Choose its half-open fundamental parallelepiped
\[
P=\left\{\sum_{j=1}^q s_jL_j:0\leq s_j<1\right\}.
\tag{7}
\]
For \(q=0\), this is the singleton zero.

For \(z\in V^\times\), put
\[
\rho=|N(z)|^{1/n},\qquad
h_v(z)=\ell_v(z)-d_v\log\rho.
\tag{8}
\]
Then \(h(z)\in H\). Define the cone and its truncation by
\[
F=\{z\in V^\times:h(z)\in P\},\qquad
D=\{0\}\cup\{z\in F:|N(z)|\leq1\}.
\tag{9}
\]
Positive scalar dilation preserves \(F\) and scales \(\rho\) by that scalar.

To make the orbit statement precise, take the free subgroup \(E_0=\langle\varepsilon_1,\ldots,\varepsilon_q\rangle\). Dirichlet's theorem gives
\(\mathcal O_K^\times=\mu_K\times E_0\).
Multiplication by an element of \(E_0\) shifts \(h(z)\) by its unit-logarithm vector. Uniqueness in (7) therefore makes \(F\) meet each \(E_0\)-orbit exactly once. Roots of unity leave \(h\) fixed and preserve \(F\). On a nonzero field element their action is free. Consequently every full unit orbit of such elements has exactly \(w_K\) representatives in \(F\).

## A bounded domain and its volume

**Proposition 15.2.** The domain \(D\) is bounded and Lipschitz bounded, and
\[
\operatorname{vol}(D)=2^{r_1}\pi^{r_2}R_K.
\tag{10}
\]

**Proof of boundedness and the boundary assertion.** Write \(h=\sum s_jL_j\). For each real sign choice, use the parametrization
\[
\begin{aligned}
z_v&=\eta_v\rho\,e^{h_v}, &&v\text{ real},\quad\eta_v\in\{1,-1\},\\
z_v&=\rho\,e^{h_v/2}e^{i\theta_v}, &&v\text{ complex},
\end{aligned}
\tag{11}
\]
with \(0<\rho\leq1\), \(0\leq s_j<1\), and \(0\leq\theta_v<2\pi\). The parameters \(h_v\) stay bounded, so every coordinate has modulus at most a constant times \(\rho\). This proves boundedness. It also shows that the only possible limit with any coordinate zero is the origin.

Use closed intervals for the parameters in (11) to obtain the closure of \(D\). Away from \(\rho=0\), these are smooth local coordinates: the absolute logarithms determine \(\rho\) and \(s\) uniquely, and the complex angles have ordinary local circle coordinates. At \(0<\rho<1\) with all \(0<s_j<1\), the coordinate map has nonzero Jacobian and its image is interior. Hence the boundary is covered by the following images:

- the top \(\rho=1\), parametrized by \(s\) and \(\theta\);
- each side \(s_j=0\) or \(s_j=1\), parametrized by \(\rho\), the remaining \(s\), and \(\theta\);
- the origin, covered by a constant map.

The top has \(q+r_2=n-1\) parameters; a side has \(1+(q-1)+r_2=n-1\). Rescale angle intervals to \([0,1]\). Each map has bounded derivatives on its compact parameter cube, including \(\rho=0\), because the coordinates depend linearly on \(\rho\) and exponentially only on bounded \(s\). Thus each map is Lipschitz. There are finitely many signs and sides. Circle-angle seams do not add geometric boundary; allowing both angle endpoints still covers the entire circle. For \(q=0\), there are no sides. The argument includes \(n=1\), where the boundary consists of finitely many points.

**Volume calculation.** Let \(L\) be the \(m\)-by-\(q\) matrix with columns \(L_j\), and let \(d=(d_v)\). The coordinate relation is
\[
\ell=d\log\rho+Ls.
\]
Since every column of \(L\) has sum zero, adding all rows into one row and expanding gives
\[
|\det[d,L]|=nR_K.
\tag{12}
\]
For \(q=0\), this states \(d_1=n\), with the empty minor equal to one. For the general case, the remaining minor is exactly the deleted-row determinant defining \(R_K\).

In a fixed real sign sector, a real coordinate has \(d|z_v|=e^{\ell_v}d\ell_v\). A complex coordinate contributes polar area
\[
|z_v|\,d|z_v|\,d\theta_v
=\tfrac12e^{\ell_v}d\ell_v\,d\theta_v.
\]
Thus the full volume element in (11) is
\[
2^{-r_2}nR_K\,\rho^{n-1}\,d\rho\,ds\,d\theta.
\tag{13}
\]
There are \(2^{r_1}\) real sign sectors, the angle integral is \((2\pi)^{r_2}\), the \(s\)-cube has volume one, and \(\int_0^1n\rho^{n-1}d\rho=1\). Their product is (10). Boundary ownership changes no volume. \(\square\)

The determinant in (12) uses the projected regulator convention. Replacing it by the Euclidean covolume of the unit lattice in \(H\) would introduce an unwanted factor \(\sqrt m\).

## The count in each ideal class

Set
\[
\kappa_K=\frac{2^{r_1}(2\pi)^{r_2}R_K}
{w_K\sqrt{|d_K|}}.
\tag{14}
\]

**Theorem 15.3.** For each ordinary ideal class \(C\), as \(X\to\infty\),
\[
A_C(X):=\#\{\mathfrak a\ne0:\mathfrak a\subseteq\mathcal O_K,\
[\mathfrak a]=C,\ N(\mathfrak a)\leq X\}
=\kappa_KX+O_{K,C}(X^{1-1/n}).
\tag{15}
\]
The count of all nonzero integral ideals satisfies
\[
A_K(X)=h_K\kappa_KX+O_K(X^{1-1/n}).
\tag{16}
\]

**Proof.** Choose \(\mathfrak c\) as in (4), and put \(T=XN(\mathfrak c)\). The condition (5) is \(|N(\alpha)|\leq T\). Each ideal has exactly \(w_K\) representatives in \(F\), and the domain with this bound is \(T^{1/n}D\). Therefore the count is exactly
\[
A_C(X)=\frac{\#(\mathfrak c\cap T^{1/n}D)-1}{w_K}.
\tag{17}
\]
The subtraction removes the origin. Apply Lemma 15.1 and Proposition 15.2:
\[
\#(\mathfrak c\cap T^{1/n}D)
=\frac{2^{r_1}\pi^{r_2}R_K\,XN(\mathfrak c)}
{2^{-r_2}\sqrt{|d_K|}N(\mathfrak c)}
+O_{K,\mathfrak c}(X^{1-1/n}).
\]
The ideal norm cancels. Dividing by \(w_K\) gives (15); the constant subtraction is absorbed in the error, also when \(n=1\). There are finitely many classes, so summing their asymptotics gives (16). The coefficient is independent of the chosen class, although its error constant may depend on the representative lattice. \(\square\)

For \(K=\mathbf Q\), the conventions are \(r_1=1,r_2=0,R_K=1,w_K=2,d_K=1\), giving \(\kappa_K=1\). The exact count is \(\lfloor X\rfloor\), which verifies the degree-one error \(O(1)\).

## Two checks of the constant

### Gaussian ideals

For \(\mathbf Q(i)\), the preceding class-number calculation gives \(h_K=1\). Every ideal is principal, its generators differ by the four units, and
\[
N(a+bi)=a^2+b^2.
\]
There are no free units, so \(D\) is the closed unit disk. Consequently
\[
A_K(X)=\frac{\#\{(a,b)\in\mathbf Z^2:a^2+b^2\leq X\}-1}{4}
=\frac{\pi}{4}X+O(\sqrt X).
\tag{18}
\]
This is exactly (14), since \(R_K=1\), \(w_K=4\), and \(\sqrt{|d_K|}=2\). If explicit generators are desired, the sector \(a>0,b\geq0\) selects one in each nonzero unit orbit; the positive horizontal axis owns the axis cases.

### A real quadratic cone

For any real quadratic field, let \(\varepsilon>1\) be a fundamental unit under one embedding, and put \(R=\log\varepsilon\). The other absolute value is \(\varepsilon^{-1}\), whether the unit norm is \(1\) or \(-1\). Thus its unit-logarithm vector is \((R,-R)\). Formula (11) becomes
\[
z_1=\eta_1\rho\,e^{sR},\qquad
z_2=\eta_2\rho\,e^{-sR},\qquad
0<\rho\leq1,\quad0\leq s<1.
\tag{19}
\]
In each of the four sign sectors the absolute Jacobian is \(2R\rho\). Its integral is \(R\), so \(\operatorname{vol}(D)=4R\), exactly (10). Equivalently, the cone and truncation satisfy
\[
1\leq|z_1/z_2|<\varepsilon^2,\qquad |z_1z_2|\leq1.
\tag{20}
\]
Both coordinates stay bounded as their product tends to zero, because their ratio stays in a compact interval. The apparent cusp is therefore just the origin, parametrized regularly by \(\rho\) in (19).

For \(K=\mathbf Q(\sqrt2)\), the previously proved values are
\[
h_K=1,\quad w_K=2,\quad d_K=8,\quad
\varepsilon=1+\sqrt2,\quad R_K=\log(1+\sqrt2).
\]
The ideal density is
\[
\kappa_K=\frac{\log(1+\sqrt2)}{\sqrt2}.
\tag{21}
\]
There are two cone representatives of each ideal, because the torsion units are \(1,-1\). Although \(\varepsilon\) has norm \(-1\) and changes one embedding's sign, the use of all four sign sectors in (19) preserves the exact orbit count.

An integer description makes this example directly countable. For \(\alpha=a+b\sqrt2\), put \(z_1=a+b\sqrt2\), \(z_2=a-b\sqrt2\). The cone (20) is equivalent to
\[
ab\geq0,\qquad (a-b)(a-2b)>0.
\tag{22}
\]
The lower inequality follows from \(z_1^2-z_2^2=4ab\sqrt2\). For the upper inequality, use \(\varepsilon^4=17+12\sqrt2\) to obtain
\[
z_1^2-\varepsilon^4z_2^2
=-4(4+3\sqrt2)(a^2-3ab+2b^2).
\]
Thus (22) implements the half-open upper boundary exactly. Counting its nonzero integer pairs with \(|a^2-2b^2|\leq X\), and dividing by two, gives the ideal count without any logarithmic rounding.

## Exercises and complete solutions

**Exercise 1.** Verify the density \(\pi/4\) for \(\mathbf Q(i)\) directly from its integer lattice.

**Solution 1.** The disk of radius \(\sqrt X\) has area \(\pi X\). Its circle boundary is covered by a Lipschitz parametrization, so Lemma 15.1 for \(\mathbf Z^2\) gives \(\pi X+O(\sqrt X)\) lattice points. Remove the origin and divide by four, since multiplication by \(1,-1,i,-i\) acts freely on each nonzero generator and preserves the norm. This yields (18). In terms of the general factors, the lattice covolume is \(2^{-1}\sqrt4=1\), the logarithmic domain has volume \(\pi\), and \(w_K=4\). These checks use the same coordinate measure as (2).

**Exercise 2.** Prove the Lipschitz principle, including half-open boundary choices and the case \(n=1\).

**Solution 2.** Send a lattice basis to the standard basis. The determinant rescales the domain volume by \(1/\operatorname{covol}(\Lambda)\). For each boundary map, subdivide its parameter cube into \(\lceil t\rceil^{n-1}\) equal cubes. The image of each under \(t\phi_j\) has bounded diameter, hence meets only a fixed number of unit lattice cells. Thus \(O(t^{n-1})\) cells meet \(\partial(tD)\). All other cells are entirely inside or outside and give equal contributions to count and volume. Boundary cells each contribute bounded error, regardless of whether a boundary lattice point is included. In dimension one the boundary consists of finitely many points, so only \(O(1)\) intervals are involved. This proves every case of (3).

**Exercise 3.** Compute the volume of the unit-domain truncation for a real quadratic field and recover its class density.

**Solution 3.** Use (19) with \(R=\log\varepsilon\). Differentiation gives the determinant
\[
\det\begin{pmatrix}
\eta_1e^{sR}&\eta_1\rho R e^{sR}\\
\eta_2e^{-sR}&-\eta_2\rho R e^{-sR}
\end{pmatrix}=-2\eta_1\eta_2R\rho.
\]
Integrating its absolute value for \(0\leq\rho\leq1\), \(0\leq s\leq1\) gives \(R\) in each sign sector, hence \(4R\) in total. The ideal lattice has covolume \(\sqrt{d_K}N(\mathfrak c)\), and the norm cutoff is \(XN(\mathfrak c)\). Divide by the two torsion units to get \(\kappa_K=2R/\sqrt{d_K}\), which specializes to (21). A negative norm of the fundamental unit changes signs, not this Jacobian or the orbit multiplicity.

**Exercise 4.** Supply a finite Lipschitz parametrization cover of the boundary in arbitrary signature, including its origin.

**Solution 4.** Fix one of the \(2^{r_1}\) real sign choices. In (11), write \(h_v=\sum_j s_jL_{vj}\) and replace every angle by \(2\pi a_v\), \(0\leq a_v\leq1\). For the top, set \(\rho=1\); this gives a map from the \(q+r_2=n-1\) dimensional cube. For each \(j\), set \(s_j=0\) and \(s_j=1\) in turn; retain \(\rho\), all other \(s\), and the angles, again \(n-1\) variables. All derivatives of the exponentials on these compact cubes are bounded, and the dependence on \(\rho\) is linear, so each map is Lipschitz even at \(\rho=0\). Add one constant map for the origin. Every other point with \(\rho<1\) and all \(s_j\) strictly between their endpoints is interior by the nonzero coordinate Jacobian, so this list covers the whole boundary. There are no side maps when \(q=0\), and when \(n=1\) the top maps are singleton endpoints. Periodic angle endpoints cover circle seams without requiring any additional boundary pieces.

## What this lesson does not prove

The unit theorem, regulator convention, ideal-lattice covolume, integral bases, and class numbers used in the examples are imported from the preceding lessons. All three numbered counting results and all four solutions are proved here. Sharper lattice-point error terms, including improvements for the circle problem, are outside this count. Analytic properties of the Dedekind zeta function are treated in the next lesson; none is used to derive the ideal density.

## References

- Erich Hecke, *Vorlesungen über die Theorie der algebraischen Zahlen*, 1923, Chapter VI §§40–42, printed pp.155–164; Satz 121 gives the common class density, and Satz 122 its sum over classes.
- J. S. Milne, [*Algebraic Number Theory*, v3.08](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Chapter 5, “Regulators,” printed p.94, for the weighted logarithm determinant convention.
- Andrew V. Sutherland, [MIT 18.785 Lecture 19](https://math.mit.edu/classes/18.785/2021fa/LectureNotes19.pdf), Lemma 19.5, Section 19.1.1 and Theorem 19.8, pp.2-7. Source scaled-coordinate volume and covolume both have factor 2^r2; the quotient matches this lesson ordinary-coordinate convention.
