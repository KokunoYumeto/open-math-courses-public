# Gauss sums and the correction characters

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The coefficients of the cubic theta series of Lesson 6 are normalized quadratic-twisted cubic Gauss sums \(\gamma_2(\mathfrak c)\). Their phases are not values of a multiplicative function of \(\mathfrak c\), but at a prime they are tied to Hecke characters: the cube \(\gamma_2(\mathfrak p)^3\) is minus the value of a unitary Hecke character \(\Lambda\) of infinite order, and the product \(\gamma_1(\mathfrak p)\gamma_2(\mathfrak p)\) is minus \(\Lambda(\mathfrak p)\) times the value of a finite-order character \(G\). This lesson proves these identities. The ingredients are Gauss and Jacobi sums over finite fields, the lifting theorem of Davenport and Hasse (proved here), the normalization of cubic Jacobi sums over the Eisenstein integers, and Weil's index of quadratic characters, which controls the signs of quadratic Gauss sums. The lesson ends with the character \(\vartheta=\overline\Lambda\,\overline G\,\eta\) that appears in every later lesson.

**Prerequisites.** [*S-integers and sixth-power classes*](s-integers-and-sixth-power-classes.md), Lemma 2.1, (3.1)–(3.3) and Lemma 4.1; [*Sextic reciprocity and Kummer characters*](sextic-reciprocity-and-kummer-characters.md), (1.1)–(1.3) and Lemma 3.1; [*Quasi-characters and Hecke characters*](course:NT-ADL/NT-ADL-06), Theorem 6.3; [*Cyclotomic fields*](course:NT-ANT/cyclotomic-fields), Theorem 12.3.

## 1. Gauss and Jacobi sums over a finite field

