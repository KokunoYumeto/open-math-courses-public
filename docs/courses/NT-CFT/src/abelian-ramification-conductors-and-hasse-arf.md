# Abelian ramification, conductors and Hasse–Arf

*Written by OpenAI GPT-6.1 Sol in Codex, Ultra effort, October 2026. Self-checked by the writing AI; no independent review is claimed. Public domain (CC0).*

The unit filtration of a local field measures abelian ramification exactly. Its integer levels become the upper ramification groups under reciprocity. We compute this first in a Lubin–Tate division field, where moving a uniformizer amounts to evaluating another division point, and then pass to every abelian quotient. The calculation controls the groups at real indices and proves that all their jumps are integers.

Fix a nonarchimedean local field \(K\), valuation ring \(\mathcal O\), uniformizer \(\pi\), maximal ideal \(\mathfrak p\), and residue field \(\mathbf F_q\). Put \(U^{(0)}=U=\mathcal O^\times\) and \(U^{(j)}=1+\mathfrak p^j\) for \(j\geq1\). The explicit symbol and local existence theorem are proved in [Explicit local reciprocity and the existence theorem](explicit-local-reciprocity-and-existence.md).

We use the actual written ramification prerequisites in [Ramification groups and the different of a local extension](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-CFT/proof-dependencies.html#NT-LOC-09), Proposition 1.1, equation (2.2) and Theorem 3.1, and [Herbrand's function and the upper numbering](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-CFT/proof-dependencies.html#NT-LOC-10), Proposition 1.1 and Theorem 3.1. In particular, the latter's quotient theorem was proved without Hasse–Arf; its reference to a planned proof of Hasse–Arf is fulfilled here and is not a hypothesis of our argument.


**Prerequisite proof availability.** The named results below identify specific programme lessons. The [prerequisite record](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-CFT/proof-dependencies.html#lesson-10) distinguishes published proofs, supplied owner texts awaiting publication, and missing full proofs. A record or external reference is not a supplied proof; arguments using an unavailable prerequisite retain that dependency.

## 1. Conventions at a jump

For a finite Galois extension \(L/K\), normalize \(v_L(L^\times)=\mathbf Z\) and put \(G=\operatorname{Gal}(L/K)\). Its motion number and lower groups are
\[
i_G(\sigma)=\min_{x\in\mathcal O_L}v_L(\sigma x-x),\qquad
G_j=\{\sigma:i_G(\sigma)\geq j+1\}.
\]
Identity has infinite motion number. Use the real-index convention
\[
G_t=G_{\lceil t\rceil}\quad(t\geq-1),\qquad
\phi(t)=\int_0^t\frac{|G_s|}{|G_0|}\,ds\quad(t\geq0).
\tag{1}
\]
On \([-1,0]\), put \(\phi(t)=t\). Let \(\psi=\phi^{-1}\), and \(G^v=G_{\psi(v)}\). Thus a group retains its value at a jump and decreases immediately afterward. The group \(G^0=G_0\) is inertia.

Herbrand's quotient theorem says that for \(H\triangleleft G\),
\[
(G/H)^v=G^vH/H\qquad(v\geq-1).
\tag{2}
\]
Hilbert's different formula is
\[
\delta_{L/K}:=v_L(\mathfrak D_{L/K})
       =\sum_{j\geq0}(|G_j|-1).
\tag{3}
\]
All sums of nonzero terms here are finite.

## 2. Motion in a Lubin–Tate field

Let \(L=K_{\pi,n}\), \(n\geq1\), and choose a primitive division point \(\lambda\) for \(f(X)=\pi X+X^q\). Lesson 8 proves that \(\lambda\) is a uniformizer and
\[
G\simeq(\mathcal O/\pi^n\mathcal O)^\times,\qquad
|G|=D_n=(q-1)q^{n-1}.
\]
Write \(\sigma_u(\lambda)=[u]_f(\lambda)\). This is the scalar-action coordinate; the reciprocity symbol of a unit \(u\) is \(\sigma_{u^{-1}}\).

For a nonidentity class, write \(u-1=\pi^k a\), where \(a\in U\) and \(0\leq k<n\). The formal group law has the form
\[
F_f(X,Y)=X+Y+XYB(X,Y),\qquad B\in\mathcal O[[X,Y]],
\]
because its restrictions to either axis are the identity. The scalar identities give
\[
\sigma_u(\lambda)-\lambda
 =[u-1]_f(\lambda)\bigl(1+\lambda B(\lambda,[u-1]_f(\lambda))\bigr).
\tag{4}
\]
The second factor is a unit. Moreover \([\pi^k]_f(\lambda)\) is primitive at level \(n-k\), hence is a uniformizer of \(K_{\pi,n-k}\). The relative ramification index from that field to \(L\) is \(q^k\). The series \([a]_f\) has unit linear coefficient and integral higher coefficients, so preserves the valuation of positive-valuation points. The uniformizer formula for motion therefore yields
\[
i_G(\sigma_u)=v_L(\sigma_u(\lambda)-\lambda)=q^k.
\tag{5}
\]

### Proposition 10.1. The Lubin–Tate upper filtration

For \(v>0\),
\[
G^v=\{\sigma_u:u\in U^{(\lceil v\rceil)}\},
\tag{6}
\]
where unit classes are taken modulo \(\pi^n\); a level at least \(n\) gives identity. For \(-1\leq v\leq0\), the group is \(G\).

**Proof.** Put \(b_k=q^k-1\), so \(b_0=0\). Formula (5) and the definition of \(G_j\) give
\[
G_t=\operatorname{image}(U^{(k)})
\quad\text{for }b_{k-1}<t\leq b_k,\quad 1\leq k<n.
\tag{7}
\]
Indeed, for the integer indices \(q^{k-1}\leq j\leq q^k-1\), the inequality \(q^{v_K(u-1)}\geq j+1\) is exactly \(v_K(u-1)\geq k\). The ceiling convention extends these intervals to (7). Beyond \(b_{n-1}\) the lower group is identity.

On the interval in (7), the group has order \(q^{n-k}\). Its index in \(G_0=G\) is \((q-1)q^{k-1}\), exactly the length \(b_k-b_{k-1}\). Thus every interval contributes 1 to the integral (1), giving
\[
\phi(b_k)=k,\qquad
\phi(t)=k-1+\frac{t-b_{k-1}}{(q-1)q^{k-1}}
\quad(b_{k-1}\leq t\leq b_k).
\tag{8}
\]
For \(t\geq b_{n-1}\), it is \(n-1+(t-b_{n-1})/D_n\). This latter formula covers all nonnegative \(t\) when \(n=1\).

The change of variable carries (7) to \(k-1<v\leq k\), proving (6) at every endpoint as well. Total ramification gives the full group at nonpositive indices. \(\square\)

The positive jumps are \(1,\ldots,n-1\). Zero is also a jump when \(q>2\), since the residue-unit quotient has order \(q-1\). When \(q=2\), \(U=U^{(1)}\), so zero is not a jump. In particular \(q=2,n=1\) gives a trivial extension.

## 3. Every abelian extension

### Theorem 10.2. Units and upper ramification

Let \(L/K\) be finite abelian, with Galois group \(G\). Then
\[
(U,L/K)=G^0,\qquad
(U^{(j)},L/K)=G^j\quad(j\geq1).
\tag{9}
\]
More precisely, at every real \(v>0\),
\[
G^v=(U^{(\lceil v\rceil)},L/K).
\tag{10}
\]
On the maximal abelian extension the corresponding upper group is the closure of the reciprocity image of the same unit group.

**Proof.** By Theorem 9.4, \(L\) lies in \(A=K_dK_{\pi,n}\) for some \(d,n\). Its Galois group is the product of the unramified group and the division-field group. The inertia group is the latter factor. The extension \(A/K_{\pi,n}\) is unramified, so the same primitive point \(\lambda\) is a uniformizer of \(A\), with the same normalized values on the division field.

The maximal unramified subfield of \(A/K\) is \(K_d\). Over it, the uniformizer formula for inertial motion applies to \(\lambda\), and (4)–(5) remain unchanged. Thus all nonnegative lower groups and the denominator \(|G_0|=D_n\) in Herbrand's integral are those of the division field. Proposition 10.1 gives their upper filtration, with trivial unramified coordinate. The explicit reciprocity law sends units to precisely these groups: inversion preserves each \(U^{(j)}\). This proves (9)–(10) for \(A/K\).

Restriction to \(L\) carries the symbol to its symbol on \(L\), and Herbrand's theorem (2) carries each real upper group onto that of \(L\). This proves the result for \(L/K\).

For the infinite assertion, the upper groups are the inverse limits of the finite upper groups, by Proposition 4.1 of the Herbrand lesson. On every finite collection of levels, their prescribed elements can be tested in the finite compositum, where (9)–(10) give surjectivity from the relevant unit group. Its image is therefore dense in the inverse-limit upper group. It is contained in that closed group, proving the closure statement. \(\square\)

### Corollary 10.3. Hasse–Arf

Every upper jump of a finite abelian extension of local fields is an integer.

**Proof.** Formula (10) makes the filtration constant on each \(k-1<v\leq k\). There can be no jump strictly between consecutive nonnegative integers. On \((-1,0]\) the group is inertia, also constant. The possible remaining jumps are at \(-1,0,1,\ldots\), all integers. \(\square\)

Abelianity is used through the containment in explicit class fields. It cannot be dropped: the splitting field of \(X^3-2\) over \(\mathbf Q_3\) has group \(S_3\) and positive upper jump \(1/2\), as computed with a uniformizer in Exercise 4 of the Herbrand lesson.

## 4. Conductors of fields and characters

For finite abelian \(L/K\), define its **conductor** to be \(\mathfrak f_{L/K}=\mathfrak p^c\), where
\[
c=\min\{j\geq0:U^{(j)}\subset N_{L/K}L^\times\}.
\tag{11}
\]
Deep units are norms by lesson 6, so the minimum exists. For a complex character \(\chi:G\to\mathbf C^\times\), put
\[
a(\chi)=\min\{j\geq0:\chi(G^j)=1\}.
\tag{12}
\]
These are integer conductor exponents; \(a(1)=0\).

### Proposition 10.4. Characterizations of the conductor

The exponent \(c\) is the least \(j\geq0\) for which \(G^j=1\), and
\[
c=0\ \Longleftrightarrow\ L/K\text{ is unramified},\qquad
c=\max_\chi a(\chi).
\tag{13}
\]
For a ramified character, \(a(\chi)\) is one plus its last upper jump; an unramified character has exponent zero.

**Proof.** Theorem 10.2 identifies the image of \(U^{(j)}\) with \(G^j\), and the norm group is the symbol kernel. This gives the first characterization. The condition \(G^0=1\) is trivial inertia, equivalently unramifiedness.

Characters separate elements of a finite abelian group. The finite character lemma in [Hilbert’s Theorem 90 and Kummer theory](hilberts-theorem-90-and-kummer-theory.md), section 4, proves this explicitly: choose a nontrivial character on the cyclic subgroup generated by a nonidentity element and extend it one finite cyclic enlargement at a time. Consequently \(G^j=1\) exactly when every character is trivial on it. Taking the least \(j\) gives the maximum in (13).

If \(a(\chi)=c_\chi\geq1\), the character is nontrivial on \(G^{c_\chi-1}\) and trivial on \(G^{c_\chi}\). The real-index formula (10) makes it nontrivial through \(v=c_\chi-1\) and trivial at all \(v>c_\chi-1\). Its last upper jump is therefore \(c_\chi-1\). If \(a(\chi)=0\), it is trivial on inertia and has no nonnegative ramification jump. \(\square\)

For the full cyclotomic extension \(\mathbf Q_p(\zeta_{p^n})/\mathbf Q_p\), its norm group is \(p^{\mathbf Z}(1+p^n\mathbf Z_p)\). The conductor exponent is \(n\), except for \(p=2,n=1\), when the extension is trivial and its exponent is zero.

## 5. Discriminants as sums of conductors

Let \(\mathfrak d_{L/K}\) denote the discriminant ideal, defined by the determinant of the trace matrix in an integral \(\mathcal O_K\)-basis. We first record explicitly its relation to the different:
\[
v_K(\mathfrak d_{L/K})=f(L/K)\,\delta_{L/K}.
\tag{14}
\]
Indeed, if \(T\) is that invertible trace matrix, the trace dual is \(T^{-1}\mathcal O_K^{[L:K]}\), while the integral lattice is \(\mathcal O_K^{[L:K]}\). The quotient of the former by the latter has length \(v_K(\det T)\). To see the length assertion over a DVR, choose an entry of \(T\) of smallest valuation, move it to the first position, and use integral row and column operations to eliminate its row and column: it divides every entry. Repeat on the smaller matrix. This gives a diagonal matrix up to invertible integral operations; the quotient length and determinant valuation are both the sum of its diagonal valuations.

By the definition of the different, the trace dual is \(\mathfrak P_L^{-\delta}\). Its quotient by \(\mathcal O_L\) has \(\delta\) successive quotients isomorphic to \(\kappa_L\), each of length \(f(L/K)\) over \(\mathcal O_K\). This proves (14) directly, including its residue-degree factor.

### Theorem 10.5. The local conductor–discriminant formula

For finite abelian \(L/K\),
\[
v_K(\mathfrak d_{L/K})=\sum_{\chi\in\widehat G}a(\chi).
\tag{15}
\]

**Proof.** Put \(\epsilon_\chi(H)=1\) if \(\chi\) is nontrivial on \(H\), and 0 otherwise. Proposition 10.4 and Hasse–Arf give
\[
a(\chi)=\epsilon_\chi(G_0)
           +\int_0^\infty\epsilon_\chi(G^v)\,dv.
\]
For a ramified character the integral is the length of the interval from zero to its last upper jump, namely \(a(\chi)-1\); for an unramified character both terms vanish. Substitute \(v=\phi(t)\) and use (1), whose ceiling convention makes \(G_t=G_j\) on \(j-1<t\leq j\). We get
\[
a(\chi)=\sum_{j\geq0}
          \frac{|G_j|}{|G_0|}\epsilon_\chi(G_j).
\tag{16}
\]
The \(j=0\) term has weight 1.

A finite abelian group \(B\) has exactly \(|B|\) complex characters. One proof is induction: restriction to a cyclic subgroup \(C\) is onto by the extension argument above, its kernel is the character group of \(B/C\), and \(C\) has \(|C|\) characters. In particular, the number of characters of \(G\) trivial on \(G_j\) is \(|G/G_j|\). Summing (16) thus gives
\[
\begin{aligned}
\sum_\chi a(\chi)
 &=\sum_{j\geq0}\frac{|G_j|}{|G_0|}
                \left(|G|-\frac{|G|}{|G_j|}\right)\\
 &=\frac{|G|}{|G_0|}\sum_{j\geq0}(|G_j|-1)\\
 &=f(L/K)\delta_{L/K}
 =v_K(\mathfrak d_{L/K}),
\end{aligned}
\]
by (3), inertia order \(|G_0|=e(L/K)\), and (14). \(\square\)

For \(\mathbf Q_3(\zeta_9)\), the group is cyclic of order 6. Of its six characters, one is trivial, one is a nontrivial tame character, and four are nontrivial on the order-three wild subgroup. Their exponents are \(0,1,2,2,2,2\), summing to 9.

## 6. Exercises and complete solutions

### Exercise 1 — easy

Compute the conductor of \(\mathbf Q_p(\zeta_{p^n})/\mathbf Q_p\) from its norm group.

**Solution.** The norm group is \(p^{\mathbf Z}U^{(n)}\), so \(U^{(n)}\) is contained in it. If \(n\geq2\), the element \(1+p^{n-1}\) belongs to \(U^{(n-1)}\) and not to \(U^{(n)}\), so the least level is \(n\). If \(n=1,p>2\), a unit with residue different from 1 shows that \(U\) is not contained, while \(U^{(1)}\) is; the exponent is 1. If \(n=1,p=2\), all units already lie in \(U^{(1)}\), the norm group is the entire multiplicative group, and the exponent is 0. Thus the conductor ideal is \(p^n\mathbf Z_p\) except in this trivial case, when it is \(\mathbf Z_2\).

### Exercise 2 — medium

Compute the norm groups and conductors of all quadratic extensions of \(\mathbf Q_2\).

**Solution.** First, an odd \(2\)-adic unit is a square exactly when it is \(1\) modulo 8. Necessity follows by squaring odd residues. For sufficiency, start a root modulo 8 and inductively lift a root \(z\) modulo \(2^r\), \(r\geq3\): replacing \(z\) by \(z+2^{r-1}\) changes its square by \(2^rz\) modulo \(2^{r+1}\), toggling the required next bit. These compatible corrections converge and square to the given unit. Valuation parity and the four odd residues modulo 8 therefore give eight square classes, with the seven nonsquare representatives in the following table. For \(d\) in its first column put \(L_d=\mathbf Q_2(\sqrt d)\).

| \(d\) | Norm group \(N_{L_d/\mathbf Q_2}L_d^\times\) | Conductor exponent |
|---|---|---:|
| \(5\) | \(2^{2\mathbf Z}\mathbf Z_2^\times\) | 0 |
| \(-1\) | \(2^{\mathbf Z}(1+4\mathbf Z_2)\) | 2 |
| \(-5\) | \(6^{\mathbf Z}(1+4\mathbf Z_2)\) | 2 |
| \(2\) | \((-2)^{\mathbf Z}\{u\mid u\bmod8\in\{1,7\}\}\) | 3 |
| \(-2\) | \(2^{\mathbf Z}\{u\mid u\bmod8\in\{1,3\}\}\) | 3 |
| \(10\) | \((-10)^{\mathbf Z}\{u\mid u\bmod8\in\{1,7\}\}\) | 3 |
| \(-10\) | \(10^{\mathbf Z}\{u\mid u\bmod8\in\{1,3\}\}\) | 3 |

In the last four rows the displayed \(u\) ranges over \(\mathbf Z_2^\times\). We justify every row. The field \(L_5\) is the unique unramified quadratic extension, as proved in the unramified-extension lesson, so its norm group is the first row. The others are ramified: they are distinct quadratic fields by the Kummer correspondence in lesson 3 and the distinct square classes, and cannot be that unique unramified field.

For any ramified quadratic field, norm valuations are all integers, since \(v_2(Nx)=f\,v_L(x)=v_L(x)\). Finite reciprocity gives norm index 2; adjusting valuations by a norm shows that its unit norm subgroup has index 2 in \(\mathbf Z_2^\times\).

For \(d=-1,-5\), a norm is \(x^2+cy^2\) with \(c=1,5\). If the minimum of \(v_2(x),v_2(y)\) is a negative integer \(r\), factor out \(2^{2r}\). The remaining norm has valuation 0 when just one scaled coordinate is odd, and valuation 1 when both are odd, since \(1+c\equiv2\pmod4\). It cannot give a unit. Thus a unit norm has integral coordinates, exactly one odd, and is 1 modulo 4. This residue condition has index 2, so the preceding index argument proves that all \(1+4\mathbf Z_2\) are unit norms. The elements \(1+i\) and \(1+\sqrt{-5}\) have norms 2 and 6, giving the two full norm groups.

For \(d=2\varepsilon\), \(\varepsilon\) odd, the terms in \(x^2-2\varepsilon y^2\) have valuations \(2v_2(x)\) and \(1+2v_2(y)\), which are distinct. A unit norm requires \(x\) odd and \(y\) integral. Modulo 8 its residue is 1 if \(y\) is even, and \(1-2\varepsilon\) if \(y\) is odd. For \(\varepsilon=1,5\) these are \(\{1,7\}\), and for \(\varepsilon=-1,-5\) they are \(\{1,3\}\). Each inverse image is an index-two subgroup of the unit group, so is the exact unit norm subgroup. The norm of \(\sqrt d\) is \(-d\), with valuation 1, supplying each displayed generator.

Finally \(U^{(1)}=U\) over \(\mathbf Q_2\). The odd ramified rows contain \(U^{(2)}\), but not all units, so have exponent 2. The even rows contain \(U^{(3)}\) and exclude the unit 5 in \(U^{(2)}\), so have exponent 3. The unramified row has exponent 0.

These also equal the discriminant exponents. For the odd ramified rows, \(1+\sqrt d\) is a uniformizer, and integral uniformizer generation gives \(\mathcal O_{L_d}=\mathbf Z_2[\sqrt d]\). For the even rows, \(X^2-d\) is Eisenstein and gives the same integral basis \(1,\sqrt d\). Its trace matrix is diagonal with entries \(2,2d\), so its discriminant is \(4d\), of valuation 2 for the odd rows and 3 for the even rows. The unramified different, hence discriminant, is trivial by (3) and (14). Theorem 10.5 gives the same values from the sole nontrivial character.

### Exercise 3 — medium

Verify the conductor–discriminant formula for \(\mathbf Q_3(\zeta_9)\).

**Solution.** Its group has order 6, inertia is the whole group, and the first upper group has order 3; the second is identity. Exactly two characters are trivial on that order-three subgroup. They have exponents 0 and 1. The other four have exponent 2, so their total is 9.

Independently (5) gives lower groups of orders \(6,3,3\) at indices \(0,1,2\), then identity. Hilbert's formula yields \(\delta=(6-1)+(3-1)+(3-1)=9\). The extension is totally ramified, so \(f=1\), and (14) gives discriminant exponent 9. This agrees with the character sum.

### Exercise 4 — hard

Deduce Hasse–Arf for every finite abelian extension using the unit-filtration theorem, including real indices.

**Solution.** Theorem 10.2 proves that for every real \(v>0\) the group is the image of \(U^{(\lceil v\rceil)}\). If \(v\) lies strictly between consecutive integers, choose \(\epsilon>0\) small enough that \(v+\epsilon\) remains in the same interval. Their ceilings, and hence their groups, agree, so \(v\) cannot be a jump. At a positive integer the group may decrease immediately afterward; these are precisely the permitted locations. The filtration on \((-1,0]\) is constantly inertia, leaving only the integer locations \(-1\) and 0 there. This proves the assertion for all jumps.

The real-index formula comes from the explicit Lubin–Tate rescaling and Herbrand's quotient theorem, both proved before invoking Hasse–Arf. Thus there is no circular use of integral jumps in obtaining it.

## Editable edition

The reading edition provides the complete LaTeX source of this lesson, the cumulative course LaTeX and the editable source ZIP. The archive contains all twenty-four Markdown lessons, complete LaTeX bodies, original diagrams, metadata and reproduction instructions.

## References

The division-point motion calculation determines all real-index ramification groups. The quotient filtration gives Hasse–Arf for every finite abelian local extension. The conductor, different and character-sum arguments retain their exact local-field prerequisites.

- [Teruyoshi Yoshida, Local class field theory via Lubin–Tate theory, arXiv:math/0606108v2](https://arxiv.org/abs/math/0606108v2).
- [Kiran S. Kedlaya, Notes on class field theory, author-hosted HTML edition](https://kskedlaya.org/cft/sec_abstractcft1.html).

The [proof guide](../FREE_PROOFS.md) gives the lesson sequence and the exact prerequisite record. External references accompany the written arguments.
