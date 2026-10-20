# Templates, transfers and frequency histories

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Lesson 7 ended with a lower bound \(|\eta_0|\ge e^{-B_0m}\) for the distinct-prime part of a positive statistic. This lesson writes \(\eta_0\) as a sum over a dual frequency of explicit phases, and then defines a sequence of amplitudes \(\eta_1,\dots,\eta_k\) by *transfers*. A transfer applies Cauchy–Schwarz over the residues of one group of primes (the *pivot*), extends that group to arbitrary integers, and expands the square. The result is a new amplitude of the same shape with twice as many copies of the word, plus a diagonal term:
\[
|\eta_{j-1}|^2\le e^{d_j}\bigl(\eta_j+\mathcal D_j\bigr)
\]
(Proposition 3.2). The phases keep a precise form, recorded by an exponent matrix, through all transfers (Lemma 3.1). Unrolling the recursion expresses each term of \(\eta_l\) through a binary tree of frequencies, a *history*; for a given top assignment and root frequency there is at most one valid history (Lemma 4.1), and the histories have controlled total square weight (Proposition 5.1). Lesson 9 bounds the diagonals and compares histories, which proves Theorem 1.1 of Lesson 7.

**Prerequisites.** [*Scales, cells and a positive statistic for higher characters*](scales-cells-and-a-positive-statistic-for-higher-characters.md); [*Gauss sums*](course:NT-DIRL/NT-DIRL-03), Theorem 2.1; [*Poisson summation, theta, and the functional equation*](course:NT-ZETA/NT-ZETA-04), Theorem 1.2.

The notation of Lesson 7 is in force: the functions \(f_p=z_p\chi^{(p)}(\cdot-t_p)\), the word with bin \(J\), the anchors, the pivot groups \(K_j\) and the filler with targets \(T_j,T_F\), the gaps \(\Delta_j\), the bounds \(V_j=e^{E_j}\), and \(n_c\ll ke^{2\epsilon k}\).

## 1. The level-zero amplitude

**Slots and roles.** The statistic \(I_*\) of Lesson 7 expands into terms indexed by an ordered list of *slots*: a positive and a conjugate copy of every role (the \(m\) bulk labels and the top label of the word, the two anchors of each step, the constituents of each pivot group and of the filler). Each slot \(i\) carries a prime \(p_i\), drawn from its prior, and a character
\[
\begin{gathered}
\lambda_i=\chi^{(p_i)}\\
\text{(positive role)},\\
\lambda_i=\overline{\chi^{(p_i)}}\\
\text{(conjugate role)},
\end{gathered}
\]
so that its local function is \(z_i\lambda_i(x-t_{p_i})\) with \(|z_i|=1\). Every \(\lambda_i\) is nonprincipal of order greater than \(2\). The rule fixing \(\lambda_i\) is attached to the slot and is copied unchanged when the slot is copied.

**The local transform.** For a nonprincipal character \(\lambda\) modulo a prime \(p\), \(t\in\mathbb F_p\) and \(w\in\mathbb F_p\),
\[
\begin{aligned}
&\mathbb E_{x\in\mathbb F_p}\lambda(x-t)\,e_p(wx)\\
&\quad=\begin{cases}
\begin{aligned}&\dfrac{1}{\sqrt p}\cdot\dfrac{\tau(\lambda)}{\sqrt p}\,\\&\quad\lambda(w)^{-1}\,e_p(wt),\end{aligned}&w\ne0,\\
0,&w=0,
\end{cases}\quad(1.1)
\end{aligned}
\]
where \(\tau(\lambda)=\sum_y\lambda(y)e_p(y)\) has modulus \(\sqrt p\) ([*Gauss sums*](course:NT-DIRL/NT-DIRL-03), Theorem 2.1). Indeed, substitute \(x=y+t\), then \(y\mapsto y\overline w\).

