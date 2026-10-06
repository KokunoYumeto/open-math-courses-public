# Pinnings and the classification of split reductive groups

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Original contributions are dedicated to the public domain (CC0). The collected lesson also carries the GNU Free Documentation License 1.2 for the explicitly attributed Stacks proof below; see History.*

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

We first record a translation argument that works over any base.

**Lemma 4.1 (extension from the open cell).** Let \(K/S\) be a smooth group with geometrically connected fibres, let \(\Omega\subset K\) be a fibrewise dense open containing the identity, and let \(H/S\) be a separated group scheme. A morphism \(f:\Omega\to H\) with \(f(1)=1\) and

$$
f(xy)=f(x)f(y)\quad\text{whenever }x,y,xy\in\Omega
\tag{4.1}
$$

extends uniquely to a homomorphism \(K\to H\).

**Proof.** This is the word-extension argument of AG-RG-03 Lemma 8.B. A geometrically connected smooth algebraic group is geometrically irreducible: its regular irreducible components are disjoint and open, and connectedness leaves one component. For a test scheme $R\to S$ and finitely many sections $g_i\in K(R)$, the open $\Omega_R\cap\bigcap_i\Omega_Rg_i^{-1}$ has a nonempty open in every geometric fibre of $K_R$. Its morphism to $R$ is smooth and surjective, so it supplies a section after an fppf cover. Apply this also to the dense open $\Omega_R^{-1}$. For any $g\in K(R)$ we can consequently choose $c$ locally with $c,c^{-1},cg\in\Omega_R$. Thus $g=c^{-1}(cg)$ is a word in cell points. Assign to a word $x_1\cdots x_d$ in cell points the product $f(x_1)\cdots f(x_d)$. To compare two words with endpoint $g$, choose $a$ so that $a$ and every translated partial product of either word belong to $\Omega_R$. There are only finitely many such open conditions, so the same smooth surjectivity argument permits this choice. Repeated use of (4.1) shows that multiplying either assigned image word on the left by $f(a)$ gives $f(ag)$. Cancellation proves independence of the word. In particular the image of an identity word is $1$, and the assigned values of words for $g$ and $g^{-1}$ are inverse. The assignments are compatible with fppf pullback and agree on overlaps, so the sheaf property of $H$ descends them to a map $K\to H$. Concatenating words proves multiplicativity. Yoneda gives the scheme morphism. Every extension must have the same values on these locally generating words, proving uniqueness. $\square$

The open cell of a split reductive group is \(\Omega=U^-TU^+\). To construct \(f\) there, maps on individual root groups and \(T\) are enough, provided they respect the normalizer conjugations, the rank-one multiplication and the positive rank-two relations.

Here is the gluing argument in detail. Torus-equivariance and Lemma 2.1 reduce any reordering of positive root factors to (3.1) in a conjugate standard rank-two subgroup. Thus the product of their images defines a homomorphism on \(U^+\), independent of the chosen root order. The same holds on \(U^-\). The resulting cell map satisfies

$$
f(vgu)=f(v)f(g)f(u)
\quad(v\in B^-,\ u\in B^+,\ g\in\Omega).
\tag{4.2}
$$

Indeed, write the three factors in \(U^-TU^+\) coordinates, move torus factors using their character actions, and multiply only within \(U^-\) or \(U^+\).

For a simple representative \(n_\alpha\), split off the \(\pm\alpha\) root factors in the cell. All remaining positive roots stay positive under \(s_\alpha\), and all remaining negative roots stay negative. On the middle factor \(U_{-\alpha}TU_\alpha\), the conjugation identity is the rank-one identity. Equation (4.2) therefore proves

$$
f(n_\alpha g n_\alpha^{-1})
=f_N(n_\alpha)f(g)f_N(n_\alpha)^{-1}
\tag{4.3}
$$

whenever both cell expressions exist. For a word in the representatives, first impose the finitely many open conditions that all intermediate conjugates lie in the cell. This open contains the identity and is fibrewise dense. Induction proves (4.3) there. [AG-RG-S08 Lemma G.3.5](AG-RG-S08.html#universal-schematic-density) proves that this open is universally schematically dense in the full common domain: that domain is an open in the smooth cell with geometrically irreducible fibres. Since the target is separated, the equalizer ideal is zero on the whole domain. The identity consequently holds for every $n\in N_K(T)$, including after nonreduced base changes.

Choose a representative \(n_0\) of the longest Weyl element using an actual reduced word for \(w_0\). It interchanges \(U^+\) and \(U^-\). For \(u\in U^+,v\in U^-\) with \(uv\in\Omega\), the product \(n_0uvn_0^{-1}\) is a negative-positive product and always lies in \(\Omega\). Its cell formula, followed by (4.3), gives \(f(uv)=f(u)f(v)\). Finally, if \(x=vtu\) and \(x'=v't'u'\), then

$$
xx'=vt(uv')t'u'.
$$

