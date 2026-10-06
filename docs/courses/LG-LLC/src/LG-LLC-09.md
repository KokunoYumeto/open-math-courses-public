# Modular forms, elliptic curves and local–global compatibility

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

A newform has a local representation at every prime, and its Galois representation has a local Weil–Deligne parameter there. Local–global compatibility identifies them. At a good prime, the identification compares two quadratic polynomials. At a multiplicative prime, it compares a monodromy block and a linear factor. At a wild additive prime, the conductor and a ramified inducing character carry information that the vanishing Hecke coefficient does not record.

We state Carayol's theorem and prove its normalization checks and the consequences for bad-prime coefficients and representation types. The elliptic-curve reduction calculations are imported from *Elliptic curves over local fields and their Weil–Deligne representations*, particularly Theorems 4.1–5.1 and Examples 6.1–6.3. We then identify explicit local characters for the complex-multiplication forms of levels 27 and 32. Our basic references are [Carayol 1986], [Deligne 1973] and [Jacquet–Langlands 1970].

## 1. Fixing all three normalizations

Let
\[
f(z)=\sum_{n\ge1}a_n e^{2\pi inz}
\]
be a normalized cuspidal newform of weight \(k\ge2\), level \(N_f\) and nebentype \(\varepsilon\). Choose a coefficient-field place \(\lambda\) of residue characteristic \(\ell\). Use the arithmetic Galois representation \(\rho_{f,\lambda}\): at \(p\nmid N_f\ell\), arithmetic Frobenius has characteristic polynomial
\[
T^2-a_pT+\varepsilon(p)p^{k-1}.
\tag{1.1}
\]
Existence with this characterization is the Deligne newform prerequisite; [Taylor 2004, §3, Theorem 3.6] describes the Galois construction and its compatibility framework. We specify (1.1) because another standard convention uses the dual representation.

Let \(\pi_f=\bigotimes_v\pi_{f,v}\) be the **unitary** automorphic representation attached to \(f\). Its local Satake values at a good prime are the two roots of (1.1), divided by \(p^{(k-1)/2}\). Its central character is the finite-order nebentype character in this automorphic convention. Write \(\nu_p=|\cdot|_{\mathbb Q_p}\), and transport it to the Weil group by geometric reciprocity. Thus
\[
\operatorname{Art}_p(p)=\Phi_p,
\qquad \|\Phi_p\|=p^{-1},
\qquad \Phi_p=\operatorname{Frob}_{p,\mathrm{arith}}^{-1}.
\tag{1.2}
\]
Fix a coefficient identification with \(\mathbb C\) for writing the parameters; equalities mean isomorphisms of complex Weil–Deligne pairs after that identification.

**Theorem 1.1 (local–global compatibility, stated).** For every \(p\ne\ell\), including primes dividing \(N_f\),
\[
\operatorname{rec}_p(\pi_{f,p})
\simeq
\operatorname{WD}\bigl(\rho_{f,\lambda}^{\vee}|_{G_{\mathbb Q_p}}\bigr)^{\mathrm{F\text{-}ss}}
\otimes\|\cdot\|^{(k-1)/2}.
\tag{1.3}
\]
Only Frobenius is semisimplified here. The monodromy operator is retained.

This is [Carayol 1986, Introduction, Theorem (A), §§0.4–0.8], expressed in our conventions. The original paper defines its Hecke correspondence separately in §0.5, with a contragredient and a half norm twist. Its hypotheses in §0.3 include holomorphic weights at least two, and a finite discrete-series place when the totally real field has even degree. For the rational field in this lesson the degree is one, so that extra condition does not arise. [Blasius 2006, §§2.3–2.4] discusses the compatibility and weight–monodromy formulations; [Taylor 2004, §3] distinguishes the local correspondence from the global assertion. These are statements of deep theorems, not substitutes for the deductions below.

**Proposition 1.2 (the unramified check).** Formula (1.3) has the required Satake values and determinant at every good prime.

**Proof.** Let \(A_p,B_p\) be the roots of (1.1). Arithmetic Frobenius on \(\rho_{f,\lambda}\) has these eigenvalues. Geometric Frobenius on its dual has matrix the transpose of arithmetic Frobenius on the original representation, hence again has eigenvalues \(A_p,B_p\). The norm twist in (1.3) multiplies them by \(p^{-(k-1)/2}\). Thus the parameter has
\[
\alpha_p=A_p p^{-(k-1)/2},\quad
\beta_p=B_p p^{-(k-1)/2},\quad
\alpha_p\beta_p=\varepsilon(p),\quad
\alpha_p+\beta_p=a_p p^{-(k-1)/2}.
\tag{1.4}
\]
Inertia is trivial, monodromy is zero, and its factor is
\[
\frac{1}{1-a_p p^{-s-(k-1)/2}+\varepsilon(p)p^{-2s}}
=L_p\bigl(f,s+(k-1)/2\bigr).
\tag{1.5}
\]
This is exactly the unitary local factor. Its determinant at \(\Phi_p\) is \(\varepsilon(p)\), agreeing with the central character at \(p\). ∎

