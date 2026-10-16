# Codes and the lamp module

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The group \(G_{\mathrm{sur}}=V\rtimes\Gamma\) of the construction is a semidirect product of \(\Gamma\) with a module \(V\) over a finite field \(\mathbb F_p\): a "lamp" in every element of \(\Gamma\), with values in \(\mathbb F_p\), subject to linear relations on every copy of every expander \(\Theta_i\). The relations come from a linear code \(C_i\) on the vertices of \(\Theta_i\): the relations on a copy are the dual code \(C_i^\perp\), and the possible patterns of lamp values that a character of \(V\) sees on the copy are then exactly the codewords of \(C_i\). The code contains one designated *prototype pattern*, which encodes the edges of \(\Theta_i\) at every vertex. This lesson chooses the codes, so that both \(C_i\) and \(C_i^\perp\) consist of vectors with large support, builds \(V\) and \(G_{\mathrm{sur}}\), and proves that, under the natural probability measure on the dual of \(V\), the pattern on every copy is uniformly distributed on its code [OpenAI-IT, Section 4]. The key point is that the relations imposed on all the overlapping copies together impose exactly the intended relations on each single copy; this is where the simultaneous overlap bound enters again.

- Ports and codes (Section 1).
- The module and the group (Section 2).
- The dual group and the distribution of patterns (Section 3).

The data of [Labelled expanders and cycle spaces](labelled-expanders-and-cycle-spaces.md), Proposition 2.1, are fixed: the graphs \(\Theta_i\) with \(n_i\) vertices, \(k_i=\lfloor n_i/2\rfloor\), \(\eta=\frac1{100}\), the labelling over \(S\), the group \(\Gamma\), its simple Cayley graph \(X\), the copies and the coned graph.

## 1. Ports and codes

An outgoing label at a vertex is called a *port*. At a vertex \(v\) of \(\Theta_i\), let \(J_i(v)\subseteq S^{\pm1}\) be the set of labels of the oriented edges leaving \(v\). Since the labelling is reduced and \(\Theta_i\) is \(d\)-regular, \(|J_i(v)|=d\).

Choose a prime \(p>2\) so large that \(p-1\) is at least the number of \(d\)-element subsets of \(S^{\pm1}\), and an injection \(J\mapsto a_J\) from these subsets into \(\mathbb F_p^\times=\mathbb F_p\setminus\{0\}\). The *decoder* is
\[
\mathcal J(a)=\begin{cases}J,&a=a_J,\\ \varnothing,&\text{otherwise}\end{cases}\qquad(a\in\mathbb F_p).
\]
The *prototype pattern* of \(\Theta_i\) is \(w_i\in\mathbb F_p^{\operatorname{Vert}(\Theta_i)}\), \(w_i(v)=a_{J_i(v)}\); all its coordinates are nonzero, and \(\mathcal J(w_i(v))=J_i(v)\).

On a coordinate space \(\mathbb F_p^E\), \(E\) a finite set, we use the bilinear form \(\langle z,z'\rangle=\sum_{v\in E}z(v)z'(v)\), which is nondegenerate, and orthogonal complements \(C^\perp\) with respect to it; thus \(\dim C^\perp=|E|-\dim C\) and \((C^\perp)^\perp=C\). The *support* of \(z\) is \(\operatorname{supp}z=\{v:z(v)\ne0\}\).

**Lemma 1.1** (counting subspaces). Let \(U\) be a vector space of dimension \(N\) over \(\mathbb F_p\), \(0\le a\le N\), and \(z\in U\) nonzero. Among the subspaces of dimension \(a\), the proportion containing \(z\) is \((p^a-1)/(p^N-1)\).

*Proof.* Count pairs \((C,y)\) with \(\dim C=a\) and \(0\ne y\in C\): every \(C\) contains \(p^a-1\) nonzero vectors. The group of invertible linear maps of \(U\) permutes the nonzero vectors transitively and the \(a\)-dimensional subspaces among themselves, so every nonzero \(y\) lies in the same number of subspaces. Hence that number is \(\frac{p^a-1}{p^N-1}\) times the number of subspaces. \(\square\)