**The Poisson dual.** Fix a tuple of distinct primes, put \(M=\prod_ip_i\) and \(F(n)=\prod_iz_i\lambda_i(n-t_{p_i})\), a function of period \(M\). Poisson summation, followed by the substitution \(v\mapsto-v\) (allowed since \(\widehat\psi\) is even), gives
\[
\begin{gathered}
\begin{aligned}
&\sum_n\psi(n/X)F(n)\\
&\quad =X\sum_{v\in\mathbb Z}\widehat F(-v)\,\widehat\psi\Bigl(\frac{vX}M\Bigr),
\end{aligned}\\
\widehat F(-v)=\mathbb E_{n\bmod M}F(n)\,e_M(vn).
\end{gathered}
\]
By the Chinese remainder theorem, \(v/M\equiv\sum_iv\,\overline{M/p_i}/p_i\pmod1\), where \(\overline{M/p_i}\) is an inverse modulo \(p_i\), and \(\widehat F(-v)\) is the product of the local transforms (1.1) at \(w_i=v\,\overline{M/p_i}\). Since \(\lambda_i(w_i)^{-1}=\lambda_i(v)^{-1}\lambda_i(M/p_i)\) and \(\lambda_i(M/p_i)=\prod_{h\ne i}\lambda_i(p_h)\),
\[
\begin{gathered}
\begin{aligned}
\widehat F(-v)&=\frac1{\sqrt M}\,A(v)\prod_i\kappa_i\lambda_i(v)^{-1}\\
&\quad \prod_i\prod_{h\ne i}\lambda_i(p_h)
\end{aligned}\\
\text{if }(v,M)=1,
\end{gathered}
\]
and \(0\) otherwise. Here \(\kappa_i=z_i\tau(\lambda_i)/\sqrt{p_i}\) has modulus \(1\), and
\[
A(v)=\prod_ie_{p_i}\bigl(t_{p_i}\,v\,\overline{M/p_i}\bigr).
\tag{1.2}
\]
Dividing by \(\sqrt X\), the level-zero amplitude of Proposition 6.1 of Lesson 7 is
\[
\eta_0=\mathbb E_{\mathcal I_0}\sum_{v}W_0\,\Theta_0,
\tag{1.3}
\]
where \(\mathbb E_{\mathcal I_0}\) is the expectation over the priors of all slots, and:

- the *phase* \(\Theta_0=A(v)\prod_i\nu_i\prod_i\prod_{h\ne i}\lambda_i(p_h)^{b_{ih}}\) with all \(b_{ih}=1\) and \(\nu_i=\kappa_i\lambda_i(v)^{-1}\);
- the *weight* \(W_0\) is the product of the bin indicators of the two words, \((X/M)^{1/2}\widehat\psi(vX/M)\), the indicators that the slots carry distinct primes and that \((v,M)=1\), and the indicator of a fixed covering interval for \(\log M=\log X+\Delta_0+O_k(1)\).

Since \(\widehat\psi\) vanishes outside \([-\frac14,\frac14]\), only \(0<|v|\le M/(4X)\le V_0\) occur. The term \(v=0\) vanishes.

## 2. Templates, atoms and the exponent matrix

The transfers work with lists of slots whose phases have the shape of \(\Theta_0\).

**Atoms.** At level zero the active slots are the positive word and the constituents of the positive pivot groups \(K_1,\dots,K_k\). The positive anchors of step \(j\) are *reserved* for step \(j\). All conjugate slots, the filler and the unused roles are *outside*. A pivot group is treated as one *atom*, whose constituents are its ordered slots; every other slot is an atom by itself. The distinctness of the constituents of a pivot atom stays in its tuple prior, without normalization; pairwise coprimality of atoms carries the remaining distinctness conditions. Copied atoms receive new independent priors with the same internal restrictions.

