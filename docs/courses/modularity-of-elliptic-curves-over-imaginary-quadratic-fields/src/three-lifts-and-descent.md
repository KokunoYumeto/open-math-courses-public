# Three lifts and descent

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The previous lessons supply every ingredient. Fix the parameter \(t\in U(K)\) of Proposition 4.1 of Lesson 7, chosen inside the local open sets of Lesson 6, and write \(B=B_t\), \(A=A_t\). The four systems \(V_\eta=H^1(A)\), \(V_\chi\), \(V_\psi\) and \(V_1=H^1(B)\) are linked by the congruences of Lesson 5, have the same local behaviour at the places above \(3\) and \(p\) (Lesson 6), and have absolutely irreducible, decomposed-generic residual representations at the primes where they are compared (Lesson 7). This lesson starts from the modularity of \(A\) over \(F\), moves automorphy along the three congruences with the lifting theorem, descends from \(F=K(\mu_{3p})\) to \(K\) by cyclic base change, and twists from \(B\) back to \(E\). It ends with the local parameters and with elliptic curves that have complex multiplication.

**Prerequisites.** All previous lessons of this course, in particular the results of Section 4 of [*Elliptic curves over imaginary quadratic fields and their automorphy*](elliptic-curves-over-imaginary-quadratic-fields-and-their-automorphy.md). From *The local Langlands correspondence*: [*The rank-two correspondence: principal series, Steinberg twists and characters*](course:LG-LLC/LG-LLC-06). From *Galois representations*: [*Frobenius elements and determination by traces*](course:LG-GAL/frobenius-elements-and-determination-by-traces).

## 1. Moving between coefficient primes

The embeddings \(j_\ell\colon\overline{\mathbb Q}\to\overline{\mathbb Q}_\ell\) and isomorphisms \(\iota_\ell\colon\overline{\mathbb Q}_\ell\to\mathbb C\) of Lesson 5 satisfy \(\iota_\ell\circ j_\ell=\iota_0\), the fixed complex embedding of \(\overline{\mathbb Q}\).

