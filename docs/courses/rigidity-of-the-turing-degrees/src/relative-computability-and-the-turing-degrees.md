# Relative computability and the Turing degrees

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A set \(B\) of natural numbers is computable from a set \(A\) if there is a procedure that decides membership in \(B\) and may ask, during its work, finitely many questions of the form "is \(k\) in \(A\)?". Two sets that are computable from each other have the same *Turing degree*. The degrees are partially ordered by this relation, and the question of this course is whether the partial order has symmetries: is there a bijection of the set of degrees that preserves the order and is not the identity? [OpenAI-R] proves that there is none, from a theorem of T. Slaman and W. H. Woodin.

This lesson fixes the definitions and proves the facts about relative computability that the course uses. Computability relative to a set is defined here through computably enumerable sets of finite pieces of information. The lesson does not use machines with oracles.

- Reductions and the relation \(B\le_TA\); composition (Lemma 2.1).
- Joins and the Turing degrees; automorphisms preserve joins (Lemmas 3.1 to 3.3).
- A sequence of sets that is computed step by step is computed uniformly (Lemma 4.1).
- Real numbers as cuts in the rationals (Lemma 5.1).

The lesson follows [OpenAI-R, Section 2] for the statements about reals. It uses the notions of a computable function, a computable set and a computably enumerable set from the core course [Mathematical Logic, Set Theory, and Computability (C80)](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C80), whose text is [OLP].

## 1. Sets, strings and computably enumerable sets

A set \(A\subset\mathbb N\) is identified with its characteristic function: \(A(n)=1\) if \(n\in A\) and \(A(n)=0\) otherwise. So the sets of natural numbers are the points of \(2^{\mathbb N}\), the infinite sequences of bits. A *string* is a finite sequence \(\sigma\) of bits, of length \(|\sigma|\). It is an *initial segment* of \(A\), written \(\sigma\prec A\), if \(\sigma(k)=A(k)\) for all \(k<|\sigma|\); in the same way a string can be an initial segment of a string.

Strings, pairs, triples and finite sequences of such objects are coded by natural numbers in a fixed computable way. So we can speak of computable and of computably enumerable sets of strings or of triples.

From [OLP, part Computability, chapter Computability Theory] we use three facts.

- (E1) A set \(S\) is computably enumerable exactly if there is a computable relation \(R\) with \(S=\{x:\exists y\,R(x,y)\}\) (section "Equivalent Definitions of Computably Enumerable Sets").
- (E2) There is a list \(W_0,W_1,W_2,\dots\) that contains every computably enumerable set, such that the set of the pairs \((e,x)\) with \(x\in W_e\) is computably enumerable. In [OLP], \(W_e\) is the domain of the partial computable function with the index \(e\), and \(x\in W_e\) exactly if \(\exists y\,T(e,x,y)\) with Kleene's computable predicate \(T\) (sections "The Normal Form Theorem" and "The Universal Partial Computable Function").
- (E3) A set is computable exactly if the set and its complement are computably enumerable (section "Computably Enumerable Sets not Closed under Complement").

By (E1), a set is computably enumerable if membership of \(x\) can be certified by a finite object \(y\) that passes a computable test. We use (E1) in this form: to show that a set is computably enumerable we say what a certificate is. A certificate may consist of several finite objects, and it may contain certificates for finitely many memberships in other computably enumerable sets.

## 2. Reductions

**Definition.** A *reduction* is a computably enumerable set \(\Phi\) of triples \((\sigma,n,b)\) of a string \(\sigma\), a number \(n\) and a bit \(b\). The reduction \(\Phi\) *computes \(B\) from \(A\)*, for sets \(A,B\), if for all \(n\) and \(b\): \(B(n)=b\) exactly if there is a string \(\sigma\prec A\) with \((\sigma,n,b)\in\Phi\).
The set \(B\) is *computable from* \(A\), written \(B\le_TA\), if some reduction computes \(B\) from \(A\).

A triple \((\sigma,n,b)\) says: "if the set begins with \(\sigma\), the answer to the question \(n\) is \(b\)". A reduction computes at most one set from a given \(A\), and from many sets \(A\) it computes nothing.

The relation \(\le_T\) is the usual Turing reducibility, which is defined in the literature by machines that may ask questions about \(A\). A computation of such a machine that halts has asked finitely many questions; so the halting computations are described by triples of this kind, which can be listed by a procedure. Conversely, a machine can search through a list of the triples of \(\Phi\) for one whose string is an initial segment of \(A\). This comparison is not used in the proofs of the course. It matters for the last lesson, where a theorem of the literature about Turing reducibility is taken as a hypothesis. Let \(\Phi_e\) be the set of the triples whose codes lie in \(W_e\). By (E2) every reduction is a \(\Phi_e\). So \(B\le_TA\) exactly if \(\Phi_e\) computes \(B\) from \(A\) for some *index* \(e\).

