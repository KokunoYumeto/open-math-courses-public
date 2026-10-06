# Symmetric tensor norms and Rademacher truncation

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Self-checked by the writing AI. New original text: public domain (CC0).* 

A bounded bilinear form initially controls a sum of tensors by a sum of products of norms. For C*-algebras, sums of squares contain more information. Random signs and functional-calculus truncation connect these two controls. The first step gives a surjection between completed tensor products; injectivity, proved in the [next lesson](tensor-completion-injectivity-and-state-domination.md), will turn it into a norm comparison.

We use the basic C*-algebra functional calculus, states and their Cauchy–Schwarz inequality, and the Banach-space projective tensor product. No factor, trace, countability or separability assumption enters.

## 1. The symmetric square norm

Write \(A\odot B\) for the complex algebraic tensor product. Put
\[
q(x)=\frac{x^*x+xx^*}{2},\qquad
\|u\|_\sigma=
\inf_{u=\sum_jx_j\otimes y_j}
\Big\|\sum_jq(x_j)\Big\|^{1/2}
\Big\|\sum_jq(y_j)\Big\|^{1/2}.
\tag{1}
\]
The infimum uses finite decompositions. The projective norm is
\[
\|u\|_\pi=\inf_{u=\sum_jx_j\otimes y_j}
\sum_j\|x_j\|\|y_j\|.
\tag{2}
\]
We also use the real projective norm on \(A_{\rm sa}\odot_{\mathbb R}B_{\rm sa}\), denoted \(\pi_{\mathbb R}\). This real space identifies with the self-adjoint part of \(A\odot B\).

**Proposition 1.1.** Formula (1) defines an involution-invariant norm, with
\[
\|u\|_\sigma\le\|u\|_\pi,
\qquad \|uv\|_\sigma\le4\|u\|_\sigma\|v\|_\sigma.
\tag{3}
\]
For self-adjoint \(u\), the infimum in (1) can be restricted to self-adjoint factors. For self-adjoint \(a,b\),
\[
\|a\otimes b\|_\sigma=\|a\|\|b\|.
\tag{4}
\]

**Proof.** In a nonzero decomposition, replace all first factors by \(t x_j\) and second factors by \(t^{-1}y_j\), with \(t>0\). The two square-sum norms can thereby be made equal, without changing their product. Concatenating two balanced decompositions gives a cost at most the sum of their costs. Taking infima proves the triangle inequality. Scalar homogeneity follows by rescaling one factor, and involution preserves every cost.

For a state \(\varphi\), Cauchy–Schwarz applied to both \(x\) and \(x^*\) gives \(|\varphi(x)|^2\le\varphi(q(x))\). Consequently
\[
|\sum_j\varphi(x_j)\psi(y_j)|
\le\varphi\Big(\sum_jq(x_j)\Big)^{1/2}
\psi\Big(\sum_jq(y_j)\Big)^{1/2}.
\tag{5}
\]
Product states therefore define \(\sigma\)-continuous functionals. States separate elements of each C*-algebra: in a faithful representation, vector states and polarization detect every nonzero operator. On any finite-dimensional subspace their restrictions span its dual. Applying this to the finite spans of the factors of a tensor shows that product states separate algebraic tensors. Thus (1) is nondegenerate. If an algebra is zero, its algebraic tensor product is zero and there is nothing to check.

Since \(\|q(x)\|\le\|x\|^2\), the elementary-tensor cost is at most \(\|x\|\|y\|\). The triangle inequality yields the first inequality in (3). If \(u=u^*\) and \(x_j=a_j+ic_j\), \(y_j=b_j+id_j\), with all four parts self-adjoint, then
\[
u=\sum_j(a_j\otimes b_j-c_j\otimes d_j),
\quad q(x_j)=a_j^2+c_j^2,
\quad q(y_j)=b_j^2+d_j^2.
\tag{6}
\]
This is a self-adjoint-factor decomposition with exactly the original square sums, proving the restricted infimum assertion. Choose states norming the self-adjoint elements \(a,b\). Equation (5) bounds any decomposition of \(a\otimes b\) below by \(\|a\|\|b\|\); the one-term decomposition gives the reverse bound. This proves (4).

