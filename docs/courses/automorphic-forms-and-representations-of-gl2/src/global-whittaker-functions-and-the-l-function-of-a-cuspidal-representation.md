# Global Whittaker functions and the L-function of a cuspidal representation

A cusp form has no constant Fourier coefficient. On \(\mathrm{GL}_2\), every remaining coefficient is a translate of one Whittaker function. Local uniqueness then makes that function a product, and a Mellin integral turns the product into the completed \(L\)-function. We will justify the unfolding, remove every possible pole using a fixed test vector, and derive the functional equation with its conductor and sign.

We work over \(\mathbb Q\). Put \(G=\mathrm{GL}_2\), \(n(x)=\left(\begin{smallmatrix}1&x\\0&1\end{smallmatrix}\right)\), \(d(a)=\operatorname{diag}(a,1)\), and
\[
w_0=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]
Let \(\pi\) be an irreducible unitary cuspidal automorphic representation, with central character \(\omega:\mathbb Q^\times\backslash\mathbb A^\times\to\mathbb C^\times\). Throughout the analytic argument, vectors are automorphic cusp forms: smooth at infinity, of finite level at the finite places, and \(K_\infty\)-finite. The Fourier expansion alone also holds for arbitrary smooth finite-level cusp functions. The automorphic vectors used in the analytic argument have the rapid decay, including derivatives, proved in Lesson 4, Theorem 4.2. The tensor product is Lesson 12, Theorem 6.1.

Fix the character
\[
\begin{aligned}
\psi_\infty(x)&=e^{2\pi ix},\\
\psi_p(x)&=e^{-2\pi i\{x\}_p},\\
\psi&=\prod_v\psi_v.
\end{aligned}
\tag{0.1}
\]
Here \(\{x\}_p\in\mathbb Z[1/p]/\mathbb Z\) is the finite negative-power part of the \(p\)-adic expansion. These signs make \(\psi\) trivial on \(\mathbb Q\). Give \(\mathbb Q\backslash\mathbb A\) additive volume one. At a finite prime, multiplicative measure gives \(\mathbb Z_p^\times\) volume one; at infinity it is \(dy/|y|\), on both signs. The induced idèle-class measure is specified in Section 3.

Our local integral is
\[
\begin{gathered}
M_v(s,W_v)
 \\
=\int_{\mathbb Q_v^\times}
    W_v(d(a))|a|_v^{s-1/2}\,d^\times a.
\end{gathered}
\tag{0.2}
\]
This is \(\Psi_v(1,s,W_v)\) in Lesson 9. Real factors and their positive-character phases are Lesson 11, Theorems 5.1 and 6.1. Thus
\[
\begin{aligned}
\Gamma_{\mathbb R}(z)&=\pi^{-z/2}\Gamma(z/2),\\
\Gamma_{\mathbb C}(z)&=2(2\pi)^{-z}\Gamma(z).
\end{aligned}
\tag{0.3}
\]

## 1. Fourier analysis on the additive quotient

Define
\[
\begin{gathered}
W_\phi(g)\\
=\int_{\mathbb Q\backslash\mathbb A}
                 \phi(n(x)g)\psi(-x)\,dx.
\end{gathered}
\tag{1.1}
\]
The quotient is compact, so this integral exists without a convergence restriction. Translation of \(x\) immediately gives
\[
W_\phi(n(y)g)=\psi(y)W_\phi(g).
\tag{1.2}
\]
The sign in (1.1) is what produces the positive character on the right of (1.2).

**Theorem 1.1 — the Fourier–Whittaker expansion.** Every smooth finite-level cusp form satisfies
\[
\phi(g)=\sum_{\alpha\in\mathbb Q^\times}W_\phi(d(\alpha)g).
\tag{1.3}
\]
The series is absolutely convergent and locally uniform in \(g\).

**Proof.** Fix \(g\). Finite-level smoothness supplies an additive compact open subgroup \(U=D\widehat{\mathbb Z}\subset\mathbb A_f\), with \(D\) a positive integer, such that
\(\phi(n(x+u)g)=\phi(n(x)g)\) for \(u\in U\). Indeed, take \(U\) small enough that \(g_f^{-1}n(U)g_f\) is in a right stabilizer of \(\phi\).

The elementary additive approximation used in Lesson 1, Section 1, gives
\[
\mathbb A_f=\mathbb Q+U,\qquad \mathbb Q\cap U=D\mathbb Z.
\]
One can see the first equality by clearing the finitely many denominators of a finite adèle and applying the Chinese remainder theorem at the remaining constrained primes. Consequently a function on \(\mathbb Q\backslash\mathbb A\) invariant under \(U\) is a function on \(\mathbb R/D\mathbb Z\). Its quotient probability measure is \(dx/D\). Applied here, this function is
\[
F_g(x)=\phi(n((x,0_f))g).
\]
It is smooth and \(D\)-periodic. Its ordinary Fourier coefficients are indexed by \(\alpha=m/D\). These are precisely the restrictions of the characters \(\psi(\alpha x)\) that are trivial on \(U\). Averaging over \(U\) makes the coefficient of every other \(\alpha\in\mathbb Q\) zero.

For each integer \(A\geq1\), integration by parts \(A\) times on the circle gives
\[
\begin{gathered}
|c_{m/D}(g)|\\
\leq C_{A,g}(1+|m|)^{-A},\\
c_\alpha(g)\\
=\int_{\mathbb Q\backslash\mathbb A}
       \phi(n(x)g)\psi(-\alpha x)\,dx.
\end{gathered}
\tag{1.4}
\]
The periodic boundary terms cancel. This proves absolute uniform Fourier convergence for fixed \(g\). On a compact set of \(g\)'s, choose a common finite stabilizer and \(D\); the derivatives of \(F_g\) are uniformly bounded on that compact set times the compact circle. Thus the same argument is locally uniform.

Cuspidality says \(c_0(g)=0\). For \(\alpha\ne0\), left rational invariance and \(n(t)d(\alpha)=d(\alpha)n(t/\alpha)\) give
\[
\begin{gathered}
W_\phi(d(\alpha)g)
 \\
=\int_{\mathbb Q\backslash\mathbb A}
      \phi(n(t/\alpha)g)\psi(-t)\,dt\\
=\int_{\mathbb Q\backslash\mathbb A}
      \phi(n(x)g)\psi(-\alpha x)\,dx
\\
=c_\alpha(g).
\end{gathered}
\tag{1.5}
\]
Multiplication by rational \(\alpha\) preserves the quotient measure: its adelic modulus is \(\prod_v|\alpha|_v=1\). Fourier inversion at \(x=0\) proves (1.3). \(\square\)

