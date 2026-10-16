# Monge plans at infinitesimal resolution

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

For the density \(\mu\) of [Two branches with a shared potential](two-branches-with-a-shared-potential.md), pairs of measure-preserving maps come within every \(\epsilon>0\) of the Kantorovich value (Theorem 4.1 of [Monge plans approach the minimum](monge-plans-approach-the-minimum.md)), no pair attains it, and the optimal coupling \(\pi_0\) is not given by maps (Theorem 4.2 of [Two branches with a shared potential](two-branches-with-a-shared-potential.md)). Abraham Robinson's nonstandard analysis gives infinitesimals a rigorous meaning [Keisler]. In its language these facts become statements about a single object: an internal pair of maps, built at an infinitely fine resolution, preserves \(\mu\), exceeds the minimum by a positive infinitesimal, and has the coupling \(\pi_0\) as its standard part (Theorem 3.2). Each central point outside an internal null set is sent to one place, infinitely close to one of four branch points; which branch is followed changes at infinitesimal scale, and at every standard resolution a quarter of the central mass follows each branch (Section 4). The hyperreal numbers are built from an ultrafilter in Section 1, so every step is proved from Zorn's lemma, elementary measure theory and the earlier lessons.

## 1. Hyperreal numbers

Write \(\mathbb N=\{1,2,3,\dots\}\).

**Definition 1.1.** A *filter* on \(\mathbb N\) is a family \(\mathcal F\) of subsets of \(\mathbb N\) such that \(\mathbb N\in\mathcal F\), \(\varnothing\notin\mathcal F\), every set containing a member is a member, and the intersection of two members is a member. An *ultrafilter* is a filter \(\mathcal U\) such that, for every \(A\subseteq\mathbb N\), either \(A\in\mathcal U\) or \(\mathbb N\setminus A\in\mathcal U\); not both, since their intersection is empty. It is *nonprincipal* if it contains every subset of \(\mathbb N\) with finite complement.

**Lemma 1.2.** There is a nonprincipal ultrafilter on \(\mathbb N\).

**Proof.** The subsets of \(\mathbb N\) with finite complement form a filter, because \(\mathbb N\) is infinite. Let \(\mathfrak F\) be the set of filters that contain all of them, ordered by inclusion. The union of a nonempty chain in \(\mathfrak F\) belongs to \(\mathfrak F\): two of its members lie in a common filter of the chain, which contains their intersection. By Zorn's lemma \(\mathfrak F\) has a maximal element \(\mathcal U\). Let \(A\subseteq\mathbb N\). If \(F\cap A\neq\varnothing\) for every \(F\in\mathcal U\), then the sets that contain \(F\cap A\) for some \(F\in\mathcal U\) form a filter containing \(\mathcal U\) and \(A\); by maximality it equals \(\mathcal U\), so \(A\in\mathcal U\). Otherwise some \(F\in\mathcal U\) is disjoint from \(A\), and \(\mathbb N\setminus A\), which contains \(F\), lies in \(\mathcal U\). \(\square\)

Fix a nonprincipal ultrafilter \(\mathcal U\). A statement about \(n\) holds *for \(\mathcal U\)-most \(n\)* if the set of \(n\) for which it holds belongs to \(\mathcal U\). Two statements that each hold for \(\mathcal U\)-most \(n\) hold together for \(\mathcal U\)-most \(n\), and a statement that fails for only finitely many \(n\) holds for \(\mathcal U\)-most \(n\). If finitely many statements are given, exactly one of which holds for each \(n\), then exactly one of them holds for \(\mathcal U\)-most \(n\): two disjoint sets are never both in \(\mathcal U\), and if none of the sets were in \(\mathcal U\), all their complements would be, and so would the intersection of the complements, which is empty.

**Definition 1.3.** Let \(S\) be a nonempty set. Two sequences \((x_n)\) and \((y_n)\) in \(S\) are *equivalent* if \(x_n=y_n\) for \(\mathcal U\)-most \(n\). The set of equivalence classes is written \({}^*S\), and the class of \((x_n)\) is written \([x_n]\). An element \(x\in S\) is identified with the class of the constant sequence; distinct elements give distinct classes, so \(S\subseteq{}^*S\). A map \(f\colon S\to S'\) extends to the map \({}^*f\colon{}^*S\to{}^*S'\) with \({}^*f([x_n])=[f(x_n)]\). Elements of \({}^*\mathbb R\) are *hyperreal numbers*, and elements of \({}^*\mathbb N\) are *hypernatural numbers*. For a sequence \(a=(a_m)\) of real numbers and \(M=[m_n]\in{}^*\mathbb N\), write \(a_M={}^*a(M)=[a_{m_n}]\).

