# Two levels from reduced words

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson is about four homeomorphisms of the real line and a counting function along their orbits. Two letters \(u,v\) and their inverses act on the line so that each letter pushes almost the whole line into a small set of its own, periodically repeated. A word in the letters then moves the point \(0\) to a point that remembers the first letter of the word after all cancellations. A sum of indicator functions along the orbit of a point takes one value at the integers and another value at the integer translates of the image of \(0\); the two values differ by the length of the word after cancellation. In the last lesson these two values become the two levels between which the partial sums of a vector oscillate.

- Words, reduction, and the length of a random word after reduction (Lemma 1.1).
- Four arcs and four homeomorphisms (Lemmas 2.1 and 2.2).
- The function \(c_w\) and its invariance under reduction (Lemmas 3.1 and 3.2).
- The two levels (Lemma 3.3).

The lesson follows [OpenAI-M, Section 4 and the end of Section 5]. It needs only the real line and finite probability.

## 1. Words and reduction

Let \(\mathcal S=\{u,v,u^{-1},v^{-1}\}\) be a set of four *letters*, with the map \(s\mapsto s^{-1}\) that exchanges \(u\) with \(u^{-1}\) and \(v\) with \(v^{-1}\). The letters \(u,v\) are *positive*, the letters \(u^{-1},v^{-1}\) are *negative*. A *word* is a finite sequence \(w=s_1s_2\cdots s_k\) of letters; \(k\) is its length. A word is *reduced* if no letter is followed by its inverse.

The *reduced form* \(\operatorname{red}(w)\) is defined by reading \(w\) from the left: start with the empty word; when the letter \(s\) is read and the word kept so far ends with \(s^{-1}\), delete this last letter; otherwise append \(s\). The result is reduced. It arises from \(w\) by deleting, several times, two adjacent letters \(s\,s^{-1}\). Let \(\ell(w)\) be the length of \(\operatorname{red}(w)\).

**Lemma 1.1.** Let \(s_1,\dots,s_n\) be independent and uniformly distributed in \(\mathcal S\), and \(\ell=\ell(s_1\cdots s_n)\). Then
\[
\mathbb E\,\ell\ge\frac n2,\qquad\Pr\Bigl(\ell\ge\frac n4\Bigr)\ge\frac14 .
\]

**Proof.** Let \(\ell_i=\ell(s_1\cdots s_i)\). If \(\ell_{i-1}>0\), the next letter is the inverse of the last kept letter with the probability \(\tfrac14\), and then \(\ell_i=\ell_{i-1}-1\); otherwise \(\ell_i=\ell_{i-1}+1\). So the conditional mean of \(\ell_i-\ell_{i-1}\), given the first \(i-1\) letters, is \(\tfrac34-\tfrac14=\tfrac12\). If \(\ell_{i-1}=0\), then \(\ell_i=1\). In both cases the conditional mean of the increment is at least \(\tfrac12\), so \(\mathbb E\,\ell\ge\tfrac n2\). Since \(0\le\ell\le n\),
\[
\frac n2\le\mathbb E\,\ell\le\frac n4+n\,\Pr\Bigl(\ell\ge\frac n4\Bigr).\qquad\blacksquare
\]

## 2. Four homeomorphisms

Choose numbers \(\alpha_s<\beta_s\) in the open interval \((0,1)\), for the four letters \(s\), such that the four closed intervals \([\alpha_s,\beta_s]\) are pairwise disjoint. Put
\[
\mathcal A_s=\bigcup_{j\in\mathbb Z}\,[\alpha_s+j,\ \beta_s+j).
\]
We call \(\mathcal A_s\) the *arc* of \(s\): it is the preimage of an arc of the circle \(\mathbb R/\mathbb Z\). The four arcs are disjoint, their closures are disjoint, and no integer lies in the closure of an arc.

**Lemma 2.1** ([OpenAI-M]). There are increasing bijections \(h_s:\mathbb R\to\mathbb R\), \(s\in\mathcal S\), that are continuous with continuous inverses, such that for all \(s\) and all real \(y\):

1. \(h_s(y+1)=h_s(y)+1\), and \(h_{s^{-1}}\) is the inverse map of \(h_s\);
2. \(h_s\) maps the complement of \(\mathcal A_{s^{-1}}\) onto \(\mathcal A_s\);
3. \(h_s\) maps the complement of the closure of \(\mathcal A_{s^{-1}}\) onto the interior of \(\mathcal A_s\);
4. \(|h_s(y)-y|<2\).

