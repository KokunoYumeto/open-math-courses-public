# Slow decrease and entire Fourier division

Original exposition and proofs: GPT-6.1 Sol (OpenAI), Ultra. CC0 1.0. Self-checked by the writing AI; independent mathematical review is not claimed.

Polynomial division preserves compact Fourier growth when the quotient is entire. For an arbitrary compact distribution's transform, that conclusion needs a lower-growth condition. We identify it through real logarithmic neighborhoods, complex averages and the absence of collapsed profiles. A complete Phragmén–Lindelöf argument and a Banach-space estimate connect these conditions to entire division.

Basic references are Tao's *246B, Notes 2* and *245B, Notes 9*, and Hörmander's *The Analysis of Linear Partial Differential Operators I* and *II*. The precise earlier proofs are Compact Fourier division and multiplicity-sensitive annihilators, Theorem CF2.1, for the compact-support growth criterion; Entire logarithms and the approximation of plurisubharmonic functions, for local integrability; Local compactness and Hartogs bounds, for PSH compactness; and Frequency-selective singularities and smooth convolutions, Theorem 1.1 and Lemma 3.2, for the smoothing characterization and Baire's theorem. We prove the additional real-to-complex propagation, entire-quotient growth and complete weighted-space arguments below.

## 1. Five descriptions of slow decrease

Let \(u\) be a compact distribution on \(\mathbb R^n\), \(n\geq1\), and use

\[
 F(\zeta)=\langle u,e^{-ix\cdot\zeta}\rangle,\qquad
 L_u(z,c)=\frac{\log|F(c+z\log|c|)|}{\log|c|},
 \quad c\in\mathbb R^n,\quad |c|>2.
 \tag{1.1}
\]

Logarithms at zeros equal \(-\infty\). A proper logarithmic profile is a canonical PSH local \(L^1\) limit. Collapse is convergence to \(-\infty\) uniformly on every compact parameter set.

**Theorem 1.1 (slow decrease and entire division).** The following five conditions are equivalent:

1. No escaping real frequency sequence has a collapsed profile.
2. There is \(A>0\) such that, for every \(c\in\mathbb R^n\),
   \[
   \sup_{\substack{\zeta\in\mathbb C^n\\
          |\zeta-c|<A\log(2+|c|)}}|F(\zeta)|
                  >(A+|c|)^{-A}.
   \tag{1.2}
   \]
3. For every \(a>0\) there is \(A>0\) such that, for every real \(c\),
   \[
   \sup_{\substack{h\in\mathbb R^n\\
             |h|<a\log(2+|c|)}}|F(c+h)|
                  >(A+|c|)^{-A}.
   \tag{1.3}
   \]
4. For every \(a>0\) there is \(A>0\) such that, for every real \(|c|>2\),
   \[
   \int_{|z|<a}\log|F(c+z\log|c|)|\,dV(z)
                         >-A\log|c|.
   \tag{1.4}
   \]
   Volume is real \(2n\)-dimensional volume, without normalization.
5. Whenever \(w\) is a compact distribution and \(G\) is entire with
   \(F_w=FG\), the function \(G\) is the Fourier–Laplace transform of a compact distribution.

For \(F\not\equiv0\), condition 5 says exactly that every entire extension of \(F_w/F\) is a compact-distribution transform. The factorization wording also handles the zero input: if \(F=0\), choose \(w=0\) and \(G(z)=e^{z_1^2}\). This function has superpolynomial real growth and fails the compact-support growth criterion. Thus condition 5 is false, as are the other four conditions.

The word *invertible* for \(u\), and *slowly decreasing* for \(F\), will mean these equivalent conditions. This terminology does not assert a compact convolution inverse or pointwise nonvanishing.

The implications are organized by their mechanisms: Section 2 proves \(1\Rightarrow4\Rightarrow3\Rightarrow2\Rightarrow1\); Sections 3–4 prove \(4\Rightarrow5\); Section 5 proves \(5\Rightarrow1\).

## 2. From real windows to complex profiles

**Lemma 2.1 (collapse propagates from a real ball).** Let \(f_j\) be PSH functions on \(\mathbb C^n\), allowing the identically \(-\infty\) function, locally uniformly bounded above. Suppose that for some \(a>0\) and \(M_j\to\infty\),

\[
 f_j(x)\leq-M_j\quad(x\in\mathbb R^n,\ |x|<a).
 \tag{2.1}
\]

