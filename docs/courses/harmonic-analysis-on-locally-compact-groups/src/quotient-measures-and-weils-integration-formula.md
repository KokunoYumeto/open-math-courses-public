# Quotient measures and Weil's integration formula

*Originally written and self-checked by GPT-6 Astra (OpenAI), Ultra reasoning effort, October 2026. Reconciled, extended and self-checked by GPT-6.1 Sol (OpenAI), Ultra, October 2026. Bounded internal AI reviews checked the reconstructed proof passages and prerequisite routes. Original text: public domain (CC0). Lemma 2.1 and Theorem 3.1 follow arguments of D. H. Fremlin, cited where they occur. The programme's CC0 sources are credited at the end.*

Integration over a group can often be separated into integration along a subgroup and integration over its cosets. For a nonabelian group, an invariant measure on the coset space need not exist. The precise obstruction is the mismatch between two modular functions:
\[
G/H\text{ has a nonzero invariant Radon measure}
\quad\Longleftrightarrow\quad
\Delta_G|_H=\Delta_H.
\]
When the obstruction does not vanish, a positive continuous density still gives a strongly quasi-invariant measure. We construct it, prove its change-of-variables formula and calculate examples where the distinction matters.

The lesson works for every locally compact Hausdorff group \(G\) and every closed subgroup \(H\). Neither is assumed second countable, \(\sigma\)-compact or unimodular. All interchanges of integrals in the main construction involve continuous functions with compact support. We will not infer a Fubini theorem for arbitrary nonnegative Borel functions on a non-\(\sigma\)-finite product.

## What to know first

The preceding programme lesson [Haar measure on locally compact groups](haar-measure-on-locally-compact-groups.md) supplies the following exact results:

- Theorem 2.2: a positive linear functional on \(C_c(X)\) is represented by a unique Radon measure.
- Proposition 3.1(2): multiplication by a strictly positive continuous function gives a Radon measure in the same measure class.
- Proposition 4.2: iterated integrals of a continuous compactly supported function on a product agree.
- Proposition 9.1 and Theorem 9.2: positivity on nonempty open sets and uniqueness of Haar measure.
- Theorems 10.1 and 11.1: the modular function and the inversion formula.

Their elementary measure-theory prerequisites are proved in the preceding tools lesson. The topology needed specifically for the quotient construction is proved below, including the cutoff argument sometimes hidden behind a reference to a partition of unity.

Fix left Haar measures \(dg\) and \(dh\). Our convention is
\[
\int_G f(ga)\,dg=\Delta_G(a)^{-1}\int_G f(g)\,dg.
\tag{1}
\]
Equivalently, the measure of a right translate \(Ea\) is \(\Delta_G(a)\) times the measure of \(E\). The same convention defines \(\Delta_H\). Put \(Y=G/H\), the space of cosets \(gH\), and \(q(g)=gH\).

As in the preceding lesson, a Radon measure here is a Borel measure finite on compact sets, outer regular on Borel sets and inner regular on open sets. Equality of Radon measures can therefore be checked on \(C_c\). Left and right translations of functions mean \(L_af(g)=f(a^{-1}g)\) and \(R_af(g)=f(ga)\).

## Local topology and compactly supported functions

**Lemma 1.1.** An LCH space has a base of relatively compact open neighborhoods. If \(K\subset V\), where \(K\) is compact and \(V\) is open, there is \(u\in C_c(X)\) with \(0\leq u\leq1\), \(u=1\) on \(K\), and \(\operatorname{supp}u\subset V\).

*Proof.* We first recall the separation argument for a compact Hausdorff space \(C\). For a point \(x\) and a closed set \(A\) not containing it, separate \(x\) from each point of \(A\) by disjoint open neighborhoods. A finite subcover of \(A\) gives an open neighborhood \(W\) of \(x\) whose closure misses \(A\). For two disjoint closed sets, do this for each point of the first, then take a finite union of the resulting neighborhoods. Thus whenever \(A\subset O\), with \(A\) closed and \(O\) open, there is open \(W\) with
\[
A\subset W\subset\overline W\subset O.
\tag{2}
\]

This proves the continuous separation needed here. For disjoint closed \(A,B\subset C\), choose open sets \(U_r\), indexed by dyadic rationals \(r\in[0,1]\), with \(A\subset U_0\), \(U_1=C\setminus B\), and \(\overline U_r\subset U_s\) when \(r<s\). Start by shrinking \(A\) inside \(C\setminus B\); at each finite dyadic stage use (2) to insert the new intermediate open sets. Set
\[
v(x)=\inf\{r:x\in U_r\},
\]
with value \(1\) when the set is empty. Then \(v=0\) on \(A\) and \(v=1\) on \(B\). The identity
\(\{v<t\}=\bigcup_{r<t}U_r\) and, for \(0\leq t<1\),
\(\{v>t\}=\bigcup_{r>t}(C\setminus\overline U_r)\)
prove continuity. In the second identity, choose a dyadic \(r\) strictly between \(t\) and \(v(x)\); if \(x\in\overline U_r\), the nesting would put \(x\) in every \(U_s\) with \(s>r\), contradicting \(v(x)>r\).

Now let \(x\in O\subset X\), with \(O\) open and \(X\) LCH. Choose a compact neighborhood \(C\) of \(x\). Apply (2) within \(C\) to \(x\) and \(O\cap\operatorname{int}C\). The resulting neighborhood lies in \(\operatorname{int}C\), so it is open in \(X\), and its closure is compact and lies in \(O\). This proves the neighborhood-base assertion.

For compact \(K\subset V\), take finitely many such neighborhoods to obtain open \(W\) with \(K\subset W\subset\overline W\subset V\) and \(\overline W\) compact. In \(\overline W\), continuously separate \(K\) and \(\overline W\setminus W\), taking the value \(1\) on the first and \(0\) on the second. Extend the function by zero outside \(W\). The two definitions agree on the boundary, so the pasting lemma on the two closed sets \(\overline W\) and \(X\setminus W\) proves continuity. This is the required \(u\). \(\square\)

**Lemma 1.2.** The quotient map \(q\) is open, \(Y\) is LCH, and every compact subset \(E\subset Y\) is the image of a compact subset of \(G\).

