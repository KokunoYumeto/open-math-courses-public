# Sextic reciprocity and Kummer characters

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The coefficient sums of Lesson 5 contain sextic residue symbols \(\chi_{\mathfrak A}(m)\), whose modulus \(\mathfrak A\) varies with the summation and whose argument \(m\) varies with the row. Two facts make such sums tractable. First, for allowed generators in the sense of [*S-integers and sixth-power classes*](s-integers-and-sixth-power-classes.md) the sextic reciprocity law holds exactly, with no supplementary factor; this lets the symbol be read in either direction. Second, for a fixed argument \(u\) the symbol \(\mathfrak a\mapsto\chi_{\mathfrak a}(u)\) is a Hecke character of finite order, a Kummer character, whose conductor is bounded by the norm of the radical of \(u\). This lesson proves both, and parametrizes the frequencies \(h\in R\setminus\{0\}\) that will appear after Poisson summation by a Kummer character and a sixth power.

**Prerequisites.** [*S-integers and sixth-power classes*](s-integers-and-sixth-power-classes.md), Lemma 2.1, (3.1)–(3.3), Lemma 3.1 and Lemma 4.1; [*Power residue symbols and reciprocity laws*](course:NT-CFT/power-residue-symbols-and-reciprocity-laws), Propositions 23.1 and 23.2 and Theorem 23.3; [*Hilbert's theorem 90 and Kummer theory*](course:NT-CFT/hilberts-theorem-90-and-kummer-theory), Theorem 3.3; [*The global reciprocity law*](course:NT-CFT/the-global-reciprocity-law), Theorem 16.4; [*Quasi-characters and Hecke characters*](course:NT-ADL/NT-ADL-06), Propositions 6.1 and 6.4; [*Hensel's lemma, squares and roots of unity in p-adic fields*](course:NT-LOC/NT-LOC-03), Corollary 1.2; [*The multiplicative group of a local field*](course:NT-LOC/NT-LOC-11), Corollary 4.2; [*Counting ideals of bounded norm*](course:NT-ANT/counting-ideals-of-bounded-norm), Theorem 15.3.

## 1. Sextic residue symbols

Keep the field \(F\supseteq\mu_{12}\), the set \(S\), the ring \(R=\mathcal O_S\) and the subgroup \(B\) of Lesson 2. Let \(\mathfrak p\) be an exterior prime, that is, a prime ideal of \(R\), with norm \(q_{\mathfrak p}\). Since \(\mathfrak p\nmid6\), reduction modulo \(\mathfrak p\) is injective on \(\mu_{12}\), so \(12\mid q_{\mathfrak p}-1\). The **sextic residue character** is
\[
\begin{gathered}
\begin{aligned}
\chi_{\mathfrak p}(x)&\equiv x^{(q_{\mathfrak p}-1)/6}\\
&\quad \pmod{\mathfrak p}\quad(x\in R\setminus\mathfrak p),
\end{aligned}\\
\chi_{\mathfrak p}(x)=0\quad(x\in\mathfrak p),\quad(1.1)
\end{gathered}
\]
with values in \(\mu_6\subset F\); it is the power residue symbol \((x/\mathfrak p)_6\) of Proposition 23.1 of [*Power residue symbols and reciprocity laws*](course:NT-CFT/power-residue-symbols-and-reciprocity-laws). For every integer \(j\) the notation \(\chi_{\mathfrak p}(x)^j\) means the usual power on units and \(0\) on nonunits, also when \(6\mid j\); this **unit mask** is used throughout the course. For an exterior ideal \(\mathfrak a=\prod_{\mathfrak p}\mathfrak p^{k_{\mathfrak p}}\) put
\[
\begin{gathered}
\chi_{\mathfrak a}(x)=\prod_{\mathfrak p\mid\mathfrak a}\chi_{\mathfrak p}(x)^{k_{\mathfrak p}},\\
\chi_R(x)=1,\quad(1.2)
\end{gathered}
\]
with the same convention for powers of \(\chi_{\mathfrak a}\). Since \(12\mid q_{\mathfrak p}-1\), the exponent \((q_{\mathfrak p}-1)/6\) is even and
\[
\chi_{\mathfrak p}(-1)=1 .
\tag{1.3}
\]

## 2. Reciprocity without supplementary factors

