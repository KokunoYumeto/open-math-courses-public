# Places of number fields in extensions and the product formula

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Independent full-lesson AI review is not yet recorded. Public domain (CC0).*

*NT-ADL bundled edition, source-reconciled on 5 October 2026 by GPT-6.1 Sol (OpenAI), Ultra. This adaptation retains the provider lesson's mathematical scope and adds the source comparisons identified below. The upstream provider draft is unchanged. Original AI-written exposition is CC0; human reference works and genuinely reused human expression retain their own terms.*

A number field has several ways of approaching a limit. After extending the field, a single such way can separate into several places. A tensor product records all of them at once: its field factors are precisely the completions above the chosen place. This gives local formulas for degrees, norms and traces, and turns the rational product formula into the product formula for every number field.

The prerequisites are **Extensions of complete valued fields** and **Hilbert's ramification theory in Galois extensions**. We also use the definitions and completion constructions from **Absolute values, valuations and Ostrowski's theorem** and **Completions, the p-adic numbers and complete discretely valued fields**. The earlier lessons on prime decomposition in **Algebraic number theory** provide the global ideal notation.

## 1. Places and the values used to measure them

A **place** of a field is an equivalence class of nontrivial absolute values. Equivalent values differ by a positive power and give the same topology. If \(L/K\) is an extension, the notation \(w\mid v\) means that restricting the place \(w\) to \(K\) gives the place \(v\). This is a statement about classes.

For completion and topology, choose an ordinary absolute value representing \(v\), and write \(K_v\) for the resulting complete field. An extension place can be represented with the same restriction to \(K\). For a nonarchimedean place, taking a positive power preserves the ultrametric inequality. For an archimedean place, the classification of complete archimedean fields and the unique-extension theorem give the appropriate representative. Since the restriction on \(K\) is nontrivial, that representative is unique within its equivalence class.

For a number field \(F\), product formulas use a different convention. Write \(\mathcal O_F\) for its ring of integers. For a nonzero prime ideal \(\mathfrak p\), let \(v_{\mathfrak p}:F^\times\to\mathbf Z\) be the integer-normalized valuation, and let
\[
N\mathfrak p=\#(\mathcal O_F/\mathfrak p).
\]
Define the **normalized local size** by
\[
|x|_{\mathfrak p}=(N\mathfrak p)^{-v_{\mathfrak p}(x)}.
\]
At a real place defined by \(\sigma:F\hookrightarrow\mathbf R\), set \(|x|_v=|\sigma(x)|\). At a complex place defined by the pair \(\sigma,\overline{\sigma}:F\hookrightarrow\mathbf C\), set
\[
|x|_v=|\sigma(x)|^2.
\]
All these sizes are multiplicative; put \(|0|_v=0\). A complex size does not satisfy the ordinary triangle inequality: \(|1+1|^2=4>2\). The topology at that place is the usual topology of \(\mathbf C\), defined with the unsquared modulus. Raising a size to a positive power does not change which sequences converge.

These conventions will remain separate. Sections 2–4 use ordinary absolute values for their topological arguments. Section 5 uses the normalized sizes just defined. In particular, \(w\mid v\) does not assert that the normalized size at \(w\) restricts literally to the normalized size at \(v\).

## 2. The canonical decomposition after completion

**Theorem 2.1 (tensor product and places).** Let \(L/K\) be a finite separable extension, and let \(v\) be a place of \(K\). There are finitely many places \(w\) of \(L\) above \(v\). The map
\[
\Phi:L\otimes_K K_v\longrightarrow\prod_{w\mid v}L_w,\qquad
x\otimes a\longmapsto(a x_w)_{w\mid v},
\]
where \(x_w\) is the image of \(x\) in its completion, is a canonical isomorphism of topological \(K_v\)-algebras. The tensor product carries its finite-dimensional \(K_v\)-vector-space topology; the right side carries the finite product topology.

