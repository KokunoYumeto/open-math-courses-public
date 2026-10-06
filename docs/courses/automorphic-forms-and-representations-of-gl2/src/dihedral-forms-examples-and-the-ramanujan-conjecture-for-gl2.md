# Dihedral forms, examples, and the Ramanujan conjecture for GL₂

A character has a degree-one Euler product. Inducing it from a quadratic field produces a degree-two Euler product over the base field. The converse theorem turns this elementary change of viewpoint into cusp forms. We will follow the construction far enough to prove the precise weight, primitive level and Fourier expansion of a CM theta series, then compute two examples with very different infinity types.

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The base field is \(\mathbb Q\), unless another global field is explicitly mentioned. Write \(C_K=K^\times\backslash\mathbb A_K^\times\), \(C_K^1=\ker|\cdot|\), and \(\sigma\) for the nontrivial automorphism of a quadratic extension. Our \(L^*(s,\pi)\) includes the archimedean factor, while \(L_{\mathrm{fin}}\) does not. The unitary normalization is that of Global Whittaker functions and the L-function of a cuspidal representation. In particular, a weight-\(k\) classical form has

\[
L_{\mathrm{fin}}(s,\pi_f)=L(f,s+(k-1)/2).
\tag{0.1}
\]

The global additive character has positive real exponential \(e^{2\pi ix}\), its finite components make it trivial on \(\mathbb Q\), and additive measures are self-dual. On \(K\) use \(\psi_K=\psi_{\mathbb Q}\circ\operatorname{Tr}_{K/\mathbb Q}\). A coherent change from the opposite sign used in the Tate-theory prerequisite multiplies local epsilon constants by character values at \(-1\); their global product is one. We retain the complex absolute value \(|z|_{\mathbb C}=z\bar z\) and
\(\Gamma_{\mathbb C}(s)=2(2\pi)^{-s}\Gamma(s)\).

## 1. Induction and its complete Euler product

Local and global class field theory identify characters of ideles with characters of the corresponding abelianized Weil groups. We use arithmetic Frobenius: an unramified character takes the value \(\chi(\varpi)\) on Frobenius. A general Hecke character need not be a finite-image character of the absolute Galois group. Finite-order characters will give such Galois representations in Section 5. Section 1.1 supplies the exact number-field construction and norm/transfer conventions for arbitrary quasicharacters. The continuous function-field abelianization is proved in NT-CFT-17, Section 8, equations (30)–(34).

Let \(H\) be an index-two normal subgroup of \(G\), choose \(t\notin H\), and put \(\chi^\sigma(h)=\chi(tht^{-1})\). In a coset basis, the induced representation \(\rho=\operatorname{Ind}_H^G\chi\) has

\[
\rho(h)=\begin{pmatrix}\chi(h)&0\\0&\chi^\sigma(h)\end{pmatrix},
\qquad
\rho(t)=\begin{pmatrix}0&\chi(t^2)\\1&0\end{pmatrix}.
\tag{1.1}
\]

These matrices satisfy the conjugation and square relations, so they define the induced representation. If \(\chi\ne\chi^\sigma\), choose \(h\) whose two eigenvalues differ. An invariant line would be an eigenspace of \(\rho(h)\), hence one coordinate axis; \(\rho(t)\) exchanges those axes. Thus \(\rho\) is irreducible. If \(\chi=\chi^\sigma\), choose a square root \(b\) of \(\chi(t^2)\). The assignments \(\chi(h)\) on \(H\) and \(\pm b\) on \(t\) define two extensions, and \(\rho\) is their direct sum.

**Theorem 1.1 — induction identity.** For a quadratic extension \(K/\mathbb Q\), a Hecke character \(\chi\), and a Hecke character \(\omega\) of \(\mathbb Q\),

\[
L^*(s,\operatorname{Ind}\chi\otimes\omega)
 =L_K^*(s,\chi(\omega\circ N_{K/\mathbb Q})).
\tag{1.2}
\]

The equality includes ramified factors and infinity, and holds initially in a common half-plane, then wherever either side continues.

**Proof.** In the function model \(f(hg)=\chi(h)f(g)\) with right translation, send \(f(g)\) to \(\omega(g)f(g)\). This gives an intertwiner
\[
\operatorname{Ind}\chi\otimes\omega
 \simeq\operatorname{Ind}(\chi\,\omega|_H).
\tag{1.3}
\]
Indeed its transformation under \(h\) is \(\chi(h)\omega(h)\), and right translation by \(g_0\) contributes exactly \(\omega(g_0)\). The norm compatibility of reciprocity identifies \(\omega|_{W_K}\) with \(\omega\circ N\). It remains to prove the induction identity without the twist.

At a finite prime \(p\), let \(I\) be inertia, \(F\) an arithmetic Frobenius and \(T=p^{-s}\). The local factor is \(\det(1-T\rho(F)|\rho^I)^{-1}\). Inertia acts on the cosets indexing induction. An invariant function on an inertia orbit exists precisely when the inducing character is trivial on that orbit's stabilizer; in that case the invariant functions on the orbit form a one-dimensional space. Frobenius permutes these lines. If a surviving cycle has length \(f\), choose a vector on its first line and successively transport it. After \(f\) steps the vector is multiplied by the inducing character's value \(c\) on the Frobenius of the extension. In this basis
\[
\det(1-TF\mid\text{cycle})=1-cT^f.
\tag{1.4}
\]
For example, expand the cyclic matrix determinant: only the diagonal choice and the full cycle survive, with the latter contributing \(-cT^f\). The cycles are exactly the places \(w\mid p\), with length their residue degree \(f_w\). Their stabilizers are \(I_w\). Consequently the determinant is the product of \(1-\chi_w(F_w)p^{-f_ws}\) for unramified \(\chi_w\), with no factor for ramified \(\chi_w\). This is exactly the product of the Hecke factors of \(K_w\).

For quadratic fields this also checks every possible finite case directly:

| Local algebra | Character condition | Inverse local factor |
|---|---|---|
| \(K\otimes\mathbb Q_p=\mathbb Q_p\times\mathbb Q_p\) | each unramified summand contributes | \(\prod_{w\mid p,\ \chi_w\text{ unramified}}(1-\chi_w(p)T)\) |
| unramified quadratic field | \(\chi_w\) unramified | \(1-\chi_w(F_w)T^2\) |
| ramified quadratic field | \(\chi_w\) unramified | \(1-\chi_w(F_w)T\) |
| quadratic field | \(\chi_w\) ramified | \(1\) |

In the ramified quadratic row inertia is transitive on the two cosets. Its fixed line has dimension one when \(\chi_w|_{I_w}=1\), even though the full two-dimensional representation is ramified. Thus ramification of the extension does not delete this degree-one factor.

At infinity, a complex character \((z/|z|)^n|z|_{\mathbb C}^{it}\) has factor \(\Gamma_{\mathbb C}(s+it+|n|/2)\). Its induction to \(W_{\mathbb R}\) has the same factor, by the defining real Weil-group factors. When \(n=0\), its two real characters have factors \(\Gamma_{\mathbb R}(s+it)\) and \(\Gamma_{\mathbb R}(s+it+1)\); their product equals \(\Gamma_{\mathbb C}(s+it)\) by gamma duplication. A split real algebra gives the two real factors separately. Multiplying the finite and infinite identities proves (1.2). \(\square\)

The same matrices give
\[
\det(\operatorname{Ind}\chi)=\epsilon_{K/\mathbb Q}\,\chi|_{\mathbb A_{\mathbb Q}^\times}.
\tag{1.5}
\]
Here \(\epsilon_{K/\mathbb Q}\) is the quadratic idele-class character. To check the character in (1.5), the determinant on \(h\in H\) is \(\chi(h)\chi(tht^{-1})\), and on \(t\) it is \(-\chi(t^2)\). The products without that minus sign describe the group transfer \(G^{\mathrm{ab}}\to H^{\mathrm{ab}}\). Under reciprocity, transfer is inclusion of base-field ideles. The sign is the quadratic quotient character. In particular the right side is trivial on \(\mathbb Q^\times\).

### 1.1. Why the two idelic maps have these directions

Here is the precise number-field Weil input for arbitrary continuous quasicharacters. Write \(C_L=L^\times\backslash\mathbb A_L^\times\). For a quadratic extension \(K/F\), use the relative Weil extension
\[
1\longrightarrow C_K\longrightarrow W_{K/F}
\longrightarrow\operatorname{Gal}(K/F)\longrightarrow1
\tag{1.6}
\]
represented by the global fundamental class. Its construction, continuous topology, closed commutator quotient, tower maps and local compatibility are proved in [NT-CFT-24, Sections 6–7](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-CFT/brauer-groups-of-local-and-global-fields.html), Theorem 24.6 and equations (29)–(39). In particular transfer gives the topological identification
\[
\tau:W_{K/F}^{\mathrm{ab}}\xrightarrow{\sim}C_F,
\qquad \tau|_{C_K}=N_{K/F}.
\tag{1.7}
\]
The superscript denotes the Hausdorff abelianization; the proof establishes that the commutator kernel is already closed at this finite relative level. Thus a continuous character of the quotient is exactly a Hecke quasicharacter, with no finite-image hypothesis. The arithmetic convention makes the quotient map to the finite Galois group the usual reciprocity map.

**Proposition 1.2 — restriction, transfer and the determinant.** In (1.6), restriction of a character of \(C_F\) is pullback by the idelic norm. Group transfer in the other direction is extension of base-field ideles. Every continuous \(\chi:C_K\to\mathbb C^\times\) is invariant under the nontrivial field automorphism if and only if it is a norm pullback from \(C_F\). The determinant identity (1.5) and the twisting identity (1.3) therefore hold for arbitrary Hecke quasicharacters.

**Proof.** Put \(E=W_{K/F}\), \(H=C_K\), and choose \(t\in E\setminus H\). Conjugation by \(t\) on \(H\) is the field automorphism \(\sigma\). Transfer \(V:E^{\mathrm{ab}}\to H\), computed from the two cosets, is
\[
V(h)=h\,\sigma(h)\quad(h\in H),\qquad
V(t)=t^2.
\tag{1.8}
\]
These formulas also follow by multiplying the coefficients in \(xs(u)=s(xu)a_u\) for the two chosen lifts. Changing the lifts cancels their factors, and multiplying two elements permutes the factors, proving independence and the homomorphism property. Its image is in \(C_K^\sigma\). The fixed-class identification in NT-CFT-24, Section 1, is \(C_K^\sigma=i(C_F)\), where \(i\) extends an idele of \(F\) to all places of \(K\). The construction of (1.7) is precisely transfer followed by \(i^{-1}\). Consequently
\[
V=i\circ\tau,\qquad \tau(h)=N_{K/F}(h).
\tag{1.9}
\]
This proves both directions of the idelic compatibility. In particular \(\mu\circ\tau\) restricts to \(\mu\circ N_{K/F}\), as used in (1.3).

Suppose \(\chi=\chi^\sigma\). Choose \(b\in\mathbb C^\times\) with \(b^2=\chi(t^2)\). Set \(\widetilde\chi(h)=\chi(h)\) and \(\widetilde\chi(t)=b\). The conjugation relation is respected by the assumed invariance and the square relation by the choice of \(b\); the two-coset multiplication therefore defines a character of \(E\). It is continuous on each of the two open cosets because \(\chi\) is continuous. It factors through the topological abelianization (1.7), giving a continuous \(\mu\) of \(C_F\). Its restriction says \(\chi=\mu\circ N_{K/F}\). Conversely a norm pullback is invariant, because the norm is unchanged by \(\sigma\). This also proves that the non-norm hypothesis in Theorem 2.1 is exactly the irreducibility hypothesis in (1.1).

Finally the coset matrices (1.1) have determinant \(\chi(h\sigma(h))\) on \(h\in H\) and \(-\chi(t^2)\) on \(t\). For any \(x\in E\) their determinant is therefore \(\epsilon(x)\chi(V(x))\), where \(\epsilon\) is the sign of the permutation of the two cosets. Under (1.7), this sign is \(\epsilon_{K/F}\) and \(V(x)=i(\tau(x))\). Hence
\[
\det(\operatorname{Ind}\chi)
=\epsilon_{K/F}\,(\chi\circ i)
\quad\text{as a character of }C_F.
\tag{1.10}
\]
This is (1.5), including its value on elements whose two cosets are exchanged. Local decomposition maps have the commuting abelianization diagram proved in NT-CFT-24, (39); hence these same characters restrict to the actual local Hecke characters used in (1.2). No passage from finite-order reciprocity to an arbitrary quasicharacter is left implicit. \(\square\)

For comparison with the primary source, Jacquet–Langlands opens Section 12 with the relative Weil extension, tower maps and local decomposition maps, referring to Artin–Tate and Weil. The exact written prerequisite above supplies the cocycle, transfer, topology and local-compatibility proofs used here.

### 1.2. The function-field relative group

**Proposition 1.3 — the same compatibility in function fields.** Proposition 1.2 holds for a quadratic global function-field extension \(K/F\), in every characteristic. Its local restrictions are the local Hecke characters, and the matrix induction identity (1.2), with \(\mathbb Q\) replaced by \(F\), holds over every global field.

**Proof.** We give the finite relative construction explicitly. The global class formation in NT-CFT-24, Theorem 24.6, applies to function fields. Its fixed coefficient group is \(C_K^\sigma=i(C_F)\), its cyclic first cohomology vanishes, and its degree-two group is \(C_F/N C_K\), of order two. Choose \(c\in C_F\setminus N C_K\). This represents the fundamental class. Form the group with two open copies of \(C_K\), generated by that coefficient group and \(t\), with
\[
tht^{-1}=\sigma(h),\qquad t^2=i(c).
\tag{1.11}
\]
The fact that \(i(c)\) is fixed by \(\sigma\) proves consistency and associativity; equivalently this is the two-element carry cocycle. Define \(\tau(h)=N h\), \(\tau(t)=c\). The square relation is preserved because \(N i(c)=c^2\). The conjugation relation is preserved because the norm is invariant. Thus \(\tau\) is a continuous homomorphism onto \(C_F\).

If \(\tau(ht^e)=1\), the nontrivial norm class of \(c\) forces \(e=0\). Then \(N h=1\). Cyclic first-cohomology vanishing gives \(h=\sigma(b)b^{-1}=[t,b]\). Consequently the kernel is exactly the commutator subgroup. This kernel is closed. The norm map on \(C_K^1\) is an open map onto its compact image, by the compact-group quotient topology. The degree coordinate is discrete, the norm preserves the adelic module, and \(N C_K\) is open of index two by NT-CFT-16, Theorem 16.4. Therefore the norm is open onto that subgroup, and \(\tau\) is open onto \(C_F\). This proves the topological abelianization, not only its algebraic form.