**Proposition 2.1** ([OpenAI-029, (3.3)–(3.5)]). Let \(\mathfrak p\ne\mathfrak p'\) be exterior primes with allowed generators \(p,p'\). Then
\[
\chi_{\mathfrak p}(p')=\chi_{\mathfrak p'}(p).
\tag{2.1}
\]
Let \(\mathfrak a\) be an exterior ideal with allowed generator \(a\), let \(m\in R\setminus\{0\}\) with \(mR=\mathfrak b\), and write \(m=\epsilon b\) with \(b\) an allowed generator of \(\mathfrak b\) and \(\epsilon\in U_S\). Then
\[
\chi_{\mathfrak a}(m)=\chi_{\mathfrak a}(\epsilon)\,\chi_{\mathfrak b}(a),
\tag{2.2}
\]
both sides being zero when \(\mathfrak a\) and \(\mathfrak b\) have a common prime, and for \(\epsilon\in U_S\)
\[
\chi_{\mathfrak a}(\epsilon)=H_S(\epsilon,a)^{-1}.
\tag{2.3}
\]
In particular \(\chi_{\mathfrak a}(\epsilon)\) depends on \(\mathfrak a\) only through the class \([a]\in B\).

*Proof.* Apply Hilbert's product formula (Theorem 23.3 of [*Power residue symbols and reciprocity laws*](course:NT-CFT/power-residue-symbols-and-reciprocity-laws)) to the symbols \((p,p')_{6,v}\) of (3.1) of Lesson 2. At an exterior prime other than \(\mathfrak p,\mathfrak p'\) both arguments are units, and the symbol is \(1\). At \(\mathfrak p\), the tame formula (3.2) of Lesson 2 with \(p'\) a unit and \(p\) a uniformizer gives \((p',p)_{6,\mathfrak p}=\chi_{\mathfrak p}(p')\), hence \((p,p')_{6,\mathfrak p}=\chi_{\mathfrak p}(p')^{-1}\) by Lemma 3.1 of Lesson 2. At \(\mathfrak p'\) the same formula gives \((p,p')_{6,\mathfrak p'}=\chi_{\mathfrak p'}(p)\). The product of the symbols at \(S\) is \(H_S(p,p')=1\), because \([p],[p']\in B\) and \(B\) is isotropic. The product formula therefore reads \(\chi_{\mathfrak p}(p')^{-1}\chi_{\mathfrak p'}(p)=1\), which is (2.1).

For (2.2), allowed generators are unique up to \(U_S^6\), and the product of allowed generators of the prime factors of \(\mathfrak b\) is an allowed generator of \(\mathfrak b\); since \(\chi_{\mathfrak p}\) is trivial on sixth powers of units, we may take \(b\) to be that product, and likewise \(a\). Multiplicativity of \(\chi_{\mathfrak a}\) in its argument and of \(\chi_{\mathfrak a}\) in \(\mathfrak a\) reduce \(\chi_{\mathfrak a}(b)=\chi_{\mathfrak b}(a)\) to (2.1) for pairs of distinct primes; if a prime divides both ideals, both sides vanish by the unit mask. Finally \(\chi_{\mathfrak a}(m)=\chi_{\mathfrak a}(\epsilon)\chi_{\mathfrak a}(b)\).

For (2.3), apply the product formula to \((\epsilon,a)_{6,v}\). At an exterior prime \(\mathfrak p\) with \(v_{\mathfrak p}(a)=k\), write \(a=p^ku\) with a local unit \(u\); then \((\epsilon,a)_{6,\mathfrak p}=(\epsilon,p)_{6,\mathfrak p}^k(\epsilon,u)_{6,\mathfrak p}=\chi_{\mathfrak p}(\epsilon)^k\) by (3.2) of Lesson 2. The product over exterior primes is \(\chi_{\mathfrak a}(\epsilon)\), the product over \(S\) is \(H_S(\epsilon,a)\), and the total is \(1\). \(\square\)

Without the normalization of generators, (2.1) acquires the factor \(\chi_{\mathfrak p}(\epsilon)\) of (2.3) for each unit adjustment; this is the supplementary factor that the choice of \(B\) removes (Exercise 5.2).

## 3. Kummer characters

**Lemma 3.1** (Kummer and class characters [OpenAI-029, Lemma 3.3]). 

