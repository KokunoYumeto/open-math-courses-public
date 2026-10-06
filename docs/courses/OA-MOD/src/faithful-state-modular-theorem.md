# Modular time from a faithful normal state

*Original AI-authored pedagogical exposition by the OA-MOD course project; CC0-1.0. The proofs use the precise earlier results stated below.*

A state gives a particularly concrete entrance to modular theory. Every bounded algebra element has a GNS vector, and the unit supplies a cyclic separating vector. The difficult point is to show that the unitaries obtained from a closed involution preserve the represented algebra. We prove that assertion by constructing resolvent vectors, converting their defining equation into bounded pairings, and recovering pointwise commutation from an integral identity.

The theorem applies to **every von Neumann algebra admitting a faithful normal state**. Neither a factor hypothesis, injectivity, a type classification, separable predual nor a separable GNS Hilbert space is required. It supplements the course's general faithful normal semifinite weight construction. It does not replace any MF, WH or SF argument, or reduce the full B1–B9 programme to states.

## The theorem, conventions and precise inputs

Inner products are linear in the first variable. A normal state means a positive ultraweakly continuous functional \(\varphi\) with \(\varphi(1)=1\). Faithfulness means \(\varphi(a)=0\), \(a\geq0\), implies \(a=0\). The predual and ultraweak topology are the projective-tensor construction of CP, not a trace-class identification. All Hilbert spaces below may have arbitrary dimension.

**Faithful-state Tomita theorem.** Let \(M\) be a von Neumann algebra and \(\varphi\) a faithful normal state. Its GNS representation \(\pi_\varphi\) is faithful, normal, and an ultraweak homeomorphism onto a weak operator closed unital *-algebra. Identify \(M\) with that algebra, and denote the GNS vector by \(\Omega\). The densely defined conjugate-linear map

\[
S_0(a\Omega)=a^*\Omega,\qquad a\in M,
\]

is closable. Its closure has polar decomposition \(S=J\Delta^{1/2}\), where \(J\) is an antiunitary involution and \(\Delta\) is positive self-adjoint and injective. With equality of the stated operator domains,

\[
\begin{gathered}
S^*=J\Delta^{-1/2}=\Delta^{1/2}J,\qquad
J\Delta J=\Delta^{-1},\qquad
J\Delta^zJ=\Delta^{-\overline z},\\
J\Omega=\Omega,\qquad \Delta^z\Omega=\Omega,\qquad z\in\mathbb C.
\end{gathered}
\tag{FS.1}
\]

Moreover,

\[
JMJ=M',\qquad \Delta^{it}M\Delta^{-it}=M\quad(t\in\mathbb R).
\tag{FS.2}
\]

The maps \(\sigma_t^\varphi(a)=\Delta^{it}a\Delta^{-it}\) form a point-strong* continuous group of normal automorphisms, and

\[
\varphi\circ\sigma_t^\varphi=\varphi,
\qquad \sigma_t^\varphi(a)\Omega=\Delta^{it}a\Omega.
\tag{FS.3}
\]