**Phases.** For a list \(\mathcal I\) of pairwise coprime atoms, with prime product \(M_{\mathcal I}\), put
\[
A_{\mathcal I}(v)=\prod_{i\in\mathcal I}e_{p_i}\bigl(t_{p_i}\,v\,\overline{M_{\mathcal I}/p_i}\bigr).
\]
Every term of every amplitude below has the form \(W\Theta\) with
\[
\begin{aligned}
\Theta&=A_{\mathcal I}(v)\prod_i\nu_i\\
&\quad \prod_i\prod_{h\ne i}\lambda_i(p_h)^{b_{ih}},\quad(2.1)
\end{aligned}
\]
where \(v\) is the *root frequency*, the *exponents* \(b_{ih}\in\{0,\pm1\}\) are fixed by the template, and each \(\nu_i\) is, once all frequencies are fixed, a function of modulus at most \(1\) of the prime in slot \(i\) alone (a *unary* factor). The entry \(b_{ih}\) is the *row* of \(i\) at the *target* \(h\).

**The invariants.** At level \(l\), the amplitude \(\eta_l\) is an expectation over the priors of a list \(\mathcal I_l\) of a sum over frequency histories (Section 4) of terms \(W_l\Theta_l\) with root frequency \(0<|v|\le V_l\), such that:

1. *Weight.* \(W_l\) depends on the current active pivot atoms only through their total products; all active word bins hold; the current atoms are pairwise coprime and are units modulo the root frequency.
2. *Regular slots.* For a slot \(i\) of an active word or an active pivot, called *regular*,
\[
\begin{gathered}
b_{ih}=\varepsilon_i\quad(h\ne i),\\
\nu_i=\kappa_i\lambda_i(v)^{-\varepsilon_i},
\end{gathered}
\]
where \(\varepsilon_i\in\{1,-1\}\) is the product of the copy signs of the transfers that produced the slot, and \(|\kappa_i|=1\) depends only on the role, the path and the prime, not on any frequency.
3. *Common columns.* For each slot \(h\), the exponent \(b_{hi}\) is the same for all constituents \(i\) of any active pivot atom. Write \(b_{hP}\) for this common value.

At level zero all three hold, with all \(\varepsilon_i=1\).

**The steps.** At step \(j\) the current list \(\mathcal I_{j-1}\) is split as \(P\sqcup H\sqcup Y\):

- \(P\) is the unique active atom of type \(K_j\);
- \(H\) consists of all active words, the unique active atom of each later type \(K_l\), \(l>j\), and the two anchors reserved for step \(j\);
- \(Y\) is the rest.

The letters \(P,H,Y\) also denote the products of the corresponding primes. The new list is
\[
\mathcal I_j=H^+\sqcup H^-\sqcup Y,
\]
two copies of \(H\) (the copy signs \(+\) and \(-\)) and the old \(Y\). Both copies of every word stay active. Of each later pivot atom, only the copy in \(H^+\) stays active; the copy in \(H^-\) becomes outside. Both copies of the step-\(j\) anchors become outside. So before step \(j\) there are \(2^{j-1}\) active words, and by the choice of targets in Lesson 7, on the bin supports,
\[
\begin{gathered}
\log P=T_j+O_k(1),\\
\log H=T_j+\Delta_j+O_k(1).\quad(2.2)
\end{gathered}
\]

## 3. The transfer identity

Fix \(j\ge1\) and put \(l=j-1\). Insert into \(W_l\) the range indicators of (2.2), with fixed covering constants, and the requirement that the pivot be a unit modulo every frequency in its history. These change nothing, because all frequencies are below every prime.

