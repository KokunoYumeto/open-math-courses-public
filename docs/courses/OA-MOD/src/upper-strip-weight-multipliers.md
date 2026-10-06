# Upper imaginary time and finite weight multipliers

An imaginary-time endpoint can be recognized without applying a weight to an infinite value or assuming that a multiplier is entire. The useful data are two finite-domain inclusions and an identity on the weight's finite linear domain. Taking adjoints explains both the sign of the imaginary time and the placement of the two multipliers.

The exact earlier proof used below is The single-weight generator has an exact finite-pair test, the lower-strip finite-pair criterion. Its modular specialization uses the normal automorphisms already constructed in The modular fundamental theorem, the full-domain results A closed intertwining relation is a bounded operator strip and A strip endpoint acts on the whole finite left ideal, and Two facts about closed strips, strip uniqueness. It does not require the separate classification of general linear isometries discussed in AG-01. The bounded-comparison route uses the preceding Hilbert completion and extension proof.

For source comparison, see Masamichi Takesaki, *Theory of Operator Algebras II*, Exercise VIII.2(2). The organization here is by adjoint reflection, finite products and examples. The external source is a reference for the mathematics; the proof is supplied through the exact earlier argument and the steps below.

## The domains and the upper-strip criterion

Let \(M\) be an arbitrary von Neumann algebra and let \(\varphi\) be a faithful normal semifinite weight. Write \(\sigma_t=\sigma_t^\varphi\). No countability hypothesis on \(M\), finiteness of \(\varphi(1)\), or norm continuity of every real modular orbit is imposed.

The finite left ideal consists of the \(x\in M\) for which \(\varphi(x^*x)<\infty\); denote it by \(\mathfrak n\). Its finite linear domain is

\[
 \mathfrak m=\operatorname{span}(\mathfrak n^*\mathfrak n).
 \tag{SM.1}
\]

Domain algebra and its positive cone and Linear extension without infinite subtraction prove the ideal properties and the unique finite complex-linear extension of \(\varphi\) to \(\mathfrak m\). In particular, \(\mathfrak m\) is closed under adjoints and
\(\varphi(z^*)=\overline{\varphi(z)}\) there. In this lesson, an identity involving \(\varphi\) on a nonpositive element always uses that extension.

Put \(S_+=\{z\in\mathbb C:0\leq\operatorname{Im}z\leq1\}\). By an upper-strip extension of \(a\in M\) we mean a bounded function \(F:S_+\to M\), sigma-weakly continuous on the closed strip and norm holomorphic in its interior, with \(F(t)=\sigma_t(a)\). The boundary continuity in this definition is essential; SM-05 exhibits why norm continuity cannot be substituted.

**Theorem.** For \(a,b\in M\), the following assertions are equivalent:

1. There is an upper-strip extension \(F\) of \(a\), and \(F(i)=b\).
2. Both domain inclusions hold:

\[
 \begin{gathered}
 \mathfrak n a\subseteq\mathfrak n,\\
 \mathfrak n b^*\subseteq\mathfrak n,
 \end{gathered}
 \tag{SM.2}
\]

and, for every \(z\in\mathfrak m\), the finite pairing identity is

\[
 \varphi(za)=\varphi(bz)
 \tag{SM.3}
\]

Consequently, the existence of a strip is equivalent to the existence of such a \(b\); that \(b\) is unique and is denoted by \(\sigma_i(a)\). The theorem concerns all of \(\mathfrak n\) and \(\mathfrak m\), not a selected dense subalgebra.

The products in (SM.3) have the required domains before their weights are compared. Indeed, for \(z=y^*x\), with \(x,y\in\mathfrak n\), (SM.2) gives

\[
 \begin{aligned}
 za&=y^*(xa),\\
 bz&=(yb^*)^*x.
 \end{aligned}
 \tag{SM.4}
\]