The two-coset transfer is still \(V(h)=h\sigma(h)=i(Nh)\), \(V(t)=t^2=i(c)\), hence \(V=i\tau\). The continuous square-root extension argument of Proposition 1.2 proves the norm-factor criterion, and its determinant and twist computations apply unchanged.

At a nonsplit place the local quadratic fundamental class, inserted into \(C_K\), has global invariant \(1/2\), by the idelic sum construction in NT-CFT-24, Section 6. It is therefore the same fundamental class as (1.11). Equality of cocycle classes gives a continuous map of the local relative extension into this group: change one finite set of lifts by the coefficient cochain whose boundary is the cocycle difference. Transfer then commutes with insertion of \(F_v^\times\) into \(C_F\), because the identical two-coset products commute with the coefficient map. At a split place the two coefficient insertions give the two local characters. This proves the local compatibility needed for induction.

The inertia-orbit and Frobenius-cycle proof (1.4) works with \(q_v^{-s}\) at every finite place. At a real place it is the real/complex comparison already made; at a complex place the local algebra splits and gives the product of its two complex factors. Multiplication proves (1.2) for any quadratic global extension and any base Hecke twist. \(\square\)

## 2. Why the induced data are cuspidal

**Theorem 2.1 — quadratic automorphic induction.** Suppose \(\chi\) is a Hecke quasicharacter of a quadratic global extension \(K/F\) which is not of the form \(\mu\circ N_{K/F}\). The local representations corresponding to \(\operatorname{Ind}\chi\) have a cuspidal automorphic restricted tensor product. The full assertion is proved in Section 2.1, using the all-field converse proved in Lesson 15, Theorem 4.5, and the exact analytic hypotheses verified below. The original locator is Jacquet–Langlands, Proposition 12.1. We first give the rational deduction; Corollary 2.3 makes its quasicharacter twist explicit.

The local quadratic construction is now proved in Lesson 10, Theorems 6.3–6.5: in every nonarchimedean field and residue characteristic it constructs the generic quadratic model, its norm-factor case, central character, twists and complete \(L\)- and epsilon-factor identity. Lesson 11, Sections 3–6 and Theorems 3.2, 5.1 and 6.1, gives the real and complex models and factors. The original comparison is Jacquet–Langlands, Theorem 4.7 and §5. At split places use the normalized principal series of the two local characters. For unitary inducing characters its local unitary classification gives an irreducible infinite-dimensional generic representation. At nonsplit places with distinct conjugate characters use the quadratic supercuspidal or real discrete-series construction. The norm-factor case gives the generic principal series. These proved local statements determine the bad factors as well as the good ones.

We first supply the strip estimate needed for the global argument.

**Lemma 2.2 — the Hecke strip estimate.** If a unitary Hecke character \(\gamma\) of a number field is nontrivial on \(C_K^1\), its completed primitive Hecke function is entire and decreases faster than every inverse power of \(|\operatorname{Im}s|\), uniformly on each closed strip \(A\le\operatorname{Re}s\le B\).

**Proof.** Use the standard Schwartz test \(f\) of [NT-ADL-10](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-ADL/NT-ADL-10.html), equations (2)–(3), whose Tate integral is exactly \(L_K^*(s,\gamma)\). Let \(a(t)\) be the norm-\(t\) idele obtained by scaling every ordinary infinite coordinate by \(t^{1/[K:\mathbb Q]}\). With quotient measure \(dh\,dt/t\), put
\[
F_f(t)=\gamma(a(t))\int_{C_K^1}E_f(ha(t))\gamma(h)\,dh,
\qquad E_f(x)=\sum_{\alpha\in K^\times}f(\alpha x).
\tag{2.1}
\]
The norm-one group is compact. The theta lemma of [NT-ADL-09](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-ADL/NT-ADL-09.html), equations (11)–(14), supplies uniform rapid decay for \(t\ge1\). Here is why that bound also controls all derivatives. Differentiation by \(D=t\,d/dt\) differentiates the infinite Schwartz function by a linear combination of coordinate Euler operators and multiplies \(\gamma(a(t))\) by a constant. Every resulting infinite function is Schwartz. The same fixed fractional-ideal lattice and compact set of lifts therefore give, for all \(r,M\),
\[
|D^rF_f(t)|\le C_{r,M}t^{-M}\qquad(t\ge1).
\tag{2.2}
\]
Local uniform convergence of the differentiated lattice sums, and the compact fibre, justify each differentiation under the sum and integral.

Poisson summation gives \(E_f(x)=|x|^{-1}E_{\widehat f}(x^{-1})+|x|^{-1}\widehat f(0)-f(0)\). The integral of \(\gamma\) over \(C_K^1\) is zero: translate it by an element on which \(\gamma\ne1\). Both correction terms vanish in (2.1). Changing \(h\) to \(h^{-1}\) yields the exact relation
\[
F_f(t)=t^{-1}F_{\widehat f,\gamma^{-1}}(t^{-1}).
\tag{2.3}
\]
The right-hand function includes its own factor \(\gamma^{-1}(a(t^{-1}))=\gamma(a(t))\). Its estimates (2.2) prove rapid decay of every \(D\)-derivative at zero as well. Thus for every real \(\sigma\),
\[
L_K^*(\sigma+iT,\gamma)
 =\int_{-\infty}^{\infty}F_f(e^x)e^{\sigma x}e^{iTx}\,dx.
\tag{2.4}
\]
This integral is entire, because its integrand and all parameter derivatives are integrable uniformly on compact \(s\)-sets. For \(\sigma\in[A,B]\), all \(x\)-derivatives of \(F_f(e^x)e^{\sigma x}\) have uniformly bounded \(L^1\)-norms: (2.2)–(2.3) absorb \(e^{Ax},e^{Bx}\) at their respective ends. Integrate by parts \(r\) times in (2.4); the boundary terms vanish, and the result is bounded by \(C_r|T|^{-r}\) for \(|T|\ge1\). The remaining compact rectangle is bounded by continuity. \(\square\)

**Deduction of Theorem 2.1 over \(\mathbb Q\).** For every unitary base-field \(\omega\), the character \(\gamma=\chi(\omega\circ N)\) is nontrivial on \(C_K^1\). Otherwise it would be a pure imaginary norm power; solving for \(\chi\) would express it through the norm, contrary to the hypothesis. The same argument applies to \(\gamma^{-1}\). Theorem 1.1 and Lemma 2.2 therefore give both entire bounded completed twist families. Their initial Euler products converge absolutely for \(\operatorname{Re}s>1\), by the degree-one Euler product and unitarity. The good degree-two parameters have modulus one.

The epsilon equation also agrees. Local induction of a degree-one character contributes
\[
\varepsilon_{\mathbb Q_v}(s,\operatorname{Ind}\gamma_v,\psi_v)
 =\lambda_v(K/\mathbb Q,\psi_v)
   \prod_{w\mid v}\varepsilon_{K_w}(s,\gamma_w,\psi_v\circ\operatorname{Tr}).
\tag{2.5}
\]
The local induction constant \(\lambda_v\), independent of \(\gamma\), is part of the proved local comparison in Lesson 10, Theorem 6.5, and the archimedean factor comparison of Lesson 11. Its global product is one. This can be checked using the inducing trivial character: \(\operatorname{Ind}1=1\oplus\epsilon_{K/\mathbb Q}\), and
\(\zeta_K^* =\zeta_{\mathbb Q}^* L^*(\epsilon_{K/\mathbb Q})\), including gamma duplication. The three Tate functional equations force equality of their epsilon products; by (2.5) their quotient is exactly \(\prod_v\lambda_v\). Thus the Hecke functional equation gives the product of the required local degree-two epsilon factors. Only finitely many factors differ from one.

The central character is trivial on \(\mathbb Q^\times\), by (1.5); the local factors are generic, and the restricted product is well defined. All four hypotheses of Multiplicity one, strong multiplicity one and the converse theorem, Theorem 4.1, now hold. Its cuspidal conclusion proves the assertion. The global converse and its convergence, smooth Mellin and Weyl-invariance arguments are proved in Lesson 15, §4; the present argument verifies its hypotheses for this quadratic tensor. \(\square\)

**Corollary 2.3 — rational induction for every quasicharacter.** The rational assertion of Theorem 2.1 holds without a unitarity assumption on \(\chi\).

**Proof.** The absolute value of a continuous quasicharacter is trivial on the compact group \(C_K^1\): its image is a compact subgroup of \(\mathbb R_{>0}\), and that group has no nontrivial compact subgroup. The number-field module identifies \(C_K/C_K^1\) with \(\mathbb R_{>0}\). A continuous positive character of this last group is \(t\mapsto t^a\), for some real \(a\), by taking logarithms. Consequently \(\chi_0=\chi|\cdot|_K^{-a}\) is unitary. Since \(|x|_K=|N_{K/\mathbb Q}x|_{\mathbb Q}\), the removed factor is a base-field norm character. Thus \(\chi_0\) still does not factor through the norm. The deduction just proved constructs a cuspidal representation \(\pi_0\) for \(\chi_0\).

The finite local twist identity of Lesson 10, Theorem 6.5, and the archimedean models identify the proposed local data for \(\chi\) with
\[
\pi=\pi_0\otimes|\det|_{\mathbb A}^{a}.
\tag{2.6}
\]
This twist is automorphic. Indeed multiplication of an automorphic function by \(|\det g|_{\mathbb A}^{a}\) preserves rational left invariance by the product formula, preserves smoothness and compact-type finiteness, and merely shifts the scalar infinitesimal character and growth exponent. It also preserves cuspidality: \(\det(n(x)g)=\det g\), so that factor is constant in the defining unipotent integral. This proves the assertion for every quasicharacter. It extends the rational theorem; Section 2.1 supplies the full general-base-field proof. \(\square\)

### 2.1. Complete the induction proof over every global field

**Lemma 2.4 — the function-field Hecke estimate and equation.** Let \(L\) be a global function field with full constant field \(\mathbf F_Q\). For a unitary Hecke character \(\gamma\) nontrivial on \(C_L^1\), its primitive completed Hecke function is a Laurent polynomial in \(Q^s\). It is entire and bounded on every finite-width strip, and satisfies its exact Tate functional equation. The same holds for its dual. Norm characters have meromorphic continuation and the same functional equation.

**Proof.** Use the residue additive character and self-dual Haar measure of NT-CFT-15, Section 5. Its proof gives \(L^\perp=L\). We first derive the exact global Poisson normalization. For a compact locally constant \(f\), its additive periodization is locally constant on the compact quotient \(\mathbb A_L/L\), hence factors through a finite quotient. If this quotient has Haar volume \(c\), finite Fourier inversion gives
\(\sum_{\alpha\in L}f(\alpha)=c^{-1}\sum_{\beta\in L}\widehat f(\beta)\).
The coefficient follows by unfolding its Fourier integral; the annihilator assertion identifies the character set with \(L\). Both sums are finite, since the Fourier transform also has compact locally constant support. Apply the same formula to \(\widehat f\) and use \(\widehat{\widehat f}(x)=f(-x)\). A nonnegative test with nonzero lattice sum gives \(c^2=1\), so \(c=1\). This proves both the self-dual covolume and Poisson formula in this characteristic.

For a test \(f\), its nonzero theta sum \(E_f(x)=\sum_{\alpha\in L^\times}f(\alpha x)\) is finite locally uniformly, because \(L\) is discrete and the support is compact. Choose a degree-one norm section and average over the compact group \(C_L^1\), as in (2.1). A nonzero term requires \(|\alpha x|\le C_f\) by the product of its finitely many nontrivial local support bounds. Since \(|\alpha|=1\), the average is zero at sufficiently large norm, uniformly on its compact fibre.

Poisson summation gives
\[
E_f(x)=|x|^{-1}E_{\widehat f}(x^{-1})
       +|x|^{-1}\widehat f(0)-f(0).
\tag{2.7}
\]
The character average kills both last terms, by Haar translation on \(C_L^1\). Changing the fibre variable to its inverse proves (2.3), now for the discrete norm values. Applying the large-norm support bound to \(\widehat f\) shows that the original average is also zero at all sufficiently small norm. Its Mellin sum thus has only finitely many terms. It is a Laurent polynomial in \(Q^s\), with the exact dual equality supplied by (2.7).

To identify it with the primitive Hecke function, take \(f_v=1_{\mathcal O_v}\) at an unramified place and \(f_v=\gamma_v^{-1}1_{\mathcal O_v^\times}\) at a ramified place. With multiplicative unit volume one, their local integrals are respectively
\[
(1-\gamma_v(\varpi_v)q_v^{-s})^{-1}
\quad\text{and}\quad1.
\tag{2.8}
\]
There are finitely many exceptions. The product and unfolded integral converge absolutely for \(\operatorname{Re}s>1\): compare places with those of \(\mathbf F_Q(u)\), over which \(L\) is finite, and use that there are at most \(Q^n\) monic polynomials of degree \(n\). The finite extension contributes a bounded number of places above each base place. Nonnegative Fubini and then absolute convergence justify the product and unfolding. Thus the finite Mellin sum is the continued primitive \(L\)-function, including every bad factor.

Here are the needed local Fourier constants in this characteristic. Write \(n\) for the additive conductor, so the annihilator of \(\mathcal O\) is \(\varpi^{-n}\mathcal O\) and its self-dual volume is \(q^{-n/2}\). For the unramified test,
\(\widehat{1_{\mathcal O}}=q^{-n/2}1_{\varpi^{-n}\mathcal O}\).
Its dual shell sum is therefore
\(\gamma(\varpi)^n q^{n(1/2-s)}L_v(1-s,\gamma^{-1})\).
For a ramified character of conductor \(a\ge1\), the test \(\gamma^{-1}1_{\mathcal O^\times}\) is constant on additive \(\varpi^a\mathcal O\)-cosets. Its Fourier transform is supported in \(\varpi^{-a-n}\mathcal O\), and is zero off its outer shell. Indeed for \(a\ge2\), multiplication by a principal unit at depth \(a-1\) with nontrivial character value preserves the additive phase at every deeper shell and forces the integral to zero; for \(a=1\) ordinary nontrivial residue-unit orthogonality gives the same result. On the outer shell set
\[
A=q^{-n/2}\int_{\mathcal O^\times}
 \gamma(u)^{-1}\psi(\varpi^{-a-n}u)\,du_0,
\]
where \(du_0\) gives \(\mathcal O\) volume one. Substitution by a unit \(w\) shows that the transform at \(\varpi^{-a-n}w\) is \(A\gamma(w)\). Its dual integral is
\[
A\gamma(\varpi)^{a+n}q^{(a+n)(1-s)}
=W\,q^{(a+n)(1/2-s)},\qquad
W=Aq^{(a+n)/2}\gamma(\varpi)^{a+n}.
\]
Finite Fourier Parseval on the additive residue quotient gives \(|A|=q^{-(a+n)/2}\): the input has squared norm \(q^{-n/2}(1-q^{-1})\), while the outer shell has additive measure \(q^{a+n}q^{-n/2}(1-q^{-1})\). Thus \(|W|=1\), and this is the exact primitive epsilon monomial. These calculations prove the same normalization as NT-ADL-07, Theorem 7.3, now directly in equal characteristic; that lesson states its field scope as finite extensions of \(\mathbb Q_p\).

