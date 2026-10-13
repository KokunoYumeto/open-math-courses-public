# Recovery from four values

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Let \(F\) assign to every real number a set of natural numbers. Suppose that \(F\) is a Borel function, that it takes every value at most countably often, and that the value at a sum is computable from the values at the summands. No relation between a real number \(x\) and the set \(F(x)\) is assumed: \(F(x)\) need not compute the cut of \(x\). This lesson proves that nevertheless an irrational number \(t\) can be computed from four values of \(F\), at arguments that are formed from \(t\) and two auxiliary real numbers \(u,v\), for all pairs \((u,v)\) outside a meager set.

The proof builds a walk on the line. Each step adds \(\delta t\) or \(\delta(t-1)\); which of the two is decided by one bit of the value of \(F\) at the present position, in such a way that the walk stays in a bounded interval. Then the proportion of steps of the second kind tends to \(t\). The assumption on sums makes the values of \(F\) along the walk computable from the four given values.

- The statement (Theorem 1.1).
- Two reductions that work near a pair \((u,v)\) (Lemma 2.1).
- The bounded walk (Lemma 3.1).
- The walk is computable from the four values, and \(t\) from the walk (Section 4).

The lesson follows [OpenAI-R, Section 4]. It uses the reductions, the iteration lemma and the cuts of Relative computability and the Turing degrees, and the category lemmas of [Category and computability](category-and-computability.md).

## 1. The statement

A function \(F:\mathbb R\to2^{\mathbb N}\) has *countable fibres* if for every set \(Z\) there are at most countably many \(x\) with \(F(x)=Z\).

**Theorem 1.1.** Let \(F:\mathbb R\to2^{\mathbb N}\) be a Borel function with countable fibres such that for all real \(x,y\)
\[
F(x+y)\le_TF(x)\oplus F(y).
\]
Let \(t\) be an irrational number with \(0<t<1\). Then there is a comeager set \(G_t\subset\mathbb R^2\) such that for every \((u,v)\in G_t\) there is a rational number \(\delta\) with \(0<\delta<1\) and
\[
\begin{aligned}
C(t)\le_T{}&F(u)\oplus F(u-v)\\
&\oplus F(v-u+\delta t)\\
&\oplus F(v-u+\delta(t-1)).
\end{aligned}
\]

The reduction and the number \(\delta\) depend on \(t\), \(u\) and \(v\). The theorem does not say that they can be found from these numbers by a procedure.

**The two additions.** For real numbers \(s\) and \(a\),
\[
\begin{aligned}
(u+s)+(v-u+a)&=v+s+a,\\
(v+s+a)+(u-v)&=u+s+a .
\end{aligned}
\]
So the value \(F(u+s+a)\) is computable from \(F(u+s)\), \(F(v-u+a)\) and \(F(u-v)\), in two steps. In the walk, \(s\) is the present position and \(a\) the next step. The walk uses only two different steps \(a\); so besides the starting value \(F(u)\) it needs the three values \(F(u-v)\), \(F(v-u+\delta t)\), \(F(v-u+\delta(t-1))\). The difficulty is that the reductions for the two additions depend on the arguments. The category lemmas make them independent of the position, for positions in a countable set near \(0\).

## 2. Two reductions near a pair

Let \(F\) and \(t\) be as in Theorem 1.1, and \(e(x,y)\) the least index of a reduction that computes \(F(x+y)\) from \(F(x)\oplus F(y)\). By Lemma 3.2 of the lesson on category, \(e\) is a Borel function on \(\mathbb R^2\). By Lemma 2.2 of that lesson there are comeager sets \(D\subset\mathbb R\) and \(E\subset\mathbb R^2\) such that the restrictions of \(F\) to \(D\) and of \(e\) to \(E\) are continuous.

Let \(H=\mathbb Q+\mathbb Qt\), the countable set of the numbers \(c+c't\) with rational \(c,c'\); it is closed under sums. Let \(G_t\) be the set of the pairs \((u,v)\) such that for all \(s,a\in H\)
\[
\begin{gathered}
u+s\in D,\\
(u+s,\ v-u+a)\in E,\\
(v+s,\ u-v)\in E .
\end{gathered}
\]

