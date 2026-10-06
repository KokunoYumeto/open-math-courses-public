# The Connes–Thom isomorphism II: surjectivity, naturality and consequences

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The missing step from Lesson 10 is universal surjectivity of the Wiener–Hopf index. We prove it by moving a coefficient representation into the complement of a shrinking rank-one projection. The complementary representation has the same \(K_0\)-map, while the sum converges to the original representation. This forces the rank-one inclusion to have zero map into the extension algebra.

Keep the positive Fourier transform, left translations and kernel-minus-cokernel boundary of Lesson 10. Put
\[
 B_\alpha=A\rtimes_\alpha\mathbb R,\qquad
 W_\alpha=C_0(\mathbb R\cup\{+\infty\},A)
             \rtimes_{\tau\otimes\alpha}\mathbb R.
 \tag{11.1}
\]
Write \(\partial_1^\alpha,\partial_0^\alpha\) for its index and exponential boundaries, identified with coefficient K-theory by the untwisting and rank-one corner of Proposition 10.1.

## Shrinking the scalar operators

For \(\varepsilon>0\), let
\[
 \begin{gathered}
 h_\varepsilon(t)=\varepsilon^{-1/2}
       e^{-t/(2\varepsilon)}\chi(t),\qquad
 E_\varepsilon=\theta_{h_\varepsilon,h_\varepsilon},\\
 (F_\varepsilon\xi)(t)=
       \chi(t)\int_0^t\varepsilon^{-1}
       e^{-(t-r)/(2\varepsilon)}\xi(r)\,dr,\qquad
 S_\varepsilon=1-F_\varepsilon .
 \end{gathered}
 \tag{11.2}
\]
Here \(\chi\) is the indicator of \((0,\infty)\). The faithful scalar representation of Lesson 10 puts these in the scalar Wiener–Hopf algebra and its unitization. The same product integrals, with \(t,r\) divided by \(\varepsilon\), give
\[
 S_\varepsilon^*S_\varepsilon=1,\qquad
 S_\varepsilon S_\varepsilon^*=1-E_\varepsilon.
 \tag{11.3}
\]
In crossed-product coordinates the projection is
\[
 E_\varepsilon(s,t)=\varepsilon^{-1}
       e^{s/(2\varepsilon)}e^{-t/\varepsilon}
       \chi(t)\chi(t-s).
 \tag{11.4}
\]

These elements are norm continuous in \(\varepsilon>0\). For \(E_\varepsilon\), the vectors \(h_\varepsilon\) are \(L^2\)-continuous on every compact interval of positive \(\varepsilon\), by dominated convergence; rank-one operators are therefore norm continuous. For \(F_\varepsilon\), let \(P_+\) be multiplication by \(\chi\). Its operator expression is
\[
 F_\varepsilon=C(a_\varepsilon)P_+,\qquad
 a_\varepsilon(s)=\varepsilon^{-1}e^{-s/(2\varepsilon)}\chi(s),
 \tag{11.5}
\]
where \(C(a)\) denotes convolution. The kernels \(a_\varepsilon\) are \(L^1\)-continuous for positive \(\varepsilon\), so the operator norm difference is bounded by their \(L^1\)-difference. Faithfulness transfers this continuity to the scalar C*-algebra.

For now assume \(A\) is unital. The equivariant coefficient map \(f\mapsto f1_A\) inserts the scalar operators into \(W_\alpha\). It is contractive on full crossed products, so the continuity and identities above persist. The constant coefficient \(a\) defines a multiplier \(\mu(a)\) of \(W_\alpha\), with the core formulas
\[
 (\mu(a)f)(s,t)=a f(s,t),\qquad
 (f\mu(a))(s,t)=f(s,t)\alpha_s(a).
 \tag{11.6}
\]
Indeed constant functions are multipliers of the cone coefficient algebra; its nondegenerate canonical representation extends to those multipliers. In particular \(\mu(1)=1\).

## A split algebra for the homotopy

We need an auxiliary algebra in which inclusion of \(W_\alpha\) is injective on K-theory. Make the quotient visible by defining
\[
 \mathcal D_\alpha=
 \{(w+\mu(a),a):w\in W_\alpha,\ a\in A\}
 \subset M(W_\alpha)\oplus A.
 \tag{11.7}
\]
It is a C*-algebra: \(W_\alpha\) is a closed ideal of its multiplier algebra, and \(\mu\) is a *-homomorphism. It is closed because convergence of the second coordinate gives convergence of \(a\), after which subtracting \(\mu(a)\) gives a convergent element of \(W_\alpha\). Its unit is \((1,1)\), and the projection onto \(a\) gives the split extension
\[
 0\longrightarrow W_\alpha\xrightarrow{j}\mathcal D_\alpha
 \longrightarrow A\longrightarrow0,\qquad
 j(w)=(w,0),\quad \widetilde\mu(a)=(\mu(a),a).
 \tag{11.8}
\]
The general split exactness prerequisite from Lesson 10 makes \(j_*\) injective on \(K_0\).

