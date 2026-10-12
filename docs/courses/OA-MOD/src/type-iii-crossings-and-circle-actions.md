# Type III crossings and circle actions

This lesson proves an integer-action classification and its circle-action consequence. Throughout, von Neumann tensor products and isomorphisms are normal, and actions are continuous in the point-predual norm topology. Fix \(0<\lambda<1\), and put

\[
 L=-\log\lambda,\qquad P=\frac{2\pi}{L}.
\]

The factor \(M\) has separable predual and is injective of type \(\mathrm{III}_\lambda\). In particular the argument applies when \(M\) is approximately finite dimensional. We retain \(M\) itself in the answer, so a separate uniqueness theorem for type \(\mathrm{III}_\lambda\) factors is not an input.

The earlier aperiodic comparison lesson and modular-period lesson supply the two main tools. Additional proofs are linked where they enter the argument.

## The two statements and the model

Let \(R\) be the hyperfinite finite factor with normalized trace. On a tracial product presentation of \(R\), take matrix sizes \(d_j\geq2\), with every size occurring infinitely often, and define

\[
 a_j=\operatorname{diag}(\zeta_{d_j},\zeta_{d_j}^{\,2},
                  \ldots,\zeta_{d_j}^{\,d_j}),\qquad
 \sigma_0=\bigotimes_j\operatorname{Ad}a_j,\qquad
 \zeta_d=e^{2\pi i/d}.
\]

The trace GNS construction, normal extension, and product identifications are proved in Matrix eigenvectors and tensor absorption, Proposition 5.1. Write

\[
 K=R\rtimes_{\sigma_0}\mathbb Z,\qquad
 W x W^*=\sigma_0(x).
\]

We shall prove \(K\cong R\). Let \(\beta\) be its negative dual circle action:

\[
 \beta_z(x)=x\quad(x\in R),\qquad \beta_z(W)=\overline z\,W
 \quad(z\in\mathbb T).
\]

This convention agrees with the normal double-duality theorem used below.

**Integer classification.** For \(\alpha\in\operatorname{Aut}(M)\), the following are equivalent:

1. \(M\rtimes_\alpha\mathbb Z\) is a factor of type \(\mathrm{III}_\lambda\).
2. There are a normal isomorphism \(F:M\to M\overline\otimes R\) and a unitary \(u\in M\overline\otimes R\) such that

\[
 \mathrm{id}_M\otimes\sigma_0
       =\operatorname{Ad}u\circ F\alpha F^{-1}.
 \tag{1}
\]

Moreover the crossing in (1) is isomorphic to \(M\). Its dual circle action is conjugate to \(\mathrm{id}_M\otimes\beta\) on \(M\overline\otimes K\).

**Circle classification.** If a continuous circle action \(a\) on \(M\) has \(M\rtimes_a\mathbb T\) a factor of type \(\mathrm{III}_\lambda\), then \(a\) is cocycle conjugate to \(\mathrm{id}_M\otimes\beta\). Explicitly, there are a strongly continuous unitary \(a\)-cocycle \(c_z\in M\) and a normal isomorphism \(\Psi:M\to M\overline\otimes K\) with

\[
 c_z a_z(c_w)=c_{zw},\qquad
 \Psi\circ\operatorname{Ad}c_z\circ a_z\circ\Psi^{-1}
       =\mathrm{id}_M\otimes\beta_z.
 \tag{2}
\]

After any fixed trace-preserving identification \(K\cong R\), this is a circle action on \(M\overline\otimes R\).

Here an automorphism is centrally trivial if it acts identically on bounded central sequences, modulo strong-star null sequences. Its asymptotic period \(p_a\) is the least positive power that is centrally trivial, or \(0\) if there is no such power. Inner automorphisms are centrally trivial. The ordinary-sequence and asymptotic-centralizer formulations, including their separability hypotheses, are those proved in the prerequisites of OA-MOD-AC.

## A hyperfinite semifinite discrete core