1. For \(u\in R\setminus\{0\}\) there is a finite-order Hecke character \(\kappa_u\) of \(F\) such that \(\kappa_u(\mathfrak p)=\chi_{\mathfrak p}(u)\) for every exterior prime \(\mathfrak p\nmid u\). Its local component at a place \(v\) is \(y\mapsto(u,y)_{6,v}\).
2. Let \(\mathfrak f_u\) be the conductor of \(\kappa_u\). Then
\[
\begin{aligned}
\operatorname N\mathfrak f_u&\le C_{F,S}\operatorname N\operatorname{rad}(uR)\\
&\le C_{F,S}\,q_u ,\quad(3.1)
\end{aligned}
\]
and the same holds, with another constant, for the conductor of \(\eta\kappa_u\) and of \(\eta\overline{\kappa_u}\).
3. \(\kappa_u=\kappa_v\) if and only if \(u/v\in F^{\times6}\).
4. Every character \(\theta_B\) of the finite group \(B\) extends to a finite-order Hecke character \(\theta\), unramified outside \(S\), with \(\theta(\mathfrak a)=\theta_B([a])\) for every exterior ideal \(\mathfrak a\) with allowed generator \(a\).

The **Kummer character** \(\chi_\bullet(u)\) is the ideal function \(\mathfrak a\mapsto\chi_{\mathfrak a}(u)\); it equals \(\kappa_u\) on exterior ideals prime to \(u\) and vanishes on those meeting \(u\).