**Lemma 2.1.**

1. There is a reduction that computes \(A\) from \(A\) for every set \(A\).
2. For reductions \(\Phi,\Psi\) there is a reduction \(\Psi\circ\Phi\) with the following property: whenever \(\Phi\) computes \(B\) from \(A\) and \(\Psi\) computes \(C\) from \(B\), the reduction \(\Psi\circ\Phi\) computes \(C\) from \(A\). In particular \(\le_T\) is transitive.
3. A set is computable exactly if it is computable from the empty set, and then it is computable from every set. A set that is computable from a computable set is computable.
4. For every \(A\) there are at most countably many sets \(B\le_TA\).

**Proof.** (1) The set of the triples \((\sigma,n,\sigma(n))\) with \(n<|\sigma|\) is computable.

(2) Let \(\Psi\circ\Phi\) be the set of the triples \((\sigma,n,b)\) for which there is a string \(\rho\) such that \((\rho,n,b)\in\Psi\) and for every \(k<|\rho|\) there is an initial segment \(\sigma_k\) of \(\sigma\) with \((\sigma_k,k,\rho(k))\in\Phi\). It is computably enumerable: a certificate consists of \(\rho\), the \(\sigma_k\), and certificates for the memberships in \(\Phi\) and \(\Psi\). Let \(\Phi\) compute \(B\) from \(A\) and \(\Psi\) compute \(C\) from \(B\).

If \(C(n)=b\), there is \(\rho\prec B\) with \((\rho,n,b)\in\Psi\). For every \(k<|\rho|\) we have \(B(k)=\rho(k)\), so there is \(\sigma_k\prec A\) with \((\sigma_k,k,\rho(k))\in\Phi\). The longest of these strings is a \(\sigma\prec A\) with \((\sigma,n,b)\in\Psi\circ\Phi\).

Conversely let \((\sigma,n,b)\in\Psi\circ\Phi\) with \(\sigma\prec A\), and \(\rho\), \(\sigma_k\) as in the definition. Each \(\sigma_k\) is an initial segment of \(A\), so \(B(k)=\rho(k)\) because \(\Phi\) computes \(B\) from \(A\). Hence \(\rho\prec B\), and \(C(n)=b\) because \(\Psi\) computes \(C\) from \(B\).

(3) If \(B\) is computable, the set of the triples \((\sigma,n,B(n))\) with the empty string \(\sigma\) is computable, and it computes \(B\) from every set. Let \(\Phi\) compute \(B\) from a computable set \(A\). Then \(n\in B\) exactly if there is \(\sigma\prec A\) with \((\sigma,n,1)\in\Phi\), and \(n\notin B\) exactly if there is \(\sigma\prec A\) with \((\sigma,n,0)\in\Phi\). The relation \(\sigma\prec A\) is computable. So \(B\) and its complement are computably enumerable, and \(B\) is computable by (E3).

(4) Each \(\Phi_e\) computes at most one set from \(A\). \(\blacksquare\)

## 3. Joins and degrees

The *join* of two sets is
\[
\begin{aligned}
A\oplus B&=\{2n:n\in A\}\\
&\quad\cup\{2n+1:n\in B\}.
\end{aligned}
\]
For strings \(\rho,\sigma\) let \(\rho\oplus\sigma\) be the join, formed in the same way, of their initial segments of the length \(\min\{|\rho|,|\sigma|\}\). If \(\rho\prec A\) and \(\sigma\prec B\), then \(\rho\oplus\sigma\prec A\oplus B\), and every initial segment of \(A\oplus B\) is an initial segment of such a string. Joins of three or more sets are formed by repetition: \(A\oplus B\oplus C=(A\oplus B)\oplus C\), and so on.

**Lemma 3.1.**

1. There are reductions that compute \(A\) from \(A\oplus B\), and \(B\) from \(A\oplus B\), for all sets \(A,B\).
2. For reductions \(\Phi_1,\Phi_2\) there is a reduction that computes \(B_1\oplus B_2\) from \(A\) whenever \(\Phi_1\) computes \(B_1\) and \(\Phi_2\) computes \(B_2\) from \(A\).
3. \(A\oplus B\le_TX\) exactly if \(A\le_TX\) and \(B\le_TX\).