Using \(\rho\) without dualizing would instead leave inverse eigenvalues at geometric Frobenius. Using the dual but omitting the norm twist would leave the classical weight in the Satake values. Both choices change the displayed factor. Equations (1.1)–(1.5) determine our convention before any bad-prime calculation.

The arithmetic local factor at every prime is consequently
\[
L_p(f,u)=L_p\bigl(u,\operatorname{WD}(\rho_{f,\lambda}^{\vee})^{\mathrm{F\text{-}ss}}\bigr)
=L_p\bigl(u-(k-1)/2,\pi_{f,p}\bigr).
\tag{1.6}
\]
The first identity at bad primes uses the theorem. It is not inferred from equality at almost all primes.

## 2. Conductors and the bad-prime coefficient

Write \(r_p=v_p(N_f)\). The newform dictionary identifies \(r_p\) with the generic newvector conductor of \(\pi_{f,p}\). Cuspidal automorphic representations of \(\mathrm{GL}_2\) are generic: the nonzero Fourier coefficient of the normalized form supplies the global Whittaker functional and its local components. The newform and local-factor inputs are [Jacquet–Langlands 1970, §§2 and 11] and [Getz–Hahn 2022, §11.5, particularly Proposition 11.5.1 and Theorem 11.5.6]. In particular the generic hypothesis excludes determinant characters.

**Proposition 2.1.** For \(p\ne\ell\), the Artin conductor of \(\rho_{f,\lambda}|_{G_{\mathbb Q_p}}\) has exponent \(r_p\).

**Proof.** Twisting a Weil–Deligne pair by an unramified norm power does not change its inertia action or invariant monodromy rank, hence does not change its conductor. Dualization also leaves the conductor unchanged. Indeed invariant dimensions for a finite ramification-group image agree in a representation and its dual, by averaging; this proves equality of the Swan terms. On inertia invariants the ranks of \(N\) and \(-N^{\mathsf T}\) agree. The formula
\[
a(r,N)=a(r)+\dim V^I-\dim(\ker N)^I
\]
therefore gives the same value for the dual. Apply (1.3), the correspondence's conductor preservation, and the generic newvector theorem to get
\[
a\bigl(\rho_{f,\lambda}|_{G_{\mathbb Q_p}}\bigr)
=a\bigl(\operatorname{rec}\pi_{f,p}\bigr)
=a_{\mathrm{new}}(\pi_{f,p})=r_p.
\tag{2.1}
\]
The conductor of an \(\ell\)-adic representation here is that of its associated Weil–Deligne pair. ∎

For a fixed \(\lambda\), (2.1) asserts equality only away from \(\ell\). To determine every prime of the level by this argument, choose a different coefficient place at the prime being computed. No assertion about the usual finite-inertia Artin conductor at \(p=\ell\) is implicit.

Assume for the rest of this section that the nebentype is trivial. Then the local central character is trivial.

**Theorem 2.2 (bad-prime coefficients and the Steinberg check).** If \(p\parallel N_f\), then
\[
\pi_{f,p}=\mathrm{St}_2\otimes(\chi_p\circ\det),
\qquad \chi_p\text{ unramified},\quad \chi_p(p)=b_p\in\{1,-1\},
\tag{2.2}
\]
and
\[
a_p=b_p p^{k/2-1}.
\tag{2.3}
\]
If \(p^2\mid N_f\), then \(a_p=0\) and \(L_p(f,u)=1\).

**Proof.** A supercuspidal parameter is an irreducible two-dimensional Weil representation with zero monodromy. Its inertia invariants vanish, so its conductor is \(2+\mathrm{Sw}\ge2\). Thus a conductor-one representation is not supercuspidal. For a principal series of central character one, its labels are \(\mu,\mu^{-1}\). Its conductor is \(2a(\mu)\), which is even. A special representation \(\mathrm{St}_\chi\) has conductor one if \(\chi\) is unramified and conductor \(2a(\chi)\) otherwise. These are the proved non-supercuspidal conductor formulas. Genericity excludes the remaining one-dimensional type, so exponent one forces (2.2). Its central character is \(\chi_p^2\); consequently \(b_p^2=1\).

The centered special parameter is \(\chi_p S_2\), with Weil lines of weights \(-1/2,+1/2\) and monodromy from the first to the second. Its kernel therefore has Frobenius value \(b_p p^{-1/2}\), giving
\[
L_p(s,\pi_{f,p})=(1-b_p p^{-s-1/2})^{-1}.
\tag{2.4}
\]
Undo the norm twist in (1.3). On the invariant kernel of \(\operatorname{WD}(\rho_{f,\lambda}^{\vee})\), geometric Frobenius has value
\[
b_p p^{-1/2}p^{(k-1)/2}=b_p p^{k/2-1}.
\tag{2.5}
\]
Equation (1.6) makes this the coefficient in the classical linear local factor \((1-a_p p^{-u})^{-1}\). This proves (2.3) and the Steinberg normalization check.

