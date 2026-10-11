# Opposite dual circles and irrational tensor products

Two discrete modular crossings have two dual circle actions. Crossing their tensor product by opposite motion in those circles produces the diagonal modular crossing, together with a full algebra of operators on a countable Hilbert space. We construct the normal isomorphism explicitly before absorbing that operator factor in type III.

A second consequence of the tensor flow theorem concerns irrational parameters: the tensor product of factors of types IIIλ and IIIμ is type III₁ when the logarithms of λ and μ have irrational ratio. Approximate finite dimensionality passes to that product. This supplies a proof of the tensor-product assertion left as an exercise in the source.

## 1. Statements, conventions and exact inputs

Let \(M_j\) be a type III₁ factor with a faithful normal state \(\varphi_j\), for \(j=1,2\), and fix \(T>0\). Set

\[
 \alpha_j=\sigma_T^{\varphi_j},\qquad
 N_j=M_j\rtimes_{\alpha_j}\mathbb Z,
 \qquad \lambda=e^{-2\pi/T}.
 \tag{1}
\]

Write \(V_j\) for the discrete implementing unitary. Our negative-character dual action is

\[
 \theta^j_z(x)=x\quad(x\in M_j),
 \qquad \theta^j_z(V_j)=\overline z V_j
 \quad(z\in\mathbb T).
 \tag{2}
\]

The circle has probability Haar measure. Define

\[
 R=N_1\bar\otimes N_2,\qquad
 \delta_z=\theta^1_z\bar\otimes\theta^2_{z^{-1}},
 \qquad Q=R\rtimes_\delta\mathbb T.
 \tag{3}
\]


**Theorem 1.1.** The algebra \(Q\) is a factor of type \(\mathrm{III}_\lambda\). More precisely, let

\[
 M=M_1\bar\otimes M_2,
 \qquad D=M\rtimes_{\alpha_1\otimes\alpha_2}\mathbb Z.
 \tag{4}
\]

There is a normal isomorphism with normal inverse

\[
 Q\cong D\bar\otimes B(\ell^2(\mathbb Z)).
 \tag{5}
\]

Since \(D\) is type \(\mathrm{III}_\lambda\), a separately specified absorption isomorphism gives \(Q\cong D\). Neither the theorem nor its construction requires separable predual or approximate finite dimensionality. The faithful normal states in (1) are retained as hypotheses.

**Theorem 1.2.** Let \(F_\lambda,F_\mu\) be factors of types \(\mathrm{III}_\lambda,\mathrm{III}_\mu\), where \(0<\lambda,\mu<1\). If \(\log\lambda/\log\mu\) is irrational, then

\[
 F_\lambda\bar\otimes F_\mu
 \quad\text{is a factor of type III₁.}
 \tag{6}
\]

If both factors are approximately finite-dimensional, so is their tensor product. This statement allows arbitrary preduals and does not require faithful normal states.

We use these earlier written proofs.

- Discrete modular crossings, MD01–MD05 proves that the discrete modular crossing of a type III₁ factor with a faithful normal state has type \(\mathrm{III}_{e^{-2\pi/T}}\).
- Tensor products and the normalized flow of weights, TF Section 1, especially TF5–TF7, proves the product-weight modular formula, normal spatial tensor maps, and tensor factoriality. Its Sections 2–4 prove the full normal core embedding and the exact fixed-centre flow formula TF3. Those proofs use the complete tensor Tomita domains, rather than only an algebraic product of modular operators.
- The positive tensor-spectrum bound, TP Section 7 proves the all-faithful-weight bound used in Section 2 below, at arbitrary predual size.
- Normal regular crossed products, NR3–NR4 supplies their faithful normal representations and normal representation independence. Circle Fourier analysis, CC0 proves the onto vector-valued Fourier map and character orthogonality with probability Haar measure.
- Continuous decompositions, CDEC Sections 1–2 constructs absorption of a countably infinite scalar operator factor when the unit is properly infinite, with an explicit normal inverse. It proves that the unit of every nonzero type III algebra is properly infinite.
- L18 Section 6 constructs a faithful normal semifinite trace from a nonzero finite projection in a factor. MIV2.h and the dual-centre kernel theorem K43 identify the positive all-weight modular intersection with the exponential of the core-centre flow kernel, for every factor.