*Proof.* For open \(O\subset G\), \(q^{-1}(q(O))=OH\) is open, so \(q(O)\) is open. If \(xH\neq yH\), then \(y^{-1}x\notin H\). Since \(H\) is closed, continuity gives neighborhoods \(V\) of \(x\) and \(W\) of \(y\) with \(W^{-1}V\cap H=\varnothing\). Their images under \(q\) are disjoint open neighborhoods. Thus \(Y\) is Hausdorff. The image of a compact neighborhood of \(g\) contains the image of its interior, an open neighborhood of \(gH\), so \(Y\) is locally compact.

For the compact-lift assertion, use the positive averaging construction of Lemma 2.1 below, which uses only the openness and LCH conclusions just proved. Choose \(b\geq0\) with \(Pb=1\) on \(E\). Then
\[
K=\operatorname{supp}b\cap q^{-1}(E)
\]
is compact, since \(E\) is closed in the Hausdorff quotient. Each \(y\in E\) has \(Pb(y)=1>0\), so its fiber contains a point where \(b>0\), and consequently \(q(K)=E\). This proves the last assertion without assuming a continuous section or using compact lifting to construct \(b\). \(\square\)

## Averaging along the subgroup

Why not simply push Haar measure forward through \(q\)? Consider \(G=\mathbb R^2\), with two-dimensional Lebesgue measure, and \(H=\mathbb R\times\{0\}\), so that \(q(x,y)=y\). The inverse image of a nondegenerate compact interval \([a,b]\) contains every rectangle \([-N,N]\times[a,b]\). Its measure is at least \(2N(b-a)\) for every \(N\), hence is infinite. The pushforward is therefore not finite on compact intervals and is not the required Radon measure. Nevertheless, the quotient plainly has the invariant measure \(dy\).

The construction below separates these two operations. First integrate a compactly supported function along the fiber, rather than measuring the whole infinite fiber. Then integrate the resulting function over the base. For the example, this is precisely \(\int f(x,y)\,dx\) followed by integration in \(y\). A function constant on every fiber is usually not compactly supported upstairs; the cutoff used below supplies a compactly supported representative without pretending that the fiber has finite mass. This is why surjectivity of the averaging map, rather than existence of a global section or finiteness of subgroup volume, is the useful starting point.

For \(f\in C_c(G)\), define
\[
Pf(gH)=\int_H f(gh)\,dh.
\tag{3}
\]
Left invariance of \(dh\) makes this independent of the representative \(g\): replacing \(g\) by \(gr\), \(r\in H\), replaces \(h\) by \(rh\).

**Lemma 2.1.** The map \(P:C_c(G)\to C_c(Y)\) is positive and surjective. For each compact \(E\subset Y\), there is \(b\in C_c(G)\), \(b\geq0\), with \(Pb=1\) on \(E\). A nonnegative function in \(C_c(Y)\) has a nonnegative lift through \(P\).

*Proof.* Positivity is immediate. For \(g\) in a compact neighborhood \(A\) of \(g_0\), only
\[
h\in H\cap A^{-1}\operatorname{supp}f
\]
can contribute to (3). This set is compact. The continuous function \((g,h)\mapsto f(gh)\) varies uniformly in \(h\) on this compact set as \(g\to g_0\): a finite cover of that set by continuity neighborhoods proves the assertion. Its integral therefore varies continuously. The resulting continuous function on \(G\) is constant on fibers, so descends continuously through the quotient map. Its support lies in \(q(\operatorname{supp}f)\), a compact set.

The remaining construction follows the freely accessible positivity-set argument of [Fremlin, §443P(v–vi)](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt443.tex). For every \(y\in Y\), select \(g\) with \(q(g)=y\), and choose \(a_y\in C_c(G)\), nonnegative, with \(a_y(g)>0\), by Lemma 1.1. Continuity gives a nonempty open set of \(h\in H\) on which \(a_y(gh)>0\). Haar positivity implies \(Pa_y(y)>0\). Thus the open sets \(\{Pa_y>0\}\) cover \(Y\).

For a compact \(E\), finitely many of these sets cover it. Sum the corresponding \(a_y\) to obtain \(a\geq0\) in \(C_c(G)\) with \(Pa>0\) on \(E\). Put \(W=\{Pa>0\}\). Choose \(\chi\in C_c(Y)\) equal to one on \(E\), with \(0\leq\chi\leq1\) and support contained in \(W\). The function \(r=\chi/Pa\) on \(W\), extended by zero elsewhere, is continuous: its numerator has compact support contained in \(W\), and is zero near each point outside that support. Define
\[
b(g)=a(g)r(q(g)).
\tag{4}
\]
It is nonnegative, continuous, compactly supported and satisfies \(Pb=rPa=\chi\), so \(Pb=1\) on \(E\). For arbitrary \(F\in C_c(Y)\), take such \(b\) for \(E=\operatorname{supp}F\). Then \(f(g)=F(q(g))b(g)\) belongs to \(C_c(G)\), and \(Pf=F\). If \(F\geq0\), its lift is nonnegative. This proves all the asserted surjectivity and normalization statements. \(\square\)

*Source of the preceding positivity-set construction:* it follows Fremlin’s §443P(v–vi), cited above, and its expansion is by GPT-6.1 Sol (OpenAI), Ultra, 5 October 2026; the proof of continuity above is the course’s own.

The map respects left translation and has a simple right-subgroup rule:
\[
P(L_a f)(y)=Pf(a^{-1}y),\qquad
P(R_h f)=\Delta_H(h)^{-1}Pf\quad(h\in H).
\tag{5}
\]
Both follow directly from (3), with the modular convention (1).

## Exactly when the quotient measure is invariant

**Theorem 3.1.** The space \(G/H\) has a nonzero \(G\)-invariant Radon measure if and only if \(\Delta_G(h)=\Delta_H(h)\) for every \(h\in H\). When this holds, it is unique up to a positive scalar. For the fixed measures \(dg,dh\), there is exactly one normalization \(d\mu\) for which
\[
\int_G f(g)\,dg=\int_Y Pf(y)\,d\mu(y)
\qquad(f\in C_c(G)).
\tag{6}
\]

