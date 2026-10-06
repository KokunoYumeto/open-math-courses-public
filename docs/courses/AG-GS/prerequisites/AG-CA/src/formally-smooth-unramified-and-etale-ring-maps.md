# Formally smooth, unramified and étale ring maps

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

An infinitesimal thickening preserves points but adds directions in which equations can move. A smooth algebra allows a solution of its equations to extend across every such thickening. An unramified algebra allows at most one extension. An étale algebra allows exactly one. These lifting tests turn the differential calculations of the previous lesson into structural statements about ring maps.

Rings are commutative with identity; no Noetherian hypothesis is implicit. A finite module is finitely generated. We use the [differentials lesson](kahler-differentials.md), especially its universal property, localization formula, conormal sequence and polynomial presentation. Nakayama's lemma is Theorem 4.2 of the [localization lesson](localization-local-properties-and-support.md); finite projective modules over local rings are free by Proposition 2.1 of the [projective-dimension lesson](projective-dimension-and-the-auslander-buchsbaum-formula.md). The field classification will also use already proved polynomial regularity and dimension results, with their locators specified there.

## 1. Extending maps across a square-zero ideal

Fix \(R\to S\). A lifting test consists of an \(R\)-algebra \(A\), an ideal \(J\subset A\) with \(J^2=0\), and an \(R\)-algebra map \(\overline u:S\to A/J\). A **lift** is an \(R\)-algebra map \(u:S\to A\) whose reduction is \(\overline u\). The map \(R\to S\) is

- **formally smooth** if every test has a lift;
- **formally unramified** if every test has at most one lift;
- **formally étale** if every test has exactly one lift.

Thus formal étaleness means formal smoothness together with formal unramifiedness. These definitions test all \(A,J,\overline u\), without finiteness assumptions. [Stacks, Tags 00TI, 00UN, 00UP.]

**Lemma 1.1 (units and thicker ideals).** Units lift across a nilpotent ideal. Each of the three definitions is unchanged if square-zero ideals are replaced by arbitrary nilpotent ideals.

**Proof.** If \(ab=1+j\) and \(j^N=0\), then \(1+j\) has inverse \(\sum_{i=0}^{N-1}(-j)^i\), so \(a\) is a unit. For \(J^N=0\), extend a map successively from \(A/J\) to \(A/J^2,\ldots,A/J^N=A\). The kernel at step \(i\) is \(J^i/J^{i+1}\), whose square is zero since \(2i\geq i+1\). Existence follows step by step. For uniqueness, two lifts agree modulo \(J\); uniqueness in the successive square-zero tests makes them agree modulo every \(J^i\). The converse follows because square-zero ideals are nilpotent. \(\square\)

**Theorem 1.2 (stability).** Each formal property is preserved by composition and arbitrary base change. Polynomial algebras in any set of variables are formally smooth. Every localization \(R\to U^{-1}R\) is formally étale. If \(R\to S\) has any of the three formal properties, so does \(R\to V^{-1}S\).

**Proof.** For \(R\to S\to T\), restrict a test map \(T\to A/J\) to \(S\). In the smooth case, lift that restriction first, regard \(A\) as an \(S\)-algebra through the lift, and then lift \(T\). In the unramified case, two candidate lifts of \(T\) have equal restrictions to \(S\); they are consequently lifts over the same \(S\)-algebra structure on \(A\), and are equal. This proves the étale case too.

For \(R'\) over \(R\), maps \(S\otimes_R R'\to A\) over \(R'\) are precisely maps \(S\to A\) over \(R\) compatible with the fixed \(R'\)-structure. A lift of the restricted map extends uniquely by \(s\otimes r'\mapsto u(s)r'\). Comparing restrictions proves uniqueness. No flatness enters.

For a polynomial algebra, choose a lift in \(A\) of each variable's image and use its universal property. For \(U^{-1}R\), a test means every element of \(U\) maps to a unit modulo \(J\). Lemma 1.1 makes those elements units in \(A\), so the structural map extends uniquely to the localization. For \(V^{-1}S\), first restrict the test to \(S\); any lift sends \(V\) to units and therefore extends uniquely. This proves both existence and uniqueness as applicable. If elements of \(R\) are inverted and already have unit images in \(S\), the same argument proves the formal property over that localized base: an \(R\)-algebra lift is automatically compatible with the forced inverses. \(\square\) [Stacks, Tags 00TJ, 031H, 00TK; Section 00UP.]

Arbitrary localizations need not be finitely presented. Principal localizations are: \(R_f=R[Z]/(fZ-1)\). This distinction will matter when passing from formal properties to smoothness or étaleness.

## 2. Uniqueness is measured by differentials

The ideal \(J\) in a test is an \(S\)-module through \(\overline u\): representatives in \(A\) of an element of \(A/J\) act identically because \(J^2=0\).

**Proposition 2.1.** If \(u,v\) are two lifts, their difference is an \(R\)-derivation \(S\to J\). Conversely, if \(u\) is a lift and \(D:S\to J\) is an \(R\)-derivation, \(u+D\) is a lift. Consequently, once a lift exists, all lifts are parametrized by \(\operatorname{Der}_R(S,J)\).

**Proof.** Put \(D=v-u\). Addition and vanishing on \(R\) are immediate. Expanding the product and dropping \(D(s)D(t)\in J^2\) gives

\[
D(st)=\overline u(s)D(t)+\overline u(t)D(s).
\tag{1}
\]

Conversely this identity makes \(u+D\) multiplicative. Derivations have \(D(1)=0\), so the identity is preserved. Subtraction and addition are inverse operations. \(\square\)