The complete discrete decomposition proof, DDP Sections 2 and 4 supplies a faithful normal semifinite generalized trace \(\varphi\), of infinite mass, with

\[
 \begin{gathered}
 N=M_\varphi,\quad \tau=\varphi|_N,\quad
 M=N\rtimes_\theta\mathbb Z,\quad UxU^*=\theta(x),\\
 \tau\circ\theta=\lambda\tau,\qquad
 \varphi=\tau\circ E_N,\qquad
 \sigma_t^\varphi(x)=x,\quad
 \sigma_t^\varphi(U)=\lambda^{it}U,\\
 \operatorname{Per}(\varphi)=T(M)=P\mathbb Z .
 \end{gathered}
 \tag{3}
\]

Here \(N\) is a semifinite factor of type \(\mathrm{II}_\infty\). The equality for \(T(M)\) is the inner-period conclusion of DDP Section 2, not an inference from the displayed periods alone. That section proves it by showing that any inner implementer of a modular automorphism belongs to the factorial centralizer and is scalar there. Its weight independence follows from the normalized balanced-weight cocycle.

Averaging the periodic modular action over one period is a normal conditional expectation onto \(N\). Thus \(N\) is injective: compose any unital completely positive retraction onto \(M\) with that expectation. Injectivity passes to a finite corner by the entrywise and corner constructions in Averaging crossed products and injectivity, Proposition 1.1. Each nonzero finite corner \(pNp\), with its normalized trace, is therefore \(R\), by the full small-corner proof, Theorem 4.1.

For clarity, the passage from this finite corner to \(N\) needs a filling family. Choose infinitely many mutually orthogonal projections \(p_i\sim p\). They can be selected recursively: the complement of finitely many has infinite trace, and factor comparison places another copy of \(p\) there. Put \(q=\sum_i p_i\). Splitting the family into odd and even terms, and summing the equivalences term by term, shows that \(q\) is properly infinite. The projections \(q\) and \(1\) have the same central support and are countably decomposable. The complete projection comparison proof, PC Sections 2 and 7 gives \(q\sim1\). Transporting the \(p_i\)'s through that equivalence gives a family filling \(1\).

Choose coherent partial isometries from its first member to the others. Matrix coefficients then identify \(N\) normally with \(pNp\overline\otimes B(\ell^2)\): multiplication is matrix multiplication on finite corners, and the coefficient arrays and their inverse are bounded and normal on the whole algebra by CA Section 0. Consequently

\[
 N\cong R_\infty:=R\overline\otimes B(\ell^2).
 \tag{4}
\]

Separability passes to \(N\) and its corners. The interleaving of two infinite dyadic products gives \(R\overline\otimes R\cong R\), hence \(R_\infty\) is strongly stable.

The finite-corner comparison and trace assertions used here are the semifinite projection arguments in Trace scaling on the hyperfinite semifinite factor, Section 3. Approximately finite dimensional \(M\)'s satisfy the injectivity hypothesis by the written increasing-algebra argument in Averaging crossed products and injectivity, Proposition 5.1 and Corollary 5.2.

## Stability and the semifinite automorphism facts

We use the following two conclusions with their exact domains:

\[
 \operatorname{Ct}(R_\infty)=\operatorname{Inn}(R_\infty),
 \qquad
 \tau\eta=\tau\ \Longrightarrow\
 \eta\in\overline{\operatorname{Inn}(R_\infty)}.
 \tag{5}
\]

These are Trace scaling on the hyperfinite semifinite factor, Theorem 4.2 and Proposition 5.1. The closure is in point-predual norm. Their proofs include the type-I amplification identification of asymptotic centralizers, the centrally trivial commutator argument, the approximately inner flip, and the nonzero-slice proof that an inner tensor automorphism has inner factors. For the second assertion the proof first matches finite projections, then all their matrix units, reducing the action to an automorphism of \(R\) tensored with the identity. Its finite-factor approximation is Hyperfinite finite factors, Theorem 6.3. In particular (5) does not assert that a trace-scaling automorphism is approximately inner.