Both products belong to \(\mathfrak m\); finite sums give this conclusion for every \(z\in\mathfrak m\).

## Reflection reverses imaginary time

Let \(S_-=\{z:-1\leq\operatorname{Im}z\leq0\}\). If \(F\) is a bounded continuous upper-strip function as above, define

\[
 G(z)=F(\overline z)^*.
 \tag{SM.5}
\]

The involution preserves norms and is sigma-weakly continuous. For the latter assertion, every normal functional \(\omega\) gives another normal functional
\(\omega^\sharp(x)=\overline{\omega(x^*)}\), as follows directly from the vector-coefficient description of the predual in Its dual is exactly B(H) and The concrete predual and its intrinsic norm. Thus each scalar test of \(G\) is continuous.

Reflection together with the conjugate-linear involution preserves holomorphy. To check this in norm, expand \(F\) near an interior point \(w\) as
\(F(w+\zeta)=\sum_{k\geq0}C_k\zeta^k\), with a norm-convergent power series. Near \(\overline w\) the function \(G\) has the norm-convergent series
\(\sum_{k\geq0}C_k^*(z-\overline w)^k\). The required local series theorem is supplied in the scalar complex-analysis programme, followed by the predual Cauchy argument in HS-01.

Since each \(\sigma_t\) preserves adjoints, the boundary and endpoint of \(G\) are

\[
 \begin{aligned}
 G(t)&=\sigma_t(a^*),\\
 G(-i)&=b^*.
 \end{aligned}
 \tag{SM.6}
\]

Applying the same construction to \(G\) recovers \(F\). We have therefore established a bijection of the two strip problems, including the complete closed-strip topology and their endpoint values.

For completeness, an upper-strip extension is unique: apply every element of \(M_*\) to the difference of two extensions and use MA-08's boundary uniqueness. These scalar differences vanish on the real edge, so vanish on the strip; the predual separates the points of \(M\). Moreover, normality of \(\sigma_s\), supplied by MF-06, permits applying it to \(F\). Comparing the two extensions with real edge \(\sigma_{t+s}(a)\) gives \(F(z+s)=\sigma_s(F(z))\). On the upper edge this reads

\[
 F(t+i)=\sigma_t(b).
 \tag{SM.7}
\]

No statement about normality of arbitrary linear isometries is used.

## The equivalence, with every finite product justified

We use AG-06 with the pair \(A=a^*\), \(B=b^*\). That theorem, with its proof on the full closed modular domain, says that the lower strip with endpoint \(B\) exists exactly when

\[
 \begin{aligned}
 A\mathfrak n^*&\subseteq\mathfrak n^*,\\
 \mathfrak n B&\subseteq\mathfrak n,\\
 \varphi(Ax)&=\varphi(xB).
 \end{aligned}
 \tag{SM.8}
\]

The last equality is required for every \(x\in\mathfrak m\). Taking adjoints in the first inclusion converts it exactly to
\(\mathfrak n a\subseteq\mathfrak n\). The second one is exactly
\(\mathfrak n b^*\subseteq\mathfrak n\).

To compare the last identity with (SM.3), let \(z\in\mathfrak m\) and set \(x=z^*\). Its two products are in \(\mathfrak m\), by (SM.4) and closure under adjoints. Conjugating the equality
\(\varphi(a^*z^*)=\varphi(z^*b^*)\) gives precisely
\(\varphi(za)=\varphi(bz)\). Conversely, conjugating (SM.3) and making the same substitution gives the last equality in (SM.8), for every \(x\in\mathfrak m\).

Thus (SM.2)–(SM.3) are equivalent to the complete lower-strip criterion for \((a^*,b^*)\). SM-02 converts that criterion to the upper-strip extension of \(a\) with endpoint \(b\). It also proves uniqueness of \(b\). This establishes both directions of SM-01.