For the product estimate, write \(Q_x=\sum_iq(x_i)\), \(Q_z=\sum_jq(z_j)\). The two unsymmetrized sums \(\sum x_i^*x_i\) and \(\sum x_ix_i^*\) are bounded above by \(2Q_x\); similarly for \(z\). Hence
\[
\begin{aligned}
\Big\|\sum_{i,j}(x_i z_j)^*(x_i z_j)\Big\|
&\le4\|Q_x\|\|Q_z\|,\\
\Big\|\sum_{i,j}(x_i z_j)(x_i z_j)^*\Big\|
&\le4\|Q_x\|\|Q_z\|.
\end{aligned}
\tag{7}
\]
For example, the first sum is \(\sum_jz_j^*(\sum_ix_i^*x_i)z_j\). Average (7), do the same in \(B\), and take square roots. The product decomposition of two tensors then has cost at most four times the product of their costs. Taking infima proves (3). \(\square\)

The completion \(A\widehat\otimes_\sigma B\) is thus an involutive algebra with continuous multiplication. Multiplying its norm by \(4\) makes multiplication submultiplicative. This auxiliary Banach algebra norm is not a C*-norm.

## 2. A fourth moment with noncommuting coefficients

Let \(r_1,\ldots,r_n\) be independent signs, each uniformly distributed on \(\{-1,1\}\). Expectations below are finite averages over \(2^n\) choices. For self-adjoint \(a_j\), put
\[
A(r)=\sum_jr_ja_j,\qquad S=\sum_ja_j^2.
\tag{8}
\]

**Lemma 2.1.** One has the operator inequalities
\[
\mathbb E A(r)^2=S,
\qquad
\mathbb E A(r)^4\le S^2+2\|S\|S\le3\|S\|S.
\tag{9}
\]

**Proof.** Orthogonality of the signs gives the first equality. Also
\[
A(r)^2=S+\sum_{j<k}r_jr_k(a_ja_k+a_ka_j).
\]
Distinct unordered pairs have zero averaged product, so
\[
\mathbb E A(r)^4=S^2+\sum_{j<k}(a_ja_k+a_ka_j)^2.
\tag{10}
\]
For any \(z\), \((z+z^*)^2\le2(z^*z+zz^*)\), because the difference is \((z-z^*)^*(z-z^*)\). Apply this to \(z=a_ja_k\). The second term in (10) is at most
\[
2\sum_ja_j\Big(\sum_{k\ne j}a_k^2\Big)a_j
\le2\sum_ja_jSa_j\le2\|S\|S.
\]
Finally \(S^2\le\|S\|S\). All these are operator-order statements; the coefficients were never commuted. \(\square\)

## 3. Truncating the random sum

For \(\tau>0\), let \(h_\tau(t)=\max(-\tau,\min(t,\tau))\), and \(e_\tau(t)=t-h_\tau(t)\). These continuous functions vanish at zero, so their functional calculus lies in the original algebra, including when it has no unit.

**Lemma 3.1.** With (8),
\[
\mathbb E h_\tau(A)^2\le S,
\qquad
\mathbb E e_\tau(A)^2
\le\frac{3}{16\tau^2}\|S\|S.
\tag{11}
\]

**Proof.** The first assertion follows from \(h_\tau(t)^2\le t^2\) and (9). For \(|t|\ge\tau\),
\[
|t|-\tau\le\frac{t^2}{4\tau},
\]
because \((|t|-2\tau)^2\ge0\). For \(|t|<\tau\) the residual is zero. Thus \(e_\tau(t)^2\le t^4/(16\tau^2)\); functional calculus and (9) give the second assertion. \(\square\)

For a finite random tensor \(\mathbb E C\otimes D\) with self-adjoint factors, absorbing the square roots of its probability weights into its factors gives
\[
\|\mathbb E C\otimes D\|_\sigma
\le\|\mathbb E C^2\|^{1/2}\|\mathbb E D^2\|^{1/2}.
\tag{12}
\]
This estimate does not require uniform operator-norm bounds on the untruncated random sums.

## 4. A bounded part and a smaller residual

**Lemma 4.1.** For every self-adjoint algebraic tensor \(u\) and every \(\eta>0\), there are self-adjoint algebraic tensors \(v,w\) with
\[
u=v+w,
\quad \|v\|_{\pi_{\mathbb R}}\le(27/16+\eta)\|u\|_\sigma,
\quad \|w\|_\sigma\le(2/3+\eta)\|u\|_\sigma.
\tag{13}
\]