Set \(\widetilde S_\varepsilon=(S_\varepsilon,1)\) and
\(\widetilde E_\varepsilon=(E_\varepsilon,0)\). They belong to \(\mathcal D_\alpha\), since \(S_\varepsilon-1=-F_\varepsilon\in W_\alpha\). The transported coefficient corner is
\[
 \phi_\varepsilon(a)(s,t)=\alpha_t(a)E_\varepsilon(s,t),
 \qquad \psi_\varepsilon=j\phi_\varepsilon .
 \tag{11.9}
\]
It is interpreted by norm completion, as in (10.17). Under untwisting it is exactly \(a\otimes E_\varepsilon\), hence a *-homomorphism. It takes values in the \(E_\varepsilon\)-corner and is point-norm continuous for positive \(\varepsilon\).

Define
\[
 \omega_\varepsilon(a)=
       \widetilde S_\varepsilon\widetilde\mu(a)
                      \widetilde S_\varepsilon^*,
 \qquad
 \mu_\varepsilon=\omega_\varepsilon+\psi_\varepsilon.
 \tag{11.10}
\]
The isometry identity makes \(\omega_\varepsilon\) a *-homomorphism, with range in the complementary corner \(1-\widetilde E_\varepsilon\). The two ranges are orthogonal, so their sum is also a *-homomorphism. They are point-norm continuous for \(\varepsilon>0\).

For every projection \(p\in M_n(A)\), the partial isometry
\((\widetilde S_\varepsilon\otimes1_n)\widetilde\mu_n(p)\)
has initial projection \(\widetilde\mu_n(p)\) and final projection
\(\omega_{\varepsilon,n}(p)\). Thus
\[
 (\omega_\varepsilon)_*=\widetilde\mu_*
       :K_0(A)\longrightarrow K_0(\mathcal D_\alpha).
 \tag{11.11}
\]
This checks all generators of \(K_0(A)\), since \(A\) is currently unital.

## The estimate at zero

For \(a\in A\), put
\[
 \begin{aligned}
 I_\varepsilon(a)&=\varepsilon^{-1}\int_0^\infty
       \|a-\alpha_{-s}(a)\|e^{-s/(2\varepsilon)}\,ds,\\
 d_\varepsilon(a)&=\sup_{t\ge0}
       \|\alpha_t(a)-a\|e^{-t/\varepsilon}.
 \end{aligned}
 \tag{11.12}
\]
Both tend to zero. In the first integral substitute \(s=\varepsilon v\), use point-norm continuity and dominate by \(2\|a\|e^{-v/2}\). For the second split \(t\) at a fixed small \(\eta>0\): continuity bounds the first part, while the rest is at most \(2\|a\|e^{-\eta/\varepsilon}\).

**Lemma 11.1.** In \(\mathcal D_\alpha\),
\[
 \|\mu_\varepsilon(a)-\widetilde\mu(a)\|
       \le 2I_\varepsilon(a)+4d_\varepsilon(a).
 \tag{11.13}
\]
In particular, defining \(\mu_0=\widetilde\mu\) extends the path to a point-norm continuous homotopy.

**Proof.** We estimate first coordinates; the second coordinates of the difference are zero. Write \(\psi_\varepsilon(a)\) for its first coordinate in the following estimates. Using (11.3), split the difference into
\[
 \begin{aligned}
 &S_\varepsilon\mu(a)S_\varepsilon^*
                  -S_\varepsilon S_\varepsilon^*\mu(a),\\
 &\phi_\varepsilon(a)-E_\varepsilon\mu(a).
 \end{aligned}
 \tag{11.14}
\]
The first norm is at most \(\|\mu(a)F_\varepsilon^*
                    -F_\varepsilon^*\mu(a)\|\).
The scalar involution gives
\[
 F_\varepsilon^*(s,t)=
   \varepsilon^{-1}e^{s/(2\varepsilon)}\chi(-s)\chi(t).
\]
Formula (11.6) and the full \(L^1\)-norm bound give
\[
 \|\mu(a)F_\varepsilon^*-F_\varepsilon^*\mu(a)\|
       \le I_\varepsilon(a).
 \tag{11.15}
\]

Here and below the inequalities are justified before passing to the discontinuous formulas. Replace each indicator by the continuous functions \(g_\delta\) of Lesson 10, with \(0\le g_\delta\le\chi\). The continuous approximants to \(F_\varepsilon\) converge in the scalar full norm and therefore in \(W_\alpha\). Their adjoint commutator has the displayed pointwise majorant. For \(E_\varepsilon\), use
\(h_{\varepsilon,\delta}(t)=\varepsilon^{-1/2}e^{-t/(2\varepsilon)}g_\delta(t)\).
These converge in \(L^2\), so both the transported coefficient corners and the scalar projections converge in norm. Their coefficients are continuous, their group \(L^1\)-norms are finite, and their magnitudes are bounded by (11.4). Applying the continuous-core \(L^1\) estimate and then taking the norm limit proves the inequalities for the original elements.

