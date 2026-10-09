# Sensitivity, block sensitivity and composition

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A Boolean function on \(n\) bits can be studied through how its value reacts to changes of the input. *Sensitivity* counts the single bits whose flip changes the value; *block sensitivity* counts disjoint groups of bits whose flip changes it. Block sensitivity is at least sensitivity, and Nisan introduced it in 1989 in the study of parallel computation. The *Sensitivity Conjecture* asked whether block sensitivity is bounded by a polynomial in sensitivity; Huang proved in 2019 that \(\operatorname{bs}(f)\le s(f)^4\) for every Boolean function [Huang]. Whether a quadratic bound \(\operatorname{bs}(f)\le Cs(f)^2\) holds was open; OpenAI showed in September 2026 that it fails for every constant \(C\) [OpenAI-S]. This course proves that result.

The present lesson sets up the two measures and the tools used to combine functions: disjoint ORs, which balance sensitivity at the two values (Lemma 2.1), and composition, which multiplies the measures (Lemma 4.1). Section 3 gives a classical example with block sensitivity a quarter of the square of sensitivity, and Section 4 shows that one function with \(\operatorname{bs}(f,0)>s(f)^2\) gives, by repeated composition, a separation by a fixed power larger than \(2\) (Proposition 4.2). The lessons [Nested predicates on a labelled tournament](nested-predicates-on-a-labelled-tournament.md) and [Sensitivity recurrences and a superquadratic separation](sensitivity-recurrences-and-a-superquadratic-separation.md) construct such functions.

Nothing beyond finite counting is used.

## 1. Sensitivity and block sensitivity

Write \([n]=\{1,\dots,n\}\). For \(x\in\{0,1\}^n\) and \(B\subseteq[n]\), let \(x^B\) be \(x\) with the coordinates in \(B\) flipped, and \(x^a=x^{\{a\}}\). Let \(f:\{0,1\}^n\to\{0,1\}\) be a Boolean function (defined on all inputs).

- The *sensitivity* of \(f\) at \(x\) is \(s(f,x)=|\{a\in[n]:f(x^a)\neq f(x)\}|\), and \(s(f)=\max_xs(f,x)\).
- A *sensitive block* of \(f\) at \(x\) is a nonempty \(B\subseteq[n]\) with \(f(x^B)\neq f(x)\). The *block sensitivity* \(\operatorname{bs}(f,x)\) is the largest number of pairwise disjoint sensitive blocks at \(x\), and \(\operatorname{bs}(f)=\max_x\operatorname{bs}(f,x)\).
- For \(b\in\{0,1\}\), \(s_b(f)=\max\{s(f,x):f(x)=b\}\), with \(s_b(f)=0\) if \(f\) never takes the value \(b\). Thus \(s(f)=\max\{s_0(f),s_1(f)\}\).

The sensitive coordinates at \(x\) form disjoint sensitive blocks \(\{a\}\), so \(s(f,x)\le\operatorname{bs}(f,x)\le n\). A constant function has \(s(f)=\operatorname{bs}(f)=0\); a nonconstant one has \(s(f)\ge1\), because along a path of single flips between inputs with different values some flip changes the value.

## 2. Disjoint ORs

For \(P:\{0,1\}^N\to\{0,1\}\) and \(m\ge1\), the *disjoint OR* of \(m\) copies of \(P\) is the function on \(mN\) bits
\[
F(x_1,\dots,x_m)=P(x_1)\vee\dots\vee P(x_m),\qquad x_i\in\{0,1\}^N.
\]

**Lemma 2.1** (disjoint ORs). \(s_0(F)\le m\,s_0(P)\) and \(s_1(F)\le s_1(P)\). If \(P(0)=0\), then \(F(0)=0\) and \(\operatorname{bs}(F,0)\ge m\operatorname{bs}(P,0)\).

**Proof.** At an input with \(F=0\), every copy has \(P(x_i)=0\). A flip changes only one copy, and it changes \(F\) only if it makes that copy accept, so there are at most \(s(P,x_i)\le s_0(P)\) such flips in copy \(i\); in total at most \(m\,s_0(P)\). At an input with \(F=1\), if two or more copies accept, no single flip makes \(F\) zero. If exactly one copy \(x_i\) accepts, a flip changes \(F\) only if it lies in \(x_i\) and makes \(P(x_i)=0\): at most \(s_1(P)\) flips. If \(P(0)=0\), the all-zero input has \(F(0)=0\); a sensitive block of \(P\) at \(0\) inside copy \(i\) makes copy \(i\), hence \(F\), accept. Blocks in different copies are disjoint, so families of disjoint sensitive blocks in the \(m\) copies combine. \(\square\)

So the OR multiplies the zero-side sensitivity and the block sensitivity at zero by \(m\), but leaves the one-side sensitivity alone. This is used to balance the two sides: Ambainis and Sun used it for their quadratic examples [AS, Section 4].

## 3. A quadratic example