Now suppose \(r_p\ge2\). A supercuspidal has local factor one. A principal series has the inverse labels \(\mu,\mu^{-1}\); a positive conductor forces both ramified, so both Tate factors are one. A special representation at this level has ramified \(\chi\), again giving factor one. All cases have \(L_p(f,u)=1\) by (1.6). The newform Euler product identifies its bad-prime factor with \((1-a_p p^{-u})^{-1}\), hence \(a_p=0\). ∎

The trivial-character condition matters. With ramified nebentype a principal series can have one ramified label and one unramified label, and a nontrivial linear factor even at a higher level.

**Corollary 2.3.** With trivial central character, an odd conductor exponent at least three forces a supercuspidal representation.

**Proof.** Principal-series conductors are even. A special conductor is either one or even. These exhaust the nonsupercuspidal generic types, so neither can have the specified exponent. ∎

Even exponents do not determine a type. A ramified principal series, a ramified special twist and a supercuspidal can all have even conductor. The assertions \(a_p=0\) and \(r_p\ge2\) do not alone distinguish them.

## 3. Reading the reduction of an elliptic curve

Let \(E/\mathbb Q\) be an elliptic curve. We use the modularity theorem as an input: there is a weight-two rational newform whose Galois representation in convention (1.1) is \(V_\ell E\). The published elliptic-curve prerequisite uses
\[
H_\ell(E)=(V_\ell E)^\vee,
\qquad L_p(E,u)=L\bigl(u,\operatorname{WD}(H_\ell(E))\bigr).
\]
Thus (1.3) becomes
\[
\operatorname{rec}(\pi_{E,p})
=\operatorname{WD}(H_\ell(E))^{\mathrm{F\text{-}ss}}\otimes\|\cdot\|^{1/2}.
\tag{3.1}
\]
Carayol's corollary in §0.8 gives equality of the curve's conductor with the associated newform's level and equality of their factors. Modularity supplies the newform for every elliptic curve; [Breuil–Conrad–Diamond–Taylor 2001, Theorem A] is the general theorem.

The following table is an application of the prerequisite's reduction/parameter results, with the extra half twist performed in (3.1).

| Reduction | Unitary parameter | Local representation | Conductor |
|---|---|---|---:|
| Good | unramified \(r\), \(N=0\), roots of \(T^2-a_p p^{-1/2}T+1\) | unramified principal series | 0 |
| Split multiplicative | \(S_2\) | \(\mathrm{St}_2\) | 1 |
| Nonsplit multiplicative | \(\eta_{\mathrm{ur}}S_2\) | \(\mathrm{St}_{\eta_{\mathrm{ur}}}\) | 1 |
| Additive potentially multiplicative | \(\chi S_2\), \(\chi\) ramified quadratic | \(\mathrm{St}_\chi\) | \(2a(\chi)\) |
| Additive potentially good | \((r,0)\), finite nontrivial inertia, no fixed vector | principal series or supercuspidal | \(2+\mathrm{Sw}(r)\) |

The potentially good case is principal series precisely when the Weil representation splits into two characters; it is supercuspidal when that representation is irreducible. Inertia characters alone need not settle this: Frobenius can interchange their two eigenspaces. For tame potentially good inertia of order \(e>2\), its characters are inverse faithful characters. If \(p\equiv1\pmod e\), Frobenius preserves the two distinct eigenspaces, so the Weil representation splits. If \(p\equiv-1\pmod e\), it interchanges them, so no line is invariant under both inertia and Frobenius and the representation is irreducible. Scalar inertia of order two gives a split Weil representation after diagonalizing Frobenius. These deductions use the prerequisite's explicit tame matrices; they are not a classification of wild inertia.

**Example 3.1 (level eleven).** Take \(E:y^2+y=x^3-x^2-10x-20\), the curve used in the non-supercuspidal lesson. Its discriminant is \(-11^5\) and \(c_4=496\). The reduction at 11 is split multiplicative; the node's tangent cone is \(Y^2-3X^2=(Y-5X)(Y+5X)\). Thus \(a_{11}=1\), \(\pi_{E,11}=\mathrm{St}_2\), and (3.1) gives \(S_2\). The geometric-Frobenius value on its kernel is \(11^{-1/2}\), while the arithmetic elliptic-curve factor is \((1-11^{-u})^{-1}\). Both statements have the same sign and different, specified centers. The epsilon factor for conductor-zero additive character is \(-11^{1/2-s}\).

At 2 the point count gives \(a_2=-2\); at 3 it gives \(a_3=-1\). Formula (1.4) gives the unitary Frobenius pairs \((-1\pm i)/\sqrt2\) and \((-1\pm i\sqrt{11})/(2\sqrt3)\). Their products are one. At a good prime the classical determinant is instead \(p\); its removal is the purpose of the half twist.

## 4. A fully labeled dihedral component at three