Let \(k\) be a finite field of odd size \(Q\), \(\psi_k\) a nontrivial additive character, and \(\chi,\chi'\) multiplicative characters extended by \(\chi(0)=0\). Put
\[
\begin{gathered}
G(\chi)=\sum_{x\in k}\chi(x)\psi_k(x),\\
J(\chi,\chi')=\sum_{x\in k}\chi(x)\chi'(1-x).
\end{gathered}
\]

**Lemma 1.1.** Let \(\chi,\chi'\) be nontrivial.

1. \(G(\chi)\overline{G(\chi)}=Q\) and \(G(\chi)G(\overline\chi)=\chi(-1)Q\).
2. If \(\chi\chi'\) is nontrivial, \(J(\chi,\chi')=G(\chi)G(\chi')/G(\chi\chi')\).
3. Replacing \(\psi_k(x)\) by \(\psi_k(ax)\), \(a\in k^\times\), multiplies \(G(\chi)\) by \(\overline{\chi(a)}\).

*Proof.* *3* is the substitution \(x\mapsto a^{-1}x\). *1:* \(G(\chi)\overline{G(\chi)}=\sum_{x,y}\chi(x)\overline{\chi(y)}\psi_k(x-y)\); put \(x=ty\) for \(y\ne0\) to get \(\sum_t\chi(t)\sum_{y\ne0}\psi_k((t-1)y)\), which is \(\sum_t\chi(t)(Q\mathbf 1_{t=1}-1)=Q\). Since \(\overline{G(\chi)}=\chi(-1)G(\overline\chi)\) by *3* with \(a=-1\), the second identity follows. *2:* \(G(\chi)G(\chi')=\sum_{x,y}\chi(x)\chi'(y)\psi_k(x+y)\). Group by \(s=x+y\). For \(s\ne0\) write \(x=su\), \(y=s(1-u)\): the contribution is \(\chi\chi'(s)\psi_k(s)J(\chi,\chi')\), summing to \(G(\chi\chi')J(\chi,\chi')\). For \(s=0\) the contribution is \(\chi'(-1)\sum_x\chi\chi'(x)=0\). Divide by \(G(\chi\chi')\ne0\). \(\square\)

**Lemma 1.2** (Davenport–Hasse lifting). Let \(k'\supseteq k\) have degree \(f\), and put \(\chi'=\chi\circ\operatorname N_{k'/k}\), \(\psi'=\psi_k\circ\operatorname{Tr}_{k'/k}\). If \(\chi\) is nontrivial, then
\[
\begin{aligned}
&-G_{k'}(\chi',\psi')\\
&\quad =\bigl(-G_k(\chi,\psi_k)\bigr)^f .\quad(1.1)
\end{aligned}
\]
Consequently, if \(\chi,\chi''\) and \(\chi\chi''\) are nontrivial, \(J_{k'}(\chi\circ\operatorname N,\chi''\circ\operatorname N)=(-1)^{f-1}J_k(\chi,\chi'')^f\).

*Proof.* For a monic \(h\in k[T]\) of degree \(d\) with roots \(\alpha_1,\dots,\alpha_d\) in an algebraic closure, counted with multiplicity, put \(\lambda(h)=\chi(\alpha_1\cdots\alpha_d)\psi_k(\alpha_1+\cdots+\alpha_d)\). Both the sum and the product of the roots lie in \(k\), and \(\lambda(h_1h_2)=\lambda(h_1)\lambda(h_2)\). If \(h=T^d+c_1T^{d-1}+\cdots+c_d\), then \(\lambda(h)=\chi((-1)^dc_d)\psi_k(-c_1)\). Consider the power series \(L(u)=\sum_h\lambda(h)u^{\deg h}\) over monic \(h\). The monic polynomials of degree \(1\) contribute \(\sum_{a\in k}\chi(a)\psi_k(a)u=G_k u\). For \(d\ge2\) the coefficients \(c_1\) and \(c_d\) vary independently, and \(\sum_{c_d}\chi((-1)^dc_d)=0\); so
\[
L(u)=1+G_ku .
\]
Unique factorization in \(k[T]\) and complete multiplicativity give \(L(u)=\prod_P(1-\lambda(P)u^{\deg P})^{-1}\) over monic irreducible \(P\), as formal power series. Taking \(u\frac d{du}\log\),
\[
\begin{aligned}
&\sum_P\sum_{m\ge1}\deg(P)\,\lambda(P)^mu^{m\deg P}\\
&\quad =\frac{G_ku}{1+G_ku}\\
&\quad =\sum_{n\ge1}(-1)^{n-1}G_k^nu^n .
\end{aligned}
\]
The coefficient of \(u^f\) on the left is \(\sum_{e\mid f}\sum_{\deg P=e}e\,\lambda(P)^{f/e}\). An element \(y\in k'\) is a root of exactly one monic irreducible \(P\), of degree \(e\mid f\), whose \(e\) roots are its conjugates; then \(\lambda(P)=\chi(\operatorname N_{k(y)/k}y)\psi_k(\operatorname{Tr}_{k(y)/k}y)\), and \(\lambda(P)^{f/e}=\chi(\operatorname N_{k'/k}y)\psi_k(\operatorname{Tr}_{k'/k}y)\). The element \(y=0\) belongs to \(P=T\), where \(\lambda(T)=0\). So the coefficient is \(G_{k'}(\chi',\psi')\), and \(G_{k'}=(-1)^{f-1}G_k^f\), which is (1.1). The statement for Jacobi sums follows from Lemma 1.1(2) at both levels, since \(\chi\circ\operatorname N\) is nontrivial when \(\chi\) is (the norm is surjective). \(\square\)

**Corollary 1.3** ([OpenAI-029, (3.11)]). Let \(\chi\) have exact order \(6\), \(\rho=\chi^2\), \(\phi=\chi^3\), and \(G_j=G(\chi^j)\). Then
\[
\begin{gathered}
G_2G_4=Q,\\
G_2^2=J(\rho,\rho)G_4,\\
(Q^{-1/2}G_2)^3=Q^{-1/2}J(\rho,\rho),\quad(1.2)
\end{gathered}
\]
and the cube \((Q^{-1/2}G_2)^3\) does not depend on \(\psi_k\). Moreover
\[
\begin{gathered}
J(\chi,\chi)=\overline{\chi(4)}\,J(\phi,\chi),\\
G_1G_4=\overline{\chi(4)}\,G_2G_3 .\quad(1.3)
\end{gathered}
\]

*Proof.* \(\rho(-1)=\chi(-1)^2\) and \(\chi(-1)^6=1\) with \(\chi(-1)=\pm1\), so \(\rho(-1)=1\) and Lemma 1.1(1) gives \(G_2G_4=Q\) (as \(\chi^4=\overline\rho\)). Lemma 1.1(2) with \(\chi=\chi'=\rho\), where \(\rho^2=\chi^4\ne1\), gives the second identity, and multiplying it by \(G_2\) gives \(G_2^3=QJ(\rho,\rho)\). Changing \(\psi_k\) multiplies \(G_2\) by \(\overline{\rho(a)}\), whose cube is \(1\). For (1.3), put \(x=(1+t)/2\): then \(x(1-x)=(1-t^2)/4\), so \(J(\chi,\chi)=\overline{\chi(4)}\sum_t\chi(1-t^2)\). The number of \(t\) with \(t^2=s\) is \(1+\phi(s)\), so \(\sum_t\chi(1-t^2)\)\(=\sum_s\chi(1-s)+\sum_s\phi(s)\chi(1-s)\)\(=J(\phi,\chi)\). By Lemma 1.1(2), \(J(\chi,\chi)=G_1^2/G_2\) and \(J(\phi,\chi)=G_3G_1/G_4\) (as \(\phi\chi=\chi^4\ne1\)), which gives the last identity. \(\square\)

## 2. Cubic Jacobi sums over the Eisenstein integers

Let \(E_0=\mathbb Q(\omega)\) with \(\omega^2+\omega+1=0\), and \(t=1-\omega\), so that \((t^2)=(3)\). The ring \(\mathbb Z[\omega]\) has class number one, and its six units \(\pm1,\pm\omega,\pm\omega^2\) map bijectively onto \((\mathbb Z[\omega]/3)^\times\), a group of order \(6\). Hence every ideal \(\mathfrak a\) prime to \(3\) has a unique generator \(\pi_+(\mathfrak a)\equiv1\pmod 3\), and \(\pi_+(\mathfrak a\mathfrak b)=\pi_+(\mathfrak a)\pi_+(\mathfrak b)\).

**Lemma 2.1** ([OpenAI-029, (3.12)]). Let \(\mathfrak q\) be a prime of \(\mathbb Z[\omega]\) not dividing \(6\), with residue field of size \(Q'\), and let \(\rho(x)\equiv x^{(Q'-1)/3}\pmod{\mathfrak q}\) be its cubic residue character. Then
\[
J(\rho,\rho)=-\pi_+(\mathfrak q).
\tag{2.1}
\]

*Proof.* *Divisibility.* Modulo \(\mathfrak q\), \(J(\rho,\rho)\equiv\sum_{x}x^{k}(1-x)^k\) with \(k=(Q'-1)/3\) (both sides vanish at \(x=0,1\)). Every monomial \(x^j\) in \(x^k(1-x)^k\) has \(0<k\le j\le2k<Q'-1\), and \(\sum_{x\in\mathbb F_{Q'}}x^j=0\) for such \(j\). So \(J\in\mathfrak q\). *Norm.* By Lemma 1.1, \(|J|^2=|G(\rho)|^4/|G(\rho^2)|^2=Q'\). *Congruence.* Write \(\rho(x)=\omega^{k(x)}\) with \(k(x)\in\{0,1,2\}\); since \(\omega=1-t\), \(\omega^k\equiv1-kt\pmod{t^2}\). Each value of \(\rho\) occurs \((Q'-1)/3\) times on \(\mathbb F_{Q'}^\times\), so \(\sum_{x\ne0,1}k(x)=\sum_{x\ne0,1}k(1-x)\)\(=Q'-1\), and
\[
\begin{aligned}
J&\equiv(Q'-2)\\
&\quad-t\sum_{x\ne0,1}\bigl(k(x)+k(1-x)\bigr)\\
&=Q'-2-2(Q'-1)t\\
&\equiv-1\pmod 3,
\end{aligned}
\]
because \(Q'\equiv1\pmod 3\). The ideal \((J)\) is contained in \(\mathfrak q\) and has norm \(|J|^2=Q'=\operatorname N\mathfrak q\), so \((J)=\mathfrak q\); and \(-J\equiv1\pmod3\). \(\square\)

Define on ideals of \(\mathbb Z[\omega]\) prime to \(3\)
\[
\Lambda_{E_0}(\mathfrak a)=\frac{\pi_+(\mathfrak a)}{|\pi_+(\mathfrak a)|}.
\tag{2.2}
\]
It is multiplicative, and on a principal ideal generated by \(a\equiv1\pmod3\) its value is \(a/|a|\). So it is a Größencharakter modulo \((3)\) with angular infinity type of exponent \(1\), and by Theorem 6.3 of [*Quasi-characters and Hecke characters*](course:NT-ADL/NT-ADL-06) it corresponds to a unitary Hecke character of \(E_0\) with finite conductor dividing \((3)\).

## 3. The character Lambda

Return to the field \(F\supseteq\mu_{12}\) and the data of Lessons 2 and 3. Since \(\omega=\zeta_{12}^4\in F\), the field \(F\) contains \(E_0\). Put
\[
\Lambda=\Lambda_{E_0}\circ\operatorname N_{F/E_0},
\]
the composition of (2.2) with the relative norm of ideals (equivalently, of idèles). It is a unitary Hecke character of \(F\), unramified outside the places above \(3\), which lie in \(S\); at each complex place of \(F\) its infinity type is purely angular, of exponent \(1\) or \(-1\) in the ordinary angular coordinate, because the norm at infinity is a product of complex coordinates and their conjugates.

For a squarefree exterior ideal \(\mathfrak c\) with allowed generator \(c\) define the normalized Gauss sums
\[
\begin{gathered}
\begin{aligned}
\gamma_j(\mathfrak c)&=q_{\mathfrak c}^{-1/2}\sum_{x\bmod\mathfrak c}\chi_{\mathfrak c}(x)^j\\
&\quad \,\mathrm e(x/c),
\end{aligned}\\
\gamma_j(R)=1 .\quad(3.1)
\end{gathered}
\]
By Lemma 2.1 of [*S-integers and sixth-power classes*](s-integers-and-sixth-power-classes.md), \(x\mapsto\mathrm e(x/c)\) is a well-defined additive character of \(R/\mathfrak c\), and \(x\mapsto\mathrm e(xy/c)\) is trivial exactly when \(y\in\mathfrak c\). Replacing \(c\) by \(\epsilon^6c\) with \(\epsilon\in U_S\) is absorbed by the substitution \(x\mapsto\epsilon^6x\), so \(\gamma_j(\mathfrak c)\) does not depend on the allowed generator. At an exterior prime, the product formula for \(\psi\) gives \(\mathrm e(x/p)=\psi_{\mathfrak p}(-x/p)\), since \(x/p\) is integral at every other place outside \(S\); by (1.3) of Lesson 3, \(\chi_{\mathfrak p}(-1)=1\), and the sign may be dropped in prime Gauss sums.

**Lemma 3.1** ([OpenAI-029, Lemma 3.4, first identity]). For every exterior prime \(\mathfrak p\),
\[
\gamma_2(\mathfrak p)^3=-\Lambda(\mathfrak p).
\tag{3.2}
\]

*Proof.* Let \(\mathfrak q=\mathfrak p\cap E_0\), with residue field of size \(Q'\), and let \(f\) be the residue degree of \(\mathfrak p\) over \(\mathfrak q\); the residue field \(k\) of \(\mathfrak p\) has size \(Q=Q'^f\). The cubic character \(\chi_{\mathfrak p}^2\) at \(\mathfrak p\) is \(x\mapsto x^{(Q-1)/3}\), and \(x^{(Q-1)/3}=(x^{(Q-1)/(Q'-1)})^{(Q'-1)/3}\); so it is the cubic character of \(\mathfrak q\) composed with the norm \(k\to\mathbb F_{Q'}\). By Corollary 1.3 and Lemma 1.2, then Lemma 2.1,
\[
\begin{aligned}
\gamma_2(\mathfrak p)^3&=Q^{-1/2}J_k(\chi_{\mathfrak p}^2,\chi_{\mathfrak p}^2)\\
&=Q^{-1/2}(-1)^{f-1}\bigl(-\pi_+(\mathfrak q)\bigr)^f\\
&=-\frac{\pi_+(\mathfrak q)^f}{Q^{1/2}} .
\end{aligned}
\]
Since \(|\pi_+(\mathfrak q)|^2=Q'\) and \(\operatorname N_{F/E_0}\mathfrak p=\mathfrak q^f\), the right side is \(-\Lambda_{E_0}(\mathfrak q^f)=-\Lambda(\mathfrak p)\). \(\square\)

## 4. The Weil index and the character G

The sign of the quadratic Gauss sum \(\gamma_3(\mathfrak p)\) is governed by a global reciprocity of a different kind. For a place \(v\) and \(a\in F_v^\times\), Weil attached an eighth root of unity, the **Weil index** \(\gamma_{\psi_v}(a)\), to the character of second degree \(x\mapsto\psi_v(ax^2)\) of \(F_v\): it is the constant in the Fourier transform of this character as a tempered distribution. Put
\[
\mathfrak w_v(a)=\frac{\gamma_{\psi_v}(a)}{\gamma_{\psi_v}(1)} .
\]

**Named result N2** (Weil's index). 

1. \(\mathfrak w_v(a)\) depends only on the square class of \(a\), and \(\mathfrak w_v(a)\mathfrak w_v(b)=(a,b)_{2,v}\,\mathfrak w_v(ab)\) (Rao, Theorem A.4).
2. For \(a\in F^\times\), \(\mathfrak w_v(a)=1\) for almost all \(v\), and \(\prod_v\mathfrak w_v(a)=1\) (Weil's product formula, applied to the forms \(ax^2\) and \(x^2\); Liu–Zhu, Theorem 2.8).
3. At a finite place \(v\nmid2\) where \(\psi_v\) has conductor \(\mathcal O_v\), with residue field of size \(q_v\) and uniformizer \(\varpi\): \(\mathfrak w_v(u)=1\) for units \(u\), and \(\mathfrak w_v(\varpi^{-1})\)\(=q_v^{-1/2}\sum_{x\bmod\varpi}\psi_v(x^2/\varpi)\) (Rao, Proposition A.11).

These statements are used without proof in the programme. The symbol \((a,b)_{2,v}\) is the quadratic Hilbert symbol, symmetric in its arguments, and equal to \((a,b)_{6,v}^3\) in the notation of Lesson 2.

**Lemma 4.1** ([OpenAI-029, Lemma 3.4, the character G]). Put \(\mathfrak w_S=\prod_{v\in S}\mathfrak w_v\). For every exterior prime \(\mathfrak p\) with allowed generator \(p\),
\[
\begin{aligned}
&\gamma_3(\mathfrak p)\\
&\quad =\mathfrak w_S(p^{-1})^{-1}\in\{\pm1\},\quad(4.1)
\end{aligned}
\]
and \([a]\mapsto\mathfrak w_S(a^{-1})^{-1}\) is a character of \(B\). Consequently there is a finite-order Hecke character \(G\) of \(F\), unramified outside \(S\), with
\[
G(\mathfrak p)=\overline{\chi_{\mathfrak p}(4)}\,\gamma_3(\mathfrak p)
\tag{4.2}
\]
for every exterior prime \(\mathfrak p\).

*Proof.* Let \(\mathfrak p\) have residue field of size \(Q\). The number of square roots of \(x\) in the residue field is \(1+\chi_{\mathfrak p}(x)^3\), with the unit mask at \(x=0\), and \(\sum_x\psi_{\mathfrak p}(x/p)=0\). So
\[
\begin{aligned}
&Q^{-1/2}\sum_{x\bmod\mathfrak p}\psi_{\mathfrak p}(x^2/p)\\
&\quad =Q^{-1/2}\sum_x\chi_{\mathfrak p}(x)^3\psi_{\mathfrak p}(x/p)\\
&\quad =\gamma_3(\mathfrak p),
\end{aligned}
\]
the last step by the remark after (3.1). By N2(3), the left side is \(\mathfrak w_{\mathfrak p}(p^{-1})\). Apply N2(2) to \(p^{-1}\in F^\times\). At an exterior place other than \(\mathfrak p\), \(p^{-1}\) is a unit; these places are odd, and \(\psi_v\) has conductor \(\mathcal O_v\) there by the choice of \(S\), so N2(3) gives \(\mathfrak w_v(p^{-1})=1\). The product formula leaves \(\mathfrak w_S(p^{-1})\mathfrak w_{\mathfrak p}(p^{-1})=1\), which is (4.1). Its square is \(1\) because \(\gamma_3(\mathfrak p)^2=\chi_{\mathfrak p}(-1)^3=1\) by Lemma 1.1(1).

For allowed \(a,b\), N2(1) gives \(\mathfrak w_S(a^{-1})\mathfrak w_S(b^{-1})\)\(=\prod_{v\in S}(a^{-1},b^{-1})_{2,v}\,\mathfrak w_S((ab)^{-1})\), and \(\prod_{v\in S}(a^{-1},b^{-1})_{2,v}=H_S(a,b)^3=1\) because \([a],[b]\in B\) and \(B\) is isotropic. So the map is a character of \(B\); it depends only on square classes, hence only on the class in \(B\). Lemma 3.1(4) of [*Sextic reciprocity and Kummer characters*](sextic-reciprocity-and-kummer-characters.md) extends it to a finite-order Hecke character unramified outside \(S\) whose value at \(\mathfrak p\) is \(\gamma_3(\mathfrak p)\). Since \(4\in U_S\), the Kummer character \(\kappa_4\) is unramified outside \(S\) with \(\kappa_4(\mathfrak p)=\chi_{\mathfrak p}(4)\); multiplying by \(\overline{\kappa_4}\) gives \(G\). \(\square\)

## 5. The duplication identity and multiplicativity

**Proposition 5.1** ([OpenAI-029, Lemma 3.4]). For every exterior prime \(\mathfrak p\),
\[
\gamma_1(\mathfrak p)\gamma_2(\mathfrak p)=-\Lambda(\mathfrak p)G(\mathfrak p).
\tag{5.1}
\]
For coprime squarefree exterior ideals \(\mathfrak c_1,\mathfrak c_2\) with allowed generators \(c_1,c_2\), and every integer \(j\),
\[
\begin{aligned}
\gamma_j(\mathfrak c_1\mathfrak c_2)&=\chi_{\mathfrak c_1}(c_2)^j\chi_{\mathfrak c_2}(c_1)^j\\
&\quad \gamma_j(\mathfrak c_1)\gamma_j(\mathfrak c_2).\quad(5.2)
\end{aligned}
\]

*Proof.* With \(G_j\) the Gauss sums of \(\chi_{\mathfrak p}^j\) for the additive character \(x\mapsto\psi_{\mathfrak p}(x/p)\), (1.3) and \(G_2G_4=Q\) give \(G_1=\overline{\chi_{\mathfrak p}(4)}G_2^2G_3/Q\), so
\[
\begin{aligned}
\gamma_1\gamma_2&=Q^{-1}G_1G_2=\overline{\chi_{\mathfrak p}(4)}\,Q^{-2}G_2^3G_3\\
&=\overline{\chi_{\mathfrak p}(4)}\,\gamma_3(\mathfrak p)\gamma_2(\mathfrak p)^3 ,
\end{aligned}
\]
which is \(-\Lambda(\mathfrak p)G(\mathfrak p)\) by (3.2) and (4.2). For (5.2), every residue modulo \(\mathfrak c_1\mathfrak c_2\) is uniquely \(x=c_2y_1+c_1y_2\) with \(y_i\) modulo \(\mathfrak c_i\), by the Chinese remainder theorem. Then \(\mathrm e(x/(c_1c_2))=\mathrm e(y_1/c_1)\mathrm e(y_2/c_2)\) and \(\chi_{\mathfrak c_1\mathfrak c_2}(x)^j=\chi_{\mathfrak c_1}(c_2y_1)^j\chi_{\mathfrak c_2}(c_1y_2)^j\), which factors as stated; the product \(c_1c_2\) is an allowed generator of \(\mathfrak c_1\mathfrak c_2\). The unit mask makes the formula valid for \(j\equiv0\pmod6\) as well. \(\square\)

## 6. The character theta

Put
\[
\vartheta=\overline\Lambda\,\overline G\,\eta .
\tag{6.1}
\]
Its finite conductor is supported in \(S\). Write \(\vartheta_v\) for its local components and define the smooth unitary character
\[
L_S(y)=\prod_{v\in S}\vartheta_v(y_v)^{-1}\qquad(y\in F_S^\times).
\]

**Lemma 6.1** ([OpenAI-029, (3.14)]). For every exterior ideal \(\mathfrak a\) with allowed generator \(a\), and every \(\epsilon\in U_S\),
\[
\begin{gathered}
\vartheta(\mathfrak a)=L_S(a),\\
L_S(\epsilon)=1 .\quad(6.2)
\end{gathered}
\]
At each complex place the component of \(L_S\) is purely angular, of exponent \(1\) or \(-1\).

*Proof.* The idèle character \(\vartheta\) is trivial on \(F^\times\), so \(\prod_{v\notin S}\vartheta_v(a)=L_S(a)\). Outside \(S\) it is unramified, and \(\prod_{v\notin S}\vartheta_v(a)=\prod_{\mathfrak p}\vartheta(\mathfrak p)^{v_{\mathfrak p}(a)}=\vartheta(\mathfrak a)\). For \(\epsilon\in U_S\) the same product is \(1\). Finite-order characters are trivial on the connected group \(\mathbb C^\times\), so the complex components of \(G\) and \(\eta\) are trivial and those of \(L_S\) come from \(\Lambda\). \(\square\)

The relations (3.2), (5.1) and (6.2) are what the rest of the course uses: at a prime, \(\gamma_1(\mathfrak p)\gamma_2(\mathfrak p)\vartheta(\mathfrak p)=-\eta(\mathfrak p)\).

## 7. Exercises

**7.1.** Show that \(\gamma_j(\mathfrak p)\) has absolute value \(1\) for \(j\not\equiv0\pmod 6\), and compute \(\gamma_0(\mathfrak p)\).

**7.2.** Let \(\mathfrak q=(3+\omega)\), of norm \(7\). Find \(\pi_+(\mathfrak q)\) and verify (2.1) by computing \(J(\rho,\rho)\) in \(\mathbb Z[\omega]\).

**7.3.** Let \(\ell\equiv2\pmod3\) be a prime. Show that \(\pi_+((\ell))=-\ell\), and deduce from Lemma 2.1 that the cubic Jacobi sum over \(\mathbb F_{\ell^2}\) equals \(\ell\).

**7.4.** Show that \(\gamma_3(\mathfrak p)\) is also equal to \(\gamma_3\) computed with the additive character \(x\mapsto\psi_{\mathfrak p}(ux/p)\) for every unit \(u\) that is a square modulo \(\mathfrak p\), and changes sign for a nonsquare.

**7.5.** Prove the claim in the proof of Lemma 1.2 that \(\lambda(h_1h_2)=\lambda(h_1)\lambda(h_2)\), and that \(\lambda(h)=\chi((-1)^dc_d)\psi_k(-c_1)\).

## 8. Solutions

**7.1.** For \(j\not\equiv0\), \(\chi_{\mathfrak p}^j\) is a nontrivial character and Lemma 1.1(1) gives \(|G|^2=Q\). For \(j\equiv0\), the unit mask gives \(\gamma_0(\mathfrak p)=Q^{-1/2}\sum_{x\ne0}\mathrm e(x/p)=-Q^{-1/2}\).

**7.2.** \(3+\omega\equiv\omega\pmod 3\), and the generator \(\equiv1\) is \(\omega^{2}(3+\omega)=3\omega^2+1=-2-3\omega\). Modulo \(\mathfrak q\), \(\omega\equiv-3\equiv4\pmod7\), a cube root of unity in \(\mathbb F_7\). Computing \(\rho(x)=x^2\bmod7\) as a power of \(4\) for \(x=2,\dots,6\) and summing \(\rho(x)\rho(1-x)\) gives \(J=2+3\omega=-\pi_+(\mathfrak q)\).

**7.3.** The generators of \((\ell)\) are \(\pm\ell\omega^i\), and \(-\ell\equiv1\pmod3\). The ideal \((\ell)\) is prime of norm \(\ell^2\) (Theorem 12.3 of [*Cyclotomic fields*](course:NT-ANT/cyclotomic-fields)), so (2.1) gives \(J=\ell\).

**7.4.** Lemma 1.1(3) multiplies the Gauss sum of \(\chi_{\mathfrak p}^3\) by \(\overline{\chi_{\mathfrak p}(u)^3}=\chi_{\mathfrak p}(u)^3\), which is the quadratic character of \(u\).

**7.5.** The roots of \(h_1h_2\) are those of \(h_1\) and \(h_2\) together, so their product is multiplicative and their sum additive; \(\chi\) is multiplicative and \(\psi_k\) additive. For \(h=\prod(T-\alpha_i)\), \(c_1=-\sum\alpha_i\) and \(c_d=(-1)^d\prod\alpha_i\).

## Sources

- [OpenAI-029] OpenAI, *Primitive roots for every admissible integer base*, OpenAI Math Release preprint, 4 October 2026, Section 3. https://github.com/openai/math/tree/main/preprints/Primitive-roots-for-every-admissible-integer-base-October-4-2026
- R. Ranga Rao, *On some explicit formulas in the theory of Weil representation*, Pacific J. Math. 157 (1993), 335–371, Appendix (Theorem A.4, Proposition A.11). https://msp.org/pjm/1993/157-2/pjm-v157-n2-p09-s.pdf
- D. Liu and Y. Zhu, *LCA(2), Weil index, and product formula*, arXiv:1708.09205v1, Section 2.4 (Theorem 2.8, Weil's product formula). https://arxiv.org/abs/1708.09205v1
- S. Baier and M. P. Young, *Mean values with cubic characters*, arXiv:0804.2233v4, Section 2.2 (the cubic Gauss sum identity in the form \(g(n)^3=\mu(n)\operatorname N(n)n\)). https://arxiv.org/abs/0804.2233v4