Equation (4.2) reduces (4.1) to the case just treated. Lemma 4.1 completes the extension.

## 5. The isomorphism theorem

**Theorem 5.1.** For pinned split reductive groups over a scheme \(S\), isomorphisms preserving the pinnings correspond bijectively to isomorphisms of their based root data. The correspondence commutes with every base change. Over a disconnected base, the datum isomorphism is allowed to be locally constant.

**Proof.** A pinning-preserving group isomorphism gives the based-datum isomorphism by its action on the torus, roots, coroots and frames. Conversely, given an isomorphism of based data, match the tori by their character lattices and match each pinned simple root parameter. Match its linked negative parameter by the perfect pairing. The rank-one formula then matches the simple representatives \(n_\alpha\), their squares \(\alpha^\vee(-1)\), and their action on the torus.

Let \(\mathcal N\) be the sheaf of groups presented by the torus and these representatives, with the torus conjugation rule, the square rule, and the rank-two power relations \(3.2\). Modulo the torus this is the Coxeter presentation proved in AG-RG-04 Theorem 3.4, so \(\mathcal N/T=\underline W\). The natural map \(\mathcal N\to N_G(T)\) is surjective as a sheaf: the representatives lift the simple reflections and every remaining normalizer element differs from one of their products by a torus element. The torus maps identically to the actual torus, hence has no collapse in the presentation. Any element in the kernel is trivial modulo \(T\), since the quotient map is the Weyl-group identity, and is then trivial in \(T\). Therefore \(\mathcal N\simeq N_G(T)\). The same presentation holds for the target, giving an actual normalizer isomorphism.

To define a parameter map at an arbitrary root, transport a pinned simple parameter by a normalizer word. Two transports differ by a root transport that fixes a simple root or carries it to another simple root. AG-RG-05 Lemma 2.2 decomposes this transport into the standard rank-two operations. Each operation intertwines the root parameter maps by the displayed conjugation table; the residual torus multiplies the parameter by the same root character in both groups. The square rule gives the negative parameter. This proves independence of every transport choice. In particular the resulting maps match all normalizer conjugations and all positive and negative rank-two multiplication relations.

Use any ordered root-product coordinates to define the isomorphism of big cells. The reordering formulas prove that the maps on \(U^+\) and \(U^-\) are homomorphisms and independent of the order. Left multiplication by \(B^-\) and right multiplication by \(B^+\) consequently intertwine the cell map. For a simple \(n_\alpha\), separate the two root factors \(U_{\pm\alpha}\) from the remaining factors. The reflection permutes the remaining positive roots amongst positive roots and the remaining negative roots amongst negative roots. On \(U_{-\alpha}TU_\alpha\) the explicit Gauss formula proves equivariance. This proves cell equivariance under each \(n_\alpha\) on its common domain.

For a word of simple representatives impose that all intermediate conjugates stay in the cell. This open contains the identity section. Induction gives equivariance there. The following coordinate argument extends the identity to the entire common domain and includes nilpotent bases.

**Cell density lemma.** Put \(A=R[q_1,\ldots,q_N,z_1^{\pm1},\ldots,z_r^{\pm1}]\), with section \(e\) given by \(q_i=0,z_j=1\). If \(d\in A\) has \(d(e)\in R^\times\), then \(D(d)\) is universally schematically dense in \(\operatorname{Spec}A\), and in every open subscheme of it. Consequently two maps from an open \(V\) containing \(e\) to a separated scheme which agree on a smaller open containing \(e\) agree throughout \(V\), locally on \(\operatorname{Spec}R\).

**Proof.** Substitution \(z_j=1+w_j\) embeds \(A\) in \(R[[q_1,\ldots,q_N,w_1,\ldots,w_r]]\). To verify injectivity, multiply a Laurent polynomial by a monomial in the \(z_j\)'s. Its image then differs by an invertible formal series from the image of an ordinary polynomial. The translation of variables \(z_j=1+w_j\) is an automorphism of the polynomial algebra, so that ordinary polynomial is zero only when it was zero. The image of \(d\) is a unit in the formal power-series ring, since its constant term is \(d(e)\). Multiplication by \(d\) is therefore injective on \(A\). It remains injective after any localization, and the same proof applies after every change of \(R\). Hence \(A_q\to(A_q)_d\) is injective on every principal chart \(D(q)\). This proves universal schematic density in every open.

