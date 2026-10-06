# First cases: characters and the real correspondence

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

Local class field theory already answers a Langlands question: which Galois-side object belongs to a character of a local field? The higher-dimensional correspondence asks the same question for representations of a general linear group. Before treating a nonarchimedean field, we work out the real two-dimensional dictionary. This case makes the role of induction, the central character and the gamma factors visible in formulas.

We assume local reciprocity and the classification of irreducible admissible representations of the real general linear group. The representation-theoretic input is stated precisely below; it is the subject of *Representations of the real and complex general linear groups*. Basic references are [Getz–Hahn 2022], [Jacquet–Langlands 1970], [Knapp 1994] and [Deligne 1973].

## 1. Fixing reciprocity before fixing a parameter

Let \(F\) be a nonarchimedean local field with residue cardinality \(q\), normalized absolute value \(\lvert\varpi\rvert_F=q^{-1}\), and Weil group \(W_F\). In this course,

\[
\operatorname{Art}_F(\varpi)=\Phi_{\mathrm{geom}},
\qquad
\lVert w\rVert=\lvert\operatorname{Art}_F^{-1}(w)\rvert_F.
\tag{1.1}
\]

The inverse on the right is understood on the abelianization; the resulting norm character is defined on all of \(W_F\). Thus \(\lVert\Phi_{\mathrm{geom}}\rVert=q^{-1}\). We write

\[
\operatorname{rec}_1(\chi)=\chi\circ\operatorname{Art}_F^{-1}.
\]

Local class field theory supplies a bijection between smooth characters of \(F^\times\) and one-dimensional smooth representations of \(W_F\). The character conductor is the least \(a\ge0\) for which \(\chi\) is trivial on the unit filtration: conductor zero means trivial on \(\mathcal O_F^\times\), while for \(a\ge1\) it means trivial on \(1+\mathfrak p_F^a\). The ramification theorem of local class field theory equates this with the Artin conductor of \(\operatorname{rec}_1\chi\).

For an unramified character,

\[
L(s,\chi)=(1-\chi(\varpi)q^{-s})^{-1};
\]

for a ramified character this factor is one. This is also the determinant definition on the inertia-invariant space of \(\operatorname{rec}_1\chi\). The local epsilon factor on the Weil side is normalized to equal Tate's epsilon factor for characters. With self-dual additive measures, replacing \(\psi\) by \(\psi_a(x)=\psi(ax)\) gives

\[
\epsilon(s,\chi,\psi_a)
=\chi(a)\lvert a\rvert_F^{s-1/2}\epsilon(s,\chi,\psi).
\tag{1.2}
\]

Thus the rank-one correspondence preserves conductors and factors by the reciprocity and normalization theorems, rather than by an additional existence argument.

If reciprocity instead sends a uniformizer to arithmetic Frobenius, its map is the inverse of (1.1). The same character of \(F^\times\) then gives the inverse character on \(W_F\). One must translate all character labels at the same time. Keeping (1.1) and changing only a Frobenius label would change the Euler factor.

**Example 1.1.** For odd \(p\), choose a generator \(g\) of \(\mathbb F_p^\times\) and a \((p-1)\)-st root of unity \(\zeta\ne1\). Define a character of \(\mathbb Q_p^\times\) by \(\chi(p)=1\) and \(\chi(u)=\zeta^j\) when \(u\bmod p=g^j\). It is trivial on \(1+p\mathbb Z_p\) and nontrivial on \(\mathbb Z_p^\times\), so its conductor is one. Its Weil character is tamely ramified with the same conductor, and its local \(L\)-factor is one. The nontriviality condition matters: the trivial residue character has conductor zero.

Globally, class field theory similarly identifies Hecke characters with one-dimensional characters of the global Weil group, compatibly with localization. We use only the local theorem in this course.

## 2. The real Weil group and all its irreducibles

The real Weil group is

\[
W_{\mathbb R}=\mathbb C^\times\sqcup j\mathbb C^\times,
\qquad j^2=-1,\quad jzj^{-1}=\bar z.
\]

Put \(\lvert z\rvert_{\mathbb C}=z\bar z\). The real reciprocity map identifies the image of \(z\in\mathbb C^\times\) in the abelianization with \(z\bar z\in\mathbb R_{>0}\), and the image of \(j\) with \(-1\). Hence a character \(\chi_{t,e}(x)=\lvert x\rvert^t\operatorname{sgn}(x)^e\), with \(t\in\mathbb C\) and \(e\in\{0,1\}\), corresponds to