**Lemma 1.2** (codes with both distances; [OpenAI-IT, Lemma 4.1]). For every \(i\) there is a subspace \(C_i\subseteq\mathbb F_p^{\operatorname{Vert}(\Theta_i)}\) of dimension \(k_i\) with \(w_i\in C_i\) such that every nonzero \(z\in C_i\cup C_i^\perp\) satisfies
\[
|\operatorname{supp}z|>\eta n_i .\tag{1.1}
\]

*Proof.* Write \(n=n_i\), \(k=k_i\), \(w=w_i\), and let \(\mathcal C\) be the set of \(k\)-dimensional subspaces \(C\supseteq\langle w\rangle\). Passing to the quotient by \(\langle w\rangle\), these correspond to the \((k-1)\)-dimensional subspaces of an \((n-1)\)-dimensional space, and a vector \(z\notin\langle w\rangle\) lies in \(C\) exactly when its image lies in the corresponding subspace. By Lemma 1.1, the proportion of \(C\in\mathcal C\) containing \(z\) is
\[
\frac{p^{k-1}-1}{p^{n-1}-1}<p^{k-n}.\tag{1.2}
\]
The map \(C\mapsto C^\perp\) is a bijection from \(\mathcal C\) onto the \((n-k)\)-dimensional subspaces of the \((n-1)\)-dimensional space \(w^\perp\), because \(C\supseteq\langle w\rangle\) exactly when \(C^\perp\subseteq w^\perp\). By Lemma 1.1 again, for nonzero \(z\in w^\perp\) the proportion of \(C\in\mathcal C\) with \(z\in C^\perp\) is
\[
\frac{p^{n-k}-1}{p^{n-1}-1}<p^{1-k},\tag{1.3}
\]
and for \(z\notin w^\perp\) it is zero.

Let \(r=\lfloor\eta n\rfloor\) and \(q=\eta/(1-\eta)<1\). For \(j\le r\), \(q^r\le q^j\), so
\[
q^r\sum_{j=0}^r\binom nj\le\sum_{j=0}^n\binom njq^j=(1+q)^n ,
\]
and since \(r\le\eta n\), \(\sum_{j\le r}\binom nj\le q^{-\eta n}(1+q)^n=2^{H\,n}\) with \(H=-\eta\log_2\eta-(1-\eta)\log_2(1-\eta)\). Here \(H<\frac9{100}\): the first term is \(\frac{\log_2100}{100}<\frac7{100}\), and the second is at most \(\eta/\ln2<2\eta\), because \(-\ln(1-\eta)\le\eta/(1-\eta)\) and \(\ln2>\frac12\). The number of vectors with support of size at most \(r\) is therefore
\[
\begin{aligned}
&\sum_{j=0}^r\binom nj(p-1)^j\\
&\quad\le p^{\eta n}2^{Hn}\le p^{(\eta+H)n}\\
&\quad<p^{n/4}.
\end{aligned}\tag{1.4}
\]
None of the nonzero ones lies in \(\langle w\rangle\), whose nonzero vectors have full support \(n>\eta n\). By (1.2), (1.3) and (1.4), the proportion of \(C\in\mathcal C\) for which \(C\) or \(C^\perp\) contains a nonzero vector of support at most \(r\) is less than
\[
\begin{aligned}
&p^{n/4}\bigl(p^{k-n}+p^{1-k}\bigr)\\
&\quad\le p^{-n/4}+p^{3/2-n/4}<1 ,
\end{aligned}
\]
using \(\frac{n-1}2\le k\le\frac n2\) and \(n>100\). So some \(C\in\mathcal C\) satisfies (1.1), since \(|\operatorname{supp}z|>r\) means \(|\operatorname{supp}z|>\eta n\). \(\square\)

Fix such codes \(C_i\). For a copy \(P=P_{g,i}\), the isomorphism \(\psi_P:\Theta_i\to P\) transports \(C_i\), \(C_i^\perp\), \(w_i\) and \(J_i\) to \(C_P,C_P^\perp\subseteq\mathbb F_p^P\), \(w_P\) and \(J_P\), where \(\mathbb F_p^P\) is the space of functions on the vertex set of \(P\); \(C_P^\perp\) is the orthogonal complement of \(C_P\), since transport preserves the bilinear form, and \(J_P(h)\) is the set of labels of the edges of \(P\) leaving \(h\).

