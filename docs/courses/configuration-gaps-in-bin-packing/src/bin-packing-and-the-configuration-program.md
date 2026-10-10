# Bin packing and the configuration program

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Bin packing asks for the least number of bins of capacity one that hold a given list of items. Its strongest classical lower bound is the *configuration linear program*: it may cut the bins into fractions of feasible bin contents. Scheithauer and Terno conjectured that the integral optimum never exceeds this bound, rounded up, by more than one. This course proves OpenAI's 2026 theorem that the difference is unbounded. It also proves that packing within any fixed additive number of bins above the optimum is NP-hard, using one imported theorem from the theory of probabilistically checkable proofs.

This lesson sets up the two configuration programs, proves the lower bounds used later, states the results and reduces the first of them to a statement about graphs. It also proves two elementary counting facts about intervals on which the whole construction rests. The second lesson proves a combinatorial lemma about trees; the third and fourth build the bin-packing instance from a graph (coordinates and items, then sizes); the fifth packs it, integrally from a vertex cover and fractionally in one special case; the sixth extracts a vertex cover from any packing that uses few extra bins and draws the consequences.

## 1. Instances, packings and the optimum

**Definition 1.1.** An *instance* is a finite set \(\mathcal I\) of items, each with a rational size \(a_i\in(0,1]\). Different items may have equal sizes; they remain distinct elements of \(\mathcal I\). A *packing into \(N\) bins* is a map \(\beta:\mathcal I\to\{1,\ldots,N\}\) such that
\[
\sum_{i:\,\beta(i)=s}a_i\leq1\qquad(1\leq s\leq N).
\]
The *optimum* \(\mathrm{OPT}(I)\) is the least \(N\) for which a packing into \(N\) bins exists. It is at most \(|\mathcal I|\), since every item fits into a bin of its own.

**Definition 1.2 (configuration programs).** An *individual configuration* is a set \(H\subseteq\mathcal I\) with \(\sum_{i\in H}a_i\leq1\); let \(\mathcal H\) be the set of all of them. Let \(\mathcal S\) be the set of distinct sizes and \(n_\sigma\) the number of items of size \(\sigma\in\mathcal S\). A *type configuration* is a vector \(c=(c_\sigma)_{\sigma\in\mathcal S}\) of nonnegative integers with \(\sum_\sigma\sigma c_\sigma\leq1\); let \(\mathcal C\) be the set of all of them. The *individual configuration program* and the *configuration program* (of Gilmore and Gomory) have the values
\[
\mathrm{LP}_{\mathrm{ind}}(I)=\inf\Bigl\{\sum_{H\in\mathcal H}y_H:\ y\geq0,\ \sum_{H\ni i}y_H\geq1\ (i\in\mathcal I)\Bigr\},
\]
\[
\mathrm{LP}(I)=\inf\Bigl\{\sum_{c\in\mathcal C}z_c:\ z\geq0,\ \sum_{c\in\mathcal C}c_\sigma z_c\geq n_\sigma\ (\sigma\in\mathcal S)\Bigr\}.
\]
Both sets of configurations are finite: \(\mathcal H\) consists of subsets of a finite set, and \(c_\sigma\leq1/\sigma\) in a type configuration. Both programs are feasible (use the configurations with one item), so both values are finite nonnegative numbers.

A type configuration may contain more copies of a size than the instance has; an individual configuration cannot. This makes \(\mathrm{LP}\) the weaker of the two bounds (Exercise 6.1).

**Lemma 1.3.** \(\mathrm{LP}(I)\leq\mathrm{LP}_{\mathrm{ind}}(I)\leq\mathrm{OPT}(I)\).

*Proof.* Let \(\beta\) be a packing into \(N\) bins. The nonempty sets \(\beta^{-1}(s)\) are pairwise disjoint individual configurations that cover every item; giving each of them weight one gives a feasible \(y\) with \(\sum_Hy_H\leq N\). Hence \(\mathrm{LP}_{\mathrm{ind}}\leq\mathrm{OPT}\).

