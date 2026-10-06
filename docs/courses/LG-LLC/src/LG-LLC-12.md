# Other proofs, functoriality and the formal-degree formula

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*

The existence theorem can be approached through geometric realization, through global constructions and numerical counting, or through a local trace characterization. These approaches establish the same factor-normalized correspondence. Further compatibility statements say what happens when one changes the field, induces a parameter, or applies a representation of the dual group.

We state the other existence theorems and explain their mechanisms. We prove unramified base change and induction explicitly, calculate the rank-two exterior square, and verify the formal-degree formula for Steinberg. A depth-zero example checks the same normalization on a supercuspidal.

## 1. Three approaches to existence

Throughout the characteristic-zero portions let \(F/\mathbb Q_p\) be finite. The reciprocity and geometric norm conventions are unchanged:
\[
\operatorname{Art}_F(\varpi_F)=\Phi_F,\qquad
\|\Phi_F\|=q^{-1}.
\]

**Theorem 1.1 (Henniart, stated).** The simultaneous local Langlands bijections for all \(\mathrm{GL}_n(F)\) exist and preserve the pair \(L\)- and epsilon factors, central characters, twists and duals. Henniart's proof [Henniart 2001, §§2–5; Carayol 2000, §4] constructs the supercuspidal correspondence using global automorphic constructions, non-Galois automorphic induction and his numerical correspondence. It does not require the analysis of bad reduction used to realize the correspondence geometrically in Harris–Taylor.

The author's detailed account [Henniart 2001, §1, Theorem 1.3; §§2–5] presents a variant of the original 2000 proof and specifies its relationship to it in §§2.4 and 4.5; [Carayol 2000, §4] gives another account of the method. These are accounts of the same existence result, not competing normalizations.

One useful mechanism appears in [Henniart 2001, §§3.2–3.5]. Consider free abelian groups on irreducible Weil representations and on supercuspidals. Pair factors define bilinear forms through orders of poles at \(s=0\). In each group the irreducible basis is orthonormal. The global construction produces a degree-preserving map compatible with those forms and factors. If an irreducible Weil representation maps to
\[
x=\sum_i a_i[\pi_i],\qquad a_i\in\mathbb Z,
\]
orthonormality gives
\[
1=(x,x)=\sum_i a_i^2.
\tag{1.1}
\]
Exactly one coefficient is \(1\) or \(-1\); preserving the positive degree rules out the negative choice. Thus the virtual object is a genuine supercuspidal. Equality of the bilinear forms also gives injectivity. The numerical theorem then supplies surjectivity. The deep input is constructing the map and proving the factor comparisons; (1.1) explains why a virtual construction can give an actual representation.

For positive characteristic write \(F=\mathbb F_q((t))\), or more generally take a nonarchimedean local field of characteristic \(p\).

**Theorem 1.2 (Laumon–Rapoport–Stuhler, stated).** The local Langlands correspondence for \(\mathrm{GL}_n(F)\) exists in this case, with the same factor and operation compatibilities. [Laumon–Rapoport–Stuhler 1993, Theorem 15.7] first states it for supercuspidals with finite-order central character and \(\ell\)-adic irreducible Galois representations with finite-order determinant. Remark 15.8 extends it by unramified twists and the representation classification to all irreducibles and Frobenius-semisimple Weil–Deligne parameters.

Their global geometric objects are \(D\)-elliptic sheaves on a curve over a finite field, where \(D\) is a central division algebra over its function field. These are bundles with an order action, meromorphic Frobenius and periodicity conditions. The relevant moduli have dimension \(n-1\); taking \(D\) to be a division algebra makes them projective. A Hecke–Frobenius fixed-point calculation identifies Galois representations in their cohomology. Globalizing the prescribed local data produces local factor comparison; numerical counting supplies surjectivity. The Introduction and §§14–15 explain these steps. This argument establishes local LLC in all ranks; it does not assert that the paper constructs every global cuspidal representation over a function field.