For
\[
E_{27}:y^2+y=x^3-7,
\]
the prerequisite's Example 6.2 computes \(\Delta=-3^9\), \(j=0\), Kodaira type \(IV^*\), seven geometric components and
\[
f_3(E_{27})=9+1-7=3.
\tag{4.1}
\]
The model is minimal. It is additive potentially good, so \(N=0\), \(L_3=1\) and Swan conductor one. Compatibility and Corollary 2.3 therefore make its local representation supercuspidal. Its CM field is \(K=\mathbb Q(\zeta)\), \(\zeta=e^{2\pi i/3}\); the automorphism \((x,y)\mapsto(\zeta x,y)\) supplies the nontrivial complex multiplication.

We now determine the actual inducing character. This requires more than the words “CM by \(K\).” Set
\[
\lambda=1-\zeta,\qquad
\lambda^2=-3\zeta,\qquad N_{K/\mathbb Q}(\lambda)=3.
\]
The ring \(\mathbb Z[\zeta]\) is norm Euclidean: a point of the complex plane differs from an Eisenstein lattice point by a number of absolute value at most \(1/\sqrt3<1\). Division with decreasing norm proves that every ideal is principal. The six units \(\mu_6\) map bijectively to \((\mathbb Z[\zeta]/3)^\times\). Indeed the quotient has nine elements and six units; \(\zeta\) has order three in it and \(-1\) has order two. Consequently every ideal prime to 3 has a **unique** generator congruent to one modulo 3.

Define an ideal Hecke character by
\[
\Psi(\mathfrak a)=\text{the generator of }\mathfrak a\text{ congruent to }1\pmod3.
\tag{4.2}
\]
Uniqueness proves multiplicativity. It has infinity type one and conductor \((3)=(\lambda^2)\): on principal ideals with generator congruent to one modulo 3 its value is that generator. Its finite local unit character is nontrivial at \(\zeta\in1+\lambda\mathcal O_{K_3}\), and trivial on \(1+\lambda^2\mathcal O_{K_3}\), proving the exact exponent two.

The theta-series identity
\[
\eta(3z)^2\eta(9z)^2
=\sum_{\substack{\mathfrak a\subset\mathbb Z[\zeta]\\(\mathfrak a,3)=1}}
\Psi(\mathfrak a)e^{2\pi i z N\mathfrak a}
\tag{4.3}
\]
is a stated input [Huber–Liu–McLaughlin–Ye–Yuan–Zhang, Lemma 2.1, equation (2.2), and Table 1]. The expression there sums over elements \(1+3m+3n\zeta\); the unique-generator argument turns it into (4.3).

To identify the curve's precise CM character, use the classical CM theorem of Deuring [Conrad CM, Theorems 3.5, 3.7 and 4.1]. At a good prime ideal it gives a generator of that ideal acting as its arithmetic Frobenius on torsion. The curve has all its 3-torsion over \(K\). Indeed, in the equation \(Y^2=x^3-27/4\), the third division polynomial is \(3x(x^3-27)\). Its eight finite torsion points have \(x=0,Y=\pm3\sqrt{-3}/2\), or \(x=3,3\zeta,3\zeta^2\) and \(Y=\pm9/2\). All lie in \(K\). By [Milne CM, Remark 7.6], as a CM module its 3-torsion is \(\mathbb Z[\zeta]/3\), so Frobenius at every good prime away from 3 is congruent to one modulo 3. Its CM generator is therefore the unique one in (4.2). This fixes the curve's Hecke character and identifies (4.3) with its associated newform; a possible conjugate choice gives the same theta series.

Some coefficient checks make the label concrete: there is no ideal of norm 2, the ideal of norm 4 has normalized generator \(-2\), and the two ideals of norm 7 have generators \(1+3\zeta\) and its conjugate. Hence
\[
a_2=0,\quad a_4=-2,\quad a_7=-1,\quad a_{13}=5.
\tag{4.4}
\]
For 13 use \(4+3\zeta\), whose norm is 13 and trace is 5. Direct point counts on \(E_{27}\) give the same prime coefficients. These checks illustrate the exact identity, rather than being used to prove it from finitely many terms.

Put \(E=K_3=\mathbb Q_3(\sqrt{-3})\). For each local unit \(u\), let \(\epsilon_3(u)\in\mu_6\) be its unique unit representative modulo \(\lambda^2\). Define
\[
\boxed{\quad
\theta(u)=\epsilon_3(u),\qquad
\theta(\lambda)=\frac{1-\zeta}{\sqrt3}=e^{-\pi i/6}.
\quad}
\tag{4.5}
\]
Every element of \(E^\times\) is \(\lambda^m u\), so these data define the entire smooth unitary character. The residue-unit lift is multiplicative because \(\mu_6\to(\mathcal O_E/\lambda^2)^\times\) is an isomorphism. Its conductor is exactly two, and \(\theta(\zeta)=\zeta\).

Here is why (4.5) is the local label, including its uniformizer phase. Unitarize (4.2), so its value on an ideal is \(\Psi(\mathfrak a)/\sqrt{N\mathfrak a}\), and take its archimedean idele character to be \((z/|z|)^{-1}\). For a global number \(a\) prime to 3, the prime-to-3 ideal product is
\((a/|a|)\epsilon_3(a)^{-1}\). Triviality on principal ideles then forces the local value \(\epsilon_3(a)\). Such numbers are dense in the local unit group, giving the first identity in (4.5). For the principal idele \(\lambda\) there are no other finite valuations, and its archimedean phase is \(((1-\zeta)/\sqrt3)^{-1}\). This forces the second identity. Thus the sign of the square root is determined, rather than left as an arbitrary unramified twist.

