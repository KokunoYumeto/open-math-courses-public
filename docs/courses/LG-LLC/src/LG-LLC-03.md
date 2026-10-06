# Local factors of pairs and the rank-two converse theorem

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A representation is more readily recognized by its response to twists than by its matrix entries. Rankin–Selberg factors record that response. In rank two, all character twists determine the Weyl operator in the Kirillov model, and that operator completes the representation. Before proving this converse theorem, we calculate spherical factors explicitly and keep track of the determinant twist in their functional equations.

We assume normalized induction, Whittaker and Kirillov models, and Tate's one-dimensional local factors. The general theory of Rankin–Selberg integrals is stated with its sources. Our proofs concern spherical computations in ranks two and one, the identification of a character pair with a determinant twist, and the rank-two converse theorem. Basic references are [Getz–Hahn 2022], [Jacquet–Langlands 1970] and [Jacquet–Piatetski-Shapiro–Shalika 1983].

## 1. What the integrals define

Let \(F\) be a nonarchimedean local field with residue cardinality \(q\), and let \(X=q^{-s}\). Fix a nontrivial additive character \(\psi\). In \(\mathrm{GL}_n(F)\), put
\[
\psi_N(u)=\psi(u_{12}+\cdots+u_{n-1,n}).
\]
A generic representation \(\pi\) has a Whittaker model \(\mathcal W(\pi,\psi)\), consisting of functions satisfying \(W(ug)=\psi_N(u)W(g)\); the model is unique. We take the model for the second representation with \(\psi^{-1}\), so products of Whittaker functions descend to a unipotent quotient.