*Proof (from the free functional construction in Fremlin, §§443Q(b), 443R).* We first establish the sufficiency direction as an order statement. Suppose \(\Delta_G|_H=\Delta_H\), and let a real \(u\in C_c(G)\) satisfy \(Pu\geq0\). By Lemma 2.1 choose a nonnegative \(v\in C_c(G)\) with \(Pv=1\) on \(q(\operatorname{supp}u)\). Both \((x,h)\mapsto v(x)u(xh)\) and its changed-variable integrand below have compact support: the two group coordinates lie in the compact supports of \(v,u\), so the subgroup coordinate lies in their compact relative-product intersection with \(H\). The compact-product theorem therefore permits each exchange. Right translation on \(G\), the modular equality, and inversion on \(H\) give
\[
\begin{aligned}
0&\leq\int_G v(x)Pu(xH)\,dx\\
 &=\int_H\int_G v(x)u(xh)\,dx\,dh\\
 &=\int_G u(t)\int_H\Delta_G(h)^{-1}v(th^{-1})\,dh\,dt\\
 &=\int_G u(t)Pv(tH)\,dt
 =\int_G u(t)\,dt.
\end{aligned}
\tag{7}
\]
Applying the conclusion to \(u\) and \(-u\) shows that \(Pu=0\) forces \(\int u=0\). Apply it to real and imaginary parts for a complex \(u\). Thus the rule
\[
\Lambda(Pu)=\int_G u\,dg
\]
defines a linear functional on \(C_c(Y)\), independent of the selected lift. It is positive by the order statement, and its domain is all of \(C_c(Y)\) by surjectivity. It is nonzero because a positive nonzero compactly supported group function has positive Haar integral. Riesz representation gives a nonzero Radon measure \(\mu\) representing \(\Lambda\). The intertwining identity (5) and left Haar invariance imply \(\Lambda(F(a^{-1}\cdot))=\Lambda(F)\); Riesz uniqueness makes \(\mu\) invariant. Its defining identity is (6).

Conversely suppose \(\eta\) is a nonzero invariant Radon measure on \(Y\). Compose integration against \(\eta\) with \(P\):
\[
J(u)=\int_Y Pu\,d\eta.
\]
This functional is positive, nonzero by positive surjectivity and Radon representation, and left invariant by (5). Its representing measure is therefore a left Haar measure on \(G\). Haar uniqueness gives \(J(u)=c\int_Gu\,dg\), with \(c>0\). For \(h\in H\), equation (5) evaluates \(J(R_hu)\) as \(\Delta_H(h)^{-1}J(u)\), whereas the representing Haar measure evaluates it as \(\Delta_G(h)^{-1}J(u)\). For a nonnegative nonzero \(u\), \(J(u)>0\). The factors must agree, proving necessity.

Finally the same composition gives a scalar multiple of Haar integration for every invariant quotient measure. Surjectivity of \(P\) makes its quotient measure a scalar multiple of the one constructed above, and (6) selects precisely one scalar. \(\square\)

*Source of this proof:* D. H. Fremlin’s freely accessible [§§443Q(b), 443R](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt443.tex), written for this course by GPT-6.1 Sol (OpenAI), Ultra, 5 October 2026. Differences from Fremlin’s treatment: the course’s outer-regular Borel convention, complex functions by real and imaginary parts, explicit compact support for every exchange, and a cutoff on \(q(\operatorname{supp}u)\) even when the subgroup average cancels. The conclusion uses only the Riesz, compact-product and Haar results proved earlier in the course.

Two useful consequences require no additional construction. A compact subgroup always satisfies the criterion: its modular function is one, and the continuous homomorphism \(\Delta_G:H\to(0,\infty)\) is one on a compact group. An open subgroup also satisfies it, because restriction of Haar measure on \(G\) to \(H\) is Haar measure and has the same right-translation factors. For a discrete subgroup, however, the criterion is \(\Delta_G|_H=1\), not an automatic assertion that every discrete-subgroup quotient has an invariant measure.

A compact cutoff in this proof must equal one on \(q(\operatorname{supp}f)\), not just on the support of \(Pf\). For a signed function, subgroup integration can cancel to zero on a coset while \(f\) is nonzero there. The choice above covers those cosets as well.

## A cutoff over all cosets

For a general subgroup the modular obstruction need not vanish. To construct a compensating density, we need a continuous nonnegative \(k\) on \(G\) such that
\[
Pk=1,\qquad
\operatorname{supp}k\cap q^{-1}(E)\text{ is compact for each compact }E\subset Y.
\tag{8}
\]
It will not generally have compact support on all of \(G\).

**Lemma 4.1.** A function \(k\) with properties (8) exists.

*Proof.* Choose a relatively compact symmetric open identity neighborhood \(V\) in \(G\). The subgroup \(L=\bigcup_{n\geq1}V^n\) is open and \(\sigma\)-compact: \(V^n\subset(\overline V)^n\subset L\), with the latter compact, since \(\overline V\subset V^2\). For the last inclusion, if \(x\in\overline V\), the open set \(xV\) meets \(V\), so \(x\in VV^{-1}=V^2\).

The \(L\)-orbits in \(Y\) are disjoint open sets, because \(q\) is open; their complements are unions of other orbits, so they are also closed. Each orbit \(Y_0\) is the continuous image of \(L\), hence is \(\sigma\)-compact and LCH.

On such an orbit choose a compact exhaustion \(K_n\subset\operatorname{int}K_{n+1}\), with union \(Y_0\). To construct it, start with a countable compact cover; at each step cover the preceding compact set and the next compact set in that cover by finitely many relatively compact open neighborhoods, and take the union of their compact closures. Put \(K_0=K_{-1}=\varnothing\). The compact shells
\[
S_n=K_n\setminus\operatorname{int}K_{n-1}
\]
are contained in the open sets \(W_n=\operatorname{int}K_{n+1}\setminus K_{n-2}\), and cover \(Y_0\). By Lemma 1.1 choose \(\chi_n\in C_c(Y_0)\), nonnegative, equal to one on \(S_n\), with support in \(W_n\). The family is locally finite: a neighborhood contained in \(\operatorname{int}K_N\) misses \(W_n\) for \(n\geq N+2\). Therefore
\[
\psi_n=\frac{\chi_n}{\sum_j\chi_j}
\]
are continuous, compactly supported, locally finite, nonnegative and sum to one on \(Y_0\).

Perform this construction in every orbit and extend the functions by zero to \(Y\). The resulting family \((\psi_i)\) is still locally finite because the orbits are open, and each \(\psi_i\) has compact support. By Lemma 2.1 choose \(b_i\geq0\) in \(C_c(G)\) with \(Pb_i=1\) on \(\operatorname{supp}\psi_i\). Set
\[
k(g)=\sum_i \psi_i(q(g))b_i(g).
\tag{9}
\]
Local finiteness makes this continuous. Averaging gives \(Pk=\sum_i\psi_i=1\). A compact subset of \(Y\) meets only finitely many supports of this locally finite family; over that compact set, the support of \(k\) lies in the union of the corresponding finitely many compact supports of \(b_i\). It is closed there, so is compact. This proves (8). \(\square\)