The source statements are Takesaki, *Theory of Operator Algebras III*, XVIII.4, Lemma 4.17(ii) and Theorem 4.16(ii), printed pages 389–390. The construction below retains the operator tensor factor and proves when it can be removed.

## 2. The positive spectrum of a tensor factor

For a nonzero factor \(A\), write

\[
 S_+(A)=\left(\bigcap_{\omega\text{ faithful normal semifinite}}
                    \operatorname{Sp}\Delta_\omega\right)
                      \cap(0,\infty).
 \tag{7}
\]

The exact bound from TP7 is

\[
 \overline{S_+(A)S_+(B)}^{\,(0,\infty)}
           \subseteq S_+(A\bar\otimes B).
 \tag{8}
\]

Here the bar is closure relative to the positive half-line, and the set before closure consists of all products of one element from each invariant.

Recall its proof to make clear what is being intersected. Let \(Z_A,Z_B\) be the two core centres, with flows \(\eta^A,\eta^B\) and period kernels \(K_A,K_B\). TF3 identifies the product core centre with

\[
 Z=(Z_A\bar\otimes Z_B)^{\eta^A_s\otimes\eta^B_{-s}},
 \tag{9}
\]

where invariance is required for every \(s\in\mathbb R\). On this entire algebra the two residual actions agree:

\[
 \Theta_t=(\eta^A_t\otimes\mathrm{id})|_Z
          =(\mathrm{id}\otimes\eta^B_t)|_Z.
 \tag{10}
\]

Thus every element of \(K_A\), and every element of \(K_B\), belongs to \(\ker\Theta\). This kernel is a closed subgroup: each equation \(\Theta_t(z)=z\) is closed under limits, by point-ultraweak continuity and separation by normal functionals. Hence

\[
 \overline{K_A+K_B}\subseteq\ker\Theta.
 \tag{11}
\]

Tensor factoriality is TF7. For the two factors and their product, MIV2.h and K43 give \(S_+=\exp K\). The exponential is a homeomorphism from \(\mathbb R\) onto \((0,\infty)\) and turns sums into products. This proves (8).

In particular, if \(A\) is type III₁, then \(S_+(A)=(0,\infty)\). The exponential description also gives \(1\in S_+(B)\). Formula (8) therefore forces

\[
 S_+(A\bar\otimes B)=(0,\infty).
 \tag{12}
\]

Each modular spectrum is closed and contains positive numbers tending to zero, so the full intersection is \([0,\infty)\). If this factor had a nonzero finite projection, L18 Section 6 would give a faithful normal semifinite trace, whose modular spectrum is \(\{1\}\). That contradicts (12). Thus

\[
 A\text{ type III₁},\quad B\ne0\text{ a factor}
 \quad\Longrightarrow\quad
 A\bar\otimes B\text{ type III₁}.
 \tag{13}
\]

The argument uses the full all-weight intersection. It does not identify that intersection with the spectrum of one arbitrarily chosen state.

## 3. The regular circle crossing

For the construction (5), initially let \(M_j\) be arbitrary nonzero algebras with faithful normal states \(\varphi_j\), and keep \(\alpha_j=\sigma_T^{\varphi_j}\). No type hypothesis is used until Section 6. Work in their faithful state GNS spaces \(H_j\), and put \(H=H_1\otimes H_2\). On \(M=M_1\bar\otimes M_2\), set

\[
 a=\alpha_1\otimes\mathrm{id},\qquad
 b=\mathrm{id}\otimes\alpha_2,\qquad
 \gamma=ab,
 \qquad A=\Delta_{\varphi_1}^{iT}\otimes I_{H_2}.
 \tag{14}
\]

The bounded unitary \(A\) implements \(a\), and \(a,b\) commute.

Regroup the tensor product of the two discrete regular representations on \(\ell^2(\mathbb Z^2,H)\). The coefficient of \(x\in M\), and the two shifts \(U=V_1\otimes1\), \(V=1\otimes V_2\), are

\[
 \begin{aligned}
 [x\xi](m,n)&=a^{-m}b^{-n}(x)\xi(m,n),\\
 [U\xi](m,n)&=\xi(m-1,n),\\
 [V\xi](m,n)&=\xi(m,n-1).
 \end{aligned}
 \tag{15}
\]