The second expression in (11.14) is consequently bounded by
\[
 \int_{\mathbb R}\sup_t
    \|\alpha_t(a)-\alpha_s(a)\|E_\varepsilon(s,t)\,ds.
 \tag{11.16}
\]
For \(s\ge0\), only \(t\ge s\) contributes. Write \(t=s+r\). Isometry of \(\alpha_s\) turns its integrand into
\[
 \varepsilon^{-1}e^{-s/(2\varepsilon)}
       \sup_{r\ge0}\|\alpha_r(a)-a\|e^{-r/\varepsilon},
\]
whose integral over positive \(s\) is \(2d_\varepsilon(a)\).
For \(s<0\), only \(t\ge0\) contributes, and
\[
 \|\alpha_t(a)-\alpha_s(a)\|e^{-t/\varepsilon}
 \le d_\varepsilon(a)+\|a-\alpha_s(a)\|.
\]
The integral over negative \(s\) is at most
\(2d_\varepsilon(a)+I_\varepsilon(a)\).
Adding this to (11.15) proves (11.13). The decay in the positive-\(s\) substitution is \(e^{-r/\varepsilon}\). ∎

## Surjectivity, first unital and then general

**Proposition 11.2.** For every \(A,\alpha\), the map
\(\partial_1^\alpha:K_1(B_\alpha)\to K_0(A)\) is surjective.

**Proof.** If \(A\) is unital, Lemma 11.1 and homotopy invariance give
\((\mu_\varepsilon)_*=\widetilde\mu_*\).
Orthogonal addition in K-theory and (11.11) give, for any positive \(\varepsilon\),
\[
 \widetilde\mu_*=(\mu_\varepsilon)_*
       =(\omega_\varepsilon)_*+(\psi_\varepsilon)_*
       =\widetilde\mu_*+(\psi_\varepsilon)_*.
 \tag{11.17}
\]
Thus \((\psi_\varepsilon)_*=0\). Injectivity of \(j_*\) in (11.8) implies
\((\phi_\varepsilon)_*:K_0(A)\to K_0(W_\alpha)\) is zero.
But \(\phi_\varepsilon\) is the stability corner followed by the inclusion of the ideal in the Wiener–Hopf extension. Exactness at that ideal's \(K_0\) therefore makes its incoming index map surjective.

For arbitrary \(A\), adjoin an external unit and extend \(\alpha\) by fixing scalars. The equivariantly split sequence
\[
 0\longrightarrow A\longrightarrow A^+
       \longrightarrow\mathbb C\longrightarrow0
 \tag{11.18}
\]
gives split exact coefficient K-theory sequences and, by full exactness, exact crossed-product sequences. The boundary naturality from Lesson 10 gives the commutative diagram with rows
\[
 \begin{gathered}
 K_1(B_\alpha)\longrightarrow K_1(B_{\alpha^+})
                     \longrightarrow K_1(C_0(\mathbb R)),\\
 K_0(A)\longrightarrow K_0(A^+)
                     \longrightarrow K_0(\mathbb C),
 \end{gathered}
 \tag{11.19}
\]
and vertical arrows the three index maps. The middle is onto by the unital argument. The last is injective by the explicit scalar calculation (10.31).

Take \(x\in K_0(A)\), and choose \(y\in K_1(B_{\alpha^+})\) whose boundary is the inclusion of \(x\). The scalar image of \(y\) has boundary zero, hence is zero. Exactness of the upper row makes \(y\) the image of some \(z\in K_1(B_\alpha)\). Commutativity says the images of \(\partial_1^\alpha z\) and \(x\) in \(K_0(A^+)\) agree. The lower inclusion is injective by split exactness, so \(\partial_1^\alpha z=x\). ∎

**Theorem 11.3 (Connes–Thom).** For every C*-algebra \(A\) and every point-norm continuous real action \(\alpha\), both Wiener–Hopf boundaries are isomorphisms:
\[
 \partial_1^\alpha:K_1(B_\alpha)\cong K_0(A),\qquad
 \partial_0^\alpha:K_0(B_\alpha)\cong K_1(A).
 \tag{11.20}
\]
No separability or unitality assumption is imposed.

**Proof.** Proposition 11.2 supplies exactly the universal surjectivity hypothesis of Proposition 10.2. That proposition proves both groups of \(W_\alpha\) vanish and both boundaries are bijective. ∎

## Naturality and the two normalizations

Define the inverse-boundary family
\[
 T_\alpha^0=(\partial_1^\alpha)^{-1},\qquad
 T_\alpha^1=(\partial_0^\alpha)^{-1}.
 \tag{11.21}
\]
Thus \(T_\alpha^i:K_i(A)\to K_{i+1}(B_\alpha)\), with degrees modulo two. For any equivariant *-homomorphism \(v:(A,\alpha)\to(D,\beta)\), including degenerate maps, the core morphism of extensions from Lesson 10 and naturality of K-theory boundaries give
\[
 (v\rtimes1)_*T_\alpha^i=T_\beta^i v_*.
 \tag{11.22}
\]
This follows by composing the commuting boundary square with its inverse isomorphisms.

We fix ordinary positive Bott maps as in Lesson 10: \(\beta_A\) for \(K_0\to K_1(SA)\), and \(\theta_A\) for \(K_1\to K_0(SA)\). Each new suspension coordinate is placed first. Write \(b_A^0=\beta_A\), \(b_A^1=\theta_A\).

For the trivial action the exact signs are
\[
 \begin{array}{c|cc}
 i&0&1\\ \hline
 T_{\mathrm{triv}}^i&-\beta_A&-\theta_A .
 \end{array}
 \tag{11.23}
\]
For \(i=0\), a projection gives an equivariant map from \(\mathbb C\) to a matrix algebra over \(A\). Naturality and (10.31) show
\(\partial_1^{\mathrm{triv}}\beta_A[p]=-[p]\).
Differences of projections prove this for unital \(A\); the split unitization sequence and its injective \(K_0\)-map prove it for every \(A\).

