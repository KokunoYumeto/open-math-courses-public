# Monge plans approach the minimum

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

By Theorem 4.2 of [Two branches with a shared potential](two-branches-with-a-shared-potential.md), the density \(\mu\) constructed there admits no Monge optimizer for the Riesz cost \(c_s\). This lesson shows that the Monge value nevertheless equals the Kantorovich value (Theorem 4.1): measure-preserving maps come arbitrarily close to the minimum without reaching it. For the Coulomb cost and every density without atoms, Colombo and Di Marino proved this equality with cyclic maps [CDM]. For the density of the previous lesson the components are separated from each other, and OpenAI gives a direct proof [OpenAI-CM, Sections 6 and 7] that adapts the cell argument of [CDM, Lemma 2.3]: cut the support into small cells, and transport each cell, piece by piece, so that every product of three cells receives the same mass as under an optimal coupling. The pieces are moved by Borel maps between absolutely continuous measures, constructed in Section 2 from the successive conditional distribution functions of Rosenblatt [Rosenblatt].

Notation is as in [Couplings and supporting potentials](couplings-and-supporting-potentials.md). Integrals of nonnegative Borel functions over products are computed by Tonelli's theorem, and Lebesgue measure of a hyperplane is zero (core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10); [Fremlin, *Measure Theory*, Volume 2, Theorem 252B and Corollary 252H](https://www1.essex.ac.uk/maths/people/fremlin/cont25.htm)).

## 1. Distribution functions

A *continuous distribution function* is a continuous nondecreasing function \(F\colon\mathbb R\to[0,1]\) with limits \(0\) at \(-\infty\) and \(1\) at \(+\infty\).

**Lemma 1.1.** Let \(R\) be a real random variable whose distribution function \(F(t)=\mathbb P(R\le t)\) is continuous. Then \(F(R)\) is uniformly distributed on \([0,1]\).

**Proof.** Let \(0<u<1\). By continuity and the limits of \(F\), the set \(\{t:F(t)=u\}\) is nonempty, closed and bounded above; let \(t_u\) be its largest element. Since \(F\) is nondecreasing, \(F(t)\le u\) exactly when \(t\le t_u\), so \(\mathbb P(F(R)\le u)=\mathbb P(R\le t_u)=F(t_u)=u\). \(\square\)

**Lemma 1.2.** Let \(F\) be a continuous distribution function, and for \(0<u<1\) let \(q(u)=\inf\{r\in\mathbb Q:F(r)\ge u\}\). Then \(q(u)\) is a real number, and
\[
q(u)\le t\iff u\le F(t)\qquad(t\in\mathbb R).
\]
Consequently, if \(U\) is uniform on \((0,1)\), then \(q(U)\) has distribution function \(F\).

**Proof.** The set of rationals \(r\) with \(F(r)\ge u\) is nonempty because \(F\to1\), and bounded below because \(F\to0\). If \(u\le F(t)\), then \(F(r)\ge u\) for every rational \(r>t\), so \(q(u)\le t\). If \(q(u)\le t\), then for every \(\epsilon>0\) some rational \(r<t+\epsilon\) has \(F(r)\ge u\), so \(F(t+\epsilon)\ge u\), and \(F(t)\ge u\) by continuity. Finally \(\mathbb P(q(U)\le t)=\mathbb P(U\le F(t))=F(t)\). \(\square\)

## 2. Transport between absolutely continuous measures