**Lemma 2.1.**

1. The set \(G_t\) is comeager in \(\mathbb R^2\).
2. For every \((u,v)\in G_t\) there are indices \(p,q\) and a number \(0<\rho<1\) such that
   - for all \(s,a\in H\) with \(|s|<\rho\), \(|a|<\rho\), the reduction \(\Phi_p\) computes \(F(v+s+a)\) from \(F(u+s)\oplus F(v-u+a)\);
   - for all \(s\in H\) with \(|s|<\rho\), the reduction \(\Phi_q\) computes \(F(u+s)\) from \(F(v+s)\oplus F(u-v)\).

**Proof.** (1) Fix \(s,a\in H\). The set of the pairs with \(u+s\in D\) is \((D-s)\times\mathbb R\); its complement is meager by Lemma 1.2 of the lesson on category. The maps \((u,v)\mapsto(u+s,v-u+a)\) and \((u,v)\mapsto(v+s,u-v)\) are homeomorphisms of the plane onto itself, so the preimages of \(E\) under them are comeager. \(G_t\) is the intersection of these countably many comeager sets.

(2) The pairs \((u,v-u)\) and \((v,u-v)\) lie in \(E\): take \(s=a=0\). Let \(p=e(u,v-u)\) and \(q=e(v,u-v)\). Since \(e\) is continuous on \(E\) with values in a discrete space, there is \(0<\rho<1\) such that \(e(x,y)=p\) for all \((x,y)\in E\) with \(|x-u|<\rho\), \(|y-(v-u)|<\rho\), and \(e(x,y)=q\) for all \((x,y)\in E\) with \(|x-v|<\rho\), \(|y-(u-v)|<\rho\). For \(s,a\in H\) the pairs \((u+s,v-u+a)\) and \((v+s,u-v)\) lie in \(E\) by the definition of \(G_t\). So \(e(u+s,v-u+a)=p\) for \(|s|,|a|<\rho\), and \(e(v+s,u-v)=q\) for \(|s|<\rho\). By the definition of \(e\) and the two additions this is the claim; in the second statement the sum is \((v+s)+(u-v)=u+s\). \(\blacksquare\)

## 3. The bounded walk

Fix \((u,v)\in G_t\) and \(p,q,\rho\) as in Lemma 2.1.

**The ends.** The set \(D\) is comeager, so it is dense (Theorem 1.1 of the lesson on category): there is \(b_-\) with \(-\rho<b_-<0\) and \(u+b_-\in D\). The set of the \(b\in(0,\rho)\) with \(u+b\in D\) is uncountable (Lemma 1.2 of that lesson), and only countably many \(x\) have \(F(x)=F(u+b_-)\). So there is \(b_+\) with \(0<b_+<\rho\), \(u+b_+\in D\) and \(F(u+b_+)\ne F(u+b_-)\). Let \(j\) be a number with \(F(u+b_+)(j)\ne F(u+b_-)(j)\), and \(h=F(u+b_+)(j)\).

**The step size.** \(F\) is continuous on \(D\). So there is a rational number \(\delta\) with \(0<\delta<\rho\) such that for all \(y\in D\): \(F(y)(j)\ne h\) if \(y\) lies in the interval \([u+b_-,\,u+b_-+\delta]\), and \(F(y)(j)=h\) if \(y\) lies in the interval \([u+b_+-\delta,\,u+b_+]\).
For \(s\in H\) the point \(u+s\) lies in \(D\). So the bit \(F(u+s)(j)\) is different from \(h\) for the \(s\in H\) in \([b_-,b_-+\delta]\), and equal to \(h\) for the \(s\in H\) in \([b_+-\delta,b_+]\).

**The walk.** Let \(s_0=0\) and, for \(n\ge0\),
\[
\begin{aligned}
r_n&=\begin{cases}1,&F(u+s_n)(j)=h,\\0,&F(u+s_n)(j)\ne h,\end{cases}\\
s_{n+1}&=s_n+\delta\,(t-r_n).
\end{aligned}
\]
So the walk goes up by \(\delta t\) when the bit is different from \(h\), and down by \(\delta(1-t)\) when it is equal to \(h\).