Since \(\tau\theta^k=\lambda^k\tau\), no nonzero power of \(\theta\) is inner. By (5), \(p_a(\theta)=0\). The identity-model case of Matrix eigenvectors and tensor absorption, Theorem 6.1 now gives an outer conjugacy between \(\theta\) and \(\theta\otimes\mathrm{id}_R\). Its assumptions hold on the strongly stable \(R_\infty\). In that theorem the identity model has index \(1\), which divides \(0\). Only this identity model is needed here.

The normal crossed-product transport in OA-MOD-AC-07 gives

\[
 M\cong(N\overline\otimes R)
                   \rtimes_{\theta\otimes\mathrm{id}}\mathbb Z
   \cong (N\rtimes_\theta\mathbb Z)\overline\otimes R
   =M\overline\otimes R .
 \tag{6}
\]

The second map is a normal isomorphism, not just a map on polynomials. In the regular representation it is the Hilbert-space regrouping

\[
 \ell^2(\mathbb Z,H_N\otimes H_R)
             \cong\ell^2(\mathbb Z,H_N)\otimes H_R.
\]

The coefficient \(\theta^{-n}(x)\otimes y\) becomes the regular coefficient of \(x\) tensored with \(y\), and the shift becomes the shift tensored with \(1\). These generate both algebras; the unitary implements the inverse as well. This also intertwines the coefficient expectations and both signs of the dual action. Thus every \(M\) under consideration is strongly stable, proved before using the aperiodic comparison theorem on \(M\).

## Normalizing an arbitrary automorphism

Let \(\alpha\) be arbitrary. Apply the full generalized-trace comparison in DDP Section 7 to \(\varphi\) and \(\psi=\varphi\circ\alpha^{-1}\). It gives a unitary \(b\in M\) and a scalar \(\mu\) with

\[
 \lambda<\mu\leq1,\qquad
 \varphi\circ\operatorname{Ad}b=\mu\psi.
\]

Therefore \(\alpha_1=\operatorname{Ad}b\circ\alpha\) satisfies

\[
 \varphi\circ\alpha_1=\mu\varphi.
 \tag{7}
\]

Modular covariance and the scalar normalization of the balanced derivative show that \(\alpha_1\) commutes with \(\sigma^\varphi\). It preserves \(N\), and (3) makes \(\alpha_1(U)U^*\) a unitary \(v\) in \(N\).

The full trace-scaling coboundary theorem DDP Section 6, applied to \(\tau\theta=\lambda\tau\), supplies \(w\in\mathcal U(N)\) with

\[
 v=w^*\theta(w).
\]

Set \(\gamma=\operatorname{Ad}w\circ\alpha_1\). Since \(w\) is in the centralizer it preserves the whole weight under conjugation. Also

\[
 \gamma(U)=w v U w^*
           =w v\theta(w^*)U=U.
\]

Thus

\[
 \gamma|_N=\eta,\qquad
 \eta\theta=\theta\eta,\qquad
 \tau\eta=\mu\tau,\qquad
 \varphi\gamma=\mu\varphi .
 \tag{8}
\]

This proves the required normalization for an arbitrary automorphism. In particular it is not an extra hypothesis in the classification.

Both inner changes give normal, dual-equivariant isomorphisms of integer crossings by OA-MOD-AC-07. They preserve the factoriality and type of the crossing. They also preserve approximate innerness and the absence of centrally trivial powers: approximate inner automorphisms form a subgroup, and the induced automorphism on the asymptotic centralizer is unchanged by an inner factor.

## The period condition forces approximate innerness

Assume \(Q=M\rtimes_\alpha\mathbb Z\) is a factor of type \(\mathrm{III}_\lambda\), and replace \(\alpha\) by \(\gamma\) as in (8). The factoriality criterion OA-MOD-MPR-02 shows that all nonzero powers of \(\gamma\) are outer.