**Theorem 2.2.** A ring map \(R\to S\) is formally unramified if and only if \(\Omega_{S/R}=0\).

**Proof.** If \(\Omega=0\), its representing property makes every derivation into \(J\) zero; Proposition 2.1 gives uniqueness. Conversely use the square-zero algebra \(A=S\oplus\Omega_{S/R}\). Both \(s\mapsto(s,0)\) and \(s\mapsto(s,ds)\) lift the identity of \(S=A/\Omega\). Formal uniqueness makes \(ds=0\) for every \(s\). These elements generate \(\Omega\), so \(\Omega=0\). \(\square\) [Stacks, Tag 00UO.]

Here **unramified** means finite type and \(\Omega_{S/R}=0\). The stronger finiteness convention, finite presentation and \(\Omega=0\), is called **G-unramified** in the Stacks project. We keep these conventions separate. [Stacks, Tag 00UT.]

## 3. Existence is measured by the conormal sequence

Let \(P=R[X_i\mid i\in E]\) for any set \(E\), let \(I\subset P\), and put \(S=P/I\). The conormal sequence from the differentials lesson is

\[
I/I^2\xrightarrow{\delta}\Omega_{P/R}\otimes_P S
\longrightarrow\Omega_{S/R}\longrightarrow0,
\qquad \delta(\overline f)=df\otimes1.
\tag{2}
\]

**Theorem 3.1.** The following conditions are equivalent:

1. \(S\) is formally smooth over \(R\).
2. \(P/I^2\to S\) has an \(R\)-algebra section.
3. Sequence (2), with zero at its left, is split exact.

In particular, a formally smooth algebra has projective differentials. For a finite presentation, both \(\Omega_{S/R}\) and \(I/I^2\) are finite projective.

**Proof.** Formal smoothness lifts \(\operatorname{id}_S\) across the square-zero ideal \(I/I^2\) in \(P/I^2\), giving a section. Conversely, in a test choose lifts of the images of all \(X_i\), giving \(P\to A\). It sends \(I\) into \(J\), hence \(I^2\) to zero. Compose \(P/I^2\to A\) with the proposed section to obtain a lift of \(S\).

A section of \(P/I^2\to S\) splits its conormal sequence by Proposition 3.4 of the differentials lesson. That sequence is (2): after tensoring with \(S\), passing from \(P\) to \(P/I^2\) adds no differential relations, because \(d(ij)=i\,dj+j\,di\) is zero there for \(i,j\in I\).

For the reverse implication, let \(\rho\) be an \(S\)-linear left inverse of \(\delta\). The map

\[
D:P\xrightarrow{d}\Omega_{P/R}\otimes_P S
  \xrightarrow{\rho}I/I^2
\tag{3}
\]

is an \(R\)-derivation, with \(D(i)=i\bmod I^2\) for \(i\in I\). Regard its values as elements of the square-zero ideal in \(P/I^2\). Then

\[
\theta(p)=p\bmod I^2-D(p)
\tag{4}
\]

is an \(R\)-algebra map: the product rule for \(D\) and \(D(p)D(q)=0\) give \(\theta(pq)=\theta(p)\theta(q)\). It kills \(I\), so factors through \(S\), and its reduction to \(S\) is the identity. This constructs the section.

Finally \(\Omega_{P/R}\otimes_P S\) is free on the \(dX_i\), by Theorem 5.1 of the differentials lesson. Split exactness makes both end modules direct summands of it. They are projective. For a finite presentation the middle module has finite rank and \(I/I^2\) is generated by finitely many defining equations, so both end modules are finite. \(\square\) [Stacks, Tags 00TL, 031I, 031J.]

Splitting includes injectivity of \(\delta\). Projective differentials alone do not provide it: over a field of characteristic two, \(k[T]/(T^2)\) has free differentials but fails the lifting test in §8.

## 4. Standard smooth presentations

A map is **smooth** if it is finitely presented and formally smooth, and **étale** if it is finitely presented and formally étale. Thus

\[
\text{étale}\quad\Longleftrightarrow\quad
\text{smooth and }\Omega_{S/R}=0.
\tag{5}
\]

These definitions agree with the Stacks definitions using the naive cotangent complex. Indeed Theorem 7.1 of *Kähler differentials* permits any polynomial presentation. Vanishing of its degree-one homology is exactly injectivity of the conormal map; projectivity of its degree-zero homology \(\Omega_{S/R}\) then splits that injection. Conversely a split conormal sequence has these two properties. Theorem 3.1 identifies split conormal sequences with formal smoothness. For finite presentations, this proves the smooth comparison in both directions. If also \(\Omega=0\), the two-term complex is acyclic, equivalently its conormal differential is an isomorphism, giving exactly the étale definition. [Stacks, Tags 00T2, 00TN, 00U1, 00U2.]

Finite presentations are preserved by composition and base change. Indeed, if \(S=R[X]/(a)\) and \(T=S[Y]/(b)\) use finite lists, choose polynomial representatives in \(R[X,Y]\) for the finitely many coefficients of \(b\). The combined finite list \(a,b\) presents \(T\) over \(R\). Applying a base map to coefficients presents a tensor product. Adjoining one variable with \(hZ-1\) presents a principal localization. Together with Theorem 1.2, this proves stability of smooth and étale maps under composition, base change and principal localization.

A **standard smooth** algebra is

\[
S=R[X_1,\ldots,X_n]/(f_1,\ldots,f_c),\qquad c\leq n,
\tag{6}
\]