Let \(f\ge0\) be a Borel function on \(\mathbb R^d\) with \(\int f=1\). For \(1\le j<d\) and \(x\in\mathbb R^d\) write \(x_{1:j}=(x_1,\dots,x_j)\), and let
\[
f_{1:j}(x_{1:j})=\int_{\mathbb R^{d-j}}f(x_{1:j},z)\,dz,\qquad f_{1:d}=f,\qquad f_{1:0}=1 .
\]
By Tonelli's theorem these are Borel functions with values in \([0,\infty]\), \(f_{1:j}\) is the density of the first \(j\) coordinates of a random vector with density \(f\), and \(\int_{\mathbb R}f_{1:j}(a,r)\,dr=f_{1:j-1}(a)\) for every \(a\in\mathbb R^{j-1}\). For \(1\le j\le d\), \(a\in\mathbb R^{j-1}\) and \(t\in\mathbb R\) let
\[
F_j(a,t)=\frac1{f_{1:j-1}(a)}\int_{-\infty}^tf_{1:j}(a,r)\,dr\qquad\text{if }0<f_{1:j-1}(a)<\infty,
\]
and \(F_j(a,t)=(1+\mathrm e^{-t})^{-1}\) otherwise. Each \(F_j(a,\cdot)\) is a continuous distribution function (the integral of an integrable function is continuous in its upper limit), and \(F_j\) is Borel in \((a,t)\) by Tonelli's theorem. The *exceptional* prefixes, those with \(f_{1:j-1}(a)\in\{0,\infty\}\), carry no mass: the measure \(f_{1:j-1}(a)\,da\) of the set where \(f_{1:j-1}=0\) is zero, and the set where \(f_{1:j-1}=\infty\) is Lebesgue-null because \(f_{1:j-1}\) is integrable.