DDP Section 2, applied to the factor \(Q\), gives \(T(Q)=P\mathbb Z\). For the dual weight \(\widetilde\varphi=\varphi\circ E_M\), OA-MOD-MPR-04 gives, with \(VxV^*=\gamma(x)\),

\[
 \sigma_t^{\widetilde\varphi}(V)=\mu^{it}V.
\]

In particular the sign is positive under the convention \(\varphi\gamma=\mu\varphi\). The actual-period intersection theorem OA-MOD-MPR-06, using \(\sigma_P^\varphi=\mathrm{id}\) and \(P\in T(Q)\), implies \(\mu^{iP}=1\). Hence \(\mu=\lambda^k\) for an integer \(k\), and the normalization \(\lambda<\mu\leq1\) forces

\[
 \mu=1.
 \tag{9}
\]

It follows from (5) that \(\eta\) is approximately inner on \(N\).

Approximate innerness on the centralizer alone is not yet approximate innerness on \(M\). Here the commuting relation in (8) is essential. Apply Central sequences and the module circle, Lemma 3.2 to \(N\), \(\theta\), and \(\eta\): \(N\) is strongly stable with separable predual, \(p_a(\theta)=0\), and \(\eta\) is approximately inner and commutes with \(\theta\). It supplies ordinary unitaries \(w_n\in N\) with

\[
 \operatorname{Ad}w_n\longrightarrow\eta
       \text{ in point-predual norm},\qquad
 \theta(w_n)-w_n\longrightarrow0
       \text{ strongly-star}.
 \tag{10}
\]

That proof corrects the central defect of an initial implementing sequence by central cocycle vanishing, and makes a joint ordinary-coordinate choice; it does not infer ordinary convergence from a single ultrafilter limit.

Lemma 3.1 in the same lesson then extends (10) to

\[
 \operatorname{Ad}w_n\longrightarrow\gamma
                       \quad\hbox{on }M .
 \tag{11}
\]

Its proof checks the norm-dense coefficient functionals
\(\rho\circ E_N(\,\cdot\,U^{-k})\), for \(\rho\in N_*\), and controls both adjoints of the moving coefficient \(w_n\theta^k(w_n^*)-1\). This is the exact extension result needed here. Consequently \(\alpha\), as well as \(\gamma\), is approximately inner.

## No centrally trivial positive power

Suppose, seeking a contradiction, that \(\gamma^p\) is centrally trivial for some integer \(p>0\). We first prove that \(\eta^p\) must be inner; no classification of all centrally trivial automorphisms of \(M\) is assumed.

Consider the commuting \(\mathbb Z^2\)-action on \(N\)

\[
 b_{(n,m)}=\eta^{pn}\theta^m.
\]

By (5) its centrally trivial kernel is its inner kernel, say \(H\). An inner automorphism preserves \(\tau\), whereas

\[
 \tau b_{(n,m)}=\lambda^m\tau.
\]

Thus \(H\subset\mathbb Z\times\{0\}\). If \(\eta^p\) were outer, \(H=d\mathbb Z\times\{0\}\) with either \(d=0\) (the zero subgroup) or \(d\geq2\). Choose \(z\in\mathbb T\setminus\{1\}\) with \(z^d=1\) when \(d\geq2\); for \(d=0\) take \(z=-1\). The character

\[
 \chi(n,m)=z^n
\]

is trivial on \(H\).

The full relative character eigenunitary theorem, Theorem 4.1 applies to this countable abelian action on the strongly stable factor \(N\). It gives a unitary \(X\in N_\omega\) such that

\[
 \theta_\omega(X)=X,\qquad
 (\eta^p)_\omega(X)=zX .
 \tag{12}
\]

The theorem's Gaussian construction, amenable projection towers, and exact original-coordinate diagonal are written out in that lesson and in Gaussian models and amenable towers, Sections 1–7.

The coefficient inclusion induces an injective equivariant map

\[
 (N_\omega)^{\theta_\omega}\longrightarrow M_\omega.
 \tag{13}
\]

