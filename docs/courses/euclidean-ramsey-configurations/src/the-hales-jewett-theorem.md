# The Hales–Jewett theorem

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The sufficiency proof of the classification in this course colours words and looks for a monochromatic *combinatorial line*. The existence of such a line, for every number of colours, is the theorem of Hales and Jewett [HJ]. This lesson proves it by the colour-focusing argument; Shelah later found a proof with primitive recursive bounds [Shelah]. Only the existence of the length is used in [The path criterion](the-path-criterion.md).

## 1. Words and lines

Let \(k\ge1\) and \([k]=\{1,\dots,k\}\), the *alphabet*. A *word* of length \(n\) is an element of \([k]^n\). A *variable word* is an element \(v\) of \(([k]\cup\{*\})^n\) in which the symbol \(*\) occurs at least once; the positions of \(*\) are its *variable positions*. For \(a\in[k]\), \(v(a)\in[k]^n\) is obtained by replacing every \(*\) by \(a\). The *combinatorial line* of \(v\) is the set \(\{v(1),\dots,v(k)\}\) of \(k\) distinct words. All its words agree outside the variable positions, and inside them each word is constant.

An \(r\)-*colouring* of a set is a map to \(\{1,\dots,r\}\). A set is *monochromatic* if the colouring is constant on it.

**Theorem 1.1** (Hales–Jewett). For all integers \(k,r\ge1\) there is an integer \(n\ge1\) such that every \(r\)-colouring of \([k]^n\) has a monochromatic combinatorial line.