The coefficient map on all of \(M\) is the normal tensor of the two faithful regular coefficient maps. These coefficients and the two shifts generate exactly \(R\), by normality and the generating description of each tensor factor.

The dual circle action fixes these coefficients and satisfies

\[
 \delta_z(U)=\overline z U,\qquad \delta_z(V)=zV.
 \tag{16}
\]

It is implemented in (15) by multiplication by \(\overline z^{\,m}z^n\). This unitary group is strongly continuous on finite-coordinate vectors, hence on the whole Hilbert space by density and its uniform bound. Thus the action is continuous and its regular circle crossing is well-defined.

The regular Hilbert space of \(Q\) is
\(L^2(\mathbb T_z,h;\ell^2(\mathbb Z^2,H))\).
The coefficient at \(z\) applies \(\delta_{z^{-1}}\); let \(K_w\) denote translation by \(w\in\mathbb T\). Its full generating operators are

\[
 \begin{aligned}
 [x f](z,m,n)&=a^{-m}b^{-n}(x)f(z,m,n),\\
 [U f](z,m,n)&=z f(z,m-1,n),\\
 [V f](z,m,n)&=\overline z f(z,m,n-1),\\
 [K_w f](z,m,n)&=f(w^{-1}z,m,n).
 \end{aligned}
 \tag{17}
\]

For example conjugation by \(K_w\) multiplies the second line by \(\overline w\), exactly as required by (16). This fixes the sign before taking a Fourier transform.

## 4. Fourier coefficients and a lattice coordinate

Expand the circle variable in its complete orthonormal basis \(z^k\), as proved in CC0. The Fourier map is onto

\[
 L^2(\mathbb T;\ell^2(\mathbb Z^2,H))
       \longrightarrow\ell^2(\mathbb Z^3,H),
 \qquad f\longmapsto\widehat f(k,m,n).
 \tag{18}
\]

Completeness for the vector-valued space follows by approximating finite simple tensors, so no separability of \(H\) is needed. In these coordinates (17) becomes

\[
 \begin{aligned}
 [x\eta](k,m,n)&=a^{-m}b^{-n}(x)\eta(k,m,n),\\
 [U\eta](k,m,n)&=\eta(k-1,m-1,n),\\
 [V\eta](k,m,n)&=\eta(k+1,m,n-1),\\
 [K_w\eta](k,m,n)&=w^{-k}\eta(k,m,n).
 \end{aligned}
 \tag{19}
\]

The combination \(c=k-m+n\) is unchanged by both shifts. Introduce the integer coordinates

\[
 q=k,\qquad l=n,\qquad c=k-m+n;
 \qquad (k,m,n)=(q,q+l-c,l).
 \tag{20}
\]

They give a bijection of \(\mathbb Z^3\). The coordinate permutation followed by the unitary correction

\[
 [\mathcal W\eta](q,l,c)
       =A^{-c}\eta(q,q+l-c,l)
 \tag{21}
\]

is consequently an onto unitary. Its inverse is

\[
 [\mathcal W^*\zeta](k,m,n)
       =A^{k-m+n}\zeta(k,n,k-m+n).
 \tag{22}
\]

Each formula preserves the sum of squared coordinate norms, and substitution shows that they are inverse.

Conjugation by \(A^{-c}\) removes the surviving \(a^c\) from the coefficient in (19):

\[
 a^{-c}a^{-(q+l-c)}b^{-l}(x)
       =a^{-q}\gamma^{-l}(x).
 \tag{23}
\]

Since the two shifts leave \(c\) unchanged, they acquire no additional operator factor. Let \(\mathcal U\) be (21) composed with the Fourier map. We obtain

\[
 \begin{aligned}
 [\mathcal Ux\mathcal U^*\zeta](q,l,c)
       &=a^{-q}\gamma^{-l}(x)\zeta(q,l,c),\\
 [\mathcal UU\mathcal U^*\zeta](q,l,c)
       &=\zeta(q-1,l,c),\\
 [\mathcal UV\mathcal U^*\zeta](q,l,c)
       &=\zeta(q+1,l-1,c),\\
 [\mathcal UK_w\mathcal U^*\zeta](q,l,c)
       &=w^{-q}\zeta(q,l,c).
 \end{aligned}
 \tag{24}
\]

All coefficients are now independent of \(c\); the last coordinate is a representation multiplicity.

