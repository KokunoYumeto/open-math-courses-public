# Pinnings and the classification of split reductive groups

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI, GPT-6.1 Sol (OpenAI). Original contributions are dedicated to the public domain (CC0). The collected lesson also carries the GNU Free Documentation License 1.2 for the explicitly attributed Stacks proof below; see History.*

The integral root datum remembers a reductive group up to isomorphism. A pinning removes the conjugation ambiguity and makes this assertion functorial. The main work is to show that the multiplication of root groups is forced by the datum, including over rings in which two or three vanish. We first do those calculations and glue them across the open cell. We then construct groups in characteristic zero and pass to an integral model.

Throughout, a split group has a specified split maximal torus, a constant identification of its character lattice, and trivial root lines. All assertions about a base scheme allow nilpotents and arbitrary characteristic. On a disconnected base, maps of constant data are locally constant; they need not have one value on every component. The purely combinatorial Coxeter presentation and length formula are the precise prerequisites from [Root systems and their Weyl groups](https://kokunoyumeto.github.io/open-math-courses-public/courses/RT-LIE/RT-LIE-08.html), identified at the end.

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

**Proof.** Points of \(\Omega\) generate \(K\) fppf locally: for a point \(g\), the open intersection \(\Omega\cap g^{-1}\Omega\) is smooth surjective over its base, since every geometric fibre is irreducible. A point \(a\) of this intersection expresses \(g=(ga)a^{-1}\); by further open intersections one can take all factors in \(\Omega\).

To show that a product of images is independent of a word, consider two words with the same endpoint. The intersection of the open conditions requiring \(a\) and every translated partial product of both words to lie in \(\Omega\) is again smooth surjective. On this cover, (4.1) identifies \(f(a)\) times each image word with \(f(a\,g)\). Cancellation proves equality. The local definition therefore descends to a map of fppf sheaves and is multiplicative. Yoneda supplies the scheme morphism. Uniqueness follows from the same word argument. \(\square\)

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

whenever both cell expressions exist. For a word in the representatives, first impose the finitely many open conditions that all intermediate conjugates lie in the cell. This open contains the identity and is fibrewise dense. Induction proves (4.3) there. Equality extends to the full common domain: an open dense in every fibre of a smooth scheme is schematically dense, including over nonreduced bases, and the target is separated. The identity consequently holds for every \(n\in N_K(T)\).

Choose a representative \(n_0\) of the longest Weyl element using an actual reduced word for \(w_0\). It interchanges \(U^+\) and \(U^-\). For \(u\in U^+,v\in U^-\) with \(uv\in\Omega\), the product \(n_0uvn_0^{-1}\) is a negative-positive product and always lies in \(\Omega\). Its cell formula, followed by (4.3), gives \(f(uv)=f(u)f(v)\). Finally, if \(x=vtu\) and \(x'=v't'u'\), then

$$
xx'=vt(uv')t'u'.
$$

Equation (4.2) reduces (4.1) to the case just treated. Lemma 4.1 completes the extension.

## 5. The isomorphism theorem

**Theorem 5.1.** For pinned split reductive groups over a scheme \(S\), isomorphisms preserving the pinnings correspond bijectively to isomorphisms of their based root data. The correspondence commutes with every base change. Over a disconnected base, the datum isomorphism is allowed to be locally constant.