**Lemma 1.1 (transport).** Let \(\pi\) be a cuspidal representation of \(\mathrm{GL}_2(\mathbb A_F)\), regular algebraic of weight zero, and suppose \(r_{\iota_\ell}(\pi)\cong V_{\theta,\ell}\) for one prime \(\ell\). Then for every prime \(\ell'\):

1. \(r_{\iota_{\ell'}}(\pi)\) and \(V_{\theta,\ell'}\) have isomorphic semisimplifications;
2. if \(\overline V_{\theta,\ell'}\) is absolutely irreducible, then \(r_{\iota_{\ell'}}(\pi)\cong V_{\theta,\ell'}\).

**Proof.** Let \(v\) be a place of \(F\) outside the finite set \(S\) of Proposition 4.2 of Lesson 5, not above \(\ell\) or \(\ell'\), at which \(\pi_v\) is unramified. By Proposition 4.2(3) of Lesson 5, the characteristic polynomial of \(\operatorname{Frob}_v\) on \(V_{\theta,\lambda}\) is \(j_\lambda(P_v)\) for a polynomial \(P_v\in M[T]\) independent of \(\lambda\). By Theorem 2.2 of Lesson 1, that on \(r_{\iota_\lambda}(\pi)\) is \(\iota_\lambda^{-1}(Q_v)\), where \(Q_v\in\mathbb C[T]\) is the characteristic polynomial of \(\operatorname{rec}^T_{F_v}(\pi_v)(\operatorname{Frob}_v)\). The isomorphism at \(\ell\) gives \(j_\ell(P_v)=\iota_\ell^{-1}(Q_v)\), so \(Q_v=\iota_0(P_v)\). At \(\ell'\) we obtain \(\iota_{\ell'}^{-1}(Q_v)=j_{\ell'}(P_v)\): the two representations have the same characteristic polynomials of Frobenius at almost all places. By the Chebotarev density theorem and the Brauer–Nesbitt theorem (Theorem 4.2 of [*Frobenius elements and determination by traces*](course:LG-GAL/frobenius-elements-and-determination-by-traces)), their semisimplifications are isomorphic. If \(\overline V_{\theta,\ell'}\) is absolutely irreducible, then \(V_{\theta,\ell'}\) is irreducible (Lemma 1.1 of Lesson 1), and \(r_{\iota_{\ell'}}(\pi)\) is semisimple by definition, so both equal their common semisimplification. \(\square\)

Part (2) is where the semisimplicity of \(V_{\theta,\ell'}\) is obtained from residual irreducibility rather than from Faltings' theorem (Remark 4.3 of Lesson 5).

**Lemma 1.2 (local automorphic conditions).** Let \(\pi\) be a cuspidal representation of \(\mathrm{PGL}_2(\mathbb A_F)\), regular algebraic of weight zero, with \(r_{\iota_\ell}(\pi)\cong V_{\theta,\ell}\) for some \(\ell\). Let \(l\in\{3,p\}\), \(v\mid l\) a place of \(F\), and \(J_t=\operatorname{Jac}(C_n(t))\).

1. If \(J_t\) has potentially good reduction at \(v\), then \(\operatorname{rec}_{F_v}(\pi_v)\) has zero monodromy.
2. If \(J_t\) acquires semistable reduction of toric rank \(n\) at \(v\), then \(\pi_v\) is the twist of the Steinberg representation by a character of order at most two, and \(\pi\) is \(\iota_l\)-ordinary of weight zero at \(v\).

**Proof.** Choose a coefficient prime \(a\ne l\). By Lemma 1.1(1), \(r_{\iota_a}(\pi)\) and \(V_{\theta,a}\) have isomorphic semisimplifications, so their restrictions to \(G_{F_v}\) do too, and so do the Weil representations of their Weil–Deligne representations after semisimplification. By (2.3) of Lesson 1 (Varma's theorem), the semisimplified Weil–Deligne representation of \(r_{\iota_a}(\pi)|_{G_{F_v}}\) is \(\iota_a^{-1}\operatorname{rec}^T_{F_v}(\pi_v)^{\mathrm{ss}}\). So the Weil representation underlying \(\operatorname{rec}^T_{F_v}(\pi_v)\) is, up to semisimplification, that of \(V_{\theta,a}|_{G_{F_v}}\). Monodromy operators are not compared in this step.

(1) Over a finite extension \(L/F_v\) the Jacobian has good reduction, so \(V_{\theta,a}|_{G_L}\) is unramified, and by Weil's theorem (Theorem 2.2 of Lesson 6) both eigenvalues of a Frobenius of \(L\) on it have complex absolute value \(Q_L^{1/2}\), where \(Q_L\) is the order of the residue field of \(L\). Suppose \(\operatorname{rec}^T_{F_v}(\pi_v)\) had nonzero monodromy. A two-dimensional Weil–Deligne representation with nonzero monodromy is a twist of the special one, with Weil part \(\mu\oplus\mu|\cdot|\) for a character \(\mu\). Restricted to the Weil group of \(L\), the two Frobenius eigenvalues of this Weil part differ by the factor \(Q_L^{\pm1}\), so their absolute values differ, while those of \(V_{\theta,a}|_{G_L}\) agree. This contradicts the equality of semisimplified Weil representations. Hence \(\operatorname{rec}^T_{F_v}(\pi_v)\), and with it \(\operatorname{rec}_{F_v}(\pi_v)\), which differs by a twist, has zero monodromy.

(2) By Corollary 6.1(3) of Lesson 6, \(V_{\theta,a}|_{G_{F_v}}\) has monodromy of rank one, so its semisimplified Weil representation is \(\mu\oplus\mu|\cdot|\) for a character \(\mu\) of the Weil group: two characters differing by the norm. A two-dimensional Weil–Deligne parameter with this Weil part either is the special parameter, with nonzero monodromy, or has zero monodromy. Under the local Langlands correspondence for \(\mathrm{GL}_2\) (Section on Steinberg twists of [*The rank-two correspondence*](course:LG-LLC/LG-LLC-06)), the first corresponds to a twist of the Steinberg representation and the second to a one-dimensional representation, which is not generic. Local components of cuspidal representations are generic (Lemma 2.1 of Lesson 1 and its proof), so \(\pi_v\cong\mathrm{St}\otimes(\nu\circ\det)\) for a character \(\nu\). Its central character \(\nu^2\) is trivial, so \(\nu\) has order at most two. The last assertion of Theorem 4.3 of Lesson 1 then shows that \(\pi\) is \(\iota_l\)-ordinary of weight zero at \(v\). \(\square\)

## 2. The three lifts

**Proposition 2.1.** The elliptic curve \(B/F\) is modular: \(H^1(B)\) is realized by a cuspidal representation of \(\mathrm{PGL}_2(\mathbb A_F)\) that is regular algebraic of weight zero.

**Proof.** *Starting point.* By Proposition 5.2(3) of Lesson 5, \(V_\eta=H^1(A)\). By Proposition 4.1 of Lesson 7, \(A\) has no complex multiplication, and its mod-\(5\) representation \(\overline V_{\eta,5}\) is absolutely irreducible on \(G_{F(\zeta_5)}\) and decomposed generic (the pair \((m,\ell)=(3,5)\)). Since \(\zeta_5\notin F\) (Exercise 6.1 of Lesson 1), Theorem 4.2 of Lesson 1 gives a cuspidal representation \(\pi_0\) of \(\mathrm{PGL}_2(\mathbb A_F)\), regular algebraic of weight zero, realizing \(V_{\eta,5}\).

*The lifts.* Apply Theorem 4.1 of Lesson 1 three times:

- Step 1: the automorphic input \(\pi_0\) realizes \(V_\eta\); the prime is \(p\), the system lifted is \(V_\chi\), and the residual input is the pair \((3,p)\).
- Step 2: the automorphic input \(\Pi_1\) realizes \(V_\chi\); the prime is \(3\), the system lifted is \(V_\psi\), and the residual input is the pair \((p,3)\).
- Step 3: the automorphic input \(\Pi_2\) realizes \(V_\psi\); the prime is \(p\), the system lifted is \(V_1=H^1(B)\), and the residual input is \(H^1(B)\bmod p\).

In each step, let \(l\) be the prime and \(r=V_{\theta,l}\) the system lifted. The hypotheses of Theorem 4.1 of Lesson 1 hold for the following reasons.

- \(l\in\{3,p\}\) is odd and different from \(5\).
- \(r\) is unramified outside finitely many places, with \(\det r=\epsilon_l^{-1}\), and potentially semistable with labelled Hodge–Tate weights \(\{0,1\}\) at every \(v\mid l\) (Proposition 4.2 of Lesson 5).
- \(\bar r\) is absolutely irreducible on \(G_{F(\zeta_l)}=G_F\) and decomposed generic (Proposition 4.1 of Lesson 7): \(\zeta_l\in F\) since \(l\mid3p\). In step 1, \(\bar r=\overline V_{\chi,p}\cong\overline V_{\eta,p}\); in step 2, \(\bar r=\overline V_{\psi,3}\); in step 3, \(\bar r=\overline V_{1,p}\).
- The input \(\pi\) of the step is cuspidal on \(\mathrm{PGL}_2(\mathbb A_F)\), regular algebraic of weight zero. It realizes the previous system at \(l\): by Lemma 1.1(2), automorphy at the previous prime transports to \(l\), because the residual representation of the previous system at \(l\) is absolutely irreducible, being isomorphic to \(\bar r\) by the congruences of Corollary 6.2 of Lesson 5. Hence \(\overline{r_{\iota_l}(\pi)}\cong\bar r\).
- At each \(v\mid l\), by Corollary 6.1 of Lesson 6 the representation \(r|_{G_{F_v}}\) and the previous system have the same type. If \(E\) has potentially good ordinary reduction at \(v\), both are potentially crystalline and potentially ordinary of weight zero; if potentially good supersingular, both are potentially crystalline and neither is potentially ordinary; in these two cases \(\operatorname{rec}_{F_v}(\pi_v)\) has zero monodromy by Lemma 1.2(1), so alternative (1) of Theorem 4.1 holds. If \(E\) has potentially multiplicative reduction at \(v\), neither is potentially crystalline and \(\pi\) is \(\iota_l\)-ordinary of weight zero at \(v\) by Lemma 1.2(2), so alternative (2) holds.

The theorem gives a cuspidal representation of \(\mathrm{PGL}_2(\mathbb A_F)\), regular algebraic of weight zero, realizing \(r\); call it \(\Pi_1\), \(\Pi_2\), \(\Pi_3\) in the three steps. It is again an admissible input for the next step. The last step gives \(H^1(B)\cong r_{\iota_p}(\Pi_3)\). \(\square\)

## 3. Descent to \(K\)

We use two theorems on \(\mathrm{GL}_2\) over number fields.

**Theorem 3.1 (named result N3: base change and multiplicity one).** Let \(L'/L\) be a cyclic extension of number fields of prime degree with Galois group \(\langle\sigma\rangle\).

1. (Strong multiplicity one.) Two isobaric automorphic representations of \(\mathrm{GL}_2(\mathbb A_L)\) whose local components agree at almost all places are isomorphic [Lan, Lemma 3.1].
2. (Cyclic base change.) Every automorphic representation \(\pi\) of \(\mathrm{GL}_2(\mathbb A_L)\) has a unique lifting \(\operatorname{BC}(\pi)\) to \(\mathrm{GL}_2(\mathbb A_{L'})\), and a cuspidal representation \(\Pi\) of \(\mathrm{GL}_2(\mathbb A_{L'})\) is a lifting if and only if \(\Pi^\sigma\cong\Pi\). The central character of \(\operatorname{BC}(\pi)\) is that of \(\pi\) composed with the norm. Liftings are compatible with the local liftings at every place; at a place \(v\) that splits completely, the local lifting of \(\pi_v\) is \(\pi_v\) at every place above \(v\); at a place where \(L'/L\) and \(\pi_v\) are unramified, it is the unramified representation whose Satake parameter is the appropriate power of that of \(\pi_v\). The lifting of an isobaric sum of two characters is the isobaric sum of the two characters composed with the norm [Lan, Chapter 2, properties A)–F) of global liftings and a)–g) of local liftings].
3. (Automorphic induction.) Let \(L'/L\) be quadratic and \(\psi\) a Hecke character of \(L'\) that does not factor through the norm to \(L\). Then the representation of \(\mathrm{GL}_2(\mathbb A_L)\) whose local components correspond, under the local Langlands correspondence, to the local components of the parameter induced from \(\psi\) is cuspidal automorphic [JL, Proposition 12.1].

The course uses these results without proof.

**Lemma 3.2 (cyclic descent).** Let \(L'/L\) be a cyclic extension of CM fields of prime degree, and \(r\colon G_L\to\mathrm{GL}_2(\overline{\mathbb Q}_\ell)\) a continuous representation whose restriction to \(G_{L'}\) is absolutely irreducible. If \(r|_{G_{L'}}\) is realized by a cuspidal representation \(\Pi\) of \(\mathrm{GL}_2(\mathbb A_{L'})\), regular algebraic of weight zero, then \(r\) is realized by a cuspidal representation of \(\mathrm{GL}_2(\mathbb A_L)\), regular algebraic of weight zero.

**Proof.** For \(\sigma\in\operatorname{Gal}(L'/L)\), the representations \(\Pi^\sigma\) and \(\Pi\) have the same local components at almost all places, because their Galois representations are \(r|_{G_{L'}}\) and its conjugate by a lift of \(\sigma\), which is isomorphic to it since \(r\) is defined on \(G_L\). By strong multiplicity one, \(\Pi^\sigma\cong\Pi\). By cyclic base change, \(\Pi=\operatorname{BC}(\pi)\) for an automorphic \(\pi\); it is cuspidal, because the lifting of an isobaric sum of characters is not cuspidal. Every archimedean place of the CM field \(L\) is complex and splits completely in \(L'\), so \(\pi_v\cong\Pi_w\) for \(w\mid v\), and \(\pi\) is regular algebraic of weight zero.

At almost all places, compatibility of base change with unramified local liftings and Theorem 2.2 of Lesson 1 show that \(r_\iota(\pi)|_{G_{L'}}\) and \(r|_{G_{L'}}\) have the same Frobenius characteristic polynomials, so \(r_\iota(\pi)|_{G_{L'}}^{\mathrm{ss}}\cong r|_{G_{L'}}\) by Chebotarev and Brauer–Nesbitt. The right side is absolutely irreducible, so the left side is already irreducible and \(r_\iota(\pi)|_{G_{L'}}\cong r|_{G_{L'}}\). Fix such an isomorphism. For \(g\in G_L\), the matrices of \(r_\iota(\pi)(g)\) and \(r(g)\) induce the same conjugation on the absolutely irreducible representation of \(G_{L'}\), so they differ by a scalar \(\delta(g)\), by Schur's lemma. Then \(\delta\) is a character of \(G_L\) trivial on \(G_{L'}\), and \(r_\iota(\pi)\cong r\otimes\delta\). By class field theory, \(\delta^{-1}\) corresponds to a finite-order Hecke character \(\omega\) of \(L\); twisting \(\pi\) by \(\omega\circ\det\) preserves cuspidality and weight zero, and \(r_\iota(\pi\otimes\omega\circ\det)\cong r\), by comparison of Frobenius polynomials at good places and Lemma 1.1 of Lesson 1. \(\square\)

**Proposition 3.3.** Let \(E/K\) have no complex multiplication. There is a cuspidal representation \(\pi_E\) of \(\mathrm{GL}_2(\mathbb A_K)\), regular algebraic of weight zero, with \(r_{\iota_p}(\pi_E)\cong H^1(E)\).

**Proof.** The extension \(F/K\) is abelian, so there is a chain \(K=L_0\subset L_1\subset\cdots\subset L_s=F\) with each \(L_{i+1}/L_i\) cyclic of prime degree. Each \(L_i\) is abelian over \(\mathbb Q\) and contains \(K\), so it is a CM field (Exercise 6.1 of Lesson 1). The representation \(H^1(B,\overline{\mathbb Q}_p)\) is absolutely irreducible on \(G_F\), since its residual representation is (Lemma 2.1 of Lesson 7), hence on every \(G_{L_i}\). Applying Lemma 3.2 down the chain to Proposition 2.1 gives a cuspidal representation of \(\mathrm{GL}_2(\mathbb A_K)\), regular algebraic of weight zero, realizing \(H^1(B)\). The curve \(B\) is the quadratic twist of \(E\) by \(h(t)\): \(H^1(E)\cong H^1(B)\otimes\kappa\), where \(\kappa\) is the quadratic character of \(K(\sqrt{h(t)})/K\). Let \(\omega\) be the corresponding quadratic Hecke character; twisting by \(\omega\circ\det\) gives \(\pi_E\) with \(r_{\iota_p}(\pi_E)\cong H^1(E)\), by comparison at good places and Lemma 1.1 of Lesson 1, since \(H^1(E)\) is absolutely irreducible at \(p\). \(\square\)

## 4. Local parameters, and complex multiplication

**Proof of Theorem 3.1 of Lesson 1 for \(E\) without complex multiplication.** By Proposition 3.3 and Theorem 4.3 of Lesson 1, \(\pi_E\) has weight zero and trivial central character, realizes \(H^1(E)\) for every prime \(\ell\) and every \(\iota\), and has the Frobenius-semisimplified local parameters \(\iota\,\mathrm{WD}(H^1(E)|_{G_{K_v}})^{\mathrm{F\text{-}ss}}\cong\operatorname{rec}^T_{K_v}(\pi_{E,v})\) at every finite \(v\nmid\ell\). Given \(v\), choosing \(\ell\) prime to \(v\) shows that every finite local \(L\)-factor of \(E\) is that of \(\pi_E\) shifted by \(\frac12\). At the complex place \(\pi_E\) is generic of weight zero, so its parameter is (2.1) of Lesson 1, which gives the archimedean factor. Hence \(L(E/K,s)=L(\pi_E,s-\frac12)\). \(\square\)

The local statement also holds with the Weil–Deligne representation attached by \(p\)-adic Hodge theory at a place above \(p=\ell\): for good reduction this follows from the crystalline comparison (Theorem 4.2(3) of Lesson 6), and in the other cases from the description of the reduction types in Lesson 6. The course does not use this.

For elliptic curves with complex multiplication we use the following.

**Theorem 4.1 (named result N9: complex multiplication).** Let \(E/K\) be an elliptic curve with complex multiplication by an imaginary quadratic field \(M\). Its endomorphisms are defined over \(KM\), and the restriction of \(H^1(E)\) to \(G_{KM}\) is the sum of the \(\ell\)-adic realizations of two algebraic Hecke characters \(\psi,\psi'\) of \(KM\), conjugate under \(\operatorname{Gal}(KM/K)\) when \(M\ne K\), with infinity types given by the CM type. This is the main theorem of complex multiplication (Deuring; Shimura and Taniyama) [MilneCM, Theorem 10.1]. The course uses it without proof.

**Proof of Theorem 3.1 of Lesson 1 for \(E\) with complex multiplication.** The endomorphisms act faithfully on invariant differentials, through \(M\), and \(G_{KM}\) fixes them, so they are defined over \(KM\).

If \(M\not\subseteq K\), then \(KM/K\) is quadratic, the nontrivial element exchanges \(\psi\) and \(\psi'\), and \(H^1(E)\) is induced from \(\psi\). The character \(\psi\) does not factor through the norm to \(K\), because its infinity type is not invariant under conjugation. By Theorem 3.1(3), the representation of \(\mathrm{GL}_2(\mathbb A_K)\) attached to the induced parameter is automorphic (indeed cuspidal), with local components given by the local correspondence at every place. If \(M=K\), take the isobaric sum of the two characters. In either case twist by \(|\det|^{1/2}\) so that the Tate-normalized parameters realize \(H^1(E)\). The central character is trivial: the determinant of \(H^1(E)\) is \(\epsilon_\ell^{-1}\), so after removing the Tate normalization the local parameters have determinant one. The finite local parameters and the infinity types are given by the theory of complex multiplication and local class field theory, with local compatibility of the induction in the first case. These are the alternatives stated in Theorem 3.1 of Lesson 1. \(\square\)

Together, the two cases prove Theorem 3.1 of Lesson 1: every elliptic curve over an imaginary quadratic field is modular, with matching local parameters at every place.

## 5. Exercises

**5.1.** In Lemma 1.1, show by an example why part (2) needs residual irreducibility: give two non-isomorphic two-dimensional \(\ell\)-adic representations of a profinite group with the same characteristic polynomials.

**5.2.** Show that the Steinberg representation twisted by a character \(\nu\) has central character \(\nu^2\), and deduce that in Lemma 1.2(2) only the four characters with \(\nu^2=1\) can occur.

**5.3.** Explain why the descent in Proposition 3.3 needs the residual representation of \(H^1(B)\) to be absolutely irreducible on \(G_F\), not only on \(G_K\).

**5.4.** Let \(E\) have complex multiplication by \(M\ne K\). Show that the representation \(H^1(E)\) of \(G_K\) is irreducible but becomes reducible on \(G_{KM}\). Why does the course treat this case separately from the prime switch?

## 6. Solutions

**5.1.** Let \(G=\mathbb Z_\ell\) with generator \(\gamma\), and let \(\rho_1(\gamma)=\left(\begin{smallmatrix}1&1\\0&1\end{smallmatrix}\right)\) and \(\rho_2(\gamma)=\left(\begin{smallmatrix}1&0\\0&1\end{smallmatrix}\right)\), extended continuously. Both have characteristic polynomial \((T-1)^2\) at every element, but \(\rho_1\) is not semisimple and \(\rho_1\not\cong\rho_2\). Their reductions both have trivial semisimplification, which is reducible. With an absolutely irreducible residual representation, the representation is irreducible and determined by its characteristic polynomials.

**5.2.** The Steinberg representation is a subquotient of the representation induced from \(|\cdot|^{1/2}\otimes|\cdot|^{-1/2}\), on which the centre acts by \(|z|^{1/2}|z|^{-1/2}=1\). Twisting by \(\nu\circ\det\) multiplies the central character by \(\nu(\det(z\cdot1))=\nu(z)^2\). So the central character is \(\nu^2\), trivial exactly when \(\nu^2=1\). The characters of order at most two of a local field \(F_v\) of odd residue characteristic correspond to the four classes of \(F_v^\times/F_v^{\times2}\), by local class field theory; for residue characteristic two there are more, and the argument does not need to count them.

**5.3.** Lemma 3.2 is applied to each step \(L_{i+1}/L_i\) of the chain, and needs absolute irreducibility on the larger group \(G_{L_{i+1}}\), in particular on \(G_F\) at the first step. Absolute irreducibility on \(G_K\) would not prevent the restriction to \(G_F\) from becoming reducible; Schur's lemma is used for the subgroup \(G_{L_{i+1}}\).

**5.4.** On \(G_{KM}\) the representation is the sum of two characters by Theorem 4.1, so it is reducible there. An element of \(G_K\setminus G_{KM}\) exchanges the two character spaces, because it acts on the endomorphisms by the nontrivial automorphism of \(M\); so no line is stable under \(G_K\), and \(H^1(E)\) is irreducible on \(G_K\). The prime switch needs a large residual image at \(p\) (Lemma 2.1 of Lesson 7), which a CM curve never has: its residual images are contained in the normalizer of a Cartan subgroup. This is why the CM case is proved through Hecke characters instead.

## Sources

- [OpenAI-030] OpenAI, *Modularity of elliptic curves over imaginary quadratic fields*, OpenAI Math Release preprint, 4 October 2026, Section 9 (propagation of automorphy and descent). https://github.com/openai/math/tree/main/preprints/Modularity-of-elliptic-curves-over-imaginary-quadratic-fields-October-4-2026
- [Lan] R. P. Langlands, *Base change for GL(2)*, Annals of Mathematics Studies 96 (1980), Chapter 2 (properties a)–g) of local liftings and A)–F) of global liftings) and Lemma 3.1 (strong multiplicity one). https://publications.ias.edu/sites/default/files/base-change-for-gl2_rpl.pdf
- [JL] H. Jacquet and R. P. Langlands, *Automorphic forms on GL(2)*, Lecture Notes in Math. 114 (1970), Proposition 12.1. https://publications.ias.edu/sites/default/files/automorphic-forms-on-gl2_rpl.pdf
- [MilneCM] J. S. Milne, *Complex Multiplication*, course notes, Theorem 10.1 (the main theorem of complex multiplication). https://www.jmilne.org/math/CourseNotes/CM.pdf