**Lemma 3.1.** For all \(n\): \(s_n\in H\), \(b_-\le s_n\le b_+\), and
\[
s_n=\delta\Bigl(nt-\sum_{k<n}r_k\Bigr).
\]

**Proof.** The formula follows from the definition by summation, and \(s_n\in H\) because \(\delta\) is rational. The bounds hold for \(s_0=0\). Let them hold for \(s_n\). If \(r_n=0\), the bit at \(s_n\) is different from \(h\), so \(s_n\) is not in \([b_+-\delta,b_+]\): \(s_n<b_+-\delta\). The step is \(\delta t\), with \(0<\delta t<\delta\), so \(b_-\le s_n<s_{n+1}<b_+\). If \(r_n=1\), the bit is equal to \(h\), so \(s_n\) is not in \([b_-,b_-+\delta]\): \(s_n>b_-+\delta\). The step is \(-\delta(1-t)\), with \(0<\delta(1-t)<\delta\), so \(b_-<s_{n+1}<s_n\le b_+\). \(\blacksquare\)

Only the behaviour of the bit near the two ends was used: near each end it sends the walk inwards. Between the ends the bit may behave in any way.

Since \(|s_n|<\rho<1\), the lemma gives for \(N\ge1\)
\[
\Bigl|\,t-\frac1N\sum_{k<N}r_k\Bigr|=\frac{|s_N|}{N\delta}<\frac1{N\delta}.
\]

## 4. Proof of Theorem 1.1

Let
\[
\begin{gathered}
T_1=F(u),\qquad T_2=F(u-v),\\
T_3=F(v-u+\delta t),\\
T_4=F(v-u+\delta(t-1)),
\end{gathered}
\]
\(T=T_1\oplus T_2\oplus T_3\oplus T_4\), and \(X_n=F(u+s_n)\).

*One step.* Let \(a_n=\delta(t-r_n)\); it lies in \(H\), and \(|a_n|<\delta<\rho\). The value \(F(v-u+a_n)\) is \(T_3\) if \(r_n=0\) and \(T_4\) if \(r_n=1\). By Lemma 3.1, \(|s_n|<\rho\) and \(|s_{n+1}|<\rho\). So by Lemma 2.1, with \(V_n=F(v+s_{n+1})\):

- \(\Phi_p\) computes \(V_n\) from \(X_n\oplus T_{3+r_n}\), because \(v+s_n+a_n=v+s_{n+1}\);
- \(\Phi_q\) computes \(X_{n+1}\) from \(V_n\oplus T_2\).

