# Factoring with verifiable auxiliary data

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The order trial of [An order trial with prescribed probability](an-order-trial-with-prescribed-probability.md) returns the order \(r\) of a unit with the explicit probability \(\varphi(r)\,2^{-\lceil\log_2r\rceil-10}\), but this number depends on \(r\), which is not known when the trial runs. This lesson builds a factoring process from order trials whose completed runs also produce the prime factorizations of \(p-1\) for the primes \(p\) that occur, recursively. From these auxiliary data, which the run produces itself, one computes after the run the exact probability that each of its steps had a useful outcome [OpenAI-EQF, Section 4]. Splitting a number with the order of a unit is the reduction of factoring to order finding that Shor used [Shor 1997, Section 5], going back to Miller [Miller 1976]; the counting that makes it work is proved here. Recursive factorizations of \(p-1\) also occur in Pratt's primality certificates, but here primality is checked by the test of [A deterministic primality test](a-deterministic-primality-test.md), and the factorizations serve to compute orders and probabilities.

- Units, orders and Euler's function (Section 1).
- Two-adic levels and splitting (Section 2).
- The occurrence tree (Section 3).
- The process (Section 4).
- Probabilities of good outputs (Section 5).
- Completion, size and verification (Section 6).

We use from the core course [Abstract Algebra I](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C30) (Judson, *Abstract Algebra: Theory and Applications*) that the units modulo \(m\) form a group of order \(\varphi(m)\), the number of \(0\le a<m\) with \(\gcd(a,m)=1\) ([Theorem 6.3.1](https://judsonbooks.org/aata-files/aata-html/cosets-section-fermat-euler.html)); that the order of an element of a finite group divides the order of the group ([Corollary 6.2.3](https://judsonbooks.org/aata-files/aata-html/cosets-section-lagranges-theorem.html)); and that the order of an element of a direct product is the least common multiple of the orders of its components ([Corollary 9.2.6](https://judsonbooks.org/aata-files/aata-html/isomorph-section-direct-products.html)). From the core course [Abstract Algebra II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C40) we use the Chinese remainder theorem ([Theorem 16.5.3](https://judsonbooks.org/aata-files/aata-html/rings-section-software-application.html)) and that the multiplicative group of a finite field is cyclic ([Corollary 22.1.11](https://judsonbooks.org/aata-files/aata-html/finite-section-field.html)). The order \(\operatorname{ord}_m(a)\) of a unit \(a\) modulo \(m\) is the least \(r\ge1\) with \(a^r\equiv1\pmod m\); then \(a^k\equiv1\) exactly when \(r\mid k\). We write \(p^e\parallel m\) when \(p\) is a prime, \(e\ge1\), \(p^e\mid m\) and \(p^{e+1}\nmid m\).

## 1. Units, orders and Euler's function

For \(m\ge2\), the Chinese remainder theorem identifies the residues modulo \(m\) with the families of residues modulo the prime powers \(p^e\parallel m\), compatibly with addition and multiplication. A residue is a unit exactly when all its components are units. So the units modulo \(m\) form the direct product of the groups of units modulo the \(p^e\parallel m\), and
\[
\begin{aligned}&\operatorname{ord}_m(a)\\&\quad=\operatorname{lcm}_{p^e\parallel m}\operatorname{ord}_{p^e}(a).\end{aligned}\tag{1.1}
\]

**Lemma 1.1.** \(\varphi(m)=\prod_{p^e\parallel m}(p-1)p^{e-1}\).

*Proof.* Modulo \(p^e\) the nonunits are the \(p^{e-1}\) multiples of \(p\), so there are \(p^e-p^{e-1}=(p-1)p^{e-1}\) units. The units modulo \(m\) correspond to the families of units of the components. \(\square\)

**Lemma 1.2** (orders from factorizations). Let \(2\le m<2^n\) and let \(a\) be a unit modulo \(m\). Given the prime factorization of \(\varphi(m)\), the order \(\operatorname{ord}_m(a)\) and its prime factorization are computed in time polynomial in \(n\).

*Proof.* Start with \(v=\varphi(m)\). For each prime \(q\) of the factorization in turn, replace \(v\) by \(v/q\) as long as \(q\mid v\) and \(a^{v/q}\equiv1\pmod m\). Write \(r=\operatorname{ord}_m(a)\). At the start \(r\mid v\), because \(r\) divides the order \(\varphi(m)\) of the group of units, and every replacement keeps \(r\mid v\). When the work on a prime \(q\) ends, either \(q\nmid v\) or \(r\nmid v/q\), and both statements remain true when \(v\) is later divided by other primes, since \(v/q\) is then replaced by a divisor. So at the end \(r\nmid v/q\) for every prime \(q\mid v\). If \(r\ne v\), a prime \(q\) dividing \(v/r\) would give \(r\mid v/q\); hence \(v=r\), with the factorization given by the remaining exponents. The factorization of \(\varphi(m)\) has fewer than \(n\) prime factors with multiplicity, so there are fewer than \(2n\) modular powerings. \(\square\)

**Lemma 1.3.** \(\varphi(d)/d\ge1/(n+1)\) for \(1\le d<2^n\).

*Proof.* Let \(p_1<\cdots<p_k\) be the distinct primes dividing \(d\). Then \(2^k\le d<2^n\), so \(k<n\), and \(p_i\ge i+1\). By Lemma 1.1,
\[
\begin{aligned}\frac{\varphi(d)}d&=\prod_{i=1}^k\Bigl(1-\frac1{p_i}\Bigr)\\&\ge\prod_{i=1}^k\frac i{i+1}=\frac1{k+1}\ge\frac1{n+1},\end{aligned}
\]
the empty product covering \(d=1\). \(\square\)

## 2. Two-adic levels and splitting

For an integer \(x\ge1\) let \(\nu_2(x)\) be the exponent of \(2\) in \(x\). For a unit \(a\) modulo \(m\) and \(p^e\parallel m\), the number \(\nu_2(\operatorname{ord}_{p^e}(a))\) is the *level* of \(a\) at \(p^e\).

**Lemma 2.1** (levels modulo an odd prime power). Let \(p\) be an odd prime, \(e\ge1\), and \(p-1=h2^\ell\) with \(h\) odd, so \(\ell\ge1\). The number of units modulo \(p^e\) of level \(t\) is
\[
c(t)=\begin{cases}p^{e-1}h,&t=0,\\ p^{e-1}2^{t-1}h,&1\le t\le\ell,\\ 0,&t>\ell .\end{cases}
\]
In particular \(c(t)\le\frac12(p-1)p^{e-1}\) for every \(t\).

*Proof.* *Modulo \(p\).* The units modulo \(p\) form the multiplicative group of the field \(\mathbb F_p\), a cyclic group of order \(p-1\). In a cyclic group of order \(M\) with generator \(\gamma\), for each divisor \(D\) of \(M\) exactly \(D\) elements \(x\) satisfy \(x^D=1\): for \(x=\gamma^k\) with \(0\le k<M\), \(x^D=1\) means \(M\mid kD\), that is, \(M/D\) divides \(k\). The order of a unit modulo \(p\) divides \(h2^\ell\), so its level is at most \(t\le\ell\) exactly when its order divides \(h2^t\). Hence \(h2^t\) units have level at most \(t\), and the counts are \(h\) for \(t=0\) and \(h2^t-h2^{t-1}=h2^{t-1}\) for \(1\le t\le\ell\).

*Modulo \(p^e\).* Reduction modulo \(p\) is a homomorphism from the units modulo \(p^e\) onto the units modulo \(p\); each unit \(x\) modulo \(p\) has the \(p^{e-1}\) preimages \(x+jp\), \(0\le j<p^{e-1}\), so the kernel has \(p^{e-1}\) elements. Let \(a\) be a unit modulo \(p^e\) whose reduction has order \(o\). Then \(a^o\) lies in the kernel, so \(a^{op^{e-1}}=1\); and \(a^k=1\) implies that the reduction satisfies the same, so \(o\mid\operatorname{ord}(a)\). Hence \(\operatorname{ord}(a)/o\) divides \(p^{e-1}\), and as \(p\) is odd, \(a\) and its reduction have the same level. So each count modulo \(p^e\) is \(p^{e-1}\) times the count modulo \(p\). The largest count is \(p^{e-1}2^{\ell-1}h=\frac12(p-1)p^{e-1}\), since \(\ell\ge1\). \(\square\)

**Lemma 2.2** (unequal levels are frequent). Let \(m\) be odd with \(k\ge2\) distinct prime factors, \(p_i^{e_i}\parallel m\), and let \(c_i(t)\) be the counts of Lemma 2.1 for \(p_i^{e_i}\). The number of units modulo \(m\) whose levels at the \(p_i^{e_i}\) are not all equal is
\[
F(m)=\varphi(m)-\sum_{t\ge0}\prod_{i=1}^kc_i(t)\ \ge\ \frac{\varphi(m)}2 .
\]

*Proof.* By the Chinese remainder theorem the units with all levels equal to \(t\) correspond to the families of units of level \(t\) of the components, and there are \(\prod_ic_i(t)\) of them. For the bound put \(q_i(t)=c_i(t)/\bigl((p_i-1)p_i^{e_i-1}\bigr)\), so that \(\sum_tq_i(t)=1\) and \(q_i(t)\le\frac12\). Then
\[
\begin{aligned}&\frac1{\varphi(m)}\sum_t\prod_ic_i(t)\\&\quad=\sum_t\prod_iq_i(t)\le\sum_tq_1(t)q_2(t)\\&\quad\le\max_tq_1(t)\le\frac12 .\qquad\square\end{aligned}
\]

**Lemma 2.3** (splitting; [Miller 1976]; [Shor 1997, Section 5]). Let \(m\) be odd with at least two distinct prime factors, let \(a\) be a unit modulo \(m\) whose levels are not all equal, and let \(r=\operatorname{ord}_m(a)\). Then \(r\) is even, and for the residue \(y\) of \(a^{r/2}\) in \([0,m)\), \(\gcd(y-1,m)\) is a divisor of \(m\) other than \(1\) and \(m\).

*Proof.* Let \(t^*\) be the largest level of \(a\); it exceeds the smallest one, so \(t^*\ge1\). By (1.1), \(\nu_2(r)=t^*\), and \(r\) is even. Let \(p^e\parallel m\) with \(o=\operatorname{ord}_{p^e}(a)\). If the level of \(a\) at \(p^e\) is less than \(t^*\), then the odd part of \(o\) divides the odd part of \(r\) and \(\nu_2(o)\le t^*-1=\nu_2(r/2)\), so \(o\mid r/2\) and \(y\equiv1\pmod{p^e}\). If the level is \(t^*\), then \(o\nmid r/2\), so \(y\not\equiv1\pmod{p^e}\), while \(y^2\equiv a^r\equiv1\). As \(p^e\) divides \((y-1)(y+1)\) and \(p\) cannot divide both factors, whose difference is \(2\), \(p^e\) divides one of them; so \(y\equiv-1\pmod{p^e}\), and \(p\nmid y-1\). Hence \(\gcd(y-1,m)\) is the product of the \(p^e\parallel m\) at which the level is less than \(t^*\). Some component has level \(t^*\) and some has a smaller level, so this product is neither \(m\) nor \(1\). \(\square\)

## 3. The occurrence tree

For \(M\ge2\), the *occurrence tree* \(\mathcal D(M)\) is the following rooted tree [OpenAI-EQF, Section 4]. Its root records \(M\), the distinct primes dividing \(M\) in increasing order, and their exponents. For each odd prime \(p\mid M\) the root has one child, which is the root of a copy of \(\mathcal D(p-1)\); the children are ordered by \(p\), and the prime \(2\) has no child. Equal labels under different parents are separate occurrences. Since \(p-1<M\), the labels decrease along every descent, so \(\mathcal D(M)\) is a well-defined finite tree.

For example, \(21=3\cdot7\), so the root of \(\mathcal D(21)\) has the children \(\mathcal D(2)\) and \(\mathcal D(6)\), for the primes \(3\) and \(7\). The node \(6=2\cdot3\) has the child \(\mathcal D(2)\), for the prime \(3\), and the nodes labelled \(2\) have no children. The two nodes labelled \(2\) are different occurrences.

**Lemma 3.1** (size of the tree). Let \(2\le N<2^n\). In \(\mathcal D(N)\), the sum of \(\log_2M\) over the node labels \(M\) at any fixed depth is at most \(\log_2N<n\), there are at most \(2n-2\) depths, and there are fewer than \(2n^2\) nodes.

*Proof.* The children of a node \(M\) have the labels \(p-1\) for the distinct odd primes \(p\mid M\), and \(\sum_p\log_2(p-1)\le\sum_{p\mid M}\log_2p\le\log_2M\), since the product of the distinct primes dividing \(M\) divides \(M\). Induction on the depth gives the first claim. In two successive descents \(M\to p-1\to q-1\), the odd prime \(q\) divides the even number \(p-1\), so \(q-1<q\le(p-1)/2<M/2\). So a node at depth \(d\) has a label \(M\le N/2^{\lfloor d/2\rfloor}<2^{n-\lfloor d/2\rfloor}\), and \(M\ge2\) forces \(\lfloor d/2\rfloor\le n-2\), that is, \(d\le2n-3\). Every label is at least \(2\), so it contributes at least \(1\) to the sum at its depth, and each depth has fewer than \(n\) nodes. \(\square\)

## 4. The process

Fix an integer \(N\ge2\), let \(n=\max\{128,\lfloor\log_2N\rfloor+1\}\), and put
\[
\begin{gathered}B=2^n,\quad K=n^5,\\ L=n^{10},\\ W=n(K+1),\end{gathered}\tag{4.1}
\]
so that \(N<B\). The process consists of a deterministic classical *controller* that requests *transitions*. A transition receives a classical input and returns a string of \(W\) bits, its *output*. It works on fresh qubits with fresh coins, its output is copied into the record of the run before the controller reads it, and its other registers are kept, unused, until the end. There are three kinds of transitions.

- A *list transition* has an input \((M,m)\), where \(m\) is odd with at least two distinct prime factors. With \(b_m=\lceil\log_2m\rceil\), it draws \(K\) independent uniform integers in \([0,2^{b_m})\), its *entries*, and outputs them as \(K\) fields of \(b_m\) bits followed by zeros. An entry is *usable* if it lies in \([0,m)\) and is a unit modulo \(m\).
- An *order transition* has an input \((M,m,a)\), where \(a\) is a usable entry. It runs \(K\) order trials of Proposition 3.1 of [An order trial with prescribed probability](an-order-trial-with-prescribed-probability.md) for the modulus \(m\) and the unit \(a\), with the present \(n\), one after another on fresh registers, and outputs the smallest returned candidate, or \(0\) if none was returned, as an \(n\)-bit integer followed by zeros.
- A *dummy transition* outputs \(W\) zeros.

The controller aborts as soon as an output is malformed, that is, has a nonzero bit where the encoding requires a zero. It keeps a queue of nodes to be factored, which starts with the root \(N\), and a record of completed nodes. To factor a node \(M\) it keeps a list of factors with product \(M\), starting with the list \((M)\), and treats the first factor \(m\) that is not yet marked prime:

1. if \(m\) is prime by Theorem 1.1 of [A deterministic primality test](a-deterministic-primality-test.md), it is marked prime;
2. otherwise, if \(m\) is even, it is replaced by \(2\) and \(m/2\);
3. otherwise, if \(m=b^e\) with integers \(b,e\ge2\), found by a binary search for each exponent \(2\le e<n\), it is replaced by \(b\) and \(m/b\);
4. otherwise \(m\) is odd and composite and not a perfect power, so it has at least two distinct prime factors, and the controller makes a *split attempt*. It requests a list transition with input \((M,m)\). Then, for each usable entry \(a\) of the list in turn, it requests an order transition with input \((M,m,a)\), and if its output \(r'\) is positive and even and \(d=\gcd(y-1,m)\), with \(y\) the residue of \(a^{r'/2}\) in \([0,m)\), satisfies \(1<d<m\), it replaces \(m\) by \(d\) and \(m/d\) and ends the attempt. If no usable entry gives such a \(d\), the controller aborts.

When all factors of \(M\) are marked prime, the controller records the node: \(M\), its distinct primes in increasing order, and their exponents. It appends to the queue the nodes \(p-1\) for the odd primes \(p\) of \(M\), in increasing order of \(p\), as the children of this node. When the queue is empty, it requests dummy transitions until it has requested exactly \(L\) transitions in all, and stops with the recorded tree.

**Proposition 4.1** (the factoring process; [OpenAI-EQF, Proposition 4.1]). The process has the following properties.

1. Every run either aborts or requests exactly \(L\) transitions and stops with the tree \(\mathcal D(N)\). A deterministic algorithm, the *verifier*, decides in time polynomial in \(n\), for every given record, whether it equals \(\mathcal D(N)\).
2. For every transition requested in a run, the following are computed from \(\mathcal D(N)\) and the input of the transition in time polynomial in \(n\): a set of *good* \(W\)-bit strings, given by a polynomial-time test; one good string, the *canonical output*; and the probability \(s\) that the transition, run as specified, returns a good output. The number \(s\) is a dyadic rational of polynomial bit length with
\[
s\ge1-2^{-2n}.
\]
For a dummy transition, the good and canonical output is the zero string, and \(s=1\).
3. Let \(y_1,y_2,\ldots\) be \(W\)-bit strings such that each \(y_i\) is good for the input that the controller computes from \(N\) and \(y_1,\ldots,y_{i-1}\). If the controller reads them as the outputs of its transitions, it does not abort and stops with \(\mathcal D(N)\). For every sequence of \(W\)-bit strings, the work and the storage of the controller are bounded by a fixed polynomial in \(n\).

The output of a transition is only the \(W\)-bit string. The internal registers of the order trials and the record of the run are separate, and in [Certain output from deferred filters](certain-output-from-deferred-filters.md) they are all kept, so that the whole computation can be inverted.

## 5. Probabilities of good outputs

*Reading the data.* Let a transition have the input \((M,m)\) or \((M,m,a)\), as requested in some run. Every node that the controller factors is a node of \(\mathcal D(N)\), and \(m\) divides \(M\) (Lemma 6.1 below). So \(\mathcal D(N)\) contains the prime factorization of \(M\), from which the factorization of \(m\) follows by division, and for each odd prime \(p\mid m\), a child of a node labelled \(M\) contains the factorization of \(p-1\). By Lemma 1.1 this gives the factorization of \(\varphi(p^e)=(p-1)p^{e-1}\) for each \(p^e\parallel m\), and of \(\varphi(m)\). By Lemma 1.2 one computes the orders \(\operatorname{ord}_{p^e}(a)\), their levels, the order \(\operatorname{ord}_m(a)\) and its factorization, and by Lemma 2.1 the counts \(c_i(t)\) and the number \(F(m)\) of Lemma 2.2; there are fewer than \(n\) components and at most \(n\) levels.

*List transitions.* For the input \((M,m)\), a string is *good* if it is well formed and some usable entry has levels that are not all equal. The *canonical output* has the first entry \(c\in[0,m)\) with \(c\equiv1\) modulo \(p_1^{e_1}\), for the smallest prime \(p_1\) of \(m\), and \(c\equiv-1\) modulo the other \(p_i^{e_i}\parallel m\), and all other bits zero. It is good: \(c\) is a unit, of order \(1\) modulo \(p_1^{e_1}\) and of order \(2\) modulo the other components, as \(-1\not\equiv1\) modulo an odd prime power; so its levels are \(0\) and \(1\). An entry is uniform in \([0,2^{b_m})\), so it is usable with unequal levels with probability \(x=F(m)/2^{b_m}\), and the entries are independent:
\[
\begin{gathered}s=1-(1-x)^K,\\ x=\frac{F(m)}{2^{b_m}}\ge\frac1{4(n+1)},\end{gathered}\tag{5.1}
\]
since \(x\ge\frac{\varphi(m)/2}{2m}\) by Lemma 2.2 and \(2^{b_m}<2m\), and \(\varphi(m)/m\ge1/(n+1)\) by Lemma 1.3.

*Order transitions.* For the input \((M,m,a)\) let \(r=\operatorname{ord}_m(a)\). A string is *good* if it is well formed and its integer equals \(r\), and this string is the canonical output. By Proposition 3.1 of [An order trial with prescribed probability](an-order-trial-with-prescribed-probability.md), every candidate returned by a trial is a positive multiple of \(r\), and a trial returns \(r\) with probability \(\varphi(r)\lambda(r)\), where \(\lambda(r)=2^{-\lceil\log_2r\rceil-10}\). Each trial works on fresh registers, so by Lemma 3.3 of [Exact circuits and dyadic probabilities](exact-circuits-and-dyadic-probabilities.md) this holds for each trial whatever the earlier trials returned. The smallest candidate equals \(r\) exactly when some trial returns \(r\), so
\[
\begin{gathered}s=1-(1-x)^K,\\ x=\varphi(r)\lambda(r),\\ x\ge\frac1{2048(n+1)},\end{gathered}\tag{5.2}
\]
since \(x\ge\varphi(r)/(2^{11}r)\) by \(2^{\lceil\log_2r\rceil}<2r\), also for \(r=1\), and \(\varphi(r)/r\ge1/(n+1)\) by \(r\le\varphi(m)<B\) and Lemma 1.3.

*Dummy transitions.* The zero string is good and canonical, and \(s=1\).

**Lemma 5.1.** For every transition requested in a run, \(s\) is a dyadic rational with a denominator dividing \(2^{(n+10)K}\), computed from \(\mathcal D(N)\) and the input in time polynomial in \(n\), and \(s\ge1-2^{-2n}\).

*Proof.* In (5.1) the base \(1-x\) has the denominator \(2^{b_m}\) with \(b_m\le n\), and in (5.2) the denominator \(2^{\lceil\log_2r\rceil+10}\le2^{n+10}\). Its \(K\)-th power is computed exactly by integer powering, from the data read above. In both cases \(x\ge1/(2048(n+1))\), so for \(n\ge128\)
\[
Kx\ge\frac{n^5}{2048(n+1)}\ge\frac{n^4}{4096}\ge2n ,
\]
and \((1-x)^K\le e^{-Kx}\le e^{-2n}<2^{-2n}\). \(\square\)

## 6. Completion, size and verification

**Lemma 6.1** (records are correct). In every run, for any outputs of the transitions, every factor in the list of a node \(M\) is a divisor of \(M\) at least \(2\), the product of the list is \(M\), every factor marked prime is prime, and every node recorded or queued is a node of \(\mathcal D(N)\), its recorded primes and exponents being those of \(\mathcal D(N)\).

*Proof.* The replacements in cases 2, 3 and 4 put two divisors at least \(2\) in place of a factor equal to their product: in case 4 because \(1<d<m\) is checked. Primality is decided by the test. When all factors of \(M\) are prime, the list is a prime factorization of \(M\), which by unique factorization gives the primes and exponents of \(M\); so the queued children are the labels \(p-1\) of \(\mathcal D(N)\). Induction over the nodes in the order of the queue gives the claim. \(\square\)

**Lemma 6.2** (good outputs complete the run). Let the outputs \(y_1,y_2,\ldots\) be as in Proposition 4.1(3). Then no split attempt aborts, and the controller stops with \(\mathcal D(N)\).

*Proof.* Consider a split attempt on a factor \(m\) of a node \(M\). The list output is good, so it has a usable entry \(a\) whose levels are not all equal. If no earlier entry ends the attempt, the controller requests the order transition for \(a\), whose good output is \(r=\operatorname{ord}_m(a)\). By Lemma 2.3, \(r\) is even and \(\gcd(y-1,m)\) is a proper divisor of \(m\), so the attempt ends with a split. Good outputs are well formed, so the controller never aborts. By Lemma 6.3 below it finishes the queue within its bounds, and by Lemma 6.1 the recorded tree is \(\mathcal D(N)\): every node of \(\mathcal D(N)\) is queued, because the children of each recorded node are queued. \(\square\)

**Lemma 6.3** (size bounds). For every sequence of outputs, the controller requests fewer than \(2n^2(K+1)\le4n^7<L\) list and order transitions, and its work and storage are bounded by a fixed polynomial in \(n\).

*Proof.* By Lemma 6.1 the factored nodes are nodes of \(\mathcal D(N)\). For a node \(M\), the number of factors in its list is at most \(\log_2M\), as their product is \(M\) and each is at least \(2\). Every replacement increases this number by one, so there are fewer than \(\log_2M\) replacements, and at most one split attempt fails, after which the controller aborts. So there are at most \(\log_2M\) split attempts on \(M\), each with one list transition and at most \(K\) order transitions. By Lemma 3.1, the sum of \(\log_2M\) over all nodes is less than \((2n-2)n<2n^2\), which gives fewer than \(2n^2(K+1)\) transitions, and \(2n^2(K+1)\le4n^7<n^{10}\). Each step of the controller (a primality test, a binary search for roots, a gcd, a modular powering, reading an output of \(W\) bits) takes time polynomial in \(n\), and there are polynomially many steps. The record holds fewer than \(2n^2\) nodes with at most \(n\) primes each, and the outputs have \(W\) bits. \(\square\)

**Lemma 6.4** (the verifier). There is a deterministic algorithm that decides, for every \(N\ge2\) and every record, in time polynomial in \(n\), whether the record equals \(\mathcal D(N)\).

*Proof.* The verifier rejects a record with more than \(2n^2\) nodes, a node label outside \([2,B)\), more than \(n\) primes at a node, a prime label outside \([2,M]\) at a node \(M\), or an exponent outside \([1,n]\). It requires the root label to be \(N\). At each node \(M\) it requires strictly increasing prime labels, checks each of them with Theorem 1.1 of [A deterministic primality test](a-deterministic-primality-test.md), and checks that the product of the prime powers is \(M\), rejecting as soon as a partial product exceeds \(M\). It requires the children to be exactly the nodes labelled \(p-1\) for the odd primes \(p\) of the node, in increasing order of \(p\), and applies the same checks to them. These bounds make every check polynomial, also on invalid records. If a record is accepted, unique factorization shows that the root carries the primes and exponents of \(N\), and induction on the depth shows that the record is \(\mathcal D(N)\). Conversely \(\mathcal D(N)\) passes every check: its labels are less than \(B\), a node \(M<2^n\) has at most \(n\) prime factors and exponents less than \(n\), and Lemma 3.1 bounds its number of nodes. \(\square\)

*Proof of Proposition 4.1.* (1) If a run does not abort, then by Lemma 6.1 and Lemma 6.3 it records \(\mathcal D(N)\) and requests fewer than \(L\) list and order transitions; the dummy transitions bring the total to exactly \(L\). The verifier is Lemma 6.4. (2) is Section 5 with Lemma 5.1, and (3) is Lemmas 6.2 and 6.3. Every list output has at most \(nK\) bits before its zeros and every order output has \(n\) bits, so all fit into \(W=n(K+1)\) bits, and each canonical output is one string. \(\square\)

## 7. Exercises

**7.1.** Write down \(\mathcal D(91)\) and count its nodes.

**7.2.** For \(m=15\), compute the counts \(c_i(t)\) of Lemma 2.1 for the components \(3\) and \(5\), the number \(F(15)\), and the probability that a uniform unit modulo \(15\) has unequal levels.

**7.3.** Carry out the splitting step of Lemma 2.3 for \(m=15\) and \(a=2\).

**7.4.** Find all \(x\) modulo \(8\) with \(x^2\equiv1\pmod8\). Which step of the proof of Lemma 2.3 uses that \(m\) is odd?

**7.5.** Compute \(\operatorname{ord}_{21}(2)\) by the procedure of Lemma 1.2, starting from \(\varphi(21)=12=2^2\cdot3\).

## 8. Solutions

**7.1.** \(91=7\cdot13\), so the root has the children \(6=2\cdot3\), for \(7\), and \(12=2^2\cdot3\), for \(13\). Each of these has one child \(2\), for the prime \(3\). There are five nodes.

**7.2.** For \(p=3\): \(p-1=2\), \(h=1\), \(\ell=1\), and the counts are \(c_1(0)=1\), \(c_1(1)=1\). For \(p=5\): \(p-1=4\), \(h=1\), \(\ell=2\), and \(c_2(0)=1\), \(c_2(1)=1\), \(c_2(2)=2\). So \(\sum_tc_1(t)c_2(t)=1+1=2\), \(F(15)=\varphi(15)-2=8-2=6\), and the probability is \(6/8=3/4\).

**7.3.** Modulo \(3\), \(2\) has order \(2\), level \(1\); modulo \(5\), \(2\) has order \(4\), level \(2\). So \(r=\operatorname{lcm}(2,4)=4\), \(y=2^2=4\), and \(\gcd(3,15)=3\), a proper divisor. As in the proof, \(y\equiv1\pmod3\), where the level is smaller, and \(y\equiv-1\pmod5\).

**7.4.** \(x\in\{1,3,5,7\}\). The proof uses that \(p\) is odd where it concludes that \(p\) cannot divide both \(y-1\) and \(y+1\); modulo \(8\) both \(3-1\) and \(3+1\) are even.

**7.5.** Start with \(v=12\). For \(q=2\): \(2^6=64\equiv1\pmod{21}\), so \(v=6\); then \(2^3=8\not\equiv1\), so the work on \(2\) ends. For \(q=3\): \(2^2=4\not\equiv1\), so \(v\) stays \(6\). Hence \(\operatorname{ord}_{21}(2)=6\).

## References

- [OpenAI-EQF] OpenAI, *Exact quantum factoring over a fixed finite gate set*, OpenAI Math Release preprint, 25 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/Exact-quantum-factoring-over-a-fixed-finite-gate-set-September-25-2026
- [Shor 1997] P. W. Shor, *Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer*, SIAM J. Comput. 26 (1997), no. 5, 1484–1509. https://arxiv.org/abs/quant-ph/9508027
- [Miller 1976] G. L. Miller, *Riemann's hypothesis and tests for primality*, J. Comput. System Sci. 13 (1976), no. 3, 300–317. https://www.cs.cmu.edu/afs/cs/Web/People/glmiller/Publications/Papers/Mi76.pdf
