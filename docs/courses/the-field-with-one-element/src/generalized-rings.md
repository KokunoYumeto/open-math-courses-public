# Generalized rings

*Written by Claude Opus 5.5 (Anthropic), September 2026, revised October 2026. The September text was spot-checked by Claude Opus 5.5 in a separate session; the October revision links the AI Integrated Stacks Project citations and is self-checked by the writing AI. Public domain (CC0).*

A commutative ring \(R\) is determined by one monad on sets. The functor of this monad sends a set \(X\) to the set \(R^{(X)}\) of formal \(R\)-linear combinations of elements of \(X\), and its algebras are the \(R\)-modules. The functor alone does not determine \(R\), because it uses only the addition of \(R\); the monad does (Corollary 2.7). [Durov 2007] takes monads of this kind as the definition of a ring-like object. A *generalized ring* is a monad on sets that is *finitary* (its operations have finitely many arguments) and *commutative* (any two of its operations commute). Commutative rings and semirings are generalized rings. So are objects without an addition: the unit ball \(\mathbb Z_\infty\) of the real numbers, the field with one element \(\mathbb F_1\), its extensions \(\mathbb F_{1^n}\), and the initial generalized ring \(\mathbb F_\varnothing\), which has no constant and maps to \(\mathbb F_1\).

The lesson has five parts.

1. Sections 1–3 define finitary monads, their operations and their modules, prove that a finitary monad is the same thing as its system of operations, define commutativity, and check the examples. Theorem 2.6 shows that a generalized ring with an addition is a commutative semiring. So the new objects are exactly those without an addition.
2. Sections 4–6 treat modules, tensor products and localization, and compute \(\mathbb Z\otimes_{\mathbb F_1}\mathbb Z=\mathbb Z\) (Theorem 6.2 and Corollary 6.3). The reason is short: a commutative monad has at most one addition.
3. Section 7 builds the prime spectrum of a generalized ring, its structure sheaf and generalized schemes, and proves that morphisms into an affine generalized scheme are homomorphisms of generalized rings (Theorem 7.9).
4. Section 8 treats the compactification of \(\operatorname{Spec}\mathbb Z\). It is a tower of generalized schemes \(S_N\), each obtained from \(\operatorname{Spec}\mathbb Z\) by adding one point \(\infty\). We prove what the tower is, that its limit is a ringed space but not a generalized scheme (Theorem 8.4), that the tower has no limit among generalized schemes (Theorems 8.8 and 8.9), and that each \(S_N\) is a subobject of the point \(\operatorname{Spec}\mathbb F_{\pm1}\), so that its square over \(\mathbb F_{\pm1}\) is itself (Theorem 8.6). Over \(\mathbb F_1\) this fails (Exercise 10.8). Then we list which further statements of [Durov 2007] are proved there and which are only constructed or asserted.
5. Section 9 states and proves the exact relation to the \(\mathbb F\)-rings of [Haran 2017] (Theorem 9.2).

The lesson assumes monads and their algebras (the definitions are recalled), commutative rings, localization and prime spectra of rings, and sheaves on a topological space. Facts about sheaves and schemes are cited from [Stacks] by tag. Monoids and their spectra are the subject of *Commutative monoids and their spectra*; their schemes are the subject of *Monoid schemes*. The objects that a geometry over \(\mathbb F_1\) is asked to supply are listed in *Weil's proof for curves and what is missing over the integers*.

Conventions. Rings are commutative with \(1\). Semirings are commutative, with \(0\) and \(1\), and \(0\cdot a=0\). A monoid is commutative, written multiplicatively, with a unit \(1\) and an absorbing element \(0\). We write \([n]=\{1,\dots,n\}\) and \([0]=\varnothing\). A tuple \(x=(x_1,\dots,x_n)\in X^n\) is also regarded as the map \(x:[n]\to X\), \(i\mapsto x_i\).

Basic references are [Durov 2007], [Haran 2017] and [López Peña–Lorscheid 2011a].

## 1. Finitary monads and their operations

A reference for this section is [Durov 2007, Chapters 3 and 4].

### Monads and algebras

A *monad* on the category of sets is a functor \(T\) from sets to sets with natural transformations \(\eta:\mathrm{Id}\to T\) and \(\mu:TT\to T\) such that, for every set \(X\),
\[
\mu_X\circ T(\mu_X)=\mu_X\circ\mu_{T(X)},\qquad \mu_X\circ T(\eta_X)=\mathrm{id}_{T(X)}=\mu_X\circ\eta_{T(X)} .
\]
A *\(T\)-algebra* is a set \(X\) with a map \(\alpha:T(X)\to X\) such that \(\alpha\circ\eta_X=\mathrm{id}_X\) and \(\alpha\circ T(\alpha)=\alpha\circ\mu_X\). A *morphism* of \(T\)-algebras \((X,\alpha)\to(Y,\beta)\) is a map \(f:X\to Y\) with \(f\circ\alpha=\beta\circ T(f)\). A *morphism of monads* \(\rho:T\to T'\) is a natural transformation with \(\rho_X\circ\eta_X=\eta'_X\) and \(\rho_X\circ\mu_X=\mu'_X\circ\rho_{T'(X)}\circ T(\rho_X)\) for every \(X\).

We use two facts about monads.

- If a functor \(U\) from a category to sets has a left adjoint \(L\), with unit \(\eta\) and counit \(\varepsilon\), then \(T=UL\) is a monad with unit \(\eta\) and multiplication \(\mu_X=U(\varepsilon_{L(X)})\). The two unit axioms are the two triangle identities of the adjunction. The associativity axiom is \(U\) applied to the naturality of \(\varepsilon\) for the morphism \(\varepsilon_{L(X)}\).
- For a monad \(T\) and a set \(X\), the pair \((T(X),\mu_X)\) is a \(T\)-algebra, by the monad axioms. It is free on \(X\): for every \(T\)-algebra \((M,\alpha)\) and every map \(g:X\to M\), the map \(\alpha\circ T(g)\) is the only morphism of \(T\)-algebras \(h:T(X)\to M\) with \(h\circ\eta_X=g\). Indeed, \(\alpha\circ T(g)\circ\mu_X=\alpha\circ\mu_M\circ TT(g)=\alpha\circ T(\alpha\circ T(g))\), so \(\alpha\circ T(g)\) is a morphism, and \(\alpha\circ T(g)\circ\eta_X=\alpha\circ\eta_M\circ g=g\). If \(h\) is a morphism with \(h\circ\eta_X=g\), then \(h=h\circ\mu_X\circ T(\eta_X)=\alpha\circ T(h)\circ T(\eta_X)=\alpha\circ T(g)\).

The example to keep in mind is the monad of a ring \(R\): \(T_R(X)=R^{(X)}\) is the set of functions \(X\to R\) with finite support, written as formal sums \(\sum_x\lambda_x\{x\}\). The unit sends \(x\) to \(\{x\}\), and \(\mu_X\) evaluates a formal combination of formal combinations. A \(T_R\)-algebra is an \(R\)-module: the map \(\alpha\) evaluates formal linear combinations.

**Definition 1.1.** A monad \(T\) on sets is *finitary* if the functor \(T\) preserves filtered colimits.

[Durov 2007, 4.1.1] calls a finitary monad an *algebraic monad*.

**Lemma 1.2.** Let \(T\) be a finitary monad and \(X\) a set.

(a) Every element of \(T(X)\) has the form \(T(x)(t)\) with \(n\ge0\), \(x\in X^n\) and \(t\in T([n])\).

(b) If \(T(x)(t)=T(x')(t')\) with \(x\in X^n\), \(t\in T([n])\), \(x'\in X^{n'}\), \(t'\in T([n'])\), then there are \(p\ge0\), \(y\in X^p\) and maps \(\varphi:[n]\to[p]\), \(\varphi':[n']\to[p]\) with \(x=y\circ\varphi\), \(x'=y\circ\varphi'\) and \(T(\varphi)(t)=T(\varphi')(t')\).

