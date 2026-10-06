# Building the two multiplication actions of a Hilbert algebra

**Self-checked by the writing AI.**

A Hilbert algebra starts with vectors that can be multiplied. Its completion contains many more vectors, and multiplication does not automatically extend to every pair. The useful extension is asymmetric: an algebra vector acts boundedly from the left, while a right-bounded vector acts boundedly from the right. This unit constructs those actions, proves their commutation and adjoint relations, and identifies the closed operators attached to vectors in the adjoint-involution domain.

The free comparison is François Combes, [*Poids associé à une algèbre hilbertienne à gauche* (1971), page 50 and Definition 2.1–Lemma 2.3 on page 51](https://www.numdam.org/item/CM_1971__23_1_49_0.pdf). These passages specify the Hilbert-algebra axioms and bounded multiplication vectors. We prove the representation, commutation, covariance and adjoint claims below from those axioms. The graph and polar statements have the earlier written proofs linked in HA04. A source citation supplies no omitted proof, and none of Combes’s later modular conclusions is an input here.

## Starting data and the multiplication domains

Let \(\mathcal A\) be a complex associative algebra with a conjugate-linear involution \(a\mapsto a^\sharp\), so

\[
(ab)^\sharp=b^\sharp a^\sharp,\qquad
(a^\sharp)^\sharp=a.
\tag{HA.1}
\]

Equip \(\mathcal A\) with a positive-definite inner product, linear in its first variable, and let \(H\) be its Hilbert completion. We identify \(\mathcal A\) with its dense image in \(H\). No unit, separability, or countability hypothesis is imposed. The zero algebra and zero Hilbert space are allowed.

A **left Hilbert algebra** has the following four properties:

1. For each \(a\in\mathcal A\), some finite \(c_a\) satisfies \(\|ab\|\leq c_a\|b\|\) for every \(b\in\mathcal A\).
2. The multiplication and involution obey

   \[
   \langle ab,c\rangle=\langle b,a^\sharp c\rangle
   \qquad(a,b,c\in\mathcal A).
   \tag{HA.2}
   \]

3. The conjugate-linear map \(s:\mathcal A\to H\), \(sa=a^\sharp\), is closable for the Hilbert norm.
4. The linear span \(\mathcal A^2=\operatorname{span}\{ab:a,b\in\mathcal A\}\) is dense in \(H\).

The third property says that \(a_n\to0\) and \(a_n^\sharp\to b\) imply \(b=0\). This sequence test uses metrizability of the Hilbert norm, not separability of \(H\). Property 4 is Hilbert-norm density. It does not yet say that \(\mathcal A^2\) is a core for the closed involution.

The preceding proof BK01 supplies completion, extension from a dense subspace, bounded adjoints and orthogonal projections for arbitrary Hilbert spaces. Its real Riesz and projection foundation is written in the linked programme note. BK02 proves the bicommutant theorem, and BK08 proves the finite unitary-span assertion. TC03 proves the linear and conjugate-linear graph and adjoint lemmas; TC05 proves closure of a densely defined involution. Only the polar conclusions in HA04 use TC07–10, whose form and spectral constructions have exact preceding proofs. The multiplication arguments depend on the graph statements alone.

For clarity, a right Hilbert algebra uses bounded right multiplication and the adjoint identity

\[
\langle ab,c\rangle=\langle a,c b^\flat\rangle,
\tag{HA.3}
\]

with a closable algebraic involution \(\flat\) and dense products. Its bounded multiplication map reverses the order of products.

## Faithful left multiplication without a unit

For \(a\in\mathcal A\), property 1 gives a unique bounded extension

\[
L_a:H\longrightarrow H,\qquad L_a b=ab\quad(b\in\mathcal A).
\tag{HA.4}
\]

**Theorem.** The map \(a\mapsto L_a\) is an injective algebraic *-representation:

\[
L_{\alpha a+\beta b}=\alpha L_a+\beta L_b,\qquad
L_{ab}=L_aL_b,\qquad L_{a^\sharp}=L_a^*.
\tag{HA.5}
\]

It is nondegenerate, in the precise sense

\[
\overline{\operatorname{span}\{L_a\xi:a\in\mathcal A,\ \xi\in H\}}=H.
\tag{HA.6}
\]

In particular,

\[
\bigl[L_a\xi=0\text{ for all }a\in\mathcal A\bigr]\Longrightarrow \xi=0.
\tag{HA.7}
\]

**Proof.** The first two identities hold on \(\mathcal A\), by linearity and associativity, and hence hold on \(H\) by boundedness and density. Equation (HA.2) says that \(L_{a^\sharp}\) has the defining pairing of \(L_a^*\) on a dense set in both variables. Continuity extends that pairing to \(H\times H\), proving the last identity.

The span in (HA.6) contains \(\mathcal A^2\), so property 4 proves nondegeneracy. More directly, if \(L_a\xi=0\) for every \(a\), then

\[
\langle \xi,a^\sharp b\rangle=\langle L_a\xi,b\rangle=0
\qquad(a,b\in\mathcal A).
\]

As \(\sharp\) maps \(\mathcal A\) onto itself, the test vectors span \(\mathcal A^2\). Density gives \(\xi=0\), proving (HA.7).

Finally suppose \(L_a=0\). Taking adjoints gives \(L_{a^\sharp}=0\). For \(b\in\mathcal A\),

\[
ba=(a^\sharp b^\sharp)^\sharp=0.
\]

Thus \(L_ba=0\) for every \(b\), and (HA.7) gives \(a=0\). This proves injectivity without inserting an algebra unit. \(\square\)

For every integer \(n\geq2\), the span \(\mathcal A^n\) of \(n\)-fold products is also Hilbert-norm dense. Indeed, if \(\mathcal A^n\) is dense and \(a,b\in\mathcal A\), approximate \(b\) in norm by elements \(v_k\in\mathcal A^n\). Boundedness of \(L_a\) gives \(av_k\to ab\). Hence the closure of \(\mathcal A^{n+1}\) contains \(\mathcal A^2\), which is dense. Induction starts at property 4. These approximations do not control the involution graph norm.

For an independently given right Hilbert algebra \(\mathcal D\), apply this theorem to the opposite product \(a\circ b=ba\). Equation (HA.3) becomes
\(\langle a\circ b,c\rangle=\langle b,a^\flat\circ c\rangle\), so all four left Hilbert algebra properties hold for \(\mathcal D^{\mathrm{op}}\). Thus right multiplication extends to an injective nondegenerate anti *-representation:

\[
R_{ab}=R_bR_a,\qquad R_{b^\flat}=R_b^*.
\tag{HA.46}
\]

Its product order is reversed precisely because it represents the opposite algebra.

## The generated algebra and its commutant

Set

\[
M=L(\mathcal A)'',\qquad
L(\mathcal A)=\{L_a:a\in\mathcal A\}.
\tag{HA.8}
\]

Here commutants are taken in \(B(H)\). The algebra \(M\) is unital even when \(\mathcal A\) is not. Its commutant is \(M'=L(\mathcal A)'\): the general identity \(E'''=E'\) follows because \(E\subseteq E''\), while every member of \(E'\) commutes with every member of \((E')'=E''\).

**Nonunital density lemma.** If a *-subalgebra \(\mathcal C\subseteq B(H)\) is nondegenerate, then

\[
\overline{\mathcal C}^{\mathrm{SOT}}
=\overline{\mathcal C}^{\mathrm{WOT}}
=\mathcal C''.
\tag{HA.9}
\]

No norm bound is asserted for the approximating nets.

**Proof.** Fix \(T\in\mathcal C''\) and finitely many vectors \(\xi_1,\ldots,\xi_n\). On \(H^n\), write \(D(c)=\operatorname{diag}(c,\ldots,c)\), \(\Xi=(\xi_1,\ldots,\xi_n)\), and let \(P\) project onto

\[
K=\overline{\{D(c)\Xi:c\in\mathcal C\}}.
\]

The set inside closure is linear. Since \(\mathcal C\) is an algebra closed under adjoints, \(K\) is invariant under \(D(c)\) and \(D(c)^*\). Thus \(P\) commutes with every \(D(c)\). For all \(c\in\mathcal C\),

\[
D(c)(I-P)\Xi=(I-P)D(c)\Xi=0.
\]

Nondegeneracy of \(\mathcal C\), applied to each coordinate, gives \((I-P)\Xi=0\). This is the step that replaces a unit.

Every matrix entry \(P_{jk}\) commutes with \(\mathcal C\), so it commutes with \(T\). Consequently \(D(T)P=PD(T)\), and \(D(T)\Xi\in K\). Given \(\varepsilon>0\), the definition of \(K\) therefore supplies \(c\in\mathcal C\) with

\[
\sum_{j=1}^n\|(c-T)\xi_j\|^2<\varepsilon^2.
\]

These conditions characterize membership of \(T\) in the strong closure. The reverse inclusions follow because strong convergence implies weak operator convergence, and \(\mathcal C''\) is weak operator closed by OA-MOD-BK-02. \(\square\)

Apply this lemma to \(L(\mathcal A)\). In particular, there is a net of left multipliers converging strongly to \(I_H\). An infinite or uncountable algebra is not supplied with an identity vector by this assertion.

## The closed involution and what its polar data say

Put

\[
S=\overline s,\qquad F=S^*=s^*.
\tag{HA.10}
\]

The adjoint convention is

\[
\langle S\xi,\eta\rangle=\langle F\eta,\xi\rangle
\quad(\xi\in D(S),\ \eta\in D(F)).
\tag{HA.11}
\]

OA-MOD-TC-03 and OA-MOD-TC-05 give closed dense domains, the graph core \(\mathcal A\subseteq D(S)\), and

\[
S(D(S))=D(S),\qquad S^2\xi=\xi.
\tag{HA.12}
\]

The graph inner product is

\[
\langle \xi,\zeta\rangle_S
=\langle\xi,\zeta\rangle+\langle S\zeta,S\xi\rangle.
\tag{HA.13}
\]

Its completion is \(D(S)\), and every \(\xi\in D(S)\) has \(a_n\in\mathcal A\) with \(a_n\to\xi\) and \(a_n^\sharp\to S\xi\).

For use in the bounded-vector construction, the involution property of \(F\) has a direct proof. If \(\eta\in D(F)\) and \(\zeta=F\eta\), substitute \(S\xi\) for \(\xi\) in (HA.11), using (HA.12):

\[
\langle \xi,\eta\rangle=\langle\zeta,S\xi\rangle.
\]

Conjugating gives \(\langle S\xi,\zeta\rangle=\langle\eta,\xi\rangle\) for every \(\xi\in D(S)\). Hence \(\zeta\in D(F)\) and \(F\zeta=\eta\). Thus

\[
F(D(F))=D(F),\qquad F^2\eta=\eta.
\tag{HA.14}
\]

This argument requires no spectral theorem.

The already-proved polar theorem TC07–10, with its written form and spectral prerequisites, applies to \(S\) and gives

\[
\begin{aligned}
\Delta&=FS,\quad
D(\Delta)=\{\xi\in D(S):S\xi\in D(F)\},\\
S&=J\Delta^{1/2},\quad D(S)=D(\Delta^{1/2}),\\
F&=J\Delta^{-1/2},\quad D(F)=D(\Delta^{-1/2}),\\
J^2&=I,\qquad J\Delta J=\Delta^{-1}.
\end{aligned}
\tag{HA.15}
\]

Here \(\Delta\) is positive self-adjoint and injective, and \(J\) is antiunitary. These identities include equality of the unbounded operator domains. They determine \(\Delta\) and \(J\) uniquely. They define the modular operator and modular conjugation of \(\mathcal A\).

At this stage these names assert no relation between \(J\) and the algebra \(M\). In particular, neither \(JMJ=M'\) nor \(\Delta^{it}M\Delta^{-it}=M\) has been used or proved in this unit.

## A vector that multiplies boundedly from the right

For \(\eta\in H\), consider the linear map

\[
r_\eta:\mathcal A\longrightarrow H,\qquad r_\eta(a)=L_a\eta.
\tag{HA.16}
\]

Call \(\eta\) **right bounded** if this map is bounded for the Hilbert norm on \(\mathcal A\). Write

\[
\mathcal B_r=\{\eta\in H:\exists c<\infty\ \forall a\in\mathcal A,\
\|L_a\eta\|\leq c\|a\|\}.
\tag{HA.17}
\]

For such \(\eta\), let \(R_\eta\in B(H)\) be the unique extension of \(r_\eta\). Its exact norm is

\[
\|R_\eta\|=\sup_{\substack{a\in\mathcal A\\\|a\|\leq1}}\|L_a\eta\|.
\tag{HA.18}
\]

Indeed, the supremum is the norm on the dense domain; taking norm approximations from that domain gives the same bound for the extension.

**Theorem.** The set \(\mathcal B_r\) is a complex vector space. The map \(\eta\mapsto R_\eta\) is linear and injective, and

\[
R_\eta\in M'\quad(\eta\in\mathcal B_r).
\tag{HA.19}
\]

If \(x\in M'\) and \(\eta\in\mathcal B_r\), then

\[
x\eta\in\mathcal B_r,\qquad R_{x\eta}=xR_\eta.
\tag{HA.20}
\]

Consequently \(\mathfrak n_r=\{R_\eta:\eta\in\mathcal B_r\}\) is a left ideal of \(M'\).

**Proof.** Linear combinations satisfy the bound in (HA.17), and uniqueness of extension proves linearity. If \(R_\eta=0\), then \(L_a\eta=0\) for every \(a\); (HA.7) gives \(\eta=0\).

For \(a,b\in\mathcal A\),

\[
R_\eta L_a b=R_\eta(ab)=L_{ab}\eta
=L_aL_b\eta=L_aR_\eta b.
\]

Both operators are bounded, so they commute on all of \(H\). Thus \(R_\eta\in L(\mathcal A)'=M'\).

For \(x\in M'\),

\[
L_a(x\eta)=xL_a\eta=xR_\eta a\qquad(a\in\mathcal A).
\]

The last map is bounded by \(\|x\|\|R_\eta\|\|a\|\), proving (HA.20). The assertion about the left ideal follows from that identity and linearity. It does not assert that \(\mathfrak n_r\) is closed or closed under adjoints. \(\square\)

We now define products for exactly these pairs:

\[
a\xi=L_a\xi\quad(a\in\mathcal A,\ \xi\in H),
\qquad
\xi\eta=R_\eta\xi\quad(\xi\in H,\ \eta\in\mathcal B_r).
\tag{HA.21}
\]

On the overlap \(a\in\mathcal A,\eta\in\mathcal B_r\), the definitions agree by (HA.16). They extend the original product whenever both old and new definitions apply. The commutation in (HA.19) gives the mixed associativity identity

\[
(a\xi)\eta=a(\xi\eta)
\quad(a\in\mathcal A,\ \xi\in H,\ \eta\in\mathcal B_r).
\tag{HA.22}
\]

No product of two arbitrary vectors of \(H\) has been introduced.

## Controlled limits of right-bounded vectors

**Proposition.** Suppose \((\eta_i)\) is a net in \(\mathcal B_r\), \(\eta_i\to\eta\) in Hilbert norm, and \(\sup_i\|R_{\eta_i}\|\leq C<\infty\). Then

\[
\eta\in\mathcal B_r,\qquad
\|R_\eta\|\leq C,\qquad R_{\eta_i}\longrightarrow R_\eta
\text{ strongly}.
\tag{HA.23}
\]

Also \(\mathcal B_r\), with norm

\[
\|\eta\|_{\mathrm{rb}}=\|\eta\|+\|R_\eta\|,
\tag{HA.24}
\]

is a Banach space.

**Proof.** For \(a\in\mathcal A\), boundedness of \(L_a\) gives \(L_a\eta_i\to L_a\eta\), and therefore \(\|L_a\eta\|\leq C\|a\|\). This proves right boundedness and the claimed norm bound. For any \(\xi\in H\) and \(a\in\mathcal A\),

\[
\|(R_{\eta_i}-R_\eta)\xi\|
\leq 2C\|\xi-a\|+\|L_a(\eta_i-\eta)\|.
\]

First approximate \(\xi\) by \(a\), then pass along the net; this proves strong convergence. If \(C=0\), all the operators vanish and injectivity makes every vector zero, so the conclusion also holds.

For completeness, a Cauchy sequence in (HA.24) has limits \(\eta_n\to\eta\) in \(H\) and \(R_{\eta_n}\to T\) in \(B(H)\). For each \(a\in\mathcal A\),

\[
Ta=\lim_nR_{\eta_n}a=\lim_nL_a\eta_n=L_a\eta.
\]

Hence \(\eta\in\mathcal B_r\), \(T=R_\eta\), and convergence holds in (HA.24). The completeness of \(B(H)\) used here follows directly by taking the pointwise limits of an operator-norm Cauchy sequence: the uniform Cauchy bound gives a bounded limit operator and then operator-norm convergence. Thus no closure of \(\mathcal B_r\) in the Hilbert norm was assumed. \(\square\)

The uniform operator bound in (HA.23) cannot be dropped; OA-MOD-HA-10 gives an explicit failure.

## Closed right multipliers and affiliation

For a closed linear operator \(T:D(T)\subseteq H\to H\), affiliation with a von Neumann algebra \(N\) means

\[
uD(T)=D(T),\qquad Tu\xi=uT\xi
\quad(\xi\in D(T),\ u\text{ unitary in }N').
\tag{HA.25}
\]

The following criterion even allows a nondense domain, although our application has a dense one.

**Graph criterion.** Suppose \(\mathcal C\subseteq B(H)\) is a *-subalgebra and

\[
cD(T)\subseteq D(T),\qquad Tc\xi=cT\xi
\quad(c\in\mathcal C,\ \xi\in D(T)).
\tag{HA.26}
\]

Then (HA.26) holds for every \(c\in\mathcal C''\). If \(\mathcal C''=N'\), \(T\) is affiliated with \(N\). In particular this applies whenever \(\mathcal C\subseteq N'\) is ultraweakly dense.

**Proof.** The closed graph \(G(T)\subseteq H\oplus H\) is invariant under \(D(c)=\operatorname{diag}(c,c)\) and under \(D(c)^*\), by *-closure. Its orthogonal projection \(P\) therefore commutes with \(D(c)\). Each of the four bounded matrix entries of \(P\) lies in \(\mathcal C'\). They consequently commute with every \(c\in\mathcal C''\), so \(P\) commutes with \(D(c)\) for those \(c\) too. Thus \(D(c)G(T)\subseteq G(T)\), which is exactly (HA.26).

For a unitary \(u\in N'\), applying that inclusion also to \(u^*\) gives \(uD(T)=D(T)\), proving affiliation. If \(\mathcal C\) is ultraweakly dense in \(N'\), every operator commuting with \(\mathcal C\) commutes with \(N'\): the commutation equation passes through the ultraweak limit because multiplication by a fixed operator is separately ultraweakly continuous by OA-MOD-BK-03. Thus \(\mathcal C'=N\) and \(\mathcal C''=N'\).

Conversely, an affiliated operator satisfies (HA.26) for all of \(N'\). Indeed every element of \(N'\) is a finite linear combination of unitaries by OA-MOD-BK-08, and the domain is a linear space. One may therefore take \(\mathcal C=N'\) in the criterion. \(\square\)

**Theorem.** For every \(\eta\in D(F)\), define linear operators with the same dense domain \(\mathcal A\):

\[
A_\eta^0 a=L_a\eta,\qquad A_{F\eta}^0 a=L_aF\eta.
\tag{HA.27}
\]

Both are closable. Their closures \(A_\eta,A_{F\eta}\) satisfy

\[
A_\eta\subseteq A_{F\eta}^*,\qquad
A_{F\eta}\subseteq A_\eta^*.
\tag{HA.28}
\]

They are affiliated with \(M'\).

**Proof.** For \(a,b\in\mathcal A\), use (HA.11) at \(b^\sharp a\):

\[
\begin{aligned}
\langle L_a\eta,b\rangle
&=\langle\eta,a^\sharp b\rangle\\
&=\langle b^\sharp a,F\eta\rangle\\
&=\langle a,L_bF\eta\rangle.
\end{aligned}
\tag{HA.29}
\]

This proves \(A_\eta^0\subseteq(A_{F\eta}^0)^*\) and \(A_{F\eta}^0\subseteq(A_\eta^0)^*\). In particular both adjoints have the dense test domain \(\mathcal A\). The linear graph lemma proved within OA-MOD-TC-03 gives closability. Adjoint pairings persist under graph closure, and the adjoint of a closable operator equals the adjoint of its closure, proving (HA.28).

For \(a,b\in\mathcal A\), associativity gives

\[
A_\eta^0(L_a b)=L_{ab}\eta=L_aA_\eta^0b.
\]

The domain \(\mathcal A\) is invariant under both \(L_a\) and \(L_a^*=L_{a^\sharp}\). Hence the graph \(G(A_\eta^0)\) is invariant under both corresponding diagonal bounded operators. Its closure \(G(A_\eta)\) retains those invariances. The graph criterion with \(\mathcal C=L(\mathcal A)\) and \(\mathcal C''=M\) proves affiliation with \(M'\). The same argument applies to \(F\eta\in D(F)\), by (HA.14). \(\square\)

The graph proof establishes domain invariance under every \(x\in M\); it does not replace domain invariance with a formal commutation symbol. It also does not turn the inclusions (HA.28) into equalities. That stronger assertion would need a further core argument.

## The right algebra obtained from the adjoint domain

Define

\[
\mathcal A_r=\mathcal B_r\cap D(F).
\tag{HA.30}
\]

This is a vector space, because \(D(F)\) is a complex-linear domain despite conjugate-linearity of \(F\).

**Adjoint theorem.** If \(\eta\in\mathcal A_r\), then

\[
F\eta\in\mathcal B_r,\qquad R_{F\eta}=R_\eta^*.
\tag{HA.31}
\]

Thus \(F\) preserves \(\mathcal A_r\) and is an involution there.

**Proof.** In (HA.29), \(L_a\eta=R_\eta a\). For each fixed \(b\in\mathcal A\), the equality for all \(a\in\mathcal A\) therefore gives

\[
R_\eta^*b=L_bF\eta.
\]

Consequently the map \(b\mapsto L_bF\eta\) is bounded by \(\|R_\eta\|\|b\|\). This proves (HA.31) on the dense domain and hence on \(H\). Equation (HA.14) gives \(F\eta\in D(F)\) and \(F^2\eta=\eta\). \(\square\)

The following pairing gives a useful supply of vectors in \(\mathcal A_r\).

**Product-pairing lemma.** For \(\eta,\zeta\in\mathcal B_r\),

\[
R_\eta^*\zeta\in\mathcal A_r,\qquad
F(R_\eta^*\zeta)=R_\zeta^*\eta.
\tag{HA.32}
\]

**Proof.** Because \(R_\eta^*\in M'\), equation (HA.20) already gives right boundedness of \(R_\eta^*\zeta\). For \(a\in\mathcal A\),

\[
\begin{aligned}
\langle a^\sharp,R_\eta^*\zeta\rangle
&=\langle R_\eta a^\sharp,\zeta\rangle\\
&=\langle L_{a^\sharp}\eta,\zeta\rangle\\
&=\langle\eta,L_a\zeta\rangle\\
&=\langle R_\zeta^*\eta,a\rangle.
\end{aligned}
\tag{HA.33}
\]

The adjoint test for \(s^*=F\) proves the claimed domain membership and value. Equivalently, approximation in the graph of \(S\) extends this pairing from \(\mathcal A\) to every \(a\in D(S)\). The right-hand vector is itself right bounded by (HA.20), consistently with (HA.31). \(\square\)

**Theorem.** For \(\eta,\zeta\in\mathcal A_r\), use the product \(\eta\zeta=R_\zeta\eta\) from (HA.21), and set \(\eta^\flat=F\eta\). This makes \(\mathcal A_r\) an associative involutive algebra, with

\[
\begin{aligned}
R_{\eta\zeta}&=R_\zeta R_\eta,\\
(\eta\zeta)^\flat&=\zeta^\flat\eta^\flat,\\
\langle\eta\zeta,\theta\rangle&=\langle\eta,\theta\zeta^\flat\rangle
\quad(\theta\in\mathcal A_r).
\end{aligned}
\tag{HA.34}
\]

Right multiplication is bounded, and \(\flat\) is closable for the inherited Hilbert norm. These are the first three right Hilbert algebra properties.

**Proof.** By (HA.31), \(R_\zeta=R_{F\zeta}^*\). Apply (HA.32) with \(F\zeta,\eta\in\mathcal B_r\). It proves

\[
R_\zeta\eta\in\mathcal A_r,\qquad
F(R_\zeta\eta)=R_\eta^*F\zeta
=R_{F\eta}F\zeta=(F\zeta)(F\eta).
\]

This supplies the domain of the product involution before asserting its value.

Equation (HA.20), with \(x=R_\zeta\), gives \(R_{\eta\zeta}=R_\zeta R_\eta\). Hence, for \(\theta\in\mathcal A_r\),

\[
(\eta\zeta)\theta=R_\theta R_\zeta\eta
=R_{\zeta\theta}\eta=\eta(\zeta\theta).
\]

The involution reverses products as just proved, is conjugate-linear, and squares to the identity by (HA.14).

The adjoint identity follows from

\[
\langle R_\zeta\eta,\theta\rangle
=\langle\eta,R_\zeta^*\theta\rangle
=\langle\eta,R_{F\zeta}\theta\rangle.
\]

For fixed \(\zeta\), the restriction of \(R_\zeta\) to \(\mathcal A_r\) is bounded. The graph of \(\flat\) is contained in the graph of the closed operator \(F\); a limit with zero first coordinate therefore has zero second coordinate. This proves closability. These arguments also apply in the Hilbert completion \(H_r=\overline{\mathcal A_r}\), since the multiplication and involution preserve \(\mathcal A_r\). \(\square\)

We have not proved that \(\mathcal A_r^2\) is dense in \(H_r\), or that \(H_r=H\). Accordingly this theorem does not yet call \(\mathcal A_r\) a right Hilbert algebra. From the proved identities one may define \(R(\mathcal A_r)''\) in \(B(H)\) and conclude

\[
R(\mathcal A_r)''\subseteq M',
\tag{HA.35}
\]

because \(R(\mathcal A_r)\) is a *-algebra contained in the von Neumann algebra \(M'\). Equality and nondegeneracy remain further assertions.

## A family of nontracial blocks on an arbitrary index set

Let \(I\) be any set and choose \(t_i\in(0,\infty)\) for each \(i\). Put

\[
D_i=\begin{pmatrix}1&0\\0&t_i\end{pmatrix},\qquad
\mathcal A=\bigoplus_{i\in I}^{\mathrm{alg}} M_2(\mathbb C).
\tag{HA.36}
\]

Thus an element of \(\mathcal A\) has only finitely many nonzero matrix blocks. Use componentwise multiplication and matrix adjoint as \(\sharp\), and set

\[
\langle a,b\rangle
=\sum_{i\in I}\operatorname{Tr}(D_i b_i^*a_i).
\tag{HA.37}
\]

Its Hilbert completion is

\[
H=\left\{\eta=(\eta_i):
\sum_{i\in I}\|\eta_iD_i^{1/2}\|_{\mathrm{HS}}^2<\infty\right\}.
\tag{HA.38}
\]

An arbitrary nonnegative sum means the supremum of its finite subsums. Every vector here has countably many nonzero blocks, but there need not be a countable set supporting every vector in \(H\).

Here is a proof of the completion assertion, including arbitrary index sets. The map \(\eta_i\mapsto \eta_iD_i^{1/2}\) identifies each block with four ordinary complex coordinates. The space of such block families with finite square sum is complete: if \(z^{(n)}\) is Cauchy in the sum norm, each coordinate converges to a limit \(z_i\). Given \(\varepsilon>0\), choose \(N\) with \(\|z^{(n)}-z^{(m)}\|\le\varepsilon\) for \(n,m\ge N\). For a finite \(F\subseteq I\), pass to the limit \(m\to\infty\) in the finite sum to obtain

\[
 \sum_{i\in F}\|z_i^{(n)}-z_i\|_{\rm HS}^2
 \le\varepsilon^2\qquad(n\ge N).
\]

The inequality

\[
 \begin{aligned}
 \|z_i\|_{\rm HS}^2
 &\le2\|z_i-z_i^{(N)}\|_{\rm HS}^2\\
 &\quad+2\|z_i^{(N)}\|_{\rm HS}^2
 \end{aligned}
\]

shows, by taking finite-subsum suprema, that \(z\) has finite square sum. The preceding estimate then proves \(\|z^{(n)}-z\|\le\varepsilon\). Completeness of each complex coordinate is the real-number completeness used in BK01.

Finite-support families are dense: a finite subsum within \(\varepsilon^2\) of the full square sum leaves a tail of norm at most \(\varepsilon\). Thus this complete space is exactly the completion of the algebraic direct sum. For every positive integer \(k\), only finitely many blocks can have norm at least \(1/k\), or their finite square sums would be unbounded. Their countable union contains every nonzero block. This proves the countable-support assertion without imposing separability on the full space.

**Verification of the four properties.** Left multiplication by \(a\in\mathcal A\) has norm

\[
\|L_a\|=\max_{i\in I}\|a_i\|_{\mathrm{op}},
\tag{HA.39}
\]

with value zero for \(a=0\). The upper bound follows from
\(\|a_i\eta_iD_i^{1/2}\|_{\mathrm{HS}}\leq
\|a_i\|_{\mathrm{op}}\|\eta_iD_i^{1/2}\|_{\mathrm{HS}}\).
For the reverse bound use one block, write its transformed matrix as \(uv^*\) with unit vectors \(u,v\), and take the supremum over \(u\). The Hilbert–Schmidt norms of \(uv^*\) and \(a_iuv^*\) are \(1\) and \(\|a_i u\|\), respectively, by the finite sums of their squared entries. Thus this supremum is exactly \(\|a_i\|_{\rm op}\), by the definition of the operator norm. The transformation \(\eta_i\mapsto\eta_iD_i^{1/2}\) is a bijective isometry to the usual Hilbert-Schmidt block.

Matrix adjoints give

\[
\operatorname{Tr}(D_i c_i^*a_i b_i)
=\operatorname{Tr}(D_i (a_i^*c_i)^*b_i),
\]

which proves (HA.2). If \(a_n\to0\) and \(a_n^*\to\eta\) in \(H\), continuity of each coordinate map gives \((a_n)_i\to0\) in its finite-dimensional block and therefore \(\eta_i=0\) for every \(i\). This proves closability. Finally every finite-support \(a\) equals \(e_Fa\), where \(e_F\) is the block identity on its finite support \(F\) and zero elsewhere. Thus \(\mathcal A^2=\mathcal A\), proving density of products.

The closure of the involution is exactly

\[
D(S)=\{\eta\in H:(\eta_i^*)_{i\in I}\in H\},
\qquad (S\eta)_i=\eta_i^*.
\tag{HA.40}
\]

One inclusion follows by coordinatewise limits. For the reverse inclusion, finite block truncations converge both for \(\eta\) and its displayed adjoint, by the finite-sum definition in (HA.38). Thus they approximate the claimed graph. This also proves that \(\mathcal A\) is a graph core.

Writing \(d_{i,1}=1,d_{i,2}=t_i\), the adjoint test on matrix units gives

\[
(F\eta)_{i,pq}
=\frac{d_{i,p}}{d_{i,q}}\,\overline{\eta_{i,qp}},
\qquad
D(F)=\left\{\eta\in H:
\left(D_i\eta_i^*D_i^{-1}\right)_{i\in I}\in H\right\}.
\tag{HA.41}
\]

Indeed \(\langle a^*,\eta\rangle=\langle \zeta,a\rangle\) on finite-support matrix units determines exactly those coordinates for \(\zeta\). If the displayed family lies in \(H\), summation over the finite support of \(a\) verifies the adjoint pairing; otherwise no representing vector in \(H\) exists. This proves both necessity and sufficiency of the domain condition.

The right-bounded condition has an equally concrete form:

\[
\eta\in\mathcal B_r
\quad\Longleftrightarrow\quad
\sup_{i\in I}\|D_i^{-1/2}\eta_iD_i^{1/2}\|_{\mathrm{op}}<\infty,
\tag{HA.42}
\]

and this supremum is \(\|R_\eta\|\). To prove it, use the unitary identification \(U\eta=(\eta_iD_i^{1/2})_i\) with a Hilbert direct sum of ordinary Hilbert-Schmidt blocks. For finite-support \(a\),

\[
U(a\eta)_i=(a_iD_i^{1/2})
\left(D_i^{-1/2}\eta_iD_i^{1/2}\right).
\]

Right multiplication by a matrix \(T\) on a Hilbert-Schmidt block has norm \(\|T\|_{\mathrm{op}}\): the upper bound follows by applying the norm estimate to rows. A unit row written as \(u^*\) has image \(u^*T\), whose norm is \(\|T^*u\|\). Taking the supremum over \(u\) gives \(\|T^*\|=\|T\|\) by the bounded-adjoint norm identity in BK01, proving the reverse bound. Testing one block proves necessity in (HA.42); summing the squared block bounds proves sufficiency and the claimed supremum.

For reference, the modular data from (HA.15) have coordinates

\[
(\Delta\eta)_{i,pq}
=\frac{d_{i,p}}{d_{i,q}}\eta_{i,pq},
\qquad
(J\eta)_{i,pq}
=\sqrt{\frac{d_{i,p}}{d_{i,q}}}\,
\overline{\eta_{i,qp}}.
\tag{HA.43}
\]

The domain of \(\Delta\) is the set of \(\eta\in H\) for which its displayed image belongs to \(H\). This domain description agrees with \(D(FS)\): square summability with the squared ratio implies square summability with the ratio by the scalar inequality \(r\leq1+r^2\), which supplies the additional \(S\)-domain condition. Equations (HA.40–41) then give the displayed action of \(FS\). The same argument with square-root ratios gives \(D(\Delta^{1/2})=D(S)\), and \(J\) is an antiunitary involution by exchanging \(p,q\) in the squared norm. Thus (HA.43) also verifies the polar formulas directly in this model.

If \(I\) is uncountable, \(H\) is nonseparable. The family \(e_F\), directed by inclusion of finite subsets \(F\subseteq I\), acts by block truncation, so \(L_{e_F}\to I_H\) strongly. No sequence of these finite-support multipliers converges strongly to the identity: its supports have countable union, and a nonzero vector in a block outside that union is annihilated by the entire sequence. The algebra has no identity vector when \(I\) is infinite. Nontrivial weights \(t_i\neq1\) produce the unequal left and right bounds in (HA.39) and (HA.42).

## Problems and worked solutions

**Problem 1: Hilbert-norm convergence is not enough for right boundedness.** In the block example take \(I=\mathbb N\), \(t_n=n^{-4}\), and

\[
\eta_n=n^{-1}e_{21}
\]

as the \(n\)-th block of a single vector \(\eta\). Show that \(\eta\in H\setminus\mathcal B_r\), although its finite block truncations belong to \(\mathcal A_r\) and converge to \(\eta\) in \(H\).

**Solution.** Since \(e_{21}\) uses the first column, its weighted squared norm is one. Hence \(\|\eta\|^2=\sum_n n^{-2}<\infty\). To justify both convergence and the tail estimate used below, for \(n\ge2\) one has

\[
 \frac1{n^2}\le\frac1{n(n-1)}
 =\frac1{n-1}-\frac1n.
\]

Sum from \(N+1\) to a finite upper endpoint and then take the supremum. The tail is at most \(1/N\); including the first term proves the asserted finite norm. On the other hand

\[
D_n^{-1/2}\eta_nD_n^{1/2}=n e_{21},
\]

whose norms are unbounded. Equation (HA.42) gives \(\eta\notin\mathcal B_r\). Each finite truncation has a finite supremum in (HA.42), and its \(F\)-image has finite support, so it lies in \(\mathcal A_r\). The tail \(\sum_{n>N}n^{-2}\) proves Hilbert-norm convergence. Its right-multiplier norm is \(N\), so the uniform bound required by (HA.23) fails.

**Problem 2: an isometric involution supplies both sides.** Suppose the involution of a left Hilbert algebra satisfies \(\|a^\sharp\|=\|a\|\). Prove that the same algebra is a right Hilbert algebra with the same involution.

**Solution.** The isometry extends to an antiunitary involution \(K:H\to H\). For \(a,b\in\mathcal A\),

\[
K L_{b^\sharp} K a
=(b^\sharp a^\sharp)^\sharp=ab.
\]

Thus right multiplication by \(b\) is bounded, with extension \(K L_{b^\sharp}K\). Its adjoint is \(K L_bK\): this follows by transporting the bounded adjoint pairing through the antiunitary involution. That operator extends right multiplication by \(b^\sharp\). Therefore
\(\langle ab,c\rangle=\langle a,c b^\sharp\rangle\).
The involution is bounded and hence closable, and the product span remains the original dense \(\mathcal A^2\). All four right Hilbert algebra properties follow. No trace or measure representation is needed.

**Problem 3: identify the right-bounded vectors in a unital model.** Assume \(\mathcal A\) has a unit \(e\). Prove

\[
\mathcal B_r=M'e,\qquad R_{xe}=x\quad(x\in M'),
\tag{HA.44}
\]

and the estimate \(\|\eta\|\leq\|e\|\|R_\eta\|\) for \(\eta\in\mathcal B_r\). Show also that \(e\in\mathcal A_r\) and is a two-sided unit for the right algebra \(\mathcal A_r\).

**Solution.** The vector \(e\) is right bounded because \(L_ae=a\), so \(R_e=I\). Equation (HA.20) gives \(xe\in\mathcal B_r\) and \(R_{xe}=x\). Conversely, for \(\eta\in\mathcal B_r\),
\(\eta=L_e\eta=R_\eta e\), proving (HA.44) and the requested estimate. For each \(a\in\mathcal A\), (HA.2) gives
\(\langle a^\sharp,e\rangle=\langle e,a\rangle\).
Thus \(e\in D(s^*)=D(F)\) and \(Fe=e\), so \(e\in\mathcal A_r\). For \(\eta\in\mathcal A_r\), the two products are \(e\eta=R_\eta e=\eta\) and \(\eta e=R_e\eta=\eta\). Hence \(\mathcal A_r^2=\mathcal A_r\) in this unital case. This does not by itself prove that \(\mathcal A_r\) is Hilbert-norm dense in \(H\).

## Exports and the next mathematical obligations

The proved multiplication interface is

\[
\begin{array}{ccc}
\mathcal A\times\mathcal B_r&\longrightarrow&H\\
(a,\eta)&\longmapsto&L_a\eta=R_\eta a,
\end{array}
\tag{HA.45}
\]

with faithful, nondegenerate left representation, faithful right-vector assignment, commuting actions, the ideal covariance (HA.20), the adjoint relation (HA.31), and the closed affiliated operators (HA.27–28). All are valid on arbitrary Hilbert spaces. The explicit graph arguments close the domain claims used in these results.

The following obligations remain distinct:

* Prove that \(\mathcal A_r\) and \(\mathcal A_r^2\) are cores for \(F\), and hence dense in \(H\). This requires additional bounded-vector approximation, beyond (HA.32).
* Prove \(R(\mathcal A_r)''=M'\), including nondegeneracy and the required approximation argument.
* Prove that \(\mathcal A^2\) is a graph core for \(S\), and identify \(\mathfrak n_r\cap\mathfrak n_r^*\) with \(R(\mathcal A_r)\). Hilbert-norm density of finite products proved in OA-MOD-HA-02 does not settle these statements.
* Construct the full left Hilbert algebra by the corresponding left-bounded-vector construction and prove the completion and dualization identities.
* Establish the modular resolvent estimates and the fundamental theorem \(JMJ=M'\), \(\Delta^{it}M\Delta^{-it}=M\), followed by the Tomita algebra of analytic vectors.
* Complete the faithful normal semifinite weight-to-Hilbert-algebra bridge. OA-MOD-WG-009 supplies a dense two-sided finite domain, but closability of its involution and all Hilbert-algebra axioms must be proved before this unit is applied to it. A finite-state model does not close the general-weight obligation.

The elementary kernel above does not claim those conclusions. Its optional polar specialization retains the explicit foundation dependencies of OA-MOD-TC.