The shifts can also be checked on basis positions, with the coefficient vector suppressed:

| Generator | Change of \((k,m,n)\) | Change of \((q,l,c)\) |
| --- | --- | --- |
| \(U\) | \((1,1,0)\) | \((1,0,0)\) |
| \(V\) | \((-1,0,1)\) | \((-1,1,0)\) |
| \(UV\) | \((0,1,1)\) | \((0,1,0)\) |

These are changes of positions of basis vectors; (19) and (24) are the corresponding inverse shifts on their coordinate functions.

## 5. Matrix units identify the whole image

Let \(H_D=\ell^2(\mathbb Z_l,H)\). The regular diagonal crossing \(D=M\rtimes_\gamma\mathbb Z\) is generated on this space by

\[
 [i(x)\xi](l)=\gamma^{-l}(x)\xi(l),
 \qquad [v\xi](l)=\xi(l-1).
 \tag{25}
\]

The constant unitary \(A\) on \(H_D\) normalizes \(D\), because \(a\) commutes with \(\gamma\). It defines an automorphism \(\kappa\) with

\[
 \kappa(i(x))=i(a(x)),\qquad \kappa(v)=v.
 \tag{26}
\]

Ignoring for a moment the constant \(c\)-multiplicity, (24) acts on \(H_D\otimes\ell^2(\mathbb Z_q)\) as

\[
 \begin{aligned}
 x&\longmapsto\operatorname{diag}_{q\in\mathbb Z}
                    \bigl(\kappa^{-q}(i(x))\bigr),\\
 U&\longmapsto1\otimes S,\\
 UV&\longmapsto v\otimes1,\\
 K_w&\longmapsto1\otimes D_w,
       \qquad D_w\delta_q=w^{-q}\delta_q.
 \end{aligned}
 \tag{27}
\]

The diagonal in the first line is bounded by \(\|x\|\). It belongs to \(D\bar\otimes B(\ell^2(\mathbb Z))\): every finite coordinate compression has entries in \(D\), and these uniformly bounded compressions converge strongly* to the diagonal. The other displayed generators also belong to that tensor algebra, as does \(V=U^{-1}(UV)\).

For the reverse inclusion, character orthogonality gives the coordinate projections

\[
 p_j=\int_{\mathbb T}w^jD_w\,dh(w)
      =|\delta_j\rangle\langle\delta_j|.
 \tag{28}
\]

The integral is a bounded strong integral, since \(w\mapsto D_w\xi\) is continuous for every vector \(\xi\). Finite Riemann sums, or scalar coefficient integration followed by vector approximation, place it in the generated von Neumann algebra. The shift therefore supplies every matrix unit:

\[
 S^i p_0 S^{-j}=E_{ij}.
 \tag{29}
\]

Compressing the first line of (27) at \(q=0\) gives \(i(x)\otimes E_{00}\). Compressing \(v\otimes1\) gives \(v\otimes E_{00}\). Since these generate \(D\) in the first variable, the image contains the full corner \(D\otimes E_{00}\). Conjugating and multiplying by the matrix units gives

\[
 d\otimes E_{ij}
 =(1\otimes E_{i0})(d\otimes E_{00})(1\otimes E_{0j})
 \tag{30}
\]

for every \(d\in D\) and every \(i,j\).

If \(X\in D\bar\otimes B(\ell^2(\mathbb Z))\), its finite coordinate compressions are finite sums of elements (30), and converge strongly* to \(X\) with norm bounded by \(\|X\|\). Indeed \(P_F=1\otimes\sum_{j\in F}E_{jj}\) increases strongly to \(1\), and

\[
 \|(P_FXP_F-X)\xi\|
 \le\|X\|\|(P_F-1)\xi\|+\|(P_F-1)X\xi\|
 \longrightarrow0,
 \tag{31}
\]

with the same argument for \(X^*\). Thus every element of the tensor algebra belongs to the generated image. Restoring the last coordinate, we have proved the equality of full algebras

\[
 \mathcal UQ\mathcal U^*
 =\bigl(D\bar\otimes B(\ell^2(\mathbb Z_q))\bigr)
                                  \otimes1_{\ell^2(\mathbb Z_c)}.
 \tag{32}
\]


Here are the normal maps underlying (5). Let \(J_0\eta=\eta\otimes\delta_0\) include the first two factors at \(c=0\). Then