*Proof.* *1.* Let \(L=F(u^{1/6})\). Since \(\mu_6\subset F\), Kummer theory (Theorem 3.3 of [*Hilbert's theorem 90 and Kummer theory*](course:NT-CFT/hilberts-theorem-90-and-kummer-theory)) makes \(L/F\) cyclic and gives the character \(\kappa_u(\sigma)=\sigma(u^{1/6})/u^{1/6}\) of its Galois group; its kernel, as a function of \(u\), is \(F^{\times6}\). Composing with the global reciprocity map (Theorem 16.4 of [*The global reciprocity law*](course:NT-CFT/the-global-reciprocity-law)), whose local components are the maps \(\operatorname{Art}_v\), gives a character of the idèle class group of finite order, whose component at \(v\) is \(y\mapsto\operatorname{Art}_v(y)(u^{1/6})/u^{1/6}=(u,y)_{6,v}\). At an exterior prime \(\mathfrak p\nmid u\), the extension is unramified and the image of a uniformizer \(\varpi\) is the Frobenius; by (3.2) of Lesson 2, \((u,\varpi)_{6,\mathfrak p}\equiv u^{(q_{\mathfrak p}-1)/6}\), so \(\kappa_u(\mathfrak p)=\chi_{\mathfrak p}(u)\) (equivalently, Proposition 23.2 of [*Power residue symbols and reciprocity laws*](course:NT-CFT/power-residue-symbols-and-reciprocity-laws)).

*2.* At an exterior prime \(\mathfrak p\), every principal unit is a sixth power: \(X^6-y\) with \(y\equiv1\pmod{\mathfrak p}\) has the simple residue root \(1\), because \(6\) is a unit, and Corollary 1.2 of [*Hensel's lemma, squares and roots of unity in p-adic fields*](course:NT-LOC/NT-LOC-03) lifts it. So the local component \(y\mapsto(u,y)_{6,\mathfrak p}\) is trivial on \(1+\mathfrak p\), and the conductor exponent is at most \(1\) (Proposition 6.1 of [*Quasi-characters and Hecke characters*](course:NT-ADL/NT-ADL-06)). If \(u\) is a unit at \(\mathfrak p\), the tame formula shows that the symbol of two units is \(1\), so the component is unramified. At a place \(v\in S\), the component depends only on the class of \(u\) in the finite group \(F_v^\times/F_v^{\times6}\); the finitely many possible local characters have a largest conductor. Hence \(\operatorname N\mathfrak f_u\) is at most a constant times the product of \(q_{\mathfrak p}\) over exterior primes dividing \(u\), which is \(\operatorname N\operatorname{rad}(uR)\le\operatorname N(uR)=q_u\). Multiplying by \(\eta\), whose conductor is supported in \(S\), changes only the components at \(S\), again among finitely many possibilities.

*3.* The reciprocity map of Theorem 16.4 maps the idèle class group onto \(\operatorname{Gal}(L/F)\) for every finite abelian \(L/F\), so two Hecke characters obtained by composing Galois characters with it are equal exactly when the Galois characters are equal. Apply this to the compositum of \(F(u^{1/6})\) and \(F(v^{1/6})\): \(\kappa_u=\kappa_v\) if and only if \(\sigma(u^{1/6})/u^{1/6}=\sigma(v^{1/6})/v^{1/6}\) for every \(\sigma\), that is, \((u/v)^{1/6}\) is fixed by every \(\sigma\), that is, \(u/v\in F^{\times6}\).

*4.* Extend \(\theta_B\) to \(\mathcal V=E\oplus B\) by \(\theta_S(eb)=\theta_B(b)\), and view it as a character of \(F_S^\times\) trivial on \(F_S^{\times6}\). It is continuous: \(F_v^{\times6}\) is open at each finite place (Corollary 4.2 of [*The multiplicative group of a local field*](course:NT-LOC/NT-LOC-11)) and equal to \(F_v^\times\) at each complex place. It is trivial on \(U_S\), whose image lies in \(E\). For an exterior ideal \(\mathfrak a=aR\) with \(a\) allowed, put \(\theta(\mathfrak a)=\theta_S(a)\); this is independent of the allowed generator and multiplicative. Define an idèle character by \(\theta_S^{-1}\) on \(F_S^\times\) and, at each exterior prime, the unramified character sending a uniformizer to \(\theta(\mathfrak p)\). For \(x\in F^\times\), write \(x=\epsilon a\) with \(a\) an allowed generator of \(xR\) and \(\epsilon\in U_S\); the value of the idèle character at \(x\) is \(\theta(xR)\theta_S(x)^{-1}=\theta_S(a)\theta_S(\epsilon a)^{-1}=1\). So it is a Hecke character of finite order, unramified outside \(S\), with the stated values. \(\square\)

### The frequency decomposition

Choose a complete set \(\mathcal U\) of representatives, modulo \(U_S^6\), of the nonzero \(S\)-integers whose valuations at all exterior primes lie in \(\{0,1,\dots,5\}\), with \(1\in\mathcal U\). For \(u\in\mathcal U\) put \(q_u=|u|_S\).

**Lemma 3.2** (frequencies [OpenAI-029, (3.7)]). With allowed generators \(r\), the map
\[
\begin{gathered}
(u,\mathfrak r)\longmapsto[ur^6]\\
\begin{aligned}
&\text{from}\ \mathcal U\times\{\text{exterior ideals}\}\\
&\quad \ \text{to}\ (R\setminus\{0\})/U_S^6
\end{aligned}\quad(3.2)
\end{gathered}
\]
is a bijection. Among \(u\in\mathcal U\), only \(u=1\) has \(\kappa_u\) principal, and distinct \(u\) give distinct characters \(\kappa_u\), also after multiplication by \(\eta\) or by \(\overline\eta\).

*Proof.* Given \(h\ne0\), write \(v_{\mathfrak p}(h)=6m_{\mathfrak p}+j_{\mathfrak p}\) with \(0\le j_{\mathfrak p}\le5\) at each exterior prime, and put \(\mathfrak r=\prod\mathfrak p^{m_{\mathfrak p}}\) with allowed generator \(r\). Then \(u_0=h/r^6\) is an \(S\)-integer with exterior valuations \(j_{\mathfrak p}\); replacing it by its representative in \(\mathcal U\) changes \(u_0r^6\) only by \(U_S^6\). Conversely the exterior valuations of a class \([ur^6]\) determine \(\mathfrak r\) and the valuations of \(u\), and then \(u\) modulo \(U_S^6\). Changing \(r\) within its allowed class does not change the image. So (3.2) is bijective.

If \(\kappa_u\) is principal, Lemma 3.1(3) gives \(u=t^6\) with \(t\in F\). The exterior valuations of \(u\) are divisible by \(6\) and lie in \([0,5]\), so they vanish, and so do those of \(t\): \(t\in U_S\), \(u\in U_S^6\), and \(u=1\). If \(\kappa_u=\kappa_{u'}\), then \(u/u'\) is a sixth power; the differences of exterior valuations are divisible by \(6\) and lie in \([-5,5]\), hence vanish; so \(u/u'\) is the sixth power of an element with vanishing exterior valuations, an \(S\)-unit, and \(u/u'\in U_S^6\), so \(u=u'\). A common factor \(\eta\) cancels from an equality of twisted characters. \(\square\)

## 4. A count of frequencies

**Lemma 4.1** ([OpenAI-029, (8.1)]). For \(U\ge1\),
\[
\begin{gathered}
\#\{u\in\mathcal U:U\le q_u<2U\}\ll U,\\
\operatorname N\mathfrak f_{\eta\overline{\kappa_u}}\ll U\quad(U\le q_u<2U).
\end{gathered}
\]

*Proof.* The ideal \(uR\) determines \(u\) up to the finite group \(U_S/U_S^6\), and the number of exterior ideals of norm less than \(2U\) is \(O(U)\): exterior ideals correspond to integral ideals of \(\mathcal O_F\) of the same norm, and (16) of Theorem 15.3 of [*Counting ideals of bounded norm*](course:NT-ANT/counting-ideals-of-bounded-norm) bounds their number. The conductor bound is (3.1). \(\square\)

## 5. Exercises

**5.1.** Show that for \(\zeta\in\mu_6\) and an exterior prime \(\mathfrak p\), \(\chi_{\mathfrak p}(\zeta)=\zeta^{(q_{\mathfrak p}-1)/6}\), and deduce \(\chi_{\mathfrak p}(\zeta_{12}^2)=1\) whenever \(72\mid q_{\mathfrak p}-1\).

**5.2.** Let \(p\) be an allowed generator of \(\mathfrak p\) and \(\epsilon\in U_S\). Show that \(\chi_{\mathfrak p'}(\epsilon p)=\chi_{\mathfrak p}(p')\,H_S(\epsilon,p')^{-1}\) for every exterior prime \(\mathfrak p'\ne\mathfrak p\) with allowed generator \(p'\).

**5.3.** Show that \(\kappa_{uv}=\kappa_u\kappa_v\), and that \(\kappa_{\epsilon^6}\) is principal for \(\epsilon\in U_S\).

**5.4.** Show that if \(u\in R\setminus\{0\}\) is squarefree as an exterior ideal (no exterior prime divides it twice), then the conductor of \(\kappa_u\) is divisible by every exterior prime dividing \(u\).

## 6. Solutions

**5.1.** \(\zeta\) is a unit at \(\mathfrak p\) and \(\chi_{\mathfrak p}(\zeta)\equiv\zeta^{(q_{\mathfrak p}-1)/6}\pmod{\mathfrak p}\); both sides are sixth roots of unity, and reduction is injective on \(\mu_6\). If \(72\mid q_{\mathfrak p}-1\), then \(12\mid(q_{\mathfrak p}-1)/6\), and \(\zeta_{12}^2\) has order \(6\), so the power is \(1\).

**5.2.** \(\chi_{\mathfrak p'}(\epsilon p)=\chi_{\mathfrak p'}(\epsilon)\chi_{\mathfrak p'}(p)\). By (2.1), \(\chi_{\mathfrak p'}(p)=\chi_{\mathfrak p}(p')\), and by (2.3) with \(\mathfrak a=\mathfrak p'\), \(\chi_{\mathfrak p'}(\epsilon)=H_S(\epsilon,p')^{-1}\).

**5.3.** \((uv,y)_{6,v}=(u,y)_{6,v}(v,y)_{6,v}\) at every place, by multiplicativity of the symbol in its first argument; and \(\epsilon^6\) is a sixth power, so \(\kappa_{\epsilon^6}\) is trivial by Lemma 3.1(3).

**5.4.** If \(v_{\mathfrak p}(u)=1\), then \(u\) is a uniformizer at \(\mathfrak p\) and \(y\mapsto(u,y)_{6,\mathfrak p}\) is nontrivial on units: by the tame formula and Lemma 3.1 of Lesson 2, \((u,y)_{6,\mathfrak p}=(y,u)_{6,\mathfrak p}^{-1}\equiv y^{-(q_{\mathfrak p}-1)/6}\) for a unit \(y\), which is not identically \(1\) because the residue field group is cyclic of order divisible by \(6\). So \(\mathfrak p\) divides the conductor.

## Sources

- [OpenAI-029] OpenAI, *Primitive roots for every admissible integer base*, OpenAI Math Release preprint, 4 October 2026, Section 3. https://github.com/openai/math/tree/main/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026