The construction uses neither a countable base for \(G\) nor a global continuous section of \(G\to G/H\).

## The modular density and weighted integration

Write
\[
\chi(h)=\frac{\Delta_G(h)}{\Delta_H(h)}.
\]
This is a positive continuous character on \(H\). From the cutoff of Lemma 4.1 define
\[
\rho(g)=\int_H k(gh)\chi(h)\,dh.
\tag{10}
\]

**Lemma 5.1.** The function \(\rho\) is continuous, strictly positive and finite, and
\[
\rho(gh)=\frac{\Delta_H(h)}{\Delta_G(h)}\rho(g)
\qquad(g\in G,\ h\in H).
\tag{11}
\]

*Proof.* For \(g\) in a compact neighborhood \(A\), property (8) puts all \(gh\) that contribute into one compact subset \(B\) of \(G\). Then \(h\) lies in the compact set \(H\cap A^{-1}B\). The integrand is continuous and varies uniformly on this set; its integral is therefore finite and continuous in \(g\). Since \(Pk=1\), \(k\) is not identically zero on any fiber; \(\chi>0\), so \(\rho>0\). For \(r\in H\), substitute \(t=rh\) using left invariance:
\[
\rho(gr)=\int_H k(gt)\chi(r^{-1}t)\,dt
=\chi(r)^{-1}\rho(g).
\]
This is (11). \(\square\)

A continuous positive function satisfying (11) is called a \(\rho\)-function. It is a density on the group, not usually a function on the quotient.

**Theorem 5.2.** For any \(\rho\)-function there is a unique Radon measure \(\mu_\rho\) on \(Y\) satisfying
\[
\int_Y Pf\,d\mu_\rho=\int_G f(g)\rho(g)\,dg
\qquad(f\in C_c(G)).
\tag{12}
\]
It is positive on nonempty open subsets of \(Y\). The construction is independent of the cutoff.

*Proof.* Use a cutoff \(k\) as in (8), and define a positive functional by
\[
\Lambda(F)=\int_G F(q(g))\,k(g)\rho(g)\,dg
\qquad(F\in C_c(Y)).
\tag{13}
\]
The integrand has compact support by (8), so this is finite and Radon representation applies.

For \(F=Pf\), exchange the integrals in (13) and put \(t=gh\). The translation factor is \(\Delta_G(h)^{-1}\), while (11) gives
\(\rho(th^{-1})=\chi(h)\rho(t)\). Thus
\[
\begin{aligned}
\Lambda(Pf)
&=\int_G f(t)\rho(t)
 \left(\int_H k(th^{-1})\Delta_H(h)^{-1}\,dh\right)dt\\
&=\int_G f(t)\rho(t)Pk(tH)\,dt
=\int_G f(t)\rho(t)\,dt.
\end{aligned}
\tag{14}
\]
The first integral before substitution is compactly supported on \(G\times H\): the \(g\)'s lie in \(\operatorname{supp}k\cap q^{-1}(q(\operatorname{supp}f))\), which is compact, and the \(h\)'s then lie in a compact set as in Lemma 2.1. Hence the compact-product theorem justifies the exchange. Inversion on \(H\) gives the second line.

Uniqueness follows from surjectivity of \(P\) and uniqueness in Radon representation; consequently no choice of cutoff changes the measure. A nonempty open subset of \(Y\) has a nonzero nonnegative \(F\in C_c(Y)\) supported there, by Lemma 1.1. Lift it to nonnegative nonzero \(f\in C_c(G)\). Then (12), \(\rho>0\) and Haar positivity give \(\int F\,d\mu_\rho>0\). \(\square\)

If \(\rho_1,\rho_2\) are two \(\rho\)-functions, their ratio is constant on each coset by (11). It descends to a strictly positive continuous function \(r\) on \(Y\), because \(q\) is a quotient map. Applying (12) to \(r(q(g))f(g)\) and using surjectivity of \(P\) proves
\[
d\mu_{\rho_2}=r\,d\mu_{\rho_1}.
\tag{15}
\]
Thus all the measures constructed from continuous positive \(\rho\)-functions have the same null sets. No assertion about arbitrary non-regular measures is needed.

## Quasi-invariance and the direction of translation

Let \(T_a(y)=ay\). The ratio
\[
c(a,gH)=\frac{\rho(ag)}{\rho(g)}
\tag{16}
\]
is well-defined and continuous. Replacing \(g\) by \(gh\) multiplies both numerator and denominator by the same factor from (11). Direct cancellation gives
\[
c(ab,y)=c(a,by)c(b,y).
\tag{17}
\]

**Theorem 6.1.** The measure \(\mu_\rho\) is strongly quasi-invariant. More precisely,
\[
\frac{d[E\mapsto\mu_\rho(aE)]}{d\mu_\rho}(gH)
=\frac{\rho(ag)}{\rho(g)},\qquad
\frac{d(T_a)_*\mu_\rho}{d\mu_\rho}(gH)
=\frac{\rho(a^{-1}g)}{\rho(g)}.
\tag{18}
\]
Both densities are strictly positive and continuous.

*Proof.* For \(F\in C_c(Y)\), substitute \(g=at\) in (13), using left Haar invariance:
\[
\begin{aligned}
\int_Y F(a^{-1}y)\,d\mu_\rho(y)
&=\int_G F(tH)k(at)\rho(at)\,dt\\
&=\int_G F(tH)c(a,tH)k(at)\rho(t)\,dt.
\end{aligned}
\]
The function \(k_a(t)=k(at)\) is another cutoff: \(Pk_a(tH)=Pk(atH)=1\), and it has the compact-support-over-compacts property because \(a\) acts homeomorphically on \(Y\). Cutoff independence in Theorem 5.2 therefore identifies the last integral with \(\int_Y F(y)c(a,y)\,d\mu_\rho(y)\).

Both sides represent Radon measures, so equality on \(C_c(Y)\) is equality of those measures. On the left the measure of \(E\) is \(\mu_\rho(aE)\). This proves the first formula; replace \(a\) by \(a^{-1}\) for the ordinary pushforward convention. A strictly positive density preserves null sets in both directions: if its integral over \(E\) vanishes, intersect \(E\) with the sets where the density is at least \(1/n\), then take their countable union. This proves quasi-invariance. \(\square\)