**Lemma 2.1** (Rosenblatt's transform). The Borel map
\[
R_f(x)=\bigl(F_1(x_1),\,F_2(x_1,x_2),\,\dots,\,F_d(x_{1:d-1},x_d)\bigr),
\]
where \(F_1(t)\) means \(F_1(\varnothing,t)\), sends the measure \(f\,dx\) to the uniform measure on \([0,1]^d\).

**Proof.** Let \(X\) have density \(f\) and \(V_j=F_j(X_{1:j-1},X_j)\). We show that \(V_j\) is uniform on \([0,1]\) and independent of \(X_{1:j-1}\). Let \(A\subseteq\mathbb R^{j-1}\) be Borel and \(0\le u\le1\). By Tonelli's theorem,
\[
\mathbb P(X_{1:j-1}\in A,\ V_j\le u)=\int_A\Bigl(\int_{\mathbb R}\mathbf 1\{F_j(a,r)\le u\}\,f_{1:j}(a,r)\,dr\Bigr)da .
\]
For a non-exceptional \(a\), the inner integral is \(f_{1:j-1}(a)\) times the probability that \(F_j(a,R_a)\le u\), where \(R_a\) has density \(f_{1:j}(a,\cdot)/f_{1:j-1}(a)\) and distribution function \(F_j(a,\cdot)\); by Lemma 1.1 this probability is \(u\). If \(f_{1:j-1}(a)=0\), the inner integral is \(0=u\,f_{1:j-1}(a)\), and the prefixes with \(f_{1:j-1}(a)=\infty\) form a null set. Hence the probability equals \(u\int_Af_{1:j-1}(a)\,da=u\,\mathbb P(X_{1:j-1}\in A)\). So \(V_j\) is uniform and independent of \(X_{1:j-1}\), and therefore of \(V_1,\dots,V_{j-1}\), which are functions of \(X_{1:j-1}\). By induction on \(j\), the variables \(V_1,\dots,V_d\) are independent and uniform. \(\square\)

**Lemma 2.2** (inverse transform). For \(0<u<1\) let \(q_j(a,u)=\inf\{r\in\mathbb Q:F_j(a,r)\ge u\}\), and let \(q_j(a,u)=0\) for \(u\in\{0,1\}\). For \(u\in[0,1]^d\) define \(S_f(u)=(z_1,\dots,z_d)\) recursively by \(z_j=q_j(z_{1:j-1},u_j)\). Then \(S_f\) is Borel and sends the uniform measure on \([0,1]^d\) to \(f\,dx\).

**Proof.** For \(0<u<1\) and real \(t\), \(q_j(a,u)<t\) holds exactly when \(F_j(a,r)\ge u\) for some rational \(r<t\); this is a countable union of Borel sets, so \(q_j\) is Borel, and so is the finite recursion \(S_f\). Let \(U\) be uniform on \([0,1]^d\) and \(Z=S_f(U)\). Suppose that \(Z_{1:j-1}\) has density \(f_{1:j-1}\). Since \(U_j\) is independent of \(Z_{1:j-1}\), a function of \(U_1,\dots,U_{j-1}\), Tonelli's theorem and Lemma 1.2 give, for Borel \(A\subseteq\mathbb R^{j-1}\) and real \(t\),
\[
\mathbb P(Z_{1:j-1}\in A,\ Z_j\le t)=\int_A\mathbb P\bigl(q_j(a,U_j)\le t\bigr)f_{1:j-1}(a)\,da=\int_AF_j(a,t)f_{1:j-1}(a)\,da=\int_A\int_{-\infty}^tf_{1:j}(a,r)\,dr\,da,
\]
using that the exceptional prefixes carry no mass. Sets of the form \(A\times(-\infty,t]\) are closed under intersection and generate the Borel sets of \(\mathbb R^j\), so \(Z_{1:j}\) has density \(f_{1:j}\). Induction on \(j\) proves the claim. \(\square\)

**Corollary 2.3.** If \(\alpha=f\,dx\) and \(\beta=g\,dx\) are Borel probability measures on \(\mathbb R^d\) with densities, then \(Q=S_g\circ R_f\) is a Borel map with \(Q_\#\alpha=\beta\).

**Proof.** \(R_{f\#}\alpha\) is uniform on \([0,1]^d\) by Lemma 2.1, and \(S_g\) sends it to \(\beta\) by Lemma 2.2. \(\square\)

## 3. Splitting a set into prescribed masses

**Lemma 3.1.** Let \(\mu\) be a Borel probability measure on \(\mathbb R^d\) with a density, let \(A\) be a Borel set, and let \(m_1,\dots,m_L\ge0\) with \(m_1+\dots+m_L=\mu(A)\). Then \(A\) is the disjoint union of Borel sets \(A_1,\dots,A_L\) with \(\mu(A_l)=m_l\).

**Proof.** The function \(\varphi(t)=\mu(A\cap\{x_1\le t\})\) on \([-\infty,\infty]\), with \(\varphi(-\infty)=0\) and \(\varphi(\infty)=\mu(A)\), is nondecreasing and continuous, because every hyperplane \(\{x_1=t\}\) is Lebesgue-null and hence \(\mu\)-null. Let \(t_0=-\infty\), let \(t_l\) be the least \(t\in[-\infty,\infty]\) with \(\varphi(t)\ge m_1+\dots+m_l\) for \(1\le l<L\), and \(t_L=\infty\). By continuity \(\varphi(t_l)=m_1+\dots+m_l\), and \(t_0\le t_1\le\dots\le t_L\). The slabs \(A_l=A\cap\{t_{l-1}<x_1\le t_l\}\) work. \(\square\)

## 4. The Monge value

Let \(d\ge2\), \(s>0\), and let \(\mu\), \(B\), \(g\), \(\mathcal H=\{Y_1,W_1,Y_2,W_2\}\) and the optimal coupling \(\pi_0\) be as in Section 4 of [Two branches with a shared potential](two-branches-with-a-shared-potential.md).

**Theorem 4.1** (OpenAI 2026). For every \(\epsilon>0\) there are Borel maps \(T_2,T_3\) preserving \(\mu\) with
\[
\mathcal E_{c_s}(\mu)<\int c_s\bigl(x,T_2(x),T_3(x)\bigr)\,d\mu(x)\le\mathcal E_{c_s}(\mu)+\epsilon .
\]
Hence the Monge value \(\mathcal M_{c_s}(\mu)\) equals the Kantorovich value \(\mathcal E_{c_s}(\mu)\), and it is not attained.

**Proof.** *Separated pieces.* Let \(K_0=\operatorname{supp}g\subseteq B\) and let \(K_1,\dots,K_4\) be its images under the four maps of \(\mathcal H\). These are five compact sets inside the five disjoint sets \(B,Y_1(B),W_1(B),Y_2(B),W_2(B)\), so
\[
\eta=\min_{a\neq b}\operatorname{dist}(K_a,K_b)>0,
\]
and \(K=K_0\cup\dots\cup K_4\) has \(\mu(K)=1\). The coupling \(\pi_0\) is carried by triples whose three entries lie in three different sets \(K_a\), namely the permutations of \((x,Y_k(x),W_k(x))\) with \(x\in K_0\).

*Cells.* Fix \(\delta>0\). Cut each \(K_a\) by a grid of half-open cubes of side \(\delta/\sqrt d\) into finitely many Borel cells of diameter at most \(\delta\), and discard the cells of \(\mu\)-measure zero. The remaining cells \(A_1,\dots,A_N\) are disjoint, each lies in a single \(K_a\), and they cover \(\mu\)-almost all of \(K\). Put \(q_{ijk}=\pi_0(A_i\times A_j\times A_k)\). Since \(\pi_0\) is carried by \(K^3\) and has marginals \(\mu\),
\[
\sum_{j,k}q_{ijk}=\mu(A_i),\qquad\sum_{i,k}q_{ijk}=\mu(A_j),\qquad\sum_{i,j}q_{ijk}=\mu(A_k).\tag{4.1}
\]
Call the triple \((i,j,k)\) *active* if \(q_{ijk}>0\). Then \(\pi_0\) charges \(A_i\times A_j\times A_k\), so the three cells lie in three different sets \(K_a\), and every point of this product has its three entries at mutual distances at least \(\eta\).

*Maps.* By (4.1) and Lemma 3.1, each \(A_i\) is the disjoint union of Borel sets \(B_{ijk}\) with \(\mu(B_{ijk})=q_{ijk}\). For active \((i,j,k)\), Corollary 2.3 gives Borel maps sending the probability measure \(q_{ijk}^{-1}\mu|_{B_{ijk}}\) to \(\mu|_{A_j}/\mu(A_j)\) and to \(\mu|_{A_k}/\mu(A_k)\), respectively; changing them on the Borel \(\mu\)-null set of points sent outside \(A_j\), respectively \(A_k\), we may assume that they take values in \(A_j\) and \(A_k\). Let \(T_2\) and \(T_3\) be these maps on each \(B_{ijk}\) with \((i,j,k)\) active, and a fixed point of \(K\) on the remaining \(\mu\)-null Borel set. For a Borel set \(D\), by (4.1),
\[
\mu\bigl(T_2^{-1}(D)\bigr)=\sum_{(i,j,k)\text{ active}}q_{ijk}\,\frac{\mu(D\cap A_j)}{\mu(A_j)}=\sum_j\mu(D\cap A_j)=\mu(D),
\]
and likewise for \(T_3\). So \(T_2\) and \(T_3\) preserve \(\mu\), and the Monge plan \(\pi_\delta=(\mathrm{id},T_2,T_3)_\#\mu\) gives each product \(A_i\times A_j\times A_k\) the mass \(\mu(B_{ijk})=q_{ijk}\), exactly as \(\pi_0\) does.

*Costs.* If \(t,t'\ge\eta\), the mean value theorem gives \(|t^{-s}-t'^{-s}|\le s\eta^{-s-1}|t-t'|\). Let \(x\) and \(y\) be two triples in one active product. Each of their entries moves by at most \(\delta\), so each of the three distances changes by at most \(2\delta\), and
\[
|c_s(x)-c_s(y)|\le6s\delta\,\eta^{-s-1}.
\]
Both \(\pi_0\) and \(\pi_\delta\) are carried by the union of the active products, give each of them the same mass, and \(c_s\le3\eta^{-s}\) there. Comparing the two integrals product by product,
\[
\Bigl|\int c_s\,d\pi_\delta-\int c_s\,d\pi_0\Bigr|\le6s\delta\,\eta^{-s-1}.
\]
Since \(\int c_s\,d\pi_0=\mathcal E_{c_s}(\mu)\), choosing \(\delta\) with \(6s\delta\eta^{-s-1}\le\epsilon\) gives the upper bound. The cost of every Monge plan is at least \(\mathcal E_{c_s}(\mu)\), and it is strictly larger by Theorem 4.2 of [Two branches with a shared potential](two-branches-with-a-shared-potential.md). \(\square\)

The argument never passes the singular cost to a limit: the approximating plans themselves keep all three particles at distance at least \(\eta\) from each other.

## 5. Exercises

**Exercise 5.1** (easy). For \(d=1\), show that the map of Corollary 2.3 is \(Q=q_G\circ F\), where \(F\) is the distribution function of \(\alpha\) and \(q_G\) the quantile function of \(\beta\), and that it is nondecreasing.

**Exercise 5.2** (easy). Show that Corollary 2.3 fails without densities: if \(\alpha\) is a point mass and \(\beta\) has a density, no map \(Q\) satisfies \(Q_\#\alpha=\beta\).

**Exercise 5.3** (easy). Prove the estimate \(|t^{-s}-t'^{-s}|\le s\eta^{-s-1}|t-t'|\) for \(t,t'\ge\eta>0\).

**Exercise 5.4** (medium). Show that Lemma 3.1 fails for a measure with an atom, and list the places in the proof of Theorem 4.1 where the density of \(\mu\) is used.

## 6. Solutions

**5.1.** For \(d=1\) there are no prefixes: \(R_f=F\) and \(S_g=q_G\), so \(Q=q_G\circ F\). Both \(F\) and \(q_G\) are nondecreasing (if \(u\le u'\), every rational with \(G(r)\ge u'\) also has \(G(r)\ge u\)).

**5.2.** If \(\alpha\) is the point mass at \(p\), then \(Q_\#\alpha\) is the point mass at \(Q(p)\), which gives the single point \(Q(p)\) mass \(1\), while \(\beta\) gives every single point mass \(0\).

**5.3.** The function \(t\mapsto t^{-s}\) has derivative \(-st^{-s-1}\), of absolute value at most \(s\eta^{-s-1}\) on \([\eta,\infty)\); apply the mean value theorem on the interval between \(t\) and \(t'\).

**5.4.** If \(\mu\) is the point mass at \(p\), the set \(\{p\}\) cannot be split into two sets of mass \(\frac12\). In the proof of Theorem 4.1, the density of \(\mu\) is used in Lemma 3.1, to split each cell into pieces of prescribed mass, and in Corollary 2.3, for both the source pieces and the target cells.

## References

- [OpenAI-CM] OpenAI, *A counterexample to the Monge ansatz for the three-marginal Coulomb cost*, OpenAI Math Release preprint, 25 September 2026. https://github.com/openai/math/tree/main/preprints/A-counterexample-to-the-Monge-ansatz-for-the-three-marginal-Coulomb-cost-September-25-2026
- [CDM] M. Colombo and S. Di Marino, *Equality between Monge and Kantorovich multimarginal problems with Coulomb cost*, Annali di Matematica Pura ed Applicata 194 (2015), 307–320; author's version. https://cvgmt.sns.it/paper/2127/
- [Rosenblatt] M. Rosenblatt, *Remarks on a multivariate transformation*, Annals of Mathematical Statistics 23 (1952), 470–472 (open access). https://doi.org/10.1214/aoms/1177729394
- [Fremlin] D. H. Fremlin, *Measure Theory*, Volume 2, author's edition. https://www1.essex.ac.uk/maths/people/fremlin/mt.htm