## 2. The module and the group

Let \(\mathbb F_p^{(\Gamma)}\) be the space of finitely supported functions \(\Gamma\to\mathbb F_p\), with basis \((\mathbf e_h)_{h\in\Gamma}\) and the action \(g\mathbf e_h=\mathbf e_{gh}\) of \(\Gamma\). We regard \(\mathbb F_p^P\) as the subspace of functions supported on \(P\). Put
\[
W_0=\sum_{g\in\Gamma,\ i\ge1}C_{P_{g,i}}^\perp\ \subseteq\ \mathbb F_p^{(\Gamma)},\tag{2.1}
\]
the set of finite sums of elements of the spaces \(C_P^\perp\). Left translation by \(g\) maps \(P_{h,i}\) onto \(P_{gh,i}\), compatibly with the identifications with \(\Theta_i\), so it maps \(C_{P_{h,i}}^\perp\) onto \(C_{P_{gh,i}}^\perp\), and \(W_0\) is \(\Gamma\)-invariant.

**Lemma 2.1** (exact relations; [OpenAI-IT, Lemma 4.2]). For every copy \(P\),
\[
W_0\cap\mathbb F_p^P=C_P^\perp .\tag{2.2}
\]

*Proof.* The space \(C_P^\perp\) is contained in both. Conversely, let \(z\in W_0\cap\mathbb F_p^P\), and write \(z=\sum_{Q\in\mathcal F}z_Q\) with \(\mathcal F\) a finite set of distinct copies and \(0\ne z_Q\in C_Q^\perp\), combining terms on the same copy and dropping zeros. Suppose \(\mathcal F\) contains a copy other than \(P\). Take \(R=c_P\) and choose \(Q\in\mathcal F\setminus\{P\}\) whose center is farthest from \(R\); every other member of \(\mathcal F\), and \(P\), has its center at distance at most \(d(c_Q,R)\) from \(R\). By Lemma 3.1 of [Thin triangles and simultaneous overlaps](thin-triangles-and-simultaneous-overlaps.md), all vertices that \(Q\) shares with these copies lie in a ball \(B_Q\), which has fewer than \(\eta n_j\) vertices if \(Q\) has type \(j\) (Proposition 2.1 of the previous lesson). By (1.1), \(|\operatorname{supp}z_Q|>\eta n_j\), so there is \(h\in\operatorname{supp}z_Q\) outside \(B_Q\). Then \(h\notin P\), and \(h\) lies in no other member of \(\mathcal F\), so \(z(h)=z_Q(h)\ne0\), contradicting \(z\in\mathbb F_p^P\). Hence \(\mathcal F\subseteq\{P\}\) and \(z\in C_P^\perp\). \(\square\)

**Definition 2.2.** Let
\[
V=\mathbb F_p^{(\Gamma)}/W_0,\qquad v_*=[\mathbf e_1]\in V,
\]
with the induced action of \(\Gamma\), so that \(hv_*=[\mathbf e_h]\), and let \(G_{\mathrm{sur}}=V\rtimes\Gamma\) be the set \(V\times\Gamma\) with the multiplication
\[
(v,g)(v',g')=(v+gv',\,gg').
\]

**Lemma 2.3.** \(G_{\mathrm{sur}}\) is a countable group, generated by \((v_*,1)\) and the elements \((0,s)\), \(s\in S\). Every nonzero element of \(V\) has order \(p\) in \(G_{\mathrm{sur}}\).

*Proof.* The multiplication is associative because \(\Gamma\) acts by linear maps, \((0,1)\) is the identity, and \((v,g)^{-1}=(-g^{-1}v,g^{-1})\). \(\Gamma\) is countable, being finitely generated, and so is \(\mathbb F_p^{(\Gamma)}\), hence \(V\) and \(G_{\mathrm{sur}}\). The elements \((0,s)\) generate the subgroup \(\{0\}\times\Gamma\), and \((0,h)(v_*,1)(0,h)^{-1}=(hv_*,1)\). The classes \(hv_*=[\mathbf e_h]\) span \(V\) over \(\mathbb F_p\), and an \(\mathbb F_p\)-multiple of an element is a repeated sum, so the subgroup generated contains \(V\times\{1\}\), and then all \((v,g)=(v,1)(0,g)\). Finally \((v,1)^p=(pv,1)=(0,1)\). \(\square\)

