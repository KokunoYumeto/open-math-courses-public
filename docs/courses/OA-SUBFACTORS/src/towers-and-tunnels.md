# Going up and down the Jones tower

The basic construction can be repeated. Going upward is canonical once the inclusion is given. Going downward requires a choice, but all choices at one step differ by a unitary in the smaller factor. The downward step also produces an element that makes the positive-operator index bound sharp.

We assume [A projection that remembers an inclusion](projection-and-basic-construction.md), [Measuring an inclusion through modules and corners](module-dimension-and-local-index.md), and [Finite bases, bounded vectors and a positive-operator inequality](finite-bases-and-positive-index.md). Basic references are [Anantharaman–Popa], [Jones] and [Pimsner–Popa]. Throughout, \(N\subseteq M\) are II₁ factors, \(d=[M:N]<\infty\), and \(\lambda=d^{-1}\).

## Repeating the upward construction

Set \(M_{-1}=N\), \(M_0=M\). Recursively define

\[
M_{i+1}=\langle M_i,e_i\rangle,
\]

where \(e_i\) is the projection of \(L^2(M_i)\) onto \(L^2(M_{i-1})\). Although these projections are first constructed on different Hilbert spaces, each is an element of \(M_{i+1}\); the compatible algebra inclusions put all of them in a common algebraic tower.

**Theorem 4.1.** Every \(M_i\) is a II₁ factor, every consecutive inclusion has index \(d\), and the normalized traces agree on overlaps. If \(E_i:M_i\to M_{i-1}\) preserves the trace, then

\[
e_ix e_i=E_i(x)e_i\quad(x\in M_i),
\qquad E_{i+1}(e_i)=\lambda1.
\]

