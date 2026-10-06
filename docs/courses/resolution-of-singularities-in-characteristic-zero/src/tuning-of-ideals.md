# Tuning of ideals

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The going-up theorem needs D-balanced ideals, and the uniqueness of maximal contact needs MC-invariant ones. A general ideal is neither. This lesson replaces an ideal \(\mathcal I\) of maximal order \(m\) by an ideal \(W(\mathcal I)\) built from all products of derivatives of \(\mathcal I\) of sufficiently high total weight. The new ideal is both D-balanced and MC-invariant, and it admits exactly the same blow-up sequences as \(\mathcal I\). Order reduction for \(\mathcal I\) is therefore the same problem as order reduction for \(W(\mathcal I)\), which has the good properties.

We use [Smooth blow-ups and transforms of ideals](smooth-blowups-and-transforms-of-ideals.md), [Blow-up sequences and the main theorems](blow-up-sequences-and-the-main-theorems.md), [Derivative ideals under blowing up](derivative-ideals-under-blowing-up.md), [Hypersurfaces of maximal contact](hypersurfaces-of-maximal-contact.md), [Logarithmic derivatives and going up](logarithmic-derivatives-and-going-up.md) and [Uniqueness of maximal contact](uniqueness-of-maximal-contact.md).

## 1. Maximal coefficient ideals

Throughout, \(\mathcal I\) is an ideal sheaf on a smooth scheme \(X\), nonzero on every component, with \(m=\operatorname{maxord}\mathcal I\ge1\), and \(L=\operatorname{lcm}(1,2,\ldots,m)\). A factor \(D^j(\mathcal I)\), \(0\le j\le m\), has *weight* \(m-j\).

**Definition 1.1.** For \(s\ge0\), the *maximal coefficient ideal* of order \(s\) is

\[
W_s(\mathcal I)=\Bigl(\ \prod_{j=0}^{m}\bigl(D^j\mathcal I\bigr)^{c_j}\ :\ \sum_j(m-j)c_j\ge s\ \Bigr).
\]

Since \(D^m(\mathcal I)=\mathcal O_X\), factors with \(j=m\) do not matter, and \(W_0(\mathcal I)=\mathcal O_X\).

**Lemma 1.2 (combinatorics).** Give variables \(u_1,\ldots,u_m\) the degrees \(\deg u_i=i\). Every monomial \(U=\prod u_i^{e_i}\) with \(\deg U\ge(r+m-1)L\) can be written \(U=U_1U_2\) with \(\deg U_1=rL\).

**Proof.** Put \(V_i=u_i^{L/i}\), of degree \(L\), and write \(u_i^{e_i}=V_i^{b_i}W_i\) with \(\deg W_i<L\). If \(\sum b_i\ge r\), choose \(0\le d_i\le b_i\) with \(\sum d_i=r\) and take \(U_1=\prod V_i^{d_i}\). Otherwise \(\sum b_i\le r-1\), and \(\deg U=\sum(b_iL+\deg W_i)<(r-1)L+mL\), a contradiction. \(\square\)

**Proposition 1.3.**

0. For \(s\ge1\), \(\operatorname{maxord}W_s(\mathcal I)=s\), \(\operatorname{cosupp}(W_s(\mathcal I),s)=\operatorname{cosupp}(\mathcal I,m)\), and \(W_s(\mathcal I)=\mathcal O\) near every point where \(\operatorname{ord}\mathcal I<m\).
1. \(W_{s+1}(\mathcal I)\subset W_s(\mathcal I)\).
2. \(W_s(\mathcal I)\cdot W_t(\mathcal I)\subset W_{s+t}(\mathcal I)\).
3. \(D(W_{s+1}(\mathcal I))=W_s(\mathcal I)\).
4. For \(s\ge1\), \(MC(W_s(\mathcal I))=W_1(\mathcal I)=MC(\mathcal I)\).
5. For \(s\ge1\), \(W_s(\mathcal I)\) is MC-invariant.
6. If \(s=rL\) and \(t\ge(m-1)L\), then \(W_s(\mathcal I)\cdot W_t(\mathcal I)=W_{s+t}(\mathcal I)\).
7. If \(s=rL\) with \(r\ge m-1\), then \(W_s(\mathcal I)^j=W_{js}(\mathcal I)\) for every \(j\ge1\).
8. If \(s=rL\) with \(r\ge\max(m-1,1)\), then \(W_s(\mathcal I)\) is D-balanced.