If an open \(U\subset V\) contains the identity, choose for each point of the base a principal open \(D(d)\subset U\) about that identity point. Shrinking the base to make \(d(e)\) invertible gives the preceding density statement. The equalizer of the two maps to the separated target is closed in \(V\). Its ideal vanishes after restriction to \(D(d)\), and injectivity on each principal chart makes that ideal zero on \(V\). The maps are equal. \(\square\)

Apply the lemma to the root-product coordinates of \(\Omega=U^-TU^+\). Both the full common domain and the intermediate-conjugate domain are opens in this cell containing the identity. Thus the equivariance identity extends to the full common domain without an external schematic-density theorem.

Choose a genuine reduced word for the longest Weyl element, allowing repetitions. Its representative interchanges \(U^+\) and \(U^-\). If \(u\in U^+\), \(v\in U^-\) and \(uv\) is in the cell, conjugation turns \(uv\) into a negative-positive product, whose image is already a product of the images of its factors. The equivariance just proved then gives \(f(uv)=f(u)f(v)\). For general cell points \(x=vtu\), \(x'=v't'u'\), use

\[
xx'=vt(uv')t'u'
\]

and the left/right triangular equivariance to obtain partial multiplicativity. the preceding rank-one lesson, Lemma 8.B extends the cell map to the entire group. Constructing the inverse from the inverse datum and using that lemma's uniqueness gives a group isomorphism. The same uniqueness proves that no second pinning-preserving isomorphism induces the chosen datum map. Because character maps, root parameters, scheme identities and fppf descent commute with base change, the construction does too. On disconnected bases the datum map is locally constant, and the construction is applied to its open-and-closed fibres. $\square$

The pinning is essential for uniqueness. Conjugation by an element of \(T\) preserves the torus and positive system and scales \(E_\alpha\) by \(\alpha(t)\). It preserves every frame precisely when it belongs to the centre.

## 6. Constructing the simply connected group in characteristic zero

The preceding lesson [Lie proofs for the characteristic-zero group construction](AG-RG-S06.md) supplies the entire Lie argument. Its Theorem 1.A proves the ordered-word basis and the relation-ideal assertion; Theorem 6.2 constructs the rational split semisimple algebra by the Serre relations; Section 7 proves the nonzero finite highest-weight presentation (7.6); and Section 8 proves the rational rank-one integration and faithful action used here. These proofs precede this construction and do not assume a group existence theorem.

Let \(\Phi\) be a reduced semisimple root system, \(Q=\mathbf Z\Phi\) its root lattice and \(P\) its weight lattice. Theorem 6.2 gives \(\mathfrak g/\mathbf Q\) with exactly those roots. For a dominant integral \(\lambda\), Section 7 forms the cyclic quotient with relations \(e_jv=0\), \(h_jv=\langle\lambda,\alpha_j^\vee\rangle v\), and \(f_j^{\langle\lambda,\alpha_j^\vee\rangle+1}v=0\). The ordered-word basis proves that its top vector survives. Local nilpotence of the simple root operators gives Weyl-invariant weights. Every occurring weight \(\mu\) satisfies both \(\lambda-\mu\in Q^+\) and \(\mu-w_0\lambda\in Q^+\); hence it lies in a finite integral box, with finite-dimensional weight spaces. Only after this proves finite dimension does Theorem 4.2 give complete reducibility and the cyclic, one-dimensional top imply irreducibility. Exact base change of this rational presentation proves absolute irreducibility over every characteristic-zero extension. Apply this to the fundamental weights and put \(V_i=L_{\mathbf Q}(\omega_i)\) and \(V=\bigoplus_iV_i\).

For every root vector \(e_\alpha\), its action on \(V\) is nilpotent. Define the polynomial matrix

$$
x_\alpha(u)=\exp(u e_\alpha)
=\sum_{j\geq0}\frac{u^j e_\alpha^j}{j!}
\quad(u\in\mathbf G_{a,\mathbf Q}).
$$

**Lemma 6.1 (polynomial rank-one actions).** The irreducible finite-dimensional complex \(\mathfrak{sl}_2\)-modules are \(\operatorname{Sym}^n(\mathbf C^2)\), for \(n\geq0\), with weights \(n,n-2,\ldots,-n\); every finite-dimensional module is their direct sum. Every finite-dimensional rational representation of \(\mathfrak{sl}_2\) integrates to a polynomial representation of \(\operatorname{SL}_{2,\mathbf Q}\). On its summands of highest weight \(n\), the upper and lower root groups act by \(\exp(xe)\) and \(\exp(xf)\), and the diagonal torus acts on weight \(m\) by \(z^m\).