Then \(f_j\to-\infty\) uniformly on every compact subset of \(\mathbb C^n\).

*Proof.* Fix \(x\) in the real ball and \(y\in\mathbb R^n\). If \(y=0\) the value at \(x\) already tends to \(-\infty\). Otherwise the restrictions
\(g_j(w)=f_j(x+wy)\) are subharmonic on \(\mathbb C\), or identically \(-\infty\), and have uniform upper bounds on compact subsets. Choose \(r>0\) so that \(x+ty\) stays in the real ball for \(-r\leq t\leq r\). On the rectangle \(-r<t<r,\ 0<s<r\), the harmonic function

\[
 \omega(t,s)=
 \sin\!\left(\frac{\pi(t+r)}{2r}\right)
 \frac{\sinh(\pi(r-s)/(2r))}{\sinh(\pi/2)}
 \tag{2.2}
\]

is positive in the interior, vanishes on the top and vertical sides, and lies between zero and one on the bottom side. Let \(C\geq0\) be a uniform upper bound for the \(g_j\) on the closed rectangle. Subharmonic maximum comparison with
\(C-(M_j+C)\omega\) gives
\[
 g_j(t+is)\leq C-(M_j+C)\omega(t,s).
 \tag{2.3}
\]
On the bottom the comparison function is at least \(-M_j\), and on the other sides it is \(C\). The boundary upper limits of \(g_j\) are bounded by these values because the functions are defined and upper semicontinuous in a neighborhood of the rectangle. Thus (2.3) follows from bounded-domain maximum comparison. It gives uniform collapse on each compact subset of the rectangle's interior.

PSH compactness in one complex dimension now makes the entire line family collapse locally uniformly: a subsequence with a proper local \(L^1\) further limit would contradict the preceding uniform collapse on a nonempty open rectangle. Specifically, pairing there against a nonnegative smooth function of positive integral would tend to \(-\infty\), whereas proper \(L^1\) convergence gives a finite pairing. If uniform collapse failed on any compact set, the compactness alternative would provide just such a proper further subsequence. Hence \(g_j(i)\to-\infty\).

We have proved \(f_j(x+iy)\to-\infty\) for all real \(|x|<a\) and all real \(y\). This is an open subset of \(\mathbb C^n\). If the full family had a proper local \(L^1\) extracted limit \(V\), take a small complex ball in this open set and a common upper bound \(C'\) there. Fatou applied to \(C'-f_j\geq0\) would force its integrals to tend to infinity, contrary to the finite \(L^1\) limit. PSH compactness excludes every proper extraction and therefore gives uniform local collapse of the full family. \(\square\)

**Lemma 2.2 (absorbing lower-bound constants).** Suppose a window supremum satisfies
\[
 S(c)\geq b(1+|c|)^{-M},\quad b>0,\ M\geq0.
 \tag{2.4}
\]
It then satisfies \(S(c)>(A+|c|)^{-A}\) for a sufficiently large \(A\).

*Proof.* Choose \(A\geq\max\{1,M\}\) with \(A^{-(A-M)}<b\). Then
\((A+q)^A=(A+q)^M(A+q)^{A-M}\geq(1+q)^M A^{A-M}\).
Its reciprocal proves the strict comparison for every \(q\geq0\). A lower bound \((B+q)^{-B}\), with arbitrary \(B>0\), gives (2.4) with \(M=\lceil B\rceil\) and \(b=\max\{1,B\}^{-B}\). \(\square\)

*Proof that condition 1 implies condition 4.* The case \(F=0\) cannot satisfy condition 1, so \(F\) is nonzero. Its logarithm is locally integrable by the precise preceding holomorphic-logarithm lemma.
Fix \(a>0\). If (1.4) had no constant \(A\), the integrals
\(\int_{|z|<a}L_u(z,c)\,dV(z)\) would be unbounded below.
They have a finite lower bound on every bounded range \(2<|c|\leq R\). Indeed the affine images \(c+z\log|c|\) lie in one compact region, and the change-of-variables factor \((\log|c|)^{-2n}\) is at most \((\log2)^{-2n}\). The integral of the negative part of \(\log|F|\) on that region is finite, giving a uniform lower bound for the unnormalized integral. Division by \(\log|c|\geq\log2\) retains such a bound.

