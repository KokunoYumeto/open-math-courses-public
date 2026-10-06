# Almost homomorphisms of measured groupoids

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

## Introduction

In the theory of measured groupoids one often meets a Borel map \(\pi\) from a groupoid \(G\) to a group \(H\) that is
multiplicative only almost everywhere: \(\pi(\gamma_1\gamma_2)=\pi(\gamma_1)\pi(\gamma_2)\) for almost every composable
pair. This happens, for instance, when a representation is decomposed fibre by fibre, because a decomposition of an
operator is determined only up to a null set. The lesson "Weights on random operators and formal dimension" meets such a
map when it passes to the stable kernel of a modulus. This lesson proves that an almost homomorphism into a Polish group
agrees almost everywhere with a genuine Borel homomorphism, defined on the reduction of \(G\) to a conull Borel set of
units that is *saturated* (Theorem 5.1).

Saturation is what the theory of transverse measures needs. A transverse measure only sees saturated negligible sets
(Measured groupoids and transverse measures, Section 5), so
a random Hilbert space may be changed on a saturated negligible set but not on an arbitrary null set of units. Ramsay's
theory of virtual groups [Ramsay 1971] identifies a measured groupoid with its reductions to conull Borel sets, and, as
Connes points out [Connes 1979, Introduction], such sets need not be saturated. The difference is real for groupoids
with large orbits: on the pair groupoid of an interval every unit has measure zero, but the only saturated conull set is
the whole interval (Example 6.2).