**Proof.** Begin with \(W_n=\operatorname{Sym}^n(\mathbf Q^2)\), written as the degree-\(n\) polynomials in the basis vectors \(u,v\). For every \(\mathbf Q\)-algebra \(A\), a matrix \(g=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\in\operatorname{SL}_2(A)\) acts by

$$
u\longmapsto au+cv,\qquad v\longmapsto bu+dv.
$$

The coefficients on the monomial basis \(u^{n-j}v^j\) are polynomials in \(a,b,c,d\). Acting successively by \(h\) and \(g\) sends each basis vector to its image under \(gh\); hence these substitutions define a group-scheme representation. The identity acts identically, and the substitution for \(g^{-1}\) is its inverse. Differentiating gives

$$
e=u\frac{\partial}{\partial v},\qquad
f=v\frac{\partial}{\partial u},\qquad
h=u\frac{\partial}{\partial u}-v\frac{\partial}{\partial v}.
$$

An upper unipotent matrix fixes \(u\) and replaces \(v\) by \(v+xu\); the finite Taylor formula is exactly \(\exp(xe)\). A lower unipotent matrix similarly gives \(\exp(xf)\). The diagonal matrix \(\operatorname{diag}(z,z^{-1})\) multiplies \(u^{n-j}v^j\) by \(z^{n-2j}\). These identities hold over every \(\mathbf Q\)-algebra.

Here is the finite-dimensional weight argument. In an irreducible complex module, choose an eigenvector of \(h\). Applying \(e\) raises its eigenvalue by two; the finite set of eigenvalues makes this process end at a nonzero \(w\) with \(ew=0\), \(hw=\lambda w\). The commutator relations give, by induction,

$$
hf^jw=(\lambda-2j)f^jw,\qquad
ef^jw=j(\lambda-j+1)f^{j-1}w.
$$

The first identity follows from \([h,f]=-2f\). For the second, commute \(e\) past one more \(f\): the new coefficient is \((\lambda-2j)+j(\lambda-j+1)=(j+1)(\lambda-j)\). There is a last nonzero vector \(f^nw\), again because the eigenvalues are distinct and the module is finite. Applying the second identity at \(j=n+1\) gives \((n+1)(\lambda-n)f^nw=0\), hence \(\lambda=n\). The string spans a nonzero submodule, so is the entire irreducible module. Its operators agree with those on \(W_n\) by the map \(f^ju^n\mapsto f^jw\). Conversely \(W_n\) is irreducible: its distinct one-dimensional \(h\)-weight spaces split every invariant subspace, and repeated \(e\) carries any nonzero weight vector to \(u^n\); repeated \(f\) then gives all of \(W_n\). Weyl complete reducibility, proved in the preceding Lie lesson, Theorem 4.2, now gives the assertion for every finite-dimensional complex module.

For a general rational module \(M\), that argument after extension to \(\mathbf C\) gives a direct sum of these modules. The rational highest-vector spaces

$$
K_n=\ker(e:M\to M)\cap\ker(h-n:M\to M)
$$

commute with field extension because they are kernels of rational linear maps. For \(w\in K_n\), send \(f^ju^n\) to \(f^jw\), for \(0\leq j\leq n\). The identity \(ef^jw=j(n-j+1)f^{j-1}w\) and \(hf^jw=(n-2j)f^jw\) prove equivariance. The relation \(f^{n+1}w=0\) follows over \(\mathbf C\) from the weight theorem and therefore over \(\mathbf Q\). These maps give

$$
\bigoplus_{n\geq0}W_n\otimes_{\mathbf Q}K_n\longrightarrow M.
$$

Only finitely many summands occur. After extension to \(\mathbf C\), the highest-vector classification makes this map an isomorphism; faithful flatness makes it an isomorphism over \(\mathbf Q\). Transport the displayed polynomial actions through it. Their differentials and root and torus formulas are the prescribed ones. \(\square\)

Let \(T=D_\mathbf Q(P)\) act on \(V_\mu\) through the character \(\mu\). The highest-weight vectors have characters \(\omega_i\); these generate \(P\), so this torus representation is faithful. Let \(G\) be the reduced algebraic closure of the subgroup of \(\operatorname{GL}(V)\) generated by \(T\) and all \(x_\alpha\). It is an algebraic group: multiplication and inversion preserve the closure, as can be checked first with one argument in the generating subgroup and then by density with both arguments. It is connected because the generating torus and additive groups are connected. Theorem G.3.4 of [Supporting group-scheme proofs](AG-RG-S08.md) proves that this finite-type characteristic-zero group is smooth.

