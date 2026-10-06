# The adèle ring of a number field

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A number field can be studied in every completion at once. The adèle ring makes this possible while retaining local compactness. Its topology expresses an arithmetic distinction: a number field is discrete when all places are present, but dense after any one place is removed. We will prove both assertions, construct fundamental domains, calculate their volume, and obtain simultaneous bounds on a nonzero field element.

We assume the results of [Restricted products and profinite completions](NT-ADL-01.md), Places of number fields in extensions and the product formula, Local fields: classification and Haar measure, and Lattices, Minkowski’s theorem and the Minkowski embedding. We also use the integral bases, ideal factorization, Chinese remainders and finite torsion-free modules proved in Discriminants and integral bases, Discrete valuation rings and Dedekind domains, and Norms of ideals, the ideal class group, and modules over Dedekind domains. The exact statements and conventions are collected near the end. The constructions can be compared with [Sutherland 25], [Getz–Hahn draft] and [Milne ANT]. [Sutherland 14] supplies the canonical Minkowski measure convention. We give complete additive quotient, box and approximation proofs here.

## Local information with an integral tail

Let \(K\) be a number field of degree \(n\), with \(r_1\) real places and \(r_2\) complex places, so \(n=r_1+2r_2\). At each place \(v\), let \(K_v\) be its completion. If \(v\) is finite, write \(\mathcal O_v\) for its valuation ring, \(\mathfrak p_v\) for the corresponding prime ideal of \(\mathcal O_K\), and \(q_v=\#(\mathcal O_K/\mathfrak p_v)\). Normalize \(\operatorname{ord}_v\) to have value group \(\mathbf Z\).

Our multiplicative local sizes are

\[
|x|_v=
\begin{cases}
q_v^{-\operatorname{ord}_v(x)},&v\text{ finite},\\
|x|,&K_v=\mathbf R,\\
|x|^2,&K_v=\mathbf C.
\end{cases}
\]

The last expression is the square of the ordinary complex modulus. It is useful for the product formula and measure scaling, but does not satisfy the ordinary triangle inequality. Whenever we use a geometric radius in \(\mathbf C\), we mean the ordinary modulus. With these conventions, \(\prod_v|x|_v=1\) for \(x\in K^\times\).

An **adèle** is a tuple \(a=(a_v)_v\), with \(a_v\in K_v\), such that \(a_v\in\mathcal O_v\) at all but finitely many finite places. Thus

\[
\mathbb A_K=\prod_v'(K_v,\mathcal O_v)
=K_\infty\times\mathbb A_{K,f},
\qquad K_\infty=\prod_{v\mid\infty}K_v
\simeq\mathbf R^{r_1}\times\mathbf C^{r_2}.
\]

There is no integral restriction at an infinite place. Addition and multiplication are coordinatewise. For a finite set \(S\) containing the infinite places, put

\[
\mathbb A_{K,S}=\prod_{v\in S}K_v\times
\prod_{v\notin S}\mathcal O_v.
\]

These are open subrings, each with its product topology, and their union is \(\mathbb A_K\). A basic open set is

\[
\prod_{v\in S}U_v\times\prod_{v\notin S}\mathcal O_v,
\tag{1}
\]

where every \(U_v\subset K_v\) is open. The requirement on the entire tail matters: this topology is finer than the topology inherited from the unrestricted product. An adèle may fail to be integral at finitely many places, but a neighborhood controls where new failures can occur.

Every element of \(K\) defines a diagonal adèle. Indeed, a nonzero field element has nonzero valuations at only finitely many finite places. We identify \(K\) with this diagonal subfield. For later use set

\[
\widehat{\mathcal O}_K=\prod_{v<\infty}\mathcal O_v.
\]

This is a compact open subring of \(\mathbb A_{K,f}\). It is not open in the full adèle ring when embedded with zero infinite component.

## Changing the number field

**Proposition 2.1.** The ring \(\mathbb A_K\) is a Hausdorff locally compact topological ring. If \(L/K\) is finite, the canonical map

\[
\Phi:L\otimes_K\mathbb A_K\longrightarrow\mathbb A_L,
\qquad
\ell\otimes(a_v)_v\longmapsto(\ell a_v)_{w\mid v}
\tag{2}
\]

is an isomorphism of topological rings. On the tensor product, use the finite product topology from any \(K\)-basis of \(L\). In particular,

\[
\mathbb A_K\simeq K\otimes_{\mathbf Q}\mathbb A_{\mathbf Q},
\qquad
\mathbb A_K\simeq\mathbb A_{\mathbf Q}^{\,n}
\tag{3}
\]

as topological rings in the first assertion and as topological \(\mathbb A_{\mathbf Q}\)-modules in the second.

**Proof.** Each stage \(\mathbb A_{K,S}\) is a product of finitely many locally compact fields and a compact product of valuation rings. It is locally compact and Hausdorff. The stages are open and cover the ring, proving these assertions for the underlying space.

For continuity of addition or multiplication at \((a,b)\), enlarge \(S\) until both adèles belong to \(\mathbb A_{K,S}\). Operations on that stage are continuous coordinatewise. Their values stay in the integral tail because each \(\mathcal O_v\) is a subring. Continuity on these open neighborhoods proves continuity on the whole ring.

We use the local field-extension identity

\[
L\otimes_K K_v\simeq\prod_{w\mid v}L_w.
\tag{4}
\]

Its map is the local version of (2), and is a homeomorphism of finite-dimensional \(K_v\)-vector spaces. To pass to restricted products we must check the integral lattices.

Here is the completion calculation. For a rational prime \(p\), finite freeness over \(\mathbf Z\), followed by the Chinese remainder theorem, gives

\[
\begin{aligned}
\mathcal O_K\otimes_{\mathbf Z}\mathbf Z_p
&\simeq\varprojlim_m\mathcal O_K/p^m\mathcal O_K\\
&\simeq\prod_{v\mid p}\varprojlim_m
\mathcal O_K/\mathfrak p_v^{\,m e(v/p)}
\simeq\prod_{v\mid p}\mathcal O_v.
\end{aligned}
\tag{5}
\]

The powers \(m e(v/p)\) form a cofinal sequence of powers of \(\mathfrak p_v\). Localizing before completing does not change these quotients: every denominator outside \(\mathfrak p_v\) is invertible modulo \(\mathfrak p_v^k\).

For the relative version, localize \(\mathcal O_L\) at \(\mathfrak p_v\) as a module over \((\mathcal O_K)_{\mathfrak p_v}\). It is finite and torsion-free over this discrete valuation ring, hence free. Tensoring this finite free module with the completed ring equals the inverse limit of its quotients by \(\mathfrak p_v^m\). Decomposing \(\mathfrak p_v\mathcal O_L\) into prime powers and applying the Chinese remainder theorem in this inverse limit gives

\[
\mathcal O_L\otimes_{\mathcal O_K}\mathcal O_v
\simeq\prod_{w\mid v}\mathcal O_w
\tag{6}
\]

at every finite place. Ramification causes no exception to this identity of completed integer rings.

Choose a \(K\)-basis \(e_1,\ldots,e_m\) of \(L\) consisting of algebraic integers. The lattice \(M=\sum_j\mathcal O_K e_j\) lies in \(\mathcal O_L\), and some nonzero \(d\in\mathcal O_K\) satisfies \(d\mathcal O_L\subset M\). Indeed, express a finite set of \(\mathcal O_K\)-module generators of \(\mathcal O_L\) in this basis and clear denominators. Thus \(M\otimes\mathcal O_v=\mathcal O_L\otimes\mathcal O_v\) outside the finitely many primes dividing \(d\).

In these coordinates the local map \(K_v^m\to\prod_{w\mid v}L_w\) takes \(\mathcal O_v^m\) onto \(\prod_{w\mid v}\mathcal O_w\) at almost every finite place. The local maps and their inverses therefore take restricted tuples to restricted tuples. They are homeomorphisms on the open product stages after adjoining the exceptional places, and assemble to a global homeomorphism. Formula (2) respects multiplication, so it is a ring isomorphism.

Changes of \(K\)-basis act by invertible matrices over \(K\) on \(\mathbb A_K^m\); the matrix and its inverse define continuous maps. The tensor-product topology is independent of the basis. Taking the base field to be \(\mathbf Q\) proves (3). The module identification depends on a basis; the ring map does not. \(\square\)

The distinction between (6) and the basis lattice is useful when comparing sources. [Sutherland 25, Proposition 25.10, pp.6–7] uses the canonical completed integer rings to pass from local tensor products to adèles; [Milne ANT, Proposition 8.2, p.136] gives the same local map \(\ell\otimes a\mapsto(\ell a)_w\). Our completion argument proves (6) at every finite place, including ramified ones. It is the auxiliary lattice \(M=\sum_j\mathcal O_K e_j\), chosen from a field basis, that agrees with \(\mathcal O_L\) only outside finitely many primes. The proof does not assume a global integral basis for \(\mathcal O_L\) over \(\mathcal O_K\): freeness is used after localization at a discrete valuation ring.

## Representatives for the additive quotient

Begin with \(\mathbf Q\), and write \(\widehat{\mathbf Z}=\prod_p\mathbf Z_p\). A rational number belongs to every \(\mathbf Z_p\) exactly when its reduced denominator has no prime divisor. Hence

\[
\mathbf Q\cap(\mathbf R\times\widehat{\mathbf Z})=\mathbf Z.
\tag{7}
\]

Every finite rational adèle can be made integral by subtracting a rational number. Take its negative \(p\)-adic digits at each of its finitely many nonintegral places and add the resulting rational principal parts. A principal part at \(p\) has denominator a power of \(p\), so is integral at every other prime. Thus

\[
\mathbb A_{\mathbf Q}
=\mathbf Q+(\mathbf R\times\widehat{\mathbf Z}).
\tag{8}
\]

After this subtraction, subtract an integer to move the real coordinate into \([0,1)\). The integer subtraction also changes every finite coordinate; it preserves their integrality.

**Theorem 2.2.** The diagonal subgroup \(K\) is discrete and closed in \(\mathbb A_K\), and \(\mathbb A_K/K\) is compact. Every coset in \(\mathbb A_{\mathbf Q}/\mathbf Q\) has exactly one representative in

\[
F_{\mathbf Q}=[0,1)\times\widehat{\mathbf Z}.
\tag{9}
\]

**Proof.** In the rational case, the open neighborhood

\[
(-1/2,1/2)\times\widehat{\mathbf Z}
\]

meets \(\mathbf Q\) only at zero, by (7). This proves discreteness. A discrete subgroup of a Hausdorff topological group is closed: choose an open neighborhood \(V\) of zero whose difference set meets the subgroup only at zero. Any translate of \(V\) contains at most one subgroup element. A point in the closure must equal that element, since otherwise a smaller neighborhood excluding it contradicts the definition of closure.

Existence of representatives in (9) follows from (8). If two representatives differ by \(q\in\mathbf Q\), their finite components imply \(q\in\mathbf Z\). Their real components differ by a number strictly between \(-1\) and \(1\), so \(q=0\). This proves uniqueness.

The domain (9) is half-open and is not compact. Its compact closure \([0,1]\times\widehat{\mathbf Z}\) still maps onto the quotient. Thus the quotient is compact.

Choose a \(\mathbf Q\)-basis of \(K\). Under (3), the diagonal \(K\) becomes the subgroup \(\mathbf Q^n\subset\mathbb A_{\mathbf Q}^n\). It is discrete and closed, and its quotient is the finite product of \(n\) compact rational quotients. This proves the assertions for \(K\). \(\square\)

For volume calculations we want a domain adapted to the integer rings. Choose an integral basis \(\omega_1,\ldots,\omega_n\) of \(\mathcal O_K\), let \(j:K\to K_\infty\) be the Minkowski embedding, and put

\[
P_K=\left\{\sum_{i=1}^n t_i j(\omega_i):0\leq t_i<1\right\}.
\]

Equations (3) and (5), applied to this basis and the rational principal-part construction, give

\[
\mathbb A_K=K+(K_\infty\times\widehat{\mathcal O}_K),
\qquad
K\cap(K_\infty\times\widehat{\mathcal O}_K)=\mathcal O_K.
\tag{10}
\]

For the intersection, write an element of \(K\) in the integral basis. By (5), integrality at all finite places says its rational coordinates belong to every \(\mathbf Z_p\), so they are integers. Reducing the infinite component modulo \(j(\mathcal O_K)\) now shows that

\[
F_K=P_K\times\widehat{\mathcal O}_K
\tag{11}
\]

is a Borel fundamental domain with unique representatives. Its closure is compact. If \(U\subset K_\infty\) is bounded, then

\[
K\cap(U\times\widehat{\mathcal O}_K)
\]

is finite: it corresponds to the points of the full lattice \(j(\mathcal O_K)\) in a bounded set.

**Worked example: rational principal parts.** Take an adèle with real component \(13/10\), components \(3/8\) at \(2\) and \(7/25\) at \(5\), and zero at all other primes. Subtract

\[
q=3/8+7/25=131/200.
\]

At \(2\) the remaining value is \(-7/25\), which is integral; at \(5\) it is \(-3/8\), also integral. At every other prime the denominator of \(q\) is a unit. The remaining real component is \(129/200\in[0,1)\), so this already gives the representative in (9).

**Worked example: the solenoid quotient.** Inclusion induces an isomorphism of topological groups

\[
(\mathbf R\times\widehat{\mathbf Z})/\mathbf Z
\longrightarrow\mathbb A_{\mathbf Q}/\mathbf Q.
\tag{12}
\]

Here \(\mathbf Z\) is embedded diagonally: \(m\mapsto(m,(m)_p)\). Surjectivity and the kernel follow from (7)–(8). The source is compact, since \([0,1]\times\widehat{\mathbf Z}\) maps onto it. The target is Hausdorff by Theorem 2.2. Thus the continuous bijection is a homeomorphism. This quotient is called the rational solenoid; its further topological structure is studied in the lesson on solenoids. Formula (9) supplies measurable representatives, not a continuous product decomposition: crossing a real endpoint also changes the finite coordinate by a diagonal integer.

## How the discriminant measures the quotient

Fix additive Haar measures \(dx_v\) by

\[
dx_v=dx\quad(K_v=\mathbf R),\qquad
dx_v=2\,dx\,dy=|dz\wedge d\bar z|
\quad(K_v=\mathbf C),\qquad
\mu_v(\mathcal O_v)=1\quad(v<\infty).
\tag{13}
\]

The restricted product measure \(dx=\prod_v dx_v\) is characterized on product sets with integral tails by the product of local measures. Multiplication by \(a\in K_v^\times\) scales \(dx_v\) by \(|a|_v\). At a finite place this follows by decomposing \(\mathcal O_v\) into \(q_v\) translates of its maximal ideal; at a complex place it follows from the real determinant \(|a|^2\).

Let \(d_K\) be the field discriminant. We give the discrete additive subgroup \(K\) counting measure. The quotient measure is induced from \(dx\) with this choice; its total mass is the measure of a Borel fundamental domain such as (11).

**Proposition 2.4.** With (13),

\[
\operatorname{vol}(\mathbb A_K/K)=\sqrt{|d_K|}.
\tag{14}
\]

**Proof.** In ordinary real coordinates on \(K_\infty\), form the matrix \(M\) whose columns are \(j(\omega_i)\), recording real and imaginary parts at each complex place. The Euclidean volume of \(P_K\) is \(|\det M|\).

Let \(B=(\tau(\omega_i))_{\tau,i}\) be the matrix of all \(n\) complex embeddings, including both members of each conjugate pair. The trace matrix is \(B^{\mathsf T}B\), so

\[
d_K=\det(B^{\mathsf T}B)=(\det B)^2.
\]

Replacing a real-coordinate pair \((u,v)\) by \((u+iv,u-iv)\) has determinant \(-2i\). Consequently

\[
|\det B|=2^{r_2}|\det M|,
\qquad
|\det M|=2^{-r_2}\sqrt{|d_K|}.
\tag{15}
\]

Our infinite measure multiplies Euclidean measure by \(2^{r_2}\). Thus \(\mu_\infty(P_K)=\sqrt{|d_K|}\). The finite factor in (11) has measure \(1\), proving (14). \(\square\)

Using \(dx\,dy\) at complex places would instead give \(2^{-r_2}\sqrt{|d_K|}\). A change of integral basis changes \(M\) by a matrix in \(\mathrm{GL}_n(\mathbf Z)\), whose determinant has absolute value \(1\), so does not change the answer.

This accounts for the apparent difference between two source conventions. [Milne ANT, Proposition 4.26, pp.79–80] gives Euclidean covolume \(2^{-r_2}N(\mathfrak a)\sqrt{|d_K|}\) for an ideal lattice. [Sutherland 14, §14.2 and Proposition 14.16] uses the canonical inner product, whose measure contributes the factor \(2^{r_2}\). The local normalization in [Sutherland 25, p.6] is also \(2\,dx\,dy\) at each complex place. Equation (14) follows with exactly those factors; a topological tensor-product isomorphism by itself cannot determine this numerical covolume.

A different finite normalization is used with Fourier transforms. For the standard trace character \(\psi_v=\psi_{\mathbf Q_p}\circ\operatorname{Tr}_{K_v/\mathbf Q_p}\), let \(\mathfrak D_v^{-1}\) be the trace-dual lattice of \(\mathcal O_v\). Its definition identifies it with the annihilator of \(\mathcal O_v\). If a self-dual measure gives \(\mathcal O_v\) mass \(c\), Fourier inversion on its indicator gives

\[
1=c^2N(\mathfrak D_v),\qquad
c=N(\mathfrak D_v)^{-1/2}.
\]

Thus the self-dual finite measure is \(N(\mathfrak D_v)^{-1/2}dx_v\). At an unramified finite place it agrees with the measure giving \(\mathcal O_v\) mass one. Here is the local algebra behind that assertion. Put \(E=K_v\) and \(F=\mathbb Q_p\). Theorem 2.1 of Unramified and totally ramified extensions gives \(\mathcal O_E=\mathcal O_F[a]\), where the monic minimal polynomial \(f\) of \(a\) reduces to a separable residue polynomial. Hence \(f'(a)\) has nonzero residue and is a unit. Proposition 14.2 of The different and the discriminant then gives \(\mathfrak D_{E/F}=(f'(a))=\mathcal O_E\), as required. Proposition 3.1 of Places of number fields in extensions and the product formula identifies the unramified global place with this local extension.