**Proof.** For the first step, represent \(M\) on \(L^2(M)\). The first lesson gives \(M_1=JN'J\). The commutant-index formula in the second lesson gives \([N':M']=[M:N]\). Conjugation by \(J\) carries \(N'\supseteq M'\) to \(M_1\supseteq M\), preserving index, so \([M_1:M]=d\). Here conjugation is a conjugate-linear isomorphism; standard Hilbert spaces and their real positive traces preserve the same dimension under it. The trace and compression assertions are the first lesson's trace formula. Applying the same argument recursively proves every assertion. \(\square\)

**Theorem 4.2 — projection relations.** In this tower,

\[
\begin{gathered}
e_i^2=e_i=e_i^*,\\
e_ie_j=e_je_i\quad(|i-j|\geq2),\\
e_ie_{i+1}e_i=\lambda e_i,\\
e_{i+1}e_ie_{i+1}=\lambda e_{i+1}.
\end{gathered}
\]

**Proof.** Each \(e_i\) commutes with \(M_{i-1}\), while \(e_j\in M_{j+1}\subseteq M_{i-1}\) for \(j\leq i-2\). This proves distant commutation. The compression identity gives

\[
e_{i+1}e_ie_{i+1}=E_{i+1}(e_i)e_{i+1}
=\lambda e_{i+1}.
\]

For the other adjacent identity it suffices to consider \(i=0\), because the same reasoning applies at every level. On \(L^2(M_1)\), \(e_1\widehat X=\widehat{E_M(X)}\). For \(a\in M\),

\[
e_0e_1e_0\widehat a
=e_0\widehat{E_M(e_0a)}
=\lambda e_0\widehat a.
\]

For \(a,b\in M\),

\[
\begin{aligned}
e_0e_1e_0\widehat{ae_0b}
&=e_0\widehat{E_M(E_N(a)e_0b)}\\
&=\lambda\widehat{e_0E_N(a)b}
=\lambda\widehat{e_0ae_0b}.
\end{aligned}
\]

These vectors span a dense subspace of \(L^2(M_1)\). The bounded operators therefore agree everywhere. \(\square\)

**Proposition 4.3.** The union \(\bigcup_i M_i\), completed in its common trace representation, generates a II₁ factor \(M_\infty\).

**Proof.** The compatible normalized traces give a faithful trace on the algebraic union and a finite von Neumann algebra in its GNS representation. Let \(z\in Z(M_\infty)\). Trace-preserving expectations onto the increasing \(M_i\) satisfy \(E_{M_i}(z)\to z\) in \(L^2\), because their range union is dense in the completed Hilbert space. Bimodularity gives \(E_{M_i}(z)\in Z(M_i)=\mathbb C\), hence \(E_{M_i}(z)=\tau(z)1\). Thus \(z\) is scalar. The algebra contains the diffuse factor \(M\), so it has type II₁. \(\square\)

This construction of \(M_\infty\) uses the common trace. It does not assert that the whole infinite tower acts normally on the original space \(L^2(M)\).

## A downward step from a module of dimension one

**Theorem 4.4 — downward construction.** There is a II₁ subfactor \(P\subseteq N\) such that

\[
[N:P]=d,\qquad M\cong\langle N,e_P\rangle,
\]

where the isomorphism fixes \(N\). Its image \(f\in M\) of \(e_P\) satisfies

\[
E_N(f)=\lambda1.
\]

**Proof.** Choose a projection \(p\in M\) with \(\tau(p)=\lambda\), and let \(K=L^2(M)p\). Left multiplication makes it an \(M\)-module with dimension \(\lambda\). Its restriction to \(N\) has dimension \(d\lambda=1\). Finite-module classification therefore identifies it, as a left \(N\)-module, with \(L^2(N)\).

Let \(\pi(M)\) be the transported left \(M\)-action on \(L^2(N)\), and let \(J_N\) be the tracial conjugation there. Since \(\pi(M)\supseteq N\), its commutant lies in \(N'\). Define

\[
P=J_N\pi(M)'J_N\subseteq N.
\]

This is a II₁ factor. The reciprocal dimension formula gives

\[
\dim_{\pi(M)'}L^2(N)=\lambda^{-1}=d.
\]

Conjugation by \(J_N\) changes this to the left \(P\)-dimension of the standard \(N\)-space. Thus \([N:P]=d\). The basic construction of \(P\subseteq N\) is

\[
J_NP'J_N=\pi(M).
\]

Transporting back to \(M\) gives the desired isomorphism. The upward trace formula for \(P\subseteq N\) says that the trace-preserving expectation from its basic construction to \(N\) sends \(e_P\) to \(d^{-1}1\). Hence \(E_N(f)=\lambda1\). \(\square\)

## Which projections can be downward Jones projections?

The scalar-expectation condition completely characterizes them.

**Theorem 4.5 — recognition and uniqueness.** Let \(f\in M\) be a projection with \(E_N(f)=\lambda1\). Then

\[
\begin{gathered}
P=N\cap\{f\}',\qquad [N:P]=d,\\
M=\langle N,f\rangle.
\end{gathered}
\]

is a downward basic construction. If \(g\) is another such projection, there is a unitary \(u\in N\) with \(g=ufu^*\). Conversely, every \(N\)-unitary conjugate of \(f\) has the same scalar expectation.

**Proof.** Since \(\tau(f)=\lambda\), the left \(N\)-dimension of \(K=L^2(M)f\) is one. The map

\[
V:L^2(N)\longrightarrow K,\qquad
V\widehat n=\lambda^{-1/2}\widehat{nf}
\]

is isometric, because

\[
\|nf\|_2^2=\tau(fn^*nf)
=\tau(n^*nE_N(f))=\lambda\|n\|_2^2.
\]

Its range is a closed \(N\)-submodule of dimension one, and so is all of \(K\). For \(x\in M\), there is therefore a unique \(a_x\in L^2(N)\) with \(xf=a_xf\). For \(n\in N\),

\[
\|na_x\|_2^2
=\lambda^{-1}\|nxf\|_2^2
\leq\lambda^{-1}\|x\|^2\|n\|_2^2.
\]

The tracial bounded-multiplier criterion shows that \(a_x\in N\), with \(\|a_x\|\leq\lambda^{-1/2}\|x\|\). To see this criterion directly, represent \(a_x\) as an affiliated \(L^2\)-operator. Testing the inequality on spectral projections of \(a_xa_x^*\) forces \(a_xa_x^*\leq\lambda^{-1}\|x\|^2\); hence it is bounded. Thus \(Mf=Nf\). Taking adjoints gives \(fM=fN\). The linear span \(NfN\) is consequently a two-sided ideal of \(M\). Its weak closure is nonzero and, since \(M\) is a factor, equals \(M\). This proves \(M=\langle N,f\rangle\).

Transport the left \(M\)-action to \(L^2(N)\) through \(V\), and write \(F=V^*L_fV\). The operator \(F\) commutes with \(J_N\). Indeed, its matrix coefficients are

\[
\langle F\widehat a,\widehat b\rangle
=\lambda^{-1}\tau(b^*faf),
\]

and tracial cyclicity gives exactly the same coefficient for \(J_NFJ_N\). Since the transported algebra is \(\langle N,F\rangle\), its conjugated commutant is

\[
J_N\langle N,F\rangle'J_N=N\cap\{F\}'=P.
\]

The same reciprocal-dimension calculation as in Theorem 4.4 gives \([N:P]=d\) and identifies the transported algebra with the basic construction of \(P\subseteq N\). Moreover \(F\widehat1=\widehat1\). Because \(F\) commutes with \(P\), its range contains \(L^2(P)\). Its range has \(P\)-dimension \(d\tau(f)=1\), the same as \(L^2(P)\). Faithfulness of the dimension trace forces equality. Thus \(F=e_P\), proving recognition with the actual Jones projection.

For uniqueness, \(\tau(f)=\tau(g)=\lambda\), so there is a unitary \(v\in M\) with \(vfv^*=g\). The coefficient argument above gives \(u\in N\) with \(uf=vf\). Then \(ufu^*=g\). Applying \(E_N\) gives \(\lambda uu^*=\lambda1\). In a finite algebra a coisometry is unitary, so \(u\in\mathcal U(N)\). The converse follows from bimodularity. \(\square\)

The factor \(P\) in the last proof is identified inside \(N\) before the basic-construction assertion. A projection merely having the right trace would not suffice; its full expectation must be scalar.

## The sharp constant at finite index

**Corollary 4.6.** For a finite-index II₁ inclusion, the largest constant \(c\geq0\) such that \(E_N(x)\geq cx\) for every \(x\in M_+\) is \(d^{-1}\). Also

\[
d^{-1}=\inf_{0\ne x\in M_+}
\frac{\|E_N(x)\|_2^2}{\|x\|_2^2}.
\]

**Proof.** The third lesson proves the lower bounds. Choose the projection \(f\) from Theorem 4.4. If \(E_N(f)\geq cf\), compression by \(f\) gives \(\lambda f\geq cf\), so \(c\leq\lambda\). Also

\[
\frac{\|E_N(f)\|_2^2}{\|f\|_2^2}
=\frac{\lambda^2}{\tau(f)}=\lambda.
\]

Thus both bounds are attained. \(\square\)

The corresponding nonsquared norm ratio has a different constant:

\[
\inf_{0\ne x\in M_+}
\frac{\|E_N(x)\|_2}{\|x\|_2}=d^{-1/2}.
\tag{4.1}
\]

Indeed, all the ratios are nonnegative, so taking square roots in Corollary 4.6 gives the lower bound. The same projection \(f\), with \(\tau(f)=\lambda\) and \(E_N(f)=\lambda1\), attains it: its two norms are \(\sqrt\lambda\) and \(\lambda\). Thus the operator-order constant and the squared-norm constant are \(\lambda\), while the nonsquared-norm constant is \(\sqrt\lambda\).

This distinction corrects the displayed norm formula in Takesaki's Theorem XIX.4.14. Its equation (14′) uses nonsquared \(L^2\)-norms but puts \([M:N]^{-1}\) on the left. At finite nontrivial index that constant is \([M:N]^{-1/2}\); equivalently, both norms must be squared to obtain the inverse index. The operator-order formula is retained. [Positivity restricts the index](positivity-and-index-rigidity.md), Theorem 7.5, proves the squared formula also at infinite index, where both norm constants are zero. At index one all three constants are one.

## Continuing downward

Apply Theorem 4.4 to \(P\subseteq N\), then repeat. This gives a **tunnel**

\[
\cdots\subseteq M_{-3}\subseteq M_{-2}\subseteq M_{-1}=N\subseteq M_0=M,
\]

in which every consecutive triple is a basic construction. Its Jones projections satisfy the same adjacent and distant relations as the upward projections. At any stage the next choice is unique up to a unitary in the current smaller factor, by Theorem 4.5. The tunnel is therefore an additional choice, whereas the upward tower is fixed by the original inclusion.

**Proposition 4.7 — the same convention at every integer level.** For every integer \(j\), the projection \(e_j\) implements \(M_{j-1}\subseteq M_j\), and

\[
\begin{gathered}
M_{j+1}=\langle M_j,e_j\rangle,\\
e_j\in M_{j+1}\cap M_{j-1}',\\
e_jxe_j=E_{M_{j-1}}(x)e_j,\\
E_{M_j}(e_j)=\lambda1.
\end{gathered}
\tag{4.2}
\]

Here the compression identity applies to \(x\in M_j\), and every expectation preserves the compatible normalized trace. The adjacent and distant relations of Theorem 4.2 hold for all integer indices.

**Proof.** Every consecutive triple in the downward construction is a basic construction by Theorems 4.4–4.5. The upward construction has the same property by Theorem 4.1. Applying the basic-construction compression and Markov identities to each such triple gives (4.2). The normalized traces agree: downward levels inherit the trace of \(M\), and upward traces restrict to that same trace. For distant indices, the later projection commutes with the earlier projection's containing factor. For adjacent indices, apply the calculation of Theorem 4.2 in their consecutive triple; no step depends on an index being nonnegative. This proves all the assertions. \(\square\)

In particular, \(e_{-1}\in M\) is the projection for \(P=M_{-2}\subseteq N=M_{-1}\), and \(M=\langle N,e_{-1}\rangle\). The already reserved \(e_0\in M_1\) is the projection for \(N\subseteq M\), while \(e_1\in M_2\) is the projection for \(M\subseteq M_1\). Naming the projection by the middle level avoids shifting it when the tunnel is introduced.

In later lessons we will ask for a tunnel whose finite-dimensional relative commutants generate the original factors. The existence of a tunnel alone says nothing about that stronger approximation property.

## Exercises

**Exercise 4.1 — introductory.** If \([M:N]=9\), compute \([M_3:N]\), \(\tau(e_2)\), and \(e_2e_3e_2\).

**Solution.** There are four consecutive inclusions from \(N=M_{-1}\) to \(M_3\), so multiplicativity gives \([M_3:N]=9^4=6561\). The Markov trace gives \(\tau(e_2)=1/9\), and the projection relation gives \(e_2e_3e_2=(1/9)e_2\).

**Exercise 4.2 — intermediate.** For \(N=Q\otimes1\subseteq Q\bar\otimes M_2\), construct a projection with expectation \(1/4\).

**Solution.** Choose matrix units \((a_{ij})_{i,j=1}^2\) for a unital \(M_2\)-subfactor of \(Q\), which exists by diffuse projection comparison. Put

\[
f=\frac12\sum_{i,j=1}^2 a_{ij}\otimes e_{ij}.
\]

Then \(f^*=f\), and multiplication of matrix units gives \(f^2=f\). Partial trace gives

\[
E_N(f)=\frac14\sum_i a_{ii}\otimes1=\frac14 1.
\]

The index is four, so Theorem 4.5 recognizes this as a downward Jones projection. It also witnesses the optimal inequality constant \(1/4\), even though scalar averaging on \(M_2\) alone has optimal constant \(1/2\).

**Exercise 4.3 — intermediate.** Why does a projection \(f\in M\) of trace \(1/d\) fail to satisfy the hypothesis of Theorem 4.5 automatically?

**Solution.** Trace preservation only gives \(\tau(E_N(f))=1/d\); it does not force \(E_N(f)\) to be scalar. In the tensor inclusion \(Q\otimes1\subseteq Q\bar\otimes M_2\), choose a projection \(a\in Q\) of trace \(1/4\) and set \(f=a\otimes1\). Then \(\tau(f)=1/4\), but \(E_N(f)=a\otimes1\ne(1/4)1\).

**Exercise 4.4 — advanced.** For index \(d\), find a partial isometry between adjacent Jones projections and its initial and final projections.

**Solution.** Set \(v=\lambda^{-1/2}e_{i+1}e_i\). The adjacent relations give

\[
\begin{gathered}
v^*v=\lambda^{-1}e_ie_{i+1}e_i=e_i,\\
vv^*=\lambda^{-1}e_{i+1}e_ie_{i+1}=e_{i+1}.
\end{gathered}
\]

Thus neighboring projections are equivalent inside the algebra they generate. This equivalence will later propagate central-support stabilization.

**Exercise 4.5 — intermediate.** For the actual index-four tensor inclusion and projection \(f\) of Exercise 4.2, compute both expectation-to-vector norm ratios. Determine the optimal constants for the operator-order and nonsquared-norm inequalities.

**Solution.** Since \(f\) is a projection of trace \(1/4\) and \(E_N(f)=\tfrac14 1\),

\[
\begin{gathered}
\|f\|_2=1/2,\qquad \|E_N(f)\|_2=1/4,\\
\frac{\|E_N(f)\|_2^2}{\|f\|_2^2}=1/4,\\
\frac{\|E_N(f)\|_2}{\|f\|_2}=1/2.
\end{gathered}
\]

Theorem 3.5 gives the universal lower bounds, and \(f\) attains both. The optimal nonsquared-norm constant is therefore \(1/2\). The optimal operator-order constant is \(1/4\): compressing \(E_N(f)\geq cf\) by \(f\) forces \(c\leq1/4\). In particular the larger norm constant cannot be used in that operator-order inequality.

**Exercise 4.6 — intermediate.** Which Jones projection implements \(M_{-4}\subseteq M_{-3}\)? Give its containing factor, its expectation onto the middle level and its generated basic construction. At nontrivial index, can it belong to the middle factor?

**Solution.** It is \(e_{-3}\in M_{-2}\), and

\[
\begin{gathered}
E_{M_{-3}}(e_{-3})=\lambda1,\\
M_{-2}=\langle M_{-3},e_{-3}\rangle.
\end{gathered}
\]

If it belonged to \(M_{-3}\), this expectation would instead fix it, giving \(e_{-3}=\lambda1\). At \(d>1\), the scalar \(0<\lambda<1\) is not a projection. Thus the projection lies in the next factor and not in the middle factor. At index one the projection is one and every tower and tunnel level agrees.

## References

- Claire Anantharaman and Sorin Popa, [*An introduction to II₁ factors*](https://www.math.ucla.edu/~popa/Books/IIun.pdf), open lecture notes.
- Masamichi Takesaki, *Theory of Operator Algebras III*, Springer, 2003, Chapter XIX, Theorem 4.14.
- Vaughan F. R. Jones, [*Index for subfactors*](https://doi.org/10.1007/BF01389127), Inventiones Mathematicae 72 (1983), 1–25.
- Mihai Pimsner and Sorin Popa, [*Entropy and index for subfactors*](https://www.numdam.org/item/ASENS_1986_4_19_1_57_0/), Annales scientifiques de l'École normale supérieure 19 (1986), 57–106.

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, September 2026; expanded October 2026. Self-checked by the writing AI. Public domain (CC0).*
