# Newvectors, conductors and the passage to classical newforms

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Author self-check complete. Public domain (CC0).*

A representation can have many vectors at a given level, but its first nonzero level has exactly one line. Every higher-level fixed vector comes from translating this line. We prove this statement in the Kirillov model, compute the conductors of principal and special representations, and prove that a supercuspidal conductor is at least two. We then give the precise global argument that turns these local lines into classical newforms.

The local proofs use Lesson 7, especially its Theorem 2.3, coefficient identity (2.9), classification Theorem 6.1 and function-space Proposition 6.2. Normalized induction and exact compact averaging are from Lesson 6 and Lesson 5. The global argument in Section 5 uses the proved restricted tensor theorem of Lesson 12, global Whittaker factorization of Lesson 14, and multiplicity-one results of Lesson 15, with exact locators below. Those later results use the local part of this lesson, rather than its classical conclusions, so the proof order is local newvectors, global Whittaker and multiplicity one, then the classical decomposition.

Throughout the local argument, \(F\) is a nonarchimedean local field, \(\mathcal O\) its integers, \(\mathfrak p=\varpi\mathcal O\), and \(q=|\mathcal O/\mathfrak p|\). Write
\[
G=\mathrm{GL}_2(F),\quad K=\mathrm{GL}_2(\mathcal O),\quad
U=\mathcal O^\times,\quad |{\varpi}|=q^{-1},
\]
\[
d(t)=\begin{pmatrix}t&0\\ 0&1\end{pmatrix},\quad
n(x)=\begin{pmatrix}1&x\\ 0&1\end{pmatrix},\quad
\bar n(y)=\begin{pmatrix}1&0\\ y&1\end{pmatrix},\quad
w_0=\begin{pmatrix}0&1\\ -1&0\end{pmatrix}.
\]
Choose \(\psi\) with conductor \(\mathcal O\): it is trivial on \(\mathcal O\) and nontrivial on \(\varpi^{-1}\mathcal O\). An arbitrary nontrivial character can be brought to this convention by rescaling its argument.

Let \(\pi\) be smooth irreducible and infinite-dimensional, with central character \(\omega\). In its scalar Kirillov model,
\[
(\pi(d(a))\xi)(t)=\xi(ta),\qquad
(\pi(n(x))\xi)(t)=\psi(tx)\xi(t),\qquad
\pi(zI)\xi=\omega(z)\xi.
\tag{0.1}
\]
Put \(W=\pi(w_0)\). Then \(W^2=\omega(-1)\). Every compact locally constant function on \(F^\times\) belongs to this model.

## 1. What the level group asks of a function

For \(n\geq1\), define
\[
K_0(n)=\left\{\begin{pmatrix}a&b\\ c&d\end{pmatrix}\in K:
c\in\mathfrak p^n\right\},\qquad
K_1(n)=\{k\in K_0(n):d\equiv1\pmod{\mathfrak p^n}\}.
\tag{1.1}
\]
Set \(K_0(0)=K_1(0)=K\), and \(V_n=V^{K_1(n)}\). For a smooth character \(\mu:F^\times\to\mathbb C^\times\), its conductor exponent is
\[
a(\mu)=0\quad\text{if }\mu|_U=1;
\]
otherwise \(a(\mu)\) is the least \(n\geq1\) with \(\mu|_{1+\mathfrak p^n}=1\). The separate definition at zero matters: \(1+\mathcal O\) is not a multiplicative unit subgroup.

A nonzero \(V_n\) forces \(a(\omega)\leq n\), since its central scalars include \(1+\mathfrak p^n\), or all of \(U\) at \(n=0\). When \(n\geq1\) and \(n\geq a(\omega)\),
\[
V_n=\{v:\pi(k)v=\omega(d_k)v\text{ for all }k\in K_0(n)\}.
\tag{1.2}
\]
Indeed \(d_k\in U\), and \(d_k^{-1}k\in K_1(n)\). Conversely \(\omega(d_k)=1\) on \(K_1(n)\). Thus the relevant \(K_0\)-space has a specified character; it is the ordinary fixed space only when \(\omega|_U=1\).

**Lemma 1.1 — support and the lower root.** For \(n\geq1\), \(n\geq a(\omega)\), a Kirillov function represents a vector of \(V_n\) exactly when
\[
\operatorname{supp}\xi\subset\mathcal O\cap F^\times,\qquad
\xi(tu)=\xi(t)\ (u\in U),\qquad
\operatorname{supp}W\xi\subset\varpi^{-n}\mathcal O\cap F^\times.
\tag{1.3}
\]
For \(n=0\), the same conditions describe \(V_0\) when \(\omega|_U=1\).

**Proof.** The first condition is invariance under \(n(\mathcal O)\), by the annihilator of \(\mathcal O\) for \(\psi\). The second is invariance under \(d(U)\). Since
\(\bar n(y)=w_0n(-y)w_0^{-1}\), the third is invariance under \(\bar n(\mathfrak p^n)\); \(W^{-1}\) is a nonzero scalar times \(W\).

For \(n\geq1\), every \(k\in K_0(n)\) has \(d\in U\) and factors as
\[
k=n(b/d)\operatorname{diag}(\det(k)/d,d)\bar n(c/d).
\tag{1.4}
\]
The indicated upper and lower groups and unit diagonals therefore generate \(K_0(n)\). The diagonal action on a unit-invariant function is precisely \(\omega(d)\). This proves (1.2). At \(n=0\), upper and lower integral unipotents generate \(\mathrm{SL}_2(\mathcal O)\), and adjoining \(d(U)\) generates \(K\). The central unit character is trivial. \(\square\)