There would consequently be an escaping sequence \(c_j\) with these normalized integrals tending to \(-\infty\). The family \(L_u(\cdot,c)\) is locally uniformly bounded above by the ordinary compact Fourier growth estimate. PSH compactness gives a proper local \(L^1\) extraction or a collapsed extraction. Condition 1 excludes collapse, and proper \(L^1\) convergence makes the integrals over the fixed ball converge to a finite value. This is a contradiction. Choose \(A\) larger than the absolute lower bound to obtain the strict inequality (1.4).

*Proof that condition 4 implies condition 3.* If (1.3) failed for a particular \(a>0\), for each integer \(j\geq2\) we could choose \(c_j\) with
\[
 \sup_{|h|<a\log(2+|c_j|)}|F(c_j+h)|
                         \leq(j+|c_j|)^{-j}.
 \tag{2.5}
\]
These centers escape. To see this, the window supremum is positive and continuous in \(c\): it is the maximum over the closed real unit ball after substituting \(h=a\log(2+|c|)t\), and the supremum over its open interior has the same value by continuity. It is positive because a nonzero entire function cannot vanish on an open real ball; applying the one-variable identity principle successively in each coordinate proves this assertion. Its minimum on any compact set of centers is therefore positive. The right side of (2.5) is at most \(j^{-j}\), which tends to zero, excluding bounded center subsequences.

Write \(q_j=|c_j|>2\) on a tail. For every real \(|x|<a\), the displacement \(h=x\log q_j\) is allowed in (2.5). Hence
\[
 L_u(x,c_j)\leq
    -j\frac{\log(j+q_j)}{\log q_j}\leq-j.
 \tag{2.6}
\]
Lemma 2.1 makes \(L_u(\cdot,c_j)\) collapse uniformly locally. Its integral over any fixed parameter ball then tends to \(-\infty\), contradicting the finite normalized lower bound (1.4). Thus condition 3 holds.

*Proof that condition 3 implies condition 2.* Use condition 3 with \(a=1\). Its real window is contained in any complex window with coefficient at least one. Lemma 2.2 converts its lower bound to the form (1.2), choosing \(A\) also at least one.

*Proof that condition 2 implies condition 1.* If \(L_u(\cdot,c_j)\) collapsed along escaping centers, the windows in (1.2) would correspond to parameter balls of radii
\(A\log(2+|c_j|)/\log|c_j|\leq2A\) on a tail. Uniform collapse on this fixed ball would contradict
\[
 \sup_{|z|<2A}L_u(z,c_j)>
       -A\frac{\log(A+|c_j|)}{\log|c_j|},
 \tag{2.7}
\]
whose right side tends to the finite number \(-A\). This completes the first four equivalences.

## 3. A half-plane bound with no residual polynomial loss

**Lemma 3.1 (a Phragmén–Lindelöf comparison).** Let \(v\) be subharmonic on an open set containing the closed upper half-plane, allowing the collapsed case, and suppose
\[
 v(x)\leq0\ (x\in\mathbb R),\qquad
 v(is)\leq C\ (s\geq0),\qquad
 v(z)\leq C+A|z|\ (\operatorname{Im}z\geq0).
 \tag{3.1}
\]
Here \(C\) is finite and \(A\geq0\). Then \(v\leq0\) on the whole upper half-plane.

*Proof.* The collapsed case is immediate. In the first quadrant write \(z=re^{i\theta}\), \(0\leq\theta\leq\pi/2\), and choose the continuous branch
\[
 H_1(z)=\operatorname{Re}[(e^{-i\pi/4}z)^{3/2}]
       =r^{3/2}\cos\!\left(\tfrac32(\theta-\pi/4)\right)
       \geq\cos(3\pi/8)\,r^{3/2}.
 \tag{3.2}
\]
It is harmonic inside the quadrant and continuous at its vertex. On the two straight boundary sides, \(v-\varepsilon H_1\leq C^+=\max\{C,0\}\). On a sufficiently large outer quarter-circle the same bound holds, because
\(C+Ar-\varepsilon\cos(3\pi/8)r^{3/2}\to-\infty\).
Bounded-domain maximum comparison gives \(v-\varepsilon H_1\leq C^+\) throughout that quarter-disk. For each fixed interior point let the disk radius become large, and then let \(\varepsilon\downarrow0\). Thus \(v\leq C^+\) in the first quadrant. Reflection \(z\mapsto-\overline z\), or the corresponding branch centered at angle \(3\pi/4\), gives the same bound in the second quadrant.