This also proves that the global Whittaker map \(\phi\mapsto W_\phi\) is injective on the whole cuspidal space: if the function \(W_\phi\) is zero, every term in (1.3) is zero. Its restriction to a nonzero cuspidal representation is therefore nonzero. No assumption of global multiplicity one entered this argument.

## 2. Why a pure vector gives a product

Write
\[
\pi\simeq\bigotimes_v'\pi_v
\tag{2.1}
\]
using Lesson 12. At a finite place, uniqueness of a nonzero local Whittaker functional is Lesson 7, Theorem 2.3. At the real place we use the uniqueness of the moderate-growth analytic Whittaker model isolated in Lesson 11, Section 5. This real analytic input is distinct from the finite-place algebraic argument.

**Theorem 2.1 — local genericity and factorization.** Every \(\pi_v\) is generic. Choose compatible local Whittaker maps, normalized at almost all primes by the spherical function \(W_p^0(1)=1\). Then for every pure tensor \(\phi=\bigotimes_v'\phi_v\),
\[
W_\phi(g)=\prod_v W_{\phi_v}(g_v).
\tag{2.2}
\]
A single nonzero scalar can be absorbed into the real Whittaker map so that this identity holds for all pure vectors. At almost every prime the factor is \(W_p^0\).

**Proof.** Fix all tensor variables except the one at \(v\), and fix the components of \(g\) away from \(v\). The map
\[
\xi_v\longmapsto
 \bigl[h_v\longmapsto
 W_{\xi_v\otimes\xi^v}(h_vg^v)\bigr]
\tag{2.3}
\]
is a local intertwining map to functions with left covariance \(\psi_v\). At infinity it intertwines the Lie algebra and the compact group and its functions have moderate growth. The latter follows from moderate growth of the automorphic form and integration over the compact additive quotient; it also holds after differentiation. We apply the analytic model uniqueness to these function-valued maps. We do not require the real unipotent group to preserve the space of \(K_\infty\)-finite vectors.

For each \(v\) some map (2.3) is nonzero. Otherwise all global Whittaker values of every pure tensor would vanish; pure tensors span the algebraic automorphic module, contradicting Theorem 1.1. Its kernel is a local submodule, so irreducibility makes a nonzero map injective. This proves local genericity, as well as the existence of the local model to which uniqueness applies.

Here is the scalar bookkeeping. Let \(\lambda_v(\xi_v)=W_{\xi_v}(1)\) be a nonzero local functional and choose a reference vector \(e_v\) with \(\lambda_v(e_v)=1\). At almost all finite primes take the distinguished spherical vector. Its value at one is nonzero by Lesson 8, Theorem 4.2. There are only finitely many other reference choices, including infinity.

Local uniqueness says that evaluation of the global map on a tensor, as one variable varies, is a scalar multiple of \(\lambda_v\). Therefore, for any finite set of variables \(S\),
\[
\begin{aligned}
W_{\otimes_v'\xi_v}(1)
 &=W_{\otimes_v'e_v}(1)\prod_{v\in S}\lambda_v(\xi_v),\\
\xi_v&=e_v\quad(v\notin S).
\end{aligned}
\tag{2.4}
\]
To justify the simultaneous product, replace the variables one at a time; each one-dimensional functional space supplies its factor, with its constant obtained by putting that variable equal to \(e_v\). This also shows that the reference value in (2.4) cannot be zero: if it were, the global functional would vanish on every pure tensor and hence identically. Denote it by \(c\ne0\).

Applying the same function-valued uniqueness to (2.3), or evaluating after local right translations, gives
\[
W_\phi(g)=c\prod_vW_{\phi_v}(g_v).
\]
Every adèle \(g\) has \(g_p\in K_p\) for almost all \(p\), and the reference functions there are right \(K_p\)-invariant with value one. Thus this product has only finitely many nonidentity factors at a given \(g\); there is no infinite scalar product to choose. Replace the real Whittaker map by \(c\) times itself. This proves (2.2) on all pure tensors and then by linearity. \(\square\)

**Corollary 2.2 — global multiplicity one.** A cuspidal representation of \(G(\mathbb A)\) occurs at most once in the cuspidal spectrum.

**Proof.** Let \(j_1,j_2\) be two embeddings of the same abstract irreducible tensor product into that spectrum. The proof above says that their Whittaker maps are scalar multiples of the same product of local maps, so
\(W_{j_1(\xi)}=cW_{j_2(\xi)}\), with one fixed \(c\ne0\). The expansion (1.3) gives \(j_1(\xi)=cj_2(\xi)\) for every vector. Their images agree. \(\square\)

This is often called weak multiplicity one. It compares two realizations of the *same* representation. The assertion that agreement outside finitely many places forces two representations to be isomorphic is strong multiplicity one; that assertion belongs to Lesson 15.

## 3. The global integral and its two ends

The idèle-class decomposition of Lesson 2, Proposition 1.1, is
\[
\mathbb Q^\times\backslash\mathbb A^\times
 \simeq \mathbb R_{>0}\times\widehat{\mathbb Z}^{\,\times}.
\tag{3.1}
\]
Choose the representative \(a=(t,u)\). Its norm is \(t\), and give this quotient measure \(dt/t\,du\), where \(\int du=1\). These measures agree with the local multiplicative measures in (0.2) under unfolding. In particular, the rational negative elements account for the two signs at infinity. There is no extra factor of two in the quotient measure.

Set
\[
\begin{gathered}
Z_\phi(s)\\
=\int_{\mathbb Q^\times\backslash\mathbb A^\times}
       \phi(d(a))|a|^{s-1/2}\,d^\times a.
\end{gathered}
\tag{3.2}
\]

**Theorem 3.1 — entire continuation and strip bounds for the integral.** The integral (3.2) converges for every \(s\), defines an entire function, and for every real \(A<B\) and integer \(m\geq0\) satisfies
\[
\begin{gathered}
\sup_{A\leq\sigma\leq B}|Z_\phi(\sigma+i\tau)|
 \\
\leq C_{A,B,m,\phi}(1+|\tau|)^{-m}.
\end{gathered}
\tag{3.3}
\]

**Proof.** Put \(F(t,u)=\phi(d(t,u))\). Lesson 4's rapid decay gives, for all integers \(j,M\geq0\),
\[
\begin{gathered}
|(t\partial_t)^jF(t,u)|\leq C_{j,M}t^{-M}
\\
(t\geq1),
\end{gathered}
\tag{3.4}
\]
uniformly in \(u\) in the compact group of finite units. For small \(t\), rational left invariance gives the exact identity
\[
\begin{gathered}
(R(w_0)\phi)(d(a))
 \\
=\phi(d(a)w_0)\\
=\phi(\operatorname{diag}(1,a))\\
=\omega(a)\phi(d(a^{-1})).
\end{gathered}
\tag{3.5}
\]
Here \(w_0^{-1}d(a)w_0=\operatorname{diag}(1,a)\). The right translate \(R(w_0)\phi\) is again cuspidal and has the same kinds of finiteness and decay. Since \(\omega\) is unitary, applying (3.4) to this translate proves the estimate \(C_{j,M}t^M\) when \(0<t\leq1\). Differentiating (3.5) causes only fixed constants from the smooth real central character. Both ends therefore have decay of every power, for every logarithmic derivative.

Write \(t=e^x\) and \(H(x)=\int F(e^x,u)\,du\). Then
\[
Z_\phi(s)=\int_{\mathbb R}H(x)e^{(s-1/2)x}\,dx.
\tag{3.6}
\]
All derivatives of \(H\) decrease faster than \(e^{-M|x|}\) for every \(M\). On any compact set of \(s\)'s, these estimates dominate the integrand and its \(s\)-derivatives, including every factor \(x^r\). Differentiation under the integral proves entireness.

For \(A\leq\sigma\leq B\), the function
\(H(x)e^{(\sigma-1/2)x}\) and all its derivatives have uniformly bounded \(L^1\)-norms and vanish at both ends. Put \(J_\sigma(x)=H(x)e^{(\sigma-1/2)x}\). For \(|\tau|\geq1\), integrate its Fourier transform by parts \(m\) times:
\[
\begin{gathered}
Z_\phi(\sigma+i\tau)
 \\
=(-i\tau)^{-m}
   \int_{\mathbb R}J_\sigma^{(m)}(x)e^{i\tau x}\,dx.
\end{gathered}
\tag{3.7}
\]
The uniform \(L^1\)-bound proves (3.3). For \(|\tau|\leq1\), use the original \(L^1\)-bound. \(\square\)

This theorem applies to any of our smooth finite-level cuspidal vectors, whether or not it is a pure tensor.

## 4. Unfolding and the fixed test tensor

For a pure tensor as in (2.2), write \(L_v(s)=L(s,\pi_v)\). At a good prime \(p\) the representation is unramified and generic, so Lesson 13, Theorem 3.2, and Lesson 8 give
\[
\begin{gathered}
W_p^0(d(p^m))\\
=\begin{cases}
p^{-m/2}h_m(\alpha_p,\beta_p)&m\geq0,\\
0&m<0,
\end{cases}
\end{gathered}
\tag{4.1}
\]
Here \(h_m(\alpha,\beta)=\sum_{i+j=m}\alpha^i\beta^j\). The local representation is unitary: restrict the global invariant positive form to one tensor variable, keeping the others fixed. The unitary list in Lesson 7, Section 7, gives
\(|\alpha_p|,|\beta_p|\leq p^{1/2}\). This bound suffices here; no Ramanujan bound is assumed. Thus
\[
\begin{gathered}
\int_{\mathbb Q_p^\times}
 |W_p^0(d(a))||a|_p^{\sigma-1/2}\,d^\times a
 \\
\leq \sum_{m\geq0}(m+1)p^{-m(\sigma-1/2)}\\
=(1-p^{-(\sigma-1/2)})^{-2}.
\end{gathered}
\tag{4.2}
\]
The product of these upper bounds converges when \(\sigma>3/2\), since
\(\sum_p p^{-(\sigma-1/2)}<\infty\). The finitely many other local integrals converge in a common sufficiently large right half-plane by Lessons 9 and 11.

**Theorem 4.1 — the Euler product.** In such a half-plane,
\[
\begin{gathered}
Z_\phi(s)\\
=\int_{\mathbb A^\times}
              W_\phi(d(a))|a|^{s-1/2}\,d^\times a\\
=\prod_v M_v(s,W_{\phi_v}).
\end{gathered}
\tag{4.3}
\]

**Proof.** Equations (2.2) and (4.2), together with the finitely many bad-place bounds, show that the absolute integral on \(\mathbb A^\times\) is finite. This can be proved first over any finite set of places, and then by monotone convergence for the absolute-value integrand; outside that set its factors are the nonnegative spherical local absolute integrals. Set \(J_\sigma(a)=|W_\phi(d(a))||a|^{\sigma-1/2}\). Tonelli gives
\[
\begin{gathered}
\int_{\mathbb Q^\times\backslash\mathbb A^\times}
 \sum_{\alpha\in\mathbb Q^\times}J_\sigma(\alpha a)\,d^\times a
 \\
=\int_{\mathbb A^\times}J_\sigma(a)\,d^\times a.
\end{gathered}
\tag{4.4}
\]
The product formula makes the rational factor's norm one. We may therefore substitute Theorem 1.1 into (3.2) and unfold absolutely, proving the first equality in (4.3). Fubini over finite sets of places, followed by the same absolute convergence bound, proves the second. \(\square\)

Define initially in this right half-plane
\[
L(s,\pi)=\prod_vL_v(s),
\tag{4.5}
\]
including infinity. To deduce entireness from Theorem 3.1, we now construct a *fixed* pure vector for which (4.3) equals (4.5).

At every finite prime choose the normalized local newvector of Lesson 8, Section 4. Its integral is exactly \(L_v(s)\). Here is the check for all local types. In the spherical case, the generating identity
\[
\begin{gathered}
\sum_{m\geq0}h_m(\alpha,\beta)X^m
 \\
=\frac1{(1-\alpha X)(1-\beta X)},\\
X\\
=p^{-s}.
\end{gathered}
\tag{4.6}
\]
follows by multiplying the two geometric series. A ramified principal series with one unramified character has newfunction
\((p^{-1/2}\mu_{\rm unram}(p))^m\) on the nonnegative shells, so its integral is
\((1-\mu_{\rm unram}(p)X)^{-1}\). An unramified twist of Steinberg has newfunction \((p^{-1}\chi(p))^m\), so its integral is
\((1-\chi(p)p^{-1/2}X)^{-1}\). In the remaining cases — two ramified principal characters, a ramified Steinberg twist, or a supercuspidal — the newfunction is \(1_{\mathbb Z_p^\times}\), and its integral is one. These are precisely the factors of Lesson 9, Theorem 1.1.

At infinity, local genericity excludes the finite-dimensional representations. The real classification gives either an irreducible principal series or \(D_{k,t}\), including the limit \(k=1\). For a principal series the parity Gaussian
\[
\Phi(u,v)=u^{\epsilon_1}v^{\epsilon_2}e^{-\pi(u^2+v^2)}
\tag{4.7}
\]
has integral \(L_\infty(s)\), by Lesson 11, Theorem 5.1. For \(D_{k,t}\), its bottom vector
\[
W_\infty(d(y))=2\,1_{y>0}y^{t+k/2}e^{-2\pi y}
\tag{4.8}
\]
has integral \(\Gamma_{\mathbb C}(s+t+(k-1)/2)\), by that lesson's equation (6.4). Both are \(K_\infty\)-finite. The product of these vectors belongs to the restricted tensor product of the local Whittaker models, so Theorem 2.1 supplies a global cuspidal vector \(\phi_*\) with this Whittaker function.

**Theorem 4.2 — the completed \(L\)-function is entire.** The function (4.5) continues to the entire function \(Z_{\phi_*}(s)\). It obeys the strip bounds (3.3), in particular is bounded in every vertical strip.

**Proof.** Every local integral of the fixed vector just constructed equals its local factor. Theorem 4.1 therefore gives \(Z_{\phi_*}(s)=L(s,\pi)\) in a right half-plane. Theorem 3.1 supplies the entire continuation and all the asserted bounds. \(\square\)

There is a useful identity for any other pure vector with spherical reference factors outside a finite set. Lessons 9 and 11 prove that
\[
P_v(s,W_v)=\frac{M_v(s,W_v)}{L_v(s)}
\tag{4.9}
\]
is entire; at finite places it is a Laurent polynomial in \(p^{-s}\), and for real \(K_\infty\)-finite vectors it is a polynomial in \(s\). At almost all places it is one. Thus
\[
\begin{aligned}
Z_\phi(s)&=P_\phi(s)L(s,\pi),\\
P_\phi(s)&=\prod_vP_v(s,W_{\phi_v}).
\end{aligned}
\tag{4.10}
\]
extends from Theorem 4.1 to the entire plane, with a finite product on its right.

Proving only that a quotient \(Z_\phi/P_\phi\) is meromorphic would leave its potential poles unresolved. The vector \(\phi_*\), for which \(P_{\phi_*}=1\), is what removes this issue.

## 5. The functional equation and its signs

Define the cuspidal form
\[
\phi^\dagger(g)=\omega(\det g)^{-1}\phi(gw_0).
\tag{5.1}
\]
The twist is automorphic because \(\omega\) is trivial on rational elements. It realizes \(\pi\otimes(\omega^{-1}\circ\det)\), which is the contragredient \(\widetilde\pi\): this is Lesson 9, Proposition 2.1, at finite places, the inverse-parameter real classification of Lesson 11 at infinity, and the local uniqueness in Lesson 12. The central character of this twist is \(\omega^{-1}\).

Rational left invariance and (3.5) give
\[
\phi^\dagger(d(a))=\phi(d(a^{-1})).
\tag{5.2}
\]
Inverting the idèle class in the everywhere convergent integral proves
\[
Z_{\phi^\dagger}(1-s)=Z_\phi(s)
\quad\text{for every }s.
\tag{5.3}
\]

The Whittaker function of (5.1) is
\[
W_{\phi^\dagger}(g)
 =\omega(\det g)^{-1}W_\phi(gw_0).
\tag{5.4}
\]
For a pure vector let
\[
W_v^\dagger(g_v)=\omega_v(\det g_v)^{-1}W_v(g_vw_0).
\]
These factors have character \(\psi_v\) and belong to the model of \(\widetilde\pi_v\). The local functional equations in Lesson 9, Theorem 3.2, and Lesson 11, Theorems 5.1 and 6.1, are exactly
\[
\begin{gathered}
P_v(1-s,W_v^\dagger)
 \\
=\varepsilon(s,\pi_v,\psi_v)P_v(s,W_v).
\end{gathered}
\tag{5.5}
\]
At an unramified prime \(w_0\in K_p\), the central character is unramified, and \(W_p^\dagger\) is the normalized spherical function of the dual. Both normalized integrals are one and the local epsilon factor is one.

**Theorem 5.1 — the global functional equation.** Put
\[
\varepsilon(s,\pi)=\prod_v\varepsilon(s,\pi_v,\psi_v).
\tag{5.6}
\]
Only finitely many factors differ from one. Then
\[
L(s,\pi)=\varepsilon(s,\pi)L(1-s,\widetilde\pi).
\tag{5.7}
\]
If \(c_p\) is the local newvector conductor and \(N_\pi=\prod_pp^{c_p}\), then
\[
\begin{aligned}
\varepsilon(s,\pi)&=\varepsilon(1/2,\pi)N_\pi^{\,1/2-s},\\
|\varepsilon(1/2,\pi)|&=1.
\end{aligned}
\tag{5.8}
\]

**Proof of the equation and conductor.** Apply (4.10) to \(\phi^\dagger\) in its own right half-plane, and continue it using the already established entireness for the dual representation. Multiplying the finitely many identities (5.5) gives
\[
\begin{gathered}
Z_{\phi^\dagger}(1-s)
 \\
=\varepsilon(s,\pi)P_\phi(s)L(1-s,\widetilde\pi).
\end{gathered}
\tag{5.9}
\]
Combine (5.3), (4.10) and (5.9), and take the fixed vector \(\phi_*\) with \(P_{\phi_*}=1\). This proves (5.7). In particular, we have not multiplied infinitely many gamma factors in two half-planes that might not overlap.

Lesson 9, Theorem 5.1, gives
\(\varepsilon(s,\pi_p,\psi_p)=\varepsilon(1/2,\pi_p,\psi_p)p^{c_p(1/2-s)}\).
The real epsilon factor is constant in \(s\), by Lesson 11: it is \(i^{\epsilon_1+\epsilon_2}\) for a principal series and \(i^k\) for \(D_{k,t}\). This proves the first assertion in (5.8). The modulus assertion is proved below after checking character independence. \(\square\)

**Proposition 5.2 — coherent character changes.** Replacing \(\psi(x)\) by \(\psi(bx)\), for \(b\in\mathbb Q^\times\), leaves (5.6) unchanged.

**Proof.** The local character-change formulas, Lesson 9, Proposition 6.1, and Lesson 11, equation (6.9), multiply (5.6) by
\[
\begin{gathered}
\prod_v\omega_v(b)|b|_v^{2s-1}
 \\
=\omega(b)|b|_{\mathbb A}^{2s-1}\\
=1.
\end{gathered}
\tag{5.10}
\]
Both equalities to one use rational \(b\). \(\square\)

A change at a *single* place need not be coherent. For example, changing only \(\psi_v\) to \(\psi_v(-\,\cdot)\) multiplies that local epsilon factor by \(\omega_v(-1)\). Changing all places in this way multiplies the global product by \(\omega(-1)=1\). This is the precise distinction behind the sign pitfall.

**Proof of the modulus in (5.8).** For a unitary representation, its contragredient is isomorphic to its conjugate: the invariant Hermitian form identifies the smooth dual with the conjugate smooth module. Conjugating local integrals changes \(\psi_v\) to \(\psi_v^{-1}\), and gives
\[
\begin{aligned}
L(s,\widetilde\pi)&=\overline{L(\bar s,\pi)},\\
\varepsilon(s,\widetilde\pi;\psi^{-1})
 &=\overline{\varepsilon(\bar s,\pi;\psi)}.
\end{aligned}
\tag{5.11}
\]
These also follow directly from the local factors of Lessons 9 and 11; the \(L\)-factor is independent of the additive character. Proposition 5.2 with \(b=-1\) removes the coherent character change in the epsilon identity. Applying (5.7) twice gives
\(\varepsilon(s,\pi)\varepsilon(1-s,\widetilde\pi)=1\): the entire \(L\)-function is not identically zero, since its convergent right-hand Euler product is nonzero. Evaluate this identity at \(s=1/2\) and use (5.11). The result is
\(|\varepsilon(1/2,\pi)|^2=1\). \(\square\)

The same proof applies to \(\pi\otimes(\chi\circ\det)\) for every unitary Hecke character \(\chi\), because its automorphic forms remain cuspidal and unitary. Thus their completed \(L\)-functions are entire and satisfy the corresponding twisted equation. Essentially unitary norm twists follow by translating \(s\); this adds no new analytic argument.

## 6. The classical variable, level and root number

Let
\[
f(z)=\sum_{n\geq1}a_ne^{2\pi inz},\qquad a_1=1,
\]
be a newform of weight \(k\geq2\), level \(N\), and character \(\chi\). “New” means orthogonal to the span of degeneracy images from proper divisor levels, and \(f\) is an eigenform for all Hecke and diamond operators. We use the classical normalization
\(T_nf=a_nf\). Its definition, Fourier coefficient formula and Fricke convention are [LG-MF-10](https://kokunoyumeto.github.io/open-math-courses-public/courses/LG-MF/LG-MF-10.html), Sections 1, 3.1 and 5.

**Lemma 6.1 — the irreducible newform representation and its conductor.** The unitary adelic lift \(\phi_f\) of Lesson 2 generates an irreducible cuspidal representation \(\pi_f\). It has real component \(D_k\) and
\[
N_{\pi_f}=N.
\tag{6.1}
\]

**Proof.** Fix the positive holomorphic weight-\(k\) line at infinity and \(K_1(N)\) at the finite places. Lessons 3–4 give a finite sum of cuspidal constituent spaces in this fixed-level, fixed-type space. The real line in every contributing constituent is the bottom line of \(D_k\), by Lesson 11, Theorem 7.1. Lesson 12, equation (5.3), factors its finite fixed space. Theorem 2.1 and Corollary 2.2 now supply the global Whittaker factorization and the absence of a multiplicity space.

For a constituent \(\rho\), set \(M_\rho=\prod_pp^{c(\rho_p)}\). It contributes only if \(M_\rho\mid N\). The tensor of its local newvectors and its holomorphic bottom vector is a line at level \(M_\rho\). Its first Fourier coefficient is nonzero: factorization gives nonzero finite values at one and the real bottom value \(e^{-2\pi}\) after choosing the real normalization \(y^{k/2}e^{-2\pi y}\). Thus this line yields a normalized classical form \(h_\rho\).

The local oldvector basis in Lesson 8, Theorem 2.1, gives the constituent's whole contribution at level \(N\). Right finite translation by \(d(p^{-j})\), moved by a rational diagonal matrix to infinity, corresponds to a nonzero scalar times \(h_\rho(p^jz)\). With several primes these basis elements are
\[
h_\rho(dz),\qquad d\mid N/M_\rho.
\tag{6.2}
\]
The scalar is \(d^{k/2}\) in the unitary lift; it does not change their span. If \(M_\rho<N\), this whole block is old, since it comes from the proper level \(M_\rho\). If \(M_\rho=N\), it is a line and cannot occur at any proper divisor level. Orthogonality of distinct constituents and the Petersson comparison in Lesson 2 therefore identify the new subspace with the sum of the lines with \(M_\rho=N\).

Project \(f\) to these constituent lines, obtaining \(f_\rho\). Orthogonal representation projections commute with all right-translation Hecke operators and diamonds; they also preserve the holomorphic bottom condition. Hence
\(T_nf_\rho=a_n(f)f_\rho\). The coefficient-of-\(q\) formula gives, at every index,
\[
\begin{gathered}
a_n(f_\rho)\\
=a_1(T_nf_\rho)\\
=a_n(f)a_1(f_\rho).
\end{gathered}
\tag{6.3}
\]
Fourier expansions then imply \(f_\rho=a_1(f_\rho)f\). Two distinct nonzero orthogonal projections cannot both be scalar multiples of \(f\). There is exactly one nonzero constituent, so \(\phi_f\) generates it irreducibly. Its block was new, whence \(M_{\pi_f}=N\). \(\square\)

This argument uses weak multiplicity one and the full Hecke coefficient formula, including bad indices. It does not assume strong multiplicity one. It also establishes here the part of Lesson 8, Section 5, that constructs the classical newform line; the separate main lemma there still requires the strong multiplicity-one input.

Put
\[
\begin{aligned}
w&=s+\frac{k-1}{2},\\
L_{\rm cl}(f,w)&=\sum_{n\geq1}a_nn^{-w}.
\end{aligned}
\tag{6.4}
\]

**Theorem 6.2 — comparison of completed functions.** With the normalizations above,
\[
L(s,\pi_f)=\Gamma_{\mathbb C}(w)L_{\rm cl}(f,w).
\tag{6.5}
\]
If
\[
\begin{gathered}
\Lambda_N(f,w)\\
=N^{w/2}(2\pi)^{-w}\Gamma(w)L_{\rm cl}(f,w),
\end{gathered}
\tag{6.6}
\]
and \(f^\vee(z)=\sum\overline{a_n}e^{2\pi inz}\), then
\[
\begin{gathered}
\Lambda_N(f,w)
 \\
=\varepsilon(1/2,\pi_f)\Lambda_N(f^\vee,k-w).
\end{gathered}
\tag{6.7}
\]
Both completed functions are entire and bounded in vertical strips.

**Proof of the factor comparison.** Lemma 6.1 makes the finite vector the tensor of local newvectors. Normalize their Whittaker values at one to one and normalize the real bottom function to
\(1_{y>0}y^{k/2}e^{-2\pi y}\), half of (4.8). The global scalar is one because \(a_1(f)=1\). To see this, the coefficient (1.5) at \(\alpha=1\), evaluated on the usual \(\widehat{\mathbb Z}\) additive fundamental domain, is \(a_1e^{-2\pi}\). The factored value is the same real value times the finite values.

More generally, evaluating (1.5) at a positive integer \(n\) gives
\[
a_n=n^{k/2}\prod_p\xi_p(p^{v_p(n)}),
\tag{6.8}
\]
where \(\xi_p\) is the normalized local newfunction. Its unit invariance removes the unit part of \(n\) at each prime. For \(w\) sufficiently far right,
\[
\begin{gathered}
\sum_{n\geq1}a_nn^{-w}
 \\
=\prod_p\sum_{m\geq0}\xi_p(p^m)p^{-m(s-1/2)}\\
=\prod_pL(s,\pi_{f,p}).
\end{gathered}
\tag{6.9}
\]
Absolute convergence follows either from (4.2) and the finitely many bad factors, or directly from their explicit newfunctions. Section 4 checked all the local sums, so (6.9) includes the bad primes. The real factor is \(\Gamma_{\mathbb C}(w)\) by Lesson 11. This proves (6.5), then continuation proves it everywhere.

The integral gives a second check on the factor of two. Since \(d(u)\in K_1(N)\) for every \(u\in\widehat{\mathbb Z}^{\,\times}\), (3.2) for the unitary lift is
\[
\begin{aligned}
Z_{\phi_f}(s)
 &=\int_0^\infty f(it)t^{w}\,\frac{dt}{t}\\
 &=(2\pi)^{-w}\Gamma(w)L_{\rm cl}(f,w)\\
 &=\tfrac12L(s,\pi_f).
\end{aligned}
\tag{6.10}
\]
The last equality agrees with the half-sized bottom vector just chosen.

**Proof of the functional equation.** Unitarity identifies the dual representation with the conjugate, so its normalized classical newform is \(f^\vee\): its finite Euler coefficients are \(\overline{a_n}\), by (5.11), (6.5) and uniqueness of a convergent Dirichlet series. The variable for \(1-s\) is
\[
1-s+\frac{k-1}{2}=k-w.
\]
Equations (5.7)–(5.8) and (6.1) yield
\[
\begin{gathered}
L(s,\pi_f)
 \\
=\varepsilon(1/2,\pi_f)
   N^{\,k/2-w}L(1-s,\widetilde\pi_f).
\end{gathered}
\tag{6.11}
\]
Multiplying by \(N^{w/2}/2\) gives (6.7), because
\(w/2+k/2-w=(k-w)/2\). Equations (6.5)–(6.6) show that \(\Lambda_N\) is \(N^{w/2}/2\) times the adelic completed function. The multiplier has bounded modulus on any fixed vertical strip, so Theorem 4.2 gives its entireness and bounds. \(\square\)

For the sign comparison, use exactly the unitary slash convention of LG-MF-10:
\[
\begin{gathered}
(f|_kA)(z)\\
=\det(A)^{k/2}(cz+d)^{-k}f(Az),\\
W_N\\
=\begin{pmatrix}0&-1\\N&0\end{pmatrix}.
\end{gathered}
\tag{6.12}
\]
Its Section 5 gives
\[
f|_kW_N=\eta_f f^\vee,\qquad |\eta_f|=1.
\tag{6.13}
\]
For trivial character, \(f^\vee=f\) and \(\eta_f\) is the Fricke sign. For a general character, (6.13) is a relation with conjugate coefficients, not a sign eigenvalue on the original character space.

We now derive the root number from (6.13). Substituting \(z=it\) into the slash gives
\[
f(i/(Nt))=i^k\eta_f N^{k/2}t^k f^\vee(it).
\tag{6.14}
\]
In the everywhere convergent Mellin integral (6.10), substitute \(y=1/(Nt)\):
\[
\begin{gathered}
\int_0^\infty f(iy)y^w\,\frac{dy}{y}
 \\
=N^{-w}\int_0^\infty f(i/(Nt))t^{-w}\,\frac{dt}{t}\\
=i^k\eta_f N^{k/2-w}
       \int_0^\infty f^\vee(it)t^{k-w}\,\frac{dt}{t}.
\end{gathered}
\tag{6.15}
\]
Multiplying by \(N^{w/2}\) gives the same completed equation as (6.7). Its dual completed function is nonzero, so comparison of the constants proves
\[
\boxed{\ \varepsilon(1/2,\pi_f)=i^k\eta_f.\ }
\tag{6.16}
\]
Thus the adelic equation specializes to the level-\(N\) functional equation assigned to LG-MF-12. That lesson's further twist and converse-theorem arguments are separate from the comparison proved here.

## 7. The discriminant form, with every normalization

For \(\Delta(z)=\sum_{n\geq1}\tau(n)e^{2\pi inz}\), weight \(k=12\) and level \(N=1\), put \(w=s+11/2\). Then
\[
\begin{gathered}
L(s,\pi_\Delta)
 \\
=2(2\pi)^{-(s+11/2)}\Gamma(s+11/2)\\
 \qquad{}\times\sum_{n\geq1}\frac{\tau(n)}{n^{s+11/2}}.
\end{gathered}
\tag{7.1}
\]
The Dirichlet series in this formula is initially evaluated far right; the entire expression continues by Theorem 4.2.

Lesson 13, Example 5.2, computed \(\tau(2)=-24,\tau(3)=252\), and the arithmetic Satake products \(2^{11}\), \(3^{11}\). Thus the first two finite factors, in the classical variable, are
\[
\begin{gathered}
L_2(\Delta,w)\\
=(1+24\,2^{-w}+2^{11-2w})^{-1},\\
L_3(\Delta,w)\\
=(1-252\,3^{-w}+3^{11-2w})^{-1}.
\end{gathered}
\tag{7.2}
\]
With \(w=s+11/2\), their linear coefficients become
\(24\,2^{-11/2}2^{-s}\) and \(-252\,3^{-11/2}3^{-s}\), and each quadratic term becomes \(p^{-2s}\). These agree with the unitary Satake factors computed there.

Every finite prime is unramified, so every finite epsilon factor is one. At infinity the component is \(D_{12}\) and its epsilon is \(i^{12}=1\). The coefficients are real, so the representation is self-dual. Hence
\[
L(s,\pi_\Delta)=L(1-s,\pi_\Delta).
\tag{7.3}
\]
Equivalently, with
\(\Lambda(\Delta,w)=(2\pi)^{-w}\Gamma(w)L_{\rm cl}(\Delta,w)\),
\[
\begin{aligned}
\Lambda(\Delta,w)&=\Lambda(\Delta,12-w),\\
L(s,\pi_\Delta)&=2\Lambda(\Delta,s+11/2).
\end{aligned}
\tag{7.4}
\]
The center is \(s=1/2\) adelically and \(w=6\) classically. A positive root number imposes no forced zero at this center.

## 8. Exercises with complete solutions

### 8.1. Whittaker covariance — easy

Prove \(W_\phi(n(y)g)=\psi(y)W_\phi(g)\), including the sign, and show that multiplying \(\phi\) by the automorphic twist \(\chi(\det g)\) multiplies its Whittaker function by the same factor.

**Solution 8.1.** In (1.1), use \(t=x+y\):
\[
\begin{aligned}
W_\phi(n(y)g)
 &=\int\phi(n(x+y)g)\psi(-x)\,dx\\
 &=\int\phi(n(t)g)\psi(-t+y)\,dt
\\
 &=\psi(y)W_\phi(g).
\end{aligned}
\]
Translation preserves quotient Haar measure. For
\(\phi_\chi(g)=\chi(\det g)\phi(g)\), the determinant of \(n(x)\) is one, so the factor \(\chi(\det g)\) is constant in the integral. Hence
\(W_{\phi_\chi}(g)=\chi(\det g)W_\phi(g)\). In particular the twist remains cuspidal, since its constant term is that factor times the old constant term.

### 8.2. The missing constant term — medium

Starting only from smooth finite-level automorphy and vanishing of the constant term, justify absolute Fourier convergence and derive (1.3). Explain why the expansion would have an extra term for a noncuspidal form.

**Solution 8.2.** Choose \(U=D\widehat{\mathbb Z}\) as in the proof of Theorem 1.1. Additive approximation and rational invariance identify the function \(x\mapsto\phi(n(x)g)\), modulo \(U\), with a smooth function of period \(D\). For \(m\ne0\), its \(m\)-th coefficient is
\[
c_{m/D}(g)=\frac1D\int_0^D F_g(x)e^{-2\pi imx/D}\,dx.
\]
Integrating twice by parts gives
\[
|c_{m/D}(g)|
 \leq \left(\frac{D}{2\pi|m|}\right)^2
       \frac1D\int_0^D|F_g''(x)|\,dx.
\]
The sum of these bounds is finite. Higher derivatives give locally uniform bounds as well. Coefficients indexed by \(\alpha\notin D^{-1}\mathbb Z\) vanish because their character is nontrivial on \(U\), while the function is \(U\)-invariant. Thus Fourier inversion at zero is an absolutely convergent sum over \(\mathbb Q\).

Its zero-frequency coefficient is
\(c_0(g)=\int_{\mathbb Q\backslash\mathbb A}\phi(n(x)g)\,dx\), zero by the hypothesis. For every other coefficient, rational \(d(\alpha)\) invariance and the change \(t=\alpha x\) prove \(c_\alpha(g)=W_\phi(d(\alpha)g)\); the adelic Jacobian is one. This gives (1.3). Without constant-term vanishing the correct formula is
\[
\phi(g)=c_0(g)+
 \sum_{\alpha\in\mathbb Q^\times}W_\phi(d(\alpha)g).
\]
It is precisely this additional term that can produce poles in a noncuspidal global zeta calculation.

### 8.3. Recover the level-\(N\) equation — medium

Let \(f\) be a normalized weight-\(k\) newform at level \(N\), with
\(f|W_N=\eta_f f^\vee\). Starting from the adelic equation, derive the classical completed equation and identify its root number. In weight two with trivial character, determine the sign when the Fricke eigenvalue is \(-1\).

**Solution 8.3.** Put \(w=s+(k-1)/2\). Lemma 6.1 identifies the conductor with \(N\), and Theorem 6.2 gives
\(L(s,\pi_f)=2(2\pi)^{-w}\Gamma(w)L_{\rm cl}(f,w)\).
At \(1-s\) the corresponding variable is \(k-w\). Consequently the adelic equation is
\[
L(s,\pi_f)=
\varepsilon(1/2,\pi_f)N^{k/2-w}
 L(1-s,\widetilde\pi_f).
\]
Multiply by \(N^{w/2}/2\). The left side is \(\Lambda_N(f,w)\), and the power of \(N\) on the right is \(N^{(k-w)/2}\). Thus
\[
\Lambda_N(f,w)=
\varepsilon(1/2,\pi_f)\Lambda_N(f^\vee,k-w).
\]
To compute the constant, use the slash (6.12) on \(it\), giving (6.14), and replace \(y\) by \(1/(Nt)\) in the Mellin integral. This gives the same identity with \(i^k\eta_f\) in place of the adelic constant, so
\(\varepsilon(1/2,\pi_f)=i^k\eta_f\). In weight two, \(i^2=-1\); a Fricke eigenvalue \(-1\) therefore gives root number \(+1\). A Fricke eigenvalue \(+1\) would give root number \(-1\), which in the self-dual case forces the value at \(w=k/2=1\) to vanish.

### 8.4. Bounds on an arbitrary strip — hard

Prove boundedness in every vertical strip of the completed \(L\)-function without using a convexity or Phragmén–Lindelöf theorem. Strengthen the bound to arbitrary polynomial decay in the imaginary direction.

**Solution 8.4.** Choose the fixed pure test vector \(\phi_*\) of Section 4. Its local newvector integrals and its real parity Gaussian or discrete bottom integral equal the local \(L\)-factors exactly. Hence
\(L(s,\pi)=Z_{\phi_*}(s)\) first far right and then everywhere by continuation.

Let
\(H(x)=\int_{\widehat{\mathbb Z}^{\,\times}}
\phi_*(d(e^x,u))\,du\).
Rapid decay at infinity gives
\(|H^{(j)}(x)|\leq C_{j,M}e^{-Mx}\) for \(x\geq0\).
Apply (3.5) to \(R(w_0)\phi_*\) for \(x\leq0\); unitarity of the central character gives
\(|H^{(j)}(x)|\leq C_{j,M}e^{Mx}\).
Fix \(A<B\) and set \(R=\max(|A-1/2|,|B-1/2|)\). Choose \(M>R+1\). The product rule shows, uniformly for \(\sigma\in[A,B]\),
\[
\begin{gathered}
\left\|\partial_x^m
 \bigl(H(x)e^{(\sigma-1/2)x}\bigr)\right\|_1
\\
\leq
 \sum_{j=0}^m\binom mj R^{m-j}
 \int_{\mathbb R}|H^{(j)}(x)|e^{R|x|}\,dx
\\
<\infty.
\end{gathered}
\]
Every boundary term vanishes. Integrating against \(e^{i\tau x}\) by parts \(m\) times gives \(C_m|\tau|^{-m}\) for \(|\tau|\geq1\); the original integral is uniformly bounded for \(|\tau|\leq1\). This proves the arbitrary-power bound. The exact test vector matters: carrying this estimate through division by an arbitrary \(P_\phi(s)\) could introduce zeros in the denominator and would not establish the assertion.

## 9. What this lesson does not prove, and source locators

All five assigned global results are proved above. The local theory and the cuspidal analytic foundations are prerequisites, with the following precise boundaries.

* The additive approximation and idèle-class descriptions are Lesson 1, Section 1, and Lesson 2, Proposition 1.1; the classical lift, central character and Petersson comparison are Lesson 2, Sections 1–4. The product formula and conductor-zero global character convention are used there.
* Cuspidal spectral decomposition, finiteness at fixed level and holomorphic compact type are Lessons 3–4, particularly Lesson 3, Proposition 5.1, and Lesson 4, Theorems 4.2 and 5.2. Rapid decay of every derivative, rather than boundedness alone, is the analytic input in Section 3.
* The restricted tensor product and its fixed-space factorization are Lesson 12, Theorem 6.1 and equation (5.3). Finite-place Whittaker uniqueness is Lesson 7, Theorem 2.3. The unramified unitary parameter bound used in (4.2) is the unitary classification proved in that lesson's Theorem 7.1; it is weaker than Ramanujan.
* The real moderate-growth Whittaker existence, uniqueness and Gaussian realization are the analytic input explicitly stated in Lesson 11, Section 5. Its primary locator is Jacquet–Langlands, Theorem 5.13 and Lemma 5.13.1. The real classification and the resulting full-family \(L\)- and epsilon calculations are proved in that lesson, Theorems 3.2, 5.1 and 6.1.
* All finite local newfunctions, including bad places, are Lesson 8, Theorem 2.1 and Section 4. Their \(L\)-factors, duality, functional equations, conductor exponents and character changes are Lesson 9, Theorem 1.1, Proposition 2.1, Theorems 3.2 and 5.1, and Proposition 6.1. The spherical representation and classical good-prime normalizations are Lesson 13, Theorems 3.2 and 4.1. No matrix-zeta definition for a nongeneric local representation is needed here.
* The classical newspace definition, coefficient identity at all Hecke indices, unitary Fricke convention, and pseudo-eigenvalue relation (6.13) are LG-MF-10, Sections 1 and 3.1, Lemma 2.2 and Section 5. The Mellin equation, shift and root-number comparison are proved here, without assuming a future classical functional equation. The strong multiplicity-one and converse theorems assigned to Lesson 15 are not assumed.

For comparison with the canonical primary sources: Jacquet–Langlands, §9, Proposition 9.2, proves factorization, while §11, Theorem 11.1, proves the cuspidal completed equation and Corollary 11.2 treats twists. Its Proposition 11.1.1 is the weak multiplicity-one argument. Getz–Hahn, §§11.3–11.7 of the 2022 draft gives Theorems 11.3.3–11.3.4, Proposition 11.4.3 and the local/global Rankin–Selberg framework. Entireness of every completed factor is proved directly here with a fixed Whittaker test tensor.

The scope throughout is \(\mathrm{GL}_2/\mathbb Q\). The same global mechanism over another number field also requires its complex-place local analytic inputs and the appropriate idèle-class compact factor; it is not an additional theorem asserted here.

## References

* H. Jacquet and R. P. Langlands, [*Automorphic Forms on GL(2)*](https://publications.ias.edu/sites/default/files/Automorphic-forms-on-GL2.pdf), Lecture Notes in Mathematics 114, 1970, §§9 and 11, especially Proposition 9.2, Theorem 11.1, Proposition 11.1.1 and Corollary 11.2.
* J. R. Getz and H. Hahn, [*An Introduction to Automorphic Representations*](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), draft of 22 April 2022, §§11.3–11.7.
* [Classical oldforms, newforms and Fricke operators](https://kokunoyumeto.github.io/open-math-courses-public/courses/LG-MF/LG-MF-10.html), LG-MF-10, Sections 1, 3.1 and 5.

*Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Self-checked by the writing AI. Public domain (CC0).*