**Removing the pivot factors.** For a constituent \(p_i\) of \(P\), the factors of (2.1) that belong to slot \(i\) are its unary factor, its row, and its additive factor. With \(M=PHY\), the regular-slot invariant gives
\[
\begin{gathered}
\begin{aligned}
&\nu_i\prod_{h\ne i}\lambda_i(p_h)^{\varepsilon_i}\\
&\quad =\kappa_i\,\lambda_i\Bigl(\frac{(P/p_i)\,Y\,H}{v}\Bigr)^{\varepsilon_i},
\end{aligned}\\
\begin{aligned}
&e_{p_i}\Bigl(t_{p_i}v\,\overline{M/p_i}\Bigr)\\
&\quad =e_{p_i}\Bigl(t_{p_i}\frac vH\,\overline{(P/p_i)Y}\Bigr).
\end{aligned}
\end{gathered}
\]
Both depend only on the residue \(u\equiv v\overline H\pmod P\), on \(Y\), and on the pivot tuple, and have modulus at most \(1\). Group the terms of \(\eta_l\) by \(u\bmod P\), remove these factors for all constituents, and call what remains, summed over \(v\) in the class of \(u\) and averaged over \(H\), the quantity \(B_u(P,Y)\). The other factors involving pivot primes are the columns \(\lambda_h(p_i)^{b_{hi}}\), which by the common-column invariant combine to \(\lambda_h(P)^{b_{hP}}\), and the additive factors of the other slots, which involve \(P\) only through \(M\). With the weight invariant, \(B_u(P,Y)\) depends on the pivot tuple only through its total \(P\).

**Cauchy–Schwarz.** Applying Cauchy–Schwarz first to the outer priors and then to the \(P\) residues,
\[
|\eta_l|^2\le\mathbb E_{Y,K_j}\,P\sum_{u\bmod P}|B_u(P,Y)|^2 .
\]
The total of a pivot tuple with \(n_j\) constituents has point mass at most \(e^{d_j}/P\), where
\[
d_j=Cn_jL+O_k(1):
\]
each constituent prime \(p\) has prior weight at most \(e^{CL}/p\) by the cell mass bounds, and a total determines its multiset of primes, hence at most \(n_j!=O_k(1)\) ordered tuples. Since the summand is nonnegative, the expectation over \(K_j\) can be replaced by \(e^{d_j}\) times a sum over all positive integers \(P\) in the range of (2.2):
\[
\begin{aligned}
|\eta_l|^2&\le e^{d_j}\,\mathbb E_Y\sum_P\\
&\qquad\sum_{u\bmod P}|B_u(P,Y)|^2 .\quad(3.1)
\end{aligned}
\]
On this extended sum the integer \(P\) keeps its coprimality with the other atoms and the weight conditions, but no condition from its tuple prior. No character of the integer \(P\) is needed: the rows of its constituents were removed before the extension.

**Expanding the square.** Write \(|B_u|^2\) with two independent copies \(H_L,H_R\) of \(H\) and root frequencies \(v,w\) of the two factors. Summing over \(u\bmod P\) gives the pairs with \(vH_R\equiv wH_L\pmod P\). The terms with \(vH_R=wH_L\) form the *diagonal* \(\mathcal D_j\). For the others, put
\[
\begin{gathered}
P=\frac{vH_R-wH_L}s,\\
s\ne0,\quad(3.2)
\end{gathered}
\]
with the condition that \(P\) is a positive integer in its range. This is a bijection between the off-diagonal terms and the quadruples \((v,w,s)\) together with the lists. By (2.2) and \(|v|,|w|\le V_l\),
\[
\log|s|\le E_{l}+\Delta_j+O_k(1)<E_j,
\]
since \(E_{j-1}+\Delta_j=E_j-2\cdot4^{j-1}\sqrt m\). A prime dividing both \(H_L\) and \(H_R\) would divide \(sP\) and be coprime to \(P\), so it would divide \(s\), which is impossible because every prime exceeds \(V_j\). So \(H_L\) and \(H_R\) are coprime, the inherited conditions separate each of them from \(Y\), and all primes of the new list are units modulo \(s\). Let \(W_j\) be the left weight times the conjugate of the right weight, with these conditions and the substitution (3.2).

**The new phase.** Modulo a prime of the new list, (3.2) gives
\[
\begin{gathered}
\frac vP\equiv\frac s{H_R}\ \ (p_i\mid H_L),\\
-\frac wP\equiv\frac s{H_L}\ \ (p_i\mid H_R),\\
\frac v{PH_L}-\frac w{PH_R}=\frac s{H_LH_R}.
\end{gathered}
\]
Using the first identity at the primes of \(H_L\), the second at those of \(H_R\), and the third at the shared primes of \(Y\), the additive factors of the left term and of the conjugated right term combine exactly into \(A_{\mathcal I_j}(s)\), with \(M_{\mathcal I_j}=H_LH_RY\).