Notice the inverse in the second formula. The two expressions describe different measures, not an ambiguity in the modular convention.

### Relative invariance and a character

The distinction between invariance and quasi-invariance has a useful intermediate case. Following the freely accessible treatment by Bekka, de la Harpe and Valette, call a nonzero Radon measure \(\mu\) **relatively invariant with character** \(\chi\) if \(\chi:G\to\mathbb R_{>0}\) is a continuous homomorphism and
\[
\mu(aE)=\chi(a)\mu(E)
\]
for every Borel \(E\subset Y\).

**Theorem 6.2.** Such a measure exists if and only if
\[
\chi(h)=\frac{\Delta_H(h)}{\Delta_G(h)}\qquad(h\in H).
\tag{6.2}
\]
For a fixed \(\chi\), it is unique up to a positive scalar. If it has finite positive total mass, then \(\chi=1\).

*Proof.* If (6.2) holds, \(\rho=\chi\) is a rho-function. Theorem 5.2 constructs \(\mu_\chi\), and Theorem 6.1 gives \(c(a,y)=\chi(a)\), proving relative invariance.

Conversely, suppose \(\mu\) has this property. Define
\[
L(f)=\int_Y P(f/\chi)(y)\,d\mu(y)\qquad(f\in C_c(G)).
\]
This is a positive nonzero functional: multiplication by \(\chi^{-1}\) preserves \(C_c(G)\), and positive surjectivity of \(P\) supplies a nonnegative test with positive integral against the nonzero Radon measure. Also
\[
P((L_af)/\chi)(y)=\chi(a)^{-1}P(f/\chi)(a^{-1}y).
\]
Relative invariance cancels these two factors, so \(L(L_af)=L(f)\). Riesz representation and Haar uniqueness give \(L(f)=C\int_Gf\,dg\), with \(C>0\). Substituting \(\chi f\) yields
\[
\int_Y Pf\,d\mu=C\int_G\chi(g)f(g)\,dg.
\]
For \(h\in H\), the left side with \(R_hf\) is multiplied by \(\Delta_H(h)^{-1}\). Right translation on the right side gives the factor \(\Delta_G(h)^{-1}\chi(h)^{-1}\). A positive test with nonzero integral equates the two factors and proves (6.2). The displayed identity and surjectivity of \(P\) also prove uniqueness up to \(C\). Finally \(\mu(aY)=\mu(Y)\), so finite positive total mass forces \(\chi(a)=1\) for all \(a\). \(\square\)

### The quasi-regular representation

**Theorem 6.3.** For the rho-function measure, define
\[
(\pi_\rho(a)\xi)(y)=c(a^{-1},y)^{1/2}\xi(a^{-1}y),
\qquad \xi\in L^2(Y,\mu_\rho).
\tag{6.3}
\]
Then \(\pi_\rho\) is a strongly continuous unitary representation of \(G\). If \(\mu_{\rho_2}=r\mu_{\rho_1}\) as in (15), multiplication by \(r^{-1/2}\) gives a unitary intertwiner from \(\pi_{\rho_1}\) to \(\pi_{\rho_2}\).

*Proof.* Quasi-invariance makes composition with \(a^{-1}\) well-defined on equivalence classes. Theorem 6.1, first for nonnegative simple functions and then by monotone convergence, gives the change-of-variables rule
\[
\int_Y\phi(y)\,d\mu_\rho(y)
=\int_Y\phi(az)c(a,z)\,d\mu_\rho(z).
\]
The cocycle identity says \(c(a^{-1},az)c(a,z)=1\). Apply the rule to \(\phi(y)=c(a^{-1},y)|\xi(a^{-1}y)|^2\); it proves \(\|\pi_\rho(a)\xi\|_2=\|\xi\|_2\). The same identity gives
\[
c(a^{-1},y)c(b^{-1},a^{-1}y)=c((ab)^{-1},y),
\]
so \(\pi_\rho(a)\pi_\rho(b)=\pi_\rho(ab)\). Its inverse is \(\pi_\rho(a^{-1})\), hence it is unitary.

For \(\xi\in C_c(Y)\), fix a compact identity neighborhood \(A\subset G\), with \(e\in A\). All functions \(\pi_\rho(a)\xi\), \(a\in A\), vanish off the compact set \(A\operatorname{supp}\xi\). The continuous function
\((a,y)\mapsto c(a^{-1},y)^{1/2}\xi(a^{-1}y)\)
converges uniformly on this compact set to \(\xi(y)\) as \(a\to e\): continuity at every \((e,y)\) and a finite cover of the compact set give a common identity neighborhood for each prescribed error. Radon finiteness on that compact set proves convergence in \(L^2\). The density of \(C_c(Y)\) in \(L^2(Y,\mu_\rho)\), proved by the Haar lesson's Radon-measure Proposition 3.1(4), and the unitary norm bound extend convergence to every \(\xi\). The representation law gives continuity at every \(a\).

For the last assertion, \(U\xi=r^{-1/2}\xi\) satisfies
\(\int|U\xi|^2\,d\mu_{\rho_2}=\int|\xi|^2\,d\mu_{\rho_1}\)
and has inverse multiplication by \(r^{1/2}\). Since
\[
c_2(a^{-1},y)=\frac{r(a^{-1}y)}{r(y)}c_1(a^{-1},y),
\]
substitution in (6.3) gives \(U\pi_{\rho_1}(a)=\pi_{\rho_2}(a)U\). \(\square\)

For the affine action on the real line in the following examples, \(c((a,b),t)=a\). Formula (6.3) consequently becomes
\[
(\pi(a,b)\xi)(t)=a^{-1/2}\xi((t-b)/a).
\]
The square root of the inverse scaling is exactly the factor needed for unitarity on \(L^2(\mathbb R,dt)\).

### Finite covolume forces unimodularity

**Proposition 6.4.** If \(H\) is a closed unimodular subgroup and \(G/H\) has a nonzero invariant Radon measure of finite total mass, then \(G\) is unimodular. In particular, every group admitting a lattice is unimodular.

