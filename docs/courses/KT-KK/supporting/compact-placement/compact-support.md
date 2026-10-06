# Compact placement and support homotopy

<a id="compact-placement"></a>

**Lemma 4.3 (stable placement of compact homomorphisms).** For a homomorphism \(\theta:D\to\mathcal K(H_B)\), adjoining a zero standard-module summand does not change its ordinary homotopy class after folding the modules. Neither does conjugating it by an arbitrary module unitary of \(H_B\).

**Proof.** Work first with one fixed folding. Identify the Hilbert-space factor of \(H_B\) with \(L^2(\mathbb R_+)\), and let \(V_t\) be right translation by \(t\), with zero extension. For a compactly supported continuous vector, translation and its adjoint vary continuously in \(L^2\); density and their norm bounds give this for every vector. Thus \(V_t,V_t^*\) are strongly continuous, and \(V_t^*V_t=1\).

For an elementary compact module operator \(\theta_{f\otimes b,g\otimes c}\), conjugation gives \(\theta_{V_tf\otimes b,V_tg\otimes c}\). The rank-one norm bound makes this norm continuous. Finite sums of these operators are norm dense in \(\mathcal K(H_B)\), and conjugation is contractive. Hence
\[
t\longmapsto (V_t\otimes1)k(V_t^*\otimes1)
\tag{4.6}
\]
is norm continuous for every compact \(k\). Applying it to \(\theta(d)\) gives a pointwise norm-continuous homotopy of homomorphisms, from the original placement to a proper infinite corner at \(t=1\).

The range \(L^2([1,\infty))\) and its complement \(L^2([0,1))\) are both infinite-dimensional separable Hilbert spaces. Choose a unitary between them, and let \(W=W^*=W^{-1}\) exchange them through that unitary and its adjoint. With \(V_1\) as above, put \(V_2=WV_1\). Their ranges are orthogonal and sum to the whole Hilbert space. The norm-continuous unitary path \(\exp(i\pi s(1-W)/2)\) joins \(1\) to \(W\). Following the translation homotopy by conjugation with this path shows that placement through either \(V_1\) or \(V_2\) is homotopic to the original map. Consequently the fixed folding
\((x,y)\mapsto (V_1\otimes1)x+(V_2\otimes1)y\)
makes adjoining a zero summand harmless in either corner.

Now let \(U\) be any adjointable module unitary. The column maps
\[
R_sx=(\cos s\,x,\ \sin s\,Ux),\qquad 0\leq s\leq\pi/2,
\tag{4.7}
\]
are norm-continuous adjointable isometries, since \(R_s^*R_s=1\). Thus \(d\mapsto R_s\theta(d)R_s^*\) is a homomorphism into \(\mathcal K(H_B\oplus H_B)\), norm continuous on each \(d\). Its endpoints are the first-corner original map and the second-corner map conjugated by \(U\). Folding by the one fixed folding, and using its two corner homotopies, proves the claimed conjugation invariance. Any other folding differs from the fixed one by a module unitary, so the assertion holds for every folding. No norm-connectedness theorem for the module unitary group is used. \(\square\)

<a id="compact-support"></a>

**Lemma 4.4 (support and compact homotopy).** Suppose \(D\) is \(\sigma\)-unital and \(\theta:D\to\mathcal K(E)\), with \(E\) countably generated. Then
\[
X=\overline{\theta(D)E}
\tag{4.8}
\]
is countably generated, and \(\theta(D)\) restricts to \(\mathcal K(X)\). After standard stabilization, the original compact homomorphism and this restricted one, extended by zero, are ordinarily homotopic.

**Proof.** Choose a positive sequential approximate identity \(u_n\) of \(D\), and homogeneous generators \(x_j\) of \(E\) when grading is present. The countable family \(\theta(u_n)x_j\) generates \(X\): first approximate \(\theta(d)x\) by \(\theta(u_n)\theta(d)x\), then approximate \(\theta(d)x\) by finite \(B\)-linear combinations of the original generators. This proves countable generation, including when the inclusion \(X\subset E\) has no adjoint.