\[
\mu_{t,e}(z)=\lvert z\rvert_{\mathbb C}^{t},
\qquad \mu_{t,e}(j)=(-1)^e.
\tag{2.1}
\]

For \(m\ge1\), define

\[
\omega_{m,t}(z)=(z/\lvert z\rvert)^m\lvert z\rvert_{\mathbb C}^{t},
\qquad R_{m,t}=\operatorname{Ind}_{\mathbb C^\times}^{W_{\mathbb R}}\omega_{m,t}.
\tag{2.2}
\]

**Proposition 2.1 (Weil-group prerequisite).** The irreducible continuous complex representations of \(W_{\mathbb R}\) are exactly the characters (2.1) and the two-dimensional representations (2.2). The labels \((t,e)\) and \((m,t)\), with \(m\ge1\), are unique.

This is [Representations of Weil groups](https://kokunoyumeto.github.io/open-math-courses-public/courses/LG-GAL/representations-of-weil-groups.html), Theorem 5.1. Its polar character \(\omega_{a,n}(re^{i\theta})=r^a e^{in\theta}\) has \((a,n)=(2t,m)\) in our notation. Conjugation changes \(m\) to \(-m\), and the positive choice is unique. This imported classification supplies the parameter side of our dictionary; the dictionary and factor comparison are proved below.

One convenient matrix for \(j\) in (2.2) is

\[
R_{m,t}(j)=\begin{pmatrix}0&(-1)^m\\1&0\end{pmatrix}.
\]

Its determinant is \((-1)^{m+1}\). On \(\mathbb C^\times\) the determinant is \(\lvert z\rvert_{\mathbb C}^{2t}\). By real reciprocity,

\[
\det R_{m,t}\ \longleftrightarrow\
\lvert x\rvert^{2t}\operatorname{sgn}(x)^{m+1}.
\tag{2.3}
\]

## 3. A dictionary that includes finite-dimensional representations

We use normalized induction

\[
I(\chi_1,\chi_2)=\operatorname{Ind}_{B(\mathbb R)}^{\operatorname{GL}_2(\mathbb R)}(\chi_1\otimes\chi_2).
\]

The following is the precise classification input from [Jacquet–Langlands 1970, Theorem 5.11]. For characters \(\chi_i=\lvert\cdot\rvert^{t_i}\operatorname{sgn}^{e_i}\), this induction is irreducible unless

\[
\chi_1\chi_2^{-1}(x)=x^d\operatorname{sgn}(x)
\quad\text{for a nonzero integer }d.
\tag{3.1}
\]

For \(d>0\) it has a discrete-series subrepresentation and a finite-dimensional quotient; for \(d<0\) the order is reversed. The finite-dimensional constituent, or the full induction in the irreducible case, is denoted \(P(\chi_1,\chi_2)\). It depends only on the unordered pair of characters, and different unordered pairs give different representations. The remaining irreducible admissible representations are the discrete series \(D_k\otimes\lvert\det\rvert^t\), with \(k\ge2\), uniquely determined by \(k,t\). Here \(D_k\) is the representation of the full, disconnected real group; on the positive-determinant component it contains the holomorphic and antiholomorphic discrete series exchanged by a reflection. Its central character is \(\operatorname{sgn}^k\).

**Theorem 3.1.** There is a bijection from semisimple two-dimensional representations of \(W_{\mathbb R}\) to irreducible admissible representations of \(\operatorname{GL}_2(\mathbb R)\), given by

\[
\mu_{t_1,e_1}\oplus\mu_{t_2,e_2}
\longmapsto P(\chi_{t_1,e_1},\chi_{t_2,e_2}),
\qquad
R_{m,t}\longmapsto D_{m+1}\otimes\lvert\det\rvert^t.
\tag{3.2}
\]

The determinant of the parameter corresponds to the central character.

**Proof.** Proposition 2.1 says that a semisimple parameter of dimension two is either an unordered sum of two characters or one of the unique induced parameters \(R_{m,t}\). The classification input gives the same two disjoint sets of labels on the representation side. This proves surjectivity and injectivity, including the reducible induction cases (3.1). On a principal-series constituent, a scalar matrix \(xI\) acts by \(\chi_1(x)\chi_2(x)\); the normalizing modulus is one on the center. This agrees with the determinant of the two characters. On \(D_{m+1}\otimes\lvert\det\rvert^t\), the central character is \(\operatorname{sgn}^{m+1}\lvert\cdot\rvert^{2t}\), which is (2.3). \(\square\)

**Example 3.2.** The trivial representation of the real general linear group belongs to the parameter \(\mu_{1/2,0}\oplus\mu_{-1/2,0}\). The corresponding induction has a one-dimensional Langlands quotient. It would therefore be incorrect to send every character sum to an irreducible principal series without specifying its constituent.

The holomorphic weight-\(k\) parameter is \(R_{k-1,0}\) in unitary normalization. A spherical Maass representation with Laplace eigenvalue \(1/4+r^2\) has parameter \(\mu_{ir,0}\oplus\mu_{-ir,0}\). Its factor is \(\Gamma_{\mathbb R}(s+ir)\Gamma_{\mathbb R}(s-ir)\). The representation is determined by \(r\) up to sign; complementary-series parameters use imaginary \(r\) in the same formula.

## 4. Computing the factors and the induction constant

Fix

\[
\psi_{\mathbb R}(x)=e^{2\pi ix},\quad
\psi_{\mathbb C}(z)=\psi_{\mathbb R}(\operatorname{Tr}_{\mathbb C/\mathbb R}z),
\quad
\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2),\quad
\Gamma_{\mathbb C}(s)=2(2\pi)^{-s}\Gamma(s).
\]

