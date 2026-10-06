# p-adic Hodge theory and the Fontaine–Mazur conjecture

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

At a prime different from the coefficient characteristic, finite inertia and a nilpotent monodromy operator describe the local representation. At the coefficient prime, a second kind of information appears: a filtration recording Hodge–Tate weights. Period rings make this information accessible from the Galois action.

Throughout, \(p\) is the coefficient prime. We use the **positive convention**: \(\mathbf Q_p(1)\), with action \(\chi_p\), has Hodge–Tate weight \(+1\). Thus the covariant Tate module of an elliptic curve has weights \(0,1\), and the representations attached to weight-\(k\) newforms have weights \(0,k-1\). The convention is explained in [Berger's free author manuscript, §II.1.2](https://perso.ens-lyon.fr/laurent.berger/articles/article05.pdf). The decreasing de Rham filtration has jumps at the **negatives** of these weights.

The course uses arithmetic Frobenius at good primes away from \(p\); local reciprocity sends a uniformizer to geometric Frobenius, and the Weil–Deligne relation is \(r(w)Nr(w)^{-1}=|w|N\). The Frobenius \(\varphi\) on a crystalline period module is a different operator: for \(\mathbf Q_p(1)\) it acts by \(p^{-1}\). It corresponds to the geometric normalization. We will calculate it rather than identifying it with arithmetic Frobenius.

We retain the full higher-weight, weight-one, comparison and modularity assertions. Their proof status matters: the preceding higher-weight construction still has unresolved arithmetic-model and comparison inputs, and no earlier lesson supplies the general \(p\)-adic comparison theorems. Below we construct the tilt, Witt vectors, \(\theta\), and the de Rham discrete valuation ring; prove the admissibility algebra; construct unramified period matrices; and calculate the Tate logarithm from divided powers. The deep estimates and comparisons still needed to make every assertion unconditional are identified before use and collected in §6. A freely accessible theorem statement does not close any of those obligations.

## 1. Weights and the period rings

The elementary field and module prerequisites are actual earlier proofs: *Profinite groups and ℓ-adic representations*, §§0A–0F, proves lattice freeness, finite and infinite Galois theory, primitive elements, finite-extension valuations, Hensel lifting, finite fields and the unramified Frobenius quotient. We use these specific proofs, including the arithmetic normalization on the residue field. The additional wild/tame structure of the monodromy lesson is not needed for the coefficient-prime logarithms below.

Write \(C_p=\widehat{\overline{\mathbf Q}_p}\). The semilinear representation \(C_p(h)\) is the one-dimensional \(C_p\)-space on which
\[
g(ae_h)=g(a)\chi_p(g)^h e_h.
\tag{1}
\]
A representation \(V\) of \(G_K\), for a finite extension \(K/\mathbf Q_p\), is **Hodge–Tate** if there is a semilinear equivariant isomorphism
\[
C_p\otimes_{\mathbf Q_p}V
\simeq\bigoplus_{h\in\mathbf Z}C_p(h)^{m_h},
\qquad \sum_hm_h=\dim_{\mathbf Q_p}V.
\tag{2}
\]
Its weights are the integers \(h\), with multiplicities \(m_h\).

**Tate's invariant theorem (full assertion, proof unclosed).** For every finite \(L/\mathbf Q_p\),
\[
C_p^{G_L}=L,\qquad C_p(h)^{G_L}=0\quad(h\ne0).
\tag{3}
\]
The free accounts [Berger, §§II.1.1–II.1.2](https://perso.ens-lyon.fr/laurent.berger/articles/article05.pdf) and [Brinon–Conrad, Theorem 2.2.7](https://math.stanford.edu/~conrad/papers/notes.pdf) state this result. Its ramification estimates are an **unclosed proof obligation here**. Conditional on (3), nonzero equivariant \(C_p\)-linear maps between \(C_p(h)\) and \(C_p(j)\) exist only when \(h=j\): their coefficient would be a fixed vector in \(C_p(j-h)\). Applying \(\operatorname{Hom}_{C_p[G_K]}(C_p(h),-)\) to (2) shows that \(m_h\) is uniquely determined. Thus (2) defines weights, rather than just a possible list, once (3) has been established.

We begin with constructions whose algebra can be given in full. Form
\[
R=\varprojlim_{x\mapsto x^p}\mathcal O_{C_p}/p,\qquad A_{\inf}=W(R).
\tag{4}
\]
**Lemma 1.0 (completion and the tilt).** The field \(C_p\) is algebraically closed. The ring \(R\) in (4) is a perfect, complete valuation domain of characteristic \(p\), with algebraically closed fraction field and value group \(\mathbf Q\). Every \(x=(x_n)\in R\) has a unique lift to an exact root system \((x^{(n)})\) in \(\mathcal O_{C_p}\), with \((x^{(n+1)})^p=x^{(n)}\). Its valuation is \(v_R(x)=v_p(x^{(0)})\), and its residue field is \(\overline{\mathbf F}_p\).

*Proof.* First let \(f\) be a monic polynomial with coefficients in \(C_p\). After replacing its variable by a sufficiently large scalar multiple, its coefficients are integral. Approximate them by integral algebraic coefficients to obtain monic \(f_n\) with coefficient errors of valuation tending to infinity. Each \(f_n\) splits over \(\overline{\mathbf Q}_p\), and all its roots are integral: a root of negative valuation would make the leading term uniquely smallest in valuation. Given a root \(a_n\) of \(f_n\), factor \(f_{n+1}(a_n)=\prod_j(a_n-b_j)\). The coefficient approximation makes the valuation of this product tend to infinity; one factor has at least that valuation divided by \(\deg f\). Choose that \(b_j\) as \(a_{n+1}\). The resulting sequence is Cauchy, and its limit is a root of \(f\). Repeating after division by a linear factor proves algebraic closedness. In particular every integral element has an integral \(p\)-th root.

The inverse of Frobenius on \(R\) is the shift \((x_0,x_1,\ldots)\mapsto(x_1,x_2,\ldots)\). Choose arbitrary integral lifts \(\widehat x_n\). The binomial theorem gives
\[
a\equiv b\pmod p\quad\Longrightarrow\quad
a^{p^j}\equiv b^{p^j}\pmod {p^{j+1}}.
\]
Indeed one application of the \(p\)-th power raises the congruence exponent by at least one; induction proves the formula. Therefore
\[
x^{(n)}=\lim_{j\to\infty}\widehat x_{n+j}^{p^j}
\]
exists, is independent of the lifts, and reduces to \(x_n\). It has the asserted power compatibility. Conversely an exact root system is recovered by this formula, proving uniqueness. Multiplication of exact systems is coordinatewise, while addition satisfies
\[
(x+y)^{(n)}=\lim_{j\to\infty}
 (x^{(n+j)}+y^{(n+j)})^{p^j}.
\]
If \(x^{(0)}=0\), every coordinate is zero. If \(v_R(x)\ge v_R(y)\) and \(y\ne0\), the quotients \(x^{(n)}/y^{(n)}\) are integral and power compatible. They define \(z\in R\) with \(x=yz\). Thus \(R\) is a valuation domain; the displayed addition formula gives its ultrametric inequality. The kernel of the projection \(R\to\mathcal O_{C_p}/p\), \(x\mapsto x_n\), is exactly \(\{v_R(x)\ge p^n\}\). The valuation topology is consequently the inverse-limit topology of discrete coordinates. A coordinatewise limit of a Cauchy sequence remains power compatible, which proves completeness.

Reduction of an integral element of \(C_p\) is already the reduction of an algebraic approximant. Hence its residue field is \(\overline{\mathbf F}_p\). Each residue element has a canonical lift into \(\mathcal O_{C_p}/p\): choose an algebraic representative and lift it to a root of \(T^{p^r}-T\), whose derivative is a unit. Modulo \(p\), these roots are closed under addition and multiplication. Uniqueness with a prescribed residue follows because a difference \(d\) of two such roots satisfies \(d^{p^r}=d\) in characteristic \(p\); a nonzero difference of positive valuation less than one cannot satisfy that equation. The elementary Newton iteration \(a\mapsto a-f(a)/f'(a)\) doubles the error valuation when \(f'(a)\) is a unit, so this lifting uses a proved convergence argument. These lifts and their compatible inverse Frobenius images define \(\overline{\mathbf F}_p\subset R\); their reductions exhaust the residue field. A nonzero limit in \(C_p\) has the valuation of a sufficiently close algebraic approximant, so its valuation is rational. Compatible roots of \(p^{a/b}\) realize every nonnegative rational value in \(R\), proving the value-group assertion.

To prove algebraic closedness of \(\operatorname{Frac}(R)\), scale a monic polynomial to make all its coefficients integral. It suffices to solve a monic \(f\in R[T]\) of degree \(d\ge2\). Project its coefficients to coordinate \(n\), lift to \(\mathcal O_{C_p}\), and factor the lifted polynomial there, with roots \(\rho_{i,n}\), \(1\le i\le d\). Its evaluation at \(\rho_{i,n+1}^p\) is divisible by \(p\), since modulo \(p\) Frobenius carries the polynomial of coordinate \(n+1\) to that of coordinate \(n\). Factoring that evaluation shows that for some \(j\),
\(v_p(\rho_{i,n+1}^p-\rho_{j,n})\ge1/d\). If a difference has valuation at least \(r/d\), \(1\le r<d\), its \(p\)-th-power difference has valuation at least \((r+1)/d\), by the binomial theorem. After \(d-1\) steps we get
\[
\rho_{i,n+1}^{p^d}\equiv\rho_{j,n}^{p^{d-1}}\pmod p.
\]
The nonempty finite sets \(U_m=\{\rho_{i,m+d-1}^{p^{d-1}}\bmod p:1\le i\le d\}\) consequently form an inverse system under the \(p\)-th-power maps; their elements are roots of the coordinate-\(m\) polynomial. There is a compatible sequence: in a finite first set choose an element with arbitrarily long lifts, then do the same at each following level. The resulting element of \(R\) is a root of \(f\), as every coordinate of \(f(x)\) vanishes. Scaling back proves the fraction-field assertion. ∎

**Lemma 1.1 (the Witt algebra used here).** For a perfect \(\mathbf F_p\)-algebra \(A\), the set \(A^{\mathbf N}\) has a functorial ring structure \(W(A)\). It is complete and separated for powers of \(p\), multiplication by \(p\) is injective, and every element has a unique expansion \(\sum_{n\ge0}p^n[a_n]\), where \([a]=(a,0,\ldots)\) is multiplicative. Its Frobenius is \([a]\mapsto[a^p]\).

*Proof.* Introduce the ghost polynomials
\[
w_n(X)=X_0^{p^n}+pX_1^{p^{n-1}}+\cdots+p^nX_n.
\]
Define the addition and multiplication coordinates recursively by requiring their ghosts to be \(w_n(X)+w_n(Y)\) and \(w_n(X)w_n(Y)\). The coordinate of index \(n\) is the difference between this prescribed ghost and the terms already found, divided by \(p^n\). We check that this division produces an integer polynomial. In the polynomial ring over \(\mathbf Z\), let \(F\) raise every variable to its \(p\)-th power. The prescribed ghost \(g_n\) satisfies \(g_n\equiv F(g_{n-1})\pmod {p^n}\). Also \(F(z)\equiv z^p\pmod p\) for every integer polynomial \(z\). If \(a\equiv b\pmod {p^r}\), the binomial theorem gives \(a^p\equiv b^p\pmod {p^{r+1}}\) for \(r\ge1\). Apply this \(n-1-i\) times to \(F(z_i)\) and \(z_i^p\); after multiplication by \(p^i\), their contributions differ by a multiple of \(p^n\). The recursion is integral by induction.

Over an integer polynomial ring the ghost map is injective, since its triangular coefficients are \(1,p,p^2,\ldots\), all nonzero divisors. All ring identities can therefore be checked on ghosts there. They are integer polynomial identities, so they specialize to every \(A\). The same recursion gives \([ab]=[a][b]\), and, in characteristic \(p\),
\[
p(a_0,a_1,\ldots)=(0,a_0^p,a_1^p,\ldots).
\]
To justify this identity, work before specialization in \(\mathbf Z[X_0,X_1,\ldots]\). Let \(Y\) be the Witt coordinates of \(pX\), so \(w_n(Y)=p w_n(X)\), and set \(C=(0,X_0^p,X_1^p,\ldots)\). Direct substitution gives
\[
 w_n(C)=p w_n(X)-p^{n+1}X_n.
\]
We prove \(Y_n-C_n\in p\mathbf Z[X_0,X_1,\ldots]\) inductively. The assertion for index zero is \(Y_0=pX_0\). For \(i<n\), the induction hypothesis and the binomial congruence in the preceding paragraph make \(Y_i^{p^{n-i}}-C_i^{p^{n-i}}\) divisible by \(p^{n-i+1}\); multiplying by \(p^i\) makes that contribution divisible by \(p^{n+1}\). Comparing the index-\(n\) ghosts thus makes \(p^n(Y_n-C_n)\) divisible by \(p^{n+1}\). The integer polynomial ring has no \(p\)-torsion, so \(Y_n-C_n\) is divisible by \(p\). Specialization to characteristic \(p\) proves the displayed identity without using injectivity of characteristic-\(p\) ghosts. Perfectness now identifies \(p^rW(A)\) with the vectors whose first \(r\) coordinates are zero and proves injectivity of multiplication by \(p\). Completeness is precisely completeness of sequences of coordinates. Remove the first coordinate as \([a_0]\), divide the remainder by \(p\), and repeat; this gives the unique expansion. Coordinatewise Frobenius is a ring automorphism by functoriality and perfectness. The integer map into \(W(\mathbf F_p)\) extends to \(\mathbf Z_p\) by completeness. It is injective since multiplication by \(p\) is injective, and surjective by lifting its residue and dividing the successive remainders by \(p\). Thus \(W(\mathbf F_p)=\mathbf Z_p\); its inclusion in \(W(R)\) supplies \(\mathbf Q_p\) after inverting \(p\). ∎

**Lemma 1.2 (\(\theta\), its kernel, and the de Rham valuation ring).** There is a surjective equivariant ring homomorphism
\[
\theta\left(\sum_{n\ge0}p^n[a_n]\right)
   =\sum_{n\ge0}p^n a_n^{(0)}.
\tag{4a}
\]
Choose \(\widetilde p\in R\) with \(\widetilde p^{(0)}=p\). Then \(\ker\theta=(\xi)\), where \(\xi=[\widetilde p]-p\). The \(\xi\)-adic completion of \(W(R)[1/p]\) is a complete discrete valuation ring \(B_{\mathrm{dR}}^+\) with residue field \(C_p\). It contains the original ring and a canonical equivariant copy of \(\overline{\mathbf Q}_p\).

*Proof.* In Witt coordinates \((r_0,r_1,\ldots)\), formula (4a) is \(\sum_i p^i r_i^{(i)}\). Modulo \(p^N\), this equals
\[
\sum_{i=0}^{N-1}p^i(r_i^{(N)})^{p^{N-i}}.
\]
It is the ghost polynomial of index \(N\), with its last term omitted because that term is divisible by \(p^N\). This ghost expression only depends on each \(r_i^{(N)}\) modulo \(p\): replacing a lift by a congruent lift changes its \(p^{N-i}\)-th power by a multiple of \(p^{N-i+1}\). Projection \(R\to\mathcal O_{C_p}/p\) at coordinate \(N\) is a ring map; functoriality of the Witt operations and the ghost addition identity prove additivity of \(\theta\) modulo \(p^N\). This holds for every \(N\). Multiplicativity then follows from additivity, convergent digit expansions, and \(\theta([a][b])=(ab)^{(0)}=a^{(0)}b^{(0)}\). Compatible roots of any integral \(z\) give \(\theta([\widetilde z])=z\), proving surjectivity. The construction is equivariant at every stage.

If \(a\in\ker\theta\), its first digit \(a_0\) has valuation at least one, since \(a_0^{(0)}\in p\mathcal O_{C_p}\). As \(v_R(\widetilde p)=1\), write \(a_0=\widetilde p b_0\). Then \(a-\xi[b_0]\) is divisible by \(p\); its quotient again belongs to \(\ker\theta\), because \(\mathcal O_{C_p}\) has no \(p\)-torsion. Repetition gives \(a=\xi\sum p^i[b_i]\). Thus the kernel is principal. The Witt ring is a domain: the product of two nonzero elements, after removing their first nonzero powers of \(p\), has a nonzero product of first digits in the domain \(R\).

The same absence of \(p\)-torsion proves by induction
\[
W(R)\cap\xi^jW(R)[1/p]=\xi^jW(R).
\]
An element in every \(\xi^jW(R)\) has first digit divisible by every \(\widetilde p^j\), hence zero. It is divisible by \(p\), and its quotient has the same property by the intersection identity. Repetition and \(p\)-adic separatedness make it zero. Consequently \(W(R)[1/p]\) embeds into its \(\xi\)-adic completion.

In each quotient modulo \(\xi^j\), an element with nonzero residue is a unit: lift a residue inverse and use the finite geometric series to correct the product. An element with zero residue is uniquely divisible by \(\xi\) modulo \(\xi^{j-1}\), because \(\xi\) is not a zero divisor. Compatible quotients show that the completed ring has maximal ideal generated by \(\xi\), with \(\xi\) still a nonzero divisor. Its powers have zero intersection and its residue is \(C_p\). Every nonzero element is a power of \(\xi\) times a unit, proving the discrete valuation assertion.

Finally any algebraic \(a\in C_p\) has a separable minimal polynomial over \(\mathbf Q_p\). Lift its residue root by Newton iteration in the complete \(\xi\)-adic ring; its derivative has nonzero residue and is a unit. The iteration doubles the \(\xi\)-adic error, and its root with prescribed residue is unique. For addition and multiplication, place the finitely many algebraic elements in a common finite extension \(F/\mathbf Q_p\). The primitive-element proof at the start of lesson 1, Proposition 0E.1, gives \(F=\mathbf Q_p[\beta]\). Lift \(\beta\) by the Newton procedure just described. Evaluation at that lift defines a homomorphism \(\mathbf Q_p[T]/(f_\beta)\to B_{\mathrm{dR}}^+\): the minimal polynomial vanishes there, and the map from this field is injective because it sends one to one. Every element of \(F\) is a polynomial in \(\beta\). Its polynomial value is a root of its own minimal polynomial with the prescribed residue, so uniqueness identifies it with its individual Newton lift. This proves compatibility with addition, multiplication and field inclusions. Applying any Galois element preserves the minimal polynomial and changes the prescribed residue accordingly, so uniqueness proves equivariance. They give the asserted canonical algebraic constants. ∎

Choose \(\epsilon=(1,\zeta_p,\zeta_{p^2},\ldots)\) as an exact root system. The logarithm in the following display converges for the maximal-ideal topology:
\[
t=\log([\epsilon]),\quad g(t)=\chi_p(g)t,\quad
B_{\mathrm{dR}}=B_{\mathrm{dR}}^+[1/t],\quad
\operatorname{Fil}^iB_{\mathrm{dR}}=t^iB_{\mathrm{dR}}^+.
\tag{5}
\]
Here is the remaining distinction between a proved construction and a period-ring structural theorem.

**Lemma 1.2A (the uniformizer and divided-power logarithms).** The element \(t=\log[\epsilon]\) is a uniformizer of \(B_{\mathrm{dR}}^+\). Set
\[
A_0=W(R)[\xi^n/n!:n\ge1],\qquad
A_{\mathrm{cris}}=\varprojlim_r A_0/p^rA_0.
\tag{5a}
\]
In this abstract completion, the logarithm of \([x]\) exists after inverting \(p\) whenever \(x\in1+\mathfrak m_R\). It is additive on products, equivariant, and satisfies \(\varphi(\log[x])=p\log[x]\). These identities include \(g(t)=\chi_p(g)t\) once the natural map from this completion to \(B_{\mathrm{dR}}^+\) has been established. The existence and injectivity of that natural map remain a structural obligation; they are not inferred from the definition (5a).

*Proof.* Put \(\epsilon_1=\epsilon^{1/p}\). The element
\[
\omega=1+[\epsilon_1]+\cdots+[\epsilon_1]^{p-1}
\]
is killed by \(\theta\), since its residue is \(\sum_{i=0}^{p-1}\zeta_p^i=0\). Modulo \(p\) it is \((\epsilon_1-1)^{p-1}\). To compute its valuation, observe that \(\Phi_{p^n}(1+T)\) has degree \(p^{n-1}(p-1)\), constant coefficient \(p\), and all intermediate coefficients divisible by \(p\): its reduction is that power of \(T\). A primitive \(p^n\)-th root reduces to one, so \(v_p(\zeta_{p^n}-1)>0\). In its polynomial equation the intermediate terms have valuation greater than one; the constant and leading terms must therefore have equal valuation. This gives
\(v_p(\zeta_{p^n}-1)=1/(p^{n-1}(p-1))\). Taking the exact-system limit gives \(v_R(\epsilon_1-1)=1/(p-1)\). For \(p=2\), subtraction in the tilt is addition; the exact-system formula uses \(\zeta_{2^{n+1}}+1=(\zeta_{2^{n+1}}-1)+2\). For \(n\ge1\), the first summand has valuation less than one, so the same valuation calculation applies. Thus the argument includes \(p=2\). Thus \(\omega\bmod p\) has valuation one. Write \(\omega=\xi c\) by Lemma 1.2; its first digit forces the first digit of \(c\) to be a unit. Hence \(c\) is a Witt unit, and \(\omega\) generates \(\ker\theta\). Since
\[
[\epsilon]-1=\omega([\epsilon_1]-1),\qquad
\theta([\epsilon_1]-1)=\zeta_p-1\ne0,
\]
the element \([\epsilon]-1\) is a uniformizer in \(B_{\mathrm{dR}}^+\). Its logarithm is itself plus terms of maximal-ideal order at least two, so \(t\) is a uniformizer.

The divided powers of \(p\) and \(\xi\) lie in \(A_0\). For sums this follows from
\((a+b)^n/n!=\sum_{i+j=n}(a^i/i!)(b^j/j!)\); for divided powers of a divided power it follows from the integer
\((mn)!/(m!(n!)^m)\), which counts partitions of \(mn\) labelled objects into \(m\) unordered blocks of size \(n\). Thus every element of \((p,\xi)A_0\) has divided powers in \(A_0\). If \(z=[x]-1\) with \(x\in1+\mathfrak m_R\), then \(\theta(z)=x^{(0)}-1\) has positive valuation. For some integer \(M\), \(\theta(z^M)\in p\mathcal O_{C_p}\), so surjectivity of \(\theta\) gives \(z^M\in(p,\xi)W(R)\). Writing \(n=Mq+r\), \(0\le r<M\), gives
\[
\frac{z^n}{n}=\frac{q!}{n}\,z^r\frac{(z^M)^q}{q!}.
\tag{5b}
\]
The last factor is integral in \(A_0\). Also
\(v_p(q!)=\sum_{j\ge1}\lfloor q/p^j\rfloor\), which grows linearly with \(q\), whereas \(v_p(n)\le\log_p n\). Hence the terms in (5b) eventually lie in \(A_0\) and tend to zero \(p\)-adically. The logarithm converges in \(A_{\mathrm{cris}}[1/p]\).

The identities for logarithms follow from the formal power-series identity
\(\log((1+Z)(1+W))=\log(1+Z)+\log(1+W)\), whose derivatives and value at \((0,0)\) determine it over \(\mathbf Q\). They can be evaluated here: the bound (5b) makes all terms beyond a sufficiently large total degree arbitrarily divisible by \(p\). The corresponding two-variable bound follows by choosing powers of both variables lying in \((p,\xi)\), and using the divided powers of their sum; factorial growth dominates the denominators. Consequently the finite-degree identities pass to the completed limit.

Witt Frobenius preserves \(A_0\):
\[
\varphi(\xi)=(\xi+p)^p-p
   =\xi^p+pw
   =p\bigl((p-1)!\xi^p/p!+w\bigr),\qquad w\in W(R),
\]
and \(p^n/n!\in\mathbf Z_p\). It extends continuously to the completion. Applying it to the convergent logarithm and using \([x^p]=[x]^p\) proves \(\varphi(\log[x])=p\log[x]\). Its injectivity on the completion has not been proved by this argument.

For completeness, exponentiation by \(a\in\mathbf Z_p\) in the logarithm identity is justified here, rather than by the discrete valuation topology, in which \(p\) is a unit. We have \([\widetilde p]^p=(\xi+p)^p\in pA_0\). Therefore a Teichmüller digit whose tilt valuation is at least \(pr\) lies in \(p^rA_0\). If two tilt elements are sufficiently close, their first \(r\) Witt difference coordinates all have sufficiently large valuation: apply functoriality to their equality modulo a sufficiently small ideal of \(R\). The Teichmüller digits are the inverse \(p^i\)-th powers of those coordinates. Each of these first digits then lies in \(p^rA_0\), and the remaining digits already carry \(p^r\). This proves continuity \(W(R)\to A_{\mathrm{cris}}\) for the product valuation topology on coordinates. The logarithm of \([\epsilon^a]\), which has residue one, has the uniformly small tails \((n-1)!w^n\xi^n/n!\) with \(w\in W(R)\). Approximate \(a\) by integers to obtain \(\log[\epsilon^a]=a\log[\epsilon]\). Taking \(a=\chi_p(g)\) gives the Galois identity in the abstract completion. Mapping this identity into the de Rham ring requires the structural map expressly retained above. ∎

Define \(B_{\mathrm{cris}}^+=A_{\mathrm{cris}}[1/p]\) and \(B_{\mathrm{cris}}=B_{\mathrm{cris}}^+[1/t]\). In all assertions using these as subrings of \(B_{\mathrm{dR}}\), we require the still unproved injective structural map. Adjoining a logarithmic period \(Y\) gives
\[
B_{\mathrm{st}}=B_{\mathrm{cris}}[Y],\qquad
\varphi(Y)=pY,\qquad N=-\frac{d}{dY},\qquad N\varphi=p\varphi N.
\tag{6}
\]
One chooses a branch of the logarithm to embed \(B_{\mathrm{st}}\) into \(B_{\mathrm{dR}}\); we take \(\log_p(p)=0\). This choice affects the displayed filtration, not the property of being semistable. The inclusions are
\[
B_{\mathrm{cris}}\subset B_{\mathrm{st}}\subset B_{\mathrm{dR}},
\qquad B_{\mathrm{st}}^{N=0}=B_{\mathrm{cris}}.
\tag{7}
\]
The last equality follows directly from (6): in characteristic zero a polynomial with zero derivative is constant. The abstract polynomial ring and its operators require no transcendence theorem. Its asserted embedding requires proving that the de Rham element \(\log([\widetilde p]/p)\) is transcendental over \(\operatorname{Frac}(B_{\mathrm{cris}})\); this is a separate **unclosed structural obligation**. On monomials \(bY^m\), both sides of \(N\varphi=p\varphi N\) equal \(-mp^m\varphi(b)Y^{m-1}\). Thus that operator relation is already proved in the abstract ring, with precisely the sign convention in (6).

For a finite \(K/\mathbf Q_p\), write \(K_0\) for its maximal unramified subfield. The invariant-ring and admissibility facts we use are
\[
B_{\mathrm{dR}}^{G_K}=K,\qquad
B_{\mathrm{cris}}^{G_K}=B_{\mathrm{st}}^{G_K}=K_0.
\tag{8}
\]
Define
\[
\begin{aligned}
D_{\mathrm{dR}}(V)&=(B_{\mathrm{dR}}\otimes_{\mathbf Q_p}V)^{G_K},\\
D_{\mathrm{cris}}(V)&=(B_{\mathrm{cris}}\otimes_{\mathbf Q_p}V)^{G_K},\\
D_{\mathrm{st}}(V)&=(B_{\mathrm{st}}\otimes_{\mathbf Q_p}V)^{G_K}.
\end{aligned}
\tag{9}
\]
Their dimensions over \(K,K_0,K_0\), respectively, are at most \(\dim V\). Equality defines **de Rham**, **crystalline**, and **semistable**, respectively. These dimension criteria are equivalent to the corresponding comparison map being an isomorphism, once the ring regularity in Lemma 1.3 has been proved for the relevant period ring. For instance, in the crystalline case,
\[
B_{\mathrm{cris}}\otimes_{K_0}D_{\mathrm{cris}}(V)
\longrightarrow B_{\mathrm{cris}}\otimes_{\mathbf Q_p}V.
\tag{10}
\]
**Lemma 1.3 (the admissibility algebra).** Let \(F\) be a field, \(B\) an \(F\)-algebra domain with a group \(G\) acting by \(F\)-algebra automorphisms, and \(E=B^G\) a field. Suppose
\[
\operatorname{Frac}(B)^G=E,
\qquad 0\ne b\in B,\ Fb\text{ stable under }G
   \Longrightarrow b\in B^\times.
\tag{10a}
\]
For every finite-dimensional \(F\)-representation \(V\), its invariant vectors are independent over \(B\) whenever they are independent over \(E\). The comparison map is injective, its invariant dimension is at most \(\dim_F V\), and equality makes that map an isomorphism. Admissible representations are closed under subquotients, tensors and duals, and their invariant functor is exact and commutes with these operations.

*Proof.* Work first over \(C=\operatorname{Frac}(B)\). A dependence among invariant vectors of minimal length can be normalized as \(x_r=\sum_{i<r}c_ix_i\), where the preceding vectors are independent. Apply \(g\) and subtract. Independence gives \(g(c_i)=c_i\), hence \(c_i\in C^G=E\), contradicting independence over \(E\). This proves comparison injectivity and the dimension bound. In the equality case its square matrix \(M\), in an invariant \(E\)-basis and an \(F\)-basis of \(V\), has nonzero determinant. Invariance gives
\[
g(\det M)=\det(\rho_V(g))^{-1}\det M.
\]
Condition (10a) makes this determinant a unit of \(B\), so the comparison matrix is invertible over \(B\), not merely over \(C\).

If \(0\to V'\to V\to V''\to0\) has admissible middle term, invariants are left exact. Consequently
\[
\dim_F V=\dim_E D(V)
 \le \dim_E D(V')+\dim_E D(V'')
 \le \dim_F V'+\dim_F V''=\dim_F V.
\]
All inequalities are equalities; both outer representations are admissible and the sequence of invariants is exact. Tensoring invariant comparison bases gives an invariant basis for the tensor product. Taking their dual basis gives an invariant basis for the dual: its vectors belong to \(B\otimes_F V^\vee\) because the comparison matrix is invertible over \(B\). Coefficients of every invariant vector in either basis lie in \(B^G=E\), proving the claimed identifications and perfect duality. Exterior and symmetric powers are quotients of tensor powers and are treated in exactly this way. Faithfulness follows because a linear map that vanishes after extension to the nonzero \(F\)-algebra \(B\) already vanishes over \(F\). ∎

This proof reconstructs the algebra of [Brinon–Conrad, Theorem 5.2.1](https://math.stanford.edu/~conrad/papers/notes.pdf). For the field \(B_{\mathrm{dR}}\), (10a) is automatic once its invariants are known. For \(B_{\mathrm{cris}}\) and \(B_{\mathrm{st}}\), (10a) is still an obligation: it does not follow merely from their displayed invariant rings (8). In the free notes, Proposition 9.1.6 uses both the stronger Tate–Sen character theorem and the unproved injectivity of \(K\otimes_{K_0}B_{\mathrm{cris}}\to B_{\mathrm{dR}}\); Proposition 9.2.11 additionally uses the semistable embedding and the crystalline character classification. Those dependencies remain open here.

One part of (8) can now be reduced explicitly to (3). Assuming the Galois identity for \(t\) in (5), the associated graded of \(B_{\mathrm{dR}}\) is \(\bigoplus_{i\in\mathbf Z}C_p(i)\). A nonzero invariant \(b\) with exact \(t\)-adic order \(i\) has a nonzero invariant leading coefficient in \(C_p(i)\); (3) forces \(i=0\). Its residue lies in \(K\). Subtract the canonical algebraic constant with that residue. A nonzero remainder would be invariant of positive order, which is impossible by the same argument. Thus \(B_{\mathrm{dR}}^{G_K}=K\). This is a full proof of this consequence, conditional precisely on (3) and the logarithm compatibility already identified. The two remaining equalities in (8) require the crystalline and semistable embedding theorems.

The full implication chain is
\[
\text{crystalline}\Longrightarrow\text{semistable}
\Longrightarrow\text{de Rham}\Longrightarrow\text{Hodge–Tate}.
\tag{11}
\]
For a de Rham \(V\), the multiplicity of weight \(h\) is
\[
\dim_K\operatorname{gr}^{-h}D_{\mathrm{dR}}(V).
\tag{12}
\]
The closure assertions for de Rham, crystalline and semistable representations are proved by Lemma 1.3 subject to the specified ring regularity. The Hodge–Tate closure assertion has its own elementary algebraic proof: regard a semilinear \(C_p\)-space as a module for the operators consisting of scalar multiplication and Galois action. Each \(C_p(h)\) is simple, since it is one-dimensional over \(C_p\). A finite direct sum of simple modules is semisimple. Indeed, given a submodule \(W\), choose a maximal direct sum \(C\) of ambient simple summands disjoint from \(W\). If \(W+C\) were proper, some generating simple summand would not lie in it and would meet it in zero, contradicting maximality. Hence \(W\) is a quotient of the ambient sum by \(C\); images of its simple generators are simple or zero, and choosing them successively proves that \(W\) is a sum of simple modules. The quotient is treated similarly. All these simple constituents are among the original \(C_p(h)\); tensors and duals follow from their displayed character formulas. Uniqueness of the weights still uses (3).

**Lemma 1.4 (the filtration comparison).** Subject to (3), the Galois action on \(t\), and the invariant and regularity obligations just stated, (11) and (12) follow from the constructed rings. In particular, they require no additional geometric comparison theorem for an already de Rham representation.

*Proof.* An invariant comparison basis over \(B_{\mathrm{cris}}\) remains a basis over \(B_{\mathrm{st}}\), and an invariant basis over \(B_{\mathrm{st}}\) remains a basis over \(B_{\mathrm{dR}}\). Coefficients of invariant vectors in the extended basis lie in its invariant field. This proves the first two implications.

Now let \(D=D_{\mathrm{dR}}(V)\) have dimension \(d=\dim V\), with the filtration induced by \(B_{\mathrm{dR}}\otimes V\). It is exhaustive and separated: every one of a finite basis of \(D\) has a finite lower bound on its coefficient orders, and a descending chain of subspaces of the finite-dimensional \(D\) stabilizes, with stable term contained in the zero intersection of all powers of \(t\). Choose a \(K\)-basis adapted to this filtration, with \(d_{i,j}\) representing a basis of \(\operatorname{gr}^iD\). Reduce
\[
r_{i,j}=\theta(t^{-i}d_{i,j})\in C_p\otimes V.
\tag{12a}
\]
These vectors satisfy \(g(r_{i,j})=\chi_p(g)^{-i}r_{i,j}\). For each fixed \(i\) they are independent over \(K\): a dependence would say that the corresponding combination of \(d_{i,j}\) lies in \(\operatorname{Fil}^{i+1}D\). They are independent over \(C_p\) as well. Indeed take a dependence of minimal length, normalize one coefficient to one, apply \(g\) and subtract; all character factors are the same, so every remaining coefficient is fixed and belongs to \(C_p^{G_K}=K\), a contradiction.

The map from the direct sum of the simple semilinear modules \(C_p(-i)\), one for each \(r_{i,j}\), to \(C_p\otimes V\) is injective. To see this, its kernel is a submodule of a finite semisimple sum, so is a sum of simple constituents by the elementary module argument above. A nonzero constituent is some \(C_p(-i)\). Its projections to the summands with different index vanish, because their equivariant Hom spaces vanish by (3); it therefore lies in the index-\(i\) block. Injectivity on that block was just proved. Hence the kernel is zero. There are \(d\) such vectors, so they form a \(C_p\)-basis and give the Hodge–Tate decomposition with weight \(-i\) occurring \(\dim_K\operatorname{gr}^iD\) times. This proves (12) and the final implication of (11).

It also proves strictness of the filtered period comparison. The vectors \(t^{-i}d_{i,j}\) lie in \(B_{\mathrm{dR}}^+\otimes V\) and reduce to the basis (12a). Their determinant has nonzero residue, so they form a basis over this discrete valuation ring. Thus the period comparison carries the tensor-product filtration on \(B_{\mathrm{dR}}\otimes_KD\) exactly to the coefficient filtration on \(B_{\mathrm{dR}}\otimes V\). Tensor and dual bases show that the usual sum filtration on tensors and annihilator filtration on duals are compatible. ∎

Being de Rham and being Hodge–Tate are invariant under restriction to a finite extension; the finite descent proof is given in Lemma 2.2A. Being crystalline can fail to descend through a ramified extension, as Theorem 3.1 will show. A representation is **potentially semistable** if it becomes semistable over some finite extension.

**The \(p\)-adic monodromy theorem (full assertion, proof unclosed).** A de Rham representation of \(G_K\) is potentially semistable. The actual free account [Berger, §IV.5.3](https://perso.ens-lyon.fr/laurent.berger/articles/article05.pdf) reduces this to quasi-unipotence of the associated differential equation over the Robba ring. That reduction requires overconvergence of \((\varphi,\Gamma)\)-modules, construction of \(N_{\mathrm{dR}}(V)\), its comparison with semistable periods, and quasi-unipotence for differential equations with Frobenius structure. None of those general results is proved here or in an inspected earlier lesson. The assertion keeps its full finite-extension scope; the Tate calculation in §4 proves one concrete example, not this theorem. This is a theorem at the coefficient prime, distinct from the prime-to-coefficient monodromy theorem proved earlier in the course.

## 2. Determinants and finite-image representations

Taking exterior powers of (2) gives an immediate but useful check.

**Proposition 2.1 (determinant weights).** If \(V\) has weights \(h_1,\ldots,h_d\), then \(\det V\) is Hodge–Tate of weight \(\sum_i h_i\). Tensoring by \(\mathbf Q_p(n)\) adds \(n\) to every weight, and dualizing negates every weight.

**Proof.** In the top exterior power of (2), choose one basis vector from each summand. The action on their wedge is the product of their cyclotomic factors:
\[
\bigwedge^d(C_p\otimes V)\simeq C_p(h_1+\cdots+h_d).
\tag{13}
\]
Exterior powers commute with scalar extension. Similarly \(C_p(h)\otimes_{C_p}C_p(n)=C_p(h+n)\), and the dual of \(C_p(h)\) is \(C_p(-h)\). These identities prove all three assertions. ∎

We will prove finite Galois descent explicitly, so that the finite-image assertions do not conceal a descent theorem.

**Lemma 2.2 (semilinear descent).** Let \(L/K\) be finite Galois with group \(H\), and let \(W\) be a finite-dimensional \(L\)-space with semilinear \(H\)-action. Then
\[
L\otimes_KW^H\xrightarrow{\ \sim\ }W,\qquad
\dim_KW^H=\dim_LW.
\tag{14}
\]

**Proof.** Distinct automorphisms of \(L\) are linearly independent as functions \(L\to L\). To see this, take a nonzero relation of minimal length \(\sum_j a_j\sigma_j(x)=0\) for every \(x\). A relation of length one is impossible by evaluating at \(1\). For length at least two, choose \(b\) with \(\sigma_1(b)\ne\sigma_2(b)\); subtract \(\sigma_1(b)\) times the original relation from the relation evaluated at \(bx\). The first term vanishes and the second does not, contradicting minimality.

Let \(S\) be the \(L\)-span of \(W^H\). It is \(H\)-stable. For every \(a\in L,w\in W\), the sum
\[
P(aw)=\sum_{g\in H}g(a)g(w)
\tag{15}
\]
is invariant and lies in \(S\). If \(W/S\ne0\), choose \(0\ne\bar w\in W/S\) and an \(L\)-linear functional \(f\) with \(f(\bar w)\ne0\). Projecting (15) to the quotient and applying \(f\) gives
\[
\sum_{g\in H}f(g\bar w)g(a)=0\quad\text{for every }a\in L.
\tag{16}
\]
Independence of the automorphisms contradicts the nonzero coefficient of the identity. Hence invariants span \(W\) over \(L\). Choose an \(L\)-basis \(w_1,\ldots,w_d\) among them. If \(w=\sum_i a_iw_i\) is invariant, uniqueness of its coefficients gives \(g(a_i)=a_i\), so all \(a_i\) lie in \(K\). The same basis is therefore a \(K\)-basis of \(W^H\), proving (14). ∎

**Lemma 2.2A (finite-extension descent).** Subject to (3) and (8), being Hodge–Tate or de Rham is equivalent over \(K\) and over any finite extension \(L/K\), with the same weights and with \(D_{\mathrm{dR},L}=L\otimes_KD_{\mathrm{dR},K}\).

*Proof.* Pass to a Galois closure, since restriction of either displayed comparison isomorphism remains an isomorphism. Suppose first that \(V|_{G_L}\) is de Rham. Its invariant module \(D_L\) carries a semilinear action of \(H=\operatorname{Gal}(L/K)\), because \(G_L\) is normal and \(B_{\mathrm{dR}}^{G_L}=L\). It has dimension \(\dim V\). Lemma 2.2 gives \(D_L=L\otimes_KD_L^H\), with \(D_L^H=D_K\). A descended invariant basis is still a period basis, proving de Rham admissibility over \(K\). The filtration is stable under \(H\). Apply the same lemma to each filtered subspace; its descended dimension is unchanged, so every graded dimension is unchanged.

For the Hodge–Tate assertion put \(D_{h,L}=(C_p(-h)\otimes V)^{G_L}\). Under a decomposition (2), (3) gives \(\dim_LD_{h,L}=m_h\). Each \(D_{h,L}\) is stable under \(H\), including its twisted action. Semilinear descent supplies \(m_h\) invariant vectors over \(K\). Their images after tensoring with \(C_p(h)\) give the same summands of (2), now with \(G_K\)-action. The direct sum remains a comparison isomorphism because it is one after extension to \(L\), so the weights and multiplicities are unchanged. ∎

**Theorem 2.3 (finite image).** A finite-image \(\mathbf Q_p\)-representation of \(G_K\) is Hodge–Tate with all weights zero. It is also de Rham with its entire de Rham module in filtration degree zero. The explicit fixed bases in its proof exist by finite descent alone. Identifying *all* invariant coefficients and uniqueness of weights uses (3) and (8).

**Proof.** Choose a finite Galois \(L/K\) whose subgroup \(G_L\) acts trivially on \(V\). Equation (3) gives
\[
(C_p\otimes V)^{G_K}
=(L\otimes V)^{\operatorname{Gal}(L/K)}.
\tag{17}
\]
Apply Lemma 2.2 to \(L\otimes V\). Its invariant \(K\)-basis becomes a \(C_p\)-basis of \(C_p\otimes V\), and each basis vector is fixed by \(G_K\). This is (2) with \(m_0=\dim V\). There are no other weights, by the uniqueness following (3).

Replace \(C_p\) by \(B_{\mathrm{dR}}\) and use (8). The same argument gives
\[
D_{\mathrm{dR}}(V)=(L\otimes V)^{\operatorname{Gal}(L/K)},
\qquad \dim_KD_{\mathrm{dR}}(V)=\dim V.
\tag{18}
\]
Algebraic constants \(L\subset B_{\mathrm{dR}}^+\) meet \(\operatorname{Fil}^1B_{\mathrm{dR}}\) only in zero: the residue map restricts to their embedding in \(C_p\). Thus \(\operatorname{Fil}^0D=D\) and \(\operatorname{Fil}^1D=0\). ∎

**Corollary 2.4 (the modular determinant).** For a newform \(f\) of weight \(k\ge2\), the stated Hodge–Tate weights \(0,k-1\) imply that \(\det\rho_{f,\lambda}\) has weight \(k-1\). This agrees with
\[
\det\rho_{f,\lambda}=\varepsilon_G\chi_p^{\,k-1}.
\tag{19}
\]

**Proof.** Proposition 2.1 gives the sum \(k-1\). The finite character \(\varepsilon_G\) has weight zero by Theorem 2.3, and \(\chi_p^{k-1}\) has weight \(k-1\) by (1). Their product has the same weight. Equation (19) is the higher-weight lesson's determinant conclusion; its full arithmetic-model and primitive-pairing dependencies remain unclosed there. This calculation proves the stated consistency when that construction exists; it does not establish (19), existence of \(\rho_{f,\lambda}\), or a global character identity by itself. ∎

For coefficients in a finite extension \(E/\mathbf Q_p\), first restrict to \(G_K\) for a finite \(K\) containing the images of every embedding of \(E\). The factorization
\(C_p\otimes_{\mathbf Q_p}E=\prod_{\sigma:E\hookrightarrow C_p}C_p\)
follows by writing \(E=\mathbf Q_p[\alpha]\) and factoring its separable minimal polynomial into distinct linear factors over the algebraically closed \(C_p\) of Lemma 1.0; evaluation at the roots and the elementary Chinese remainder identity give the product. Its factors are stable over the chosen \(K\), and the calculations apply in each factor. Lemma 2.2A proves that weights are unchanged under this finite extension, with the same foundational dependence on (3). For the modular representations in (33), the two asserted weights are \(0,k-1\) in every factor. Restriction of scalars repeats them \([E: \mathbf Q_p]\) times; the \(E\)-linear determinant still has weight \(k-1\) in each factor.

## 3. Crystalline examples and the role of inertia

**Theorem 3.1 (finite-image crystalline criterion).** For a finite-image representation \(V\) of \(G_{\mathbf Q_p}\),
\[
\dim_{\mathbf Q_p}D_{\mathrm{cris}}(V)
=\dim_{\mathbf Q_p}V^{I_p}.
\tag{20}
\]
Consequently it is crystalline if and only if it is unramified.

**Proof.** Let \(L/\mathbf Q_p\) be finite Galois killing the action, \(H=\operatorname{Gal}(L/\mathbf Q_p)\), and \(J\subset H\) its inertia subgroup. By (8),
\[
D_{\mathrm{cris}}(V)=(L_0\otimes_{\mathbf Q_p}V)^H.
\tag{21}
\]
The group \(J\) fixes \(L_0\) pointwise, so taking \(J\)-invariants gives \(L_0\otimes V^J\). The quotient \(H/J\) is \(\operatorname{Gal}(L_0/\mathbf Q_p)\); apply Lemma 2.2 to its semilinear action. This proves (20). Finally \(V^J=V^{I_p}\), and the dimension criterion (9) makes crystallinity equivalent to trivial inertia. ∎

For finite unramified \(V\), (21) is particularly concrete: \(L=L_0\), and the invariant basis supplied by descent exhibits all the crystalline periods. The general infinite-image assertion can be proved by constructing its periods, without importing the completed inertial restriction theorem.

**Proposition 3.2 (all unramified period matrices).** Every continuous unramified \(\mathbf Q_p\)-representation of \(G_{\mathbf Q_p}\) has a fixed basis after extension to \(W(\overline{\mathbf F}_p)[1/p]\subset B_{\mathrm{cris}}\). Consequently it is crystalline, subject only to the crystalline structural embedding and invariant-ring obligations already specified. In that basis the crystalline Frobenius has the characteristic polynomial of the inverse of arithmetic Frobenius on \(V\), so every slope is zero.

*Proof.* We first justify an integral lattice. A compact subgroup of \(\operatorname{GL}_d(\mathbf Q_p)\) and its inverses have bounded matrix entries. If \(\Lambda_0\) is a lattice, the \(\mathbf Z_p\)-span of its translates lies between \(\Lambda_0\) and \(p^{-m}\Lambda_0\) for some \(m\). It is finitely generated, free of rank \(d\), and stable. This supplies a basis in which the arithmetic Frobenius generator has matrix \(A\in\operatorname{GL}_d(\mathbf Z_p)\).

Write \(\sigma\) for Witt Frobenius on \(W(\overline{\mathbf F}_p)\). We construct a unit matrix \(X\) satisfying
\[
A\sigma(X)=X.
\tag{21a}
\]
Let \(r\) be the order of \(\overline A\in\operatorname{GL}_d(\mathbf F_p)\). On \(\mathbf F_{p^r}^d\), the operator \(\overline A\sigma\) is a semilinear action of the cyclic group of order \(r\): its \(r\)-th power is the identity since \(\sigma\) fixes the entries of \(\overline A\). Lemma 2.2 supplies a basis fixed by this action. Its columns form an invertible solution \(X_1\) of (21a) modulo \(p\).

Inductively suppose that a unit matrix \(X_n\) solves (21a) modulo \(p^n\). In \(W(\overline{\mathbf F}_p)\) write
\[
X_n^{-1}A\sigma(X_n)=1+p^nE_n.
\]
Replace \(X_n\) by \(X_n(1+p^nY_n)\). Modulo \(p^{n+1}\) the left side becomes \(1+p^n(E_n-Y_n+\sigma(Y_n))\). Each equation \(y^p-y=-e\) has a solution in \(\overline{\mathbf F}_p\), so choose the entries of \(Y_n\) accordingly. This constructs \(X_{n+1}\equiv X_n\pmod {p^n}\). Completeness gives an invertible limiting \(X\) satisfying (21a). Each finite approximation uses a finite residue field; thus the usual unramified Galois action on its Witt digits is continuous, and agrees with \(\sigma\) at arithmetic Frobenius.

The residue-field inclusion \(\overline{\mathbf F}_p\subset R\) of Lemma 1.0 gives \(W(\overline{\mathbf F}_p)\subset W(R)\subset A_{\mathrm{cris}}\). Its inertia action is trivial. The columns of \(X\), regarded as vectors in \(B_{\mathrm{cris}}\otimes V\), are invariant under arithmetic Frobenius by (21a). They are invariant under the whole unramified group, since its integer Frobenius powers are dense and the action on these digits is continuous. They form a period basis because \(X\) is a unit matrix. Given \(B_{\mathrm{cris}}^{G_{\mathbf Q_p}}=\mathbf Q_p\), all invariant vectors are exactly the rational combinations of these columns, proving the dimension criterion.

Period Frobenius acts by \(X^{-1}\sigma(X)=X^{-1}A^{-1}X\) on this basis. Its characteristic polynomial is that of \(A^{-1}\), establishing the normalization. Every eigenvalue of \(A\) and of \(A^{-1}\) is integral, since each satisfies a monic polynomial over \(\mathbf Z_p\). Their valuations are therefore both nonnegative, so the eigenvalues are units and the slopes are zero. ∎

The successive-approximation mechanism appears in the scalar calculation [Brinon–Conrad, Lemma 9.3.3](https://math.stanford.edu/~conrad/papers/notes.pdf); the matrix construction and its initial finite descent are written above. It proves the infinite-image assertion with its actual ring dependencies, rather than treating the notes' reference to completed descent as a proof.

A crystalline representation can be ramified. For \(V=\mathbf Q_p(n)\), with basis \(e_n\), equations (5)–(8) give
\[
D_{\mathrm{cris}}(V)=\mathbf Q_p(t^{-n}e_n),\qquad
\varphi(t^{-n}e_n)=p^{-n}t^{-n}e_n.
\tag{22}
\]
Indeed \(t^{-n}e_n\) is invariant; if \(be_n\) is invariant, then \(bt^n\) is invariant and hence belongs to \(\mathbf Q_p\). Its filtration is
\[
\operatorname{Fil}^iD_{\mathrm{dR}}(\mathbf Q_p(n))
=\begin{cases}
D_{\mathrm{dR}}(\mathbf Q_p(n))&i\le -n,\\
0&i>-n.
\end{cases}
\tag{23}
\]
Thus the Hodge–Tate weight is \(n\), the filtration jump is \(-n\), and the crystalline Frobenius eigenvalue is \(p^{-n}\). These are three consistent quantities. In particular \(\mathbf Q_p(1)\) is crystalline despite its nontrivial cyclotomic inertia.

**Elliptic comparison statements (full assertions, proofs unclosed).** For an elliptic curve \(E/K\), \(V_pE\) is de Rham, with weights \(0,1\). It is crystalline exactly when \(E\) has good reduction, and semistable exactly when \(E\) has semistable reduction. The free author account [Berger, §§II.3.2, II.5.1](https://perso.ens-lyon.fr/laurent.berger/articles/article05.pdf) states the geometric comparison theorems and the reduction converses. It does not give those proofs. The good-reduction direction requires a comparison between the \(p\)-adic Tate module and crystalline cohomology or the Dieudonné module of the integral \(p\)-divisible group. Its converse requires recovering a good integral model from the crystalline representation; the semistable converse similarly requires recovering the toric part. None is supplied by the prime-to-\(p\) finite-étale specialization proof of the Tate-module lesson, since multiplication by \(p\) is not étale on its special fibre. We retain both equivalences as obligations, not as consequences of that earlier specialization.

At a good ordinary prime the two Frobenius slopes on the covariant period module are \(-1,0\); at a good supersingular prime both slopes are \(-1/2\). This assertion also needs the crystalline/Dieudonné comparison and the height-two slope classification, neither yet proved here. The signs are consistent with (22). The unramified calculation of Proposition 3.2 has slopes zero and does not prove these elliptic slope assertions.

## 4. A Tate curve, with its periods calculated

Let \(q\in\mathbf Q_p^\times\) satisfy \(v_p(q)>0\), and let \(E_q\) be the split Tate curve. Lemma 3.0 of the earlier local elliptic-curve lesson actually proves, by the convergent series and their inverse series, the equivariant group isomorphism \(E_q(\overline{\mathbf Q}_p)=\overline{\mathbf Q}_p^\times/q^{\mathbf Z}\). We need its coefficient-prime torsion, so we give that passage explicitly. A class \([z]\) is killed by \(p^n\) exactly when \(z^{p^n}=q^b\) for an integer \(b\). Sending it to \(b\bmod p^n\) is well defined, since replacing \(z\) by \(zq^a\) adds \(ap^n\) to \(b\). The kernel is \(\mu_{p^n}\), and compatible roots \(q_n\) with \(q_n^{p^n}=q\) give a compatible preimage of \(1\). Together with compatible primitive \(\zeta_{p^n}\), they give a basis at every level. Multiplication by \(p\) carries these bases to the previous level, so the inverse limit, including its surjectivity, gives
\[
0\longrightarrow\mathbf Q_p(1)\longrightarrow V_pE_q
\longrightarrow\mathbf Q_p\longrightarrow0.
\tag{24}
\]
Choose compatible \(p\)-power roots of \(q\). With suitable basis vectors \(e,f\), the action is
\[
g(e)=\chi_p(g)e,\qquad g(f)=f+c_q(g)e.
\tag{25}
\]
More explicitly \(g(q_n)/q_n=\zeta_{p^n}^{c_q(g)}\); compatibility defines \(c_q(g)\in\mathbf Z_p\) and
\(c_q(gg')=c_q(g)+\chi_p(g)c_q(g')\). This proves (25) directly also at \(\ell=p\), without using the earlier prime-to-\(p\) assertion that unit roots are unramified.

**Lemma 4.0 (the Tate logarithmic period).** In the abstract semistable period algebra of (6), there is an explicitly constructed \(u=\log[\widetilde q]\) with
\[
g(u)=u+c_q(g)t,\quad
\varphi(u)=pu,\quad
N(u)=-v_p(q),\quad
\theta(u)=\log_p(q).
\tag{26}
\]
The last expression uses the proposed embedding in \(B_{\mathrm{dR}}\); its proof below is conditional on that embedding carrying the divided-power sums to their de Rham sums. The other identities already hold in the abstract completed algebra. In particular the logarithmic identities themselves no longer form an independent unexplained input.

*Proof.* Put \(m=v_p(q)\in\mathbf Z_{>0}\) and \(a=q/p^m\in\mathbf Z_p^\times\). Choose a root system \(\widetilde p\), put \(\widetilde a=\widetilde q/\widetilde p^m\in R^\times\), and take \(M=p-1\) (so \(M=1\) if \(p=2\)). The residue of \(\widetilde a\) belongs to \(\mathbf F_p^\times\), hence \(\widetilde a^M\in1+\mathfrak m_R\). Lemma 1.2A defines
\[
u_a=\frac1M\log[\widetilde a^M]\in A_{\mathrm{cris}}[1/p].
\tag{26a}
\]
It satisfies \(\varphi(u_a)=pu_a\). Let \(c_p\) be the cocycle from the chosen roots of \(p\). Define the action on the formal variable by \(g(Y)=Y+c_p(g)t\). The cocycle identity and \(g(t)=\chi_p(g)t\) verify the group law for this action. It commutes with \(\varphi(Y)=pY\) and with \(N=-d/dY\), by substitution. From the exact root systems,
\[
g(\widetilde a)/\widetilde a
 =\epsilon^{c_q(g)-mc_p(g)}.
\]
The logarithm product identity and its \(\mathbf Z_p\)-exponent identity in Lemma 1.2A therefore give
\[
g(u_a)=u_a+(c_q(g)-mc_p(g))t.
\]
Set \(u=mY+u_a\). Then \(g(u)=u+c_q(g)t\), \(\varphi(u)=pu\), and \(N(u)=-m\), proving the first three identities of (26).

The logarithm branch on \(\mathbf Q_p^\times\) is itself elementary. On \(1+p\mathbf Z_p\), the usual series \(\sum_{n\ge1}(-1)^{n+1}(b-1)^n/n\) converges because \(v_p((b-1)^n/n)\to\infty\), including \(p=2\). Its formal product identity passes to this convergent limit. Extend to units by \(\log_p(a)=M^{-1}\log_p(a^M)\), killing the finite root-of-unity factor, and then to every \(p^r a\) by assigning \(\log_p(p)=0\). Multiplying by further powers of \(M\) or by a positive integer changes neither value nor its additive property.

For the claimed de Rham image, take
\[
Y\longmapsto\log_{\mathrm{dR}}([\widetilde p]/p).
\tag{26b}
\]
The ratio has residue one, so this particular logarithm is a well-defined \(\xi\)-adic sum even before its transcendence is known. To compare (26a) with that topology, write
\[
[\widetilde a]^M-1=(a^M-1)+\xi w,
\qquad a^M-1\in p\mathbf Z_p,\quad w\in W(R).
\]
Both terms admit divided powers. The convergent logarithm product identity gives, in the completed divided-power algebra,
\[
\log[\widetilde a^M]
 =\log_p(a^M)
  +\log\bigl([\widetilde a]^M/a^M\bigr).
\]
The second logarithm has argument \(1+\xi w/a^M\), with integral denominator \(a^M\), and its divided-power series is
\(\sum(-1)^{n+1}(n-1)!(w/a^M)^n\xi^n/n!\). Its prescribed de Rham image is exactly the same \(\xi\)-adic series. Consequently, under the structural map with that series compatibility,
\[
u_a=\log_p(a)+\log_{\mathrm{dR}}([\widetilde a]/a),
\qquad
u=\log_p(q)+\log_{\mathrm{dR}}([\widetilde q]/q).
\tag{26c}
\]
Its residue is \(\log_p(q)\), proving the last identity of (26). This comparison uses the structural-map obligation exactly once, rather than interchanging two different completions without justification. ∎

The calculation reconstructs the actual free material [Berger, §§II.4.2–II.4.4](https://perso.ens-lyon.fr/laurent.berger/articles/article05.pdf) and [Brinon–Conrad, Lemmas 9.2.2 and 9.2.7](https://math.stanford.edu/~conrad/papers/notes.pdf). We use \(\varphi(Y)=pY\), not \(Y^p\), and the ordinary logarithm power \(n\), not \(n-1\). These details are essential to (26)–(29).

For the rest of this calculation retain explicitly the period embeddings and invariant rings (8). Subject to those specified structural obligations, the following basis, monodromy and filtration proof is complete.

Set
\[
x=t^{-1}e,\qquad y=f-ut^{-1}e.
\tag{27}
\]
Equation (25) and the first identity of (26) show that both vectors are invariant: the two \(c_q(g)e\) terms in \(g(y)\) cancel. The matrix from \(e,f\) to \(x,y\) has invertible determinant \(t^{-1}\). Thus they form a \(B_{\mathrm{st}}\)-basis after extension of scalars. Any invariant vector expressed in this basis has invariant scalar coefficients; by (8) these lie in \(\mathbf Q_p\). We have proved
\[
D_{\mathrm{st}}(V_pE_q)=\mathbf Q_px\oplus\mathbf Q_py,
\qquad
\varphi(x)=p^{-1}x,\quad\varphi(y)=y,
\qquad N(x)=0,\quad N(y)=v_p(q)x.
\tag{28}
\]
In particular the representation is semistable and \(N\ne0\). On \(y\), the relation \(N\varphi=p\varphi N\) reads
\[
v_p(q)x=p\varphi(v_p(q)x);
\tag{29}
\]
on \(x\), both sides vanish.

By (7) and invariance,
\[
D_{\mathrm{cris}}(V)
=D_{\mathrm{st}}(V)^{N=0}.
\tag{30}
\]
For (28), the right side is \(\mathbf Q_px\), of dimension one. The crystalline criterion requires dimension two. Therefore **the Tate curve is semistable and not crystalline**.

Its filtration is also visible. Write \(A=\log_p(q)\). A vector \(ax+by\) has coefficients \(b\) on \(f\) and \(t^{-1}(a-bu)\) on \(e\). Both belong to \(B_{\mathrm{dR}}^+\) exactly when \(a=bA\); this uses \(\theta(u)=A\) and that \(t\) generates the maximal ideal. All vectors lie in \(\operatorname{Fil}^{-1}\), and membership in \(\operatorname{Fil}^1\) forces first \(b=0\), then \(a=0\). Hence
\[
\operatorname{Fil}^iD_{\mathrm{dR}}(V_pE_q)
=\begin{cases}
D_{\mathrm{dR}}(V_pE_q)&i\le-1,\\
\mathbf Q_p(y+Ax)&i=0,\\
0&i\ge1.
\end{cases}
\tag{31}
\]
The associated graded has dimensions one in degrees \(-1,0\); the proved filtration algebra in Lemma 1.4 gives weights \(1,0\), subject to its precise period foundations. There is also a direct check needing no general filtration lemma. Put \(b=\theta((u-A)/t)\in C_p\). The quotient is integral because \(\theta(u-A)=0\), and (26) gives \(\chi_p(g)g(b)=b+c_q(g)\). Thus \(f-be\) is fixed in \(C_p\otimes V_pE_q\), whereas \(e\) transforms by \(\chi_p\). The vectors \(e,f-be\) form a basis and exhibit \(C_p(1)\oplus C_p(0)\) directly. For the especially simple choice \(q=p\), \(u=Y\), \(A=0\), and \(N(y)=x\); the filtration line is \(\mathbf Q_py\).

## 5. Geometry and modularity

We call a continuous \(E\)-representation of \(G_{\mathbf Q}\), with \(E/\mathbf Q_p\) finite, **geometric in the Fontaine–Mazur sense** if it is unramified at all but finitely many primes and de Rham at \(p\). The full \(p\)-adic monodromy assertion makes the last condition equivalent to potential semistability; this equivalence retains the general monodromy proof obligation in §1. We separately say **arises from geometry** for a subquotient, with coefficient extension allowed, of
\[
H^i_{\mathrm{\acute et}}(X_{\overline{\mathbf Q}},\mathbf Q_p)(j),
\qquad X/\mathbf Q\text{ smooth projective}.
\tag{32}
\]
In [Taylor’s freely accessible original account, §1](https://www.numdam.org/item/AFST_2004_6_13_1_73_0.pdf), the word “geometric” is used for the conclusion (32); our terminology distinguishes the local conditions from their conjectural geometric realization.

Smooth proper base change and \(p\)-adic comparison imply that (32) satisfies the two local conditions. They also imply crystallinity at a prime \(p\) where a smooth proper model exists. These are deep inputs, not consequences of the definition of “geometric.”

**Fontaine–Mazur conjecture (stated).** Every irreducible representation satisfying those two local conditions arises from geometry in the sense of (32). See [Taylor, Conjecture 1.1, printed p.80](https://www.numdam.org/item/AFST_2004_6_13_1_73_0.pdf). Irreducibility belongs in this formulation. In particular, one expects purity of a single weight for such an irreducible representation; merely being locally de Rham does not itself prove purity or a compatible system.

For a weight-\(k\) newform with \(k\ge2\), the geometric construction and comparison give
\[
\operatorname{HT}(\rho_{f,\lambda}|_{G_{\mathbf Q_p}})=\{0,k-1\},
\qquad
\rho_{f,\lambda}|_{G_{\mathbf Q_p}}\text{ crystalline if }p\nmid N.
\tag{33}
\]
The scope in (33) is **every** \(p\nmid N\), including \(p<k\). Here is the precise conditional deduction. Suppose that the newform representation is a projector summand, with the required dual and twist, of a smooth projective Kuga–Sato variety having a smooth proper model at \(p\). Smooth proper crystalline comparison would make that full cohomology crystalline; Lemma 1.3 then makes its projector summand crystalline. Geometric Hodge comparison, followed by Lemma 1.4 and the two nonzero Hodge pieces of the newform summand, would give weights \(0,k-1\). The missing arithmetic model, projector and higher-dimensional geometric comparisons are still obligations in the higher-weight construction and here. This paragraph supplies the deduction, not those missing proofs.

The actual free [Scholl author manuscript, Theorem 1.2.4(ii), Remark 1.2.5 and §4.2.3](https://www.dpmms.cam.ac.uk/~ajs1005/preprints/mf.pdf) explicitly assumes \(p\ge k\) for the crystalline statement available there, since the variety has dimension \(k-1\). Its §4.2.1 asserts the good integral models using an external modular-model theorem. The general smooth proper comparison is stated in [Berger’s free author manuscript, §II.5.1](https://perso.ens-lyon.fr/laurent.berger/articles/article05.pdf). Neither statement is being relabelled as a local proof or used to shrink (33) to \(p\ge k\).

In weight one, once the preceding lesson’s asserted finite-image representation has actually been constructed over a number field, its \(p\)-adic realization is de Rham with weights \(0,0\) by Theorem 2.3. The existence theorem is not proved again here, and no still-unclosed part of that construction is discharged by this local calculation. It is crystalline at \(p\) exactly when its local inertia is trivial. Thus the weight-one case is geometric but does not satisfy a hypothesis of **distinct** weights.

Here are two precise modularity statements. They illustrate how much more is required than the phrase “odd and geometric.” They are historical theorem versions, not assertions that their hypotheses are the weakest now possible. In each, a stable lattice defines the semisimplified residual representation \(\bar\rho\), and \(\bar\chi_p\) denotes the mod-\(p\) cyclotomic character. Absolute irreducibility in their hypotheses makes the global residual representation irreducible. Its **local restriction** is taken with its extension data; semisimplifying that local restriction would lose the meaning of the stars in (34)–(35).

**Lemma 5.0 (the elementary normalization).** Under either theorem's residual absolute-irreducibility hypothesis, the characteristic-zero representation is irreducible. For \(p>2\), residual oddness implies characteristic-zero oddness. Distinct integral Hodge–Tate weights can be normalized by a Tate twist to \(0,k-1\) for an integer \(k\ge2\).

*Proof.* The compact-image lattice argument in Proposition 3.2 works for any profinite Galois group and, with its valuation-ring basis, for finite coefficient fields. If an invariant coefficient-field line existed, intersect it with the lattice and choose a generator with at least one unit coordinate. Its reduction gives a nonzero stable line in the residual two-dimensional space: the intersection is saturated, since a vector in the line divisible by the uniformizer in the ambient lattice has its quotient in that same line. This contradicts residual absolute irreducibility, already implied by irreducibility on the subgroup \(G_{\mathbf Q(\zeta_p)}\). At complex conjugation the determinant has square one. Its reduction is \(-1\), and for \(p>2\) the two values \(+1,-1\) have distinct reductions; the determinant is therefore \(-1\). Finally, if the weights are \(a<b\), twisting by \(\mathbf Q_p(-a)\) gives \(0,b-a\) by Proposition 2.1. Put \(k=b-a+1\). ∎

This normalization alone proves no modularity lifting theorem.

**Kisin's printed 2009 theorem (stated).** Let \(p>2\) and let
\(\rho:G_{\mathbf Q,S}\to\operatorname{GL}_2(\mathcal O_E)\), where \(S\) is finite and contains \(p,\infty\). Suppose:

1. \(\rho|_{G_{\mathbf Q_p}}\) is potentially semistable with distinct Hodge–Tate weights.
2. It becomes semistable over an **abelian** extension of \(\mathbf Q_p\).
3. \(\bar\rho\) is odd, and \(\bar\rho|_{G_{\mathbf Q(\zeta_p)}}\) is absolutely irreducible.
4. Its local reduction is not, for any character \(\eta\), of the form
   \[
   \eta\otimes\begin{pmatrix}\bar\chi_p&*\\0&1\end{pmatrix}.
   \tag{34}
   \]

Then \(\rho\), up to twist, comes from a holomorphic cuspidal eigenform of weight at least two. This is the [openly deposited printed Kisin 2009 article, introduction, main theorem, pp.641–642](https://dash.harvard.edu/entities/publication/73120378-dc24-6bd4-e053-0100007fdf3b). The discussion immediately after it explains how removal of condition 2 depends on compatibility for the \(p\)-adic local Langlands correspondence; deleting that condition from the printed theorem without identifying the further input would misstate its scope. The proof remains unclosed here. The actually read introductory proof outline on printed p.643 reduces modularity lifting to equality of local deformation-ring and automorphic multiplicities, and obtains the required local inequality through the \(p\)-adic local Langlands correspondence. A complete proof still requires those deformation rings, the multiplicity comparison, patching, residual modularity, and the stated local/classical compatibility. The local period computations above do not provide those global or deformation inputs.

**Emerton's theorem (stated, March 2011 version).** Let \(p>2\) and \(V\) be a continuous, irreducible, odd, two-dimensional \(E\)-representation of \(G_{\mathbf Q}\), unramified at all but finitely many primes. Suppose that \(\bar V|_{G_{\mathbf Q(\zeta_p)}}\) is absolutely irreducible and that \(\bar V|_{G_{\mathbf Q_p}}\) is neither of the forms
\[
\eta\otimes\begin{pmatrix}1&*\\0&1\end{pmatrix},
\qquad
\eta\otimes\begin{pmatrix}1&*\\0&\bar\chi_p\end{pmatrix}
\tag{35}
\]
for any residue-field-valued \(\eta\); the star may be zero. If \(V|_{G_{\mathbf Q_p}}\) is de Rham with distinct Hodge–Tate weights, then \(V\) is a twist of the representation attached to a classical cuspidal eigenform of weight at least two. See [Emerton's March 2011 author draft, Theorem 1.2.4(2), p.4](https://math.uchicago.edu/~emerton/pdffiles/lg.pdf). Unlike its earlier Corollary 1.2.2, this theorem does not assume promodularity: Theorem 1.2.3 supplies it under the stated residual hypotheses. The exclusion in (35) has the displayed **ordering** of characters; it should not silently be replaced by (34).

Its exact logical deduction is as follows, with its still-unproved interfaces identified. Theorem 1.2.3 would give promodularity from precisely \(p>2\), residual irreducibility on \(G_{\mathbf Q(\zeta_p)}\), oddness, and the two exclusions (35). The first exclusion also prevents a local direct sum of two characters with identical reductions: their reduction would have both diagonal characters equal and would have the first excluded form, for any stable lattice. Thus the additional local condition of Corollary 1.2.2(2) is met. That corollary would then give the classical cuspidal conclusion. This proves the logical passage between these statements, without treating either intermediate theorem as proved here.

The actual proof on p.94, Theorem 7.1.1, uses the local-global embedding into completed modular-curve cohomology (Theorem 1.2.1), nonzero locally algebraic vectors for a de Rham local representation (Theorem 3.3.21), and identification of those completed-cohomology vectors with classical forms. The promodularity argument on p.96 uses residual modularity and a deformation-ring/Hecke-algebra comparison. These are the missing proof interfaces for this exact conclusion. Replacing them by the words “odd and geometric” would not establish it.

These theorems combine local \(p\)-adic representation theory, deformation theory, residual modularity, and global automorphic methods. The final lesson states the residual modularity theorem used in this circle of arguments.

## 6. Exact remaining proof obligations

The full assertions have been retained. The following distinctions prevent a citation from concealing a missing proof.

1. **Completed algebraic closure invariants.** Equation (3) still requires the Ax–Sen–Tate ramification estimate and the cyclotomic trace bounds. The free Brinon–Conrad notes state the result in Theorem 2.2.7 and reduce its twisted vanishing in Theorem 14.3.4 to their Tate–Sen hypotheses and Lemma 14.1.9. Those bounds have not been reconstructed here. Lemma 1.0 proves algebraic closedness of the completion and of the tilt fraction field; neither implies (3). Uniqueness of weights, the precise invariant fields, and character regularity still depend on this gap.
2. **Crystalline and semistable structural maps.** Lemmas 1.1–1.2 construct the Witt algebra, \(\theta\), its principal kernel and the de Rham discrete valuation ring completely. Lemma 1.2A constructs the completed divided-power logarithms and their formal Galois and Frobenius identities. Still required are the injective map \(A_{\mathrm{cris}}\to B_{\mathrm{dR}}^+\) with its divided-power-series compatibility, injectivity of Frobenius on the completed ring, injectivity after \(K\otimes_{K_0}(-)\), and transcendence of (26b) over \(\operatorname{Frac}(B_{\mathrm{cris}})\). The actual free notes omit proofs of substantial parts of these statements in §§9.1–9.2. The invariant fields for the crystalline and semistable rings and their regularity (10a) must also be proved. The fact that \(B_{\mathrm{st}}^{N=0}=B_{\mathrm{cris}}\) and its operator relation are polynomial calculations already given here; they do not prove the embeddings.
3. **Consequences with identified dependencies.** Lemma 1.3 proves the entire admissibility algebra under (10a); Lemma 1.4 proves strict filtered comparison, (11) and (12) under the explicitly listed period foundations. Lemma 2.2 proves finite Galois descent without any period theorem, and Lemma 2.2A proves finite-extension descent once the invariant fields are known. Proposition 3.2 constructs period matrices for **all** continuous unramified representations, including infinite image, without completed unramified descent. Thus no additional inertial-restriction theorem is being assumed for that example. Its identification as a crystalline module still depends on the crystalline structural maps and invariants. The finite-image criterion (20) has precisely the same invariant-field dependence.
4. **The Tate example.** The earlier local elliptic-curve lesson’s Lemma 3.0 supplies its actual all-characteristic uniformization proof. The argument before (24) proves the coefficient-prime torsion passage directly; Lemma 4.0 proves the logarithmic identities and residue formula with precisely the structural-series map specified in item 2. The basis, \(N\), Frobenius, filtration and direct Hodge–Tate splitting in (27)–(31) are then explicit calculations. This is a conditional period-ring calculation with a proved elliptic input, not a proof of all the general structural embeddings or of local monodromy.
5. **General geometric and local comparison.** We still owe full de Rham and Hodge–Tate comparison for smooth proper varieties, crystalline comparison for smooth proper integral models at every coefficient prime, semistable comparison, both elliptic reduction converses, and the height-two ordinary/supersingular slope classification. The full local monodromy theorem also requires the Robba-ring constructions, overconvergence and Frobenius differential-equation quasi-unipotence identified in §1. Berger’s free author manuscript states or reduces these results; it does not provide a complete proof of them. No earlier \(p\)-adic-Hodge programme lesson has been inspected that supplies them.
6. **Global geometry and modularity.** Formula (33) retains every weight \(k\ge2\), nebentypus, level and prime \(p\nmid N\). Its general integral modular models, Kuga–Sato projector, arithmetic comparison and newform pairing inputs remain unclosed in the higher-weight construction. The finite-image weight-one existence theorem is an earlier construction obligation, whereas its local consequences for any representation actually given follow from §2. The printed Kisin 2009 and March 2011 Emerton conclusions retain every hypothesis in §5. Their proofs require the deformation and completed-cohomology interfaces traced there, not supplied by our determinant normalization or the Tate example.

Fontaine–Mazur itself is explicitly a conjecture. Its general geometric realization and expected purity are not being claimed as theorems proved by this lesson. The retained theorem obligations in items 1–6 mean that this edition is **not yet a complete proof of every result it uses**. A successful formula render or a freely accessible reference cannot change that status.

## 7. Exercises, with complete solutions

**Exercise 7.1 (easy).** Compute the weights, de Rham filtration, and crystalline Frobenius of \(\mathbf Q_p(n)\), for positive, zero, and negative \(n\).

**Solution.** Equation (1) gives \(C_p\otimes\mathbf Q_p(n)=C_p(n)\), so its unique weight is \(n\), including when \(n<0\). The invariant period is \(t^{-n}e_n\), since the cyclotomic factors cancel. Multiplying by \(t^n\) shows that every invariant period is its \(\mathbf Q_p\)-multiple. Its \(t\)-adic order is \(-n\), so it belongs to \(\operatorname{Fil}^i\) precisely when \(i\le-n\). Finally \(\varphi(t)=pt\) gives eigenvalue \(p^{-n}\). For \(n=0\) all three values are respectively \(0,0,1\); for \(n=-1\) they are \(-1,1,p\). ∎

**Exercise 7.2 (medium).** Show that a finite-image local representation has all weights zero. Explain why this does not make it crystalline automatically.

**Solution.** Choose finite Galois \(L/K\) killing its action. The invariant theorem identifies the \(C_p\)-invariants with \((L\otimes V)^{\operatorname{Gal}(L/K)}\). Lemma 2.2 supplies \(\dim V\) fixed vectors forming an \(L\)-basis, hence a \(C_p\)-basis. This decomposes \(C_p\otimes V\) into \(\dim V\) copies of \(C_p(0)\), proving the assertion without a choice of eigencharacters. For \(K=\mathbf Q_p\), Theorem 3.1 gives \(\dim D_{\mathrm{cris}}(V)=\dim V^{I_p}\). A nontrivial finite ramified character has no inertia invariants, so its crystalline module is zero even though its sole Hodge–Tate weight is zero. All such finite-image representations are de Rham by (18). ∎

**Exercise 7.3 (medium).** For the Tate curve \(E_p/\mathbf Q_p\), calculate \(D_{\mathrm{cris}}\) and prove it is not crystalline.

**Solution.** Take \(u=Y\) and the basis (27). Equation (28) gives a two-dimensional semistable module with \(N(x)=0,N(y)=x\). For \(ax+by\), the image under \(N\) is \(bx\), so its kernel is exactly \(\mathbf Q_px\). Since \(B_{\mathrm{st}}^{N=0}=B_{\mathrm{cris}}\), invariants in that kernel are precisely the crystalline module, by (30). Its dimension is one, whereas \(V_pE_p\) has dimension two. This violates the crystalline dimension criterion. Its weights remain \(0,1\), as the filtration in (31) shows. ∎

**Exercise 7.4 (hard).** Explain why an irreducible even two-dimensional Artin representation is geometric, yet cannot be the representation of a holomorphic cuspidal eigenform. Give an explicit example and identify its geometric realization.

**Solution.** An Artin representation has finite image. A finite extension ramifies at finitely many primes: choose an integral primitive element, and exclude the finitely many prime divisors of its nonzero polynomial discriminant. At every remaining prime its residue polynomial has distinct roots; those roots lift uniquely in an unramified extension by the unit-derivative Newton iteration. Thus its splitting field is unramified there. Theorem 2.3 shows that every local restriction at \(p\) is de Rham with weights \(0,0\), with exactly the period-foundation dependencies of that theorem. Thus any \(p\)-adic realization over a finite coefficient field is geometric.

Finite image also has a literal geometric realization: a finite Galois extension \(L/\mathbf Q\) gives the regular permutation representation in \(H^0_{\mathrm{\acute et}}(\operatorname{Spec}L_{\overline{\mathbf Q}},E)\). It contains every irreducible representation of its Galois group after a suitable coefficient extension. To verify this, for an irreducible \(W\) choose \(0\ne w\in W\); the map from the group algebra sending \(\sum a_g g\) to \(\sum a_g g(w)\) is surjective by irreducibility. Its kernel has a stable complement: average any linear projection onto the kernel over the finite group and divide by its order, which is invertible in the characteristic-zero coefficient field. The complementary representation is \(W\). This proves the assertion for the regular representation. The variety is smooth, zero-dimensional, and projective: a finite separable field is the zero locus of its separable homogenized minimal polynomial in \(\mathbf P^1\); the leading coefficient excludes the point at infinity, and the nonzero derivative proves smoothness. Its étale \(H^0\) consists of functions on its geometric points, giving precisely that permutation action.

For a concrete rational example, take \(P(X)=X^3-4X+1\). It has no rational root, since neither \(1\) nor \(-1\) is a root; the rational-root test proves irreducibility. Its discriminant is \(256-27=229\), a nonsquare. Its splitting group is therefore the transitive subgroup \(S_3\), rather than \(A_3\). A cubic with positive discriminant has three distinct real roots: nonreal roots would form one conjugate pair, making the discriminant negative. Hence its splitting field is totally real, and complex conjugation acts trivially. The two-dimensional summand of the three-root permutation representation,
\[
\{(a,b,c)\in\mathbf Q_p^3:a+b+c=0\},
\tag{36}
\]
is absolutely irreducible. Indeed a three-cycle has two distinct primitive cube-root eigenlines after scalar extension, and a transposition interchanges them. Neither line is \(S_3\)-stable. Complex conjugation has determinant \(+1\), so the representation is even. If \(F=\mathbf Q[X]/(P)\), the permutation representation is \(H^0_{\mathrm{\acute et}}(\operatorname{Spec}F_{\overline{\mathbf Q}},\mathbf Q_p)\); its constants split off by the projection \((a,b,c)\mapsto(a+b+c)/3\). Its complementary summand is (36), realizing this example in geometry for every \(p\).

A holomorphic cuspidal newform of weight \(k\ge2\) has distinct weights \(0,k-1\), so cannot give this finite-image representation. A weight-one cusp form gives an **odd** representation by Deligne–Serre, so cannot give it either. More generally the determinant formula gives \(\det\rho_f(c)=\varepsilon(-1)(-1)^{k-1}=-1\), because \(\varepsilon(-1)=(-1)^k\). Twists do not change this parity: a one-dimensional character takes \(c\) to \(\pm1\), whose square is one in the determinant of a two-dimensional twist. This example therefore fits Fontaine–Mazur through \(H^0\), while lying outside the holomorphic cuspidal correspondence. ∎

## References

All references below point to freely accessible primary material. They document the constructions and the exact retained theorem versions; they do not discharge the obligations of §6.

- **Berger, free author manuscript:** L. Berger, [*An introduction to the theory of p-adic representations*](https://perso.ens-lyon.fr/laurent.berger/articles/article05.pdf), also [author preprint math/0210184](https://arxiv.org/abs/math/0210184); §§II.1–II.5 and IV.5.3.
- **Brinon–Conrad, free author notes:** O. Brinon and B. Conrad, [*CMI Summer School Notes on p-adic Hodge Theory*](https://math.stanford.edu/~conrad/papers/notes.pdf), preliminary version of June 24, 2009; §§4.2–4.4, Theorem 5.2.1, §§9.1–9.3, Theorems 2.2.7 and 14.3.4. Several structural proofs are expressly omitted in this version.
- **Taylor, free original article:** R. Taylor, [*Galois representations*](https://www.numdam.org/item/AFST_2004_6_13_1_73_0.pdf), 2004; §1, Conjecture 1.1, printed p.80.
- **Scholl, free author manuscript:** A. J. Scholl, [*Motives for modular forms*](https://www.dpmms.cam.ac.uk/~ajs1005/preprints/mf.pdf); Theorem 1.2.4, Remark 1.2.5, §§4.1–4.2.
- **Kisin, openly deposited printed 2009 article:** M. Kisin, [*The Fontaine–Mazur conjecture for GL₂*](https://dash.harvard.edu/entities/publication/73120378-dc24-6bd4-e053-0100007fdf3b), Harvard institutional repository; printed pp.641–690, main theorem pp.641–642. The [free author preprint](https://people.math.harvard.edu/~kisin/dvifiles/fmc.dvi) is separately available; the printed hypotheses in §5 were checked against the printed edition.
- **Emerton, free author draft:** M. Emerton, [*Local-global compatibility in the p-adic Langlands programme for GL₂/Q*](https://math.uchicago.edu/~emerton/pdffiles/lg.pdf), March 23, 2011; Theorems 1.2.3–1.2.4, Remark 1.2.5, §§7.1 and 7.3.