The relation is an equivalence relation because two statements that hold for \(\mathcal U\)-most \(n\) hold together, and \({}^*f\) is well defined for the same reason. On \({}^*\mathbb R\) define \([x_n]+[y_n]=[x_n+y_n]\) and \([x_n][y_n]=[x_ny_n]\), and \([x_n]<[y_n]\) if \(x_n<y_n\) for \(\mathcal U\)-most \(n\).

**Lemma 1.4.** With these operations \({}^*\mathbb R\) is an ordered field containing \(\mathbb R\) as an ordered subfield.

**Proof.** The operations and the order are well defined. Each identity among the field axioms holds for every \(n\), hence in \({}^*\mathbb R\). If \([x_n]\neq0\), then \(x_n\neq0\) for \(\mathcal U\)-most \(n\), and the class of the sequence with \(y_n=1/x_n\) for these \(n\) and \(y_n=0\) otherwise is an inverse. For each \(n\) exactly one of \(x_n<y_n\), \(x_n=y_n\), \(x_n>y_n\) holds, so exactly one of \([x_n]<[y_n]\), \([x_n]=[y_n]\), \([x_n]>[y_n]\) holds. Transitivity, and the compatibility of the order with addition and with multiplication by positive elements, hold for \(\mathcal U\)-most \(n\). Constant sequences add, multiply and compare as real numbers. \(\square\)

**Definition 1.5.** A hyperreal number \(a\) is *infinitesimal* if \(|a|<r\) for every real \(r>0\), and *finite* if \(|a|<r\) for some real \(r\). Write \(a\approx b\) if \(a-b\) is infinitesimal. A hypernatural number is *infinite* if it is larger than every natural number.

The class \(N=[n]\) of the sequence \(1,2,3,\dots\) is infinite: for \(m\in\mathbb N\), the inequality \(n>m\) fails for only finitely many \(n\). For every infinite \(M\), the hyperreal number \(1/M\) is a positive infinitesimal: for real \(r>0\) choose a natural number \(m>1/r\); then \(M>m\) and \(1/M<1/m<r\).

**Lemma 1.6** (standard part). Every finite hyperreal number \(a\) is infinitely close to exactly one real number, its *standard part* \(\operatorname{st}(a)\). If \(a\le b\) are finite, then \(\operatorname{st}(a)\le\operatorname{st}(b)\).

**Proof.** The set of real \(r\) with \(r<a\) is nonempty and bounded above, since \(a\) is finite; let \(t\) be its supremum. For real \(r>0\), some element of the set exceeds \(t-r\), so \(t-r<a\); and \(t+r\) is not in the set, so \(a\le t+r\). Hence \(|a-t|\le r\) for every real \(r>0\), and \(a\approx t\). Two real numbers that are infinitely close are equal, which proves uniqueness. If \(\operatorname{st}(a)>\operatorname{st}(b)\), then \(a-b\) is infinitely close to the positive real number \(c=\operatorname{st}(a)-\operatorname{st}(b)\), so \(a-b>c/2>0\), contradicting \(a\le b\). \(\square\)

**Lemma 1.7.** A sequence \((a_m)\) of real numbers converges to \(L\) if and only if \(a_M\approx L\) for every infinite hypernatural number \(M\).

**Proof.** Suppose that \(a_m\to L\). Let \(M=[m_n]\) be infinite and \(r>0\) real, and choose \(m_0\) with \(|a_m-L|<r\) for \(m\ge m_0\). Since \(M>m_0\), we have \(m_n>m_0\) for \(\mathcal U\)-most \(n\), and for these \(n\), \(|a_{m_n}-L|<r\). So \(|a_M-L|<r\). Conversely, if \((a_m)\) does not converge to \(L\), there are a real \(r>0\) and indices \(m_1<m_2<\cdots\) with \(|a_{m_n}-L|\ge r\) for all \(n\). Since \(m_n\ge n\), the hypernatural number \(M=[m_n]\) is infinite, and \(|a_M-L|\ge r\). \(\square\)

## 2. Internal Monge pairs

