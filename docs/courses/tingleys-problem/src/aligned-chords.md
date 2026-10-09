# Aligned chords

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson turns an attained positive defect into a rigid configuration: a line through the point \(ty\) inside the unit ball of \(X\) whose chord is mapped by \(f\) to a chord of the unit sphere of \(Y\) through \(t f(y)\), with the lengths of the four half-chords related by the defect (Proposition 5.1). The configuration is a fixed point of a *return map* on directions [OpenAI-T, Section 4]. Starting from a direction \(v\) at \(ty\), go to the sphere, apply \(f\), take the opposite end of the chord through \(tf(y)\) in \(Y\), pull it back by \(f^{-1}\), and read off the direction from that point back to \(ty\). Extremality of the defect propagates along common supports and produces a closed convex set of directions that the return map preserves. On this set the return map contracts the measure of noncompactness, and Darbo's theorem gives a fixed direction.

We use: from [Supports, radial contact and the Mazur–Ulam theorem](supports-radial-contact-and-the-mazur-ulam-theorem.md), Lemma 1.1 (common supports), Lemma 2.1 (radial contact) and the defect of Section 4; from [Ultrapowers and Darbo's fixed-point theorem](ultrapowers-and-darbos-fixed-point-theorem.md), Proposition 3.1 (attainment) and Theorem 6.1 (Darbo).

**Standing assumptions.** \(X,Y\) are real Banach spaces, \(f:S_X\to S_Y\) is a surjective isometry, \(M>0\), and there are \(x_0,y\in S_X\) and \(0<t<1\) with
\[
|D_q(a,c)|\le M\quad(a,c\in S_X,\ 0\le q\le1),\qquad D_t(x_0,y)=M,\tag{0.1}
\]
as Proposition 3.1 of the previous lesson provides. Put \(b=f(y)\in S_Y\) and \(\epsilon=1-t\).

## 1. The return map

For \(v\in S_X\) define, in this order:

- \(p=p(v)>0\) with \(x(v)=ty+pv\in S_X\), by Lemma 2.1 of the first lesson with \(c=ty\);
- \(s=s(v)=\|f(x(v))-tb\|\) and \(w=w(v)=(f(x(v))-tb)/s\in S_Y\), so that \(f(x(v))=tb+sw\);
- \(u=u(v)>0\) with \(tb-uw\in S_Y\), by Lemma 2.1 of the first lesson in \(Y\) with \(c=tb\) and the direction \(-w\);
- \(z=z(v)=f^{-1}(tb-uw)\in S_X\), \(r=r(v)=\|z-ty\|\), and \(g(v)=(ty-z)/r\in S_X\), so that \(z=ty-r\,g(v)\).

**Lemma 1.1.** The maps \(p,s,w,u,z,r,g\) are well defined and continuous on \(S_X\), and \(p,s,u,r\in[\epsilon,1+t]\). For every \(v\in S_X\),
\[
s-p=D_t(x(v),y)\le M,\qquad r-u=-D_t(z(v),y)\le M.\tag{1.1}
\]

**Proof.** For unit vectors \(e\) and \(\|c\|=t\), \(\|e-c\|\in[1-t,1+t]\); this bounds \(s\) and \(r\), and Lemma 2.1 of the first lesson bounds \(p\) and \(u\). In particular \(s,r>0\), so \(w\) and \(g\) are defined. Continuity follows from the continuity of \(p\) and of the radial contact in \(Y\) (Lemma 2.1 of the first lesson), of \(f\) and \(f^{-1}\), and of the norm. Finally \(D_t(x(v),y)=\|tb+sw-tb\|-\|ty+pv-ty\|=s-p\) and \(D_t(z(v),y)=u-r\), and (0.1) bounds both. \(\square\)

## 2. The extremal set and propagation

Let \(E=\{v\in S_X:s(v)-p(v)=M\}\).

**Lemma 2.1.** \(E\) is closed, and \(v_0=(x_0-ty)/\|x_0-ty\|\) lies in \(E\).

**Proof.** \(E\) is closed by continuity of \(s-p\) on the closed set \(S_X\). The point \(x_0=ty+\|x_0-ty\|v_0\) lies on \(S_X\), so \(x(v_0)=x_0\) by uniqueness of radial contact, and \(s(v_0)-p(v_0)=D_t(x_0,y)=M\). \(\square\)

**Lemma 2.2.** Let \(v\in E\). Then \(r-u=M\), \(\|x(v)-z(v)\|=p+r=s+u\), and \(v\) and \(g(v)\) share a support.

**Proof.** Since \(f\) is an isometry, \(\|x(v)-z(v)\|=\|f(x(v))-f(z(v))\|=\|(s+u)w\|=s+u\). Also \(x(v)-z(v)=pv+r\,g(v)\), so \(s+u\le p+r\), that is \(r-u\ge s-p=M\). With (1.1), \(r-u=M\) and \(\|pv+r\,g(v)\|=p+r\). Lemma 1.1 of the first lesson gives a common support. \(\square\)

**Lemma 2.3** (propagation). Let \(v\in E\), and let \(l\in S_X\) share a support with \(g(v)\). Then \(l\in E\). In particular \(g(E)\subseteq E\).

**Proof.** Keep \(z=z(v)\), \(r=r(v)\), \(u=u(v)\), \(w=w(v)\), and let \(\varphi\) be a common support of \(l\) and \(g(v)\). Since \(x(l)-z=p(l)l+r\,g(v)\),
\[
p(l)+r=\varphi\bigl(x(l)-z\bigr)\le\|x(l)-z\|\le p(l)+r,
\]
so \(\|x(l)-z\|=p(l)+r\). On the other side, \(\|x(l)-z\|=\|f(x(l))-f(z)\|=\|s(l)w(l)+uw\|\le s(l)+u\). Hence \(s(l)-p(l)\ge r-u=M\), and (1.1) gives equality. By Lemma 2.2, \(g(v)\) shares a support with itself, so \(g(v)\in E\). \(\square\)

## 3. An invariant convex set

**Lemma 3.1.** There is a nonempty closed convex set \(C\subseteq E\) with \(g(C)\subseteq C\).

**Proof.** Fix an enumeration \((\pi_n)_{n\ge0}\) of the pairs \((m,\beta)\), \(m\ge0\), \(\beta\) a probability vector with rational entries indexed by \(\{0,\dots,m\}\), in which every pair occurs infinitely often; the set of pairs is countable. Put \(\lambda_n=1/(n+2)\). Let \(v_0\) be as in Lemma 2.1, and suppose \(v_0,\dots,v_n\) have been chosen with \(\operatorname{conv}\{v_0,\dots,v_n\}\subseteq E\), which holds for \(n=0\). If \(\pi_n=(m,\beta)\) with \(m\le n\), let \(\alpha^{(n)}\) be \((1-\lambda_n)\tilde\beta+\lambda_n\upsilon_n\), where \(\tilde\beta\) is \(\beta\) extended by zeros to \(\{0,\dots,n\}\) and \(\upsilon_n\) is the uniform probability vector on \(\{0,\dots,n\}\); otherwise let \(\alpha^{(n)}=\upsilon_n\). Put
\[
a_n=\sum_{i=0}^n\alpha^{(n)}_iv_i\in\operatorname{conv}\{v_0,\dots,v_n\}\subseteq E,\qquad v_{n+1}=g(a_n).
\]
All coefficients \(\alpha^{(n)}_i\) are positive. By Lemma 2.2, \(a_n\) and \(v_{n+1}\) share a support \(\varphi\). By Lemma 1.1 of the first lesson, \(\varphi(v_i)=1\) for \(i\le n\), hence \(\varphi=1\) on \(\operatorname{conv}\{v_0,\dots,v_{n+1}\}\), and every \(l\) in this hull is a unit vector sharing the support \(\varphi\) with \(g(a_n)\). By Lemma 2.3, \(l\in E\). This continues the induction.

Let \(C\) be the closed convex hull of \(\{v_0,v_1,\dots\}\). It is nonempty, closed, bounded and convex, and \(C\subseteq E\) because \(E\) is closed and contains every \(\operatorname{conv}\{v_0,\dots,v_n\}\). The points \(a_n\) are dense in \(C\): the rational convex combinations \(\sum_{i\le m}\beta_iv_i\) are dense in \(C\), and for each such \((m,\beta)\) the infinitely many \(n\ge m\) with \(\pi_n=(m,\beta)\) give \(\|a_n-\sum_i\beta_iv_i\|\le\lambda_n\|\upsilon_n-\tilde\beta\|_1\le2\lambda_n\to0\). Since \(g(a_n)=v_{n+1}\in C\) and \(g\) is continuous, \(g(C)\subseteq C\). \(\square\)

## 4. The return map contracts noncompactness

**Lemma 4.1.** For \(v,v'\in E\), with the quantities of \(v'\) marked by primes,
\[
\|g(v)-g(v')\|\le\gamma\|v-v'\|+\frac2\epsilon\bigl(|u-u'|+|p-p'|\bigr),\qquad\gamma=\Bigl(1-\frac M{1+t}\Bigr)^2<1.
\]

**Proof.** From \(g(v)=(ty-z)/r\) and \(\|ty-z'\|=r'\),
\[
r\|g(v)-g(v')\|=\Bigl\|(ty-z)-\tfrac r{r'}(ty-z')\Bigr\|\le\|z-z'\|+|r-r'|.
\]
Since \(f\) is an isometry, \(\|z-z'\|=\|uw-u'w'\|\le|u-u'|+u\|w-w'\|\). In the same way, from \(w=(f(x(v))-tb)/s\),
\[
s\|w-w'\|\le\|f(x(v))-f(x(v'))\|+|s-s'|=\|pv-p'v'\|+|s-s'|\le p\|v-v'\|+|p-p'|+|s-s'|.
\]
On \(E\) we have \(s=p+M\) and \(r=u+M\) (Lemma 2.2), so \(|s-s'|=|p-p'|\) and \(|r-r'|=|u-u'|\). Combining,
\[
\|g(v)-g(v')\|\le\frac{up}{rs}\|v-v'\|+\frac{2|u-u'|}r+\frac{2u|p-p'|}{rs}.
\]
Here \(\frac{up}{rs}=(1-\frac Mr)(1-\frac Ms)\le\gamma\) because \(r,s\le1+t\), and \(\frac ur<1\), \(r,s\ge\epsilon\). \(\square\)

**Lemma 4.2.** For every nonempty \(H\subseteq C\), \(\chi(g(H))\le\gamma\chi(H)\).

**Proof.** Let \(H\) be covered by finitely many sets \(H_1,\dots,H_N\subseteq H\) of diameter at most \(\delta\), and let \(\eta>0\). Divide \([\epsilon,1+t]\) into finitely many intervals of length at most \(\eta\), and split each \(H_j\) according to the intervals containing \(p(v)\) and \(u(v)\). On each of the finitely many resulting pieces, Lemma 4.1 gives \(\|g(v)-g(v')\|\le\gamma\delta+4\eta/\epsilon\), since \(C\subseteq E\). So \(g(H)\) is covered by finitely many sets of diameter at most \(\gamma\delta+4\eta/\epsilon\). Letting \(\eta\to0\) and then \(\delta\downarrow\chi(H)\) proves the claim. \(\square\)

## 5. Aligned chords

**Proposition 5.1.** Under the standing assumptions there are \(v\in S_X\), \(w\in S_Y\) and numbers \(p,r,s,u\in[\epsilon,1+t]\) such that the points
\[
x=ty+pv,\qquad z=ty-rv\qquad\text{lie in }S_X,\qquad f(x)=tb+sw,\qquad f(z)=tb-uw,\tag{5.1}
\]
and
\[
s-p=r-u=M,\qquad d:=p+r=s+u=\|x-z\|\le2.\tag{5.2}
\]

**Proof.** By Lemmas 3.1 and 4.2, Darbo's theorem (Theorem 6.1 of the previous lesson) applies to \(g\) on \(C\), in the Banach space \(X\), and gives \(v\in C\) with \(g(v)=v\). Take \(x=x(v)\), \(z=z(v)=ty-r\,g(v)=ty-rv\), and \(p,s,u,r,w\) as in Section 1. Since \(v\in E\), Lemma 2.2 gives \(s-p=r-u=M\) and \(\|x-z\|=p+r=s+u\), and \(\|x-z\|\le\|x\|+\|z\|=2\). \(\square\)

Both chords lie on lines: the chord \([z,x]\) of the unit ball of \(X\) through \(ty\) has direction \(v\), and its image chord \([f(z),f(x)]\) through \(tb\) has direction \(w\). The segment from \(ty\) to \(x\) has length \(p\), and its image segment from \(tb\) to \(f(x)\) is longer by exactly \(M\); on the other side the segment from \(ty\) to \(z\) is longer than the image segment by exactly \(M\). The point \(x\) need not equal \(x_0\).

## 6. Exercises

**Exercise 6.1** (easy). Show that if \(f\) is the restriction of a linear isometry \(T\), then \(g(v)=v\) for every \(v\in S_X\), with \(w=Tv\), \(s=p\) and \(u=r\).

**Exercise 6.2** (medium). Show that the constant \(\gamma\) of Lemma 4.1 can be replaced by \(\sup_{v\in E}\frac{u(v)p(v)}{r(v)s(v)}\), and explain why the argument needs \(M>0\): what happens to the estimate when \(M=0\)?

**Exercise 6.3** (easy). Let \(\varphi_n\) be the common support of \(a_n\) and \(v_{n+1}\) in the proof of Lemma 3.1. Show that \(\varphi_n=1\) on \(\overline{\operatorname{conv}}\{v_0,\dots,v_{n+1}\}\), and that this set consists of unit vectors.

**Exercise 6.4** (medium). Show that a single \(\varphi\in X^*\) with \(\|\varphi\|\le1\) equals \(1\) on all of \(C\). (Use the Banach–Alaoglu theorem.)

## 7. Solutions

**6.1.** Then \(f(x(v))=T(ty+pv)=tb+pTv\), so \(s=p\) and \(w=Tv\); the opposite contact in \(Y\) is \(tb-rTv=T(ty-rv)\), where \(ty-rv\in S_X\) is the opposite contact of the line in \(X\), so \(u=r\), \(z=ty-rv\), and \(g(v)=v\).

**6.2.** The first term of the last display in the proof of Lemma 4.1 is \(\frac{up}{rs}\|v-v'\|\), so the supremum over \(E\) can replace \(\gamma\). When \(M=0\), \(\frac{up}{rs}=1\) and no contraction results; positivity of \(M\) makes the factor \((1-\frac Mr)(1-\frac Ms)\) strictly less than \(1\), uniformly because \(r,s\le1+t\).

**6.3.** \(\varphi_n\) has norm at most \(1\) and equals \(1\) on \(\operatorname{conv}\{v_0,\dots,v_{n+1}\}\), as shown in the proof; by continuity it equals \(1\) on the closure, and \(1=\varphi_n(l)\le\|l\|\le1\) there.

**6.4.** For each \(i\), \(\varphi_n(v_i)=1\) for all \(n\ge i\), by Exercise 6.3. By the Banach–Alaoglu theorem the sequence \((\varphi_n)\) has a weak\* limit point \(\varphi\) in the unit ball of \(X^*\). For \(N\ge i\), the weak\* closed set \(\{\psi:\psi(v_i)=1\}\) contains every \(\varphi_n\) with \(n\ge N\), hence \(\varphi\); so \(\varphi(v_i)=1\) for all \(i\), and \(\varphi=1\) on \(C\) by linearity and continuity. The argument of the lesson does not need this.

## References

- [OpenAI-T] OpenAI, *A positive solution to Tingley's problem*, OpenAI Math Release preprint, 23 September 2026, Section 4. https://github.com/openai/math/blob/main/preprints/A-positive-solution-to-Tingleys-problem-September-23-2026