**Lemma 3.1** (the update rule [OpenAI-013, (4.9)]). Label the slots of \(\mathcal I_j\) as \(i^t\) (\(i\in H\), \(t=\pm\), with \(H^+=H_L\), \(H^-=H_R\)) and \(y\in Y\). The new exponents are
\[
\begin{gathered}
\begin{aligned}
b^{\rm new}_{i^th^{t'}}&=
\begin{cases}
t\,b_{ih},&t=t',\ i\ne h,\\
t\,b_{iP},&t\ne t',
\end{cases}
\end{aligned}\\
b^{\rm new}_{i^ty}=t\,b_{iy},\\
b^{\rm new}_{yi^t}=t\,b_{yi},\\
b^{\rm new}_{yy'}=0\ \ (y\ne y'),\quad(3.3)
\end{gathered}
\]
and the three invariants hold at level \(j\), with \(\varepsilon_{i^t}=t\varepsilon_i\) and the root frequency \(s\).

*Proof.* The left term contributes its rows \(\lambda_i(p_h)^{b_{ih}}\) for \(i,h\) in \(P\cup H_L\cup Y\), and the conjugated right term contributes \(\lambda_i(p_h)^{-b_{ih}}\) for \(i,h\) in \(P\cup H_R\cup Y\). Rows between two slots of the same copy give the first case of (3.3). For \(i\in H_L\), the column into the pivot is \(\lambda_i(P)^{b_{iP}}\), and at the prime \(p_i\), \(P\equiv vH_R/s\); so
\[
\lambda_i(P)^{b_{iP}}=\lambda_i(v/s)^{b_{iP}}\prod_{h\in H_R}\lambda_i(p_h)^{b_{iP}},
\]
which is the cross-copy row \(b^{\rm new}_{i^+h^-}=b_{iP}\) and a new unary factor \(\lambda_i(v/s)^{b_{iP}}\). For \(i\in H_R\), conjugation and \(P\equiv-wH_L/s\) give the row \(-b_{iP}\) and the unary factor \(\lambda_i(-w/s)^{-b_{iP}}\). Rows between \(H\) and \(Y\) appear once, from the side containing the \(H\)-slot, with that side's sign. Between two shared slots \(y,y'\in Y\), and from \(y\) into \(P\), the left and right factors are conjugate and cancel; the unary factors of \(y\) combine into a new unary factor.

For a regular slot, \(b_{iP}=\varepsilon_i\). In the left copy the old unary factor \(\kappa_i\lambda_i(v)^{-\varepsilon_i}\) times \(\lambda_i(v/s)^{\varepsilon_i}\) is \(\kappa_i\lambda_i(s)^{-\varepsilon_i}\); in the right copy, \(\overline{\kappa_i}\lambda_i(w)^{\varepsilon_i}\) times \(\lambda_i(-w/s)^{-\varepsilon_i}\) is \(\overline{\kappa_i}\lambda_i(-1)^{-\varepsilon_i}\lambda_i(s)^{\varepsilon_i}\). With \(\varepsilon_{i^\pm}=\pm\varepsilon_i\) and the sign \(\lambda_i(-1)^{-\varepsilon_i}\) absorbed into the new \(\kappa\), both have the form \(\kappa\lambda(s)^{-\varepsilon}\), and (3.3) gives \(b^{\rm new}_{i^t\cdot}=t\varepsilon_i\) on every target. The later pivot atoms are copied together, so their columns stay common; and the weight sees them only through their totals. \(\square\)

**Proposition 3.2** (the transfer [OpenAI-013, (4.7)]). Let \(\eta_j\) be the off-diagonal part of the extended sum in (3.1), that is, the expectation over the priors of \(\mathcal I_j\), with the pivot extended to positive integers by (3.2), of the sum over histories of \(W_j\Theta_j\). Then \(\eta_j\) has the form described in Section 2, and
\[
|\eta_{j-1}|^2\le e^{d_j}\bigl(\eta_j+\mathcal D_j\bigr),
\]
where the diagonal \(\mathcal D_j\) consists of the terms of (3.1) with \(vH_R=wH_L\). \(\square\)

The extended sum in (3.1) is a sum of squared moduli, hence real and nonnegative. Exchanging the two copies maps the diagonal terms to their complex conjugates, so \(\mathcal D_j\) and \(\eta_j\) are real as well. Since every prime of \(H_L\) and \(H_R\) exceeds the frequencies, the diagonal equation \(vH_R=wH_L\) forces \(H_L=H_R\) as integers and \(v=w\). Lesson 9 bounds \(\mathcal D_j\).

## 4. Frequency histories

Unroll a term of \(\eta_l\) from its root. A *history* of depth \(l\) is a full binary tree with \(2^l\) leaves, with a nonzero integer frequency at each node: at a node of step \(j\) it is the root frequency \(s\) of that step, of absolute value at most \(V_j\), and the two children carry the frequencies \(v,w\) of the two factors. At a node of step \(j\), the output slots are \(Y,H_L,H_R\); each child keeps \(Y\) and one copy of \(H\), and inserts the pivot integer (3.2). An inserted pivot can itself appear in a later substitution, as an atom of a later \(H\). Every inserted pivot is required to be coprime to every frequency below its node, and all inherited conditions are evaluated recursively. We also use the same histories with one current active pivot replaced by a fixed positive integer, after its outgoing factors have been removed as in Section 3; this is the *fixed-external* version.

**Lemma 4.1** (uniqueness of histories [OpenAI-013, Section 4]). For a fixed assignment of the top list, including the fixed-external version, and a fixed root frequency, there is at most one valid history.

*Proof.* At the top node, of step \(j\), suppose \((v,w,P)\) and \((v',w',P')\) are both valid, with the same \(s,H_L,H_R\). From \(sP=vH_R-wH_L\) and \(sP'=v'H_R-w'H_L\), the congruences \(vH_R\equiv wH_L\) and \(v'H_R\equiv w'H_L\pmod s\) give \((vw'-v'w)H_R\equiv0\pmod s\), and \(H_R\) is a unit modulo \(s\), so \(s\mid vw'-v'w\). Also
\[
H_R(vw'-v'w)=s(Pw'-P'w),
\]
so
\[
|vw'-v'w|\le|s|\,\frac{P|w'|+P'|w|}{H_R}<|s|,
\]
because \(P|w'|/H_R\le V_{j-1}e^{-\Delta_j+O_k(1)}\) and \(\Delta_j-E_{j-1}=2\cdot4^{j-1}\sqrt m\to\infty\). Hence \(vw'=v'w\): the pairs \((v,w)\) and \((v',w')\) are proportional, and then so are \(P\) and \(P'\), with the same positive ratio \(a/b\) in lowest terms. Then \(b\) divides \(v,w\) and \(P\), and \(a\) divides \(v',w'\) and \(P'\). The inserted pivot is coprime to the frequencies below its node, so \(a=b=1\). The children are then determined, and recursion proves the claim. \(\square\)

## 5. The square weights of the histories

**Proposition 5.1** ([OpenAI-013, (4.10)]). With \(r=2^l\),
\[
\mathbb E\sum_{\text{histories}}|W_l|^2\le\exp\bigl(Crm+o_k(m)\bigr),
\]
with \(C\) independent of \(k\) and \(B_D\). The same holds in the fixed-external version, averaged over its other priors.

*Proof.* *A pointwise bound.* Each history has \(r\) leaves, and each leaf carries a level-zero weight with the factor \((X/M)^{1/2}\widehat\psi\); by (6.2) of Lesson 7, \(X/M=e^{-\Delta_0+O_k(1)}\). So \(|W_l|^2\le\exp(-r\Delta_0+O_k(1))\). After this bound, the bin, range and internal distinctness indicators can be dropped, because only an upper bound for a nonnegative support probability is needed. We keep the integrality conditions and the conditions that frequencies be units.

*Uniform residues.* Every leaf has its own active word. Fix all frequencies and all labels except one chosen bulk prime in each leaf's word. Let \(R\) be the product of the absolute values of all node and leaf frequencies, and \(Q=R^{k+2}=\exp(O_k(m))\). A bulk prior has point weight \(O(1/p)\). In a unit class modulo \(Q\), the sum of \(1/n\) over a dyadic interval of integers much larger than \(Q\) is \(O(1/Q)\), and there are at most \(e^{CL}\) dyadic intervals in the bulk range. So the residue of one chosen prime modulo \(Q\) is dominated by \(e^{CL}\) times the uniform measure on the units modulo \(Q\), and by independence the joint residues of the \(r\) chosen primes are dominated by \(e^{CrL}\) times independent uniform units.

*Exposure.* Under independent uniform units, expose first the product of all chosen variables, then, going down the tree, the product of the chosen variables in the left subtree at each split. Given the parent product, the left product is uniform on the units modulo \(Q\) and determines the right product, because \((x,y)\mapsto(x,xy)\) is a bijection of pairs of units. At a node write
\[
H_L=C_LX_L,\qquad H_R=C_RX_R,
\]
with \(X_L,X_R\) the products of the chosen variables in the two subtrees. The constants \(C_L,C_R\) may contain inserted ancestor pivots, whose residues are known from the splits already exposed. Every chosen word stays inside a copied part \(H\) at every transfer, so a later split refines a product already exposed at each ancestor.

*Precision.* The recurrence (3.2) uses the two current child totals and known integers. If \(s\mid R\) and a numerator is known modulo \(R^a\), its integral quotient by \(s\) is known modulo \(R^{a-1}\); products lose no precision. There are at most \(k\) divisions on a branch, so every quantity is known modulo \(R^2\), enough for all divisibility and unit conditions. A fixed external pivot is known from the start.

*Divisor bounds.* For every \(\varepsilon>0\) there is \(C_\varepsilon\) with \(\tau(n)\le C_\varepsilon n^\varepsilon\) for all \(n\ge1\), where \(\tau(n)\) is the number of divisors. Indeed \(\tau(n)n^{-\varepsilon}=\prod_{p^e\parallel n}(e+1)p^{-e\varepsilon}\); a factor with \(p\ge2^{1/\varepsilon}\) is at most \((e+1)2^{-e}\le1\), and each of the finitely many primes \(p<2^{1/\varepsilon}\) contributes at most \(\max_{e\ge0}(e+1)2^{-e\varepsilon}\). Also \(2^{\omega(n)}\le\tau(n)\) and \(n/\varphi(n)=\prod_{p\mid n}(1-1/p)^{-1}\le2^{\omega(n)}\). So for \(n\le\exp(O_k(m))\), all of \(\tau(n)\), \(2^{\omega(n)}\) and \(n/\varphi(n)\) are \(\exp(o_k(m))\).

*One node.* On valid support \(C_L,C_R\) are units modulo \(|s|\). Given their residues and \(X_LX_R\), integrality of \(P\) requires
\[
vC_RX_R\equiv wC_LX_L\pmod{|s|}.
\]
Congruent integers have the same greatest common divisor with \(s\), so this is impossible unless \((v,s)=(w,s)\); then \(g=(v,w,s)\) equals both. Dividing by \(g\), the congruence becomes a unit square-root equation for \(X_L\) modulo \(|s|/g\), which has at most \(2^{\omega(|s|/g)+1}\) unit solutions. Since \(X_L\) is uniform on units modulo \(Q\) and \(|s|/g\mid Q\), the conditional probability is at most \(2^{\omega(n)+1}/\varphi(n)\) with \(n=|s|/g\le\exp(O_k(m))\). The divisor bounds above give \(2^{\omega(n)+1}n/\varphi(n)=\exp(o_k(m))\), so the probability is at most
\[
\exp(o_k(m))\,\frac g{|s|}.
\]
The sequential exposure multiplies these bounds over the nodes.

*Summing the frequencies.* For fixed child frequencies \(v,w\), grouping \(s=dh\) by \(d=(v,w,s)\), which divides \((v,w)\),
\[
\begin{aligned}
&\sum_{0<|s|\le V_j}\frac{(v,w,s)}{|s|}\\
&\quad \le2\sum_{d\mid(v,w)}\sum_{h\le V_j/d}\frac1h\\
&\quad \le2\tau\bigl((v,w)\bigr)(1+\log V_j)\\
&\quad =\exp(o_k(m)).
\end{aligned}
\]
Sum the internal frequencies from the root down, each with its children fixed; there are \(r-1=O_k(1)\) internal nodes. The \(r\) leaf frequencies have at most \((2V_0)^r=\exp(r\Delta_0+o_k(m))\) choices, which cancels the pointwise factor. The remaining cost is \(\exp(CrL+o_k(m))\)\(\le\exp(Crm+o_k(m))\). \(\square\)

## 6. Exercises

**6.1.** Verify (1.1), including the case \(w=0\).

**6.2.** Let \(x,y\) be independent uniform units modulo \(Q\). Show that, conditionally on \(xy\), the variable \(x\) is uniform on the units, and that this fails if \(x,y\) are uniform on all residues and \(Q\) is not prime.

**6.3.** Check the three identities preceding Lemma 3.1 from \(sP=vH_R-wH_L\).

**6.4.** In Lemma 4.1, give an example of two proportional triples \((v,w,P)\), \((2v,2w,2P)\) that satisfy \(sP=vH_R-wH_L\) and \(s(2P)=2vH_R-2wH_L\), and say which condition excludes the second.

## 7. Solutions

**6.1.** With \(x=y+t\), the sum is \(e_p(wt)\,\mathbb E_y\lambda(y)e_p(wy)\). If \(w=0\) this is the mean of a nonprincipal character, \(0\). If \(w\ne0\), put \(y=y'\overline w\): \(\sum_y\lambda(y)e_p(wy)\)\(=\sum_{y'}\lambda(y'\overline w)e_p(y')=\lambda(\overline w)\tau(\lambda)\)\(=\lambda(w)^{-1}\tau(\lambda)\). Dividing by \(p\) gives (1.1).

**6.2.** The map \((x,y)\mapsto(x,xy)\) is a bijection of \((\mathbb Z/Q)^\times\times(\mathbb Z/Q)^\times\), so \((x,xy)\) is uniform on pairs of units and \(x\) is independent of \(xy\). For \(Q=4\) and uniform residues, \(xy=1\) forces \(x\in\{1,3\}\), whereas \(x\) is uniform on four residues, so \(x\) is not independent of \(xy\).

**6.3.** Modulo a prime \(p_i\mid H_L\), \(sP\equiv vH_R\), so \(v/P\equiv s/H_R\). Modulo \(p_i\mid H_R\), \(sP\equiv-wH_L\), so \(-w/P\equiv s/H_L\). Finally \(\frac v{PH_L}-\frac w{PH_R}=\frac{vH_R-wH_L}{PH_LH_R}=\frac{sP}{PH_LH_R}\).

**6.4.** If \((v,w,P)\) is valid, so is \((2v,2w,2P)\) as far as the equation goes. The second is excluded because \(2\) divides both the inserted pivot \(2P\) and the frequencies \(2v,2w\) below it, contradicting the coprimality of inserted pivots and frequencies.

## Sources

- [OpenAI-013] OpenAI, *The additive indecomposability of the primes*, OpenAI Math Release preprint, 24 September 2026, Section 4: templates and the transfer identity, (4.5)–(4.10). https://github.com/openai/math/tree/main/preprints/the-additive-indecomposability-of-the-primes-September-24-2026
