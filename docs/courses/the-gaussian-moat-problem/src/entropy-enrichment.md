# Entropy enrichment

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Sample a point of a walk with bounded steps at a random time, and reduce it modulo many prime factors at once. How uniformly are the residues spread? This lesson proves that a simple random operation spreads them further. Starting from the sampled time, look at a long stretch of the walk ahead, pick one of its distinct differences uniformly at random, and move to one of the two endpoints of that difference. The residues of the new point carry, on average over random coordinates, at least half of the maximal possible entropy plus half of the entropy fraction that the old point had, up to a small error. Iterating the operation at decreasing scales drives the entropy of the residues to almost its maximal value, whatever the starting time.

The proof combines the many-differences theorem and the separation of differences by randomly signed products from [Differences of a walk and separating products](differences-of-a-walk-and-separating-products.md) with the entropy calculus of [Entropy of finite random variables](entropy-of-finite-random-variables.md), and Chebyshev's inequality for sampling without replacement from [Concentration and the discrete cube](concentration-and-the-discrete-cube.md). The setting is that of [Walks through Gaussian primes](walks-through-gaussian-primes.md).

A basic reference is [OpenAI-moat].

## 1. Residue entropy profiles

Throughout, \(D\ge1\), and \(z_0,z_1,\dots\) is a fixed infinite \(D\)-walk in \(\mathbb Z[i]\); no congruence condition is assumed. Let \(T\ge5\), and let \(\mathcal B\) be a set of \(k\ge1\) distinct rational primes congruent to \(1\) modulo \(4\), all in \([T,2T]\). Put

\[
L_*=\frac1k\sum_{p\in\mathcal B}\log p,\qquad \log T\le L_*\le\log(2T)\le2\log T.
\]

As in Example 7.4 of [Entropy of finite random variables](entropy-of-finite-random-variables.md), a **signed coordinate** is a pair \(c=(p,\pm)\) consisting of a prime \(p\in\mathcal B\) and one of its two conjugate factors \(\pi_c\); there are \(2k\) of them. Let \(c_1,\dots,c_k\) be a **random signed ordering**: \(c_j=(p_j,\sigma_j)\), where \(p_1,\dots,p_k\) is a uniformly random ordering of \(\mathcal B\) and the signs \(\sigma_j\) are independent fair coins. This sequence is exchangeable, each \(c_j\) is uniform on the signed coordinates, and it is independent of everything else. For a set \(\mathcal S\) of signed coordinates and a Gaussian integer \(z\), write

\[
F_{\mathcal S}(z)=\bigl(z\bmod\pi_c\bigr)_{c\in\mathcal S}\in\prod_{c\in\mathcal S}\mathbb Z[i]/(\pi_c),
\]

a homomorphism of groups. For a random point \(Z\) of \(\mathbb Z[i]\) taking finitely many values, its **residue entropy profile** is

\[
f_Z(s)=\mathbb E\,H\bigl(F_{\{c_1,\dots,c_s\}}(Z)\bigr)\qquad(0\le s\le k),
\]

an average of entropies computed with the ordering fixed (Convention 7.1 of the entropy lesson). For \(s\ge1\) its **normalized deficit** is

\[
\operatorname{def}_Z(s)=1-\frac{f_Z(s)}{sL_*}.
\]

**Proposition 1.1** (properties of profiles). Let \(Z\), \(X\), \(Y\) be random points taking finitely many values.

1. \(f_Z(0)=0\) and \(0\le f_Z(s)\le sL_*\); hence \(0\le\operatorname{def}_Z(s)\le1\).
2. \(f_Z\) is concave: for \(1\le s<k\), \(f_Z(s+1)-f_Z(s)\le f_Z(s)/s\), and \(f_Z(1)\ge f_Z(s)/s\) for \(1\le s\le k\).
3. If \(Z=z_\tau\) and \(Z'=z_{\tau'}\) for random times with \(|\tau'-\tau|\le n\), then \(f_{Z'}(s)\ge f_Z(s)-2\log(n+1)-\log(\pi D^2)\).
4. If \(V=X\) or \(V=Y\) according to an independent fair coin, then \(f_V(s)\ge\frac12\bigl(f_X(s)+f_Y(s)\bigr)\).