For example, over \(\mathbf F_3((t))\) let the additive character read the coefficient of \(t^{-1}\) through \(e^{2\pi i(\cdot)/3}\), and take the quadratic residue-unit character with \(\gamma(t)=1\). Then \(n=0\), \(a=1\), and
\(A=(e^{2\pi i/3}-e^{4\pi i/3})/3=i/\sqrt3\).
Thus \(W=i\) and the epsilon factor is \(i\,3^{1/2-s}\), with the sign fixed by the displayed additive character.

Applying these calculations to the product test identifies its Fourier-dual integral with the primitive dual function times the product of its exact epsilon monomials. Equation (2.7) therefore gives the complete Tate equation. For a norm character the two zero terms survive; their norm-coordinate sums are geometric series, giving the meromorphic continuation with at most the corresponding two poles and the same Fourier-dual equation. This includes the zeta functions used to normalize induction. \(\square\)

**Proof of Theorem 2.1 over every global field.** First suppose \(\chi\) is unitary. The local quadratic models of Lessons 10–11, together with the split principal models, are infinite-dimensional, generic and unitary. Almost everywhere their Satake values have absolute value one. Propositions 1.2–1.3 identify the central character as \(\epsilon_{K/F}(\chi\circ i)\), trivial on \(F^\times\), and identify every twisted complete function with
\[
L_K^*(s,\chi(\mu\circ N_{K/F})).
\tag{2.9}
\]
If this character were a norm pullback, dividing by \(\mu\circ N\) would make \(\chi\) one too. It is therefore non-norm. In particular it is nontrivial on \(C_K^1\): a unitary character trivial there is a norm-coordinate character, and the equality \(|N x|_F=|x|_K\) makes every such character a norm pullback. The same assertions hold for its dual. Lemma 2.2 supplies the entire bounded-strip Hecke functions over number fields; Lemma 2.4 supplies them over function fields.

The exact local epsilon comparison in Lesson 10 has a quadratic induction constant \(\lambda_v(K/F,\psi_v)\), independent of \(\chi\); the archimedean comparison is Lesson 11. Its global product is one. Indeed apply the comparison to the trivial inducing character. Its induced representation is \(1\oplus\epsilon_{K/F}\), and the induction identity is \(\zeta_K=\zeta_F L_F(\epsilon_{K/F})\), with all factors. The three complete Tate equations, proved in NT-ADL-09 for number fields and in Lemma 2.4 for function fields, identify their global epsilon products. Their quotient is exactly \(\prod_v\lambda_v\), giving one. Thus (2.9) satisfies the exact full equation demanded by Lesson 15, Theorem 4.5. That proved all-field converse realizes the proposed tensor as cuspidal automorphic, with every local component prescribed.

For an arbitrary continuous quasicharacter, compactness of \(C_K^1\) makes its absolute value trivial on that group. The quotient is \(\mathbf R_{>0}\) for a number field and a cyclic discrete norm group for a function field. Hence
\[
\chi=\chi_0|\cdot|_K^a,\qquad \chi_0\text{ unitary},\quad a\in\mathbf R.
\tag{2.10}
\]
Module compatibility shows that \(\chi_0\) is still non-norm. Apply the unitary result to obtain \(\pi_0\). The local twist identity of Lessons 10–11 identifies the required local tensor with \(\pi_0\otimes|\det|_{\mathbb A_F}^a\). Multiply each automorphic function by \(|\det g|^a\). The product formula preserves rational left invariance; the multiplier is smooth and compact-trivial, shifts scalar infinitesimal parameters at infinity and preserves moderate growth. Its determinant is one on the unipotent group, so every cusp integral remains zero. This is the required automorphic realization and proves Theorem 2.1 for every quasicharacter, over every global field. \(\square\)

## 3. The primitive CM theta theorem

Fix an imaginary quadratic \(K\subset\mathbb C\), discriminant \(d_K\), an integral conductor \(\mathfrak f\), and \(m=k-1\ge1\). An **algebraic ideal character of type \(z^m\)** is a multiplicative \(\Psi\) on fractional ideals prime to \(\mathfrak f\) such that
\[
\Psi((\alpha))=\alpha^m\qquad(\alpha\equiv1\pmod{\mathfrak f}).
\tag{3.1}
\]
Its conductor is the least such modulus. Equivalently there is a finite character \(\eta\) on the units modulo \(\mathfrak f\) with \(\Psi((\alpha))=\eta(\alpha)\alpha^m\) for \(\alpha\) prime to \(\mathfrak f\). This is the ideal/idelic dictionary of NT-ADL-06, Theorem 6.3. The finite character satisfies \(\eta(\epsilon)=\epsilon^{-m}\) for each unit \(\epsilon\).

The absolute value of \(\Psi(\mathfrak a)\) is \(N\mathfrak a^{m/2}\). Indeed the quotient of these two positive multiplicative functions is one on principal ideals, because \(|\eta(\alpha)|=1\) and \(N(\alpha)=|\alpha|^2\). It therefore factors through the finite ideal class group. A finite group has no nontrivial homomorphism to \(\mathbb R_{>0}\). Consequently
\[
u(\mathfrak a)=\Psi(\mathfrak a)N\mathfrak a^{-m/2}
\tag{3.2}
\]
is unitary. Its actual idelic component at infinity is
\(u_\infty(z)=(z/|z|)^{-m}\). The inverse sign is forced by triviality on diagonal \(K^\times\). Complex conjugation changes \(-m\) to \(m\), so \(u\ne u^\sigma\); in particular \(u\) cannot factor through the norm.

**Theorem 3.1 — CM theta series, proved from the analytic converse.** Suppose \(\Psi\) is primitive and \(m\ge1\). All ideal sums below run over nonzero integral ideals. Then
\[
\theta_\Psi(z)=\sum_{\substack{\mathfrak a\subset\mathcal O_K\\(\mathfrak a,\mathfrak f)=1}}
 \Psi(\mathfrak a)q^{N\mathfrak a},\qquad q=e^{2\pi iz},
\tag{3.3}
\]
is a normalized primitive cusp form of weight \(k=m+1\), exact level
\[
N=|d_K|N\mathfrak f,
\tag{3.4}
\]
and nebentypus \(\varepsilon(n)=\epsilon_{d_K}(n)\Psi((n))/n^m\) on integers prime to \(N\), extended as a Dirichlet character modulo \(N\).

**Proof.** For a rational \(n\), the number of ideals of norm \(n\) is at most the divisor function \(d(n)\). Check prime powers: a split prime has at most \(r+1\) ideals of norm \(p^r\), an inert prime has at most one, and a ramified prime at most one; unique ideal factorization multiplies these counts. Thus the coefficient \(b_n\) in (3.3) satisfies \(|b_n|\le d(n)n^{m/2}\). This proves locally uniform convergence on the upper half-plane and hence holomorphy there. Also \(b_1=1\).

Apply Section 2 to \(u\). Every norm-pulled-back base twist still has nonzero angular type \(-m\), so the entire dual families and strip estimates are available. We obtain a unitary cuspidal \(\Pi=\operatorname{AI}_{K/\mathbb Q}u\). At infinity the induction of the angular character is \(D_k\), the full real discrete series whose positive-determinant restriction contains the holomorphic lowest-weight \(k\) module. Its factor is \(\Gamma_{\mathbb C}(s+m/2)\), agreeing with Lesson 11, Theorem 6.1.

We must determine the conductor before claiming an exact level. The primitive Hecke equation of NT-ADL-10, Theorem 10.1, has epsilon monomial
\[
\varepsilon_K(s,u)=W_K(u)(|d_K|N\mathfrak f)^{1/2-s},
\qquad |W_K(u)|=1.
\tag{3.5}
\]
The local comparison (2.5), with global product of \(\lambda_v\) equal to one, identifies it with the epsilon product of \(\Pi\). By Lesson 9's conductor normalization and Lesson 14, Section 6, that product is \(W_\Pi N_\Pi^{1/2-s}\), where \(N_\Pi=\prod_p p^{c(\Pi_p)}\). Equality of these nonzero monomials for every \(s\) gives \(N_\Pi=|d_K|N\mathfrak f\), by differentiating their logarithmic dependence on \(s\). This proves (3.4), including the discriminant contribution and every bad prime.

The newvector and classical dictionary of Lesson 8, Theorem 5.1, and Lesson 11, Theorem 7.1, give a normalized primitive holomorphic form \(f_\Pi\) of weight \(k\) and this level. Formula (1.5) gives its nebentypus: at a good rational \(p\), the central character has value \(\epsilon_{d_K}(p)u((p))=\epsilon_{d_K}(p)\Psi((p))/p^m\). This is a finite Dirichlet character on the rational units. Its parity is \((-1)^k\), since \(\epsilon_{d_K}(-1)=-1\) and \(\Psi((-1))=1\). The primitive character modulus divides \(N_\Pi\), as also follows from the central action on the newvector.

Finally, (0.1), (1.2) and (3.2) give
\[
L(f_\Pi,s)=L_{K,\mathrm{fin}}(s-m/2,u)
 =\sum_{(\mathfrak a,\mathfrak f)=1}\frac{\Psi(\mathfrak a)}{N\mathfrak a^s}
 =\sum_{n\ge1}\frac{b_n}{n^s}.
\tag{3.6}
\]
These are equal absolutely convergent Dirichlet series on a right half-plane, with their full finite Euler factors. Such a series determines its coefficients: if the difference has first nonzero coefficient \(c_{n_0}\), multiply its value on the positive real axis by \(n_0^s\) and let \(s\to+\infty\). The remaining terms tend to zero by dominated convergence, using absolute convergence at a fixed initial real \(s_0\); the limit is \(c_{n_0}\), a contradiction. Therefore all coefficients of \(f_\Pi\) are \(b_n\). Their normally convergent Fourier expansions identify \(f_\Pi=\theta_\Psi\), proving modularity, all-cusp holomorphy, cuspidality and primitive newness. \(\square\)

