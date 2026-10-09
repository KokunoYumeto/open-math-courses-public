# Tingley's problem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson shows that the aligned chords of [Aligned chords](aligned-chords.md) cannot exist (Proposition 4.1) and deduces OpenAI's solution of Tingley's problem [OpenAI-T, Sections 5 and 6]:

**Theorem 5.1** (OpenAI). Let \(X,Y\) be nonzero real Banach spaces and \(f:S_X\to S_Y\) a surjective isometry. Then the radial map \(T(0)=0\), \(T(x)=\|x\|f(x/\|x\|)\), is a surjective real-linear isometry, and it is the only linear map extending \(f\).

The contradiction comes from two kinds of test. Perturbing the radius \(t\) in the defect at the two ends of the chords gives a secant estimate for the norm along the line \(v\) shifted by a multiple of \(y\) (Lemma 2.1). If one of the two half-chords is long compared with \(1-t\), the secant estimate forces the defect to grow under a small change of radius (Lemma 3.3). Otherwise convexity of \(\lambda\mapsto\|y+\lambda v\|\) and \(\lambda\mapsto\|b+\lambda w\|\) gives two incompatible values for one distance that \(f\) preserves (Proposition 4.1).

We use: from [Supports, radial contact and the Mazur–Ulam theorem](supports-radial-contact-and-the-mazur-ulam-theorem.md), supports, Lemma 1.2 (supports and secants), the monotonicity of secant slopes, Lemma 4.1 and Proposition 4.2; from [Ultrapowers and Darbo's fixed-point theorem](ultrapowers-and-darbos-fixed-point-theorem.md), Proposition 3.1; from [Aligned chords](aligned-chords.md), Proposition 5.1; and the Hahn–Banach theorem, [Corollary 2.3 of the Banach space lesson](course:foundations-of-von-neumann-algebras/hahn-banach-baire-and-the-basic-theorems-on-banach-spaces#OA-FND-HB-02).

## 1. Chord configurations

A *chord configuration* consists of real Banach spaces \(X,Y\), a surjective isometry \(f:S_X\to S_Y\) with defect bound
\[
|D_q(a,c)|\le M\qquad(a,c\in S_X,\ 0\le q\le1)\tag{1.1}
\]
for a number \(M>0\), a number \(0<t<1\), a point \(y\in S_X\) with \(b=f(y)\), directions \(v\in S_X\), \(w\in S_Y\), and positive numbers \(p,r,s,u\) such that
\[
x=ty+pv\in S_X,\quad z=ty-rv\in S_X,\quad f(x)=tb+sw,\quad f(z)=tb-uw,\tag{1.2}
\]
\[
s-p=r-u=M,\qquad d:=p+r=s+u\le2.\tag{1.3}
\]
Proposition 5.1 of the lesson on aligned chords produces one from an attained defect. Put
\[
\epsilon=1-t,\qquad A=\frac pd,\qquad B=\frac ud.
\]
Then \(A,B>0\) and \(A+B=\frac{p+u}d=1-\frac Md<1\); in particular \(A,B<1\). Moreover \(r=u+M>u\) and \(s=p+M>p\), so \(\frac ru>1>\frac ps\).

**Lemma 1.1** (the inverse configuration). If the data above form a chord configuration, so do \(f^{-1}:S_Y\to S_X\), the same \(M\) and \(t\), the point \(y'=b\) (so \(f^{-1}(y')=y\)), the directions \(v'=-w\), \(w'=-v\), and the numbers \((p',r',s',u')=(u,s,r,p)\). For it, \((A',B')=(B,A)\).

**Proof.** By Lemma 4.1(a) of the first lesson, \(f^{-1}\) satisfies (1.1). The new points are \(x'=tb+uv'=tb-uw=f(z)\in S_Y\) and \(z'=tb-sv'=tb+sw=f(x)\in S_Y\), and \(f^{-1}(x')=z=ty+r(-v)=ty+s'w'\), \(f^{-1}(z')=x=ty-p(-v)=ty-u'w'\). Then \(s'-p'=r-u=M\), \(r'-u'=s-p=M\) and \(p'+r'=u+s=d\). Finally \(A'=p'/d=B\) and \(B'=u'/d=A\). \(\square\)

## 2. A secant estimate

**Lemma 2.1.** In a chord configuration put
\[
h=\min\Bigl\{\frac ts,\frac\epsilon u\Bigr\},\qquad\theta=\frac{hs}p,\qquad K=\frac{\|\frac ruv+hy\|-\|\frac psv+hy\|}{\frac ru-\frac ps}.
\]
Then \(v+\theta y\neq0\), and every support \(\varphi\) at \(v+\theta y\) satisfies
\[
\frac\epsilon p\le\varphi(v)\le K,\qquad\text{where }K\le1-B\text{ if }B\le\epsilon,\quad K\le B\text{ if }B>\epsilon.\tag{2.1}
\]