The global quadratic automorphic-induction theorem [Jacquet–Langlands 1970, Proposition 12.1] says that these local Weil-construction representations form the cuspidal representation attached to the Hecke theta series. The character is not invariant under conjugation, as is already visible at infinity. Its local representation at three is therefore
\[
\pi_{f,3}=\Pi_E(\theta),\qquad
\operatorname{rec}(\pi_{f,3})
=\operatorname{Ind}_{W_E}^{W_{\mathbb Q_3}}\widehat\theta,
\qquad N=0.
\tag{4.6}
\]
This uses the Weil-construction label of the dihedral lesson, not a depth-zero finite-field label. The character has positive depth; no depth-zero rectifier is inserted.

We can check every identifying invariant. Conjugation sends \(\zeta\) to \(\zeta^2\), so \(\theta\ne\theta^\sigma\) and induction is irreducible. The extension is tame ramified quadratic: \(e=2,f=1,d=1\). The conductor formula from the dihedral lesson gives
\[
a(\operatorname{Ind}\theta)=1\cdot(2+1)=3.
\tag{4.7}
\]
Its standard factor is one. On rational units \(\theta\) is the quadratic character modulo 3. Moreover
\[
\theta(3)=\theta(-1)\theta(\zeta)^{-1}\theta(\lambda)^2
=(-1)\zeta^{-1}(-\zeta)=1.
\]
These are exactly the values of \(\eta_{E/\mathbb Q_3}\): its unit restriction is the nontrivial residue quadratic character, and \(3=N\lambda\) has value one. Hence \(\theta|_{\mathbb Q_3^\times}\eta_{E/\mathbb Q_3}=1\), verifying the trivial central character and determinant. Finally, for any additive character \(\psi\), its epsilon factor is the completely specified value
\[
\epsilon(s,\pi_{f,3},\psi)
=\lambda(E/\mathbb Q_3,\psi)
\epsilon_E(s,\theta,\psi\circ\operatorname{Tr}).
\tag{4.8}
\]
Both the character and the induction constant's normalization were specified; the conductor exponent of (4.8) is three for conductor-zero \(\psi\).

## 5. The wild prime in the level-32 example

Take \(E_{32}:y^2=x^3-x\). The elliptic-curve prerequisite's Example 6.3 gives \(\Delta=64\), \(j=1728\), type III with two geometric components, and
\[
f_2(E_{32})=6+1-2=5.
\tag{5.1}
\]
Thus \(N=0\), the Swan term is three and \(\pi_{f,2}\) is supercuspidal. The form is
\[
f_{32}(z)=\eta(4z)^2\eta(8z)^2
=q-2q^5-3q^9+6q^{13}+\cdots,
\]
as recorded in [LMFDB, newform orbit 32.2.a.a] and [Huber–Liu–McLaughlin–Ye–Yuan–Zhang, Table 1 and Lemma 2.1, equation (2.3)]. Its CM field is \(\mathbb Q(i)\), as is also seen on the curve from \((x,y)\mapsto(-x,iy)\).

There is an explicit local label here too. Set \(E=\mathbb Q_2(i)\), \(\varpi=1+i\). The four units \(\mu_4\) map bijectively to \((\mathcal O_E/\varpi^3)^\times\), a group of order four. Their distinctness follows from \(v_E(i-1)=1\) and \(v_E(-1-1)=2\). Let \(\epsilon_2(u)\) be the unique representative, and define
\[
\theta_2(u)=\epsilon_2(u),\qquad
\theta_2(1+i)=\frac{1+i}{\sqrt2}.
\tag{5.2}
\]
Its conductor is exactly three: it is trivial on \(1+\varpi^3\mathcal O_E\), while \(-1\in1+\varpi^2\mathcal O_E\) has value minus one. The different exponent of \(\mathbb Q_2(i)/\mathbb Q_2\) is two, from its integral basis discriminant \(-4\). Thus
\[
a(\operatorname{Ind}\theta_2)=3+2=5.
\tag{5.3}
\]
Conjugation changes its value on \(i\), so induction is irreducible. Since \((1+i)^2=2i\), we have \(\theta_2(2)=1\). On rational odd units it is the character modulo 4, the unit restriction of \(\eta_{E/\mathbb Q_2}\). The determinant is again trivial.