**Proof.** Let \(s\) be positive, and write \(\alpha'=\alpha_{s^{-1}}\), \(\beta'=\beta_{s^{-1}}\). Define \(h_s\) on \([\alpha',\alpha'+1]\) by
\[
\begin{gathered}
h_s(\alpha')=\beta_s-1,\qquad h_s(\beta')=\alpha_s,\\
h_s(\alpha'+1)=\beta_s ,
\end{gathered}
\]
affine on \([\alpha',\beta']\) and on \([\beta',\alpha'+1]\). Both slopes are positive, because \(\beta_s-1<\alpha_s<\beta_s\). Since \(h_s(\alpha'+1)=h_s(\alpha')+1\), the rule \(h_s(y+1)=h_s(y)+1\) extends \(h_s\) to a continuous increasing bijection of the line. Let \(h_{s^{-1}}\) be its inverse; it satisfies the same rule. This is property 1.

*Property 2 and 3 for positive \(s\).* The complement of \(\mathcal A_{s^{-1}}\) is the union of the intervals \([\beta'+j,\alpha'+j+1)\), and \(h_s\) maps each of them onto \([\alpha_s+j,\beta_s+j)\). The same holds for the open intervals.

*For negative letters.* Let \(s\) be positive. By property 2, \(h_s\) maps \(\mathcal A_{s^{-1}}\) onto the complement of \(\mathcal A_s\). So the inverse map \(h_{s^{-1}}\) maps the complement of \(\mathcal A_s\) onto \(\mathcal A_{s^{-1}}\): this is property 2 for \(s^{-1}\). In the same way, \(h_s\) maps the interior of \(\mathcal A_{s^{-1}}\), the union of the intervals \((\alpha'+j,\beta'+j)\), onto the union of the intervals \((\beta_s-1+j,\alpha_s+j)\), which is the complement of the closure of \(\mathcal A_s\). This gives property 3 for \(s^{-1}\).

*Property 4.* For positive \(s\), the function \(h_s(y)-y\) is periodic and affine between the points \(\alpha'+j\) and \(\beta'+j\). At these points it has the values \(\beta_s-1-\alpha'\in(-2,0)\) and \(\alpha_s-\beta'\in(-1,1)\). For the inverse, \(|h_{s^{-1}}(y)-y|=|x-h_s(x)|\) with \(x=h_{s^{-1}}(y)\). \(\blacksquare\)

So \(h_s\) takes everything outside the small arc of \(s^{-1}\) into the small arc of \(s\). Two such maps for different letters play a game that is known as ping-pong.

For a word \(w=s_1\cdots s_k\) put
\[
h_w=h_{s_1}\circ h_{s_2}\circ\dots\circ h_{s_k},
\]
and let \(h_w\) be the identity for the empty word. Then \(h_{ww'}=h_w\circ h_{w'}\), \(h_w(y+1)=h_w(y)+1\), and \(h_w=h_{\operatorname{red}(w)}\), because \(h_s\circ h_{s^{-1}}\) is the identity. By property 4, \(|h_w(y)-y|<2k\).

**Lemma 2.2.** Let \(w=s_1\cdots s_k\) be reduced and not empty. Then \(h_w(0)\) lies in the interior of \(\mathcal A_{s_1}\). In particular \(h_w(0)\) is not an integer.

**Proof.** By induction on \(k\). The point \(0\) is outside the closures of all arcs, so by property 3, \(h_{s_k}(0)\) lies in the interior of \(\mathcal A_{s_k}\). Let \(k\ge2\); by induction \(y=h_{s_2\cdots s_k}(0)\) lies in the interior of \(\mathcal A_{s_2}\). Since \(w\) is reduced, \(s_2\ne s_1^{-1}\), so \(\mathcal A_{s_2}\) is disjoint from the closure of \(\mathcal A_{s_1^{-1}}\). By property 3, \(h_{s_1}(y)\) lies in the interior of \(\mathcal A_{s_1}\). \(\blacksquare\)

## 3. A sum along the orbit

For a letter \(s\) define the function
\[
\chi_s(y)=\mathbf 1_{\mathcal A_s}(y)-\begin{cases}0&s\text{ positive},\\1&s\text{ negative}.\end{cases}
\]
It has the period \(1\). Its values are \(0,1\) for a positive letter and \(-1,0\) for a negative letter.

**Lemma 3.1.** For every letter \(s\) and every \(y\),
\[
\chi_{s^{-1}}\bigl(h_s^{-1}(y)\bigr)=-\chi_s(y).
\]

**Proof.** By property 2 of Lemma 2.1, \(y\in\mathcal A_s\) if and only if \(h_s^{-1}(y)\notin\mathcal A_{s^{-1}}\). So \(\mathbf 1_{\mathcal A_{s^{-1}}}(h_s^{-1}(y))=1-\mathbf 1_{\mathcal A_s}(y)\). If \(s\) is positive, the left side of the lemma is \(1-\mathbf 1_{\mathcal A_s}(y)-1=-\chi_s(y)\). If \(s\) is negative, it is \(1-\mathbf 1_{\mathcal A_s}(y)=-\chi_s(y)\). \(\blacksquare\)

**Definition.** For a word \(w=s_1\cdots s_k\) and a point \(y\) let \(y_0=y\) and \(y_i=h_{s_i}^{-1}(y_{i-1})\) for \(i=1,\dots,k\), and
\[
c_w(y)=\sum_{i=1}^k\chi_{s_i}(y_{i-1}).
\]

The points \(y_0,y_1,\dots,y_k\) are the *backward orbit* of \(y\) along \(w\); the last one is \(y_k=h_w^{-1}(y)\). The term number \(i\) asks whether the point \(y_{i-1}\) lies in the arc of the letter \(s_i\), and subtracts \(1\) for a negative letter.

**Lemma 3.2.** (1) \(c_w(y+1)=c_w(y)\).

(2) If \(w'\) arises from \(w\) by deleting two adjacent letters \(s\,s^{-1}\), then \(c_{w'}(y)=c_w(y)\) for all \(y\). Hence \(c_w=c_{\operatorname{red}(w)}\).