The proof has two parts. Sections 2–4 construct, by essential values, a homomorphism \(\pi'\) on a subgroupoid \(D\)
that contains almost every arrow and every arrow between points of a conull set \(Y_1\). The set \(Y_1\) need not be
saturated, and in general \(D\) misses arrows that end outside \(Y_1\) (Example 6.2). Section 5 passes to a saturated
conull set \(Y\): every unit \(x\in Y\) is joined to \(Y_1\) by an arrow \(\theta(x)\), chosen in a Borel way, and the
homomorphism is transported along these arrows. The Borel choice comes from a uniformization theorem for Borel sets
whose sections have positive measure, proved in Section 1 from a uniform form of inner regularity.

We use the measurable groupoids, kernels and transverse functions of Measured groupoids and transverse
measures, and the isomorphism theorem for standard Borel spaces from
Polish spaces and standard Borel spaces.
Section "Results used from other lessons" lists exactly what is used.

*Conventions.* \(\mathcal F^+(X)\) is the set of measurable functions \(X\to[0,\infty]\). A *probability kernel* from a
measurable space \(X\) to a measurable space \(Z\) is a family \((\rho_x)_{x\in X}\) of probability measures on \(Z\)
such that \(x\mapsto\rho_x(E)\) is measurable for every measurable \(E\subseteq Z\). For \(W\subseteq X\times Z\) and
\(x\in X\) we write \(W_x=\{z:(x,z)\in W\}\). The *Cantor space* \(\mathcal C=\{0,1\}^{\mathbb N}\) carries the
product topology; for a finite word \(s\in\{0,1\}^{<\mathbb N}\), \(N_s\) is the set of \(c\in\mathcal C\) that begin
with \(s\), and \(c|n\) is the word of the first \(n\) letters of \(c\). A *Polish group* is a topological group whose
topology is Polish.

## Results used from other lessons

**(R1) Kernels and the Tonelli theorem.** For an s-finite kernel \(\kappa\) from \(Y\) to \(Z\) and
\(F\in\mathcal F^+(Y\times Z)\), the function \(y\mapsto\int F(y,z)\,d\kappa_y(z)\) is measurable, and iterated
integrals of nonnegative functions against s-finite measures may be interchanged. This is (B1) of Measured groupoids
and transverse measures. Bounded kernels, in particular probability
kernels, are s-finite.

**(R2) Groupoids and transverse functions.** We use the definitions of Measured groupoids and transverse measures,
Sections 1 and 2: measurable groupoids \(G\), their units
\(G^{(0)}\), range and source maps \(r,s\), the sets \(G^y=r^{-1}(y)\), composable pairs \(G^{(2)}\), saturated sets,
reductions, kernels on \(G\), and transverse functions \(\nu\), for which \(\gamma\nu^x=\nu^y\) for every
\(\gamma:x\to y\) (Definition 2.1). \(\mathcal E^+\) is the set of proper transverse functions, and \(\nu\) is
*faithful* when \(\nu^y\neq0\) for every \(y\). By Lemma 2.2(b) there, \(\nu\in\mathcal E^+\) has measurable sets
\(A_1\subseteq A_2\subseteq\cdots\) with union \(G\) and \(\sup_y\nu^y(A_n)<\infty\) for every \(n\). The standing
assumption there (one-point sets of units are measurable) holds for the groupoids of this lesson, whose Borel structure
is standard.

**(R3) Standard Borel spaces.** Every countable standard Borel space has all its subsets Borel, and every uncountable
one is Borel isomorphic to \(\mathcal C\) (Polish spaces and standard Borel spaces, Theorem
5.2). Hence every standard Borel
space \(Y\) has a Borel isomorphism \(j\) onto a Borel subset of \(\mathcal C\): for countable \(Y\), take any injection
onto a countable subset of \(\mathcal C\), whose points are closed.

**(R4) Elementary facts on the Cantor space and on separable metric spaces.** The cylinders \(N_s\) are clopen and
form a countable base of \(\mathcal C\), so they generate its Borel sets. A point \(c\) lies in the closure of a set
\(C\subseteq\mathcal C\) exactly when every \(N_{c|n}\) meets \(C\). If \(P\) is a separable metric space, every open
subset of \(P\times P\) is a countable union of products of open balls with rational radii around points of a dense
sequence, so the Borel sets of \(P\times P\) are generated by products of Borel sets. A pointwise limit of measurable
maps into a metric space is measurable, and the set where two measurable maps into a separable metric space agree is
measurable (it is the preimage of the closed diagonal).

## 1. Uniform regularity and Borel choice

Throughout this section, \((X,\mathcal X)\) is a measurable space and \((\rho_x)\) is a probability kernel from \(X\)
to \(\mathcal C\). Sets in \(X\times\mathcal C\) are measurable for the product \(\sigma\)-algebra
\(\mathcal X\otimes\mathcal B(\mathcal C)\). The sections \(W_x\) of such a set are Borel, and by (R1) the function
\(x\mapsto\rho_x(W_x)\) is measurable.

**Lemma 1.1** (uniform regularity). Let \(W\subseteq X\times\mathcal C\) be measurable and \(\varepsilon:X\to(0,\infty)\)
measurable. There are measurable sets \(F\subseteq W\subseteq O\) such that, for every \(x\), \(F_x\) is closed, \(O_x\)
is open and \(\rho_x(O_x\setminus F_x)<\varepsilon(x)\).

**Proof.** Let \(\mathcal R\) be the class of measurable \(W\) with this property for *every* measurable
\(\varepsilon>0\). It contains \(B\times N_s\) for \(B\in\mathcal X\) and every word \(s\): take \(F=O=B\times N_s\),
whose sections \(N_s\) or \(\varnothing\) are clopen. These sets generate \(\mathcal X\otimes\mathcal B(\mathcal C)\)
by (R4). We show that \(\mathcal R\) is a \(\sigma\)-algebra, so that it contains every measurable set.

*Complements.* If \(F\subseteq W\subseteq O\) work for \(W\) and \(\varepsilon\), then the complements
\(O^c\subseteq W^c\subseteq F^c\) work for \(W^c\) and \(\varepsilon\), with closed sections \((O^c)_x\), open sections
\((F^c)_x\), and \(F^c\setminus O^c=O\setminus F\).

*Countable unions.* Let \(W=\bigcup_nW_n\) with \(W_n\in\mathcal R\), and let \(\varepsilon>0\) be measurable. Choose
\(F_n\subseteq W_n\subseteq O_n\) for \(W_n\) and \(\varepsilon2^{-n-2}\), and put \(O=\bigcup_nO_n\), a measurable set
with open sections containing \(W\). Then \(\rho_x\big(O_x\setminus\bigcup_nF_{n,x}\big)\le\sum_n\rho_x(O_{n,x}\setminus
F_{n,x})<\varepsilon(x)/4\). Let \(F^N=\bigcup_{n\le N}F_n\). Since \(\rho_x\) is finite,
\(\rho_x\big(\bigcup_nF_{n,x}\setminus F^N_x\big)\to0\) as \(N\to\infty\), so
\[
N(x)=\min\Big\{N:\ \rho_x\Big(\bigcup_nF_{n,x}\setminus F^N_x\Big)<\varepsilon(x)/4\Big\}
\]
is finite, and it is measurable in \(x\) because each function \(x\mapsto\rho_x(\bigcup_nF_{n,x}\setminus F^N_x)\) is.
Put \(F=\bigcup_N\big(\{x:N(x)=N\}\times\mathcal C\big)\cap F^N\). It is measurable, \(F\subseteq W\), and
\(F_x=F^{N(x)}_x\) is a finite union of closed sets, hence closed. Finally
\(\rho_x(O_x\setminus F_x)<\varepsilon(x)/4+\varepsilon(x)/4<\varepsilon(x)\).

*The whole space* \(X\times\mathcal C\) is \(X\times N_\varnothing\). So \(\mathcal R\) is a \(\sigma\)-algebra.
\(\square\)

**Theorem 1.2** (Borel choice in sections of positive measure). Let \(Y\) be a standard Borel space, \((\rho_x)\) a
probability kernel from \(X\) to \(Y\), and \(A\subseteq X\times Y\) a measurable set with \(\rho_x(A_x)>0\) for every
\(x\in X\). Then there is a measurable map \(\theta:X\to Y\) with \((x,\theta(x))\in A\) for every \(x\).

**Proof.** *Reduction to \(\mathcal C\).* Let \(j\) be a Borel isomorphism of \(Y\) onto a Borel set
\(j(Y)\subseteq\mathcal C\) (R3). The images \(\rho'_x\) of the \(\rho_x\) under \(j\) form a probability kernel from
\(X\) to \(\mathcal C\). The set \(A'=\{(x,c):c\in j(Y),\ (x,j^{-1}(c))\in A\}\) is measurable, being the preimage of
\(A\) under the measurable map \((x,c)\mapsto(x,j^{-1}(c))\) on the measurable set \(X\times j(Y)\), and
\(\rho'_x(A'_x)=\rho_x(A_x)>0\). If \(\theta'\) is a measurable choice for \(A'\), then \(\theta'(x)\in j(Y)\), and
\(\theta=j^{-1}\circ\theta'\) is a measurable choice for \(A\). So we may assume \(Y=\mathcal C\).

*A closed part of positive measure.* Apply Lemma 1.1 to \(W=A\) and \(\varepsilon(x)=\rho_x(A_x)/2\). It gives a
measurable \(C\subseteq A\) with closed sections and \(\rho_x(A_x\setminus C_x)<\rho_x(A_x)/2\), so \(\rho_x(C_x)>0\).

*The leftmost choice.* Define \(\theta(x)\in\mathcal C\) letter by letter: if the first \(n\) letters form the word
\(s\) and \(\rho_x(C_x\cap N_s)>0\), the next letter is \(0\) when \(\rho_x(C_x\cap N_{s0})>0\) and \(1\) otherwise. By
induction, \(\rho_x(C_x\cap N_{\theta(x)|n})>0\) for every \(n\): it holds for \(n=0\), and since \(N_s\) is the
disjoint union of \(N_{s0}\) and \(N_{s1}\), one of them meets \(C_x\) in positive measure, and the rule picks such a
one. Each letter of \(\theta(x)\) is determined by finitely many of the measurable functions
\(x\mapsto\rho_x(C_x\cap N_t)\), so the coordinates of \(\theta\) are measurable, and \(\theta\) is measurable by
(R4). Every cylinder \(N_{\theta(x)|n}\) meets \(C_x\), so \(\theta(x)\) lies in the closure of \(C_x\), which is
\(C_x\). Hence \(\theta(x)\in C_x\subseteq A_x\). \(\square\)

When all \(\rho_x\) equal one probability measure, Theorem 1.2 is the measure uniformization theorem recalled in
[Kechris–Wolman 2024, Theorem 1.1].

## 2. Essential values

In this section \((X,\mathcal X)\) and \((Z,\mathcal Z)\) are measurable spaces, \((\rho_x)\) is a probability kernel
from \(X\) to \(Z\), \(P\) is a separable metric space with metric \(d\), \(\bar d=\min(d,1)\), and
\(F:X\times Z\to P\) is measurable for \(\mathcal X\otimes\mathcal Z\) and the Borel sets of \(P\). We say that
\(F(x,\cdot)\) is *\(\rho_x\)-essentially constant* if there is \(p\in P\) with \(F(x,z)=p\) for \(\rho_x\)-almost
every \(z\). Since \(\rho_x\) is a probability measure, \(p\) is then unique; it is the *essential value*.

**Lemma 2.1.**

1. The function \((x,z,z')\mapsto\bar d(F(x,z),F(x,z'))\) on \(X\times Z\times Z\) is measurable.
2. The set \(X_c\) of \(x\) for which \(F(x,\cdot)\) is \(\rho_x\)-essentially constant is
\[
X_c=\Big\{x:\ \int\!\!\int\bar d\big(F(x,z),F(x,z')\big)\,d\rho_x(z)\,d\rho_x(z')=0\Big\},
\]
and it is measurable.
3. The essential value \(e:X_c\to P\) is measurable.

**Proof.** (1) The map \((x,z,z')\mapsto(F(x,z),F(x,z'))\) is measurable into \(P\times P\) for the
\(\sigma\)-algebra generated by products of Borel sets, which is the Borel \(\sigma\)-algebra of \(P\times P\) by
(R4); and \(\bar d\) is continuous.

(2) If \(F(x,\cdot)=p\) almost everywhere, the integrand vanishes \(\rho_x\otimes\rho_x\)-almost everywhere. Conversely,
if the double integral is \(0\), then for \(\rho_x\)-almost every \(z\) the inner integral
\(\int\bar d(F(x,z),F(x,z'))\,d\rho_x(z')\) is \(0\) (R1). Such a \(z_0\) exists, and \(F(x,z')=F(x,z_0)\) for almost
every \(z'\). The double integral is measurable in \(x\): apply (R1) to the probability kernel \((x,z)\mapsto\rho_x\)
from \(X\times Z\) to \(Z\), and then to \((\rho_x)\).

(3) Let \((p_k)\) be dense in \(P\). For \(x\in X_c\), \(\int\bar d(F(x,z),p_k)\,d\rho_x(z)=\bar d(e(x),p_k)\), a
measurable function of \(x\) by (R1). Let \(k_j(x)\) be the least \(k\) with \(\bar d(e(x),p_k)<2^{-j}\); it is
measurable in \(x\), and \(e(x)=\lim_jp_{k_j(x)}\). By (R4), \(e\) is measurable. \(\square\)

## 3. Almost homomorphisms and their essential values

From now on we fix the following data.

- \((G,\mathcal B)\) is a measurable groupoid whose measurable space is standard Borel.
- \(\kappa\in\mathcal E^+(G)\) is a faithful proper transverse function.
- \(\mu\) is a \(\sigma\)-finite measure on \(G^{(0)}\), and \(m=\mu\circ\kappa\) is the measure
  \(m(E)=\int\kappa^y(E)\,d\mu(y)\) on \(G\). We assume that \(m\) and its image \(\tilde m\) under
  \(\gamma\mapsto\gamma^{-1}\) have the same null sets.
- \(m^{(2)}\) is the measure on \(G^{(2)}\) given by
  \(m^{(2)}(f)=\int\!\!\int f(\gamma_1,\gamma_2)\,d\kappa^{s(\gamma_1)}(\gamma_2)\,dm(\gamma_1)\).
- \(H\) is a Polish group with unit \(1\), and \(\pi:G\to H\) is Borel with \(\pi(\gamma_1\gamma_2)=\pi(\gamma_1)
  \pi(\gamma_2)\) for \(m^{(2)}\)-almost every \((\gamma_1,\gamma_2)\in G^{(2)}\). We call \(\pi\) an *almost
  homomorphism*.

By (R2), \(\kappa^y\) is carried by \(G^y\), and \(\gamma\kappa^x=\kappa^y\) for every \(\gamma:x\to y\): left
translation by \(\gamma\), \(\delta\mapsto\gamma\delta\), is a bijection of \(G^x\) onto \(G^y\) that carries
\(\kappa^x\) to \(\kappa^y\). In particular it carries \(\kappa^x\)-null sets onto \(\kappa^y\)-null sets.

**Lemma 3.1** (normalization). There is a measurable \(w:G\to(0,\infty)\) with \(0<\kappa^y(w)\le1\) for every
\(y\in G^{(0)}\). The measures \(\rho^y=\kappa^y(w)^{-1}\,w\,\kappa^y\) form a probability kernel from \(G^{(0)}\) to
\(G\), and \(\rho^y\) and \(\kappa^y\) have the same null sets.

**Proof.** Take \(A_n\) as in (R2), with \(C_n=\sup_y\kappa^y(A_n)<\infty\), and
\(w=\sum_n2^{-n}(1+C_n)^{-1}1_{A_n}\). Every arrow lies in some \(A_n\), so \(w>0\), and
\(\kappa^y(w)\le\sum_n2^{-n}\le1\). Since \(\kappa\) is faithful and \(w>0\), \(\kappa^y(w)>0\). Measurability of
\(y\mapsto\rho^y(E)=\kappa^y(1_Ew)/\kappa^y(w)\) is (R1). As \(w>0\), \(\rho^y\) and \(\kappa^y\) have the same null
sets. \(\square\)

For \(\gamma,\delta\in G\) put \(F(\gamma,\delta)=\pi(\gamma\delta)\pi(\delta)^{-1}\) if \((\gamma,\delta)\in G^{(2)}\)
and \(F(\gamma,\delta)=1\) otherwise. Let \(D\) be the set of \(\gamma\in G\) such that \(F(\gamma,\cdot)\) is
\(\rho^{s(\gamma)}\)-essentially constant, and for \(\gamma\in D\) let \(\pi'(\gamma)\) be its essential value. Since
\(\rho^{s(\gamma)}\) is carried by \(G^{s(\gamma)}\), the definition only involves the arrows \(\delta\) with
\((\gamma,\delta)\in G^{(2)}\): \(\gamma\in D\) with \(\pi'(\gamma)=h\) means that \(\pi(\gamma\delta)=h\,\pi(\delta)\) for
\(\kappa^{s(\gamma)}\)-almost every \(\delta\in G^{s(\gamma)}\).

**Proposition 3.2.**

1. \(D\) is a Borel set and \(\pi':D\to H\) is a Borel map.
2. Every unit \(x\) lies in \(D\), and \(\pi'(x)=1\).
3. If \(\gamma\in D\), then \(\gamma^{-1}\in D\) and \(\pi'(\gamma^{-1})=\pi'(\gamma)^{-1}\).
4. If \(\gamma_1,\gamma_2\in D\) are composable, then \(\gamma_1\gamma_2\in D\) and
   \(\pi'(\gamma_1\gamma_2)=\pi'(\gamma_1)\pi'(\gamma_2)\).
5. The set \(E=\{\gamma\in D:\pi'(\gamma)=\pi(\gamma)\}\) is Borel and \(m(G\setminus E)=0\).

So \(D\) is a subgroupoid of \(G\) containing all units, and \(\pi'\) is a homomorphism on it.

**Proof.** (1) The set \(G^{(2)}\) is measurable in \(G\times G\), and \(F\) is measurable, because the product, the
inverse in \(H\) and \(\pi\) are measurable. The maps \(\gamma\mapsto\rho^{s(\gamma)}\) form a probability kernel from
\(G\) to \(G\), by Lemma 3.1 and the measurability of \(s\). Apply Lemma 2.1 with \(X=Z=G\) and \(P=H\), which is a
separable metric space for any compatible metric.

(2) For \(\delta\in G^x\), \(x\delta=\delta\), so \(F(x,\delta)=1\) for every such \(\delta\).

(3) Let \(\gamma:x\to y\), \(h=\pi'(\gamma)\), and let \(B\subseteq G^x\) be a \(\kappa^x\)-conull set with
\(\pi(\gamma\delta)=h\pi(\delta)\) for \(\delta\in B\). Then \(\gamma B\) is \(\kappa^y\)-conull in \(G^y\), and for
\(\varepsilon=\gamma\delta\in\gamma B\) we have \(F(\gamma^{-1},\varepsilon)=\pi(\delta)\pi(\gamma\delta)^{-1}
=\pi(\delta)\big(h\pi(\delta)\big)^{-1}=h^{-1}\).

(4) Let \(\gamma_2:x\to y\) and \(\gamma_1:y\to z\), with \(h_i=\pi'(\gamma_i)\). For \(\kappa^x\)-almost every
\(\delta\in G^x\), \(\pi(\gamma_2\delta)=h_2\pi(\delta)\). For \(\kappa^y\)-almost every \(\varepsilon\in G^y\),
\(\pi(\gamma_1\varepsilon)=h_1\pi(\varepsilon)\); since \(\delta\mapsto\gamma_2\delta\) carries \(\kappa^x\) to
\(\kappa^y\), this holds for \(\varepsilon=\gamma_2\delta\) with \(\kappa^x\)-almost every \(\delta\). For such
\(\delta\),
\(\pi(\gamma_1\gamma_2\delta)=h_1\pi(\gamma_2\delta)=h_1h_2\pi(\delta)\).

(5) \(E\) is Borel by (1) and (R4). By hypothesis and (R1), for \(m\)-almost every \(\gamma\) we have
\(\pi(\gamma\delta)=\pi(\gamma)\pi(\delta)\) for \(\kappa^{s(\gamma)}\)-almost every \(\delta\), that is,
\(\gamma\in D\) and \(\pi'(\gamma)=\pi(\gamma)\). \(\square\)

## 4. Conull sets and saturation

For a Borel set \(N\subseteq G^{(0)}\) put
\[
[N]_\kappa=\{y\in G^{(0)}:\ \kappa^y(s^{-1}(N))>0\},
\]
the set of units into which a \(\kappa\)-nonnegligible set of arrows comes from \(N\).

**Lemma 4.1.** Let \(N\subseteq G^{(0)}\) be a Borel set with \(\mu(N)=0\).

1. \(m(r^{-1}(N))=0\) and \(m(s^{-1}(N))=0\).
2. \([N]_\kappa\) is Borel, saturated and \(\mu\)-null, and \(\kappa^y(s^{-1}(N))=0\) for every \(y\notin[N]_\kappa\).

**Proof.** (1) Since \(\kappa^y\) is carried by \(G^y\), \(\kappa^y(r^{-1}(N))\) is \(\kappa^y(G)\) for \(y\in N\) and
\(0\) otherwise, so \(m(r^{-1}(N))=\int_N\kappa^y(G)\,d\mu(y)=0\). The inverse of \(s^{-1}(N)\) is \(r^{-1}(N)\), so
\(\tilde m(s^{-1}(N))=m(r^{-1}(N))=0\), and \(m(s^{-1}(N))=0\) because \(m\) and \(\tilde m\) have the same null sets.

(2) \([N]_\kappa\) is Borel by (R1). It is saturated: for \(\gamma:x\to y\), left translation by \(\gamma\) carries
\(\kappa^x\) to \(\kappa^y\) and preserves sources, so \(\kappa^y(s^{-1}(N))=\kappa^x(s^{-1}(N))\). It is \(\mu\)-null,
because \(\int\kappa^y(s^{-1}(N))\,d\mu(y)=m(s^{-1}(N))=0\). The last assertion is the definition. \(\square\)

**Lemma 4.2.** The sets \(Y_1=\{x:\kappa^x(G\setminus D)=0\}\) and \(Y_2=\{x:\kappa^x(G\setminus E)=0\}\) are Borel and
\(\mu\)-conull, and \(Y_2\subseteq Y_1\). Every arrow whose source and range lie in \(Y_1\) belongs to \(D\).

**Proof.** The sets are Borel by (R1), and \(Y_2\subseteq Y_1\) because \(E\subseteq D\). Since
\(\int\kappa^x(G\setminus E)\,d\mu(x)=m(G\setminus E)=0\) (Proposition 3.2(5)), \(Y_2\) is \(\mu\)-conull, and so is
\(Y_1\). Let \(\gamma:x\to y\) with \(x,y\in Y_1\). For \(\kappa^x\)-almost every \(\delta\in G^x\), \(\delta\in D\);
and since left translation by \(\gamma\) carries \(\kappa^x\) to \(\kappa^y\) and \(\kappa^y(G\setminus D)=0\),
\(\gamma\delta\in D\) for \(\kappa^x\)-almost every \(\delta\). As \(\kappa^x\neq0\), some \(\delta\) has both
properties, and \(\gamma=(\gamma\delta)\delta^{-1}\in D\) by Proposition 3.2(3), (4). \(\square\)

## 5. Regularization on a saturated set

**Theorem 5.1.** In the setting of Section 3 there are a \(\mu\)-conull saturated Borel set \(Y\subseteq G^{(0)}\) and
a Borel homomorphism \(\pi''\) from the reduction \(G_Y=r^{-1}(Y)\) to \(H\) such that \(\pi''=\pi\)
\(m\)-almost everywhere on \(G_Y\).

**Proof.** *The saturated set.* Let \(N=G^{(0)}\setminus Y_2\), a \(\mu\)-null Borel set (Lemma 4.2), and
\(Y=G^{(0)}\setminus[N]_\kappa\). By Lemma 4.1(2), \(Y\) is a \(\mu\)-conull saturated Borel set, and for every
\(x\in Y\), \(\kappa^x\)-almost every arrow into \(x\) has its source in \(Y_2\). Since \(Y\) is saturated, the source
of every arrow of \(G_Y=r^{-1}(Y)\) also lies in \(Y\).

*The connecting arrows.* Let
\[
A=\{(x,\varepsilon)\in Y\times G:\ r(\varepsilon)=x,\ s(\varepsilon)\in Y_2,\ \text{and }\varepsilon\in E\text{ if }
x\in Y_2\},
\]
a measurable subset of \(Y\times G\) (the units form a standard Borel space, so the set of \((x,\varepsilon)\) with
\(r(\varepsilon)=x\) is measurable). For \(x\in Y\), \(\kappa^x\)-almost every \(\varepsilon\in G^x\) has
\(s(\varepsilon)\in Y_2\), and if \(x\in Y_2\) then also \(\kappa^x\)-almost every \(\varepsilon\) lies in \(E\). So
\(\rho^x(A_x)=1\) for every \(x\in Y\) (Lemma 3.1). Theorem 1.2, applied to \(X=Y\), the standard Borel space \(G\) and
the probability kernel \((\rho^x)_{x\in Y}\), gives a Borel map \(\theta:Y\to G\) with \((x,\theta(x))\in A\) for
every \(x\in Y\): \(\theta(x)\) is an arrow from a point of \(Y_2\) to \(x\), and it lies in \(E\) when \(x\in Y_2\).

*The homomorphism.* For \(\gamma:x\to y\) in \(G_Y\), the arrow \(\theta(y)^{-1}\gamma\,\theta(x)\) goes from
\(s(\theta(x))\) to \(s(\theta(y))\), two points of \(Y_2\subseteq Y_1\); by Lemma 4.2 it lies in \(D\). Put
\[
\pi''(\gamma)=\pi(\theta(y))\;\pi'\big(\theta(y)^{-1}\gamma\,\theta(x)\big)\;\pi(\theta(x))^{-1}.
\]
This is a Borel function of \(\gamma\): \(\gamma\mapsto\big(\theta(r(\gamma)),\gamma,\theta(s(\gamma))\big)\) is Borel,
the product of \(G\) is Borel on composable triples, \(\pi'\) is Borel on \(D\) (Proposition 3.2(1)), and the group
operations of \(H\) are continuous. For composable \(\gamma_1:y\to z\) and \(\gamma_2:x\to y\) in \(G_Y\), the middle
factors \(\pi(\theta(y))^{-1}\pi(\theta(y))\) cancel and Proposition 3.2(4) gives
\[
\pi''(\gamma_1)\pi''(\gamma_2)=\pi(\theta(z))\,\pi'\big(\theta(z)^{-1}\gamma_1\theta(y)\,\theta(y)^{-1}\gamma_2\,
\theta(x)\big)\,\pi(\theta(x))^{-1}=\pi''(\gamma_1\gamma_2).
\]
So \(\pi''\) is a homomorphism.

*Agreement with \(\pi\).* Let \(\gamma:x\to y\) lie in \(E\), with \(x,y\in Y\cap Y_2\). Then \(\theta(x)\) and
\(\theta(y)\) lie in \(E\), so \(\pi(\theta(x))=\pi'(\theta(x))\) and \(\pi(\theta(y))=\pi'(\theta(y))\). The arrows
\(\theta(y)\), \(\theta(y)^{-1}\gamma\theta(x)\) and \(\theta(x)^{-1}\) lie in \(D\), so Proposition 3.2(3), (4) give
\[
\pi''(\gamma)=\pi'(\theta(y))\,\pi'\big(\theta(y)^{-1}\gamma\theta(x)\big)\,\pi'(\theta(x))^{-1}=\pi'(\gamma)=\pi(\gamma).
\]
The arrows of \(G_Y\) not covered by this are in \((G\setminus E)\cup r^{-1}(G^{(0)}\setminus Y_2)\cup
s^{-1}(G^{(0)}\setminus Y_2)\), an \(m\)-null set by Proposition 3.2(5) and Lemma 4.1(1). \(\square\)

**Remark 5.2.** The proof also shows that \(\pi''\) is the identity on the units of \(Y\), since
\(\theta(x)^{-1}x\,\theta(x)\) is a unit, and that \(\pi''(\gamma^{-1})=\pi''(\gamma)^{-1}\). The homomorphism
\(\pi''\) is not unique: two Borel homomorphisms on \(G_Y\) that agree \(m\)-almost everywhere may differ on the arrows
at a \(\mu\)-null set of units (Example 6.2).

## 6. Examples

**Example 6.1** (groups). Let \(K\) be a locally compact second countable group, viewed as a groupoid with one unit,
and let \(\kappa\) be a left Haar measure on \(K\) (R2 and Measured groupoids and transverse measures, Definition
2.1) and \(\mu\) the point mass at the unit. Then \(m=\kappa\),
and \(\tilde m\) is a right Haar measure, which has the same null sets as \(\kappa\) by the formula
\(\int f(t^{-1})\,dt=\int f(t)\Delta_K(t)^{-1}\,dt\) of (B4) in that lesson. The measure \(m^{(2)}\) is
\(\kappa\otimes\kappa\). So Theorem 5.1 says: a Borel map \(\pi:K\to H\) into a Polish group with
\(\pi(st)=\pi(s)\pi(t)\) for almost every \((s,t)\in K\times K\) agrees almost everywhere with a Borel homomorphism.
Here the only saturated conull set is the unit itself, and \(D=K\) by Lemma 4.2.

**Example 6.2** (the pair groupoid). Let \(X\) be a standard Borel space with a probability measure \(\lambda\), and
\(G=X\times X\) the pair groupoid, with \((x,y)(y,z)=(x,z)\), \(r(x,y)=x\), \(s(x,y)=y\). The measures
\(\kappa^x=\varepsilon_x\otimes\lambda\) on \(G^x=\{x\}\times X\) form a faithful proper transverse function, since left
translation by \((y,x)\) carries \((x,z)\) to \((y,z)\). With \(\mu=\lambda\), \(m=\lambda\otimes\lambda\) is invariant
under \((x,y)\mapsto(y,x)\). An almost homomorphism is a Borel \(\pi\) with \(\pi(x,z)=\pi(x,y)\pi(y,z)\) for
\(\lambda^{\otimes3}\)-almost every \((x,y,z)\). The groupoid has a single orbit, so \(Y=X\), and Theorem 5.1 gives a
Borel homomorphism \(\pi''\) on all of \(X\times X\). Every such homomorphism has the form
\(\pi''(x,z)=f(x)f(z)^{-1}\) with \(f(x)=\pi''(x,x_0)\) for a fixed \(x_0\), because
\(\pi''(x,z)=\pi''(x,x_0)\pi''(x_0,z)\) and \(\pi''(x_0,z)=\pi''(z,x_0)^{-1}\). Changing \(f\) at one point gives
another homomorphism that agrees with \(\pi''\) almost everywhere. This also shows why Section 5 is needed. If
\(\pi=f(x)f(z)^{-1}\) almost everywhere but \(\pi(x_1,\cdot)\) is replaced by an arbitrary Borel function for one point
\(x_1\) with \(\lambda(\{x_1\})=0\), then \(\pi\) is still an almost homomorphism, but for \(\gamma=(x_1,z)\) the function
\(\delta=(z,w)\mapsto\pi(x_1,w)\pi(z,w)^{-1}\) need not be essentially constant. Then \(\gamma\notin D\), although the
saturated conull set is all of \(X\). The connecting arrows \(\theta(x_1)=(x_1,w)\) with \(w\in Y_2\) repair this.

**Example 6.3** (cocycles of group actions). Let a locally compact second countable group \(K\) act measurably on the
right on a standard Borel space \(X\), \((x,k)\mapsto xk\), and let \(\mu\) be a \(\sigma\)-finite measure on \(X\)
that is quasi-invariant: \(\mu(Bk)=0\) whenever \(\mu(B)=0\), for all \(k\). On the action groupoid \(X\rtimes K\) of
Measured groupoids and transverse measures, Example 1.2(d),
with \(r(x,k)=x\), \(s(x,k)=xk\) and \((x,k)(xk,l)=(x,kl)\), let \(\kappa^x\) be the image of a left Haar measure
\(dl\) under \(l\mapsto(x,l)\). Left translation by \((x,k)\) sends \((xk,l)\) to \((x,kl)\), so \(\kappa\) is
transverse by left invariance of \(dl\), and it is faithful and proper. Then \(m=\mu\otimes dl\) on \(X\times K\). The
inverse is \((x,k)^{-1}=(xk,k^{-1})\), and by quasi-invariance, Fubini and the fact that inversion on \(K\) preserves
Haar-null sets, \(m\) and \(\tilde m\) have the same null sets (Exercise 7.1). An almost homomorphism is a Borel map
\(c:X\times K\to H\) with \(c(x,kl)=c(x,k)\,c(xk,l)\) for almost every \((x,k,l)\), an *almost cocycle*. Theorem 5.1
gives an invariant conull Borel set \(Y\subseteq X\) and a Borel map \(c''\) on \(Y\times K\) satisfying the cocycle
identity everywhere and agreeing with \(c\) almost everywhere.

## 7. Exercises

**Exercise 7.1.** In Example 6.3, show that \(m\) and \(\tilde m\) have the same null sets.

*Solution.* \(\tilde m\) is the image of \(m=\mu\otimes dl\) under \(\iota(x,k)=(xk,k^{-1})\). For a Borel
\(E\subseteq X\times K\), Tonelli gives \(\tilde m(E)=\int\mu(\{x:(xk,k^{-1})\in E\})\,dk\). The set inside is
\(\{x:xk\in E^{k^{-1}}\}=E^{k^{-1}}k^{-1}\), where \(E^l=\{x:(x,l)\in E\}\). By quasi-invariance (for \(k\) and
\(k^{-1}\)) its measure vanishes exactly when \(\mu(E^{k^{-1}})=0\). So \(\tilde m(E)=0\) exactly when
\(\mu(E^{k^{-1}})=0\) for almost every \(k\), that is, when \(\mu(E^l)=0\) for almost every \(l\), because inversion on
\(K\) carries Haar-null sets to Haar-null sets ((B4) of Measured groupoids and transverse
measures). By Tonelli this says \(m(E)=0\).

**Exercise 7.2.** Show that the set \(D\) of Section 3 does not depend on the choice of the function \(w\) of Lemma 3.1,
and that neither does \(\pi'\).

*Solution.* Membership in \(D\) and the essential value only depend on the null sets of \(\rho^{s(\gamma)}\), which are
those of \(\kappa^{s(\gamma)}\) for every choice of \(w>0\) (Lemma 3.1).

**Exercise 7.3.** Suppose that \(\pi\) is a homomorphism: \(\pi(\gamma_1\gamma_2)=\pi(\gamma_1)\pi(\gamma_2)\) for
every composable pair. Show that \(D=G\), \(\pi'=\pi\), and that the map \(\pi''\) of Theorem 5.1 is the restriction of
\(\pi\) to \(G_Y\).

*Solution.* For every \(\gamma\) and every \(\delta\in G^{s(\gamma)}\), \(F(\gamma,\delta)=\pi(\gamma)\pi(\delta)
\pi(\delta)^{-1}=\pi(\gamma)\), so \(F(\gamma,\cdot)\) is constant: \(\gamma\in D\) and \(\pi'(\gamma)=\pi(\gamma)\). Then
\(\pi''(\gamma)=\pi(\theta(y))\pi(\theta(y))^{-1}\pi(\gamma)\pi(\theta(x))\pi(\theta(x))^{-1}=\pi(\gamma)\) for
\(\gamma:x\to y\) in \(G_Y\).

## References



- [Connes 1979] A. Connes, Sur la théorie non commutative de l'intégration, in: *Algèbres d'opérateurs* (Sém.,
  Les Plans-sur-Bex, 1978), Lecture Notes in Math. 725, Springer, Berlin, 1979, 19–143. Free at https://alainconnes.org/wp-content/uploads/ThNonComm.pdf
- [Kechris–Wolman 2024] A. S. Kechris and M. Wolman, Invariant uniformization, free preprint arXiv:2405.15111 (version 3,
  2026), https://arxiv.org/abs/2405.15111.
- [Ramsay 1971] A. Ramsay, Virtual groups and group actions, *Advances in Mathematics* 6 (1971), 253–322 (free to read
  in the publisher's open archive). Free at https://doi.org/10.1016/0001-8708(71)90018-1