such that, after ordering the variables, the determinant

\[
\Delta=\det\left(\frac{\partial f_i}{\partial X_j}\right)_{1\leq i,j\leq c}
\tag{7}
\]

is a unit in \(S\). The empty determinant for \(c=0\) is one. This convention uses a polynomial quotient; localizations will be written in this form by adding a variable. [Stacks, Tag 00T6.]

**Theorem 4.1.** A standard smooth algebra is smooth. Its conormal module is free on the classes of \(f_1,\ldots,f_c\), and its differentials are free on \(dX_{c+1},\ldots,dX_n\). Standard smooth presentations are preserved by arbitrary base change and principal localization.

**Proof.** Choose lifts \(a_j\in A\) of all variable images in a square-zero test. The errors \(f_i(a)\) lie in \(J\). The matrix \(B=(\partial f_i/\partial X_j)(a)\), for \(i,j\leq c\), has unit determinant modulo \(J\), hence has an inverse over \(A\). Define

\[
(\epsilon_1,\ldots,\epsilon_c)^{\mathsf t}
  =-B^{-1}(f_1(a),\ldots,f_c(a))^{\mathsf t},
\qquad \epsilon_j=0\quad(j>c).
\tag{8}
\]

All corrections lie in \(J\). Polynomial expansion, valid in every characteristic, gives
\(f_i(a+\epsilon)=f_i(a)+\sum_j(\partial f_i/\partial X_j)(a)\epsilon_j=0\):
terms involving two corrections vanish. The corrected variables define a lift. Finite presentation is explicit in (6).

The classes of the \(f_i\) generate \(I/I^2\). A linear relation among these classes would, after differentiation and projection to the first \(c\) coordinates, give a relation among the rows of the invertible matrix (7). All coefficients are zero. They are therefore a free basis. In the quotient of the free differential module, the equations \(df_i=0\) uniquely express \(dX_1,\ldots,dX_c\) in terms of the remaining \(dX_j\). Thus those remaining classes form a free basis of \(\Omega\).

Under base change the same equations and determinant have their coefficients mapped to the new base; the determinant remains a unit. For a principal localization, choose \(h\in R[X]\) representing its inverted element. Present it by the original equations and \(hZ-1\). Use pivot variables \(X_1,\ldots,X_c,Z\). Its square minor is

\[
\begin{pmatrix}
B&0\\
Z(\partial h/\partial X_1,\ldots,\partial h/\partial X_c)&h
\end{pmatrix},
\tag{9}
\]

where \(B\) now denotes the polynomial Jacobian block. Its determinant is \(h\Delta\), a unit in the localization. This is a standard smooth presentation with \(c+1\) equations in \(n+1\) variables. \(\square\) [Stacks, Tag 00T7.]

## 5. From a split sequence to local coordinates

**Theorem 5.1 (local standard form).** If \(S\) is smooth over an arbitrary ring \(R\), every \(\mathfrak p\in\operatorname{Spec}S\) has a principal neighborhood \(D(g)\) on which \(S_g\) is standard smooth over \(R\).

**Proof.** Write \(S=P/I\), where \(P=R[X_1,\ldots,X_n]\) and \(I=(a_1,\ldots,a_m)\) is finite. Let \(\mathfrak q\) be the preimage of \(\mathfrak p\). By Theorem 3.1, \(M=I/I^2\) is finite projective. Thus \(M_{\mathfrak p}\) is free of some rank \(c\). Choose \(c\) of the \(a_i\), denoted \(f_1,\ldots,f_c\), whose classes form a basis after passage to \(\kappa(\mathfrak p)\). Nakayama makes their map \(S_{\mathfrak p}^c\to M_{\mathfrak p}\) surjective. In a free basis its square matrix is invertible modulo the maximal ideal, so its determinant is a unit; these classes are a basis over \(S_{\mathfrak p}\).

The conormal injection is split, so remains injective after tensoring with \(\kappa(\mathfrak p)\). The differentials \(df_i\) are therefore independent in \(\kappa(\mathfrak p)^n\). Choose \(c\) variable columns giving a nonzero minor and reorder them first. Its determinant \(\Delta\) lies outside \(\mathfrak q\).

Put \(K=(f_1,\ldots,f_c)\subset P\). The basis assertion implies
\(I_{\mathfrak q}=K_{\mathfrak q}+I_{\mathfrak q}^2\). Apply Nakayama to the finite module

\[
N=I_{\mathfrak q}/K_{\mathfrak q}
\quad\text{over }P_{\mathfrak q}.
\qquad N=I_{\mathfrak q}N,\quad
I_{\mathfrak q}\subset\mathfrak qP_{\mathfrak q}.
\tag{10}
\]

It follows that \(N=0\). This step uses the localized polynomial ring, not a presumed \(S\)-module structure on \(I/K\).

The module \(I/K\) is finite over \(P\). Since its localization at \(\mathfrak q\) vanishes, choose, for each member of a finite generating list, an annihilating denominator outside \(\mathfrak q\); their product \(h\) is outside \(\mathfrak q\) and gives \(I_h=K_h\). Replace \(h\) by \(h\Delta\), preserving that equality and making the Jacobian minor invertible. Its image \(g\in S\) is outside \(\mathfrak p\), and

\[
S_g=P_h/(f_1,\ldots,f_c).
\tag{11}
\]

Adding \(Z\) with equation \(hZ-1\), as in (9), turns (11) into a standard smooth polynomial quotient. This works at every prime. If \(S=0\), its spectrum is empty and the assertion has no points to check. The rank-zero case uses an empty list of \(f_i\) and the same argument. \(\square\) [Stacks, Tag 00TA.]