For completeness the parity-one sign requires a second calculation. The general exponential-boundary convention gives
\[
 \partial_0^\alpha
   =-\theta_A^{-1}\partial_1^{S\alpha}\beta_{B_\alpha},
 \tag{11.24}
\]
where \((SA)\rtimes_{S\alpha}\mathbb R\) is identified with
\(S(B_\alpha)\) while retaining the old suspension coordinate first.
The minus sign is required by the positive exponential convention: The six-term exact sequence and the exponential map, Theorem 1.1, equations (1.5)–(1.9) proves the suspended-index comparison. We reuse that general extension result. Its matrix path identifies the suspended index with the negative suspension of the exponential class.

The ordinary Bott maps have a coordinate interchange sign. We prove the precise form needed here without assuming a general exterior-product theorem.

**Lemma (interchanging the two suspension coordinates).** In coordinates \(r,u\),
\[
 \beta^r_{S_u A}\theta_A^u
 =-\operatorname{flip}_*
       \bigl(\beta^u_{S_r A}\theta_A^r\bigr)
 \quad\text{in }K_1(S_r S_u A).
 \tag{11.25}
\]
This holds for every C*-algebra \(A\).

**Proof.** First take \(A=C(\mathbb T)\). Write \(I=C_0(\mathbb R^2)\) and let \(q\) be the planar Bott projection, with scalar value \(P=q(\infty)\). The written programme lesson *Bott periodicity*, Theorem 4.1 and §6, proves \(K_0(I)=\mathbb Z([q]-[P])\), \(K_1(I)=0\), and that exchanging the two real coordinates negates \([q]-[P]\). The same lesson's coefficient Toeplitz argument gives \(K_1(I\otimes\mathcal T)=K_1(I)=0\), where \(\mathcal T\) is the Toeplitz algebra. The six-term sequence therefore makes the boundary
\(K_1(I\otimes C(\mathbb T))\to K_0(I)\) injective.

Let \(z\) be the circle coordinate. The unitary
\[
w=(qz+1-q)(P\overline z+1-P)
\tag{11A.1}
\]
belongs to the unitization of \(I\otimes C(\mathbb T)\), with scalar value one at infinity. The Toeplitz lift of \(qz+1-q\) is \(qS+1-q\), where \(S\) is the unilateral shift. Its initial defect is zero and its final defect is \(q\otimes e_{00}\). Thus its index is \(-[q]\). The constant-projection factor has the opposite index \([P]\). Boundary additivity gives
\(\partial[w]=-[q]+[P]\).
For rigor, compute these two indices over \(I^\dagger\), then use the split scalar quotient and boundary naturality to pass to the relative group over \(I\). The result lies in that relative group because the two scalar projections coincide. Its value generates \(K_0(I)\). Injectivity and this generator show that the boundary is an isomorphism.

Boundary naturality and the planar sign now show that coordinate flip acts as minus identity on \(K_1(I\otimes C(\mathbb T))\). In particular it negates the image of \([z]\) under either ordered Bott iteration. Relabeling the two ordered coordinates gives exactly (11.25) for \([z]\), and therefore for every circle K-class.

For arbitrary \(A\), represent a K-class by a unitary \(v\) in a finite matrix algebra over \(A^\dagger\), with scalar part one. The homomorphism \(C(\mathbb T)\to M_n(A^\dagger)\), \(z\mapsto v\), transports the circle identity by naturality of \(\beta\) and \(\theta\). Matrix stability removes the matrix size. The transported identity lies in the relative scalar kernel; split exactness embeds that kernel, so it gives (11.25) over \(A\). Every K-class has such a representative. No separability or countable-generation assumption has entered. ∎

The graded exterior-product formulation of this sign is described by Blackadar, *K-Theory for Operator Algebras*, §§14.4, 18.9–18.10 and 19.2.5. The elementary Toeplitz and planar-clutching argument above supplies the particular interchange identity used in this lesson.

Apply (11.24) to \(\theta_A^u x\) for the trivial action. Equation (11.25) makes its suspended input minus the positive Bott loop in the frequency \(u\), with coefficient class \(\theta_A^r x\). The already proved degree-zero calculation makes the suspended index of that input \(+\theta_A^r x\). The outer minus in (11.24), followed by \(\theta_A^{-1}\), gives \(-x\). Thus
\(\partial_0^{\mathrm{triv}}\theta_A=-\operatorname{id}\), proving (11.23).

It is often useful to use positive projection normalization instead:
\[
 \Gamma_\alpha^i=(-1)^{i+1}T_\alpha^i,\qquad
 \Phi_\alpha^i=(-1)^i\Gamma_\alpha^i
              =-T_\alpha^i.
 \tag{11.26}
\]
Then \(\Gamma_{\mathrm{triv}}^0=\beta_A\),
\(\Gamma_{\mathrm{triv}}^1=-\theta_A\), whereas
\(\Phi_{\mathrm{triv}}^i=b_A^i\) in both parities. These are the suspension-compatible and index-normalized conventions used in *Frequency calculus for an action of Euclidean space*, §7. Equation (11.26) specifies the normalization of our family; comparison with the projection construction is developed in Lesson 12. The names do not alter the kernel-minus-cokernel index boundary.