The earlier full-domain argument matters here. In the reverse implication, AG-06 first obtains a modular-operator identity on the Tomita algebra. AG-05 proves that algebra is a graph core for the required powers. Closedness then gives the identity on the entire domain of \(\Delta\), and HS-01 constructs the bounded strip. Hence using AG-06 in this proof does not promote an equality on merely dense test vectors to an unproved domain identity.

There is also a useful uniqueness test entirely inside the finite domains. If \(b_1,b_2\) both satisfy (SM.2)–(SM.3), put \(d=b_1-b_2\). Then
\(\mathfrak n d^*\subseteq\mathfrak n\) and \(\varphi(dz)=0\) on \(\mathfrak m\). For \(y\in\mathfrak n\), choose \(x=yd^*\in\mathfrak n\) and \(z=y^*x\). It follows that

\[
 \begin{aligned}
 0&=\varphi(dy^*yd^*)\\
  &=\varphi((yd^*)^*(yd^*)).
 \end{aligned}
 \tag{SM.9}
\]

Faithfulness gives \(yd^*=0\) for every \(y\in\mathfrak n\). Semifiniteness means that \(\mathfrak m\) is sigma-weakly dense in \(M\), by The finite part of an extended-valued weight. Since \(\mathfrak n\) is a linear left ideal, it contains \(\mathfrak m=\operatorname{span}(\mathfrak n^*\mathfrak n)\), so it too is dense. Separate sigma-weak continuity of multiplication, proved in The ultraweak convergence needed by finite cutoffs, extends \(yd^*=0\) to all \(y\in M\). Taking \(y=1\) gives \(d=0\).

## A matrix calculation fixes the sign

Let \(M=M_2(\mathbb C)\) and
\(\varphi(x)=\operatorname{Tr}(hx)\), where \(h\) is positive and invertible. The finite-dimensional modular calculation in A block model with infinite mass and arbitrarily fast modular motion gives \(\sigma_z(a)=h^{iz}ah^{-iz}\). In particular,

\[
 \sigma_i(a)=h^{-1}ah.
 \tag{SM.10}
\]

Every matrix belongs to both finite domains. Directly, cyclicity of the finite matrix trace gives

\[
 \begin{aligned}
 \varphi(za)&=\operatorname{Tr}(ahz),\\
 \varphi(bz)&=\operatorname{Tr}(hbz).
 \end{aligned}
 \tag{SM.11}
\]

Cyclicity follows by writing the trace of a product as
\(\sum_{j,k}X_{jk}Y_{kj}\) and interchanging the two finite indices. The equality of the two expressions in (SM.11) for every matrix \(z\) forces \(ah=hb\): testing \(z=E_{jk}\) reads each entry of their difference. Thus \(b=h^{-1}ah\), confirming the upper, rather than lower, imaginary-time sign.

If \(h\) is diagonal with entries \(r_j>0\), the endpoint of \(E_{jk}\) is \((r_k/r_j)E_{jk}\). This elementary check is useful because the real modular group has the factor \((r_j/r_k)^{it}\); substituting \(t=i\) reverses that ratio.

## A bounded strip whose real edge is not norm continuous

Here is an infinite-weight example that satisfies every condition of SM-01. Take \(M=\prod_{n\geq1}M_2(\mathbb C)\), put \(h_n=\operatorname{diag}(1,e^n)\), and define

\[
 \begin{gathered}
 \varphi(x)\\
 =\sum_{n\geq1}\operatorname{Tr}(h_nx_n).
 \end{gathered}
 \tag{SM.12}
\]

This defines the weight for \(x\geq0\). KM-08 proves faithfulness, normality for arbitrary increasing nets, semifiniteness, and its modular action by identifying the full closed Tomita operator. In particular, \(\varphi(1)=\infty\).

Set \(a_n=E_{21}\) and \(b_n=e^{-n}E_{21}\). They define bounded elements of \(M\), and the strip is

\[
 F(z)_n=e^{inz}E_{21}.
 \tag{SM.13}
\]