For \(k\ge1\) let \(g_k:\{0,1\}^{2k}\to\{0,1\}\), with the coordinates grouped into \(k\) pairs \(\{2j-1,2j\}\), accept exactly the \(k\) inputs that are \(1\) on one pair and \(0\) elsewhere. Let \(R_k\) be the disjoint OR of \(k\) copies of \(g_k\), a function on \(2k^2\) bits.

**Proposition 3.1** (an example of Rubinstein). \(s(R_k)=2k\) and \(\operatorname{bs}(R_k,0)\ge k^2\). Hence \(\operatorname{bs}(R_k)\ge\frac14s(R_k)^2\).

**Proof.** If \(g_k(y)=1\), every flip leaves the set of accepted inputs: a flip inside the pair leaves a single \(1\), and a flip outside adds a third \(1\). So \(s(g_k,y)=2k\) and \(s_1(g_k)=2k\). If \(g_k(y)=0\) and a flip of coordinate \(a\) makes \(y\) accepted, then \(y^a\) is \(1\) exactly on one pair \(\{2j-1,2j\}\); so \(y\) is \(1\) exactly on \(\{2j-1,2j\}\triangle\{a\}\). A set \(S\) determines the possible \(a\): if \(|S|=1\), \(a\) is the partner of the element of \(S\); if \(|S|=3\), \(S\) contains exactly one pair and \(a\) is its third element. So \(s_0(g_k)\le1\). The pairs are disjoint sensitive blocks of \(g_k\) at \(0\), so \(\operatorname{bs}(g_k,0)\ge k\). Lemma 2.1 with \(m=k\) gives \(s_0(R_k)\le k\), \(s_1(R_k)\le2k\) and \(\operatorname{bs}(R_k,0)\ge k^2\). At an input where exactly one copy accepts all \(2k\) coordinates of that copy are sensitive, so \(s(R_k)=2k\). \(\square\)

Virza, and then Ambainis and Sun, improved the constant to \(\frac23\) by refining such examples [AS]. The functions of this course have \(\operatorname{bs}(f)/s(f)^2\) unbounded.

## 4. Composition

For \(f:\{0,1\}^a\to\{0,1\}\) and \(g:\{0,1\}^b\to\{0,1\}\), the *composition* \(f\circ g\) is the function on \(ab\) bits
\[
(f\circ g)(x_1,\dots,x_a)=f\bigl(g(x_1),\dots,g(x_a)\bigr),\qquad x_i\in\{0,1\}^b.
\]
We index its coordinates by \([a]\times[b]\), the coordinate \((i,c)\) being coordinate \(c\) of \(x_i\).

**Lemma 4.1** (composition). \(s(f\circ g)\le s(f)\,s(g)\). If \(g(0)=0\), then \((f\circ g)(0)=f(0)\) and \(\operatorname{bs}(f\circ g,0)\ge\operatorname{bs}(f,0)\operatorname{bs}(g,0)\).

**Proof.** Fix \(x=(x_1,\dots,x_a)\) and let \(y=(g(x_1),\dots,g(x_a))\). Flipping coordinate \((i,c)\) changes at most the \(i\)-th entry of \(y\); it changes \(f\circ g\) exactly when it changes \(g(x_i)\) and \(f(y^i)\neq f(y)\). Hence
\[
s(f\circ g,x)=\sum_{i:\,f(y^i)\neq f(y)}s(g,x_i)\le s(f,y)\,s(g)\le s(f)\,s(g).
\]
Now let \(g(0)=0\), so the all-zero input gives \(y=0\). Let \(C_1,\dots,C_p\subseteq[a]\) be disjoint sensitive blocks of \(f\) at \(0\) and \(D_1,\dots,D_q\subseteq[b]\) disjoint sensitive blocks of \(g\) at \(0\). The sets \(C_i\times D_j\) are nonempty and pairwise disjoint. Flipping \(C_i\times D_j\) at \(0\) turns exactly the children \(x_l\), \(l\in C_i\), into \(0^{D_j}\), where \(g\) is \(1\); so \(y\) becomes \(0^{C_i}\), where \(f\) differs from \(f(0)\). This gives \(pq\) disjoint sensitive blocks. \(\square\)

**Proposition 4.2** (powering). Let \(f\) be a Boolean function with \(f(0)=0\), \(s(f)\le A\) and \(\operatorname{bs}(f,0)\ge B\), where \(A>1\) and \(B>A^2\). Put \(F_1=f\) and \(F_{m+1}=f\circ F_m\), and \(\alpha=\log B/\log A>2\). Then for every \(m\ge1\), \(F_m(0)=0\), \(F_m\) is nonconstant, and
\[
\operatorname{bs}(F_m)\ge\operatorname{bs}(F_m,0)\ge B^m\ge s(F_m)^\alpha,\qquad\frac{\operatorname{bs}(F_m)}{s(F_m)^2}\ge\Bigl(\frac B{A^2}\Bigr)^m.
\]