This is the consequence (2.8)–(2.9) of Theorem 2.1 in Central sequences and the module circle. Its proof uses the full predual Fourier tests, and the faithful state \(\rho\circ E_N\) restricts to the same null-sequence seminorm as \(\rho\) on \(N\), proving injectivity. Therefore the nonzero unitary in (12) would give a central sequence class in \(M_\omega\) moved by \(\gamma^p\). This contradicts central triviality. We conclude \(\eta^p=\operatorname{Ad}v\) for a unitary \(v\in N\).

Commutation with \(\theta\), and factoriality of \(N\), give \(\theta(v)=c v\) for \(c\in\mathbb T\). Now

\[
 \operatorname{Ad}(v^*)\gamma^p|_N=\mathrm{id},
 \qquad
 \operatorname{Ad}(v^*)\gamma^p(U)
       =v^*\theta(v)U=cU.
\]

Choose \(s\in\mathbb R\) with \(\lambda^{is}=c\). The generator formulas (3) show

\[
 \gamma^p=\operatorname{Ad}v\circ\sigma_s^\varphi .
 \tag{14}
\]

But \(\gamma\) preserves \(\varphi\), and

\[
 T(M\rtimes_\gamma\mathbb Z)=P\mathbb Z
                         =\operatorname{Per}(\varphi).
\]

OA-MOD-MPR-07 excludes every return (14): its proof produces an inner modular time \(ps\) with a nonzero implementing Fourier degree \(p^2\), whereas a time in \(\operatorname{Per}(\varphi)\) can only have degree zero. The root of unity in the implementing unitary is removed in that proof before the degree argument is used.

This contradiction proves \(p_a(\gamma)=0\). Since inner perturbations induce the same automorphism of the asymptotic centralizer, \(p_a(\alpha)=0\) as well.

## Comparison and the full integer classification

The action \(\delta=\mathrm{id}_M\otimes\sigma_0\) is approximately inner: the finite-factor implementers for \(\sigma_0\), tensored with \(1\), converge on product normal functionals and hence on the full predual by their norm density.

Also \(p_a(\delta)=0\). For any nonzero integer \(k\), choose a size \(d\) not dividing \(k\), and move an entry \(e_{12}\) through the infinitely many size-\(d\) tensor positions of \(R\). These entries are bounded central sequences: they commute with finite tensor heads, and head-supported normal functionals are norm dense. Their displacement under \(\sigma_0^k\) has constant trace \(2\)-norm

\[
 \frac{|\zeta_d^{-k}-1|}{\sqrt d}>0.
\]

The tensors \(1\otimes e_{12}\) are central for all normal product functionals on \(M\overline\otimes R\), hence for its whole predual. The product of any faithful state on \(M\) with the trace detects that same nonzero displacement. This proves the assertion without assuming an identification of the entire tensor asymptotic centralizer.

Choose an isomorphism \(h:M\to M\overline\otimes R\) from (6). The automorphisms \(h\alpha h^{-1}\) and \(\delta\) act on the same strongly stable factor with separable predual. Both are approximately inner and have asymptotic period zero by Sections 5–6. The full aperiodic comparison theorem OA-MOD-AC-06 therefore gives (1), after composing its conjugating automorphism with \(h\).

OA-MOD-AC-07 supplies the normal isomorphism of crossings on their entire von Neumann algebras:

\[
 x\longmapsto F(x),\qquad V\longmapsto u^*W',
 \tag{15}
\]

where \(W'\) implements \(\delta\). The equation \(\delta=\operatorname{Ad}u\circ F\alpha F^{-1}\) verifies the orientation \(u^*W'\). This map intertwines the negative dual circle actions. The regular tensor regrouping from Section 3 then gives

\[
 M\rtimes_\alpha\mathbb Z
       \cong M\overline\otimes
                    (R\rtimes_{\sigma_0}\mathbb Z)
       =M\overline\otimes K,
 \tag{16}
\]

with dual action \(\mathrm{id}_M\otimes\beta\).