The infinite factors in (13) are self-dual for the standard trace characters. The local character pairing and Fourier normalization used in this comparison are proved in Propositions 5.1–5.2 of Additive characters, self-dual measures and Poisson summation on the adèles, including its Lemma 5.4A for the entire archimedean space. This is only a normalization comparison; the proofs of this lesson’s additive quotient, box and approximation results use (13). [Getz–Hahn draft, Appendix B, §§B.1–B.2] and [Sutherland 12] provide the classical references.

## A box large enough to contain a field element

An **idèle** is a tuple \(\alpha=(\alpha_v)\) with \(\alpha_v\in K_v^\times\) and \(\alpha_v\in\mathcal O_v^\times\) at almost every finite place. These are precisely the units of \(\mathbb A_K\): both a tuple and its coordinatewise inverse must have integral tails. Define

\[
\|\alpha\|_{\mathbb A}=\prod_v|\alpha_v|_v.
\]

Only finitely many factors differ from \(1\). We need the following bound before proving strong approximation.

**Lemma 2.5 (adelic Minkowski lemma).** One may take

\[
C_K=\left(\frac2\pi\right)^{r_2}\sqrt{|d_K|}.
\tag{16}
\]

For every idèle \(\alpha\) with \(\|\alpha\|_{\mathbb A}\geq C_K\), there exists \(x\in K^\times\) such that