For \(n>m\), one basic integral is
\[
Z(s,W,W')=\int_{N_m\backslash G_m}
 W\!\begin{pmatrix}g&0\\0&1_{n-m}\end{pmatrix}
 W'(g)|\det g|^{s-(n-m)/2}\,dg.
\tag{1.1}
\]
For \(n=m\), a Schwartz function \(\Phi\in\mathcal S(F^n)\) enters:
\[
Z(s,W,W',\Phi)=
\int_{N_n\backslash G_n}
 W(g)W'(g)\Phi(e_n g)|\det g|^s\,dg.
\tag{1.2}
\]
Here \(e_n=(0,\ldots,0,1)\). Haar measures are fixed once; rescaling them multiplies integrals by nonzero constants and does not change their normalized ideal generator.

**Theorem 1.1 (Rankin–Selberg theory, stated).** These integrals converge in a right half-plane and continue as rational functions of \(X\). Their span over \(\mathbb C[X,X^{-1}]\) is a fractional principal ideal with a unique generator
\[
L(s,\pi\times\pi')=P_{\pi,\pi'}(X)^{-1},
\qquad P_{\pi,\pi'}(0)=1.
\tag{1.3}
\]
The local functional equation gives a rational function \(\gamma(s,\pi\times\pi',\psi)\). Define
\[
\epsilon(s,\pi\times\pi',\psi)
=\gamma(s,\pi\times\pi',\psi)
\frac{L(s,\pi\times\pi')}{L(1-s,\pi^\vee\times\pi'^\vee)}.
\tag{1.4}
\]
It is a nonzero constant times a power of \(X\). With self-dual additive measure and an additive character of conductor zero, write it as
\[
\epsilon(s,\pi\times\pi',\psi)
=\epsilon(1/2,\pi\times\pi',\psi)\,
q^{-a(\pi\times\pi')(s-1/2)}.
\tag{1.5}
\]
For \(\psi_b(x)=\psi(bx)\), of arbitrary conductor, the change is
\[
\epsilon(s,\pi\times\pi',\psi_b)
=\omega_\pi(b)^m\omega_{\pi'}(b)^n
|b|^{nm(s-1/2)}\epsilon(s,\pi\times\pi',\psi).
\tag{1.6}
\]

For a pair of tempered representations, every integral converges and is holomorphic for \(\operatorname{Re}(s)>0\). Since the ideal generator is a finite Laurent-polynomial combination of those integrals, its \(L\)-factor is holomorphic there too. The rationality, principal ideal, tempered convergence and functional equation assertions are [Getz–Hahn 2022, Proposition 11.5.1, Theorem 11.5.4 and Proposition 11.5.5], from [Jacquet–Piatetski-Shapiro–Shalika 1983]. The conventions in a functional equation also include the chosen Weyl representative and its explicit central-character sign; this sign is retained in Section 3.

For arbitrary irreducible representations, use their Langlands quotients. If \(\pi=L(\Delta_1,\ldots,\Delta_t)\) and \(\pi'=L(\Delta'_1,\ldots,\Delta'_u)\), then
\[
\begin{aligned}
L(s,\pi\times\pi')&=\prod_{i,j}L(s,Q(\Delta_i)\times Q(\Delta'_j)),\\
\epsilon(s,\pi\times\pi',\psi)&=\prod_{i,j}\epsilon(s,Q(\Delta_i)\times Q(\Delta'_j),\psi).
\end{aligned}
\tag{1.7}
\]
The analogous product holds for \(\gamma\). The consistency of (1.7) with the integral definition whenever the quotient is generic is another general theorem input, [Getz–Hahn 2022, §11.8]. Gamma factors are also multiplicative for arbitrary parabolic inductions with their corresponding generic constituents. For the special representations used below, the precise formula is [Jacquet–Piatetski-Shapiro–Shalika 1983, Theorems 3.1 and 8.2, equation (14) in §8.2]. In contrast, one cannot obtain the Steinberg \(L\)-factor merely by multiplying the \(L\)-factors of its character support: grouping into a segment matters.

The conductor \(a(\pi)=a(\pi\times\mathbf1)\) in (1.5) is the epsilon-factor conductor. For generic \(\pi\), it equals the smallest \(r\ge0\) with a \(K_1(\varpi^r)\)-fixed vector, whose space at that first level is one-dimensional [Getz–Hahn 2022, Theorem 11.5.6]. This newvector theorem belongs to the generic setting. The extension (1.7) defines factors for nongeneric representations as well, without making the newvector assertion for them.

## 2. Computing the spherical factors

Assume in this section that \(\psi\) is trivial on \(\mathcal O\) and nontrivial on \(\varpi^{-1}\mathcal O\). Normalize \(\operatorname{vol}(G_r(\mathcal O))=\operatorname{vol}(N_r(\mathcal O))=1\). Let \(\pi\) be an unramified generic representation of \(G_2\), with unitary-normalized Satake parameters \(\alpha_1,\alpha_2\), and let \(W(1)=1\) be its spherical Whittaker function. Put \(A=\alpha_1\alpha_2=\omega_\pi(\varpi)\).

**Lemma 2.1.** If \(a_r=\operatorname{diag}(\varpi^r,1)\), then
\[
W(a_r)=
\begin{cases}
q^{-r/2}h_r(\alpha_1,\alpha_2),&r\ge0,\\
0,&r<0,
\end{cases}
\qquad
h_r(x,y)=\sum_{j=0}^r x^{r-j}y^j.
\tag{2.1}
\]

**Proof.** Right invariance by \(n(u)\), \(u\in\mathcal O\), implies
\(W(a_r)=\psi(\varpi^r u)W(a_r)\). For \(r<0\), some \(u\) makes this scalar different from one, so the value vanishes.

The double coset \(K\operatorname{diag}(\varpi,1)K\) has right coset representatives
\[
\begin{pmatrix}\varpi&u\\0&1\end{pmatrix}
\quad(u\in\mathcal O/\varpi\mathcal O),\qquad
\begin{pmatrix}1&0\\0&\varpi\end{pmatrix}.
\]
Its Hecke eigenvalue is \(q^{1/2}(\alpha_1+\alpha_2)\), by the normalized Satake convention. Evaluating the Hecke action at \(a_r\), for \(r\ge0\), gives
\[
q^{1/2}(\alpha_1+\alpha_2)W(a_r)
=qW(a_{r+1})+A W(a_{r-1}).
\]
The initial values are \(W(a_0)=1\), \(W(a_{-1})=0\). Multiplying the \(r\)-th value by \(q^{r/2}\) gives the recurrence
\(h_{r+1}=(\alpha_1+\alpha_2)h_r-Ah_{r-1}\), which the displayed finite sum satisfies. This proves the formula, including the coincident-parameter case. ∎

The Hecke eigenvalue convention is [Getz–Hahn 2022, Proposition 7.6.8]; the formula also agrees with the general Shintani formula, Corollary 11.4.2. We have proved its rank-two instance directly.

**Theorem 2.2.** For an unramified character \(\chi\), put \(\beta=\chi(\varpi)\). Then
\[
L(s,\pi\times\chi)=
\frac1{(1-\alpha_1\beta X)(1-\alpha_2\beta X)}.
\tag{2.2}
\]
If \(\pi'\) is an unramified generic representation of \(G_2\), with parameters \(\beta_1,\beta_2\), then
\[
L(s,\pi\times\pi')=\prod_{i,j=1}^2(1-\alpha_i\beta_jX)^{-1}.
\tag{2.3}
\]

**Proof.** In the first case (1.1), the integral is a sum over \(F^\times/\mathcal O^\times\). Lemma 2.1 gives
\[
Z(s,W,\chi)=\sum_{r\ge0}h_r(\alpha_1,\alpha_2)(\beta X)^r.
\]
The sum defining \(h_r\), reindexed by two independent nonnegative integers, gives (2.2).

For (2.3), take \(\Phi=1_{\mathcal O^2}\). Iwasawa decomposition writes the integral as a sum over diagonal matrices
\(\operatorname{diag}(\varpi^{r+m},\varpi^m)\). Whittaker support requires \(r\ge0\). Since \(e_2k\) is a primitive integral row for every \(k\in K\), the Schwartz condition requires \(m\ge0\). The two \(q^{-r/2}\) factors cancel \(\delta_B^{-1}=q^r\). Consequently, with \(B=\beta_1\beta_2\) and \(C=AB\),
\[
Z(s,W,W',1_{\mathcal O^2})
=\frac1{1-CX^2}\sum_{r\ge0}
h_r(\alpha_1,\alpha_2)h_r(\beta_1,\beta_2)X^r.
\tag{2.4}
\]
The elementary two-variable Cauchy identity is
\[
\sum_{r\ge0}h_r(\alpha)h_r(\beta)X^r
=\frac{1-CX^2}{\prod_{i,j}(1-\alpha_i\beta_jX)}.
\tag{2.5}
\]
To verify it, first suppose each pair of parameters is distinct. Substitute
\(h_r(x,y)=(x^{r+1}-y^{r+1})/(x-y)\), and sum the four geometric series. Their numerator, over the common denominator, is
\((\alpha_1-\alpha_2)(\beta_1-\beta_2)(1-CX^2)\).
Cancellation gives (2.5). Multiplying through by the polynomial denominators extends the identity to coincident parameters. Equation (2.4) is therefore the right side of (2.3).

For identification with the normalized ideal generator, we also need the general consistency statement in (1.7): an irreducible unramified generic principal series has Langlands blocks the two unramified characters. Their rank-one pair factors are Tate's factors. Thus (1.7) gives the same product as the computed integral. This supplies the reverse divisibility that an evaluation of one integral alone would not establish. ∎

For an unramified nongeneric representation of \(G_2\), the only possibility is a determinant character. Its Langlands blocks are also two unramified characters, with exponents differing by one, so (1.7) gives the same Satake product. There is no spherical Whittaker vector in that nongeneric representation; the integral calculation above was for generic representations.

## 3. A character pair is a determinant twist

**Proposition 3.1.** For an infinite-dimensional irreducible \(\pi\) of \(G_2\) and any character \(\chi\) of \(F^\times\),
\[
\begin{aligned}
L(s,\pi\times\chi)&=L(s,\pi\otimes(\chi\circ\det)),\\
\epsilon(s,\pi\times\chi,\psi)&=\epsilon(s,\pi\otimes(\chi\circ\det),\psi).
\end{aligned}
\tag{3.1}
\]
Here the standard factor on the right means the pair with the trivial character.

**Proof.** The map \(W(g)\mapsto W_\chi(g)=\chi(\det g)W(g)\) is a bijection between the two Whittaker models. On \(\operatorname{diag}(x,1)\), it multiplies by \(\chi(x)\). Hence the entire families of integrals defining the two \(L\)-factors are identical, so their normalized ideal generators agree. The same argument applies to the duals.

For the gamma factor, retain the sign in the functional equation. Let
\(w_2=\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\) and
\(\widetilde W(g)=W(w_2\,{}^tg^{-1})\). The rank-two pair equation in this convention is
\[
Z(1-s,\widetilde W,\chi^{-1})
=\chi(-1)\gamma(s,\pi\times\chi,\psi)Z(s,W,\chi).
\]
But \(\widetilde{W_\chi}(g)=\chi(-1)\chi^{-1}(\det g)\widetilde W(g)\). Thus the standard dual integral for \(W_\chi\) is \(\chi(-1)\) times the left side. Since \(\chi(-1)^2=1\), the standard equation has exactly the same gamma factor. Equations (1.4) and the two \(L\)-factor equalities give the epsilon-factor equality. ∎

For a determinant character, the identities extend by (1.7) and Tate's twist identity on each of its two character blocks. This covers all irreducible representations of \(G_2\).

## 4. Character twists recover the Weyl action

The Kirillov-model prerequisite says that every infinite-dimensional irreducible representation of \(G_2\) is generic and has a faithful model \(V_\pi\) of locally constant functions on \(F^\times\). It contains
\(S=C_c^\infty(F^\times)\). If its central character is \(\omega\), the upper triangular action is
\[
(\pi(\begin{pmatrix}a&b\\0&d\end{pmatrix})f)(x)
=\omega(d)\psi(bx/d)f(ax/d).
\tag{4.1}
\]
Each Kirillov function vanishes for \(|x|\) sufficiently large: a compact open subgroup of upper unipotents fixes its vector, and (4.1) forces this bound. Its Mellin transforms have the rational continuation supplied by local factor theory.

Put \(w=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\), so \(w^2=-1\). In this determinant-one convention the standard rank-two functional equation, applied after a character twist, reads
\[
\int_{F^\times}(\pi(w)f)(x)\omega(x)^{-1}\chi(x)^{-1}
 |x|^{1/2-s}\,d^\times x
=\gamma(s,\pi\times\chi,\psi)
\int_{F^\times}f(x)\chi(x)|x|^{s-1/2}\,d^\times x.
\tag{4.2}
\]
This is [Jacquet–Langlands 1970, Theorem 2.18 and equation (2.18.1)], translated through (3.1). The symmetric Weyl convention of Section 3 has its explicit \(\chi(-1)\) sign instead; both give (4.2) after the indicated change of representative.

**Lemma 4.1 (Mellin inversion in the needed form).** A locally constant Kirillov function \(g\), bounded in support toward \(|x|=\infty\) and with rational Mellin transforms, is determined by those transforms against all characters.

**Proof.** Decompose \(x=\varpi^r u\), with \(u\in\mathcal O^\times\), and normalize unit volume to one. For each character \(\eta\) of \(\mathcal O^\times\), its Mellin transform is a Laurent series
\[
\sum_{r\ge R}
\left(\int_{\mathcal O^\times}g(\varpi^r u)\eta(u)\,d^\times u\right)z^r.
\tag{4.3}
\]
In its domain of convergence near \(z=0\), this is the Laurent expansion of the rational continuation; the coefficients are unique. Allowing arbitrary unramified twists varies \(z\), so the meromorphic transform determines each coefficient. For a fixed \(r\), the function of \(u\) factors through a finite quotient of \(\mathcal O^\times\). Finite Fourier inversion over its characters reconstructs it from all the coefficients in (4.3). Doing this for each \(r\) determines \(g\). ∎

**Theorem 4.2 (rank-two local converse).** Suppose \(\pi_1,\pi_2\) are infinite-dimensional irreducible representations of \(G_2\), have the same central character, and satisfy
\[
\gamma(s,\pi_1\times\chi,\psi)
=\gamma(s,\pi_2\times\chi,\psi)
\quad\text{for every character }\chi.
\tag{4.4}
\]
Then \(\pi_1\simeq\pi_2\).

**Proof.** Realize both in their Kirillov models with the same \(\psi\). Their copies of \(S\) have the same upper triangular action by (4.1). For \(f\in S\), the right sides of (4.2) agree. Mellin inversion therefore shows
\(\pi_1(w)f=\pi_2(w)f\), as actual functions on \(F^\times\).

We check that this equality controls the whole model. In either model put \(U=S+\pi(w)S\). It is stable under diagonal matrices and the center, by (4.1) and the relation between a diagonal matrix and \(w\). If \(g=\pi(w)f\), then
\[
(\pi(n(b))-1)g(x)=(\psi(bx)-1)g(x)
\]
belongs to \(S\): it vanishes near zero because \(\psi(bx)=1\) there, and it vanishes for large \(|x|\) because \(g\) does. Thus \(U\) is stable under the upper unipotents as well. It is stable under \(w\), since \(w^2=-1\) acts by the scalar \(\omega(-1)\). Upper triangular matrices and \(w\) generate \(G_2\), so irreducibility implies \(U=V_\pi\).

The two spaces \(S+\pi_i(w)S\) coincide. The upper triangular actions on this common function space agree. The Weyl actions agree on \(S\), and on their common \(\pi(w)S\) they agree because both square to \(\omega(-1)\). Hence the identity on the common function space intertwines every element of \(G_2\). ∎

This proof explains the central-character hypothesis: it fixes the common upper triangular action and the square of the Weyl operator. A later bounded-twist argument will also recover that character from suitable twist data.

## 5. Steinberg times Steinberg: a parameter and an integral

Use the centered special parameter \(S_2\), with basis \(e_-,e_+\), Weil characters \(\lVert\cdot\rVert^{-1/2},\lVert\cdot\rVert^{1/2}\), and \(Ne_-=e_+\), \(Ne_+=0\). On its tensor square, \(N\) is \(N\otimes1+1\otimes N\). The three vectors
\[
a=e_-\otimes e_-,\quad
b=e_+\otimes e_-+e_-\otimes e_+,\quad
c=2e_+\otimes e_+
\]
have exponents \(-1,0,1\) and satisfy \(Na=b,\ Nb=c,\ Nc=0\). The remaining vector
\(d=e_+\otimes e_--e_-\otimes e_+\) has exponent zero and is killed by \(N\). Thus
\[
S_2\otimes S_2\simeq S_3\oplus\mathbf1,\qquad
L(s,S_2\otimes S_2)=\frac1{(1-q^{-1}X)(1-X)}.
\tag{5.1}
\]
Its conductor is two, and its epsilon factor for conductor-zero \(\psi\) is \(q^{1-2s}\), from the two-dimensional monodromy quotient of \(S_3\).

We now identify the analytic factor independently. Multiplicativity of gamma factors at the two generic Steinberg constituents gives
\[
\gamma(s,\mathrm{St}_2\times\mathrm{St}_2,\psi)
=\gamma(s,|\cdot|^{-1},\psi)\gamma(s,1,\psi)^2
 \gamma(s,|\cdot|,\psi)
=qX^2\frac{(1-X)(1-q^{-1}X)}
 {(1-q^{s-1})(1-q^{s-2})}.
\tag{5.2}
\]
The last equality follows by substituting Tate's unramified factors and cancelling one factor at each of \(X=q^{-1}\) and \(X=1\).

Both Steinberg representations are tempered, by the square-integrability proof in the classification lesson. For any tempered pair and its dual, write the factor equation as
\(\gamma=\epsilon P(q^{-s})/P^\vee(q^{s-1})\). All roots of \(P(q^{-s})\) have \(\operatorname{Re}(s)\le0\), by tempered convergence. In that half-plane \(P^\vee(q^{s-1})\) is nonzero, since its argument represents \(L(1-s)\) in \(\operatorname{Re}(1-s)\ge1\). The epsilon monomial is also nonzero. Thus the zeros of \(\gamma\) in \(\operatorname{Re}(s)\le0\), with multiplicity, are exactly the roots of \(P(q^{-s})\). They determine \(P\), whose constant coefficient is one.

Equation (5.2) has exactly the roots \(X=1,q\) in that half-plane. Hence
\[
L(s,\mathrm{St}_2\times\mathrm{St}_2)
=\frac1{(1-X)(1-q^{-1}X)},\qquad
\epsilon(s,\mathrm{St}_2\times\mathrm{St}_2,\psi)=q^{1-2s}.
\tag{5.3}
\]
This proves agreement with the parameter calculation, including its conductor two and root number one. We can also realize its precise denominator in a single integral.

In the boundary model \(C^\infty(\mathbb P^1(F))/\mathbb C\), use the open coordinate \(wn(x)\), and let \(v\) be the class of \(1_{\mathcal O}(x)\). For a boundary function \(\phi\), the integral
\[
\Lambda(\phi)=\int_F\phi(x)\psi(-x)\,dx
\]
means the stabilized integral over increasing compact balls. It stabilizes because \(\phi\) is constant outside a ball, and those constant tails have zero integral against \(\psi\). It vanishes on constants, is a \(\psi\)-Whittaker functional, and satisfies \(\Lambda(v)=1\). Its Whittaker function is Iwahori-fixed. Directly applying the fractional linear transformations gives
\[
W(a_r)=
\begin{cases}q^{-r}&r\ge0,\\0&r<0,\end{cases}
\qquad
W(a_r w)=
\begin{cases}-q^{-r-1}&r\ge-1,\\0&r<-1.\end{cases}
\tag{5.4}
\]
For example, \(a_r\) sends the boundary function to \(1_{\varpi^r\mathcal O}\); \(a_rw\) sends it, modulo a constant, to \(-1_{\varpi^{r+1}\mathcal O}\). This proves both formulas by additive integration. The \(\psi^{-1}\)-Whittaker function \(W'\) has the same values.

The \(q+1\) right Iwahori cosets in \(K\) have representatives \(1\) and \(n(u)w\), \(u\in\mathcal O/\varpi\mathcal O\). Their opposite Whittaker phases cancel in \(WW'\). Consequently the \(K\)-average at \(a_r\) is \(q^{-2r}/q\) for \(r\ge0\), \(q/(q+1)\) for \(r=-1\), and zero otherwise. In (1.2), \(\Phi=1_{\mathcal O^2}\) imposes only that the central exponent \(m\ge0\); the Steinberg central characters are trivial. Iwasawa integration therefore gives
\[
\begin{aligned}
Z(s,W,W',1_{\mathcal O^2})
&=\frac1{1-X^2}
 \left(\frac{X^{-1}}{q+1}+\frac{q^{-1}}{1-q^{-1}X}\right)\\
&=\frac{X^{-1}}{(q+1)(1-X)(1-q^{-1}X)}.
\end{aligned}
\tag{5.5}
\]
Thus this integral is (5.1) times a unit of \(\mathbb C[X,X^{-1}]\). Its factor at \(1-X\) would be missed by treating the two Whittaker functions as spherical; Steinberg has an Iwahori-fixed vector and no \(K\)-fixed vector.

## 6. Higher-rank converse theorems

The following results are statements, not consequences of the rank-two proof.

**Theorem 6.1 (Henniart, stated).** Two irreducible generic representations of \(G_n\), with the same central character, are isomorphic if their gamma factors agree after twisting by every irreducible generic representation of every \(G_r\), \(1\le r\le n-1\).

**Theorem 6.2 (Jacquet–Liu and Chai, stated).** The same conclusion holds with \(1\le r\le\lfloor n/2\rfloor\).

The first is the \(J(n,n-1)\) theorem recalled in [Jacquet–Liu 2017, Introduction], referring to [Henniart 1993]. The second is [Jacquet–Liu 2017, Theorem 1.3] over nonarchimedean local fields; [Chai 2016, Theorem 1.1] gives an independent proof over p-adic fields. The hypotheses concern generic representations. Arbitrary nongeneric Langlands quotients require their segment data as well; these converse theorems do not state that every irreducible representation is determined by the same generic integral argument.

## 7. Exercises and complete solutions

**Exercise 7.1 (easy).** If \(\pi\) has unramified parameters \(\alpha_1,\alpha_2\) and \(\chi(\varpi)=\beta\), calculate the twisted factor and the first three coefficients of its power series.

**Solution.** Proposition 3.1 and (2.2) give \(((1-\alpha_1\beta X)(1-\alpha_2\beta X))^{-1}\). Its constant coefficient is one, its \(X\)-coefficient is \((\alpha_1+\alpha_2)\beta\), and its \(X^2\)-coefficient is \((\alpha_1^2+\alpha_1\alpha_2+\alpha_2^2)\beta^2\). These are the three spherical Whittaker coefficients after their modular-character factors have been cancelled in the zeta integral.

**Exercise 7.2 (medium).** Calculate \(L(s,\mathrm{St}_2\times\mathrm{St}_2)\) on the parameter side, and compare it with a local integral.

**Solution.** The four explicit tensor vectors in Section 5 split the parameter as \(S_3\oplus\mathbf1\). The two vectors in its monodromy kernel have Frobenius eigenvalues \(q^{-1}\) and one, respectively. This gives \(((1-q^{-1}X)(1-X))^{-1}\). The integral (5.5), with opposite Iwahori Whittaker functions and \(1_{\mathcal O^2}\), is this expression times \(X^{-1}/(q+1)\). Multiplicativity gives (5.2), and tempered convergence identifies its left-half-plane zeros with the roots of the inverse \(L\)-polynomial, proving the same factor analytically. The exponent shift is one in the \(S_3\) block; there is no shift in the trivial block. The two epsilon factors are both \(q^{1-2s}\).

**Exercise 7.3 (medium).** Derive the rank-two converse theorem from the Kirillov model and its functional equation.

**Solution.** For every \(f\in C_c^\infty(F^\times)\), equality of gamma factors makes the right sides of (4.2) equal, hence all Mellin transforms of the two Weyl images equal. Laurent coefficient uniqueness and finite Fourier inversion give equality of the Weyl images as functions. The upper triangular actions agree because the central characters agree. The subspace \(S+\pi(w)S\) is stable under that subgroup and \(w\), using \((\psi(bx)-1)\pi(w)f\in S\) and \(w^2=-1\), so is the full irreducible model. The common actions on this space give the required isomorphism. This reproduces every step of Theorem 4.2.

**Exercise 7.4 (hard).** Give explicit integers \(c,c'\) for a bounded-twist converse: among infinite-dimensional irreducible representations with \(a(\pi)\le c'\), show that the gamma factors for all characters of conductor at most \(c\) determine \(\pi\). The central character should also be recovered from those factors.

**Solution.** Let \(c'\ge0\) be any prescribed integer. A valid, nonoptimal choice is
\[
c=2c'+4.
\tag{7.1}
\]
This solution uses the existence and pair-factor compatibility of the correspondence theorem stated in *The statement of the local Langlands correspondence*, and the precise stability theorem [Deligne–Henniart 1981, Theorem 4.6 and Lemma 4.7]. The converse theorem of Section 4 was proved independently of these inputs.

Let \((r_i,N_i)\) be the two parameters, \(a(r_i,N_i)\le c'\). Their Weil parts are semisimple. Every irreducible ramified constituent of upper break \(b\) has conductor \(\dim(\rho)(1+b)\); unramified constituents have break zero for this estimate. Thus the largest break of either \(r_i\) is at most \(c'\). Also \(a(\det r_i)\le a(r_i)\le c'\): in the Artin conductor formula, the codimension of invariants of a determinant is at most that of the original representation for each ramification group, and the Swan integral preserves this inequality.

The cited stability theorem has the following precise consequence. If a character \(\chi\) has conductor \(m\ge2\) and the largest break of a virtual Weil representation \(V\) of dimension zero is \(<(m-1)/2\), then
\[
\epsilon(s,V\otimes\chi,\psi)=\det V(c_\chi),
\tag{7.2}
\]
where \(v(c_\chi)=m+n(\psi)\) and
\(\chi(1+y)=\psi(c_\chi^{-1}y)\) for \(v(y)>(m-1)/2\). The determinant evaluation includes its Weil-character interpretation through geometric reciprocity. For \(m>c'+1\), both \(r_i\otimes\chi\) have zero inertia invariants: on a ramification group beyond all the breaks of \(r_i\), the nontrivial character \(\chi\) acts by a scalar. Therefore both their \(L\)-factors, and those of their duals, equal one; their monodromy determinant corrections also equal one. Equations (1.4) and (7.2) then give
\[
\frac{\gamma(s,\pi_1\times\chi,\psi)}
{\gamma(s,\pi_2\times\chi,\psi)}
=\eta(c_\chi),\qquad
\eta=\det r_1/\det r_2=\omega_{\pi_1}/\omega_{\pi_2}.
\tag{7.3}
\]

Use (7.3) first at \(m=c\) and then at \(m=c-1\), both covered by the assumed twist data. Its strict break inequality holds at both levels. For every \(u\in\mathcal O^\times\), one can choose \(\chi\) with \(c_\chi=\varpi^{m+n(\psi)}u\) in the determinant evaluation. Here is the required existence check. Set \(h=\lceil m/2\rceil\), \(t=(\varpi^{m+n(\psi)}u)^{-1}\), and prescribe
\(\chi(1+y)=\psi(ty)\) on \(1+\varpi^h\mathcal O\). It is multiplicative because \(2h\ge m\), so the product error \(tyz\) lies in the additive-character kernel. It is nontrivial on \(1+\varpi^{m-1}\mathcal O\) and trivial on \(1+\varpi^m\mathcal O\). A character of this subgroup of the finite abelian unit quotient extends to the whole quotient; extend further to \(F^\times\) by an arbitrary value at \(\varpi\). Its conductor is exactly \(m\), and its prescribed linearization supplies this \(c_\chi\). The linearization determines \(c_\chi\) modulo multiplication by \(1+\mathfrak p^{\lfloor m/2\rfloor}\): the annihilator of \(\mathfrak p^h\) under \(\psi\) is \(\mathfrak p^{-n(\psi)-h}\), so replacing \(c_\chi\) by \(c_\chi u\) preserves the restriction exactly when \(v(u-1)\ge m-h=\lfloor m/2\rfloor\). This ambiguity is invisible to \(\eta\), since \(a(\eta)\le c'\) and \(\lfloor m/2\rfloor\ge c'+1\) at both chosen levels.

Equality of the bounded twist factors now gives
\(\eta(\varpi^{m+n(\psi)}u)=1\) for every unit \(u\), at two consecutive values of \(m\). Taking \(u=1\) and dividing the two equalities gives \(\eta(\varpi)=1\); dividing the equality for general \(u\) by that for \(u=1\) gives \(\eta(u)=1\). Thus the central characters agree.

For any remaining character of conductor \(m>c\), the same stability formula applies, and its ratio is now one because \(\eta=1\). Together with the assumed factors at \(m\le c\), this gives all character-twist factors. Theorem 4.2 proves \(\pi_1\simeq\pi_2\). This proves (7.1), including central-character recovery. The hypothesis supplies functions of \(s\), and all unramified values of the twist characters, rather than only finitely many numerical values of gamma factors. ∎

## What this lesson does not prove

The general Rankin–Selberg rationality, ideal, functional equation, multiplicativity and Langlands-quotient consistency theorems are inputs from [Getz–Hahn 2022, §§11.5 and 11.8] and [Jacquet–Piatetski-Shapiro–Shalika 1983]. The Hecke eigenvalue convention used in the spherical recurrence is [Getz–Hahn 2022, Proposition 7.6.8]. The rank-two Kirillov model and its functional equation are the assigned prerequisites, with [Jacquet–Langlands 1970, §2, Theorem 2.18 and equation (2.18.1)] as locators. Mellin inversion and the consequent converse argument were proved here.

The two higher-rank converse theorems are only stated, with their exact locators in Section 6. The bounded-twist exercise uses the correspondence existence and pair compatibility theorem [Wedhorn 2000, (1.2.2)], which is stated in the next lesson and proved in [Scholze 2013, Theorem 1.2]. The Steinberg pair calculation uses only the stated general gamma multiplicativity and tempered convergence, together with our explicit computations. The stability input for the explicit bound is [Deligne–Henniart 1981, Theorem 4.6 and Lemma 4.7], whose strict upper-break inequality was displayed in (7.2). This is stronger information than a qualitative sufficiently-ramified assertion.

## References

- [Getz–Hahn 2022] Jayce R. Getz and Heekyoung Hahn, *An Introduction to Automorphic Representations, with a View toward Trace Formulae*, draft of 22 April 2022, §§7.6 and 11.2–11.8; published as Graduate Texts in Mathematics 300, Springer, 2024. The [author version](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf) uses the numbering cited here.
- [Jacquet–Langlands 1970] Hervé Jacquet and Robert P. Langlands, [*Automorphic Forms on GL(2)*](https://publications.ias.edu/sites/default/files/Automorphic-forms-on-GL2.pdf), Lecture Notes in Mathematics 114, Springer, 1970, §2. The IAS re-typeset edition retains its theorem numbering.
- [Jacquet–Piatetski-Shapiro–Shalika 1983] Hervé Jacquet, Ilya I. Piatetski-Shapiro and Joseph A. Shalika, “[Rankin–Selberg convolutions](https://www.math.columbia.edu/~hj/Rankin%20Selberg%20convolutions.pdf),” *American Journal of Mathematics* 105 (1983), 367–464. The general integral theory is cited through the precise exposition in [Getz–Hahn 2022].
- [Henniart 1993] Guy Henniart, “[Caractérisation de la correspondance de Langlands locale par les facteurs \(\epsilon\) de paires](https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0113/LOG_0039.pdf),” *Inventiones mathematicae* 113 (1993), 339–350. The \(J(n,n-1)\) statement is recalled in [Jacquet–Liu 2017, Introduction].
- [Jacquet–Liu 2017] Hervé Jacquet and Baiying Liu, *On the local converse theorem for p-adic GL_n*, version of 14 March 2017, [arXiv:1601.03656](https://arxiv.org/abs/1601.03656), Theorem 1.3; published in *American Journal of Mathematics* 140 (2018), 1399–1422.
- [Chai 2016] Jingsong Chai, *Bessel functions and local converse conjecture of Jacquet*, version of 29 November 2016, [arXiv:1601.05450](https://arxiv.org/abs/1601.05450), Theorem 1.1.
- [Deligne–Henniart 1981] Pierre Deligne and Guy Henniart, “[Sur la variation, par torsion, des constantes locales d'équations fonctionnelles de fonctions L](https://publications.ias.edu/sites/default/files/Number43.pdf),” *Inventiones mathematicae* 64 (1981), 89–118, §0.6, Theorem 4.6 and Lemma 4.7.
- [Wedhorn 2000] Torsten Wedhorn, [*The local Langlands correspondence for GL(n) over p-adic fields*](https://arxiv.org/abs/math/0011210v2), lectures at the School on Automorphic Forms on GL(n), ICTP Trieste, 2000, §1.2.
- [Scholze 2013] Peter Scholze, [*The Local Langlands Correspondence for GL_n over p-adic fields*](https://arxiv.org/abs/1010.1540v1), *Inventiones mathematicae* 192 (2013), 663–715, Theorem 1.2.