**Proof.** (1) The triples \((\gamma,n,\gamma(2n))\) with \(2n<|\gamma|\), and \((\gamma,n,\gamma(2n+1))\) with \(2n+1<|\gamma|\). (2) The triples \((\sigma,2n,b)\) with \((\sigma,n,b)\in\Phi_1\) and \((\sigma,2n+1,b)\) with \((\sigma,n,b)\in\Phi_2\). (3) follows from (1), (2) and Lemma 2.1 (2). \(\blacksquare\)

**Definition.** Sets \(A,B\) are *Turing equivalent* if \(A\le_TB\) and \(B\le_TA\). By Lemma 2.1 this is an equivalence relation. Its classes are the *Turing degrees*; \(\deg(A)\) is the class of \(A\), and \(\mathcal D\) the set of all degrees. Let \(\deg(B)\le\deg(A)\) if \(B\le_TA\); this is well defined and a partial order on \(\mathcal D\).

**Lemma 3.2.**

1. The computable sets form one degree \(\mathbf 0\), and \(\mathbf 0\le\mathbf a\) for every degree \(\mathbf a\).
2. Every two degrees have a least upper bound: \(\deg(A)\vee\deg(B)=\deg(A\oplus B)\).
3. Every degree is a countable set of sets, and below every degree there are at most countably many degrees.

**Proof.** (1) is Lemma 2.1 (3), (2) is Lemma 3.1 (3), and (3) is Lemma 2.1 (4). \(\blacksquare\)

An *automorphism* of the degrees is a bijection \(\pi:\mathcal D\to\mathcal D\) such that \(\mathbf a\le\mathbf b\) exactly if \(\pi(\mathbf a)\le\pi(\mathbf b)\).

**Lemma 3.3.** Let \(\pi\) be an automorphism of the degrees. Then \(\pi^{-1}\) is an automorphism, \(\pi(\mathbf 0)=\mathbf 0\), and \(\pi(\mathbf a\vee\mathbf b)=\pi(\mathbf a)\vee\pi(\mathbf b)\) for all degrees.

**Proof.** The first statement is clear. The degree \(\mathbf 0\) is the least element, and \(\mathbf a\vee\mathbf b\) is the least upper bound; both notions are defined by the order and are preserved by a bijection that preserves the order in both directions. \(\blacksquare\)

## 4. Computing a sequence step by step

Let \(\langle n,m\rangle\) be a computable pairing of natural numbers. For sets \(X_0,X_1,\dots\) let
\[
\bigoplus_nX_n=\{\langle n,m\rangle:\ m\in X_n\}.
\]
If \(\bigoplus_nX_n\le_TT\), then every \(X_n\) is computable from \(T\), and more: one reduction answers all questions about all \(X_n\). The next lemma gives this for a sequence in which every set is computed from its predecessor by one of two fixed reductions, and the choice between the two is read from the predecessor.

**Lemma 4.1.** Let \(\Gamma_0,\Gamma_1\) be reductions, \(j\) a number, \(h\) a bit and \(T\) a set. Let \(X_0,X_1,\dots\) be sets such that \(X_0\le_TT\) and, for every \(n\), with
\[
r_n=\begin{cases}1,&X_n(j)=h,\\0,&X_n(j)\ne h,\end{cases}
\]
the reduction \(\Gamma_{r_n}\) computes \(X_{n+1}\) from \(X_n\oplus T\). Then \(\bigoplus_nX_n\le_TT\), and the set \(\{n:r_n=1\}\) is computable from \(T\).

**Proof.** Let \(\Lambda\) be a reduction that computes \(X_0\) from \(T\). Let \(\Theta\) be the set of the triples \((\sigma,\langle n,m\rangle,b)\) for which there are strings \(\rho_0,\dots,\rho_n\), each longer than \(j\) and the last one longer than \(m\), such that

- for every \(i<|\rho_0|\) there is an initial segment \(\tau\) of \(\sigma\) with \((\tau,i,\rho_0(i))\in\Lambda\);
- for every \(k<n\) and every \(i<|\rho_{k+1}|\) there is an initial segment \(\alpha\) of \(\rho_k\oplus\sigma\) with \((\alpha,i,\rho_{k+1}(i))\in\Gamma_r\), where \(r=1\) if \(\rho_k(j)=h\) and \(r=0\) otherwise;
- \(\rho_n(m)=b\).

The set \(\Theta\) is computably enumerable: a certificate consists of the strings and of certificates for the finitely many memberships in \(\Lambda,\Gamma_0,\Gamma_1\).