**Proof.** (1) For a fixed ordering, the tuple \(F_{\{c_1,\dots,c_s\}}(Z)\) takes at most \(\prod_{j\le s}p_j\) values, so its entropy is at most \(\sum_{j\le s}\log p_j\), whose average is \(sL_*\). (2) is Proposition 7.2 of the entropy lesson. (3) Apply Lemma 1.2 of [Differences of a walk and separating products](differences-of-a-walk-and-separating-products.md) for each fixed ordering, with the homomorphism \(F_{\{c_1,\dots,c_s\}}\), and average. (4) is Lemma 4.1 of the entropy lesson, applied for each fixed ordering. \(\square\)

**Example 1.2.** If \(Z\) is a fixed point, then \(f_Z=0\) and \(\operatorname{def}_Z\equiv1\). If \(Z\) is uniformly distributed on a complete set of residues modulo \(\prod_{p\in\mathcal B}p\), then every tuple \(F_{\mathcal S}(Z)\) is uniformly distributed, by the Chinese remainder theorem and Exercise 7.4 of the first lesson, so \(f_Z(s)\) is the average of \(\sum_{j\le s}\log p_j\), namely \(sL_*\), and \(\operatorname{def}_Z\equiv0\).

## 2. The sampling transition

**Definition 2.1** (the transition). Let \(\tau\) be a random time and \(Z=z_\tau\). Let \(U>0\) and \(0<g<\frac1{100}\), and put \(n=\lfloor e^{gU}\rfloor\), assumed at least \(1\). Conditionally on \(\tau=t\), with fresh randomness:

1. let \(E_t=\{z_t,z_{t+1},\dots,z_{t+n}\}\) be the stretch of \(n\) steps starting at \(t\);
2. choose \(h\) uniformly at random from the set \(E_t-E_t\) of its distinct differences (including \(0\));
3. let \((X,Y)\in E_t\times E_t\) be the pair with \(X-Y=h\) chosen by a fixed rule, for instance the pair \((z_{t+i},z_{t+j})\) with \((i,j)\) lexicographically least;
4. toss an independent fair coin and let \(V=X\) or \(V=Y\) accordingly.

