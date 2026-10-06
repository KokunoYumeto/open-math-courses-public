# Complex smooth division of order one

*Complete proof excerpt from AN-04, “Fourier-integral operators,” lesson “Real and complex symplectic normal forms of functions,” §4. Original AN-04 exposition, CC0 1.0 Universal.*

The fifty-line statement and proof below are preserved verbatim after LF newline normalization. The surrounding symplectic normal-form argument is outside this excerpt. Its citation to a book identifies the classical theorem; the complete proof is supplied here.

The dividend is used on its actual supplied neighborhood. A common output neighborhood applies to dividends actually supplied on one common domain; unrelated local germs first require intersection with their individual domains. In the receiver, the preparation of the divisor and all dividend restrictions retain this distinction.

**Smooth complex division.** If a complex \(C^\infty\) function \(F(t,z)\), with real \(t,z\), has \(F(0,0)=0\) and \(\partial_tF(0,0)\ne0\), then every smooth \(G(t,z)\) has a representation
\[
 G=QF+S(z)
 \tag{4.1}
\]
on a neighborhood chosen from \(F\) and the original domain, with \(Q,S\) smooth and complex valued. The remainder is independent of \(t\). This is the \(k=1\) case of Hörmander I, Theorem 7.5.6; its hypotheses are those of Theorem 7.5.5. Neither the quotient nor the remainder is asserted to be unique. The following proof treats complex functions in real variables; it does not assume that their real zeros form a parameter graph.

**Proof.** First extend a smooth function \(a(t,z)\) almost analytically in \(t\). Multiply it by a fixed real cutoff equal to one on the patch in use. For \(v=t+iw\), choose a fixed smooth cutoff \(\chi\), equal to one near zero, and put
\[
 A(t+iw,z)=\sum_{k=0}^{\infty}
       \chi(w/\varepsilon_k)\frac{(iw)^k}{k!}\partial_t^ka(t,z).
\]
All coefficients and their derivatives are bounded on a fixed larger compact patch. A derivative of total order \(l<k\) of the \(k\)-th term is bounded by \(C_{kl}\varepsilon_k^{k-l}\). Choose positive radii decreasing to zero so that these bounds are at most \(2^{-k}\) for every \(l\le k/2\). Each fixed derivative series then converges uniformly after finitely many terms. The sum is smooth on a fixed complex domain; only the radii and its seminorm bounds depend on \(a\). Its normal jets at \(w=0\) are the formal analytic jets. Thus, with \(\partial_{\bar v}=(\partial_t+i\partial_w)/2\), Taylor's integral remainder gives
\[
 A(t,z)=a(t,z),\qquad
 |D^\beta\partial_{\bar v}A(t+iw,z)|\le C_{\beta L}|w|^L
 \quad\text{for every }\beta,L.
\]
The derivatives here include all real parameters \(z\). No holomorphic continuation of an arbitrary smooth function is claimed.

Apply this construction to \(F\), writing its extension as \(\widetilde F(v,z)\). At the mark, its real derivative in \((t,w)\) is complex multiplication by \(\lambda=\partial_tF(0,0)\ne0\). In particular it is invertible. A direct parameter argument produces a smooth complex root \(T(z)\), with \(T(0)=0\). Indeed the real map
\[
 v\longmapsto v-\lambda^{-1}\widetilde F(v,z)
\]
has derivative zero at the mark. On a sufficiently small closed complex disc its derivative norm is at most \(q<1\), uniformly on a smaller parameter patch. Shrink that patch so that its value at \(v=0\) has modulus at most \((1-q)/2\) times the disc radius. It maps the disc into itself and its fixed point lies in the interior. Iteration from zero has geometrically summable successive differences, so completeness of \(\mathbb C\) gives its unique fixed point \(T(z)\). The same contraction estimate first bounds parameter differences of \(T\) by a constant times the parameter differences. Taylor's formula in the fixed-point identity then proves differentiability, with real derivative
\[
 D_zT=-(D_v\widetilde F(T,z))^{-1}D_z\widetilde F(T,z).
\]
The inverse exists throughout the disc by the contraction bound. This formula has continuous coefficients. Induction differentiating it proves smoothness of every order. Thus \(\widetilde F(T(z),z)=0\), with no real-zero or holomorphic-root assumption.

We next divide by the known graph \(t-T(z)\). For any almost-analytic extension \(A\) as above, the segment \(v_s=T+s(t-T)\) stays inside its fixed domain after one shrink depending on \(T\). Set \(R(z)=A(T(z),z)\). The full real chain rule gives
\[
 \begin{split}
 a(t,z)-R(z)&=(t-T(z))U_0(t,z)+E(t,z),\\
 U_0&=\int_0^1(\partial_v+\partial_{\bar v})A(v_s,z)\,ds,\\
 E&=2i\operatorname{Im}T(z)
                       \int_0^1\partial_{\bar v}A(v_s,z)\,ds.
 \end{split}
\]
The sign and the error term follow from \(t-\overline T=(t-T)+2i\operatorname{Im}T\). Every derivative of \(E\) is bounded by every positive power of \(|\operatorname{Im}T|\), because the imaginary part of \(v_s\) is \((1-s)\operatorname{Im}T\) and the antiholomorphic derivative has all the preceding flat estimates. Put \(s_0=|t-T(z)|^2\ge|\operatorname{Im}T|^2\). For \(s_0>0\), define
\[
 e(t,z)=\frac{\overline{t-T(z)}\,E(t,z)}{s_0}.
\]
Each derivative of this expression costs only finitely many negative powers of \(s_0\). The arbitrary positive powers in the bounds for \(E\) absorb them, so every derivative tends to zero faster than every power of \(s_0\). Its zero extension across \(s_0=0\) is smooth even if that zero set is singular: multiply the expression by a smooth cutoff vanishing for \(s_0\le\delta\) and equal to one for \(s_0\ge2\delta\). On the transition region all differentiated cutoff factors cost finitely many powers of \(\delta^{-1}\), while the flat estimates give arbitrarily many positive powers. These smooth functions and all their derivatives converge uniformly to the zero extension. The fundamental theorem of calculus identifies those derivative limits with the derivatives of the limit. Consequently
\[
 a=(t-T)(U_0+e)+R(z)
\]
holds smoothly and exactly, including real zeros of the graph.

For \(a=F\), use the particular extension \(\widetilde F\) which constructed \(T\). Its remainder is zero, so \(F=(t-T)U\). Differentiating at the mark gives \(U(0,0)=\partial_tF(0,0)\ne0\); shrink once so \(U\) never vanishes. Apply the same graph division to \(a=G\), obtaining \(G=(t-T)V+S(z)\). Then \(Q=V/U\) proves (4.1). The real and complex neighborhoods were fixed before choosing \(G\); its extension radii and coefficient bounds may depend on \(G\). This proves exactly the needed common-neighborhood division. \(\square\)

## Component terms

The selected original AN-04 proof is dedicated to the public domain under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/). The source course retains its original authorship and credits. External books and separately cited prerequisite lessons remain under their own terms. No book prose or external PDF is included in this component. Reader typography is licensed separately by the receiving edition.
