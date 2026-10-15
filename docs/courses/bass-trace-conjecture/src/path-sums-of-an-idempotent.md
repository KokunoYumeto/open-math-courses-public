# Path sums of an idempotent

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Fix a finitely generated group \(G\), an idempotent matrix \(e\) over \(\mathbb CG\) and an element \(g\in G\) of infinite order. This lesson attaches to \(e\) and \(g\) a finite weighted sum \(v_k\) over lists of \(k\) group elements, for every \(k\ge1\). The weight of a list is the trace of a product of coefficient matrices of \(e\) along the list, closed up by \(g\). Three identities hold: a cyclic shift of the lists that multiplies one entry by \(g\) preserves \(v_k\); deleting one entry of the lists turns \(v_k\) into \(v_{k-1}\); and the total weight of every \(v_k\) is the coefficient \(\lambda\) of the trace of \(e\) at \([g]\). These identities and the finiteness of the sums are all that the later lessons use about \(e\). The construction follows [OpenAI-BT, Section 7].

- The kernel of an idempotent (Section 1).
- The centralizer and the coset graph (Section 2).
- Path weights (Section 3).
- The twisted shift and the deletion identities (Section 4).

Notation from [Traces of projective modules](traces-of-projective-modules.md): right modules, matrices acting on columns, and \(\operatorname{HS}_G(x)(C)\) for the coefficient of the Hattori–Stallings trace at a conjugacy class \(C\).

## 1. The kernel of an idempotent