**Proof.** (0) At a point \(x\) with \(\operatorname{ord}_x\mathcal I=m\), each \(D^j\mathcal I\) has order \(\ge m-j\) at \(x\), so every generator of \(W_s\) has order \(\ge s\). By [Hypersurfaces of maximal contact, Lemma 1.2](hypersurfaces-of-maximal-contact.md#1-the-ideal-of-maximal-contact) there is \(x_1\in MC(\mathcal I)=D^{m-1}(\mathcal I)\) of order \(1\) at \(x\), and \(x_1^s\in W_s\) has order \(s\). At a point where \(\operatorname{ord}\mathcal I<m\), \(MC(\mathcal I)\) contains a unit \(v\) (same lemma), and \(v^s\in W_s\).

(1) and (2) are immediate from the definition.

(3) By the product rule, a derivative of a product of factors \(D^j\mathcal I\) is a sum of products in which one factor \(D^j\mathcal I\) is replaced by \(D^{j+1}\mathcal I\), of weight one less; so \(D(W_{s+1})\subset W_s\). For the reverse inclusion we argue near a point \(x\). If \(\operatorname{ord}_x\mathcal I<m\), both sides are \(\mathcal O\) near \(x\) by (0). If \(\operatorname{ord}_x\mathcal I=m\), take \(x_1\in MC(\mathcal I)\) of order \(1\) at \(x\). By the Taylor criterion some coordinate derivation \(\partial_i\) has \(\partial_ix_1\) a unit near \(x\); put \(\delta=(\partial_ix_1)^{-1}\partial_i\), so \(\delta(x_1)=1\). We show by induction on \(t\), \(0\le t\le s\), that \(x_1^{s-t}W_t\subset D(W_{s+1})\). For \(t=0\): \(x_1^{s+1}\in W_{s+1}\), and \((s+1)x_1^s=\delta(x_1^{s+1})\), so \(x_1^s\in D(W_{s+1})\) since the characteristic is zero. For \(t\ge1\) and \(f\in W_t\): \(x_1^{s+1-t}f\in W_{s+1-t}W_t\subset W_{s+1}\), so

\[
(s+1-t)\,x_1^{s-t}f+x_1^{s+1-t}\,\delta f=\delta\bigl(x_1^{s+1-t}f\bigr)\in D(W_{s+1}).
\]

Since \(\delta f\in D(W_t)\subset W_{t-1}\), the induction hypothesis gives \(x_1^{s+1-t}\delta f\in D(W_{s+1})\). As \(s+1-t\ge1\), also \(x_1^{s-t}f\in D(W_{s+1})\). The case \(t=s\) is the claim.

(4) By (0), \(MC(W_s)=D^{s-1}(W_s)\), which is \(W_1\) by (3) applied \(s-1\) times. A generator of \(W_1\) has a factor \(D^j\mathcal I\) with \(j<m\), so \(W_1\subset\sum_{j<m}D^j\mathcal I=D^{m-1}\mathcal I\); conversely \(D^{m-1}\mathcal I\) has weight \(1\).

(5) \(MC(W_s)\cdot D(W_s)=W_1\cdot W_{s-1}\subset W_s\) by (4), (3) and (2).

(6) "\(\subset\)" is (2). A generator of \(W_{s+t}\) is a product of factors of weights \(m-j\in\{1,\ldots,m\}\) (factors of weight \(0\) are units) with total weight \(\ge s+t\ge(r+m-1)L\). Regard each factor of weight \(i\) as the variable \(u_i\). By Lemma 1.2 the product splits into a product of total weight exactly \(rL=s\), which lies in \(W_s\), and a product of the remaining weight \(\ge t\), which lies in \(W_t\).

(7) By induction on \(j\): \(W_s^{j}=W_s\cdot W_s^{j-1}=W_s\cdot W_{(j-1)s}=W_{js}\), using (6) with \(t=(j-1)s\ge s\ge(m-1)L\).

(8) By (0) the maximal order of \(W_s\) is \(s\), and by (3), \(D^i(W_s)=W_{s-i}\). For \(0\le i<s\), (2) and (7) give \((D^iW_s)^s=W_{s-i}^{\,s}\subset W_{s(s-i)}=W_s^{\,s-i}\). \(\square\)

## 2. Tuning

**Theorem 2.1 (tuning).** Let \(s\ge1\) and let \(\mathcal J\) be an ideal with \(\mathcal I^s\subset\mathcal J\subset W_{ms}(\mathcal I)\). A smooth blow-up sequence of \(X\) is a blow-up sequence of order \(\ge m\) for \((X,\mathcal I,m)\) if and only if it is a blow-up sequence of order \(\ge ms\) for \((X,\mathcal J,ms)\). The same holds with snc divisors \(E\) carried along on both sides.

**Proof.** Both directions are proved by induction on the length; suppose the first \(r-1\) blow-ups are valid for both marked ideals, with transforms \(\mathcal I_{r-1}\) and \(\mathcal J_{r-1}\), and let \(Z\subset X_{r-1}\) be the next centre.

Suppose \(\operatorname{ord}_Z\mathcal I_{r-1}\ge m\). The ideal \(W_{ms}(\mathcal I)\) is generated, locally, by finitely many products \(P=\prod_j(D^j\mathcal I)^{c_j}\) of weight \(\ge ms\). By [Derivative ideals under blowing up, Corollary 3.2](derivative-ideals-under-blowing-up.md#3-the-basic-inclusion), applied to the first \(r-1\) steps, which are of order \(\ge m\) for \((\mathcal I,m)\), the transform of \((P,ms)\) is defined and contained in \(\prod_j(D^j\mathcal I_{r-1})^{c_j}\). Transforms preserve sums and inclusions, so

\[
\mathcal J_{r-1}\subset\Pi_{r-1}{}^{-1}_*\bigl(W_{ms}(\mathcal I),ms\bigr)\subset\Bigl(\prod_j(D^j\mathcal I_{r-1})^{c_j}:\ \textstyle\sum_j(m-j)c_j\ge ms\Bigr).
\]

Each factor \(D^j\mathcal I_{r-1}\) has order \(\ge m-j\) along \(Z\), so the right side has order \(\ge ms\) along \(Z\), and so does \(\mathcal J_{r-1}\).

Conversely suppose \(\operatorname{ord}_Z\mathcal J_{r-1}\ge ms\). Since \(\mathcal I^s\subset\mathcal J\) and transforms are multiplicative, \(\mathcal I_{r-1}^{\,s}=\Pi_{r-1}{}^{-1}_*(\mathcal I^s,ms)\subset\mathcal J_{r-1}\). Hence \(s\cdot\operatorname{ord}_Z\mathcal I_{r-1}=\operatorname{ord}_Z\mathcal I_{r-1}^{\,s}\ge ms\), so \(\operatorname{ord}_Z\mathcal I_{r-1}\ge m\).

The snc conditions on the centres and the transforms of \(E\) do not involve the ideals, so they are the same on both sides. \(\square\)

**Corollary 2.2.** Let \(s=rL\) with \(r\ge\max(m-1,1)\). Then \(W_s(\mathcal I)\) is D-balanced and MC-invariant, of maximal order \(s\), with \(\operatorname{cosupp}(W_s(\mathcal I),s)=\operatorname{cosupp}(\mathcal I,m)\); and a smooth blow-up sequence is of order \(\ge m\) for \((X,\mathcal I,m,E)\) if and only if it is of order \(\ge s\) for \((X,W_s(\mathcal I),s,E)\). Equivalently, by Lemma 2.3 of the second lesson, the blow-up sequences of order \(m\) for \((X,\mathcal I,E)\) are exactly those of order \(s\) for \((X,W_s(\mathcal I),E)\).

**Proof.** The properties are Proposition 1.3 (0), (5) and (8). Since \(m\) divides \(L\), put \(s'=s/m\). Then \(\mathcal I^{s'}\subset W_s(\mathcal I)\), because \(\mathcal I=D^0\mathcal I\) has weight \(m\), and \(W_s(\mathcal I)=W_{ms'}(\mathcal I)\). Theorem 2.1 applies with \(\mathcal J=W_s(\mathcal I)\). \(\square\)

**Definition 2.3 (the tuned ideal).** For \(m=\operatorname{maxord}\mathcal I\), put \(s(m)=m\cdot\operatorname{lcm}(1,\ldots,m)\) and \(W(\mathcal I)=W_{s(m)}(\mathcal I)\). For \(m=1\), \(W(\mathcal I)=W_1(\mathcal I)=\mathcal I\).

The choice depends only on \(m\), so it introduces no further choices. Since derivative ideals commute with smooth pull-back and with field extension ([Smooth blow-ups and transforms of ideals, Proposition 2.6](smooth-blowups-and-transforms-of-ideals.md#2-order-of-vanishing-and-derivative-ideals)), so does the tuned ideal: if \(h:Y\to X\) is smooth and its image meets \(\operatorname{cosupp}(\mathcal I,m)\), then \(\operatorname{maxord}h^*\mathcal I=m\) and \(W(h^*\mathcal I)=h^*W(\mathcal I)\).

**Remark 2.4.** The transform of \(W(\mathcal I)\) along a blow-up sequence is in general not the tuned ideal of the transform of \(\mathcal I\), and it need not stay D-balanced (Example 5.1 of the previous lesson). This is harmless: the going-up theorem and the uniqueness theorems are statements about whole sequences starting with the tuned ideal, and the tuning can be repeated whenever a construction starts afresh.

## 3. An example

**Example 3.1.** Let \(\mathcal I=(x^2+y^3)\) on \(\mathbf A^2\), so \(m=2\), \(L=2\) and \(s(2)=4\). Here \(D(\mathcal I)=(x,y^2)\), of weight \(1\), and \(\mathcal I\) has weight \(2\), so

\[
W(\mathcal I)=W_4(\mathcal I)=\mathcal I^2+\mathcal I\cdot D(\mathcal I)^2+D(\mathcal I)^4 .
\]

It has maximal order \(4\), attained only at the origin. On the MC-hypersurface \(H=V(x)\), the restrictions of the three summands are \((y^6)\), \((y^3\cdot y^4)\) and \((y^8)\), so \(W(\mathcal I)|_H=(y^6)\). The marked ideal \((W(\mathcal I)|_H,4)\) has cosupport the origin of \(H\), and after blowing it up its transform is \((y^2)\), of order \(<4\). By going up (Corollary 4.3 of the previous lesson), the blow-up of the origin of \(\mathbf A^2\) is a blow-up of order \(4\) for \(W(\mathcal I)\) and of order \(2\) for \(\mathcal I\), after which \(\mathcal I\) has maximal order \(1\), as Exercise 5.2 of the first lesson confirmed directly.

## 4. Exercises

**Exercise 4.1.** Compute \(W(\mathcal I)\) for \(\mathcal I=(x^2)\) and for \(\mathcal I=(x,y)^m\).

*Solution.* For \((x^2)\): \(m=2\), \(D(\mathcal I)=(x)\), and \(W_4=(x^2)^2+(x^2)(x)^2+(x)^4=(x^4)=\mathcal I^2\). For \((x,y)^m\): \(D^j\mathcal I=(x,y)^{m-j}\), so every generator of weight \(w\) lies in \((x,y)^w\), and \(W_s=(x,y)^s\); then \(W=(x,y)^{s(m)}\).

**Exercise 4.2.** Verify Proposition 1.3(3) for \(\mathcal I=(x,y)^m\).

*Solution.* By Exercise 4.1, \(W_{s+1}=(x,y)^{s+1}\), and \(D((x,y)^{s+1})=(x,y)^s=W_s\).

**Exercise 4.3.** For \(m=1,2,3\), find the smallest \(s\) of the form \(rL\) with \(r\ge\max(m-1,1)\), and compare with \(s(m)\) and with \(m!\).

*Solution.* For \(m=1\): \(L=1\), smallest \(s=1\), \(s(1)=1=1!\). For \(m=2\): \(L=2\), \(r\ge1\), smallest \(s=2\), \(s(2)=4\), \(2!=2\). For \(m=3\): \(L=6\), \(r\ge2\), smallest \(s=12\), \(s(3)=18\), while \(3!=6=1\cdot L\) has \(r=1<m-1\). So Corollary 2.2 does not cover \(W_{3!}\) for \(m=3\); the traditional choice \(W_{m!}\) needs a separate check for small \(m\), which the choice \(s(m)\) avoids.

## References

- [Kollár] J. Kollár, *Resolution of singularities — Seattle lecture*, arXiv:math/0508332, section "Tuning of ideals" (maximal coefficient ideals \(W_s\)). <https://arxiv.org/abs/math/0508332>
- [Włodarczyk] J. Włodarczyk, *Simple Hironaka resolution in characteristic zero*, arXiv:math/0401401, coefficient and homogenized ideals, from which the term "tuning" comes. <https://arxiv.org/abs/math/0401401>