We prove its Lie algebra is exactly \(\mathfrak g\). The representation \(\rho:\mathfrak g\to\operatorname{End}(V)\) is faithful: its kernel is an ideal, and each simple factor acts nontrivially in one of its fundamental modules. The torus and root exponentials normalize \(\rho(\mathfrak g)\). Hence \(G\) lies in its linear normalizer, whose Lie algebra is

$$
\{A:[A,\rho(\mathfrak g)]\subset\rho(\mathfrak g)\}.
$$

For such an \(A\), commutation defines a derivation of \(\mathfrak g\). The preceding Lie lesson, Proposition 3.1, proves nondegeneracy of the Killing form; Proposition 3.3 proves the needed inner-derivation assertion. Its short calculation is repeated here. For a derivation $D$, nondegeneracy of the Killing form $\kappa$ gives $z$ with $\kappa(z,x)=\operatorname{tr}(D\operatorname{ad}x)$ for all $x$. Set $E=D-\operatorname{ad}z$. Then $\operatorname{tr}(E\operatorname{ad}x)=0$, and

$$
0=\operatorname{tr}(E\operatorname{ad}[x,y])
=\operatorname{tr}([E,\operatorname{ad}x]\operatorname{ad}y)
=\kappa(Ex,y).
$$

Nondegeneracy makes $E=0$. This proof applies directly over $\mathbf Q$. Thus

$$
A\in\rho(\mathfrak g)+\operatorname{End}_{\mathfrak g}(V).
\tag{6.1}
$$

After algebraic closure, the distinct irreducible \(V_i\) have commutant consisting of one scalar on each summand. On the other hand every generator of \(G\) has determinant one on each \(V_i\). For exponentials this follows from nilpotence. For \(T\), the determinant character is the sum of the weights with multiplicity; its differential is the trace of \(\mathfrak h\) on \(V_i\), which is zero because \(\mathfrak g=[\mathfrak g,\mathfrak g]\). In characteristic zero a character with zero differential is zero. Therefore

$$
G\subset\prod_i\operatorname{SL}(V_i).
$$

In (6.1) a scalar on \(V_i\) has trace \((\dim V_i)c_i\). The trace condition makes every \(c_i=0\). It follows that \(\operatorname{Lie}(G)\subset\rho(\mathfrak g)\). The reverse inclusion follows from the torus and root-group tangent vectors, which span \(\mathfrak g\). We have equality.

We check reductivity and semisimplicity over an algebraic closure $k$ of $\mathbf Q$. Let $N\subset G_k$ be any smooth connected normal unipotent subgroup. In the unitriangular characterization of unipotent groups used in AG-RG-01 Lemma 2.A, its Lie algebra embeds in the strictly upper triangular matrices and is nilpotent: a bracket of $j$ such matrices lies in the $j$th power of that strictly upper triangular algebra, which is zero for large $j$. Normality makes $\operatorname{Lie}N$ an ideal in $\operatorname{Lie}G_k=\mathfrak g_k$; this follows by differentiating conjugation, as in *Lie algebras and smoothness*, Theorem 2.9. Semisimplicity of $\mathfrak g_k$ gives $\operatorname{Lie}N=0$. Since $N$ is smooth, its dimension is zero; over the algebraically closed field a connected smooth zero-dimensional group is the identity. The geometric reductivity criterion of AG-RG-01 Section 1 therefore makes $G$ reductive.

The closed centre is represented by the coefficient proof in *Group schemes over a field*, Proposition 5.3. Its Lie algebra is contained in the centre of $\mathfrak g_k$, by the centralizer tangent calculation in Theorem 2.9, and is therefore zero. The characteristic-zero Cartier theorem, [AG-RG-S08 Theorem G.3.4](AG-RG-S08.html), makes this finite-type closed subgroup smooth; hence it is zero-dimensional. A zero-dimensional affine finite-type $k$-algebra is finite-dimensional by the written proof in [AG-RG-S04 Lemma P0.9](AG-RG-S04.html): it has finitely many local Artinian factors, and the finite nilradical filtrations have finite-dimensional layers over residue fields that are finite over $k$. Thus the centre of $G_k$ is finite, and finite-dimensionality descends over the field extension: independent vectors stay independent after tensoring with $k$. A reductive group with finite centre has trivial radical, by the character-lattice definition in AG-RG-03 Section 1, so $G$ is semisimple.

