# The Herbrand quotient of the idèle class group

*Written by OpenAI GPT-6.1 Sol in Codex, Ultra effort, October 2026. Self-checked by the writing AI; no independent review is claimed. Public domain (CC0).*

A local norm obstruction can be measured at each place, but global elements relate those obstructions. Which part survives after principal idèles are removed? For a cyclic extension of degree \(n\), the answer is a ratio of two finite cohomological defects equal to \(n\). It gives a lower bound for the global norm index before global reciprocity is available.

We begin with a calculation in which all the places and units can be seen. We then identify the exact sequence needed for the general cancellation, prove that finitely many places suffice, and calculate the unit representation. The final applications explain what this information about norms can already say about splitting primes.

The definitions and fixed-class descent are [Idèles in extensions and their cohomology](ideles-in-extensions-and-their-cohomology.md). Herbrand-quotient multiplicativity and lattice comparison are [Cohomology of cyclic groups and the Herbrand quotient](cohomology-of-cyclic-groups-and-the-herbrand-quotient.md). Number-field unit lattices are the written *Dirichlet's unit theorem*, Theorems 9.2 and 9.4 of *Number fields*, and *Idèles and the idèle class group*, Corollary 3.4 of *Adèles and L-functions*. The function-field compactness and unit-lattice arguments are supplied in sections 3–4 below.

Throughout, \(L/K\) is cyclic of degree \(n\), \(G=\operatorname{Gal}(L/K)\), and \(n_v=[L_w:K_v]\) for a choice of \(w\mid v\).