Indeed, invert (11.24) to get the precise suspension identity
\[
 \beta_{B_\alpha}T_\alpha^1
       =-T_{S\alpha}^0\theta_A.
 \tag{11.27}
\]
Here \(\Gamma_\alpha^1=T_\alpha^1\) and \(\Gamma_{S\alpha}^0=-T_{S\alpha}^0\), so \(\beta_{B_\alpha}\Gamma_\alpha^1=\Gamma_{S\alpha}^0\theta_A\). Thus \(\Gamma\) commutes with the suspension comparison, while \(T\) and \(\Phi=-T\) anticommute. Equation (11.23) explains why declaring every inverse boundary to be the positive Bott map would lose a sign.

## Iteration in ordered coordinates

Let \(\alpha\) be a continuous action of \(\mathbb R^n\). Cross successively in the directions \(e_n,e_{n-1},\ldots,e_1\). Each remaining direction acts on the preceding crossed product by its coefficient action and fixes the canonical multipliers of the directions already crossed. Commutation of the original directions gives covariance and point-norm continuity on compact cores.

Iterated integration identifies the resulting algebra with \(A\rtimes_\alpha\mathbb R^n\): its covariant representations consist exactly of a coefficient representation and \(n\) commuting unitary one-parameter groups implementing \(\alpha\). The two universal maps are inverse on these generators. Successive applications of Theorem 11.3 give
\[
 K_i(A\rtimes_\alpha\mathbb R^n)\cong K_{i+n}(A).
 \tag{11.28}
\]
Place each new frequency coordinate first, so the final target order is \((u_1,\ldots,u_n)\). Let \(\Theta_A^{n,i}\) be the corresponding ordinary ordered Bott iteration starting in degree \(i\).

For the three ordered Thom families the signs are
\[
 \begin{aligned}
 \Phi_\alpha^{(n),i}
    &=(-1)^n T_\alpha^{(n),i},\\
 \Phi_\alpha^{(n),i}
    &=(-1)^{ni+n(n-1)/2}\Gamma_\alpha^{(n),i},\\
 T_{\mathrm{triv}}^{(n),i}
    &=(-1)^n\Theta_A^{n,i},\qquad
 \Phi_{\mathrm{triv}}^{(n),i}=\Theta_A^{n,i}.
 \end{aligned}
 \tag{11.29}
\]
To verify these, the input parities at the successive steps are \(i,i+1,\ldots,i+n-1\). Each conversion from \(T\) to \(\Phi\) contributes \(-1\), giving \((-1)^n\). The conversion from \(\Gamma\) contributes \((-1)^{i+k}\); summing these input parities gives \(ni+n(n-1)/2\). At the trivial action every inverse boundary is minus the appropriate ordinary Bott map, proving the third formula.

In particular the two-coordinate inverse-boundary iteration equals the ordered Bott map in either starting parity. The suspension-compatible two-step iteration is minus that map. The index-normalized iteration equals the ordered Bott map. Exchanging the two frequency coordinates reverses the ordered ordinary Bott orientation by (11.25).

The same coordinate-order rule holds for an arbitrary action. To justify transferring the rule, set \(D=C([0,1],A)\) and
\((\rho_sF)(r)=\alpha_{rs}(F(r))\). Finite approximation of the compact range of \(F\) proves continuity of this action. Each evaluation \(e_r:D\to A\) is equivariant for \(\rho\) and the scaled action \(\alpha^{(r)}\). Ordinary contraction of the interval makes \((e_r)_*\) a K-isomorphism. Naturality and the already proved invertible ordered Thom maps then make \((e_r\rtimes1)_*\) a K-isomorphism. The two coordinate-order maps form commuting naturality squares with these evaluations. Since their sign relation holds at \(r=0\), it holds at \(r=1\). This argument does not cross a nonequivariant homotopy inverse.

## Semidirect products and solvable groups

Let \(G=N\rtimes_\vartheta H\) be a semidirect product of locally compact groups, acting on \(A\). Fix left Haar measures \(dn,dh\), and define the modulus \(m(h)>0\) by
\[
 dn(\vartheta_h E)=m(h)\,dn(E).
 \tag{11.30}
\]
The induced action on \(A\rtimes N\), specified on multiplier generators by
\(\beta_h(i_A(a))=i_A(\alpha_h(a))\) and
\(\beta_h(i_N(n))=i_N(\vartheta_h n)\), is on compact cores
\[
 (\beta_hf)(n)=m(h)^{-1}\alpha_h(f(\vartheta_h^{-1}n)).
 \tag{11.31}
\]
The change of variables supplies the modulus; the generator formulation gives the inverse action, covariance and isometry. The continuity of \(m\) is the scalar test-function argument of Proposition 5.5 in Lesson 1. Near the identity of \(H\), the transformed support of a compact core stays in a common compact set; uniform continuity there and the Haar change of variables give group \(L^1\)-continuity, hence crossed-product norm continuity. Density completes the assertion.

**Proposition 11.4.** There is a natural full crossed-product isomorphism
\[
 (A\rtimes N)\rtimes_\beta H\cong A\rtimes_\alpha(N\rtimes H).
 \tag{11.32}
\]