Use self-dual additive measures \(dx\) and \(2\,dx\,dy\). Fourier transformation uses the plus sign in \(\psi(xy)\).

For a real character, the Gaussian and its odd companion give

\[
L(s,\mu_{t,e})=\Gamma_{\mathbb R}(s+t+e),
\qquad \epsilon(s,\mu_{t,e},\psi_{\mathbb R})=i^e.
\tag{4.1}
\]

For example \(x^e e^{-\pi x^2}\) has Fourier transform \(i^e x^e e^{-\pi x^2}\), for \(e=0,1\). Its Mellin transform against \(\operatorname{sgn}^e\lvert x\rvert^{s+t}\) is \(\Gamma_{\mathbb R}(s+t+e)\). Evaluating the Tate functional equation on this vector gives (4.1).

Similarly, for \(m\ge0\), the test function \(\bar z^m e^{-2\pi\lvert z\rvert^2}\) has Fourier transform \(i^m z^m e^{-2\pi\lvert z\rvert^2}\) with the complex trace pairing. In polar coordinates its Mellin integral is a constant independent of \(s,t,m\) times

\[
\Gamma_{\mathbb C}(s+t+m/2).
\]

One can use \(d^\times z=2\,dx\,dy/\lvert z\rvert^2\); the constant is then \(\pi\), and cancels in the functional equation. It follows that

\[
L(s,\omega_{m,t})=\Gamma_{\mathbb C}(s+t+m/2),
\qquad \epsilon(s,\omega_{m,t},\psi_{\mathbb C})=i^m.
\tag{4.2}
\]

Induction preserves this \(L\)-factor. For epsilon factors it introduces the Langlands constant. Since \(\operatorname{Ind}_{\mathbb C^\times}^{W_{\mathbb R}}1=1\oplus\operatorname{sgn}\), (4.1) and (4.2) give

\[
\lambda(\mathbb C/\mathbb R,\psi_{\mathbb R})
=\frac{\epsilon(1\oplus\operatorname{sgn},\psi_{\mathbb R})}{\epsilon(1,\psi_{\mathbb C})}=i.
\]

Consequently

\[
L(s,R_{m,t})=\Gamma_{\mathbb C}(s+t+m/2),
\qquad \epsilon(s,R_{m,t},\psi_{\mathbb R})=i^{m+1}.
\tag{4.3}
\]

We now compute the representation-side factors, without assuming their equality with (4.3). The discrete-series Whittaker model with positive additive character has a lowest-weight vector with

\[
W_k(a(y))=2y^{k/2}e^{-2\pi y}\quad(y>0),
\qquad W_k(a(y))=0\quad(y<0),
\tag{4.4}
\]