**Proof.** By induction with Lemma 4.1, \(F_m(0)=0\), \(s(F_m)\le A^m\) and \(\operatorname{bs}(F_m,0)\ge B^m\ge1\); the last bound gives a sensitive block, so \(F_m\) is nonconstant. Then \(s(F_m)^\alpha\le A^{m\alpha}=B^m\), and \(B^m/s(F_m)^2\ge B^m/A^{2m}\). \(\square\)

Ambainis and Prūsis observed that a single function with \(\operatorname{bs}(f)>s(f)^2\) would give a power separation in this way [AP, Section 1], and Tal studied composition systematically [Tal]. Such a function is constructed in [Sensitivity recurrences and a superquadratic separation](sensitivity-recurrences-and-a-superquadratic-separation.md).

## 5. Exercises

**Exercise 5.1** (easy). Compute \(s\) and \(\operatorname{bs}\) of \(\mathrm{OR}_n(x)=x_1\vee\dots\vee x_n\) and of \(\mathrm{AND}_n\).

**Exercise 5.2** (easy). Show that \(\operatorname{bs}(f,x)\le n\) and that a minimal sensitive block \(B\) at \(x\) (no proper nonempty subset is a sensitive block) has every coordinate of \(B\) sensitive at \(x^B\).

**Exercise 5.3** (medium). Let \(f=\mathrm{OR}_a\) and \(g=\mathrm{AND}_b\). Compute \(s(f\circ g)\) and compare with \(s(f)s(g)\).

**Exercise 5.4** (medium). Show that the condition \(g(0)=0\) in Lemma 4.1 cannot be dropped: give \(f,g\) with \(g(0)=1\) and \(\operatorname{bs}(f\circ g,0)<\operatorname{bs}(f,0)\operatorname{bs}(g,0)\).

## 6. Solutions

**5.1.** At \(x=0\) every coordinate is sensitive for \(\mathrm{OR}_n\), so \(s(\mathrm{OR}_n)=\operatorname{bs}(\mathrm{OR}_n)=n\). For \(\mathrm{AND}_n\) use \(x=(1,\dots,1)\): again both equal \(n\).

**5.2.** Disjoint nonempty subsets of \([n]\) number at most \(n\). If \(B\) is minimal and \(a\in B\), then \(B\setminus\{a\}\) is not a sensitive block (or is empty), so \(f(x^{B\setminus\{a\}})=f(x)\neq f(x^B)\); and \(x^{B\setminus\{a\}}=(x^B)^a\).

**5.3.** \(f\circ g\) is the OR of \(a\) ANDs of \(b\) bits. At an input where every AND is \(0\) and each block has exactly one zero, each of the \(a\) zeros is sensitive, so \(s_0(f\circ g)\ge a\); at most one bit per block can turn its AND on, so \(s_0(f\circ g)=a\). At an input with exactly one AND equal to \(1\), its \(b\) bits are sensitive, so \(s_1(f\circ g)=b\). Hence \(s(f\circ g)=\max\{a,b\}\), much less than \(s(f)s(g)=ab\) when \(a,b\ge2\).

**5.4.** Take \(g=\mathrm{NOT}\) on one bit, so \(g(0)=1\) and \(\operatorname{bs}(g,0)=1\), and \(f=\mathrm{OR}_2\), so \(\operatorname{bs}(f,0)=2\). Then \((f\circ g)(x_1,x_2)=\overline{x_1}\vee\overline{x_2}\) equals \(1\) at \(0\), and a flip changes it only if it makes both \(x_1\) and \(x_2\) equal to \(1\). The only sensitive block at \(0\) is \(\{1,2\}\), so \(\operatorname{bs}(f\circ g,0)=1<2=\operatorname{bs}(f,0)\operatorname{bs}(g,0)\).

## References

- [AP] A. Ambainis and K. Prūsis, *A tight lower bound on certificate complexity in terms of block sensitivity and sensitivity*, ECCC TR14-027, revision 1 (2014). https://eccc.weizmann.ac.il/report/2014/027/
- [AS] A. Ambainis and X. Sun, *New separation between s(f) and bs(f)*, arXiv:1108.3494 (2011). https://arxiv.org/abs/1108.3494
- [Huang] H. Huang, *Induced subgraphs of hypercubes and a proof of the Sensitivity Conjecture*, Ann. of Math. 190 (2019); arXiv:1907.00847. https://arxiv.org/abs/1907.00847
- [OpenAI-S] OpenAI, *A superquadratic separation between sensitivity and block sensitivity*, OpenAI Math Release preprint, 25 September 2026. https://github.com/openai/math/tree/main/preprints/A-superquadratic-separation-between-sensitivity-and-block-sensitivity-September-25-2026
- [Tal] A. Tal, *Properties and applications of Boolean function composition*, ECCC TR12-163 (2012). https://eccc.weizmann.ac.il/report/2012/163/