**Proof.** A covariant representation on the left consists of \((\pi,U_N)\) and \(U_H\), with
\[
 U_H(h)U_N(n)U_H(h)^*=U_N(\vartheta_h n).
\]
Then \(U(n,h)=U_N(n)U_H(h)\) is a continuous representation of the semidirect product and is covariant for \(\pi,\alpha\). Conversely restrict such a pair to \(N\) and \(H\). These operations are inverse, and the integrated universal maps are inverse on dense products of coefficient and group kernels.

The left Haar measure on \(G\) is \(m(h)^{-1}dn\,dh\): left multiplication by \((n_0,h_0)\) changes \(dn\) by \(m(h_0)\), \(dh\) by no factor, and \(m(h)\) by \(m(h_0)\), so the factors cancel. Thus a separated iterated kernel corresponds in group coordinates to \(m(h)f(h)(n)\); this factor matches the two integrated formulas. The representation bijection therefore respects both full completions. ∎

Every nontrivial simply connected solvable Lie group has a closed simply connected normal subgroup of codimension one and a splitting by \(\mathbb R\). Here is the group argument. If \(\mathfrak g\ne0\) is solvable, \([\mathfrak g,\mathfrak g]\ne\mathfrak g\), since otherwise its derived series could never reach zero. Choose a nonzero linear functional \(\ell\) vanishing on that commutator. The associated left-invariant one-form is closed: on left-invariant vector fields its differential is \(-\ell([X,Y])=0\). On the simply connected group, integrate the form along a path from the identity; path independence follows by integrating its zero differential over a homotopy of paths. Left invariance makes the resulting smooth map \(p:G\to\mathbb R\) additive under group multiplication.

Choose \(X\) with \(\ell(X)=1\). Then \(p(\exp(tX))=t\), so \(p\) is onto and has the one-parameter subgroup section \(\sigma(t)=\exp(tX)\). Its kernel \(N\) is closed and is a codimension-one Lie subgroup, since \(p\) is a submersion. The mutually inverse smooth maps
\[
 (n,t)\longmapsto n\sigma(t),\qquad
 g\longmapsto\bigl(g\sigma(-p(g)),p(g)\bigr)
 \tag{11.33}
\]
identify \(G=N\rtimes\mathbb R\). They also identify its underlying space with \(N\times\mathbb R\); connectedness and simple connectedness of \(G\) imply those of \(N\). Its Lie algebra is an ideal of the solvable algebra, hence solvable. Repeat this argument until the kernel is trivial.

Proposition 11.4 and one real Thom isomorphism at each step consequently prove, for any coefficient algebra \(A\),
\[
 K_i(A\rtimes G)\cong K_{i+\dim G}(A)
 \tag{11.34}
\]
for every simply connected solvable Lie group \(G\). Choices of the splitting chain and orientations specify the isomorphism. This is a K-theory assertion; for separable \(A\), the stronger KK-equivalence is [Blackadar 1998]. The real-action theorem here was proved without importing that stronger statement.

## Applications

For an irrational \(\eta\), let \(\mathbb R\) act on \(\mathbb T^2\) by the flow
\(t\cdot(x,y)=(x+t,y+\eta t)\) modulo integers. The action on functions is pullback by the inverse flow. Theorem 11.3 gives
\[
 K_0(C(\mathbb T^2)\rtimes\mathbb R)=\mathbb Z^2,\qquad
 K_1(C(\mathbb T^2)\rtimes\mathbb R)=\mathbb Z^2.
 \tag{11.35}
\]
To compute the coefficient groups, evaluation in the second circle coordinate has a constant-function splitting, with kernel \(SC(\mathbb T)\). Hence
\(K_i(C(\mathbb T^2))\cong K_i(C(\mathbb T))\oplus K_{i+1}(C(\mathbb T))\).
Evaluation in the first circle gives \(K_0(C(\mathbb T))=\mathbb Z\) and \(K_1(C(\mathbb T))=\mathbb Z\) by the same split extension and Bott periodicity. This proves the two ranks in (11.35), without a Künneth assumption. Irrationality describes the orbit geometry; the calculation also applies to rational flow velocities.

The connected affine group consists of pairs \((b,a)\), \(b\in\mathbb R\), \(a>0\), with product
\((b,a)(b',a')=(b+ab',aa')\). Its manifold is \(\mathbb R^2\), and its Lie algebra is solvable. For the trivial coefficient \(\mathbb C\), (11.34) therefore gives
\[
 K_0(C^*(G))=\mathbb Z,\qquad K_1(C^*(G))=0.
 \tag{11.36}
\]
More generally, a simply connected solvable group of dimension \(d\) has \(K_i(C^*(G))=\mathbb Z\) when \(i\equiv d\pmod2\), and zero in the other parity.

There is also a route from this theorem to the Pimsner–Voiculescu sequence. Let \(\theta\in\operatorname{Aut}(A)\), and use the induced-algebra convention of Lesson 7. Its mapping torus is
\[
 M=\{f\in C([0,1],A):f(1)=\theta^{-1}(f(0))\}.
 \tag{11.37}
\]
Green imprimitivity identifies \(A\rtimes_\theta\mathbb Z\) up to Morita equivalence with \(M\rtimes\mathbb R\). We compute the coefficient extension's boundary before changing its K-group identifications.