The torus $T$ is geometrically maximal. Indeed, its Lie algebra is $\mathfrak h_k$, and the root decomposition gives $C_{\mathfrak g_k}(\mathfrak h_k)=\mathfrak h_k$: each root is a nonzero linear functional in characteristic zero. A torus $T'\supset T_k$ would have its Lie algebra in this centralizer, so its dimension would equal that of $T_k$. The closed inclusion of these split tori corresponds to a surjection of free character lattices of that same rank, hence an isomorphism. Thus $T'=T_k$. Its adjoint root spaces and their $T$-characters are exactly the prescribed $\Phi$.

The Lie algebra for each simple root is an \(\mathfrak{sl}_2\). On each finite-dimensional module its exponential matrices and diagonal weight matrices give the usual algebraic \(\operatorname{SL}_2\) action, by Lemma 6.1. Its diagonal torus is the cocharacter of \(D(P)\) pairing with \(\mu\) by \(\langle\mu,\alpha^\vee\rangle\). The rank-one Gauss characterization identifies it with the group coroot. Hence

$$
\mathcal R(G,T)=(P,\Phi,P^*,\Phi^\vee).
\tag{6.2}
$$

This is the simply connected datum: its cocharacter lattice \(P^*\) is the coroot lattice. The construction is over \(\mathbf Q\), which will let us check integral polynomial identities in one characteristic-zero fibre.

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

For the next construction we need the partial translations to be open isomorphisms with dense domains and images in every fibre. This can be arranged without a characteristic restriction. For either universal translation map

$$
(x,y)\longmapsto(x,m(x,y)),\qquad
(x,y)\longmapsto(m(x,y),y),
\tag{7.6}
$$

the differential is an isomorphism along both identity axes. Here is a way to check the potentially nontrivial differential. Factor an arbitrary \(x\) into its ordered negative root factors, its torus factor, and its ordered positive root factors. Left translation by these successive factors is defined at the successive suffixes of this factorization: a negative or torus factor uses \(B^-\times X\), and a positive factor encounters a suffix in \(U^+\). Translation by its inverse is defined at the resulting point by the same conditions. The inverse identity, checked over \(\mathbf Q\), makes these local maps mutually inverse on neighborhoods. Their composition is left translation by \(x\) near \(e\), so that translation is a local isomorphism there. Ordered prefixes give the corresponding assertion for right translation. The argument works with the universal coordinates and therefore after every base change.

Restrict (7.6) to the open on which both maps are étale. It contains both identity axes. Each map is separated, quasi-finite and birational between integral normal Noetherian schemes smooth over \(\mathbf Z\), so [the preceding Zariski Main supporting lesson](AG-RG-S04.md), Corollary D7.4, makes it an open immersion. Its images, and the domain, are dense relative to both projections: each slice contains the corresponding identity-axis point and is a nonempty open in an irreducible geometric fibre. The graph of this restricted multiplication consequently has all three pair projections open, with dense slices. This is a **strict partial group law** on \(X\).

## 8. Completing a strict partial group law

We give the construction rather than assuming a group already exists. This is the translation method of Weil and Artin; the algebraic-space quotient in the final step is the exact bootstrap prerequisite identified below.

**Lemma 8.1.** Suppose \(X/S\) is smooth, separated and of finite presentation, with geometrically irreducible nonempty fibres. Suppose \(X\) has a strict associative partial group law, an identity section, and partial inversion, with the translation maps defined and invertible locally along both identity axes. Then there is a unique smooth separated group algebraic space \(K/S\) of finite presentation containing \(X\) as a fibrewise dense open and extending its partial group law. Formation of \(K\) commutes with base change.