\[
|x|_v\leq|\alpha_v|_v\qquad\text{at every place }v.
\tag{17}
\]

**Proof.** First suppose \(\|\alpha\|_{\mathbb A}>C_K\). Establish the counting principle behind Blichfeldt's argument. If a measurable set \(E\subset\mathbb A_K\) satisfies \(\mu(E)>\mu(F_K)\), two distinct points of \(E\) differ by a nonzero element of \(K\). Indeed, the translates \(F_K+k\), for \(k\in K\), partition the ring. Translation invariance and Tonelli's theorem give

\[
\int_{F_K}\sum_{k\in K}\mathbf1_E(f+k)\,df=\mu(E).
\tag{18}
\]

The group \(K\) is countable. If every coset met \(E\) at most once, the sum would be at most \(1\), contradicting the strict volume inequality. A coset meeting \(E\) twice gives the asserted difference.

Let \(R_v\) be the ordinary real or complex modulus of \(\alpha_v\) at an infinite place. Choose

\[
E=\prod_{v\text{ real}}[-R_v/2,R_v/2]
\times\prod_{v\text{ complex}}\{z:|z|\leq R_v/2\}
\times\prod_{v<\infty}\alpha_v\mathcal O_v.
\tag{19}
\]

This is a compact measurable subset of an open product stage. At real places its factor has measure \(R_v=|\alpha_v|_v\). At complex places its measure is