*Proof.* Choose a primitive element \(\alpha\), with monic minimal polynomial \(f\in K[X]\). Separability persists over \(K_v\): a Bézout identity between \(f\) and \(f'\) over \(K\) remains one over \(K_v\). Consequently
\[
f=f_1\cdots f_r
\]
over \(K_v\), with the \(f_i\) distinct monic irreducible polynomials. Put
\[
E_i=K_v[X]/(f_i),\qquad \beta_i=X\bmod f_i.
\]
Each \(E_i\) is a finite extension of the complete field \(K_v\). By Theorem 1.2 of **Extensions of complete valued fields**, it is complete for the unique absolute value extending the chosen one on \(K_v\).

Sending \(\alpha\) to \(\beta_i\) defines a \(K\)-homomorphism \(L\to E_i\). It is injective because \(L\) is a field and the map sends \(1\) to \(1\). Its image is dense: every element of \(E_i\) is a polynomial in \(\beta_i\) of degree less than \(\deg f_i\), with coefficients in \(K_v\), and those coefficients can be approximated by elements of \(K\). Pulling back the absolute value gives a place \(w_i\) of \(L\), and the completion's universal property identifies
\[
L_{w_i}=E_i
\]
by an isomorphism fixing the image of \(L\) and the completed base field.

The places \(w_i\) are distinct. Indeed, if two induced absolute values are equivalent, they are equal: both restrict to the same nontrivial value on \(K\), so the power relating them must be \(1\). The identity on \(L\) would then extend to a \(K_v\)-isomorphism between \(E_i\) and \(E_j\), carrying \(\beta_i\) to \(\beta_j\). Their minimal polynomials over \(K_v\) would coincide, forcing \(f_i=f_j\).

Conversely, let \(w\mid v\). Choose its representative restricting to the chosen absolute value on \(K\). The map \(K\to L_w\) extends to an isometric embedding \(K_v\to L_w\). Inside \(L_w\), consider \(K_v(\alpha)\). This is a finite extension of \(K_v\) and hence complete. Its absolute value is the restriction of the one on \(L_w\), so it is a closed subspace of \(L_w\). It contains \(L=K(\alpha)\), which is dense in \(L_w\). Therefore
\[
L_w=K_v(\alpha).
\]
The minimal polynomial of \(\alpha\) over \(K_v\) is one of the \(f_i\). The resulting isomorphism \(E_i\to L_w\) respects absolute values by uniqueness of extension and identifies \(w\) with \(w_i\). This proves that the field factors enumerate all the places, without repetitions.

There are natural algebra identifications
\[
L\otimes_K K_v
\simeq K_v[X]/(f)
\simeq\prod_{i=1}^r K_v[X]/(f_i).
\]
The second is the Chinese remainder theorem. Its component maps evaluate \(X\) at \(\beta_i\), so, under the completion identifications, the composite is precisely \(\Phi\). The formula for \(\Phi\) also shows that it does not depend on the chosen primitive element.

It remains to check the topology. Proposition 2.1 of **Extensions of complete valued fields** says that any norm on a finite-dimensional vector space over a complete valued field is equivalent to the maximum norm in any basis. On \(\prod_i E_i\), take the maximum of the component absolute values. This is a norm over \(K_v\) and induces exactly the product topology. The tensor product has a basis norm by definition. A linear isomorphism between these finite-dimensional normed spaces is continuous with continuous inverse: in bases it and its inverse are finite matrices, whose entries give bounds for the maximum norms. Thus \(\Phi\) is a homeomorphism. \(\square\)

The formula also fixes the compatibility with the original fields. The map \(L\to L\otimes_KK_v\), \(x\mapsto x\otimes1\), becomes \(x\mapsto(x_w)_w\), and \(K_v\to L\otimes_KK_v\), \(a\mapsto1\otimes a\), becomes the diagonal completed-base embedding. Pure tensors span, so these two compatibility requirements determine the algebra map uniquely. The auxiliary primitive element describes its factors and proves that it is an isomorphism; it does not change this canonical map.

The same factorization also describes the places as \(K\)-embeddings \(L\hookrightarrow\overline{K_v}\), up to the action of \(\operatorname{Aut}(\overline{K_v}/K_v)\). An embedding chooses a root of \(f\); two roots lie in the same orbit exactly when they have the same irreducible polynomial \(f_i\) over \(K_v\). Finite separability supplies the extension of such embeddings to automorphisms of an algebraic closure.

**Corollary 2.2 (degrees, norms and traces).** In the setting of Theorem 2.1,
\[
[L:K]=\sum_{w\mid v}[L_w:K_v].
\]
For \(x\in L\), the images in \(K_v\) of its global norm and trace satisfy
\[
N_{L/K}(x)=\prod_{w\mid v}N_{L_w/K_v}(x_w),\qquad
\operatorname{Tr}_{L/K}(x)=
\sum_{w\mid v}\operatorname{Tr}_{L_w/K_v}(x_w).
\]

*Proof.* Take dimensions in Theorem 2.1. For the other identities, multiplication by \(x\) is a \(K\)-linear endomorphism of \(L\). Its determinant and trace are the norm and trace. Extending scalars to \(K_v\) leaves that matrix, determinant and trace unchanged, now viewed in \(K_v\). Under \(\Phi\), the endomorphism acts componentwise by multiplication by \(x_w\). Its matrix is block diagonal. The determinant is the product of the block determinants, and the trace is the sum of the block traces. This also covers \(x=0\). \(\square\)

## 3. Finite places and prime ideals

Now let \(L/K\) be an extension of number fields. For nonzero prime ideals \(\mathfrak P\subset\mathcal O_L\) and \(\mathfrak p\subset\mathcal O_K\), write \(\mathfrak P\mid\mathfrak p\) when \(\mathfrak P\cap\mathcal O_K=\mathfrak p\). The global ideal factorization defines \(e(\mathfrak P\mid\mathfrak p)\), and
\[
f(\mathfrak P\mid\mathfrak p)=
[\mathcal O_L/\mathfrak P : \mathcal O_K/\mathfrak p].
\]

**Proposition 3.1 (local and global ramification).** The places of \(L\) above the finite place \(\mathfrak p\) are precisely those defined by \(\mathfrak P\mid\mathfrak p\). Their completions satisfy
\[
[L_{\mathfrak P}:K_{\mathfrak p}]
=e(\mathfrak P\mid\mathfrak p)f(\mathfrak P\mid\mathfrak p).
\]
The ramification index and residue degree on the right are also the index and residue degree of this extension of complete discretely valued fields.

*Proof.* The classification of number-field places identifies every finite place of \(L\) with a nonzero prime ideal \(\mathfrak P\). An archimedean place cannot restrict to a finite one: its restriction to \(\mathbf Q\) is archimedean. The global prime-valuation identity is
\[
v_{\mathfrak P}(a)=
e(\mathfrak P\mid\mathfrak p)v_{\mathfrak p}(a)
\quad(a\in K^\times),\qquad
\mathfrak p=\mathfrak P\cap\mathcal O_K.
\]
Here \(\mathfrak p\) is nonzero, as follows from the integral extension of rings of integers. Thus the restriction has exactly the place \(\mathfrak p\). Conversely this identity shows that every prime above \(\mathfrak p\) gives an extension of that place. The number-field classification gives the asserted bijection.

Completion of a discretely valued field preserves its value group and residue field, by Theorem 2.1 of **Completions, the p-adic numbers and complete discretely valued fields**. Before completion, the valuation rings are \((\mathcal O_K)_{\mathfrak p}\) and \((\mathcal O_L)_{\mathfrak P}\), with residue fields \(\mathcal O_K/\mathfrak p\) and \(\mathcal O_L/\mathfrak P\). Therefore the two completed value groups, measured using \(v_{\mathfrak P}\), are \(\mathbf Z\) for \(L_{\mathfrak P}\) and \(e(\mathfrak P\mid\mathfrak p)\mathbf Z\) for the base. This proves the agreement of the indices, and the residue fields prove the agreement of the residue degrees. The identity \([L_{\mathfrak P}:K_{\mathfrak p}]=ef\) follows from Theorem 3.1 of **Extensions of complete valued fields**. \(\square\)

In particular, Corollary 2.2 recovers the familiar identity
\[
[L:K]=\sum_{\mathfrak P\mid\mathfrak p}
e(\mathfrak P\mid\mathfrak p)f(\mathfrak P\mid\mathfrak p).
\]
The proof uses completions and their digit bases; it needs no assumption that a chosen integral element generates the entire ring of integers.

**Example 3.2 (three behaviors for a quadratic field).** Put \(F=\mathbf Q(\sqrt2)\). At \(7\), the roots \(3\) and \(4\) of \(X^2-2\) modulo \(7\) are simple. Hensel's lemma lifts them to two roots in \(\mathbf Q_7\), and
\[
F\otimes_{\mathbf Q}\mathbf Q_7\simeq
\mathbf Q_7\times\mathbf Q_7.
\]
There are two primes above \(7\), both with \(e=f=1\).

Modulo \(3\), \(X^2-2\) is irreducible. It remains irreducible over \(\mathbf Q_3\): a root would be integral by its monic equation and would reduce to a root modulo \(3\). In \(E=\mathbf Q_3(\sqrt2)\), the reduction of \(\sqrt2\) has degree \(2\) over \(\mathbf F_3\). Hence \(f\ge2\), while \([E : \mathbf Q_3]=2=ef\); thus \(e=1,f=2\). There is one prime above \(3\), with completion \(E\).

At \(2\), \(X^2-2\) is Eisenstein. There is one completion \(\mathbf Q_2(\sqrt2)\), of degree \(2\), with \(e=2,f=1\), and \(\sqrt2\) is a uniformizer. At infinity there are two real places, since
\[
F\otimes_{\mathbf Q}\mathbf R\simeq\mathbf R\times\mathbf R.
\]

## 4. Global automorphisms seen at one place

Suppose \(L/K\) is finite Galois, with group \(G\). For a prime \(\mathfrak P\) above \(\mathfrak p\), its **decomposition group** is
\[
D_{\mathfrak P}=\{\sigma\in G\mid\sigma(\mathfrak P)=\mathfrak P\}.
\]
Its **inertia group** \(I_{\mathfrak P}\) is the kernel of the action of \(D_{\mathfrak P}\) on \(\mathcal O_L/\mathfrak P\).

**Proposition 4.1 (decomposition and inertia after completion).** The extension \(L_{\mathfrak P}/K_{\mathfrak p}\) is Galois. Every element of \(D_{\mathfrak P}\) extends uniquely to the completion, and extension gives an isomorphism
\[
D_{\mathfrak P}\xrightarrow{\sim}
\operatorname{Gal}(L_{\mathfrak P}/K_{\mathfrak p}).
\]
Its inverse is restriction to \(L\). This isomorphism identifies \(I_{\mathfrak P}\) with the inertia group of the local extension.

*Proof.* Choose \(L=K(\alpha)\), with minimal polynomial \(f\). By Theorem 2.1, \(L_{\mathfrak P}=K_{\mathfrak p}(\alpha)\) in the chosen completion. Since \(L/K\) is Galois, \(f\) is separable and all its roots belong to \(L\). The minimal polynomial of \(\alpha\) over \(K_{\mathfrak p}\) divides \(f\), and all its roots therefore belong to \(L_{\mathfrak P}\). Thus \(L_{\mathfrak P}/K_{\mathfrak p}\) is finite, separable and normal, hence Galois.

For \(\sigma\in D_{\mathfrak P}\), the identity
\[
v_{\mathfrak P}(\sigma x)=v_{\mathfrak P}(x)
\]
follows from the global prime valuation. Thus \(\sigma\) is an isometry on \(L\), extends uniquely to \(L_{\mathfrak P}\), and fixes \(K_{\mathfrak p}\) because it fixes the dense subfield \(K\). Extension respects composition. If its extension is the identity, then \(\sigma\) was already the identity on \(L\); the map is injective.

For surjectivity, take \(\tau\in\operatorname{Gal}(L_{\mathfrak P}/K_{\mathfrak p})\). The element \(\tau(\alpha)\) is a root of \(f\), and all those roots are in the embedded copy of \(L\). Normality of \(L/K\) gives a \(K\)-automorphism \(\sigma\) of \(L\) sending \(\alpha\) to \(\tau(\alpha)\). Therefore \(\tau|_L=\sigma\). Uniqueness of the absolute value on the finite extension of the complete base makes \(\tau\) an isometry. Its restriction preserves the valuation ring and maximal ideal on \(L\), so \(\sigma(\mathfrak P)=\mathfrak P\). Extension of \(\sigma\) equals \(\tau\), by agreement on dense \(L\).

Finally, completion identifies the global and local residue fields. The global action induced by \(\sigma\) and the local action induced by its extension agree on \(\mathcal O_L/\mathfrak P\); every local residue class is already represented there. Their kernels therefore coincide, which is precisely the assertion about inertia. \(\square\)

The global ramification prerequisite gives transitivity of \(G\) on the primes above a fixed \(\mathfrak p\). In particular, \(\sigma\) induces a \(K_{\mathfrak p}\)-isomorphism from \(L_{\mathfrak P}\) to \(L_{\sigma\mathfrak P}\). The same statement holds for all places, including archimedean ones; a proof is given in Solution 3.

Conjugation carries the groups accordingly:
\[
D_{\sigma\mathfrak P}=\sigma D_{\mathfrak P}\sigma^{-1},
\qquad
I_{\sigma\mathfrak P}=\sigma I_{\mathfrak P}\sigma^{-1}.
\]
Thus a prime \(\mathfrak P\) determines an actual subgroup, whereas the base prime \(\mathfrak p\) determines its conjugacy class. For fixed \(\mathfrak p\), all local degrees, ramification indices and residue degrees agree. They can change when \(\mathfrak p\) changes.

## 5. Norms and the normalized product formula

**Lemma 5.1 (relative normalization).** Let \(L/K\) be an extension of number fields, and let \(w\mid v\). For the normalized sizes of Section 1, and for every \(x\in L_w\),
\[
|x|_w=|N_{L_w/K_v}(x)|_v.
\]
In particular, for \(a\in K_v\),
\[
|a|_w=|a|_v^{[L_w:K_v]}.
\]

*Proof.* First suppose \(v\) is finite. Put \(q=\#\kappa(K_v)\), \(e=e(L_w/K_v)\), \(f=f(L_w/K_v)\), and \(n=[L_w:K_v]=ef\). Use integer-normalized additive valuations \(v_K,v_L\), so that \(v_L|_{K_v}=e v_K\) and \(\#\kappa(L_w)=q^f\).

The absolute value on \(L_w\) that restricts exactly to \(q^{-v_K}\) is \(q^{-v_L/e}\). The norm formula for that exact extension yields
\[
q^{-v_K(Nx)}=(q^{-v_L(x)/e})^n
=q^{-f v_L(x)}=(q^f)^{-v_L(x)}
\]
for \(x\ne0\), giving the first assertion. The second follows either from this computation or from \(N(a)=a^n\). Zero satisfies both identities as well.

At archimedean places the possible extensions of completed fields are \(\mathbf R/\mathbf R\), \(\mathbf C/\mathbf R\), and \(\mathbf C/\mathbf C\). The first and third have degree \(1\) and identity norm; both sides use the same real size or the same squared complex size. In the second,
\[
N_{\mathbf C/\mathbf R}(z)=z\overline z=|z|^2,
\]
exactly the complex size. For real \(a\) this becomes \(|a|^2\), as required by the degree \(2\). These exhaust the cases. \(\square\)

**Theorem 5.2 (number-field product formula).** For every number field \(F\) and every \(x\in F^\times\), all but finitely many normalized local sizes equal \(1\), and
\[
\prod_{v\text{ a place of }F}|x|_v=1.
\]

*Proof.* The nonzero fractional principal ideal \(x\mathcal O_F\) has a factorization involving finitely many prime ideals. Hence \(v_{\mathfrak p}(x)=0\) except at finitely many finite places. There are only finitely many archimedean places. The product is therefore a finite product of factors different from \(1\).

Apply Corollary 2.2 to \(F/\mathbf Q\). For each rational place \(u\), including infinity, its norm identity and Lemma 5.1 give
\[
\prod_{v\mid u}|x|_v
=\prod_{v\mid u}|N_{F_v/\mathbf Q_u}(x)|_u
=|N_{F/\mathbf Q}(x)|_u.
\]
Every place of \(F\) lies over a rational place. Grouping the finite set of nonunit factors by \(u\) yields
\[
\prod_v|x|_v
=\prod_u|N_{F/\mathbf Q}(x)|_u=1,
\]
by the rational product formula proved in Proposition 7.1 of **Absolute values, valuations and Ostrowski's theorem**. The norm is nonzero because \(x\ne0\). \(\square\)

The square at a complex place has an algebraic reason: that completion contributes two real dimensions to the norm. Replacing it by an unsquared modulus generally destroys the formula with the stated finite-place normalizations.

## 6. A cubic field at finite and infinite places

Let \(\alpha=\sqrt[3]{2}\) be the real root and \(F=\mathbf Q(\alpha)\). Its minimal polynomial is \(X^3-2\), irreducible by Eisenstein at \(2\). Modulo \(5\),
\[
X^3-2=(X-3)(X^2+3X+4).
\]
The quadratic discriminant is \(3\) modulo \(5\), a nonsquare. These distinct irreducible factors are coprime, so factor lifting gives a monic linear factor and a monic quadratic factor over \(\mathbf Z_5\). The quadratic is irreducible over \(\mathbf Q_5\). Indeed, any root would be integral by its monic equation and would contradict the irreducibility of its reduction. Thus
\[
F\otimes_{\mathbf Q}\mathbf Q_5\simeq\mathbf Q_5\times E,
\qquad [E : \mathbf Q_5]=2.
\]
The linear completion has \(e=f=1\). The quadratic root reduces to an element of degree \(2\) over \(\mathbf F_5\); the degree formula forces \(e=1,f=2\). This gives two places above \(5\), of local degrees \(1\) and \(2\).

At infinity,
\[
X^3-2=(X-\alpha)(X^2+\alpha X+\alpha^2)
\]
over \(\mathbf R\). The quadratic discriminant is \(-3\alpha^2<0\), so
\[
F\otimes_{\mathbf Q}\mathbf R\simeq\mathbf R\times\mathbf C.
\]
There is one real place and one complex place. Their local degrees \(1\) and \(2\) again add to \(3\). The real root and the conjugate pair define two places, even though the field has three embeddings into \(\mathbf C\).

## 7. Exercises

1. Evaluate every factor different from \(1\) in the product formula for \(3/10\in\mathbf Q\), and for \(1+i\in\mathbf Q(i)\).

2. For \(F=\mathbf Q(\sqrt[3]{2})\), determine all places above \(2,3,5,7\), including their local degrees, ramification indices and residue degrees. Express the corresponding ideal factorizations and compare them with prime decomposition in **Algebraic number theory**.

3. Let \(L/K\) be finite Galois and \(v\) a place of \(K\). Prove that all \(L_w\), for \(w\mid v\), are \(K_v\)-isomorphic, also when \(v\) is archimedean.

4. Reconstruct the canonical tensor-product isomorphism in Theorem 2.1. Show that its factors are exactly the completions, and prove continuity of both directions without assuming that an algebra isomorphism is automatically a homeomorphism.

## 8. Complete solutions

**Solution 1.** For \(3/10\), the integer valuations at \(2,3,5\) are \(-1,1,-1\), respectively. Thus the factors are
\[
|3/10|_\infty=3/10,\qquad
|3/10|_2=2,\qquad
|3/10|_3=1/3,\qquad
|3/10|_5=5.
\]
Every other finite factor is \(1\), and their product is \((3/10)\cdot2\cdot(1/3)\cdot5=1\).

For \(\mathbf Q(i)\), use \(\mathcal O_F=\mathbf Z[i]\). The quotient by \((1+i)\) is \(\mathbf F_2\): in the quotient \(i=-1=1\), and \(2=0\). Hence \((1+i)\) is a prime ideal of norm \(2\). The principal ideal of the element \(1+i\) is that prime to exponent \(1\), so its only nonunit finite size is \(1/2\). There is one complex place, whose normalized size is
\[
|1+i|_v=|1+i|^2=2.
\]
The product is \(2\cdot(1/2)=1\). The ring-of-integers identification here is the standard quadratic-field result from **Algebraic number theory**.

**Solution 2.** Write \(\alpha=\sqrt[3]{2}\). We compute with completions, then apply Proposition 3.1; this avoids using reduction of a defining polynomial at a bad prime without checking an integral-basis hypothesis.

At \(2\), \(X^3-2\) is Eisenstein. It is irreducible over \(\mathbf Q_2\) and gives one completion of degree \(3\), with \(e=3,f=1\). The element \(\alpha\) is a uniformizer.

At \(3\), use \(Y=\alpha+1\). Its equation is
\[
(Y-1)^3-2=Y^3-3Y^2+3Y-3.
\]
This is Eisenstein at \(3\). Thus there is again one completion, of degree \(3\), with \(e=3,f=1\). Here \(\alpha+1\) is a uniformizer; \(\alpha\) itself is a unit.

At \(5\), Section 6 gives two completions of degrees \(1\) and \(2\), with pairs \((e,f)=(1,1)\) and \((1,2)\).

At \(7\), the possible cubes modulo \(7\) are \(0,1,6\). The cubic \(X^3-2\) therefore has no root over \(\mathbf F_7\) and is irreducible there. It is irreducible over \(\mathbf Q_7\) as well: a reducible cubic over a field has a root, a root here would be integral, and its reduction would be a root modulo \(7\). In the degree-\(3\) extension generated by its root, the residue of that root has degree \(3\). The degree formula forces \(e=1,f=3\). There is one place above \(7\).

With subscripts distinguishing the two primes above \(5\), the global factorizations are consequently
\[
2\mathcal O_F=\mathfrak P_2^3,\qquad
3\mathcal O_F=\mathfrak P_3^3,\qquad
5\mathcal O_F=\mathfrak P_{5,1}\mathfrak P_{5,2},\qquad
7\mathcal O_F=\mathfrak P_7.
\]
Their prime norms are \(2,3,5,25,343\), respectively. For each rational prime, the sum of the local degrees is \(3\). These are exactly the ramification exponents and residue degrees recorded by the global prime-decomposition theorem.

**Solution 3.** Fix an algebraic closure \(\overline{K_v}\) with the unique extension of the chosen absolute value of \(K_v\). For each \(w\mid v\), embed the finite separable extension \(L_w/K_v\) into this closure. The composite gives an embedding \(\rho_w:L\hookrightarrow\overline{K_v}\) fixing \(K\), and
\[
\rho_w(L_w)=K_v\,\rho_w(L).
\]
The identity follows from the completion construction in Theorem 2.1.

Choose a primitive element of the Galois extension \(L/K\), with minimal polynomial \(f\). Its image under any \(\rho_w\) generates a copy of \(L\) containing every root of \(f\). Since \(L\) is its splitting field over \(K\), all the subfields \(\rho_w(L)\) in \(\overline{K_v}\) are the same splitting field of \(f\). Thus for two places \(w_1,w_2\) there is a \(\sigma\in G\) such that
\[
\rho_{w_2}=\rho_{w_1}\circ\sigma.
\]
The completed images \(K_v\rho_{w_1}(L)\) and \(K_v\rho_{w_2}(L)\) are equal. Both completion embeddings respect their absolute values, by unique extension from \(K_v\). The displayed identity gives
\[
|x|_{w_2}=|\sigma x|_{w_1}\quad(x\in L)
\]
for the representatives restricting exactly to the base value. Hence \(x\mapsto\sigma x\) is an isometry from \(L\) with the \(w_2\)-topology to \(L\) with the \(w_1\)-topology. It extends to a field isomorphism \(L_{w_2}\to L_{w_1}\). Its inverse is the extension of \(\sigma^{-1}\), and both fix \(K_v\) by continuity and density of \(K\). This works equally for finite and archimedean places.

It also proves transitivity on places: with the left action defined by \((\sigma w)(x)=w(\sigma^{-1}x)\), the equality of absolute values says \(w_2=\sigma^{-1}w_1\).

**Solution 4.** Take \(L=K(\alpha)\) and factor its minimal polynomial \(f\) into distinct irreducibles \(f_i\) over \(K_v\). Distinctness follows from separability and a Bézout identity for \(f,f'\). The Chinese remainder map
\[
K_v[X]/(f)\longrightarrow\prod_i E_i,\qquad
[g]\longmapsto([g]\bmod f_i)_i,\qquad
E_i=K_v[X]/(f_i),
\]
is an algebra isomorphism. The left side identifies with \(L\otimes_K K_v\).

Each \(E_i\) is complete by the finite-extension theorem, and \(L\) embeds in it by \(\alpha\mapsto[X]\). Approximating the coefficients of a polynomial in \([X]\) by elements of \(K\) proves that this image is dense. Thus \(E_i\) is the completion at the pulled-back place. If two such places were equivalent, their values would be equal by nontriviality of the common restriction, and the identity of \(L\) would extend to a \(K_v\)-isomorphism carrying one \([X]\) to the other. This would force their minimal polynomials \(f_i\) to agree.

For an arbitrary \(w\mid v\), \(K_v\) embeds in \(L_w\), and the finite complete subfield \(K_v(\alpha)\) is closed there. It contains dense \(L\), so it equals \(L_w\). The minimal polynomial of \(\alpha\) over \(K_v\) must be one of the \(f_i\). Hence there are neither extra factors nor missing places. The component map sends \(x\otimes a\) to \(a x_w\), proving the stated canonical formula.

For topology, choose a basis of \(L\) over \(K\); it gives a basis of \(L\otimes_K K_v\) and the coordinate maximum norm. Give each \(E_i\) its unique extending absolute value, and their product the maximum of these values. This is a \(K_v\)-vector-space norm and induces the finite product topology. Finite-dimensional norm equivalence over the complete base identifies it, up to bounds in both directions, with a coordinate maximum norm. In coordinate bases the Chinese remainder map is an invertible finite matrix. If its entries are \(a_{ij}\), the ordinary triangle inequality gives
\[
\max_i\left|\sum_j a_{ij}x_j\right|
\le \left(\max_i\sum_j|a_{ij}|\right)\max_j|x_j|.
\]
The inverse matrix gives a corresponding bound for the inverse. Combining these bounds with norm equivalence proves continuity both ways. In the complex case the component norms in this argument use ordinary modulus, or its ordinary absolute-value representative, rather than squared normalized size.

## Source comparison for this edition

Milne, Proposition 8.2, and Sutherland, Lecture 13, Theorem 13.5, give the completion decomposition. The proof in Section 2 identifies the actual map \(x\otimes a\mapsto(ax_w)_w\), enumerates every extension place and proves continuity in both directions. Corollary 2.2 is the determinant-and-trace calculation after scalar extension; Milne 8.4 and Sutherland, Lecture 11, Corollary 11.24, state the resulting norm and trace formulas. No assumption that \(L/K\) is Galois or that \(v\) is nonarchimedean is added to these statements.

For the Galois-group identification, Milne 8.10 and Sutherland, Lecture 11, Theorem 11.23, give the extension and restriction maps; Section 4 also checks that residue kernels agree, so that inertia is identified as well as decomposition. For the number-field product formula, Milne 8.6–8.8 and Sutherland, Lecture 13, Lemma 13.19 and Theorem 13.21, supply the same normalized local sizes. The ordinary absolute values needed for topology and the squared size at a complex place retain their distinct roles. Field-theoretic prerequisites can be read in Milne's Fields and Galois Theory, especially Corollary 3.12, Theorem 3.17 and Theorem 5.1.

## 9. What this lesson does not prove

- The construction and universal property of completions, and preservation of the value group and residue field for a discrete valuation, are Theorem 2.1 of **Completions, the p-adic numbers and complete discretely valued fields**.
- The unique absolute value on a finite extension of a complete valued field, its completeness and norm formula, finite-dimensional norm equivalence, and \([E:K]=ef\) for complete discretely valued fields are Theorem 1.2, Proposition 2.1 and Theorem 3.1 of **Extensions of complete valued fields**.
- The classification of number-field places and the rational product formula are Proposition 6.1 and Proposition 7.1 of **Absolute values, valuations and Ostrowski's theorem**. The archimedean completions are classified in Theorem 2.4 and Corollary 2.5 of **Completions, the p-adic numbers and complete discretely valued fields**.
- Hensel lifting of simple roots and coprime monic factors is Corollary 1.2 and Theorem 3.2 of **Hensel's lemma, squares and roots of unity in p-adic fields**. The Eisenstein degree and ramification assertions are Corollary 5.2 of **Extensions of complete valued fields**.
- Global fractional-ideal factorization, prime contraction, the definition of \(e,f\), and the prime-valuation restriction identity are the ideal-theoretic results in **Algebraic number theory**; precise classical locators are Milne, Chapter 3, Theorem 3.7, Lemma 3.33 and the section “Factorization in extensions.” Transitivity and global decomposition/inertia definitions are supplied by **Hilbert's ramification theory in Galois extensions**, with Sutherland, Lecture 7, Corollary 7.3 and Definitions 7.7 and 7.10, as a classical reference. Proposition 4.1 proves their identification with the local groups here.
- The primitive-element theorem, the splitting-field description of a finite Galois extension, extension of separable embeddings, and the Chinese remainder theorem are algebra prerequisites. Exact field-theoretic references are Milne, *Fields and Galois Theory*, Theorem 5.1 and Chapter 3, especially Corollary 3.12 and Theorem 3.17; the Chinese remainder theorem is Milne, *Algebraic Number Theory*, Theorem 1.14. The standard quadratic-field computation \(\mathcal O_{\mathbf Q(i)}=\mathbf Z[i]\) is Milne, Chapter 2, Example 2.41.

The tensor decomposition is the local algebra used in passing from a field extension to its adèles. The decomposition-group identification provides the local Galois group that appears in global Galois representations. The product formula supplies the normalization in the lessons on global fields and characteristic one.

The exact written global providers are in *Number fields*: lesson 1, [**Algebraic integers and rings of integers**](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-ANT/algebraic-integers-and-rings-of-integers.html), Proposition 1.2 for separable norm/trace and Theorem 1.4 for quadratic integer rings; lesson 3, **Discrete valuation rings and Dedekind domains**, Theorem 3.2 and Proposition 3.3 for fractional ideals and Chinese remainders; lesson 5, **Decomposition of primes in extensions**, Theorems 5.1–5.2 for finite integral closure, ramification and prime norms; and lesson 6, [**Hilbert's ramification theory in Galois extensions**](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-ANT/hilberts-ramification-theory-in-galois-extensions.html), Theorems 6.1–6.2 for transitivity and decomposition/inertia. A primitive element in any finite separable field extension has an open proof at [Stacks, Tag 030N](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/fields.html#fields-lemma-primitive-element). These providers, together with the preceding local lessons, supply the proof dependencies; the classical references remain attribution.

## References

J. S. Milne, [*Algebraic Number Theory*](https://www.jmilne.org/math/CourseNotes/ANT.pdf), version 3.08, Chapter 8: Propositions 8.1–8.4, Lemma 8.6, Proposition 8.7, Theorem 8.8 and Proposition 8.10.

A. V. Sutherland, MIT 18.785 Number Theory I lecture notes, Fall 2021: Lecture 7, [*Galois extensions, Frobenius elements, the Artin map*](https://math.mit.edu/classes/18.785/2021fa/LectureNotes7.pdf), Corollary 7.3 and Definitions 7.7 and 7.10; Lecture 11, [*Totally ramified extensions and Krasner's lemma*](https://math.mit.edu/classes/18.785/2021fa/LectureNotes11.pdf), Theorem 11.23 and Corollary 11.24; Lecture 13, [*Global fields and the product formula*](https://math.mit.edu/classes/18.785/2021fa/LectureNotes13.pdf), Theorem 13.5, Definition 13.17, Lemma 13.19 and Theorem 13.21.

J. S. Milne, [*Fields and Galois Theory*](https://www.jmilne.org/math/CourseNotes/FT.pdf), version 5.10 (September 2022), Chapter 3 and Theorem 5.1, for the algebraic prerequisites.
