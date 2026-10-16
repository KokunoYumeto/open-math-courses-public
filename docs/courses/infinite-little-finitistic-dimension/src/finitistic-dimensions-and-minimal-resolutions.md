# Finitistic dimensions and minimal resolutions

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(k\) be a field and \(A\) a finite-dimensional \(k\)-algebra. A finitely generated \(A\)-module may have a projective resolution that stops, or one that goes on forever. Bass asked how long the resolutions that stop can be [Bass]. The *little finitistic dimension* of \(A\) is
\[
\operatorname{findim}A=\sup\{\operatorname{pd}_AN:\operatorname{pd}_AN<\infty\},
\]
the supremum over finitely generated left modules \(N\); the *big finitistic dimension* \(\operatorname{Findim}A\) is the same supremum over all left modules, so \(\operatorname{findim}A\le\operatorname{Findim}A\). The *finitistic dimension conjecture* asserted that \(\operatorname{findim}A\) is finite for every finite-dimensional algebra. This course proves OpenAI's counterexample [OpenAI-FD]:

**Theorem** (OpenAI 2026). There is a finite-dimensional complex algebra \(A\) such that for every integer \(m\ge1\) some finite-dimensional left \(A\)-module \(N_m\) satisfies
\[
2m-2\le\operatorname{pd}_AN_m<\infty .
\]
In particular \(\operatorname{findim}A=\operatorname{Findim}A=\infty\).

The algebra is fixed before \(m\) varies; only the modules change. The construction has three stages. A finitely presented group algebra \(R\) carries a *selection* operation \(H\) that keeps a direct summand of a module and twists the action, and modules \(Y_m\) survive exactly \(m-1\) selections ([A selection process with unbounded extinction](a-selection-process-with-unbounded-extinction.md)). A finite-dimensional algebra \(B\) of global dimension at most two and a single bounded complex \(P\) of \(B\)-bimodules then realize the selection as a derived tensor product: \(P\otimes^{\mathbf L}_BM(Y)\) is isomorphic to \(M(H(Y))\oplus M(H(Y))[3]\) (the next four lessons). Finally an ordinary bimodule \(X\) over an algebra \(D\) of finite global dimension simulates \(P\), and the trivial extension \(A=D\ltimes X\) turns the number of nonzero iterates of the derived tensor product into projective dimension ([Simulation by an ordinary bimodule](simulation-by-an-ordinary-bimodule.md) and [Trivial extensions and unbounded projective dimension](trivial-extensions-and-unbounded-projective-dimension.md)).

This lesson proves the facts about finite-dimensional algebras that the last step uses: the radical, projective covers, minimal resolutions, and the computation of projective dimension from the derived tensor product with the semisimple quotient \(A/\operatorname{rad}A\) (Theorem 4.3).

The question has a long history, summarized in [OpenAI-FD, Section 1]. The little and big finitistic dimensions can differ, and the little one is finite for several classes of algebras, among them monomial algebras and algebras whose radical has cube zero. Cummings showed that the conjecture for all algebras is equivalent to the statement that, for every finite-dimensional algebra, finiteness on the left is equivalent to finiteness on the right [Cummings, Theorem A]. Rickard showed that \(\operatorname{Findim}\) is finite whenever the injective modules generate the derived category [Rickard, Theorem 4.3]; the last lesson uses both results. After OpenAI's manuscript, Chen constructed a ten-dimensional algebra \(A\) with \((\operatorname{rad}A)^3=0\), \(\operatorname{findim}A=2\), \(\operatorname{Findim}A=\infty\) and \(\operatorname{Findim}A^{\mathrm{op}}=0\), so the big conjecture fails already for radical cube zero [Chen].

## 1. Conventions