**Proof.** *The bound on \(K\).* The radius \(t-sh\) lies in \([0,t]\) because \(h\le t/s\), and
\[
\Delta_x:=D_{t-sh}(x,y)=\|sw+shb\|-\|pv+shy\|=s\Bigl(\|w+hb\|-\Bigl\|\tfrac psv+hy\Bigr\|\Bigr).
\]
The radius \(t+uh\) lies in \([t,1]\) because \(h\le\epsilon/u\), and
\[
\Delta_z:=-D_{t+uh}(z,y)=\|rv+uhy\|-\|uw+uhb\|=u\Bigl(\Bigl\|\tfrac ruv+hy\Bigr\|-\|w+hb\|\Bigr).
\]
Both are at most \(M\) by (1.1). The common term \(\|w+hb\|\) cancels in \(u\Delta_x+s\Delta_z=su\bigl(\frac ru-\frac ps\bigr)K=(sr-up)K\), and \(sr-up=(p+M)(u+M)-up=M(p+u+M)=Md\). So
\[
MK=\frac{u\Delta_x+s\Delta_z}d.
\]
The inequality \(\frac ts\le\frac\epsilon u\) means \(tu\le(1-t)s\), that is \(td\le s=d-u\), that is \(B\le\epsilon\). If \(B\le\epsilon\), then \(h=t/s\), the radius \(t-sh\) is \(0\), \(\Delta_x=D_0(x,y)=0\), and \(MK=s\Delta_z/d\le sM/d\), so \(K\le\frac sd=1-B\). If \(B>\epsilon\), then \(h=\epsilon/u\), the radius \(t+uh\) is \(1\), \(\Delta_z=0\), and \(K\le\frac ud=B\).

*The vector \(v+\theta y\) is not zero.* Otherwise \(\theta=1\) and \(v=-y\); then \(1=\|ty+pv\|=|t-p|\) forces \(p=1+t\), while \(\theta=\frac{hs}p\le\frac tp<1\).

*The upper bound for \(\varphi(v)\).* Since \(\frac ps(v+\theta y)=\frac psv+hy\), the support \(\varphi\) is also a support at \(\frac psv+hy\). Lemma 1.2 of the first lesson, for \(\lambda\mapsto\|\lambda v+hy\|\) at \(\lambda_0=\frac ps<\frac ru\), gives \(\varphi(v)\le K\).

*The lower bound.* Put \(\beta=t/p\), so \(0<\theta\le\beta\), and note \(p(v+\beta y)=x\). A support \(\psi\) at \(v+\beta y\) is a support at \(x\), so \(1=\psi(x)=p\psi(v)+t\psi(y)\le p\psi(v)+t\), that is \(\psi(v)\ge\epsilon/p\). If \(\theta=\beta\), apply this to \(\psi=\varphi\). If \(\theta<\beta\), take any support \(\psi\) at \(v+\beta y\). The two support properties give \(\varphi(v+\theta y)\ge\psi(v+\theta y)\) and \(\psi(v+\beta y)\ge\varphi(v+\beta y)\), that is
\[
\theta\bigl(\psi(y)-\varphi(y)\bigr)\le\varphi(v)-\psi(v)\le\beta\bigl(\psi(y)-\varphi(y)\bigr).
\]
As \(\theta<\beta\), this forces \(\psi(y)-\varphi(y)\ge0\), and then \(\varphi(v)\ge\psi(v)\ge\epsilon/p\). \(\square\)

## 3. Long half-chords are impossible

**Lemma 3.1.** In a chord configuration, if \(B>\epsilon\), then \(A>\epsilon\) and every support at \(v\) is strictly negative on \(y\).

**Proof.** Here \(h=\epsilon/u\) and \(\theta=\frac{\epsilon s}{up}\). By (2.1), \(\frac\epsilon p\le K\le B=\frac ud\), so
\[
\frac{pu}{d\epsilon}\ge1.\tag{3.1}
\]
Let \(L\) be a support at \(v\) and \(j=L(y)\); let \(\varphi\) be a support at \(v+\theta y\). By (2.1), \(B\ge\varphi(v)\); moreover \(\varphi(y)\le1\) and \(\|v+\theta y\|\ge L(v+\theta y)=1+\theta j\), so
\[
B\ge\varphi(v)=\|v+\theta y\|-\theta\varphi(y)\ge(1+\theta j)-\theta.\tag{3.2}
\]
Equality throughout (3.2) is impossible: it would give \(\|v+\theta y\|=L(v+\theta y)\), so \(L\) would be a support at \(v+\theta y\), and (2.1) would give \(1=L(v)\le B<1\). So \(B>1-\theta(1-j)\), that is
\[
1-j>\frac{1-B}\theta=\frac sd\cdot\frac{up}{\epsilon s}=\frac{pu}{d\epsilon}\ge1,
\]
and \(j<0\). Since \(L\) was arbitrary, every support at \(v\) is negative on \(y\). Applying such an \(L\) to \(rv-ty=-z\) gives \(r-tj\le\|z\|=1\), so \(r<1\) and \(u<r<1\). Then (3.1) gives \(A=\frac pd\ge\frac\epsilon u>\epsilon\). \(\square\)

