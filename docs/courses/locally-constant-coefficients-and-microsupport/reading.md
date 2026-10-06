# Locally constant coefficients and microsupport

Tensoring a sheaf complex with a nonzero locally constant complex over a field preserves every microsupport direction. Internal Hom from that coefficient preserves them too. The coefficient may have infinite-dimensional stalks. This reading proves the statement by a local retract and works through two failures when the hypotheses change.

Original teaching text and solutions by GPT-6.1 Sol (OpenAI), Ultra, October 2026.

## Setting and prerequisites

Let $X$ be a finite-dimensional real analytic manifold and let $D^b(k_X)$ denote the bounded derived category of sheaves of modules over $k$. Tensor products are derived, and $R\mathcal Hom$ means derived internal Hom. A bounded locally constant complex is locally a constant complex $L_U$; no finite-dimensionality is implicit.

Microsupport $\operatorname{SS}(F)\subset T^*X$ is tested by local cohomology with support in the superlevel sets of differentiable functions. A covector is absent when these tests vanish uniformly for nearby points and nearby differentials. We use three standard microsupport facts: invariance under shifts, the finite direct-sum rule, and the noncharacteristic tensor and internal-Hom estimates. These estimates give the upper inclusions below for a locally constant first input, whose microsupport lies in the zero section. Their general proofs are prerequisites; this reading proves the reverse inclusions and the resulting equality.

For the exercises, a nonzero sheaf supported at one point has microsupport equal to the entire cotangent fibre there, including the zero covector. Indeed, every nonzero local support test at that point sees the same point coefficient, in every differential direction.

Equation numbers 37–39 retain their locators in the existing sheaf-operations lesson.

### The upper estimates with a locally constant first input

The precise general estimate we use is Theorem 5.2.2 of Kashiwara and Schapira's *Microlocal study of sheaves*, Astérisque 128 (1985), pp. 82–83. In its notation the operation is the limiting cotangent sum, written here as $\widehat{+}$:

$$
\operatorname{SS}(K\otimes F)
\subset \operatorname{SS}(K)\widehat{+}\operatorname{SS}(F),
\qquad
\operatorname{SS}(R\mathcal Hom(K,F))
\subset \operatorname{SS}(K)^a\widehat{+}\operatorname{SS}(F).
$$

The tensor estimate requires finite weak global dimension of the coefficient ring, which a field satisfies. The internal-Hom estimate requires a bounded first input, which is part of our hypothesis. Neither estimate imposes finite rank on that input.

Here is why the limiting operation gives the claimed upper inclusions. Put $A=\operatorname{SS}(K)$ and $B=\operatorname{SS}(F)$. The sequence criterion in Corollary 1.2.4(a), p. 18, says that a point of $A\widehat{+}B$ is witnessed in local cotangent coordinates by $(x_i;\alpha_i)\in A$, $(y_i;\beta_i)\in B$, with $x_i,y_i\to x$, $\alpha_i+\beta_i\to\xi$, and $|x_i-y_i|\,|\alpha_i|\to0$. Since $A$ lies in the zero section, every $\alpha_i=0$. Thus $(y_i;\beta_i)\to(x;\xi)$; closedness of $B$ puts the limit in $B$. The antipodal image $A^a$ has the same property. This proves both upper inclusions without replacing the limiting sum by an unjustified ordinary sum. The general tensor and internal-Hom estimates remain external prerequisites; the special zero-section reduction and the reverse inclusions are explained in this reading.

## The theorem and its proof

### Nonzero locally constant coefficients preserve microsupport over a field

**Theorem.** Suppose $k$ is a field, $X$ is connected, $K\neq0$ is bounded locally constant, and $F\in D^b(k_X)$ is arbitrary. Then

$$
\operatorname{SS}(K\otimes F)=\operatorname{SS}(F)
=\operatorname{SS}(R\mathcal Hom(K,F)).
\tag{37}
$$

Weak constructibility of $F$, finite rank of $K$, and finite dimension of its stalk modules are not needed.

**Proof.** A locally constant complex has microsupport in the zero section. The noncharacteristic tensor and Hom estimates therefore give both upper inclusions in (37), because adding the zero covector or its antipode changes no cotangent direction.

Work on a connected trivializing chart, with $K=L_U$. Connectedness and $K\neq0$ imply $L\neq0$ on every such chart: the set of points with nonzero stalk is both open and closed. Over a field, split the cycles, boundaries and their complements in a complex representing $L$. This decomposes it in the derived category as its finitely many nonzero cohomology degrees plus a contractible complex. Choose a nonzero vector in one $H^j(L)$ and split its one-dimensional span. Thus

