# Convex supports and convolution cancellation

*Reconstructed and checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Public domain (CC0).*

A convolution can lose isolated points of support through complex cancellation. For two compact distributions its convex hull is nevertheless exactly the sum of the two factor hulls. We prove the statement in every dimension, including its approximation steps, and then determine when actual support can be recovered.

The dimension \(n\ge1\) is fixed. Pairings are complex linear and \(\partial_j=\partial/\partial x_j\). Write \(\mathcal D=C_c^\infty\), and let \(\mathcal E'\) denote compactly supported distributions. The [convolution lesson](convolution-as-addition-of-supports.md), B0–B3 and Theorems 1.1, 2.1, 3.1, 3.2 and 5.2, proves support localization, tensor products, convolution under proper addition, smoothing, associativity, joint weak sequence convergence on fixed supports and shrinking approximate identities. Finite point jets and their independence are proved in [angular foundations, A3](../prerequisites/U011-free-foundations/angular-foundations-U018.md). The ordinary integral operations, finite-dimensional compactness and scalar calculus used below have the exact supplied proof locations listed at the end.

## Every finite support function determines a compact convex set

For a nonempty bounded \(E\subset\mathbb R^n\), define
\[
 H_E(\xi)=\sup_{x\in E}x\cdot\xi,\qquad
 \operatorname{ch}E=\overline{\operatorname{conv}E}.                 \tag{1.1}
\]
Here the convex hull consists of finite convex combinations. Such combinations remain in a ball containing \(E\); their closure is closed and bounded, hence compact. A linear functional has the same supremum on \(E\), on its convex combinations and on their closure. Thus \(H_E=H_{\operatorname{ch}E}\). A supremum of linear functionals is convex and positively homogeneous. Support functions can have negative values and need not be even.

**Theorem 1.1.** If \(H:\mathbb R^n\to\mathbb R\) is finite, convex and positively homogeneous, there is a unique nonempty compact convex set \(K\) with support function \(H\). It is
\[
 K=\{x:x\cdot\xi\le H(\xi)\text{ for every }\xi\in\mathbb R^n\}.       \tag{1.2}
\]
For each \(\eta\), at least one \(x_\eta\in K\) satisfies \(x_\eta\cdot\eta=H(\eta)\).

**Proof.** Homogeneity gives \(H(0)=0\); convexity applied to a midpoint gives subadditivity \(H(\xi+\eta)\le H(\xi)+H(\eta)\). Set \(M=\max_j\{|H(e_j)|,|H(-e_j)|\}\). Decomposing a vector into its signed coordinate vectors gives \(H(\xi)\le M\|\xi\|_1\). Since \(0\le H(\xi)+H(-\xi)\), the opposite bound follows. Subadditivity applied in both orders now proves
\[
 |H(\xi)|\le M\|\xi\|_1,\qquad
 |H(\xi)-H(\eta)|\le M\|\xi-\eta\|_1.                              \tag{1.3}
\]

We prove the required finite-dimensional linear extension directly. Suppose \(L\) is linear on a subspace \(V\) and \(L\le H\) there. For \(v\notin V\), a number \(c\) can be chosen between
\[
 \sup_{m\in V}\{L(m)-H(m-v)\}
 \quad\hbox{and}\quad
 \inf_{m\in V}\{H(m+v)-L(m)\}.
\]
Every quantity on the left is at most every quantity on the right: for \(m,k\in V\),
\[
 L(m)+L(k)=L(m+k)\le H(m+k)\le H(m-v)+H(k+v).
\]
Taking \(m=0\) or \(k=0\) also bounds both endpoints by finite numbers, so completeness of the reals supplies \(c\). Define \(\widetilde L(m+tv)=L(m)+tc\). If \(t>0\), use the upper bound for \(c\) with \(m/t\) to get \(\widetilde L(m+tv)\le H(m+tv)\). If \(t=-s<0\), use the lower bound with \(m/s\) and multiply by \(s\). The case \(t=0\) was assumed. This proves the extension step.

For \(\eta\ne0\), start with \(L(t\eta)=tH(\eta)\). Domination for \(t<0\) follows from \(H(\eta)+H(-\eta)\ge0\), and for \(t\ge0\) from homogeneity. Extend to \(\mathbb R^n\) in at most \(n-1\) steps. The resulting linear functional is \(x_\eta\cdot\xi\), with coordinates \(x_{\eta,j}=L(e_j)\); it is dominated by \(H\) and equals \(H\) at \(\eta\). Starting from the zero subspace also produces a dominated functional, which handles \(\eta=0\). Hence \(K\) is nonempty and \(H_K=H\).

The intersection (1.2) is closed and convex. Applying its inequalities to \(\pm e_j\) gives
\[
 -H(-e_j)\le x_j\le H(e_j)\quad(x\in K).                            \tag{1.4}
\]
It is consequently bounded and compact. To prove uniqueness, let \(L\) be any nonempty compact convex set and \(y\notin L\). Choose a nearest \(z\in L\), put \(d=|y-z|>0\) and \(\xi=y-z\). For \(x\in L\), the segment \(z+t(x-z)\) lies in \(L\), \(0\le t\le1\). Differentiating its squared distance to \(y\) at the minimizing endpoint \(t=0\) gives \(\xi\cdot(x-z)\le0\). Therefore \(H_L(\xi)=z\cdot\xi\) and, for \(0<\varepsilon<d\),
\[
 H_L(\xi)+\varepsilon|\xi|\le y\cdot\xi.                            \tag{1.5}
\]
Thus a point satisfying all the support inequalities for \(L\) must belong to \(L\). This identifies every compact convex set with its half-space intersection and proves uniqueness. \(\square\)

In particular, for nonempty compact convex sets,
\[
 K\subset L\ \Longleftrightarrow\ H_K\le H_L,\qquad
 K=L\ \Longleftrightarrow\ H_K=H_L.                                 \tag{1.6}
\]
For arbitrary nonempty sets \(E,F\), the support-sum identity is
\(H_{E+F}=H_E+H_F\), with values allowed in \(\mathbb R\cup\{+\infty\}\). The upper inequality follows term by term. For the lower one, choose independent points approaching the two finite suprema. If one supremum is infinite, fix a point of the other set and let the first scalar product grow without bound. These arguments cover every case.

For bounded \(E,F\), the compact convex set \(\operatorname{ch}E+\operatorname{ch}F\) has this support function. Theorem 1.1 gives \(\operatorname{ch}(E+F)=\operatorname{ch}E+\operatorname{ch}F\). Also \(H_{tE}(\xi)=tH_E(\xi)\) for \(t>0\), while \(H_{tE}(\xi)=(-t)H_E(-\xi)\) for \(t<0\); for \(t=0\) it is zero. These follow by taking the supremum of \(tx\cdot\xi\).

For a vector \(c\) and any real matrix \(A:\mathbb R^m\to\mathbb R^n\), including a singular one,
\[
 H_{c+A\overline B(0,1)}(\xi)=c\cdot\xi+|A^T\xi|.                  \tag{1.7}
\]
Cauchy–Schwarz gives the upper bound. If \(A^T\xi\ne0\), take the unit vector \(A^T\xi/|A^T\xi|\); otherwise every point of the ball gives equality.

## Two square-integral identities locate a self-convolution

For a smooth compact function put \(\widetilde u(x)=\overline{u(-x)}\).

**Lemma 2.1.** For complex \(u\in\mathcal D(\mathbb R^n)\),
\[
 \|u*\widetilde u\|_2^2=\|u*u\|_2^2.                               \tag{2.1}
\]
**Proof.** For any such \(g\), \((g*\widetilde g)(0)=\int|g(y)|^2\,dy\). A change of variable in the compact integral gives \(\widetilde{f*g}=\widetilde f*\widetilde g\), and \(\widetilde{\widetilde f}=f\). Applying the first identity to \(g=u*\widetilde u\) and to \(g=u*u\) gives the same value at zero of \(u*u*\widetilde u*\widetilde u\), by associativity and commutativity. All rearranged integrals are over compact sets and absolutely integrable. \(\square\)

**Lemma 2.2.** Let \(Q=\prod_{j=1}^n[-R_j,R_j]\), \(R_j>0\), and let \(g\) be smooth with support in \(Q\). With \(D=\partial_1^2\cdots\partial_n^2\),
\[
 \|g\|_\infty\le C_Q\|Dg\|_2,\qquad
 C_Q=3^{-n/2}\prod_{j=1}^n(2R_j)^{3/2}.                           \tag{2.2}
\]
**Proof.** Twice applying the one-dimensional fundamental theorem, using zero values sufficiently far to the left, and then doing this in every coordinate yields
\[
 g(x)=\int_{\substack{y_j<x_j\\1\le j\le n}}
            \prod_{j=1}^n(x_j-y_j)\,Dg(y)\,dy.                    \tag{2.3}
\]
Fubini is valid because the differentiated function has compact support. For \(x\in Q\), Cauchy–Schwarz bounds the integral by \(\|Dg\|_2\) times the square root of
\[
 \prod_j\int_{-R_j}^{x_j}(x_j-y_j)^2\,dy
 =3^{-n}\prod_j(x_j+R_j)^3
 \le3^{-n}\prod_j(2R_j)^3.
\]
Outside \(Q\), \(g(x)=0\); the same supremum bound follows. \(\square\)

**Proposition 2.3.** If \(0\ne u\in\mathcal D(\mathbb R^n)\), then \(q=u*u\ne0\) and
\[
 \operatorname{ch}\operatorname{supp}q
       =2\operatorname{ch}\operatorname{supp}u.                   \tag{2.4}
\]
**Proof.** Choose one box \(Q\) containing both \(\operatorname{supp}(u*\widetilde u)\) and \(\operatorname{supp}(u*u)\). Set \(v=\partial_1\cdots\partial_nu\). Reflection gives
\[
 D(u*\widetilde u)=(-1)^n v*\widetilde v,\qquad Dq=v*v.
\]
Lemmas 2.1–2.2 therefore imply
\[
 \|u\|_2^2=(u*\widetilde u)(0)
       \le C_Q\|D(u*\widetilde u)\|_2
       =C_Q\|Dq\|_2.                                             \tag{2.5}
\]
This already proves \(q\ne0\).

For real \(\xi\), replace \(u\) by \(u_\xi(x)=e^{x\cdot\xi}u(x)\). Its self-convolution is \(e^{x\cdot\xi}q(x)\); the same box works for all \(\xi\). Expanding its mixed derivative by the product rule gives a finite sum of terms \(c_\alpha e^{x\cdot\xi}\xi^{2\mathbf1-\alpha}\partial^\alpha q(x)\), with \(0\le\alpha_j\le2\) and \(c_\alpha=\prod_j\binom2{\alpha_j}\). Each derivative of \(q\) is supported in \(\operatorname{supp}q\). Taking \(L^2\) norms and absorbing their fixed norms into a constant proves
\[
 \int e^{2x\cdot\xi}|u(x)|^2\,dx
 \le C_u(1+|\xi|)^{2n}e^{H_{\operatorname{supp}q}(\xi)}.           \tag{2.6}
\]
At a point \(x_0\) where \(u(x_0)\ne0\), choose a ball \(B(x_0,r)\) on which \(|u|\ge c>0\). Apply (2.6) with \(t\xi\), \(t>0\). The left side is at least \(c^2|B(x_0,r)|e^{2t(x_0\cdot\xi-r|\xi|)}\). Taking logarithms, dividing by \(t\), and letting \(t\to\infty\) removes the constant and polynomial factors. Let \(r\downarrow0\) to obtain \(2x_0\cdot\xi\le H_{\operatorname{supp}q}(\xi)\).

The support of a continuous function is the closure of its nonzero set: a nonzero value has a neighborhood detected by a nonnegative test times its conjugate phase, and a zero function on an open set gives zero pairings there. Passing to closures and suprema gives \(2H_{\operatorname{supp}u}\le H_{\operatorname{supp}q}\). The reverse inequality follows from the convolution support inclusion. Theorem 1.1 proves (2.4). \(\square\)

## Polynomial localization prevents cancellation between different factors

Set \(\operatorname{ch}\varnothing=\varnothing\), and use \(\varnothing+E=\varnothing\).

**Theorem 3.1.** For all \(u,v\in\mathcal E'(\mathbb R^n)\), real or complex and including zero,
\[
 \operatorname{ch}\operatorname{supp}(u*v)
 =\operatorname{ch}\operatorname{supp}u+
  \operatorname{ch}\operatorname{supp}v.                          \tag{3.1}
\]
**Proof for smooth compact factors.** The zero cases are immediate. Assume \(u,v\ne0\), and for integers \(j\ge0\) define
\[
 K_j=\operatorname{ch}
 \bigcup_{\deg p+\deg q\le j}
       \operatorname{supp}\bigl((pu)*(qv)\bigr).                  \tag{3.2}
\]
There are only finitely many pairs of monomials \(p=x^\alpha,q=x^\beta\) with \(|\alpha|+|\beta|\le j\). Expanding any pair of polynomials shows that its convolution support is contained in the union of these finitely many monomial-pair supports. Since monomials are themselves allowed, the hull in (3.2) is exactly the hull of that finite union. Thus \(K_j\) is compact or empty. The sets are nested and contained in the fixed compact convex set \(S=\operatorname{ch}\operatorname{supp}u+\operatorname{ch}\operatorname{supp}v\).

We claim, for every \(j\ge1\),
\[
                  2K_j\subset K_{j-1}+K_{j+1}.                   \tag{3.3}
\]
It suffices to prove this for twice the support of each monomial convolution \(f=(pu)*(qv)\), then take convex hulls; the right side is convex. If its total degree is below \(j\), \(f\) is supported in both \(K_{j-1}\) and \(K_{j+1}\). The usual support inclusion for \(f*f\), together with Proposition 2.3 if \(f\ne0\), gives the claim.

For total degree \(j\), at least one monomial has positive degree. Interchange the two factors if needed, and write \(p=x_\ell r\). Put
\[
 a=(ru)*(qv),\qquad b=(ru)*(x_\ell qv),\qquad
 c=(pu)*(x_\ell qv).
\]
Multiplication by the output coordinate in the convolution integral and associativity give
\[
 x_\ell a=f+b,\qquad b*f=a*c,\qquad
 f*f=(x_\ell a)*f-a*c.                                           \tag{3.4}
\]
Here \(a,x_\ell a\) are supported in \(K_{j-1}\), whereas \(f,c\) are supported in \(K_{j+1}\). Both terms in the last expression are therefore supported in \(K_{j-1}+K_{j+1}\). For \(f\ne0\), Proposition 2.3 identifies the hull of \(f*f\) with twice the hull of \(f\). For \(f=0\) there is nothing to prove. This proves (3.3), even if some of the sets are empty.

We next show \(K_0\ne\varnothing\). If it were empty, (3.3) for \(j=1\) would force \(K_1=\varnothing\), and induction would force every \(K_j\) empty. All polynomially weighted convolutions would vanish. Choose \(x_0,y_0\) with \(u(x_0)v(y_0)\ne0\), and introduce
\[
 G_{t,z}(x)=(4\pi t)^{-n/2}
                 \exp\!\left(-\frac{|x-z|^2}{4t}\right),
 \qquad t>0.                                                     \tag{3.5}
\]
For fixed \(t,z\), the partial sums of the exponential series are polynomials in \(x\) and converge with every derivative uniformly on compact sets. Here is a derivative bound: on a compact set let \(R\ge1\) bound \(|x-z|\) and all first and second derivatives of \(Q(x)=|x-z|^2/(4t)\), as well as \(|Q(x)|\). A derivative of order \(m\) of \(Q^k\) is a sum of at most \(C_m(1+k)^m\) products of at most \(k\) factors, each bounded by \(\max(1,R)\). Thus
\[
 \sup|\partial^\alpha(Q^k/k!)|
 \le C_m(1+k)^m R^k/k!,\qquad |\alpha|\le m,
\]
after increasing \(R,C_m\) to include the finitely many \(k<m\). The series of these bounds converges by the ratio test, which follows since the successive ratio tends to zero. This proves the asserted convergence, including all derivatives. Multiplication by \(u\) or \(v\) gives convergence in the corresponding fixed compact test space. The joint fixed-support convolution theorem then implies
\((G_{t,x_0}u)*(G_{t,y_0}v)=0\).

The Gaussian integral \(\int G_{t,z}=1\) is proved in [Fourier foundations, F3](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md) by Tonelli, one-dimensional substitution and the arctangent primitive. Substituting \(x=x_0+\sqrt t\,r\) and using dominated convergence with the integrable density \((4\pi)^{-n/2}e^{-|r|^2/4}\) proves, for every test,
\[
 G_{t,x_0}u\longrightarrow u(x_0)\delta_{x_0},\qquad
 G_{t,y_0}v\longrightarrow v(y_0)\delta_{y_0}.                     \tag{3.6}
\]
The factors stay supported in the fixed compact supports of \(u,v\). Along, for example, \(t=1/k\), joint weak convolution convergence gives the nonzero limit \(u(x_0)v(y_0)\delta_{x_0+y_0}\), contradicting the zero convolution. Hence \(K_0\), and therefore every \(K_j\), is nonempty.

For a fixed \(\xi\), let \(h_j=H_{K_j}(\xi)\). Nesting and (3.3) imply
\[
 0\le h_j-h_{j-1}\le h_{j+1}-h_j,\qquad
 h_j\le H_S(\xi).                                                 \tag{3.7}
\]
If one increment were positive, all subsequent increments would be at least that number and \(h_j\) would grow without bound. Thus every increment is zero, in every direction. Theorem 1.1 gives \(K_j=K_0\).

The same polynomial approximation now shows that each Gaussian-weighted convolution is supported in the closed set \(K_0\): every approximant is, and a distributional limit vanishes on every test in its complement. Equation (3.6) then puts \(x_0+y_0\) in \(K_0\) whenever \(u(x_0)v(y_0)\ne0\). Approximate arbitrary factor support points by nonzero points and use closedness to obtain
\[
 \operatorname{supp}u+\operatorname{supp}v
    \subset K_0=\operatorname{ch}\operatorname{supp}(u*v).         \tag{3.8}
\]
Taking convex hulls and using the ordinary upper support inclusion proves (3.1) for smooth factors.

**Passage to distributions.** Choose a single nonnegative even \(\rho\in\mathcal D\) of integral one, supported in the unit ball, and put \(\rho_\varepsilon(x)=\varepsilon^{-n}\rho(x/\varepsilon)\). Such a profile follows from the scalar smooth cutoff construction and normalization. By U021, Theorems 2.1 and 5.2, \(u_\varepsilon=u*\rho_\varepsilon\) and \(v_\varepsilon=v*\rho_\varepsilon\) are smooth compact functions converging to \(u,v\). The same theorem proves the reflected-test identity; evenness of this fixed profile makes its reflection equal itself.

Let \(K=\operatorname{ch}\operatorname{supp}(u*v)\). Associativity gives
\(u_\varepsilon*v_\varepsilon=(u*v)*(\rho_\varepsilon*\rho_\varepsilon)\).
The smooth result and support inclusion give, with the empty-set convention,
\[
 \operatorname{supp}u_\varepsilon+\operatorname{supp}v_\varepsilon
       \subset K+\overline B(0,2\varepsilon).                     \tag{3.9}
\]
Assume both original factors are nonzero, and choose \(x\in\operatorname{supp}u\), \(y\in\operatorname{supp}v\). In every ball about \(x\) there is a test \(\phi\) with \(u(\phi)\ne0\), by the definition of support and localization. Since \(u_\varepsilon(\phi)\to u(\phi)\), all sufficiently small \(\varepsilon\) have some support point in that ball. The identical assertion holds at \(y\). For each integer \(k\), choose one common \(0<\varepsilon_k<1/k\) small enough for the two balls of radius \(1/k\), and obtain \(x_k,y_k\) in the respective mollified supports, tending to \(x,y\).

Equation (3.9) first proves \(K\ne\varnothing\), since its left side contains \(x_k+y_k\). It then gives points \(z_k\in K\) with \(|x_k+y_k-z_k|\le2\varepsilon_k\). Hence \(z_k\to x+y\), and \(x+y\in K\) because \(K\) is closed. This proves the lower hull inclusion; the upper one was already proved in U021. Zero factors satisfy both sides trivially. \(\square\)

For example,
\((\delta_0-\delta_a)*(\delta_0+\delta_a)=\delta_0-\delta_{2a}\).
When \(a\ne0\), the middle support point disappears, but the hull remains the segment \([0,2a]\).

## Positivity, affine confinement and differential operators

**Proposition 4.1.** Let \(\mu,\nu\) be positive locally finite Borel measures, with at least one compactly supported. Then their convolution is a locally finite positive measure and
\[
              \operatorname{supp}(\mu*\nu)
                   =\operatorname{supp}\mu+\operatorname{supp}\nu. \tag{4.1}
\]
**Proof.** Addition is proper on the two supports: if the first is compact \(F\) and the output lies in a compact \(L\), the second coordinate lies in \(L-F\), also compact. The product integral of \(\phi(x+y)\) is consequently finite for compactly supported bounded \(\phi\); it defines the convolution measure by the product measure and is positive. Its support has the usual upper inclusion. The sum of the supports is closed: for a convergent sequence \(x_j+y_j\), compactness gives a subsequence \(x_j\to x\in F\), whence \(y_j\to y\) in the other closed support.

For the lower inclusion, take support points \(x,y\) and an open neighborhood \(O\) of \(x+y\). Choose small relatively compact open balls \(U,W\) about them whose closure sum is contained in \(O\). A nonnegative smooth cutoff \(\phi\) supported in \(O\) equals one on this compact sum. Both \(\mu(U)\) and \(\nu(W)\) are positive by the definition of measure support, and finite by local finiteness. Thus \((\mu*\nu)(\phi)\ge\mu(U)\nu(W)>0\). Every such \(O\) detects the convolution. If either measure is zero, both sides of (4.1) are empty. \(\square\)

**Corollary 4.2.** The convolution algebra \(\mathcal E'(\mathbb R^n)\) has no zero divisors. If \(u,v\ne0\) are compact distributions and \(\operatorname{supp}(u*v)\) is contained in an affine subspace \(V\), then each factor support is contained in a translate of \(V\).

**Proof.** Both nonzero factor supports are nonempty compact sets. Their hull sum is nonempty, so Theorem 3.1 implies \(u*v\ne0\). If the output is supported in \(V\), its convex hull is also in \(V\). Fix \(a\in\operatorname{supp}u\), \(b\in\operatorname{supp}v\). Theorem 3.1 places every \(x+b\), \(x\in\operatorname{supp}u\), and every \(a+y\), \(y\in\operatorname{supp}v\), in \(V\). Thus the factors lie in \(V-b\) and \(V-a\). \(\square\)

The nonzero hypothesis matters: \(u=0\), \(v=\delta_0+\delta_{e_1}\) has zero output, which is supported in a point, although \(v\) is not. Compactness also matters: the noncompact constant distribution \(1\) is annihilated by the nonzero compact kernel \(\delta_0-\delta_a\), \(a\ne0\).

**Corollary 4.3.** For a nonzero constant-coefficient polynomial \(P(\partial)\) and any compact distribution \(u\),
\[
 \operatorname{ch}\operatorname{supp}P(\partial)u
                  =\operatorname{ch}\operatorname{supp}u.         \tag{4.2}
\]
**Proof.** The distribution \(P(\partial)\delta_0\) has support \(\{0\}\) and is nonzero. Indeed its coefficients are detected separately by monomials times a cutoff equal to one near zero; this is the point-jet independence proved in angular foundations A3. U021, Theorem 1.1, gives \(P(\partial)u=(P(\partial)\delta_0)*u\). Apply Theorem 3.1, including the case \(u=0\). \(\square\)

**Proposition 4.4 (every polynomial on a square).** Let \(h=1_{(-1,1)}\), \(u=h\otimes h\), and \(Q=[-1,1]^2\). Write the unique decomposition
\[
 P(s,t)=c+sA(s)+tB(t)+stC(s,t).                                    \tag{4.3}
\]
Then the exact support of \(P(\partial_x,\partial_y)u\) is as follows.

- If \(c\ne0\), it is \(Q\).
- If \(c=0\) and both \(A,B\ne0\), it is the full boundary of \(Q\).
- If \(c=0\), \(A\ne0\), \(B=0\), it is the two closed vertical edges.
- If \(c=0\), \(A=0\), \(B\ne0\), it is the two closed horizontal edges.
- If \(c=0\), \(A=B=0\), \(C\ne0\), it is the four vertices.
- If \(P=0\), it is empty.

**Proof.** Group the monomials of \(P\) according to which variables have positive exponent; this proves existence and uniqueness of (4.3). The fundamental theorem applied to \(-\int_{-1}^1\phi'\) gives \(h'=\delta_{-1}-\delta_1\). Tensor differentiation therefore yields
\[
 \begin{aligned}
 P(\partial)u
 &=c\,h\otimes h\\
 &\quad+A(\partial_x)(\delta_{-1}-\delta_1)\otimes h\\
 &\quad+h\otimes B(\partial_y)(\delta_{-1}-\delta_1)\\
 &\quad+C(\partial_x,\partial_y)
          [(\delta_{-1}-\delta_1)\otimes(\delta_{-1}-\delta_1)].
 \end{aligned}                                                    \tag{4.4}
\]
These terms give all stated upper inclusions. If \(c\ne0\), the distribution equals the nonzero constant \(c\) on the open square, so support closedness fills \(Q\). If \(c=0\) and \(A\ne0\), in a neighborhood of any relative interior point of a vertical edge the only nonzero term is the normal point jet \(\pm A(\partial_x)\delta_{\pm1}\) times the nonzero interval density in \(y\). Independence of point jets supplies a normal test with nonzero pairing; a tangential nonnegative test of positive integral completes a detecting tensor test. Thus every such edge point belongs to the support. Taking closures adds both corners of each edge, regardless of \(C\). The same argument applies to horizontal edges and \(B\). Finally, if only \(C\ne0\), at each vertex the distribution is the nonzero point jet \(\pm C(\partial_x,\partial_y)\delta_{\text{vertex}}\). Distinct vertices are separated by tests, and point-jet independence prevents cancellation at any one of them. These facts prove all cases. \(\square\)

## Exercises

**Exercise 1 (basic).** For \(c=(3,0)\), \(A=\begin{pmatrix}2&0\\1&2\end{pmatrix}\), let \(K=c+A\overline B(0,1)\). Compute \(H_K\), a supporting point in each nonzero direction, a Cartesian inequality for \(K\), and its area.

**Exercise 2 (basic).** Put \(a=(2,-1)\), \(b=(-1,3)\), \(u=\delta_0-i\delta_a\), \(v=\delta_b+i\delta_{a+b}\). Determine \(u*v\), its support, its hull and its support function.

**Exercise 3 (intermediate).** Let \(\mu=2\delta_{-3}+\delta_2\), and let \(\nu\) be Lebesgue measure on \([0,\infty)\), extended by zero. Explain why convolution exists; calculate its density, support and singular support.

**Exercise 4 (intermediate).** Set
\[
 u(x)=
 \begin{cases}
 e^{-1/(1-x^2)}e^{ix^3},&|x|<1,\\
 0,&|x|\ge1.
 \end{cases}
\]
Prove smoothness and the limit
\(\lim_{t\to\infty}t^{-1}\log\int e^{2tx}|u(x)|^2\,dx=2\).
Use the two directions on the line to find the hull of \(\operatorname{supp}(u*u)\).

**Exercise 5 (intermediate).** For \(a\ne0\), define \(T_a u=\delta_a*u\). Show that \(I-T_a\) is injective on \(\mathcal E'\), but that \((I-T_a)u=\delta_0\) has no compactly supported solution. What happens to the constant distribution?

**Exercise 6 (advanced).** Let \(A=\begin{pmatrix}2&1\\-1&3\end{pmatrix}\), \(c=(4,-2)\), and \(u=1_{c+A(-1,1)^2}\). Define \(L_1=(2,-1)\cdot\nabla_x\), \(L_2=(1,3)\cdot\nabla_x\). Find the exact supports of
\[
 f_1=(L_1+L_1L_2^2)u,\qquad
 f_2=(L_1^2+L_2)u,\qquad
 f_3=L_1L_2u.
\]
Give \(f_3\) as a signed sum of point masses, with its density factor.

**Exercise 7 (advanced).** For \(U=1_{(-1,1)^3}\), decompose an arbitrary polynomial by the set of variables actually appearing in each monomial:
\[
 P=\sum_{S\subset\{1,2,3\}}P_S,\qquad
 P_S=\sum_{\{j:\alpha_j>0\}=S}c_\alpha s^\alpha.
\]
Let \(F_S\) be the union of closed cube faces where each coordinate in \(S\) is an endpoint \(\pm1\). Prove \(\operatorname{supp}P(\partial)U=\bigcup_{P_S\ne0}F_S\). Identify the support for \(P=s_1s_2+s_2s_3\).

**Exercise 8 (advanced).** For linearly independent \(a,b\in\mathbb R^2\), let \(w=\delta_0+\delta_a+\delta_b\). Given \(0\ne g\in\mathcal E'\), show that \(w*u=g\) has at most one compact solution. Obtain a necessary inequality for every directional width of \(\operatorname{ch}\operatorname{supp}g\), and exclude a solution when \(g\) is supported on a line.

## Complete solutions

**Solution 1.** Since \(A^T\xi=(2\xi_1+\xi_2,2\xi_2)\), (1.7) gives
\[
 H_K(\xi)=3\xi_1+\sqrt{4\xi_1^2+4\xi_1\xi_2+5\xi_2^2},\qquad
 x_\xi=c+\frac{AA^T\xi}{|A^T\xi|}\quad(\xi\ne0).
\]
The denominator is nonzero because \(\det A=4\ne0\). The vector \(A^T\xi/|A^T\xi|\) attains equality in Cauchy–Schwarz on the unit ball, so \(x_\xi\) is the stated supporting point. Writing \(X=x_1-3\), \(Y=x_2\), solve \(Ay=(X,Y)\) to obtain \(y=(X/2,Y/2-X/4)\). Thus
\[
 K=\left\{(x_1,x_2):
        \frac{X^2}{4}+\left(\frac Y2-\frac X4\right)^2\le1\right\}.
\]
The linear change-of-variables formula in Banach foundations §15.1 multiplies disk area \(\pi\) by \(|\det A|=4\), so the area is \(4\pi\). In direction \((-1,0)\) the support value is \(-3+2=-1\); this explicitly exhibits a negative support value.

**Solution 2.** Expand the four atom convolutions, using \(\delta_x*\delta_y=\delta_{x+y}\):
\[
 u*v=\delta_b+i\delta_{a+b}-i\delta_{a+b}+(-i)i\delta_{2a+b}
     =\delta_b+\delta_{2a+b}.
\]
The distinct surviving points are \(b=(-1,3)\) and \(2a+b=(3,1)\). Tests supported near either point prove both belong to the support. The hull is \(b+[0,2]a\), and
\[
 H(\xi)=b\cdot\xi+2\max(0,a\cdot\xi).
\]
The canceled middle point affects actual support but not the hull.

**Solution 3.** If an output test is supported in compact \(L\), the possible second coordinates lie in \((L+3)\cup(L-2)\), a compact set. Thus addition is proper on the relevant supports, and the convolution is defined. Evaluating the two translations gives the regular density
\[
              2\,1_{[-3,\infty)}+1_{[2,\infty)}.
\]
Its values away from endpoints are \(0,2,3\) on the three consecutive intervals. Hence its support is \([-3,\infty)\). It is smooth away from \(-3,2\); integration by parts gives derivative \(2\delta_{-3}+\delta_2\).

To check that these atoms prevent local smoothness, a smooth distribution equal to a nonzero point mass near a point would vanish as a function on the punctured neighborhood, by uniqueness of regular distributions (U021, B0). Continuity would make it zero at the point as well, contradicting a test equal to one there. The derivative of a smooth function is smooth, so neither jump point admits a smooth representative. The singular support is exactly \(\{-3,2\}\).

**Solution 4.** On \((-1,1)\), every derivative is a finite sum of a bounded polynomial times powers of \((1-x^2)^{-1}\), multiplied by \(e^{-1/(1-x^2)}e^{ix^3}\). For any integer \(N\ge0\), the exponential series gives \(e^{s/2}\ge(s/2)^{N+1}/(N+1)!\), so \(s^Ne^{-s}\to0\) as \(s\to\infty\). Thus all these derivatives tend to zero at both endpoints. Extending them by zero gives smoothness of \(u\): inductively, the fundamental theorem on intervals approaching an endpoint shows the extended derivative is the derivative of the extended previous function. The function is nonzero at every interior point, so its support is \([-1,1]\).

For \(t>0\),
\[
 \int e^{2tx}|u|^2\,dx\le e^{2t}\|u\|_2^2.
\]
For any \(0<\delta<1\), choose a closed interval \(I\) of positive length inside \((1-\delta,1)\). Its positive minimum \(c_I=\min_I|u|\) gives the opposite estimate
\[
 \int e^{2tx}|u|^2\,dx\ge c_I^2|I|e^{2t(1-\delta)}.
\]
Taking logarithms, dividing by \(t\), and sending \(t\to\infty\) bounds the lower and upper limits between \(2(1-\delta)\) and \(2\). Letting \(\delta\downarrow0\) proves the claimed limit. Replacing \(x\) by \(-x\) gives the corresponding value two in the opposite direction. Proposition 2.3 now yields \(\operatorname{ch}\operatorname{supp}(u*u)=[-2,2]\).

**Solution 5.** The compact kernel \(k=\delta_0-\delta_a\) is nonzero, as a test near zero and away from \(a\) shows. By Corollary 4.2, \(k*u=0\) for compact \(u\) forces \(u=0\). If \(k*u=\delta_0\), then \(u\ne0\) and Theorem 3.1 would give
\[
             \{0\}=[0,a]+\operatorname{ch}\operatorname{supp}u.
\]
Choose any \(x\) in the nonempty second set. The right side contains the distinct points \(x,x+a\), a contradiction. On the other hand, changing variables in the pairing with the constant distribution proves \(T_a1=1\), so \((I-T_a)1=0\).

**Solution 6.** In the affine coordinates \(x=c+Ay\), \(\partial_{y_j}\phi(c+Ay)=L_j\phi(c+Ay)\). The determinant is seven. Pairing the indicator with a test and then differentiating by integration by parts therefore transports the \(y\)-coordinate derivatives with the common density factor seven.

The three polynomials in these coordinates are \(s+st^2\), \(s^2+t\), \(st\). Proposition 4.4 gives for \(f_1\) the images of the two closed vertical edges of the square, for \(f_2\) the whole parallelogram boundary, and for \(f_3\) precisely its four vertices. An invertible affine map preserves support under this transport: tests in either coordinate system correspond bijectively by composition, and the constant density is nonzero.

In particular,
\[
 \begin{aligned}
 f_3
 &=7\sum_{\varepsilon_1,\varepsilon_2=\pm1}
       \varepsilon_1\varepsilon_2\,
         \delta_{c+A(\varepsilon_1,\varepsilon_2)}\\
 &=7\bigl(\delta_{(1,-4)}-\delta_{(3,2)}
                 -\delta_{(5,-6)}+\delta_{(7,0)}\bigr).
 \end{aligned}
\]
Indeed \(h'=\delta_{-1}-\delta_1\); its coefficient at \(\varepsilon\) is \(-\varepsilon\). Multiplying the two coefficients gives \(\varepsilon_1\varepsilon_2\), and the affine integral retains the factor seven.

**Solution 7.** For each positive exponent \(\alpha_j\), differentiating \(h\) that many times gives \(\partial^{\alpha_j-1}(\delta_{-1}-\delta_1)\); for exponent zero it leaves \(h\). Consequently each grouped term is supported in \(F_S\), proving the upper inclusion.

For the reverse inclusion, it suffices to consider the inclusion-minimal sets \(S\) with \(P_S\ne0\). Every other such set \(T\) contains a minimal one, and \(F_T\subset F_S\) when \(S\subset T\). Fix a relative interior point of a face in \(F_S\). The coordinates outside \(S\) lie strictly inside \((-1,1)\). A term with a positive exponent in any of those coordinates vanishes on a small neighborhood of this point. A term with derivative set strictly contained in \(S\) is absent by minimality. Thus only \(P_S\) can remain.

The remaining distribution is, in the normal coordinates, a point-jet polynomial whose coefficients are \(c_\alpha\) times the common nonzero sign \(\prod_{j\in S}(-\varepsilon_j)\), and whose derivative orders are \((\alpha_j-1)_{j\in S}\). Distinct \(\alpha\)'s give distinct orders; the polynomial is nonzero by point-jet independence. Choose a normal test detecting it in an arbitrarily small neighborhood, and tangential tests with positive integrals in the other coordinates. The resulting tensor test detects the distribution. Hence every relative interior point belongs to its support; taking closures includes the entire face. For \(S=\varnothing\), the same argument is simply the nonzero constant density on the cube interior. If no \(P_S\) is nonzero, both proposed sets are empty.

For \(P=s_1s_2+s_2s_3\), the two minimal sets are \(\{1,2\}\) and \(\{2,3\}\). The support is
\[
 \{x_1,x_2\in\{-1,1\},\ |x_3|\le1\}
 \ \cup\
 \{|x_1|\le1,\ x_2,x_3\in\{-1,1\}\}.
\]
These are the four edges parallel to the third axis and the four parallel to the first. They contain all eight vertices. The interiors of the four edges parallel to the second axis are excluded. Their convex hull is the full cube, as Corollary 4.3 also requires.

**Solution 8.** The difference of two compact solutions is annihilated by the nonzero compact kernel \(w\); Corollary 4.2 makes the difference zero. A solution for \(g\ne0\) must itself be nonzero. Let \(T=\operatorname{ch}\{0,a,b\}\) and \(K=\operatorname{ch}\operatorname{supp}u\). Theorem 3.1 gives \(\operatorname{ch}\operatorname{supp}g=T+K\).

For a nonempty compact \(E\), its directional width is \(W_E(\xi)=H_E(\xi)+H_E(-\xi)\). This is the maximum of \(x\cdot\xi\) minus its minimum, so it is nonnegative. Applying the support-sum identity yields
\[
 \begin{aligned}
 W_{\operatorname{supp}g}(\xi)
 &=W_T(\xi)+W_K(\xi)\ge W_T(\xi),\\
 W_T(\xi)
 &=\max(0,a\cdot\xi,b\cdot\xi)-\min(0,a\cdot\xi,b\cdot\xi).
 \end{aligned}
\]
For \(\xi\ne0\), this last width is strictly positive: if it were zero, all three scalar products would equal zero, so \(\xi\) would be perpendicular to the basis \(a,b\), a contradiction. A nonempty compact set in an affine line has zero width in a nonzero normal direction. Thus a line-supported \(g\ne0\) cannot admit a compact solution. The inequality is a necessary condition; the argument makes no assertion of sufficiency.

## Programme proof locations and freely accessible sources

- [Convolution as addition of supports](convolution-as-addition-of-supports.md), B0–B3 and Theorems 1.1, 2.1, 3.1, 3.2, 5.2: localization, tensors, proper convolution, support inclusion, smoothness, associativity, joint limits on fixed supports and normalized mollifiers. These are the exact earlier proofs used throughout Sections 2–4 and the solutions.
- [Angular foundations](../prerequisites/U011-free-foundations/angular-foundations-U018.md), A3: independence of arbitrary finite point jets, used in Corollary 4.3, Proposition 4.4 and Solution 7.
- [Schwartz and Fourier foundations](../prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md), F3: the full real Gaussian mass proof used in (3.5)–(3.6).
- [Metric foundations](../prerequisites/U011-free-foundations/metric-foundation-bridges.md), §§12–13: finite-dimensional compactness, completeness of the real numbers, scalar fundamental theorem, exponential series and smooth cutoffs. [Stable algebra foundations](../prerequisites/U011-free-foundations/stable-prerequisite-bridges.md), §10: finite-dimensional linear algebra and determinants. [Banach foundations](../prerequisites/U011-free-foundations/banach-foundation-bridges.md), §§15.1–15.3, 16.1–16.2: dominated convergence, Fubini–Tonelli, Cauchy–Schwarz, linear changes of variables and product measures. These supplied components retain their stated licenses.
- Andrew Comech, *Solutions with compact time spectrum to nonlinear Klein–Gordon and Schrödinger equations and the Titchmarsh theorem for partial convolution*, [freely accessible author preprint, arXiv:1810.09047v4](https://arxiv.org/pdf/1810.09047), December 30, 2020, §§2.3–2.5, pp. 7–9. The scalar self-convolution mechanism and polynomial increment argument in Lemmas 5–8 guide Sections 2–3 here. The present lesson supplies the conjugate-reflection identity, all-dimensional derivative estimate, finite polynomial hull argument, Gaussian localization and fixed-profile distributional limit in full; no partial-convolution theorem or external proof is assumed.