To identify this label, the Gaussian integers are norm Euclidean and every ideal prime to 2 has a unique generator congruent to one modulo \((1+i)^3\). Writing that generator as \(a+bi\), the condition is
\[
a\text{ odd},\qquad b\text{ even},\qquad a+b\equiv1\pmod4.
\]
The parametrization \(a=2m-2n+1,b=2m+2n\) in the cited theta identity is exactly this condition. To fix the curve's CM character, its \((1+i)^3\)-torsion is all defined over \(\mathbb Q(i)\). Its kernel consists of the four 2-torsion points, together with \((i,\pm(1-i))\) and \((-i,\pm(1+i))\). The latter four double to \((0,0)\), which is the kernel of \([1+i]\); since \((1+i)^2=2i\), all eight are killed by \((1+i)^3\). For example, doubling \((i,1-i)\) has tangent slope \(-1-i\), giving doubled coordinates \((0,0)\). These are eight distinct points, the degree of that CM endomorphism, so they exhaust its kernel. The CM Frobenius theorem now forces every good-prime ideal generator to be congruent to one modulo \((1+i)^3\), as required. The same principal-idele calculation as in Section 4 gives (5.2), and quadratic automorphic induction gives \(\pi_{f,2}=\Pi_E(\theta_2)\).

In particular this dyadic supercuspidal is dihedral, even though primitive parameters are possible at two. Good-prime checks use the primary generators \(-1+2i\) of norm 5 and \(3+2i\) of norm 13, giving traces \(-2\) and 6, respectively. At 5 the unitary Satake values are \((-1\pm2i)/\sqrt5\), with determinant one. At 2 the factor is one and \(a_2=0\).

## 6. The Atkin–Lehner sign at a multiplicative prime

For trivial nebentype and \(p\parallel N_f\), use the normalized local Atkin–Lehner operator represented by
\[
A_p=\begin{pmatrix}0&1\\-p&0\end{pmatrix}.
\tag{6.1}
\]
Its square is the central matrix \(-p\), which acts trivially, so its eigenvalue on the newvector line is \(w_p\in\{1,-1\}\). The usual classical slash normalization gives this same involution; the sign change to \(\left(\begin{smallmatrix}0&-1\\p&0\end{smallmatrix}\right)\) is central and has no effect here [Stein, §10.5]. This convention for \(w_p\) is part of the assertion.

**Proposition 6.1.** With (6.1),
\[
w_p=-b_p,\qquad a_p=-w_p p^{k/2-1}.
\tag{6.2}
\]
For an elliptic curve this gives \(w_p=-1\) in the split multiplicative case and \(w_p=1\) in the nonsplit case.

**Proof.** Put \(a_r=\operatorname{diag}(p^r,1)\) and \(w=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\). The Steinberg Iwahori newvector, normalized by \(W(1)=1\), satisfies
\[
W(a_r w)=-p^{-r-1}\quad(r\ge-1),
\tag{6.3}
\]
as proved in the local-factor lesson, Section 6, equation (5.4). In particular \(W(a_{-1}w)=-1\). For \(\mathrm{St}_{\chi_p}\), twist this function by \(\chi_p\circ\det\). Because
\[
A_p=pI_2\,a_{-1}w,
\]
the central factor is \(\chi_p(p)^2=1\), while the determinant twist at \(a_{-1}w\) is \(\chi_p(p^{-1})=b_p\). Thus \(W_{\chi_p}(A_p)=-b_p\). The operator normalizes the Iwahori subgroup and preserves its one-dimensional fixed space; evaluating its scalar action at the identity gives \(w_p=-b_p\). Combine with (2.3).

For a Tate curve the prerequisite gives the covariant pair \(\chi_p\mathrm{Sp}(2)\), with \(\chi_p\) the unramified splitting character. Dualizing and taking the half norm twist gives \(\chi_p S_2\) in (3.1). Its kernel before unitarization has value \(\chi_p(\Phi_p)=1\) or \(-1\), so \(a_p=b_p\) in weight two. The calculation just made yields the two stated Atkin–Lehner signs. ∎

This proof retains the Tate curve's nonzero monodromy. Taking the full semisimplification of its Galois representation would destroy the kernel calculation that gives both the linear factor and the conductor one.

## 7. History and the role of the theorem

Langlands' Antwerp work and Deligne's 1973 letter treated bad-prime representations through modular-curve geometry. The letter's opening records an exception at two; part (B), “The fundamental local construction,” organizes a local construction from supersingular elliptic curves, formal groups and level data. That source is a historical precursor, not a theorem establishing all the cases in (1.3). Deligne's *Formes modulaires et représentations de GL(2)*, §3.2.7, explicitly relates the local correspondence to the elliptic-curve representation and distinguishes its Hecke convention.

Carayol's Theorem (A) determines the local representation at every finite prime distinct from the coefficient characteristic, including the exceptional primitive cases. Its introduction separates a geometric intermediate Theorem (B) from the final base-change argument. The theorem is proved using Shimura-curve cohomology, vanishing cycles and local representation theory. Our computations use the resulting identification; they do not prove that geometric compatibility. The later course lessons explain the higher-rank existence methods.

## 8. Exercises and complete solutions

**Exercise 8.1 (easy).** For an elliptic curve with multiplicative reduction at \(p\), determine \(a_p\) and its sign from the Weil–Deligne pair.