\[
 \Phi(Y)=J_0^*\mathcal UY\mathcal U^*J_0,
 \qquad
 \Phi^{-1}(X)=\mathcal U^*(X\otimes1)\mathcal U.
 \tag{33}
\]

Equation (32) shows that they are inverse unital star maps on their entire stated domains. Compression is multiplicative on this range because every operator there is a constant amplification. Unitary conjugation and compression are normal. Amplification is normal as well: a vector-series functional pulls back to the sum of its coordinate vector-series functionals, with square-summable tails and hence convergence in predual norm. This proves normality in both directions. No cancellation of a Hilbert multiplicity, or extension from only formal generators, is left implicit.

## 6. Apply the construction in type III₁

Return to the hypotheses of Theorem 1.1. By (13), \(M=M_1\bar\otimes M_2\) is a type III₁ factor. The product-weight theorem TF5 gives a faithful normal state \(\varphi=\varphi_1\otimes\varphi_2\) and the exact modular formula

\[
 \sigma_t^\varphi
       =\sigma_t^{\varphi_1}\bar\otimes\sigma_t^{\varphi_2}.
 \tag{34}
\]

Its value at the identity is \(1\), since both factors are states. At time \(T\), (34) is \(\gamma=\alpha_1\otimes\alpha_2\). Thus MD05 applies to (4) and proves that \(D\) has type \(\mathrm{III}_\lambda\).

CDEC Sections 1–2 now gives \(D\bar\otimes B(\ell^2(\mathbb Z))\cong D\). To retain the mechanism, enumerate the integer basis by \(\mathbb N_0\) and choose the filling isometries furnished by that theorem:

\[
 s_i^*s_j=\delta_{ij}1,
 \qquad \sum_i s_is_i^*=1\quad\text{strongly}.
 \tag{35}
\]

The map on finite matrices is

\[
 \sum_{i,j}d_{ij}\otimes E_{ij}
       \longmapsto\sum_{i,j}s_i d_{ij}s_j^*.
 \tag{36}
\]

It is conjugation by the onto unitary
\(\eta\otimes\delta_i\mapsto s_i\eta\).
The inverse has matrix entries \(s_i^*d s_j\). CDEC proves that the bounded finite compressions converge to these full operators in the tensor algebra and in \(D\), and that both maps are normal. Countability concerns only the scalar operator factor, not a basis of a representation of \(D\).

Composing (33) with (36) gives the asserted normal isomorphism \(Q\cong D\). Algebra isomorphisms preserve the type III condition because they transport projections, partial isometries and their defining equations. They also preserve \(S\): pulling back any faithful normal semifinite weight transports its entire GNS involution and modular operator by an onto GNS unitary, and gives a bijection of all weights in the defining intersection. Consequently \(Q\) is a factor of type \(\mathrm{III}_\lambda\), proving Theorem 1.1.

The absorption map uses the chosen family \((s_i)\). It does not say that the natural coefficient embeddings in the two crossings coincide. The generator formulas before absorption are exactly (27).

## 7. Irrational logarithms and finite-dimensional approximation

Let \(F_\lambda,F_\mu\) satisfy Theorem 1.2, and put

\[
 a_0=-\log\lambda>0,\qquad b_0=-\log\mu>0.
\]

The defining subtypes give

\[
 S_+(F_\lambda)=\exp(a_0\mathbb Z),
 \qquad S_+(F_\mu)=\exp(b_0\mathbb Z).
 \tag{37}
\]

Their product therefore contains the exponential of
\(G=a_0\mathbb Z+b_0\mathbb Z\).
We prove directly that this additive subgroup is dense when \(r=a_0/b_0\) is irrational.

For an integer \(N\ge1\), place the \(N+1\) fractional parts of \(0,r,2r,\ldots,Nr\) in the \(N\) half-open intervals of length \(1/N\) in \([0,1)\). Two occupy the same interval. Their difference is nonzero, since equality would make \(r\) rational. Thus some integers \(j,m\), with \(j\ne0\), satisfy

\[
 0<|jr-m|<1/N.
\]

It follows that

\[
 d_N=|j a_0-m b_0|\in G,
 \qquad 0<d_N<b_0/N.
 \tag{38}
\]