## 3. The dual group and the distribution of patterns

Let \(\Omega=\operatorname{Hom}_{\mathbb F_p}(V,\mathbb F_p)\), the set of \(\mathbb F_p\)-linear functionals on \(V\), an abelian group under addition. The space \(V\) is countable, so it has a basis \(\mathcal B\), finite or countable: run through a countable spanning set and keep each vector that is not in the span of those kept before. Restriction to \(\mathcal B\) is a bijection \(\Omega\to\mathbb F_p^{\mathcal B}\), and we give \(\Omega\) the product topology and the product \(m\) of the uniform probability measures on the factors \(\mathbb F_p\) [Measure and Integration, Section 254]. A *cylinder set* is a set of the form \(\{\omega:\omega(b_1)=x_1,\ldots,\omega(b_k)=x_k\}\) with \(b_j\in\mathcal B\); it has measure \(p^{-k}\), and every nonempty open set contains one. The measure \(m\) is invariant under translations \(\omega\mapsto\omega+\omega_0\): translation permutes the cylinder sets of each fixed shape, and a measure on the product is determined by its values on cylinder sets.

For \(\omega\in\Omega\) and \(h\in\Gamma\) put
\[
X_\omega(h)=\omega(hv_*)\in\mathbb F_p ,
\]
the *pattern* of \(\omega\). For each \(v\in V\), \(\omega\mapsto\omega(v)\) depends on finitely many coordinates, since \(v\) is a finite combination of elements of \(\mathcal B\); so it is continuous and locally constant.

**Lemma 3.1** (uniform pattern marginals; [OpenAI-IT, Lemma 4.4]). Let \(P\) be a copy of type \(i\). The restriction map \(\operatorname{res}_P:\Omega\to\mathbb F_p^P\), \(\omega\mapsto X_\omega|_P\), has image \(C_P\), and the measure of \(\{\omega:X_\omega|_P=a\}\) is \(p^{-k_i}\) for every \(a\in C_P\). In particular \(m\{\omega:X_\omega|_P=w_P\}=p^{-k_i}\).

*Proof.* Let \(q_P:\mathbb F_p^P\to V\) be the restriction of the quotient map. By Lemma 2.1, \(\ker q_P=C_P^\perp\). For \(z\in\mathbb F_p^P\),
\[
\omega(q_P(z))=\sum_{h\in P}z(h)\,\omega(hv_*)=\langle z,X_\omega|_P\rangle .
\]
So \(X_\omega|_P\) annihilates \(C_P^\perp\), that is \(X_\omega|_P\in C_P\). Conversely, for \(a\in C_P\) the rule \(q_P(z)\mapsto\langle z,a\rangle\) is a well-defined linear functional on the finite-dimensional subspace \(U_P=q_P(\mathbb F_p^P)\) of \(V\), since \(a\) annihilates \(\ker q_P\); extending a basis of \(U_P\) to a basis of \(V\) extends it to some \(\omega\in\Omega\), and then \(X_\omega|_P=a\). So the image is \(C_P\).

The map \(\operatorname{res}_P\) is additive and depends only on the restriction of \(\omega\) to \(U_P\), so on finitely many coordinates; its fibres are measurable. The fibres over \(a\) and \(a'\) are translates of each other by any \(\omega_0\) with \(\operatorname{res}_P(\omega_0)=a'-a\), so by translation invariance they have the same measure. They partition \(\Omega\) into \(|C_P|=p^{k_i}\) sets of equal measure, each of measure \(p^{-k_i}\). The prototype \(w_P\) belongs to \(C_P\) because \(w_i\in C_i\). \(\square\)

The lemma describes the pattern on each single copy; it says nothing about the joint distribution on several copies, and nothing of the kind is needed. Without the exact relations (2.2), the relations imposed on overlapping copies could combine into further relations on a single copy, and the patterns there would not be uniform on \(C_P\).