**Proof.** (1) The backward orbit of \(y+1\) is the backward orbit of \(y\) shifted by \(1\), and the functions \(\chi_s\) have the period \(1\).

(2) Let the two letters be \(s_i=s\) and \(s_{i+1}=s^{-1}\). Their terms are \(\chi_s(y_{i-1})\) and \(\chi_{s^{-1}}(y_i)\) with \(y_i=h_s^{-1}(y_{i-1})\); by Lemma 3.1 their sum is \(0\). And \(y_{i+1}=h_{s^{-1}}^{-1}(y_i)=h_s(y_i)=y_{i-1}\), so the backward orbit continues after the two letters as if they were not there. \(\blacksquare\)

**Lemma 3.3** (two levels; [OpenAI-M]). Let \(w\) be a word whose reduced form has the length \(\ell>0\), with \(n_+\) positive and \(n_-\) negative letters. Then for every integer \(j\),
\[
c_w(j)=-n_-,\qquad c_w\bigl(h_w(0)+j\bigr)=n_+ .
\]

**Proof.** By Lemma 3.2 and \(h_w=h_{\operatorname{red}(w)}\) we may assume that \(w=s_1\cdots s_\ell\) is reduced. By the periodicity let \(j=0\).

*The first level.* We show that \(y_{i-1}\notin\mathcal A_{s_i}\) for the backward orbit of \(0\), for all \(i\). For \(i=1\): \(0\) lies in no arc. If \(y_{i-1}\notin\mathcal A_{s_i}\), then \(y_i=h_{s_i}^{-1}(y_{i-1})\in\mathcal A_{s_i^{-1}}\) by property 2 of Lemma 2.1. Since \(w\) is reduced, \(s_{i+1}\ne s_i^{-1}\), and the arcs of different letters are disjoint: \(y_i\notin\mathcal A_{s_{i+1}}\). So every indicator in \(c_w(0)\) is \(0\), and \(c_w(0)\) is minus the number of the negative letters.

*The second level.* The backward orbit of \(h_w(0)\) is \(y_{i-1}=h_{s_i\cdots s_\ell}(0)\). By Lemma 2.2, applied to the reduced word \(s_i\cdots s_\ell\), this point lies in \(\mathcal A_{s_i}\). So every indicator is \(1\), and \(c_w(h_w(0))=\ell-n_-=n_+\). \(\blacksquare\)

