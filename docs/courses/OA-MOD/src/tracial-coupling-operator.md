# Compatible traces and the coupling operator

Original exposition and solved examples: GPT-6.1 Sol (OpenAI), Ultra, October 2026; CC0-1.0. This lesson proves the classical statement of Takesaki, *Theory of Operator Algebras II*, IX.3.14, pp. 197–198, using the course's spatial construction and the programme's existing finite-algebra and coupling-function providers. No new research result is asserted.

## The theorem and its precise prerequisites

Let \(M\subseteq B(H)\) be a finite von Neumann algebra whose commutant \(N=M'\) is finite. Let \(\tau\) and \(\psi\) be faithful normal tracial states on \(M\) and \(N\), respectively. Their common center is \(Z=M\cap N\). Assume

\[
 \tau(z)=\psi(z)\quad(z\in Z).
 \tag{CO.1}
\]

Then, on the original represented Hilbert space,

\[
 \frac{d\tau}{d\psi}=c_M.
 \tag{CO.2}
\]

Here \(c_M\) is the positive injective self-adjoint operator affiliated with \(Z\) that represents the canonical coupling function. Neither this operator nor its inverse is assumed bounded. Equality in (CO.2) includes their full operator domains. The existence of the two states implies that these algebras have faithful normal states; it imposes no separability assumption on \(H\).

We recall the normalization of the coupling function to prevent a reciprocal ambiguity. Write \(T_M,T_N\) for the normalized center-valued traces. For \(\xi\in H\), let

\[
 \begin{aligned}
 p_\xi&=s(\omega_\xi|_M)=[N\xi]\in M,\\
 q_\xi&=s(\omega_\xi|_N)=[M\xi]\in N.
 \end{aligned}
 \tag{CO.3}
\]

Brackets mean the projection onto the indicated closed cyclic subspace. Its commutation with the acting algebra puts it in the other algebra by the bicommutant theorem. It fixes \(\xi\), and every projection of that other algebra fixing \(\xi\) contains the cyclic subspace. This proves both minimality and the support formula. The coupling normalization is

\[
 \begin{gathered}
T_M(p_\xi)=c_M T_N(q_\xi)\\
(\xi\in H).
\end{gathered}
 \tag{CO.4}
\]

Unbounded central products in this lesson mean their closed spectral products. In (CO.4) that product is bounded because it equals the bounded left side.

The existing [programme multiplicity lesson](https://kokunoyumeto.github.io/open-math-courses-public/courses/traces-and-noncommutative-integration/multiplicity-of-a-von-neumann-algebra-on-a-hilbert-space.html#oa-fnd-mu-17), Theorem 10.2 and Definition 10.3, owns the general existence and uniqueness of this coupling function. The source convention is Takesaki I, V.3.8–3.9, p. 339. The [projection lesson](https://kokunoyumeto.github.io/open-math-courses-public/courses/foundations-of-von-neumann-algebras/projections-and-types-of-von-neumann-algebras.html#oa-fnd-ty-18), Theorem 14.1, supplies finite joins. The trace lesson, Lemma 1.5 and Theorems 5.2 and 5.5, supplies full-corner center identifications and the canonical center-valued trace with its uniqueness. These are attributed programme proofs by Claude Opus 5.5 (Anthropic), September 2026, with the multiplicity lesson revised October 2026, CC0. This application retains their ownership and declared antecedents.

Within OA-MOD we use Conventions and exact inputs through The opposite weight and its modular data, Every finite rectangular intertwiner has a vector through The relative map has exactly the coefficient form and The nonfaithful relative map and its full graph core for bounded module vectors, the first-column linking construction and the closed relative map; The trace pairing fills the whole predual for unique positive predual densities; and Complete norms on actual measurable operators through Bounded strong convergence acts on each integrable vector and The Hilbert space behind the trace for concrete measurable \(L^p\), products, bounded strong convergence and tracial \(L^2\). The measurable closure and polar calculus are Closed graphs detected outside small defects through Adjoint, addition and multiplication keep the domains, and full spectral domains are Changes of variable, powers, and actual ranges. The complete application below does not prove these inputs or their prerequisites.

## Place both trace densities in the correct corners

Put \(K=H_\psi\), the tracial GNS space of \(N\). In the faithful linking algebra of SI-06 set

\[
 \begin{aligned}
R&=\operatorname{End}_N(K\oplus H),\\
eRe&=B=\pi_\psi(N)\prime,\\
fRf&=M,\\
e+f&=1,\qquad ef=0.
\end{aligned}
 \tag{CO.5}
\]

The two module representations of \(N\) are faithful, so \(e,f\) both have full central support in \(R\). The algebra \(B\) is anti-isomorphic to \(N\) through \(j_\psi(y)=J_\psi\pi_\psi(y^*)J_\psi\). Its trace \(\chi=\psi^{\mathrm{opp}}\) satisfies \(\chi(j_\psi(y))=\psi(y)\). Both corners are finite, hence \(e,f\) are finite projections; the programme finite-join theorem makes \(1=e+f\) finite. Thus \(R\) is finite.

Identify \(Z(R)\) with \(Z\) by its full \(f\)-corner. The corresponding \(e\)-corner identification is the same one transported through the original \(N\)-module action. This follows from the linking bicommutant: its central elements have the form \(\pi_\psi(z)\oplus z\), \(z\in Z\). Let \(T_R\) be the canonical normalized center-valued trace. The formula

\[
 \omega(x)=\tfrac12\{\chi(exe)+\tau(fxf)\}
 \tag{CO.6}
\]

defines a faithful normal state on \(R\). For a positive \(x\), vanishing of both corner terms gives \(x^{1/2}e=x^{1/2}f=0\), hence \(x=0\). Therefore \(\nu_0=\omega|_{Z(R)}\) is faithful, and

\[
 \rho_0=\nu_0\circ T_R
 \tag{CO.7}
\]

is a faithful normal tracial state on \(R\). We have constructed a scalar trace instead of silently assuming that the linking algebra is countably decomposable.

Apply the positive density theorem TI-06 in each finite corner with the restricted trace \(\rho_0\). Traciality forces each density to commute with every corner unitary: conjugating a density represents the same functional, so uniqueness gives equality. Its spectral projections therefore belong to the corner center. Faithfulness gives full support. The full-corner center isomorphisms lift these densities to positive injective operators \(a,b\) affiliated with \(Z(R)\), with

\[
 \begin{aligned}
\tau(y)&=\rho_0(ay),\\
&\quad y\in(fRf)_+,\\
\chi(x)&=\rho_0(bx),\\
&\quad x\in(eRe)_+.
\end{aligned}
 \tag{CO.8}
\]

Thus the numerator density is \(af\) and the reference density is \(be\). Their integrals are both one. The globally lifted \(a,b\) need not themselves be integrable on all of \(R\). They are finite on increasing central spectral cutoffs; no bounded density or bounded inverse is assumed.

For the faithful normal weight \(\rho=\chi\oplus\tau\) on \(R\), put \(d=be+af\). This is its positive integrable density relative to \(\rho_0\), with \(\rho_0(d)=2\). Although \(a,b\) are central, \(d\) need not be central in \(R\). The GNS map

\[
 U\Lambda_\rho(x)=x d^{1/2}
 \quad(x\in R)
 \tag{CO.9}
\]

is isometric into the actual measurable-operator space \(L^2(R,\rho_0)\): bounded cyclicity and TI-10 give

\[
 \|x d^{1/2}\|_2^2=\rho_0(d x^*x)=\rho(x^*x).
\]

It is onto. Indeed, \(k_n=1_{[1/n,n]}(d)\uparrow1\). For bounded \(y\in R\),

\[
 yk_n=(yk_n d^{-1/2})d^{1/2}
 \tag{CO.10}
\]

is in the range because the parenthesized factor is bounded. TI-11 gives \(yk_n\to y\) in \(L^2\), and TI-09 says that bounded elements are dense there. The range of the completed isometry is closed and contains a dense set, proving surjectivity.

The SI-06 first-column unitary followed by \(U\) restricts to an onto unitary

\[
 W:H\longrightarrow fL^2(R,\rho_0)e.
 \tag{CO.11}
\]

It carries the original \(M\)-action to left multiplication and the original \(N\)-action to right multiplication by \(j_\psi(N)\). To see the right action on all vectors, the first-corner algebra commutes with \(d\); multiplication on \(x d^{1/2}\) consequently agrees with its GNS first-column action. Both actions are bounded, so the identity extends from the dense first-column vectors to the entire rectangular \(L^2\) space. No auxiliary identification of only the bounded-vector subset has replaced the original representation.

## Identify the entire closed relative map

Under \(W\), the initial bounded-module-vector domain \(D_\psi\) of SI-01 and SI-04 is exactly

\[
 \begin{aligned}
W(D_\psi)&=\{x b^{1/2}:\\
&\qquad x\in fRe\}.
\end{aligned}
 \tag{CO.12}
\]

Here \(x\) is the bounded intertwiner coefficient. Since \(\tau\) is finite, every such coefficient has finite second-corner energy. Thus the smaller finite-energy domain \(E_{\tau,\psi}\) equals \(D_\psi\). The initial conjugate-linear relative map, expressed in the two rectangular \(L^2\) corners, is

\[
 \begin{gathered}
T_0(xb^{1/2})=x^*a^{1/2}\\
{}\in eL^2(R,\rho_0)f.
\end{gathered}
 \tag{CO.13}
\]

This is the first-column Tomita map of SI-06 and SI-10 through (CO.9); both expressions are \(L^2\) vectors by (CO.8).

Define the positive central operators

\[
 c=ab^{-1},\qquad h=c^{1/2}.
 \tag{CO.14}
\]

They are well-defined by joint central spectral calculus, with full support. On the rectangular Hilbert space let \(J_0\xi=\xi^*\), the onto antiunitary to the opposite corner supplied by TI-15. The measurable-algebra identities and centrality give

\[
 \begin{gathered}
hxb^{1/2}=xa^{1/2},\\
T_0=J_0h\big|_{W(D_\psi)}.
\end{gathered}
 \tag{CO.15}
\]

In particular the initial vectors lie in the actual Hilbert-space domain of \(h\). For a direct domain check, use the joint cutoffs \(z_n\) of (CO.16). Then \(z_nxb^{1/2}\to xb^{1/2}\) and \(hz_nxb^{1/2}=z_nxa^{1/2}\to xa^{1/2}\) in \(L^2\), by TI-11. Closedness of the spectral operator \(h\) proves both membership and the asserted value. This does not assert an ordinary everywhere-defined product of unbounded factors.

We now prove that (CO.12) is a graph core. Set

\[
 \begin{aligned}
 z_n={}&1_{[1/n,n]}(a)\,1_{[1/n,n]}(b)\\
      &\cdot1_{[1/n,n]}(c).
 \end{aligned}
 \tag{CO.16}
\]

These commuting central projections increase to one. For each \(\xi\in D(h)\), scalar spectral integration gives

\[
 \begin{gathered}
z_n\xi\to\xi,\\
hz_n\xi\to h\xi\quad\hbox{in }L^2.
\end{gathered}
 \tag{CO.17}
\]

Fix \(n\). Since \(R\) is dense in \(L^2\), bounded rectangular elements \(v\in fRe\) approximate \(z_n\xi\); compressing the approximants by \(z_n\) preserves that convergence. On this central corner, \(\|hz_n\|\leq\sqrt n\), and

\[
 \begin{gathered}
z_nv=xb^{1/2},\\
x=z_nv b^{-1/2}\in fRe.
\end{gathered}
 \tag{CO.18}
\]

Consequently the same approximation has graph-norm error at most \((1+n)^{1/2}\) times its \(L^2\) error. Choose one sufficiently accurate approximant for each \(n\), then use (CO.17). Every vector of \(D(h)\) is obtained in graph norm from (CO.12). This argument uses a sequence of spectral cutoffs of these particular operators, not a separable algebra or a countable basis of \(H\).

It follows that the closure of the initial map is exactly \(T=J_0h\), with domain \(D(h)\). Taking its conjugate-linear adjoint and squared modulus gives

\[
 \begin{gathered}
W\frac{d\tau}{d\psi}W^*=T^*T=c,\\
D(T^*T)=D(c).
\end{gathered}
 \tag{CO.19}
\]

Indeed \(T^*=hJ_0^{-1}\), so \(T^*T=h^2\) on precisely the spectral domain of \(h^2\). For the scalar spectral measure \(\mu_\xi\) of the central \(c\) at a vector \(\xi\), the two domains are

\[
 \begin{gathered}
 D(c)=\{\xi:\\
 \int_0^\infty t^2\,d\mu_\xi(t)<\infty\},\\
 D(c^{1/2})=\{\xi:\\
 \int_0^\infty t\,d\mu_\xi(t)<\infty\}.
 \end{gathered}
 \tag{CO.20}
\]

This establishes full closed-operator equality, rather than an equality of quadratic forms on a possibly proper initial domain.

## Compare with the canonical coupling function

Put \(t_e=T_R(e)\), \(t_f=T_R(f)\). They are bounded positive central operators, sum to one and have support one: if a central projection annihilated either value, faithfulness would make it annihilate that full corner. The canonical traces of the two corners, identified with \(Z(R)\), satisfy

\[
 \begin{aligned}
T_B(x)&=\frac{T_R(x)}{t_e},\\
T_M(y)&=\frac{T_R(y)}{t_f}.
\end{aligned}
 \tag{CO.21}
\]

For positive \(x\in eRe\), \(0\leq T_R(x)\leq\|x\|t_e\), so the quotient defines a bounded positive map with value one at \(e\). It is tracial, center-linear and normal. For normality, test its increasing bounded positive nets after central cutoffs where \(t_e^{-1}\) is bounded, then let those cutoffs increase to one. The same reasoning applies to \(f\). The programme trace uniqueness theorem identifies these maps with the canonical center-valued traces. Transport through \(j_\psi\) identifies \(T_B\) with \(T_N\); an anti-isomorphism also preserves the positive tracial identities, as in programme Lemma 10.1.

Take an arbitrary vector \(\xi\in H\), and write its actual measurable polar decomposition

\[
 \begin{gathered}
v=W\xi=u|v|\\
{}\in fL^2(R,\rho_0)e.
\end{gathered}
 \tag{CO.22}
\]

Its bounded polar partial isometry lies in \(fRe\). Put \(p=uu^*\in fRf\) and \(q=u^*u\in eRe\). The projection \(p\) is the smallest left-corner projection fixing \(v\): \(p_0v=v\) implies \(p_0u=u\) on the range closure of \(|v|\), hence \(p\leq p_0\). The converse follows from the polar factorization. Applying this argument to \(v^*\) shows that \(q\) is the smallest right-corner projection fixing \(v\). These facts concern every \(L^2\) vector. With (CO.3) and the full action identities of (CO.11),

\[
 p=p_\xi,\qquad q=j_\psi(q_\xi).
 \tag{CO.23}
\]

Traciality gives \(T_R(p)=T_R(q)\). Applying (CO.21) yields

\[
 \begin{gathered}
T_M(p_\xi)=\frac{t_e}{t_f}T_N(q_\xi)\\
(\xi\in H).
\end{gathered}
 \tag{CO.24}
\]

One may read this first on cutoffs where \(t_e/t_f\) is bounded and then as the closed central product. Its bounded value is \(T_M(p_\xi)\). Thus the existing programme coupling-function characterization and uniqueness give

\[
 c_M=t_e t_f^{-1}.
 \tag{CO.25}
\]

This computes the canonical coupling operator in our linking representation; its general foundational existence theorem remains with the programme provider.

Now use the hypothesis that the scalar traces agree on \(Z\). For \(z\in Z_+\), (CO.7)–(CO.8) imply

\[
 \begin{aligned}
 \tau(z)&=\nu_0(a t_f z),\\
 \psi(z)&=\nu_0(b t_e z).
 \end{aligned}
 \tag{CO.26}
\]

For unbounded \(a,b\), these formulas follow by monotone central cutoffs. Both positive central densities \(a t_f,b t_e\) are integrable of mass one. Equality on every \(z\) and the unique positive density theorem in the commutative algebra give

\[
 \begin{gathered}
a t_f=b t_e,\\
ab^{-1}=t_e t_f^{-1}=c_M.
\end{gathered}
 \tag{CO.27}
\]

Combining (CO.19) and (CO.27) proves (CO.2), including (CO.20) on the original Hilbert space. All divisions and cancellations can first be made on joint central cutoffs with bounded inverses, then extended by spectral uniqueness.

For comparison, if the faithful tracial states do not agree on the center, the same calculation gives

\[
 \begin{aligned}
 r&=\frac{d(\tau|_Z)}{d(\psi|_Z)}
    =\frac{a t_f}{b t_e},\\
 \frac{d\tau}{d\psi}&=r c_M.
 \end{aligned}
 \tag{CO.28}
\]

The commutative Radon–Nikodym derivative here is a positive injective affiliated operator, supplied by the same central density theorem. This formula isolates the role of (CO.1); it does not remove that hypothesis from (CO.2).

**Source comparison.** Takesaki II IX.3.14, p. 198, initially attaches the numerator density to \(e\) and the opposite reference density to \(f\). Those labels are interchanged relative to the preceding definitions: the numerator is on \(fRf\), and the reference is on \(eRe\). The later printed calculation uses the correctly typed order. Equations (CO.8)–(CO.13) keep that order throughout.

## A complete rectangular matrix calculation

Let \(H=\operatorname{HS}(\mathbb C^n,\mathbb C^m)\) with its unnormalized Hilbert–Schmidt norm. Let \(M=M_m(\mathbb C)\) act on the left and \(N\) be the right multiplications by \(M_n(\mathbb C)\). Its multiplication is opposite matrix multiplication. Use

\[
 \begin{aligned}
\tau&=\operatorname{Tr}_m/m,\\
\psi(r_y)&=\operatorname{Tr}_n(y)/n.
\end{aligned}
 \tag{CO.29}
\]

These tracial states agree on the scalar center. Identify \(H_\psi\) with \(\operatorname{HS}(\mathbb C^n)\) by \(\Lambda_\psi(r_y)=y/\sqrt n\). The bounded-vector operator of SI-01 is then

\[
 \begin{aligned}
R_\psi(\xi)\eta&=\sqrt n\,\xi\eta,\\
\theta_\psi(\xi)&=n\xi\xi^*.
\end{aligned}
 \tag{CO.30}
\]

Every vector is bounded here. Its spatial energy is

\[
 \tau(\theta_\psi(\xi))
   =\frac nm\|\xi\|_{\mathrm{HS}}^2.
 \tag{CO.31}
\]

Polarization therefore gives \(d\tau/d\psi=(n/m)I_H\). The linking algebra is \(M_{n+m}\). Relative to \(\rho_0=\operatorname{Tr}_{n+m}/(n+m)\), the two corner densities and trace values are

\[
 \begin{aligned}
b&=(n+m)/n,\\
a&=(n+m)/m,\\
t_e&=n/(n+m),\\
t_f&=m/(n+m).
\end{aligned}
 \tag{CO.32}
\]

Thus \(a/b=t_e/t_f=n/m\), while the closed relative map has modulus \(\sqrt{n/m}\,I_H\). The derivative is its squared modulus.

If \(\xi\) has rank \(k\), its two support projections have ranks \(k\) in the left and right corners. Consequently

\[
 \begin{aligned}
T_M(p_\xi)&=k/m\\
&=(n/m)(k/n)\\
&=c_M T_N(q_\xi).
\end{aligned}
 \tag{CO.33}
\]

This verifies the canonical coupling normalization independently of the energy calculation. Exchanging the two algebras gives the reciprocal \(m/n\). When \(m=n\), the standard tracial bimodule has coupling one. All the initial, form and operator domains in this finite-dimensional example equal \(H\).

## Unbounded coupling and the center hypothesis

**An unbounded operator with unbounded reciprocal.** Index blocks by \(i=(k,\pm)\), \(k\geq1\), and set

\[
 \begin{gathered}
(m_{k,+},n_{k,+})=(1,k),\\
(m_{k,-},n_{k,-})=(k,1),\\
H=\bigoplus_i H_i,\\
H_i=\operatorname{HS}(\mathbb C^{n_i},\mathbb C^{m_i}).
\end{gathered}
 \tag{CO.34}
\]

Take the bounded product of the left matrix algebras for \(M\), and its right-matrix commutant for \(N\). Both are finite: an isometry in either product is unitary in every finite-dimensional block. Give block \(i=(k,\pm)\) the positive weight \(w_i=2^{-(k+1)}\). The sum over both signs is one. The sums of these weights times the normalized block traces define faithful normal tracial states \(\tau,\psi\) agreeing on the entire center \(\ell^\infty(\mathbb N\times\{+,-\})\).

The weighted GNS block of \(N\) is represented by \(\Lambda_\psi(r_y)_i=\sqrt{w_i/n_i}\,y_i\). Hence

\[
 \begin{gathered}
\xi\in D_\psi\quad\Longleftrightarrow\\
\sup_i\sqrt{n_i/w_i}\,\|\xi_i\|_{\mathrm{op}}<\infty,\\
\tau(\theta_\psi(\xi))\\
{}=\sum_i(n_i/m_i)\|\xi_i\|_{\mathrm{HS}}^2\\
(\xi\in D_\psi).
\end{gathered}
 \tag{CO.35}
\]

The first equivalence is the norm criterion for the block-diagonal bounded operator \(\eta_i\mapsto\sqrt{n_i/w_i}\,\xi_i\eta_i\); its operator norm equals the displayed supremum. For the energy formula, the positive left coefficient is \((n_i/w_i)\xi_i\xi_i^*\), and its normalized weighted trace cancels \(w_i\). This supplies both claims directly, including their constants.

Finite-block vectors lie in \(D_\psi\) and are dense in the form domain by truncation. Thus the closed derivative and its exact domains are

\[
 \begin{aligned}
A_{k,+}&=kI,\\
A_{k,-}&=k^{-1}I.
\end{aligned}
 \tag{CO.36}
\]

\[
 \begin{gathered}
D(A)=\{\xi\in H:\\
\sum_k\bigl[k^2\|\xi_{k,+}\|^2\\
{}+k^{-2}\|\xi_{k,-}\|^2\bigr]<\infty\},\\
D(A^{1/2})=\{\xi\in H:\\
\sum_k\bigl[k\|\xi_{k,+}\|^2\\
{}+k^{-1}\|\xi_{k,-}\|^2\bigr]<\infty\}.
\end{gathered}
 \tag{CO.37}
\]

For \(A^{-1}\) and its square root, exchange the plus and minus coefficients. Both operators are unbounded, although both algebras are finite and both states are normalized. There is no positive uniform lower bound for \(A\).

Let \(E_k\) be the first matrix unit of norm one in the plus block. The vector \(\xi_{k,+}=k^{-3/2}E_k\), \(\xi_{k,-}=0\), belongs to \(D(A^{1/2})\), since its energy sum is \(\sum k^{-2}<\infty\). It does not belong to \(D(A)\), whose sum is \(\sum k^{-1}\). Nor does it belong to \(D_\psi\), since \(\sqrt{k/w_{k,+}}\,k^{-3/2}\) is unbounded. Thus both inclusions

\[
 D_\psi\subsetneq D(A^{1/2})\subsetneq H
 \tag{CO.38}
\]

are strict: the second is witnessed by \(\eta_{k,+}=k^{-1}E_k\), whose Hilbert sum converges but whose energy sum diverges. Putting the same sequences in the minus blocks gives the corresponding distinctions for the reciprocal. Every closure and domain distinction in CO-03 is necessary even in this elementary example.

**Why agreement on the center is essential.** Let \(H=\mathbb C^2\) and \(M=N\) be the diagonal algebra. Its intrinsic coupling operator is one: both canonical center-valued traces are the identity and the two support projections of every vector coincide. Set

\[
 \begin{aligned}
 \tau(x)&=\tfrac34x_1+\tfrac14x_2,\\
 \psi(x)&=\tfrac14x_1+\tfrac34x_2.
 \end{aligned}
 \tag{CO.39}
\]

They are faithful tracial states with different central restrictions. The normalized GNS coordinates show \(\theta_\psi(\xi)_i=|\xi_i|^2/\psi_i\), so the energy is \(3|\xi_1|^2+\tfrac13|\xi_2|^2\). Therefore

\[
 \begin{aligned}
\frac{d\tau}{d\psi}&=\operatorname{diag}(3,1/3)\\
&=r c_M\ne c_M.
\end{aligned}
 \tag{CO.40}
\]

This is exactly (CO.28) on its full, finite-dimensional domain. It shows why traciality and normalization alone cannot replace (CO.1).

The proof of IX.3.14 is complete at the declared providers. The proofs of those providers are not given here.