**Proof.** For nonzero \(u\), choose a balanced self-adjoint decomposition
\[
u=\sum_ja_j\otimes b_j,
\qquad \Big\|\sum_ja_j^2\Big\|=\Big\|\sum_jb_j^2\Big\|=M
<\|u\|_\sigma+\delta.
\]
Use the same signs in \(A=\sum r_ja_j\) and \(B=\sum r_jb_j\). Then \(\mathbb E A\otimes B=u\). Set
\[
\begin{aligned}
v&=\mathbb E h_\tau(A)\otimes h_\tau(B),\\
w&=\mathbb E\big[e_\tau(A)\otimes B+
h_\tau(A)\otimes e_\tau(B)\big].
\end{aligned}
\tag{14}
\]
The pointwise identity \(A\otimes B=v(r)+w(r)\) follows by adding and subtracting \(h_\tau(A)\otimes B\). In particular, the first residual in (14) uses the full \(B\). Using a truncated factor in both residual terms would omit \(e_\tau(A)\otimes e_\tau(B)\).

The bounded part has projective norm at most \(\tau^2\). Equations (11)–(12), together with \(\mathbb E B^2=\sum b_j^2\), give
\[
\|w\|_\sigma\le\frac{\sqrt3}{2\tau}M^{3/2}.
\tag{15}
\]
Choose \(\tau=3^{3/2}M^{1/2}/4\). Then the two bounds are \(27M/16\) and \(2M/3\). Taking \(\delta\) sufficiently small gives (13). For \(u=0\), take \(v=w=0\). \(\square\)

## 5. Surjectivity at the completion level

**Theorem 5.1.** The identity on algebraic tensors extends to a surjection
\[
I_{\mathbb R}:A_{\rm sa}\widehat\otimes_{\pi,\mathbb R}B_{\rm sa}
\longrightarrow (A\widehat\otimes_\sigma B)_{\rm sa}.
\tag{16}
\]
For every \(u\) in the target and \(\varepsilon>0\), it has a preimage \(z\) with
\[
\|z\|_{\pi_{\mathbb R}}\le(81/16)\|u\|_\sigma+\varepsilon.
\tag{17}
\]
This statement does not yet assert uniqueness of the preimage.

**Proof.** First suppose \(u\) is algebraic. Choose \(0<\eta<1/3\) and repeatedly apply (13), starting with \(w_0=u\), to obtain \(w_{k-1}=v_k+w_k\). Put \(a=27/16+\eta\), \(b=2/3+\eta<1\). Then
\[
\|v_k\|_{\pi_{\mathbb R}}\le a b^{k-1}\|u\|_\sigma,
\quad \|w_k\|_\sigma\le b^k\|u\|_\sigma.
\tag{18}
\]
The series \(z=\sum_kv_k\) converges projectively, maps to \(u\), and has norm at most \(a(1-b)^{-1}\|u\|_\sigma\). Letting \(\eta\) be small gives (17), since \(a/(1-b)\to81/16\).

For a completed self-adjoint \(u\), choose self-adjoint algebraic approximants so that their successive differences \(d_k\) satisfy \(u=\sum_kd_k\) in \(\sigma\)-norm and \(\sum_k\|d_k\|_\sigma\le\|u\|_\sigma+\delta\). This is achieved by making the first approximation error small and later errors decrease geometrically. Lift each \(d_k\) by the preceding construction, allowing a summable additional projective error. The sum of these lifts converges projectively and maps to \(u\). Taking \(\delta\) and the additional errors small proves (17).

Finally, the self-adjoint algebraic tensors are dense in the target: replace any approximant \(t\) to a self-adjoint \(u\) by \((t+t^*)/2\). This justifies the approximation used above. \(\square\)

## 6. Exercises with complete solutions

**Exercise 1.** Explain why balancing a decomposition does not change its tensor or its cost.

*Solution.* Replacing \(x_j,y_j\) by \(t x_j,t^{-1}y_j\) preserves each tensor. The square sums are multiplied by \(t^2,t^{-2}\). Their product of square-root norms is unchanged. If their original norms are \(s,t_0>0\), choose the scaling parameter \((t_0/s)^{1/4}\) to make them equal.

**Exercise 2.** Verify (6), including its square-sum identity.

*Solution.* Expanding \((a+ic)\otimes(b+id)\) and averaging it with its adjoint leaves \(a\otimes b-c\otimes d\). Also \((a-ic)(a+ic)+(a+ic)(a-ic)=2(a^2+c^2)\). Thus \(q(a+ic)=a^2+c^2\), even if \(a,c\) do not commute. Summing proves the identities.

**Exercise 3.** Why do product states separate an algebraic tensor?

*Solution.* Put all its first and second factors in finite-dimensional spaces \(E,F\). Since states separate elements of each algebra, their restrictions have zero common annihilator on \(E\) and \(F\). In finite dimension their linear spans are the entire dual spaces. Products therefore span \(E^*\otimes F^*\), which separates \(E\otimes F\). A tensor annihilated by every product state is zero.