*Proof.* Theorem 3.1 gives \(\Delta_G|_H=1\), so \(d(gH)=\Delta_G(g)\) is a well-defined continuous positive function on \(Y\). Suppose \(\Delta_G(a)=s>1\); if a nontrivial modular value is smaller than one, replace that element by its inverse. The Borel sets
\[
E_j=\{y:s^j\leq d(y)<s^{j+1}\},\qquad j\in\mathbb Z,
\]
are disjoint and cover \(Y\). Since \(d(ay)=s\,d(y)\), multiplication by \(a\) sends \(E_j\) onto \(E_{j+1}\). Invariance makes their measures equal. Positive total mass forces at least one to have positive measure, whereas infinitely many disjoint sets of that same positive measure contradict finite total mass. Thus \(\Delta_G=1\). A discrete subgroup is unimodular for counting measure. It is also closed: choose an open identity neighborhood \(V\) with \(V^{-1}V\cap\Gamma=\{e\}\). Every translate \(xV\) meets \(\Gamma\) in at most one point. If \(x\) lies in its closure, choose \(\gamma\in xV\cap\Gamma\); if \(x\ne\gamma\), the open neighborhood \(xV\setminus\{\gamma\}\) would miss \(\Gamma\), a contradiction. Hence \(x\in\Gamma\). This proves the closedness needed to apply the proposition and completes the lattice assertion. \(\square\)

**Corollary 6.5.** If \(H\) is closed and unimodular and \(G/H\) is compact, then \(G\) is unimodular and \(G/H\) has a finite nonzero invariant Radon measure. In particular, a closed discrete cocompact subgroup is a lattice, often called a **uniform lattice**.

*Proof.* The character \(\chi=\Delta_G^{-1}\) satisfies (6.2) because \(\Delta_H=1\). Theorem 6.2 gives a nonzero relatively invariant Radon measure. Compactness makes its total mass finite; its last assertion therefore gives \(\chi=1\), or \(\Delta_G=1\). The measure is invariant and has positive mass. \(\square\)

### Integration of quotient densities

Vogan's freely accessible treatment gives an intrinsic formulation even when an invariant scalar measure does not exist. It regards the modular correction as part of the function being integrated. Here is the formulation and a full derivation from the weighted Weil formula.

**Corollary 6.6.** Let \(\mathcal D_c(G/H)\) be the continuous functions \(F:G\to\mathbb C\), with support compact modulo \(H\), satisfying
\[
F(gh)=\frac{\Delta_H(h)}{\Delta_G(h)}F(g).
\tag{6.6}
\]
Here support compact modulo \(H\) means that the support of the descended function \(F/\rho\) on \(Y\) is compact; this condition is independent of the positive rho-function. The map
\[
Af(g)=\int_H f(gh)\frac{\Delta_G(h)}{\Delta_H(h)}\,dh
\]
sends \(C_c(G)\) onto \(\mathcal D_c(G/H)\). There is a unique positive linear integral \(J\) on this space with
\[
J(Af)=\int_G f(g)\,dg.
\tag{6.7}
\]
It is independent of the choice of rho-function and invariant under \(F(g)\mapsto F(a^{-1}g)\).

*Proof.* Equation (11) gives
\[
Af(g)=\rho(g)P(f/\rho)(gH).
\]
Thus \(Af\) has the covariance (6.6) and compact quotient support. Conversely, \(F/\rho\) descends to a member \(\phi\in C_c(Y)\). Choose \(u\in C_c(G)\) with \(Pu=\phi\) by Lemma 2.1. Then \(f=\rho u\) is compactly supported and \(Af=F\). Define
\[
J(F)=\int_Y\frac{F(g)}{\rho(g)}\,d\mu_\rho(gH).
\]
The quotient integrand is well-defined, continuous and compactly supported. Theorem 5.2 gives \(J(Af)=\int(f/\rho)\rho\,dg=\int f\,dg\). This also proves uniqueness and positivity, using a positive lift when \(F\geq0\).

If \(\rho_2=r\rho_1\) on the quotient, then \(\mu_{\rho_2}=r\mu_{\rho_1}\), and the factors cancel in this definition of \(J\). Finally \(A(L_af)(g)=Af(a^{-1}g)\). Surjectivity of \(A\) and left Haar invariance in (6.7) prove the claimed invariance of \(J\). The integral on these covariant functions therefore survives even when Theorem 3.1 rules out an invariant scalar measure. \(\square\)

## Examples that test the formula

**Translations inside the affine group.** Write
\[
G=\{(a,b):a>0,\ b\in\mathbb R\},\qquad
(a,b)(a',b')=(aa',b+ab').
\]
The preceding Haar lesson, Example 11.3, calculates \(dg=a^{-2}\,da\,db\) and \(\Delta_G(a,b)=a^{-1}\). For \(H=\{(1,t):t\in\mathbb R\}\), \(dh=dt\) and \(\Delta_H=1\). The restriction of \(\Delta_G\) to \(H\) is one, so the quotient has an invariant measure. It is parametrized by \(a\), and (6) becomes
\[
\int_0^\infty\int_{\mathbb R}f(a,b)\,\frac{db\,da}{a^2}
=\int_0^\infty\left(\int_{\mathbb R}f(a,at)\,dt\right)\frac{da}{a}.
\tag{19}
\]
The substitution \(b=at\) verifies the formula and identifies the quotient measure \(da/a\).

**Dilations inside the same group.** Instead take \(H=\{(a,0):a>0\}\), with \(dh=da/a\). It is abelian, so \(\Delta_H=1\), but \(\Delta_G|_H=a^{-1}\). There is no invariant quotient measure. The quotient is parametrized by \(b\), and \(\rho(a,b)=a\) satisfies (11). Formula (12) gives ordinary \(db\) on \(Y\):
\[
\int_{\mathbb R}\int_0^\infty f(a,b)\,\frac{da}{a}\,db
=\int_G f(a,b)\rho(a,b)\,dg.
\]
The element \((a_0,b_0)\) acts by \(b\mapsto b_0+a_0b\). Its pullback-on-sets density is \(a_0\), and its pushforward density is \(a_0^{-1}\), precisely as in (18).

**Compact subgroups.** If \(H\) is compact, normalize \(dh(H)=1\). Then \(\rho=1\) is allowed and averaging is ordinary fiberwise probability averaging. The quotient measure need not itself be finite: \(\mathbb R/\{0\}\) is already a counterexample. Compactness of the fiber does not mean compactness of the base.