Each difference receives the same weight, whatever the number of pairs realizing it. Since the walk has distinct points, \(X=z_{\tau_X}\), \(Y=z_{\tau_Y}\) and \(V=z_{\tau'}\) for random times with \(\tau\le\tau_X,\tau_Y,\tau'\le\tau+n\). Thus the transition replaces the random time \(\tau\) by a later random time \(\tau'\), at most \(n\) steps later. It uses no prime factors.

## 3. Entropy enrichment

**Theorem 3.1** (entropy enrichment). Put \(K_D=2000+8\log(\pi D^2)\). Let \(T\ge5\) and \(\mathcal B\) be as in Section 1, let \(0<g<\frac1{100}\) and \(U>0\) with

\[
g^5U\ge K_D\log T,
\]

and put \(q=\lfloor U/L_*\rfloor\) and \(b=\lfloor g^2U/L_*\rfloor\). Assume \(q\le k\). Then \(1\le b<q\), and for every random time \(\tau\), the point \(Z=z_\tau\) and the endpoint \(V\) of the transition with parameters \(U,g\) satisfy

\[
\frac{f_V(b)}{bL_*}\ge\frac12\Bigl(1+\frac{f_Z(q)}{qL_*}\Bigr)-16g,
\qquad\text{equivalently}\qquad
\operatorname{def}_V(b)\le\tfrac12\operatorname{def}_Z(q)+16g.
\]

The right side keeps half of the old entropy fraction and adds half of the largest possible one. Before the proof, we record what the hypothesis gives. Put \(\lambda=U/L_*\). Since \(L_*\le2\log T\),

\[
g^5\lambda\ge\frac{K_D}2.
\tag{3.1}
\]

Hence \(\lambda\) is large, \(q\ge\lambda-1\ge\lambda/2\), \(1\le g^2\lambda/2\le b\le g^2\lambda\), and \(q-b\ge\lambda-1-g^2\lambda\ge\lambda/2\); in particular \(1\le b<q\). Moreover \(gU=g\lambda L_*\ge g\lambda\log5\ge K_D/2\), so \(e^{gU}\ge2\), and

\[
1\le\tfrac12e^{gU}\le n\le e^{gU},\qquad \log(n+1)\le gU+\log2.
\tag{3.2}
\]

We use the random signed ordering \(c_1,c_2,\dots\) of Section 1, and write

\[
\mathcal S=\{c_1,\dots,c_b\},\qquad \mathcal Q=\{c_1,\dots,c_q\},\qquad B_x=F_{\mathcal S}(X),\quad B_y=F_{\mathcal S}(Y),\qquad h=X-Y.
\]

For a signed coordinate \(c\), write \(h_c=h\bmod\pi_c\). The proof compares two estimates for the quantity

\[
\Delta=\mathbb E\,H\bigl(h_{c_{b+1}}\mid B_x,B_y\bigr),
\]

the average conditional entropy of one fresh coordinate of the difference, given the first \(b\) coordinates of both endpoints.

**Lemma 3.2** (a fresh coordinate of the difference). In the setting of Theorem 3.1, \(\Delta\ge(1-21g)L_*\).

**Proof.** Fix a value \(t\) of \(\tau\) of positive probability. Let \(A_t\) be the quantity \(A=RW\) of Theorem 2.2 of [Differences of a walk and separating products](differences-of-a-walk-and-separating-products.md) for the stretch \(E_t\), and \(a_t=\log A_t\). By that theorem and (3.2),

\[
gU-3\le\log\frac{\pi n}{24}\le a_t\le2\log D+2gU,
\qquad |E_t-E_t|\ge\frac{A_t}{\pi D^2}.
\tag{3.3}
\]

Put \(r=\lceil(1+10g)a_t/L_*\rceil\). Then \(r\ge(gU-3)/L_*\ge g\lambda-3\ge g\lambda/2\), and

\[
r\le1.1\,\frac{2gU+2\log D}{L_*}+1\le2.2\,g\lambda+2.2\log D+1\le3g\lambda\le q-b,
\]

using (3.1) for the third inequality. Let \(\mathcal J=\{c_{b+1},\dots,c_{b+r}\}\). Its primes form a uniformly random subset of \(\mathcal B\) with \(r\) elements, and given these primes the signs are independent and fair.

*The product of the primes of \(\mathcal J\) is large.* The numbers \(\log p\), \(p\in\mathcal B\), lie in an interval of length \(\log2\). By Proposition 1.1 of [Concentration and the discrete cube](concentration-and-the-discrete-cube.md), the sum \(\Sigma\) of \(\log p\) over the primes of \(\mathcal J\) has mean \(rL_*\) and variance at most \(r(\log2)^2/4\le r/8\). Since \(a_t\le rL_*/(1+10g)\), the event \(\Sigma<(1+5g)a_t\) requires \(\Sigma\le rL_*-\frac{5g}{1+10g}rL_*\le rL_*-4.5\,grL_*\). By Chebyshev's inequality its probability is at most

\[
\frac{r/8}{(4.5\,grL_*)^2}\le\frac1{160\,g^2rL_*^2}\le\frac1{80\,g^3\lambda}\le\frac g2,
\]

using \(L_*\ge1\), \(r\ge g\lambda/2\) and (3.1).

*Separation.* On the complementary event, the product \(P_{\mathcal J}\) of the primes of \(\mathcal J\) satisfies \(P_{\mathcal J}^{1-g}\ge A_t^{(1+5g)(1-g)}\ge A_t^{1+3g}\ge16A_t\), because \(4g-5g^2\ge3g\) and \(3ga_t\ge3g(gU-3)\ge\log16\). Also \(g^3r\ge g^4\lambda/2\ge2\) by (3.1). Corollary 3.3 of [Differences of a walk and separating products](differences-of-a-walk-and-separating-products.md), with \(d=g\), shows that, given the primes of \(\mathcal J\), the reduction \(F_{\mathcal J}\) is injective on \(E_t-E_t\) except with probability at most

\[
\exp\Bigl(-\frac{g^3r}{640\log2}\Bigr)\le\exp\Bigl(-\frac{g^4\lambda}{1280\log2}\Bigr)\le\exp\Bigl(-\frac{1}{g}\Bigr)\le\frac g2,
\]

using \(g^4\lambda\ge K_D/(2g)\ge1280\log2/g\). Altogether, the ordering is *good*, meaning that \(F_{\mathcal J}\) is injective on \(E_t-E_t\), except with probability at most \(g\).

*Entropy of the separated difference.* Given \(\tau=t\), the difference \(h\) is uniform on \(E_t-E_t\). For a good ordering, \(F_{\mathcal J}(h)\) is therefore uniform on \(|E_t-E_t|\) values, and by (3.3)

\[
H\bigl(F_{\mathcal J}(h)\mid\tau=t\bigr)=\log|E_t-E_t|\ge a_t-\log(\pi D^2).
\]

For every ordering, \(B_x\) and \(B_y\) take at most \((2T)^b\) values each, so by Corollary 2.4(3) and subadditivity in the entropy lesson,

\[
H\bigl(F_{\mathcal J}(h)\mid\tau=t\bigr)-2b\log(2T)\le H\bigl(F_{\mathcal J}(h)\mid B_x,B_y,\tau=t\bigr)\le\sum_{i=1}^rH\bigl(h_{c_{b+i}}\mid B_x,B_y,\tau=t\bigr).
\]

Average over the ordering. By exchangeability, each summand on the right has the same average as the one with \(i=1\). Since the left side is at least \(-2b\log(2T)\) for every ordering, and at least \(a_t-\log(\pi D^2)-2b\log(2T)\) for good ones,

\[
\mathbb E\,H\bigl(h_{c_{b+1}}\mid B_x,B_y,\tau=t\bigr)\ge(1-g)\frac{a_t}r-\frac{\log(\pi D^2)+2b\log(2T)}r.
\]

Now \(r\le(1+10g)a_t/L_*+1\) gives \(a_t/r\ge L_*/(1+10g+L_*/a_t)\ge(1-10g-L_*/a_t)L_*\), and \(L_*/a_t\le2L_*/(gU)=2/(g\lambda)\le g\) by (3.1). Further, \(2b\log(2T)/r\le2g^2\lambda\cdot2L_*/(g\lambda/2)=8gL_*\), and \(\log(\pi D^2)/r\le2\log(\pi D^2)/(g\lambda)\le gL_*\) by (3.1) and the choice of \(K_D\). Therefore

\[
\mathbb E\,H\bigl(h_{c_{b+1}}\mid B_x,B_y,\tau=t\bigr)\ge(1-g)(1-11g)L_*-9gL_*\ge(1-21g)L_*.
\]

Finally, for each fixed ordering, \(H(h_{c_{b+1}}\mid B_x,B_y)\ge H(h_{c_{b+1}}\mid B_x,B_y,\tau)\), which is the average over \(t\) of the conditional entropies given \(\tau=t\). Averaging over the ordering proves the lemma. \(\square\)

**Lemma 3.3** (retaining the starting entropy). In the setting of Theorem 3.1,

\[
\Delta\le\bigl[f_X(b+1)-f_X(b)\bigr]+\bigl[f_Y(b+1)-f_Y(b)\bigr]-\frac{f_Z(q)}q+11gL_*.
\]

**Proof.** Fix the ordering and write \(c=c_{b+1}\) and \(\phi=F_{\{c\}}\). The pairs \((\phi(X),\phi(Y))\) and \((h_c,\phi(X))\) determine each other, since \(h_c=\phi(X)-\phi(Y)\). By the chain rule, subadditivity, and Corollary 2.4(4) of the entropy lesson (the full difference \(h\) determines \(h_c\)),

\[
H(h_c\mid B_x,B_y)=H\bigl(\phi(X),\phi(Y)\mid B_x,B_y\bigr)-H\bigl(\phi(X)\mid B_x,B_y,h_c\bigr)
\le H(\phi(X)\mid B_x)+H(\phi(Y)\mid B_y)-H\bigl(\phi(X)\mid B_x,B_y,h\bigr).
\]

Average over the ordering. By Proposition 7.2 of the entropy lesson, the first two terms average to \(f_X(b+1)-f_X(b)\) and \(f_Y(b+1)-f_Y(b)\).

For the last term, exchangeability shows that its average equals the average of

\[
\frac1{q-b}\sum_{i=1}^{q-b}H\bigl(F_{\{c_{b+i}\}}(X)\mid B_x,B_y,h\bigr)\ge\frac1{q-b}H\bigl(F_{\mathcal Q}(X)\mid B_x,B_y,h\bigr),
\]

where we used subadditivity, and the fact that \(F_{\mathcal Q}(X)\) consists of \(F_{\mathcal Q\setminus\mathcal S}(X)\) and the known \(B_x\). By Corollary 2.4(3) of the entropy lesson, and since \(B_x,B_y\) take at most \((2T)^b\) values each,

\[
H\bigl(F_{\mathcal Q}(X)\mid B_x,B_y,h\bigr)\ge H\bigl(F_{\mathcal Q}(X)\bigr)-2b\log(2T)-H(h).
\]

The average of \(H(F_{\mathcal Q}(X))\) is \(f_X(q)\ge f_Z(q)-H(X-Z)\), by Proposition 1.1(3) and its proof. Both \(h\) and \(X-Z\) are displacements of the walk over at most \(n\) steps, so by Lemma 1.2 of [Differences of a walk and separating products](differences-of-a-walk-and-separating-products.md) and (3.2),

\[
H(h)+H(X-Z)\le4\log(n+1)+2\log(\pi D^2)\le4gU+4\log2+2\log(\pi D^2)\le5gU,
\]

since \(gU\ge K_D/2\). Using \(f_Z(q)\ge0\), \(q-b\ge\lambda/2\), \(b\le g^2\lambda\) and \(\log(2T)\le2L_*\), the average of the subtracted term is at least

\[
\frac{f_Z(q)}{q}-\frac{4g^2\lambda L_*+5g\lambda L_*}{\lambda/2}\ge\frac{f_Z(q)}q-11gL_*.
\]

\(\square\)

**Proof of Theorem 3.1.** Lemmas 3.2 and 3.3 give

\[
\bigl[f_X(b+1)-f_X(b)\bigr]+\bigl[f_Y(b+1)-f_Y(b)\bigr]\ge L_*+\frac{f_Z(q)}q-32gL_*.
\]

By concavity (Proposition 1.1(2)), each bracket is at most \(f_X(b)/b\), respectively \(f_Y(b)/b\). By Proposition 1.1(4), \(f_V(b)\ge\frac12(f_X(b)+f_Y(b))\). Hence \(f_V(b)/b\ge\frac12\bigl(L_*+f_Z(q)/q\bigr)-16gL_*\). Divide by \(L_*\). \(\square\)

The proof explains the design of the transition. The difference of the two endpoints is spread over many values, because the stretch has many distinct differences and a random product of factors separates them; so the endpoints together carry about \(L_*\) units of entropy per coordinate beyond what their first \(b\) coordinates reveal. Each endpoint also inherits the residue entropy of the starting point, because it is only a short displacement away. Concavity converts the per-coordinate gain into a gain for the whole profile.

## 4. Iterating the transition

**Corollary 4.1** (iteration). Let \(g\) be fixed, and let \(U_0>U_1>\dots>U_l\) satisfy \(U_{j+1}=g^2U_j\). Suppose that the hypotheses of Theorem 3.1 hold for each pair \((U_j,g)\), \(0\le j<l\). Start from any random time \(\tau_0\), and let \(\tau_{j+1}\) be the time produced by the transition with parameters \((U_j,g)\) applied at \(\tau_j\), with fresh randomness at each stage. Put \(q_j=\lfloor U_j/L_*\rfloor\). Then

\[
\operatorname{def}_{z_{\tau_l}}(q_l)\le2^{-l}+32g.
\]

**Proof.** The output size of stage \(j\) is \(\lfloor g^2U_j/L_*\rfloor=q_{j+1}\), the input size of stage \(j+1\). Theorem 3.1 gives \(\operatorname{def}_{z_{\tau_{j+1}}}(q_{j+1})\le\frac12\operatorname{def}_{z_{\tau_j}}(q_j)+16g\). Since deficits are at most \(1\), induction gives \(2^{-l}+16g(1+\frac12+\dots)\le2^{-l}+32g\). \(\square\)

The starting law is arbitrary; in particular \(\tau_0\) may be a fixed time, with deficit \(1\). After \(l\) transitions the deficit is below \(2^{-l}+32g\). The last lessons combine this with Proposition 1.1(3): a later random time, at most \(N\) steps after \(\tau_l\), changes the profile at \(q_l\) by at most \(2\log(N+1)+\log(\pi D^2)\), which is small compared with \(q_lL_*\approx U_l\) when \(\log N\) is small compared with \(U_l\).

## 5. Exercises

**Exercise 5.1 (easy).** Let \(\tau_0\) be a fixed time. Show that after one transition, \(f_V(b)\ge(\frac12-16g)bL_*\), under the hypotheses of Theorem 3.1.

**Exercise 5.2 (easy).** Check the inequality \((1+5g)(1-g)\ge1+3g\) for \(0\le g\le\frac15\), and \(\frac{5g}{1+10g}\ge4.5g\) for \(0\le g\le\frac1{100}\).

**Exercise 5.3 (medium).** Consider the straight walk \(z_t=t\) on the real axis, which has \(D=1\), and a fixed starting time. Describe the law of \(h\) and of \(V\) in Definition 2.1, and show that \(V-z_\tau\) is not uniformly distributed on \(\{0,\dots,n\}\).

**Exercise 5.4 (medium).** Show that the deficit bound of Corollary 4.1 cannot drop below \(32g\) by iteration alone: if \(\operatorname{def}_{j+1}=\frac12\operatorname{def}_j+16g\) for all \(j\), then \(\operatorname{def}_j\to32g\). Explain why the schedule of the next lessons uses smaller and smaller values of \(g\).

**Exercise 5.5 (hard).** In the proof of Lemma 3.2, the number \(r\) of fresh coordinates depends on the starting time \(t\). Explain why this does not affect the final averaged inequality, and why the proof first conditions on \(\tau=t\) and only at the end removes this condition.

## 6. Solutions

**5.1.** A fixed point has \(f_Z\equiv0\), so Theorem 3.1 gives \(f_V(b)/(bL_*)\ge\frac12-16g\).

**5.2.** \((1+5g)(1-g)-(1+3g)=g-5g^2=g(1-5g)\ge0\) for \(g\le\frac15\). And \(\frac{5}{1+10g}\ge\frac5{1.1}>4.5\) for \(g\le\frac1{100}\).

**5.3.** Here \(E_t=\{t,\dots,t+n\}\) and \(E_t-E_t=\{-n,\dots,n\}\), so \(h\) is uniform on these \(2n+1\) integers. For \(h=m\ge0\) the lexicographically least pair is \((z_{t+m},z_t)\), and for \(h=-m<0\) it is \((z_t,z_{t+m})\). Thus \(\{X,Y\}=\{t,t+|h|\}\), and \(V-t\) equals \(0\) with probability \(\frac12\) (the coin selects the endpoint \(t\)) and equals \(|h|\) otherwise. So \(\mathbb P(V=t)=\frac12+\frac1{2(2n+1)}\), which is far from uniform. The theorem does not claim uniformity of the displacement; it concerns residues modulo many large primes, and the entropy gain comes from the difference \(h\).

**5.4.** The map \(x\mapsto\frac12x+16g\) has the fixed point \(32g\) and contracts distances by \(\frac12\), so the iterates converge to \(32g\). To make the deficit tend to zero, the schedule uses bands of scales with parameters \(g\) that decrease with the overall size, and accuracy \(O(g)\) in each band.

**5.5.** For a fixed \(t\), the set \(\mathcal J\) and the number \(r\) are fixed functions of the ordering, and the inequality obtained,
\(\mathbb E\,H(h_{c_{b+1}}\mid B_x,B_y,\tau=t)\ge(1-21g)L_*\), involves only the single coordinate \(c_{b+1}\), whose law does not depend on \(t\). Averaging this inequality over \(t\) with the weights \(\mathbb P(\tau=t)\) is therefore legitimate. Conditioning on \(\tau=t\) is needed because the geometry of the stretch, and with it the separation argument, depends on \(t\); the conditional entropy given \(\tau\) is at most the one without it, so the condition can be removed at the end.

## References

- [OpenAI-moat] OpenAI, Bounded-step walks on Gaussian primes, preprint, 26 September 2026. https://github.com/openai/math/blob/main/preprints/Bounded-Step-Walks-on-Gaussian-Primes-September-26-2026/paper.pdf