We will also need the conditions in (1.3) when the putative central conductor is too large. The elementary identity
\[
n(u)\bar n(v)=
\bar n\!\left(\frac v{1+uv}\right)
\operatorname{diag}(1+uv,(1+uv)^{-1})
n\!\left(\frac u{1+uv}\right)
\tag{1.5}
\]
shows that a vector fixed by \(n(\mathcal O)\), \(\bar n(\mathfrak p^n)\) and \(d(U)\) must satisfy \(\omega(s)=1\) for \(s\in1+\mathfrak p^n\), when \(n\geq1\). Take \(u=1,v=s-1\); the diagonal in (1.5) acts by \(\omega(s^{-1})\). At \(n=0\), take \(u=s-1,v=1\) for any \(s\in U\). Hence these conditions force the vector to be zero if \(n<a(\omega)\).

One further boundary case will stop the level descent. If a vector is fixed by \(n(\mathcal O)\) and \(\bar n(\varpi^{-1}\mathcal O)\), (1.5) with \(u=1,v=\varpi^{-1}-1\) makes it fixed by \(\operatorname{diag}(\varpi^{-1},\varpi)\). Its conjugations expand the two root subgroups to all of \(F\). The vector is therefore fixed by \(\mathrm{SL}_2(F)\). The space of such vectors is \(G\)-stable, since \(\mathrm{SL}_2(F)\) is normal. If nonzero, irreducibility makes the whole representation factor through the determinant; Lesson 5, Proposition 6.2, then makes it one-dimensional. Our infinite-dimensional representation has no such vector.

## 2. The first level and all its translates

**Theorem 2.1 — the newvector dimension theorem.** There is a least integer \(c=c(\pi)\geq0\) such that \(V_c\ne0\). For every \(n\geq0\),
\[
\dim V_n=\max(0,n-c+1).
\tag{2.1}
\]
There is a unique vector \(v_c\in V_c\) whose Kirillov function takes the value one on \(U\). For \(n\geq c\), a basis of \(V_n\) is
\[
v_c,\ \pi(d(\varpi^{-1}))v_c,\ \ldots,\
\pi(d(\varpi^{-(n-c)}))v_c.
\tag{2.2}
\]
We call \(c\) the conductor exponent and \(v_c\) the normalized newvector.

**Proof of existence.** The compact function \(1_U\) is in the model. It is fixed by \(n(\mathcal O)\) and \(d(U)\). Its smoothness makes it fixed by \(\bar n(\mathfrak p^n)\) for sufficiently large \(n\). Increase \(n\) to be at least \(a(\omega)\). Lemma 1.1 puts this nonzero vector in \(V_n\).