**Prerequisite proof availability.** The named results below identify specific programme lessons. The [prerequisite record](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-CFT/proof-dependencies.html#lesson-14) shows which results are proved in published lessons and which full proofs are still missing. A record or external reference is not a supplied proof; arguments using an unavailable prerequisite retain that dependency.

## 1. A calculation with six constant-field automorphisms

Take \(K=\mathbf F_2(t)\), \(L=\mathbf F_{64}(t)\), and let \(S\) consist of the places defined by
\[
t,\qquad t^2+t+1,\qquad t^3+t+1.
\]
The second polynomial has no root in \(\mathbf F_2\); neither does the cubic, so they are irreducible. Their residue degrees are 1, 2 and 3. In a constant extension of degree six, a place of degree \(d\) has \(\gcd(6,d)\) places above it, each with local degree \(6/\gcd(6,d)\). This follows by factoring the finite-field tensor product, or by the orbits of the sixth iterate of binary Frobenius on its roots. The three decomposition-group orders are therefore 6, 3 and 2.

There are six places of \(L\) above \(S\), all rational over \(\mathbf F_{64}\). Write them as \(t-a_1,\ldots,t-a_6\). An \(S\)-unit has divisor supported there, and the product formula says that its six exponents sum to zero. Conversely every such exponent vector is realized by a product of the ratios \((t-a_j)/(t-a_6)\). Thus, modulo the finite constant units, the unit lattice is exactly the augmentation kernel of the permutation lattice on these six places. The group permutes them in orbits of sizes 1, 2 and 3.

For a cyclic group, a permutation orbit with stabilizer of order \(m\) has Herbrand quotient \(m\). Consequently this permutation lattice has quotient \(6\cdot3\cdot2=36\). Its trivial augmentation target has quotient 6, so its kernel has quotient 6. Finite constant units have quotient 1 even when their order is not prime to six. The \(S\)-idèle quotient is 36 by the local computation of lesson 13. To check that these places suffice, let \(P\) be any monic irreducible polynomial over \(\mathbf F_{64}\). Its function has divisor \([P]-\deg(P)[\infty]\). Subtracting such principal divisors from an arbitrary divisor leaves its degree times \([\infty]\). The divisor of \(t-a_1\) is \([t-a_1]-[\infty]\), so the remaining class can be represented at this place in \(S\). In particular every degree-zero divisor is principal. Applied to the finite valuation support of an idèle, this gives \(J_L=L^\times J_L^S\). Dividing the two quotients gives
\[
h(G,C_L)=36/6=6.
\]
The infinite product of local factors has disappeared from the calculation. The principal elements removed a sum-zero lattice; the one trivial direction they did not remove is responsible for the extension degree.

## 2. The three modules that have to be compared

For finite \(S\), let \(J_L^S\) allow arbitrary components above \(S\) and units elsewhere, and let \(E_{L,S}=L^\times\cap J_L^S\). Once \(S\) is large enough that \(J_L=L^\times J_L^S\), these groups fit into
\[
1\longrightarrow E_{L,S}\longrightarrow J_L^S\longrightarrow C_L\longrightarrow1.
\]
The calculation to be proved is
\[
\begin{array}{c|c|c}
\text{module}&\text{Herbrand quotient}&\text{reason}\\\hline
J_L^S&\prod_{v\in S}n_v&\text{local norms and induced modules}\\
E_{L,S}&n^{-1}\prod_{v\in S}n_v&\text{the sum-zero logarithmic lattice}\\
C_L&n&\text{the exact cyclic hexagon}.
\end{array}
\]
The first line is Proposition 13.4. The second is Proposition 14.2 below. Multiplicativity gives the third only after both groups have finite Tate defects. We therefore need to prove the choice of \(S\), the full-lattice assertion and that finiteness; the table itself is not a substitute for those arguments.

Adding a finite unramified place of local degree \(m\) to a permissible set \(S\) multiplies both numerator and denominator by \(m\). For the idèles this is the newly unrestricted local factor; for the units it is the additional orbit in the permutation representation. The global answer is unchanged. This is a useful check that the result describes \(C_L\), rather than the auxiliary set of places.

## 3. Compactness and a finite set of places

For a global field \(F\), normalize the finite absolute values by
\(|x|_w=q_w^{-v_w(x)}\), and the real and complex ones by ordinary modulus and its square. The product formula makes
\[
|x|=\prod_w|x_w|_w,\qquad
C_F^1=\ker\bigl(|\cdot|:C_F\to\mathbf R_{>0}\bigr)
\tag{1}
\]
well-defined. For number fields \(C_F^1\) is compact by the full box argument in *Adèles and L-functions*, Theorem 3.3. The norm has a continuous section at any archimedean place, so \(C_F=C_F^1\times\mathbf R_{>0}\) after choosing that section.

### The function-field compactness argument

We give the additional support for \(F\) a function field over its full constant field \(k=\mathbf F_q\).

First \(F\) has a separating rational parameter \(t\), so \(F/k(t)\) is finite separable. Here is the elementary characteristic-\(p\) justification. For any rational parameter \(u\), Frobenius and the degree formula give
\([F:F^p]=p\): both \([F:k(u)]\) and \([F^p:k(u)^p]\) are the same, while \([k(u):k(u)^p]=p\). Choose \(t\notin F^p\). Then \(F=F^p(t)\). A finite extension of a one-variable field over a perfect field is inseparable only if it contains the \(p\)th root of that field's rational parameter. To verify this criterion, take its maximal separable subfield \(E\). It too satisfies \([E:E^p]=p\), and \(t\notin E^p\), since a separable extension cannot contain the nontrivial purely inseparable element \(t^{1/p}\). Hence \(E=E^p(t)\) and \(E^{1/p}=E(t^{1/p})\). A nontrivial finite purely inseparable extension of \(E\) contains \(E^{1/p}\): if an element has minimal purely inseparable exponent \(r\geq1\), its \(p^{r-1}\) power generates a degree-\(p\) extension, which is the entire degree-\(p\) field \(E^{1/p}\). This proves the criterion. Since \(t\) is not a \(p\)th power in \(F\), \(F/k(t)\) is separable.

For \(E=k(t)\), partial fractions and the polynomial Chinese remainder theorem give a compact set of additive representatives for \(\mathbb A_E/E\):
\[
D_E=\prod_{P\text{ finite}}\mathcal O_P
       \times t^{-1}k[[t^{-1}]].
\tag{2}
\]
Indeed, finitely many finite principal parts can be removed by a rational function with poles only at those irreducible polynomials \(P\). Subtract a polynomial to remove the nonnegative powers of \(t\) at infinity. The remainder lies in (2). Also \(E\cap D_E=0\): a rational function integral at every finite place is a polynomial, and one vanishing at infinity is zero. Since \(D_E\) is open, \(E\) is discrete; since it is compact and supplies representatives, the quotient is compact.

An \(E\)-basis of \(F\) identifies \(\mathbb A_F\) topologically with \(\mathbb A_E^{[F:E]}\), and \(F\) with \(E^{[F:E]}\). To check the tail topology, take an integral primitive basis and exclude its denominators and discriminant. Outside those finitely many primes it is an integral basis of the local product: the trace-pairing matrix has unit determinant, so the coordinates of any integral element are integral. At the remaining finitely many completions it is a vector-space isomorphism. Thus \(F\) is discrete in \(\mathbb A_F\), and \(\mathbb A_F/F\) is compact.

The function-field product formula also follows from this rational parameter: local determinant norms give
\[
\prod_{w\mid v}|a|_w=|N_{F/E}(a)|_v.
\]
The rational formula is just equality of the degree of a polynomial with the sum of the degrees of its prime factors, including the opposite valuation at infinity. Multiplying the displayed norm formula proves the product formula for \(F\).

Give \(\mathbb A_F\) additive Haar measure and let \(c\) be the finite positive volume of its compact quotient by the discrete subgroup \(F\). For an idèle \(\beta\), the compact open box \(B_\beta=\prod_w\beta_w\mathcal O_w\) has volume \(b|\beta|\), where \(b=\operatorname{vol}(B_1)>0\). If this volume exceeds \(c\), there are two distinct box elements differing by a nonzero element of \(F\). For clarity, integration of \(\sum_{a\in F}\mathbf1_{B_\beta}(x+a)\) over the quotient gives \(\operatorname{vol}(B_\beta)\). If every coset met the box at most once, that integral would be at most \(c\). The integration identity follows by partitioning into local slices on which the discrete quotient is injective. Since the box is an additive subgroup, their difference belongs to the box. Thus
\[
|\beta|>c/b\quad\Longrightarrow\quad
0\ne a\in F,\quad |a|_w\leq|\beta_w|_w\ \text{for every }w.
\tag{3}
\]

The norm-one idèles are closed in \(\mathbb A_F\), and their additive and idèle subspace topologies agree. We include the topology check needed to use (3). For a norm-one idèle, constrain finitely many coordinates to have product absolute value less than 2 and leave integral tails. A new tail nonunit costs a factor at most \(1/2\), so a norm-one element in that additive neighborhood must still have unit tails. This proves equality of the two topologies. To prove closedness, a zero component, or infinitely many tail nonunits, allows a finite coordinate product less than 1, excluding norm one. For an idèle of norm \(d<1\), the same argument works. For norm \(d>1\), include all places with \(q_w\leq2d\) and constrain the finite product to lie between 1 and \(2d\); a tail nonunit then forces the total below 1, and a unit tail leaves it above 1. There are only finitely many such places: each lies over a prime of \(k(t)\) of bounded residue degree, and that rational field has only finitely many irreducible polynomials of bounded degree.

Choose \(\eta\) with \(|\eta|>c/b\). Apply (3) to \(\eta x^{-1}\) for \(x\in J_F^1\). The resulting \(a x\) is still norm one and belongs to the fixed compact box \(B_\eta\). Its intersection with \(J_F^1\) is compact by the topology check. Every norm-one class has a representative there, proving compactness of \(C_F^1\).

### Choosing \(S\)

For either kind of global field, \(C_F/\operatorname{image}(J_F^S)\) is finite when \(S\) is finite, contains infinity, and is nonempty. The image is open. In a number field it has the full norm image because of an archimedean component, so the quotient is an image of compact \(C_F^1\), and is discrete, hence finite. In a function field the norm image is a subgroup of \(q^{\mathbf Z}\); the norm image of \(J_F^S\) contains a nonzero power of \(q\), so it has finite index in the full norm image. Each of finitely many norm cosets is then accounted for by a compact norm-one quotient. Again the discrete quotient is finite.

Take representatives of this finite quotient and enlarge \(S\) to include their nonunit components. The enlarged set satisfies \(J_F=F^\times J_F^S\). Applying this to \(F=K,L\), and taking the finite images of the needed places of \(L\) in \(K\), we can choose a single finite \(S\) containing ramification and infinity with
\[
J_K=K^\times J_K^S,\qquad J_L=L^\times J_L^S.
\tag{4}
\]
For function fields keep \(S\) nonempty. Define
\[
E_{L,S}=L^\times\cap J_L^S
=\{a\in L^\times:v_w(a)=0\text{ for }w\notin S_L\}.
\]
Equation (4) gives the exact sequence of \(G\)-modules
\[
1\longrightarrow E_{L,S}\longrightarrow J_L^S
\longrightarrow C_L\longrightarrow1.
\tag{5}
\]

## 4. The \(S\)-unit representation

The logarithm map
\[
\ell:E_{L,S}\longrightarrow
H=\left\{(x_w)_{w\in S_L}\in\mathbf R^{S_L}:
                         \sum_w x_w=0\right\},
\quad a\longmapsto(\log|a|_w)_w
\tag{6}
\]
has finite kernel \(\mu_L\), and its image is a full lattice in \(H\).

For number fields this is the written \(S\)-logarithmic theorem cited above. In function fields, here is the proof from section 3. The group \(J_L^{S,1}/E_{L,S}\) identifies with the image of \(J_L^{S,1}\) in compact \(C_L^1\). It is an open subgroup, hence closed of finite index and compact. The local valuation map sends \(J_L^{S,1}\) onto the discrete lattice
\[
\Delta=\left\{(-m_w\log q_w)_w:m_w\in\mathbf Z,\
                            \sum_w m_w\log q_w=0\right\}.
\]
Since all \(q_w\) are powers of the full constant-field cardinality, \(\Delta\) spans \(H\). Its kernel is the compact product of all local unit groups. Compactness of the preceding quotient makes \(\Delta/\ell(E_{L,S})\) finite, so the logarithmic image is a full lattice. Its kernel on principal elements is finite, being the intersection of a discrete closed subgroup with that compact product. It consists exactly of the constants \(k_L^\times\), or equivalently the roots of unity: a finite-order element is algebraic over the finite constant field, and every nonzero constant is a unit everywhere. This proves (6) with all its assertions in this case, too.

The action on logarithms is a permutation:
\[
\ell(g a)_w=\ell(a)_{g^{-1}w}.
\tag{7}
\]
There is no extra residue-degree factor: the normalized absolute value is transported by the isomorphism \(L_{g^{-1}w}\to L_w\).

### Proposition 14.2. The \(S\)-unit quotient

For cyclic \(L/K\),
\[
h(G,E_{L,S})=\frac1n\prod_{v\in S}n_v.
\tag{8}
\]

**Proof.** Finite torsion has Herbrand quotient 1, so we may replace \(E_{L,S}\) by its logarithmic lattice \(\Lambda\) in \(H\). Adjoin the trivial lattice \(\mathbf Z e\), \(e=(1,\ldots,1)\), to form \(\Lambda\oplus\mathbf Z e\). Its real representation is the full permutation space \(\mathbf R^{S_L}\). The lattice comparison theorem in lesson 2 therefore gives the same Herbrand quotient as the permutation lattice
\[
P=\mathbf Z^{S_L}
=\bigoplus_{v\in S}\mathbf Z[G/G_w].
\]
That comparison does not require the two lattices to have rational coordinates in a common real embedding. Their integral representations are real-isomorphic; the rational commuting-map equations consequently have a real solution with nonzero determinant. The determinant is a nonzero polynomial on that rational solution space, so it has a rational nonzero value. Clearing denominators gives an equivariant injection with finite cokernel, exactly the argument proved in lesson 2.

The explicit induced cyclic calculation in lesson 13 gives
\(h(G,\mathbf Z[G/G_w])=h(G_w,\mathbf Z)=|G_w|=n_v\).
The trivial lattice \(\mathbf Z e\) has quotient \(n\). Multiplicativity now gives
\[
n\,h(G,E_{L,S})=h(G,\Lambda\oplus\mathbf Z e)
              =h(G,P)=\prod_{v\in S}n_v,
\]
proving (8). ∎

## 5. The quotient of the idèle class group

### Theorem 14.1. The degree survives

For every cyclic extension \(L/K\) of global fields,
\[
h(G,C_L)=n.
\tag{9}
\]
Both Tate groups defining this quotient are finite.

**Proof.** Choose \(S\) as in (4). Proposition 13.4 gives
\(h(G,J_L^S)=\prod_{v\in S}n_v\); Proposition 14.2 gives (8), with finite Tate groups. Apply the full exact cyclic hexagon and its quotient multiplicativity to (5). This gives finiteness for the third module, and
\[
h(G,C_L)=\frac{h(G,J_L^S)}{h(G,E_{L,S})}
        =\frac{\prod_{v\in S}n_v}{(\prod_{v\in S}n_v)/n}=n.
\]
No Herbrand quotient of the unrestricted idèle group is used. ∎

### Corollary 14.3. The norm index is at least the degree

For cyclic \(L/K\),
\[
[C_K:N_{L/K}C_L]
=n\,|\widehat H^{-1}(G,C_L)|\geq n.
\tag{10}
\]

**Proof.** Proposition 13.2 identifies \(C_L^G=C_K\), and the module norm is the idèle-class norm. Thus degree zero is \(C_K/N C_L\). Equation (9) says that the size of this finite group is \(n\) times the size of degree minus one. ∎

The later norm inequality will show equality and kill the remaining Tate group. Equation (10) alone makes no such assertion.

## 6. Primes cannot all split

We use the fully proved weak approximation theorem of *Local fields*, *Absolute values, valuations and Ostrowski's theorem*, Theorem 5.2. Its hypothesis is a finite list of pairwise inequivalent nontrivial absolute values on any field; it therefore applies to both global-field cases here. Density of the field in its individual completions turns its original field-valued targets into arbitrary completion-valued targets.

**Lemma.** A nontrivial cyclic extension \(L/K\) has infinitely many finite places that do not split completely.

**Proof.** Suppose only finitely many finite places fail to split, and include these and infinity in a finite set \(T\). Given \(x\in J_K\), each local norm image at a place of \(T\) is open. Weak approximation chooses \(a\in K^\times\) close enough to \(x_v\) that \(x_v/a\) is a local norm for every \(v\in T\). Choose the neighborhoods to exclude zero. Outside \(T\), complete splitting makes the local norm surjective. Proposition 13.3 then says \(x/a\in N J_L\). Thus every idèle class is a norm, giving \([C_K:N C_L]=1\), contrary to (10) and \(n>1\). ∎

There is a stronger conclusion for cyclic extensions of prime-power degree: infinitely many finite places are **inert**, meaning they are unramified and have just one place above them. To prove it, let \(G\) have order \(\ell^r>1\) and let \(H\) be its unique subgroup of index \(\ell\). Every proper subgroup is contained in \(H\). If only finitely many places were inert, every other unramified place would have proper decomposition group and would therefore split completely in the degree-\(\ell\) field \(L^H/K\). This contradicts the preceding lemma for that field.

Inertness and failure of complete splitting are different conditions. For a noncyclic Galois extension, an unramified decomposition group is cyclic, so it cannot equal the whole group. There are consequently no inert unramified places, although Corollary 14.4 below gives infinitely many places that fail to split completely. Only the finitely many ramified places can remain a single place for another reason.

### Corollary 14.4. Complete splitting detects the field

If almost all finite places of \(K\) split completely in a finite separable extension \(M/K\), then \(M=K\).

**Proof.** Let \(L\) be its Galois closure. At a completely split place of \(M/K\), its primitive-element polynomial splits into linear factors over \(K_v\), by the local decomposition (2) of lesson 13. Its splitting field therefore embeds in \(K_v\). Since \(L/K\) is Galois, all the completions of \(L\) above \(v\) have degree one. Thus almost all places of \(K\) split completely in \(L\).

If \(L\ne K\), its finite group contains an element of prime order: take any nonidentity element of order \(m\), a prime \(\ell\mid m\), and its \(m/\ell\) power. Let \(K'\) be the fixed field of that order-\(\ell\) subgroup. Then \(L/K'\) is a nontrivial cyclic extension. Every place of \(K'\) above a completely split place of \(L/K\) is completely split in \(L/K'\); only finitely many places of \(K'\) lie above the exceptional finite set. This contradicts the lemma. Hence \(L=K\) and \(M=K\). ∎

Taking the contrapositive gives infinitely many nonsplit primes in every nontrivial finite separable extension. The proof uses a cyclic extension over an intermediate base field, so it also works when the original Galois group has no nontrivial cyclic quotient.

**Separating cyclic extensions.** Let \(L_1,\ldots,L_r\) be cyclic extensions of the same prime degree \(\ell\), and put \(M=L_2\cdots L_r\). If \(L_1\not\subset M\), there are infinitely many finite primes of \(K\) that split completely in \(M\) and are inert in \(L_1\).

**Proof.** Put \(E=L_1M\). The hypothesis makes \(E/M\) cyclic of degree \(\ell\). It has infinitely many inert primes by the prime-power conclusion above. Exclude those over the finitely many primes ramified in \(E/K\). At a remaining prime \(v\) of \(K\), the decomposition group \(D\) in \(\operatorname{Gal}(E/K)\) is cyclic. This Galois group embeds in a product of groups of order \(\ell\), so every nonidentity element has order \(\ell\); hence \(|D|\leq\ell\). If its image in \(\operatorname{Gal}(M/K)\) were nontrivial, \(D\cap\operatorname{Gal}(E/M)\) would be trivial, contradicting the selected prime's inertness in \(E/M\). Thus \(D\) maps trivially to the group of \(M/K\), which makes \(v\) completely split in \(M\), and \(D=\operatorname{Gal}(E/M)\) maps nontrivially to \(\operatorname{Gal}(L_1/K)\), making \(v\) inert in \(L_1\). Infinitely many primes of \(M\) lie over infinitely many primes of \(K\), since every fiber is finite. ∎

Pairwise intersections \(L_i\cap L_j=K\) do not imply the hypothesis just used. For example, \(\mathbf Q(\sqrt6)\), \(\mathbf Q(\sqrt2)\), and \(\mathbf Q(\sqrt3)\) have pairwise intersection \(\mathbf Q\), but the first is contained in the compositum of the latter two. Away from ramification, splitting in both latter fields forces splitting in the first. The required condition is independence of the first field from the **whole** compositum.

## 7. Returning to a number-field example

For \(L=\mathbf Q(i)\), \(K=\mathbf Q\), take \(S=\{2,\infty\}\). The Gaussian integers are Euclidean, as proved in *Idèles and the idèle class group*, so all their ideal classes are trivial and this \(S\) satisfies (4). Both local degrees are 2. Thus
\[
h(G,J_L^S)=4,\qquad h(G,E_{L,S})=2,\qquad h(G,C_L)=2.
\tag{11}
\]
Concretely \(E_{L,S}=\mu_4(1+i)^{\mathbf Z}\). To verify this description, an \(S\)-unit's Gaussian fractional ideal is supported only on \(1+i\); dividing by the corresponding power leaves a Gaussian unit, which is in \(\mu_4\). Conjugation sends \(1+i\) to \(1-i=-i(1+i)\), so it acts trivially on the infinite cyclic quotient by torsion. That quotient has Herbrand quotient 2. The explicit computation in lesson 13 gives \([C_{\mathbf Q}:N C_{\mathbf Q(i)}]=2\), consistent with (10), and in this example \(\widehat H^{-1}(G,C_L)=0\).

## 8. Exercises with solutions

### Exercise 1. Permutation and augmentation lattices — easy

Let \(G=C_6\) act on three orbits with stabilizers of orders 6, 3 and 2. Compute the Herbrand quotient of their permutation lattice and its augmentation kernel. Then give the formula for one orbit \(G/H\) in a cyclic group of order \(n\), and for the augmentation kernel of the regular lattice.

**Solution.** The three-orbit permutation quotient is \(6\cdot3\cdot2=36\). Its augmentation is onto a trivial integer lattice of quotient 6, so the kernel has quotient 6, exactly the unit calculation in section 1. In general an orbit lattice is induced from the trivial \(H\)-module \(\mathbf Z\). Its invariant norm quotient has order \(|H|\), and its degree-minus-one group is zero, by the twisted-cycle calculation, so the quotient is \(|H|\). For the regular lattice \(h=1\). The augmentation is surjective, and its target is a trivial lattice of quotient \(n\). Multiplicativity gives \(h\) of the augmentation kernel equal to \(1/n\), including \(n=1\), when the kernel is zero.

### Exercise 2. Quadratic fields directly — medium

For quadratic \(L/\mathbf Q\), prove (8) directly from the plus and minus eigenspaces of conjugation.

**Solution.** Let \(s\) places in \(S\) split and \(t\) not split. A split place contributes a swapped pair of coordinates to \(\mathbf R^{S_L}\); a nonsplit place contributes one fixed coordinate. The plus eigenspace has dimension \(s+t\), and the minus eigenspace dimension \(s\). Removing the trivial sum line gives dimensions \(a=s+t-1\) and \(b=s\) for the unit representation. By integral lattice comparison, its quotient equals that of \(a\) trivial lattices and \(b\) sign lattices. A trivial rank-one lattice for a group of order 2 has quotient 2; a sign lattice has invariants zero, norm zero and \((\sigma-1)\mathbf Z=2\mathbf Z\), hence quotient \(1/2\). Finite torsion contributes 1. Consequently \(h(E_{L,S})=2^{a-b}=2^{t-1}\). Exactly the \(t\) nonsplit local degrees are 2, so this is \((\prod n_v)/2\). This includes both real and imaginary quadratic fields.

### Exercise 3. Arbitrary extensions — medium

Deduce Corollary 14.4 from the norm inequality without assuming the Galois group has a cyclic quotient.

**Solution.** Complete splitting in \(M\) makes its defining separable polynomial split over the completion, hence makes its Galois closure \(L\) split there too. If \(L\ne K\), choose a prime-order subgroup of \(\operatorname{Gal}(L/K)\), with fixed field \(K'\). Almost all places of \(K'\) split in the nontrivial cyclic extension \(L/K'\). Weak approximation at the finitely many exceptional places then makes every \(K'\)-idèle class a norm: local norm groups are open there, and all other local norms are surjective. This gives norm index 1, violating (10) for that cyclic extension. Therefore \(L=K\).

### Exercise 4. The general unit calculation — hard

Show why enlarging a permissible set of places cannot change the quotient in Theorem 14.1. Your argument should prove (8) and explain why a real logarithmic lattice suffices for integral cohomology.

**Solution.** Remove the finite torsion of \(E_{L,S}\); its quotient is the full logarithmic lattice \(\Lambda\) in the sum-zero hyperplane. Adjoin a trivial rank-one lattice. The resulting real representation is the permutation representation on \(S_L\). To compare integral lattices, solve the intertwining matrix equations over \(\mathbf Q\). A real isomorphism gives a point where the determinant polynomial is nonzero; a nonzero polynomial over \(\mathbf Q\) cannot vanish at every rational point, as follows by induction on its number of variables. A rational invertible intertwiner therefore exists. Clearing denominators embeds one lattice in the other with finite cokernel, which has quotient 1. Thus the Herbrand quotients agree. Decompose the permutation lattice into \(\mathbf Z[G/G_w]\), one for each \(v\in S\). Their quotients are \(|G_w|=n_v\) by Exercise 1. The adjoined trivial line has quotient \(n\); divide by it to obtain (8). Adding a place of local degree \(m\) inserts its permutation orbit, so (8) multiplies the unit quotient by \(m\). Proposition 13.4 multiplies the idèle quotient by the same factor. Their ratio, and hence \(h(G,C_L)\), remains \(n\).

## Editable edition

The reading edition provides the complete LaTeX source of this lesson, the cumulative course LaTeX and the editable source ZIP. The archive contains all twenty-four Markdown lessons, complete LaTeX bodies, original diagrams, metadata and reproduction instructions.

## References

The local induced-module quotients and the proved S-unit representation give the idèle-class Herbrand quotient. The function-field compactness and lattice argument and the constant-field example are written separately with their full hypotheses.

- [Jürgen Neukirch, Class Field Theory — The Bonn Lectures, Online Edition 2.0 (May 2015), edited by Alexander Schmidt](https://www.mathi.uni-heidelberg.de/~schmidt/Neukirch-en/Neukirch_cft_02_may15.pdf).
- [J. S. Milne, Class Field Theory, version 4.03](https://www.jmilne.org/math/CourseNotes/CFT.pdf).
- [Kiran S. Kedlaya, Notes on class field theory, author-hosted HTML edition](https://kskedlaya.org/cft/sec_abstractcft1.html).

The [proof guide](../FREE_PROOFS.md) gives the lesson sequence and the exact prerequisite record. External references accompany the written arguments.