## 2. Scholze's trace characterization

Scholze replaces a prescribed cohomological multiplicity by a family of local test functions. The deformation spaces here allow one-dimensional divisible \(\mathcal O_F\)-modules with an étale part, as well as the connected formal modules of the Lubin–Tate tower.

Let \(F_r/F\) be unramified of degree \(r\ge1\), and let \(\tau\in W_F\) project to \(\Phi_F^r\). For a compactly supported locally constant function \(h\) on \(\mathrm{GL}_n(\mathcal O_F)\), the deformation and level spaces define a nearby-cycle test function \(\phi_{\tau,h}\) on \(\mathrm{GL}_n(F_r)\). Transfer of twisted orbital integrals gives \(f_{\tau,h}\) on \(\mathrm{GL}_n(F)\); its representative is not unique, but its representation traces are.

**Theorem 2.1 (Scholze, stated).** There is a unique semisimple \(n\)-dimensional Weil representation \(R_{\mathrm{tr}}(\pi)\) for each irreducible smooth \(\pi\) such that
\[
\operatorname{tr}\pi(f_{\tau,h})
=\operatorname{tr}R_{\mathrm{tr}}(\pi)(\tau)\,
\operatorname{tr}\pi(h)
\tag{2.1}
\]
for all the preceding \(\tau,h\). Put
\[
\sigma(\pi)=R_{\mathrm{tr}}(\pi)\otimes\|\cdot\|^{(1-n)/2}.
\tag{2.2}
\]
The assignment \(\sigma\) commutes with normalized parabolic induction on supercuspidal support, gives a bijection from supercuspidals to irreducible Weil representations, and satisfies the standard twist, central-character, dual and pair-factor compatibilities.

This is [Scholze, Introduction, Theorems 1.1–1.2]. The functions are defined from alternating nearby-cycle traces, with the transpose-inverse operation on \(h\) specified there. We have renamed the paper's trace assignment \(R_{\mathrm{tr}}\) to distinguish it from this course's rec. Its Tate twist in (2.2) is exactly the stated half norm in the geometric-Frobenius convention. Thus on a supercuspidal \(\sigma(\pi)=\operatorname{rec}_F(\pi)\); on a general irreducible, it is the semisimple underlying Weil representation and does not include \(N\).

The proof uses geometry of inertia-invariant nearby cycles to establish bijectivity before the pair-factor comparison. This avoids reliance on the numerical local Langlands theorem for that step. The remaining local-factor identification uses global automorphic induction and ramified twisting [Scholze, §§12–14]. The trace test needs the cutoff \(h\): a single compactly supported function cannot have the desired nonzero traces in every Bernstein component.

Fargues and Scholze give a further geometric framework for general reductive groups over nonarchimedean local fields. Their stack \(\operatorname{Bun}_G\) parametrizes \(G\)-bundles on the Fargues–Fontaine curve. Geometric Satake produces dual-group actions; Hecke and excursion operators produce semisimple Weil \(L\)-parameters for irreducible smooth representations.

**Theorem 2.2 (Fargues–Scholze, stated).** With algebraically closed \(\ell\)-adic coefficients, \(\ell\ne p\), their construction attaches a continuous semisimple \(L\)-parameter to every irreducible smooth representation. It has the twist, central-character, dual, restriction-of-scalars and parabolic-induction properties in [Fargues–Scholze, Theorem I.9.6]. For \(\mathrm{GL}_n\) it agrees with usual LLC on supercuspidals and with its semisimple Weil parameter in general. Their spectral action is [Theorem I.10.1].

The categorical equivalence in Conjecture I.10.2 is presented there as a conjecture. A constructed semisimple parameter and spectral action do not by themselves establish all packet identifications, monodromy information or that equivalence. These assertions give a precise entry point to the geometric theory.

## 3. Conductors and cyclic functoriality