**Proof of the dimension and basis.** Restriction to \(U\) is a linear map
\[
r_n:V_n\longrightarrow\mathbb C,
\]
because all functions in \(V_n\) are constant there. Its kernel has an exact description:
\[
\ker r_n=\pi(d(\varpi^{-1}))V_{n-1},
\qquad V_{-1}:=0.
\tag{2.3}
\]
To prove it, let \(\xi\in\ker r_n\). Upper integral invariance and unit invariance make it vanish outside \(\varpi\mathcal O\). The shifted function
\(\xi'(t)=\xi(\varpi t)\) is supported in \(\mathcal O\), remains unit-invariant, and is fixed by \(\bar n(\mathfrak p^{n-1})\):
\[
d(\varpi)^{-1}\bar n(y)d(\varpi)=\bar n(\varpi y).
\]
Its upper integral invariance follows from its support; it need not follow from conjugating the original upper group.

If \(n-1\geq a(\omega)\), Lemma 1.1 gives \(\xi'\in V_{n-1}\), including its \(n-1=0\) case. If \(0\leq n-1<a(\omega)\), identity (1.5) forces \(\xi'=0\). If \(n=0\), the preceding boundary argument again forces \(\xi'=0\). This proves one inclusion in (2.3). For the converse, shift a function of \(V_{n-1}\) by \(\varpi^{-1}\). Its support enters \(\varpi\mathcal O\), and its lower level increases by one. Lemma 1.1 gives a vector of \(V_n\) which vanishes on \(U\).

At the least nonzero level \(c\), (2.3) makes \(r_c\) injective. Its target is one-dimensional, so \(V_c\) is a line and \(r_c\) is nonzero. Normalize its value to one. Repeated use of (2.3) gives
\(\dim V_n\leq n-c+1\). The \(j\)-th vector of (2.2) is supported in \(\varpi^j\mathcal O\) and takes value one at \(\varpi^j\). Evaluations at \(1,\varpi,\ldots,\varpi^{n-c}\) give a triangular matrix with diagonal entries one. The vectors are independent, lie in \(V_n\), and reach the upper bound. \(\square\)

This proof uses smoothness and the full Kirillov model, including its compact functions. It does not quote the newvector theorem. Admissibility already follows from the local theory, but the argument itself also computes these fixed-space dimensions.

Deligne, §2.2, Théorème 2.2.6, provides a second proof in a different convention: his unipotent is lower triangular, his torus restriction uses \(\operatorname{diag}(1,t)\), and his level is on the upper-right entry. Conjugation by \(w_0\), together with \(\psi(x)\mapsto\psi(-x)\), gives (1.1)–(1.2). In particular his diagonal-character condition must be transferred as well as his level condition.

## 3. Principal series and special conductors

Put
\[
U_0=U,\qquad U_j=1+\mathfrak p^j\quad(j\geq1).
\]
Let \(I(\mu_1,\mu_2)\) denote normalized induction, with left \(B\)-transformation
\(|a/d|^{1/2}\mu_1(a)\mu_2(d)\). This notation includes the reducible exceptional parameters.

**Lemma 3.1 — the compact induction count.** For all \(n\geq0\),
\[
\dim I(\mu_1,\mu_2)^{K_1(n)}
=\max(0,n-a(\mu_1)-a(\mu_2)+1).
\tag{3.1}
\]

**Proof.** The Iwasawa decomposition \(G=BK\) identifies the compact restriction with functions on \(K\) transforming under \(B(\mathcal O)\) by
\(\mu_1(a)\mu_2(d)\); the modulus is one there. At \(n\geq1\),
\(K/K_1(n)\) is the set of primitive rows modulo \(\mathfrak p^n\), via \(k\mapsto(0,1)k^{-1}\). A row is primitive if at least one entry is a unit. The right action of \(B(\mathcal O)\) has \(n+1\) orbits, indexed by the valuation \(i\in\{0,\ldots,n\}\) of the first entry, capped at \(n\). A unit first entry permits eliminating the second; otherwise the second is a unit, and both unit factors can be normalized. Representatives for \(i<n\) are \(r_i=\bar n(\varpi^i)\); the last representative is \(r_n=1\).

For \(i<n\), writing \(x=\varpi^i\) gives
\[
r_i^{-1}\begin{pmatrix}a&b\\0&d\end{pmatrix}r_i
=\begin{pmatrix}a+bx&b\\x(d-a)-bx^2&d-bx\end{pmatrix}.
\tag{3.2}
\]
It lies in \(K_1(n)\) precisely when
\[
d-bx\equiv1\pmod{\mathfrak p^n},\qquad
a\equiv1\pmod{\mathfrak p^{n-i}}.
\]
The allowed pairs of diagonal entries are exactly
\(a\in U_{n-i},d\in U_i\). Every such pair is realized by taking \(b=(d-1)/x\); the congruence for the lower-left entry then follows. For \(i=0\), \(U_i=U\), as required. At the last representative the stabilizer has \(a\in U,d\in U_n\), giving the same description with \(i=n\).

A transforming function on one orbit has one free value exactly when its character is trivial on this stabilizer; otherwise its value is zero. Thus the orbit contributes one precisely if
\[
a(\mu_2)\leq i\leq n-a(\mu_1).
\tag{3.3}
\]
Counting these integers proves (3.1). At \(n=0\), there is one orbit and its stabilizer is \(B(\mathcal O)\); it contributes one exactly when both characters are unramified. This is again (3.1). \(\square\)

**Theorem 3.2 — the conductor formulas.** For an irreducible principal series and a special representation,
\[
c(I(\mu_1,\mu_2))=a(\mu_1)+a(\mu_2),\qquad
c(\mathrm{St}_\chi)=
\begin{cases}
1&a(\chi)=0,\\
2a(\chi)&a(\chi)>0.
\end{cases}
\tag{3.4}
\]
Every supercuspidal satisfies \(c(\pi)\geq2\); this last assertion is proved in Theorem 4.3 below.

**Proof of (3.4).** The first formula follows directly from Lemma 3.1. For the second, use the exceptional induction sequences of Lessons 6–7:
\[
0\longrightarrow\mathrm{St}_\chi
\longrightarrow I(\chi|\ |^{1/2},\chi|\ |^{-1/2})
\longrightarrow D_\chi\longrightarrow0,
\quad D_\chi(g)=\chi(\det g).
\tag{3.5}
\]
Taking compact fixed spaces is exact by averaging. If \(\chi\) is unramified, \(D_\chi^{K_1(n)}\) has dimension one at every \(n\), whereas the induced fixed space has dimension \(n+1\). Hence the special fixed space has dimension \(n\), with first level one. If \(\chi\) is ramified, \(D_\chi^{K_1(n)}=0\) for every \(n\), because \(d(U)\subset K_1(n)\). Both inducing characters have conductor \(a(\chi)\), so (3.1) gives the second formula. \(\square\)

For completeness, a finite-dimensional irreducible is \(D_\chi\). Its \(K_1(n)\)-fixed space is one-dimensional at all levels if \(\chi\) is unramified, and zero at all levels if \(\chi\) is ramified. The conductor defined by Theorem 2.1 is an invariant of the infinite-dimensional, hence generic, representations; its dimension formula is not asserted for \(D_\chi\).

## 4. The actual newfunctions and the supercuspidal bound

**Lemma 4.1 — the one-step operator.** For \(n\geq1\), the operator
\[
\mathcal U=E_{\mathcal O}\pi(d(\varpi))
=\frac1q\sum_{b\in\mathcal O/\mathfrak p}\pi(n(b)d(\varpi))
\tag{4.1}
\]
preserves \(V_n\). It also preserves the \(K_0(n)\)-space with character \(k\mapsto\omega(a_k)\). On any function fixed by \(n(\mathcal O)\),
\[
(\mathcal U\xi)(t)=1_{\mathcal O}(t)\xi(\varpi t).
\tag{4.2}
\]

**Proof.** The intersection \(K_1(n)\cap d(\varpi)K_1(n)d(\varpi)^{-1}\) has upper-right entry in \(\mathfrak p\), of index \(q\) in \(K_1(n)\). Its coset representatives are \(n(b)\). This gives the double-coset operator (4.1), which preserves fixed vectors. The same intersection calculation holds for \(K_0(n)\); conjugation keeps its two diagonal entries. Consequently either diagonal character is compatible on the intersection, and the same coset sum preserves its character space.

Averaging \(\psi(tx)\) over \(x\in\mathcal O\) gives \(1_{\mathcal O}(t)\), proving (4.2). To replace the integral by the finite sum, \(\pi(d(\varpi))v\) is fixed by \(n(\mathfrak p)\), since \(d(\varpi)^{-1}n(x)d(\varpi)=n(x/\varpi)\). \(\square\)

When \(c\geq1\), \(\mathcal U\) acts on the newvector line by a scalar \(A\). Thus its normalized function has the form
\[
\xi_c(\varpi^m u)=
\begin{cases}
A^m&m\geq0,\ u\in U,\\
0&m<0.
\end{cases}
\tag{4.3}
\]
Here \(A^0=1\), including when \(A=0\). If the function is compact away from zero, (4.3) forces \(A=0\).

Lesson 7, Proposition 6.2, determines \(A\) from the germ. If precisely one principal-series character is unramified, then
\(A=q^{-1/2}\mu_{\rm unram}(\varpi)\). If both are ramified, unit invariance eliminates both germ characters, so \(\xi_c=1_U\). In the repeated-parameter ramified case it also eliminates the valuation-times-character germ. For \(\mathrm{St}_\chi\), an unramified \(\chi\) gives \(A=q^{-1}\chi(\varpi)\); a ramified \(\chi\) gives \(\xi_c=1_U\). For supercuspidals the whole model is compact away from zero, so \(\xi_c=1_U\) whenever \(c\geq1\).

For either of the cases with a unit-invariant nonzero germ, the newfunction really has a nonzero germ. Indeed choose a unit-invariant function with that germ and support in \(\mathcal O\). Smoothness puts it in some \(V_n\). If the newfunction were compact away from zero, every shift in its oldbasis (2.2) would be compact as well and could not span this function. Thus (4.3) has the nonzero-germ scalar asserted above.

**Theorem 4.2 — the spherical newfunction.** Suppose \(\mu_1,\mu_2\) are unramified and their normalized induction is irreducible. Write \(\alpha=\mu_1(\varpi),\beta=\mu_2(\varpi)\). The normalized \(K\)-fixed vector has function
\[
\xi_0(\varpi^m u)=
\begin{cases}
q^{-m/2}\displaystyle\sum_{i+j=m}\alpha^i\beta^j&m\geq0,\\
0&m<0.
\end{cases}
\tag{4.4}
\]
In particular equal parameters give \(q^{-m/2}(m+1)\alpha^m\).

**Proof.** The double coset \(Kd(\varpi)K\) has \(q+1\) right cosets:
\(n(b)d(\varpi)\), \(b\bmod\mathfrak p\), and \(\operatorname{diag}(1,\varpi)\). One way to check the count is that its stabilizer in \(K\), modulo \(\mathfrak p\), fixes a line in the two-dimensional residue space; the lines are \(\mathbb P^1(\mathbb F_q)\). The displayed matrices give all the lines.

The corresponding unnormalized operator \(\mathcal T\) has eigenvalue
\(q^{1/2}(\alpha+\beta)\). Indeed evaluate the spherical induced section, normalized to one at \(1\): each of the first \(q\) upper triangular representatives contributes \(q^{-1/2}\alpha\), and the last contributes \(q^{1/2}\beta\). On its Kirillov function, with \(\xi_m=\xi_0(\varpi^m)\) and \(z=\omega(\varpi)=\alpha\beta\),
\[
q\xi_{m+1}+z\xi_{m-1}
=q^{1/2}(\alpha+\beta)\xi_m\quad(m\geq0),
\qquad \xi_{-1}=0,\quad\xi_0=1.
\tag{4.5}
\]
The first term is the upper coset sum; the last coset acts as \(z\xi(t/\varpi)\). The polynomials
\(h_m=\sum_{i+j=m}\alpha^i\beta^j\) satisfy
\(h_m=(\alpha+\beta)h_{m-1}-\alpha\beta h_{m-2}\),
with \(h_0=1,h_{-1}=0\). Substitution in (4.5) proves (4.4) by induction. \(\square\)

**Theorem 4.3 — a supercuspidal cannot have conductor zero or one.**

**Proof at zero.** If a supercuspidal had \(c=0\), its normalized \(K\)-fixed function would be compact away from zero. The operator \(\mathcal T\) preserves its one-dimensional fixed line and satisfies the left side of (4.5), with some scalar eigenvalue and \(z\ne0\). Let \(M\geq0\) be the largest valuation at which its function is nonzero. At \(m=M+1\), the recurrence reads \(z\xi_M=0\), a contradiction.

**Proof at one.** Put \(\epsilon=\omega|_U,z=\omega(\varpi)\). Suppose \(c=1\). Define
\[
Y_1=\{v:\pi(k)v=\omega(a_k)v,\ k\in K_0(1)\},\qquad
w_1=w_0d(\varpi).
\]
Conjugation by \(w_1\) normalizes \(K_0(1)\) and exchanges its diagonal entries:
\[
w_1\begin{pmatrix}a&b\\c&d\end{pmatrix}w_1^{-1}
=\begin{pmatrix}d&-c/\varpi\\-\varpi b&a\end{pmatrix}.
\]
Hence \(\pi(w_1)\) identifies \(V_1\) and \(Y_1\), so both are lines. The former has function \(1_U\). A function in \(Y_1\) is supported in \(\mathcal O\), transforms under \(d(u)\) by \(\epsilon(u)\), and satisfies the recurrence (4.2) with a scalar. Compact support forces that scalar to be zero and its value on \(U\) to be nonzero. Thus \(Y_1\) has normalized function \(\epsilon\,1_U\).

Since \(w_1=\varpi I\,d(\varpi^{-1})w_0\), it follows that \(W1_U\) is a nonzero multiple of \(\epsilon(t/\varpi^{-1})\) on the single shell \(v_F(t)=-1\), and zero on every other shell. Likewise \(W(\epsilon1_U)\) has only that shell and is unit-invariant. In Lesson 7's coefficient notation this says
\[
C_r^{\epsilon^{-1}}=C_r^1=0\ (r\ne-1),\qquad
z C_{-1}^1C_{-1}^{\epsilon^{-1}}=\epsilon(-1).
\tag{4.6}
\]
The product follows by applying \(W^2\) to \(1_U\).

Now use the already proved identity (2.9) of Lesson 7 with
\(\ell=0,n=p=0,\alpha=1,\widetilde\alpha=\epsilon^{-1}\).
Its left side is
\[
S_{0,0}^{1,\epsilon^{-1}}
=\sum_\sigma
\eta(\sigma^{-1},1)\eta(\sigma^{-1}\epsilon^{-1},1)C_0^\sigma=0.
\]
Indeed the first factor vanishes unless \(\sigma=1\); the second then vanishes unless \(\epsilon=1\); and in that remaining case \(C_0^1=0\). All terms indexed by \(r\leq-2\) on the right vanish by (4.6). The right side is therefore
\[
\epsilon(-1)+\frac{z}{q^{-1}-1}
 C_{-1}^1C_{-1}^{\epsilon^{-1}}
=-\frac{\epsilon(-1)}{q-1}\ne0.
\]
This contradiction proves the assertion. It uses the finite Weyl coefficient calculation of the preceding lesson, with its signs and averaging normalization intact. \(\square\)

Combining the results gives the following useful description.

| Representation | Conductor | Normalized function at \(\varpi^m u\), \(m\geq0\) |
|---|---:|---|
| Unramified irreducible principal series | \(0\) | \(q^{-m/2}\sum_{i+j=m}\alpha^i\beta^j\) |
| Principal series, one unramified character | \(a(\mu_{\rm ram})\) | \((q^{-1/2}\mu_{\rm unram}(\varpi))^m\) |
| Principal series, both characters ramified | \(a(\mu_1)+a(\mu_2)\) | \(1\) at \(m=0\), \(0\) at \(m>0\) |
| \(\mathrm{St}_\chi\), \(\chi\) unramified | \(1\) | \((q^{-1}\chi(\varpi))^m\) |
| \(\mathrm{St}_\chi\), \(\chi\) ramified | \(2a(\chi)\) | \(1\) at \(m=0\), \(0\) at \(m>0\) |
| Supercuspidal | \(c\geq2\) | \(1\) at \(m=0\), \(0\) at \(m>0\) |

Every entry is zero for \(m<0\). For a supercuspidal the number \(c\) is determined by its Weyl action, rather than its compact function space alone. For example, the exact first level is the least \(n\) for which \(W1_U\) is supported in \(\varpi^{-n}\mathcal O\), once \(n\geq a(\omega)\).

## 5. How the local lines give classical newforms

Let \(k\geq1\), and write \(\iota_d f(z)=f(dz)\). We use the classical–adelic correspondence of Lesson 2, including its inverse finite nebentypus convention and Petersson comparison, and the cuspidal decomposition of Lessons 3–4.

Here are the proved global inputs for this section.

1. An irreducible cuspidal representation is the restricted tensor product of its local representations; at almost all finite primes its distinguished vector is spherical. This is proved in Lesson 12, Theorem 6.1; its equation (5.3) gives the fixed-space tensor basis.
2. Each such representation occurs once in the cuspidal spectrum: Lesson 15, Theorem 2.1. Its global Whittaker functional is nonzero and factors into the local ones: Lesson 14, Theorems 1.1 and 2.1. Two cuspidal representations with isomorphic local representations outside a finite set are isomorphic: Lesson 15, Theorem 3.1 and the complete argument in Solution 7.4.

The local newvector theorem proved above supplies all fixed-space and conductor assertions used here. The global inputs use the local theorems above and do not assume the classical conclusions that follow.

**Theorem 5.1 — classical decomposition.** Each weight-\(k\) cuspidal representation \(\pi\) has a unique normalized classical newform \(f_\pi\), with \(a_1(f_\pi)=1\), at the level
\[
M_\pi=\prod_p p^{c(\pi_p)}.
\tag{5.1}
\]
For every \(N\),
\[
S_k(\Gamma_1(N))
=\bigoplus_{M\mid N}\ \bigoplus_{\pi:\,M_\pi=M}\
 \bigoplus_{d\mid N/M}\mathbb C\,\iota_d f_\pi .
\tag{5.2}
\]
Only representations with the indicated holomorphic archimedean type occur. Blocks for distinct \(\pi\) are orthogonal. The new subspace, defined as the Petersson orthogonal complement of the span of all degeneracy images from proper divisor levels, is
\[
S_k^{\rm new}(\Gamma_1(N))
=\bigoplus_{\pi:\,M_\pi=N}\mathbb C f_\pi.
\tag{5.3}
\]
Its normalized forms are simultaneous eigenforms for the Hecke and diamond operators.

**Proof.** Decompose \(S_k(\Gamma_1(N))\) into its finite nebentypus spaces and apply Lesson 2 to each. The finite group is
\[
K_1(N)=\prod_p K_1(v_p(N)).
\]
The positive holomorphic weight-\(k\) line at infinity is one-dimensional by Lesson 3, Proposition 5.1. The fixed finite-level, compact-type and infinitesimal-character space is finite-dimensional by the arithmetic-finiteness theorem proved in Lesson 4, Section 4. The algebraic cuspidal comparison and discrete spectrum therefore give a finite direct sum of cuspidal constituent spaces.

By inputs 1–2, the contribution of \(\pi\) is its holomorphic line tensored with
\[
\bigotimes_{p\mid N}\pi_p^{K_1(v_p(N))}
\]
and the spherical lines at the remaining primes, with no additional multiplicity space. It is zero unless \(M_\pi\mid N\). If it is nonzero, Theorem 2.1 gives a tensor-product basis with \(j_p=0,\ldots,v_p(N)-c(\pi_p)\). The tensor of the local newvectors is a line at level \(M_\pi\). Its first Whittaker value is nonzero, since every local newfunction equals one at \(1\) and the holomorphic archimedean functional is nonzero on its lowest line. Global Whittaker factorization therefore gives a classical form with nonzero first coefficient; scaling it gives \(f_\pi\).

Let \(d=\prod p^{j_p}\). The corresponding local oldvector is right translation by the finite idèle matrix with components \(\operatorname{diag}(p^{-j_p},1)\). Components away from the support of \(d\), and the unit factors between \(p^{-j_p}\) and \(d^{-1}\), act trivially on the newvectors. Left rational invariance by \(\operatorname{diag}(d,1)\) moves this translation to the positive real matrix \(\operatorname{diag}(d,1)\). In the unitary lift of Lesson 2 this is
\[
d^{k/2}f_\pi(dz).
\tag{5.4}
\]
The nonzero scalar does not change the classical basis. This proves (5.2), and also its linear independence, since the local shifted vectors are a basis.

If \(M_\pi<N\), every basis vector in its block already comes from the divisor level \(M_\pi\); its whole block is old. If \(M_\pi=N\), that block is a line and cannot occur at a proper divisor level, since at some prime its local fixed space would be zero. Distinct irreducible constituents are orthogonal in the unitary spectrum, and Lesson 2 transfers this to Petersson orthogonality. These facts prove (5.3). At the minimal level, every level-preserving Hecke or diamond operator preserves the one-dimensional constituent line, so its normalized vector is a simultaneous eigenform. The vanishing of local fixed spaces below \(c(\pi_p)\) proves that its exact new level is (5.1). \(\square\)

There is a concrete normalization behind the phrase “first Whittaker value.” Choose the global character with \(\psi_\infty(x)=e^{2\pi ix}\), its finite components of conductor \(\mathbb Z_p\), and quotient additive volume one. Normalize the lowest real Whittaker function by
\[
W_\infty(d(y))=y^{k/2}e^{-2\pi y}\quad(y>0).
\]
For the normalized \(f_\pi(z)=\sum_{n\geq1}a_n e^{2\pi inz}\), let \(\xi_p\) be the local newfunction of this lesson. Global factorization gives
\[
a_n=n^{k/2}\prod_p \xi_p(p^{v_p(n)})\qquad(n\geq1).
\tag{5.5}
\]
To check the power, evaluate the global Whittaker function at the rational adelic matrix \(d(n)\). Moving \(d(n)\) to the left changes the integration variable \(x\) to \(x/n\); its adelic Jacobian is one. The character becomes the \(n\)-th Fourier character. On a fundamental domain with finite coordinate in \(\widehat{\mathbb Z}\), the lift is \(f_\pi(x+i)\), so the integral is \(a_n e^{-2\pi n}\). The factored value is
\(n^{k/2}e^{-2\pi n}\prod_p\xi_p(n)\). Local unit invariance replaces \(n\) by \(p^{v_p(n)}\) in each factor. This proves (5.5). It also proves \(a_{mn}=a_ma_n\) when \((m,n)=1\).

At \(p\nmid M_\pi\), (4.4) gives
\[
a_p=p^{(k-1)/2}(\alpha_p+\beta_p),\qquad
a_{p^2}=p^{k-1}(\alpha_p^2+\alpha_p\beta_p+\beta_p^2).
\tag{5.6}
\]
The pair \(a_p,a_{p^2}\) therefore determines the unordered local parameters: its first value gives their sum and its second gives their product. This will avoid any unproved assertion that traces alone distinguish all the constituents.

**Theorem 5.2 — the classical main lemma.** If \(f\in S_k(\Gamma_1(N))\) and
\[
a_n(f)=0\quad\text{for every }n\text{ with }(n,N)=1,
\]
then
\[
f=\sum_{p\mid N}\iota_p f_p,\qquad
f_p\in S_k(\Gamma_1(N/p)).
\tag{5.7}
\]
For \(N=1\), the empty sum says \(f=0\).

**Proof.** Expand \(f\) in the basis (5.2). Every term with \(d>1\) has zero coefficient at \(n\) coprime to \(N\), since \(d\mid N\). Thus on those indices its coefficient sequence is
\[
\sum_{\pi} b_\pi a_n(f_\pi),
\tag{5.8}
\]
where \(b_\pi\) is the coefficient of the unshifted newform.

These finitely many sequences are independent on the indices coprime to \(N\). Fix one constituent \(i\). For each other constituent \(j\), strong multiplicity one gives infinitely many primes where its unramified local parameters differ from those of \(i\); otherwise they would agree outside a finite set. Choose distinct such primes \(p_j\nmid N\). By (5.6), there is \(r_j\in\{1,2\}\) such that
\[
a_{p_j^{r_j}}(f_i)\ne a_{p_j^{r_j}}(f_j).
\]
For a sequence \(a=(a_n)\), define the linear functional
\[
L_i(a)=
\sum_{A\subset\{j:j\ne i\}}
 \left(\prod_{j\notin A} -a_{p_j^{r_j}}(f_j)\right)
 a_{\prod_{j\in A}p_j^{r_j}}.
\tag{5.9}
\]
The empty product in the index is \(1\). All its indices are coprime to \(N\). Coprime multiplicativity, proved in (5.5), says
\[
L_i(a(f_\pi))=
\prod_{j\ne i}
 \bigl(a_{p_j^{r_j}}(f_\pi)-a_{p_j^{r_j}}(f_j)\bigr).
\]
This vanishes for every \(\pi\ne i\), and is nonzero for \(\pi=i\). Applying \(L_i\) to the zero sequence (5.8) gives \(b_i=0\). If there is only one constituent, the functional is just \(a_1\). Thus every unshifted coefficient vanishes.

It remains to organize the shifted terms. For each \(d>1\), choose one prime \(p\mid d\). The term \(f_\pi(dz)\) is \(\iota_p\) applied to \(f_\pi((d/p)z)\). Since \(d\mid N/M_\pi\), its inner form has level dividing \(M_\pi d/p\), a divisor of \(N/p\). Collecting the finitely many terms for each chosen prime produces \(f_p\) and proves (5.7). \(\square\)

These are the decomposition and main lemma assigned to the modular-forms course, Lesson 10. The argument here derives them from the local and adelic representation theory; the classical Fricke-operator computations remain with that course. Theorem 5.1 uses global multiplicity one, while the separation step (5.9) uses strong multiplicity one. Local uniqueness of a Whittaker functional by itself supplies neither global conclusion.

Deligne's §2.2, Remarque 2.2.7.1, emphasizes the normalized function of the newvector; §§2.4–2.5 connect it with the classical newform and its coefficients. In our unitary induction convention the local function is not the raw sequence \(a_{p^m}\): formula (5.5) inserts the factor \(p^{mk/2}\). Keeping that factor is what makes the spherical formula and the special coefficient agree.

## 6. Two levels, two local types

**Example 6.1 — level \(11\).** Use the normalized weight-two trivial-character newform
\[
f_{11}(z)=\eta(z)^2\eta(11z)^2
=q-2q^2-q^3+2q^4+q^5+\cdots+q^{11}+\cdots,
\]
where in this example \(q=e^{2\pi iz}\). Its level, character, eta expression and \(a_{11}=1\) are recorded on the [LMFDB page for \(11.2.a.a\)](https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/11/2/a/a/).

Theorem 5.1 gives \(c(\pi_{11})=1\). Trivial central character on the units rules out a principal series with just one ramified character; if its central character is trivial, the two unit characters are inverse and have equal conductors. An unramified principal has conductor zero, and a supercuspidal has conductor at least two. Thus
\(\pi_{11}=\mathrm{St}_\chi\) with \(\chi\) unramified. Equations (4.3) and (5.5) give
\(a_{11}=11(\chi(11)/11)=\chi(11)\).
It equals one, so \(\chi\) is the trivial unramified character and \(\pi_{11}=\mathrm{St}\).

**Example 6.2 — level \(27\).** Use the weight-two trivial-character newform \(27.2.a.a\). The [LMFDB record for \(27.a1\)](https://www.lmfdb.org/EllipticCurve/Q/27/a/1) identifies this associated modular form and records
\[
f_{27}=q-2q^4-q^7+5q^{13}+4q^{16}-7q^{19}+O(q^{20}).
\]
The recorded form is input data for this example; no elliptic-curve modularity argument is being assumed proved here.

Its exact level gives \(c(\pi_3)=3\). With trivial central character a principal conductor is even, since the inducing unit characters are inverse. A special conductor is either one or \(2a(\chi)\), also excluding three. The classification therefore makes \(\pi_3\) supercuspidal. Its normalized function is \(1_{\mathbb Z_3^\times}\), so (5.5) gives \(a_3=0\), agreeing with the displayed expansion. The zero coefficient alone would not determine conductor three; the exact level is essential.

## 7. Exercises with complete solutions

**Exercise 7.1 — one ramified character.** Let \(\mu_1\) be unramified and \(a(\mu_2)=2\). Compute the conductor of \(I(\mu_1,\mu_2)\), its fixed-space dimensions and its normalized newfunction.

**Solution 7.1.** The ratio \(\mu_1/\mu_2\) is ramified, so it cannot be either exceptional unramified ratio \(|\ |^{\pm1}\). The induction is irreducible. Lemma 3.1 counts the cells
\[
2\leq i\leq n.
\]
There are none at \(n=0,1\), one at \(n=2\), and \(n-1\) at \(n\geq2\). Thus \(c=2\) and \(\dim V_n=\max(0,n-1)\). The only unit-invariant noncompact germ is \(|t|^{1/2}\mu_1(t)\). The normalized recurrence (4.3), and the nonzero-germ argument following it, give
\[
\xi_2(\varpi^m u)=q^{-m/2}\mu_1(\varpi)^m
\quad(m\geq0),\qquad \xi_2=0\quad(m<0).
\]
The oldbasis at level \(n\geq2\) consists of its shifts by \(\varpi^{-j}\), \(0\leq j\leq n-2\). A ramified central character does not turn this into ordinary \(K_0(n)\)-invariance: the character is \(\omega(d)\) as in (1.2).

**Exercise 7.2 — the Steinberg vector.** Find the normalized newvector of the untwisted Steinberg representation in the Kirillov model.

**Solution 7.2.** The exact induction sequence gives \(\dim\mathrm{St}^{K_1(n)}=n\), so the first level is \(1\). Its germ is \(c|t|\) by Lesson 7, Proposition 6.2. A unit-invariant function with this germ and support in \(\mathcal O\) belongs to \(V_n\) for some \(n\) by smoothness and Lemma 1.1. Consequently the level-one newfunction cannot be compact: all the oldbasis shifts would then be compact and could not span that function. In (4.3) its nonzero germ forces \(A=q^{-1}\). Normalizing its value on \(U\) gives exactly
\[
\xi_{\rm St}(t)=|t|\,1_{\{|t|\leq1\}}\qquad(t\in F^\times).
\]
This is an equality of functions, not only an asymptotic at zero. The recurrence fixes all shells of nonnegative valuation, and upper integral invariance kills the negative shells. Its Weyl transform meets the lower level-one support condition by Lemma 1.1, because it is the computed vector of \(V_1\). No assertion that \(1_U\) itself is the Steinberg newvector has been made.

**Exercise 7.3 — a zero bad-prime coefficient.** Using the proved global inputs of Section 5, show that a normalized trivial-character newform whose level is divisible by \(p^2\) has \(a_p=0\).

**Solution 7.3.** At \(p\), the conductor \(c(\pi_p)=v_p(N)\) is at least two. A principal series with trivial central character has inverse inducing unit characters, hence either both unramified or both ramified. The former has conductor zero and is excluded. In the latter case its unit-invariant newfunction is compact and equals \(1_U\). A special representation at this conductor must be a ramified twist, since an unramified twist has conductor one; its newfunction is again \(1_U\). The remaining possibility is supercuspidal, with the same normalized function. These exhaust the infinite-dimensional local classification. In all cases \(\xi_p(p)=0\), so the normalization (5.5) gives
\[
a_p=p^{k/2}\xi_p(p)=0.
\]
A principal series with one ramified inducing character can have a nonzero bad-prime coefficient, but its unit central character is then ramified. The trivial-character assumption excludes it.

**Exercise 7.4 — principal-series dimensions directly.** Prove the dimension formula for principal series without invoking Theorem 2.1. Identify a basis at each level.

**Solution 7.4.** At \(n=0\) the spherical section exists precisely when both inducing characters are unramified. At \(n\geq1\), use the primitive-row identification and representatives \(r_i\) from Lemma 3.1. Equation (3.2) shows that the stabilizer on the \(i\)-th cell has diagonal characters on \(U_{n-i}\times U_i\). A function supported on that cell is determined by \(f(r_i)\). It is well-defined with \(f(r_i)=1\) exactly when
\[
a(\mu_1)\leq n-i,\qquad a(\mu_2)\leq i.
\]
When this holds, define it on \(B(\mathcal O)r_iK_1(n)\) by the inducing character and extend by zero to the other cells. The stabilizer calculation makes this definition independent of the chosen decomposition. The finitely many cells are open and closed, so it is a locally constant compact-picture section. These sections have disjoint supports and form a basis; all other cells force value zero. Their number is
\(\max(0,n-a(\mu_1)-a(\mu_2)+1)\).

For irreducible induction this is precisely the requested formula with \(c=a(\mu_1)+a(\mu_2)\). For exceptional induction it remains the dimension of the whole induced representation. Subtracting the determinant-character fixed space using exact compact averaging gives the special dimensions in (3.4), rather than incorrectly applying an irreducible formula to the reducible induction.

## References

- H. Jacquet and R. P. Langlands, [*Automorphic Forms on GL(2)*](https://publications.ias.edu/sites/default/files/Automorphic-forms-on-GL2.pdf), LNM 114, 1970, §2: Kirillov action and the finite Weyl-coefficient identities underlying Theorem 4.3. The proofs in Lesson 7 fix the conventions used here.
- P. Deligne, [*Formes modulaires et représentations de GL(2)*](https://publications.ias.edu/sites/default/files/Number21.pdf), in *Modular Functions of One Variable II*, LNM 349, 1973, §2.2, Théorème 2.2.6 and Remarque 2.2.7.1; §§2.3–2.5 for the newvector normalization and classical passage. His lower-unipotent convention is translated explicitly after Theorem 2.1.
- [LMFDB newform \(11.2.a.a\)](https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/11/2/a/a/) and [LMFDB elliptic-curve record \(27.a1\)](https://www.lmfdb.org/EllipticCurve/Q/27/a/1), the latter's associated modular form \(27.2.a.a\) and displayed coefficient data. Accessed October 2026. Only the identified example data are inputs; the local type deductions are given in Section 6.