*Every triple with \(\sigma\prec T\) is correct.* Let \((\sigma,\langle n,m\rangle,b)\in\Theta\) with \(\sigma\prec T\), and \(\rho_0,\dots,\rho_n\) as in the definition. We show \(\rho_k\prec X_k\) by induction. For \(k=0\): \((\tau,i,\rho_0(i))\in\Lambda\) with \(\tau\prec T\) gives \(X_0(i)=\rho_0(i)\). Let \(\rho_k\prec X_k\). Then \(\rho_k(j)=X_k(j)\), so the \(r\) of the definition is \(r_k\), and \(\rho_k\oplus\sigma\prec X_k\oplus T\). Since \(\Gamma_{r_k}\) computes \(X_{k+1}\) from \(X_k\oplus T\), the triple \((\alpha,i,\rho_{k+1}(i))\) gives \(X_{k+1}(i)=\rho_{k+1}(i)\). So \(b=\rho_n(m)=X_n(m)\).

*Every question has a triple.* Fix \(n\) and \(m\). We choose the strings from the last to the first. Let \(\rho_n\) be the initial segment of \(X_n\) of length \(\max\{j,m\}+1\). If \(\rho_{k+1}\prec X_{k+1}\) is chosen, then for each \(i<|\rho_{k+1}|\) the reduction \(\Gamma_{r_k}\) has a triple for the value \(X_{k+1}(i)\) whose string is an initial segment of \(X_k\oplus T\). These are finitely many strings; let \(\ell_k\) be larger than \(j\) and than all their lengths, and \(\rho_k\) the initial segment of \(X_k\) of length \(\ell_k\). At the end, for each \(i<|\rho_0|\) the reduction \(\Lambda\) has a triple for \(X_0(i)\) whose string is an initial segment of \(T\). Let \(\sigma\) be an initial segment of \(T\) that is longer than these strings and than all \(\ell_k\). Then every string used for the step from \(k\) to \(k+1\) is an initial segment of \(\rho_k\oplus\sigma\), and the triple \((\sigma,\langle n,m\rangle,X_n(m))\) lies in \(\Theta\).

So \(\Theta\) computes \(\bigoplus_nX_n\) from \(T\). The triples \((\sigma,n,1)\) with \((\sigma,\langle n,j\rangle,h)\in\Theta\) and \((\sigma,n,0)\) with \((\sigma,\langle n,j\rangle,1-h)\in\Theta\) form a reduction that computes \(\{n:r_n=1\}\) from \(T\). \(\blacksquare\)

## 5. Real numbers

Fix a list \(q_0,q_1,q_2,\dots\) of all rational numbers, without repetitions, such that the order and the arithmetic of the rationals are computable in terms of the indices. For a real number \(x\) let
\[
\begin{gathered}
C(x)=\{i:\ q_i<x\},\\
d(x)=\deg(C(x)).
\end{gathered}
\]
The set \(C(x)\) is the *cut* of \(x\). Statements about the computability of real numbers are statements about their cuts.

**Lemma 5.1.**

1. The map \(C:\mathbb R\to2^{\mathbb N}\) is one-to-one.
2. Let \(c_0,\dots,c_k\) be rational numbers, \(k\ge1\), and \(x_1,\dots,x_k\) real numbers. Then
\[
\begin{aligned}
&d\Bigl(c_0+\sum_{i=1}^kc_ix_i\Bigr)\\
&\quad\le d(x_1)\vee\dots\vee d(x_k).
\end{aligned}
\]
3. For every set \(B\) that is not computable there is an irrational number \(t\) with \(0<t<1\) and \(d(t)=\deg(B)\).

**Proof.** (1) Between two different real numbers there is a rational number.

(2) Let \(z=c_0+\sum c_ix_i\). If \(z\) is rational, \(C(z)\) is a computable set, and the claim holds by Lemma 2.1 (3). Let \(z\) be irrational. A string \(\gamma\), read as a join of \(k\) strings \(\gamma_1,\dots,\gamma_k\), *shows the brackets* \(q_{l_i}<x_i\le q_{u_i}\), \(1\le i\le k\), if \(\gamma_i(l_i)=1\) and \(\gamma_i(u_i)=0\). For such brackets let \(z^-\) and \(z^+\) be the smallest and the largest value of \(c_0+\sum c_iy_i\) for \(y_i\in[q_{l_i},q_{u_i}]\); these are rational numbers, computed from the indices. Let \(\Phi\) be the set of the triples \((\gamma,n,1)\) such that \(\gamma\) shows brackets with \(z^->q_n\), and \((\gamma,n,0)\) such that \(\gamma\) shows brackets with \(z^+<q_n\). It is a computable set of triples. If \(\gamma\) is an initial segment of \(C(x_1)\oplus\dots\oplus C(x_k)\), the brackets hold, so \(z^-\le z\le z^+\), and the triples are correct. Since \(z\ne q_n\), and \(z^-\), \(z^+\) are as close to \(z\) as we like for narrow brackets, every \(n\) has a triple. So \(\Phi\) computes \(C(z)\) from the join.