The classical Mellin correspondence in [LG-MF-12](https://kokunoyumeto.github.io/open-math-courses-public/courses/LG-MF/LG-MF-12.html), Theorem 4.1, explains the Fricke transformation encoded by these completed equations. Its Section 5 states a specialized even-weight, trivial-character Weil converse. Our proof uses the adelic converse of Lesson 15, so it also covers the nebentypus in Theorem 3.1. The theorem being proved has not been imported as a weighted-theta assertion.

## 4. Gaussian integers and the curve of conductor 32

Let \(K=\mathbb Q(i)\), \(\varpi=1+i\), \(\mathfrak f=(\varpi^3)\). The Gaussian Euclidean algorithm uses nearest integer coordinates: for \(z\in\mathbb C\) choose \(a+bi\) with squared distance at most \(1/2<1\). Division therefore strictly lowers the norm of a nonzero remainder. Every ideal is principal.

The four units \(1,-1,i,-i\) are distinct modulo \(\varpi^3\), and \((\mathcal O_K/\varpi^3)^\times\) has four elements. Thus every ideal prime to \(\varpi\) has a unique generator \(\alpha\equiv1\pmod{\varpi^3}\), called its primary generator. Define \(\Psi(\mathfrak a)=\alpha\). Products of primary generators are primary, so this is an ideal character of type \(z\). Its conductor is exactly \(\varpi^3\): a smaller exponent would have \(-1\equiv1\) modulo the conductor, forcing the impossible equation \(\Psi((-1))=-1\). Exponent three works by construction.

For \(\alpha=a+bi\), divisibility of \(\alpha-1\) by the associate \(2+2i\) says that \((a-1+b)/4\) and \((b-a+1)/4\) are integers. Equivalently
\[
a\text{ odd},\quad b\text{ even},\quad a+b\equiv1\pmod4.
\tag{4.1}
\]
Theorem 3.1 gives weight two and level \(4\cdot8=32\). For odd rational \(n\), the primary generator of \((n)\) is \(\epsilon_{-4}(n)n\); hence the nebentypus \(\epsilon_{-4}(n)\Psi((n))/n\) is trivial. Formula (3.3) becomes the explicit lattice sum
\[
f_{32}(z)=\sum_{\substack{a,b\in\mathbb Z\\ a\text{ odd},\ b\text{ even}\\ a+b\equiv1\ (4)}}
 (a+bi)q^{a^2+b^2}.
\tag{4.2}
\]
Conjugate terms cancel their imaginary parts. Enumerating (4.1) gives
\[
f_{32}=q-2q^5-3q^9+6q^{13}+2q^{17}-q^{25}
 -10q^{29}-2q^{37}+10q^{41}+O(q^{42}).
\tag{4.3}
\]
All even coefficients vanish. For an inert odd \(p\equiv3\pmod4\) there is no ideal of norm \(p\), so \(a_p=0\). Its degree-two Hecke factor is \((1+p^{1-2s})^{-1}\), giving \(a_{p^2}=-p\). At a split \(p=a^2+b^2\) with the two conjugate primary generators, \(a_p=2a\). For instance the primary pair at five is \(-1\pm2i\), giving \(-2\); at thirteen it is \(3\pm2i\), giving \(6\). The recurrence \(a_{p^2}=a_p^2-p\) gives \(a_{25}=-1\).

For \(E:y^2=x^3-x\), direct counting at an odd prime gives
\[
\#E(\mathbb F_p)=p+1+\sum_{x\in\mathbb F_p}\left(\frac{x^3-x}{p}\right),
\qquad a_p(E)=-\sum_x\left(\frac{x^3-x}{p}\right).
\tag{4.4}
\]
The summand is zero at a zero of the cubic. There is one point at infinity, and each finite \(x\) contributes \(1+(\frac{x^3-x}{p})\) points. For \(p\equiv3\pmod4\), pair \(x\) with \(-x\); the signs cancel, proving \(a_p(E)=0\) for every such prime.

| \(p\) | \(3\) | \(5\) | \(7\) | \(13\) | \(17\) | \(29\) | \(37\) | \(41\) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| \(\#E(\mathbb F_p)\) | 4 | 8 | 8 | 8 | 16 | 40 | 40 | 32 |
| \(a_p(E)=a_p(f_{32})\) | 0 | −2 | 0 | 6 | 2 | −10 | −2 | 10 |

To identify the forms for all coefficients, use elliptic modularity, stated in Allen–Anderson–Hamakiotes–Oltsik–Swisher, Theorem 1.1, and the exact conductor-32 record for [LMFDB curve 32.a3](https://www.lmfdb.org/EllipticCurve/Q/32/a/3). It gives a normalized \(g_E\in S_2(\Gamma_0(32))\). The curve has additive reduction at two, so its local factor there is one. Equations (4.4) at \(3,5,7\) and the elliptic Euler-product recurrence give all coefficients through eight: only \(a_1=1\) and \(a_5=-2\) are nonzero. They agree with (4.2).

Here is the needed finite-index uniqueness argument, which we will also use at level 23. If \(h\ne0\) is a holomorphic weight-\(k\) form with a finite-order character on a subgroup \(\Gamma\) of index \(d\), form
\(P=\prod_{\gamma\in\Gamma\backslash\mathrm{SL}_2(\mathbb Z)}h|_k\gamma\).
Right multiplication permutes cosets and contributes values of the character. If its order divides \(r\), then \(P^r\) is a level-one form of weight \(rkd\). Every factor is bounded at infinity, because \(h\) is holomorphic at every cusp. The identity factor shows \(v_\infty(P^r)\ge r v_\infty(h)\). The valence bound of [LG-MF-05](https://kokunoyumeto.github.io/open-math-courses-public/courses/LG-MF/LG-MF-05.html), Theorem 1.1, implies
\[
v_\infty(h)\le kd/12.
\tag{4.5}
\]
The factors may individually have fractional cusp exponents, but their product power is level one, and all of their orders are nonnegative. No assumption that each has period one is needed.

For \(\Gamma_0(32)\), \(d=32(1+1/2)=48\). If \(g_E-f_{32}\) were nonzero it would have order at least nine, exceeding \(2\cdot48/12=8\). Thus \(g_E=f_{32}\). The conductor and elliptic modularity are precisely stated inputs; the coefficient calculations and the all-coefficient identification are proved here.

## 5. A dihedral weight-one form of level 23

Put \(K=\mathbb Q(\sqrt{-23})\), \(\vartheta=(1+\sqrt{-23})/2\). Then
\(\mathcal O_K=\mathbb Z[\vartheta]\), \(\vartheta^2-\vartheta+6=0\), and
\[
N(a+b\vartheta)=a^2+ab+6b^2.
\tag{5.1}
\]
The norm equals \((a+b/2)^2+23b^2/4\), so the only units are \(\pm1\). We calculate the class group, rather than assuming its order. Minkowski's ideal-class bound gives an integral representative of norm at most \((2/\pi)\sqrt{23}<4\). The primes two and three split, since their defining polynomial is \(X(X-1)\) modulo each. Set \(\mathfrak p=(2,\vartheta)\) and \(\mathfrak q=(3,\vartheta)\). Then
\[
(\vartheta)=\mathfrak p\mathfrak q,
\qquad (\vartheta+1)=\overline{\mathfrak p}^{\,3}.
\tag{5.2}
\]
The first equality follows from divisibility and norm six. For the second, \(N(\vartheta+1)=8\), and \(\vartheta+1\) is not in \(\mathfrak p\); all its factors are therefore the conjugate prime. The class of \(\mathfrak p\) has order dividing three. It is nontrivial, because (5.1) cannot equal two: \(b\ne0\) gives norm at least \(23/4\), while \(b=0\) gives a square. Every class has a representative of norm one, two or three, and (5.2) identifies the norm-three classes with the two norm-two classes. Hence
\(\operatorname{Cl}(K)=\langle[\mathfrak p]\rangle\simeq C_3\).

Choose \(\xi([\mathfrak p])=\zeta_3\). It is an unramified finite-order Hecke character, and \(\xi^\sigma=\xi^{-1}\ne\xi\). The quadratic induction is an irreducible dihedral representation. Define
\[
\Theta_0=\sum_{a,b\in\mathbb Z}q^{a^2+ab+6b^2},
\qquad
\Theta_1=\sum_{a,b\in\mathbb Z}q^{2a^2+ab+3b^2}.
\tag{5.3}
\]
The class-character ideal series is
\[
F(z)=\sum_{\mathfrak a\subset\mathcal O_K}\xi(\mathfrak a)q^{N\mathfrak a}
       =\frac{\Theta_0-\Theta_1}{2}.
\tag{5.4}
\]
To prove the equality, for a representative ideal \(A\), integral ideals in class \([A]^{-1}\) are \((\alpha)A^{-1}\) with \(0\ne\alpha\in A\), modulo the two units, and have norm \(N\alpha/NA\). For \(A=\mathcal O_K\) this gives \((\Theta_0-1)/2\). The basis \(2,\vartheta\) of \(\mathfrak p\) gives \(N(2a+b\vartheta)/2=2a^2+ab+3b^2\). Its conjugate gives the minus cross term, with the same theta series after \(a\mapsto-a\). The two class weights add to \(\zeta_3+\zeta_3^{-1}=-1\), giving (5.4); the constant terms cancel.

The two Gram matrices are \(A_0=\bigl(\begin{smallmatrix}2&1\\1&12\end{smallmatrix}\bigr)\), \(A_1=\bigl(\begin{smallmatrix}4&1\\1&6\end{smallmatrix}\bigr)\). Each has determinant 23 and lattice level 23, since \(23A_j^{-1}\) is integral with even diagonal and no smaller positive integer has that property. The stated lattice-theta theorem of [LG-MF-14](https://kokunoyumeto.github.io/open-math-courses-public/courses/LG-MF/LG-MF-14.html), Theorem 6.1, gives weight one and character \(\epsilon_{-23}\), including holomorphy at every cusp.

There are two cusps, infinity and zero. At infinity the constant term of each \(\Theta_j\) is one. At zero use ordinary two-dimensional Poisson summation:
\[
\Theta_j(-1/(23z))=-i\sqrt{23}\,z\,\Theta_j(z).
\tag{5.5}
\]
Indeed \(\theta_A(-1/z)=(-iz)(\det A)^{-1/2}\theta_{A^{-1}}(z)\); replacing \(z\) by \(23z\) yields (5.5), because \(23A^{-1}=\operatorname{adj}(A)=JAJ^t\) for \(J=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)\), an integral change of basis. With determinant-normalized weight-one Fricke slash, the constants at zero are the same common nonzero multiple of the constants at infinity. Their difference is zero. Thus \(F\) is cuspidal, with first terms \(q-q^2-q^3+\cdots\).

The eta-quotient criterion, stated in Allen–Anderson–Hamakiotes–Oltsik–Swisher, Theorems 1.2 and 1.4, shows
\[
G(z)=\eta(z)\eta(23z)\in S_1(\Gamma_0(23),\epsilon_{-23}).
\tag{5.6}
\]
Both required sums are \(1+23=24\); the character is \((\frac{-23}{d})\). The cusp-order formula gives order one at each cusp. Also
\(G=q\prod_{n\ge1}(1-q^n)(1-q^{23n})=q-q^2+O(q^3)\).
If \(F-G\) were nonzero it would have order at least three, whereas (4.5) gives the bound \(1\cdot24/12=2\). Therefore \(F=G\). Direct expansion gives
\[
F=q-q^2-q^3+q^6+q^8-q^{13}-q^{16}+q^{23}
 -q^{24}+q^{25}+q^{26}+q^{27}-q^{29}-q^{31}+O(q^{32}).
\tag{5.7}
\]

For clarity, its Hecke eigenform property follows from the ideal Euler product as well. At a split \(p\ne23\), \(\xi(\mathfrak p)\xi(\overline{\mathfrak p})=1\), and the factor is \((1-a_pT+T^2)^{-1}\). At an inert \(p\), the unique prime has norm \(p^2\) and is principal, giving \((1-T^2)^{-1}\), which equals the degree-two formula with \(\epsilon_{-23}(p)=-1\) and \(a_p=0\). At 23 the ramified ideal has class of order dividing two and hence trivial in \(C_3\); its factor is \((1-T)^{-1}\). Unique ideal factorization gives multiplicativity and the prime-power recurrences. The weight-one formula for \(T_p\) now gives \(T_pF=a_pF\), and \(U_{23}F=F\), by equality of every Fourier coefficient. Its character has conductor 23, so it cannot be an oldform from level one. It is a normalized primitive weight-one form.

Let \(H\) be the Hilbert class field of \(K\). Reciprocity gives \(\operatorname{Gal}(H/K)=C_3\), with complex conjugation acting by inversion, hence \(\operatorname{Gal}(H/\mathbb Q)=S_3\). A concrete description is the splitting field of \(P(X)=X^3-X-1\). The polynomial is irreducible by the rational-root test, and its discriminant \(-4(-1)^3-27(-1)^2=-23\) is not a square. Its group is therefore \(S_3\), with quadratic subfield \(K\). Only 23 ramifies. Modulo 23 it factors as
\(P(X)=(X-10)^2(X-3)\).
Here is the ramification check in the splitting field \(L\), before identifying \(L\) with \(H\). At \(p\ne23\), the integral roots have pairwise distinct residues: the product of the squares of their differences is the unit discriminant. Inertia preserves residues and permutes the roots, so it fixes each root and is trivial. At 23 the inertia order divides six and is prime to 23. Tame inertia is cyclic, by Milne, *Algebraic Number Theory*, Corollary 7.59. Its image in \(S_3/A_3\) is nontrivial, since the quadratic field of discriminant \(-23\) ramifies at 23. The only cyclic subgroup of \(S_3\) with nontrivial sign has order two, so inertia is generated by a transposition. Its intersection with \(A_3\) is trivial. Thus \(L/K\) is an everywhere unramified cyclic cubic extension; \(K\) has no real infinite places to check. Its degree and the class-number calculation identify it with the Hilbert class field by reciprocity and existence.

The finite-order \(\xi\) gives a character of \(\operatorname{Gal}(H/K)\). Its induction is the standard irreducible two-dimensional representation of \(S_3\). Complex conjugation is a transposition, with eigenvalues \(1,-1\), so it is odd. For \(p\ne23\), (1.2) and (5.4) show that \(a_p(F)\) is its Frobenius trace:

| Frobenius in \(S_3\) | Splitting in \(K\) | Splitting in \(H/\mathbb Q\) | \(P\bmod p\) factor degrees | \(a_p\) |
|---|---|---|---|---:|
| identity | split, principal prime ideals | six primes of degree one | \(1,1,1\) | 2 |
| transposition | inert | three primes of degree two | \(1,2\) | 0 |
| three-cycle | split, nonprincipal prime ideals | two primes of degree three | \(3\) | −1 |

The degree pattern in the third column is the Galois extension's pattern, whereas the fourth is the cubic subfield's pattern. They are different statements. At the excluded ramified prime, \(a_{23}=1\), not one of the three unramified cases. As sample checks, \(P\) is irreducible modulo \(2,3,13,29,31\), giving \(-1\); modulo five it has the single root two, giving zero. At 59 it has three distinct roots and gives two.

For real quadratic \(K\), infinity instead splits into two real characters. Their induction is a real principal series, so this construction gives Maass forms rather than the holomorphic discrete series above. For example, if a norm-one unitary Hecke character has infinite components \(|x_1|^{it}|x_2|^{-it}\), invariance under a totally positive unit \(\epsilon\) requires \(2t\log\epsilon\in2\pi\mathbb Z\), after fixing the embedding with \(\epsilon>1\). The corresponding spherical infinity type has Laplace eigenvalue \(1/4+t^2\). The finite-order signs and any finite conductor must also satisfy the unit relation; an arbitrary choice of \(t\) is not a Hecke character.

## 6. The analytic Artin criterion and its boundary

**Analytic criterion — proved as Theorem 6.10 below.** Let \(F\) be a global field, and \(\rho\) a two-dimensional representation of a relative Weil group for a finite Galois extension. Suppose that, for every idele-class quasicharacter \(\omega\), both complete functions
\[
L^*(s,\rho\otimes\omega),\qquad
L^*(s,\rho^\vee\otimes\omega^{-1})
\tag{6.1}
\]
are entire and bounded on every finite-width closed vertical strip. With the Artin–Hecke local factors and their epsilon functional equations, the local corresponding \(\pi(\rho_v)\) exists at every place, and its tensor product is cuspidal automorphic. This is Jacquet–Langlands, Theorem 12.2. Over \(\mathbb Q\) it applies, in particular, to a finite-image irreducible two-dimensional complex Galois representation satisfying these analytic conditions.

The all-twist hypotheses identify every exceptional local component, not only almost all of them. In the original proof, Lemma 12.3 shows that agreement of Weil representations at almost every place implies their global equivalence. Lemma 12.4 uses Brauer's induction to identify the pole order at one with the trivial-representation multiplicity, and Lemma 12.5 prescribes a local character while forcing high ramification at the other exceptional places. These comparisons and local pole tests rule out the wrong principal or special component, and the converse theorem supplies the global realization. This explains why one untwisted entire function is insufficient for this particular theorem.

Proposition 12.6 is a different historical conditional result: an analyticity assertion for all irreducible degree-two Weil representations over every finite extension of the global field implies local correspondence existence. Its hypothesis is not established by one example. Modern local Langlands gives local correspondence directly; see Getz–Hahn, §§12.3–12.4. We do not infer a proof of general Artin automorphy from that local existence.

For finite-image \(\rho\), the strong Artin conjecture predicts an automorphic representation compatible at all places, cuspidal when \(\rho\) is irreducible. The induction case above proves the dihedral example. Getz–Hahn, §13.4, Theorems 13.4.5–13.4.6, states the solvable projective-image results and the odd two-dimensional case over totally real fields. Over \(\mathbb Q\), odd finite-image representations have holomorphic weight-one realizations. Even representations have real principal-series infinity type and lead instead to Maass forms; the general even icosahedral case is not asserted to be solved here. The Artin criterion itself has no oddness hypothesis: parity determines the real type of its conditional conclusion.

### 6.1. Hecke nonvanishing and the Weil pole comparison

The two analytic families in Section 6 must exclude a global Eisenstein pair before the exceptional-set converse can give a cusp form. We give the pole argument and its finite representation calculation explicitly. They use Artin local factors, not a local Langlands correspondence.

**Lemma 6.1 — unitary Hecke functions on the closed right half-plane.** Let \(E\) be any global field and \(\chi\) a unitary Hecke character. Its finite Hecke Euler product has no zero for \(\operatorname{Re}s\ge1\). On the boundary, its possible poles are the norm-character translates of the zeta pole; at one the trivial character has its simple pole. At \(s=1\) a nontrivial character is holomorphic and nonzero. Removing finitely many finite Euler factors does not change these assertions at one.

**Proof.** Absolute convergence of the logarithmic Euler series gives nonvanishing for \(\operatorname{Re}s>1\). Tate continuation over number fields, or the finite Poisson proof of Lemma 2.4 in function fields, gives holomorphy at one for every nontrivial unitary character. A character trivial on the norm-one group is a pure imaginary norm power; its possible poles are the corresponding translates of the two zeta poles, so it has a pole at one precisely when the character itself is trivial. Infinite-place unitary Tate gamma factors are finite and nonzero at one, so this assertion holds for the finite Euler product too. The same Poisson proof gives a simple pole of \(\zeta_E(s)\) at one with nonzero positive residue: its zero-term contribution is a nonzero positive Haar volume, divided by the simple continuous or discrete norm denominator.

For real \(\sigma>1\), the logarithmic Euler expansions and
\(3+4\cos t+\cos(2t)=2(1+\cos t)^2\ge0\) give
\[
\zeta_E(\sigma)^3|L_0(\sigma,\chi)|^4
|L_0(\sigma,\chi^2)|\ge1.
\tag{6.2}
\]
At an unramified place its prime-power contribution is this nonnegative expression with \(e^{it}=\chi(\varpi)^n\). At a ramified place omit the missing \(\chi\)-factor; the contribution is either \(3\), or \(3+\operatorname{Re}\chi^2(\varpi)^n\ge2\) if \(\chi^2\) is unramified. Thus the inequality includes every finite place.

If \(\chi^2\ne1\) and \(L_0(s,\chi)\) had a zero at one of order \(r\ge1\), the left side would be \(O((\sigma-1)^{4r-3})\), since \(L_0(s,\chi^2)\) is holomorphic there. It would tend to zero, contradicting (6.2). If \(\chi^2=1\) but \(\chi\ne1\), global class field existence gives its quadratic extension \(E'/E\). The complete finite Euler induction identity is
\(\zeta_{E'}(s)=\zeta_E(s)L_0(s,\chi)\), including ramified and constant-field places. Both zeta functions have simple poles with nonzero residues at one. Their quotient is therefore finite and nonzero there. This proves the quadratic case as well.

For \(s=1+it\), replace \(\chi\) by \(\chi|\cdot|^{it}\) and apply the just-proved assertion at one. At a removed finite place the factor is one or \((1-\chi(\varpi)q^{-1})^{-1}\), analytic and nonzero because \(|\chi(\varpi)|=1\). This proves the lemma. \(\square\)

For the finite relative Weil groups used below, the coefficient group is \(C_K\), and the relative fundamental class is the class of NT-CFT-24, Theorem 24.6. Its restriction to a subgroup gives the relative group for the corresponding intermediate field. The algebraic transfer calculation of that lesson, equations (29)–(32), identifies the abelianization of \(W_{K/E}\) with \(C_E\). This finite-extension calculation applies to both kinds of global fields: it uses the class-formation cup isomorphism and the norm index, not an infinite-place argument. For the topology, transfer on the coefficient subgroup is the norm \(C_K\to C_E\), which is open onto its finite-index norm subgroup. Transfer on the whole finite relative group is consequently open as well. Its kernel meets each of its finitely many coefficient cosets in a closed translate of a subgroup of \(C_K^1\): idèlic norm preserves the absolute global norm, so kernel elements have fixed coefficient norm. The norm-one group is compact over both kinds of fields. Hence this kernel is compact and closed, and the quotient has exactly the topology of \(C_E\). The norm-coordinate group is a real line in number fields and a discrete degree group in function fields; this changes no step in the finite class-formation calculation. Consequently a continuous one-dimensional representation of \(W_{K/E}\) is exactly a Hecke quasicharacter of \(E\). These finite relative statements suffice; no absolute inverse-limit group is needed in the following proof.

**Lemma 6.2 — the unitary Weil pole test.** Let \(R\) be a unitary finite-dimensional representation of \(W_{K/F}\). Its finite Artin Euler product has a meromorphic continuation near one, and the order of its pole there is
\[
\dim\operatorname{Hom}_{W_{K/F}}(1,R).
\tag{6.3}
\]
Omitting any finite set of finite places gives the same order.

**Proof: a finite character calculation.** The commuting unitary operators from \(C_K\) decompose the space into finitely many character spaces. The finite quotient \(G=\operatorname{Gal}(K/F)\) permutes their characters. For each orbit choose a character \(\theta\), let \(H\le G\) stabilize it, and let \(T\) be the corresponding \(W_H\)-representation on its character space. Then \(R\) is the sum of \(\operatorname{Ind}_{W_H}^{W_{K/F}}T\) over these orbits. On \(C_K\), \(T\) is the scalar character \(\theta\).

Choose one lift for every element of \(H\). The lift matrices of \(T\) give a projective representation of this finite group, with scalar unitary cocycle obtained by applying \(\theta\) to the relative Weil cocycle. Projective characters for this one fixed cocycle are orthonormal by Schur orthogonality: average an intertwining matrix over the finite group, and the common cocycle cancels in the conjugation. This is the same finite proof as for ordinary characters.

For a cyclic subgroup \(C\le H\), \(\theta\) extends to a unitary character of \(W_C\). Indeed a lift \(t\) of its generator satisfies \(t^{|C|}\in C_K\); choose a unit-modulus \(|C|\)-th root of \(\theta(t^{|C|})\) for its value. Invariance of \(\theta\) under \(C\) proves the relation, and the finitely many open coefficient cosets prove continuity. The extensions differ by the ordinary characters of \(C\).

The representations induced from all these extensions span the finite projective character space over \(\mathbb C\). To see this, suppose a virtual projective character is orthogonal to them all. Finite Frobenius reciprocity makes its restriction to every cyclic subgroup orthogonal to every extension of \(\theta\). After removing one chosen extension, the ordinary characters of that cyclic group are a basis, so the restriction is zero. Every element generates a cyclic subgroup; hence the virtual character is identically zero. Projective Schur orthogonality then makes the original virtual character zero. Orthogonal-complement zero proves the spanning assertion.

It follows, after inducing to the full Weil group and summing orbits, that the character of \(R\) is a finite complex linear combination
\[
\operatorname{char}R=
\sum_j z_j\operatorname{char}
\operatorname{Ind}_{W_{K/E_j}}^{W_{K/F}}\gamma_j,
\qquad z_j\in\mathbb C,
\tag{6.4}
\]
where every \(\gamma_j\) is a unitary Hecke character of the intermediate field \(E_j\). Integral Brauer induction would give a stronger expression; complex spanning is enough here because the proof compares logarithmic derivatives and residues, rather than declaring a fractional product of meromorphic functions.

**Proof: Euler derivatives and the residue.** Artin induction gives
\(L_{0,F}(s,\operatorname{Ind}\gamma_j)=L_{0,E_j}(s,\gamma_j)\).
For completeness the local identity follows by decomposing the inertia invariants into the orbits of Frobenius on the induced cosets. An orbit of length \(f\) contributes \(1-bq_v^{-fs}\), with \(b\) the product of its character scalars; this is the factor at the corresponding place of \(E_j\), whose residue cardinality is \(q_v^f\). This calculation includes ramified places, by first taking inertia invariants.

In a common right half-plane, expand \(-\log\det(1-q_v^{-s}\mathrm{Frob}_v)\) as the sum of traces of its powers. The character identity (6.4) therefore gives
\[
\frac{L'_{0,F}}{L_{0,F}}(s,R)=
\sum_j z_j\frac{L'_{0,E_j}}{L_{0,E_j}}(s,\gamma_j).
\tag{6.5}
\]
By Lemma 6.1, the right side has near one only the simple pole contributed by trivial \(\gamma_j\), whose residue is \(-\sum_{\gamma_j=1}z_j\). Frobenius reciprocity in (6.4) identifies this sum with \(m=\dim\operatorname{Hom}(1,R)\). Thus (6.5) is \(-m/(s-1)+h(s)\), with \(h\) holomorphic near one. Integrating on a punctured neighbourhood continues the initial Euler product as \((s-1)^{-m}\exp(H(s))\), with \(H\) holomorphic and an initial nonzero constant. Since \(m\) is an integer, this continuation is single-valued and meromorphic there. Its pole has exactly order \(m\).

All eigenvalues on local inertia invariants have absolute value one. Their omitted Euler polynomials are consequently nonzero at one, since \(q_v^{-1}<1\). They do not change the pole order. This proves (6.3). \(\square\)

**Lemma 6.3 — almost-everywhere Weil equivalence.** Two semisimple continuous finite-dimensional representations \(R,T\) of the same relative Weil group are equivalent if their local restrictions are equivalent outside a finite set of places.

**Proof.** First suppose they are unitary. If \(A\) is any irreducible unitary constituent of \(R\), the local tensor representations \(R^\vee\otimes A\) and \(T^\vee\otimes A\) agree outside that finite set. Their incomplete finite Euler products agree initially; Lemma 6.2 gives equal pole orders at one. These orders are respectively
\(\dim\operatorname{Hom}(R,A)\) and \(\dim\operatorname{Hom}(T,A)\).
Hence each constituent of \(R\) occurs in \(T\) with the same multiplicity. Local equivalence also gives equality of the total dimensions, so there are no remaining constituents in \(T\).

In general the coefficient action is semisimple as follows. In an irreducible Weil representation, the commuting coefficient matrices have a common eigenvector. The sum of their actual joint eigenspaces is nonzero and is preserved by the finite quotient, which permutes the coefficient characters; irreducibility makes this sum the whole representation. Apply this to each simple summand. Thus the \(C_K\)-action can be diagonalized. The absolute value of each of its quasicharacters is a real norm power, because \(C_K^1\) is compact. Group the character spaces by that real exponent \(a\). Conjugation by the finite Galois quotient preserves the norm, so each grouped space is Weil-invariant. Removing the scalar norm power \(|\cdot|^a\) makes its coefficient action unitary; averaging an inner product over the finitely many quotient cosets makes the whole grouped Weil representation unitary. Thus each representation is a direct sum of unitary representations times real norm powers.

The local restriction identifies these groups separately: on a local coefficient group every character in the group indexed by \(a\) has absolute value \(|\cdot|^a\), and that local module has a nontrivial norm coordinate. A local intertwiner therefore preserves the groups indexed by \(a\). Apply the unitary argument to each group after its common norm twist. This proves global equivalence. \(\square\)

**Corollary 6.4 — exclusion of an Eisenstein pair.** Let \(\rho\) be the two-dimensional Weil representation of Section 6, and suppose its entire all-twist family holds. Its good local factors cannot be those of a global Hecke pair \(\mu\oplus\nu\) at almost every place.

**Proof.** Such local agreement and Lemma 6.3 would give \(\rho\simeq\mu\oplus\nu\) globally. Twisting by \(\mu^{-1}\) and \(\nu^{-1}\) gives respectively the products
\[
\zeta_F(s)L_F(s,\nu/\mu),
\qquad \zeta_F(s)L_F(s,\mu/\nu).
\tag{6.6}
\]
Write \(\nu/\mu=\chi|\cdot|^a\), with \(\chi\) unitary and \(a\in\mathbb R\); imaginary norm powers are included in \(\chi\). If \(a\ge0\), Lemma 6.1 makes the first remaining factor nonzero at \(s=1\), or gives it a pole, since it is evaluated at \(1+a\) in the closed right half-plane. If \(a\le0\), the same statement holds for the second remaining factor, evaluated at \(1-a\). Infinite-place Tate factors at these points are finite and nonzero for a unitary character at real part at least one. In either case one completed product in (6.6) retains a pole at one, contradicting the assumed entireness. This excludes the pair. \(\square\)

The comparison locators are Jacquet–Langlands, Lemmas 12.3–12.4, printed pp. 208–210. The complex cyclic spanning and logarithmic-residue proof above supplies precisely the needed pole assertion without using a general automorphy theorem or treating a nonintegral character expression as a literal meromorphic product.

### 6.2. Character interpolation and the two stability calculations

The Artin local constants in this section have Tate's one-dimensional normalization, are multiplicative on virtual representations, and obey induction for virtual dimension zero. Their existence and full global functional equation are the Artin–Hecke inputs in Section 6. The written local conductor and epsilon prerequisites use geometric reciprocity. Here a one-dimensional Weil character is first transported to the actual idèlic character in this course’s arithmetic convention, and its epsilon factor is Tate’s positive-kernel factor for that character. Inertia invariants, conductor sums, induction of dimension-zero differences and determinant transfer are independent of the Frobenius choice. Every phase below is then derived from the idèlic character formula; no geometric Frobenius eigenvalue or root number is copied into an arithmetic formula. We use self-dual measures and the positive Fourier kernel throughout. These are explicit inputs; writing a Brauer product alone would not prove their existence or its independence of choices.

**Lemma 6.5 — the rank-zero Brauer refinement.** For a finite group \(G\), every virtual representation \(X\) of dimension zero is an integer sum of \(\operatorname{Ind}_H^G(\theta-1)\), with \(\theta\) one-dimensional.

**Proof.** The written Brauer theorem RT-FIN-11, Theorem 5.1, gives an integral expression \(1_G=\sum_j n_j\operatorname{Ind}_{E_j}^G\lambda_j\), with elementary, hence nilpotent, \(E_j\). Multiply by \(X\) and apply the projection formula. It suffices to handle the rank-zero virtual representation \((\operatorname{Res}_{E_j}X)\lambda_j\) in a finite nilpotent group \(E_j\).

Every subgroup \(H\) of a finite nilpotent group \(E\) has a subnormal chain to \(E\), refinable to steps of prime cyclic quotient. Indeed a proper subgroup is strictly contained in its normalizer: take the first term of the upper central series not contained in it; an element of that term outside the subgroup normalizes it, since all its commutators lie in the preceding term. Iterating the normalizer reaches \(E\). The quotients in this normal chain are nilpotent; their composition factors are simple nilpotent groups, hence cyclic of prime order. Refining yields the asserted chain.

For a normal step \(H\triangleleft J\) with \(J/H\) cyclic of prime order \(p\),
\(\operatorname{Ind}_H^J1-p1_J=\sum_{\alpha\ne1}(\alpha-1_J)\), where \(\alpha\) runs over the nontrivial characters of that quotient. Induce these identities along the chain and telescope. This expresses \(\operatorname{Ind}_H^E1-[E:H]1_E\) as an integer sum of induced character differences. Every irreducible of \(E\) is monomial by RT-FIN-11, Theorem 1.2. For \(V=\operatorname{Ind}_H^E\theta\), subtract its dimension times the trivial representation: the difference is \(\operatorname{Ind}_H^E(\theta-1)\) plus the just-treated permutation difference. Rank-zero virtual representations are integer sums of these differences. Induction in stages now proves the lemma for \(G\). \(\square\)

**Lemma 6.6 — the high-character Tate calculation.** Let \(F\) be a finite-place field, of either characteristic, and \(\psi\) have additive annihilator \(\mathfrak p^{-n}\) on \(\mathcal O\). For a character \(\chi\) of sufficiently high conductor \(a\), choose \(c_\chi\in F^\times\), of valuation \(a+n\), such that
\[
\chi(1+x)=\psi(x/c_\chi)
\quad\text{on a sufficiently deep unit subgroup.}
\tag{6.7}
\]
For each of finitely many fixed finite separable extensions \(E/F\) and fixed characters \(\theta_E\), increasing \(a\) if necessary gives
\[
\frac{\epsilon_E(s,\theta_E(\chi\circ N_{E/F}),\psi\circ\operatorname{Tr}_{E/F})}
{\epsilon_E(s,\chi\circ N_{E/F},\psi\circ\operatorname{Tr}_{E/F})}
=\theta_E(c_\chi).
\tag{6.8}
\]
The same \(c_\chi\) is regarded as an element of \(E\) on the right.

**Proof.** On \(\mathfrak p^r/\mathfrak p^a\), with \(2r\ge a\), the law of \(1+x\) is the additive law. Additive self-duality therefore expresses the restriction of \(\chi\) as \(x\mapsto\psi(x/c_\chi)\). Its exact conductor gives \(v_F(c_\chi)=a+n\). Its ambiguity is multiplication by \(1+\mathfrak p^{a-r}\): equality of the two additive restrictions is equivalent to the difference of their inverse elements annihilating \(\mathfrak p^r\). Since \(r=\lceil a/2\rceil\), this depth tends to infinity.

Fix \(E/F\), let \(e=e(E/F)\) and \(d=v_E(\mathfrak D_{E/F})\). Trace duality gives \(n_E=e n+d\). Choose \(r_E=\lceil ea/2\rceil+C_E\), with a fixed sufficiently large \(C_E\). The trace of \(\mathfrak p_E^{r_E}\) then belongs to the base-field subgroup on which (6.7) holds. To justify the estimate in either characteristic, take the separable embeddings in a normal closure. Every conjugate of \(y\) has base-normalized valuation at least \(r_E/e\). Each elementary symmetric term of degree \(k\ge2\) consequently has valuation at least \(kr_E/e\); the ultrametric inequality preserves this bound in its sum. Thus \(N(1+y)-1-\operatorname{Tr}y\) belongs to \(\mathfrak p_F^a\). Trace duality gives \(\operatorname{Tr}(\mathfrak p_E^{r_E})\subset\mathfrak p_F^{\lfloor(r_E+d)/e\rfloor}\), which is inside \(\mathfrak p_F^{\lceil a/2\rceil}\) after the fixed choice of \(C_E\). Dividing the norm by \(1+\operatorname{Tr}y\) changes it by an element of \(1+\mathfrak p_F^a\), killed by \(\chi\). Thus
\[
(\chi\circ N)(1+y)=\psi_E(y/c_\chi)
\quad(y\in\mathfrak p_E^{r_E}).
\]
For all sufficiently large \(a\), this determines its exact conductor
\(a_E=v_E(c_\chi)-n_E=ea-d\): the displayed character is trivial on \(\mathfrak p_E^{a_E}\) and nontrivial on \(\mathfrak p_E^{a_E-1}\), both contained in the range just considered. In particular \(a_E-r_E\) tends to infinity.

The primitive Tate test, as calculated in Lemma 2.4 and in NT-ADL-07, gives for any character \(\xi\) of conductor \(a_E\)
\[
\epsilon_E(s,\xi,\psi_E)
=\xi(c_\chi)q_E^{a_E/2}|c_\chi|_E^{s-1/2}
\int_{\mathcal O_E^\times}\xi(u)^{-1}\psi_E(u/c_\chi)du_0,
\tag{6.9}
\]
when \(v_E(c_\chi)=a_E+n_E\); here \(du_0\) is additive measure with \(\operatorname{vol}(\mathcal O_E)=1\). Rescaling \(c_\chi\) by a unit changes the integral by the inverse character value, so the formula is independent of that choice.

Partition the unit integral into cosets \(u_0(1+\mathfrak p_E^{r_E})\). For \(\xi=\chi\circ N\), its inner factor is the additive integral of \(\psi_E((u_0-1)y/c_\chi)\). It is zero unless \(v_E(u_0-1)\ge a_E-r_E\). Make this last bound exceed the conductor of the fixed \(\theta_E\), and also make \(r_E\) exceed it. On every surviving coset, \(\theta_E(u)=1\). The two integrals for \(\xi\) and \(\theta_E\xi\) are therefore identical. Their conductors are equal, and the only remaining ratio in (6.9) is \(\theta_E(c_\chi)\). This proves (6.8) in all residue characteristics, including characteristic two. The allowed ambiguity in \(c_\chi\) is deep enough to be killed by every fixed character used. \(\square\)

**Lemma 6.7 — highly ramified Artin stability.** For any smooth finite-dimensional semisimple local Weil representation \(R\), and all characters \(\chi\) of sufficiently high conductor,
\[
L(s,R\otimes\chi)=L(1-s,R^\vee\otimes\chi^{-1})=1,
\qquad
\epsilon(s,R\otimes\chi,\psi)
=\epsilon(s,\chi,\psi)^{\dim R}\det R(c_\chi).
\tag{6.10}
\]
The determinant is evaluated on the local idèlic character corresponding to \(\det R\).

**Proof.** For an irreducible \(R\), inertia has finite image. Some power of a Frobenius lift centralizes that finite image and hence, by Schur's lemma, is a scalar on \(R\). Remove an unramified character \(\zeta\) whose corresponding power is that scalar. The remaining representation \(R_0\) has finite image. Such a finite continuous quotient of the local Weil group is the Galois group of a finite extension, by its profinite completion; inverse images of its subgroups are the Weil groups of the intermediate fields. Lemma 6.5 therefore gives
\([R_0]-d[1]=\sum_j m_j\operatorname{Ind}_{W_{E_j}}^{W_F}(\theta_j-1)\).
After tensoring by \(\zeta\chi\), each difference still has virtual dimension zero. Induction of epsilon constants transports it exactly to
\(\theta_j(\zeta\chi)\circ N-(\zeta\chi)\circ N\)
over \(E_j\). Formula (6.8) gives the ratio \(\theta_j(c_\chi)\). Unramified \(\zeta\) does not affect the critical-unit identity (6.7).

The determinant of a dimension-zero induced difference is the determinant character transferred to the extension; the permutation determinant cancels. Transfer on idèles is the inclusion \(F^\times\subset E_j^\times\). Hence the product of these ratios is \(\det R_0(c_\chi)\). The one-dimensional case of (6.8) gives \(\epsilon(s,\zeta\chi)=\zeta(c_\chi)\epsilon(s,\chi)\). Multiplying its \(d\) copies proves (6.10). Additivity proves it for any semisimple \(R\).

For the \(L\)-assertion choose a sufficiently deep upper inertia group on which \(R\) and its dual are trivial but \(\chi\) is nontrivial. Any inertia-fixed vector in the twist would be fixed by that nontrivial scalar action, and so is zero. The local determinant factors are consequently one. This uses only the upper ramification filtration and character conductor correspondence, with their precise hypotheses recorded in the local conductor prerequisite. \(\square\)

**Lemma 6.8 — highly ramified automorphic stability.** Let \(\pi\) be an infinite-dimensional irreducible local representation with unitary central character \(\eta\). For every sufficiently highly ramified \(\chi\),
\[
L(s,\pi\otimes\chi)=L(1-s,\widetilde\pi\otimes\chi^{-1})=1,
\qquad
\epsilon(s,\pi\otimes\chi,\psi)
=\epsilon(s,\chi\eta,\psi)\epsilon(s,\chi,\psi).
\tag{6.11}
\]

**Proof.** First take \(\psi\) of conductor \(\mathcal O\). In every compact Kirillov part use the same vector \(f_0=1_{\mathcal O^\times}\). Smoothness gives an integer \(r\) such that the lower unipotent matrices \(\bar n(x)\), \(x\in\mathfrak p^r\), fix it. For \(\chi\) of conductor \(a\ge r\), put \(f_\chi=\chi^{-1}1_{\mathcal O^\times}\). Its finite primitive Fourier transform is supported on \(\mathfrak p^{-a}\mathcal O^\times\), by Lemma 2.4's shell calculation. Fourier inversion gives the finite vector integral
\[
f_\chi=\int\widehat f_\chi(-b)\pi(n(b))f_0\,db.
\]
The exact matrix relation is
\[
w_0n(b)=n(-b^{-1})(-b)I\,d(b^{-2})\bar n(b^{-1}).
\tag{6.12}
\]
On the integration shell the last factor fixes \(f_0\). Therefore its Weyl transform is the universal formula
\[
(\pi(w_0)f_\chi)(t)=
\int\widehat f_\chi(-b)\eta(-b)\psi(-t/b)
1_{\mathcal O^\times}(tb^{-2})db.
\tag{6.13}
\]
It depends only on \(\eta\), not on \(\pi\). All integrals here are over compact shells and finite locally constant quotients; no unbounded oscillatory interchange is used.

The principal and special germ formulas of Lesson 9 show that both twist \(L\)-factors are one when \(a\) exceeds their fixed unit-character conductors; supercuspidal twists already have both factors one. The original twisted Mellin integral of \(f_\chi\) equals one. Its dual Weyl integral is therefore exactly the epsilon factor by Lesson 9, Theorem 3.2. Formula (6.13) proves equality of those factors for any two such representations with central character \(\eta\). Compare with \(I(\eta,1)\), irreducible because \(\eta\) is unitary and cannot be \(|\cdot|^{\pm1}\). Its two-character epsilon formula is Lesson 9, Theorem 4.1, giving (6.11). A changed additive character has the determinant-and-module multiplier of Lesson 9, Section 6; it is the same for both representations. This proves the formula for every \(\psi\). \(\square\)

By Lemma 6.6 in the base field, (6.10) for a two-dimensional \(R\) can also be written \(\epsilon(s,\chi\det R,\psi)\epsilon(s,\chi,\psi)\). Thus (6.10) and (6.11) agree exactly when \(\eta=\det R\); their phases, not merely their conductor powers, agree.

**Lemma 6.9 — one local character and fixed unit restrictions elsewhere.** Let \(v_0\) belong to a finite set \(S\) of finite places. Given a local quasicharacter \(\chi_{v_0}\) and unitary characters \(\theta_v\) of \(\mathcal O_v^\times\), \(v\in S\setminus\{v_0\}\), there is a global Hecke quasicharacter with that complete local component at \(v_0\) and those unit restrictions at the other places. In particular their conductors can be forced as high as prescribed.

**Proof.** First remove the real local norm power of \(\chi_{v_0}\). Consider the idèles supported in \(S\), arbitrary at \(v_0\) and unit at all the other places. Their intersection with \(F^\times\) is one, because a rational element with component one outside \(S\) is one. Their image in \(C_F\) is a closed embedded subgroup: in a bounded norm interval its \(v_0\)-valuations are bounded and all remaining coordinates are compact, so its intersection with that interval is compact; discreteness of \(F^\times\) proves closedness and the quotient embedding. Its unit part is consequently a closed compact subgroup of \(C_F^1\).

Every character of a closed subgroup of a compact abelian group extends to the group. Here is the needed compact argument. The group characters separate points, by the convolution Fourier-density proof in Lemma 4.8. Their restrictions form a self-adjoint unital algebra separating points on the closed subgroup, hence are uniformly dense there by Stone–Weierstrass. A given subgroup character cannot be orthogonal to all those restrictions; compact character orthogonality therefore makes it equal to at least one restriction. This proves extension.

Extend the prescribed product of unit characters to \(C_F^1\). Split the global norm as in Lemma 4.8. The chosen local uniformizer at \(v_0\) has a fixed compact component and a nonzero norm degree. A unitary character of the real or discrete norm group can take any prescribed unit-modulus value there: in the discrete case choose the requisite root. Choose this value to correct the value already contributed by the compact extension. The resulting global character has exactly the prescribed unit and uniformizer values. Restore the removed real norm power. This proves the lemma; choosing the other unit characters nontrivial on arbitrarily deep unit quotients gives the last assertion. Such characters exist because each deeper principal-unit quotient is a nonzero finite additive residue group. \(\square\)

### 6.3. The complete analytic criterion

**Theorem 6.10 — the Artin–Weil criterion with every local component.** Under the entire all-twist hypotheses and the Artin–Hecke full functional equations of Section 6, a two-dimensional continuous global Weil representation \(\rho\) has a corresponding infinite-dimensional generic local representation at every place, with its determinant, both full twisted \(L\)-families and every epsilon factor. Their restricted tensor product is cuspidal automorphic.

**Proof: unitary reduction and the partial data.** First pass to the global semisimplification. The finite inertia image makes inertia invariants exact, so the local determinant \(L\)-factors are multiplicative on exact sequences; the epsilon factors are multiplicative by their axiom, and the infinite-place factors use the same semisimplification. Thus both global analytic families are unchanged. Corollary 6.4 excludes a sum of two Hecke characters in this semisimplification. In dimension two that makes it irreducible, and therefore the original \(\rho\) itself was irreducible and equal to its semisimplification. Its coefficient characters have a common real norm exponent, since irreducibility makes their orbit transitive. The averaging argument of Lemma 6.3 makes \(\rho\) unitary after removing that norm power. The analytic hypotheses merely shift \(s\), so first work in this unitary case. Put \(\eta=\det\rho\).

At every infinite place, and at all but finitely many finite places, the corresponding generic local representation is already supplied by the direct-sum or quadratic models of Lessons 6, 10 and 11. In the unitary case a direct-sum ratio is unitary, so its normalized principal representation is irreducible and infinite-dimensional. Let \(S\) be the finite set still missing. At these places \(\rho_v\) is irreducible: reducible semisimple parameters have the known two-character model. Every twist of an irreducible two-dimensional finite-place Weil representation has zero inertia invariants. Otherwise irreducibility would make the invariants its whole space, and an unramified irreducible representation of the cyclic Frobenius group is one-dimensional. Thus both local \(L\)-families at \(S\) are one.

For \(v\in S\), let \(m_v=a(\rho_v)\), and let \(\mathfrak p_v^{-n_v}\) be the annihilator of \(\mathcal O_v\) for \(\psi_v\). The monomial Artin epsilon formula gives
\[
\epsilon(s,\rho_v\otimes\omega_v,\psi_v)
=b_v\omega_v(\varpi_v)^{m_v+2n_v}
q_v^{(m_v+2n_v)(1/2-s)}
\tag{6.14}
\]
for unramified \(\omega_v\), with \(b_v=\epsilon(1/2,\rho_v,\psi_v)\). This exponent and unramified-twist rule follow from rank-zero induction and the character formula, as in the local epsilon prerequisite, Theorem 4.1; alternatively the same rank-zero proof of Lemma 6.7, retaining the conductor instead of taking a high twist, gives it. The conductor is integral by the Artin conductor input. It is at least two here: the inertia-fixed dimension is zero, so the tame contribution is two and the Swan contribution is nonnegative. Thus the diagonal entries on \(K_0(\mathfrak p_v^{m_v})\) are units, as needed for the level characters below. Moreover \(a(\eta_v)\le m_v\): at each ramification subgroup the determinant's moved dimension is at most that of \(\rho_v\), so the conductor sum has this inequality.

Use the exceptional-set theorem of Lesson 15 with level \(m_v\),
\(e_v(k)=\eta_v(k_{22})\) and \(\widehat e_v(k)=\eta_v(k_{11})\) on diagonal residues. Set
\[
a_\alpha=1,\qquad
\widehat a_\alpha=\prod_{v\in S}b_v\eta_v(\alpha)
\quad\text{if }v(\alpha)=-n_v\text{ for every }v\in S,
\tag{6.15}
\]
and set both zero otherwise. The character conductor bound makes \(e,\widehat e\) well-defined on the stated level quotient. The coefficients are bounded, obey covariance for **all rational units at \(S\)**, and have the required additive-annihilator support. Weak approximation gives a rational \(\alpha\) with this valuation tuple, so the original coefficient function is nonzero.

For allowed \(\omega\), which is unramified at \(S\), there is just one rational-unit coset with this valuation tuple. Consequently
\[
\Lambda(s,\omega)=
\left(\prod_{v\in S}\omega_v(\varpi_v)^{-n_v}
q_v^{n_v(s-1/2)}\right)L(s,\rho\otimes\omega).
\tag{6.16}
\]
The hatted family at \(1-s,\eta^{-1}\omega^{-1}\) is
\(\prod_{v\in S}b_v\omega_v(\varpi_v)^{n_v}q_v^{n_v(1/2-s)}\)
times the completed dual function. These exponential factors preserve entireness and boundedness on finite-width strips. Choose \(A\in F^\times\) with \(v(A)=m_v\) at \(S\). Combining (6.14) with the complete Artin equation gives exactly Lesson 15, (4.25): its remaining scalar is \(\omega(-A_S)|A_S|^{s-1/2}\). Indeed both sides have at each missing place the factor \(b_v\omega_v(\varpi_v)^{m_v+n_v}q_v^{(m_v+n_v)(1/2-s)}\). This checks all additive conductor signs and powers.

Corollary 6.4 supplies the excluded Eisenstein-pair condition. Lesson 15, Corollary 4.13, therefore gives a cuspidal \(\pi'\) with central character \(\eta\) and all prescribed components outside \(S\).

**Proof: eliminate a wrong exceptional local type.** Divide the complete functional equations of \(\rho\) and \(\pi'\), which agree outside \(S\). For every global \(\omega\),
\[
\prod_{v\in S}\frac{L(s,\rho_v\otimes\omega_v)}{L(s,\pi'_v\otimes\omega_v)}
=\prod_{v\in S}\frac{\epsilon(s,\rho_v\otimes\omega_v,\psi_v)}{\epsilon(s,\pi'_v\otimes\omega_v,\psi_v)}
\prod_{v\in S}\frac{L(1-s,\rho_v^\vee\otimes\omega_v^{-1})}{L(1-s,\widetilde\pi'_v\otimes\omega_v^{-1})}.
\tag{6.17}
\]
Fix \(v_0\in S\) and any \(\omega_{v_0}\). Lemma 6.9 extends it while forcing the other local conductors high enough for Lemmas 6.7–6.8. Since \(\pi'\) and \(\rho\) have the same determinant, their epsilon factors at those other places agree, and all their \(L\)-factors are one. Thus (6.17) becomes the exact local equation
\[
\frac{L(1-s,\widetilde\pi'_{v_0}\otimes\omega_{v_0}^{-1})}
{L(s,\pi'_{v_0}\otimes\omega_{v_0})}
=\frac{\epsilon(s,\rho_{v_0}\otimes\omega_{v_0},\psi_{v_0})}
{\epsilon(s,\pi'_{v_0}\otimes\omega_{v_0},\psi_{v_0})}.
\tag{6.18}
\]
The right side is a nonzero exponential monomial, hence entire with no zeros. The local representation \(\pi'_{v_0}\) is infinite-dimensional and generic. Indeed, for a nonzero vector in the global cusp module, Fourier reconstruction on the compact quotient \(\mathbb A_F/F\) and its zero constant term give a nonzero coefficient at some \(\alpha\in F^\times\). Rational diagonal translation makes that coefficient the \(\psi\)-coefficient. Integration defines its global Whittaker function, nonzero on a suitable right translate. Irreducibility makes this function map injective, and fixing the other tensor factors gives a nonzero local Whittaker map at each place. A one-dimensional local representation has trivial unipotent action and cannot admit that map. This argument uses additive self-duality over either kind of global field. If it were principal, write it \(I(\mu,\nu)\) and take \(\omega_{v_0}=\mu^{-1}\). For ramified \(\nu/\mu\), the left side is \((1-q^{-s})/(1-q^{s-1})\), with a pole at one. For unramified \(\nu/\mu\), put \(B=(\nu/\mu)(\varpi)\); it is
\[
\frac{(1-q^{-s})(1-Bq^{-s})}
{(1-q^{s-1})(1-B^{-1}q^{s-1})}.
\tag{6.19}
\]
It has a pole at one unless \(B=q\). In that case it has a pole at two. Either contradicts (6.18). If \(\pi'_{v_0}=\mathrm{St}_\xi\), take \(\omega_{v_0}=\xi^{-1}\). In this course's normalized Steinberg convention the ratio is
\( (1-q^{-s-1/2})/(1-q^{s-3/2})\),
with a pole at \(3/2\) and nonzero numerator there. This also contradicts (6.18). The finite-place classification of Lesson 7 now makes \(\pi'_{v_0}\) supercuspidal.

**Proof: every missing factor and the original norm twist.** All twists of that supercuspidal have both \(L\)-factors one. Equation (6.18) consequently identifies its epsilon factor with the Artin factor for every local quasicharacter. Its central character is already \(\det\rho_{v_0}\). This is the defining complete local match, and Lesson 9's local converse theorem gives uniqueness. Repeat at every place of \(S\). Thus \(\pi'\) has precisely the required local components at every place, including their phases and bad factors.

Finally restore the removed common real norm power \(|\cdot|^a\) of the global Weil representation by the automorphic twist \(\pi'\otimes|\det|^a\). The local factors shift by the same \(a\); multiplication by \(|\det g|^a\) preserves rational invariance by the product formula, smooth and infinitesimal finiteness, moderate growth and the zero constant term. The result remains cuspidal automorphic. This proves the theorem. \(\square\)

The primary comparison is Jacquet–Langlands, Theorem 12.2 and Lemmas 12.3–12.5, printed pp. 207–212. The finite rank-zero refinement, primitive Gauss cancellation, compact-character interpolation and universal Kirillov calculation above provide the required missing arguments. Proposition 12.6 retains its separate universal hypothesis over all separable extensions; this conditional criterion does not assert that hypothesis.

## 7. Temperedness, proved cases and the remaining bound

The **Ramanujan conjecture for \(\mathrm{GL}_2\)** says that every unitary cuspidal automorphic representation is tempered at every place. The word unitary fixes the norm twist: arithmetic Satake roots of a weight-\(k\) form have size \(p^{(k-1)/2}\), while the corresponding unitary parameters should have size one. At a good prime write
\[
L_p(s,f)=(1-a_pp^{-s}+\varepsilon(p)p^{k-1-2s})^{-1},
\quad
\alpha_p=p^{-(k-1)/2}A_p,\quad
\beta_p=p^{-(k-1)/2}B_p,
\tag{7.1}
\]
where \(A_p+B_p=a_p\), \(A_pB_p=\varepsilon(p)p^{k-1}\). Temperedness is \(|\alpha_p|=|\beta_p|=1\), giving \(|a_p|\le2p^{(k-1)/2}\).

**Proposition 7.1 — the dihedral case.** The unitary induction of a unitary quadratic Hecke character, when cuspidal, is tempered at all places.

**Proof.** At a split finite place its two inducing characters are unitary, so the principal series is tempered by Lesson 7, Theorem 7.2. At a nonsplit finite place with noninvariant character it is a unitary supercuspidal, hence square-integrable modulo its centre and tempered. In the invariant case the two extensions in (1.1) are unitary: choose \(b\) on the unit circle. The corresponding principal series is again induced from unitary characters. At a split real place the two real characters are unitary and yield tempered principal series. At an imaginary quadratic real place a nonzero angular exponent yields a unitary discrete series, and zero angular exponent yields the tempered principal series with opposite real parities. The real classification of Lesson 11 gives these alternatives; its limit-of-discrete-series case has the same tempered conclusion. Thus every local component is tempered. \(\square\)

The general holomorphic theorem is a stated deep input. For weights \(k\ge2\), Deligne's purity theorem gives \(|A_p|=|B_p|=p^{(k-1)/2}\) at every good prime, under every complex embedding. The exact earlier prerequisite is [LG-GAL-12](https://kokunoyumeto.github.io/open-math-courses-public/courses/LG-GAL/deligne-construction-in-higher-weight.html), Section 4, equation (22), based on *La conjecture de Weil. I*, Theorem (8.2). For weight one, Deligne–Serre, Theorem 4.1 and Corollary 4.2, attaches a finite-image complex representation to a normalized cusp eigenform; its good Frobenius eigenvalues are roots of unity, giving \(|a_p|\le2\). Their Theorem 4.6 identifies the conductor and full finite \(L\)-function for a primitive form.

These good-prime conclusions also give temperedness at every bad finite prime. Indeed, by the unitary generic classification in Lesson 7, the only non-tempered possibilities are complementary principal series
\(I(\mu|\cdot|^r,\mu|\cdot|^{-r})\), with \(\mu\) unitary and \(0<r<1/2\). If this occurs at \(p\), choose a finite-order global character whose local unit restriction is \(\mu^{-1}|_{\mathbb Z_p^\times}\). A Dirichlet character of sufficiently large \(p\)-power conductor supplies it, with the required parity at infinity. Twisting removes the ramified unit character, so the \(p\)-component becomes spherical with parameter moduli \(p^r,p^{-r}\). The holomorphic weight is preserved. The good-prime theorem for the resulting primitive holomorphic eigenform contradicts those moduli. Thus no bad component was non-tempered. At infinity the holomorphic discrete series, or weight-one limit, is tempered. This argument also explains why ramification by itself is not a temperedness criterion: a ramified character twist of a complementary series stays non-tempered.

For general Hecke–Maass cusp forms the conjecture remains open. The Kim–Sarnak theorem, as stated by Sarnak, §1, equations (23)–(24), gives the exponent
\(\theta=7/64\). At an unramified prime, the unitary Satake parameters satisfy \(p^{-\theta}\le|\alpha_p|,|\beta_p|\le p^\theta\), hence
\[
|\lambda_p|\le p^{7/64}+p^{-7/64}.
\tag{7.2}
\]
The sharper right side follows from the unitary alternatives: a tempered pair gives at most two, while a complementary pair has moduli \(p^r,p^{-r}\), \(|r|\le\theta\). Its sum bound is at most \(p^\theta+p^{-\theta}\). At the weight-zero real place, a complementary parameter \(r\) has
\[
\lambda=\frac14-r^2\ge\frac14-\left(\frac7{64}\right)^2
 =\frac{975}{4096}.
\tag{7.3}
\]
For real principal-series parameter \(it\), \(\lambda=1/4+t^2\). This is the stated Selberg spectral bound for congruence quotients; the conjectural value is \(\lambda\ge1/4\). The May 2026 introduction of Huang–Zhao, equation (1.1), still records (7.2) as the best general finite-prime bound. None of these statements claim full temperedness for all Maass forms.

## 8. Exercises with complete solutions

### 8.1. Induction at an inert prime — easy

**Exercise 8.1.** Prove (1.2) using induction and explain why an unramified inert prime contributes \(1-cp^{-2s}\), rather than two degree-one factors with the same value \(c\). Include ramified characters.

**Solution 8.1.** The intertwiner \(f(g)\mapsto\omega(g)f(g)\) changes the transformation character from \(\chi\) to \(\chi\omega|_H\); reciprocity identifies the latter restriction with the norm pullback. At an unramified inert prime, inertia lies in \(W_K\), while the base Frobenius exchanges the two cosets. If \(\chi\) is unramified, its Frobenius matrix is \(\bigl(\begin{smallmatrix}0&c\\1&0\end{smallmatrix}\bigr)\), where \(c=\chi(F_K)=\chi(F_{\mathbb Q}^2)\). Its determinant polynomial is \(1-cT^2\), agreeing with the ideal norm \(p^2\). Its eigenvalues are square roots of \(c\) with opposite signs, not both \(c\). If \(\chi\) is ramified, inertia fixes no line on either coset, so the factor is one. At a ramified extension, the inertia action instead joins the cosets into one orbit; it has one surviving line for unramified \(\chi\), and none for ramified \(\chi\). This gives \(1-cT\) or one. Split places give the separate character factors. At infinity the complex character and its real induction share \(\Gamma_{\mathbb C}(s+it+|n|/2)\), with gamma duplication handling \(n=0\). Thus multiplication gives the complete identity, including both kinds of ramification and infinity.

### 8.2. Primary generators and point counting — medium

**Exercise 8.2.** Compute all coefficients of \(f_{32}\) through \(q^{17}\), and compare the prime coefficients with \(E:y^2=x^3-x\). Explain the coefficients at nine and at even indices.

**Solution 8.2.** Apply (4.1) to \(a^2+b^2\le17\). The primary pairs contributing are

| Norm | Primary generators | Sum |
|---:|---|---:|
| 1 | \(1\) | 1 |
| 5 | \(-1+2i,-1-2i\) | −2 |
| 9 | \(-3\) | −3 |
| 13 | \(3+2i,3-2i\) | 6 |
| 17 | \(1+4i,1-4i\) | 2 |

These exhaust the possibilities: \(b\) is even with \(|b|\le4\), \(a\) is odd, and the congruence selects the displayed signs. Norms \(2,3,4,6,7,8,10,11,12,14,15,16\) have no primary generator of those norms. The complete expansion is therefore \(q-2q^5-3q^9+6q^{13}+2q^{17}+O(q^{18})\). The norm of an ideal prime to \(\varpi\) is odd, so every even coefficient is zero. The inert prime three has one ideal of norm nine, namely \((3)\), whose primary generator is \(-3\). This gives the negative coefficient independently of the Hecke recurrence.

For the curve, the quadratic character sums in (4.4) at \(3,5,7,13,17\) are respectively \(0,2,0,-6,-2\), giving point counts \(4,8,8,8,16\). For example at five the values of \(x^3-x\), for \(x=0,1,2,3,4\), are \(0,0,1,4,0\); the sum is two. These give prime traces \(0,-2,0,6,2\), exactly the theta values. The discriminant is 64, so the curve has good reduction at every odd prime; its additive factor at two is one. The Euler factor at three gives \(a_9=a_3^2-3=-3\), and the missing two-factor gives every even coefficient zero. Finally Section 4 proves equality of the modular forms using coefficients through eight and (4.5), so the finite computations extend to an all-coefficient identification through the stated modularity input.

### 8.3. Which splitting gives which trace? — medium

**Exercise 8.3.** For \(F=\eta(z)\eta(23z)\), determine \(a_p\) from the splitting in the Hilbert class field of \(\mathbb Q(\sqrt{-23})\). Check the primes two, five and 59, and handle 23 separately.

**Solution 8.3.** In the coset model (1.1), an element outside \(C_3\) has trace zero. It is a transposition; the corresponding rational prime is inert in \(K\) and has three degree-two primes in the Galois field \(H\). For the identity, the two diagonal values are both one, giving trace two and six degree-one primes. For a nonidentity element of \(C_3\), the values are \(\zeta_3,\zeta_3^{-1}\), giving trace \(-1\); there are two degree-three primes in \(H\). These are the three unramified classes, and (5.4)–(5.6) identify their traces with \(a_p(F)\).

Modulo two, \(X^3-X-1\) has no root and is irreducible, so the class is a three-cycle and \(a_2=-1\). Modulo five its root is two and division leaves \(X^2+2X+3\), of discriminant two, a nonsquare; the class is a transposition and \(a_5=0\). Modulo 59 its three roots are \(4,13,42\); multiplication of their three linear factors recovers the cubic, so \(a_{59}=2\). At 23 the prime of \(K\) has square equal to \((23)\), hence class of order dividing two. The class group has order three, so its class is trivial and \(\xi\) takes value one. The local Hecke factor is \((1-23^{-s})^{-1}\), giving \(a_{23}=1\). Applying the unramified three-row table at 23 would be incorrect.

### 8.4. Derive modularity from Hecke's analytic theory — hard

**Exercise 8.4.** Starting with a primitive ideal character satisfying (3.1), \(m\ge1\), prove that its theta series is a normalized newform of weight \(m+1\) and exact level \(|d_K|N\mathfrak f\). You may use Tate's Hecke functional equation, local quadratic correspondence and the global converse theorem. Verify the bounded-strip hypothesis rather than assuming it.

**Solution 8.4.** First divide the ideal values by \(N\mathfrak a^{m/2}\). The resulting absolute-value character is one on principal ideals and on the finite ideal class group, hence one everywhere; this produces the unitary \(u\) of (3.2). Triviality on diagonal elements forces \(u_\infty=(z/|z|)^{-m}\). Thus every base norm-pullback twist has this same nonzero angular exponent and is nontrivial on \(C_K^1\). Its dual has exponent \(m\) and the same nontriviality. Both Euler products converge absolutely for \(\operatorname{Re}s>1\).

Use the Gaussian-polynomial archimedean test and finite primitive-character tests of NT-ADL-10 so that the Tate integral is exactly the completed function. Average the nonzero theta sum against the character on the compact norm-one group. Uniform lattice estimates bound each log-norm derivative by every negative power at infinity. Poisson summation has two zero correction terms; compact character averaging kills both, giving (2.3). All derivatives then decay by every positive power at zero. With \(t=e^x\), the Mellin transform is (2.4). On a strip, all derivatives of its nonoscillating integrand are uniformly integrable; repeated integration by parts gives \(O((1+|\operatorname{Im}s|)^{-r})\) for every \(r\). This proves both entire continuation and the required strip bounds. The derivations and justifications for differentiation are those in the full proof of Lemma 2.2.

Theorem 1.1 identifies these complete twisted functions with the functions of the proposed local quadratic tensor. Its central character is (1.5), trivial on \(\mathbb Q^\times\); local genericity and the good unitary parameters satisfy the remaining converse hypotheses. The local epsilon comparison (2.5) has global induction constant one, as checked using the trivial inducing character and the three Tate equations. Thus the functional equation is also the exact one demanded by Lesson 15, Theorem 4.1. It yields a cuspidal \(\Pi\).

The real induction has infinity type \(D_{m+1}\). Equality of the primitive Hecke epsilon monomial \(W(|d_K|N\mathfrak f)^{1/2-s}\) with \(W_\Pi N_\Pi^{1/2-s}\) gives \(N_\Pi=|d_K|N\mathfrak f\). The newvector line yields a normalized holomorphic primitive form \(f_\Pi\) of that weight and exact level, with the central-character nebentypus of Theorem 3.1. Its finite Dirichlet series, shifted by \(m/2\), is precisely (3.6). The bound \(|b_n|\le d(n)n^{m/2}\) gives both absolute initial convergence and normal convergence of the theta expansion. Uniqueness of absolutely convergent Dirichlet-series coefficients, proved in Theorem 3.1, identifies every Fourier coefficient with the ideal sum. Hence \(f_\Pi=\theta_\Psi\). This establishes transformations at the whole congruence group and cuspidality at every cusp through the proved converse deduction and classical dictionary, rather than inferring them from the untwisted Fricke equation alone.

## 9. What this lesson does not prove

The induction identity, the arbitrary-quasicharacter norm/transfer/determinant identities, the strip estimate, the full quadratic induction theorem over every global field and for every quasicharacter, the full primitive CM theta theorem for \(k\ge2\), both explicit examples, the finite-index valence deduction and all four solutions are proved above. The proof of the theta theorem is relative to the following precisely stated prerequisites; it does not assume the theta theorem itself.

- The ideal/idelic Hecke-character dictionary is NT-ADL-06, Theorem 6.3. The compact norm-one group, Poisson identity, uniform theta estimate and Tate continuation are NT-ADL-09, the theta lemma, Lemma 9.3 and Theorem 9.2. Exact primitive tests, gamma factors and the conductor equation are NT-ADL-10, equations (2)–(3) and Theorem 10.1.
- Reciprocity, existence and norm compatibility are now the written proofs in [The global reciprocity law](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-CFT/the-global-reciprocity-law.html), Proposition 16.1 and Theorem 16.4, and [Global existence and the idèlic class field correspondence](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-CFT/global-existence-and-the-idelic-class-field-correspondence.html), Theorems 17.1–17.2. They prove the exact finite abelian norm quotient, norm functoriality with arithmetic Frobenius, realization of every open finite-index subgroup, and local ramification/splitting criteria, including function fields. The conductor-one case gives the Hilbert class field used above. Original locators are Milne, *Class Field Theory*, V.3.3, V.3.5–3.6 and V.5.2–5.5. The number-field relative Weil construction, topological abelianization, transfer, tower maps and local decomposition compatibility are now the written proof in [Brauer groups of local and global fields](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-CFT/brauer-groups-of-local-and-global-fields.html), Theorem 24.6 and Section 7, equations (29)–(39). Proposition 1.2 derives both idelic directions, the norm-factor criterion and the determinant/twist identities for arbitrary continuous Hecke quasicharacters. The primary-source convention is Jacquet–Langlands, Section 12 opening; the function-field continuous abelianization is NT-CFT-17, Section 8.
- Local quadratic construction and matching twisted factors are proved in Lesson 10, Theorems 6.3–6.5, including the norm-factor case and epsilon induction constant in every residue characteristic. Original locators are Jacquet–Langlands, Theorem 4.7 and §12 before Proposition 12.1. Real and complex factors and classification are proved in Lesson 11, Sections 3–6 and Theorems 3.2, 5.1 and 6.1. The global converse is proved in Lesson 15, Theorem 4.1 and Lemmas 4.2–4.4; the original theorem is Jacquet–Langlands, Theorem 11.3. The general-global-field Proposition 12.1 is now proved in Theorem 2.1 and Section 2.1, using the all-field converse of Lesson 15, Theorem 4.5. Proposition 1.3 and Lemma 2.4 supply the function-field relative group, exact Poisson covolume, primitive local Fourier constants and full Hecke equation/strip estimate. The analytic Artin Theorem 12.2 is now proved in Theorem 6.10, with the exact all-twist hypotheses and Artin–Hecke functional-equation inputs; historical Proposition 12.6 retains its separate universal hypothesis. Corollary 2.3 proves the rational induction assertion for every quasicharacter by an automorphic determinant twist.
- The conditional analytic criterion is proved in Lemmas 6.1–6.9 and Theorem 6.10. Lesson 15, Theorem 4.10, Lemmas 4.11–4.12 and Corollary 4.13, proves its exceptional-set converse and full cuspidal constituent selection. The written [Brauer induction](https://kokunoyumeto.github.io/open-math-courses-public/courses/RT-FIN/brauers-induction-theorem.html), Theorems 1.2 and 5.1, supplies nilpotent monomiality and ordinary integral induction; Lemma 6.5 proves the needed rank-zero refinement here. The written [local conductor lesson](https://kokunoyumeto.github.io/open-math-courses-public/courses/LG-GAL/conductors-of-weil-group-representations.html), Sections 1–4, records the ramification, conductor integrality and character-conductor inputs and proves their smooth induction/single-break consequences. The written [local epsilon lesson](https://kokunoyumeto.github.io/open-math-courses-public/courses/LG-GAL/local-l-factors-and-epsilon-factors.html), Sections 3–4, states Langlands–Deligne existence, including independence of Brauer choices, and derives the exponent, induction and determinant rules. Its reciprocity is geometric; Section 6.2 binds these formal rules to this course’s arithmetic idèlic Tate normalization and derives the actual phases. The local existence theorem is Deligne 1973, Theorem 4.1; conductor integrality (Artin) and upper ramification are taken as known; the abelian case of the Hasse–Arf theorem is proved in [Abelian ramification, conductors and Hasse–Arf](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-CFT/abelian-ramification-conductors-and-hasse-arf.html). These are stated foundational inputs. The Artin–Hecke global functional equations are the stated inputs to the criterion, not a proof of its universal all-twist analytic premise. Lemmas 6.6–6.8 prove the required high-character stability directly; the provider’s stated Deligne–Henniart theorem is not used as a proved input.

- Local conductors, the newvector line and primitive classical decomposition are Lessons 8–9, especially Lesson 8, Theorem 5.1. The full finite-function/classical shift and global conductor normalization are Lesson 14, Section 6. The holomorphic real type is Lesson 11, Theorem 7.1. The classical Mellin input is LG-MF-12, Theorem 4.1; its specialized Weil theorem is not used as a general-character theorem.
- The lattice-theta theorem, including all-cusp holomorphy, is LG-MF-14, Theorem 6.1, with its exact Voight locators 40.4.4–40.4.5. Minkowski's ideal-class bound is Milne, *Algebraic Number Theory*, Theorem 4.3. Ideal factorization and polynomial factorization are Theorems 3.7 and 3.41; the discriminant criterion is Theorem 3.35. The local inertia facts are Theorem 7.58 and Corollary 7.59, with global decomposition groups and their tower compatibility in Propositions 8.10–8.13. The computations in Section 5 determine the specific class group, ideal norm forms and unramified cubic extension.
- Eta transformation and cusp orders are Allen–Anderson–Hamakiotes–Oltsik–Swisher, Theorems 1.2 and 1.4, citing Ono, Theorems 1.64–1.65. The level-one valence bound is LG-MF-05, Theorem 1.1; congruence index and the two prime-level cusps are LG-MF-03, Section 3, and Lesson 19, Theorem 4.2. Elliptic modularity is Allen–Anderson–Hamakiotes–Oltsik–Swisher, Theorem 1.1; the conductor and additive reduction of the specified curve are the LMFDB 32.a3 record. We prove its finite coefficient comparisons and the valence identification, not elliptic modularity or the general Tate algorithm.
- Deligne's purity input is LG-GAL-12, Section 4, equation (22), based on Deligne, Theorem (8.2). The weight-one representation and primitive factor theorem are Deligne–Serre, Theorems 4.1 and 4.6 and Corollary 4.2. The finite unitary and tempered classifications used to extend good-prime temperedness are proved in Lesson 7, Theorems 7.1–7.2. The Maass bounds are Sarnak, §1, equations (23)–(25); their proofs and the general Ramanujan conjecture are outside this lesson. Getz–Hahn, §13.4, states the Artin automorphy results mentioned in Section 6. The later Langlands–Tunnell and Deligne–Serre lessons develop those stated results further.

## References

- H. Jacquet and R. P. Langlands, *Automorphic Forms on GL(2)*, LNM 114, 1970, §§1, 4, 11–12; Proposition 12.1, Theorem 12.2 and Proposition 12.6. [IAS author collection](https://publications.ias.edu/rpl/section/22).
- J. R. Getz and H. Hahn, [*An Introduction to Automorphic Representations, with a View toward Trace Formulae*](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), draft of 22 April 2022, §§12.3–12.4 and 13.4.
- P. Sarnak, “Notes on the generalized Ramanujan conjectures,” in *Harmonic Analysis, the Trace Formula, and Shimura Varieties*, Clay Mathematics Proceedings 4, 2005, §1 equations (23)–(25). [Clay volume](https://www.claymath.org/wp-content/uploads/2022/03/cmip04c.pdf).
- P. Deligne and J.-P. Serre, “Formes modulaires de poids 1,” *Annales scientifiques de l'École Normale Supérieure* **7** (1974), 507–530, Theorems 4.1 and 4.6 and Corollary 4.2. [Journal article](https://www.numdam.org/articles/10.24033/asens.1277/).
- P. Deligne, *La conjecture de Weil. I*, *Publications Mathématiques de l'IHÉS* **43** (1974), 273–307, Theorem (8.2), used through the exact LG-GAL-12 prerequisite.
- M. Allen, N. Anderson, A. Hamakiotes, B. Oltsik and H. Swisher, “Eta-quotients of prime or semiprime level and elliptic curves,” *Involve* **13** (2020), 879–901, Theorems 1.1–1.4. [Primary article](https://msp.org/involve/2020/13-5/involve-v13-n5-p12-s.pdf).
- J. S. Milne, *Class Field Theory*, Chapter V, §§3–5. [Author's notes](https://www.jmilne.org/math/CourseNotes/CFT.pdf). Also *Algebraic Number Theory*, Theorem 4.3 and the ideal/ramification theory in Chapters 3 and 8. [Author's notes](https://www.jmilne.org/math/CourseNotes/ANT.pdf).
- E. Frenkel, *Lectures on the Langlands program and conformal field theory*, §1, for the modular-form, elliptic-curve and representation viewpoint. [Author preprint](https://arxiv.org/abs/hep-th/0512172).
- J. R. Getz and H. Hahn, [*An Introduction to Automorphic Representations*](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), draft of 22 April 2022, §§6.7–6.8, for the passage from classical forms to automorphic representations and the unitary normalization of the classical example.
- T. Huang and S. Zhao, *On Ramanujan Primes for Hecke-Maass cusp forms*, 2026, introduction, equation (1.1), for the contemporary status comparison of the finite-prime bound. [Primary preprint](https://arxiv.org/html/2605.09807v1).