Finally, \(S^*\) is the closure of \(b\Omega\mapsto b^*\Omega\) for \(b\in M'\).

The exact earlier inputs are as follows.

| Earlier proof | Exact use here |
|---|---|
| **CP-02–06**, `public/src/concrete-preduals.md` | \(E_H=H\widehat\otimes_\pi\overline H\), \(E_H^*=B(H)\), summable coefficient series, \(M=(M_*)^*\), and norm closedness of \(M_*\subset M^*\). |
| **CP-07**, same file | Positive-functional Cauchy–Schwarz, ultraweak continuity of adjoints and fixed multiplication, closedness of self-adjoint balls. |
| **CP-01**, norm-preserving Hahn–Banach; **OA-MOD-OPEN-CONVEX-SEPARATION** | Norm separation in the preadjoint quotient argument. The latter's earlier full programme proof is HB §6, linked below. The resolvent separation is also reduced below to finite-dimensional Euclidean separation. |
| **AB-04 and the Banach–Alaoglu part of AB-05**, `public/src/banach-second-adjoint.md` | Compactness of the dual unit ball for pointwise convergence on the predual. No weak sequential compactness theorem is needed. |
| **TC-03**, `public/src/tomita-closability.md` | The conjugate-linear adjoint and its graph-closure theorem. FS-03 includes the state specialization. |
| **QF-03**, `public/src/closed-positive-forms.md` | The full representation and uniqueness theorem for a densely defined closed nonnegative form, including its exact square-root domain. |
| **TC-07–10**, `public/src/tomita-closability.md` | The complete form-based closed-involution argument. FS-04 gives the construction and inverse-domain calculation explicitly. |
| **SK-04–09**, `public/src/spectral-calculus-kernel.md` | Spectral integral domains, multiplication, inverse ranges, antiunitary transport, finite spectral approximation, graph cutoffs and strong continuity of imaginary powers. |
| **MA-02–04**, `public/src/modular-analytic-kernel.md` | Vectorwise strong integration and Fourier uniqueness for continuous integrable scalar functions, proved through Gaussian approximation. |
| **MA-05**, same file, and **OA-MOD-ANALYTIC-BRIDGE-SIMPLE-RESIDUE** | The scalar rectangle/residue calculation already justified there. FS-07 calculates the particular complex-parameter kernel required here. |

For the Hahn–Banach inputs, see the complete earlier programme [norm-preserving extension, HB §2](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html#oa-fnd-hb-02) and [locally convex separation, HB §6](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces.html#oa-fnd-hb-06). The course's `public/course.json` binds these exact contracts. Scalar dominated convergence, absolutely integrable Fubini and the rectangle/simple-residue input retain the existing MA and SK foundation bindings. No general modular fundamental theorem, standard-form theorem, weight-GNS normality theorem or trace-class duality is an input.

## Constructing the GNS von Neumann algebra

On the vector space \(M\), put

\[
\langle a\Omega,b\Omega\rangle=\varphi(b^*a).
\tag{FS.4}
\]

Positivity and Cauchy–Schwarz follow from CP-07. Faithfulness makes this an inner product. Complete it to a Hilbert space \(H\). The inequality

\[
\varphi(a^*x^*xa)\leq\|x\|^2\varphi(a^*a)
\]

extends left multiplication to a bounded operator \(\pi(x)\). Products and adjoints agree on the dense subspace \(M\Omega\), so \(\pi\) is a unital *-representation. Since \(\pi(x)\Omega=x\Omega\), it is injective.

We will need its norm, not just injectivity. If \(a\geq0\) and \(0<c<\|a\|\), the spectral projection \(p=1_{(c,\infty)}(a)\) is nonzero. Faithfulness gives \(\|p\Omega\|^2=\varphi(p)>0\), and

\[
\|\pi(a)p\Omega\|^2=\varphi(pa^2p)
\geq c^2\varphi(p).
\]

Thus \(\|\pi(a)\|\geq c\). Letting \(c\uparrow\|a\|\), and using the opposite contractive bound, gives equality. Applying this to \(x^*x\) proves \(\|\pi(x)\|=\|x\|\) for every \(x\).

For \(a,b\in M\), the coefficient

\[
x\longmapsto\langle\pi(x)a\Omega,b\Omega\rangle
=\varphi(b^*xa)
\]

belongs to \(M_*\), by ultraweak continuity of fixed multiplication. Approximate arbitrary \(\xi,\eta\in H\) by such vectors. The coefficient norm estimate

\[
\|\omega_{\xi,\eta}-\omega_{\xi_0,\eta_0}\|
\leq\|\xi-\xi_0\|\|\eta\|+\|\xi_0\|\|\eta-\eta_0\|
\]

and CP-06 show that every coefficient of \(\pi\) lies in the norm-closed space \(M_*\).

Consequently the bilinear prescription

\[
\Theta(\xi\otimes\overline\eta)(x)
=\langle\pi(x)\xi,\eta\rangle
\]

extends to a contraction \(\Theta:E_H\to M_*\), and \(\Theta^*=\pi\) under the dualities supplied by CP. This also proves normality: pulling back any ultraweak coefficient series on \(B(H)\) gives \(\Theta u\in M_*\).

**Why the preadjoint is onto.** Let \(C\) be the norm closure of \(\Theta(B_{E_H})\). If \(f\in B_{M_*}\) lay outside \(C\), Hahn–Banach separation would give \(a\in(M_*)^*=M\) such that

\[
\operatorname{Re}f(a)>
\sup_{u\in B_{E_H}}\operatorname{Re}\Theta(u)(a)
=\|\Theta^*a\|=\|a\|.
\]

This contradicts \(\|f\|\leq1\). Hence \(B_{M_*}\subset C\). For an arbitrary residual \(r\ne0\), choose \(u\) with
\(\|u\|\leq\|r\|\) and \(\|r-\Theta u\|\leq\|r\|/2\). Starting with \(r=f\) and repeating, the chosen vectors form an absolutely summable series of norm at most \(2\|f\|\), whose sum maps exactly to \(f\). A zero residual ends the construction. Thus every \(f\) has a lift of norm at most \(2\|f\|\).

If \(T\in E_H^*=B(H)\) annihilates \(\ker\Theta\), define \(g(\Theta u)=T(u)\). It is well-defined and the lift estimate gives \(|g(f)|\leq2\|T\|\|f\|\). CP duality therefore gives \(g(f)=f(a)\) for some \(a\in M\), and \(T=\Theta^*a=\pi(a)\). We have proved

\[
\pi(M)=(\ker\Theta)^\perp.
\tag{FS.5}
\]

The right side is ultraweakly closed. Surjectivity of \(\Theta\) also proves that \(\pi^{-1}\) is ultraweakly continuous on its image: each original predual functional is the restriction of some \(u\in E_H\).

**Why ultraweak closure gives the required weak operator closure.** We give the coefficient argument so no assertion about boundedness of arbitrary approximating nets is hidden. Let \(A\subset B(H)\) be any unital *-algebra and \(T\in A''\). By CP-04 an ultraweak functional annihilating \(A\) has the form

\[
f(a)=\sum_n\langle a\xi_n,\eta_n\rangle,
\qquad (\xi_n),(\eta_n)\in\ell^2(H).
\]

In \(\ell^2(H)\), write \(D(a)\) for diagonal multiplication by \(a\), and let \(p\) project onto \(K=\overline{\{D(a)\xi:a\in A\}}\). The space \(K\) reduces \(D(A)\). Thus the matrix entries \(p_{ij}:H\to H\) commute with \(A\), so they belong to \(A'\). They commute with \(T\), whence \(pD(T)=D(T)p\), first on finite coordinate vectors and then by density. As \(1\in A\), \(p\xi=\xi\). Since \(f|_A=0\), the vector \(\eta\) is perpendicular to \(K\). It follows that

\[
f(T)=\langle D(T)\xi,\eta\rangle=0.
\]

The elementary annihilator argument of CP-05 now shows \(T\in\overline A^{\mathrm{uw}}\). Conversely \(A''\) is WOT closed, hence ultraweakly closed, because its defining commutation equations are coefficient-continuous. Thus \(\overline A^{\mathrm{uw}}=A''\). Apply this to \(A=\pi(M)\) and (FS.5). Its image is WOT closed, as required. We now identify \(M\) with this image.

The vector \(\Omega\) is cyclic by construction and separating by faithfulness. It is cyclic for \(M'\) as well. Indeed, the projection \(e\) onto \(\overline{M'\Omega}\) commutes with \(M'\), hence belongs to \(M\). Since \(e\Omega=\Omega\), separation gives \(e=1\). Cyclicity for \(M\) also makes \(\Omega\) separating for \(M'\): an operator in \(M'\) killing \(\Omega\) kills dense \(M\Omega\).

Countable series occurred only in the representation of one functional. They did not supply or require a countable dense subset of \(H\).

## Closing the involution

Define

\[
S_0(a\Omega)=a^*\Omega\quad(a\in M),\qquad
F_0(b\Omega)=b^*\Omega\quad(b\in M').
\]

Both domains are dense, and both maps are well-defined conjugate-linear involutions. Our adjoint convention, including its reversal of entries, is

\[
\langle A\xi,\eta\rangle=\langle A^*\eta,\xi\rangle
\quad\text{for conjugate-linear }A.
\tag{FS.6}
\]

Commutation of \(a\) and \(b\) gives

\[
\langle S_0(a\Omega),b\Omega\rangle
=\langle a^*\Omega,b\Omega\rangle
=\langle b^*\Omega,a\Omega\rangle.
\tag{FS.7}
\]

Hence \(F_0\subset S_0^*\), and the symmetric calculation gives \(S_0\subset F_0^*\). In particular, if \(a_n\Omega\to0\) and \(a_n^*\Omega\to\eta\), (FS.7) makes \(\eta\) perpendicular to \(M'\Omega\), so \(\eta=0\). This is closability directly. TC-03 supplies the identical adjoint/graph conclusion.

Put \(S=\overline{S_0}\) and \(F=S^*\). If \(\xi\in D(S)\), choose \(a_n\Omega\to\xi\), \(a_n^*\Omega\to S\xi\). Reversing these two convergences and using closedness proves \(S\xi\in D(S)\), \(S(S\xi)=\xi\). Thus

\[
S^{-1}=S,
\qquad \operatorname{ran}S=D(S).
\tag{FS.8}
\]

The space \(M\Omega\) is a graph core by definition of closure. Its graph norm is complete after closure. This fact does not say that \(M\Omega\subset D(S^*S)\). We also have \(F_0\subset F\); equality after closure will be proved only after (FS.2).

## Polar decomposition with its domains

On \(D(S)\), the form

\[
q(\xi,\eta)=\langle S\eta,S\xi\rangle
\]

is nonnegative, densely defined and closed: its form norm is exactly \((\|\xi\|^2+\|S\xi\|^2)^{1/2}\). Apply the **full representation theorem QF-03**. Its representing positive self-adjoint operator \(\Delta\) has

\[
D(\Delta^{1/2})=D(S),\qquad
\langle\Delta^{1/2}\xi,\Delta^{1/2}\eta\rangle
=\langle S\eta,S\xi\rangle.
\tag{FS.9}
\]

The intrinsic domain clause of that theorem, combined with (FS.6), identifies

\[
\Delta=FS,\qquad
D(\Delta)=\{\xi\in D(S):S\xi\in D(F)\}.
\tag{FS.10}
\]

In detail, \(q(\xi,\eta)=\langle v,\eta\rangle\) for every \(\eta\in D(S)\) says precisely that \(S\xi\in D(F)\) and \(FS\xi=v\). If \(\Delta^{1/2}\xi=0\), (FS.9) gives \(S\xi=0\), and (FS.8) gives \(\xi=0\). Thus \(A=\Delta^{1/2}\) is injective and has dense range.

Define \(J\) initially on \(\operatorname{ran}A\) by \(J(A\xi)=S\xi\). Equation (FS.9) makes this a conjugate-linear isometry. Its range is \(D(S)\), which is dense. It extends to a surjective antiunitary on \(H\), and \(S=JA\) on \(D(A)\).

This polar factorization is unique. If \(S=KB\) with \(K\) antiunitary and \(B\geq0\) self-adjoint on the same domain, then its closed form is \(\langle B\xi,B\eta\rangle\). Form uniqueness gives \(B^2=\Delta\), and spectral square-root uniqueness gives \(B=A\). Agreement on dense \(\operatorname{ran}A\) then gives \(K=J\).

The actual inverse has factorization

\[
S^{-1}=A^{-1}J^{-1}
=J^{-1}(JA^{-1}J^{-1}),
\qquad D(S^{-1})=J\operatorname{ran}A.
\]

Here \(A^{-1}\) is self-adjoint on \(\operatorname{ran}A\), and antiunitary transport preserves positivity and self-adjointness, by SK-08. This is a polar factorization of \(S^{-1}=S\). Uniqueness proves

\[
J^{-1}=J,\qquad JAJ=A^{-1},\qquad JD(A)=D(A^{-1}).
\tag{FS.11}
\]

No bounded inverse has been asserted.

For \(\xi\in D(A)\),
\(\langle JA\xi,\eta\rangle=\langle J\eta,A\xi\rangle\).
The adjoint test therefore says \(\eta\in D(F)\) exactly when \(J\eta\in D(A)\), and then \(F\eta=AJ\eta\). Consequently

\[
\begin{array}{c|c|c}
\text{operator}&\text{formula}&\text{domain}\\ \hline
S&JA=A^{-1}J&D(A)\\
F&AJ=JA^{-1}&D(A^{-1})\\
FS&\Delta&\{\xi\in D(S):S\xi\in D(F)\}\\
SF&\Delta^{-1}&\{\xi\in D(F):F\xi\in D(S)\}
\end{array}
\tag{FS.12}
\]

For the last row, the composition condition is \(J\xi\in D(A^2)\); the operator there is \(JA^2J=A^{-2}\), including domains. Equation (FS.11) also shows \(F(D(F))=D(F)\) and \(F^2=1\) there.

Antiunitary spectral transport conjugates scalars. For spectral projections \(E(B)\),
\(J(cE(B))J=\overline c\,JE(B)J\). Simple functions and the squared-integral domain test therefore give

\[
J\Delta^zJ=\Delta^{-\overline z},\qquad
JD(\Delta^z)=D(\Delta^{-\overline z}),
\tag{FS.13}
\]

where

\[
D(\Delta^z)=\left\{\xi:
\int_{(0,\infty)}r^{2\operatorname{Re}z}\,d\langle E(r)\xi,\xi\rangle<\infty\right\}.
\]

In particular \(J\Delta^{it}=\Delta^{it}J\), with the **same** real parameter \(t\). The group \(U_t=\Delta^{it}\) is strongly continuous and preserves all these domains, by SK-07 and SK-09.

Both units give \(S\Omega=F\Omega=\Omega\). Thus \(\Omega\in D(FS)\) and \(\Delta\Omega=\Omega\). Its spectral measure is supported at \(1\), so \(\Delta^z\Omega=\Omega\) for every \(z\). Finally \(J\Omega=S\Omega=\Omega\). This completes the polar and distinguished-vector assertions without any modular commutant identity.

## A resolvent vector from positive-functional separation

Fix \(-\pi<\theta<\pi\), and write

\[
\lambda=e^{i\theta},\qquad
\alpha=(1+\lambda)^{-1}.
\]

Then \(\alpha+\overline\alpha=1\), \(\overline\alpha=\lambda\alpha\), and \(|\alpha|=[2\cos(\theta/2)]^{-1}\). The spectral function \((r+\lambda)^{-1}\) is bounded on \([0,\infty)\), and \((\Delta+\lambda)^{-1}\) maps \(H\) into \(D(\Delta)\).

**Resolvent lemma.** For each \(b\in M'\), there is a unique \(a\in M\) such that

\[
a\Omega=(\Delta+\lambda)^{-1}b\Omega.
\tag{FS.14}
\]

**Proof first for \(0\leq b\leq1\).** Set \(\chi(y)=\langle y\Omega,b\Omega\rangle\). Since \(b^{1/2}\) commutes with \(M\), for \(y\geq0\),

\[
\chi(y)=\langle yb^{1/2}\Omega,b^{1/2}\Omega\rangle\geq0.
\]

Replacing \(b\) by \(1-b\) shows \(0\leq\chi\leq\varphi\).

For self-adjoint contractions \(c\in M\), consider the hermitian functionals

\[
\chi_c(y)=\varphi(\alpha cy+\overline\alpha yc).
\tag{FS.15}
\]

Their set \(K\), regarded by restriction as a subset of \(\mathbb R^{M_{\rm sa}}\), is convex and compact. Indeed, the self-adjoint unit ball is ultraweakly closed in the dual ball and hence compact by CP and AB-05; each coordinate in (FS.15) is ultraweakly continuous in \(c\). Hermitian functionals are determined by their real values on \(M_{\rm sa}\).

If \(\chi\notin K\), a basic product neighborhood separating it from this closed set involves finitely many coordinates. The image of \(K\) in those finitely many coordinates is compact convex and misses the coordinate vector of \(\chi\). Choose a closest point to that vector in the Euclidean norm. Expanding squared distance along line segments in the convex set gives a strictly separating real linear functional. Combining its finitely many coordinates yields a single \(y=y^*\in M\) with

\[
\chi(y)>\sup_{c=c^*,\ \|c\|\leq1}\chi_c(y).
\tag{FS.16}
\]

But positivity, domination and Borel functional calculus give

\[
\chi(y)\leq\chi(|y|)\leq\varphi(|y|)
=\chi_{\operatorname{sgn}(y)}(y).
\]

Here \(\operatorname{sgn}(0)=0\), and \(\operatorname{sgn}(y)y=y\operatorname{sgn}(y)=|y|\). This contradicts (FS.16). Therefore \(\chi=\chi_c\) for a self-adjoint contraction \(c\).

For every \(y\in M\), this equality becomes

\[
\langle y\Omega,b\Omega-\overline\alpha c\Omega\rangle
=\langle\overline\alpha c\Omega,S(y\Omega)\rangle.
\tag{FS.17}
\]

Because \(M\Omega\) is a graph core for \(S\), the equality extends to every vector in \(D(S)\). The adjoint definition, with its reversed entries, gives

\[
F(\overline\alpha c\Omega)=b\Omega-\overline\alpha c\Omega.
\]

Thus \(c\Omega\in D(F)\). Since \(Sc\Omega=c\Omega\), it also lies in \(D(FS)=D(\Delta)\), and conjugate-linearity gives

\[
b\Omega=\alpha\Delta c\Omega+\overline\alpha c\Omega
=(\Delta+\lambda)(\alpha c\Omega).
\]

Set \(a=\alpha c\). This proves (FS.14), with \(\|a\|\leq|\alpha|\), for positive contractions. Every bounded \(b\) is a complex linear combination of four positive contractions, by taking positive and negative parts of its real and imaginary parts and rescaling. Linearity of the resolvent gives the general assertion. Uniqueness follows from separation of \(\Omega\). \(\square\)

The argument uses boundedness of the state at the compact separation step. It has not proved the corresponding resolvent lemma for an arbitrary n.s.f. weight.

## Interpolating the graph core and obtaining the pairing equation

Set

\[
\mathcal D=D(\Delta^{1/2})\cap D(\Delta^{-1/2}),
\qquad T=\Delta^{1/2}+\Delta^{-1/2}\text{ on }\mathcal D.
\]

Its spectral multiplier is \(r^{1/2}+r^{-1/2}\geq2\). Thus \(T^{-1}\) is bounded, maps onto \(\mathcal D\), and

\[
T^{-1}=\Delta^{1/2}(1+\Delta)^{-1},\quad
\Delta^{1/2}T^{-1}=\Delta(1+\Delta)^{-1},\quad
\Delta^{-1/2}T^{-1}=(1+\Delta)^{-1}.
\tag{FS.18}
\]

These are identities of bounded spectral multipliers. Also

\[
\|T\xi\|^2=\|\Delta^{1/2}\xi\|^2+
\|\Delta^{-1/2}\xi\|^2+2\|\xi\|^2.
\tag{FS.19}
\]

The cross term equals \(\|\xi\|^2\), first on spectral bands and then by convergence of both powers.

Since \(F(b\Omega)=b^*\Omega\), we know

\[
\Delta^{-1/2}M'\Omega=JM'\Omega,
\]

which is dense. For a given \(\xi\in\mathcal D\), choose \(b_n\in M'\) such that \(\Delta^{-1/2}b_n\Omega\to T\xi\). Define

\[
\xi_n=(1+\Delta)^{-1}b_n\Omega
=T^{-1}\Delta^{-1/2}b_n\Omega.
\]

The resolvent lemma at \(\theta=0\) places \(\xi_n\) in \(M\Omega\), and (FS.18) places it in \(\mathcal D\). The three bounded multipliers in (FS.18) prove convergence of \(\xi_n\), \(\Delta^{1/2}\xi_n\), and \(\Delta^{-1/2}\xi_n\) to the corresponding values at \(\xi\). Hence

\[
M\Omega\cap\mathcal D
\text{ is a core for the joint graph norm of the two powers.}
\tag{FS.20}
\]

This is the needed interpolation statement; Hilbert-norm density alone would not suffice.

Now choose \(a,b\) as in (FS.14), and put \(Y=Ja^*J\). We claim

\[
\boxed{\ 
\langle b\xi,\eta\rangle
=\langle Y\Delta^{-1/2}\xi,\Delta^{1/2}\eta\rangle
+\lambda\langle Y\Delta^{1/2}\xi,\Delta^{-1/2}\eta\rangle
\quad(\xi,\eta\in\mathcal D).
\ }
\tag{FS.21}
\]

First let \(\xi=v\Omega\), \(\eta=u\Omega\) belong to \(M\Omega\cap\mathcal D\). The resolvent equation and the adjoint pairing give

\[
\begin{aligned}
\langle b\xi,\eta\rangle
&=\langle(\Delta+\lambda)a\Omega,v^*u\Omega\rangle\\
&=\langle S(v^*u\Omega),Sa\Omega\rangle
 +\lambda\langle va\Omega,u\Omega\rangle\\
&=\langle\xi,ua^*\Omega\rangle
 +\lambda\langle va\Omega,\eta\rangle.
\end{aligned}
\tag{FS.22}
\]

The first pairing in (FS.21) equals

\[
\begin{aligned}
\langle Ja^*J\Delta^{-1/2}\xi,\Delta^{1/2}\eta\rangle
&=\langle Ja^*F\xi,Ju^*\Omega\rangle\\
&=\langle au^*\Omega,F\xi\rangle
=\langle\xi,S(au^*\Omega)\rangle
=\langle\xi,ua^*\Omega\rangle.
\end{aligned}
\]

For the second, \(Y\Delta^{1/2}\xi=Ja^*v^*\Omega
=JS(va\Omega)=\Delta^{1/2}(va\Omega)\). Spectral multiplication therefore gives

\[
\langle Y\Delta^{1/2}\xi,\Delta^{-1/2}\eta\rangle
=\langle va\Omega,\eta\rangle.
\]

All adjoint tests have vectors in their domains: \(a\Omega\in D(\Delta)\), \(au^*\Omega,va\Omega\in D(S)\), and \(\xi,\eta\in\mathcal D\). Now use (FS.20) to pass to arbitrary \(\xi,\eta\in\mathcal D\). Boundedness of \(b,Y\) and simultaneous convergence of both powers justify each pairing. Equation (FS.21) does not claim that \(Y\) preserves either unbounded domain.

## The scalar cosh kernel and a bounded inverse

Put

\[
w(t)=2\cosh(\pi t),\qquad
k_\theta(t)=\frac{e^{-\theta t-i\theta/2}}{w(t)}.
\tag{FS.23}
\]

Since \(|\theta|<\pi\), this continuous kernel is integrable. For \(r>0\),

\[
\int_{\mathbb R}k_\theta(t)r^{-it}\,dt
=\frac{\sqrt r}{r+e^{i\theta}},
\qquad
\|k_\theta\|_1=\frac1{2\cos(\theta/2)}=|\alpha|.
\tag{FS.24}
\]

Here are the signs and constants of the scalar proof. For \(|\operatorname{Im}u|<\pi\), integrate
\(f_u(z)=e^{-iuz}/(2\cosh\pi z)\) over the positively oriented rectangle with vertices \(-R,R,R+i,-R+i\). The sole pole is \(i/2\), with residue \(e^{u/2}/(2\pi i)\). The denominator on a vertical side has modulus at least \(e^{\pi R}-e^{-\pi R}\), while the numerator is at most \(C_u e^{|\operatorname{Im}u|R}\); hence those two integrals tend to zero. Since \(f_u(t+i)=-e^u f_u(t)\), the bottom and top edges give

\[
(1+e^u)\int_{\mathbb R}\frac{e^{-iut}}{w(t)}\,dt=e^{u/2}.
\tag{FS.25}
\]

This uses exactly the rectangle/simple-residue input of MA-05; alternatively subtract the displayed principal part at \(i/2\), apply rectangle Cauchy to the regular remainder and integrate the principal part. Set \(u=\log r-i\theta\) and multiply by \(e^{-i\theta/2}\) to obtain the first identity in (FS.24). Setting \(u=-i\theta\) gives the positive integral of \(e^{-\theta t}/w(t)\), proving the norm identity.

By the spectral theorem, in the vectorwise strong sense of MA-02,

\[
\Delta^{1/2}(\Delta+\lambda)^{-1}
=\int_{\mathbb R}k_\theta(t)\Delta^{-it}\,dt.
\tag{FS.26}
\]

For completeness, compress to \(E_n=1_{[1/n,n]}(\Delta)\). On the band both sides follow from (FS.24) and bounded spectral calculus. The integrals converge strongly as \(E_n\uparrow1\), by the common integrable bound \(|k_\theta(t)|\|\xi\|\) for each vector. The multiplier \(\sqrt r/(r+\lambda)\) is bounded, and the resolvent really maps into \(D(\Delta)\), so the displayed left-side composition has the asserted everywhere-defined meaning.

**Bounded pairing inversion.** Let \(X,Y\in B(H)\). If

\[
\langle X\xi,\eta\rangle
=\langle Y\Delta^{-1/2}\xi,\Delta^{1/2}\eta\rangle
+\lambda\langle Y\Delta^{1/2}\xi,\Delta^{-1/2}\eta\rangle
\quad(\xi,\eta\in\mathcal D),
\tag{FS.27}
\]

then necessarily

\[
Y=\int_{\mathbb R}k_\theta(t)\Delta^{-it}X\Delta^{it}\,dt.
\tag{FS.28}
\]

Conversely (FS.28) always defines a bounded operator satisfying (FS.27), and \(\|Y\|\leq|\alpha|\|X\|\).

**Proof.** Fix a nonzero spectral band \(E_nH\), put \(A=\Delta|_{E_nH}\), and let \(X_n,Y_n\) be the compressions. The weak equation there is equivalent to the bounded equation

\[
A^{1/2}X_nA^{1/2}=AY_n+\lambda Y_nA.
\tag{FS.29}
\]

Indeed the first pairing in (FS.27) represents \(A^{1/2}Y_nA^{-1/2}\), and the second represents \(\lambda A^{-1/2}Y_nA^{1/2}\). This establishes the order of the two terms before inversion.

If \(A=\sum_jr_jP_j\) has finite spectrum, the \((i,j)\) corner of the integral in (FS.28) is

\[
\left(\int k_\theta(t)(r_i/r_j)^{-it}\,dt\right)P_iX_nP_j
=\frac{\sqrt{r_ir_j}}{r_i+\lambda r_j}P_iX_nP_j.
\]

Multiplication by \(r_i+\lambda r_j\) gives precisely the corresponding corner of (FS.29). For a general \(A\), approximate it in norm by finite spectral sums \(A_m\) with spectra in \([1/n,n]\). Continuous calculus gives norm convergence of their square roots and, for each fixed \(t\), their imaginary powers. Dominated convergence with bound \(|k_\theta|\|X_n\|\) shows convergence of the band integrals in operator norm. Passing to the limit proves (FS.29) for the proposed integral.

There is at most one bounded solution of (FS.29). If \(AZ+\lambda ZA=0\), put \(c=e^{-i\theta/2}\). Norm differentiation of bounded-operator exponential series gives

\[
\frac d{ds}\left(e^{-csA}Ze^{-c\lambda sA}\right)=0.
\]

Both exponential factors have norm at most \(e^{-s\cos(\theta/2)/n}\). Letting \(s\to\infty\) shows that their constant product, whose value at zero is \(Z\), is zero. This proves uniqueness. A zero spectral band requires no argument.

Compression of the global strong integral equals the band integral, since \(E_n\) commutes with all imaginary powers. Thus any solution of (FS.27) has its every compression given by (FS.28); \(E_nYE_n\to Y\) strongly proves necessity. For existence, start with the global integral. Its compressions satisfy (FS.29), hence (FS.27) on each band. For \(\xi,\eta\in\mathcal D\), the vectors \(E_n\xi,E_n\eta\) converge together with both powers by SK-09, so every term in (FS.27) converges. The integral norm estimate follows from MA-02 and (FS.24). \(\square\)

This proves the complex-unit-parameter version needed by the state separation argument. The real-parameter versions already proved in MA-06–07 have different kernels and are not silently substituted for it.

## Recovering commutation from the integral identity

Fix \(b,d\in M'\). For each \(\theta\), take the \(a\in M\) from (FS.14). Applying (FS.28) to (FS.21) gives

\[
Ja^*J=\int k_\theta(t)U_{-t}bU_t\,dt.
\]

Conjugating by the antiunitary conjugates the scalar kernel. If
\(B_t=JU_{-t}bU_tJ\), then

\[
a^*=\int\overline{k_\theta(t)}B_t\,dt.
\tag{FS.30}
\]

On the other hand, (FS.26), the resolvent-vector formula and \(S=J\Delta^{1/2}\) give

\[
a^*\Omega
=J\Delta^{1/2}(\Delta+\lambda)^{-1}b\Omega
=\int\overline{k_\theta(t)}JU_{-t}b\Omega\,dt.
\tag{FS.31}
\]

These manipulations are legitimate on vectors: an antiunitary is real-linear continuous and sends a vector integral of \(k(t)v(t)\) to that of \(\overline{k(t)}Jv(t)\).

Since \(a^*\in M\) commutes with \(d\), subtract (FS.31), multiplied by \(d\), from (FS.30) applied to \(d\Omega\). Remove the nonzero phase \(e^{i\theta/2}\). The result is

\[
\int_{\mathbb R}\frac{e^{-\theta t}}{w(t)}v(t)\,dt=0,
\quad
v(t)=B_td\Omega-dJU_{-t}b\Omega,
\quad -\pi<\theta<\pi.
\tag{FS.32}
\]

The vector function \(v\) is continuous and bounded by \(2\|b\|\|d\|\|\Omega\|\). We spell out the uniqueness step because (FS.32) initially contains real exponentials, not Fourier characters. For fixed \(\eta\in H\), set

\[
G_\eta(z)=\int_{\mathbb R}
\frac{e^{-zt}}{w(t)}\langle v(t),\eta\rangle\,dt,
\qquad |\operatorname{Re}z|<\pi.
\]

On a disc centered at \(z_0\) whose radius \(r\) satisfies \(|\operatorname{Re}z_0|+r<\pi\), expand \(e^{-(z-z_0)t}\) in its power series. The sum of absolute values is bounded by \(e^{r|t|}\), so the common exponential tail permits termwise integration and yields a convergent local power series. Hence \(G_\eta\) is holomorphic. It vanishes on the real interval by (FS.32). All derivatives at its real interior points are therefore zero, so its power series is zero on a disc. Overlapping discs along a path inside the strip propagate this zero germ throughout the strip. This is the elementary power-series proof of the identity theorem in the present case.

In particular, at \(z=is\) it gives

\[
\int_{\mathbb R}e^{-ist}
\frac{\langle v(t),\eta\rangle}{w(t)}\,dt=0
\qquad(s\in\mathbb R).
\]

The scalar function is continuous and integrable. **MA-04**, whose proof uses the explicit Gaussian transform and approximation to the identity, makes it zero at every \(t\). As \(w(t)>0\) and \(\eta\) is arbitrary, \(v(t)=0\) for every \(t\).

Since \(U_tJ\Omega=\Omega\), this says

\[
B_td\Omega=dB_t\Omega\qquad(d\in M').
\tag{FS.33}
\]

For \(d_1,d_2\in M'\), applying it to \(d_1d_2\) and then to \(d_2\) gives
\(B_td_1d_2\Omega=d_1B_td_2\Omega\). Density of \(M'\Omega\) proves \(B_t\in(M')'=M\). We have obtained

\[
JU_{-t}M'U_tJ\subset M,
\qquad JM'J\subset M\quad(t=0).
\tag{FS.34}
\]

Scalarization was performed for each vector separately. No countable family of functionals or vectors was chosen.

## The reverse commutant inclusion and modular invariance

The inclusion at \(t=0\) in (FS.34) is only one of the two necessary inclusions. We prove the other directly, retaining the domains.

Fix \(a,y\in M\) and \(b\in M'\). Put \(c=JbJ\), which belongs to \(M\) by (FS.34). Then \(c^*=Jb^*J\in M\), so
\(a^*c^*\Omega\in M\Omega\subset D(S)\). The identity \(FJ=JS\) is therefore applicable to this vector. We compute

\[
\begin{aligned}
\langle yJa\Omega,b^*\Omega\rangle
&=\langle bJa\Omega,y^*\Omega\rangle\\
&=\langle Jca\Omega,y^*\Omega\rangle\\
&=\langle JS(a^*c^*\Omega),y^*\Omega\rangle\\
&=\langle FJa^*Jb^*\Omega,y^*\Omega\rangle\\
&=\langle S(y^*\Omega),Ja^*Jb^*\Omega\rangle\\
&=\langle JaJy\Omega,b^*\Omega\rangle.
\end{aligned}
\tag{FS.35}
\]

The fifth line uses the adjoint pairing between \(F=S^*\) and \(S=F^*\), justified by closedness and TC-03. The preceding domain observation puts \(Ja^*Jb^*\Omega=J(a^*c^*\Omega)\) in \(D(F)\); also \(y^*\Omega\in D(S)\). Thus this is not formal multiplication of unbounded operators.

Density of \(M'\Omega\) gives \(yJa\Omega=JaJy\Omega\). Since \(JaJ\Omega=Ja\Omega\), applying this equality to products \(y_1y_2\) and to \(y_2\) proves that \(JaJ\) commutes with \(y_1\) on dense \(M\Omega\). Hence \(JMJ\subset M'\). Conjugating \(JM'J\subset M\) by \(J\) gives the reverse inclusion \(M'\subset JMJ\). Therefore \(JMJ=M'\).

Conjugate (FS.34) by \(J\) to obtain \(U_{-t}M'U_t\subset M'\). Applying the same inclusion at \(-t\) gives equality. Taking commutants, using \(M=M''\), proves

\[
U_tMU_{-t}=M.
\]

Thus \(\sigma_t^\varphi=\operatorname{Ad}U_t|_M\) is a group of *-automorphisms. It is normal because fixed bounded multiplication is ultraweakly continuous, and its inverse is \(\sigma_{-t}^\varphi\). Strong continuity of \(U_t\) gives strong continuity of \(U_taU_{-t}\) on each vector. Applying the same reasoning to \(a^*\) gives point-strong* continuity. Since \(U_t\Omega=\Omega\),

\[
\varphi(\sigma_t^\varphi(a))
=\langle U_taU_{-t}\Omega,\Omega\rangle
=\langle a\Omega,\Omega\rangle=\varphi(a),
\]

and \(\sigma_t^\varphi(a)\Omega=U_ta\Omega\), proving (FS.3).

Finally \(F=JSJ\) with domain \(JD(S)\). The antiunitary \(J\) transports the graph core \(M\Omega\) for \(S\) to a graph core \(JM\Omega=M'\Omega\) for \(F\). More explicitly, \(JS_0J=F_0\) on \(M'\Omega\): writing \(b=JaJ\), one obtains \(JS_0J(b\Omega)=Ja^*\Omega=b^*\Omega\). Taking closures gives

\[
\boxed{\ \overline{F_0}=J\overline{S_0}J=JSJ=S^*.\ }
\tag{FS.36}
\]

Thus \(M'\Omega\) is a graph core for \(S^*\). This completes every assertion in FS-01 and supplies the adjoint-core conclusion for the separate state natural-cone companion.

## Normalization and a bounded tracial density

**Positive-scalar normalization lemma (FS-10a).** Let \(\Phi\) be a faithful normal positive functional with \(0<\Phi(1)<\infty\), and let \(r>0\). Denote the corresponding GNS spaces by \(H_\Phi,H_{r\Phi}\), with their algebraic vectors \(\Lambda_\Phi(a)\) and \(\Lambda_{r\Phi}(a)\). The map

\[
W_r\Lambda_\Phi(a)=r^{-1/2}\Lambda_{r\Phi}(a)
\]

extends to a unitary \(H_\Phi\to H_{r\Phi}\). It intertwines the left representations and all modular data:

\[
W_rS_\Phi W_r^*=S_{r\Phi},\qquad
W_r\Delta_\Phi W_r^*=\Delta_{r\Phi},\qquad
W_rJ_\Phi W_r^*=J_{r\Phi}.
\]

**Proof.** On algebraic vectors, the factor \(r^{-1/2}\) cancels the factor \(r\) in the squared GNS norm, so \(W_r\) is an isometry with dense range and hence extends to a unitary. Left multiplication visibly intertwines. The factor is positive real, so conjugate-linearity causes no phase:

\[
W_rS_{\Phi,0}\Lambda_\Phi(a)
=r^{-1/2}\Lambda_{r\Phi}(a^*)
=S_{r\Phi,0}W_r\Lambda_\Phi(a).
\]

Taking graph closures gives the first operator equality with domains. Adjoint transport and \(\Delta=S^*S\) give the second, and uniqueness of the polar factors gives the third. All construction facts for \(\Phi\) follow by transport from the normalized state \(\Phi/\Phi(1)\), so this argument adds no general-weight prerequisite. In particular, replacing \(\Phi\) by \(\Phi/2\) leaves \(S,\Delta,J\) unchanged under the canonical identification \(W_{1/2}\Lambda_\Phi(a)=\sqrt2\Lambda_{\Phi/2}(a)\). The distinguished cyclic vector itself is rescaled: \(W_r\Lambda_\Phi(1)=r^{-1/2}\Lambda_{r\Phi}(1)\). \(\square\)

**Bounded tracial density.**

Let \(N\) have a faithful normal tracial state \(\tau\), and let \(h\in N\) be positive and boundedly invertible. The normalized state is

\[
\omega(a)=\frac{\tau(ha)}{\tau(h)}.
\]

It is positive, normal and faithful: traciality gives \(\tau(ha)=\tau(h^{1/2}ah^{1/2})\) for \(a\geq0\), normality follows from fixed multiplication, and \(h\geq\varepsilon1\) implies \(\tau(ha)\geq\varepsilon\tau(a)\).

On \(L^2(N,\tau)\), define \(L_a z=az\), \(R_a z=za\) initially on \(N\). Right multiplication is bounded because

\[
\|za\|_2^2=\tau(a^*z^*za)=\tau(z^*zaa^*)
\leq\|a\|^2\tau(z^*z).
\]

Left and right multiplication commute, and the trace pairing gives \(R_a^*=R_{a^*}\). For \(a\geq0\), \(\langle R_a z,z\rangle=\tau(z^*za)\geq0\), so positive right multipliers are positive operators. The map \(J_\tau z=z^*\) extends to an antiunitary involution by traciality. With \(c=\tau(h)^{1/2}\), the vector \(\Omega=h^{1/2}/c\) is cyclic because right multiplication by \(h^{1/2}\) is boundedly invertible. It is separating because \(a h^{1/2}=0\) forces \(a=0\).

The operators \(L_h,R_{h^{-1}}\) are commuting positive bounded invertible operators. Put

\[
D=L_hR_{h^{-1}},\qquad
D^{1/2}=L_{h^{1/2}}R_{h^{-1/2}}.
\]

The square-root assertion follows by squaring the positive commuting product and using uniqueness. On every \(a\Omega\),

\[
J_\tau D^{1/2}(a h^{1/2}/c)
=J_\tau(h^{1/2}a/c)=a^*h^{1/2}/c.
\]

Since \(J_\tau D^{1/2}\) is bounded and \(N\Omega\) is dense, it is the closure of the state Tomita operator. Polar uniqueness identifies \(J=J_\tau\), \(\Delta=D\).

To justify imaginary powers without assuming an unproved joint spectral formula, set \(k=\log h\in N_{\rm sa}\). The bounded commuting self-adjoint operators \(L_k,R_k\) satisfy
\(D=\exp(L_k-R_k)\), by the exponential series and continuous calculus. Therefore spectral change of variable gives

\[
D^{it}=\exp(it(L_k-R_k))=L_{h^{it}}R_{h^{-it}}.
\]

Conjugating left multiplication now yields the explicit state dynamics

\[
\boxed{\ \sigma_t^\omega(a)=h^{it}ah^{-it}.\ }
\tag{FS.37}
\]

Multiplying \(h\) by a positive scalar leaves this formula unchanged; its normalization affects the vector's length, not modular time.

## Worked examples and exercises

**Example 1: a two-level nontracial state.** On the Hilbert space of \(2\times2\) matrices with inner product \(\operatorname{Tr}(z^*x)\), let
\(\rho=\operatorname{diag}(p,q)\), \(p,q>0\), \(p+q=1\), and \(\Omega=\rho^{1/2}\). Represent \(M_2(\mathbb C)\) by left multiplication. Direct computation from FS-10 gives

\[
Jz=z^*,\qquad \Delta z=\rho z\rho^{-1},\qquad
\Delta e_{ij}=\frac{p_i}{p_j}e_{ij},
\quad (p_1,p_2)=(p,q).
\]

Consequently \(\sigma_t(e_{12})=(p/q)^{it}e_{12}\). The different eigenvalues of the state create a nontrivial rotation of the off-diagonal observation; diagonal observations remain fixed.

**Exercise 1: check the antiunitary sign.** Compute \(J\Delta^{it}e_{12}\) and \(\Delta^{it}Je_{12}\). Does \(J\Delta^{it}J=\Delta^{-it}\) hold?

**Solution.** The first vector is \((p/q)^{-it}e_{21}\), because \(J\) conjugates the scalar. The second is \((q/p)^{it}e_{21}\), the same vector. Thus \(J\Delta^{it}J=\Delta^{it}\). Unless the parameters give an accidental equality, the negative-time expression is different. The positive operator is inverted and its complex exponent is conjugated; both changes must be retained.

**Exercise 2: check the complex resolvent and both indices.** In the same matrix model take \(b'=R_b\in M'\). Find the matrix \(a\) satisfying \((\Delta+\lambda)a\Omega=b'\Omega\), and verify \(Ja^*J=R_a\).

**Solution.** Entrywise, the right side is \(\sqrt{p_i}\,b_{ij}\), while the left side is \((p_i/p_j+\lambda)a_{ij}\sqrt{p_j}\). Hence

\[
a_{ij}=\frac{\sqrt{p_ip_j}}{p_i+\lambda p_j}\,b_{ij}.
\]

For any matrix \(z\), \(Ja^*J(z)=(a^*z^*)^*=za\), so the result is \(R_a\). The denominator is \(p_i+\lambda p_j\); interchanging its coefficients would reverse the two terms in (FS.29).

**Exercise 3: conjugation of an integral.** If \(J\) is antiunitary and \(Y=\int k(t)T(t)\,dt\) is a vectorwise strong integral, determine \(JYJ\). Apply this to (FS.28).

**Solution.** For a fixed vector, pass \(J\) through the real Riemann sums and their norm limits. The result is \(JYJ=\int\overline{k(t)}JT(t)J\,dt\). Thus (FS.30) has phase \(e^{+i\theta/2}\), not \(e^{-i\theta/2}\). The factor \(e^{-\theta t}\) is real and is unchanged.

**Example 2: two distinct half-power domains.** This is an abstract closed-involution model, not a new representation theorem. On \(\ell^2(\mathbb N\times\{+,-\})\), put

\[
\Delta e_{n,+}=n^2e_{n,+},\qquad
\Delta e_{n,-}=n^{-2}e_{n,-},
\]

and let \(J\) conjugate coefficients and interchange the two signs. Then \(J\Delta J=\Delta^{-1}\), and \(S=J\Delta^{1/2}\) is a closed conjugate-linear involution on its exact domain.

**Exercise 4: identify the domains.** Show that \(\xi_+=\sum_{n\geq1}n^{-1}e_{n,+}\) lies in \(D(\Delta^{-1/2})\) but not \(D(\Delta^{1/2})\), and that the roles reverse for \(\xi_-=\sum_{n\geq1}n^{-1}e_{n,-}\).

**Solution.** Both vectors are square summable. For \(\xi_+\), application of \(\Delta^{1/2}\) would give coefficients \(1\), which are not square summable, while \(\Delta^{-1/2}\) gives \(n^{-2}\), which are. For \(\xi_-\) the two multipliers interchange. Thus neither half-power domain contains the other. A pairing such as (FS.21) cannot be extended to one half-power domain merely by suppressing the other domain condition.

**Exercise 5: why ordinary density is insufficient.** Explain exactly what the approximation in FS-06 adds to density of \(M\Omega\). Verify that the approximating vectors converge in the three-term graph norm.

**Solution.** Ordinary density controls only \(\|\xi_n-\xi\|\). In (FS.21), one must also control \(\Delta^{1/2}(\xi_n-\xi)\) and \(\Delta^{-1/2}(\xi_n-\xi)\). If \(r_n=\Delta^{-1/2}b_n\Omega-T\xi\to0\), these three differences are respectively \(T^{-1}r_n\), \(\Delta(1+\Delta)^{-1}r_n\), and \((1+\Delta)^{-1}r_n\). Their norms tend to zero because each displayed multiplier is bounded.

**Exercise 6: the tracial endpoint.** Prove that a faithful normal tracial state has \(\Delta=1\) and trivial modular dynamics in its GNS representation.

**Solution.** Traciality gives \(\|a^*\Omega\|^2=\varphi(aa^*)=\varphi(a^*a)=\|a\Omega\|^2\). Hence \(S_0\) extends to an antiunitary involution on all of \(H\). Its modulus is the identity, so polar uniqueness gives \(\Delta=1\). Therefore \(\sigma_t(a)=a\) for every \(t\).

**Exercise 7: a state does not force separability.** Identify every use of sequences or countable sums in the proof and explain why none is a hypothesis that \(H\) is separable.

**Solution.** CP expresses one predual functional by a summable series, on the arbitrary space \(H\). Completion, graph closure and approximation of one fixed vector occur in metric spaces and admit sequences. The bands \(1_{[1/n,n]}(\Delta)\) exhaust the positive real spectral axis, independently of multiplicity or Hilbert dimension. Finally Fourier uniqueness is applied separately to each scalar coefficient. None of these statements produces or uses a countable dense set of all vectors.

## Source locators and proof boundaries

The free human scholarly source consulted was Brent Nelson, [*Tomita–Takesaki Theory*](https://users.math.msu.edu/users/banelson/files/Tomita-Takesaki%20Theory.pdf): **Lemma 1.20, printed p. 9** (pairing equation and simultaneous half-power approximation); **Lemma 1.21, printed p. 10** (cosh-kernel inversion); **Lemma 1.22, printed pp. 10–11** (spectral resolvent); **Lemma 1.23, printed p. 11** (bounded inversion by spectral compression); and **the proof of Theorem 1.24, printed pp. 11–12** (integral commutation and Fourier uniqueness). These selected proof passages were read. The present state argument supplies its own compact positive-functional separation, complex-parameter kernel and domain-checked reverse inclusion. It imports none of Nelson's general Hilbert-algebra modular theorem. The complete local QF/TC form proof supplies self-adjointness and polar identities.

The other candidate examined was **P20, “Haagerup modular approximation,” Step 1, §§1.1–1.5**, an AI-generated candidate supplied for review, SHA-256 `f93c69db9f110fc4ef2d3bfe59150d1db3837fb958cb215942806632aa6fedc5`. It is not identified as a human scholarly source. Its encompassing injective type-III₁ factor and separable-predual hypotheses are not used in this state's modular theorem. Its trace-class preadjoint step has been replaced here by the already established CP projective tensor and quotient dualities.

This companion establishes only the assertions stated in FS-01 and its bounded-density model. It leaves the existing general n.s.f.-weight, full Hilbert-algebra, natural-cone, KMS-characterization and standard-form developments in their existing ownership and scope. Their substantive proofs and the complete B1–B9 objective remain required.
