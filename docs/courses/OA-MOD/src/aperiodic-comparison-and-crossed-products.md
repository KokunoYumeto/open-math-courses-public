# Aperiodic comparison and crossed products

Two approximately inner automorphisms can have the same kind of motion on central sequences without being conjugate by a unitary. On a strongly stable factor, asymptotic aperiodicity is nevertheless enough to compare them by an approximately inner change of coordinates and an inner perturbation. The perturbation can be arbitrarily small in a prescribed faithful state.

We connect that theorem to its complete earlier programme constructions, keeping the complementary factors and the state transport explicit. We then prove the induced normal isomorphism of integer crossed products in regular coordinates, including its action on the implementing unitary, the coefficient expectation and the dual circle.

## 1. The comparison theorem and its hypotheses

Let \(M\ne0\) be a factor with separable predual. Throughout Sections 1–6, suppose

\[
M\cong M\bar\otimes R,
\tag{AC.1}
\]

where \(R\) is the hyperfinite \(\mathrm{II}_1\) factor. This is strong stability. Write \(\overline{\operatorname{Int}}(M)\) for the closure of the inner automorphisms in the \(u\)-topology: pointwise norm convergence on \(M_*\). The group operations and the normality of the inner subgroup are proved in AQ01–02.

By CFR05, the condition

\[
p_a(\theta)=0
\tag{AC.2}
\]

means that no nonzero power is centrally trivial. Equivalently, every nonzero power of \(\theta_\omega\) is properly outer on \(M_\omega\), for every free ultrafilter \(\omega\). The finite algebra \(M_\omega\) need not be a factor or have separable predual. Ordinary outerness of the powers of \(\theta\) is not substituted for (AC.2).

**Aperiodic comparison theorem.** If

\[
\theta_1,\theta_2\in\overline{\operatorname{Int}}(M),
\qquad p_a(\theta_1)=p_a(\theta_2)=0,
\tag{AC.3}
\]

there are \(\sigma\in\overline{\operatorname{Int}}(M)\) and \(u\in\mathcal U(M)\) with

\[
\theta_2=\operatorname{Ad}(u)\,
             \sigma\theta_1\sigma^{-1}.
\tag{AC.4}
\]

More precisely, for every faithful normal state \(\varphi\) and every \(\varepsilon>0\), there are \(w\in\mathcal U(M)\) and \(\gamma\in\overline{\operatorname{Int}}(M)\) such that