where \(a(y)=\operatorname{diag}(y,1)\). Its right action under \(k_\theta=\left(\begin{smallmatrix}\cos\theta&\sin\theta\\ -\sin\theta&\cos\theta\end{smallmatrix}\right)\) is \(e^{ik\theta}\). These are the explicit discrete-series model formulas used in the archimedean representation theory; (4.4) follows by solving the lowering-operator equation \(yW'=(k/2-2\pi y)W\), with moderate growth on the negative half-line. This model is the one in [Jacquet–Langlands 1970, §5, Theorem 5.15]. Twisting by \(\lvert\det\rvert^t\) multiplies (4.4) by \(y^t\).

Its zeta integral is exactly

\[
\begin{aligned}
Z(s,W_k\lvert\det\rvert^t)
&=2\int_0^\infty y^{s+t+(k-1)/2}e^{-2\pi y}\,\frac{dy}{y}\\
&=\Gamma_{\mathbb C}(s+t+(k-1)/2).
\end{aligned}
\tag{4.5}
\]

Other \(K\)-finite Whittaker vectors are generated from the lowest-weight vectors by raising operators. Their Mellin transforms are this factor times polynomials and exponential normalizing constants; differentiation is integrated by parts, and multiplication by \(y\) uses \(\Gamma(u+1)=u\Gamma(u)\). Thus (4.5) is the normalized local factor, rather than merely one zeta integral with an accidental extra factor.

The archimedean local functional equation reads

\[
\frac{\widetilde Z(1-s,\pi(w)W)}{L(1-s,\pi^\vee)}
=\epsilon(s,\pi,\psi_{\mathbb R})\frac{Z(s,W)}{L(s,\pi)},
\quad w=k_{\pi/2},
\]

where the tilde integral includes the inverse central character, as in [Jacquet–Langlands 1970, Theorem 5.15]. On (4.4), \(w\) acts by \(i^k\). The inverse central character on \(y>0\) is \(y^{-2t}\), so the tilde integral is \(i^k\Gamma_{\mathbb C}(1-s-t+(k-1)/2)\), precisely \(i^kL(1-s,\pi^\vee)\). Therefore

\[
L(s,D_k\otimes\lvert\det\rvert^t)=\Gamma_{\mathbb C}(s+t+(k-1)/2),
\quad
\epsilon(s,D_k\otimes\lvert\det\rvert^t,\psi_{\mathbb R})=i^k.
\tag{4.6}
\]

Equations (4.3) and (4.6), with \(m=k-1\), prove both factor matchings. The extra \(i\) in the epsilon factor is exactly the induction constant.

For a sum of real characters, the factors are products of (4.1). Normalized principal-series factors, including the factors defined by the Langlands quotient for a finite-dimensional constituent, are the same products. This convention extends factors to the representations with no Whittaker model. It is consistent with (3.2); it is not a claim that a finite-dimensional representation is generic.

## 5. Exercises with solutions

**Exercise 5.1 (easy).** Compute the Weil character belonging to \(\lvert\cdot\rvert^u\) with geometric and arithmetic reciprocity.

**Solution.** With (1.1) it is \(\lVert\cdot\rVert^u\), whose value on geometric Frobenius is \(q^{-u}\). With arithmetic reciprocity it is \(\lVert\cdot\rVert^{-u}\), whose value on the same geometric Frobenius is \(q^u\) and whose value on arithmetic Frobenius is \(q^{-u}\). The two parameter characters are inverse to one another.

**Exercise 5.2 (medium).** Compute the factors and central character for the weight-four discrete series twisted by \(\lvert\det\rvert^{-3/2}\).

**Solution.** Its parameter is \(R_{3,-3/2}\). Formula (4.3) gives \(L(s)=\Gamma_{\mathbb C}(s)\) and \(\epsilon(s)=i^4=1\). The representation-side integral in (4.5) has exponent \(s\) and gives the same gamma factor. Its central character is \(\lvert x\rvert^{-3}\), agreeing with (2.3). More generally the weight-\(k\) factor in unitary normalization is \(\Gamma_{\mathbb C}(s+(k-1)/2)\).

**Exercise 5.3 (medium).** Show that inducing \(\omega_{m,t}\) or its complex conjugation transform gives the same parameter. Translate \(z^{-a}\bar z^{-b}\) when \(a-b=k-1>0\).

**Solution.** Exchanging the two coset basis vectors exchanges \(\omega\) and \(\omega^j\). The new character has angular exponent \(-m\) and the same radial exponent \(t\), so its induction is unchanged. For the displayed algebraic character, the angular exponent is \(b-a=-(k-1)\) and \(t=-(a+b)/2\). Thus the induced parameter is \(R_{k-1,-(a+b)/2}\), corresponding to \(D_k\otimes\lvert\det\rvert^{-(a+b)/2}\). This also specifies the central-character twist; an unspecified power of the determinant would leave the dictionary ambiguous.

**Exercise 5.4 (hard).** Verify the weight-three epsilon factor, including the induction constant, and determine what happens when the real additive character is replaced by \(\psi_{\mathbb R}(-x)\).

**Solution.** The complex inducing character has angular exponent two, so its epsilon factor is \(i^2=-1\). The induction constant is \(i\), giving \(-i=i^3\). On the automorphic side \(k_{\pi/2}\) acts on the weight-three vector by \(i^3=-i\), which is the constant in the local functional equation. Under \(\psi\mapsto\psi_{-1}\), the two-dimensional change-of-character formula multiplies epsilon by the determinant evaluated at \(-1\), since \(\lvert-1\rvert^{2(s-1/2)}=1\). This determinant is \((-1)^3=-1\); the new value is \(i\). The central character of \(D_3\) has the same value at \(-1\), so both sides change together.

## What this lesson does not prove

The real Weil-group classification is the prerequisite [Representations of Weil groups](https://kokunoyumeto.github.io/open-math-courses-public/courses/LG-GAL/representations-of-weil-groups.html), Theorem 5.1, with the parameter translation in Section 2.

Local class field theory and its ramification comparison are assumed; see [Milne CFT, Chapters I and III]. Tate's functional equation and the induction normalization of Weil epsilon factors are used in Section 4; see [Deligne 1973, §§3–5]. The classification of real admissible representations is the exact input [Jacquet–Langlands 1970, Theorem 5.11]; their Whittaker model and local functional equation are [Jacquet–Langlands 1970, §5 and Theorem 5.15]. The lesson proves the comparison of their labels and explicitly evaluates the factors.

For all \(n\), the archimedean local Langlands theorem gives a bijection between semisimple \(n\)-dimensional representations of \(W_{\mathbb R}\), respectively \(W_{\mathbb C}=\mathbb C^\times\), and irreducible admissible representations of \(\operatorname{GL}_n(\mathbb R)\), respectively \(\operatorname{GL}_n(\mathbb C)\). A real parameter decomposes into the one- and two-dimensional blocks of Proposition 2.1; the corresponding representation is their Langlands quotient. A complex parameter is a sum of characters, and the corresponding representation is the Langlands quotient of their normalized induction. The theorem preserves factors. This higher-rank statement is not proved here; see [Getz–Hahn 2022, §12.3].

## References

- [Getz–Hahn 2022] J. R. Getz and H. Hahn, [*An Introduction to Automorphic Representations, with a View toward Trace Formulae*](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), draft of 22 April 2022, §§12.1–12.3.
- [Jacquet–Langlands 1970] H. Jacquet and R. P. Langlands, [*Automorphic Forms on GL(2)*](https://publications.ias.edu/sites/default/files/Automorphic-forms-on-GL2.pdf), Lecture Notes in Mathematics 114, 1970, §5, Theorems 5.11 and 5.15 and Proposition 5.20.
- [Knapp 1994] A. W. Knapp, [*Local Langlands correspondence: the archimedean case*](https://www.math.stonybrook.edu/~aknapp/pdf-files/motives.pdf), in *Motives*, Proceedings of Symposia in Pure Mathematics 55, Part 2, 1994, 393–410, §§2–4.
- [Deligne 1973] P. Deligne, [*Les constantes des équations fonctionnelles des fonctions L*](https://publications.ias.edu/sites/default/files/Number20.pdf), in *Modular Functions of One Variable II*, Lecture Notes in Mathematics 349, Springer, 1973, 501–597, §§2–5.
- [Milne CFT] J. S. Milne, [*Class Field Theory*](https://www.jmilne.org/math/CourseNotes/CFT.pdf), course notes, Chapters I (Lubin–Tate theory and ramification) and III (local class field theory).