\[
2\pi(R_v/2)^2=(\pi/2)|\alpha_v|_v.
\]

At finite places its measure is \(|\alpha_v|_v\). Hence

\[
\mu(E)=(\pi/2)^{r_2}\|\alpha\|_{\mathbb A}
>\sqrt{|d_K|}=\mu(F_K).
\]

Choose distinct \(y,z\in E\) with \(x=y-z\in K^\times\). At a real place their difference has modulus at most \(R_v\). At a complex place use the ordinary triangle inequality to obtain \(|y_v-z_v|\leq R_v\), then square to obtain (17). At a finite place \(\alpha_v\mathcal O_v\) is an additive subgroup, so the difference stays in it.

Now suppose \(\|\alpha\|_{\mathbb A}=C_K\). Choose an infinite place \(w\), and for \(j\geq1\) replace \(\alpha_w\) by \((1+1/j)\alpha_w\), leaving every other component fixed. The resulting idèle has norm \((1+1/j)^{d_w}C_K>C_K\), where \(d_w=1\) at a real place and \(d_w=2\) at a complex place. The strict case gives a nonzero \(x_j\in K\) with the corresponding bounds. All these elements lie in one fixed compact box: double only the ordinary radius at \(w\), retain the other infinite radii, and retain every finite subgroup \(\alpha_v\mathcal O_v\). By Theorem 2.2, this box meets \(K\) in a finite set. Some nonzero \(x\) therefore occurs for infinitely many \(j\). Its bounds at \(v\ne w\) already have the required size. Along that unbounded subsequence, its bound at \(w\) tends to \(|\alpha_w|_w\). Thus (17) also holds at equality. \(\square\)