**Proof.** A group isomorphism preserving the pinning clearly supplies the datum isomorphism. Conversely let a datum isomorphism be given. It defines an isomorphism \(f_T:T\to T'\), and isomorphisms \(f_\alpha:U_\alpha\to U'_\alpha\) for simple roots by matching their frames. Match also the dual negative frames and \(n_\alpha\) with \(n'_\alpha\).

These assignments extend to an isomorphism of normalizers. To see that there are no unspecified relations here, take the group sheaf generated by \(T\) and letters \(n_\alpha\), with the conjugation relations in (1.2), their square relations, and (3.2). Its quotient by \(T\) is the constant Weyl group by its Coxeter presentation. The map to \(N_G(T)\) is surjective, since the representatives lift the simple reflections. It is injective on \(T\), since their prescribed relations hold in the actual group. Its kernel thus vanishes: modulo \(T\) the map is an isomorphism, and on \(T\) it is the identity. The same presentation applies to \(N_{G'}(T')\). This proves the asserted normalizer isomorphism \(f_N\).

Extend the simple-root maps by transport: if \(n\alpha=\gamma\), use conjugation by \(n\) on the source and by \(f_N(n)\) on the target. This is independent of the choice. For two choices, their quotient transports one simple root to another. Lemma 2.2 factors that operation into rank-two operations. In each such group the conjugation table in Section 3 intertwines the chosen simple-root maps, including the factors fixing a simple root. A residual torus factor scales its root coordinate by the same character on both sides. The square relation handles negative roots. Thus the maps \(f_\gamma\) are well defined and intertwine all normalizer conjugations.

On the centralizer of the kernel of a simple root, the maps on \(T,U_\alpha,U_{-\alpha}\) respect the Gauss formula

$$
x_\alpha(u)x_{-\alpha}(v)
=x_{-\alpha}\!\left(\frac{v}{1+uv}\right)
\alpha^\vee(1+uv)
x_\alpha\!\left(\frac{u}{1+uv}\right).
\tag{5.1}
$$

The cell argument of Lemma 4.1 gives its rank-one homomorphism. In every positive rank-two subgroup, the tables (3.1) give a homomorphism on its ordered root product. The gluing argument of Section 4 now extends the cell map to \(f:G\to G'\). Applying the same construction to the inverse datum gives an inverse homomorphism: the compositions are the identity on \(T\) and all simple root frames and hence on every root group and on the open cell. Lemma 4.1 makes them the identity everywhere.

The same argument proves uniqueness. All constructions are scheme-theoretic identities and use only the prescribed datum and pinning, so commute with arbitrary base change and descend across open decompositions. \(\square\)

The pinning is essential for uniqueness. Conjugation by an element of \(T\) preserves the torus and positive system and scales \(E_\alpha\) by \(\alpha(t)\). It preserves every frame precisely when it belongs to the centre.

## 6. Constructing the simply connected group in characteristic zero

This step uses the Lie-algebra construction and highest-weight results identified precisely in the prerequisite list. It does not assume the group existence theorem.

Let \(\Phi\) be a reduced semisimple root system, \(Q=\mathbf Z\Phi\) its root lattice and \(P\) its weight lattice. The Serre presentation gives a split semisimple Lie algebra \(\mathfrak g/\mathbf Q\) with this root system, and highest-weight theory gives the rational irreducible modules \(V_i=L(\omega_i)\) for the fundamental weights. One can obtain these rational objects directly from their presentations: impose the rational Serre relations, and the rational highest-weight relations \(f_j^{\langle\omega_i,\alpha_j^\vee\rangle+1}v_i=0\). After scalar extension to \(\mathbf C\), highest-weight theory makes these integrable presentations finite-dimensional. Weyl complete reducibility makes each simple: its generating highest vector lies in its sole summand of that highest weight, and generates the entire module. The dimensions, simplicity and weight decomposition therefore descend to the rational presentations. The exact supporting result is [Complete reducibility](https://kokunoyumeto.github.io/open-math-courses-public/courses/RT-LIE/RT-LIE-04.html). Put \(V=\bigoplus_iV_i\).

For every root vector \(e_\alpha\), its action on \(V\) is nilpotent. Define the polynomial matrix

$$
x_\alpha(u)=\exp(u e_\alpha)
=\sum_{j\geq0}\frac{u^j e_\alpha^j}{j!}
\quad(u\in\mathbf G_{a,\mathbf Q}).
$$

Let \(T=D_\mathbf Q(P)\) act on \(V_\mu\) through the character \(\mu\). The highest-weight vectors have characters \(\omega_i\); these generate \(P\), so this torus representation is faithful. Let \(G\) be the reduced algebraic closure of the subgroup of \(\operatorname{GL}(V)\) generated by \(T\) and all \(x_\alpha\). It is an algebraic group: multiplication and inversion preserve the closure, as can be checked first with one argument in the generating subgroup and then by density with both arguments. It is connected because the generating torus and additive groups are connected. In characteristic zero it is smooth.

We prove its Lie algebra is exactly \(\mathfrak g\). The representation \(\rho:\mathfrak g\to\operatorname{End}(V)\) is faithful: its kernel is an ideal, and each simple factor acts nontrivially in one of its fundamental modules. The torus and root exponentials normalize \(\rho(\mathfrak g)\). Hence \(G\) lies in its linear normalizer, whose Lie algebra is

$$
\{A:[A,\rho(\mathfrak g)]\subset\rho(\mathfrak g)\}.
$$

For such an \(A\), commutation defines a derivation of \(\mathfrak g\). Whitehead's first lemma makes every derivation inner, first over $\mathbf C$ and then over $\mathbf Q$ by faithful-flat descent of the linear derivation equations. Thus

$$
A\in\rho(\mathfrak g)+\operatorname{End}_{\mathfrak g}(V).
\tag{6.1}
$$

After algebraic closure, the distinct irreducible \(V_i\) have commutant consisting of one scalar on each summand. On the other hand every generator of \(G\) has determinant one on each \(V_i\). For exponentials this follows from nilpotence. For \(T\), the determinant character is the sum of the weights with multiplicity; its differential is the trace of \(\mathfrak h\) on \(V_i\), which is zero because \(\mathfrak g=[\mathfrak g,\mathfrak g]\). In characteristic zero a character with zero differential is zero. Therefore

$$
G\subset\prod_i\operatorname{SL}(V_i).
$$

In (6.1) a scalar on \(V_i\) has trace \((\dim V_i)c_i\). The trace condition makes every \(c_i=0\). It follows that \(\operatorname{Lie}(G)\subset\rho(\mathfrak g)\). The reverse inclusion follows from the torus and root-group tangent vectors, which span \(\mathfrak g\). We have equality.

The solvable radical of the smooth connected linear group \(G\) has a solvable Lie ideal in \(\mathfrak g\). It is zero, so that radical is zero and \(G\) is semisimple. The torus \(T\) is maximal: its Lie algebra is the Cartan subalgebra \(\mathfrak h\), whose centralizer in \(\mathfrak g\) is itself; a larger torus would give a larger commuting semisimple subalgebra. Its adjoint root spaces and their \(T\)-characters are exactly the prescribed \(\Phi\).

The Lie algebra for each simple root is an \(\mathfrak{sl}_2\). On each finite-dimensional module its exponential matrices and diagonal weight matrices give the usual algebraic \(\operatorname{SL}_2\) action, by the explicit \(\mathfrak{sl}_2\) representation formulas. Its diagonal torus is the cocharacter of \(D(P)\) pairing with \(\mu\) by \(\langle\mu,\alpha^\vee\rangle\). The rank-one Gauss characterization identifies it with the group coroot. Hence

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

Restrict (7.6) to the open on which both maps are étale. It contains both identity axes. Each map is separated, quasi-finite and birational between integral normal Noetherian schemes smooth over \(\mathbf Z\), so the internal Zariski Main Theorem makes it an open immersion. Its images, and the domain, are dense relative to both projections: each slice contains the corresponding identity-axis point and is a nonempty open in an irreducible geometric fibre. The graph of this restricted multiplication consequently has all three pair projections open, with dense slices. This is a **strict partial group law** on \(X\).

## 8. Completing a strict partial group law

We give the construction rather than assuming a group already exists. This is the translation method of Weil and Artin; the algebraic-space quotient in the final step is the exact bootstrap prerequisite identified below.

**Lemma 8.1.** Suppose \(X/S\) is smooth, separated and of finite presentation, with geometrically irreducible nonempty fibres. Suppose \(X\) has a strict associative partial group law, an identity section, and partial inversion, with the translation maps defined and invertible locally along both identity axes. Then there is a unique smooth separated group algebraic space \(K/S\) of finite presentation containing \(X\) as a fibrewise dense open and extending its partial group law. Formation of \(K\) commutes with base change.

**Proof.** On each \(S\)-scheme \(R\), consider germs of isomorphisms between fibrewise dense open subschemes of \(X_R\); two representatives agree if they agree on such an open. Finite intersections of dense opens remain dense, and composition and inversion make these germs a group. They form an fppf sheaf: the maximal domains of a germ and its inverse descend along a flat covering, as do their inverse morphisms. The separatedness of \(X\) ensures agreement on common dense domains. Write \(\operatorname{Bir}(X)\) for this sheaf.

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

over a germ \(g\) is the graph \(a=g(b)\) on the intersection of the translated \(X\)-charts. This is an open in \(X_R\), and is fibrewise dense by the preceding construction. Hence \(\delta\) is representable, smooth and surjective. Its equivalence relation is a scheme explicitly: write a related pair as \(((a,b),(c,d))\). The equality \(L_aL_b^{-1}=L_cL_d^{-1}\) says that \(b\) belongs to the translated-chart domain of the universal germ \(L_cL_d^{-1}\), and that \(a=(L_cL_d^{-1})(b)\). Thus the relation is the graph of that evaluation, parametrized by an open subscheme of \(X^3\) with coordinates \((c,d,b)\). The domain is open because representative domains of the universal germ are open and their union is its maximal domain. Both projections are smooth, being base changes of \(\delta\). The bootstrap theorem for flat locally finitely presented equivalence relations represents their quotient by an algebraic space. The sheaf quotient is precisely \(K\), by (8.1). Smoothness follows from (8.2); quasi-compactness follows from its quasi-compact source. Over a Noetherian model the relation, an open in \(X^3\), is quasi-compact; this gives quasi-separatedness and finite presentation. Approximation of these finite-presentation charts gives the assertion over a general base. Moreover each geometric fibre of \(K\) is irreducible, since it is the surjective image of the irreducible \(X\times X\).

For completeness, separation follows from a boundary argument. The diagonal of \(K\) is an immersion: on a product of translation charts it is the graph of their overlap map. Let \(D\) be its image and take its schematic closure in \(K\times_SK\). Its boundary is invariant under simultaneous translation of both coordinates. It has empty intersection with \(X\times_SX\), because \(X/S\) is separated. If a geometric boundary point \((a,b)\) existed, choose a translation carrying both points into \(X\). Such translations form the intersection of two dense opens in an irreducible fibre; one exists. Translation would then put a boundary point in \(X\times X\), a contradiction. The diagonal is therefore closed. This argument is valid on the smooth charts, so also proves separation of the algebraic space.

In each geometric fibre, the open \(X\) and all its translates have dense pairwise intersections. They cover \(K\) by (8.2), so \(X\) is dense and the fibre is irreducible. A second extension acts on \(X\) by the same translation germs and, by (8.2), is generated by them. This gives the unique isomorphism between two extensions. The construction uses sheaves, dense-slice conditions and open immersions, all preserved by base change, proving the final assertion. \(\square\)

Apply this lemma to (7.1). We obtain a smooth separated group algebraic space \(G_{\mathbf Z}\), containing \(X\), with generic fibre the characteristic-zero group already constructed. The torus and root subgroups embed in it and have their prescribed multiplication. Conjugation identities between their morphisms hold over \(\mathbf Z\), because their sources are flat and they hold over \(\mathbf Q\).

## 9. Why the completed integral group is affine and reductive

There are two separate issues: an algebraic space must be shown to be an affine scheme, and its positive-characteristic fibres must be reductive.

First work over an algebraically closed field \(k\). Translates of \(X_k\) by \(k\)-points cover the group algebraic space: every point is \(ab^{-1}\) with \(a,b\in X_k(k)\), by (8.2). These translates are open schemes, so the fibre is itself a smooth separated group scheme.

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

We can already deduce that every geometric fibre is affine. The image of its adjoint homomorphism is a closed reduced subgroup of the affine general linear group. Indeed a constructible subgroup contains an open of its closure; translations make it the full closure. The map onto that image is flat: generic flatness gives a nonempty flat open in the smooth reduced image, and group translations carry it over the whole image. Its kernel is the finite group \(J_k\), and

$$
G_k\times J_k\simeq G_k\times_{\operatorname{Ad}(G_k)}G_k.
$$

It is therefore a finite torsor and is finite onto its affine image. This proves affineness of \(G_k\) without any assumption of its reductivity.

Now let \(N=R_u(G_k)\). A unipotent group meets a torus trivially as a group scheme, by triangularizing its representations and diagonalizing those of the torus. Hence \(\operatorname{Lie}(N)\cap\operatorname{Lie}(T_k)=0\). If \(N\ne1\), its torus-stable Lie algebra contains one of the one-dimensional root lines, say \(kE_\alpha\). Let \(T_\alpha=(\ker\alpha)^0_{\mathrm{red}}\). Its centralizer in \(N\) is smooth, and the positive limit subgroup for \(\alpha^\vee\) in that centralizer is smooth with tangent line \(kE_\alpha\). In \(G_k\) the corresponding limit subgroup is \(U_\alpha\), since the only nonzero weights trivial on \(T_\alpha\) are \(\pm\alpha\). Inclusion and equality of dimension force \(U_\alpha\subset N\). Normality and conjugation by \(n_\alpha\) then give \(U_{-\alpha}\subset N\). Their Gauss relation forces \(\alpha^\vee(\mathbf G_m)\subset N\): for any unit \(d\) take \(u=d-1,v=1\) in (5.1). This is a nontrivial torus, a contradiction. Thus \(N=1\). The centre has character group \(P/Q\), which is finite, so the reductive fibre is semisimple.

To finish, we prove affineness over \(\mathbf Z\), rather than just in its fibres. We need the following small geometric fact, included with its complete openly licensed proof.

**One-dimensional affine-open lemma (Stacks, Tag 09N9).** If \(Y\) is affine and all its local rings are Noetherian of dimension at most one, then every quasi-compact open \(O\subset Y\) is affine.

**Proof, adapted from the Stacks authors.** For the open immersion \(j:O\to Y\), higher direct images \(R^ij_*\mathcal F\), \(i>0\), vanish for every quasi-coherent \(\mathcal F\). This can be checked at stalks by flat localization. On the spectrum of a Noetherian local ring of dimension at most one, an open either contains the closed point and is the whole spectrum, or is a finite discrete set of generic points; in either case it is affine and has no higher quasi-coherent cohomology. Thus the stated higher direct images vanish. The sheaf \(j_*\mathcal F\) is quasi-coherent, since \(j\) is quasi-compact and quasi-separated. Affine vanishing on \(Y\) and the Leray spectral sequence give \(H^i(O,\mathcal F)=0\) for \(i>0\). Serre's affine criterion now gives affineness of \(O\). \(\square\)

**Lemma 9.1.** A quasi-finite separated homomorphism \(f:K\to H\) of finite-type group schemes over a Dedekind base is affine if \(K\) is smooth with geometrically connected fibres of constant dimension.

**Proof in the case needed here.** Affineness can be checked locally on the base and after faithfully flat extension. At a closed point, pass to a complete strictly henselian discrete valuation ring \(R\) with algebraically closed residue field. Replace \(H\) by the schematic closure of the generic image. It is flat over \(R\), the generic map is finite and surjective, and its geometric special-fibre components have dimension \(\dim K_s\), by flatness and the dimension formula over a discrete valuation ring.

Let \(z_i\) be the generic points of those special-fibre components. The local rings \(\mathcal O_{H,z_i}\) have dimension one. The internal Zariski Main Theorem factors the quasi-finite separated base change of \(K\) to each such spectrum as an open in a finite scheme. That finite scheme has dimension at most one; the affine-open lemma shows that the open is affine. Finite-presentation approximation spreads this affineness to a neighborhood of \(z_i\) in \(H\).

Let \(V\subset H\) be the maximal open over which \(f\) is affine. It contains the generic fibre and every \(z_i\). In each special component choose a closed point of \(V\). The map \(K_s\to H_s\) is quasi-finite with full-dimensional image, so its connected image is the whole reduced identity component of \(H_s\): the image is a closed subgroup, and both dimensions are \(\dim K_s\). Translations by this image are transitive on the closed points of each component. Every such translating point lifts to \(K(R)\), since \(K/R\) is smooth and \(R\) is henselian. Translation preserves \(V\). Hence \(V\) contains every closed point of \(H_s\), and therefore all of \(H_s\). Together with the generic fibre this gives \(V=H\). This proves affineness over \(R\), and faithfully flat descent and base localization prove the required assertion. \(\square\)

Apply Lemma 9.1 to (9.3). Its target is affine, so \(G_{\mathbf Z}\) is affine. The torus factor \(T\) of its cell is now a closed subgroup, by the closed-immersion result for multiplicative-type homomorphisms in the first lesson. The zero-weight computation shows it is maximal in every fibre. Equations (9.1), (9.2) and the Gauss formula identify its roots and coroots with the original simply connected datum. Its root lines have the chosen integral frames. We have constructed the pinned split semisimple group over \(\mathbf Z\) for that datum.

## 10. The existence theorem for every reduced datum

**Theorem 10.1.** Every reduced root datum is the datum of a pinned split reductive group over \(\mathbf Z\). For every nonempty scheme \(S\), pinned split groups of a specified constant datum over \(S\) are obtained by base change from this integral group, up to a unique pinning-preserving isomorphism.

**Proof.** Let \(\mathcal R=(X,\Phi,X^*,\Phi^\vee)\), and let \(V=\mathbf Q\Phi\). Decompose

$$
X_{\mathbf Q}=V\oplus C,\qquad
C=\{x:\langle x,\alpha^\vee\rangle=0\text{ for all }\alpha\}.
$$

Let \(\pi\) and \(c\) be the two projections. If \(P\subset V\) is the weight lattice, then \(\pi(X)\subset P\), since all coroot pairings of elements of \(X\) are integral. Set \(L=c(X)\); it is a finite free lattice in \(C\). The map

$$
j:X\longrightarrow P\oplus L,\qquad
x\longmapsto(\pi(x),c(x))
\tag{10.1}
$$

is injective with finite cokernel. It sends every root to \((\alpha,0)\), and its dual sends \((\alpha^\vee,0)\) to the specified coroot in \(X^*\).

The preceding construction gives the simply connected semisimple group \(G_{\mathrm{sc}}\) with torus \(D(P)\). Form \(G_{\mathrm{sc}}\times D(L)\). Inside its torus, the subgroup

$$
H=D(\operatorname{coker}j)
$$

is finite flat and central: every root belongs to \(j(X)\) and restricts trivially to \(H\). The central multiplicative-type quotient theorem proved in *Root data, Weyl chambers and the Bruhat decomposition*, Section 7, constructs

$$
G=(G_{\mathrm{sc}}\times D(L))/H
$$

as a reductive group over \(\mathbf Z\), with torus of character lattice \(j(X)\), the given root characters, and the dual coroots. The root subgroups are unchanged, so their simple frames give a pinning. This realizes \(\mathcal R\). If the root set is empty, the construction is simply \(D(X)\).

Base change preserves the group, datum and pinning. Theorem 5.1 gives the unique pinned isomorphism to any other group of that constant datum over \(S\). \(\square\)

Without a pinning, two globally split groups with isomorphic constant data are still isomorphic: choose their simple-root frames and apply Theorem 5.1. If the type varies on a disconnected base, apply the result to each constant-type part. Such a family need not be the base change of one integral group.

### The derived group

The classification also supplies a construction needed earlier in the course. In the displayed quotient, the image

$$
D=(G_{\mathrm{sc}}\times1)/(H\cap(G_{\mathrm{sc}}\times1))
\tag{10.2}
$$

is a closed normal semisimple subgroup, and \(G/D\) is the torus \(D(L)/\operatorname{pr}_L(H)\). These assertions follow by the already proved central quotient theorem and fppf descent of the closed subgroup in the product.

The group \(G_{\mathrm{sc}}\) is perfect as an fppf sheaf. A homomorphism to a commutative group kills each root group, since

$$
[\alpha^\vee(t),x_\alpha(u)]
=x_\alpha((t^2-1)u)
$$

and fppf locally \(t\) and \(t^2-1\) can be chosen invertible. The Gauss relation then puts the coroot torus in the subgroup generated by the two opposite root groups. The simple coroots form a basis of the simply connected cocharacter lattice, so all of \(T_{\mathrm{sc}}\), and hence the open cell and whole group, are generated by root groups fppf locally. Thus (10.2) is perfect, while its quotient in \(G\) is commutative. It is exactly the derived subgroup.

For an arbitrary reductive group over \(S\), this construction descends from étale local splittings: the characterization as the derived subgroup makes the local constructions unique on overlaps. It is smooth, semisimple, closed, and commutes with every base change. The maximal central torus \(Z\) and \(D\) map to \(G\) by multiplication, with finite central kernel and fppf-surjective image; on the split presentation this follows from the finite-index lattice map (10.1), and then descends. In particular the radical of a reductive group is its maximal central torus.

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

The course prerequisite guide records the exact supporting statements and which lessons are published or still planned.

## References and exact prerequisite proofs

- Michel Demazure, *Schémas en groupes*, SGA 3, Exposé XXI, §§3.5 and 5; Exposé XXIII, §§1–3; Exposé XXV. These are the historical sources for root transport, the rank-two relations and the classification over a base.
- Brian Conrad, [*Reductive group schemes*](https://math.stanford.edu/~conrad/papers/luminysga3.pdf), §§6.2–6.3 and Appendix D. The argument here gives the rank-two calculations and uses a direct matrix construction in characteristic zero.
- Bas Edixhoven and Matthieu Romagny, [*Group schemes out of birational group laws, Néron models*](https://imag.umontpellier.fr/~romagny/articles/artin_birational_law.pdf), §3, for the translation-sheaf construction behind Section 8. The construction and proof are written out here.
- The Stacks authors, *Varieties*, [Tag 09N9](https://stacks.math.columbia.edu/tag/09N9), read in the AI Integrated Stacks Project English source edition, for the one-dimensional affine-open lemma and its proof.
- J. S. Milne, *Algebraic Groups* (2017), Chapter 23, for the field case and the dual datum.

The internal Lie-algebra prerequisites are supporting lessons, with their current published or planned state recorded in the course prerequisite guide: [Root systems and their Weyl groups](https://kokunoyumeto.github.io/open-math-courses-public/courses/RT-LIE/RT-LIE-08.html), the length formula and Coxeter presentation; [The isomorphism theorem and Serre's theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/RT-LIE/RT-LIE-11.html), the split semisimple Lie algebra defined by a finite-type Cartan matrix; [Low-degree cohomology, Whitehead's lemmas and the Levi decomposition](https://kokunoyumeto.github.io/open-math-courses-public/courses/RT-LIE/RT-LIE-06.html), Whitehead's first lemma for a finite-dimensional module in characteristic zero; [Weights, Verma modules and the theorem of the highest weight](https://kokunoyumeto.github.io/open-math-courses-public/courses/RT-LIE/RT-LIE-14.html), existence, finite dimension and uniqueness of \(L(\lambda)\) for dominant integral \(\lambda\); and [Representations of sl(2)](https://kokunoyumeto.github.io/open-math-courses-public/courses/RT-LIE/RT-LIE-05.html), its finite-dimensional weight and exponential formulas. Their uses are confined to the combinatorics and characteristic-zero construction explicitly stated above. The group isomorphism theorem is proved in this lesson.

The geometric prerequisites are likewise exact supporting lessons: The bootstrap theorem, quotient of a flat locally finitely presented equivalence relation by an algebraic space; [Zariski's Main Theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-MO/AG-MO-12.html), the open-into-finite factorization and the normal birational open-immersion consequence; [Limits of schemes and Noetherian approximation](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-MO/AG-MO-03.html), spreading finite-presentation constructions and their affineness; *Cohomology of sheaves on ringed spaces*, the Leray spectral sequence; and *Cohomology of affine schemes and Serre's criterion*, affine vanishing and its converse. The algebraic-space normalization proof used in Section 9 is present in the preceding rank-one lesson. These are supporting results, not substitutes for the integral group construction in Sections 7–10.

## History

This lesson's new exposition, group constructions, calculations, examples and solutions were written by GPT-6.1 Sol (OpenAI), Ultra setting, in October 2026, and are dedicated to the public domain under CC0.

The one-dimensional affine-open lemma and its full proof are adapted from the Stacks authors, *The Stacks Project*, *Varieties*, Tag 09N9, through the AI Integrated Stacks Project English source edition read on 1 October 2026. The Stacks authors retain copyright in that material. The source is the [versioned transparent source](https://github.com/KokunoYumeto/unofficial-stacks-project-ai-drafts/blob/565b10e987aba5969b21145a0833f42d69f96790/varieties.tex). Its proof is included and explained for use in the integral affineness argument.

This collected lesson, *Pinnings and the classification of split reductive groups* (2026), is published by Open Mathematics Courses. The Stacks authors are the authors of its imported proof; GPT-6.1 Sol (OpenAI) is responsible for the new contributions and adaptation. Permission is granted to copy, distribute and modify this collected lesson under the GNU Free Documentation License, Version 1.2, with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. An unaltered copy of the licence is supplied as [GNU Free Documentation License 1.2](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-RG/assets/GFDL-1.2.txt). This additional licence for the collected lesson does not withdraw the CC0 dedication of its original contributions.