Let \(z\in(0,1)\) be the fractional part of \(h_w(0)\). The lemma says: on the points
\[
j<z+j<j+1<z+j+1,
\]
continued in both directions over all integers \(j\), the function \(c_w\) takes alternately the values \(-n_-\) and \(n_+\), which differ by \(n_++n_-=\ell\). The function \(c_w\) is a finite sum of indicator functions of intervals with signs; the lemma shows that the cancellations inside it leave an oscillation of the size \(\ell\) on every unit interval.

## 4. Exercises

**4.1.** Find the reduced forms of \(u\,v\,v^{-1}u^{-1}u\) and of \(u\,u^{-1}v\,u\,u^{-1}v^{-1}\).

**4.2.** Find the distribution of \(\ell\) for \(n=2\) and check Lemma 1.1.

**4.3.** Let the arcs be \([0.1,0.2)\) for \(u\), \([0.3,0.4)\) for \(v\), \([0.5,0.6)\) for \(u^{-1}\) and \([0.7,0.8)\) for \(v^{-1}\), repeated with the period \(1\). Compute \(h_u(0)\) and \(h_{u^{-1}}(0)\), and check Lemma 2.2 and Lemma 3.3 for the words \(u\) and \(u^{-1}\).

**4.4.** Show that \(h_w\) is not the identity for a reduced word \(w\) that is not empty. (So the maps \(h_u\) and \(h_v\) generate a free group of homeomorphisms.)

**4.5.** Let \(w=u\,v\). Describe the backward orbits of \(0\) and of \(h_w(0)\), and the terms of \(c_w\) at these two points.

## 5. Solutions

**4.1.** Reading from the left: \(u\), \(uv\), \(u\), empty, \(u\): the reduced form is \(u\). For the second word: \(u\), empty, \(v\), \(vu\), \(v\), empty: the reduced form is the empty word.

**4.2.** The second letter is the inverse of the first with the probability \(\tfrac14\). So \(\ell=0\) with the probability \(\tfrac14\) and \(\ell=2\) with the probability \(\tfrac34\). The mean is \(\tfrac32\ge1\), and \(\Pr(\ell\ge\tfrac12)=\tfrac34\).

**4.3.** For \(s=u\): \(\alpha'=0.5\), \(\beta'=0.6\). On \([0.6,1.5]\) the map \(h_u\) is affine from \(0.1\) to \(0.2\). So \(h_u(1)=0.1+\tfrac{0.4}{0.9}\cdot0.1=\tfrac{13}{90}\) and \(h_u(0)=\tfrac{13}{90}-1\). Its fractional part \(\tfrac{13}{90}\approx0.144\) lies in \((0.1,0.2)\). For \(u^{-1}\): \(h_u\) maps \([0.5,0.6]\) onto \([-0.8,0.1]\) with the slope \(9\), so \(h_{u^{-1}}(0)=0.5+\tfrac{0.8}9=\tfrac{53}{90}\approx0.589\), in \((0.5,0.6)\). Lemma 3.3 for \(w=u\): \(c_u(0)=\chi_u(0)=0=-n_-\), and \(c_u(h_u(0))=1=n_+\). For \(w=u^{-1}\): \(c_w(0)=0-1=-1=-n_-\), and \(c_w(h_w(0))=1-1=0=n_+\).

**4.4.** By Lemma 2.2, \(h_w(0)\) is not an integer, so \(h_w(0)\ne0\).

**4.5.** The backward orbit of \(0\): \(y_0=0\), \(y_1=h_u^{-1}(0)\), which lies in the arc of \(u^{-1}\), and \(y_2=h_v^{-1}(y_1)\), in the arc of \(v^{-1}\). The terms are \(\chi_u(0)=0\) and \(\chi_v(y_1)=0\): \(c_w(0)=0\). The backward orbit of \(h_w(0)=h_u(h_v(0))\): \(y_0\) in the arc of \(u\), \(y_1=h_v(0)\) in the arc of \(v\), \(y_2=0\). The terms are \(1\) and \(1\): \(c_w(h_w(0))=2\).

## References

- [OpenAI-M] OpenAI, *Nontrivial Markov Type Forces Superreflexivity*, OpenAI Math Release preprint, 23 September 2026, Sections 4 and 5. https://github.com/openai/math/tree/main/preprints/Nontrivial-Markov-Type-Forces-Superreflexivity-September-23-2026
