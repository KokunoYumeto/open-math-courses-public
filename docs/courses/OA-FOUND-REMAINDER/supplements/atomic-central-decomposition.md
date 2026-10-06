# Central decomposition when the centre is atomic

*Original exposition: GPT-6.1 Sol (OpenAI), Ultra, October 2026. CC0 1.0 public-domain dedication. Classical operator-algebra results, with complete proofs at the stated hypotheses.*

The countable-field construction in the direct-integral lessons need not apply to a general nonseparable von Neumann algebra. There is nevertheless a complete decomposition for every algebra with atomic centre, with no cardinality or separability restriction. Its natural base is a possibly uncountable atomic measure space, and its fibres may be nonseparable.

## 1. The bounded product of factor corners

<a id="AC-DECOMPOSITION"></a>

**Theorem 1.1 (Atomic central decomposition).** Let \(M\subseteq B(H)\) be a von Neumann algebra containing \(I_H\), with no separability hypothesis, and suppose \(Z(M)\) is atomic: every nonzero central projection majorizes a nonzero minimal central projection. Let \((z_i)_{i\in I}\) be all its distinct nonzero minimal projections. Then
\[
H=\bigoplus_{i\in I}H_i,\qquad H_i=z_iH,
\]
and the restriction map is a normal *-isomorphism
\[
M\longrightarrow\prod_{i\in I}^{\ell^\infty}M_i,
\qquad M_i=(Mz_i)|_{H_i},\qquad
x\longmapsto(x|_{H_i})_{i\in I}.
\tag{A.1}
\]
Every nonzero \(M_i\) is a factor. The norm in (A.1) is \(\sup_i\|x|_{H_i}\|\). The centre corresponds to \(\ell^\infty(I)\), acting by one scalar on each \(H_i\). For the zero algebra, the index set is empty, and both the direct sum and product are zero.

**Proof.** Minimal projections in an abelian algebra are orthogonal when distinct: \(z_i z_j\) is a central projection below each, so any nonzero product forces \(z_i=z_j\). Let \(z=\bigvee_i z_i\), the strong limit of finite sums of these orthogonal projections. Such sums have norm at most one, and belong to \(Z(M)\); the complete bounded increasing-net proof, BK-04, keeps their supremum in that von Neumann algebra. If \(1-z\ne0\), atomicity supplies a minimal central projection below it, contradicting the definition of \((z_i)\). Thus \(z=1\). The orthogonal subspaces \(H_i\) therefore have dense algebraic sum, and \(H\) is their Hilbert direct sum.

Each \(H_i\) reduces every \(x\in M\) because \(z_i\) is central. Restriction is a unital *-homomorphism with norm at most \(\|x\|\). The direct-sum norm identity gives
\[
\|x\|=\sup_i\|x|_{H_i}\|.
\]
To prove surjectivity, let \((x_i)\) be a family with \(x_i\in Mz_i\) and \(C=\sup_i\|x_i\|<\infty\). Extend each operator by zero off \(H_i\). For finite \(F\subseteq I\), put \(x_F=\sum_{i\in F}x_i\in M\). These have norm at most \(C\). For \(\xi=\bigoplus_i\xi_i\), the series of nonnegative numbers \(\sum_i\|\xi_i\|^2\), defined as the supremum of its finite sums, is finite. Hence
\[
\|(x_G-x_F)\xi\|^2
\le C^2\sum_{i\in G\setminus F}\|\xi_i\|^2
\qquad(F\subseteq G)
\]
proves that the net \((x_F\xi)\) is Cauchy; the same finite-tail bound constructs the block operator \(x\) with \(x\xi=\bigoplus_i x_i\xi_i\). It is a strong limit of \((x_F)\), so \(x\in M\), and its restrictions are the prescribed \(x_i\). This also proves injectivity and (A.1).