Let \(\mathrm{HJ}(k,r)\) denote the least such \(n\). If every \(r\)-colouring of \([k]^n\) has a monochromatic line, so does every \(r\)-colouring of \([k]^{n'}\) for \(n'\ge n\): colour \([k]^n\) by the colour of the word extended by a fixed tail, and append the tail to the line. So the property holds for all lengths from \(\mathrm{HJ}(k,r)\) on.

## 2. Focused lines

Fix \(k\ge2\) and \(r\). Lines \(L_1,\dots,L_t\) in \([k]^n\), with variable words \(v_1,\dots,v_t\), are *focused* at the word \(f\) if \(v_j(k)=f\) for every \(j\). Under a colouring \(c\), they are *colour focused* if, moreover, for every \(j\) the \(k-1\) words \(v_j(1),\dots,v_j(k-1)\) have one colour \(c_j\), and the colours \(c_1,\dots,c_t\) are distinct.

If there are \(r\) colour focused lines, then the colours \(c_1,\dots,c_r\) are all the colours, so the focus \(f\) has some colour \(c_j\), and the line \(L_j\) is monochromatic. The proof of the theorem produces either a monochromatic line or \(r\) colour focused lines.

## 3. Proof of Theorem 1.1

Induction on \(k\). For \(k=1\), \([1]^1\) is a single word, which is a monochromatic line, so \(\mathrm{HJ}(1,r)=1\).

Let \(k\ge2\) and assume that \(\mathrm{HJ}(k-1,r')\) exists for every \(r'\). Fix \(r\). We prove by induction on \(t=1,\dots,r\):

**Claim.** There is \(n_t\) such that every \(r\)-colouring of \([k]^{n_t}\) has a monochromatic line or \(t\) colour focused lines.

*The case \(t=1\).* Put \(n_1=\mathrm{HJ}(k-1,r)\). Restrict a colouring of \([k]^{n_1}\) to \([k-1]^{n_1}\). There is a monochromatic line of \([k-1]^{n_1}\), with variable word \(v\) over the alphabet \([k-1]\). Read as a variable word over \([k]\), \(v\) has \(v(1),\dots,v(k-1)\) of one colour: one colour focused line, with focus \(v(k)\).

*From \(t\) to \(t+1\), for \(t<r\).* Put \(m=n_t\), \(N=r^{k^m}\), \(p=\mathrm{HJ}(k-1,N)\) and \(n_{t+1}=p+m\). Let \(c\) be an \(r\)-colouring of \([k]^{p+m}\), and write words as pairs \((x,y)\) with \(x\in[k]^p\) and \(y\in[k]^m\).

Colour \(x\in[k-1]^p\) by the function \(y\mapsto c(x,y)\) on \([k]^m\); there are \(N\) such functions. By the choice of \(p\), there is a variable word \(u\) over \([k-1]\) of length \(p\) whose line is monochromatic for this colouring:
\[
\begin{gathered}
c(u(a),y)=c(u(1),y)\\
(a\le k-1,\ y\in[k]^m).
\end{gathered}
\]
Colour \([k]^m\) by \(y\mapsto c(u(1),y)\). By the choice of \(m=n_t\), there is a monochromatic line for this colouring, or \(t\) colour focused lines.

If a line \(L\) of \([k]^m\) is monochromatic for \(y\mapsto c(u(1),y)\), then the words \((u(1),y)\), \(y\in L\), form a line of \([k]^{p+m}\) (its variable positions are those of \(L\), shifted by \(p\)), and it is monochromatic for \(c\).

Otherwise let \(v_1,\dots,v_t\) be variable words of colour focused lines in \([k]^m\), with focus \(f\) and distinct colours \(c_1,\dots,c_t\). Consider in \([k]^{p+m}\) the \(t+1\) variable words
\[
(u,v_1),\ \dots,\ (u,v_t),\ (u,f),
\]
where in \((u,v_j)\) the variable positions of \(u\) and of \(v_j\) carry the same variable. Their \(k\)th words are \((u(k),v_j(k))=(u(k),f)\) and \((u(k),f)\): the lines are focused at \((u(k),f)\). For \(a\le k-1\),
\[
\begin{aligned}
c(u(a),v_j(a))&=c(u(1),v_j(a))=c_j,\\
c(u(a),f)&=c(u(1),f).
\end{aligned}
\]
So the first \(t\) lines have their first \(k-1\) words in the colours \(c_1,\dots,c_t\), and the last one in the colour \(c_{t+1}=c(u(1),f)\). If \(c_{t+1}=c_j\) for some \(j\le t\), then the line of \(v_j\) in \([k]^m\) is monochromatic for \(y\mapsto c(u(1),y)\), since its focus \(v_j(k)=f\) has colour \(c(u(1),f)=c_j\), and the previous paragraph gives a monochromatic line. Otherwise the \(t+1\) lines are colour focused. This proves the claim.

*Conclusion.* With \(t=r\), a colouring of \([k]^{n_r}\) has a monochromatic line or \(r\) colour focused lines, and by Section 2 the latter also give a monochromatic line. So \(\mathrm{HJ}(k,r)\le n_r\). \(\square\)

## 4. Exercises

**4.1** (easy). Show that \(\mathrm{HJ}(2,1)=1\) and \(\mathrm{HJ}(k,1)=1\) for every \(k\).

**4.2** (medium). Show that \(\mathrm{HJ}(2,r)\le r\): every \(r\)-colouring of \([2]^r\) has a monochromatic line. (Look at the \(r+1\) words \(1\cdots1\), \(21\cdots1\), \(221\cdots1\), \(\dots\), \(2\cdots2\).)

**4.3** (medium). Deduce van der Waerden's theorem from Theorem 1.1: for all \(k,r\) there is \(N\) such that every \(r\)-colouring of \(\{1,\dots,N\}\) has a monochromatic arithmetic progression of length \(k\). (Send a word \(x\in[k]^n\) to \(\sum_jx_j\).)

**4.4** (easy). In the step from \(t\) to \(t+1\), why must the colouring of \([k-1]^p\) record the whole function \(y\mapsto c(x,y)\), and not just one colour?

## 5. Solutions

**4.1.** With one colour every line is monochromatic, and \([k]^1\) contains the line of the variable word \(*\).

**4.2.** Among the \(r+1\) listed words, two have the same colour, say the words with \(i\) and \(j\) leading \(2\)s, \(i<j\). The variable word with \(2\) in the first \(i\) positions, \(*\) in positions \(i+1,\dots,j\), and \(1\) afterwards has these two words as its line.

**4.3.** Let \(n=\mathrm{HJ}(k,r)\) and \(N=kn\). Colour \(x\in[k]^n\) by the colour of \(\sum_jx_j\in\{n,\dots,kn\}\). A monochromatic line with \(m\ge1\) variable positions has sums \(s_0+am\), \(a=1,\dots,k\), where \(s_0\) is the sum over the fixed positions: an arithmetic progression of length \(k\) and difference \(m\), all of one colour.

**4.4.** The words \((u(a),y)\) for different \(a\le k-1\) must have the same colour for every \(y\) simultaneously, because the later lines \((u,v_j)\) pair \(u(a)\) with \(v_j(a)\), which depends on \(a\). A single colour of \(x\) would not control the colours of \((x,y)\) for the various \(y\).

## References

- [HJ] A. W. Hales and R. I. Jewett, *Regularity and positional games*, Transactions of the American Mathematical Society 106 (1963), 222–229. https://doi.org/10.1090/S0002-9947-1963-0143712-1
- [Shelah] S. Shelah, *Primitive recursive bounds for van der Waerden numbers*, Journal of the American Mathematical Society 1 (1988), 683–697. https://doi.org/10.1090/S0894-0347-1988-0929498-X