Let \(\rho=\operatorname{rec}_F(\pi)\). The conductor attached to \(\pi\)'s standard local epsilon factor satisfies
\[
a(\pi)=a(\rho).
\tag{3.1}
\]
Indeed, for an additive character of conductor zero, the exponent of \(q^{-s}\) in that epsilon factor is the conductor exponent. Pair compatibility with the trivial rank-one representation identifies it with the Artin–monodromy exponent on the right. For generic \(\pi\) this agrees with the newform conductor. For nongeneric representations, a statement about minimal fixed vectors under a newform subgroup would require a separate hypothesis; (3.1) is the factor conductor.

For a cyclic finite extension \(E/F\), local cyclic base change and local automorphic induction are compatible with restriction and induction of parameters:
\[
\begin{aligned}
\operatorname{rec}_E(\operatorname{BC}_{E/F}\pi)
&=\operatorname{rec}_F(\pi)|_{W'_E},\\
\operatorname{rec}_F(\operatorname{AI}_{E/F}\pi_E)
&=\operatorname{Ind}_{W'_E}^{W'_F}\operatorname{rec}_E(\pi_E).
\end{aligned}
\tag{3.2}
\]
One may express \(W'_F\) as \(W_F\times\mathrm{SL}_2(\mathbb C)\); induction acts on the Weil part and retains the commuting \(\mathrm{SL}_2\)-action. This specifies the monodromy normalization. Induction increases the dimension by \([E:F]\).

The compatibility on semisimple Weil classes is [Henniart 2001, §§7.2–7.3, Properties 1–2]. That passage alone does not compare monodromy operators. The full-parameter formulation in (3.2) uses the usual extension of the cyclic operations to the segment classification: on each block \(\sigma\otimes S_k\), restrict or induce \(\sigma\) and keep \(S_k\), then form the corresponding Langlands quotient. Decomposing the resulting semisimple Weil representation gives the segment data, so the earlier classification verifies (3.2) for this extension, including its monodromy. The existence of the original cyclic representation-theoretic operations is the Arthur–Clozel/Henniart–Herb input identified in that passage. A base change can cease to be supercuspidal, and an automorphic induction can be a principal-series representation. Neither operation has a general irreducibility assertion on the underlying Weil representation.

The global analogues carry a representation over \(\mathbb A_F\) to one over \(\mathbb A_E\), or a representation over \(\mathbb A_E\) to one over \(\mathbb A_F\), respectively. In prime cyclic degree, a cuspidal base change stays cuspidal precisely when there is no nontrivial self-twist by a character of the cyclic extension; automorphic induction stays cuspidal precisely when the inducing cuspidal representation is not invariant under its nontrivial Galois action. These are the global theorems discussed in [Getz–Hahn, §13.5], with the field of the inducing representation taken to be \(E\).

## 4. Unramified base change, with proof

**Proposition 4.1.** Let \(E/F\) be unramified of degree \(f\). If \(\rho\) is unramified with \(N=0\) and Frobenius eigenvalues \(\alpha_1,\ldots,\alpha_n\), its restriction has eigenvalues \(\alpha_1^f,\ldots,\alpha_n^f\), and
\[
L_E(s,\rho|_{W_E})
=\prod_{i=1}^n(1-\alpha_i^f q^{-fs})^{-1}.
\tag{4.1}
\]
Thus unramified base change raises the Satake parameters to the \(f\)-th power.

**Proof.** The inertia groups are equal, and a geometric Frobenius of \(E\) is \(\Phi_F^f\) modulo inertia. Inertia acts trivially on \(\rho\), so its matrix is exactly \(\rho(\Phi_F)^f\). Frobenius semisimplicity gives the asserted eigenvalues. The residue cardinality is \(q_E=q^f\); applying the determinant definition of the local \(L\)-factor gives (4.1). Compatibility (3.2) identifies these with the Satake eigenvalues of the spherical base change. ∎

For example an unramified rank-two parameter with eigenvalues \(a,b\) becomes \((a^3,b^3)\) under degree-three unramified base change. The factor is \((1-a^3q^{-3s})^{-1}(1-b^3q^{-3s})^{-1}\). It need not equal the old factor with the same variable and residue cardinality.

## 5. Unramified induction, with proof

**Proposition 5.1.** Let \(E/F\) be unramified of degree \(n\) and let \(\theta\) be an unramified character of \(E^\times\). Put \(a=\theta(\varpi_E)\ne0\). Then \(\operatorname{Ind}_{W_E}^{W_F}\widehat\theta\) is unramified, has zero monodromy, and its Frobenius characteristic polynomial and local factor are
\[
P_\Phi(T)=T^n-a,\qquad
L_F(s,\operatorname{Ind}\widehat\theta)
=(1-aq^{-ns})^{-1}
=\prod_{\zeta^n=1}(1-\zeta a^{1/n}q^{-s})^{-1}.
\tag{5.1}
\]

**Proof.** Choose coset representatives \(1,\Phi_F,\ldots,\Phi_F^{n-1}\). In a basis for induction compatible with these representatives, the Frobenius operator \(A\) is the cyclic shift
\[
Ae_j=e_{j+1}\ (0\le j<n-1),\qquad Ae_{n-1}=a e_0.
\tag{5.2}
\]
Changing between the function and tensor models of induction may reverse the basis ordering; (5.2) is the companion matrix convention. It is determined by \(A^n=a\), since \(\Phi_F^n=\Phi_E\) acts through \(\widehat\theta(\Phi_E)=a\). Inertia fixes every basis vector because it lies in \(W_E\) and \(\theta\) is trivial there.

The vector \(e_0\) is cyclic, and \(A^n e_0=a e_0\). Thus both the minimal and characteristic polynomial are \(T^n-a\). It has distinct roots over \(\mathbb C\), namely \(\zeta a^{1/n}\). The representation is therefore a direct sum of unramified one-dimensional characters with these Frobenius values. Taking \(\det(1-q^{-s}A)^{-1}\) gives the product in (5.1), and the polynomial identity \(\prod_{\zeta^n=1}(1-\zeta x)=1-x^n\) gives its first expression. Choosing another \(n\)-th root merely permutes the factors. ∎

For \(n>1\) this induction is reducible as a Weil representation. Its automorphic induction is the spherical representation with those Satake parameters. For \(n=2\) they are \(a^{1/2},-a^{1/2}\); their ratio is \(-1\), so their normalized principal series is irreducible by the rank-two reducibility criterion. This is consistent with the character's failure to be regular for the unramified extension: it is fixed by its Galois group.

## 6. Formal degrees: measure and two complete checks

For a unitary square-integrable representation \(\pi\), the formal degree for a Haar measure \(\mu\) on \(G/Z\) is defined by Schur orthogonality. For a unit vector \(v\),
\[
\int_{G/Z}|\langle\pi(g)v,v\rangle|^2\,d\mu(g)
=d(\pi,\mu)^{-1}.
\tag{6.1}
\]
Multiplying \(\mu\) by \(c>0\) divides the formal degree by \(c\).

For \(G=\mathrm{GL}_n(F)\), choose a conductor-zero additive character and the integral gauge measures on \(G\) and \(Z=F^\times\), then take their quotient \(\mu_\psi\). The maximal compact image \(\overline K\) has volume
\[
\mu_\psi(\overline K)=\prod_{j=2}^n(1-q^{-j}).
\tag{6.2}
\]
To see the constant, the gauge volume of \(\mathrm{GL}_n(\mathcal O_F)\) is \(\#\mathrm{GL}_n(\mathbb F_q)/q^{n^2}=\prod_{j=1}^n(1-q^{-j})\). Dividing by the gauge volume \(1-q^{-1}\) of \(\mathcal O_F^\times\) gives (6.2).

**Theorem 6.1 (formal-degree theorem for \(\mathrm{GL}_n\), stated).** For a unitary square-integrable \(\pi\), with parameter \(\rho\),
\[
d(\pi,\mu_\psi)=\frac1n\,|\gamma(0,\operatorname{Ad}\rho,\psi)|.
\tag{6.3}
\]
Here \(\operatorname{Ad}\) acts on \(\mathfrak{sl}_n(\mathbb C)\), removing the scalar endomorphisms. This is the general-linear-group case of [Hiraga–Ichino–Ikeda 2008, Theorem 3.1]. The gauge convention and an equivalent formula at \(s=1\) are verified directly in [Ichino–Lapid–Mao, Notation and Theorem 2.1]. Their \(d_\pi\) denotes the Schur-normalized measure, rather than the numerical degree in (6.1); taking absolute values and using the gamma functional equation converts their formula to (6.3).

**Proposition 6.2 (Steinberg check).** For \(\mathrm{St}_2\), if \(\mu_0(\overline K)=1\), then
\[
d(\mathrm{St}_2,\mu_0)=\frac{q-1}{2}.
\tag{6.4}
\]
It satisfies (6.3) with \(\mu_\psi=(1-q^{-2})\mu_0\).

**Proof.** The representation-classification lesson, Section 5, proved the Iwahori double-coset description and coefficient formula. For a normalized coefficient \(c\) of its invariant line,
\[
|c(g)|=q^{-\ell(w)}\quad(g\in IwI).
\]
There are two extended-affine-Weyl elements of length zero and four of every positive length. With \(\mu_0(\overline K)=1\), the index \([\overline K:I]=q+1\) gives \(\mu_0(I)=1/(q+1)\), and \(\mu_0(IwI)=q^{\ell(w)}/(q+1)\). Choose the invariant vector to be a unit vector in a unitary realization of Steinberg; its smooth dual coefficient is then this Hermitian coefficient. Hence
\[
\int|c|^2\,d\mu_0
=\frac1{q+1}\left(2+4\sum_{r\ge1}q^{-r}\right)
=\frac2{q-1}.
\tag{6.5}
\]
Equation (6.1) proves (6.4).

The parameter of Steinberg is \(S_2\). Its adjoint parameter is the centered three-dimensional block \(S_3\). The Frobenius weights are \(\|\cdot\|^{-1},1,\|\cdot\|\), and \(N\) has one Jordan block with kernel on the last line. Thus
\[
L(s,\operatorname{Ad}S_2)=(1-q^{-s-1})^{-1}.
\]
The underlying Weil representation is unramified, so its epsilon factor is one. The monodromy determinant on the two-dimensional quotient by the kernel is
\[
\varepsilon(s,\operatorname{Ad}S_2,\psi)
=(-q^{1-s})(-q^{-s})=q^{1-2s}.
\]
This checks conductor two and both signs. The adjoint parameter is self-dual, giving
\[
\gamma(s,\operatorname{Ad}S_2,\psi)
=q^{1-2s}\frac{1-q^{-s-1}}{1-q^{s-2}},
\qquad
\gamma(0,\operatorname{Ad}S_2,\psi)=\frac{q^2}{q+1}.
\tag{6.6}
\]
On the other hand
\[
d(\mathrm{St}_2,\mu_\psi)
=\frac{q-1}{2(1-q^{-2})}
=\frac{q^2}{2(q+1)}.
\]
This is half of (6.6), as required. ∎

For a depth-zero supercuspidal, take an unramified quadratic extension \(E/F\) and a regular unitary tame character \(\theta\). The dihedral-supercuspidal lesson supplies the type description
\[
\pi=\mathrm{c\!-\!Ind}_{F^\times K}^{G}\widetilde\tau,\qquad
\dim\tau=q-1,
\tag{6.7}
\]
where \(\tau\) is a cuspidal representation of \(\mathrm{GL}_2(\mathbb F_q)\), inflated to \(K\). Its parameter is induced from the tame character with the stated rectifier; the rectifier has no effect on the adjoint inertia calculation.

We check the degree in (6.7) rather than assume it. A unit vector supported on \(F^\times K\) has coefficient zero outside this subgroup: distinct support cosets in compact induction are orthogonal. On its image in \(G/Z\) the coefficient is that of the finite-dimensional type. Schur orthogonality for this compact group, with volume one, gives integral \(1/\dim\tau\). Therefore
\[
d(\pi,\mu_0)=q-1,\qquad
d(\pi,\mu_\psi)=\frac{q^2}{q+1}.
\tag{6.8}
\]

For its induced parameter \(r\), the diagonal and off-diagonal endomorphisms give
\[
\operatorname{Ad}r=\eta_{E/F}\oplus
\operatorname{Ind}_{W_E}^{W_F}(\theta/\theta^\sigma).
\tag{6.9}
\]
The quadratic \(\eta_{E/F}\) is unramified with Frobenius value \(-1\). Regularity makes \(\theta/\theta^\sigma\) nontrivial on inertia. Consequently the second summand is tame with no inertia invariants, even when it splits into two ramified characters. Thus \(a(\operatorname{Ad}r)=2\),
\[
L(s,\operatorname{Ad}r)=(1+q^{-s})^{-1},\qquad
|\varepsilon(s,\operatorname{Ad}r,\psi)|=q^{1-2s}
\]
for real \(s\). The unitary Gauss-sum root number has absolute value one, as in the earlier tame-factor calculation. It follows that
\[
|\gamma(0,\operatorname{Ad}r,\psi)|
=q\,\frac2{1+q^{-1}}
=\frac{2q^2}{q+1}.
\tag{6.10}
\]
Half of (6.10) is (6.8). For \(q=3\), the two \(\mu_0\)-degrees are \(1\) and \(2\), while their \(\mu_\psi\)-degrees are \(9/8\) and \(9/4\). The measure conversion accounts for the difference completely.

## 7. Exterior and symmetric squares

**Theorem 7.1 (Cogdell–Shahidi–Tsai, stated).** For \(F/\mathbb Q_p\) finite, any irreducible admissible \(\pi\) of \(\mathrm{GL}_n(F)\), its parameter \(\rho\), and nontrivial additive \(\psi\), the analytic and arithmetic factors agree for \(R=\Lambda^2,\operatorname{Sym}^2\):
\[
\varepsilon(s,\pi,R,\psi)=\varepsilon(s,R\rho,\psi),\qquad
L(s,\pi,R)=L(s,R\rho).
\tag{7.1}
\]
The analytic factors are the Langlands–Shahidi factors, extended to nongeneric representations through the Langlands classification. This is [Cogdell–Shahidi–Tsai 2017, §1, Theorem 1.1]. Their proof combines multiplicativity, globalization, functional equations and stability under ramified twists. General pair compatibility alone does not formally separate the exterior and symmetric summands of \(\rho\otimes\rho\); (7.1) is an additional theorem.

For a two-dimensional Weil–Deligne pair \((r,N)\), its exterior square is particularly explicit:
\[
\Lambda^2(r,N)=(\det r,0).
\tag{7.2}
\]
Indeed the induced nilpotent operator on \(v\wedge w\) is \(Nv\wedge w+v\wedge Nw\); in a basis this acts by \(\operatorname{tr}N=0\). Therefore
\[
a(\Lambda^2\rho)=a(\det r)=a(\omega_\pi).
\tag{7.3}
\]
For Steinberg with trivial central character, this conductor is zero although \(a(S_2)=1\). For a principal-series parameter \(\widehat\chi_1\oplus\widehat\chi_2\), it is \(a(\chi_1\chi_2)\), not necessarily \(a(\chi_1)+a(\chi_2)\). Cancellation in the determinant can lower it.

## 8. Exercises and complete solutions

**Exercise 8.1 (easy).** Compute degree-\(f\) unramified base change of a spherical representation with Satake parameters \(\alpha_1,\ldots,\alpha_n\).

**Solution.** Since \(\Phi_E=\Phi_F^f\) modulo inertia and inertia is trivial, diagonalizing \(\rho(\Phi_F)\) gives diagonal entries \(\alpha_i^f\) on restriction. The new residue cardinality is \(q^f\), so the factor is \(\prod_i(1-\alpha_i^f q^{-fs})^{-1}\). The determinant becomes \((\prod_i\alpha_i)^f\). These are precisely the spherical Satake data through base-change compatibility.

**Exercise 8.2 (medium).** Compute the factor of induction of an unramified character from degree-\(n\) unramified \(E/F\).

**Solution.** Write \(a=\theta(\varpi_E)\). The coset basis in (5.2) has Frobenius matrix \(A\), with a single cyclic wraparound entry \(a\). A cyclic vector has minimal polynomial \(T^n-a\), equal to the characteristic polynomial by dimension. Inertia is trivial. Its distinct eigenvalues are \(\zeta a^{1/n}\), so the determinant formula gives the product in (5.1), and multiplying the factors gives \((1-aq^{-ns})^{-1}\). The choice of the root only orders these eigenvalues. The induced parameter has zero monodromy and is a sum of unramified characters.

**Exercise 8.3 (medium).** Check the exterior-square conductor formula for every two-dimensional parameter, including nonzero monodromy.

**Solution.** For a basis \(e_1,e_2\), write \(Ne_1=a e_1+c e_2\), \(Ne_2=b e_1+d e_2\). Its action on \(e_1\wedge e_2\) is \((a+d)e_1\wedge e_2\). Nilpotence gives \(a+d=0\). The Weil action on that line is \(\det r\), proving (7.2). A one-dimensional parameter with zero monodromy has its usual character conductor, so (7.3) follows from determinant–central-character compatibility. For \(r=\widehat\chi S_2\), its determinant is \(\widehat\chi^2\), and the answer is \(a(\chi^2)\); for a principal sum it is \(a(\chi_1\chi_2)\); for an irreducible Weil parameter it is likewise the character conductor of its determinant. Thus the same formula covers every rank-two type.

**Exercise 8.4 (hard).** Verify the Steinberg formal-degree formula, retaining Haar normalization.

**Solution.** With \(\mu_0(\overline K)=1\), each Iwahori double coset of length \(r\) has volume \(q^r/(q+1)\), and the invariant-line unit coefficient has squared absolute value \(q^{-2r}\). The length counts give integral \((2+4/(q-1))/(q+1)=2/(q-1)\). Schur orthogonality therefore gives \((q-1)/2\). The adjoint parameter is \(S_3\); its kernel of \(N\) has Frobenius \(q^{-1}\), giving \(L(s)=(1-q^{-s-1})^{-1}\), and its quotient by that kernel has determinant contribution \(q^{1-2s}\). Consequently \(\gamma(0)=q^2/(q+1)\). Changing to \(\mu_\psi=(1-q^{-2})\mu_0\) divides the formal degree by \(1-q^{-2}\), giving \(q^2/[2(q+1)]\), exactly \(\gamma(0)/2\). Any further scalar change of measure divides the degree by that same scalar.

## What this lesson does not prove

Henniart's global existence proof is outlined in [Carayol 2000, §4], with the author's precise variant and mechanism in [Henniart 2001, §§1–5]. The LRS positive-characteristic theorem is [Theorem 15.7 and Remark 15.8] of their paper; its geometric and trace-formula construction is stated. The Scholze trace characterization and bijectivity are [Theorems 1.1–1.2; §§12–14], with the half norm converted explicitly in (2.2). The Fargues–Scholze semisimple parameter, spectral action and categorical conjecture are respectively [Theorem I.9.6, Theorem I.10.1 and Conjecture I.10.2] of their manuscript.

Cyclic base change and induction on semisimple Weil classes are the stated inputs [Henniart 2001, §§7.2–7.3]. The full-parameter formulation uses their extension through the earlier segment classification as described after (3.2). Proposition 4.1 and Proposition 5.1 prove their unramified parameter calculations. The standard factor conductor equality follows from the earlier pair-factor theorem.

The general formal-degree theorem is [Hiraga–Ichino–Ikeda 2008, Theorem 3.1], with the exact gauge-normalized general-linear formulation in [Ichino–Lapid–Mao, Theorem 2.1]. Schur orthogonality is the defining harmonic-analysis input. The earlier representation-classification lesson proves the Steinberg double-coset coefficient calculation used here. We proved its numerical degree and adjoint-factor comparison. The depth-zero type construction and finite-field type dimension in (6.7) are the stated earlier dihedral and finite-group inputs; we proved its compact-induction degree calculation and adjoint-factor check.

The exterior- and symmetric-square matching theorem is [Cogdell–Shahidi–Tsai 2017, Theorem 1.1]. The rank-two exterior-square parameter and conductor calculation are proved here. None of the geometric statements is a claim that the general reductive-group packet conjecture has thereby been proved.

## References

- [Carayol 2000] Henri Carayol, [“Preuve de la conjecture de Langlands locale pour GL_n : travaux de Harris–Taylor et Henniart”](https://www.numdam.org/item/SB_1998-1999__41__191_0/), Séminaire Bourbaki, exposé 857 (1998–1999), *Astérisque* 266 (2000), 191–243, §4.
- [Henniart 2001] Guy Henniart, [“Sur la conjecture de Langlands locale pour GL_n”](https://www.numdam.org/item/JTNB_2001__13_1_167_0/), *Journal de Théorie des Nombres de Bordeaux* 13 (2001), 167–187, especially §§2–5 and §7.
- [Laumon–Rapoport–Stuhler 1993] Gérard Laumon, Michael Rapoport and Ulrich Stuhler, [*D-elliptic sheaves and the Langlands correspondence*](https://www.math.uni-bonn.de/people/rapoport/myalggeom/preprints/Dellipticsheaves.pdf), *Inventiones mathematicae* 113 (1993), 217–338, Introduction, Theorem 15.7 and Remark 15.8.
- [Scholze] Peter Scholze, [*The Local Langlands Correspondence for GL_n over p-adic Fields*](https://arxiv.org/abs/1010.1540), Introduction, Theorems 1.1–1.2, and §§12–14.
- [Fargues–Scholze] Laurent Fargues and Peter Scholze, [*Geometrization of the local Langlands correspondence*](https://arxiv.org/abs/2102.13459), Introduction, §§I.9–I.10.
- [Hiraga–Ichino–Ikeda 2008] Kaoru Hiraga, Atsushi Ichino and Tamotsu Ikeda, [*Formal degrees and adjoint gamma-factors*](https://www.ams.org/journals/jams/2008-21-01/S0894-0347-07-00567-X/S0894-0347-07-00567-X.pdf), *Journal of the American Mathematical Society* 21 (2008), 283–304, Theorem 3.1.
- [Ichino–Lapid–Mao] Atsushi Ichino, Erez Lapid and Zhengyu Mao, [*On the formal degrees of square-integrable representations of odd special orthogonal and metaplectic groups*](https://arxiv.org/abs/1404.2909), Notation and §2, Theorem 2.1, the general-linear-group case.
- [Cogdell–Shahidi–Tsai 2017] James W. Cogdell, Freydoon Shahidi and Tien-Chi Tsai, [*Local Langlands correspondence for GL_n and the exterior and symmetric square epsilon-factors*](https://arxiv.org/abs/1412.1448), *Duke Mathematical Journal* 166 (2017), §1, Theorem 1.1.
- [Getz–Hahn 2022] Jayce R. Getz and Heekyoung Hahn, [*An Introduction to Automorphic Representations, with a View toward Trace Formulae*](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), draft of 22 April 2022, §§12.5 and 13.5.