**Proof.** The set \(X\) is the union of its finite subsets \(F\). This is a filtered colimit, so \(T(X)\) is the colimit of the sets \(T(F)\). A colimit of sets over a directed system is the disjoint union modulo the relation "equal at a later stage". So every element of \(T(X)\) comes from some \(T(F)\), and two elements, from \(T(F)\) and \(T(F')\), have the same image in \(T(X)\) only if they have the same image in \(T(F'')\) for some finite \(F''\supseteq F\cup F'\). For (a), choose a bijection \([n]\to F\). For (b), take \(F\) and \(F'\) to be the images of \(x\) and \(x'\), choose \(F''\) as above and a bijection \(y:[p]\to F''\), and put \(\varphi=y^{-1}\circ x\), \(\varphi'=y^{-1}\circ x'\). Since \(T(y)\) is a bijection from \(T([p])\) to \(T(F'')\), we get \(T(\varphi)(t)=T(\varphi')(t')\). \(\square\)

### Clones and modules

By Lemma 1.2 a finitary monad is controlled by the sets \(T([n])\). We now describe the structure that these sets carry.

**Definition 1.3.** A *clone* \(A\) consists of sets \(A(n)\) for \(n\ge0\), elements \(e^n_i\in A(n)\) for \(1\le i\le n\), and *substitution* maps
\[
A(k)\times A(n)^k\to A(n),\qquad (t;t_1,\dots,t_k)\mapsto t(t_1,\dots,t_k),
\]
for all \(k,n\ge0\), such that for all \(t\in A(k)\), \(t_1,\dots,t_k\in A(n)\) and \(s_1,\dots,s_n\in A(m)\):

- (C1) \(e^k_i(t_1,\dots,t_k)=t_i\);
- (C2) \(t(e^k_1,\dots,e^k_k)=t\);
- (C3) \(\bigl(t(t_1,\dots,t_k)\bigr)(s_1,\dots,s_n)=t\bigl(t_1(s_1,\dots,s_n),\dots,t_k(s_1,\dots,s_n)\bigr)\).

The elements of \(A(n)\) are the *\(n\)-ary operations* of \(A\), and the elements of \(A(0)\) are its *constants*. A *homomorphism* of clones \(\rho:A\to B\) is a family of maps \(\rho_n:A(n)\to B(n)\) that preserves the elements \(e^n_i\) and substitution. A *subclone* of \(A\) is a family of subsets \(B(n)\subseteq A(n)\) that contains all \(e^n_i\) and is closed under substitution. A set \(G\) of operations *generates* \(A\) if the only subclone containing \(G\) is \(A\).

We write \(|A|=A(1)\) and \(e=e^1_1\). By (C1)–(C3) the product \(uv=u(v)\) on \(|A|\) is associative with unit \(e\). So \(|A|\) is a monoid in the general sense: it need not be commutative and need not have an absorbing element. For a generalized ring with zero it will be a monoid in the sense of our conventions (Proposition 2.5). A constant \(c\in A(0)\) gives the element \(c()\in A(n)\) for every \(n\) (substitution with \(k=0\)); we denote it again by \(c\). For a map \(\varphi:[k]\to[n]\) and \(t\in A(k)\) we put
\[
\varphi_*t=t(e^n_{\varphi(1)},\dots,e^n_{\varphi(k)})\in A(n).
\]
This operation renames, repeats or adds dummy variables.

[Durov 2007, 4.3] describes an algebraic monad by equivalent data (the sets \(A(n)\), the maps \(\varphi_*\), the substitution maps and the element \(e\)) and calls this the naive description; the conditions are written out in [Durov 2007, 4.3.1–4.3.3].

**Definition 1.4.** Let \(A\) be a clone. An *\(A\)-module* is a set \(M\) with maps \([t]_M:M^n\to M\) for all \(n\ge0\) and \(t\in A(n)\), such that

- (M1) \([e^n_i]_M(x_1,\dots,x_n)=x_i\);
- (M2) \([t(t_1,\dots,t_k)]_M(x)=[t]_M\bigl([t_1]_M(x),\dots,[t_k]_M(x)\bigr)\) for \(t\in A(k)\), \(t_i\in A(n)\), \(x\in M^n\).

We write \(t(x_1,\dots,x_n)\) for \([t]_M(x_1,\dots,x_n)\), and \(ux\) for \([u]_M(x)\) when \(u\in|A|\). A *homomorphism* of \(A\)-modules is a map \(f\) with \(f(t(x_1,\dots,x_n))=t(f(x_1),\dots,f(x_n))\) for all \(t\). The category of \(A\)-modules is denoted \(A\text{-}\mathrm{Mod}\).

Two consequences of (M1) and (M2): the monoid \(|A|\) acts on every module, and for \(\varphi:[k]\to[n]\), \(t\in A(k)\) and \(x\in M^n\)
\[
(\varphi_*t)(x_1,\dots,x_n)=t(x_{\varphi(1)},\dots,x_{\varphi(k)}).\tag{1.1}
\]
A module over a clone with a constant \(c\) is not empty: it contains the value of \(c\).

**Lemma 1.5.** The set \(A(n)\) is an \(A\)-module under substitution. It is free on \(e^n_1,\dots,e^n_n\): for every \(A\)-module \(M\) and every \(x\in M^n\) there is exactly one homomorphism \(f:A(n)\to M\) with \(f(e^n_i)=x_i\), namely \(f(t)=t(x_1,\dots,x_n)\).

**Proof.** (M1) and (M2) for \(A(n)\) are (C1) and (C3). The map \(t\mapsto t(x_1,\dots,x_n)\) is a homomorphism by (M2) and sends \(e^n_i\) to \(x_i\) by (M1). If \(f\) is a homomorphism with \(f(e^n_i)=x_i\), then by (C2) \(f(t)=f(t(e^n_1,\dots,e^n_n))=t(x_1,\dots,x_n)\). \(\square\)

**Example 1.6.** (a) *Semirings.* Let \(R\) be a semiring; for this example it need not be commutative. Put \(T_R(n)=R^n\), let \(e^n_i\) be the standard basis vectors, and define
\[
\lambda(\mu^1,\dots,\mu^k)=\sum_{i=1}^k\lambda_i\mu^i\qquad(\lambda\in R^k,\ \mu^i\in R^n).
\]
(C1)–(C3) are the rules for linear combinations, so \(T_R\) is a clone. An *\(R\)-semimodule* is a commutative monoid \((M,+,0)\) with a map \(R\times M\to M\) such that \(r(x+y)=rx+ry\), \((r+s)x=rx+sx\), \((rs)x=r(sx)\), \(1x=x\), \(0x=0\) and \(r0=0\); for a ring \(R\) these are the \(R\)-modules. A \(T_R\)-module is the same thing as an \(R\)-semimodule. Indeed, in a \(T_R\)-module put \(0=[()]_M\), \(x+y=(1,1)(x,y)\) and \(rx=(r)(x)\). Each semimodule axiom is (M2) applied to an identity in \(T_R\); for example \((1,1)\bigl((1,1,0),(0,0,1)\bigr)=(1,1,1)=(1,1)\bigl((1,0,0),(0,1,1)\bigr)\) gives \((x+y)+z=x+(y+z)\). Since \(\lambda\) is obtained by substitution from \((1,1)\), the \((\lambda_i)\) and the \(e^n_i\), we get \([\lambda]_M(x)=\sum_i\lambda_ix_i\). Conversely, in a semimodule the maps \([\lambda]_M(x)=\sum_i\lambda_ix_i\) satisfy (M1) and (M2).

(b) *The clone of all operations on a set.* For a set \(X\) let \(\mathrm{END}(X)(n)\) be the set of all maps \(X^n\to X\), let \(e^n_i\) be the projections, and let substitution be composition: \(t(t_1,\dots,t_k)(x)=t(t_1(x),\dots,t_k(x))\). By (M1) and (M2), an \(A\)-module structure on \(X\) is the same thing as a homomorphism of clones \(A\to\mathrm{END}(X)\).

### The dictionary

**Proposition 1.7.** Let \((T,\eta,\mu)\) be a monad on sets. Put \(A_T(n)=T([n])\) and \(e^n_i=\eta_{[n]}(i)\). For \(t\in A_T(k)\) and \(t_1,\dots,t_k\in A_T(n)\) put
\[
t(t_1,\dots,t_k)=\mu_{[n]}\bigl(T(\tau)(t)\bigr),\qquad\text{where }\tau:[k]\to T([n]),\ \tau(i)=t_i .
\]

(a) \(A_T\) is a clone, and \(\varphi_*=T(\varphi)\) for every map \(\varphi:[k]\to[n]\).

(b) Every \(T\)-algebra \((X,\alpha)\) is an \(A_T\)-module under \([t]_X(x)=\alpha\bigl(T(x)(t)\bigr)\) for \(t\in A_T(n)\), \(x\in X^n\). Morphisms of \(T\)-algebras are homomorphisms of \(A_T\)-modules.

(c) If \(T\) is finitary, then (b) is a bijection between the \(T\)-algebra structures and the \(A_T\)-module structures on a set, and a map between \(T\)-algebras is a morphism if and only if it is a homomorphism of \(A_T\)-modules.

**Proof.** We write \(\mu_n=\mu_{[n]}\) and \(\eta_n=\eta_{[n]}\).

(a) (C1): by naturality of \(\eta\), \(T(\tau)(\eta_k(i))=\eta_{T([n])}(\tau(i))\), and \(\mu_n\circ\eta_{T([n])}=\mathrm{id}\). (C2): here \(\tau=\eta_k\), and \(\mu_k\circ T(\eta_k)=\mathrm{id}\). (C3): let \(\sigma:[n]\to T([m])\), \(\sigma(j)=s_j\). The left side of (C3) is \(\mu_mT(\sigma)\mu_nT(\tau)(t)\). Naturality of \(\mu\) gives \(T(\sigma)\circ\mu_n=\mu_{T([m])}\circ TT(\sigma)\), and associativity gives \(\mu_m\circ\mu_{T([m])}=\mu_m\circ T(\mu_m)\). So the left side is \(\mu_mT(\mu_m\circ T(\sigma)\circ\tau)(t)\), and \((\mu_m\circ T(\sigma)\circ\tau)(i)=t_i(s_1,\dots,s_n)\). This is the right side. Finally \(\varphi_*t=\mu_nT(\eta_n\circ\varphi)(t)=\mu_nT(\eta_n)T(\varphi)(t)=T(\varphi)(t)\).

(b) (M1): \(\alpha(T(x)(\eta_n(i)))=\alpha(\eta_X(x_i))=x_i\). (M2): \(\alpha\,T(x)\,\mu_n\,T(\tau)(t)=\alpha\,\mu_X\,T(T(x)\circ\tau)(t)=\alpha\,T(\alpha\circ T(x)\circ\tau)(t)\), and \((\alpha\circ T(x)\circ\tau)(i)=[t_i]_X(x)\). For a morphism \(f\): \(f(\alpha(T(x)(t)))=\beta(T(f)T(x)(t))=\beta(T(f\circ x)(t))\).

(c) Let maps \([t]_X\) with (M1) and (M2) be given. Define \(\alpha:T(X)\to X\) by \(\alpha(T(x)(t))=[t]_X(x)\). By Lemma 1.2(a) this covers \(T(X)\). It is well defined: in the situation of Lemma 1.2(b), formula (1.1) and \(\varphi_*=T(\varphi)\) give
\[
[t]_X(x)=[t]_X(y\circ\varphi)=[\varphi_*t]_X(y)=[\varphi'_*t']_X(y)=[t']_X(x').
\]
We have \(\alpha\circ\eta_X=\mathrm{id}\), because \(\eta_X(x)=T(\tilde x)(e)\) for the map \(\tilde x:[1]\to X\) with value \(x\), and \([e]_X=\mathrm{id}\). For \(\alpha\circ T(\alpha)=\alpha\circ\mu_X\), let \(\Xi\in T(T(X))\). By Lemma 1.2(a), \(\Xi=T(\xi)(t)\) with \(\xi:[k]\to T(X)\) and \(t\in T([k])\), and each \(\xi(i)\) has the form \(T(x)(t_i)\) with \(t_i\in T([n])\) and one tuple \(x\in X^n\) that enumerates a finite subset large enough for all \(i\). So \(\xi=T(x)\circ\tau\) with \(\tau(i)=t_i\). Then
\[
\mu_X(\Xi)=\mu_X\,TT(x)\,T(\tau)(t)=T(x)\,\mu_n\,T(\tau)(t)=T(x)\bigl(t(t_1,\dots,t_k)\bigr),
\]
so \(\alpha(\mu_X(\Xi))=[t(t_1,\dots,t_k)]_X(x)\). On the other hand \(T(\alpha)(\Xi)=T(\alpha\circ\xi)(t)\), so \(\alpha(T(\alpha)(\Xi))=[t]_X([t_1]_X(x),\dots,[t_k]_X(x))\). The two agree by (M2). The two constructions are inverse to each other by Lemma 1.2(a). If \(f:X\to Y\) is a homomorphism of \(A_T\)-modules, then \(f(\alpha(T(x)(t)))=[t]_Y(f\circ x)=\beta(T(f)(T(x)(t)))\), so \(f\circ\alpha=\beta\circ T(f)\) by Lemma 1.2(a). \(\square\)

**Theorem 1.8.** (a) Let \(A\) be a clone. The forgetful functor from \(A\)-modules to sets has a left adjoint \(X\mapsto A(X)\). The monad \(T_A\) of this adjunction is finitary, and its clone is \(A\): \(T_A([n])=A(n)\), with the same elements \(e^n_i\) and the same substitution.

(b) For every finitary monad \(T\), the monads \(T\) and \(T_{A_T}\) are isomorphic.

(c) For finitary monads \(T\) and \(T'\), restriction to the sets \([n]\) is a bijection from the morphisms of monads \(T\to T'\) to the homomorphisms of clones \(A_T\to A_{T'}\).

So \(T\mapsto A_T\) is an equivalence between the category of finitary monads on sets and the category of clones, and it identifies \(T\)-algebras with \(A_T\)-modules.

**Proof.** (a) *Filtered colimits of modules.* Let \((M_i)\) be a filtered diagram of \(A\)-modules and \(M\) its colimit as a set. For \(t\in A(n)\) and \(z\in M^n\) there is an index \(i\) such that all \(z_j\) come from elements \(\tilde z_j\in M_i\). Define \(t(z)\) as the image of \(t(\tilde z)\). Two choices become equal at a later index, because the transition maps are homomorphisms; so this is well defined. (M1) and (M2) hold in \(M\) because they hold in each \(M_i\). With this structure \(M\) is the colimit in \(A\text{-}\mathrm{Mod}\). So the forgetful functor \(U\) preserves filtered colimits.

*Free modules.* Let \(X\) be a set. For every finite subset \(F\subseteq X\) fix a bijection \(b_F:[n]\to F\); if \(X=[m]\), take \(b_{[m]}=\mathrm{id}\). Let \(A(F)\) be the module \(A(n)\), and write \(\{f\}=e^n_i\) for \(f=b_F(i)\). By Lemma 1.5, homomorphisms \(A(F)\to M\) correspond to maps \(F\to M\). For \(F\subseteq F'\) let \(A(F)\to A(F')\) be the homomorphism with \(\{f\}\mapsto\{f\}\). By uniqueness these maps compose correctly. Let \(A(X)\) be the colimit of the modules \(A(F)\) over the finite subsets \(F\subseteq X\). Homomorphisms \(A(X)\to M\) are compatible families of homomorphisms \(A(F)\to M\), that is, compatible families of maps \(F\to M\), that is, maps \(X\to M\). So \(A(X)\), with the map \(x\mapsto\{x\}\), is a free module on \(X\), and \(X\mapsto A(X)\) is left adjoint to \(U\). For \(X=[m]\) the colimit is \(A(m)\).

*The monad.* \(T_A(X)\) is the underlying set of \(A(X)\). A left adjoint preserves all colimits and \(U\) preserves filtered colimits, so \(T_A\) is finitary. We have \(T_A([n])=A(n)\) and \(\eta_{[n]}(i)=e^n_i\). For \(t\in A(k)\) and \(t_1,\dots,t_k\in A(n)\), the map \(T_A(\tau)\) is the homomorphism \(A(k)\to A(A(n))\) with \(e^k_i\mapsto\{t_i\}\), and \(\mu_{[n]}\) is the homomorphism \(A(A(n))\to A(n)\) with \(\{s\}\mapsto s\). Their composite is the homomorphism \(A(k)\to A(n)\) with \(e^k_i\mapsto t_i\). By Lemma 1.5 it sends \(t\) to \(t(t_1,\dots,t_k)\). So the substitution of \(A_{T_A}\) is that of \(A\).

(b) Put \(A=A_T\). By Proposition 1.7(c), \(T\)-algebras and \(A\)-modules are the same. So \((T(X),\mu_X)\) with \(\eta_X\), and \(A(X)\) with \(x\mapsto\{x\}\), are both free \(A\)-modules on \(X\). Let \(\theta_X:A(X)\to T(X)\) be the homomorphism with \(\{x\}\mapsto\eta_X(x)\). It is bijective and natural in \(X\), and compatible with the units. It is compatible with the multiplications: \(\theta_X\circ\mu^A_X\) and \(\mu_X\circ\theta_{T(X)}\circ A(\theta_X)\) are homomorphisms \(A(A(X))\to T(X)\), and both send a generator \(\{a\}\), \(a\in A(X)\), to \(\theta_X(a)\).

(c) Let \(\rho:T\to T'\) be a morphism of monads. Then \(\rho_{[n]}(e^n_i)=e^n_i\), and with \(\tau\) as in Proposition 1.7,
\[
\rho_{[n]}\bigl(\mu_nT(\tau)(t)\bigr)=\mu'_n\,\rho_{T'([n])}\,T(\rho_{[n]}\circ\tau)(t)=\mu'_n\,T'(\rho_{[n]}\circ\tau)\bigl(\rho_{[k]}(t)\bigr),
\]
by naturality of \(\rho\). So \((\rho_{[n]})_n\) is a homomorphism of clones. It determines \(\rho\), because \(\rho_X(T(x)(t))=T'(x)(\rho_{[n]}(t))\) and by Lemma 1.2(a). Conversely, by (b) we may take \(T=T_A\) and \(T'=T_{A'}\). Let \(\rho:A\to A'\) be a homomorphism of clones. Every \(A'\)-module is an \(A\)-module through \(\rho\). Let \(\rho_X:A(X)\to A'(X)\) be the homomorphism of \(A\)-modules with \(\{x\}\mapsto\{x\}\). It is natural in \(X\) and compatible with the units, and \(\rho_{[n]}=\rho_n\) by Lemma 1.5. The maps \(\rho_X\circ\mu_X\) and \(\mu'_X\circ\rho_{T'(X)}\circ T(\rho_X)\) are homomorphisms of \(A\)-modules \(A(A(X))\to A'(X)\), and both send \(\{a\}\) to \(\rho_X(a)\). So \(\rho\) is a morphism of monads. \(\square\)

*Reference:* [Durov 2007, 4.1.3 and 4.3.1–4.3.3].

From now on we do not distinguish between a finitary monad and its clone. For a clone \(A\) and a set \(X\), \(A(X)\) is the free \(A\)-module on \(X\); by Lemma 1.2(a) each of its elements is \(t(\{x_1\},\dots,\{x_n\})\) for some \(t\in A(n)\) and \(x_i\in X\). For the semiring clone \(T_R\) of Example 1.6(a) the free module is \(R^{(X)}\), so \(T_R\) is the monad described before Definition 1.1.

## 2. Commutativity and generalized rings

A reference for this section is [Durov 2007, 5.1].

**Definition 2.1.** Let \(A\) be a clone, \(t\in A(n)\) and \(s\in A(m)\). We say that \(t\) and \(s\) *commute* if for every \(A\)-module \(M\) and every \(n\times m\) matrix \((x_{ij})\) with entries in \(M\)
\[
t\bigl(s(x_{11},\dots,x_{1m}),\dots,s(x_{n1},\dots,x_{nm})\bigr)=s\bigl(t(x_{11},\dots,x_{n1}),\dots,t(x_{1m},\dots,x_{nm})\bigr).\tag{2.1}
\]
In words: applying \(s\) to the rows and then \(t\) gives the same result as applying \(t\) to the columns and then \(s\). The clone \(A\) is *commutative* if any two of its operations commute; this includes each operation with itself.

The relation is symmetric. It suffices to test (2.1) in the free module \(A(nm)\) on the matrix of the generators \(e^{nm}_{(i-1)m+j}\): by Lemma 1.5 every matrix in a module \(M\) is the image of this one under a homomorphism. So "\(t\) and \(s\) commute" is one identity between two elements of \(A(nm)\). Therefore homomorphisms of clones preserve commutation, and two operations of a subclone \(B\subseteq A\) commute in \(B\) if and only if they commute in \(A\).

**Lemma 2.2.** Let \(A\) be a clone.

(a) For every operation \(t\), the set \(C(t)\) of operations that commute with \(t\) is a subclone of \(A\).

(b) If a set \(G\) generates \(A\) and any two elements of \(G\) commute (each with itself included), then \(A\) is commutative.

**Proof.** (a) Let \(t\in A(n)\). For a module \(M\), let \(M^n\) be the product module, with operations computed in each coordinate. Read the columns of the matrix in (2.1) as elements of \(M^n\). Then (2.1) says that the map \([t]_M:M^n\to M\) satisfies \([t]_M(s(z_1,\dots,z_m))=s([t]_M(z_1),\dots,[t]_M(z_m))\) for all \(z_j\in M^n\); we say that \([t]_M\) *respects* \(s\). For any map \(g\) between two modules, the operations respected by \(g\) contain all \(e^m_i\) and are closed under substitution: if \(g\) respects \(s,s_1,\dots,s_m\), then \(g(s(s_1(z),\dots,s_m(z)))=s(g(s_1(z)),\dots)=s(s_1(g(z)),\dots,s_m(g(z)))\), where \(g(z)\) is computed entry by entry. So \(C(t)\) is a subclone.

(b) For \(g\in G\) the subclone \(C(g)\) contains \(G\), so \(C(g)=A\). Thus every operation \(t\) commutes with every \(g\in G\). So \(C(t)\) contains \(G\), and \(C(t)=A\). \(\square\)

**Proposition 2.3.** For a clone \(A\) the following are equivalent.

(i) \(A\) is commutative.

(ii) For every \(A\)-module \(M\) and every \(t\in A(n)\), the map \([t]_M:M^n\to M\) is a homomorphism of \(A\)-modules.

(iii) For all \(A\)-modules \(M\) and \(N\), the set \(\operatorname{Hom}_A(M,N)\) is a submodule of the product module \(N^M\) of all maps \(M\to N\).

**Proof.** (i) and (ii) are equivalent by the proof of Lemma 2.2(a). Assume (ii) and let \(f_1,\dots,f_n\in\operatorname{Hom}_A(M,N)\). Then \(t(f_1,\dots,f_n)\), computed in \(N^M\), is the composite of the homomorphism \(M\to N^n\), \(x\mapsto(f_i(x))_i\), with the homomorphism \([t]_N\). So it is a homomorphism; this is (iii). Assume (iii) and take \(M=N^n\) and the projections \(f_i=\mathrm{pr}_i\), which are homomorphisms. Then \(t(\mathrm{pr}_1,\dots,\mathrm{pr}_n)=[t]_N\) is a homomorphism; this is (ii). \(\square\)

So commutativity is what makes the set of homomorphisms between two modules a module again, as for commutative rings.

**Definition 2.4.** A *generalized ring* is a commutative finitary monad on sets; equivalently (Theorem 1.8), a commutative clone. A *homomorphism* of generalized rings is a homomorphism of clones. A generalized ring *with zero* is one that has a constant.

*Reference:* [Durov 2007, 5.1.1 and 5.1.6].

**Proposition 2.5.** Let \(A\) be a generalized ring.

(a) \(A\) has at most one constant. If it has one, we write \(0\) for it, for its image in each \(A(n)\), and for its value in each module.

(b) The monoid \(|A|\) is commutative. If \(A\) has a zero, then \(0\in|A|\) is absorbing, so \(|A|\) is a monoid in the sense of our conventions.

(c) For every module \(M\), every \(u\in|A|\) and every \(t\in A(n)\): \(u\,t(x_1,\dots,x_n)=t(ux_1,\dots,ux_n)\), and \(t(0,\dots,0)=0\) if \(A\) has a zero.

**Proof.** These are instances of (2.1). For two constants \(c,c'\) the matrix is empty and (2.1) reads \(c=c'\). For \(u,v\in|A|\) it reads \(u(v(x))=v(u(x))\). For \(u\in|A|\) and \(t\in A(n)\), with an \(n\times1\) matrix, it reads \(t(ux_1,\dots,ux_n)=u\,t(x_1,\dots,x_n)\). For \(t\in A(n)\) and the constant, with an \(n\times0\) matrix, it reads \(t(0,\dots,0)=0\); for \(n=1\) this is \(u\cdot0=0\). Finally \(0\cdot u=0\) by (C3), since \(0\) is a constant. \(\square\)

### Generalized rings with an addition

**Theorem 2.6.** Let \(A\) be a generalized ring with zero. Suppose that \(p\in A(2)\) satisfies \(p(e,0)=e=p(0,e)\) in \(A(1)\). Write \(x+y=p(x,y)\) in every module.

(a) \(p\) is the only binary operation with this property. In every module, \(+\) is commutative and associative, with neutral element \(0\).

(b) For \(t\in A(n)\) put \(\lambda_i(t)=t(0,\dots,0,e,0,\dots,0)\in|A|\), with \(e\) in place \(i\). Then \(t=\lambda_1(t)e^n_1+\dots+\lambda_n(t)e^n_n\), and \(t\mapsto(\lambda_i(t))_i\) is a bijection \(A(n)\to|A|^n\).

(c) With this addition and its product, \(|A|\) is a commutative semiring \(R\), and the bijections of (b) form an isomorphism \(A\cong T_R\). The semiring \(R\) is a ring if and only if there is \(u\in|A|\) with \(e+u=0\).

**Proof.** By (M2), \(x+0=x=0+x\) in every module.

(a) Let \(q\in A(2)\) have the same property. Apply (2.1) to \(q\), \(p\) and the matrix with rows \((x,0)\) and \((0,y)\). Applying \(p\) to the rows gives \(x\) and \(y\). Applying \(q\) to the columns gives \(x\) and \(y\). So \(q(x,y)=p(x,y)\); with \(x=e^2_1\), \(y=e^2_2\) in \(A(2)\) this is \(q=p\). This is the Eckmann–Hilton argument. For \(q(x,y)=p(y,x)\) it gives \(x+y=y+x\). Now apply (2.1) to \(p\), \(p\) and the matrix with rows \((x,y)\) and \((0,z)\): \((x+y)+z=(x+0)+(y+z)=x+(y+z)\).

(b) Let \(\sigma_n=e^n_1+\dots+e^n_n\in A(n)\). Apply (2.1) to \(t\) and \(\sigma_n\) and the \(n\times n\) matrix in \(A(n)\) with \(x_{ii}=e^n_i\) and \(x_{ij}=0\) for \(i\ne j\). Applying \(\sigma_n\) to row \(i\) gives \(e^n_i\), so the left side is \(t(e^n_1,\dots,e^n_n)=t\). Applying \(t\) to column \(j\) gives \(t(0,\dots,e^n_j,\dots,0)=\lambda_j(t)e^n_j\) by (C3). So \(t=\sum_j\lambda_j(t)e^n_j\), and the map is injective. It is surjective: for \(u_1,\dots,u_n\in|A|\) the operation \(t=\sum_iu_ie^n_i\) has \(\lambda_j(t)=u_j\), because \(u_i0=0\) by Proposition 2.5.

(c) By (a), applied to the module \(A(1)\), \((|A|,+,0)\) is a commutative monoid. By Proposition 2.5 the product is commutative and associative with unit \(e\), and \(0\) is absorbing. Distributivity \(u(v+w)=uv+uw\) is Proposition 2.5(c) for \(t=p\). So \(R=|A|\) is a semiring. The bijection of (b) sends \(e^n_i\) to the \(i\)-th basis vector. For \(t\in A(k)\) and \(t_i\in A(n)\), (C3), (b) and distributivity in the module \(A(n)\) give
\[
t(t_1,\dots,t_k)=\sum_i\lambda_i(t)\,t_i=\sum_j\Bigl(\sum_i\lambda_i(t)\lambda_j(t_i)\Bigr)e^n_j ,
\]
which is the substitution of \(T_R\). If \(e+u=0\), then \(v+uv=(e+u)v=0\) for every \(v\), so \(R\) is a ring. The converse is clear. \(\square\)

*Reference:* [Durov 2007, 5.1.8].

**Corollary 2.7.** (a) For semirings \(R\) and \(R'\), the homomorphisms of generalized rings \(T_R\to T_{R'}\) are exactly the maps \(\lambda\mapsto(\varphi(\lambda_i))_i\) for semiring homomorphisms \(\varphi:R\to R'\). So \(R\mapsto T_R\) is a fully faithful functor from semirings to generalized rings.

(b) Let \(R\) be a semiring, \(A\) a generalized ring and \(\rho:T_R\to A\) a homomorphism. Then \(A\) has a zero and an addition. So \(A\cong T_{R'}\) with \(R'=|A|\), and \(\rho\) comes from the semiring homomorphism \(\rho_1:R\to R'\). If \(R\) is a ring, then \(R'\) is a ring.

**Proof.** (b) \(\rho(0)\) is a constant of \(A\). For \(p=(1,1)\in T_R(2)\) we have \(p(e,0)=e=p(0,e)\), so \(\rho(p)\) satisfies the hypothesis of Theorem 2.6. The map \(\rho_1\) preserves products, \(e\) and \(0\), and \(\rho_1(a+b)=\rho(p(a,b))=\rho(p)(\rho_1a,\rho_1b)=\rho_1a+\rho_1b\). Also \(\rho_n(\lambda)=\rho_n(\sum_i\lambda_ie^n_i)=\sum_i\rho_1(\lambda_i)e^n_i\). If \(R\) is a ring, then \(u=\rho_1(-1)\) satisfies \(e+u=0\). (a) follows from (b), and conversely every semiring homomorphism induces a homomorphism of clones. \(\square\)

In particular, a generalized ring that receives a homomorphism from \(T_{\mathbb Z}\) is a commutative ring. So a generalized ring that is not a ring receives no homomorphism from \(T_{\mathbb Z}\). From now on we write \(R\) for \(T_R\) when no confusion can arise.

## 3. Examples

Each example comes with its commutativity check. References are [Durov 2007, 3.4.12 and 5.1.16] and, for monoids, [López Peña–Lorscheid 2011a, §2.5].

**Example 3.1** (Semirings and rings). For a semiring \(R\) that is not assumed commutative, let \(\lambda\in R^n\), \(\nu\in R^m\) and let \((x_{ij})\) be a matrix in a semimodule. The two sides of (2.1) are \(\sum_{i,j}\lambda_i\nu_jx_{ij}\) and \(\sum_{i,j}\nu_j\lambda_ix_{ij}\). They agree if \(R\) is commutative. Conversely, if \(T_R\) is commutative, then \(|T_R|=(R,\cdot)\) is commutative by Proposition 2.5. So \(T_R\) is a generalized ring exactly when \(R\) is commutative. It has a zero and an addition. By Theorem 2.6 and Corollary 2.7, commutative semirings are exactly the generalized rings with zero and addition, and commutative rings are those in which \(e\) has a negative. Examples are \(\mathbb Z\), \(\mathbb Q\), \(\mathbb R\), the semiring \(\mathbb N\) of natural numbers, and the Boolean semiring \(\mathbb B=\{0,1\}\) with \(1+1=1\).

**Example 3.2** (The unit ball \(\mathbb Z_\infty\)). A subclone of a commutative clone is commutative, because commutation is an identity in \(A(nm)\). Inside \(T_{\mathbb R}\) let
\[
\mathbb Z_\infty(n)=\Bigl\{\lambda\in\mathbb R^n:\ \sum_i|\lambda_i|\le1\Bigr\}.
\]
This is a subclone: it contains the basis vectors, and for \(\lambda\in\mathbb Z_\infty(k)\) and \(\mu^i\in\mathbb Z_\infty(n)\)
\[
\sum_j\Bigl|\sum_i\lambda_i\mu^i_j\Bigr|\le\sum_i|\lambda_i|\sum_j|\mu^i_j|\le1 .
\]
So \(\mathbb Z_\infty\) is a generalized ring with zero. Its monad sends \(X\) to the unit ball of the \(\ell^1\) norm on \(\mathbb R^{(X)}\); for non-empty \(X\) this is the convex hull of the vectors \(\pm\{x\}\). The monoid \(|\mathbb Z_\infty|\) is \([-1,1]\). Every subset \(K\) of a real vector space that contains \(\sum_i\lambda_ix_i\) whenever \(x_i\in K\) and \(\sum_i|\lambda_i|\le1\) is a \(\mathbb Z_\infty\)-module; the unit ball of a seminorm is an example. There is no addition: an operation \(p=(a,b)\) with \(p(e,0)=e=p(0,e)\) has \(a=b=1\), and \(|a|+|b|=2\). So \(\mathbb Z_\infty\) is not a semiring. The map \(t\mapsto(\lambda_1(t),\lambda_2(t))\) of Theorem 2.6(b) is defined for every generalized ring with zero. For \(\mathbb Z_\infty\) it is the inclusion of the diamond \(\mathbb Z_\infty(2)\) in the square \([-1,1]^2\): injective, not surjective.

Intersections of subclones are subclones. We will use
\[
\mathbb Z_{(\infty)}=\mathbb Z_\infty\cap T_{\mathbb Q},\qquad A_N=\mathbb Z_{(\infty)}\cap T_{\mathbb Z[1/N]}\quad(N\ge1),\qquad\mathbb F_{\pm1}=A_1=\mathbb Z_\infty\cap T_{\mathbb Z}.
\]
So \(A_N(n)\) is the set of \(\lambda\in\mathbb Z[1/N]^n\) with \(\sum_i|\lambda_i|\le1\), and \(\mathbb F_{\pm1}(n)=\{0,\pm e^n_1,\dots,\pm e^n_n\}\).

**Example 3.3** (A module that is not a convex set). Let \(Q=\{-1,0,1\}\). For \(\lambda\in\mathbb Z_\infty(n)\) and \(x\in Q^n\) let \([\lambda]_Q(x)\) be the real number \(\sum_i\lambda_ix_i\) if it equals \(\pm1\), and \(0\) otherwise. This is a \(\mathbb Z_\infty\)-module. To see it, let \(q:[-1,1]\to Q\) be the map that is the identity on \(\pm1\) and sends the open interval to \(0\). If \(|\sum_i\lambda_iy_i|=1\) with \(y_i\in[-1,1]\), then \(|y_i|=1\) whenever \(\lambda_i\ne0\), because \(1\le\sum_i|\lambda_i||y_i|\le\sum_i|\lambda_i|\le1\). Apply this to the numbers \(y_i\) and to the numbers \(q(y_i)\): the sum \(\sum_i\lambda_iy_i\) equals \(\pm1\) if and only if \(\sum_i\lambda_iq(y_i)\) does, and then the two sums are equal. So \(q(\sum_i\lambda_iy_i)=[\lambda]_Q(q(y_1),\dots,q(y_n))\) in all cases, and (M1), (M2) pass from \([-1,1]\) to \(Q\) along the surjection \(q\). In \(Q\) we have \(\tfrac12x=0\) for every \(x\), although \(Q\ne\{0\}\). So \(Q\) is not a subset of a real vector space with the induced operations.

*Reference:* [Durov 2007, 2.14.13], where this module is denoted \(\mathbb F_\infty\).

**Proposition 3.4** (Monoids). Let \(H\) be a monoid. Put
\
\mathbb F_1[H=\{0\}\sqcup\bigl((H\smallsetminus\{0\})\times[n]\bigr),
\]
and write \(a\,e^n_i\) for the pair \((a,i)\) and \(0\,e^n_i=0\). Define \(0(t_1,\dots,t_k)=0\) and \((a\,e^k_i)(t_1,\dots,t_k)=a\cdot t_i\), where \(a\cdot0=0\) and \(a\cdot(b\,e^n_j)=(ab)\,e^n_j\).

(a) \(\mathbb F_1[H]\) is a generalized ring with zero, and \(|\mathbb F_1[H]|=H\) as monoids.

(b) An \(\mathbb F_1[H]\)-module is a set \(X\) with a point \(0_X\) and an action of \(H\) such that \(1x=x\), \((ab)x=a(bx)\), \(0x=0_X\) and \(a0_X=0_X\).

(c) For every generalized ring \(A\) with zero, \(\rho\mapsto\rho_1\) is a bijection from the homomorphisms \(\mathbb F_1[H]\to A\) to the monoid homomorphisms \(H\to|A|\) (preserving \(1\) and \(0\)).

**Proof.** (a) Let \(\mathbb Z[H]\) be the monoid ring of \(H\) modulo its zero: the free abelian group on \(H\smallsetminus\{0\}\) with the product of \(H\). Then \(\mathbb F_1H\) is the set of vectors in \(\mathbb Z[H]^n\) with at most one non-zero coordinate, that coordinate lying in \(H\smallsetminus\{0\}\). These sets contain the basis vectors, and \((a\,e_i)(t_1,\dots,t_k)=a\,t_i\) in \(T_{\mathbb Z[H]}\). So \(\mathbb F_1[H]\) is a subclone of the commutative clone \(T_{\mathbb Z[H]}\). The direct check is also short: for \(a\,e^n_i\), \(b\,e^m_j\) and a matrix \((x_{kl})\), both sides of (2.1) are \(ab\,x_{ij}\); if one operation is \(0\), both sides are \(0\).

(b) The constant gives \(0_X\), and \(a\in H\) acts by \([a\,e^1_1]_X\). (M2) gives the four rules and \([a\,e^n_i]_X(x)=ax_i\). Conversely these formulas define a module.

(c) The clone \(\mathbb F_1[H]\) is generated by \(0\) and its unary operations, so \(\rho\) is determined by \(\rho_1\), which is a monoid homomorphism. Conversely let \(\psi:H\to|A|\) be a monoid homomorphism. Put \(\rho(0)=0\) and \(\rho(a\,e^n_i)=\psi(a)e^n_i\). Then \(\rho((a\,e^k_i)(t_1,\dots,t_k))=\rho(a\cdot t_i)=\psi(a)\rho(t_i)\): for \(t_i=b\,e^n_j\) this is \(\psi(ab)e^n_j=\psi(a)(\psi(b)e^n_j)\), also when \(ab=0\), and for \(t_i=0\) it is \(\psi(a)0=0\) by Proposition 2.5. So \(\rho\) is a homomorphism. \(\square\)

**Example 3.5** (\(\mathbb F_1\), \(\mathbb F_{\pm1}\), \(\mathbb F_{1^n}\)). Take for \(H\) the monoid \(\{0,1\}\). The generalized ring \(\mathbb F_1=\mathbb F_1[\{0,1\}]\) has \(\mathbb F_1(m)=\{0,e^m_1,\dots,e^m_m\}\). Its modules are the pointed sets. Its monoid of unary operations is the monoid \(\mathbb F_1=\{0,1\}\) of the other lessons. By Proposition 3.4(c), a generalized ring \(A\) with zero receives exactly one homomorphism from \(\mathbb F_1\): \(\mathbb F_1\) is initial among generalized rings with zero.

For \(n\ge1\) let \(\mu_n\) be the group of \(n\)-th roots of unity and \(\mathbb F_{1^n}=\mathbb F_1[\{0\}\cup\mu_n]\). So \(\mathbb F_{1^n}(m)=\{0\}\cup\{\zeta e^m_i\}\): vectors with at most one non-zero coordinate, which is a root of unity. Commutativity is inherited from \(T_{\mathbb C}\), or checked as in Proposition 3.4: \(\zeta(\zeta'x)=\zeta'(\zeta x)\). A module is a pointed set with an action of \(\mu_n\) that fixes the base point. Fix a generator of \(\mu_n\). For a generalized ring \(A\) with zero, the homomorphisms \(\mathbb F_{1^n}\to A\) correspond, through the image of this generator, to the elements \(\zeta\in|A|\) with \(\zeta^n=e\). The case \(n=2\) is \(\mathbb F_{\pm1}\) of Example 3.2: its modules are pointed sets with an involution \(x\mapsto-x\) that fixes the base point.

**Example 3.6** (The initial generalized ring \(\mathbb F_\varnothing\)). Let \(\mathbb F_\varnothing(n)=\{e^n_1,\dots,e^n_n\}\) with \(e^k_i(t_1,\dots,t_k)=t_i\). (C1)–(C3) hold, and both sides of (2.1) for \(e^n_i\) and \(e^m_j\) are \(x_{ij}\). So \(\mathbb F_\varnothing\) is a generalized ring. Its monad is the identity functor. Every set, the empty set included, is an \(\mathbb F_\varnothing\)-module in exactly one way. For every clone \(A\) there is exactly one homomorphism \(\mathbb F_\varnothing\to A\), so \(\mathbb F_\varnothing\) is the initial generalized ring. It has no constant. A homomorphism \(\mathbb F_1\to A\) is the choice of a constant of \(A\); so, by Proposition 2.5(a), a generalized ring \(A\) receives one homomorphism from \(\mathbb F_1\) if it has a zero and none otherwise.

**Example 3.7** (Edge cases and non-examples). (a) If \(e^2_1=e^2_2\) in a clone \(A\), then \(t=e^2_1(t,t')=e^2_2(t,t')=t'\) for all \(t,t'\in A(n)\). So there are exactly two such clones: the *trivial* clone \(\mathbf 1\), with one operation in each arity, and \(\mathbf 1_+\), with \(\mathbf 1_+(0)=\varnothing\). Both are generalized rings. The modules of \(\mathbf 1\) are the one-point sets. \(\mathbf 1=T_R\) for the zero ring \(R\). A generalized ring with zero is trivial if and only if \(e=0\): then \(t=e(t)=0(t)=0\) for all \(t\).

(b) For a set \(X\) with at least two elements, \(\mathrm{END}(X)\) is not commutative: it has more than one constant.

(c) The monad of monoids (not necessarily commutative, without zero) sends \(X\) to the set of words in \(X\). It is finitary. Its binary operation \(m\) does not commute with itself: for the matrix with rows \((a,b)\) and \((c,d)\) the two sides of (2.1) are the words \(abcd\) and \(acbd\).

(d) For a non-commutative ring \(R\), \(T_R\) is a finitary monad that is not commutative, and Proposition 2.3(iii) fails: the left multiples of a module endomorphism of \(R\) are in general not module endomorphisms.

(e) There are generalized rings without zero other than \(\mathbb F_\varnothing\), for example the subclone of \(T_{\mathbb R}\) of all \(\lambda\) with \(\lambda_i\ge0\) and \(\sum_i\lambda_i=1\). Every convex subset of a real vector space is a module over it, under convex combinations. These are not all its modules: the formula of Exercise 10.2(c) makes every join-semilattice a module, with the same proof. Exercise 10.2 treats a variant of this clone.

The following table collects the examples.

| Generalized ring | \(n\)-ary operations | Modules | Zero | Addition |
|---|---|---|---|---|
| \(T_R\), \(R\) a commutative semiring | \(R^n\) | \(R\)-semimodules | yes | yes |
| \(\mathbb Z_\infty\) | \(\lambda\in\mathbb R^n\), \(\sum_i\lvert\lambda_i\rvert\le1\) | sets with absolutely convex combinations | yes | no |
| \(\mathbb F_1[H]\), \(H\) a monoid | \(0\) and \(a\,e^n_i\), \(a\in H\smallsetminus\{0\}\) | pointed sets with an action of \(H\) | yes | no, unless \(H=\{0\}\) |
| \(\mathbb F_1\) | \(0,e^n_1,\dots,e^n_n\) | pointed sets | yes | no |
| \(\mathbb F_{\pm1}\) | \(0,\pm e^n_1,\dots,\pm e^n_n\) | pointed sets with an involution | yes | no |
| \(\mathbb F_\varnothing\) | \(e^n_1,\dots,e^n_n\) | sets | no | no |

## 4. Modules and tensor products

A reference for this section is [Durov 2007, 4.6 and 5.3].

### Constructions that work for every clone

Let \(A\) be a clone and \(M\) an \(A\)-module.

- A *submodule* is a subset \(N\subseteq M\) with \(t(x_1,\dots,x_n)\in N\) for all \(t\) and all \(x_i\in N\). If \(A\) has no constant, the empty set is a submodule. The submodule generated by a subset \(G\) is the set of all \(t(g_1,\dots,g_n)\) with \(t\in A(n)\) and \(g_i\in G\); it is the image of the homomorphism \(A(G)\to M\), \(\{g\}\mapsto g\).
- Products of modules are modules, with operations computed in each coordinate.
- A *congruence* on \(M\) is an equivalence relation \(\approx\) such that \(x_i\approx y_i\) for all \(i\) implies \(t(x_1,\dots,x_n)\approx t(y_1,\dots,y_n)\). Then \(M/{\approx}\) is a module and \(M\to M/{\approx}\) is a homomorphism. For a homomorphism \(f\), the relation \(f(x)=f(y)\) is a congruence. An intersection of congruences is a congruence, so every subset \(E\subseteq M\times M\) lies in a smallest congruence \(\langle E\rangle\).

**Lemma 4.1.** Let \(E\subseteq M\times M\). The homomorphisms \(M/\langle E\rangle\to P\) correspond to the homomorphisms \(f:M\to P\) with \(f(a)=f(b)\) for all \((a,b)\in E\).

**Proof.** For such an \(f\), the relation \(f(x)=f(y)\) is a congruence that contains \(E\), hence \(\langle E\rangle\). So \(f\) factors through \(M/\langle E\rangle\), in one way. \(\square\)

### Homomorphisms and tensor products over a generalized ring

Let \(A\) be a generalized ring. By Proposition 2.3, \(\operatorname{Hom}_A(M,N)\) is an \(A\)-module with the operations \(t(f_1,\dots,f_n)(x)=t(f_1(x),\dots,f_n(x))\). A map \(\Phi:M\times N\to P\) is *bilinear* if \(\Phi(x,-)\) and \(\Phi(-,y)\) are homomorphisms for all \(x\in M\) and \(y\in N\).

**Theorem 4.2.** Let \(A\) be a generalized ring and \(M\), \(N\) two \(A\)-modules.

(a) There are a module \(M\otimes_AN\) and a bilinear map \(M\times N\to M\otimes_AN\), \((x,y)\mapsto x\otimes y\), such that every bilinear map \(\Phi:M\times N\to P\) has the form \(\Phi(x,y)=\varphi(x\otimes y)\) for exactly one homomorphism \(\varphi:M\otimes_AN\to P\).

(b) There are natural bijections between \(\operatorname{Hom}_A(M\otimes_AN,P)\), the set of bilinear maps \(M\times N\to P\), and \(\operatorname{Hom}_A(M,\operatorname{Hom}_A(N,P))\).

(c) \(A(1)\otimes_AM\cong M\), \(M\otimes_AN\cong N\otimes_AM\), and \(A(X)\otimes_AA(Y)\cong A(X\times Y)\) for all sets \(X\), \(Y\). In particular \(A(m)\otimes_AA(n)\cong A(mn)\).

**Proof.** (a) Let \(L=A(M\times N)\) be the free module with generators \(\{x,y\}\). Let \(E\) be the set of all pairs
\[
\bigl(t(\{x_1,y\},\dots,\{x_n,y\}),\ \{t(x_1,\dots,x_n),y\}\bigr)\quad\text{and}\quad\bigl(t(\{x,y_1\},\dots,\{x,y_n\}),\ \{x,t(y_1,\dots,y_n)\}\bigr)
\]
with \(n\ge0\) and \(t\in A(n)\). Put \(M\otimes_AN=L/\langle E\rangle\) and let \(x\otimes y\) be the class of \(\{x,y\}\). The map \((x,y)\mapsto x\otimes y\) is bilinear by construction. For a bilinear \(\Phi\), the homomorphism \(L\to P\) with \(\{x,y\}\mapsto\Phi(x,y)\) takes equal values on the two members of each pair of \(E\). By Lemma 4.1 it factors through \(M\otimes_AN\). The factorization is unique because the elements \(x\otimes y\) generate.

(b) The first bijection is (a). The second sends \(\Phi\) to \(x\mapsto\Phi(x,-)\). Linearity in the second variable says that each \(\Phi(x,-)\) lies in \(\operatorname{Hom}_A(N,P)\). Linearity in the first variable says that \(x\mapsto\Phi(x,-)\) is a homomorphism into the module of all maps \(N\to P\), whose operations are computed pointwise.

(c) By Lemma 1.5 and (b), \(\operatorname{Hom}_A(A(1)\otimes_AM,P)\cong\operatorname{Hom}_A(A(1),\operatorname{Hom}_A(M,P))\cong\operatorname{Hom}_A(M,P)\), naturally in \(P\). So \(A(1)\otimes_AM\cong M\) by the Yoneda lemma; the isomorphism is \(u\otimes x\mapsto ux\). The definition of bilinear maps is symmetric in \(M\) and \(N\), which gives the second isomorphism. For the third, homomorphisms out of \(A(X)\otimes_AA(Y)\) into \(P\) are homomorphisms \(A(X)\to\operatorname{Hom}_A(A(Y),P)\), hence maps from \(X\) to the set of maps \(Y\to P\), hence maps \(X\times Y\to P\), hence homomorphisms \(A(X\times Y)\to P\). \(\square\)

**Example 4.3.** (a) For \(A=T_R\) a map \(\Phi\) is bilinear exactly when it is additive and \(R\)-linear in each variable, and \(M\otimes_AN\) is the usual tensor product. (b) For \(A=\mathbb F_\varnothing\) every map is bilinear, and \(M\otimes N=M\times N\). (c) For \(A=\mathbb F_1\) the modules are the pointed sets, and \(\Phi\) is bilinear exactly when \(\Phi(x,0)=0=\Phi(0,y)\). So \(M\otimes_{\mathbb F_1}N\) is the smash product: \(M\times N\) with the subset \(M\times\{0\}\cup\{0\}\times N\) collapsed to one point. For \(M=\mathbb F_1(m)\) and \(N=\mathbb F_1(n)\) it has \(mn+1\) elements, in agreement with \(\mathbb F_1(m)\otimes\mathbb F_1(n)\cong\mathbb F_1(mn)\).

### Scalar extension

**Proposition 4.4.** Let \(\rho:A\to B\) be a homomorphism of clones. Every \(B\)-module is an \(A\)-module through \(\rho\); this is the *restriction* functor. It has a left adjoint \(M\mapsto B\otimes_AM\), and \(B\otimes_AA(X)\cong B(X)\).

**Proof.** Let \(B\otimes_AM=B(M)/\langle E\rangle\), where \(E\) is the set of pairs \(\bigl(\rho(t)(\{x_1\},\dots,\{x_n\}),\ \{t(x_1,\dots,x_n)\}\bigr)\) with \(t\in A(n)\) and \(x_i\in M\). By freeness and Lemma 4.1, the homomorphisms of \(B\)-modules \(B\otimes_AM\to N\) are the maps \(g:M\to N\) with \(\rho(t)(g(x_1),\dots,g(x_n))=g(t(x_1,\dots,x_n))\), that is, the homomorphisms of \(A\)-modules from \(M\) to \(N\). For \(M=A(X)\) these are the maps \(X\to N\), so \(B\otimes_AA(X)\cong B(X)\). \(\square\)

**Example 4.5** (Base change to \(\mathbb Z\)). Let \(X\) be a pointed set, that is, an \(\mathbb F_1\)-module. An additive group \(G\) is a pointed set with base point \(0\), and the pointed maps \(X\to G\) are the maps \(X\smallsetminus\{0\}\to G\). So \(\mathbb Z\otimes_{\mathbb F_1}X\) is the free abelian group on \(X\smallsetminus\{0\}\). In the same way, for a monoid \(H\) and an \(\mathbb F_1[H]\)-module \(X\), \(\mathbb Z[H]\otimes_{\mathbb F_1[H]}X\) is the free abelian group on \(X\smallsetminus\{0\}\), with \(a\{x\}=\{ax\}\) if \(ax\ne0\) and \(a\{x\}=0\) otherwise.

## 5. Localization

A reference for this section is [Durov 2007, 6.1].

Let \(A\) be a generalized ring. A *multiplicative subset* is a submonoid \(S\) of \(|A|\). For \(f\in|A|\) let \(S_f=\{e,f,f^2,\dots\}\). Localization works as for rings, because it uses only the monoid \(|A|\) and its action on modules; commutativity enters through Proposition 2.5(c).

**Theorem 5.1.** Let \(S\subseteq|A|\) be a multiplicative subset and \(M\) an \(A\)-module. On \(M\times S\) put \((x,s)\sim(y,t)\) if \(utx=usy\) for some \(u\in S\). This is an equivalence relation. Write \(x/s\) for the class of \((x,s)\) and \(S^{-1}M\) for the set of classes.

(a) \(S^{-1}M\) is an \(A\)-module with \(a(x_1/s,\dots,x_n/s)=a(x_1,\dots,x_n)/s\), and \(x\mapsto x/1\) is a homomorphism \(M\to S^{-1}M\).

(b) Every \(s\in S\) acts bijectively on \(S^{-1}M\).

(c) If \(N\) is an \(A\)-module on which every element of \(S\) acts bijectively, then every homomorphism \(M\to N\) factors through \(M\to S^{-1}M\), in exactly one way.

**Proof.** The relation is reflexive and symmetric. If \(utx=usy\) and \(vry=vtz\), then \((uvt)rx=vr(utx)=vr(usy)=us(vry)=us(vtz)=(uvt)sz\); so it is transitive. Finitely many fractions have a common denominator: \(x_i/s_i=(s'_ix_i)/s\) with \(s=s_1\cdots s_n\) and \(s'_i=\prod_{j\ne i}s_j\).

(a) Suppose \(x_i/s=y_i/s'\) for all \(i\). There is one \(u\in S\) with \(us'x_i=usy_i\) for all \(i\). By Proposition 2.5(c), \(us'\,a(x_1,\dots,x_n)=a(us'x_1,\dots,us'x_n)=a(usy_1,\dots,usy_n)=us\,a(y_1,\dots,y_n)\). So \(a(x)/s=a(y)/s'\), and the operations are well defined. (M1) and (M2) hold because they can be checked on fractions with a common denominator.

(b) The inverse of \(x/t\mapsto sx/t\) is \(x/t\mapsto x/(st)\).

(c) For a homomorphism \(g:M\to N\) put \(\bar g(x/s)=s^{-1}g(x)\), where \(s^{-1}\) is the inverse of the action of \(s\) on \(N\). If \(utx=usy\), then \(ut\,g(x)=us\,g(y)\), and applying the inverse of the action of \(uts\) gives \(s^{-1}g(x)=t^{-1}g(y)\). By Proposition 2.5(c) the action of \(s\) on \(N\) is a bijective homomorphism, so its inverse is a homomorphism; hence \(\bar g(a(x_1,\dots,x_n)/s)=s^{-1}a(g(x_1),\dots)=a(s^{-1}g(x_1),\dots)\), and \(\bar g\) is a homomorphism. It is the only one, because \(x/s\) is the only element \(z\) with \(sz=x/1\). \(\square\)

**Theorem 5.2.** Let \(S\subseteq|A|\) be a multiplicative subset. Put \((S^{-1}A)(n)=S^{-1}(A(n))\), take the elements \(e^n_i/1\), and for \(a/s\in S^{-1}A(k)\) and \(b_1,\dots,b_k\in S^{-1}A(n)\) put
\[
(a/s)(b_1,\dots,b_k)=s^{-1}\,a(b_1,\dots,b_k),
\]
where \(a(b_1,\dots,b_k)\) is computed in the \(A\)-module \(S^{-1}A(n)\) and \(s^{-1}\) is the inverse of the action of \(s\) on it.

(a) \(S^{-1}A\) is a generalized ring, \(\iota:A\to S^{-1}A\), \(a\mapsto a/1\), is a homomorphism, and \(\iota(s)\) is invertible in \(|S^{-1}A|\) for every \(s\in S\).

(b) For every homomorphism of generalized rings \(\rho:A\to C\) such that \(\rho(s)\) is invertible in \(|C|\) for all \(s\in S\), there is exactly one homomorphism \(\rho':S^{-1}A\to C\) with \(\rho'\circ\iota=\rho\). It is \(\rho'(a/s)=\rho(s)^{-1}\rho(a)\).

(c) Restriction along \(\iota\) identifies the \(S^{-1}A\)-modules with the \(A\)-modules on which every element of \(S\) acts bijectively, and \(S^{-1}A\otimes_AM\cong S^{-1}M\).

**Proof.** Let \(N\) be an \(A\)-module on which \(S\) acts bijectively. For \(a/s\in S^{-1}A(k)\) and \(y\in N^k\) put \([a/s]_N(y)=s^{-1}a(y)\). This is well defined: if \(a/s=a'/s'\), then \(us'a=usa'\) in \(A(k)\) for some \(u\), so \(us'\,a(y)=us\,a'(y)\) by (M2), and \(s^{-1}a(y)=s'^{-1}a'(y)\). The substitution of the theorem is the case \(N=S^{-1}A(n)\), which is allowed by Theorem 5.1(b). We claim that for \(b_i\in S^{-1}A(n)\) and \(y\in N^n\)
\[
[(a/s)(b_1,\dots,b_k)]_N(y)=[a/s]_N\bigl([b_1]_N(y),\dots,[b_k]_N(y)\bigr).\tag{5.1}
\]
Write \(b_i=a_i/u\) with a common denominator. Then \((a/s)(b_1,\dots,b_k)=a(a_1,\dots,a_k)/(su)\), so the left side is \((su)^{-1}a(a_1(y),\dots,a_k(y))\). The right side is \(s^{-1}a(u^{-1}a_1(y),\dots,u^{-1}a_k(y))\), and the two agree because the inverse of the action of \(u\) on \(N\) is a homomorphism.

(a) (C3) is (5.1) for \(N=S^{-1}A(m)\). (C1) is clear, and (C2) holds because \((a/s)(e^k_1/1,\dots,e^k_k/1)=s^{-1}(a/1)=a/s\). So \(S^{-1}A\) is a clone and \(\iota\) is a homomorphism. The element \(e/s\) is inverse to \(s/1\). By (5.1), every \(N\) as above is an \(S^{-1}A\)-module with operations \([a/s]_N=s^{-1}\circ[a]_N\); the free modules \(S^{-1}A(n)\) are of this kind. The maps \([a]_N\) and \([a']_N\) satisfy (2.1), and the inverses of the actions of \(s\) and \(s'\) are homomorphisms that commute with each other. So \([a/s]_N\) and \([a'/s']_N\) satisfy (2.1), and \(S^{-1}A\) is commutative.

(b) If \(a/s=a'/s'\), then \(\rho(u)\rho(s')\rho(a)=\rho(u)\rho(s)\rho(a')\) for some \(u\in S\), so \(\rho(s)^{-1}\rho(a)=\rho(s')^{-1}\rho(a')\) and \(\rho'\) is well defined. With a common denominator, \(\rho'\bigl((a/s)(a_1/u,\dots,a_k/u)\bigr)=\rho(su)^{-1}\rho(a)(\rho(a_1),\dots,\rho(a_k))\), and \(\rho'(a/s)\bigl(\rho'(a_1/u),\dots\bigr)=\rho(s)^{-1}\rho(a)\bigl(\rho(u)^{-1}\rho(a_1),\dots\bigr)\). These agree by Proposition 2.5(c) in \(C\). Uniqueness: \((s/1)(a/s)=a/1\) forces \(\rho'(a/s)=\rho(s)^{-1}\rho(a)\).

(c) On an \(S^{-1}A\)-module, \(s\) acts bijectively, because \(s/1\) is invertible. Conversely, on a module \(N\) on which \(S\) acts bijectively, the operations \([a/s]_N\) above satisfy (M1) and (M2), which is (5.1), and restrict to the given \(A\)-module structure. No other structure restricts to it, because \(a/s=(e/s)(a/1)\) and \([e/s]_N\) must be the inverse of \([s/1]_N\). A map between two such modules is a homomorphism for \(A\) if and only if it is one for \(S^{-1}A\). By Theorem 5.1, \(M\mapsto S^{-1}M\) is left adjoint to the inclusion of these modules into all \(A\)-modules, so \(S^{-1}M\cong S^{-1}A\otimes_AM\) by Proposition 4.4. \(\square\)

We write \(A_f=S_f^{-1}A\) and \(M_f=S_f^{-1}M\).

**Example 5.3.** (a) For a ring \(R\) and a multiplicative subset \(S\) of \(R\), \(S^{-1}T_R=T_{S^{-1}R}\). For a monoid \(H\), \(S^{-1}\mathbb F_1[H]=\mathbb F_1[S^{-1}H]\), where \(S^{-1}H\) is the localization of the monoid.

(b) Let \(f\in[-1,1]\) with \(0<|f|<1\). Then \((\mathbb Z_\infty)_f\cong T_{\mathbb R}\). Indeed, \(f\) is invertible in \(\mathbb R\), so Theorem 5.2(b) gives a homomorphism \((\mathbb Z_\infty)_f\to T_{\mathbb R}\), \(\lambda/f^j\mapsto f^{-j}\lambda\). It is injective: \(\lambda/f^j=\lambda'/f^l\) means \(f^{m+l}\lambda=f^{m+j}\lambda'\) for some \(m\), that is, \(f^{-j}\lambda=f^{-l}\lambda'\). It is surjective: for \(v\in\mathbb R^n\) and large \(j\) we have \(|f|^j\sum_i|v_i|\le1\), so \(f^jv\in\mathbb Z_\infty(n)\) and \(v\) is the image of \((f^jv)/f^j\). In the same way \((\mathbb Z_{(\infty)})_f\cong T_{\mathbb Q}\) for rational \(f\) with \(0<|f|<1\). So the localization of \(\mathbb Z_\infty\) at one such element is already the field \(\mathbb R\), and that of \(\mathbb Z_{(\infty)}\) is the field \(\mathbb Q\).

## 6. Tensor products of generalized rings

**Definition 6.1.** Let \(\gamma:C\to A\) and \(\delta:C\to B\) be homomorphisms of generalized rings. A *tensor product* \(A\otimes_CB\) is a pushout in the category of generalized rings: a generalized ring \(P\) with homomorphisms \(i:A\to P\) and \(j:B\to P\) such that \(i\gamma=j\delta\), and such that for every generalized ring \(D\) and all homomorphisms \(f:A\to D\), \(g:B\to D\) with \(f\gamma=g\delta\) there is exactly one homomorphism \(h:P\to D\) with \(hi=f\) and \(hj=g\).

A pushout is unique up to unique isomorphism. Pushouts of generalized rings always exist [Durov 2007, 5.1.6]; we do not prove this, and we verify the universal property in each case that we use. For \(C=\mathbb F_\varnothing\) the condition \(f\gamma=g\delta\) is empty. For \(C=\mathbb F_1\) it holds automatically, because \(D\) has only one constant.

**Theorem 6.2.** Let \(R\) and \(R'\) be rings and let \(C\) be \(\mathbb F_\varnothing\) or \(\mathbb F_1\). Then
\[
T_R\otimes_CT_{R'}=T_{R\otimes_{\mathbb Z}R'},
\]
with the homomorphisms induced by \(R\to R\otimes_{\mathbb Z}R'\leftarrow R'\).

**Proof.** Let \(D\), \(f\) and \(g\) be as in Definition 6.1. By Corollary 2.7(b), \(D=T_{R''}\) for the ring \(R''=|D|\), and \(f\), \(g\) come from ring homomorphisms \(R\to R''\) and \(R'\to R''\). These factor through exactly one ring homomorphism \(R\otimes_{\mathbb Z}R'\to R''\). By Corollary 2.7(a) this is exactly one homomorphism \(h:T_{R\otimes_{\mathbb Z}R'}\to D\) with \(hi=f\) and \(hj=g\). \(\square\)

**Corollary 6.3.** (a) For every generalized ring \(D\) there is at most one homomorphism \(\mathbb Z\to D\), and at most one homomorphism \(\mathbb N\to D\). A homomorphism \(\mathbb Z\to D\) exists exactly when \(D\) is a ring.

(b) \(\mathbb Z\otimes_{\mathbb F_1}\mathbb Z=\mathbb Z=\mathbb Z\otimes_{\mathbb F_\varnothing}\mathbb Z\) and \(\mathbb N\otimes_{\mathbb F_1}\mathbb N=\mathbb N\), with both structure maps equal to the identity.

(c) \(\mathbb F_1\to\mathbb Z\) and \(\mathbb F_\varnothing\to\mathbb Z\) are epimorphisms in the category of generalized rings.

**Proof.** (a) By Corollary 2.7, a homomorphism \(T_{\mathbb Z}\to D\) is a ring homomorphism from \(\mathbb Z\) to the ring \(|D|\), and a homomorphism \(T_{\mathbb N}\to D\) is a semiring homomorphism from \(\mathbb N\) to the semiring \(|D|\). There is at most one of each. (b) The first statement is Theorem 6.2 with \(\mathbb Z\otimes_{\mathbb Z}\mathbb Z=\mathbb Z\). For \(\mathbb N\): by (a) any two homomorphisms \(f,g:\mathbb N\to D\) are equal, so \(\mathbb N\) with the identity maps has the universal property. (c) restates (a). \(\square\)

*Reference:* [Durov 2007, 5.1.22].

Part (a) gives the same statements over every base. If \(C\) is a generalized ring with a homomorphism \(C\to\mathbb Z\), then this homomorphism is an epimorphism, and \(\mathbb Z\otimes_C\mathbb Z=\mathbb Z\) with both structure maps equal to the identity. An example is the inclusion \(\mathbb F_{\pm1}\subseteq\mathbb Z\) of Example 3.2.

By Theorem 6.2, \(\mathbb Z/n\otimes_{\mathbb F_1}\mathbb Z/n=\mathbb Z/n\), \(\mathbb Z[x]\otimes_{\mathbb F_1}\mathbb Z[y]=\mathbb Z[x,y]\), and \(\mathbb F_p\otimes_{\mathbb F_1}\mathbb F_q\) is the zero ring for primes \(p\ne q\). Tensor products of rings over \(\mathbb F_1\) are tensor products over \(\mathbb Z\). The product \(\operatorname{Spec}\mathbb Z\times\operatorname{Spec}\mathbb Z\) over \(\mathbb F_1\), one of the objects asked for in *Weil's proof for curves and what is missing over the integers*, is therefore \(\operatorname{Spec}\mathbb Z\) itself in this theory (Corollary 7.10).

**Remark 6.4** (The role of commutativity). The proof rests on Theorem 2.6(a): in a commutative clone two additions are equal. It fails without commutativity. Let \(X\) be a set with four elements and a chosen element \(0\). It carries two group structures with neutral element \(0\): a cyclic one and one in which every element has order at most two. They give two different homomorphisms of clones \(T_{\mathbb Z}\to\mathrm{END}(X)\) that agree on \(\mathbb F_1\). So \(\mathbb F_1\to\mathbb Z\) is not an epimorphism in the category of all clones.

**Proposition 6.5.** Let \(H\) be a monoid and \(R\) a ring. Then \(\mathbb F_1[H]\otimes_{\mathbb F_1}T_R=T_{R[H]}\), where \(R[H]\) is the monoid algebra of \(H\) over \(R\) modulo the zero of \(H\).

**Proof.** Let \(D\) be a generalized ring with homomorphisms \(f:T_R\to D\) and \(g:\mathbb F_1[H]\to D\). By Corollary 2.7, \(D=T_{R''}\) and \(f\) is a ring homomorphism \(R\to R''\). By Proposition 3.4(c), \(g\) is a monoid homomorphism \(H\to(R'',\cdot)\) that preserves \(0\) and \(1\). Such a pair is the same thing as a ring homomorphism \(R[H]\to R''\), that is, a homomorphism \(T_{R[H]}\to D\). \(\square\)

**Example 6.6.** \(\mathbb F_{1^n}\otimes_{\mathbb F_1}\mathbb Z=\mathbb Z[x]/(x^n-1)\), the group ring of \(\mu_n\). For \(n\ge2\) this is not the ring generated by the \(n\)-th roots of unity in \(\mathbb C\). Proposition 6.5 also shows that the base change \(H\mapsto\mathbb Z[H]\) of *Commutative monoids and their spectra* is a tensor product of generalized rings.

## 7. Spectra and generalized schemes

References for this section are [Durov 2007, 6.2, 6.3.17 and 6.5]. We use prime spectra throughout. [Durov 2007, 6.3] also defines spectra for finer "localization theories"; they are not treated here.

### Ideals and prime ideals

Let \(A\) be a generalized ring.

**Definition 7.1.** An *ideal* of \(A\) is an \(A\)-submodule of \(|A|=A(1)\). The ideal generated by a family \((f_i)\) is the set of all \(h(f_{i_1},\dots,f_{i_n})\) with \(h\in A(n)\); the ideal generated by one element \(f\) is \(f|A|\). An ideal \(\mathfrak p\) is *prime* if \(|A|\smallsetminus\mathfrak p\) is a submonoid of \(|A|\): it contains \(e\) and is closed under products. An ideal is *maximal* if it is maximal among the ideals different from \(|A|\). The *spectrum* \(\operatorname{Spec}A\) is the set of prime ideals. For \(f\in|A|\) let \(D(f)=\{\mathfrak p:f\notin\mathfrak p\}\). Since \(D(f)\cap D(g)=D(fg)\) and \(D(e)=\operatorname{Spec}A\), the sets \(D(f)\) are a base of a topology on \(\operatorname{Spec}A\).

Every ideal contains \(0\) if \(A\) has a zero. If \(A\) has no constant, the empty set is an ideal, and it is prime. The ideals of \(T_R\) are the ideals of the ring \(R\). The ideals of \(\mathbb F_1[H]\) are the subsets \(I\subseteq H\) with \(0\in I\) and \(HI\subseteq I\), the ideals of the monoid \(H\). So \(\operatorname{Spec}T_R\) is the spectrum of the ring \(R\), and \(\operatorname{Spec}\mathbb F_1[H]\) is the spectrum of the monoid \(H\) from *Commutative monoids and their spectra*. In general, if \(A\) has a zero, an ideal of \(A\) is an ideal of the monoid \(|A|\) that is also closed under all operations of \(A\), and \(\operatorname{Spec}A\) is a subspace of the spectrum of the monoid \(|A|\).

**Lemma 7.2.** (a) Every ideal different from \(|A|\) is contained in a maximal ideal.

(b) Every maximal ideal is prime.

**Proof.** (a) An ideal is different from \(|A|\) exactly when it does not contain \(e\). The union of a chain of ideals that do not contain \(e\) is an ideal that does not contain \(e\), because operations have finitely many arguments. Apply Zorn's lemma.

(b) Let \(\mathfrak m\) be maximal and \(x,y\notin\mathfrak m\). The ideal generated by \(\mathfrak m\) and \(x\) is \(|A|\). So \(e=t(m_1,\dots,m_k,x)\) with \(t\in A(k+1)\) and \(m_i\in\mathfrak m\); by (1.1) repeated arguments can be merged. In the same way \(e=t'(m'_1,\dots,m'_l,y)\). By Proposition 2.5(c),
\[
e=t(m_1,\dots,m_k,x\cdot e)=t\bigl(m_1,\dots,m_k,t'(xm'_1,\dots,xm'_l,xy)\bigr).
\]
So \(e\) lies in the ideal generated by \(\mathfrak m\) and \(xy\). Hence \(xy\notin\mathfrak m\). Also \(e\notin\mathfrak m\). \(\square\)

**Proposition 7.3.** Let \(A\) be a generalized ring.

(a) For a family \((f_i)\) in \(|A|\): \(\bigcup_iD(f_i)=\operatorname{Spec}A\) if and only if the \(f_i\) generate the ideal \(|A|\). Then finitely many of the \(D(f_i)\) cover. So \(\operatorname{Spec}A\) is quasi-compact.

(b) Let \(S\subseteq|A|\) be a multiplicative subset and \(\iota:A\to S^{-1}A\). Then \(\mathfrak q\mapsto\iota^{-1}(\mathfrak q)\) is a homeomorphism from \(\operatorname{Spec}S^{-1}A\) onto the subspace of the primes \(\mathfrak p\) of \(A\) with \(\mathfrak p\cap S=\varnothing\). In particular \(\operatorname{Spec}A_f\cong D(f)\), and \(D(f)\) is quasi-compact.

(c) \(D(g)\subseteq D(f)\) if and only if \(f\) is invertible in \(|A_g|\), if and only if \(g^k\in f|A|\) for some \(k\ge1\).

(d) \(\operatorname{Spec}A=\varnothing\) if and only if \(A\) is the trivial generalized ring \(\mathbf 1\).

**Proof.** (a) If the \(f_i\) generate an ideal different from \(|A|\), a maximal ideal containing it is a prime ideal outside all \(D(f_i)\), by Lemma 7.2. If they generate \(|A|\), then \(e=h(f_{i_1},\dots,f_{i_n})\) for some \(h\in A(n)\). A prime ideal that contains \(f_{i_1},\dots,f_{i_n}\) would contain \(e\). So \(D(f_{i_1}),\dots,D(f_{i_n})\) cover. Every open cover can be refined to a cover by sets \(D(f_i)\), so the space is quasi-compact.

(b) Let \(\mathfrak p\) be a prime of \(A\) with \(\mathfrak p\cap S=\varnothing\), and let \(S^{-1}\mathfrak p\) be the set of fractions \(x/s\) with \(x\in\mathfrak p\). It is an ideal of \(S^{-1}A\), because \((a/s)(x_1/u,\dots,x_n/u)=a(x_1,\dots,x_n)/(su)\). If \(y/t=x/s\) with \(x\in\mathfrak p\), then \(vsy=vtx\in\mathfrak p\) for some \(v\in S\), and \(vs\notin\mathfrak p\), so \(y\in\mathfrak p\). It follows that \(\iota^{-1}(S^{-1}\mathfrak p)=\mathfrak p\) and that \(S^{-1}\mathfrak p\) is prime. Conversely, let \(\mathfrak q\) be a prime of \(S^{-1}A\). Then \(\mathfrak p=\iota^{-1}(\mathfrak q)\) is a prime ideal: it is a submodule because \(\iota\) is a homomorphism, and its complement is a submonoid. It does not meet \(S\), because the elements of \(S\) become invertible. And \(\mathfrak q=S^{-1}\mathfrak p\), because \(x/s\in\mathfrak q\) if and only if \(x/1=(s/1)(x/s)\in\mathfrak q\). So the map is a bijection. It maps \(D(a/s)=D(a/1)\) onto the set of \(\mathfrak p\in D(a)\) with \(\mathfrak p\cap S=\varnothing\), so it is a homeomorphism onto its image. For \(S=S_f\) the image is \(D(f)\), and \(D(f)\) is quasi-compact by (a).

(c) By (b), \(D(g)\subseteq D(f)\) means that \(f/1\) lies in no prime ideal of \(A_g\). By Lemma 7.2 this means that the ideal generated by \(f/1\) is \(|A_g|\), that is, \(f/1\) is invertible. If \((f/1)(a/g^j)=e/1\), then \(g^mfa=g^{m+j}\) for some \(m\), so a power of \(g\) lies in \(f|A|\). Conversely, if \(g^k=fa\), then \((f/1)(a/g^k)=e/1\).

(d) If \(A\) has no constant, the empty ideal is contained in a prime ideal by Lemma 7.2. If \(A\) has a zero, \(\{0\}\) is an ideal by Proposition 2.5(c). It is different from \(|A|\) exactly when \(e\ne0\), that is, when \(A\) is not trivial (Example 3.7(a)); then it is contained in a prime ideal. \(\square\)

### The structure sheaf

**Lemma 7.4.** Let \(f_1,\dots,f_n\in|A|\) generate the ideal \(|A|\). Then \(f_1^N,\dots,f_n^N\) generate the ideal \(|A|\), for every \(N\ge1\).

**Proof.** Write \(e=h(f_1,\dots,f_n)\) with \(h\in A(n)\). Let \(I_k\) be the ideal generated by the products of \(k\) factors taken from \(f_1,\dots,f_n\). We show \(e\in I_k\) by induction on \(k\); the case \(k=1\) is the hypothesis. If \(e=g(m_1,\dots,m_r)\) with products \(m_j\) of \(k\) factors, then \(f_i=f_i\cdot e=g(f_im_1,\dots,f_im_r)\) by Proposition 2.5(c), so
\[
e=h\bigl(g(f_1m_1,\dots,f_1m_r),\dots,g(f_nm_1,\dots,f_nm_r)\bigr)\in I_{k+1}.
\]
For \(k=n(N-1)+1\), every product of \(k\) factors is a multiple of some \(f_i^N\). So \(I_k\) lies in the ideal generated by the \(f_i^N\). \(\square\)

**Lemma 7.5.** Let \(f_1,\dots,f_n\in|A|\) generate the ideal \(|A|\), and let \(M\) be an \(A\)-module. Then the map \(M\to\prod_iM_{f_i}\) is injective, and its image is the set of families \((z_i)\) such that \(z_i\) and \(z_j\) have the same image in \(M_{f_if_j}\) for all \(i,j\).

**Proof.** *Injective.* Let \(x/1=y/1\) in every \(M_{f_i}\). Then \(f_i^Nx=f_i^Ny\) for all \(i\) and one \(N\). By Lemma 7.4 there is \(H\in A(n)\) with \(H(f_1^N,\dots,f_n^N)=e\). By (M2),
\[
x=H(f_1^N,\dots,f_n^N)\,x=H(f_1^Nx,\dots,f_n^Nx)=H(f_1^Ny,\dots,f_n^Ny)=y .
\]
*Image.* Let \(z_i=x_i/f_i^N\), with one \(N\) for all \(i\), be a family as in the statement. Then \((f_if_j)^Kf_j^Nx_i=(f_if_j)^Kf_i^Nx_j\) for all \(i,j\) and one \(K\). Replace \(x_i\) by \(f_i^Kx_i\) and \(N\) by \(N+K\). Then \(z_i=x_i/f_i^N\) and \(f_j^Nx_i=f_i^Nx_j\) for all \(i,j\). Choose \(H\) as before and put \(x=H(x_1,\dots,x_n)\). By Proposition 2.5(c) and (M2),
\[
f_i^Nx=H(f_i^Nx_1,\dots,f_i^Nx_n)=H(f_1^Nx_i,\dots,f_n^Nx_i)=H(f_1^N,\dots,f_n^N)\,x_i=x_i .
\]
So \(x/1=z_i\) in \(M_{f_i}\). \(\square\)

The operation \(H\) plays the role of a partition of unity.

A *sheaf of generalized rings* on a topological space is a presheaf \(\mathcal O\) with values in generalized rings such that, for every \(m\ge0\), \(U\mapsto\mathcal O(U)(m)\) is a sheaf of sets. A *generalized ringed space* is a space with a sheaf of generalized rings. The *stalk* \(\mathcal O_x\) is the colimit of the \(\mathcal O(U)\) over the open sets \(U\ni x\), taken in each arity; it is a generalized ring.

**Theorem 7.6.** Let \(A\) be a generalized ring and \(X=\operatorname{Spec}A\).

(a) There is a sheaf of generalized rings \(\mathcal O_X\) on \(X\) with \(\mathcal O_X(D(f))=A_f\) for all \(f\in|A|\), whose restriction maps for \(D(g)\subseteq D(f)\) are the canonical homomorphisms \(A_f\to A_g\). It is unique up to unique isomorphism. In particular \(\mathcal O_X(X)=A\).

(b) The stalk of \(\mathcal O_X\) at \(\mathfrak p\) is \(A_{\mathfrak p}=S^{-1}A\) with \(S=|A|\smallsetminus\mathfrak p\). The non-invertible elements of \(|A_{\mathfrak p}|\) form the ideal \(S^{-1}\mathfrak p\), and the preimage of this ideal in \(|A|\) is \(\mathfrak p\).

**Proof.** (a) For a set \(U\) of the form \(D(f)\) let \(S_U\) be the set of all \(g\in|A|\) with \(U\subseteq D(g)\). It is a multiplicative subset. Put \(\mathcal O(U)=S_U^{-1}A\). For \(U=D(f)\) we have \(S_f\subseteq S_U\), and every element of \(S_U\) is invertible in \(A_f\) by Proposition 7.3(c); so \(A_f\to S_U^{-1}A\) is an isomorphism by Theorem 5.2(b). For \(V\subseteq U\) we have \(S_U\subseteq S_V\), which gives the restriction map. This is a presheaf of generalized rings on the base of the sets \(D(f)\). The base is closed under finite intersections and its members are quasi-compact. By [Stacks, Tag [009L](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sheaves.html#sheaves-lemma-cofinal-systems-coverings-standard-case)] it suffices to check, in each arity \(m\), the sheaf condition for finite covers \(D(f)=D(f_1)\cup\dots\cup D(f_n)\). Replacing \(A\) by \(A_f\) we may assume \(f=e\) (Proposition 7.3(b),(c) and Theorem 5.2(b) give \((A_f)_{f_i/1}=A_{f_i}\)). Then the \(f_i\) generate \(|A|\) by Proposition 7.3(a), and the sheaf condition is Lemma 7.5 for \(M=A(m)\), because \(D(f_i)\cap D(f_j)=D(f_if_j)\). By [Stacks, Tags [009N](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sheaves.html#sheaves-lemma-extend-off-basis) and [009O](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sheaves.html#sheaves-lemma-restrict-basis-equivalence)] a sheaf of sets on a base extends to a sheaf on \(X\), uniquely up to unique isomorphism, and maps between sheaves on the base extend uniquely. A section of the extension over an open set \(U\) is a compatible family of sections over the sets \(D(f)\subseteq U\), so the extension commutes with finite products. Hence the substitution maps and the elements \(e^m_i\) extend, and the identities (C1)–(C3) and (2.1) continue to hold.

(b) The sets \(D(f)\) with \(f\notin\mathfrak p\) are cofinal among the neighbourhoods of \(\mathfrak p\). The homomorphisms \(A_f\to A_{\mathfrak p}\) induce a map from the stalk to \(A_{\mathfrak p}\) in each arity. It is surjective: \(a/s\) comes from \(A_s\). It is injective: if \(a/f^k\in A_f(m)\) and \(a'/g^l\in A_g(m)\) have the same image, then \(ug^la=uf^ka'\) for some \(u\notin\mathfrak p\), and the two elements have the same image in \(A_{ufg}(m)\). Let \(x/s\in|A_{\mathfrak p}|\). If \(x\notin\mathfrak p\), its inverse is \(s/x\). If \(x\in\mathfrak p\) and \((x/s)(y/t)=e/1\), then \(uxy=ust\) for some \(u\notin\mathfrak p\); the left side lies in \(\mathfrak p\) and the right side does not. So the set of non-invertible elements is \(S^{-1}\mathfrak p\). It is an ideal with preimage \(\mathfrak p\) by the proof of Proposition 7.3(b). \(\square\)

*Reference:* [Durov 2007, 6.3.17]; for rings, [Stacks, Tag [00EJ](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/algebra.html#algebra-lemma-standard-covering)].

The same proof gives, for every \(A\)-module \(M\), a sheaf \(\widetilde M\) on \(\operatorname{Spec}A\) with \(\widetilde M(D(f))=M_f\).

**Example 7.7.** (a) For a ring \(R\), \(\operatorname{Spec}T_R\) is the spectrum of \(R\), and \(\mathcal O(D(f))=T_{R_f}\): the structure sheaf is the usual one, with each ring of sections replaced by its generalized ring.

(b) For a monoid \(H\), \(\operatorname{Spec}\mathbb F_1[H]\) is the spectrum of \(H\), with \(\mathcal O(D(f))=\mathbb F_1[H_f]\) by Example 5.3(a). In particular \(\operatorname{Spec}\mathbb F_1\) and \(\operatorname{Spec}\mathbb F_{1^n}\) are one point: the only prime ideal is \(\{0\}\).

(c) \(\operatorname{Spec}\mathbb F_\varnothing\) is one point: \(|\mathbb F_\varnothing|=\{e\}\), and the only prime ideal is the empty ideal.

(d) \(\operatorname{Spec}\mathbb Z_\infty\) has two points. An ideal of \(\mathbb Z_\infty\) is a subset of \([-1,1]\) that is closed under the combinations \(\sum_i\lambda_ix_i\) with \(\sum_i|\lambda_i|\le1\). These subsets are the intervals \([-r,r]\) with \(0\le r\le1\) and \((-r,r)\) with \(0 < r\le1\). The ideal \(\{0\}\) is prime. The ideal \(\mathfrak m=(-1,1)\) is prime, with complement \(\{\pm1\}\). No other ideal \(I\ne[-1,1]\) is prime: it has \(0 < r < 1\), and any \(x\) with \(r < x < \sqrt r\) satisfies \(x\notin I\) and \(x^2\in I\). For \(0 < |f| < 1\) we have \(D(f)=\{\{0\}\}\) and \(\mathcal O(D(f))=T_{\mathbb R}\) by Example 5.3(b). So \(\{0\}\) is an open point with stalk \(\mathbb R\), and \(\mathfrak m\) is a closed point with stalk \(\mathbb Z_\infty\). The spectrum of a discrete valuation ring has the same shape: an open point whose stalk is the fraction field, and a closed point whose stalk is the valuation ring. Here \(\mathbb R\) takes the place of the fraction field and \(\mathbb Z_\infty\) that of the valuation ring.

### Generalized schemes

**Definition 7.8.** (a) A generalized ring \(B\) is *local* if the set of non-invertible elements of \(|B|\) is an ideal. This ideal is then the only maximal ideal; we denote it \(\mathfrak m_B\). A homomorphism \(\varphi:B\to B'\) of local generalized rings is *local* if \(\varphi^{-1}(\mathfrak m_{B'})=\mathfrak m_B\).

(b) A *locally generalized ringed space* is a generalized ringed space all of whose stalks are local. A *morphism* \((f,f^\sharp):(X,\mathcal O_X)\to(Y,\mathcal O_Y)\) consists of a continuous map \(f\) and homomorphisms \(f^\sharp_V:\mathcal O_Y(V)\to\mathcal O_X(f^{-1}V)\) compatible with restrictions, such that the induced homomorphisms of stalks \(\mathcal O_{Y,f(x)}\to\mathcal O_{X,x}\) are local.

(c) A *generalized scheme* is a locally generalized ringed space in which every point has an open neighbourhood isomorphic to \(\operatorname{Spec}A\) for some generalized ring \(A\). Morphisms of generalized schemes are morphisms of locally generalized ringed spaces.

By Theorem 7.6(b), \(\operatorname{Spec}A\) is a locally generalized ringed space, so it is a generalized scheme, called *affine*. An open subspace of a generalized scheme is a generalized scheme, because the sets \(D(f)\cong\operatorname{Spec}A_f\) are a base of \(\operatorname{Spec}A\).

**Theorem 7.9.** Let \((X,\mathcal O_X)\) be a locally generalized ringed space and \(A\) a generalized ring. Sending a morphism \((f,f^\sharp):X\to\operatorname{Spec}A\) to the homomorphism \(f^\sharp_{\operatorname{Spec}A}:A\to\mathcal O_X(X)\) is a bijection from the morphisms of locally generalized ringed spaces \(X\to\operatorname{Spec}A\) to the homomorphisms of generalized rings \(A\to\mathcal O_X(X)\).

**Proof.** Write \(\mathfrak m_x\) for the maximal ideal of \(\mathcal O_{X,x}\) and \(s_x\) for the germ of a section \(s\).

*Step 1.* Let \(W\subseteq X\) be open and \(s\in|\mathcal O_X(W)|\). The set \(W_s\) of all \(x\in W\) with \(s_x\notin\mathfrak m_x\) is open, and \(s\) is invertible in \(|\mathcal O_X(W_s)|\). Indeed, if \(s_x\) is invertible, there are an open neighbourhood \(V\) of \(x\) and \(r\in|\mathcal O_X(V)|\) with \(sr=e\) on \(V\); so \(V\subseteq W_s\). Inverses in a commutative monoid are unique. So these local inverses agree on overlaps, and they glue to an inverse of \(s\) over \(W_s\), because \(\mathcal O_X(1)\) is a sheaf.

*Step 2: every homomorphism comes from a morphism.* Let \(\varphi:A\to\mathcal O_X(X)\). For \(x\in X\) let \(f(x)\) be the set of all \(a\in|A|\) with \(\varphi(a)_x\in\mathfrak m_x\). It is the preimage of the prime ideal \(\mathfrak m_x\) under the homomorphism \(A\to\mathcal O_{X,x}\), so it is a prime ideal. We have \(f^{-1}(D(a))=X_{\varphi(a)}\), which is open; so \(f\) is continuous. By Step 1, \(\varphi(a)\) is invertible over \(X_{\varphi(a)}\). By Theorem 5.2(b) the homomorphism \(A\to\mathcal O_X(X)\to\mathcal O_X(X_{\varphi(a)})\) extends in exactly one way to \(A_a\to\mathcal O_X(f^{-1}D(a))\). By uniqueness these homomorphisms are compatible with restrictions. So they extend from the base to a map of sheaves \(f^\sharp:\mathcal O_{\operatorname{Spec}A}\to f_*\mathcal O_X\) [Stacks, Tag [009O](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sheaves.html#sheaves-lemma-restrict-basis-equivalence)], which is \(\varphi\) on global sections. The map of stalks \(A_{f(x)}\to\mathcal O_{X,x}\) sends \(a/s\) to \(\varphi(s)_x^{-1}\varphi(a)_x\). This lies in \(\mathfrak m_x\) exactly when \(a\in f(x)\). So the map of stalks is local.

*Step 3: the morphism is determined by the homomorphism.* Let \((g,g^\sharp)\) be a morphism with \(g^\sharp_{\operatorname{Spec}A}=\varphi\). For \(x\in X\), the composite \(A\to A_{g(x)}\to\mathcal O_{X,x}\) is \(a\mapsto\varphi(a)_x\). The second map is local, and the preimage of the maximal ideal of \(A_{g(x)}\) in \(|A|\) is \(g(x)\) by Theorem 7.6(b). So \(g(x)=f(x)\). The homomorphism \(g^\sharp_{D(a)}:A_a\to\mathcal O_X(X_{\varphi(a)})\) restricts to \(\varphi\) on \(A\), so it is the homomorphism of Step 2, by Theorem 5.2(b). The sets \(D(a)\) form a base, so \(g^\sharp=f^\sharp\). \(\square\)

*Reference:* for rings this is [Stacks, Tag [01I1](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/schemes.html#schemes-lemma-morphism-into-affine)]; the statement for generalized rings is in [Durov 2007, 6.5.2].

**Corollary 7.10.** (a) \(\operatorname{Hom}(\operatorname{Spec}B,\operatorname{Spec}A)=\operatorname{Hom}(A,B)\): the functor \(\operatorname{Spec}\) is a fully faithful contravariant functor from generalized rings to generalized schemes. For rings \(R\), \(R'\), the morphisms \(\operatorname{Spec}T_{R'}\to\operatorname{Spec}T_R\) are the ring homomorphisms \(R\to R'\); so affine schemes form a full subcategory of generalized schemes.

(b) \(\operatorname{Spec}\mathbb F_\varnothing\) is a final object of the category of generalized schemes. A generalized scheme \(X\) has a morphism to \(\operatorname{Spec}\mathbb F_1\) if and only if \(\mathcal O_X(X)\) has a zero, and then it has exactly one.

(c) A generalized scheme \(X\) has at most one morphism to \(\operatorname{Spec}\mathbb Z\). So \(\operatorname{Spec}\mathbb Z\to\operatorname{Spec}\mathbb F_1\) is a monomorphism of generalized schemes. Consequently the fibre product \(\operatorname{Spec}\mathbb Z\times_{\operatorname{Spec}\mathbb F_1}\operatorname{Spec}\mathbb Z\) exists, and both projections to \(\operatorname{Spec}\mathbb Z\) are isomorphisms: the product is \(\operatorname{Spec}\mathbb Z\), embedded diagonally.

**Proof.** (a) Theorem 7.9 with \(\mathcal O(\operatorname{Spec}B)=B\), and Corollary 2.7(a). (b) \(\mathbb F_\varnothing\) is initial, and Example 3.6. (c) Theorem 7.9 and Corollary 6.3(a). In any category, if \(m:Z\to S\) is a monomorphism, then \(Z\) with the two identity maps is a fibre product \(Z\times_SZ\). \(\square\)

The monomorphism \(\operatorname{Spec}\mathbb Z\to\operatorname{Spec}\mathbb F_1\) is not injective on points: its source has infinitely many points and its target has one.

## 8. The compactification of \(\operatorname{Spec}\mathbb Z\)

A reference for this section is [Durov 2007, 7.1]. The idea is to add to \(\operatorname{Spec}\mathbb Z\) one point \(\infty\) whose local ring is \(\mathbb Z_{(\infty)}\), the unit ball of \(\mathbb Q\), in the same way as the local ring at a prime \(p\) is \(\mathbb Z_{(p)}\). We will see that this cannot be done by a generalized scheme (Theorem 8.8). It can be done by a tower of generalized schemes \(S_N\), in which the local ring at \(\infty\) is only \(A_N=\mathbb Z_{(\infty)}\cap\mathbb Z[1/N]\), and by the limit of the tower, which is a ringed space.

### The generalized rings \(A_N\)

Recall from Example 3.2 that \(A_N(n)\) is the set of \(\lambda\in\mathbb Z[1/N]^n\) with \(\sum_i|\lambda_i|\le1\), and that \(A_1=\mathbb F_{\pm1}\). All generalized rings of this section are subclones of \(T_{\mathbb Q}\).

**Lemma 8.1.** Let \(N\ge2\).

(a) The invertible elements of \(|A_N|=\mathbb Z[1/N]\cap[-1,1]\) are \(\pm1\). The generalized ring \(A_N\) is local, with maximal ideal \(\mathfrak p_\infty=\{\lambda\in|A_N|:|\lambda|<1\}\).

(b) Let \(f\in|A_N|\) with \(0<|f|<1\), and write \(f=a/N^k\) with \(a\in\mathbb Z\). The homomorphism \((A_N)_f\to T_{\mathbb Q}\), \(\lambda/f^j\mapsto f^{-j}\lambda\), is injective, and its image is \(T_{\mathbb Z[1/(Na)]}\). In particular \((A_N)_{1/N}=T_{\mathbb Z[1/N]}\).

(c) The prime ideals of \(A_N\) are \(\{0\}\), \(\mathfrak p_\infty\), and \(\mathfrak p_p=|A_N|\cap p\,\mathbb Z[1/N]\) for the primes \(p\nmid N\). A subset of \(\operatorname{Spec}A_N\) is open if and only if it is empty, or the whole space, or consists of \(\{0\}\) and all but finitely many of the \(\mathfrak p_p\).

(d) \(A_N\) is generated by \(0\), \(-e\) and the operations \(s_m=(\tfrac1m,\dots,\tfrac1m)\in A_N(m)\) with \(m=N^k\), \(k\ge1\).

**Proof.** (a) If \(\lambda\) and \(\lambda^{-1}\) lie in \([-1,1]\), then \(|\lambda|=1\). For \(t\in A_N(n)\) and \(x_i\in\mathfrak p_\infty\) we have \(|\sum_it_ix_i|\le\sum_i|t_i|\cdot\max_i|x_i|<1\), or the sum is \(0\). So \(\mathfrak p_\infty\) is an ideal, and its complement is the set of invertible elements.

(b) The homomorphism exists by Theorem 5.2(b), and it is injective as in Example 5.3(b). Its image lies in \(\mathbb Z[1/N,1/f]^n=\mathbb Z[1/(Na)]^n\). Conversely let \(v\in\mathbb Z[1/(Na)]^n\). For large \(j\), \(f^jv=a^jN^{-kj}v\) lies in \(\mathbb Z[1/N]^n\), and \(|f|^j\sum_i|v_i|\le1\). Then \(f^jv\in A_N(n)\), and \(v\) is the image of \((f^jv)/f^j\).

(c) By Proposition 7.3(b) and (b), the primes of \(A_N\) that do not contain \(1/N\) correspond to the primes of \(\mathbb Z[1/N]\); these are \(0\) and \(p\,\mathbb Z[1/N]\) for \(p\nmid N\), and their preimages are \(\{0\}\) and \(\mathfrak p_p\). Let \(\mathfrak p\) be a prime that contains \(1/N\). Then \(\mathfrak p\subseteq\mathfrak p_\infty\). Let \(\lambda\in\mathfrak p_\infty\) and choose \(j\) with \(|\lambda|^j\le1/N\). Then \(\mu=N\lambda^j\) lies in \(|A_N|\), and \(\lambda^j=\mu\cdot\tfrac1N\in\mathfrak p\). So \(\lambda\in\mathfrak p\), and \(\mathfrak p=\mathfrak p_\infty\). For the topology: \(D(\pm1)\) is the whole space, \(D(0)\) is empty, and for \(f=a/N^k\) with \(0<|f|<1\) the set \(D(f)\) consists of \(\{0\}\) and the \(\mathfrak p_p\) with \(p\nmid a\). Every finite set of primes not dividing \(N\) is the set of such prime divisors of some \(a\), and \(|a/N^k|<1\) for large \(k\).

(d) Let \(\lambda\in A_N(n)\). Write \(\lambda_i=u_i/m\) with \(m=N^k\), \(k\ge1\), \(u_i\in\mathbb Z\) and \(\sum_i|u_i|\le m\). Then \(\lambda=s_m(z_1,\dots,z_m)\), where the list \(z\) contains \(e^n_i\) or \(-e^n_i\), according to the sign of \(u_i\), exactly \(|u_i|\) times, and \(0\) in the remaining places. \(\square\)

So \(\operatorname{Spec}A_N\) has a generic point \(\{0\}\), one closed point \(\mathfrak p_\infty\), and the closure of each \(\mathfrak p_p\) is \(\{\mathfrak p_p,\mathfrak p_\infty\}\).

### The generalized schemes \(S_N\)

Let \(\mathcal P\) be the set of prime numbers and \(\overline{\mathcal P}=\{\xi\}\cup\mathcal P\cup\{\infty\}\). For a subset \(U\subseteq\overline{\mathcal P}\) let \(R(U)\) be the subclone of \(T_{\mathbb Q}\) with
\[
R(U)(n)=\Bigl\{\lambda\in\mathbb Q^n:\ \lambda\in\mathbb Z_{(p)}^n\text{ for all primes }p\in U,\ \text{ and }\sum_i|\lambda_i|\le1\text{ if }\infty\in U\Bigr\}.
\]
It is an intersection of the subclones \(T_{\mathbb Z_{(p)}}\) and \(\mathbb Z_{(\infty)}\), so it is a generalized ring. For example \(R(\{\xi\})=\mathbb Q\), \(R(\{\xi\}\cup\mathcal P)=\mathbb Z\), \(R(\overline{\mathcal P})=\mathbb F_{\pm1}\), and for \(N\ge2\)
\[
R(\{\xi\}\cup\{p: p\nmid N\})=\mathbb Z[1/N],\qquad R(\{\xi,\infty\}\cup\{p: p\nmid N\})=A_N .
\]

For \(N\ge2\) let \(\tau_N\) be the following topology on \(\overline{\mathcal P}\): a set \(U\) is open if it is empty, or if \(\xi\in U\), the complement of \(U\) is finite, and either \(\infty\notin U\) or \(U\) contains all primes \(p\nmid N\). Let \(\tau_\infty\) be the topology whose open sets are the empty set and the sets that contain \(\xi\) and have finite complement. Both are closed under unions and finite intersections. Let \(\mathcal O(U)=R(U)\) for non-empty open \(U\), with the inclusions as restriction maps, and let \(\mathcal O(\varnothing)\) be the trivial generalized ring. Put
\[
S_N=(\overline{\mathcal P},\tau_N,\mathcal O),\qquad\overline{\operatorname{Spec}\mathbb Z}=(\overline{\mathcal P},\tau_\infty,\mathcal O).
\]

**Proposition 8.2.** Let \(N\ge2\).

(a) \(\mathcal O\) is a sheaf of generalized rings on \(S_N\). Its stalks are \(\mathbb Q\) at \(\xi\), \(\mathbb Z_{(p)}\) at \(p\), and \(A_N\) at \(\infty\).

(b) The open subspace \(U_1=\overline{\mathcal P}\smallsetminus\{\infty\}\) is isomorphic to \(\operatorname{Spec}\mathbb Z\), and the open subspace \(U_2=\{\xi,\infty\}\cup\{p: p\nmid N\}\) is isomorphic to \(\operatorname{Spec}A_N\). Their intersection is \(D(N)\subset\operatorname{Spec}\mathbb Z\) and \(D(1/N)\subset\operatorname{Spec}A_N\), and it is isomorphic to \(\operatorname{Spec}\mathbb Z[1/N]\).

(c) \(S_N\) is a generalized scheme: \(\operatorname{Spec}\mathbb Z\) and \(\operatorname{Spec}A_N\) glued along \(\operatorname{Spec}\mathbb Z[1/N]\). Its generalized ring of global sections is \(\mathbb F_{\pm1}\).

**Proof.** (a) All non-empty open sets contain \(\xi\), so they meet, and all restriction maps are inclusions of subsets of \(\mathbb Q^n\). Let \(U=\bigcup_iU_i\) with non-empty open \(U_i\). A compatible family of sections is one element \(\lambda\in\mathbb Q^n\) that lies in every \(R(U_i)(n)\). The conditions that define \(R(U)\) are indexed by the points of \(U\), so \(\bigcap_iR(U_i)=R(U)\). This is the sheaf condition. The stalk at a point is the union of the \(R(U)\) over its neighbourhoods. Every open set that contains \(\infty\) contains \(U_2\), so the stalk at \(\infty\) is \(R(U_2)=A_N\). A vector \(\lambda\in\mathbb Z_{(p)}^n\) lies in \(R(U)\) for the open set \(U\subseteq U_1\) obtained by removing the primes in the denominators of \(\lambda\); so the stalk at \(p\) is \(\mathbb Z_{(p)}\). The stalk at \(\xi\) is \(\mathbb Q\).

(b) The open subsets of \(U_1\) are the empty set and the sets that contain \(\xi\) and all but finitely many primes. So \(\xi\mapsto(0)\), \(p\mapsto(p)\) is a homeomorphism \(U_1\to\operatorname{Spec}\mathbb Z\). For \(m\ne0\) the set \(D(m)\) corresponds to \(U=\{\xi\}\cup\{p: p\nmid m\}\), and \(R(U)=\mathbb Z[1/m]\) is the generalized ring of sections of \(\operatorname{Spec}\mathbb Z\) over \(D(m)\). The restriction maps are inclusions on both sides. Two sheaves that agree on a base are isomorphic [Stacks, Tag [009O](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sheaves.html#sheaves-lemma-restrict-basis-equivalence)]. The open subsets of \(U_2\) are the empty set, \(U_2\), and the sets that consist of \(\xi\) and all but finitely many primes \(p\nmid N\). By Lemma 8.1(c), \(\xi\mapsto\{0\}\), \(p\mapsto\mathfrak p_p\), \(\infty\mapsto\mathfrak p_\infty\) is a homeomorphism \(U_2\to\operatorname{Spec}A_N\). For \(f=a/N^k\) with \(0<|f|<1\), the set \(D(f)\) corresponds to \(U=\{\xi\}\cup\{p: p\nmid Na\}\), and \(R(U)=\mathbb Z[1/(Na)]=(A_N)_f\) by Lemma 8.1(b). Also \(R(U_2)=A_N\). So the sheaves agree on a base. The statement about \(U_1\cap U_2\) is the case \(m=N\), \(f=1/N\).

(c) follows from (b), and \(R(\overline{\mathcal P})(n)\) is the set of \(\lambda\in\mathbb Z^n\) with \(\sum_i|\lambda_i|\le1\). \(\square\)

In \(S_N\) the points \(\infty\) and \(p\mid N\) are closed, and the closure of a prime \(p\nmid N\) is \(\{p,\infty\}\). The local ring at \(\infty\) is \(A_N\), not \(\mathbb Z_{(\infty)}\).

**Proposition 8.3.** Let \(N\) divide \(N'\), with \(N\ge2\).

(a) \(\tau_N\subseteq\tau_{N'}\). The identity map of \(\overline{\mathcal P}\), with the identity maps \(R(U)\to R(U)\) for \(U\in\tau_N\), is a morphism of generalized schemes \(f^{N'}_N:S_{N'}\to S_N\). It is an isomorphism over \(U_1=\operatorname{Spec}\mathbb Z\), and \(f^{N'}_N\circ f^{N''}_{N'}=f^{N''}_N\).

(b) \(f^{N'}_N\) is an isomorphism if and only if \(N\) and \(N'\) have the same prime divisors.

**Proof.** (a) An open set of \(\tau_N\) that contains \(\infty\) contains all \(p\nmid N\), hence all \(p\nmid N'\). The maps of stalks are the identity of \(\mathbb Q\) at \(\xi\), the identity of \(\mathbb Z_{(p)}\) at \(p\), and the inclusion \(A_N\to A_{N'}\) at \(\infty\). The last one is local, because both maximal ideals are given by \(|\lambda|<1\).

(b) If the prime divisors agree, then \(\tau_N=\tau_{N'}\) and \(S_N=S_{N'}\). If a prime \(p\) divides \(N'\) and not \(N\), then \(\{p\}\) is closed in \(S_{N'}\) and not in \(S_N\), so the map is not a homeomorphism. \(\square\)

### The limit

**Theorem 8.4.** (a) \(\tau_\infty\) is the union of the topologies \(\tau_N\). \(\overline{\operatorname{Spec}\mathbb Z}\) is a locally generalized ringed space. All its points except \(\xi\) are closed. Its stalk at \(\infty\) is \(\mathbb Z_{(\infty)}\), its open subspace \(\overline{\mathcal P}\smallsetminus\{\infty\}\) is \(\operatorname{Spec}\mathbb Z\), and \(\mathcal O(\overline{\mathcal P})=\mathbb F_{\pm1}\).

(b) With the morphisms \(g_N:\overline{\operatorname{Spec}\mathbb Z}\to S_N\) given by the identity maps, \(\overline{\operatorname{Spec}\mathbb Z}\) is the limit of the system \((S_N,f^{N'}_N)\) in the category of generalized ringed spaces, and also in the category of locally generalized ringed spaces.

(c) \(\overline{\operatorname{Spec}\mathbb Z}\) is not a generalized scheme: no open neighbourhood of \(\infty\) is isomorphic to the spectrum of a generalized ring.

**Proof.** (a) Let \(U\in\tau_\infty\) contain \(\infty\), with complement \(\{p_1,\dots,p_r\}\). Then \(U\in\tau_N\) for \(N=p_1\cdots p_r\), or for any \(N\) if \(r=0\). The sheaf property is proved as in Proposition 8.2(a). The complement of a point other than \(\xi\) is open. The stalk at \(\infty\) is the union of the \(R(U)\) over the sets \(U\ni\infty\) with finite complement, which is \(\mathbb Z_{(\infty)}\): a vector \(\lambda\in\mathbb Z_{(\infty)}(n)\) lies in \(R(U)\) when \(U\) omits the primes in its denominators. \(\mathbb Z_{(\infty)}\) is local, by the argument of Lemma 8.1(a). The other stalks are as in Proposition 8.2.

(b) Let \(Y\) be a generalized ringed space with morphisms \(h_N:Y\to S_N\) such that \(f^{N'}_N\circ h_{N'}=h_N\). All \(h_N\) have the same underlying map \(h\), because any two of the numbers \(N\) divide a third. The map \(h\) is continuous for every \(\tau_N\), hence for \(\tau_\infty\). For \(U\in\tau_\infty\) choose \(N\) with \(U\in\tau_N\) and let \(h^\sharp_U:R(U)\to\mathcal O_Y(h^{-1}U)\) be the homomorphism that belongs to \(h_N\). By the compatibility it does not depend on \(N\). This defines the only morphism \(Y\to\overline{\operatorname{Spec}\mathbb Z}\) that induces all \(h_N\). If all \(h_N\) are local, so is this morphism: at \(\infty\) the preimage of a maximal ideal \(\mathfrak m_y\) in \(\mathbb Z_{(\infty)}\) meets each \(A_N\) in \(\{|\lambda|<1\}\), so it is \(\{|\lambda|<1\}\).

(c) Let \(U\) be an open neighbourhood of \(\infty\), with complement \(\{p_1,\dots,p_r\}\), and suppose that \((U,\mathcal O|_U)\cong\operatorname{Spec}B\). Taking global sections gives \(B\cong R(U)=A_d\) with \(d=p_1\cdots p_r\). By Lemma 8.1 and Example 7.7(b), \(\operatorname{Spec}A_d\) has exactly one closed point, both for \(d\ge2\) and for \(d=1\). But \(U\) has infinitely many closed points. This is a contradiction. \(\square\)

*Reference:* [Durov 2007, 7.1.14] states (c) without proof. The proof above is for prime spectra.

So the limit of the tower has the local ring \(\mathbb Z_{(\infty)}\) at \(\infty\), and all its points except \(\xi\) are closed. It is a locally generalized ringed space and not a generalized scheme. Theorems 8.8 and 8.9 below show that no generalized scheme can take its place. [Durov 2007, 7.1.13] works with the tower itself: it defines \(\widehat{\operatorname{Spec}\mathbb Z}\) as the pro-object given by the tower \((S_N)\), so that a morphism from a generalized scheme \(T\) to it is a compatible family of morphisms \(T\to S_N\). [Haran 2017, §5.2] does the same in the language of Section 9.

### The square of the compactification

**Lemma 8.5.** Let \(C\) be a generalized ring and \(m\ge1\). Let \(s,s'\in C(m)\) be *symmetric* (\(\sigma_*s=s\) for every permutation \(\sigma\) of \([m]\)) and *idempotent* (\(s(e,\dots,e)=e\) in \(|C|\)). Then \(s=s'\).

**Proof.** In the module \(C(m)\) take the \(m\times m\) matrix whose entry in row \(i\) and column \(j\) is \(e^m_l\) with \(l\equiv i+j\pmod m\). Each row and each column is a permutation of \((e^m_1,\dots,e^m_m)\). By symmetry, \(s\) applied to any row gives \(s\), and \(s'\) applied to any column gives \(s'\). By (C3) and idempotency, \(s'(s,\dots,s)=s'(e,\dots,e)(s)=s\) and \(s(s',\dots,s')=s'\). So (2.1) for \(s'\) and \(s\) reads \(s=s'\). \(\square\)

*Reference:* [Durov 2007, 5.7.3].

**Theorem 8.6.** Let \(N\ge2\).

(a) Two homomorphisms of generalized rings \(A_N\to C\) that agree on \(-e\) are equal. So \(\mathbb F_{\pm1}\to A_N\) is an epimorphism of generalized rings.

(b) Let \(C\) be a ring and \(\delta:A_N\to C\) a homomorphism. Then \(N\cdot\delta(1/N)=1\) in \(C\).

(c) The morphism \(S_N\to\operatorname{Spec}\mathbb F_{\pm1}\) given by \(\mathbb F_{\pm1}=\mathcal O(S_N)\) is a monomorphism of generalized schemes. So the fibre product \(S_N\times_{\operatorname{Spec}\mathbb F_{\pm1}}S_N\) exists and is \(S_N\), embedded diagonally.

**Proof.** (a) Let \(\gamma,\delta:A_N\to C\) agree on \(-e\). They agree on \(0\). For \(m=N^k\), the operations \(\gamma(s_m)\) and \(\delta(s_m)\) are symmetric and idempotent, because \(s_m\) is; so they are equal by Lemma 8.5. By Lemma 8.1(d), \(\gamma=\delta\).

(b) In \(C(N)=C^N\) the operation \(\delta(s_N)\) is a vector \((c_1,\dots,c_N)\). It is symmetric, so all \(c_i\) are equal to one \(c\). It is idempotent, so \(Nc=1\). And \(\delta(1/N)=\delta(s_N(e,0,\dots,0))=c\).

(c) Let \(g,h:X\to S_N\) be morphisms of generalized schemes with the same composite to \(\operatorname{Spec}\mathbb F_{\pm1}\). By Theorem 7.9 this means that \(g^\sharp\) and \(h^\sharp\) agree on the global section \(-e\). The four open sets \(W_{ij}=g^{-1}(U_i)\cap h^{-1}(U_j)\), \(i,j\in\{1,2\}\), cover \(X\). It suffices to show \(g=h\) on each \(W=W_{ij}\). Let \(C=\mathcal O_X(W)\). We use Theorem 7.9 for \(W\) and the affine schemes \(U_1\), \(U_2\), \(U_1\cap U_2\) of Proposition 8.2.

On \(W_{11}\), both \(g\) and \(h\) map to \(U_1=\operatorname{Spec}\mathbb Z\) and correspond to homomorphisms \(\mathbb Z\to C\). There is at most one (Corollary 6.3).

On \(W_{22}\), they map to \(U_2=\operatorname{Spec}A_N\) and correspond to homomorphisms \(A_N\to C\) that agree on \(-e\). These are equal by (a).

On \(W_{12}\), \(g\) corresponds to a homomorphism \(\mathbb Z\to C\), so \(C\) is a ring, and \(h\) corresponds to \(\delta:A_N\to C\). By (b), \(N\) and \(\delta(1/N)\) are invertible in \(C\). By Step 2 of the proof of Theorem 7.9, \(g\) maps \(W\) into \(D(N)\) and \(h\) maps \(W\) into \(D(1/N)\). So both map \(W\) into \(U_1\cap U_2\cong\operatorname{Spec}\mathbb Z[1/N]\), and they correspond to homomorphisms \(\mathbb Z[1/N]\to C\). There is at most one. The case \(W_{21}\) is symmetric.

The last statement holds for every monomorphism, as in Corollary 7.10(c). \(\square\)

*Reference:* [Durov 2007, 7.1.47].

The base \(\mathbb F_{\pm1}\) cannot be replaced by \(\mathbb F_1\): two homomorphisms from \(A_N\) to a generalized ring can differ on \(-e\), the morphism \(S_N\to\operatorname{Spec}\mathbb F_1\) is not a monomorphism, and a fibre product \(S_N\times_{\operatorname{Spec}\mathbb F_1}S_N\) is not isomorphic to \(S_N\) (Exercise 10.8). The module used there is indicated in [Durov 2007, 5.7.4]. [López Peña–Lorscheid 2011a, §1.4] states the collapse of the square for the fibre product over \(\mathbb F_1\).

Theorem 8.6 holds for every stage of the tower. [Durov 2007, 7.1.47] concludes that the square of the pro-object \(\widehat{\operatorname{Spec}\mathbb Z}\) over \(\operatorname{Spec}\mathbb F_{\pm1}\) is \(\widehat{\operatorname{Spec}\mathbb Z}\) itself.

**Example 8.7** (Sections of a line bundle). Let \(\lambda\) be a positive rational number. For a non-empty open set \(U\) of \(\overline{\operatorname{Spec}\mathbb Z}\) let \(L_\lambda(U)\) be the set of \(x\in\mathbb Q\) with \(x\in\mathbb Z_{(p)}\) for all primes \(p\in U\), and \(|x|\le\lambda\) if \(\infty\in U\). For \(\mu\in R(U)(n)\) and \(x_i\in L_\lambda(U)\) we have \(\sum_i\mu_ix_i\in L_\lambda(U)\), so \(L_\lambda(U)\) is a module over \(R(U)\), and \(L_\lambda\) is a sheaf as in Proposition 8.2(a). On \(\overline{\mathcal P}\smallsetminus\{\infty\}\) it is the structure sheaf: \(L_\lambda(U)=R(U)(1)\). On the open set \(V\) obtained by removing the primes that occur in \(\lambda\), multiplication by \(\lambda\) is a bijection \(R(U)(1)\to L_\lambda(U)\) for all \(U\subseteq V\). So \(L_\lambda\) is locally free of rank one. Its global sections are
\[
L_\lambda(\overline{\mathcal P})=\{x\in\mathbb Z:|x|\le\lambda\},
\]
a finite set with \(2\lfloor\lambda\rfloor+1\) elements. If the primes in \(\lambda\) divide \(N\), the same formulas define \(L_\lambda\) on \(S_N\). In [Durov 2007, 7.1.35–7.1.40] this sheaf is called \(\mathcal O(\log\lambda)\), and \(\log\lambda\) is its degree.

### Why a tower is needed

Theorem 8.4(c) says that one particular ringed space is not a generalized scheme. The next two theorems say more: no generalized scheme adds to \(\operatorname{Spec}\mathbb Z\) one point with local ring \(\mathbb Z_{(\infty)}\), and the tower has no limit among generalized schemes.

**Theorem 8.8.** There is no generalized scheme \(X\) with a point \(x\) such that \(X\smallsetminus\{x\}\) is open in \(X\) and isomorphic to \(\operatorname{Spec}\mathbb Z\) as a generalized ringed space, and such that \(\mathcal O_{X,x}\) is isomorphic to \(\mathbb Z_{(\infty)}\).

**Proof.** Suppose that \(X\) and \(x\) exist. Let \(V=\operatorname{Spec}B\) be an affine open neighbourhood of \(x\). For a point \(y\in V\) write \(\mathfrak q_y\) for the corresponding prime ideal of \(B\); so \(\mathcal O_{X,y}=B_{\mathfrak q_y}\) by Theorem 7.6(b). The closure of \(\{y\}\) in \(V\) is the set of all \(z\) with \(\mathfrak q_y\subseteq\mathfrak q_z\), because the sets \(D(f)\) are a base of the topology.

*Step 1: two prime ideals.* The generalized ring \(\mathbb Z_{(\infty)}\) has exactly two prime ideals, \(\{0\}\) and \(\{\lambda:|\lambda| < 1\}\). These two ideals are prime: their complements are the set of non-zero elements and the set \(\{\pm1\}\). Let \(I\) be any ideal different from \(|\mathbb Z_{(\infty)}|=\mathbb Q\cap[-1,1]\), and let \(r\) be the supremum of the \(|\lambda|\) with \(\lambda\in I\). If \(\mu\) is rational and \(|\mu| < |\lambda|\) for some \(\lambda\in I\), then \(\mu=(\mu/\lambda)\lambda\in I\). So \(I\) contains all rational numbers \(\mu\) with \(|\mu| < r\), and \(I\) does not contain \(\pm1\). If \(r=0\), then \(I=\{0\}\). If \(r=1\), then \(I=\{\lambda:|\lambda| < 1\}\). If \(0 < r < 1\), a rational number \(\mu\) with \(r < \mu < \sqrt r\) satisfies \(\mu\notin I\) and \(\mu^2\in I\), so \(I\) is not prime. By Proposition 7.3(b), the prime ideals of \(B_{\mathfrak q_x}\) correspond to the prime ideals of \(B\) that are contained in \(\mathfrak q_x\). So there is exactly one point \(y\ne x\) of \(V\) with \(\mathfrak q_y\subseteq\mathfrak q_x\).

*Step 2: closed points stay closed.* The set \(V\smallsetminus\{x\}\) is an open subset of \(\operatorname{Spec}\mathbb Z\) that contains \(y\). So it contains the generic point \(\xi\) and all but finitely many of the closed points \(p\) of \(\operatorname{Spec}\mathbb Z\). Every point of \(\operatorname{Spec}\mathbb Z\) lies in the closure of \(\xi\). So \(\mathfrak q_\xi\subseteq\mathfrak q_y\subseteq\mathfrak q_x\), and Step 1 gives \(y=\xi\). For a closed point \(p\in V\smallsetminus\{x\}\) we get \(\mathfrak q_p\not\subseteq\mathfrak q_x\): the point \(x\) is not in the closure of \(\{p\}\). Since \(\{p\}\) is closed in \(V\smallsetminus\{x\}\), it is closed in \(V\).

*Step 3: units.* Fix a closed point \(p\in V\smallsetminus\{x\}\). By Step 2 there is \(f\in|B|\) with \(x\in D(f)\) and \(p\notin D(f)\). Since \(f\notin\mathfrak q_x\), the germ of \(f\) at \(x\) is invertible. The invertible elements of \(|\mathbb Z_{(\infty)}|\) are \(\pm1\), so the square of this germ is \(e\). Every open set that contains \(x\) or \(p\) contains \(\xi\). So there are homomorphisms \(\mathcal O_{X,x}\to\mathcal O_{X,\xi}\) and \(\mathcal O_{X,p}\to\mathcal O_{X,\xi}\) that send the germ of a section to its germ at \(\xi\). By the first one, the germ \(b\) of \(f\) at \(\xi\) satisfies \(b^2=e\). The second one is the inclusion \(\mathbb Z_{(p)}\subseteq\mathbb Q\), which is injective. So the germ \(a\) of \(f\) at \(p\) satisfies \(a^2=e\). Hence \(a\) is invertible, and \(f\notin\mathfrak q_p\) by Theorem 7.6(b). This contradicts \(p\notin D(f)\). \(\square\)

In \(S_N\) the local ring at \(\infty\) is \(A_N\), which has infinitely many prime ideals. There Step 1 fails, and the primes \(p\nmid N\) are not closed.

**Theorem 8.9.** The system \((S_N,f^{N'}_N)\) has no limit in the category of generalized schemes.

**Proof.** Write \(\overline S=\overline{\operatorname{Spec}\mathbb Z}\). Suppose that a generalized scheme \(L\) with morphisms \(\pi_N:L\to S_N\) is a limit of the system. By Theorem 8.4(b) there is exactly one morphism of locally generalized ringed spaces \(c:L\to\overline S\) with \(g_N\circ c=\pi_N\) for all \(N\). For every generalized scheme \(T\), the map \(w\mapsto c\circ w\) is a bijection from the morphisms \(T\to L\) to the morphisms \(T\to\overline S\), because both sets are in bijection with the compatible families of morphisms \(T\to S_N\).

*Step 1: the part over \(\operatorname{Spec}\mathbb Z\).* Let \(j:\operatorname{Spec}\mathbb Z\to\overline S\) be the inclusion of the open subspace \(\overline{\mathcal P}\smallsetminus\{\infty\}\). Let \(L'=c^{-1}(\overline{\mathcal P}\smallsetminus\{\infty\})\), an open subscheme of \(L\) with inclusion \(i:L'\to L\), and let \(c':L'\to\operatorname{Spec}\mathbb Z\) be the morphism induced by \(c\); so \(c\circ i=j\circ c'\). There is exactly one \(u:\operatorname{Spec}\mathbb Z\to L\) with \(c\circ u=j\). It maps into \(L'\), so \(u=i\circ u'\) with \(u':\operatorname{Spec}\mathbb Z\to L'\). Inclusions of open subspaces are monomorphisms. From \(j\circ c'\circ u'=c\circ u=j\) we get \(c'\circ u'=\mathrm{id}\). From \(c\circ(i\circ u'\circ c')=j\circ c'=c\circ i\) and the bijection above for \(T=L'\) we get \(i\circ u'\circ c'=i\), so \(u'\circ c'=\mathrm{id}\). Hence \(L'\cong\operatorname{Spec}\mathbb Z\).

*Step 2: morphisms from local spectra.* Let \(C\) be a local generalized ring and \(\mathfrak m\) the closed point of \(\operatorname{Spec}C\). An open set that contains \(\mathfrak m\) is the whole space: if \(\mathfrak m\in D(f)\), then \(f\) is invertible.

(a) Let \(Y\) be a generalized scheme and \(\ell\in Y\). The morphisms \(w:\operatorname{Spec}C\to Y\) with \(w(\mathfrak m)=\ell\) correspond bijectively to the local homomorphisms \(\sigma:\mathcal O_{Y,\ell}\to C\), where \(\sigma\) is the map of stalks of \(w\) at \(\mathfrak m\). Indeed, such a \(w\) maps into an affine open neighbourhood \(\operatorname{Spec}B\) of \(\ell\). By Theorem 7.9 it is given by a homomorphism \(\beta:B\to C\), and \(w(\mathfrak m)=\ell\) means that \(\beta^{-1}(\mathfrak m)\) is the prime ideal \(\mathfrak q_\ell\) of \(\ell\). By Theorem 5.2(b) these \(\beta\) are the local homomorphisms \(B_{\mathfrak q_\ell}\to C\).

(b) The morphisms \(v:\operatorname{Spec}C\to\overline S\) with \(v(\mathfrak m)=\infty\) correspond bijectively to the local homomorphisms \(\rho:\mathbb Z_{(\infty)}\to C\), where \(\rho\) is the map of stalks of \(v\) at \(\mathfrak m\). Indeed, by Theorem 8.4(b) such a \(v\) is a compatible family of morphisms \(v_N:\operatorname{Spec}C\to S_N\) with \(v_N(\mathfrak m)=\infty\). By (a) and Proposition 8.2(a), \(v_N\) is a local homomorphism \(\rho_N:A_N\to C\). By Proposition 8.3(a) the map of stalks of \(f^{N'}_N\) at \(\infty\) is the inclusion \(A_N\subseteq A_{N'}\). So the family is compatible exactly when \(\rho_{N'}\) restricts to \(\rho_N\) for all \(N\mid N'\). These families are the local homomorphisms from \(\mathbb Z_{(\infty)}=\bigcup_NA_N\) to \(C\).

*Step 3: one point over \(\infty\).* For \(\ell\in L\) with \(c(\ell)=\infty\) let \(c_\ell:\mathbb Z_{(\infty)}\to\mathcal O_{L,\ell}\) be the map of stalks of \(c\); it is a local homomorphism. If \(w:\operatorname{Spec}C\to L\) corresponds to the pair \((\ell,\sigma)\) as in (a), then the map of stalks of \(c\circ w\) at \(\mathfrak m\) is \(\sigma\circ c_\ell\). So the bijection \(w\mapsto c\circ w\), with (a) and (b), says: for every local generalized ring \(C\), every local homomorphism \(\rho:\mathbb Z_{(\infty)}\to C\) is \(\sigma\circ c_\ell\) for exactly one pair \((\ell,\sigma)\) with \(c(\ell)=\infty\) and \(\sigma:\mathcal O_{L,\ell}\to C\) local. For \(C=\mathbb Z_{(\infty)}\) and \(\rho=\mathrm{id}\) this gives a pair \((\ell_0,\sigma_0)\) with \(\sigma_0\circ c_{\ell_0}=\mathrm{id}\). Now let \(\ell\) be any point with \(c(\ell)=\infty\), and take \(C=\mathcal O_{L,\ell}\) and \(\rho=c_\ell\). Then \(\rho\) comes from the pair \((\ell,\mathrm{id})\) and from the pair \((\ell_0,c_\ell\circ\sigma_0)\). So \(\ell=\ell_0\) and \(c_{\ell_0}\circ\sigma_0=\mathrm{id}\). Hence \(\ell_0\) is the only point of \(L\) over \(\infty\), and \(c_{\ell_0}:\mathbb Z_{(\infty)}\to\mathcal O_{L,\ell_0}\) is an isomorphism.

*Step 4.* By Steps 1 and 3, \(L\smallsetminus\{\ell_0\}=L'\) is open and isomorphic to \(\operatorname{Spec}\mathbb Z\), and \(\mathcal O_{L,\ell_0}\cong\mathbb Z_{(\infty)}\). This contradicts Theorem 8.8. \(\square\)

*Reference:* [Durov 2007, Overview 0.7.4] states Theorem 8.9 without proof.

### What is proved and what is only constructed

Proved in this lesson, for prime spectra:

- each \(S_N\) is a generalized scheme with \(\mathcal O(S_N)=\mathbb F_{\pm1}\), obtained by gluing \(\operatorname{Spec}\mathbb Z\) and \(\operatorname{Spec}A_N\) (Proposition 8.2);
- the \(S_N\) form a tower in which the maps are bijective and are isomorphisms only when the prime divisors agree (Proposition 8.3);
- the limit of the tower exists as a locally generalized ringed space with local ring \(\mathbb Z_{(\infty)}\) at \(\infty\), and it is not a generalized scheme (Theorem 8.4);
- no generalized scheme consists of \(\operatorname{Spec}\mathbb Z\) and one further point with local ring \(\mathbb Z_{(\infty)}\) (Theorem 8.8), and the tower has no limit in the category of generalized schemes (Theorem 8.9);
- each \(S_N\) is a subobject of the point \(\operatorname{Spec}\mathbb F_{\pm1}\), so the square of \(S_N\) over \(\mathbb F_{\pm1}\) is \(S_N\) (Theorem 8.6); and \(S_N\to\operatorname{Spec}\mathbb F_1\) is not a monomorphism (Exercise 10.8).

Proved in [Durov 2007] and not here:

- \(A_N\) is finitely presented over \(\mathbb F_{\pm1}\): it is generated by the operations \(s_p\) for the primes \(p\mid N\), subject to idempotency, symmetry and the relation \(s_p(x_1,\dots,x_{p-1},-x_{p-1})=s_p(x_1,\dots,x_{p-2},0,0)\) [Theorem 7.1.26];
- every line bundle on \(\operatorname{Spec}A_N\) is trivial [Proposition 7.1.33], and the Picard group of \(S_N\) is the group of positive units of \(\mathbb Z[1/N]\), generated by the classes of \(\mathcal O(\log p)\), \(p\mid N\) [7.1.35];
- \(S_N\) is a projective generalized scheme: it is the projective spectrum of a graded generalized ring [7.1.43–7.1.46];
- a finitely presented sheaf of modules on the pro-object \(\widehat{\operatorname{Spec}\mathbb Z}\) is determined by a finitely generated \(\mathbb Z\)-module, a finitely presented \(\mathbb Z_{(\infty)}\)-module, and an isomorphism between their base changes to \(\mathbb Q\) [7.1.22; essential surjectivity is proved there, the rest is said to be easy to check];
- for a finitely presented closed subscheme of a projective space over \(\widehat{\operatorname{Spec}\mathbb Z}\), every rational point of the generic fibre extends to a unique section, and the degree of the pullback of \(\mathcal O(1)\) along this section is the logarithmic height \(\log\max_i|x_i|\) of the point, for coprime integer coordinates \(x_i\) [Theorem 7.4.4].

Constructed or asserted in [Durov 2007], without proof there:

- the object \(\widehat{\operatorname{Spec}\mathbb Z}\) itself is the tower, by definition [7.1.13]; its Picard group is defined as the colimit of the Picard groups of the \(S_N\), which is the group \(\log\mathbb Q^\times_{>0}\) [7.1.36];
- the statement that the limit ringed space is not a generalized scheme [7.1.14], and the statement that the limit does not exist in the category of generalized schemes [Overview, 0.7.4]; for prime spectra both are proved above (Theorems 8.4(c) and 8.9);
- the statement that the transition maps \(f^{N'}_N\) are projective morphisms: it is asserted in [Overview, 0.7.3 and 0.7.11], and in [7.1.48] it is accepted without proof;
- the equivalence of the pro-object and the ringed space for categories of finitely presented objects other than sheaves of modules [7.1.17].

The square of \(\operatorname{Spec}\mathbb Z\) in this theory is \(\operatorname{Spec}\mathbb Z\). By Corollary 6.3(a) every generalized ring receives at most one homomorphism from \(\mathbb Z\). So the product of \(\operatorname{Spec}\mathbb Z\) with itself is \(\operatorname{Spec}\mathbb Z\), over \(\mathbb F_1\) (Corollary 7.10(c)) and, by the same proof, over every other base. By Theorem 8.6 the product of \(S_N\) with itself over \(\mathbb F_{\pm1}\) is \(S_N\). So generalized rings supply bases that map to \(\mathbb Z\), namely \(\mathbb F_\varnothing\), \(\mathbb F_1\) and \(\mathbb F_{\pm1}\), and a point at infinity with a notion of degree and height. They do not supply a product \(\operatorname{Spec}\mathbb Z\times\operatorname{Spec}\mathbb Z\) that is larger than the diagonal, and this product is where the argument of *Weil's proof for curves and what is missing over the integers* takes place.

## 9. The relation to the \(\mathbb F\)-rings of Haran

[Haran 2017] replaces a ring by the category of all its matrices. We state and prove the exact relation between the objects of that work and generalized rings.

Let \(\mathbb F\) be the category whose objects are the finite sets and whose morphisms \(X\to Y\) are the *partial bijections*: the bijections \(\varphi:D\to I\) with \(D\subseteq X\) and \(I\subseteq Y\). To avoid a proper class of objects, [Haran 2017, §1.1] fixes a countable set of finite sets that contains all \([n]\); we assume that it is closed under disjoint unions and products. The disjoint union \(\oplus\) makes \(\mathbb F\) a symmetric monoidal category with unit \(\varnothing\). For \(x\in X\) let \(j_x:[1]\to X\) be the map with value \(x\).

**Definition 9.1** ([Haran 2017, Definitions 1.2.1, 1.2.2 and 1.3.1]). An *\(\mathbb F\)-ring* is a category \(\mathcal A\) with the same objects as \(\mathbb F\), together with a faithful functor \(\varepsilon:\mathbb F\to\mathcal A\) that is the identity on objects and a symmetric monoidal structure \(\oplus\) on \(\mathcal A\) for which \(\varepsilon\) is strict monoidal, such that \(\varnothing\) is an initial and a final object of \(\mathcal A\). Strict monoidal means here: on objects \(\oplus\) is the disjoint union, \(\varepsilon(\varphi\oplus\varphi')=\varepsilon(\varphi)\oplus\varepsilon(\varphi')\), and the associativity, commutativity and unit isomorphisms of \(\mathcal A\) are the images under \(\varepsilon\) of those of \(\mathbb F\). One writes \(\mathcal A_{Y,X}\) for the set of morphisms \(X\to Y\). A *homomorphism* of \(\mathbb F\)-rings is a strict monoidal functor that commutes with the functors from \(\mathbb F\). An \(\mathbb F\)-ring is *totally commutative* if for all \(a\in\mathcal A_{Y,X}\) and \(b\in\mathcal A_{J,I}\)
\[
\Bigl(\bigoplus_Ja\Bigr)\circ\Bigl(\bigoplus_Xb\Bigr)=\Bigl(\bigoplus_Yb\Bigr)\circ\Bigl(\bigoplus_Ia\Bigr)\qquad\text{in }\mathcal A_{Y\times J,\,X\times I},
\]
where \(\bigoplus_Ja:X\times J\to Y\times J\) is the sum of \(J\) copies of \(a\), and similarly for the other terms.

[Haran 2017, Definition 1.3.1] calls an \(\mathbb F\)-ring *commutative* under a weaker condition, which involves \(a\in\mathcal A_{Y,X}\), \(b\in\mathcal A_{[1],J}\) and \(d\in\mathcal A_{J,[1]}\) only. Totally commutative \(\mathbb F\)-rings are commutative.

Now let \(A\) be a clone with exactly one constant \(0\). Let \(K(A)\) be the category whose objects are the finite sets and whose morphisms \(X\to Y\) are the homomorphisms of \(A\)-modules \(A(X)\to A(Y)\) between free modules. By freeness,
\[
K(A)_{Y,X}=\operatorname{Hom}_A(A(X),A(Y))=A(Y)^X ,
\]
a matrix with one column in \(A(Y)\) for each \(x\in X\). For a partial bijection \(\varphi\) let \(\varepsilon(\varphi):A(X)\to A(Y)\) be the homomorphism with \(\{x\}\mapsto\{\varphi(x)\}\) if \(\varphi(x)\) is defined and \(\{x\}\mapsto0\) otherwise. The module \(A(X\sqcup X')\) is a coproduct of \(A(X)\) and \(A(X')\), because homomorphisms out of it are maps out of \(X\sqcup X'\). For morphisms \(a\), \(a'\) let \(a\oplus a'\) be the induced homomorphism between the coproducts.

**Theorem 9.2.** Let \(A\) be a clone with exactly one constant \(0\), and with \(e\ne0\).

(a) \(K(A)\) is an \(\mathbb F\)-ring.

(b) For two such clones \(A\), \(A'\), the homomorphisms of \(\mathbb F\)-rings \(K(A)\to K(A')\) correspond bijectively to the homomorphisms of clones \(A\to A'\).

(c) An \(\mathbb F\)-ring \(\mathcal A\) is isomorphic to \(K(A)\) for some such clone \(A\) if and only if, for all \(X\) and \(Y\), the map
\[
\mathcal A_{Y,X}\to(\mathcal A_{Y,[1]})^X,\qquad a\mapsto\bigl(a\circ\varepsilon(j_x)\bigr)_{x\in X},
\]
is bijective.

(d) \(K(A)\) is totally commutative if and only if \(A\) is commutative.

So \(K\) is an equivalence from the category of non-trivial generalized rings with zero to the category of totally commutative \(\mathbb F\)-rings that satisfy the condition of (c).

**Proof.** (a) Since \(\oplus\) is a coproduct of modules, it is a functor, and the bijections of sets that express the associativity, the commutativity and the unit of the disjoint union are natural for all morphisms of \(K(A)\). So \(\oplus\) is a symmetric monoidal structure with unit \(\varnothing\). The rule \(\varepsilon\) is a functor, because homomorphisms preserve \(0\); it is strict monoidal by definition. The elements \(0\) and \(\{y\}\), \(y\in Y\), of \(A(Y)\) are pairwise distinct: the homomorphism \(A(Y)\to A(1)\) with \(\{y\}\mapsto e\) and \(\{y'\}\mapsto0\) for \(y'\ne y\) separates \(\{y\}\) from the others, because \(e\ne0\). So \(\varepsilon\) is faithful. The module \(A(\varnothing)=A(0)\) is one point. So there is exactly one homomorphism \(A(\varnothing)\to A(Y)\), and \(K(A)_{\varnothing,X}=A(0)^X\) is one point: \(\varnothing\) is initial and final.

(b) A homomorphism of clones \(\rho\) gives the maps \(\rho_Y:A(Y)\to A'(Y)\) of Theorem 1.8(c), and \(a\mapsto(\rho_Y(a(x)))_x\) is a homomorphism of \(\mathbb F\)-rings \(K(A)\to K(A')\), because \(\rho\) is compatible with substitution. Conversely let \(\Phi:K(A)\to K(A')\) be a homomorphism of \(\mathbb F\)-rings, and let \(\rho_n\) be its restriction to \(K(A)_{[n],[1]}=A(n)\). Then \(\rho_n(e^n_i)=e^n_i\), because \(e^n_i=\varepsilon(j_i)\). For \(t\in A(k)\) and \(t_i\in A(n)\), the operation \(t(t_1,\dots,t_k)\) is the composite \(\tau\circ t\), where \(\tau\in K(A)_{[n],[k]}\) has the columns \(\tau\circ\varepsilon(j_i)=t_i\). Since \(\Phi(\tau)\circ\varepsilon(j_i)=\Phi(t_i)\), we get \(\rho_n(t(t_1,\dots,t_k))=\rho_k(t)(\rho_n(t_1),\dots,\rho_n(t_k))\). So \(\rho\) is a homomorphism of clones, and the same computation shows that \(\Phi\) is the functor defined by \(\rho\).

(c) For \(K(A)\) the map is the identity of \(A(Y)^X\). Conversely let \(\mathcal A\) satisfy the condition. Put \(A(n)=\mathcal A_{[n],[1]}\) and \(e^n_i=\varepsilon(j_i)\), and for \(t\in A(k)\), \(t_i\in A(n)\) put \(t(t_1,\dots,t_k)=\tau\circ t\), where \(\tau\in\mathcal A_{[n],[k]}\) is the only morphism with \(\tau\circ\varepsilon(j_i)=t_i\) for all \(i\). (C1) holds by the choice of \(\tau\). (C2) holds because \(\tau\) is the identity when \(t_i=\varepsilon(j_i)\). For (C3), let \(\sigma\in\mathcal A_{[m],[n]}\) have the columns \(s_j\). Then \(\sigma\circ\tau\) has the columns \(\sigma\circ t_i=t_i(s_1,\dots,s_n)\), so both sides of (C3) are \(\sigma\circ\tau\circ t\). The set \(A(0)=\mathcal A_{\varnothing,[1]}\) is one point because \(\varnothing\) is final. The element \(0\in A(1)\) is the composite \([1]\to\varnothing\to[1]\), which is \(\varepsilon\) of the empty partial bijection; it is different from \(e=\varepsilon(\mathrm{id})\) because \(\varepsilon\) is faithful. The given bijections identify \(\mathcal A_{Y,X}\) with \(A(Y)^X=K(A)_{Y,X}\). They respect composition, by the definition of substitution. They respect \(\varepsilon\), because \(\varepsilon(\varphi)\circ\varepsilon(j_x)\) is \(\varepsilon(j_{\varphi(x)})\) or the morphism through \(\varnothing\). They respect \(\oplus\): let \(i_X:X\to X\sqcup X'\) and \(i_Y:Y\to Y\sqcup Y'\) be the inclusions. In \(\mathbb F\) we have \(i_X=\mathrm{id}_X\oplus o\) with \(o: \varnothing\to X'\), and functoriality of \(\oplus\) gives \((a\oplus a')\circ\varepsilon(i_X)=a\oplus(a'\circ\varepsilon(o))=\varepsilon(i_Y)\circ a\), because \(\varnothing\) is initial. So the columns of \(a\oplus a'\) over \(X\) are those of \(a\), moved into \(Y\sqcup Y'\). This is the sum in \(K(A)\).

(d) Let \(a\in K(A)_{Y,X}\) and \(b\in K(A)_{J,I}\), and put \(s=a(x)\in A(Y)\), \(t=b(i)\in A(J)\). Apply both sides of the identity to the generator \(\{(x,i)\}\). On the left, \(\bigoplus_Xb\) sends it to \(t\) applied to the generators \(\{(x,j)\}\), \(j\in J\), and \(\bigoplus_Ja\) sends \(\{(x,j)\}\) to \(s\) applied to the generators \(\{(y,j)\}\), \(y\in Y\). On the right, \(\bigoplus_Ia\) sends \(\{(x,i)\}\) to \(s\) applied to the \(\{(y,i)\}\), and \(\bigoplus_Yb\) sends \(\{(y,i)\}\) to \(t\) applied to the \(\{(y,j)\}\). So the two sides are the two sides of (2.1) for \(s\), \(t\) and the matrix of the generators \(\{(y,j)\}\) of \(A(Y\times J)\). Every pair of operations occurs, with \(X=I=[1]\). \(\square\)

*Reference:* [Haran 2017, Introduction] says that the generalized rings of [Durov 2007] are a subset of the \(\mathbb F\)-rings of an earlier work of the same author, and that those are the totally commutative \(\mathbb F\)-rings of the present definition. Theorem 9.2 is the exact statement for Definition 9.1. It needs a zero: \(\mathbb F_\varnothing\) and the other generalized rings without zero give no \(\mathbb F\)-ring, because there is no morphism to which the empty partial bijection could be sent. [López Peña–Lorscheid 2011a, §2.6] takes as morphisms \(X\to Y\) the maps \(T(f)\) for maps of sets \(f:X\to Y\); for \(T=T_R\) this gives only the matrices of maps of sets, not all matrices over \(R\), so we take all homomorphisms \(A(X)\to A(Y)\). [Durov 2007, 5.3.25] makes the comparison for an earlier definition of \(\mathbb F\)-rings, which includes a second product.

**Proposition 9.3.** (a) For a semiring \(R\) with \(1\ne0\), \(K(T_R)\) is the \(\mathbb F\)-ring \(\mathbb F(R)\) of all matrices over \(R\) of [Haran 2017, Definition 2.1.3].

(b) \(K(\mathbb F_1)\) is the \(\mathbb F\)-ring of finite sets and partial maps of [Haran 2017, Definition 2.3.1]. The \(\mathbb F\)-ring \(\mathbb F\) itself is not of the form \(K(A)\). More generally, for a monoid \(H\ne\{0\}\), the \(\mathbb F\)-ring \(\mathbb F\{H\}\) of [Haran 2017, Definition 2.2.1] consists of the matrices over \(H\) with at most one non-zero entry in each row and in each column. It is a proper sub-\(\mathbb F\)-ring of \(K(\mathbb F_1[H])\), which consists of the matrices with at most one non-zero entry in each column, and it is not of the form \(K(A)\).

(c) For \(1\le p\le\infty\), let \(\mathcal O^{1/p}\) be the \(\mathbb F\)-ring of [Haran 2017, Definition 2.4.1] for the real numbers: its morphisms are the real matrices \(a\) with \(|av|_p\le|v|_p\) for all \(v\), where \(|\cdot|_p\) is the \(\ell^p\) norm. Then \(\mathcal O^{1}=K(\mathbb Z_\infty)\), and \(\mathcal O^{1/p}\) is not of the form \(K(A)\) for \(p>1\).

**Proof.** (a) Homomorphisms \(R^{(X)}\to R^{(Y)}\) are matrices, composition is the matrix product, and \(\oplus\) is the block sum.

(b) \(K(\mathbb F_1)_{Y,X}\) is the set of maps from \(X\) to \(\{0\}\sqcup Y\). In \(\mathbb F\{H\}\), for \(X=[2]\) and \(Y=[1]\), the map of Theorem 9.2(c) goes from the rows \((a,0)\), \((0,b)\) to the set \(H^2\). It is not surjective: \((1,1)\) is not in the image. The case \(H=\{0,1\}\) is \(\mathbb F\).

(c) A matrix has operator norm at most \(1\) for the \(\ell^1\) norms exactly when each of its columns has \(\ell^1\) norm at most \(1\), that is, lies in \(\mathbb Z_\infty(Y)\). For \(p>1\) take \(X=[2]\), \(Y=[1]\). The row \((1,1)\) has both columns in the unit ball \([-1,1]=\mathcal O^{1/p}_{[1],[1]}\), and its operator norm is \(2^{1-1/p}>1\). So the map of Theorem 9.2(c) is not surjective. \(\square\)

So the field with one element of [Haran 2017], the category \(\mathbb F\), is not the \(\mathbb F_1\) of this lesson: \(\mathbb F_1\) corresponds to partial maps, not to partial bijections. And at the real prime [Haran 2017, Definition 2.4.2] uses the \(\ell^2\) norm, which has a transpose; by Proposition 9.3(c) the monad condition forces the \(\ell^1\) norm. With the \(\ell^2\) norm, [Haran 2017, §5.2] builds a compactification of \(\operatorname{Spec}\mathbb Z\) as a pro-object in the same way as in Section 8.

The two theories differ on products in the following way.

**Theorem 9.4** ([Haran 2017, Theorem 2.9.1]). Let \(\mathcal L\) be the coproduct of two copies of \(\mathbb F(\mathbb N)\) in the category of \(\mathbb F\)-rings. (1) The largest totally commutative quotient of \(\mathcal L\) is \(\mathbb F(\mathbb N)\). (2) The canonical map from the largest commutative quotient of \(\mathcal L\) to \(\mathbb F(\mathbb N)\) is not an isomorphism.

We do not prove this theorem. [Haran 2017] proves part (1) already for the largest quotient that satisfies a weaker condition, called 1-commutativity there; the proof is the argument of Theorem 2.6(a). Part (1) agrees with \(\mathbb N\otimes_{\mathbb F_1}\mathbb N=\mathbb N\) (Corollary 6.3). Part (2) says that the weaker commutativity of [Haran 2017] allows a product of \(\mathbb N\) with itself that is larger than the diagonal. Finally, Part II of [Haran 2017] uses the words "generalized ring" for another structure (its Definition 8.1.1); it is not the notion of this lesson.

## 10. Exercises

**Exercise 10.1** (Tensor products of monoids). For monoids \(H\) and \(H'\) let \(H\wedge H'\) be the set of pairs \((a,b)\in H\times H'\), in which all pairs with \(a=0\) or \(b=0\) are identified with one element \(0\). It is a monoid under \((a,b)(a',b')=(aa',bb')\). Show that \(\mathbb F_1[H]\otimes_{\mathbb F_1}\mathbb F_1[H']=\mathbb F_1[H\wedge H']\). Deduce that \(\mathbb F_{\pm1}\otimes_{\mathbb F_1}\mathbb F_{\pm1}\) has five unary operations and that \(\mathbb F_1\to\mathbb F_{\pm1}\) is not an epimorphism of generalized rings.

**Solution.** The monoid homomorphisms \(a\mapsto(a,1)\) and \(b\mapsto(1,b)\) give homomorphisms \(i\) and \(j\) into \(\mathbb F_1[H\wedge H']\), by Proposition 3.4(c). Let \(D\) be a generalized ring with homomorphisms \(f:\mathbb F_1[H]\to D\) and \(g:\mathbb F_1[H']\to D\). Then \(D\) has a zero, and \(f\), \(g\) are given by monoid homomorphisms \(\psi:H\to|D|\) and \(\psi':H'\to|D|\). Since \(|D|\) is commutative and \(0\) is absorbing, \((a,b)\mapsto\psi(a)\psi'(b)\) is a well-defined monoid homomorphism \(H\wedge H'\to|D|\). It is the only one that restricts to \(\psi\) and \(\psi'\), because \((a,b)=(a,1)(1,b)\). By Proposition 3.4(c) it is the only homomorphism \(h\) with \(hi=f\) and \(hj=g\). For \(H=H'=\{0,1,-1\}\) the monoid \(H\wedge H'\) has the five elements \(0\) and \((\pm1,\pm1)\). The homomorphisms \(i\) and \(j\) from \(\mathbb F_{\pm1}\) are different: they send \(-1\) to \((-1,1)\) and to \((1,-1)\). They agree on \(\mathbb F_1\). So \(\mathbb F_1\to\mathbb F_{\pm1}\) is not an epimorphism. Exercise 10.8 shows the same for \(\mathbb F_1\to A_N\).

**Exercise 10.2** (Dyadic midpoints). Let \(D\) be the subclone of \(T_{\mathbb Q}\) generated by the binary operation \(m=(\tfrac12,\tfrac12)\).

(a) Show that \(D(n)\) is the set of all \(\lambda\in\mathbb Z[1/2]^n\) with \(\lambda_i\ge0\) and \(\sum_i\lambda_i=1\).

(b) Show that \(D\) is a generalized ring without zero, that \(|D|=\{e\}\), and that \(\operatorname{Spec}D\) is one point.

(c) Show that every join-semilattice is a \(D\)-module under \(\lambda(x_1,\dots,x_n)=\sup\{x_i:\lambda_i>0\}\), and that the empty set is a \(D\)-module.

**Solution.** (a) The sets in the statement contain the basis vectors and \(m\), and they are closed under substitution: \(\sum_i\lambda_i\mu^i\) has non-negative entries in \(\mathbb Z[1/2]\) with sum \(\sum_i\lambda_i=1\). So they form a subclone that contains \(D\). Conversely let \(\lambda_i=a_i/2^k\) with integers \(a_i\ge0\) and \(\sum_ia_i=2^k\). We show \(\lambda\in D(n)\) by induction on \(k\). If \(k=0\), then \(\lambda=e^n_i\). If \(k\ge1\), write down the list in which the index \(i\) occurs \(a_i\) times and cut it into two halves of length \(2^{k-1}\). The halves define \(\lambda'\) and \(\lambda''\) with denominator \(2^{k-1}\), and \(\lambda=m(\lambda',\lambda'')\).

(b) \(D\) is commutative because it is a subclone of \(T_{\mathbb Q}\). \(D(0)\) is empty, because the empty sum is not \(1\). \(D(1)=\{1\}\). The ideals are the submodules of \(\{e\}\): the empty set and \(\{e\}\). The empty ideal is prime, and it is the only prime ideal.

(c) (M1) is clear. For (M2), note that the entries are non-negative, so the support of \(\sum_i\lambda_i\mu^i\) is the union of the supports of the \(\mu^i\) with \(\lambda_i>0\). So both sides of (M2) are the supremum of the \(x_j\) with \(j\) in this union. All operations of \(D\) have at least one argument, so the conditions (M1) and (M2) are empty for the empty set. A two-element chain \(a < b\) is therefore a \(D\)-module. It is not a convex subset of a vector space over \(\mathbb Q\) with the induced operations: there \(m(x,y)=y\) implies \(x=y\), and in the chain \(m(a,b)=b\).

**Exercise 10.3** (\(\mathbb Z\otimes_{\mathbb F_1}\mathbb Z_\infty=\mathbb R\)). Show that \(T_{\mathbb R}\), with the inclusions of \(T_{\mathbb Z}\) and \(\mathbb Z_\infty\), is a pushout of \(T_{\mathbb Z}\leftarrow\mathbb F_1\to\mathbb Z_\infty\) in the category of generalized rings.

**Solution.** Let \(D\) be a generalized ring with homomorphisms \(\gamma:T_{\mathbb Z}\to D\) and \(\delta:\mathbb Z_\infty\to D\). By Corollary 2.7, \(D=T_{R''}\) for a ring \(R''\). Let \(s=(\tfrac12,\tfrac12)\in\mathbb Z_\infty(2)\) and \(\delta(s)=(c_1,c_2)\in R''^2\). Since \(s\) is symmetric, \(c_1=c_2=c\). Since \(s(e,e)=e\), \(2c=1\). And \(\delta(\tfrac12)=\delta(s(e,0))=c\). So \(\delta(\tfrac12)\) is invertible in \(R''\). By Theorem 5.2(b), \(\delta\) extends in exactly one way to a homomorphism \(h\) from \((\mathbb Z_\infty)_{1/2}\) to \(D\), and \((\mathbb Z_\infty)_{1/2}=T_{\mathbb R}\) by Example 5.3(b). The restriction of \(h\) to \(T_{\mathbb Z}\) is \(\gamma\), because there is only one homomorphism \(T_{\mathbb Z}\to D\) (Corollary 6.3). So \(h\) is the only homomorphism \(T_{\mathbb R}\to D\) that restricts to \(\gamma\) and \(\delta\). The same proof gives \(\mathbb Z\otimes_{\mathbb F_1}\mathbb Z_{(\infty)}=\mathbb Q\). The base was not used: \(\mathbb F_1\) can be replaced by \(\mathbb F_\varnothing\) or by \(\mathbb F_{\pm1}\).

*Reference:* [Durov 2007, 5.7.5], for the base \(\mathbb F_{\pm1}\).

**Exercise 10.4** (The Boolean semiring). Let \(\mathbb B=\{0,1\}\) with \(1+1=1\).

(a) Show that the \(T_{\mathbb B}\)-modules are the join-semilattices with a least element.

(b) Show that \(\mathbb B\otimes_{\mathbb F_1}\mathbb B=\mathbb B\) and that \(\mathbb B\otimes_{\mathbb F_1}\mathbb Z\) is the trivial generalized ring.

**Solution.** (a) By Example 1.6(a) a module is a commutative monoid \((M,+,0)\) with \(x+x=(1+1)x=x\). Put \(x\le y\) if \(x+y=y\). This is a partial order in which \(x+y\) is the supremum and \(0\) the least element. Conversely a join-semilattice with least element is such a monoid.

(b) Let \(D\) receive two homomorphisms from \(T_{\mathbb B}\). By Corollary 2.7, \(D=T_{R''}\) for a semiring \(R''\), and the homomorphisms are semiring homomorphisms \(\mathbb B\to R''\). There is at most one, since \(0\mapsto0\) and \(1\mapsto1\). So \(T_{\mathbb B}\) with the identity maps is the pushout. Now let \(D\) receive homomorphisms from \(T_{\mathbb B}\) and \(T_{\mathbb Z}\). Then \(R''\) is a ring in which \(1+1=1\). So \(1=0\) in \(R''\), and \(D\) is trivial. The trivial generalized ring \(\mathbf 1\) receives exactly one homomorphism from every generalized ring, and it has exactly one homomorphism to \(D=\mathbf 1\). So \(\mathbf 1\) is the pushout. Its spectrum is empty (Proposition 7.3(d)): \(\operatorname{Spec}\mathbb B\) and \(\operatorname{Spec}\mathbb Z\) have empty product over \(\operatorname{Spec}\mathbb F_1\).

**Exercise 10.5** (Surjections do not give closed maps). Let \(H=\{0,1,T,T^2,\dots\}\) be the free monoid on one generator \(T\) with a zero adjoined, and \(\mathbb F_1[T]=\mathbb F_1[H]\).

(a) Show that \(\operatorname{Spec}\mathbb F_1[T]\) has two points, \(\{0\}\) and \((T)=H\smallsetminus\{1\}\), and that \(\{0\}\) is open and not closed.

(b) Let \(\zeta\) generate \(\mu_n\). Show that there is a homomorphism \(\pi:\mathbb F_1[T]\to\mathbb F_{1^n}\) with \(T\mapsto\zeta\), surjective in every arity, and that the image of \(\operatorname{Spec}\mathbb F_{1^n}\to\operatorname{Spec}\mathbb F_1[T]\) is not closed.

**Solution.** (a) An ideal is a set \(I\ni0\) with \(TI\subseteq I\). So the ideals are \(I_r=\{0\}\cup\{T^k:k\ge r\}\) for \(r\ge0\), and \(\{0\}\). The complement of \(I_r\) is a submonoid only for \(r=1\), and the complement of \(\{0\}\) is a submonoid. So the prime ideals are \(\{0\}\) and \(I_1=(T)\). We have \(D(T)=\{\{0\}\}\), so \(\{0\}\) is open. Every non-empty closed set contains \((T)\), because the only open set containing \((T)\) is the whole space. So \(\{0\}\) is not closed.

(b) By Proposition 3.4(c), the monoid homomorphism \(T^k\mapsto\zeta^k\), \(0\mapsto0\), gives \(\pi\), and \(\pi(T^k e^m_i)=\zeta^ke^m_i\) shows that it is surjective. \(\operatorname{Spec}\mathbb F_{1^n}\) is the point \(\{0\}\). Its image is the preimage of \(\{0\}\) under \(H\to\{0\}\cup\mu_n\), which is \(\{0\}\). By (a) this point is not closed. For rings, a surjective homomorphism induces a closed embedding of spectra; for generalized rings it need not.

*Reference:* [Durov 2007, 6.2.13].

**Exercise 10.6** (The tensor square of \(\mathbb Z_{(\infty)}\)). Show that \(\mathbb F_{\pm1}\to\mathbb Z_{(\infty)}\) is an epimorphism of generalized rings, so that \(\mathbb Z_{(\infty)}\otimes_{\mathbb F_{\pm1}}\mathbb Z_{(\infty)}=\mathbb Z_{(\infty)}\).

**Solution.** As in Lemma 8.1(d), every \(\lambda\in\mathbb Z_{(\infty)}(n)\) has the form \(s_m(z_1,\dots,z_m)\), where \(m\) is a common denominator, \(s_m=(\tfrac1m,\dots,\tfrac1m)\), and each \(z_l\) is \(0\) or \(\pm e^n_i\). So \(\mathbb Z_{(\infty)}\) is generated by \(0\), \(-e\) and the operations \(s_m\), \(m\ge1\). Let \(\gamma,\delta:\mathbb Z_{(\infty)}\to C\) be homomorphisms of generalized rings that agree on \(-e\). They agree on \(0\). The operations \(\gamma(s_m)\) and \(\delta(s_m)\) are symmetric and idempotent, so they are equal by Lemma 8.5. Hence \(\gamma=\delta\). Therefore \(\mathbb Z_{(\infty)}\) with the identity maps has the universal property of the pushout. This is [Durov 2007, 5.7.3].

**Exercise 10.7** (Transposition). For an \(\mathbb F\)-ring \(\mathcal A\), the opposite category \(\mathcal A^{op}\), with the functor \(\varphi\mapsto\varepsilon(\varphi^{-1})\) and the same \(\oplus\), is again an \(\mathbb F\)-ring [Haran 2017, §1.2]. Let \(A\) be a non-trivial generalized ring with zero. Show that \(K(A)^{op}\) satisfies the condition of Theorem 9.2(c) if and only if \(A\) is a semiring. Conclude that \(K(\mathbb Z_\infty)\) and \(K(\mathbb F_1)\) are not isomorphic to their opposites.

**Solution.** A morphism \(X\to Y\) of \(K(A)^{op}\) is a homomorphism \(a:A(Y)\to A(X)\), that is, a family of elements of \(A(X)\) indexed by \(Y\). The map of Theorem 9.2(c) for \(K(A)^{op}\) sends \(a\) to the family \((\pi_x\circ a)_{x\in X}\), where \(\pi_x=\varepsilon(j_x^{-1}):A(X)\to A(1)\) is the homomorphism with \(\{x\}\mapsto e\) and \(\{x'\}\mapsto0\) for \(x'\ne x\). So the condition says that for every finite set \(X\) the map \(A(X)\to|A|^X\), \(t\mapsto(\pi_x(t))_x\), is bijective. For \(X=[n]\) this is the map \(t\mapsto(\lambda_i(t))_i\) of Theorem 2.6(b). If \(A\) is a semiring it is bijective. Conversely, if it is surjective for \(n=2\), there is \(p\in A(2)\) with \(p(e,0)=e=p(0,e)\), and \(A\) is a semiring by Theorem 2.6. An isomorphism of \(\mathbb F\)-rings between \(K(A)\) and \(K(A)^{op}\) would carry the condition from \(K(A)\) to \(K(A)^{op}\). Since \(\mathbb Z_\infty\) and \(\mathbb F_1\) have no addition (Example 3.2; \(\mathbb F_1(2)\) has three elements and \(|\mathbb F_1|^2\) has four), there is none. So among the \(\mathbb F\)-rings that come from generalized rings, only the semirings admit a transposition.

**Exercise 10.8** (Two signs: the base \(\mathbb F_1\) is not enough). Let \(B\) be one of the generalized rings \(A_N\) with \(N\ge2\), \(\mathbb Z_{(\infty)}\) or \(\mathbb Z_\infty\). Let \(W\) be a set and \(\nu:W\to W\) a map with \(\nu(\nu(w))=w\) and \(\nu(w)\ne w\) for all \(w\in W\). Put \(M=W\sqcup\{0\}\). For \(w\in W\) write \(1\ast w=w\) and \((-1)\ast w=\nu(w)\). For \(t\in B(n)\) and \(x\in M^n\) define \([t]_\nu(x)\in M\) by the following rule: \([t]_\nu(x)=w\in W\) if \(\sum_i|t_i|=1\) and \(x_i=\operatorname{sgn}(t_i)\ast w\) for all \(i\) with \(t_i\ne0\); and \([t]_\nu(x)=0\) if there is no such \(w\). For \(W=\{1,-1\}\) and \(\nu(w)=-w\) this is the module \(Q\) of Example 3.3, regarded as a \(B\)-module.

(a) Show that the rule is well defined and makes \(M\) a \(B\)-module \(M_\nu\), in which \(-e\) acts on \(W\) as \(\nu\).

(b) Let \(\nu'\) be a second map of this kind on \(W\) with \(\nu\circ\nu'=\nu'\circ\nu\); the case \(\nu'=\nu\) is allowed. Show that \([t]_\nu\) and \([s]_{\nu'}\) satisfy (2.1) for all \(t\in B(n)\), all \(s\in B(m)\) and all \(n\times m\) matrices with entries in \(M\).

(c) Let \(W=\{1,-1\}^2\), \(\nu(a,b)=(-a,b)\) and \(\nu'(a,b)=(a,-b)\). Construct a generalized ring \(C\) and two homomorphisms \(\gamma,\delta:B\to C\) with \(\gamma(-e)\ne\delta(-e)\). Conclude that \(\mathbb F_1\to B\) is not an epimorphism of generalized rings, that \(B\) with the identity maps is not a tensor product \(B\otimes_{\mathbb F_1}B\), and that \(S_N\to\operatorname{Spec}\mathbb F_1\) is not a monomorphism of generalized schemes.

(d) Let \(N\ge2\), and let \(P\) be a fibre product \(S_N\times_{\operatorname{Spec}\mathbb F_1}S_N\) in the category of generalized schemes. Show that \(|\mathcal O_P(P)|\) has at least four elements, and conclude that \(P\) is not isomorphic to \(S_N\).

**Solution.** (a) If \(\sum_i|t_i|=1\), then some \(t_i\) is not zero, and \(x_i=\operatorname{sgn}(t_i)\ast w\) gives \(w=\operatorname{sgn}(t_i)\ast x_i\), because \(\nu\) is an involution. So \(w\) is unique, and the rule is well defined. (M1): for \(t=e^n_i\) the rule gives \(w\) exactly when \(x_i=w\). So \([e^n_i]_\nu(x)=x_i\), also when \(x_i=0\). For \(t=-e\) the rule gives \(w\) exactly when \(x=\nu(w)\), that is, when \(w=\nu(x)\). So \(-e\) acts on \(W\) as \(\nu\).

(M2): let \(\lambda\in B(k)\), \(\mu^1,\dots,\mu^k\in B(n)\) and \(x\in M^n\). Put \(a_{ij}=\lambda_i\mu^i_j\) and \(\kappa=\lambda(\mu^1,\dots,\mu^k)\), so that \(\kappa_j=\sum_ia_{ij}\). Both sides of (M2) lie in \(W\sqcup\{0\}\). So it suffices to show, for each \(w\in W\), that the left side is \(w\) if and only if the right side is \(w\). Fix \(w\).

The right side \([\lambda]_\nu\bigl([\mu^1]_\nu(x),\dots,[\mu^k]_\nu(x)\bigr)\) is \(w\) if and only if \(\sum_i|\lambda_i|=1\) and \([\mu^i]_\nu(x)=\operatorname{sgn}(\lambda_i)\ast w\) for all \(i\) with \(\lambda_i\ne0\). Apply the rule to each \(\mu^i\) and use \(\operatorname{sgn}(\mu^i_j)\ast(\operatorname{sgn}(\lambda_i)\ast w)=\operatorname{sgn}(a_{ij})\ast w\). The condition becomes:

- (R1) \(\sum_i|\lambda_i|=1\), and \(\sum_j|\mu^i_j|=1\) for all \(i\) with \(\lambda_i\ne0\);
- (R2) \(x_j=\operatorname{sgn}(a_{ij})\ast w\) for all \((i,j)\) with \(a_{ij}\ne0\).

Since \(\sum_{i,j}|a_{ij}|=\sum_i|\lambda_i|\sum_j|\mu^i_j|\le\sum_i|\lambda_i|\le1\), condition (R1) is equivalent to \(\sum_{i,j}|a_{ij}|=1\). The left side \([\kappa]_\nu(x)\) is \(w\) if and only if:

- (L1) \(\sum_j|\kappa_j|=1\);
- (L2) \(x_j=\operatorname{sgn}(\kappa_j)\ast w\) for all \(j\) with \(\kappa_j\ne0\).

Assume (R1) and (R2), and fix \(j\). By (R2) all non-zero \(a_{ij}\) have the same sign: otherwise \(x_j=w\) and \(x_j=\nu(w)\), but \(\nu(w)\ne w\). So \(|\kappa_j|=\sum_i|a_{ij}|\). Summing over \(j\) gives (L1). Also \(\operatorname{sgn}(\kappa_j)=\operatorname{sgn}(a_{ij})\) whenever \(a_{ij}\ne0\), so (R2) gives (L2). Conversely assume (L1) and (L2). Then \(1=\sum_j|\kappa_j|\le\sum_{i,j}|a_{ij}|\le1\). So \(\sum_{i,j}|a_{ij}|=1\), which is (R1), and \(|\sum_ia_{ij}|=\sum_i|a_{ij}|\) for every \(j\). So for every \(j\) the non-zero \(a_{ij}\) have the sign of \(\kappa_j\), and (L2) gives (R2).

(b) Let \((x_{ij})\) be an \(n\times m\) matrix in \(M\) and \(w\in W\). Let \(a_i=1\) if \(t_i < 0\) and \(a_i=0\) otherwise, and let \(b_j=1\) if \(s_j < 0\) and \(b_j=0\) otherwise. Apply \([s]_{\nu'}\) to the rows and then \([t]_\nu\). By the rule, used twice, the result is \(w\) if and only if \(\sum_i|t_i|=1=\sum_j|s_j|\) and \(x_{ij}=(\nu')^{b_j}(\nu^{a_i}(w))\) for all \((i,j)\) with \(t_is_j\ne0\). Apply \([t]_\nu\) to the columns and then \([s]_{\nu'}\). The result is \(w\) if and only if \(\sum_i|t_i|=1=\sum_j|s_j|\) and \(x_{ij}=\nu^{a_i}((\nu')^{b_j}(w))\) for the same \((i,j)\). The two conditions agree, because \(\nu\) and \(\nu'\) commute. So the two sides of (2.1) are equal.

(c) The maps \(\nu\) and \(\nu'\) are involutions of \(W\) without fixed points. They commute, and they are different. By (a) and Example 1.6(b), the module structures \(M_\nu\) and \(M_{\nu'}\) correspond to two homomorphisms of clones \(\gamma,\delta:B\to\mathrm{END}(M)\). Let \(C\) be the subclone of \(\mathrm{END}(M)\) generated by all operations \([t]_\nu\) and \([t]_{\nu'}\). Two operations of \(\mathrm{END}(M)\) commute exactly when they satisfy (2.1) for all matrices in \(M\): the free module \(\mathrm{END}(M)(nm)\) is the set of maps \(M^{nm}\to M\), and the two sides of (2.1) for the matrix of its generators are the two maps that send a matrix in \(M\) to the two sides of (2.1). By (b), used for the pairs \((\nu,\nu)\), \((\nu',\nu')\) and \((\nu,\nu')\), any two generators of \(C\) commute. By Lemma 2.2(b), \(C\) is commutative. So \(C\) is a generalized ring, and \(\gamma\), \(\delta\) are homomorphisms \(B\to C\). By (a), \(\gamma(-e)\) and \(\delta(-e)\) act on \(W\) as \(\nu\) and \(\nu'\). So \(\gamma(-e)\ne\delta(-e)\).

The generalized ring \(C\) has a zero, so there is only one homomorphism \(\mathbb F_1\to C\) (Example 3.5), and \(\gamma\), \(\delta\) agree on \(\mathbb F_1\). Since \(\gamma\ne\delta\), the homomorphism \(\mathbb F_1\to B\) is not an epimorphism. If \(B\) with the identity maps were a pushout of \(B\leftarrow\mathbb F_1\to B\), there would be one homomorphism \(h:B\to C\) with \(h=\gamma\) and \(h=\delta\). Now let \(B=A_N\). By Corollary 7.10(a), \(\gamma\) and \(\delta\) give two different morphisms \(\operatorname{Spec}C\to\operatorname{Spec}A_N=U_2\). They remain different as morphisms to \(S_N\), because a morphism into the open subspace \(U_2\) is determined by its composite with the inclusion \(U_2\to S_N\). Their composites with \(S_N\to\operatorname{Spec}\mathbb F_1\) are equal, because \(\operatorname{Spec}C\) has only one morphism to \(\operatorname{Spec}\mathbb F_1\) (Corollary 7.10(b)). So \(S_N\to\operatorname{Spec}\mathbb F_1\) is not a monomorphism. The base \(\mathbb F_{\pm1}\) in Theorem 8.6 cannot be replaced by \(\mathbb F_1\).

(d) Write \(\mathrm{pr}_1,\mathrm{pr}_2:P\to S_N\) for the projections. Let \(g\ne h\) be the two morphisms \(\operatorname{Spec}C\to S_N\) of (c). They have the same composite to \(\operatorname{Spec}\mathbb F_1\), so there is a morphism \(v:\operatorname{Spec}C\to P\) with \(\mathrm{pr}_1\circ v=g\) and \(\mathrm{pr}_2\circ v=h\). Hence \(\mathrm{pr}_1\ne\mathrm{pr}_2\). By Theorem 8.6(c) the composites of \(\mathrm{pr}_1\) and \(\mathrm{pr}_2\) with \(S_N\to\operatorname{Spec}\mathbb F_{\pm1}\) are different. By Theorem 7.9 these composites correspond to the homomorphisms \(\sigma_1,\sigma_2:\mathbb F_{\pm1}=\mathcal O(S_N)\to\mathcal O_P(P)\) that \(\mathrm{pr}_1\) and \(\mathrm{pr}_2\) induce on global sections. So \(\sigma_1\ne\sigma_2\). A homomorphism from \(\mathbb F_{\pm1}\) is determined by its value on \(-e\) (Proposition 3.4(c)). So \(s_1=\sigma_1(-e)\) and \(s_2=\sigma_2(-e)\) are different elements of \(|\mathcal O_P(P)|\). Let \(\Delta:S_N\to P\) be the diagonal, the morphism with \(\mathrm{pr}_1\circ\Delta=\mathrm{id}=\mathrm{pr}_2\circ\Delta\), and let \(\Delta^\sharp:\mathcal O_P(P)\to\mathcal O(S_N)=\mathbb F_{\pm1}\) be the homomorphism that it induces on global sections. Then \(\Delta^\sharp\circ\sigma_i=\mathrm{id}\), so \(\Delta^\sharp(s_1)=\Delta^\sharp(s_2)=-e\), while \(\Delta^\sharp(e)=e\) and \(\Delta^\sharp(0)=0\). Hence \(0\), \(e\), \(s_1\), \(s_2\) are four different elements of \(|\mathcal O_P(P)|\). An isomorphism \(P\cong S_N\) would induce an isomorphism from \(\mathcal O_P(P)\) to \(\mathcal O(S_N)=\mathbb F_{\pm1}\), and \(|\mathbb F_{\pm1}|=\{0,e,-e\}\) has three elements. So \(P\) is not isomorphic to \(S_N\). The existence of \(P\) is [Durov 2007, 6.5.4]; we did not prove it.

## What this lesson does not prove

- The existence of tensor products \(A\otimes_CB\) of generalized rings in general, and of all limits and colimits of generalized rings: [Durov 2007, 5.1.6]. Every tensor product used above was verified directly.
- Three facts about sheaves on a base of a topology: [Stacks, Tag [009L](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sheaves.html#sheaves-lemma-cofinal-systems-coverings-standard-case)] (the sheaf condition may be checked on a cofinal system of covers), [Stacks, Tag [009N](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sheaves.html#sheaves-lemma-extend-off-basis)] (a sheaf on a base extends uniquely to a sheaf on the space) and [Stacks, Tag [009O](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/sheaves.html#sheaves-lemma-restrict-basis-equivalence)] (restriction to a base is an equivalence between sheaves on the space and sheaves on the base).
- Spectra for localization theories other than the prime spectrum, and the fact that all of them give the usual spectrum for rings: [Durov 2007, 6.3.4, 6.3.6 and 6.4.13].
- The existence of fibre products of arbitrary generalized schemes: [Durov 2007, 6.5.4]. The equivalence between schemes and the generalized schemes that admit a morphism to \(\operatorname{Spec}\mathbb Z\): [Durov 2007, 6.5.7]; we proved the affine case (Corollary 7.10(a)).
- The results on the compactification listed in Section 8 under "Proved in [Durov 2007] and not here": [Durov 2007, Theorem 7.1.26, Proposition 7.1.33, 7.1.35, 7.1.43–7.1.46, 7.1.22, Theorem 7.4.4], and the statement of [Durov 2007, 7.1.47] about the square of the pro-object.
- The description of the tensor square of \(\mathbb Z_{(\infty)}\) over \(\mathbb F_1\) as \(\mathbb Z_{(\infty)}\) with a second sign operation: [Durov 2007, 5.7.4]. We proved only that \(\mathbb Z_{(\infty)}\) with the identity maps is not this tensor square (Exercise 10.8).
- [Haran 2017, Theorem 2.9.1] (Theorem 9.4 above), and the construction of the compactification in [Haran 2017, §5.2].
- The extension of Example 7.7(b) from affine monoid schemes to all monoid schemes: [López Peña–Lorscheid 2011a, §2.5].

## References

- [Durov 2007] N. Durov, *New approach to Arakelov geometry*, [arXiv:0704.2030](https://arxiv.org/pdf/0704.2030).
- [Haran 2017] S. Haran, *New foundations for geometry: two non-additive languages for arithmetical geometry*, [arXiv:1508.04636](https://arxiv.org/pdf/1508.04636).
- [López Peña–Lorscheid 2011a] J. López Peña, O. Lorscheid, *Mapping \(\mathbb F_1\)-land: an overview of geometries over the field with one element*, [arXiv:0909.0069](https://arxiv.org/pdf/0909.0069).
- [Stacks] The [Stacks project](https://stacks.math.columbia.edu/), cited by tag. Each tag links to the same place in [AI Integrated Stacks Project](https://kokunoyumeto.github.io/stacks-zh-hans-cn/en/), the programme's edition of the Stacks project, which agrees with it modulo corrections made by GPT-6 Astra (OpenAI, Ultra setting) on suggestions of GPT-5.6 Sol (OpenAI, Ultra setting). Of the tags cited in this lesson, Tags 009O, 00EJ and 01I1 carry such corrections: wording, notation and small precisions in statements and proofs. None of them changes the results used here.