The half-radius choice is essential. Applying the counting principle directly to the full box would only bound the difference by twice its archimedean radii. Halving affects a complex factor by \(1/4\), because it has two real dimensions. We need not halve the finite factors, which are additive subgroups.

Compactness and discreteness extend the strict volume argument to the closed boundary. The product formula explains why a size hypothesis is needed: (17) for nonzero \(x\) implies \(1\leq\|\alpha\|_{\mathbb A}\).

[Sutherland 25, Lemma 25.14, p.9] proves the same local-bound mechanism with an unspecified positive constant and a strict inequality. Here the real intervals of length \(R_v\), the complex disks of radius \(R_v/2\), and (13) determine the explicit constant (16), and the final compactness argument retains equality. [Milne ANT, Theorems 4.17 and 4.19, pp.75–76] gives the corresponding finite-dimensional counting and closed-boundary arguments. The ideal-norm bound in its Proposition 4.27 uses a different convex body; its constant is not the simultaneous place-by-place bound (16).

## Removing a place frees approximation

For a fixed place \(v_0\), write

\[
\mathbb A_K^{(v_0)}
=\prod_{v\ne v_0}'(K_v,\mathcal O_v),
\]

imposing integral restrictions only at finite places. Projection from the full ring forgets the \(v_0\)-coordinate.

**Theorem 2.3 (strong approximation).** For every finite or infinite place \(v_0\), the diagonal image of \(K\) is dense in \(\mathbb A_K^{(v_0)}\).

Equivalently, let \(S\) be a finite set disjoint from \(\{v_0\}\), containing all infinite places other than \(v_0\). Given \(a_v\in K_v\) and \(\varepsilon_v>0\) for \(v\in S\), there exists \(q\in K\) such that

\[
|q-a_v|_v<\varepsilon_v\quad(v\in S),
\qquad
q\in\mathcal O_v\quad(v<\infty,\ v\notin S\cup\{v_0\}).
\tag{20}
\]

**Proof.** Let \(D=\overline{P_K}\times\widehat{\mathcal O}_K\). By (11), every adèle is \(k+d\) for \(k\in K\) and \(d\in D\). For each infinite place set

\[
B_v=\max\left(1,\sup_{d\in D}|d_v|_v\right),
\]

and for finite places set \(B_v=1\). These are bounds on a fixed compact set, not norms on \(K_\infty\).