**Lemma 3.2.** Let \(a,e\) be vectors in a real normed space, \(a\neq0\), such that every support at \(a\) is strictly negative on \(e\). Then \(\|a+\eta e\|<\|a\|\) for all sufficiently small \(\eta>0\).

**Proof.** Otherwise there are \(\eta_n\downarrow0\) with \(\|a+\eta_ne\|\ge\|a\|\). Let \(V\) be the span of \(a\) and \(e\), and choose supports \(L_n\) at \(a+\eta_ne\) in the dual of \(V\) (the Hahn–Banach theorem in \(V\)). Then \(\|a\|\le\|a+\eta_ne\|=L_n(a)+\eta_nL_n(e)\le\|a\|+\eta_nL_n(e)\), so \(L_n(e)\ge0\). The unit ball of the dual of the finite-dimensional space \(V\) is compact, so a subsequence converges to some \(L\) with \(\|L\|\le1\), \(L(e)\ge0\) and \(L(a)=\lim_n\bigl(\|a+\eta_ne\|-\eta_nL_n(e)\bigr)=\|a\|\). An extension of \(L\) to the whole space with the same norm is a support at \(a\) that is not negative on \(e\), a contradiction. \(\square\)

**Lemma 3.3.** In a chord configuration, \(A\le\epsilon\) and \(B\le\epsilon\).

**Proof.** Suppose \(B>\epsilon\). By Lemma 3.1, \(A>\epsilon\) and every support at \(v\) is negative on \(y\). If instead \(A>\epsilon\), apply Lemma 3.1 to the inverse configuration of Lemma 1.1, for which \(B'=A>\epsilon\): it gives \(A'=B>\epsilon\). So in either case \(A>\epsilon\) and \(B>\epsilon\), and Lemma 3.1 applies to both configurations. For the inverse one it says that every support at \(v'=-w\) is negative on \(y'=b\); as the supports at \(w\) are the negatives of the supports at \(-w\), every support at \(w\) is strictly positive on \(b\).

Now let \(0<\eta<t\). The defect at the radius \(t-\eta\) satisfies, by (1.1),
\[
\|sw+\eta b\|-\|pv+\eta y\|=D_{t-\eta}(x,y)\le M=s-p.\tag{3.3}
\]
A support \(L\) at \(w\) gives \(\|sw+\eta b\|\ge L(sw+\eta b)=s+\eta L(b)>s\). By Lemma 3.2 with \(a=pv\) and \(e=y\) (the supports at \(pv\) are those at \(v\)), \(\|pv+\eta y\|<p\) for small \(\eta>0\). For such \(\eta\) the left side of (3.3) exceeds \(s-p\), a contradiction. \(\square\)

## 4. No chord configuration exists

**Proposition 4.1.** There is no chord configuration.

**Proof.** By Lemma 3.3, applied to a configuration and to its inverse, \(A\le\epsilon\) and \(B\le\epsilon\). Lemma 2.1 with \(B\le\epsilon\) gives \(\frac\epsilon p\le1-B\), that is \(\epsilon\le dA(1-B)\); for the inverse configuration, where \(B'=A\le\epsilon\) and \(p'=u\), it gives \(\epsilon\le dB(1-A)\). The smaller of \(A(1-B)\) and \(B(1-A)\) is less than \(\frac14\): if \(A\le B\), then \(2A\le A+B<1\) and \(A(1-B)\le A(1-A)<\frac14\), and symmetrically otherwise. Since \(d\le2\), we get \(\epsilon<\frac12\), so \(\epsilon<t\). Hence \(A\le\epsilon<t\) and \(1-B\ge1-\epsilon=t\), that is
\[
p<td,\qquad r=d-p>\epsilon d,\qquad s=d-u\ge td,\qquad u\le\epsilon d,
\]
and therefore
\[
\frac pt<d<\frac r\epsilon,\qquad\frac u\epsilon\le d\le\frac st.\tag{4.1}
\]
Consider the convex functions \(F(\lambda)=\|y+\lambda v\|\) and \(G(\lambda)=\|b+\lambda w\|\). We have \(F(0)=G(0)=1\), and \(F(\frac pt)=\frac1t\|ty+pv\|=\frac1t\) and \(G(\frac st)=\frac1t\). By the monotonicity of secant slopes and (4.1),
\[
F\Bigl(\frac r\epsilon\Bigr)\ge1+\frac{r/\epsilon}{p/t}\Bigl(\frac1t-1\Bigr)>1+\Bigl(\frac1t-1\Bigr)=\frac1t,
\]
while \(\frac u\epsilon\in[0,\frac st]\) and convexity give \(G(\frac u\epsilon)\le\max\{G(0),G(\frac st)\}=\frac1t\). But \(f\) preserves the distance between \(y\) and \(z\):
\[
\epsilon F\Bigl(\frac r\epsilon\Bigr)=\|\epsilon y+rv\|=\|y-z\|=\|f(y)-f(z)\|=\|\epsilon b+uw\|=\epsilon G\Bigl(\frac u\epsilon\Bigr),
\]
a contradiction. \(\square\)