**Exercise 4.** Derive (10) for two noncommuting self-adjoint elements.

*Solution.* For \(A=r_1a+r_2b\), one has \(A^2=a^2+b^2+r_1r_2(ab+ba)\). Squaring and averaging kills the two terms linear in \(r_1r_2\), and leaves \((a^2+b^2)^2+(ab+ba)^2\). No reordering of \(a,b\) occurs.

**Exercise 5.** Prove the residual scalar estimate in Lemma 3.1.

*Solution.* Inside \([-\tau,\tau]\) the residual is zero. Outside it has absolute value \(|t|-\tau\). The inequality \((|t|-2\tau)^2\ge0\) gives \(4\tau(|t|-\tau)\le t^2\). Squaring gives \(e_\tau(t)^2\le t^4/(16\tau^2)\), and functional calculus preserves this nonnegative scalar inequality.

**Exercise 6.** Refute the decomposition obtained by truncating both second factors in (14).

*Solution.* In the scalar case take \(A=B=1\), \(\tau=1/2\). The proposed bounded term is \(1/4\) and the two proposed residual terms total \(1/2\), so their sum is \(3/4\), rather than \(1\). The missing term is the product of the two residuals, \(1/4\). The asymmetric formula (14) includes it through \(e_\tau(A)B\).

**Exercise 7.** Show that the same omission can occur at the threshold chosen in Lemma 4.1.

*Solution.* Take four scalar coefficients \(a_j=b_j=1\). Then \(M=4\), \(A=B=\sum_{j=1}^4r_j\), and \(\tau=3\sqrt3/2<4\). The two events \(A=\pm4\) have total probability \(1/8\); the other values have absolute value at most \(2\). The omitted expected residual product is therefore \((4-3\sqrt3/2)^2/8>0\). Thus the omission is relevant even at the proof's specified threshold.

**Exercise 8.** Check the constants in (15).

*Solution.* Each residual term costs at most \((\sqrt3 M/(4\tau))\sqrt M\), by (11) and the second moment bound. There are two terms, giving \(\sqrt3 M^{3/2}/(2\tau)\). At \(\tau=3^{3/2}\sqrt M/4\), this is \(2M/3\), while \(\tau^2=27M/16\).

**Exercise 9.** Compute the geometric-series constant without discarding \(\eta\).

*Solution.* Equation (18) gives total cost at most \((27/16+\eta)/(1/3-\eta)\) times \(\|u\|_\sigma\). This is larger than \(81/16\) when \(\eta>0\), and tends to \(81/16\) as \(\eta\downarrow0\). Before injectivity is known, this proves approximate bounds for preimages; it does not justify an equality at a positive \(\eta\).

**Exercise 10.** Construct the summable algebraic differences used in Theorem 5.1.

*Solution.* Choose \(u_k\) algebraic and self-adjoint with \(\|u-u_k\|_\sigma<\delta 2^{-k-3}\). Set \(d_1=u_1\), \(d_k=u_k-u_{k-1}\) for \(k\ge2\). The telescoping series converges to \(u\). Its total norm is at most \(\|u\|_\sigma+\|u-u_1\|_\sigma+\sum_{k\ge2}(\|u-u_k\|_\sigma+\|u-u_{k-1}\|_\sigma)<\|u\|_\sigma+\delta\). Lift the differences with additional errors summing to any prescribed positive tolerance.

## References

Gilles Pisier, [*Grothendieck's Theorem, past and present*, expanded UNCUT author version, 21 August 2013](https://webusers.imj-prg.fr/~gilles.pisier/grothendieck.UNCUT.pdf), Section 9, Lemma 9.2 and the full proof of Theorem 9.1, printed pp.29–31 (PDF pp.31–33). The fourth-moment statements, continuous clipping and geometric iteration were actually read. Section 9 of [arXiv:1101.4195v3](https://arxiv.org/pdf/1101.4195v3), printed pp.29–30 (PDF pp.31–32), gives the earlier selected truncation proof. These are separately identified source versions.

Sections 1–5 here supply the full symmetric tensor norm, noncommuting operator-order estimates, asymmetric residual and completed real lifting argument. Their bounds are 27/16, 2/3 and 81/16 in the normalization stated here. Pisier's Khintchine constants concern a different formulation; the complex reduction he describes as parallel is not used as a missing proof. This lesson establishes surjectivity and approximate lifts; the next lesson proves uniqueness. Exact transitive C*-algebra and Banach-space foundation closure remains pending.