Let \(e\in\operatorname{Mat}_r(\mathbb CG)\) be idempotent and write
\[
e=\sum_{s\in G}A_s\,s,\qquad A_s\in\operatorname{Mat}_r(\mathbb C),
\]
with finite support \(S_0=\{s:A_s\ne0\}\). The coefficient of \(t\) in \(e^2\) is \(\sum_{uv=t}A_uA_v\), so idempotence says that for every \(t\in G\)
\[
\sum_{uv=t}A_uA_v=A_t .
\tag{1.1}
\]
Define the matrix-valued *kernel* on \(G\times G\) by
\[
a(h,h')=A_{h^{-1}h'} .
\]
It is invariant under simultaneous left translation, \(a(ch,ch')=a(h,h')\) for all \(c\in G\), and for fixed \(h\) it is nonzero only for \(h'\in hS_0\); for fixed \(h'\) only for \(h\in h'S_0^{-1}\). Substituting \(u=h^{-1}k\) and \(v=k^{-1}h'\) in (1.1) gives the kernel identity
\[
\begin{aligned}
&\sum_{k\in G}a(h,k)\,a(k,h')\\
&\quad=a(h,h') ,
\end{aligned}
\tag{1.2}
\]
a finite sum. In products \(a(h_0,h_1)a(h_1,h_2)\cdots\) the matrices multiply in the order in which the coefficients of \(e\) multiply in the powers of \(e\), which is the order of composition of maps on columns.

By formula (3.1) of [Traces of projective modules](traces-of-projective-modules.md), the coefficient of the trace of \(e\) at \([g]\) is
\[
\begin{aligned}
\lambda&=\operatorname{HS}_G\bigl([e(\mathbb CG)^r]\bigr)([g])\\
&=\sum_{s\in[g]}\operatorname{tr}A_s .
\end{aligned}
\tag{1.3}
\]

## 2. The centralizer and the coset graph

Put
\[
\begin{gathered}
J=C_G(g),\qquad H=J/\langle g\rangle,\\
Y=\langle g\rangle\backslash G ,
\end{gathered}
\]
and write \(\bar h=\langle g\rangle h\) for the coset of \(h\). The cyclic group \(\langle g\rangle\) is central in \(J\), so \(H\) is a group. Choose a finite symmetric generating set \(S\) of \(G\) with \(1\notin S\) and \(S_0\setminus\{1\}\subseteq S\); this is possible since \(G\) is finitely generated. Join \(\bar h\) to \(\overline{hs}\) by an edge for every \(s\in S\) with \(\overline{hs}\ne\bar h\).

**Lemma 2.1.** (a) The edges are well defined and make \(Y\) a connected simple graph in which every vertex has at most \(|S|\) neighbours. Put \(D=\max\{2,|S|\}\).
(b) The rule \(\bar c\cdot\bar h=\overline{ch}\) for \(c\in J\) defines an action of \(H\) on \(Y\) by graph automorphisms, free on vertices.
(c) \(H\) and \(Y\) are countable.

*Proof.* (a) If \(\bar h=\bar h'\), then \(h'=g^jh\) and \(\overline{h's}=\overline{g^jhs}=\overline{hs}\), so the neighbours of a vertex do not depend on the representative. The relation is symmetric because \(S=S^{-1}\): \(\overline{hs}\) is joined to \(\overline{hss^{-1}}=\bar h\). Each vertex has at most \(|S|\) neighbours. For \(h=s_1\cdots s_m\) with \(s_i\in S\), the vertices \(\bar1,\overline{s_1},\overline{s_1s_2},\ldots,\bar h\) are consecutively equal or adjacent, so the graph is connected.

(b) For \(c\in J\) and \(j\in\mathbb Z\), \(\overline{c\,g^jh}=\overline{g^jch}=\overline{ch}\) since \(c\) commutes with \(g\); and \(\overline{g^ic\,h}=\overline{ch}\). So \(\overline{ch}\) depends only on \(\bar c\in H\) and \(\bar h\in Y\). The map \(\bar h\mapsto\overline{ch}\) sends the edge from \(\bar h\) to \(\overline{hs}\) to the edge from \(\overline{ch}\) to \(\overline{chs}\), so it is a graph automorphism. If \(\overline{ch}=\bar h\), then \(ch=g^jh\) for some \(j\), so \(c=g^j\) and \(\bar c=1\): the action is free on vertices.

(c) A finitely generated group is countable, and so are its quotients and coset spaces. \(\square\)

The graph \(Y\), the group \(H\) and the bound \(D\) are fixed once and for all by \(e\) and \(g\). Later lessons build simplicial cycles of every even dimension on the vertex set \(Y\); the degree bound \(D\) does not depend on the dimension.

## 3. Path weights

For \(k\ge1\) let \(J\) act on \(G^k\) by simultaneous left multiplication, \(c\cdot(h_0,\ldots,h_{k-1})=(ch_0,\ldots,ch_{k-1})\), and let \(Q_k=J\backslash G^k\) be the set of orbits. This action is free, since left multiplication on \(G\) is free. Define the *weight*
\[
\begin{aligned}
&w_k(h_0,\ldots,h_{k-1})\\
&\ =\operatorname{tr}\bigl(a(h_0,h_1)\cdots a(h_{k-2},h_{k-1})\\
&\qquad\quad a(h_{k-1},gh_0)\bigr),
\end{aligned}
\]
with \(w_1(h_0)=\operatorname{tr}a(h_0,gh_0)\). For \(c\in J\) we have \(cgh_0=gch_0\), and the kernel is left invariant, so \(w_k\) is constant on \(J\)-orbits.

The *increments* of a tuple are
\[
\begin{gathered}
s_i=h_i^{-1}h_{i+1}\quad(0\le i<k-1),\\
s_{k-1}=h_{k-1}^{-1}gh_0 .
\end{gathered}
\]
The weight is \(\operatorname{tr}(A_{s_0}A_{s_1}\cdots A_{s_{k-1}})\), so it vanishes unless every increment lies in \(S_0\). The product of the increments telescopes:
\[
s_0s_1\cdots s_{k-1}=h_0^{-1}gh_0 .
\tag{3.1}
\]

**Lemma 3.1.** Two tuples with the same increments lie in the same \(J\)-orbit. Consequently at most \(|S_0|^k\) orbits in \(Q_k\) have nonzero weight.

*Proof.* The increments determine the tuple from its first entry: \(h_{i+1}=h_is_i\). If two tuples with first entries \(h_0\), \(h_0'\) have the same increments, (3.1) gives \(h_0^{-1}gh_0=h_0'^{-1}gh_0'\), so \(c=h_0'h_0^{-1}\) commutes with \(g\), and the second tuple is \(c\) times the first. \(\square\)

So
\[
v_k=\sum_{q\in Q_k}w_k(q)\,q
\]
is a finite linear combination of elements of \(Q_k\); we call it the *path sum* of length \(k\). For a function \(p\) on \(G^k\) that is constant on \(J\)-orbits write
\[
v_k(p)=\sum_{q\in Q_k}w_k(q)\,p(q),
\]
a finite sum. The weights are complex numbers; they need not be real or positive.

## 4. The twisted shift and the deletion identities

The *twisted shift* is the map
\[
T(h_0,\ldots,h_{k-1})=(h_1,\ldots,h_{k-1},gh_0)
\]
of \(G^k\). For \(c\in J\), \(T(ch)=cT(h)\) because \(cg=gc\), so \(T\) induces a map of \(Q_k\), again written \(T\). For \(k\ge2\) and \(0\le i<k\), deleting the entry in position \(i\) gives a map \(d_i:G^k\to G^{k-1}\) which commutes with the action of \(J\) and induces \(d_i:Q_k\to Q_{k-1}\). For a finite combination \(v=\sum_qv(q)q\) put \(T_*v=\sum_qv(q)\,Tq\) and \((d_i)_*v=\sum_qv(q)\,d_iq\).

**Lemma 4.1** (path identities [OpenAI-BT, Lemma 7.2]). Let \(k\ge1\).

1. \(T\) is a bijection of \(Q_k\), and \(w_k(Tq)=w_k(q)\) for all \(q\). Hence \(T_*v_k=v_k\).
2. For \(k\ge2\) and \(0\le i<k\), \((d_i)_*v_k=v_{k-1}\).
3. Every \(v_k\) has total weight \(v_k(1)=\lambda\), the coefficient (1.3).

*Proof.* (1) The map sending \((h_0,\ldots,h_{k-1})\) to \((g^{-1}h_{k-1},h_0,\ldots,h_{k-2})\) is inverse to \(T\) and also commutes with \(J\). For \(k=1\), \(T(h_0)=gh_0\) lies in the orbit of \(h_0\) since \(g\in J\), so \(T\) is the identity of \(Q_1\). For \(k\ge2\),
\[
\begin{aligned}
&w_k(Th)\\
&\ =\operatorname{tr}\bigl(a(h_1,h_2)\cdots a(h_{k-1},gh_0)\\
&\qquad\quad a(gh_0,gh_1)\bigr),
\end{aligned}
\]
and \(a(gh_0,gh_1)=a(h_0,h_1)\). The product is a cyclic rotation of the product defining \(w_k(h)\), and the trace of a product of matrices is invariant under cyclic rotation. So \(w_k\circ T=w_k\), and \(T_*v_k=\sum_qw_k(q)\,Tq\) equals \(\sum_{q'}w_k(T^{-1}q')\,q'=v_k\).

(2) Fix an orbit \(q'\in Q_{k-1}\) and a representative \((h'_0,\ldots,h'_{k-2})\). An orbit \(q\in Q_k\) with \(d_iq=q'\) contains exactly one tuple whose entries outside position \(i\) are \(h'_0,\ldots,h'_{k-2}\), in order: some tuple in \(q\) has this property after left multiplication by an element of \(J\), and that element is unique because \(J\) acts freely on \(G^{k-1}\). So the orbits over \(q'\) correspond to the elements \(u\in G\) inserted at position \(i\), and
\[
\bigl((d_i)_*v_k\bigr)(q')=\sum_{u\in G}w_k(\ldots,u,\ldots),
\]
a finite sum since the kernel has finite rows and columns. Write \(h=(h_0,\ldots,h_{k-1})\) for the tuple with \(h_i=u\).

For \(0<i<k-1\), the factors of \(w_k\) involving \(u\) are \(a(h_{i-1},u)a(u,h_{i+1})\), and (1.2) gives \(\sum_ua(h_{i-1},u)a(u,h_{i+1})=a(h_{i-1},h_{i+1})\). For \(i=k-1\), the factors are \(a(h_{k-2},u)a(u,gh_0)\), and (1.2) gives \(a(h_{k-2},gh_0)\). In both cases the result is \(w_{k-1}(h')\).

For \(i=0\), put \(B=a(h_1,h_2)\cdots a(h_{k-2},h_{k-1})\), with \(B\) the identity matrix if \(k=2\). By cyclicity of the trace, then left invariance under \(g\), then (1.2) with the substitution \(u'=gu\),
\[
\begin{aligned}
&\sum_u\operatorname{tr}\bigl(a(u,h_1)\,B\,a(h_{k-1},gu)\bigr)\\
&\ =\sum_u\operatorname{tr}\bigl(B\,a(h_{k-1},gu)\,a(gu,gh_1)\bigr)\\
&\ =\operatorname{tr}\bigl(B\,a(h_{k-1},gh_1)\bigr),
\end{aligned}
\]
which is \(w_{k-1}(h_1,\ldots,h_{k-1})\).

(3) Deletion preserves total weight, so by (2) all \(v_k(1)\) equal \(v_1(1)=\sum_{Jh\in Q_1}\operatorname{tr}A_{h^{-1}gh}\). The map \(Jh\mapsto h^{-1}gh\) from \(J\backslash G\) to the class \([g]\) is well defined and surjective, and it is injective: \(h^{-1}gh=h'^{-1}gh'\) means that \(h'h^{-1}\) commutes with \(g\). So \(v_1(1)=\sum_{s\in[g]}\operatorname{tr}A_s=\lambda\) by (1.3). \(\square\)

The proof of (2) uses idempotence of \(e\) only through (1.2), and (1) uses only the cyclicity of the trace. Both use the invariance of the kernel under left multiplication by elements of \(J\); invariance under all of \(G\) is not needed. The lessons [Exterior chains and sparse cycles](exterior-chains-and-sparse-cycles.md) and [A Pfaffian cocycle](a-pfaffian-cocycle.md) use only Lemmas 2.1, 3.1 and 4.1.

**Example 4.2.** Let \(G=\langle t,s\mid s^2=1,\ sts^{-1}=t^{-1}\rangle\) be the infinite dihedral group, \(f=\tfrac12(1+s)\) and \(e=f-f\,t\,(1-f)\). Then \(e\) is idempotent (Exercise 5.1), and since \((1+s)t(1-s)=t-ts+st-t^{-1}\),
\[
e=\tfrac12+\tfrac12s-\tfrac14t+\tfrac14ts-\tfrac14st+\tfrac14t^{-1}.
\]
For \(g=t\), the class \([t]\) is \(\{t,t^{-1}\}\) and \(\lambda=-\tfrac14+\tfrac14=0\). Here \(J=\langle t\rangle\), \(Q_1\) has the two elements \(J\) and \(Js\), and \(v_1=-\tfrac14J+\tfrac14Js\), since \(s^{-1}ts=t^{-1}\). The weights are nonzero, and their total is \(0\).

## 5. Exercises

**5.1** (easy). Show that \(e=f-fa(1-f)\) is idempotent for every idempotent \(f\) and every \(a\) in a ring, and that \(e\) and \(f\) have the same trace in \(\operatorname{HH}_0\).

**5.2** (easy). Show that \(T^k\) is the identity map of \(Q_k\).

**5.3** (easy). Let \(F\le G\) be a finite subgroup and \(e=|F|^{-1}\sum_{f\in F}f\). Show that \(v_k=0\) for every \(k\) and every \(g\) of infinite order.

**5.4** (medium). Suppose that \(e\in\operatorname{Mat}_r(\mathbb CG)\) satisfies \(e^2=\mu e\) for a complex number \(\mu\), and define \(w_k\) and \(v_k\) by the same formulas. Show that \((d_i)_*v_k=\mu\,v_{k-1}\) and \(T_*v_k=v_k\).

**5.5** (medium). Compute \(v_2\) in Example 4.2: list the orbits in \(Q_2\) with nonzero weight by their increments, give the weights, and check \((d_0)_*v_2=(d_1)_*v_2=v_1\).

## 6. Solutions

**5.1.** Put \(n=fa(1-f)\). Then \(fn=n\), \(nf=0\) and \(n^2=0\), so \(e^2=(f-n)^2=f-fn-nf+n^2\), which is \(f-n=e\). The trace of \(n\) is \(\operatorname{tr}(fa(1-f))\equiv\operatorname{tr}(a(1-f)f)=0\) modulo commutators (Lemma 2.1 of [Traces of projective modules](traces-of-projective-modules.md)).

**5.2.** \(T^k(h_0,\ldots,h_{k-1})=(gh_0,\ldots,gh_{k-1})\), which is \(g\) times the original tuple, and \(g\in J\).

**5.3.** All increments of a tuple of nonzero weight lie in \(S_0\subseteq F\), so their product lies in \(F\). By (3.1) it is conjugate to \(g\), which has infinite order, while elements of \(F\) have finite order. So no tuple has nonzero weight.

**5.4.** The coefficient form of \(e^2=\mu e\) is \(\sum_{uv=t}A_uA_v=\mu A_t\), so (1.2) becomes \(\sum_ka(h,k)a(k,h')=\mu\,a(h,h')\), and each deletion in the proof of Lemma 4.1(2) produces a factor \(\mu\). The shift identity uses only the cyclicity of the trace.

**5.5.** The support is \(S_0=\{1,s,t,ts,st,t^{-1}\}\) with coefficients \(\tfrac12,\tfrac12,-\tfrac14,\tfrac14,-\tfrac14,\tfrac14\). An orbit in \(Q_2\) with nonzero weight is given by its increments \((s_0,s_1)\in S_0^2\), with \(s_0s_1\in\{t,t^{-1}\}\) by (3.1), and its weight is \(A_{s_0}A_{s_1}\). Using \(ts=st^{-1}\) and \(st=t^{-1}s\), exactly eight pairs qualify:

- product \(t\): \((1,t)\), \((t,1)\), \((s,st)\), \((ts,s)\), with weights \(-\tfrac18,-\tfrac18,-\tfrac18,\tfrac18\);
- product \(t^{-1}\): \((1,t^{-1})\), \((t^{-1},1)\), \((s,ts)\), \((st,s)\), with weights \(\tfrac18,\tfrac18,\tfrac18,-\tfrac18\).

Deleting \(h_1\) keeps \(h_0\), and \(h_0\in J\) exactly when \(s_0s_1=h_0^{-1}th_0=t\). So \((d_1)_*v_2=-\tfrac14J+\tfrac14Js=v_1\). Deleting \(h_0\) keeps \(h_1\), and \(h_1^{-1}th_1=s_1s_0\). The reversed products are \(t\) for \((1,t)\), \((t,1)\), \((s,ts)\), \((st,s)\), with total weight \(-\tfrac14\), and \(t^{-1}\) for the other four, with total weight \(\tfrac14\). So \((d_0)_*v_2=v_1\) as well.

## References

- [OpenAI-BT] OpenAI, *The Bass trace conjecture for complex group rings*, OpenAI Math Release preprint, 24 September 2026, Section 7. https://github.com/openai/math/tree/main/preprints/The-Bass-trace-conjecture-for-complex-group-rings-September-24-2026