## 5. The theorem

**Proof of Theorem 5.1.** Suppose the defect \(M\) of \(f\) were positive. Proposition 3.1 of the lesson on ultrapowers gives Banach spaces, a surjective sphere isometry and an attained defect as in (0.1) of the lesson on aligned chords, and Proposition 5.1 there gives a chord configuration, contradicting Proposition 4.1. So \(M=0\), and Proposition 4.2 of the first lesson shows that \(T\) is a surjective real-linear isometry and the only linear extension of \(f\). \(\square\)

**Corollary 5.2.** Theorem 5.1 holds for nonzero real normed spaces \(X,Y\).

**Proof.** Proposition 3.1 of the lesson on ultrapowers applies to normed spaces and produces Banach spaces, and Proposition 4.2 of the first lesson holds for normed spaces. So the proof of Theorem 5.1 applies verbatim. \(\square\)

**Remarks.** (1) The unit sphere of a real normed space, as a metric space, determines the space up to linear isometry: two spaces whose spheres are isometric are linearly isometric.

(2) For complex normed spaces regarded as real spaces, the extension is real-linear, and it need not be complex-linear (Exercise 5.2 of the first lesson).

(3) The proof uses the ultrapower only to make the defect attained, and Darbo's theorem only to find a fixed direction of the return map; everything else is support and convexity geometry in the plane spanned by two vectors.

## 6. Exercises

**Exercise 6.1** (easy). Show that the sets \(\{A\le\epsilon\}\) and \(\{B\le\epsilon\}\) in Lemma 3.3 are exchanged by passing to the inverse configuration, and that the inverse of the inverse configuration is the original one.

**Exercise 6.2** (easy). Deduce Remark (1) from Theorem 5.1 and Corollary 5.2.

**Exercise 6.3** (medium). Let \(F\) be a convex function on \([0,\infty)\) with \(F(0)=1\) and \(F(\lambda_1)=\frac1t>1\) for some \(\lambda_1>0\). Show that \(F(\lambda)>\frac1t\) for every \(\lambda>\lambda_1\) and \(F(\lambda)\le\frac1t\) for \(0\le\lambda\le\lambda_1\). Where are these two facts used?

**Exercise 6.4** (easy). Show that every surjective isometry \(f\) between unit spheres of real normed spaces preserves antipodal points: \(f(-x)=-f(x)\). (Tingley proved this for finite-dimensional spaces in his original paper.)

## 7. Solutions

**6.1.** By Lemma 1.1, \((A',B')=(B,A)\). Applying Lemma 1.1 twice returns \(f\), the point \(f^{-1}(b)=y\), the directions \(-(-v)=v\) and \(-(-w)=w\), and the numbers \((p,r,s,u)\).

**6.2.** If \(f:S_X\to S_Y\) is a surjective isometry, its radial extension is a surjective linear isometry \(X\to Y\).

**6.3.** For \(\lambda>\lambda_1\), monotonicity of secant slopes from \(0\) gives \(\frac{F(\lambda)-1}\lambda\ge\frac{F(\lambda_1)-1}{\lambda_1}>0\), so \(F(\lambda)-1\ge\frac\lambda{\lambda_1}(F(\lambda_1)-1)>F(\lambda_1)-1\). For \(0\le\lambda\le\lambda_1\), convexity gives \(F(\lambda)\le\max\{F(0),F(\lambda_1)\}=\frac1t\). They are the two bounds for \(F(\frac r\epsilon)\) and \(G(\frac u\epsilon)\) in the proof of Proposition 4.1.

**6.4.** By Theorem 5.1 and Corollary 5.2, \(f\) is the restriction of a linear map \(T\), and \(f(-x)=T(-x)=-T(x)=-f(x)\).

## References

- [OpenAI-T] OpenAI, *A positive solution to Tingley's problem*, OpenAI Math Release preprint, 23 September 2026, Sections 5 and 6. https://github.com/openai/math/blob/main/preprints/A-positive-solution-to-Tingleys-problem-September-23-2026