$$
L\simeq k[-j]\oplus L',\qquad
K\otimes F|_U\simeq F|_U[-j]\oplus(L'_U\otimes F|_U),
\tag{38}
$$

and

$$
R\mathcal Hom(K,F)|_U
\simeq F|_U[j]\oplus R\mathcal Hom(L'_U,F|_U).
\tag{39}
$$

Only a decomposition into two summands was used, even when $L'$ is infinite dimensional. Microsupport is invariant under shifts and is the union for a finite direct sum: the defining support tests preserve that sum and a retract of a zero test is zero. Hence both right sides have microsupport containing $\operatorname{SS}(F|_U)$. These lower inclusions are local and glue, proving (37). A global splitting compatible with monodromy is unnecessary. $\square$

In particular, extension and coextension by any field extension $\ell/k$, including one of infinite degree, preserve the microsupport of $F$. The preceding argument applies to the nonzero locally constant $k$-complex $\ell_X$. Comparing the answer as a sheaf of $\ell$-modules or of $k$-modules gives the same microsupport: restriction of coefficients is exact and conservative and commutes with the local support tests. For a direct verification it preserves injectives, because its left adjoint $\ell\otimes_k-$ is exact; the ordinary support subfunctor has the same underlying sections in both coefficient categories. Thus its derived support tests have exactly the same vanishing.

## Exercises with complete solutions

### Connectedness ensures that a nonzero coefficient is present everywhere

*Difficulty: Introductory.*

Let $X=X_1\sqcup X_2$, with both components nonempty. Put $K=k_{X_1}$, extended by zero, and let $F=k_{\{p\}}$ for $p\in X_2$. Compute both outputs in (37).

**Solution.** This $K$ is a nonzero locally constant sheaf on the disconnected $X$. Near $X_2$ it is zero, so both its tensor with $F$ and its internal Hom into $F$ are zero there; near $X_1$, the target $F$ is zero. Hence both outputs are zero everywhere, with empty microsupport. The microsupport of $F$ is the full cotangent fibre at $p$, including its zero covector. Thus global nonvanishing of $K$ is insufficient on a disconnected space. The sufficient replacement for connectedness is that $K$ have a nonzero stalk on every component.

### A nonzero integral coefficient can erase a microsupport

*Difficulty: Intermediate.*

On $X=\mathbb R$, take $k=\mathbb Z$, $K=(\mathbb Z/p)_X$ for a prime $p$, and $F=i_*\mathbb Q$ for the point $i:\{0\}\hookrightarrow X$. Compute $K\otimes^LF$ and $R\mathcal Hom(K,F)$. Does perfection of $K$ replace the field hypothesis in (37)?

**Solution.** The finite free resolution
$[\mathbb Z\xrightarrow{p}\mathbb Z]$ of $\mathbb Z/p$, in degrees minus one and zero, makes $K$ perfect. After tensoring with $F$, multiplication by $p$ on $\mathbb Q$ is invertible, so the resulting two-term complex is acyclic. The same finite resolution calculates internal Hom into $F$, with multiplication by $p$ in the opposite cohomological degrees; it is also acyclic. Both outputs are zero. The nonzero point coefficient $F$ has the entire cotangent fibre at zero as its microsupport, so equality fails. The field proof needed a copy of the coefficient unit as a direct summand of a nonzero coefficient complex. A nonzero perfect torsion complex over $\mathbb Z$ need not contain that unit. Perfection of $K$ therefore does not substitute for the field hypothesis.

## Sources and reuse

Andreas Hohl and Pierre Schapira's [Unusual functorialities for weakly constructible sheaves](https://arxiv.org/abs/2303.11189v2), version 2 (7 January 2025), Proposition 4.12, gives the field-coefficient microsupport result. The versioned author TeX was compared for the locally constant hypothesis, arbitrary stalk dimensions and the splitting argument. For the upper estimates we use Masaki Kashiwara and Pierre Schapira's [Microlocal study of sheaves](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), Theorem 5.2.2, pp. 82–83, with the limiting-sum criterion of Corollary 1.2.4(a), p. 18. The subsection above spells out its zero-section specialization. This teaching proof makes the two-summand retract and local monodromy issue explicit; the exercises isolate the connectedness and field hypotheses.

The mathematical references are consulted and credited. Their text is not included in this bundle. This original AI teaching text, its solutions and reader code are released under CC0. The reading is an author self-checked selection from *Constructible and perverse sheaves*. Completion or independent review of the entire parent course is not claimed.

[Reading index](README.md) · [Reuse terms](LICENSE.txt) · Provenance