Algebras are associative and unital, and modules are left modules unless they are called right modules. Since \(A\) is finite-dimensional, an \(A\)-module is finitely generated exactly when it is finite-dimensional over \(k\). A *projective resolution* of a module \(N\) is an exact sequence \(\cdots\to P_1\to P_0\to N\to0\) of projective modules; it has *length* \(n\) if \(P_i=0\) for \(i>n\). The *projective dimension* \(\operatorname{pd}_AN\) is the least length of a projective resolution, or \(\infty\) if there is none of finite length. For a right module \(M\), the groups \(\operatorname{Tor}^A_i(M,N)\) are the homology groups of \(M\otimes_AP_\bullet\) for any projective resolution \(P_\bullet\) of \(N\); they do not depend on the resolution, and a short exact sequence in either variable gives a long exact sequence (core course [Category Theory and Homological Methods](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D80); [Li, *Methods of Algebra*, Volume 2, Definition–Proposition 3.14.7](https://github.com/KokunoYumeto/methods-of-algebra-volume-2-en)). In particular, if \(\operatorname{pd}_AN\le n\), then \(\operatorname{Tor}^A_i(M,N)=0\) for all \(i>n\) and all \(M\).

## 2. The radical

**Definition 2.1.** The *radical* \(J=\operatorname{rad}A\) is the intersection of all maximal left ideals of \(A\).

**Lemma 2.2.** Every simple module \(T\) is isomorphic to \(A/\mathfrak m\) for a maximal left ideal \(\mathfrak m\). The radical is the set of elements of \(A\) that annihilate every simple module; in particular it is a two-sided ideal.

**Proof.** For \(t\in T\setminus\{0\}\), the map \(A\to T\), \(a\mapsto at\), is surjective because \(At\) is a nonzero submodule of the simple module \(T\); its kernel \(\operatorname{Ann}(t)\) is a maximal left ideal, since the left ideals containing it correspond to the submodules of \(T\). So \(T\cong A/\operatorname{Ann}(t)\), and the annihilator \(\operatorname{Ann}(T)\), the intersection of the \(\operatorname{Ann}(t)\), contains \(J\). Conversely, a maximal left ideal \(\mathfrak m\) is the annihilator of the element \(1+\mathfrak m\) of the simple module \(A/\mathfrak m\), so it contains \(\operatorname{Ann}(A/\mathfrak m)\). Hence \(J\) is the intersection of the annihilators of the simple modules. Each annihilator of a module is a two-sided ideal, and so is their intersection. \(\square\)

**Lemma 2.3** (Nakayama's lemma). If \(M\) is a finitely generated module with \(JM=M\), then \(M=0\).

**Proof.** Suppose \(M\neq0\). Among the proper submodules of the finite-dimensional module \(M\), choose one, \(N\), of largest dimension. Then \(M/N\) is simple, so \(J(M/N)=0\) by Lemma 2.2, that is \(JM\subseteq N\neq M\). \(\square\)

**Lemma 2.4.** The radical is nilpotent, and it contains every nilpotent left ideal.

**Proof.** The subspaces \(J\supseteq J^2\supseteq\cdots\) of the finite-dimensional space \(A\) stabilize: \(J^{m+1}=J^m\) for some \(m\). Then \(J\cdot J^m=J^m\), and Lemma 2.3 applied to the finitely generated left module \(J^m\) gives \(J^m=0\). Let \(L\) be a left ideal with \(L^n=0\), and \(T\) a simple module. The submodule \(LT\) is \(0\) or \(T\); if it were \(T\), then \(T=LT=L^2T=\cdots=L^nT=0\). So \(LT=0\), and \(L\subseteq J\) by Lemma 2.2. \(\square\)

**Proposition 2.5.** The quotient \(A/J\) is a semisimple left \(A\)-module. For every finitely generated module \(M\), the module \(M/JM\) is semisimple, and every simple module is isomorphic to \((A/J)\bar e\) for an idempotent \(\bar e\) of \(A/J\).

**Proof.** Choose finitely many maximal left ideals \(\mathfrak m_1,\dots,\mathfrak m_r\) whose intersection has the least possible dimension. Intersecting with a further maximal left ideal cannot lower the dimension, so the intersection is contained in every maximal left ideal, and \(J=\mathfrak m_1\cap\dots\cap\mathfrak m_r\). The map \(A/J\to\bigoplus_iA/\mathfrak m_i\), \(a+J\mapsto(a+\mathfrak m_i)_i\), is injective, and its target is a direct sum of simple modules. Submodules and quotients of semisimple modules are semisimple (core course [Graduate Algebra](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D70); [Li, *Methods of Algebra*, Volume 1, Proposition 6.11.4](https://github.com/KokunoYumeto/methods-of-algebra-volume-1-en)); so \(A/J\) is semisimple, and so is every quotient of \((A/J)^n\), in particular \(M/JM\) when \(M\) is generated by \(n\) elements. A simple module \(T\) is annihilated by \(J\) (Lemma 2.2), so it is a quotient of \(A/J\); the kernel of a surjection \(A/J\to T\) has a complement \(L\cong T\) in \(A/J\) by the same proposition. Writing \(1=\bar e+\bar e'\) with \(\bar e\in L\) and \(\bar e'\) in the kernel, one finds, for \(x\in L\), that \(x=x\bar e+x\bar e'\) with \(x\bar e\in L\) and \(x\bar e'\) in the kernel, so \(x=x\bar e\). Taking \(x=\bar e\) gives \(\bar e^2=\bar e\), and \(L=(A/J)\bar e\). \(\square\)

## 3. Lifting idempotents and projective covers

**Lemma 3.1** (lifting idempotents). Let \(I\) be a two-sided ideal with \(I^n=0\), and let \(a\in A\) satisfy \(a^2-a\in I\). Then
\[
e=\sum_{j=n}^{2n-1}\binom{2n-1}{j}a^j(1-a)^{2n-1-j}
\]
is an idempotent with \(e-a\in I\).

**Proof.** The elements \(a\) and \(1-a\) commute, and \(1=(a+(1-a))^{2n-1}=e+f\) with \(f=\sum_{j=0}^{n-1}\binom{2n-1}{j}a^j(1-a)^{2n-1-j}\). Every term of \(e\) contains the factor \(a^n\), and every term of \(f\) the factor \((1-a)^n\). Hence \(ef\) is a polynomial in \(a\) times \(\bigl(a(1-a)\bigr)^n\), which lies in \(I^n=0\). So \(e=e(e+f)=e^2\). Modulo \(I\), the class \(\bar a\) is idempotent, so \(\bar a^j(1-\bar a)^{l}=0\) whenever \(j,l\ge1\); the only surviving term of \(e\) is \(\bar a^{2n-1}=\bar a\). \(\square\)

**Proposition 3.2** (projective covers). For every finitely generated module \(M\) there are a finitely generated projective module \(P\) and a surjection \(p\colon P\to M\) with \(\ker p\subseteq JP\). The map \(p\) induces an isomorphism \(P/JP\cong M/JM\); in particular \(P\neq0\) if \(M\neq0\).

**Proof.** By Proposition 2.5, \(M/JM\cong T_1\oplus\dots\oplus T_r\) with simple modules \(T_i\cong(A/J)\bar e_i\). By Lemmas 2.4 and 3.1, each \(\bar e_i\) is the class of an idempotent \(e_i\in A\). The kernel of the surjection \(Ae_i\to(A/J)\bar e_i\), \(xe_i\mapsto\bar x\bar e_i\), is \(Ae_i\cap J=Je_i\): an element \(y\in Ae_i\cap J\) satisfies \(y=ye_i\in Je_i\). So \(P=Ae_1\oplus\dots\oplus Ae_r\), a direct summand of \(A^r\), satisfies \(P/JP\cong M/JM\). Since \(P\) is projective, the composite \(P\to P/JP\cong M/JM\) lifts along the surjection \(M\to M/JM\) to a map \(p\colon P\to M\). Its image \(p(P)\) satisfies \(p(P)+JM=M\), so \(J\bigl(M/p(P)\bigr)=M/p(P)\), and \(p\) is surjective by Lemma 2.3. If \(p(x)=0\), the class of \(x\) in \(P/JP\) maps to \(0\) under the isomorphism \(P/JP\to M/JM\), so \(x\in JP\). \(\square\)

## 4. Minimal resolutions

**Definition 4.1.** A *minimal resolution* of a finitely generated module \(N\) is a projective resolution \(\cdots\xrightarrow{d_2}P_1\xrightarrow{d_1}P_0\xrightarrow{d_0}N\to0\) by finitely generated projective modules with \(\ker d_i\subseteq JP_i\) for every \(i\ge0\).

**Proposition 4.2.** Every finitely generated module has a minimal resolution.

**Proof.** Apply Proposition 3.2 to \(N\), obtaining \(d_0\colon P_0\to N\); then to the finite-dimensional module \(\ker d_0\), obtaining \(P_1\to\ker d_0\), and let \(d_1\) be its composite with the inclusion into \(P_0\); and so on. \(\square\)

In a minimal resolution, \(d_i(P_i)=\ker d_{i-1}\subseteq JP_{i-1}\) for \(i\ge1\): every differential maps into the radical of its target.

**Theorem 4.3.** Let \(S=A/J\), regarded as a right \(A\)-module, let \(N\) be finitely generated, and let \(P_\bullet\) be a minimal resolution of \(N\). Then \(\operatorname{Tor}^A_i(S,N)\cong P_i/JP_i\) for every \(i\ge0\), and
\[
\begin{aligned}
\operatorname{pd}_AN&=\sup\{i:P_i\neq0\}\\
&=\sup\{i:\operatorname{Tor}^A_i(S,N)\neq0\},
\end{aligned}
\]
with the value \(\infty\) when the set is unbounded.

**Proof.** The functor \(S\otimes_A-\) sends \(P_i\) to \(P_i/JP_i\) and sends \(d_i\) to \(0\) for \(i\ge1\), since \(d_i(P_i)\subseteq JP_{i-1}\). So the complex \(S\otimes_AP_\bullet\) has zero differentials, and \(\operatorname{Tor}^A_i(S,N)\cong P_i/JP_i\). By Lemma 2.3, \(P_i/JP_i\neq0\) exactly when \(P_i\neq0\); this proves the second equality. The minimal resolution has length \(\sup\{i:P_i\neq0\}\), so \(\operatorname{pd}_AN\) is at most this number. Conversely, if \(\operatorname{pd}_AN=n<\infty\), then \(\operatorname{Tor}^A_i(S,N)=0\) for \(i>n\) (Section 1), so \(P_i=0\) for \(i>n\). \(\square\)

**Corollary 4.4.** A finitely generated module \(N\) has finite projective dimension if and only if \(\operatorname{Tor}^A_i(A/J,N)=0\) for all sufficiently large \(i\). \(\square\)

The last lesson applies Corollary 4.4 in the form: if the complex \((A/J)\otimes^{\mathbf L}_AN\), whose cohomology in degree \(-i\) is \(\operatorname{Tor}^A_i(A/J,N)\), has bounded cohomology, then \(\operatorname{pd}_AN<\infty\).

## 5. Exercises

**Exercise 5.1** (easy). Let \(A=k[x]/(x^2)\). Show that \(\operatorname{rad}A=(x)\), that \(\cdots\xrightarrow{x}A\xrightarrow{x}A\to k\to0\) is a minimal resolution of \(k=A/(x)\), and that \(\operatorname{pd}_Ak=\infty\).

**Exercise 5.2** (medium). For \(A=k[x]/(x^2)\), show that every finitely generated module is a direct sum of copies of \(k\) and \(A\), and conclude that \(\operatorname{findim}A=0\).

**Exercise 5.3** (easy). Let \(I\) be an ideal with \(I^2=0\) and \(a^2-a\in I\). Show that Lemma 3.1 gives \(e=3a^2-2a^3\), and verify \(e^2=e\) directly.

**Exercise 5.4** (medium). Let \(A\) be the algebra of upper triangular \(2\times2\) matrices over \(k\). Find \(\operatorname{rad}A\), the two simple modules up to isomorphism, their projective covers and their projective dimensions.

**Exercise 5.5** (medium). Let \(p\colon P\to M\) and \(p'\colon P'\to M\) be as in Proposition 3.2. Show that \(P\cong P'\).

## 6. Solutions

**5.1.** The ideal \((x)\) is nilpotent, so it lies in the radical by Lemma 2.4; it is a maximal ideal because \(A/(x)\cong k\). Hence \(\operatorname{rad}A=(x)\). Multiplication by \(x\) on \(A\) has kernel and image \((x)\), and \(A\to k\) has kernel \((x)\); so the sequence is exact, and every kernel is \((x)=JA\). By Theorem 4.3, \(\operatorname{pd}_Ak=\infty\), since every \(P_i=A\) is nonzero.

**5.2.** A finitely generated \(A\)-module is a finitely generated \(k[x]\)-module on which \(x^2\) acts as \(0\). By the structure theorem over the principal ideal domain \(k[x]\) (core course [Graduate Algebra](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D70); [Li, *Methods of Algebra*, Volume 1, Theorem 6.7.8](https://github.com/KokunoYumeto/methods-of-algebra-volume-1-en)), it is a direct sum of modules \(k[x]/(f)\) with \(f\) a power of an irreducible polynomial dividing \(x^2\), that is \(k[x]/(x)=k\) or \(k[x]/(x^2)=A\). Let \(N\cong k^a\oplus A^b\). Since \(\operatorname{Tor}\) is additive, \(\operatorname{Tor}^A_i(S,N)\cong\operatorname{Tor}^A_i(S,k)^a\) for \(i\ge1\), and \(\operatorname{Tor}^A_i(S,k)\cong k\) for every \(i\) by Exercise 5.1 and Theorem 4.3. So if \(a>0\), then \(\operatorname{pd}_AN=\infty\) by Theorem 4.3. Thus every finitely generated module of finite projective dimension is free, and \(\operatorname{findim}A=0\).

**5.3.** For \(n=2\), the sum in Lemma 3.1 is \(\binom32a^2(1-a)+\binom33a^3=3a^2-2a^3\). Let \(b=a^2-a\in I\); it commutes with \(a\), and \(b^2=0\). Then \(e=a^2(3-2a)\) and \(1-e=1-3a^2+2a^3\), which is \((1-a)^2(1+2a)\), so
\[
\begin{aligned}
e(1-e)&=\bigl(a(1-a)\bigr)^2(3-2a)(1+2a)\\
&=b^2(3-2a)(1+2a)=0,
\end{aligned}
\]
that is \(e^2=e\). Moreover \(e-a=3a^2-2a^3-a=b(1-2a)\in I\), using \(a^2=a+b\) and \(a^3=a+b+ab\).

**5.4.** The strictly upper triangular matrices form a nilpotent two-sided ideal \(N\), so \(N\subseteq J\) by Lemma 2.4. The modules \(T_1\) and \(T_2\) below are simple, and a matrix that annihilates both has zero diagonal, so \(J\subseteq N\) by Lemma 2.2; hence \(J=N\). The idempotents \(e_1=\operatorname{diag}(1,0)\) and \(e_2=\operatorname{diag}(0,1)\) give the projective modules \(Ae_1\) (the first column, one-dimensional) and \(Ae_2\) (the second column, two-dimensional), with tops the two simple modules \(T_1=Ae_1\) and \(T_2=Ae_2/Je_2\). The module \(T_1\) is projective, and \(0\to Ae_1\to Ae_2\to T_2\to0\) is a minimal resolution of \(T_2\) (the kernel \(Je_2\) is isomorphic to \(Ae_1\)). So \(\operatorname{pd}T_1=0\) and \(\operatorname{pd}T_2=1\).

**5.5.** Both \(P/JP\) and \(P'/JP'\) are isomorphic to \(M/JM\). Lift \(p'\) along \(p\): projectivity of \(P'\) gives \(g\colon P'\to P\) with \(pg=p'\). The map \(g\) induces an isomorphism \(P'/JP'\to P/JP\), so \(g(P')+JP=P\), and \(g\) is surjective by Lemma 2.3. Since \(P\) is projective, \(g\) splits: \(P'\cong P\oplus\ker g\), and \(\ker g\subseteq JP'\) because \(g\) induces an isomorphism modulo the radical. Then \(\ker g=J\ker g\) as a direct summand, so \(\ker g=0\) by Lemma 2.3.

## References

- [OpenAI-FD] OpenAI, *An algebra of infinite little finitistic dimension*, OpenAI Math Release preprint, 23 September 2026. https://github.com/openai/math/tree/main/preprints/An-algebra-of-infinite-little-finitistic-dimension-September-23-2026
- [Bass] H. Bass, *Finitistic dimension and a homological generalization of semi-primary rings*, Transactions of the American Mathematical Society 95 (1960), 466–488. https://doi.org/10.1090/S0002-9947-1960-0157984-8
- [Cummings] C. Cummings, *Left-right symmetry of finite finitistic dimension*, Bulletin of the London Mathematical Society (2024); arXiv:2211.04394. https://arxiv.org/abs/2211.04394
- [Rickard] J. Rickard, *Unbounded derived categories and the finitistic dimension conjecture*, Advances in Mathematics 354 (2019); arXiv:1804.09801. https://arxiv.org/abs/1804.09801
- [Chen] L. Chen, *Big finitistic dimensions of radical-cube-zero algebras*, arXiv:2610.00433 (30 September 2026). https://arxiv.org/abs/2610.00433
- [Li] W.-W. Li, *Methods of Algebra*, Volumes 1 and 2, English edition. https://github.com/KokunoYumeto/methods-of-algebra-volume-1-en and https://github.com/KokunoYumeto/methods-of-algebra-volume-2-en