To identify \(K\), the preceding moving-entry argument already shows that all nonzero powers of \(\sigma_0\) are outer. OA-MOD-MPR-02 makes \(K\) a factor. The dual weight of the normalized trace is \(\tau_R\circ E_R\), a faithful normal state; its modular group fixes both \(R\) and \(W\), since \(\sigma_0\) preserves the trace. The full dual-weight formula OA-MOD-MPR-04, equivalently GDW7, therefore makes it a trace. The diffuse subalgebra \(R\) rules out a finite-dimensional type-I factor. Hence \(K\) is a finite factor of type \(\mathrm{II}_1\).

The integers are amenable: interval averages have translation errors tending to zero and a weak-star cluster point gives an invariant mean. The full amenable-crossing injectivity proof, Theorem 2.3 makes \(K\) injective. Its regular representation has separable Hilbert space, so its predual is separable. The small-corner Theorem 4.1 used in Section 2 gives \(K\cong R\). Equations (6) and (16) now yield \(M\rtimes_\alpha\mathbb Z\cong M\).

Conversely, (1), (15), and the normal regrouping give (16) without any type assumption on the crossing. Since \(K\cong R\) and \(M\overline\otimes R\cong M\), that crossing is a factor of type \(\mathrm{III}_\lambda\). This proves both directions of the integer classification and the additional dual-action assertion.

## Removing a type-I amplification with a cocycle

The following construction applies to more than circle actions.

**Proposition 8.1.** Let \(G\) be a topological group, let \(A\) be a properly infinite von Neumann algebra, and let \(a:G\to\operatorname{Aut}(A)\) be point-strong-star continuous. For every strongly continuous unitary representation \(r:G\to\mathcal U(\ell^2)\), there are a normal isomorphism \(\Pi:A\bar\otimes B(\ell^2)\to A\) and a strongly continuous unitary \(a\)-cocycle \(c\) such that
\(\Pi(a_z\otimes\operatorname{Ad}r_z)\Pi^{-1}=\operatorname{Ad}c_z\circ a_z\) for every \(z\in G\).
Neither separability of the predual nor local compactness of \(G\) is required. The scalar operator factor is countably infinite dimensional.

**Proof.** The filling construction CA Section 6 gives isometries \(s_i\in A\) with

\[
 s_i^*s_j=\delta_{ij}1,\qquad
 \sum_i s_i s_i^*=1,
\]

and the normal isomorphism

\[
 \Pi:A\overline\otimes B(\ell^2)\longrightarrow A,\qquad
 \Pi(x\otimes e_{ij})=s_i x s_j^*.
 \tag{17}
\]

It is implemented by the onto Hilbert-space row unitary; its inverse has entries \(s_i^*x s_j\). Thus the formula is justified on all bounded arrays, not just finite matrices.

Define

\[
 v_z=\sum_i s_i a_z(s_i^*).
 \tag{18}
\]

The summands are partial isometries with orthogonal initial projections \(a_z(s_i s_i^*)\) and orthogonal final projections \(s_i s_i^*\), both filling \(1\). Their strong-star sum is unitary. Multiplication of these orthogonal sums gives

\[
 v_z a_z(v_w)=
 \sum_{i,j}s_i a_z(s_i^*s_j)a_{zw}(s_j^*)
 =\sum_i s_i a_{zw}(s_i^*)=v_{zw}.
 \tag{19}
\]

Alternatively one may first multiply finite partial sums; bounded strong-star convergence justifies the limit.

This cocycle is strongly continuous. Let \(q_n=\sum_{i\leq n}s_i s_i^*\). The tail in (18), acting on a vector \(\xi\), has squared norm

\[
 \left\|\sum_{i>n}s_i a_z(s_i^*)\xi\right\|^2
       =\langle a_z(1-q_n)\xi,\xi\rangle.
\]

