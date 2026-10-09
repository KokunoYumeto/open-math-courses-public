# Pinnings and the classification of split reductive groups

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Original text: public domain (CC0). The one-dimensional affine-open lemma follows the Stacks Project's proof; see History.*

The integral root datum remembers a reductive group up to isomorphism. A pinning removes the conjugation ambiguity and makes this assertion functorial. The main work is to show that the multiplication of root groups is forced by the datum, including over rings in which two or three vanish. We first do those calculations and glue them across the open cell. We then construct groups in characteristic zero and pass to an integral model.

Throughout, a split group has a specified split maximal torus, a constant identification of its character lattice, and trivial root lines. All assertions about a base scheme allow nilpotents and arbitrary characteristic. On a disconnected base, maps of constant data are locally constant; they need not have one value on every component. The purely combinatorial Coxeter presentation and length formula are the precise prerequisites from [Root systems and their Weyl groups](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-RG/prerequisites.html#prerequisite-rt-lie-08), identified at the end.

## 1. What a pinning fixes

Let \(G/S\) be reductive, let \(T=D_S(X)\) be a split maximal torus, and choose a positive system \(\Phi^+\) with simple roots \(\Delta\). A **pinning** consists of a frame \(E_\alpha\) in every simple root line \(\mathfrak g_\alpha\), \(\alpha\in\Delta\). The canonical root parametrization from the preceding lesson gives

$$
x_\alpha:\mathbf G_a\longrightarrow U_\alpha,\qquad
x_\alpha(u)=\exp_\alpha(uE_\alpha).
$$

The perfect rank-one pairing gives a unique frame \(E_{-\alpha}\) with \(E_\alpha E_{-\alpha}=1\). Put

$$
n_\alpha=x_\alpha(1)x_{-\alpha}(-1)x_\alpha(1),
\qquad t_\alpha=\alpha^\vee(-1).
\tag{1.1}
$$

The rank-one homomorphism \(\operatorname{SL}_2\to G\) proves

$$
n_\alpha^2=t_\alpha,\quad
n_\alpha t n_\alpha^{-1}=s_\alpha(t),\quad
\operatorname{Ad}(n_\alpha)E_\alpha=-E_{-\alpha}.
\tag{1.2}
$$

It also proves \((n_\alpha x_\alpha(1))^3=1\). These are identities of group schemes, including in characteristic two.

For example, the usual pinning of \(\operatorname{SL}_2\) uses the diagonal torus, the upper triangular Borel, and

$$
x_\alpha(u)=
\begin{pmatrix}1&u\\0&1\end{pmatrix}.
$$

Then \(\alpha(\operatorname{diag}(z,z^{-1}))=z^2\), \(\alpha^\vee(z)=\operatorname{diag}(z,z^{-1})\), and \(n_\alpha=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\). The frame, rather than just its line, is part of the pinning.

A based root datum includes \(X,X^\vee,\Phi,\Phi^\vee\) and \(\Delta\). An isomorphism of based data induces the corresponding torus isomorphism, and matches roots and coroots. We use this covariant formulation; its map on character lattices runs in the opposite direction.

### Integral Weyl representatives

The pinned representatives also determine the full arithmetic normalizer, including the signs from the central torus.

**Proposition 1.1 (the integral normalizer).** Let \(G/\mathbb Z\) be a pinned split reductive group, with split maximal torus \(T=D_{\mathbb Z}(X)\), constant reduced root datum and Weyl group \(W\). Put \(r=\operatorname{rank}X\) and \(N=N_G(T)\). Then \(N/T\simeq\underline W\), and
\[
1\longrightarrow\operatorname{Hom}(X,\{\pm1\})
\longrightarrow N(\mathbb Z)\longrightarrow W\longrightarrow1
\]
is an exact sequence of finite groups. Thus \(|N(\mathbb Z)|=2^r|W|\). For every ring \(A\), an integral element \(n\) above \(w\) acts on \(T(A)\) by
\[
(nhn^{-1})(\chi)=h(w^{-1}\chi).
\]
Moreover
\[
N(A)/T(A)\simeq\underline W(A)
=\operatorname{LC}(\operatorname{Spec}A,W).
\]
The representatives of \(W\) need not form a subgroup of \(N(\mathbb Z)\).

**Proof.** Choose the negative parameter linked to each pinned simple-root parameter. The rank-one homomorphism \(\operatorname{SL}_2\to G\) gives
\[
n_\alpha=x_\alpha(1)x_{-\alpha}(-1)x_\alpha(1),
\qquad n_\alpha^2=\alpha^\vee(-1),
\qquad\operatorname{Int}(n_\alpha)|_T=s_\alpha.
\]
These identities are proved in AG-RG-03 Theorem 7.1 and AG-RG-05 (1.1)–(1.2). Since the simple reflections generate the Weyl group, selecting one reflection word for each \(w\) and multiplying these elements yields \(n_w\in N(\mathbb Z)\). This choice uses no word-independence assertion.

AG-RG-04 Theorem 4.2 makes \(Q=N/T\) finite étale. The chosen classes define a map \(\coprod_{w\in W}\operatorname{Spec}\mathbb Z\to Q\). By AG-RG-04 Theorem 4.1, on every geometric fibre these classes are distinct and exhaust its Weyl group. On coordinate rings the map is between finite free \(\mathbb Z\)-modules of equal rank, and its determinant is invertible modulo every prime; the determinant is therefore \(\pm1\). The map is an isomorphism. Its group laws agree on geometric fibres and hence on the constant reduced source. This identifies \(Q\) with \(\underline W\) as a group scheme.

A section of \(N\) maps to the identity section of \(Q\) exactly when it factors through the kernel \(T\). The chosen representatives prove surjectivity on \(\mathbb Z\)-points. Since
\[
T(\mathbb Z)=\operatorname{Hom}(X,\mathbb Z^\times)
=\operatorname{Hom}(X,\{\pm1\}),
\]
the displayed extension and its order follow. Retain all these torus signs, including those arising from the central torus; the subgroup generated by coroot signs can be smaller.

The convention \(w\chi=\chi\circ\operatorname{Int}(n^{-1})\) gives \(\chi(nhn^{-1})=(w^{-1}\chi)(h)\) after every base change. This proves the stated action.

Finally a section of \(\underline W\) over \(A\) is a locally constant map from \(\operatorname{Spec}A\) to \(W\). Its finitely many fibres are clopen. On the fibre with value \(w\), base change \(n_w\); these sections glue to an element of \(N(A)\). Thus the map \(N(A)\to\underline W(A)\) is surjective, with kernel \(T(A)\). This proves the quotient formula without a hypothesis on \(\operatorname{Pic}(A)\). \(\square\)

For \(\operatorname{SL}_2\), \(T(\mathbb Z)=\{\pm I\}\), and both lifts of the nonidentity Weyl element square to \(-I\). Hence this extension is \(C_4\to C_2\), and has no group-homomorphic section.

**Lifting scope.** For a general normalizer extension over a scheme, the fibre over a Weyl section is a \(T\)-torsor. That section lifts precisely when this torsor has a global section, equivalently when its class in \(H^1_{\mathrm{fppf}}(A,T)\) is trivial. A sheaf quotient alone does not assert surjectivity on \(A\)-points. For the pinned split model above, the explicit integral representatives trivialize every such fibre; the obstruction is zero even when \(\operatorname{Pic}(A)\ne0\). This is a torsor trivialization argument, not an assertion that \(H^1(A,T)\) vanishes.

## 2. Reducing comparisons to two simple roots

We need two facts about root systems. The first explains why rank-two calculations control commutators even when the two roots under consideration are not simple.

**Lemma 2.1.** For independent roots \(\alpha,\gamma\), there is a base of the root system containing \(\alpha\) and another root \(\beta\) such that \(\gamma=a\alpha+b\beta\), with \(a,b\) nonnegative integers.

**Proof.** In the plane \(E=\mathbf R\alpha+\mathbf R\gamma\), choose a positive system for \(\Phi\cap E\) in which \(\alpha\) is simple and \(\gamma\) is positive. One can do this by taking a linear functional which is positive and sufficiently small on \(\alpha\), and positive on \(\gamma\). In the limit in which its value on \(\alpha\) is zero, the only roots of \(E\) on that wall are \(\pm\alpha\). Thus \(\alpha\) is an extremal positive root; reducedness makes it simple. Let \(\beta\) be the other simple root of this plane system. The positive-root expansion gives the asserted integers.

Extend this positive system to the whole root system as follows. Choose a functional \(q\) vanishing on \(E\) and nonzero on each root outside \(E\), and add a sufficiently small extension of the functional just chosen on \(E\). Roots outside \(E\) keep the sign of \(q\). A sum of positive roots involving any root outside \(E\) has positive \(q\)-value and cannot equal \(\alpha\) or \(\beta\). Their indecomposability in the plane therefore implies their indecomposability in the full positive system. They belong to its base. If \(E\) is the full root space, the extension step is unnecessary. \(\square\)

The next fact controls different choices for transporting a simple root to another root. Write

$$
\ell(w)=\#\{\gamma\in\Phi^+:w\gamma\in-\Phi^+\}.
$$

**Lemma 2.2 (root transport).** If \(w\alpha=\beta\) for simple roots \(\alpha,\beta\), then \(w\) is a product of elements of standard rank-two Weyl groups, each carrying the current simple root to the next simple root. A factor fixing that root belongs to a rank-two subgroup containing it.

**Proof.** Induct on \(\ell(w)\). Length zero means \(w=1\). Otherwise some simple root \(\delta\) has \(w\delta<0\): if all simple roots had positive images, all positive roots would. Here \(\delta\ne\alpha\). Let \(E\) be their plane and set

$$
A=w^{-1}\Phi^+\cap E.
$$

This is a positive system of \(\Phi\cap E\). Choose \(v\in W_{\alpha,\delta}\) with \(vA=\Phi^+\cap E\), and put \(w'=wv^{-1}\). An element of this rank-two subgroup permutes the positive roots outside \(E\): their positive coefficients at the other simple roots are unchanged. Thus \(w'\) has the same number of inversions outside \(E\) as \(w\), and no inversions inside \(E\). At least \(\delta\) was an inversion of \(w\), so \(\ell(w')<\ell(w)\).

The root \(\alpha\) is simple for \(A\), since \(w\alpha=\beta\) is simple in the full positive system. Consequently \(v\alpha\) is either \(\alpha\) or \(\delta\). Apply induction to \(w'\), which carries this simple root to \(\beta\), and prepend the factor \(v\). \(\square\)

These arguments apply to the root space; central directions in a reductive datum are fixed by its Weyl group.

## 3. The multiplication forced in rank two

Fix two distinct simple roots \(\alpha,\beta\), taking \(\alpha\) short in the unequal-length cases. In the formulas below all parameters are sections over an arbitrary \(S\)-scheme. We choose frames for the remaining positive roots by the indicated conjugations:

| Type | Positive roots besides \(\alpha,\beta\) | Chosen frames |
|---|---|---|
| \(A_2\) | \(c=\alpha+\beta\) | \(E_c=\operatorname{Ad}(n_\beta)E_\alpha\) |
| \(B_2\) | \(c=\alpha+\beta,\ d=2\alpha+\beta\) | \(E_c=\operatorname{Ad}(n_\beta)E_\alpha,\ E_d=\operatorname{Ad}(n_\alpha)E_\beta\) |
| \(G_2\) | \(c=\alpha+\beta,\ d=2\alpha+\beta,\ e=3\alpha+\beta,\ f=3\alpha+2\beta\) | \(E_c=\operatorname{Ad}(n_\beta)E_\alpha,\ E_d=\operatorname{Ad}(n_\alpha)E_c,\ E_e=-\operatorname{Ad}(n_\alpha)E_\beta,\ E_f=\operatorname{Ad}(n_\beta)E_e\) |

Write \(x_c,x_d,\ldots\) for the corresponding root parametrizations. The complete noncommuting positive-root relations are

$$
\begin{array}{ll}
A_2:&
x_\beta(y)x_\alpha(x)=
x_\alpha(x)x_\beta(y)x_c(xy);\\[2mm]
B_2:&
x_\beta(y)x_\alpha(x)=
x_\alpha(x)x_\beta(y)x_c(xy)x_d(x^2y),\\
&
x_c(y)x_\alpha(x)=x_\alpha(x)x_c(y)x_d(2xy);\\[2mm]
G_2:&
x_\beta(y)x_\alpha(x)=
x_\alpha(x)x_\beta(y)x_c(xy)x_d(x^2y)x_e(x^3y)x_f(x^3y^2),\\
&
x_c(y)x_\alpha(x)=
x_\alpha(x)x_c(y)x_d(2xy)x_e(3x^2y)x_f(3xy^2),\\
&
x_d(y)x_\alpha(x)=x_\alpha(x)x_d(y)x_e(3xy),\\
&
x_e(y)x_\beta(x)=x_\beta(x)x_e(y)x_f(-xy),\\
&
x_d(y)x_c(x)=x_c(x)x_d(y)x_f(3xy).
\end{array}
\tag{3.1}
$$

All other positive-root pairs commute. The powers in these formulas are forced by torus weights, and the coefficient integers are independent of the base. In particular, the terms with coefficient two or three disappear in the relevant characteristics; the proof never divides by them.

Here are the conjugation rules needed along with (3.1):

| Type | \(\operatorname{Ad}(n_\alpha)\) | \(\operatorname{Ad}(n_\beta)\) |
|---|---|---|
| \(A_2\) | \(E_\beta\mapsto-E_c,\ E_c\mapsto E_\beta\) | \(E_\alpha\mapsto E_c,\ E_c\mapsto-E_\alpha\) |
| \(B_2\) | \(E_\beta\mapsto E_d,\ E_d\mapsto E_\beta,\ E_c\mapsto-E_c\) | \(E_\alpha\mapsto E_c,\ E_c\mapsto-E_\alpha,\ E_d\mapsto E_d\) |
| \(G_2\) | \(E_c\mapsto E_d,\ E_d\mapsto-E_c,\ E_\beta\mapsto-E_e,\ E_e\mapsto E_\beta,\ E_f\mapsto E_f\) | \(E_\alpha\mapsto E_c,\ E_c\mapsto-E_\alpha,\ E_d\mapsto E_d,\ E_e\mapsto E_f,\ E_f\mapsto-E_e\) |

In \(A_1\times A_1\), the two rank-one groups commute. The normalizer relations are

$$
(n_\alpha n_\beta)^m=
\begin{cases}
t_\alpha t_\beta,&m=2,\ A_1\times A_1,\\
1,&m=3,\ A_2,\\
t_\alpha,&m=4,\ B_2\text{ with }\alpha\text{ short},\\
1,&m=6,\ G_2.
\end{cases}
\tag{3.2}
$$

### Deriving the coefficients

We give the calculations over an affine open of \(S\), where all unknown coefficients lie in its ring \(R\). Since root-product coordinates are unique, identities with indeterminate parameters in \(R[x,y]\) determine coefficients even when \(R\) has nilpotents.

If no root is a positive integral combination of two roots, their root groups commute, by the weight calculation in the preceding lesson. A rank-one group therefore acts trivially on a root line \(\mathfrak g_\gamma\) when neither \(\gamma+\alpha\) nor \(\gamma-\alpha\) is a root. The definition of the frames and \(n_\alpha^2=t_\alpha\) give every entry in the conjugation table except the scalar on \(E_c\) in \(B_2\) and the scalar carrying \(E_\beta\) to \(E_c\) in \(A_2\).

For \(A_2\), put an unknown \(A\) in the last parameter of the first formula of (3.1). Conjugating that formula by \(n_\beta\) gives

$$
x_{-\beta}(-y)x_c(x)
=x_c(x)x_{-\beta}(-y)x_\alpha(-Axy).
$$

The identity \(n_\beta x_\alpha(x)n_\beta^{-1}=x_c(x)\), after cancelling commuting end factors, becomes

$$
x_\beta(1)x_\alpha(x)x_\beta(-1)
=x_{-\beta}(1)x_c(x)x_{-\beta}(-1).
$$

Reordering its two sides gives respectively \(x_\alpha(x)x_c(Ax)\) and \(x_\alpha(Ax)x_c(x)\). Thus \(A=1\). If \(\operatorname{Ad}(n_\alpha)E_\beta=zE_c\), apply the same cancellation with \(\alpha,\beta\) interchanged. It gives

$$
x_\beta(y)x_c(-y)=x_\beta(-z^{-1}y)x_c(zy).
$$

Hence \(z=-1\). This proves both tables for \(A_2\).

For \(B_2\), use unknown coefficients \(A,B,C\) in place of \(1,1,2\) in its two relations, and write \(\operatorname{Ad}(n_\alpha)E_c=kE_c\). Conjugating the first relation by \(n_\beta\), and cancelling as above, gives

$$
x_\alpha(x)x_c(Ax)x_d(Bx^2)
=x_\alpha(Ax)x_c(x)x_d((AC-B)x^2).
$$

Thus \(A=1\) and \(C=2B\). Conjugate the first relation by \(n_\alpha\), and use \(n_\alpha x_\beta(y)n_\alpha^{-1}=x_d(y)\). The resulting cancellation gives

$$
x_\beta(y)x_c(-Ay)x_d(By)
=x_\beta(By)x_c(Aky)x_d(y).
$$

The three groups on each side commute. Therefore \(B=1,\ k=-1,\ C=2\).

For \(G_2\), put coefficients \(A,B,C,D\) in the four extra parameters of the first relation, \(E,F,G\) in the second, \(H\) in the third, and \(J\) in the fourth. Conjugation by \(n_\beta\) makes the coefficient in the fifth relation also \(H\). The frame choices and the square relations already give its full conjugation table.

The cancellation identity for \(n_\beta x_\alpha(x)n_\beta^{-1}=x_c(x)\) gives the following two normal forms:

$$
\begin{aligned}
&x_\alpha(x)x_c(Ax)x_d(Bx^2)x_e(Cx^3)x_f((D-CJ)x^3),\\
&x_\alpha(Ax)x_c(x)x_d((AE-B)x^2)
 x_e((A^2F+CJ-D)x^3)x_f((AG-C)x^3).
\end{aligned}
$$

Comparison gives

$$
A=1,\qquad E=2B,\qquad C+D=F+CJ,\qquad F=G.
\tag{3.3}
$$

The identity \(n_\alpha x_\beta(y)n_\alpha^{-1}=x_e(-y)\) similarly gives

$$
\begin{aligned}
&x_\beta(y)x_c(-Ay)x_d(By)x_e(-Cy)x_f(-Dy^2),\\
&x_\beta(Cy)x_c(-By)x_d(Ay)x_e(-y)x_f((D-CJ-ABH)y^2).
\end{aligned}
$$

Consequently \(C=1,\ A=B,\ D-CJ-ABH=-D\). Together with (3.3) this says

$$
A=B=C=1,\quad E=2,\quad F=G,\quad D+1=F+J,\quad 2D=H+J.
\tag{3.4}
$$

The cancellation identity carrying \(E_e\) to \(E_f\) under \(n_\beta\) reduces to

$$
x_e(x)x_f(-Jx)=x_e(-Jx)x_f(x);
$$

thus \(J=-1\). Finally use \(n_\alpha x_c(y)n_\alpha^{-1}=x_d(y)\). The left side, after cancelling its rank-one end factors, has normal form

$$
x_c(y)x_d(-Ey)x_e(Fy)x_f(-Gy^2).
$$

The right side is \(x_{-\alpha}(1)x_d(y)x_e(Hy)x_{-\alpha}(-1)\). Move \(x_{-\alpha}\) past these factors, using the conjugates by \(n_\alpha\) of the already written relations. In this movement a \(d\)-factor can create a \(c\)-factor, and an \(e\)-factor can create \(\beta,c,d\)-factors; none creates an additional \(e\)-factor. The \(e\)-coordinate is therefore \(Hy\). This gives \(F=H\). Equations (3.4) now imply \(F=D+2\) and \(2D=F-1\), so \(D=1\) by subtraction, and \(F=G=H=3\). No cancellation by two or three has occurred. This proves (3.1).

### Checking the normalizer powers

For a frame \(E_\gamma\), write \(n_\gamma\) for its rank-one representative. If \(n\) carries \(E_\gamma\) to \(zE_\delta\), direct substitution in (1.1) gives

$$
n n_\gamma n^{-1}=\delta^\vee(z)n_\delta.
\tag{3.5}
$$

For \(z=-1\) this is \(n_\delta^{-1}\). In moving torus factors through representatives use \(n_\alpha t=s_\alpha(t)n_\alpha\); in particular

$$
s_\alpha(t_\beta)
=t_\beta t_\alpha^{\langle\alpha,\beta^\vee\rangle}.
\tag{3.6}
$$

These formulas give (3.2) without assuming that torus two-torsion is central. For clarity, here are reductions of the alternating words. In \(A_2\),

$$
n_\alpha n_\beta n_\alpha=n_c^{-1}t_\alpha,\qquad
n_\beta n_\alpha n_\beta n_\alpha n_\beta=n_\alpha^{-1}.
$$

In \(B_2\),

$$
\begin{aligned}
n_\alpha n_\beta n_\alpha&=n_dt_\alpha,\\
n_\beta n_\alpha n_\beta n_\alpha n_\beta&=n_dt_\alpha t_\beta,\\
n_\alpha n_\beta n_\alpha n_\beta n_\alpha n_\beta n_\alpha&=n_\beta^{-1}t_\alpha.
\end{aligned}
$$

Here \(t_\alpha\) is central in this rank-two group. In \(G_2\) the conjugation table and (3.5) give, successively,

$$
\begin{aligned}
n_\alpha n_\beta n_\alpha&=n_e^{-1}t_\alpha,\\
n_\beta(n_\alpha n_\beta)^2&=n_f^{-1}t_\alpha,\\
n_\alpha(n_\beta n_\alpha)^3&=n_f^{-1},\\
n_\beta(n_\alpha n_\beta)^4&=n_et_\beta,\\
n_\alpha(n_\beta n_\alpha)^5&=n_\beta^{-1}.
\end{aligned}
$$

Multiplying the last word by \(n_\beta\) proves the sixth-power relation. The commuting case follows at once from \(n_\alpha^2=t_\alpha\) and \(n_\beta^2=t_\beta\). This completes all the rank-two assertions.

## 4. From local multiplication to the entire group

We first prove the extension on all test schemes, and then prove the cell identities to which it will be applied.

**Lemma 4.1 (extension from the open cell).** Let \(K/S\) be a smooth group with geometrically connected fibres, let \(\Omega\subset K\) be a fibrewise dense open containing the identity, and let \(H/S\) be a separated group scheme. A morphism \(f:\Omega\to H\) with \(f(1)=1\) and

$$
f(xy)=f(x)f(y)\quad\text{whenever }x,y,xy\in\Omega
\tag{4.1}
$$

extends uniquely to a homomorphism \(K\to H\).

**Proof.** The regular-component argument in S08 Theorem G.4.2 shows that a smooth geometrically connected field group is geometrically irreducible: its regular irreducible components are disjoint and open, so only one remains. For any test scheme \(R\to S\) and any finite list \(g_1,\ldots,g_d\in K(R)\), the open

$$
\Omega_R\cap\bigcap_{i=1}^d\Omega_Rg_i^{-1}
$$

has a nonempty open in every geometric fibre. Indeed each translate is open dense in the same irreducible fibre, and a finite intersection of nonempty opens in an irreducible space is nonempty. Its morphism to \(R\) is smooth and surjective, being an open of \(K_R\). Its affine smooth neighbourhoods, covering the base, give an fppf cover with a section: take these neighbourhoods themselves as the covering schemes. This argument also permits intersecting with the open \(\Omega_R^{-1}\).

For \(g\in K(R)\), choose on such a cover \(c,c^{-1},cg\in\Omega_R\). Then \(g=c^{-1}(cg)\) is a word in cell points. To a word \(x_1\cdots x_d\), assign \(f(x_1)\cdots f(x_d)\). This assignment is independent of the word. For two words with the same endpoint \(g\), choose \(a\) so that \(a\), every \(ax_1\cdots x_i\), and every translated prefix of the other word belong to \(\Omega_R\). There are finitely many conditions of the preceding form. At each step the two successive translated prefixes and the next letter are in \(\Omega_R\), so (4.1) applies. Multiplying either assigned image word on the left by \(f(a)\) gives \(f(ag)\). Group cancellation proves equality after the cover, and hence before it, since equality of morphisms is fpqc local by S04 Lemma A1.5.

The empty word at the identity has image \(1\). The same comparison consequently gives image \(1\) to every identity word. An inverse word has the inverse image, by comparing its concatenation with the original word to that empty word. Pullback of test schemes preserves all words, comparisons and their values. On overlaps of the covers the assigned values therefore agree. The sheaf property for scheme-valued points, proved in S04 Lemma A1.5, glues them to a natural transformation \(K(-)\to H(-)\). Concatenation gives multiplication and the empty word gives the identity. Yoneda then gives a scheme homomorphism. Every extension must have these values on all local generating words, proving uniqueness. This is the full word-extension argument also proved in RG03 Lemma 8.B. \(\square\)

We need a scheme-level density argument for the normalizer identities.

**Lemma 4.2 (density in a cell over arbitrary rings).** Put

$$
A=R[q_1,\ldots,q_N,z_1^{\pm1},\ldots,z_r^{\pm1}],
\qquad e:\ q_i=0,\ z_j=1.
$$

If \(d(e)\in R^\times\), then \(D(d)\) is universally schematically dense in \(\operatorname{Spec}A\) and in every open subscheme. Two maps from an open containing the section \(e\) to a separated scheme, agreeing on a smaller open containing \(e\), therefore agree on the entire common domain, locally on \(\operatorname{Spec}R\).

**Proof.** Substitute \(z_j=1+w_j\) in \(R[[q_1,\ldots,q_N,w_1,\ldots,w_r]]\). This embeds \(A\) in that ring. To check injectivity, multiply a Laurent polynomial by a Laurent monomial to make it an ordinary polynomial. Its substituted multiplier is an invertible formal series. Translation \(z_j\mapsto1+w_j\) identifies the ordinary polynomial algebra with the polynomial algebra in \(w_j\), and a polynomial has zero formal series exactly when every coefficient is zero. This argument is valid over any \(R\), including rings with nilpotents.

The series of \(d\) has invertible constant term, so it is a unit. Its inverse is obtained recursively by total degree, using only that constant unit. Multiplication by \(d\) is consequently injective on \(A\). On any localization \(A_h\) it remains injective: if \(da/h^n=0\), some power of \(h\) annihilates \(da\), and injectivity on \(A\) makes the same power annihilate \(a\). Thus \(A_h\to(A_h)_d\) is injective. Every open is covered by these principal charts. The identical proof works after every \(R\)-algebra extension, proving the asserted universal schematic density.

For the last assertion, let \(U\subset V\) be the smaller and larger domains. Around the identity over any base point, choose a principal \(D(d)\subset U\) in the cell, then restrict the base to \(D(d(e))\). This is a neighbourhood of that base point, and \(d(e)\) is a unit there. The equalizer of the two maps is closed in \(V\), by separatedness of the target. Each element of its ideal vanishes after localization at \(d\). The injection just proved on every principal chart makes the ideal zero. Hence the equalizer is all of \(V\). The base neighbourhoods cover, giving equality everywhere. \(\square\)

Now let \(K\) be split reductive and let the maps on its torus and canonical root groups have values in \(H\). Suppose they intertwine torus characters, linked rank-one multiplication, normalizer conjugations and the positive rank-two relations of Section 3. We prove that their ordered product on

$$
\Omega=U^-TU^+
$$

satisfies (4.1). All the maps and identities below are identities on their test schemes, not just on geometric points.

First they give homomorphisms \(f_+:U^+\to H\) and \(f_-:U^-\to H\). Lemma 2.1 embeds the plane of any independent root pair into a base; the chamber transitivity proved in RG04 transports that base to the specified one. Thus the assumed normalizer conjugations transport (3.1) to every nonopposite root pair. Collinear positive roots are equal, by reducedness, and their factors combine by the additive root-group law. A pair with no positive combination that is a root commutes by the full weight-coordinate proof in RG04 Section 5.

Here is why these pair identities suffice. Give a positive root the sum of its simple-root coefficients as height. A commutator term \(i\alpha+j\beta\), \(i,j>0\), has height strictly larger than each input root. Collect the height-one factors first, then height two, and so on. Moving a factor past another introduces only factors of larger height; at each fixed height no new factor of that height is created, and only finitely many original or previously created factors remain. The maximum root height is finite, so this process terminates. Equal-root factors add their parameters. The ordered root-product isomorphism in RG04 Section 5 gives a unique final coordinate expression. The identical collection, with the identical parameter polynomials, holds for the images in \(H\). It proves multiplicativity and independence of order for \(f_+\). Apply the same argument to negative roots to prove it for \(f_-\).

Define \(f(vtu)=f_-(v)f_T(t)f_+(u)\) by the cell product isomorphism. Torus-equivariance and the just proved homomorphisms give

$$
f(b_-gb_+)=f(b_-)f(g)f(b_+),
\qquad b_-\in B^-,\ b_+\in B^+,\ g\in\Omega.
\tag{4.2}
$$

The domain is stable under these two triangular multiplications: multiply the negative factors on the left and the positive factors on the right, moving torus factors by their characters.

For a simple \(\alpha\), choose the root orders with its negative factor last and its positive factor first. Write

$$
g=v_0\,h\,u_0,\qquad h\in U_{-\alpha}TU_\alpha,
$$

where \(v_0,u_0\) use the other negative and positive roots. Reflection \(s_\alpha\) preserves those other two root sets, by the simple-root coefficient calculation in RG04. Conjugation by \(n_\alpha\) therefore keeps the exterior factors triangular. By (4.2), membership of the conjugate in the cell reduces exactly to its middle rank-one factor.

This middle domain is a scheme domain. For the subtorus \(T_\alpha\) of the rank-one construction, the full torus action fixes exactly the \(\pm\alpha\) root coordinates in \(\Omega\): every other root restricts nontrivially to \(T_\alpha\), and coefficient comparison with its universal character makes its coordinate zero. Thus \(\Omega\cap C_K(T_\alpha)=U_{-\alpha}TU_\alpha\) on every test algebra. In its rank-one cover, the required multiplication is the explicit identity

$$
x_\alpha(a)x_{-\alpha}(b)
=x_{-\alpha}(b/q)\,\alpha^\vee(q)\,x_\alpha(a/q),
\qquad q=1+ab\in R^\times.
$$

Direct multiplication of the two-by-two matrices proves this identity; its upper left entry is \(q\), so invertibility is exactly the Gauss-cell condition. Pull back the torus factor along the fppf torus cover of RG04 Theorem 2.1. RG03 Theorem 7.1 supplies the linked rank-one homomorphism and this exact unit criterion on the middle cell. The pulled-back identities descend by S04 Lemma A1.5. The assumed maps preserve the two root parameters, the coroot and torus characters; they consequently preserve this full Gauss identity. Together with (4.2) it gives

$$
f(n_\alpha g n_\alpha^{-1})
=f_N(n_\alpha)f(g)f_N(n_\alpha)^{-1}
\tag{4.3}
$$

on the entire common cell domain.

For a word in simple representatives, impose that all its intermediate conjugates lie in \(\Omega\). This is an open containing the identity section. Induction proves (4.3) there. Its full common domain is also an open in the cell containing that section. Lemma 4.2 therefore extends the identity to that full domain, including every nilpotent base change. Torus conjugations already intertwine by their characters; multiplying with a torus element gives the corresponding identity for every normalizer section.

Choose a word for the longest Weyl element \(w_0\), using the Coxeter theorem in RG04; letters may repeat. Its representative \(n_0\) interchanges \(U^+\) and \(U^-\). For \(u\in U^+\), \(v\in U^-\) with \(uv\in\Omega\), conjugation makes \(uv\) a negative-positive product. Its cell map is the product of the two factor maps. Apply (4.3) and cancel the two normalizer factors to obtain \(f(uv)=f_+(u)f_-(v)\).

Finally, for \(x=vtu\) and \(x'=v't'u'\) in the cell,

$$
xx'=vt(uv')t'u'.
$$

If \(xx'\in\Omega\), triangular stability and its inverse give \(uv'\in\Omega\). Apply (4.2) and the preceding mixed-product identity. The resulting value is precisely \(f(x)f(x')\). This proves (4.1) on its full open domain. Lemma 4.1 extends the cell map uniquely to \(K\to H\).

## 5. The isomorphism theorem

**Theorem 5.1.** For pinned split reductive groups over a scheme \(S\), isomorphisms preserving the pinnings correspond bijectively to isomorphisms of their based root data. The correspondence commutes with every base change. Over a disconnected base, the datum isomorphism is allowed to be locally constant.

**Proof.** A pinning-preserving group isomorphism identifies its split torus, root characters, coroots and simple frames, hence gives an isomorphism of based root data. We prove the converse and uniqueness over the entire base, including its nilpotents. Work locally where the given datum map is constant; the final uniqueness will glue these local constructions.

Match \(T\) with \(T'\) by the group-algebra character map, using AG-GS, *Diagonalizable groups*, Theorem 2.2. Match the pinned simple additive parameters. RG03 Theorem 7.1 gives their linked negative parameters and full rank-one homomorphisms. Thus the maps preserve \(n_\alpha\), \(n_\alpha^2=\alpha^\vee(-1)\), all torus conjugations, and the rank-one Gauss formulas. They also match the root lattices with their central directions; all torus elements, not only coroot signs, must be retained.

We first identify the normalizer presentation as an actual sheaf. Form the presheaf of groups generated by \(T(R)\) and symbols \(n_\alpha\), for every test scheme \(R\), with their torus conjugation rules, square rules and rank-two power rules (3.2). Sheafify for the fppf topology and call the result \(\mathcal N\). The torus is normal in this presentation, because conjugation by each generator has the prescribed torus automorphism. Killing it leaves exactly the Coxeter presentation in RG04 Theorem 3.4. Consequently the quotient sheaf is the constant Weyl sheaf \(\underline W\).

There is a homomorphism \(\mathcal N\to N_G(T)\), since all its relations were proved in Section 3. The copy of \(T\) has no collapse: its composite into \(N_G(T)\) is the original closed torus inclusion. The actual quotient \(N_G(T)/T\) is also \(\underline W\). To verify this last identification over the base, choose one simple-reflection word for each \(w\) and its product \(n_w\). RG04 Theorem 4.2 makes the quotient finite étale. The sections \(n_wT\) give a map from \(\coprod_w S\), which is an isomorphism on every geometric fibre by RG04 Theorem 4.1. On an affine base its algebra map is between finite projective modules and is an isomorphism on every residue-field fibre. Its cokernel vanishes by Nakayama; the surjection splits, and the same argument kills its finite projective kernel. Thus it is an isomorphism on the full base. The multiplication labels agree on fibres; their equality locus is open and closed, since the finite étale target has open-and-closed diagonal. It contains every point and hence is the entire source. This proves the group-sheaf identification with nilpotents included.

The map \(\mathcal N\to N_G(T)\) is surjective as a sheaf. A normalizer section locally has label \(w\), and multiplication by \(n_w^{-1}\) puts it in the kernel \(T\); these expressions glue on the clopen label fibres. If a section of \(\mathcal N\) maps to the identity, its image in \(\underline W\) is trivial, so fppf locally it belongs to \(T\). The unchanged injection of \(T\) then makes it trivial. Sheaf descent proves that the kernel is zero. Hence \(\mathcal N\simeq N_G(T)\). The datum map identifies this presentation with the target presentation: it preserves all torus characters, coroot signs and the types in (3.2). We obtain an actual normalizer isomorphism \(f_N\).

Every root can be transported from a simple root. For completeness, let \(\gamma=\sum c_i\alpha_i>0\). If it is not simple, the invariant form gives some \((\gamma,\alpha_i)>0\), because \((\gamma,\gamma)=\sum c_i(\gamma,\alpha_i)>0\). The reflection subtracts the positive integer \(\langle\gamma,\alpha_i^\vee\rangle\alpha_i\). It keeps a positive coefficient at another simple root, so remains positive, by the common-sign root expansion in RG04. Its integer height strictly decreases. Iteration reaches a simple root. A negative root is first transported from its positive opposite by the corresponding reflection. This is a finite integer argument independent of the characteristic.

Choose such a normalizer word to transport each pinned simple parameter to a parameter at \(\gamma\), and perform the same transport through \(f_N\) in the target. We check independence. Two choices reduce, after their Weyl words are compared, to a word carrying one simple root to another, with a remaining torus factor. Lemma 2.2 decomposes that word into standard rank-two factors, each carrying the current simple root to the next one; fixing factors are included. The complete conjugation table of Section 3 intertwines the parameter maps for each factor, with the indicated coefficients \(1\) or \(-1\). Linked negative parameters obey the same square rule. The remaining torus acts by the same root character in the two groups, since \(f_T\) comes from the given datum map. Thus both transports give the same root-group map. This proves every transport independence and every normalizer-conjugation identity, on all test schemes.

Lemma 2.1 places any independent pair in a conjugate standard rank-two subsystem. The paired root maps just constructed therefore preserve all relations (3.1); the commuting and equal-root cases are the weight-coordinate and additive identities. The frame maps preserve the linked rank-one formulas as well. These are exactly the hypotheses of the full cell-multiplicativity construction of Section 4. Use any ordered root-product coordinates of RG04 Section 5 to define

$$
f_\Omega(vtu)=f_-(v)f_T(t)f_+(u).
$$

The finite height collection there proves that the two unipotent maps are homomorphisms; the rank-one calculation and Lemma 4.2 prove normalizer equivariance on the whole common domain. The longest-element calculation proves mixed multiplicativity, and Lemma 4.1 extends \(f_\Omega\) uniquely to a group homomorphism \(f:G\to G'\).

Apply this construction to the inverse datum map. Its cell map is the inverse of \(f_\Omega\), so the two extended composites restrict to the identity on their big cells. Uniqueness in Lemma 4.1 makes each composite the identity on the whole group. Thus \(f\) is an isomorphism.

Any pinning-preserving isomorphism inducing the specified datum map has the same torus and simple parameters. The rank-one and normalizer formulas force its linked negative and transported root maps. Its cell map is therefore \(f_\Omega\); Lemma 4.1 makes it equal to \(f\). This proves the required bijection.

Group-algebra maps, root parameters, finite collection identities, Gauss identities and scheme morphism descent all commute with base change. The uniqueness just proved consequently gives compatibility after every base change. On a disconnected or non-quasi-compact base the datum map may have different locally constant values, with no finite-image assumption. Apply the construction on affine neighbourhoods where all finitely many lattice-generator images are fixed. On overlaps the datum maps agree, so uniqueness identifies the group maps; S04 Lemma A1.5 glues them and their inverses. This proves the theorem over the original \(S\). \(\square\)

The pinning is essential for uniqueness. Conjugation by an element of \(T\) preserves the torus and positive system and scales \(E_\alpha\) by \(\alpha(t)\). It preserves every frame precisely when it belongs to the centre.

## 6. Constructing the simply connected group in characteristic zero

The preceding supporting lesson [Lie proofs for the characteristic-zero group construction](AG-RG-S06.md) proves the rational Serre algebra and its integrable highest-weight modules. We use those complete proofs before constructing any algebraic group. The construction below includes its finite-presentation, group-law, geometric connectedness, Lie-algebra and root-datum arguments.

### The finite modules and their matrix parameters

Let \(\Phi\) be a reduced semisimple root system, \(Q=\mathbf Z\Phi\), and \(P\) its weight lattice. Write \(\alpha_i^\vee\) for the simple coroots and \(\omega_i\) for their dual fundamental weights, so \(P=\bigoplus_i\mathbf Z\omega_i\). S06 Theorem 6.2 supplies the rational split semisimple algebra

$$
\mathfrak g=\mathfrak n^-\oplus\mathfrak h\oplus\mathfrak n^+,
\qquad
\mathfrak h=\bigoplus_i\mathbf Qh_i,
$$

with exactly the prescribed one-dimensional root spaces and the simple rank-one brackets. It remains semisimple after every characteristic-zero field extension, as the whole proof there verifies.

For a dominant integral \(\lambda\), S06 Section 7 constructs the cyclic module with relations

$$
e_i v=0,\qquad
h_i v=\langle\lambda,\alpha_i^\vee\rangle v,\qquad
f_i^{\langle\lambda,\alpha_i^\vee\rangle+1}v=0.
$$

Its proof first uses the complete ordered-word theorem, S06 Theorem 1.A, to identify the induced module with \(U(\mathfrak n^-)\). The additional singular-vector submodules have no top \(\lambda\)-component. Thus this quotient has a nonzero cyclic vector and a one-dimensional top *before* finite-dimensional complete reducibility is applied.

The same proof establishes local nilpotence and Weyl symmetry before finiteness: the finite-on-each-vector operators \(\exp(e_i)\exp(-f_i)\exp(e_i)\) carry a weight to its simple reflection. Every weight \(\mu\) consequently satisfies

$$
\lambda-\mu\in Q^+,\qquad \mu-w_0\lambda\in Q^+.
$$

Write \(\lambda-w_0\lambda=\sum b_i\alpha_i\) and \(\lambda-\mu=\sum d_i\alpha_i\). Since \(\lambda\) and its Weyl translates occur, the \(b_i\) are nonnegative integers; the two inequalities say \(0\le d_i\le b_i\). There are only finitely many such tuples. For each fixed tuple, a negative-root PBW monomial has exponents \(m_\beta\) with \(\sum_{\beta>0}m_\beta\operatorname{ht}(\beta)=\sum d_i\). All positive heights are at least one, so only finitely many monomials occur. Each weight space, and hence the whole quotient, is finite-dimensional.

Now S06 Theorem 4.2 gives complete reducibility. If a proper submodule had a nonzero top component, it would contain the cyclic generator and would be the whole module. It therefore has top component zero. An invariant complement contains the generator, since projection preserves weights, and cyclicity makes that complement the entire module. Thus the proper submodule is zero. Denote the resulting irreducible module by \(L_{\mathbf Q}(\lambda)\). Tensoring its left-ideal presentation with any characteristic-zero field is exact; the top stays nonzero and one-dimensional, cyclicity stays true, and the same complement argument applies. These particular modules are absolutely irreducible.

Put \(V_i=L_{\mathbf Q}(\omega_i)\) and \(V=\bigoplus_iV_i\). They remain pairwise nonisomorphic after field extension: an isomorphism between top weights \(\lambda,\mu\) would force both \(\lambda-\mu\) and \(\mu-\lambda\) to belong to \(Q^+\), hence \(\lambda=\mu\). The representation \(\rho:\mathfrak g\to\operatorname{End}(V)\) is faithful by S06 Section 8: its kernel is a sum of simple diagram ideals, and an ideal containing index \(i\) acts nontrivially on \(V_i\), since \(h_i\) acts by one on its top.

Choose a rational root vector \(e_\alpha\) in each root line, with \(e_{\alpha_i}=e_i\) and \(e_{-\alpha_i}=f_i\) for the linked simple choices. It raises a weight by \(\alpha\). The finite weight set contains no arbitrarily long sequence \(\mu+j\alpha\), so \(E_\alpha=\rho(e_\alpha)\) is nilpotent. The finite matrix series

$$
x_\alpha(u)=\exp(uE_\alpha)
=\sum_{j\ge0}\frac{u^jE_\alpha^j}{j!}
$$

is a morphism over \(\mathbf Q\) on every test algebra. Multiplying two such series and collecting the coefficient of \(E_\alpha^j\) gives the binomial formula, hence \(x_\alpha(u)x_\alpha(v)=x_\alpha(u+v)\) and inverse \(x_\alpha(-u)\).

**Lemma 6.1 (polynomial rank-one actions).** The irreducible finite-dimensional complex \(\mathfrak{sl}_2\)-modules are \(\operatorname{Sym}^n(\mathbf C^2)\), for \(n\geq0\), with weights \(n,n-2,\ldots,-n\); every finite-dimensional module is their direct sum. Every finite-dimensional rational representation of \(\mathfrak{sl}_2\) integrates to a polynomial representation of \(\operatorname{SL}_{2,\mathbf Q}\). On its summands of highest weight \(n\), the upper and lower root groups act by \(\exp(xe)\) and \(\exp(xf)\), and the diagonal torus acts on weight \(m\) by \(z^m\).

**Proof.** The trace-zero algebra with basis \(e,f,h\) and brackets \([h,e]=2e\), \([h,f]=-2f\), \([e,f]=h\) is simple in characteristic zero. An ideal is stable under \(\operatorname{ad}h\), whose three eigenvalues \(2,-2,0\) are distinct. Polynomial projections isolate any nonzero basis component, and bracketing that component with the other generators gives all three. Thus S06 Theorem 4.2 applies to its finite-dimensional modules.

Let \(W_n=\operatorname{Sym}^n(\mathbf Q^2)\), with basis the degree-\(n\) monomials in \(u,v\). On every \(\mathbf Q\)-algebra, the matrix \(\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\) acts by

$$
u\longmapsto au+cv,\qquad v\longmapsto bu+dv.
$$

The resulting matrix entries are polynomials in \(a,b,c,d\). Composing the substitutions gives matrix multiplication, the identity substitution is the identity, and the substitution for the inverse matrix is inverse. For determinant one, the inverse entries are again polynomials in these four entries. This defines a group-scheme representation. Its differential is

$$
e=u\partial_v,\qquad f=v\partial_u,\qquad
h=u\partial_u-v\partial_v.
$$

Upper and lower unipotent substitutions give the finite Taylor series \(\exp(xe)\), \(\exp(xf)\), and the diagonal multiplies \(u^{n-j}v^j\) by \(z^{n-2j}\). All these are identities over every \(\mathbf Q\)-algebra.

In a nonzero irreducible complex module choose an \(h\)-eigenvector. Applying \(e\) repeatedly raises its eigenvalue by two; finitely many eigenvalues force a last nonzero vector \(w\), with \(ew=0\), \(hw=\lambda w\). Commutator induction gives

$$
hf^jw=(\lambda-2j)f^jw,\qquad
ef^jw=j(\lambda-j+1)f^{j-1}w.
$$

For the second induction step, commuting past one further \(f\) adds \(\lambda-2j\) to the preceding coefficient and gives \((j+1)(\lambda-j)\). Lowering also ends, since nonzero \(f^jw\) have distinct eigenvalues. If \(f^nw\ne0\) and \(f^{n+1}w=0\), the second equation at \(n+1\) gives \((n+1)(\lambda-n)f^nw=0\), hence \(\lambda=n\). The string spans a nonzero invariant submodule and is therefore the whole irreducible module. The map \(f^ju^n\mapsto f^jw\), \(0\le j\le n\), identifies its operators with those of \(W_n\). These vectors are a basis: the coefficients of \(f^ju^n\) are \(n!/(n-j)!\ne0\).

Conversely \(W_n\) is irreducible. Polynomial projections in its distinct \(h\)-eigenvalues split any invariant subspace into weight components. Repeated \(e\) takes any nonzero such component to \(u^n\), with nonzero coefficients in characteristic zero, and repeated \(f\) generates all basis vectors. Complete reducibility now proves the decomposition of every finite-dimensional complex module.

For a rational module \(M\), put \(K_n=\ker e\cap\ker(h-n)\). Kernels of these rational linear maps commute with field extension. Over \(\mathbf C\), only finitely many \(K_n\), with \(n\ge0\), occur. The string equations give an equivariant map

$$
\bigoplus_{n\ge0}W_n\otimes_{\mathbf Q}K_n\longrightarrow M,
\qquad f^ju^n\otimes w\longmapsto f^jw.
$$

The relation \(f^{n+1}w=0\) follows over \(\mathbf C\) from its decomposition, and hence over \(\mathbf Q\). That decomposition makes the displayed map an isomorphism after extension. A rational kernel or cokernel with zero faithful field extension is zero, so it is an isomorphism over \(\mathbf Q\). Transport the polynomial actions on its finitely many summands. Their differentials, diagonal weights and unipotent exponentials are the prescribed ones. This proves every assertion of the lemma. \(\square\)

### The closed group generated by the matrices

Let \(T=D_{\mathbf Q}(P)\) act on \(V_\mu\) by \(\mu\). This is a closed torus embedding. Indeed choose a weight basis containing the fundamental highest vectors. Their diagonal matrix entries restrict to the basis characters \(\omega_i\), and the corresponding inverse-matrix entries restrict to their inverses. Inverse entries are regular on \(\operatorname{GL}(V)\), by the adjugate formula. These restricted functions generate \(\mathbf Q[P]\), so the coordinate map onto the torus algebra is surjective, as also proved in S06 Section 8.

If \(\Phi\) is empty, then \(P=\mathfrak g=V=0\); take \(G=1\), with its empty pinning and datum. Henceforth suppose \(\Phi\ne\varnothing\).

Let \(\Gamma\subset\operatorname{GL}(V)(\mathbf Q)\) be the subgroup generated by \(T(\mathbf Q)\) and all \(x_\alpha(\mathbf Q)\). In \(B=\mathbf Q[\operatorname{GL}(V)]\), let \(I\) be the ideal of functions vanishing at every element of \(\Gamma\), and put \(C=B/I\), \(G=\operatorname{Spec}C\). Explicitly \(B=\mathbf Q[m_{ab},z]/(z\det(m_{ab})-1)\), so its presentation is finite. Evaluation embeds \(C\) into the \(\mathbf Q\)-valued functions on \(\Gamma\), so \(I\) is radical.

This closed subscheme is of finite presentation. Here is the algebra input explicitly. A field is Noetherian. If \(R\) is Noetherian and \(J\subset R[x]\), let \(L_n\) be the ideal of coefficients of \(x^n\) in elements of \(J\) of degree at most \(n\). Multiplication by \(x\) gives \(L_n\subset L_{n+1}\). This chain stabilizes: its union is an ideal with finitely many generators, all lying at a single finite stage. Choose polynomials furnishing generators of each \(L_n\) up to the stabilizing stage \(N\). For a polynomial of degree \(m\ge N\), subtract multiples of \(x^{m-N}\) times the chosen degree-\(N\) polynomials to remove its leading coefficient. For \(m<N\), use the chosen degree-\(m\) polynomials. Induction on degree shows that this finite collection generates \(J\). Thus \(R[x]\) is Noetherian. Induct on the variables. Quotients preserve this property by taking ideal inverse images; localization preserves it because any localized ideal is generated by the extension of its contraction. Hence \(B\), a localization of a finite polynomial algebra over \(\mathbf Q\), is Noetherian. The ideal \(I\) is finitely generated, and its quotient is finitely presented.

We prove the group law on this scheme rather than assume it from a point closure. The set \(\Gamma\times\Gamma\) is schematically dense in \(G\times G\). To see this, write an element of \(C\otimes C\) as \(\sum a_i\otimes b_i\), with the \(b_i\) linearly independent. The vectors \((b_i(\gamma))_i\), \(\gamma\in\Gamma\), span the full finite-dimensional coordinate space. Otherwise a nonzero linear functional would make a nontrivial linear combination of the \(b_i\) vanish on all of \(\Gamma\), contradicting the evaluation injection. Choose finitely many such vectors as a basis. If the tensor vanishes at every pair, evaluation at this chosen second-variable basis makes each \(a_i\) vanish at every \(\gamma\), so \(a_i=0\). This proves the injection into functions on \(\Gamma\times\Gamma\).

Multiplication in \(\operatorname{GL}(V)\) pulls every element of \(I\) to a function zero on \(\Gamma\times\Gamma\), so it factors through \(G\times G\to G\). Inversion pulls \(I\) into \(I\), because \(\Gamma\) is a subgroup. The identity belongs to \(G\). All group axioms are the restrictions of the matrix identities. Thus \(G\) is an affine finite-presentation group scheme over \(\mathbf Q\).

The given torus and additive matrix morphisms factor through \(G\). A Laurent polynomial vanishing on \((\mathbf Q^\times)^r\) is zero: multiply by a monomial, then induct on the variables using the bound of the degree on the number of roots of a nonzero one-variable polynomial. The same argument applies to the ordinary polynomial parameter of \(x_\alpha\). Pullbacks of \(I\) along these morphisms are consequently zero.

S08 Theorem G.3.4, with its complete Cartier proof, makes \(G\) smooth. It is geometrically connected. For any field extension \(k/\mathbf Q\), the same rational points \(\Gamma\) are schematically dense in \(G_k\): write a function as a finite sum \(\sum c_i a_i\) with the \(c_i\in k\) linearly independent over \(\mathbf Q\). Its values at \(\Gamma\) have \(a_i(\gamma)\in\mathbf Q\); vanishing forces each \(a_i(\gamma)=0\), hence each \(a_i=0\). Over an algebraic closure, the smooth-component argument of S08 Theorem G.4.2 makes the identity component an open-and-closed subgroup. The connected torus and additive images lie in it. Their rational products contain \(\Gamma\), so schematic density makes that component all of \(G_k\).

Each root parameter is a closed immersion into \(G\). For a nonzero nilpotent \(E=E_\alpha\) of index \(d\), the matrices \(1,E,\ldots,E^{d-1}\) are linearly independent. In a proposed relation take the smallest nonzero power coefficient; its remaining polynomial factor has nonzero constant term and is invertible at \(E\), forcing that power of \(E\) to be zero, contrary to its index. A rational linear functional on matrices can therefore take value one on \(E\) and zero on the other listed powers. Its value on \(\exp(uE)\) is exactly \(u\). Matrix-entry functions consequently surject onto \(\mathbf Q[u]\), proving the closed immersion, including on nonreduced test algebras.

### Its Lie algebra, centre and root datum

Put \(\mathfrak l=\rho(\mathfrak g)\subset\operatorname{End}(V)\). Its matrix normalizer is closed: on a basis of \(\mathfrak l\), require the images under conjugation by \(g\) and by \(g^{-1}\) to have zero components in the quotient space \(\operatorname{End}(V)/\mathfrak l\). These are finitely many regular equations on \(\operatorname{GL}(V)\), and both conditions give equality of the submodules after every test-algebra extension. The torus preserves \(\mathfrak l\) by its root weights. For a root exponential, binomial expansion gives

$$
\exp(uE_\alpha)\rho(x)\exp(-uE_\alpha)
=\rho\left(\sum_{j\ge0}\frac{u^j(\operatorname{ad}e_\alpha)^j x}{j!}\right).
$$

Both sides are finite sums: nilpotence on the finite root-weight decomposition bounds the adjoint sum. Thus these generators normalize \(\mathfrak l\) as schemes. Their rational subgroup \(\Gamma\) does too, and its defining density puts \(G\) in this closed normalizer.

At the identity, conjugation by \(1+\varepsilon A\), \(\varepsilon^2=0\), changes \(\rho(x)\) by \(\varepsilon[A,\rho(x)]\). Thus a tangent vector \(A\in\operatorname{Lie}(G)\) satisfies \([A,\mathfrak l]\subset\mathfrak l\). Faithfulness defines a derivation \(D_A\) of \(\mathfrak g\); the derivation equation follows directly by expanding the matrix Jacobi identity.

For clarity, the entire inner-derivation calculation of S06 Proposition 3.3 is as follows. Its Proposition 3.1 makes the Killing form \(\kappa\) nondegenerate. Choose \(z\) with \(\kappa(z,x)=\operatorname{tr}(D_A\operatorname{ad}x)\), and set \(E=D_A-\operatorname{ad}z\). Then \(\operatorname{tr}(E\operatorname{ad}x)=0\). The derivation identity gives \([E,\operatorname{ad}x]=\operatorname{ad}(Ex)\), and cyclic trace gives

$$
0=\operatorname{tr}(E\operatorname{ad}[x,y])
=\operatorname{tr}([E,\operatorname{ad}x]\operatorname{ad}y)
=\kappa(Ex,y).
$$

Hence \(E=0\), so

$$
A\in\rho(\mathfrak g)+\operatorname{End}_{\mathfrak g}(V).
\tag{6.1}
$$

Over an algebraic closure \(k\), the commutant is one scalar on each \(V_i\). A nonzero map between two irreducible summands has zero kernel and full image and would be an isomorphism; their distinct top weights rule this out. On one irreducible summand, subtract an eigenvalue of a commuting endomorphism. Its nonzero kernel is invariant and hence the whole summand, so the endomorphism is scalar. This proves the full commutant assertion.

Every generator has determinant one on each \(V_i\). For a root exponential, a basis adapted to kernels of powers of its nilpotent generator makes the matrix upper triangular with all diagonal entries one. For \(T\), let \(\sigma_i\in P\) be the sum of its weights with multiplicities. Its pairing with every simple coroot is the trace of \(h_j\) on \(V_i\). This trace is zero: S06 Proposition 3.2 gives \(\mathfrak g=[\mathfrak g,\mathfrak g]\), and a matrix commutator has trace zero. The simple coroots are the dual basis of \(P\), so \(\sigma_i=0\) in the lattice. Thus \(G\subset\prod_i\operatorname{SL}(V_i)\), by the same defining density.

For a tangent matrix, \(\det(1+\varepsilon A_i)=1+\varepsilon\operatorname{tr}(A_i)\). Each block trace is therefore zero. In (6.1) the block trace of \(\rho(z)\) is zero by perfectness, and a scalar \(c_i\) has trace \((\dim V_i)c_i\). Characteristic zero makes every \(c_i=0\). This proves \(\operatorname{Lie}(G_k)\subset\rho(\mathfrak g_k)\). Conversely the torus tangent vectors give \(\rho(\mathfrak h_k)\), and each additive parameter has tangent \(E_\alpha\). They span the whole algebra. Consequently

$$
\operatorname{Lie}(G_k)=\rho(\mathfrak g_k).
$$

The rational equality follows as well: tangent equations are rational linear equations, and a kernel or quotient with zero faithful field extension is zero.

The group is reductive. Let \(N\subset G_k\) be a smooth connected normal unipotent subgroup. Use a faithful closed unitriangular realization of \(N\), as in the unipotent convention of RG01 Lemma 2.A. Its Lie algebra is nilpotent: commutators of strictly upper triangular matrices lie in successive powers of that associative algebra, which eventually vanish. Normality makes \(\operatorname{Lie}N\) an ideal of \(\operatorname{Lie}G_k\); differentiating the conjugation identity gives \([X,Y]\in\operatorname{Lie}N\) for \(X\in\operatorname{Lie}G_k\), \(Y\in\operatorname{Lie}N\). A nilpotent Lie algebra is solvable, since its successive derived brackets have lengths at least \(2^j\). Semisimplicity of \(\mathfrak g_k\) therefore forces \(\operatorname{Lie}N=0\).

Smoothness makes every tangent rank of \(N\) zero, by translation. The pointwise differential criterion and field classification in AG-FSE, *Unramified morphisms*, Theorems 3.2 and 3.3, make it a disjoint union of reduced points over \(k\). Connectedness leaves only the identity point. Thus no nontrivial such \(N\) exists, which is precisely geometric reductivity in RG01 Section 1.

The closed torus \(T\) is geometrically maximal. The exhaustive Lie grading just obtained has zero-weight part \(\rho(\mathfrak h_k)=\operatorname{Lie}T_k\) and nonzero characters exactly \(\Phi\). If a torus \(T'\) contains \(T_k\), its tangent vectors centralize \(T_k\), so they lie in this zero-weight part. The reverse tangent inclusion comes from \(T_k\subset T'\); their ranks agree. Over \(k\) both tori are split. Their closed inclusion induces a surjection of free character lattices, by exponent-basis comparison in their group algebras, as in AG-GS Theorem 2.2. Equal ranks give a rank-zero free kernel, hence zero. The inclusion is an isomorphism. This proves maximality on every geometric fibre.

Now apply the complete centre calculation in RG03 Section 1 to this reductive group and maximal torus. It gives

$$
Z(G)=D_{\mathbf Q}(P/Q).
$$

This is finite. In the fundamental-weight basis the simple roots form an integral square matrix with nonzero determinant \(d\), since they span the rational root space. The adjugate identity gives \(dP\subset Q\); therefore \(P/Q\) is a quotient of the finite group \(P/dP\). Its group algebra has the finite exponent basis, so the diagonalizable centre is finite over \(\mathbf Q\). The radical formula in RG03 Section 1 then gives trivial radical and proves that \(G\) is semisimple. This also identifies its entire centre as a scheme.

The closed parameters \(x_\alpha\) have the required characters and identity differential on their root lines. RG03 Theorem 4.1 identifies them with the canonical root groups of \(G\). For a simple root, Lemma 6.1 integrates the \((e_i,f_i,h_i)\)-action on \(V\) to \(\operatorname{SL}_2\). Its image lies in \(G\) on all test schemes: on the open where the upper-left matrix entry \(a\) is invertible, the Gauss decomposition is a product of its two root parameters and its diagonal. The diagonal acts on weight \(\mu\) by \(z^{\langle\mu,\alpha_i^\vee\rangle}\), hence is the stated cocharacter of \(T\). On the other open \(D(c)\), left multiplication by \(\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\), itself a product of the two root matrices, reduces to \(D(a)\). These opens cover because \(ad-bc=1\) makes \((a,c)\) the unit ideal. Thus the whole polynomial action factors through \(G\).

The linked Gauss formula in RG03 Theorem 7.1 identifies that diagonal cocharacter with the canonical group coroot. For every root, transport a simple root by a Weyl word, using the finite height descent in Section 5. RG04 Theorem 2.1 gives the action of each integrated simple representative on \(P\) by the prescribed simple reflection. Conjugating the linked Gauss identity and applying its uniqueness in RG03 Theorem 7.1 transports each coroot with its root. Successive conjugation therefore gives precisely the prescribed \(\Phi^\vee\). Consequently

$$
\mathcal R(G,T)=(P,\Phi,P^*,\Phi^\vee).
\tag{6.2}
$$

Its simple root frames are \(E_{\alpha_i}\), so \(G\) is pinned split. Since the \(\omega_i\) are the dual basis of the simple coroots, \(P^*\) is exactly the coroot lattice. This is the simply connected semisimple datum. The empty-root case specified above has the same conclusion. Everything was constructed over \(\mathbf Q\), before any integral model, and all polynomial identities hold on arbitrary commutative \(\mathbf Q\)-algebras.

## 7. Integral coordinates and a partial group law

Continue with the simply connected group of Section 6. Choose its simple-root pinning. Choose a frame in every other root line by transporting a simple frame with a word in the \(n_\alpha\), and use the dual frame in the negative line. Such frames form a **Chevalley system**: a simple representative carries each chosen root frame to the chosen frame of the reflected root, up to a sign.

Here is why the signs really are integral and independent of the field. Compare two transport words. Lemma 2.2 reduces their comparison to the conjugation tables in Section 3 and torus factors arising from (1.2) and (3.2). Those tables have coefficients \(1\) or \(-1\). The torus factors lie in \(T[2]\); the representatives normalize \(T[2]\), and every root has value \(1\) or \(-1\) on it. Moving such factors through a word changes only these signs. There is no assertion that \(T[2]\) centralizes the representatives.

It follows that all root reordering polynomials have integer coefficients. Indeed, Lemma 2.1 moves a pair into a standard rank-two system; the chosen frames there differ from those of Section 3 only by signs. Its commutator formulas are (3.1). Repeatedly apply these formulas in an order refining root height. A new factor has greater height than the factors it corrects, so reordering terminates. For the negative roots use negative height. Thus the positive and negative unipotent groups extend to groups \(U^+_{\mathbf Z},U^-_{\mathbf Z}\), each an affine space in its ordered root coordinates. Their multiplication and inverse are triangular integral polynomials. Associativity holds because it is a polynomial identity true over \(\mathbf Q\).

Changing the root order still gives a polynomial isomorphism: reorder using the same relations, and reorder back. Both compositions are the identity over \(\mathbf Q\), hence over \(\mathbf Z\). Let

$$
T_{\mathbf Z}=D_{\mathbf Z}(P),\qquad
X=U^-_{\mathbf Z}\times T_{\mathbf Z}\times U^+_{\mathbf Z}.
\tag{7.1}
$$

This smooth affine scheme has geometrically irreducible fibres. The torus acts on each root coordinate through the prescribed character. We write \(e=(1,1,1)\).

We next give the partial conjugations on \(X\). For a simple root \(\alpha\), reorder the coordinates as

$$
\left(\prod_{\gamma\in\Phi^+\setminus\{\alpha\}}x_{-\gamma}(v_\gamma)\right)
x_{-\alpha}(v)\,t\,x_\alpha(u)
\left(\prod_{\gamma\in\Phi^+\setminus\{\alpha\}}x_\gamma(u_\gamma)\right).
$$

Put \(a=\alpha(t)\) and \(D=1+auv\). On the principal open \(D\ne0\), conjugation by \(n_\alpha\) has the integral cell formula obtained by reflecting and changing signs in the outer root factors, and replacing the middle three factors by

$$
x_{-\alpha}\!\left(\frac{-au}{D}\right)
\alpha^\vee(D)s_\alpha(t)
x_\alpha\!\left(\frac{-av}{D}\right).
\tag{7.2}
$$

This is exactly the rank-one Gauss identity applied after conjugation. It fixes the identity, acts by \(s_\alpha\) on the torus, and is defined on each individual root group.

One can check the torus and denominator directly for \(\operatorname{SL}_2\). Conjugating \(y(v)h(z)x(u)\) by \(\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\) gives an upper-left entry \(z^{-1}(1+z^2uv)\). Thus the torus factor is \(h(z^{-1}(1+z^2uv))\), as in (7.2).

Choose a reduced word for the longest Weyl element \(w_0\), and compose these partial conjugations along that word. Call the resulting map \(h:V\to X\). Reverse the word and use inverse representatives to obtain \(h':V'\to X\). These are inverse rational maps, and

$$
U^-,T,U^+\subset V\cap V',\qquad
h(U^\pm)=U^\mp,\quad h(T)=T.
\tag{7.3}
$$

To justify that the whole unipotent subgroups, and not just the separate root axes, are in the domains, consider an intermediate conjugate of \(U^+\). Its roots form a positive system. Reordering its root factors into negative and positive order never uses opposite roots: every root created by a commutator is still positive in that system. It therefore needs only the integral reordering polynomials, with torus component one. In (7.2) at most one of the two opposite-root coordinates is nonzero, so the denominator is one. The same argument applies to \(U^-\) and the inverse word. This proves (7.3). Equality \(h'h=1\) on its common domain follows over \(\mathbf Q\) and then over \(\mathbf Z\), because that domain is flat.

For \(x=(v,t,u)\) and \(x'=(v',t',u')\), impose the open condition

$$
(h(u),1,h(v'))\in V'.
$$

Write \(h'(h(u),1,h(v'))=(v'',t'',u'')\). Define

$$
m(x,x')=
\bigl(v(t v''t^{-1}),\ tt''t',\ (t'^{-1}u''t')u'\bigr).
\tag{7.4}
$$

The condition and formula are integral; over \(\mathbf Q\) they say precisely that \(ux'_{-}=uv'\) has been rewritten in the cell before multiplying the outer factors. The domain contains \(e\times X\), \(X\times e\), \(B^-\times X\), \(X\times B^+\), and the pairs within \(U^\pm\) or \(T\). Here \(B^-=U^-T\) and \(B^+=TU^+\). Partial inversion is obtained on the open where the following expression exists:

$$
\iota(v,t,u)=h'\bigl(h(u^{-1}),h(t^{-1}),h(v^{-1})\bigr).
\tag{7.5}
$$

This domain contains \(T,U^-,U^+\). Associativity on common domains, the identity rule, and the inverse rule hold as integral identities: they hold in the characteristic-zero group, and the domains in question are flat open subschemes of products of \(X\).

For the next construction we need open partial translations with dense domains and images in every fibre. Write \(D\subset X\times_{\mathbf Z}X\) for the multiplication domain just constructed. Its two universal translation maps are

$$
(x,y)\longmapsto(x,m(x,y)),\qquad
(x,y)\longmapsto(m(x,y),y).
\tag{7.6}
$$

Both maps are local isomorphisms along both identity axes. At \((e,y)\), the first map has identity differential in the \(y\)-direction; at \((x,e)\), the second has identity differential in the \(x\)-direction. We give the other two assertions explicitly. Factor the universal \(x\) into its ordered negative root factors, torus factor and ordered positive root factors. For left translation, apply these factors from right to left to successive suffixes, starting at \(e\). A positive factor and its suffix are in \(U^+\times U^+\); a torus or negative factor uses \(B^-\times X\). Translation by the inverse factor is defined at the resulting suffix: the positive case stays in \(U^+\), and the other cases again use \(B^-\times X\). On the common open neighbourhoods the two maps are inverse. Indeed their compositions are the identity over \(\mathbf Q\), and the coordinate rings of their open domains are \(\mathbf Z\)-flat, so equality holds over \(\mathbf Z\). Composing gives left translation by \(x\) as a local isomorphism at \(e\). Associativity identifies this composition with the existing \(m(x,-)\) on their common neighbourhood of \(e\). For right translation, start at \(e\), apply factors from left to right to successive prefixes, and use \(U^-\times U^-\) or \(X\times B^+\) and the inverse factors. This gives right translation by \(x\) as a local isomorphism at \(e\). All the points, factors and neighbourhoods here use universal coordinates; thus the assertions hold after every base change, rather than only at rational points.

The same inverse-factor argument works at every pair in \(U^-\times U^-\), \(U^+\times U^+\) and \(T\times T\): the intermediate products and inverse products stay in that subgroup. The two maps in (7.6) are therefore étale at all those pairs as well. Let \(D^\circ\subset D\) be the intersection of their étale loci. It contains both identity axes and those three whole pair subschemes. Retain \(m\) on \(D^\circ\).

The two restricted maps in (7.6) are open immersions. Here their sources and targets are integral normal Noetherian schemes. Their coordinate algebras are localizations of finite polynomial algebras over \(\mathbf Z\). The complete integer-factorization proof in S04 Lemma B1.1 and the reduced-fraction proof in Lemma P0.5 make \(\mathbf Z\) normal. S04 Corollary B1.2 gives polynomial normality by induction on the variables, and Lemma P0.3 gives normality after localization. Every integer ideal is principal by the least-positive-generator argument in S04 Lemma P0.10; thus \(\mathbf Z\) is Noetherian, and the complete leading-coefficient proof in Section 6 makes these polynomial algebras and their localizations Noetherian. These properties pass to their open subschemes. Each restricted map is separated, since it is a morphism between separated \(\mathbf Z\)-schemes; it is quasi-finite, since it is étale and its Noetherian open domain is quasi-compact. It is birational: over \(\mathbf Q\) it is the restriction of multiplication in the group constructed in Section 6, whose big cell is \(X_{\mathbf Q}\), so the generic translation has the inverse supplied by the group law. The exact normal birational consequence, [S04 Corollary D7.4](AG-RG-S04.md), consequently applies to each map over \(\mathbf Z\). Denote their open images by \(D_{13},D_{23}\).

Every slice of each of \(D^\circ,D_{13},D_{23}\) over either coordinate projection is a nonempty open in the corresponding geometrically irreducible fibre of \(X\), and hence is dense. For \(D^\circ\) this follows from its two identity axes. The first translation sends \((x,e)\) to \((x,x)\) and \((e,y)\) to \((e,y)\), so both types of slices of \(D_{13}\) have a point. The second sends these axes to \((x,e)\) and \((y,y)\), giving the same conclusion for \(D_{23}\). These are statements on geometric fibres and remain true after arbitrary base change. The graph
\[
W=\{(x,y,m(x,y)):(x,y)\in D^\circ\}\subset X^3
\]
therefore projects isomorphically onto each of the three open subschemes \(D^\circ,D_{13},D_{23}\subset X^2\), with the required dense slices. Associativity, identity and partial inversion remain the already verified integral identities on common domains. This is the strict partial group law used below. Its restriction to each torus or root subgroup still contains the entire multiplication law.

## 8. Completing a strict partial group law

We give the construction rather than assuming a group already exists. This is the translation method of Weil and Artin; the algebraic-space quotient in the final step is the exact bootstrap prerequisite identified below.

**Lemma 8.1.** Suppose \(X/S\) is smooth, separated and of finite presentation, with geometrically irreducible nonempty fibres. Suppose \(X\) has a strict associative partial group law, an identity section, and partial inversion, with the translation maps defined and invertible locally along both identity axes. Then there is a unique smooth separated group algebraic space \(K/S\) of finite presentation containing \(X\) as a fibrewise dense open and extending its partial group law. Formation of \(K\) commutes with base change.

**Proof.** Write \(D_{12},D_{13},D_{23}\subset X\times_SX\) for the three open images of the strict multiplication graph, ordering the pair for \(D_{23}\) as output followed by second input. Projection to any pair is an isomorphism from that graph. Fixing either entry in any pair leaves a fibrewise dense open in \(X\). In particular the left and right partial translations are isomorphisms between fibrewise dense opens. Denote the inverse of the right-translation pair map by partial right division:
\[
q:D_{23}\longrightarrow X,\qquad q(z,b)=a\ \Longleftrightarrow\ (a,b,z)\in W.
\]
The pair order here is \((z,b)\); it is obtained from the usual \((b,z)\) projection by exchanging its two entries.

**Germs and their descent.** On an \(S\)-scheme \(R\), take isomorphisms between fibrewise dense opens of \(X_R\), identifying two when they agree on a fibrewise dense common open. Intersections of finitely many such opens are dense in every geometric fibre. Composition is defined on the inverse image of the intersection of the intermediate image and domain; inversion reverses a representative. These constructions give a group of germs and commute with pullback.

Whenever two representatives of the same germ have a common domain, they agree on that entire domain. Apply [S08 Lemma G.3.5](AG-RG-S08.html#universal-schematic-density) to the common open: it is smooth, and each nonempty geometric fibre is an open of a geometrically irreducible fibre of \(X\). Restrict the base to its open image when necessary. The separated target \(X_R\) and universal schematic density give equality, including on nonreduced tests. This also proves that the maps and their inverse maps glue across compatible representative domains.

The germs are an fppf sheaf. To prove effectivity, represent a compatible germ over a covering \(R'\to R\) by \(h':A'\xrightarrow{\sim}B'\), with both opens fibrewise dense. A covering family is treated by the disjoint union of its members. Let \(A,B\subset X_R\) be their images. They are open because flat locally finitely presented maps are universally open, with the complete proof in [AG-FSE, *Flat morphisms*, Theorem 3.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-FSE/flat-morphisms.html#3-what-flatness-does-to-the-topology). The maps \(A'\to A,B'\to B\) are surjective flat and locally finitely presented. The two representatives agree on \(A'\times_{X_R}A'\): compatibility gives equality as germs on the base overlap, and the preceding density argument gives equality on the entire intersection of domains. [S04 Lemma A1.5](AG-RG-S04.md) therefore descends \(h'\) to \(A\to X_R\). Its image is in \(B\), as can be checked after the covering. Descend its inverse to \(B\to A\); both inverse equations hold after the covers and hence before them. The opens \(A,B\) are fibrewise dense, since their fibres contain the images of the dense covering fibres after a residue-field extension. Thus this is the descended germ. The same whole-common-domain argument and morphism descent prove uniqueness. Write \(\operatorname{Bir}(X)\) for this sheaf. No assertion about base change of maximal representative domains has been used.

**Translation germs and one-point faithfulness.** For \(a\in X(R)\), let \(L_a\) and \(R_a\) be its partial left and right translation germs. Associativity gives
\[
L_aR_b=R_bL_a,\qquad L_aL_b=L_{m(a,b)}
\]
when the displayed partial product exists. For these germ equalities the composed domains are fibrewise dense: each translation is an isomorphism between dense opens, and finite intersections stay dense. Associativity gives equality on their common triple-product domain, and the preceding schematic-density argument extends it over each whole common domain. Let \(K\) be the subgroup sheaf of \(\operatorname{Bir}(X)\) generated by the \(L_a\); concretely its sections are fppf locally finite words in these germs and their inverses. They commute with every \(R_b\), after every test-scheme extension.

If a representative of \(g\in K(R)\) is defined at a section \(x\) and satisfies \(g(x)=x\), then \(g=1\). To see this on all tests, let \(b\) vary in \(X_R\). Retain the open on which \(xb\) exists and belongs to the chosen domain of \(g\). It is fibrewise dense: \(L_x\) is a dense-open isomorphism, and its image meets that domain densely. On this open the two compositions \(gR_b\) and \(R_bg\) are both defined at \(x\). Their equality on the whole common domain gives
\[
g(xb)=g(x)b=xb.
\]
The points \(xb\) range over a fibrewise dense open via \(L_x\), so \(g\) is the identity germ. This argument uses the universal \(b\), rather than a choice of rational points.

The map \(j:X\to K\), \(a\mapsto L_a\), is injective. For \(L_a=L_b\), choose \(z\) in the intersection of their dense domains fppf locally; that intersection is smooth and surjective over \(R\). Then \(az=bz\), and the open-immersion right-translation pair map makes \(a=b\). Morphism descent gives the original equality on \(R\).

**The open chart.** This injection is representable by open immersions. Fix \(g\in K(R)\) and one dense-open representative \(g:A_g\to B_g\). Let
\[
E_g=\{z\in A_g:(g(z),z)\in D_{23,R}\},\qquad
O_g=\operatorname{image}(E_g\to R).
\]
Both are open; the latter follows from smooth openness. On \(E_g\) put \(a=q(g(z),z)\). The germ \(L_a^{-1}g\) is defined at \(z\) and fixes it, so one-point faithfulness gives \(L_a=g\). Injectivity of \(j\) makes these \(a\)'s agree on \(E_g\times_{O_g}E_g\). The smooth surjection \(E_g\to O_g\), together with S04 Lemma A1.5, descends them to a unique section \(a\in X(O_g)\) with \(j(a)=g\).

This open has the required property after every \(R'\to R\). If \(g_{R'}=L_a\), intersect the pullback of the fixed original domain \(A_g\) with the partial left-translation domain of \(a\). This is fibrewise dense and smooth-surjective over \(R'\). On it \(g(z)=az\), by equality of representatives on their whole common domain; hence \((g(z),z)\in D_{23}\), and \(a=q(g(z),z)\). The cover therefore factors through \(E_g\), so \(R'\to R\) factors through \(O_g\). Conversely a map through \(O_g\) pulls back its unique section. Thus
\[
R\times_KX=O_g
\]
as functors on all schemes. In particular this proves the open-immersion claim without assuming that a maximal domain commutes with base change.

**Translated charts and the quotient.** A translate \(j_g=(g\cdot)j_R:X_R\to K_R\) is again a representable open immersion of sheaves. Define the intersection chart
\[
\Omega_g=X_R\cap g^{-1}X_R.
\]
Precisely, it is the inverse image of the open subfunctor \(j_R(X_R)\) under \(j_g\). It is an open subscheme of \(X_R\), and its formation commutes with every base change by this fibre-product definition. The corresponding unique section in \(X_R\) gives an isomorphism
\[
\gamma_g:\Omega_g\xrightarrow{\sim}\Omega_{g^{-1}},\qquad
j(\gamma_g(b))=g\,j(b).
\]

Every dense-open representative \(g:A_g\to B_g\) maps into this chart. Indeed on the scheme \(A_g\), take its universal section \(b\) and put \(a=g(b)\). The local identity-axis hypothesis makes \(L_b\) defined and invertible near \(e\), with \(L_b(e)=b\), and gives the same assertion for \(L_a\). Thus \(L_a^{-1}gL_b\) is defined at \(e\) and fixes it. One-point faithfulness gives \(gL_b=L_a\). This is exactly \(b\in\Omega_g\) and \(\gamma_g(b)=g(b)\). Consequently \(\Omega_g\) is fibrewise dense and smooth-surjective over \(R\), including after arbitrary base change. We have not identified it with a maximal domain of an arbitrary birational map; its represented intersection is what proves the required base-change property.

It follows that every section of \(K\) is fppf locally
\[
g=L_aL_b^{-1}\qquad(a,b\in X).
\tag{8.1}
\]
Choose \(b\) in \(\Omega_g\) on its smooth covering and let \(a=\gamma_g(b)\). More precisely the fibre over \(g\) of
\[
\delta:X\times_SX\longrightarrow K,\qquad
(a,b)\longmapsto L_aL_b^{-1}
\tag{8.2}
\]
is the graph of \(\gamma_g\), with coordinates \((a,b)=(\gamma_g(b),b)\). This is an equality on every further test scheme, since its defining equality is exactly \(j(a)=g\,j(b)\). Thus \(\delta\) is representable by schemes, smooth and surjective.

Its equality relation is a scheme with an explicit chart. Over the parameter scheme \(X^2\) with coordinates \((c,d)\), take the universal \(g=L_cL_d^{-1}\) and its represented open \(\Omega_g\subset X^3\), whose third coordinate is \(b\). The graph \(a=\gamma_g(b)\) identifies this open with the relation between \((a,b)\) and \((c,d)\). Both relation projections are smooth, as base changes of \(\delta\); its endpoint map is a monomorphism on all tests. [S07 Theorem 8.2](AG-RG-S07.md) now applies to this flat locally finitely presented equivalence relation. Its fppf quotient is an algebraic space, and (8.1) and the equality relation identify that quotient with \(K\).

The group operations are already operations of its sheaf, so Yoneda gives operations on this algebraic space satisfying the group axioms. Smoothness of \(K/S\) follows from the representable smooth covering (8.2) with smooth source. Each geometric fibre is irreducible, as the continuous surjective image of the irreducible \(X_s\times X_s\). The open \(X_s\) is therefore dense in it.

**Separation, finiteness and uniqueness.** On any scheme test \(R\to K\times_SK\), write its sections as \(u,v\). The two translated opens
\[
F=u^{-1}X_R\cap v^{-1}X_R\subset K_R
\]
meet in every geometric fibre, by irreducibility. This open is smooth-surjective over \(R\). A scheme atlas and its affine opens give an fppf scheme covering \(R_i\to R\) with sections \(t_i\in F(R_i)\). Both \(ut_i\) and \(vt_i\) lie in \(X(R_i)\). Cancellation identifies the equalizer of \(u,v\) on every further test with the equalizer of \(ut_i,vt_i\), which is closed because \(X/S\) is separated. S04 Corollary A3.2 descends this closed immersion. Since the original scheme test was arbitrary, the diagonal of \(K/S\) is a closed immersion and \(K/S\) is separated.

It is locally of finite presentation by smoothness. Over every affine open of \(S\), \(X\times_SX\) is quasi-compact because \(X/S\) is of finite presentation. Surjectivity of (8.2) makes \(K\) quasi-compact there. The closed diagonal is quasi-compact, being an affine closed immersion, so \(K/S\) is quasi-separated. These three properties give finite presentation. No quasi-compactness of the open relation in \(X^3\) was assumed.

For any second extension \(K'\), each geometric fibre has the dense irreducible open \(X_s\), and hence is irreducible. Every section \(g'\) is fppf locally \(ab^{-1}\): the open \(X_R\cap (g')^{-1}X_R\) is smooth-surjective, so choose \(b\) there and set \(a=g'b\). Left translation restricts to a dense-open isomorphism of \(X_R\), giving a homomorphism \(K'\to\operatorname{Bir}(X)\). It is faithful: an identity germ fixes a section on a dense-open smooth cover, and cancellation in \(K'\) gives \(g'=1\). Its restriction to \(X\) is \(a\mapsto L_a\), since the original partial product is extended. The local difference expression identifies its image with \(K\). This gives the unique isomorphism fixing \(X\); uniqueness also follows because those differences generate the whole sheaf. After every \(S'\to S\), the constructed \(K_{S'}\) is another such extension of \(X_{S'}\), with the same translated-chart fibre products and multiplication. Uniqueness supplies the canonical base-change identification and its cocycle. This proves the entire lemma. \(\square\)

Apply the lemma to (7.1) and its strict graph. We obtain a smooth separated finite-presentation group algebraic space \(G_{\mathbf Z}\) containing \(X\) as an open. Its generic fibre is canonically the characteristic-zero group of Section 6: that group has this same dense big cell and partial law, so the uniqueness just proved identifies the two extensions. The torus and root axes are closed subschemes of \(X\), hence are locally closed immersions into \(G_{\mathbf Z}\). The whole pair laws retained in Section 7 make them subgroup morphisms with their prescribed multiplication and inverse. Their characters and parameter differentials are the specified ones on the identity cell.

The required conjugation and Gauss relations hold as morphisms over \(\mathbf Z\) on their stated domains. Their parameter sources are flat over \(\mathbf Z\); localization to \(\mathbf Q\) is injective on their structure sheaves. The target is separated, so the equalizer ideal of the two morphisms is zero if it is zero after this localization. The characteristic-zero relations thus give the integral identities, including over nonreduced test rings. Affineness, closedness of the eventual canonical root groups and positive-characteristic reductivity are the separate arguments of Section 9.

## 9. Why the completed integral group is affine and reductive

There are two separate issues: an algebraic space must be shown to be an affine scheme, and its positive-characteristic fibres must be reductive.

First work over an algebraically closed field $k$. Every $g\in G_k(k)$ lifts through the smooth surjection (8.2): its nonempty fibre is an open subscheme of $X_k$, and hence has a $k$-point. Thus $g=ab^{-1}$ for some $a,b\in X_k(k)$, and $g$ lies in the right translate $X_kb^{-1}$. These translates are open schemes. Let $O$ be their union. If its closed complement were nonempty, its inverse image under the surjection $X_k\times_kX_k\to G_k$ would be a nonempty closed subscheme of a finite-type $k$-scheme. It would have a $k$-point, whose image would be a rational point outside $O$, a contradiction. Therefore these scheme opens cover every point of $G_k$, and the fibre is a smooth separated group scheme.

The conjugation action of \(T_k\) on the identity cell has the decomposition

$$
\operatorname{Lie}(G_k)
=\operatorname{Lie}(T_k)\oplus
\bigoplus_{\alpha\in\Phi}kE_\alpha.
\tag{9.1}
$$

The Gauss relation differentiated in the two root parameters gives

$$
[E_\alpha,E_{-\alpha}]=d\alpha^\vee(1).
\tag{9.2}
$$

For the simply connected datum the coroot is primitive in \(P^*\), so this vector is nonzero even in characteristics two and three.

Consider the kernel \(J_k\) of the adjoint representation. Its Lie algebra is stable under \(T_k\). Equation (9.2) rules out every root line, so its Lie algebra has only torus-weight zero. Its reduced identity component \(J_k^0\) is smooth over the perfect field \(k\). The fixed locus of \(T_k\) in a neighborhood of its identity is smooth, with tangent space the invariant vectors: split equivariant formal coordinates, as in the torus fixed-point argument of the earlier lessons. Thus the fixed locus has the full dimension of \(J_k^0\), and connectedness makes \(T_k\) centralize \(J_k^0\). The fixed locus of \(T_k\) in the identity cell \(X_k\) is exactly \(T_k\), by its distinct nonzero root characters. Consequently an open neighborhood of the identity of \(J_k^0\) lies in \(T_k\), and hence \(J_k^0\subset T_k\). Here \(T_k\) is closed in \(G_k\): a locally closed subgroup of an algebraic group is closed, since its dense open in its closure and translations make it open and closed in that closure.

The adjoint kernel on \(T_k\) is \(D_k(P/Q)\), which is finite. Therefore \(J_k\) is zero-dimensional. It follows that the adjoint homomorphism of the group algebraic space over \(\mathbf Z\),

$$
\operatorname{Ad}:G_{\mathbf Z}\longrightarrow
\operatorname{GL}(\operatorname{Lie}(G_{\mathbf Z})),
\tag{9.3}
$$

is quasi-finite and separated. The algebraic-space normalization lemma, with its complete proof in *Roots and reductive groups of rank one*, Section 5, makes it representable and quasi-affine. Thus \(G_{\mathbf Z}\) is a scheme.

We can already prove affineness of each geometric fibre. Apply the earlier *Group schemes over a field*, Proposition 5.8, to its adjoint homomorphism. Here the source has just been proved to be a smooth finite-type scheme, so the map is quasi-compact and its source is reduced. The proposition constructs the closed schematic image $I\subset\operatorname{GL}(\operatorname{Lie}G_k)$ and proves that $q:G_k\to I$ is faithfully flat. Concretely its defining ideal is the kernel of the structure-sheaf map into $q_*\mathcal O_{G_k}$; flat base change makes $q\times q$ schematically dominant, so multiplication and inversion preserve that ideal. Reducedness of the source makes the ideal radical. The complete closed-image and flatness arguments are the preceding provider's Propositions 5.6 and 5.8. The group $I$ is affine because it is closed in the general linear group. The scheme-theoretic kernel of $q$ is the zero-dimensional finite group $J_k$ computed above, and multiplication gives an isomorphism
\[
G_k\times_kJ_k\xrightarrow{\sim}G_k\times_I G_k,
\qquad(g,j)\longmapsto(g,gj).
\]
Its inverse is $(g,g')\mapsto(g,g^{-1}g')$. Thus $q$ is an fppf $J_k$-torsor. After the faithfully flat base change $G_k\to I$ it is finite, since the displayed projection is the base change of the finite $J_k\to\operatorname{Spec}k$. Finiteness descends by the earlier affine and finite-module descent proofs in AG-RG-S04, Lemmas A1.2–A1.3 and Corollary A3.2. Consequently $q$ is finite and its source is affine. This proves affineness of $G_k$ before its reductivity is used.

Now let \(N=R_u(G_k)\). Lemma 2.A of [lesson one](AG-RG-01.md) proves that a subgroup scheme of a unitriangular group has no nontrivial characters, including nonreduced subgroup schemes. A multiplicative-type subgroup has a representation decomposed into characters; applying that lemma to its faithful unitriangular representation makes it trivial. Thus a unipotent group meets a torus trivially as a group scheme. Hence \(\operatorname{Lie}(N)\cap\operatorname{Lie}(T_k)=0\). If \(N\ne1\), its torus-stable Lie algebra contains one of the one-dimensional root lines, say \(kE_\alpha\). Let \(T_\alpha=(\ker\alpha)^0_{\mathrm{red}}\). Its centralizer in \(N\) is smooth, and the positive limit subgroup for \(\alpha^\vee\) in that centralizer is smooth with tangent line \(kE_\alpha\). In \(G_k\) the corresponding limit subgroup is \(U_\alpha\), since the only nonzero weights trivial on \(T_\alpha\) are \(\pm\alpha\). Inclusion and equality of dimension force \(U_\alpha\subset N\). Normality and conjugation by \(n_\alpha\) then give \(U_{-\alpha}\subset N\). Their Gauss relation in AG-RG-03 Theorem 7.1 forces $\alpha^\vee(\mathbf G_m)\subset N$: for any unit $d$, put $u=d-1$ and $v=1$, so $1+uv=d$, and solve that relation for the coroot factor. All the other factors belong to the two opposite root groups. This is a nontrivial torus, a contradiction. Thus \(N=1\). The centre has character group \(P/Q\), which is finite, so the reductive fibre is semisimple.

To finish, we prove affineness over \(\mathbf Z\), rather than just in its fibres. We need the following small geometric fact, included with its complete openly licensed proof.

### Flat base change and localization of quasi-coherent cohomology

**Statement.** Let $X$ be a quasi-compact quasi-separated scheme over $\operatorname{Spec}A$, let $\mathcal F$ be quasi-coherent, and let $B$ be any flat $A$-algebra. Write $g:X_B\to X$ for the projection and $\mathcal F_B=g^*\mathcal F$. For every $q\geq0$, the canonical map is an isomorphism

$$
H^q(X,\mathcal F)\otimes_A B
\longrightarrow H^q(X_B,\mathcal F_B).
$$

The declared geometric input is [affine vanishing, AG-QC-03, Theorem 2.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-LTF/support/AG-QC--affine-cohomology-and-serres-criterion.html): for every ring $R$ and every $R$-module $M$, $H^q(\operatorname{Spec}R,\widetilde M)=0$ for $q>0$. We also use the affine module–sheaf correspondence and the derived-functor definition of sheaf cohomology. No finite generation, Noetherianity or finite presentation is assumed for $A$, $B$ or $\mathcal F$.

**The separated case and the ordered cover construction.**

First suppose that $X$ is separated over the affine base. Choose a finite affine open cover $U_1,\ldots,U_r$. For a strictly increasing tuple $I=(i_0<\cdots<i_p)$ put $U_I=U_{i_0}\cap\cdots\cap U_{i_p}$, and let $j_I:U_I\hookrightarrow X$. Empty intersections contribute zero. Every $U_I$ is affine: the intersection of two affine opens is the inverse image of their affine product under the closed diagonal, and induction gives the assertion for finite intersections.

We construct the cohomological comparison rather than assume that a section complex computes it. For any sheaf of modules $\mathcal G$, form the augmented alternating sheaf complex

$$
0\longrightarrow\mathcal G\longrightarrow
\mathcal C^0(\mathcal G)\longrightarrow\cdots\longrightarrow
\mathcal C^{r-1}(\mathcal G)\longrightarrow0,
\qquad
\mathcal C^p(\mathcal G)=\prod_{i_0<\cdots<i_p}(j_I)_*(\mathcal G|_{U_I}).
$$

The differential is the alternating sum of restriction maps. This complex is exact on stalks. Indeed, near a point $x$ choose $a$ with $x\in U_a$ and restrict to a neighbourhood $V\subset U_a$. Regard an ordered cochain as alternating in all its indices, with repeated-index components zero. The map lowering the degree is

$$
(hc)_{i_0\ldots i_{p-1}}=c_{a i_0\ldots i_{p-1}}.
$$

It is well defined because $V\cap U_I\cap U_a=V\cap U_I$. In degree zero it takes $c_a$ to a section on $V$, the augmented term. Expanding the alternating differential cancels all terms except $c$, so $dh+hd=1$, including the augmented degree. This proves exactness even when a direct-image stalk at a boundary point is nonzero.

Take an injective resolution $\mathcal F\to\mathcal I^\bullet$ in sheaves of $\mathcal O_X$-modules. Restriction to an open preserves injectives: its left adjoint, extension by zero, is exact, as one checks on stalks. Direct image under an open immersion also preserves injectives because it is right adjoint to exact restriction. Thus each term of the augmented sheaf complex for $\mathcal I^q$ is injective. Its first injection splits, and successive cokernels are injective direct summands; inductively the whole finite exact row splits. Applying global sections therefore leaves it exact.

Consequently the augmentation from $\Gamma(X,\mathcal I^\bullet)$ to the total complex of

$$
C^{p,q}=\prod_{i_0<\cdots<i_p}\Gamma(U_I,\mathcal I^q|_{U_I}),
\qquad 0\leq p<r,\quad q\geq0,
$$

is a quasi-isomorphism. Here the total differential is $d_{\mathrm{cover}}+(-1)^p d_{\mathrm{resolution}}$. Exactness of the augmented horizontal rows proves the assertion by the row filtration. Each total degree contains finitely many terms.

The column filtration $F^p\operatorname{Tot}^n=\bigoplus_{a\geq p}C^{a,n-a}$ gives the ordered-cover spectral sequence

$$
E_1^{p,q}=\prod_{i_0<\cdots<i_p}H^q(U_I,\mathcal F|_{U_I})
\quad\Longrightarrow\quad H^{p+q}(X,\mathcal F),
$$

with $d_1$ the alternating restriction differential. Explicitly, for $s\geq1$ set

$$
Z_s^{p,q}=\{z\in F^p\operatorname{Tot}^{p+q}:dz\in F^{p+s}\operatorname{Tot}^{p+q+1}\},
\qquad
E_s^{p,q}=\frac{Z_s^{p,q}}
{Z_{s-1}^{p+1,q-1}+dZ_{s-1}^{p-s+1,q+s-2}},
$$

where $Z_0^{p,q}=F^p\operatorname{Tot}^{p+q}$. The total differential induces $d_s:E_s^{p,q}\to E_s^{p+s,q-s+1}$, and taking its cohomology gives the next page. Extend the filtration by $F^p=\operatorname{Tot}$ for $p\leq0$ and $F^p=0$ for $p\geq r$. For sufficiently large $s$, the cycle condition is $dz=0$ and the denominator accounts for the next filtration piece and all boundaries lying in $F^p$. Thus the stable terms are the associated graded pieces of cohomology. There are only $r$ columns, so each abutment has a finite filtration and convergence involves no infinite-product or completion issue. This construction works for any finite open cover, including covers with non-affine intersections.

For our separated affine cover, affine vanishing makes every row with $q>0$ on $E_1$ zero. The augmentation therefore canonically identifies cohomology with that of the finite section complex

$$
\check C^p(\mathcal U,\mathcal F)=\prod_{i_0<\cdots<i_p}\Gamma(U_I,\mathcal F).
$$

If $U_I=\operatorname{Spec}R$ and $\mathcal F|_{U_I}=\widetilde M$, its base change has sections

$$
M\otimes_R(R\otimes_A B)=M\otimes_A B.
$$

These identifications commute with restriction. Tensor also commutes with the finite products, so the section complex on $X_B$ is the section complex on $X$ tensored with $B$. Flat tensor preserves kernels and images and hence cohomology. This proves the claimed isomorphism in the separated case.

**Canonical comparison and nonseparated intersections.**

To identify the preceding calculation with the canonical map and compare the general cover spectral sequences, choose an injective resolution $\mathcal F_B\to\mathcal J^\bullet$ on $X_B$. The projection $g$ is flat, so $g^*\mathcal I^\bullet$ is a resolution of $\mathcal F_B$. Target injectivity extends its identity on $\mathcal F_B$ degree by degree to a chain map $g^*\mathcal I^\bullet\to\mathcal J^\bullet$. The same extension argument makes any two choices chain homotopic. Pulling back sections and multiplying by elements of $B$ gives a map of augmented double complexes

$$
C^{p,q}(X,\mathcal I)\otimes_A B
\longrightarrow C^{p,q}(X_B,\mathcal J).
$$

Its augmentation is the usual cohomology base-change map; its column maps are the canonical comparisons on the intersections. It is independent of the resolution choices and compatible with restriction and successive base changes. Since $B$ is flat, the source total complex has cohomology $H^n(X,\mathcal F)\otimes_A B$. Flat tensor also commutes with the cycles, boundaries and finite sums defining every spectral-sequence page.

Now let $X$ be merely quasi-compact and quasi-separated. Choose a finite affine cover as before. Each $U_I$ is quasi-compact, by quasi-separatedness and finite intersection, and is separated over $\operatorname{Spec}A$, since it is an open subscheme of the affine $U_{i_0}$. It need not be affine. Apply the separated result to each $U_I$. It shows that every term of the comparison on $E_1$ is an isomorphism, for all $q\geq0$. Therefore every subsequent page and every associated graded piece of the abutment is an isomorphism. Induction through the finite filtrations gives an isomorphism of the abutments themselves. This proves the statement for every flat $A$-algebra $B$.

**Localization and higher direct images.**

Taking $B=S^{-1}A$ for any multiplicative set gives, canonically,

$$
S^{-1}H^q(X,\mathcal F)\cong
H^q(X\times_A\operatorname{Spec}S^{-1}A,\mathcal F_{S^{-1}A}).
$$

This includes $A\to A_a$ and $A\to A_{\mathfrak p}$.

For completeness, let $f:X\to Y$ be a quasi-compact quasi-separated morphism and let $\mathcal F$ be quasi-coherent. The sheaf $R^qf_*\mathcal F$ is the sheafification of $V\mapsto H^q(f^{-1}V,\mathcal F)$. Indeed, use an injective resolution on $X$, restrict it to $f^{-1}V$, and take stalks of $f_*\mathcal I^\bullet$; filtered colimits of modules are exact, so taking cohomology commutes with that stalk limit. On an affine $V=\operatorname{Spec}A$, put $M=H^q(f^{-1}V,\mathcal F)$. The localization result identifies the presheaf on every distinguished $D(a)\subset V$ with $M_a$, compatibly with restriction. Its sheafification is therefore $\widetilde M$. This proves quasi-coherence of $R^qf_*\mathcal F$ and supplies the canonical identification of its sections on $V$ with $M$.

If $h:Y'\to Y$ is flat, cover $Y'$ by affines $W=\operatorname{Spec}B$ mapping into affines $V=\operatorname{Spec}A$ of $Y$. Here $B$ is flat over $A$. For the Cartesian base change $f':X\times_Y Y'\to Y'$, the theorem identifies the modules describing both sides of

$$
h^*R^qf_*\mathcal F\longrightarrow R^qf'_*\mathcal F_{Y'}.
$$

Naturality makes these identifications agree on overlaps, so this is an isomorphism of sheaves. In particular, at $y\in V$ corresponding to $\mathfrak p$,

$$
(R^qf_*\mathcal F)_y\cong
H^q(f^{-1}V\times_A\operatorname{Spec}A_{\mathfrak p},\mathcal F_{A_{\mathfrak p}}).
$$

This is the flat-localization identity needed for the stalk calculation in AG-RG-05, §9. $\square$

**One-dimensional affine-open lemma (Stacks, Tag 09N9).** If \(Y\) is affine and all its local rings are Noetherian of dimension at most one, then every quasi-compact open \(O\subset Y\) is affine.

**Proof, with the Stacks statement retained and the cohomological steps written out.** Write \(Y=\operatorname{Spec}A\) and let \(\mathcal F\) be quasi-coherent on \(O\). The open \(O\) is quasi-compact and separated. The full flat-localization proof in the earlier supporting lesson *Algebra and sheaf cohomology before reductive groups*, Section 6, gives, for every prime \(\mathfrak p\subset A\),
\[
H^i(O,\mathcal F)_{\mathfrak p}
=H^i(O\times_Y\operatorname{Spec}A_{\mathfrak p},\mathcal F_{A_{\mathfrak p}}).
\]
An open in the spectrum of the Noetherian local ring \(A_{\mathfrak p}\) either contains its closed point, and is the whole spectrum, or contains only generic points. There are finitely many generic points: in a Noetherian topological space every closed subset has finitely many irreducible components, by induction on closed subsets (a reducible counterexample splits into two strictly smaller counterexamples). In dimension at most one no distinct nonclosed primes can specialize to one another. Thus the latter open is a finite discrete space. Each of its singleton components has an affine neighbourhood contained in that component, so it is affine; their finite disjoint union is the spectrum of the product of their rings. Both possibilities are affine. The affine-vanishing proof of that supporting lesson, Theorem 5.1, therefore makes the displayed localization zero for \(i>0\).

A module with zero prime localizations is zero: a nonzero element has a proper annihilator contained in a maximal ideal, at which its localization remains nonzero. Consequently \(H^i(O,\mathcal F)=0\) for every \(i>0\) and every quasi-coherent \(\mathcal F\). The full ideal-sheaf affine criterion in the supporting lesson, Theorem 9.2, now proves that \(O\) is affine. This argument uses no separate Leray or higher-direct-image theorem. \(\square\)

**Lemma 9.1.** A quasi-finite separated homomorphism \(f:K\to H\) of finite-type group schemes over a Dedekind base is affine if \(K\) is smooth with geometrically connected fibres of constant dimension.

**Proof.** Write $d$ for the constant fibre dimension of $K$. We first justify the local base change, its dimension assertion and the translating lifts. Affineness of a scheme morphism is local on its target and descends faithfully flatly by AG-RG-S04 Corollary A3.2. Finite-presentation limit descent in AG-MO-03 Theorem 4.2 then permits localization on the Dedekind base. The generic field case is included below. At a closed point its local ring is a discrete valuation ring $R_0$, with uniformizer $\pi$.

Use the actual strict-henselization construction of *Henselian local rings and henselization*, Theorem 5.1. Its residue field is the separable closure $k$ of the residue field of $R_0$; we do not assume that $k$ is perfect. We record the needed discrete valuation property directly. The current henselization lesson also proves general Noetherianity and dimension in Theorems 6.3--6.4; the following argument uses only its actual strict-henselization construction and the earlier Krull-intersection proof. A localized pointed etale neighborhood $A$ of $R_0$ is Noetherian and flat, has maximal ideal $\pi A$ and has field residue ring. The element $\pi$ is regular. Krull intersection, AG-RG-S02 Section 1.1, shows that every nonzero $a\in A$ is $\pi^n u$ for a unique $n\geq0$ and a unit $u$. Thus $A$ is a discrete valuation ring. Local transition maps preserve $\pi$ and units and are injective; their colimit has the same description of each nonzero element. Every nonzero ideal of that colimit is generated by the element of smallest valuation, so this strict henselization is itself Noetherian and a discrete valuation ring. Its faithfully flat completion $R$ is a complete discrete valuation ring with the same residue field $k$, by the written completion proof of AG-RG-S02 Lemma 1.3 and the same regular-uniformizer and Krull-intersection argument. Consequently $R_0\to R$ is faithfully flat. All hypotheses on $f$ and $K$ survive this change.

Let $I_\eta$ be the closed schematic image of $K_\eta\to H_\eta$. The actual image proof in *Group schemes over a field*, Proposition 5.8, makes $K_\eta\to I_\eta$ faithfully flat and makes formation of this reduced image commute with field extension. After every algebraic closure of the generic field, smoothness makes the local rings of $K_\eta$ regular domains, by the actual regularity proofs in AG-CA-18 Theorem 2.1 and AG-CA-14 Theorem 1.1. Distinct irreducible components therefore cannot meet: on an affine chart at an intersection they would give distinct minimal primes in that local domain. There are finitely many components since the scheme is of finite type over a field, so they are disjoint open and closed subsets. Geometric connectedness leaves one component, and the local domains make the scheme reduced: every nilpotent section has zero germ at every point. Thus $K_\eta$ is geometrically integral. This is the local component argument of AG-RG-S02 Lemma 4.1 on affine charts; it does not require the whole group to be affine. Thus $I_\eta$ is geometrically integral. Its dimension is $d$: the image-dimension proof of Theorem 5.10 has zero-dimensional kernel here, since $f$ is quasi-finite. That kernel is a separated finite-type zero-dimensional scheme over a field. It has finitely many points, by the Noetherian component argument, and each singleton is open. Each singleton has an affine neighborhood contained in that open, so is the spectrum of a zero-dimensional local Artinian finite-type field algebra. Lemma P0.9 of AG-RG-S04 makes each such algebra finite-dimensional, including its nilpotents. The finite disjoint union is affine with the product of these finite-dimensional algebras, hence the kernel is finite even before any affineness of $K_\eta$ has been proved. The identity
\[
 K_\eta\times\ker f_\eta
   =K_\eta\times_{I_\eta}K_\eta
\]
on all tests makes the faithfully flat map a torsor under this finite group. Finiteness descends from its trivialization, by the finite module/algebra descent proof of AG-RG-S04 Lemmas A1.2--A1.3. Hence the generic map is finite.

Replace $H$ by the schematic closure of $I_\eta$ in $H$. This is a finite-type closed subgroup. On an affine chart its ring injects into its localization at $\pi$ by the definition of schematic closure, so it is $R$-flat by the valuation-domain flatness proof in *Tor and flat modules*, Theorem 4.1. These same injections show that each nonempty affine chart is a domain, since its generic chart is an open of the integral $I_\eta$. The subgroup equations hold on the closure: multiplication is checked on the flat product of two copies of the closure, inversion on one copy, and the generic equations then hold everywhere by injectivity into localization at $\pi$. The map from $K$ factors through it for the same reason, since $K$ is flat. Proving affineness with this target suffices, as its inclusion into the original target is a closed immersion. We now use $H$ for the closure.

Here is the needed special-fibre dimension calculation. Over an algebraic closure of $k$, all components of the finite-type group $H_s$ have one common dimension $r$, by the actual homogeneous-dimension proof in *Lie algebras and smoothness*, Lemma 3.1. Their reduced connected components are translates of the identity component by the component proof in *Group schemes over a field*, Proposition 2.4. Field-extension invariance of dimension is AG-RG-S08 Lemma G.1.2. Choose an affine chart $\operatorname{Spec}A$ of $H$ meeting the special fibre. Its nonzero special algebra $A/\pi A$ has dimension $r$. The actual Noether-normalization proof in *Krull dimension and Noether normalization*, Corollary 3.2, gives a finite inclusion
\[
 k[t_1,\ldots,t_r]\lhook\joinrel\longrightarrow A/\pi A.
\]
Lift the $t_i$ to $A$. The resulting map $R[t_1,\ldots,t_r]\to A$ is injective: a nonzero polynomial relation can be divided by the largest common power of $\pi$ in its finitely many coefficients; regularity of $\pi$ then gives a primitive relation whose reduction contradicts that inclusion. The induced map to affine $r$-space is quasi-finite at every point of this chart's special fibre, because its special-fibre map is finite. Its quasi-finite locus is open by the fully proved AG-RG-S04 Theorem C5.1. It is nonempty and has a nonempty generic fibre, since every affine chart of the flat closure injects into its generic chart. Its generic map is dominant, by the polynomial-ring injection, and quasi-finite. The function-field dimension calculation in *Krull dimension and Noether normalization*, Theorem 4.2, therefore gives $r=d$. This proves the asserted dimension of every geometric special component without a separate discrete-valuation dimension formula.

Let $z_i$ be the generic points of the finitely many special-fibre components. In a domain affine chart of $H$ their primes are minimal over $(\pi)$. The principal-ideal height theorem in *Dimension theory of Noetherian local rings*, Theorem 3.1, gives height at most one; regularity and nonvanishing of $\pi$ give height at least one. Thus $\mathcal O_{H,z_i}$ has dimension one. Apply AG-RG-S04 Theorem D7.1 to the quasi-finite separated base change of $K$ to this local spectrum. It is a quasi-compact open in a finite scheme. Integral prime lifting and incomparability, AG-RG-S04 Lemma P0.4, make that finite scheme's local rings Noetherian of dimension at most one. The preceding affine-open lemma proves that the open is affine. The actual eventual-affineness proof in AG-MO-03 Theorem 4.2, using Lemma 2.3, spreads this affineness to an open neighborhood of $z_i$ in $H$.

Let $V\subset H$ be the union of the opens on which $f$ is affine. Affineness is local on the target, so $f$ is affine over $V$. The finite generic map gives $H_\eta\subset V$, and the preceding paragraph puts every $z_i$ in $V$. The closed reduced image of $K_s\to H_s$ commutes with field extension by Proposition 5.8 and has dimension $d$ by Theorem 5.10. Over an algebraic closure $\bar k$, this image is connected and reduced, so it equals $(H_{\bar s})^0_{\mathrm{red}}$: it is a closed connected subgroup of that irreducible component with the same dimension. Translation by it is transitive on the closed points of each component. Since $V_{\bar s}$ meets each component, for every geometric closed point $y$ of $H_s$ the set of elements of $K_{\bar s}$ whose translation sends $y$ into $V_{\bar s}$ is a nonempty open.

We must choose a translator that lifts over $R$. The set $K_s(k)$ is dense in $K_{\bar s}$. First, every nonempty open in the smooth $k$-scheme $K_s$ has a $k$-point: take a nonempty standard smooth chart with an etale map to affine space. The map is open by *Flat morphisms*, Theorem 3.2. A nonempty open in affine space over the infinite separably closed field $k$ has a $k$-point by successive avoidance of the finitely many polynomial zeros. Its nonempty etale fibre has a finite separable residue extension, which equals $k$. Next, $\bar k/k$ is purely inseparable. A principal open over $\bar k$ uses only finitely many coefficients; in positive characteristic a sufficiently large $p$-power of its defining function belongs to the original $k$-algebra and defines the same open after base change. In characteristic zero $k=\bar k$. Thus every nonempty geometric open contains a point of $K_s(k)$, proving the density assertion.

Every $a\in K_s(k)$ lifts to $K(R)$. Take a smooth affine chart of $K$ containing $a$. The formally smooth lifting property, written in *Formally smooth, unramified and etale ring maps*, Theorems 3.1 and 4.1, lifts its point compatibly through $R/\pi^n$ for all $n$. A finite presentation of the chart and completeness of $R$ turn the compatible coordinate values into an $R$-point: its finitely many polynomial equations vanish because they vanish modulo every $\pi^n$, and its inverted coordinates stay units. This supplies the required lift without any assumption that an arbitrary geometric point is rational over the residue field.

Choose such a rational translator in the nonempty open associated to $y$ and lift it to $K(R)$. The commuting translations by this lift on $K$ and by its image on $H$ preserve the property that $f$ is affine; hence they preserve $V$. They send $y$ into $V$, so $y$ already belongs to $V$. All geometric closed points of $H_s$ lie in $V$. A nonempty closed subset of a finite-type field scheme has a geometric closed point, by the earlier Nullstellensatz proof. Therefore $H_s\subset V$. Together with $H_\eta\subset V$ this gives $H=V$. The map $f$ is affine over $R$, and faithfully flat descent and the initial localization prove the statement over the Dedekind base. $\square$

Apply Lemma 9.1 to (9.3). Its target is affine, so \(G_{\mathbf Z}\) is affine. The torus factor \(T\) of its cell is now a closed subgroup, by the closed-immersion result for multiplicative-type homomorphisms in the first lesson. The zero-weight computation shows it is maximal in every fibre. Equations (9.1), (9.2) and the Gauss formula identify its roots and coroots with the original simply connected datum. Its root lines have the chosen integral frames. We have constructed the pinned split semisimple group over \(\mathbf Z\) for that datum.

## 10. The existence theorem for every reduced datum

**Theorem 10.1.** Every reduced root datum is the datum of a pinned split reductive group over \(\mathbf Z\). For every nonempty scheme \(S\), pinned split groups of a specified constant datum over \(S\) are obtained by base change from this integral group, up to a unique pinning-preserving isomorphism.

**Proof.** Let \(\mathcal R=(X,\Phi,X^*,\Phi^\vee)\) be reduced. The reflection calculation in AG-RG-04 §1 gives

\[
X_{\mathbf Q}=V\oplus C,
\quad V=\mathbf Q\Phi,
\quad C=\{x:\langle x,\alpha^\vee\rangle=0\ (\alpha\in\Phi)\}.
\]

Let \(P\subset V\) be the weight lattice, \(\pi,c\) the two projections, and \(L=c(X)\). This image is finitely generated and torsion-free, hence free. It has rank \(\dim C\), since \(X\) spans \(X_{\mathbf Q}\). The map

\[
j:X\longrightarrow P\oplus L,\qquad x\longmapsto(\pi(x),c(x))
\]

is well-defined because the coroot pairings of \(\pi(x)\) are those of \(x\), hence integral. It is injective because its two coordinates recover \(x\). Both lattices have the same rank and their rational spaces coincide, so its cokernel is finite. Each root maps to \((\alpha,0)\), and the dual map sends each \((\alpha^\vee,0)\) to the prescribed coroot.

Once the simply connected integral group \(G_{\mathrm{sc}}\) has actually been constructed, form \(G_{\mathrm{sc}}\times D(L)\). The torus map \(D(P\oplus L)\to D(X)\) has finite flat kernel \(H=D(\operatorname{coker}j)\). Every root vanishes on \(H\), so the already proved centre calculation makes \(H\) central. AG-RG-04 Theorem 7.1 constructs its fppf quotient as an affine reductive group. Its torus has character lattice \(j(X)\), its root subgroups are unchanged, and its coroots are their images under the quotient. The resulting datum is therefore \(\mathcal R\); the simple frames give its pinning. The empty-root case is \(D(X)\) directly.

Base change preserves the group, datum and pinning. Theorem 5.1 gives the unique pinning-preserving isomorphism to any other group with that constant datum. $\square$

Without a pinning, two globally split groups with isomorphic constant data are still isomorphic: choose their simple-root frames and apply Theorem 5.1. If the type varies on a disconnected base, apply the result to each constant-type part. Such a family need not be the base change of one integral group.

### The derived group

Use the split presentation $G=(G_{\mathrm{sc}}\times D(L))/H$ constructed in Theorem 10.1, and put $H_{\mathrm{sc}}=H\cap(G_{\mathrm{sc}}\times1)$. The central quotient theorem gives a semisimple group
\[
D=(G_{\mathrm{sc}}\times1)/H_{\mathrm{sc}}.
\tag{10.2}
\]
Its map to $G$ is a closed normal immersion. Indeed its inverse image in the faithfully flat cover $G_{\mathrm{sc}}\times D(L)\to G$ is $(G_{\mathrm{sc}}\times1)H$, the inverse image of the finite subgroup $\operatorname{pr}_L(H)$ under the projection to $D(L)$; this is closed. The quotient of this inverse image by $H$ is exactly (10.2), and affine closed-subgroup descent identifies it with the indicated closed subgroup of $G$. Its quotient is the torus
\[
G/D\simeq D(L)/\operatorname{pr}_L(H).
\]
The subgroup $\operatorname{pr}_L(H)$ is a finite subgroup of multiplicative type; the diagonalizable quotient calculation proves that this quotient is a torus over every base.

The simply connected group is perfect as an fppf sheaf. To see this directly, work over an arbitrary test ring $A$. The algebra
\[
B=A[t,t^{-1},(t^2-1)^{-1}]
\]
is smooth and faithfully flat over $A$: every fibre is the nonempty open of the affine line on which $t$ and $t^2-1$ are invertible. In $G_{\mathrm{sc}}(B)$, the torus action gives
\[
[\alpha^\vee(t),x_\alpha(v)]
=x_\alpha((t^2-1)v).
\]
Thus any $x_\alpha(u)$ becomes a commutator on this fppf cover, by taking $v=u/(t^2-1)$. The same argument applies to every root. The rank-one Gauss relation expresses $\alpha^\vee(d)$ as a product in $U_\alpha$ and $U_{-\alpha}$ for any unit $d$, using $u=d-1,v=1$. The simple coroots form a basis of the simply connected cocharacter lattice, so the root groups generate the whole torus and hence the big cell. The word-generation argument of Lemma 4.1 proves that the big cell generates the group fppf locally. Therefore the fppf subgroup generated by commutators is the whole $G_{\mathrm{sc}}$.

A faithfully flat quotient of a perfect sheaf is perfect: lift a section locally, write its lift locally as a product of commutators, and take the images. Thus $D$ is perfect. Since $G/D$ is commutative, every commutator of $G$ lies in $D$. Conversely, perfection of $D$ expresses each of its sections locally as a product of commutators of its own sections, and these are commutators in $G$. Hence $D$ is exactly the fppf derived subgroup of $G$.

Here is the maximal central torus and its isogeny without an implicit lattice assertion. Put
\[
Q=\mathbf Z\Phi,
\qquad Q_{\mathrm{sat}}=X\cap\mathbf Q\Phi.
\]
The centre calculation in AG-RG-03 Section 1 gives $Z(G)=D_S(X/Q)$. The torsion subgroup of $X/Q$ is $Q_{\mathrm{sat}}/Q$, so
\[
Z=D_S(X/Q_{\mathrm{sat}})\hookrightarrow Z(G)
\]
is a torus. Any homomorphism from a torus to $D_S(X/Q)$ kills the torsion of $X/Q$ on character groups, because the character lattice of a torus is torsion-free. It therefore factors through $Z$; thus $Z$ is the maximal central torus. This argument is a statement about diagonalizable sheaves, so it includes nonreduced centres and arbitrary base change.

Let $\pi:X\to\mathbf Q\Phi$ be the root-space projection of Theorem 10.1. Restriction to the torus of $D$ identifies its character lattice with $\pi(X)$. One can verify the latter equality directly in the presentation: the exact sequence for the projection of the finite diagonalizable $H$ onto $D(L)$ shows that a character $p\in P$ trivial on $H_{\mathrm{sc}}$ becomes trivial on $H$ after adding a suitable $l\in L$; equivalently $(p,l)\in j(X)$. These are precisely $p\in\pi(X)$. The torus part of multiplication $Z\times D\to G$ consequently has character map
\[
X\longrightarrow (X/Q_{\mathrm{sat}})\oplus\pi(X),
\qquad x\longmapsto([x],\pi(x)).
\]
This map is injective: its kernel is contained in both the root span and its complementary central span. Its source and target have equal rank, so its cokernel is finite. The diagonalizable calculation makes the corresponding torus map a finite faithfully flat isogeny. Multiplication is the identity on each root subgroup. Its image therefore contains the big cell fppf locally and, by Lemma 4.1's word-generation argument, every section of $G$ fppf locally. Its kernel lies in $Z\times Z(D)$: a kernel pair has its $D$-coordinate equal to the inverse of a central element. The centre of the semisimple group $D$ is finite of multiplicative type, and the same torus character map identifies this kernel with its finite diagonalizable kernel. Hence multiplication $Z\times D\to G$ is a central isogeny.

For an arbitrary reductive $G/S$, perform these constructions on the étale local splittings of AG-RG-04 Section 8. The derived subgroup is intrinsically the fppf subgroup generated by commutators, and the central torus is intrinsically the maximal torus in the centre. These characterizations identify the local constructions on overlaps and satisfy the triple cocycle. Effective affine and closed-subgroup descent glues them to a smooth closed semisimple subgroup $D$ and a closed central torus $Z$. The same local formulas identify their pullbacks with the corresponding constructions after every base change. The central isogenies also descend. Thus the earlier assertions about the derived group and the central torus hold over all bases, including nonreduced ones. The radical is this central torus: its geometric fibres are the maximal connected solvable normal subgroups of the reductive fibres, and the local split central-torus construction supplies their smooth relative model.

## 11. The dual group

Interchanging roots with coroots gives

$$
\mathcal R^\vee=(X^\vee,\Phi^\vee,X,\Phi).
$$

It is again a reduced root datum. Its integral group from Theorem 10.1, base changed to \(\mathbf C\), is the **dual group**. A dual base determines its pinning up to the unique isomorphism of Theorem 5.1. The construction reverses simply connected and adjoint semisimple data.

For \(\operatorname{SL}_n\), \(X=\mathbf Z^n/\mathbf Z(1,\ldots,1)\) and \(X^\vee=\{(a_i):\sum a_i=0\}\), with roots \(e_i-e_j\) and the matching coroots. For \(\operatorname{PGL}_n\), those two lattices are interchanged. Their complex groups are therefore dual.

For type \(C_n\), the simply connected symplectic group has character lattice \(\mathbf Z^n\), roots \(\pm e_i\pm e_j,\pm2e_i\), and coroots \(\pm e_i\pm e_j,\pm e_i\). Its dual datum is the adjoint datum of type \(B_n\), the split odd orthogonal group. In characteristic two this notation means the smooth split reductive group of that datum; a naive odd-dimensional bilinear-form stabilizer need not be the correct smooth group scheme. Both assertions about dual groups concern their characteristic-zero complex groups.

## 12. Exercises and solutions

**Exercise 1 (easy).** Write the pinning, coroot and simple Weyl representative of \(\operatorname{SL}_2\), and check its square.

**Solution.** Take \(T=\{\operatorname{diag}(z,z^{-1})\}\), the upper triangular Borel, and \(E_\alpha=E_{12}\). Its paired negative frame is \(E_{21}\), its coroot is \(z\mapsto\operatorname{diag}(z,z^{-1})\), and (1.1) gives \(n_\alpha=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\). The square is \(-I=\alpha^\vee(-1)\). The same matrix identity holds over any ring.

**Exercise 2 (medium).** Verify that the data of \(\operatorname{SL}_n\) and \(\operatorname{PGL}_n\) are dual.

**Solution.** A character of the determinant-one diagonal torus is a monomial modulo the relation \(\prod t_i=1\), giving \(X_{\mathrm{SL}}=\mathbf Z^n/\mathbf Z(1,\ldots,1)\). A cocharacter must have \(\sum a_i=0\). In the scalar quotient torus, a character is a monomial trivial on scalars, so has exponent sum zero, and its cocharacter lattice is the quotient by the scalar vector. The roots and coroots in both descriptions are the differences of the corresponding basis vectors. Exchanging the two lattices therefore exchanges the full data, not just their common \(A_{n-1}\) root system.

**Exercise 3 (medium).** Verify the duality between the symplectic and adjoint odd orthogonal data, and explain which root becomes long.

**Solution.** The symplectic torus is \(\operatorname{diag}(t_1,\ldots,t_n,t_1^{-1},\ldots,t_n^{-1})\), with character lattice \(\mathbf Z^n\). Its long root \(2e_i\) has coroot \(e_i\), while \(e_i\pm e_j\) has the same-coordinate coroot \(e_i\pm e_j\). The dual roots are therefore the \(B_n\) roots \(e_i,e_i\pm e_j\). Its coroot corresponding to \(e_i\) is \(2e_i\). The lattice is the root lattice of \(B_n\), so the dual group is adjoint. A long \(C_n\) root becomes a short \(B_n\) root; duality reverses the length ratio. The rank-two roots-and-coroots figure in the preceding lesson shows this metric reversal explicitly.

**Exercise 4 (hard).** Deduce that two globally split reductive groups of the same constant root datum over a nonempty scheme are isomorphic. Is the isomorphism canonical without pinnings?

**Solution.** Choose positive systems corresponding under the datum isomorphism, and choose frames in their globally trivial simple root lines. Theorem 5.1 gives a unique isomorphism preserving these pinnings. Forgetting the chosen frames gives an isomorphism of the original groups. It need not be unique: conjugation by an element of the adjoint torus can scale the frames while preserving the datum. For example \(\operatorname{SL}_2\) admits nontrivial diagonal conjugations.

**Exercise 5 (medium).** In \(\operatorname{SL}_3\), show that a product using each simple reflection once need not be the longest element, and that \(T[2]\) need not commute with a simple representative.

**Solution.** The Weyl group is \(S_3\), with \(s_1=(12),s_2=(23)\). The product \(s_1s_2\) is a three-cycle and has length two, whereas \(w_0=s_1s_2s_1\) reverses the three positions and has length three. Over a field of characteristic different from two, take \(t=\operatorname{diag}(-1,-1,1)\). It belongs to \(T[2]\). Conjugation by the representative swapping positions two and three sends it to \(\operatorname{diag}(-1,1,-1)\), which is different. The representative does normalize \(T[2]\), since it acts on the torus by the corresponding permutation.

The [course prerequisite guide](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-RG/prerequisites.html) records the exact supporting statements and their exact statements and full proof routes.

## References and exact prerequisite proofs

- Michel Demazure, *Schémas en groupes*, freely accessible Gille–Polo re-edition of 13 October 2024: [Exposé XXI](https://webusers.imj-prg.fr/~patrick.polo/SGA3/Exp21-13oct24.pdf), §§3.5 and 5; [Exposé XXIII](https://webusers.imj-prg.fr/~patrick.polo/SGA3/Exp23-13oct24.pdf), §§1–3; [Exposé XXV](https://webusers.imj-prg.fr/~patrick.polo/SGA3/Exp25-13oct24.pdf). These editions provide comparison material for the root transport, rank-two relations and base classification proved here.
- Brian Conrad, [*Reductive group schemes*](https://math.stanford.edu/~conrad/papers/luminysga3.pdf), §§6.2–6.3 and Appendix D. The argument here gives the rank-two calculations and uses a direct matrix construction in characteristic zero.
- Bas Edixhoven and Matthieu Romagny, [*Group schemes out of birational group laws, Néron models*](https://imag.umontpellier.fr/~romagny/articles/artin_birational_law.pdf), §3, for the translation-sheaf construction behind Section 8. The construction and proof are written out here.
- The Stacks authors, *Varieties*, [Tag 09N9](https://stacks.math.columbia.edu/tag/09N9), read in the AI Integrated Stacks Project English source edition, for the one-dimensional affine-open lemma and its proof.
- [Milne’s freely accessible *Algebraic Groups*, version 2.00 (2015)](https://www.jmilne.org/math/CourseNotes/iAG200.pdf). This exact free author edition provides comparison material; its citations do not replace the programme proofs.

The complete Lie proof route is [the preceding Lie lesson](AG-RG-S06.md): Theorem 1.A (ordered words), Section 5 (root geometry), Theorem 6.2 (rational Serre construction), Section 7 (finite absolutely irreducible highest-weight presentations), Theorem 4.2 (complete reducibility), and Proposition 3.3 (inner derivations). Lemma 6.1 above also gives the polynomial rank-one actions explicitly. The Weyl-group presentation for Sections 2 and 5 is proved in the preceding root-data lesson, Section 3. The group isomorphism theorem is proved in this lesson.

The geometric prerequisites are likewise exact supporting lessons: [Flat quotient bootstrap](AG-RG-S07.md), Theorem 8.2, proving the algebraic-space quotient of an arbitrary-base flat locally finitely presented equivalence relation; [Zariski's Main Theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-MO/AG-MO-12.html), the open-into-finite factorization and the normal birational open-immersion consequence, proved in [Affine descent, Zariski Main and recognition of spaces](AG-RG-S04.md), Theorem D7.1 and Corollary D7.4; [Limits of schemes and Noetherian approximation](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-MO/AG-MO-03.html), spreading finite-presentation constructions and their affineness; *Cohomology of sheaves on ringed spaces*, the Leray spectral sequence; and *Cohomology of affine schemes and Serre's criterion*, affine vanishing and its converse. The algebraic-space normalization proof used in Section 9 is present in the preceding rank-one lesson. These are supporting results, not substitutes for the integral group construction in Sections 7–10.

## History

This lesson's exposition, group constructions, calculations, examples and solutions were written by GPT-6.1 Sol (OpenAI), Ultra setting, in October 2026, and are dedicated to the public domain under CC0.

The one-dimensional affine-open lemma and its proof follow the Stacks authors' argument in *The Stacks Project*, *Varieties*, Tag 09N9, read through the AI Integrated Stacks Project English source edition on 1 October 2026 ([versioned transparent source](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/varieties.tex)). The proof is explained for its use in the integral affineness argument. The Stacks Project itself is distributed under the GNU FDL 1.2 or later.