The path-algebra extension
\(0\to C_0((0,1),A)\to C([0,1],A)\to A\oplus A\to0\)
has boundary, in the positive suspension identifications of Lesson 10, equal to endpoint one minus endpoint zero. For \(K_0\), the lifts \(rp\) and \((1-r)p\) of a projection at the two endpoints give the positive and negative exponential loops. Differences of projections and unitization cover all classes. For \(K_1\), the doubled lift for \((1,u)\) is a path from \(1\) to \(\operatorname{diag}(u,u^{-1})\), giving \(\theta_A[u]\); reversing the path gives its negative for \((u,1)\). Additivity covers both endpoint groups. This proves the boundary formula in either parity.

The torus extension is the pullback along \(a\mapsto(a,\theta^{-1}(a))\). Boundary naturality therefore gives \(\theta_*^{-1}-1\) after the ordinary suspension identification. Multiplying its target coefficient group by \(\theta_*\) changes this endomorphism to \(1-\theta_*\). The Thom parity change and Green Morita equivalence convert its cyclic sequence to
\[
 \begin{gathered}
 K_0(A)\xrightarrow{1-\theta_*}K_0(A)\longrightarrow
 K_0(A\rtimes_\theta\mathbb Z)\longrightarrow K_1(A),\\
 K_1(A)\xrightarrow{1-\theta_*}K_1(A)\longrightarrow
 K_1(A\rtimes_\theta\mathbb Z)\longrightarrow K_0(A).
 \end{gathered}
 \tag{11.38}
\]
The arrows are transported from this mapping-torus sequence with the indicated coefficient identifications. For separable coefficient algebras, the required Morita K-isomorphisms are proved in the written programme lesson *Morita invariance of K-theory and maps induced by correspondences*, Corollary 2.2 and Theorem 5.1. Its sigma-unital hypotheses hold for the separable algebras and linking algebras used here. For general \(A\), use directed separable \(\theta\)-invariant subalgebras and continuity of K-theory: a countable coefficient set generates such a subalgebra after adjoining all its integer translates, and these subalgebras have dense union. The coefficient inclusions commute with the four Green module formulas of Lesson 7, and with the Thom maps by (11.22), so the transported sequences are compatible. Full crossed products here equal reduced ones, so the inclusions and dense direct limits identify the resulting sequence with that for \(A\).

The directed-continuity step follows directly from the finite-matrix definitions. A projection over the limit is close to a self-adjoint matrix at one stage; spectral cutoff gives a stage projection with the same class. A unitary is close to a stage matrix, whose polar part gives the same class. Every homotopy has compact parameter range, so finitely many approximations and one common upper stage give a piecewise-linear approximation to the whole path. Projection cutoff or polar decomposition repairs it; close-endpoint paths retain the prescribed endpoints. Thus classes and every stable homotopy relation occur at a finite stage, proving continuity in both degrees. The estimates and scalar normalization are those of the written lessons *Matrix stability, stability and continuity of \(K_0\)*, §2, and *Invertibles, unitaries and \(K_1\)*, §4; the finite common-stage argument also works for a directed set, without a sequence. Exactness passes to this limit because any element and any equality needed to test a kernel occur at a common finite stage.

The coefficient-to-crossed-product arrows in the PV presentation are induced by the canonical inclusion \(A\to A\rtimes_\theta\mathbb Z\). The written programme lesson *The Pimsner–Voiculescu exact sequence*, Lemma 2.1 and equation (2.9), proves the required identification using a Fourier window, positive interval suspensions and the normalization \(\Phi=-T\) from (11.26). We use those compatible middle-group identifications in (11.38). That proof depends on this course's period-one theorem, Takai duality, and Theorem 11.3 with equations (11.22)–(11.26); it does not depend on the PV application in the present section. This is an acyclic dependency. Rosenberg, §2.5, p. 108, records the classical PV presentation.

## Exercises with complete solutions

**Exercise 1 (basic).** Verify both identities in (11.3).

**Solution.** For positive \(t,r\), integration over \(v>\max(t,r)\) gives the kernel of \(F_\varepsilon^*F_\varepsilon\) as
\(\varepsilon^{-1}e^{-|t-r|/(2\varepsilon)}\).
Integration over \(0<v<\min(t,r)\) gives the kernel of \(F_\varepsilon F_\varepsilon^*\) as
\(\varepsilon^{-1}(e^{-|t-r|/(2\varepsilon)}-e^{-(t+r)/(2\varepsilon)})\).
The sum \(F_\varepsilon+F_\varepsilon^*\) has the first of these kernels, off the measure-zero diagonal. Expanding \((1-F_\varepsilon)^*(1-F_\varepsilon)\) yields \(1\), and expanding in the reverse order yields \(1-E_\varepsilon\). On the negative half-line \(F_\varepsilon\) vanishes, so \(S_\varepsilon\) is the identity. The norm-completion argument of Lesson 10 makes these operator equalities equalities in the scalar Wiener–Hopf unitization; the coefficient map transfers them to (11.3).

**Exercise 2 (intermediate).** Prove the convergence of \(I_\varepsilon(a)\) with an explicit bound.