Choose an idèle \(\beta\) with

\[
|\beta_v|_v B_v<\varepsilon_v\quad(v\in S),
\qquad
|\beta_v|_v=1\quad(v<\infty,\ v\notin S\cup\{v_0\}).
\]

At \(v_0\) choose its component sufficiently large that \(\|\beta\|_{\mathbb A}>C_K\). Every completion has elements of arbitrarily large size, so this is possible whether \(v_0\) is finite or infinite. Lemma 2.5 supplies nonzero \(c\in K\) with \(|c|_v\leq|\beta_v|_v\) everywhere.

Let \(t\in\mathbb A_K\) have components \(a_v\) for \(v\in S\) and zero elsewhere, including at \(v_0\). Apply the representative property to \(c^{-1}t\). There are \(k\in K\) and \(d\in D\) with

\[
c^{-1}t=k+d.
\]

Set \(q=ck\). Then \(t-q=cd\), so for \(v\in S\),

\[
|a_v-q|_v\leq|\beta_v|_v B_v<\varepsilon_v.
\]

At a finite place outside \(S\cup\{v_0\}\), both \(c\) and \(d_v\) are integral and \(t_v=0\), so \(q=-cd_v\) is integral. This proves (20).

A neighborhood of a truncated adèle contains a set as in (20): include in \(S\) its finitely many nonintegral places, all retained infinite places, and the places with specified local neighborhoods. Choose smaller local balls inside those neighborhoods. Thus (20) proves density. \(\square\)

The omitted coordinate pays for the simultaneous small bounds on the other coordinates: it allows an arbitrarily large component before invoking Lemma 2.5. The proof uses neither a unit theorem nor multiplicative strong approximation.

**Worked example: rational finite approximation.** Suppose we want

\[
q-1/4\in\mathbf Z_2,\qquad q-2/9\in\mathbf Z_3,
\]

and integrality at every other finite prime. Set \(q=m/36\). The congruences become

\[
m\equiv1\pmod4,\qquad m\equiv8\pmod9.
\]

Choose \(m=17\). Indeed, \(17/36-1/4=2/9\in\mathbf Z_2\), while \(17/36-2/9=1/4\in\mathbf Z_3\). Its denominator has no other prime factors. Higher precision gives higher prime-power congruences, solved by the same Chinese remainder theorem. In particular, \(\mathbf Q\) is dense in \(\mathbb A_{\mathbf Q,f}\), the additive assertion used in [Bost–Connes 1995, §3, proof of Proposition 12].

This does not give density in the full ring. If a rational \(q\) is integral at every finite prime, it is an integer. No such \(q\) lies in \((1/3,2/3)\). Thus \((1/3,2/3)\times\widehat{\mathbf Z}\) contains no rational number.

## Exercises

**Exercise 1 (easy).** Prove (7) and (8) directly, without using Theorem 2.2. Explain why subtracting an arbitrary real number cannot replace rational subtraction in (8).

**Exercise 2 (medium).** Exhibit a Borel fundamental domain for \(\mathbf Q(i)\) in \(\mathbb A_{\mathbf Q(i)}\). Compute its volume with (13), including the discriminant.

**Exercise 3 (medium).** Prove strong approximation for \(\mathbf Q\) directly. Treat both omission of infinity and omission of a finite prime. In the latter case include approximation at the real place.

**Exercise 4 (hard).** Prove Proposition 2.4 from an integral basis. Explain exactly where the factor \(2^{r_2}\) enters, and why an arbitrary vector-space identification does not preserve the measure without a normalization check.

## Solutions

**Solution 1.** Write \(q=a/b\) with coprime integers \(a,b\) and \(b>0\). If \(b>1\), some prime \(p\mid b\) has \(\operatorname{ord}_p(q)<0\), so \(q\notin\mathbf Z_p\). Conversely, every integer belongs to every \(\mathbf Z_p\). This proves (7).

For \(a=(a_\infty,(a_p))\), let \(T\) be its nonintegral finite places. Choose \(D=\prod_{p\in T}p^{d_p}\) with \(D a_p\in\mathbf Z_p\) for \(p\in T\). The Chinese remainder theorem gives an integer \(m\) satisfying

\[
m\equiv D a_p\pmod{p^{d_p}}\qquad(p\in T).
\]

Each right side denotes an integral residue class. Then \(q=m/D\) satisfies \(a_p-q\in\mathbf Z_p\) at primes in \(T\). At other primes \(D\) is a unit and both \(a_p,q\) are integral. Thus \(a-q\in\mathbf R\times\widehat{\mathbf Z}\), proving (8). For empty \(T\), take \(D=1,m=0\). A real number only supplies an infinite coordinate; it has no specified images in finite completions. Rational numbers supply the diagonal translation needed here.

**Solution 2.** First \(\mathcal O_{\mathbf Q(i)}=\mathbf Z[i]\). If \(a+bi\), with \(a,b\in\mathbf Q\), is integral, traces of it and its product with \(i\) show \(2a,2b\in\mathbf Z\). Its norm \(a^2+b^2\) is integral. Writing \(2a=m,2b=n\), the condition \(m^2+n^2\equiv0\pmod4\) forces both \(m,n\) even. Hence \(a,b\in\mathbf Z\).