*Two reductions for all steps.* For \(r\in\{0,1\}\) there is a reduction \(\Gamma_r\) with the following property: for all sets \(X,X',V,T_1,\dots,T_4\) such that \(\Phi_p\) computes \(V\) from \(X\oplus T_{3+r}\) and \(\Phi_q\) computes \(X'\) from \(V\oplus T_2\), the reduction \(\Gamma_r\) computes \(X'\) from \(X\oplus T\). It is composed, by Lemma 2.1 (2) and Lemma 3.1 of the lesson on relative computability, of the reductions that compute \(X\), \(T_2\) and \(T_{3+r}\) from \(X\oplus T\), of \(\Phi_p\), and of \(\Phi_q\). It depends only on \(p\), \(q\) and \(r\). By the first part, \(\Gamma_{r_n}\) computes \(X_{n+1}\) from \(X_n\oplus T\) for every \(n\).

*The walk is computable from \(T\).* \(X_0=F(u)=T_1\le_TT\). So Lemma 4.1 of the lesson on relative computability applies to \(\Gamma_0,\Gamma_1\), \(j\), \(h\), \(T\) and the sets \(X_n\): the set \(R=\{n:r_n=1\}\) is computable from \(T\).

*\(t\) is computable from the walk.* For a string \(\beta\) and \(1\le N\le|\beta|\) let \(A_N(\beta)\) be the number of the \(k<N\) with \(\beta(k)=1\), divided by \(N\). Let \(\Omega\) be the set of the triples \((\beta,i,1)\) such that \(q_i<A_N(\beta)-\tfrac1{N\delta}\) for some \(N\le|\beta|\), and \((\beta,i,0)\) such that \(q_i>A_N(\beta)+\tfrac1{N\delta}\) for some \(N\le|\beta|\). This is a computable set of triples. For \(\beta\prec R\), \(A_N(\beta)\) is the mean of \(r_0,\dots,r_{N-1}\), which differs from \(t\) by less than \(\tfrac1{N\delta}\); so the triples are correct. Since \(t\ne q_i\), and the means tend to \(t\), every \(i\) has a triple. So \(\Omega\) computes \(C(t)\) from \(R\), and \(C(t)\le_TR\le_TT\). \(\blacksquare\)

The reduction that was found uses the numbers \(p,q,j,h\) and \(\delta\) and the four sets. It does not use the positions \(s_n\), the numbers \(b_-,b_+,\rho\), or the cuts of \(t,u,v\).

## 5. Exercises

**5.1.** Let \(c\ne0\) be a real number and \(F(x)=C(cx)\). Check the assumptions of Theorem 1.1, and prove its conclusion for this \(F\) directly, for all \(u,v\) and every rational \(\delta\ne0\).

**5.2.** Let \(t=\tfrac1{\sqrt2}\) and \(\delta=\tfrac1{10}\), and suppose that the bit \(F(u+s)(j)\) is equal to \(h\) exactly for \(s>0.01\). Compute \(r_0,\dots,r_5\) and \(s_6\).

**5.3.** Where does the proof use that \(F\) has countable fibres? Give a Borel function \(F\) with \(F(x+y)\le_TF(x)\oplus F(y)\) for which the conclusion fails.

**5.4.** Why is the set \(H\) taken to be \(\mathbb Q+\mathbb Qt\) and not \(\mathbb R\)?

**5.5.** In the last step, why is the bound \(\tfrac1{N\delta}\) needed, and not only the convergence of the means to \(t\)?

## 6. Solutions

**5.1.** \(F\) is one-to-one, it is Borel because each bit of \(C(cx)\) is the indicator of a half-line, and \(c(x+y)=cx+cy\) gives the reduction by Lemma 5.1 (2) of the lesson on relative computability. Let \(T\) be the join of the four values. The numbers \(c(v-u+\delta t)-c(v-u+\delta(t-1))=c\delta\) and \(c(u-v)+c(v-u+\delta t)=c\delta t\) have cuts computable from \(T\), by the same lemma. Then \(t=c\delta t/(c\delta)\); the cut of a quotient of two real numbers is computable from their cuts, by brackets as in that lemma. So \(C(t)\le_TT\).

**5.2.** \(\delta t\approx0.0707\) and \(\delta(1-t)\approx0.0293\). \(s_0=0\): \(r_0=0\), \(s_1\approx0.0707\); \(r_1=1\), \(s_2\approx0.0414\); \(r_2=1\), \(s_3\approx0.0121\); \(r_3=1\), \(s_4\approx-0.0172\); \(r_4=0\), \(s_5\approx0.0536\); \(r_5=1\), \(s_6\approx0.0243\). Check: \(s_6=\delta(6t-4)\), which is \(0.6\cdot0.7071-0.4\approx0.0243\).

**5.3.** In the choice of \(b_+\): two points \(u+b_-\), \(u+b_+\) of \(D\) with different values of \(F\) are needed, to get a bit that separates the two ends. For a constant \(F\) the assumption on sums holds and the conclusion fails for every \(t\) whose cut is not computable from the constant value.

**5.4.** The pair \((u,v)\) must satisfy one condition for every position and every step that can occur, and a countable intersection of comeager sets is comeager; an intersection over all real shifts need not be. The positions of the walk are sums of multiples of \(\delta t\) and \(\delta(t-1)\) with rational \(\delta\), so they lie in \(\mathbb Q+\mathbb Qt\).

**5.5.** A reduction must certify each answer by a finite initial segment of \(R\). To decide \(q_i<t\) from finitely many of the \(r_k\) one needs to know how far the mean of the first \(N\) of them can be from \(t\).

## References

- [OpenAI-R] OpenAI, *Rigidity of the Turing degrees*, OpenAI Math Release preprint, 24 September 2026, Section 4. https://github.com/openai/math/tree/main/preprints/Rigidity-of-the-Turing-degrees-September-24-2026