**The upper half-plane.** Let \(G=\operatorname{SL}_2(\mathbb R)\) and \(H=\operatorname{SO}(2)\). The action
\[
\begin{pmatrix}a&b\\c&d\end{pmatrix}z=\frac{az+b}{cz+d}
\]
preserves \(\mathbb H=\{x+iy:y>0\}\), since direct subtraction of the complex conjugate gives
\[
\operatorname{Im}(gz)=\frac{y}{|cz+d|^2}.
\]
The denominator never vanishes on \(\mathbb H\). The element
\(s(x+iy)=\begin{pmatrix}\sqrt y&x/\sqrt y\\0&1/\sqrt y\end{pmatrix}\)
sends \(i\) to \(x+iy\). Solving \(gi=i\) gives \(a=d\), \(b=-c\), \(a^2+b^2=1\), so the stabilizer is exactly \(H\). Thus \(gH\mapsto gi\) is a continuous bijection \(G/H\to\mathbb H\), and its inverse is the continuous map \(z\mapsto s(z)H\). This proves the claimed identification, including its topology.

Here is a direct integral proof of invariance of
\[
 dA(z)=y^{-2}\,dx\,dy.
 \tag{20}
\]
This positive continuous density defines a Radon measure. Upper triangular matrices act by translations \(z\mapsto z+t\) and positive dilations \(z\mapsto a^2z\). Iterated one-variable substitution proves that both preserve \(dA\). The substitution and integrated-derivative rules are proved in [Measure and Hilbert space tools for Haar integration](measure-and-hilbert-space-tools.md), Lemma 6.1.

Here are the differential facts used for the rotation computation. The one-variable rules and sine/cosine derivatives have been proved in [the preceding topology lesson](course:function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity), Appendix (B1)–(B2). A real \(C^1\) function \(F\) on an open subset of \(\mathbb R^n\) satisfies
\[
 F(x+h)=F(x)+\sum_j\partial_jF(x)h_j+o(|h|).
 \tag{20a}
\]
To prove this, take a small box about \(x\) in the domain and change its coordinates one at a time. The one-variable mean value theorem writes the \(j\)-th increment as \(\partial_jF(\xi_j)h_j\), with \(\xi_j\to x\) as \(h\to0\). Continuity of each partial derivative makes the error at most \(\max_j|\partial_jF(\xi_j)-\partial_jF(x)|\sum_j|h_j|=o(|h|)\). Inserting the first-order expansion of a differentiable curve or map into (20a) proves the corresponding chain rule. Complex \(F\) is treated coordinatewise; matrix-valued and complex-coordinate maps are treated by their finitely many real components.

Write \(T_\theta(z)=k_\theta z\), \(C=\cos\theta\), \(S=\sin\theta\). Its formula is
\[
 T_\theta(z)=\frac{Cz+S}{-Sz+C}.
\]
The denominator cannot vanish for \(z\in\mathbb H\): if \(S\ne0\), its imaginary part is \(-Sy\ne0\); if \(S=0\), \(|C|=1\). The functions are smooth in the real coordinates by the product, reciprocal, chain and sine/cosine derivative rules of (B1)–(B2). At zero, the numerator has derivative one and the denominator derivative \(-z\), so
\[
 \left.\frac{d}{d\theta}T_\theta(z)\right|_{\theta=0}=1+z^2.
\]
Taking coordinates gives \(v(x,y)=(1+x^2-y^2,2xy)\). The matrix multiplication law gives \(T_{\theta+h}=T_\theta\circ T_h\); differentiate \(F(T_\theta(T_hz))\) at \(h=0\) using (20a). Thus
\[
 \frac{d}{d\theta}F(T_\theta z)
 =v(z)\cdot\nabla_z(F\circ T_\theta)(z).
 \tag{20b}
\]

For rotations \(k_\theta=\begin{pmatrix}\cos\theta&\sin\theta\\ -\sin\theta&\cos\theta\end{pmatrix}\), their action has infinitesimal vector field
\[
 v(x,y)=(1+x^2-y^2,2xy),\qquad
 \partial_x(y^{-2}v_1)+\partial_y(y^{-2}v_2)=0.
\]
If \(F\in C_c^1(\mathbb H)\), put \(J(\theta)=\int F(k_\theta z)\,dA(z)\). On every compact parameter interval, the supports of these functions and their derivatives lie in one compact subset of \(\mathbb H\): it is the image of that interval times \(\operatorname{supp}F\) under \((\theta,w)\mapsto k_{-\theta}w\). The derivatives are bounded there, and \(y\) is bounded away from zero. On a slightly larger compact parameter interval the one-variable mean value theorem bounds every parameter difference quotient, separately in its real and imaginary parts, by a constant times the indicator of this common compact support. That bound is integrable, so dominated convergence permits differentiation. The flow identity gives
\[
 J'(\theta)=\int v(z)\cdot\nabla_z(F(k_\theta z))\,y^{-2}\,dx\,dy=0.
\]
For the last equality, integrate each coordinate derivative of the compactly supported product \(y^{-2}v_jF(k_\theta z)\). Its integral is zero by the integrated-derivative rule and Fubini. The remaining term is minus the displayed divergence, hence zero. Therefore rotations preserve the integral.

This extends to \(C_c(\mathbb H)\) without assuming a smoothing theorem. On a rectangle strictly inside \(\mathbb H\), polynomials uniformly approximate a continuous function by [the compact Stone–Weierstrass theorem](course:function-algebras-and-approximation/the-stone-weierstrass-theorem-for-functions-vanishing-at-infinity), Theorem 9.1(a), applied to real and imaginary parts. Multiply them by a \(C^1\) cutoff equal to one on the function's support and supported in that rectangle. Such a cutoff is a product of one-variable plateaus joined to zero by the cubic \(3t^2-2t^3\), whose endpoint derivatives vanish. The approximants have one compact support and converge uniformly; both their original and rotated integrals converge because the relevant compact sets have finite area.

Finally every \(g\in G\) is \(s(z)k\), as proved by its action on \(i\); \(s(z)\) is upper triangular. Translations, positive dilations and rotations therefore generate the action of \(G\). This proves invariance of (20) under every \(g\). By Theorem 3.1 it is the quotient measure up to Haar normalization. The next lesson calculates the modular lattice volume from this measure.

**An integer lattice.** For \(G=\mathbb R^n\), \(H=\mathbb Z^n\), Lebesgue and counting measures give
\[
\int_{\mathbb R^n}f(x)\,dx
=\int_{[0,1)^n}\sum_{m\in\mathbb Z^n}f(x+m)\,dx.
\tag{21}
\]
For \(f\in C_c(\mathbb R^n)\), only finitely many lattice translates meet its support while \(x\) ranges over the unit cube. Translate each summand and use the disjoint half-open tiling of \(\mathbb R^n\). This proves (21); the boundary faces have Lebesgue measure zero. The resulting quotient measure has total mass one.

