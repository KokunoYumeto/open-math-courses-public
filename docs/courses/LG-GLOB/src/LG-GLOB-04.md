# L-functions for GL_n: Godement–Jacquet and Rankin–Selberg

*Draft lesson. Written by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Public domain (CC0).*

For general linear groups, integral representations turn the Euler products of the preceding lesson into meromorphic functions with functional equations. Their poles detect whether two cuspidal representations are contragredient. That analytic test recovers a representation from almost all of its local parameters. It also recovers every constituent of an isobaric sum, including multiplicities and real norm twists.

We state the analytic constructions with their hypotheses and prove the uniqueness deductions. A boundary issue deserves particular attention: convergence for \(\operatorname{Re}s>1\) alone gives a weak local bound. Positivity and the complete self-pairing pole give the strict bound, and a second positivity argument proves nonvanishing on the line one. The prerequisites are *Automorphic representations and automorphic L-functions* and the adelic theory of Hecke L-functions. Basic free references are the author draft of Getz–Hahn, the author notes of Goldfeld–Jacquet, and the original papers of Jacquet–Shalika and Jacquet–Piatetski-Shapiro–Shalika.

The general local analytic identification in Theorem 2.1 and complete global continuation and pole theorem in Theorem 3.1 are stated below without their full proofs. The arguments in Sections 4–6 are conditional deductions from these precise statements. Section 1 proves general adelic reduction, the entire finite-place matrix zeta ideal and Fourier equation, general archimedean continuation and scalar Fourier identities in actual smooth dual-pair models, the complete canonical determinant-character theory, and general cuspidal admissibility and realization with compatible unitary tensor pairings. It proves the global standard-function argument over every number field from these results and the remaining standard-conductor/factor identification and canonical archimedean inputs. The degree-one and \(GL_2/\mathbb Q\) cases also have earlier proofs.

## 1. Normalizations and standard L-functions

Throughout, \(F\) is a number field and \(\mathbb A=\mathbb A_F\). Normalize the local absolute value by \(|\varpi_v|_v=q_v^{-1}\) at a finite place. Write \(\nu(g)=|\det g|_{\mathbb A}\), and write \(\widetilde\pi\) for the contragredient. Initially all cuspidal representations are unitary. In particular their central characters are unitary. A real norm twist will be explicitly indicated later.

At an unramified finite place, the normalized Satake parameter of a representation of \(GL_n(F_v)\) has eigenvalues \(\alpha_{1,v},\ldots,\alpha_{n,v}\). The normalization is the one for normalized parabolic induction: an unramified principal series induced from \(\chi_1,\ldots,\chi_n\) has eigenvalues \(\chi_i(\varpi_v)\). Its standard local factor is

\[
L_v(s,\pi)=\prod_{i=1}^n(1-\alpha_{i,v}q_v^{-s})^{-1}.
\tag{1.1}
\]

At a ramified finite place, the Godement–Jacquet integral defines the corresponding factor. At infinity one obtains products of

\[
\Gamma_{\mathbb R}(s)=\pi^{-s/2}\Gamma(s/2),\qquad
\Gamma_{\mathbb C}(s)=2(2\pi)^{-s}\Gamma(s).
\tag{1.2}
\]

We distinguish the finite product \(L_f(s,\pi)\), the product \(L_\infty(s,\pi)\) at infinity, and the complete product

\[
\mathcal L(s,\pi)=L_\infty(s,\pi)L_f(s,\pi).
\tag{1.3}
\]

Let \(\mathfrak f(\pi)\) be the finite conductor and put \(A(\pi)=|D_F|^nN\mathfrak f(\pi)\). With this convention the conductor-normalized completion is \(\Lambda(s,\pi)=A(\pi)^{s/2}\mathcal L(s,\pi)\). The two completions are different functions and have the same poles and zeros. The factor \(A^{s/2}\) moves the conductor out of the epsilon factor.

**Theorem 1.1 (Godement–Jacquet standard analytic theory).** Let \(\pi\) be a unitary cuspidal automorphic representation of \(GL_n(\mathbb A)\). The complete standard L-function continues meromorphically to \(\mathbb C\). If \(n\ge2\), it is entire. For \(n=1\), it is entire unless \(\pi=|\cdot|_{\mathbb A}^{it}\) for some real \(t\); in that exceptional case its only poles are simple poles at \(s=-it\) and \(s=1-it\). There is a constant \(\varepsilon(\pi)\) of absolute value one such that

\[
\mathcal L(s,\pi)
=\varepsilon(\pi)A(\pi)^{1/2-s}\mathcal L(1-s,\widetilde\pi),
\qquad
\Lambda(s,\pi)=\varepsilon(\pi)\Lambda(1-s,\widetilde\pi).
\tag{1.4}
\]

For the entire cases the completion is bounded in each closed vertical strip; in the exceptional case the same assertion holds after multiplication by \((s+it)(s-1+it)\).

The degree-one proof, including the pure-norm exception, is *Hecke L-functions and the Dedekind zeta function*, Theorem 10.1. The earlier \(GL_2/\mathbb Q\) proof is *Global Whittaker functions and the L-function of a cuspidal representation*, Theorems 3.1, 4.2 and 5.1. We now give the matrix-space argument for arbitrary \(n\ge2\) and arbitrary number fields. Its global steps are proved below. Proposition 1.1a proves general adelic reduction; Propositions 1.2–1.3 prove the unramified Fourier theory and the complete finite-place matrix ideal. Theorems 1.11 and 1.13 prove smooth comparison and compatible unitary tensor pairings for actual admissible Hilbert cusp constituents, with reverse comparison in Proposition 1.14 and Lemma 1.15. Theorem 1.17 proves the finite-place scalar Fourier equation in every rank, including ramification. Theorem 1.18 proves the full real/complex determinant-character Schwartz family. Theorem 1.25 proves exact Gaussian ideals, attainment, entire Schwartz division and scalar Fourier equations for all real/complex symmetric powers, their antiholomorphic companions, duals and norm twists. Theorem 1.19 proves realization and admissibility for every abstract cuspidal subquotient, including its unitary norm normalization. Theorems 1.21 and 1.22 prove general archimedean continuation and scalar Fourier identities in the stated smooth dual-pair models. Theorem 1.24 and Corollary 1.24c prove the nonnegative finite-place matrix epsilon exponent, and Corollary 1.24d bounds the reciprocal-factor degree by n. The remaining inputs are standard-factor and standard-conductor identification for general finite-place irreducibles, and the explicit archimedean standard-factor identification in 1.1c; Theorem 1.31 below proves the genuine Gaussian ideal and conjugation package in every prescribed actual dual-pair model; Proposition 1.16 supplies the exact finite-place determinant-character conductor and Tate-product factors. The global proof below is conditional on these precise remaining assertions. The freely accessible treatment being used is [Goldfeld–Jacquet, author notes, §§2–5 and 8–9](https://www.math.columbia.edu/~goldfeld/LanglandsBookChapter.pdf).

### The quotient and cusp estimates

Put \(d=[F:\mathbb Q]\), \(G=GL_n\), \(G^1=\ker\nu\), and \([G]^1=G(F)\backslash G^1\). For \(t>0\), let \(a_t\) be the central matrix whose entries at every infinite embedding are the positive real scalar \(t^{1/(nd)}\), and whose finite entries are \(I_n\). Then \(\nu(a_t)=t\), and

\[
G(\mathbb A)=a_{\mathbb R_{>0}}\times G^1.
\tag{1.5a}
\]

The positive center acts on a unitary irreducible representation by \(t^{i\tau}\), for some real \(\tau\). Replacing \(\pi\) by \(\pi_0=\pi\nu^{-i\tau}\) makes this action trivial. We first prove the assertions for \(\pi_0\), and restore the twist at the end.

For \(c>0\), define the positive diagonal cone

\[
A(c)=\left\{\operatorname{diag}(b_1,\ldots,b_n):
b_i>0,\ \prod_i b_i=1,\ b_i/b_{i+1}\ge c\right\}.
\tag{1.5b}
\]

Each \(b_i\) is embedded by the same real scalar at every infinite place and by \(1\) at every finite place.

**Proposition 1.1a (adelic reduction for every general linear group).** Let \(F\) be any number field, \(d=[F:\mathbf Q]\), \(G=GL_n\), and \(G^1=\{g\in G(\mathbb A_F):|\det g|_{\mathbb A}=1\}\). Put
\[
K=\prod_{v\text{ real}}O(n)\times
\prod_{v\text{ complex}}U(n)\times
\prod_{v<\infty}GL_n(\mathcal O_v).
\]
There are \(c>0\), a compact subset \(\Omega_N\subset N(\mathbb A_F)\), and a compact subset \(\Omega_T\) of the diagonal group whose individual entries have idèle norm one, such that
\[
G^1=G(F)\,\Omega_N A(c)\Omega_T K,
\]
where \(A(c)\) is exactly (1.5b): the entry \(b_i\) is the same positive real scalar at every infinite place and is one at every finite place, \(\prod_i b_i=1\), and \(b_i/b_{i+1}\ge c\). In particular, one such compact-factor set suffices for the covering requested there.

*Proof.* We use the proofs in The adèle ring of a number field, Theorem 2.2 and equations (10)–(11), giving additive compactness and integral-lattice representatives; Idèles and the idèle class group, Theorem 3.3, giving compact norm-one idèle representatives; and Lattices, Minkowski's theorem and the Minkowski embedding, Proposition 7.2, giving the full integer lattice in \(F_\infty\). We prove the remaining reduction steps below. The covering assertion is the classical one stated in [Goldfeld–Jacquet, Section 5, Theorem 5.1](https://www.math.columbia.edu/~goldfeld/LanglandsBookChapter.pdf); its statement fixes the conventional form of the covering.

**Two compact representative sets.** Write \(J^1=\{h\in\mathbb A_F^\times:|h|_{\mathbb A}=1\}\). Fix a compact set \(H\subset J^1\) mapping onto \(F^\times\backslash J^1\). This is supplied directly by the norm-one compactness proof: its compact set \(B_\eta\cap J^1\) represents every class. We may adjoin one to \(H\).

For \(\lambda>0\), let \(s_\lambda\) be the idèle equal to \(\lambda^{1/d}\) at every infinite place and to one at every finite place. Then \(|s_\lambda|_{\mathbb A}=\lambda\), since the complex absolute values are squared and \(r_1+2r_2=d\). Every idèle \(t\) can therefore be written
\[
t=a\,s_{|t|_{\mathbb A}}h,\qquad a\in F^\times,\quad h\in H.
\tag{1.5b.1}
\]
Also fix a compact additive representative set \(D_0\subset\mathbb A_F\) for \(F\backslash\mathbb A_F\), for example the compact closure of the domain in equation (11) of *The adèle ring of a number field*.

We shall use the following elementary compactness consequence. Every compact subset of \(\mathbb A_{F,f}^r\) is contained in \(m^{-1}\widehat{\mathcal O}_F^r\) for a positive rational integer \(m\). A finite cover by restricted-product neighborhoods involves only finitely many exceptional finite places; their finitely many coordinates have bounded valuations. A rational integer with sufficiently large powers of the underlying rational primes clears all these bounds. In particular the set \(H H^{-1}\), which is compact in the idèle topology and hence in the additive adèle topology, admits this kind of finite-coordinate bound.

**A least adelic projective height.** For a row vector \(z\in F_v^r\), use the local quantities
\[
\ell_v(z)=
\begin{cases}
\left(\sum_j|z_j|^2\right)^{1/2},&v\text{ real},\\
\sum_j|z_j|^2,&v\text{ complex},\\
\max_j|z_j|_v,&v<\infty.
\end{cases}
\]
They satisfy \(\ell_v(az)=|a|_v\ell_v(z)\), with the normalized field absolute values. They are invariant under the indicated local compact groups. At a finite place this follows by applying the integral-entry bound first to \(k\), then to \(k^{-1}\); at infinity it is the Euclidean or Hermitian isometry identity.

For \(g\in GL_r(\mathbb A_F)\) and \(0\ne x\in F^r\), define
\[
h_g(x)=\prod_v\ell_v(xg_v).
\tag{1.5b.2}
\]
Almost every factor is one, and the product is positive. The product formula makes it unchanged under \(x\mapsto ax\), \(a\in F^\times\), so it is a height on rational lines. For clarity, the product formula here follows from the principal-ideal norm formula proved in Norms of ideals, the ideal class group, and modules over Dedekind domains, Proposition 4.1: the finite norm product is \(|N_{F/\mathbf Q}(a)|^{-1}\), while the real and complex embedding product is \(|N_{F/\mathbf Q}(a)|\).

For fixed \(g\) and \(R>0\), only finitely many rational lines have height at most \(R\). To prove this, choose an idèle \(t\) with \(|t_v|_v=\ell_v(xg_v)\): at infinity use the ordinary Euclidean length as its positive component, and at a finite place choose a uniformizer power with the required valuation. Write \(t=a s_{h_g(x)}h\) as in (1.5b.1), and put \(x'=a^{-1}x\). The finite local lengths of \(x'g\) are bounded by the corresponding components of the fixed compact set \(H\); its ordinary infinite lengths are at most \(C R^{1/d}\), uniformly in \(h\). Multiplying by the fixed \(g^{-1}\) puts the finite coordinates of \(x'\) in one compact subset of \(\mathbb A_{F,f}^r\), and bounds its infinite coordinates.

Thus \(x'\in m^{-1}\mathcal O_F^r\) for one fixed positive integer \(m\), and its Minkowski embedding lies in a fixed bounded set. The integer-lattice proof of Proposition 7.2 shows that this set contains only finitely many such vectors: an inverse lattice-basis matrix bounds their integer coordinates. Every line of height at most \(R\) has one of these representatives. Choosing \(R=h_g(x_0)\) for any nonzero \(x_0\) now proves that the height has a positive attained minimum.

**Successively reduce the last row of each block.** For any \(GL_r(\mathbb A_F)\) matrix, choose a rational line of least height and extend one of its vectors to the last row of a matrix in \(GL_r(F)\). At each place, right multiplication by the local compact group sends this last row to \((0,\ldots,0,t_r)\). At infinity, extend the normalized row to an orthonormal basis: successively subtract its projections from the standard rows, then normalize the nonzero residuals. Orthogonality makes these rows independent, and the process ends with a full basis. At a finite place, divide the row by an entry of smallest valuation to make it primitive; one coordinate is a unit, and integral column operations carry it to the last coordinate. The upper-left \((r-1)\)-block is invertible.

These local choices form an element of the adelic compact group. Indeed, almost everywhere the matrix after the rational row change already belongs to \(GL_r(\mathcal O_v)\), and we can take its inverse as the local right compact factor, producing the identity matrix there. Now perform the same operation on the upper-left adelic block, and continue down to rank one. Embed every later rational change and right compact change in the preceding block, with identities on the remaining coordinates. This produces \(\gamma\in GL_n(F)\), \(k\in K\), and an upper triangular matrix
\[
T=\gamma gk,\qquad
T_{ii}=t_i\in\mathbb A_F^\times.
\]
For its upper-left \(r\)-block \(T^{(r)}\), the last coordinate line has least height:
\[
h_{T^{(r)}}(x)\ge h_{T^{(r)}}(e_r)=|t_r|_{\mathbb A}
\quad(0\ne x\in F^r).
\tag{1.5b.3}
\]
Here is why subsequent steps preserve this assertion. They multiply the first \(r-1\) rows by a rational invertible matrix, fixing \(e_r\), and multiply the first \(r-1\) columns by a compact matrix, preserving every local length. Rational row multiplication permutes all the rational lines on which the minimum was taken. Thus (1.5b.3), established when the \(r\)-block is first reduced, persists through every smaller-block step.

Write each diagonal idèle as \(t_i=a_i s_{|t_i|}h_i\), and multiply on the left by \(\operatorname{diag}(a_i^{-1})\in GL_n(F)\). This keeps (1.5b.3): on an \(r\)-block it is another rational row change, and the last row is rescaled by \(a_r^{-1}\), whose product of absolute values is one. Rename the resulting triangular matrix \(T\). Its entries are now
\[
t_i=b_i h_i,\qquad b_i=|t_i|_{\mathbb A}^{1/d}>0,\quad h_i\in H,
\]
where \(b_i\) denotes the prescribed equal positive scalar idèle. All compact and rational changes have determinant norm one, so for \(g\in G^1\) we have \(\prod_i b_i=1\).

**The adjacent diagonal ratios have a uniform lower bound.** Compactness of \(H H^{-1}\) gives a positive rational integer \(D\) and a real \(L\ge1\) such that, for every \(h,h'\in H\),
\[
|D h_v/h'_v|_v\le1\quad(v<\infty),\qquad
|h_v/h'_v|\le L\quad(v\mid\infty),
\tag{1.5b.4}
\]
where the latter absolute value is the ordinary real or complex modulus.

We also need a uniform simultaneous approximation, and supply its proof. Let
\[
U=\{z\in\mathbb A_F: |z_v|<1/4\ (v\mid\infty),\
z_v\in\mathcal O_v\ (v<\infty)\}.
\]
Its image in the compact additive quotient is open. Finitely many translates of that image cover the quotient; let their number be \(M\ge1\). For any \(u\in\mathbb A_F\), the \(M+1\) classes of
\(0,Du,2Du,\ldots,MDu\) have two in the same member of this cover. Subtract them. There are
\[
\beta=jD,\quad 1\le j\le M,\qquad \alpha\in F
\]
with
\[
|\beta u_v-\alpha|<1/2\quad(v\mid\infty),\qquad
\beta u_v-\alpha\in\mathcal O_v\quad(v<\infty).
\tag{1.5b.5}
\]
This uses only compactness of the additive quotient; \(\alpha\) is not required to be integral or bounded.

Set \(c=(2MDL)^{-1}\). Fix \(i<n\) and put \(r=i+1\). In the \(r\)-block write its \((i,r)\)-entry as \(u t_r\). If \(b_i/b_r<c\), apply (1.5b.5) to this \(u\). The nonzero rational row \(\beta e_i-\alpha e_r\), multiplied by \(T^{(r)}\), has only two possibly nonzero coordinates:
\[
\beta t_i,\qquad (\beta u-\alpha)t_r.
\]
At a finite place, its local length divided by \(|t_r|_v\) is
\[
\max\bigl(|\beta t_i/t_r|_v,|\beta u-\alpha|_v\bigr)\le1.
\]
Indeed \(b_i,b_r\) have finite components one, (1.5b.4) clears the ratio of \(h_i,h_r\), and the rational integer \(j\) is integral everywhere. At each infinite place,
\[
|\beta t_i/t_r|
\le MDL\,b_i/b_r<1/2,\qquad |\beta u-\alpha|<1/2.
\]
The Euclidean length ratio is therefore less than \(1/\sqrt2\); at a complex place its normalized local length ratio is the square of that number. Multiplying all these inequalities gives
\[
h_{T^{(r)}}(\beta e_i-\alpha e_r)<|t_r|_{\mathbb A},
\]
contradicting (1.5b.3). Thus \(b_i/b_{i+1}\ge c\) for every \(i\). The constant depends on the fixed arithmetic compact sets, not on \(g\), its rational flag, or its diagonal entries.

**Reduce the unipotent coordinates.** Write \(T=v\operatorname{diag}(t_i)\) with \(v\in N(\mathbb A_F)\). Every left \(N(F)\)-coset has a representative whose upper entries lie in \(D_0\). To verify this without invoking unipotent reduction theory, process each row \(i\), with columns \(j=i+1,\ldots,n\) in increasing order. Left multiplication by \(1+aE_{ij}\), \(a\in F\), adds \(a\) times row \(j\) to row \(i\). It changes entry \((i,j)\) by \(a\), does not change that row's earlier entries, and may change only its later upper entries. Choose \(a\) to put the current entry in \(D_0\). Later operations do not disturb the entries already fixed. The set \(\Omega_N\) of upper unitriangular matrices with every upper entry in \(D_0\) is compact, being the continuous coordinate image of the finite product \(D_0^{n(n-1)/2}\).

Consequently some \(q\in N(F)\) gives
\[
qT=\omega_N\,\operatorname{diag}(b_i)\,\operatorname{diag}(h_i),
\qquad \omega_N\in\Omega_N,\quad
\operatorname{diag}(b_i)\in A(c).
\]
Take \(\Omega_T=\{\operatorname{diag}(h_1,\ldots,h_n):h_i\in H\}\), a compact set with every diagonal entry of norm one. Undoing the rational and right compact changes proves the asserted equality.

For \(n=1\), the same assertion is simply \(J^1=F^\times H\); \(A(c)=\{1\}\) and the unipotent factor is trivial. Nonprincipal ideal classes are retained by the finite components of \(H\), rather than discarded by an assumption of a free integral lattice. Constant Weyl permutations belong to \(K\) at all places. There are no extra unbounded finite or Weyl factors in this proof. Since \(H\) is compact in the idèle restricted product, it has finitely many finite valuation patterns: outside one finite set its entries are units, and inside it each valuation ranges over a bounded set of integers. If desired, splitting \(\Omega_T\) according to those patterns expresses the same covering as finitely many compact-factor sets.

Finally, the positive central splitting in (1.5a) is unchanged: \(a_t\) has the scalar \(t^{1/(nd)}\) at every infinite place, its determinant norm is \(t\), and this proposition is applied to \(a_t^{-1}g\in G^1\). \(\square\)

Here are the consequences of Proposition 1.1a used below. Local Gram–Schmidt decomposition, or triangular reduction of an integral lattice at a finite place, gives \(G=NAK\). Conjugation by \(b\) on the entry \((i,j)\) of \(N\) has additive modulus \(|b_i/b_j|_{\mathbb A}\). Consequently the Iwasawa density is

\[
\delta_B(b)^{-1}\,du\,d^\times b\,dk,\qquad
\delta_B(b)=\prod_{i<j}|b_i/b_j|_{\mathbb A}.
\tag{1.5c}
\]

For the scalars in (1.5b), set \(\rho_i=b_i/b_{i+1}\) and
\(\beta(b)=(b_1/b_n)^d=\prod_i\rho_i^d\). In these coordinates
\(\delta_B(b)=\prod_i\rho_i^{d\,i(n-i)}\). The integral of this density over \(\rho_i\ge c\) is finite, because each exponent \(d\,i(n-i)\) is positive. The other factors in a Siegel set are compact. Proposition 1.1a therefore proves \(\operatorname{vol}[G]^1<\infty\). Also \(b^{-1}\Omega_Nb\) remains compact: its upper entries are multiplied by \(b_j/b_i\le c^{-(j-i)}\). Thus a Siegel representative has the form \(b\omega\), with \(\omega\) in a fixed compact set. Finally, solving \(\prod b_i=1\) in the \(\rho_i\) shows that every \(b_i^{\pm1}\), and hence every matrix height of \(b\), is bounded by a fixed power of \(\beta(b)\), times a constant.

**Lemma 1.1b (rapid decay).** Let \(\phi\) be a smooth, finite-level, \(K_\infty\)-finite cusp form in a unitary admissible automorphic realization, of moderate growth, with trivial positive-central action. For every \(M>0\) and every right differential operator \(D\),

\[
|R(D)\phi(b\omega)|\le C_{D,M}\beta(b)^{-M}
\tag{1.5d}
\]

on each of the sets above. In particular \(\phi\) is integrable, and its absolute value remains integrable after multiplication by any fixed power of the representative's matrix height.

**Proof.** We supply the smoothing and Fourier estimates. Fix a finite set of compact types and a finite level containing \(\phi\). Admissibility makes the resulting space \(E\) inside its irreducible representation finite-dimensional. Let \(P_E\) be its compact-type and level projector. A smooth compactly supported approximate identity \(h_\epsilon\) gives
\(T_\epsilon=P_E R(h_\epsilon)P_E\to I\) on \(E\). This convergence is in operator norm, since \(E\) is finite-dimensional. For small \(\epsilon\), \(T_\epsilon|_E\) is invertible. Its characteristic polynomial has nonzero constant term, so Cayley–Hamilton expresses \(I|_E\) as a polynomial in \(T_\epsilon\) with zero constant term. The corresponding finite sum of convolution powers is a smooth compactly supported kernel \(f\) on \(G^1\), with

\[
\phi(g)=\int_{G^1}\phi(h)f(g^{-1}h)\,dh.
\tag{1.5e}
\]

The compact projectors are compactly supported distributions; convolution with \(h_\epsilon\) makes their kernels smooth. Differentiating (1.5e) transfers derivatives to a compactly supported derivative of \(f\). Moderate growth of \(\phi\) therefore gives one polynomial growth exponent for all its right derivatives, with constants depending on the derivative. Right differentiation preserves cuspidality.

Apply Iwasawa decomposition to (1.5e) at \(g=b\omega\), and periodize the \(N\)-coordinate. The kernel becomes

\[
\sum_{\gamma\in N(F)}
f(\omega^{-1}b^{-1}\gamma u b' k),
\qquad u\in N(F)\backslash N(\mathbb A).
\tag{1.5f}
\]

For each subset \(\theta\) of the \(n-1\) simple cuts, let \(V_\theta\) be the upper unipotent radical with entries crossing at least one cut in \(\theta\), and \(N_\theta\) the upper unipotent group within the resulting diagonal blocks. Thus \(N=N_\theta\ltimes V_\theta\). Replace (1.5f) by

\[
\operatorname{Alt}
=\sum_{\theta\subset\{1,\ldots,n-1\}}(-1)^{|\theta|}
\int_{V_\theta(\mathbb A)}
\sum_{\gamma\in N_\theta(F)}
f(\omega^{-1}b^{-1}\gamma v u b' k)\,dv.
\tag{1.5g}
\]

The empty-set term is (1.5f). Every other term is left \(V_\theta(\mathbb A)\)-invariant as a function of \(u\): translating \(u\) merely changes the \(v\)-variable. It is also left \(N_\theta(F)\)-invariant. On integrating against \(\phi(ub'k)\), first integrate over \(V_\theta(F)\backslash V_\theta(\mathbb A)\). This is a proper-parabolic constant term and is zero. The compactness needed for these averages is proved in *Automorphic representations and automorphic L-functions*, Lemma 1.0. It follows directly for these upper unipotent groups by successive upper-diagonal additive quotients and compactness of \(F\backslash\mathbb A\). Thus the replacement does not change the integral.

Write upper unipotent matrices as \(1+X\), with \(X\) strictly upper triangular. If \(\xi\) lies in a block of \(N_\theta\) and \(X\) in the radical, then
\((1+\xi)(1+X)=1+\xi+(1+\xi)X\). The change of variables \(X\mapsto(1+\xi)X\) preserves additive measure: it is triangular with diagonal entries one. Apply additive Poisson summation to the block coordinates and integrate over the radical coordinates. Under the trace pairing the dual space consists of strictly lower triangular matrices. Inclusion–exclusion in (1.5g) leaves exactly those dual matrices \(\lambda\) whose nonzero coordinates cross, collectively, every simple cut. Indeed, a frequency supported within the blocks survives for every \(\theta\) disjoint from its crossed cuts; its total coefficient is \((1-1)^{\#\text{uncrossed cuts}}\). Therefore

\[
\delta_B(b')^{-1}\operatorname{Alt}
=\delta_B(bb'^{-1})
\sum_{\lambda}^{*}\widehat H(b^{-1}\lambda b),
\quad
H(X)=f\bigl(\omega^{-1}(1+X)b^{-1}ub\,b^{-1}b'k\bigr).
\tag{1.5h}
\]

The asterisk means that every cut is crossed by at least one nonzero coordinate. The Jacobian in (1.5h) is \(\delta_B(b)\), since \(X\mapsto bXb^{-1}\) scales the upper root spaces by that modulus. The trace pairing gives the displayed inverse conjugation on the lower dual space.

Choose compact representatives for \(N(F)\backslash N(\mathbb A)\). Their conjugates \(b^{-1}ub\) stay compact by the root-ratio bound. The support of \(f\) forces \(b^{-1}b'\) to lie in a fixed compact subset of the diagonal group, as follows by applying the diagonal Iwasawa projection to its argument. Consequently the \(H\) in (1.5h), and their Fourier transforms, have uniformly bounded Schwartz seminorms and a common compact finite support. Additive Fourier inversion and Poisson apply to these whole archimedean Schwartz functions, as in *Additive characters, self-dual measures and Poisson summation*, Theorems 5.4–5.5.

Here is the necessary number-field lattice bound. The finite support forces every coordinate of \(\lambda\) into a fixed fractional ideal. Its image in the full Minkowski space \(F_\infty\) is a lattice. A nonzero lattice vector has Euclidean norm at least \(c_1>0\). This uses the entire infinite block; a lower bound at each individual embedding would be false. An occupied lower coordinate \((j,i)\), \(i<j\), is scaled by \(b_i/b_j\), which is at least \(c^{j-i}\). Uniform Schwartz estimates imply, for arbitrary \(Q\) and sufficiently large \(N\),

\[
|\widehat H(b^{-1}\lambda b)|
\le C_{Q,N}
\prod_{\lambda_{ji}\ne0}(b_i/b_j)^{-Q}
\prod_{i<j}(1+\|\lambda_{ji}\|)^{-N}.
\tag{1.5i}
\]

To verify this inequality, apply a product Schwartz bound to the coordinate blocks. For each nonzero coordinate, use its lattice minimum \(c_1\) to extract the factor \((b_i/b_j)^{-Q}\); use the fixed lower bound on \(b_i/b_j\) for the remaining summable weight. Zero coordinates need no extracted factor.

The intervals belonging to the occupied coordinates cover all cuts. If a cut occurs \(m_i\ge1\) times, the extracted product is \(\prod_i\rho_i^{-Qm_i}\), bounded by a constant times \((b_1/b_n)^{-Q}\), since \(\rho_i\ge c\) and \(m_i\) has a fixed upper bound. Choose \(Q=dM\). The remaining lattice sum in (1.5i) is finite for sufficiently large \(N\), by lattice-point counting in real dimension \(d\) for each coordinate. We conclude that (1.5h) is \(O(\beta(b)^{-M})\) for every \(M\).

The remaining \(u,k,b' b^{-1}\) integrations range over compact sets. Moderate growth gives \(|\phi(ub'k)|\le C\beta(b)^C\). Absorb this fixed power by choosing \(M\) larger. This proves (1.5d); applying the same argument to right derivatives proves the stated derivative version. The integrability assertions follow from the finite-volume density (1.5c) and the polynomial height bound. \(\square\)

### Local data and the good-place calculation

For a Schwartz–Bruhat function \(\Phi_v\) on \(M_n(F_v)\) and a matrix coefficient \(c_v\) of \(\pi_v\), set

\[
Z_v(s,\Phi_v,c_v)=\int_{GL_n(F_v)}
\Phi_v(g)c_v(g)|\det g|_v^{s+(n-1)/2}\,d^\times g.
\tag{1.5}
\]

Use the trace pairing \((X,Y)\mapsto\psi_v(\operatorname{tr}(XY))\) and its self-dual additive measure to define \(\widehat\Phi_v\), and put \(c_v^\vee(g)=c_v(g^{-1})\). The following is precisely the local theory needed for the global argument.

**Local input 1.1c.** The local integrals continue meromorphically, and
\(H_v(s)=Z_v(s,\Phi_v,c_v)/L_v(s,\pi_v)\) is entire. At a finite place they span the fractional ideal generated by \(L_v=P_v(q_v^{-s})^{-1}\), \(P_v(0)=1\), over \(\mathbb C[q_v^s,q_v^{-s}]\). At an infinite place the \(K_v\)-finite coefficient and Gaussian-polynomial test family generates the corresponding factor over \(\mathbb C[s]\). In particular, at each exceptional place there is a finite identity

\[
L_v(s,\pi_v)=\sum_j p_{v,j}(s)Z_v(s,\Phi_{v,j},c_{v,j}),
\tag{1.5j}
\]

where \(p_{v,j}\in\mathbb C[q_v^s,q_v^{-s}]\) or \(\mathbb C[s]\), respectively. The archimedean generator has the gamma-factor normalization used in (1.2). The local functional equation is

\[
H_v(1-s,\widehat\Phi_v,c_v^\vee;\widetilde\pi_v)
=\epsilon_v(s,\pi_v,\psi_v)H_v(s,\Phi_v,c_v;\pi_v).
\tag{1.5k}
\]

For an unramified additive character at a finite place, the epsilon factor is \(w_vq_v^{a_v(1/2-s)}\), with \(a_v\ge0\) the standard conductor exponent. The archimedean epsilon factor is constant in the gamma normalization (1.2). At a good place the spherical integral is the distinguished generator and \(\epsilon_v=1\). The exponents \(a_v\) define \(\mathfrak f(\pi)=\prod_{v<\infty}\mathfrak p_v^{a_v}\) in this normalization. For the standard global trace character and self-dual measures we will consequently obtain

\[
\prod_v\epsilon_v(s,\pi_v,\psi_v)
=w(\pi) \bigl(|D_F|^nN\mathfrak f(\pi)\bigr)^{1/2-s}.
\tag{1.5l}
\]

The local normalizations commute with conjugation and duality for unitary representations, and an unramified norm twist shifts \(s\) without changing the finite conductor. Proposition 1.3 proves rational continuation, the principal matrix ideal, entire normalized quotients and generator attainment at every finite place, including ramification. Its generator is denoted \(L_{\mathrm{mat}}\); Theorem 2.3l below identifies it with the rank-one Rankin–Selberg factor for every actual generic irreducible; agreement with the chosen standard parameter remains part of the factor-identification input. Theorem 1.17 proves the scalar Fourier equation for every finite-place smooth admissible irreducible representation. Equations (1.7j)–(1.7m) then give an integral epsilon exponent, character scaling and the compatible-unitary phase. Theorem 1.24 and Corollary 1.24c prove nonnegativity of the matrix epsilon exponent for every finite-place irreducible; Corollary 1.24d proves the degree bound and its exponent-zero consequence. Standard-factor and standard-conductor identification remain unproved. At infinity, Theorems 1.21–1.22 prove full-Schwartz continuation and a scalar Fourier equation in actual smooth dual-pair models; Theorem 1.31 proves the canonical Gaussian ideal, finite attainment and compatible conjugation normalization in every prescribed actual dual-pair model; explicit standard-factor identification remains unproved. Proposition 1.21b and Corollary 1.22e supply canonical full-Schwartz division and constant epsilon under the precise Gaussian-ideal premise, while Corollary 1.22f proves the unitary scalar critical-line phase. Proposition 1.16 supplies the full finite-place Fourier equation, exact matrix/Tate-product factor and nonnegative conductor exponent for every determinant character, including ramification. Propositions 1.5–1.7 supply polynomial-module closure and the full Gaussian ideal for determinant characters over both real and complex fields; Theorem 1.18 supplies their full-Schwartz continuation, entire division and Fourier equation with exact phases. Theorem 1.25 supplies this entire canonical package for the explicit all-rank symmetric-power families and their duals, including exact Tate-product comparison and conjugation; Theorem 1.31 below extends Gaussian-ideal existence to every prescribed actual irreducible dual-pair model; its explicit standard-factor labels remain open. Proposition 1.2 proves the local functional equation with epsilon factor one at every unramified finite place, in every rank; the Satake inverse/conjugate calculations in Proposition 2.3 give their unramified duality and conjugation normalization. A determinant norm twist shifts the integral variable directly. The exact free source locators for the local integral theory are [Goldfeld–Jacquet, §2, Theorem 2.1 and Lemma 2.2; §3, Theorem 3.5, Lemma 3.6 and the subsequent generator construction](https://www.math.columbia.edu/~goldfeld/LanglandsBookChapter.pdf). The identification of the standard conductor exponent with the epsilon exponent is also part of the required local data; for the rank-one Rankin–Selberg definition of the standard function it is [Getz–Hahn, 22 April 2022 draft, Proposition 11.5.5 and Theorem 11.5.6](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf). Agreement of the two standard constructions belongs to this identification input. An unspecified local functional equation would not suffice to deduce (1.4).

The discriminant power in (1.5l) can be verified directly. If \(\psi_{v,a}(x)=\psi_v(ax)\), the self-dual measure on \(M_n(F_v)\) is multiplied by \(|a|_v^{n^2/2}\). Hence
\(\widehat\Phi^{\,\psi_{v,a}}(X)=|a|_v^{n^2/2}\widehat\Phi^{\,\psi_v}(aX)\).
In the transformed zeta integral change \(g\) to \(a^{-1}g\). The multiplicative matrix measure is unchanged, the coefficient contributes \(\omega_{\pi_v}(a)\), and the determinant weight contributes
\(|a|_v^{-n(1-s+(n-1)/2)}\). Comparing the local functional equations gives

\[
\epsilon_v(s,\pi_v,\psi_{v,a})
=\omega_{\pi_v}(a)|a|_v^{n(s-1/2)}
\epsilon_v(s,\pi_v,\psi_v).
\tag{1.5la}
\]

At a finite place the trace character has annihilator
\(\mathcal O_v^\perp=\mathfrak D_v^{-1}\), as proved in *Additive characters, self-dual measures and Poisson summation*, Proposition 5.1. Relative to a character with annihilator \(\mathcal O_v\), it is obtained by a parameter \(a\) of valuation \(d_v=\operatorname{ord}_v\mathfrak D_v\). Formula (1.5la) therefore contributes \(q_v^{nd_v(1/2-s)}\), times an \(s\)-independent central-character factor. Since \(\prod_vq_v^{d_v}=|D_F|\), multiplying the finite local conductor factors and the constant infinite factors proves (1.5l), with an \(s\)-independent nonzero constant \(w(\pi)\). Its absolute value will be proved globally below.

We can, however, compute the good-place integral and its convergence explicitly. Let \(v\) be finite, \(K_v=GL_n(\mathcal O_v)\) of volume one, and let the inducing unramified characters be \(\chi_1,\ldots,\chi_n\). In the normalized principal series the spherical function \(\varphi_0\) satisfies
\(\varphi_0(uak)=\delta_B(a)^{1/2}\prod_i\chi_i(a_i)\), and the normalized spherical coefficient is
\(c_v(g)=\int_{K_v}\varphi_0(kg)\,dk\). This is the coefficient of its spherical constituent, with the Satake identification of the preceding lesson. To verify the assertion even when the principal series is reducible, let \(\eta\) be its character on the one-dimensional compact fixed space. At a representative \(g\) of \(K_vgK_v\), integrating right translates of the fixed vector and evaluating at the identity gives \(\eta(\mathbf1_{K_vgK_v})=\operatorname{vol}(K_vgK_v)\int_{K_v}\varphi_0(kg)\,dk\). The normalized compact fixed vector in the irreducible spherical constituent gives the identical formula for its coefficient, because averaging its translates projects onto that fixed line. The two coefficients are therefore equal on every double coset. Take \(\Phi_v=\mathbf1_{M_n(\mathcal O_v)}\). Its left \(K_v\)-invariance removes the average in \(c_v\). For \(g=uak\), integrating its upper off-diagonal entries gives

\[
\int_{N(F_v)}\mathbf1_{M_n(\mathcal O_v)}(ua)\,du
=\prod_i\mathbf1_{\mathcal O_v}(a_i)|a_i|_v^{-(i-1)}.
\tag{1.5m}
\]

Indeed, each entry above the diagonal in column \(i\) is \(u_{ji}a_i\), so there are \(i-1\) independent additive integrals of volume \(|a_i|_v^{-1}\). Multiplying (1.5m), the Haar density \(\delta_B^{-1}\), the normalized induction factor \(\delta_B^{1/2}\), and \(|\det a|^{s+(n-1)/2}\), leaves the exponent \(s\) on every \(a_i\). Thus

\[
Z_v(s,\Phi_v,c_v)
=\prod_i\int_{F_v^\times}\mathbf1_{\mathcal O_v}(a_i)
\chi_i(a_i)|a_i|_v^s\,d^\times a_i
=\prod_i(1-\chi_i(\varpi_v)q_v^{-s})^{-1}.
\tag{1.5n}
\]

The last equality is the geometric series over the valuation of \(a_i\). This proves the value of the spherical integral. Proposition 1.2 below proves the additional generator identification and the full good-place functional equation, using a finite Smith-type basis of Hecke translates.

For a unitary coefficient, \(|c_v(g)|\le C_v\); for normalized unit spherical vectors \(C_v=1\). The same computation with \(c_v=1\) and exponent \(u=s+(n-1)/2\) gives

\[
\int_{G(F_v)}\mathbf1_{M_n(\mathcal O_v)}(g)\nu_v(g)^u\,dg
=\prod_{j=0}^{n-1}(1-q_v^{-(u-j)})^{-1}.
\tag{1.5o}
\]

Formula (1.5o) converges locally for \(\operatorname{Re}s>(n-1)/2\). Thus, for a unitary spherical coefficient, the left side of (1.5n) is holomorphic in this half-plane. The inducing-character computation was initially performed farther to the right, where its individual Tate integrals converge. The identity theorem extends (1.5n) to the unitary half-plane, so no uniform bound on the inducing characters was silently needed.

The product of the good-place absolute integrals converges whenever \(\operatorname{Re}s>(n+1)/2\): every exponent \(u-j\) then has real part greater than one. This uses the already proved convergence of the Dedekind zeta Euler product. At an exceptional place, multiplicative Haar measure on \(GL_n\) is a constant times \(|\det X|_v^{-n}dX\). This follows by applying the Jacobian \(|\det g|_v^n\) of left matrix multiplication. Consequently, if \(\operatorname{Re}s>(n+1)/2\), boundedness of a unitary coefficient reduces absolute convergence to the integrability of a Schwartz function times a positive power of \(|\det X|_v\). At a finite place its support is compact; at infinity \(|\det X|\) grows polynomially. Both integrals are finite, locally uniformly in \(s\); powers of \(\log|\det X|_v\) inserted by differentiation are absorbed by a smaller positive exponent near the singular locus. This proves a common initial half-plane without assuming temperedness.

### Why the spherical test is the local generator

Computing one integral does not ordinarily identify the generator of an integral family. In the unramified matrix case we can make that additional step: finite matrix congruences give a triangular basis of Hecke translates of the basic test.

**Proposition 1.2 (unramified local standard theory).** Let \(k=F_v\) be nonarchimedean, \(K=GL_n(\mathcal O)\), and let \(\tau\) be an irreducible admissible unramified unitary representation. Let \(\psi\) have conductor \(\mathcal O\): it is trivial on \(\mathcal O\), and \(\mathcal O\) is its own annihilator under \(\psi(xy)\). Put \(X=q^{-s}\) and \(R=\mathbb C[X,X^{-1}]\). For every Schwartz–Bruhat \(\Phi\) on \(M_n(k)\) and every smooth matrix coefficient \(c\) of \(\tau\),

\[
Z(s,\Phi,c)=L(s,\tau)Q_{\Phi,c}(X),
\qquad Q_{\Phi,c}\in R.
\tag{1.5oa}
\]

The integral family therefore generates exactly \(R\,L(s,\tau)\), with
\(L(s,\tau)=\prod_i(1-\alpha_iX)^{-1}\). Its normalized integrals are entire functions of \(s\), and

\[
\frac{Z(1-s,\widehat\Phi,c^\vee;\widetilde\tau)}
{L(1-s,\widetilde\tau)}
=\frac{Z(s,\Phi,c;\tau)}{L(s,\tau)}.
\tag{1.5ob}
\]

Thus the good-place standard generator and epsilon factor in 1.1c are proved: the epsilon factor is one and its conductor exponent is zero. No genericity hypothesis is needed for this assertion.

**Proof.** Write \(u=s+(n-1)/2\). Normalize multiplicative Haar measure by \(\operatorname{vol}K=1\). Let \(v_0\) be a spherical unit vector and
\(c_0(g)=\langle\tau(g)v_0,v_0\rangle\). The fixed line, its Hecke character \(\eta\), and its Satake parameter are established in *The unramified local correspondence and the Satake isomorphism*, Theorem 4.3 and Proposition 5.1. The calculation (1.5n), including its justification for a spherical constituent, gives
\(Z(s,\Phi_0,c_0)=L(s,\tau)\), where \(\Phi_0=\mathbf1_{M_n(\mathcal O)}\).

First prove a statement about the test functions, independently of the representation. Let \(\mathcal H=\mathcal H(GL_n(k),K)\) act by
\((T*\Phi)(A)=\int_G T(h)\Phi(h^{-1}A)\,dh\). We claim

\[
\mathcal S(M_n(k))^{K\times K}=\mathcal H*\Phi_0.
\tag{1.5oc}
\]

Here the right side means finite linear combinations of these convolutions.
For an integer \(N\ge1\) and a partition
\(N\ge\lambda_1\ge\cdots\ge\lambda_n\ge0\), set
\(t_\lambda=\operatorname{diag}(\varpi^{\lambda_1},\ldots,\varpi^{\lambda_n})\),
\(T_\lambda=\mathbf1_{Kt_\lambda K}\), and \(F_\lambda=T_\lambda*\Phi_0\).
The right cosets \(hK\) in this double coset correspond bijectively to the lattices
\(L=h\mathcal O^n\subset\mathcal O^n\) satisfying
\(\mathcal O^n/L\simeq\bigoplus_i\mathcal O/\varpi^{\lambda_i}\mathcal O\).
Indeed, changing the basis of \(L\) is right multiplication by \(K\), and integral row operations give its stated elementary divisors. Every such coset has measure one. Consequently, for \(A\in M_n(k)\),

\[
F_\lambda(A)=
\#\{L:\mathcal O^n/L\text{ has type }\lambda,\qquad
A\mathcal O^n\subset L\}.
\tag{1.5od}
\]

The number is finite, since every such \(L\) contains
\(\varpi^N\mathcal O^n\). The function is zero outside \(M_n(\mathcal O)\) and, inside that set, depends only on \(A\bmod\varpi^N\).

The \(K\times K\)-orbits of matrices modulo \(\varpi^N\) are indexed by the same partitions \(\mu\), allowing exponent \(N\) to represent a zero diagonal entry. To see this directly, choose a nonzero entry of smallest valuation, move it to the first diagonal position, and eliminate its row and column using integral operations. Every other entry is divisible by this pivot. Induction gives a diagonal matrix; permuting the entries orders the exponents. These operations over \(\mathcal O/\varpi^N\) lift to \(K\): a lift of an invertible matrix modulo \(\varpi^N\) has unit determinant. For uniqueness, the quotient
\(\mathcal O^n/(A\mathcal O^n+\varpi^N\mathcal O^n)\) has summands
\(\mathcal O/\varpi^{\mu_i}\mathcal O\). The dimensions of its successive
\(\varpi^{j-1}/\varpi^j\) layers count the \(\mu_i\ge j\), recovering every exponent. This also proves the elementary-divisor assertion for the lattices in (1.5od); equivalently one may use the integral pivot proof in Proposition 1.1 of the preceding lesson.

If \(A\) has truncated type \(\mu\), each lattice counted in (1.5od) gives a quotient of this finite module of type \(\lambda\). Its cardinality is \(q^{|\lambda|}\), where \(|\lambda|=\sum_i\lambda_i\); the original module has cardinality \(q^{|\mu|}\). Hence \(F_\lambda(A)=0\) when
\(|\lambda|>|\mu|\). If the cardinalities are equal, a surjection is an isomorphism, so the number is zero unless \(\lambda=\mu\). When they are equal, exactly one lattice occurs:
\(L=A\mathcal O^n+\varpi^N\mathcal O^n\).
Thus the square matrix of values \(F_\lambda(\mu)\), ordered by total size, is triangular with every diagonal entry one. It follows that the \(F_\lambda\) form a basis of all \(K\times K\)-invariant functions on \(M_n(\mathcal O/\varpi^N)\), extended by zero outside \(M_n(\mathcal O)\).

Every compactly supported locally constant test on \(M_n(\mathcal O)\) factors through one such congruence quotient. Compactness gives a finite cover by neighborhoods of constancy; a common sufficiently small additive subgroup preserves the entire function, including its zero set. More generally, compact support on \(M_n(k)\) lies in
\(\varpi^{-r}M_n(\mathcal O)\) for some \(r\ge0\). A central translate reduces it to the integral case. Its characteristic matrix test is also a Hecke translate:
\(\mathbf1_{\varpi^{-r}M_n(\mathcal O)}=T_{\varpi^{-r}I}*\Phi_0\).
Combining this central translation with the preceding finite expansion proves (1.5oc).

Now apply the integral to these functions. Since \(T_\lambda\) is bi-invariant, the operator \(\tau(T_\lambda)\) has image in the spherical line and vanishes on its orthogonal complement: averaging on both sides gives
\(\tau(T_\lambda)=P_K\tau(T_\lambda)P_K=\eta(T_\lambda)P_K\).
Consequently
\(\int T_\lambda(h)c_0(hx)\,dh=\eta(T_\lambda)c_0(x)\).
Changing \(g=hx\) and using that the determinant norm is constant on the double coset gives

\[
Z(s,F_\lambda,c_0)
=q^{-|\lambda|u}\eta(T_\lambda)\,
Z(s,\Phi_0,c_0).
\tag{1.5oe}
\]

The multiplier is a constant times \(X^{|\lambda|}\). A central translate gives an integral power of \(X\), possibly negative. Equation (1.5oc) therefore proves (1.5oa) for all bi-invariant tests with coefficient \(c_0\). For any test with that coefficient, averaging on the left and right over \(K\) preserves its integral; its average is again Schwartz–Bruhat.

It remains to include every coefficient. Irreducibility implies that every smooth vector is a finite linear combination of translates of \(v_0\). Admissibility identifies the smooth contragredient with the conjugate smooth vectors in the invariant Hermitian pairing: a smooth functional fixed by a compact open \(J\) factors through the finite-dimensional space \(\tau^J\), where it is represented by a vector; averaging over \(J\) extends that identity to the entire smooth representation. Thus every smooth coefficient is a finite linear combination of
\(c_0(b^{-1}ga)\), \(a,b\in G\).
For such a coefficient put \(d_{b,a}=|\det b/\det a|\) and
\(\Phi_{b,a}(x)=\Phi(bxa^{-1})\). Unimodularity and substitution give

\[
Z(s,\Phi,c_0(b^{-1}(\,\cdot\,)a))
=d_{b,a}^{\,u}Z(s,\Phi_{b,a},c_0).
\tag{1.5of}
\]

The determinant norm is an integral power of \(q\), so this adds only a Laurent monomial in \(X\). We have proved rational continuation, the entire normalized quotient, and divisibility by \(L\) for every coefficient. Conversely the basic integral is exactly \(L\); hence the fractional ideal is precisely \(R\,L\). Its prescribed polynomial has constant term one by (1.5n).

Finally prove the functional equation for the whole family, rather than only for the basic test. Self-dual additive measure for conductor-zero \(\psi\) gives
\(\widehat\Phi_0=\Phi_0\). For one coordinate this is the compact-character integral: the transform of \(\mathbf1_{\mathcal O}\) is its volume times the indicator of its annihilator, and inversion forces that volume to be one. The finite Cartesian product with the trace pairing merely permutes the matrix coordinates. The inversion and coset-indicator proof is *Additive characters, self-dual measures and Poisson summation*, Proposition 5.2, after scaling the local character to conductor zero.

Left matrix multiplication by \(h\) has additive Jacobian
\(|\det h|^n\). Under the trace pairing,

\[
\widehat F_\lambda(Y)
=\int_G T_\lambda(h)|\det h|^n\Phi_0(Yh)\,dh.
\tag{1.5og}
\]

Write \(u'=(1-s)+(n-1)/2=n-u\). In the dual integral substitute \(x=gh\). Then
\(c_0^\vee(xh^{-1})=c_0(hx^{-1})\); integrating the \(h\)-variable uses the same Hecke character \(\eta(T_\lambda)\), rather than an incorrectly inverted determinant multiplier. We obtain

\[
Z(1-s,\widehat F_\lambda,c_0^\vee)
=q^{-|\lambda|u}\eta(T_\lambda)\,
Z(1-s,\Phi_0,c_0^\vee).
\tag{1.5oh}
\]

The basic dual integral is \(L(1-s,\widetilde\tau)\), by the already proved good-place calculation applied to the contragredient. This proves (1.5ob) for \(F_\lambda\), and the same substitution proves it for their central translates. All substitutions first take place in a half-plane of absolute convergence of the relevant integral; (1.5og) is an identity of compactly supported tests, and the resulting identities extend as rational functions. No common convergence half-plane for \(s\) and \(1-s\) is needed.

Bi-invariant averaging commutes with Fourier transformation: changing
\(A\mapsto k_1Ak_2\) transforms the dual argument to
\(k_2^{-1}Yk_1^{-1}\), and the Jacobian is one. Thus (1.5oc) and linearity extend the equation to every \(\Phi\) with coefficient \(c_0\).
For the translated coefficient in (1.5of), its dual is
\(c_0^\vee(a^{-1}(\,\cdot\,)b)\), and

\[
\widehat{\Phi_{b,a}}(Y)
=d_{b,a}^{-n}\widehat\Phi(aYb^{-1}).
\tag{1.5oi}
\]

The dual substitution contributes \(d_{b,a}^{-u'}\), and (1.5oi) contributes \(d_{b,a}^n\). Their product is
\(d_{b,a}^{n-u'}=d_{b,a}^u\), exactly the multiplier in (1.5of).
This proves the equation for every coefficient and every test. The epsilon factor is one; for the unramified representation the standard epsilon exponent is therefore zero. The additive-character change (1.5la) supplies the equation for any other local character without importing a ramified-representation theorem. \(\square\)


### Finite-place matrix zeta ideals

Let \(F\) be any nonarchimedean local field, with integers \(\mathcal O\),
uniformizer \(\varpi\), and residue cardinality \(q\). Set
\(G=\mathrm{GL}_n(F)\), \(K=\mathrm{GL}_n(\mathcal O)\), and
\(\nu(g)=|\det g|\), with \(|\varpi|=q^{-1}\). Normalize \(dg\) by
\(\operatorname{vol}(K)=1\). For an irreducible smooth admissible
representation \((\pi,V)\), a smooth dual vector \(\ell\), and \(v\in V\), write
\[
c(g)=\ell(\pi(g)v),\qquad
Z(s,\Phi,c)=\int_G\Phi(g)c(g)\nu(g)^{s+(n-1)/2}\,dg,
\qquad X=q^{-s}.
\]
Here \(\Phi\) is any locally constant compactly supported function on
\(M_n(F)\). Admissibility means that \(V^J\) is finite-dimensional for
every compact open \(J\). It is an explicit hypothesis throughout.

**Proposition 1.3 (finite-place rationality and the fractional ideal).**
In every rank, all these integrals converge absolutely in a right
half-plane and continue to rational functions of \(X\). Their complex
linear span is
\[
\mathcal I_\pi=\frac{1}{P_\pi(X)}\mathbb C[X,X^{-1}],
\qquad P_\pi\in\mathbb C[X],\quad P_\pi(0)=1.
\]
The polynomial is unique. In particular
\(L_{\mathrm{mat}}(s,\pi)=P_\pi(q^{-s})^{-1}\) has no zeros, and its
reciprocal is entire in \(s\). Every quotient
\(Z(s,\Phi,c)/L_{\mathrm{mat}}(s,\pi)\) is a Laurent polynomial in
\(q^{-s}\), hence is entire in \(s\), and a finite sum of actual
integrals attains the generator. This assertion includes every ramified
admissible irreducible representation; it does not require genericity or
a classification of its Jacquet modules.

#### 1. Compact averaging and the dual

For a compact open subgroup \(J\), the average
\(e_Jv=\int_J\pi(j)v\,dj\), with probability Haar measure, is a finite sum
on each smooth vector and projects onto \(V^J\). Every functional on
the finite-dimensional space \(V^J\), composed with \(e_J\), is a
smooth dual vector fixed by \(J\). Thus
\[
(\widetilde V)^J=(V^J)^*
\]
under the natural pairing.

The smooth dual \(\widetilde V\) is irreducible. Indeed, a nonzero
invariant subspace \(W\subset\widetilde V\) has annihilator zero in
\(V\): that annihilator is invariant, and irreducibility of \(V\)
excludes any other proper possibility. Consequently the restrictions
of \(e_JW\) to \(V^J\) separate \(V^J\). A subspace of its
finite-dimensional dual which separates it is the full dual. Hence
\((\widetilde V)^J\subset W\) for every \(J\), and smoothness gives
\(W=\widetilde V\). The same finite-dimensional pairing identifies the
smooth double dual with \(V\).

Every central element acts by a scalar. To see this, choose a nonzero
finite-dimensional \(V^J\). Its action preserves this space and has an
eigenvector over \(\mathbb C\). The corresponding eigenspace in \(V\)
is invariant under \(G\), so is all of \(V\). These scalars form a
smooth character \(\omega_\pi:F^\times\to\mathbb C^\times\).

#### 2. A positive diagonal semigroup on a finite fixed space

Fix \(r\geq1\) and put \(J=1+\varpi^rM_n(\mathcal O)\).
This subgroup is normal in \(K\). Gaussian elimination using pivots
in \(1+\varpi^r\mathcal O\) gives
\[
J=J^+J^0J^-,
\]
where \(J^+\) and \(J^-\) are respectively upper and lower unipotent
matrices congruent to the identity modulo \(\varpi^r\), and \(J^0\)
is the diagonal subgroup with entries in \(1+\varpi^r\mathcal O\).
For completeness, eliminate the last row and last column using the
bottom-right unit pivot. Their off-diagonal entries are in
\(\varpi^r\mathcal O\); the remaining Schur complement is again
the identity modulo \(\varpi^r\). Induction gives the displayed
upper-diagonal-lower factorization, with all its factors in \(J\).

For integers \(\lambda_1\geq\cdots\geq\lambda_n\), put
\(a_\lambda=\operatorname{diag}(\varpi^{\lambda_1},\ldots,
\varpi^{\lambda_n})\). If \(a=a_\lambda\) and \(b=a_\mu\) are both
of this form, then
\[
aJ^+a^{-1}\subset J^+,\qquad
b^{-1}J^-b\subset J^-,\qquad [a,J^0]=[b,J^0]=1.
\]
The first assertion follows because an upper entry is multiplied by
\(\varpi^{\lambda_i-\lambda_j}\) with \(i<j\); the second follows
by the corresponding lower-entry calculation. Therefore
\[
JaJbJ=JabJ.                                                    \tag{1.7a}
\]
The inclusion from left to right follows by inserting the factorization
of the middle \(J\) and absorbing its three factors. The reverse
inclusion follows by taking that middle element to be the identity.

The compactly supported probability measure
\(\mu_a=e_J*\delta_a*e_J\) is invariant under left and right \(J\).
By (1.7a), \(\mu_a*\mu_b\) is a bi-\(J\)-invariant probability
measure on \(JabJ\). Such a measure is unique: \(J\times J\) acts
transitively on that compact double coset, and averaging a continuous
function over \(J\times J\) gives a constant there. Consequently
\[
\mu_a*\mu_b=\mu_{ab}.
\]
On \(E=V^J\), let \(T_a=e_J\pi(a)e_J|_E\). It follows that
\[
T_aT_b=T_{ab}.                                                \tag{1.7b}
\]
In particular the \(n\) commuting operators
\[
T_i=T_{\operatorname{diag}(\varpi I_i,I_{n-i})},\quad 1\leq i\leq n,
\qquad T_n=\omega_\pi(\varpi)\operatorname{id}_E               \tag{1.7c}
\]
control every dominant diagonal. Negative central powers are allowed,
since \(T_n\) is invertible.

#### 3. The Cartan sum and its volume

Elementary row and column operations over the discrete valuation ring
give
\[
G=\coprod_{\lambda_1\geq\cdots\geq\lambda_n}Ka_\lambda K.
\tag{1.7d}
\]
One proof first multiplies a matrix by a scalar to make its entries
integral, moves an entry of smallest valuation into a pivot position,
and eliminates its row and column by integral invertible operations.
Apply induction to the remaining block and arrange the valuations
in decreasing order. Uniqueness follows because the ideals generated
by the \(i\)-rowed minors are unchanged by these operations: their
valuations recover the successive partial sums of the smallest
diagonal valuations. This also proves disjointness in (1.7d).

Put \(d_i=\lambda_i-\lambda_{i+1}\) for \(i<n\). Let \(b_1,\ldots,b_t\)
be the sizes of the successive equal-entry blocks in \(\lambda\).
The exact volume is
\[
\operatorname{vol}(Ka_\lambda K)=
q^{\sum_{i=1}^{n-1}i(n-i)d_i}\,
\frac{\prod_{j=1}^n(1-q^{-j})}
{\prod_{\alpha=1}^t\prod_{j=1}^{b_\alpha}(1-q^{-j})}.
\tag{1.7e}
\]
Here is the counting argument. The volume is the index of
\(K\cap a_\lambda Ka_\lambda^{-1}\) in \(K\). The intersection
requires its \((i,j)\) entry, for \(i<j\), to be divisible by
\(\varpi^{\lambda_i-\lambda_j}\); lower entries have no additional
condition. Modulo \(\varpi\) this is the lower block parabolic with
the indicated block sizes. Counting ordered bases gives
\[
|\mathrm{GL}_m(\mathbb F_q)|
=q^{m^2}\prod_{j=1}^m(1-q^{-j}).
\]
Thus the residue index contributes one power of \(q\) for each
cross-block upper entry, together with the ratio of products in
(1.7e). Beyond the first congruence, such an entry contributes
\(q^{\lambda_i-\lambda_j-1}\). These are independent entry
conditions on matrices with invertible residue. Their total exponent
is \(\sum_{i<j}(\lambda_i-\lambda_j)
=\sum_i i(n-i)d_i\), as claimed.

For an integrable function on \(Ka_\lambda K\), its integral is its
volume times its average over \(k_1a_\lambda k_2\), \(k_1,k_2\in K\),
with probability measure on \(K\times K\). This follows from the
same uniqueness of an invariant probability measure used above.
The multiplicative Haar measure is bi-invariant: explicitly it is
a positive constant times \(|\det g|^{-n}d g_{\mathrm{add}}\).
Left or right multiplication by a matrix \(h\) changes additive
matrix measure by \(|\det h|^n\), which proves the assertion.

Choose \(J\) small enough to fix both \(v\) and \(\ell\). Since it
is normal in \(K\), every \(k_1,k_2\) gives \(J\)-fixed vectors
\(\ell'=\ell\pi(k_1)\), \(v'=\pi(k_2)v\), and there are only finitely
many such choices. On a dominant diagonal,
\[
c(k_1a_\lambda k_2)=\ell'(T_{a_\lambda}v').
\tag{1.7f}
\]
If the support of \(\Phi\) lies in
\(\varpi^{-B}M_n(\mathcal O)\), then \(\lambda_n\geq-B\) on the
Cartan cosets which meet it. Indeed integral invertible left and
right multiplication preserves the maximum absolute matrix-entry
norm. Write
\[
\lambda=(-B,\ldots,-B)+
\sum_{i=1}^n k_i(\underbrace{1,\ldots,1}_{i},0,\ldots,0),
\quad k_i\geq0.
\]
Equations (1.7b), (1.7e), and (1.7f), together with boundedness of
\(\Phi\), bound the absolute integral by a constant times
\[
\sum_{k_1,\ldots,k_n\geq0}
\prod_{i=1}^n
\left(q^{i(n-i)-i(\Re s+(n-1)/2)}
\max(1,\|T_i\|)\right)^{k_i}.
\]
For \(i=n\) the term \(i(n-i)\) is zero. Every factor is less than
one when \(\Re s\) is sufficiently large. This proves absolute
convergence before any averaging of \(\Phi\).

#### 4. A common denominator, independent of the test

We can now average \(\Phi\) on the left and right by \(J\).
Since \(c\) is bi-\(J\)-invariant, its zeta integral is unchanged.
Choose \(R\geq0\) so that this averaged test is invariant under
addition by \(\varpi^RM_n(\mathcal O)\). Such a uniform \(R\)
exists for a locally constant compactly supported function: cover
its compact support by finitely many constant additive cosets and
refine them to one common lattice. Outside their union the function
is zero on each coset of that lattice as well.

For each dominant \(\lambda\), let \(h\) be the number of entries
\(\lambda_j\geq R\). The remaining entries
\[
m_{h+1}\geq\cdots\geq m_n,\qquad -B\leq m_j<R,
\]
have only finitely many possibilities. On each such region,
\(\Phi(k_1a_\lambda k_2)\) is independent of the first \(h\)
diagonal entries: replace them by zero. The replacement changes
the matrix by an element of \(\varpi^RM_n(\mathcal O)\), even
after multiplication by \(k_1,k_2\).

For \(h>0\), take the base
\(\lambda^0=(R,\ldots,R,m_{h+1},\ldots,m_n)\). Every member of the
region has the unique expression
\[
\lambda=\lambda^0+
\sum_{i=1}^h k_i(\underbrace{1,\ldots,1}_{i},0,\ldots,0),
\quad k_i\geq0,
\]
where \(k_i\) for \(i<h\) are successive gaps, and
\(k_h=\lambda_h-R\). Split each \(k_i\), \(i<h\), into the cases
zero and at least one. On each resulting region the equal-entry
block pattern, and hence the product ratio in (1.7e), is constant.
If \(h<n\), its boundary gap is already positive because
\(R>m_{h+1}\). If \(h=n\), the variable \(k_n\) is central and
does not change any gap.

Put
\[
z_i(X)=q^{\,i(n-i)-i(n-1)/2}X^i,\qquad
D_J(X)=\prod_{i=1}^n\det(1-z_i(X)T_i).                         \tag{1.7g}
\]
In every region the Cartan sum is a constant, a Laurent monomial,
and a finite-dimensional matrix element of products of series
\[
\sum_{k\geq0}(z_iT_i)^k=(1-z_iT_i)^{-1},\qquad
\sum_{k\geq1}(z_iT_i)^k=z_iT_i(1-z_iT_i)^{-1}.
\]
The formulas hold in the right half-plane just proved, and
adjugates give their rational continuations. The regions with
\(h=0\) contain finitely many diagonals. The \(K\times K\) average
is a finite average, since both the coefficient and the averaged
test are bi-\(J\)-invariant and \(J\) is normal in \(K\).
We have therefore proved
\[
Z(s,\Phi,c)\in D_J(X)^{-1}\mathbb C[X,X^{-1}]
\quad\hbox{for every }\Phi,\qquad D_J(0)=1.                   \tag{1.7h}
\]
\(D_J\) depends on the fixed coefficient space, not
on the support or constancy radius of the test.

Choose once and for all \(v_0,\ell_0\) with
\(\ell_0(v_0)=1\), and a principal congruence \(J\) fixing them.
Irreducibility of \(V\) and \(\widetilde V\) means that every
coefficient is a finite linear combination of
\(c_0(a^{-1}gb)\), where \(c_0(g)=\ell_0(\pi(g)v_0)\).
The substitution \(g=ax b^{-1}\) turns its integral into the
integral with coefficient \(c_0\), test \(\Phi(axb^{-1})\), and
factor \(\nu(ab^{-1})^{s+(n-1)/2}\). This factor is a nonzero
constant times a Laurent monomial in \(X\). Thus (1.7h) supplies
one common denominator for every test and every coefficient.

#### 5. From that denominator to the canonical generator

Let \(\mathscr R=\mathbb C[X,X^{-1}]\). Simultaneously replacing
\(\Phi(g),c(g)\) by \(\Phi(gh),c(gh)\), with
\(\det h=\varpi\), multiplies the integral by
\(q^{s+(n-1)/2}\). The inverse translation gives the inverse
factor. Therefore the complex span \(\mathcal I_\pi\) is an
\(\mathscr R\)-submodule of \(D_J^{-1}\mathscr R\).
It contains 1: take
\(\Phi=\operatorname{vol}(J)^{-1}1_J\) and \(c=c_0\).
The test is a Schwartz function on the matrix space, and on \(J\)
the coefficient and determinant norm are both 1.

The Laurent polynomial ring is a principal ideal domain. Indeed
clear powers of \(X\) and use the usual Euclidean division in
\(\mathbb C[X]\); localizing permits precisely the additional
units \(cX^m\). Write \(D_J\mathcal I_\pi=A\mathscr R\).
Since \(1\in\mathcal I_\pi\), \(A\) divides \(D_J\). Choose its
polynomial representative with nonzero constant term. The quotient
\(D_J/A\), normalized to have constant term 1, is \(P_\pi\).
This proves Proposition 1.3. If two such normalized polynomials
give the same ideal, their ratio is \(cX^m\); their nonzero
constant terms force \(m=0\), and normalization forces \(c=1\).
The generator is a finite linear combination of actual matrix
zeta integrals, because \(\mathcal I_\pi\) was their span. Multiplying
an integral by a Laurent monomial can also be absorbed into the
simultaneous translations just used. \(\square\)

#### 6. Consequences of a scalar Fourier equation

Take a unitary additive character \(\psi\), the trace-pairing
Fourier transform
\[
\widehat\Phi(Y)=\int_{M_n(F)}\Phi(X)\psi(\operatorname{tr}(XY))\,dX
\]
with self-dual additive measure, and \(\check c(g)=c(g^{-1})\).
Here inversion can be checked directly, as in the earlier
proof in *Additive characters, self-dual measures and Poisson
summation on the adèles*, Propositions 5.1–5.2.
The annihilator of \(\mathcal O\) is a fractional ideal
\(\varpi^h\mathcal O\). Indeed continuity puts the image of
some \(\varpi^r\mathcal O\) in a small arc around 1; a subgroup
of the circle contained in such an arc is trivial. The
annihilator is therefore open, is an \(\mathcal O\)-submodule,
and is proper by nontriviality of \(\psi\), so has the stated
form. The annihilator of \(\varpi^r\mathcal O\) is
\(\varpi^{h-r}\mathcal O\). Giving \(\mathcal O\) mass
\(q^{h/2}\), character orthogonality gives
\[
\widehat{1_{a+\varpi^r\mathcal O}}(y)
=\operatorname{vol}(\varpi^r\mathcal O)\,
\psi(ay)1_{\varpi^{h-r}\mathcal O}(y).
\]
Applying this twice yields \(1_{a+\varpi^r\mathcal O}(-x)\),
since the two subgroup volumes multiply to 1. Every scalar
Schwartz function is a finite sum of such indicators.
The matrix trace pairing is \(\sum_{i,j}X_{ij}Y_{ji}\),
a product of scalar pairings followed by coordinate permutation.
Refining a matrix Schwartz function to one common additive
matrix lattice gives a finite sum of products of scalar
indicators. Thus
\(\widehat{\widehat\Phi}(X)=\Phi(-X)\) on the whole matrix space.
Theorem 1.17 below proves that one scalar independent of
both test and coefficient satisfies
\[
Z(1-s,\widehat\Phi,\check c)
=\gamma(s,\pi,\psi) Z(s,\Phi,c)                         \tag{1.7i}
\]
for all the tests and coefficients. With that existence theorem, the proved fractional ideal gives the following algebraic consequences. Taking
a pair whose integral is 1 shows that \(\gamma\) is rational
in \(X\). Fourier transformation and coefficient inversion are
bijections of the respective families, so (1.7i) identifies their
entire fractional ideals. The dual variable
\(q^{-(1-s)}=q^{-1}X^{-1}\) generates the same Laurent ring.
Hence
\[
\gamma(s,\pi,\psi)=\epsilon(s,\pi,\psi)
\frac{L_{\mathrm{mat}}(1-s,\widetilde\pi)}
{L_{\mathrm{mat}}(s,\pi)},\qquad
\epsilon(s,\pi,\psi)=cX^m,\quad c\ne0,\quad m\in\mathbb Z.       \tag{1.7j}
\]
Indeed the ratio after dividing out the two ideal generators
must be a unit of \(\mathscr R\).

Fourier inversion gives \(\widehat{\widehat\Phi}(X)=\Phi(-X)\).
Applying (1.7i) twice, with the same character \(\psi\), therefore gives
\[
\gamma(s,\pi,\psi)\gamma(1-s,\widetilde\pi,\psi)
=\epsilon(s,\pi,\psi)\epsilon(1-s,\widetilde\pi,\psi)
=\omega_\pi(-1).                                           \tag{1.7k}
\]
The central sign is essential with this positive trace convention:
substituting \(g\mapsto-g\) in \(Z(s,\Phi(-\,\cdot),c)\) multiplies
it by \(\omega_\pi(-1)\).

For \(\psi_a(x)=\psi(ax)\), self-dual matrix measure is multiplied
by \(|a|^{n^2/2}\). Thus
\(\widehat\Phi^{\,\psi_a}(Y)=|a|^{n^2/2}\widehat\Phi^{\,\psi}(aY)\).
Substituting \(Y\mapsto a^{-1}Y\) in the dual integral proves
\[
\epsilon(s,\pi,\psi_a)=
\omega_\pi(a)|a|^{\,n(s-1/2)}\epsilon(s,\pi,\psi).              \tag{1.7l}
\]

If \(\pi\) has a compatible unitary realization, all its smooth
dual vectors are represented by inner products with smooth
vectors. To verify this, a \(J\)-fixed dual vector is represented
on finite-dimensional \(V^J\) by its Hilbert inner product and
extends by the orthogonal average \(e_J\). Consequently
\(\widetilde\pi\) is the complex conjugate of \(\pi\), and
uniqueness of the normalized ideal generator gives
\[
L_{\mathrm{mat}}(s,\widetilde\pi)
=\overline{L_{\mathrm{mat}}(\bar s,\pi)}.
\]
Conjugating Fourier transformation replaces \(\psi\) by
\(\bar\psi=\psi_{-1}\). Thus
\(\epsilon(s,\widetilde\pi,\bar\psi)
=\overline{\epsilon(\bar s,\pi,\psi)}\).
At \(s=1/2\), (1.7l) replaces the left side by
\(\omega_{\widetilde\pi}(-1)\epsilon(1/2,\widetilde\pi,\psi)\).
Together with (1.7k), and \(\omega_\pi(-1)^2=1\), this proves
\[
|\epsilon(1/2,\pi,\psi)|=1,\qquad
\epsilon(s,\pi,\psi)=wq^{\,m(1/2-s)},\quad |w|=1.              \tag{1.7m}
\]
It proves that \(m\) is an integer, not that \(m\geq0\).
Nonnegativity for a character of conductor \(\mathcal O\) still
requires a further argument. For a general \(\psi_a\), the integer
changes by \(n\,v_F(a)\).

#### 7. A precise compact-mod-center case

**Proposition 1.4 (compact-mod-center coefficients).** If, in addition to the hypotheses of Proposition 1.3,
all coefficients of \(\pi\) have compact support modulo the center
and \(V^K=0\), then \(L_{\mathrm{mat}}(s,\pi)=1\).

Fix a coefficient with right \(J\)-fixed vector. Replace its test by
\[
\Phi_*(X)=\int_J\Phi(Xj)\,dj-\int_K\Phi(Xk)\,dk.
\]
The first term has the same integral; the second has zero integral,
because its coefficient average replaces \(v\) by \(e_Kv=0\).
These substitutions are justified in the convergent half-plane
from Proposition 1.3. Both averages have value \(\Phi(0)\) at zero,
so \(\Phi_*\) vanishes on a neighborhood of zero. Its support is
bounded. If \(\operatorname{supp}(c)\subset F^\times C\) for compact
\(C\subset G\), then on the support of \(\Phi_*c\) the absolute
value of that central scalar is bounded above and below. This
follows by taking the positive minimum and finite maximum of the
matrix-entry norm on \(C\). The intersection is therefore contained
in a compact subset of \(G\) with finitely many determinant
valuations. Integrating on those shells gives a Laurent polynomial
in \(X\). All the zeta integrals are Laurent polynomials, and
their ideal contains 1 by the earlier test; hence it is \(\mathscr R\).
\(\square\)

**Corollary 1.4a (the compact-mod-center generator).** Using the unramified matrix theorem proved in
Proposition 1.2, when \(n>1\) the compact-mod-center hypothesis alone
implies \(V^K=0\), and therefore \(L_{\mathrm{mat}}(s,\pi)=1\).

First a real determinant twist makes the central character unitary.
Indeed a smooth character has finite image on \(\mathcal O^\times\);
choose \(t\in\mathbb R\) with
\(q^{-nt}|\omega_\pi(\varpi)|=1\) and replace \(\pi\) by
\(\pi\nu^t\). This preserves its compact fixed spaces and the
compact-mod-center support of every coefficient.

The twisted representation has a compatible unitary realization.
Choose a nonzero smooth dual vector \(\ell\), and put
\[
\langle v,w\rangle=
\int_{F^\times\backslash G}
\ell(\pi(g)v)\overline{\ell(\pi(g)w)}\,d\bar g.
\]
The integrand is independent of the central representative and
has compact support, so this is finite. It is positive definite:
the kernel of the coefficient map for this fixed \(\ell\)
is invariant in \(V\), and cannot be all of \(V\) since
\(\ell\ne0\). Right invariance of quotient Haar measure makes
the form invariant. The coefficient embedding also shows its
action is continuous before completion, since smooth vectors
have open stabilizers. In the Hilbert completion \(H\), compact
averaging has range \(H^J=\overline{V^J}=V^J\); the last equality
uses admissibility. Hence every smooth vector of \(H\) belongs
to \(V\). The completion is irreducible as well: an orthogonal
projection onto a closed invariant subspace commutes with \(G\),
preserves all \(H^J=V^J\), and on the irreducible \(V\) is zero
or the identity. Thus Proposition 1.2 applies if \(V^K\ne0\).

Suppose now that a spherical unit vector \(v_0\) exists and write
\(c_0(g)=\langle\pi(g)v_0,v_0\rangle\). Compact support modulo
the center gives only finitely many dominant Cartan patterns
modulo adding a common integer to every diagonal valuation.
This follows also directly because those successive valuation
differences are bounded on a compact subset of \(G\).
For each pattern choose its representative \(\lambda_n=0\).
The cosets in it that meet \(M_n(\mathcal O)\) are then precisely
\(a_{\lambda+k(1,\ldots,1)}\), \(k\geq0\). Central covariance,
the constant Cartan volume along a central translate, and
the determinant weight give
\[
Z(s,1_{M_n(\mathcal O)},c_0)=
\frac{Q(X)}
{1-\omega_\pi(\varpi)q^{-n(n-1)/2}X^n},
\qquad Q\in\mathbb C[X],\quad Q(0)=1.
\]
The constant term comes from \(K\); every other normalized
pattern has positive valuation sum. Proposition 1.2 says that
the same integral is \(1/P(X)\), where
\(P(X)=\prod_{i=1}^n(1-\alpha_iX)\) and
\(\prod_i\alpha_i=\omega_\pi(\varpi)\).
All the parameters are nonzero, so \(P\) and the displayed
denominator both have degree \(n\). Their equality
\(PQ=1-\omega_\pi(\varpi)q^{-n(n-1)/2}X^n\) forces \(Q=1\).
Comparing their leading coefficients would give
\((-1)^n=-q^{-n(n-1)/2}\), impossible for \(n>1\).
This proves \(V^K=0\). Proposition 1.4 applies to the original
representation, since the determinant twist does not change
its \(K\)-fixed space. \(\square\)

For a general rank greater than two, these propositions do not
prove that abstract supercuspidality implies compact support of
all coefficients modulo the center. That implication, and the
Fourier equation even under the compact-support hypothesis,
are separate obligations. In rank two the earlier
programme supplies the implication and the full equation.

The freely available Goldfeld–Jacquet author notes, §2, Theorem 2.1
and Lemma 2.2, PDF pp. 6–11, provide the normalization and the
traditional reduction route:
[author-hosted text](https://www.math.columbia.edu/~goldfeld/LanglandsBookChapter.pdf).
The argument above proves the stated ideal assertions directly;
the source's statement of the reduction lemma is not used as a
substitute for its proof.

### The full finite-place theory for determinant characters

We now prove the ramified Fourier equation and its nonnegative conductor exponent for an explicit family in every rank. Let \(k\) be nonarchimedean, let \(\psi\) have conductor \(\mathcal O\), and use the positive trace Fourier transform and self-dual additive matrix measure. For a smooth character \(\chi:k^\times\to\mathbb C^\times\), put \(\tau(g)=\chi(\det g)\). Its conductor \(a=a(\chi)\) is zero when \(\chi\) is trivial on \(\mathcal O^\times\); otherwise it is the least positive integer for which \(\chi(1+\varpi^a\mathcal O)=1\). Define the scalar Tate factor by

\[
L_k(z,\chi)=
\begin{cases}
(1-\chi(\varpi)q^{-z})^{-1},&a=0,\\
1,&a>0.
\end{cases}
\tag{1.20a}
\]

The entire scalar theory is proved in *Tate's local theory at the finite places*, Propositions 7.1 and 7.4 and Theorems 7.2–7.3. The matrix argument below includes the necessary boundary and finite-sum steps.

**Proposition 1.16 (determinant characters, all finite places and all ranks).** The matrix generator of Proposition 1.3 is

\[
L_{\mathrm{mat}}(s,\tau)=
\prod_{j=1}^n L_k\left(s+j-\frac{n+1}{2},\chi\right).
\tag{1.20b}
\]

For every matrix Schwartz–Bruhat test, write
\(H(s,\Phi,\chi)=Z(s,\Phi,\chi\circ\det)/L_{\mathrm{mat}}(s,\tau)\).
Then the whole family satisfies

\[
H(1-s,\widehat\Phi,\chi^{-1})
=\epsilon(s,\tau,\psi)H(s,\Phi,\chi).
\tag{1.20c}
\]

The epsilon factor is the product of the scalar Tate epsilon factors at the shifts in (1.20b). For \(a=0\), it is one. For \(a>0\), put

\[
\mathcal G_a(\chi,\psi)=
\sum_{u\in(\mathcal O/\varpi^a)^\times}
\chi(u)^{-1}\psi(\varpi^{-a}u).
\tag{1.20d}
\]

Then

\[
\epsilon(s,\tau,\psi)=
\chi(\varpi)^{an}q^{-ans}\mathcal G_a(\chi,\psi)^n.
\tag{1.20e}
\]

In particular, for unitary \(\chi\),

\[
\epsilon(s,\tau,\psi)=W(\chi,\psi)^n q^{na(1/2-s)},
\qquad
W(\chi,\psi)=\chi(\varpi)^a q^{-a/2}\mathcal G_a(\chi,\psi),
\quad |W(\chi,\psi)|=1.
\tag{1.20f}
\]

Thus the matrix/Tate-product conductor exponent for this family is exactly \(na\ge0\). This establishes Fourier existence and conductor nonnegativity for determinant characters, including their ramified members; it makes neither assertion for every irreducible representation.

**Proof: equivariant distributions and the singular ranks.** Write \(V=M_n(k)\), and let \(G\times G\) act by \(X\mapsto AXB^{-1}\). For \(r=0,\ldots,n\), the rank-\(r\) matrices form one orbit \(\mathcal O_r\), with base point \(E_r=\operatorname{diag}(I_r,0)\). Row and column elimination gives transitivity. Its topology is the homogeneous-space topology: on a chart where the leading \(r\)-minor is invertible, a matrix of rank \(r\) has the form

\[
\begin{pmatrix} A&B\\ C&CA^{-1}B\end{pmatrix},
\qquad A\in GL_r(k),
\tag{1.20g}
\]

Indeed take \(g_1=\left(\begin{smallmatrix}A&0\\C&I\end{smallmatrix}\right)\) and \(g_2^{-1}=\left(\begin{smallmatrix}I&A^{-1}B\\0&I\end{smallmatrix}\right)\); then \(g_1E_rg_2^{-1}\) is the displayed matrix, giving a continuous local section of the orbit map. Permuting rows and columns supplies all charts.

A distribution here is a linear functional on locally constant compactly supported tests. The space is the union of finite-dimensional spaces with bounded support and fixed additive constancy level; linear functionals and the compact averaging used below are continuous on each such space. For \(t\in\mathbb C\), consider the covariance

\[
D\bigl(\Phi(A^{-1}\,\cdot\, B)\bigr)
=\chi(\det A/\det B)|\det A/\det B|^{t+n}D(\Phi).
\tag{1.20h}
\]

If \(\chi\) is ramified, no nonzero distribution supported on the singular matrices has this covariance, for any \(t\). We prove the claim on each orbit first. Choose a unit \(u\) with \(\chi(u)\ne1\). For \(r<n\), the pair

\[
h=(\operatorname{diag}(I_r,u,1,\ldots,1),I_n)
\]

fixes \(E_r\). It lies in \(K\times K\) and normalizes every pair of principal congruence subgroups \(J_b\times J_b\), where \(J_b=I_n+\varpi^bM_n(\mathcal O)\). Choose \(b\) large enough that \(\chi\) is trivial on \(\det J_b\). The compact orbit \(U=(J_b\times J_b)E_r\) is open in \(\mathcal O_r\) by the chart (1.20g); for \(r=0\) it is the one-point orbit. On this compact transitive orbit, averaging any test over \(J_b\times J_b\) gives its mean times \(1_U\). This is a finite averaging operation on each test. Covariance is trivial on these congruence subgroups, so an equivariant distribution on \(U\) is determined by \(D(1_U)\). But \(h\) preserves \(U\), whereas (1.20h) multiplies that value by \(\chi(u)\). Thus \(D(1_U)=0\), and the distribution vanishes on \(U\). Covariance and transitivity give vanishing on every translate of \(U\); a finite compact-open partition of a test's support then proves vanishing on all of \(\mathcal O_r\).

To pass from the orbits to the boundary, let \(F_r\) be the closed set of matrices of rank at most \(r\). A distribution supported on \(F_r\) factors through tests on \(F_r\): an ambient locally constant test zero on \(F_r\) has compact support disjoint from it, so the distribution kills it. Every test on \(F_r\) extends to an ambient test by covering its compact support with finitely many compact-open balls on which its restriction is constant and taking a disjoint refinement. The rank-\(r\) stratum is open in \(F_r\). Its compactly supported tests extend by zero to \(F_r\). Their annihilation puts the remaining distribution on \(F_{r-1}\). Descending through the ranks proves the claim.

On the open orbit \(G\), the space with covariance (1.20h) has dimension one. Indeed put \(w_t(g)=\chi(\det g)|\det g|^{t+n}\). Multiplying tests by \(w_t^{-1}\) turns any such distribution into a left-invariant distribution on \(G\). A left-invariant distribution is a scalar multiple of Haar integration: on a compact open subgroup its compact average is the constant mean, and its value on any translate of a smaller compact open subgroup is determined by the finite index. Refining two subgroups to their intersection makes the scalar independent of the subgroup. Every test is a finite sum of compact-open coset indicators. This proves the assertion without an orbit-distribution uniqueness theorem as an additional input. Since a difference with zero open-orbit restriction is supported on the boundary, the same one-dimensional bound holds on all of \(V\) when \(\chi\) is ramified.

**Proof: entireness and the Fourier equation.** Up to the positive Haar constant, the matrix integral is the distribution

\[
T_{\chi,t}(\Phi)=\int_V\Phi(X)\chi(\det X)|\det X|^t\,dX,
\qquad t=s-\frac{n+1}{2},
\tag{1.20i}
\]

initially in its convergence half-plane. The singular set has additive measure zero: a point in \(k\) has measure zero since its balls have masses tending to zero; an invertible linear coordinate change then gives measure zero to any proper linear subspace. Successive columns of a matrix almost surely avoid the span of their predecessors, by Fubini on compact matrix boxes. Proposition 1.3 gives rational continuation with one denominator for all tests. If it had a pole, take a highest nonzero Laurent coefficient at that pole; the common denominator bounds its possible order uniformly over tests. Compactly supported tests inside \(G\) have entire integrals, so this coefficient is supported on the singular set. Change of variables gives precisely (1.20h); its highest Laurent coefficient has that covariance at the pole parameter. Boundary vanishing rules it out. Thus every integral is entire when \(\chi\) is ramified. A nonconstant canonical polynomial \(P\), with \(P(0)=1\), would have a nonzero complex root and would give a pole of its attained generator at some \(s\). That is impossible. Hence \(L_{\mathrm{mat}}=1\), proving (1.20b) in the ramified case.

Fourier transformation takes the distribution for \(\chi^{-1}\) and parameter \(t'=-t-n\) to another distribution with covariance (1.20h). In detail, with \(R=|\det A/\det B|\),

\[
\widehat{\Phi(A^{-1}\,\cdot\,B)}(Y)
=R^n\widehat\Phi(B^{-1}YA).
\tag{1.20j}
\]

Applying the dual covariance contributes \(\chi(\det A/\det B)R^{-t'-n}\); the displayed extra \(R^n\) leaves \(\chi(\det A/\det B)R^{t+n}\). The one-dimensional result therefore proves the existence of one Fourier scalar for every test. A normalized principal-congruence indicator has original zeta integral identically one, so this scalar is a single rational function of \(q^{-s}\), independent of the test. Fourier inversion ensures that it is nonzero. Here the entire assertion and Fourier uniqueness were proved for the whole family, not inferred from one example.

**Proof: the scalar and its conductor.** Assume \(a>0\), put \(J_a=I_n+\varpi^aM_n(\mathcal O)\), and take

\[
\Phi=\operatorname{vol}_{dg}(J_a)^{-1}1_{J_a}.
\]

Then \(Z(s,\Phi,\chi\circ\det)=1\). Write \(dg=C|\det X|^{-n}dX\); on \(J_a\) the determinant norm is one, so \(\operatorname{vol}_{dg}(J_a)=Cq^{-an^2}\). The scalar coset-indicator transform proved in *Additive characters, self-dual measures and Poisson summation on the adèles*, Proposition 5.2, applied to the trace coordinates, gives

\[
\widehat\Phi(Y)=C^{-1}\psi(\operatorname{tr}Y)
1_{\varpi^{-a}M_n(\mathcal O)}(Y).
\tag{1.20k}
\]

In the initial half-plane for the dual integral, substitute \(Y=\varpi^{-a}A\). The Fourier scalar is

\[
\chi(\varpi)^{an}q^{an((n+1)/2-s)}
\int_{M_n(\mathcal O)\cap G}
\psi(\varpi^{-a}\operatorname{tr}A)\chi(\det A)^{-1}
|\det A|^{-s-(n-1)/2}\,dA.
\tag{1.20l}
\]

Only \(A\in K\) contributes. Here is a cancellation proof for all the other residue cells modulo \(\varpi^a\). For a singular residue cell, choose an integral lift \(A_0\) with Smith form. At least one diagonal Smith entry is divisible by \(\varpi\), or is zero. If \(a\ge2\), choose \(u\in1+\varpi^{a-1}\mathcal O\) with \(\chi(u)\ne1\); minimality of \(a\) supplies it. If \(a=1\), choose any unit with \(\chi(u)\ne1\). Scaling that Smith row by \(u\), and conjugating the row operation back, gives \(E\in K\) with

\[
(E-I)A_0\in\varpi^aM_n(\mathcal O),\qquad \det E=u.
\]

For every \(A\) in the same cell, \(EA\) is still in that cell and has the same trace modulo \(\varpi^a\). Its determinant norm and additive measure are unchanged. Its multiplicative character is multiplied by \(\chi(u)^{-1}\). Thus the cell integral in (1.20l) is zero. These changes of variables are valid in the convergent dual half-plane, and subsequently by continuation.

On the invertible residue cells all determinant norms are one, so the remaining integral is

\[
q^{-an^2}S_n,\qquad
S_n=\sum_{A\in GL_n(\mathcal O/\varpi^a)}
\chi(\det A)^{-1}\psi(\varpi^{-a}\operatorname{tr}A).
\tag{1.20m}
\]

Let \(R_a=\mathcal O/\varpi^a\), \(|R_a|=q^a\), and let \(U_n(R_a)\) be its upper unitriangular group. Right multiplication by \(u\in U_n(R_a)\) permutes \(GL_n(R_a)\) and leaves its determinant unchanged. Average the sum over these right multiplications. Since

\[
\operatorname{tr}(Au)=\operatorname{tr}A+
\sum_{i<j}A_{ji}u_{ij},
\]

orthogonality kills every matrix with a nonzero entry below the diagonal. Indeed the annihilator of \(\mathcal O\) is \(\mathcal O\), so for any nonzero residue \(c\) the character \(v\mapsto\psi(\varpi^{-a}cv)\) of \(R_a\) is nontrivial and its sum is zero. The independent upper entries of the surviving triangular matrix are arbitrary, and its diagonal entries are units. It follows that

\[
S_n=q^{a n(n-1)/2}\mathcal G_a(\chi,\psi)^n.
\tag{1.20n}
\]

Combining (1.20l)–(1.20n) gives
\(\chi(\varpi)^{an}q^{-ans}\mathcal G_a^n\), which is (1.20e).
The scalar Tate formula in the earlier Theorem 7.3 is
\(\epsilon_k(z,\chi,\psi)=\chi(\varpi)^a q^{-az}\mathcal G_a\).
The shifts \(j-(n+1)/2\) sum to zero, so its product is exactly (1.20e).

For completeness, the size of the primitive scalar sum follows directly from the same positive Fourier inversion. For \(f(x)=\chi(x)^{-1}1_{\mathcal O^\times}(x)\), additive invariance under \(\varpi^a\mathcal O\) puts its transform in \(\varpi^{-a}\mathcal O\). On every shallower shell, multiplying the unit variable by the same \(u\) used in the singular-cell argument leaves its additive phase unchanged and multiplies its character by a nontrivial scalar, so the transform is zero. On the remaining shell
\(\widehat f(\varpi^{-a}w)=q^{-a}\chi(w)\mathcal G_a(\chi,\psi)\).
Applying Fourier transformation again and evaluating at one gives
\(\mathcal G_a(\chi,\psi)\mathcal G_a(\chi^{-1},\psi)=\chi(-1)q^a\).
Conjugation of the first sum, followed by \(u\mapsto-u\), gives
\(\overline{\mathcal G_a(\chi,\psi)}=\chi(-1)\mathcal G_a(\chi^{-1},\psi)\).
The restriction of \(\chi\) to the finite unit quotient has modulus one, so these identities prove \(|\mathcal G_a|=q^{a/2}\). This also proves nonvanishing. Formula (1.20f) and the nonnegative exponent \(na\) follow.

**Proof: the unramified characters.** First suppose \(\chi\) is unramified and unitary. In the normalized principal series with inducing characters
\(\chi|\cdot|^{j-(n+1)/2}\), its spherical function is \(\chi(\det g)\), because these exponents cancel the upper-Borel half-modulus in Iwasawa coordinates. This function spans the determinant-character subrepresentation and its fixed line. The spherical Hecke character therefore has eigenvalues
\(\chi(\varpi)q^{(n+1)/2-j}\). Proposition 1.2 gives exactly (1.20b) and the whole Fourier equation with epsilon factor one. Every smooth \(\chi\) is a unitary character times a real determinant norm power; replacing \(\chi\) by \(\chi|\cdot|^b\) replaces \(s\) by \(s+b\), while the dual parameter becomes \(1-s-b\). This supplies the nonunitary unramified case as well, and proves the same norm-twist compatibility in the ramified formula. All scalar multiples of the coefficient are included, since the representation is one dimensional. \(\square\)

For \(n>1\), determinant characters are not the general cuspidal local factors: the upper unipotent subgroup acts trivially, so a nontrivial generic character admits no Whittaker functional on this representation. The proposition supplies a complete family of ramified matrix Fourier and conductor calculations; the general irreducible local assertion in 1.1c remains separate.


### The scalar matrix Fourier equation in every finite-place rank

Let \(k\) be any nonarchimedean local field, with integers \(\mathcal O\),
uniformizer \(\varpi\) and residue cardinality \(q\). Put
\(G=\mathrm{GL}_n(k)\), \(\nu(g)=|\det g|\), and \(u_s=s+(n-1)/2\).
Let \((\pi,V)\) be irreducible, smooth and admissible. Its smooth dual
is \(\widetilde V\). We use the positive trace convention
\[
\widehat\Phi(Y)=\int_{M_n(k)}\Phi(X)\psi(\operatorname{tr}(XY))\,dX,
\qquad \check c(g)=c(g^{-1}),
\tag{1.21a}
\]
with a nontrivial unitary additive character and self-dual measure.

**Theorem 1.17.** There is a nonzero rational function
\(\gamma_{\mathrm{mat}}(s,\pi,\psi)\) of \(q^{-s}\), independent of
the Schwartz–Bruhat test and the smooth matrix coefficient, such that
\[
Z(1-s,\widehat\Phi,\check c)
=\gamma_{\mathrm{mat}}(s,\pi,\psi)Z(s,\Phi,c).             \tag{1.21b}
\]
The identity holds for the rational continuations of the entire
test/coefficient family in every rank, including all ramified
representations. Admissibility is a hypothesis. The theorem does
not identify the matrix factor with a parameter or a rank-one
Rankin–Selberg factor. Theorem 1.24 and Corollary 1.24c below supply nonnegativity of its matrix conductor exponent.

The already proved Proposition 1.3 supplies rational continuation,
one denominator uniform over the entire family, smooth dual
admissibility and biduality, and a test/coefficient pair whose
integral is identically 1. Its Fourier inversion proof also supplies
\(\widehat{\widehat\Phi}(X)=\Phi(-X)\) and preservation of the whole
matrix Schwartz space. We use those proved assertions here,
without treating the principal ideal as a Fourier equation.

#### 1. A compact-fixed Jacquet lemma

Fix \(0<r<n\), put \(m=n-r\), and let
\[
U=\left\{\begin{pmatrix}I_r&B\\0&I_m\end{pmatrix}\right\},
\quad
U^-=\left\{\begin{pmatrix}I_r&0\\C&I_m\end{pmatrix}\right\},
\quad M=\mathrm{GL}_r(k)\times\mathrm{GL}_m(k).
\]
For any smooth representation \(W\), let
\(W_U=W/\langle \pi(u)w-w:u\in U,w\in W\rangle\), with its
unnormalized \(M\)-action. Write \(p:W\to W_U\) for the quotient.
Set
\[
J_d=1+\varpi^dM_n(\mathcal O),\quad
J_{M,d}=J_d\cap M,\quad J_{U,d}=J_d\cap U,\quad
J_{U^-,d}=J_d\cap U^-,\qquad d\geq1.
\]

**Lemma 1.17a.** If \(W\) is smooth and admissible, then
\[
p(W^{J_d})=(W_U)^{J_{M,d}},
\tag{1.21c}
\]
and \(W_U\) is a smooth admissible representation of \(M\).

**Proof.** Block elimination gives the unique decomposition
\[
J_d=J_{U,d}J_{M,d}J_{U^-,d}.
\tag{1.21d}
\]
Indeed for a block matrix \(\left(\begin{smallmatrix}A&B\\C&D\end{smallmatrix}\right)\)
in \(J_d\), its last block \(D\) is invertible, and the three
factors have upper entry \(BD^{-1}\), diagonal blocks
\(A-BD^{-1}C,D\), and lower entry \(D^{-1}C\).
They have the asserted congruences. The same formulas over
\(\mathcal O/\varpi^N\), \(N>d\), give a bijection of the three
finite coordinate sets with \(J_d/J_N\). Counting their uniform
probabilities, then passing through these finite quotients,
proves the probability-average identity
\[
e_{J_d}=e_{J_{U,d}}e_{J_{M,d}}e_{J_{U^-,d}}.                  \tag{1.21e}
\]
All averages on smooth vectors are finite sums.

Put \(a=\operatorname{diag}(\varpi I_r,I_m)\). It commutes with
\(M\), contracts \(U\), and expands \(U^-\). Let
\(E=p(W^{J_d})\). This is finite-dimensional and lies in
\((W_U)^{J_{M,d}}\). If \(w\in W^{J_d}\), then \(\pi(a)w\)
is still fixed by \(J_{M,d}\) and \(J_{U^-,d}\), since
\(a^{-1}J_{U^-,d}a\subset J_{U^-,d}\).
Equation (1.21e), and the trivial action of \(U\) on \(W_U\), give
\[
p(e_{J_d}\pi(a)w)=p(\pi(a)w)=a\,p(w).
\]
Thus \(aE\subset E\). The action of \(a\) on \(W_U\) is
invertible. Its restriction to finite-dimensional \(E\) is
therefore bijective, so \(aE=E\).

Now take \(y\in(W_U)^{J_{M,d}}\). Lift it to \(w\in W\) and
average over \(J_{M,d}\), obtaining a \(J_{M,d}\)-fixed lift.
Smoothness gives an \(N\) for which it is fixed by the lower
block subgroup with entries in \(\varpi^NM_{m,r}(\mathcal O)\).
For \(j\) sufficiently large, \(\pi(a^j)w\) is fixed by
\(J_{U^-,d}\), because conjugation by \(a^j\) multiplies its
lower entries by \(\varpi^{-j}\). It remains \(J_{M,d}\)-fixed.
Again (1.21e) yields
\[
a^j y=p(e_{J_d}\pi(a^j)w)\in E.
\]
Since \(a^{-j}E=E\), \(y\in E\). This proves (1.21c).
The quotient is smooth under \(M\). Every compact open
subgroup of \(M\) contains some \(J_{M,d}\), so its fixed
space is contained in the finite-dimensional space in (1.21c).
This proves admissibility. \(\square\)

The cases \(r=0\), \(U=\{1\}\), \(M=G\), and \(r=n\) need
no Jacquet argument. No cuspidal-support or classification
theorem has been used in Lemma 1.17a.

#### 2. The orbit functional and its modular factor

Put \(H=G\times G\), acting on matrix points by
\((a,b)\cdot X=aXb^{-1}\). Its test-function action is
\[
\rho(a,b)\Phi(X)=\Phi(a^{-1}Xb).
\]
On \(E=\widetilde V\otimes V\), let
\[
\sigma(a,b)(\ell\otimes v)=\widetilde\pi(a)\ell\otimes\pi(b)v,
\qquad
\chi_s(a,b)=\nu(a)^{u_s}\nu(b)^{-u_s}.
\tag{1.21f}
\]
We will prove that, outside a countable set of \(s\),
\[
\dim\operatorname{Hom}_H(\mathcal S(M_n(k))\otimes E,\chi_s)
\leq1.                                                       \tag{1.21g}
\]
The Hom space here consists of linear functionals with
\(T(\rho(h)f\otimes\sigma(h)e)=\chi_s(h)T(f\otimes e)\);
no unproved continuity or irreducible-distribution theorem
is implicit in that notation.

For \(0\leq r\leq n\), write \(x_r=\operatorname{diag}(I_r,0)\)
and let \(\mathcal O_r\) be its rank-\(r\) orbit. Its stabilizer is
\[
S_r=
\left\{
\left(
\begin{pmatrix}A&B\\0&D\end{pmatrix},
\begin{pmatrix}A&0\\C&D'\end{pmatrix}
\right):
A\in\mathrm{GL}_r,\ D,D'\in\mathrm{GL}_m
\right\},\qquad m=n-r.                                      \tag{1.21h}
\]
This follows by equating \(a x_r=x_r b\).
The unipotent radical is the product of the two additive
off-diagonal block spaces. Its conjugation modulus under
the displayed Levi is
\[
\delta_r(a,b)=|\det A|^m|\det D|^{-r}
|\det D'|^r|\det A|^{-m}
=|\det D'|^r|\det D|^{-r}.                     \tag{1.21i}
\]
The two determinant powers involving \(A\) cancel. In
coordinates \(u l\) on \(S_r\), its left Haar measure is
\(\delta_r(l)^{-1}du\,dl\), since each general linear Levi
factor is unimodular. Thus its right-translation convention is
\[
\int_{S_r}f(xp)\,dx=\delta_r(p)\int_{S_r}f(x)\,dx.
\tag{1.21j}
\]
For \(r=0\) or \(n\), the same formulas read \(\delta_r=1\).

**Lemma 1.17b (orbit functional).** There is a natural identification
\[
\operatorname{Hom}_H(\mathcal S(\mathcal O_r)\otimes E,\chi_s)
\simeq
\{\lambda\in E^*:
\lambda(\sigma(p)e)=\chi_s(p)\delta_r(p)\lambda(e)
\text{ for }p\in S_r\}.
\tag{1.21k}
\]

**Proof.** The quotient \(H/S_r\) identifies with \(\mathcal O_r\)
and has local continuous sections. To check this explicitly near
\(x_r\), a rank-\(r\) matrix with invertible upper-left block has
the form
\[
Y=\begin{pmatrix}A&B\\ C&CA^{-1}B\end{pmatrix}
=L(Y)x_rR(Y),\quad
L(Y)=\begin{pmatrix}A&0\\ C&I_m\end{pmatrix},\quad
R(Y)=\begin{pmatrix}I_r&A^{-1}B\\0&I_m\end{pmatrix}.
\]
The section is \((L(Y),R(Y)^{-1})\). Permuting rows and columns
gives sections on the other nonzero-minor charts. Their formulas
and inverses are continuous. Above a chart, \(h=s(Y)p\)
therefore gives a product homeomorphism with \(S_r\).

Define the surjective \(H\)-map
\[
Q:\mathcal S(H)\longrightarrow\mathcal S(H/S_r),\qquad
Qf(hS_r)=\int_{S_r}f(hp)\,dp.
\]
It is well-defined by left invariance of \(dp\).
Surjectivity follows using a local section, a compactly
supported locally constant function of \(p\) with integral 1,
and a finite partition of the compact support into charts.
Its kernel is spanned by
\[
R(p)f-\delta_r(p)f,\qquad R(p)f(h)=f(hp).                    \tag{1.21l}
\]
Here are the details of this kernel assertion. On any chart,
a compactly supported locally constant function is a finite
sum of products in the quotient and subgroup coordinates:
cover its compact support by constant compact-open rectangles
and refine that finite cover into a disjoint partition.
Refining also in the quotient coordinate makes each vertical
function have integral zero if \(Qf=0\).
For a locally constant compactly supported function on \(S_r\),
choose a compact open subgroup under which it is left
invariant. Express it as a finite sum of indicators of left
cosets \(Kp\). In the quotient by (1.21l),
\([1_{Kp}]=\delta_r(p)^{-1}[1_K]\), exactly their Haar-mass
ratio by (1.21j). Refining \(K\) replaces \(1_K\) by its
index times \(1_{K'}\), and \(\delta_r\) is 1 on compact
subgroups. Consequently the only surviving coordinate is
the Haar integral. Its kernel is precisely the span (1.21l).
Multiplying by the quotient-coordinate functions proves
the assertion on each chart, then on the whole space.

An \(H\)-equivariant functional on \(\mathcal S(H)\otimes E\)
is uniquely of the form
\[
B_\lambda(f,e)=
\int_H f(h)\chi_s(h)\lambda(\sigma(h^{-1})e)\,dh,
\qquad \lambda\in E^*.                                     \tag{1.21m}
\]
This formula needs no growth hypothesis, since \(f\) has compact
support and the vector orbit is locally constant. To prove
uniqueness rather than assume it, for a compact open \(J\)
fixing \(e\) and annihilating \(\chi_s\), set
\(\lambda(e)=B(1_J,e)/\operatorname{vol}(J)\).
Refining \(J\) and decomposing it into left cosets proves
independence of this choice by equivariance. A common such
subgroup for finitely many vectors proves linearity.
On a compact support the set of vectors
\(\sigma(h^{-1})e\) is finite. Refine a right-coset partition
of \(f\) to a subgroup fixing all these vectors and lying
in the kernel of \(\chi_s\); equivariance on each coset
then gives exactly (1.21m). Conversely (1.21m) has the required
covariance by substituting \(h\mapsto ah\).

Finally \(H\) is unimodular, so
\[
B_\lambda(R(p)f,e)
=\chi_s(p)^{-1}B_{\lambda\circ\sigma(p)}(f,e).
\]
It descends through \(Q\otimes1_E\) exactly when (1.21l)
vanishes, namely when
\(\lambda\circ\sigma(p)=\chi_s(p)\delta_r(p)\lambda\).
This proves (1.21k), including its modular sign. \(\square\)

#### 3. Singular ranks give only a countable obstruction

For \(r<n\), let \(U_r\) be the upper block subgroup in the first
component of (1.21h), and put \(W_r=(\widetilde V)_{U_r}\).
For \(r=0\), put \(W_0=\widetilde V\) directly. Lemma 1.17a and
the proved smooth dual admissibility show that \(W_r\) is
admissible for \(M_r=\mathrm{GL}_r\times\mathrm{GL}_{n-r}\).

Suppose a nonzero \(\lambda\) in (1.21k) exists. Its character
is trivial on \(U_r\), so it descends in its first tensor
factor to \(W_r\). Choose a vector in its second tensor
factor for which the resulting functional \(\lambda_0\)
on \(W_r\) is nonzero. For
\[
p_t=(\operatorname{diag}(I_r,tI_m),I_n)\in S_r,
\qquad m=n-r,
\]
equations (1.21f), (1.21i) and (1.21k) give
\[
\lambda_0(t\,w)=|t|^{m(u_s-r)}\lambda_0(w).                  \tag{1.21n}
\]
Here \(t\) acts by the central element
\(\operatorname{diag}(I_r,tI_m)\) of \(M_r\).

Pick \(w\) with \(\lambda_0(w)\ne0\), fixed by some principal
compact subgroup \(J_{M_r,d}\). Its fixed space is finite
dimensional, and the central element
\(\operatorname{diag}(I_r,\varpi I_m)\) acts on it by an
invertible operator \(A_{r,d}\). Restricting (1.21n) to this
space shows
\[
q^{-m(s+(n-1)/2-r)}\in\operatorname{Spec}(A_{r,d}).           \tag{1.21o}
\]
For a fixed \(r,d\), there are finitely many nonzero eigenvalues.
The preimage of any one under the displayed exponential is
countable and discrete. Taking the union over
\(0\leq r<n\) and integers \(d\geq1\) gives a countable set
\(\mathscr E\subset\mathbb C\). Hence every singular-rank
Hom space in (1.21k) is zero when \(s\notin\mathscr E\).
We need no finite-length theorem and do not assert that this
countable set is finite.

On the full-rank orbit, \(S_n\) is diagonal \(G\),
\(\delta_n=1\), and \(\chi_s|_{S_n}=1\).
Its functionals are invariant pairings on
\(\widetilde V\otimes V\). Such a pairing gives an intertwiner
\(V\to(\widetilde V)^{\vee}=V\): its value at a vector fixed
by \(J\) is a \(J\)-fixed functional on \(\widetilde V\),
so lies in the proved smooth bidual. The intertwiner is scalar.
Indeed it preserves a nonzero finite-dimensional \(V^J\),
where it has an eigenvector; its eigenspace in \(V\) is
invariant and therefore all of \(V\). The evaluation pairing
is nonzero. Thus the full-rank Hom space has dimension one.

To pass from the strata to the whole matrix space, put
\(X_{\geq r}=\{X:\operatorname{rank}X\geq r\}\). These are
open and have the finite exact filtration
\[
0\longrightarrow\mathcal S(X_{\geq r+1})
\longrightarrow\mathcal S(X_{\geq r})
\longrightarrow\mathcal S(\mathcal O_r)\longrightarrow0.
\tag{1.21p}
\]
Restriction is onto: a compactly supported locally constant
function on the closed subset \(\mathcal O_r\) of \(X_{\geq r}\)
extends by a finite compact-open cover in the ambient space,
refined into a disjoint partition. Its nonzero level sets
are compact, so finitely many such neighborhoods suffice;
choose each neighborhood to meet the closed subset only
where that level is constant. The kernel is precisely the
functions compactly supported in the open complement,
extended by zero. Tensoring with \(E\) preserves this exact
sequence over \(\mathbb C\).

An equivariant functional which is zero on the full-rank
subspace consequently factors successively through the
singular-rank quotients in (1.21p). For \(s\notin\mathscr E\)
each such quotient has zero Hom space, so the functional
is zero. Restriction to the full-rank orbit is injective,
and its one-dimensional Hom space proves (1.21g).

#### 4. Both zeta families have the same covariance

For \(e=\ell\otimes v\), let \(c_e(g)=\ell(\pi(g)v)\).
In the common initial convergent half-plane, the substitution
\(g=ax b^{-1}\) gives
\[
Z(s,\rho(a,b)\Phi,c_{\sigma(a,b)e})
=\chi_s(a,b)Z(s,\Phi,c_e).                              \tag{1.21q}
\]
Both sides are rational by Proposition 1.3, so the equality
continues. That proposition gives a common denominator for
all tests and coefficients. Away from its poles we obtain
a genuine element \(T_s\) of the Hom space in (1.21g).
It is nonzero: the compact subgroup test of Proposition 1.3
has \(T_s(\Phi_0,e_0)=1\) for every \(s\).

Consider the second rational family
\[
D_s(\Phi,e)=Z(1-s,\widehat\Phi,\check c_e).
\]
It is rational by the same proved proposition for
\(\widetilde\pi\), with variable \(q^{-(1-s)}=q^{-1}q^s\).
Fourier change of variables in the additive matrix space gives
\[
\widehat{\rho(a,b)\Phi}(Y)
=\nu(a)^n\nu(b)^{-n}\widehat\Phi(b^{-1}Ya).                  \tag{1.21r}
\]
Indeed \(X=aZb^{-1}\) has additive Jacobian
\(\nu(a)^n\nu(b)^{-n}\), and
\(\operatorname{tr}(aZb^{-1}Y)=\operatorname{tr}(Zb^{-1}Ya)\).
This is the positive trace Fourier convention, with no
extra inverse additive character.

Also
\[
\check c_{\sigma(a,b)e}(g)=\check c_e(b^{-1}ga).
\]
Apply (1.21q) to the dual representation with the two
group components exchanged and the parameter \(1-s\).
Together with (1.21r), this gives
\[
\begin{split}
D_s(\rho(a,b)\Phi,\sigma(a,b)e)
&=\nu(a/b)^n\,\nu(b/a)^{1-s+(n-1)/2}D_s(\Phi,e)\\
&=\nu(a/b)^{s+(n-1)/2}D_s(\Phi,e)
=\chi_s(a,b)D_s(\Phi,e).
\end{split}                                                \tag{1.21s}
\]
The first application may be made in the dual convergent
half-plane; rationality then gives the displayed identity
everywhere. Thus outside the poles of its own uniform
denominator \(D_s\) belongs to the same Hom space.

#### 5. Generic uniqueness gives the entire rational equation

Remove \(\mathscr E\) and the poles of the two uniform
denominators. Their union is countable. At every remaining
parameter, (1.21g), (1.21q), and (1.21s) give
\[
D_s=\gamma(s)T_s,\qquad
\gamma(s)=D_s(\Phi_0,e_0),
\tag{1.21t}
\]
because \(T_s(\Phi_0,e_0)=1\). The last expression is a
single rational function of \(q^{-s}\), independent of the
test/coefficient family. For every fixed \(\Phi,e\), the
difference \(D_s(\Phi,e)-\gamma(s)T_s(\Phi,e)\) is rational
in \(q^{-s}\) and vanishes outside that countable set.
The complement of a countable subset of \(\mathbb C\)
is dense in every open disk. On any disk avoiding the
finitely many local poles of this particular rational
difference it therefore vanishes identically, and rational
continuation proves its vanishing everywhere.

Finally \(\gamma\) is not the zero rational function.
Fourier transformation is a bijection on the matrix
Schwartz space, and smooth biduality makes coefficient
inversion a bijection with the dual coefficient family.
The latter has a test/coefficient pair whose integral is
identically 1. Its inverse image under these bijections
gives \(D_s(\Phi,e)=1\) for every \(s\). If \(\gamma\)
were zero, (1.21t) at the generic parameters would contradict
this pair. Equations (1.21t) are precisely (1.21b).
\(\square\)

The rational scalar equation is now proved. The consequences in Proposition 1.3, §6,
therefore apply: the matrix epsilon factor is a Laurent unit,
the same-character double equation has the central sign
\(\omega_\pi(-1)\), and a compatible unitary realization
has unit central epsilon phase. Nothing in the rank-stratum
argument imposes nonnegativity of that Laurent-unit exponent; Theorem 1.24 and Corollary 1.24c provide the separate positivity proof.

The freely available
[Goldfeld–Jacquet author notes](https://www.math.columbia.edu/~goldfeld/LanglandsBookChapter.pdf),
§2, Theorem 2.1, PDF pp.6–9, give the precise local analytic
package and its normalization. The scalar-existence proof
above uses the preceding proved rational family and the
explicit compact-average and orbit arguments; a quoted
local functional-equation theorem, a general classification
or Whittaker uniqueness is not a premise.

### Conductor exponents from compact induction

Let \(k\) be any nonarchimedean local field, \(\mathcal O\) its integers,
\(\varpi\) a uniformizer, \(q\) the residue cardinality, and
\(G=\mathrm{GL}_n(k)\), \(n\geq2\). Write
\[
Z=k^\times I_n,\quad K=\mathrm{GL}_n(\mathcal O),\quad
J_r=1+\varpi^rM_n(\mathcal O),\quad
j(g)=v_k(\det g),\quad X=q^{-s}.
\tag{1.24a}
\]
Multiplicative Haar measure gives \(K\) volume 1. The additive character
\(\psi\) has annihilator \(\mathcal O\), and additive matrix measure is
self-dual for
\[
\widehat\Phi(Y)=\int\Phi(A)\psi(\operatorname{tr}(AY))\,dA .
\tag{1.24b}
\]
Thus \(M_n(\mathcal O)\) has additive volume 1. Put
\[
Z_\pi(s,\Phi,c)=\int_G\Phi(g)c(g)
|\det g|^{s+(n-1)/2}\,dg,\qquad
c^\vee(g)=c(g^{-1}).
\tag{1.24c}
\]

We use the following preceding results of this lesson:
Proposition 1.3 and its §§1–3 prove smooth dual irreducibility and
biduality, the normalized rational ideal, the principal-congruence diagonal
semigroup, and the elementary Cartan decomposition; Proposition 1.4 and
Corollary 1.4a prove that compact-mod-center coefficients imply
\(L_{\mathrm{mat}}=1\) in rank \(n>1\); Theorem 1.17 proves the whole-family
scalar Fourier equation and Lemma 1.17a proves the two-block probability
factorization. The consequences in Proposition 1.3 §6 give
\[
\gamma_\pi(s,\psi)=\epsilon_\pi(s,\psi)
\frac{L_{\widetilde\pi}(1-s)}{L_\pi(s)},\qquad
\epsilon_\pi(s,\psi)=c_\pi X^{a_\pi},\quad
c_\pi\ne0,\quad a_\pi\in\mathbb Z .
\tag{1.24d}
\]
Positivity is not assumed in (1.24d).

#### Zero Jacquet modules imply compact-mod-center coefficients

For \(1\leq i<n\), let \(U_i\) be the upper two-block unipotent subgroup
of block sizes \(i,n-i\). Its entries form the additive space
\(M_{i,n-i}(k)\). The unnormalized Jacquet quotient is
\[
V_{U_i}=V/\langle\pi(u)v-v:u\in U_i,\ v\in V\rangle .
\]

**Lemma 1.20a.** Let \(\pi\) be smooth admissible, and suppose
\(V_{U_i}=0\) for all \(i<n\). Every smooth matrix coefficient of
\(\pi\) has compact support modulo \(Z\). If \(\pi\) is also
irreducible and \(n>1\), then \(L_\pi=L_{\widetilde\pi}=1\).

**Proof.** Fix \(r\geq1\), and put \(E=V^{J_r}\). For
\[
a_i=\operatorname{diag}(\varpi I_i,I_{n-i}),\qquad
T_i=e_{J_r}\pi(a_i)e_{J_r}|_E,
\]
the proved diagonal semigroup identity gives
\[
T_i^b=e_{J_r}\pi(a_i^b)e_{J_r}|_E,\qquad b\geq0.
\tag{1.24e}
\]
We show that \(T_i\) is nilpotent. Any \(v\in V\), because its
Jacquet class is zero, is a finite sum of differences
\(\pi(u_\alpha)w_\alpha-w_\alpha\). Choose a compact additive
subgroup \(U_i(\varpi^{-t}\mathcal O)\) containing every
\(u_\alpha\). Its probability average kills every difference,
by translation invariance of its finite smooth average. Hence
it kills \(v\). A basis of the finite-dimensional space \(E\)
gives a single \(t\) for which this average kills all of \(E\).
Every larger compact subgroup of \(U_i\) also has zero average
on \(E\), since averaging again over a larger group preserves
the zero obtained by averaging the smaller subgroup.

The two-block factorization, including its probability-average
identity, is
\[
J_r=(J_r\cap U_i)(J_r\cap M_i)(J_r\cap U_i^-),\qquad
e_{J_r}=e_{J_r\cap U_i}e_{J_r\cap M_i}e_{J_r\cap U_i^-}.
\tag{1.24f}
\]
Conjugation by \(a_i^{-b}\) expands the upper entries to
\(\varpi^{r-b}\mathcal O\), contracts the lower entries to
\(\varpi^{r+b}\mathcal O\), and fixes the block diagonal group.
For \(v\in E\), the lower and diagonal averages therefore fix \(v\),
so
\[
e_{J_r}\pi(a_i^b)v
=\pi(a_i^b)e_{a_i^{-b}J_ra_i^b}v
=\pi(a_i^b)e_{U_i(\varpi^{r-b}\mathcal O)}v=0
\quad(b\geq r+t).
\tag{1.24g}
\]
This proves \(T_i^{N_i}=0\) for some \(N_i\).

Now choose \(J_r\) fixing the vector and smooth dual vector of a
coefficient \(c\). It is normal in \(K\), so their finitely many
\(K\)-translates also lie in the same fixed spaces. For
\(\lambda_1\geq\cdots\geq\lambda_n\), write
\(d_i=\lambda_i-\lambda_{i+1}\), \(i<n\). The diagonal semigroup gives
\[
c(k_1a_\lambda k_2)
=\ell_{k_1}\!\left(
T_n^{\lambda_n}\prod_{i<n}T_i^{d_i}v_{k_2}\right),
\qquad T_n=\pi(\varpi I_n)|_E .
\tag{1.24h}
\]
The central operator \(T_n\) is invertible and commutes with every
\(T_i\); negative central powers are therefore allowed, even when
\(\pi\) is not irreducible.
If any \(d_i\geq N_i\), this is zero. Modulo scalar
\(\varpi^{\lambda_n}I_n\), only finitely many Cartan double
cosets with \(0\leq d_i<N_i\) remain. Each is compact, so their
finite union is a compact support bound modulo \(Z\).

In the irreducible case Corollary 1.4a now gives \(L_\pi=1\).
Every coefficient of \(\widetilde\pi\) is the inversion of one
of \(\pi\), by the proved smooth bidual pairing, so the same
support assertion and the same corollary give
\(L_{\widetilde\pi}=1\). \(\square\)

Zero proper Jacquet modules therefore give the coefficient-support assertion. A compact-induction realization remains a separate assertion.

#### Trace integrality in a subgroup compact modulo the center

The next elementary observation supplies the sign of the conductor
without an inducing classification or a newvector theorem.

**Lemma 1.20b.** Let \(H\) be an open subgroup of \(G\) containing \(Z\),
with \(H/Z\) compact. Set \(H_j=\{h\in H:j(h)=j\}\).
Then \(H_0\) is compact open, every nonempty \(H_j\) is a coset
of \(H_0\), and
\[
h\in H,\quad j(h)\geq0\quad\Longrightarrow\quad
\operatorname{tr}(h)\in\mathcal O .
\tag{1.24i}
\]
Moreover, a single integer \(r_0\) has
\[
\bigcup_{j\geq0}H_j\subset\varpi^{-r_0}M_n(\mathcal O).
\tag{1.24j}
\]

**Proof.** Use the maximum entry norm \(\|h\|\). The continuous
function
\[
\rho(h)=\|h\|\,|\det h|^{-1/n}
\]
is unchanged by multiplying \(h\) by any scalar in \(Z\);
it is therefore bounded by a constant \(B\) on \(H\).
Likewise \(\rho(h^{-1})\) is bounded there. Thus on \(H_0\)
both the matrix entries and the inverse entries are uniformly
bounded. The set \(H_0\) is closed: an open subgroup is closed,
and \(j\) is continuous to the discrete group \(\mathbb Z\).
These entry and inverse-entry bounds put it in a compact subset
of \(G\); explicitly, its determinants are units, so the closed
bounded matrix set has no singular limit. Hence \(H_0\) is
compact. It is open as an intersection of two open subgroups.
The coset assertion follows from the homomorphism \(j:H\to\mathbb Z\).
The bound
\(\|h\|\leq Bq^{-j(h)/n}\leq B\) for \(j(h)\geq0\) proves (1.24j).

Fix such an \(h\). All its nonnegative powers lie in \(H\), and
\[
\|h^b\|\leq Bq^{-b j(h)/n}\leq B,\qquad b\geq0.
\]
Consequently
\(\Lambda=\sum_{b\geq0}h^b\mathcal O^n\) is an
\(\mathcal O\)-submodule between \(\mathcal O^n\) and
\(\varpi^{-R}\mathcal O^n\) for some \(R\). The latter quotient
by \(\mathcal O^n\) is finite, so this sum is finitely generated.
A submodule of a finite free module over the discrete valuation
ring is free: choose a coordinate with an element of least
valuation, eliminate that coordinate, and induct on the rank,
just as in the preceding Smith reduction. Since \(\Lambda\)
contains \(\mathcal O^n\), its rank is \(n\). Also
\(h\Lambda\subset\Lambda\). The matrix of \(h\) in a basis of
\(\Lambda\) therefore has integral entries. Its trace is integral,
and trace is invariant under the change of basis. This proves
(1.24i) in every residue characteristic. \(\square\)

#### Positive conductor for arbitrary compact inducing data

For an open \(H\) as in Lemma 1.20b and a finite-dimensional smooth
irreducible representation \(\tau\) of \(H\), compact induction
means the space of smooth functions
\[
f:G\longrightarrow W_\tau,\qquad f(hg)=\tau(h)f(g),
\]
with support in finitely many left \(H\)-cosets, acted on by right
translation. No classification or irreducibility theorem for such
an induction is assumed below: irreducibility and admissibility
of this realization are explicit hypotheses.

**Theorem 1.20.** Suppose
\[
\pi\simeq\mathrm{c\!-\!Ind}_H^G\tau
\tag{1.24k}
\]
is irreducible smooth admissible, \(H\supset Z\) is open and compact
modulo \(Z\), and \(\tau\) is finite-dimensional smooth irreducible.
For conductor-zero \(\psi\), the matrix exponent satisfies
\[
a_\pi>0.
\tag{1.24l}
\]
More precisely, choose \(r\geq1\) such that \(J_r\subset H\),
\(\tau(J_r)=1\), and (1.24j) holds with \(r\) in place of \(r_0\).
Then
\[
1\leq a_\pi\leq nr,\qquad a_\pi\in j(H)\subset\mathbb Z.
\tag{1.24m}
\]
This includes all positive-depth data satisfying (1.24k).

**Proof.** First \(\tau^{H_0}=0\). Otherwise this nonzero space
is \(H\)-stable, because \(H_0\) is normal, and irreducibility
would make \(\tau\) trivial on \(H_0\). The group
\(H/H_0=j(H)=d\mathbb Z\) is cyclic, with \(d\mid n\), since
\(\varpi I_n\in H\). A finite-dimensional irreducible complex
representation of a cyclic group is one-dimensional: an
eigenvector of its generator gives an invariant line. Thus
\(\tau(h)=b^{j(h)/d}\). Choose \(a\in\mathbb C^\times\) with
\(a^d=b\), and put \(\chi(g)=a^{j(g)}\). It extends \(\tau\).
There is then the explicit nonzero equivariant map
\[
f\longmapsto\sum_{Hg\in H\backslash G}\chi(g)^{-1}f(g)
\tag{1.24n}
\]
from the compact induction to the one-dimensional \(\chi\).
The finite sum is independent of the left-coset representatives;
substitution \(g\mapsto gx\) multiplies it by \(\chi(x)\).
Irreducibility would identify \(\pi\) with \(\chi\).
This is impossible: \(H\backslash G\) is infinite, so its compact
induction has infinite dimension. Indeed otherwise \(G/Z\)
would be a finite union of translates of the compact \(H/Z\).
But the continuous scalar-invariant function
\(\|g\|\|g^{-1}\|\) takes the unbounded values \(q^b\) on
\(\operatorname{diag}(\varpi^b,1,\ldots,1)\), \(b\geq0\);
thus \(G/Z\) is not compact. This proves the assertion.

Every coefficient of \(\pi\) has compact support modulo \(Z\).
Here is the complete dual-support justification. For
\(\lambda\in W_\tau^*\), evaluation
\(\ell_\lambda(f)=\lambda(f(1))\) is a smooth dual vector:
an open subgroup of \(H\) fixing \(\lambda\) fixes this
functional. The span of all its \(G\)-translates is a nonzero
invariant subspace of the irreducible smooth dual, hence the
whole smooth dual by Proposition 1.3 §1. A coefficient using
evaluation is \(g\mapsto\lambda(f(g))\), supported in finitely
many \(H\)-cosets. Translated evaluation and a finite linear
combination give the same conclusion with finitely many
translated \(H\)-cosets. These sets have compact image modulo
\(Z\). Corollary 1.4a therefore gives
\[
L_\pi=L_{\widetilde\pi}=1,\qquad \gamma_\pi=\epsilon_\pi.
\tag{1.24o}
\]

Choose \(v_0\in W_\tau\) and \(\lambda\in W_\tau^*\) with
\(\lambda(v_0)=1\). Let \(v\) be supported on \(H\), with
\(v(h)=\tau(h)v_0\), and use \(\ell_\lambda\). The coefficient
is exactly
\[
c(g)=
\begin{cases}
\lambda(\tau(g)v_0),&g\in H,\\
0,&g\notin H.
\end{cases}
\tag{1.24p}
\]
Our choice of \(r\) makes both vectors \(J_r\)-fixed. The test
\(\Phi=\operatorname{vol}_G(J_r)^{-1}1_{J_r}\) has
\(Z_\pi(s,\Phi,c)=1\). Since \(J_r=I_n+\varpi^rM_n(\mathcal O)\)
as an additive matrix coset, character orthogonality with the
positive trace pairing gives
\[
\widehat\Phi(Y)=A_r\psi(\operatorname{tr}Y)
1_{\varpi^{-r}M_n(\mathcal O)}(Y),\qquad
A_r=\frac{q^{-rn^2}}{\operatorname{vol}_G(J_r)}.
\tag{1.24q}
\]
In fact \(A_r=\prod_{i=1}^n(1-q^{-i})\), independently of \(r\):
\([K:J_r]=|\mathrm{GL}_n(\mathcal O/\varpi^r)|=
q^{rn^2}\prod_i(1-q^{-i})\), by reduction modulo \(\varpi\),
its \(q^{n^2}\)-element successive kernels, and ordered-basis
counting over the residue field.

Consider the dual integral with this test. On a shell \(H_j\),
\(j\geq0\), its test is the constant \(A_r\): the lattice
condition holds by our choice of \(r\), and the trace character
is 1 by Lemma 1.20b. This shell contributes zero, because
\[
\int_{H_j}\lambda(\tau(g^{-1})v_0)\,dg=0.
\tag{1.24r}
\]
To verify (1.24r), write \(H_j=h_jH_0\) and use the probability
average \(e_{H_0}\) of \(\tau\). It is the projection onto
\(\tau^{H_0}=0\). Inversion preserves Haar measure on the
compact group \(H_0\), so the integral is
\(\operatorname{vol}_G(H_0)\lambda(e_{H_0}\tau(h_j^{-1})v_0)=0\).
Every individual shell is compact; these cancellations are
valid first in the absolutely convergent dual half-plane.

If \(g\in\varpi^{-r}M_n(\mathcal O)\), expansion of its
determinant gives \(j(g)\geq-nr\). Thus only the finitely many
negative shells can remain, and the Fourier equation with
the integral-1 test is the polynomial identity
\[
\epsilon_\pi(s,\psi)=
\sum_{j=-nr}^{-1} A_r q^{-j(n+1)/2} X^{-j}
\int_{H_j\cap\varpi^{-r}M_n(\mathcal O)}
\psi(\operatorname{tr}g)\lambda(\tau(g^{-1})v_0)\,dg .
\tag{1.24s}
\]
Empty shells are zero. Every exponent on the right lies
between 1 and \(nr\). The left side is a nonzero Laurent
monomial by the proved scalar Fourier equation and ideal
normalization (1.24d). Hence exactly one shell coefficient is
nonzero; its exponent is \(a_\pi=-j\). Since \(j\in j(H)\),
also \(-j\in j(H)\). This proves (1.24l)–(1.24m).
No unitarity hypothesis, restriction on the residue
characteristic, or generic newvector was used. \(\square\)

Equation (1.24s) is also an exact inducing-data interpretation:
\(-a_\pi\) is the unique determinant shell carrying the nonzero
matrix Gauss average displayed there. This assertion is independent
of the chosen sufficiently large \(r\), \(v_0\) and \(\lambda\)
with \(\lambda(v_0)=1\), since all give the same scalar
\(\epsilon_\pi\). It identifies that shell, not an Artin conductor
or the minimal newvector level.

**Corollary 1.20c (a depth-zero realization).** Let
\(\sigma\) be an irreducible representation of
\(\mathrm{GL}_n(\mathbb F_q)\) with zero invariants under the
unipotent radical of every proper parabolic. Inflate it to \(K\).
Extend its scalar central character on \(\mathcal O^\times\) to
a smooth character \(\omega:k^\times\to\mathbb C^\times\);
one may choose \(\omega(\varpi)\) arbitrarily. Then
\[
\tau(zk)=\omega(z)\sigma(\bar k),\qquad
\pi=\mathrm{c\!-\!Ind}_{ZK}^G\tau
\tag{1.24sa}
\]
is irreducible smooth admissible, and \(a_\pi=n\).

**Proof.** The displayed \(\tau\) is well-defined: two
decompositions differ by a scalar unit, on which its two
characters agree. It is finite-dimensional smooth irreducible.
We prove the hypotheses on \(\pi\), rather than use a
compact-induction irreducibility criterion.

For a \(J_r\)-fixed function \(f\), if \(f(g)\ne0\), every
\(u\in K\cap gJ_rg^{-1}\) fixes \(f(g)\) under \(\tau\),
because \(ug=gj\) implies
\(\tau(u)f(g)=f(ug)=f(gj)=f(g)\).
Write \(g=k_1a_\lambda k_2\) in Cartan form. Since \(J_r\)
is normal in \(K\), \(k_2\) does not change the intersection
condition; \(k_1\) just conjugates its subgroup in \(K\).
If some gap \(\lambda_i-\lambda_{i+1}\geq r\), the opposite
two-block unipotent group with all its lower off-block entries
in \(\mathcal O\) lies in \(K\cap a_\lambda J_ra_\lambda^{-1}\).
Indeed conjugation by \(a_\lambda^{-1}\) multiplies its
\((b,a)\) entry, \(b>i\geq a\), by
\(\varpi^{\lambda_a-\lambda_b}\), which belongs to
\(\varpi^r\mathcal O\). Its reduction is the full opposite
unipotent radical of that proper parabolic. The assumption on
\(\sigma\), also for conjugate parabolics, forces \(f(g)=0\).

Thus every gap on the support of a \(J_r\)-fixed function
is smaller than \(r\). After removing the central
\(\varpi^{\lambda_n}I_n\), only finitely many Cartan forms
remain. Each gives finitely many left \(ZK\)- and right
\(J_r\)-cosets, since \(K/J_r\) is finite. Values in the
finite-dimensional \(W_\tau\) therefore prove
\(\dim\pi^{J_r}<\infty\). Every compact open subgroup contains
a \(J_r\), proving admissibility.

For \(r=1\), the support condition says that all gaps vanish,
so \(\pi^{J_1}\) consists exactly of the functions supported
on \(ZK\). Evaluation at 1 identifies this space with
\(\sigma\) as a \(K\)-module. If a nonzero invariant subspace
of \(\pi\) contains \(f\), translate a nonzero value to 1
and average over \(J_1\). The averaged value at 1 remains
that value, since \(\tau(J_1)=1\). Thus the subspace meets
\(\pi^{J_1}\) nontrivially, contains it by irreducibility of
\(\sigma\), and contains all of \(\pi\): its translates
span the functions on every finite collection of \(ZK\)-cosets.
This proves irreducibility.

Apply Theorem 1.20 with \(H=ZK\) and \(r=1\). Its hypotheses
hold, including (1.24j), since
\(H_j=\varpi^{j/n}K\) for \(j\in n\mathbb Z\).
Consequently \(1\leq a_\pi\leq n\) and \(a_\pi\in n\mathbb Z\),
so \(a_\pi=n\).

For completeness its exact positive-trace epsilon constant is
\[
\epsilon_\pi(s,\psi)=
C_n\,\omega(\varpi)\,q^{n(n+1)/2}\,\mathcal G_\sigma X^n,
\quad C_n=\prod_{i=1}^n(1-q^{-i}),
\tag{1.24sb}
\]
where the finite-group operator
\[
\frac1{|\mathrm{GL}_n(\mathbb F_q)|}
\sum_{h\in\mathrm{GL}_n(\mathbb F_q)}
\psi_{\mathrm{res}}(\operatorname{tr}h)\sigma(h^{-1})
=\mathcal G_\sigma I
\tag{1.24sc}
\]
is scalar by conjugation invariance and the finite-dimensional
Schur argument. Here
\(\psi_{\mathrm{res}}(\bar x)=\psi(\varpi^{-1}x)\) is well-defined on the
residue field. Formula (1.24sb) is (1.24s) on its sole negative
shell \(\varpi^{-1}K\). The nonzero scalar Fourier theorem
proves \(\mathcal G_\sigma\ne0\), so no unproved nonvanishing
theorem for finite Gauss sums has been used. \(\square\)

#### The polynomial correction in a parabolic reduction

The algebraic step in a general reduction can be proved without
assuming that epsilon exponents are already nonnegative.

**Lemma 1.20d (conditional parabolic transfer).** Let \(\sigma\) and
\(\pi_1,\ldots,\pi_t\) be irreducible smooth admissible
representations with the matrix ideal and scalar Fourier theorem.
Suppose the following additional identities have been proved for
this data, with the same conductor-zero additive character:
\[
\gamma_\sigma(s,\psi)=\prod_i\gamma_{\pi_i}(s,\psi),\qquad
L_\sigma(s)=R(X)\prod_iL_{\pi_i}(s),\qquad
L_{\widetilde\sigma}(s)=\widetilde R(X)
\prod_iL_{\widetilde\pi_i}(s),
\tag{1.24t}
\]
where \(R,\widetilde R\in\mathbb C[X]\) and
\(R(0)=\widetilde R(0)=1\). Then
\[
\deg R=\deg\widetilde R=d,\qquad
a_\sigma=\sum_i a_{\pi_i}+d .
\tag{1.24u}
\]
In particular nonnegative exponents for the inducing data give a
nonnegative exponent for \(\sigma\).

**Proof.** Substituting (1.24d) into the first identity gives
\[
\frac{\epsilon_\sigma(s)}{\prod_i\epsilon_{\pi_i}(s)}
=\frac{R(X)}{\widetilde R(q^{-1}X^{-1})}.
\tag{1.24v}
\]
The left side is \(bX^e\), with
\(e=a_\sigma-\sum_i a_{\pi_i}\). The order at \(X=0\) of the
right side is \(\deg\widetilde R\): \(R\) has nonzero constant
term, while the reversed polynomial in the denominator has
order \(-\deg\widetilde R\). Thus \(e=\deg\widetilde R=d\).
The identity
\[
R(X)=bX^d\widetilde R(q^{-1}X^{-1})
\tag{1.24w}
\]
has degree exactly \(d\), because \(\widetilde R(0)=1\).
Hence \(\deg R=d\) as well, and (1.24u) follows. \(\square\)

It is essential to include the factor \(X^d\) in (1.24w).
The unqualified identity
\(\widetilde R(X)=R(q^{-1}X^{-1})\) cannot hold for two
nonconstant polynomials with constant term 1. We do not use
such a reversed-polynomial assertion as an inducing theorem.
The identities (1.24t) themselves are not proved by this algebra,
by the scalar Fourier theorem, or by the existence of the ideal.


Theorem 1.20 includes positive-depth inducing data, whenever the stated compact induction is irreducible and admissible. It does not assert that every cuspidal representation has such a realization. Lemma 1.20a proves the coefficient-support direction from zero proper Jacquet modules; it does not construct an inducing subgroup. Theorem 1.23 and Corollary 1.23c below prove the parabolic identities (1.24t), and Theorem 1.23e proves cuspidal-support embedding. Lemmas 1.23f–1.23g construct compact inducing data under their precise orthogonality or compact-intertwining hypotheses. Universal existence of such data is not asserted. The direct proof in Theorem 1.24 and the parabolic transfer in Corollary 1.24c prove general nonnegativity without requiring those inducing data.

The exponent in (1.24s) has a precise matrix-Gauss-shell meaning. Identification with an Artin conductor requires a parameter construction and epsilon compatibility; identification with a minimal newvector level requires a generic newvector theorem. The latter cannot be extended to every irreducible representation. For the usual subgroup
\[
K_1(\varpi^a)=\{g\in K:g_{nj}\in\varpi^a\mathcal O\ (j<n),\quad
g_{nn}\equiv1\pmod{\varpi^a}\},\qquad a\geq1,
\]
every \(\operatorname{diag}(u,1,\ldots,1)\), \(u\in\mathcal O^\times\), belongs to \(K_1(\varpi^a)\). A ramified determinant character in rank at least two therefore has no fixed vector at any such level or at level zero \(K\), although Proposition 1.16 proves its finite epsilon exponent.

Further reading on the normalization and the general cuspidal-support reduction is [Goldfeld–Jacquet, author notes, §2.1 and Theorem 2.1/Lemma 2.2, PDF pages 5–9](https://www.math.columbia.edu/~goldfeld/LanglandsBookChapter.pdf).

### Cuspidal support and parabolic matrix factors

Fix a nonarchimedean local field \(k\), integers \(\mathcal O\),
uniformizer \(\varpi\), and residue cardinality \(q\). All
representations are complex, smooth and admissible, and irreducible
when so stated. Let
\[
G=\mathrm{GL}_n(k),\quad K=\mathrm{GL}_n(\mathcal O),\quad
\nu(g)=|\det g|,\quad X=q^{-s}.
\tag{1.27a}
\]
Multiplicative Haar measure gives each standard maximal compact
volume 1. Additive matrix measures are self-dual for the positive
trace pairing with the same conductor-zero character \(\psi\).
Thus every integral matrix lattice has additive volume 1.

We use Proposition 1.3’s complete matrix ideal and Theorem 1.17’s scalar Fourier equation. Every \(L\)-factor in this section denotes the normalized matrix-ideal generator; identification with parameter factors is a separate question.
The tensor factorization used below is the fully general local-unit
algebra theorem, Theorem 4.1 of
*Restricted tensor products and the tensor product
theorem*.
Its proof concerns arbitrary algebras and finite-dimensional corners;
its use here does not import the rank-two restriction of that lesson's
subsequent adelic application.

#### Iwasawa integration and normalized induction in every rank

Let \(n=r+t\), \(r,t>0\), and put
\[
P=MU,\quad
M=\mathrm{GL}_r(k)\times\mathrm{GL}_t(k),\quad
U=\left\{u(B)=\begin{pmatrix}I_r&B\\0&I_t\end{pmatrix}\right\}.
\]
For \(m=\operatorname{diag}(A,D)\), the conjugation modulus is
\[
\delta_P(m)=|\det A|^t|\det D|^{-r}.
\tag{1.27b}
\]
This follows from \(B\mapsto ABD^{-1}\) on its \(rt\) additive
coordinates.

Here \(G=PK\). To see it directly, let \(W\subset k^n\) be the
row span of the last \(t\) rows of \(g\). The lattice
\(\Lambda=W\cap\mathcal O^n\) is saturated: if \(a x\in W\),
\(a\ne0\), then \(x\in W\). A basis of \(\Lambda\) extends
to an integral basis of \(\mathcal O^n\), by the following
explicit argument. If \(W\ne0\), scale a nonzero vector
of \(W\) so its coordinates are integral and at least one
is a unit. Move that unit coordinate to the last position
and use integral elementary coordinate changes to send
the vector to \(e_n\). These changes belong to
\(\mathrm{GL}_n(\mathcal O)\). Then
\[
W=k e_n\oplus(W\cap k^{n-1}),\qquad
W\cap\mathcal O^n=\mathcal O e_n
\oplus(W\cap k^{n-1}\cap\mathcal O^{n-1}).
\]
Induction on \(\dim W\) constructs the desired basis and
an integral complement. This also proves that the rank is
\(t\) and that the quotient lattice is free.
Let these basis vectors be the rows of \(k_0\in K\), with the
last \(t\) spanning \(\Lambda\). Expressing the rows of \(g\)
in this basis gives \(g=p k_0\), \(p\in P\): the last \(t\)
rows have zero first \(r\) coordinates, and both diagonal
blocks are invertible because \(g\) is invertible.

With \(dB\) giving \(M_{r,t}(\mathcal O)\) volume 1, left
Haar measure on \(P\), in the order \(u(B)m\), is
\[
dp=\delta_P(m)^{-1}\,dB\,dm .
\tag{1.27c}
\]
Left translation by \(U\) is additive translation; left
translation by \(m_0\) scales \(dB\) by \(\delta_P(m_0)\),
which cancels the extra inverse-modulus factor. This proves
left invariance, and \(P\cap K\) has volume 1.

For every integrable function on \(G\) the exact Iwasawa formula is
\[
\int_G F(g)\,dg
=\int_K\int_M\int_{M_{r,t}(k)}
F(u(B)m k)\delta_P(m)^{-1}\,dB\,dm\,dk .
\tag{1.27d}
\]
Indeed first average \(F\) on the right over \(K\). A right
\(K\)-invariant function integrates as a sum on the discrete
quotient \(G/K\), each coset of volume 1. The map
\(P/(P\cap K)\to G/K\) is a bijection by \(G=PK\).
Its cosets have volume 1 for the left Haar measure (1.27c).
This proves (1.27d), first for nonnegative functions by counting
cosets, then for integrable functions by linearity.

For a smooth admissible \(M\)-representation \(\rho\), normalized
induction \(I_P(\rho)\) consists of smooth functions \(f:G\to V_\rho\)
with a common right open stabilizer and
\[
f(u m g)=\delta_P(m)^{1/2}\rho(m)f(g).
\tag{1.27e}
\]
Right translation is the action. The quotient \(P\backslash G\)
is compact, as the image of \(K\).

**Lemma 1.23a.** Normalized induction is admissible, and its smooth
dual is \(I_P(\widetilde\rho)\), with invariant pairing
\[
\langle\widetilde f,f\rangle
=\int_K\langle\widetilde f(k),f(k)\rangle\,dk .
\tag{1.27f}
\]
It preserves injections and is exact.

**Proof.** Fix a compact open \(J\subset K\). The double quotient
\(P\backslash G/J\) is finite: a finite right \(J\)-cover of the
compact \(K\) supplies representatives \(k_\alpha\in K\).
A \(J\)-fixed section is determined by its values at these
representatives. Such a value is fixed by \(\rho\) under the
\(M\)-projection of \(P\cap k_\alpha Jk_\alpha^{-1}\); the
modulus on this compact group is 1. Its projection is compact
and contains a compact open subgroup of \(M\), since the
intersection contains \(M\cap k_\alpha Jk_\alpha^{-1}\).
Consequently its fixed space is finite-dimensional. There are
finitely many representatives, proving admissibility.

We verify the invariant pairing without assuming an invariant
measure on \(P\backslash G\). A smooth scalar function \(F\) with
\(F(pg)=\delta_P(p)F(g)\) is the finite sum, at its right level
\(J\), of the functions
\[
Q\eta(g)=\int_P\eta(pg)\,dp,\qquad \eta\in C_c^\infty(G).
\tag{1.27g}
\]
For \(\eta=1_{k_\alpha J}\), this function is supported on
\(P k_\alpha J\) and has value
\(\operatorname{vol}_P(P\cap k_\alpha Jk_\alpha^{-1})>0\)
at \(k_\alpha\). Left Haar measure satisfies
\(\int_P a(pp_0)\,dp=\delta_P(p_0)\int_P a(p)\,dp\)
by (1.27c), so \(Q\eta\) has precisely the required left
transformation. The finite representative values therefore
prove the spanning assertion. Formula (1.27d) gives
\[
\int_K Q\eta(k)\,dk=\int_G\eta(g)\,dg .
\]
Right translation commutes with \(Q\), and the right side is
right invariant, since the matrix Haar measure on \(G\)
is bi-invariant. Thus \(\int_K F(k)\,dk\) is a right
\(G\)-invariant functional on these scalar densities.
The product in (1.27f) has exactly this transformation;
hence (1.27f) is invariant.

It is nondegenerate. A nonzero section has a nonzero value
\(v\) at some \(k_\alpha\). Choose a dual vector detecting
that value and average it over the compact projected
stabilizer. Because \(v\) is fixed, its detected value is
unchanged. The dual section supported on \(P k_\alpha J\)
with that value exists by (1.27e). Its pairing with \(f\)
is a nonzero constant times the positive measure of the
corresponding subset of \(K\). This gives an injection of
the dual induction into the smooth dual. At every \(J\)
the two inducing fixed-value spaces are finite-dimensional
dual spaces, by compact averaging. Thus the fixed-space
dimensions agree, and the injection is onto every fixed
space, hence onto the entire smooth dual.

Injections are preserved pointwise. For a surjection of
smooth \(M\)-modules, a \(J\)-fixed target section has only
finitely many representative values. Lift each value,
then average over its compact projected stabilizer;
this supplies a fixed lift of that value. The sections
defined from these values by (1.27e), zero on the other
double cosets, give a preimage. For kernels, the section
takes values in the kernel exactly when its image section
is zero. This proves exactness. \(\square\)

#### The complete two-block matrix descent

Let \(\rho=\pi_1\otimes\pi_2\), with irreducible smooth admissible
\(\pi_1,\pi_2\) on \(\mathrm{GL}_r(k),\mathrm{GL}_t(k)\).
Set \(I=I_P(\rho)\). For \(f\in I\) and
\(\widetilde f\in I_P(\widetilde\rho)\), its coefficient is
\[
c_I(g)=\int_K\langle\widetilde f(k),f(kg)\rangle\,dk .
\tag{1.27h}
\]
For \(\Phi\in\mathcal S(M_n(k))\), define
\[
\Phi^P_{k,k'}(A,D)=
\int_{M_{r,t}(k)}
\Phi\left(k^{-1}\begin{pmatrix}A&C\\0&D\end{pmatrix}k'\right)dC,
\qquad
c_{k,k'}(A,D)=
\langle\widetilde f(k),\rho(A,D)f(k')\rangle .
\tag{1.27i}
\]
Each \(\Phi^P_{k,k'}\) is a Schwartz–Bruhat function on the
product of the two matrix spaces. These functions and the two
section values have only finitely many possibilities as
\((k,k')\) ranges over \(K\times K\). A common sufficiently
small principal congruence subgroup fixes \(\Phi\) on both
sides and fixes both sections on the right. This makes the
dependence constant on finitely many compact cosets.

For a Levi test \(\Psi\) and coefficient \(b\), put
\[
Z_\rho(s,\Psi,b)=
\int_{\mathrm{GL}_r(k)\times\mathrm{GL}_t(k)}
\Psi(A,D)b(A,D)
|\det A|^{s+(r-1)/2}|\det D|^{s+(t-1)/2}\,dA\,dD .
\tag{1.27j}
\]
Every such integral is a finite sum of products of the two
factor zeta integrals. A product-space Schwartz function is
a finite sum of rectangular product tests, by partition into
cosets of a common additive product lattice. A coefficient
has the same finite-product property: the vectors are finite
sums of tensors, and a smooth dual vector fixed by a product
compact subgroup is in the dual of its finite-dimensional
fixed space, the tensor product of the factor fixed spaces.
Compact averaging extends its finite tensor expression to
the factor smooth duals.

**Lemma 1.23b (matrix descent).** In an absolute-convergence
right half-plane, and consequently for the rational continuations,
\[
Z_I(s,\Phi,c_I)
=\int_{K\times K}Z_\rho(s,\Phi^P_{k,k'},c_{k,k'})\,dk\,dk' .
\tag{1.27k}
\]
Every induced coefficient integral is rational and its entire
ideal is
\[
\mathcal I_I=L_{\pi_1}(s)L_{\pi_2}(s)\,
\mathbb C[X,X^{-1}] .
\tag{1.27l}
\]
Here the ideal is the span of all induced tests and coefficients;
no irreducibility of \(I\) is required.

**Proof.** Insert (1.27h) and substitute \(h=kg\), then apply
(1.27d) to \(h=u(B)m k'\). The section law supplies
\(\delta_P(m)^{1/2}\rho(m)\), leaving
\(\delta_P(m)^{-1/2}\nu(m)^{s+(n-1)/2}\).
In
\[
u(B)m=\begin{pmatrix}A&BD\\0&D\end{pmatrix}
\]
put \(C=BD\); then \(dB=|\det D|^{-r}dC\).
The resulting two determinant powers are exactly
\[
s+(n-1)/2-t/2=s+(r-1)/2,\qquad
s+(n-1)/2+r/2-r=s+(t-1)/2 .
\tag{1.27m}
\]
This proves (1.27k).

It also justifies all these rearrangements initially:
with absolute values inserted, the \(C\)-integral is again
a bounded compactly supported locally constant Levi test.
There are finitely many section values and tests on \(K^2\).
Factor absolute convergence therefore supplies a common
right half-plane. The finite factor expansion gives
rational continuation and the inclusion
\(\mathcal I_I\subset L_{\pi_1}L_{\pi_2}\mathbb C[X,X^{-1}]\).

We prove the reverse inclusion by constructing actual sections
and tests; it is not an assertion of generator attainment.
Given factor vectors and dual vectors, form
\(v=v_1\otimes v_2\), \(\ell=\ell_1\otimes\ell_2\).
Given factor tests \(\Phi_1,\Phi_2\), take a compact matrix
test
\[
\Phi\begin{pmatrix}A&C\\W&D\end{pmatrix}
=\Phi_1(A)\Phi_2(D)\eta(C)\zeta(W),
\quad \int\eta(C)\,dC=1,\quad \zeta(0)=1 .
\tag{1.27n}
\]
For example normalized lattice indicators supply \(\eta,\zeta\).
Then \(\Phi^P_{1,1}=\Phi_1\Phi_2\).

Choose \(J=J_a\) small enough that \(\Phi\) is bi-\(J\)-invariant
and that \(J\cap M\) fixes \(v,\ell\). Such matrix-test
invariance is explicit: if the support is in
\(\varpi^{-B}M_n(\mathcal O)\) and the additive constancy
lattice is \(\varpi^R M_n(\mathcal O)\), take \(a-B\geq R\).
Left and right multiplication by \(J_a\) changes a matrix
in this ball by that constancy lattice and preserves the
ball, since both a matrix in \(J_a\) and its inverse are
integral. Smoothness gives the remaining vector condition.

Let \(f,\widetilde f\) be the sections supported on \(PJ\)
with respective values \(v,\ell\) at 1, extended by (1.27e).
They are well-defined: the \(M\)-projection of \(P\cap J\)
fixes those values, its modulus is 1, and \(U\) acts trivially.
Only \(k,k'\in (P\cap K)J\) contribute to (1.27k).
Write \(k=pj\), \(k'=p'j'\), \(p,p'\in P\cap K\).
Bi-\(J\)-invariance removes \(j,j'\) from the test.
Write \(m_p,m_{p'}\) for the diagonal blocks of \(p,p'\).
Both have unit determinants. The upper off-diagonal integration
is changed by an affine bijection preserving its additive
measure, so
\[
\Phi^P_{p,p'}(m)=\Phi^P_{1,1}(m_p^{-1}m m_{p'}),\qquad
c_{p,p'}(m)=\langle\ell,\rho(m_p^{-1}m m_{p'})v\rangle .
\tag{1.27o}
\]
The Levi change of variable \(m\mapsto m_p^{-1}m m_{p'}\)
preserves Haar measure and both determinant weights.
Every contributing \(Z_\rho\) therefore has the same value
\[
Z_{\pi_1}(s,\Phi_1,c_1)Z_{\pi_2}(s,\Phi_2,c_2).
\]
If \(b=\operatorname{vol}_K((P\cap K)J)>0\), (1.27k) is
exactly \(b^2\) times this product. Thus every product of
actual factor integrals is an actual induced integral up
to a nonzero constant. The product of their entire ideals
is generated by these products. Simultaneous determinant
translations also make \(\mathcal I_I\) a Laurent-ring
module, by the same change of variable as in Proposition
1.3. This proves (1.27l). \(\square\)

#### Fourier descent and the gamma factor

Let \(\mathcal F_M\) denote the product of the factor matrix
Fourier transforms with the same positive trace convention.
The exact elementary identity is
\[
(\widehat\Phi)^P_{k,k'}
=\mathcal F_M\bigl(\Phi^P_{k',k}\bigr).
\tag{1.27p}
\]
To prove it first put \(k=k'=1\). In the trace pairing,
the upper-right block of the Fourier variable pairs with
the lower-left block of the original variable. Integrating
over that Fourier block therefore sets the original
lower-left block to zero. What remains is the factor
Fourier transform of the upper-right integral in (1.27i).
This statement uses ordinary finite Fourier orthogonality,
not a distributional delta assertion: partition a
Schwartz–Bruhat test into additive matrix-lattice cosets;
the scalar coset Fourier formula of Proposition 1.3 §6
proves the identity for each rectangular coset indicator.
Refining to a common lattice and adding proves it for
every test.

More explicitly, for a rectangular product
\(\Phi(A,C,W,D)=\phi_1(A)\eta(C)\zeta(W)\phi_2(D)\),
its transform is
\[
\widehat\phi_1(A')\widehat\phi_2(D')
\widehat\eta(W')\widehat\zeta(C').
\]
The rectangular Fourier transforms use the dual trace
pairing between \(M_{r,t}\) and \(M_{t,r}\).
Putting \(W'=0\) and integrating \(C'\) gives
\(\widehat\phi_1(A')\widehat\phi_2(D')
(\int\eta)\zeta(0)\), exactly the Levi transform of
\(\Phi^P_{1,1}\). The identity
\(\int\widehat\zeta=\zeta(0)\) follows from the same
lattice-coset orthogonality formula and the chosen
self-dual measures; no extra block-volume constant occurs.

For \(k,k'\in K\), the matrix substitution
\(A=k^{-1}Bk'\) has additive Jacobian 1, and the trace is
cyclic. The Fourier covariance swaps \(k,k'\):
\[
\widehat{\Phi(k^{-1}(\,\cdot\,)k')}(Y)
=\widehat\Phi(k'^{-1}Yk).
\]
Combining this with the identity at 1 proves (1.27p),
including the index order.

**Theorem 1.23.** For every induced test and coefficient,
\[
Z_{\widetilde I}(1-s,\widehat\Phi,c_I^\vee)
=\gamma_{\pi_1}(s,\psi)\gamma_{\pi_2}(s,\psi)
Z_I(s,\Phi,c_I).
\tag{1.27q}
\]
Thus the induced gamma factor is the product, in every
residue characteristic and for the full ramified family.

**Proof.** The invariant pairing (1.27f) identifies \(c_I^\vee\)
with the coefficient on \(\widetilde I\) whose vector is
\(\widetilde f\) and whose dual vector is \(f\).
Its descended coefficient at indices \(k,k'\) is
\[
\langle\widetilde\rho(m)\widetilde f(k'),f(k)\rangle
=c_{k',k}(m^{-1}).
\tag{1.27r}
\]
Apply (1.27k) to the dual integral, use (1.27p), and apply
the proved whole-family factor Fourier equations to each
of the finitely many factor test/coefficient terms.
They multiply every term by
\(\gamma_{\pi_1}(s,\psi)\gamma_{\pi_2}(s,\psi)\).
Finally exchange \(k,k'\) in the compact integral; (1.27k)
gives (1.27q). Both descent formulas are rational identities,
so their initial convergence half-planes need not intersect.
The resulting identity holds for their rational continuations.
\(\square\)

**Corollary 1.23c (every irreducible constituent).** If
\(\sigma\) is any irreducible subquotient of \(I_P(\pi_1\otimes\pi_2)\),
then
\[
\gamma_\sigma=\gamma_{\pi_1}\gamma_{\pi_2},\qquad
L_\sigma(s)=R(X)L_{\pi_1}(s)L_{\pi_2}(s),\quad R(0)=1,
\quad R\in\mathbb C[X].
\tag{1.27s}
\]
The dual identity has an analogous
\(\widetilde R\in\mathbb C[X]\), \(\widetilde R(0)=1\).
No finite-length assumption is needed.

**Proof.** For a subrepresentation, every smooth dual functional
on it extends smoothly to the ambient module: choose a compact
open \(J\) fixing the functional, extend its linear restriction
from the subspace of \(J\)-fixed vectors to the ambient
\(J\)-fixed space, and compose with \(e_J\).
The restriction remains the original functional.
For a quotient, lift the vector and compose the dual
functional with the quotient map. Thus every coefficient
of any subquotient is a coefficient of the original
induction, through a submodule and a quotient as needed.
Its integral and inverse-coefficient Fourier equation are
identical to the ambient ones. The nonzero integral-1
test fixes its scalar, giving the first identity in (1.27s).

The same lifting gives \(\mathcal I_\sigma\subset\mathcal I_I\).
Since their normalized generators are \(L_\sigma=1/P_\sigma\)
and \(L_I=1/(P_{\pi_1}P_{\pi_2})\), (1.27l) implies
\[
R(X)=\frac{P_{\pi_1}(X)P_{\pi_2}(X)}{P_\sigma(X)}
\in\mathbb C[X,X^{-1}].
\]
It is regular at 0 with value 1, so has no negative powers.
This proves the polynomial assertion.

Smooth duality is exact for admissible smooth modules:
the same extension by compact averaging proves surjectivity
of restriction for an injection, and composition proves
the other direction. Every submodule and quotient is
admissible, since compact averages lift its fixed vectors
in the quotient. Lemma 1.23a identifies the dual induction.
Consequently \(\widetilde\sigma\) is a subquotient of
\(I_P(\widetilde\pi_1\otimes\widetilde\pi_2)\), and the
same ideal argument proves its polynomial identity.
\(\square\)

With the scalar Laurent-unit epsilon already proved, these
identities supply the precise correction without any remaining
parabolic premise:
\[
\deg R=\deg\widetilde R=d,\qquad
a_\sigma=a_{\pi_1}+a_{\pi_2}+d,\qquad
R(X)=bX^d\widetilde R(q^{-1}X^{-1}),\quad b\ne0.
\tag{1.27t}
\]
Indeed divide (1.27s)'s gamma identity by the two \(L\)-factor
ratios. The epsilon ratio is a Laurent monomial. Its order
at \(X=0\) is exactly \(\deg\widetilde R\), since \(R(0)=1\).
The last identity then gives \(\deg R=d\).

#### General cuspidal-support embedding without classification

For a two-block \(P=MU\), write
\(r_U(V)=\delta_P^{-1/2}V_U\).
The unnormalized quotient \(V_U\) is the quotient by all
\(\pi(u)v-v\).

**Lemma 1.23d (reciprocity and a noncuspidal embedding).**
For smooth modules there is the exact normalized adjunction
\[
\operatorname{Hom}_G(V,I_P(\rho))
=\operatorname{Hom}_M(r_U(V),\rho).
\tag{1.27u}
\]
If \(V\) is irreducible admissible and \(V_U\ne0\), there
are irreducible admissible \(\pi_1,\pi_2\) on the two blocks
and an embedding \(V\hookrightarrow I_P(\pi_1\otimes\pi_2)\).

**Proof.** Evaluate an intertwining section at 1.
Its value map \(T:V\to V_\rho\) has
\[
T(\pi(u)v)=T(v),\qquad
T(\pi(m)v)=\delta_P(m)^{1/2}\rho(m)T(v),
\]
so factors through the indicated normalized quotient.
Conversely a map on that quotient gives
\((Av)(g)=T(\pi(g)v)\).
The displayed identities prove the section law (1.27e),
and an open subgroup fixing \(v\) fixes this section on
the right. It is equivariant under right translation.
Evaluation and this construction are inverse, proving (1.27u).

The quotient \(r_U(V)\) is finitely generated under \(M\).
Choose a nonzero cyclic vector \(v\) of \(V\). Its
finite-dimensional compact \(K\)-orbit span has a finite
basis \(v_\alpha\), because an open stabilizer has finite
index in \(K\). By \(G=PK\), their Jacquet classes generate
\(V_U\) under \(M\); \(U\) has become trivial. Twisting
by \(\delta_P^{-1/2}\) preserves finite generation.
The actual compact-fixed Jacquet lemma, Lemma 1.17a,
proves that this quotient is admissible.

It has a simple nonzero quotient \(S\). In Zorn's argument
the union of a chain of proper submodules cannot contain
all its finite set of generators unless one member already
does; hence a maximal proper submodule exists. The quotient
\(S\) is smooth and admissible by compact averaging.
The actual arbitrary-algebra tensor theorem factors it as
\(S=\pi_1\otimes\pi_2\) with irreducible admissible block
representations. For completeness its hypotheses apply
here: the two group Hecke algebras have local units \(e_J\);
finite product test functions identify the product group
Hecke algebra with their algebraic tensor product, and
\((e_{J_1}\otimes e_{J_2})S=S^{J_1\times J_2}\) is finite.
A Hecke-invariant subspace is group-invariant, since
on a \(J\)-fixed vector translation by \(g\) is the action
of \(\operatorname{vol}(J)^{-1}1_{gJ}\). Thus simplicity
and admissibility are exactly the algebra theorem's
hypotheses. Its proved Theorem 4.1 supplies the factors.

Here the abstract factor modules really give smooth group
representations. For a factor vector \(x=e_Jx\) define
\[
\pi(g)x=h_{g,J}x,\qquad
h_{g,J}=\operatorname{vol}(J)^{-1}1_{gJ}.
\]
If \(L\subset J\), convolution gives
\(h_{g,L}e_J=h_{g,J}\); a common subgroup of two choices
therefore proves independence of \(J\).
Also \(e_{gJg^{-1}}h_{g,J}=h_{g,J}\), so the image is
fixed at that conjugate level. With
\(L\subset g_2Jg_2^{-1}\) the convolution identity
\(h_{g_1,L}h_{g_2,J}=h_{g_1g_2,J}\) proves the group
law. This constructs a smooth action. Partitioning a
compact test into finitely many right \(J\)-cosets shows
that its original algebra action is the integral of this
group action. Hence group-fixed spaces are exactly the
local-unit corners and invariant subspaces are the same;
the factors are indeed irreducible admissible group
representations.

Applying (1.27u) to the quotient map gives a nonzero
map \(V\to I_P(S)\). Its kernel is zero by irreducibility.
\(\square\)

Normalized induction is transitive with its exact square-root
moduli. If \(Q\) is a standard parabolic of \(M\), and
\(R=Q U\subset P\), then
\[
I_P^G(I_Q^M(\tau))\simeq I_R^G(\tau).
\tag{1.27v}
\]
Here \(\delta_R(q)=\delta_P(q)\delta_Q(q)\), since conjugation
on the two successive unipotent radicals multiplies their
coordinate determinants. An explicit isomorphism sends
\[
f_R\longmapsto
\bigl[g\mapsto(m\mapsto\delta_P(m)^{-1/2}f_R(mg))\bigr],
\qquad F\longmapsto[g\mapsto F(g)(1)].
\tag{1.27w}
\]
Substituting \(q m\) verifies the inner \(Q\)-section law;
substituting \(u m_0 g\) verifies the outer \(P\)-section
law and its factor \(\delta_P(m_0)^{1/2}\).
The maps are inverse and commute with right translation.
If \(J\) fixes \(f_R\) on the right, it also fixes the
outer section on the right. For each fixed \(g\), its
inner section is fixed by the compact open subgroup
\(M\cap gJg^{-1}\), after shrinking \(J\) to a compact
open subgroup. The modulus is 1 on that subgroup.
This proves both smoothness requirements.
For the inverse a right stabilizer of \(F\) fixes
its evaluated section. Inducing simultaneously in both
blocks also commutes with their tensor product: sections
on the two compact flag quotients have finite rectangular
locally constant partitions and finite tensor values,
so are finite sums of products. This proves the required
vector-space and action identification, not a statement
about arbitrary smooth functions on noncompact products.

**Theorem 1.23e (cuspidal support).** Every irreducible smooth
admissible representation of \(\mathrm{GL}_n(k)\) embeds
in normalized induction from an outer tensor product
of irreducible admissible block representations having
zero Jacquet modules for every proper two-block parabolic.

**Proof.** Induct on the rank. In rank 1 there is no proper
Jacquet condition, and an irreducible smooth admissible
representation is a character. Indeed a nonzero compact
fixed space is invariant under the abelian group \(k^\times\),
so irreducibility makes it the whole finite-dimensional space;
commuting complex matrices have a common eigenline, which
must be the whole space. In higher rank, if all such modules are
zero, take the representation itself as the sole block.
Otherwise apply Lemma 1.23d. Both block ranks are smaller,
so the induction hypothesis embeds each factor into an
induction of the indicated cuspidal factors. Induction
preserves injections by Lemma 1.23a, tensoring injections
over a field preserves injections, and (1.27v)–(1.27w)
combine the successive inductions. This proves the
embedding in finitely many steps. \(\square\)

The condition on the terminal blocks also means zero
Jacquet module for every proper parabolic. For a proper
standard multiblock parabolic choose a cut between two
of its blocks. Its unipotent radical contains the radical
of the resulting two-block parabolic, so its coinvariant
quotient is a further quotient of that already zero
two-block coinvariant module. Every parabolic of
\(\mathrm{GL}_n(k)\) stabilizes a flag; choosing a basis
adapted to that flag conjugates it to a standard
parabolic. Coinvariant vanishing is unchanged by
conjugation. Thus no extra nonstandard-parabolic
condition has been left implicit.

Combining this embedding with the two-block descent and
gamma theorem proves, for every such irreducible \(\sigma\),
with any resulting cuspidal block factors \(\rho_i\),
\[
\gamma_\sigma=\prod_i\gamma_{\rho_i},\qquad
L_\sigma=R(X)\prod_iL_{\rho_i},\quad
L_{\widetilde\sigma}=\widetilde R(X)\prod_iL_{\widetilde\rho_i},
\quad R(0)=\widetilde R(0)=1,
\tag{1.27x}
\]
and
\[
a_\sigma=\sum_i a_{\rho_i}+\deg R .
\tag{1.27y}
\]
For a general multiblock induction one applies the same
two-block formulas iteratively; when an intermediate
induction is reducible, its descent formula is applied
to its finite products of cuspidal coefficient families,
without requiring it to be irreducible. The kernel proof
uses only its explicitly known family formula, ideal and
dual pairing, so the iteration remains valid.

#### Parabolic reduction and the direct positivity proof

The parabolic formulas hold for the entire smooth admissible
matrix family and every irreducible constituent. Theorem 1.23e
provides cuspidal-support embedding in arbitrary rank and
characteristic. Lemma 1.20a and Proposition 1.4 give factor 1
for each higher-rank terminal block, while the rank-one scalar
Tate proof gives its exact character factor and nonnegative
exponent. Theorem 1.24 below proves strict positivity directly
for every higher-rank terminal block. Formula (1.27y) therefore
proves the universal nonnegative matrix exponent in Corollary
1.24c. This route uses no universal compact-induction construction.
Standard-factor, generic minimal-\(K_1\)-level and Artin conductor
identifications remain separate.

Further reading is [Goldfeld–Jacquet’s author notes, §2, Lemma 2.2, PDF page 9](https://www.math.columbia.edu/~goldfeld/LanglandsBookChapter.pdf). The full matrix-kernel and embedding arguments are proved above, with the positive-trace convention fixed in (1.27p)–(1.27r).

### Compact intertwining and finite inducing data

Let \(G=\mathrm{GL}_n(k)\), \(n\geq2\), \(Z=k^\times I_n\), and let \(\pi\)
be irreducible smooth admissible with compact-mod-center
coefficients. A real determinant twist makes its central
character unitary; the preceding compact-coefficient proof,
Corollary 1.4a, then constructs a compatible unitary realization.
A determinant twist shifts \(s\) and leaves the epsilon exponent
unchanged by direct substitution in the matrix integral.
We may therefore work in that unitary realization.

**Lemma 1.23f (orthogonal finite inducing subspace).** Suppose
there is an open \(H\supset Z\), compact modulo \(Z\), and a
nonzero finite-dimensional \(H\)-invariant subspace
\(W\subset V\) which is irreducible as an \(H\)-module, such that
\[
\langle\pi(g)w,w'\rangle=0
\quad(g\notin H,\ w,w'\in W).
\tag{1.28a}
\]
Then
\[
V\simeq\mathrm{c\!-\!Ind}_H^G(W).
\tag{1.28b}
\]
Consequently the earlier compact-induction theorem proves
\(a_\pi>0\).

**Proof.** For a function in the compact induction supported on
the left coset \(Hg\), let its value at \(g\) be \(w\). Send this
function to \(\pi(g^{-1})w\). The map does not depend on the
representative: replacing \(g\) by \(hg\) replaces the value
by \(\pi(h)w\), and
\(\pi((hg)^{-1})\pi(h)w=\pi(g^{-1})w\).
A compactly induced vector has finitely many such cosets, so
addition defines a linear map. Under right translation by \(x\)
the support coset is \(Hg x^{-1}\), with the same value \(w\);
its image is \(\pi(x)\pi(g^{-1})w\). Thus it is equivariant.

Different coset subspaces have orthogonal images. Indeed
for \(Hg_i\ne Hg_j\),
\[
\langle\pi(g_i^{-1})w_i,\pi(g_j^{-1})w_j\rangle
=\langle\pi(g_jg_i^{-1})w_i,w_j\rangle=0
\]
by (1.28a), since \(g_jg_i^{-1}\notin H\).
Each individual image preserves the norm of its value.
The norm square of a finite sum is therefore the sum of
the norm squares of its values. The map is injective.
Its image is a nonzero invariant algebraic subspace of
the irreducible smooth module \(V\), hence equals \(V\).
This proves (1.28b). The untwisted realization follows by
twisting the finite-dimensional inducing representation;
the subgroup is unchanged. \(\square\)

#### From compact intertwining to that realization

The extension step in a simple-type route can itself be
proved here, with a weaker hypothesis than an already
constructed inducing representation.

**Lemma 1.23g (compact intertwining criterion).** In the unitary
realization above suppose that a compact open \(J\subset G\)
has an irreducible smooth representation \(\tau\) occurring in
\(V|_J\). Define
\[
I_G(\tau)=
\left\{g\in G:
\operatorname{Hom}_{J\cap g^{-1}Jg}
\bigl(\tau(h),\tau(ghg^{-1})\bigr)\ne0\right\}.
\tag{1.28c}
\]
Suppose \(J\subset H\), \(Z\subset H\), where \(H\) is an open
subgroup compact modulo \(Z\), and \(I_G(\tau)\subset H\).
Then \(V\) is compactly induced from a finite-dimensional
irreducible representation of \(H\).

**Proof.** Let \(E\) be the full \(\tau\)-isotypic subspace of
\(V|_J\). It is finite-dimensional. Indeed, a smooth irreducible
representation of a compact group factors through a finite
quotient: the orbit of a vector is finite and spans its whole
irreducible module; intersecting the stabilizers of a finite
basis gives an open normal kernel \(J_0\). Thus
\(E\subset V^{J_0}\), which is finite-dimensional by
admissibility. Compact-group representations on that space
split into irreducibles by invariant orthogonal complements.
This also shows that \(E\) is a sum of finitely many copies of
\(\tau\). In the Hilbert completion \(E\) is closed; write
\(P_E\) for its orthogonal projection. The projection commutes
with \(J\), since the subspace and its orthogonal complement
are \(J\)-invariant.

For \(g\in G\), put \(A_g=P_E\pi(g)|_E\). If
\(h\in J\cap g^{-1}Jg\), then
\[
A_g\pi(h)|_E
=\pi(ghg^{-1})|_E A_g.                       \tag{1.28d}
\]
Decompose both domain and range into their copies of \(\tau\).
If \(A_g\ne0\), a nonzero coordinate of this operator is an
intertwiner in (1.28c). Hence \(A_g=0\) for \(g\notin H\), and
all coefficients between vectors of \(E\) vanish there.

The span \(W_0=\operatorname{span}\pi(H)E\) is
finite-dimensional and \(H\)-invariant. To see finiteness,
\(ZJ\) is an open subgroup of \(H\). The quotient
\(H/(ZJ)\) is discrete and is the image of the compact space
\(H/Z\), so has finitely many cosets \(h_i ZJ\).
The center acts by its scalar character and \(J\) preserves
\(E\), giving \(W_0=\sum_i\pi(h_i)E\).

For \(g\notin H\), \(h_i^{-1}gh_j\notin H\).
Unitarity and the preceding vanishing therefore give
\[
\langle\pi(g)\pi(h_j)e_j,\pi(h_i)e_i\rangle=0
\quad(e_i,e_j\in E).
\tag{1.28e}
\]
By linearity every coefficient between vectors of \(W_0\)
vanishes outside \(H\). Choose an irreducible \(H\)-subspace
\(W\subset W_0\): a nonzero invariant subspace of minimal
positive dimension exists, and is irreducible. It satisfies
all hypotheses of Lemma 1.23f. That lemma proves the claimed
compact induction, including injectivity and surjectivity,
by the explicit equivariant map and orthogonality proof. \(\square\)

Thus a sufficient remaining existence theorem is precise:
every abstract Jacquet-cuspidal \(\pi\) must contain some
compact-open type \((J,\tau)\) whose full intertwining set
is contained in an open subgroup compact modulo the center.
Lemma 1.23g supplies the ensuing finite inducing data and its
actual compact-induction realization. The existence of that
type is still unproved here.

Compact coefficient support does imply that the set of \(g\)
with \(P_E\pi(g)|_E\ne0\) is compact modulo \(Z\): use a
finite basis of \(E\) and its finitely many coefficients.
It does not imply that the full abstract intertwining set
\(I_G(\tau)\) is compact, because the reverse implication
in (1.28d) has not been proved and is not assumed.
Even compactness of the actual nonzero-compression set
does not place it in a compact subgroup, as the following
explicit example explains.

#### What compact support actually gives

For any chosen finite-dimensional \(W\subset V\), compact
support of its finitely many basis coefficients gives a compact
set \(C_W\subset G/Z\) outside which all
\(\langle\pi(g)w,w'\rangle\) vanish. This is a finite union
of support bounds. It does not show that \(C_W\) is contained
in a compact subgroup of \(G/Z\), or that one can choose
\(W,H\) satisfying (1.28a).

The distinction is mathematical. Even a compact subset of
\(\mathrm{PGL}_2(k)\) can generate a noncompact subgroup.
For example, let \(K=\mathrm{GL}_2(\mathcal O)\) and
\(a=\operatorname{diag}(\varpi,1)\). The images of \(K\) and
\(aKa^{-1}\) in \(G/Z\) are compact. Their generated
group is noncompact modulo \(Z\). To verify this, it contains
the two elementary matrices
\[
u(1)=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad
l(\varpi^{-1})=\begin{pmatrix}1&0\\\varpi^{-1}&1\end{pmatrix}.
\]
Put \(t=1+\varpi^{-1}\), of valuation \(-1\). The identity
\[
u(1)l(\varpi^{-1})=
l(\varpi^{-1}/t)\operatorname{diag}(t,t^{-1})u(1/t)
\]
has its other two factors in \(K\). Thus the generated
group contains every power of \(\operatorname{diag}(t,t^{-1})\).
The scalar-invariant entry-norm product on those powers
is \(q^{2b}\), \(b\geq0\), which is unbounded.
Replacing a compact support bound by its generated subgroup
is therefore not a valid completion of the realization proof.


The criteria just proved do not establish universal existence of compact inducing data. Theorem 1.24 proves the matrix exponent positive directly for every Jacquet-cuspidal irreducible of rank greater than one, making that existence theorem unnecessary for nonnegativity. A freely accessible account of the type-construction route is [Sécherre–Stevens, author arXiv preprint math/0607298, Theorems 4.1 and 5.21 and Corollary 5.22(i)](https://arxiv.org/pdf/math/0607298). Its simple-character and intertwining constructions are not proved here. The generic minimal-\(K_1\)-level and Artin conductor identifications also remain separate.

### Direct positivity of the cuspidal matrix epsilon exponent

This proof treats every nonarchimedean local field and every rank
\(n\geq2\). It uses the full matrix Fourier family and zero proper
Jacquet modules. It does not construct an inducing type or assume
a compact-induction realization.

Let \(k\) have integer ring \(\mathcal O\), uniformizer \(\varpi\),
residue cardinality \(q\), and valuation \(v(\varpi)=1\). Put
\[
G=\mathrm{GL}_n(k),\quad Z=k^\times I_n,\quad
K=\mathrm{GL}_n(\mathcal O),\quad j(g)=v(\det g),\quad X=q^{-s}.
\tag{1.29a}
\]
The character \(\psi\) has annihilator \(\mathcal O\), and the
matrix Fourier pairing is positive:
\[
\widehat\Phi(Y)=\int_{M_n(k)}\Phi(A)\psi(\operatorname{tr}(AY))\,dA.
\tag{1.29b}
\]
The additive measures give every integral coordinate lattice volume
1; they are self-dual. Multiplicative Haar measure gives \(K\) volume 1.
Write
\[
\alpha_n=\prod_{i=1}^n(1-q^{-i}),\qquad
dg=\alpha_n^{-1}|\det g|^{-n}\,d_{\rm add}g.
\tag{1.29c}
\]
Indeed additive matrix measure scaled by \(|\det g|^{-n}\) is
left and right invariant: multiplication by \(a\) has additive
Jacobian \(|\det a|^n\). The additive volume of \(K\) is
the fraction of invertible matrices over the residue field, namely
\(q^{-n^2}\prod_{i=0}^{n-1}(q^n-q^i)=\alpha_n\).
This proves (1.29c) with the exact constant.

Proposition 1.3, Proposition 1.4, Corollary 1.4a, Theorem 1.17 and Lemma 1.20a are the preceding matrix proofs used here.
They supply the entire rational matrix ideal, the scalar Fourier
equation, the Laurent-unit epsilon factor, and compact-mod-center
coefficient support from zero two-block Jacquet modules. In rank
greater than one that support also gives
\[
V^K=0,\qquad L_\pi=L_{\widetilde\pi}=1.
\tag{1.29d}
\]
We also use the complete proofs of the unique extended absolute
value and Newton factorization in
*Extensions of complete valued fields*, Theorems 1.2 and
5.1.
Those actual proofs explicitly include inseparable extensions and
polynomials in positive characteristic.

Fix an irreducible smooth admissible \(\pi\) with
\(V_{U_r}=0\) for every upper two-block radical \(U_r\),
\(1\leq r<n\). Let \(c(g)=\ell(\pi(g)v)\). Both \(c\) and
\(c^\vee(g)=c(g^{-1})\) have compact support modulo \(Z\).

#### Constant terms and compact determinant shells

If a locally constant function \(f\) has support in \(ZC\) for
compact \(C\subset G\), its support on every shell \(j(g)=j\)
is compact. In fact \(j(C)\) is a finite set, and
\(j(zc)=nv(z)+j(c)\) confines \(v(z)\) to finitely many
integers. The corresponding subsets \(\varpi^b\mathcal O^\times\)
are compact, so their products with \(C\) are compact.
In particular all integrals below on a fixed shell are absolutely
convergent.

**Lemma 1.24a (vanishing along the full unipotent fiber).**
For \(m=\operatorname{diag}(A,D)\), \(k_0\in K\), and
\[
u(B)=\begin{pmatrix}I_r&B\\0&I_t\end{pmatrix},
\quad B\in M_{r,t}(k),\quad r+t=n,
\]
both \(f=c\) and \(f=c^\vee\) satisfy
\[
\int_{M_{r,t}(k)}
f(k_0u(B)m k_0^{-1})\,dB=0.                  \tag{1.29e}
\]
Moreover
\[
\int_{j(g)=j}f(g)\,dg=0\qquad(j\in\mathbb Z).
\tag{1.29f}
\]

**Proof.** If a vector \(w\) has zero Jacquet class, write it as
a finite sum of \((\pi(u_i)-1)w_i\). Any sufficiently large compact
additive subgroup of \(U_r\) contains all \(u_i\); its probability
average kills every summand by translation invariance. Thus its
average kills \(w\).

The integrand in (1.29e) has compact support in \(B\). To check this
from compact support modulo \(Z\), conjugation by \(k_0\) preserves
compactness, so consider \(u(B)m=z h\) with \(h\) in a fixed compact
subset of \(G\). The fixed invertible diagonal blocks \(A,D\)
bound \(|z|\) below, using the bound on the entries of \(h\);
the fixed diagonal blocks of the inverse bound \(|z|\) above,
using the bound on the entries of \(h^{-1}\). The upper-right
block \(BD\) is then bounded, hence so is \(B\). Closedness of
the support and local compactness prove the assertion.

For \(c\), averaging the vector \(\pi(mk_0^{-1})v\) over a
compact subgroup containing this support gives zero, proving
(1.29e). For the inverse coefficient the integrand is
\[
c^\vee(k_0u(B)m k_0^{-1})
=\ell\bigl(\pi(k_0m^{-1})\pi(u(-B))\pi(k_0^{-1})v\bigr).
\]
Averaging the vector \(\pi(k_0^{-1})v\) proves the same result.
This does not require an unproved dual-Jacquet identity.

Finally use (1.29d). The shell is invariant under right \(K\)
translation, and its integral for \(c\) equals the integral
of the right \(K\)-average, which replaces \(v\) by \(e_Kv=0\).
For \(c^\vee\), use left \(K\)-translation instead; it likewise
replaces \(v\) by \(e_Kv=0\). Compact shell support and the
compact \(K\)-orbit of each smooth vector justify Fubini.
This proves (1.29f). \(\square\)

#### Splitting matrices according to root absolute values

Extend the absolute value uniquely to an algebraic closure of \(k\).
For \(g\in G\), call its characteristic polynomial *equal-valued*
if all its roots, counted with algebraic multiplicity, have the
same absolute value. In that case their common valuation is
\(j(g)/n\). Consequently
\[
j(g)\geq0,\quad g\text{ equal-valued}
\quad\Longrightarrow\quad \operatorname{tr}(g)\in\mathcal O.
\tag{1.29g}
\]
Indeed the trace is the sum of those roots, all of absolute value
at most 1, and belongs to \(k\).

If the roots are not equal-valued, let \(R\) be their largest
absolute value, let \(r\) be the number of roots of that value,
and put \(t=n-r>0\). Newton factorization, including polynomial
multiplicities, gives coprime monic polynomials in \(k[T]\):
\[
p_g=p_+p_-,\quad \deg p_+=r,\quad\deg p_-=t,
\quad |\text{roots of }p_+|=R>
|\text{each root of }p_-|.
\tag{1.29h}
\]
There is a unique canonical \(r\)-dimensional subspace
\[
W_g=\ker p_+(g).
\tag{1.29i}
\]
For completeness, Bézout for \(p_+,p_-\), together with
Cayley–Hamilton, splits \(k^n\) as
\(\ker p_+(g)\oplus\ker p_-(g)\).
The polynomial \(p_+\) kills the first summand and \(p_-\)
the second. Over a splitting field an operator is upper
triangularizable: choose an eigenvector, pass to its quotient,
and induct on the dimension. Applying the annihilating
polynomial to such a triangular form shows that its diagonal
roots belong to the roots of that polynomial. The two
summand characteristic polynomials therefore have disjoint
root sets and multiply to \(p_g\); all the multiplicities
of \(p_+\) must be in the first and all those of \(p_-\)
in the second. They are \(p_+,p_-\) respectively.
Their dimensions are therefore \(r,t\). The same reasoning
shows that any invariant subspace carrying all \(r\) of the
largest-value roots is killed by \(p_+(g)\), by Cayley–Hamilton
on that subspace, and equals (1.29i). This proves uniqueness.

The Cayley–Hamilton identity used here also follows directly
from
\((TI-g)\operatorname{adj}(TI-g)=p_g(T)I=
\operatorname{adj}(TI-g)(TI-g)\).
The two identities show that each coefficient matrix of
the adjugate commutes with \(g\); evaluating this polynomial
matrix identity at \(T=g\) gives \(p_g(g)=0\).
For the direct-sum assertion, a Bézout identity
\(a p_++b p_-=1\) writes each vector as the sum of its
\(b(g)p_-(g)\) image in \(\ker p_+(g)\) and its
\(a(g)p_+(g)\) image in \(\ker p_-(g)\); their intersection
is zero by the same identity.

The root-valuation multiset is locally constant as a function
of an invertible matrix. Here is the needed topological detail.
At a polynomial with nonzero leading and constant coefficients,
the finitely many coefficient points defining its Newton polygon
have fixed finite heights. A sufficiently small coefficient change
keeps each nonzero coefficient's valuation fixed and puts every
formerly zero coefficient strictly above that polygon.
The polygon is unchanged. The preceding Newton theorem identifies
its slopes and lengths with the root valuations and multiplicities.
Characteristic coefficients are polynomial functions of matrix
entries, so the assertion follows.

Write \(\Omega_r\) for matrices whose largest-value group has
dimension \(r<n\). The \(\Omega_r\) are disjoint open sets
covering the matrices that are not equal-valued.
Define the open block domain
\[
\mathcal D_r=
\{(A,D)\in\mathrm{GL}_r(k)\times\mathrm{GL}_t(k):
\text{all roots of }A\text{ have one absolute value,
larger than every root absolute value of }D\}.
\tag{1.29j}
\]

We give finite integral charts for \(W_g\). Any \(r\)-subspace
\(W\subset k^n\) has a saturated lattice
\(\Lambda=W\cap\mathcal O^n\), and a basis of \(\Lambda\)
extends to an integral basis of \(\mathcal O^n\).
An explicit proof is to scale a nonzero vector in \(W\)
until one coordinate is a unit, use integral elementary
coordinate changes to send it to \(e_n\), and split
\[
W=k e_n\oplus(W\cap k^{n-1}),\quad
\Lambda=\mathcal O e_n\oplus(W\cap k^{n-1}\cap\mathcal O^{n-1}).
\]
Induction supplies the asserted integral basis.

Thus \(\Lambda/\varpi\Lambda\) determines an \(r\)-plane
\(\overline W\) in the residue-field vector space. For each
of the finitely many such planes choose \(k_{\overline W}\in K\)
carrying the first coordinate \(r\)-plane to it on reduction.
Every \(W\) with that reduction has a unique form
\[
W=k_{\overline W}
\{(x,Bx):x\in k^r\},\qquad
B\in\varpi M_{t,r}(\mathcal O).
\tag{1.29k}
\]
Indeed after \(k_{\overline W}^{-1}\), the projection of an
integral basis of \(\Lambda\) to its first \(r\) coordinates
is invertible modulo \(\varpi\), hence belongs to
\(\mathrm{GL}_r(\mathcal O)\). Normalizing that projection
to the identity makes its lower block the unique \(B\),
which is zero modulo \(\varpi\).

Put \(l(B)=\left(\begin{smallmatrix}I_r&0\\B&I_t\end{smallmatrix}\right)\)
and \(k_B=k_{\overline W}l(B)\in K\). The map
\[
F_{\overline W}(B,A,C,D)
=k_B\begin{pmatrix}A&C\\0&D\end{pmatrix}k_B^{-1},
\quad B\in\varpi M_{t,r}(\mathcal O),\quad
(A,D)\in\mathcal D_r,\quad C\in M_{r,t}(k),
\tag{1.29l}
\]
is a bijection onto the part of \(\Omega_r\) with
\(\overline{W_g}=\overline W\). Its canonical subspace is
exactly \(k_B k^r\); uniqueness in (1.29i) determines \(B\),
and reading the conjugated blocks determines \(A,C,D\).
Conversely any \(g\) in that part preserves its canonical
subspace, so this block reading gives (1.29l) and (1.29j).
The charts are disjoint; no Weyl multiplicity or finite
representative factor is omitted.

#### The measure calculation, including its analytic justification

Define the Sylvester map on the lower rectangular block:
\[
S_{A,D}:M_{t,r}(k)\longrightarrow M_{t,r}(k),
\qquad H\longmapsto HA-DH.
\tag{1.29m}
\]
It is invertible on \(\mathcal D_r\). If \(HA=DH\), then
\(Hp_A(A)=p_A(D)H=0\), where \(p_A\) is the characteristic
polynomial of \(A\). Its coprimality with the characteristic
polynomial of \(D\) makes \(p_A(D)\) invertible by Bézout.
Hence \(H=0\), which proves invertibility in finite dimension.

The exact chart measure is
\[
dg=\alpha_n^{-1}|\det A\,\det D|^{-n}
|\det S_{A,D}|\,dB\,d_{\rm add}A\,dC\,d_{\rm add}D.
\tag{1.29n}
\]
Most importantly its density is independent of \(B,C\).
To calculate it, discard the fixed integral conjugation
\(k_{\overline W}\), whose additive Jacobian is 1.
Conjugation by \(l(B)\) also has additive Jacobian 1.
Since \(l(B)^{-1}dl(B)=
\left(\begin{smallmatrix}0&0\\dB&0\end{smallmatrix}\right)\),
the differential of (1.29l), after that conjugation, is
\[
\begin{pmatrix}
dA-C\,dB&dC\\
dB\,A-D\,dB&dD+dB\,C
\end{pmatrix}.                                  \tag{1.29o}
\]
As a linear map in \(dA,dC,dD,dB\), its determinant has
absolute value \(|\det S_{A,D}|\): the lower output is
\(S_{A,D}(dB)\), and the other three outputs have identity
coefficients on \(dA,dC,dD\). Finally
\(\det F_{\overline W}=\det A\,\det D\), and (1.29c) gives (1.29n).

Here the change of variables is valid in every characteristic.
We include the finite-dimensional analytic fact being used,
instead of importing it from a manual. If a polynomial map
\(F:k^d\to k^d\) has invertible derivative \(L\) at \(x_0\),
write
\[
L^{-1}(F(x_0+h)-F(x_0))=h+R(h).
\]
The polynomial \(R\) has no constant or linear terms.
On a sufficiently small ball \(\varpi^N\mathcal O^d\),
its finitely many coefficients and the telescoping formula
for a difference of monomials give
\[
\|R(h)-R(h')\|\leq q^{-1}\|h-h'\|,
\qquad R(\varpi^N\mathcal O^d)\subset
\varpi^{N+1}\mathcal O^d.      \tag{1.29p}
\]
For \(y\) in this ball, \(h\mapsto y-R(h)\) is a contraction
of that complete ball. Successive iterates are Cauchy, with
errors bounded by the geometric powers \(q^{-i}\); their
limit is its unique fixed point. This proves a bijection
of the ball under \(h\mapsto h+R(h)\), and proves continuity
of its inverse. The same argument on every contained
coset ball of radius \(q^{-a}\), \(a\geq N\), sends it onto
the coset ball of the same radius around its image.
It therefore preserves additive Haar measure: these coset
balls form a basis, and locally constant compact tests
are finite linear combinations of their indicators.
Translation and the linear map \(L\) then supply the measure
factor \(|\det L|\). The latter factor follows from integral
row and column elimination and diagonal scalings.

The derivative determinant remains of that same absolute
value on the sufficiently small ball. Thus this is the
Jacobian change of variables there. A nonarchimedean local
field has a countable basis of such coordinate balls:
each quotient \(k/\varpi^a\mathcal O\) is countable.
Partitioning an open domain into countably many sufficiently
small disjoint balls proves the formula globally for
nonnegative measurable functions, then for integrable
functions. On (1.29l) its derivative is invertible everywhere,
and the previously proved bijection removes all multiplicities.
This proves (1.29n) and justifies its use for all the integrals
below, without a separability or residual-characteristic restriction.

#### The nonnegative determinant Gauss integrals vanish

**Lemma 1.24b.** For \(f=c\) or \(f=c^\vee\),
\[
\int_{j(g)=j}\psi(\operatorname{tr}g)f(g)\,dg=0
\qquad(j\geq0).         \tag{1.29q}
\]

**Proof.** By (1.29f) it suffices to integrate
\[
h(g)f(g),\qquad h(g)=\psi(\operatorname{tr}g)-1.
\]
On the equal-valued matrices in this shell, (1.29g) and the
conductor of \(\psi\) give \(h=0\). On each remaining
\(\Omega_r\), use the finitely many disjoint charts (1.29l).
The determinant and the trace are
\(\det A\,\det D\) and \(\operatorname{tr}A+\operatorname{tr}D\).
The shell condition, the root condition (1.29j), \(h\), and
the measure density (1.29n) are consequently all independent
of \(C\). The inner integral is
\[
\int_C f\!\left(k_B
\begin{pmatrix}A&C\\0&D\end{pmatrix}
k_B^{-1}\right)\,dC
=|\det D|^r\int_Q f(k_Bu(Q)m k_B^{-1})\,dQ=0,       \tag{1.29r}
\]
by \(C=QD\) and Lemma 1.24a. This proves the desired vanishing
on each chart. Compact shell support, boundedness of \(h\),
and (1.29n) justify the absolute Fubini rearrangement.
Summing over the finite charts and \(1\leq r<n\) proves
(1.29q). \(\square\)

The subtraction of 1 is essential: its shell integral is zero
by the compact \(K\)-average, while the difference vanishes
exactly where the trace is known to be integral. The argument
does not identify a coefficient with a character distribution
and does not infer scalar operator vanishing from a trace limit.

#### The Fourier equation now forces strict positivity

**Theorem 1.24 (every Jacquet-cuspidal block).** If \(n\geq2\)
and \(\pi\) is irreducible smooth admissible with all proper
two-block Jacquet modules zero, then its conductor-zero,
positive-trace matrix epsilon factor has
\[
\epsilon_\pi(s,\psi)=c_\pi X^{a_\pi},\qquad
c_\pi\ne0,\qquad a_\pi>0.                          \tag{1.29s}
\]
This holds over every nonarchimedean local field.

**Proof.** The scalar Fourier equation and the Laurent-unit
argument have already proved \(a_\pi\in\mathbb Z\).
Choose \(v,\ell\) with \(\ell(v)=1\), and let \(J_N=
1+\varpi^N M_n(\mathcal O)\), \(N\geq1\), fix \(v,\ell\).
Every deeper \(J_N\) does too. The actual test
\[
\Phi_N=\operatorname{vol}_G(J_N)^{-1}1_{J_N}
\]
has \(Z_\pi(s,\Phi_N,c)=1\). Additive lattice orthogonality
and (1.29c) give exactly
\[
\widehat\Phi_N(Y)=
\alpha_n\psi(\operatorname{tr}Y)\,
1_{\varpi^{-N}M_n(\mathcal O)}(Y).       \tag{1.29t}
\]
There is no \(N\)-dependent scalar: the additive and
multiplicative volumes of \(J_N\) have ratio \(\alpha_n\).

By (1.29d) gamma equals epsilon. Apply the whole-family
Fourier equation to this test. Its exact Laurent expansion is
\[
c_\pi X^{a_\pi}
=\alpha_n\sum_{j\in\mathbb Z}
q^{-j(n+1)/2}X^{-j}
\int_{\substack{j(g)=j\\
g\in\varpi^{-N}M_n(\mathcal O)}}
\psi(\operatorname{tr}g)c^\vee(g)\,dg.  \tag{1.29u}
\]
For clarity this sum is finite. Its lower bound is
\(j\geq-nN\), by the determinant expansion. For large
positive \(j\), compact-mod-center support of \(c^\vee\)
places its entire shell support in \(M_n(\mathcal O)\):
write \(g=z h\), \(h\) in a fixed compact subset of \(G\);
the finite values of \(j(h)\) force \(v(z)\to+\infty\)
uniformly as \(j\to+\infty\). Its entries therefore tend
uniformly to zero. The ball indicator is then 1 and
\(\psi(\operatorname{tr}g)=1\); (1.29f) makes that shell
coefficient zero. Thus (1.29u) is a genuine finite Laurent
identity, obtained first in a convergence half-plane and
then as the proved rational continuation.

Suppose \(a_\pi\leq0\), and put \(j_0=-a_\pi\geq0\).
The support of \(c^\vee\) on that one shell is compact.
Choose \(N\) sufficiently large that its support lies in
\(\varpi^{-N}M_n(\mathcal O)\), retaining the fixed-vector
condition. The coefficient of \(X^{a_\pi}=X^{-j_0}\)
on the right of (1.29u) is then
\[
\alpha_n q^{-j_0(n+1)/2}
\int_{j(g)=j_0}\psi(\operatorname{tr}g)c^\vee(g)\,dg=0
\]
by Lemma 1.24b. On the left it is the nonzero number \(c_\pi\).
This contradiction proves \(a_\pi>0\). \(\square\)

Only one shell needs eventual containment. No uniform support
bound over every vector, coefficient, test or determinant shell
is assumed in this final extraction.

#### Every irreducible representation: nonnegative exponent and factor degree

**Corollary 1.24c (universal nonnegative matrix exponent).** Every irreducible smooth admissible \(\sigma\) embeds in normalized induction from terminal Jacquet-cuspidal blocks \(\rho_i\), by Theorem 1.23e. Its exact polynomial correction (1.27x)–(1.27y) gives
\[
a_\sigma=\sum_i a_{\rho_i}+\deg R,\qquad R(0)=1,
\quad R\in\mathbb C[X].   \tag{1.29v}
\]
Each block of rank greater than one has positive exponent by
Theorem 1.24. Each rank-one block is a character and has
nonnegative scalar Tate exponent by Proposition 1.16 in
rank one. Since \(\deg R\geq0\), this proves
\[
a_\sigma\geq0
\]
for every smooth irreducible admissible \(\mathrm{GL}_n(k)\),
in all ranks and all nonarchimedean characteristics. This proves the corollary. \(\square\)

This closes nonnegativity of the *matrix epsilon exponent*.
It does not identify it with a generic minimal \(K_1\)-level
or an Artin conductor, and does not assert existence of
compact inducing data for every cuspidal representation.
Those separate statements are unnecessary for the proof here.


**Corollary 1.24d (degree bound and exponent zero).** Write
\(L_\sigma(s)=P_\sigma(q^{-s})^{-1}\), \(P_\sigma(0)=1\).
For a cuspidal-support embedding as in Theorem 1.23e, let
\(\chi_1,\ldots,\chi_h\) be its unramified rank-one blocks,
listed with multiplicity. Then
\[
P_\sigma(X)R(X)=\prod_{i=1}^{h}(1-\chi_i(\varpi)X),
\qquad \deg P_\sigma\leq h\leq n.                 \tag{1.29w}
\]
In particular \(L_\sigma=1\) if there are no such blocks.
If \(a_\sigma=0\), every block has rank one and is unramified,
\(h=n\), \(R=1\), and
\[
P_\sigma(X)=\prod_{i=1}^{n}(1-\chi_i(\varpi)X).
\tag{1.29x}
\]

**Proof.** Lemma 1.20a and Proposition 1.4 give factor 1 for
each cuspidal block of higher rank. Proposition 1.16 in rank
one gives factor 1 for a ramified character and
\((1-\chi(\varpi)X)^{-1}\) for an unramified character.
Substitution in (1.27x), followed by multiplication by
\(P_\sigma\prod_i(1-\chi_i(\varpi)X)\), proves (1.29w).
Degrees add in a product of nonzero polynomials, so its degree
is \(h\), proving the bound. If \(h=0\), both polynomials have
constant term 1 and their product is 1; hence both equal 1.

When \(a_\sigma=0\), (1.29v) is a sum of nonnegative integers.
Every summand is therefore zero. Theorem 1.24 excludes a
higher-rank block. The exact rank-one conductor in Proposition
1.16 makes every remaining character unramified. Thus \(h=n\).
Also \(\deg R=0\) and \(R(0)=1\), so \(R=1\), proving
(1.29x). \(\square\)

This is a conclusion about the cuspidal-support embedding and
the matrix factor. A proof that \(\sigma\) itself has a
\(K\)-fixed vector would require an additional argument.
The algebraic compact-induction criteria in Lemmas 1.23f–1.23g
retain \(n\geq2\) for strict positivity: an unramified rank-one
character has exponent zero.

Further reading is [Getz–Hahn, 22 April 2022 author draft,
§8.7, Proposition 8.7.1, printed pages 207–208](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf).
The finite Newton charts, Sylvester Jacobian and full-fiber
cancellation above provide the proof, including matrices that
are not semisimple and fields of positive characteristic.

### Matrix tests at a real or complex place

For \(F=\mathbb R\) use \(|x|_F=|x|\); for \(F=\mathbb C\) use
\(|z|_F=z\bar z\). Put \(G=\mathrm{GL}_n(F)\),
\(\nu(g)=|\det g|_F\), and \(u_s=s+(n-1)/2\). On the additive
matrix space use ordinary real Lebesgue measure, or the product
of \(2\,d\Re z\,d\Im z\) at a complex place. Multiplicative
Haar measure is \(dg=C_F\nu(g)^{-n}dX\), where \(C_F>0\)
records the chosen normalization. This formula follows from the
left and right additive Jacobians \(|\det h|_F^n\).

These arguments use smooth matrix coefficients of a specified
smooth realization. Wherever differentiation of a zeta integral
is used, the coefficients and the indicated Lie derivatives are
assumed to have polynomial growth. No algebraic-to-smooth or
Hilbert-to-smooth comparison theorem is inferred here.
Polynomial growth here means a bound by
\(C(1+\|g\|+\|g^{-1}\|)^N\), with a possibly different \(C,N\)
for each of the finitely many derivatives used in an argument.

#### 1. Polynomial multiplication and tests supported on the group

**Proposition 1.5 (polynomial-module closure).** Suppose a matrix coefficient \(c\) and its
Lie derivatives have polynomial growth. In the initial domain
of convergence, the complex span of its matrix zeta integrals,
allowing all coefficient vectors and Schwartz tests, is stable
under multiplication by \(s\). The same is true if the tests
are Gaussian times polynomials and the coefficient vectors are
bi-\(K\)-finite, where \(K=O(n)\) or \(U(n)\).

Choose a real Lie algebra element \(A\) with
\[
\left.\frac{d}{dt}\log\nu(e^{tA})\right|_{t=0}=1:
\quad A=\operatorname{diag}(1,0,\ldots,0)\ \ (F=\mathbb R),
\quad A=\operatorname{diag}(1/2,0,\ldots,0)\ \ (F=\mathbb C).
\]
For functions on \(G\) or on the matrix space let
\(R_Af(g)=\left.\frac d{dt}f(ge^{tA})\right|_{0}\).
Right invariance of Haar measure and the substitution
\(g\mapsto ge^{-tA}\) give
\[
Z(s,R_A\Phi,c)+Z(s,\Phi,R_Ac)
=-\left(s+\frac{n-1}{2}\right)Z(s,\Phi,c).              \tag{1.8a}
\]
Polynomial growth of the coefficients and their derivatives,
together with the Schwartz bounds, justifies differentiation
in a sufficiently far right half-plane. Near singular matrices,
the same determinant weight and polynomial bound in \(g^{-1}\)
give a common integrable majorant after increasing \(\Re s\);
for example Cartan polar coordinates, or the column Gram–Schmidt
coordinates below, bound powers of \(g^{-1}\) by a power of
\(\nu(g)^{-1}\) times a polynomial in the matrix entries.
More explicitly, the adjugate identity gives
\(\|g^{-1}\|\leq C\|g\|^{n-1}|\det g|_{\mathrm{ordinary}}^{-1}\);
the Gram–Schmidt integral of a sufficiently large positive
determinant power is finite. Both estimates are uniform when
\(t\) ranges over a compact interval.

Equation (1.8a) expresses \(sZ\) as a sum of three actual integrals.
Iterating proves the assertion for any polynomial in \(s\).
Differentiating a polynomial times the basic Gaussian again
gives a polynomial times that Gaussian. A Lie derivative of a
\(K\)-finite vector remains \(K\)-finite: if its original
\(K\)-span is \(W\), the span after differentiation lies in
the image of the finite-dimensional space
\(\operatorname{span}\{\operatorname{Ad}(k)A:k\in K\}\otimes W\).
Apply the same observation to the dual vector. \(\square\)

**Proposition 1.6 (an entire test nonzero at a prescribed parameter).** For every \(s_0\in\mathbb C\) and a coefficient
with \(c(1)=1\), there is a Schwartz test supported inside \(G\)
for which \(Z(s_0,\Phi,c)\ne0\). Integrals with such compact
support are entire in \(s\).

Take a nonzero nonnegative smooth function \(\eta\) supported in
a sufficiently small compact neighborhood of 1 in \(G\), and set
\[
\Phi(g)=\eta(g)\overline{c(g)}\,\nu(g)^{-s_0-(n-1)/2}.
\]
Extend it by zero to the matrix space. Its support stays away
from the singular locus, so the extension is smooth and Schwartz.
Then
\[
Z(s_0,\Phi,c)=\int_G\eta(g)|c(g)|^2\,dg>0.
\]
On a compact subset of \(G\), the real function \(\log\nu(g)\)
is bounded. This bounds every parameter derivative uniformly
on compact sets of \(s\), proving entireness. \(\square\)

In particular, **if** a common meromorphic generator \(L\) has
already been shown to divide every zeta integral with entire
quotient, Proposition 1.6 proves that it has no zeros. The
entire-quotient assertion is indispensable: nonvanishing of a
compact-support integral does not prove that division theorem.

#### 2. The Gaussian ideal for determinant characters in every rank

Let \(\pi(g)=\chi(\det g)\), with
\[
\chi(x)=\operatorname{sgn}(x)^e|x|^a,\quad e\in\{0,1\},
\quad F=\mathbb R;
\qquad
\chi(z)=(z/|z|)^k|z|_F^a,\quad k\in\mathbb Z,
\quad F=\mathbb C.
\]
All matrix coefficients are scalar multiples of this character.
These formulas cover every smooth character of \(F^\times\):
on positive radii the character, written in the logarithmic
coordinate, satisfies \(h'(t)=h'(0)h(t)\) and is an exponential.
Over \(\mathbb R\) its value at \(-1\) has square one. Over
\(\mathbb C\), the same differential equation on the angular
coordinate and period \(2\pi\) force the exponent to be \(ik\)
with \(k\in\mathbb Z\); the radial exponent is written as \(2a\)
because the normalized complex norm is the squared radius.
Let \(\mathcal S_0\) be the polynomials times
\(e^{-\pi\operatorname{tr}(XX^t)}\) over \(\mathbb R\), or the
polynomials in \(X,\overline X\) times
\(e^{-2\pi\operatorname{tr}(XX^*)}\) over \(\mathbb C\).

**Proposition 1.7 (the Gaussian ideal for determinant characters).** The span of the matrix zeta integrals with
tests in \(\mathcal S_0\) is exactly \(L_\chi(s)\mathbb C[s]\),
where a constant normalization independent of \(s\) is permitted
and
\[
L_\chi(s)=
\begin{cases}
\displaystyle\prod_{j=1}^n
\Gamma_{\mathbb R}\!\left(s+a+e+j-\frac{n+1}{2}\right),
&F=\mathbb R,\\[4pt]
\displaystyle\prod_{j=1}^n
\Gamma_{\mathbb C}\!\left(s+a+\frac{|k|}{2}
+j-\frac{n+1}{2}\right),
&F=\mathbb C.
\end{cases}                                                \tag{1.8b}
\]
Here
\(\Gamma_{\mathbb R}(w)=\pi^{-w/2}\Gamma(w/2)\) and
\(\Gamma_{\mathbb C}(w)=2(2\pi)^{-w}\Gamma(w)\).
This is an assertion about every Gaussian-polynomial test,
not just a calculation of one test.

**Proof: averaging the polynomial.**
Replace a test by
\[
\Phi^\chi(X)=\int_{K\times K}\chi(\det k_1)\chi(\det k_2)
\Phi(k_1Xk_2)\,dk_1\,dk_2.             \tag{1.8c}
\]
The measures here are probability measures. Change of variables
in the absolutely convergent integral shows that its zeta
integral is unchanged. The basic Gaussian is bi-\(K\)-invariant;
averaging its polynomial factor gives another polynomial of
the same degree bound. Write this factor as \(P_\chi\). It has
the transformation law
\[
P_\chi(h_1Xh_2)=
\chi(\det h_1\det h_2)^{-1}P_\chi(X)
\quad(h_1,h_2\in K).                                 \tag{1.8d}
\]

Over \(\mathbb R\), restrict to diagonal matrices with entries
\(x_1,\ldots,x_n\). Changing the sign of an individual entry
shows that its polynomial degree in that entry has parity \(e\).
Conjugating by permutation matrices shows that
\[
P_\chi(\operatorname{diag}(x_j))
=(x_1\cdots x_n)^e Q(x_1^2,\ldots,x_n^2)
\]
with \(Q\) symmetric. Over \(\mathbb C\), restrict to diagonal
entries \(z_j\). An independent unitary phase in entry \(j\)
shows that every surviving monomial has
\(\deg z_j-\deg\bar z_j=-k\). Thus its restriction is
\(\prod_j\bar z_j^k Q(|z_1|^2,\ldots,|z_n|^2)\) if \(k\geq0\),
and \(\prod_jz_j^{-k}Q(|z_1|^2,\ldots,|z_n|^2)\) if \(k<0\),
again with \(Q\) symmetric.

Every symmetric polynomial in \(n\) variables is a polynomial
in their elementary symmetric functions. An elementary proof
subtracts the product of elementary symmetric functions with
the same highest lexicographic monomial, and repeats; each
subtraction decreases that monomial and terminates at bounded
degree. Apply this to \(Q\). Its value on the squared singular
values is therefore a polynomial in the characteristic
coefficients of \(X^*X\), or \(X^tX\). These coefficients
are themselves polynomials in the matrix entries.

Every matrix admits a real or complex singular-value
decomposition. To obtain it, diagonalize the positive symmetric
or Hermitian matrix \(X^*X\): the maximum of its quadratic form
on the unit sphere gives an eigenvector, its orthogonal
complement is invariant, and induction gives an orthonormal
eigenbasis. The positive-eigenvalue columns of \(X\), divided
by their singular values, are orthonormal; complete them to an
orthonormal basis. This gives the desired two compact factors,
also for singular matrices. The transformation law (1.8d)
therefore identifies the full polynomial as
\[
P_\chi(X)=
\begin{cases}
(\det X)^e Q_{\mathrm{Gram}}(X^tX),&F=\mathbb R,\\
(\overline{\det X})^k Q_{\mathrm{Gram}}(X^*X),&F=\mathbb C,\ k\geq0,\\
(\det X)^{-k}Q_{\mathrm{Gram}}(X^*X),&F=\mathbb C,\ k<0.
\end{cases}                                                \tag{1.8e}
\]
The notation \(Q_{\mathrm{Gram}}\) means a polynomial in those
characteristic coefficients. None of the displayed powers
has a negative exponent.

**Proof: all the Gaussian moments.**
The real Gaussian matrix measure and the complex Gaussian
matrix measure just specified both have total mass one:
the one-entry integrals are respectively
\(\int_{\mathbb R}e^{-\pi x^2}dx=1\) and
\(\int_{\mathbb C}e^{-2\pi|z|^2}2\,d\Re z\,d\Im z=1\).
Perform Gram–Schmidt on the independent Gaussian columns and
write \(X=UR\), with \(R\) upper triangular and positive real
diagonal entries \(r_1,\ldots,r_n\). The singular set has
measure zero: successively, a Gaussian column lies in the
span of preceding columns with probability zero, since that
is a proper linear subspace.

Conditional on the preceding columns, the next Gaussian
column in any orthonormal frame has the same product Gaussian
law. Its coordinates along those columns and its orthogonal
component are independent, and their distributions do not
depend on the preceding columns. Thus the upper entries of
\(R\) are independent one-entry Gaussians, and \(r_j\) is
the length of a Gaussian vector in dimension \(d=n-j+1\).
The variables so obtained are independent. Radial integration
shows that \(r_j^2\) has gamma density with shape \(d/2\)
and rate \(\pi\) in the real case, or shape \(d\) and rate
\(2\pi\) in the complex case. The normalizing constants follow
by dividing the radial integral by its value at exponent zero.
This uses only the one-dimensional gamma integral.

Consequently, for the test in (1.8e) with \(Q_{\mathrm{Gram}}=1\),
put
\[
\kappa=s+a+e-\frac{n+1}{2}\quad(F=\mathbb R),\qquad
\beta=s+a+\frac{|k|}{2}-\frac{n+1}{2}\quad(F=\mathbb C).
\]
The sign or angular character cancels the determinant
polynomial. Including the factor \(\nu(g)^{-n}\) in Haar
measure, its integral is
\[
\begin{split}
Z_{\mathrm{base}}(s)
&=C_{\mathbb R}\pi^{-n\kappa/2}
\prod_{j=1}^n\frac{\Gamma((\kappa+j)/2)}{\Gamma(j/2)}
&&(F=\mathbb R),\\
Z_{\mathrm{base}}(s)
&=C_{\mathbb C}(2\pi)^{-n\beta}
\prod_{j=1}^n\frac{\Gamma(\beta+j)}{\Gamma(j)}
&&(F=\mathbb C).
\end{split}                                                \tag{1.8f}
\]
Initially these formulas hold respectively for
\(\Re\kappa>-1\) and \(\Re\beta>-1\).
Their ratios to (1.8b) are the positive constants
\[
C_{\mathbb R}
\frac{\pi^{\,n(n+1)/4}}{\prod_{j=1}^n\Gamma(j/2)},
\qquad
C_{\mathbb C}
\frac{(2\pi)^{\,n(n+1)/2}}{2^n\prod_{j=1}^n\Gamma(j)}.
\tag{1.8g}
\]

For a general \(Q_{\mathrm{Gram}}\), substitute \(X^*X=R^*R\)
and integrate the polynomial in the strictly upper entries
of \(R\). Their Gaussian moments are finite, so the result is
a polynomial in the \(r_j\). It is a polynomial in the
squares \(r_j^2\): in the real case, changing the sign of row
\(j\) of \(R\) preserves \(R^tR\) and the Gaussian law of
all its upper entries; in the complex case the analogous
row phase preserves \(R^*R\) and forces equal holomorphic
and antiholomorphic degrees in its diagonal variable.
It is thus a finite sum of monomials \(\prod_jr_j^{2m_j}\),
with \(m_j\geq0\).

The ratio of each corresponding real radial moment to the
base moment is
\(\pi^{-m_j}((\kappa+d)/2)_{m_j}\); the complex ratio is
\((2\pi)^{-m_j}(\beta+d)_{m_j}\). The rising factorial
\((w)_m=w(w+1)\cdots(w+m-1)\) follows by integrating the
gamma integral by parts \(m\) times. These ratios are
polynomials in \(s\). Hence every Gaussian-polynomial
integral is a polynomial multiple of (1.8f), and continues
meromorphically by that formula.
The base test attains a nonzero constant times (1.8b).
Proposition 1.5 then supplies every polynomial multiple.
This proves the full asserted \(\mathbb C[s]\)-ideal. \(\square\)

The one-dimensional gamma integral, its recurrence and its
absence of zeros are proved in the earlier
*Tate's local theory at the infinite places*, the
section “Mellin continuation without a functional equation”
and Proposition 8.2. In particular (1.8b) is zero-free, its
reciprocal is entire, and it has finitely many poles in any
bounded vertical strip. Indeed the gamma poles form decreasing
real arithmetic progressions after a fixed complex shift.
The polynomial Gaussian calculation (1.8f) will now be extended to every Schwartz test in Theorem 1.18.

#### 3. The full Schwartz family for determinant characters

Let \(F=\mathbb R\) or \(\mathbb C\), \(G=GL_n(F)\), and
\(\nu(g)=|\det g|_F\). The complex absolute value is squared:
\(|z|_F=z\bar z\). Use additive measure \(dX\) equal to real Lebesgue measure, or the product of \(2\,d\Re z\,d\Im z\) on complex entries, and write
\[
dg=C_F\nu(g)^{-n}dX,\qquad C_F>0.
\]
Let
\[
\chi(x)=\operatorname{sgn}(x)^e|x|^a
\quad(F=\mathbb R,\ e=0,1),\qquad
\chi(z)=(z/|z|)^k|z|_F^a
\quad(F=\mathbb C,\ k\in\mathbb Z),
\]
where \(a\in\mathbb C\), and put \(\pi=\chi\circ\det\). Set
\[
Z_\chi(s,\Phi)=\int_G\Phi(g)\chi(\det g)\nu(g)^{s+(n-1)/2}\,dg.
\]
The factor already obtained from all polynomial Gaussian tests is
\[
L_\chi(s)=
\begin{cases}
\displaystyle\prod_{j=1}^n
\Gamma_{\mathbb R}\!\left(s+a+e+j-\frac{n+1}{2}\right),&F=\mathbb R,\\[3pt]
\displaystyle\prod_{j=1}^n
\Gamma_{\mathbb C}\!\left(s+a+\frac{|k|}{2}+j-\frac{n+1}{2}\right),&F=\mathbb C.
\end{cases}                                                   \tag{1.22a}
\]
Here \(\Gamma_{\mathbb R}(w)=\pi^{-w/2}\Gamma(w/2)\) and
\(\Gamma_{\mathbb C}(w)=2(2\pi)^{-w}\Gamma(w)\).

**Theorem 1.18 (the full Schwartz family for determinant characters).** In every rank, \(Z_\chi(s,\Phi)\) converges absolutely for every \(\Phi\in\mathcal S(M_n(F))\) when
\(\Re(s+a)>(n-1)/2\). It continues meromorphically, and
\[
\mathcal D_\chi(s)(\Phi)=Z_\chi(s,\Phi)/L_\chi(s)                 \tag{1.22b}
\]
is an entire family of tempered distributions. More precisely, for every compact set \(B\subset\mathbb C\) there is a Schwartz seminorm \(p_B\) such that
\[
\sup_{s\in B}|\mathcal D_\chi(s)(\Phi)|\le p_B(\Phi);             \tag{1.22c}
\]
the same assertion holds for every parameter derivative.

Use the programme characters
\[
\psi_{\mathbb R}(x)=e^{-2\pi ix},\qquad
\psi_{\mathbb C}(z)=e^{-2\pi i(z+\bar z)}
\]
and the positive trace argument in the Fourier kernel:
\[
\widehat\Phi(Y)=\int\Phi(X)\psi_F(\operatorname{tr}(XY))\,dX.
\]
Then, for every Schwartz test,
\[
\frac{Z_{\chi^{-1}}(1-s,\widehat\Phi)}{L_{\chi^{-1}}(1-s)}
=\epsilon_\chi\,
\frac{Z_\chi(s,\Phi)}{L_\chi(s)},\qquad
\epsilon_\chi=
\begin{cases}
(-i)^{ne},&F=\mathbb R,\\
(-i)^{n|k|},&F=\mathbb C.
\end{cases}                                                   \tag{1.22d}
\]
All matrix coefficients of this one-dimensional representation are scalar multiples of the coefficient used here, so the assertion includes the whole coefficient family.

The polynomial Gaussian family still has exactly the ideal
\(L_\chi(s)\mathbb C[s]\), with an attaining test; that is the earlier Proposition 1.7, whose proof applies to this same normalization. The present theorem supplies division and the Fourier equation on the full Schwartz space.

##### 1. Normalized Mellin distributions with seminorm bounds

For an even Schwartz function \(f\) on \(\mathbb R\), initially define
\[
\mathcal M_w(f)=\frac1{\Gamma(w/2)}
\int_0^\infty f(r)r^{w-1}\,dr,\qquad\Re w>0.
\]
This is an entire family of continuous functionals on the even Schwartz space, locally bounded by a finite number of its seminorms.

Here is the complete continuation argument. Choose an even compactly supported smooth cutoff \(\rho\), equal to one near zero. For an integer \(N\ge1\), subtract
\[
\rho(r)\sum_{j=0}^{N-1}\frac{f^{(2j)}(0)}{(2j)!}r^{2j}.
\]
The remainder is \(O(r^{2N})\) at zero, uniformly with the requisite derivative bounds, and remains rapidly decreasing at infinity. Its Mellin integral is holomorphic for \(\Re w>-2N\). Each subtracted term has Mellin integral
\[
\frac1{w+2j}+\text{an entire function of }w,
\]
if the region on which \(\rho=1\) is chosen as \([0,1]\); another such region changes only an entire term and a nonzero exponential factor in the pole term. The reciprocal \(\Gamma(w/2)^{-1}\) has a simple zero at each \(w=-2j\), so all these poles cancel.

The Taylor remainder on \([0,1]\) is bounded by a finite derivative seminorm. On \(1,\infty)\), a sufficiently high Schwartz decay seminorm bounds the integral uniformly on any fixed compact parameter set. The same estimates absorb each power of \(\log r\) introduced by parameter differentiation. The canceled pole terms are bounded on compact sets as entire functions. Increasing \(N\) proves the assertion everywhere, with the required seminorm bounds. The gamma recurrence, its poles, and the entire reciprocal are actually proved in [*Tate's local theory at the infinite places*, the section “Mellin continuation without a functional equation”; no gamma nonvanishing assertion is being inferred from a functional equation.

For \(h\in\mathcal S(\mathbb R^n)\) even in every variable, this construction in each variable gives
\[
\mathcal M_{\boldsymbol w}(h)=
\frac1{\prod_j\Gamma(w_j/2)}
\int_{(0,\infty)^n}h(\boldsymbol r)\prod_j r_j^{w_j-1}\,d\boldsymbol r.
\tag{1.22e}
\]
It is jointly entire and satisfies the analogous seminorm bounds. To justify this without a tensor-product assertion, apply the preceding cutoff and finite Taylor subtraction in each coordinate. The resulting finite expansion consists of products of the canceled pole terms and integrals of remainders on coordinate rectangles. Each remainder has the independently prescribed order of vanishing at each small coordinate and rapid decay in every large coordinate. On a compact subset of \(\mathbb C^n\), choose all subtraction orders sufficiently large and a common sufficiently large decay exponent. The product bounds give absolute majorants for these integrals and all parameter derivatives. The finite expression proves both joint holomorphy and continuity on the entire even Schwartz space.

##### 2. QR coordinates on the whole matrix space

Put
\[
\delta=\dim_{\mathbb R}F,\quad
b_F=\begin{cases}\pi,&F=\mathbb R,\\[2pt]
2\pi,&F=\mathbb C,\end{cases}
\quad d_j=n-j+1,\quad m=\begin{cases}e,&F=\mathbb R,\\|k|,&F=\mathbb C.\end{cases}
\]
Every invertible matrix has a unique decomposition \(X=UR\), where
\(U\in K=O(n)\) or \(U(n)\), and \(R\) is upper triangular with positive real diagonal \(r_j\). The strictly upper entries form a vector \(Y\) over \(F\). Successive column Gram–Schmidt proves this decomposition.

Its additive integration formula is
\[
dX=A_F\,dU\,dY\prod_{j=1}^n r_j^{\delta d_j-1}\,dr_j,\qquad
A_F=\frac{2^n b_F^{\delta n(n+1)/4}}
{\prod_{j=1}^n\Gamma(\delta j/2)},                              \tag{1.22f}
\]
where \(dU\) is probability Haar measure and each complex upper entry uses measure \(2\,d\Re y\,d\Im y\).

For completeness, obtain the exponents by taking polar coordinates in the first column, then decomposing each subsequent column into its coordinates along the preceding orthonormal columns and its orthogonal component. That component has real dimension \(\delta d_j\), so radial measure contributes \(r_j^{\delta d_j-1}dr_j\). Changes to an orthonormal frame have real Jacobian one. The successive angular probability measures give a probability measure on complete orthonormal frames invariant under left \(K\); averaging over \(K\) shows it is Haar probability. These steps prove (1.22f) up to a positive constant. To find it, integrate the basic Gaussian \(e^{-b_F\|X\|^2}\), whose mass is one. Every strictly upper Gaussian integral has mass one, and the \(j\)-th radial integral is
\[
\frac12 b_F^{-\delta d_j/2}\Gamma(\delta d_j/2).
\]
Their product gives the displayed constant. The excluded singular set has additive measure zero: in successive column integration, a column lying in the span of its predecessors belongs to a proper real linear subspace.

Write \(\xi(x)=\operatorname{sgn}(x)^e\) or
\(\xi(z)=(z/|z|)^k\). For arbitrary diagonal entries \(z_j\in F\), define
\[
H_\Phi(\boldsymbol z)=
\int_K\int_{F^{n(n-1)/2}}\xi(\det U)\,
\Phi\bigl(U R(\boldsymbol z,Y)\bigr)\,dY\,dU.                  \tag{1.22g}
\]
This is a continuous linear map from \(\mathcal S(M_n(F))\) to
\(\mathcal S(F^n)\). Indeed \(\|UR\|=\|R\|\); differentiation in the diagonal entries gives a finite combination of derivatives of \(\Phi\) with coefficients bounded uniformly in \(U\). A Schwartz bound of arbitrarily large order in \((\boldsymbol z,Y)\), integrated over \(Y\) and compact \(K\), bounds every weighted derivative in \(\boldsymbol z\). This proves the assertion, with each target seminorm bounded by finitely many source seminorms.

Changing row \(j\) of \(R\) by a real sign gives
\[
H_\Phi(\ldots,-r_j,\ldots)=(-1)^e H_\Phi(\ldots,r_j,\ldots).
\]
Over \(\mathbb C\), changing that row by \(e^{i\theta}\), rotating its upper entries in the \(Y\)-integral, and replacing \(U\) by \(U\operatorname{diag}(1,\ldots,e^{i\theta},\ldots,1)\), gives
\[
H_\Phi(\ldots,e^{i\theta}z_j,\ldots)
=e^{-ik\theta}H_\Phi(\ldots,z_j,\ldots).                       \tag{1.22h}
\]
In the Taylor expansion at \(z_j=0\), this retains only monomials \(z_j^p\bar z_j^q\) with \(p-q=-k\). All derivatives of total order less than \(|k|\) vanish, and restriction to the real axis has parity \((-1)^{|k|}\).

It follows that on the real diagonal
\[
H_\Phi(\boldsymbol r)=\prod_j r_j^m\,h_\Phi(\boldsymbol r),
\qquad h_\Phi\in\mathcal S(\mathbb R^n),
\tag{1.22i}
\]
with \(h_\Phi\) even in each variable; this division is continuous on the indicated subspace. Explicitly, near \(r_j=0\), division by \(r_j^m\) is given by the integral Taylor remainder
\[
\frac{f(r_j)}{r_j^m}
=\frac1{(m-1)!}\int_0^1(1-\theta)^{m-1}
f^{(m)}(\theta r_j)\,d\theta\quad(m>0).
\]
On \(|r_j|\ge1\), differentiate the ordinary quotient. Both formulas bound all Schwartz seminorms, using ordinary derivatives on the bounded coordinate and rapid decay in the other coordinates. Repeating in the coordinates gives (1.22i). For \(m=0\) no division is required.

##### 3. Entire division for every Schwartz test

Put
\[
t=s+a-\frac{n+1}{2},\qquad
w_j=\delta(t+d_j)+m.
\]
For \(\Re t>-1\), QR integration is absolutely convergent before the compact angular average: the smallest radial dimension is \(\delta\), and \(\delta(t+1)>0\) is precisely the worst radial integrability condition. Infinity is controlled by Schwartz decay. Equations (1.22f)–(1.22i) give
\[
Z_\chi(s,\Phi)=C_FA_F
\int_{(0,\infty)^n}h_\Phi(\boldsymbol r)
\prod_j r_j^{w_j-1}\,d\boldsymbol r.
\tag{1.22j}
\]
Let \(\iota_F=0\) over \(\mathbb R\) and \(1\) over \(\mathbb C\).
Reindexing \(d_j\) in (1.22a) gives exactly
\[
L_\chi(s)=
2^{n\iota_F} b_F^{-\sum_jw_j/2}
\prod_j\Gamma(w_j/2).
\]
Consequently
\[
\mathcal D_\chi(s)(\Phi)=
C_FA_F\,2^{-n\iota_F}
b_F^{\sum_jw_j/2}\mathcal M_{\boldsymbol w}(h_\Phi).             \tag{1.22k}
\]
The Mellin construction and continuity of \(\Phi\mapsto h_\Phi\) prove (1.22b)–(1.22c), including their derivative versions. Multiplication by \(L_\chi\) then gives the meromorphic continuation of the original integral. Angular cancellation may enlarge the convergence domain of (1.22j); it has not been used to assert absolute convergence of the original integral in that larger domain.

##### 4. A uniqueness lemma for determinant-equivariant distributions

Fix \(t\in\mathbb C\) with \(\Re t>0\), and let a distribution \(T\) on \(M_n(F)\) satisfy
\[
T(\Phi(hX))=
\xi(\det h)^{-1}|\det h|_F^{-(t+n)}T(\Phi),
\qquad
T(\Phi(Xh))=
\xi(\det h)^{-1}|\det h|_F^{-(t+n)}T(\Phi)                     \tag{1.22l}
\]
for every \(h\in G\). Such distributions form a one-dimensional space, spanned by the regular distribution
\(\Phi\mapsto\int\Phi(X)\xi(\det X)|\det X|_F^t\,dX\).

First consider restriction to \(G\). Multiplying the distribution by the reciprocal of the smooth character
\[
W(X)=\xi(\det X)|\det X|_F^{t+n}
\]
makes it left invariant. A left-invariant distribution is a constant times Haar measure. Here is a distribution-level proof of that assertion. Choose compactly supported smooth approximate identities \(\rho_j\) of Haar integral one. Left invariance gives
\[
S(\phi*\rho_j)=S(\rho_j)\int_G\phi\,dg.
\]
Convolution with \(\rho_j\) tends to the identity in the compactly supported smooth topology: in a group coordinate chart this follows by Taylor estimates uniformly on a common compact support. Fixing one \(\phi_0\) of integral one shows \(S(\rho_j)\to S(\phi_0)\), and the displayed equality then proves the assertion for every \(\phi\). Since \(dg\) is a constant times \(\nu^{-n}dX\), the restriction of \(T\) has the claimed density.

It remains to prove that no nonzero distribution satisfying (1.22l) can be supported on singular matrices. Induct downwards on the largest rank \(r<n\) in its support. Near a rank-\(r\) matrix, choose an invertible \(r\)-by-\(r\) minor, after fixed row and column permutations. Put \(m_0=n-r\) and use the chart
\[
X=
\begin{pmatrix}
A&Ab\\
cA&cAb+W
\end{pmatrix},
\quad A\in GL_r(F),\quad
b\in M_{r,m_0}(F),\quad c\in M_{m_0,r}(F).
\tag{1.22m}
\]
Here \(\operatorname{rank}X=r+\operatorname{rank}W\). Left lower-block unipotents translate \(c\), and right upper-block unipotents translate \(b\), with determinant one. Thus the chart distribution factors as Lebesgue measure in \(b,c\), times a distribution \(U\) in \(A,W\).

For clarity, translation invariance gives this factorization without a disintegration theorem. In one variable, a compactly supported smooth function of integral zero is the derivative of its compactly supported primitive. In several variables choose fixed integral-one bumps and subtract successive coordinate averages. The difference from the product bump times the total integral is a sum of coordinate derivatives, with compact support and smooth dependence on all other parameters. A translation-invariant distribution annihilates these derivatives. This proves the asserted factorization; constants in the complex coordinate measures do not change it.

The support of \(U\) lies in \(W=0\). On every compact \(A\)-subchart it has finite normal order:
\[
U(f)=\sum_{|\alpha|\le N}U_\alpha\bigl(\partial_W^\alpha f(A,0)\bigr),
\tag{1.22n}
\]
for distributions \(U_\alpha\) in \(A\). To prove this assertion, take a finite-order bound for \(U\) on a compact coordinate set. If all normal derivatives through that order vanish at \(W=0\), multiply \(f\) by a cutoff supported in \(\|W\|\le\varepsilon\), equal to one near zero. Taylor's estimate makes its bounded derivatives tend to zero as \(\varepsilon\to0\), while its value under \(U\) is unchanged. Thus \(U(f)=0\). Subtracting the finite Taylor polynomial in \(W\), multiplied by a fixed cutoff equal to one near zero, proves (1.22n), including continuity of its coefficients.

Now apply left multiplication by \(\operatorname{diag}(I_r,h)\), \(h\in GL_{m_0}(F)\). In (1.22m) this sends \((c,W)\) to \((hc,hW)\). The \(c\)-integration contributes \(|\det h|_F^{-r}\), so (1.22l) implies
\[
U(f(A,hW))=
\xi(\det h)^{-1}|\det h|_F^{-(t+m_0)}U(f).                    \tag{1.22o}
\]
Take \(h=zI_{m_0}\) with \(z>1\) real. The angular character is one. A normal jet of degree \(j\) on the left of (1.22o) is multiplied by \(z^j\), while the right multiplier is
\[
z^{-\delta m_0(t+m_0)}.
\]
Its absolute value is less than one, whereas \(z^j\ge1\). Tests with one prescribed normal Taylor monomial isolate each coefficient in (1.22n), so every \(U_\alpha\) is zero. The distribution therefore vanishes near the rank-\(r\) stratum. Descending the rank, including \(r=0\), proves the uniqueness lemma. This argument uses only positive real scalar elements of the stabilizer and works over both fields with all angular characters.

##### 5. Fourier equation on the whole Schwartz space

The Fourier transform preserves the Schwartz space continuously, has square \(\Phi(X)\mapsto\Phi(-X)\), and fixes the basic Gaussian. These are the actual earlier whole-space proofs in *Additive characters, self-dual measures and Poisson summation on the adèles*, Proposition 5.2 and Lemma 5.4A, applied in real dimension \(n^2\) or \(2n^2\). The trace pairing permutes entry coordinates; over \(\mathbb C\) its real coefficient matrix has eigenvalues \(2,-2\) on each scalar pair, matching the factor two in the self-dual measure.

Consider the two entire tempered-distribution families
\[
\mathcal D_\chi(s)(\Phi),\qquad
\mathcal B_\chi(s)(\Phi)=\mathcal D_{\chi^{-1}}(1-s)(\widehat\Phi).
\]
The first satisfies (1.22l) with \(t=s+a-(n+1)/2\), first by substitution in its integral and then everywhere by continuation. The second satisfies the same laws. Indeed
\[
\widehat{\Phi(h\,\cdot)}(Y)=|\det h|_F^{-n}
\widehat\Phi(Yh^{-1}),
\]
and the dual determinant parameter is \(t'=-t-n\). Its right-equivariance factor therefore combines with the Fourier Jacobian to give
\(\xi(\det h)^{-1}|\det h|_F^{-(t+n)}\). The other side is identical with the two matrix multiplication sides exchanged. Notice that the trace pairing requires \(Yh^{-1}\), not a conjugate transpose.

When \(\Re t>0\), the uniqueness lemma makes these two distributions proportional. Its conclusion on compactly supported smooth tests also determines a tempered distribution on the entire Schwartz space. Indeed, multiply a Schwartz test by a smooth cutoff \(\rho(X/R)\), equal to one on \(\|X\|\le R\). Each seminorm of the discarded tail is bounded by \(O(R^{-1})\) times finitely many seminorms with one additional decay power; the derivatives of the cutoff satisfy the same bound. Thus the cutoff tests converge in Schwartz topology, and continuity extends the distribution identity. Determine the scalar using the attaining test
\[
\Phi_\chi(X)=
\begin{cases}
(\det X)^e e^{-\pi\|X\|^2},&F=\mathbb R,\\
(\overline{\det X})^k e^{-2\pi\|X\|^2},&F=\mathbb C,\ k\ge0,\\
(\det X)^{-k}e^{-2\pi\|X\|^2},&F=\mathbb C,\ k<0.
\end{cases}
\]
QR integration, or the earlier Gaussian calculation, gives
\[
\mathcal D_\chi(s)(\Phi_\chi)=K_F,\qquad
K_{\mathbb R}=C_{\mathbb R}
\frac{\pi^{n(n+1)/4}}{\prod_j\Gamma(j/2)},\quad
K_{\mathbb C}=C_{\mathbb C}
\frac{(2\pi)^{n(n+1)/2}}{2^n\prod_j\Gamma(j)}.                  \tag{1.22p}
\]
Both constants are nonzero and independent of \(s,a,e,k\).

With the negative-exponent programme character and positive trace argument,
\[
\widehat{\Phi_\chi}=(-i)^{ne}\Phi_{\chi^{-1}}
\quad(F=\mathbb R),\qquad
\widehat{\Phi_\chi}=(-i)^{n|k|}\Phi_{\chi^{-1}}
\quad(F=\mathbb C).                                         \tag{1.22q}
\]
Here \(\Phi_{\chi^{-1}}\) denotes the opposite angular attaining polynomial, and is independent of the radial exponent. Over \(\mathbb R\), multiplication by a coordinate transforms to \(-(2\pi i)^{-1}\) times the appropriate derivative of the Fourier Gaussian. Every determinant monomial uses distinct coordinates, giving exactly \((-i)^n\det Y\), with transpose harmless. Over \(\mathbb C\), the scalar calculation gives
\(\widehat{\bar z\,e^{-2\pi|z|^2}}=-iz\,e^{-2\pi|z|^2}\) and its conjugate counterpart. Successive Wirtinger differentiation of a holomorphic or antiholomorphic polynomial introduces no lower contractions: the resulting polynomial depends on the coordinate independent of that derivative. Hence a homogeneous such polynomial of degree \(N\) has phase \((-i)^N\); determinant powers have degree \(n|k|\). This proves (1.22q) in all ranks.

Equations (1.22p)–(1.22q) determine the proportionality scalar as the value in (1.22d). The identity initially obtained for \(\Re t>0\) extends to every \(s\): for each Schwartz test both sides are entire by (1.22k) and Fourier continuity, so the ordinary identity theorem applies. No overlapping convergence half-plane for the original and transformed integrals is required. This proves the full theorem.

For the positive-exponent characters \(e^{2\pi ix}\) and
\(e^{2\pi i(z+\bar z)}\), the same proof replaces \(-i\) by \(i\).
In either convention the product of the two epsilon phases is
\(\chi((-1)^n)\), exactly the central sign from applying Fourier twice.

For any nonzero scalar \(b\in F\), let \(\psi_b(x)=\psi_F(bx)\).
Self-dual matrix measure is multiplied by \(|b|_F^{n^2/2}\), and
\[
\widehat\Phi^{\,\psi_b}(Y)=|b|_F^{n^2/2}\widehat\Phi^{\,\psi_F}(bY).
\]
Substitution \(Y=b^{-1}X\) in the dual integral gives
\[
\epsilon_\chi(s,\psi_b)=
\chi(b^n)|b|_F^{n(s-1/2)}\epsilon_\chi.                       \tag{1.22r}
\]
This includes every nontrivial archimedean additive character by the actual local self-duality proof in Proposition 5.1 of the preceding additive-character lesson.

Replacing \(\chi(x)\) by \(\chi(x)|x|_F^b\) replaces \(s\) by \(s+b\) in the original integral and in (1.22a), while the dual parameter becomes \(1-s-b\). If \(\chi\) is unitary, then \(\Re a=0\); the inverse has radial parameter \(-a=\bar a\) and the same \(e\) or \(|k|\). The gamma definition, initially by its real integral and then by continuation, therefore gives
\[
L_{\chi^{-1}}(s)=\overline{L_\chi(\bar s)}.
\]
The canonical phases in (1.22d) have absolute value one, and (1.22r) retains that property at \(s=1/2\) for every additive character when \(\chi\) is unitary.

##### 6. Preceding proofs and further reading

- *Tate's local theory at the infinite places*, “Mellin continuation without a functional equation,” equations (5)–(11): actual gamma reciprocal, pole and scalar angular Mellin proofs. Section 1 above supplies the needed stronger multivariable seminorm argument.
- *Additive characters, self-dual measures and Poisson summation on the adèles*, equations (1)–(2), Proposition 5.2 and Lemma 5.4A: actual character conventions, Gaussian transforms, Schwartz continuity and inversion.
- Proposition 1.7 of this lesson: the complete polynomial Gaussian ideal, including its Gram–Schmidt moment proof. The theorem above adds every Schwartz test and its full Fourier equation.
- B. Rubin, [*Zeta integrals and integral geometry in the space of rectangular matrices*, arXiv:math/0406289](https://arxiv.org/pdf/math/0406289), Lemma 2.7, printed p. 13; Lemma 4.2, printed p. 18; Theorem 4.3, printed pp. 19–21. These give the QR/Mellin method and Fourier theorem for the unsigned real determinant case when the matrix is square. Sections 1–5 above include the topology, sign and complex angular arguments rather than importing that source's result for them.
- D. Goldfeld and H. Jacquet, [*Automorphic representations and L-functions for GL(n)*, author-hosted notes](https://www.math.columbia.edu/~goldfeld/LanglandsBookChapter.pdf), Theorem 3.5, printed pp. 15–16, and Lemma 3.6, printed p. 17, formulate the general irreducible archimedean target. Their Fourier definition on printed p. 15 uses \(\psi(-\operatorname{tr}(XY))\); phases from that convention require reversing the character to use (1.22d).

The general irreducible target is unchanged: prove its Gaussian gamma ideal and attaining family, full-Schwartz division and Fourier equation, with the necessary realization, induced-representation and factor-identification arguments. The scalar equivariance in (1.22l) is specific to determinant characters; this proof does not supply those representation-valued arguments.

### Canonical matrix gamma ideals for symmetric powers in every archimedean rank

Let \(F=\mathbb R\) or \(\mathbb C\), \(G=GL_n(F)\), and
\(\nu(g)=|\det g|_F\). Write
\[
\rho_j=\frac{n+1}{2}-j,\qquad
B_F(s)=\prod_{j=1}^n\Gamma_F(s+\rho_j),
\qquad
\Gamma_{\mathbb R}(z)=\pi^{-z/2}\Gamma(z/2),\quad
\Gamma_{\mathbb C}(z)=2(2\pi)^{-z}\Gamma(z).
\tag{1.30a}
\]
We use the actual programme characters
\(\psi_{\mathbb R}(x)=e^{-2\pi ix}\) and
\(\psi_{\mathbb C}(z)=e^{-2\pi i(z+\bar z)}\), self-dual additive
matrix measure, and the **positive trace argument**
\[
\widehat\Phi(Y)=\int_{M_n(F)}\Phi(X)\psi_F(\operatorname{tr}(XY))\,dX .
\tag{1.30b}
\]
Put \(dg=C_F\nu(g)^{-n}dX\), where \(C_F>0\) is fixed. The
matrix integral is
\[
Z_\pi(s,\Phi,c)=
\int_G\Phi(g)c(g)\nu(g)^{s+(n-1)/2}\,dg.
\tag{1.30c}
\]
Our Gaussian is \(G_{\mathbb R}(X)=e^{-\pi\|X\|^2}\) or
\(G_{\mathbb C}(X)=e^{-2\pi\|X\|^2}\). A polynomial Gaussian means
a polynomial in all real coordinates times this Gaussian; over
\(\mathbb C\) these are exactly the polynomials in \(X,\bar X\)
times \(G_{\mathbb C}\).

For \(m\geq0\) and \(t\in\mathbb C\), consider the actual finite-dimensional
smooth representation
\[
\pi_{m,t}(g)=\nu(g)^t\operatorname{Sym}^m(g).
\tag{1.30d}
\]
Over \(\mathbb C\) we also allow the antiholomorphic representation
\(\nu(g)^t\operatorname{Sym}^m(\bar g)\). The theorem below includes
their contragredients. It is a theorem about these explicit families
in every rank, not a classification of all admissible representations.

**Theorem 1.25.** Put \(m=2l+e\), \(e\in\{0,1\}\), in the real case.
The canonical Gaussian-polynomial matrix ideals for (1.30d) have generators
\[
\begin{aligned}
L_{\pi_{m,t}}(s)
&=\Gamma_{\mathbb R}(s+t+\rho_1+m+e)
\prod_{j=2}^n\Gamma_{\mathbb R}(s+t+\rho_j),
&&F=\mathbb R,\\
L_{\pi_{m,t}}(s)
&=\Gamma_{\mathbb C}(s+t+\rho_1+m)
\prod_{j=2}^n\Gamma_{\mathbb C}(s+t+\rho_j),
&&F=\mathbb C .
\end{aligned}
\tag{1.30e}
\]
The antiholomorphic complex family has the same formula.
For the contragredients,
\[
\begin{aligned}
L_{\pi_{m,t}^{\vee}}(s)
&=\Gamma_{\mathbb R}(s-t-\rho_1-m+e)
\prod_{j=2}^n\Gamma_{\mathbb R}(s-t-\rho_j),
&&F=\mathbb R,\\
L_{\pi_{m,t}^{\vee}}(s)
&=B_{\mathbb C}(s-t),
&&F=\mathbb C .
\end{aligned}
\tag{1.30f}
\]
The complex antiholomorphic dual again has the same formula.
More precisely, the \(\mathbb C[s]\)-span of **all** polynomial-Gaussian
tests and matrix coefficients is exactly \(L_\pi(s)\mathbb C[s]\).
One test and one coefficient attain a nonzero constant multiple
of the displayed generator. For every Schwartz test and every coefficient,
\(Z_\pi/L_\pi\) is entire; on each compact parameter set it has a bound
by a fixed finite sum of Schwartz seminorms and a norm on the finite
coefficient space.

For \(c^\vee(g)=c(g^{-1})\), the complete scalar functional equation is
\[
Z_{\pi^\vee}(1-s,\widehat\Phi,c^\vee)
=\epsilon_\pi\frac{L_{\pi^\vee}(1-s)}{L_\pi(s)}
Z_\pi(s,\Phi,c),\qquad
\epsilon_\pi=
\begin{cases}(-i)^e,&F=\mathbb R,\\(-i)^m,&F=\mathbb C.\end{cases}
\tag{1.30g}
\]
The same phases hold for the contragredient and antiholomorphic families.
These statements hold for every \(n\geq1\), every \(m\geq0\), and
every complex norm exponent \(t\).

#### Exactly which preceding results enter

The determinant-character theorem of this lesson, Theorem 1.18, supplies
the following proved entire distribution family:
\[
T_F(z)(\Psi)=
\frac{C_F}{B_F(z)}
\int_{M_n(F)}\Psi(X)|\det X|_F^{\,z-(n+1)/2}\,dX .
\tag{1.30h}
\]
It is initially the integral in its convergence region, extends to
every \(z\), and has compact-parameter Schwartz seminorm bounds.
Every polynomial Gaussian has polynomial \(T_F(z)\)-value,
and
\[
T_F(z)(G_F)=K_F\ne0
\tag{1.30i}
\]
independently of \(z\). The proof of Theorem 1.18 gives the exact
constant \(K_F\), but its value will cancel throughout this argument.
It also proves the full determinant functional equation
\[
T_F(1-z)(\widehat\Psi)=T_F(z)(\Psi).
\tag{1.30j}
\]
The Gram–Schmidt measure and its first-column gamma moments are the
proved calculation of Proposition 1.7, “Proof: all the Gaussian
moments,” equations (1.8f)–(1.8g) and the ensuing radial-moment argument.

The scalar gamma recurrence, its pole set and absence of zeros, and
the real parity and complex angular Tate normalizations are the actual
proofs in *Tate’s local theory at the infinite places*,
“Mellin continuation without a functional equation” and
Propositions 8.2–8.4. Full-Schwartz Fourier continuity, inversion,
and the basic Gaussian transform are proved in *Additive characters, self-dual measures and Poisson summation on the adèles*, Proposition 5.2 and Lemma 5.4A.
No general induction, classification, globalization or asymptotic theorem
is used below.

#### Representations and coefficient spans

Identify \(\operatorname{Sym}^m(\mathbb C^n)\) with homogeneous
polynomials of degree \(m\) in formal variables. It is irreducible
under \(\mathfrak{gl}_n(\mathbb C)\): the commuting diagonal operators
have distinct monomial joint weights. From any nonzero invariant
subspace, polynomial spectral projections in those diagonal operators
extract a nonzero monomial. The operators \(x_i\partial_{x_j}\)
move one unit of exponent from \(j\) to \(i\), with nonzero coefficient
whenever that exponent is positive. They connect every degree-\(m\)
monomial to every other. Thus the invariant subspace is the entire space.
The differentiated real \(GL_n(\mathbb R)\) action has this complex
enveloping-algebra action, and the differentiated holomorphic
\(GL_n(\mathbb C)\) action does too. Norm twisting changes no invariant
subspaces. Antiholomorphic conjugation and duality preserve irreducibility.

These are actual complete smooth moderate-growth realizations with their
finite-dimensional topology and the usual continuous dual pairing.
Indeed \(\|\operatorname{Sym}^m(g)\|\leq C\|g\|^m\), and
\(|\nu(g)^t|=\nu(g)^{\operatorname{Re}t}\) is bounded by a power of
\(1+\|g\|+\|g^{-1}\|\). Every differentiated action is a fixed matrix.
The same estimates with \(g^{-1}\) give the dual. No abstract
globalization assertion is needed.

Pure powers \(v^{\otimes m}\), \(v\in F^n\), span the symmetric power.
If a linear functional killed every pure power, its homogeneous
polynomial in the coordinates of \(v\) would vanish identically.
A polynomial vanishing on \(\mathbb R^n\), or on \(\mathbb C^n\),
has every coefficient zero, by the one-variable polynomial identity
successively in each coordinate. The same argument applies to the dual.
Consequently all coefficients, with the norm character removed, are
spanned by
\[
c_{u,v}(X)=(u^tXv)^m,\qquad u,v\in F^n.
\tag{1.30k}
\]
The dual coefficients are spanned by \((u^tX^{-1}v)^m\).
Over \(\mathbb C\) complex conjugation gives the corresponding
antiholomorphic spans.

In particular, the coefficient \((X_{11})^m\) has left and right
\(G\)-translates spanning the entire coefficient space. This last fact
uses the full group, not the restriction to \(O(n)\); that restriction
of a real symmetric power can be reducible.

#### Removing exactly the finite polynomial from the base generator

Put \(p=z-(n+1)/2\). In the real case let
\[
a=(p+n)/2=(z+\rho_1)/2;
\]
in the complex case let
\[
a=p+n=z+\rho_1.
\]
At negative integral values of \(a\), (1.30j) makes (1.30h) particularly
simple.

**Lemma 1.25a (the point distributions).** At \(a=-k\), \(k=0,1,\ldots\),
\(T_{\mathbb R}(z)\) is a nonzero scalar multiple of
\((\det\partial)^{2k}\delta_0\). At \(a=-k\),
\(T_{\mathbb C}(z)\) is a nonzero scalar multiple of
\((\det\partial_X)^k(\det\partial_{\bar X})^k\delta_0\).

**Proof.** For the real parameter \(z=-2k-\rho_1\), the dual exponent
in (1.30h), at \(1-z\), is \(2k\). Its kernel is the polynomial
\(\det(Y)^{2k}\), divided by the nonzero number \(B_{\mathbb R}(1-z)\).
All its gamma arguments are positive. In the complex case
\(z=-k-\rho_1\) gives dual exponent \(k\), and the dual kernel is
\(\det(Y)^k\overline{\det(Y)}^k/B_{\mathbb C}(1-z)\), again with a
nonzero denominator. The Fourier transform of a coordinate polynomial
is the corresponding derivative of \(\delta_0\), with a nonzero
constant. This follows by differentiating (1.30b) and applying its proved
Schwartz inversion; entry transposition in the trace pairing leaves the
determinant differential operator unchanged. Equation (1.30j) proves
the claimed identities as identities on the **whole** Schwartz space.
\(\square\)

Multiplication by \(X_{11}^m\) kills the real point distribution when
\(m>2k\), since every term of \((\det\partial)^{2k}\) has total
derivative degree \(2k\) in its first row. It kills the complex point
distribution when \(m>k\), since the holomorphic first-row derivative
degree is \(k\). These assertions hold after applying the derivative
to \(X_{11}^m\Psi\): every resulting evaluation at zero vanishes.

The distribution (1.30h) is relatively equivariant under
\(X\mapsto AXB\). A direct change of variables proves this in its
initial half-plane, and the identity theorem proves it everywhere.
Thus if a coefficient polynomial \(c\) annihilates \(T_F(z)\),
then every left and right \(G\)-translate of \(c\) also annihilates it.
For clarity, the relative scalar is
\[
T_F(z)(\Psi(AXB))
=|\det A\det B|_F^{-(z+\rho_1)}T_F(z)(\Psi).
\tag{1.30l}
\]
It is nonzero for every invertible \(A,B\). The coefficient-span result
of Section 2 therefore proves the same annihilation for every coefficient
of the symmetric power, including arbitrary linear combinations.

For (1.30d), use \(z=s+t\) in this discussion. By (1.30h), every
\(Z_{\pi_{m,t}}(s,\Phi,c)/B_F(s+t)\), with the norm factor removed
from \(c\), is a polynomial for a polynomial-Gaussian \(\Phi\).
It is divisible by
\[
\begin{cases}
(a)_{l+e},&F=\mathbb R,\quad a=(s+t+\rho_1)/2,\\
(a)_m,&F=\mathbb C,\quad a=s+t+\rho_1,
\end{cases}
\qquad (a)_r=\prod_{h=0}^{r-1}(a+h).
\tag{1.30m}
\]
The roots here are distinct and were just proved to be zero values
for every coefficient and every Schwartz test.
The gamma recurrence gives exactly
\[
\frac{L_{\pi_{m,t}}(s)}{B_F(s+t)}=
\begin{cases}
\pi^{-(l+e)}(a)_{l+e},&F=\mathbb R,\\
(2\pi)^{-m}(a)_m,&F=\mathbb C.
\end{cases}
\tag{1.30n}
\]
So every polynomial-Gaussian integral is a polynomial multiple of
the proposed canonical generator, rather than merely an entire multiple
of a larger gamma product.

#### One coefficient and one Gaussian attain the bound

In the QR calculation \(X=UR\), the first column is \(r_1u\),
where \(u\) is a compact uniform unit vector. With determinant weight,
the first radial gamma argument is the \(a\) of Section 3.
Thus its even moment ratio is
\(\pi^{-h}(a)_h\) over \(\mathbb R\), or
\((2\pi)^{-h}(a)_h\) over \(\mathbb C\).
This is the explicit first-column specialization of Proposition 1.7's
Gram–Schmidt measure proof.

For real \(m=2l\), take
\[
c(X)=\left(\sum_iX_{i1}^2\right)^l,\qquad \Phi=G_{\mathbb R}.
\tag{1.30o}
\]
This is a coefficient: apply the degree-\(m\) polynomial
\((\sum_i x_i^2)^l\) as the dual functional to
\(\operatorname{Sym}^m(X)e_1^{\otimes m}\).
Its QR value is \(r_1^{2l}\), so
\[
Z_{\pi_{m,t}}(s,G_{\mathbb R},\nu^t c)
=K_{\mathbb R}L_{\pi_{m,t}}(s).
\tag{1.30p}
\]
For real \(m=2l+1\), take
\[
c(X)=X_{11}\left(\sum_iX_{i1}^2\right)^l,\qquad
\Phi=X_{11}G_{\mathbb R}.
\tag{1.30q}
\]
Now the angular average is
\(\int u_1^2\,du=1/n\): orthogonal invariance makes all coordinate
second moments equal and their sum is one. The radial moment is
\(r_1^{2l+2}\). Hence
\[
Z_{\pi_{m,t}}(s,X_{11}G_{\mathbb R},\nu^t c)
=\frac{K_{\mathbb R}}{n}L_{\pi_{m,t}}(s).
\tag{1.30r}
\]

For the holomorphic complex family, take
\[
c(X)=X_{11}^m,\qquad \Phi=\bar X_{11}^mG_{\mathbb C}.
\tag{1.30s}
\]
The angular moment is \(m!/(n)_m\). Here is a proof of its constant.
The product complex Gaussian gives the moment \(m!/(2\pi)^m\)
in one coordinate. Polar coordinates for the whole \(n\)-vector
give radius moment \((n)_m/(2\pi)^m\); the radial gamma integral
follows by the same substitution as the one-coordinate integral.
Dividing the two equal descriptions of the Gaussian integral yields
the angular moment. Therefore
\[
Z_{\pi_{m,t}}(s,\bar X_{11}^mG_{\mathbb C},\nu^t c)
=\frac{K_{\mathbb C}m!}{(n)_m}L_{\pi_{m,t}}(s).
\tag{1.30t}
\]
For the antiholomorphic family interchange \(X\) and \(\bar X\).
All constants in (1.30p), (1.30r), (1.30t) are nonzero and independent of
\(s,t\).

To finish the ideal assertion, the family is closed under multiplication
by \(s\). Let \(E\) be real scalar dilation on matrix space and
\(d=[F:\mathbb R]\). Differentiating a change of variable \(X\mapsto rX\)
in an absolutely convergent integral gives
\[
Z_{\pi_{m,t}}(s,E\Phi,c)
=-\{dn(s+t+\rho_1)+m\}Z_{\pi_{m,t}}(s,\Phi,c),
\tag{1.30u}
\]
where \(c\) on both sides denotes the coefficient including the norm
factor. The meromorphic identity continues, and \(E\Phi\) is again a
polynomial Gaussian. Thus all polynomials times the attained generator
belong to the span. Combined with (1.30n), this proves the exact
\(\mathbb C[s]\)-ideal and finite attainment for the original family.

#### Every dual Gaussian and every dual Schwartz test

The matrix determinant lemma, proved by multilinearity of columns, says
\[
\det(X+hvu^t)=\det X\,(1+h\,u^tX^{-1}v).
\tag{1.30v}
\]
Let \(D_{v u^t}\) be differentiation along this rank-one matrix.
Over \(\mathbb C\) use its holomorphic directional derivative;
for the antiholomorphic family use the conjugate derivative.
On invertible matrices,
\[
D_{v u^t}^{\,m}|\det X|_F^p
=(p)^{\downarrow}_m(u^tX^{-1}v)^m|\det X|_F^p,
\qquad
(p)^{\downarrow}_m=\prod_{h=0}^{m-1}(p-h).
\tag{1.30w}
\]
In the complex case \(|\det X|_{\mathbb C}^p\) has the local form
\(\det(X)^p\overline{\det(X)}^p\), and the holomorphic derivative
differentiates only the first factor. In the real case, on either
determinant component, differentiating \(|\det X|^p\) gives the same
formula.

The identity holds as a distribution for sufficiently large
\(\operatorname{Re}p\), by integration by parts. To justify this without a
boundary assumption, take \(\operatorname{Re}p>m+1\) on each compact
set. Each derivative through order \(m\) is a sum of a polynomial
times a power of \(|\det X|\) whose real exponent remains positive.
The derivatives extend by zero continuously across \(\det X=0\).
Restricting to coordinate lines and using the fundamental theorem of
calculus proves they are the distributional derivatives: generic lines
have finitely many determinant zeros, and general lines follow by
continuous approximation. Schwartz cutoffs remove the boundary at
infinity. The identity theorem then proves (1.30w) meromorphically on the
whole Schwartz space, using (1.30h).

For a dual coefficient use \(z=s-t\), \(p=z-(n+1)/2\).
Equation (1.30w) and the coefficient span prove that every dual
polynomial-Gaussian integral has the form
\[
B_F(s-t)\frac{Q(p)}{(p)^{\downarrow}_m},\qquad Q\in\mathbb C[p].
\tag{1.30x}
\]
Indeed a constant-coefficient directional derivative preserves polynomial
Gaussians, so the numerator is a polynomial by (1.30h).

At \(p=k\geq0\), the complex normalized determinant kernel is the
polynomial \(\det X^k\overline{\det X}^k/B_{\mathbb C}(k+(n+1)/2)\).
Equation (1.30v) makes its holomorphic rank-one degree \(k\).
Thus its \(m\)-th rank-one derivative is zero when \(k<m\);
every root of the denominator in (1.30x) cancels. This proves the dual
bound \(B_{\mathbb C}(s-t)\), including all coefficients and all
polynomial Gaussian tests.

At real \(p=2h\geq0\), the kernel is the polynomial
\(\det X^{2h}/B_{\mathbb R}(2h+(n+1)/2)\).
Its rank-one degree is \(2h\), so the derivative vanishes if \(2h<m\).
The even roots of the denominator cancel. The remaining factor is
\[
R_m(p)=\prod_{h=1}^l(p-(2h-1)).
\tag{1.30y}
\]
With \(b=s-t-\rho_1=p+1\), gamma recurrence gives
\[
L_{\pi_{m,t}^{\vee}}(s)
=B_{\mathbb R}(s-t)\frac{(2\pi)^l}{R_m(p)}.
\tag{1.30z}
\]
Consequently every dual Gaussian integral is a polynomial multiple
of (1.30f). It is not necessary, or correct, to cancel the odd real roots
by regarding \(|\det X|^{2h+1}\) as a polynomial.

These arguments also prove **entire division for every Schwartz test**.
For the original family, \(T_F(s+t)(c\Phi)\) is entire and continuous,
because multiplication by the fixed coefficient polynomial is a continuous
Schwartz operator. Its zeros (1.30m) hold for every Schwartz test by
Lemma 1.25a, so division by the finite polynomial is entire.
For the dual family, directional derivatives of \(T_F(s-t)\) are entire
continuous families. The canceled roots in (1.30x) are zeros of these
distributions on every Schwartz test. Dividing by their finite
polynomial leaves an entire family; the remaining real odd-root
denominator is exactly the one absorbed by (1.30z).

Here is the continuity detail. If a continuous entire distribution family
\(A(s)\) vanishes at a root \(s_0\), then each scalar \(A(s)(\Phi)/(s-s_0)\)
has a removable singularity. On a small circle around \(s_0\), Cauchy's
formula bounds the quotient on an inner disk by a fixed constant times
the supremum of \(A(s)(\Phi)\) on that circle. The latter has the
compact-parameter Schwartz seminorm bound of (1.30h), also after a
polynomial multiplier or directional derivative. Remove the finitely
many roots successively and cover a compact parameter set by finitely
many disks and their complement. This gives the asserted locally
uniform seminorm bounds. The coefficient space is finite dimensional,
so a basis makes these bounds jointly continuous in the coefficient.
This proves full-Schwartz entire division directly, without assuming a
general density reduction.

#### The scalar Fourier equation and dual attainment

For the rank-one matrix \(M=vu^t\), differentiation of the Fourier kernel
gives
\[
D_M^m\widehat\Phi=(-2\pi i)^m
\widehat{(u^tXv)^m\Phi}.
\tag{1.30aa}
\]
In the complex holomorphic or antiholomorphic case the corresponding
Wirtinger derivative gives the same formula. This is the reason for
retaining the positive trace argument in (1.30b); entry transposition
in the trace makes \(D_M\) pair with \(u^tXv\), not with a Hermitian
coefficient.

Put \(w=s+t+\rho_1\), and let
\(\gamma_0(s+t)=B_F(1-s-t)/B_F(s+t)\).
At the dual variable \(1-s-t\), the determinant exponent is \(-w\).
Apply (1.30w), integration by parts, (1.30aa), and the whole-family
determinant Fourier equation (1.30j). This gives
\[
(-w)^{\downarrow}_m
Z_{\pi^\vee}(1-s,\widehat\Phi,\nu^{-t}(u^tX^{-1}v)^m)
=(2\pi i)^m\gamma_0(s+t)
Z_\pi(s,\Phi,\nu^t(u^tXv)^m).
\tag{1.30ab}
\]
All operations are identities of meromorphic distributions. There is no
need for overlapping original convergence half-planes. By the
coefficient span, the same scalar equation holds for every coefficient.
Since \((-w)^{\downarrow}_m=(-1)^m(w)_m\), its scalar is
\[
\frac{(-2\pi i)^m}{(w)_m}\gamma_0(s+t).
\tag{1.30ac}
\]

For \(F=\mathbb C\), (1.30n) and (1.30f) immediately turn this into (1.30g).
For \(F=\mathbb R\), split the factors of \((w)_m\) into their even
and odd offsets. With \(h=l+e\),
\[
\begin{aligned}
\frac{L_\pi(s)}{B_{\mathbb R}(s+t)}
&=(2\pi)^{-h}\prod_{j=0}^{h-1}(w+2j),\\
\frac{L_{\pi^\vee}(1-s)}{B_{\mathbb R}(1-s-t)}
&=(-1)^l(2\pi)^l
\left\{\prod_{j=1}^{l}(w+2j-1)\right\}^{-1}.
\end{aligned}
\tag{1.30ad}
\]
Their ratio, times \((-i)^e\), is the multiplier
\((-2\pi i)^m/(w)_m\), since
\((-i)^e(-1)^l=(-i)^m\).
This proves the real phase in (1.30g).

The original attaining test has Fourier transform equal to the
following dual attaining test times exactly \(\epsilon_\pi\):
\[
\begin{array}{c|c|c}
F,m&\Phi&\Phi^\vee\\ \hline
\mathbb R,\ m\ {\rm even}&G_{\mathbb R}&G_{\mathbb R}\\
\mathbb R,\ m\ {\rm odd}&X_{11}G_{\mathbb R}&X_{11}G_{\mathbb R}\\
\mathbb C,\ {\rm holomorphic}&\bar X_{11}^mG_{\mathbb C}&X_{11}^mG_{\mathbb C}\\
\mathbb C,\ {\rm antiholomorphic}&X_{11}^mG_{\mathbb C}&\bar X_{11}^mG_{\mathbb C}.
\end{array}
\tag{1.30ae}
\]
The real transform is the differentiated Gaussian transform. In the
complex case successive Wirtinger differentiation of the Gaussian
introduces no contractions, giving degree-\(m\) phase \((-i)^m\).
Use \(c^\vee(X)=c(X^{-1})\) for the attaining coefficient of
Section 4. Equation (1.30g) and (1.30p), (1.30r) or (1.30t) now show
that \((\Phi^\vee,c^\vee)\) attains the dual generator with the same
nonzero constant. The dual analogue of (1.30u), with coefficient degree
\(-m\) and norm exponent \(-t\), proves polynomial-module stability.
Together with Section 5 this finishes the exact dual Gaussian ideal.

Fourier inversion gives the equation for the dual representation too.
Its phase must be \(\omega_\pi(-I)/\epsilon_\pi\). Here
\(\omega_\pi(-I)=(-1)^m\), so this is \((-i)^e\) over \(\mathbb R\)
and \((-i)^m\) over \(\mathbb C\). Thus the two phases multiply to
the required central sign.

#### Standard character data and canonical dual/conjugation

These gamma factors agree with the Tate factors of an explicit
normalized Borel embedding, without using an all-rank classification.
Let \(B\) be upper triangular and
\(\delta_B^{1/2}(b)=\prod_j|b_{jj}|_F^{\rho_j}\).
The functional taking the \(e_n^{\otimes m}\)-coordinate obeys
\(\ell(\operatorname{Sym}^m(b)v)=b_{nn}^m\ell(v)\).
The map
\[
v\longmapsto f_v(g)=\ell(\pi_{m,t}(g)v)
\tag{1.30af}
\]
therefore embeds (1.30d) into smooth normalized Borel induction with
characters
\[
\chi_n(x)=x^m|x|_F^{\,t-\rho_n},\qquad
\chi_j(x)=|x|_F^{\,t-\rho_j}\quad(j<n).
\tag{1.30ag}
\]
It is injective because the representation is irreducible and \(\ell\ne0\).
The scalar action and differentiated action in (1.30af) are actual smooth
group actions. On the compact group the embedding is continuous,
and finite dimensionality gives a closed image.

The unordered multiset (1.30ag) consists of
\[
x^m|x|_F^{\,t+\rho_1},
\quad |x|_F^{\,t+\rho_2},\ldots,|x|_F^{\,t+\rho_n}.
\tag{1.30ah}
\]
The first real character is
\(\operatorname{sgn}(x)^e|x|^{t+\rho_1+m}\).
Its Tate factor is the first real factor of (1.30e).
The first complex character has angular weight \(m\) and radial
exponent \(t+\rho_1+m/2\); its Tate factor is the first complex factor
of (1.30e). Antiholomorphic conjugation changes angular weight to
\(-m\), whose absolute angular degree is still \(m\).
Thus the direct matrix ideal calculation has proved exactly these
Tate-product factors, and not merely a gamma product with unspecified
shifts.

For the dual representation, the functional taking the first symmetric
coordinate transforms under \(B\) by \(b_{11}^{-m}\).
The same embedding construction gives
\[
\chi'_1(x)=x^{-m}|x|_F^{-t-\rho_1},\qquad
\chi'_j(x)=|x|_F^{-t-\rho_j}\quad(j>1).
\tag{1.30ai}
\]
This multiset is the inverse of (1.30ag). The real special factor has
parity \(e\) and radial exponent \(-t-\rho_1-m\), giving (1.30f).
The complex special factor has angular weight \(-m\) and radial
exponent \(-t-\rho_1-m/2\); its absolute angular shift cancels the
\(-m/2\), giving \(B_{\mathbb C}(s-t)\).
Replacing the absolute angular degree by its signed value would
produce a wrong dual factor. The product of the actual scalar Tate
phases is precisely (1.30g).

These particular embeddings and the direct integral calculations identify the matrix factors with the stated Tate products for the explicit family. They do not assert that an arbitrary irreducible
subquotient of a Borel induction has that induction's entire product
as its matrix generator.

Gamma conjugation is exact, since the Euler integral and continuation
prove \(\overline{\Gamma(\bar z)}=\Gamma(z)\).
Over \(\mathbb R\), conjugation sends \(t\) to \(\bar t\);
over \(\mathbb C\), it additionally interchanges the holomorphic and
antiholomorphic families. Equations (1.30e)–(1.30f) thus give
\[
L_{\bar\pi}(s)=\overline{L_\pi(\bar s)},\qquad
L_{\overline{\pi^\vee}}(s)=\overline{L_{\pi^\vee}(\bar s)}
\tag{1.30aj}
\]
with no undetermined exponential or scalar.
The phases satisfy
\(\epsilon_{\bar\pi}=\omega_\pi(-I)\overline{\epsilon_\pi}\),
as also follows by conjugating the Fourier kernel.

If \(n>1\) and \(m>0\), (1.30d) admits no invariant positive Hermitian
form: \(\operatorname{diag}(e^r,e^{-r},1,\ldots,1)\), of determinant
one, has symmetric-power eigenvalues \(e^{mr}\) and \(e^{-mr}\).
A unitary operator has eigenvalues of modulus one, so \(r\ne0\)
contradicts unitarity. For \(n=1\), unitarity is exactly
\(\operatorname{Re}t=-m\) over \(\mathbb R\) and
\(\operatorname{Re}t=-m/2\) over \(\mathbb C\).
In those cases (1.30e)–(1.30f) explicitly yield
\[
L_{\pi^\vee}(s)=\overline{L_\pi(\bar s)},\qquad
|\epsilon_\pi|=1 .
\tag{1.30ak}
\]
For \(m=0\), the unitary condition is \(\operatorname{Re}t=0\) in
every rank, and the same identity follows by the symmetry of
the \(\rho_j\)'s. This treats every unitary member of the explicit family.

Finally, for \(\psi_b(x)=\psi_F(bx)\), self-dual matrix measure changes
by \(|b|_F^{n^2/2}\), and
\(\widehat\Phi^{\,\psi_b}(Y)=|b|_F^{n^2/2}\widehat\Phi^{\,\psi_F}(bY)\).
Substitute \(X=bY\) in the dual integral. Since
\(\omega_\pi(bI)=b^m|b|_F^{nt}\) for the holomorphic or real family,
this gives
\[
\epsilon_\pi(s,\psi_b)=
\omega_\pi(bI)|b|_F^{n(s-1/2)}\epsilon_\pi.
\tag{1.30al}
\]
Use \(\bar b^m|b|_F^{nt}\) for the antiholomorphic family.
At \(s=1/2\) this retains absolute value one for every unitary member.
An arbitrary determinant norm twist shifts \(s\) as displayed in
(1.30e)–(1.30f).

The proof has established a complete canonical Gaussian and whole-Schwartz
matrix package for symmetric powers, their antiholomorphic companions,
their duals and all norm twists in every real and complex rank.
The general infinite-dimensional irreducible generator and the general
higher-rank standard-module factor identification remain separate.

### Determinant differential operators and the full archimedean matrix family

Let \(F=\mathbb R\) or \(\mathbb C\), let \(d=[F:\mathbb R]\),
and put \(G=GL_n(F)\), \(K=O(n)\) or \(U(n)\).
Write \(\nu(g)=|\det g|_F=|\det g|^d\).
Fix an additive Haar measure \(dX\) on \(M_n(F)\) and
\(dg=c_F\nu(g)^{-n}dX\), with \(c_F>0\).

Here is the precise realization hypothesis. The representations \(V,W\)
are complete Fréchet smooth representations of \(G\), with continuous
moderate-growth action and a continuous invariant bilinear pairing
\[
B:V\times W\longrightarrow\mathbb C.
\tag{1.25a}
\]
Their \(K\)-finite cores \(V_0,W_0\) are respectively an irreducible
admissible \((\mathfrak g,K)\)-module and its algebraic admissible
contragredient, and \(B\) restricts to that duality. Invariance means
\(B(\pi(g)v,\widetilde\pi(g)w)=B(v,w)\).
For every continuous seminorm \(p\) on \(V\), moderate growth means that
\[
p(\pi(g)v)\le C\bigl(1+\|g\|+\|g^{-1}\|\bigr)^N p'(v)
\tag{1.25b}
\]
for some continuous seminorm \(p'\), integer \(N\), and constant \(C\);
the analogous condition holds on \(W\).
These are conditions on actual supplied realizations. Their existence
and comparison for an abstract module are not inferred here.

Put \(c_{v,w}(g)=B(\pi(g)v,w)\), and
\[
Z_\pi(s,\Phi;v,w)=
\int_G\Phi(g)c_{v,w}(g)\nu(g)^{s+(n-1)/2}\,dg.
\tag{1.25c}
\]
The integral always uses the whole Schwartz space, not just its
Gaussian-polynomial subspace.

#### Dense cores and scalar central operators

The cores \(V_0,W_0\) are dense. To see this, average a vector over a
continuous probability kernel on \(K\) supported in a sufficiently
small identity neighbourhood. Continuity of its compact orbit makes
the average tend to the vector in every prescribed finite list of
seminorms. Uniformly approximate the kernel by a finite sum of compact
matrix coefficients. This is the actual proved Peter–Weyl theorem in
*Matrix coefficients and the Peter–Weyl theorem*, Theorem 4.1.
The error in a seminorm \(p\) is at most the uniform kernel error times
\(\sup_{k\in K}p(\pi(k)v)\). A finite coefficient kernel has image in a
finite sum of \(K\)-types, hence in \(V_0\). Successively treating the
first \(j\) seminorms gives a sequence converging to \(v\). The proof
on \(W\) is identical.

Every endomorphism of \(V_0\) commuting with \((\mathfrak g,K)\) is a
scalar. Indeed, it preserves a nonzero finite-dimensional
\(K\)-isotypic component. An eigenvector there supplies a nonzero
kernel of \(T-\lambda\). That kernel is a submodule, so irreducibility
makes it all of \(V_0\). A central complexified enveloping element
is fixed by the adjoint action of \(K\) in these matrix groups:
the complex group \(GL_n(\mathbb C)\) is generated by elementary
unipotents and diagonal matrices, all complex exponentials,
and a central element is fixed by each exponential. The real
compact group is contained in this complex group; for the
complex group regarded as real apply this observation to
both complexified summands. Thus the central operator does
commute with the full \(K\), including its real disconnected
component. In particular the centre
\(Z(U(\mathfrak g_\mathbb C))\) acts by a character.
Continuity of differentiation and density extend each scalar central
identity to \(V\). The same statements hold for \(W\).

The admissible contragredient is simple: the annihilator of a proper
submodule of \(W_0\) is a nonzero submodule of \(V_0\). Nonzeroness
follows on a \(K\)-type on which the submodule is proper, since the
pairing of corresponding finite-dimensional isotypic components is
perfect. Invariance makes the annihilator a submodule. Thus it is
all of \(V_0\), and the original submodule is zero.

The central group elements also act scalarly: they preserve the core
and commute with \((\mathfrak g,K)\). Density extends the result to
the realization. Denote the resulting group character by
\(\omega_\pi\).

#### A central determinant operator

For real matrices put
\[
D=\det\left(\frac{\partial}{\partial x_{ij}}\right),\qquad
C=(\det X)D.
\tag{1.25d}
\]
For complex matrices use Wirtinger derivatives and put
\[
D_+=\det(\partial/\partial z_{ij}),\quad
D_-=\det(\partial/\partial\bar z_{ij}),\quad
C_+=(\det Z)D_+,\quad C_-=(\overline{\det Z})D_-.
\tag{1.25e}
\]
On \(G\), \(C\), respectively \(C_+,C_-\), are central invariant
differential operators.

Here is a proof that does not assume a Capelli formula. The chain
rule gives
\[
D\bigl(f(aXb)\bigr)=(\det a)(\det b)(Df)(aXb).
\tag{1.25f}
\]
Multiplication by \(\det X\) cancels these two determinant factors,
so \(C\) commutes with both translations. The holomorphic and
antiholomorphic chain rules give the same assertions for \(C_+,C_-\).
Every left-invariant differential operator is an element of the
enveloping algebra of right differentiations: choose an ordered Lie
basis, subtract the ordered products with its principal symbol at
the identity, and repeat at lower orders. Its coefficients are
determined everywhere by left invariance. A bi-invariant operator
then commutes with every right first derivative, so its enveloping
element is central. This also proves the assertion for the two
complexified summands in
\(\mathfrak{gl}_n(\mathbb C)_{\mathbb R}\otimes\mathbb C
 \simeq\mathfrak{gl}_n(\mathbb C)\oplus\mathfrak{gl}_n(\mathbb C)\).

Twist the differentiated representation by \(\nu^t\).
In the real case this replaces \(d\pi(A)\) by
\(d\pi(A)+t\operatorname{tr}(A)\); in the complex case it makes that
replacement on each complexified summand. The central operators
therefore act by polynomials
\[
b_\pi(t),\qquad b_{\pi,+}(t),\quad b_{\pi,-}(t).
\tag{1.25g}
\]
Each polynomial is monic of degree \(n\). Polynomiality follows by
substitution in an enveloping element of order \(n\). Its leading
coefficient is the principal symbol on the trace functional: at
\(X=I\), \(\partial_{ij}\log\det X=\delta_{ij}\), and the determinant
of that diagonal derivative matrix is one.

In particular, on the invertible locus,
\[
D\bigl(c(X)|\det X|^t\bigr)
=b_\pi(t)(\det X)^{-1}c(X)|\det X|^t .
\tag{1.25h}
\]
The sign character is locally constant, so a second application
gives
\[
D^2\bigl(c(X)|\det X|^{t+2}\bigr)
=b_\pi(t+2)b_\pi(t+1)c(X)|\det X|^t .
\tag{1.25i}
\]
For complex matrices, \(D_+\) does not differentiate an
antiholomorphic determinant. Consequently
\[
D_+D_-\bigl(c(Z)|\det Z|^{2(t+1)}\bigr)
=b_{\pi,+}(t+1)b_{\pi,-}(t+1)c(Z)|\det Z|^{2t}.
\tag{1.25j}
\]
Neither identity assumes that the representation is a principal
series, tempered, spherical, finite dimensional or unitary.

#### Bounds and distributional integration by parts

**Lemma 1.21a.** In a sufficiently far right half-plane, (1.25c) converges
absolutely, is holomorphic, and satisfies bounds
\[
\sup_{s\in\Omega}|Z_\pi(s,\Phi;v,w)|
\le C_\Omega\,p_\Omega(\Phi)\,p_V(v)\,p_W(w)
\tag{1.25k}
\]
on each compact parameter set \(\Omega\) there. The same assertion
holds with any fixed number of parameter derivatives.

**Proof.** Continuity of \(B\) bounds it by a product of seminorms.
Applying (1.25b) yields a uniform polynomial bound for \(c_{v,w}\).
Adjugates give
\[
1+\|X\|+\|X^{-1}\|
\le C_n(1+\|X\|)^n(1+|\det X|^{-1}).
\tag{1.25l}
\]
Since the additive density of (1.25c) is
\(c_Fc_{v,w}(X)|\det X|^{d(s-(n+1)/2)}\), a sufficiently large real
part makes its possible negative determinant power disappear.
The remaining bound is a polynomial in \(\|X\|\), absorbed by a
Schwartz seminorm. This proves absolute convergence and (1.25k).
Parameter differentiation adds powers of \(d\log|\det X|\).
Near zero, \(x^\epsilon|\log x|^j\) is bounded for every
\(\epsilon>0\); at infinity an extra polynomial weight absorbs the
logarithm. Dominated differentiation proves holomorphy and the
derivative assertions. \(\square\)

For clarity, integration by parts across the singular matrices
needs justification. Every coordinate derivative of \(c(X)\) is a
finite sum of coefficients of differentiated vectors, with
polynomial expressions in the entries of \(X^{-1}\). This follows
by writing an additive coordinate tangent at \(X\) as a right
tangent \(XA\), where \(A=X^{-1}\dot X\), and iterating the chain
rule. For each fixed derivative order, (1.25l), moderate growth
and the derivative seminorms therefore give another bound by a
polynomial in \(\|X\|\) times a finite negative determinant power.
The same is true after differentiating
\(|\det X|^{dt}\).

Take \(\operatorname{Re}t\) sufficiently large for all derivatives
up to order \(2n\). On every compact set, these derivatives tend
to zero at the singular locus. Extending the function by zero
there gives a \(C^{2n}\) function. One elementary verification is
to restrict to coordinate lines on which the determinant
polynomial is not identically zero. Such lines have finitely many
singular points; the fundamental theorem of calculus, and the
vanishing one-sided derivatives, prove the derivative identity
across them. Lines of this kind are dense among parallel lines,
because the determinant polynomial is not identically zero on
any open set. Continuity then proves the derivative identity on
every line, successively up to order \(2n\).

These extended derivatives have polynomial growth at infinity.
Integrate first with a compact cutoff and then let its radius
tend to infinity; all cutoff terms tend to zero against a
Schwartz test. Thus (1.25i) and (1.25j) hold as distributional
identities in a far right half-plane. The transposed differential
operator has the same sign: its total order is \(2n\).

Put \(c_n=(n+1)/2\), and define
\[
(a,A,B_\pi(s))=
\begin{cases}
(2,D^2,b_\pi(s-c_n+2)b_\pi(s-c_n+1)),&F=\mathbb R,\\
(1,D_+D_-,b_{\pi,+}(s-c_n+1)b_{\pi,-}(s-c_n+1)),
&F=\mathbb C.
\end{cases}
\tag{1.25m}
\]
Then
\[
B_\pi(s)Z_\pi(s,\Phi;v,w)
=Z_\pi(s+a,A\Phi;v,w).
\tag{1.25n}
\]
This is initially a proved integral identity, not a presupposed
functional equation.

#### A common gamma majorant for every smooth coefficient

**Theorem 1.21.** Factor the monic degree-\(2n\) polynomial
\(B_\pi(s)=\prod_{\ell=1}^{2n}(s-\beta_\ell)\), including
multiplicities, and put
\[
H_\pi(s)=\prod_{\ell=1}^{2n}
\Gamma\left(\frac{s-\beta_\ell}{a}\right).
\tag{1.25o}
\]
For all \(\Phi\in\mathcal S(M_n(F)),v\in V,w\in W\),
\[
Z_\pi(s,\Phi;v,w)=H_\pi(s)Q_\pi(s,\Phi;v,w),
\tag{1.25p}
\]
where \(Q_\pi\) is entire in \(s\), trilinear, and obeys a bound
of the form (1.25k) on every compact subset of \(\mathbb C\).
Thus (1.25c) has meromorphic continuation as a continuous tempered
family with a fixed gamma pole majorant in every rank.
On any closed vertical strip, after removing its finitely many
possible poles by a fixed polynomial, the resulting family
decreases faster than every inverse power of
\(1+|\operatorname{Im}s|\), with joint seminorm bounds.

**Proof.** The gamma recurrence gives exactly
\[
H_\pi(s+a)=a^{-2n}B_\pi(s)H_\pi(s).
\tag{1.25q}
\]
The gamma poles, entire reciprocal and absence of zeros are the
actual scalar proofs in *Tate’s local theory at the infinite places*, “Mellin continuation without a functional equation”.
No general representation-theoretic local factor is imported
from that scalar result.

Choose a right half-plane beyond all roots of \(B_\pi\) and
all thresholds used above. There \(Z/H_\pi\) is holomorphic, and
(1.25n) becomes
\[
Q_\pi(s,\Phi)=a^{-2n}Q_\pi(s+a,A\Phi).
\tag{1.25r}
\]
For a compact parameter set choose \(N\) so that its translate
by \(Na\) lies in this half-plane, and define
\[
Q_\pi(s,\Phi;v,w)
=a^{-2nN}
\frac{Z_\pi(s+Na,A^N\Phi;v,w)}{H_\pi(s+Na)}.
\tag{1.25s}
\]
Increasing \(N\) does not change this expression, by (1.25r)
in the original half-plane. These formulas therefore patch to
an entire family. The differential operator \(A^N\) is continuous
on the Schwartz space. Lemma 1.21a bounds the numerator uniformly
on a compact set, and \(1/H_\pi\) is bounded there. This proves
the required joint seminorm bounds. Meromorphic continuation
and uniqueness follow from agreement with the original integral
in its convergence domain.

For the strip assertion, a bounded real-part interval meets
only finitely many poles of the finitely many gamma factors
in (1.25o). Choose a polynomial \(P_{\mathrm{strip}}\)
canceling these poles with their full possible multiplicities.
Iteration of the already proved meromorphic identity (1.25n)
gives
\[
Z_\pi(s,\Phi;v,w)=
\frac{Z_\pi(s+Na,A^N\Phi;v,w)}
{\prod_{k=0}^{N-1}B_\pi(s+ka)}.
\tag{1.25sa}
\]
Choose \(N\) large enough to put the entire shifted strip
in the absolute-convergence domain. The modulus of
\(\nu(g)^{i\operatorname{Im}s}\) is one, so the numerator
is bounded uniformly in the imaginary part by a fixed
Schwartz seminorm and the same coefficient seminorms
used in Lemma 1.21a. For large imaginary part the denominator
is bounded below by a positive constant times
\((1+|\operatorname{Im}s|)^{2nN}\).
Increasing \(N\) makes this dominate the degree of
\(P_{\mathrm{strip}}\) and any prescribed inverse power.
On the remaining compact part of the strip,
\(P_{\mathrm{strip}}H_\pi Q_\pi\) is holomorphic and has
the previously proved local seminorm bound.
This proves the strip assertion, without assuming
a functional equation. \(\square\)

The factor \(H_\pi\) is a **majorant**, not the canonical standard
gamma generator. Confusing these would create a false proof.
For instance, in rank one with trivial real character,
\[
B(s)=s(s+1),\quad
H(s)=\Gamma(s/2)\Gamma((s+1)/2),\quad
Z(s,e^{-\pi x^2})=\pi^{-s/2}\Gamma(s/2).
\tag{1.25t}
\]
Its quotient by \(H\) is
\(\pi^{-s/2}/\Gamma((s+1)/2)\). It has infinitely many zeros and
is not a polynomial. Taking a polynomial gcd of these majorant
quotients would not be legitimate.

#### The exact Gaussian-to-Schwartz division lemma

Let \(\mathcal S_0\) be the span of the polynomial multiples of
\(e^{-\pi\operatorname{tr}(XX^t)}\) over \(\mathbb R\), or of
\(e^{-2\pi\operatorname{tr}(XX^*)}\) over \(\mathbb C\).
It is dense in \(\mathcal S(M_n(F))\). The actual proof is
*Hermite functions, tempered distributions and the Schwartz kernel theorem*, Lemma 3.1 and Theorem 3.2.
After a real scalar dilation, its finite Hermite sums are exactly
Gaussian-polynomial tests in the real coordinates; complex
polynomials in \(Z,\bar Z\) are the same polynomial algebra.
That theorem proves convergence in every Schwartz seminorm,
not merely \(L^2\) density.

**Proposition 1.21b (conditional canonical division, with the
missing hypothesis isolated).** Suppose a nonzero meromorphic
function \(L_\pi(s)\) has the following *Gaussian ideal* property:
\[
\operatorname{span}_{\mathbb C}
\{Z_\pi(s,\Phi;v,w):
\Phi\in\mathcal S_0,\ v\in V_0,\ w\in W_0\}
=L_\pi(s)\mathbb C[s].
\tag{1.25u}
\]
Then every full-Schwartz, full-smooth-vector quotient
\(Z_\pi/L_\pi\) is entire, with local joint seminorm bounds.
Moreover \(L_\pi\) has no zeros.

**Proof.** Equality (1.25u) supplies a finite attaining family:
\(L_\pi=\sum_{i=1}^r Z_\pi(\Phi_i;v_i,w_i)\).
Theorem 1.21 therefore shows that
\[
h_\pi(s)=L_\pi(s)/H_\pi(s)
\tag{1.25v}
\]
is an entire nonzero function. For every Gaussian-core test,
\(Q_\pi=h_\pi P\) with \(P\in\mathbb C[s]\).

Approximate \(\Phi,v,w\) in their respective topologies by
Gaussian-polynomial and core vectors. Theorem 1.21's joint
compact-parameter bounds make the corresponding \(Q_\pi\)'s
converge locally uniformly in \(s\). If \(h_\pi\) has a zero of
order \(m\) at \(s_0\), all approximating functions and their
first \(m-1\) derivatives vanish there. Cauchy's formula makes
the derivatives converge too. The limit is divisible by
\((s-s_0)^m\). Consequently \(Q_\pi/h_\pi\), and hence
\(Z_\pi/L_\pi\), is entire.

This also proves continuity, rather than just pointwise division.
On a sufficiently small circle about \(s_0\), \(h_\pi\) has no
zeros. For \(s\) inside the circle the entire quotient equals
the Cauchy integral of \(Q_\pi(\zeta)/h_\pi(\zeta)\).
Theorem 1.21 bounds that integral by fixed Schwartz and vector
seminorms. Away from the isolated zeros, divide directly by the
nonvanishing \(h_\pi\). A finite cover treats every compact
parameter set.

Finally, at any prescribed \(s_0\), choose a coefficient nonzero
at some \(g_0\). Take a nonnegative bump \(\eta\) supported in a
small compact subset of \(G\), where that coefficient is nonzero,
and set
\[
\Phi(g)=\eta(g)\overline{c_{v,w}(g)}
\nu(g)^{-i\operatorname{Im}s_0}.
\tag{1.25w}
\]
It extends by zero to a Schwartz function on the matrix space.
The entire compact-support integral at \(s_0\) is strictly
positive, up to the fixed positive Haar constant.
If \(L_\pi\) had a zero there, the entire division just proved
would force every such integral to vanish. This contradiction
proves the absence of zeros. \(\square\)

The hypothesis (1.25u) has not been proved for a general
irreducible representation here. Theorem 1.21 does not imply it:
its normalized functions lie in \(\mathcal O(\mathbb C)\),
not necessarily in \(\mathbb C[s]\). Proposition 1.21b supplies
the full continuity and multiplicity-sensitive density argument
once a genuine Gaussian generator and finite attaining family
have been established.

### A scalar Fourier equation for all archimedean matrix coefficients

Use the actual smooth dual-pair realizations, measures and integrals
(1.25a)–(1.25c) of *Determinant differential operators and the full
archimedean matrix family*. The argument below supplies a meromorphic
scalar Fourier equation in all ranks over \(\mathbb R,\mathbb C\).
It does not identify the canonical Gaussian generator.

Fix a nontrivial unitary additive character \(\psi\), its self-dual
additive measure, and the positive-trace convention
\[
\widehat\Phi(Y)=\int_{M_n(F)}\Phi(X)\psi(\operatorname{tr}(XY))\,dX.
\tag{1.26a}
\]
The actual whole-space Schwartz continuity and inversion proof is
*Additive characters, self-dual measures and Poisson summation on the adèles*, Proposition 5.2 and Lemma 5.4A, applied in real dimension \(dn^2\).
Trace permutes the matrix coordinates, so
\(\widehat{\widehat\Phi}(X)=\Phi(-X)\).

#### Finite central algebra on unipotent coinvariants

**Lemma 1.22a.** Let \(\mathfrak g=\mathfrak{gl}_n(\mathbb C)\),
and let \(\mathfrak p=\mathfrak l+\mathfrak u\) be the two-block
upper parabolic of sizes \(r,m=n-r\). If the centre of
\(U(\mathfrak g)\) acts on a module \(M\) by a character
\(\alpha\), there is a monic polynomial \(q_{\alpha,r}\) such that
\[
q_{\alpha,r}(z_m)(M/\mathfrak uM)=0,\qquad
z_m=\operatorname{diag}(0_r,I_m).
\tag{1.26b}
\]
For \(\mathfrak{gl}_n(\mathbb C)\) regarded as a real Lie algebra
the same assertion holds for the sum of the two complexified
block-centre elements.

**Proof.** Ordered monomials in a Lie basis span its enveloping
algebra by replacing inverted pairs \(YX\) by \(XY+[Y,X]\).
They are independent for the Lie algebras here: realize them as
invariant differential operators on the corresponding complex
matrix group. Their highest symbols at the identity are the
independent commutative tangent monomials. Descending through
the orders proves independence. This proves the required PBW
decomposition, in particular
\[
U(\mathfrak g)
=U(\mathfrak u)\,U(\mathfrak l)\,U(\mathfrak u^-)
\quad\text{as an ordered vector-space decomposition.}
\tag{1.26c}
\]
Its centres have associated graded algebras
\[
\operatorname{gr}Z(U(\mathfrak{gl}_a))
=S(\mathfrak{gl}_a)^{GL_a}
=\mathbb C[e_1,\ldots,e_a].
\tag{1.26d}
\]
Indeed, a central highest symbol is invariant. Conversely
symmetrization intertwines the adjoint Lie action, so an
invariant polynomial symmetrizes to a central element with
that symbol. For the last equality restrict to diagonal
matrices: the dense open set of distinct-eigenvalue matrices
is diagonalizable, so restriction is injective; permutation
invariance makes the restriction symmetric. Successively
subtracting products of elementary symmetric functions with
the same lexicographic leading monomial expresses every such
polynomial in the \(e_i\)'s. These extend as characteristic-
polynomial coefficients.

Project a central element onto its \(U(\mathfrak l)\) term in
(1.26c), and call the projection \(\Gamma\). Every other term
lies in \(\mathfrak uU(\mathfrak g)\). To see this, use a
block-centre element whose adjoint weights are positive on
\(\mathfrak u\) and negative on \(\mathfrak u^-\). A
weight-zero ordered monomial containing a negative part
must contain a positive part. Thus
\[
z-\Gamma(z)\in\mathfrak uU(\mathfrak g).
\tag{1.26e}
\]
Projection is \(\mathfrak l\)-equivariant, so \(\Gamma(z)\)
is central in \(U(\mathfrak l)\).
It is an algebra homomorphism on the centre: the right
ideal \(\mathfrak uU(\mathfrak g)\) is preserved by left
multiplication by \(U(\mathfrak l)\); use (1.26e) on two
factors and project their product. Its leading-symbol
map is restriction to block diagonal matrices.

The algebra \(Z(U(\mathfrak l))\) is a finite module over
\(\Gamma Z(U(\mathfrak g))\). Here are the details.
The block invariant polynomial ring is
\(\mathbb C[x_1,\ldots,x_n]^{S_r\times S_m}\).
Each \(x_i\) satisfies the degree-\(n\) monic polynomial
with the full symmetric coefficients. Reducing every
power \(x_i^n\) shows that the monomials with each exponent
\(<n\) span the entire polynomial ring over the full
symmetric ring. Average this finite set over \(S_r\times S_m\).
Its averages span the block invariant ring, because the
coefficients in the full symmetric ring are already
invariant. Lift these homogeneous averages to central
elements of \(U(\mathfrak l)\) by (1.26d), and lift the full
elementary symmetric generators to \(Z(U(\mathfrak g))\).
Subtract a lifted expression for the highest symbol
and repeat at lower filtered degree. Induction proves
finite generation of the central enveloping algebra.

By (1.26e), \(\Gamma(z)\) acts on \(M/\mathfrak uM\) as
\(\alpha(z)\). The quotient central algebra by these
scalar relations is finite dimensional. Multiplication
by \(z_m\) obeys its monic characteristic polynomial;
that polynomial acts as zero on every module over the
quotient. This proves (1.26b). If the quotient is zero,
use the polynomial \(1\).
For the complex group regarded as real, apply the
argument to both complexified summands. Their tensor
product central quotient is finite dimensional, and
the sum of the block-centre elements again obeys its
monic characteristic polynomial. \(\square\)

This statement applies to the entire supplied smooth
realization as a Lie module: central scalar identities
extend from its dense core by continuity. No smooth/core
coinvariant comparison or Jacquet admissibility is assumed.

#### Relative descent and normal jets

**Lemma 1.22b (relative descent).** Let \(H\) be a unimodular
Lie group, \(P\) a closed subgroup, \(E\) a complete locally
convex smooth \(H\)-module, and \(J\) a finite-dimensional
\(P\)-module with action \(\tau\).
Assume the orbit projection has local smooth product
sections. In the application below these are the
explicit minor-chart sections (1.26l).
Jointly continuous relative functionals on compactly
supported smooth sections of \(H\times_PJ\), together
with \(E\), are in bijection with continuous \(\lambda\)
on \(E\otimes J\) satisfying
\[
\lambda(\sigma(p)e\otimes\tau(p)j)
=\chi(p)\delta_P(p)\lambda(e\otimes j),\qquad
\delta_P(p)=|\det(\operatorname{Ad}(p);\operatorname{Lie}P)|.
\tag{1.26f}
\]

**Proof.** For left Haar measure on \(P\),
\(\int f(tp)\,dt=\delta_P(p)\int f(t)\,dt\).
In exponential coordinates the conjugation Jacobian
is the displayed determinant; right translation is
the composition of left translation and conjugation.
This fixes the modular sign.

A lifted test \(\Psi\in C_c^\infty(H,J)\) maps to the section
whose value in the frame \(h\) is
\[
Q\Psi(h)=\int_P\tau(p)\Psi(hp)\,dp.
\tag{1.26g}
\]
It obeys \(Q\Psi(hp_0)=\tau(p_0)^{-1}Q\Psi(h)\).
Use the supplied local smooth product sections.
A finite partition of unity on each compact support,
and a compact fibre bump of integral one, show
that \(Q\) is onto. The partitions needed here can
be constructed in the Euclidean orbit charts:
choose finitely many smooth compact bumps whose
positive sets cover the compact support, and divide
them by their positive sum.

Its kernel is the closed span of
\[
R_p\Psi-\delta_P(p)\tau(p)^{-1}\Psi.
\tag{1.26h}
\]
Here is the local kernel calculation. In a real coordinate
rectangle, a compact scalar test with zero integral is
a sum of compactly supported coordinate derivatives:
choose unit-mass one-variable bumps, successively
subtract each marginal times its bump, and take the
compact primitive of each zero-marginal remainder.
Insert the Haar density to obtain Haar divergences.
Right-invariant Lie fields span the tangent space;
expressing a vector field in that frame makes its
Haar divergence a sum of right Lie derivatives with
their constant modular correction. Each corrected
derivative is the limit of differences in (1.26h).
A finite partition of unity handles compact support.
The integrals of the pieces are moved to one fixed
bump through overlapping charts in a component;
right translation also moves between components,
with precisely the factor \(\delta_P\). For the
\(J\)-valued version apply this argument componentwise
after multiplication by \(\tau(p)\). In local product
charts this is exactly the condition of zero fibre
integral in (1.26g). Finite partitions on the base prove
the stated kernel.

The lifted relative functional has the regular-group form
\[
D(\Psi,e)=\int_H
\chi(h)\lambda(\sigma(h)^{-1}e\otimes\Psi(h))\,dh.
\tag{1.26i}
\]
To derive it, permit compact smooth \(E\otimes J\)-valued
tests and conjugate the diagonal regular action by
\((JF)(h)=\chi(h)^{-1}\sigma(h)F(h)\).
The relative functional composed with \(J\) is left
invariant. A scalar left-invariant distribution is
a multiple of Haar integration: convolve it with a
compact smooth approximate identity. Invariance makes
each convolution a constant smooth function. Testing
one fixed unit-mass test makes those constants
converge; convergence of the convolutions to the
distribution proves the claim. Apply it to every
fixed vector, obtaining a continuous \(\lambda\),
and undo \(J\). This gives (1.26i).

The vector-valued extension just used can be checked
without assuming a nuclearity theorem. In a compact
coordinate cube, cut off and periodize a smooth
vector-valued test. Its Fourier coefficients in any
continuous seminorm decrease faster than every power:
integrate by parts sufficiently many times.
Taking that order larger than the dimension plus
the distribution order gives an absolutely
convergent sum of finite vector-valued Fourier tests
for the relevant seminorm and derivatives. A joint
bound therefore extends the functional uniquely.
For the coefficient variables one uses the completed
projective tensor, whose seminorm on a finite tensor
is the infimum of \(\sum_i p(v_i)q(w_i)\); the same
estimate proves the extension there.

Finally, (1.26i) kills (1.26h) exactly when
\[
\chi(p)^{-1}\lambda(\sigma(p)e\otimes j)
=\delta_P(p)\lambda(e\otimes\tau(p)^{-1}j).
\]
Replace \(j\) by \(\tau(p)j\) to get (1.26f).
Conversely that equation makes (1.26i) descend by the
proved kernel statement. All estimates are continuous
on compact supports. \(\square\)

**Lemma 1.22c (normal jets).** A distribution supported on a
smooth closed submanifold and locally of order at most
\(N\) depends only on its first \(N\) normal jets.
Its highest nonzero normal part is a distribution
on the submanifold with the dual of
\(\operatorname{Sym}^j(N^*)\), for some \(j\le N\).
The assertion includes jointly continuous coefficient
variables.

**Proof.** Write the submanifold locally as \(y=0\)
in coordinates \((x,y)\). A test whose normal
derivatives through order \(N\) vanish is, by
Taylor's integral remainder, a sum of
\(y^\alpha f_\alpha\), \(|\alpha|=N+1\).
Multiply by a cutoff supported in \(|y|<2\epsilon\)
and equal to one in \(|y|<\epsilon\).
Support makes the distribution value unchanged.
Every derivative through order \(N\) of the
cutoff remainder is \(O(\epsilon)\), so the
order bound makes the value tend to zero.
Arbitrary finite jets are attained by
\(\chi(y)\sum y^\alpha f_\alpha(x)/\alpha!\).
The highest normal degree transforms under
coordinate change by the induced normal-bundle
action. This proves the assertion. Its estimates
carry the unchanged coefficient seminorms, which
proves the vector-valued assertion too. \(\square\)

#### Rank strata and generic uniqueness

Let \(H=G\times G\) act on matrices by \(aXb^{-1}\),
on tests by \(\rho(a,b)\Phi(X)=\Phi(a^{-1}Xb)\), and
on \(E=W\widehat\otimes V\) by
\[
\sigma(a,b)=\widetilde\pi(a)\otimes\pi(b).
\quad
u_s=s+\frac{n-1}{2},\qquad
\chi_s(a,b)=(\nu(a)/\nu(b))^{u_s}.
\tag{1.26j}
\]
The tensor completion encodes the joint coefficient
seminorm bounds, rather than any representation-
theoretic tensor classification.

The rank-\(r\) orbit has base point
\(x_r=\operatorname{diag}(I_r,0_m)\), with stabilizer
\[
a=\begin{pmatrix}A&B\\0&D\end{pmatrix},\qquad
b=\begin{pmatrix}A&0\\C&D'\end{pmatrix}.
\tag{1.26k}
\]
It is a smooth orbit, with explicit sections on
invertible-minor charts:
\[
\begin{pmatrix}U&V\\W&WU^{-1}V\end{pmatrix}
=\begin{pmatrix}U&0\\W&I_m\end{pmatrix}
x_r
\begin{pmatrix}I_r&U^{-1}V\\0&I_m\end{pmatrix}.
\tag{1.26l}
\]
Permuting rows and columns covers the orbit.
The projective tensor action is smooth: on finite tensors its
derivatives are the finite Leibniz sums of the continuous
derivative operators on \(V,W\). On a compact group-coordinate
set their seminorm bounds extend to the tensor completion.
Approximate by finite tensors and use the fundamental theorem
of calculus in each coordinate to pass these derivative
identities to the limit, successively at every order.
Its modular factor is
\[
\delta_r(a,b)=|\det D'/\det D|^{dr}.
\tag{1.26m}
\]
Indeed \(B_0\mapsto AB_0D^{-1}\) has determinant
\(|\det A|^{dm}|\det D|^{-dr}\);
\(C_0\mapsto D'C_0A^{-1}\) has determinant
\(|\det D'|^{dr}|\det A|^{-dm}\).
Conjugation on each reductive block has determinant
one, proving (1.26m).
The normal space is the bottom-right matrix block,
with action \(Y\mapsto DY(D')^{-1}\).
The two stabilizer unipotent blocks act trivially
on that normal space and its symmetric jet powers.

**Proposition 1.22d (generic uniqueness).** Outside a
countable subset of \(s\), the space of jointly
continuous functionals satisfying
\[
T(\rho(a,b)\Phi,\sigma(a,b)e)
=\chi_s(a,b)T(\Phi,e)
\tag{1.26n}
\]
has dimension at most one. This concerns the full
Schwartz and smooth coefficient spaces in (1.25a).

**Proof.** First consider a boundary-supported
relative functional. Take its highest support rank
\(r<n\), on the open set of rank at least \(r\).
Its rank-\(r\) orbit is a closed smooth submanifold
there. Joint continuity bounds test order by a
finite \(N\) near one base point, uniformly in
the coefficient variables. Covariance transports
this bound to every point of the orbit.
Lemma 1.22c gives a highest nonzero normal degree
\(j\le N\). Lemma 1.22b then gives a nonzero
\(\lambda\) satisfying (1.26f) for
\(J=\operatorname{Sym}^j(N^*)\).

Vary only the first-factor upper unipotent block
in (1.26k), with second component the identity.
Its character, modular factor and action on
normal jets are trivial. Differentiating shows
that \(\lambda\) factors through
\(W/\mathfrak uW\) in its first variable.
Lemma 1.22a supplies a monic polynomial
\(q_{\widetilde\pi,r}\) annihilating the radial
block-centre operator on that quotient.

Take \(a_t=\operatorname{diag}(I_r,tI_m)\), \(b=I_n\),
with real \(t>0\). A normal degree-\(j\) jet has
weight \(t^{-j}\), while \(\chi_s\delta_r\)
has weight \(t^{dm(u_s-r)}\). Equation (1.26f) says
\[
\lambda(\widetilde\pi(a_t)w\otimes v\otimes\xi)
=t^{dm(u_s-r)+j}\lambda(w\otimes v\otimes\xi).
\tag{1.26o}
\]
Differentiate at one and apply the annihilating
polynomial. A nonzero \(\lambda\) requires
\[
q_{\widetilde\pi,r}\bigl(dm(u_s-r)+j\bigr)=0.
\tag{1.26p}
\]
For each \(r,j\) its nonconstant affine argument
allows only finitely many parameters. The union
over \(0\le r<n,\ j\ge0\) is countable.
Off that union the highest normal part vanishes.
Descending in the normal degree and then in the
finitely many ranks proves that every boundary-
supported relative distribution is zero.

For the full-rank orbit the stabilizer is
diagonal \(G\), with trivial character and
modular factor. Lemma 1.22b identifies its
relative functionals with continuous invariant
pairings on \(W\times V\), a one-dimensional
space. Indeed a core pairing gives a
\((\mathfrak g,K)\)-map
\(V_0\to(W_0)^\sim=V_0\):
\(K\)-invariance makes each functional
\(K\)-finite, and finite-dimensional isotypic
duality proves this bidual equality.
The scalar-endomorphism proof under “Dense cores and scalar central operators” applies. Density
of the cores extends the scalar identity.

Two relative distributions with proportional
full-rank restrictions thus have zero difference
off the countable set. This proves the result
for compactly supported tests.
These tests are dense in Schwartz space:
cut off outside a radius-\(R\) ball; rapid
decay makes every Schwartz seminorm of the
error tend to zero, including the cutoff
derivatives. A continuous Schwartz functional
is determined by its compact-test restriction,
proving the stated result. \(\square\)

This proof uses neither finite length nor a
principal-series embedding or asymptotic
expansion. It does not assert that the
exceptional set is finite.

#### The scalar Fourier equation

**Theorem 1.22.** A nonzero meromorphic scalar
\(\gamma_{\rm mat}(s,\pi,\psi)\) exists, independent
of all tests and coefficient vectors, such that
\[
Z_{\widetilde\pi}(1-s,\widehat\Phi;w,v)
=\gamma_{\rm mat}(s,\pi,\psi)
Z_\pi(s,\Phi;v,w).
\tag{1.26q}
\]
It holds for every full Schwartz test and all
smooth vectors in the actual dual pair (1.25a).

**Proof.** Theorem 1.21 supplies meromorphic
continuous families for both sides.
Substitution in the original convergence
domain, followed by continuation, gives
\[
Z_{\pi,s}(\rho(a,b)\Phi,\sigma(a,b)e)
=\chi_s(a,b)Z_{\pi,s}(\Phi,e).
\tag{1.26r}
\]
The positive Fourier chain rule is
\[
\widehat{\rho(a,b)\Phi}
=(\nu(a)/\nu(b))^n\rho(b,a)\widehat\Phi.
\tag{1.26s}
\]
Change \(X=aYb^{-1}\); its additive Jacobian
is \((\nu(a)/\nu(b))^n\), and trace is cyclic.
Swap the coefficient variables and use
\[
n-\left(1-s+\frac{n-1}{2}\right)
=s+\frac{n-1}{2}.
\tag{1.26t}
\]
The dual Fourier family therefore has the
same character \(\chi_s\).

Off Proposition 1.22d's countable set and the
discrete majorant pole sets, the two families
are proportional. Choose a fixed compact
test supported inside \(G\) and coefficient
pair whose integral is nonzero at a real
parameter in the convergence domain.
Its integral \(A(s)\) is entire and not
identically zero. Evaluate the Fourier family
on this same triple, obtaining meromorphic
\(D(s)\), and define \(\gamma_{\rm mat}=D/A\).
This is meromorphic on \(\mathbb C\).
On the dense complement of the exceptional
set, poles and zeros of \(A\), it is the
proportionality scalar. For each other
triple, the difference in (1.26q) is a
meromorphic function vanishing on that
dense set. The identity theorem proves
the equation everywhere.

The scalar cannot vanish identically.
Otherwise the dual Fourier family vanishes
on every triple. Fourier transformation and
swapping the coefficient spaces are
bijections. The entire dual original family
would then vanish, contradicting an ordinary
nonzero compact-support integral in its
convergence domain. \(\square\)

The exact reflection and character-change
identities are
\[
\gamma_{\rm mat}(s,\pi,\psi)
\gamma_{\rm mat}(1-s,\widetilde\pi,\psi)
=\omega_\pi(-I_n),
\tag{1.26u}
\]
\[
\gamma_{\rm mat}(s,\pi,\psi_a)
=\omega_\pi(aI_n)|a|_F^{n(s-1/2)}
\gamma_{\rm mat}(s,\pi,\psi),
\qquad \psi_a(x)=\psi(ax).
\tag{1.26v}
\]
Applying (1.26q) twice reflects the test;
substituting \(g\mapsto-g\) contributes
\(\omega_\pi(-I_n)\), proving (1.26u).
For (1.26v), the self-dual measure scales
by \(|a|_F^{n^2/2}\), and
\(\widehat\Phi_{\psi_a}(Y)=|a|_F^{n^2/2}
 \widehat\Phi_\psi(aY)\).
In the dual integral substitute \(Y=aX\).
The inverse coefficient contributes
\(\omega_\pi(aI_n)\), and its determinant
power contributes
\(|a|_F^{-n(1-s+(n-1)/2)}\).
The product is the exponent in (1.26v).
These are meromorphic identities, initially
verified by substitution in the convergent
dual integral and then continued.

#### Consequences of a genuine Gaussian generator

**Corollary 1.22e (conditional canonical epsilon).**
For \(\psi_{\mathbb R}(x)=e^{-2\pi ix}\) and
\(\psi_{\mathbb C}(z)=e^{-4\pi i\operatorname{Re}z}\),
suppose the Gaussian ideal (1.25u) holds for
both \(\pi\) and \(\widetilde\pi\).
Then Proposition 1.21b gives canonical full-
Schwartz division and absence of zeros, and
\[
\gamma_{\rm mat}(s,\pi,\psi)
=\epsilon_\pi\,L_{\widetilde\pi}(1-s)/L_\pi(s),
\qquad \epsilon_\pi\in\mathbb C^\times
\text{ constant}.
\tag{1.26w}
\]

**Proof.** Differentiating the basic Gaussian
Fourier identity shows that Fourier
transformation preserves polynomial Gaussian
tests for these standard characters.
Trace transpose and the complex pairing's
real sign just change polynomial coordinates.
Swap the core coefficient spaces too.
Taking the Gaussian family spans in (1.26q)
therefore gives
\[
\gamma_{\rm mat}(s,\pi,\psi)L_\pi(s)\mathbb C[s]
=L_{\widetilde\pi}(1-s)\mathbb C[s].
\tag{1.26x}
\]
The ratio in (1.26w) multiplies
\(\mathbb C[s]\) onto itself.
Applying this to \(1\) in both directions
makes the ratio and its inverse polynomials.
Polynomial units are nonzero constants,
proving the assertion. General character
dependence follows from (1.26v).
\(\square\)

Theorem 1.31 below supplies the general Gaussian ideal and its finite
attaining family in every prescribed actual complete smooth moderate
dual-pair model.
The common gamma majorant, scalar Fourier
equation and polynomial-module closure do
not establish it. These arguments do not
identify the canonical factors with the
gamma factors of a local Langlands parameter.


#### Unitary conjugation and the critical line

**Corollary 1.22f.** Suppose the dual pair is the smooth pair furnished by an actual admissible irreducible unitary Hilbert representation, with the compatible Hilbert pairing. For every nontrivial unitary additive character, the scalar in Theorem 1.22 has neither a zero nor a pole on \(\operatorname{Re}s=1/2\), and
\[
|\gamma_{\rm mat}(1/2+it,\pi,\psi)|=1\qquad(t\in\mathbb R).
\tag{1.26y}
\]
If both Gaussian ideals exist and their chosen generators additionally obey
\(L_{\widetilde\pi}(s)=\overline{L_\pi(\bar s)}\), the constant in Corollary 1.22e has absolute value one.

**Proof.** Hilbert conjugation identifies the conjugate smooth representation with its compatible contragredient. This follows directly from invariance of the Hilbert form: a conjugate vector defines its paired functional, differentiation commutes with this map, and on each finite-dimensional compact type it is the ordinary dual identification. Thus conjugating a matrix coefficient of \(\pi\) gives a coefficient of \(\widetilde\pi\), with the swapped dual pair. Conjugation of the positive Fourier integral gives
\(\overline{\widehat\Phi_\psi}=\widehat{\bar\Phi}_{\psi^{-1}}\), since the additive measure is real. Conjugating (1.26q) in its meromorphic continuation and using uniqueness of its scalar therefore proves
\[
\overline{\gamma_{\rm mat}(s,\pi,\psi)}
=\gamma_{\rm mat}(\bar s,\widetilde\pi,\psi^{-1})
=\omega_\pi(-I_n)\gamma_{\rm mat}(\bar s,\widetilde\pi,\psi).
\tag{1.26z}
\]
The second equality is (1.26v) with \(a=-1\); its norm factor is one and the inverse central sign equals the same sign. On the critical line \(\bar s=1-s\). At every regular point (1.26u) now gives the square modulus \(\omega_\pi(-I_n)^2=1\), because \((-I_n)^2=I_n\). A Laurent expansion at a putative zero or pole on that line would force the modulus along the line to tend to zero or infinity. The regular values have modulus one, so neither can occur. Finally, under the stated generator conjugation, \(L_{\widetilde\pi}(1-s)/L_\pi(s)\) has modulus one at a regular critical-line point. Substitution in (1.26w) gives \(|\epsilon_\pi|=1\). This last assertion uses the specified generator normalization; the scalar Fourier equation alone does not identify it. \(\square\)


### The all-rank archimedean inducing Gaussian kernel

Let \(F=\mathbb R\) or \(\mathbb C\), \(G=GL_n(F)\), \(K=O(n)\) or
\(U(n)\), \(B\) the upper triangular subgroup, and \(M=B\cap K\).
Put \(d=[F:\mathbb R]\), \(\nu(g)=|\det g|_F\), and
\(\rho_j=(n+1)/2-j\). Every smooth character has the form
\[
\chi_j(x)=\operatorname{sgn}(x)^{e_j}|x|^{t_j}
\quad(F=\mathbb R),\qquad
\chi_j(z)=(z/|z|)^{\ell_j}|z|_{\mathbb C}^{t_j}
\quad(F=\mathbb C),
\tag{1.31a}
\]
with \(e_j\in\{0,1\}\), \(\ell_j\in\mathbb Z\), \(t_j\in\mathbb C\).
Indeed a smooth homomorphism on the positive radial group, transported
by logarithm, solves \(f'(u)=cf(u)\). On the real sign group it has
value \(1\) or \(-1\). On the complex unit circle the same differential
equation and period \(2\pi\) force an integer angular exponent.

Use the programme's negative-exponent characters
\(\psi_{\mathbb R}(x)=e^{-2\pi ix}\),
\(\psi_{\mathbb C}(z)=e^{-2\pi i(z+\bar z)}\), their self-dual measures,
and the positive trace Fourier argument. With \(dg=C_F\nu(g)^{-n}dX\),
\[
Z(s,\Phi,c)=\int_G\Phi(g)c(g)\nu(g)^{s+(n-1)/2}\,dg.
\tag{1.31b}
\]
The fixed matrix Gaussians throughout are
\[
G_{\mathbb R}(X)=e^{-\pi\operatorname{tr}(XX^t)},\qquad
G_{\mathbb C}(X)=e^{-2\pi\operatorname{tr}(XX^*)}.
\tag{1.31ba}
\]
The self-dual additive measures are ordinary Lebesgue measure in
each real entry and \(2\,du\,dv\) in each complex entry.
For each scalar diagonal coordinate use exactly
\(d^\times x=dx/|x|\) over \(\mathbb R\) and
\(d^\times z=(2\,du\,dv)/(\pi|z|_{\mathbb C})\) over \(\mathbb C\).
These are the actual NT-ADL-08 normalizations; the positive constant
\(\kappa_F\) in the matrix decomposition absorbs only the remaining
matrix Haar normalization and compact angular redundancy.
Write
\[
\begin{aligned}
\mathcal I(\boldsymbol\chi)
&=\{f\in C^\infty(G):
f(bg)=\delta_B(b)^{1/2}\boldsymbol\chi(b)f(g)\},\\
\delta_B(b)^{1/2}
&=\prod_j|b_{jj}|_F^{\rho_j},\qquad
\boldsymbol\chi(b)=\prod_j\chi_j(b_{jj}).
\end{aligned}
\tag{1.31c}
\]
The topology is the usual \(C^\infty\) topology on the compact model
\[
\{f\in C^\infty(K):f(mk)=\boldsymbol\chi(m)f(k)\}.
\tag{1.31d}
\]
The extension between (1.31c) and (1.31d) is defined by row Gram--Schmidt,
with positive diagonal, and is unique. This is an actual complete
smooth moderate-growth realization, not a formal induced module.

Put
\[
L_{\boldsymbol\chi}(s)=
\begin{cases}
\prod_j\Gamma_{\mathbb R}(s+t_j+e_j),&F=\mathbb R,\\
\prod_j\Gamma_{\mathbb C}(s+t_j+|\ell_j|/2),&F=\mathbb C,
\end{cases}
\qquad
\epsilon_{\boldsymbol\chi}=
\begin{cases}
(-i)^{\sum e_j},&F=\mathbb R,\\
(-i)^{\sum |\ell_j|},&F=\mathbb C.
\end{cases}
\tag{1.31e}
\]

**Theorem 1.26.** For the paired actual models
\(\mathcal I(\boldsymbol\chi)\) and
\(\mathcal I(\boldsymbol\chi^{-1})\), the matrix zeta family has:

1. the full polynomial-Gaussian ideal
   \(L_{\boldsymbol\chi}(s)\mathbb C[s]\), over all compact-finite
   coefficient vectors;
2. one polynomial Gaussian and one coefficient attaining
   \(\kappa_F L_{\boldsymbol\chi}(s)\), where \(\kappa_F>0\) depends
   only on the measures;
3. entire normalized division for every Schwartz test and every smooth
   paired coefficient, with compact-parameter joint seminorm bounds;
4. the full scalar positive-trace Fourier equation
\[
Z_{\boldsymbol\chi^{-1}}(1-s,\widehat\Phi,c^\vee)=
\epsilon_{\boldsymbol\chi}
\frac{L_{\boldsymbol\chi^{-1}}(1-s)}
{L_{\boldsymbol\chi}(s)}
Z_{\boldsymbol\chi}(s,\Phi,c).
\tag{1.31f}
\]

This holds in every rank, for all the character parameters in (1.31a);
the induced representation need not be irreducible. It therefore
proves the intended exact Gaussian generator for every irreducible
full Borel induction in this actual model, without a classification
of when the induction is irreducible.

#### Step 1: The actual compact model and its pairing

Row Gram--Schmidt writes \(g=T k\), with \(T\) upper triangular
and positive real diagonal. The coefficients and derivatives of the
Gram--Schmidt maps are bounded by powers of
\[
H(g)=1+\|g\|+\|g^{-1}\|.
\tag{1.31g}
\]
Here is the estimate. Each orthogonal component of a row has length
at most \(\|g\|\) and at least \(\|g^{-1}\|^{-1}\): subtracting
later rows amounts to forming a row combination with one coefficient
equal to one, whose norm is bounded below by the smallest singular
value of \(g\). Every fixed derivative of the recursion has a polynomial
numerator in the entries and previously computed quantities and a
denominator consisting of finitely many powers of these positive
lengths. Character differentiation gives only further powers of
the same lengths. On the compact \(k\)-variable, this proves
\[
p_N(\mathcal I(g)f)\le C_N H(g)^{A_N}p_N(f)
\tag{1.31h}
\]
for increasing compact smooth seminorms \(p_N\), with fixed \(A_N\).
Differentiating the action in \(g\) gives continuous maps with finitely
more compact derivatives. The closed space (1.31d) is complete, and
these formulas prove a smooth moderate-growth action.

The compact pairing is
\[
\langle f,\widetilde f\rangle=\int_K f(k)\widetilde f(k)\,dk,
\qquad \widetilde f\in\mathcal I(\boldsymbol\chi^{-1}),
\tag{1.31i}
\]
with Haar probability. It is nondegenerate, including on paired finite
compact types: \(\boldsymbol\chi|_M\) is unitary, so the conjugate
of a nonzero \(f\) has the inverse \(M\)-covariance and its pairing
with \(f\) is positive.

For completeness, the pairing is \(G\)-invariant with exactly this
normalization. Identify \(B\backslash G=M\backslash K\).
If \(kg=b(k,g)k_g\), the Jacobian of \(Bk\mapsto Bkg\) in compact
Haar quotient density is \(\delta_B(b(k,g))\).
To compute it, use right translation by \(k\) and \(k_g\) to identify
the two tangent spaces with \(\mathfrak g/\mathfrak b\).
The differential is \(\operatorname{Ad}(b^{-1})\) on that quotient.
For diagonal \(b\), its lower-entry weights are \(b_{jj}/b_{ii}\),
\(i>j\), whose product of normalized absolute values is
\(\delta_B(b)\). For an upper unipotent generator
\(\exp(xE_{ij})\), its adjoint action on the quotient is the
exponential of a nilpotent operator and has determinant one;
these generators exhaust the unipotent subgroup. Thus the Jacobian
formula holds for every \(b\). The tangent identifications use the
right-\(K\)-invariant quotient density, so there is no additional
point-dependent scalar. Changes of the factorization by \(M\) have
unit Jacobian.

The two multiplier factors in (1.31c) multiply to \(\delta_B(b)\).
The computed Jacobian then proves (1.31i) invariant by change of variable.
The inverse coefficient is accordingly
\[
c^\vee(g)=c(g^{-1})
=\langle \mathcal I(\boldsymbol\chi^{-1})(g)\widetilde f,f\rangle
\quad\text{if }c(g)=\langle\mathcal I(\boldsymbol\chi)(g)f,\widetilde f\rangle .
\tag{1.31j}
\]

The compact-finite cores are admissible and dense by the elementary
compact-polynomial argument written in Step 1 of the subquotient argument below. Its evaluation-at-identity argument bounds the
multiplicity of a compact type in the scalar function space by the
type's dimension; the line-covariance subspace (1.31d) can only reduce
it. Its explicit central polynomial approximate identities converge
in all compact smooth seminorms and have compact-finite range.
Thus no general Peter--Weyl or globalization statement is needed
as a separate unproved input.

#### Step 2: The all-rank upper-triangular measure

For \(a=(a_1,\ldots,a_n)\in(F^\times)^n\) and strict upper entries
\(x=(x_{ij})_{i<j}\), let \(T(a,x)\) be upper triangular with that
diagonal. The Haar integration formula is
\[
dg=\kappa_F\prod_{i=1}^n|a_i|_F^{\,i-n}\,
\prod_i d^\times a_i\prod_{i<j}dx_{ij}\,dk .
\tag{1.31k}
\]
This formula includes the redundant unit-diagonal factors in \(a_i\);
\(\kappa_F>0\) accounts for their fixed multiplicative angular masses.

Here is a derivation in every rank. Orthogonalize rows in the order
\(n,n-1,\ldots,1\). At step \(i\), the row components along the
already chosen later rows are \(n-i\) additive coordinates over \(F\).
Its remaining orthogonal component lies in an \(i\)-dimensional
\(F\)-space. Polar coordinates there contribute
\(r_i^{di-1}dr_i\) and its unit-vector measure. Successively these
unit vectors form a complete orthonormal frame. Their product measure
is invariant under right-\(K\) rotation of the ambient row space,
hence a fixed positive multiple of Haar measure.
The orthogonal coordinate changes have real Jacobian one.
Consequently additive matrix measure is a positive constant times
\(\prod_i r_i^{di}\,dr_i/r_i\prod dx_{ij}\,dk\).
Division by \(\nu(g)^n=\prod_i r_i^{dn}\) gives the powers in
(1.31k). Finally replace positive \(r_i\) by arbitrary \(a_i\)
using the diagonal compact phases/signs: multiply column \(j\)
of \(T\) by its unit \(m_j\) and replace \(k\) by \(m^{-1}k\).
The upper-entry additive measures and Haar probability are unchanged.
The multiplicative angular masses are constants, giving precisely
(1.31k). This derives the density without importing an Iwasawa
integration theorem.

#### Step 3: The matrix kernel

Define the Schwartz diagonal marginal
\[
\phi_{\Phi;h,k}(a)=
\int_{F^{n(n-1)/2}}
\Phi(h^{-1}T(a,x)k)\,\prod_{i<j}dx_{ij}
\tag{1.31l}
\]
on the **whole** additive space \(F^n\), including zero coordinates,
and the kernel
\[
\mathcal K_{\Phi,\boldsymbol\chi}(h,k;s)=
\int_{(F^\times)^n}\phi_{\Phi;h,k}(a)
\prod_i\chi_i(a_i)|a_i|_F^s\,d^\times a_i.
\tag{1.31m}
\]
Restriction to a linear coordinate subspace and integration in other
coordinates map the Schwartz space continuously to itself.
For example, after differentiating in \(a\), choose an upper-variable
decay power greater than its real dimension plus the desired
seminorm degree, integrate that bound, and retain the required
decay in \(a\). Linear substitutions by compact \(h,k\) have
uniform seminorm bounds. This proves continuity and compact uniformity
of (1.31l).

The matrix coefficient integral is exactly
\[
Z(s,\Phi,c_{f,\widetilde f})
=\kappa_F\int_{K\times K}
\mathcal K_{\Phi,\boldsymbol\chi}(h,k;s)
\widetilde f(h)f(k)\,dh\,dk .
\tag{1.31n}
\]
In fact expand the pairing coefficient by (1.31i), substitute
\(g\mapsto h^{-1}g\), and apply (1.31k). The power of each \(|a_i|_F\)
is
\[
\rho_i+\frac{n-1}{2}+(i-n)+s=s.
\tag{1.31o}
\]
Thus (1.31m) is the resulting diagonal integral with no extra shift.
The same calculation with absolute values proves every integral
absolutely convergent in a common far right half-plane; compact
\(h,k\) and the bounds of (1.31l) make all uses of Fubini valid.

#### Step 4: Full-Schwartz division and polynomial Gaussian quotients

The scalar Tate normalized distributions
\[
A_{\chi}(s)(f)=Z_F(s,f,\chi)/L_F(s,\chi)
\tag{1.31p}
\]
are entire continuous Schwartz families with compact-parameter seminorm
bounds. The actual proof of *Tate’s local theory at the infinite places* supplies their Mellin continuation,
pole cancellation and entire reciprocal gamma. Its Taylor proof also
gives the seminorm bound needed here: expand the parity or angular
projection to order \(N\) at zero; its finitely many coefficient
functionals are continuous derivatives at zero, and the remainder
is bounded by a fixed \(C^N\) seminorm times the radial power \(N\).
Choose \(N\) for a fixed compact \(s\)-set. The integral outside a unit
ball is bounded by a fixed Schwartz seminorm. Multiplication by the
entire gamma reciprocal removes the finite polar terms, with
bounded coefficients on the compact set. This proves the assertion
without a family-level continuity assumption.

The same estimate holds with Schwartz variables as parameters:
apply it to every derivative in the other variables after multiplying
by their desired polynomial weights. It defines a continuous entire
operator from \(\mathcal S(F^r)\) to \(\mathcal S(F^{r-1})\).
This is entireness in its Schwartz topology: the Taylor-subtracted
integrals can be differentiated in \(s\) with arbitrary fixed
Schwartz seminorms under domination, and their Cauchy formulas
converge in each seminorm on smaller parameter disks. The finitely
many removed polar terms obey the same formulas after multiplication
by the entire gamma reciprocal.
Iterate this in the \(n\) diagonal coordinates. Hence
\[
\mathcal K_{\Phi,\boldsymbol\chi}(h,k;s)/
L_{\boldsymbol\chi}(s)
\tag{1.31q}
\]
is entire, continuous in \(\Phi\), and uniformly bounded by finitely
many Schwartz seminorms for compact \(h,k,s\).
Equation (1.31n) proves entire normalized division for all smooth
paired coefficient vectors, with a bound by such a test seminorm
times \(\|f\|_\infty\|\widetilde f\|_\infty\).

If \(\Phi=P G_F\) is a polynomial Gaussian, compact multiplication
preserves the Gaussian. Integrating its upper-entry polynomial
gives a polynomial in \(a,\bar a\) times the diagonal Gaussian;
its degree is bounded independently of \(h,k\).
Every real monomial of degree \(r\) has zero scalar Tate integral
unless \(r=e+2q\), in which case its quotient by
\(\Gamma_{\mathbb R}(s+t+e)\) is
\(\pi^{-q}((s+t+e)/2)_q\).
Every complex monomial \(a^u\bar a^v\) has zero integral unless
\(v-u=\ell_j\), in which case its quotient is
\((2\pi)^{-\min(u,v)}(s+t+|\ell_j|/2)_{\min(u,v)}\).
These are proved gamma recurrence calculations with nonnegative
integers. Therefore (1.31q), and then the normalized matrix integral
in (1.31n), is a polynomial in \(s\). Its coefficients are smooth
functions of \(h,k\), and the finite degree bound permits the
compact integrations coefficient by coefficient.

#### Step 5: A Gaussian attaining the whole product

Take the scalar fundamental angular Gaussian polynomials
\[
p_j(z)=
\begin{cases}
z^{e_j},&F=\mathbb R,\\
\bar z^{\ell_j},&F=\mathbb C,\quad \ell_j\ge0,\\
z^{-\ell_j},&F=\mathbb C,\quad \ell_j<0,
\end{cases}
\tag{1.31r}
\]
In the following formula evaluate these polynomials on \(X_{jj}\):
\[
\Phi_0(X)=\prod_jp_j(X_{jj})\,G_F(X).
\tag{1.31s}
\]
At \(h=k=e\), its upper marginal is the tensor of the fundamental
scalar Tate tests: each upper-coordinate Gaussian has mass one
in its self-dual measure. Thus
\[
\mathcal K_{\Phi_0,\boldsymbol\chi}(e,e;s)
=L_{\boldsymbol\chi}(s).
\tag{1.31t}
\]

It remains to realize this evaluation by actual finite coefficient
vectors, not by a delta distribution on \(K\).
The kernel (1.31m) has the compact covariances
\[
\mathcal K(mh,k;s)=\boldsymbol\chi(m)\mathcal K(h,k;s),\qquad
\mathcal K(h,mk;s)=\boldsymbol\chi(m)^{-1}\mathcal K(h,k;s).
\tag{1.31u}
\]
For the first, replace \(T\) by \(m^{-1}T\); for the second replace
it by \(Tm\). The diagonal changes supply the indicated characters,
and all compact unit Jacobians are one.

For (1.31s), the normalized kernel is a polynomial in \(s\) and
in the entries and conjugate entries of \(h,k\).
It lies in a fixed finite-dimensional tensor product \(E_h\otimes E_k\),
independent of \(s\), with
\[
E_h\subset\mathcal I(\boldsymbol\chi)|_K,\qquad
E_k\subset\mathcal I(\boldsymbol\chi^{-1})|_K.
\tag{1.31v}
\]
To see this exactly, start with the finite-dimensional spaces of
coordinate polynomials of the bounded degrees in \(h,k\).
Project their left \(M\)-actions onto the two characters in (1.31u).
These compact averages preserve degree and commute with right \(K\).
Applying both projections to the kernel fixes it, so their images
are the required finite compact spaces.

Evaluation at \(e\) on \(E_h\) is represented by pairing with a
single \(\widetilde f\in\overline{E_h}
\subset\mathcal I(\boldsymbol\chi^{-1})|_K\);
evaluation on \(E_k\) is represented by pairing with a single
\(f\in\overline{E_k}\subset\mathcal I(\boldsymbol\chi)|_K\).
This is just finite-dimensional nondegenerate Gram duality:
choose a basis, invert its positive Haar Gram matrix, and form the
vector representing the evaluation functional. These choices do not
depend on \(s\). The tensor of the two evaluations therefore gives
\[
\int_{K\times K}\mathcal K_{\Phi_0,\boldsymbol\chi}(h,k;s)
\widetilde f(h)f(k)\,dh\,dk
=\mathcal K_{\Phi_0,\boldsymbol\chi}(e,e;s).
\tag{1.31w}
\]
Equations (1.31n) and (1.31t) prove the claimed one-coefficient
attainment.

Polynomial-module closure follows directly from scalar dilation.
For the real dilation Euler operator \(E\),
\[
Z(s,E\Phi,c)
=-\{dn(s+(n-1)/2)+d\sum_jt_j\}Z(s,\Phi,c).
\tag{1.31x}
\]
The coefficient's positive-central homogeneity is
\(r^{d\sum t_j}\). Prove (1.31x) by differentiating the change
of variable \(X\mapsto rX\) in a convergence half-plane and continue
meromorphically. \(E\) preserves polynomial Gaussians, so multiplication
by \(s\) preserves the span. The polynomial bound and the attained
product now prove the exact ideal of Theorem 1.26.
In particular polynomial coefficients in an attaining identity can
be absorbed into new polynomial Gaussian tests: the operator
\[
\mathscr S=-\frac{E}{dn}-\frac{n-1}{2}
-\frac{\sum_jt_j}{n}
\tag{1.31xa}
\]
satisfies \(Z(s,\mathscr S\Phi,c)=sZ(s,\Phi,c)\).
It preserves the fixed polynomial-Gaussian space. Thus any finite
polynomial combination of matrix integrals is a finite unweighted
sum of integrals with explicitly changed tests.

#### Step 6: The all-rank diagonal Fourier marginal

At \(h=k=e\), the identity of Schwartz functions is
\[
\phi_{\widehat\Phi;e,e}
=\widehat{\phi_{\Phi;e,e}},
\tag{1.31y}
\]
where the right transform is the \(n\)-coordinate diagonal transform.
The trace pairing pairs an upper Fourier entry \(Y_{ij}\), \(i<j\),
with the lower original entry \(X_{ji}\).
Integrating in all upper Fourier entries sets all those lower original
entries to zero by partial Schwartz Fourier inversion.
The upper original entries are then integrated out, and the diagonal
entries retain exactly their ordinary bilinear Fourier transform.
One can perform this as successive continuous partial Fourier transforms,
restriction and integration on Schwartz spaces, so no nonabsolutely
convergent iterated integral is being asserted.

For compact \(h,k\),
\[
\widehat{\Phi(h^{-1}Xk)}(Y)=\widehat\Phi(k^{-1}Yh).
\tag{1.31z}
\]
Apply (1.31y) to \(\Phi(k^{-1}Xh)\). The \(n\) scalar Tate equations
then yield
\[
\mathcal K_{\widehat\Phi,\boldsymbol\chi^{-1}}(h,k;1-s)
=\left(\prod_j\gamma_F(s,\chi_j,\psi_F)\right)
\mathcal K_{\Phi,\boldsymbol\chi}(k,h;s).
\tag{1.31aa}
\]
The scalar equations are the actual whole-Schwartz proof of
NT-ADL-08; iterating them in parameter variables is justified by
the operators of Step 4 of this argument. Compact integration and interchanging
\(h,k\) in (1.31n) prove (1.31f) for the **whole** smooth coefficient
family. Formula (1.31e) is the product of those exact scalar
normalizations. This finishes Theorem 1.26.

There are two useful sign checks. Fourier inversion gives
\(\widehat{\widehat\Phi}(X)=\Phi(-X)\). Applying (1.31f) twice must
therefore give the central sign of the coefficient. In fact
\[
\epsilon_{\boldsymbol\chi}\epsilon_{\boldsymbol\chi^{-1}}
=(-1)^{\sum e_j}\quad(\mathbb R),\qquad
=(-1)^{\sum|\ell_j|}=\prod_j\chi_j(-1)\quad(\mathbb C),
\tag{1.31ab}
\]
as required. If \(\psi_F\) is replaced by \(x\mapsto\psi_F(ax)\)
with \(a\in F^\times\), the self-dual matrix measure is multiplied
by \(|a|_F^{n^2/2}\), and
\(\widehat\Phi_a(Y)=|a|_F^{n^2/2}\widehat\Phi(aY)\).
Changing \(g\) to \(a^{-1}g\) in the dual matrix integral gives
\[
\epsilon_{\boldsymbol\chi}(s,\psi_{F,a})
=\omega_{\boldsymbol\chi}(a)|a|_F^{n(s-1/2)}
\epsilon_{\boldsymbol\chi},
\qquad \omega_{\boldsymbol\chi}(a)=\prod_j\chi_j(a).
\tag{1.31ac}
\]
This uses matrix Haar invariance and the exact exponent
\(n^2/2-n((n+1)/2-s)=n(s-1/2)\); it does not change the
Gaussian generator for the original fixed Gaussian convention.

#### Scope of this proof

Theorem 1.26 proves the all-rank inducing kernel and its actual smooth
paired realization, Gaussian polynomial quotient, attainment, full
Schwartz continuity and Fourier equation. It does not assert that
every irreducible admissible module embeds in this principal series,
or that an arbitrary constituent has the full product generator.
The subquotient argument below proves the exact
finite polynomial correction and its attaining identity for every
algebraic constituent that is actually supplied.
The identification of those corrections with the intended
standard-module gamma data for **every** irreducible remains a
further obligation.

The earlier programme inputs used here are the actual scalar
NT-ADL-08 theory and the
whole-Schwartz Fourier proof of *Additive characters, self-dual measures and Poisson summation on the adèles*. Goldfeld--Jacquet's
freely accessible author notes, §3, Theorem 3.5 and Lemma 3.6
at [Goldfeld–Jacquet, freely accessible author notes](https://www.math.columbia.edu/~goldfeld/LanglandsBookChapter.pdf),
locate the general target; their inducing reduction is not
being used as an unproved premise.

### Actual closed principal-series subquotients and their Gaussian ideals

Use the actual compact models \(I=\mathcal I(\boldsymbol\chi)\) and
\(\widetilde I=\mathcal I(\boldsymbol\chi^{-1})\), compact pairing,
measures and gamma factors of the preceding Theorem 1.26.
Write \(I_0,\widetilde I_0\) for their compact-finite cores.

**Theorem 1.26a.** For every pair of algebraic
\((\mathfrak g,K)\)-submodules \(W_0\subset V_0\subset I_0\), their
compact-smooth closures \(W\subset V\subset I\) are closed
\(G\)-subrepresentations. The quotient
\[
Q=V/W                                                   \tag{1.32a}
\]
is an actual complete smooth moderate-growth realization with core
\(Q_0=V_0/W_0\). The inclusion and quotient are actual continuous
\(G\)-maps. If \(Q_0\) is irreducible, \(Q\) is topologically irreducible.
There is a paired actual smooth realization
\[
Q^\vee=\operatorname{Ann}(W)/\operatorname{Ann}(V)
\quad\text{inside }\widetilde I,                  \tag{1.32b}
\]
whose core is the admissible contragredient of \(Q_0\).
Every smooth paired coefficient lifts to an induced coefficient;
every compact-finite coefficient has compact-finite lifts.

**Theorem 1.26b.** If \(Q_0\ne0\), its exact Gaussian ideal is
\[
L_Q(s)\mathbb C[s],\qquad
L_Q(s)=P_Q(s)L_{\boldsymbol\chi}(s),                     \tag{1.32c}
\]
where \(P_Q\) is a nonzero monic polynomial defined by the actual
Gaussian integrals. A finite sum of polynomial multiples of Gaussian
coefficient integrals equals \(L_Q\).
For every Schwartz test and paired smooth coefficient,
\(Z_Q/L_Q\) is entire, with compact-parameter joint seminorm bounds.
\(L_Q\) has no zeros. With \(b=\deg P_Q\),
\[
P_{Q^\vee}(1-s)=(-1)^bP_Q(s),\qquad
\epsilon_Q=(-1)^b\epsilon_{\boldsymbol\chi},             \tag{1.32d}
\]
and
\[
Z_{Q^\vee}(1-s,\widehat\Phi,c^\vee)
=\epsilon_Q\frac{L_{Q^\vee}(1-s)}{L_Q(s)}
Z_Q(s,\Phi,c).  \tag{1.32e}
\]
Thus \(|\epsilon_Q|=1\) for the programme's basic characters.
Conjugation gives the construction in
\(I(\overline{\boldsymbol\chi})\), and exactly
\[
L_{\bar Q}(s)=\overline{L_Q(\bar s)}.                    \tag{1.32f}
\]
If \(Q_0\) has an invariant positive Hermitian form, also
\[
L_{Q^\vee}(s)=\overline{L_Q(\bar s)}                     \tag{1.32g}
\]
in this monic polynomial normalization.

These statements cover every **supplied algebraic principal-core
subquotient**, with its actual models and maps constructed below.
They do not assume an abstract globalization functor. They do not
assert that every irreducible admissible module occurs in a principal
core, or identify \(P_Q\) with the intended standard-module factors.

#### Step 1: Compact polynomials, finite packets and density

On \(K=O(n)\) or \(U(n)\) put
\[
q(k)=\frac{1+\operatorname{Re}\operatorname{tr}(k)/n}{2}
=1-\frac{\|k-I\|_{\mathrm{HS}}^2}{4n},\qquad
A_Nf(k)=\frac{\int_Kq(h)^Nf(kh)\,dh}{\int_Kq(h)^N\,dh}.
\tag{1.32h}
\]
Here \(0\le q\le1\), and \(q=1\) only at the identity.
These are approximate identities. On the complement of a fixed
identity neighborhood let \(q\le c<1\); a smaller neighborhood has
\(q\ge c'>c\) and positive Haar mass. The relative mass on that
complement is at most \((c/c')^N/\operatorname{mass}(U')\), tending
to zero. Uniform continuity gives uniform convergence \(A_Nf\to f\).

The class function \(q^N\) makes \(A_N\) commute with right \(K\)
and its differentiated actions. Applying uniform convergence to each
compact derivative proves convergence in every compact smooth seminorm.
The operator preserves the left \(M\)-character of \(I\).
After changing variable \(y=kh\), its kernel is \(q(k^{-1}y)^N\),
a polynomial in entries and conjugate entries of \(k\). Hence
\(A_Nf\) is a coordinate polynomial restriction, of bounded degree,
and has finite-dimensional right-\(K\) orbit. This proves core density.
It works for disconnected \(O(n)\), including \(O(1)\).

Conversely every compact-finite function is a coordinate polynomial.
Its finite orbit splits into irreducibles by averaging a Hermitian
form. On each type, central convolution \(A_N\) is scalar by the
finite-dimensional Schur lemma. Its scalar tends to one, hence is
nonzero for large \(N\). Invert the finitely many scalars to write
the original function as \(A_Nf'\), a coordinate polynomial.
The elementary facts used here can be checked directly. Averaging
any positive Hermitian form over compact \(K\) preserves positivity
and makes the form invariant; invariant orthogonal complements
give the finite irreducible decomposition by induction on dimension.
An endomorphism of a nonzero complex irreducible representation has
an eigenvalue; its eigenspace is nonzero and invariant, hence the
whole space. It is therefore scalar. The integral defining \(A_N\)
preserves each such irreducible copy, and its centrality makes it
an intertwiner there, so the scalar argument applies to every copy.

Every compact type has finite multiplicity in \(C^\infty(K)\):
an equivariant map \(T:E_\tau\to C^\infty(K)\) is determined by
\(\ell(v)=(Tv)(e)\), since \((Tv)(k)=\ell(\tau(k)v)\).
Its multiplicity is at most \(\dim E_\tau\).
The compact-type projector
\[
P_\tau f(k)=\dim E_\tau\int_K
\overline{\operatorname{tr}\tau(h)}f(kh)\,dh    \tag{1.32i}
\]
is continuous and has finite-dimensional range. Its projection
property follows by averaging a linear map between finite-dimensional
irreducibles: the average is zero or scalar, and trace fixes the
scalar. Changing variable \(y=kh\) in (1.32i) exhibits its finite
matrix-coefficient range directly. The same statements hold in
the line-covariance space \(I\). This supplies all the compact
finiteness used below without a general globalization theorem.
More explicitly, for irreducibles \(\sigma,\tau\), the map
\(\int_K\tau(h)A\sigma(h)^{-1}\,dh\) intertwines them.
It is zero when they are inequivalent, since a nonzero intertwiner
has invariant kernel and image and is an isomorphism. For
\(\sigma=\tau\), the scalar is \(\operatorname{tr}(A)/\dim E_\tau\).
Taking \(A\) to be the matrix units gives the matrix-entry
orthogonality and exactly the character projector (1.32i).

#### Step 2: Uniform analytic exponentials on the principal core

For fixed \(X\in\mathfrak g_{\mathbb R}\) and any \(f\in I_0\),
\[
t\longmapsto \mathcal I(\exp(tX))f                     \tag{1.32j}
\]
has a Taylor series converging in the compact smooth topology for
\(|t|<r_X\), with \(r_X>0\) independent of \(f\).

Indeed \(f\) is a coordinate polynomial on \(K\).
Factor \(k\exp(tX)=T(t,k)k'(t,k)\) by row Gram--Schmidt with positive
diagonal. Squared pivots are ratios of consecutive trailing row-Gram
determinants. The Gram matrix on real \(t\) is
\[
k\exp(tX)\exp(tX^*)k^*.                                \tag{1.32k}
\]
Replace \(t\) by a complex variable in this formula, keeping \(X^*\)
fixed. At zero all those determinants are one, uniformly in \(k\).
On a small disk they stay near one and avoid zero; choose their
logarithm and square-root branches starting at one. All remaining
Gram--Schmidt entries are algebraic expressions divided by these
nonzero pivots. The conjugate trajectory, with the conjugated fixed
coefficients, similarly gives a holomorphic extension of the actual
conjugate entries of \(k'(t,k)\). Thus every polynomial in
\(k',\bar k'\) has a holomorphic extension in \(t\).
The inducing multiplier is
\(\prod_j r_j(t,k)^{d(t_j+\rho_j)}\), using the same logarithms;
the diagonal is positive on real \(t\), so its angular characters
are one.

Every fixed number of compact derivatives is bounded on a smaller
closed complex disk. Its radius is determined by the Gram
determinants, not by the degree of \(f\). Cauchy's coefficient
estimate proves Taylor convergence in every compact smooth seminorm,
on a common disk. The coefficients are
\((d\mathcal I(X))^af/a!\), by differentiation of the actual action.

The same argument near any \(g_0\in G\), replacing \(k\) by \(kg_0\),
proves real analyticity of its core matrix coefficients. Pivots at
\(g_0\) are uniformly positive by the singular-value estimates in
Theorem 1.26. The construction extends in all real group coordinates
in a small complex polydisk, and continuous compact pairing and
uniform compact bounds preserve analyticity after integration.

#### Step 3: Algebraic closures are genuinely group stable

Let \(V=\overline{V_0}\). For \(v\in V_0\), every term of the Taylor
series in (1.32j) lies in \(V_0\), by Lie stability. Its sum therefore
lies in \(V\) for \(|t|<r_X\). The radius is independent of \(v\).
Approximation by \(V_0\) and continuity show the same inclusion
for every \(v\in V\). Use negative \(t\) and finite products of
small intervals to obtain equality for every real \(t\).
The closure is also \(K\)-stable.

These elements generate the whole group. Polar decomposition gives
\(g=k\exp H\): diagonalize the positive matrix \((g^*g)^{1/2}\)
by the spectral theorem and take the logarithms of its positive
eigenvalues. The resulting \(H\) is real symmetric or complex
Hermitian and belongs to the real Lie algebra. Any negative real
determinant is carried by \(k\in O(n)\), so both real components
are included. Thus \(V\), and likewise \(W\), is an actual closed
\(G\)-subrepresentation.
Only elementary finite-dimensional spectral theory is needed:
a Hermitian matrix has an eigenvector by maximizing its real
Rayleigh quotient on the unit sphere and differentiating there.
The orthogonal complement of that eigenvector is invariant, so
induction gives an orthonormal eigenbasis. For \(g^*g\), each
eigenvalue is strictly positive. Define its positive square root
and logarithm in this basis; \(k=g(g^*g)^{-1/2}\) is orthogonal or
unitary, and \(H=\log((g^*g)^{1/2})\) gives the claimed factorization.

Its core is exactly \(V_0\).
The projector \(P_\tau\) maps \(V_0\) into its finite-dimensional
type space \(V_0(\tau)\), closed in the ambient finite packet.
The projection of any limit in \(V\) therefore remains in this
space. A compact-finite limit is a finite sum of such projections,
and lies in \(V_0\). The reverse inclusion is immediate.
The same argument gives \(W_0\).

#### Step 4: Complete quotients and exact continuous core maps

The Fréchet quotient \(Q=V/W\) is complete. For an explicit argument,
use increasing seminorms \(p_j\). A Cauchy quotient sequence has a
subsequence whose successive differences have quotient \(p_j\)-seminorm
less than \(2^{-j}\). Choose lifts of those differences with
\(p_j<2^{-j+1}\). Their series converges in every fixed seminorm
of the complete \(V\); its sum lifts the quotient limit, and the
original Cauchy sequence has the same limit.

All smooth orbit maps and differentiated actions pass to the quotient.
Its seminorms
\[
\bar p_N(v+W)=\inf_{w\in W}p_N(v+w)                    \tag{1.32l}
\]
inherit the moderate bound (1.31h), since \(\mathcal I(g)W=W\).
For a compact-finite quotient vector, apply the finite sum of its
compact-type projectors to any lift. This produces a lift in
\(V_0\), with kernel \(W_0\). Thus the quotient core is exactly
\(V_0/W_0\), and the inclusion and quotient are the actual continuous
maps asserted in Theorem 1.26a. The operators \(A_N\) give core density.

If that core is irreducible, a nonzero closed group-stable subspace
of \(Q\) has a nonzero core vector by these approximate identities.
Difference quotients give Lie stability of its core. Irreducibility
makes it contain all \(Q_0\), and density makes it equal to \(Q\).
This proves topological irreducibility.

#### Step 5: Actual duals, annihilators and coefficient lifts

Under the continuous invariant ambient pairing let
\[
\operatorname{Ann}(V)=
\{\widetilde f\in\widetilde I:
\langle v,\widetilde f\rangle=0\text{ for all }v\in V\}.
\tag{1.32m}
\]
It and \(\operatorname{Ann}(W)\) are closed group-stable spaces.
Their cores are the algebraic annihilators of \(V_0,W_0\).
They are the closures of those cores: \(A_N\) preserves the
annihilator, since its compact adjoint preserves the original
\(K\)-stable space. Its outputs are core vectors and converge
in the smooth topology. Pairing with the dense original core
is equivalent to pairing with its closure.

Finite-dimensional packet duality gives
\[
W_0^\perp/V_0^\perp\simeq(V_0/W_0)^\vee.               \tag{1.32n}
\]
To check surjectivity, pull a finite-packet functional back to \(V_0\),
extend it to the ambient finite packet by linear algebra, and represent
it by the compact pairing. Extend by zero to all other packets.
It annihilates \(W_0\); its restriction is the given functional,
and the kernel of restriction is \(V_0^\perp\).
Invariance of the pairing makes this identification Lie- and
compact-equivariant, so no exact dual functor is being assumed.

There is also exact double-annihilator recovery in these models.
If every finite compact projection of \(v\in I\) lies in \(V_0\),
then each finite-range \(A_Nv\) lies in \(V_0\), and their smooth
convergence puts \(v\) in \(V\). If a projection lies outside \(V_0\),
finite-packet duality provides a core vector in
\(\operatorname{Ann}(V)\) pairing nontrivially with it; compact
adjunction gives such a vector pairing nontrivially with \(v\).
Consequently \(\operatorname{Ann}(\operatorname{Ann}(V))=V\),
and likewise for \(W\). Thus the constructed double dual is
literally paired with \(Q\); coefficient inversion loses no core
coefficients in Step 8 of this argument.

The ambient pairing descends jointly continuously to \(Q\times Q^\vee\).
Minimize its seminorm bound over both lifts to obtain quotient
seminorm bounds. It is nondegenerate on the whole models:
a nonzero vector has a nonzero finite compact projection, by
convergence of \(A_N\), and the finite packet pairing detects it.
Compact adjunction then detects the original vector.

In particular every smooth paired coefficient is literally
\[
\langle Q(g)(v+W),\widetilde f+\operatorname{Ann}(V)\rangle
=\langle I(g)v,\widetilde f\rangle,\quad
v\in V,\ \widetilde f\in\operatorname{Ann}(W).
\tag{1.32o}
\]
Both core vectors have core lifts by Step 4 of this argument. Changing either
lift changes the function by zero for all \(g\), by group stability.
All normalized bounds from Theorem 1.26 descend by infima over lifts,
and its complete Fourier equation descends too. This completes
Theorem 1.26a, including its genuine continuous maps.

#### Step 6: The polynomial correction and its finite attainment

Let \(J_Q\) be the span in \(\mathbb C[s]\) of
\[
Z_Q(s,\Phi,c)/L_{\boldsymbol\chi}(s),\quad
\Phi\text{ polynomial Gaussian},\quad c\text{ paired core coefficient}.
\tag{1.32p}
\]
These values are polynomials by Theorem 1.26 and (1.32o). The radial
identity (1.31x) makes their span an ideal.
It is nonzero: choose core vectors with nonzero pairing, so their
coefficient is nonzero near the identity, and a compact test inside
\(G\) giving a nonzero integral in a right half-plane.
The actual earlier Hermite theorem, Lemma 3.1 and Theorem 3.2 in
*Hermite functions, tempered distributions and the Schwartz kernel
theorem*, proves polynomial-Gaussian Schwartz density after dilation.
The continuous normalized bound of Theorem 1.26 therefore approximates
that nonzero value by one of (1.32p).

Choose a monic nonzero ideal element \(P_Q\) of least degree.
Polynomial division of any other element leaves a smaller-degree
remainder in the ideal, which must vanish. Hence \(J_Q=P_Q\mathbb C[s]\).
By the definition of its span, this chosen polynomial is an actual
finite sum of polynomial multiples of integral values. Thus
\[
\sum_{\alpha=1}^r p_\alpha(s)Z_Q(s,\Phi_\alpha,c_\alpha)
=P_Q(s)L_{\boldsymbol\chi}(s).     \tag{1.32q}
\]
The actual test operator \(\mathscr S\) in (1.31xa) absorbs each
\(p_\alpha\) into \(\Phi'_\alpha=p_\alpha(\mathscr S)\Phi_\alpha\).
These are still fixed polynomial Gaussians, and consequently
\[
\sum_{\alpha=1}^r Z_Q(s,\Phi'_\alpha,c_\alpha)=L_Q(s).
\tag{1.32qa}
\]
This proves the exact ideal and finite attainment, not an unspecified
common meromorphic majorant.

#### Step 7: Entire division for the whole family; no zeros

The functions \(H=Z_Q/L_{\boldsymbol\chi}\) are entire and jointly
continuous with compact-parameter bounds from Step 5 of this argument.
For a core coefficient, approximate any Schwartz test by polynomial
Gaussians. The resulting \(H\)'s converge locally uniformly.
Cauchy's derivative formula preserves every zero multiplicity of
\(P_Q\) in the limit, so \(H/P_Q\) is entire.
Next approximate both arbitrary smooth coefficient vectors by their
core \(A_N\)-approximants. The joint bounds give the same locally
uniform convergence, hence the same conclusion for every smooth
paired coefficient.

Continuity after division is explicit. Surround the finitely many
roots of \(P_Q\) by circles avoiding roots on their boundaries.
Cauchy's formula for \(H/P_Q\) bounds it on inner disks by a fixed
constant times the controlled \(H\) on those circles.
On the complement \(1/P_Q\) is bounded. The same finite Schwartz
and quotient-vector seminorms therefore control the entire normalized
family on any compact parameter set.

For any \(s_0\), take a nonzero core coefficient and a nonnegative
smooth cutoff \(\eta\) in a compact subset of \(G\) on which it
is nonzero. The following test, extended by zero, is Schwartz:
\[
\Phi(g)=\eta(g)\overline{c(g)}
\nu(g)^{-i\operatorname{Im}s_0}.
\tag{1.32r}
\]
Its compact-support integral is entire, and
\[
Z_Q(s_0,\Phi,c)
=\int_G\eta(g)|c(g)|^2
\nu(g)^{\operatorname{Re}s_0+(n-1)/2}\,dg>0.       \tag{1.32s}
\]
The proved entire normalized quotient would make this value zero
if \(L_Q(s_0)=0\). Therefore \(L_Q\) has no zeros.
Every root of \(P_Q\) cancels an inducing-product pole, with no
excess multiplicity. This does not yet identify which roots occur
for every standard-module label.

#### Step 8: Exact reflection, constant epsilon and conjugation

The raw Fourier equation descended from the actual kernel is
\[
\frac{Z_{Q^\vee}(1-s,\widehat\Phi,c^\vee)}
{L_{\boldsymbol\chi^{-1}}(1-s)}
=\epsilon_{\boldsymbol\chi}
\frac{Z_Q(s,\Phi,c)}{L_{\boldsymbol\chi}(s)}.
\tag{1.32t}
\]
Fourier is a bijection of the polynomial-Gaussian space.
Coefficient inversion is a bijection of the two core coefficient
families by the perfect dual pairing. Taking their polynomial spans
and using the automorphism \(s\mapsto1-s\) of \(\mathbb C[s]\) gives
\[
P_{Q^\vee}(1-s)\mathbb C[s]=P_Q(s)\mathbb C[s].          \tag{1.32u}
\]
The units of this ring are nonzero constants. The two monic
polynomials have equal degree \(b\); comparison of the reflected
leading coefficients gives exactly the constant \((-1)^b\).
This proves (1.32d)--(1.32e), including absolute value one of epsilon
by the exact scalar phases in (1.31e).
The central sign check (1.31ab) survives the correction:
the two correction degrees agree and contribute \((-1)^{2b}=1\).
The character-change calculation (1.31ac) applies verbatim because
the positive and angular central actions descend to \(Q\). Thus
\[
\epsilon_Q(s,\psi_{F,a})
=\omega_Q(a)|a|_F^{n(s-1/2)}\epsilon_Q.
\tag{1.32ua}
\]
For a unitary core, the central character has modulus one: its
radial Lie scalar is purely imaginary by skew Hermitian invariance,
and its compact angular/sign action is unitary by invariance of the
positive form. Hence (1.32ua) has modulus one on
\(\operatorname{Re}s=1/2\), including every changed basic character.

Conjugation of the actual compact model changes \(t_j\) to \(\bar t_j\),
keeps real parity and negates complex angular weights.
Conjugate closures and quotients are the actual constructed models.
The Euler gamma integral and continuation give
\(L_{\overline{\boldsymbol\chi}}(s)
 =\overline{L_{\boldsymbol\chi}(\bar s)}\).
Conjugation preserves the Gaussian polynomial space and conjugates
every coefficient. The normalized ideal is consequently the
coefficientwise conjugate ideal. Its unique monic generator is
\(\overline{P_Q(\bar s)}\), proving (1.32f) with no unknown scalar.

#### Step 9: Coefficient independence and the unitary normalization

Two constructed models with isomorphic cores and identified dual-core
pairings have the same core coefficient functions.
Indeed these functions are real analytic by Step 2 of this argument and (1.32o).
Every Taylor derivative at the identity is the paired core action
of an enveloping-algebra operator, hence agrees under the isomorphism.
Analyticity gives equality on a neighborhood and its connected
component. Each other component has a representative in \(K\);
the isomorphism preserves that action, so the same reasoning covers
every component. Thus their unnormalized Gaussian ideals agree.
This assertion concerns the **constructed principal subquotient
models**, not comparison with an arbitrary other smooth realization.

An invariant positive Hermitian form on \(Q_0\) identifies
\(\bar Q_0\) with its admissible contragredient.
It is onto on every finite compact packet by finite-dimensional
Hermitian duality, and the direct sum of packets gives the core
isomorphism. Skew Lie invariance and compact invariance make it
an intertwiner. The preceding coefficient independence therefore
shows that \(L_{Q^\vee}\) and \(L_{\bar Q}\) differ by a nonzero constant.

That constant is one. The positive central infinitesimal scalar is
\(d\sum t_j\); skew Hermitian invariance forces
\(\operatorname{Re}\sum t_j=0\).
The inverse-character and conjugate-character inducing products
have the same parity/angular shifts, and their norm-exponent sums
are \(-\sum t_j=\sum\bar t_j\). Their correcting polynomials have
equal degree, by reflection and conjugation, and are monic.

We need only the elementary ratio asymptotic
\[
\frac{\Gamma(u+\alpha)}{\Gamma(u)u^\alpha}\longrightarrow1
\quad(u\to+\infty)                         \tag{1.32v}
\]
for fixed complex \(\alpha\). To prove it, let \(Y_u\) have density
\(e^{-y}y^{u-1}/\Gamma(u)\) on \(y>0\).
Gamma recurrence gives mean \(\mathbb E(Y_u/u)=1\) and variance
\(1/u\), so \(Y_u/u\to1\) in probability.
For an integer \(A>|\operatorname{Re}\alpha|+2\), recurrence also
bounds uniformly its positive and negative \(A\)-moments for
\(u>A+1\). Outside \([R^{-1},R]\), use the strictly smaller exponent
\(\operatorname{Re}\alpha\) and these moments to bound the tails
of \((Y_u/u)^\alpha\) by a quantity tending to zero with \(R\).
Inside that interval this is a bounded continuous function and
convergence in probability gives expectation tending to one.
Its expectation is the left side of (1.32v), by the Euler integral.
This proves the asymptotic without a quoted Stirling theorem.

Hence \(\Gamma_{\mathbb R}(s+\alpha)/\Gamma_{\mathbb R}(s)
 \sim(s/(2\pi))^{\alpha/2}\) and
\(\Gamma_{\mathbb C}(s+\alpha)/\Gamma_{\mathbb C}(s)
 \sim(s/(2\pi))^\alpha\) for real \(s\to+\infty\).
The equal shift sums make the inverse/conjugate inducing-product
ratio tend to one. The equal-degree monic polynomial ratio also
tends to one. Their constant ratio is therefore one, proving (1.32g).

#### Precise unclosed part of the original target

Theorem 1.26a provides actual continuous maps and paired models for
every algebraic principal-core subquotient, and Theorem 1.26b proves
its exact Gaussian ideal and finite attainment as a **finite
polynomial correction** of the explicit inducing gamma product.
That correction is defined by the integrals, not an imported
classification statement.

Theorems 1.27–1.31 below prove principal-core occurrence and transfer
the Gaussian package to every prescribed actual complete smooth
moderate dual-pair realization. Theorems 1.32–1.34 below construct a compatible actual realization
for every abstract irreducible admissible core. Explicit identification of
\(P_Q\) and its scalar with the intended real character/discrete-series
or complex angular standard gamma factors also remains required.
LG-LLC-01's unproved classification and the rank-two kernel are not
being used to supply them.

The prior programme inputs are the actual scalar Fourier/Tate
proofs used in Theorem 1.26 and actual polynomial-Gaussian Schwartz
density, *Hermite functions, tempered distributions and the Schwartz
kernel theorem*, Lemma 3.1 and Theorem 3.2.
All compact, analytic-core, closure, quotient, annihilator, ideal,
reflection and gamma-ratio arguments used here are written above.
Goldfeld--Jacquet's free author notes §3,
[Goldfeld–Jacquet, freely accessible author notes](https://www.math.columbia.edu/~goldfeld/LanglandsBookChapter.pdf),
are a locator for the general target, not a substitute for these
proofs or for the still-missing classification.

### Finite generation over the minimal nilpotent algebra for real and complex general linear groups

Let \(F=\mathbb R\) or \(\mathbb C\), \(G=GL_n(F)\),
\(K=O(n)\) or \(U(n)\), and \(N\) the upper unitriangular group.
All enveloping algebras and Harish-Chandra modules below are over
\(\mathbb C\). Thus \(\mathfrak g\) denotes the complexification of
the real Lie algebra, and \(\mathfrak n,\mathfrak k\) denote the
corresponding complexifications.
An admissible module means a compatible \((\mathfrak g,K)\)-module
with finite-dimensional compact isotypic packets. Compact-finite
vectors have finite-dimensional \(K\)-orbits.

**Theorem 1.27.** Every irreducible admissible
\((\mathfrak g,K)\)-module \(V_0\) for \(GL_n(\mathbb R)\) or
\(GL_n(\mathbb C)\) is finitely generated over \(U(\mathfrak n)\).
Consequently \(V_0/\mathfrak n^qV_0\) is finite-dimensional for
every positive integer \(q\). The same statements hold for lower
unitriangular \(\mathfrak n\).

This is an algebraic statement about an arbitrary core. No
globalization, subrepresentation, Jacquet nonvanishing or
classification theorem is used.

#### Step 1: Finite core generators and the required central operators

Choose a nonzero compact-finite vector \(v\) and let \(W\) be its
finite-dimensional \(K\)-orbit span. Then \(U(\mathfrak g)W=V_0\):
the former is a nonzero Lie- and compact-stable subspace, because
\(\operatorname{Ad}(K)\) preserves every finite-degree part of the
enveloping algebra. Irreducibility gives equality.

Use the total-degree filtration on the enveloping algebra.
Only the following spanning statement is needed. In a word of
Lie generators, exchanging an out-of-order adjacent pair replaces
their difference by a single commutator and therefore lowers the
word length. Induction first on length and then on the number of
inversions expresses each word in ordered monomials. Commutators
have smaller length, so the leading symbols commute and there is
a surjection \(S(\mathfrak g)\twoheadrightarrow
\operatorname{gr}U(\mathfrak g)\). No linear-independence assertion
about these ordered monomials is required: this surjection and
their spanning suffice for every graded quotient used below.

For a matrix algebra, the invariant polynomial
\(\operatorname{tr}(X^r)\) has an invariant symmetrization \(C_r\)
in its enveloping algebra. Explicitly, under the trace identification,
its symbol is
\[
 p_r=\sum_{i_1,\ldots,i_r}
       E_{i_1i_2}E_{i_2i_3}\cdots E_{i_ri_1}.             \tag{1.33a}
\]
Symmetrization averages each degree-\(r\) monomial over all orders.
It commutes with every adjoint derivation, since applying a
derivation before or after the average gives the same sum.
The polynomial \(p_r\) is adjoint-invariant, because differentiating
\(\operatorname{tr}(e^{tY}Xe^{-tY})^r\) gives zero.
Thus \(C_r\) commutes with every Lie generator and with the full
compact group.

For the real group use \(r=1,\ldots,n\) in
\(\mathfrak g=\mathfrak{gl}_n(\mathbb C)\).
For the complex group
\[
 \mathfrak g=\mathfrak{gl}_n(\mathbb C)\oplus
                         \mathfrak{gl}_n(\mathbb C),\qquad
 \mathfrak k=\{(X,-X^t):X\in\mathfrak{gl}_n(\mathbb C)\};
                                                               \tag{1.33b}
\]
use these \(n\) central operators from the first summand.
This description follows by complexifying the real map
\(Y\mapsto(Y,\bar Y)\); for skew-Hermitian \(Y\),
\(\bar Y=-Y^t\).

Each \(C_r\) acts by a scalar \(\lambda_r\) on \(V_0\).
Indeed it preserves every finite compact packet. On any nonzero
such packet it has an eigenvector over \(\mathbb C\).
The kernel of \(C_r-\lambda_r\) is a nonzero Lie- and
compact-stable subspace, so is the whole irreducible module.
This argument uses neither an infinite-dimensional Schur theorem
nor the Harish-Chandra isomorphism.

Filter \(V_0\) by \(V_j=U_j(\mathfrak g)W\).
Its associated graded is a finitely generated symmetric-algebra
module. The symbols of \(\mathfrak k\) kill its generators:
\(\mathfrak kW\subset W\), so this action has degree zero.
The symbols \(p_r\) also kill the entire graded module, because
\((C_r-\lambda_r)V_0=0\). Commutativity of the symbols now gives
a surjection
\[
 \left(S(\mathfrak g)/
        (\mathfrak k,p_1,\ldots,p_n)\right)\otimes W
                      \longrightarrow \operatorname{gr}V_0.
                                                               \tag{1.33c}
\]
We prove directly that the algebra on the left is finite over
the image of \(S(\mathfrak n)\).

#### Step 2: The finite commutative calculation

Over the real group, quotienting by \(\mathfrak k\) sets
\(E_{ij}=E_{ji}\). Write \(a_i=E_{ii}\), and
\(y_{ij}=E_{ij}=E_{ji}\), \(i<j\). The quotient is
\[
 \mathbb C[y_{ij}:i<j]\,[a_1,\ldots,a_n],
                                                               \tag{1.33d}
\]
with the off-diagonal polynomial ring precisely the image of
\(S(\mathfrak n)\). The symbols \(p_r\) are traces of powers
of the symmetric symbol matrix having diagonal \(a_i\) and
off-diagonal entries \(y_{ij}\).

For the complex group, the relations in (1.33b) set
\(E_{ij}^{(1)}=E_{ji}^{(2)}\). The upper entries in the first
summand and the upper entries in the second supply all off-diagonal
entries of one unrestricted symbol matrix. Its diagonal entries
\(a_i=E_{ii}^{(1)}=E_{ii}^{(2)}\) supply the remaining variables.
Again the quotient has the form (1.33d), now with all ordered
off-diagonal entries, and their polynomial ring is the image of
\(S(\mathfrak n)\). The selected first-summand \(p_r\)'s are exactly
the traces of powers of this unrestricted symbol matrix.

Give diagonal variables degree one and off-diagonal variables
degree zero. In either case,
\[
 p_r=\sum_i a_i^r+\text{terms of diagonal degree less than }r.
                                                               \tag{1.33e}
\]
For a term using an off-diagonal matrix entry, at least one factor
is off-diagonal, so the asserted strict inequality follows directly
from (1.33a).

Newton's identities imply that the ideal \((p_1,\ldots,p_n)\)
also contains characteristic-polynomial coefficients \(Q_r\)
whose leading diagonal terms are the elementary symmetric
polynomials \(e_r(a)\), \(r=1,\ldots,n\).
Here the identities can be obtained without any invariant-theory
input: for indeterminates \(z_i\),
differentiate \(\prod_i(1+z_it)\), divide formally by that product,
and compare coefficients with
\(\sum_i z_i/(1+z_it)\).
This gives
\[
 r e_r=\sum_{j=1}^r(-1)^{j-1}e_{r-j}\sum_i z_i^j,
 \quad e_0=1.
                                                               \tag{1.33f}
\]
Applying these polynomial formulas to the \(p_j\)'s gives \(Q_r\),
and (1.33e) gives \(Q_r=e_r(a)+R_r\) with
\(\deg_a R_r<r\).

In the quotient by these relations, use the elementary identity
\[
 a_i^n=\sum_{r=1}^n(-1)^{r+1}e_r(a)a_i^{n-r}
       =\sum_{r=1}^n(-1)^rR_r a_i^{n-r}.
                                                               \tag{1.33g}
\]
The first equality evaluates
\(\prod_j(T-a_j)\) at \(T=a_i\).
Every term on the final right side has diagonal degree at most
\(n-1\). Whenever a diagonal monomial has an exponent at least
\(n\), (1.33g) therefore lowers its total diagonal degree.
Iteration terminates and leaves a combination, over the
off-diagonal ring, of the finite list
\[
 a_1^{b_1}\cdots a_n^{b_n},\qquad 0\le b_i<n.             \tag{1.33h}
\]
Thus (1.33c) is finite over \(S(\mathfrak n)\).
No assertion about a polynomial gamma majorant or a standard-module
classification enters this finite calculation.

#### Step 3: Lifting generators and finite Jacquet quotients

Lift the finitely many generators (1.33h) times a basis of \(W\)
to actual vectors of \(V_0\). They generate \(V_0\) over
\(U(\mathfrak n)\): for a vector of filtration degree \(j\),
its leading symbol is a combination of the lifted generators
with nilpotent-algebra symbols; subtract the corresponding
enveloping-algebra combination to lower the filtration degree.
Induction on \(j\) finishes the argument.

Let \(I=\mathfrak nU(\mathfrak n)\) be the augmentation ideal.
If \(V_0\) has \(r\) nilpotent-algebra generators, there is a
surjection
\[
 (U(\mathfrak n)/I^q)^r\longrightarrow V_0/I^qV_0.
                                                               \tag{1.33i}
\]
Ordered monomials of length at least \(q\) belong to \(I^q\);
hence the quotient on the left is spanned by the finite list
of monomials of length less than \(q\).
This proves finite dimension without identifying \(I^q\)
with a PBW filtration piece.
The notation \(\mathfrak n^qV_0\) means exactly \(I^qV_0\).
The quotient is stable under the diagonal Lie algebra and the
compact diagonal subgroup, since their adjoint actions preserve
\(\mathfrak n\) and every power of its augmentation ideal.

The long permutation matrix in \(K\) exchanges upper and lower
unitriangular groups. Transporting the proof by that matrix gives
the lower-nilpotent statement and completes Theorem 1.27.

#### Scope

Theorem 1.27 supplies finite minimal Jacquet quotients for every abstract
irreducible admissible core. It does not assert that the first
quotient is nonzero: an augmentation ideal is not automatically
the Jacobson radical of its enveloping algebra, so a bare use of
Nakayama's lemma here would be invalid.
Theorem 1.28 below proves that nonvanishing for a supplied actual
dual pair. Theorems 1.32–1.34 then prove nonvanishing and construct a
compatible complete smooth moderate realization for every abstract
irreducible admissible core.

The free primary locator is Casselman's *Canonical extensions of
Harish-Chandra modules to representations of G*, §5, available as
the publisher's freely accessible PDF:
[Casselman, publisher open-access edition](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/90CFF3C365389AA3AEE897611EC8DE2D/S0008414X00000523a.pdf/canonical-extensions-of-harish-chandra-modules-to-representations-of-g.pdf).
Its cited finite-generation and nonvanishing results are not
being imported in place of the proofs written here.

### Nonzero minimal Jacquet quotients and actual algebraic Borel occurrence

Let \(G=GL_n(F)\), \(F=\mathbb R\) or \(\mathbb C\), with
the upper unitriangular group \(N\), upper triangular group \(B\)
and maximal compact group \(K\). Suppose \(E,\widetilde E\) are
actual complete Hausdorff locally convex smooth moderate-growth
representations, with continuous differentiated actions and a jointly
continuous nondegenerate invariant pairing
\[
 B_E:E\times\widetilde E\longrightarrow\mathbb C .
 \tag{1.34a}
\]
Their compact-finite cores are \(V_0,\widetilde V_0\), with
\(\widetilde V_0\) the admissible contragredient, and \(V_0\) is
irreducible admissible. Moderate growth means that for each continuous
seminorm \(p\) there are a continuous seminorm \(q\), \(C\) and \(A\)
such that
\[
 p(\pi(g)v)\le C H(g)^Aq(v),\qquad
 H(g)=1+\|g\|+\|g^{-1}\| .                               \tag{1.34b}
\]
The actions are jointly continuous. No prescribed realization is
replaced by an unstated canonical completion.

**Theorem 1.28.** Under these hypotheses, \(V_0/\mathfrak nV_0\ne0\).
It is finite-dimensional by Theorem 1.27. There are smooth diagonal
characters \(\chi_1,\ldots,\chi_n\) and an explicit injective
\((\mathfrak g,K)\)-map
\[
 T_0:V_0\longrightarrow I_0(\chi_1,\ldots,\chi_n)          \tag{1.34c}
\]
into the compact-finite core of the full normalized Borel induction.
The same assertion holds for \(\widetilde V_0\). Transposing its
injection on finite compact packets gives a surjective core map
from a full inverse-character Borel induction onto \(V_0\).

This proves occurrence in every rank and for both fields for every
core having the stipulated actual realization, including the
compatible smooth cuspidal realizations supplied by lesson04
Theorem 1.19. It does not claim existence of those realizations for an
arbitrary abstract core. It also does not assert continuity of the
algebraic \(T_0\) on \(E\).
Removing or restoring a central norm twist does not restrict this
scope: multiply the paired actions by that character and its
inverse. Their pairing stays invariant, and the norm character
and its inverse are bounded by fixed powers of \(H(g)\), so
smoothness, completeness and moderate growth persist.

#### Step 1: Compact smoothing and fixed finite generators

The compact-finite core is dense in each supplied topology.
One can check this directly using the polynomial class functions
\[
 q_K(k)=\frac{1+\operatorname{Re}\operatorname{tr}(k)/n}{2},
 \qquad
 A_m v=\frac{\int_Kq_K(k)^m\pi(k)v\,dk}{\int_Kq_K(k)^m\,dk}.
 \tag{1.34d}
\]
They are positive approximate identities: away from an identity
neighborhood \(q_K\le c<1\), whereas a smaller neighborhood has
\(q_K\ge c'>c\) and positive Haar mass. Its relative exterior mass
is at most \((c/c')^m/\operatorname{mass}(U')\).
Joint continuity gives \(A_m v\to v\) in every seminorm.
The integrals exist by compact Riemann sums and completeness.
Under left or right compact translation the polynomial kernel
has finite-dimensional orbit, so the output is compact-finite.
This proves density without a globalization theorem.
Compact character projectors are continuous by the same integration
and finite-dimensional Schur orthogonality. Their ranges are exactly
the finite isotypic packets in the given core.

The contragredient core is irreducible. If a nonzero proper
submodule \(U\subset\widetilde V_0\) existed, some finite compact
packet of \(U\) would be proper in the corresponding dual packet.
Finite-dimensional duality gives a nonzero vector annihilating
\(U\). The annihilator in \(V_0\) is Lie- and compact-stable, hence
equals \(V_0\), contradicting \(U\ne0\). Here an entire proper
submodule cannot fill every packet, since the core is their
algebraic direct sum. Thus both cores are finitely generated over
\(U(\mathfrak g)\) by finite compact-stable spaces.

We require the following elementary strengthening in an actual
realization. Choose a finite set of compact types whose *entire*
isotypic packets \(W\) contain core generators. Their sum \(W\)
is finite-dimensional. Let \(P_W\) be their character projector.
Choose nonnegative smooth approximate identities \(h_\epsilon\)
on \(G\), supported near the identity, with integral one.
Then
\[
 A=P_W\pi(h_\epsilon)P_W|_W
 \tag{1.34e}
\]
is arbitrarily close to identity on the finite space \(W\), hence
invertible for small \(\epsilon\). Both compact convolutions convert
\(h_\epsilon\) into one bi-compact-finite \(h\in C_c^\infty(G)\);
its support lies in the compact set \(K\operatorname{supp}
(h_\epsilon)K\).
For \(w\in W\), \(w=\pi(h)A^{-1}w\).

Every core vector is a finite sum \(D w\), \(D\in U(\mathfrak g)\),
\(w\in W\). Differentiation under the compactly supported convolution
and integration by parts express \(D\pi(h)w'\) as \(\pi(h_D)w'\),
with \(h_D\in C_c^\infty(G)\). The sign and left/right differentiation
are fixed by the identity
\(\pi(\exp(tX))\pi(h)=\pi(h(\exp(-tX)\,\cdot))\).
Consequently every core vector has a representation
\[
 \sum_{j=1}^r\pi(f_j)w_j,\qquad f_j\in C_c^\infty(G),     \tag{1.34f}
\]
with a *fixed* finite list \(w_1,\ldots,w_r\in W\).
The functions may depend on the vector. Apply the same construction
to the contragredient supplied realization.

#### Step 2: One coefficient-growth exponent for every dual core vector

There are a continuous seminorm \(Q\) on \(E\) and one exponent
\(A\) such that for each \(\widetilde v\in\widetilde V_0\)
there is a finite constant \(C_{\widetilde v}\) with
\[
 |B_E(\pi(g)v,\widetilde v)|
       \le C_{\widetilde v}H(g)^A Q(v)
 \quad(v\in E,\ g\in G).                                \tag{1.34g}
\]
The exponent and the seminorm do not change when
\(\widetilde v\) is differentiated any fixed number of times.

Indeed choose the fixed generators \(\widetilde w_j\) in (1.34f).
Joint continuity bounds all \(B_E(v,\widetilde w_j)\) by one
continuous seminorm \(p(v)\). Apply (1.34b) to that one \(p\);
this gives a single \(Q,A\).
For \(\widetilde v=\sum_j\widetilde\pi(f_j)\widetilde w_j\),
invariance gives
\[
 B_E(\pi(g)v,\widetilde v)
   =\sum_j\int_G f_j(h)
           B_E(\pi(h^{-1}g)v,\widetilde w_j)\,dh .
 \tag{1.34h}
\]
The elementary norm satisfies \(H(h^{-1}g)\le C H(h)H(g)\).
Insert the bound just obtained and integrate
\(|f_j(h)|H(h)^A\), finite by compact support. This proves (1.34g).
Every differentiated dual core vector is still in the same core,
so (1.34f) gives its own finite constant and exactly the same \(Q,A\).
No unproved uniform asymptotic estimate is being used.

#### Step 3: A bounded radial finite jet system

We prove the precise fact about compact-finite coefficient functions
that will prevent arbitrary exponential decay.
Let \(f\) be a smooth function on \(G\), finite under both compact
translations, and with a scalar action of the selected matrix
central operators. Its finite compact translation span identifies
the restriction to
\[
 a(x)=\operatorname{diag}(e^{x_1},\ldots,e^{x_n})
 \tag{1.34i}
\]
with a vector \(F(x)\) in a fixed finite-dimensional space.
Using all finite left/right translates avoids choosing a single
possibly vanishing radial component.

Fix a chamber with \(|x_i-x_j|\ge\eta>0\), and its part in
which the signs of those differences do not change.
Each central trace operator of degree \(r\), normalized as specified
below, has radial expression
\[
 \mathcal C_r F
     =\sum_i\partial_{x_i}^{\,r}F+L_rF,\qquad
        \operatorname{ord}_x L_r\le r-1,                 \tag{1.34j}
\]
where the coefficients of \(L_r\), and every fixed number of their
derivatives, are bounded on this chamber portion. They are matrices
on the finite compact translation space.

Here is the coordinate computation, including the bounds.
For \(r_i=e^{x_i}\), the right vector field \(E_{ij}\), \(i\ne j\),
at \(a\) is a combination of compact left and right fields.
Over \(\mathbb R\), take \(K_{ij}=E_{ij}-E_{ji}\). Solving
\(aE_{ij}=uK_{ij}a+v aK_{ij}\) gives exactly
\[
 u=\frac{r_ir_j}{r_j^2-r_i^2}
     =\frac1{2\sinh(x_j-x_i)},\qquad
 v=-\frac{r_i^2}{r_j^2-r_i^2}
     =-\frac1{e^{2(x_j-x_i)}-1}.                         \tag{1.34k}
\]
The analogous expression for \(E_{ji}\) uses
the same \(u\) and \(v=-r_j^2/(r_j^2-r_i^2)\).
These formulas follow by comparing the two off-diagonal entries,
so introduce no integration or asymptotic theorem.
For \(\mathbb C\), the compact generators
\(E_{ij}-E_{ji}\) and \(i(E_{ij}+E_{ji})\) solve the two
real off-diagonal systems; the same denominators and bounded
ratios occur. Imaginary diagonal generators are compact fields,
and real diagonal generators are \(\partial_{x_i}\).

All the displayed coefficients and their derivatives are bounded
when the gap has magnitude at least \(\eta\). Derivatives only
produce rational expressions in \(e^{x_j-x_i}\) with the same
excluded zero denominator; at either infinite endpoint they
have finite limits or tend to zero.
The local compact-angular coordinate expressions away from identity
are obtained by conjugating the Lie generators by compact matrices.
Their fixed derivatives are bounded because compact adjoint
matrices and their derivatives are bounded. The same two-by-two
systems then apply. Diagonal compact redundancy in the complex
case is removed by choosing one compact torus factor rather than
two; it gives a compact derivative, not a growing radial coefficient.

Applying a product of \(r\) vector fields now gives bounded
coefficients on a finite sum of compact derivatives and radial
derivatives. The compact derivatives act by fixed matrices on
the chosen finite translation space.
Only products of the diagonal radial components can contribute
radial derivative order \(r\); differentiating any coefficient
lowers that order, and an off-diagonal generator has zero radial
component at \(a\). The invariant trace symbol restricts on the
diagonal to \(\sum_i\xi_i^r\).
This proves (1.34j) with every stated bound. Over the complex group
use \(2^r C_r^{(1)}\): the first-summand generator
\((E_{ii},0)\) has radial component
\(\tfrac12\partial_{x_i}\), its other component being compact.
Over the real group no such factor is present.

Newton's polynomial construction (1.33f) applied to these commuting
central operators gives degree-\(r\) central operators whose radial
expressions are
\[
 e_r(\partial_x)F+\mathcal L_rF=\mu_rF,\qquad
       \operatorname{ord}\mathcal L_r\le r-1,
                    \quad r=1,\ldots,n.                \tag{1.34l}
\]
All coefficient derivatives remain bounded, by finite products
and the product rule.
No Harish-Chandra isomorphism or radial formula has been assumed.

For each \(i\), the ordinary constant-coefficient identity
\[
 \partial_{x_i}^{\,n}
   =\sum_{r=1}^n(-1)^{r+1}
          \partial_{x_i}^{\,n-r}e_r(\partial_x)          \tag{1.34m}
\]
is the characteristic-polynomial identity used in (1.33g).
Apply (1.34l) to \(F\) on its right side. Every resulting term has
total radial order at most \(n-1\); its coefficients and fixed
derivatives are bounded.
Differentiate these equations to reduce every derivative whose
multi-index has some component at least \(n\). Each reduction
strictly lowers total derivative order, so it terminates.
Thus the finite jet
\[
 J(x)=\big(\partial_x^\alpha F(x)\big)_{0\le\alpha_i<n}
 \tag{1.34n}
\]
satisfies a first-order system
\[
 \partial_{x_i}J=A_i(x)J,\qquad \sup_x\|A_i(x)\|<\infty
 \tag{1.34o}
\]
on every such fixed-gap chamber portion. Only finitely many
derivatives of the bounded coefficients are needed to form
these matrices.

Along a ray \(x(t)=x^{(0)}-tH\) remaining in that portion,
\(J'(t)=A(t)J(t)\) with \(\|A(t)\|\le M\).
For a nonzero initial jet, the elementary integral inequality
for the backward equation gives
\[
 \|J(t)\|\ge e^{-Mt}\|J(0)\|,\qquad t\ge0.               \tag{1.34p}
\]
To check this without dividing by a possibly zero norm,
solve backwards from \(t\) and use the integral inequality
\(\|J(s)\|\le \|J(t)\|+\int_s^t M\|J(u)\|du\);
iteration of its integral series gives the factor \(e^{M(t-s)}\).
If \(J(t)=0\), this argument also forces \(J(0)=0\).

#### Step 4: Nonvanishing of the Jacquet quotient

For \(n=1\), \(\mathfrak n=0\), so there is nothing to prove.
For \(n\ge2\), suppose instead that \(V_0=\mathfrak nV_0\).
Then \(V_0=\mathfrak n^qV_0\) for every \(q\).
Choose a nonzero paired core coefficient
\[
 f(g)=B_E(\pi(g)v,\widetilde v);
 \tag{1.34q}
\]
one can choose its value at identity nonzero.
The function is finite under both compact translations.
Each chosen central operator acts by a scalar on the irreducible
core, by the finite-packet argument in Theorem 1.27.
The radial system in Step 3 of this argument therefore applies.

Choose a regular matrix near the identity where this coefficient
is nonzero. Such matrices have pairwise distinct singular values:
the discriminant of the characteristic polynomial of \(g^*g\)
is a nonzero polynomial in the real entries, so its zero set has
empty interior. Elementary diagonalization gives
\(g=k_1a(x^{(0)})k_2\), with \(x_1^{(0)}<\cdots<x_n^{(0)}\),
after a compact permutation. Including all finite compact translates
in \(F\) makes \(F(x^{(0)})\ne0\), hence \(J(x^{(0)})\ne0\).

Take real \(H_1>\cdots>H_n\), put
\(\epsilon=\min_i(H_i-H_{i+1})>0\), and use
\[
 a_t=\operatorname{diag}(e^{x_i^{(0)}-tH_i}).
 \tag{1.34r}
\]
The ordered gaps grow and stay bounded away from zero.
For every upper-root generator \(X_{ij}\), including its imaginary
companion over \(\mathbb C\),
\[
 \operatorname{Ad}(a_t)X_{ij}
   =e^{x_i^{(0)}-x_j^{(0)}}e^{-t(H_i-H_j)}X_{ij}.
 \tag{1.34s}
\]
Every fixed core vector \(w\), since it belongs to \(\mathfrak n^qV_0\),
is a finite sum \(X_1\cdots X_qw'\) with upper-root generators.
Apply (1.34s) to \(\pi(a_t)w\) and transfer those Lie generators
to the dual vector using invariance of (1.34a).
The bound (1.34g) uses the same exponent \(A\) for every resulting
dual core vector. Since \(H(a_t)\le C e^{Lt}\) with a fixed \(L\),
it gives
\[
 |B_E(\pi(a_t)w,\widetilde w)|
       \le C_{q,w,\widetilde w}
                   e^{(AL-q\epsilon)t}.                \tag{1.34t}
\]
Constants may depend on \(q\), but are finite and do not depend on
\(t\). This estimate therefore beats every prescribed exponential.

Each component of the finite radial jet (1.34n) is a coefficient
of fixed core vectors: radial derivatives differentiate the
commuting diagonal action on the original vector, and compact
translations remain in the core. Apply (1.34t) to its finitely many
components. Choosing \(q\epsilon>AL+M+1\) contradicts (1.34p)
as \(t\to\infty\).
Thus \(V_0/\mathfrak nV_0\ne0\).
This is a complete nonvanishing argument in the stated actual
realization scope; an external asymptotic expansion or a source
statement is not substituting for it.

#### Step 5: Explicit algebraic Frobenius map into a full Borel induction

By Theorem 1.27 the nonzero quotient \(V_0/\mathfrak nV_0\) is finite-dimensional.
The diagonal real Lie algebra commutes with \(M=B\cap K\)
on this quotient, and its operators commute with one another.
First split the finite compact diagonal action into its one-dimensional
characters. This follows by averaging a Hermitian form and
simultaneously diagonalizing the commuting unitary matrices; each
invariant eigenspace can be treated in turn.
On one nonzero compact-character subspace, commuting complex matrices
have a common eigenfunctional: choose an eigenspace for one transpose,
restrict the others to it and repeat until a common eigenvector
is obtained. Pulling it back gives a nonzero \(\ell_0:V_0\to\mathbb C\)
with
\[
 \ell_0(\mathfrak nV_0)=0,\qquad
 \ell_0(H_iv)=\beta_i\ell_0(v),\qquad
 \ell_0(mv)=\sigma(m)\ell_0(v).                          \tag{1.34u}
\]
Here \(H_i\) is the real diagonal \(E_{ii}\).
The sign weights of \(\sigma\) over \(\mathbb R\) are
\(e_i\in\{0,1\}\). Its circle weights over \(\mathbb C\)
are integers \(\ell_i\), since the smooth circle character
solves a constant differential equation and has period \(2\pi\).

Set \(\rho_i=(n+1)/2-i\) and \(d=[F:\mathbb R]\).
Choose
\[
 t_i=\beta_i/d-\rho_i,\qquad
 \chi_i(x)=\operatorname{sgn}(x)^{e_i}|x|^{t_i}
       \quad(\mathbb R),\qquad
 \chi_i(z)=(z/|z|)^{\ell_i}|z|_{\mathbb C}^{t_i}
       \quad(\mathbb C).
 \tag{1.34v}
\]
Then the infinitesimal Borel character of \(\ell_0\) is exactly
\(\delta_B^{1/2}\prod_i\chi_i\), including every factor \(d\).
The upper nilpotent action is trivial, and the compact diagonal
character matches the selected signs or angles.

In the actual compact model of full normalized induction define
\[
 (T_0v)(k)=\ell_0(kv),\qquad k\in K.                    \tag{1.34w}
\]
The finite compact orbit of \(v\) proves this is smooth and
compact-finite, with left \(M\)-covariance
\((T_0v)(mk)=\prod_i\chi_i(m_i)(T_0v)(k)\).
The action and the complete compact model are constructed in the
previous written Theorem 1.26; equivalently extend (1.34w) from \(K\)
by the row-QR formula \(g=bk\) and
\(f(bk)=\delta_B(b)^{1/2}\boldsymbol\chi(b)f(k)\).

It is a Lie intertwiner, as can be checked in compact coordinates.
For a real Lie generator \(X\), differentiate
\[
 k\exp(tX)=b(t,k)k'(t,k).
\]
At \(t=0\), its infinitesimal decomposition is
\(\operatorname{Ad}(k)X=Y_B+Y_K\), with
\(Y_B\) upper triangular with real diagonal, and \(Y_K\in\mathfrak k\).
The derivative of the inducing multiplier is its Borel character
on \(Y_B\), which equals \(\ell_0(Y_Bkv)/\ell_0(kv)\)
where that denominator is nonzero; without division the same
linear identity follows from (1.34u).
The compact derivative contributes \(\ell_0(Y_Kkv)\).
Their sum is
\[
 (dI(X)T_0v)(k)=\ell_0(\operatorname{Ad}(k)X\,kv)
               =\ell_0(kXv)=(T_0Xv)(k).                \tag{1.34x}
\]
Compact equivariance follows immediately by right translation.
Since \(\ell_0\ne0\), \(T_0\ne0\); its Lie- and compact-stable
kernel in an irreducible core is zero. This proves (1.34c).

Repeat for the supplied contragredient realization.
Each compact packet of its injection is an injective map of finite
spaces. Its transpose is surjective onto the dual packet.
The invariant compact pairing identifies the dual core of
\(I_0(\boldsymbol\chi)\) with \(I_0(\boldsymbol\chi^{-1})\);
the pairing is the explicit compact integral in Theorem 1.26.
Summing packet transposes therefore gives an actual surjective
\((\mathfrak g,K)\)-map
\[
 I_0(\boldsymbol\chi^{-1})\twoheadrightarrow V_0.
 \tag{1.34y}
\]
This is the dual-core occurrence/quotient interface; no closed-range
or continuous quotient theorem is concealed in the word “surjective.”

#### Step 6: The exact continuity boundary

If a selected algebraic \(\ell_0\) in (1.34u) extends to a continuous
functional \(\ell\) on the prescribed \(E\), its covariance integrates
to the actual Borel group: along each real diagonal one-parameter
group the functional satisfies the scalar differential equation,
along each upper unipotent one it is constant, and \(M\)-covariance
is already prescribed. The diagonal and elementary unipotent
generators generate \(B\).
Then
\[
 (Tv)(g)=\ell(\pi(g)v)                                  \tag{1.34z}
\]
is a continuous \(G\)-map \(E\to I(\boldsymbol\chi)\).
For each compact derivative, differentiation under this formula
and compact equicontinuity bound its compact \(C^\infty\) seminorm
by a continuous seminorm on \(E\). Compact equicontinuity itself
follows from a finite cover of \(K\) and joint continuity.
Its kernel is zero: a nonzero closed invariant kernel contains a
nonzero compact-finite vector by (1.34d), contradicting the injective
core map.

This last statement is an injection, without an asserted continuous
inverse or closed image. The proofs in this subsection do not establish that
every algebraic Borel eigenfunctional extends continuously, nor
that the image in (1.34z) is closed in the compact-smooth topology.
Theorem 2.0y below supplies a selected continuous Borel eigenfunctional
and the actual smooth injection in this complete moderate dual-pair
class, using exact principal synthesis and the paired distribution
embedding. The present subsection alone does not give that continuity.
Theorems 1.32–1.34 below construct a compatible realization of every
abstract irreducible admissible core. A continuous inverse or closed
image for comparison with another prescribed topology remains unproved.

The free primary comparison locator is Casselman's freely accessible
publisher paper, §§5,7–8:
[Casselman, publisher open-access edition](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/90CFF3C365389AA3AEE897611EC8DE2D/S0008414X00000523a.pdf/canonical-extensions-of-harish-chandra-modules-to-representations-of-g.pdf).
The finite-generation, radial, uniform-growth, nonvanishing and
core-occurrence proofs actually used above are written here.

### Analytic core coefficients and comparison of actual smooth models

Let \(F=\mathbb R\) or \(\mathbb C\), \(G=GL_n(F)\), and let
\((E,\widetilde E,B_E)\) be an actual smooth continuous paired
realization as in Theorem 1.28. Its compact-finite core \(V_0\) is
irreducible admissible, and the second core is its admissible dual.
The first assertion below needs smoothness and the core action;
moderate growth and completeness are needed only in the subsequent
topological applications, and are not substituted for analyticity.

**Theorem 1.29.** Every paired core coefficient
\[
 f_{v,\widetilde v}(g)=B_E(\pi(g)v,\widetilde v),
       \qquad v\in V_0,\quad \widetilde v\in\widetilde V_0,
 \tag{1.35a}
\]
is real analytic on \(G\).
If two actual smooth paired realizations have identified
\((\mathfrak g,K)\)-cores and the same core pairing, then all their
paired core coefficient functions are identical on \(G\).
Neither assertion identifies their complete topologies or proves
automatic continuity of an arbitrary algebraic core map.

#### Step 1: A scalar elliptic equation for a compact packet

On the real Lie algebra use the invariant nondegenerate symmetric
form
\[
 b(X,Y)=\operatorname{tr}(XY)\quad(F=\mathbb R),\qquad
 b(X,Y)=\operatorname{Re}\operatorname{tr}(XY)
                                      \quad(F=\mathbb C).
 \tag{1.35b}
\]
The Cartan decomposition is the direct sum of self-adjoint matrices
\(\mathfrak p\) and skew-adjoint matrices \(\mathfrak k_{\mathbb R}\).
The form is positive definite on the former and negative definite
on the latter; the two are orthogonal. Choose bases \(P_i\) and
\(K_j\) orthonormal for \(b\) and \(-b\), respectively. Put
\[
 C_G=\sum_iP_i^2-\sum_jK_j^2,\qquad
 C_K=-\sum_jK_j^2,\qquad
 \Delta=\sum_iP_i^2+\sum_jK_j^2=C_G-2C_K .
 \tag{1.35c}
\]
The tensor for \(C_G\) is invariant: in a basis and its \(b\)-dual,
the two commutator sums cancel by
\(b([X,Y],Z)=-b(Y,[X,Z])\). Applying multiplication into the
enveloping algebra gives \([X,C_G]=0\).
Conjugation by every element of \(K\) also preserves \(b\), so
\(C_G\) commutes with the full compact action.
Its scalar action \(\mu\) on \(V_0\) follows from the finite-packet
eigenvector and irreducibility argument in Theorem 1.27.

On a finite compact orbit, average any positive Hermitian form over
\(K\). The differentiated \(K_j\)'s are skew-Hermitian, and \(C_K\)
is Hermitian nonnegative. It is compact-invariant, because the sum
of squares of an orthonormal basis is invariant under the compact
adjoint action. Decompose the finite orbit into eigenspaces of
\(C_K\). A core vector is a finite sum of eigenvectors \(v_\kappa\)
with eigenvalues \(\kappa\ge0\).
For the coefficient of each \(v_\kappa\), right differentiation
\(R_Xf(g)=\frac{d}{dt}f(g\exp(tX))|_{t=0}\) gives
\[
 (\Delta-\mu+2\kappa)f_{v_\kappa,\widetilde v}=0.
 \tag{1.35d}
\]

In any real matrix-entry chart on \(G\), the vector fields \(R_X\)
have real analytic coefficients: matrix multiplication is
polynomial, and inversion on \(GL_n\) is analytic. The principal
symbol of \(\Delta\) is the sum of the squares of a real tangent
basis. It is positive definite. Thus (1.35d) is a scalar elliptic
equation with analytic coefficients. The analytic regularity
argument needed here is proved next.

#### Step 2: Interior estimates without an analytic-regularity citation

Consider on a real coordinate ball \(B_R\subset\mathbb R^m\) an
operator
\[
 P=\sum_{i,j}a_{ij}(x)\partial_i\partial_j
              +\sum_i b_i(x)\partial_i+c(x),
 \tag{1.35e}
\]
where \(a\) is real symmetric positive definite, all coefficients
are analytic, and \(b,c\) may be complex. Shrink \(R\le1\) so that
the ellipticity constant is uniform and \(a(x)\) differs as little
as needed from \(a(0)\). All constants in this section are fixed
by this ball and its coefficients, and do not depend on a
derivative order.

For \(u\in C_c^\infty(B_R)\), Fourier transformation on
\(\mathbb R^m\) gives
\[
 \|D^2u\|_2\le C\|a(0):D^2u\|_2,\qquad
 \|Du\|_2\le \varepsilon\|D^2u\|_2+C_\varepsilon\|u\|_2 .
 \tag{1.35f}
\]
For example, the first inequality is the pointwise symbol bound
\(\sum_{i,j}|\xi_i\xi_j|^2\le C|\xi^ta(0)\xi|^2\);
the second follows from
\(|\xi|^2\le \varepsilon^2|\xi|^4+C_\varepsilon^2\).
The normalization of the Fourier transform cancels on the two
sides. To justify its \(L^2\) identity directly, insert
\(e^{-\epsilon|\xi|^2}\) in the inverse-transform double integral.
The scalar Gaussian integral turns that integral into convolution
with an approximate identity. Letting \(\epsilon\) tend to zero
gives the identity first for compact smooth functions, then for
their differentiated functions. No distributional regularity
theorem is being used in (1.35f).

Write \(a(0):D^2u=Pu-(a-a(0)):D^2u-b\cdot Du-cu\).
Smallness of \(a-a(0)\), followed by (1.35f) with a sufficiently
small \(\varepsilon\), absorbs the second- and first-derivative
terms. Hence
\[
 \|D^2u\|_2\le C\big(\|Pu\|_2+\|u\|_2\big).
 \tag{1.35g}
\]
For a smooth \(v\) and concentric balls \(B_r\subset B_s\subset B_R\),
put \(\delta=s-r\). Cutoffs with derivative bounds
\(|D^j\zeta|\le C_j\delta^{-j}\), \(j=1,2\), exist by rescaling one
fixed smooth radial cutoff. Apply (1.35g) to a cutoff times \(v\)
which equals \(v\) on \(B_r\) and is supported before the midpoint
between \(r\) and \(s\). The product rule yields
\[
 \|D^2v\|_{2,B_r}
 \le C\big(\|Pv\|_{2,B_s}
            +\delta^{-1}\|Dv\|_{2,B_{(r+s)/2}}
            +\delta^{-2}\|v\|_{2,B_s}\big).
 \tag{1.35h}
\]

The gradient term is controlled by a separate cutoff \(\zeta\)
which is one on \(B_{(r+s)/2}\) and supported in \(B_s\).
Integrate the real part of \(-Pv\,\zeta^2\bar v\).
Integration by parts puts the principal term in the form
\(\int\zeta^2a_{ij}\partial_i v\,\overline{\partial_jv}\).
Terms differentiating \(a\) or \(\zeta\), and the lower terms,
are bounded by Cauchy's inequality by half that positive principal
term plus \(C\delta^{-2}\|v\|_2^2\).
The remaining undifferentiated expression is bounded by
\(\|Pv\|_2\|v\|_2\). Thus
\[
 \|Dv\|_{2,B_{(r+s)/2}}
 \le C\big((\|Pv\|_{2,B_s}\|v\|_{2,B_s})^{1/2}
                                      +\delta^{-1}\|v\|_{2,B_s}\big).
 \tag{1.35i}
\]
Insert this into (1.35h) and use
\(\delta^{-1}(ab)^{1/2}\le \tfrac12a+\tfrac12\delta^{-2}b\).
We obtain the fixed-order interior estimate
\[
 \boxed{\quad
 \|D^2v\|_{2,B_r}
       \le C_0\big(\|Pv\|_{2,B_s}+\delta^{-2}\|v\|_{2,B_s}\big).
       \quad}
 \tag{1.35j}
\]
It applies to every differentiated smooth \(v\) with the same
constant \(C_0\).

#### Step 3: Factorial derivative bounds

Analyticity of the coefficients on a slightly larger ball gives
fixed constants \(A_0,A\) such that
\[
 \sup_{B_R}|D^\beta a_{ij}|,\;
 \sup_{B_R}|D^\beta b_i|,\;
 \sup_{B_R}|D^\beta c|
                       \le A_0A^{|\beta|}|\beta|!.
 \tag{1.35k}
\]
Here is a direct power-series check. On a polydisc of radius
\(r\), write a coefficient as \(\sum_\alpha c_\alpha
(x-x_0)^\alpha\) with \(\sum_\alpha|c_\alpha|r^{|\alpha|}\le M_0\).
On the half polydisc its \(\beta\)-th derivative is bounded by
\[
 M_0r^{-|\beta|}\beta!\,
       \sum_{\gamma\ge0}\binom{\gamma+\beta}{\beta}2^{-|\gamma|}
       =M_0r^{-|\beta|}\beta!\,2^{|\beta|+m}.
\]
The identity on the right is the product of the differentiated
geometric-series identities in each coordinate.
Termwise differentiation is justified by these absolutely
convergent majorants. A finite cover of the closed smaller ball
makes the constants uniform. Since \(\beta!\le|\beta|!\), this
proves (1.35k) directly from convergent real power series.

Suppose \(Pf=0\) and \(f\) is smooth. Let
\[
 M=\max\big(1,\|f\|_{H^1(B_R)}\big).
 \tag{1.35l}
\]
For a fixed integer \(N\ge2\), put
\[
 r_j=R-\frac{jR}{2N},\qquad 0\le j\le N .
 \tag{1.35m}
\]
For a derivative order \(j\), use the maximum \(L^2\) norm of its
ordered coordinate derivatives; including all \(m^j\) ordered
derivatives separately is unnecessary.
We show, with a fixed sufficiently large \(B\),
\[
 \max_{|\alpha|=j}\|D^\alpha f\|_{2,B_{r_j}}
                          \le M(BN)^j,\qquad 0\le j\le N.
 \tag{1.35n}
\]
The cases \(j=0,1\) follow from (1.35l), after taking \(B\ge1\).
For \(j\ge2\), apply (1.35j) to an ordered derivative of length
\(j-2\), using \(B_{r_j}\subset B_{r_{j-1}}\).
Commuting that derivative past \(P\), the \(k\) derivatives which
fall on a coefficient leave a derivative of \(f\) of order at
most \(j-k\), with \(k\ge1\).
Their Leibniz coefficients are bounded by
\(\binom{j-2}{k}k!\le N^k\).
The fixed sums over \(i,j\) and the choices of differentiated
coordinates are absorbed by enlarging \(A_0,A\).
Since \(r_{j-k}\ge r_{j-1}\), the already established bounds
(1.35n) control all these derivatives on \(B_{r_{j-1}}\).
Derivatives of \(f\) of smaller order also obey the same upper
bound, since \(BN\ge1\).
The resulting induction inequality is
\[
 \max_{|\alpha|=j}\|D^\alpha f\|_{2,B_{r_j}}
 \le C_0A_0M\sum_{k=1}^{j-2}(AN)^k(BN)^{j-k}
          +\frac{4C_0N^2}{R^2}\,M(BN)^{j-2}.
 \tag{1.35o}
\]
For \(j=2\) the sum is empty, since \(Pf=0\).
Choose \(B>A\) so large that
\[
 C_0A_0\frac{A/B}{1-A/B}+\frac{4C_0}{B^2R^2}\le1.
 \tag{1.35p}
\]
Dividing (1.35o) by \(M(BN)^j\) proves (1.35n).
This is a direct factorial estimate, rather than a repeated
second-order estimate with uncontrolled constants.

Set \(j=N\). The elementary integral comparison
\(\sum_{\ell=1}^N\log\ell\ge\int_1^N\log x\,dx
                              \ge N\log N-N\)
implies \(N^N\le e^NN!\). Therefore
\[
 \max_{|\alpha|=N}\|D^\alpha f\|_{2,B_{R/2}}
                            \le M(Be)^N N!.
 \tag{1.35q}
\]
The first two orders are covered by increasing the constant.

To pass to supremum norms, fix an integer \(q>m/2\).
For a compact smooth function \(u\), Fourier inversion and
Cauchy--Schwarz give
\[
 \|u\|_\infty\le C_q\sum_{|\gamma|\le q}\|D^\gamma u\|_2:
 \tag{1.35r}
\]
the squared weight \((1+|\xi|^2)^{-q}\) is integrable. Gaussian
regularization justifies inversion as in the proof of (1.35f).
Apply this to a *fixed* cutoff times \(D^\alpha f\), equal to that
derivative on \(B_{R/4}\), supported in \(B_{R/2}\).
Only \(q\) additional derivatives and fixed cutoff constants occur.
By (1.35q), their factorials are at most
\((N+q)!\le N!(N+q)^q q!\).
The fixed-degree polynomial in \(N\) is bounded by a fixed
constant times \(2^N\). Consequently there is \(C_1\) with
\[
 \max_{|\alpha|=N}\sup_{B_{R/4}}|D^\alpha f|
                                  \le M C_1^{N+1}N!.
 \tag{1.35s}
\]
Taylor's formula on a short coordinate segment now has remainder
bounded by \(M C_1^{N+2}\|h\|_1^{N+1}\).
It tends to zero if \(C_1\|h\|_1<1\) and the segment stays in the
ball. The Taylor series therefore represents \(f\) there.
This proves real analyticity of every smooth solution of (1.35e)
with positive principal symbol and analytic coefficients.

Apply this proved result to (1.35d). Each of the finitely many
compact-Casimir components of a coefficient is analytic.
Their finite sum is analytic, proving the first assertion of Theorem 1.29
in both fields and every rank.

#### Step 4: The coefficient comparison

Suppose two actual realizations have identified core actions,
compact actions and invariant core pairings. Every derivative
at identity of the difference of corresponding core coefficients
vanishes:
\[
 R_{X_1}\cdots R_{X_r}f(e)
                 =B_E(X_1\cdots X_rv,\widetilde v).
 \tag{1.35t}
\]
The order convention in the product is fixed by successive right
differentiation; either convention gives the same matched jets.
At identity, the \(R_X\)'s form a coordinate tangent basis.
Induction on derivative order expresses coordinate derivatives
through these products and lower-order products, so all coordinate
Taylor coefficients agree.
Theorem 1.29 gives equality on a neighborhood of identity.

An analytic function vanishing on a neighborhood vanishes on a
connected component: along any path, finitely many overlapping
analytic coordinate balls propagate the zero Taylor series.
The connected component of \(GL_n(\mathbb C)\) is the whole group;
one can connect a matrix to its positive diagonal singular-value
part through \(U(n)\), and then deform the positive values to one.
For \(GL_n(\mathbb R)\) the positive-determinant component is
connected by the same singular-value argument and connectedness
of \(SO(n)\). Plane rotations connect \(SO(n)\) to identity, and
diagonal phases connect \(U(n)\) to identity after unitary
diagonalization, so these connectivity facts need no classification.
The other real component is the first multiplied by
\(\operatorname{diag}(-1,1,\ldots,1)\in K\).
Applying the matched compact action to a core vector gives the
coefficient equality there as well. This proves the second assertion.

#### Scope for the principal-series comparison

**Corollary 1.29a (uniform weak analyticity for a core vector).**
This corollary only needs an actual complete smooth realization
of an irreducible admissible core; a supplied dual is unnecessary.
For a fixed core vector \(v\), the conclusion that
\(g\mapsto\lambda(\pi(g)v)\) is analytic holds for *every*
continuous linear functional \(\lambda\) on the supplied model,
not only the paired core functionals. On each fixed coordinate
ball, its factorial derivative constant is uniform over
\(\lambda\)'s bounded by a fixed continuous seminorm.
In particular \(v\) has a convergent vector Taylor expansion on
a neighborhood whose radius is independent of that seminorm.

Indeed the scalar equation (1.35d) used only the actions of the
Casimirs on \(v\), so it holds with an arbitrary \(\lambda\).
For the functionals satisfying \(|\lambda(w)|\le p(w)\), compact
joint continuity bounds the \(H^1\) quantity in (1.35l) by one
finite \(M_p\), using finitely many \(p(\pi(g)Dv)\) on the compact
coordinate ball. All constants in (1.35j)--(1.35s) depend on the
operator and the coordinate ball, and not on \(\lambda,p\).
Thus (1.35s) is uniform with \(M=M_p\).
Continuous functionals bounded by \(p\) recover the quotient
seminorm \(p\); this follows from the elementary linear-functional
extension described in the common-refinement proof below.
The vector Taylor partial sums are therefore Cauchy in every
seminorm on one fixed smaller ball. Completeness supplies their
limit in \(E\). Applying every continuous functional, and using
the scalar Taylor identity, identifies that limit with the actual
orbit vector. A finite decomposition into compact-Casimir
eigenvectors gives the assertion for a general fixed core vector.

Theorem 1.29 proves analytic identity of intrinsic core coefficients
between any two *supplied* actual smooth paired models.
It applies in particular to the explicit principal-series
subquotient models constructed in Theorem 1.26a and to a prescribed cusp
model with the same core. It does not prove that the identity on
cores extends continuously in either direction, that a selected
Borel eigenfunctional is continuous, or that a dense principal
map has closed or surjective range in a prescribed topology.
Those assertions require an additional estimate or a proved
universal property. No analytic-elliptic, subrepresentation or
globalization theorem has been invoked without a written proof.

### A complete common refinement of prescribed smooth realizations

Suppose two actual complete Hausdorff locally convex smooth
moderate-growth \(G=GL_n(F)\) representations \(E_1,E_2\),
\(F=\mathbb R\) or \(\mathbb C\), have identified irreducible
admissible \((\mathfrak g,K)\)-cores \(V_0\). Denote the core
identification by \(J_0\). No continuity of \(J_0\) is assumed.

**Theorem 1.30.** In \(E_1\times E_2\), the closed graph
\[
 R=\overline{\{(v,J_0v):v\in V_0\}}
 \tag{1.36a}
\]
is a complete smooth moderate \(G\)-representation. Its exact
compact-finite core is the graph of \(J_0\).
Both projections
\[
 p_i:R\longrightarrow E_i
 \tag{1.36b}
\]
are continuous injective \(G\)-maps with dense images containing
the entire respective core. If matching supplied dual-pair
realizations are given, the same construction on their dual cores
gives a complete nondegenerate invariant dual pair for \(R\).
This theorem does not claim that a projection is onto, has closed
image, or has a continuous inverse on its image.

#### Step 1: Separation by a continuous functional

We recall the elementary locally convex separation needed below,
including the extension step. If \(L\) is a closed subspace of a
Hausdorff locally convex space \(X\) and \(x\notin L\), there is a
continuous seminorm \(p\) and \(\epsilon>0\) for which
\(p(x-\ell)\ge\epsilon\) for all \(\ell\in L\):
choose a convex balanced neighborhood of zero disjoint from
\(x-L\), and take a smaller finite intersection of seminorm balls.
The maximum of their normalized seminorms is such a \(p\).
On \(L+\mathbb Cx\), define
\(\lambda(\ell+zx)=z\epsilon\). Then
\(|\lambda(\ell+zx)|\le p(\ell+zx)\), by scaling when \(z\ne0\).

Here is the linear-functional extension principle in this setting.
For a real linear functional \(a\) with \(a\le p\), extension to
one additional real direction \(y\) requires choosing \(a(y)\)
between
\[
 \sup_{u\in D}\big(a(u)-p(u-y)\big)
 \quad\hbox{and}\quad
 \inf_{w\in D}\big(p(w+y)-a(w)\big).
 \tag{1.36c}
\]
The left endpoint is no greater than the right: by subadditivity,
\(a(u)+a(w)=a(u+w)\le p(u+w)
                                    \le p(u-y)+p(w+y)\).
The formulas obtained by dividing the two possible signs of the
new real coefficient verify \(a(u+ty)\le p(u+ty)\).
A maximal compatible extension, obtained from the union on each
chain of extension domains, therefore has the whole real space
as domain; otherwise (1.36c) extends it further.
Since \(p(-z)=p(z)\), it obeys \(|a|\le p\).
For a complex functional, first extend its real part by this
argument and define
\(\Lambda(z)=a(z)-i\,a(iz)\).
It is complex linear. Rotating \(z\) by a phase which makes
\(\Lambda(z)\) positive real shows
\(|\Lambda(z)|\le p(z)\), because \(p\) is balanced.
This proves the required continuous extension and separation.
Applied to a single vector modulo the kernel of a seminorm, the
same argument shows
\[
 p(x)=\sup_{\Lambda:\,|\Lambda|\le p}|\Lambda(x)|.
 \tag{1.36d}
\]
The only set-theoretic extension step is the maximal-chain
principle; no representation-theoretic continuity theorem occurs.

#### Step 2: The graph is group-stable

The core graph is Lie- and compact-stable. Let \(\Lambda\) be a
continuous functional on \(E_1\times E_2\) which annihilates its
closure \(R\). For a core graph vector \(w=(v,J_0v)\), the function
\[
 g\longmapsto\Lambda((\pi_1(g),\pi_2(g))w)
 \tag{1.36e}
\]
is analytic, by Corollary 1.29a applied in each factor.
Every derivative at identity vanishes, since the Lie algebra
preserves the core graph. It is therefore zero on the identity
component by the proved analytic identity principle in Theorem 1.29.
The compact action preserves the core graph and meets the other
real component, so it is zero on all of \(G\).
The separation in Step 1 of this argument implies
\((\pi_1(g),\pi_2(g))w\in R\).
By continuity of the action and density of the core graph in
its closure, this holds for every \(w\in R\).
Thus \(R\) is group-stable.

It is complete because it is closed in the complete product.
Orbit derivatives in the product belong to \(R\), since it is
closed and invariant; restrictions of the continuous
differentiated maps give the actual smooth differentiated action
in the subspace topology. The orbit maps have their full smooth
derivatives there: a remainder tends to zero in the induced
seminorms exactly when it does so in the ambient product.
Joint continuity is inherited.
Every continuous seminorm on \(R\) is bounded by the restriction
of a finite sum of continuous seminorms on the two factors,
by the definition of the subspace topology.
Apply their moderate inequalities, take the larger exponent and
sum the controlling seminorms. This proves moderate growth on \(R\)
without an open-mapping or globalization theorem.

#### Step 3: Exact compact packets and the two projections

For each compact type \(\tau\), its character projector is a
continuous operator on the product and on \(R\).
The projection of the core graph is exactly the finite graph
packet
\[
 R_\tau=\{(v,J_0v):v\in(V_0)_\tau\}.
 \tag{1.36f}
\]
A finite-dimensional subspace in a Hausdorff locally convex space
is closed: select continuous functionals separating a basis,
use their finite invertible coordinate matrix, and reduce closure
to closure in a finite Euclidean space.
Projecting the approximating core graph vectors thus shows that
the entire \(\tau\)-packet of \(R\) is (1.36f).
Every compact-finite vector lies in finitely many such packets,
so the exact core of \(R\) is the core graph.

If the kernel of \(p_i\) were nonzero, it would be a nonzero
closed compact-stable subspace of \(R\).
The polynomial compact approximate identities (1.34d) preserve it,
converge to identity on it, and have compact-finite values.
Some approximant of a nonzero vector would therefore be a
nonzero core vector in that kernel. This is impossible on the
core graph. Both projections are consequently injective.
They are continuous equivariant maps by construction and
contain the respective cores in their images.
Core density (1.34d) makes both images dense.

This identifies an actual complete common refinement of the
prescribed topologies and constructs both continuous comparison
maps. It does not promote dense images to onto or closed images.
A complete space can map continuously and injectively onto a
proper dense subspace of another complete space; completeness
alone supplies no missing inverse estimate.

#### Step 4: The paired version

Apply the same construction to the prescribed admissible dual
cores and actual dual models, obtaining \(\widetilde R\).
Restrict the first given pairing to
\[
 B_R(r,\widetilde r)
       =B_1(p_1r,\widetilde p_1\widetilde r).
 \tag{1.36g}
\]
It is jointly continuous and invariant.
It equals the second restricted pairing: both agree on the core
graphs by the specified core pairing, and each core graph is
dense in its complete refinement. First fix a dual core vector
and extend in \(r\); then fix \(r\) and extend in
\(\widetilde r\). Separate continuity suffices for this equality.
If \(B_R(r,\widetilde R)=0\), density of
\(\widetilde p_1(\widetilde R)\) and nondegeneracy of \(B_1\)
give \(p_1r=0\). Injectivity then gives \(r=0\).
The other radical is zero in the same way.
Thus \((R,\widetilde R,B_R)\) is an actual compatible complete
smooth moderate dual pair with the identified core and dual core.

#### Remaining comparison obligation

Apply Theorem 1.30 to a prescribed cusp model and the explicit complete
principal-series subquotient model of Theorem 1.26a, once their cores are
identified using Theorem 1.28. It gives actual injective dense continuous
maps from their complete common refinement to each model.
To identify the prescribed model itself with that subquotient,
one still needs an inverse seminorm estimate or surjectivity of
these comparison maps. The existence of a full principal-core
quotient in 1.34y does not establish that estimate.
Theorems 1.32–1.34 below prove occurrence and construct a compatible
actual realization for every abstract irreducible admissible core. No assertion here
identifies the residual correction polynomial with the intended
standard real/complex gamma factors.

### The canonical Gaussian package in every prescribed actual dual-pair model

Use \(F=\mathbb R\) or \(\mathbb C\), the positive trace Fourier
argument, the basic programme characters
\(\psi_{\mathbb R}(x)=e^{-2\pi ix}\) and
\(\psi_{\mathbb C}(z)=e^{-2\pi i(z+\bar z)}\), and their self-dual
measures. Let \((E,\widetilde E,B_E)\) satisfy the actual complete
smooth moderate dual-pair hypotheses of Theorem 1.28, with irreducible
admissible core \(V_0\).
Let \(\mathcal S_0\) denote the polynomial multiples of
\(G_{\mathbb R}(X)=e^{-\pi\operatorname{tr}(XX^t)}\), or of
\(G_{\mathbb C}(X)=e^{-2\pi\operatorname{tr}(XX^*)}\).
Write \(\nu(g)=|\det g|_F\) and
\[
 Z_E(s,\Phi;v,\widetilde v)=
       \int_G\Phi(g)B_E(\pi(g)v,\widetilde v)
                       \nu(g)^{s+(n-1)/2}\,dg.
 \tag{1.37a}
\]
Its initial convergence and continuation in the prescribed
topologies follow from the written continuation proof of Theorem 1.21,
with the locally convex extension supplied in Step 3 below.

**Theorem 1.31.** In every such prescribed model, in every rank and
both fields, the Gaussian coefficient span is exactly
\[
 \operatorname{span}_{\mathbb C}
 \{Z_E(s,\Phi;v,\widetilde v):
      \Phi\in\mathcal S_0,\ v\in V_0,\
                    \widetilde v\in\widetilde V_0\}
                    =L_E(s)\mathbb C[s].
 \tag{1.37b}
\]
One can choose full Borel inducing characters by Theorem 1.28 and a
nonzero monic polynomial \(P\) for which
\[
 L_E(s)=P(s)L_{\boldsymbol\chi}(s),\qquad
 L_{\boldsymbol\chi}(s)=
 \begin{cases}
 \prod_i\Gamma_{\mathbb R}(s+t_i+e_i),&F=\mathbb R,\\
 \prod_i\Gamma_{\mathbb C}(s+t_i+|\ell_i|/2),&F=\mathbb C.
 \end{cases}
 \tag{1.37c}
\]
There is an actual finite attaining family
\[
 \sum_{\alpha=1}^r
       Z_E(s,\Phi_\alpha;v_\alpha,\widetilde v_\alpha)=L_E(s).
 \tag{1.37d}
\]
For every Schwartz test and every pair of smooth vectors,
\(Z_E/L_E\) is entire with compact-parameter joint test/vector
seminorm bounds. The generator has no zeros.
For its compatible paired dual normalization,
\[
 P_{\widetilde E}(1-s)=(-1)^bP(s),\qquad b=\deg P,
 \quad
 \epsilon_E=(-1)^b
 \begin{cases}
 (-i)^{\sum e_i},&F=\mathbb R,\\
 (-i)^{\sum|\ell_i|},&F=\mathbb C,
 \end{cases}
 \tag{1.37e}
\]
and the full scalar Fourier equation is
\[
 Z_{\widetilde E}(1-s,\widehat\Phi;\widetilde v,v)
 =\epsilon_E
       \frac{L_{\widetilde E}(1-s)}{L_E(s)}
                          Z_E(s,\Phi;v,\widetilde v).
 \tag{1.37f}
\]
Conjugation, and compatible unitary duality, have the exact
normalizations proved in Theorem 1.26b. The polynomial in (1.37c) is the
integral-defined correction. This theorem does not yet compute
its roots and scalar from every intended real discrete-series,
parity or complex angular standard-factor label.

#### Step 1: Occurrence is now proved in the required actual scope

Theorem 1.28 constructs an actual algebraic injection
\(T_0:V_0\hookrightarrow I_0(\boldsymbol\chi)\).
It does so from finite \(U(\mathfrak n)\)-generation Theorem 1.27, the
nonzero Jacquet proof in Steps 1–4 of Theorem 1.28 and the explicit compact map 1.34w.
No source statement supplies an unproved occurrence premise.

Apply the written closure theorem Theorem 1.26a with
\(W_0=0\) and the submodule \(T_0V_0\) in that principal core.
It constructs the complete smooth moderate principal submodel
\(Q=\overline{T_0V_0}\) and its actual paired dual
\[
 Q^\vee=I(\boldsymbol\chi^{-1})/
                             \operatorname{Ann}(Q).
 \tag{1.37g}
\]
Their exact cores and compact pairing identify with
\(V_0,\widetilde V_0,B_E|_{V_0\times\widetilde V_0}\).
The finite-packet transpose in 1.34y supplies this dual core
identification; the smooth paired construction is Theorem 1.26a.
These are actual constructed models. No continuous map between
the entire original \(E\) and \(Q\) is being assumed.

#### Step 2: Core coefficients identify the ideals and the attaining family

Theorem 1.29 proves
\[
 B_E(\pi(g)v,\widetilde v)
       =B_Q(\pi_Q(g)T_0v,\widetilde T_0\widetilde v)
                    \qquad(g\in G)
 \tag{1.37h}
\]
for every pair of core vectors, where \(\widetilde T_0\) denotes
the exact dual core identification in (1.37g).
Both actual realizations have the same core Lie/compact actions
and pairing, so their analytic coefficient jets agree at identity
and propagate over the whole group. This is the proved Theorem 1.29
comparison, rather than an asserted uniqueness of globalizations.

Consequently the original integrals for these coefficients are
identical on an initial convergence half-plane and their
meromorphic continuations are identical.
The exact Gaussian ideal theorem Theorem 1.26b for \(Q\) proves (1.37b)--(1.37c)
for \(E\). Its finite attaining tests and core vectors, pulled
back through the two algebraic core identifications, prove (1.37d)
in the original model.
Every polynomial multiplier used in constructing the attaining
family has already been absorbed into a polynomial-Gaussian
test by the Euler operator in Theorem 1.26b. Thus (1.37d) is an actual
finite family of allowed integrals, not a formal polynomial gcd.
This proves the genuine Gaussian-ideal premise in the prescribed
model; a common gamma majorant was not substituted for it.

#### Step 3: Full Schwartz division and its continuity

Theorem 1.21 was stated for complete Fréchet models.
Here is the precise extension of its argument to the complete
locally convex models allowed in Theorem 1.28. Its central determinant
operator proof in the preceding dense-core and central-determinant
subsections is algebraic after density of the core.
Replace its countable compact-density argument by (1.34d);
continuity of differentiation then extends the same scalar
central identities to the whole supplied model.
Its far-right integral bound and scalar integration by parts,
in the preceding bounds and integration-by-parts subsection, use
joint pairing seminorms, moderate growth and finitely
many derivative seminorms, and no countable topology assumption.
Thus the same proved differential recurrence holds:
\[
 B_E(s)Z_E(s,\Phi)=Z_E(s+a,\mathscr D\Phi),\qquad
       \deg B_E=2n,\quad B_E\text{ monic},
 \tag{1.37ha}
\]
where \(a=2,\mathscr D=D^2\) over \(\mathbb R\) and
\(a=1,\mathscr D=D_+D_-\) over \(\mathbb C\).
Every coordinate coefficient derivative in its integration-by-parts
proof is bounded by a finite negative determinant power and a
finite list of continuous seminorms. Taking the real part of \(s\)
large makes its extension across the singular set \(C^{2n}\).
This is exactly the scalar line-by-line extension verified there;
it uses no vector-valued integration across that set.

If \(B_E(s)=\prod_j(s-\beta_j)\), put
\(H_E(s)=\prod_j\Gamma((s-\beta_j)/a)\). The proved scalar gamma
recurrence gives
\(H_E(s+a)=a^{-2n}B_E(s)H_E(s)\).
For a compact parameter set choose \(N\) so that its translate
by \(Na\) lies beyond the integral convergence threshold.
Define
\[
 F_E(s,\Phi;v,\widetilde v)
       =a^{-2nN}
          \frac{Z_E(s+Na,\mathscr D^N\Phi;v,\widetilde v)}
                        {H_E(s+Na)} .
 \tag{1.37hb}
\]
The recurrence shows independence of larger \(N\). These formulas
patch to an entire family with the far-right joint seminorm
bounds, since \(\mathscr D^N\) is a continuous Schwartz operator
and the scalar reciprocal gamma product is entire and bounded
on the shifted compact set. This writes the extension required
for the broader topology, rather than silently importing the
Fréchet theorem with enlarged hypotheses.
In the Fréchet scope it is Theorem 1.21. In either scope it gives the entire continuous family
\[
 F_E(s,\Phi;v,\widetilde v)=Z_E(s,\Phi;v,\widetilde v)/H_E(s),
 \tag{1.37i}
\]
with joint test/vector seminorm bounds on every compact
parameter set. Its proof uses the written central differential
identity and a smooth-model coefficient bound. It does not
require a principal-series topological comparison.
The finite identity (1.37d) shows that
\[
 h_E(s)=L_E(s)/H_E(s)
 \tag{1.37j}
\]
is an entire nonzero function.
For a polynomial-Gaussian core integral, (1.37b) says
\(F_E=h_E p\) with \(p\in\mathbb C[s]\).

The core is dense in each prescribed topology by (1.34d).
Polynomial-Gaussian tests are dense in the full Schwartz space:
the actual earlier programme proof is
*Hermite functions, tempered distributions and the Schwartz kernel theorem*, Lemma 3.1 and Theorem 3.2.
Its Hermite truncations converge in every Schwartz seminorm;
a scalar dilation changes its fixed Gaussian to \(G_F\).
Over \(\mathbb C\), polynomials in \(Z,\bar Z\) are the full real
coordinate polynomial algebra, so no complex-angular tests are
discarded.

Approximate a given \(\Phi,v,\widetilde v\) in these topologies.
In a general locally convex topology this may be a net;
the joint bounds in (1.37i) imply uniform convergence on every
compact parameter set, regardless. At a zero of \(h_E\) of
order \(m\), the first \(m\) jets of every approximating function
vanish. Cauchy's formula on a fixed small circle gives convergence
of the jets and hence their vanishing in the limit.
Thus \(F_E/h_E=Z_E/L_E\) is entire.

The same circle proves a joint seminorm bound for the division:
inside it the quotient is its Cauchy integral, with denominator
\(h_E\) nonzero on the circle. Bound its numerator by (1.37i).
Away from these isolated zeros divide directly. Finitely many
circles and neighborhoods cover a compact parameter set.
This gives full continuity with the original prescribed vector
seminorms, rather than seminorms of an unproved equivalent model.
The absence of zeros of \(L_E\) follows from Theorem 1.26b or independently
by the compact-support test in the proof of Proposition 1.21b: at a
prescribed \(s_0\), use a bump times the conjugate of a nonzero
coefficient and the inverse imaginary norm phase.
Its integral is strictly positive. An entire division by a
zero of \(L_E\) would force it to vanish. This proves that no
correction root can create an excess zero.

#### Step 4: The Fourier equation on every test and smooth coefficient

Theorem 1.26b proves (1.37e)--(1.37f) on \(Q,Q^\vee\). For core coefficients,
(1.37h) transfers it to \(E,\widetilde E\).
First take polynomial-Gaussian tests. Their Fourier transforms
remain polynomial-Gaussian: differentiating the exact scalar
Gaussian transform gives the transformed polynomial, and the
Gaussian is self-dual with the specified real/complex measures.
These facts are proved in *Additive characters, self-dual measures and Poisson summation on the adèles*, Proposition 5.2 and Lemma 5.4A.

Approximate arbitrary Schwartz tests and both smooth vectors
as in Step 3 of this argument. Fourier transformation is continuous on the
whole Schwartz space by that same written Lemma5.4A.
For both the representation and its dual, divide first by the
entire-continuation majorants in (1.37i). At parameter points
avoiding the discrete poles of the fixed scalar gamma ratio,
joint compact convergence passes the Fourier identity to the
limit. The identity of meromorphic continuations gives it
everywhere. This proves (1.37f) for all smooth coefficients
without any continuous lifting of them to the principal model.
It also identifies the already proved general scalar in
Theorem B.5 / lesson04 Theorem1.22 with (1.37e)--(1.37f).

#### Step 5: Duality, conjugation and the unitary phase

The paired principal model for \(Q^\vee\) uses the inverse
inducing characters. Theorem 1.26b proves its exact polynomial reflection
\(P_{Q^\vee}(1-s)=(-1)^bP_Q(s)\) and the sign
\(\epsilon_Q=(-1)^b\epsilon_{\boldsymbol\chi}\).
Equation (1.37h), applied also to the swapped actual dual pair,
transfers those identities to the prescribed dual normalization.
Under conjugation, real parity remains \(e_i\), complex angular
weight becomes \(-\ell_i\), and \(t_i\) becomes \(\bar t_i\).
Its product gamma factor is the complex conjugate at \(\bar s\).
The monic-polynomial normalization in Theorem 1.26b then gives exactly
\[
 L_{\bar E}(s)=\overline{L_E(\bar s)}.
 \tag{1.37k}
\]
If the supplied core pairing comes from an invariant positive
Hermitian form, core conjugation identifies its conjugate with
the admissible dual. The Theorem 1.26b core-unitary argument proves, with
no unidentified scalar in this paired normalization,
\[
 L_{\widetilde E}(s)=\overline{L_E(\bar s)}.
 \tag{1.37l}
\]
In particular the basic scalar in (1.37e) has absolute value one.
Changing the basic character to \(\psi_a(x)=\psi(ax)\) gives
the exact factor
\[
 \epsilon_E(s,\psi_a)=
        \omega_E(a)|a|_F^{n(s-1/2)}\epsilon_E(s,\psi).
 \tag{1.37m}
\]
To check it directly, the self-dual additive matrix measure changes
by \(|a|_F^{n^2/2}\), Fourier substitution is \(Y\mapsto aY\),
and changing \(g\mapsto a^{-1}g\) in the dual zeta integral
contributes the determinant power
\(|a|_F^{-n(1-s+(n-1)/2)}\) and the dual central coefficient
\(\omega_E(a)\). The net exponent is \(n(s-1/2)\).
For unitary \(\omega_E\), its modulus is one on the critical line.

#### Exact scope and the remaining target

Theorem 1.31 proves a genuine Gaussian ideal, finite attainment, full
Schwartz division with continuity, full scalar Fourier equation
and paired dual/conjugation normalization in **every prescribed
actual complete smooth moderate dual-pair realization** of an
irreducible admissible real/complex \(GL_n\) core.
Theorem 1.19 supplies those models in the full automorphic cusp
scope, so this removes the abstract occurrence/comparison
premise from the Gaussian-ideal existence argument in that
scope. Theorem 1.30 gives further actual continuous dense comparison maps,
but a topological isomorphism with the original model is not
needed for the coefficient-and-density proof above.

Theorems 1.32–1.34 below prove nonzero Jacquet quotient and construct
a compatible realization for every abstract irreducible admissible
core. Full continuous inverse/closed-image comparison
for arbitrary prescribed topologies also remains unproved.
Finally, (1.37c) is monic relative to the inducing product chosen
by Theorem 1.28. Computing \(P\) and the resulting scalar from all
intended standard-factor labels, including real discrete-series
blocks and complex angular data, remains a precise mathematical
obligation. The free classification statements in Goldfeld–Jacquet do not supply that proof.

### Analytic coefficient germs of an arbitrary admissible general linear core

Let \(F=\mathbb R\) or \(\mathbb C\), \(G=GL_n(F)\), and
\(K=O(n)\) or \(U(n)\). Complexify the real Lie algebra of \(G\).
Let \(V\) be an arbitrary irreducible admissible
\((\mathfrak g,K)\)-module. No actual noncompact action or topology
on \(V\) is assumed. Its algebraic admissible contragredient \(V^\vee\)
is the direct sum of the duals of its finite compact packets, with
the usual contragredient compact and Lie actions. Write
\[
 B(v,w)=w(v),\qquad
 B(Xv,w)=-B(v,Xw).
 \tag{1.38a}
\]
The second action preserves compact-finiteness. Indeed a functional
supported in a finite set of compact types can, after a Lie
generator is applied, meet only types in their tensor products with
the finite compact representation \(\mathfrak g^*\). Those tensor
products are finite-dimensional and have finite irreducible
decompositions. Each compact packet remains finite-dimensional.
The contragredient is irreducible: a nonzero proper submodule has a
proper part in some finite dual packet, whose finite-dimensional
annihilator gives a nonzero submodule of \(V\); irreducibility and
the perfect packet pairing contradict its being proper.

Theorem 1.27 above applies to both cores. In particular they are generated
over \(U(\mathfrak g)\) by finite compact-stable spaces, and the
selected invariant central trace operators act by scalars. These
are written algebraic proofs, not assumptions about classification
or globalization.

**Theorem 1.32.** For every \(v\in V,\;w\in V^\vee\) there is a unique
real analytic germ \(c_{v,w}\) on a neighborhood of \(K\) with the
compact covariance in (1.38c) and the identity jets
\[
 (R_Dc_{v,w})(1)=B(Dv,w),\qquad D\in U(\mathfrak g).
 \tag{1.38b}
\]
The germs are bilinear, compact-finite under left and right
translations, and satisfy wherever both sides are defined
\[
 R_Xc_{v,w}=c_{Xv,w},\qquad
 L_Xc_{v,w}=-c_{v,Xw},\qquad
 c_{v,w}(k_1gk_2)=c_{k_2v,k_1^{-1}w}(g).
 \tag{1.38c}
\]
Here \(R_Xf(g)=\frac d{dt}f(g\exp(tX))|_{0}\) and
\(L_Xf(g)=\frac d{dt}f(\exp(tX)g)|_{0}\).
The neighborhood may depend on the finite compact orbits of
\(v,w\). This theorem asserts germs of scalar functions; it does
not assume or construct a noncompact action on an abstract vector.

#### Step 1: The formal germ and its identities

We first justify the enveloping-algebra jet dictionary needed here,
rather than importing an analytic-vector theorem. Choose a real
matrix Lie basis \(X_1,\ldots,X_d\) and local analytic coordinates
at identity. Their invariant vector fields have independent
values there. Commuting an out-of-order pair of invariant fields
introduces a single commutator and lowers total order. Therefore
ordered monomials span the enveloping algebra. They are also
independent as differential operators: the highest-order symbol
at identity of the monomial of multi-index \(\alpha\) is the
distinct commutative monomial in the basis of cotangent variables
dual to \(X_i\). A relation of highest total order \(m\) has zero
degree-\(m\) symbol only when every coefficient of that order is
zero; induction removes all orders. This proves the required
ordered-monomial independence directly in the actual matrix group.

Consequently the evaluations at identity of invariant monomials
of order at most \(m\) are a triangular invertible linear change
from ordinary coordinate derivatives of order at most \(m\).
The leading diagonal blocks are the change of symmetric basis
just described. Specifying a linear functional on \(U(\mathfrak g)\)
therefore specifies a unique compatible formal Taylor germ, and
every formal germ specifies that functional.
Apply this to \(D\mapsto B(Dv,w)\).
Right differentiation gives the first identity of (1.38c).
Left fields commute with right fields; at identity
\[
 (R_D L_Xc)(1)=B(XDv,w)=-B(Dv,Xw),
\]
which proves the second identity on formal jets. Compact changes
of variables give the third identity on jets by compatibility
of the given \(K\)-action with its Lie action. These computations
also give bilinearity and the scalar central equations.

These identities may be pulled back through any actual analytic
matrix-coordinate map. They hold as formal identities there;
after multiplying by the determinants of its differential, they
also hold for rational lifts on a generically invertible
coordinate map. This assertion is elementary: the chain rule for
each finite jet is a polynomial identity in finitely many
derivatives of the coordinate map. Its inverse uses the adjugate
divided by its determinant, so multiplication clears its
denominators. No convergence is used at this stage.

On the diagonal \(a(x)=\operatorname{diag}(e^{x_i})\) the formal
restriction is explicitly
\[
 F_{v,w}(x)=
 \sum_{\alpha\in\mathbb N^n}
       B(H_1^{\alpha_1}\cdots H_n^{\alpha_n}v,w)
       \frac{x^\alpha}{\alpha!},\qquad H_i=E_{ii}.
 \tag{1.38d}
\]
For a fixed pair, take the vector of all its finite left and right
compact translates. It is a formal power series with values in
one finite-dimensional space. All compact derivatives act there
by fixed matrices.

#### Step 2: A pole-order refinement of the written radial system

The radial computation in Theorem 1.28, Step 3, equations (1.34j)–(1.34o), is a
calculation with matrix vector fields. It applies to formal jets
as well as to actual functions by the preceding chain rule.
We need the following refinement at the origin.

Fix a compact set of real diagonal directions \(h\) with all
\(|h_i-h_j|\ge\eta>0\), and bounded \(|h_i|\). Then a coefficient
of a radial derivative of order \(k\) in a central operator of
degree \(r\), restricted to \(x=th\), has pole order at most
\(r-k\) at \(t=0\). After that power of \(t\) is multiplied in,
it is holomorphic in a disk whose radius and bounds are uniform
on this compact set of \(h\).

Here is the additional calculation. At \(a(x)\), an off-diagonal
right field is a sum of left and right compact fields, with
coefficients
\[
 \frac{1}{2\sinh(x_j-x_i)},\quad
 -\frac{1}{e^{2(x_j-x_i)}-1},\quad
 -\frac{e^{2(x_j-x_i)}}{e^{2(x_j-x_i)}-1}.
 \tag{1.38e}
\]
Each has a simple pole along \(x_i=x_j\). Real diagonal fields
are \(\partial_{x_i}\); imaginary diagonal fields for the complex
group are compact fields. At \(k_1a(x)k_2\), first conjugate the
Lie generator by \(k_2\) and use the same formulas. All angular
coefficients and their angular derivatives are analytic and
bounded on the compact factors. Off-diagonal compact coefficients
have one pole, and a radial derivative of any such coefficient
adds at most one pole. An angular derivative adds none.

Induction on the number of fields in a word proves the assertion:
creating a compact differentiation uses one field and at most
one pole; creating a radial differentiation uses one field and
raises \(k\) by one; differentiating an existing coefficient uses
one field and raises its pole order by at most one. Thus the
sum of radial derivative order and pole order is at most the
word length. The finite compact derivatives can then be replaced
by their matrices. Symmetrizing invariant trace words preserves
this bound. Newton's finite polynomial construction and the
product rule preserve it as well.

More precisely, choose the normalizations used in Theorem 1.28:
the real \(C_r\), or \(2^rC_r^{(1)}\) for the complex group.
The factor \(2^r\) compensates exactly for the radial
\(\frac12\partial_{x_i}\) in the first complexified summand.
The resulting elementary-symmetric central equations are
\[
 e_r(\partial_x)F=\mu_rF-\mathcal L_rF,\qquad
 \operatorname{ord}\mathcal L_r\le r-1.
 \tag{1.38f}
\]
A coefficient of a derivative \(\partial^\beta\) on the right
has pole order at most \(r-|\beta|\); the scalar term has order
zero. Every fixed radial derivative of a coefficient adds at
most its own order to this bound.
These statements hold in the localized formal ring obtained by
inverting the nonzero root linear forms \(x_j-x_i\).
They follow from (1.38e), the matrix chain rule and the invariant
trace symbol, not a general radial-part theorem.

Use the constant-coefficient identity
\[
 \partial_{x_i}^{\,n}
  =\sum_{r=1}^n(-1)^{r+1}
      \partial_{x_i}^{\,n-r}e_r(\partial_x).
 \tag{1.38g}
\]
Replacing \(e_r(\partial_x)F\) by (1.38f) expresses its left
side as derivatives of total order at most \(n-1\), with a
coefficient for \(\partial^\beta F\) of pole order at most
\(n-|\beta|\). Differentiate and repeat to reduce every
derivative having an index at least \(n\). Each replacement
lowers total derivative order. The pole bound is preserved
because the loss of derivative order pays for all coefficient
derivatives and all subsequent substitutions.

For
\[
 J_\alpha=\partial_x^\alpha F,\qquad 0\le\alpha_i<n,
\]
this gives
\[
 \partial_{x_i}J_\alpha
       =\sum_\beta (A_i)_{\alpha\beta}(x)J_\beta,
 \qquad
 \operatorname{pole}_{t=0}
       (A_i)_{\alpha\beta}(th)
           \le |\alpha|+1-|\beta|.
 \tag{1.38h}
\]
An entry with a negative upper bound is zero: the reduction
never increases total derivative order. The entries with
\(|\beta|=|\alpha|+1\) are the unreduced constant jet shifts.
The formulas are those of the fixed finite compact array.
Only finitely many differentiations and substitutions are
required, so the holomorphic bounds along \(th\) are uniform
on the fixed compact set of directions.

Set
\[
 Y_\alpha(t)=t^{|\alpha|}J_\alpha(th).
\]
Equation (1.38h) gives a genuine Fuchsian formal system
\[
 tY'(t)=A_h(t)Y(t),
 \tag{1.38i}
\]
where
\[
 (A_h)_{\alpha\beta}
 =|\alpha|\delta_{\alpha\beta}
  +\sum_i h_i\,t^{1+|\alpha|-|\beta|}
                      (A_i)_{\alpha\beta}(th).
\]
Every entry is holomorphic at zero, uniformly for the selected
directions. \(Y\) itself is an ordinary formal power series,
since every \(J_\alpha\) comes from (1.38d).

#### Step 3: Convergence of the formal Fuchsian solution

We prove exactly the elementary ODE fact used here. Suppose
\(A(t)=\sum_{k\ge0}A_kt^k\) is holomorphic on a disk, with
\(\|A_k\|\le C R^{-k}\), and \(Y=\sum_{m\ge0}Y_mt^m\) formally
satisfies \(tY'=AY\). Then
\[
 (mI-A_0)Y_m=\sum_{k=1}^m A_kY_{m-k}.
 \tag{1.38j}
\]
For \(m>2\|A_0\|\), the geometric series gives
\(\|(mI-A_0)^{-1}\|\le2/m\).
Choose an integer \(m_0>2\|A_0\|+4C+1\) and \(S\ge2/R\).
Choose \(M\) so that \(\|Y_m\|\le MS^m\) for \(m\le m_0\).
For larger \(m\), induction and (1.38j) give
\[
 \|Y_m\|
 \le \frac{2C}{m}MS^m
        \sum_{k\ge1}(RS)^{-k}
 \le MS^m.
 \tag{1.38k}
\]
Thus the series converges. Resonant small integers cause no
problem: the finitely many initial coefficients already
satisfy the formal equation. The same choices work uniformly
for a compact family of \(A_h\) whose finite initial coefficients
are bounded.

In (1.38i) the initial coefficients are fixed finite jets from
(1.38d), hence polynomials in \(h\), with bounded compact
matrices on the chosen array. They are uniformly bounded.
In particular
\[
 \left|\frac{B((\sum h_iH_i)^m v,w)}{m!}\right|
          \le M S^m
 \tag{1.38l}
\]
uniformly for separated bounded diagonal \(h\), and for \(v,w\)
in bounded parts of the fixed compact orbit spaces.
The same conclusion holds in rank one directly from its scalar
central equation.

#### Finite-dimensional diagonalization

**Lemma 1.32a.** A real symmetric matrix has an orthonormal real
eigenbasis, and a complex Hermitian matrix has an orthonormal complex
eigenbasis. A commuting family of complex Hermitian matrices has a
common orthonormal eigenbasis. Consequently every unitary matrix,
and every commuting family of unitary matrices, can be diagonalized
by a unitary change of basis.

*Proof.* For a symmetric or Hermitian matrix \(A\), the real function
\(\langle Ax,x\rangle\) attains its maximum on the unit sphere.
Let \(x\) be a maximizing unit vector. For every unit \(y\perp x\),
differentiate this function at
\(x\cos t+y\sin t\) when \(t=0\). The derivative is
\(2\operatorname{Re}\langle Ax,y\rangle\), hence vanishes. Over
\(\mathbb C\) replace \(y\) by \(iy\) as well, so
\(\langle Ax,y\rangle=0\). Therefore \(Ax=\lambda x\), with
\(\lambda=\langle Ax,x\rangle\) real. The orthogonal complement of
\(x\) is invariant, since
\(\langle Az,x\rangle=\langle z,Ax\rangle=0\) for \(z\perp x\).
Induction on dimension supplies the asserted eigenbasis.

For a commuting Hermitian family, every eigenspace of one member is
invariant under all the others. Choose a nonscalar member, decompose
into its mutually orthogonal proper eigenspaces, and apply induction
on their dimensions. If every member is scalar there is nothing to
do. This argument applies to an arbitrary family, since each
nonscalar choice strictly lowers dimension.

For a unitary matrix \(U\), its Hermitian real and imaginary parts
\[
 H=(U+U^*)/2,\qquad J=(U-U^*)/(2i)
 \tag{1.38ak}
\]
commute: use \(U^*=U^{-1}\). A common eigenbasis for \(H,J\)
diagonalizes \(U=H+iJ\). A commuting family of unitary matrices
commutes also with every inverse, so all its Hermitian real and
imaginary parts commute. The same common-eigenbasis argument
diagonalizes the whole family. \(\square\)

This proof also gives the singular-value factorizations used below:
diagonalize the positive definite matrix \(g^*g\), take the positive
square roots of its eigenvalues, and divide the corresponding
columns of \(g\) by those square roots. Their orthonormality follows
by taking inner products. Every positive-definite eigenspace has
positive eigenvalue since
\(\langle g^*gx,x\rangle=\|gx\|^2>0\) for \(x\ne0\).

#### Step 4: From separated diagonal directions to a full local germ

Let \(\mathfrak p_{\mathbb R}\) be the real symmetric or Hermitian
matrices. For each \(m\) the expression
\[
 p_m(P)=B(P^m v,w)/m!
 \tag{1.38m}
\]
is an ordinary homogeneous polynomial of degree \(m\) on this
finite-dimensional real vector space. Choose a small closed cube
\(Q\) about a matrix with simple eigenvalues, so that every
matrix in \(Q\) has eigenvalue gaps at least \(\eta\), with
bounded eigenvalues. Lemma 1.32a gives
\(P=k(\sum h_iH_i)k^{-1}\). All \(k\)-translates of \(v,w\)
stay in the fixed bounded compact orbit spaces, so (1.38l) gives
\(\sup_Q|p_m|\le MS^m\).
No smooth choice of eigenvectors is needed for this bound.

We give the polynomial extrapolation which removes the gap
restriction. After an affine change sending \(Q\) to
\([-1,1]^b\), expand any polynomial \(p\) of total degree at
most \(m\) in products of Chebyshev polynomials
\(T_j(\cos\theta)=\cos(j\theta)\). Orthogonality on the product
of circles bounds each coefficient by \(2^b\sup_Q|p|\).
The triangular leading terms ensure that only multi-indices
of total degree at most \(m\) occur. On any fixed complex
coordinate box, the transformed coordinates have magnitude
at most \(A\); the recurrence
\(T_{j+1}(z)=2zT_j(z)-T_{j-1}(z)\) gives
\(|T_j(z)|\le(2A+1)^j\).
There are at most \((m+1)^b\le2^{bm}\) terms for \(m\ge1\).
Therefore, on that fixed complex box,
\[
 \sup|p_m|\le M_1S_1^m.
 \tag{1.38n}
\]
Because the original \(p_m\) is homogeneous, on a sufficiently
small complex neighborhood of zero the series \(\sum_mp_m(P)\)
converges normally. Cauchy's elementary one-variable integral
estimate applied successively in the coordinates controls all
derivatives on smaller boxes. In this use it follows directly
by integrating a polynomial on a circle: the integral of
\(z^j/z^{k+1}\) is zero unless \(j=k\), when it is \(2\pi i\).
Normal convergence passes this coefficient identity to the
series; a smaller circle gives the geometric bounds for every
fixed differentiated series. The limit is analytic and its
Taylor series is the given formal series.

For \(g\) near \(K\), polar coordinates are analytic:
\[
 P=\tfrac12\log(g^*g),\qquad k=g\exp(-P),\qquad g=k\exp P.
\]
Near \(g^*g=I\), the convergent matrix logarithm series proves
this directly; its adjoint entries are analytic real-coordinate
functions. Compact finite-dimensional representations are
analytic: in coordinates formed by finite products of small
one-parameter exponentials their matrices are the ordinary
finite matrix exponentials, by the finite-dimensional
constant-coefficient differential equation. Both components
of \(O(n)\) are included by its given compact action.
Define
\[
 c_{v,w}(k\exp P)=\sum_{m\ge0}B(P^mv,k^{-1}w)/m!.
 \tag{1.38o}
\]
The bounds above are uniform for the compact translates in
this formula. It is therefore an actual analytic germ near \(K\).
Its formal jets agree with the germ of Step 1: the pullback through
\(k\exp P\) is exactly the iterated formal Lie exponential,
and the invariant-jet dictionary makes this equality unique.
All identities (1.38c) and the central equations have identical
formal jets on their common neighborhoods. Analyticity
therefore proves those identities there, and proves uniqueness.
This completes Theorem 1.32 without a supplied realization.

#### Proof dependencies

The algebraic finite-generation and central-scalar input is the
proof of Theorem 1.27; the exact root-frame and Newton radial calculation
is the radial computation in Theorem 1.28, Step 3. The pole refinement, formal-germ
dictionary, Fuchsian convergence and polynomial extrapolation
are proved here. Neither a source's subrepresentation statement,
a globalization theorem, an asymptotic expansion, nor an
abstract analytic-vector theorem is used.

### The nonzero minimal Jacquet quotient without a supplied realization

Use the notation of Theorem 1.32 above. In particular
\(V\) is an arbitrary irreducible admissible real or complex
general linear Harish-Chandra core, \(V^\vee\) is its algebraic
admissible contragredient, and its coefficient germs have been
constructed and proved convergent without any actual
noncompact representation.

**Theorem 1.33.** For every \(n\ge1\), and \(F=\mathbb R\) or
\(\mathbb C\),
\[
 V/\mathfrak n V\ne0,
 \tag{1.38p}
\]
where \(\mathfrak n\) is the complexified upper unitriangular
Lie algebra. The quotient is finite-dimensional by Theorem 1.27.
The same conclusion holds for the lower unitriangular algebra.

The proof first extends the scalar germs only to matrices
with distinct singular values. It never assumes extension
across the singular walls, or that those scalar functions
already come from an actual representation.

#### Step 1: Analytic continuation on the regular chamber

Let
\[
 C=\{x\in\mathbb R^n:x_1<\cdots<x_n\}.
 \tag{1.38q}
\]
For one fixed finite compact coefficient array, the analytic
germ of Theorem 1.32 gives the jet \(J\) of (1.34n) on a neighborhood
of zero intersected with \(C\). The matrix system
\(\partial_iJ=A_i(x)J\) of (1.34o) has analytic coefficients
everywhere in \(C\).
The explicit coefficients consist of finite products,
derivatives and quotients in (1.38e), whose denominators
do not vanish there.

For \(x\in C\) choose \(\delta>0\) small enough that
\(\delta x\) lies in that germ neighborhood, and solve the
ordinary linear equation
\[
 \frac{d}{dt}J(tx)=
       \left(\sum_i x_iA_i(tx)\right)J(tx),
 \qquad \delta\le t\le1,
 \tag{1.38r}
\]
with its germ value at \(\delta x\).
There is a unique solution on this compact interval.
For completeness, on a small interval the iterated integral
series has its \(m\)-th increment bounded by
\(M^m|t-\delta|^m/m!\) times the initial norm.
It converges uniformly, differentiates to the equation,
and the same integral iteration proves uniqueness.
Finitely many such intervals cover the path.
Choosing a smaller admissible \(\delta\) gives the same
solution, because the known germ already solves (1.38r)
on their overlap.

This construction is analytic in \(x\). Around any fixed
path, the explicit matrix coefficients extend
holomorphically to a small complex neighborhood of its
compact parameter set, with uniform bounds. The initial
germ is holomorphic there as well. The same iterated
integral series converges normally in \(x,t\) on successive
small intervals, so the endpoint is holomorphic in \(x\).
Use a fixed sufficiently small \(\delta\) for each such
parameter neighborhood; independence of \(\delta\)
patches the results into an analytic \(J\) on all \(C\).

The differences
\(\partial_iJ-A_iJ\) and
\(J_\alpha-\partial^\alpha J_0\) are analytic on \(C\).
They are zero on its nonempty germ portion, so they are
zero everywhere. Here the elementary identity principle
requires no additional PDE theorem: an analytic function
zero on a ball has all its Taylor derivatives zero there;
overlapping analytic balls continue this fact along any
path. The convex set \(C\) is connected.
Thus the continued \(J\) is the genuine full finite jet
of its zeroth component and solves every radial equation,
not just the particular ray equation used to construct it.

#### Step 2: Scalar functions on the regular part of the group

Every matrix in
\[
 G_{\mathrm{reg}}
 =\{g:g^*g\text{ has }n\text{ distinct eigenvalues}\}
\]
has an ordered singular-value factorization
\(g=k_1a(x)k_2\), \(x\in C\), \(k_i\in K\).
Lemma 1.32a supplies this factorization directly:
diagonalize \(g^*g\), take positive square roots of the
eigenvalues and normalize the resulting columns of \(g\).
Define
\[
 c_{v,w}(k_1a(x)k_2)
       =F_{k_2v,k_1^{-1}w}(x),
 \tag{1.38s}
\]
where \(F\) is the continued zeroth radial component.
The required compact translates form finite arrays, so
this formula is well-defined by the preceding construction.
Changing to a larger finite array gives exactly the same
components: the analytic continuations agree on the initial
germ portion of \(C\), hence everywhere in \(C\).
The same argument preserves all bilinear relations between
different pairs. Thus these separately constructed finite
arrays define one consistent bilinear family.

The only ambiguity with ordered distinct singular values
is \((k_1,k_2)\mapsto(k_1m,m^{-1}k_2)\), where \(m\) is a
diagonal sign matrix or diagonal unitary matrix. To check
this, compare two factorizations and square the positive
diagonal factor. A compact matrix commuting with a diagonal
matrix of distinct eigenvalues is diagonal; its entries
are signs or phases. Invariance of \(B\), and commutation
of this \(m\) with all \(H_i\), give
\[
 F_{m^{-1}v,m^{-1}w}(x)=F_{v,w}(x)
\]
on the formal germ, then on all \(C\) by analyticity.
This proves independence of the ambiguity in (1.38s).

The functions are analytic locally on \(G_{\mathrm{reg}}\).
Here a local analytic singular-value factorization can
also be verified without a spectral perturbation theorem.
At a simple eigenvalue, the characteristic polynomial has
nonzero derivative. Its nearby root is given by the
uniformly convergent Newton iteration on a sufficiently
small complex coordinate neighborhood: its derivative
stays bounded away from zero and the Newton error squares
at each step. This gives an analytic root. The projectors
\(\prod_{j\ne i}(g^*g-\lambda_j I)/(\lambda_i-\lambda_j)\)
are analytic. Apply each to a fixed eigenvector which
remains nonzero locally, and divide by the positive square
root of its squared norm, using the branch positive at
the starting point. These are analytic orthonormal
eigenvectors in real coordinates. The left singular
vectors are obtained by division by the nonzero singular
values. This supplies the desired local coordinates.

Each determinant component of \(G_{\mathrm{reg}}\) is
connected. For the real group the factorization is the
image of \(SO(n)\times C\times SO(n)\), or of the same
space with one fixed compact reflection inserted.
A simultaneous diagonal sign in the two compact factors
changes both compact determinants, so these images cover
the corresponding determinant component. \(SO(n)\) is
connected: successive rotations in coordinate planes
reduce an orthogonal matrix of determinant one to
identity, and reversing those finite rotations gives a
path. \(U(n)\) is connected by diagonalizing a unitary
matrix and replacing its eigenphases by their multiples
of a parameter between zero and one. Its unitary diagonalization is proved in Lemma 1.32a. Rank one is treated separately below.

Consequently the Lie and compact identities (1.38c)
extend from the germ to all \(G_{\mathrm{reg}}\).
For a Lie identity, both sides are analytic on this open
set, including the derivative of the analytic left side.
They agree on a nonempty germ portion of each component,
so the identity principle applies. Compact covariance
also follows directly from (1.38s). The scalar central
equations extend in the same way.

#### Step 3: One exponential bound for all abstract core pairs

This is the step that replaces the supplied moderate
dual-pair topology used in Theorem 1.28, Step 2.
Choose finite compact-stable algebraic generating spaces
\(W\subset V\), \(U\subset V^\vee\), so that
\[
 U(\mathfrak g)W=V,\qquad
 U(\mathfrak g)U=V^\vee.
 \tag{1.38t}
\]
Such spaces exist by irreducibility, exactly as in Theorem 1.27, Step 1.
Take the one finite coefficient array consisting of
all pairs in fixed bases of \(W,U\).
It contains every left and right compact translate of
these pairs. Let \(J_{\mathrm{base}}\) be its central
radial finite jet.

Choose \(x^{(0)}\in C\) and
\(H_1>\cdots>H_n\), and put
\[
 x(t)=x^{(0)}-tH,\qquad
 a_t=a(x(t)),\qquad t\ge0.
 \tag{1.38u}
\]
All gaps remain at least
\(\eta=\min_i(x^{(0)}_{i+1}-x^{(0)}_i)>0\).
The explicit 1.34o system is bounded on this fixed-gap
chamber portion. Therefore its ordinary integral
iteration gives
\[
 \|J_{\mathrm{base}}(x(t))\|
       \le \|J_{\mathrm{base}}(x^{(0)})\|e^{Mt}
 \tag{1.38v}
\]
for one finite \(M\), depending on this base array and ray.

Every fixed radial derivative of every base component
is a linear combination of that same finite jet with
bounded coefficients along the ray. This follows by
differentiating (1.38g)–(1.38h) and reducing total order,
as in Theorem 1.28, Step 3: every required fixed derivative of the
coefficients in (1.38e) is bounded when the gaps are
at least \(\eta\).

The same assertion holds for an arbitrary fixed left
and right Lie differential word on a base component.
To make its angular uniformity precise, lift right
fields to \(K\times C\times K\). For
\(g=k_1a(x)k_2\), conjugate a right generator by \(k_2\)
and write \(a(x)\operatorname{Ad}(k_2)X\) as radial,
left compact and right compact fields using (1.38e).
The real diagonal is radial and the imaginary diagonal
is compact. This is a global differential lift; the
compact diagonal redundancy is harmless because the
pulled-back function is invariant under it. Left
fields are obtained by the analogous decomposition,
or by the same computation on the inverse matrix.
All angular coefficients are bounded with all fixed
angular derivatives on the compact factors. Composition
of finitely many fields and the product rule therefore
give a finite sum of radial derivatives and compact
derivatives with bounded coefficients on the fixed-gap
portion. Compact derivatives act by matrices on the
same base array; radial derivatives reduce to its same
finite jet. Hence for every fixed \(D,E\),
\[
 |L_D R_E c_{w,u}(a_t)|\le C_{D,E,w,u}e^{Mt},
 \quad w\in W,\ u\in U,
 \tag{1.38w}
\]
with exactly the \(M\) of (1.38v). The constants may
depend on the words; the exponential rate does not.

By (1.38t) and the globally valid Lie identities,
every \(c_{v,w}\) is a finite linear combination of
such differentiated base components. We have proved
\[
 |c_{v,w}(a_t)|\le C_{v,w}e^{Mt}
 \quad(v\in V,\ w\in V^\vee)
 \tag{1.38x}
\]
with **one \(M\) for all pairs**, including all
differentiated pairs. This is a bound on the specified
regular ray. No global-growth theorem, topology,
continuity of an abstract functional or classification
is being presumed.

#### Step 4: The contracting-root contradiction

Suppose \(V=\mathfrak nV\). Induction then gives
\(V=\mathfrak n^qV\) for every positive integer \(q\).
Every core vector is a finite sum
\(X_1\cdots X_qv'\), with \(X_j\) upper-root generators,
including their imaginary companions for the complex
field. For the ray (1.38u),
\[
 \operatorname{Ad}(a_t)X_{ij}
  =e^{x^{(0)}_i-x^{(0)}_j}
     e^{-t(H_i-H_j)}X_{ij}.
 \tag{1.38y}
\]
Put \(\epsilon=\min_i(H_i-H_{i+1})>0\).
The identity between left and right tangent vectors
at a fixed \(g\), combined with (1.38c), gives
\[
 c_{Xv,w}(g)=-c_{v,\operatorname{Ad}(g)X\,w}(g).
 \tag{1.38z}
\]
Iterate this pointwise identity; \(g\) stays fixed
while the pairs are replaced, so no derivative of
the coefficient \(\operatorname{Ad}(g)\) is introduced.
For a word the dual order is reversed:
\[
 c_{X_1\cdots X_qv',w}(g)
  =(-1)^q c_{v',
       \operatorname{Ad}(g)X_q\cdots
       \operatorname{Ad}(g)X_1w}(g).
\]
Equations (1.38x)–(1.38y) imply for every pair
\[
 |c_{v,w}(a_t)|
       \le C_{q,v,w}e^{(M-q\epsilon)t}.
 \tag{1.38aa}
\]
The constant may depend on \(q\); the \(M\) does not.

Choose \(v,w\) with \(B(v,w)\ne0\).
Its analytic diagonal germ is nonzero at identity,
so choose a sufficiently small \(x^{(0)}\in C\)
with \(F_{v,w}(x^{(0)})\ne0\).
The finite compact array of this pair has nonzero
initial jet \(J_0\). Its own bounded radial system
along the ray gives, by the backwards integral
iteration,
\[
 \|J(t)\|\ge e^{-M_0t}\|J_0\|,\qquad t\ge0.
 \tag{1.38ab}
\]
Each component is a coefficient of fixed core pairs:
compact translation stays in the core, and radial
derivatives apply commuting diagonal Lie generators
to the first member of the pair. Apply (1.38aa) to
these finitely many components. Choose
\(q\epsilon>M+M_0+1\). The resulting upper bound
contradicts (1.38ab) as \(t\) tends to infinity.
This proves (1.38p).

For \(n=1\) there is no nilpotent algebra and
\(V/\mathfrak nV=V\ne0\). The central Lie algebra
and compact action make the irreducible admissible
core one-dimensional by the same finite-packet
eigenvector argument as in Theorem 1.27. No chamber argument
is needed. Conjugating upper roots by the compact
long permutation proves the lower version.

#### Scope

Theorem 1.33 is purely about arbitrary abstract
irreducible admissible cores, in every rank for
both archimedean fields. The auxiliary scalar
functions have been proved analytic only on a
neighborhood of \(K\) and on \(G_{\mathrm{reg}}\).
Their use establishes a nonzero finite Jacquet
quotient; it does not silently declare them
matrix coefficients of an already globalized core.
The compatible actual completion will instead be
constructed from the algebraic Borel occurrence
and the already written closed-principal-model
proof.

### Full Borel occurrence and an actual compatible realization of every core

Let \(V\) be any irreducible admissible Harish-Chandra core of
\(GL_n(\mathbb R)\) or \(GL_n(\mathbb C)\), in every rank.
Theorems 1.27 and 1.33 prove that its upper minimal Jacquet
quotient is finite-dimensional and nonzero. Those proofs
require no pre-existing realization.

**Theorem 1.34.** There is an explicit injective core map
\[
 T_0:V\hookrightarrow I_0(\chi_1,\ldots,\chi_n)
 \tag{1.38ac}
\]
into a full normalized Borel induction, and a full inverse
Borel core surjecting onto \(V\). The closure of (1.38ac) in
the actual compact smooth induced model has exactly core
\(V\). With the paired principal annihilator quotient it
is a complete Fréchet smooth moderate-growth continuous
dual-pair realization of \(V,V^\vee\), with jointly
continuous nondegenerate invariant bilinear pairing.

This asserts existence of a compatible actual realization
for an arbitrary core, rather than identification with
every independently prescribed smooth topology. The
principal-core quotient is onto algebraically; no onto
range for its extension to another topology is inferred.

#### Step 1: The algebraic occurrence map

Put \(d=[F:\mathbb R]\), \(M=K\cap B\), and
\(\rho_i^0=(n+1)/2-i\).
On the nonzero finite quotient \(V/\mathfrak nV\), the
diagonal real Lie operators commute with one another
and with the compact diagonal group \(M\). Average a
positive Hermitian form over \(M\); by Lemma 1.32a, the commuting
unitary compact matrices split the quotient into
character spaces. On one nonzero such space, the
commuting transposed diagonal operators have a common
eigenvector: choose an eigenspace for one transpose and
continue restricting to it when a remaining operator
is not scalar. Its dimension strictly drops at such
a step, so the procedure terminates. Pull it back to
a nonzero algebraic functional \(\ell_0\) on \(V\):
\[
 \ell_0(\mathfrak nV)=0,\quad
 \ell_0(H_iv)=\beta_i\ell_0(v),\quad
 \ell_0(mv)=\sigma(m)\ell_0(v).
 \tag{1.38ad}
\]
This is the same finite-dimensional construction as
(1.34u), now with the nonzero quotient justified for
an arbitrary core by Theorem 1.33.

The character \(\sigma\) has sign exponents
\(e_i\in\{0,1\}\) in the real case and integer circle
exponents \(l_i\) in the complex case. The circle
statement follows directly from the finite-dimensional
smooth character differential equation and period
\(2\pi\). Define
\[
 t_i=\beta_i/d-\rho_i^0,\qquad
 \chi_i(x)=\operatorname{sgn}(x)^{e_i}|x|^{t_i}
                   \quad(F=\mathbb R),
 \quad
 \chi_i(z)=(z/|z|)^{l_i}|z|_{\mathbb C}^{t_i}
                   \quad(F=\mathbb C).
 \tag{1.38ae}
\]
Thus the inducing character \(\delta_B^{1/2}\prod_i\chi_i\)
has exactly the infinitesimal diagonal and compact
characters of \(\ell_0\), including the factor \(d\).
The actual full compact model \(I(\boldsymbol\chi)\)
and its smooth action are the row-QR model constructed
in Theorem 1.26 above.

Set
\[
 (T_0v)(k)=\ell_0(kv),\qquad k\in K.
 \tag{1.38af}
\]
Its compact orbit is finite; it is smooth and has the
prescribed left \(M\)-covariance. For a real Lie generator
\(X\), differentiate the actual factorization
\(k\exp(tX)=b(t,k)k'(t,k)\).
Its infinitesimal decomposition is
\(\operatorname{Ad}(k)X=Y_B+Y_K\), with \(Y_B\)
upper triangular with real diagonal and \(Y_K\) compact.
The derivative of its multiplier equals the eigencharacter
of \(\ell_0\) on \(Y_B\); the compact derivative contributes
\(\ell_0(Y_Kkv)\). Therefore
\[
 (dI(X)T_0v)(k)
       =\ell_0((Y_B+Y_K)kv)
       =\ell_0(kXv)=(T_0Xv)(k).
 \tag{1.38ag}
\]
This is a linear identity even where \(\ell_0(kv)=0\);
no division is taken. Right compact translation gives
the compact intertwining. \(T_0\) is nonzero because
evaluation at identity is \(\ell_0\); its Lie- and
compact-stable kernel is zero by irreducibility.

Apply the same construction to the abstract \(V^\vee\).
The compact integral pairing between full induction
with characters \(\boldsymbol\eta\) and
\(\boldsymbol\eta^{-1}\), proved in Theorem 1.26, pairs their
finite packets perfectly. Transposing the injection
of \(V^\vee\) on each finite packet gives an onto
map of that packet onto its dual packet in \(V\).
The algebraic direct sum of these maps is the onto
core map
\[
 I_0(\boldsymbol\eta^{-1})\twoheadrightarrow V.
 \tag{1.38ah}
\]
No global topological quotient is needed to justify
this finite-packet transposition. It is precisely
the interface (1.34y), now available for every core.

#### Step 2: A concrete complete smooth paired model

Let \(S_0=T_0(V)\subset I_0(\boldsymbol\chi)\), and put
\[
 E=\overline{S_0}^{\,C^\infty(K)},\qquad
 E^\vee=
 I(\boldsymbol\chi^{-1})/
       \operatorname{Ann}(E).
 \tag{1.38ai}
\]
The closure and annihilator are taken in the actual
compact smooth induced spaces, with their countable
derivative seminorms and the compact integral pairing.
This is the special case \(W_0=0,V_0=S_0\) of the
closure construction of Theorem 1.26a above.
We state its concrete verified conclusions and the
mechanisms relevant to this construction.

First, compact-finite vectors in a full compact model
are coordinate polynomials. This is proved using the
positive polynomial compact approximate identities
(1.32h), finite-dimensional compact decomposition and
Schur orthogonality. Row-QR applied to
\(k\exp(tX)\) gives a holomorphic exponential expansion
in a disk whose radius is independent of that coordinate
polynomial: its row-Gram pivots stay near one uniformly
on compact \(K\). Thus its compact-smooth Taylor series
converges on a common disk. Every Taylor coefficient
of a vector in \(S_0\) stays in \(S_0\), by Lie stability.
Continuity, the common radius, finite iteration and
polar generation of \(G\) make its closure \(E\) an
actual closed \(G\)-subrepresentation. This is the
group-stability proof in Theorem 1.26a, Steps 2–3.

Second, every compact projector has finite-dimensional
range. Projecting the closure \(E\) puts its packet in
the closure of the packet of \(S_0\), which is already
a closed finite-dimensional subspace. Hence the
core of \(E\) is exactly \(S_0\), and is identified
with \(V\) through (1.38ac). The annihilator is closed
and group-stable by the invariant continuous pairing.
Finite packet duality gives exactly the core
\(V^\vee\) in the quotient in (1.38ai), as proved in
Theorem 1.26a, Steps 4–5. The quotient is Fréchet and complete:
Theorem 1.26a gives the explicit summable lifting argument
for a Cauchy sequence in a closed Fréchet quotient,
not an assumed comparison theorem.

Third, the full induced actions and all their
derivatives are continuous and moderate, with
polynomial matrix-height bounds on each compact
derivative seminorm from Theorem 1.26. Restriction to a closed
subspace and the quotient seminorm bounds preserve
these properties; quotient smoothness and differentiation
are verified by the actual smooth lift in Theorem 1.26a.
The compact integral gives the jointly continuous
invariant pairing
\[
 E\times E^\vee\longrightarrow\mathbb C.
 \tag{1.38aj}
\]
It is nondegenerate in both variables: a nonzero
compact packet has a detecting paired packet by
finite-dimensional duality, and the compact polynomial
approximate identities detect a nonzero vector.
The same identities prove density of both cores.
These are actual maps and actual complete spaces.

Finally, core irreducibility makes \(E\) and \(E^\vee\)
topologically irreducible. A nonzero closed invariant
subspace has a nonzero compact-finite vector by the
positive compact approximate identities. Its core
is then the whole irreducible core, whose density
makes that subspace the whole model.
This completes Theorem 1.34.

#### Step 3: Consequences and comparison

Every irreducible admissible abstract core therefore has a compatible
actual complete smooth moderate dual pair. Theorem 1.31 applies to
this constructed pair and proves its attained Gaussian ideal, entire
Schwartz division and paired Fourier equation.

For a separately prescribed actual complete smooth moderate dual
pair, Theorems 1.29–1.31 give coefficient comparison, a complete common
refinement and the Gaussian package in that original topology.
Theorems 2.0x–2.0y below extend a principal-core quotient continuously
with dense range and embed the entire continuous dual. None of these
dense-range statements proves surjectivity or an inverse seminorm
estimate for a comparison with an independently prescribed topology.

The integral-defined polynomial in Theorem 1.31 also requires a
separate computation to identify it with every intended real
discrete-series, parity and complex angular standard-factor label.

### The remaining canonical archimedean input

Theorem 1.21 proves continuation, entire division by a common pole majorant and rapid strip bounds for every smooth coefficient and Schwartz test in the stated actual dual-pair models. Theorem 1.22 proves their scalar Fourier equation, including reflection and character scaling. Proposition 1.21b and Corollary 1.22e prove full-Schwartz canonical division and constant epsilon once the genuine Gaussian ideals have been established; Corollary 1.22f proves the scalar critical-line phase in compatible unitary models. Theorem 1.19 and Theorems 1.11–1.13 furnish the actual smooth pair for cuspidal automorphic constituents.

Theorem 1.26 proves the exact Gaussian product and one-pair attainment for every full real/complex Borel induction in the actual compact model, including reducible inductions. Theorems 1.26a–1.26b construct actual closed subquotient/dual models for every supplied principal-core subquotient and prove its exact monic polynomial correction, finite attaining family, entire Schwartz division and Fourier equation. Theorem 1.28 proves all-rank principal-core occurrence for every prescribed actual smooth moderate dual pair; Theorems 1.29–1.31 prove coefficient comparison, a complete common refinement, and the full Gaussian package in that original realization. Theorems 1.32–1.34 prove abstract-core existence and full Borel occurrence. Full onto/closed-image comparison with separately prescribed topologies remains open, together with explicit standard-factor identification of the correction polynomial and scalar. The generator normalization in Theorem 1.26b is monic relative to its supplied inducing product. Theorem 1.31 proves the paired dual and unitary conjugation normalization of these integral-defined factors. For every abstract irreducible admissible core, Theorem 1.34 supplies such an actual smooth dual pair. Propositions 1.7 and 1.18 supply the complete canonical package for determinant characters over both real and complex fields. The majorant example (1.25t) shows why polynomial-module stability and an entire common-denominator quotient cannot replace the Gaussian-ideal proof.

The freely accessible [Goldfeld–Jacquet author notes, §3, Theorem 3.5 and Lemma 3.6, PDF pages 14–19](https://www.math.columbia.edu/~goldfeld/LanglandsBookChapter.pdf) describe the canonical archimedean package. Their induced-representation reduction and generator statements do not supply the missing full proof. The continuation, distributional descent and Fourier arguments above are proved here.

### Matrix theta estimates and singular orbits

Take cusp vectors \(\phi\in\pi_0\) and \(\widetilde\phi\in\widetilde\pi_0\), paired by

\[
c(g)=\int_{[G]^1}\phi(xg)\widetilde\phi(x)\,dx.
\tag{1.5p}
\]

For a Schwartz–Bruhat function \(\Phi\) on \(M_n(\mathbb A)\), define

\[
K_\Phi(t)=\int_{[G]^1\times[G]^1}
\widetilde\phi(x)\phi(y)
\sum_{\gamma\in G(F)}
\Phi(x^{-1}a_t\gamma y)\,dx\,dy.
\tag{1.5q}
\]

We first justify the sums and integrations.

**Lemma 1.1d (matrix lattice bounds).** For \(x=b\omega_1\), \(y=b'\omega_2\) in the Siegel sets of 1.1a, there are polynomial height bounds

\[
\sum_{\substack{\gamma\in M_n(F)\\\gamma\ne0}}
|\Phi(x^{-1}a_t\gamma y)|
\le C H(x,y)^C t^{-n}\quad(0<t\le1),
\qquad
\le C_M H(x,y)^{C_M}t^{-M}\quad(t\ge1).
\tag{1.5r}
\]

The same estimates hold after any number of logarithmic \(t\)-derivatives.

**Proof.** The compact \(\omega_i\) put the transformed tests in a bounded Schwartz family with a common finite support. Rational matrices in that support lie in a fixed full lattice \(\mathcal M\) in \(M_n(F_\infty)\), of real dimension \(D=n^2d\). Set \(\lambda=t^{1/(nd)}\). A matrix height \(H\ge1\) bounds the inverse operator norm of \(X\mapsto b^{-1}Xb'\), so Schwartz bounds reduce the sum to
\(\sum_{X\in\mathcal M\setminus\{0\}}(1+\lambda H^{-1}\|X\|)^{-N}\).

A lattice has \(O((1+R)^D)\) points in a ball of radius \(R\), and a positive minimum length. Dyadic summation therefore bounds this sum by \(C_N\eta^{-D}\) for \(0<\eta=\lambda/H\le1\), and by \(C_N\eta^{-N}\) for \(\eta\ge1\), when \(N>D\). For \(t\le1\), this is \(C H^D t^{-n}\). For \(t\ge1\), choose \(N>D+ndM\). In the region \(\lambda\le H\), the first bound is at most \(C H^N\lambda^{-ndM}\); in the region \(\lambda\ge H\), the second has the same upper bound. This is the second estimate. A logarithmic derivative replaces \(\Phi\) by a constant multiple of its archimedean Euler derivative, which is again Schwartz. \(\square\)

Multiplying (1.5r) by \(|\widetilde\phi(x)\phi(y)|\) and using Lemma 1.1b makes both height factors integrable. Hence \(K_\Phi(t)=O(t^{-n})\) at zero and \(O_M(t^{-M})\) at infinity. The same proof works for the sum over matrices of any fixed positive rank. All these statements also hold for \(\widehat\Phi\).

For \(0<r<n\), matrices of rank \(r\) form one \(G(F)\times G(F)\)-orbit of \(e_r=\operatorname{diag}(I_r,0)\). Its stabilizer consists of pairs \(p,q\) satisfying \(p^{-1}e_rq=e_r\), or

\[
p=\begin{pmatrix}A&B\\0&D\end{pmatrix},
\qquad q=\begin{pmatrix}A&0\\C&E\end{pmatrix}.
\tag{1.5s}
\]

Unfold the rank-\(r\) sum in the double quotient integral. This is legitimate by the absolute estimate just proved. The stabilizer contains the upper and lower block radicals

\[
U_+=\left\{\begin{pmatrix}I&B\\0&I\end{pmatrix}\right\},
\qquad
U_-=\left\{\begin{pmatrix}I&0\\C&I\end{pmatrix}\right\}.
\tag{1.5t}
\]

Their adelic quotients by rational points are compact copies of
\((F\backslash\mathbb A)^{r(n-r)}\). Disintegrate the unfolded integral first over these two normal unipotent subgroups. The matrix kernel is unchanged, since \(U_+^{-1}e_r=e_r=e_rU_-\). Its two inner averages are therefore the \(U_+\)-constant term of \(\widetilde\phi\) and the \(U_-\)-constant term of \(\phi\). Both are zero by cuspidality. Thus every positive singular-rank contribution vanishes. Norm-one restrictions do not affect these inner averages, since unipotent determinants are one.

The zero matrix also contributes zero. To justify this separately, integration on the finite-volume quotient gives a bounded \(G^1\)-invariant functional on the unitary space of \(\pi_0\). Restriction from \(G(\mathbb A)=a_{\mathbb R_{>0}}G^1\) to \(G^1\) remains irreducible, because the removed central group acts by scalars. A nonzero invariant functional would therefore make this restriction trivial. Its forms would be constant on \(G^1\), contradicting a proper-parabolic zero constant term when \(n\ge2\). Hence
\(\int_{[G]^1}\phi=\int_{[G]^1}\widetilde\phi=0\), and the rank-zero double period is zero.

### Poisson summation and the Mellin transform

Additive self-duality, covolume one and Poisson summation for \(F\backslash\mathbb A\) are proved in *Additive characters, self-dual measures and Poisson summation*, Theorems 5.4–5.5. Their finite Cartesian product applies to \(M_n\). The trace pairing exchanges the \((i,j)\) and \((j,i)\) coordinates, so the annihilator of \(M_n(F)\) is again \(M_n(F)\), with covolume one. Whole-block Schwartz inversion is the same real-vector-space calculation as Lemma 5.4A there; lattice periodization is justified by the same dyadic argument, in dimension \(n^2d\). Thus this application includes Schwartz functions whose archimedean matrix entries do not separate.

The linear map \(T(X)=x^{-1}a_tXy\) has additive modulus \(t^n\), since \(\nu(x)=\nu(y)=1\) and scalar multiplication by \(a_t\) on \(n^2\) entries has modulus \(t^n\). Its trace adjoint is \(T^*(Y)=a_tyYx^{-1}\). Poisson gives

\[
\sum_{\gamma\in M_n(F)}\Phi(x^{-1}a_t\gamma y)
=t^{-n}\sum_{\gamma\in M_n(F)}
\widehat\Phi(y^{-1}a_t^{-1}\gamma x).
\tag{1.5u}
\]

Integrate against \(\widetilde\phi(x)\phi(y)\). Every singular-rank period on both sides vanishes by (1.5s)–(1.5t) and the zero-rank argument. Therefore, denoting the swapped cusp vectors on the right explicitly,

\[
K_\Phi(t;\phi,\widetilde\phi)
=t^{-n}K_{\widehat\Phi}(t^{-1};\widetilde\phi,\phi).
\tag{1.5v}
\]

The large-\(t\) bound in Lemma 1.1d now shows that \(K_\Phi\) also decreases faster than every power at zero: choose the exponent on the right larger than \(n\) plus any prescribed power. This conclusion holds for every logarithmic derivative; differentiate (1.5v), using the derivative bounds already proved at infinity.

For \(\operatorname{Re}s>(n+1)/2\), absolute unfolding of the matrix-coefficient integral gives

\[
Z(s,\Phi,c)=\int_{G(\mathbb A)}\Phi(g)c(g)\nu(g)^{s+(n-1)/2}\,dg
=\int_0^\infty K_\Phi(t)t^{u}\,\frac{dt}{t},
\qquad u=s+(n-1)/2.
\tag{1.5w}
\]

One first inserts (1.5p), changes \(g\) to \(x^{-1}g\), then writes \(g=a_t\gamma y\) with \(y\in[G]^1\). The absolute integral of the unfolded expression is finite: (1.5r) and rapid cusp decay bound its small-\(t\) part by a constant times \(\int_0^1t^{\operatorname{Re}u-n}dt/t\), and its large-\(t\) part by an arbitrarily fast decaying power. Haar measures in (1.5w) are chosen compatibly with (1.5a).

Both ends of the Mellin integral are now rapidly decreasing. For every compact set of \(s\), the integral and all its \(s\)-derivatives converge uniformly, since derivatives insert powers of \(\log t\). It defines an entire function. More precisely, put \(v=\log t\). On every closed strip the function
\(K_\Phi(e^v)e^{(\operatorname{Re}s+(n-1)/2)v}\), together with every \(v\)-derivative, is integrable uniformly in \(\operatorname{Re}s\). Repeated integration by parts, with zero boundary terms, proves

\[
Z(s,\Phi,c)=O_{a,b,N}\bigl((1+|\operatorname{Im}s|)^{-N}\bigr)
\quad(a\le\operatorname{Re}s\le b)
\tag{1.5x}
\]

for every \(N\). This proves the required strip control without a Phragmén–Lindelöf argument.

Changing \(t\) to \(t^{-1}\) in (1.5w) and using (1.5v) changes the exponent to \(n-u=(1-s)+(n-1)/2\). The swapped vectors give \(c^\vee\). Hence the global integral functional equation is

\[
Z(s,\Phi,c)=Z(1-s,\widehat\Phi,c^\vee).
\tag{1.5y}
\]

The shift in (1.5) is exactly what turns \(u\mapsto n-u\) into \(s\mapsto1-s\).

### Cuspidal Hilbert realizations and products of local pairings

Let \(F\) be a number field, \(d=[F:\mathbb Q]\), \(G=GL_n\), and \(\nu(g)=|\det g|_{\mathbb A}\). Put \(G^1=\ker\nu\), \(\Gamma=G(F)\), and \(X=\Gamma\backslash G^1\). For \(t>0\), take \(a_t\) to have scalar entry \(t^{1/(nd)}\) at every infinite embedding and entry \(1\) at the finite places. Then \(\nu(a_t)=t\), and \(G(\mathbb A)=a_{\mathbb R_{>0}}\times G^1\). We fix probability Haar measure on the norm-one idèle class group and a compatible quotient Haar measure \(dx\) on \(X\). Inner products are linear in the first argument.

The statements below concern an actual admissible cuspidal Hilbert constituent, and also give a reverse comparison under an explicit square-integrability hypothesis. They prove the product pairing and the compatible unitary tensor realization. Theorem 1.19 below proves existence and admissibility of every cuspidal constituent by elliptic estimates, a cusp-tail bound and a spectral decomposition.

**Central normalization.** An irreducible admissible automorphic module has a continuous scalar central character. Its restriction to the norm-one idèle classes is unitary. Its positive-central action is \(a_t\mapsto t^\mu\) for some \(\mu\in\mathbb C\). Consequently \(\pi_0=\pi\otimes\nu^{-\operatorname{Re}\mu}\) has unitary central character, and its positive-central action is \(t^{i\operatorname{Im}\mu}\). This normalization needs no L-function theorem.

To verify this even for the algebraic subquotient definition, the central Lie generators act on every automorphic form through finite-dimensional spaces, by enveloping-center finiteness. On each such space, solving the constant-coefficient ordinary differential equation for central real translation gives the matrix exponential of the Lie action. Thus these translations preserve algebraic mixed submodules and their quotients. Finite-place central elements and the compact real center already act in the mixed category. Every central translation operator commutes with the mixed action; the finite-corner Schur argument makes it scalar on an irreducible admissible module. The positive-central generator is likewise scalar \(\mu\), giving \(t^\mu\). Continuity follows from this exponential formula, the compact real action, and finite-place smoothness on a nonzero finite-level vector. Scalar rational translations are trivial by left automorphy. Finally \(F^\times\backslash\mathbb A^1\) is compact by *Idèles and the idèle class group*, Theorem 3.3; a continuous character of a compact group has modulus one, since its modulus has compact image in \(\mathbb R_{>0}\), whose only compact subgroup is \(\{1\}\). Twisting by the indicated power of \(\nu\) removes just the real part of \(\mu\). All Hilbert assertions below apply to \(\pi_0\); the original module is recovered by the inverse twist.

**Lemma 1.8 (the cuspidal Hilbert space).** The space \(L^2(X)\) carries a strongly continuous unitary right action of \(G^1\). For each unitary character \(\omega^1\) of \(F^\times\backslash\mathbb A^1\), its central \(\omega^1\)-space is a closed invariant subspace. The simultaneous kernel of all proper-parabolic constant terms, interpreted as distributions on the group, is closed and right invariant. Fixing a real number \(\tau\) extends this representation to \(G(\mathbb A)\) by letting \(a_t\) act as \(t^{i\tau}\).

**Proof.** The matrix coordinate embedding and *The adèle ring of a number field*, Theorem 2.2 make \(\Gamma\) closed and discrete. The product formula proved in *Places of number fields in extensions and the product formula*, Theorem 5.2 puts it in \(G^1\). At each place \(|\det g|_v^{-n}d g\), with \(d g\) additive matrix measure, is both left and right Haar measure: either multiplication has additive Jacobian \(|\det g|_v^n\). The restricted product is therefore unimodular, and its central direct-product decomposition makes \(G^1\) unimodular as well.

A quotient measure can be constructed by choosing a measurable fundamental set. Indeed, the group is second countable, so a countable collection of open coordinate sets whose rational translates are disjoint covers the quotient. Enumerate those sets and assign a coset to its first available chart. Restricting Haar measure to the resulting disjoint measurable section defines \(dx\). Left invariance makes the definition independent of the chosen section and gives

\[
\int_X\sum_{\gamma\in\Gamma}h(\gamma x)\,dx
=\int_{G^1}h(g)\,dg
\]

for compactly supported continuous \(h\), first for nonnegative \(h\) and then by linearity. Right Haar invariance now proves right invariance of \(dx\). Thus right translations are unitary. They are strongly continuous: on continuous compactly supported quotient functions, uniform continuity on the compact union of nearby translated supports proves convergence in \(L^2\); regularity of the quotient measure and approximation by such functions give it for every \(L^2\) vector.

The norm-one scalar center acts through \(F^\times\backslash\mathbb A^1\), compact by *Idèles and the idèle class group*, Theorem 3.3. Its character projection is

\[
e_{\omega^1}u=\int_{F^\times\backslash\mathbb A^1}
\overline{\omega^1(z)}R(zI_n)u\,dz.
\]

Character orthogonality makes this a self-adjoint idempotent with the asserted range. Centrality makes the range invariant.

For a proper parabolic with radical \(N_P\), its rational adelic quotient is compact by *Automorphic representations and automorphic L-functions*, Lemma 1.0. Choose compact representatives \(D_P\). On any compact set \(B\subset G^1\), pullback from \(X\) has local \(L^2\)-norm at most a fixed constant times the quotient norm: only finitely many rational translates of a compact lift can meet that lift, because their ratios lie in a compact set intersected with the closed discrete \(\Gamma\). Jensen's inequality and left translation on the group therefore give

\[
\left\|\int_{N_P(F)\backslash N_P(\mathbb A)}u(ng)\,dn\right\|_{L^2(B)}
\le C_B\|u\|_{L^2(X)}.
\]

This also defines the integral as a distribution if a representative has not been chosen. The kernels of these bounded local maps, over all \(B\) and \(P\), have closed intersection. Right translations commute with constant terms, so the intersection is invariant. Finally define, for \(g\in G(\mathbb A)\),

\[
(R_\tau(g)u)(x)=\nu(g)^{i\tau}u\bigl(xg a_{\nu(g)}^{-1}\bigr).
\]

Centrality of \(a_t\) makes this a strongly continuous unitary representation extending the given one. On smooth representatives it is the right action on the extension \(u(a_t x)=t^{i\tau}u(x)\). \(\square\)

**Lemma 1.9 (finite vectors in an admissible unitary representation).** Let \(H\) be an irreducible strongly continuous unitary representation of \(G(\mathbb A)\). Assume that every simultaneous compact-open finite-place fixed space and finite packet of \(K_\infty\)-types is finite dimensional. Then its mixed finite-vector space \(H_{\mathrm{fin}}\) is smooth at infinity, dense, admissible and irreducible as a \((\mathfrak g,K_\infty)\times G(\mathbb A_f)\)-module. It is a common operator core for every real Lie generator. At each finite level it is dense in the smooth-vector topology

\[
p_D(u)=\|dR(D)u\|_H,\qquad D\in U(\mathfrak g).
\tag{1.11}
\]

**Proof.** Finite-place compact-open averages tend strongly to the identity. Compact matrix-coefficient averages do the same at infinity, by the uniform density proved in *Matrix coefficients and the Peter–Weyl theorem*, Theorem 4.1: first average against a continuous probability kernel concentrated near the identity and then approximate that kernel uniformly by a finite sum of coefficients. These averages have finite compact-type range. The two kinds of averaging commute, proving density of \(H_{\mathrm{fin}}\).

Fix one finite-dimensional joint corner \(E=e_Ee_UH\). Average a real smooth compactly supported approximate-identity kernel under conjugation by \(K_\infty\). Its convolution commutes with the compact-type projector, and with \(e_U\), so it preserves \(E\). On \(E\) its strong convergence to the identity is convergence of finite matrices. It is eventually invertible. Its image is smooth, since all derivatives can be transferred to its smooth compact kernel. Thus every vector of \(E\) is smooth. Lie differentiation preserves finite compact type because \(D\) has a finite-dimensional adjoint \(K_\infty\)-orbit in each bounded enveloping degree; it also preserves finite level. We have obtained the mixed module.

The same compact approximation works in every seminorm (1.11). Indeed,

\[
dR(D)R(k)u=R(k)dR(\operatorname{Ad}(k^{-1})D)u,
\]

and the adjoint orbit of \(D\) lies in a finite-dimensional space. Its coefficients vary continuously over the compact group. The orbit of a smooth vector is therefore continuous in all the seminorms, and its compact supremum in any fixed seminorm is finite. Uniform kernel approximation and the approximate-identity argument prove the asserted smooth density, retaining the same finite level.

We give the operator-core argument, since norm density alone would not justify integration of the Lie action. Let \(A_X\) be the generator of \(R(\exp(tX))\). It is closed: if \(u_j\to u\) and \(A_Xu_j\to v\), pass to the limit in \(R(\exp(tX))u_j-u_j=\int_0^t R(\exp(sX))A_Xu_j\,ds\); differentiation of the resulting identity puts \(u\) in its domain with derivative \(v\). Smooth convolution supplies a dense domain. For a smooth compact kernel \(f\) on the real group, let \(L_Xf(g)\) and \(R_Xf(g)\) mean differentiation of \(f(\exp(-tX)g)\) and \(f(g\exp(-tX))\), respectively. Changes of variable in convolution give, for \(u\in\operatorname{Dom}A_X\),

\[
A_XR(f)u=R(f)A_Xu+R\bigl((L_X-R_X)f\bigr)u.
\tag{1.12}
\]

Take mass-one kernels \(f_\epsilon\) in a coordinate ball of radius \(O(\epsilon)\). The coefficients of \(L_X-R_X\) vanish at the identity and are \(O(\epsilon)\) on that ball; the first derivatives of the scaled kernel have \(L^1\)-norm \(O(\epsilon^{-1})\). Hence \(\|(L_X-R_X)f_\epsilon\|_1\) is bounded uniformly. Its integral is zero, because both invariant vector fields have zero divergence for the bi-invariant Haar measure. Strong continuity gives

\[
\left\|R\bigl((L_X-R_X)f_\epsilon\bigr)u\right\|
\le C_X\sup_{g\in\operatorname{supp}f_\epsilon}\|R(g)u-u\|
\longrightarrow0.
\]

Equation (1.12) proves convergence of \(R(f_\epsilon)u\) to \(u\) in the graph norm of \(A_X\). These convolved vectors are real-smooth. Finite-place compact-open averages commute with \(A_X\) and approximate both \(u\) and \(A_Xu\); the real compact smooth approximation just proved then approximates the resulting smooth finite-level vectors in graph norm by mixed finite vectors. Thus \(H_{\mathrm{fin}}\) is a core for \(A_X\).

Let \(M\) be a nonzero algebraic mixed submodule and let \(P\) be orthogonal projection onto its Hilbert closure. This closure is invariant under the compact group and under the finite adelic group, so \(P\) commutes with their averages. For a joint corner \(e\), the subspace \(eM\subset eH\) is finite dimensional and closed. Density gives \(e\overline M=eM\). Therefore \(P\) maps \(H_{\mathrm{fin}}\) into \(M\). On finite vectors, \(M\) and its orthogonal complement are both Lie invariant: for \(u\perp M\), \(\langle dR(X)u,m\rangle=-\langle u,dR(X)m\rangle=0\). Hence \(P A_X=A_XP\) on the common core. Closedness extends this identity to \(\operatorname{Dom}A_X\).

It then holds for the actual one-parameter group. For \(u\) in that domain, differentiate \(R(\exp(-tX))P R(\exp(tX))u\); the derivative is zero. Density proves the commutation identity on all of \(H\). Exponentials generate the identity component, and \(K_\infty\) meets every real component of the general linear group, so \(P\) commutes with the whole adelic representation. Irreducibility gives \(\overline M=H\). Applying each finite-dimensional joint corner again gives \(eM=eH\), and their union is \(H_{\mathrm{fin}}\). Thus \(M=H_{\mathrm{fin}}\). \(\square\)

The smooth space at a fixed finite level, with seminorms (1.11), is Fréchet and complete. To verify completeness, take a sequence for which all word derivatives are Cauchy. Closedness of each one-parameter generator first identifies the limits of its first derivatives and then, successively, the limits of every word derivative. Coordinate products of exponentials and the fundamental theorem of calculus identify the resulting derivatives with derivatives of the orbit map. Thus the limit is a smooth vector. The displayed adjoint identity also proves moderate growth of this smooth representation: coefficients of \(\operatorname{Ad}(g)D\) are polynomially bounded in the entries of \(g\) and \(g^{-1}\).

**Lemma 1.10 (a polynomial quotient Sobolev bound).** At a fixed compact-open finite level \(U\), every real-smooth vector in \(L^2(X)^U\) has a unique smooth representative. Write

\[
\mathcal H(g)=\mathcal H_\infty(g)\mathcal H_f(g),
\quad
\mathcal H_\infty(g)=\max\bigl(1,\|g_v\|,\|g_v^{-1}\|:v\mid\infty\bigr),
\]

where infinite norms are ordinary operator norms, and

\[
\mathcal H_f(g)=\prod_{v<\infty}
\max\bigl(1,|(g_v)_{ij}|_v,|(g_v^{-1})_{ij}|_v:1\le i,j\le n\bigr).
\]

For \(m=dn^2-1>0\) and every right differential operator \(D\), there is a constant \(C_{U,D}\) and a finite list of Lie words of length at most \(m\) such that

\[
|R(D)u(g)|\le C_{U,D}\mathcal H(g)^{2m}
\sum_{|\alpha|\le m}\|R(X_\alpha D)u\|_2,
\qquad g\in G^1.
\tag{1.13}
\]

For \(m=0\) use the corresponding finite-level point-evaluation norm bound. In particular the inclusion of smooth vectors into smooth functions is continuous on compact sets, for every derivative, and all such vectors and derivatives have polynomial growth.

**Proof.** Use a small exponential coordinate box in the real Lie group \(G_\infty^1\), of dimension \(m\). There is a constant \(c_U>0\) such that

\[
g(B_\epsilon\times U)\longrightarrow X
\quad\hbox{is injective if}\quad
0<\epsilon<c_U\mathcal H(g)^{-4}.
\tag{1.14}
\]

Here is an arithmetic verification. If two points in that set differ by \(\gamma\in\Gamma\), then \(g^{-1}\gamma g\) has infinite entries \(O(\epsilon)\) away from the identity and finite component in \(U\). For any nonzero entry \(a\) of \(\gamma-I_n\), finite-place matrix multiplication gives

\[
\prod_{v<\infty}|a|_v\le C_U\mathcal H_f(g)^2,
\qquad
\prod_{v\mid\infty}|a|_v
\le (C\epsilon\mathcal H_\infty(g)^2)^d.
\]

The finite constant is a finite product, since \(U\) is integral outside finitely many places. The product formula makes the product of these two bounds at least one. For \(\epsilon<c_U\mathcal H(g)^{-4}\), with \(c_U\) small enough, their product is less than one. Thus \(\gamma=I_n\), proving (1.14). This uses no Siegel covering or finite-volume theorem.

On the injective chart, \(U\)-invariance gives

\[
\operatorname{vol}(U)\int_{B_\epsilon}|u(gb)|^2\,db\le\|u\|_2^2,
\]

and the same inequality for every right derivative. Chart Haar density is bounded above and below by fixed positive constants. Coordinate derivatives are linear combinations of right Lie words with uniformly bounded smooth coefficients on a fixed small chart.

Choose a smooth cutoff equal to one near zero and supported in the coordinate box, scaled by \(\epsilon\). For a smooth function \(h\) so cut off, iterating the one-variable fundamental theorem of calculus gives

\[
h(0)=(-1)^m\int_0^\infty\cdots\int_0^\infty
\partial_1\cdots\partial_m h(t)\,dt.
\]

The integral has support of volume \(O(\epsilon^m)\). Cauchy–Schwarz and the product rule bound it by a constant times \(\epsilon^{-m/2}\) times the sum of the local \(L^2\)-norms of derivatives of order at most \(m\). Take \(\epsilon\) a fixed multiple of \(\mathcal H(g)^{-4}\) and use the chart inequalities. This proves (1.13).

For an \(L^2\) smooth vector, its group derivatives are weak coordinate derivatives locally: this follows by differentiating translation against a compact coordinate test function. Mollify in those coordinates. Weak derivatives converge in local \(L^2\), and the just proved inequality, applied also after arbitrary derivatives on a smaller box, makes the mollified functions Cauchy in every compact smooth seminorm. Their limit is a smooth representative of the original class. Such representatives agree on overlapping charts, since their difference is continuous and zero almost everywhere. The same argument proves (1.13) for the representative. If \(m=0\), the infinite chart is a single point and its finite \(U\)-fibre has positive measure, giving the asserted norm bound directly. \(\square\)

**Theorem 1.11 (comparison inside an admissible Hilbert cusp constituent).** Let \(H\ne0\) be a closed irreducible subrepresentation of the cuspidal central-character space in Lemma 1.8, and assume its joint compact corners are finite dimensional. Then \(\pi=H_{\mathrm{fin}}\) is an irreducible admissible module of automorphic cusp forms. Moreover

\[
H_{\mathrm{fin}}=H\cap\mathcal A_{\mathrm{cusp},\omega},
\qquad \overline{H_{\mathrm{fin}}}^{\,\|\cdot\|_2}=H.
\tag{1.15}
\]

Its finite-level smooth-vector space has exactly the smooth-realization properties required for continuous archimedean Whittaker functionals.

**Proof.** Lemma 1.9 gives smoothness, irreducibility and admissibility. An endomorphism of this simple module is scalar: restrict it to a nonzero finite-dimensional joint corner, take an eigenvector there, and use simplicity on the kernel of the endomorphism minus that eigenvalue. For \(GL_n\), the enveloping center commutes with the compact action as well as the Lie and finite-place actions; its elements therefore act by scalars. Compact components also fix that center, since their actions are inner on each factor of the complexified general linear Lie algebra. Thus every finite vector is enveloping-center finite.

Lemma 1.10 gives its smooth representative and moderate growth, including every derivative. The positive-central extension has polynomial height as well: \(\nu(g)\) and \(\nu(g)^{-1}\) are bounded by powers of \(\mathcal H(g)\), so \(\mathcal H(a_{\nu(g)}^{-1}g)\) is polynomially bounded in \(\mathcal H(g)\); the factor \(\nu(g)^{i\tau}\) has modulus one. The distributional constant terms defining the Hilbert cusp space now coincide with smooth compact-domain averages. They vanish everywhere. Hence the finite vectors are automorphic cusp forms. The reverse inclusion in (1.15) follows immediately from the finite-level and compact-finiteness requirements in the definition of an automorphic form. Density is Lemma 1.9.

At fixed finite level the topology (1.11) is complete, smooth and of moderate growth, as proved after Lemma 1.9. Lemma 1.10 makes its function-space inclusion continuous in every compact derivative seminorm. Compact averaging and Lie differentiation are continuous. Its mixed finite core is \(\pi\). These are precisely the required realization properties. \(\square\)

**Lemma 1.12 (factorization of an invariant positive form).** Suppose \(S,T\) are simple admissible modules for algebras \(A,B\) with directed self-adjoint local units, and \(S\otimes T\) has a positive Hermitian form satisfying

\[
\langle av,w\rangle=\langle v,a^*w\rangle,
\qquad
\langle bv,w\rangle=\langle v,b^*w\rangle.
\]

Then the form is a product \(h_S\otimes h_T\) of positive invariant forms. These factors are unique up to multiplying one by a positive scalar and the other by its inverse.

**Proof.** Fix \(0\ne t_0\in T\), and set \(h_S(s,s')=\langle s\otimes t_0,s'\otimes t_0\rangle\). It is positive and invariant. For arbitrary \(t,t'\), consider \(b_{t,t'}(s,s')=\langle s\otimes t,s'\otimes t'\rangle\). If a self-adjoint unit \(e\) fixes \(s\), invariance gives \(b_{t,t'}(s,z)=b_{t,t'}(s,ez)\). Finite-dimensional Riesz representation on \(eS\) therefore gives a vector \(Ts\in eS\) with

\[
b_{t,t'}(s,z)=h_S(Ts,z)\quad(z\in S).
\]

Larger units give the same vector, since the positive form separates vectors. Thus \(T\) is a well-defined linear operator on \(S\). Invariance of both forms gives \(Ta=aT\). The finite-corner Schur lemma proved in *Restricted tensor products and the tensor product theorem*, Lemma 3.2 implies \(T\) is scalar. Choose \(s_0\) of \(h_S\)-norm one and put \(h_T(t,t')=\langle s_0\otimes t,s_0\otimes t'\rangle\). The scalar just obtained is \(h_T(t,t')\), proving the product identity. Positivity and \(B\)-invariance follow from this formula. Comparing with any other product form on nonzero fixed vectors proves the claimed scalar freedom. \(\square\)

**Theorem 1.13 (unitary restricted tensor realization and local pairings).** In the situation of Theorem 1.11, take the algebraic restricted factorization proved in *Automorphic representations and automorphic L-functions*, Theorem 1.1. There are positive invariant local Hermitian forms \(h_v\), local irreducible unitary Hilbert representations \(H_v\) with finite cores \(\pi_v\), and spherical reference vectors \(\xi_v\) of norm one outside a finite set, such that

\[
H\simeq\widehat{\bigotimes_v'}(H_v,\xi_v),
\qquad
\left\langle\bigotimes_v x_v,\bigotimes_v y_v\right\rangle_H
=\prod_v h_v(x_v,y_v).
\tag{1.16}
\]

The Hilbert isomorphism integrates the actual full adelic action. The local contragredient finite core is the conjugate core through \(\overline y\mapsto[x\mapsto h_v(x,y)]\). In the automorphic realization, if \(\phi_x,\phi_y\) are the pure tensor cusp forms corresponding to \(x,y\), then

\[
c(g)=\int_X\phi_x(ug)\overline{\phi_y(u)}\,du
=\prod_v h_v(\pi_v(g_v)x_v,y_v),
\qquad |c(g)|\le\|x\|\|y\|.
\tag{1.17}
\]

Thus the bilinear automorphic pairing with the dual cusp form \(\widetilde\phi_y=\overline{\phi_y}\) is exactly the product of local dual pairings. Neither local Whittaker uniqueness nor any standard or Rankin–Selberg analytic theorem is used.

**Proof.** The global Hilbert form is invariant for the convolution involution at finite places, for compact distributions, and for \(X^*=-X\) on real Lie generators. The compact-open and compact-type local units are self-adjoint orthogonal projections. The algebraic local modules are simple admissible modules by the already proved factorization theorem. Apply Lemma 1.12 at each finite tensor stage.

Here is a compatible normalization, avoiding an infinite product of arbitrary constants. Choose a nonzero vector \(\xi_v\) in every local factor, using the specified fixed reference line at all but finitely many places, and let \(x_0=\bigotimes_v\xi_v\). Put \(C=\|x_0\|^2>0\). Define the form in factor \(v\) by replacing just that factor in \(x_0\) and dividing the resulting form by \(C\). It gives \(\xi_v\) norm one. Lemma 1.12 on a finite stage shows that its global form is \(C\) times the product of these normalized local forms: evaluate at its reference tensor to determine the one remaining scalar. The forms obtained at different stages agree, since their definitions use the same fixed \(x_0\). Absorb \(C\) into the form at one infinite place. Now (1.16)'s product identity holds on the whole algebraic restricted tensor product, and every tail reference vector still has norm one. Its finite-stage embeddings are isometric. Completing gives an isometry onto \(H\), since the finite core is dense.

We must show that the forms give actual unitary local groups also at infinity. Regroup the algebraic core as \(S\otimes T=\pi_v\otimes\pi^v\) and its form as \(h_v\otimes h^v\). For a nonzero finite tensor \(t\in T\), the operator

\[
P_t(s\otimes z)=s\otimes
\frac{h^v(z,t)}{h^v(t,t)}t
\]

is an orthogonal projection of norm one for the product form, so it extends to \(H\). It preserves the mixed core and commutes there with every local Lie operator and local compact operation at \(v\), and with every finite-place group element when \(v\) is finite. Lemma 1.9's common operator core and the one-parameter commutation argument extend the infinitesimal commutation at infinity to the actual \(G(F_v)\)-action. Thus \(P_tH\) is a reducing local Hilbert subspace. Its identification with the completion of \(\pi_v\), with the harmless fixed factor \(\|t\|\), defines \(H_v\) and its full unitary local action.

Its finite core is exactly \(\pi_v\). A local compact-open fixed vector at a finite \(v\), or a local compact-finite vector at an infinite \(v\), combined with the fixed other-place tensor \(t\), is a global mixed finite vector: the other components of \(t\) already have finite level and finite compact type. It therefore belongs to the global core, and hence to \(\pi_v\otimes\mathbb Ct\). Conversely all vectors of that local core have the required properties. They are dense by compact averaging. A nonzero closed local invariant subspace contains a nonzero such vector; simplicity of \(\pi_v\) forces it to contain the whole core, and density forces it to be \(H_v\). This proves local irreducibility and admissibility. The operator-core proof of Lemma 1.9 applies to this local representation with its local compact projectors, so \(\pi_v\) is a core for every local real Lie generator.

The full tensor action equals the given global action. At a finite place this already holds on the invariant algebraic core and extends by continuity. At infinity the two actions have the same Lie generators on the core, and this core is a common generator core on both sides. For the tensor side, approximate in the other Hilbert factors by finite-dimensional orthogonal projections and in the active factor by its generator core; this approximates both the vector and its derivative in graph norm. Closed generators therefore agree under the isometry. Their one-parameter groups agree by the differentiated identity used in Lemma 1.9, and compact components agree on the core. This proves full adelic equivariance. The restricted tensor action is strongly continuous because the compact tail fixes every pure reference-tail tensor, while only finitely many active local factors remain; density and unitarity extend continuity to the completion.

For a local finite vector \(y\), the functional \(x\mapsto h_v(x,y)\) has finite compact support: a self-adjoint finite compact projector fixing \(y\) can be transferred to \(x\). Conversely every functional in the restricted compact-finite dual is supported on one finite-dimensional admissible corner, where Riesz representation supplies such a \(y\). This identifies the conjugate core with the contragredient core. The group identity \(h_v(x,\pi_v(g)y)=h_v(\pi_v(g^{-1})x,y)\) proves equivariance. Complex conjugation of the automorphic functions supplies the dual central character and realizes this dual pairing as the integral in (1.17). That integral is absolutely convergent by Cauchy–Schwarz. The tensor isometry gives its product identity; outside a finite set \(g_v\in K_v\) and both vectors equal the unit \(\xi_v\), so every omitted factor is exactly one. Cauchy–Schwarz and unitarity give the stated uniform bound. \(\square\)

**Proposition 1.14 (reverse comparison under square integrability).** Let \(\pi\) be an irreducible admissible cuspidal submodule of automorphic forms with unitary central character. Suppose that every \(R(D)\phi\), for \(\phi\in\pi\) and every real Lie word \(D\), belongs to \(L^2(X)\). Then its closure in \(L^2(X)\) is an irreducible unitary cuspidal Hilbert constituent, its mixed finite core is exactly \(\pi\), and Theorem 1.13 applies to it.

**Proof.** The functions and their derivatives define real-smooth Hilbert vectors. For a real generator \(X\), the pointwise fundamental theorem of calculus gives

\[
R(\exp(tX))\phi-\phi=\int_0^t R(\exp(sX))R(X)\phi\,ds.
\]

The right side is an \(L^2\) integral. Strong continuity makes its norm derivative at zero equal to \(R(X)\phi\). Repeating with all Lie words and using coordinate products of exponentials proves Hilbert smoothness. Thus the restricted integral form is positive and infinitesimally invariant.

We give the integration argument rather than assume that the algebraic module is already invariant under arbitrary real translates. On the real Lie algebra of the product of general linear groups, take the Cartan involution \(\theta X=-X^*\) and the invariant real trace form, scaled on each factor so that it is negative on \(\mathfrak k\) and positive on \(\mathfrak p\). Let \(K_i,P_j\) be corresponding orthonormal bases. The element

\[
\Omega=\sum_j P_j^2-\sum_i K_i^2
\]

is central: invariance of the trace form makes the commutator with its dual-basis quadratic sum zero. The finite-corner Schur argument makes it scalar \(\lambda\) on \(\pi\). Infinitesimal unitarity makes \(\lambda\) real and gives

\[
\sum_j\|P_jw\|^2+\sum_i\|K_iw\|^2
=-\lambda\|w\|^2+2\sum_i\|K_iw\|^2.
\tag{1.18}
\]

Fix a finite compact-orbit space \(E\) containing \(w\). The vectors obtained by Lie words of length at most \(r\) are a compact-equivariant image of
\((\mathbb C\oplus\mathfrak g)^{\otimes r}\otimes E\). On that finite-dimensional compact tensor representation, the norm of any \(K_i\) is at most \(rM+M_E\), by the tensor derivative formula. This remains a bound on its image: compact unitarity makes each \(K_i\) normal, and its eigenvalues on a quotient are among those on the tensor representation. Equation (1.18) therefore bounds the norm of every real generator on such an image by \(C(r+1+M_E)\).

Iteration, followed by expansion of a fixed \(X\) in the chosen basis, yields

\[
\|R(X)^rw\|\le C_w A_X^r r!\,r^{b_w}.
\]

The constant \(A_X\) is independent of the initial compact packet: \(\prod_{j=1}^r(j+c)/r!\le e^c r^c\), so its size affects only \(C_w,b_w\). Taylor's integral remainder for the actual unitary one-parameter group is bounded by \(|t|^r\|R(X)^rw\|/r!\). For \(|t|A_X<1\), its Lie-polynomial partial sums therefore converge to \(R(\exp(tX))w\). All those sums lie in \(\pi\). The common radius and density prove that the Hilbert closure is invariant under these near-identity exponentials, hence all exponentials. Compact components and finite adelic translations already preserve \(\pi\), so its closure is fully invariant.

Each joint compact corner of this closure is the closure of the corresponding corner of \(\pi\). The latter is finite dimensional by admissibility, so it is already closed. Thus the closure is admissible and its finite core equals \(\pi\). Any nonzero closed invariant subspace contains a nonzero finite vector by compact averaging; irreducibility of \(\pi\) and density make that subspace the whole closure. The closure remains cuspidal by Lemma 1.8. This proves every assertion. \(\square\)

**Lemma 1.15 (smoothing before unitarity).** Let an irreducible admissible cuspidal mixed module \(\pi\) with unitary central character be embedded in a full \(G(\mathbb A)\)-invariant space \(V\) of smooth, finite-level, moderate-growth cuspidal functions. Assume that each fixed-finite-level space of \(V\) is complete Fréchet, that the right action is continuous and smooth at infinity, that its inclusion in \(C^\infty_{\mathrm{loc}}\) is continuous, and that its mixed finite core is exactly \(\pi\). No Hilbert norm is assumed. Every \(\phi\in\pi\) is reproduced by a smooth compactly supported convolution kernel. All its right derivatives have a common polynomial growth exponent. Consequently the rapid-decay argument in Lemma 1.1b applies with its Hilbert assumption replaced by these hypotheses. In conjunction with the adelic reduction Proposition 1.1a, it gives the square-integrability hypothesis of Proposition 1.14, and hence the compatible unitary realization and product pairings of Theorem 1.13.

**Proof.** Choose a finite compact-type packet and finite-place level containing \(\phi\), and let \(P\) be their averaging projector. Then \(E=PV\) is precisely the corresponding joint corner of \(\pi\), so it is finite dimensional. Take a smooth real approximate identity, with a fixed finite-place compact-open average small enough to fix \(E\). Convolution tends to the identity on each vector of \(E\) by continuity of the action. Hence

\[
T_\epsilon=P R(h_\epsilon)P|_E\longrightarrow I_E
\]

in any finite-dimensional operator norm. It is eventually invertible. If \(p(z)\) is its characteristic polynomial, then \(p(0)\ne0\) and \(p(T_\epsilon)=0\) expresses \(I_E\) as a polynomial in \(T_\epsilon\) having zero constant term. The compact projectors are compactly supported distributions, real convolution with \(h_\epsilon\) makes their product kernel smooth, and its positive convolution powers are again smooth and compactly supported. Their indicated linear combination supplies a kernel \(f\) with

\[
\phi(g)=R(f)\phi(g)=\int_{G^1}\phi(h)f(g^{-1}h)\,dh.
\tag{1.19}
\]

For derivatives in the positive central direction the asserted unitary character acts by a scalar, so it suffices to work on \(G^1\). Differentiation in (1.19) transfers every right derivative to a derivative of \(f\); all these kernels have a common compact support. If \(|\phi(g)|\le C\mathcal H(g)^q\), submultiplicativity of the matrix height on that compact support gives

\[
|R(D)\phi(g)|\le C_D\mathcal H(g)^q
\]

for every \(D\), with the same exponent \(q\). All differentiations and integrations are legitimate on compact sets by the stated smooth inclusion. Right differentiation preserves cuspidality because the unipotent averaging domains are compact.

The remaining proof of Lemma 1.1b uses only (1.19), this common exponent, vanishing constant terms, compact unipotent quotients, additive Poisson summation, and the lattice bounds; it uses no positive Hermitian form. The general reduction and Iwasawa density therefore make \(R(D)\phi\) square integrable for every \(D\). Apply Proposition 1.14. \(\square\)

Lemma 1.15 is a comparison route once \(V\) is given. The general construction in Theorem 1.19 below supplies an actual admissible smooth realization for every abstract cuspidal subquotient. Its proof treats the algebraic subquotient through the discrete Hilbert spectrum and a positive-central filtration; it does not assume that arbitrary real convolution preserves an algebraic mixed submodule.

The complete general comparison is stated in [Getz–Hahn, freely accessible author draft of 22 April 2022, Theorem 6.5.1, printed page 150/PDF page 166, and §9.7, printed pages 233–236/PDF pages 249–252](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf). The free account of unitary tensor products and cusp spaces is [Goldfeld–Jacquet, *Automorphic representations and L-functions for GL(n)*, §4, printed/PDF pages 19–21, and §8, printed/PDF pages 31–39](https://www.math.columbia.edu/~goldfeld/LanglandsBookChapter.pdf). Theorem 1.19 now supplies the general comparison, with its analytic and spectral steps proved below.


### The general cuspidal realization

Let \(F\) be a number field, \(d=[F:\mathbb Q]\), \(G=GL_n\), \(\nu=|\det|_{\mathbb A}\), \(G^1=\ker\nu\), and \(X=G(F)\backslash G^1\). We use the quotient measure, closed cuspidal Hilbert space, positive-central splitting and matrix height \(\mathcal H\) already constructed in *L-functions for GL_n: Godement–Jacquet and Rankin–Selberg*, Lemmas 1.8–1.10. The general covering in Proposition 1.1a is
\[
S=\Omega_N A(c)\Omega_TK,\qquad G^1=G(F)S,
\]
where \(b=\operatorname{diag}(b_i)\in A(c)\) has the same positive entries at every infinite place, finite entries one, \(\prod b_i=1\), and \(\rho_i=b_i/b_{i+1}\ge c>0\). Decrease \(c\) if needed so \(c\le1\). Each diagonal entry of \(\Omega_T\) has idèle norm one. Write
\[
B(b)=\max\left(1,\beta(b)\right),\qquad
\beta(b)=\prod_{i=1}^{n-1}\rho_i^d .
\]
The already proved covering also gives \(\mathcal H(b)\le C B(b)^a\) for a fixed \(a\), and finite quotient volume. We treat \(n\ge2\) first.

On \(\mathfrak g_\infty^1\), restrict the invariant real trace form with weights one at real places and two at complex places. The omitted positive scalar direction is its orthogonal complement, so this restriction is nondegenerate. The Cartan involution is \(X\mapsto-X^*\). Choose orthonormal bases \(K_j\) of its negative compact part and \(P_j\) of its positive part. Put
\[
\Omega=\sum_jP_j^2-\sum_jK_j^2,\qquad
C_K=-\sum_jK_j^2,\qquad
L=-\sum_jP_j^2-\sum_jK_j^2=-\Omega+2C_K .
\tag{1.23a}
\]
Invariance of the trace form proves that \(\Omega\) is central, by commuting a generator with the dual-basis quadratic sum. The operator \(L\) is elliptic on the real group: its principal symbol is the sum of squares of a real tangent frame. The scalar \(C_K\) on an irreducible compact type \(\sigma\) will be denoted \(c_\sigma\ge0\). Scalarity follows from compact Schur; nonnegativity follows by integration of the squares.

**Lemma 1.19a (the local estimates used below).** On fixed relatively compact nested real coordinate boxes, a smooth solution of a scalar elliptic differential equation \(Pu=0\), of order \(2r\) with principal symbol whose modulus is bounded below by a positive multiple of \(|\xi|^{2r}\), satisfies
\[
\|u\|_{C^j(B_0)}\le C_j\|u\|_{L^2(B_1)}
\tag{1.23b}
\]
for every \(j\), where \(B_0\Subset B_1\). For a second-order smooth operator with positive real principal quadratic form, an \(L^2_{\rm loc}\) distributional eigenfunction is smooth. These assertions apply to \(L\) and its polynomials on a fixed group chart. Left-translating the chart leaves their constants unchanged.

*Proof.* Here are the Fourier estimates and the regularity argument. Define the integer Sobolev norms by the Fourier weight \((1+|\xi|^2)^{s/2}\), after inserting a compact coordinate cutoff. For a constant principal operator \(P_0\), ellipticity gives
\[
\|v\|_{H^{s+2r}}\le C\bigl(\|P_0v\|_{H^s}+\|v\|_2\bigr).
\]
This is the pointwise inequality between its Fourier symbol and the displayed weights, integrated against \(|\widehat v|^2\). On a sufficiently small box freeze the highest coefficients at its centre. The difference of the highest coefficients contributes at most
\(\epsilon C\|v\|_{H^{s+2r}}\); differentiating a coefficient, and every lower-order term, contributes at most \(C_s\|v\|_{H^{s+2r-1}}\). The elementary Fourier inequality
\[
\|v\|_{H^{k-1}}\le\eta\|v\|_{H^k}+C_{k,\eta}\|v\|_2
\]
follows by splitting \(|\xi|\) below and above a sufficiently large threshold. Absorb the first term with \(\epsilon,\eta\) small. For compactly supported \(v\) in that box we obtain
\[
\|v\|_{H^{s+2r}}\le C_s\bigl(\|Pv\|_{H^s}+\|v\|_2\bigr).
\tag{1.23c}
\]
For a solution, apply this to \(\chi u\). The commutator \([P,\chi]\) has order at most \(2r-1\). On boxes \(B_t\Subset B_T\), choose cutoffs whose \(l\)-th derivatives are bounded by constants times \((T-t)^{-l}\). Apply the preceding interpolation to a second cutoff equal to one on the first one's support. For any chosen \(0<\theta<1\), (1.23c) gives
\[
\|u\|_{H^{s+2r}(B_t)}
\le\theta\|u\|_{H^{s+2r}(B_T)}
+C_{s,\theta}(T-t)^{-N_s}\|u\|_{L^2(B_T)} .
\]
There are only finitely many cutoff derivatives, so \(N_s\) is finite. Iterate on radii approaching a fixed larger box with gaps proportional to \(2^{-j}\), choosing \(\theta<2^{-N_s-1}\). The resulting geometric series converges; its last term tends to zero because the smooth function has a finite Sobolev norm on that fixed larger box. Thus all interior Sobolev norms are bounded by the larger-box \(L^2\) norm. Fourier Cauchy–Schwarz bounds \(C^j\) by \(H^s\) when \(s>j+\dim(B_1)/2\), proving (1.23b). A finite chart cover gives the same assertion without the small-box restriction.

For clarity, weak regularity does not require an assumed smooth representative. In divergence coordinates a second-order elliptic operator has leading term \(-\partial_i(a_{ij}\partial_j)\). Integration by parts and positivity give, for compactly supported smooth \(v\),
\[
\|v\|_{H^1}\le C\bigl(\|Pv\|_{H^{-1}}+\|v\|_2\bigr).
\]
Mollify a localized weak solution with kernels \(J_\epsilon\). The commutator \([P,J_\epsilon]\) maps \(L^2\) to \(H^{-1}\) with a bound independent of \(\epsilon\). To check this, the leading commutator is
\(-\partial_i([a_{ij},J_\epsilon]\partial_j u)\). Transfer the derivative of \(u\) to its integral kernel. The difference \(a(x)-a(y)\) is \(O(\epsilon)\) on that kernel's support, while a kernel derivative has \(L^1\) norm \(O(\epsilon^{-1})\); the remaining coefficient derivatives have bounded kernels. Thus the expression in parentheses is bounded in \(L^2\). Lower terms and cutoff commutators obey the same, or an easier, estimate. Young's inequality gives the asserted bounds directly. The displayed estimate makes the mollifications bounded in local \(H^1\); weak compactness and their \(L^2\) convergence give \(u\in H^1_{\rm loc}\).

Now \([P,J_\epsilon]\) maps \(H^1\) to \(L^2\) uniformly. In nondivergence form, transfer one of the two derivatives to the kernel: the same coefficient difference times a kernel derivative is bounded, and the remaining derivative of \(u\) is in \(L^2\). Estimate (1.23c) with \(s=0,r=1\), including a nested cutoff, gives local \(H^2\) bounds and hence \(H^2_{\rm loc}\) regularity. If \(u\in H^k_{\rm loc}\) satisfies \(Pu=\lambda u\), commute a derivative of order \(k-1\) with \(P\). Its commutator uses derivatives of \(u\) of order at most \(k\), already in \(L^2\). Applying the \(H^2\) result to that derivative gives \(H^{k+1}_{\rm loc}\). Induction and Fourier Cauchy–Schwarz prove smoothness. All coefficient bounds are fixed in a left-translated group chart because the differential fields in (1.23a) are left invariant. \(\square\)

**Lemma 1.19b (rapid decay without a realization assumption).** Every moderate-growth, finite-level, compact-finite, enveloping-center-finite cusp function with unitary central character, restricted to \(G^1\), and every one of its right derivatives, satisfies
\[
|R(D)\phi(b\omega)|\le C_{D,M}B(b)^{-M}
\tag{1.23d}
\]
for every \(M\), with \(\omega\) in a fixed compact set and \(b\in A(c)\). Consequently every such derivative belongs to \(L^2(X)\).

*Proof.* Compact projection decomposes \(\phi\) into finitely many compact types. Enveloping-center finiteness supplies a nonzero polynomial \(p\) with \(p(\Omega)\phi=0\); a nonzero constant polynomial forces \(\phi=0\), so suppose its degree is positive. On type \(\sigma\) this becomes
\[
p(-L+2c_\sigma)\phi_\sigma=0 .
\]
This is an elliptic scalar equation with constant nonzero leading coefficient. Apply Lemma 1.19a on \(gB_1\). Moderate growth and \(\mathcal H(gh)\le C_{B_1}\mathcal H(g)\) give
\[
|R(D)\phi(g)|\le C_D\mathcal H(g)^q
\tag{1.23e}
\]
for every \(D\), with one exponent \(q\). The compact projections have preserved that exponent. This step takes place on the group and needs no injectivity radius in the quotient.

For a cut \(i\), the radical \(V_i\) of the maximal upper block parabolic is the *abelian* group of matrices with entries in rows \(r\le i\), columns \(s>i\). Put \(f_i(v)=R(D)\phi(vb\omega)\). Its average over \(V_i(F)\backslash V_i(\mathbb A)\) is zero. The finite components of \(b\) are one and \(\omega_f\) ranges in a compact set. Finite level therefore gives one compact open additive subgroup \(W_i\subset V_i(\mathbb A_f)\) that fixes every such \(f_i\): choose it so that \(\omega_f^{-1}W_i\omega_f\) lies in the fixed level throughout that compact family. Existence follows by a finite subcover of the continuous conjugation map near the identity.

Strong approximation and the lattice construction in *The adèle ring*, Theorems 2.2–2.3 identify the resulting quotient with \(V_i(F_\infty)/\Lambda_i\), where \(\Lambda_i=V_i(F)\cap W_i\) is a full real lattice. Indeed projection of strong approximation to the finite coordinates makes \(F\) dense in \(\mathbb A_f\), so every class has an infinite representative modulo \(F+W_i\). Its kernel is \(\Lambda_i\). A compact open \(W_i\) contains a product \(M\widehat{\mathcal O}_F\) and is contained in a product \(M^{-1}\widehat{\mathcal O}_F\) for some positive rational integer \(M\). Its rational intersection is therefore a full finite-index lattice between the corresponding Minkowski integer lattices. Compactness makes the resulting continuous torus bijection a homeomorphism. Its Fourier frequencies form a dual lattice, with a positive nonzero minimum and a summable \(\sum_{\lambda\ne0}|\lambda|^{-2r}\) for \(2r>\dim_\mathbb R V_i(F_\infty)\). These facts follow by an invertible lattice-basis change from the corresponding integer-lattice facts. Character completeness is *Matrix coefficients and the Peter–Weyl theorem*, Theorem 4.1; on a torus the characters are precisely the dual-lattice exponentials.

For an upper root \(E_{rs}\) in \(V_i\), \(b^{-1}E_{rs}b=(b_s/b_r)E_{rs}\), and
\[
b_r/b_s=\prod_{\ell=r}^{s-1}\rho_\ell\ge c^{n}\rho_i .
\]
Abelianity makes differentiation of \(f_i\) transfer to the constant right field \(\operatorname{Ad}(\omega^{-1}b^{-1})E_{rs}\). Its coefficients are \(O(\rho_i^{-1})\). Compact representatives of the torus and (1.23e) thus bound every \(2r\)-th derivative by \(C_{D,r}\rho_i^{-2r}B(b)^{aq}\). Integrating by parts in its Fourier coefficient extracts \((4\pi^2|\lambda|^2)^{-r}\). The zero coefficient is zero. Absolute summation gives
\[
|R(D)\phi(b\omega)|\le C_{D,r}\rho_i^{-2r}B(b)^{aq}.
\]
Choose a largest \(\rho_i\). It is at least \(\beta(b)^{1/(d(n-1))}\), and is bounded below independently of \(b\) even when \(\beta<1\). Increasing \(r\) proves (1.23d). All differentiations preserve cusp averages, whose domains are compact by *Automorphic representations and automorphic L-functions*, Lemma 1.0. The finite-volume Iwasawa density and covering then give square integrability, also after arbitrary polynomial height weights. No compact convolution was assumed to preserve an algebraic mixed submodule. \(\square\)

**Lemma 1.19c (finite intersection for the proved covering).** The set
\[
\{\gamma\in G(F):\gamma S\cap S\ne\varnothing\}
\]
is finite.

*Proof.* We give the flag and matrix argument; this assertion is not inferred just from a covering. For decomposable \(0\ne w\in\bigwedge^rF^n\), define \(h_g(w)\) as the product of the exterior Euclidean norms at infinity, squared at complex places, and the exterior coordinate maximum norms at finite places. It is invariant under rational rescaling. Let \(m_r(g)\) be its infimum over such \(w\), with \(m_0=1\). Rational left multiplication permutes this set, so \(m_r(\gamma g)=m_r(g)\).

For \(g=ubhk\in S\), \(b^{-1}ub\), \(h\), \(k\) and their inverses range in fixed compact sets. Indeed upper entries of the first factor are multiplied by \(b_j/b_i\le c^{-(j-i)}\). Thus \(g=b\omega\) with \(\omega\) in a fixed compact set. For any rational exterior vector, a nonzero rational coordinate and the product formula proved in *Places of number fields in extensions and the product formula*, Theorem 5.2 give \(h_1(w)\ge1\). The least exterior weight of \(b\) is at least a fixed multiple of \(\prod_{j=n-r+1}^n b_j\), because every \(\rho_i\ge c\). Compact exterior operator bounds therefore give
\[
C^{-1}\left(\prod_{j=n-r+1}^n b_j\right)^d
\le m_r(g)\le
\left(\prod_{j=n-r+1}^n b_j\right)^d .
\tag{1.23f}
\]
For the upper bound take the last \(r\) standard rows: upper unipotence fixes their exterior vector, \(k\) preserves the chosen local norms, and the product of the corresponding \(h_j\)-norms is one.

Suppose \(g'=\gamma g\), with \(g=ubhk\) and \(g'=u'b'h'k'\) in \(S\). Applying (1.23f) to every \(r\), and dividing adjacent last-row products, bounds all \(b'_j/b_j\) above and below by one fixed constant. The finite components of \(\gamma=g'g^{-1}\) lie in a fixed compact set, so its entries belong to one fixed fractional ideal of \(F\). The full Minkowski embedding of this ideal is a lattice, by *Lattices, Minkowski's theorem and the Minkowski embedding*, Proposition 7.2. A nonzero entry therefore has full infinite Euclidean norm at least \(\eta>0\).

At infinity write
\[
\gamma=u'b'Mb^{-1}u^{-1},\qquad M=h'k'k^{-1}h^{-1}.
\]
All entries of \(u,u^{-1},u',u'^{-1},M\) are uniformly bounded. If \(a>b\), the \((a,b)\)-entry of \(\gamma\) is a sum of terms indexed by \(r\ge a\), \(s\le b\), each bounded by a constant times \(b'_r/b_s\). For a cut \(\ell\) with \(b\le\ell<a\), this is at most \(C/\rho_\ell\). Take a fixed threshold \(T\) so large that the full infinite bound is less than \(\eta\) whenever \(\rho_\ell>T\). Rationality forces every entry below that cut to be zero.

Partition the indices into blocks at those large cuts. Then \(\gamma\), and hence \(M\), is block upper triangular. Diagonal \(h,h'\) preserve that condition, so \(k'k^{-1}\) is block upper triangular at every infinite place. A real orthogonal or complex unitary block upper triangular matrix is block diagonal: its last block row is orthogonal to all preceding rows, forcing the corresponding last block column to vanish above its diagonal; repeat on the preceding block. Thus \(M\) is block diagonal at infinity.

Inside each block the adjacent ratios are at most \(T\) and at least \(c\). Together with \(b'_j/b_j\) bounded, this bounds every entry of the block diagonal \(b'Mb^{-1}\). Consequently \(\gamma=u'(b'Mb^{-1})u^{-1}\) has uniformly bounded infinite entries. Its finite entries were already uniformly bounded. A compact adelic matrix set contains only finitely many rational matrices, by discreteness of \(F\) in the adèles proved in *The adèle ring*, Theorem 2.2. This proves finiteness.

In particular, Haar integration over \(S\) has bounded multiplicity over \(X\). If two lifts of a coset lie in \(S\), their ratio is one of this finite list; the number of lifts is therefore at most its cardinality. The Iwasawa parameterization only introduces its usual compact fibres of fixed Haar volume. Compact sets of torus representatives may be thickened within the compact norm-one torus coordinates when necessary. Hence, for nonnegative quotient functions \(f\),
\[
\int_{S}f(g)\,dg\le C_S\int_X f(x)\,dx .
\tag{1.23g}
\]
The same bound holds for the standard Iwasawa parameter integrals restricted to the compact factors of the covering.

We may also arrange that these parameter integrals dominate integration on the quotient when its representative is chosen in the original covering. Here is the compact-fibre detail. At infinity an upper triangular unitary matrix is diagonal, so the Iwasawa fibre changes only compact diagonal phases. At a finite place it changes the diagonal by units and the unipotent coordinate by a member of the integral unipotent group conjugated by the finite diagonal. The finite diagonal lies in the fixed compact \(\Omega_{T,f}\). Enlarge \(\Omega_T\) once by its compact diagonal phases and units, and enlarge \(\Omega_N\) once by the compact set of these conjugated integral unipotents. Then every full Iwasawa fibre over a point in the original covering is contained in the enlarged parameter set, with its probability Haar measure. These fibre changes preserve every \(b_i\) and \(\beta\). The enlarged compact factors still satisfy the finite-intersection proof. This gives both the domination needed for quotient tails and the upper bound (1.23g) for their parameter integrals. \(\square\)

**Lemma 1.19d (compact cusp form embedding).** Fix a finite level \(U\) and a unitary norm-one central character. On that entire closed cuspidal Hilbert space, the form
\[
q(u)=\sum_j\|R(P_j)u\|_2^2+\sum_j\|R(K_j)u\|_2^2
\tag{1.23h}
\]
is densely defined and closed. Its form-domain embedding into the Hilbert space is compact. The same holds after projection to a finite packet of compact types.

*Proof.* Derivatives mean domains of the actual closed right-translation generators. Their graph intersections make the form closed. Smooth real convolution approximates every vector and gives a dense domain; the kernels preserve finite level and the closed cusp space. For a form-domain vector it converges also in the form norm: differentiation under translation uses the continuously varying finite matrix \(\operatorname{Ad}(g^{-1})\), so its orbit is continuous in all first-derivative norms. The Cartan inner product is invariant under \(K_\infty\), so compact-type projection reduces this form; finite-level and central projections also do. Such projections can therefore be retained in this approximation whenever a compact packet is prescribed.

We prove the uniform tail estimate. For the maximal radical \(V_i\), write the full upper unipotent group \(N=V_i\rtimes N_i\), where \(N_i\) is block diagonal upper unipotent. Quotient integration is integration first over \(V_i(F)\backslash V_i(\mathbb A)\), then over \(N_i(F)\backslash N_i(\mathbb A)\). Choose compact representatives of the second quotient. Conjugation by \(N_i\) preserves additive Haar measure on \(V_i\), since it is triangular with diagonal entries one, so these fibre identifications preserve the probability measures.

At \(n_i b\omega\), the function \(v\mapsto u(vn_i b\omega)\) has zero average. The same uniform finite-level argument as in Lemma 1.19b gives a fixed real torus on which to apply the zero-mean Fourier Poincaré inequality
\[
\int |f|^2\le C\sum_\alpha\int|\partial_\alpha f|^2 .
\]
It follows by dividing nonzero Fourier coefficients by the positive minimum frequency norm; it holds for weak \(H^1\) functions by Fourier truncation. Conjugating a \(V_i\)-direction successively by \(n_i^{-1}\), \(b^{-1}\) and \(\omega^{-1}\) gives a right-field linear combination with coefficients \(O(\rho_i^{-1})\): the first conjugation stays in that radical and is bounded on the chosen compact representatives; all its roots cross cut \(i\). Hence
\[
\int_{N(F)\backslash N(\mathbb A)}|u(nb\omega)|^2\,dn
\le C\rho_i^{-2}
\int_{N(F)\backslash N(\mathbb A)}
\sum_X|R(X)u(nb\omega)|^2\,dn ,
\tag{1.23i}
\]
where \(X\) ranges over the full fixed real frame in (1.23h). This holds first for smooth vectors and then on the form domain by approximation. Distributional cuspidality gives the zero mean almost everywhere in these fibre integrals.

Partition the diagonal region according to a largest \(\rho_i\). Integrate (1.23i) against its Iwasawa density and the compact torus and compact-group factors. On \(\beta>R\), \(\rho_i^{-2}\le R^{-2/(d(n-1))}\). Let \(C_R\subset X\) be the image of the covering parameters with \(\beta\le R\); it is compact since all diagonal ratios and entries are then bounded. Every point outside \(C_R\) has a covering representative with \(\beta>R\). Bounded multiplicity (1.23g) gives
\[
\|u\|_{L^2(X\setminus C_R)}^2
\le C R^{-2/(d(n-1))}q(u).
\tag{1.23j}
\]

On a compact part of \(X\), a fixed finite level gives finitely many real coordinate charts with positive finite-fibre volume. Injective charts follow from the arithmetic chart construction in Lemma 1.10 of this lesson, or directly from discreteness on a compact group set. Their local \(H^1\) norms are bounded by \(\|u\|_2^2+q(u)\). Insert chart cutoffs and expand on fixed boxes in Fourier series. The bound controls the sum of squared coefficients weighted by \(1+|k|^2\); the \(L^2\) tail beyond \(|k|>A\) is \(O(A^{-2})\). The finitely many remaining coefficients have convergent subsequences. A finite chart cover and then (1.23j) prove precompactness globally.

For completeness, only finitely many real quotient components occur at fixed \(U\): the finite part of the proved covering is compact and has finitely many cosets modulo \(U\). Each component is a quotient of \(G_\infty^1\) by a discrete group. Its discreteness follows because a compact real set times its fixed compact finite stabilizer meets \(G(F)\) only finitely. Thus the real charts just used are genuine group-quotient charts. No cusp compactness or finite-intersection statement was assumed. \(\square\)

**Lemma 1.19e (finite-dimensional cusp spaces).** Fix \(U\), finitely many compact types, a unitary norm-one central character, and a nonzero polynomial \(p\). The space of smooth moderate-growth cusp functions on \(X\) satisfying
\[
p(\Omega)\phi=0
\tag{1.23k}
\]
with those level and compact-type constraints is finite dimensional. In particular the fixed-level, fixed-compact-type, fixed-cofinite-infinitesimal-character space is finite dimensional.

*Proof.* Lemma 1.19b applies using just (1.23k), so all these functions and their derivatives lie in \(L^2\). On a single compact type, use the closed form in Lemma 1.19d. For \(f\) in its Hilbert space, the complete form norm gives a unique \(Tf\) with
\[
q(Tf,v)+\langle Tf,v\rangle=\langle f,v\rangle .
\]
The representing-vector assertion follows directly from the Hilbert projection argument: minimize the distance from a vector outside a bounded functional's closed kernel; the parallelogram identity makes a minimizing sequence Cauchy, and the closest-point difference is orthogonal to the kernel and represents the functional after scaling.

Thus \(T\) maps a Hilbert unit ball into a bounded form ball. It is compact by Lemma 1.19d, self-adjoint by the displayed identity, positive, injective and has dense range; injectivity follows from density of the form domain. The compact self-adjoint argument gives an orthonormal eigenbasis with positive eigenvalues tending to zero and finite multiplicities. To recall its mechanism, a bounded maximizing sequence has a weakly convergent subsequence: diagonalize its coefficients in a countable orthonormal basis, use Bessel's inequality for the limit, and approximate each test vector by its finite coefficient sums. Compactness then makes its images converge in norm, so a maximal positive Rayleigh value is attained. Varying the vector proves its eigenvector equation. Restrict to its orthogonal complement and repeat. An infinite orthogonal family whose eigenvalues stay away from zero contradicts compactness; a remaining orthogonal complement has zero operator and is zero by injectivity. This also proves finite multiplicities.

Define \(L=T^{-1}-1\). Its eigenvalues \(\kappa\ge0\) tend to infinity. It is the weak differential operator in (1.23a). Indeed start with the same derivative form on the whole ambient \(L^2(X)\). The closed cusp projection commutes with every right group action and hence with its generators. Finite-level projection has the same property for the real generators. Compact and central projections reduce the form because it is invariant under those compact groups. The Riesz resolvent therefore reduces to the just constructed restricted resolvent. Its equation against unrestricted compact coordinate tests is exactly the distributional differential equation for \(L\).

A function in (1.23k) has all Lie derivatives in \(L^2\). The pointwise fundamental theorem of calculus and strong right continuity identify them with its Hilbert derivatives, as in Proposition 1.14 of this lesson. Skew-adjoint generator identities then give
\[
q(\phi,v)=\left\langle-\sum_XR(X)^2\phi,v\right\rangle
\]
for every form-domain \(v\); the identity extends from smooth vectors by form approximation. Hence \(\phi\) belongs to the operator domain, and repeating gives every power of \(L\). On type \(\sigma\), \(\Omega=-L+2c_\sigma\). Its expansion in the eigenbasis of \(L\) can therefore involve only eigenvalues solving \(p(-\kappa+2c_\sigma)=0\). There are finitely many roots and each eigenspace is finite dimensional. Sum over the finite compact packet.

Finally a cofinite ideal in the enveloping centre supplies a nonzero polynomial in \(\Omega\), because its powers are linearly dependent modulo that ideal. This proves the last assertion. Notice that the whole cusp space at a fixed compact type was not asserted to be finite dimensional. \(\square\)

**Corollary 1.19f (reproducing kernels for algebraic cusp forms).** Every automorphic cusp form is reproduced by a smooth compactly supported convolution kernel on the central-normalized group.

*Proof.* For a fixed positive-central character, its central-normalized restriction, annihilating polynomial \(p(\Omega)\), finite level, compact packet and norm-one central character put it in the finite-dimensional actual function space \(E\) of Lemma 1.19e. For a general central-finite form use all the finitely many coefficient functions in its positive-central exponential-polynomial expansion (1.23m), and all its finitely many norm-one characters; their construction is proved below and does not use this corollary. Choose the finite direct sum of constrained spaces containing those coefficients as \(E\). Smooth compact real convolution, and a fixed finite compact-open average, preserve \(p(\Omega)\) and each norm-one central character. The polynomial is preserved because the general linear adjoint action fixes the centre of the complexified enveloping algebra. Convolution preserves moderate growth and cuspidality. Applying the compact packet projector \(P\) makes
\[
T_\epsilon=P R(h_\epsilon)P
\]
an operator on \(E\), converging to the identity there. These facts concern the entire *proved finite-dimensional constrained function space*, not an assumed real-group-invariant algebraic mixed submodule.

Invertibility for small \(\epsilon\), followed by the characteristic-polynomial identity, writes the identity on \(E\) as a polynomial in \(T_\epsilon\) with zero constant term. Compact projectors are compactly supported distributions; convolution with the smooth \(h_\epsilon\) and all its positive convolution powers are smooth and compactly supported. Their linear combination is the required reproducing kernel. Since its action on \(G^1\) fixes every coefficient in (1.23m), it fixes the original form on all positive-central translates as well. \(\square\)

**Lemma 1.19g (compact cuspidal convolution and discrete spectrum).** Every smooth compactly supported convolution on a fixed norm-one central-character cuspidal Hilbert space is compact. This space is a Hilbert direct sum of irreducible unitary representations, each with finite multiplicity.

*Proof.* A finite-place smooth compact kernel is bi-invariant under some compact open \(U\); this follows by covering its compact finite support by finitely many locally constant coordinate neighbourhoods. Its operator has image in that \(U\)-level. Derivatives transfer to its smooth compact kernel, so Young's inequality gives
\[
\|R(X)R(f)u\|_2\le C_{f,X}\|u\|_2 .
\]
Its unit-ball image is bounded in the form domain of Lemma 1.19d, which was proved for the whole \(U\)-level, with no compact-type restriction. The operator is therefore compact. This does not assert finite dimensionality of that level.

Here is the representation decomposition argument; no type-I theorem is needed. Smooth compact approximate identities \(h_j\) tend strongly to the identity by strong continuity. The operators \(T_j=R(h_j)^*R(h_j)\) are positive compact and also tend strongly to the identity. On a nonzero closed invariant subspace \(W\), some \(T_j\) is nonzero and has a positive finite-dimensional eigenspace \(E\subset W\). Every invariant orthogonal projection commutes with \(T_j\). Among invariant subspaces of \(W\) meeting \(E\), choose one \(V\) minimizing the positive integer \(\dim(E\cap V)\), and replace it by the closed group span of that intersection; the dimension is unchanged.

If \(V\) had a proper nonzero invariant subspace, its orthogonal decomposition would split \(E\cap V\). Two nonzero parts contradict minimality. A zero part forces the corresponding subspace to be zero, because \(V\) is generated by \(E\cap V\). Thus \(V\) is irreducible. A maximal orthogonal family of these irreducible subspaces exhausts the Hilbert space: any nonzero orthogonal complement has the same construction. The Hilbert space is separable, from its countable quotient charts, so the family is countable.

For an irreducible representation that occurs, choose a \(T_j\) nonzero on it and a positive eigenvalue there. Every equivalent copy has that same eigenvalue. Infinitely many copies would give an infinite-dimensional eigenspace of the compact global \(T_j\), which is impossible. This proves finite multiplicity. \(\square\)

**Lemma 1.19h (admissibility of the cuspidal Hilbert constituents).** Every irreducible Hilbert constituent just obtained has finite joint level-and-compact-type corners. Its mixed finite core is an irreducible admissible module of actual cusp forms.

*Proof.* Let \(H_i\) be a constituent. Compact averaging and finite-place averaging give a nonzero vector in some \(U\)-level and compact type \(\sigma\). Projection onto \(H_i\) commutes with the closed real generators and reduces their form, and commutes with the compact and finite projections. Thus the compact resolvent constructed in Lemma 1.19e restricts to this nonzero corner. It has an eigenvector \(u\ne0\) there. The ambient weak equation is \(Lu=\kappa u\), as proved there. Lemma 1.19a supplies a smooth representative. On type \(\sigma\), this gives \(\Omega u=\lambda u\), where \(\lambda=2c_\sigma-\kappa\) is real.

We establish the global derivative estimates needed to integrate its algebraic span. A fixed finite level has finitely many real group-quotient components. Give them the complete metric whose orthonormal fields are the frame in (1.23a). Completeness and proper distance balls can be seen directly: a path of length \(R\) bounds a matrix and its inverse by \(e^{CR}\), by the differential equation \(g'=gX\). Bounded closed real matrix sets are compact. Paths lift to the group quotient, so quotient distance balls are compact images of such balls. Lipschitz cutoffs \(\eta_R\), equal to one on larger balls, can therefore be chosen with compact support and \(\sum_X|X\eta_R|^2\le C/R^2\). Lipschitz cutoffs are legitimate weak energy tests by local mollification.

For any \(L^2\) smooth compact-finite distributional \(\Omega\)-eigenvector \(v\), project to its finitely many compact types. On each type it satisfies \(Lv_\sigma=(2c_\sigma-\lambda)v_\sigma\). Test this equation against \(\eta_R^2v_\sigma\). Integration by parts and \(2ab\le a^2/2+2b^2\) bound
\[
\int\eta_R^2\sum_X|R(X)v_\sigma|^2
\le 2|2c_\sigma-\lambda|\|v_\sigma\|_2^2+
\frac{C}{R^2}\|v_\sigma\|_2^2 .
\]
Letting \(R\) increase proves that every first derivative is in \(L^2\). Its right derivatives still satisfy the same \(\Omega\)-eigen-equation, and their compact packets are contained in the original packet tensored with the finite adjoint representation. Repeat the argument to prove all word derivatives belong to \(L^2\). The fundamental theorem of calculus identifies these with Hilbert derivatives. In particular the quotient Sobolev bound in Lemma 1.10 of this lesson gives polynomial growth of every derivative.

Let \(M\) be the mixed algebraic module generated by \(u\). It is made of smooth moderate-growth cusp functions with \(\Omega=\lambda\). Lemma 1.19e shows every joint corner of \(M\) is finite dimensional. The algebraic span is thus admissible, without assuming it is already simple.

Its Hilbert closure is invariant under the real group. We recall the uniform-radius argument to make this step explicit. For its finite vectors,
\[
\sum_j\|P_jw\|^2+\sum_j\|K_jw\|^2
=-\lambda\|w\|^2+2\sum_j\|K_jw\|^2 .
\]
A Lie word of length at most \(r\) from a compact-orbit space \(E\) has compact representation contained in the image of
\((\mathbb C\oplus\mathfrak g)^{\otimes r}\otimes E\). Norms of compact generators there are at most \(rA+A_E\). This follows from the tensor derivative formula; on a quotient their eigenvalues are a subset, and compact unitarity identifies operator norms with maximal eigenvalue moduli. The displayed energy identity bounds every real generator on that image by \(C(r+1+A_E)\). Iteration gives
\[
\|R(Y)^rw\|\le C_w A_Y^r r!\,r^{b_w},
\]
where \(A_Y\) is independent of the starting compact packet: use
\(\prod_{j=1}^r(1+a/j)\le e^a r^a\).
Taylor's integral remainder for the actual unitary one-parameter group is bounded by \(|t|^r\|R(Y)^rw\|/r!\). On a common neighbourhood it therefore converges to its Lie-polynomial series in \(M\). Density then makes \(\overline M\) invariant under these exponentials, hence the whole connected real group. Compact components meet every real component of \(GL_n\), and the finite adelic action already preserves \(M\). Thus \(\overline M\) is fully invariant. Irreducibility of \(H_i\) gives \(\overline M=H_i\).

For each joint compact projector \(e\), \(eM\) is finite dimensional by Lemma 1.19e, hence closed. Projecting the dense \(M\) gives \(eH_i=eM\). All joint corners of \(H_i\) are consequently finite dimensional and its mixed finite core is \(M\). The actual-Hilbert comparison in *L-functions for GL_n: Godement–Jacquet and Rankin–Selberg*, Theorem 1.11 now applies and makes this core simple and enveloping-center finite, as well as an actual cusp module. There is no reliance on an admissibility theorem for arbitrary local unitary representations. \(\square\)

**Theorem 1.19 (every abstract cuspidal representation has an actual realization).** Every irreducible admissible cuspidal automorphic subquotient for \(GL_n/F\) is isomorphic to an embedded smooth cusp module. After removal of the real positive-central norm exponent it is the mixed finite core of an actual irreducible admissible cuspidal Hilbert constituent. Its finite-level complete smooth realization and compatible unitary local tensor pairings are those constructed in Theorems 1.11 and 1.13 of this lesson. This holds for every number field and every \(n\ge1\).

*Proof.* First fix a unitary norm-one central character and trivial positive-central action. Let \(\mathcal C_\omega\) be the algebraic space of cusp forms with these data. Lemma 1.19b places every vector and all its derivatives in the closed Hilbert cusp space. Lemma 1.19g decomposes that Hilbert space, with finite multiplicities, into \(H_i\). Lemma 1.19h and the actual-Hilbert comparison put every \(H_{i,\mathrm{fin}}\) in \(\mathcal C_\omega\).

Conversely take \(\phi\in\mathcal C_\omega\), fixed by \(U\), in a finite compact packet, and killed by \(p(\Omega)\). Orthogonal constituent projections commute with real generators and their domains, since the constituents reduce the full unitary action. They therefore retain those three constraints. Every nonzero projected vector is a finite vector of its admissible constituent and hence an actual automorphic cusp form. All these vectors are pairwise orthogonal and lie in the finite-dimensional constrained space of Lemma 1.19e. Only finitely many can be nonzero. Consequently
\[
\mathcal C_\omega=\bigoplus_i H_{i,\mathrm{fin}}
\tag{1.23l}
\]
as an *algebraic* direct sum of simple admissible mixed modules.

We now justify the passage from general algebraic subquotients, including nonunitary positive-central exponents and possible central Jordan blocks. Let \(H_0\) denote differentiation of the positive splitting \(a_{e^t}\). It is a central Lie operator. Every automorphic form has a finite-dimensional orbit under the real central Lie algebra, because that algebra lies in the enveloping centre. Solving its constant-coefficient ordinary differential equations gives the actual matrix-exponential central translations on this finite-dimensional orbit. Thus every algebraic mixed submodule is preserved by those translations; they are not being assumed to extend a noncentral real action.

The norm-one scalar idèle-class group is compact, by *Idèles and the idèle class group*, Theorem 3.3. Its orbit on any given finite-level, central-finite automorphic form is finite dimensional. To see this explicitly, let \(W\) be its finite-dimensional real-central Lie orbit. The connected archimedean scalar group acts on \(W\) by those matrix exponentials. Scalar finite elements in the fixed finite level act trivially. The image of their product with the connected archimedean norm-one scalar group is an open subgroup of the norm-one idèle-class group: it is the image of the corresponding open subgroup of \(\mathbb A^1\). Compactness gives finite index. Finitely many coset representatives therefore put the entire orbit in a finite sum of translates of \(W\). A finite-dimensional continuous representation of a compact abelian group splits into characters: average an inner product, simultaneously diagonalize its commuting unitary matrices, and use their common eigenspaces. Those characters have modulus one. Their projections are finite linear combinations on the finite orbit and preserve every algebraic mixed submodule.

For a fixed norm-one character \(\omega\), the locally finite operator \(H_0\) gives a direct sum of generalized eigenvalue spaces. In its generalized \(\mu\)-space every function has a finite expansion
\[
\phi(a_{e^t}x)=e^{\mu t}\sum_{j=0}^r t^j f_j(x),
\qquad x\in G^1 .
\tag{1.23m}
\]
The coefficients are smooth cusp functions, at finite level, compact finite and central finite on \(G_\infty^1\), with polynomial growth. For a verification, evaluations at finitely many real \(t\)'s recover these coefficients by an invertible evaluation matrix: point evaluations span the dual of the finite-dimensional exponential-polynomial solution space, since a function killed by every evaluation is zero. Evaluations at those fixed central translates commute with compact actions, finite levels and central differential operators. They preserve polynomial growth. Linear independence in \(t\) and compact-domain integration show that every cusp constant term of every coefficient is zero. Thus \(f_j\in\mathcal C_\omega\).

These observations also prove full cuspidal arithmetic finiteness when a central character has not been specified separately. At fixed \(U\), the open subgroup made from connected archimedean norm-one scalars and scalar finite level has a fixed finite index in the compact idèle-class group. A cofinite ideal in the enveloping centre supplies polynomial equations for a basis of the central Lie algebra, as well as for \(H_0\) and \(\Omega\). There are finitely many joint Lie-character choices. They determine the character on the connected archimedean scalar subgroup, because that subgroup is generated by its exponentials; the finite remaining quotient permits only finitely many extensions. The polynomial in \(H_0\) bounds both its possible \(\mu\)'s and every Jordan degree \(r\). The polynomial in \(\Omega\) annihilates all coefficient functions in (1.23m). Lemma 1.19e makes each of their constrained spaces finite dimensional. Recovering the original function from its finitely many coefficients therefore proves finite dimensionality at fixed finite level, compact packet and cofinite infinitesimal-character ideal without an extra central-character restriction.

Filter this generalized space by the degree \(r\) in (1.23m). The filtration is invariant under the full mixed action. The leading-coefficient map identifies its degree-\(r\) quotient with
\[
\mathcal C_\omega\otimes\nu^\mu .
\tag{1.23n}
\]
Indeed right translation by \(g\) replaces \(t\) by \(t+\log\nu(g)\), multiplies the leading coefficient by \(\nu(g)^\mu\), and translates \(x\) by \(g a_{\nu(g)}^{-1}\). This also verifies the assertion infinitesimally. Every \(f\in\mathcal C_\omega\) occurs as a leading coefficient: \(e^{\mu t}t^r f(x)\) is a legitimate automorphic cusp function. It has moderate growth because \(\nu^{\pm1}\), the normalized representative height and powers of \(\log\nu\) are bounded by fixed powers of the original matrix height. Central finiteness follows from the finite polynomial degree in \(t\) and central finiteness of \(f\); the Lie algebra is the direct sum of its norm-one algebra and the central \(H_0\), so its enveloping algebra is the corresponding tensor product.

Let now \(\pi=A_1/A_0\) be an abstract irreducible admissible cuspidal subquotient. Finite-corner Schur makes its real central Lie action scalar, say \(H_0=\mu\), and makes its norm-one central action a scalar character \(\omega\). The finite-orbit compact argument makes that character unitary. Choose a vector of \(A_1\) with nonzero image. Its finite central orbit can be projected to the matching \(\omega\) and generalized \(\mu\) pieces; the other pieces have zero image. For the latter assertion, \(H_0-\mu\) is invertible on a finite orbit of any other eigenvalue, whereas it is zero on \(\pi\). These projections preserve \(A_1,A_0\) and supply a nonzero preimage with the desired data.

Choose the least degree \(r\) for which \(A_1\) intersected with that filtered space has nonzero image in \(\pi\). Its image is all of \(\pi\) by irreducibility; the preceding degree has zero image. Consequently \(\pi\) is a simple subquotient of (1.23n). Equation (1.23l) makes (1.23n) semisimple. One can check the needed elementary assertion without a categorical theorem: a cyclic preimage has support in finitely many simple summands; a submodule of a finite direct sum of simples is a sum of simples, by induction, projecting to the first summand and splitting off its graph after choosing the inductive complement to the kernel. Its quotient is again a sum of simples. Thus every simple subquotient is isomorphic to one of the original simple summands. We obtain
\[
\pi\simeq H_{i,\mathrm{fin}}\otimes\nu^\mu .
\tag{1.23o}
\]

Remove \(\operatorname{Re}\mu\). The remaining imaginary twist is an actual unitary central extension of \(H_i\); it is therefore an irreducible admissible cuspidal Hilbert realization of \(\pi\otimes\nu^{-\operatorname{Re}\mu}\). Its complete smooth-vector spaces and continuous automorphic inclusion are supplied by the already proved actual-Hilbert comparison. Restoring the real determinant twist gives the full invariant smooth moderate-growth embedded cusp realization of \(\pi\) itself. The local unitary tensor factors and product pairings apply to its unitary normalization, with the prescribed norm-twist bookkeeping.

For \(n=1\), \(X=F^\times\backslash\mathbb A^1\) is compact and is the whole norm-one centre. A fixed central character function is a scalar multiple of that character: \(\phi(xz)=\omega(z)\phi(x)\) determines it from its value at one. Its Hilbert space is one dimensional. The finite central-orbit decomposition, positive-central expansion and filtration argument just given therefore apply directly. There are no proper-parabolic conditions or cusp tails in this case.

This proves the theorem in the subquotient definition used in *Automorphic representations and automorphic L-functions*. In particular the realization hypothesis of its archimedean genericity Corollary 1.4 and of the global product pairing is now furnished by an actual construction. \(\square\)

Further readings are [Getz–Hahn, freely accessible author draft of 22 April 2022, Theorem 6.5.1, printed page 150/PDF page 166, and §9.7, printed pages 233–236/PDF pages 249–252](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf). The tensor and cusp-space discussion is [Goldfeld–Jacquet, *Automorphic representations and L-functions for GL(n)*, §§4 and 8, printed/PDF pages 19–21 and 31–39](https://www.math.columbia.edu/~goldfeld/LanglandsBookChapter.pdf). The preceding proof establishes the realization and admissibility assertions. No standard or Rankin–Selberg analytic continuation theorem, local Whittaker uniqueness theorem, or general type-I classification is used.

### Recovering the complete Euler product

The algebraic restricted tensor decomposition is proved in *Automorphic representations and automorphic L-functions*, Theorem 1.1. Theorem 1.13 now proves the compatible unitary restricted tensor realization and product pairings for the actual admissible Hilbert cusp constituents of Theorem 1.11. Proposition 1.14 and Lemma 1.15 extend this conclusion to the specified embedded smooth cuspidal realizations. We apply the integral argument to these realizations: their finite vectors are the smooth moderate-growth cusp forms used above. Theorem 1.19 places every abstract cuspidal subquotient in such a realization after its specified norm normalization, so this integral argument applies to that definition as well.

In this realization pure tensor cusp vectors and their duals, with spherical unit vectors at almost every place, have matrix coefficient \(c(g)=\prod_vc_v(g_v)\). Choose \(\Phi=\bigotimes_v\Phi_v\), with the good-place tests of (1.5n) outside a finite set \(S\) containing infinity, ramification and the different.

The absolute estimates (1.5o) and the exceptional-place estimate justify product integration in the initial half-plane. Thus

\[
Z(s,\Phi,c)=\prod_v Z_v(s,\Phi_v,c_v)
=\mathcal L(s,\pi_0)\prod_{v\in S}H_v(s).
\tag{1.5z}
\]

Only finitely many normalized factors occur on the right. At each \(v\in S\), local input (1.5j) says \(1=\sum_jp_{v,j}(s)H_{v,j}(s)\). Multiply these finite identities and use (1.5z) for each tensor choice. This writes

\[
\mathcal L(s,\pi_0)=\sum_{\boldsymbol j}
\left(\prod_{v\in S}p_{v,j_v}(s)\right)
Z(s,\Phi_{\boldsymbol j},c_{\boldsymbol j}).
\tag{1.6}
\]

Every coefficient in (1.6) is entire, with at most polynomial growth on a closed strip: \(q_v^{\pm s}\) has bounded modulus there and the infinite-place coefficients are polynomials. The global integrals are entire and decrease faster than every power by (1.5x). Consequently (1.6) proves that the complete standard product is entire and bounded on every closed strip.

For one tensor choice whose normalized product is not identically zero, apply the local equation (1.5k) to (1.5z) and compare with (1.5y). This gives

\[
\mathcal L(s,\pi_0)\prod_{v\in S}H_v(s)
=\left(\prod_v\epsilon_v(s,\pi_{0,v},\psi_v)\right)
\mathcal L(1-s,\widetilde\pi_0)\prod_{v\in S}H_v(s).
\]

Cancel the nonzero meromorphic product. Such a choice exists, since the finite identity (1.6) and the nonzero Euler product in its initial half-plane preclude every choice being zero. Equation (1.5l) now gives the first equation in (1.4), with root constant \(w(\pi_0)\).

Finally, unitarity gives \(\widetilde\pi_0\simeq\overline{\pi_0}\), by the invariant Hermitian pairing as in Proposition 2.3 below. The conjugation normalization in local input 1.1c therefore gives
\(\mathcal L(s,\widetilde\pi_0)=\overline{\mathcal L(\overline s,\pi_0)}\). The entire product is not identically zero, so some point \(s=1/2+iT\) has nonzero value. At that point the functional equation has the form
\(\mathcal L(s,\pi_0)=w(\pi_0)A(\pi_0)^{-iT}\overline{\mathcal L(s,\pi_0)}\). Taking absolute values proves \(|w(\pi_0)|=1\). Multiplying by \(A^{s/2}\) yields the conductor-normalized equation.

To restore the removed central character, the local twist identity gives
\(\mathcal L(s,\pi)=\mathcal L(s+i\tau,\pi_0)\) and
\(\mathcal L(1-s,\widetilde\pi)=\mathcal L(1-s-i\tau,\widetilde\pi_0)\). The conductor is unchanged and
\(\varepsilon(\pi)=w(\pi_0)A(\pi)^{-i\tau}\), still of absolute value one. Entireness and strip bounds are unchanged by this imaginary shift. This completes the global deduction for all \(n\ge2\) and all number fields, conditional on the remaining general conductor/factor identification and general archimedean local inputs. Theorem 1.19 supplies the realization comparison for every abstract cuspidal subquotient, and Theorem 1.13 supplies the compatible product pairings.

For \(\pi=|\cdot|^{it}\) in degree one, \(\mathcal L(s,\pi)=\mathcal L(s+it,1)\). The complete zeta function has poles at zero and one, so the shift gives the two poles in Theorem 1.1. The finite Dedekind zeta function has no pole at zero; this is why the finite product cannot replace the completion in that assertion.


## 2. Rankin–Selberg factors and their reciprocals

Let \(\pi\) and \(\pi'\) be unitary cuspidal automorphic representations of \(GL_n(\mathbb A)\) and \(GL_m(\mathbb A)\). The nonzero global Whittaker transform for every nonzero smooth cuspidal function, over every number field and in every rank, is proved in *Automorphic representations and automorphic L-functions*, Theorem 1.3. Corollary 1.4 there proves local Whittaker existence for an irreducible admissible cusp module with its specified smooth cuspidal realization: the full adelic right action, a finite-level Fréchet smooth topology of moderate growth, continuous inclusion for all derivatives on compact sets, the given \(K_\infty\)-finite core, and continuous differentiation and compact averaging. At infinity the resulting functional is continuous. Theorem 1.19 supplies this smooth realization for every abstract cuspidal subquotient. Thus Corollary 1.4 of that earlier lesson gives a continuous archimedean Whittaker functional for every such local factor. Theorem 2.0 below proves local uniqueness at every finite place in every rank; Theorem 2.0n proves the archimedean distributional-principal-series bound; Theorems 2.0x–2.0z below construct the full continuous-dual embedding and prove uniqueness in every supplied actual complete smooth moderate dual-pair model. Theorem 1.34 supplies a compatible pair for every abstract irreducible admissible core.

For a fixed nontrivial additive character \(\psi:F\backslash\mathbb A\to\mathbb C^\times\), local Rankin–Selberg integrals pair a \(\psi_v\)-Whittaker function with a \(\psi_v^{-1}\)-Whittaker function. For equal ranks a Schwartz function also enters. The opposite characters ensure that the integrand descends to the unipotent quotient. The defining integrals and their analytic factor construction are [Getz–Hahn, 22 April 2022 draft, §11.5]. Local Whittaker uniqueness, local factor identification and the general integral construction remain additional assertions, rather than consequences of the existence proofs.

The resulting factor \(L_v(s,\pi_v\times\pi'_v)\) has degree at most \(nm\) at a finite place and degree \(nm\) when both representations are unramified. Define

\[
\mathcal L(s,\pi\times\pi')=\prod_v L_v(s,\pi_v\times\pi'_v),\qquad
L^S(s,\pi\times\pi')=\prod_{v\notin S}L_v(s,\pi_v\times\pi'_v),
\tag{2.1}
\]

where \(S\) is finite and contains infinity and the ramified places. The products initially mean products in a sufficiently far right half-plane.

### Local Whittaker uniqueness over every nonarchimedean local field

This proof concerns complex smooth admissible representations. The field \(F\) is an arbitrary nondiscrete nonarchimedean local field, of either characteristic, and \(n\geq1\). Set \(G=GL_n(F)\), let \(U\) be its upper unitriangular subgroup, and let
\[
\Psi(u)=\psi\!\left(\sum_{i=1}^{n-1}u_{i,i+1}\right),
\qquad \tau(g)=w_0\,{}^tg\,w_0,
\qquad \theta(g)=\tau(g)^{-1},
\tag{2.6a}
\]
where \(\psi\) is a nontrivial continuous additive character and \(w_0\) has ones on the antidiagonal. Thus \(\tau\) is an involutive antiautomorphism, \(\theta\) is an involutive automorphism, \(\tau(U)=U\), \(\Psi\circ\tau=\Psi\), and \(\Psi\circ\theta=\Psi^{-1}\).

We prove the theorem for every nondegenerate continuous character of \(U\), not only the normalization in (2.6a). All the distribution, duality and multiplicity arguments needed for the theorem are included below. The classical comparison is [Bernstein–Zelevinsky's freely accessible author-hosted 1976 paper, §§6–7, especially Theorems 6.9–6.13 and 7.3 and the proof of 5.16 on printed/PDF pages 58–60](https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/B-Zel-RepsGL-Usp.pdf). The localization, duality and multiplicity arguments are proved below.

The local topology and Haar measure used here are the actual earlier proofs in *Local fields: classification and Haar measure*, Proposition 3.1 and Proposition 6.1. The compact averaging and smooth-dual proofs in *Smooth local representations and the Hecke-module dictionary*, §§1, 3–5 apply to any totally disconnected group; their necessary arbitrary-rank arguments are also written below. No admissibility theorem for all irreducible representations is assumed: admissibility is a hypothesis of the local theorem.

#### Test functions, closed support and localization

An \(l\)-space is a locally compact Hausdorff space with a basis of compact open sets. Write \(\mathcal S(X)=C_c^\infty(X)\) for its locally constant compactly supported complex functions. A distribution is a linear functional on \(\mathcal S(X)\). In the spaces below the usual test-function topology is the inductive limit of the finite-dimensional spaces obtained by fixing a compact support and a finite compact-open partition. Thus these algebraic functionals are exactly the usual distributions; no finite-order differential distributions occur in a nonarchimedean direction.

**Lemma 2.0a (closed support).** If \(Y\subset X\) is closed, restriction gives an exact sequence
\[
0\longrightarrow\mathcal S(X\setminus Y)
\longrightarrow\mathcal S(X)
\longrightarrow\mathcal S(Y)\longrightarrow0.
\tag{2.6b}
\]
Consequently a distribution supported on \(Y\) is exactly a distribution on \(Y\), composed with restriction. The same statement holds for a locally closed subset after restricting to an open neighbourhood in which it is closed.

*Proof.* A test function on \(Y\) has a finite partition of its compact support into subsets open and closed in \(Y\), on each of which it is constant. Choose compact open neighbourhoods in \(X\) whose intersections with \(Y\) give these subsets near their compact supports; finitely many suffice. Taking differences and intersections refines them to a disjoint compact-open partition in \(X\), and extending the constants on that partition gives an extension with compact support. A function restricting to zero on \(Y\) has compact support disjoint from \(Y\), so is the extension by zero of a function in \(\mathcal S(X\setminus Y)\). Dualizing the sequence proves the assertion. In particular there are no additional transverse derivatives attached to a closed subset. \(\square\)

Suppose an \(l\)-group \(H\) acts continuously on \(X\), and \(\chi:H\to\mathbb C^\times\) is a continuous character. On test functions use \(L_h f(x)=f(h^{-1}x)\). A \(\chi\)-equivariant distribution satisfies \(D(L_hf)=\chi(h)D(f)\). It is the dual of
\[
Q_H^\chi(X)=\mathcal S(X)\big/\operatorname{span}
\{L_hf-\chi(h)f:h\in H,\ f\in\mathcal S(X)\}.
\tag{2.6c}
\]

**Lemma 2.0b (localization over an \(l\)-space).** Let \(p:X\to B\) be continuous, where \(B\) is an \(l\)-space and \(p(hx)=p(x)\). If every fibre \(X_b\) has no nonzero \(\chi\)-equivariant distribution, neither does \(X\).

*Proof.* Multiplication by functions pulled back from \(\mathcal S(B)\) commutes with \(H\) and acts on (2.6c). It has local units: for a test function \(f\), choose a compact-open function on \(B\) equal to one on the compact set \(p(\operatorname{supp}f)\). At \(b\in B\), quotient this module by the ideal of functions vanishing at \(b\). The resulting fibre of \(\mathcal S(X)\) is precisely \(\mathcal S(X_b)\). Restriction is onto by Lemma 2.0a. If \(f\) vanishes on \(X_b\), the compact set \(p(\operatorname{supp}f)\) avoids \(b\), and a compact-open function equal to one on that set and zero near \(b\) expresses \(f\) as an element of the stated ideal. Taking the further quotient by the \(H\)-relations commutes with this quotient. Therefore the fibre of \(Q_H^\chi(X)\) is \(Q_H^\chi(X_b)=0\).

For completeness, zero fibres imply a zero module here. Given a class \(q\), its zero class at \(b\) expresses it as a finite sum \(\sum a_jq_j\) with every \(a_j(b)=0\). All \(a_j\) vanish on a common compact-open neighbourhood \(V_b\), so \(1_{V_b}q=0\). A representative of \(q\) has a compact image of its support in \(B\). Cover that image by finitely many \(V_b\), refine to disjoint compact-open pieces, and use a local unit for \(q\). Summing the corresponding zero products gives \(q=0\). A nonzero vector-space quotient has a nonzero linear functional, so the asserted vanishing of distributions on a fibre is equivalent to its quotient being zero. \(\square\)

We will also need localization by orbits without importing an algebraic-group distribution theorem. An action is called **constructive** here if its orbit relation
\[
R_H=\{(x,hx):x\in X,h\in H\}\subset X\times X
\tag{2.6d}
\]
is a finite union of locally closed subsets. This is a condition we verify explicitly for both matrix actions used below.

**Lemma 2.0c (localization by constructive orbits).** Suppose \(H\) is second countable, \(X\) is an \(l\)-space, and the action is constructive. If every orbit has no nonzero \(\chi\)-equivariant distribution, \(X\) has none. In this assertion each orbit has its subspace topology, which agrees with \(H/H_x\).

*Proof.* Here are the topological details. For a subset \(M\) which is a union of \(r\) locally closed sets, let \(U(M)\) be the points of \(M\) at which \(M\) is closed in some ambient open neighbourhood, and put \(M^0=M\), \(M^{j+1}=M^j\setminus U(M^j)\). The set \(U(M)\) is locally closed and open in \(M\), and \(M^j\) is closed in \(M\). These constructions commute with restriction to an ambient open set. They terminate with \(M^r=\varnothing\). Indeed, write \(M=\bigcup_{i=1}^r S_i\), with \(S_i\) locally closed. On the complement of \(\overline{S_i}\), induction on \(r\) gives \(M^{r-1}=\varnothing\). Hence \(M^{r-1}\subset\bigcap_i\overline{S_i}\). The subset \(S_i\cap M^{r-1}\) is open in \(M^{r-1}\), because \(S_i\) is open in its closure, and closed in \(S_i\), because \(M^{r-1}\) is closed in \(M\). It is therefore a locally closed open part of \(M^{r-1}\). Its points belong to \(U(M^{r-1})\); these parts cover \(M^{r-1}\), proving the induction. In particular \(U(M)\) is nonempty when \(M\) is nonempty, and is dense in \(M\), by applying the same conclusion on every nonempty ambient open set meeting \(M\).

Let \(Y=X/H\), initially just a quotient topological space, and \(p:X\to Y\) the orbit map. It is open, since \(p^{-1}p(V)=\bigcup_h hV\). The image of an invariant closed subset is closed, by the definition of the quotient topology. An invariant locally closed subset has a locally closed image: express it as its invariant closure intersected with the invariant open complement of its boundary. Apply the preceding intrinsic decomposition to \(R_H\), which is invariant under \(H\times H\). Since \(p\times p\) is an open quotient map, the diagonal of \(Y\times Y\) is a finite union of locally closed sets. At some point \((y,y)\) that diagonal is closed in an open neighbourhood. Choosing a smaller product neighbourhood gives a nonempty open subset \(V\subset Y\) on which the diagonal is closed. Thus \(V\) is Hausdorff. It is an \(l\)-space: if \(x\in p^{-1}V\), a compact-open neighbourhood \(C\subset p^{-1}V\) has compact-open image \(p(C)\subset V\). Lemma 2.0b applies on \(p^{-1}V\).

Every orbit is locally closed. It is constructive by slicing (2.6d); its nonempty locally closed part \(U(Hx)\) is intrinsic and \(H\)-invariant, hence is the whole transitive orbit. To check the topology assertion, a continuous transitive action of a second-countable locally compact group on a locally compact Hausdorff orbit has an open orbit map. Given an identity neighbourhood \(A\subset H\), choose a compact neighbourhood \(C\) with \(C^{-1}C\subset A\). Countably many translates of \(C\) cover \(H\). Their compact orbit images are closed and cover the orbit. The Baire property of a locally compact Hausdorff space implies that some translate of \(Cx\) has interior; translating back and then by an element of \(C^{-1}\) shows that \(Ax\) contains an orbit neighbourhood of \(x\). The Baire property used here follows by placing successively smaller nonempty open sets with compact closures inside the complement of each proposed closed set with empty interior; the nested compact closures have a common point. Therefore \(H/H_x\to Hx\) is a homeomorphism.

Finally, if \(D\ne0\), replace \(X\) by its closed support. The support is \(H\)-invariant, remains an \(l\)-space, and the restricted orbit relation is constructive. The argument just given produces a nonempty invariant open subset with Hausdorff \(l\)-space orbit quotient. Its fibres have zero equivariant distributions, so \(D\) vanishes there by Lemma 2.0b, contradicting the definition of its full support. \(\square\)

#### The distribution on a single homogeneous orbit

All groups to which the following homogeneous calculation is applied have arbitrarily small compact-open subgroups: for matrix groups use their intersection with \(1+\varpi^rM_n(\mathcal O)\), for unipotent matrix groups use the corresponding integral root coordinates, and for the finite extensions choose these subgroups stable under the specified involution. Haar measures on the unipotent groups and their pattern subgroups are the triangular-coordinate measures proved in §3. Haar measures on \(GL_n\) and on the conjugacy stabilizers are constructed explicitly in §§4–5. Thus the applications do not require an unstated Haar-existence or centralizer-unimodularity theorem.

**Lemma 2.0d (homogeneous distributions).** Let \(H\) be a second-countable \(l\)-group, \(J\subset H\) closed, and \(X=H/J\).

1. An \(H\)-invariant distribution on \(X\) has dimension at most one. If a nonzero one exists, it is a scalar multiple of a positive invariant quotient Haar measure.
2. If \(H\) and \(J\) are unimodular, a \(\chi\)-equivariant distribution exists precisely when \(\chi|_J=1\), and then has dimension one. It is the weighted quotient measure
\[
D_\chi(f)=\int_{H/J} f(hJ)\chi(h)\,d\dot h .
\tag{2.6e}
\]
3. Suppose an involutive automorphism \(\alpha\) of \(H\) preserves \(J\) and \(\chi\), and let \(s\) be the induced involution of \(H/J\). If \(H,J\) are unimodular, \(s\) fixes the distribution in part 2. If \(\chi=1\), a more general assertion needs neither a fixed point nor unimodularity: any involution normalizing the \(H\)-action and preserving this orbit fixes its invariant distributions.

*Proof.* We give the descent argument, including uniqueness. Averaging on a right fibre defines
\[
qf(hJ)=\int_J f(hj)\,dj,\qquad q:\mathcal S(H)\to\mathcal S(H/J).
\tag{2.6f}
\]
It is onto. To see this without a section theorem, a compact-open subgroup \(C\subset H\) has compact-open orbit \(CJ\) in \(H/J\); the average of \(1_C\) is the constant \(\operatorname{vol}_J(C\cap J)\) on that orbit and zero off it. Its translates, with successively smaller compact-open \(C\), give a basis of compact-open neighbourhoods in \(H/J\). Finite partitions of a compact support therefore give every test function in the image. With a character, use instead
\(q_\chi f(hJ)=\int_J f(hj)\chi(hj)^{-1}\,dj\) when \(\chi|_J=1\).

A left-invariant distribution on \(H\) is a scalar multiple of left Haar measure. Indeed, its value on \(1_{hC}\) is independent of \(h\). If \(C'\subset C\) are compact open, their finite coset partition gives \(D(1_C)=[C:C']D(1_{C'})\), exactly the Haar relation. Intersecting two such subgroups compares their constants, and partitioning arbitrary compact-open supports into cosets proves uniqueness. Multiplication by \(\chi\) gives the corresponding statement for \(\chi\)-equivariant distributions on \(H\), with density \(\chi(h)\,dh\).

Pull a distribution on \(H/J\) back by (2.6f). It is therefore a scalar Haar distribution if it is invariant. Right translation by \(j\in J\) scales \(qf\) by the modular character of \(J\), while it scales Haar integration on \(H\) by that of \(H\). Nonzero descent forces \(\Delta_H|_J=\Delta_J\). Under this equality, integrating first along \(J\) defines a positive quotient measure. Here is a kernel calculation that establishes independence of the lift without assuming a local section. Choose a compact-open \(C\subset H\) such that \(f\) is left \(C\)-invariant. It is a finite linear combination of \(1_{Ch_i}\). Group these cosets by their right \(J\)-orbits in \(C\backslash H\). On one such orbit choose a representative \(h\), so its terms are \(1_{Chj_i}\). Their fibre integrals at \(hJ\) are positive constants proportional to the left-Haar masses of \((h^{-1}Ch\cap J)j_i\), and their quotient functions are supported on the same compact-open \(C\)-orbit \(ChJ\). Thus a combination has zero fibre integral exactly when its weighted coefficient sum is zero. Subtracting that sum times the representative \(1_{Ch}\) writes it as a finite sum of right-\(J\) translation differences, with precisely the positive modular factors given by those masses. Under \(\Delta_H|_J=\Delta_J\), Haar integration on \(H\) has the same right-translation factors and annihilates all these differences. This proves descent. It is positive because \(q\) has nonnegative lifts of nonnegative test functions, obtained from the compact-open quotient patches used to prove surjectivity. This proves part 1 and the quotient formula, not merely uniqueness up to an unspecified distribution.

The identical argument after multiplying by \(\chi^{-1}\) proves part 2. If \(\chi\) is nontrivial on \(J\), pullback would have both the fibre transformation law and the incompatible character law on \(J\); with unimodularity these cannot agree. If it is trivial, (2.6e) is well-defined, nonzero, and has the stated transformation law under \(L_h\).

For part 3, \(\alpha\) preserves Haar measure on \(H\) and \(J\): each Haar modulus is positive and its square is one. Hence it preserves quotient measure, and \(\chi\circ\alpha=\chi\) preserves the weight in (2.6e). More generally one can normalize the quotient measure directly: an involution carries a positive invariant quotient measure to a positive scalar multiple of itself, and that scalar has square one, hence equals one. This proves the last assertion when \(\chi=1\). \(\square\)

We use part 3 only with the literal involutive group automorphism just specified. It follows that if every orbit of a constructive action is preserved by an involution and every invariant orbital distribution is fixed, every invariant distribution is fixed. To prove this assertion, subtract its involution translate. The difference is invariant under the original group and transforms by sign under the group extended by the involution. This extended action is constructive: its orbit relation is the union of the original relation and its translate. On each extended orbit its sign-equivariant distribution space is zero by Lemma 2.0d. The original-group orbits are open and closed in that extended orbit because the original group has finite index and its orbit map is open, as proved in Lemma 2.0c. Consequently Lemma 2.0c applies to the sign character and kills the difference.

#### Bruhat orbits carrying a generic character

We first record all the relevant matrix geometry. For a permutation \(p\in S_n\), let \(w_pe_j=e_{p(j)}\), put
\[
U_p=U\cap w_pU^-w_p^{-1},
\qquad C_p=U\,T\,w_p\,U,
\tag{2.6g}
\]
and let \(T\) denote the diagonal torus. Each matrix in \(C_p\) has a unique expression \(a\,t\,w_p\,b\), with \(a\in U_p\), \(t\in T\), \(b\in U\). The coordinates are polynomial in the unipotent parameters and rational in matrix entries on the cell; they give its \(F\)-topological coordinates.

Here is a direct verification. Upper row operations preserve the ranks of the last \(n-i+1\) rows in the first \(j\) columns, and upper column operations preserve those ranks as well. Eliminate successively from the first column, choosing its lowest nonzero entry as pivot, clearing all entries above it by upper row operations and the other entries in its pivot row by upper column operations. Remove that row and column and repeat in the remaining ordered rows and columns. These invertible operations give precisely one permutation pivot position in every row and column. The pivot diagonal scalars give \(t\). Once the permutation is fixed, the permitted entries in \(a\) are exactly \(r<s\) with \(p^{-1}(r)>p^{-1}(s)\); the other upper entries can be moved through \(t w_p\) into \(b\). Both sets of roots are closed under addition, so their ordered elementary products are subgroups, and moving entries in increasing height gives unique coordinates. Alternatively uniqueness follows because
\(U_p\cap w_pUw_p^{-1}=\{1\}\), while diagonal entries force equality of \(t\). Every pivot division is by a specified nonzero minor. Thus the cell and its coordinates are described by finitely many polynomial equalities and nonzero inequalities.

In particular,
\[
r_{ij}(g)=\operatorname{rank}g_{\{i,\ldots,n\},\{1,\ldots,j\}}
=\#\{\ell\leq j:p(\ell)\geq i\}\quad(g\in C_p).
\tag{2.6h}
\]
These rank patterns distinguish the cells, and each cell is locally closed. The orbit relation for the action
\(H=U\times U\), \((u,v)g=u g v^{-1}\), is constructive: two matrices are in the same orbit exactly when they have the same permutation \(p\) and the same \(t\) in these coordinates. Equality of the rational coordinates, after their nonzero pivot denominators are specified, is a finite union of locally closed conditions. This verifies the hypothesis of Lemma 2.0c directly, rather than citing a general algebraic orbit theorem.

Use the character \(\chi(u,v)=\Psi(u)\Psi(v)^{-1}\) of \(H\). At \(g=t w_p\) the stabilizer is
\[
H_g=\{(gvg^{-1},v):v\in U\cap w_p^{-1}Uw_p\}.
\tag{2.6i}
\]
The groups in (2.6i) are unimodular. Their elementary coordinates are the roots \(i<j\) with \(p(i)<p(j)\); these roots are closed under addition. Translation in coordinates ordered by height is triangular with diagonal one, so product additive Haar measure is left and right invariant. The same proves unimodularity of \(U\) and \(H\).

**Lemma 2.0e (relevant orbits).** The orbit of \(t w_p\) has a nonzero \(\chi\)-equivariant distribution precisely when the list \(p(1),\ldots,p(n)\) consists of consecutive increasing intervals placed in decreasing order, and \(t\) is constant on each of these image intervals. Every such representative satisfies \(\tau(t w_p)=t w_p\).

*Proof.* For a root \(i<j\) with \(p(i)<p(j)\), conjugation in (2.6i) gives
\[
g(1+xE_{ij})g^{-1}
=1+x\frac{t_{p(i)}}{t_{p(j)}}E_{p(i),p(j)}.
\tag{2.6j}
\]
The character on the right-hand root is \(\psi(x)\) exactly when \(j=i+1\), and is trivial otherwise. The conjugated root contributes exactly when \(p(j)=p(i)+1\). Since \(\psi(cx)=\psi(x)\) for all \(x\) forces \(c=1\), stabilizer compatibility is equivalent to

- \(j=i+1\) if and only if \(p(j)=p(i)+1\), whenever \(i<j\) and \(p(i)<p(j)\);
- \(t_{p(i)}=t_{p(j)}\) for these simultaneous simple roots.

Every ascending step in the list \(p(1),\ldots,p(n)\) must therefore rise by exactly one. Split the list at its descending steps. Each run is a consecutive increasing interval of values. Distinct runs are disjoint intervals, and a descending step forces the preceding interval to lie wholly above the following one. Thus the intervals occur in decreasing order. Conversely a list of this form has an increasing pair of consecutive values only within one run, where their positions are consecutive; both conditions follow, provided \(t\) is constant on that run. These root conditions imply compatibility on the whole stabilizer, since the root groups generate it and both sides are characters. Lemma 2.0d proves the existence and uniqueness of its weighted orbit distribution.

The matrix \(t w_p\) now consists of square scalar-identity blocks on the block antidiagonal. Reflection across the full antidiagonal carries each such block to itself and reverses its diagonal entries. Those entries are equal by the condition on \(t\), proving \(\tau(t w_p)=t w_p\). \(\square\)

**Theorem 2.0f (generic distribution symmetry).** Every distribution \(D\) on \(G\) satisfying
\[
D\bigl(f(u^{-1}\,{\cdot}\,v^{-1})\bigr)
=\Psi(u)\Psi(v)D(f)
\qquad(u,v\in U)
\tag{2.6k}
\]
is fixed by \(\tau\).

*Proof.* In the \(H\)-action convention above this is \(\chi\)-equivariance. The involution \(\tau\) normalizes that action through the involutive automorphism
\[
(u,v)\longmapsto\bigl(\tau(v)^{-1},\tau(u)^{-1}\bigr),
\tag{2.6l}
\]
which preserves \(\chi\). By Lemma 2.0e, any orbit carrying an equivariant distribution has a representative fixed by \(\tau\). Formula (2.6e) and Lemma 2.0d therefore show that its orbital distribution is fixed by \(\tau\): (2.6l) preserves both Haar measures and the character weight. Every other orbit has zero equivariant distribution space. The difference \(D-\tau D\) is \(\chi\)-equivariant and transforms by sign under \(\tau\). The finite extension by (2.6l) is constructive. On each extended orbit its sign-equivariant distribution space is zero, by the preceding orbital calculation; original \(H\)-orbits are open and closed there. Lemma 2.0c proves that the difference is zero. This argument treats distributions on all Bruhat boundaries, through closed support and localization, not only functions on the open cell. \(\square\)

#### Transpose and conjugation-invariant distributions

The representation-theoretic duality needed below must be established separately. A product multiplicity bound by itself would not prove uniqueness for a representation whose dual had not been shown to be generic.

**Lemma 2.0g (constructiveness of conjugacy).** The conjugacy orbit relation on \(M_n(F)\), and on its open subset \(G\), is a finite union of locally closed sets. Every matrix is similar over \(F\) to its transpose.

*Proof.* We supply the polynomial-algebra verification. Regard \(F^n\), with \(z\) acting by \(A\), as an \(F[z]\)-module. It is presented by the polynomial matrix \(zI-A\): the map \(\sum z^rv_r\mapsto\sum A^rv_r\) is onto, and repeatedly subtracting multiples of \(zI-A\) reduces any polynomial vector uniquely to a constant vector. That constant is its image, so the kernel is precisely the image of \(zI-A\). Elementary polynomial row and column operations put any polynomial matrix into Smith form
\(\operatorname{diag}(d_1,\ldots,d_n)\), with monic \(d_i\mid d_{i+1}\). Here is the algorithm: choose a nonzero entry of smallest degree; divide other entries in its row and column by it and subtract the multiples. A nonzero remainder has smaller degree and becomes the new pivot. Once the pivot divides its row and column, clear them. If it fails to divide an entry of the remaining block, add that entry into the pivot row and perform division again, decreasing the pivot degree. Thus that stage terminates. Remove the cleared row and column and repeat. The resulting pivots divide their successors because, before removal, each pivot divides the remaining block. Multiplication by a scalar makes each pivot monic. For \(zI-A\) no pivot is zero, since its determinant is monic of degree \(n\).

Elementary operations preserve the ideals generated by the \(k\)-minors. Their monic generators are
\(\Delta_k=d_1\cdots d_k\), with \(\Delta_0=1\); hence the Smith factors are unique. The presentation decomposes into \(\bigoplus F[z]/(d_i)\), omitting unit factors. In the power basis of each nonconstant quotient the action of \(z\) is its companion matrix. Thus two matrices over \(F\) are similar if and only if they have the same \(\Delta_1,\ldots,\Delta_n\). Transposing a matrix permutes the minors of \(zI-A\), so preserves all these generators and proves similarity to the transpose. This works for inseparable polynomials and in characteristic two as well.

To verify constructiveness, compute each \(\Delta_k\) as the monic gcd of the finitely many \(k\)-minors, polynomials of degree at most \(n\). A polynomial's degree is found by testing its finitely many coefficients, and division by its nonzero leading coefficient is rational in those coefficients. The Euclidean algorithm decreases degree at each nonzero remainder, so a gcd of two such polynomials has at most \(n+1\) division stages. Compute the gcd of a finite list by successive pairs, ignoring zero polynomials. There are consequently only finitely many possible branches. On each branch the output coefficients are rational functions of the entries of \(A\), with denominators required to be nonzero. The branch itself is given by polynomial equalities and nonzero inequalities. For a pair \(A,B\), choose branches for both, require equal degrees and equal output coefficients for each \(\Delta_k\), and clear the specified nonzero denominators. Each condition is locally closed; the finite union of them is exactly the similarity relation. No algebraic orbit constructibility theorem has been used. \(\square\)

Here are explicit Haar measures for this conjugacy calculation. On \(G\), the density \(dg=|\det g|^{-n}d^{n^2}g\) is both left and right invariant: multiplication by a matrix \(a\) scales additive matrix measure by \(|\det a|^n\), which is cancelled by the density. For the stabilizer of \(A\), put \(\mathcal C_A=\{X\in M_n(F):XA=AX\}\). This is a finite-dimensional \(F\)-algebra, and \(G_A=\mathcal C_A^\times\) is its open unit set. Indeed a matrix inverse of a commuting invertible matrix still commutes with \(A\), and invertibility of its left multiplication \(L_x\) on \(\mathcal C_A\) is equivalent to having such an inverse: surjectivity supplies \(xy=I\).

Choose additive product Haar measure \(dx\) in a basis of \(\mathcal C_A\). Then
\[
d\mu_A(x)=\frac{dx}{|\det_F L_x|_F}
\qquad(x\in\mathcal C_A^\times)
\tag{2.6ha}
\]
is a left Haar measure. It is positive, finite on compact subsets and locally nonzero. Left multiplication by \(j\) changes the numerator by \(|\det L_j|_F\), while \(L_{jx}=L_jL_x\) changes the denominator by the same factor. Right multiplication instead has the positive factor \(|\det R_j|_F/|\det L_j|_F\), giving its modular character explicitly. Thus the closed stabilizer's Haar measure exists without an external theorem; no assertion that this character is trivial is needed. An invariant distribution, if it exists on the orbit, forces the compatible quotient measure by Lemma 2.0d.

**Theorem 2.0h (transpose symmetry for conjugacy distributions).** Every conjugation-invariant distribution on \(G\) is invariant under \(g\mapsto{}^tg\).

*Proof.* Transpose normalizes conjugation by \(h\mapsto{}^th^{-1}\), has order two, and preserves each conjugacy orbit by Lemma 2.0g. On any such orbit an invariant distribution is either zero or a scalar positive quotient Haar measure by Lemma 2.0d. Transpose fixes that measure: it carries it to a positive scalar multiple of itself, and the scalar has square one. The conjugation action is constructive by Lemma 2.0g. The sign-equivariant localization argument following Lemma 2.0d therefore applies. \(\square\)

#### Smooth duality and identification by traces

Give \(G\) Haar measure \(dg=|\det g|^{-n}\,d^{n^2}g\), up to a positive constant. Left or right multiplication by \(a\) scales additive matrix measure by \(|\det a|^n\), cancelling the determinant density. Thus \(G\) is unimodular. Transpose preserves this measure. Inversion preserves it as well: it carries left Haar to right Haar and has positive modulus whose square is one. Inner conjugation and \(\tau,\theta\) therefore preserve Haar measure.

Let \(\mathcal H=\mathcal S(G)\) with convolution. A test function is left and right invariant under a sufficiently small common compact-open subgroup \(K\). The averages \(e_K=\operatorname{vol}(K)^{-1}1_K\) are local units. For a smooth representation \(V\), the integral \(\pi(f)v\) is a finite sum: on the compact support of \(f\), intersect its finite locally constant partition with the open stabilizer cosets of \(v\). The convolution action and group action determine each other; a group translate of a smooth vector equals its Hecke translate by \(\delta_g*e_K\) when \(K\) fixes it.

The smooth contragredient is the open-stabilizer part \(V^\vee\) of the algebraic dual, with action \(\pi^\vee(g)\ell=\ell\circ\pi(g^{-1})\). For every compact open \(K\), restriction and averaging give
\[
(V^\vee)^K=(V^K)^*,\qquad
\ell\longleftrightarrow \ell|_{V^K},\quad
a\longmapsto a\circ e_K.
\tag{2.6m}
\]
If \(V\) is admissible, the dual is admissible and evaluation identifies \(V\) with its smooth bidual, since this is ordinary finite-dimensional biduality on every fixed space. If \(V\) is irreducible, so is \(V^\vee\): the annihilator in \(V\) of a nonzero invariant subspace \(W\subset V^\vee\) is proper and invariant, hence zero. Averaging shows that the annihilator of \(W^K\) in \(V^K\) is zero; finite dimension yields \(W^K=(V^\vee)^K\), and the union over \(K\) gives \(W=V^\vee\). A commuting endomorphism of an irreducible admissible module is scalar: restrict it to a nonzero finite-dimensional fixed space, choose an eigenvalue, and use the invariant nonzero kernel of the difference from that scalar.

For an admissible \(V\), \(\pi(f)\) has finite rank, because it has image in \(V^K\) and factors through \(e_K\) for any common bi-invariance subgroup of \(f\). Define the trace distribution \(\Theta_V(f)=\operatorname{tr}\pi(f)\). It is conjugation-invariant by finite-rank trace invariance under conjugation. It is a genuine distribution because it is a linear functional on \(\mathcal H\).

**Lemma 2.0i (traces determine irreducible admissible modules).** Two irreducible admissible representations with the same trace distribution are isomorphic.

*Proof.* Choose \(K\) with \(V^K\ne0\). Equality of \(\Theta(e_K)\) gives \(\dim V^K=\dim W^K>0\). The corners are simple modules for the unital algebra \(A=e_K\mathcal H e_K\). Indeed, if \(0\ne E\subset e_KV\) is \(A\)-invariant, \(\mathcal H E=V\) by simplicity, and \(e_K\mathcal H E=e_K\mathcal H e_KE=E\), proving \(E=e_KV\).

We recall the finite-dimensional character argument, so it is not an imported density theorem. A finite direct sum of simple modules is semisimple: induct on the number of summands, intersect a submodule with the first summands, choose a complement by induction, and project to the last simple summand. If this projection is nonzero, its kernel has already been removed and the remaining submodule is the graph of a module homomorphism; otherwise it lies in the first summands. This also shows that a proper submodule of \(S^r\) imposes a nonzero relation \(\sum c_i s_i=0\) when \(\operatorname{End}_A(S)=\mathbb C\). For a basis \(v_1,\ldots,v_r\) of the finite-dimensional simple \(S\), the image of \(a\mapsto(av_1,\ldots,av_r)\) is a submodule of \(S^r\). Such a proper-submodule relation would give \(\sum c_iv_i=0\), impossible. The image is therefore all of \(S^r\). For two nonisomorphic simples the same argument in \(S^r\oplus T^s\) separates their components, since \(\operatorname{Hom}_A(S,T)=0\). There is then an \(a\in A\) acting as the identity on \(S\) and zero on \(T\), which gives different traces. Equal characters therefore imply \(e_KV\simeq e_KW\).

Finally a simple smooth \(\mathcal H\)-module with nonzero \(e_K\)-corner is determined by that simple corner. Form \(M=\mathcal H e_K\otimes_A e_KV\). It is generated by its corner, and \(e_KM=e_KV\). Every proper submodule of \(M\) has zero corner: otherwise the simple corner, hence its generated module \(M\), would be contained in it. The sum of all proper submodules still has zero corner and is proper. Thus \(M\) has a unique simple quotient with that corner. The surjections to \(V\) and \(W\) identify both with this quotient. This proves the lemma. \(\square\)

**Theorem 2.0j (contragredient through transpose inverse).** For every irreducible smooth admissible representation of \(G\),
\[
\pi^\vee\simeq\pi\circ\theta.
\tag{2.6n}
\]

*Proof.* Write \(\check f(g)=f(g^{-1})\). The adjoint of \(\pi(\check f)\), restricted to the smooth dual, is \(\pi^\vee(f)\). On a common fixed-space corner it is an ordinary finite-dimensional transpose, and its trace is equal. Hence \(\Theta_{\pi^\vee}(f)=\Theta_\pi(\check f)\). Haar preservation gives \(\Theta_{\pi\circ\theta}(f)=\Theta_\pi(f\circ\theta)\). But
\(f\circ\theta=\check f\circ\tau\); conjugation and transpose invariance of \(\Theta_\pi\), proved in Theorem 2.0h, gives \(\Theta_\pi(f\circ\theta)=\Theta_\pi(\check f)\). Both representations are irreducible admissible. Lemma 2.0i identifies them. \(\square\)

It follows in particular that
\[
\operatorname{Hom}_U(\pi,\Psi)
\simeq \operatorname{Hom}_U(\pi^\vee,\Psi^{-1}).
\tag{2.6o}
\]
Indeed the same functional on the vector space of \(\pi\circ\theta\) transforms by \(\Psi\circ\theta=\Psi^{-1}\). This establishes genericity of the dual without using uniqueness or a classification of generic representations.

#### From distributions to multiplicity one

**Lemma 2.0k (the kernel argument).** Suppose an involutive Haar-preserving antiautomorphism \(\tau\) preserves \(U\) and \(\Psi\), and every distribution satisfying (2.6k) is \(\tau\)-invariant. If \(V\) is irreducible smooth admissible and both
\(\operatorname{Hom}_U(V,\Psi)\) and \(\operatorname{Hom}_U(V^\vee,\Psi^{-1})\) are nonzero, each has dimension one.

*Proof.* Choose nonzero functionals \(\ell\) and \(m\) in those spaces. Neither is assumed smooth. Nevertheless test-function convolution smooths them. For example, define \(\pi(f)m\in V\) by
\[
\langle\pi(f)m,v^\vee\rangle
=m\bigl(\pi^\vee(\check f)v^\vee\bigr).
\tag{2.6p}
\]
If \(f\) is left \(K\)-invariant, the right side depends only on \(e_Kv^\vee\), so lies in the \(K\)-fixed smooth bidual, which is \(V^K\) by (2.6m). Similarly \(\pi^\vee(f)\ell\) belongs to \(V^\vee\). These maps respect convolution and translation by the finite-sum identities for
\(\mathcal H\). Their images span all of \(V\) and \(V^\vee\), respectively: a compact average of either nonzero functional is nonzero by evaluation on a fixed vector, and its image is an invariant nonzero submodule.

Define
\[
T_{\ell,m}(f)=\ell(\pi(f)m).
\tag{2.6q}
\]
This is a distribution. Left translation gives the factor \(\Psi(u)\) by \(\ell\)-equivariance. Right translation by \(v^{-1}\) gives the factor \(\Psi(v)\), because the distribution-vector action is
\((\pi(v)m)(v^\vee)=m(\pi^\vee(v^{-1})v^\vee)=\Psi(v)m(v^\vee)\).
Thus it satisfies (2.6k), and is \(\tau\)-invariant.

Put \(f^\tau=f\circ\tau\). Haar preservation and the antiautomorphism identity give \((f*h)^\tau=h^\tau*f^\tau\). Therefore
\[
\begin{aligned}
B(f,h)&=T_{\ell,m}(f*h)
=\langle\pi(h)m,\pi^\vee(\check f)\ell\rangle,\\
B(f,h)&=B(h^\tau,f^\tau).
\end{aligned}
\tag{2.6r}
\]
Since the two smoothing maps are onto, the left kernel of \(B\) is
\(I_\ell=\ker[f\mapsto\pi^\vee(\check f)\ell]\), and the right kernel is
\(J_m=\ker[h\mapsto\pi(h)m]\). The symmetry says \(I_\ell=\{f:f^\tau\in J_m\}\). For fixed nonzero \(m\), this kernel is independent of the choice of nonzero \(\ell\).

Two surjective smoothing maps with this same kernel consequently induce an automorphism of \(V^\vee\). It commutes with the group: on the domain the right translate \(f(xa^{-1})\) maps, after inversion, to the left translate by \(a^{-1}\), so the common transformation rule on the target is \(\pi^\vee(a^{-1})\). Schur's lemma following (2.6m) makes this automorphism scalar. Evaluating at \(f=e_K\) and then on any \(v\in V^K\) recovers \(\ell(v)\); hence the original two functionals are scalar multiples. This proves that the first Hom space has dimension one. Keeping \(\ell\) fixed gives the same conclusion for the second. No dimension or continuity assumption on the original Whittaker functionals was used. \(\square\)

**Theorem 2.0 (nonarchimedean local Whittaker uniqueness, all ranks).** Let \(F\) be any nondiscrete nonarchimedean local field, \(n\geq1\), \(\pi\) an irreducible smooth admissible complex representation of \(GL_n(F)\), and \(\Xi\) a nondegenerate continuous character of its upper unipotent subgroup. Then
\[
\dim_{\mathbb C}\operatorname{Hom}_{U}(\pi,\Xi)\leq1.
\tag{2.6s}
\]
If this Hom space is nonzero it has dimension one, and the Whittaker realization \(v\mapsto[g\mapsto\ell(\pi(g)v)]\) is unique up to scalar. If it is zero the assertion includes that case without an existence assumption.

*Proof.* First take \(\Xi=\Psi\). If its Hom space is zero there is nothing to prove. Otherwise Theorem 2.0j gives a nonzero opposite-character functional on \(\pi^\vee\) through (2.6o). Theorem 2.0f and Lemma 2.0k give dimension one. A nonzero Whittaker map has invariant kernel; irreducibility makes it injective. An equivariant map into smooth \(\Psi\)-equivariant functions on \(G\) is determined by evaluation at the identity, so the same result proves the uniqueness of its image and normalization.

Here is the reduction for arbitrary \(\Xi\), including local fields of positive characteristic. The commutator identity
\([1+xE_{ij},1+yE_{jk}]=1+xyE_{ik}\) kills every nonsimple upper root in a character. The abelianization is therefore the list of first-superdiagonal entries, and \(\Xi(u)=\prod_i\psi_i(u_{i,i+1})\), with each \(\psi_i\) a nontrivial continuous additive character.

Every continuous additive character of \(F\) is unitary and locally constant. In characteristic \(p\), its values have order dividing \(p\). In characteristic zero, \(x\mapsto\log|\psi_i(x)|\) vanishes on the compact additive integral ring, and a sufficiently large integer power \(p^r x\) is integral; thus it vanishes everywhere. A sufficiently small additive ideal has character values in a fixed short arc around one. No nontrivial subgroup of the unit circle lies in that arc (the multiples of any nonzero angle eventually leave it), so that ideal is in the kernel.

Fix the character \(\psi\) of (2.6a), and let \(\varpi^c\mathcal O\) be its largest trivial fractional ideal. A nontrivial locally constant additive character has such an ideal: the set of trivial ideals is nonempty, is upward closed in their integer exponents, and is not all ideals, whose union is \(F\). If \(\psi_i\) is trivial on \(\varpi^m\mathcal O\), its restriction to
\(\varpi^{-r}\mathcal O/\varpi^m\mathcal O\), \(r\geq\max(0,-m)\), is \(x\mapsto\psi(a_rx)\) for a unique
\[
a_r\in\varpi^{c-m}\mathcal O/\varpi^{c+r}\mathcal O.
\tag{2.6t}
\]
Indeed these parameters inject into the character group: the annihilator of the ideal \(\varpi^{-r}\mathcal O\) is exactly \(\varpi^{c+r}\mathcal O\), by the definition of \(c\). Both finite groups have order \(q^{m+r}\), hence the injection is onto. The finite-character count used here has an elementary proof: a character on a subgroup extends on adjoining an element by choosing the appropriate root of its already specified value; restriction of characters is therefore onto, with kernel the characters of the quotient. Induction on finite group order, starting with cyclic groups, gives exactly the group's order many characters.

The cosets in (2.6t) are compatible as \(r\) increases. They are nested compact sets in \(\varpi^{c-m}\mathcal O\), with diameters tending to zero, so compactness and the valuation metric give a unique \(a_i\in F\). The ideals \(\varpi^{-r}\mathcal O\) exhaust \(F\), proving \(\psi_i(x)=\psi(a_ix)\) for all \(x\). Nontriviality means \(a_i\ne0\). Choose a diagonal \(d\) with \(a_i d_i/d_{i+1}=1\) recursively. Then \(\Xi(dud^{-1})=\Psi(u)\). Inner twisting by \(d\), or transferring a functional through \(\pi(d)\), identifies the two Hom spaces and proves (2.6s).

For \(n=1\), \(U\) is trivial. Irreducibility and the admissible Schur argument make every group element scalar, because \(F^\times\) is abelian; consequently the representation has dimension one. This gives the same bound directly. \(\square\)

#### Scope at the archimedean places

The preceding theorem proves the entire finite-place uniqueness assertion, including nongeneric representations, without unitarity, a cuspidal origin, a restriction-to-mirabolic theorem, or an assumed contragredient identity. It is valid in residue characteristic two and in positive characteristic.

The proof above does not establish higher-rank uniqueness for arbitrary irreducible smooth admissible realizations of \(GL_n(\mathbb R)\) or \(GL_n(\mathbb C)\). Lemma 2.0a is specific to locally constant test functions: over the archimedean fields a distribution supported on a closed Bruhat stratum can have transverse derivatives. Killing the orbital distribution alone does not kill those derivatives. For a continuous Whittaker functional on an actual smooth admissible realization, the associated smoothed matrix-coefficient distribution still has the two equivariance laws, but a proof through its transpose symmetry would have to control the transverse jets and the infinitesimal-character equations. An alternative route uses an embedding of the continuous dual in a distributional principal series. That embedding is a separate theorem from a smooth–Hilbert comparison, and the finite-place closed-support argument cannot prove it.

Rank one at infinity is covered directly for an actual irreducible smooth admissible complete Fréchet realization. The maximal compact subgroup is \(\{\pm1\}\) over \(\mathbb R\), and the circle over \(\mathbb C\). Some compact-character projection has nonzero image. For the finite group this follows by adding its two projections. For the circle it follows from the Fejér kernels \(m^{-1}|\sum_{r=0}^{m-1}e^{ir\vartheta}|^2\): these are nonnegative with normalized integral one and tend to zero uniformly off every neighbourhood of zero, so averaging them converges to each vector in every continuous seminorm by compact uniform continuity. If all character projections were zero, these finite Fourier sums would be zero and their limit would be zero.

Admissibility makes the image of such a character projection finite-dimensional. It is invariant under the abelian full group and closed, so topological irreducibility makes it the whole realization. Commuting complex matrices on that finite-dimensional space have a common eigenvector: take an eigenspace of one matrix and continue inside it whenever a remaining matrix is not scalar, strictly decreasing dimension. Its line is invariant under the group; irreducibility forces dimension one. Since \(U=1\), its continuous Hom space has dimension one. Theorem 2.0z below proves the higher-rank bound for every prescribed actual complete smooth moderate dual-pair model.


### Archimedean uniqueness inside distributional principal series

Let \(F=\mathbb R\) or \(\mathbb C\), viewed as a real Lie field, let \(G=GL_n(F)\), and let \(N\) and \(\bar N\) be the upper and lower unitriangular groups. Let \(\bar B=T\bar N\) be the lower triangular group. A nondegenerate unitary character \(\Psi\) of \(N\) is one whose restriction to every first-superdiagonal root group is nontrivial. Fix any smooth character \(\chi_T:T\to\mathbb C^\times\), extended trivially across \(\bar N\). Define the space of distributional functions
\[
I^{-\infty}(\chi_T)
=\{f\in C^{-\infty}(G):f(bx)=\chi_T(b)f(x),\
b\in\bar B\}.
\tag{2.7a}
\]
Here a generalized function is a continuous functional on compactly supported smooth densities. Its pullback by a diffeomorphism is therefore intrinsic; equations such as (2.7a) mean equality of such pullbacks. The group acts by \(R(g)f(x)=f(xg)\). We prove, including all transverse-support steps,
\[
\dim\{f\in I^{-\infty}(\chi_T):
R(n)f=\Psi(n)^{-1}f\text{ for }n\in N\}\leq1.
\tag{2.7b}
\]
This is an unconditional theorem about the explicitly defined distributional principal series. Applying it to an arbitrary irreducible smooth admissible representation requires an injective equivariant map of its continuous dual into one of the spaces (2.7a). That additional statement is not assumed or proved in this section.

The freely accessible primary comparison is [Jiang–Sun–Zhu, *Vanishing of quasi-invariant generalized functions*, arXiv:1212.6015v1, §4.2, printed/PDF pages 10–12](https://arxiv.org/pdf/1212.6015v1). Their proof uses a distributional version of Casselman's subrepresentation theorem to pass from (2.7b) to arbitrary representations. The following proof establishes (2.7b) directly; this citation does not supply that embedding theorem or any omitted distribution argument.

#### Equivariant generalized sections on a homogeneous manifold

**Lemma 2.0l (transitivity makes equivariant distributions smooth).** Suppose a second-countable real Lie group \(H\) acts smoothly and transitively on a manifold \(Z\), acts smoothly on a finite-dimensional vector bundle \(E\to Z\), and \(s\) is a generalized section with \(A_hs=\rho(h)s\), where \(A_h\) is the induced section action and \(\rho\) is a smooth character of \(H\). Then \(s\) is smooth. Its value at any \(z\) satisfies
\[
h\,s(z)=\rho(h)s(z)\qquad(h\in H_z).
\tag{2.7c}
\]
In particular \(s=0\) if the indicated eigenspace of the stabilizer on \(E_z\) is zero.

*Proof.* Choose \(a\in C_c^\infty(H)\) such that \(c=\int_H a(h)\rho(h)\,dh\ne0\), using a small neighbourhood on which \(\rho\) is close to its nonzero value at one point. Averaging the action gives \(A(a)s=cs\). This averaging operator has a smooth integral kernel on \(Z\times Z\), locally with the compact support in its second variable needed to apply a distribution.

Here are the kernel details. The map
\[
H\times Z\longrightarrow Z\times Z,\qquad
(h,y)\longmapsto(hy,y)
\tag{2.7d}
\]
is a submersion: the \(H\)-directions span the tangent space of the first factor, by transitivity, and the \(y\)-directions supply the second. To check the first assertion directly, an orbit map has constant differential rank, since translations in \(H\) and the action on \(Z\) identify its differentials. Constant-rank coordinates show that, if this rank were smaller than \(\dim Z\), the image of each sufficiently small compact coordinate patch in \(H\) would be contained in a lower-dimensional submanifold and have empty interior. A countable collection of such compact patches covers \(H\), so their closed images would cover the locally compact manifold \(Z\), contradicting the Baire property. That property follows from nested nonempty relatively compact open sets, as in Lemma 2.0c. In the matrix orbits used below, the rational elimination coordinates give these submersion charts directly as well.

In coordinate neighbourhoods, choose among the \(H\)-coordinate directions a basis for the first tangent space. The inverse function theorem, with the remaining coordinates as parameters, writes (2.7d) as a coordinate projection. Its needed local form has the elementary following proof. Normalize an invertible derivative to the identity. On a small closed coordinate ball the derivative of \(f(x)-x\) has norm less than \(1/2\). For target \(y\) sufficiently close to \(f(0)\), iteration of \(x\mapsto y-(f(x)-x)\) stays in that ball and has geometrically decreasing differences. It converges to the unique solution \(f(x)=y\). Subtracting the equations for two targets, and then using the differentiable remainder of \(f\), gives derivative \(Df(x)^{-1}\) for the inverse; induction in that identity gives a smooth inverse. Keeping the other coordinates as parameters gives the submersion form and the constant-rank charts just used.

Fibre integration of a compactly supported smooth function in such a chart is smooth, by differentiating under its integral. A finite smooth partition of unity on each relevant compact subset patches these formulae. Such a partition is constructed by choosing finitely many coordinate bump functions positive on a cover of that compact set and dividing each by their positive sum on its neighbourhood. In a bundle trivialization the matrix transporting \(E_y\) to \(E_{hy}\) is smooth, so the same argument gives a matrix-valued smooth kernel.

For \(x\) in a fixed compact coordinate patch and \(h\in\operatorname{supp}a\), any \(y\) contributing to that kernel lies in the compact set \((\operatorname{supp}a)^{-1}\{x\}\), with the \(x\)-patch enlarged slightly. Thus pairing the kernel with \(s\) in its \(y\)-variable is defined and differentiable in \(x\) to every order. This proves that \(A(a)s\), hence \(s\), is smooth. Evaluating the equivariance identity at a fixed point gives (2.7c). The orbit of one point is all of \(Z\), so a zero value at that point makes the entire section zero. \(\square\)

The only analytic constructions just used are ordinary local coordinates, the inverse function theorem, finite smooth partitions on a compact set, and differentiation under compactly supported integrals. In particular the lemma does not import elliptic regularity, a distributional Frobenius-reciprocity theorem, or a representation-theoretic globalization theorem.

#### Transverse derivatives and a unipotent stabilizer

**Lemma 2.0m (normal-jet vanishing on a transitive stratum).** Let \(Z\) be a locally closed, transitive \(H\)-invariant submanifold of a manifold \(M\). Fix a smooth character \(\rho\) of \(H\). Suppose that at a point \(z\in Z\) the stabilizer contains an element \(j\) such that

- \(\rho(j)\ne1\);
- its action on \(T_zM\) is unipotent.

Then no nonzero \(\rho\)-equivariant generalized function on an open neighbourhood in which \(Z\) is closed can be supported on \(Z\).

*Proof.* Use coordinates \((y,t)\), with \(Z=\{t=0\}\). On a relatively compact coordinate patch every distribution has a finite order \(m\): its continuity gives a bound by the supremum of finitely many derivatives, all of order at most \(m\), of a test density. A distribution supported on \(t=0\) annihilates all tests whose derivatives in \(t\) of order at most \(m\) vanish there. Indeed, multiply such a test by a cutoff \(\eta(t/\epsilon)\) equal to one near zero. Support makes its distributional value unchanged. Taylor's formula in \(t\) bounds all derivatives of this product of total order at most \(m\) by \(O(\epsilon)\), so its value tends to zero. This proves the asserted annihilation.

Consequently the distribution on that patch has a unique finite expression
\[
\sum_{|\alpha|\leq m}s_\alpha(y)\,\partial_t^\alpha\delta(t),
\tag{2.7e}
\]
where \(s_\alpha\) are distributions in \(y\), with the local density factors understood. To construct and identify them, prescribe the finitely many Taylor coefficients by tests \(t^\alpha/\alpha!\) times a cutoff equal to one near zero, and subtract the resulting finite Taylor polynomial from an arbitrary test. The annihilation just proved gives (2.7e); testing these prescribed jets gives uniqueness.

The filtration by maximal transverse order is intrinsic: its order-\(m\) quotient is a finite-rank bundle on \(Z\), consisting of homogeneous degree-\(m\) normal derivatives with the normal-density factor. A diffeomorphism preserving \(Z\) preserves its ideal of functions vanishing on \(Z\), and hence this filtration. On the top quotient it acts by the corresponding symmetric power of the normal linear map and by its normal determinant factor. This follows directly by applying the chain rule to the highest transverse Taylor coefficient; terms involving fewer transverse derivatives belong to the lower filtration.

Equivariance and transitivity give a single finite upper bound for the transverse order along all of \(Z\): take the bound on a neighbourhood of one point and carry it by the \(H\)-action to neighbourhoods of every other point. Coordinate changes preserving \(Z\) preserve the transverse order. Thus a supported equivariant distribution has a top coefficient which is an equivariant generalized section of this finite-rank jet bundle over the whole orbit.

At \(z\), the action of \(j\) on \(T_zZ\) and on the normal quotient is unipotent, because these are an invariant subspace and quotient of \(T_zM\). Its normal determinant is one. All symmetric powers and duals of a unipotent linear map are unipotent: in a basis in which the map is triangular with diagonal one, the induced ordered monomial bases have the same property. The action on each top-jet fibre is therefore unipotent. It has no eigenvector with eigenvalue \(\rho(j)\ne1\); equivalently its difference from \(\rho(j)I\) is invertible.

Lemma 2.0l now makes the top coefficient smooth and zero. The transverse order drops by one. Repeating finitely many times makes every coefficient zero, including order zero, and proves the assertion. This argument explicitly eliminates derivatives supported on the stratum; it does not merely eliminate measures on the stratum. \(\square\)

#### The opposite Bruhat filtration

Put \(H=\bar B\times N\), with action \((b,n)x=bxn^{-1}\) and character
\[
\chi(b,n)=\chi_T(b)\Psi(n).
\tag{2.7f}
\]
Equations (2.7a) and (2.7b) say precisely that the generalized function has pullback law \(f(hx)=\chi(h)f(x)\). With the induced section action \(A_h f=f(h^{-1}x)\), the character in Lemmas 2.7c–4 is \(\rho=\chi^{-1}\).

The orbits of \(H\) are
\[
C_p=\bar B w_p N,\qquad p\in S_n.
\tag{2.7g}
\]
We give the matrix verification and the required open filtration. Lower row operations preserve the ranks of the first \(i\) rows in the first \(j\) columns. Upper column operations preserve the same ranks. Starting in the first column, choose its highest nonzero entry as pivot, clear the entries below it by lower row operations and clear the later entries of its pivot row by upper column operations. Remove that row and column and repeat in the remaining ordered rows and columns. Invertibility ensures one pivot in each row and column. Diagonal row operations normalize its nonzero scalars; thus there is exactly one permutation \(p\). The residual lower-root coordinates and upper-column coordinates give rational coordinates, with precisely the nonzero pivot minors as denominators, on the orbit (2.7g). They make it a locally closed smooth submanifold, on which \(H\) is transitive. The rank pattern is
\[
r_{ij}(x)=\operatorname{rank}x_{\{1,\ldots,i\},\{1,\ldots,j\}}
=\#\{\ell\leq j:p(\ell)\leq i\}.
\tag{2.7h}
\]
These patterns determine \(p\). This is also obtained by reversing the row order in the elementary upper-row Bruhat elimination; no abstract orbit classification is required.

If \(C_q\) meets the closure of \(C_p\), semicontinuity of matrix rank gives \(r_{ij}(w_q)\leq r_{ij}(w_p)\) for all \(i,j\). If \(q\ne p\), at least one inequality is strict. Order the permutations by decreasing \(\sum_{i,j}r_{ij}(w_p)\), breaking ties arbitrarily. The identity comes first: its pattern \(\min(i,j)\) is the unique maximal one. The union of any tail of this ordering is closed. Indeed its closure is the union of the closures of its finitely many cells, and any newly acquired cell has strictly smaller rank sum and is still in that tail. The closure is a union of whole cells because it is \(H\)-invariant. The complements therefore give an increasing sequence of invariant open subsets
\[
\varnothing=M_0\subset M_1\subset\cdots\subset M_{n!}=G,
\qquad M_i\setminus M_{i-1}=C_{p_i}.
\tag{2.7i}
\]
Here \(M_1=\bar B N\). The multiplication map \(\bar B\times N\to M_1\) is a diffeomorphism, since lower-times-upper Gaussian elimination is unique and its pivot denominators do not vanish. Its stabilizer is trivial.

For every nonidentity \(p\), the list \(p(1),\ldots,p(n)\) has a descent \(p(i)>p(i+1)\); a strictly increasing permutation would be the identity. Choose \(v=1+aE_{i,i+1}\in N\) with \(\Psi(v)\ne1\), which exists by nondegeneracy. Then
\[
\bar v=w_p v w_p^{-1}\in\bar N,\qquad
j=(\bar v,v)\in H_{w_p},\qquad
\chi(j)=\Psi(v)\ne1.
\tag{2.7j}
\]
Its differential on the ambient matrix space at the fixed point is
\[
A\longmapsto\bar v A v^{-1}.
\tag{2.7k}
\]
Left multiplication by \(\bar v\) and right multiplication by \(v^{-1}\) are commuting unipotent real linear maps, including when \(F=\mathbb C\). Their product is unipotent: writing them as \(I+P,I+Q\), with commuting nilpotent \(P,Q\), a sufficiently high power of \(P+Q+PQ\) is zero by the finite binomial expansion. The tangent space of \(G\), an open subset of the matrix space, has this same differential. Thus (2.7j) satisfies both hypotheses of Lemma 2.0m on every nonopen cell.

**Theorem 2.0n (all-rank principal-series bound over \(\mathbb R,\mathbb C\)).** The space in (2.7b) has dimension at most one.

*Proof.* Restriction to \(M_1\) is injective. To prove this, suppose an equivariant generalized function is zero on \(M_1\), and proceed along (2.7i). If it is zero on \(M_{i-1}\), its restriction to \(M_i\) is supported on the closed stratum \(C_{p_i}\). Equations (2.7j)–(2.7k) and Lemma 2.0m make it zero there as well. Finite induction proves it zero on \(G\).

On \(M_1\) the action is simply transitive. Lemma 2.0l makes every equivariant generalized function smooth, and its value at the identity determines it:
\[
f(bn^{-1})=\chi_T(b)\Psi(n)f(1).
\tag{2.7l}
\]
The right side defines a smooth equivariant function for any chosen value, so the space on this open orbit has dimension exactly one. Its injective restriction from \(G\) proves the bound; extension from the open orbit is not asserted or needed. \(\square\)

#### Precisely what transports to an arbitrary realization

**Corollary 2.0o (transport through an actual distributional embedding).** Let \(V\) be an actual smooth topological representation of \(G\), let \(V'\) be its continuous dual with action \((g\ell)(v)=\ell(g^{-1}v)\), and suppose a particular injective equivariant linear map
\[
\iota:V'\hookrightarrow I^{-\infty}(\chi_T)
\tag{2.7m}
\]
has been constructed. Then \(\dim\operatorname{Hom}^{\mathrm{cont}}_N(V,\Psi)\leq1\).

*Proof.* Such functionals are precisely the vectors \(\ell\in V'\) satisfying \(n\ell=\Psi(n)^{-1}\ell\). Equivariance and injectivity of (2.7m) put their space injectively into (2.7b), whose dimension is at most one by Theorem 2.0n. \(\square\)

Theorems 2.0x–2.0y below construct (2.7m) for every prescribed actual complete smooth moderate dual-pair model with irreducible admissible core. Their exact synthesis and full continuous-dual transpose proofs supply the required embedding, and Theorem 2.0z gives the bound in every real and complex rank. Theorem 1.34 constructs a compatible actual model for every abstract irreducible admissible core. Full onto/closed-image comparison remains a separate obligation.

### Direct archimedean Whittaker uniqueness in compatible unitary realizations

This section proves the continuous Whittaker multiplicity bound for every actual unitary Hilbert representation with irreducible admissible compact-type core of \(GL_n(\mathbb R)\) or \(GL_n(\mathbb C)\), on its full smooth-vector space, and for every determinant-character twist of such a representation. In particular it applies to all archimedean local factors of the cuspidal realizations constructed in Theorems 1.19 and 1.11–1.13. It uses neither a principal-series embedding nor a classification of those local factors.

It also proves the distribution symmetry used in the argument in every real and complex rank. The subsequent principal-synthesis and continuous-dual construction extends the uniqueness bound to every prescribed actual nonunitary smooth moderate dual pair in Theorem 2.0z.

Let \(F=\mathbb R\) or \(\mathbb C\), viewed as a real field, \(G=GL_n(F)\), and \(U\) the upper unitriangular subgroup. Fix
\[
\Psi(u)=\psi\left(\sum_{i=1}^{n-1}u_{i,i+1}\right),\qquad
\tau(g)=w_0\,{}^tg\,w_0,
\tag{2.8a}
\]
where \(w_0e_i=e_{n+1-i}\) and \(\psi:F\to\mathbb C^\times\) is a nontrivial unitary additive character. The map \(\tau\) is an involutive antiautomorphism, preserves \(U\), and preserves \(\Psi\). The positive Haar density is \(dg=c_F|\det g|_F^{-n}dX\). Transposition and multiplication by \(w_0\) preserve this density. Generalized functions mean continuous functionals on compactly supported smooth densities, with pullback by a diffeomorphism; this convention includes all normal-density factors.

#### Finite transverse order and a transverse differential operator

**Lemma 2.0p.** Let \(Z\) be a locally closed smooth submanifold of \(M\), and work in an open set where it is closed. Suppose \(P\) is a differential operator of order \(r\) whose highest symbol has nonzero image in
\(\operatorname{Sym}^r(T_zM/T_zZ)\) at every \(z\in Z\). A generalized function \(D\) supported on \(Z\) and satisfying \(PD=0\) is zero.

*Proof.* In coordinates \((y,t)\) with \(Z=\{t=0\}\), a distribution has finite order on every relatively compact patch. If its order there is at most \(a\), it annihilates tests whose normal Taylor coefficients through degree \(a\) vanish. Indeed, multiply such a test by a cutoff \(\eta(t/\epsilon)\) equal to one near zero. Support leaves its value unchanged, whereas Taylor's formula makes every derivative of the product through total order \(a\) tend to zero. Thus on the smaller patch
\[
D=\sum_{|\alpha|\le a}D_\alpha(y)\partial_t^\alpha\delta(t).
\tag{2.8b}
\]
Prescribing the finitely many normal Taylor coefficients of a test gives existence and uniqueness of this expression. The filtration by maximal normal order is intrinsic, since a diffeomorphism preserving \(Z\) preserves its vanishing ideal and its powers. Its degree-\(m\) quotient is the bundle of degree-\(m\) normal derivatives, with the normal-density line.

Let \(m\) be the largest nonzero normal order on a chosen patch, and \(q_z\) the indicated normal symbol of \(P\). The normal-order-\(m+r\) coefficient of \(PD\) is multiplication by \(q_z\) on the top coefficient of \(D\). Terms with a tangential derivative, or derivatives of the coefficients of \(P\), have smaller normal order. Multiplication by a nonzero homogeneous polynomial
\[
q_z:\operatorname{Sym}^m N_z\longrightarrow
\operatorname{Sym}^{m+r}N_z
\tag{2.8c}
\]
is injective: after choosing a basis, these are homogeneous polynomials, and a polynomial ring over \(\mathbb C\) has no zero divisors. The matrix of (2.8c) has full column rank. Locally it has a smooth left inverse, for example \((A^*A)^{-1}A^*\) in chosen auxiliary Hermitian metrics. This left inverse acts on generalized sections by multiplication by smooth coefficients. Consequently \(PD=0\) makes the top coefficient zero. Descending in \(m\) proves the assertion on the patch and hence on \(Z\). This proof does not assume smoothness of the coefficients \(D_\alpha\). \(\square\)

We also need a version of normal-jet vanishing with a parameter space.

**Lemma 2.0q.** Suppose \(H\) acts on a smooth manifold \(Z\), preserving a submersion \(Z\to B\), transitively on each fibre, and on a finite-rank bundle \(E\to Z\). Let \(\rho\) be a smooth character of \(H\). Suppose locally on \(Z\) there is a smooth map \(z\mapsto X(z)\in\mathfrak h\) such that

1. \(X(z)\) is in the stabilizer Lie algebra of \(z\);
2. its infinitesimal action on \(E_z\) is nilpotent;
3. \(d\rho(X(z))\ne0\).

Then a \(\rho\)-equivariant generalized section of \(E\) is zero on that neighbourhood. The conclusion remains true for a generalized function supported on \(Z\subset M\), provided the infinitesimal stabilizer action on \(T_zM\) is nilpotent and \(E\) is each of its normal-jet bundles.

*Proof.* Trivialize \(E\) and use a fixed basis \(X_j\) of \(\mathfrak h\). Write \(X(z)=\sum_j a_j(z)X_j\). Differentiating equivariance gives
\(\mathcal L_{X_j}s=d\rho(X_j)s\). In a local frame the induced first-order operator on generalized sections is the fundamental vector field of \(X_j\), followed by an order-zero matrix. These are precisely the operators obtained by differentiating the smooth bundle action; the same identity holds on distributions by transposition on test densities.

Multiply these identities by \(a_j\) and add them. The sum of the first-order coefficient vector fields vanishes, because \(X(z)\) stabilizes \(z\). The resulting identity is therefore
\[
\bigl(A_{X(z)}-d\rho(X(z))I\bigr)s=0.
\tag{2.8d}
\]
Here \(A_{X(z)}\) is the infinitesimal action of the stabilizer on the fibre. This observation avoids evaluation of a distribution at a parameter. It is an identity of generalized sections with smooth matrix coefficients. In the chosen frame it follows simply by writing the differential operators as \(v_j^a\partial_a+A_j\); the coefficients of every \(\partial_a\) sum to zero. In particular there is no unproved pointwise localization on \(B\).

A nilpotent matrix minus a nonzero scalar is invertible. Its inverse is the finite geometric sum in that nilpotent matrix, divided by the scalar, and is smooth locally. Applying this inverse to (2.8d) proves the first assertion.

For the second assertion use the local finite expression (2.8b). Equivariance preserves its intrinsic normal-order filtration. On the degree-\(m\) quotient, the action is the corresponding symmetric power of the normal map, with its normal-density line. If \(X(z)\) acts nilpotently on \(T_zM\), its exponential is unipotent on \(T_zM\), on \(T_zZ\), and on the normal quotient. Its determinant on the latter is one. Its infinitesimal action on the degree-\(m\) bundle is nilpotent, as follows by triangularizing the normal map and using the monomial basis for its symmetric power. Apply the first part to the top coefficient and descend through the finitely many local normal orders. \(\square\)

#### Bruhat strata and the trace quadratic form

Write \(w_pe_i=e_{p(i)}\) for a permutation \(p\). The Bruhat stratum
\[
C_p=U T w_p U
\tag{2.8e}
\]
has unique coordinates \(u\,t\,w_p\,v\), where \(u\in U_p\), \(t\in T\), \(v\in U\), and \(U_p\) consists of the ordered upper root coordinates \(E_{rs}\) with \(p^{-1}(r)>p^{-1}(s)\). The root coordinates are ordered by increasing height. Elimination with lower-left pivots constructs these coordinates: permitted upper row operations remove entries above a pivot, upper column operations remove entries to its right, and division by the nonzero pivots recovers \(t\). Successive elimination recovers \(u,v\). Thus the coordinate maps and their inverses are rational on the stratum and are smooth over both fields.

The ranks of lower-left rectangular submatrices distinguish these strata. The conditions that such a rank is at most \(r\) are the vanishing of minors and hence closed. The finite collection of rank patterns orders the strata so that successive unions starting with \(C_{w_0}\) are open. Equivalently remove a stratum maximal among the remaining lower-left rank patterns at each step. The usual elimination shows that every residual matrix has one of the residual patterns. This provides a finite open filtration and justifies induction on boundary support below.

Let \(H=U\times U\) act by \((a,b)g=agb^{-1}\), with character
\(\chi(a,b)=\Psi(a)\Psi(b)^{-1}\). At \(g=t w_p\), its stabilizer consists of pairs with
\[
b\in U\cap w_p^{-1}Uw_p,\qquad
a=t w_p b w_p^{-1}t^{-1}.
\tag{2.8f}
\]
A root \(E_{ij}\), \(i<j\), occurs in this intersection exactly when \(p(i)<p(j)\). Its image on the other side is
\((t_{p(i)}/t_{p(j)})E_{p(i),p(j)}\).
The differential of \(\chi\) vanishes on this root precisely when either both roots are nonsimple, or both are simple and the displayed ratio is one. Thus compatibility is exactly
\[
j=i+1\ \Longleftrightarrow\ p(j)=p(i)+1
\quad\hbox{whenever }i<j,\ p(i)<p(j),
\tag{2.8g}
\]
and \(t_{p(i)}=t_{p(i+1)}\) at each increasing adjacent pair.

For completeness, (2.8g) has a simple finite combinatorial consequence. Split the list \(p(1),\ldots,p(n)\) into its maximal increasing adjacent runs. Every increasing adjacent step must increase its value by one, so the runs are disjoint intervals of integers partitioning \(\{1,\ldots,n\}\). Consider two intervals adjacent in the ordering by value, with the lower interval ending at \(a\) and the higher one beginning at \(a+1\). If the lower interval occurred first in the list, their endpoint positions would ascend; (2.8g) would make those positions adjacent. But the endpoints are the last entry of the lower run and the first entry of the higher run, so the two runs would then be consecutive and merge into one increasing run, a contradiction. Thus the higher interval precedes the lower one. Applying this to every consecutive pair of value intervals orders all runs decreasingly. Conversely such a list satisfies (2.8g), since every ascending pair lies inside a run and its position and value differences agree.

Call these permutations relevant. On a relevant stratum the compatible parameters \(t\) are constant on each image interval. Denote their smooth closed locus by \(T_p^0\), and put
\[
Z_p=U T_p^0 w_p U\subset C_p.
\tag{2.8h}
\]
The coordinates above make it a smooth closed submanifold of \(C_p\), with a smooth parameter space \(T_p^0\).

Outside \(Z_p\), or everywhere in a nonrelevant \(C_p\), one root in (2.8f) has \(d\chi\ne0\). Near a given point choose that root and its fixed real parameter direction with nonzero differential. For \(F=\mathbb C\), choose one real direction in its complex root line on which the nonzero real additive functional is nonzero. Equation (2.8f) then gives a smoothly varying stabilizer Lie element. At a general coordinate point \(u t w_p v\), conjugate the stabilizer by \((u,v^{-1})\); a character is unchanged by inner conjugation. Its action on the matrix tangent space is
\[
A\longmapsto a A b^{-1}.
\tag{2.8i}
\]
For these root stabilizers \(a,b\) are unipotent. Left and right multiplication commute and are unipotent, so their product is unipotent; differentiating gives the needed nilpotent infinitesimal action. Lemma 2.0q kills every equivariant normal jet on the incompatible part. This includes distributions in the torus parameters, rather than only distributions on an individual orbit.

Consider the nondegenerate real bilinear form
\[
\beta(X,Y)=
\begin{cases}
\operatorname{tr}(XY),&F=\mathbb R,\\
\operatorname{Re}\operatorname{tr}(XY),&F=\mathbb C.
\end{cases}
\tag{2.8j}
\]
It is invariant under conjugation. Left translation gives a bi-invariant pseudo-Riemannian form on \(G\). If \((X_a)\) is any real basis and \((X^a)\) its \(\beta\)-dual, its quadratic Casimir is
\(\Omega=\sum_a X_aX^a\). Invariance makes it central: differentiating
\(\beta([Y,X],Z)+\beta(X,[Y,Z])=0\) shows that the commutator with \(Y\) of the sum is zero. Its highest symbol is the inverse quadratic form of \(\beta\).

Here is a direct check that its left and right differential operators coincide, including the order-one terms. For real matrix coordinates \(g_{ab}\), the left and right fields for \(E_{ij}\) are respectively
\(\sum_a g_{ai}\partial_{aj}\) and \(\sum_b g_{jb}\partial_{ib}\). Expanding the dual-basis sum \(\sum_{i,j}E_{ij}E_{ji}\) gives on the left
\[
n\sum_{a,i}g_{ai}\partial_{ai}
+\sum_{a,b,i,j}g_{ai}g_{bj}\partial_{aj}\partial_{bi}.
\tag{2.8ja}
\]
On the right it gives the same Euler term and
\(\sum_{i,j,b,c}g_{jb}g_{ic}\partial_{ib}\partial_{jc}\).
Relabel the four indices and commute the coordinate derivatives to obtain the second term of (2.8ja). For \(F=\mathbb C\), complexify the real Lie algebra into its holomorphic and antiholomorphic matrix summands. The real basis \(E_{ij},iE_{ij}\) has \(\beta\)-dual \(E_{ji},-iE_{ji}\); their quadratic sum is twice the sum of the two complex Casimirs. Formula (2.8ja) applies separately to \(g_{ab}\) and \(\bar g_{ab}\), giving the same equality. Transposition conjugates the left fields into right fields and preserves the trace duality; conjugation by \(w_0\) preserves it too. Therefore \(\tau\) preserves \(\Omega\).

**Lemma 2.0r.** For every relevant \(p\ne w_0\), the normal symbol of \(\Omega\) on \(Z_p\) is nonzero at every point.

*Proof.* At \(g=t w_p\), use the left trivialization \(T_gG\simeq\mathfrak g\), \(A\mapsto g^{-1}A\). If the consecutive domain runs have lengths \(m_1,\ldots,m_r\), then
\[
g^{-1}T_gZ_p=
\mathfrak u+w_p^{-1}\mathfrak u w_p+\mathfrak a_p,
\tag{2.8k}
\]
where \(\mathfrak a_p\) consists of diagonal matrices constant on each domain run. Conjugation by \(t\) preserves \(\mathfrak u\). Between two different runs the first two spaces in (2.8k) include both off-diagonal directions. Within one run they include only the upper directions; their diagonal contribution is zero. If \(p\ne w_0\), at least one \(m_j\ge2\). Choose two positions \(i,i+1\) in that run and let
\[
H_0=E_{ii}-E_{i+1,i+1}.
\tag{2.8l}
\]
It is \(\beta\)-orthogonal to (2.8k), and \(\beta(H_0,H_0)=2\). Therefore the conormal covector \(\beta(H_0,\cdot)\) has nonzero value under the inverse quadratic form. This is exactly nonvanishing of the normal symbol. The \(H\)-action is by left and right multiplication and is isometric. Every point of \(Z_p\) is in an \(H\)-orbit of one of these representatives. The assertion follows everywhere. \(\square\)

**Theorem 2.0s (archimedean generic eigendistribution symmetry).** Suppose \(D\) is a generalized function on \(G\) such that
\[
D(agb^{-1})=\chi(a,b)D(g),\qquad
(\Omega-\lambda)D=0
\tag{2.8m}
\]
for all \(a,b\in U\), in the sense of pullback, and some \(\lambda\in\mathbb C\). Then \(\tau^*D=D\).

*Proof.* The open stratum is \(C_{w_0}=UTw_0U\). Its \(H\)-stabilizers are trivial. In its coordinates, equivariance determines the \(U\times U\) variables and leaves an arbitrary generalized function on \(T\). This statement holds for distributions: in a coordinate product chart, divide by the smooth character in the orbit variables. All its derivatives in those variables are zero. A distribution with \(\partial_{x_j}D=0\) is independent of those variables, because every compact test of fibre integral zero is a sum of their derivatives. To see the latter in one dimension, the primitive \(\int_{-\infty}^x f(t)\,dt\) is compactly supported when \(\int f=0\); use this successively in a rectangular product chart, subtracting a fixed bump of integral one in each variable. The change from Lie-group coordinates to ordinary derivatives uses their invertible smooth coefficient matrix. This proves the asserted descent on the open stratum without a kernel or localization theorem.

Each \(t w_0\) is fixed by \(\tau\), since \(w_0\,{}^t(tw_0)w_0=t w_0\). The map \(\tau\) switches the two orbit variables and preserves their character. Its action on the parameter \(t\) is the identity. Thus \(\tau^*D=D\) there, including for nonsmooth generalized functions on \(T\).

Set \(E=D-\tau^*D\). It has the same equivariance and Casimir eigenvalue and is zero on the open stratum. Use the finite Bruhat open filtration. If \(E\) has already vanished on its preceding open terms, its next restriction is supported on the next stratum \(C_p\). Lemma 2.0q kills its incompatible part with all normal derivatives. Its support is then in \(Z_p\); for a nonrelevant permutation nothing remains. For a relevant boundary permutation \(p\ne w_0\), Lemma 2.0r and Lemma 2.0p applied to \(P=\Omega-\lambda\) kill it on \(Z_p\). Here \(Z_p\) is a submanifold of the ambient open set, not only of \(C_p\); the normal symbol is computed in \(T_gG/T_gZ_p\), as required. Induction through the finite filtration gives \(E=0\). \(\square\)

The preceding proof is the group-case Casimir mechanism. A freely accessible primary comparison is [Aizenbud–Gourevitch, *Vanishing of certain equivariant distributions on spherical spaces*, author manuscript, 19 July 2013, §2.2 and §3.3, PDF pages 2–4](https://www.wisdom.weizmann.ac.il/~aizenr/4Publications/non_deg_gel_van.pdf). Their more general spherical-space theorem also uses a singular-support integrability theorem. No such theorem is being used here: the explicit vector (2.8l) proves the required nonzero normal symbol for every relevant \(GL_n\) boundary stratum, and Lemma 2.0p proves the resulting vanishing.

#### Smoothing Hilbert distribution vectors

Let \((\pi,\mathcal H)\) be an actual strongly continuous unitary Hilbert representation of \(G\), and let \(V=\mathcal H^\infty\) carry its full smooth-vector topology. In that topology the seminorms are
\(\sum_{D\in S}\|d\pi(D)v\|\) for finite subsets \(S\subset U(\mathfrak g_\mathbb C)\). It suffices to take words in a fixed real Lie basis. Smoothness, completeness and the comparison with the actual local cusp model are proved in Theorems 1.11–1.13. The following elementary argument uses this topology rather than an unspecified globalization.

**Lemma 2.0t.** If \(\ell\in V'\) is a continuous linear functional, it is a finite sum of Hilbert vector functionals composed with Lie derivatives. For \(f\in C_c^\infty(G)\), convolution of the corresponding distribution vector is a member of \(\mathcal H^\infty\), continuously in \(f\). The same assertions hold for the conjugate Hilbert representation.

*Proof.* Continuity supplies finitely many words \(D_j\) and \(C\) with
\[
|\ell(v)|\le C\left(\sum_j\|d\pi(D_j)v\|^2\right)^{1/2}.
\tag{2.8n}
\]
The map \(v\mapsto(d\pi(D_j)v)_j\) has values in a finite Hilbert direct sum. Its indicated bounded functional extends to the closure of that image, and then by zero on its orthogonal complement. Here the Hilbert facts can be proved directly. A closed subspace has an orthogonal projection: a sequence minimizing the distance from a fixed vector is Cauchy by the parallelogram identity, and its limit is orthogonal to the subspace by varying the minimizer along any line in it. A nonzero bounded functional on a Hilbert space is represented by a vector: minimize the norm on the closed affine hyperplane where its value is one. The same parallelogram argument gives a minimizer orthogonal to its kernel, and subtracting the functional value times that minimizer gives the representation formula. The zero functional is immediate. Applying this construction in the finite direct sum gives vectors \(h_j\in\mathcal H\) realizing the functional. Thus \(\ell(v)\) is a sum of the Hilbert pairings of \(d\pi(D_j)v\) with \(h_j\), with the linear-variable convention fixed once and for all.

Integration by parts transfers a distribution derivative to an invariant derivative of \(f\). Consequently convolution of a finite-order distribution vector is a finite sum of terms \(\pi(D_j^\# f)h_j\), where \(D_j^\#\) is the corresponding invariant differential operator, with signs obtained from the ordinary integration-by-parts rule. Every such vector is smooth, because
\[
d\pi(A)\pi(f)h=\pi(A_L f)h,\qquad
\|\pi(A_L f)h\|\le \|A_L f\|_{L^1(G)}\|h\|.
\tag{2.8o}
\]
For a first-order word this follows by changing variables in \(\pi(\exp(tX))\pi(f)\) and differentiating the compact smooth test; induction treats every word. Difference quotients converge in the displayed \(L^1\) bound. This also gives continuity into every smooth-vector seminorm on a fixed compact support of \(f\).

No negative-Sobolev completion or elliptic estimate is needed: (2.8n) is a finite-order expression, and (2.8o) is the full smoothing estimate. Applying the same proof to the conjugate representation gives the last assertion. \(\square\)

Use the invariant bilinear pairing
\[
B:V\times W\longrightarrow\mathbb C,\qquad
W=\overline{\mathcal H}^{\,\infty}.
\tag{2.8p}
\]
The Hilbert form identifies the \(K\)-finite core of \(W\) with the algebraic admissible contragredient of that of \(V\). Theorem 1.13 proves this identification for the local cusp factors. It also follows directly: the orthogonal compact-type projector transfers across the Hilbert form, and Riesz on its finite-dimensional image gives exactly the admissible finite dual.

For \(\ell\in V'\), \(m\in W'\), let \(\pi(f)m\in V\) and \(\widetilde\pi(\check f)\ell\in W\) denote the smooth vectors supplied by Lemma 2.0t; here \(\check f(g)=f(g^{-1})\). The defining transposition identities give
\[
B(\pi(h)m,\widetilde\pi(\check f)\ell)
=\ell(\pi(f*h)m).
\tag{2.8q}
\]
Indeed they hold for ordinary Hilbert vectors by Fubini and invariance; the finite Lie-derivative expressions and compact integration by parts prove the same identity for distribution vectors. All integrations are over compact supports, and (2.8o) bounds them.

#### The convolution kernel argument on the full smooth spaces

Assume the \(K\)-finite core \(V_0\) is irreducible and admissible, as in the actual local factors of Theorem 1.13. Its conjugate core \(W_0\) is also irreducible and admissible. Compact-type projections separate vectors and the cores are dense: finite coefficient kernels on \(K\) approximate an identity neighbourhood kernel in any fixed finite collection of smooth seminorms. This is the actual Peter–Weyl proof in *Matrix coefficients and the Peter–Weyl theorem*, Theorem 4.1. The finite-dimensional compact corners imply scalar endomorphisms of the simple core: an endomorphism has an eigenvector on a nonzero corner, and its eigenkernel is the whole simple module.

The central element \(\Omega\) acts by a scalar on \(V_0\). It commutes with every compact component, because the trace form is invariant under the full group, including the disconnected real component. The finite-corner eigenvector argument just given makes it scalar there; density and continuity of differentiation extend the scalar identity to \(V\).

**Lemma 2.0u (the archimedean kernel argument).** Suppose \(0\ne m\in\operatorname{Hom}^{\mathrm{cont}}_U(W,\Psi^{-1})\). Then
\[
\dim\operatorname{Hom}^{\mathrm{cont}}_U(V,\Psi)\le1.
\tag{2.8r}
\]

*Proof.* Fix such an \(m\). For a nonzero \(\ell\in\operatorname{Hom}^{\mathrm{cont}}_U(V,\Psi)\), define
\[
T_{\ell,m}(f)=\ell(\pi(f)m),\qquad
A_\ell(f)=\widetilde\pi(\check f)\ell,\qquad
S_m(h)=\pi(h)m .
\tag{2.8s}
\]
Lemma 2.0t makes the first expression a continuous distribution on \(G\) and makes the other two actual smooth vectors. Their images contain the entire finite cores \(W_0,V_0\), respectively. Here is the precise argument for that assertion. Each image is stable under the group, by translating its test; it is stable under Lie differentiation, by differentiating that translation; and it is stable under any compact-type projector, by integrating the translates of its test over compact \(K\). That integral is still in \(C_c^\infty(G)\), with support contained in a compact \(K\)-translate of the original support. Its image is nonzero. For example, if \(A_\ell(f)=0\) for every \(f\), then \(\ell(\pi(f)v)=0\) for every \(v\in V\); compact approximate identities converge to \(v\) in its smooth topology, so \(\ell=0\). The argument for \(S_m\) is identical. Some compact-type projection of a nonzero image vector is nonzero. It lies in the image and in the appropriate finite core. Simplicity of that core, and stability under \((\mathfrak g,K)\), put the whole core in the image.

Equivariance of \(\ell,m\) gives the pullback law (2.8m) for \(T_{\ell,m}\). In function notation the left and right character factors are \(\Psi(a)\) and \(\Psi(b)^{-1}\) under \(g\mapsto agb^{-1}\); changing variables in the defining compact integral gives the same identity for its distribution. Central scalarity gives \((\Omega-\lambda)T_{\ell,m}=0\). Theorem 2.0s therefore makes \(T_{\ell,m}\) invariant under \(\tau\).

Put \(f^\tau(g)=f(\tau(g))\). Haar preservation and the antiautomorphism identity give
\((f*h)^\tau=h^\tau*f^\tau\), directly by changing the convolution variable. Invariance of \(T_{\ell,m}\) and (2.8q) yield
\[
B(S_m(h),A_\ell(f))
=B(S_m(f^\tau),A_\ell(h^\tau)).
\tag{2.8t}
\]
Because the image of \(S_m\) contains the dense core \(V_0\), the left side is zero for every \(h\) exactly when \(A_\ell(f)=0\). Because the image of \(A_\ell\) contains \(W_0\), the right side is zero for every \(h\) exactly when \(S_m(f^\tau)=0\). Nondegeneracy on the cores and compact projections justify both assertions, including for the actual smooth vectors. Thus
\[
\ker A_\ell=\{f:S_m(f^\tau)=0\},
\tag{2.8u}
\]
which is independent of the nonzero \(\ell\).

For \(\ell_1,\ell_2\ne0\), define a map between the two images by
\[
A(A_{\ell_1}(f))=A_{\ell_2}(f).
\tag{2.8v}
\]
The equality of kernels makes it well defined and bijective. It commutes with the group, Lie derivatives and compact-type projections, since the same translation, derivative and compact integral on \(f\) gives those actions for both maps. Each image contains \(W_0\). A compact-type projection has finite-dimensional range contained in \(W_0\); consequently \(A\) carries \(W_0\) to \(W_0\), and its restriction is an endomorphism of the simple admissible core. It is a nonzero scalar \(c\) there.

No claim that \(A_\ell\) is onto the full Fréchet space is being made. For any \(f\), commuting (2.8v) with each compact-type projection gives
\[
P_\delta A_{\ell_2}(f)=cP_\delta A_{\ell_1}(f).
\tag{2.8w}
\]
Those projections separate vectors, so the two smooth vectors themselves agree. Pairing with \(v\in V\) gives
\(\ell_2(\pi(f)v)=c\ell_1(\pi(f)v)\). A compact approximate identity converges to \(v\) in every smooth seminorm, proving \(\ell_2=c\ell_1\). This proves (2.8r). \(\square\)

**Theorem 2.0v (all-rank uniqueness for actual unitary and cuspidal models).** Let \(\pi\) be an actual unitary Hilbert representation with irreducible admissible \(K\)-finite core for \(GL_n(\mathbb R)\) or \(GL_n(\mathbb C)\), and use its full smooth-vector realization \(V\). For every nondegenerate continuous character \(\Xi:U\to\mathbb C^\times\),
\[
\dim\operatorname{Hom}^{\mathrm{cont}}_U(V,\Xi)\le1.
\tag{2.8x}
\]
The same bound holds after twisting \(\pi\) by any smooth determinant character. It therefore holds for every real and complex local cusp model supplied by Theorems 1.19 and 1.11–1.13, including a cuspidal representation before removing its real determinant norm twist.

*Proof.* First use \(\Psi\). If its Hom space is zero there is nothing to prove. Otherwise choose \(0\ne\ell\) in it. Hilbert conjugation supplies
\[
m(\bar v)=\overline{\ell(v)}\quad(\bar v\in W).
\tag{2.8y}
\]
This is a nonzero continuous linear functional on \(W\), with character \(\Psi^{-1}\). Lemma 2.0u applies. This argument proves the required opposite functional; it does not assume genericity of the contragredient.

Every continuous unitary additive character of \(\mathbb R\) is \(x\mapsto e^{2\pi i ax}\), and of \(\mathbb C\) is \(z\mapsto e^{2\pi i\operatorname{Re}(az)}\), for a unique real or complex \(a\), respectively. One elementary proof lifts the character on a small interval to its continuous argument, uses additivity there to make that argument linear, then subdivides an arbitrary input; the two real coordinate axes treat \(\mathbb C\). The commutator subgroup of \(U\) consists of the coordinates of height at least two: \([1+aE_{ij},1+bE_{jk}]=1+abE_{ik}\), and induction on height eliminates those coordinates. Hence a nondegenerate unitary character has the form \(\psi(\sum a_i u_{i,i+1})\), with all \(a_i\ne0\). A diagonal conjugation with \(d_i/d_{i+1}=a_i\) transports it to \(\Psi\). The continuous invertible operator \(\pi(d)\) transports the functional space.

If \(\Xi\) is not unitary, its absolute-value logarithm is a nonzero continuous additive real functional on \(U/[U,U]\). Additivity and continuity make it real linear: first on rational multiples, then on real multiples by continuity. Thus for some real direction \(X\) in a simple root line,
\(|\Xi(\exp(tX))|=e^{ct}\) with \(c\ne0\). A continuous Whittaker functional with a nonzero value on \(v\) would make \(|\ell(\pi(\exp(tX))v)|=e^{ct}|\ell(v)|\). This contradicts a polynomial bound in \(|t|\). That bound follows directly in the present smooth Hilbert model: unitarity and
\[
d\pi(D)\pi(u)v=\pi(u)d\pi(\operatorname{Ad}(u^{-1})D)v
\tag{2.8xa}
\]
express every derivative seminorm of \(\pi(\exp(tX))v\) as a finite sum bounded by polynomials in \(t\), since \(X\) is a nilpotent matrix and the adjoint exponential is a finite polynomial. A determinant twist is one on this root group. More generally the moderate-growth inequality (1.25b) gives the same polynomial bound in any actual moderate-growth model, because \(\exp(tX)=I+tX\) for this root direction. Let \(t\) tend to the infinity with \(ct>0\). Consequently every such nonunitary-character Hom space is zero. This completes (2.8x) for all the characters stated.

A determinant character is trivial on \(U\). Multiplying the group action by it therefore leaves the functional space and its topology unchanged. Its smooth-vector topology is the same: differentiation of the twist and its inverse expresses each set of derivative seminorms as finite combinations of the other. Thus the result persists under the stated twists.

Theorem 1.19 removes exactly a real determinant norm twist from an abstract cuspidal subquotient and supplies an actual admissible Hilbert constituent. Theorems 1.11–1.13 identify its full smooth local spaces and compatible conjugate duality. Applying the theorem to these local unitary factors and restoring the twists proves the final assertion. The local existence provided by Theorem 1.3 and Corollary 1.4 of *Automorphic representations and automorphic L-functions* then makes each of these cusp-model Hom spaces exactly one-dimensional for a nondegenerate unitary character. For a nonunitary character it is zero, as proved above. \(\square\)

### Continuous principal quotients and the general archimedean Whittaker bound

Throughout, \(k=\mathbb R\) or \(\mathbb C\), \(d=[k:\mathbb R]\),
\(G=GL_n(k)\), \(K=O(n)\) or \(U(n)\), \(B=MAN\) is the upper
triangular group, and \(\bar N\) is lower unitriangular. Haar measure
on \(K\) has mass one. Put
\[
 H(g)=\max(1,\|g\|_{\mathrm{op}},\|g^{-1}\|_{\mathrm{op}}),\qquad
 \rho_i=\frac d2(n+1-2i).
 \tag{2.10a}
\]
This height is submultiplicative, is one on \(K\), and bounds every
matrix coefficient of \(\operatorname{Ad}(g)\) by \(H(g)^2\).

The supplied model \(E\) is complete Hausdorff locally convex, with
a jointly continuous smooth \(G\)-action and continuous differentiated
actions. Its topology satisfies moderate growth: for every continuous
seminorm \(p\) there are a continuous seminorm \(q\), \(C,A\) such that
\[
 p(\pi(g)v)\le C H(g)^Aq(v).
 \tag{2.10b}
\]
Its compact-finite core \(E_0\) is admissible. We may assume either
that this core is irreducible or that \(E\) is topologically
irreducible; Lemma 2.0w below proves their equivalence here. A supplied
dual-pair model additionally has a model \(\widetilde E\) with the same
properties and a jointly continuous nondegenerate invariant bilinear
pairing; its core is the admissible contragredient of \(E_0\).
These hypotheses describe the actual spaces and actions. Theorem
1.34 constructs one such pair for every abstract irreducible admissible
core; these statements also apply to a separately prescribed pair. The cuspidal models in Theorems 1.19 and 1.11–1.13 of this lesson have
these properties.

The algebraic input used below is the written Theorem 1.28, equation
(1.34y), of *Nonzero minimal Jacquet quotients and actual algebraic
Borel occurrence*: for a supplied dual pair there is a full Borel
principal core \(P_0\) and a surjective
\((\mathfrak g,K)\)-map \(A_0:P_0\to E_0\).
Its finite-generation, bounded radial-system and nonvanishing proofs
are part of that input, not a citation to an unwritten occurrence
theorem. The analytic estimate used below is the written §§1–4 of
*Analytic core coefficients and comparison of actual smooth models*,
Theorem 1.29. Their full proofs are given in the preceding subsections.

We prove a continuous extension of \(A_0\) in the supplied topology.
Its image need only be dense: the transpose then embeds the *entire
continuous dual* into a distributional principal series. That is the
exact hypothesis of Corollary 2.0o, whose principal-series bound is
proved in Theorem 2.0n of the same lesson.

#### Irreducibility of the core follows in the actual model

**Lemma 2.0w.** In an actual smooth model as above with admissible
compact-finite core, topological irreducibility implies core
irreducibility. Conversely, core irreducibility implies
topological irreducibility.

The compact polynomial approximate identities (1.34d) prove core
density, and the compact character projector \(p_\tau\) has range
the entire finite-dimensional packet \(E_\tau\). Indeed its integral
has finite compact orbit by the finite matrix-coefficient formula;
thus every vector in its range belongs to the given admissible
core. Its range is finite-dimensional by admissibility.

For later use, compact-finite continuous functionals separate
points modulo any closed \(K\)-stable subspace \(W\).
If every \(p_\tau v\) belongs to \(W\), each class-polynomial
approximate identity applied to \(v\) belongs to \(W\): its finite
compact Fourier expansion is a finite sum of scalar character
projectors. Their convergence puts \(v\) in \(W\).
Otherwise, on some finite packet \(p_\tau v\notin W\cap E_\tau\),
choose a finite-dimensional linear functional zero on that
subspace and nonzero on \(p_\tau v\). Compose it with \(p_\tau\);
the result is a compact-finite continuous functional annihilating
\(W\) and detecting \(v\). No infinite-dimensional dual extension
theorem is required for this separation.

Suppose \(E\) is topologically irreducible. The quadratic invariant
Casimir \(C_G\) commutes with the full compact group and preserves
each finite packet. Choose an eigenvector \(v\ne0\) in one such
packet, with eigenvalue \(\mu\), and let
\(V=U(\mathfrak g)\operatorname{span}(Kv)\).
This is a nonzero \((\mathfrak g,K)\)-submodule of the core and
\(C_G=\mu\) on it. Let \(W=\overline V\) in the actual topology.
It is closed and \(K\)-stable.

For any compact-finite continuous \(\eta\) annihilating \(W\),
and any \(u\in V\), the scalar coefficient
\(\eta(\pi(g)u)\) is analytic on \(G\). To verify the precise
input, split \(u\)'s finite compact orbit into compact-Casimir
eigenvectors \(\kappa\). Each coefficient solves
\((\Delta-\mu+2\kappa)f=0\) with the analytic elliptic
operator (2.10ad). The written scalar regularity proof in
Theorem 1.29 §§1–3 therefore applies. It requires the Casimir
scalar on \(u\), not irreducibility of the ambient model.
All Lie jets at identity vanish, since every derivative of
\(u\) remains in \(V\). Thus the Taylor series is zero near
identity and analyticity gives zero on the whole identity
component. The other real component is reached by an element
of \(K\), which preserves \(V\), so the coefficient is zero
there too.

The separation argument just proved implies
\(\pi(g)V\subset W\) for every \(g\). Continuity gives
\(\pi(g)W\subset W\); applying the inverse gives equality.
Topological irreducibility now forces \(W=E\).
For every packet,
\[
 p_\tau E=p_\tau\overline V
       \subset\overline{p_\tau V}=p_\tau V.
\]
The final equality holds because \(p_\tau V\) is a subspace
of a finite-dimensional packet. Hence \(E_0=V\), and
\(C_G=\mu\) on the entire core.

Given any nonzero core submodule \(U\), repeat the same
analytic annihilator argument: the Casimir is already scalar
on \(U\), so \(\overline U\) is group-stable. It equals \(E\);
finite packet projection then gives \(U=E_0\).
This proves core irreducibility. Conversely a nonzero closed
group-stable subspace has a nonzero core vector by compact
approximation. Its core is Lie- and compact-stable, so core
irreducibility puts every core vector in it. Density then
makes that closed subspace all of \(E\). This proves the
converse and the lemma.

#### Compact estimates with polynomial constants

Let \(\tau\) run through irreducible compact representations,
\(d_\tau=\dim\tau\), and let \(\kappa_\tau\ge0\) be the scalar of the
positive compact Casimir
\(C_K=-\sum X_j^2\), for an invariant orthonormal basis of the compact
Lie algebra. On \(O(n)\) the same construction is used on each of its
two components. For \(n=1\), its finite compact group causes no
spectral issue.

The actual earlier proof of Schur orthogonality and Peter–Weyl is
*Matrix coefficients and the Peter–Weyl theorem*, Theorem 4.1 and
its preceding orthogonality proof.
We supply the additional estimates needed here.

There is an integer \(s\) and a constant \(C_s\) such that
\[
 \sum_{\kappa_\tau\le R}d_\tau^2\le C_s(1+R)^s.
 \tag{2.10c}
\]
Indeed a local coordinate cutoff, Fourier inversion and
Cauchy–Schwarz with the integrable weight
\((1+|\xi|^2)^{-s}\), \(s>\dim K/2\), give
\(\|f\|_\infty\le C\sum_{j\le s}\|D^jf\|_2\).
A finite coordinate cover replaces coordinate derivatives by words
in the \(X_j\)'s, with bounded coefficients. Fourier inversion here
can be justified by inserting \(e^{-\epsilon|\xi|^2}\), evaluating
the Gaussian, and taking the resulting approximate-identity limit.
For a finite combination of compact coefficients with
\(\kappa_\tau\le R\),
\[
 \sum_j\|X_jf\|_2^2=\langle C_Kf,f\rangle\le R\|f\|_2^2.
\]
The Casimir commutes with every \(X_j\), so iteration bounds every
word of length \(j\) by \(R^{j/2}\|f\|_2\).
Thus evaluation on this coefficient space has norm at most
\(C(1+R)^{s/2}\). For any finite orthonormal coefficient list
\(\phi_1,\ldots,\phi_M\), the square of that evaluation norm is
\(\sum_\nu|\phi_\nu(x)|^2\). Integrating gives
\(M\le C^2(1+R)^s\). Apply this to successively larger finite lists
from the Peter–Weyl basis; the same bound forces the entire list
below \(R\) to be finite and proves (2.10c).

Write \(P=P_{\lambda,\sigma}\) for the complete compact-smooth
principal model
\[
 P=\{q\in C^\infty(K):q(mk)=\sigma(m)q(k)\},\qquad
 F(ua mk)=a^{\lambda+\rho}\sigma(m)q(k).
 \tag{2.10d}
\]
Here \(\sigma\) is any smooth character of \(M\), and
\(\lambda\in\mathbb C^n\); the real positive diagonal powers use
ordinary real logarithms. The action is right translation of \(F\).
Row Gram–Schmidt constructs its action and topology explicitly.
All its compact derivatives satisfy (2.10b): Gram determinants of
rows of \(kg\), and their inverses, are bounded by fixed powers of
\(H(g)\); differentiation of the row-QR formulas only introduces
further such powers. Thus each compact \(C^r\) seminorm is bounded
by \(C_rH(g)^{A_r}\) times a compact \(C^r\) seminorm of \(q\).

The \(\tau\)-packet \(P_\tau\) is \(U_\tau\otimes\mathbb C^{m_\tau}\),
where \(m_\tau=\dim\operatorname{Hom}_M(U_\tau,\sigma)\le d_\tau\).
For completeness, a \(K\)-map \(U_\tau\to P\) is determined by
evaluation at the identity; that evaluation is an \(M\)-covariant
functional. Conversely its matrix coefficient defines the map,
giving this multiplicity identity. Put \(D_\tau=d_\tau m_\tau\).
Evaluation has norm \(\sqrt{D_\tau}\): its squared norm is constant
on the transitive compact flag, and the integral of that square,
computed in an orthonormal basis of \(P_\tau\), is \(D_\tau\).
Consequently
\[
 \|q_\tau\|_{C^r}\le C_r\sqrt{D_\tau}
                 (1+\kappa_\tau)^{r/2}\|q_\tau\|_2.
 \tag{2.10e}
\]
One may choose a basis of the \(M\)-covariant subspace of \(U_\tau\)
so that the evaluation Riesz vector, viewed as a
\(d_\tau\)-by-\(m_\tau\) matrix, is
\[
 d_\tau^{\,\mathrm{ev}}
     =\sqrt{d_\tau}\,[u_1\ \cdots\ u_{m_\tau}],
 \quad u_i\text{ orthonormal}.
 \tag{2.10f}
\]
This follows directly from the orthogonality norm
\(\int_K|\langle\tau(k)u,v\rangle|^2dk
 =\|u\|^2\|v\|^2/d_\tau\), applied to the multiplicity basis.
We take the \(L^2\) inner product linear in its first argument, so
\(\langle d_\tau^{\,\mathrm{ev}},q\rangle=\overline{q(1)}\).

Every \(q\in P\) has rapid compact-packet coefficients. Precisely,
for every \(R\),
\[
 \sum_\tau(1+\kappa_\tau)^R\|q_\tau\|_2
       \le C_R\|(1+C_K)^{b_R}q\|_2
 \tag{2.10g}
\]
for some integer \(b_R\). To prove it, apply Cauchy–Schwarz to
the sum with a factor \((1+\kappa_\tau)^{-a}\); (2.10c), grouped
in dyadic intervals, makes its square summable for large \(a\).
Orthogonality identifies the second square sum with the right
side for \(b_R\ge R+a\). Equations (2.10e) and (2.10g) also prove
convergence of the packet expansion in every \(C^\infty\)
seminorm, with continuous bounds. No compact highest-weight
classification or Weyl dimension formula is needed.

#### A single compact-finite vector concentrating at a flag

Write \(x_{ij}\), \(i>j\), for the matrix coordinates on \(\bar N\),
and \(m=d n(n-1)/2\) for its real dimension. Lebesgue measure in
these coordinates is Haar measure: multiplication is triangular
with all diagonal Jacobian entries one. For \(1\le r<n\), let
\[
 Q_r(x)=\det\operatorname{Gram}(\text{last }r\text{ rows of }x),
 \quad Q_0=Q_n=1.
 \tag{2.10h}
\]
Cauchy–Binet expresses this as the sum of squared absolute values
of all last-row minors, so \(Q_r\ge1\).
In row-QR \(x=u(x)a(x)k(x)\) with upper \(u\), positive diagonal
\(a\) and \(k\in K\), the last \(r\) rows span exactly the last
\(r\) orthonormal rows. Hence
\[
 Q_r(x)=\prod_{j=n-r+1}^na_j(x)^2.
 \tag{2.10i}
\]
The trailing \(r\)-minor of \(k(x)\) is
\(\prod_{j=n-r+1}^na_j(x)^{-1}\), a positive real number:
upper row operations preserve the bottom-row determinant and
the trailing minor of \(x\) is one.

Set
\[
 h(k)=\prod_{r=1}^{n-1}
       |\det k_{\{n-r+1,\ldots,n\},\{n-r+1,\ldots,n\}}|^2.
 \tag{2.10j}
\]
It is a polynomial in matrix entries and their conjugates,
is \(M\)-invariant on the left, is compact-finite, and \(h(1)=1\).
On the \(\bar N\) chart, \(h(k(x))=\prod_rQ_r(x)^{-1}\).
For \(i=n-r+1\), the minor using columns \(j,i+1,\ldots,n\),
\(j<i\), is \(x_{ij}\): its first row has zeros in the later
columns and the remaining triangular block has determinant one.
Together with the trailing minor, this proves
\[
 Q_{n-i+1}(x)\ge1+\sum_{j<i}|x_{ij}|^2,\qquad
 h(k(x))\le(1+|x|^2)^{-1}.
 \tag{2.10k}
\]
Each \(Q_r\) is polynomial, at least one, and at most a fixed
power of \(1+|x|\). Formula (2.10i) therefore bounds \(a_j\) and
\(a_j^{-1}\) by powers of \(1+|x|\).

The character of \(M\) has signs \(\epsilon_i\in\{0,1\}\) over
\(\mathbb R\), or integer circle weights \(l_i\) over \(\mathbb C\).
The circle assertion follows by differentiating its scalar
one-parameter character and imposing period \(2\pi\).
Choose
\[
 f_0(k)=\prod_i k_{ii}^{\epsilon_i}\quad(\mathbb R),\qquad
 f_0(k)=\prod_i k_{ii}^{\max(l_i,0)}
                    \overline{k_{ii}}^{\max(-l_i,0)}
                                             \quad(\mathbb C).
 \tag{2.10l}
\]
Then \(f_0(mk)=\sigma(m)f_0(k)\), \(f_0(1)=1\), and
\(|f_0|\le1\). Polynomial degree is preserved under compact
translation, so it is compact-finite. For a large fixed integer
\(L\), put
\[
 \xi(k)=f_0(k)h(k)^L,\qquad
 \xi_{\bar N}(x)=a(x)^{\lambda+\rho}f_0(k(x))h(k(x))^L.
 \tag{2.10m}
\]
By (2.10k), \(L\) can make the latter decay by any *fixed*
required power. We choose it below with sufficiently many
integrable moments. The same fixed \(\xi\) is used for all
compact packets.

We can also require
\[
 I_\xi=\int_{\bar N}\xi_{\bar N}(x)\,dx\ne0.
 \tag{2.10n}
\]
Here is a proof that cancellation does not obstruct this choice.
Write \(\phi(x)=a(x)^{\lambda+\rho}f_0(k(x))\); it is continuous,
equals one at zero, and has polynomial growth.
The positive density \(h(k(x))^L dx\), after normalization,
concentrates at zero as \(L\to\infty\).
Outside \(|x|<\epsilon\), (2.10k) bounds \(h\) by
\(\theta_\epsilon<1\); keep a fixed integrable power \(h^{L_0}\)
to dominate both \(1\) and \(|\phi|\), and the exterior integral
is \(O(\theta_\epsilon^{L-L_0})\).
Near zero the smooth nonnegative \(h\) has maximum one, so
\(h(k(x))\ge1-C|x|^2\). The integral on
\(|x|\le L^{-1/2}\) is at least \(cL^{-m/2}\), after reducing
the ball by a fixed factor. The exterior mass divided by this
lower bound tends to zero. On the interior \(\phi\) tends
uniformly to one as \(\epsilon\to0\).
Thus \(I_\xi/\int h(k(x))^Ldx\to1\), proving (2.10n) for all
sufficiently large \(L\), together with the desired moments.

We record the measure factor to fix the sign in this construction:
\[
 dk=a(x)^{2\rho}\,dx
 \quad\text{on the open flag chart }M\backslash K.
 \tag{2.10o}
\]
A positive constant is absorbed into \(dx\).
For an elementary verification, matrix Haar measure is
\(|\det g|_k^{-n}d_{\mathrm{Leb}}g\); direct multiplication
shows both left and right invariance. On the Gauss chart
\(g=u a m x\), elimination starting with the bottom pivot
gives the Lebesgue Jacobian
\(\prod_j a_j^{\,2d(j-1)}\) in the diagonal-entry and
upper/lower-entry coordinates. One obtains this inductively:
the final column entries above the bottom pivot and final row
entries to its left contribute \(a_n^{d(n-1)}\) each, and
their Schur complement leaves the \((n-1)\)-matrix calculation.
Passing from diagonal Lebesgue measure to \(da_j/a_j\), with
the polar circle measure when \(d=2\), yields
\(\prod_j a_j^{d(2j-n-1)}=a^{-2\rho}\).
Thus \(dg=a^{-2\rho}\,du\,da\,dm\,dx\).
In Iwasawa coordinates \(g=u'a'k\) the upper
triangular Jacobian gives \(dg=(a')^{-2\rho}du'\,da'\,dk\).
At a positive diagonal matrix, each pair of off-diagonal
positions is parametrized by an upper entry and a
skew-adjoint compact entry; its real Jacobian is
\(a_j^{2d}\) for \(i<j\). The diagonal radial and compact
phase directions supply the usual polar factors.
Their product is precisely the Gauss Jacobian just computed;
left upper translation and right compact translation
propagate it to all Iwasawa charts.
Substitute \(x=u(x)a(x)k(x)\); the upper translation Jacobian
is one and \(a'=aa(x)\). Comparing the two formulas gives
(2.10o). The complements of these charts are zeros of
nonzero minors and have measure zero. This calculation also
proves invariance of the compact integral pairing between
\(P_{\lambda,\sigma}\) and \(P_{-\lambda,\sigma^{-1}}\).

For \(t\ge1\), put
\[
 Y_i=(n+1)/2-i,\quad
 a_t=\operatorname{diag}(t^{Y_i}),\quad
 C_t(x)=a_t^{-1}xa_t,\quad
 b_t=a_t^{\lambda-\rho}I_\xi.
 \tag{2.10p}
\]
The coordinate \(x_{ij}\) is multiplied by \(t^{i-j}\).
Thus \(C_t\) has Jacobian \(a_t^{2\rho}\) and
\(|C_t^{-1}x|\le t^{-1}|x|\). Right translation in (2.10d)
and (2.10o) give, for \(q\in P_\tau\),
\[
 \frac{\langle P(a_t)\xi,q\rangle}{b_t}
 = I_\xi^{-1}\int_{\bar N}
    \xi_{\bar N}(y)\,
    a(C_t^{-1}y)^{\rho-\lambda}
    \overline{q(k(C_t^{-1}y))}\,dy.
 \tag{2.10q}
\]
In particular this tends to \(\overline{q(1)}\), with a
polynomial bound uniform in \(\tau\):
\[
 \left\|
 \frac{P_\tau P(a_t)\xi}{b_t}
       -d_\tau^{\,\mathrm{ev}}\right\|_2
 \le C\sqrt{D_\tau}(1+\sqrt{\kappa_\tau})t^{-1/2}.
 \tag{2.10r}
\]
To verify the bound, split the integral at \(|y|=\sqrt t\).
On the interior, row-QR is smooth at zero, the weight is
\(1+O(|C_t^{-1}y|)\), and (2.10e) bounds the change of \(q\)
by \(C\sqrt{D_\tau}(1+\sqrt{\kappa_\tau})t^{-1/2}\|q\|_2\).
On the exterior, the weight in (2.10q) is bounded by
\(C(1+|y|)^a\), uniformly for \(t\ge1\), by (2.10i).
Choose \(L\) in (2.10m) so that
\(\int|\xi_{\bar N}(y)|(1+|y|)^{a+2}dy<\infty\).
The exterior integral is then at most
\(Ct^{-1}\sqrt{D_\tau}\|q\|_2\); the same estimate controls
the discarded constant \(q(1)\). Taking the supremum over
unit \(q\in P_\tau\) proves (2.10r).

#### Exact compact-packet synthesis by group tests

Only packets with \(m_\tau>0\) are used; zero packets are omitted.
Choose once and for all
\(t_\tau=T(1+\kappa_\tau)^b\), where \(T,b\) are large enough
that the right side of (2.10r) is at most
\(\sqrt{d_\tau}/2\). This is possible by (2.10c) and
\(m_\tau\le d_\tau\). Let
\[
 X_\tau=P_\tau P(a_{t_\tau})\xi.
 \tag{2.10s}
\]
View it as a \(d_\tau\)-by-\(m_\tau\) matrix in (2.10f).
Its smallest column singular value is at least
\(|b_{t_\tau}|\sqrt{d_\tau}/2\).
For a target matrix \(Q\in P_\tau\), define
\[
 T_{\tau,Q}=Q(X_\tau^*X_\tau)^{-1}X_\tau^*.
 \tag{2.10t}
\]
Then \(T_{\tau,Q}X_\tau=Q\), linearly in \(Q\), and
\(\|T_{\tau,Q}\|_{\mathrm{HS}}
 \le2\|Q\|_2/(|b_{t_\tau}|\sqrt{d_\tau})\).
The compact Fourier kernel
\[
 k_{\tau,Q}(k)=d_\tau
                 \operatorname{tr}(T_{\tau,Q}\tau(k^{-1}))
 \tag{2.10u}
\]
acts as \(T_{\tau,Q}\) on \(U_\tau\), and zero on all other
compact types, by Schur orthogonality. The same orthogonality
gives
\[
 \|k_{\tau,Q}\|_1\le\|k_{\tau,Q}\|_2
   =\sqrt{d_\tau}\|T_{\tau,Q}\|_{\mathrm{HS}}
   \le2|b_{t_\tau}|^{-1}\|Q\|_2.
 \tag{2.10v}
\]
Both \(H(a_{t_\tau})\) and \(|b_{t_\tau}|^{-1}\) are bounded
by fixed powers of \(1+\kappa_\tau\), because \(t_\tau\) is
such a power and \(|a_t^{\lambda-\rho}|\) is a fixed real
power of \(t\).

We need one exact smooth group kernel fixing \(\xi\).
Let \(W\) be the sum of the *entire* compact isotypic packets
containing \(\xi\). It is finite-dimensional; using only its
compact orbit span would not ensure invariance under the kernel.
Average a compact smooth approximate identity on \(G\) under
compact conjugation. The resulting \(h_\epsilon\) commutes
with \(K\), preserves \(W\), and tends to identity on \(W\).
For small \(\epsilon\), \(P(h_\epsilon)|_W\) is invertible.
Its characteristic polynomial, with nonzero constant term,
expresses identity on \(W\) as a polynomial in
\(P(h_\epsilon)|_W\) with zero constant term.
The corresponding finite linear combination of positive
convolution powers is \(h_0\in C_c^\infty(G)\), with
\(P(h_0)\xi=\xi\).

Define the smooth compactly supported group function
\[
 f_{\tau,Q}=k_{\tau,Q}*\delta_{a_{t_\tau}}*h_0,
 \qquad P(f_{\tau,Q})\xi=Q.
 \tag{2.10w}
\]
The first convolution is integration on \(K\); the point
mass in the second one is merely left translation of \(h_0\).
Its support lies in \(K a_{t_\tau}\operatorname{supp}h_0\).
For every right Lie word \(D\) and integer \(R\ge0\),
right differentiation transfers to \(h_0\), giving
\[
 \int_G H(g)^R|R_Df_{\tau,Q}(g)|\,dg
       \le C_{R,D}(1+\kappa_\tau)^{a_{R,D}}\|Q\|_2.
 \tag{2.10x}
\]
Here (2.10v), submultiplicativity of \(H\), and the fixed
weighted derivative integrals of \(h_0\) prove the bound.
Left derivative words satisfy bounds of the same form:
express a left vector field through right vector fields
using \(\operatorname{Ad}(g^{-1})\), whose coefficients are
bounded by \(H(g)^2\). Differentiating these coefficients
introduces only further fixed powers of \(H\).

Let \(\mathcal S_H(G)\) have all seminorms
\(\int H^R|R_Df|\), for all \(R,D\).
The series
\[
 s(q)=\sum_\tau f_{\tau,q_\tau}
 \tag{2.10y}
\]
converges in every such seminorm by (2.10g) and (2.10x);
the resulting map \(s:P\to\mathcal S_H(G)\) is linear and
continuous. There is an actual smooth function behind the
series. On a compact coordinate set, left/right invariant
derivatives span coordinate derivatives with bounded coefficients.
The elementary \(L^1\) local estimate obtained by repeated
one-dimensional fundamental theorem of calculus bounds a
supremum by the \(L^1\) norms of coordinate derivatives through
order \(\dim G+1\), after a fixed cutoff. It makes the series
and each fixed derivative uniformly Cauchy there. Its smooth
local limits agree, and the weighted \(L^1\) bounds pass to the
limit by Fatou. This also verifies completeness for the limits
being used, without an imported Schwartz-space theorem.

For any actual model satisfying (2.10b), the action
\(\pi(f)v=\int f(g)\pi(g)v\,dg\) exists for
\(f\in\mathcal S_H(G)\). On compact sets it is the limit of
Riemann sums in the complete locally convex space; outside
those sets (2.10b) bounds the tail in each seminorm by
\(Cq(v)\int H^A|f|\). The resulting net is Cauchy and its
limit is independent of the cutoffs. Thus
\[
 p(\pi(f)v)\le Cq(v)\int H^A|f|.
 \tag{2.10z}
\]
Changing variables under a one-parameter translation transfers
differentiation to \(f\); (2.10x) and its left-derivative version
justify the difference-quotient limit in every seminorm.
This proves all differentiated action formulas and continuity.
Applying it to \(P\), (2.10w), (2.10y), and smooth packet
convergence prove the exact identity
\[
 P(s(q))\xi=q \qquad(q\in P).
 \tag{2.10aa}
\]
This is an explicitly proved principal-series universal estimate,
including support, derivative and topology control.
For \(n=1\), \(M=K\) and \(P\) is one-dimensional; choose
\(\xi=\sigma\), one compact smooth kernel acting nontrivially
on its character and rescale it. Equations (2.10y)–(2.10aa)
then hold with a single packet. This covers that rank directly.

#### Continuous extension of every principal-core map

**Theorem 2.0x.** Let \(A_0:P_0\to E_0\) be a
\((\mathfrak g,K)\)-map, where \(E\) is a supplied model
as above. It has a continuous \(G\)-equivariant extension
\[
 A:P\longrightarrow E,\qquad
 A(q)=\pi(s(q))A_0(\xi).
 \tag{2.10ab}
\]
If \(A_0\) is surjective, \(A(P)\) contains \(E_0\) and
is dense in \(E\).

We first verify the coefficient identity needed to prove that
(2.10ab) extends the stated map, rather than an unrelated one.
The quadratic invariant Casimir \(C_G\) of the real trace form
(real part over \(\mathbb C\)) acts by a scalar on a full
Borel principal series. Here is the algebraic verification.
Its complexified expression is a sum of diagonal squares
and pairs \(E_{ij}E_{ji}+E_{ji}E_{ij}\), with fixed nonzero
normalizing constants; in the complex case apply this in the
two matrix summands. Left upper-root derivatives kill an
inducing function and left diagonal derivatives are its
fixed inducing scalars. Reorder each root pair to place the
upper derivative on the right. The other term differs by
the diagonal commutator \(E_{ii}-E_{jj}\), with the sign
fixed by the anti-representation convention for left
derivatives. The remaining diagonal polynomial is a scalar.
Finally the left and right quadratic operators agree:
the left field \(L_X\) at \(g\) is the right field
with parameter \(\operatorname{Ad}(g^{-1})X\). Along its
own curve \(\exp(tX)g\) that parameter is constant, since
\(\operatorname{Ad}(\exp(-tX))X=X\).
Thus its square introduces no coefficient-derivative term.
Summing those squares with the trace-form signs leaves
the same quadratic tensor, by its adjoint invariance.
Thus the right Casimir
has that same scalar on \(P\).
If \(A_0\ne0\), it intertwines this scalar with the scalar
on the irreducible core \(E_0\); the latter follows also by
the finite-packet eigenvector argument. If \(A_0=0\) the
assertion is immediate.

Let \(\eta\) be a compact-finite continuous functional on \(E\).
It is supported on finitely many compact packets. Therefore
\(\eta A_0\) on \(P_0\) has a continuous extension \(\eta_P\)
to \(P\): compose the finite sum of packet projectors with
the appropriate finite-dimensional functional.
For every core vector \(u\in P_0\), we claim
\[
 \eta(\pi(g)A_0u)=\eta_P(P(g)u)\qquad(g\in G).
 \tag{2.10ac}
\]
All Lie derivatives at identity agree because \(A_0\) is
a core intertwiner. Both scalar functions are analytic.
In detail, decompose \(u\) into its finitely many compact
Casimir eigencomponents \(\kappa\). The right coefficient
of each component solves
\[
 (\Delta-\mu+2\kappa)f=0,\qquad
 \Delta=C_G-2C_K=\sum P_i^2+\sum K_j^2,
 \tag{2.10ad}
\]
an elliptic scalar equation with analytic matrix-coordinate
coefficients. The interior Fourier estimate, cutoff gradient
estimate, nested-ball induction and factorial Taylor bound
in §§1–3 of the written Theorem 1.29 prove analyticity of
every smooth solution of this equation. That proof uses
the scalar equation and a fixed compact packet; it does
*not* require irreducibility of the ambient principal series.
It therefore applies to both sides here. Matched Taylor
jets give equality near identity; overlapping analytic
coordinate balls give it throughout the identity component.
The second component over \(\mathbb R\) is a compact sign
matrix times that component, and the matched \(K\)-actions
give equality there too. This proves (2.10ac) without
assuming continuity of \(A_0\).

Continuity of (2.10ab) follows directly from (2.10z) and
continuity of \(s\). Integrating (2.10ac) with \(u=\xi\)
against \(s(q)\), and using (2.10aa), gives
\[
 \eta(Aq)=\eta_P(q).
 \tag{2.10ae}
\]
For a core \(q\), the right side is \(\eta(A_0q)\).
Compact-finite continuous functionals separate points of
\(E\): each finite packet has all its linear functionals
continuous, through its continuous character projector;
if all packets of a vector vanish, the polynomial compact
approximate identities in (1.34d) converge to that vector
and have zero output. Thus (2.10ae) proves \(Aq=A_0q\)
on the whole core.

For a general \(g\in G\), pair \(\pi(g)Aq\) with the same
\(\eta\), use (2.10ac) at \(gh\) under the integral defining
(2.10ab), and obtain \(\eta_P(P(g)q)\). Equation (2.10ae)
applied to \(P(g)q\) gives that same number for \(A(P(g)q)\).
Separation proves \(G\)-equivariance. Compact core density
follows from (1.34d), so a surjective core map has dense
image, as asserted. Uniqueness of the continuous extension
also follows from core density.

Neither surjectivity on the full supplied smooth space nor
closed image is needed or asserted in this theorem.

#### The entire continuous dual embeds

**Theorem 2.0y.** For every supplied irreducible admissible
moderate smooth dual-pair model \(E\), there is a particular
injective equivariant map
\[
 A':E'\hookrightarrow P',
 \qquad A'(\ell)(q)=\ell(Aq).
 \tag{2.10af}
\]
Here \(E'\) is its *full continuous dual*, with
\((g\ell)(v)=\ell(g^{-1}v)\), and \(P'\) is the distributional
principal series dual to (2.10d), namely
\(I^{-\infty}_{-\lambda,\sigma^{-1}}\).

Use the surjective principal-core map \(A_0:P_0\to E_0\) already
constructed in (1.34y), and apply Theorem 2.0x to it. The resulting \(A\) has dense image. Thus a
continuous \(\ell\) annihilating \(A(P)\) annihilates \(E\),
which proves injectivity. Equivariance follows by applying
the equivariance of \(A\) in (2.10ab) to \(g^{-1}q\).
Every \(\ell A\) is continuous on the compact \(C^\infty\)
model, hence is an actual distribution on its compact
flag line bundle; this is the definition of \(P'\).
The dual parameter and action follow from the invariant
compact integral pairing verified in (2.10o).
To identify this with the exact convention in (2.7a),
first extend a distribution in the compact model to a
generalized function on \(G\) with the *upper* covariance
\(F(ua mk)=a^{-\lambda+\rho}\sigma(m)^{-1}F(k)\).
Locally a flag section and upper coordinates identify
the relevant bundle with a product: tensor its distribution
with that smooth upper character. Changes of sections
give exactly the compact line-bundle transition factors,
so these products patch to a generalized function.
Right translation induces the dual compact action.
This can be checked on smooth sections by (2.10o);
compact-coordinate smoothing approximates any distribution
weakly: convolution with a compact integral-one mollifier
transposes to convolution of a test density, which converges
with every derivative on a fixed compact neighborhood.
Distribution continuity gives the limit; a finite coordinate
partition of unity patches these smooth approximants.
Continuous pullback on test densities passes
the identity to their limit. Thus it holds for the full
distribution space.
Let \(w_0\) reverse the basis order, and put
\[
 (\mathcal JT)(x)=T(w_0x),\qquad
 \chi_T(b)=a(w_0bw_0^{-1})^{-\lambda+\rho}
              \sigma(m(w_0bw_0^{-1}))^{-1}
 \quad(b\in\bar B).
 \tag{2.10afa}
\]
Upper unipotents are ignored in this character.
Left pullback \(\mathcal J\) is an isomorphism, commutes
with every right translation, and exchanges the upper
covariance with this lower covariance. Consequently
\(\mathcal J A':E'\hookrightarrow I^{-\infty}(\chi_T)\)
is literally the map required by (2.7m), with the same
upper group \(N\) and no change to its character.
No assertion about abstract algebraic duals is substituted
for this distributional embedding.

The construction even gives continuity for the strong dual
topologies: continuous linear \(A\) takes bounded sets to
bounded sets, so each strong-dual seminorm of \(\ell A\)
is the corresponding bounded-set seminorm of \(\ell\).
The weaker linear-equivariant conclusion is already enough
for Corollary 2.0o.

There is a useful additional smooth comparison, with a precise
limitation. The supplied \(\widetilde E\) embeds continuously
into the *smooth* dual principal model by
\[
 j(w)(q)=B_E(Aq,w).
 \tag{2.10ag}
\]
Joint continuity gives
\(|j(w)(q)|\le C r(w)\|q\|_{C^a}\) for a fixed integer \(a\)
and a fixed continuous seminorm \(r\) on \(\widetilde E\).
This is a fixed distribution-order bound for *every* \(w\).
Invariance transfers any compact-Casimir power to \(w\)
while retaining exactly that order. With (2.10e), it gives
\[
 (1+\kappa_\tau)^b\|j(w)_\tau\|_2
 \le C(1+\kappa_\tau)^c
                      r((1+C_K)^bw).
 \tag{2.10ah}
\]
Given any compact derivative order, choose \(b\) larger
than \(c\), that order, and the polynomial counting exponent
in (2.10c). Equations (2.10e) and (2.10ah), summed in dyadic
intervals, make the compact series and its derivatives
absolutely uniformly convergent. They bound that smooth
seminorm by the single continuous seminorm
\(Cr((1+C_K)^bw)\). Thus (2.10ag) is a continuous map into
\(P_{-\lambda,\sigma^{-1}}\), not merely into distributions.
Its injectivity follows from nondegeneracy of \(B_E\) and
density of \(A(P)\). Its core map is exactly the transpose
of \(A_0\). Swapping the supplied dual pair gives the
analogous smooth principal embedding of \(E\), including
continuity of the selected Borel eigenfunctional obtained
by evaluation at identity.

This proof uses a fixed-order estimate for every differentiated
vector. Smooth dependence of an orbit in the strong distribution
topology alone would not imply smoothness of its distribution:
point masses already have smooth translated orbits there.
We have not made that incorrect identification. Closed range,
a continuous inverse on the image, or smoothing an arbitrary
functional on \(E\) into the prescribed \(\widetilde E\) do
not follow just from (2.10ag); none is used in (2.10af).

#### General uniqueness in the supplied topology

**Theorem 2.0z.** Let \(E,\widetilde E\) be any supplied models
as above. For every nondegenerate continuous unitary character
\(\Psi:N\to\mathbb C^\times\),
\[
 \dim\operatorname{Hom}^{\mathrm{cont}}_N(E,\Psi)\le1.
 \tag{2.10ai}
\]
This includes nongeneric models, whose space may be zero.
It holds in every rank for both real and complex fields,
without unitarity of the representation or a determinant
twist reduction.

A Whittaker functional is precisely \(\ell\in E'\) with
\(n\ell=\Psi(n)^{-1}\ell\). The actual injective map (2.10af)
followed by (2.10afa) puts its space into the corresponding eigendistributions
of one full principal series. Theorem 2.0n proves that
space has dimension at most one, including all transverse
boundary jets, and Corollary 2.0o is its stated transport
argument. Applying it proves (2.10ai).
The standard-character convention entails no restriction:
every nondegenerate unitary character has nonzero real
simple-root coefficients over \(\mathbb R\), or nonzero
complex coefficients in the real trace pairing over
\(\mathbb C\). Conjugation by a diagonal matrix makes
these coefficients the fixed standard ones, solving the
successive ratios of its diagonal entries. It preserves
dimension of the Hom space.

For a continuous *nonunitary* character the Hom space is
zero in the same moderate models. Such a character has
on some real elementary-root one-parameter subgroup
\(u(t)\) the value \(e^{ct}\) with \(\Re c\ne0\).
Indeed choose a continuous logarithm of the character
near zero. On a smaller interval its additivity defect
is a continuous \(2\pi i\mathbb Z\)-valued function
vanishing at zero, hence is zero. Its local additive
law, first on rationals and then by continuity, gives
the logarithm \(ct\), and subdividing any interval gives
the exponential on all of \(\mathbb R\). Its
real-logarithm homomorphism is nonzero on some generator
when the character is nonunitary. The elementary-root
subgroups generate \(N\).
If \(\ell(v)\ne0\) and \(\ell\) is such an eigenfunctional,
continuity and (2.10b) bound
\[
 |e^{ct}\ell(v)|
   =|\ell(\pi(u(t))v)|
   \le C(1+|t|)^Aq(v).
 \tag{2.10aj}
\]
Take \(t\) in the direction with \((\Re c)t\to+\infty\).
This is impossible, so \(\ell=0\).

For every actual archimedean cuspidal factor, the supplied
paired models are furnished by Theorems 1.19 and 1.11–1.13.
The nonzero continuous Whittaker functional is proved
by Theorem 1.3 and Corollary 1.4 of
*Automorphic representations and automorphic L-functions*.
Consequently its space for a nondegenerate unitary
character has dimension exactly one. This application
uses the actual model, continuity and global existence;
the bound (2.10ai) itself does not presume genericity.

#### Proven scope and precise further obligations

Lemma 2.0w derives core irreducibility from topological
irreducibility and admissibility in the actual smooth model.
Theorem 2.0y constructs the missing continuous-dual
distributional embedding for *every supplied* complete
smooth moderate dual-pair model with irreducible admissible
core. Theorem 2.0z therefore closes general archimedean
Whittaker uniqueness in that exact model class, including
all compatible cuspidal models and nonunitary representations.
The occurrence and scalar analytic estimates it uses are
proved in Theorems 1.28 and 1.29 above.

Theorem 1.34 supplies a compatible dual pair for every abstract
irreducible admissible Harish-Chandra core. The present proof also
applies to any separately prescribed pair with the stated hypotheses.
It does not assert a general onto/closed-image globalization comparison,
opposite Whittaker existence in nongeneric models, or that
all continuous-dual convolutions land in a preselected
smooth contragredient. Onto comparison remains an additional obligation; it is unnecessary
for (2.10ai).

The free primary comparison source is Bernstein–Krötz,
*Smooth Fréchet globalizations of Harish-Chandra modules*,
author-hosted version dated 3 August 2014, §8, Theorem 8.1 (pp.35–36),
and Appendix A, §§12.1–12.4, especially Theorems 12.2
and 12.8 (pp.57–64):
[verified author-hosted PDF](https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/Bern-Kroetz-2014.pdf).
Our explicit row-minor vector (2.10j)–(2.10n), compact
packet estimate, exact kernel synthesis, coefficient
transport and dual embedding are proved above.
The full row-minor, synthesis and transport arguments have been
given above.

**Theorem 2.1 (Jacquet–Piatetski-Shapiro–Shalika, 1983; local factor identification; ordered essentially tempered factor identification and archimedean construction remain open).** Over a nonarchimedean local field, the Rankin–Selberg integrals for irreducible generic representations are rational functions of \(q^{-s}\). Their span over \(\mathbb C[q^s,q^{-s}]\) is a fractional ideal with a unique generator \(P(q^{-s})^{-1}\), where \(P(0)=1\); this generator defines the local L-factor. When both representations are unramified and have Satake matrices \(t,t'\),

\[
L_v(s,\pi_v\times\pi'_v)
=\det(1-q_v^{-s}t\otimes t')^{-1}.
\tag{2.2}
\]

Proposition 2.3b and Proposition 2.3d below prove convergence, rationality, the whole normalized nonarchimedean ideal and finite test-sum attainment in every pair of ranks and every nonarchimedean field; Corollary 2.3f proves rectangular-index independence. Theorem 2.3h proves the full scalar functional equation, and Proposition 2.3i and Corollary 2.3j prove Laurent epsilon, exact character scaling and norm shifts. Theorems 2.3l–2.3n identify the complete rank-one ideal, gamma and epsilon with the twisted matrix package, including ramified characters and both finite-field characteristics. Their block formula gives rank-one gamma multiplicativity when the inducing blocks are generic. Theorem 2.3ac and Corollary 2.3ad below prove full finite-place parabolic gamma multiplicativity and its polynomial correction for actual generic inducing data and supplied actual generic irreducible subquotients. Theorem 2.3ae identifies the whole spherical generator. Ordered essentially tempered data identification remains an additional assertion, located in the freely accessible author version [Jacquet–Piatetski-Shapiro–Shalika, *Rankin–Selberg convolutions*, §9.4]. Propositions 2.1a and 2.1c below prove the spherical Whittaker formula and the good-place integral value in every rank and over every nonarchimedean field. Theorem 2.3ae proves that this value generates the whole ideal. The freely accessible draft [Getz–Hahn, 22 April 2022 draft, Theorems 11.6.1–11.6.2] provides further reading for these statements. At archimedean places the factors have the form of finite products of shifted \(\Gamma_{\mathbb R}\) and \(\Gamma_{\mathbb C}\) functions, with nonzero exponential normalization factors. This shape belongs to the local factor construction; it does not assert that all the shifts are tempered.

Propositions 2.3b–2.3d construct the whole nonarchimedean fractional ideal. Theorem 2.3ae combines the spherical test with the proved parabolic polynomial correction to identify its normalized generator. Identification with ordered essentially tempered constituent factors and the archimedean factor construction still require the indicated proofs. Once a factor has the stated shape, Lemma 2.2 proves the elementary entire-reciprocal property.

### Spherical Whittaker functions in every finite-place rank

Let \(k\) be any nonarchimedean local field, with integers \(\mathcal O\), uniformizer \(\varpi\), residue cardinality \(q\), and a unitary additive character \(\psi\) trivial on \(\mathcal O\) and nontrivial on \(\varpi^{-1}\mathcal O\). Write \(G_r=\mathrm{GL}_r(k)\), \(K_r=\mathrm{GL}_r(\mathcal O)\), and \(N_r\) for the upper unitriangular group, with character
\[
\psi_r(u)=\psi\!\left(\sum_{i=1}^{r-1}u_{i,i+1}\right).
\]
For \(\lambda\in\mathbb Z^r\), put \(a_\lambda=\operatorname{diag}(\varpi^{\lambda_1},\ldots,\varpi^{\lambda_r})\). The Iwasawa modulus is
\[
\delta_r(a_\lambda)=q^{-\sum_i(r+1-2i)\lambda_i}.
\tag{2.5a}
\]
We use the proved general-linear Iwasawa integration and spherical classification in *The Satake isomorphism and spherical representations*, Proposition 1.1, equation (1.2), Proposition 5.1 and Corollary 5.2.

For a partition \(\lambda_1\ge\cdots\ge\lambda_r\ge0\), define
\[
s_\lambda^{(r)}(t)=
\frac{\det(t_i^{\lambda_j+r-j})_{i,j=1}^r}
{\det(t_i^{r-j})_{i,j=1}^r}.
\tag{2.5b}
\]
This agrees with (4.2): reversing the columns changes both determinants by the same sign. The numerator is alternating, so every \(t_i-t_j\) divides it; their distinct linear factors are prime, hence their product divides it. Thus (2.5b) is a polynomial even when parameters coincide. For any dominant integer tuple, extend the definition by
\[
s_\lambda^{(r)}(t)=
(t_1\cdots t_r)^{\lambda_r}
s_{\lambda-\lambda_r(1,\ldots,1)}^{(r)}(t),
\qquad t_i\ne0.
\tag{2.5c}
\]

**Proposition 2.1a (spherical Whittaker formula and uniqueness).** Let \(\pi\) be irreducible smooth unramified with Satake eigenvalues \(t_1,\ldots,t_r\), and let \(v_K\ne0\) be its spherical vector. Evaluation
\[
\operatorname{Hom}_{N_r}(\pi,\psi_r)\longrightarrow\mathbb C,
\qquad \ell\longmapsto\ell(v_K)
\]
is injective. In particular that space has dimension at most one. If it is nonzero, normalize \(\ell(v_K)=1\) and put \(W(g)=\ell(\pi(g)v_K)\). Then
\[
W(a_\lambda)=
\begin{cases}
\delta_r(a_\lambda)^{1/2}s_\lambda^{(r)}(t),
&\lambda_1\ge\cdots\ge\lambda_r,\\
0,&\text{otherwise}.
\end{cases}
\tag{2.5d}
\]
The assertion includes rank one, arbitrary residue characteristic and repeated Satake eigenvalues. Existence of a nonzero functional is a hypothesis in the normalized formula.

**Proof.** If \(\lambda_i<\lambda_{i+1}\), choose \(b\in\mathcal O\) for which \(\psi(\varpi^{\lambda_i-\lambda_{i+1}}b)\ne1\). Right \(K_r\)-invariance and left Whittaker equivariance give
\[
W(a_\lambda)=W(a_\lambda(1+bE_{i,i+1}))
=\psi(\varpi^{\lambda_i-\lambda_{i+1}}b)W(a_\lambda),
\]
so this value is zero.

For \(1\le j\le r\), let \(T_j=1_{K_ra_{(1^j,0^{r-j})}K_r}\), with \(\operatorname{vol}(K_r)=1\). We give the full right-coset calculation. A right coset corresponds to a lattice \(L\) satisfying
\(\varpi\mathcal O^r\subset L\subset\mathcal O^r\) and
\(\dim_{\mathbb F_q}(L/\varpi\mathcal O^r)=r-j\).
Reduced column echelon form, choosing each pivot to be the last nonzero coordinate of its column, gives a unique tuple \(\epsilon\in\{0,1\}^r\), \(\sum_i\epsilon_i=j\). The pivot positions are those with \(\epsilon_i=0\). The free entries are
\(x_{ab}\in\mathcal O/\varpi\mathcal O\) with \(a<b\), \(\epsilon_a=1\), \(\epsilon_b=0\). Consequently representatives are
\[
u(x)a_\epsilon,\qquad
u(x)=1+\sum_{\substack{a<b\\\epsilon_a=1,\ \epsilon_b=0}}
x_{ab}E_{ab},
\]
where each residue has one chosen integral lift. This construction also proves exhaustiveness and distinctness: reduce the lattice modulo \(\varpi\), take its unique reduced basis, and adjoin the \(\varpi e_i\)'s in the remaining coordinates. There are
\[
q^{I(\epsilon)},\qquad
I(\epsilon)=\sum_{a<b}\epsilon_a(1-\epsilon_b)
=\sum_a(r-a)\epsilon_a-\frac{j(j-1)}2
\tag{2.5e}
\]
representatives for this tuple.

Let \(\chi_i(\varpi)=t_i\). In normalized unramified induction the spherical vector has value
\(\delta_r(a_\epsilon)^{1/2}\prod_i t_i^{\epsilon_i}\) on \(u(x)a_\epsilon\). The preceding spherical-classification proof identifies its Hecke character with that of \(\pi\), including when the principal series is reducible. Since
\[
I(\epsilon)-\frac12\sum_i(r+1-2i)\epsilon_i
=\frac{j(r-j)}2,
\tag{2.5f}
\]
the eigenvalue of \(T_j\) on \(v_K\) is
\(q^{j(r-j)/2}e_j(t)\), where \(e_j(t)=\sum_{\sum\epsilon_i=j}\prod_i t_i^{\epsilon_i}\).

If \(\lambda\) is dominant, every entry of \(a_\lambda u(x)a_\lambda^{-1}\) is integral. Its Whittaker character is therefore one. Applying the same right-coset sum to \(W(a_\lambda)\), and setting
\(F_\lambda=\delta_r(a_\lambda)^{-1/2}W(a_\lambda)\), gives
\[
e_j(t)F_\lambda=
\sum_{\substack{\epsilon\in\{0,1\}^r,\ \sum\epsilon_i=j\\
\lambda+\epsilon\text{ dominant}}}F_{\lambda+\epsilon}.
\tag{2.5g}
\]
Nondominant terms vanish by the first paragraph; (2.5f) cancels all the remaining powers of \(q\). In particular \(T_r\) is the central coset \(\varpi I_rK_r\), so \(\pi(\varpi I_r)\) acts by \(e_r(t)=t_1\cdots t_r\).

The polynomials (2.5b) obey exactly (2.5g). Indeed multiply the numerator alternant by the symmetric polynomial \(e_j\). Expanding the determinant gives
\[
e_j(t)\det(t_i^{\lambda_b+r-b})
=\sum_{\sum\epsilon_b=j}
\det(t_i^{\lambda_b+r-b+\epsilon_b}).
\]
When \(\lambda+\epsilon\) is not dominant, two adjacent exponents coincide and that determinant is zero. In every other case it is the numerator for \(\lambda+\epsilon\). Dividing by the denominator proves the asserted recurrence, including coincident parameters by polynomial identity.

We verify that this recurrence and \(F_0\) determine every value; no uniqueness theorem for general Whittaker models is being used. Induct on the degree of a nonnegative partition and, at fixed degree, on lexicographic order. If \(\lambda\ne0\), let \(j\) be its number of positive parts and put
\(\mu=\lambda-(1^j,0^{r-j})\). This is a partition of smaller degree. In (2.5g) for \(\mu,j\), one term is \(F_\lambda\). Every other dominant tuple has the same degree as \(\lambda\) and is lexicographically smaller: its first omitted position among the first \(j\) parts is smaller by one. Those terms are already determined, so this equation determines \(F_\lambda\). The set of partitions of any fixed degree is finite. The initial value is \(F_0=W(1)\), whereas \(s_0=1\); hence
\(F_\lambda=W(1)s_\lambda^{(r)}(t)\) for every nonnegative partition. The central action just computed extends this to all dominant integer tuples by (2.5c).

If \(W(1)=0\), all diagonal values vanish. Iwasawa writes every \(g\) as \(u a_\lambda k\), with integral diagonal units absorbed into \(k\); equivariance then makes \(W(g)=0\). The translates of \(v_K\) span \(\pi\), by irreducibility, so \(\ell=0\). This proves injectivity of evaluation and also allows normalization of every nonzero functional. Formula (2.5d) and uniqueness follow. \(\square\)

### The spherical Rankin–Selberg integral

**Lemma 2.1b (rectangular Cauchy identity).** For \(n\ge m\) and complex tuples \(t=(t_1,\ldots,t_n)\), \(t'=(t'_1,\ldots,t'_m)\),
\[
\sum_{\lambda_1\ge\cdots\ge\lambda_m\ge0}
s_{(\lambda,0^{n-m})}^{(n)}(t)s_\lambda^{(m)}(t')z^{|\lambda|}
=\prod_{i=1}^n\prod_{j=1}^m(1-zt_it'_j)^{-1}.
\tag{2.5h}
\]
This holds formally, including repeated or zero parameters, and the sum converges absolutely whenever \(|z|RR'<1\), for arbitrary
\(R>\max_i|t_i|\) and \(R'>\max_j|t'_j|\).

**Proof.** The equal-size Cauchy identity, with its full determinant proof, is Lemma 4.2 of this lesson. To specialize its second tuple to \((t',0^{n-m})\), we prove the needed stability directly. In (2.5b) with the last variable zero, the last numerator row is zero if \(\lambda_r>0\). If \(\lambda_r=0\), only its last entry is one; expanding that row and factoring one power of each remaining variable gives
\[
s_\lambda^{(r)}(t_1,\ldots,t_{r-1},0)=
\begin{cases}
s_{(\lambda_1,\ldots,\lambda_{r-1})}^{(r-1)}
(t_1,\ldots,t_{r-1}),&\lambda_r=0,\\
0,&\lambda_r>0.
\end{cases}
\tag{2.5i}
\]
The denominator factors by precisely the same product. First take the remaining variables nonzero and distinct, then extend by the polynomial identity. Repeated specialization retains exactly the partitions with at most \(m\) nonzero parts, proving (2.5h).

For absolute convergence choose distinct radii
\(\max_i|t_i|<r_i<R\). On the product of these circles the denominator alternant has modulus at least
\(\prod_{i<j}|r_i-r_j|>0\), and the numerator has modulus at most
\(n!R^{|\lambda|+n(n-1)/2}\). The elementary polynomial contour formula bounds its value at \(t\) by this supremum times
\(\prod_i(1-|t_i|/r_i)^{-1}\). That formula follows simply by expanding each kernel
\(r_ie^{i\theta}/(r_ie^{i\theta}-t_i)\) geometrically and integrating the monomials; it needs no convergence theorem for the partition sum. Thus
\(\lvert s_\lambda^{(n)}(t)\rvert\le C_RR^{|\lambda|}\), with a constant independent of \(\lambda\). The same argument gives
\(\lvert s_\lambda^{(m)}(t')\rvert\le C_{R'}(R')^{|\lambda|}\). There are at most \((h+1)^m\) partitions of degree \(h\) with at most \(m\) parts. The resulting geometric series with polynomial coefficient bounds proves absolute convergence. \(\square\)

Give \(G_m,N_m\) Haar measures with volumes of \(K_m,N_m(\mathcal O)\) equal to one, and use their quotient measure. Let \(\pi,\pi'\) be unramified irreducible generic representations of \(G_n,G_m\), with spherical Whittaker functions normalized by \(W(1)=W'(1)=1\), for opposite characters \(\psi_n,\psi_m^{-1}\). For \(n>m\) define
\[
\Psi(s,W,W')=
\int_{N_m\backslash G_m}
W\!\begin{pmatrix}g&0\\0&I_{n-m}\end{pmatrix}
W'(g)|\det g|^{\,s-(n-m)/2}\,dg.
\tag{2.5j}
\]
For \(n=m\), with \(e_n=(0,\ldots,0,1)\) and \(\Phi_0=1_{\mathcal O^n}\), define
\[
\Psi(s,W,W',\Phi_0)=
\int_{N_n\backslash G_n}
W(g)W'(g)\Phi_0(e_ng)|\det g|^s\,dg.
\tag{2.5k}
\]
Opposite characters make these integrands invariant under the left unipotent group. In the equal-rank case \(e_nu=e_n\), so the Schwartz factor is invariant too.

**Proposition 2.1c (all-rank spherical integral value).** In a sufficiently far right half-plane these integrals converge absolutely, and in both cases their value is
\[
\prod_{i=1}^n\prod_{j=1}^m(1-t_it'_jq^{-s})^{-1}
=\det(1-q^{-s}t\otimes t')^{-1}.
\tag{2.5l}
\]
This proves the value of the spherical test, for every nonarchimedean \(k\). Theorem 2.3ae below proves that this value is the normalized generator of the full Rankin–Selberg fractional ideal.

**Proof.** For a left \(N_m\)-invariant, right \(K_m\)-invariant integrand, the proved Iwasawa formula in \(u a k\) order is the sum over \(\lambda\in\mathbb Z^m\) with weight \(\delta_m(a_\lambda)^{-1}\). Each torus-unit shell has volume one; \(K_m\) has volume one. This also gives the absolute integral by using absolute values.

When \(n=m\), Proposition 2.1a forces \(\lambda\) to be dominant. The last row of \(a_\lambda k\), for \(k\in K_n\), is \(\varpi^{\lambda_n}\) times a primitive integral row: some coordinate is a unit because \(k\) is invertible modulo \(\varpi\). Thus \(\Phi_0(e_na_\lambda k)=1\) exactly when \(\lambda_n\ge0\). The two Whittaker moduli cancel \(\delta_n^{-1}\), and the integral becomes the left side of (2.5h) with \(z=q^{-s}\).

When \(n>m\), apply Proposition 2.1a to the full tuple
\((\lambda_1,\ldots,\lambda_m,0,\ldots,0)\). Its nonzero values require precisely \(\lambda_1\ge\cdots\ge\lambda_m\ge0\). Here
\[
\delta_n(a_{(\lambda,0)})^{1/2}
\delta_m(a_\lambda)^{-1/2}
=q^{-(n-m)|\lambda|/2}.
\]
This cancels the \(-(n-m)/2\) shift in (2.5j), leaving
\(q^{-s|\lambda|}s_{(\lambda,0)}^{(n)}(t)s_\lambda^{(m)}(t')\).
Lemma 2.1b proves absolute convergence in a right half-plane and sums the series to (2.5l). The tensor matrix has eigenvalues \(t_it'_j\), giving the determinant form. \(\square\)

The general spherical formula is also treated in [Casselman–Shalika, the freely accessible NUMDAM edition, Theorem 5.4, printed page 227](https://www.numdam.org/item/CM_1980__41_2_207_0.pdf). The local integral normalization and the distinction between its value and ideal-generator identification are [Getz–Hahn, author draft of 22 April 2022, Theorems 11.6.1–11.6.2, printed pages 268–269/PDF pages 284–285](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf).


**Lemma 2.2 (entire reciprocals).** Each local factor in Theorem 2.1 has an entire reciprocal and has no zeros wherever it is holomorphic. It can have poles, and multiplying a complete product by reciprocal local factors can cancel those poles.

**Proof.** At a finite place the reciprocal is \(P(q_v^{-s})\), an entire function of \(s\); the factor \(1/P(q_v^{-s})\) cannot vanish. At infinity it suffices to establish that \(1/\Gamma(s)\) is entire. For \(\operatorname{Re}s>0\), repeated integration by parts gives

\[
B(s,M+1)=\int_0^1t^{s-1}(1-t)^M\,dt
=\frac{M!}{s(s+1)\cdots(s+M)}.
\]

Substitute \(u=Mt\). Since \((1-u/M)^M\le e^{-u}\) on \(0\le u\le M\), dominated convergence gives \(M^s B(s,M+1)\to\Gamma(s)\). Writing the reciprocals of these finite products and using \(\gamma=\lim_M(\sum_{k=1}^M1/k-\log M)\), we obtain the locally uniform product

\[
G(s)=s e^{\gamma s}\prod_{k\ge1}(1+s/k)e^{-s/k}.
\tag{2.3a}
\]

The limit defining \(\gamma\) exists by integral comparison. The product converges uniformly on compact sets: away from its finitely many initial factors, \(\log(1+s/k)-s/k=O(k^{-2})\) uniformly there. It defines an entire function and has zeros only at \(0,-1,-2,\ldots\). The product of each finite beta expression with its reciprocal is one. Passing to both limits gives \(\Gamma(s)G(s)=1\) in \(\operatorname{Re}s>0\); in particular \(\Gamma\) is nonzero there and \(G=1/\Gamma\). It follows by meromorphic continuation that \(\Gamma\) has no zeros and only its familiar poles. The exponential and scaling factors in \(\Gamma_{\mathbb R},\Gamma_{\mathbb C}\), and in the local normalizations, are entire and nonzero. Finite products preserve the asserted reciprocal property. ∎


**Proposition 2.3 (the unramified self-pairing formula).** For an irreducible unramified generic representation \(\tau\) of \(GL_n(F_v)\) with Satake eigenvalues \(\alpha_1,\ldots,\alpha_n\),

\[
L_v(s,\tau\times\widetilde\tau)
=\prod_{i,j=1}^n(1-\alpha_i\alpha_j^{-1}q_v^{-s})^{-1}.
\tag{2.3}
\]

If \(\tau\) is unitary, its inverse eigenvalue multiset is its complex-conjugate eigenvalue multiset, so also

\[
L_v(s,\tau\times\widetilde\tau)
=\prod_{i,j=1}^n(1-\alpha_i\overline{\alpha_j}q_v^{-s})^{-1}.
\tag{2.4}
\]

**Proof.** The Satake parameter of the contragredient is the inverse of the original parameter, up to conjugacy. In eigenbases, \(t\otimes t^{-1}\) acts on \(e_i\otimes e_j\) by \(\alpha_i\alpha_j^{-1}\). Its characteristic determinant is the product of the corresponding linear factors. Substitute this determinant into (2.2) to obtain (2.3).

For the unitary assertion, fix an invariant positive Hermitian form, linear in its first argument. The map from the conjugate representation to the smooth contragredient defined by \(\overline y\mapsto(x\mapsto\langle x,y\rangle)\) is an intertwiner, since \(\langle x,\tau(g)y\rangle=\langle\tau(g^{-1})x,y\rangle\). On each compact-open fixed space it is an isomorphism by finite-dimensional nondegeneracy and admissibility; these fixed spaces exhaust the smooth representations. Thus \(\widetilde\tau\simeq\overline\tau\). Complex conjugation conjugates the eigenvalues of the spherical Hecke character, whereas taking the contragredient inverts the Satake class. Spherical classification identifies the two multisets. Reordering the second index in (2.3) gives (2.4). ∎

### Finite-place Rankin–Selberg integrals in arbitrary ranks

Let \(k\) be a nondiscrete nonarchimedean local field, of either
characteristic, with integers \(\mathcal O\), uniformizer \(\varpi\), and
residue cardinality \(q\). Put \(G_r=\mathrm{GL}_r(k)\),
\(K_r=\mathrm{GL}_r(\mathcal O)\), and let \(N_r\) be the upper
unitriangular group. Initially the unitary additive character \(\psi\)
has annihilator \(\mathcal O\). Each additive coordinate has its
self-dual measure, so \(\operatorname{vol}(\mathcal O)=1\).
Multiplicative measures give \(K_r\) and \(\mathcal O^\times\) volume
one. The quotient measure on \(N_r\backslash G_r\) is the one obtained
from these measures by fibre integration. Write

\[
\psi_r(u)=\psi\left(\sum_{i=1}^{r-1}u_{i,i+1}\right),\qquad
R=\mathbb C[X,X^{-1}],\quad X=q^{-s}.
\tag{2.9a}
\]

The representations \(\pi\) of \(G_n\) and \(\sigma\) of \(G_m\)
are actual irreducible smooth admissible complex representations, and
are generic. Their Whittaker models are denoted
\(\mathcal W(\pi,\psi_n)\) and
\(\mathcal W(\sigma,\psi_m^{-1})\). This hypothesis does not ask for
a global realization, a unitary norm twist, or an unramified vector.
The complete preceding proof of uniqueness and of the contragredient
identification is Theorem 2.0 of this lesson.
The compact averaging and Jacquet-admissibility proofs used below are
Lemma 1.17a of that lesson. The general Iwasawa proof and normalized
induction are in its Theorem 1.23; its Theorem 1.23e supplies a
cuspidal-support embedding where explicitly invoked later. These are
actual proof bodies, not a generalization of the separate rank-two
classification lesson.

For \(n=m\) put
\[
Z(s,W,W',\Phi)=
\int_{N_n\backslash G_n}W(g)W'(g)\Phi(e_ng)|\det g|^s\,dg,
\qquad \Phi\in C_c^\infty(k^n).
\tag{2.9b}
\]
For \(n>m\) and \(0\le j\le n-m-1\), put
\[
Z_j(s,W,W')=
\int_{N_m\backslash G_m}\int_{M_{j,m}(k)}
W\left(\begin{pmatrix}g&0&0\\x&I_j&0\\0&0&I_{n-m-j}\end{pmatrix}\right)
W'(g)|\det g|^{s-(n-m)/2}\,dx\,dg.
\tag{2.9c}
\]
The last identity block always has positive size. Both integrands
descend to the stated quotient: replacing \(g\) by \(ug\),
\(u\in N_m\), multiplies the first displayed matrix on the left
by \(\operatorname{diag}(u,I)\), and the two Whittaker characters
cancel. We state the formulas with \(n\ge m\). For the opposite
ordering, exchange the names of the ranks and representations,
keeping the chosen base character on the larger-rank Whittaker
space. If models with the opposite character assignments were
specified initially, the transport in (2.9av), with \(b=-1\),
gives their exact conversion.

#### Uniform central polynomials on proper Jacquet modules

For \(1\le i<n\), let \(U_i\) be the upper radical of the parabolic
of type \((i,n-i)\), and let
\[
a_i=\operatorname{diag}(\varpi I_i,I_{n-i}).
\tag{2.9d}
\]
The Jacquet module in this paragraph is **unnormalized**.

**Lemma 2.3.** There is a polynomial \(p_{\pi,i}(T)\in\mathbb C[T]\),
with nonzero constant term, annihilating the action of \(a_i\) on
\(\pi_{U_i}\). It is independent of the vector and of its compact
open stabilizer. If the Jacquet module is zero, take \(p_{\pi,i}=1\).

**Proof.** Fix a nonzero vector \(v_0\). Irreducibility says that its
\(G_n\)-translates span the representation. The general-linear
Iwasawa decomposition \(G_n=P_iK_n\) gives
\[
[\pi(u m k)v_0]=m[\pi(k)v_0]
\quad\text{in }\pi_{U_i}.
\]
The compact orbit \(K_nv_0\) is finite: an open subgroup of \(K_n\)
fixes \(v_0\), and its index is finite. Thus finitely many vectors
\(y_1,\ldots,y_b\) generate \(\pi_{U_i}\) as an \(M_i\)-module.
They have a common compact open stabilizer \(J\subset M_i\).
By the complete compact-fixed lifting proof of Lemma 1.17a,
\((\pi_{U_i})^J\) is finite-dimensional. The central element \(a_i\)
and its inverse preserve this fixed space. Its characteristic
polynomial has nonzero constant term, annihilates all \(y_l\),
and, since \(a_i\) commutes with \(M_i\), annihilates every one of
their \(M_i\)-translates. This proves the assertion. The finite
dimensional characteristic-polynomial identity can be checked
directly: \((TI-A)\operatorname{adj}(TI-A)=
\det(TI-A)I=\operatorname{adj}(TI-A)(TI-A)\). The two identities
show that every coefficient of the adjugate commutes with \(A\);
substitution \(T=A\) gives the asserted identity. \(\square\)

Write a diagonal matrix in ratio coordinates as
\[
a(t)=\operatorname{diag}(t_1\cdots t_n,t_2\cdots t_n,\ldots,t_n).
\tag{2.9e}
\]
Let \(W(g)=\lambda(\pi(g)v)\). For a fixed \(v\), the equality
\(p_{\pi,i}(a_i)[v]=0\) means an **actual finite** expression
\[
p_{\pi,i}(\pi(a_i))v=
\sum_{l=1}^b(\pi(u_l)-1)v_l,\qquad u_l\in U_i.
\tag{2.9f}
\]
Consequently
\[
\sum_h p_{\pi,i,h}W(a(t)a_i^h)=0
\quad\text{if }v(t_i)\ge B_{v,i}.
\tag{2.9g}
\]
Indeed \(\psi_n(a(t)u_la(t)^{-1})\) is exactly
\(\psi(t_i(u_l)_{i,i+1})\); every other entry of \(U_i\) is a
nonsimple root and contributes nothing to \(\psi_n\). Choose
\(B_{v,i}\) making these finitely many characters equal to one.
Crucially, this threshold is independent of all the other \(t_h\).
There is no assertion of continuity of the algebraic functional
\(\lambda\) in this argument.

On the other side, if \(v\) is fixed by
\(1+\varpi^d E_{i,i+1}\mathcal O\), then
\[
W(a(t))=0\quad\text{unless }v(t_i)\ge-d.
\tag{2.9h}
\]
This follows by applying left Whittaker equivariance and right
invariance to \(a(t)(1+bE_{i,i+1})\), with
\(b\in\varpi^d\mathcal O\). If \(t_i\varpi^d\mathcal O\) is not
in the annihilator, some such scalar character is different from
one. Thus every ratio valuation has a lower bound, and an eventual
recurrence with a fixed polynomial.

The center acts on \(\pi\) by a smooth character \(\omega_\pi\), by
the countable Schur proof for a cyclic smooth irreducible module.
Therefore
\[
W(a(t_1,\ldots,t_{n-1},t_n))=
\omega_\pi(t_n)W(a(t_1,\ldots,t_{n-1},1)).
\tag{2.9i}
\]
These statements hold uniformly over the finitely many right
\(K_n\)-translates needed in an Iwasawa integral. They provide a
finite polynomial majorant without importing a finite-length
theorem for the entire mirabolic restriction.

#### The elementary recurrence calculation

**Lemma 2.3a.** Suppose a sequence \(f(v_1,\ldots,v_d)\) vanishes
unless \(v_i\ge A_i\), and for each coordinate satisfies an eventual
constant-coefficient recurrence with invertible characteristic
roots, independent of the other coordinates. Its multivariable
generating series is rational, with denominator a product of
one-coordinate recurrence denominators. It converges absolutely
when the variables have sufficiently small absolute values.

If two sequences have eventual roots \(\alpha,\beta\), of respective
Jordan multiplicities \(u,v\), their pointwise product has eventual
root \(\alpha\beta\), of multiplicity at most \(u+v-1\).

**Proof.** A sequence satisfying a monic recurrence of degree \(h\)
with nonzero constant term is determined by \(h\) consecutive
values. Over \(\mathbb C\), the vector of consecutive values is
advanced by its invertible companion matrix. Reducing this finite
matrix to Jordan form shows that the sequence is a sum of
\(\alpha^v P_\alpha(v)\), where
\(\deg P_\alpha\) is smaller than the root multiplicity. This is
also proved without naming a normal-form theorem by successively
solving \((S-\alpha)^u f=0\): after division by \(\alpha^v\),
the \(u\)-th forward difference is zero, and induction expresses
the result as a linear combination of the binomial polynomials
\(\binom v0,\ldots,\binom v{u-1}\). Factoring the characteristic
polynomial and using polynomial Bézout projections separates the
different roots. Multiplying two such expressions gives the
claimed bound \(u+v-1\).

After shifting each \(A_i\) to zero, multiplication of the formal
series by the denominator of the \(i\)-th recurrence leaves a
series supported on a finite set of values of its \(i\)-th
coordinate. Doing this for all coordinates leaves a polynomial:
the recurrences in other coordinates survive each subtraction.
The denominator has nonzero constant term, so this establishes the
formal rational identity. Alternatively the preceding exponential
polynomial description gives an upper bound
\(C\prod_i C_i^{v_i}(1+v_i)^{h_i}\), with \(C\) depending on the
finitely many initial values. This proves absolute convergence for
sufficiently small variables and proves that the formal identity
is the corresponding analytic identity. \(\square\)

The same proof applies when the initial values depend on finitely
many unit cosets. Every smooth torus function arising here is
invariant under a common open subgroup of each
\(\mathcal O^\times\); consequently these unit integrations are
finite sums. Absolute values obey the exponential-polynomial
bound, so no formal calculation is used to infer convergence.

#### Convergence and a common rational denominator

The exact Iwasawa quotient integration is
\[
\int_{N_r\backslash G_r}F(g)\,dg
=\int_{K_r}\int_{(k^\times)^r}
F(a(t)k)\prod_{i=1}^{r-1}|t_i|^{-i(r-i)}
\prod_{i=1}^r d^\times t_i\,dk.
\tag{2.9j}
\]
The exponent follows by multiplying the positive-root moduli:
\(\delta_{B_r}(a(t))=\prod_{i<r}|t_i|^{i(r-i)}\).
The multiplicative and additive compact subgroups all have volume
one, so the Iwasawa proof by the bijection
\(B_r/(B_r\cap K_r)\to G_r/K_r\) introduces no numerical
constant. Fibre integration over \(N_r\) gives (2.9j).

**Proposition 2.3b.** For every pair in (2.9a), all integrals
(2.9b)–(2.9c) converge absolutely in a right half-plane, are rational
in \(X=q^{-s}\), and have a common denominator
\(D_{\pi,\sigma}(X)\in\mathbb C[X]\), \(D_{\pi,\sigma}(0)=1\),
independent of \(W,W',\Phi\) and of \(j\).

**Proof for equal ranks.** Right smoothness and compactness of \(K_n\)
reduce the \(K_n\)-integral to finitely many summands. Their scalar
Schwartz factor is
\(\Phi(t_ne_nk)\). It vanishes for \(v(t_n)\) sufficiently negative
and is constant for \(v(t_n)\) sufficiently positive. For \(i<n\),
the product of the two Whittaker values has eventual roots
\(\alpha\beta\), where \(\alpha\) is a root of \(p_{\pi,i}\) and
\(\beta\) is a root of \(p_{\sigma,i}\). Lemma 2.3a bounds their
multiplicities independently of the tests. The measure factor in
(2.9j) and the determinant power multiply the \(v(t_i)\)-th
coefficient by
\[
q^{i(n-i)v(t_i)}X^{iv(t_i)}.
\tag{2.9k}
\]
Thus a common denominator is the product, over these finitely many
roots and \(i<n\), of suitable powers of
\(1-\alpha\beta q^{i(n-i)}X^i\), together with
\(1-\omega_\pi(\varpi)\omega_\sigma(\varpi)X^n\).
Including a factor which cancels after integration over units is
harmless. All constant terms are one. Equations (2.9g)–(2.9i) and
Lemma 2.3a give absolute convergence in a common sufficiently
right half-plane, and the rational identity there. The finitely
many initial negative valuations contribute only Laurent powers.

**Uniform bound for the rectangular variable.** A right-smooth
Whittaker function satisfies, at every point \(h=uak\) in Iwasawa
form,
\[
W(h)\ne0\Longrightarrow
|a_l/a_{l+1}|\le C_W\quad(1\le l<n).
\tag{2.9l}
\]
This is (2.9h) for the finitely many \(K_n\)-translates. In the
matrix in (2.9c), the last row is \(e_n\). Its sup norm, and
invariance of that norm under \(K_n\), give \(|a_n|=1\).
Hence every \(|a_l|\) is bounded above independently of \(g,x\).
For \(r>m\), the wedge of rows \(r,\ldots,n\) has norm
\[
\left\|\bigwedge_{l=r}^n e_lh\right\|
=\prod_{l=r}^n|a_l|.
\tag{2.9m}
\]
Upper-unipotent row operations preserve this wedge, and the
integral compact group preserves its sup norm, by its integral
inverse. If \(r\le m+j\), the coefficient on columns
\(b,r+1,\ldots,n\), \(b\le m\), is exactly \(x_{r-m,b}\):
the remaining identity columns form a triangular identity matrix,
and row \(r\) is zero in all those columns. Thus every entry of
\(x\) is bounded by (2.9m), uniformly in \(g\). This proves that
the integrand is zero outside one fixed compact rectangular set.

On that compact set, \(W\) has only finitely many right translates
under
\(\left(\begin{smallmatrix}I_m&0&0\\x&I_j&0\\0&0&I\end{smallmatrix}\right)\).
Indeed a sufficiently fine additive lattice changes that element
on the right by a member of a common open stabilizer of \(W\).
The \(x\)-integral in (2.9c) is consequently a **finite** linear
combination of \(j=0\) integrals for right translates of \(W\).

**Proof for unequal ranks.** For \(j=0\), use (2.9j) in \(G_m\).
The embedded diagonal has ratio coordinates
\((t_1,\ldots,t_m,1,\ldots,1)\) in \(G_n\). For \(i<m\), its
product with the \(G_m\) Whittaker function has roots
\(\alpha\beta\) from \(p_{\pi,i},p_{\sigma,i}\). For \(i=m\),
the roots are \(\alpha\omega_\sigma(\varpi)\), from
\(p_{\pi,m}\) and the exact central character of \(\sigma\).
The corresponding measure and determinant weight is
\[
q^{[i(m-i)+i(n-m)/2]v(t_i)}X^{iv(t_i)}
\quad(i<m),\qquad
q^{m(n-m)v(t_m)/2}X^{mv(t_m)}.
\tag{2.9n}
\]
Again Lemma 2.3a proves convergence and a denominator independent
of the tests. The preceding finite rectangular reduction proves
the assertions for every \(j\), with the same denominator.
Replacing the tests by their absolute values and using the
exponential-polynomial bound proves absolute convergence of all
integrals before any reordering. \(\square\)

This proof proves common-denominator rationality directly from
compact-fixed Jacquet admissibility. It does not presume a
finite-length mirabolic restriction or a classification of
irreducible representations.

#### The spectral two-orbit lemma and the compact mirabolic part

Write
\[
P_r=\left\{\begin{pmatrix}h&b\\0&1\end{pmatrix}
:h\in G_{r-1},\ b\in k^{r-1}\right\},\qquad
U_r=\left\{\begin{pmatrix}I&b\\0&1\end{pmatrix}\right\}.
\tag{2.9o}
\]
In this paragraph induction is **unnormalized** unless a density
factor is explicitly stated. For a smooth \(P_r\)-module \(V\),
Fourier transform of compact \(U_r\)-averages makes \(V\) a
nondegenerate module over \(C_c^\infty((k^{r-1})^*)\): a vector
fixed by a compact open lattice in \(U_r\) is fixed by the Fourier
idempotent of its annihilator. Compact additive averages are
finite sums on smooth vectors.

Here are the elementary sheaf facts needed for this construction.
For an \(l\)-space \(Y\) and a nondegenerate
\(C_c^\infty(Y)\)-module \(M\), its fibre at \(y\) is
\(M_y=M/\{fM:f(y)=0\}\). A compact-open idempotent localizes a
vector. A vector whose fibres vanish at every point of a compact
open localization is zero: each vanishing fibre means an identity
on a neighbourhood of that point, and a finite compact-open
partition combines those identities. The same partition proves
gluing of finitely many localized vectors. Consequently the
kernel of the map to the fibre at a closed point is exactly the
submodule obtained by functions supported off that point.
This gives the exact sequence
\[
0\longrightarrow V_{\ne0}\longrightarrow V
\longrightarrow V_{U_r}\longrightarrow0.
\tag{2.9p}
\]
There is no normal-jet term over an \(l\)-space.

The action of \(G_{r-1}\) on the nonzero row frequencies is
transitive; the stabilizer of \(e_{r-1}\) is \(P_{r-1}\).
An equivariant sheaf on this orbit is determined by its fibre
\(D(V)=V_{U_r,\psi(e_{r-1}\,\cdot)}\). Explicitly its compactly
supported sections are
\[
V_{\ne0}\simeq
c\operatorname{-Ind}_{P_{r-1}U_r}^{P_r}
(D(V)\otimes\psi(e_{r-1}\,\cdot)).
\tag{2.9q}
\]
For completeness the compact-induction identification is proved
by local sections, not an appeal to a representation theorem.
On the chart where the \(i\)-th coordinate of a row is nonzero,
elementary column operations give a continuous matrix sending
\(e_{r-1}\) to that row; dividing by its nonzero coordinate is the
only denominator. On a compact-open subchart, use this section
to transport a fibre vector. Its smooth stabilizer makes the
transport locally constant after a finite partition. Fourier
idempotents localize it to the chosen subchart. The fibre
criterion in the preceding paragraph proves injectivity, and
the finite gluing criterion proves surjectivity. The transition
matrices belong to the stabilizer and give precisely the
covariance in (2.9q). Compact support off zero is exactly compact
support modulo that stabilizer. This proves (2.9q).

Both ordinary and twisted coinvariants used here are exact:
a vector in a submodule whose image is a finite sum of twisted
differences in the ambient module is killed by one sufficiently
large compact weighted average; that average belongs to the
submodule. Conversely each such average differs from the vector
by a finite sum of twisted differences. This also proves exactness
at every iteration.

Iterating the injections (2.9p)–(2.9q) produces in \(V\) a
canonical submodule
\[
c\operatorname{-Ind}_{N_r}^{P_r}\psi_r\ \otimes\
V_{N_r,\psi_r}.
\tag{2.9r}
\]
To check the fibre on the right, order the upper unipotent
coordinates by their last column, starting with column \(r\).
The corresponding character is \(\psi\) on its last coordinate
and trivial on its other coordinates. Its stabilizer is
\(P_{r-1}\); the next column gives the same construction there.
Successive quotienting is exactly quotienting by all the
\(N_r\)-twisted differences: the group is generated by these
columns, and its character is their product. The zero-frequency
quotient at any step has zero final generic coinvariant, since
the last simple-root subgroup there acts trivially but its
prescribed character is nontrivial. Exactness therefore shows
that (2.9r) maps isomorphically onto the final generic fibre.

Applied to the Whittaker model of a generic irreducible \(\pi\),
that fibre has dimension one by Theorem 2.0. The Whittaker
functional is nonzero on (2.9r). In the compact-induced model,
its evaluation functional and its translates are the usual
compact Whittaker functions: (2.9q) proves this by induction,
starting from \(P_1=\{1\}\). Thus
\[
C_c^\infty(N_r\backslash P_r,\psi_r)
\subset \{W|_{P_r}:W\in\mathcal W(\pi,\psi_r)\}.
\tag{2.9s}
\]
This inclusion is proved for every generic irreducible, with no
cuspidal or unramified restriction.

#### The value one and the normalized fractional ideal

**Proposition 2.3d.** For every generic pair, the \(R\)-span of
(2.9b), and the \(R\)-span of each family (2.9c), contains \(1\).
Each is a fractional ideal with a unique generator
\(1/P(X)\), \(P\in\mathbb C[X]\), \(P(0)=1\). Its generator is
attained by a finite sum of integrals of actual test data.

**Proof of the value one, equal ranks.** In (2.9s) choose compact
Whittaker restrictions \(\phi,\phi'\), with inverse characters,
equal to \(1\) at the identity. Choose their supports sufficiently
small in \(N_n\backslash P_n\) that they lie in the determinant
unit locus. More explicitly, take the functions supported on
\(N_n(P_n\cap J_0)\), for a sufficiently deep principal congruence
subgroup \(J_0\subset K_n\), with values
\(\phi(np)=\psi_n(n)\) and
\(\phi'(np)=\psi_n(n)^{-1}\), \(p\in P_n\cap J_0\).
These are well-defined since \(\psi_n\) is trivial on
\(N_n\cap J_0\). Choose Whittaker lifts \(W,W'\) of them and a
deeper principal congruence subgroup \(J\subset J_0\) fixing
both lifts. Put \(\Phi=1_{e_nJ}\).

Every \(g\) with \(e_ng\in e_nJ\) is \(pk\), \(p\in P_n\),
\(k\in J\). Thus the product in (2.9b) is the indicator, on the
quotient, of \(N_nH\), where
\(H=(P_n\cap J_0)J\). This is a compact open subgroup of \(K_n\):
\(J\) is normal in \(K_n\), and \(P_n\cap J_0\) normalizes it.
Every determinant on this support is a unit. The integral is
therefore the positive constant
\[
C=\frac{\operatorname{vol}_{G_n}(H)}
{\operatorname{vol}_{N_n}(N_n\cap H)},
\tag{2.9t}
\]
independent of \(s\). Formula (2.9t) follows directly by fibre
integration on the compact group \(H\). Dividing \(\Phi\) by
\(C\) gives the value \(1\). Both volumes are actual finite
congruence-index volumes for the measures in (2.9a).

**Proof of the value one, unequal ranks.** The map
\[
(N_mg,x)\longmapsto
N_n\begin{pmatrix}g&0&0\\x&I_j&0\\0&0&I\end{pmatrix}
\tag{2.9u}
\]
into \(N_n\backslash P_n\) is injective. Comparing the identity
columns in an upper-unitriangular equality forces every
cross-block upper entry to vanish and then forces \(x'=x\)
and \(g'=ug\), \(u\in N_m\). Near the identity it is an embedding
of a closed coordinate subspace: Gaussian elimination of a
matrix with all trailing pivots nonzero gives unique lower
entries, nonzero diagonal entries and an upper-unipotent
factor. The eliminations are polynomial operations and division
by these pivots; their inverses are continuous. Its lower
entries and diagonal entries provide a compact-open coordinate
box around the identity in \(N_n\backslash P_n\).

Choose the box so small that every determinant on it is a unit
and its intersection with (2.9u) projects in \(N_m\backslash G_m\)
to an identity neighbourhood where a Whittaker function
\(W'(1)=1\) is constant after removing its \(N_m\)-character.
Choose \(\phi\in C_c^\infty(N_n\backslash P_n,\psi_n)\)
to be the character of its Gaussian upper factor on this box,
and zero outside. On (2.9u), the upper factor is the upper
factor of \(g\) in its first block: the other displayed upper
entries are zero and the lower rows are already reduced.
Hence \(\phi\) and \(W'\) have cancelling phases on their
support. Lift \(\phi\) by (2.9s). The integrand in (2.9c) is
the nonnegative indicator of a compact neighbourhood of
\((N_mI_m,0)\), with determinant power one. Compactness is
also a consequence of (2.9l)–(2.9m); the torus values of \(g\)
are units on the chosen box. Its integral is a finite positive
constant for the exact quotient and additive measures. Dividing
the lifted \(W\) by that constant gives \(Z_j=1\).

**The ideal.** For equal ranks, simultaneously right translating
\(W,W'\), and \(\Phi(x)\mapsto\Phi(xh)\) multiplies (2.9b) by
\(|\det h|^{-s}\). For unequal ranks, translating \(W\) by
\(\operatorname{diag}(h,I)\), translating \(W'\) by \(h\), and
making \(g\mapsto gh\), \(x\mapsto xh\), gives
\[
Z_j(s,\rho(\operatorname{diag}(h,I))W,\rho(h)W')
=|\det h|^{-s+(n-m)/2-j}Z_j(s,W,W').
\tag{2.9v}
\]
The constant in (2.9v) is nonzero. Taking
\(v(\det h)=\pm1\) proves stability under \(X\) and \(X^{-1}\).
Thus the complex spans themselves are \(R\)-modules.
Proposition 2.3b puts each in \(D^{-1}R\), so they are fractional
ideals, and the just-constructed value one makes them nonzero.

Here is the normalization and attainment argument explicitly.
The localization \(R=\mathbb C[X,X^{-1}]\) is a principal ideal
domain: clearing finitely many powers of \(X\) reduces Euclidean
division to \(\mathbb C[X]\). If \(I\subset D^{-1}R\) and
\(1\in I\), the ideal \(DI\) has a generator \(A\) dividing
\(D\). Since \(D(0)=1\), canceling an invertible Laurent monomial
normalizes \(A(0)\ne0\) and yields
\(I=R/P(X)\), \(P(0)=1\). The units of \(R\) are exactly
\(cX^b\): compare the least and greatest powers of a Laurent
polynomial and its inverse. This proves uniqueness of the
normalized reciprocal generator.

Euclidean division also expresses the generator as an \(R\)-linear
combination of finitely many original integrals. By (2.9v), or
its equal-rank counterpart, each Laurent coefficient is a finite
sum of scalar multiples of integrals with actual translated test
data. Hence \(1/P\) is attained by a **finite sum of actual pure
test integrals**, equivalently by one element of the algebraic
tensor product of the test spaces. No additional assertion that
one pure tensor always attains the generator is being inferred
from a greatest-common-divisor calculation. \(\square\)

#### The ideals are independent of the rectangular index

**Lemma 2.3e (one exact root exchange).** For \(1\le j\le n-m-1\)
and \(\varphi\in C_c^\infty(k^m)\), set
\[
W^\varphi(h)=\int_{k^m}
W\bigl(h(1+\textstyle\sum_{i=1}^m z_iE_{i,m+j+1})\bigr)
\widehat\varphi(-z)\,dz,
\qquad
\widehat\varphi(z)=\int_{k^m}\varphi(x)\psi(xz)\,dx.
\tag{2.9w}
\]
The integrals in (2.9w) are finite smooth-vector averages, so
\(W^\varphi\) is an actual member of the Whittaker model. If
\(b\in M_{j-1,m}(k)\), \(x\in k^m\), and
\[
T(g,b,x)=
\begin{pmatrix}g&0&0&0\\b&I_{j-1}&0&0\\x&0&1&0\\0&0&0&I_{n-m-j}\end{pmatrix},
\]
then
\[
W^\varphi(T(g,b,x))=W(T(g,b,x))\varphi(x).
\tag{2.9x}
\]
On the corresponding \(j-1\) matrix the equality reads
\(W^\varphi(T(g,b,0))=\varphi(0)W(T(g,b,0))\).

**Proof.** Multiply \(T\) by the upper root vector in (2.9w).
Its new column \(m+j+1\) has entries \(gz,bz,xz\) in the three
preceding blocks. Removing them by a left upper-unipotent
matrix leaves \(T\). Its only simple-root entry is \(xz\), in
position \((m+j,m+j+1)\); the preceding entries are all at
distance at least two from the diagonal. Thus the Whittaker
multiplier is \(\psi(xz)\). Positive-trace self-dual Fourier
inversion gives
\(\int\psi(xz)\widehat\varphi(-z)\,dz=\varphi(x)\).
This proves both identities, including the signs. \(\square\)

**Corollary 2.3f.** The ideals \(I_j\) of (2.9c) are all equal.

**Proof.** The uniform compact bound for the last rectangular
row, and smoothness, express \(Z_j\) as a finite sum of
\(Z_{j-1}\)'s for right translates by that lower row. This gives
\(I_j\subset I_{j-1}\). Conversely choose
\(\varphi=1_L\), where \(L\subset k^m\) is so small that the
lower-row unipotent with entries in \(L\) fixes \(W\). Then
(2.9x) and right invariance give
\[
Z_j(s,W^\varphi,W')=
\operatorname{vol}(L)Z_{j-1}(s,W,W').
\tag{2.9y}
\]
Indeed \(T(g,b,x)=T(g,b,0)(1+\sum x_iE_{m+j,i})\).
The volume in (2.9y) is nonzero, and the integral is absolutely
convergent in its initial half-plane. This proves the reverse
inclusion, then the equality of rational functions everywhere.
\(\square\)

The normalized generator of Proposition 2.3d therefore defines a
single \(L(s,\pi\times\sigma)\), independently of \(j\).

#### Mirabolic pairings outside finitely many parameters

The following argument needs a finite filtration by **orbit depth**,
not a finite composition series. Its central polynomial exclusion
works even if the intermediate derivative modules have infinite
length.

Use the raw functors of the preceding two-orbit construction: \(D\) is the nonzero-character fibre
for \(U_r\), \(E\) is the ordinary \(U_r\)-coinvariant, \(D^+\)
is the compact induction in (2.9q), and \(E^+\) is inflation
from \(G_{r-1}\) to \(P_r\). Both \(D,E\) are exact. Repeating
the two-orbit sequence (2.9p) gives a filtration with one layer
for each \(1\le i\le r\):
\[
\mathcal I_i(V^{(i)}),\qquad
V^{(i)}=ED^{i-1}V,\qquad
\mathcal I_i=(D^+)^{i-1}E^+.
\tag{2.9z}
\]
Its bottom submodule is the \(i=r\) layer. In matrix notation
\[
\mathcal I_i(A)=
c\operatorname{-Ind}_{H_{r,i}}^{P_r}(A\otimes\psi_i),
\quad
H_{r,i}=
\left\{\begin{pmatrix}h&b\\0&u\end{pmatrix}:
h\in G_{r-i},\ u\in N_i\right\},
\tag{2.9aa}
\]
where \(\psi_i\) is the generic character on the trailing
\(N_i\) and is trivial on \(b\). Induction here is unnormalized.
For \(i=1\) this simply means inflation, and for \(i=r\)
it is compact Whittaker induction. Transitivity of the
compact-induction descriptions follows by composing their
local sections; a compact support in each successive quotient
is a compact support in the composed quotient.

The raw derivative has the concrete description
\[
V^{(i)}=
\bigl(V_{U_{r-i,i}}\bigr)_{N_i,\psi_i}.
\tag{2.9ab}
\]
To verify it, take the last \(i-1\) columns with their nonzero
last-coordinate characters and then the ordinary last column
in the remaining \(P_{r-i+1}\). Their generated subgroup is
\(U_{r-i,i}\rtimes N_i\): its rectangular entries have
character one, and exactly the trailing simple roots have
character \(\psi\). Quotienting by successive twisted
differences is quotienting by their union, since these columns
generate the group and the stated character respects every
commutator. The \(G_{r-i}\)-action on both quotients is the
original action. This proves (2.9ab), including its absence of
a normalization twist.

In particular, for \(r-i=l>0\), the action of
\(\varpi I_l\) on \(V^{(i)}\), when \(V=\pi|_{P_r}\), is
annihilated by \(p_{\pi,l}\). Indeed that central element is
\(a_l\) before the quotient (2.9ab), and the polynomial of
Lemma 2.3 survives every further quotient. No derivative
admissibility assertion is needed. Also
\(V^{(r)}=\pi_{N_r,\psi_r}\) is one-dimensional.

Here is the exact pairing calculation for the layers. The
second module uses the inverse generic character.
\[
\operatorname{Bil}_{P_r}
(\mathcal I_i(A)\otimes|\det|^z,\mathcal I_h(B))=0
\quad\text{if }i\ne h.
\tag{2.9ac}
\]
If \(i=h\) and \(l=r-i\), this space identifies with the
bilinear forms \(\lambda\) on \(A\times B\) satisfying
\[
\lambda(a(g)v,b(g)w)
=|\det g|^{\,i-1-z}\lambda(v,w),
\qquad g\in G_l.
\tag{2.9ad}
\]
For \(l=0\), the right side means all bilinear forms on the
two fibres, with no parameter restriction.

We give the kernel and density justification. At one nonzero
frequency step, the two \(U_r\)-actions on sections are
multiplication by \(\psi(\xi b)\) and
\(\psi(-\eta b)\). Their invariant bilinear kernel is supported
on \(\xi=\eta\). Indeed a pair of disjoint compact-open
frequency boxes is killed by one Fourier idempotent equal
to one on one box and zero on the other. Every compact
off-diagonal support is a finite union of such rectangles.
Restriction to the diagonal has no jets: a locally constant
test vanishing on it vanishes on a neighbourhood of its
compact intersection, and the same finite-rectangle argument
proves the restriction kernel. Local sections from (2.9q)
identify the remaining kernel with a homogeneous equivariant
functional on compact sections over the nonzero row orbit.

Such a functional is determined by a functional on the
stabilizer fibre with the Haar-density transformation. This
can be verified directly by pulling back along
\(G_{r-1}\to P_{r-1}\backslash G_{r-1}\), integrating on each
compact fibre, and using a finite compact-open partition.
The pullback averaging map is onto. Its kernel is generated
by right translates minus their Haar-mass ratios: expressing
a compact locally constant function on the fibre as a finite
sum of compact coset indicators shows that its sole surviving
coordinate is its Haar integral. An equivariant functional
on the group itself is
\(\int f(g)\chi(g)\lambda(g^{-1}v)\,dg\);
its uniqueness follows by evaluating on an identity compact
open subgroup fixing \(v\), then decomposing the compact
support into its cosets. These steps prove the stabilizer
identification for algebraic smooth modules as well.

The row-orbit additive measure transforms under \(g\in
G_{r-1}\) by \(|\det g|\). Equivalently the modulus of \(P_r\)
on its \(G_{r-1}\) block is \(|\det g|\). Thus a pairing of
two nonzero-frequency layers with the first twisted by
\(|\det|^z\) reduces to a pairing of the two fibre modules
with first twist \(|\det|^{z-1}\). Iterating \(i-1\) steps
gives (2.9ad). If at some step one frequency is zero and the
other nonzero, the same Fourier idempotents kill the pairing.
This proves (2.9ac). One can also check the entire density at
once: \(H_{r,i}\) has modulus \(|\det g|^i\), whereas \(P_r\)
has modulus \(|\det g|\), so their ratio is
\(|\det g|^{i-1}\), exactly (2.9ad).

**Proposition 2.3g.** Suppose two smooth \(P_r\)-modules have
the filtration (2.9z), one-dimensional bottom generic fibres,
and each positive-rank derivative has a finite annihilating
polynomial for its central uniformizer. Then
\[
\dim\operatorname{Bil}_{P_r}(V\otimes|\det|^z,V')
\le1
\tag{2.9ae}
\]
except for finitely many values of \(q^{-z}\). In particular
this holds for the restrictions of any two generic irreducible
smooth admissible \(G_r\)-representations.

**Proof.** At a layer with \(i=h<r\), let the possible central
eigenvalues on its two derivative modules be \(\alpha,\beta\).
Their finite polynomials decompose each module into its
generalized eigenspaces by polynomial Bézout projections;
this is valid for infinite-dimensional modules because the
annihilating polynomials are global. Equation (2.9ad) can be
nonzero only if
\[
\alpha\beta=q^{-l(i-1-z)},\qquad l=r-i>0.
\tag{2.9af}
\]
For example, apply its central operator to the bilinear form:
on a generalized \((\alpha,\beta)\) pair the product operator
has sole eigenvalue \(\alpha\beta\); subtracting a different
scalar gives an invertible polynomial operator. The required
bilinear form must therefore vanish. Each (2.9af) excludes
only finitely many values of \(q^{-z}\), and there are finitely
many layers and roots.

Outside these exclusions, the only possible nonzero layer
pair is \(i=h=r\), whose space has dimension one. Restriction
to the two bottom submodules is injective. To see this without
an extension argument, choose the least pair of filtration
indices on which a nonzero form is nonzero. It then factors
through the corresponding pair of layers; all such pairs
except the bottom pair have just been killed. A form
vanishing on the bottom pair is consequently zero.
This proves (2.9ae). The statements following (2.9ab) verify
all its hypotheses for the actual representations here.
\(\square\)

#### The scalar functional equation

Let \(w_r\) be the antidiagonal permutation matrix, with all
its nonzero entries \(1\), and put
\[
\widetilde W(g)=W(w_rg^{-t}),\qquad
\widehat\Phi(y)=\int_{k^n}\Phi(x)\psi(xy^t)\,dx.
\tag{2.9ag}
\]
The preceding contragredient theorem identifies
\(\widetilde W\in\mathcal W(\pi^\vee,\psi_n^{-1})\);
similarly \(\widetilde W'\) has character \(\psi_m\).
Put \(d=n-m>0\), \(w_{n,m}=\operatorname{diag}(I_m,w_d)\),
and \(k=d-1-j\).

**Theorem 2.3h.** There is a nonzero rational scalar
\(\Gamma(s,\pi,\sigma,\psi)\), independent of the tests and
of \(j\), with
\[
Z(1-s,\widetilde W,\widetilde W',\widehat\Phi)
=\Gamma(s,\pi,\sigma,\psi)Z(s,W,W',\Phi)
\quad(n=m),
\tag{2.9ah}
\]
and
\[
Z_k(1-s,\rho(w_{n,m})\widetilde W,\widetilde W')
=\Gamma(s,\pi,\sigma,\psi)Z_j(s,W,W')
\quad(n>m).
\tag{2.9ai}
\]
These are identities of rational functions with the measures
in (2.9a) and the determinant shifts in (2.9b)–(2.9c).

**Proof for equal ranks.** A trilinear form underlying (2.9b)
has covariance
\[
B(\pi(h)v,\sigma(h)v',\Phi(\,\cdot\,h))
=|\det h|^{-s}B(v,v',\Phi).
\tag{2.9aj}
\]
Its restriction to tests supported off zero is determined
by a stabilizer-fibre functional on \(V\times V'\), because
\(P_n\backslash G_n\) is the nonzero row orbit. The explicit
fibre-averaging proof in the pairing argument applies. The stabilizer modulus
is \(|\det p|\), so that functional satisfies
\[
\lambda(\pi(p)v,\sigma(p)v')
=|\det p|^{1-s}\lambda(v,v').
\tag{2.9ak}
\]
Thus it belongs to the mirabolic pairing space with first
twist \(|\det|^{s-1}\), and Proposition 2.3g bounds it by one
outside a finite set of \(X\). A form whose restriction is
zero is supported at zero and is
\(\lambda_0(v,v')\Phi(0)\). The center then requires
\[
\omega_\pi(a)\omega_\sigma(a)=|a|^{-ns}.
\tag{2.9al}
\]
At \(a=\varpi\) this excludes all but finitely many \(X\).
There are no point-supported derivatives over an \(l\)-space.
Therefore the entire space (2.9aj) has dimension at most one
outside a finite set.

The left side of (2.9ah) has the same covariance. In fact
\(\widetilde{\rho(h)W}=\rho(h^{-t})\widetilde W\), and
\[
\widehat{\Phi(\,\cdot\,h)}(y)
=|\det h|^{-1}\widehat\Phi(yh^{-t}).
\tag{2.9am}
\]
Multiplying this factor by the determinant covariance of
the integral at \(1-s\) gives exactly \(|\det h|^{-s}\).
Both families are rational by Proposition 2.3b. Choose the
fixed pure test triple with \(Z=1\) from Proposition 2.3d;
its transformed value is a rational candidate for \(\Gamma\).
Generic uniqueness proves (2.9ah) for every test. This candidate
is not identically zero, since the transforms are bijections
of the test spaces and the dual integral family contains one.
Rational identities holding outside a finite set hold everywhere.

**Proof for \(n>m\), initially \(j=0\).** The direct bilinear
form has \(G_m\)-covariance \(|\det h|^{d/2-s}\), and under
\[
U_{m+1,n}=
\left\{\begin{pmatrix}I_{m+1}&b\\0&u\end{pmatrix}:
u\in N_{d-1}\right\}
\tag{2.9an}
\]
in its first argument it has character \(\psi_n\).
Both assertions follow by multiplication of the displayed
matrices in (2.9c). The second has no entry in position
\((m,m+1)\), which is essential: its first identity block
has size \(m+1\).

Any such form factors through
\[
Q=D^{d-1}(\pi|_{P_n}),
\tag{2.9ao}
\]
a smooth \(P_{m+1}\)-module. Successive last-column characters
are precisely the character in (2.9an), with no normalization
twists. Its ordinary quotient \(E(Q)=\pi^{(d)}\) is a
\(G_m\)-module with a global central polynomial, by (2.9ab)
and Lemma 2.3. A pairing of this quotient with \(\sigma\)
having the stated \(G_m\)-covariance is therefore zero
outside finitely many \(X\).

Its nonzero-frequency submodule restricts to \(G_m\) as
\[
c\operatorname{-Ind}_{P_m}^{G_m}D(Q).
\tag{2.9ap}
\]
The same local-section/fibre-averaging proof gives for its
pairing with \(\sigma\) a stabilizer pairing on
\(D(Q)\times(\sigma|_{P_m})\), with covariance
\(|\det p|^{d/2-s+1}\). All positive-rank derivative
polynomials of \(D(Q)\) are the polynomials of the
corresponding derivatives of \(\pi\); its bottom fibre is
the one-dimensional full generic fibre of \(\pi\).
Proposition 2.3g, with parameter \(s-d/2-1\), bounds this
space by one outside finitely many \(X\). Restriction from
the full pairing space is injective because the ordinary
quotient pairing has been killed. Thus the desired unequal
bilinear model also has generic dimension at most one.

The left side of (2.9ai) for \(j=0,k=d-1\) has exactly
this covariance and this unipotent character. Here are the
matrix checks. A \(G_m\) translation passes through
\(w_{n,m}\); inverse transpose changes it to \(h^{-t}\).
In the lower rectangle of the dual integral, changing its
\(d-1\) rows by \(x\mapsto xh^{-t}\) contributes
\(|\det h|^{d-1}\), while the determinant power at \(1-s\)
contributes \(|\det h|^{1-s-d/2}\) after inversion.
Together these give \(|\det h|^{d/2-s}\) in the original
covariance convention. For (2.9an), inverse transpose and
conjugation by \(w_{n,m}\) turn its nontrivial simple roots
into the trailing simple roots with the reversed negative
parameters. The inverse Whittaker character cancels those minus
signs. More explicitly, conjugating \(1-cE_{ba}\) by
\(w_{n,m}\) has the following three forms. If \(a\le m\),
it is a lower entry in one of the \(d-1\) integrated rows;
changing that row variable is a Haar translation, and
the original root character is one. If \(a=m+1\), it
is an upper entry \((b',n)\), \(b'=n+m+1-b\).
The last column of the integration matrix is \(e_n^t\),
so this right entry equals the same left upper entry.
Its inverse Whittaker multiplier is \(\psi(c)\) exactly
when \(b'=n-1\), that is, when \(b=m+2\); otherwise
both character factors are one. Finally if \(a\ge m+2\),
it is an upper entry wholly inside the middle identity
block. Moving it to the left changes the lower rectangle
by an elementary row operation of determinant one.
Its inverse Whittaker multiplier is \(\psi(c)\) exactly
when \(b=a+1\), as required. These root matrices
generate (2.9an), proving the full unipotent covariance.

Generic uniqueness and the fixed value-one tests therefore
produce a nonzero rational \(\Gamma\), exactly as in equal
ranks, and prove (2.9ai) for \(j=0\).

**Passage from \(j-1\) to \(j\), with the same scalar.**
This step uses a Fourier identity on a compact last row,
and supplies the otherwise missing index-independence of
the functional equation. Fix \(j\ge1\), let \(k=d-1-j\),
and define
\[
\begin{split}
F_s(x)&=Z_{j-1}(s,\rho(l_j(x))W,W'),\\
H_s(y)&=\int_{N_m\backslash G_m}
\int_{M_{k,m}(k)}
(\rho(w_{n,m})\widetilde W)
(T(g,b,y))\widetilde W'(g)
|\det g|^{1-s-d/2}\,db\,dg,
\end{split}
\tag{2.9aq}
\]
where \(l_j(x)=1+\sum x_iE_{m+j,i}\), and in the second
line \(T\) has \(k+1\) lower rectangular rows, the last
being \(y\). By the compact bounds (2.9l)–(2.9m) and right
smoothness, both are compactly supported locally constant
row functions, with one compact support and one open
constancy lattice independent of \(s\). Their finitely many
values are rational functions by Proposition 2.3b.

The inverse transpose of \(l_j(x)\), conjugated by
\(w_{n,m}\), is
\[
1-\sum_{i=1}^m x_iE_{i,m+k+2}.
\tag{2.9ar}
\]
The dual Whittaker model has character \(\psi_n^{-1}\);
evaluation of the upper entry \(-x\) on the dual matrix
with last row \(y\) therefore multiplies its value by
\(\psi(+yx^t)\), exactly the inverse-character version
of the matrix calculation of (2.9x). Applying the already
proved \(j-1\) equation to \(\rho(l_j(x))W\) yields
\[
\int H_s(y)\psi(+yx^t)\,dy
=\Gamma(s,\pi,\sigma,\psi)F_s(x).
\tag{2.9as}
\]
This is an identity in
\(C_c^\infty(k^m)\otimes_\mathbb C\mathbb C(X)\);
initial convergence and then rationality justify every
value. Integrating (2.9as) in \(x\), self-dual Fourier
inversion gives \(H_s(0)\) on the left, whereas the right
is \(\Gamma Z_j(s,W,W')\). The value \(H_s(0)\) is exactly
the dual \(Z_k\). This proves (2.9ai) for \(j\), with no
new scalar. Induction completes the proof. \(\square\)

#### Laurent epsilon, inversion and additive-character scaling

In the usual Rankin–Selberg convention set
\[
\begin{split}
\gamma(s,\pi\times\sigma,\psi)
&=\omega_\sigma(-1)^{n-1}\Gamma(s,\pi,\sigma,\psi),\\
\epsilon(s,\pi\times\sigma,\psi)
&=\gamma(s,\pi\times\sigma,\psi)
\frac{L(s,\pi\times\sigma)}
{L(1-s,\pi^\vee\times\sigma^\vee)}.
\end{split}
\tag{2.9at}
\]
When the ranks are exchanged, use the convention in (2.9c)
with the same chosen base character on the larger rank.
The central sign in (2.9at) is the sign in the JPSS statement;
it is included explicitly rather than silently incorporated
in the antidiagonal matrices.

**Proposition 2.3i.** The normalized epsilon factor is a
Laurent unit
\[
\epsilon(s,\pi\times\sigma,\psi)=cX^a,\qquad
c\ne0,\quad a\in\mathbb Z.
\tag{2.9au}
\]
For every \(b\in k^\times\), using the self-dual additive
measures for \(\psi_b(x)=\psi(bx)\), one has
\[
\begin{split}
L(s,\pi\times\sigma;\psi_b)&=L(s,\pi\times\sigma;\psi),\\
\gamma(s,\pi\times\sigma,\psi_b)
&=\omega_\pi(b)^m\omega_\sigma(b)^n
|b|^{nm(s-1/2)}\gamma(s,\pi\times\sigma,\psi),\\
\epsilon(s,\pi\times\sigma,\psi_b)
&=\omega_\pi(b)^m\omega_\sigma(b)^n
|b|^{nm(s-1/2)}\epsilon(s,\pi\times\sigma,\psi).
\end{split}
\tag{2.9av}
\]

**Proof of the unit assertion.** Divide (2.9ah) or (2.9ai)
by the corresponding normalized ideal generators. Finite
attainment in Proposition 2.3d shows that \(\epsilon\in R\):
a finite test sum whose normalized direct value is one
has normalized transformed value
\(\omega_\sigma(-1)^{n-1}\epsilon\).
Apply the equation again with the dual representations,
the inverse character and \(1-s\). In equal ranks
\(\widetilde{\widetilde W}=W\), and Fourier transforms
with \(\psi\) and \(\psi^{-1}\) compose to the identity.
In unequal ranks, the two \(w_{n,m}\)'s and inverse
transposes compose to the identity as well:
\[
\widetilde{\rho(w_{n,m})\widetilde W}
=\rho(w_{n,m}^{-t})W,\qquad
w_{n,m}^{-t}=w_{n,m}.
\]
The two central signs in (2.9at) multiply to one.
Consequently
\[
\epsilon(s,\pi\times\sigma,\psi)
\epsilon(1-s,\pi^\vee\times\sigma^\vee,\psi^{-1})=1.
\tag{2.9aw}
\]
The second factor belongs to \(R\) after
\(q^{-(1-s)}=q^{-1}X^{-1}\). Thus \(\epsilon\) and its
inverse are Laurent polynomials, proving (2.9au).

**Exact change of additive measure.** Put
\[
D_r=\frac{r(r-1)}2,\quad E_r=\frac{r(r^2-1)}6,\qquad
t_r(b)=\operatorname{diag}(b^{r-1},\ldots,b,1).
\tag{2.9ax}
\]
The transported Whittaker functions are
\(W_b(g)=W(t_n(b)g)\) and
\(W'_b(g)=W'(t_m(b)g)\).
Changing from \(\psi\) to \(\psi_b\) multiplies each
additive coordinate measure by \(|b|^{1/2}\):
this is checked by substituting in the two successive
Fourier transforms. Since multiplicative Haar measure on
\(G_r\) stays fixed, its quotient measure is multiplied
by \(|b|^{-D_r/2}\).

For equal ranks, \(\det t_n(b)=b^{D_n}\) and its
conjugation modulus on \(N_n\) is \(|b|^{E_n}\).
Left substitution by \(t_n(b)\) on the quotient therefore
gives
\[
Z_{\psi_b}(s,W_b,W'_b,\Phi)
=C_b(s)Z_\psi(s,W,W',\Phi),\quad
C_b(s)=|b|^{E_n-D_n(s+1/2)}.
\tag{2.9ay}
\]
This scalar is an \(R\)-unit, so the normalized generator
is unchanged. The tilde operation gives
\[
\widetilde W_b(g)=\omega_\pi(b)^{n-1}
\widetilde W(t_n(b)g),
\tag{2.9az}
\]
since \(w_nt_n(b)w_n=b^{n-1}t_n(b)^{-1}\);
the analogous factor for \(W'\) is
\(\omega_\sigma(b)^{n-1}\). Also
\(\widehat\Phi_{\psi_b}(y)=|b|^{n/2}\widehat\Phi_\psi(by)\).
The central substitution \(g\mapsto bg\) in the dual
integral contributes
\(\omega_\pi(b)\omega_\sigma(b)|b|^{-n(1-s)}\).
Combining this with
\(C_b(1-s)/C_b(s)=|b|^{D_n(2s-1)}\) gives
\[
[\omega_\pi(b)\omega_\sigma(b)]^n
|b|^{n+2D_n},
\]
which is precisely (2.9av) because \(n+2D_n=n^2\).

For unequal ranks put \(d=n-m\) and
\[
h_b=\operatorname{diag}(b^dI_m,t_d(b)).
\tag{2.9ba}
\]
The identity
\[
t_n(b)T_j(g,x)=T_j(t_m(b)g,x')h_b,\qquad
x'_{\ell,*}=b^{-\ell}x_{\ell,*}
\tag{2.9bb}
\]
shows that this right translation of \(W\) is independent
of \(j\). The \(jm\) additive measures, the \(N_m\)-quotient
measure and the determinant shift in (2.9c) give
\[
Z_{j,\psi_b}(s,W_b,W'_b)
=C_{j,b}(s)
Z_{j,\psi}(s,\rho(h_b)W,W'),\qquad
C_{j,b}(s)=
|b|^{E_m-D_ms+D_m(d-1)/2+mj(j+2)/2}.
\tag{2.9bc}
\]
For clarity, the two rectangular contributions are
\(|b|^{jm/2}\) from self-dual measure and
\(|b|^{mj(j+1)/2}\) from (2.9bb). The left torus
substitution contributes \(|b|^{E_m}\), its determinant
contributes \(|b|^{-D_m(s-d/2)}\), and the quotient
measure contributes \(|b|^{-D_m/2}\). Their product
is exactly (2.9bc). Again the scalar is an \(R\)-unit
and the right translation is a bijection of the model,
so the ideal generator is unchanged.

In the transformed equation, (2.9az) contributes
\(\omega_\pi(b)^{n-1}\omega_\sigma(b)^{m-1}\).
Moreover
\[
h_bw_{n,m}
=b^{d-1}I_n\,
\operatorname{diag}(b^{d+1}I_m,I_d)\,
w_{n,m}h_b^{-t}.
\tag{2.9bd}
\]
The first two factors on the right, by central characters
and by \(g,x\mapsto b^{d+1}g,b^{d+1}x\) in the dual
\(Z_k\), contribute
\[
\omega_\pi(b)^{-(d-1)}\omega_\sigma(b)^{d+1}
|b|^{-m(d+1)(1-s-d/2+k)}.
\tag{2.9be}
\]
The character product is now
\(\omega_\pi(b)^m\omega_\sigma(b)^n\). The remaining
absolute-value exponent is
\[
\begin{split}
&D_m(2s-1)+\frac m2[k(k+2)-j(j+2)]\\
&\hspace{20mm}-m(d+1)(1-s-d/2+k)
=mn(s-1/2),
\end{split}
\tag{2.9bf}
\]
using \(j+k=d-1\). This proves (2.9av) with every
measure and shift accounted for. The central sign in
(2.9at) is unchanged by the additive character.
\(\square\)

In particular (2.9aw) and (2.9av) imply the same-character
reflection identity
\[
\epsilon(s,\pi\times\sigma,\psi)
\epsilon(1-s,\pi^\vee\times\sigma^\vee,\psi)
=\omega_\pi(-1)^m\omega_\sigma(-1)^n.
\tag{2.9bg}
\]
No nonnegativity or generic-conductor identification of the
integer in (2.9au) has been inferred here.

**Corollary 2.3j (exact norm shifts).** For arbitrary complex
\(u,v\), the twists \(\pi\otimes|\det|^u\) and
\(\sigma\otimes|\det|^v\) satisfy
\[
L(s,(\pi\otimes|\det|^u)\times
(\sigma\otimes|\det|^v))
=L(s+u+v,\pi\times\sigma),
\tag{2.9bh}
\]
and the same identity holds for \(\gamma\) and \(\epsilon\).
Indeed the two twisted Whittaker values in (2.9b)–(2.9c)
introduce exactly \(|\det g|^{u+v}\). In the dual family
their exponents are \(-u,-v\); hence its parameter
\(1-s-u-v\) is the reflection of \(s+u+v\). The reciprocal
polynomial at \(q^{-(s+u+v)}\) still has constant term one,
so normalization of the ideal gives (2.9bh), and the scalar
identities then give the other two assertions.


Free comparison: [Jacquet–Piatetski-Shapiro–Shalika, author-hosted Rankin–Selberg convolutions](https://www.math.columbia.edu/~hj/Rankin%20Selberg%20convolutions.pdf), §§2.4–2.12, printed pp. 387–403, PDF pp. 22–38. The common-denominator recurrence and orbit-depth pairing arguments above are fully written; the citation supplies no omitted auxiliary theorem.

### Complete finite rank-one Rankin–Selberg / matrix identification

#### A direct comparison with the matrix ideal in rank \(m=1\)

This comparison is a proved inclusion of complete integral
families; it is not a claim identifying their gamma factors.

**Proposition 2.3k.** If \(\chi\) is a smooth character of
\(k^\times\), every integral for \(\pi\times\chi\) belongs
to the standard matrix ideal for \(\pi\otimes(\chi\circ\det)\).
In particular the Rankin–Selberg factor divides that matrix
factor, in the reciprocal-polynomial sense. If \(\pi\) is
Jacquet-cuspidal of rank \(n>1\), then
\[
 L(s,\pi\times\chi)=1.
 \tag{2.9bl}
\]

**Proof.** It suffices to realize \(Z_0(s,W,\chi)\)
as an actual matrix zeta integral. Its torus value
\(W(\operatorname{diag}(t,I_{n-1}))\) vanishes for
\(|t|>C\), by (2.9h). Let \(v\) be its vector and
\(\lambda\) its algebraic Whittaker functional. Choose
a sufficiently deep principal congruence subgroup \(J\)
fixing \(v\), with \(\psi\) trivial on its upper entries.
Put \(\mu=\lambda\circ e_J\). This belongs to the smooth
dual, because it is \(J\)-fixed.

For \(|t|\le C\), the exact upper–diagonal-block–lower
probability factorization of \(J\) gives
\[
 \mu\bigl(\pi(\operatorname{diag}(t,I))v\bigr)
       =W(\operatorname{diag}(t,I)).
 \tag{2.9bm}
\]
Indeed the upper average is invisible to \(\lambda\);
the block-diagonal average fixes \(v\) and commutes with
the displayed diagonal; and conjugating its lower-block
average by that diagonal multiplies the entries by \(t\).
Taking the lower congruence lattice sufficiently small
makes it fix \(v\) for every \(|t|\le C\). Entries internal
to the last block already fix \(v\). This proves (2.9bm)
uniformly as \(t\) tends to zero.

Write a matrix with invertible last block as
\[
 g=\begin{pmatrix}a&b\\c&D\end{pmatrix}
   =\begin{pmatrix}1&bD^{-1}\\0&I\end{pmatrix}
     \operatorname{diag}(t,D)
     \begin{pmatrix}1&0\\D^{-1}c&I\end{pmatrix},
 \quad t=a-bD^{-1}c.
 \tag{2.9bn}
\]
Choose \(D\) in a small compact neighbourhood of
\(I_{n-1}\), and \(b,c\) in small compact additive
neighbourhoods of zero, so that the right lower factor
fixes \(v\), the left upper factor fixes \(\mu\), and
\(\chi(\det D)=1\). The coefficient
\[
 c_\chi(g)=\chi(\det g)\mu(\pi(g)v)
 \]
then equals
\(\chi(t)W(\operatorname{diag}(t,I))\) on this set.
Choose a scalar Schwartz function in the coordinates
\((t,b,c,D)\), equal to a function \(\phi(t)\) times
the indicators of these three small neighbourhoods,
where \(\phi=1\) on \(|t|\le C\) and has compact
support there. Extended by zero away from the chosen
invertible-\(D\) chart, this is an actual Schwartz
function on \(M_n(k)\), including \(t=0\).

The additive Jacobian of (2.9bn) is one:
only \(a=t+bD^{-1}c\) is changed. With
\(\alpha_n=\prod_{i=1}^n(1-q^{-i})\), the matrix Haar
measure is \(\alpha_n^{-1}|\det g|^{-n}\,dg_{\rm add}\).
The standard exponent \(s+(n-1)/2\) and
\(dt=(1-q^{-1})|t|\,d^\times t\) therefore leave
\[
 |t|^{s-(n-1)/2}\,d^\times t.
 \]
The three transverse integrations are a finite positive
constant; divide the Schwartz function by it. The resulting
matrix integral is exactly \(Z_0(s,W,\chi)\), initially
by absolute convergence and then by rationality.
Every \(Z_j\) belongs to the same ideal by Corollary 2.3f.
If \(n=1\), this calculation is simply the scalar Tate
integral with a cutoff equal to one on the original test
support.

The standard matrix ideal and its normalized generator
were proved in Proposition 1.3. Its inclusion now gives
the stated polynomial divisibility. Twisting a
Jacquet-cuspidal representation by a determinant
character preserves every zero Jacquet module.
Lemma 1.20a and Proposition 1.4 give matrix factor
one; its ideal is \(R\). The Rankin–Selberg ideal is
contained in \(R\) and contains one, so is exactly
\(R\), proving (2.9bl). \(\square\)

As another immediate consequence, the completed spherical
integral identifies the full generator when one rank is
one and the pair is unramified: the spherical value equals
the already proved unramified matrix factor, and the
inclusion of this proposition gives both ideal inclusions.
This argument does not extrapolate to a general tensor
parameter in two higher ranks.

#### The complete rank-one comparison of the two finite ideals

The following is a reverse inclusion to Proposition 2.3k, for every actual
generic irreducible and every character. It proves standard-factor
identification between the two integral definitions at a finite
place; it does not silently identify their Fourier scalars.

**Theorem 2.3l.** For every actual generic irreducible smooth
admissible \(\pi\) of \(G_n\), and every smooth character
\(\chi\) of \(k^\times\),
\[
 \mathcal I_{\mathrm{RS}}(\pi\times\chi)
       =\mathcal I_{\mathrm{mat}}
                   (\pi\otimes(\chi\circ\det)),\qquad
 L_{\mathrm{RS}}(s,\pi\times\chi)
       =L_{\mathrm{mat}}
                   (s,\pi\otimes(\chi\circ\det)).
 \tag{2.9ck}
\]
The measures are those already fixed: matrix additive
measure is self-dual, \(K_n\) has group volume one,
and \(\mathcal O^\times\) has multiplicative volume one.

**Step 1: ordinary and generalized matrix coefficients
have the same ideal.** Write
\[
 J_s(\Phi,W)=\int_{G_n}\Phi(g)W(g)
                |\det g|^{s+(n-1)/2}\,dg.
 \tag{2.9cl}
\]
Given \(\Phi\), choose a compact open \(J\) for
which \(\Phi(jg)=\Phi(g)\). Such a group exists
even though \(\Phi\) is a test on the whole
matrix space: if its support is in
\(\varpi^{-B}M_n(\mathcal O)\) and its constancy
lattice is \(\varpi^RM_n(\mathcal O)\), take
\(J=1+\varpi^cM_n(\mathcal O)\) with \(c-B\ge R\).
Both \(j\) and \(j^{-1}\) preserve the support
ball, and change a matrix there by its constancy
lattice.

For \(W(g)=\lambda(\pi(g)v)\), the functional
\(\lambda e_J\) is in the smooth dual. Averaging
the integral on the left over \(J\) gives
\[
 J_s(\Phi,W)
   =Z_{\rm mat}(s,\Phi,(\lambda e_J)(\pi(\,\cdot\,)v)).
 \tag{2.9cm}
\]
Indeed determinants in \(J\) have norm one
and the test is left invariant. Absolute
convergence is checked before averaging.
Iwasawa and the compact support ball of
the matrix test bound every \(|a_j|\)
above; its absolute \(N_n\)-integral is
at most a constant times
\(\prod_j|a_j|^{-(j-1)}\).
The bounds (2.9h) put all ratio valuations
below a fixed lower threshold. On each
of their tails Lemma 2.3 bounds \(W\)
by a polynomial times finitely many
exponentials. Its central character
is another exponential. Every increasing
ratio valuation has determinant exponent
\(i\,\operatorname{Re}s\), and the
central valuation has exponent
\(n\,\operatorname{Re}s\). Taking
\(\operatorname{Re}s\) sufficiently
large makes each geometric series
converge, including the fixed Iwasawa
and upper-entry Jacobian exponents.
This proves absolute convergence of
(2.9cl) in a right half-plane. Identity
(2.9cm) then gives its rational continuation.

Conversely every smooth dual vector is a
finite sum of averaged translated Whittaker
functionals. Fix its compact open stabilizer
\(J\). The functionals
\[
 v\longmapsto\lambda(\pi(h)e_Jv),\qquad h\in G_n,
 \tag{2.9cn}
\]
span \((V^J)^*\): otherwise a nonzero vector
in the finite-dimensional \(V^J\) would be
annihilated by all of them; all its translates
would then be annihilated by \(\lambda\),
contrary to irreducibility and \(\lambda\ne0\).
Compact averaging extends the finite spanning
identity to the full module. A coefficient
therefore is a finite sum of
\(\int_J W(hjg)\,dj\). In its matrix integral
put \(g'=hjg\). This leaves a generalized
integral (2.9cl) with a translated matrix test,
times
\(|\det h|^{-s-(n-1)/2}\).
The latter is a Laurent unit in \(X\), times
a nonzero complex constant. The generalized
matrix and ordinary matrix families thus
have the same \(R\)-span. In particular this
argument proves equality of the *entire*
ideals, rather than equality of a selected
coefficient's denominator.

**Step 2: an explicit compact determinant-one kernel.**
Assume \(n\ge2\), and let
\(K_n^1=\mathrm{SL}_n(\mathcal O)\), with
probability Haar measure. The Iwasawa formula
can use \(K_n^1\) in place of \(K_n\) while
retaining all the diagonal coordinates.
Indeed the determinant map on \(K_n\) splits
by \(u\mapsto\operatorname{diag}(u,1,\ldots,1)\).
Its Haar integral is the product of the unit
Haar integral and the \(K_n^1\) integral.
Absorb the unit \(u\) in the first diagonal
coordinate. The other Haar measures and
the Iwasawa density are unchanged.

For \(k\in K_n^1\), let \(B(a,C)\) be the
upper triangular matrix with diagonal
\(a=(a_1,\ldots,a_n)\) and strict upper
entries \(C=(C_{ij})_{i<j}\). Define the
actual Schwartz function
\[
 \begin{split}
 \Psi_k(a;\zeta_2,\ldots,\zeta_n)
    &=\int \Phi(B(a,C)k)
                  \psi\!\left(\sum_{j=2}^n
                          \zeta_j C_{j-1,j}\right)dC,\\
 \mathcal K_k(\xi;a_2,\ldots,a_n;
                             \zeta_2,\ldots,\zeta_n)
    &=\int_k\Psi_k(a;\zeta)\psi(-a_1\xi)\,da_1.
 \end{split}
 \tag{2.9co}
\]
The first integration includes the non-simple
strict upper entries with trivial character.
It is an integration and a partial Fourier
transform of a Schwartz function. Consequently
both displayed functions are Schwartz in their
stated coordinates. This can be verified
without a topological tensor assertion:
partition the original test into finitely many
cosets of one additive matrix lattice. Each
coset integral or Fourier transform is the
usual lattice-coset integral, a constant
times a coset indicator and a character.
Adding gives the assertion. The functions
have only finitely many possibilities as
\(k\) varies, by compactness and the matrix
test's right open stabilizer.

In the \(N_n\)-integration put
\(C_{ij}=u_{ij}a_j\). Its Jacobian is
\(\prod_{j=2}^n|a_j|^{j-1}\). Whittaker
equivariance replaces that integration by
\[
 \prod_{j=2}^n|a_j|^{-(j-1)}
       \Psi_k(a;a_2^{-1},\ldots,a_n^{-1}).
 \tag{2.9cp}
\]
Apply Fourier inversion in \(a_1\) in (2.9co).
Let \(b=a_2\cdots a_n\), set \(t=a_1b\), and put
\[
 h(\xi,a_2,\ldots,a_n,k)
     =\left(1+\frac{\xi}{b}E_{12}\right)
            \operatorname{diag}
                  (b^{-1},a_2,\ldots,a_n)\,k.
 \tag{2.9cq}
\]
This is in \(\mathrm{SL}_n(k)\). The equality
\[
 W\bigl(\operatorname{diag}(t,I)h\bigr)
  =\psi(t\xi/b)\,
        W\bigl(\operatorname{diag}
                       (t/b,a_2,\ldots,a_n)k\bigr)
 \tag{2.9cr}
\]
is simply left Whittaker equivariance for
the first simple root. It absorbs the
Fourier-inversion multiplier
\(\psi(a_1\xi)\).

The Iwasawa density and (2.9cp) give the
diagonal exponents
\[
 s+(n-1)/2-(n+1-2j)-(j-1)
                  =s-(n-1)/2+(j-1).
 \]
Replacing \(a_1\) by \(t/b\) therefore leaves
exactly
\[
 |t|^{s-(n-1)/2}
       \prod_{j=2}^n|a_j|^{j-1}.
 \tag{2.9cs}
\]
Define a complex measure \(\mu_\Phi\) on
\(\mathrm{SL}_n(k)\) by pushing forward, under
(2.9cq), the finite measure
\[
 \mathcal K_k(\xi;a_2,\ldots,a_n;
                              a_2^{-1},\ldots,a_n^{-1})
 \prod_{j=2}^n|a_j|^{j-1}
                  \,d\xi\prod_{j=2}^nd^\times a_j\,dk .
 \tag{2.9ct}
\]
Its support is compact. In fact the
Schwartz support in (2.9co) bounds each
\(|a_j|\) above, and bounds \(|a_j^{-1}|\)
above after the displayed specialization.
Thus all \(a_j\), \(j\ge2\), stay in compact
subsets of \(k^\times\); \(\xi\) is bounded,
as is \(k\). Formula (2.9cq) then has compact
image. The total variation of (2.9ct) is
finite for the same reason. No singular
coordinate at zero is passed over in this
compactness argument.

Equations (2.9co)–(2.9cs) prove the exact identity
\[
 J_s(\Phi,W)=
        \int_{\mathrm{SL}_n(k)}
          Z_0(s,R(h)W,1)\,d\mu_\Phi(h).
 \tag{2.9cu}
\]
All its measures are the fixed normalized
ones, so there is no suppressed constant.
Initially the calculation is justified by
absolute convergence: (2.9ct) has finite
total variation and compact support,
and the translates \(R(h)W\) have only
finitely many values on that support.
Their \(Z_0\) integrals converge absolutely
in a common half-plane by Proposition 2.3b. Conversely
(2.9cm) proves absolute convergence of
the left side. The Fourier expansion's
additional variables stay in the compact
set just identified, which also bounds
the absolute values of every rearrangement.
Both sides continue rationally.

Finally the compactly supported measure
in (2.9cu) integrates only finitely many
actual Whittaker translates. Thus every
generalized matrix integral is a finite
linear combination of actual rank-one
Rankin–Selberg integrals. Step 1 proves
\(\mathcal I_{\rm mat}(\pi)
      \subset\mathcal I_{\rm RS}(\pi\times1)\).
Proposition 2.3k proves the reverse inclusion.
Twisting \(\pi\) by \(\chi\circ\det\)
gives (2.9ck), including every ramified
character. In rank one both sides are
exactly the already proved Tate integral
family, with exponent \(s\), so the
same equality holds. Normalization at
\(X=0\) identifies the factors uniquely.
\(\square\)

Free comparison for this determinant-one kernel:
Jacquet–Piatetski-Shapiro–Shalika,
[*Automorphic forms on GL(3), I*, author-hosted
version](https://www.math.columbia.edu/~hj/Automorphic%20forms%20on%20GL%283%29%20I.pdf),
§3.1 and §4.3, printed pp. 185–194
(PDF pp. 18–27). Those sections treat arbitrary
local rank \(r\). The coordinate formulas
(2.9co)–(2.9cu) above give the full kernel and
both ideal inclusions; the source title's
global rank does not limit this calculation.

#### Exact Fourier comparison with the rank-one family

Keep the positive trace Fourier transform of the matrix
theory, and the inverse-transpose definition of
\(\widetilde W\) in Theorem 2.3h. The transpose in the following
test is essential:
\[
 \Phi^*(g)=\widehat\Phi(g^t w_n),\qquad
 w=\operatorname{diag}(1,w_{n-1}),\qquad
 T(a,x)=
 \begin{pmatrix}a&0&0\\x&I_{n-2}&0\\0&0&1\end{pmatrix}.
 \tag{2.9cv}
\]
The middle block is absent when \(n=2\).

**Lemma 2.3m (the same compact kernel on the Fourier
side).** The actual measure \(\mu_\Phi\) in (2.9ct)
satisfies
\[
 \int_{G_n}\Phi^*(g)H(g)\,dg
  =\int_{\mathrm{SL}_n(k)}\int_{k^\times}
       \int_{k^{n-2}}H(T(a,x)w h^{-t})
             |a|^{-(n-1)}\,dx\,d^\times a\,
                                      d\mu_\Phi(h)
 \tag{2.9cw}
\]
for every smooth inverse-character Whittaker function
\(H\) of compact support modulo \(N_n\).
It also holds by absolute limits whenever both sides
have the convergence bounds just proved.

**A finite Fourier identity used in the proof.**
For a matrix Schwartz test \(f\) and \(h\in
\mathrm{SL}_n(k)\), additive self-dual measures give
\[
 \begin{split}
 &\int_k\int_{N_n}
   \widehat f\bigl(h^t\operatorname{diag}(a,I)
                                   w_n u\bigr)
                          \psi_n(u)^{-1}\,du\,da\\
 &\hspace{8mm}=
   \int_k\int_{k^{n-2}}\int_{N_n}
       f(vT(a,x)w h^{-t})\psi_n(v)\,dv\,dx\,da.
 \end{split}
 \tag{2.9cx}
\]
Here the scalar integrations include zero. This is
not a formal delta calculation. Both sides are
the Fourier orthogonality identity for an affine
matrix subspace, which can first be checked on
additive lattice-coset indicators and added.
Its exact subspace and its Jacobian are as follows.

Put \(M=\operatorname{diag}(a,I)w_nu\).
Its first row has the sole entry \(M_{1,n}=a\).
For \(1\le r<n\), its row \(n+1-r\) has
fixed entry \(M_{n+1-r,r}=1\) and entries
\(M_{n+1-r,j}=u_{rj}\) for \(j>r\).
The phase on these free entries is
\(\psi(-\sum_{r<n}u_{r,r+1})\).
Expanding the positive trace transform, and
putting \(Z=Yh^t\), therefore forces
\[
 Z_{n,1}=0,\qquad
 Z_{r+1,n+1-r}=1\ (r<n),\qquad
 Z_{j,n+1-r}=0\ (j>r+1).
 \tag{2.9cy}
\]
The residual phase is
\(\psi(\sum_{r<n}Z_{r,n+1-r})\).
Every matrix satisfying (2.9cy) is uniquely
\[
 Z=vT(a,x)w .
 \tag{2.9cz}
\]
Indeed its columns \(c\ge2\) are the
\((n+2-c)\)-th columns of \(v\): their
fixed pivot is one, their lower entries
are zero, and their upper entries supply
all the independent entries of \(v\).
Its first column has last entry zero.
Reading upwards, that column supplies
the \(n-2\) entries of \(x\), then \(a\),
by triangular equations with coefficient
one. This is a polynomial bijection
with polynomial inverse and additive
Jacobian one. Moreover
\[
 Z_{r,n+1-r}=v_{r,r+1}.
 \]
Thus the residual phase is exactly
\(\psi_n(v)\). Since \(\det h=1\),
the linear substitution \(Z=Yh^t\)
also has additive Jacobian one.
These observations prove (2.9cx),
including its character, absence of
a sign unit, and all its measures.
Lattice orthogonality proves the formula
even when a chosen lattice is not the
coordinate-unit lattice: choose dual
lattices in the free coordinates.

**Proof of (2.9cw) for compact quotient support.**
Write the inverse-character function as
\[
 H(g)=|\det g|^n
             \int_{N_n}f(ug)\psi_n(u)\,du,
                 \qquad f\in C_c^\infty(G_n).
 \tag{2.9da}
\]
Such an \(f\) exists. On finitely many
compact-open quotient charts meeting
the support of \(|\det|^{-n}H\), choose
a compact open fibre lattice and a
locally constant fibre function with
the prescribed character and integral
one. Multiply it by the finitely many
quotient values and add using a
compact-open partition. The resulting
function has the required \(N_n\)-average,
and its support is compact in \(G_n\).
Extend it by zero to the matrix space;
its support is away from the singular
locus, so this extension is Schwartz.

Define
\[
 K(X)=|\det X|^n
          \int_{N_n}\widehat f(X^t w_nu)
                           \psi_n(u)^{-1}\,du.
 \tag{2.9db}
\]
The function \(K\) is smooth and has the
positive Whittaker character. For \(v\in N_n\),
put \(v'=w_nv^tw_n\in N_n\). Its generic
character equals that of \(v\).
Replacing \(u\) by \(v'^{-1}u\) proves
\(K(vX)=\psi_n(v)K(X)\).
A sufficiently deep left matrix-test
stabilizer of \(\widehat f\), after transpose,
gives a right open stabilizer of \(K\).

Matrix Parseval and (2.9da) give
\[
 \int_G\Phi^*(g)H(g)\,dg
                      =\int_G\Phi(X)K(X)\,dX_G.
 \tag{2.9dc}
\]
To verify the indices, change \(g\) to \(u^{-1}Y\)
in its \(N_n\)-average. The Fourier phase is
\[
 \operatorname{tr}
       \bigl(XY^tu^{-t}w_n\bigr)
    =\operatorname{tr}
       \bigl(X^tw_nu^{-1}Y\bigr).
 \]
Its \(Y\)-integration is the positive
transform \(\widehat f(X^tw_nu^{-1})\).
Replacing \(u\) by \(u^{-1}\) yields
the inverse character in (2.9db).
The conversion
\[
 dg_G=\alpha_n^{-1}|\det g|^{-n}dg_{\rm add}
 \]
on both sides cancels the identical
\(\alpha_n^{-1}\), while the factor
\(|\det|^n\) in (2.9da) and (2.9db)
converts each additive integral back to
the group integral. Hence (2.9dc)
has no normalization constant.

Here is a direct absolute bound for the
double Schwartz integrals in this use
of Parseval. For any two matrix Schwartz
tests \(f_1,f_2\), the integral
\[
 \int_G|\det g|^n
      |f_1(g)|\int_N|f_2(gu)|\,du\,dg
 \tag{2.9dd}
\]
is finite. Use the right Iwasawa formula
\(G=K_n A_n N_n\), whose density is
\(\delta_{B_n}(a)\), and integrate both
right \(N_n\)-coordinates. Each upper
entry is \(a_i u_{ij}\); its Jacobian
gives the bound
\(\prod_i|a_i|^{-(n-i)}\) for each of
the two \(N_n\)-integrals. Each diagonal
coordinate is bounded above by the
two support balls. The remaining
exponent is, for every \(i\),
\[
 n+(n+1-2i)-2(n-i)=1.
 \]
Thus (2.9dd) is bounded by a constant
times \(\prod_i\int_{|a_i|\le C}|a_i|\,d^\times a_i\),
which is finite. Left \(N_n\)-averages
have the same proof by transposing.
This bound justifies the Schwartz
pairings and the limits of compact
unipotent averages in (2.9dc).

Apply the coordinate kernel construction
of Theorem 2.3l to the positive-character
function \(K\). That calculation uses
only Whittaker equivariance, smoothness
and absolute integrability; it does
not require \(K\) to be an irreducible
model. At matrix exponent zero it gives
\[
 \int_G\Phi(X)K(X)\,dX_G
   =\int\mu_\Phi(h)\int_{k^\times}
       K(\operatorname{diag}(a,I)h)
                    |a|^{-(n-1)}\,d^\times a.
 \tag{2.9de}
\]
These row integrals are absolutely
convergent: in (2.9db) along this row,
the compact support of \(\widehat f\)
bounds all the unipotent variables
uniformly and bounds \(|a|\) above;
the prefactor is \(|a|^n\).
Uniformity holds for \(h\) in the
compact support of \(\mu_\Phi\).

In (2.9de) use (2.9db), and in the
proposed right side of (2.9cw) use
(2.9da). Both have the factor
\(|a|^n|a|^{-(n-1)}d^\times a
=(1-q^{-1})^{-1}da\).
The two resulting integrals are exactly
the two sides of (2.9cx). Their
identical scalar factor cancels.
Equations (2.9dc)–(2.9de) now prove
(2.9cw).

To extend the identity, exhaust \(N_n\backslash G_n\)
by finite unions of right compact-open orbits,
at a fixed right stabilizer of \(H\).
Their characteristic functions give
Whittaker-character-preserving smooth
cutoffs with compact quotient support.
For the functions \(H\) to which we
apply the lemma, both sides converge
absolutely in the same left half-plane:
the left by the absolute generalized
matrix bound in Theorem 2.3l, and the right
by Proposition 2.3b, since the compact kernel has
only finitely many actual translates.
The cutoffs have absolute value at
most one. Dominated convergence
therefore proves the required limit.
This completes the proof of the lemma.
\(\square\)

**Theorem 2.3n (both finite Fourier scalars agree).**
For every actual generic irreducible smooth admissible
\(\pi\) of \(G_n\), and every character \(\chi\),
\[
 \gamma_{\mathrm{RS}}(s,\pi\times\chi,\psi)
       =\gamma_{\mathrm{mat}}
                 (s,\pi\otimes(\chi\circ\det),\psi),
 \qquad
 \epsilon_{\mathrm{RS}}(s,\pi\times\chi,\psi)
       =\epsilon_{\mathrm{mat}}
                 (s,\pi\otimes(\chi\circ\det),\psi).
 \tag{2.9df}
\]

**Proof.** First take \(\chi=1\) and \(n\ge2\).
The actual matrix Fourier equation extends to the
generalized coefficients (2.9cl) with exactly
the test (2.9cv):
\[
 J_{1-s}(\Phi^*,\widetilde W)
          =\gamma_{\rm mat}(s,\pi,\psi)J_s(\Phi,W).
 \tag{2.9dg}
\]
Here is the precise extension. Choose a compact
open left stabilizer \(J\) of \(\Phi\), and
replace \(\lambda\) by \(\lambda e_J\)
as in (2.9cm). Its ordinary inverse coefficient
is the average of \(W(jg^{-1})\). Put
\(h=w_ng^t\). From the definition of
\(\widetilde W\),
\[
 W(jg^{-1})=
          \widetilde W(w_nj^{-t}w_nh).
 \]
Also \(g=h^tw_n\), so its Fourier test becomes
\(\widehat\Phi(h^tw_n)=\Phi^*(h)\).
This test is left invariant under
\(w_nJ^{-t}w_n\): left invariance of
\(\Phi\) makes \(\widehat\Phi\) right
\(J^{-1}\)-invariant under the positive
trace pairing. The displayed average
can therefore be removed from its
integral. Transpose and the permutation
preserve the group Haar measure and
determinant norm. Applying the actual
matrix equation proves (2.9dg), including
its entire finite family.

Apply Lemma 2.3m to
\[
 H(g)=\widetilde W(g)
           |\det g|^{1-s+(n-1)/2}.
 \]
The weight on its row becomes
\(|a|^{1-s-(n-1)/2}\), exactly the
dual Rankin–Selberg weight for \(n\times1\).
Moreover
\(\widetilde{R(h)W}(g)=\widetilde W(gh^{-t})\).
Consequently (2.9cw) is
\[
 J_{1-s}(\Phi^*,\widetilde W)
   =\int \mu_\Phi(h)\,
       Z_{n-2}(1-s,R(w)
                       \widetilde{R(h)W},1).
 \tag{2.9dh}
\]
The rank-one character's sign is one,
so the scalar in the functional equation
of Theorem 2.3h is precisely \(\gamma_{\rm RS}\).
Apply that proved equation to each of
the finitely many translates in (2.9dh),
then use (2.9cu). This gives
\[
 J_{1-s}(\Phi^*,\widetilde W)
          =\gamma_{\rm RS}(s,\pi\times1,\psi)
                                      J_s(\Phi,W).
 \]
Both equations hold rationally, although
their original half-planes differ.
There is a nonzero \(J_s\), by the
entire ideal equality (2.9ck) and the
integral-one construction. Comparing
with (2.9dg) proves equality of scalars.
The factors and their duals agree by
Theorem 2.3l, so the normalized epsilons agree
as well. To check every ramified character with the present
sign convention, set \(W_\chi(g)=\chi(\det g)W(g)\).
Then
\[
 \widetilde W_\chi(g)=\chi(\det w_n)\chi(\det g)^{-1}\widetilde W(g).
\]
Write \(w=\operatorname{diag}(1,w_{n-1})\), as in the
dual Rankin–Selberg test. Since
\(\det w_n/\det w=(-1)^{n-1}\), that test is multiplied by
\(\chi(-1)^{n-1}\chi(a)^{-1}\).
This is precisely the extra factor converting \(\Gamma\) into
\(\gamma\) in (2.9at), so comparison for \(\pi\otimes\chi\circ\det\)
proves (2.9df). For \(\psi_b(x)=\psi(bx)\), the two already proved
character-scaling laws multiply the scalar by the identical quantity
\(\omega_\pi(b)\chi(b)^n|b|^{n(s-1/2)}\).
Thus the equality also holds for every nontrivial additive character. For \(n=1\)
the assertion is exactly the Tate
Fourier equation already proved.
\(\square\)

Let \(\sigma\) be an actual generic irreducible constituent of
\(I_P(\pi_1\otimes\pi_2)\), with actual smooth admissible irreducible
blocks. Theorem 1.23, Corollary 1.23c and (2.9df) give
\[
 \gamma_{\mathrm{RS}}(s,\sigma\times\chi,\psi)
 =\prod_{i=1}^2\gamma_{\mathrm{mat}}
       (s,\pi_i\otimes\chi\circ\det,\psi),
\]
together with their exact matrix \(L\)-polynomial correction.
When both blocks \(\pi_i\) are generic, Theorems 2.3l and 2.3n
identify each factor on the right with its Rankin–Selberg factor.
For nongeneric blocks this statement retains the proved matrix factors;
it makes no additional Rankin–Selberg definition or genericity assertion.

Free comparison: the same author-hosted
[*Automorphic forms on GL(3), I*](https://www.math.columbia.edu/~hj/Automorphic%20forms%20on%20GL%283%29%20I.pdf),
§4.5, printed pp. 194–198
(PDF pp. 27–31). Formulas (2.9cx)–(2.9cz)
give its elementary Fourier step with
the present positive *trace* convention.
This is why (2.9cv) has \(g^tw_n\).

### Whittaker induction and exact trailing-block insertion

Let \(\rho,\tau\) be actual generic smooth admissible
representations of \(G_a,G_b\), with one-dimensional
generic coinvariants. Let
\[
 I=\operatorname{Ind}_{P_{a,b}}^{G_{a+b}}
          (\rho\otimes\tau)
 \tag{2.9bo}
\]
be normalized upper-parabolic induction. It is admissible
by the complete compact-double-coset proof in Lemma 1.23a.

**Lemma 2.3o.** Its generic coinvariant is the tensor
product of those of \(\rho,\tau\), hence one-dimensional.
For every \(W_\tau\) and every
\(\Phi\in C_c^\infty(k^b)\), its Whittaker model contains
a function satisfying
\[
 W\left(\operatorname{diag}(h,I_a)\right)
       =W_\tau(h)\Phi(e_bh)|\det h|^{a/2},
       \qquad h\in G_b.
 \tag{2.9bp}
\]

**Proof of the induction assertion.** Ordinary upper
Bruhat elimination, coarsened by the Levi permutation
group, decomposes \(P_{a,b}\backslash G_{a+b}\) into
the finitely many \(N_{a+b}\)-orbits indexed by words
of \(a\) letters \(A\) and \(b\) letters \(B\).
This follows directly from pivot elimination: each
pivot records which of the two row blocks it belongs
to, and permutations internal to either block are
absorbed by the Levi. The nonzero-minor pivot charts
also give local sections and the closure ordering
by ranks of the initial column spans. Rank conditions
are closed because their defining minors are
continuous. Consequently there is a finite closed–open
filtration of smooth section spaces by these orbits.
Restriction on a closed stratum is exact: locally
constant compactly supported sections extend from
a compact-open coordinate partition, and a section
vanishing there vanishes near its compact support.

Except for the open word \(B^bA^a\), the word has
an adjacent \(AB\). The corresponding simple upper
root, conjugated by its pivot permutation, belongs
to the upper radical of \(P_{a,b}\). It acts trivially
on the inducing fibre; its prescribed generic character
is nontrivial. The homogeneous fibre-averaging argument
of Proposition 2.3g therefore kills that orbit's generic
coinvariant. There are no transverse jets.
For the open word the stabilizer consists of the
two internal upper-unipotent groups; integrating
the cross-block additive coordinates with their
generic character leaves exactly the two inducing
generic coinvariants. Exactness of twisted
coinvariants, proved in the mirabolic spectral filtration above, now identifies the
coinvariant of the entire induction with this open
one. This proves the assertion and constructs its
Whittaker functional, including on sections not
supported in the open orbit.

**The exact insertion formula.** In block rows
\((a,b)\) and block columns \((b,a)\), put
\[
 w=\begin{pmatrix}0&I_a\\I_b&0\end{pmatrix},
 \qquad u(Y)=\begin{pmatrix}I_b&Y\\0&I_a\end{pmatrix}.
 \tag{2.9bq}
\]
An open-cell section with
\(f(wu(Y))=\xi(Y)v_\rho\otimes v_\tau\),
\(\xi\in C_c^\infty(M_{b,a}(k))\), extends by zero
to an actual smooth induced section: its support
is compact inside the open flag chart. Normalize
the functional of \(\rho\) by
\(\lambda_\rho(v_\rho)=1\). On these sections the
Whittaker functional just constructed is exactly
\[
 \Lambda(f)=\int_{M_{b,a}(k)}
   (\lambda_\rho\otimes\lambda_\tau)(f(wu(Y)))
             \psi(-Y_{b,1})\,dY.
 \tag{2.9br}
\]
The sign is checked by translating \(Y\); the two
internal blocks use their original generic
functionals. Since the open and full generic
coinvariants agree, (2.9br) is its restriction,
not an asserted convergent integral for arbitrary
sections.

For \(g=\operatorname{diag}(h,I_a)\), one has
\[
 wu(Y)g=\operatorname{diag}(I_a,h)\,
            wu(h^{-1}Y).
 \]
The normalized inducing modulus contributes
\(|\det h|^{-a/2}\); replacing \(Y\) by \(hY\)
in its \(a\) columns contributes \(|\det h|^a\).
Thus \(\Lambda(R(g)f)\) is
\[
 |\det h|^{a/2}W_\tau(h)
       \int\xi(Y)\psi(-e_bhYe_1)\,dY.
 \tag{2.9bs}
\]
Choose
\(\xi(Y)=\widehat\Phi(Y e_1)\xi_0(Y_{\rm other})\),
where the remaining \(b(a-1)\) additive coordinates
have a compact Schwartz function of integral one.
For \(a=1\) that factor is absent. Positive Fourier
inversion makes the last integral precisely
\(\Phi(e_bh)\). This proves (2.9bp), with all
modulus powers and measures written. \(\square\)

In particular, if the second Rankin–Selberg rank
equals \(b\), the \(j=0\) integrals for \(I\) include
every equal-rank integral for \(\tau\): the
\(a/2\) factor in (2.9bp) cancels the unequal-rank
shift. If the second rank is smaller than \(b\),
choose \(\Phi(e_b)=1\) and embed its group in the
first coordinates of \(G_b\); its last row is
exactly \(e_b\). The same cancellation includes
every \(j=0\) integral for that smaller-rank pair.
This is an exact inducing test construction,
without importing an induced-representation
functional-equation theorem.

### The required two-parabolic Jacquet calculation, with its proof

This supplies central annihilators for induction. Its proof does
not assume finite length, the noetherian property of a Hecke
algebra, or a geometric-lemma statement from a reference.

Let \(P=P_{a,b}\) and \(Q=P_{l,n-l}\), \(n=a+b\),
be upper two-block parabolics. Write \(U_Q\) for the
radical of \(Q\), and \(M_Q=G_l\times G_{n-l}\).
For a two-block parabolic \(P_{c,d}\) write
\(r_{c,d}=\delta_{P_{c,d}}^{-1/2}(\,\cdot\,)_{U_{c,d}}\).
For \(c=0\) or \(d=0\) this is the original module
in its single nonzero block.

**Lemma 2.3p.** The normalized \(Q\)-Jacquet module of
\(I=\operatorname{Ind}_{P_{a,b}}^{G_n}(\rho\otimes\tau)\)
has a finite filtration with one quotient for each pair
\[
 0\le i\le a,\quad 0\le j\le b,\qquad i+j=l.
 \tag{2.9cc}
\]
That quotient is normalized induction on \(M_Q\) from
the four-block module
\[
 r_{i,a-i}(\rho)\otimes r_{j,b-j}(\tau),
 \tag{2.9cd}
\]
whose four factors are assigned, in order, to blocks
\((i,j)\) in \(G_l\) and \((a-i,b-j)\) in \(G_{n-l}\).
Expression (2.9cd) means the module of the indicated
four-block product group; it does not assert a tensor
decomposition of either individual Jacquet module
into simple factors.

**Proof of the orbit filtration.** The \(Q\)-orbits of
\(P\backslash G_n\) are indexed by
the dimension \(i\) of the intersection of the
represented \(a\)-plane with the fixed first
\(l\)-plane; the remaining first-plane dimension
is \(j=l-i\). Elementary pivot elimination gives
representatives which assign \(i\) coordinates
of the \(\rho\)-block and \(j\) of the
\(\tau\)-block to the first \(Q\)-block, and
their complementary coordinates to the second.
Here an \(a\)-plane can equivalently be represented
by the rows or kernels defining the coset, after
reversing all the choices consistently. The
representatives are characterized invariantly
by the block assignment just given.

For completeness, eliminate a full-rank matrix
representing that plane using changes of its
basis, and column operations preserving the
first \(l\)-plane. First choose a basis of its
intersection with that plane and move its pivots
to the first \(i\) available coordinates there.
Project its complementary vectors to the quotient
by the first plane; their independent images
give the remaining \(a-i\) pivots. Subtract
their components in the first plane and clear
the other entries by the allowed operations.
This produces the coordinate representative.
The intersection dimension is unchanged by
the operations and distinguishes the representatives.
On a fixed nonzero-minor chart these operations
are rational functions with nonzero denominators,
so they also give local continuous sections of
each orbit map. Rank inequalities describing
its boundary are closed, being vanishing
conditions on minors. Ordering the finitely
many possible intersection dimensions therefore
gives a closed–open filtration of the section
space. Its orbit quotient is the compactly
supported smooth section space on that orbit,
with the inducing fibre.

Restriction to each successive closed stratum
is onto: at the right level of a section, use
finitely many compact-open coordinate pieces
to extend its finitely many fibre values.
A section zero on that stratum is zero on
a neighbourhood of its compact support there,
and belongs to the section space of the
remaining open set. This proves exactness.
Ordinary \(U_Q\)-coinvariants are exact,
by the compact-averaging proof of the mirabolic spectral filtration above with
the trivial character; \(U_Q\) here is just
an additive matrix group. It remains to
compute the coinvariant of an individual
orbit.

**The orbit and its ordinary coinvariant.**
Choose its permutation \(w\), and put
\(H=Q\cap w^{-1}Pw\). It splits as
\[
 H=H_M H_U,\qquad
 H_M=H\cap M_Q,\quad H_U=H\cap U_Q.
 \tag{2.9ce}
\]
The group \(H_M\) is the upper parabolic
of block types \((i,j)\) and
\((a-i,b-j)\) in the two factors of \(M_Q\).
Its radical acts trivially on the inducing
fibre: its roots are from the \(\rho\)-block
to the \(\tau\)-block in \(P\).
The nontrivial \(H_U\)-actions on the fibre
are precisely \(U_{i,a-i}\) in \(\rho\)
and \(U_{j,b-j}\) in \(\tau\). Its other
roots belong to the radical of \(P\).
These descriptions follow by listing a
root's source and target among the four
blocks; a root from the first \(\tau\)
block to the last \(\rho\) block is the
only forbidden cross-block type.

In particular \(U_Q\) is abelian, and
\[
 U_Q/H_U\simeq M_{j,a-i}(k).
 \tag{2.9cf}
\]
The orbit section module is
\(\mathrm{c\!-\!Ind}_H^Q F\), with
\[
 F(h)=\delta_P(whw^{-1})^{1/2}
                     (\rho\otimes\tau)(whw^{-1}).
 \]
Taking its \(U_Q\)-coinvariant first
takes the \(H_U\)-coinvariant of \(F\),
then integrates the compactly supported
coordinates (2.9cf). Here is an explicit
proof that no kernel is omitted. On a
compact-open local chart of \(H_M\backslash
M_Q\), sections are finite sums of locally
constant functions in the additive coordinate
with finitely many fibre values. Divide the
coordinate support into cosets of a common
compact open additive lattice. A function
with integral zero is a finite sum of
differences between a coset indicator
and a translate of it. These differences
are exactly translation coinvariant
relations. Taking the \(H_U\)-coinvariant
of a finite collection of fibre values is
also exact by compact averaging. Lift its
finite relations, and then use these
coset differences. This proves both
surjectivity and the kernel assertion
locally.

There are finitely many such charts for
the compact support of the section.
Refine their compact-open partitions until
all matrix-coordinate changes, translated
coset indicators and fibre values have
common open stabilizers. A fixed translation
in \(U_Q\) then gives the required coordinate
translation throughout each piece: differences
inside the constancy lattice act trivially.
Thus the local relations are actual
\(U_Q\)-relations, not relations involving
a variable group element. Adding the finitely
many pieces proves the global assertion.
The resulting section space on \(H_M\backslash
M_Q\) is induction with a transformation
character contributed by this integration.

**The exact density calculation.** Write an
element of the four-block Levi as
\((A_1,B_1,A_2,B_2)\), with block dimensions
\((i,j,a-i,b-j)\). Its action on (2.9cf) is
\[
 z\longmapsto B_1zA_2^{-1},
 \qquad
 dz\longmapsto
       |\det B_1|^{a-i}|\det A_2|^{-j}\,dz.
 \tag{2.9cg}
\]
If a section is integrated as
\(\int f(u(z)m)\,dz\), replacing \(m\)
by \(hm\), \(h\in H_M\), conjugates
the variable by \(h^{-1}\). Changing it
back gives the *positive* Jacobian in
(2.9cg). The inducing half modulus has
exponents \(b/2,b/2,-a/2,-a/2\) on
\((A_1,A_2,B_1,B_2)\).
Multiplying by (2.9cg), and then by
\(\delta_Q^{-1/2}\) to normalize the
Jacquet module, gives the exponents
\[
 \begin{array}{c|cccc}
       &A_1&B_1&A_2&B_2\\ \hline
       &\dfrac{j-a+i}{2}
       &\dfrac{-i-b+j}{2}
       &\dfrac{b-j+i}{2}
       &\dfrac{-a+i+j}{2}.
 \end{array}
 \tag{2.9ch}
\]
These are exactly the sum of the half
modulus for induction from \((i,j)\)
and \((a-i,b-j)\), and the two negative
half moduli normalizing the inducing
Jacquet modules. This proves (2.9cd),
including its density, and finishes
the proof of the lemma. \(\square\)

**Corollary 2.3q (global central polynomials for
induced Whittaker models).** Suppose that \(\rho,\tau\)
are actual irreducible smooth admissible representations.
For \(0\le i\le a\), let \(p_{\rho,i}\) be the global
raw Jacquet polynomial of Lemma 2.3, with the conventions
\[
 p_{\rho,0}(T)=T-1,\qquad
 p_{\rho,a}(T)=T-\omega_\rho(\varpi),
 \tag{2.9ci}
\]
and similarly for \(\tau\). The raw \(Q\)-Jacquet
module of \(I\) is annihilated by the product,
over the pairs (2.9cc), of the polynomials whose
roots are
\[
 q^{\{i(a-i)+j(b-j)-l(n-l)\}/2}\alpha\beta,
 \quad
 p_{\rho,i}(\alpha)=p_{\tau,j}(\beta)=0.
 \tag{2.9cj}
\]
If the respective root multiplicities are \(u,v\),
give the product root multiplicity \(u+v-1\);
combine repeated roots by adding these
multiplicities. An empty root set means the
corresponding Jacquet quotient is zero.

**Proof.** The central element
\(\operatorname{diag}(\varpi I_l,I_{n-l})\)
acts on a normalized quotient (2.9cd)
through the two partial scalar elements of
the inducing Jacquet modules. Their normalization
contributes
\(q^{i(a-i)/2+j(b-j)/2}\).
This element is central in \(M_Q\), so the
inducing modulus on \(H_M\) is one: in each
of its two blocks the same scalar appears
on both subblocks. Returning to the raw
Jacquet module contributes
\(q^{-l(n-l)/2}\). This gives (2.9cj).
On generalized root spaces write the
two actions as \(\alpha+N\) and
\(\beta+M\), with \(N^u=M^v=0\).
After subtracting the product root,
every summand contains at least one
of \(N,M\). Its \((u+v-1)\)-st power
is zero by the pigeonhole count of the
two nilpotent powers. Bézout projections
separate the finitely many roots exactly
as in Lemma 2.3a. Thus the indicated polynomial
annihilates each orbit quotient. Applying
their polynomials successively down the
finite filtration annihilates the
whole module. \(\square\)

In particular the convergence and uniform-denominator
argument of the preceding uniform-recurrence and denominator proofs also works for this full induced
Whittaker family. One uses (2.9cj) to see that
the polynomial action is an actual finite
sum of unipotent differences on each vector;
one does not need finite generation of \(I\).
Admissibility is Lemma 1.23a and its generic
coinvariant is Lemma 2.3o. This observation prepares
the induction-family calculation; it does
not assert multiplicativity of its scalar
functional equation.

### Algebraic Whittaker families and coefficientwise continuation

We construct the inducing family over a Laurent polynomial ring
and prove specialization and uniform determinant-shell support.

Let \(A=\mathbb C[z,z^{-1}]\), and let
\(\chi_z\) denote the \(A^\times\)-valued unramified
character \(a\mapsto z^{v(a)}\). For actual generic
irreducible admissible \(\rho,\tau\), form the normalized
induction over \(A\)
\[
 I_A=\operatorname{Ind}_{P_{a,b}}^{G_{a+b}}
                  ((\rho\otimes\chi_z\circ\det)
                                      \otimes\tau).
 \tag{2.9di}
\]
Its compact picture consists of the same locally
constant functions on \(K_{a+b}\) as before,
now with fibre values in
\((V_\rho\otimes V_\tau)\otimes_\mathbb C A\).
The compatibility condition on \(P\cap K\) is
independent of \(z\), since every Levi determinant
there is a unit. Right translation by a fixed
\(g\) produces an \(A\)-valued section: its
restriction to \(K\) is computed on the compact
set \(Kg\); only finitely many Iwasawa
valuation patterns and compact fibre values
occur, so only finitely many powers of \(z\)
occur at any fixed right level.

**Lemma 2.3r.** There is an \(A\)-linear generic
functional
\[
 \Lambda_A:I_A\longrightarrow A
 \tag{2.9dj}
\]
whose specialization at each \(z_0\in
\mathbb C^\times\) is the generic functional
normalized by the open-cell integral (2.9br).
For a compact-picture section \(f\) and a
fixed \(g\),
\[
 W_f(z,g)=\Lambda_A(R(g)f)\in A.
 \tag{2.9dk}
\]
There is a common right compact open stabilizer
of this family for all \(z_0\). Every Whittaker
function in a specialized induction is obtained
by specializing such a family.

**Proof.** The exactness of ordinary and
twisted unipotent coinvariants used in the mirabolic spectral filtration above
is valid over \(A\): a compact weighted
average is an idempotent whose coefficients
are complex numbers, and the finite relations
of a vector are killed by a sufficiently
large compact average. The division involved
is only by a nonzero Haar volume in
\(\mathbb C^\times\), already a unit of \(A\).
This gives the same finite averaging proof
of injectivity, not an assertion that an
arbitrary base change is exact.

The pivot charts and closed–open orbit
filtration of Lemma 2.3o likewise work with
these fibres. Restriction and extension
use finitely many compact-open pieces,
not an infinite algebraic sum. Each
non-open orbit is killed by an adjacent
root \(AB\): the relevant radical acts
trivially, while its nonzero prescribed
character acts by a nontrivial complex
unit. The open orbit's coinvariant is
the tensor product of the two inducing
generic coinvariants, which is \(A\).
Thus the full generic coinvariant is
canonically \(A\), with its generator
fixed by the open integral. Composing
its quotient map with this identification
is (2.9dj).

Specialization of coinvariants commutes
with evaluation \(z=z_0\): both are
quotients by the same action relations,
and tensoring a quotient gives the
specialized quotient. Specialization
of the induction itself is the actual
complex induction. At each right
compact level its sections are
determined by finitely many double-coset
values, with the \(z\)-independent
compatibility on \(P\cap K\); specialize
these values or lift them as constants.
Taking the union of levels proves
surjectivity and the asserted
identification of section modules.
The open functional specializes to
the normalized one in Lemma 2.3o and is
nonzero. Formula (2.9dk) follows
because every value of an \(A\)-linear
map lies in \(A\). A right stabilizer
of \(f\) fixes all its Whittaker
functions. Conversely a specialized
Whittaker function has a section at
one such level; lift its finite
compact-picture values as constants.
This proves the last assertion.
\(\square\)

**Corollary 2.3s (uniform formal coefficients).**
In each equal- or unequal-rank integral, replace an
induced Whittaker function by (2.9dk). The coefficient
of a fixed determinant shell is a Laurent polynomial
in \(z\). The integral has only finitely many
negative powers of \(X\), with a bound independent
of \(z\). The same statements hold for its
inverse-transpose Fourier family.

**Proof.** The common right level gives a
common upper bound for all simple torus
ratios, by the nontrivial-character
argument (2.9h), independently of \(z\).
For the equal-rank family the vector
test also bounds the central coordinate
above. On a fixed determinant shell
these upper bounds bound every coordinate
below as well: solve for each valuation
in the weighted sum of the fixed
determinant valuation. Hence its
support in \(N\backslash G\) lies
in a compact set independent of \(z\).
The finitely many inverse coordinates
give a uniform lower bound on the
determinant valuation, and hence on
the occurring powers of \(X\).

For unequal ranks the large-rank
Whittaker support bounds the first
smaller-rank ratios and its final
smaller diagonal coordinate against
the trailing identity. Thus every
diagonal entry of its smaller-rank
block is bounded above. Fixing that
block's determinant bounds them all
below, as before. The rectangular
coordinates are in the common compact
set proved in Proposition 2.3b; that proof uses
only the common right level. The
smaller compact coordinates are
already compact. These observations
again give a uniform compact set
for each shell and a uniform bound
on negative determinant valuations.

On a compact set a right-level
Whittaker family (2.9dk) takes
only finitely many values in \(A\).
Integrating their finitely many
compact-open pieces is a finite
sum of those Laurent polynomials
times fixed complex volumes. This
is the desired shell coefficient.
Inverse transpose changes the common
right level to its transpose-inverse;
the fixed Weyl matrix and Fourier
test have common levels too. Repeating
the argument proves the dual statement.
\(\square\)

For several irreducible inducing blocks, iterate this construction
over the same ring \(A\). At each stage the inducing generic
coinvariant is free of rank one; the orbit filtration and weighted
compact averages above require this fact and the given action, not
irreducibility of the intermediate module. The compact picture is
still independent of the unramified parameter on its unit
compatibility subgroup. Thus constant compact-picture values lift
every specialized section and the normalized open functional remains
nonzero at every specialization. An overall norm twist multiplies a
value at a fixed matrix by a Laurent monomial.

If an intermediate block is its faithful Whittaker quotient, lift
its finitely many section values to the full inducing module, using
compact averaging to preserve their common stabilizer. Exactness of
the generic coinvariant identifies the normalized functional of that
quotient with the original one. Hence the resulting Whittaker
functions are exactly the original functions. All uniform shell and
specialization conclusions therefore hold for the iterated faithful
models used in the following arguments as well.

The global polynomials of Lemma 2.3p have an
algebraic parameter version. In (2.9cj) a
root belonging to the partial scalar
on the first inducing block is
multiplied by \(z^i\). The paired-root
polynomials have coefficients in \(A\),
and the products along the filtration
have nonzero constant terms which are
units of \(A\). They annihilate the
whole universal Jacquet module by the
same nilpotent calculation. In particular
root collisions after specialization
do not invalidate the common denominator.

Suppose therefore that a proposed identity of
Rankin–Selberg families has been multiplied by
the actual child reciprocal polynomials and
Laurent-unit epsilons, so that all its fixed
\(X\)-coefficients are Laurent polynomials
in \(z\). If it is proved for every \(z\)
in a nonempty open annulus, all those
coefficient identities hold for every
nonzero \(z\): multiply a coefficient
by a power of \(z\) and use that a
nonzero complex polynomial has finitely
many roots. This proves the coefficientwise
continuation needed to move to a
convergent inducing chamber. It supplies
that continuation input; the unproved
two-block functional-equation identity
itself is still not inferred from it.

### The exact inducing-family scope and removal of an auxiliary character

For the following induction argument the representation
need not be irreducible. Its *Whittaker function model*
means the image of the map
\(v\mapsto[g\mapsto\lambda(\rho(g)v)]\); it is a
smooth admissible quotient of the representation and
evaluation at one is faithful under all its translates.
For a reducible inducing representation its reflected
model means the functions \(\widetilde W\) in Theorem 2.3h.
This definition does not assert that inverse transpose
is an isomorphism with its ordinary contragredient.

**Lemma 2.3t.** The preceding finite-place integral theory, including the scalar
functional equation, hold for the Whittaker models
of normalized parabolic inductions of finitely
many actual generic irreducible admissible blocks.
In the reflected equation each inducing block
is dualized and the block order is reversed.
The entire rank-one ideal and scalar comparisons
the preceding rank-one ideal and Fourier comparisons hold for these function models too.

**Proof.** Iterate Lemma 2.3o to obtain generic
coinvariant of dimension one. Admissibility
is the actual Lemma 1.23a. Iterate the
two-parabolic calculation Lemma 2.3p to obtain
global central polynomials on every
ordinary two-block Jacquet module.
The iteration does not require a
tensor decomposition into irreducibles:
its filtration modules are the original
iterated Jacquet modules of the finitely
many irreducible blocks, each with
their global polynomials; exactness
and the finite filtration give a product
annihilator. Passing to the function
model is an admissible quotient.
Exactness of ordinary coinvariants
preserves the annihilators, and its
nonzero generic functional makes its
generic coinvariant one-dimensional.

In Lemma 2.3 finite generation was used only
to obtain these global annihilators.
Their polynomial action on a vector
is already a finite sum of actual
unipotent differences, by the definition
of its zero Jacquet class. The proof
of the eventual recurrences therefore
goes through unchanged. the recurrence and denominator proofs use
those recurrences and smoothness.
the mirabolic spectral filtration above is an exact spectral filtration
for arbitrary smooth modules. Its
bottom fibre in the present model
has dimension one, so Proposition 2.3d's compact
test and Corollary 2.3f's root exchange apply.
Proposition 2.3g uses global polynomials on
ordinary Jacquet modules and the
one-dimensional bottom fibre, not
a composition series or a simple
ambient module. Hence its uniqueness
bound applies. The proof of Theorem 2.3h
constructs the reflected integrals
as functions and checks their
covariance explicitly, so it also
applies to these models. The
one-dimensional bottom fibre
in the reflected model is again
Lemma 2.3o applied to the reversed dual
blocks: inverse transpose changes
an upper induction into a lower
one, and the fixed Weyl permutation
puts it in reversed upper-block
order. The actual irreducible
blocks' inverse-transpose/dual
identification was proved by the
preceding finite Whittaker theorem.
There is no assertion here identifying
the whole reducible induction
with its ordinary dual.

To be explicit about Theorem 2.3l, the
spanning argument (2.9cn) remains
valid in the faithful function
model. A nonzero vector gives
a function nonzero somewhere,
so some translate is detected
by evaluation. Compact-fixed
admissibility then makes the
evaluation translates span its
entire fixed dual space. This
replaces irreducibility at precisely
that point of the argument.
The direct inclusion Proposition 2.3k and the
kernel 2.9cu use only a faithful
Whittaker functional, smoothness
and the already proved support
bounds. Therefore both full
ideals agree.

The induced matrix scalar is the
product of the actual block matrix
scalars, by Theorem 1.23 above, iterated over blocks.
Every coefficient of the function
model is a coefficient of the
original induction: lift its
vector and compose its dual
functional with the quotient map.
Its inverse-coefficient equation
is consequently the same whole-family
matrix equation. The proof of
(2.9dg) uses that inverse coefficient
and the actual functions
\(\widetilde W\); it requires no
module isomorphism with an ordinary
dual. 2.9cw and scalar uniqueness
then prove the rank-one scalar
comparison exactly as in Lemma 2.3m.
This proves the lemma. \(\square\)

**Lemma 2.3ta (characters of arbitrarily large conductor).**
For every integer \(c\ge2\), there is a smooth character
\(\mu:k^\times\to\mathbf C^\times\) of conductor \(c\).

*Proof.* On \(U_{c-1}/U_c\), where
\(U_j=1+\mathfrak p^j\), multiplication is the additive law of the
residue field: the cross term belongs to \(\mathfrak p^c\).
For the conductor-zero additive character fixed above,
\[
 1+\varpi^{c-1}x\longmapsto\psi(\varpi^{-1}x)
 \tag{2.9dm}
\]
is well-defined and nontrivial on that quotient. Extend it to the
finite abelian group \(\mathcal O^\times/U_c\). Here is the extension
argument: if a character is defined on a subgroup \(D\) and
\(g\notin D\), let \(m\) be the least positive integer with
\(g^m\in D\); choose an \(m\)-th root \(\lambda\) of its value at
\(g^m\), and set \(\chi(dg^j)=\chi(d)\lambda^j\). The minimality of
\(m\) makes this well-defined on the generated subgroup.
Finitely many repetitions extend to the whole finite group.
Finally set \(\mu(\varpi)=1\) and use
\(k^\times=\varpi^{\mathbf Z}\mathcal O^\times\).
The character is trivial on \(U_c\) and nontrivial on \(U_{c-1}\),
so its conductor is exactly \(c\). \(\square\)

**Proposition 2.3u (sufficiently ramified auxiliary
twists have factor one).** Given finitely many
actual irreducible admissible blocks, choose a
character \(\mu\) with sufficiently large
conductor, using Lemma 2.3ta. For every one of their induced
Whittaker models \(\rho\),
\[
 L(s,\rho\times\mu)=1.
 \tag{2.9dl}
\]
The quantifier concerns all tests in the
entire family, not a vanishing spherical
integral.

**Proof.** The actual earlier Theorem
1.23e embeds every irreducible block
in a normalized induction of finitely
many Jacquet-cuspidal irreducible
blocks. Its proof terminates by
decreasing ranks and constructs the
actual embeddings; it does not invoke
a classification. Exactness of
induction and its elementary
transitivity give an embedding of
each induction under consideration
in an induction of those terminal
blocks. Transitivity follows by
evaluating an induced section as
a function on the two successive
flag quotients, and combining their
section laws: the moduli multiply
to the modulus of the refined
parabolic. Conversely restrict
to its compact quotient and use
the same finite double-coset values
to recover the iterated section.
The two maps are inverse at every
compact level and commute with
right translation.

The higher-rank terminal blocks
have matrix factor one, after
every determinant-character twist,
by the actual compact coefficient
Lemma 1.20a and Proposition 1.4.
Rank-one terminal blocks are a
finite collection of characters
\(\xi\). Take the conductor of
\(\mu\) larger than all their
conductors. Then \(\xi\mu\) is
ramified: on the last nontrivial
unit subgroup for \(\mu\), the
character \(\xi\) is trivial.
The complete Tate theory gives
factor one for each such block.
The whole refined inducing matrix
ideal is therefore \(R\), by the
actual Lemma 1.23b and its proof
of both ideal inclusions.

Every coefficient of the embedded
original induction is a coefficient
of this ambient representation:
extend a compact-fixed dual functional
linearly on the finite-dimensional
ambient fixed space and compose
with compact averaging. Quotient
coefficients of its Whittaker
model lift as just described.
Thus their entire matrix ideal
is contained in \(R\). The
rank-one ideal comparison Lemma 2.3t
puts the entire Rankin–Selberg
family in \(R\). It contains
one by Proposition 2.3d, hence equals \(R\).
Its normalized factor is one.
This proves (2.9dl). \(\square\)

### Equal-rank parabolic multiplicativity

Let \(r=a+b\), \(a,b\ge1\). Let \(\pi\) have rank \(r\), and let
\(\sigma_a,\sigma_b\) have ranks \(a,b\). They may be actual irreducible
generic admissible representations, or the faithful induced Whittaker
models covered by Lemma 2.3t. Put
\[
 \sigma=\operatorname{Ind}_{Q^-}^{G_r}(\sigma_a\otimes\sigma_b),
 \qquad
 Q^-=\left\{\begin{pmatrix}A&0\\ C&D\end{pmatrix}\right\}.
 \tag{2.11a}
\]
Induction is normalized. The blocks are realized with upper Whittaker
character \(\psi^{-1}\); \(\pi\) uses \(\psi\). A section takes values in
functions of \(h_a,h_b\), with the law
\[
 f\left(\begin{pmatrix}A&0\\ C&D\end{pmatrix}g;h_a,h_b\right)
 =\nu(A)^{-b/2}\nu(D)^{a/2}
       f(g;h_aA,h_bD).
 \tag{2.11b}
\]
Here \(\nu(g)=|\det g|\), and all additive measures are self-dual.
The Haar and quotient measures are those of Proposition 2.3b and Theorem 2.3h.

#### The needed convergence chamber, with proof

Twist the blocks to \(\sigma_a\nu^{-u},\sigma_b\nu^u\), first with \(u\)
real and sufficiently positive. The compact picture of a section is fixed.
Set
\[
 M(Y)=\max(1,|Y_{ij}|),\qquad
 H(Y)=\max\bigl(1,|\text{all square minors of }Y|\bigr)
 \quad(Y\in M_{a,b}(k)).
 \tag{2.11c}
\]
In particular \(H(Y)\ge M(Y)\).

**Lemma 2.3v.** For each fixed compact-picture section and each compact set
of \(g\)'s, the integral
\[
 W_f(g)=\int_{M_{a,b}(k)}
 f\left(\begin{pmatrix}I_a&Y\\0&I_b\end{pmatrix}g;e,e\right)
                       \psi(Y_{a1})\,dY
 \tag{2.11d}
\]
converges absolutely for all sufficiently positive \(u\), uniformly on that
compact set. It is the Whittaker function defined by Lemma 2.3o and Lemma 2.3r.

**Proof.** First record the polynomial growth bound already implicit in
the proof of Lemma 2.3. For every fixed Whittaker vector \(V\) and fixed compact
set of right translates there are \(C,D\) such that
\[
 |V(h)|\le C\,\mathcal H(h)^D,\qquad
 \mathcal H(h)=\max(1,|h_{ij}|,|(h^{-1})_{ij}|).
 \tag{2.11e}
\]
Here are the details connecting the torus recurrence to this assertion.
Use upper Iwasawa \(h=ntk\). The bottom \(j\) rows have wedge norm
\(|t_{r-j+1}\cdots t_r|\): the corresponding primitive wedge of a matrix
in \(K_r\) has norm one, and the upper-unipotent bottom-row changes have
determinant one. Every such wedge norm is at most a fixed power of
\(\mathcal H(h)\). It is at least its reciprocal to a fixed power, since
right multiplication by \(h^{-1}\) takes it to the coordinate wedge, and
its exterior-power norm is at most \(\mathcal H(h)^j\). Thus the valuations
of every \(t_i\) and every ratio \(t_i/t_{i+1}\) are bounded in absolute
value by a constant times \(1+\log_q\mathcal H(h)\).
Whittaker support gives the fixed lower valuation bounds for those ratios.
The finitely many recurrences of Lemma 2.3 bound their remaining values by
finite sums of exponential-polynomial sequences. The central recurrence
does the same in both directions for the last coordinate. Such a bound,
on this valuation interval, is at most a power of \(\mathcal H(h)\);
increase \(D\) to absorb the polynomial in its logarithm. Smoothness
leaves finitely many right-\(K_r\) vectors. Finally \(|\psi(n)|=1\).
This proves (2.11e). The same proof uses the global central polynomials of
Lemma 2.3p for an induced model.

Take lower Iwasawa
\[
 \begin{pmatrix}I&Y\\0&I\end{pmatrix}
 =\begin{pmatrix}A&0\\ C&D\end{pmatrix}k,\qquad k\in K_r.
 \tag{2.11f}
\]
The top \(a\)-row wedge gives \(\nu(A)=H(Y)\): its minors are precisely
the square minors of \(Y\), with signs and unit minors included. The first
\(a\) rows of \(k\) have primitive wedge of norm one. Determinant one
then gives \(\nu(D)=H(Y)^{-1}\).
Both the left matrix of (2.11f) and its inverse have entries bounded by
 \(M(Y)\). Multiplying by \(k^{\pm1}\) preserves this bound. In particular
the entries of \(A,D,A^{-1},D^{-1}\), being diagonal blocks of these two
matrices, have that bound.

The untwisted section on \(K_r\) takes values in a fixed finite span of
pure tensor Whittaker vectors, since it is right invariant under an open
compact subgroup. Formula (2.11e), applied to those vectors and (2.11b),
therefore bounds the integrand without its phase by
\[
 C H(Y)^{-r/2-2u}M(Y)^D
 \le C M(Y)^{D-r/2-2u}.
 \tag{2.11g}
\]
For sufficiently positive \(u\) this is integrable on the \(ab\)-dimensional
additive space: the shell \(M(Y)=q^\ell\) has measure at most
\(q^{ab\ell}\), and the resulting geometric series converges.

For \(g\) in a fixed compact set, both \(g\) and \(g^{-1}\) have bounded
entries. Exterior multiplication shows that the top wedge norm of
\(\left(\begin{smallmatrix}I&Y\\0&I\end{smallmatrix}\right)g\)
is comparable to \(H(Y)\), with uniform positive constants. Its determinant
and inverse-entry bounds are uniformly comparable as well. This proves
the asserted uniform version of (2.11g).

Changing variables in (2.11d) proves the upper Whittaker law, including
the sign: translation by an upper rectangular block \(Y_0\) multiplies
the integral by \(\psi(-Y_{0,a1})\). Its restriction to a compactly
supported open-cell section is the explicit nonzero functional of Lemma 2.3o.
Uniqueness of that functional, proved there by the finite flag filtration,
identifies (2.11d) with that construction. This proves the lemma. \(\square\)

#### The intermediate partial Fourier integral

Write \(w_j\) for the anti-diagonal permutation and set
\[
 S=w_r\operatorname{diag}(w_a,w_b),\qquad
 H_{a,b}=\left\{\begin{pmatrix}n_a&0\\ x&n_b\end{pmatrix}:
          n_a\in N_a,\ n_b\in N_b,\ x\in M_{b,a}(k)\right\}.
 \tag{2.11h}
\]
Thus \(S H_{a,b}S^{-1}=N_r\), with measure preserved: its coordinate
map is a permutation with signs of self-dual additive coordinates.
For a row Schwartz function put
\[
 (g\Phi)^{[a]}(\xi,\eta)=
       \int_{k^a}\Phi((v,\eta)g)\psi(v\xi^t)\,dv.
 \tag{2.11i}
\]
Let \(\xi_a=e_1\in k^a,\eta_b=e_b\in k^b\). Define
\[
 B_f(s)=\int_{H_{a,b}\backslash G_r}
 f(g;e,e)\,W(Sg)\,
       (g\Phi)^{[a]}(\xi_a,\eta_b)\,\nu(g)^s\,dg.
 \tag{2.11j}
\]
The integrand is well defined on the quotient. The internal \(N_a,N_b\)
characters of \(f\) cancel those of \(W(Sg)\). For a lower rectangular
translation \(x\), (2.11i) gains \(\psi(-x_{b1})\), which cancels the
cross-block Whittaker character of \(W(Sg)\).

Every determinant-shell coefficient of (2.11j) is absolutely integrable
for sufficiently positive \(u\). This can be checked directly, as follows.
Via \(g\mapsto Sg\), use \(N_r\backslash G_r\) Iwasawa coordinates \(tk\).
A representative is \(g=S^{-1}tk\). Then
\[
 f(g;e,e)=
 \nu(t_{b+1},\ldots,t_r)^{-b/2-u}
 \nu(t_1,\ldots,t_b)^{a/2+u}
 f(S^{-1}k;\operatorname{diag}(t_{b+1},\ldots,t_r),
                    \operatorname{diag}(t_1,\ldots,t_b)).
 \tag{2.11k}
\]
Polynomial growth of the finitely many block vectors bounds the last
factor by a fixed product of powers of \(\max(|t_i|,|t_i|^{-1})\).

Schwartz support and local constancy in (2.11i) give, uniformly in \(k\),
\[
 |t_b|\le C,\qquad |t_{b+1}|\ge c>0,\qquad
 |(g\Phi)^{[a]}(\xi_a,\eta_b)|
       \le C\prod_{i=b+1}^{r}|t_i|^{-1}.
 \tag{2.11l}
\]
Indeed \((v,\eta_b)S^{-1}t=(0,\ldots,0,t_b,
v_1t_{b+1},\ldots,v_at_r)\). Support bounds \(t_b\);
after changing \(v_it_{b+i}\) to new coordinates, the phase frequency
in the first of these coordinates is \(t_{b+1}^{-1}\).
A Schwartz function's Fourier transform vanishes outside a fixed compact
set: partition it into finitely many compact-open cosets and apply
additive-character orthogonality. This gives the second bound and the
displayed Jacobian. The same argument is uniform in \(k\), since
\(\Phi(\,\cdot\,k)\) ranges through finitely many functions.

Whittaker support for \(W(tk)\) gives \(|t_i/t_{i+1}|\le C'\).
Consequently all of \(t_1,\ldots,t_b\) have bounded absolute value,
and all of \(t_{b+1},\ldots,t_r\) have absolute value bounded below.
The quotient density \(\delta_{B_r}(t)^{-1}\), (2.11k), (2.11l), and
(2.11e) leave a bound of the form
\[
 C\prod_{i\le b}|t_i|^{u-D}
       \prod_{i>b}|t_i|^{-u+D}
 \tag{2.11m}
\]
on each determinant shell, after increasing the fixed \(D\).
Its extension to the product of the indicated half-lines is integrable
when \(u>D\), by independent geometric series in each valuation.
The determinant factor is constant on a shell. This proves the claim.
In particular no general intertwining-convergence theorem is a hidden
premise of the partial Fourier calculation.

#### A first-block identity with its exact Jacobians

Abbreviate \(P_a(s)=L(s,\pi\times\sigma_a)^{-1}\), and
\(P_a^\vee(1-s)=L(1-s,\pi^\vee\times\sigma_a^\vee)^{-1}\).
Let \(Z_f(s)=Z(s,W,W_f,\Phi)\). The identity is
\[
 \epsilon_a(s)P_a(s) Z_f(s)
   =\omega_{\sigma_a}(-1)^{r-1}
          P_a^\vee(1-s)\, B_f(s).
 \tag{2.11n}
\]
It is first an identity of determinant-shell formal Laurent series
in the convergence chamber; polynomials act by finite coefficient shifts.

Here is a direct derivation. Unfold (2.11d) in the equal-rank integral:
the substitution \(g\mapsto u(Y)g\) supplies \(\psi(-Y_{a1})\) from
\(W\), canceling its phase. The last row is fixed by \(u(Y)\).
The result is integration over
\((N_a\times N_b)\backslash G_r\) of \(W(g)f(g;e,e)\Phi(e_rg)\nu(g)^s\).
Each shell of \(W(g)\Phi(e_rg)\) is compact modulo \(N_r\), by the
support argument of Lemma 2.3r. Lemma 2.3v therefore justifies this unfolding
absolutely in the stated chamber.

Put \(G_j^0=\{g:\nu(g)=1\}\). Disintegrate first through
\(\operatorname{diag}(G_a^0,N_b)\), and then through
\[
 L^0=\left\{\begin{pmatrix}A&0\\ z&n_b\end{pmatrix}:
                          A\in G_a^0,\ n_b\in N_b\right\}.
 \tag{2.11o}
\]
These groups are unimodular. Write \(z=\left(\begin{smallmatrix}Y\\x\end{smallmatrix}\right)\),
\(Y\in M_{b-1,a},x\in k^a\).
For fixed outer \(h\in L^0\backslash G_r^0\) and \(x\), the inner expression is
\[
 \int_{N_a\backslash G_a}\int_{M_{b-1,a}}
 W\left[
 \begin{pmatrix}A&0&0\\Y&I_{b-1}&0\\0&0&1\end{pmatrix}
 \begin{pmatrix}I_a&0&0\\0&I_{b-1}&0\\x&0&1\end{pmatrix}h
 \right] f(h;A,e)\,\nu(A)^{s-b/2}\,dY\,dA.
 \tag{2.11p}
\]
The remaining weight is \(\Phi((x,\eta_b)h)\,dx\,dh\).
Thus (2.11p) is precisely the already proved unequal-rank functional
equation for \((\pi,\sigma_a)\), at index \(j=b-1\); its opposite index
is zero.

After that equation, replace its \(A\) by \(w_a A^{-t}\).
This transformation preserves the \(N_a\backslash G_a\) measure: the
induced automorphism on \(N_a\) permutes its additive coordinates with
signs, while inverse transpose preserves Haar measure on \(G_a\).
The reflected \(W\) becomes the **original** \(W\) evaluated at
\[
 S\operatorname{diag}(A,I_b)
       \begin{pmatrix}I_a&0&0\\0&I_{b-1}&0\\x&0&1\end{pmatrix}h.
 \tag{2.11q}
\]
The reflected block Whittaker function becomes \(f(h;A,e)\).
The determinant power is \(\nu(A)^{s-1+b/2}\).
The central-sign factor is \(\omega_{\sigma_a}(-1)^{r-1}\), exactly
the conversion from the raw scalar to \(\gamma_a\) in Proposition 2.3i.

Change \(x\) to \(xA\). Its additive Jacobian is \(\nu(A)\), so the
power becomes \(\nu(A)^{s+b/2}\).
The matrix equality
\[
 \operatorname{diag}(A,I_b)u_{\rm last}(xA)
       =u_{\rm last}(x)\operatorname{diag}(A,I_b)
 \tag{2.11r}
\]
and \(S u_{\rm last}(x)S^{-1}\in N_r\) give the multiplier
\(\psi(x_1)\). Integrating \(x\) gives exactly
\((\operatorname{diag}(A,I_b)h\Phi)^{[a]}(\xi_a,\eta_b)\),
with the **positive** Fourier kernel.
Finally (2.11b) gives
\[
 f(h;A,e)\nu(A)^{s+b/2}
        =f(\operatorname{diag}(A,I_b)h;e,e)\nu(A)^{s+b}.
 \tag{2.11s}
\]
Disintegration of \(H_{a,b}\backslash G_r\) through (2.11o) has density
\(\nu(A)^b\,dA\,dh\). To verify the sign of this density, conjugation
by \(\operatorname{diag}(A,I_b)\) takes \(z\) to \(zA^{-1}\),
whose additive determinant is \(\nu(A)^{-b}\).
Left Haar on the larger semidirect group consequently has density
\(\nu(A)^b\,dA\,dz\,dn_b\). Division by the self-dual measures of
\(N_a,N_b,z\) gives the asserted quotient formula. It converts (2.11s)
to (2.11j) without an extra measure constant.

All interchanges with \(P_a,P_a^\vee,\epsilon_a\) involve finitely many
shell shifts. Within a fixed shell, the transformed inner \(A,x\) domain
has compact support modulo \(N_a\). For fixed \(h\), write
\(A=n\operatorname{diag}(t_1,\ldots,t_a)k\).
The internal unipotent \(n\) moves through \(S\) into \(N_r\).
The right factor \(\operatorname{diag}(k,I_b)h\) ranges over a compact set,
so its finitely many Whittaker translates have a common ratio support
bound. Applied to the diagonal
\((1,\ldots,1,t_1,\ldots,t_a)\), this gives \(|t_1|\ge c_h\) and
\(|t_i/t_{i+1}|\le C_h\). All \(t_i\) are consequently bounded below.
Their fixed determinant-shell product bounds them above as well.
Choose these compact representatives of \(N_a\backslash G_a\).
Schwartz support of \(\Phi((xA,\eta_b)h)\) then bounds \(x\) in a
compact set. These bounds justify commuting the polynomial with the
\(x\)-integral before applying its Fourier transform. The remaining outer integration
is absolutely convergent by (2.11m). One may equivalently apply compact
cutoffs first and use these bounds to pass to the limit. This proves
(2.11n) with the exact stated measures. \(\square\)

#### Comparing the two partial transforms

The reversed lower induction of
\((\sigma_b^\vee,\sigma_a^\vee)\), with character \(\psi\), has section
\[
 f^\vee(g;h_b,h_a)=
 f(S^{-1}g^{-t};w_a h_a^{-t},w_b h_b^{-t}).
 \tag{2.11t}
\]
Its section law follows directly from (2.11b). Its Whittaker function
is \(\widetilde W_f(g)=W_f(w_r g^{-t})\).
Indeed, for its upper rectangular coordinate \(Z\in M_{b,a}\),
put \(Y=-w_a Z^t w_b\) in (2.11d). The Jacobian is one,
\(Y_{a1}=-Z_{b1}\), and the two block Weyl factors in (2.11t) move
to the left using (2.11b); their product with \(S^{-1}\) is \(w_r\).
This proves the assertion including its additive-character sign.

Apply (2.11n) to \((\widetilde W,f^\vee,\widehat\Phi)\), at \(1-s\),
with blocks reversed and additive character \(\psi^{-1}\).
Its intermediate integral is the same \(B_f(s)\).
To check this without a sign convention left implicit, substitute
\(g=w_r h^{-t}\). Formula (2.11t) then gives
\(f^\vee(g;e,e)=f(h;e,e)\), because
\(S^{-1}w_r=\operatorname{diag}(w_a,w_b)\) and the block Weyl
factors square to one. Also
\(\widetilde W(S^{-1}g)=W(Sh)\).
The change of quotient measure is one by the same permutation and
inverse-transpose calculation as above.

The remaining Fourier identity is
\[
 \bigl((w_r h^{-t})\widehat\Phi\bigr)^{[b]}_{\psi^{-1}}
                                  (e_1,e_a)
   =\nu(h)\,(h\Phi)^{[a]}_{\psi}(e_1,e_b).
 \tag{2.11u}
\]
For proof let \(F(y)=\Phi(yh)\); then
\(\widehat F(x)=\nu(h)^{-1}\widehat\Phi(xh^{-t})\).
The left integral, divided by \(\nu(h)\), is
\(\int_{k^b}\widehat F(e_1,u)\psi(-u_b)\,du\),
after reversing the \(b\) coordinates. Expand the positive Fourier
transform. Orthogonality in \(u\) sets the last \(b\) row coordinates
equal to \(e_b\), leaving
\(\int_{k^a}F(v,e_b)\psi(v_1)\,dv\), as required.
This calculation is valid on compact-open coset indicators by finite
additive orthogonality and hence for every Schwartz function by linearity.
The factor \(\nu(h)\) changes \(\nu(g)^{1-s}=\nu(h)^{s-1}\)
to precisely the determinant power of (2.11j).

Both intermediate integrals are absolutely convergent in the same
chamber: reversal and duality change the twisted blocks to
\(\sigma_b^\vee\nu^{-u},\sigma_a^\vee\nu^u\).
The above change of variables also verifies this directly.
Consequently the second partial identity is
\[
 \epsilon_b^\vee(1-s,\psi^{-1})P_b^\vee(1-s)\,
                   Z^\vee_f(1-s)
 =\omega_{\sigma_b}(-1)^{r-1}P_b(s)\,B_f(s).
 \tag{2.11v}
\]
Use the proved reflection identity 2.9aw,
\(\epsilon_b^\vee(1-s,\psi^{-1})\epsilon_b(s,\psi)=1\),
and (2.11n). We obtain
\[
 P_a^\vee(1-s)P_b^\vee(1-s)\,Z_f^\vee(1-s)
 =\omega_\sigma(-1)^{r-1}
       \epsilon_a(s)\epsilon_b(s)P_a(s)P_b(s) Z_f(s).
 \tag{2.11w}
\]

#### The theorem and the polynomial correction

**Theorem 2.3w.** For the entire induced Whittaker model in (2.11a),
\[
 \gamma(s,\pi\times\sigma,\psi)
   =\gamma(s,\pi\times\sigma_a,\psi)
                 \gamma(s,\pi\times\sigma_b,\psi),
 \qquad
 \frac{L(s,\pi\times\sigma)}
 {L(s,\pi\times\sigma_a)L(s,\pi\times\sigma_b)}
                         \in\mathbf C[q^{-s}].
 \tag{2.11x}
\]
The quotient polynomial has constant term one.
This theorem asserts the exact polynomial correction, not unconditional
equality of the three \(L\)-factors.

**Proof.** First in the chamber, the right side of (2.11w), as a formal
series in \(X=q^{-s}\), is bounded below in exponent. Its left side is
bounded above, since \(Z_f^\vee(1-s)\) is a series in \(q^{-1}X^{-1}\).
Their equality therefore makes both sides finite Laurent polynomials.
Since \(\epsilon_a\epsilon_b\) is a Laurent unit, this shows
\[
 P_a(s)P_b(s)\,Z_f(s)\in\mathbf C[X,X^{-1}]
 \tag{2.11y}
\]
for every actual triple of tests.
Comparing (2.11w) with the scalar equation of the preceding scalar-equation and normalization proofs and using a nonzero
test gives the asserted product of \(\gamma\)'s.

Finally remove the chamber restriction. Lemma 2.3r constructs the universal
compact-picture sections over \(\mathbf C[z,z^{-1}]\), \(z=q^u\),
with a common right level and Laurent-polynomial determinant-shell
coefficients for their Whittaker functions and reflected functions.
The two block polynomials in (2.11w) are the original polynomials with
\(X\) replaced by \(z^{-1}X\) or \(zX\). Their epsilon factors have the
same substitutions and are Laurent units. Thus each coefficient of
the difference in (2.11w) is a Laurent polynomial in \(z\).
It vanishes for every sufficiently large positive real \(z\), and so
vanishes identically: multiply by a power of \(z\) and use that a
nonzero polynomial has only finitely many roots. This proves (2.11w),
and hence (2.11y) and the scalar identity, for every specialization,
including the original induction and every collision of parameters.
No analytic continuation theorem for induced representations is used.

Let \(P_\sigma(0)=1\) be the reciprocal generator of the full ideal.
By Proposition 2.3d the ideal is \(P_\sigma^{-1}\mathbf C[X,X^{-1}]\).
Its finite test-data attainment and (2.11y) give
\(P_\sigma\mid P_aP_b\) in the Laurent polynomial ring.
All three polynomials have nonzero constant term one, so this is
polynomial divisibility in \(\mathbf C[X]\). Consequently
\(P_aP_b/P_\sigma\) is a polynomial of constant term one and is exactly
the quotient in (2.11x). \(\square\)

### Parabolic multiplicativity with a strictly larger fixed rank

Let the fixed rank be \(r>t=a+b\), with \(a,b\ge1\).
Put \(d=r-t\), and let \(\sigma\) be the full lower normalized induction
of \(\sigma_a,\sigma_b\) as in (2.11a)–(2.11b). All representations have
the scope of Theorem 2.3w. Write \(j=d-1\) initially, so the opposite index is zero.
There is at least one intervening identity coordinate even when \(d=1\).
The direct integral is
\[
 Z_j(s)=\int_{N_t\backslash G_t}\int_{M_{j,t}}
 W(T_j(g,z))W_f(g)\nu(g)^{s-d/2}\,dz\,dg,
 \quad
 T_j(g,z)=\begin{pmatrix}g&0&0\\z&I_j&0\\0&0&I_{d-j}\end{pmatrix}.
 \tag{2.12a}
\]

For bookkeeping, the following matrix notation also describes the
opposite calculation at index zero. If \(j+k=d-1\), partition the \(r\)
coordinates as \((a,k,1,j,b)\), and put
\[
 U_{a,k,1,j,b}(X,Y)=
 \begin{pmatrix}
 I_a&X&0&0&0\\
 0&I_k&0&0&0\\
 0&0&1&0&0\\
 0&0&0&I_j&Y\\
 0&0&0&0&I_b
 \end{pmatrix},
 \quad X\in M_{a,k},\quad Y\in M_{j,b}.
 \tag{2.12b}
\]
Empty blocks and their integrals have the usual value one.
Let \(D_a=\operatorname{diag}(w_a,w_{r-a})\), and define
\[
 B_{a,b;j,k}(s)=
 \int_{H_{a,b}\backslash G_t}\int_{M_{a,k}}\int_{M_{j,b}}
 f(g;e,e)\,
 W\left[w_r U_{a,k,1,j,b}(X,Y)D_a
                  \operatorname{diag}(g,I_d)\right]\,
 \nu(g)^{s-d/2+j}\,dY\,dX\,dg.
 \tag{2.12c}
\]
Here \(H_{a,b}\) is (2.11h) in \(G_t\). The formula is invariant under its
left action, with the rectangular variables changed accordingly.
One can also establish this directly from the quotient disintegration
used in the next proof; that construction fixes its measures.
Only \(k=0\), and the reflected \(j=0\) instance, are needed below.

#### The first-block identity

With the polynomial and epsilon notation of the first-block identity (2.11n), we have
\[
 \epsilon_a(s)P_a(s)\,Z_j(s)
 =\omega_{\sigma_a}(-1)^{r-1}
       P_a^\vee(1-s)\,B_{a,b;j,k}(s).
 \tag{2.12d}
\]
For \(j=d-1,k=0\), this is an identity of absolutely integrable
determinant-shell coefficients in the same positive-\(u\) chamber as Lemma 2.3v.
The reflected identity at \(j=0,k=d-1\) has the same interpretation.

**Matrix derivation.** Unfold the upper rectangular integral (2.11d).
Its phase cancels the upper character of \(W\); changing \(z\) by the
corresponding unipotent column operation has additive Jacobian one.
The resulting outer quotient is \((N_a\times N_b)\backslash G_t\).
Disintegrate through the unimodular groups (2.11o), now inside \(G_t^0\).
Write a lower rectangular coordinate of its \(G_t\) variable as
\(z_0\in M_{b,a}\). Split the original \(j\times t\) rectangle into
its first \(a\) and last \(b\) columns. The former together with \(z_0\)
gives a \((b+j)\times a\) rectangle. For fixed remaining variables,
the inner integral is the Rankin–Selberg integral for
\((\pi,\sigma_a)\) at index \(b+j\).
Its determinant exponent is
\[
 s-d/2-b/2=s-(r-a)/2;
 \tag{2.12e}
\]
the extra \(-b/2\) is exactly the section modulus (2.11b).
Its opposite index is \(k=r-a-1-(b+j)\).

For clarity the right translation in this integral is
\[
 h_*=
 u_{\mathrm{lower},j,b}(Y_0)\operatorname{diag}(h,I_d),
 \tag{2.12f}
\]
where \(u_{\mathrm{lower},j,b}\) has its entries in rows
\(t+1,\ldots,t+j\) and columns \(a+1,\ldots,t\).
The \(b+j\) first-column rectangle and (2.12f) multiply to precisely
the unfolded matrix in (2.12a).
In passing the original rectangular variable through \(h\), its Jacobian
is \(\nu(h)^j=1\), because the outer representative is in \(G_t^0\).

Apply the already proved equation 2.9ai to this inner integral.
Its dual test uses the **right** translation
\(\rho(w_{r,a})\widetilde W_{h_*}\), with
\(w_{r,a}=\operatorname{diag}(I_a,w_{r-a})\).
For a dual rectangle \(Z\in M_{k,a}\) its Whittaker value is
\[
 W\left[w_r T_k(B,Z)^{-t}w_{r,a}h_*\right].
 \tag{2.12g}
\]
In particular the right translation cannot be moved to the left of
\(T_k\) when \(k>0\).
Replace \(B\) by \(w_a A^{-t}\), and change \(Z\) to
\[
 X=-w_a A Z^t\in M_{a,k}.
 \tag{2.12h}
\]
The Jacobian in (2.12h) is \(\nu(A)^k\). Direct multiplication gives
\[
 w_r T_k(w_a A^{-t},Z)^{-t}w_{r,a}
 =w_r U_{a,k}(X)D_a\operatorname{diag}(A,I_{r-a}).
 \tag{2.12i}
\]
Conjugating the lower rectangle in (2.12f) by \(D_a\) converts it,
by reversal of its row and column coordinates, into the \(Y\)-block
of (2.12b). This reversal has Jacobian one, and it commutes with its
disjoint \(X\)-block. The reflected block Whittaker function becomes
\(f(h;A,e)\).

After (2.12h) the determinant power is
\(\nu(A)^{s-1+(r-a)/2-k}\).
Using (2.11b) adds \(b/2\), and quotient disintegration adds the density
\(\nu(A)^b\) on \(H_{a,b}\backslash G_t\). The remaining exponent is
\[
 s-1+(r-a)/2-k+b/2-b
     =s-d/2+j.
 \tag{2.12j}
\]
This verifies every determinant power and the rectangular Jacobian in
(2.12c). Conversion from the raw functional-equation scalar supplies
\(\omega_{\sigma_a}(-1)^{r-1}\), as in the first-block identity (2.11n).
It proves (2.12d), provided the indicated coefficient integrals and
interchanges are justified. They are justified next.

#### Rectangular support and shellwise absolute convergence

We prove the required bounds for \(j=d-1,k=0\).
Conjugating the lower rectangle (2.12f) by
\(S_{r,a}=w_rD_a\), instead of by \(D_a\) alone, puts it in rows
\(b+1,\ldots,b+j\), columns \(1,\ldots,b\). Its coordinates may be
reversed, with no change in measure. Use
\(S_t=w_t\operatorname{diag}(w_a,w_b)\) to identify
\(H_{a,b}\backslash G_t\) with \(N_t\backslash G_t\).
In its Iwasawa coordinates \(g=S_t^{-1}\operatorname{diag}(t_1,\ldots,t_t)k\),
the Whittaker matrix in (2.12c) is therefore
\[
 \operatorname{diag}(t_1,\ldots,t_b,I_d,
                 t_{b+1},\ldots,t_t)\,
 u_{\mathrm{lower}}(Y\operatorname{diag}(t_1,\ldots,t_b))\,k_*,
 \tag{2.12k}
\]
where \(k_*\) ranges through a fixed compact subset of \(K_r\).
The lower rectangle in (2.12k) has \(j\) rows; the final row of the
middle \(I_d\) remains untouched.

The following support implications are uniform for the finitely many
right-\(k_*\) translates of \(W\):
\[
 \begin{split}
 |Y_{\ell i}t_i|&\le C &&(\ell\le j,\ i\le b),\\
 |t_i|&\le C &&(i\le b),\\
 |t_i|&\ge c>0 &&(i>b).
 \end{split}
 \tag{2.12l}
\]
Here is the wedge proof, to make the constant in the identity block
meaningful. Remove \(k_*\) by changing the Whittaker vector.
The final \(a\) rows of the displayed matrix are the pure diagonal rows
with entries \(t_{b+1},\ldots,t_t\). Their successive bottom-row wedges
give precisely those Iwasawa diagonal absolute values.
Adding the last middle identity row multiplies their wedge norm by one.
Thus the last middle Iwasawa diagonal has absolute value one.
The ratio support bound (2.9l), propagated upwards, bounds all preceding
Iwasawa diagonal absolute values by a fixed constant.

For each preceding middle row, its bottom-row wedge, divided by the
product of the tail diagonal entries, has a coefficient equal, up to
sign, to \(Y_{\ell i}t_i\). Choose column \(i\), all subsequent identity
columns, and all tail columns; the identity and tail submatrix is
triangular. The other entries in column \(i\) lie below the selected
row and do not change that triangular determinant. The wedge bound
therefore gives the first assertion of (2.12l), just as in (2.9m).
Its bounded rectangle now ranges through one compact subset.
Smoothness leaves finitely many right translates under that subset.
Apply the ratio support bound again to the pure diagonal part of (2.12k).
The last first-block coordinate is adjacent to a middle coordinate one,
giving all first-block upper bounds. The last middle coordinate one is
adjacent to the first tail coordinate, giving its lower bound and then
the lower bounds for the remaining tail. This proves (2.12l).

For fixed torus coordinates, the first line of (2.12l) bounds the measure
of the \(Y\)-domain by
\[
 C\prod_{i\le b}|t_i|^{-j}.
 \tag{2.12m}
\]
On this domain the rectangular right translates are in a fixed compact
set. Formula (2.11e) bounds their Whittaker values by a fixed product of
powers of \(\max(|t_i|,|t_i|^{-1})\).
The section formula (2.11k), the quotient density, and (2.12m) give,
after increasing a fixed \(D\), the bound
\[
 C\prod_{i\le b}|t_i|^{u-D}
       \prod_{i>b}|t_i|^{-u+D}
 \tag{2.12n}
\]
on each determinant shell. The remaining determinant factor is constant
there. For \(u>D\) this is integrable over the product of the first-block
bounded half-lines and the tail half-lines bounded away from zero.
This proves shellwise absolute convergence of (2.12c).

The original unfolding is justified by Lemma 2.3v. In (2.12a) the extra rectangle
is uniformly compact by (2.9l)–(2.9m). On a fixed determinant shell the
remaining Whittaker variable is compact modulo its full upper unipotent,
by the same ratio bounds and its last fixed coordinate one. Thus Lemma 2.3v
is used on a compact set of representatives.

The polynomial interchanges in (2.12d) can also be made shell by shell.
For fixed outer \(h\), the transformed \(A\)-variable has all its
Iwasawa diagonal entries bounded on one side by a retained middle
coordinate one. With its determinant shell fixed, their product bounds
them on the other side. The associated rectangle is compact by the
same bottom-wedge computation above; if rescaled by \(A\), its
Jacobian is exactly (2.12h). Consequently this inner domain is compact
modulo \(N_a\). Each polynomial shifts only finitely many shells, and
the outer domain has the absolutely integrable bound (2.12n).
Cutoffs and these bounds give the same justification without a choice
of quotient representatives.

#### The reflected rectangular integral is the same one

The reflected equal-rank-\(t\) section is the actual section (2.11t),
using \(S_t\). Its Whittaker function is \(\widetilde W_f\).
Apply (2.12d) to the reversed blocks, parameter \(1-s\), additive character
\(\psi^{-1}\), and first Whittaker test
\(\rho(w_{r,t})\widetilde W\). Its direct index is \(k=0\);
its opposite inner index is \(j=d-1\). This is exactly the dual integral
in 2.9ai for the direct test (2.12a).

Its intermediate integral is \(B_{a,b;j,0}(s)\), with no Fourier
transform or determinant constant remaining. We verify that fact
explicitly. Change \(g=w_t h^{-t}\). As in (2.11t),
the section becomes \(f(h;e,e)\). The matrix value of \(W\) becomes
\[
 W\left[
 U_{b,j,1,0,a}(X',Y')^{-t}
  D_b\operatorname{diag}(w_t,w_d)
                   \operatorname{diag}(h,I_d)\right].
 \tag{2.12o}
\]
In this case \(Y'\) is empty. The general notation permits the following
check for any \(j+k=d-1\), which also verifies that no zero-sized block
convention causes an error. The permutation identity is
\[
 D_b\operatorname{diag}(w_t,w_d)=w_rD_a.
 \tag{2.12p}
\]
Furthermore
\[
 w_r U_{b,j,1,k,a}(X',Y')^{-t}w_r
       =U_{a,k,1,j,b}(X,Y),
 \quad
 X=-w_a(Y')^tw_k,\quad
 Y=-w_j(X')^tw_b.
 \tag{2.12q}
\]
Both off-diagonal blocks in (2.12b) are disjoint, so inverse transpose
adds no cross term. Reversal, negative transpose and permutation have
additive Jacobian one. Equations (2.12p)–(2.12q) turn (2.12o) into the
Whittaker matrix in (2.12c).
The determinant exponent also agrees:
\[
 \nu(g)^{\,1-s-d/2+k}
     =\nu(h)^{\,s-1+d/2-k}
     =\nu(h)^{\,s-d/2+j}.
 \tag{2.12r}
\]
Inverse transpose and multiplication by \(w_t\) preserve the quotient
measures; their maps on the unipotent coordinates have Jacobian one.
This proves equality of the two intermediate integrals.
It also proves their equal absolute bounds, including for the reflected
index-zero calculation whose outer rectangle is an upper one.

Thus the two block identities combine, by 2.9aw, to
\[
 P_a^\vee(1-s)P_b^\vee(1-s)
 Z_0(1-s,\rho(w_{r,t})\widetilde W,\widetilde W_f)
 =\omega_\sigma(-1)^{r-1}
       \epsilon_a(s)\epsilon_b(s)P_a(s)P_b(s)Z_{d-1}(s).
 \tag{2.12s}
\]

#### Conclusion

**Theorem 2.3x.** For every fixed rank \(r\ge a+b\) and the entire
normalized induced Whittaker model \(\sigma\),
\[
 \gamma(s,\pi\times\sigma,\psi)
 =\gamma(s,\pi\times\sigma_a,\psi)
                  \gamma(s,\pi\times\sigma_b,\psi),
 \qquad
 \frac{L(s,\pi\times\sigma)}
 {L(s,\pi\times\sigma_a)L(s,\pi\times\sigma_b)}
                 \in\mathbf C[q^{-s}],\quad P(0)=1.
 \tag{2.12t}
\]

**Proof.** Equal rank is Theorem 2.3w. In strictly unequal rank use (2.12s).
One side has exponents bounded above and the other exponents bounded
below, so both are Laurent polynomials. Hence \(P_aP_b\) clears every
direct integral at index \(d-1\). Its entire ideal is the full ideal,
by the written root-exchange Corollary 2.3f. Finite test-data attainment therefore
gives polynomial divisibility \(P_\sigma\mid P_aP_b\), with all constant
terms one.
Comparing (2.12s) with 2.9ai and a nonzero test gives the scalar product.
Finally Lemma 2.3r's Laurent-polynomial shell families and norm-twist
substitutions extend the cleared identity from sufficiently positive
real \(u\) to every specialization, by the coefficientwise polynomial
root argument in the proof of Theorem 2.3w. This proves (2.12t) for every original block
parameter, without invoking an unproved induced analytic-family theorem.
\(\square\)

### The adjacent-rank character case

Let \(\pi,\rho\) have rank \(r\ge1\), and let \(\mu:k^\times\to\mathbf C^\times\)
be a smooth character. Let
\[
 \sigma=\operatorname{Ind}_{Q^-}^{G_{r+1}}(\rho\otimes\mu),
 \qquad Q^-=\left\{\begin{pmatrix}A&0\\ c&a\end{pmatrix}\right\}.
 \tag{2.13a}
\]
We use the entire faithful Whittaker model of this induction. The first
representation \(\sigma\) uses \(\psi\), its rank-\(r\) inducing model
\(\rho\) uses \(\psi\), and the second representation \(\pi\) uses
\(\psi^{-1}\). Their inverse-transpose functions use the inverse
characters. This choice makes the larger-rank ordering explicit.
The scope permits actual irreducible generic admissible \(\pi,\rho\)
and the admissible induced models proved in Lemma 2.3t.

#### A rectangular Schwartz kernel

Write \(E=k^{r\times(r+1)}\), with elements \([x,y]\), where
\(x\in M_r(k)\) and \(y\in k^r\) is a column. Let \(e=e_r^t\).
Define
\[
 T\Phi(x,\eta)=\int_{k^r}\Phi(x,y)\psi(-\eta^ty)\,dy,
 \qquad R(g)\Phi(M)=\Phi(Mg),\qquad
 \rho_0(g)=T R(g)T^{-1}.
 \tag{2.13b}
\]
All measures are self-dual. Compact-open character orthogonality makes
\(T\) a bijection of the Schwartz space. In particular
\[
 \begin{split}
 \rho_0(\operatorname{diag}(h,1))\Phi(x,\eta)&=\Phi(xh,\eta),\\
 \rho_0\left(\begin{pmatrix}I&v\\0&1\end{pmatrix}\right)\Phi(x,\eta)
       &=\psi(\eta^txv)\Phi(x,\eta),\\
 \rho_0(\operatorname{diag}(I,a))\Phi(x,\eta)
       &=|a|^{-r}\Phi(x,a^{-1}\eta).
 \end{split}
 \tag{2.13c}
\]
Each identity follows by its indicated linear substitution in (2.13b);
in particular the middle sign is positive.

For a Whittaker vector \(V\) of \(\rho\), put
\[
 W_{\Psi,V,\mu}(g)=
 \mu(\det g)\nu(g)^{r/2}
 \int_{G_r}(\rho_0(g)\Psi)(h,h^{-t}e)
      V(h^{-1})\mu(\det h)\nu(h)^{(r-1)/2}\,dh.
 \tag{2.13d}
\]
The Haar measure on \(G_r\) has \(K_r\)-volume one.
For a finite sum of pure tensor kernels sum (2.13d) by linearity.

**Lemma 2.3y.** The integral (2.13d) is absolutely convergent for every
fixed \(g,\Psi,V,\mu\). In a sufficiently positive unramified twist of
\(\mu\), its functions span the entire Whittaker model in (2.13a).

**Proof of convergence.** Reduce to \(g=e\), since \(\rho_0(g)\Psi\)
is still Schwartz, and then to
\(\Psi(x,y)=\Phi_1(x)\Phi_2(y)\).
Use right-unipotent Iwasawa \(h=k an\).
Then \(V(h^{-1})=V(n^{-1}a^{-1}k^{-1})\).
Whittaker support gives
\(|a_{i+1}/a_i|\le C\) on its support, uniformly in the finite
set of \(k\)-translates. Moreover
\(h^{-t}e=k^{-t}a^{-1}e\), because \(n^{-t}e=e\).
The compact support of \(\Phi_2\) therefore gives
\(|a_r|\ge c>0\), and the ratio bounds give lower bounds for all
\(|a_i|\). Compact support of \(\Phi_1(h)\) bounds the entries of
\(an\), so its diagonal entries \(a_i\) are bounded above, and,
using their lower bounds, every entry of \(n\) is bounded.
The integration is consequently over a compact subset of \(G_r\).
This proves convergence, with no assumption on \(\mu\).

**Proof of spanning in a chamber.** First use a Schwartz function
\(\Phi\) supported in the open full-row-rank subset of \(E\), and set
\(\mu_0=[I_r,0]\). Define a section with values in the \(\rho\) model by
\[
 f_\Phi(g;m)=\mu(\det g)\nu(g)^{r/2}
 \int_{G_r}\Phi(h\mu_0g)V(mh^{-1})
       \mu(\det h)\nu(h)^{(r+1)/2}\,dh.
 \tag{2.13e}
\]
The integral is over a compact set: the support is compact inside the
full-rank open subset, and the embedding \(h\mapsto h\mu_0g\) has
compact inverse image there. A change \(h\mapsto hA^{-1}\) proves
\[
 f_\Phi\left(\begin{pmatrix}A&0\\c&a\end{pmatrix}g;m\right)
 =\mu(a)|a|^{r/2}\nu(A)^{-1/2} f_\Phi(g;mA),
 \tag{2.13f}
\]
the exact normalized lower-parabolic section law.

These sections span the induction. To prove this concretely, cover its
compact flag quotient by finitely many matrix charts where a specified
row minor is invertible. The full-rank frame above such a chart is
uniquely \(h\mu_0g(q)\), \(h\in G_r\), after choosing the chart section
\(g(q)\). Partition an arbitrary smooth section into compact-open
pieces in these charts; each piece has values in a finite span of
fixed vectors. For a single vector \(V\) and a scalar compact-open
chart function \(c(q)\), choose an open compact \(J\subset G_r\)
fixing \(V\) with \(\mu(\det J)=1\). Prescribe
\(\Phi(h\mu_0g(q))\) to equal its required scalar multiple of
\(c(q)1_J(h)/\operatorname{vol}(J)\), absorbing the nonzero factor
\(\mu(\det g(q))\nu(g(q))^{r/2}\).
This is a locally constant compactly supported function on the chart
of the full-rank open set and extends by zero to a Schwartz function
on \(E\). Formula (2.13e) recovers that section piece exactly.
Their finite sum proves spanning.

For \(\mu=\mu_0\nu^u\) with sufficiently positive real \(u\), Lemma 2.3v,
after separating the overall central norm twist, justifies its upper
Jacquet integral absolutely. Its phase is \(\psi(-v_r)\), because this
larger Whittaker model has character \(\psi\). Substitute (2.13e) and
change \(y=hv\). The Jacobian is \(\nu(h)^{-1}\), the phase becomes
\(\psi(-(h^{-t}e)^ty)\), and the power \((r+1)/2\) becomes \((r-1)/2\).
The result is (2.13d) with \(\Psi=T\Phi\).
This proves spanning of the Whittaker functions in that chamber.
It uses the actual section construction, not a source assertion about
generic newvectors. \(\square\)

#### The exact rectangular Fourier identity

Use the positive entrywise Fourier transform
\[
 \widehat\Psi(X,Y)=\int_E\Psi(A,B)
                 \psi(\operatorname{tr}(A^tX)+B^tY)\,dA\,dB.
 \tag{2.13g}
\]
It commutes with \(T\). Direct linear substitution gives
\[
 \widehat{\rho_0(g)\Psi}
       =\nu(g)^{-r}\rho_0(g^{-t})\widehat\Psi.
 \tag{2.13h}
\]
Let \(\zeta=\operatorname{diag}(-I_r,1)\). Then
\[
 \widetilde W_{\Psi,V,\mu}(g)
       =W_{\widehat\Psi,\widetilde V,\mu^{-1}}(\zeta g),
 \qquad \widetilde V(h)=V(w_rh^{-t}).
 \tag{2.13i}
\]
This equality will be proved rather than imported from the source's
“completely analogous” argument.
The operator \(\rho_0\) on its right remains the operator (2.13b) for
the original \(\psi\). With \(\widetilde V\) it has inverse internal
root characters and a positive last root; evaluation at \(\zeta g\)
negates that last root and gives the actual full inverse Whittaker
character. Thus (2.13i) does not silently replace the last-column
Fourier operator by one for \(\psi^{-1}\).

First establish the affine Fourier identity, for every \(h\in G_r\):
\[
 \begin{split}
 &\int_{N_r}
   (\rho_0(w_{r+1})\Psi)(hn,h^{-t}e)\psi^{-1}(n)\,dn\\
 &\qquad=\nu(h)^{-(r-1)}
       \int_{N_r}\widehat\Psi(-h^{-t}w_rn,he_1)
                                      \psi(n)\,dn.
 \end{split}
 \tag{2.13j}
\]
Here the \(e_1\) on the right is a column of length \(r\).
For proof, expansion of the conjugated last-column transform in (2.13b)
gives
\[
 (\rho_0(w_{r+1})\Psi)(X,Y)
 =\int_{k^r}\int_{k^r}
 \Psi([v,X_r,X_{r-1},\ldots,X_2],z)
                 \psi(z^tX_1-Y^tv)\,dv\,dz.
 \tag{2.13k}
\]
At \(X=hn,Y=h^{-t}e\), put \(v=hu,z=h^{-t}z'\).
The two Jacobians cancel. Since \(n_1=e_1\), the left side of (2.13j)
is integration of
\[
 \Psi\bigl(h[u,n_r,\ldots,n_2],h^{-t}z'\bigr)
       \psi\left(z'_1-u_r-\sum_{i<r}n_{i,i+1}\right)
 \tag{2.13l}
\]
over \(u,z',n\).

Expand (2.13g) on the right, and put \(A=hA',B=h^{-t}B'\).
Their Jacobian is \(\nu(h)^{r-1}\).
Orthogonality in each upper entry \(n_{ij}\) imposes
\[
 A'_{r+1-i,j}=\delta_{j,i+1}\qquad(i<j).
 \tag{2.13m}
\]
The remaining matrices are exactly
\(A'=[u,n_r',\ldots,n_2']\) for a unique \(u\in k^r,n'\in N_r\):
the prescribed entries are the reversed identity entries and their
zeros; the free entries are the first column and the strict upper
entries of \(n'\). This is an affine coordinate bijection with
Jacobian one. Its constant phase is precisely
\(\psi(B'_1-u_r-\sum n'_{i,i+1})\), proving (2.13l) and (2.13j).

This orthogonality calculation is an ordinary Schwartz Fourier
calculation. To avoid an implicit integral of a constant character on
a noncompact space, prove it first for a product of compact-open coset
indicators. Restrict all Fourier-coordinate integrations to a sufficiently
large compact lattice; character orthogonality imposes (2.13m) modulo
the annihilator lattice. The test is constant on that annihilator
lattice, so integration over the remaining cosets gives the asserted
affine measure exactly. The original Schwartz functions and their
transforms have compact support on both affine spaces; a sufficiently
large cutoff includes both. Finite linear combinations establish the
identity for every Schwartz test. This also proves (2.13j) in residue
characteristic two: signs may agree there, and the unit Jacobians remain one.

Now prove (2.13i) at \(g=e\). In the expression for
\(W_{\widehat\Psi,\widetilde V,\mu^{-1}}(\zeta)\), change
the \(G_r\) variable to \(h^{-t}w_r\). Its vector value becomes
\(V(h^{-1})\); its two test arguments become
\((-h^{-t}w_r,he_1)\).
The constant prefactor is
\(\mu^{-1}(\det\zeta)\mu^{-1}(\det w_r)\), equal to
\(\mu(\det w_{r+1})\), because
\[
 \det w_{r+1}\,\det w_r\,\det\zeta
       =(-1)^{r(r+1)/2+r(r-1)/2+r}=1.
 \tag{2.13n}
\]
Disintegrate the full \(G_r\) integral on the right by its right \(N_r\)
cosets. Since \(V((hn)^{-1})=\psi^{-1}(n)V(h^{-1})\), the remaining
test average is exactly the one in (2.13j); the change
\(n\mapsto w_rn^{-t}w_r\) changes its character to \(\psi(n)\).
The factor \(\nu(h)^{-(r-1)}\) in (2.13j) changes
\((r-1)/2\) to \(-(r-1)/2\), which is the transformed kernel power.
All original kernel integrations are over the compact sets proved
in Lemma 2.3y. This proves (2.13i) at identity.
For general \(g\), replace \(\Psi\) by \(\rho_0(g^{-t})\Psi\);
(2.13h) supplies \(\nu(g)^r\), which combines with the kernel prefactor
\(\mu^{-1}(\det g)\nu(g)^{-r/2}\) to give the correct
\(\mu^{-1}(\det g)\nu(g)^{r/2}\) on the right. This proves (2.13i).
\(\square\)

#### Decomposing each local integral into two actual families

Take a pure tensor
\(\Psi(x,y)=\Phi_1(x)\Phi_2(y)\), and write
\(\phi_2(v)=\Phi_2(v^t)\) for its row test.
Substitute (2.13d) into the adjacent direct integral
\[
 Z(s)=\int_{N_r\backslash G_r}
 W_{\Psi,V,\mu}(\operatorname{diag}(g,1))
                               W'(g)\nu(g)^{s-1/2}\,dg,
 \tag{2.13o}
\]
where \(W'\) is the \(\pi,\psi^{-1}\) vector.
Change the kernel variable from \(h\) to \(hg^{-1}\), and then the
quotient variable from \(g\) to \(gh\). The characters cancel and the
determinant powers give
\[
 Z(s)=\int_{N_r\backslash G_r}
 V(g)\phi_2(e_rg)\nu(g)^s
 \int_{G_r}\Phi_1(h)W'(gh)
            \mu(\det h)\nu(h)^{s+(r-1)/2}\,dh\,dg.
 \tag{2.13p}
\]

Every coefficient of this double integral is absolutely convergent.
Indeed \(\Phi_1(h)\) bounds all entries of \(h\) and hence \(\nu(h)\)
above. In Iwasawa representatives for \(g\), \(V\)'s ratio support
and \(\phi_2(e_rg)\)'s last-coordinate support bound every diagonal
entry of \(g\) above. Thus \(\nu(g)\) is bounded above.
On a fixed determinant shell \(\nu(gh)=q^{-m}\), these two upper
bounds give lower bounds for both determinants. The diagonal entries
of \(g\) are therefore bounded below as well, so \(g\) lies in a compact
set modulo \(N_r\); \(h\) lies in a compact subset of \(G_r\), using
its bounded entries, determinant lower bound, and the adjugate inverse
formula. The \(N_r\) phases in \(V(g)W'(gh)\) cancel.
Consequently all changes, compact averaging, and finite sums below are
valid coefficient by coefficient, without a hidden absolute-convergence
claim for a formal infinite series.

Choose an open compact \(J\subset G_r\) making \(\Phi_1\) left invariant,
with \(\mu(\det J)=1\); let \(e_J\) denote averaging with probability
Haar measure. Admissibility makes \(\pi^J\) finite-dimensional.
Choose a basis \(v_i\), and expand
\[
 e_J\pi(h)v'=\sum_i f_i(h)v_i,\qquad
 W_i'(g)=\lambda_\pi(\pi(g)v_i).
 \tag{2.13q}
\]
Each \(f_i\) is an actual smooth ordinary coefficient: its dual form is
the basis functional composed with \(e_J\).
Changing \(h\) by \(jh\) in (2.13p) and averaging gives
\[
 Z(s)=\sum_i
 Z(s,V,W_i',\phi_2)\,
 J(s,\Phi_1,f_i\otimes\mu),
 \tag{2.13r}
\]
where the first factor is the equal-rank Rankin–Selberg family and
\[
 J(s,\Phi_1,f_i\otimes\mu)
 =\int_{G_r}\Phi_1(h)f_i(h)\mu(\det h)
                         \nu(h)^{s+(r-1)/2}\,dh
 \tag{2.13s}
\]
is exactly the already proved standard matrix family. Its entire ideal
and scalar agree with the rank-one Rankin–Selberg family by the preceding rank-one ideal and Fourier comparisons,
also for the induced model scope of Lemma 2.3t.
There is no compact subgroup required to fix a nonzero column vector
pointwise; only Schwartz and character invariance of the stated functions
is used.

#### Functional equation and signs

By (2.13i) the reflected \(\sigma\) test at
\(\operatorname{diag}(g,1)\) is the kernel with
\(\mu^{-1},\widetilde V,\widehat\Phi_1,\widehat\Phi_2\), evaluated at
\(\operatorname{diag}(-g,1)\).
It contributes the scalar \(\mu(\det\zeta)\) and replaces its matrix
test by \(\widehat\Phi_1(-\,\cdot\,)\).
Use \(J'=J^{-t}\) in its analogue of (2.13q). The original averaged
identity, evaluated at \(w_rg^{-t},h^{-t}\), shows that its factors are
exactly
\(\widetilde W_i'(g)\) and \(f_i(h^{-t})\), respectively.
Fourier invariance gives left \(J^{-t}\)-invariance of
\(\widehat\Phi_1\), so this is the same permissible averaging.
Thus its product decomposition is
\[
 Z^\vee(1-s)=\mu(\det\zeta)\sum_i
 Z(1-s,\widetilde V,\widetilde W_i',\widehat\phi_2)\,
 \int_{G_r}\widehat\Phi_1(-h)f_i(h^{-t})
       \mu^{-1}(\det h)\nu(h)^{1-s+(r-1)/2}\,dh.
 \tag{2.13t}
\]

The equal-rank equation converts its first factor with scalar
\(\omega_\pi(-1)^{r-1}\gamma(s,\rho\times\pi,\psi)\).
For the second factor recall that matrix Fourier uses
\(\psi(\operatorname{tr}(XY))\). Therefore its matrix transform is
\(\Phi_1^\#(h)=\widehat\Phi_1(h^t)\), with the transpose essential.
The actual matrix equation followed by \(h\mapsto h^t\) gives
\[
 \int_{G_r}\widehat\Phi_1(h)f_i(h^{-t})
   \mu^{-1}(\det h)\nu(h)^{1-s+(r-1)/2}\,dh
 =\gamma(s,\pi\times\mu,\psi)\,J(s,\Phi_1,f_i\otimes\mu).
 \tag{2.13u}
\]
Replacing \(h\) by \(-h\) gives for the negative matrix test in (2.13t)
the additional factor \(\omega_\pi(-1)\mu(\det\zeta)\).
The two \(\mu(\det\zeta)\)'s cancel because their square is one.
The total remaining sign is consequently
\(\omega_\pi(-1)^r\), exactly the conversion from the raw adjacent
scalar to the normalized Rankin–Selberg gamma factor. We obtain
\[
 Z^\vee(1-s)=\omega_\pi(-1)^r
 \gamma(s,\rho\times\pi,\psi)\gamma(s,\pi\times\mu,\psi)\,Z(s).
 \tag{2.13v}
\]
All equal-rank and matrix equations can be cleared by their reciprocal
polynomials and Laurent-unit epsilon factors before applying them to
(2.13r)–(2.13t); every sum is finite and every shell has the proved compact
integration domain. Thus this is a formal coefficient identity as well
as a rational one.

#### The theorem and continuation of the whole family

**Theorem 2.3z.** For every rank \(r\ge1\) and the entire induction (2.13a),
\[
 \gamma(s,\sigma\times\pi,\psi)
  =\gamma(s,\rho\times\pi,\psi)\gamma(s,\pi\times\mu,\psi),
 \qquad
 \frac{L(s,\sigma\times\pi)}
 {L(s,\rho\times\pi)L(s,\pi\times\mu)}
                  \in\mathbf C[q^{-s}],\quad P(0)=1.
 \tag{2.13w}
\]

**Proof.** In the positive-twist chamber Lemma 2.3y spans every actual
Whittaker test of the induction. Equation (2.13v), compared to the scalar
equation 2.9ai with its only index zero, proves the gamma product.
Equation (2.13r) shows that the product of the two child reciprocal
polynomials clears every such entire-family integral.
Finite test-data attainment gives the indicated polynomial correction,
as in the proof of Theorem 2.3w.

For an arbitrary original \(\mu\), use Lemma 2.3r's compact-picture family
\(\mu\nu^u\). Clear (2.13v) with both child reciprocal polynomials and
epsilon Laurent units. Each coefficient is a Laurent polynomial in
\(z=q^u\); the block matrix factor uses the norm shift \(s+u\), while
the equal-rank block is fixed. It vanishes for every sufficiently
positive real \(z\), hence identically. The direct and reflected series
have uniform lower and upper exponent bounds, respectively, by Lemma 2.3r.
The degrees of the child polynomials and epsilon monomials are fixed
under these substitutions. The cleared identity therefore also proves
polynomial clearing at every specialization, not merely an equality of
meromorphic scalar functions. A nonzero test and the whole-family ideal
then prove both assertions of (2.13w). \(\square\)

### Full finite parabolic multiplicativity and its polynomial correction

Write \(\mathscr R=\mathbf C[X,X^{-1}]\), \(X=q^{-s}\).
All pair notation uses the actual larger-rank integral of the preceding finite-place integral theory;
the two labels of a pair may therefore be exchanged. At equal rank this
is also the same normalized scalar, as verified in (2.14m) and its subsequent equal-rank symmetry calculation.
The representations considered are actual generic irreducible admissible
representations or their full faithful induced Whittaker models proved
in Lemma 2.3t. No existence or classification of an unspecified Langlands
decomposition is assumed.

#### An actual opposite ideal insertion

**Lemma 2.3aa.** Let \(\tau\) have rank \(N\), let \(\pi\) have rank \(r<N\),
let \(\eta\) be any smooth character, and put
\[
 I=\operatorname{Ind}_{Q^-}^{G_{r+1}}(\pi\otimes\eta).
 \tag{2.14a}
\]
Then
\[
 I(\tau\times\pi)\subset I(\tau\times I)
 \tag{2.14b}
\]
as actual full fractional ideals. Each old pure integral is an actual new
integral constructed below, after a specified nonzero scalar normalization.
The equality case \(N=r+1\) uses the new equal-rank Schwartz test.

**Proof.** The larger Whittaker function \(W_0\) uses \(\psi\), and the
smaller model uses \(\psi^{-1}\).
For any old smaller Whittaker vector \(V\), choose a lower-parabolic
section supported in the open upper-unipotent chart by
\[
 f\left[
 \begin{pmatrix}m&0\\ x&a\end{pmatrix}
 \begin{pmatrix}I_r&y\\0&1\end{pmatrix};\,h\right]
 =\nu(m)^{-1/2}|a|^{r/2}\eta(a)\,V(hm)\,\phi(y).
 \tag{2.14c}
\]
Here \(\phi\) is any compactly supported locally constant function on
\(k^r\), later chosen with sufficiently small support. Extending by zero
outside the open chart gives an actual smooth induced section: its chart
support is compact inside the open flag cell, and its values use the
specified vector and its normalized section law.

We fix the normalizations of its open-chart Haar measure explicitly.
For conductor-zero \(\psi\), additive \(\mathcal O\)-volume is one.
Let
\[
 \alpha_j=\prod_{i=1}^j(1-q^{-i}),\qquad
 c_r=\frac{\alpha_r(1-q^{-1})}{\alpha_{r+1}}>0.
 \tag{2.14d}
\]
The matrix chart
\[
 g=\begin{pmatrix}m&my\\x&a+xy\end{pmatrix}
 \tag{2.14e}
\]
has additive Jacobian \(\nu(m)\) and determinant \(\det(m)a\).
Since \(dg=\alpha_{r+1}^{-1}|\det g|^{-(r+1)}d_{\rm add}g\),
\(d_{\rm add}m=\alpha_r\nu(m)^r\,dm\), and
\(d_{\rm add}a=(1-q^{-1})|a|\,d^\times a\),
the Haar measure of (2.14e) is
\[
 dg=c_r|a|^{-r}\,dm\,dx\,d^\times a\,dy.
 \tag{2.14f}
\]
Dividing its \(m\)-variable by \(N_r\)'s self-dual measure gives the
same formula with \(N_r\backslash G_r\). For another additive character,
the identical calculation uses that character's additive volumes, gives
its positive chart constant, and is normalized in exactly the same way;
alternatively Proposition 2.3i transfers the ideal statement by character scaling.

First suppose \(N\ge r+2\). The old full ideal may be computed with its
index-one family by Corollary 2.3f. An old pure test is
\[
 Z_1(s,W_0,V)=
 \int_{N_r\backslash G_r}\int_{k^r}
 W_0\left[
 \begin{pmatrix}m&0&0\\x&1&0\\0&0&I_{N-r-1}\end{pmatrix}\right]
                 V(m)\nu(m)^{s-(N-r)/2}\,dx\,dm.
 \tag{2.14g}
\]
Choose a compact open group \(J\) fixing \(W_0\), and choose a small
unit neighbourhood \(S=1+\mathfrak p^\ell\) such that
\(\operatorname{diag}(I_r,a,I)\in J\) and \(\eta(a)=1\) for \(a\in S\).
Set \(b(a)=1_S(a)/\operatorname{vol}_\times(S)\), regarded also as a
Schwartz function on the additive field. Define an actual Whittaker
vector by Fourier averaging the upper simple root:
\[
 W(g)=\int_k\left(\int_k b(a)\psi(-au)\,da\right)
                W_0(g(1+uE_{r+1,r+2}))\,du.
 \tag{2.14h}
\]
The weight is Schwartz and hence supported on a compact set; averaging
is a finite linear combination on the smooth representation.
For the matrix
\[
 q(m,x,a)=
 \begin{pmatrix}m&0&0\\x&a&0\\0&0&I_{N-r-1}\end{pmatrix}
 \tag{2.14i}
\]
right multiplication by that root equals left multiplication by
\(1+auE_{r+1,r+2}\). Self-dual Fourier inversion therefore gives
\[
 W(q(m,x,a))=b(a)W_0(q(m,x,a)).
 \tag{2.14j}
\]
On \(S\) the second factor equals the same value with \(a=1\), by its
right \(J\)-invariance. There is no determinant-dependent frequency
or an unstated root sign in this cutoff.

Choose the support of \(\phi\) in (2.14c) inside the right stabilizer of
the **new** \(W\), and normalize \(\int\phi(y)\,dy=c_r^{-1}\).
Unfold its upper Jacquet integral in the new index-zero family
\((\tau,I)\). The Jacquet phase cancels the larger Whittaker character.
Use (2.14f) and the small upper-chart support to remove \(y\).
The resulting determinant powers are exactly
\[
 \nu(m)^{s-(N-r-1)/2-1/2}
       =\nu(m)^{s-(N-r)/2},\qquad
 |a|^{s-(N-r-1)/2+r/2-r}
       =|a|^{s-(N-1)/2}.
 \tag{2.14k}
\]
Equations (2.14j) and the choice of \(S\) make the \(a\)-integral one.
Thus the new integral equals (2.14g) exactly.

Now suppose \(N=r+1\). The old family has index zero. Use \(W=W_0\).
Choose a small compact open additive lattice \(L\subset k^r\) such
that the lower matrices
\(\left(\begin{smallmatrix}I&0\\x&1\end{smallmatrix}\right)\)
lie in its right stabilizer for \(x\in L\). Choose \(S\) as above and
put \(\chi=1_L/\operatorname{vol}_{\rm add}(L)\).
Use the new equal-rank row test
\[
 \Phi_{\rm new}(x,a)=\chi(x)b(a).
 \tag{2.14l}
\]
Choose the upper-chart support of \(\phi(y)\) small enough to stabilize
\(W_0\) and to make \(xy\in\mathfrak p^\ell\) for every \(x\in L\).
Then (2.14l) is unchanged under \((x,a)\mapsto(x,a+xy)\).
On its support the Whittaker value in (2.14i) is
\(W_0(\operatorname{diag}(m,1))\).
Unfold as before; the \(x\)- and \(a\)-integrals are both one.
The \(m\)-power in (2.14k) is now \(s-1/2\), the required old adjacent
power, and the new integral equals that old test exactly.

For complete justification of unfolding, first replace \(\eta\) by
\(\eta\nu^u\) with \(u\) sufficiently positive. Lemma 2.3v gives its
actual absolutely convergent upper Jacquet integral and identifies it
with the Whittaker model. The coupled unfolded integral is absolutely
convergent for sufficiently right \(s\): \(y\) is compact, \(a\) lies
in \(S\), and (2.14j), respectively (2.14l), leaves exactly the old
absolutely convergent integral. Its old rectangle is uniformly compact
by (2.9l)–(2.9m). Thus Fubini proves the exact equalities just derived.

Finally remove \(u\). The section (2.14c), its compact chart support and
its restriction to \(K_{r+1}\) define a Laurent-polynomial compact-picture
family; on the small open chart in \(K_{r+1}\) all the relevant \(a\)'s
are units, so its restriction is in fact independent of \(u\).
The scalar cutoffs above use only \(a\in S\) and are also independent
of \(u\). Lemma 2.3r proves that every new determinant-shell coefficient is
Laurent polynomial in \(q^u\). The old coefficient is constant.
Their equality for all sufficiently positive real \(u\) proves equality
of each coefficient identically, hence at the original \(\eta\).
This proves (2.14b) with actual tests. \(\square\)

#### Equal-rank symmetry and cancellation convention

At equal rank \(r\), interchanging the two representations and using
base character \(\psi^{-1}\) preserves the direct integral. Its reflected
Schwartz transform changes from \(\widehat\Phi_\psi\) to
\(\widehat\Phi_{\psi^{-1}}(x)=\widehat\Phi_\psi(-x)\).
Changing \(g\mapsto-g\) in that reflected integral gives
\(\omega_\pi(-1)\omega_\rho(-1)\).
Conversion of the two raw scalars and the character-scaling law Proposition 2.3i
then give
\[
 \gamma(s,\pi\times\rho,\psi)=\gamma(s,\rho\times\pi,\psi).
 \tag{2.14m}
\]
For detail, the comparison before changing the base character back is
\(\gamma(s,\rho\times\pi,\psi^{-1})
 =\omega_\pi(-1)^r\omega_\rho(-1)^r
       \gamma(s,\pi\times\rho,\psi)\).
Proposition 2.3i contributes exactly the same central factor, whose square is one.
The ideals are similarly unchanged, and normalization gives equality
of \(L\)-factors. For unequal ranks the notation in this fragment always
uses the canonical larger-rank family; exchanging the labels introduces
no independently chosen incompatible normalization.

The rank-one polynomial correction used below also needs its actual
scope spelled out. The whole ordinary matrix ideal of an induction
has the product generator, by the preceding matrix theorem. Each
coefficient of its faithful Whittaker quotient is a coefficient of
the induction: lift its vector and compose its dual form with the
quotient. Thus that quotient's matrix ideal is **contained** in the
product matrix ideal. Lemma 2.3t identifies its own matrix ideal with its
own entire rank-one Rankin–Selberg ideal. Finite test-data attainment
therefore gives the rank-one **polynomial correction**, not unconditional
equality of these two matrix ideals.
In particular this proof does not confuse a reducible full induction
with its possibly irreducible Whittaker quotient.

#### All fixed ranks when the last lower inducing block is a character

**Lemma 2.3ab.** For every rank of the fixed representation \(\pi\), and
every \(t\ge2\), let
\(\sigma=\operatorname{Ind}_{Q^-}(\rho_{t-1}\otimes\mu)\).
Then
\[
 \gamma(\pi\times\sigma)=\gamma(\pi\times\rho)\gamma(\pi\times\mu),
 \qquad
 \frac{L(\pi\times\sigma)}
 {L(\pi\times\rho)L(\pi\times\mu)}\in\mathbf C[X],\quad P(0)=1.
 \tag{2.14n}
\]
All gamma arguments are the same \(s,\psi\).

**Proof for gamma.** Fixed rank at least \(t\) is Theorem 2.3x, rank \(t-1\)
is Theorem 2.3z, and rank one is the rank-one comparison and inducing-family extension. Fix \(t\) and descend in the
remaining fixed rank \(r\le t-2\). Put
\(I=\operatorname{Ind}_{Q^-}(\pi_r\otimes\eta)\).
The induction hypothesis gives
\(\gamma(\sigma\times I)=\gamma(\rho\times I)\gamma(I\times\mu)\).
Theorem 2.3x applies to both \(\sigma\times I\) and \(\rho\times I\), because
\(t\ge r+1\) and \(t-1\ge r+1\). Rank-one multiplicativity applies
to \(I\times\mu\) and \(\sigma\times\eta\).
After substitution, the identity is
\[
 \gamma(\sigma\times\pi)\gamma(\sigma\times\eta)
 =\gamma(\rho\times\pi)\gamma(\rho\times\eta)
                       \gamma(\pi\times\mu)\gamma(\eta\times\mu).
 \tag{2.14o}
\]
But \(\gamma(\sigma\times\eta)
 =\gamma(\rho\times\eta)\gamma(\mu\times\eta)\);
all these rational scalars are nonzero. Cancel them to get (2.14n).
The auxiliary character may be arbitrary in this scalar argument.

**Proof for the polynomial correction.** Choose \(\eta\) sufficiently
ramified that Proposition 2.3u gives
\(L(\sigma\times\eta)=L(\rho\times\eta)=L(\mu\times\eta)=1\).
Theorem 2.3x supplies polynomials of constant term one with
\[
 L(\sigma\times I)=L(\sigma\times\pi)P_3,\qquad
 L(\rho\times I)=L(\rho\times\pi)P_2.
 \tag{2.14p}
\]
Lemma 2.3aa supplies the opposite inclusion of the \(\sigma\)-ideals, so
\(L(\sigma\times\pi)\in L(\sigma\times I)\mathscr R\).
The first identity in (2.14p) thus makes \(P_3^{-1}\) a Laurent polynomial.
A polynomial with constant term one whose inverse is Laurent polynomial
is one: it is a Laurent unit, hence a monomial, and its constant term
forces degree zero. Consequently \(P_3=1\).

For the rank-one pair \(I\times\mu\), the rank-one polynomial correction
just proved and \(L(\eta\times\mu)=1\) give
\(L(I\times\mu)=L(\pi\times\mu)P_4\), with \(P_4\in\mathbf C[X]\)
and \(P_4(0)=1\).
The descending induction hypothesis for \(\sigma\times I\), together
with (2.14p), now gives (2.14n), with its correction the product of the
induction polynomial, \(P_2\), and \(P_4\). All constant terms are one.
This proves the lemma. \(\square\)

#### Arbitrary binary and multiple parabolic data

**Theorem 2.3ac.** Let
\(\sigma=\operatorname{Ind}_{Q^-}(\sigma_a\otimes\sigma_b)\), with
both blocks of the indicated actual generic admissible scope.
For every fixed rank and every nonarchimedean local field,
\[
 \gamma(s,\pi\times\sigma,\psi)=
       \gamma(s,\pi\times\sigma_a,\psi)
       \gamma(s,\pi\times\sigma_b,\psi),
 \qquad
 \frac{L(s,\pi\times\sigma)}
 {L(s,\pi\times\sigma_a)L(s,\pi\times\sigma_b)}
                  \in\mathbf C[q^{-s}],\quad P(0)=1.
 \tag{2.14q}
\]
For several blocks the gamma is their product and the \(L\)-factor
has the same product times a polynomial of constant term one.

**Proof.** Fixed rank \(r\ge t=a+b\) is Theorem 2.3x and fixed rank one is Lemma 2.3t.
Descend in \(r<t\), putting again
\(I=\operatorname{Ind}_{Q^-}(\pi_r\otimes\eta)\).
The induction hypothesis gives
\(\gamma(\sigma\times I)
 =\gamma(\sigma_a\times I)\gamma(\sigma_b\times I)\).
Lemma 2.3ab, applied to the character-last induction \(I\), expands
each of these three scalars in its two blocks \(\pi,\eta\), regardless
of the three fixed ranks. Rank-one multiplicativity gives
\(\gamma(\sigma\times\eta)
 =\gamma(\sigma_a\times\eta)\gamma(\sigma_b\times\eta)\).
Cancel these nonzero factors. This gives the scalar part of (2.14q).

For \(L\), choose \(\eta\) sufficiently ramified for
\(\sigma,\sigma_a,\sigma_b\), using Proposition 2.3u.
The induction hypothesis and Lemma 2.3ab give polynomials of constant term one:
\[
 \begin{split}
 L(\sigma\times I)
   &=L(\sigma_a\times I)L(\sigma_b\times I)P,\\
 L(\sigma_i\times I)&=L(\sigma_i\times\pi)P_i,\\
 L(\sigma\times I)&=L(\sigma\times\pi)P_3 .
 \end{split}
 \tag{2.14r}
\]
Lemma 2.3aa applies because \(r<t\); it includes the equality \(r+1=t\).
It forces \(P_3=1\) by the same reciprocal-unit argument as in Lemma 2.3ab.
The first two identities in (2.14r) prove (2.14q) with correction
\(PP_aP_b\), of constant term one.

For multiple blocks, use actual transitivity of normalized induction,
proved by the two inverse maps (1.27v)–(1.27w): the section laws on the two successive flag quotients
multiply to the refined modulus, and the compact-level inverse gives
the actual isomorphism. Group the last block and repeat the binary
statement. No assertion reordering arbitrary inducing blocks is needed
by this induction. This proves the theorem. \(\square\)

#### Actual generic irreducible subquotients

**Corollary 2.3ad.** Suppose an actual generic irreducible \(\tau\) is a specified subquotient
\(U/V\) of one of these inductions. Its gamma is the same block product,
and its \(L\)-factor divided by the block product is a polynomial of
constant term one.

Here is the proof, without assuming finite length or a classification.
Twisted \(N\)-coinvariants are exact by the compact Fourier averaging
proof in the mirabolic spectral filtration above. The full induction has generic coinvariant dimension one
by Lemma 2.3o, and \(\tau\) has dimension one by the actual Whittaker uniqueness
provider. The two exact sequences imply
\(\dim U_{N,\psi}=1\) and \(V_{N,\psi}=0\).
Thus the full induction's functional restricts nontrivially to \(U\)
and descends to \(U/V\). Its functions give a well-defined actual
inclusion of the \(\tau\) Whittaker model in the induced function model:
changing a lift by a vector of \(V\) gives zero under every translate.
The full scalar equation restricts to this model; its reflected
functions are the same actual inverse-transpose functions.
Theorem 2.3h's uniqueness and a nonzero test therefore give the same gamma.

The inclusion of actual test families gives \(I(\tau\times\pi)
\subset I(\operatorname{Ind}\times\pi)\).
Writing their normalized generators as \(1/P_\tau,1/P_I\), finite
test-data attainment gives \(P_\tau\mid P_I\) in \(\mathbf C[X]\);
the quotient has constant term one. Hence
\(L(\tau\times\pi)=L(\operatorname{Ind}\times\pi)(P_I/P_\tau)\).
Combine with Theorem 2.3ac to get the claimed polynomial correction.
This is an assertion about the supplied actual subquotient, not the
existence or ordering of an unspecified decomposition.

### The spherical value generates the whole local ideal

**Theorem 2.3ae.** Let \(\pi,\sigma\) be actual irreducible unramified
generic representations of \(GL_n(k),GL_m(k)\), with Satake tuples
\(\alpha=(\alpha_i)\), \(\beta=(\beta_j)\). With conductor-zero additive
character and the measure normalization preceding (2.9a),
\[
 L(s,\pi\times\sigma)=
 \prod_{i=1}^n\prod_{j=1}^m(1-\alpha_i\beta_jq^{-s})^{-1}.
 \tag{2.15a}
\]
The spherical tests in the preceding Proposition 2.1c attain the
normalized generator of the **whole** family. This includes repeated
Satake eigenvalues and every residue characteristic.

**Proof.** The actual proof of
*The Satake isomorphism for unramified groups and unramified L-factors*, Proposition 5.1 and Corollary 5.2
supplies \(\pi\) as an actual
subquotient of normalized induction of the unramified characters
\(\chi_i\), with \(\chi_i(\varpi)=\alpha_i\); it also supplies the
analogous \(\eta_j(\varpi)=\beta_j\) data for \(\sigma\).
It does not assume those principal series are irreducible.
The hypotheses here supply the actual nonzero generic functionals.
The complete spherical Whittaker proof in the preceding
Proposition 2.1a shows evaluation at the spherical vector is injective
on those functionals, so each may be normalized to have \(W(1)=1\).

Apply Theorem 2.3ac and Corollary 2.3ad to the supplied subquotients and then to all their
rank-one inducing blocks. The full local factor has the form
\[
 L(s,\pi\times\sigma)=D(X)P(X),\qquad P\in\mathbf C[X],\quad P(0)=1,
 \quad
 D(X)=\prod_{i,j}(1-\alpha_i\beta_jX)^{-1}.
 \tag{2.15b}
\]
The rank-one factors are the actually proved unramified Tate factors.
No direct equality of inducing and constituent factors was assumed.

The actual proofs of Lemma 2.1b and Proposition 2.1c give a pure
spherical test with integral exactly \(D(X)\), using
\(1_{\mathcal O^n}\) in equal rank and index zero in unequal rank.
Since every actual test belongs to the full fractional ideal
\(L(s,\pi\times\sigma)\mathbf C[X,X^{-1}]\), (2.15b) implies
\(P(X)^{-1}\in\mathbf C[X,X^{-1}]\).
Its constant term one makes a polynomial Laurent unit equal to one.
Hence \(P=1\), proving (2.15a) and actual generator attainment.
\(\square\)

For a different additive character, Proposition 2.3i proves that the entire normalized
ideal is unchanged. Thus the factor (2.15a) is independent of that choice;
the corresponding changed-character spherical tests are obtained by
the explicitly proved diagonal scaling and measure factors in Proposition 2.3i.

## 3. Global continuation, poles and nonvanishing

**Theorem 3.1 (Jacquet–Piatetski-Shapiro–Shalika, 1979/1983; global Rankin–Selberg analytic theory; proof not yet supplied).** For unitary cuspidal \(\pi\) on \(GL_n(\mathbb A)\) and \(\pi'\) on \(GL_m(\mathbb A)\), the complete product (2.1) has meromorphic continuation and satisfies

\[
\mathcal L(s,\pi\times\pi')
=\varepsilon(\pi\times\pi')A(\pi\times\pi')^{1/2-s}
\mathcal L(1-s,\widetilde\pi\times\widetilde{\pi'}),
\tag{3.1}
\]

where \(A(\pi\times\pi')=|D_F|^{nm}N\mathfrak f(\pi\times\pi')\) and \(|\varepsilon(\pi\times\pi')|=1\). It is entire unless \(n=m\) and

\[
\pi'\simeq\widetilde\pi\otimes\nu^{it}
\quad\text{for some }t\in\mathbb R.
\tag{3.2}
\]

In the exceptional case its only poles are simple poles at \(-it\) and \(1-it\). In particular, at the real point one it has a simple pole exactly when \(\pi'\simeq\widetilde\pi\). The split-central normalized assertion is [Getz–Hahn, 22 April 2022 draft, Theorem 11.7.1], due to Jacquet, Piatetski-Shapiro and Shalika; the twist rule below gives the unrestricted unitary form. This global integral theorem is stated with all its hypotheses. Its general-rank construction and proof are not given here.

To see the twist rule and pole locations, replace \(\pi,\pi'\) by \(\pi\otimes\nu^u,\pi'\otimes\nu^{u'}\). At an unramified place, their eigenvalues acquire factors \(q_v^{-u},q_v^{-u'}\), so

\[
L_v(s,(\pi_v\otimes\nu_v^u)\times(\pi'_v\otimes\nu_v^{u'}))
=L_v(s+u+u',\pi_v\times\pi'_v).
\tag{3.3}
\]

The local integral theory gives the same identity at the remaining places. Consequently it holds for the complete and partial products by continuation. Normalize the actions of the positive split center by imaginary norm twists, apply the zero-and-one pole statement of Theorem 11.7.1, and undo those twists using (3.3). In case (3.2), the complete function is \(\mathcal L(s+it,\pi\times\widetilde\pi)\), so its poles are exactly as stated. A nonzero imaginary norm twist cannot stabilize a cuspidal representation: its central character would acquire \(|\cdot|^{int}\), which is nontrivial on the positive real split center when \(t\ne0\). This also explains why only the untwisted dual gives a pole at the real point one.

The standard factor is the rank-one pairing \(L_v(s,\pi_v\times1)\). For \(n\ge2\), Theorem 3.1 supplies another route to its entire continuation. The Godement–Jacquet and Rankin–Selberg constructions agree on these factors; they are not two different standard L-functions.

## 4. Positivity, the strict bound and boundary nonvanishing

The complete pole theorem and the shape of the local factors suffice for the deductions in this section. We do not assume a local boundary convergence theorem or global boundary nonvanishing. The essential extra fact is a lower bound for certain coefficients of a positive self-pairing series.

### 4.1. A positive series cannot hide its first real singularity

**Lemma 4.1 (Landau's positivity principle).** Let \(a_r\ge0\), and suppose \(\sum_{r\ge1}a_rr^{-s}\) has a finite real abscissa of convergence \(c\). Its sum cannot be holomorphic in a neighborhood of the real point \(c\).

**Proof.** Suppose it is holomorphic there. Choose \(\epsilon>0\) so small that the disk of radius \(3\epsilon\) about \(c\) lies in the continuation neighborhood. Put \(b=c+\epsilon\). Termwise differentiation at \(b\) is valid, since for each \(j\), \((\log r)^j r^{-b}\) is bounded by a constant times \(r^{-(c+\epsilon/2)}\). The Taylor expansion on the disk of radius \(2\epsilon\) about \(b\) is

\[
f(b-z)=\sum_{j\ge0}\frac{z^j}{j!}
\sum_{r\ge1}a_r(\log r)^j r^{-b}.
\tag{4.1}
\]

Choose a real \(z\) with \(\epsilon<z<2\epsilon\). Every summand is nonnegative, so monotone convergence allows the order of summation to be reversed. The finite Taylor sum becomes

\[
\sum_r a_r r^{-b}\sum_{j\ge0}\frac{(z\log r)^j}{j!}
=\sum_r a_r r^{-(b-z)}<\infty.
\]

Since \(b-z<c\), this contradicts the definition of the abscissa. ∎

For an ideal Dirichlet series, group the ideals by their integral norm and apply this lemma. There are finitely many ideals of any fixed norm, by the ideal-lattice construction in *Idèles and the idèle class group*.

### 4.2. The determinant supplies coefficients that cannot disappear

For \(N\) variables \(x=(x_1,\ldots,x_N)\), put

\[
\Delta(x)=\det(x_i^{j-1})_{1\le i,j\le N}.
\]

If \(\lambda=(\lambda_1\ge\cdots\ge\lambda_N\ge0)\) is a partition, define

\[
s_\lambda(x)=
\frac{\det(x_i^{\lambda_{N-j+1}+j-1})_{i,j}}{\Delta(x)}.
\tag{4.2}
\]

The numerator is alternating. It vanishes when any two variables agree, and therefore is divisible by every \(x_j-x_i\). These distinct linear factors are relatively prime, so their product \(\Delta(x)\) divides it. Thus \(s_\lambda\) is a polynomial, including when the variables coincide. Its degree is \(|\lambda|=\sum_j\lambda_j\).

**Lemma 4.2 (Cauchy's identity and the determinant coefficient).** As a formal power series in \(z\),

\[
\prod_{i,j=1}^N(1-zx_i y_j)^{-1}
=\sum_\lambda s_\lambda(x)s_\lambda(y)z^{|\lambda|}.
\tag{4.3}
\]

Consequently, for nonzero complex \(x_i\), all coefficients of \(\prod_{i,j}(1-zx_i\overline{x_j})^{-1}\) are nonnegative. If \(|\prod_i x_i|=1\), the coefficient of \(z^{Nr}\) is at least one for every integer \(r\ge0\).

**Proof.** First assume the variables are distinct. The Cauchy determinant formula is

\[
\det\left(\frac1{1-zx_i y_j}\right)
=\frac{z^{N(N-1)/2}\Delta(x)\Delta(y)}
{\prod_{i,j}(1-zx_i y_j)}.
\tag{4.4}
\]

Here is a direct verification. After multiplication by the common denominator, the left numerator is alternating separately in the \(x\)'s and \(y\)'s and has degree at most \(N-1\) in each variable. It is therefore \(\Delta(x)\Delta(y)\) times a quantity depending only on \(z\). Every monomial has the same degree in the \(x\)'s, in the \(y\)'s and in \(z\), so this quantity is a constant times \(z^{N(N-1)/2}\). Expanding the entries geometrically, the first nonzero determinant term uses the distinct exponents \(0,1,\ldots,N-1\); its coefficient is \(\Delta(x)\Delta(y)\). The constant is one, proving (4.4).

Expand the same determinant by multilinearity. Terms with two equal exponents cancel. Grouping the others by \(0\le k_1<\cdots<k_N\) gives

\[
\det\left(\sum_{k\ge0}z^kx_i^ky_j^k\right)
=\sum_{k_1<\cdots<k_N}
z^{\sum k_j}\det(x_i^{k_j})\det(y_i^{k_j}).
\]

Only finitely many choices occur in each coefficient, so this calculation is valid formally. Write \(k_j=\lambda_{N-j+1}+j-1\), divide by \(z^{N(N-1)/2}\Delta(x)\Delta(y)\), and use (4.2). This gives (4.3). Clearing denominators shows that it holds without the distinctness assumption.

Set \(y=\overline x\). The polynomials in (4.2) have real coefficients, and each term is \(|s_\lambda(x)|^2z^{|\lambda|}\). For \(\lambda=(r,\ldots,r)\), factoring \(x_i^r\) from row \(i\) gives \(s_\lambda(x)=(\prod_i x_i)^r\). This single summand has coefficient one when \(|\prod_i x_i|=1\); all the others are nonnegative. ∎

Let \(x_v\) be the union of the Satake eigenvalues of any finite list of unitary cuspidal representations, with total rank \(N\). The list need not have an automorphic isobaric sum for this calculation. Unitarity and Proposition 2.3 identify the dual multiset with \(\overline{x_v}\), and the determinant has modulus one because each central character is unitary. Expanding the good-place self-pairing product gives coefficients \(a_{\mathfrak a}\ge0\), with

\[
a_{\mathfrak b^N}\ge1
\quad\text{for every integral ideal }\mathfrak b\text{ prime to }S.
\tag{4.5}
\]

Indeed, if \(\mathfrak b=\prod_v\mathfrak p_v^{r_v}\), the relevant coefficient is the product of the coefficients of \(z^{Nr_v}\) at those places.

The series therefore has abscissa at least \(1/N\): at \(s=1/N\) it majorizes \(\sum_{(\mathfrak b,S)=1}(N\mathfrak b)^{-1}\), which diverges. To justify this last assertion, the positive residue at one of \(\zeta_F\) is proved in *Hecke L-functions and the Dedekind zeta function*, Theorem 10.2 and Corollary 10.4. Deleting finitely many Euler factors multiplies it by factors \(1-q_v^{-s}\), nonzero at one. If its nonnegative ideal series converged at one, monotone convergence as real \(s\downarrow1\) would bound its value, contradicting that pole.

### 4.3. Initial convergence does not require the strict bound

**Lemma 4.3.** For fixed rank \(n\), there is a constant \(C_n\) such that every unitary unramified representation of \(GL_n(F_v)\) has \(|\alpha_{i,v}|\le q_v^{C_n}\). Thus the good-place products for any fixed pair, and for any finite list of pairs, converge absolutely in a sufficiently far right half-plane.

**Proof.** Normalize \(\operatorname{vol}(K_v)=1\). Let \(T_j\) be the characteristic function of
\(K_v\operatorname{diag}(\varpi_v I_j,I_{n-j})K_v\). The lattice description of its right cosets identifies them with subspaces of \(k_v^n\) of a fixed dimension. Choosing spanning vectors overcounts them, so there are at most \(q_v^{n^2}\). On a unitary representation,

\[
\|\pi_v(T_j)\|\le\int|T_j(g)|\,dg\le q_v^{n^2}.
\]

The normalized Satake calculation in *The Satake isomorphism for unramified groups and unramified L-factors* identifies its eigenvalue on the spherical line as \(q_v^{j(n-j)/2}e_j(\alpha_v)\). Hence \(|e_j(\alpha_v)|\le q_v^{n^2}\). Each \(\alpha_i\) is a root of the monic polynomial with coefficients \((-1)^je_j\). If \(|z|>1+M\), where \(M\) bounds those coefficients, then
\(M\sum_{j=1}^n|z|^{n-j}<|z|^n\), so such a \(z\) cannot be a root. We may take \(C_n=n^2+1\), because \(1+q_v^{n^2}\le q_v^{n^2+1}\).

For a pair of ranks \(n,m\), its tensor eigenvalues are bounded by \(q_v^{C_n+C_m}\). The geometric logarithmic expansion is consequently absolutely summable over \(v\) for \(\operatorname{Re}s>C_n+C_m+1\). Explicitly its absolute value is bounded by a rank-dependent constant times \(q_v^{-(\operatorname{Re}s-C_n-C_m)}\). For \(a>1\), \(\sum_vq_v^{-a}<\infty\): over a rational prime there are at most \([F:\mathbb Q]\) prime ideals and each has norm at least that prime. This proves the assertion. ∎

The coarse bound in this lemma is only a starting estimate. The strict exponent \(1/2\) will follow from the pole theorem and (4.5).

### 4.4. Absolute convergence to the right of one

**Proposition 4.4.** For unitary cuspidal \(\pi,\pi'\), the partial Rankin–Selberg Euler product converges absolutely and locally uniformly, and is nonzero, on \(\operatorname{Re}s>1\).

**Proof.** First take \(\pi'=\widetilde\pi\). Lemma 4.3 supplies an initial convergent Dirichlet series with nonnegative coefficients, by Lemma 4.2. Its abscissa \(c\) is finite and at least \(1/n\), by (4.5). The identity

\[
L^S(s,\pi\times\widetilde\pi)
=\mathcal L(s,\pi\times\widetilde\pi)
\prod_{v\in S}L_v(s,\pi_v\times\widetilde\pi_v)^{-1}
\tag{4.6}
\]

continues it meromorphically. The reciprocals are entire by Lemma 2.2, and Theorem 3.1 permits no pole with real part greater than one. If \(c>1\), Lemma 4.1 contradicts holomorphy at \(c\). Thus \(c\le1\).

Fix a real \(\sigma>1\). For one included place, its nonnegative local series is bounded term by term by the convergent global series, so it converges at \(\sigma\). Its radius of convergence is
\(R_v^{-2}\), where \(R_v=\max_i|\alpha_{i,v}|\): the rational function (2.4) has a denominator zero at the positive real point \(z=R_v^{-2}\), and none nearer the origin. It has numerator one, so no pole cancels. Convergence for every \(\sigma>1\) implies

\[
R_v^2\le q_v.
\tag{4.7}
\]

This weak inequality holds at every unramified place: choose \(S\) containing all the other exceptions but not the place under consideration. It makes the local logarithmic expansion valid on \(\operatorname{Re}s>1\). Put \(p_k(\alpha_v)=\sum_i\alpha_{i,v}^k\). Then

\[
\log L_v(s,\pi_v\times\widetilde\pi_v)
=\sum_{k\ge1}\frac{|p_k(\alpha_v)|^2}{k}q_v^{-ks}.
\tag{4.8}
\]

For real \(\sigma>1\), finite Euler products increase to the sum of the convergent nonnegative ideal series: every ideal occurs once its prime factors are included. Taking logarithms yields

\[
\sum_{v\notin S}\sum_{k\ge1}
\frac{|p_k(\alpha_v)|^2}{k}q_v^{-k\sigma}<\infty.
\tag{4.9}
\]

Apply the same argument to \(\pi'\), with eigenvalues \(\beta_v\). Cauchy–Schwarz on the indices \((v,k)\), with weight \(q_v^{-k\sigma}/k\), gives

\[
\sum_{v,k}\frac{|p_k(\alpha_v)p_k(\beta_v)|}{k}q_v^{-k\sigma}
\le
\left(\sum_{v,k}\frac{|p_k(\alpha_v)|^2}{k}q_v^{-k\sigma}\right)^{1/2}
\left(\sum_{v,k}\frac{|p_k(\beta_v)|^2}{k}q_v^{-k\sigma}\right)^{1/2}<\infty.
\tag{4.10}
\]

By (4.7) for both representations, each tensor eigenvalue has modulus at most \(q_v\); its logarithmic expansion is valid for \(\operatorname{Re}s>1\). Equation (4.10) proves absolute convergence of the sum of these logarithms. The estimate at the minimum real part of a compact subset proves uniform convergence there. Exponentiation gives a holomorphic nonzero product, agreeing with the initial one by continuation.

The associated ideal Dirichlet series converges absolutely as well. Pad the shorter eigenvalue list by zeros and use (4.3); padding adds factors equal to one. For any ideal \(\mathfrak a=\prod_v\mathfrak p_v^{r_v}\), its mixed coefficient is a finite sum of products of \(s_{\lambda_v}(\alpha_v)s_{\lambda_v}(\beta_v)\), over \(|\lambda_v|=r_v\). Cauchy–Schwarz bounds its absolute value by \((a_{\mathfrak a}^{\pi}a_{\mathfrak a}^{\pi'})^{1/2}\), where the two superscripts denote the nonnegative self-pairing coefficients. A second Cauchy–Schwarz inequality gives

\[
\sum_{\mathfrak a}|a_{\mathfrak a}^{\pi\times\pi'}|(N\mathfrak a)^{-\sigma}
\le
\left(\sum_{\mathfrak a}a_{\mathfrak a}^{\pi}(N\mathfrak a)^{-\sigma}\right)^{1/2}
\left(\sum_{\mathfrak a}a_{\mathfrak a}^{\pi'}(N\mathfrak a)^{-\sigma}\right)^{1/2}<\infty.
\]

The same bound at the minimum real part gives local uniform convergence. ∎

### 4.5. Why equality at the local boundary is impossible

**Corollary 4.5 (Jacquet–Shalika strict local bound).** For a unitary cuspidal \(\pi\), every local self-pairing factor, including every archimedean factor, is holomorphic and nonzero at every real \(s\ge1\). At every unramified finite place,

\[
q_v^{-1/2}<|\alpha_{i,v}|<q_v^{1/2}.
\tag{4.11}
\]

**Proof.** Choose any finite \(S\) containing infinity, all ramified places and any additional places desired. Its self-pairing series has abscissa \(c\ge1/n\), by (4.5). Suppose an omitted local factor had a pole at one. Its entire reciprocal would vanish there. In (4.6) this zero would cancel the complete function's simple pole at one. The other reciprocal factors are entire, so they cannot restore a pole. The partial product would then be holomorphic near every positive real point, because the complete function's only poles are zero and one. Lemma 4.1 would forbid any finite positive abscissa, contradicting \(c\ge1/n\). Hence no omitted local factor has a pole at one. Local factors have no zeros wherever finite, by Lemma 2.2, so each is a holomorphic unit there. Any particular place can be included in \(S\); the conclusion holds at every place. It also shows that every such partial self-pairing has a simple pole at one.

At a real \(x>1\), Proposition 4.4 makes the partial self-pairing finite and nonzero. The complete function is holomorphic there by Theorem 3.1. In its factorization as the partial function times the omitted local factors, a pole of any local factor could not be cancelled: every other local factor has no zeros by Lemma 2.2. Such a pole would give a complete pole. Hence each local factor is also holomorphic and nonzero at every such \(x\). This includes archimedean places.

For an unramified \(v\), (4.7) gives \(R_v^2\le q_v\). If equality held, the \((i,i)\) denominator in (2.4), for an \(i\) of maximum modulus, would vanish at \(s=1\). Numerator one prevents cancellation. This contradicts the local regularity just proved, so \(R_v<q_v^{1/2}\). Apply the same argument to \(\widetilde\pi\), whose eigenvalues are the inverses, to get the lower bound. ∎

Convergence in the open half-plane alone only gave (4.7). The strict inequality used the complete pole theorem, positivity and the determinant coefficients. For example the formal self-pairing class \(q_v^{1/2},q_v^{-1/2}\) gives

\[
\frac1{(1-q_v^{1-s})(1-q_v^{-s})^2(1-q_v^{-1-s})}.
\tag{4.12}
\]

Its local geometric series converges for \(\operatorname{Re}s>1\), but it has a pole at one. The trivial representation of \(GL_2(F_v)\) realizes that class; its automorphic realization is residual, not cuspidal. It therefore lacks the cuspidal complete-pole hypothesis used in the proof. A partial Euler product by itself also says nothing about an omitted place. Our proof handles that place by including it in \(S\) and ruling out cancellation of the complete pole.

There is no uniform \(\delta>0\) in this argument such that \(|\alpha_{i,v}|\le q_v^{1/2-\delta}\) at every place. The result also does not imply the Ramanujan conjecture \(|\alpha_{i,v}|=1\).

### 4.6. Nonvanishing on the entire boundary line

**Theorem 4.6 (Shahidi, 1980; boundary nonvanishing, positivity proof).** For unitary cuspidal \(\pi,\pi'\) and finite \(S\) containing infinity and all ramified places, \(L^S(s,\pi\times\pi')\) has no zeros on \(\operatorname{Re}s=1\). A point on that line can be a pole; at every holomorphic point the value is nonzero.

**Proof.** Fix real \(t\), and set \(\tau=\widetilde{\pi'}\otimes\nu^{-it}\). This is unitary cuspidal, and the twist identity gives

\[
L^S(s,\pi\times\widetilde\tau)
=L^S(s+it,\pi\times\pi').
\]

If \(\tau\simeq\pi\), Corollary 4.5 makes the left side have a simple pole at one. Suppose instead that \(\tau\not\simeq\pi\) and that the left side vanishes at one. Form

\[
D(s)=L^S(s,\pi\times\widetilde\pi)
L^S(s,\tau\times\widetilde\tau)
L^S(s,\pi\times\widetilde\tau)
L^S(s,\tau\times\widetilde\pi).
\tag{4.13}
\]

The last two factors are conjugate on the real axis. This follows from their good Euler factors and \(\widetilde\pi\simeq\overline\pi\), \(\widetilde\tau\simeq\overline\tau\), first in a convergent half-plane and then by continuation. Their orders at the real point one are equal. Each has a zero of order at least one. Each self factor has a simple pole there by Corollary 4.5, so the zeros cancel both poles in (4.13).

Because \(\tau\not\simeq\pi\), the complete cross factors have no pole at the real points one or zero. An imaginary norm relation between \(\tau\) and \(\pi\) can give poles at other complex points, but cannot give a positive real pole. Theorem 3.1 and the entire reciprocal local factors therefore show that \(D\) is holomorphic near every positive real point, including one after the cancellation.

At a good place the product of the four factors is the self-pairing factor for the union of the eigenvalue lists of \(\pi_v\) and \(\tau_v\). Lemma 4.2 makes its coefficients nonnegative and bounds its coefficient at every \((n+m)\)-th ideal power below by one. Proposition 4.4 supplies initial convergence. Thus its abscissa is finite and at least \(1/(n+m)>0\). Landau's Lemma 4.1 contradicts its holomorphy at every positive real point. The supposed zero does not exist. Twisting back proves the assertion at \(1+it\) for every \(t\). ∎

The pole-versus-zero argument here is the positivity method discussed in [Sarnak, *Nonvanishing of L-functions on Re(s)=1*, §1]. The determinant coefficient and Landau step explain why cancellation of two simple poles cannot leave a positive series holomorphic on the whole positive real axis. Continuation and a functional equation by themselves do not prove the theorem.

### 4.7. The partial pole test

**Proposition 4.7.** For unitary cuspidal \(\pi\) on \(GL_n\) and \(\pi'\) on \(GL_m\), \(L^S(s,\pi\times\pi')\) has a simple pole at one exactly when \(n=m\) and \(\pi'\simeq\widetilde\pi\). Otherwise it is holomorphic and nonzero there.

**Proof.** In the dual case Corollary 4.5 proves the simple partial pole. In every other case Theorem 3.1 makes the complete function holomorphic at one. Multiplication by the entire reciprocal factors in Lemma 2.2 proves holomorphy of the partial function. Theorem 4.6 proves its nonvanishing. ∎

For completeness these arguments also establish the local boundary assertion needed for the global cuspidal pairs considered here. For \(\operatorname{Re}s>1\), Proposition 4.4 makes \(L^S\) nonzero, while the complete function is holomorphic. No omitted local factor can have a pole, since every local factor is zero-free and such a pole would give a complete pole. At \(1+it\), Theorem 4.6 gives the same conclusion unless the complete function has a pole. In that case the shifted dual relation of Theorem 3.1 reduces every local factor to a self-pairing at one, and Corollary 4.5 applies. Hence all local factors of these global pairs are holomorphic and nonzero on \(\operatorname{Re}s\ge1\). We have not asserted absolute convergence there of every local integral for arbitrary unitary generic local representations.


## 5. Strong multiplicity one from the pole criterion

**Theorem 5.1 (Jacquet–Shalika, 1981; strong multiplicity one, analytic deduction).** If \(\pi,\pi'\) are unitary cuspidal automorphic representations of \(GL_n(\mathbb A)\) and \(\pi_v\simeq\pi'_v\) for all but finitely many places, then \(\pi\simeq\pi'\). The original analytic argument is due to Jacquet and Shalika. See also [Getz–Hahn, 22 April 2022 draft, Theorem 11.7.2]. We prove it from Theorem 3.1 and the positivity results above.

**Proof.** Choose \(S\) containing the exceptional places, infinity, and all ramified places. The local agreement gives equality of the partial products

\[
L^S(s,\pi\times\widetilde{\pi'})
=L^S(s,\pi\times\widetilde\pi).
\tag{5.1}
\]

Initially this is equality in an absolutely convergent half-plane by Proposition 4.4. Both sides have meromorphic continuation, so the identity theorem extends the equality to the plane. Proposition 4.7 says that the right side has a simple pole at one. It also says that the left side has such a pole only if \(\widetilde{\pi'}\simeq\widetilde\pi\). Taking contragredients gives \(\pi'\simeq\pi\). The simple partial self-pairing pole has already been proved in Corollary 4.5; it is not inferred from a complete pole without checking cancellation. ∎

Agreement of Satake classes outside a finite set suffices, by spherical classification. The theorem concerns almost all places; it does not assert that an arbitrary single local component determines a cusp.

The self-pairing pole is invariant under any common norm twist, even a nonunitary one:

\[
\mathcal L(s,(\pi\otimes\nu^a)\times
\widetilde{(\pi\otimes\nu^a)})
=\mathcal L(s,\pi\times\widetilde\pi).
\tag{5.2}
\]

Indeed the contragredient twist is \(\nu^{-a}\), so the two shifts in (3.3) cancel. Unitary normalization is needed for the stated analytic inputs and estimates, but the pole of a representation paired with its own contragredient does not move under a common twist. Independently twisting just the second member moves it as in (3.2).

## 6. Isobaric sums and uniqueness with multiplicities

An **isobaric sum**

\[
\Sigma=\boxplus_{i=1}^r\rho_i
\tag{6.1}
\]

of cuspidal automorphic representations of \(GL_{n_i}(\mathbb A)\) is the automorphic representation of \(GL_N(\mathbb A)\), \(N=\sum_i n_i\), obtained by taking at each place the representation attached to the union of their local Langlands data. It is an irreducible automorphic subquotient of normalized parabolic induction. The global existence theorem is [Getz–Hahn, 22 April 2022 draft, Theorem 10.6.5]; local construction and order independence are in Theorems 10.5.1–10.5.2 and equation (10.21). These existence and local-classification results are not proved here. We do not assume that a naïve induction from the entire \(\rho_{i,v}\), in an arbitrary order, always has this representation as its unique quotient.

An arbitrary automorphic subquotient need not be an isobaric sum. Also, a unitary isobaric representation need not be a sum of *unitary cuspidal constituents*. Residual examples in §7 explain the distinction.

Every cuspidal constituent can be written uniquely as

\[
\rho_i=\sigma_i\otimes\nu^{a_i},\qquad
a_i\in\mathbb R,\qquad \sigma_i\text{ unitary cuspidal}.
\tag{6.2}
\]

Here imaginary norm twists remain part of \(\sigma_i\). The real exponent is determined by the modulus of its central character, and Theorem 1.19 proves existence of the cuspidal Hilbert realization and hence of this unitary normalization. At an unramified place the eigenvalue multiset of \(\Sigma_v\) is the union, with multiplicities, of \(q_v^{-a_i}\) times the eigenvalue multisets of \(\sigma_{i,v}\). At good places multiplicativity against an isobaric sum follows directly from the union of eigenvalue multisets and (2.2). Only these good-place products are needed in the uniqueness proof.

**Theorem 6.1 (Jacquet–Shalika, 1981; isobaric uniqueness, analytic deduction).** Two isobaric sums are isomorphic if their Satake classes agree at almost every finite place. Their multisets of cuspidal constituents, including repeated constituents and real norm exponents, are then equal. Compare [Getz–Hahn, 22 April 2022 draft, Corollary 11.7.3].

**Proof.** Write the two sums as lists \((\sigma_i,a_i)\) and \((\sigma'_j,a'_j)\) in the normalization (6.2). Choose a finite \(S\) containing infinity, all ramified places of every constituent, and all places where the Satake classes disagree. If both lists are empty the assertion is immediate. Otherwise let \(A\) be the largest real exponent occurring in either list, and choose a unitary cusp \(\sigma\) paired with exponent \(A\) in one of them.

Pair \(\sigma\) with the *contragredient of each sum*. Define

\[
P_\Sigma(s)=\prod_i L^S(s-a_i,\sigma\times\widetilde{\sigma_i}),\qquad
P_{\Sigma'}(s)=\prod_j L^S(s-a'_j,\sigma\times\widetilde{\sigma'_j}).
\tag{6.3}
\]

The minus sign comes from taking the contragredient of \(\nu^{a_i}\). The local union of eigenvalues and (2.2) show that these products have identical Euler factors outside \(S\). They converge for \(\operatorname{Re}s>1+A\), by Proposition 4.4 applied to each shifted factor. Hence they are equal there and everywhere by meromorphic continuation.

Examine the real point \(s_0=1+A\). If \(a_i<A\), the argument \(s_0-a_i\) is strictly greater than one, so Proposition 4.4 makes that factor holomorphic and nonzero. If \(a_i=A\), its argument is one. Proposition 4.7 makes it a simple pole exactly when \(\sigma_i\simeq\sigma\), and otherwise a holomorphic nonzero value. Thus

\[
\operatorname{ord}_{s=s_0}\text{ pole of }P_\Sigma
=\#\{i:a_i=A,\ \sigma_i\simeq\sigma\}.
\tag{6.4}
\]

There are no zeros to cancel these poles. Equality of the two meromorphic products gives equality of the two counts. In particular the chosen constituent \(\sigma\otimes\nu^A\) occurs in both sums with the same positive multiplicity.

Remove all its matched copies from both lists. At every place outside \(S\), remove the corresponding Satake eigenvalues with multiplicities from the two equal eigenvalue multisets. Multiset subtraction is valid even when eigenvalues of different constituents coincide: for each complex number the same finite multiplicity is subtracted from both sides. The remaining unions are still equal. Repeat the argument with the largest exponent in the remaining lists. Each step removes at least one constituent from each list, so the procedure ends after finitely many steps. It cannot end with only one nonempty list: choosing its largest exponent would force a pole in its probe (6.3), whereas the empty list gives the function one. Therefore all constituents match with multiplicity.

The order-independent local isobaric construction then identifies the local representations at every place, including those in \(S\). Their restricted tensor products are isomorphic, giving \(\Sigma\simeq\Sigma'\). ∎

For sums of unitary cusps all exponents are zero, so the test is the pole order at one. For general sums the largest-real-exponent argument is essential. Testing the opposite pairing at \(1-A\) would place some factors to the left of one, where zeros could cancel poles; the proof deliberately uses the arguments \(1+A-a_i\ge1\).

This proves uniqueness given existence. It does not construct the global automorphic isobaric sum, and it does not classify every automorphic subquotient.

## 7. The residual spectrum and a computed example

Fix a unitary cuspidal \(\sigma\) on \(GL_d(\mathbb A)\), normalized to be trivial on the positive split center, and let \(m\ge1\). Its discrete Speh representation on \(GL_{dm}(\mathbb A)\) is

\[
\operatorname{Speh}(\sigma,m)
=\boxplus_{j=1}^m\left(\sigma\otimes
\nu^{(m+1)/2-j}\right).
\tag{7.1}
\]

**Theorem 7.1 (Mœglin–Waldspurger, 1989; discrete spectrum of GL_n).** On the automorphic quotient by the positive split center, every irreducible constituent of the discrete \(L^2\) spectrum of \(GL_n\) is \(\operatorname{Speh}(\sigma,m)\) for a unique pair \((\sigma,m)\) with \(dm=n\), and each occurs with multiplicity one. The case \(m=1\) is cuspidal; the cases \(m>1\) form the residual discrete spectrum and arise from iterated residues of Eisenstein series. The original complete classification is [Mœglin–Waldspurger, *Le spectre résiduel de GL(n)*, théorème de l'introduction]. A further free exposition of the statement is [Getz–Hahn, 22 April 2022 draft, Theorem 10.7.1 and (10.24)]. The construction of the residues and proof of exhaustiveness are not given here. To work with other unitary split-central characters, restore the corresponding imaginary norm twists.

At an unramified place with eigenvalues \(\alpha_1,\ldots,\alpha_d\) for \(\sigma_v\), the complete list for (7.1) is

\[
\alpha_i q_v^{-(m+1)/2+j}
\quad(1\le i\le d,\ 1\le j\le m).
\tag{7.2}
\]

Consequently

\[
L_v(s,\operatorname{Speh}(\sigma,m))
=\prod_{j=1}^m L_v(s+(m+1)/2-j,\sigma_v).
\tag{7.3}
\]

For \(d=1,m=2,\sigma=1\), the two characters are \(\nu^{1/2},\nu^{-1/2}\). The Speh representation is the trivial representation of \(GL_2(\mathbb A)\) on the split-central quotient. Its eigenvalues are \(q_v^{-1/2},q_v^{1/2}\), and over \(\mathbb Q\) its finite standard L-function is

\[
\zeta(s+1/2)\zeta(s-1/2).
\tag{7.4}
\]

It is unitary but nongeneric, and its isobaric constituents are not unitary. Thus it neither contradicts Corollary 4.5 nor falls under the entire-cuspidal assertion of Theorem 1.1. This is the automorphic realization of the boundary example (4.12).

## 8. GL_2 times GL_1: twisting a modular form

Let \(f(z)=\sum_{r\ge1}a_r e^{2\pi irz}\) be a normalized holomorphic cuspidal Hecke newform over \(\mathbb Q\), of weight \(k\ge2\), level \(N\), and nebentypus \(\omega\). Let \(\pi_f\) be its unitary automorphic representation. At \(p\nmid N\), its two unitary-normalized Satake eigenvalues satisfy

\[
\alpha_p+\beta_p=a_pp^{-(k-1)/2},\qquad
\alpha_p\beta_p=\omega(p).
\tag{8.1}
\]

Let \(\chi\) be a primitive Dirichlet character, viewed as its unitary Hecke character with the convention \(\chi_p(p)=\chi(p)\) at an unramified prime. At \(p\nmid N\operatorname{cond}(\chi)\), (2.2) gives

\[
L_p(s,\pi_f\times\chi)
=\frac1{(1-\alpha_p\chi(p)p^{-s})(1-\beta_p\chi(p)p^{-s})}
=\frac1{1-a_p\chi(p)p^{-(s+(k-1)/2)}
+\omega(p)\chi(p)^2p^{-2s}}.
\tag{8.2}
\]

Put \(u=s+(k-1)/2\). The denominator becomes

\[
1-a_p\chi(p)p^{-u}+\omega(p)\chi(p)^2p^{k-1-2u}.
\tag{8.3}
\]

Expanding its reciprocal gives coefficients \(b_{p^r}=a_{p^r}\chi(p)^r\): the recurrence is

\[
b_{p^0}=1,\quad b_p=a_p\chi(p),\quad
b_{p^r}=a_p\chi(p)b_{p^{r-1}}
-\omega(p)\chi(p)^2p^{k-1}b_{p^{r-2}}.
\tag{8.4}
\]

In particular \(b_{p^2}=\chi(p)^2(a_p^2-\omega(p)p^{k-1})\) and \(b_{p^3}=\chi(p)^3(a_p^3-2\omega(p)p^{k-1}a_p)\). Multiplicativity gives the good part of the classical series \(\sum a_r\chi(r)r^{-u}\). The twist's central character is \(\omega\chi^2\), since the central scalar \(zI_2\) has determinant \(z^2\).

At infinity the standard factor of \(\pi_f\) is \(\Gamma_{\mathbb C}(s+(k-1)/2)\). Its two-dimensional real Weil parameter is induced from a character of \(\mathbb C^\times\). In the two induced basis vectors, the subgroup \(\mathbb C^\times\) acts diagonally and a representative of the other coset acts by an off-diagonal matrix. The sign character is one on the subgroup and minus one on that coset. Conjugation by \(\operatorname{diag}(1,-1)\) leaves every diagonal matrix fixed and negates every off-diagonal matrix, giving an explicit isomorphism with the sign twist. Thus the gamma factor remains \(\Gamma_{\mathbb C}(u)\) for either parity of \(\chi\). Let \(N_\chi\) be the actual finite conductor of \(\pi_f\otimes\chi\). Then

\[
\Lambda(s,\pi_f\times\chi)
=N_\chi^{s/2}\Gamma_{\mathbb C}(u)L_f(s,\pi_f\otimes\chi).
\tag{8.5}
\]

At ramified primes the local twist, rather than a guessed quadratic conductor rule, determines the factor and \(N_\chi\). When \(\chi=1\), \(N_\chi=N\) and \(L_f(s,\pi_f)=L(f,u)\). For a general twist, a naïve coefficient twist at a bad prime can differ from the standard L-function of the primitive newform in the twisted automorphic representation; (8.2) is asserted only at the stated good primes.

The conductor factor in (8.5) differs by the constant \(N_\chi^{-(k-1)/4}\) from the classical normalization \(N_\chi^{u/2}\Gamma_{\mathbb C}(u)L(f\otimes\chi,u)\), when the latter denotes the primitive twist with its correct local factors. The transformation \(s\mapsto1-s\) becomes \(u\mapsto k-u\). The entire twisted standard function and its functional equation in this rational rank-two example are proved in *Global Whittaker functions and the L-function of a cuspidal representation*, Theorems 4.2 and 5.1, applied to \(\pi_f\otimes\chi\). They also follow from Theorem 3.1, since ranks two and one exclude its pole exception. Pairing with the contragredient form and \(\chi^{-1}\) gives the classical weight-\(k\) equation. A converse theorem requires further hypotheses.

## 9. Exercises and complete solutions

**Exercise 9.1 (easy).** For an unramified generic \(\tau\) on \(GL_3(F_v)\) with eigenvalues \(a,b,c\), compute its self-pairing factor and separate the diagonal terms. Explain why the formula does not require unitarity.

**Solution 9.1.** The contragredient eigenvalues are \(a^{-1},b^{-1},c^{-1}\). Hence the nine tensor eigenvalues are three copies of one and the six ratios \(a/b,a/c,b/a,b/c,c/a,c/b\). By Theorem 2.1 and the eigenbasis argument of Proposition 2.3,

\[
L_v(s,\tau\times\widetilde\tau)
=(1-q_v^{-s})^{-3}
\prod_{x\ne y\in\{a,b,c\}}(1-(x/y)q_v^{-s})^{-1},
\tag{9.1}
\]

where the indices distinguish the three positions even if some numerical eigenvalues coincide. The tensor determinant uses inverse eigenvalues for every contragredient, regardless of unitarity. Unitarity is needed to replace the inverse multiset by the conjugate multiset and to apply the positivity argument of §4. In general rank \(n\), exactly the same computation gives the \(n\) diagonal factors and the \(n(n-1)\) indexed off-diagonal factors of (2.3). ∎

**Exercise 9.2 (medium).** Identify and repair the assertion that convergence of a partial self-pairing Euler product for \(\operatorname{Re}s>1\) by itself proves \(|\alpha_{i,v}|<q_v^{1/2}\). Prove the strict bound with the necessary additional input.

**Solution 9.2.** At an included unitary unramified place, the positive local expansion is bounded by the positive global Dirichlet series. Its nearest denominator zero has modulus \(R_v^{-2}\), where \(R_v=\max_i|\alpha_{i,v}|\). Convergence at every real \(\sigma>1\) therefore gives \(R_v^2\le q_v\). Equality is compatible with open-half-plane convergence: (4.12) supplies the geometric-series counterexample. An omitted place is not constrained by a partial product's convergence.

To obtain strictness, include the desired place in \(S\). The complete self-pairing has only a simple pole at one on the positive real axis. If the local factor had a pole there, its entire reciprocal would cancel that pole in \(L^S\), leaving \(L^S\) holomorphic at every positive real point. Cauchy's identity gives nonnegative coefficients and \(a_{\mathfrak b^n}\ge1\). Its abscissa is therefore at least \(1/n>0\); Lemma 4.1 forbids holomorphy at that real abscissa. Hence the local factor is regular at one. Equality \(R_v^2=q_v\) would produce a pole in (2.4), so \(R_v<q_v^{1/2}\). Applying the same upper bound to every inverse eigenvalue of the dual gives \(|\alpha_{i,v}|^{-1}<q_v^{1/2}\), equivalently \(|\alpha_{i,v}|>q_v^{-1/2}\). This proof uses the complete pole theorem and the positive determinant coefficients, in addition to convergence. ∎

**Exercise 9.3 (medium).** Deduce strong multiplicity one from the pole criterion, allowing arbitrary real norm twists of cuspidal representations with unitary normalizations.

**Solution 9.3.** First suppose the two cusps are unitary. Choose \(S\) containing all disagreements and ramified places. Equality of the local representations outside \(S\) gives (5.1). Corollary 4.5 shows that the removed self-pairing factors are holomorphic nonzero at one; thus the self-pairing on the right has a simple partial pole at one. Equality by continuation transfers this pole to the left. Proposition 4.7 forces \(\pi\simeq\pi'\).

Now write the general cusps as \(\rho=\sigma\nu^a\) on \(GL_n\) and \(\rho'=\sigma'\nu^{a'}\), with \(\sigma,\sigma'\) unitary and \(a,a'\) real. At one common unramified place their Satake determinants agree. The moduli of these determinants are respectively \(q_v^{-na}\) and \(q_v^{-na'}\), because the unitary central characters of \(\sigma,\sigma'\) have modulus one. Thus \(a=a'\). After removing the same twist, \(\sigma_v\simeq\sigma'_v\) at almost all places. The unitary case gives \(\sigma\simeq\sigma'\), and therefore \(\rho\simeq\rho'\). This does not apply a unitary local analytic theorem directly to a nonunitary cusp. ∎

**Exercise 9.4 (hard).** Suppose \(\rho_1\boxplus\rho_2\) and \(\rho'_1\boxplus\rho'_2\) have the same Satake classes at almost all places. Prove that their constituent multisets are equal. Include repeated constituents and nonunitary constituents.

**Solution 9.4.** Write every constituent as \(\sigma\nu^a\), with \(\sigma\) unitary and \(a\) real, and take \(S\) large enough for all four constituents and all disagreements. Choose the largest exponent \(A\) among the four, and one unitary cusp \(\sigma\) at that exponent. Probe each sum with \(\sigma\) on the left and its contragredient on the right, giving the two factors per side in (6.3). At \(s=1+A\), any smaller-exponent factor is holomorphic nonzero because its argument is greater than one. A factor at exponent \(A\) has a simple pole exactly when its unitary constituent equals \(\sigma\); all other factors there are holomorphic nonzero by Proposition 4.7. Equality of the Euler factors and meromorphic continuation imply equality of pole orders. Hence both sums have the same multiplicity of \(\sigma\nu^A\), either one or two.

If the multiplicity is two, the two lists are already equal. If it is one, subtract that constituent's eigenvalue multiset at every good place. The remaining single constituents have equal Satake classes, and the norm-twist version of strong multiplicity one proved in Solution 9.3 identifies them. Thus in both cases the original two-element multisets agree. The argument does not label equal constituents artificially, and it permits the constituents to have different ranks before the comparison. Existence and order independence of the isobaric construction then identify the two global representations. ∎


**Exercise 9.5 (medium).** In Proposition 1.2 with \(n=2\), let \(\Psi_r\) be the indicator of integral matrices of rank \(r\) modulo \(\varpi\), for \(r=0,1,2\). Express these three tests in the basis \(F_{(0,0)},F_{(1,0)},F_{(1,1)}\), and compute their normalized standard integrals. Explain why the full-rank answer must agree with integration over \(K\).

**Solution 9.5.** The lattices with quotient of type \((1,0)\) correspond to the \(q+1\) lines in \(\kappa^2\). A rank-one image lies in exactly one line; the zero image lies in all of them. The lattice of type \((1,1)\) is uniquely \(\varpi\mathcal O^2\). Therefore

\[
\Psi_0=F_{(1,1)},\qquad
\Psi_1=F_{(1,0)}-(q+1)F_{(1,1)},\qquad
\Psi_2=F_{(0,0)}-F_{(1,0)}+qF_{(1,1)}.
\tag{9.2}
\]

The basic matrix test is \(\Psi_0+\Psi_1+\Psi_2=F_{(0,0)}\).
Let the Satake eigenvalues be \(\alpha_1,\alpha_2\). The \(q+1\) right-coset representatives of \(K\operatorname{diag}(\varpi,1)K\) are
\(\begin{psmallmatrix}\varpi&a\\0&1\end{psmallmatrix}\), \(a\in\kappa\), and
\(\operatorname{diag}(1,\varpi)\). The normalized inducing spherical function has values \(q^{-1/2}\alpha_1\) on the first \(q\) representatives and \(q^{1/2}\alpha_2\) on the last. Thus
\(\eta(T_{(1,0)})=q^{1/2}(\alpha_1+\alpha_2)\).
The central double coset has one coset and
\(\eta(T_{(1,1)})=\alpha_1\alpha_2\).
By (1.5oe), with \(u=s+1/2\) and \(X=q^{-s}\), their normalized integrals are respectively \((\alpha_1+\alpha_2)X\) and \(q^{-1}\alpha_1\alpha_2X^2\); that of \(F_{(0,0)}\) is one. Hence

\[
\begin{aligned}
\frac{Z(s,\Psi_0,c_0)}{L(s,\tau)}
&=q^{-1}\alpha_1\alpha_2X^2,\\
\frac{Z(s,\Psi_1,c_0)}{L(s,\tau)}
&=(\alpha_1+\alpha_2)X-(1+q^{-1})\alpha_1\alpha_2X^2,\\
\frac{Z(s,\Psi_2,c_0)}{L(s,\tau)}
&=1-(\alpha_1+\alpha_2)X+\alpha_1\alpha_2X^2.
\end{aligned}
\tag{9.3}
\]

The last expression is \(L(s,\tau)^{-1}\), so the unnormalized integral is one. Indeed \(\Psi_2|_G=\mathbf1_K\), \(c_0|_K=1\), and \(\operatorname{vol}K=1\). This also checks the determinant shift in (1.5oe). \(\square\)


**Exercise 9.6 (medium).** In Proposition 1.1a, explain why using the same positive scalar at every infinite embedding preserves arbitrary number fields, including fields with several complex places and nonprincipal ideal classes. Verify the two different exponents in the scalar idèle \(s_\lambda\) and central matrix \(a_t\). For a pair of adjacent diagonal entries, derive the strict height contradiction from (1.5b.4)–(1.5b.5).

**Solution 9.6.** The \(r_1\) real absolute values and \(r_2\) squared complex absolute values give the idèle norm of a common scalar \(b\) as
\(b^{r_1+2r_2}=b^d\). Thus \(s_\lambda\) uses \(\lambda^{1/d}\).
A central rank-\(n\) matrix of scalar \(b\) has determinant \(b^n\), so its adelic determinant norm is \(b^{nd}\); hence \(a_t\) uses \(t^{1/(nd)}\).
After rational rescaling, every diagonal idèle is \(s_\lambda h\), with \(h\) in the compact norm-one representative set. This factor retains its finite valuations and unit/embedding imbalance. No principal-ideal representative or uniformity of the original archimedean components is assumed.

For the adjacent pair \(i,r=i+1\), put \(u=T_{ir}/t_r\).
If \(b_i/b_r<(2MDL)^{-1}\), the rational row
\(\beta e_i-\alpha e_r\) has coordinates \(\beta t_i,(\beta u-\alpha)t_r\).
After division by \(t_r\), its two ordinary infinite moduli are less than \(1/2\), so its real local length ratio is less than \(2^{-1/2}\) and its complex normalized length ratio is less than \(1/2\).
At every finite place the ratio is at most one because \(D\) clears all compact diagonal ratios and the approximation error is integral. The total height ratio is therefore less than
\(2^{-r_1/2-r_2}=2^{-d/2}<1\), contradicting the selected last row's minimum. This proves a uniform lower bound for every adjacent ratio with exactly the lesson's scalar convention. \(\square\)


**Exercise 9.7 (medium).** For \(GL_2(k)\), let \(E=V^J\) have dimension \(r\), let \(T_1=T_{\operatorname{diag}(\varpi,1)}\), and write \(w=\omega_\pi(\varpi)\). Compute the common denominator in (1.7g). Explain why this is generally a multiple of the canonical denominator, rather than its identification. What further conclusion about epsilon factors follows from Theorem 1.17?

**Solution 9.7.** The two scalar weights are \(z_1=q^{1/2}X\) and \(z_2=q^{-1}X^2\). Since \(T_2=wI_E\),

\[
D_J(X)=\det(I_E-q^{1/2}XT_1)(1-q^{-1}wX^2)^r.
\]

Let \(D_J\mathcal I_\pi=A\mathbb C[X,X^{-1}]\). The compact-group test giving \(1\in\mathcal I_\pi\) implies \(A\mid D_J\), and the canonical polynomial is the constant-term normalization of \(D_J/A\). Cancellations therefore remain possible; a resolvent denominator is not the canonical factor by itself. Theorem 1.17 proves one scalar Fourier equation for all tests and coefficients, so (1.7j) makes its normalized epsilon factor a Laurent unit \(cX^m\). For a compatible unitary realization, (1.7m) gives \(w_0q^{m(1/2-s)}\) with \(|w_0|=1\). The argument proves \(m\in\mathbb Z\); Theorem 1.24 and Corollary 1.24c supply its nonnegativity. Standard-conductor identification remains separate. \(\square\)

**Exercise 9.8 (medium).** Compute the Gaussian matrix generator for the determinant sign character on \(GL_2(\mathbb R)\) and the angular determinant character \((\det g/|\det g|)^2\) on \(GL_2(\mathbb C)\). Give an attaining polynomial Gaussian and explain what these computations establish about other tests.

**Solution 9.8.** In the real case \(e=1,a=0,n=2\); in the complex case \(k=2,a=0,n=2\). Formula (1.8b) gives

\[
L_{\mathbb R}(s)=\Gamma_{\mathbb R}(s+1/2)\Gamma_{\mathbb R}(s+3/2),
\qquad
L_{\mathbb C}(s)=\Gamma_{\mathbb C}(s+1/2)\Gamma_{\mathbb C}(s+3/2).
\]

The attaining tests are \(\det X\,e^{-\pi\operatorname{tr}(XX^t)}\) and \(\overline{\det X}^{2}e^{-2\pi\operatorname{tr}(XX^*)}\), respectively. Their integrals equal the displayed factors times the nonzero constants (1.8g). Every polynomial Gaussian gives a polynomial multiple of the corresponding factor by compact angular averaging and the Gram–Schmidt moment proof. The polynomial-module identity supplies every polynomial multiple, so this is the entire Gaussian-polynomial ideal for these characters. Theorem 1.18 extends these determinant-character calculations to entire normalized division and the Fourier equation for every Schwartz test; general irreducible archimedean representations remain separate. \(\square\)


**Exercise 9.9 (medium).** Let \(k=\mathbb Q_3\), let \(\chi\) be the quadratic unit character with \(\chi(3)=1\), and use \(\psi(1/3)=e^{2\pi i/3}\). For \(\tau=\chi\circ\det\) on \(GL_2(k)\), compute the scalar and matrix Gauss sums, the matrix L-factor and epsilon factor. Check the same-character double Fourier equation.

**Solution 9.9.** The character has conductor one and unit values \(\chi(1)=1,\chi(2)=-1\). Thus

\[
\mathcal G_1=e^{2\pi i/3}-e^{4\pi i/3}=i\sqrt3,
\qquad S_2=3\mathcal G_1^2=-9.
\]

All scalar Tate factors are one, so (1.20b) gives \(L_{\mathrm{mat}}(s,\tau)=1\). Formula (1.20e) gives

\[
\epsilon(s,\tau,\psi)=3^{-2s}(i\sqrt3)^2=-3^{1-2s}.
\]

Its conductor exponent is two and its central phase is \(-1\). Since \(\chi^{-1}=\chi\), multiplication by the factor at \(1-s\) gives one. This equals \(\omega_\tau(-1)=\chi((-1)^2)=1\), as required by (1.7k). The rank-one phase is \(i\), whose squared phase \(-1\) correctly accounts for the matrix example. \(\square\)


**Exercise 9.10 (medium).** Use the programme archimedean characters and the positive trace argument. For the real rank-three determinant character with \(e=1\), and the complex rank-two character with \(k=2\), compute the normalized Fourier phases. Explain why they hold for every Schwartz test and check the double Fourier sign.

**Solution 9.10.** Theorem 1.18 gives \((-i)^3=i\) in the real case and \((-i)^4=1\) in the complex case. The inverse real character has the same sign exponent; its two phases multiply to \(-1=\chi((-1)^3)\). The inverse complex character has angular weight \(-2\); its two phases multiply to \(1=\chi((-1)^2)\). These agree with the central sign of Fourier inversion. The attaining polynomial Gaussians determine the phases. The QR/angular map, continuous division by the diagonal monomials and normalized multivariable Mellin continuation give entire tempered families with local Schwartz seminorm bounds. Rank-stratum uniqueness proves the identity first for \(\Re t>0\); compact-support cutoff density and the identity theorem extend it to every Schwartz test and parameter. A Gaussian calculation alone would not provide that extension. \(\square\)

**Exercise 9.11 (medium).** For the rank-one boundary orbit in \(M_2(k)\), compute the modular factor of its stabilizer. What eigenvalue would a nonzero boundary functional at parameter \(s\) require on the first-factor Jacquet module? Explain why a countable exceptional set suffices for Theorem 1.17.

**Solution 9.11.** The stabilizer is the pair of upper and lower triangular matrices sharing their upper-left entry \(A\). Its two unipotent conjugation factors are \(|A/D|\) and \(|D'/A|\), so their product is \(\delta_1=|D'/D|\). The stabilizer-functional character is \(\chi_s\delta_1\). On \((\operatorname{diag}(1,t),I_2)\) it is \(|t|^{s-1/2}\). Thus the central Jacquet operator at \(t=\varpi\) must have eigenvalue \(q^{-(s-1/2)}\) on some finite principal-congruence fixed space. Lemma 1.17a proves that space is finite-dimensional. Each eigenvalue has a countable discrete preimage in \(s\), and there are countably many congruence levels. Outside the resulting countable union the whole-matrix functional space has dimension at most one. For each test and coefficient the difference of the two Fourier families is rational and vanishes on the dense complement; the rational identity follows. No finite-length or finiteness assertion for the full exceptional set is needed. \(\square\)


**Exercise 9.12 (hard).** In the cuspidal compactness proof, derive the exponent \(2/[d(n-1)]\) in the tail estimate (1.23j). Explain why fixing a finite level and a compact type does not by itself make the whole cusp space finite dimensional, and identify the additional condition used in Lemma 1.19e.

**Solution 9.12.** Since \(\beta=\prod_{i=1}^{n-1}\rho_i^d\), a largest adjacent ratio satisfies \(\rho_i\ge\beta^{1/[d(n-1)]}\). The zero-mean Fourier Poincaré inequality on the maximal-parabolic radical yields an energy factor \(\rho_i^{-2}\), because every crossing root is contracted by \(O(\rho_i^{-1})\). On \(\beta>R\) this is at most \(R^{-2/[d(n-1)]}\). The finite-intersection proof and its compact Iwasawa-fibre enlargement control the integration multiplicity and give (1.23j). Compact local Fourier truncation plus this tail bound makes bounded energy sets precompact; it does not bound the dimension of the Hilbert space. The compact resolvent has eigenvalues \(\kappa\to\infty\). On a fixed compact type, \(\Omega=-L+2c_\sigma\), so the extra condition \(p(\Omega)\phi=0\) retains only the finitely many eigenvalues solving \(p(-\kappa+2c_\sigma)=0\), each with finite multiplicity. This is the finite-dimensional constrained space used for admissibility and reproducing kernels. \(\square\)

**Exercise 9.13 (medium).** Let a central-finite cusp function in a fixed norm-one central character satisfy
\[
\phi(a_{e^t}x)=e^{\mu t}\sum_{j=0}^r t^j f_j(x).
\]
Compute the leading-coefficient action of a right translate by \(g\), and explain why every simple cuspidal subquotient can be realized by an actual cusp module even when its preimage has central Jordan blocks.

**Solution 9.13.** Put \(c=\log\nu(g)\) and \(g_0=g a_{\nu(g)}^{-1}\in G^1\). Right translation changes \(t\) to \(t+c\) and \(x\) to \(xg_0\). Its degree-\(r\) coefficient is therefore \(e^{\mu c}f_r(xg_0)=\nu(g)^\mu f_r(xg_0)\). Thus the degree quotient is \(\mathcal C_\omega\otimes\nu^\mu\). Theorem 1.19 proves that \(\mathcal C_\omega\) is an algebraic direct sum of simple finite cores of actual admissible Hilbert cusp constituents. For an irreducible subquotient, choose the least degree with nonzero image. The preceding degree maps to zero, so the irreducible quotient is a simple subquotient of this semisimple degree quotient and hence one of its constituent twists. Removing \(\Re\mu\) leaves the unitary imaginary norm twist. The Hilbert smooth-vector comparison and tensor-pairing theorem supply its actual smooth and local unitary realizations. No real-group invariance of the original algebraic preimage has been assumed. \(\square\)


**Exercise 9.14 (medium).** Let \(n=q=2\), let \(\sigma\) be the sign of the permutation action of \(\mathrm{GL}_2(\mathbb F_2)\) on its three nonzero vectors, and choose \(\omega(\varpi)=1\) in Corollary 1.20c. Prove the required finite-field cuspidality condition. For \(\psi_{\mathrm{res}}(x)=(-1)^x\), compute the matrix Gauss scalar, the epsilon factor and its value at \(s=1/2\).

**Solution.** An ordered basis has \(3\cdot2=6\) choices. The permutation action is faithful, because a matrix fixing all nonzero vectors fixes a basis; hence it identifies this group with \(S_3\). A nonidentity upper transvection fixes one nonzero vector and exchanges the other two, so it acts by \(-1\) in \(\sigma\). Its order-two unipotent radical consequently has no fixed vector. Every proper parabolic in rank two is the stabilizer of a line and is conjugate to this one, giving the required condition for all such radicals. The center of \(\mathrm{GL}_2(\mathbb F_2)\) is trivial, so the stated extension with \(\omega(\varpi)=1\) is allowed.

Enumerating the six matrices gives the following trace/sign pairs; inversion leaves the sign unchanged:

| Matrix \((a,b;c,d)\) | \(\operatorname{tr}h\) in \(\mathbb F_2\) | \(\sigma(h^{-1})\) | \(\psi_{\mathrm{res}}(\operatorname{tr}h)\sigma(h^{-1})\) |
|---|---:|---:|---:|
| \((0,1;1,0)\) | 0 | \(-1\) | \(-1\) |
| \((0,1;1,1)\) | 1 | \(+1\) | \(-1\) |
| \((1,0;0,1)\) | 0 | \(+1\) | \(+1\) |
| \((1,0;1,1)\) | 0 | \(-1\) | \(-1\) |
| \((1,1;0,1)\) | 0 | \(-1\) | \(-1\) |
| \((1,1;1,0)\) | 1 | \(+1\) | \(-1\) |

Thus \(\mathcal G_\sigma=-4/6=-2/3\). Since \(C_2=(1-2^{-1})(1-2^{-2})=3/8\), formula (1.24sb) yields
\[
\epsilon_\pi(s,\psi)=\frac38\,2^3\!\left(-\frac23\right)X^2
=-2X^2=-2^{1-2s},\qquad a_\pi=2.
\]
Its value at \(s=1/2\) is \(-1\). All constants use the positive trace Fourier character of this lesson. \(\square\)


**Exercise 9.15 (medium).** For \(G_2\), compute the right cosets of \(T_1\), its spherical eigenvalue, and the recurrence for \(W(\operatorname{diag}(\varpi^h,1))\), \(h\ge0\). Pair this function with an unramified character of \(G_1\) whose value at \(\varpi\) is \(u\). Evaluate the unequal-rank integral and explain the role of its \(-1/2\) determinant shift. Does this calculation alone identify the generator of all local Rankin–Selberg integrals?

**Solution.** The representatives are
\[
\begin{pmatrix}\varpi&b\\0&1\end{pmatrix},
\quad b\in\mathcal O/\varpi\mathcal O,\qquad
\begin{pmatrix}1&0\\0&\varpi\end{pmatrix}.
\]
There are \(q+1\) cosets. Their normalized spherical eigenvalue is \(q^{1/2}(t_1+t_2)\); at the Satake parameters \((q^{1/2},q^{-1/2})\) of the trivial representation it is \(q+1\), confirming the normalization. Put \(S_h=s_{(h,0)}^{(2)}(t)\). The recurrence (2.5g), together with the central eigenvalue \(t_1t_2\), gives
\[
S_0=1,\quad S_1=t_1+t_2,\quad
S_{h+1}=(t_1+t_2)S_h-t_1t_2S_{h-1}\quad(h\ge1).
\]
Thus \(S_h=\sum_{a=0}^h t_1^at_2^{h-a}\), also when \(t_1=t_2\), and \(W(\operatorname{diag}(\varpi^h,1))=q^{-h/2}S_h\). The norm weight in (2.5j) is \(q^{-h(s-1/2)}\), so its half-power cancels \(q^{-h/2}\), leaving
\[
\Psi(s,W,W')=\sum_{h\ge0}S_hu^hq^{-hs}
=\frac1{(1-t_1uq^{-s})(1-t_2uq^{-s})}.
\]
Without the determinant shift this would instead evaluate at \(s+1/2\). The calculation produces a member of the local integral family with this value. To identify its normalized generator, one still needs divisibility of every other integral and the full rational-ideal theorem; one attained value supplies neither assertion. \(\square\)


**Exercise 9.16 (medium).** For the trivial representation of \(\mathrm{GL}_1(\mathbb R)\), compare the pole majorant in Theorem 1.21 with the actual basic Gaussian integral. Does its entire quotient generate a polynomial ideal?

**Solution.** Here \(D=d/dx\) and the twisted scalar polynomial is \(b(t)=t\). With \(c_1=1\), the recurrence is
\[
s(s+1)Z(s,\Phi)=Z(s+2,\Phi''),\qquad
H(s)=\Gamma(s/2)\Gamma((s+1)/2).
\]
The Gaussian integral with \(dg=dx/|x|\) is
\(Z(s,e^{-\pi x^2})=\pi^{-s/2}\Gamma(s/2)\), by the scalar Mellin substitution \(u=\pi x^2\). Thus its majorant quotient is \(\pi^{-s/2}/\Gamma((s+1)/2)\). It is entire and nonzero as a function, but vanishes at \(s=-1,-3,-5,\ldots\), so it is not a polynomial. The canonical Gaussian ideal in this example is \(\Gamma_{\mathbb R}(s)\mathbb C[s]\), as proved in Proposition 1.7. The pole majorant supplies analytic continuation and common entire division; it supplies neither polynomial quotients nor canonical attainment. \(\square\)

**Exercise 9.17 (medium).** In Corollary 1.22f, why is the inverse additive character needed in the conjugation identity? Check that the reflection sign cancels in the critical-line modulus.

**Solution.** A unitary additive character satisfies \(\bar\psi=\psi^{-1}\), so conjugating the Fourier kernel changes the character. Character scaling with \(a=-1\) changes it back and contributes \(\omega_\pi(-I_n)\). On \(s=1/2+it\), reflection supplies the same sign from \(\gamma_\pi(s,\psi)\gamma_{\widetilde\pi}(1-s,\psi)\). Their product is \(\omega_\pi(-I_n)^2=\omega_\pi(I_n)=1\). Hence the scalar has modulus one; the Laurent argument in the corollary rules out exceptional zeros and poles there. A phase for a specified standard epsilon factor further requires the stated canonical generator and its conjugation normalization. \(\square\)


**Exercise 9.18 (medium).** In the parabolic correction (1.27t), suppose the block exponents are zero and \(R(X)=\widetilde R(X)=1-q^{1/2}X\). Determine the reverse-polynomial constant and the resulting exponent. Why is the factor \(X^d\) necessary? Which extra theorem would make this an example of a particular representation?

**Solution.** Here \(d=1\), and
\[
X\widetilde R(q^{-1}X^{-1})=X-q^{-1/2},\qquad
R(X)=-q^{1/2}\bigl(X-q^{-1/2}\bigr).
\]
Thus \(b=-q^{1/2}\) and \(a_\sigma=0+0+1=1\). Omitting \(X\) leaves a negative Laurent power, which cannot equal the polynomial with constant term one. This is a calculation under the stated correction-polynomial hypotheses. To attach it to a named representation one must additionally construct that constituent and prove that its entire matrix ideal has these particular correction polynomials. The computation alone does not provide either assertion. \(\square\)


**Exercise 9.19 (medium).** In rank three, list the permutations whose upper Bruhat orbits can carry a bi-generic distribution. Give the diagonal conditions and verify antidiagonal-transpose invariance of their representatives. Explain why an open-cell calculation alone would not prove Theorem 2.0.

**Solution.** The compositions of three give exactly
\[
(1,2,3),\quad(3,1,2),\quad(2,3,1),\quad(3,2,1).
\]
The runs are consecutive increasing intervals in decreasing order. The corresponding diagonal conditions are respectively
\(t_1=t_2=t_3\), \(t_1=t_2\), \(t_2=t_3\), and no condition. In each case the square scalar-identity blocks on the block antidiagonal are fixed by \((r,s)\mapsto(4-s,4-r)\), so \(\tau(tw_p)=tw_p\). The open upper Bruhat cell has permutation \((3,2,1)\); relevant smaller cells also carry equivariant distributions. The constructive-orbit localization and sign argument in Theorem 2.0f control distributions supported on all of these boundaries. At infinity such boundary distributions can additionally have normal derivatives; Lemmas 2.0l–2.0m explicitly control them in the distributional-principal-series argument. \(\square\)

**Exercise 9.20 (medium).** In rank two, take \(A=\varpi^{-1}\)
and \(D=\varpi\). Describe the spectral chart (1.29l), its
Sylvester factor and determinant shell. Explain why cancellation
must use the whole upper fiber and why only one shell needs
eventual containment in the proof of Theorem 1.24.

**Solution.** The larger root is \(A\), so \(r=t=1\) and
the unique spectral line has one of \(q+1\) reductions.
In each corresponding chart \(B\in\varpi\mathcal O\),
\(C\in k\), and \(k_B\in K\). The Sylvester map is
\(H\mapsto(A-D)H\), with
\(|A-D|=q\), since
\(A-D=\varpi^{-1}(1-\varpi^2)\). The determinant is 1,
so this is shell \(j=0\), and the trace \(A+D\) has
valuation \(-1\). Both are independent of \(B,C\).
The Haar density is \(\alpha_2^{-1}q\,dB\,dA\,dC\,dD\).
Vanishing in (1.29r) integrates all \(C\in k\); zero
Jacquet class gives zero average on every sufficiently large
compact unipotent subgroup, and compact coefficient support
on that fiber then gives the full integral. An arbitrary
smaller subgroup need not have zero average. If a hypothetical
exponent satisfies \(a_\pi\leq0\), the single Laurent
coefficient at \(X^{a_\pi}\) is indexed by
\(j=-a_\pi\). The coefficient support on this fixed shell
is compact, so one sufficiently large \(N\) contains it.
No support bound uniform over all shells or coefficients is
needed. \(\square\)

**Exercise 9.21 (medium).** Suppose a representation of rank
four has a cuspidal-support embedding with block ranks
\((2,1,1)\), where one character block is unramified and
the other is ramified of conductor exponent \(b\geq1\).
Bound its reciprocal matrix-factor degree and epsilon exponent.

**Solution.** The higher-rank cuspidal factor and the ramified
character factor both equal 1. If the unramified character is
\(\chi\), (1.29w) gives
\(P_\sigma R=1-\chi(\varpi)X\), so
\(\deg P_\sigma\leq1\). The rank-two block has integral
exponent at least 1 by Theorem 1.24, the ramified character has
exponent \(b\), and the unramified character has exponent 0.
Formula (1.29v) gives
\(a_\sigma\geq1+b+\deg R\geq2\).
These deductions use the assumed embedding; they do not construct
a particular named constituent or determine its correction
polynomial. \(\square\)

**Exercise 9.22 (medium).** Compute the canonical matrix factors
and Fourier phases of \(\operatorname{Sym}^5(\mathrm{std})\)
on \(GL_3(\mathbb R)\) and \(GL_3(\mathbb C)\), and of
their duals. Give one attaining coefficient and Gaussian test.
Explain the real finite cancellation and the complex dual angular shift.

**Solution.** Here \((\rho_1,\rho_2,\rho_3)=(1,0,-1)\).
Theorem 1.25 gives
\[
\begin{aligned}
L_{\mathbb R}(s)&=\Gamma_{\mathbb R}(s+7)
\Gamma_{\mathbb R}(s)\Gamma_{\mathbb R}(s-1),\\
L_{\mathbb R}^{\vee}(s)&=\Gamma_{\mathbb R}(s-5)
\Gamma_{\mathbb R}(s)\Gamma_{\mathbb R}(s+1),\\
L_{\mathbb C}(s)&=\Gamma_{\mathbb C}(s+6)
\Gamma_{\mathbb C}(s)\Gamma_{\mathbb C}(s-1),\\
L_{\mathbb C}^{\vee}(s)&=\Gamma_{\mathbb C}(s+1)
\Gamma_{\mathbb C}(s)\Gamma_{\mathbb C}(s-1).
\end{aligned}
\]
The real phase is \((-i)^1=-i\), and the complex phase is
\((-i)^5=-i\); the dual phases are the same. Over the reals
take \(c(X)=X_{11}(\sum_iX_{i1}^2)^2\),
\(\Phi=X_{11}G_{\mathbb R}\). Its integral is
\(K_{\mathbb R}L_{\mathbb R}/3\).
Over the complex field take \(c=X_{11}^5\) and
\(\Phi=\bar X_{11}^5G_{\mathbb C}\). Its integral is
\(K_{\mathbb C}L_{\mathbb C}/21\), since
\(5!/(3)_5=1/21\). The dual tests in (1.30ae), with
\(c^\vee(X)=c(X^{-1})\), attain the dual factors.

For the real original family, \(a=(s+1)/2\) and
\(L/B_{\mathbb R}=\pi^{-3}(a)_3\). The point distributions
at \(a=0,-1,-2\) are killed by every degree-five symmetric
coefficient because their first-row derivative degrees are
0, 2 and 4. For the complex dual, the special character is
\(x^{-5}|x|_{\mathbb C}^{-1}\); its radial exponent is
\(-7/2\), while its angular weight is \(-5\).
The absolute angular shift \(5/2\) gives the Tate argument
\(s-1\), as in the displayed dual product. Using a signed
angular shift would produce the wrong factor. \(\square\)

**Exercise 9.23 (medium).** A formal vector series \(Y=\sum_{m\ge0}Y_mt^m\)
satisfies \(tY'=A(t)Y\), where \(\|A_k\|\le CR^{-k}\).
Prove convergence even when \(A_0\) has a nonnegative integer
eigenvalue. Explain which coefficients may be freely chosen.

*Solution.* Comparing coefficients gives (1.38j). For every integer
\(m>2\|A_0\|\), the Neumann series gives
\(\|(mI-A_0)^{-1}\|\le2/m\). Choose \(S\ge2/R\) and an integer
\(m_0>2\|A_0\|+4C+1\); bound the finitely many given initial
coefficients by \(MS^m\). Induction then gives
\(\|Y_m\|\le (2C/m)MS^m\sum_{k\ge1}(RS)^{-k}\le MS^m\).
Thus the series converges for \(|t|<S^{-1}\). At a resonant integer,
the formal equation requires compatibility and may leave a kernel
component undetermined; it does not justify an arbitrary choice of
the entire coefficient. Only those finite compatible kernel choices
are free. The large-index estimate works for every such formal
solution.

**Exercise 9.24 (hard).** In the proof of Theorem 1.33, why is a
separate exponential estimate for each differentiated coefficient
insufficient? Prove that the one common exponent yields the required
contradiction, without extending the coefficients across singular
walls.

*Solution.* Moving \(q\) contracting root factors to the second
vector differentiates that vector \(q\) times. If the new growth
exponent depended on \(q\), it could grow faster than \(q\epsilon\).
The estimate (1.38x) instead uses one \(M\) for every core pair,
because all fixed Lie words reduce to the same finite generating
array and its bounded radial jet. Under \(V=\mathfrak nV\), iteration
gives \(V=\mathfrak n^qV\), and (1.38aa) bounds every component of
the chosen nonzero finite jet by \(C_qe^{(M-q\epsilon)t}\).
Its own bounded first-order system gives
\(\|J(t)\|\ge e^{-M_0t}\|J(0)\|\). Choosing
\(q\epsilon>M+M_0\) contradicts both bounds as \(t\to\infty\).
The ray stays in one fixed-gap regular chamber, so every identity and
bound used holds where the analytic coefficients have actually been
constructed.

**Exercise 9.25 (medium).** Construct the complete paired realization
of Theorem 1.34 from its injection \(T_0\), and explain why this does
not prove that a dense continuous comparison with an arbitrary
supplied topology is onto.

*Solution.* Take \(E=\overline{T_0V}^{\,C^\infty(K)}\) in the full
induced model and \(E^\vee=I(\boldsymbol\chi^{-1})/\operatorname{Ann}(E)\).
Theorem 1.26a proves group stability, completeness, smoothness,
moderate growth and the invariant nondegenerate compact-integral
pairing. A finite compact projector sends the closure into the
already closed finite-dimensional packet of \(T_0V\), so the core
is exactly \(V\); finite packet duality gives exactly \(V^\vee\)
in the quotient. These are statements about the constructed spaces.
Density of a continuous comparison into a second complete space
does not make its image closed: the inclusion of rapidly decreasing
sequences, with seminorms \(\sup_j(1+j)^N|a_j|\), into \(\ell^2\)
is continuous since
\(\|a\|_2\le\sqrt2\sup_j(1+j)|a_j|\): the integral comparison
\(\sum_{j\ge0}(1+j)^{-2}\le1+\int_1^\infty x^{-2}dx=2\)
proves this bound. Finite sequences show density. The domain is
complete: a Cauchy sequence for all the displayed seminorms converges
coordinatewise, and passing each uniform Cauchy bound to the limit
gives convergence in every seminorm. The inclusion still omits the
\(\ell^2\) sequence \(a_j=(1+j)^{-1}\), whose seminorm for \(N=2\)
is infinite. Completeness of the domain alone therefore
provides no onto conclusion. An inverse seminorm estimate or an
independent closed-range argument would still be needed.

**Exercise 9.26 (medium).** Let \(P_1,P_2\in\mathbf C[X]\)
have constant term one. Suppose the test ideals with generators
\(1/P_1\) and \(1/P_2\) satisfy
\((1/P_1)\mathscr R\subset(1/P_2)\mathscr R\), where
\(\mathscr R=\mathbf C[X,X^{-1}]\). Determine the direction of
divisibility and explain the subquotient correction in Corollary 2.3ad.

*Solution.* Inclusion says \(P_2/P_1\in\mathscr R\).
This rational function is regular at zero, so its Laurent polynomial
has no negative powers and belongs to \(\mathbf C[X]\).
Therefore \(P_1\mid P_2\), and
\(L_1=L_2(P_2/P_1)\); its polynomial correction has value one at
zero. With the irreducible subquotient as family 1 and the induction
as family 2, this is precisely the correction in Corollary 2.3ad.
Reversing the ideal inclusion would reverse the divisibility claim.

**Exercise 9.27 (hard).** Derive the chart measure (2.14f) and explain
why the extra row test is necessary when \(N=r+1\) in Lemma 2.3aa.

*Solution.* In (2.14e), changing the upper-right column from \(y\)
to \(my\) has additive Jacobian \(\nu(m)\); changing the bottom-right
entry to \(a+xy\) has Jacobian one. The determinant is \(\det(m)a\).
Multiplying the density \(\alpha_{r+1}^{-1}|\det g|^{-r-1}\)
by \(\alpha_r\nu(m)^r\,dm\),
\((1-q^{-1})|a|\,d^\times a\), and that Jacobian leaves
\[
 \frac{\alpha_r(1-q^{-1})}{\alpha_{r+1}}
       |a|^{-r}\,dm\,dx\,d^\times a\,dy.
\]
Dividing \(dm\) by the prescribed measure of \(N_r\) gives
(2.14f). When \(N\ge r+2\), the root \(E_{r+1,r+2}\) exists and
its Fourier average cuts the \(a\)-variable down to a unit
neighborhood. When \(N=r+1\) that root is absent. The equal-rank
Schwartz test \(\chi(x)b(a)\) cuts both remaining variables down,
and sufficiently small upper-chart support makes it invariant under
\(a\mapsto a+xy\). Its two probability integrals and
\(\int\phi=c_r^{-1}\) give the old test with exactly the old
determinant exponent. Thus the equality-rank edge is an actual
test construction.

**Exercise 9.28 (medium).** Suppose parabolic multiplicativity gives
\(L(X)=D(X)P(X)\), where \(P\) is a polynomial with \(P(0)=1\).
Show that an actual test with value \(D(X)\) forces \(P=1\).
Why would a gamma product alone be insufficient?

*Solution.* The actual test belongs to the full ideal \(L\mathscr R\),
so \(D/(DP)=P^{-1}\) is a Laurent polynomial. Hence \(P\) is a
Laurent unit. For two nonzero Laurent polynomials, their smallest
exponents add under multiplication and their largest exponents add
as well: the two extreme coefficients are nonzero products.
If their product is one, their nonnegative exponent widths sum to
zero. Each factor is therefore a monomial. Since \(P\) is a
polynomial with constant term one, it is the monomial 1.
A gamma product compares a factor with its reflected dual factor;
it alone does not determine that numerator correction. The actual
test inclusion supplies the missing ideal information.

## 10. What this lesson does not prove

The determinant computation, Landau's lemma, Cauchy's identity and coarse initial convergence are proved above. Assuming the analytic identification and complete pole theorem in Theorems 2.1 and 3.1, the subsequent proofs establish absolute convergence for \(\operatorname{Re}s>1\), the strict local bound, boundary nonvanishing, strong multiplicity one and uniqueness of the cuspidal constituent multiset. These are conditional deductions until those general analytic proofs are supplied.

The degree-one analytic theory has a preceding complete proof in *Hecke L-functions and the Dedekind zeta function*, Theorems 10.1–10.2. For \(GL_2/\mathbb Q\), the standard-function construction, fixed local test vectors, entireness and twisted functional equation have preceding proofs in *Global Whittaker functions and the L-function of a cuspidal representation*, §§3–5. These statements have the field and rank scope indicated; they do not supply a proof of the general \(GL_n\times GL_m\) analytic theorem.

The following statements made in this lesson still require the indicated general-rank constructions.

- For Theorem 1.1, the remaining local input 1.1c consists of standard-conductor and standard-factor identification for general finite-place irreducibles, and explicit archimedean standard-factor identification. Theorem 1.31 proves Gaussian-ideal existence, finite attainment, entire Schwartz division and compatible factor conjugation in every prescribed actual complete smooth moderate dual-pair model. Theorems 1.21–1.22 prove general archimedean full-Schwartz continuation, a common pole majorant with entire quotients and strip bounds, and the scalar Fourier equation in actual smooth dual-pair models; Proposition 1.21b and Corollary 1.22e prove canonical division and constant epsilon under the genuine Gaussian-ideal premise. Corollary 1.22f proves the unitary scalar critical-line phase. These results do not identify the canonical factor. Proposition 1.3 has proved the entire finite-place matrix ideal and its attaining generator in every rank, including ramification; Theorem 1.17 proves the scalar Fourier equation for every finite-place smooth admissible irreducible representation; the Laurent-unit, reflection-sign, character-scaling and compatible-unitary consequences in (1.7j)–(1.7m) therefore apply. Proposition 1.16 does prove the full finite-place theory and exact nonnegative conductor in the matrix/Tate-product normalization for determinant characters in every rank, including ramification. Lemma 1.20a proves compact-mod-center coefficient support from zero proper Jacquet modules. Theorem 1.20 proves strictly positive exponent for every irreducible admissible compact induction from finite-dimensional data on an open compact-mod-center subgroup, including positive-depth data; Corollary 1.20c constructs the depth-zero family and proves exponent n. Lemma 1.20d proves the polynomial degree correction, whose parabolic identities are now proved by Theorem 1.23 and Corollary 1.23c for the full induced matrix family and every irreducible subquotient. Theorem 1.23e proves general cuspidal-support embedding; Lemmas 1.23f–1.23g prove compact inducing realization from the stated finite-subspace or compact-intertwining criteria. Theorem 1.24 proves strict matrix-exponent positivity for every terminal higher-rank cuspidal block by finite spectral charts, full unipotent-fiber cancellation and the exact Fourier-shell extraction. Corollary 1.24c consequently proves the nonnegative matrix exponent for every irreducible, and Corollary 1.24d gives the factor-degree bound and exponent-zero consequence. Universal compact-induction data are unnecessary for these conclusions; standard-factor/conductor identifications remain open. Propositions 1.5–1.7 prove polynomial-module closure and the full Gaussian ideal for determinant characters over both real and complex fields, and Theorem 1.18 proves their full-Schwartz continuation, normalized division and Fourier equation with exact real/complex phases. Theorem 1.25 proves the full canonical Gaussian ideal, finite attainment, entire Schwartz division, Fourier equation and exact dual/conjugation formulas for every norm-twisted symmetric power in each rank, its complex antiholomorphic companion and their duals. Theorem 1.26 now proves the exact Gaussian product and whole-Schwartz Fourier package for every full Borel induction. Theorems 1.26a–1.26b construct actual closure, quotient and admissible dual models for every supplied principal-core subquotient, with an exact finite monic polynomial correction, finite attainment, entire division, Fourier reflection and unitary conjugation normalization. Theorems 1.27–1.31 prove nilpotent finite generation, nonzero Jacquet quotient, principal-core occurrence, analytic coefficient comparison, a complete common refinement and the full Gaussian package in every prescribed actual dual-pair realization. Theorems 1.32–1.34 prove existence and full Borel occurrence for every abstract irreducible admissible core. Full onto/closed-image comparison and explicit standard-factor/scalar identification remain required. Theorems 1.11 and 1.13 prove compatible unitary realization and tensor pairings for an actual admissible Hilbert cusp constituent; Proposition 1.14 and Lemma 1.15 give the stated reverse-comparison routes. Theorem 1.19 proves realization and admissibility for every abstract cuspidal subquotient: local elliptic estimates, rapid decay without a prior realization, bounded covering multiplicity, compact cusp energy embedding, finite-dimensional constrained cusp spaces, compact convolution and discrete Hilbert spectrum, constituent admissibility, and the positive-central Jordan filtration are all supplied. Proposition 1.1a proves general adelic reduction, and Proposition 1.2 proves the whole unramified matrix family and its Fourier equation with epsilon factor one. Lemmas 1.1b and 1.1d supply the cusp and matrix estimates; singular-orbit cancellation, Poisson, Mellin continuation, strip bounds, Euler-product recovery and the global functional-equation deduction are proved in §1 from the remaining precise inputs. The free readings are [Goldfeld–Jacquet, §§2–5 and 8–9] and [Getz–Hahn, 22 April 2022 draft, Theorem 6.5.1].
- Theorem 2.1: ordered essentially tempered constituent factors, and the general archimedean Rankin–Selberg local factors and their equation. Theorems 2.3ac–2.3ae prove finite-place parabolic gamma multiplicativity, the exact polynomial correction and the full spherical generator. Propositions 2.3b–2.3d prove the entire finite-place rational ideal and finite actual test-sum attainment in all ranks and both field characteristics. Corollary 2.3f proves index independence, Proposition 2.3g proves generic pairing uniqueness by orbit depth and global derivative polynomials, Theorem 2.3h proves the scalar functional equation, and Proposition 2.3i and Corollary 2.3j prove Laurent epsilon, reflection and exact character/norm laws. Theorems 2.3l–2.3n prove the complete finite-place rank-one ideal, gamma and epsilon identification with the twisted matrix factors and the stated generic-block multiplicativity. Theorem 2.3ac and Corollary 2.3ad below prove higher-rank finite-place multiplicativity with its exact polynomial correction; Theorem 2.3ae identifies the whole spherical generator. Ordered essentially tempered data identification remains required. Theorem 2.0 proves finite-place Whittaker uniqueness for every irreducible smooth admissible representation, every nondegenerate character and every rank/field, including the zero Hom case. Its localization, Bruhat symmetry, contragredient identification and convolution-kernel proof are written in full. Theorem 2.0n proves the all-rank real/complex distributional-principal-series bound and kills every transverse boundary jet; Corollary 2.0o transports it through a specified continuous-dual embedding. Theorems 2.0x–2.0y now construct it for every prescribed actual complete smooth moderate dual-pair model, and Theorem 2.0z proves the general archimedean bound in that class, including nonunitary and nongeneric representations. Lemmas 2.0p–2.0r and Theorem 2.0s prove generic Casimir eigendistribution symmetry in every real and complex rank by finite transverse-order and explicit Bruhat normal-symbol arguments. Lemmas 2.0t–2.0u prove smoothing of Hilbert distribution vectors and the full smooth-space kernel argument. Theorem 2.0v proves uniqueness for every compatible unitary model with irreducible admissible compact-type core and all determinant twists; Theorems 1.19 and 1.11–1.13 supply these hypotheses for every actual archimedean cusp factor. Together with the preceding local existence proof their cusp-model functional spaces are exactly one-dimensional. No opposite-functional existence or onto model comparison is needed for this general uniqueness proof; Theorem 1.34 proves abstract-core existence; full onto comparison remains a separate obligation. Proposition 2.1a proves uniqueness for every unramified irreducible and the normalized spherical formula whenever it is generic. Lemma 2.1b and Proposition 2.1c prove the all-rank spherical integral values, including unequal ranks and repeated parameters; Theorem 2.3ae now uses the full parabolic polynomial correction to prove that this spherical value is the generator of the whole ideal. Global cuspidal genericity and local Whittaker existence under the precise smooth-realization hypothesis have preceding proofs in *Automorphic representations and automorphic L-functions*, Theorem 1.3 and Corollary 1.4; Theorem 1.19 supplies that realization and comparison for every abstract cuspidal subquotient. The precise free sources for the remaining local assertions are [Jacquet–Piatetski-Shapiro–Shalika, *Rankin–Selberg convolutions*, §§2.7, 3–7 and 9.4] and [Getz–Hahn, 22 April 2022 draft, §§11.5–11.6]. Lemma 2.2 proves the entire-reciprocal property once the factor shape is established.
- Theorem 3.1 for arbitrary number fields and arbitrary positive ranks: complete global continuation, the functional equation with conductor and root number, and the exact simple dual-pairing poles after split-central normalization and imaginary twists. The theorem is [Getz–Hahn, 22 April 2022 draft, Theorem 11.7.1]; the local twist identity extends the normalized statement. The unfolding, analytic estimates and pole calculation are not proved here. Boundary nonvanishing is proved in Theorem 4.6, rather than included among these assumptions.
- Local and global isobaric existence in §6: local classification constructs the order-independent irreducible representation from essentially square-integrable data; the global sum is an automorphic subquotient; the unitary cuspidal norm normalization has now been proved in Theorem 1.19. The exact free statement locators for the remaining classification/existence assertions are [Getz–Hahn, 22 April 2022 draft, Theorem 6.5.1, Theorems 10.5.1–10.5.2, equation (10.21), and Theorem 10.6.5]. The proof of multiset uniqueness does not assume that existence is a consequence of the good-place Euler product.
- Theorem 7.1: the discrete spectrum consists exactly of the unique Speh pairs, with multiplicity one, and \(m>1\) gives the residual part. [Mœglin–Waldspurger, *Le spectre résiduel de GL(n)*, théorème de l'introduction]; [Getz–Hahn, 22 April 2022 draft, Theorem 10.7.1]. The Eisenstein residues and their exhaustiveness are not constructed here.

For the modular-form example, the precise earlier \(GL_2/\mathbb Q\) dictionary is *Global Whittaker functions and the L-function of a cuspidal representation*, §6. The good-prime twist factors, recurrence, conductor-normalization constant and shift \(u\mapsto k-u\) are computed in §8.

## References

- W. Casselman, [*Canonical extensions of Harish-Chandra modules to representations of G*, publisher open-access edition](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/90CFF3C365389AA3AEE897611EC8DE2D/S0008414X00000523a.pdf/canonical-extensions-of-harish-chandra-modules-to-representations-of-g.pdf), 1989, §§5, 7–8, printed pp.407–409 and 414–423.
- J. Bernstein and B. Krötz, [*Smooth Fréchet globalizations of Harish-Chandra modules*, author version dated 3 August 2014](https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/Bern-Kroetz-2014.pdf), introduction and §5.1; §8, Theorem 8.1, and Appendix A, Theorems 12.2 and 12.8.
- H. Jacquet, I. I. Piatetski-Shapiro and J. A. Shalika, [*Automorphic forms on GL(3), I*, author-hosted edition](https://www.math.columbia.edu/~hj/Automorphic%20forms%20on%20GL%283%29%20I.pdf), 1979, §§3.1 and 4.3–4.5, printed pp.185–198.

- B. Rubin, [*Zeta integrals and integral geometry in the space of rectangular matrices*, arXiv:math/0406289](https://arxiv.org/pdf/math/0406289), Lemmas 2.7 and 4.2 and Theorem 4.3, for the real unsigned QR/Mellin and Fourier comparison.

- J. R. Getz and H. Hahn, [*An Introduction to Automorphic Representations, with a View toward Trace Formulae*, author draft of 22 April 2022](https://sites.duke.edu/jgetz/files/2022/04/Graduate_Text.pdf), §§10.5–10.7 and 11.3–11.8. All locators here refer to this freely accessible draft.
- W. Casselman and J. Shalika, [*The unramified principal series of p-adic groups. II. The Whittaker function*, freely accessible NUMDAM edition](https://www.numdam.org/item/CM_1980__41_2_207_0.pdf), 1980, Theorem 5.4, printed page 227.
- J. Bernstein and A. Zelevinsky, [*Representations of the group GL(n,F), where F is a non-archimedean local field*, author-hosted freely accessible paper](https://www.math.tau.ac.il/~bernstei/Publication_list/publication_texts/B-Zel-RepsGL-Usp.pdf), 1976, §§6–7, printed/PDF pages 52–60.
- D. Jiang, B. Sun and C.-B. Zhu, [*Vanishing of quasi-invariant generalized functions*, arXiv:1212.6015v1](https://arxiv.org/pdf/1212.6015v1), §4.2, printed/PDF pages 10–12.
- D. Goldfeld and H. Jacquet, [*Automorphic Representations and L-Functions for GL(n)*, author notes](https://www.math.columbia.edu/~goldfeld/LanglandsBookChapter.pdf), §§2–5, 8–9 and 11; Theorem 9.1 gives the standard cuspidal analytic theory.
- H. Jacquet and J. A. Shalika, [*On Euler Products and the Classification of Automorphic Representations I*, author-hosted paper](https://www.math.columbia.edu/~hj/On%20Euler%20products%20I.pdf), 1981.
- H. Jacquet, I. I. Piatetski-Shapiro and J. A. Shalika, [*Rankin–Selberg Convolutions*, author-hosted paper](https://www.math.columbia.edu/~hj/Rankin%20Selberg%20convolutions.pdf), 1983, especially §§2.7 and 9.4.
- C. Mœglin and J.-L. Waldspurger, [*Le spectre résiduel de GL(n)*, freely accessible paper](https://www.numdam.org/item/ASENS_1989_4_22_4_605_0/), 1989.
- F. Shahidi, [*On Nonvanishing of L-functions*, author-hosted paper](https://www.math.purdue.edu/~fshahidi/articles/Shahidi%20%5B1980,%203pp%5D---On%20nonvanishing%20of%20L-functions.pdf), 1980; the theorem announces boundary nonvanishing.
- P. Sarnak, [*Nonvanishing of L-functions on Re(s)=1*, author notes](https://web.math.princeton.edu/sarnak/ShalikaBday2002.pdf), §1; positivity and auxiliary self-pairing products.
