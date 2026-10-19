# Artin L-functions, conductors and discriminants

*Written by OpenAI GPT-6.1 Sol in Codex, Ultra effort, October 2026. Self-checked by the writing AI; no independent review is claimed. Public domain (CC0).*

**Lesson 21.** A finite Galois representation packages Frobenius operators into an Euler product. Its ramification determines a conductor, and permutation representations recover discriminants. We prove the formal identities at ramified as well as unramified primes, prove conductor integrality in every dimension, and obtain the analytic continuation and functional equation by integer Brauer induction. The splitting field of \(X^3-2\) provides a concrete nonabelian example. The last section distinguishes global orthogonal root numbers from Deligne's local formula.

Our representation-theoretic inputs are written in [Characters and the orthogonality relations](https://kokunoyumeto.github.io/open-math-courses-public/courses/RT-FIN/characters-and-the-orthogonality-relations.html#theorem-3-2), Theorem 3.2; [Induced representations and Frobenius reciprocity](https://kokunoyumeto.github.io/open-math-courses-public/courses/RT-FIN/induced-representations-and-frobenius-reciprocity.html#1-one-copy-for-each-coset), §§1–4; and [Brauer's induction theorem](https://kokunoyumeto.github.io/open-math-courses-public/courses/RT-FIN/brauers-induction-theorem.html#theorem-5-1), Theorem 5.1. In particular, Brauer's theorem expresses every character as an **integer** linear combination of characters induced from one-dimensional characters of subgroups. The induction model and regular multiplicities are used below; their representation-theoretic proofs stay in those lessons.

For ramification we use Hilbert's different formula and Herbrand's quotient theorem, with the conventions of [Abelian ramification, conductors and Hasse–Arf](abelian-ramification-conductors-and-hasse-arf.md). [Ray class fields, conductors and ideal reciprocity](ray-class-fields-conductors-and-ideal-reciprocity.md) identifies rank-one Galois and idèle characters. The written number-field analytic input is Theorem 10.1 of [Hecke L-functions and the Dedekind zeta function](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-CFT/proof-dependencies.html#NT-ADL-10). Section 6 also supplies the function-field analytic argument from the adelic duality proved in lessons 15 and 17 and the local Fourier calculations of lesson 12.


**Prerequisite proof availability.** The named results below identify specific programme lessons. The [prerequisite record](https://kokunoyumeto.github.io/open-math-courses-public/courses/NT-CFT/proof-dependencies.html#lesson-21) shows which results are proved in published lessons and which full proofs are still missing. A record or external reference is not a supplied proof; arguments using an unavailable prerequisite retain that dependency.

## 1. Euler factors and induction

Let \(L/K\) be a finite Galois extension of global fields, \(G=\operatorname{Gal}(L/K)\), and let \(V\) be a finite-dimensional complex representation of \(G\). At a finite place \(v\) of \(K\), choose a place \(w\) of \(L\), decomposition group \(D_w\), and inertia group \(I_w\). Put \(q_v=|\kappa(v)|\). An arithmetic Frobenius \(\phi_w\in D_w/I_w\) acts on the residue field by \(x\mapsto x^{q_v}\). It acts unambiguously on \(V^{I_w}\), even though its lift to \(D_w\) is not unique. Define
\[
L_v(s,V)=\det(1-q_v^{-s}\phi_w\mid V^{I_w})^{-1},
\qquad L_K(s,V)=\prod_{v\text{ finite}}L_v(s,V).
\tag{1}
\]
Changing \(w\) conjugates the relevant groups and operator, so does not change the determinant. Eigenvalues have absolute value one, since \(G\) is finite. The logarithmic expansion is
\[
\log L_K(s,V)=\sum_v\sum_{m\geq1}
\frac{\operatorname{tr}(\phi_w^m\mid V^{I_w})}{m q_v^{ms}}.
\tag{2}
\]
Its absolute value is bounded termwise by \(\dim V\) times the logarithmic series for \(\zeta_K(\operatorname{Re}s)\). The latter converges for \(\operatorname{Re}s>1\). Thus (1) converges absolutely there, locally uniformly, and has no zeros there. For a virtual representation, take quotients of these products.

**Proposition 21.1.** Artin L-functions satisfy
\[
\begin{aligned}
L_K(s,V\oplus W)&=L_K(s,V)L_K(s,W),\\
L_K(s,\operatorname{Ind}_H^G W)&=L_E(s,W),\quad E=L^H,\\
L_K(s,\operatorname{Inf}_{G/N}^G U)&=L_K(s,U),\quad N\triangleleft G.
\end{aligned}
\tag{3}
\]
The last function on the right is computed in \(L^N/K\). Also
\[
\zeta_E(s)=L_K(s,\mathbf C[G/H]),\qquad
\zeta_L(s)=\prod_{\rho\in\operatorname{Irr}(G)}L_K(s,\rho)^{\dim\rho}.
\tag{4}
\]

**Proof.** Direct sums give block-diagonal determinants. Under passage to a quotient, decomposition and inertia map onto their counterparts, and Frobenius maps to Frobenius. The invariant space and its operator are consequently unchanged, proving inflation invariance.

We prove induction place by place. Restrict \(\mathbf C[G]\otimes_{\mathbf C[H]}W\) to \(D=D_w\). Splitting its coset basis into \(D\)-orbits gives
\[
\operatorname{Res}_D\operatorname{Ind}_H^G W
\simeq\bigoplus_{g\in D\backslash G/H}
\operatorname{Ind}_{J_g}^{D}W_g,
\quad J_g=D\cap gHg^{-1}.
\tag{5}
\]
Here \(W_g\) is the conjugate representation on the same vector space. The double cosets correspond to the places \(u\mid v\) of \(E\), and \(J_g\) is the local Galois group over \(E_u\).

Let \(I=I_w\). For one summand of (5), its \(I\)-invariants have one copy of \(W_g^{I\cap J_g}\) for each \(I\)-orbit in \(D/J_g\). This follows directly in the coset model: an invariant vector on an orbit is determined by its value at a representative, and that value must be fixed by its stabilizer. Because \(D/I\) is cyclic, Frobenius permutes these orbits cyclically, in
\(f=[D:IJ_g]=[\kappa(u):\kappa(v)]\) slots. After one circuit its action on the initial copy is arithmetic Frobenius of \(E_u\): \(\phi_w^f\) can be adjusted by an element of \(I\) to lie in \(J_g\), and that adjustment does not affect the invariant vectors.

For a cyclic block operator with wrap-around operator \(A\),
\[
\det(1-T\Phi)=\det(1-T^f A).
\tag{6}
\]
To see this, successively change bases in the slots so that all transition maps except the last are identities. Eliminating the first \(f-1\) variables from \((1-T\Phi)x\) leaves the last block \(1-T^f A\); the other diagonal blocks are identities. This is a polynomial identity, so the computation over \(\mathbf C(T)\) proves it for every \(T\). Since \(q_u=q_v^f\), (6) proves that this summand contributes exactly \(L_u(s,W)\). Taking all summands proves the middle identity of (3), including ramified places.

The trivial representation has Euler factor \((1-q_v^{-s})^{-1}\), hence L-function \(\zeta_K\). Apply induction to \(W=\mathbf1\) to obtain the first identity of (4). For \(H=1\), the permutation representation is the regular representation. The written regular-multiplicity theorem decomposes it as \(\bigoplus_\rho\rho^{\oplus\dim\rho}\). Additivity gives the second identity. \(\square\)

## 2. Rank one and primitive Hecke characters

Write \(\operatorname{rec}_{\mathrm{arith}}:C_K\to G^{\mathrm{ab}}\) for arithmetic global reciprocity. For a one-dimensional character \(\chi:G\to\mathbf C^\times\), define
\[
\omega=\chi\circ\operatorname{rec}_{\mathrm{arith}}.
\tag{7}
\]
It is a finite-order Hecke character. Its finite conductor is the least ideal whose local principal unit groups it kills; real sign conditions are recorded separately in its infinite type.

**Theorem 21.2.** With the primitive Euler product, \(L_K(s,\chi)=L_K(s,\omega)\).

**Proof.** Local compatibility sends units onto inertia. If \(\chi\) is nontrivial on inertia at \(v\), its invariant space is zero, so the Artin factor is 1. The local Hecke character is ramified and its primitive factor is also 1. If \(\chi\) is trivial on inertia, then
\(\omega_v(\pi_v)=\chi(\phi_w)\), and both factors are
\((1-\omega_v(\pi_v)q_v^{-s})^{-1}\). This proves equality in the convergence region, hence wherever continuation is defined. One may equivalently replace \(L\) by the abelian field fixed by \(\ker\chi\); inflation invariance proves that this replacement changes no factor. \(\square\)

A prime ramified in \(L\) can be unramified for \(\chi\). Its factor must then be retained. Omitting every prime dividing the conductor of the ambient extension produces an imprimitive Hecke function, generally different from (1). The relevant modulus is the character's conductor.

Deligne's Euler factors use geometric Frobenius. On a finite-image representation they give our arithmetic factors for \(V^\vee\). In rank one the corresponding reciprocity map is geometric as well. These two changes must be made together. For self-dual representations the L-functions themselves coincide in either Frobenius convention.

## 3. The local conductor and its integrality

Let \(T/F\) be a finite Galois extension of nonarchimedean local fields, with group \(G\), residue degree \(f\), and lower ramification groups \(G_j\). For \(\sigma\ne1\), let \(i_G(\sigma)\) be its motion number as in lesson 10; it is zero off inertia. Define the class function
\[
a_G(\sigma)=-f i_G(\sigma)\quad(\sigma\ne1),\qquad
a_G(1)=f\sum_{\sigma\ne1}i_G(\sigma).
\tag{8}
\]
For a representation \(V\), its conductor exponent is
\[
a_F(V)=\langle a_G,\chi_V\rangle_G
=\sum_{j\geq0}\frac{|G_j|}{|G_0|}
       \operatorname{codim}V^{G_j}.
\tag{9}
\]
Indeed \(i_G(\sigma)\) counts the indices \(j\geq0\) for which \(\sigma\in G_j\). Insert this count into the character inner product and use
\(|G_j|^{-1}\sum_{\sigma\in G_j}\overline{\chi_V(\sigma)}=\dim V^{G_j}\) and \(|G|=f|G_0|\). The expression in (9) is nonnegative rational; its integrality requires proof.

With the ceiling convention of lesson 10, change variables by Herbrand's function to obtain
\[
a_F(V)=\operatorname{codim}V^{G^0}
       +\int_0^\infty\operatorname{codim}V^{G^u}\,du.
\tag{10}
\]
Herbrand's quotient theorem shows that (10), hence (9), is unchanged if the representation is realized in a larger finite Galois extension. It therefore defines the exponent intrinsically for any finite-image local representation. It is additive on direct sums, and extends additively to virtual representations.

**Proposition 21.4.** For a one-dimensional \(\chi\), \(a_F(\chi)\) is the least integer \(a\geq0\) for which its multiplicative character under reciprocity kills \(U_F^{(a)}\), where \(U_F^{(0)}=\mathcal O_F^\times\). In particular it is an integer.

**Proof.** Pass to the abelian quotient through which \(\chi\) factors, using (10). Lesson 10 identifies its upper groups with the images of \(U_F^{(\lceil u\rceil)}\) for \(u>0\) and with the units at \(u=0\). If the character is unramified, every codimension in (10) is zero. Otherwise its least unit level is some integer \(a\geq1\), and its invariant space is zero at \(u=0\) and for \(0<u\leq a-1\), and is all of its line for \(u>a-1\). Endpoints have no effect on the integral. Formula (10) gives \(1+(a-1)=a\), also for tame characters with \(a=1\). The integer filtration theorem used here is the proved Hasse–Arf theorem of lesson 10. \(\square\)

To pass to higher dimension, we need the different in a tower. Here and below \(\mathfrak D\) is the different and \(\mathfrak d\) the discriminant ideal.

**Different in a tower.** For finite separable local extensions \(T/E/F\),
\[
\mathfrak D_{T/F}=\mathfrak D_{T/E}\mathfrak D_{E/F}\mathcal O_T,
\quad \delta_{T/F}=\delta_{T/E}+e(T/E)\delta_{E/F}.
\tag{11}
\]
For completeness, identify the inverse different with the trace-dual lattice:
\(\mathfrak D_{E/F}^{-1}=\{x:\operatorname{Tr}_{E/F}(x\mathcal O_E)\subseteq\mathcal O_F\}\).
There is an adjunction
\[
\operatorname{Hom}_{\mathcal O_F}(\mathcal O_T,\mathcal O_F)
\simeq
\operatorname{Hom}_{\mathcal O_E}
\bigl(\mathcal O_T,\operatorname{Hom}_{\mathcal O_F}(\mathcal O_E,\mathcal O_F)\bigr),
\tag{12}
\]
sending \(\ell\) to the map \(z\mapsto(b\mapsto\ell(bz))\); its inverse evaluates at \(b=1\). Under trace identifications the middle lattice is \(\mathfrak D_{E/F}^{-1}\). It is a principal fractional \(\mathcal O_E\)-ideal, so it factors out of the final Hom in (12). Trace transitivity then identifies the left lattice with
\(\mathfrak D_{T/E}^{-1}\mathfrak D_{E/F}^{-1}\mathcal O_T\).
Inverting and taking valuations proves (11). All trace identifications are isomorphisms because the extensions are separable.

**Induction formula.** If \(E=T^H\), with \(H\leq G\), and \(W\) is a representation of \(H\), then
\[
a_F(\operatorname{Ind}_H^G W)
=(\dim W)v_F(\mathfrak d_{E/F})+f(E/F)a_E(W).
\tag{13}
\]
This does not require \(H\) to be normal.

**Proof.** The lower groups of \(T/E\) are \(H_j=H\cap G_j\), since their definition uses \(v_T\) and \(\mathcal O_T\) in both cases. Since \(G_j\) is normal in \(G\), its orbits on \(G/H\) all have size \(|G_j|/|H_j|\). An invariant vector on each orbit is determined by a vector fixed by \(H_j\). Thus
\[
\dim(\operatorname{Ind}W)^{G_j}=[G:G_jH]\dim W^{H_j}.
\tag{14}
\]
Separating the missing orbit dimensions from the missing dimensions within each orbit in (9) gives
\[
a_F(\operatorname{Ind}W)
=(\dim W)a_F(\operatorname{Ind}\mathbf1)
 +f(E/F)a_E(W),
\tag{15}
\]
because
\(\frac{|G_j|}{|G_0|}[G:G_jH]
=f(E/F)\frac{|H_j|}{|H_0|}\).
Here \(f(E/F)=|G||H_0|/(|G_0||H|)\).

For the permutation term, direct substitution in (9) yields
\[
a_F(\operatorname{Ind}\mathbf1)
=\frac{f(E/F)}{|H_0|}\sum_{j\geq0}(|G_j|-|H_j|).
\tag{16}
\]
Hilbert's different formula identifies the sum with \(\delta_{T/F}-\delta_{T/E}\). By (11) this is \(|H_0|\delta_{E/F}\). Finally the local trace-dual discriminant formula, proved in lesson 10, is
\(v_F(\mathfrak d_{E/F})=f(E/F)\delta_{E/F}\).
This proves (13). \(\square\)

**Artin integrality in every dimension.** Apply the written integer Brauer induction theorem to \(\chi_V\):
\[
\chi_V=\sum_i n_i\operatorname{Ind}_{H_i}^G\chi_i,
\qquad n_i\in\mathbf Z,\quad\dim\chi_i=1.
\tag{17}
\]
The conductor is a linear functional on characters. Each induced term has integral conductor by (13) and Proposition 21.4. Hence \(a_F(V)\in\mathbf Z\); (9) makes it nonnegative for an actual representation. This proves integrality without assuming it in the definition. Moreover (8) is itself a character: its multiplicity on each irreducible is the nonnegative integer just proved, and irreducible characters form an orthonormal basis of class functions.

## 4. Global conductors and the discriminant formula

At each finite place use the restricted local representation, and set
\[
\mathfrak f_K(V)=\prod_v\mathfrak p_v^{a_{K_v}(V)}.
\tag{18}
\]
Only finitely many exponents are nonzero. This is an integral ideal for an actual representation; for virtual representations it is a fractional ideal. Infinite signs contribute to the gamma factors below rather than to (18).

For a finite separable global \(E/K\), Mackey's decomposition (5) and (13) give
\[
\mathfrak f_K(\operatorname{Ind}_{E}^{K}W)
=\mathfrak d_{E/K}^{\dim W}\,N_{E/K}\mathfrak f_E(W).
\tag{19}
\]
Indeed, at \(v\) sum (13) over \(u\mid v\). The second term is precisely the valuation of the ideal norm. The first is the valuation of the global discriminant: completion decomposes the integral lattice into the local integer rings, its trace pairing is block diagonal, and determinant valuations add. This localization argument was also given explicitly in lesson 20. No normality assumption on \(E/K\) is needed in (19).

**Theorem 21.5 (conductor–discriminant).** For finite Galois \(L/K\),
\[
\mathfrak d_{L/K}
=\prod_{\rho\in\operatorname{Irr}(G)}\mathfrak f_K(\rho)^{\dim\rho}.
\tag{20}
\]
More generally \(\mathfrak f_K(\mathbf C[G/H])=\mathfrak d_{L^H/K}\).

**Proof.** Set \(W=\mathbf1\) in (19). Its conductor over \(E\) is the unit ideal, proving the permutation assertion. For \(H=1\), use the regular decomposition in Proposition 21.1 and additivity of every local exponent. This proves (20) as an equality of ideals. Alternatively (16) with \(H=1\) gives the exponent \(f(L_w/K_v)\delta_{L_w/K_v}\) for one local regular representation, and the global restriction has one such copy for every place above \(v\). This is exactly the completed global trace discriminant. \(\square\)

## 5. Meromorphy and the functional equation over number fields

Suppose first that \(K\) is a number field, of absolute discriminant \(d_K\). Put
\[
Q_K(V)=|d_K|^{\dim V}N_{K/\mathbf Q}\mathfrak f_K(V),\quad
\Gamma_{\mathbf R}(s)=\pi^{-s/2}\Gamma(s/2),\quad
\Gamma_{\mathbf C}(s)=2(2\pi)^{-s}\Gamma(s).
\tag{21}
\]
At a real place, let \(d_v^+,d_v^-\) be the multiplicities of \(+1,-1\) for complex conjugation. At a complex place there is one gamma factor of complex type per dimension. Define
\[
\Gamma_K(s,V)=
\prod_{v\text{ real}}\Gamma_{\mathbf R}(s)^{d_v^+}
                         \Gamma_{\mathbf R}(s+1)^{d_v^-}
\prod_{v\text{ complex}}\Gamma_{\mathbf C}(s)^{\dim V},
\quad
\Lambda_K(s,V)=Q_K(V)^{s/2}\Gamma_K(s,V)L_K(s,V).
\tag{22}
\]
For virtual representations, dimensions and multiplicities in these formulas are signed integers and \(Q_K(V)\) is a positive real number.

Both completion factors respect induction. For \(Q\), use (19) and
\[
|d_E|=|d_K|^{[E:K]}N_{K/\mathbf Q}\mathfrak d_{E/K},
\quad Q_K(\operatorname{Ind}_E^K W)=Q_E(W).
\tag{23}
\]
The discriminant tower identity follows by taking norms of (11) at every finite place, or by trace adjunction for the corresponding global lattices. For the gamma factor, a real place of \(E\) over a real place of \(K\) retains its sign type, whereas a complex place over a real place contributes one \(+1\) and one \(-1\) per dimension. The gamma duplication identity gives
\(\Gamma_{\mathbf R}(s)\Gamma_{\mathbf R}(s+1)=\Gamma_{\mathbf C}(s)\).
At a complex place induction simply adds the dimensions for the places above it. Therefore
\[
\Lambda_K(s,\operatorname{Ind}_E^K W)=\Lambda_E(s,W).
\tag{24}
\]

**Theorem 21.3.** Every finite-image Artin L-function is meromorphic on \(\mathbf C\). With the above completion it satisfies
\[
\Lambda_K(s,V)=W_K(V)\Lambda_K(1-s,V^\vee),
\qquad |W_K(V)|=1.
\tag{25}
\]
The function-field version is proved in section 6.

**Proof over number fields.** Use (17) for the global Galois group, and put \(E_i=L^{H_i}\). Propositions 21.1 and Theorem 21.2 imply, initially in \(\operatorname{Re}s>1\),
\[
L_K(s,V)=\prod_i L_{E_i}(s,\omega_i)^{n_i},
\quad
\Lambda_K(s,V)=\prod_i\Lambda_{E_i}(s,\omega_i)^{n_i},
\tag{26}
\]
where \(\omega_i=\chi_i\circ\operatorname{rec}_{\mathrm{arith}}\). The second equality uses (24) and additivity of conductors, dimensions and gamma multiplicities. Theorem 10.1 of the written Hecke lesson proves continuation and the completed functional equation for each finite-order \(\omega_i\), with unit absolute-value root number. Integer powers in (26) give meromorphic functions, including when some \(n_i\) are negative. Taking their functional equations gives (25), with
\(W_K(V)=\prod_i W_{E_i}(\omega_i)^{n_i}\).
The dual of an induced representation is induced from the dual, as follows by dualizing its finite coset model, so the function on the right is the required \(V^\vee\).

The resulting function agrees with (1) on its convergence half-plane, hence is independent of the Brauer expression by analytic uniqueness. The constant is independent as well: on a nonempty open set where both completed functions are finite and nonzero it is their ratio in (25). Thus two expressions give the same constant. \(\square\)

Negative powers explain why this argument proves meromorphy rather than holomorphy. **Artin's conjecture** for number fields asserts that the L-function of every nontrivial irreducible finite-image representation is entire. It is proved in dimension one by the Hecke theorem; (26) does not prove it in general. The trivial representation has the zeta pole and is deliberately excluded. Nothing here asserts the conjecture for all solvable Galois groups.

## 6. The analytic argument over function fields

Let \(K\) now be a global function field. We give the analytic input needed for the same Brauer argument, rather than applying a number-field theorem to it. Lessons 15 and 17 proved that \(\mathbb A_K/K\) is compact and that there is a continuous additive character \(\psi\), trivial on \(K\), for which the pairing \(\psi(xy)\) identifies the adèles with their dual and has exact annihilator \(K\). Use the product of the local self-dual measures of lesson 12 and the positive Fourier kernel. Schwartz functions here are locally constant with compact support.

First the additive covolume of \(K\) is 1. Here is a finite counting proof, also fixing the normalization in Poisson summation. Choose a compact open additive subgroup \(U\) with \(U\cap K=0\), and put \(V=U^\perp\). The finite quotient \(\mathbb A_K/(K+U)\) has dual \(K\cap V\), by the exact annihilator assertion; write their common order as \(N\). The map from \(U\) into the compact quotient \(\mathbb A_K/K\) is injective and its image has index \(N\), so the covolume is \(N\operatorname{vol}(U)\). Also \(K+V=\mathbb A_K\): this open subgroup is closed and its quotient has annihilator \(K\cap U=0\), so that quotient is trivial, since characters separate a compact abelian quotient. Consequently the covolume is \(\operatorname{vol}(V)/N\). Local Fourier inversion gives \(\operatorname{vol}(U)\operatorname{vol}(V)=1\). The two covolume formulas therefore give covolume squared 1, and positivity gives 1. The finite duality used here is the character duality already proved for the relevant adelic compact quotients in lesson 15.

Periodize a Schwartz function on \(\mathbb A_K/K\). The periodization is locally constant, so factors through a finite quotient of this compact group. Its Fourier coefficients, indexed by the annihilator \(K\), are \(\widehat f(\alpha)\), since the covolume is 1; unfolding the integral proves this assertion directly. Finite Fourier inversion at zero gives
\[
\sum_{\alpha\in K}f(\alpha x)
=|x|^{-1}\sum_{\alpha\in K}\widehat f(\alpha/x),\qquad x\in\mathbb A_K^\times.
\tag{27}
\]
The scaling factor follows by the substitution \(z\mapsto zx\) in additive measure. Each sum is finite on compact sets of idèles. This follows from discreteness of \(K\) and compactness of the supports.

The content image is a nontrivial discrete cyclic subgroup of \(\mathbf R_{>0}\), say \(R^{\mathbf Z}\) with \(R>1\). Choose an idèle class \(c\) with \(|c|=R\). No assertion that a degree-one place exists is required. The norm-one group \(C_K^1\) is compact, as proved in lesson 14. Fix its quotient Haar measure, of volume \(\kappa\), so that each norm level is a translate with that same measure. Let \(\omega\) be a finite-order Hecke character and put
\[
\Theta_f(x)=\sum_{\alpha\in K^\times}f(\alpha x),\qquad
Z(f,\omega,s)=\int_{C_K}\Theta_f(x)\omega(x)|x|^s\,d^\times x.
\tag{28}
\]
For \(\operatorname{Re}s>1\), this converges and unfolds to the usual idèle zeta integral. To check convergence directly, (27) bounds \(\Theta_f\) on negative norm levels by \(C(|x|^{-1}+1)\): the inverted classes have positive norm, where the Fourier theta sum vanishes beyond a fixed bound, and the remaining finitely many levels are compact. Summing the resulting geometric bound gives convergence for \(\operatorname{Re}s>1\).

Write \(P_{\geq}(f,\omega,s)\) and \(P_>(f,\omega,s)\) for the portions of (28) with norm at least 1 and strictly greater than 1. Both are finite Laurent polynomials in \(R^{-s}\). Indeed a compact additive support bounds the module of every idèle lying in it: outside a finite set its components are integral, and inside that set their absolute values are bounded. Since \(|\alpha|=1\) for \(\alpha\in K^\times\), the condition \(\alpha x\in\operatorname{supp}f\) bounds \(|x|\). Thus only finitely many positive levels occur; their integrals are finite by compactness of \(C_K^1\).

Apply (27) to the negative levels in (28), removing the zero summands and substituting \(y=x^{-1}\). It gives
\[
Z(f,\omega,s)=P_{\geq}(f,\omega,s)
 +P_>(\widehat f,\omega^{-1},1-s)+C(f,\omega,s).
\tag{29}
\]
If \(\omega\) is nontrivial on \(C_K^1\), the correction \(C\) is zero by character orthogonality. Otherwise set \(\lambda=\omega(c)\). Summing the negative-level zero terms gives exactly
\[
C(f,\omega,s)=\kappa\left(
\widehat f(0)\frac{\lambda^{-1}R^{1-s}}{1-\lambda^{-1}R^{1-s}}
-f(0)\frac{\lambda^{-1}R^{-s}}{1-\lambda^{-1}R^{-s}}
\right).
\tag{30}
\]
This was derived in the convergence region by geometric series and is now a rational continuation in \(R^{-s}\).

The continued integral satisfies
\[
Z(f,\omega,s)=Z(\widehat f,\omega^{-1},1-s).
\tag{31}
\]
Here is the check at norm zero, which avoids any overlap assumption on convergence regions. The two strictly positive polynomial parts in (29) exchange. The norm-one terms satisfy, by (27),
\[
P_0(f,\omega,s)-P_0(\widehat f,\omega^{-1},1-s)
=\begin{cases}\kappa(\widehat f(0)-f(0)),&\omega|_{C_K^1}=1,\\0,&\text{otherwise}.
\end{cases}
\tag{32}
\]
When applying Poisson to the inverted norm-one class, use that inversion preserves Haar measure and that \(\Theta_{\widehat{\widehat f}}=\Theta_f\), since \(\widehat{\widehat f}(z)=f(-z)\) and \(-1\in K^\times\). If \(\omega\) is trivial on \(C_K^1\), write \(A=\lambda^{-1}R^{1-s}\) and \(B=\lambda^{-1}R^{-s}\). The corresponding variables in the dual correction are \(1/B,1/A\). The identity
\(z/(1-z)+(1/z)/(1-1/z)=-1\)
shows that the difference of the two corrections is \(-\kappa(\widehat f(0)-f(0))\), canceling (32). If \(\omega\) is nontrivial there, both corrections and the difference in (32) vanish. This proves (31) as a rational identity.

To extract the L-function, take at every unramified place \(f_v=\mathbf1_{\mathcal O_v}\), and at each ramified place
\(f_v=\omega_v|_{\mathcal O_v^\times}^{-1}\mathbf1_{\mathcal O_v^\times}\).
These form a restricted tensor product Schwartz function. With multiplicative unit volume 1 its local zeta integrals are respectively the primitive Euler factor and 1. Absolute factorization in \(\operatorname{Re}s>1\) therefore gives \(Z(f,\omega,s)=L_K(s,\omega)\).

Let \(n_v\) be the local additive conductor in the convention that \(\psi_v\) is trivial on \(\mathfrak p_v^{-n_v}\), and set
\[
D_K(\psi)=\prod_vq_v^{n_v},\qquad
Q_K(V)=D_K(\psi)^{\dim V}N\mathfrak f_K(V),\qquad
\Lambda_K(s,V)=Q_K(V)^{s/2}L_K(s,V).
\tag{33}
\]
Only finitely many \(n_v\) are nonzero. The actual finite Fourier calculation of lesson 12, equations (13)–(17), gives
\[
\epsilon_v(s,\omega_v)=W_v(\omega_v)q_v^{(a_v+n_v)(1/2-s)},
\qquad |W_v(\omega_v)|=1.
\tag{34}
\]
This holds in positive characteristic too. Factor the dual integral in its own convergence region, use the local equations, and then use the rational continuations (29). Equations (31) and (34) imply
\(L_K(s,\omega)=W_K(\omega)Q_K(\omega)^{1/2-s}L_K(1-s,\omega^{-1})\),
where \(W_K(\omega)=\prod_v W_v(\omega_v)\). Hence (25) holds in rank one, with no infinite gamma factors. In particular the trivial character has \(W_K(\mathbf1)=1\), since its local central constants in (34) are all 1.

For \(E/K\), use \(\psi_E=\psi\circ\operatorname{Tr}_{E/K}\). The trace-dual formula (12) gives
\(n_u=e(E_u/K_v)n_v+\delta_{E_u/K_v}\).
Multiplying the corresponding powers of residue cardinalities gives
\[
D_E(\psi_E)=D_K(\psi)^{[E:K]}N\mathfrak d_{E/K}.
\tag{35}
\]
Thus (19) makes \(Q\) respect induction here as well. The Brauer proof (26) now proves meromorphy and (25) for every finite-image representation over a function field. It also proves rationality in \(q^{-s}\), where \(q\) is the cardinality of the full constant field: every \(R\) and every residue norm is an integral power of \(q\), and the same is true for the constant fields of the finite extensions used in (26). The completed function may include the elementary exponential factor \(Q^{s/2}\); the uncompleted L-function is rational in \(q^{-s}\).

The scale \(D_K(\psi)\) is independent of multiplying the global character by a principal nonzero scalar: the local conductor changes multiply it by the inverse global module of that scalar, which is 1. Formula (33) suffices here without invoking a separate theorem about degrees of canonical divisors.

## 7. The cubic field and its two-dimensional representation

Put \(\alpha=\sqrt[3]2\), \(E=\mathbf Q(\alpha)\), and \(L=\mathbf Q(\alpha,\zeta_3)\). The polynomial is irreducible by Eisenstein at 2. Its discriminant is \(-108\), computed as \((-1)^3N_{E/\mathbf Q}(3\alpha^2)\). Since this is not a square, the transitive cubic Galois group is \(S_3\). Its quadratic subfield is \(\mathbf Q(\sqrt{-3})\).

The polynomial order is already maximal. At 2 the polynomial is Eisenstein, so \(\alpha\) is a local uniformizer and \(\mathcal O_{E_2}=\mathbf Z_2[\alpha]\). At 3, \(\beta=\alpha+1\) satisfies
\[
\beta^3-3\beta^2+3\beta-3=0,
\tag{36}
\]
an Eisenstein equation, so \(\mathcal O_{E_3}=\mathbf Z_3[\beta]=\mathbf Z_3[\alpha]\). The local integer-ring assertion for an Eisenstein generator follows by expanding an integer in powers of the uniformizer with residue representatives from the base field, then reducing by its monic equation; the resulting degree-less-than-three coefficients converge in \(\mathbf Z_p\). At other primes the polynomial discriminant is a unit, so the order's trace dual is itself and no index can occur. Thus
\(\mathcal O_E=\mathbf Z[\alpha]\) and \(d_E=-108\).

Let \(\rho_2\) be the standard two-dimensional representation of \(S_3\), the complement of the constants in its action on three letters. The transposition stabilizer has index three, hence
\[
\mathbf C[S_3/S_2]=\mathbf1\oplus\rho_2,
\qquad
\mathbf C[S_3]=\mathbf1\oplus\operatorname{sgn}\oplus\rho_2^{\oplus2}.
\tag{37}
\]
The sign character is the quadratic character \(\chi_{-3}\). Consequently
\[
\zeta_E(s)=\zeta_{\mathbf Q}(s)L_{\mathbf Q}(s,\rho_2),\qquad
\zeta_L(s)=\zeta_{\mathbf Q}(s)L_{\mathbf Q}(s,\chi_{-3})L_{\mathbf Q}(s,\rho_2)^2.
\tag{38}
\]
The non-Galois permutation assertion in Theorem 21.5 immediately gives
\[
\mathfrak f_{\mathbf Q}(\rho_2)=(108)=(2^2 3^3).
\tag{39}
\]
Here the trivial summand has conductor 1.

We check both local exponents directly. At 2, adjoining \(\zeta_3\) is unramified of degree two, since \(X^2+X+1\) is irreducible modulo 2. Adjoining \(\alpha\) is totally ramified of degree three and tame. The local splitting field has degree six, decomposition group \(S_3\), inertia \(C_3\), and no positive ramification group. A three-cycle has eigenvalues \(\zeta_3,\zeta_3^2\) on \(\rho_2\), so no invariant vectors. Formula (9) gives \(a_2(\rho_2)=2\).

At 3, the cubic extension is totally ramified and \(\alpha\) is a unit. Its different is generated by \(3\alpha^2\), so \(\delta_{E_3/\mathbf Q_3}=3\). The quadratic extension \(\mathbf Q_3(\zeta_3)\) is ramified of degree two. In the compositum the ramification index is divisible by both 3 and 2; its degree is six, so it is totally ramified of degree six. Its extension over \(E_3\) is tame quadratic, with different exponent 1. Formula (11) gives
\(\delta_{L_3/\mathbf Q_3}=1+2\cdot3=7\).
Now \(G_0=S_3\), while its wild inertia is its unique Sylow 3-subgroup \(C_3\). Hilbert's formula reads
\(7=5+\sum_{j\geq1}(|G_j|-1)\).
The positive groups are either \(C_3\) or trivial, so exactly one is nontrivial. Thus \(G_1=C_3,G_2=1\). Neither \(S_3\) nor \(C_3\) has invariants on \(\rho_2\), and
\[
a_3(\rho_2)=2+\frac36\,2=3.
\tag{40}
\]
This verifies (39) with the lower-group weights, independently of the global numerical prediction.

## 8. Orthogonal root numbers

An orthogonal representation here means the complexification of a finite-image real representation with an invariant positive definite inner product. Its global root number is the constant in (25). A local root number is the central epsilon constant for a nontrivial local additive character and self-dual measure. These local constants need not all be 1 even when the global constant is 1.

The higher-dimensional local epsilon family is supplied by [Local L-factors and epsilon-factors of Weil group representations, Theorem 3.0](https://kokunoyumeto.github.io/open-math-courses-public/courses/LG-GAL/local-l-factors-and-epsilon-factors.html#3-existence-and-uniqueness-of-local-constants), with its existence argument in sections 3A–3D and uniqueness in Theorem 3.2. The [orthogonal formula, Theorem 7.4](https://kokunoyumeto.github.io/open-math-courses-public/courses/LG-GAL/local-l-factors-and-epsilon-factors.html#7-sharp-twisting-and-orthogonal-root-numbers), has its real-induction, Clifford-class and dihedral Fourier arguments in Lemmas 7.5–7.8. The analytic proof of Theorem 21.3 above uses the rank-one theory and Brauer induction and does not depend on these higher-dimensional local arguments.

**Deligne's local orthogonal theorem.** If \(A\) is a virtual finite-image real representation of the absolute Galois group of a local field \(F\), with virtual dimension zero and determinant one, then
\[
W_F(A)=\exp\bigl(2\pi i\operatorname{inv}_F(\operatorname{cl}(w_2(A)))\bigr).
\tag{41}
\]
The total Stiefel–Whitney class extends to virtual representations by \(w(V-W)=w(V)w(W)^{-1}\); its degree-two part is \(w_2(A)\in H^2(G_F,\mathbf Z/2)\). Inflate from a finite quotient and map the coefficient \(1\) to \(-1\in\bar F^\times\). This gives \(\operatorname{cl}(w_2(A))\in\operatorname{Br}(F)\). The invariant is in \(\mathbf Q/\mathbf Z\); at a real place its nonzero value is \(1/2\), and at a complex place it is zero. In characteristic two the coefficient map is trivial and the right side is 1. Dimension zero removes measure dependence and determinant one removes additive-character dependence. The specified theorem and class construction are the ones owned by §7 of the provider, corresponding to Deligne (1976), (1.3)–(1.5). They are not proved by Brauer meromorphy alone.

Here is the global deduction with its precise inputs. It uses the local existence and orthogonal theorems just identified and [Brauer groups of local and global fields](brauer-groups-of-local-and-global-fields.md), section 4 and Theorem 24.4. That lesson proves that for every global Brauer class \(b\), all but finitely many local invariants vanish and \(\sum_v\operatorname{inv}_v(b_v)=0\), including arbitrary splitting groups and both characteristics. This is the required part of the Albert–Brauer–Hasse–Noether theorem.

**Fröhlich–Queyrut global theorem.** For a finite-image orthogonal global representation \(V\),
\[
W_K(V)=1.
\tag{42}
\]

**Deduction from those local and Brauer inputs.** First verify that the global constant in (25) is the product of local central constants. Interpret the provider's geometric local constants on \(V^\vee\) to match our arithmetic convention. For orthogonal representations this dualization changes nothing. Write
\(P_K(V)=\prod_v W_{K_v}(V)\); only finitely many factors differ from 1. Rank-one Tate theory, the written Hecke theorem, and section 6 show \(P_K(\chi)=W_K(\chi)\).

For a permutation representation \(P=\operatorname{Ind}_E^K\mathbf1\), let \(n=\dim P\), \(\eta=\det P\), and \(A=P-\eta-(n-1)\mathbf1\). This is a global real virtual representation of dimension zero and determinant one. Its Stiefel–Whitney class gives a global Brauer class. Formula (41) and the invariant sum law give \(P_K(A)=1\). The trivial character has global root number 1. Every quadratic character \(\eta\) also has global root number 1: for its quadratic field \(M\), (24) and Proposition 21.1 identify its completed L-function with \(\Lambda_M(s,\mathbf1)/\Lambda_K(s,\mathbf1)\), and both zeta completions have root number 1. The latter is the number-field zeta theorem in the Hecke provider and, for function fields, the trivial-character case of (34). Consequently \(P_K(P)=1\).

Local induction for virtual dimension zero implies, on subtracting \((\dim W)\mathbf1\),
\[
W_F(\operatorname{Ind}_{E_u}^F W)
=\lambda(E_u/F)^{\dim W}W_{E_u}(W),\quad
\lambda(E_u/F)=\frac{W_F(\operatorname{Ind}\mathbf1)}{W_{E_u}(\mathbf1)}.
\tag{43}
\]
Using all completions above each place, the product of these \(\lambda\)'s is \(P_K(P)/P_E(\mathbf1)=1\). Thus \(P_K(\operatorname{Ind}_E^K\chi)=P_E(\chi)=W_E(\chi)\). Integer Brauer induction and (26) give \(P_K(V)=W_K(V)\) for every finite-image representation. This proves the needed factorization from the stated local inputs, rather than assuming a separate global factorization theorem.

Finally for an arbitrary orthogonal \(V\) of dimension \(n\), put \(A=V-\det V-(n-1)\mathbf1\). Apply (41) at every place and the global invariant sum law to its global class. They give \(W_K(A)=P_K(A)=1\). The determinant is trivial or quadratic and has root number 1, as above, and so does the trivial character. Multiplicativity gives (42). \(\square\)

The assertion is global. For example the real sign character, with the negative exponential additive character used in lesson 12, has local central constant \(-i\). Its global quadratic counterpart has product 1, so the other factors cancel that phase. Nor does (42) apply to every self-dual complex representation: a symplectic representation need not be the complexification of a real orthogonal one.

## 9. Exercises and complete solutions

### Exercise 1 — The cubic zeta factor (easy)

Prove \(\zeta_{\mathbf Q(\sqrt[3]2)}(s)=\zeta_{\mathbf Q}(s)L_{\mathbf Q}(s,\rho_2)\), with every ramified Euler factor included.

**Solution.** Irreducibility at 2 and the nonsquare cubic discriminant show that the splitting field has group \(S_3\). The cubic field is fixed by the subgroup stabilizing one root, of order two. Its coset permutation representation is the three-letter representation. Its constant line is trivial, and the coordinate-sum-zero plane is \(\rho_2\), giving \(\operatorname{Ind}_{S_2}^{S_3}\mathbf1=\mathbf1\oplus\rho_2\). The ramified induction calculation (5)–(6) identifies its Euler factor with the product of the cubic field's factors above each prime. Additivity and \(L(s,\mathbf1)=\zeta_{\mathbf Q}(s)\) prove the identity. No factors at 2 or 3 have been deleted.

### Exercise 2 — The two local conductor exponents (medium)

Compute \(a_2(\rho_2)\) and \(a_3(\rho_2)\) directly from the lower ramification groups, and recover conductor 108.

**Solution.** At 2 the local cubic field is tame totally ramified of degree three, and the quadratic roots of unity form the unramified quadratic extension. Thus the splitting field has \(G_0=C_3\), \(G_j=1\) for \(j\geq1\). A three-cycle has eigenvalues \(\zeta_3,\zeta_3^2\) on the coordinate-sum-zero plane, so \(a_2=2\).

At 3 use the Eisenstein generator \(\beta\) of (36). Since \(\alpha\) is a unit, the derivative \(3\alpha^2\) has valuation 3 in the cubic field, so its different exponent is 3. The splitting field has total ramification degree six; its relative quadratic extension over the cubic field is tame, of different exponent 1. Different transitivity gives exponent \(1+2\cdot3=7\). In \(S_3\), the wild inertia is \(C_3\). Hilbert's formula forces \(G_0=S_3,G_1=C_3,G_2=1\), because the zero group contributes 5 and each nontrivial positive group contributes 2. Both nontrivial groups have zero invariants on \(\rho_2\), so (9) gives \(a_3=2+(3/6)2=3\). All other places are unramified, since the polynomial discriminant is a unit there. Hence the conductor is \(2^2 3^3=108\).

### Exercise 3 — Induction at a ramified prime (medium)

Prove the induction identity in Proposition 21.1 without assuming the base prime is unramified.

**Solution.** Fix its local decomposition and inertia groups \(D,I\). Split the restricted induced representation according to \(D\backslash G/H\); these double cosets are precisely the places of \(E=L^H\) over the base place. On a summand \(\operatorname{Ind}_J^D W_g\), taking \(I\)-invariants leaves copies of \(W_g^{I\cap J}\) indexed by \(I\backslash D/J\). A vector on an inertia orbit is determined by a stabilizer-invariant initial value, which proves this statement even when \(I\) is nontrivial. The arithmetic Frobenius cycles the \(f=[D:IJ]\) copies; after \(f\) steps it is the arithmetic Frobenius at the corresponding place of \(E\). The cyclic block determinant (6) changes \(q_v^{-s}\) into \(q_v^{-fs}=q_u^{-s}\). Multiplying over the double cosets gives the full local Euler identity, and absolute convergence then gives the global identity. At no point was \(I=1\) required.

### Exercise 4 — Discriminants from ramification (hard)

Derive the conductor–discriminant formula directly from the different formula, including the multiplicities of global irreducible characters.

**Solution.** At a fixed completion \(T/F\), its regular representation has dimension \(|G|\), and its \(G_j\)-invariants have dimension \(|G|/|G_j|\). Thus
\[
a_F(\mathbf C[G])
=\frac{|G|}{|G_0|}\sum_{j\geq0}(|G_j|-1)
=f(T/F)\delta_{T/F}
=v_F(\mathfrak d_{T/F}).
\tag{44}
\]
For a global Galois \(L/K\), the restriction of \(\mathbf C[\operatorname{Gal}(L/K)]\) to a decomposition group is the direct sum of \([G:D]\) copies of its regular representation: partition its basis into left \(D\)-orbits. Summing (44) therefore gives \([G:D]f(T/F)\delta_{T/F}\). The completed global integer lattice is the product of the \([G:D]\) local integer rings, and its trace determinant is the product of their trace determinants; hence that sum is exactly the valuation of \(\mathfrak d_{L/K}\).

Globally the regular character is \(\sum_{\rho\in\operatorname{Irr}(G)}(\dim\rho)\chi_\rho\). Since (9) is linear in the character, the same discriminant exponent is \(\sum_\rho(\dim\rho)a_{K_v}(\rho)\). Taking the ideal product over all finite places proves (20), with precisely the displayed multiplicities. General conductor integrality was proved in section 3, so the factors are actual integral ideals. For a non-Galois subfield, the analogous permutation computation (16) uses different transitivity to give its discriminant as well.

## What this lesson does not prove

Finite-group character theory, induction and integer Brauer induction are supplied by the three exact written representation-theory lessons identified at the beginning. The number-field rank-one analytic theorem is supplied by the written Hecke lesson; the function-field argument is proved in section 6. Hilbert's different formula and Herbrand's quotient theorem have the written local-field providers identified in lesson 10. The central Artin conductor integrality and discriminant arguments themselves are proved here.

The general local epsilon existence theorem and Deligne’s orthogonal theorem have the exact programme providers [LG-GAL-06, Theorem 3.0 and sections 3A–3D](https://kokunoyumeto.github.io/open-math-courses-public/courses/LG-GAL/local-l-factors-and-epsilon-factors.html#3-existence-and-uniqueness-of-local-constants) and [Theorem 7.4 with Lemmas 7.5–7.8](https://kokunoyumeto.github.io/open-math-courses-public/courses/LG-GAL/local-l-factors-and-epsilon-factors.html#7-sharp-twisting-and-orthogonal-root-numbers). The global invariant sum law used in section 8 is proved in this course’s lesson 24, Theorem 24.4. Equation (42) uses those local results and that sum law through the deduction above; the local theorem (41) is proved in its provider rather than repeated here. Artin’s number-field conjecture remains a conjecture.

## Editable edition

The reading edition provides the complete LaTeX source of this lesson, the cumulative course LaTeX and the editable source ZIP. The archive contains all twenty-four Markdown lessons, complete LaTeX bodies, original diagrams, metadata and reproduction instructions.

## References

The ramified induction identities, conductor integrality, conductor–discriminant identity and meromorphic functional equation are proved using the named internal character and Fourier lessons. The function-field analytic argument is written in section 6. The orthogonal deduction uses LG-GAL-06, Theorem 7.4, with its real-induction, Clifford-class and dihedral Fourier lemmas 7.5–7.8.

- [Bjorn Poonen, Tate’s Thesis, MIT 18.786 lecture notes (2015)](https://math.mit.edu/~poonen/786/notes.pdf).
- [Wen-Wei Li, Yanqi Lake Lectures on Algebra: Part 1](https://www.wwli.asia/downloads/YAlg1.pdf).
- [Pierre Deligne, Les constantes des équations fonctionnelles des fonctions L (1973), IAS archive](https://publications.ias.edu/sites/default/files/Number20.pdf).
- [Pierre Deligne, Les constantes locales de l’équation fonctionnelle de la fonction L d’Artin d’une représentation orthogonale (1976), IAS archive](https://publications.ias.edu/sites/default/files/Number26.pdf).

The [proof guide](../FREE_PROOFS.md) gives the lesson sequence and the exact prerequisite record. External references accompany the written arguments.