The absolute value remains in \(G\) because \(G\) is a group. For any \(x\in\mathbb R\), let \(k_N=\lfloor x/d_N\rfloor\). Then

\[
 k_Nd_N\in G,
 \qquad 0\le x-k_Nd_N<d_N\longrightarrow0.
 \tag{39}
\]

This also holds for negative \(x\). Thus \(\overline G=\mathbb R\), and the exponential homeomorphism gives

\[
 \overline{\lambda^{\mathbb Z}\mu^{\mathbb Z}}^{\,(0,\infty)}
       =(0,\infty).
 \tag{40}
\]

Formula (8) proves that the tensor factor has this entire positive modular invariant. Closedness adds zero to every spectrum. The finite-projection trace contradiction from Section 2 excludes every nonzero finite projection. Hence the tensor factor is type III₁, proving (6).

For the approximation assertion, use the following definition: a von Neumann algebra is approximately finite-dimensional if an increasing directed family of finite-dimensional unital star subalgebras generates it. Let \((A_i)\) and \((B_j)\) be such families for \(F_\lambda\) and \(F_\mu\). Then

\[
 C_{i,j}=A_i\otimes B_j
 \tag{41}
\]

is a finite-dimensional unital star subalgebra of their spatial tensor product. Its dimension is finite because it is spanned by the finitely many tensors from bases of \(A_i,B_j\). The product of the two directed index sets is directed, and the family (41) is increasing.

Let \(C\) be the von Neumann algebra it generates. For each fixed \(j\), unitality gives \(A_i\otimes1\subset C_{i,j}\), for every \(i\). The normal coefficient embedding sends the ultraweak closure of \(\bigcup_iA_i\) into the ultraweakly closed algebra \(C\). Thus \(F_\lambda\otimes1\subset C\). The same reasoning gives \(1\otimes F_\mu\subset C\). These two commuting algebras generate the whole spatial tensor product, so \(C=F_\lambda\bar\otimes F_\mu\). This proves approximate finite dimensionality. If the input approximations are increasing sequences, the diagonal sequence \(A_n\otimes B_n\) has the same generating property.

This establishes the tensor-product assertion without presupposing uniqueness of the approximately finite-dimensional type III₁ factor. That uniqueness is a subsequent theorem.

## 8. Checks on the circle, the operator factor and irrationality

**Opposite characters select the diagonal.** From (16),

\[
 \delta_z(U^mV^n)=z^{n-m}U^mV^n.
 \tag{42}
\]

The degree is zero exactly when \(m=n\), so \(UV\) is the diagonal discrete translation in (27). Using the same character on both factors would instead make the zero-degree condition \(m=-n\); it would select a different discrete action. The sign in (3) is therefore essential to the stated diagonal modular construction.

**The operator factor cannot be discarded in general.** Take \(M_1=M_2=\mathbb C\), with their scalar states. Both modular actions are trivial. Then

\[
 R=L(\mathbb Z^2),\qquad D=L(\mathbb Z),
 \qquad Q\cong L(\mathbb Z)\bar\otimes B(\ell^2(\mathbb Z)).
 \tag{43}
\]

The first two algebras are abelian; the last is not, since it contains noncommuting matrix units. The dual fixed algebra of \(R\) is generated by \(UV\): the two-variable circle Fourier basis and its finite Fejér approximants retain exactly the diagonal powers in (42). It is therefore the abelian algebra \(L(\mathbb Z)\). Thus the fixed algebra and the full circle crossing are different here. The type III absorption hypothesis in Section 6 supplies the additional step needed in the theorem.

**A concrete irrational pair.** The ratio \(\log2/\log3\) is irrational. Otherwise it equals \(p/q\) for positive integers \(p,q\), giving \(2^q=3^p\), impossible because the left side is even and the right side is odd. Consequently any given factors of types III₁⁄₂ and III₁⁄₃ have type III₁ tensor product; if they are approximately finite-dimensional, so is that product. This calculation uses the factors as inputs and makes no separate existence assertion.

**The rational case is not a density argument.** If \(\lambda=\mu=1/2\), the subgroup in (38) is \((\log2)\mathbb Z\), which is not dense. Formula (8) then supplies only the lower bound \(2^{\mathbb Z}\) on the positive invariant. It does not by itself identify the complete subtype. Theorem 1.2 uses irrationality exactly in the passage from (38) to (40).