The theorem explains what the lifting property buys: locally, some variables can be solved to first order in terms of the others. It does not require the equations chosen in an arbitrary initial presentation to be independent everywhere.

## 6. Étale equations and separable fields

A **standard étale** algebra has the form

\[
S=R[T]_g/(f),\qquad
f\in R[T]\text{ monic},\quad f'\text{ a unit in }S.
\tag{12}
\]

Here \(g\in R[T]\). [Stacks, Tag 00UB.]

**Proposition 6.1.** A standard étale algebra is étale.

**Proof.** Choose \(a\in A\) lifting the image of \(T\). Both \(g(a)\) and \(f'(a)\) are units, by Lemma 1.1. The error \(f(a)\) is in \(J\), and

\[
b=a-f'(a)^{-1}f(a),\qquad f(b)=0.
\tag{13}
\]

The equality follows by the square-zero expansion used in (8). Also \(g(b)\) is a unit, so \(b\) defines a lift from (12). For any other lift \(b+\epsilon\), with \(\epsilon\in J\), the equation
\(0=f(b+\epsilon)-f(b)=f'(b)\epsilon\) forces \(\epsilon=0\).
The algebra is finitely presented by adjoining an inverse for \(g\). Thus it is formally étale and finitely presented. \(\square\) [Stacks, Tag 00UC.]

**Lemma 6.2 (idempotents lift uniquely).** Every idempotent of \(A/J\), for \(J^2=0\), has a unique idempotent lift to \(A\).

**Proof.** Choose a lift \(a\), put \(r=a^2-a\in J\), and \(u=2a-1\). Since \(u^2=1+4r\), the element \(u\) is a unit. Then \(e=a-u^{-1}r\) satisfies \(e^2-e=r-u(u^{-1}r)=0\). If \(e,f\) are idempotent lifts of the same element, then \((e+f-1)(e-f)=0\). Modulo \(J\), the first factor has square one, so is a unit; hence \(e=f\). No division by two was used. \(\square\)

**Proposition 6.3.** Every finite separable field extension \(L/k\), and every finite product of such extensions, is étale over \(k\).

**Proof.** Choose a finite generating tower \(k=E_0\subset E_1\subset\cdots\subset E_m=L\), with \(E_i=E_{i-1}(\alpha_i)\). Each \(\alpha_i\) is separable over \(E_{i-1}\): its minimal polynomial divides its separable minimal polynomial over \(k\). Suppose a test map from \(L\) to \(A/J\) is given. Starting with \(k\), lift the tower inductively. With \(E_{i-1}\to A\) already lifted, let \(f_i\) be the monic minimal polynomial of \(\alpha_i\) and choose a lift \(a\) of its image. The image of \(f_i'(\alpha_i)\) is a unit modulo \(J\), because it is nonzero in \(E_i\). Formula (13) produces a unique root lifting \(\alpha_i\), and hence a unique lift of \(E_i=E_{i-1}[T]/(f_i)\). Induction proves formal étaleness.

For \(L_1\times\cdots\times L_r\), lift the images of its coordinate idempotents using Lemma 6.2. Their products for distinct indices are idempotents in \(J\), hence zero. Their sum is an idempotent lifting one, hence one. They decompose
\(A\simeq\prod_i e_iA\), by \(a\mapsto(e_i a)_i\), with inverse summation. The quotient decomposes correspondingly, and each field's lifting test has a unique solution in its component. These solutions combine to the unique lift of the product.

Both a finite extension and a finite product are finite-dimensional over \(k\), hence finite type. The polynomial algebra in a finite generating set is Noetherian by Theorem 2.1 of the [Noetherian lesson](noetherian-and-artinian-rings.md), so its quotient kernel is finite and the algebra is finitely presented. The empty product is the zero ring: a test from it requires \(A/J=0\), which forces \(A=0\) because \(J^2=0\). It too has exactly one lift and has presentation \(k/(1)\). \(\square\)

## 7. Classifying étale algebras over a field

**Lemma 7.1.** For a finite field extension \(L/k\), the condition \(\Omega_{L/k}=0\) is equivalent to separability.

**Proof.** The separable direction follows from Theorem 2.2 and Proposition 6.3. For the converse, choose a finite tower \(E_i=E_{i-1}(\alpha_i)\) as above, without assuming separability. Every coefficient of the monic minimal polynomial \(f_i\in E_{i-1}[T]\) can be expressed as a polynomial over \(k\) in the earlier \(\alpha_j\): the finite algebraic field \(E_{i-1}\) is already \(k[\alpha_1,\ldots,\alpha_{i-1}]\). Choose these expressions to form
\(F_i\in k[X_1,\ldots,X_i]\), monic in \(X_i\). Successive quotienting by \(F_i\) gives precisely \(E_i\), so

\[
L=k[X_1,\ldots,X_m]/(F_1,\ldots,F_m).
\tag{14}
\]

Its differential presentation is the cokernel of a square triangular Jacobian matrix. Its diagonal entries are \(f_i'(\alpha_i)\), because the coefficients use only earlier variables. If \(\Omega=0\), this matrix is surjective over the field \(L\), hence has nonzero determinant. Every \(f_i'(\alpha_i)\) is nonzero, so every tower step is separable.

For completeness, separability of these steps implies separability over \(k\). In an algebraic closure of \(k\), an embedding of \(E_{i-1}\) extends to \(E_i\) by choosing a root of the corresponding minimal polynomial. There are exactly \([E_i:E_{i-1}]\) choices when that polynomial is separable, and at most that many without separability. Multiplication along the separable tower gives \([L:k]\) distinct \(k\)-embeddings of \(L\). If some \(\beta\in L\) had an inseparable minimal polynomial over \(k\), it would have fewer than \([k(\beta):k]\) distinct roots. Restricting embeddings to \(k(\beta)\), and using the same upper bound on extensions, would give fewer than \([k(\beta):k][L:k(\beta)]=[L:k]\) embeddings. This contradiction proves separability. \(\square\)

**Theorem 7.2.** An algebra \(S\) over any field \(k\) is étale if and only if it is a finite product of finite separable field extensions of \(k\).

**Proof.** The product-to-étale direction is Proposition 6.3. For the converse, \(S\) is smooth and has zero differentials by (5). Cover its spectrum by the standard presentations of Theorem 5.1. On any nonzero chart, Theorem 4.1 gives a free differential module of rank \(n-c\). Its vanishing forces \(n=c\).

Consider such a chart \(T=P/(f_1,\ldots,f_n)\), with \(P=k[X_1,\ldots,X_n]\) and invertible full Jacobian. For a prime \(\mathfrak p\) of \(T\), let \(\mathfrak q\subset P\) be its preimage. The classes of the \(df_i\) form a basis of \(\Omega_{P/k}\otimes_P\kappa(\mathfrak q)=\kappa(\mathfrak q)^n\). The natural conormal map from
\(\mathfrak qP_{\mathfrak q}/(\mathfrak qP_{\mathfrak q})^2\) to this vector space is therefore surjective.

Proposition 3.3 and Theorem 3.2 of the [regular-local lesson](regular-local-rings.md) say that \(P_{\mathfrak q}\) is regular. Its cotangent dimension is its dimension, namely \(\operatorname{ht}\mathfrak q\), which is at most \(n\) by Theorem 4.2 of the [dimension lesson](krull-dimension-and-noether-normalization.md). Surjectivity onto an \(n\)-dimensional space forces equality. The \(f_i\) are thus a basis of this cotangent space. Nakayama, applied to the finite module \(\mathfrak qP_{\mathfrak q}/(f_1,\ldots,f_n)P_{\mathfrak q}\), gives

\[
(f_1,\ldots,f_n)P_{\mathfrak q}=\mathfrak qP_{\mathfrak q},
\qquad T_{\mathfrak p}=\kappa(\mathfrak q).
\tag{15}
\]

The height formula in that dimension theorem gives
\(\operatorname{trdeg}_k\kappa(\mathfrak q)=n-\operatorname{ht}\mathfrak q=0\).
This residue field is generated as a field by the finitely many images of the \(X_i\), so is a finite algebraic extension. Localization of differentials makes its differential module zero, and Lemma 7.1 makes the extension separable. The argument includes \(n=0\).

Consequently every \(S_{\mathfrak p}\) is a field. The algebra \(S\) is Noetherian, since it is finite type over \(k\). It is reduced: a nilpotent element vanishes in every local field, and Theorem 5.1 of the localization lesson detects its vanishing. Every prime is maximal: a strict inclusion \(\mathfrak p\subsetneq\mathfrak m\) would produce distinct primes in the field \(S_{\mathfrak m}\), contrary to the localization correspondence. By Theorem 4.2 of the Noetherian lesson, \(S\) is Artinian and a finite product of its local rings. These local rings are fields; their extensions of \(k\) are finite separable by the local calculation just made. The zero algebra is the empty product. \(\square\) [Stacks, Tag 00U3.]

A finite type ring map is **quasi-finite** when every residue-field fibre has finitely many primes, all maximal. This is the algebraic condition of having finitely many points in each fibre.

**Corollary 7.3.** Every étale ring map is quasi-finite. In fact each fibre is a finite product of finite separable extensions of its residue field.

**Proof.** For \(\mathfrak p\subset R\), base change makes \(S\otimes_R\kappa(\mathfrak p)\) étale over \(\kappa(\mathfrak p)\). Theorem 7.2 gives the asserted product. Such a product has finitely many primes, one for each field factor, and all are maximal. Étale maps are finitely presented, hence finite type. \(\square\) [Stacks, Tag 00U5.]

**Proposition 7.4 (maps between étale algebras).** Every \(R\)-algebra map \(S\to T\) between étale \(R\)-algebras is étale.

**Proof.** Choose a finite presentation \(T=R[Y_1,\ldots,Y_n]/(b_1,\ldots,b_r)\) and finite algebra generators \(x_1,\ldots,x_m\) of \(S\). Represent the images of the \(x_i\)'s by polynomials \(p_i(Y)\). Then
\[
T=S[Y]/(b_1,\ldots,b_r,x_1-p_1(Y),\ldots,x_m-p_m(Y)),
\]
where the \(b_j\)'s are read through the base map. To verify this presentation, impose \(x_i=p_i(Y)\); every relation of \(S\) becomes a polynomial already zero in \(R[Y]/(b)\), by the given map to \(T\). Thus it is indeed \(T\) and is finitely presented over \(S\).

In a square-zero lifting test over \(S\), first lift the map from \(T\) as an \(R\)-map by formal étaleness of \(T/R\). Its restriction to \(S\) and the specified structure map \(S\to A\) have identical reductions, so formal unramifiedness of \(S/R\) makes them equal. The lift is therefore an \(S\)-map. Uniqueness holds because it already holds for \(R\)-maps from \(T\). This proves formal étaleness and, with the presentation, étaleness. \(\square\)

**Lemma 7.5 (finite flat quotients).** If \(A\to A/I\) is flat and finitely presented, then \(I=(e)\) for an idempotent \(e\), and \(A/I=A_{1-e}\).

**Proof.** The ideal \(I\) is finitely generated by finite presentation. Tensoring \(I\hookrightarrow A\) with the flat quotient gives an injection \(I/I^2\to A/I\); the map is zero, so \(I=I^2\). Express a finite generating column \(x\) of \(I\) as \(x=Mx\) with entries of \(M\) in \(I\). The adjugate identity gives \(\det(1-M)I=0\). Write this determinant as \(1-e\), with \(e\in I\). Then \((1-e)e=0\), so \(e^2=e\), and \(a=ea\) for every \(a\in I\), giving \(I=eA\). Killing \(e\) is exactly inverting the complementary idempotent. \(\square\)

**Theorem 7.6 (principal standard étale neighborhoods).** If \(R\to S\) is étale and \(\mathfrak q\subset S\) is prime, some \(S_g\), \(g\notin\mathfrak q\), is standard étale over \(R\). The single monic equation in (12) thus describes every étale map near a chosen point.

The complete required proof is Theorem 3.1 of [*Étale morphisms and their local structure*](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-FSE/etale-morphisms-and-their-local-structure.html), in the programme's course *Flat, smooth and étale morphisms*. Its finite-fibre, primitive-element, Nakayama and monic-polynomial steps are written there. Proposition 7.4 and Lemma 7.5 above supply the final étale quotient argument; flatness of étale algebras is proved in the following smoothness lesson before this continuation is used in *Henselian local rings and henselization*.

That proof's algebraic Zariski step is supplied by *Morphisms of schemes*, [Zariski's Main Theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/AG-MO/AG-MO-12.html#section-1), Theorem 1.1, proved in Sections 1–2. For any finite-type ring map \(R\to S\), if \(\mathfrak q\) is isolated in its residue-field fibre, the integral closure \(S'\) of \(R\) in \(S\) contains \(g\notin\mathfrak q\) with \(S'_g=S_g\). There are no Noetherian or field assumptions. The proof uses conductor and strong-transcendence lemmas with exact complete open proof providers. Both the local-standard-form proof and this algebraic Zariski proof are written and published. This identifies the required written argument; it does not certify every recursively used foundation.

## 8. Examples and exercises

**A curve with a free direction.** The algebra \(k[X,Y]/(XY-1)\) is standard smooth: use \(X\) as pivot, since \(\partial(XY-1)/\partial X=Y\) is a unit. Its differentials are free on \(dY\), with \(dX=-XY^{-1}dY\). This is the punctured line written with an explicit inverse variable. It is smooth of relative differential rank one, rather than étale.

**A branch point.** Let \(R=k[X]\) and \(S=R[Y]/(Y^2-X)=k[Y]\), with \(\operatorname{char}k\ne2\). After inverting \(X\), equivalently \(Y\), the monic equation has unit derivative \(2Y\), so the map is étale over \(D(X)\). Before localization,

\[
\Omega_{S/R}=S/(2Y)\,dY.
\tag{16}
\]

At the origin its fibre is one-dimensional, so the map is not unramified there. The fibre equation \(Y^2=0\) records multiplicity two at the branch point. In characteristic two the derivative vanishes everywhere and \(\Omega_{S/R}=S\,dY\).

**A finiteness warning.** Formal smoothness alone need not imply flatness. Solution 8.6 constructs even a formally étale, nonflat map over every field. Smoothness includes finite presentation; its flatness in the Noetherian setting will be proved in *Smooth algebras over a field and the Jacobian criterion*. [Stacks, Section 057V.]

**Exercise 8.1 (easy).** Prove directly that \(\mathbb Z\to\mathbb Z[1/n]\) is formally étale, for every integer \(n\), including \(n=0\).

**Exercise 8.2 (easy).** Let \(k\) be any field. Test formal smoothness of \(k[T]/(T^2)\) using \(A=k[T]/(T^3)\), \(J=(T^2)\), and the identity map to \(A/J\).

**Exercise 8.3 (medium).** Determine where \(\mathbb Z\to\mathbb Z[i]\) is unramified, both at primes of \(\mathbb Z[i]\) and after localization at primes \((p)\) of \(\mathbb Z\). Show that away from two it is étale.

**Exercise 8.4 (medium).** Given a finite separable extension \(L/k\) and a square-zero test, construct the unique lift of \(L\) by a finite generating tower, without using a primitive element theorem.

**Exercise 8.5 (hard).** In a finite presentation \(S=P/I\) of a smooth algebra, choose \(f_1,\ldots,f_c\in I\) whose classes form a basis of \((I/I^2)_{\mathfrak p}\). Prove carefully that they generate \(I\) after inverting one element outside the preimage of \(\mathfrak p\). Complete the standard smooth presentation, including the extra variable needed for that inversion.

**Exercise 8.6 (hard).** Over a field \(k\), form the directed system

\[
k[t_0]\longrightarrow k[t_1]\longrightarrow k[t_2]\longrightarrow\cdots,
\qquad t_n\longmapsto t_{n+1}^2.
\tag{17}
\]

Let \(R\) be its colimit and \(I=(t_0,t_1,\ldots)\). Prove that \(R\) is a domain, \(R/I=k\), \(I\ne0\), and \(I=I^2\). Prove that \(R\to k\) is formally étale but nonflat and is not finitely presented.

## 9. Complete solutions

**Solution 8.1.** A test map requires the image of \(n\) in \(A/J\) to be a unit. Lemma 1.1 makes its image in \(A\) a unit. The unique homomorphism \(\mathbb Z\to A\) therefore extends uniquely by sending \(1/n\) to its inverse. It reduces to the prescribed map, since the inverse is forced in the quotient too. If \(n=0\), the test requires \(A/J=0\); then \(1\in J\) and \(J^2=0\) force \(A=0\). The unique map from \(\mathbb Z[1/0]=0\) is the unique lift.

**Solution 8.2.** Any lift of the residue class of \(T\) must send it to \(T+aT^2\), with \(a\in k\). Its square in \(A\) is \(T^2\), since all terms of degree at least three vanish. This is nonzero, contradicting the defining relation \(T^2=0\) in the source. Thus the identity has no lift and the algebra is not formally smooth. The computation works in every characteristic. In characteristic two its differentials are nevertheless free, which illustrates the need for conormal injectivity in Theorem 3.1.

**Solution 8.3.** Write \(B=\mathbb Z[i]=\mathbb Z[T]/(T^2+1)\). The differential presentation gives

\[
\Omega_{B/\mathbb Z}=B/(2i)\,di=B/(2)\,di,
\tag{18}
\]

because \(i\) is a unit. This vanishes on a localization precisely where two becomes invertible. Indeed, the support of the cyclic module \(B/(2)\) is \(V(2)\), by Proposition 6.1 of the localization lesson. The quotient is
\(\mathbb F_2[T]/((T+1)^2)\), whose unique prime gives the prime \((1+i)\) in \(B\). Thus this is exactly the target prime where the map is ramified.

For a prime \((p)\subset\mathbb Z\), with \(p\) prime, the algebra \(B\otimes_{\mathbb Z}\mathbb Z_{(p)}\) is unramified if \(p\ne2\), since (18) becomes zero. For \(p=2\) its quotient by two is the nonzero ring just displayed, so the differential module is nonzero. At the generic prime \((0)\) it vanishes as well. The algebra is finitely presented, so these are the stated unramified tests. Away from two, \(T^2+1\) is monic and its derivative \(2i\) is a unit; Proposition 6.1 makes the map étale there.

**Solution 8.4.** Write \(L=k(\alpha_1,\ldots,\alpha_m)\) and \(E_j=k(\alpha_1,\ldots,\alpha_j)\). With \(E_{j-1}\) already lifted, map the coefficients of the minimal polynomial \(f_j\) into \(A\). Its root in \(A/J\) has nonzero derivative in the image of \(E_j\), hence unit derivative. Choose any representative \(a\) of that root, and replace it by \(b=a-f_j'(a)^{-1}f_j(a)\). Since \(f_j(a)\in J\), square-zero expansion proves \(f_j(b)=0\). The quotient description \(E_j=E_{j-1}[T]/(f_j)\) gives the extension of the lift. If two extensions send \(\alpha_j\) to \(b,b+\epsilon\), their difference satisfies \(f_j'(b)\epsilon=0\), hence is zero. Starting at the fixed \(k\)-map proves existence and uniqueness at every stage. Each minimal polynomial is separable because it divides the separable polynomial of \(\alpha_j\) over \(k\). This proves formal étaleness.

**Solution 8.5.** Let \(\mathfrak q\subset P\) be the preimage of \(\mathfrak p\), and set \(K=(f_1,\ldots,f_c)\). Localizing the given basis assertion gives
\(I_{\mathfrak q}=K_{\mathfrak q}+I_{\mathfrak q}^2\).
The module \(N=I_{\mathfrak q}/K_{\mathfrak q}\) is finite over \(P_{\mathfrak q}\), since \(I\) is generated by a finite list. Moreover
\(I_{\mathfrak q}N=(I_{\mathfrak q}^2+K_{\mathfrak q})/K_{\mathfrak q}=N\).
As \(I_{\mathfrak q}\) is contained in the maximal ideal, Nakayama gives \(N=0\).

Choose finite generators \(a_j\) of \(I\). Each class of \(a_j\) in \(I/K\) becomes zero at \(\mathfrak q\), so some \(h_j\notin\mathfrak q\) kills it. Their product \(h\) gives \(I_h=K_h\). The split conormal injection stays injective on the residue field, so the \(df_i\) are independent there. Some \(c\)-column Jacobian minor \(\Delta\) is outside \(\mathfrak q\); after reordering variables, replace \(h\) by \(h\Delta\). Its image \(g\) in \(S\) is outside \(\mathfrak p\), and \(S_g=P_h/K_h\).

Present this algebra as
\(R[X_1,\ldots,X_n,Z]/(f_1,\ldots,f_c,hZ-1)\).
The Jacobian minor using \(X_1,\ldots,X_c,Z\) has determinant \(h\Delta\), by (9), and is a unit. It is standard smooth. The finite generation used for clearing denominators was over \(P\); no Noetherianity of \(P\) or \(R\) was required.

**Solution 8.6.** Each transition in (17) is injective: substituting \(t_{n+1}^2\) in a nonzero polynomial produces distinct monomial exponents and remains nonzero. Thus the colimit is a union of domains and is a domain. The compatible evaluations \(t_n\mapsto0\) give \(R\to k\). Every element comes from a polynomial at some stage; subtracting its constant term gives a multiple of \(t_n\). Its kernel is therefore \(I\), and \(R/I=k\). The element \(t_0\) remains nonzero. Also \(t_n=t_{n+1}^2\in I^2\) for every \(n\), so \(I=I^2\).

For a test of \(R\to R/I\), the structural map \(R\to A\) sends \(I\) into \(J\). But its image of \(I=I^2\) lies in \(J^2=0\). It factors uniquely through \(R/I\), and its reduction is the prescribed map, since a map from this quotient is determined by the structural map from \(R\). This proves formal étaleness.

Multiplication by \(t_0\) is injective on the domain \(R\). Tensoring this injection with \(k=R/I\) gives the zero map \(k\to k\), which is not injective. Hence \(k\) is not flat over \(R\).

The ideal \(I\) is maximal since \(R/I=k\). If \(I\) were finite, its localization \(I_I\) would be a finite module over the local ring \(R_I\), with \(I_I=I_I^2\). Nakayama would give \(I_I=0\), whereas the nonzero element \(t_0\) stays nonzero under localization in a domain. Thus \(I\) is not finite. Finally a quotient \(R/I\) that is finitely presented as an \(R\)-algebra has finite kernel: write it as \(R[X_1,\ldots,X_m]/(b_1,\ldots,b_r)\), and choose \(a_i\in R\) representing the images of \(X_i\). Every element \(s\in I\), viewed as a constant polynomial, belongs to \((b_1,\ldots,b_r)\). Evaluating its polynomial expression at the \(a_i\) shows \(s\in(b_1(a),\ldots,b_r(a))\), and each \(b_j(a)\) is in \(I\). These finitely many elements generate \(I\). The contradiction shows that our map is not finitely presented.

## References and proof scope

The Stacks project supplies the lifting, conormal and standard-presentation framework at the tags cited above. Ravi Vakil, [*The Rising Sea: Foundations of Algebraic Geometry*](https://math.stanford.edu/~vakil/216blog/FOAGjul2724public.pdf), public draft of 27 July 2024, §§13.6 and 21.7, supplies geometric interpretations and the unramified viewpoint. Timothy J. Ford, [*Commutative Algebra*](https://tim4datfau.github.io/Timothy-Ford-at-FAU/preprints/CA.pdf), version of 23 September 2026, Chapter 8, Sections 5–6, and Chapter 10, Sections 1–2, discusses separable algebras, including their classification over a field, algebras presented by a single monic polynomial, lifting across square-zero ideals, and the vanishing of differentials that characterizes separability for finitely generated algebras.

Verified tag references: [Tag 00TI](https://stacks.math.columbia.edu/algebra.html#definition-formally-smooth), [Tag 00TJ](https://stacks.math.columbia.edu/algebra.html#lemma-base-change-fs), [Tag 031H](https://stacks.math.columbia.edu/algebra.html#lemma-compose-formally-smooth), [Tag 00TK](https://stacks.math.columbia.edu/algebra.html#lemma-polynomial-ring-formally-smooth), [Tag 00TL](https://stacks.math.columbia.edu/algebra.html#lemma-characterize-formally-smooth), [Tag 031I](https://stacks.math.columbia.edu/algebra.html#lemma-characterize-formally-smooth-again), [Tag 031J](https://stacks.math.columbia.edu/algebra.html#proposition-characterize-formally-smooth), [Tag 00UN](https://stacks.math.columbia.edu/algebra.html#definition-formally-unramified), [Tag 00UO](https://stacks.math.columbia.edu/algebra.html#lemma-characterize-formally-unramified), [Tag 00T2](https://stacks.math.columbia.edu/algebra.html#definition-smooth), [Tag 00T6](https://stacks.math.columbia.edu/algebra.html#definition-standard-smooth), [Tag 00T7](https://stacks.math.columbia.edu/algebra.html#lemma-standard-smooth), [Tag 00TN](https://stacks.math.columbia.edu/algebra.html#proposition-smooth-formally-smooth), [Tag 00TA](https://stacks.math.columbia.edu/algebra.html#lemma-smooth-syntomic), [Tag 00UT](https://stacks.math.columbia.edu/algebra.html#definition-unramified), [Tag 00U1](https://stacks.math.columbia.edu/algebra.html#definition-etale), [Tag 00U2](https://stacks.math.columbia.edu/algebra.html#lemma-etale), [Tag 00U3](https://stacks.math.columbia.edu/algebra.html#lemma-etale-over-field), [Tag 00UB](https://stacks.math.columbia.edu/algebra.html#definition-standard-etale), [Tag 00UC](https://stacks.math.columbia.edu/algebra.html#lemma-standard-etale), [Tag 00U5](https://stacks.math.columbia.edu/algebra.html#lemma-etale-quasi-finite), [Tag 00U7](https://stacks.math.columbia.edu/algebra.html#lemma-map-between-etale), [Tag 00UE](https://stacks.math.columbia.edu/algebra.html#proposition-etale-locally-standard), [Tag 00UP](https://stacks.math.columbia.edu/algebra.html#section-formally-etale), [Tag 00US](https://stacks.math.columbia.edu/algebra.html#section-unramified), [Tag 057V](https://stacks.math.columbia.edu/examples.html#section-formally-smooth-nonflat).

**Proof dependencies.** Section 4 proves the naive-complex comparison, and Proposition 7.4 proves étaleness of maps between étale algebras. Theorem 7.6 identifies its written internal proof in *Flat, smooth and étale morphisms*, and links the written algebraic Zariski proof in *Morphisms of schemes*, Theorem 1.1, Sections 1–2, above. All lifting criteria, standard smooth presentations, field classifications and exercises are proved here using the named earlier results. Flatness and geometric regularity of smooth algebras follow in the next lesson.