**Solution.** The covariant pair is \(\chi\mathrm{Sp}(2)\), with \(\chi\) trivial in the split case and unramified quadratic in the nonsplit case. The dual pair is \(\chi\nu_p^{-1}\mathrm{Sp}(2)\); its kernel has character \(\chi\), hence eigenvalue \(b=\chi(p)\). Its arithmetic factor is \((1-bp^{-u})^{-1}\), so \(a_p=b=1\) for split reduction and \(-1\) for nonsplit reduction. The unitary parameter is \(\chi S_2\); its kernel has eigenvalue \(bp^{-1/2}\), giving the same factor after \(u=s+1/2\). Its conductor is one, since inertia invariants have dimension two and the invariant kernel has dimension one.

**Exercise 8.2 (medium).** Prove that an odd conductor exponent at least three with trivial central character forces a supercuspidal local component.

**Solution.** The component of a cuspidal newform is generic, so it is principal series, special or supercuspidal. Trivial central character gives inverse principal-series labels and conductor \(2a(\mu)\). For a special twist the conductor is one if its character is unramified and \(2a(\chi)\) otherwise. Both exclude odd exponents at least three. Hence the component must be supercuspidal. This argument does not prove the converse and does not classify components of even conductor.

**Exercise 8.3 (medium).** Determine the component at three of the level-27 form as a Weil-constructed representation \(\Pi_E(\theta)\).

**Solution.** Set \(E=\mathbb Q_3(\zeta)\), \(\lambda=1-\zeta\). On \(\mathcal O_E^\times\), take \(\theta(u)\) to be the unique sixth root of unity congruent to \(u\) modulo \(\lambda^2\), and set \(\theta(\lambda)=(1-\zeta)/\sqrt3\). The local unit quotient has six elements and is identified with \(\mu_6\), so these values define a smooth character of all \(E^\times\). It is trivial on \(1+\lambda^2\mathcal O_E\) and has \(\theta(\zeta)=\zeta\ne1\), with \(\zeta\in1+\lambda\mathcal O_E\); thus its conductor is two. Conjugation changes that value to \(\zeta^2\), proving regularity. The different exponent is one, so induction has conductor three. On rational units it equals the quadratic residue character, and \(\theta(3)=1\); these give \(\theta|_{\mathbb Q_3^\times}\eta=1\), the required central character. The exact theta identity (4.3) identifies the global Hecke character, its principal-idele relation fixes the displayed uniformizer value, and Jacquet–Langlands Proposition 12.1 identifies the local component with \(\Pi_E(\theta)\). Its parameter is \(\operatorname{Ind}\widehat\theta\), with zero monodromy, factor one and conductor three. The character is specified completely, rather than only up to an unramified twist.

**Exercise 8.4 (hard).** Use the Tate-curve parameter and the normalized Atkin–Lehner operator to derive \(a_p=-w_p\) in weight two.

**Solution.** The Tate parameter is \(\chi\mathrm{Sp}(2)\) on the covariant module. Dualization gives kernel character \(\chi\), so \(a_p=\chi(p)=b\). The half norm twist gives \(\chi S_2\), corresponding to \(\mathrm{St}_\chi\). Its normalized Iwahori newvector has \(W(a_{-1}w)=-1\), and twisting multiplies this by \(\chi(p^{-1})=b\). Since \(A_p=pI_2a_{-1}w\) and the central character is trivial, \(W(A_p)=-b\). The one-dimensional newvector line makes this value its Atkin–Lehner eigenvalue \(w_p\). Hence \(a_p=b=-w_p\). Split and nonsplit multiplicative reduction give \((a_p,w_p)=(1,-1)\) and \((-1,1)\). The same local calculation combined with (2.5) gives \(a_p=-w_pp^{k/2-1}\) in general weight.

## What this lesson does not prove

Deligne's construction of newform Galois representations and their good-prime Frobenius polynomial are prerequisites; [Taylor 2004, §3, Theorem 3.6] gives the compatibility framework. The local–global theorem itself is [Carayol 1986, Theorem (A), §§0.3–0.8], with the rational-field specialization and our conventions stated in (1.3). Frobenius and dual normalization checks, the conductor deduction, bad-prime coefficient formulas and the odd-conductor type criterion were proved here. The weight-two modularity theorem is [Breuil–Conrad–Diamond–Taylor 2001, Theorem A].

The adelic newform dictionary, genericity and Euler factors are [Jacquet–Langlands 1970, §§2 and 11]; the generic newvector theorem is [Getz–Hahn 2022, §11.5, Proposition 11.5.1 and Theorem 11.5.6]. The classification and all non-supercuspidal factor/conductor formulas, the supercuspidal vanishing of standard factors and the explicit Steinberg Iwahori function are earlier proved course results. Their generic hypotheses are retained. The Atkin–Lehner normalization is [Stein, §10.5], and its local scalar and the resulting sign formula were computed in Section 6.