With basis \(1,i\), formula (11) gives

\[
\{x+iy:0\leq x<1,\ 0\leq y<1\}
\times\prod_{v<\infty}\mathcal O_v.
\]

By (10), subtracting a field element makes the finite components integral. Subtracting a Gaussian integer then moves both real coordinates into the stated intervals. Two such representatives differ by a Gaussian integer whose real and imaginary parts lie strictly between \(-1\) and \(1\), so they agree. The complex square has ordinary area \(1\), hence measure \(2\); the finite product has measure \(1\). Its volume is \(2\). Finally,

\[
d_{\mathbf Q(i)}=
\det\begin{pmatrix}
\operatorname{Tr}(1)&\operatorname{Tr}(i)\\
\operatorname{Tr}(i)&\operatorname{Tr}(i^2)
\end{pmatrix}
=\det\begin{pmatrix}2&0\\0&-2\end{pmatrix}=-4.
\]

The volume is \(\sqrt{|-4|}\), as required.

**Solution 3.** Finite local conditions may be written \(q-a_p\in p^{r_p}\mathbf Z_p\), with \(r_p\in\mathbf Z\). Let \(T\) be the finite set of constrained primes, including all nonintegral target components. Choose \(d_p\geq0\) so \(D a_p\in\mathbf Z_p\) and \(d_p+r_p\geq0\), where \(D=\prod_{p\in T}p^{d_p}\).

If the omitted place is infinity, choose

\[
m\equiv D a_p\pmod{p^{d_p+r_p}}\qquad(p\in T)
\]

and put \(q=m/D\). This solves all conditions and gives integrality at every other finite prime.

Now omit a finite prime \(\ell\), so \(\ell\notin T\). For every \(N\geq0\), solve

\[
m\equiv D\ell^N a_p\pmod{p^{d_p+r_p}}\qquad(p\in T).
\]

All solutions form \(m_N+M\mathbf Z\), where \(M=\prod_{p\in T}p^{d_p+r_p}\). The rationals

\[
q=\frac{m_N+Mk}{D\ell^N}\qquad(k\in\mathbf Z)
\]

satisfy the finite conditions. In \(\mathbf R\) they form an arithmetic progression with mesh \(M/(D\ell^N)\), tending to zero. Given \(a_\infty\) and \(\varepsilon>0\), choose \(N\) with mesh less than \(2\varepsilon\), then choose the nearest progression point. Its distance is at most half the mesh, hence less than \(\varepsilon\). Its denominator is supported on \(T\cup\{\ell\}\), so it is integral outside that set. This proves density for every omitted place. For empty \(T\), use \(D=M=1\).

**Solution 4.** The Minkowski lattice theorem gives a parallelepiped for \(j(\mathcal O_K)\) of Euclidean volume \(2^{-r_2}\sqrt{|d_K|}\). To verify the convention, group the embeddings into real embeddings and complex conjugate pairs. Replacing real and imaginary coordinates by a conjugate pair multiplies the determinant's absolute value by \(2\) per pair. Thus the embedding determinant has absolute value \(2^{r_2}\) times the real-coordinate determinant. Its square is the discriminant, giving the stated Euclidean volume.

By (10), the parallelepiped times \(\widehat{\mathcal O}_K\) meets every additive coset exactly once. Counting measure on the diagonal subgroup identifies its measure with the total quotient mass. Each complex measure in (13) is twice ordinary area, so the infinite product measure multiplies Euclidean volume by \(2^{r_2}\). The finite factor has mass \(1\). The result is

\[
2^{r_2}\cdot2^{-r_2}\sqrt{|d_K|}\cdot1=\sqrt{|d_K|}.
\]

An arbitrary \(\mathbf Q\)-basis gives a topological module isomorphism, but its infinite determinant need not have absolute value \(1\), and its finite maps need not preserve the integer lattices. Haar measures transform by these local determinants. A topological isomorphism alone does not preserve their chosen numerical normalization.

## Prerequisites and further directions

We use the following prerequisite results with their stated conventions.