Its norm is at most one for \(0\leq\operatorname{Im}z\leq1\), its real edge is \(\sigma_t(a)\), and its upper endpoint is \(b\).

We check all the analytic assertions. In the faithful block representation on
\(\bigoplus_{n\geq1}\mathbb C^2\), a vector coefficient is a sum of continuous scalar functions dominated by
\(\sum_n\|\xi_n\|\|\eta_n\|<\infty\), by Hilbert-space Cauchy–Schwarz. Finite partial sums therefore converge uniformly on the whole strip. CP-03 represents every normal functional as an absolutely convergent sum of such coefficients; the uniform operator bound gives the same uniform approximation for that sum. This proves sigma-weak continuity, including at both boundaries. Around an interior point \(z_0\) with \(\operatorname{Im}z_0=\delta>0\), choose \(0<r<\delta\). The \(k\)-th exponential coefficient has norm \(A_k\), the supremum over \(n\geq1\) of \(e^{-n\delta}n^k/k!\). Bounding this supremum by the nonnegative sum and then summing the exponential series gives

\[
 \begin{gathered}
 \sum_{k\geq0}A_kr^k\\
 \leq\sum_{n\geq1}e^{-n(\delta-r)}\\
 <\infty .
 \end{gathered}
 \tag{SM.14}
\]

Hence the coordinate power series converges in the product norm for \(|z-z_0|\leq r\) and equals \(F\). This proves norm holomorphy in the interior.

The finite-domain conditions can also be checked without the theorem. Write \(c_{1,n},c_{2,n}\) for the columns of \(x_n\), and put \(Q(x)=\varphi(x^*x)\). Then

\[
 \begin{gathered}
 Q(x)\\
 =\sum_n\|c_{1,n}\|^2\\
 +\sum_n e^n\|c_{2,n}\|^2.
 \end{gathered}
 \tag{SM.15}
\]

The only nonzero column of \(x_na_n\) is its first, equal to \(c_{2,n}\). The only nonzero column of \(x_nb_n^*\) is its second, equal to \(e^{-n}c_{1,n}\). Consequently,

\[
 \begin{gathered}
 Q(xa)\\
 =\sum_n\|c_{2,n}\|^2,\\
 Q(xb^*)\\
 =\sum_n e^{-n}\|c_{1,n}\|^2.
 \end{gathered}
 \tag{SM.16}
\]

Each is bounded above by (SM.15). Thus both inclusions in (SM.2) hold on the whole finite left ideal.

In each block the two finite traces
\(\operatorname{Tr}(h_nz_na_n)\) and
\(\operatorname{Tr}(h_nb_nz_n)\) both equal \((z_n)_{12}\).
For \(z=y^*x\) with \(x,y\in\mathfrak n\), put \(u_n=c_{1,n}(y)\) and \(v_n=c_{2,n}(x)\). Formula (SM.15) makes both sequences square summable. Their Hilbert norms give the bound

\[
 \begin{gathered}
 \sum_n |(z_n)_{12}|\\
 \leq \|u\|_2\|v\|_2<\infty.
 \end{gathered}
 \tag{SM.17}
\]

The GNS polarization formula in WG-005 identifies the finite extension of \(\varphi\) with these absolutely convergent block sums. Summing the block identity, then taking finite linear combinations, proves (SM.3) for every \(z\in\mathfrak m\).

Finally let \(t_n=\pi/n\), so \(t_n\to0\). The \(n\)-th block of \(F(t_n)-F(0)\) is \(-2E_{21}\). Since \(F(0)=a\), we obtain

\[
 \|F(t_n)-a\|=2.
 \tag{SM.18}
\]

Thus the real edge is not norm continuous, although the bounded upper-strip extension and all finite-domain identities exist. The topology specified in SM-01 retains this legitimate example and the arbitrary-von-Neumann-algebra scope of the theorem.