\[
\begin{gathered}
\|w-1\|_{\varphi,\#}<\varepsilon,\\
\theta_2=\gamma\,\operatorname{Ad}(w)\theta_1\gamma^{-1},
\end{gathered}
\tag{AC.5}
\]

where \(\|x\|_{\varphi,\#}^2=\varphi(x^*x)+\varphi(xx^*)\).

The full earlier programme proof is Comparing asymptotically aperiodic automorphisms, Theorem 1.1 and Sections 2–6. Sections 2–5 below give the precise construction inputs for (AC.4); Section 6 proves the final passage to (AC.5). Each input links to its written proof, rather than replacing a proof by a paper citation.

## 2. Approximately invariant implementers

The quotient cohomology theorem bound in CFR08 has an ordinary-sequence consequence. For a factor with separable predual, if \(\theta\) is approximately inner and \(p_a(\theta)=0\), there are unitaries \(u_n\in M\) satisfying

\[
\begin{gathered}
\operatorname{Ad}(u_n)\longrightarrow\theta
       \quad\text{in the }u\text{-topology},\\
\theta(u_n^k)-u_n^k\longrightarrow0
       \quad\text{strongly* for every fixed }k\in\mathbb Z.
\end{gathered}
\tag{AC.6}
\]

This consequence does not require (AC.1). Its complete proof is Almost invariant inner implementers, Sections 1–3.

The proof begins with \(\operatorname{Ad}(v_n)\to\theta\). The defect

\[
d_n=v_n^*\theta(v_n)
\tag{AC.7}
\]

is ordinarily centralizing: the inner automorphisms it implements tend to the identity, and the norm of a unitary's predual commutator equals the corresponding inner-automorphism displacement. Cohomology in \(M_\omega\) supplies a unitary \(X\) such that, with \(D=[(d_n)]\),

\[
D=X^*\theta_\omega(X).
\tag{AC.8}
\]

The exact unitary-lifting theorem gives representatives \(x_n\). The corrected implementers \(v_nx_n^*\) have defect with quotient class
\(XD\theta_\omega(X^*)=1\). Section 3 of the cited proof selects one increasing subsequence on which both the predual tests and the faithful-state defect tests converge ordinarily. Both factors use the same selected coordinate.

There is a further analytic step in (AC.6). A strongly*-null bounded sequence cannot be multiplied arbitrarily on the right by varying unitaries. Section 1 of the implementer proof supplies the exact estimate: if \(\operatorname{Ad}(u_n)\to\theta\), then for fixed \(j\),

\[
\|a_nu_n^j\|_\psi^2
 =(\psi\circ\operatorname{Ad}(u_n^{-j}))(a_n^*a_n).
\tag{AC.9}
\]

The moving functional converges in norm to \(\psi\circ\theta^{-j}\). This controls the right product; the corresponding adjoint and left-product estimates complete the strong* argument. The finite power telescope then proves every fixed integer \(k\) in (AC.6). It gives no assertion uniform over all \(k\).

## 3. Exact matrix phases and tensor extraction

For the aperiodic case needed here, Matrix eigenvectors and tensor absorption, Lemma 3.1 and Theorem 3.2 has the following exact form. If \(M\) satisfies (AC.1) and \(p_a(\theta)=0\), then for any \(d\ge2\), any \(\lambda\in\mathbb T\), finitely many normal-functional tests and any positive tolerance, there are unital matrix units \(e_{ij}\) and a unitary \(a\) such that

\[
\begin{gathered}
\|[e_{ij},\psi_l]\|<\varepsilon,\\
\operatorname{Ad}(a)\theta(e_{ij})
       =\lambda^{i-j}e_{ij},\\
\|a-1\|_{\varphi,\#}<\varepsilon .
\end{gathered}
\tag{AC.10}
\]

The proof uses the stable case of the matrix-eigenvector lemma, exact matrix lifts, and a prescribed-support partial isometry to repair covariance. The relative-corner type-II input is supplied also by CFR06.

Two consequences of its complete Section 6 proof are used in the comparison:

- An arbitrarily small inner perturbation extracts the product clock action \(\sigma_0\) on \(R\), whose coordinate list contains every matrix size \(d\ge2\) infinitely often.
- An aperiodic action on a strongly stable factor can extract an identity action on an \(R\) tensor leg.

These are Corollary 6.2, with model parameters \(0\) and \(1\), respectively. The same section's Proposition 6.3 gives a small perturbation conjugate to the original action tensored with its model. These uses lie in the asymptotically aperiodic branch; the finite-period branch is a distinct statement.

The construction retains more than approximate commutation of matrix blocks. At stage \(v\), its correcting unitary lies in the preceding blocks' exact relative commutant. A state containing both \(\varphi\) and its translate by the preceding product controls multiplication by that varying product. Matrix averaging turns the centrality estimates into summable errors

\[
\sum_v\|\psi-\psi\circ E_{K_v}\|<\infty
\tag{AC.11}
\]

on a norm-total family. The complete splitting proof is Strong stability and tensor absorption, Theorem 3.1, with the norm-total extension in Section 1 of the matrix-eigenvector lesson. It constructs a faithful normal tail expectation and a spatial tensor decomposition. Commutation and generation alone would not establish that decomposition.

## 4. A common product with identity on the complement

Choose integers \(n_v\ge2\) with \(\sum_v n_v^{-1}<\infty\), let \(c_v\) be the cyclic shift on \(\mathbb C^{n_v}\), and form the tracial product

\[
\begin{gathered}
K_{\mathrm{mod}}=\bar\bigotimes_{v\ge1}
       (M_{n_v},\operatorname{tr}_{n_v})\cong R,\\
\alpha=\bigotimes_{v\ge1}\operatorname{Ad}(c_v).
\end{gathered}
\tag{AC.12}
\]

For each \(\theta\) as in (AC.3), the product-extraction theorem, Section 3 constructs \(W\in\mathcal U(M)\) and a normal decomposition

\[
\begin{gathered}
M=K\bar\otimes C,\qquad K\cong K_{\mathrm{mod}},\\
\operatorname{Ad}(W)\theta=\alpha\otimes\mathrm{id}_C,\\
\|W-1\|_{\varphi,\#}\le8\sum_v n_v^{-1}.
\end{gathered}
\tag{AC.13}
\]

The identification of \(K\) with the model intertwines the specified actions.

Here are the estimates that make the conclusion about \(C\) possible. Cyclic finite models for outer conjugacy, Theorem 4.1 supplies a finite projection cycle and an implementer \(u\) that still approximates the action on all listed predual tests. Its finite-order correction is

\[
U=u f_n(u^n)^*,\qquad U^n=1,
\tag{AC.14}
\]

where \(f_n(e^{it})=e^{it/n}\) for \(-\pi<t\le\pi\). The approximate implementer is \(u\); replacing it by \(U\) in the global predual estimate would be unjustified.

Sections 2–3 of that proof choose a spectral cut of uniformly small state mass before applying the discontinuous root. Lemma 5.1 then gives a centrality modulus independent of the state and algebra, for positive functionals dominated by the chosen state. Lemmas 5.2–5.3 supply the matrix-average bound and the exact finite coefficient tests. In the extraction induction, the errors are chosen with

\[
\delta_v=\frac{2^{-v}}{n_v^2(n_v+1)}.
\tag{AC.15}
\]

The averaging error is at most \(n_v^2(n_v+1)\delta_v=2^{-v}\), and the root correction costs at most \(\pi/n_v\) in operator norm.

The complete induction in the comparison proof simultaneously forces the inverse action to approach the inverse product action on a norm-total family. After tensor splitting, finite product actions converge on the whole predual, so the limiting complementary action is the identity in (AC.13). The normal extension of the finite-coordinate identifications and these predual limits are proved in Normal tensor tests and tracial GNS identifications, TF0–TF4. They allow an arbitrary nontracial complementary factor.

Apply (AC.13) to both \(\theta_i\), using the same sequence \((n_v)\). This produces two copies of the same product action. It does not yet prove that their complements are isomorphic to \(M\).

## 5. Comparing the complementary factors

The placement theorem Moving hyperfinite tensor factors, Theorem 1.1 says: if two hyperfinite \(\mathrm{II}_1\) subfactors \(A_1,A_2\) factorize a strongly stable separable-predual factor \(M\), and

\[
A_1'\cap M\cong M\cong A_2'\cap M,
\tag{AC.16}
\]

then an approximately inner automorphism of \(M\) takes \(A_1\) onto \(A_2\). Its Sections 2–4 prove convergence of both directions on the predual, exact coordinate matching, and expansion of a selected subproduct to the whole factor.

The complement condition (AC.16) must be established. In Section 4 of the comparison proof, the model action \(\alpha\) of (AC.12) first absorbs an identity \(R\) leg. Its asymptotic period is zero by Lemma 3.3 there: a tail Weyl unitary with frequency nearest to \(n_v/(2|q|)\) has displacement tending to \(2\) under each fixed nonzero power \(q\). Proposition 6.3 from Section 3 above therefore gives an inner perturbation and a decomposition

\[
K_{\mathrm{mod}}=A\bar\otimes B,\qquad
A\cong B\cong R,\qquad
\operatorname{Ad}(t)\alpha=\beta\otimes\mathrm{id}_B.
\tag{AC.17}
\]

The two factors here can be taken as inverse images of the two factors under that proposition's normal isomorphism.

Transport these same objects into the two product extractions. For suitable \(h_i\in\mathcal U(M)\), this gives

\[
\begin{gathered}
M=A_i\bar\otimes D_i,\qquad
\operatorname{Ad}(h_i)\theta_i
       =\beta_i\otimes\mathrm{id}_{D_i},\\
D_i=B_i\bar\otimes C_i
       \cong K_i\bar\otimes C_i\cong M.
\end{gathered}
\tag{AC.18}
\]

The \(\beta_i\) correspond to the same \(\beta\). Thus (AC.16) holds for the \(A_i\).

The placement theorem moves \(A_1\) to \(A_2\) by an approximately inner automorphism \(\sigma_0\). Its restriction may differ from the specified identification of the actions. Correct that restriction by an automorphism of \(A_2\), extended as the identity on \(D_2\). Every automorphism of \(R\) is approximately inner by Local approximation and the hyperfinite finite factor, Theorem 6.3. TF1 and TF4 prove that its tensor extension remains approximately inner. The corrected \(\sigma\) therefore satisfies

\[
\sigma(\operatorname{Ad}(h_1)\theta_1)\sigma^{-1}
       =\operatorname{Ad}(h_2)\theta_2.
\tag{AC.19}
\]

On the first tensor factor it is the chosen action identification; on each complement the action is the identity. Rearranging (AC.19) gives (AC.4) with

\[
u=h_2^*\sigma(h_1).
\tag{AC.20}
\]

This proves the first comparison assertion using the exact earlier constructions.

## 6. One small perturbation in the prescribed state

A unitary of \(M_\omega\) having an exact cohomology solution does not itself solve a prescribed equation for a unitary of \(M\). The ordinary result needed here is the approximate-coboundary lemma, Section 5: on the present strongly stable separable-predual factor, if \(p_a(\beta)=0\), then for every \(u\in\mathcal U(M)\), faithful normal state \(\rho\), and \(\varepsilon>0\), there is \(x\in\mathcal U(M)\) with

\[
\|xu\beta(x^*)-1\|_{\rho,\#}<\varepsilon.
\tag{AC.21}
\]

Approximate innerness of \(\beta\) is not required by that lemma.

Its full proof repairs ordinary finite projection partitions, performs the cyclic corner recursion, and obtains a residual supported on a level of mass tending to \(1/n\). It also proves that the recursively constructed varying multipliers preserve the strong*-null ideal. This is what justifies replacing the nearby actions and unitaries in the final estimate. The error bound before choosing a large coordinate is \(2\sqrt{2/n}\).

Starting with (AC.4), fix

\[
\beta=\sigma\theta_1\sigma^{-1},\qquad
\rho=\varphi\circ\sigma^{-1}.
\tag{AC.22}
\]

Conjugacy preserves asymptotic period, so (AC.21) applies. Put

\[
c=xu\beta(x^*),\qquad
w=\sigma^{-1}(c),\qquad
\gamma=\operatorname{Ad}(x^*)\sigma.
\tag{AC.23}
\]

Conjugating (AC.4) by \(\operatorname{Ad}(x)\) yields

\[
\operatorname{Ad}(x)\theta_2\operatorname{Ad}(x^*)
       =\operatorname{Ad}(c)\beta.
\tag{AC.24}
\]

Substitute (AC.22)–(AC.23) into (AC.24) to obtain
\(\theta_2=\gamma\operatorname{Ad}(w)\theta_1\gamma^{-1}\).
The closure of the inner subgroup is a group by AQ02, so \(\gamma\) is approximately inner. Finally

\[
\|w-1\|_{\varphi,\#}
   =\|c-1\|_{\varphi\circ\sigma^{-1},\#}<\varepsilon.
\tag{AC.25}
\]

The state \(\rho\) was chosen after \(\sigma\) and before \(x\). This order proves the estimate for the originally prescribed \(\varphi\), and completes (AC.5).

## 7. Normal transport of the crossed products

The next assertion needs only the outer-conjugacy equation (AC.4), not factoriality, strong stability, separable predual or approximate innerness. Let \(M\) be any nonzero von Neumann algebra, let \(\theta_1,\theta_2,\sigma\) be normal automorphisms, and suppose (AC.4) holds for \(u\in\mathcal U(M)\). Put

\[
N_i=M\rtimes_{\theta_i}\mathbb Z,\qquad
U_i xU_i^*=\theta_i(x).
\tag{AC.26}
\]

There is a normal isomorphism with normal inverse

\[
\begin{aligned}
\Phi:N_1&\longrightarrow N_2,\\
\Phi(x)&=\sigma(x),\\
\Phi(U_1)&=u^*U_2.
\end{aligned}
\tag{AC.27}
\]

It intertwines the dual actions with convention
\(\widehat\theta_{i,z}(U_i)=zU_i\), and

\[
E_2\Phi=\sigma E_1,
\tag{AC.28}
\]

where \(E_i\) is the coefficient expectation.

Here is a spatial proof of normality and surjectivity. Choose a faithful normal representation \(\rho:M\to B(H)\), and use \(\rho_1=\rho\circ\sigma\), \(\rho_2=\rho\) for the two regular constructions. The normal regular representation and its independence of the initial faithful representation are proved in NR3–NR4. On \(\ell^2(\mathbb Z;H)\),

\[
\begin{gathered}
[\pi_i(a)\xi]_k=\rho_i(\theta_i^{-k}(a))\xi_k,\\
[U_i\xi]_k=\xi_{k-1}.
\end{gathered}
\tag{AC.29}
\]


Set \(\beta=\sigma\theta_1\sigma^{-1}\). Define unitaries \(b_n\), for all integers \(n\), by

\[
b_0=1,\qquad b_{n+1}=b_n\beta^n(u).
\tag{AC.30}
\]

The recurrence uniquely determines positive and negative indices. For fixed \(m\), the families \(b_{m+n}\) and \(b_m\beta^m(b_n)\) agree at \(n=0\) and satisfy the same recurrence in both directions. Hence

\[
b_{m+n}=b_m\beta^m(b_n),\qquad
\theta_2^n=\operatorname{Ad}(b_n)\beta^n.
\tag{AC.31}
\]

The second identity follows by induction from \(\theta_2=\operatorname{Ad}(u)\beta\); applying the inverse recurrence proves it for negative \(n\).

Define the diagonal Hilbert unitary

\[
[D\xi]_k=\rho(b_{-k})\xi_k.
\tag{AC.32}
\]

Its inverse has diagonal entries \(\rho(b_{-k}^*)\); both preserve the sum of the squared coordinate norms. From (AC.29)–(AC.31),

\[
D\pi_1(a)D^*=\pi_2(\sigma(a)).
\tag{AC.33}
\]

For the shift, (AC.30) gives

\[
\begin{aligned}
b_{-k}b_{1-k}^*
 &=b_{-k}\beta^{-k}(u^*)b_{-k}^*\\
 &=\theta_2^{-k}(u^*).
\end{aligned}
\tag{AC.34}
\]

Thus

\[
DU_1D^*=\pi_2(u^*)U_2.
\tag{AC.35}
\]

Conjugation by \(D\) is normal with normal inverse: every normal vector-series test pulls back by applying \(D^*\) to its vectors, preserving the square-summable bounds. The images in (AC.33)–(AC.35) generate \(N_2\), since \(\sigma(M)=M\) and
\(U_2=\pi_2(u)\Phi(U_1)\). Taking the generated von Neumann algebras proves (AC.27), including onto-ness, without inferring normality from the algebraic covariance relation alone.

The diagonal phase unitary \(L_z\), given by
\([L_z\xi]_k=z^k\xi_k\), implements the dual circle on each regular algebra. It commutes with \(D\). Therefore \(\Phi\) intertwines these actions on every element.

Finally compression to coordinate zero is the coefficient expectation, with the initial representation understood. The proof in DAS02 uses only the regular matrix entries: for a Fourier polynomial, \(X_{kk}=\rho_i(\theta_i^{-k}(E_i(X)))\); normality extends the identity to all \(X\). A positive operator with all those diagonal entries zero is zero, giving faithfulness. This argument works in either faithful normal representation in (AC.29). Since \(b_0=1\), coordinate-zero compression is unchanged by \(D\), so

\[
\rho(E_2(\Phi(X)))=\rho(\sigma(E_1(X))).
\]

Faithfulness of \(\rho\) proves (AC.28).

## 8. Consequences and orientation checks

Under (AC.3), Sections 5 and 7 show that the two integer crossed products are normally isomorphic by a map intertwining their dual circles. The map remembers more than an abstract algebra isomorphism: it takes the coefficient copy through the approximately inner \(\sigma\) and sends the implementing unitary to \(u^*U_2\).

For any normal positive functional \(\varphi\) on \(M\), equation (AC.28) gives

\[
(\varphi\circ\sigma^{-1}\circ E_2)\circ\Phi
       =\varphi\circ E_1.
\tag{AC.36}
\]

Thus the coefficient functionals have the exact corresponding transport. When \(\varphi\) is a faithful normal state, so are both functionals on the crossed products, by faithfulness of the expectations.

The small-perturbation form (AC.5) gives a useful refinement. Apply Section 7 with \(\sigma=\gamma\) and \(u=\gamma(w)\), because
\(\theta_2=\operatorname{Ad}(\gamma(w))\gamma\theta_1\gamma^{-1}\).
Then

\[
\Phi(U_1)=\gamma(w^*)U_2,\qquad
\|\gamma(w^*)-1\|_{\varphi\circ\gamma^{-1},\#}
       =\|w-1\|_{\varphi,\#}<\varepsilon.
\tag{AC.37}
\]

This estimate controls the coefficient unitary in the transported base state. Multiplication by \(U_2\) changes the state in one of the two seminorms, so (AC.37) is not asserted as the same bound for \(\Phi(U_1)-U_2\).

The adjoint in (AC.27) is necessary. Covariance gives

\[
(u^*U_2)\sigma(x)(u^*U_2)^*
 =u^*\theta_2(\sigma(x))u
 =\sigma(\theta_1(x)).
\tag{AC.38}
\]

For a concrete check, take \(M=M_2(\mathbb C)\), \(\theta_1=\mathrm{id}\), \(\sigma=\mathrm{id}\), \(u=\operatorname{diag}(1,i)\), and \(\theta_2=\operatorname{Ad}(u)\). Formula (AC.38) fixes \(e_{12}\), as it must. Replacing \(u^*U_2\) by \(uU_2\) instead gives \(\operatorname{Ad}(u^2)(e_{12})=-e_{12}\), violating covariance. This finite example checks Section 7 and is not an instance of the aperiodic theorem.

No type classification of these crossed products follows from the comparison alone. Applying it to type \(\mathrm{III}_\lambda\) actions requires the module and central-period hypotheses of that later classification. The result established here is the full asymptotically aperiodic comparison (AC.4)–(AC.5), together with the explicit dual-equivariant transport (AC.27)–(AC.28).

## Source

Masamichi Takesaki, *Theory of Operator Algebras III*, Chapter XVII, Theorem 3.1, printed p.270, with the construction through p.282. The exact programme proofs used above are the linked OA-CLASSIFY and OA-APPROX lessons and their specified tensor and topology companions. The regular-coordinate crossed-product argument in Section 7 supplies its complete unitary, inverse, generator, expectation and dual-action checks.