Now \(\log|z+i|\) is harmonic in the upper half-plane and at least zero on its real boundary. The function
\(v(z)-\varepsilon\log|z+i|\) has boundary upper limit at most zero and tends to \(-\infty\) on outer upper semicircles, since \(v\leq C^+\) there. Maximum comparison on large upper half-disks therefore makes it at most zero. Let \(\varepsilon\downarrow0\) to obtain \(v\leq0\). The two different barriers first remove linear growth and then remove the remaining constant. \(\square\)

**Lemma 3.2 (exponential type and real polynomial growth imply compact Fourier growth).** Suppose an entire \(G\) satisfies
\[
 |G(z)|\leq C_0e^{A|z|},\qquad
 |G(\xi)|\leq C_1(1+|\xi|)^N\quad(\xi\in\mathbb R^n),
 \tag{3.3}
\]
where \(A\geq0\), \(N\) is a nonnegative integer and \(C_0,C_1>0\). Then
\[
 |G(\xi+i\eta)|\leq 2^N C_1
       (1+|\xi+i\eta|)^N e^{A|\eta|}.
 \tag{3.4}
\]
Consequently \(G\) is the transform of a distribution supported in the closed ball of radius \(A\).

*Proof.* The conclusion is trivial if \(G=0\). Fix real \(\xi,\eta\), with \(b=|\eta|>0\), and put \(a=1+|\xi|\). The linear function \(p(z)=a-ibz\) has its zero in the lower half-plane, so \(\log|p|\) is harmonic above the real axis. There \(|p(z)|\geq a\geq1\). Consider
\[
 v(z)=\log|G(\xi+z\eta)|-N\log|a-ibz|
       -Ab\operatorname{Im}z-\log(2^{N/2}C_1).
 \tag{3.5}
\]
This is subharmonic in a neighborhood of the closed upper half-plane, or identically \(-\infty\). For real \(t\),
\[
 1+|\xi+t\eta|\leq a+b|t|
       \leq\sqrt2\,|a-ibt|,
 \tag{3.6}
\]
so the real-axis bound gives \(v(t)\leq0\). On \(z=is\), the exponential bound gives
\(v(is)\leq \log C_0+A|\xi|-\log(2^{N/2}C_1)\), since the term \(Abs\) cancels and \(-N\log(a+bs)\leq0\).
For every upper-half-plane \(z\) it also gives
\(v(z)\leq C_\xi+Ab|z|\), with the same finite constant increased if necessary. The proof of Lemma 3.1 uses only a neighborhood of the closed upper half-plane, so applies here as well; equivalently, each bounded comparison domain used there lies in that neighborhood. Hence \(v(i)\leq0\).

This yields
\(|G(\xi+i\eta)|\leq2^{N/2}C_1(a+b)^Ne^{Ab}\).
Since \(a+b=1+|\xi|+|\eta|\leq\sqrt2(1+|\xi+i\eta|)\), we obtain (3.4). For \(\eta=0\) it follows directly from (3.3). The exact compact-support growth theorem CF2.1 in the preceding compact Fourier chapter, applied to the ball with support function \(A|\eta|\), supplies the distribution and its uniqueness. \(\square\)

## 4. Entire quotients: first exponential, then polynomial