The reduction, Tate-module extension, conductor formulas and actual Tate-algorithm branches for the three curves are the published elliptic-curve prerequisite, Theorems 4.1–5.1 and Examples 6.1–6.3. Their external geometric inputs include [Milne EC2, Chapter II, §§3–4 and 7–8; Chapter III, §3; Chapter IV, §10] and the specified branches of Cremona's algorithm. Those geometric results are not re-proved here. The tame inertia matrices are that prerequisite's Proposition 2.2; we deduced their local representation types.

The CM curve/Hecke-character theory is [Conrad CM, Theorems 3.5, 3.7 and 4.1] and [Milne CM, Remark 7.6]. The two exact eta/theta identities are [Huber–Liu–McLaughlin–Ye–Yuan–Zhang, Lemma 2.1, equations (2.2)–(2.3), Table 1]. Quadratic global automorphic induction with its local components is [Jacquet–Langlands 1970, Proposition 12.1]. The ideal generators, complete local unit/uniformizer labels, regularity, determinants and conductor calculations were given explicitly. The ideal norm and different formulas use local class field and ramification prerequisites. No reconstruction of a ramified local character from the single value \(a_p=0\) is asserted.

## References

- [Carayol 1986] Henri Carayol, [“Sur les représentations \(\ell\)-adiques associées aux formes modulaires de Hilbert”](https://www.numdam.org/item/ASENS_1986_4_19_3_409_0/), *Annales scientifiques de l'École Normale Supérieure* 19 (1986), 409–468, Introduction §§0.3–0.11, Theorems (A) and (B), and §0.8 corollary.
- [Deligne 1973] Pierre Deligne, [*Formes modulaires et représentations de GL(2)*](https://publications.ias.edu/sites/default/files/Number21.pdf), in *Modular Functions of One Variable II*, Lecture Notes in Mathematics 349, Springer, 1973, 55–105, §§3.2.3–3.2.7.
- [Deligne 1973 letter] Pierre Deligne, [letter to Ilya Piatetski-Shapiro](https://publications.ias.edu/sites/default/files/deligne73.pdf), 25 March 1973, opening and part (B), “The fundamental local construction.”
- [Taylor 2004] Richard Taylor, [“Galois representations”](https://www.numdam.org/item/AFST_2004_6_13_1_73_0/), *Annales de la faculté des sciences de Toulouse* 13 (2004), 73–119, §3 and Theorem 3.6.
- [Blasius 2006] Don Blasius, [*Hilbert Modular Forms and the Ramanujan Conjecture*](https://arxiv.org/abs/math/0511007), in *Noncommutative Geometry and Number Theory*, Vieweg, 2006, §§2.3–2.4.
- [Jacquet–Langlands 1970] Hervé Jacquet and Robert P. Langlands, [*Automorphic Forms on GL(2)*](https://publications.ias.edu/sites/default/files/Automorphic-forms-on-GL2.pdf), Lecture Notes in Mathematics 114, Springer, 1970, §§2 and 11, and Proposition 12.1.
- [Getz–Hahn 2022] Jayce R. Getz and Heekyoung Hahn, [*An Introduction to Automorphic Representations, with a View toward Trace Formulae*](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), draft of 22 April 2022, §11.5.
- [Milne EC2] J. S. Milne, [*Elliptic Curves*](https://www.jmilne.org/math/Books/EC2.pdf), second edition, World Scientific, 2020, Chapter II, §§3–4 and 7–8, Chapter III, §3, and Chapter IV, §10.
- [Conrad CM] Brian Conrad, [*Main theorem of complex multiplication*](https://math.stanford.edu/~conrad/vigregroup/vigre04/mainthm.pdf), seminar notes, §§3–4, Theorems 3.5, 3.7 and 4.1.
- [Milne CM] J. S. Milne, [*Complex Multiplication*](https://www.jmilne.org/math/CourseNotes/CM.pdf), course notes, version of 14 July 2020, Remark 7.6.
- [Huber–Liu–McLaughlin–Ye–Yuan–Zhang] Tim Huber, Chang Liu, James McLaughlin, Dongxi Ye, Miaodan Yuan and Sumeng Zhang, [*On the Vanishing of the Coefficients of CM Eta Quotients*](https://www.wcupa.edu/sciences-mathematics/mathematics/jMcLaughlin/documents/Huber_Liu_McLaughlin_Ye_Yuan_Zhang_CM_eta_quotients_r2.pdf), author version, Table 1 and §2.1, Lemma 2.1, equations (2.2)–(2.3).
- [LMFDB] [Newform orbit 32.2.a.a](https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/32/2/a/a/), properties, eta expression and q-expansion.
- [Stein] William A. Stein, [*Explicitly Computing Modular Forms*](https://www.wstein.org/msri06/refs/stein-book-on-modular-forms.pdf), §10.5, the normalization of the Atkin–Lehner operator.
- [Breuil–Conrad–Diamond–Taylor 2001] Christophe Breuil, Brian Conrad, Fred Diamond and Richard Taylor, [“On the Modularity of Elliptic Curves over \(\mathbb Q\): Wild 3-adic Exercises”](https://math.stanford.edu/~conrad/papers/tswfinal.pdf), *Journal of the American Mathematical Society* 14 (2001), 843–939, Theorem A.