We spell out the norm used for compact inclusion. For vectors \(\xi_i,\eta_i\in X\), define the finite column operators \(C,D:B^r\to X\), or into \(E\), by those same columns. Both have adjoints given by the inner products with their columns. The finite operator \(T=CD^*\) has
\[
\|T\|^2=\|(C^*C)^{1/2}(D^*D)(C^*C)^{1/2}\|.
\]
Indeed \(T^*T=D(C^*C)D^*\), and \(\|ZZ^*\|=\|Z^*Z\|\) for \(Z=D(C^*C)^{1/2}\). The two Gram matrices are identical in \(X\) and \(E\). Therefore the rank-one inclusion extends isometrically to \(\mathcal K(X)\to\mathcal K(E)\). This argument uses no projection onto \(X\).

For \(d\in D\), approximate identities give
\[
\theta(u_n)\theta(d)\theta(u_n)\longrightarrow\theta(d)
\quad\text{in norm}.
\tag{4.9}
\]
For fixed \(n\), approximate the middle compact operator on \(E\) by finite rank sums. Sandwiching places both rank-one vectors in \(X\), since \(\theta(u_n)\) is self-adjoint and has range in \(X\). The shared norm formula proves compactness of the restriction to \(X\); norm convergence in (4.9) then proves it for \(\theta(d)\). It also gives nondegeneracy of the restricted action, because \(\theta(u_n)\xi\to\xi\) on the dense span \(\theta(D)E\) and hence on all of \(X\).

Consider the Hilbert \(C([0,1],B)\)-module
\[
\mathcal M=\{f\in C([0,1],E):f(1)\in X\}.
\tag{4.10}
\]
Use the pointwise inner product. This is a closed module and hence complete. It is generated by the constant sections of the countable family just obtained for \(X\), together with \((1-t)x_j\). Here is the density check. Approximate the endpoint value of a section by a finite \(B\)-linear combination of the constant sections. Subtract it. Continuity makes the remaining section uniformly small near \(1\), so cutoff changes it by an arbitrarily small norm. A section vanishing near \(1\) is uniformly approximated by finite sums of original generating vectors with continuous \(B\)-valued coefficients; divide those coefficients by \(1-t\) on their common support and extend by zero. Thus these sums lie in the span of \((1-t)x_j\). A scalar partition of unity supplies the finite uniform approximation from the pointwise generator property.

Evaluation at \(t<1\) has fibre \(E\), using a scalar cutoff supported away from \(1\); at \(1\) its fibre is \(X\), using constant sections. In either case its kernel is the closure of the module times coefficient functions vanishing at that point. This follows by cutting off a section whose value is zero there, then using uniform continuity. Consequently these are the actual quotient fibres, not just dense evaluation ranges.

Constant application of \(\theta(d)\) and of its adjoint preserves \(\mathcal M\). It is compact there: (4.9), followed by finite rank approximation of its middle factor, approximates it uniformly by rank-one operators whose vectors are constant sections in \(X\). The error norm on \(\mathcal M\) is at most the corresponding error on \(E\). Thus \(d\mapsto\theta(d)|_{\mathcal M}\) is a homomorphism into \(\mathcal K(\mathcal M)\), with the required original and support endpoint actions.

Apply the earlier graded stabilization theorem, Lesson 05 Theorem 6.2, over \(C([0,1],B)\):
\(\mathcal M\oplus H_{C([0,1],B)}\cong H_{C([0,1],B)}\), with the appropriate grading copies when needed. Conjugate the compact action plus zero by this module unitary. The standard compact algebra is \(C([0,1],\mathcal K(H_B))\): finite rank fields give one inclusion, and a finite interval partition and uniform finite rank approximation give the other. We have therefore obtained an ordinary pointwise norm-continuous homotopy of homomorphisms into \(\mathcal K(H_B)\). Its endpoints are exactly the two stabilized actions. Their endpoint unitary choices and zero summands are harmless by Lemma 4.3. This proves the assertion. \(\square\)


## Earlier proofs and source credit

This independent argument uses the [ordinary module receiving proofs, MF.3–MF.7](../hilbert-c-star-modules-and-morita-equivalence/hilbert-module-foundations.html#mf-003), and the full compact-module and graded stabilization proofs in [Lesson 05, Lemma 2.0 and Theorem 6.2](../../KT-KK-05.html#lemma-2-0-compact-module-operators-and-their-multipliers). Their actual free author sources are credited there. The translation/folding paths, Gram inclusion without a complement, interval quotient fibres and uniformly compact support action are proved above; these are receiving versions of the written Lemmas 4.3–4.4 of the picture lesson. Original exposition by GPT-6.1 Sol (OpenAI), Codex, Ultra, October 2026; CC0. No broader picture theorem is claimed here.