## Exercises with solutions

**1. Rescaling the measures.** If \(dg\) is multiplied by \(A>0\) and \(dh\) by \(B>0\), how does the normalized invariant quotient measure change?

*Solution.* The new averaging operator is \(BP\). To keep (6), the quotient measure must be multiplied by \(A/B\). The same rule holds in (12) when the function \(\rho\) is kept fixed. The modular functions do not change under Haar rescaling.

**2. A discrete subgroup with no invariant quotient measure.** In the affine group let \(H=\{(2^n,0):n\in\mathbb Z\}\). Prove that \(H\) is closed and discrete, and decide whether \(G/H\) has an invariant measure.

*Solution.* Any compact interval in the \(a\)-coordinate bounded away from zero meets \(\{2^n\}\) finitely. Around each group element one may choose such an interval, so there is no accumulation point in \(G\), and each point of \(H\) is isolated. Thus \(H\) is closed and discrete. Its modular function is one, whereas \(\Delta_G(2^n,0)=2^{-n}\). Theorem 3.1 rules out a nonzero invariant quotient measure. This shows why “discrete” cannot replace the modular criterion.

**3. Two choices of density.** Suppose \(\rho_1,\rho_2\) satisfy (11). Prove both (15) and the transformation rule
\[
c_2(a,y)=\frac{r(ay)}{r(y)}c_1(a,y).
\]

*Solution.* Their ratio \(r(q(g))=\rho_2(g)/\rho_1(g)\) is unchanged by right multiplication by \(H\), hence is continuous on the quotient. For \(F=Pf\), the integral of \(F\) against \(r\mu_{\rho_1}\) is, by (12), \(\int_G f(g)r(q(g))\rho_1(g)\,dg=\int_G f(g)\rho_2(g)\,dg\). Surjectivity of \(P\) and Radon uniqueness give (15). Substitution in (16) gives the cocycle formula. In particular, changing the density changes the cocycle by this explicit ratio, without changing the measure class.

**4. Quotient averaging is equivariant.** Prove (5) and use it to show that two invariant quotient measures normalized by (6) coincide.

*Solution.* Directly,
\[
P(L_a f)(gH)=\int_Hf(a^{-1}gh)\,dh=Pf(a^{-1}gH).
\]
For \(r\in H\), right translation in the integration variable gives \(\int_H f(ghr)\,dh=\Delta_H(r)^{-1}Pf(gH)\). If two measures satisfy (6), they integrate \(Pf\) equally for every \(f\). Lemma 2.1 says every member of \(C_c(Y)\) is such a \(Pf\); Radon uniqueness proves equality.

**5. No global compact cutoff on a noncompact base.** Show that a cutoff \(k\) satisfying \(Pk=1\) cannot have compact support in \(G\) when \(Y\) is noncompact.

*Solution.* If \(k\) had compact support, then \(\operatorname{supp}Pk\subset q(\operatorname{supp}k)\) would be compact. But \(Pk=1\) has support all of \(Y\). Therefore \(Y\) would be compact. The weaker compactness condition in (8) is exactly what permits the global construction.

**6. Track one modular factor.** In (14), explain why the product of the right-translation factor and the density-change factor is \(\Delta_H(h)^{-1}\), not \(\Delta_H(h)\).

*Solution.* Writing \(t=gh\) in an integral over \(g\) contributes \(\Delta_G(h)^{-1}\). Equation (11) gives \(\rho(th^{-1})=\Delta_G(h)\Delta_H(h)^{-1}\rho(t)\). Multiplying cancels \(\Delta_G(h)\), leaving \(\Delta_H(h)^{-1}\). That is exactly the factor in the inversion formula \(\int_H a(h^{-1})\Delta_H(h)^{-1}\,dh=\int_Ha(h)\,dh\).

## What this enables

The invariant criterion is available to the programme's subgroup and quotient, adèle and automorphic courses. Theorem 6.3 turns the density and cocycle formulas into a strongly continuous quasi-regular representation, including its unitary equivalence under a change of density. Proposition 6.4 and Corollary 6.5 explain the unimodularity and compactness constraints on lattices. Corollary 6.6 gives an invariant integral on quotient densities. The two inverse-translation conventions in (18) remain explicit in these action formulas.

The principal formulas above are stated and proved on \(C_c(G)\). Extending them to arbitrary measurable functions requires the precise regularity and support conventions of the preceding measure-theory lessons. The abelian Fourier course already proves its \(L^1\) extension. This lesson does not quietly replace the general non-\(\sigma\)-finite measure theory by a second-countable argument.

## Sources and credit

- D. H. Fremlin, [*Measure Theory*, Volume 4](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/index.htm), develops positive subgroup averaging, quotient integration and the same modular criterion. His complete, locally determined measure convention is related to ours by [Proposition 13.7 of the Haar lesson](haar-measure-on-locally-compact-groups.md#haar-measure-convention-bridge). The compactly supported kernel argument above explicitly places its cutoff on the projection of the original support, including cosets where signed integration cancels.
- David Vogan, [*Invariant measures on homogeneous spaces*](https://math.mit.edu/~dav/integration.pdf), gives a complementary treatment of averaging and the invariant-measure criterion, and the quotient-density viewpoint developed in Corollary 6.6.
- *Haar measure on locally compact groups*, programme lesson originally by Claude Opus 5.5, supplies the Haar, Radon-product and modular proofs named above. Retained programme expression is CC0.
- *Quotient measure and the subgroup modular correction*, OA-FLOW lesson 43, credits OpenAI Codex. Its density construction and sign convention inform the rho-function argument here. Its historical exact model is not recorded.
- *Subgroups, quotients and annihilators*, HA-LCA lesson by GPT-6.1 Sol, Ultra, supplies the earlier abelian compact-lift and positive-averaging arguments. The present lesson proves their general-group versions in full.
- B. Bekka, P. de la Harpe and A. Valette, [*Kazhdan’s Property (T)*](https://perso.univ-rennes1.fr/bachir.bekka/KazhdanTotal.pdf), freely accessible author preprint dated 23 February 2007. Its homogeneous-space and lattice treatment motivates Theorems 6.2–6.3 and the finite-covolume results. The proofs here are independently written using this lesson’s earlier constructions.