**Proof.** On each \(S\)-scheme \(R\), consider germs of isomorphisms between fibrewise dense open subschemes of \(X_R\); two representatives agree if they agree on such an open. Finite intersections of dense opens remain dense, and composition and inversion make these germs a group. Apply [AG-RG-S08 Lemma G.3.5](AG-RG-S08.html#universal-schematic-density) on every common open domain. Its fibres are nonempty opens of the geometrically irreducible smooth fibres of $X_R$, so they are geometrically irreducible. Consequently two representatives equal as germs agree on their entire common domain, since $X_R$ is separated. Their domains and their inverse domains can therefore be united and their maps glued to a largest representative isomorphism.

Here is effectiveness of fppf descent without assuming that this largest domain commutes with a flat pullback. Let $R'\to R$ be an fppf cover, and let a descent datum of germs be represented by an isomorphism $h':D'\xrightarrow{\sim}E'$ of fibrewise dense opens of $X_{R'}$. An fppf covering family is handled by the disjoint union of its members and the same argument. Let $O,P\subset X_R$ be the open images of $D',E'$ respectively; they are open by the arbitrary-base openness proof in [*Flat morphisms*, Theorem 3.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-FSE/flat-morphisms.html#3-what-flatness-does-to-the-topology): flatness lifts generizations, the finite-presentation image is constructible by [*Quasi-finite morphisms and Chevalley*, Theorem 5.1](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-MO/quasi-finite-morphisms-and-chevalley.html#5-chevalley-by-noetherian-approximation), and constructibly compact specialization-stable complements are closed. The maps $D'\to O$ and $E'\to P$ are faithfully flat covering maps. On $D'\times_O D'=D'\times_{X_R}D'$, the two maps $h'$ to $X_R$ agree. Indeed this overlap is the intersection of the two pulled-back dense domains inside $X_{R'\times_RR'}$; the cocycle says that the two germs agree there, and Lemma G.3.5 makes their representatives equal on that entire intersection. Morphism descent from [AG-RG-S04 Lemma A1.5](AG-RG-S04.html) descends $h'$ to a map $h:O\to X_R$. It factors through $P$, because this can be checked on the faithfully flat cover $D'\to O$. Descend $(h')^{-1}$ in the same way to $P\to O$. Their composites are the identities, as is checked on $D'$ and $E'$. Thus $h:O\xrightarrow{\sim}P$ is an isomorphism. Both $O$ and $P$ are fibrewise dense: after a field extension supplied by a point of the covering base, their fibres contain the images of the dense fibres of $D'$ and $E'$. The descended isomorphism represents the required germ, and its pullback agrees with the initial germ on $D'$. Uniqueness follows from the same common-domain equality and faithfully flat morphism descent. The germs therefore form an fppf sheaf. Write \(\operatorname{Bir}(X)\) for this sheaf.

For \(a\in X(R)\), partial left translation defines a germ \(L_a\), and right translation defines a germ \(R_a\). Strictness supplies their dense isomorphic domains and images. Associativity implies that the left translations commute with all right translations, and \(L_aL_b=L_{ab}\) whenever the partial product exists. Let \(K\) be the subgroup sheaf generated by the \(L_a\).

A germ \(g\in K(R)\) that is defined at one section \(x\) and fixes it is the identity. Indeed, \(g\) fixes every partial product \(xb\) where that product and \(g\) are defined, since it commutes with \(R_b\). These points form a fibrewise dense open, by strictness. This proves the claim. Likewise \(a\mapsto L_a\) is injective: if \(L_a=L_b\), choose a section \(z\) in their common dense domains fppf locally. The two partial products \(az=bz\) and the injectivity of partial right translation give \(a=b\).

The injection \(X\to K\) is an open immersion. To check it, take \(g\in K(R)\), let \(D_g\subset X_R\) be a representative domain, and retain points \(z\) for which the partial division of \(g(z)\) by \(z\) exists. This is an open \(E\subset D_g\), whose image \(O\subset R\) is open because \(X_R\to R\) is smooth. On \(E\), that division gives \(a\in X(E)\) with \(L_a=g\): their quotient fixes \(z\), so the preceding claim applies. The injectivity just proved makes these local \(a\)'s agree on \(E\times_OE\), and they descend to \(a\in X(O)\). Conversely, if \(g=L_a\) after a base change, the dense slice conditions provide such \(z\) locally. This is precisely the universal property of \(R\times_KX=O\).

Every germ \(g\in K(R)\) can fppf locally be written

$$
g=L_aL_b^{-1}\quad(a,b\in X).
\tag{8.1}
$$

Choose \(b\) in its representative dense domain and put \(a=g(b)\). The germs \(L_b,L_a\) are invertible on neighborhoods of \(e\), taking \(e\) to \(b,a\). Thus \(L_a^{-1}gL_b\) is defined at \(e\) and fixes it, so it is the identity. The choices of \(b\) form a smooth surjective open of \(X_R\).

More precisely, the fibre of

$$
\delta:X\times_SX\longrightarrow K,\qquad
(a,b)\longmapsto L_aL_b^{-1}
\tag{8.2}
$$

over a germ \(g\) is the graph \(a=g(b)\) on the intersection of the translated \(X\)-charts. This is an open in \(X_R\), and is fibrewise dense by the preceding construction. Hence \(\delta\) is representable, smooth and surjective. Its equivalence relation is a scheme explicitly: write a related pair as \(((a,b),(c,d))\). The equality \(L_aL_b^{-1}=L_cL_d^{-1}\) says that \(b\) belongs to the translated-chart domain of the universal germ \(L_cL_d^{-1}\), and that \(a=(L_cL_d^{-1})(b)\). Thus the relation is the graph of that evaluation, parametrized by an open subscheme of \(X^3\) with coordinates \((c,d,b)\). The domain is open because representative domains of the universal germ are open and their union is its maximal domain. Both projections are smooth, being base changes of \(\delta\). Theorem 8.2 of [Flat quotient bootstrap](AG-RG-S07.md) applies to this explicit relation: its endpoint map is a monomorphism on all test schemes, and its smooth projections are flat and locally finitely presented. Its fppf quotient is therefore an algebraic space, with this relation as its equality relation. The sheaf quotient is precisely \(K\), by (8.1). Smoothness of $K/S$ follows from the representable smooth surjection (8.2), whose source $X\times_SX$ is smooth over $S$. In particular $K/S$ is locally of finite presentation. Over each affine open of $S$, the source of (8.2) is quasi-compact, so surjectivity makes $K$ quasi-compact over that open. The separation argument in the next paragraph makes $K/S$ separated and hence quasi-separated. Thus $K/S$ is locally of finite presentation, quasi-compact and quasi-separated, which proves finite presentation. This argument works over the given base and does not require the open relation in $X^3$ to be quasi-compact in advance. Each geometric fibre of $K$ is irreducible, since it is the surjective image of the irreducible fibre of $X\times_SX$.

For completeness, separation can be checked on every scheme test $R\to K\times_SK$. Write its two sections as $a,b\in K(R)$ and consider the open
\[
E=a^{-1}X_R\cap b^{-1}X_R\subset K_R.
\]
Each geometric fibre of $K_R$ is irreducible by (8.2), and each translate of $X_R$ is a nonempty open in that fibre. Their intersection is therefore nonempty, so $E\to R$ is smooth and surjective. A scheme atlas of $E$ supplies an fppf scheme covering $R_i\to R$ and sections $t_i\in E(R_i)$. Right multiplication by $t_i$ puts both $a$ and $b$ in $X_{R_i}$. The equalizer of $a$ and $b$ over $R_i$ is exactly the equalizer of $at_i$ and $bt_i$, by cancellation in the group sheaf. The latter is a closed subscheme because $X/S$ is separated. This is an equality of functors on every further test scheme, so the pullback of the diagonal of $K/S$ is a closed immersion after the fppf covering. Closed immersions descend by AG-RG-S04 Corollary A3.2; thus the tested diagonal is a closed immersion over $R$. Since the test was arbitrary, the diagonal of $K/S$ is closed. This proves separation over the given base, including nonreduced bases.

In each geometric fibre, the open \(X\) and all its translates have dense pairwise intersections. They cover \(K\) by (8.2), so \(X\) is dense and the fibre is irreducible. A second extension acts on \(X\) by the same translation germs and, by (8.2), is generated by them. This gives the unique isomorphism between two extensions. The construction uses sheaves, dense-slice conditions and open immersions, all preserved by base change, proving the final assertion. \(\square\)

Apply this lemma to (7.1). We obtain a smooth separated group algebraic space \(G_{\mathbf Z}\), containing \(X\), with generic fibre the characteristic-zero group already constructed. The torus and root subgroups embed in it and have their prescribed multiplication. Conjugation identities between their morphisms hold over \(\mathbf Z\), because their sources are flat and they hold over \(\mathbf Q\).

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

This lesson's new exposition, group constructions, calculations, examples and solutions were written by GPT-6.1 Sol (OpenAI), Ultra setting, in October 2026, and are dedicated to the public domain under CC0.

The one-dimensional affine-open lemma and its full proof are adapted from the Stacks authors, *The Stacks Project*, *Varieties*, Tag 09N9, through the AI Integrated Stacks Project English source edition read on 1 October 2026. The Stacks authors retain copyright in that material. The source is the [versioned transparent source](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/varieties.tex). Its proof is included and explained for use in the integral affineness argument.

This collected lesson, *Pinnings and the classification of split reductive groups* (2026), is published by Open Mathematics Courses. The Stacks authors are the authors of its imported proof; GPT-6.1 Sol (OpenAI) is responsible for the new contributions and adaptation. Permission is granted to copy, distribute and modify this collected lesson under the GNU Free Documentation License, Version 1.2, with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. An unaltered copy of the licence is supplied as [GNU Free Documentation License 1.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-RG/assets/GFDL-1.2.txt). This additional licence for the collected lesson does not withdraw the CC0 dedication of its original contributions.