(3) Let \(t=\sum_nB(n)2^{-n-1}\). If \(t\) were rational, its binary expansions would be periodic from some place on, hence computable; \(B\) is one of them. So \(t\) is irrational, and \(0<t<1\). For a string \(\beta\) let \(s_\beta=\sum_{n<|\beta|}\beta(n)2^{-n-1}\); then \(\beta\prec B\) exactly if \(s_\beta<t<s_\beta+2^{-|\beta|}\), because \(t\) is not a dyadic rational. The triples \((\beta,n,1)\) with \(s_\beta>q_n\) and \((\beta,n,0)\) with \(s_\beta+2^{-|\beta|}<q_n\) compute \(C(t)\) from \(B\). The triples \((\tau,n,\beta(n))\), where \(\beta\) is a string of length \(n+1\) and \(\tau\) is a string with \(\tau(i)=1\) for the index \(i\) of \(s_\beta\) and \(\tau(i')=0\) for the index \(i'\) of \(s_\beta+2^{-n-1}\), compute \(B\) from \(C(t)\). \(\blacksquare\)

In (2) the reduction depends on the numbers \(c_i\), and the proof distinguishes whether \(z\) is rational. No procedure is claimed that decides this.

## 6. Exercises

**6.1.** Let \(\Phi\) be the set of all triples \((\sigma,n,b)\). From which sets \(A\) does \(\Phi\) compute a set?

**6.2.** Show that \(A\oplus B\) and \(B\oplus A\) are Turing equivalent, and that \(A\oplus A\) is Turing equivalent to \(A\).

**6.3.** Let \(A\) be a set and \(A'\) a set that differs from \(A\) in finitely many places. Show \(A'\le_TA\).

**6.4.** Show that there are uncountably many Turing degrees.

**6.5.** Let \(x\) be a real number and \(c\ne0\) rational. Show \(d(cx)=d(x)\), and \(d(x+y)\vee d(x)=d(x)\vee d(y)\) for all real \(x,y\).

**6.6.** In Lemma 5.1 (3), where is it used that \(B\) is not computable?

## 7. Solutions

**6.1.** From none: for \(\sigma\prec A\) both \((\sigma,0,0)\) and \((\sigma,0,1)\) lie in \(\Phi\), so no set \(B\) satisfies the condition for \(n=0\).

**6.2.** The triples \((\gamma,2n,\gamma(2n+1))\) and \((\gamma,2n+1,\gamma(2n))\), for \(\gamma\) long enough, compute \(B\oplus A\) from \(A\oplus B\). By Lemma 3.1, \(A\le_TA\oplus A\), and \(A\oplus A\le_TA\) because \(A\le_TA\) twice.

**6.3.** Let \(F\) be the finite set of the places where they differ. The triples \((\sigma,n,\sigma(n))\) for \(n\notin F\) and \((\sigma,n,1-\sigma(n))\) for \(n\in F\), with \(n<|\sigma|\), form a computable set.

**6.4.** There are uncountably many sets, and every degree is a countable set of sets (Lemma 3.2).

**6.5.** By Lemma 5.1 (2), \(d(cx)\le d(x)\) and \(d(x)=d(c^{-1}\cdot cx)\le d(cx)\). Also \(d(x+y)\le d(x)\vee d(y)\), and \(d(y)\le d(x+y)\vee d(x)\) because \(y=(x+y)-x\).

**6.6.** In the proof that \(t\) is irrational. For a computable \(B\) the number \(t\) can be rational, for example \(t=0\) for the empty set; and then \(\beta\prec B\) is not equivalent to the strict inequalities.

## References

- [OpenAI-R] OpenAI, *Rigidity of the Turing degrees*, OpenAI Math Release preprint, 24 September 2026, Section 2. https://github.com/openai/math/tree/main/preprints/Rigidity-of-the-Turing-degrees-September-24-2026
- [OLP] Open Logic Project, *The Open Logic Text*, part Computability, chapter Computability Theory. https://openlogicproject.org