Let \(d\ge2\) and \(s>0\), let \(\mu\), \(\nu\), \(B\), \(\mathcal H=\{Y_1,W_1,Y_2,W_2\}\) and \(\pi_0\) be as in Section 4 of [Two branches with a shared potential](two-branches-with-a-shared-potential.md), and let \(E=\mathcal E_{c_s}(\mu)\). As in the proof of Theorem 4.1 of [Monge plans approach the minimum](monge-plans-approach-the-minimum.md), \(K_0\) is the support of \(\nu\), the sets \(K_1,\dots,K_4\) are its images \(H(K_0)\) under the four branches, \(K=K_0\cup\dots\cup K_4\), and any two of the five compact sets \(K_0,\dots,K_4\) are at distance at least \(\eta>0\). On \(K_0\) the measure \(\mu\) equals \(\nu/3\), and \(\nu(K_0)=1\).

Let \(\mathcal A\) be the set of pairs \((T_2,T_3)\) of Borel maps \(\mathbb R^d\to\mathbb R^d\) that preserve \(\mu\), and for \((T_2,T_3)\in\mathcal A\) let \(J(T_2,T_3)\in[0,\infty]\) be the cost of the Monge plan \((\mathrm{id},T_2,T_3)_\#\mu\):
\[
\begin{aligned}
&J(T_2,T_3)\\
&\quad=\int c_s\bigl(x,T_2(x),T_3(x)\bigr)\,d\mu(x).
\end{aligned}
\]

**Definition 2.1.** An *internal Monge pair* is an element \(\mathcal T=[(T_{2,n},T_{3,n})]\) of \({}^*\mathcal A\). It acts on \({}^*\mathbb R^d\) by \(\mathcal T_2([x_n])=[T_{2,n}(x_n)]\) and \(\mathcal T_3([x_n])=[T_{3,n}(x_n)]\). Write \(J_n=J(T_{2,n},T_{3,n})\). The statement \({}^*J(\mathcal T)>E\) means that \(J_n>E\) for \(\mathcal U\)-most \(n\); if \(J_n<\infty\) for \(\mathcal U\)-most \(n\), then \({}^*J(\mathcal T)=[J_n]\) is a hyperreal number, with any real value in place of \(J_n\) for the remaining \(n\). An *internal Borel set* is a class \(\Sigma=[\Sigma_n]\) of a sequence of Borel sets, with \({}^*\mu(\Sigma)=[\mu(\Sigma_n)]\) and \({}^*\nu(\Sigma)=[\nu(\Sigma_n)]\); a point \([x_n]\in{}^*\mathbb R^d\) lies in \(\Sigma\) if \(x_n\in\Sigma_n\) for \(\mathcal U\)-most \(n\). For a Borel set \(V\), the class of the constant sequence \(V\) is written \({}^*V\). For \(x=[x_n]\) and \(y=[y_n]\) in \({}^*\mathbb R^d\), write \(|x-y|=[|x_n-y_n|]\), and \(x\approx y\) if \(|x-y|\) is infinitesimal. For a bounded Borel function \(\varphi\) on \((\mathbb R^d)^3\), let
\[
\begin{aligned}
\langle\mathcal T,\varphi\rangle&=\bigl[I_n(\varphi)\bigr],\\
I_n(\varphi)&=\int\varphi\bigl(x,T_{2,n}(x),T_{3,n}(x)\bigr)\,d\mu(x).
\end{aligned}
\]
This hyperreal number is finite, with \(|\langle\mathcal T,\varphi\rangle|\le\sup|\varphi|\). A Borel probability measure \(\pi\) on \((\mathbb R^d)^3\) is a *standard part* of \(\mathcal T\) if \(\langle\mathcal T,\varphi\rangle\approx\int\varphi\,d\pi\) for every bounded continuous function \(\varphi\).

Since \(I_n(\varphi)=\int\varphi\,d\pi_n\) for the Monge plan \(\pi_n=(\mathrm{id},T_{2,n},T_{3,n})_\#\mu\), a standard part is a coupling that the internal plans approximate up to infinitesimals, tested against continuous functions.

**Lemma 2.2.** An internal Monge pair has at most one standard part.

**Proof.** Let \(\pi\) and \(\pi'\) be standard parts. For every bounded continuous \(\varphi\), the real numbers \(\int\varphi\,d\pi\) and \(\int\varphi\,d\pi'\) are infinitely close to \(\langle\mathcal T,\varphi\rangle\), hence to each other, hence equal. For a closed set \(C\subseteq(\mathbb R^d)^3\), the continuous functions \(\varphi_k(y)=\max\bigl(0,1-k\operatorname{dist}(y,C)\bigr)\) take values in \([0,1]\) and decrease to the indicator function of \(C\) as \(k\to\infty\), because \(\operatorname{dist}(y,C)>0\) for \(y\notin C\). By dominated convergence (core course [Measure and Integration](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-D10); [Fremlin, *Measure Theory*, Volume 1, 123C](https://www1.essex.ac.uk/maths/people/fremlin/chap12.pdf)), \(\pi(C)=\pi'(C)\). Closed sets are closed under finite intersections and generate the Borel \(\sigma\)-algebra, so \(\pi=\pi'\) ([Fremlin, *Measure Theory*, Volume 1, Corollary 136C](https://www1.essex.ac.uk/maths/people/fremlin/chap13.pdf)). \(\square\)

## 3. The theorem in infinitesimal form

For \(H\in\mathcal H\) and real \(\delta>0\), let \(\omega_H(\delta)\) be the supremum of \(|H(x)-H(x')|\) over \(x,x'\in K_0\) with \(|x-x'|\le\delta\). Since \(H\) is uniformly continuous on the compact set \(K_0\), \(\omega_H(\delta)\to0\) as \(\delta\to0\).

**Lemma 3.1.** For every real \(\delta>0\) there are a pair \((T^\delta_2,T^\delta_3)\in\mathcal A\) and finitely many disjoint Borel sets, the *cells*, each of diameter at most \(\delta\) and contained in one of \(K_0,\dots,K_4\), which together cover \(\mu\)-almost all of \(K\), with the following properties. Write \(\pi_\delta=(\mathrm{id},T^\delta_2,T^\delta_3)_\#\mu\).

1. \(E<J(T^\delta_2,T^\delta_3)\) and \(J(T^\delta_2,T^\delta_3)\le E+6s\delta\eta^{-s-1}\).
2. \(\pi_\delta\) and \(\pi_0\) are carried by \(K^3\), and they give the same mass to every product \(A\times A'\times A''\) of three cells.
3. For \(\mu\)-almost every \(x\in K_0\) there is \(H\in\mathcal H\) with \(T^\delta_2(x)\in H(K_0)\) and \(|T^\delta_2(x)-H(x)|\le\delta+\omega_H(\delta)\).
4. For every cell \(A\subseteq K_0\) and every \(H\in\mathcal H\), the set of \(x\in A\) with \(T^\delta_2(x)\in H(K_0)\) has \(\mu\)-measure \(\nu(A)/12\).

**Proof.** Take the cells \(A_1,\dots,A_N\), the masses \(q_{ijk}=\pi_0(A_i\times A_j\times A_k)\), the sets \(B_{ijk}\) and the maps \(T_2,T_3\) of the proof of Theorem 4.1 of [Monge plans approach the minimum](monge-plans-approach-the-minimum.md) for this \(\delta\), and put \(T^\delta_2=T_2\), \(T^\delta_3=T_3\). Property 1 is the cost estimate of that proof together with Theorem 4.2 of [Two branches with a shared potential](two-branches-with-a-shared-potential.md).

*Property 2.* The triples of \(\pi_0\) are the permutations of \((x,Y_k(x),W_k(x))\) with \(x\in K_0\), so \(\pi_0\) is carried by \(K^3\). Its marginals are \(\mu\) and the cells cover \(\mu\)-almost all of \(K\), so \(\pi_0\) is carried by the union of the products of cells. For every active triple \((i,j,k)\) the maps send \(B_{ijk}\) into \(A_j\) and \(A_k\), and the sets \(B_{ijk}\) cover \(A_i\); the remaining points form a \(\mu\)-null set. So \(\pi_\delta\) is carried by the union of the active products and gives each of them the mass \(\mu(B_{ijk})=q_{ijk}\). Both measures give the other products mass zero.

*Properties 3 and 4.* Let \(A_i\subseteq K_0\) and let \((i,j,k)\) be active. In \(\pi_0\), a triple whose first entry lies in \(K_0\) has the form \((x',H(x'),H'(x'))\) with \(x'\in K_0\) and \(\{H,H'\}=\{Y_l,W_l\}\) for some \(l\), because the branch points lie outside \(K_0\). Since \(\pi_0(A_i\times A_j\times A_k)>0\), there is such a triple with \(x'\in A_i\) and \(H(x')\in A_j\). The cell \(A_j\) lies in a single one of the five sets, which is therefore \(H(K_0)\). For \(x\in B_{ijk}\), both \(T_2(x)\) and \(H(x')\) lie in \(A_j\), and both \(x\) and \(x'\) lie in \(A_i\), so
\[
\begin{aligned}
|T_2(x)-H(x)|&\le|T_2(x)-H(x')|\\
&\quad+|H(x')-H(x)|\\
&\le\delta+\omega_H(\delta).
\end{aligned}
\]
The sets \(B_{ijk}\) with \(A_i\subseteq K_0\) and \((i,j,k)\) active cover \(\mu\)-almost all of \(K_0\), which proves property 3. Up to a \(\mu\)-null set, the points \(x\in A_i\) with \(T_2(x)\in H(K_0)\) form the union of the sets \(B_{ijk}\) with \(A_j\subseteq H(K_0)\), whose measure is the sum of the corresponding \(q_{ijk}\). Since the cells in \(H(K_0)\) cover \(\mu\)-almost all of \(H(K_0)\), this sum is the \(\pi_0\)-probability that the first entry lies in \(A_i\) and the second in \(H(K_0)\). In the construction of \(\pi_0\), the first entry is the central point \(x\) with probability \(\frac13\), independently of \(x\); given this, the second entry is \(H(x)\) with probability \(\frac14\), since the branch index is uniform and the random permutation puts each of the two branch points second with probability \(\frac12\). The probability is therefore \(\frac13\cdot\frac14\,\nu(A_i)=\nu(A_i)/12\). \(\square\)

**Theorem 3.2.** Let \(M=[m_n]\) be an infinite hypernatural number, let \(\delta_n=1/m_n\), and let \(\mathcal T\) be the internal Monge pair \([(T^{\delta_n}_2,T^{\delta_n}_3)]\).

1. Every internal Monge pair \(\mathcal S\) satisfies \({}^*J(\mathcal S)>E\).
2. \(0<{}^*J(\mathcal T)-E\le6s\eta^{-s-1}/M\); in particular \({}^*J(\mathcal T)\approx E\).
3. The coupling \(\pi_0\) is the standard part of \(\mathcal T\).
4. The coupling \(\pi_0\) is not a Monge plan.

**Proof.** *1.* For every \(n\), the pair \((S_{2,n},S_{3,n})\) preserves \(\mu\), so its energy exceeds \(E\) by Theorem 4.2 of [Two branches with a shared potential](two-branches-with-a-shared-potential.md).

*2.* By property 1 of Lemma 3.1, \(0<J(T^{\delta_n}_2,T^{\delta_n}_3)-E\le6s\eta^{-s-1}\delta_n\) for every \(n\), which is the asserted inequality in \({}^*\mathbb R\). Since \(1/M\) is infinitesimal, so is \({}^*J(\mathcal T)-E\).

*3.* Let \(\varphi\) be bounded and continuous, and let \(\omega_\varphi(\delta)\) be the supremum of \(|\varphi(y)-\varphi(y')|\) over triples \(y,y'\in K^3\) whose corresponding entries are at distance at most \(\delta\). By property 2 of Lemma 3.1, \(\pi_\delta\) and \(\pi_0\) are carried by the products of cells, and give each product the same mass \(q\). On a product \(P\) the entries of any two triples are within \(\delta\) of each other, and both integrals of \(\varphi\) over \(P\) lie between \(q\inf_P\varphi\) and \(q\sup_P\varphi\). Summing over the products,
\[
\Bigl|\int\varphi\,d\pi_\delta-\int\varphi\,d\pi_0\Bigr|\le\omega_\varphi(\delta).
\]
The function \(\varphi\) is uniformly continuous on the compact set \(K^3\), so \(a_m=\omega_\varphi(1/m)\) tends to \(0\). Since \(I_n(\varphi)=\int\varphi\,d\pi_{\delta_n}\), Lemma 1.7 gives \(|\langle\mathcal T,\varphi\rangle-\int\varphi\,d\pi_0|\le a_M\approx0\). Uniqueness is Lemma 2.2.

*4.* If \(\pi_0=(\mathrm{id},F_2,F_3)_\#\mu\) for Borel maps \(F_2,F_3\), these preserve \(\mu\), since the marginals of \(\pi_0\) are \(\mu\), and their energy is \(\int c_s\,d\pi_0=E\), contradicting Theorem 4.2 of [Two branches with a shared potential](two-branches-with-a-shared-potential.md). \(\square\)

Statement 1 is nonattainment in internal form: infinitesimals do not create a Monge optimizer. Statement 2 is Theorem 4.1 of [Monge plans approach the minimum](monge-plans-approach-the-minimum.md) in internal form, with the error bound evaluated at \(\delta=1/M\). Statements 3 and 4 locate the missing optimizer: the internal plan is given by maps, and its standard part is optimal but not given by maps. In the language of sequences, statement 3 for every infinite \(M\) says, by Lemma 1.7, that \(\int\varphi\,d\pi_{1/m}\to\int\varphi\,d\pi_0\) for every bounded continuous \(\varphi\): the Monge plans \(\pi_{1/m}\) converge narrowly to \(\pi_0\).

**Proposition 3.3** (internal mass imbalance). Let \(\mathcal S=[(S_{2,n},S_{3,n})]\) be an internal Monge pair, let \(H\in\mathcal H\), and let \(\Sigma=[\Sigma_n]\) with \(\Sigma_n=\{x\in B:S_{2,n}(x)=H(x)\}\). Then \({}^*\nu(\Sigma)=0\).

**Proof.** For each \(n\), the proof of Lemma 3.1 of [Couplings and supporting potentials](couplings-and-supporting-potentials.md), applied to the map \(S_{2,n}\), gives \(\frac13\nu(\Sigma_n)\le\frac16\nu(\Sigma_n)\), so \(\nu(\Sigma_n)=0\). \(\square\)

The inequality \(\frac13a\le\frac16a\) forces \(a\le0\) in every ordered field. The selection obstruction therefore excludes positive infinitesimal masses as well: an internal map cannot follow a branch exactly on any internal set of positive measure, however small.

## 4. Where the determinism goes

Let \(M\), \(\delta_n\) and \(\mathcal T\) be as in Theorem 3.2. For a real number \(r>0\) and \(H\in\mathcal H\) let \(S_H(r)=[S_{H,n}(r)]\), where \(S_{H,n}(r)\) is the set of \(x\in K_0\) with \(|T^{\delta_n}_2(x)-H(x)|<r\).

**Proposition 4.1.** (a) There is an internal Borel set \(Z\) with \({}^*\mu(Z)=0\) such that for every \(x\in{}^*K_0\) outside \(Z\) some \(H\in\mathcal H\) satisfies \(\mathcal T_2(x)\approx{}^*H(x)\).

(b) Let \(0<r\le\eta\) be real, let \(H\in\mathcal H\), and let \(\psi\) be a bounded continuous function on \(\mathbb R^d\). Then
\[
\Bigl[\int_{S_{H,n}(r)}\psi\,d\mu\Bigr]\approx\frac1{12}\int\psi\,d\nu .
\]
In particular \({}^*\mu(S_H(r))\approx\frac1{12}\).

**Proof.** (a) Let \(Z_n\) be the \(\mu\)-null set of points of \(K_0\) at which property 3 of Lemma 3.1 fails for \(\delta=\delta_n\), and \(Z=[Z_n]\). Let \(x=[x_n]\in{}^*K_0\) lie outside \(Z\), so that \(x_n\in K_0\setminus Z_n\) for \(\mathcal U\)-most \(n\). For these \(n\) choose \(H_n\in\mathcal H\) as in property 3. There are four branches, so one of them, \(H\), equals \(H_n\) for \(\mathcal U\)-most \(n\), and then
\[
|\mathcal T_2(x)-{}^*H(x)|\le[\delta_n+\omega_H(\delta_n)].
\]
The right side is the value at \(M\) of the sequence \(1/m+\omega_H(1/m)\), which tends to \(0\); by Lemma 1.7 it is infinitesimal.

(b) Let \(\delta>0\) satisfy \(\delta+\omega_H(\delta)<r\), let \(S=\{x\in K_0:|T^\delta_2(x)-H(x)|<r\}\), and let \(A\subseteq K_0\) be a cell. By property 3 of Lemma 3.1, for \(\mu\)-almost every \(x\in A\) there is \(H'\in\mathcal H\) with \(T^\delta_2(x)\in H'(K_0)\) and \(|T^\delta_2(x)-H'(x)|<r\). If \(H'=H\), then \(x\in S\). If \(H'\neq H\), then \(T^\delta_2(x)\) and \(H(x)\) lie in two different sets among \(K_1,\dots,K_4\), so \(|T^\delta_2(x)-H(x)|\ge\eta\ge r\) and \(x\notin S\). Hence, up to a \(\mu\)-null set, \(S\cap A\) is the set of \(x\in A\) with \(T^\delta_2(x)\in H(K_0)\), which has measure \(\nu(A)/12\) by property 4. Both \(\int_{S\cap A}\psi\,d\mu\) and \(\frac1{12}\int_A\psi\,d\nu\) lie between \(\frac{\nu(A)}{12}\inf_A\psi\) and \(\frac{\nu(A)}{12}\sup_A\psi\). The cells in \(K_0\) cover \(\nu\)-almost all of \(K_0\), and \(\nu(K_0)=1\). Summing over these cells,
\[
\Bigl|\int_S\psi\,d\mu-\frac1{12}\int\psi\,d\nu\Bigr|\le\frac{\omega_\psi(\delta)}{12},
\]
where \(\omega_\psi(\delta)\) is the supremum of \(|\psi(x)-\psi(x')|\) over \(x,x'\in K_0\) with \(|x-x'|\le\delta\). By Lemma 1.7, applied to the sequence \(1/m+\omega_H(1/m)\), which tends to \(0\), the inequality \(\delta_n+\omega_H(\delta_n)<r\) holds for \(\mathcal U\)-most \(n\). For these \(n\) the estimate holds with \(\delta=\delta_n\), and \(\omega_\psi(1/m)\to0\) by uniform continuity of \(\psi\) on \(K_0\). Lemma 1.7 gives the claim. The last statement is the case \(\psi=1\). \(\square\)

**Corollary 4.2.** Let \(0<r\le\eta\) be real, let \(H\in\mathcal H\), and let \(V\subseteq\mathbb R^d\) be open with \(\nu(V)>0\). Then \({}^*\mu\bigl(S_H(r)\cap{}^*V\bigr)\) is positive and not infinitesimal.

Here \(S_H(r)\cap{}^*V=[S_{H,n}(r)\cap V]\).

**Proof.** The open set \(V\) is the union of the countably many closed balls with rational centres and rational radii that it contains, so one of them, \(C\), has \(\nu(C)>0\). Since \(C\) is compact and \(V\) is open, there is a real \(\rho>0\) such that every point at distance at most \(\rho\) from \(C\) lies in \(V\). The function \(\psi(x)=\max\bigl(0,1-\operatorname{dist}(x,C)/\rho\bigr)\) is continuous, equal to \(1\) on \(C\), and \(0\le\psi\le\mathbf 1_V\). By Proposition 4.1,
\[
\begin{aligned}
{}^*\mu\bigl(S_H(r)\cap{}^*V\bigr)&\ge\Bigl[\int_{S_{H,n}(r)}\psi\,d\mu\Bigr]\\
&\approx\frac1{12}\int\psi\,d\nu\ge\frac{\nu(C)}{12},
\end{aligned}
\]
so \({}^*\mu(S_H(r)\cap{}^*V)>\nu(C)/24\). \(\square\)

Together with Proposition 3.3 this describes the internal map \(\mathcal T_2\) on the central points. It sends each central point outside an internal null set to a single place, infinitely close to one of the four branch points (Proposition 4.1(a)), and it never coincides with a branch on an internal set of positive measure (Proposition 3.3). Inside every standard open set charged by \(\nu\), each of the four branches is followed on a part of mass that is not infinitesimal, and the proportions are \(\frac14\) each (Proposition 4.1(b) and Corollary 4.2). The choice of branch thus varies at infinitesimal scale. Taking standard parts keeps only the proportions, which form the conditional law of \(\pi_0\) at a central point: the four ordered pairs \((Y_k(x),W_k(x))\) and \((W_k(x),Y_k(x))\), \(k=1,2\), each with probability \(\frac14\).

## 5. Exercises

**Exercise 5.1** (easy). Let \(m_0\in\mathbb N\). Show that \(\{A\subseteq\mathbb N:m_0\in A\}\) is an ultrafilter that is not nonprincipal, and that with it the construction of Definition 1.3 gives \({}^*\mathbb R=\mathbb R\).

**Exercise 5.2** (easy). Let \(a\) and \(b\) be finite hyperreal numbers. Show that \(a+b\) and \(ab\) are finite, that \(\operatorname{st}(a+b)=\operatorname{st}(a)+\operatorname{st}(b)\), and that \(\operatorname{st}(ab)=\operatorname{st}(a)\operatorname{st}(b)\).

**Exercise 5.3** (easy). Show that a hyperreal number \(a\ge0\) with \(\frac13a\le\frac16a\) is \(0\).

**Exercise 5.4** (medium). Show that the set of Monge plans of \(\mu\) is not closed under narrow convergence: there are Monge plans \(\pi_m\) with \(\int\varphi\,d\pi_m\to\int\varphi\,d\pi_0\) for every bounded continuous \(\varphi\), and \(\pi_0\) is not a Monge plan.

**Exercise 5.5** (medium). Let \(0<r\le\eta/2\) be real. Show that the four internal sets \(S_H(r)\), \(H\in\mathcal H\), are pairwise disjoint, and that \({}^*\mu\bigl({}^*K_0\setminus\bigcup_{H\in\mathcal H}S_H(r)\bigr)\approx0\).

**Exercise 5.6** (medium). Show that the standard part \(\operatorname{st}\langle\mathcal T,\varphi\rangle\) in Theorem 3.2 does not depend on the nonprincipal ultrafilter \(\mathcal U\) or on the infinite hypernatural number \(M\), and compute it.

## 6. Solutions

**5.1.** The family contains \(\mathbb N\), not \(\varnothing\), is closed under supersets and intersections, and contains exactly one of \(A\) and \(\mathbb N\setminus A\); it does not contain \(\mathbb N\setminus\{m_0\}\), whose complement is finite. For a sequence \((x_n)\), the statement \(x_n=x_{m_0}\) holds for \(n=m_0\), so \([x_n]\) is the class of the constant sequence \(x_{m_0}\), a real number.

**5.2.** Write \(a=\operatorname{st}(a)+\epsilon\) and \(b=\operatorname{st}(b)+\epsilon'\) with \(\epsilon,\epsilon'\) infinitesimal. For real \(r>0\), \(|\epsilon+\epsilon'|<r/2+r/2\), so \(a+b\approx\operatorname{st}(a)+\operatorname{st}(b)\). A finite number times an infinitesimal is infinitesimal: if \(|c|<R\) and \(|\epsilon|<r/R\), then \(|c\epsilon|<r\). Hence \(ab-\operatorname{st}(a)\operatorname{st}(b)=\operatorname{st}(a)\epsilon'+\operatorname{st}(b)\epsilon+\epsilon\epsilon'\) is infinitesimal. Both sums are within \(1\) of real numbers, hence finite.

**5.3.** \(\frac13a-\frac16a=\frac16a\le0\) gives \(a\le0\), so \(a=0\). Only the ordered field axioms are used, and they hold in \({}^*\mathbb R\) by Lemma 1.4.

**5.4.** Take \(\pi_m=\pi_{1/m}\) from Lemma 3.1. The estimate \(|\int\varphi\,d\pi_\delta-\int\varphi\,d\pi_0|\le\omega_\varphi(\delta)\) in the proof of Theorem 3.2 and \(\omega_\varphi(1/m)\to0\) give the convergence, and \(\pi_0\) is not a Monge plan by statement 4 of Theorem 3.2.

**5.5.** If \(x\in S_{H,n}(r)\cap S_{H',n}(r)\) with \(H\neq H'\), then \(|H(x)-H'(x)|<2r\le\eta\), although \(H(x)\) and \(H'(x)\) lie in two different sets among \(K_1,\dots,K_4\); so the sets are disjoint for every \(n\). By Proposition 4.1(b), each \({}^*\mu(S_H(r))\approx\frac1{12}\), so their union has measure \(\approx\frac13={}^*\mu({}^*K_0)\), and the complement in \({}^*K_0\) has infinitesimal measure.

**5.6.** By statement 3 of Theorem 3.2 and Lemma 1.6, \(\operatorname{st}\langle\mathcal T,\varphi\rangle=\int\varphi\,d\pi_0\), whatever \(\mathcal U\) and \(M\) are.

## References

- [Keisler] H. J. Keisler, *Foundations of Infinitesimal Calculus*, author's edition, 2007, revised 2022; Sections 1B (standard parts) and 1G (the ultrapower construction). https://people.math.wisc.edu/~hkeisler/foundations.pdf
- [OpenAI-CM] OpenAI, *A counterexample to the Monge ansatz for the three-marginal Coulomb cost*, OpenAI Math Release preprint, 25 September 2026. https://github.com/openai/math/tree/main/preprints/A-counterexample-to-the-Monge-ansatz-for-the-three-marginal-Coulomb-cost-September-25-2026
- [Fremlin] D. H. Fremlin, *Measure Theory*, Volume 1, author's edition. https://www1.essex.ac.uk/maths/people/fremlin/mt.htm