## 4. Exercises

**4.1** (easy). Let \(d=3\) and \(|S|=2\). How many \(3\)-element subsets does \(S^{\pm1}\) have, and what is the smallest admissible prime \(p\)?

**4.2** (medium). Let \(n=4\), \(p=3\) and \(w=(1,1,1,1)\). Find a \(2\)-dimensional code \(C\ni w\) in \(\mathbb F_3^4\) such that every nonzero vector of \(C\cup C^\perp\) has support at least \(2\). (Note that \(\langle w,w\rangle=4=1\ne0\) in \(\mathbb F_3\).)

**4.3** (easy). Show that \((v,1)\) and \((0,g)\) satisfy \((0,g)(v,1)(0,g)^{-1}=(gv,1)\) in \(G_{\mathrm{sur}}\), and that \(V\times\{1\}\) is a normal abelian subgroup.

**4.4** (medium). Show that for every \(v\ne0\) in \(V\) there is \(\omega\in\Omega\) with \(\omega(v)\ne0\), and deduce that \(\int_\Omega e^{2\pi i\,\omega(v)/p}\,dm(\omega)=0\), where \(\omega(v)\in\mathbb F_p\) is read as an integer in \(\{0,\ldots,p-1\}\).

## 5. Solutions

**4.1.** \(S^{\pm1}\) has \(4\) elements and \(\binom43=4\) subsets of size \(3\). The prime must satisfy \(p>2\) and \(p-1\ge4\), so \(p=5\).

**4.2.** Take \(C\) spanned by \(w=(1,1,1,1)\) and \(u=(1,2,0,0)\). Its vectors are \(\alpha w+\beta u=(\alpha+\beta,\alpha+2\beta,\alpha,\alpha)\). If \(\alpha\ne0\), the last two coordinates are nonzero; if \(\alpha=0\ne\beta\), the vector \((\beta,2\beta,0,0)\) has support \(2\). The dual \(C^\perp\) consists of the \(z\) with \(z_1+z_2+z_3+z_4=0\) and \(z_1+2z_2=0\). In \(\mathbb F_3\) the second equation gives \(z_1=z_2\), and then the first gives \(z_4=z_2-z_3\): so \(z=(z_2,z_2,z_3,z_2-z_3)\). If \(z_2\ne0\), the first two coordinates are nonzero; if \(z_2=0\ne z_3\), the vector \((0,0,z_3,-z_3)\) has support \(2\). So every nonzero vector of \(C\cup C^\perp\) has support at least \(2\).

**4.3.** \((0,g)(v,1)=(gv,g)\) and \((gv,g)(0,g^{-1})=(gv,1)\). The subgroup \(V\times\{1\}\) is abelian because \((v,1)(v',1)=(v+v',1)\), and normal by the conjugation formula and \((v',1)(v,1)(v',1)^{-1}=(v,1)\).

**4.4.** Extend \(v\) to a basis of \(V\) and let \(\omega\) be \(1\) on \(v\) and \(0\) on the other basis vectors. Put \(\chi(\omega)=e^{2\pi i\,\omega(v)/p}\), a continuous function with \(\chi(\omega+\omega_0)=\chi(\omega)\chi(\omega_0)\), because \(\omega\mapsto\omega(v)\) is additive and the exponential is periodic modulo \(p\). By translation invariance, \(\int\chi\,dm=\chi(\omega_0)\int\chi\,dm\) for every \(\omega_0\); with \(\omega_0(v)=1\), \(\chi(\omega_0)=e^{2\pi i/p}\ne1\), so \(\int\chi\,dm=0\).

## References

- [OpenAI-IT] OpenAI, *An irrational-trace counterexample to reduced Baum–Connes*, OpenAI Math Release preprint, 23 September 2026, Section 4, Lemmas 4.1, 4.2 and 4.4. https://github.com/openai/math/tree/main/preprints/An-Irrational-Trace-Counterexample-to-Reduced-Baum-Connes-September-23-2026
- [Measure and Integration] Core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10): D. H. Fremlin, *Measure Theory*, Volume 2, Section 254 (infinite products of probability spaces).