**Solution.** Split the integral at \(\sqrt\varepsilon\). The first exponential mass is at most two, and \(\|a-\alpha_{-s}(a)\|\le2\|a\|\) controls the tail. Thus
\[
 I_\varepsilon(a)\le
 2\sup_{0\le s\le\sqrt\varepsilon}\|a-\alpha_{-s}(a)\|
       +4\|a\|e^{-1/(2\sqrt\varepsilon)}.
 \tag{11.39}
\]
Point-norm continuity makes the first term tend to zero, and the exponential makes the second tend to zero. No differentiability assumption is needed.

**Exercise 3 (intermediate).** Determine the trivial-action signs relative to the positive Bott maps. Why does the scalar index calculation settle only one parity?

**Solution.** The Cayley loop of positive winding has boundary \(-[1]\), so \(T_{\mathrm{triv}}^0=-\beta_A\), first on projection classes and then on all \(K_0\) by unitization. The other scalar K-groups are zero and reveal no parity-one sign. Use the suspended-index definition (11.24) and swap the two odd factors as in (11.25). The swap contributes \(-1\), and the suspended scalar index contributes a second \(-1\). They cancel before the outer minus in (11.24), giving \(\partial_0^{\mathrm{triv}}\theta_A=-\operatorname{id}\) and \(T_{\mathrm{triv}}^1=-\theta_A\). Therefore the suspension-compatible family is \(\Gamma^i=(-1)^{i+1}T^i\), while the index-normalized \(\Phi^i=(-1)^i\Gamma^i\) equals both ordinary positive Bott maps at the trivial action. A geometric cotangent orientation would require its own comparison.

**Exercise 4 (advanced).** Iterate two real directions in order \(e_2,e_1\), and compare the inverse-boundary and index-normalized constructions with the ordered Bott map.

**Solution.** The first step takes \(K_i(A)\) to \(K_{i+1}(A\rtimes\mathbb R e_2)\); the second takes this to \(K_i(A\rtimes\mathbb R^2)\). The universal covariant-pair argument identifies the iterated algebra with the full two-dimensional crossed product. The target frequency order is \((u_1,u_2)\). The two factors converting \(T\) to \(\Phi\) multiply to
\((-1)(-1)=+1\), so \(\Phi^{(2),i}=T^{(2),i}\).
For the trivial action \(\Phi^{(2),i}=\Theta_A^{2,i}\), hence \(T^{(2),i}=\Theta_A^{2,i}\). Converting the two \(T\)-steps to \(\Gamma\) contributes \((-1)^{i+1}(-1)^{i+2}=-1\); hence \(\Gamma^{(2),i}=-\Theta_A^{2,i}\). These are the signs in §7 of *Frequency calculus for an action of Euclidean space*. Reversing the two coordinate directions reverses the positive planar Bott orientation, and the rescaled-action naturality argument above transfers that rule to arbitrary actions.

## What this lesson does not prove

The general K-theory foundations of Lesson 10 are reused. The ordinary Bott maps and the planar orientation use the written programme suspension and Bott lessons identified above and in Lesson 10. The exact interchange rule is proved above by a circle-unitary reduction; the arbitrary directed-continuity step is proved in the PV application. The formulas use these general tools to compute the two Thom signs; they do not import the Connes–Thom theorem.

The stronger KK-version of the theorem and its equivariant refinements are not proved here. The PV application uses the exact written Morita and Fourier-window proof providers identified above; its endpoint boundary and parity argument are proved here. The geometric cotangent Thom class and analytic index orientation require additional geometric data. Lesson 12 develops the projection and cocycle construction of the real Thom map.

## References

[Blackadar 1998] Bruce Blackadar, *K-Theory for Operator Algebras*, second edition. The Wiener–Hopf proof is §10.9, Lemmas 10.9.3–10.9.8 and the nonunital argument, pp. 80–83. Ordinary products are §§14.4, 18.9–18.10 and 19.2.5. The stronger solvable-group statement is Corollary 19.3.9, p. 193. [Author's second edition](https://www.bruceblackadar.com/Mathematics/book6.pdf).

[Connes 1994] Alain Connes, *Noncommutative Geometry*, Chapter II, Appendix C, Theorem 8 and the following solvable-group remark. In the [author's electronic edition](https://alainconnes.org/wp-content/uploads/book94bigpdf.pdf), these are on p. 179. The present proof uses the Wiener–Hopf extension rather than that theorem as a prerequisite.

[Rosenberg 2012] Jonathan Rosenberg, *Examples and applications of noncommutative geometry and K-theory*, in *Topics in Noncommutative Geometry*, Clay Mathematics Proceedings 16, 2012, §§2.4–2.5, pp. 106–108; general Morita and K-theory framework in §§1.1–1.3, pp. 94–99. [Electronic volume](https://www.claymath.org/wp-content/uploads/2022/03/cmip016c.pdf).

[Frequency calculus] *Frequency calculus for an action of Euclidean space*, in *Cyclic cohomology, connections and transverse geometry*, §7: the positive Bott maps, the suspension-compatible \(\Gamma\), and the index-normalized \(\Phi\).

The six-term exact sequence and the exponential map K-theory for operator algebras, Lesson 11, Theorem 1.1, including the positive-exponential suspension comparison.