Let \(y\) be feasible for the individual program. The *type* of \(H\in\mathcal H\) is the vector \(\tau(H)\) with \(\tau(H)_\sigma=\#\{i\in H:a_i=\sigma\}\); it is a type configuration, because \(\sum_\sigma\sigma\tau(H)_\sigma=\sum_{i\in H}a_i\leq1\). Put \(z_c=\sum_{H:\tau(H)=c}y_H\). Then \(\sum_cz_c=\sum_Hy_H\), and for every size \(\sigma\)
\[
\sum_cc_\sigma z_c=\sum_H\tau(H)_\sigma y_H=\sum_{i:\,a_i=\sigma}\ \sum_{H\ni i}y_H\geq n_\sigma .
\]
So every value of the individual program is also a value of the type program, and \(\mathrm{LP}\leq\mathrm{LP}_{\mathrm{ind}}\). \(\square\)

**Lemma 1.4 (the counting bound).** Suppose every item size exceeds \(1/6\). Then every individual configuration has at most five items, every type configuration has \(\sum_\sigma c_\sigma\leq5\), and
\[
\mathrm{LP}(I)\geq\frac{|\mathcal I|}5 .
\]
Consequently \(\mathrm{LP}_{\mathrm{ind}}(I)\geq|\mathcal I|/5\) and \(\mathrm{OPT}(I)\geq|\mathcal I|/5\).

*Proof.* Six items of size greater than \(1/6\) have total size greater than one. For feasible \(z\),
\[
\sum_cz_c\geq\sum_c\frac{\sum_\sigma c_\sigma}5\,z_c=\frac15\sum_\sigma\sum_cc_\sigma z_c\geq\frac15\sum_\sigma n_\sigma=\frac{|\mathcal I|}5 .
\]
The rest follows from Lemma 1.3. \(\square\)

The proof gives every item the weight \(1/5\) and observes that no configuration collects more than total weight one; this is the weak duality of linear programming in the case at hand. When an instance with \(|\mathcal I|=5B\) items of sizes above \(1/6\) has a fractional solution of value \(B\), Lemma 1.4 shows that its configuration value is exactly \(B\). This is how the fractional value will be determined.

## 2. Integer round-up

An instance has the *integer round-up property* if \(\mathrm{OPT}(I)=\lceil\mathrm{LP}(I)\rceil\). Marcotte found instances without it in 1985. Scheithauer and Terno then studied the weaker bound
\[
\mathrm{OPT}(I)\leq\lceil\mathrm{LP}(I)\rceil+1,\tag{2.1}
\]
and the statement that (2.1) holds for every instance became known as the *modified integer round-up conjecture*. No instance violating it was known.

Two lines of work are related. Algorithms that solve the configuration program approximately and round it obtain packings with \(\mathrm{OPT}(I)+O(\log^2\mathrm{OPT}(I))\) bins (Karmarkar and Karp, 1982), \(O(\log\mathrm{OPT}\cdot\log\log\mathrm{OPT})\) extra bins (Rothvoss, 2013) and \(O(\log\mathrm{OPT})\) extra bins (Hoberg and Rothvoss, 2017); the last two bounds are measured against \(\mathrm{LP}(I)\), so they also bound the gap \(\mathrm{OPT}-\mathrm{LP}\) logarithmically. Whether a polynomial-time algorithm can always use at most \(\mathrm{OPT}(I)+C\) bins for an absolute constant \(C\) is listed as an open problem in the book of Williamson and Shmoys.

## 3. The results

**Theorem 3.1 (unbounded configuration gap; OpenAI, 2026).** For every integer \(c\geq0\) there are an instance \(I\) and an integer \(B\) such that every item size exceeds \(1/6\) and
\[
\mathrm{LP}(I)=\mathrm{LP}_{\mathrm{ind}}(I)=B,\qquad\mathrm{OPT}(I)>B+c .
\]

With \(c=1\) the instance violates (2.1), since \(\lceil\mathrm{LP}\rceil=B\). The theorem uses no hypothesis from complexity theory. The instances grow very fast with \(c\); the theorem is compatible with the logarithmic upper bounds of Section 2.

**Theorem 3.2 (additive hardness; OpenAI, 2026).** For every fixed integer \(c\geq0\) it is NP-hard to distinguish pairs \((I,B)\) for which \(I\) packs into \(B\) bins from pairs for which \(I\) does not pack into \(B+c\) bins, already for instances whose item sizes all exceed \(1/6\).

**Corollary 3.3.** A deterministic polynomial-time algorithm that packs every instance into at most \(\mathrm{OPT}(I)+C\) bins, for an absolute constant \(C\), exists if and only if \(\mathrm P=\mathrm{NP}\).

Theorem 3.1 is proved completely in this course. Theorem 3.2 and Corollary 3.3 are proved in the sixth lesson from Theorem 4.1 below and one imported theorem of Håstad on satisfiability gaps, which is recorded as an open obligation of the course. The precise meaning of NP-hardness for such distinguishing problems is given there.

## 4. The plan: a reduction from vertex cover

A *vertex cover* of a graph \(G=(V,E)\) is a set of vertices that contains an endpoint of every edge. Write \(\tau(G)\) for the least size of a vertex cover.

**Theorem 4.1 (graph-to-packing reduction; OpenAI, 2026).** Fix an integer \(c\geq0\) and a real \(\rho>0\). There is a deterministic procedure, running in time polynomial in the size of its input, that takes a simple graph \(G\) with vertex set \(\{1,\ldots,n\}\) and at least one edge, and an integer \(0\leq k\leq n\), and returns an integer \(B\) and \(5B\) items with rational sizes in \((1/6,1)\), such that:

(a) if \(\tau(G)\leq k\), the items pack into \(B\) bins;

(b) if the items pack into at most \(B+c\) bins, then \(\tau(G)\leq k+\rho n\).

The constants in the running time may depend on \(c\) and \(\rho\).

The third and fourth lessons construct the instance, the fifth proves (a) and the sixth proves (b). For Theorem 3.1 one more fact is needed, proved in the fifth lesson: for the complete graph \(K_4\) on four vertices and \(k=2\), the configuration programs of the constructed instance have value \(B\), although no vertex cover of size two exists.

*Proof of Theorem 3.1 from these facts.* Fix \(c\geq0\), put \(\rho=1/8\), and apply the construction to \(K_4\) with \(k=2\). The fractional value is \(B\). Every vertex cover of \(K_4\) has at least three vertices, since two vertices miss the edge joining the other two, while \(k+\rho n=2+4/8<3\). So by (b) the items do not pack into \(B+c\) bins, that is, \(\mathrm{OPT}>B+c\). \(\square\)

The construction has many parts, but they serve one mechanism. A bin of the main kind contains a *row* item, which records a point \(b\) on the real line, an *anchor* item, which records a *deadline* \(z\), and two *auxiliary* items whose lengths move the row's point leftwards to a *completion* \(h\leq b\). The sizes are chosen so that the bin fits exactly when \(h\leq z\). Some deadlines are moved from the right end of a short *test interval* to its left end; comparing how many completions and deadlines lie to the left of each point then forces the intervals \([h,b)\) to *cover* every test interval many times. Long auxiliary items are scarce, and two trees of nested intervals make it impossible to cover both sides of a vertex cheaply. The side that a vertex pays for in a packing marks it as chosen or not, and further items attached to the edges force every edge to have a chosen endpoint.

## 5. Two counting identities

The following facts about half-open intervals are used repeatedly. For a statement \(E\) let \(\mathbf 1\{E\}\) be \(1\) if \(E\) holds and \(0\) otherwise.

**Lemma 5.1 (prefix identities).** Let \(a\in\mathbb R\).

(a) If \(h\leq b\), then \(\mathbf 1\{h\leq a\}=\mathbf 1\{b\leq a\}+\mathbf 1\{h\leq a<b\}\).

(b) If \(l<r\), then \(\mathbf 1\{l\leq a\}-\mathbf 1\{r\leq a\}=\mathbf 1\{l\leq a<r\}\).

Consequently, for finitely many pairs \(h_j\leq b_j\),
\[
\#\{j:h_j\leq a\}=\#\{j:b_j\leq a\}+\#\{j:a\in[h_j,b_j)\}.\tag{5.1}
\]

*Proof.* (a) If \(b\leq a\), then \(h\leq a\) and \(a\not<b\), so both sides are \(1\). If \(a<b\), the right side is \(\mathbf 1\{h\leq a\}\). (b) is (a) with \(h=l\), \(b=r\). Summing (a) over \(j\) gives (5.1). \(\square\)

In words: moving a point from \(r\) to \(l<r\) raises the number of points at or left of \(a\) by one exactly for \(a\in[l,r)\). Identity (5.1) says that the completions left of \(a\) are the baselines left of \(a\) plus the intervals \([h_j,b_j)\) that cover \(a\). The cases \(h_j=b_j\) (empty intervals) and \(a\) at an endpoint are included.

**Lemma 5.2 (matching by sorting).** Let \(h_1,\ldots,h_N\) and \(z_1,\ldots,z_N\) be real numbers with
\[
\#\{i:h_i\leq a\}\geq\#\{j:z_j\leq a\}\qquad\text{for every }a\in\mathbb R .
\]
List both families in nondecreasing order, \(h_{(1)}\leq\cdots\leq h_{(N)}\) and \(z_{(1)}\leq\cdots\leq z_{(N)}\). Then \(h_{(j)}\leq z_{(j)}\) for every \(j\). In particular there is a bijection \(\pi\) of \(\{1,\ldots,N\}\) with \(h_i\leq z_{\pi(i)}\) for all \(i\).

*Proof.* Suppose \(h_{(j)}>z_{(j)}\) for some \(j\), and put \(a=z_{(j)}\). At least \(j\) of the \(z\)'s are at most \(a\), namely \(z_{(1)},\ldots,z_{(j)}\). Since \(h_{(j)}>a\) and the list is sorted, at most \(j-1\) of the \(h\)'s are at most \(a\). This contradicts the hypothesis. Send the item listed \(j\)-th among the \(h\)'s to the item listed \(j\)-th among the \(z\)'s. \(\square\)

The fifth lesson uses Lemma 5.2 to attach deadlines to completions; the sixth uses (5.1) in the other direction, to turn deadlines that a packing must meet into coverage of test intervals.

## 6. Exercises

**6.1.** Let \(I\) consist of one item of size \(1/2\). Show that \(\mathrm{LP}(I)=1/2\) and \(\mathrm{LP}_{\mathrm{ind}}(I)=\mathrm{OPT}(I)=1\).

**6.2.** Show that \(\mathrm{LP}_{\mathrm{ind}}(I)\geq\sum_{i\in\mathcal I}a_i\) for every instance.

**6.3.** Give an instance with all sizes above \(1/6\) for which \(\mathrm{OPT}(I)=|\mathcal I|/5\), and one for which \(\mathrm{LP}(I)>|\mathcal I|/5\).

**6.4.** Show that the hypothesis of Lemma 5.2 cannot be weakened to "for every \(a\) among the \(h_i\)": give \(N=2\) and numbers satisfying the inequality at \(a=h_1,h_2\) for which no bijection with \(h_i\leq z_{\pi(i)}\) exists.

**6.5.** In the proof of Theorem 3.1, why is it necessary that the fractional value of the constructed instance is computed for the same graph \(K_4\) and the same \(k=2\) to which (b) is applied, rather than for a graph that has a vertex cover of size \(k\)?

## 7. Solutions

**6.1.** The type configuration with \(c_{1/2}=2\) has total size one, so \(z=1/2\) on it is feasible and \(\mathrm{LP}\leq1/2\). Every type configuration has \(c_{1/2}\leq2\), so \(\sum_cz_c\geq\frac12\sum_cc_{1/2}z_c\geq\frac12\). The only individual configuration containing the item is the singleton, so \(y\geq1\) there and \(\mathrm{LP}_{\mathrm{ind}}=1=\mathrm{OPT}\).

**6.2.** For feasible \(y\), \(\sum_Hy_H\geq\sum_Hy_H\sum_{i\in H}a_i=\sum_ia_i\sum_{H\ni i}y_H\geq\sum_ia_i\).

**6.3.** Five items of size \(1/5\) fill one bin: \(\mathrm{OPT}=1=5/5\). For the second, take five items of size \(2/5\): any configuration holds at most two of them, so \(\mathrm{LP}\geq5/2>1\) by the argument of Lemma 1.4 with weight \(1/2\).

**6.4.** Take \(h_1=0\), \(h_2=2\), \(z_1=z_2=1\). At \(a=0\) the left side is \(1\geq0\); at \(a=2\) it is \(2\geq2\). But \(h_2=2>1\) exceeds both \(z\)'s. The inequality fails at \(a=1\), where the left side is \(1\) and the right side \(2\).

**6.5.** Theorem 3.1 needs one instance whose fractional value is \(B\) and whose optimum exceeds \(B+c\). If the graph had a vertex cover of size \(k\), part (a) would give a packing into \(B\) bins, and there would be no gap. The point of the special case is that the fractional program can mix two local choices at every vertex, while an integral packing must make one choice per vertex, and \(K_4\) has no small enough cover.

## References

- [OpenAI-BP] OpenAI, *Additive hardness and unbounded configuration gaps in bin packing*, OpenAI Math Release preprint, 24 September 2026. https://github.com/openai/math/tree/main/preprints/Additive-hardness-and-unbounded-configuration-gaps-in-bin-packing-September-24-2026
- [OpenAI-Lean] OpenAI Math Release, *Bin packing and unbounded configuration-LP gaps*, scope of the Lean formalization. https://github.com/openai/math/blob/main/lean/docs/118.md
- [WS] D. P. Williamson and D. B. Shmoys, *The Design of Approximation Algorithms*, electronic edition on the authors' site. https://www.designofapproxalgs.com/
- [R] T. Rothvoss, *Approximating bin packing within O(log OPT · log log OPT) bins*, arXiv:1301.4010. https://arxiv.org/abs/1301.4010
- [HR] R. Hoberg and T. Rothvoss, *A logarithmic additive integrality gap for bin packing*, arXiv:1503.08796. https://arxiv.org/abs/1503.08796
- P. C. Gilmore and R. E. Gomory (1961), O. Marcotte (1985, 1986), G. Scheithauer and J. Terno (1995, 1997), and N. Karmarkar and R. M. Karp (1982) are named for credit for the program, the counterexamples to integer round-up, the conjecture and the first rounding algorithm; the course does not use their results.
