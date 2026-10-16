# Trivial extensions and unbounded projective dimension

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The last step turns the iterates of the tensor functor \(F=X\otimes^{\mathbf L}_D-\) of [Simulation by an ordinary bimodule](simulation-by-an-ordinary-bimodule.md) into projective dimensions over one finite-dimensional algebra, the trivial extension \(A=D\ltimes X\). For a \(D\)-module \(N\) regarded as an \(A\)-module, the bar resolution splits according to the number of entries from \(X\), and
\[
D\otimes^{\mathbf L}_AN\simeq\bigoplus_{r\ge0}(F^rN)[r]
\]
(Proposition 2.2). If some iterate vanishes, \(N\) has finite projective dimension; if the \(r\)th iterate does not vanish, the projective dimension is at least \(r\) (Corollary 3.2). Applied to the modules of the earlier lessons, this proves the theorem stated in [Finitistic dimensions and minimal resolutions](finitistic-dimensions-and-minimal-resolutions.md) (Theorem 4.1). Section 5 combines it with results of Cummings and Rickard into an algebra whose finitistic dimensions are infinite on one side and zero on the other. The construction follows [OpenAI-FD, Section 6]; the splitting also follows from the graded decomposition of Minamoto and Yamaura [MY, Lemma 4.13(4) and the proof of Theorem 4.17], whose formula \(\operatorname{pd}_AN=\sup_r\{\operatorname{pd}_D(F^rN)+r\}\) [MY, Corollary 4.11] is sharper than what is needed here.

Throughout, \(k\) is a field, \(D\) a finite-dimensional \(k\)-algebra and \(X\) a finite-dimensional \(D\)-bimodule; tensor products without subscript are over \(k\).

## 1. Trivial extensions

