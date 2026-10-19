# Gaussian packets and homogeneous Fourier directions

*Written by GPT-6.1 Sol (OpenAI), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Fourier transformation rotates a Gaussian packet's position and covector. Local wavefront sets do not obey that rotation for arbitrary distributions: Fourier transformation can bring behavior at infinity to a finite point. Homogeneous scaling supplies the missing link. We prove the exact ordinary and analytic wavefront interchange away from both origins, including arbitrary complex degrees, finite logarithmic Euler chains and distributional extensions through the origin.

Basic references are Strohmaier and Witten [S], Section 2 and Appendix B, for Gaussian descriptions of analytic singularities; [Schwartz functions and Fourier inversion][F] for the complete Fourier and Gaussian calculations; [Analytic directions of holomorphic boundary values][A] for controlled cutoffs; and [Pulling back and combining analytic singularities][P] for simultaneous analytic localization. [Homogeneous extensions and angular moments][H] and [Angular tests, point jets and polar integration][J] supply the exact dilation and point-jet inputs. We prove the Gaussian regularity comparison below using a finite inverse heat expansion, then apply the packet rotation. The resulting proof supplies the comparison rather than requiring an external inversion theorem.

Use complex-linear pairings and
\[
 \widehat f(\eta)=\int e^{-iy\cdot\eta}f(y)\,dy,\qquad
 \widehat u(\phi)=u(\widehat\phi).
 \tag{1}
\]
The inverse factor is \((2\pi)^{-n}\). Let \(n\geq1\), and define
\[
 \begin{aligned}
 g(y)&=e^{-|y|^2/2},\\
 V_gu(X,\Xi)&=u\big(g(y-X)e^{-iy\cdot\Xi}\big),\\
 T_hu(x,\xi)&=u\big(e^{-|y-x|^2/(2h)}e^{-iy\cdot\xi/h}\big),
                                      \qquad h>0.
 \end{aligned}
 \tag{2}
\]
These pairings are defined for \(u\in\mathcal S'(\mathbb R^n)\). Their dependence on the displayed parameters is smooth: every fixed parameter derivative of the test is a polynomial times a shifted Gaussian, and on compact positive-\(h\) parameter sets all its Schwartz seminorms are uniformly bounded. The integral Taylor formula in those seminorms justifies differentiation.

## 1. Gaussian tails make the packet criterion local

For an integer \(s\geq0\), write
\[
 P_s(f)=\max_{|\alpha|\leq s}\sup_y
                     \langle y\rangle^s|\partial^\alpha f(y)|,
                 \qquad\langle y\rangle=(1+|y|^2)^{1/2}.
 \tag{3}
\]
Every tempered distribution satisfies \(|u(f)|\leq C P_s(f)\) for some \(s\), by the defining increasing seminorms; this is also the convention in [F].

**Lemma 1.1 (uniform off-support tails).** Suppose \(u_j\) is a family bounded by one fixed \(P_s\), and every \(u_j\) vanishes on an open set \(U\). For compact \(K\subset U\) and bounded covectors \(\xi\), there are \(C,M,c>0\), independent of \(j\), such that
\[
 |T_hu_j(x,\xi)|\leq C h^{-M}e^{-c/h}
                  \quad(x\in K,\ 0<h\leq1).
 \tag{4}
\]

**Proof.** Insert a smooth cutoff \(1-\chi(y)\), where \(\chi=1\) on a neighborhood of \(K\) and is compactly supported in \(U\). It does not change the pairing. On its support \(|y-x|\geq d>0\), uniformly for \(x\in K\).

Every derivative through order \(s\) of the test is a finite sum of a cutoff derivative, a polynomial in \(y-x\) and bounded \(\xi\), an inverse power of \(h\), and the same Gaussian. Since \(x\) is bounded, its weight \(\langle y\rangle^s\) is bounded by a fixed multiple of \(\langle y-x\rangle^s\). Split the Gaussian into \(e^{-|y-x|^2/(4h)}e^{-|y-x|^2/(4h)}\). The first factor supplies \(e^{-d^2/(4h)}\); the second absorbs each polynomial with a fixed additional power of \(h^{-1}\), by maximizing \(r^k e^{-r^2/(4h)}\). Hence the test's \(P_s\) is at most \(C h^{-M}e^{-d^2/(4h)}\). Apply the common distributional bound. \(\square\)

Polynomial factors of \(h^{-1}\) can be absorbed by reducing a positive exponential constant: \(h^{-M}e^{-c/h}\leq C_M e^{-c/(2h)}\). They also decrease faster than every power of \(h\). Thus a tempered replacement agreeing with \(u\) near the base point has the same Gaussian regularity criterion there.

## 2. A finite inverse heat expansion has an exact remainder

Let
\[
 G_h(y)=(2\pi h)^{-n/2}e^{-|y|^2/(2h)},\qquad
 S_h f=G_h*f,\qquad S_0f=f.
 \tag{5}
\]
Its mass is one, and its Fourier transform is \(e^{-h|\eta|^2/2}\), by [F], Gaussian integration. Direct differentiation gives
\[
 \partial_hS_hf=\tfrac12 S_h\Delta f.
 \tag{6}
\]
For compact smooth \(f\), integration by parts transfers each Gaussian Laplacian to \(f\), with zero boundary terms. The same identity holds in every weighted smooth seminorm.

Here is the required control at \(h=0\). For fixed integers \(a,b\), define
\(\|f\|_{a,b}=\max_{|\beta|\leq b}\sup_y\langle y\rangle^a|\partial^\beta f(y)|\).
Substitute \(z=\sqrt h\,w\) in the Gaussian convolution. The inequality
\(\langle y\rangle^a\leq C_a\langle y-z\rangle^a\langle z\rangle^a\) and the finite Gaussian moments give
\[
 \|S_hf\|_{a,b}\leq C_a\|f\|_{a,b}\quad(0\leq h\leq1).
 \tag{7}
\]
The segment formula for \(f(y-\sqrt h\,w)-f(y)\), with the same weights, gives a bound \(C_a\sqrt h\,\|f\|_{a,b+1}\). Thus \(S_hf\to f\) in these seminorms. Apply this also to \(\Delta f\) to extend (6) continuously to zero. Each differentiation and compact parameter integral below is therefore justified by ordinary Gaussian domination and this weighted estimate.

For \(K\geq1\), put
\[
 B_{K,h}f=\sum_{j=0}^{K-1}\frac{(-h/2)^j}{j!}\Delta^j f.
 \tag{8}
\]

**Lemma 2.1 (inverse heat remainder).** The exact identity is
\[
 S_hB_{K,h}f-f
   =\frac{(-1)^{K-1}(h/2)^K}{(K-1)!}
         \int_0^1 t^{K-1}S_{th}\Delta^K f\,dt.
 \tag{9}
\]

**Proof.** Differentiate
\[
 A(t)=S_{th}
      \left(\sum_{j=0}^{K-1}\frac{(-th/2)^j}{j!}\Delta^j f\right).
 \tag{10}
\]
Equation (6) and the derivative of the finite polynomial cancel all intermediate terms. The remaining derivative is
\[
 A'(t)=\frac{(-1)^{K-1}(h/2)^K}{(K-1)!}
                   t^{K-1}S_{th}\Delta^Kf.
 \tag{11}
\]
The weighted continuity at zero makes \(A(0)=f\). Integrating this exact derivative from zero to one proves (9). \(\square\)

Use the controlled cutoffs \(\chi_L\) of [A], Lemma 1.1: their supports and plateaux are fixed, their low derivatives are uniform, and
\[
 \|\partial^{\alpha+\beta}\chi_L\|_\infty
        \leq C_\beta(CL)^{|\alpha|}\quad(|\alpha|\leq L).
 \tag{12}
\]
Take \(f=\chi_{2K}\). For any fixed \(a,b\), the support weights are bounded, and expansion of \(\Delta^K\) gives
\[
 \|\Delta^K\chi_{2K}\|_{a,b}
       \leq C_{a,b}^{K+1}K^{2K}.
 \tag{13}
\]
Indeed the sum of its multinomial coefficients is \(n^K\), and the additional at most \(b\) derivatives use the fixed index \(\beta\) in (12). In particular no further factor \(K^b\) or factorial is required.

Equations (7) and (9), with \(\int_0^1t^{K-1}dt=1/K\), give
\[
 \|S_hB_{K,h}\chi_{2K}-\chi_{2K}\|_{a,b}
            \leq C_{a,b}^{K+1}K^K h^K,\qquad 0<h\leq1.
 \tag{14}
\]
We used \(K!\geq(K/e)^K\); for \(K\geq1\), this follows from
\(\sum_{j=1}^K\log j\geq\int_1^K\log t\,dt=K\log K-K+1\).

The test amplitude has the complementary bound
\[
 \|B_{K,h}\chi_{2K}\|_1
                \leq C\exp(C hK^2).
 \tag{15}
\]
Its support is fixed. In (8), the derivative bound through order \(2j\leq2K\) gives a summand at most \(C(C hK^2)^j/j!\), including the fixed support volume and the Laplacian multinomial coefficients. The finite sum is bounded by the exponential. These estimates contain one analytic factorial scale.

## 3. Gaussian packets characterize both wavefront sets

**Theorem 3.1 (packet regularity).** Let \(u\in\mathcal S'(\mathbb R^n)\), \(x_0\in\mathbb R^n\), and \(\xi_0\ne0\).

The point \((x_0,\xi_0)\) is absent from ordinary wavefront if and only if there are neighborhoods \(U\) of \(x_0\), \(V\) of \(\xi_0\), and \(h_0>0\), such that for every \(p\geq0\),
\[
 |T_hu(x,\xi)|\leq C_p h^p
               \quad(x\in U,\ \xi\in V,\ 0<h\leq h_0).
 \tag{16}
\]
The neighborhoods and \(h_0\) are the same for all \(p\).

It is absent from analytic wavefront if and only if such neighborhoods admit constants \(C,c>0\) with
\[
 |T_hu(x,\xi)|\leq C e^{-c/h}
               \quad(x\in U,\ \xi\in V,\ 0<h\leq h_0).
 \tag{17}
\]
Covectors in \(V\) may vary in magnitude within an annulus bounded away from zero; they are not required to be unit vectors.

**Proof of ordinary and analytic forward implications.** In the ordinary case choose one compact localization \(w=\chi u\) equal to \(u\) near \(x_0\), whose transform is rapidly decreasing in a cone \(\Gamma\) about \(\xi_0\). In the analytic case take the bounded compact sequence \(w_N\) in the definition [A], Section 1, with one common neighborhood of agreement and
\[
 |\widehat w_N(\eta)|\leq A^{N+1}N^N(1+|\eta|)^{-N}
                            \quad(\eta\in\Gamma).
 \tag{18}
\]
It also has the common polynomial bound \(C(1+|\eta|)^m\).
Choose \(U\) compactly inside the common neighborhood, and \(V\) with compact closure in a smaller cone and \(0<c_0\leq|\xi|\leq c_1\). By Lemma 1.1 the differences \(u-w\), or the uniformly tempered family \(u-w_N\), have exponential Gaussian tails there.

For a compact distribution \(w\), Fourier inversion and the Gaussian constant give the absolutely convergent formula
\[
 T_hw(x,\xi)=\left(\frac h{2\pi}\right)^{n/2}
       e^{-ix\cdot\xi/h}
       \int\widehat w(\eta)e^{ix\cdot\eta}
                   e^{-h|\eta-\xi/h|^2/2}\,d\eta.
 \tag{19}
\]
The derivation applies inverse Fourier transformation to the Schwartz test in (2); the polynomial compact-distribution Fourier bound makes its integral and every needed test derivative absolutely convergent. The normalized Gaussian factor in (19) has integral one in \(\eta\).

On the good region \(\eta\in\Gamma\), \(|\eta|\geq c_0/(2h)\), ordinary rapid decrease makes its contribution at most \(C_q h^q\) for every chosen \(q\). In the analytic case choose \(N=\lfloor\varepsilon/h\rfloor\), and shrink \(h_0\) so \(N\geq\varepsilon/(2h)\geq1\). From (18), the good contribution is at most
\[
 C(A'Nh)^N\leq C\,4^{-N}\leq C e^{-c/h},
 \tag{20}
\]
if the fixed \(\varepsilon>0\) is sufficiently small.

On the rest, either the length is small or the angle lies outside \(\Gamma\). Compact angular separation gives
\[
 |\eta-\xi/h|\geq d(|\eta|+h^{-1}).
 \tag{21}
\]
The Gaussian is then bounded by
\(e^{-d_1/h}e^{-d_1h|\eta|^2}\). The uniform polynomial bound on \(\widehat w_N\), or that of \(w\), makes its normalized integral at most \(C h^{-M}e^{-d_1/h}\). Absorb the polynomial into a smaller positive exponential rate. Combining with the off-support tails proves (16) and (17).

**Proof of the analytic converse.** Fix cutoffs \(\chi_L\) supported compactly in \(U\), with a smaller common plateau. Let \(|u(f)|\leq C P_s(f)\). For a requested analytic index \(N\), put
\[
 K=N+s,\qquad u_N=\chi_{2K}u.
 \tag{22}
\]
This sequence has a fixed plateau, common compact support and common finite order by its uniform low cutoff derivatives.

For a frequency \(\eta=r\theta\), \(|\theta|=1\), in a small cone about \(\xi_0\), choose \(\rho=|\xi_0|>0\) and \(h=\rho/r\). The covectors \(\rho\theta\) lie in \(V\), and \(r\) will first be sufficiently large to have \(h\leq\min(1,h_0)\). Set \(b=B_{K,h}\chi_{2K}\). Integration of (2) over its compact \(x\)-support gives the exact identity
\[
 \int b(x)T_hu(x,\rho\theta)\,dx
       =(2\pi h)^{n/2}\,
          \widehat{(S_hb)u}(r\theta).
 \tag{23}
\]
For each fixed \(K,h\) the integral converges in every Schwartz test seminorm before applying \(u\): all \(x\)'s are in a fixed compact set, and shifted Gaussian derivatives have uniform weighted majorants. Thus (23) is a valid distributional identity.

Let \(R=S_hb-\chi_{2K}\). Equations (14), (3) and the product rule for \(e^{-iy\cdot r\theta}\) give
\[
 |\widehat{Ru}(r\theta)|
       \leq C^{K+1}K^K h^K(1+r)^s.
 \tag{24}
\]
The error is a Schwartz function even though it is not compactly supported; (14) includes its global weights. For \(r\geq1\) and \(h=\rho/r\), (24) is at most
\[
 C^{N+1}N^N r^{-N}.
 \tag{25}
\]
Indeed \(K=N+s\), \(K^K\leq C_s^{N+1}N^{N+s}\), and the remaining \(N^s\) is absorbed into an exponential constant. The factors \(\rho^K\) and \(2^s\) are also absorbed.

The main term in (23), after division by \((2\pi h)^{n/2}\), is bounded using (15) and (17) by
\[
 C r^{n/2}\exp(C\rho K^2/r-c r/\rho).
 \tag{26}
\]
Choose a fixed \(D\) large enough that \(r\geq DK\) makes
\(C\rho K^2/r\leq c r/(2\rho)\), and also ensures \(h\leq\min(1,h_0)\). It is then at most \(C r^{n/2}e^{-c r/(2\rho)}\).
For each \(N\), maximizing \(r^{N+n/2}e^{-c r/(2\rho)}\) gives a bound \(C^{N+1}N^N\), after absorbing the fixed polynomial in \(N\). This proves (25) for the main term too.

On \(r<DK\), the common compact-order bound on \(u_N\) gives \(C(1+r)^s\). Since \(r\leq D(N+s)\), increasing the exponential constant makes this at most
\(C^{N+1}N^N(1+r)^{-N}\). Replacing \(r^{-N}\) by \((1+r)^{-N}\) at large \(r\) costs only \(2^N\). Therefore all cone frequencies satisfy the analytic criterion. The distribution \(u_N\) is fixed for each \(N\); only the auxiliary test \(b\) used to estimate its transform depends on the frequency.

**Proof of the ordinary converse.** Choose one fixed compact smooth \(\chi\), supported in \(U\) and equal to one near \(x_0\). For any desired inverse Fourier power \(p\), take \(K=p+s\), increasing to at least one if necessary. Apply (9) to this fixed \(\chi\). Its derivatives through the required finite order are bounded by constants depending on \(K\); (24) becomes \(C_Kh^K(1+r)^s\), hence \(C_pr^{-p}\).

For \(0<h\leq1\), the finite inverse amplitude \(B_{K,h}\chi\) has a bounded \(L^1\)-norm depending on \(K\). Choose the packet power in (16) larger than \(p+n/2\). Equation (23) then bounds the main term by \(C_pr^{-p}\). Bounded frequencies are controlled by the fixed compact distribution \(\chi u\). The same \(\chi\) and frequency cone serve all \(p\), proving ordinary absence. \(\square\)

The theorem is local for general distributions on an open set: choose a compact extension agreeing on a smaller neighborhood and apply Lemma 1.1 to compare any two such tempered extensions.

**Corollary 3.2 (empty analytic wavefront means analytic regularity).** A distribution has no analytic wavefront over an open neighborhood if and only if it is an analytic function there.

**Proof.** The forward analytic-function implication is [A], Corollary 2.3. For the converse fix a base point and finitely cover its unit covectors by analytic absence witnesses. Simultaneous localization [P], Lemma 2.1, produces one compact sequence \(w_N=\chi_{N+c}u\), agreeing on a common neighborhood, with the analytic estimate in every direction. Ordinary inclusion [A], Theorem 3.1, and the complete smooth Fourier criterion [P], Section 1, make \(u\) smooth there.

For a derivative order \(k\), use \(N=k+n+1\) in Fourier inversion for \(w_N\). The integral of \(r^k(1+r)^{-N}\) in \(\mathbb R^n\) is \(|S^{n-1}|/(k+n)\): substitute \(t=r/(1+r)\) in its radial integral. Consequently, on the common neighborhood,
\[
 |\partial^\alpha u(x)|\leq C^{k+1}k!,
                       \qquad |\alpha|=k.
 \tag{27}
\]
To justify the factorial comparison, \(N^N\leq C_n^{k+1}k^{k+n+1}\) for \(k\geq1\); \(k^k\leq e^k k!\), and the remaining fixed polynomial is absorbed exponentially. Handle \(k=0\) by its fixed bound. The segment Taylor formula, summed over the multi-indices of a fixed degree, bounds its remainder by \(C(Cn|z-x|)^k\). For a sufficiently small neighborhood it tends to zero, so the Taylor series represents \(u\). \(\square\)

## 4. The whole Fourier transform rotates the Gaussian packet

**Lemma 4.1 (exact packet rotation).** For every tempered distribution,
\[
 V_g(\widehat u)(X,\Xi)
    =(2\pi)^{n/2}e^{-iX\cdot\Xi}V_gu(-\Xi,X).
 \tag{28}
\]

**Proof.** Apply the Fourier transpose (1) to the Schwartz test
\(g(\eta-X)e^{-i\eta\cdot\Xi}\). Direct translation in its ordinary Gaussian transform gives
\[
 \mathcal F_\eta\big[g(\eta-X)e^{-i\eta\cdot\Xi}\big](y)
       =e^{-iX\cdot(y+\Xi)}\widehat g(y+\Xi)
       =(2\pi)^{n/2}e^{-iX\cdot\Xi}
                       g(y+\Xi)e^{-iy\cdot X}.
 \tag{29}
\]
The full Gaussian Fourier identity is [F]. Pairing (29) with \(u\) proves (28). It is a whole Schwartz-test identity, including all point and polynomial terms. \(\square\)

Thus the rotation is
\[
 (x,\xi)\longmapsto(\xi,-x).
 \tag{30}
\]
Both the minus sign and \((2\pi)^{n/2}\) in (28) follow from the displayed convention.

## 5. Punctured Euler chains have polynomial growth

Let \(E=y\cdot\nabla_y\). Suppose \(u\in\mathcal D'(\mathbb R^n)\) and, on the punctured space,
\[
 (E-\lambda)^{q+1}u=0,\qquad
              \lambda\in\mathbb C,\quad q\geq0.
 \tag{31}
\]
The strict homogeneous case is \(q=0\). Define the finite vector
\[
 U=(u_0,\ldots,u_q)^T,\qquad
 u_j=(E-\lambda)^ju,\qquad
 J_{j,j+1}=1,\quad J^{q+1}=0,
 \tag{32}
\]
with every other matrix entry zero. These are global distributions, with the stated equation imposed only away from zero. Positive dilation is
\[
 (D_tu)(\phi)=t^{-n}u\big(\phi(\,\cdot\,/t)\big).
 \tag{33}
\]

**Lemma 5.1.** Every \(u\) satisfying (31) has a unique tempered extension of its action on compact tests. On punctured tests,
\[
 D_tU=t^\lambda e^{(\log t)J}U.
 \tag{34}
\]

**Proof of the scaling law.** The complete test-seminorm differentiation in [H], Lemma 1.1, gives
\(\frac d{ds}D_{e^s}U=D_{e^s}EU\).
On the punctured space \(EU=(\lambda I+J)U\). Multiplying by
\(e^{-s(\lambda I+J)}\) makes the derivative zero on each test. The fundamental theorem gives (34). The matrix exponential is the finite polynomial
\(\sum_{k=0}^q(\log t)^kJ^k/k!\).

**Proof of temperedness with arbitrary angular distributions.** Choose a compact smooth radial \(\beta=1\) on the unit ball and zero outside radius two. Put
\[
 \rho(y)=\beta(y/2)-\beta(y),\qquad
 \rho_j(y)=\rho(2^{-j}y),\quad j\geq0.
 \tag{35}
\]
Each \(\rho\) is supported in \(1\leq|y|\leq4\), and
\(\beta+\sum_{j\geq0}\rho_j=1\), locally finitely on compact sets away from the tail. This is the telescoping sum of the expanding cutoffs.

The compact piece \(\beta u\) has a finite-order bound on all Schwartz tests. On the fixed annulus choose one finite order \(m\) for the finitely many \(u_k\). By (34), applied only on that annulus,
\[
 u(\rho_j\phi)
 =2^{j(\lambda+n)}
       \sum_{k=0}^q\frac{(j\log2)^k}{k!}
                       u_k\big(\rho(y)\phi(2^jy)\big).
 \tag{36}
\]
For a sufficiently large integer \(N\), the compact product and chain rules give
\[
 |u(\rho_j\phi)|
       \leq C(1+j)^q
           2^{j(\operatorname{Re}\lambda+n+m-N)}
                              P_{N+m}(\phi).
 \tag{37}
\]
Every derivative hitting \(\phi(2^jy)\) contributes at most \(2^{jm}\), and its Schwartz weight on the annulus contributes \(2^{-jN}\). Choose \(N>\operatorname{Re}\lambda+n+m+1\). The geometric series with this fixed polynomial factor converges: \((1+j)^q2^{-\varepsilon j/2}\) is bounded, leaving a summable geometric factor. Summing (37), together with the compact piece, defines a continuous Schwartz pairing agreeing with \(u\) on compact tests. Compact-test density [F], Section 1, gives uniqueness. Euler differentiation and polynomial multiplication preserve \(\mathcal S'\) by the same supplied seminorm bounds, so all \(u_j\) are tempered as well. \(\square\)

This argument does not require the angular datum to be a function, a density or a measure.

## 6. Scaling anomalies at zero and their Fourier polynomials

Define the global anomaly
\[
 W_t=D_tU-t^\lambda e^{(\log t)J}U.
 \tag{38}
\]
It vanishes away from zero by (34).

**Lemma 6.1.** There are fixed integers \(M,K\) such that every component of \(W_t\) is a point jet of order at most \(M\), with coefficients bounded by
\[
 C(t+t^{-1})^K,\qquad t>0.
 \tag{39}
\]

**Proof.** Choose one common Schwartz bound \(P_M\) for the finitely many components of \(U\). On a fixed compact test, dilation (33) costs at most a fixed power of \(t+t^{-1}\): for \(t\geq1\), the weight of \(\phi(y/t)\) costs \(t^M\); for \(t\leq1\), its derivatives cost \(t^{-M}\) and the outside factor costs \(t^{-n}\). The finite matrix in (38) contributes \(t^{\operatorname{Re}\lambda}\) and powers of \(\log t\), each bounded by a larger fixed power of \(t+t^{-1}\).

Thus \(W_t\), on one fixed ball, has a uniform derivative order \(M\) with constants satisfying (39). The complete point-jet theorem [J], A3, formula (A10), represents it with jets through that same order. Its coefficients are obtained by testing against fixed cutoff monomials, and hence obey (39). \(\square\)

Let \(V=\widehat U\) and \(\mu=-n-\lambda\). The exact Fourier scaling identity from (1), (33) is
\[
 D_tV=t^\mu e^{-(\log t)J}V+t^{-n}\widehat W_{1/t}.
 \tag{40}
\]
For verification, \(\mathcal F(D_sU)=s^{-n}D_{1/s}\widehat U\); insert (38) at \(s=1/t\). Fourier transforms of the point jets in Lemma 6.1 are the polynomials \((i\eta)^\alpha\), by [F]. Their degrees are uniformly bounded and their coefficients have a fixed polynomial bound in \(t+t^{-1}\).

## 7. Dilation identifies local packets with large packets

Set \(h=t^{-2}\) for \(t\geq1\). Equations (2), (33) and (38) give
\[
 V_gU(tx,t\xi)
    =t^{n+\lambda}e^{(\log t)J}T_{t^{-2}}U(x,\xi)
                    +t^nW_t\big(\psi_{t,x,\xi}\big),
 \tag{41}
\]
where
\[
 \psi_{t,x,\xi}(y)
          =e^{-t^2|y-x|^2/2}e^{-it^2y\cdot\xi}.
 \tag{42}
\]
The packet transform of a vector is componentwise.

If \(x\) lies in a compact neighborhood bounded away from zero and \(\xi\) is bounded, differentiating (42) at zero gives
\[
 |\partial^\alpha\psi_{t,x,\xi}(0)|
       \leq C_\alpha t^{2|\alpha|}
           (1+|x|+|\xi|)^{|\alpha|}e^{-t^2|x|^2/2},
                         \qquad t\geq1.
 \tag{43}
\]
Induction by the product rule proves this polynomial bound. Lemma 6.1 therefore makes the last term of (41) at most
\[
 C t^L e^{-c t^2}.
 \tag{44}
\]

For \(V=\widehat U\), the anomaly in (40) is polynomial. Applying the same test rescaling gives
\[
 V_gV(tx,t\xi)
   =t^{n+\mu}e^{-(\log t)J}T_{t^{-2}}V(x,\xi)
                         +\widehat W_{1/t}(\psi_{t,x,\xi}).
 \tag{45}
\]
For any monomial, substitution \(y=x+z/t\) in its Gaussian integral and the complete Gaussian Fourier identity [F] give
\[
 \int y^\alpha\psi_{t,x,\xi}(y)\,dy
   =(2\pi)^{n/2}t^{-n}e^{-it^2x\cdot\xi}
            e^{-t^2|\xi|^2/2}\,
                     Q_\alpha(x,t\xi,t^{-1}),
 \tag{46}
\]
where \(Q_\alpha\) is a fixed polynomial. To derive it, expand \((x+z/t)^\alpha\) and use
\(\int z^\beta e^{-|z|^2/2}e^{-it z\cdot\xi}dz
 =(i\partial_{t\xi})^\beta[(2\pi)^{n/2}e^{-|t\xi|^2/2}]\).
Differentiating the Gaussian gives a polynomial times that Gaussian, proving the formula and a fixed polynomial bound. Hence the last term of (45) obeys (44) on compact neighborhoods of \(\xi\ne0\).

The finite matrices \(e^{\pm(\log t)J}\), their inverses and the powers \(t^{n+\lambda}\), \(t^{n+\mu}\) have at most polynomial growth together with their inverses for \(t\geq1\). Thus (41) is an equivalence between arbitrary inverse-power decay, respectively \(e^{-c t^2}\) decay, of its two packet families, wherever \(x\ne0\). Equation (45) gives the corresponding equivalence for \(V\) wherever \(\xi\ne0\). Multiplication by fixed polynomial powers only changes the constants or reduces a positive exponential rate; it cannot change either kind of absence.

## 8. Homogeneous Fourier directions interchange exactly

**Theorem 8.1.** Let \(u\in\mathcal D'(\mathbb R^n)\) satisfy (31) on the punctured space, with arbitrary \(\lambda\in\mathbb C\) and finite \(q\geq0\). Its tempered Fourier transform is well defined by Lemma 5.1. For either ordinary or analytic wavefront,
\[
 (x,\xi)\in\operatorname{WF}_{\star}(u)
      \quad\Longleftrightarrow\quad
 (\xi,-x)\in\operatorname{WF}_{\star}(\widehat u),
       \qquad x\ne0,\quad \xi\ne0,
       \quad\star\in\{\text{ordinary},A\}.
 \tag{47}
\]
No parity, integer-degree or vanishing-moment assumption is required for this interchange. The equation is only required away from zero, so arbitrary distributional extensions and their point terms are included.

**Proof.** We first compare vector wavefront sets. Each \(u_j=(E-\lambda)^ju\) has wavefront contained in that of \(u\). For analytic wavefront this is [A], Corollary 2.3. For ordinary wavefront use the complete cutoff Fourier calculation in [P], Section 1: local multiplication preserves cone decrease, and on a smaller cutoff
\(b\,\partial_j u=\partial_j(bu)-(\partial_jb)u\);
the Fourier multiplier \(i\eta_j\) costs one inverse power. The available rapid estimates are of every order, so all constant derivatives and smooth polynomial coefficients preserve ordinary absence. Iterate and take finite sums. Thus the union of the components' wavefront sets is exactly that of the first component \(u\).

The complete coordinate rules [F] give
\[
 \widehat{Eu}=-(E+n)\widehat u,\qquad
 \widehat{(E-\lambda)^ju}
          =(-1)^j(E-\mu)^j\widehat u.
 \tag{48}
\]
Indeed apply \(\mathcal F(\partial_j u)=i\eta_j\widehat u\) and
\(\mathcal F(y_ju)=i\partial_{\eta_j}\widehat u\), including the derivative of \(\eta_j\), and sum \(j\). The same differential-decrease argument therefore makes the union of the wavefront sets of \(V\) equal to that of \(\widehat u\).

For a finite vector, absence of this union is equivalent to the scalar packet criterion holding for every component on common smaller neighborhoods: intersect finitely many neighborhoods and take maxima of the constants, with the smallest positive analytic rate. This applies Theorem 3.1 componentwise.

At \(x\ne0,\xi\ne0\), shrink neighborhoods so both stay away from zero. Theorem 3.1 and (41) identify absence for \(U\) at \((x,\xi)\) with arbitrary inverse-power decay, respectively \(e^{-c t^2}\) decay, of \(V_gU(tx,t\xi)\). The exact Fourier rotation (28) makes this equivalent to the same decay of \(V_gV(t\xi,-tx)\). Equation (45), now evaluated near \((\xi,-x)\), and Theorem 3.1 identify it with absence for \(V\) at that point. Both anomaly errors are exponentially small by the two nonzero conditions. The union equalities just proved reduce this equivalence to \(u\) and \(\widehat u\). Taking complements gives (47). \(\square\)

For a strict homogeneous distribution of degree \(\lambda\) on the whole space, \(q=0\) and \(W_t=0\); both packet scaling identities are exact. For a homogeneous distribution on the punctured space, every distributional extension satisfies the hypothesis at \(q=0\), and is tempered by the annular proof. Existence and its exact resonant qualifications are [H], Theorems 3.1 and 4.1. The parity-sensitive whole angular Fourier formula has its separate precise assumptions in [Angular distributions and their full Fourier transforms][R]; those assumptions are retained there.

**Corollary 8.2 (independence of point terms).** Replacing an extension \(u\) by \(u+\sum c_\alpha\partial^\alpha\delta_0\) does not change either side of (47) in its indicated domain.

**Proof.** The physical difference vanishes near every \(x\ne0\). Its whole Fourier transform is the polynomial \(\sum c_\alpha(i\xi)^\alpha\), which is analytic everywhere. Adding an analytic function leaves analytic wavefront unchanged by the finite-sum argument [A], Corollary 2.3, and leaves ordinary wavefront unchanged by its smooth analogue. \(\square\)

The exclusions are substantive. The constant distribution is analytic, whereas its Fourier transform is \((2\pi)^n\delta_0\). A point jet has all its singular covectors at the physical origin, whereas its transform is a polynomial. Also homogeneity is substantive: an analytic plane wave \(e^{ia\cdot y}\), \(a\ne0\), has Fourier transform \((2\pi)^n\delta_a\), whose singular base point is nonzero. The Fourier and translation identities are [F]. These examples do not satisfy an unrestricted local wavefront rotation rule.

## References

[F] [Schwartz functions and Fourier inversion][F], Sections 1–5, with complete Gaussian constants, Schwartz estimates, compact-test density, Fourier transpose and coordinate rules.

[A] [Analytic directions of holomorphic boundary values][A], Lemma 1.1, Corollary 2.3 and Theorem 3.1, with the bounded-sequence analytic-wavefront convention.

[P] [Pulling back and combining analytic singularities][P], Lemma 2.1, for simultaneous analytic localization; Section 1 for the exact smooth Fourier cutoff inputs.

[H] [Homogeneous extensions and angular moments][H], Lemma 1.1 and Theorems 3.1–5.1, with exact resonance, moment and parity qualifications.

[J] [Angular tests, point jets and polar integration][J], A3, formula (A10), with the complete finite-jet and coefficient proof.

[R] [Angular distributions and their full Fourier transforms][R], Theorem 4.1, with its full-frequency and parity-sensitive formula.

[S] Alexander Strohmaier and Edward Witten, *Analytic States in Quantum Field Theory on Curved Spacetimes*, Annales Henri Poincaré **25** (2024), 4543–4590, Section 2 and Appendix B. [Open-access primary article](https://link.springer.com/article/10.1007/s00023-024-01419-0), retaining its CC BY 4.0 terms. The complete ordinary and analytic packet comparison used here is supplied in Section 3 above.

Original exposition and proofs here are CC0. Linked prerequisite proofs and references retain their actual component authorship and terms.

[F]: https://github.com/KokunoYumeto/open-math-courses-public/blob/669e247325664fa3196edb055821b20075db741d/docs/courses/AN-01/prerequisites/U011-free-foundations/schwartz-fourier-foundations-U017.md
[A]: ../../AN02-L186.html#complete-proof
[P]: ../../AN02-L188.html#complete-proof
[H]: https://github.com/KokunoYumeto/open-math-courses-public/blob/669e247325664fa3196edb055821b20075db741d/docs/courses/AN-01/src/homogeneous-extensions-and-angular-moments.md
[J]: https://github.com/KokunoYumeto/open-math-courses-public/blob/669e247325664fa3196edb055821b20075db741d/docs/courses/AN-01/prerequisites/U011-free-foundations/angular-foundations-U018.md
[R]: ../../AN02-L185.html#complete-proof