At any fixed \(z_0\) choose \(n\) making this small. Continuity of \(a_z(q_n)\) makes it small on a neighborhood of \(z_0\). The finite partial sum is strongly continuous there. This proves strong continuity of \(v_z\); unitarity implies strong continuity of the adjoints as well.

Put \(b_z=\Pi(a_z\otimes\mathrm{id})\Pi^{-1}\). On the generating entries in (17),

\[
 b_z=\operatorname{Ad}v_z\circ a_z.
 \tag{20}
\]

Let \(r_z\) be any strongly continuous unitary representation on \(\ell^2\), and put \(t_z=\Pi(1\otimes r_z)\). The action \(b\) fixes every \(t_w\). Therefore

\[
 c_z=t_zv_z
\]

is an \(a\)-cocycle: using \(v_z a_z(t_w)=t_wv_z\) and (19),

\[
 c_z a_z(c_w)=t_z t_w v_z a_z(v_w)
              =t_{zw}v_{zw}=c_{zw}.
\]

It is strongly continuous, and

\[
 \Pi(a_z\otimes\operatorname{Ad}r_z)\Pi^{-1}
             =\operatorname{Ad}c_z\circ a_z.
 \tag{21}
\]

This proves Proposition 8.1. Every calculation used only the group law, and the tail argument used continuity near an arbitrary group element. Taking \(G=\mathbb T\) gives the cocycle conjugacy needed below. The conclusion is cocycle conjugacy; no ordinary conjugacy between the original and amplified actions has been asserted. \(\square\)

## Double duality and the circle classification

Let \(a\) satisfy the circle hypothesis in Section 1, and set \(Q=M\rtimes_a\mathbb T\). Compact Haar averaging makes \(\mathbb T\) amenable, so the full amenable-crossing injectivity theorem used in Section 7 applies: \(Q\) is injective. A faithful normal representation of \(M\) can be chosen on a separable Hilbert space; the circle regular representation remains separable. Thus \(Q\) has separable predual. By assumption its type is \(\mathrm{III}_\lambda\).

Let \(\eta=\widehat a\) denote the negative dual integer action on \(Q\). The full normal double-duality theorem, ND statement and construction gives

\[
 Q\rtimes_\eta\mathbb Z
       \cong M\overline\otimes B(L^2(\mathbb T)),
 \qquad
 \widehat\eta_z\longleftrightarrow
                  a_z\otimes\operatorname{Ad}R_z,
 \tag{22}
\]

where \(R_zf(t)=f(tz)\). Both assertions concern the normal von Neumann algebras and continuous actions. The proof of ND includes the Weyl commutant argument, the bounded-array tensor transport, the partial Fourier transform, and the shear; the action formula is checked on each of the three types of generators.

Since \(M\) is properly infinite, (17) identifies the algebra on the right of (22) with \(M\). In particular \(Q\rtimes_\eta\mathbb Z\) is a factor of type \(\mathrm{III}_\lambda\). Apply the now-proved integer classification to the base \(Q\) and the automorphism \(\eta\). Its dual-equivariant conclusion is

\[
 (Q\rtimes_\eta\mathbb Z,\widehat\eta)
       \cong (Q\overline\otimes K,\mathrm{id}_Q\otimes\beta).
 \tag{23}
\]

Combining (22) and (23) gives an actual conjugacy between \(a\otimes\operatorname{Ad}R\) and \(\mathrm{id}_Q\otimes\beta\).

We must identify the base factors as well. Section 3, applied to \(Q\), gives \(Q\overline\otimes R\cong Q\). Since \(K\cong R\), equations (22)–(23), with (17), give

\[
 Q\cong Q\overline\otimes K
   \cong Q\rtimes_\eta\mathbb Z
   \cong M\overline\otimes B(L^2(\mathbb T))
   \cong M.
\]

Choose one resulting normal isomorphism \(J:Q\to M\). Composing the conjugacy (22)–(23) with \(J\otimes\mathrm{id}_K\) gives a normal isomorphism

\[
 H:M\overline\otimes B(L^2(\mathbb T))
          \longrightarrow M\overline\otimes K
\]