- A number field has an integral basis by Theorem 2.3 of Discriminants and integral bases. Proposition 7.2 of Lattices, Minkowski’s theorem and the Minkowski embedding proves that the Minkowski image of \(\mathcal O_K\) is a full lattice, with Euclidean covolume \(2^{-r_2}\sqrt{|d_K|}\); the canonical complex measure in (13) multiplies this by \(2^{r_2}\). A nonzero integral ideal \(\mathfrak a\) therefore has canonical covolume \(\sqrt{|d_K|}[\mathcal O_K:\mathfrak a]\). The determinant calculation for (14) is given above. [Sutherland 14, Proposition 14.16 and Corollary 14.17] is a scholarly reference.
- Each finite completion is locally compact, its valuation ring is compact open, and that ring is the inverse limit of its quotients by powers of the maximal ideal. These are Theorem 2.1, Propositions 2.2–2.3 and the number-field completion paragraph of Completions, the p-adic numbers and complete discretely valued fields, using the Dedekind and finite-residue facts from Discrete valuation rings and Dedekind domains. Propositions 3.1 and 6.1 of Local fields: classification and Haar measure fix the valuation and measure conventions.
- For finite separable \(L/K\), the canonical map \(L\otimes_K K_v\to\prod_{w\mid v}L_w\) is an isomorphism by Theorem 2.1 of Places of number fields in extensions and the product formula; its Corollary 2.2 proves compatibility with traces and norms. Finite extensions of number fields are separable. [Milne ANT, Proposition 8.2] records the same decomposition.
- With real modulus, squared complex modulus and finite values \(q_v^{-\operatorname{ord}_v}\), the product formula for \(K^\times\) is Theorem 5.2 of Places of number fields in extensions and the product formula, using its Lemma 5.1 for the normalized local norm. Scholarly references are [Milne ANT, Theorem 8.8] and [Getz–Hahn draft, Proposition 2.1.1].
- Unique fractional ideal factorization and local valuation exponents are Theorem 3.2 of Discrete valuation rings and Dedekind domains; its Proposition 3.3 proves Chinese remainders for distinct prime powers and their localization quotients. Theorem 4.3 and Corollary 4.4 of Norms of ideals, the ideal class group, and modules over Dedekind domains give the finite torsion-free module structure used in the relative version of Proposition 2.1. Over a discrete valuation ring its fractional ideal summands are principal, so the localized module is free. The rational approximation application of Chinese remainders is also written in this lesson. [Milne ANT, Proposition 2.29, p.35, and the module discussion in §3, pp.57–58] gives the corresponding finite-module context; the complete programme proof is the one just named.
- Haar existence is Theorem 8.3 of Haar measure on locally compact groups. The restricted-product measure and its integral-tail product formula are Proposition 1.2 of [Restricted products and profinite completions](NT-ADL-01.md). The local normalizations are also stated in [Sutherland 25, p.6] and [Getz–Hahn draft, §3.5, pp.75–76].
- The standard trace characters, their perfect local pairings and self-dual measure are Propositions 5.1–5.2 of Additive characters, self-dual measures and Poisson summation on the adèles, with full archimedean inversion in Lemma 5.4A. Only the normalization comparison after Proposition 2.4 uses this result; no main proof here depends on later Fourier theory.
- The unit different of an unramified finite local extension follows from the explicit bridge after Proposition 2.4: Theorem 2.1 of Unramified and totally ramified extensions supplies the full integral power basis, and Proposition 14.2 of The different and the discriminant supplies its derivative different. Theorem 14.4 of the latter gives the global unramified-prime criterion.

The solenoid's classification and duality, multiplicative idèle class groups, and Poisson summation belong to subsequent lessons. The quotient proved compact here is the additive quotient \(\mathbb A_K/K\).

## References

- **[Sutherland 25]** A. V. Sutherland, *The ring of adeles, strong approximation*, MIT 18.785, Lecture 25 (29 November 2021), [MIT OpenCourseWare notes](https://ocw.mit.edu/courses/18-785-number-theory-i-fall-2021/resources/mit18_785f21_lec25/), Proposition 25.10 and Corollary 25.11, pp.6–7; Theorem 25.12, pp.7–8; Lemma 25.14, p.9; Theorem 25.16 and Corollary 25.17, pp.9–10. These are comparison references for the independently written proofs here.
- **[Milne ANT]** J. S. Milne, *Algebraic Number Theory*, version 3.08 (19 July 2020), [author-hosted notes](https://www.jmilne.org/math/CourseNotes/ANT.pdf), Proposition 8.2 and Corollary 8.4, p.136; Theorem 8.8, p.138; Theorem 4.17 and Theorem 4.19, pp.75–76; Proposition 4.26, pp.79–80.
- **[Bost–Connes 1995]** J.-B. Bost and A. Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Mathematica (N.S.) 1 (1995), 411–457, §3, proof of Proposition 12(2), p.427, for additive density after removal of infinity. [Author-hosted scan](https://alainconnes.org/wp-content/uploads/bostconnesscan.pdf).
- **[Getz–Hahn draft]** J. R. Getz and H. Hahn, *An Introduction to Automorphic Representations: With a View toward Trace Formulae*, [author-hosted draft dated 22 April 2022](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), §2.1, pp.37–42; §3.5, pp.75–76; Appendix B, §§B.1–B.2, pp.485–487. The local character and inversion statements are comparison references, with the proof providers identified above.
- **[Sutherland 14]** A. V. Sutherland, *The geometry of numbers*, MIT 18.785, Lecture 14 (27 October 2021), [lecture notes](https://math.mit.edu/classes/18.785/2021fa/LectureNotes14.pdf), §14.2, Proposition 14.16 and Corollary 14.17: the canonical inner product, its normalized Haar measure, and the covolumes of \(\mathcal O_K\) and its fractional ideals.
- **[Sutherland 12]** A. V. Sutherland, *The different and the discriminant*, MIT 18.785, Lecture 12 (20 October 2021), [lecture notes](https://math.mit.edu/classes/18.785/2021fa/LectureNotes12.pdf), Definition 12.2, Proposition 12.4 and Theorem 12.17.