**Lemma 4.1 (Lindelöf's exponential-type division argument).** Let \(F\not\equiv0\) and \(W\) be entire functions satisfying exponential-type bounds \(C e^{A|z|}\), possibly with different constants. If \(W=FG\) with \(G\) entire, then \(G\) also has an exponential-type bound.

*Proof.* If \(G=0\), there is nothing to show. Translate the complex origin to a point where \(F\neq0\). The exponential-type bounds persist under this fixed translation. Write \(f=\log|F|\), so \(f\) is proper PSH and locally integrable. Choose constants \(A,B\) with \(f(z)\leq A|z|+B\). On the ball \(B_R\), the submean inequality at its center gives
\(\operatorname{avg}_{B_R}f\geq f(0)\), whereas \(f_+\leq AR+|B|\). Since \(|f|=2f_+-f\) almost everywhere,
\[
 \operatorname{avg}_{B_R}|f|\leq
          2(AR+|B|)-f(0)=O(R+1).
 \tag{4.1}
\]
For \(|z|\leq R\), the ball \(B_R(z)\) lies in \(B_{2R}(0)\). Its volume is \(2^{-2n}\) times that of the larger ball, so
\(\operatorname{avg}_{B_R(z)} f_-\leq2^{2n}\operatorname{avg}_{B_{2R}}|f|=O(R+1)\).
The logarithm of \(W\) is bounded above on this ball by \(O(R+1)\). Away from the zero sets, which have real volume zero by the preceding holomorphic-logarithm lemma,
\(\log|G|=\log|W|-\log|F|\).
Apply the submean inequality to \(\log|G|\), using its local integrability, to get
\[
 \log|G(z)|\leq
   \operatorname{avg}_{B_R(z)}\log|W|
   +\operatorname{avg}_{B_R(z)}f_-
   =O(R+1).
 \tag{4.2}
\]
All constants are independent of \(|z|\leq R\), for \(R\geq1\). Take \(R=\max\{1,|z|\}\), exponentiate, and undo the fixed translation. This proves the exponential-type bound. \(\square\)

*Proof that condition 4 implies condition 5.* Let \(W=F_w=FG\), with \(w\) compact. The case \(G=0\) has the zero inverse. Otherwise \(F,W\) are nonzero. Ordinary compact Fourier growth bounds both by exponential type, since any fixed polynomial factor is bounded by a constant times \(e^{|z|}\). Lemma 4.1 gives (3.3)'s exponential bound for \(G\).

We next establish real polynomial growth. Fix any \(a>0\), put \(\ell=\log|c|\), \(q=|c|>2\), and let \(V_a=\operatorname{vol}(B_a)\). Submean comparison and the product equality give
\[
 \log|G(c)|\leq\frac1{V_a}
 \left[\int_{|z|<a}\log|W(c+z\ell)|\,dV(z)
       -\int_{|z|<a}\log|F(c+z\ell)|\,dV(z)\right].
 \tag{4.3}
\]
If \(G(c)=0\), this inequality holds with left side \(-\infty\). The identity under the integrals is valid almost everywhere and all the logarithms are locally integrable.
Choose a compact support ball of radius \(R\) for \(w\), and Fourier order \(M\). On this parameter ball,
\[
 |W(c+z\ell)|\leq C(1+q+a\ell)^M e^{Ra\ell}
                    \leq C_a q^{M+Ra}.
 \tag{4.4}
\]
The last inequality uses \(\ell\leq q\) and \(q>2\). Condition 4 bounds the subtracted integral below by \(-A_a\ell\). Thus
\(\log|G(c)|\leq\log C_a+(M+Ra+A_a/V_a)\log q\).
Take an integer \(N\) at least the nonnegative part of that exponent, and include the bounded real region by increasing a constant. We obtain the real bound in (3.3). Lemma 3.2 upgrades it to (3.4), and Theorem CF2.1 supplies the compact inverse transform. This proves condition 5 for an arbitrary entire divisor \(F\), including its zeros with their full analytic multiplicities.

## 5. Why the division property excludes a collapsed profile

We must obtain one polynomial exponent for a whole class of quotients. An exponent depending separately on every derivative would not suffice.

**Lemma 5.1 (multiplication controls local entire quotients).** Fix a nonzero entire \(F\). For every compact \(T\subset\mathbb C^n\), there are another compact \(S\) and a finite constant \(C_T\) such that every entire \(G\) satisfies
\[
 \sup_T|G|\leq C_T\sup_S|FG|.
 \tag{5.1}
\]

*Proof.* At any \(z_0\), choose a complex direction \(\theta\) for which \(t\mapsto F(z_0+t\theta)\) is not identically zero. Such a direction exists: otherwise every point of \(\mathbb C^n\) would lie on a line from \(z_0\) on which \(F\) vanishes identically, making \(F=0\). The one-variable zeros are isolated, so choose a positive radius \(r\) whose circle has no zeros. By compactness of that circle and continuity, for \(z\) in some neighborhood of \(z_0\),
\[
 |F(z+t\theta)|\geq\delta>0\quad(|t|=r).
 \tag{5.2}
\]
The Cauchy formula for \(t\mapsto G(z+t\theta)\) gives
\(|G(z)|\leq\delta^{-1}\sup_{|t|=r}|F(z+t\theta)G(z+t\theta)|\).
Shrink to a neighborhood with compact closure so the indicated points form a compact set. Finitely many such neighborhoods cover \(T\). Their compact point sets form \(S\), and the maximum of their reciprocal bounds gives \(C_T\). This works at zeros of \(F\) as well as at nonzeros. \(\square\)

Assume condition 5, and \(u\neq0\). Let \(K\) be the compact convex hull of \(\operatorname{supp}u\), with support function \(H_K\). Define
\[
 \mathcal B=\left\{G\text{ entire}:
    \|G\|_{\mathcal B}
    =\sup_{\zeta\in\mathbb C^n}
       |F(\zeta)G(\zeta)|e^{-H_K(\operatorname{Im}\zeta)
                                   -|\operatorname{Im}\zeta|}
                   <\infty\right\}.
 \tag{5.3}
\]

**Lemma 5.2 (the weighted quotient space is Banach).** The expression (5.3) is a norm, \(\mathcal B\) is complete, and point evaluation of \(G\) is continuous.

*Proof.* The norm properties follow from the supremum; if it is zero then \(FG=0\) everywhere. Since \(F\) is nonzero on a nonempty open set, \(G=0\) there and hence everywhere by the identity principle. Lemma 5.1 and the finite upper bound of \(e^{H_K(\operatorname{Im}\zeta)+|\operatorname{Im}\zeta|}\) on its compact \(S\) bound every compact supremum of \(G\) by a constant times \(\|G\|_{\mathcal B}\). This proves continuity of evaluations and local uniform control.

A Cauchy sequence \(G_j\) in this norm is therefore Cauchy uniformly on every compact set. Its limit \(G\) is entire: the coordinate Cauchy integrals on small polydisks pass to the uniform limit and give the holomorphic derivatives there. For each fixed \(\zeta\), the weighted product difference converges to that of \(G_j-G\). Taking the pointwise limit in a common norm-Cauchy inequality, then its supremum, proves \(\|G_j-G\|_{\mathcal B}\to0\). Comparison with one \(G_j\) shows that \(G\in\mathcal B\). Hence the space is complete. \(\square\)

Every \(G\in\mathcal B\) has a product \(FG\) satisfying the compact-support growth bound for \(K+\overline B_1\), with polynomial order zero. Theorem CF2.1 gives a compact distribution \(w_G\) with transform \(FG\). Condition 5 then makes \(G\) a compact-distribution transform, so its real growth is bounded by some polynomial.

For positive integers \(m\), set
\[
 D_m=\{G\in\mathcal B:
        |G(\xi)|\leq m(1+|\xi|)^m
                          \text{ for every real }\xi\}.
 \tag{5.4}
\]
These sets are closed by evaluation continuity and cover \(\mathcal B\), since each real polynomial bound can be dominated by the displayed one for sufficiently large \(m\). Baire's theorem, proved in the preceding frequency-selective chapter, gives \(G_0,\varepsilon>0,m\) with \(G_0+\{G:\|G\|_{\mathcal B}<\varepsilon\}\subset D_m\). In particular \(G_0\in D_m\). Subtracting the values at \(G_0+G\) and \(G_0\) bounds \(|G(\xi)|\) by \(2m(1+|\xi|)^m\) when \(\|G\|_{\mathcal B}<\varepsilon\). For a nonzero arbitrary \(G\), apply this to \(\varepsilon G/(2\|G\|_{\mathcal B})\). The zero function already satisfies the result. We obtain one fixed exponent, with \(C=4m/\varepsilon\):
\[
 |G(\xi)|\leq C\|G\|_{\mathcal B}(1+|\xi|)^m
 \quad(G\in\mathcal B,\ \xi\in\mathbb R^n).
 \tag{5.5}
\]

*Proof that condition 5 implies condition 1.* If condition 1 failed, Theorem 1.1 of Frequency-selective singularities and smooth convolutions would provide a compact continuous \(v\notin C^1\), supported in \(\overline B_1(0)\), with \(u*v\) smooth. Put \(V=F_v\).
For every multi-index \(\alpha\), \(G_\alpha(\zeta)=(i\zeta)^\alpha V(\zeta)\) belongs to \(\mathcal B\): its product with \(F\) is the transform of the smooth compact function \(D^\alpha(u*v)\), whose support lies in \(K+\overline B_1\). Its direct integral bound is
\[
 |F(\zeta)G_\alpha(\zeta)|
 \leq\|D^\alpha(u*v)\|_1
                   e^{H_K(\operatorname{Im}\zeta)+|\operatorname{Im}\zeta|}.
 \tag{5.6}
\]
Thus (5.5) applies with the same \(m\) to every derivative, although its norm constant may depend on \(\alpha\).

Given an integer \(s>m\), apply it to \(\alpha=se_t\), for every coordinate \(t\). At a real \(\xi\) with \(|\xi|\geq1\), choose \(t\) with \(|\xi_t|\geq|\xi|/\sqrt n\). Taking the maximum of the finitely many norm constants gives
\[
 |V(\xi)|\leq C_s n^{s/2}|\xi|^{-s}(1+|\xi|)^m.
 \tag{5.7}
\]
Choose \(s\) arbitrarily large. This is rapid decay of \(V\) on all real frequencies. Its inverse Fourier integral and all differentiated inverse integrals are absolutely convergent, yielding a smooth representative of \(v\); Fourier injectivity identifies that representative with the given distribution, as proved in the preceding compact Fourier chapter. Since \(v\) is continuous, its representative agrees pointwise with it. This contradicts \(v\notin C^1\). Condition 1 follows, completing all five equivalences. \(\square\)

## 6. The terminology and finite-regularity stability

**Definition 6.1.** A compact distribution satisfying Theorem 1.1 is called invertible; its transform is called slowly decreasing.

Zeros of the transform are allowed. For example, every nonzero polynomial symbol, multiplied by a point-mass exponential if desired, has the entire-division property by the preceding polynomial division theorem. Thus its distribution is invertible even when the polynomial has zeros. The term records the convolution regularity and division criteria, not a claim that its transform has a pointwise reciprocal which is entire.

**Corollary 6.2 (a finite amount of smoothness suffices for perturbations).** If \(u\) is invertible, there is a nonnegative integer \(r\) such that \(u+v\) is invertible for every compactly supported \(v\in C^r(\mathbb R^n)\). The size and support of \(v\) may vary. In particular invertibility is unchanged by compact smooth perturbations.

*Proof.* Use condition 3 with \(a=1\), and Lemma 2.2's preliminary conversion to choose \(b>0,M\geq0\) with
\[
 \sup_{|h|<\log(2+|c|)}|F_u(c+h)|
                         \geq b(1+|c|)^{-M}.
 \tag{6.1}
\]
Choose an integer \(r>M\). For any compact \(C^r\) function, integration by parts \(r\) times in a coordinate with large frequency gives
\(|F_v(\xi)|\leq C_v(1+|\xi|)^{-r}\) on real frequencies; bounded frequencies are included by increasing \(C_v\).
When \(|c|\) is large and \(|h|<\log(2+|c|)\), \(|c+h|\geq|c|/2\). Hence the perturbing transform is at most
\(C'_v(1+|c|)^{-r}\), which is less than \((b/4)(1+|c|)^{-M}\) beyond a threshold depending on \(v\).
Choose a point in the window where the original modulus exceeds \((3b/4)(1+|c|)^{-M}\). The reverse triangle inequality gives a new window supremum at least \((b/2)(1+|c|)^{-M}\).

These tail lower bounds show that \(F_{u+v}\) is not identically zero. Its real-window suprema are continuous and positive on every bounded set of centers, as proved in Section 2. Decrease the constant \(b/2\) to extend a positive polynomial bound to all centers. That one real window sits in a complex window; Lemma 2.2 gives condition 2 for \(u+v\). Thus \(u+v\) is invertible. If a compact smooth perturbation changed a noninvertible \(u\) to an invertible one, applying the same result to the invertible \(u+v\) and the smooth perturbation \(-v\) would make \(u\) invertible too, a contradiction. \(\square\)

## References

- Terence Tao, [246B, Notes 2: Some connections with the Fourier transform](https://terrytao.wordpress.com/2021/01/23/246b-notes-2-some-connections-with-the-fourier-transform/), 2021. Background on entire transforms and support; its Fourier normalization differs from (1.1).
- Terence Tao, [245B, Notes 9: The Baire category theorem and its Banach space consequences](https://terrytao.wordpress.com/2009/02/01/245b-notes-9-the-baire-category-theorem-and-its-banach-space-consequences/), 2009. Background on the boundedness argument.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I*, Springer, 1983. Compact Fourier growth and subharmonic estimates.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators II*, Springer, 1983, Chapter XVI. Slow decrease and entire division. The real-ball propagation, Phragmén–Lindelöf barriers, Lindelöf division argument and Banach-space proof are supplied above.