intertwining \(a_z\otimes\operatorname{Ad}R_z\) with \(\mathrm{id}_M\otimes\beta_z\). This argument does not invoke uniqueness of all injective type \(\mathrm{III}_\lambda\) factors.

Finally choose a Hilbert-space identification \(L^2(\mathbb T)\cong\ell^2\), use (17) on \(M\), and construct \(c_z\) by Section 8 for the representation \(R_z\). Set \(\Psi=H\Pi^{-1}\). Equation (21) gives exactly (2). The cocycle is strongly continuous, has the correct multiplication order, and lies in the original algebra \(M\). The circle classification is proved.

## Checks, solved exercises, and scope

**Exercise 1: the scaling sign.** Suppose \(\varphi\gamma=\mu\varphi\). What is the phase on the crossing unitary at \(P\), and what changes if instead \(\varphi\gamma^{-1}=\mu\varphi\)?

**Solution.** The normalized derivative for the first convention is \(\mu^{it}1\), so the phase is \(\mu^{iP}\). In the second convention \(\varphi\gamma=\mu^{-1}\varphi\), so it is \(\mu^{-iP}\). Both yield the same period obstruction, but only the first sign matches (7)–(9).

**Exercise 2: separating a subgroup.** In Section 6 let \(H=3\mathbb Z\times\{0\}\). Give a character that separates \((1,0)\) from \(H\), and explain why a character on the second coordinate cannot do so.

**Solution.** Take \(\chi(n,m)=e^{2\pi in/3}\). It equals one on \(H\), but not on \((1,0)\). A character depending only on \(m\) equals one at \((1,0)\), so its eigenunitary would not contradict central triviality of \(\gamma^p\). The trace multiplier first confines the kernel to the first axis; the character then detects the remaining first-coordinate obstruction.

**Exercise 3: the crossing unitary.** Derive (15) from (1).

**Solution.** For \(x\in M\),

\[
 (u^*W')F(x)(u^*W')^*
    =u^*\delta(F(x))u=F(\alpha(x)).
\]

Its negative dual phase is \(\overline z\), since \(u\) belongs to the coefficient algebra. Choosing \(uW'\) would not satisfy this calculation in general. Normal extension and the inverse are supplied by the regular-representation proof in OA-MOD-AC-07.

**Exercise 4: the cocycle order.** Why is \(t_zv_z\) the cocycle in Section 8, and why can one not simply declare the unitaries \(v_zt_z\) to work?

**Solution.** The known fixedness is for \(b_z=\operatorname{Ad}v_z a_z\), giving \(v_z a_z(t_w)=t_wv_z\). It makes
\((t_zv_z)a_z(t_wv_w)=t_z t_wv_z a_z(v_w)\).
It supplies no corresponding commutation for \(v_zt_z\). Moreover conjugating first by \(v_z\), then by \(t_z\), gives the product \(t_zv_z\), exactly as required by (21).

**Exercise 5: the duality sign on the circle.** With \(Q_n f(t)=t^{-n}f(t)\), verify the bidual phase in (22).

**Solution.** Since \(R_z^*f(t)=f(tz^{-1})\),

\[
 R_zQ_nR_z^*f(t)=(tz)^{-n}f(t)
              =\overline z^{\,n}Q_n f(t).
\]

The right translations, rather than their inverses, therefore implement the negative bidual convention. On the coefficient field \(t\mapsto a_{t^{-1}}(x)\), the extra coefficient action \(a_z\) cancels the translation: \(a_z a_{(tz)^{-1}}(x)=a_{t^{-1}}(x)\).

**Reference.** Masamichi Takesaki, *Theory of Operator Algebras III*, Chapter XVIII, Lemma 4.18(i)–(ii), printed pp.390–391. The classifications above use the given injective factor \(M\). They take the usual \(R_\lambda\) form after a chosen normal identification \(M\cong R_\lambda\); a separate classification of all such underlying factors is not part of this argument.