The centre of the corner \(Mz_i\) is \(Z(M)z_i\). To verify the nontrivial inclusion, if \(a\in Mz_i\) commutes with \(Mz_i\), then for \(x\in M\) its products with \(x(1-z_i)\) vanish, and its products with \(xz_i\) commute by assumption; thus \(ax=xa\) and \(a\in Z(M)z_i\). Minimality of \(z_i\) in \(Z(M)\) implies \(Z(M)z_i=\mathbb Cz_i\): indeed, if \(a=a^*\) in this corner has two spectral values \(s_1<s_2\), choose \(t\in(s_1,s_2)\). The continuous calculus gives nonzero positive \((a-tz_i)_+\) and \((tz_i-a)_+\) with zero product. Their support projections are central, nonzero and orthogonal, by the full bounded support proof, BK-06. Either is a proper nonzero projection below \(z_i\), contradicting minimality. Therefore \(M_i\) is a factor.

For normality, a bounded increasing net \((x_\alpha)\) in \(M_+\) has strong limit its supremum. Restricting to a reducing subspace commutes with that limit, so every coordinate map preserves the supremum. Conversely, for a bounded increasing net of positive families in the product, the coordinate strong limits assemble to its supremum block operator. The finite-tail estimate, followed by convergence on the finitely many retained coordinates, shows strong convergence on \(H\). Thus (A.1) and its inverse preserve arbitrary bounded increasing suprema and are normal, by the complete positive-map criterion after Corollary 11.5. Finally, a block family is central exactly when each coordinate is central in its factor, giving \(\ell^\infty(I)\). \(\square\)

The finite-tail argument is valid for an uncountable index set: each Hilbert direct-sum vector has countable support, but the algebra and the index set may be uncountable. The algebra consists of all uniformly bounded families, so it is the \(\ell^\infty\) product rather than the algebraic or \(c_0\) sum.

## 2. Why a probability base need not exist

<a id="AC-NONSIGMAFINITE"></a>

**Example 2.1 (Uncountably many central atoms).** For uncountable \(I\), let \(M=\ell^\infty(I)\) on \(\ell^2(I)\). Every \(z_i\) is a minimal central projection and the factors are \(\mathbb C\). A normal state has coefficients \(w_i=\varphi(z_i)\ge0\) with \(\sum_i w_i=1\), by normality on finite sums. There are only countably many positive coefficients: for each \(n\), the set \(\{i:w_i\ge1/n\}\) is finite. Therefore the state vanishes on some nonzero \(z_i\), and no normal state is faithful. It follows that this algebra cannot be identified with \(L^\infty\) of a sigma-finite base: such a nonzero base has an equivalent probability measure and hence a faithful normal integration state. To see this directly, partition a sigma-finite base into measurable sets \(E_n\) of finite measure, and set \(w=\sum_n 2^{-n}(1+\mu(E_n))^{-1}1_{E_n}\). Then \(w>0\) almost everywhere and \(0<\int w\,d\mu\le1\); dividing by this integral gives the required probability density. Write \(q=w/\int w\,d\mu\). Integration against \(q\) is faithful on positive \(L^\infty\) classes. The full multiplication realization, Proposition 3.2a, identifies this algebra with its von Neumann multiplication algebra on \(L^2(X,\mu)\). The integration state is its vector state at \(q^{1/2}\), so it is normal; this argument does not invoke a monotone-convergence theorem for arbitrary measurable nets. Every *-isomorphism between von Neumann algebras is normal, by the complete Corollary 11.4. Such an isomorphism would pull it back to a faithful normal state on \(\ell^\infty(I)\), which the preceding argument excludes. This is a precise reason why the standard probability construction in Corollary 4.3 cannot simply be reused for arbitrary algebras. It does not rule out generalized central decompositions over other bases.

The nonatomic centre with arbitrary nonseparable fibres remains a separate construction. A lifting for a constant Hilbert field proves decomposition of operators commuting with the scalar algebra in that model; it does not alone supply a factorial field for every arbitrary algebra.

The ordinary separable-predual construction has its complete proof in Lemma 4.2 and Corollary 4.3 of Base changes and disintegration.