The *trivial extension* \(A=D\ltimes X\) is the vector space \(D\oplus X\) with the product
\[
(d,x)(d',x')=(dd',\,dx'+xd').
\]
It is an associative algebra with unit \((1,0)\); the subspace \(X\) is a two-sided ideal with \(X\cdot X=0\), and \(A/X\cong D\). Every \(D\)-module is an \(A\)-module through the projection \(A\to D\), on which \(X\) acts by zero; we say that it is *inflated* from \(D\). Similarly \(D\) is a right \(A\)-module.

**Lemma 1.1.** \(\operatorname{rad}A=\operatorname{rad}D\oplus X\), and \(A/\operatorname{rad}A\cong D/\operatorname{rad}D\).

**Proof.** The ideal \(X\) is nilpotent, so it lies in every maximal left ideal of \(A\) (Lemma 2.4 of [Finitistic dimensions and minimal resolutions](finitistic-dimensions-and-minimal-resolutions.md)). Hence the maximal left ideals of \(A\) are the preimages of the maximal left ideals of \(A/X\cong D\), and their intersection is the preimage of \(\operatorname{rad}D\), which is \(\operatorname{rad}D\oplus X\). \(\square\)

## 2. The bar decomposition

**Lemma 2.1** (bar resolution). Let \(\Lambda\) be a \(k\)-algebra and \(N\) a left \(\Lambda\)-module. The complex \(\beta(N)\) with \(\beta(N)^{-n}=\Lambda\otimes\Lambda^{\otimes n}\otimes N\) for \(n\ge0\) and differential \(\partial=\sum_{i=0}^n(-1)^i\partial_i\), where \(\partial_i\) for \(i<n\) replaces the factors \(\lambda_i\otimes\lambda_{i+1}\) of \(\lambda_0\otimes\dots\otimes\lambda_n\otimes v\) by their product \(\lambda_i\lambda_{i+1}\), and \(\partial_n\) replaces \(\lambda_n\otimes v\) by \(\lambda_nv\), is a complex of free left \(\Lambda\)-modules, and \(\lambda_0\otimes v\mapsto\lambda_0v\) is a quasi-isomorphism \(\beta(N)\to N\).

**Proof.** The identities \(\partial_i\partial_j=\partial_{j-1}\partial_i\) for \(i<j\) give \(\partial^2=0\). Each term is \(\Lambda\otimes V\) for a vector space \(V\), a free module. The \(k\)-linear map \(\sigma(\lambda_0\otimes\dots\otimes v)=1\otimes\lambda_0\otimes\dots\otimes v\), together with \(\sigma(v)=1\otimes v\) on \(N\), satisfies \(\partial\sigma+\sigma\partial=\mathrm{id}\) on the augmented complex \(\cdots\to\beta(N)^{-1}\to\beta(N)^0\to N\to0\): the face \(\partial_0\sigma\) is the identity and the faces \(\partial_{i+1}\sigma\) cancel against \(\sigma\partial_i\). So the augmented complex is contractible, hence exact. \(\square\)

Let \(N\) be a left \(D\)-module inflated to \(A\). Since \(\beta(N)\) is a bounded-above complex of free left \(A\)-modules, \(D\otimes^{\mathbf L}_AN\) is computed by \(\mathcal B=D\otimes_A\beta(N)\) (core course [Category Theory and Homological Methods](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D80); [Li, *Methods of Algebra*, Volume 2, Propositions 4.12.4 and 4.12.9](https://github.com/KokunoYumeto/methods-of-algebra-volume-2-en)), with
\[
\mathcal B^{-n}=D\otimes A^{\otimes n}\otimes N,
\]
the face \(\partial_0\) using the right action of \(A\) on \(D\). Recall that \(F^rN\) denotes the \(r\)-fold derived tensor power \(X\otimes^{\mathbf L}_D\cdots\otimes^{\mathbf L}_DX\otimes^{\mathbf L}_DN\), and \(F^0N=N\).

**Proposition 2.2** (bar decomposition; OpenAI). In the derived category of left \(D\)-modules,
\[
D\otimes^{\mathbf L}_AN\simeq\bigoplus_{r\ge0}(F^rN)[r].
\]

**Proof.** *The splitting.* Write each tensor factor \(A=D\oplus X\) and expand: \(\mathcal B^{-n}\) is the direct sum of the subspaces spanned by words in which each of the \(n\) middle entries lies in \(D\) or in \(X\). Every face preserves the number of entries from \(X\) or gives zero: a product of two entries from \(D\) lies in \(D\), a product of an entry from \(D\) with one from \(X\) lies in \(X\), a product of two entries from \(X\) is zero, and an entry from \(X\) acts by zero on the leading factor \(D\) and on \(N\). So \(\mathcal B=\bigoplus_{r\ge0}\mathcal B_r\) as complexes, where \(\mathcal B_r\) is spanned by the words with exactly \(r\) entries from \(X\). In degree \(-n\) only \(r\le n\) occur, so in each degree the sum is finite, and a direct sum of quasi-isomorphisms is a quasi-isomorphism. It remains to show \(\mathcal B_r\simeq(F^rN)[r]\).

*Blocks.* A word in \(\mathcal B_r\) has the shape (2.1)
\[
\begin{gathered}
D\otimes D^{\otimes i_0}\otimes X\otimes D^{\otimes i_1}\otimes\cdots\\
\cdots\otimes X\otimes D^{\otimes i_r}\otimes N,
\end{gathered}
\]
in degree \(-n\) with \(n=r+i_0+\dots+i_r\). Call the \(i_j\) entries between the \(j\)th and \((j+1)\)st entries from \(X\) the \(j\)th *block*. Number the factors of a word from \(0\) (the leading \(D\)) to \(n\), so that the face \(\partial_m\) combines factors \(m\) and \(m+1\) (or factor \(n\) with \(N\)). The left neighbour of block \(j\) is the factor numbered \(p_j=i_0+\dots+i_{j-1}+j\), and the faces that involve block \(j\) are \(\partial_{p_j+t}\) for \(0\le t\le i_j\): face \(t\) of the block combines the left neighbour with the first entry, two consecutive entries, or the last entry with the right neighbour (the next entry from \(X\), or \(N\)). When \(r\ge1\) and \(i_j=0\), the only such face combines the two neighbours of an empty block: two entries from \(X\), an entry from \(X\) and \(N\), or the leading \(D\) and an entry from \(X\), and it is zero. The sign of face \(t\) of block \(j\) in \(\mathcal B\) is \((-1)^{p_j+t}\).

*The iterated bar complex.* For a bounded-above complex \(Z\) of left \(D\)-modules, let \(\beta_D(Z)\) be the total complex of the double complex with terms \(D\otimes D^{\otimes i}\otimes Z^q\) in bidegree \((-i,q)\), the bar differential in \(i\) and \((-1)^i\) times the differential of \(Z\) in \(q\). Only finitely many \(i\) contribute to each total degree, because \(Z\) is bounded above. Its terms are free left \(D\)-modules, and \(\beta_D(Z)\to Z\) is a quasi-isomorphism, since the augmented rows are exact by Lemma 2.1 and a row-exact double complex of this shape has exact total complex ([Li, Volume 2, Corollary 3.10.7](https://github.com/KokunoYumeto/methods-of-algebra-volume-2-en)). Hence \(X\otimes_D\beta_D(Z)\simeq X\otimes^{\mathbf L}_DZ\). Put \(Z_0=N\) and \(Z_{t+1}=X\otimes_D\beta_D(Z_t)\); by induction \(Z_t\simeq F^tN\), and \(Z_t\) is bounded above. Finally \(D\otimes_D\beta_D(Z_r)=\beta_D(Z_r)\simeq Z_r\simeq F^rN\). Unwinding the definitions, \(\beta_D(Z_r)\) has the same terms (2.1), placed in degree \(-(i_0+\dots+i_r)\), and its differential is the sum over the blocks of their bar differentials, where face \(t\) of block \(j\) carries the sign \((-1)^{t+i_0+\dots+i_{j-1}}\): the block \(j\) sits inside the bar complexes of the blocks to its left, and each of them contributes its degree to the sign.

*Comparison of signs.* The shifted complex \(\beta_D(Z_r)[r]\) has the terms (2.1) in degree \(-n\) and differential \((-1)^r\) times that of \(\beta_D(Z_r)\). So face \(t\) of block \(j\) carries the sign \((-1)^{p_j+t}=(-1)^{t+i_0+\dots+i_{j-1}+j}\) in \(\mathcal B_r\), and \((-1)^{r+t+i_0+\dots+i_{j-1}}\) in \(\beta_D(Z_r)[r]\); the two differ by \((-1)^{r-j}\). Multiply the summand (2.1) by
\[
\varepsilon(i_0,\dots,i_r)=(-1)^{\sum_{j=0}^r(r-j)i_j}.
\]
A face of block \(j\) lowers \(i_j\) by one and changes \(\varepsilon\) by the factor \((-1)^{r-j}\). Hence multiplication by \(\varepsilon\) is an isomorphism of complexes of left \(D\)-modules \(\mathcal B_r\to\beta_D(Z_r)[r]\simeq(F^rN)[r]\). For \(r=0\), \(\mathcal B_0\) is the bar complex \(\beta_D(N)\), quasi-isomorphic to \(N\). \(\square\)

## 3. Detecting projective dimension

**Lemma 3.1.** Suppose \(D\) has finite global dimension \(g\) for right modules, and let \(Z\) be a complex of left \(D\)-modules whose cohomology is finite-dimensional and concentrated in degrees \([a,0]\). Then \(X\otimes^{\mathbf L}_DZ\) has finite-dimensional cohomology concentrated in degrees \([a-g,0]\). Consequently, if \(N\) is a finite-dimensional \(D\)-module, each \(F^rN\) has finite-dimensional cohomology in degrees \([-rg,0]\).

**Proof.** If \(Z\) is a module \(V\) placed in degree \(q\), then \(X\otimes^{\mathbf L}_DV[-q]\) has cohomology \(\operatorname{Tor}^D_i(X,V)\) in degree \(q-i\); these groups vanish for \(i>g\), since \(X\) has a projective resolution of length at most \(g\) by finitely generated projective right modules, and they are finite-dimensional. In general, induct on the number of nonzero cohomology modules, using the truncation triangle that splits off the lowest one and the long exact cohomology sequence. The last statement follows by induction on \(r\). \(\square\)

**Corollary 3.2** (OpenAI). Suppose \(D\) has finite global dimension for left and for right modules, and let \(N\) be a finite-dimensional left \(D\)-module, inflated to \(A=D\ltimes X\).

1. If \(F^tN\simeq0\) for some \(t\ge1\), then \(\operatorname{pd}_AN<\infty\).
2. If \(F^rN\not\simeq0\), then \(\operatorname{pd}_AN\ge r\).

**Proof.** *1.* If \(F^tN\simeq0\), then \(F^rN\simeq0\) for all \(r\ge t\), and by Proposition 2.2 the complex \(Z=D\otimes^{\mathbf L}_AN\simeq\bigoplus_{r<t}(F^rN)[r]\) has bounded cohomology (Lemma 3.1). Let \(S=D/\operatorname{rad}D\), which by Lemma 1.1 is \(A/\operatorname{rad}A\) as a right \(A\)-module. By associativity of derived tensor products ([Li, Volume 2, Proposition 4.12.13](https://github.com/KokunoYumeto/methods-of-algebra-volume-2-en)),
\[
S\otimes^{\mathbf L}_AN\simeq S\otimes^{\mathbf L}_D\bigl(D\otimes^{\mathbf L}_AN\bigr)=S\otimes^{\mathbf L}_DZ .
\]
The right \(D\)-module \(S\) has a finite projective resolution, so \(S\otimes^{\mathbf L}_DZ\) has bounded cohomology. Its cohomology in degree \(-i\) is \(\operatorname{Tor}^A_i(A/\operatorname{rad}A,N)\), which therefore vanishes for large \(i\), and \(\operatorname{pd}_AN<\infty\) by Corollary 4.4 of [Finitistic dimensions and minimal resolutions](finitistic-dimensions-and-minimal-resolutions.md).

*2.* By Lemma 3.1 the cohomology of \(F^rN\) lies in degrees \(\le0\); choose \(q\le0\) with \(H^q(F^rN)\neq0\). The summand \((F^rN)[r]\) of Proposition 2.2 gives \(H^{q-r}(D\otimes^{\mathbf L}_AN)\neq0\), that is \(\operatorname{Tor}^A_{r-q}(D,N)\neq0\) with \(r-q\ge r\). A projective resolution of \(N\) of length less than \(r\) would make this group zero. So \(\operatorname{pd}_AN\ge r\). \(\square\)

## 4. The theorem

**Theorem 4.1** (OpenAI 2026). There is a finite-dimensional complex algebra \(A\) such that for every \(m\ge1\) a finite-dimensional left \(A\)-module \(N_m\) satisfies \(2m-2\le\operatorname{pd}_AN_m<\infty\). In particular \(\operatorname{findim}A=\operatorname{Findim}A=\infty\).

**Proof.** Work over \(k=\mathbb C\). Take the finitely presented algebra \(R\), the central idempotent \(e\) and the automorphism \(\alpha\) of Proposition 5.1 of [A selection process with unbounded extinction](a-selection-process-with-unbounded-extinction.md), with \(H(Y)={}_\alpha(eY)\). Take the algebra \(B\) of [Directed algebras and quadratic presentations](directed-algebras-and-quadratic-presentations.md) for a quadratic presentation of \(R\), and the bounded complex \(P\) of \(B\)-bimodules of Theorem 3.1 of [A bimodule complex that realizes selection](a-bimodule-complex-that-realizes-selection.md). Choose \(a_*\le0\le b_*\) as in [Simulation by an ordinary bimodule](simulation-by-an-ordinary-bimodule.md), form \(C\), \(W\), \(O\), \(T\), \(D\) and \(X\) as there, and let \(A=D\ltimes X\). All these choices are made once; none depends on \(m\).

For \(m\ge1\), let \(Y_m\) be the module of Proposition 5.1 of [A selection process with unbounded extinction](a-selection-process-with-unbounded-extinction.md), and \(N_m=M(Y_m)\), a finite-dimensional module on the first factor of \(D\), inflated to \(A\). By Corollary 3.2 of [Simulation by an ordinary bimodule](simulation-by-an-ordinary-bimodule.md),
\[
\begin{aligned}
&F^{2j}N_m\\
&\quad\simeq\bigoplus_{q=0}^j\bigl(M(H^{\circ j}(Y_m))[jb_*+3q]\bigr)^{\oplus\binom jq}.
\end{aligned}
\]
Since \(H^{\circ m}(Y_m)=0\), \(F^{2m}N_m\simeq0\). Since \(H^{\circ(m-1)}(Y_m)\neq0\), the complex \(F^{2m-2}N_m\) is a nonzero finite direct sum of shifts of the nonzero module \(M(H^{\circ(m-1)}(Y_m))\), so \(F^{2m-2}N_m\not\simeq0\). The algebra \(D\) has finite global dimension on both sides by Proposition 3.1 of [Simulation by an ordinary bimodule](simulation-by-an-ordinary-bimodule.md). Corollary 3.2 gives \(\operatorname{pd}_AN_m<\infty\) and \(\operatorname{pd}_AN_m\ge2m-2\). These lower bounds are unbounded while \(A\) is fixed, so \(\operatorname{findim}A=\infty\), and \(\operatorname{Findim}A\ge\operatorname{findim}A\). \(\square\)

Exercise 6.2 improves the lower bound to \(2m-1\).

## 5. Infinite on the left, zero on the right

Cummings attached to every basic finite-dimensional algebra \(\Gamma\) over an algebraically closed field a triangular matrix algebra
\[
\widetilde\Gamma=\begin{pmatrix}\Gamma&0\\ {}_EU_\Gamma&E\end{pmatrix},
\]
where \(E\) is a product of copies of \(k[\varepsilon]/(\varepsilon^2)\), one for each simple right \(\Gamma\)-module, and \(U\) is the direct sum of the simple right \(\Gamma\)-modules [Cummings, Construction 2.1]. *Injective modules generate* for an algebra if the smallest triangulated subcategory of the unbounded derived category of all modules that contains the injective modules and is closed under arbitrary direct sums is the whole derived category. The following statements are used as named statements; their proofs are not given in the programme (see the open obligations of this course).

- **(CUM)** [Cummings, Propositions 3.2, 3.3, 4.3 and 4.4], for right modules: \(\operatorname{findim}\Gamma\le\operatorname{findim}\widetilde\Gamma\) and \(\operatorname{Findim}\Gamma\le\operatorname{Findim}\widetilde\Gamma\); \(\operatorname{findim}\widetilde\Gamma^{\mathrm{op}}=\operatorname{Findim}\widetilde\Gamma^{\mathrm{op}}=0\); if injective modules generate for \(\widetilde\Gamma\), they generate for \(\Gamma\); and injective modules generate for \(\widetilde\Gamma^{\mathrm{op}}\).
- **(RIC)** [Rickard, Theorem 4.3], for right modules over a finite-dimensional algebra: if injective modules generate, then \(\operatorname{Findim}<\infty\).
- **(MOR)** Every finite-dimensional algebra is Morita equivalent to a basic one, and an equivalence of module categories preserves finite generation and projective dimension, and induces an equivalence of unbounded derived categories that preserves injective modules and direct sums.

**Corollary 5.1** (OpenAI, under (CUM), (RIC) and (MOR)). There is a finite-dimensional complex algebra \(\Lambda\) with
\[
\begin{gathered}
\operatorname{findim}\Lambda=\operatorname{Findim}\Lambda=\infty,\\
\operatorname{findim}\Lambda^{\mathrm{op}}=\operatorname{Findim}\Lambda^{\mathrm{op}}=0,
\end{gathered}
\]
all four for left modules; injective left \(\Lambda\)-modules do not generate, and injective right \(\Lambda\)-modules do.

**Proof.** Let \(A\) be the algebra of Theorem 4.1. Its left modules are the right modules over \(A^{\mathrm{op}}\); by (MOR) choose a basic algebra \(\Gamma\) Morita equivalent to \(A^{\mathrm{op}}\). Then the little and big finitistic dimensions of \(\Gamma\) for right modules are infinite. Injective right \(\Gamma\)-modules do not generate: otherwise (RIC) would make \(\operatorname{Findim}\Gamma\) finite. Let \(\widetilde\Gamma\) be Cummings's algebra. By (CUM), both finitistic dimensions of \(\widetilde\Gamma\) for right modules are infinite, injective right \(\widetilde\Gamma\)-modules do not generate, both finitistic dimensions of \(\widetilde\Gamma^{\mathrm{op}}\) for right modules are zero, and injective right \(\widetilde\Gamma^{\mathrm{op}}\)-modules generate. Put \(\Lambda=\widetilde\Gamma^{\mathrm{op}}\): left \(\Lambda\)-modules are right \(\widetilde\Gamma\)-modules, and left \(\Lambda^{\mathrm{op}}\)-modules are right \(\widetilde\Gamma^{\mathrm{op}}\)-modules. \(\square\)

The corollary makes no statement about the right modules of the algebra \(A\) of Theorem 4.1 itself. Chen later gave a ten-dimensional algebra with radical cube zero for which the big finitistic dimension is infinite on one side and zero on the other, while the little one is \(2\) [Chen].

## 6. Exercises

**Exercise 6.1** (easy). Let \(D=k\) and \(X=k\), so \(A=k[x]/(x^2)\). Show that Proposition 2.2 gives \(\operatorname{Tor}^A_r(k,k)\cong k\) for every \(r\ge0\), in accordance with Exercise 5.1 of [Finitistic dimensions and minimal resolutions](finitistic-dimensions-and-minimal-resolutions.md).

**Exercise 6.2** (medium). Show that \(F^{2m-1}N_m\not\simeq0\) in the proof of Theorem 4.1, and conclude \(\operatorname{pd}_AN_m\ge2m-1\).

**Exercise 6.3** (easy). Show that \(\operatorname{findim}\Lambda=\infty\) implies \(\operatorname{Findim}\Lambda=\infty\).

**Exercise 6.4** (medium). Show that the face identities \(\partial_i\partial_j=\partial_{j-1}\partial_i\) for \(i<j\) imply \(\partial^2=0\) for \(\partial=\sum(-1)^i\partial_i\).

## 7. Solutions

**6.1.** With \(D=k\), derived tensor products over \(D\) are ordinary ones, and \(F^rk=k^{\otimes r}\otimes k\cong k\) in degree \(0\). Proposition 2.2 gives \(k\otimes^{\mathbf L}_Ak\simeq\bigoplus_rk[r]\), whose cohomology in degree \(-r\) is \(k\). This agrees with the minimal resolution \(\cdots\to A\to A\to k\), whose terms have one-dimensional tops.

**6.2.** Write \(Y'=H^{\circ(m-1)}(Y_m)\neq0\). By Corollary 3.2 of [Simulation by an ordinary bimodule](simulation-by-an-ordinary-bimodule.md), \(F^{2m-2}N_m\) contains a shift of \(M(Y')\) as a direct summand, so \(F^{2m-1}N_m\) contains a shift of \(F(M(Y'))=O\otimes_BM(Y')\) (Proposition 3.1 of that lesson). This is a module, the direct sum of the \(P^n\otimes_BM(Y')\). Each \(P^n\) is a finitely generated projective right \(B\)-module. The simple right \(B\)-modules are the one-dimensional tops \(\mathbf e_iB/\mathbf e_i\operatorname{rad}B\), so by Proposition 3.2 and Exercise 5.5 of [Finitistic dimensions and minimal resolutions](finitistic-dimensions-and-minimal-resolutions.md), applied to right modules, \(P^n\) is isomorphic to its projective cover, a direct sum of copies of the \(\mathbf e_iB\); and \(\mathbf e_iB\otimes_BM(Y')\cong Y'\neq0\). Since \(P\neq0\) (it realizes the nonzero selection of any module with \(eY\neq0\), for instance \(Y_2\)), some \(P^n\neq0\), and \(F^{2m-1}N_m\not\simeq0\). Corollary 3.2 gives \(\operatorname{pd}_AN_m\ge2m-1\).

**6.3.** Finitely generated modules are modules, so the supremum defining \(\operatorname{Findim}\) is over a larger set.

**6.4.** In \(\partial^2=\sum_{i,j}(-1)^{i+j}\partial_i\partial_j\), split the pairs into \(i<j\) and \(i\ge j\). The substitution \((i,j)\mapsto(j-1,i)\) maps the first set bijectively onto the second and changes the sign \((-1)^{i+j}\) to \((-1)^{i+j-1}\); by the face identities the corresponding terms are equal, so they cancel in pairs.

## References

- [OpenAI-FD] OpenAI, *An algebra of infinite little finitistic dimension*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026
- [MY] H. Minamoto and K. Yamaura, *Homological dimension formulas for trivial extension algebras*, Journal of Pure and Applied Algebra (2020); arXiv:1710.01469. https://arxiv.org/abs/1710.01469
- [Cummings] C. Cummings, *Left-right symmetry of finite finitistic dimension*, Bulletin of the London Mathematical Society (2024); arXiv:2211.04394. https://arxiv.org/abs/2211.04394
- [Rickard] J. Rickard, *Unbounded derived categories and the finitistic dimension conjecture*, Advances in Mathematics 354 (2019); arXiv:1804.09801. https://arxiv.org/abs/1804.09801
- [Chen] L. Chen, *Big finitistic dimensions of radical-cube-zero algebras*, arXiv:2610.00433 (30 September 2026). https://arxiv.org/abs/2610.00433
- [Li] W.-W. Li, *Methods of Algebra*, Volume 2, English edition. https://github.com/KokunoYumeto/methods-of-algebra-volume-2-en
