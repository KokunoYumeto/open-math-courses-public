# Narrow modular spectra and projection displacement



Scalar averaging by the centralizer of a dominant weight yields operators of small modular frequency that move a prescribed vector. We prove the weight approximation, matrix-column passage, selfadjoint reduction and projection extraction with their constants. The dominant-weight averaging property is a hypothesis throughout; the proof does not assume the conclusion that the bicentralizer is trivial.

The exact earlier inputs are commuting weight approximation, IAP3–5, faithful dominant-weight uniqueness from pointwise scalar absorption, DS5, full matrix tensor weights and their modular action, TW2 and TW4–5, and properly infinite filling families and type III projection comparison, PC5 and PC8. We also use the faithful-state polar and modular identities, FS04 and FS09, spectral powers and step approximation, SK07–08, strong integration and the Gaussian Fourier calculation, MA02–03, and the real spectral projection transfer, SCV01–02.

Let \(M\) be a type \(\mathrm{III}_1\) factor with separable predual, acting in standard form \((M,H,J,P)\). Inner products are linear in the first variable and \(\eta a=Ja^*J\eta\). A weight means a faithful normal semifinite weight on the entire positive cone. Infinite multiplicity means that its centralizer is properly infinite. A dominant weight has infinite multiplicity and is unitarily equivalent to each of its positive scalar multiples. The earlier DS5 proves that any two faithful dominant weights on this algebra are unitarily equivalent, retaining equality also at infinite values.

Our hypothesis is the following property for one dominant weight \(\Phi\):

\[
 \overline{\operatorname{co}}^{\,uw}
 \{u^*xu:u\in\mathcal U(M_\Phi)\}\cap\mathbb C1\ne\varnothing
 \qquad(x\in M).
 \tag{MSD.1}
\]

Dominant-weight uniqueness transports this property to every dominant weight. Indeed the implementing inner automorphism carries the two centralizers, their unitary groups and ultraweak convex hulls onto one another. The same argument transports the property under a normal star isomorphism of algebras. Replacing every unitary by its adjoint makes the displayed convention identical to conjugation in the opposite direction.

## What a narrow modular spectrum controls

For a modular action \(\alpha_t=\sigma_t^\rho\), define its spectral subspace \(M_\rho(r)\), \(r>0\), by the tests

\[
 a\in M_\rho(r)
 \quad\Longleftrightarrow\quad
 \int_{\mathbb R}f(t)\alpha_t(a)\,dt=0
 \text{ whenever } f\in L^1(\mathbb R),\quad
 \mathcal F_+f(s):=\int e^{its}f(t)\,dt=0\ (|s|\le r).
 \tag{MSD.2}
\]

The integral is ultraweak, obtained by testing the bounded orbit on the predual as in MA02. Its norm is at most \(\|f\|_1\|a\|\). These are precisely the spectral-support tests for the closed interval \([-r,r]\). Adjoints preserve this subspace: conjugate the integral and use \(\mathcal F_+(\overline f)(s)=\overline{\mathcal F_+f(-s)}\). Normal equivariant coefficient maps preserve it for the same reason.

Let \(\varphi\) be a faithful normal state, with positive cyclic separating unit vector \(\xi\) and modular operator \(\Delta\). If \(a\in M_\varphi(r)\), then the spectral measure of \(\log\Delta\) on \(a\xi\) is supported in \([-r,r]\). To justify the localization, for \(\chi\in C_c^\infty(\mathbb R)\) supported outside that interval put

\[
 f(t)=\frac1{2\pi}\int e^{-its}\chi(s)\,ds.
\]

Two integrations by parts bound \(|f(t)|\) by a constant times \((1+|t|)^{-2}\), so \(f\in L^1\). The Gaussian calculation MA03 gives

\[
 \int e^{its}e^{-\varepsilon t^2}f(t)\,dt
 =\frac1{\sqrt{4\pi\varepsilon}}
       \int e^{-(s-q)^2/(4\varepsilon)}\chi(q)\,dq.
\]

Fubini is justified by the Gaussian factor and integrability of \(\chi\). The right side tends to \(\chi(s)\): split near \(s\), using continuity, and away from \(s\), using the vanishing Gaussian tails. Dominated convergence by \(|f|\) on the left proves \(\mathcal F_+f=\chi\).

FS09 gives \(\alpha_t(a)\xi=\Delta^{it}a\xi\). The spectral integral and (MSD.2) therefore yield \(\chi(\log\Delta)a\xi=0\). Choose nonnegative such functions positive on a countable collection of relatively compact intervals covering \(\mathbb R\setminus[-r,r]\). Their squared spectral integrals show zero measure outside the interval. SK07 then gives

\[
 \|a\xi-\xi a\|
 =\|(1-\Delta^{1/2})a\xi\|
 \le(e^{r/2}-1)\|a\xi\|.
 \tag{MSD.3}
\]

The identity \(\Delta^{1/2}a\xi=Ja^*\xi=\xi a\) includes its domain, by FS04. For \(0<r\le1\), \(e^{r/2}-1\le r\). For example the derivative of \(r+1-e^{r/2}\) is positive on \([0,1]\), since \(e^{1/2}<2\); the latter follows from the exponential series bounded by the geometric series. Consequently, if \(a_i\in M_\varphi(r)\) and \(\sum_i a_i^*a_i=1\) strongly, then

\[
 \sum_i\|[a_i,\xi]\|^2\le r^2,
 \qquad \sum_i\|a_i\zeta\|^2=\|\zeta\|^2\quad(\zeta\in H).
 \tag{MSD.4}
\]

The second identity is obtained from finite partial sums and strong convergence; the first follows termwise from (MSD.3).

## Dominant averaging inside a narrow spectral interval

For every weight \(\rho\) of infinite multiplicity, \(x\in M\), and \(r>0\),

\[
 \overline{\operatorname{co}}^{\,uw}
 \{u^*xu:u\in\mathcal U(M)\cap M_\rho(r)\}
       \cap\mathbb C1\ne\varnothing.
 \tag{MSD.5}
\]

IAP3–5 supplies a bounded selfadjoint \(h\in M_\rho\), with \(\|h\|<r/2\), such that

\[
 \rho_h(y)=\rho(e^{h/2}ye^{h/2})
\]

is dominant. The same proved centralizer perturbation gives
\(\sigma_t^{\rho_h}=\operatorname{Ad}(e^{ith})\sigma_t^\rho\).
For \(u\in\mathcal U(M_{\rho_h})\), this means

\[
 \sigma_t^\rho(u)=e^{-ith}ue^{ith}.
 \tag{MSD.6}
\]

We verify its spectral support without inferring it merely from an entire extension. SK08 gives finite spectral step sums \(h_n=\sum_j\lambda_{nj}p_{nj}\to h\) in norm, with all \(\lambda_{nj}\in[-\|h\|,\|h\|]\). For these sums,

\[
 e^{-ith_n}ue^{ith_n}
 =\sum_{j,k}e^{it(\lambda_{nk}-\lambda_{nj})}p_{nj}up_{nk}.
\]

Every frequency lies in \([-2\|h\|,2\|h\|]\subset[-r,r]\). Hence each tested integral in (MSD.2) vanishes for this finite sum. For every real \(t\) the sum converges in norm to the right side of (MSD.6). The difference is bounded by \(2\|u\|\), so scalar dominated convergence of its norm against \(|f|\) passes the vanishing integral to the limit. Thus \(u\in M_\rho(r)\). Apply (MSD.1) to the dominant \(\rho_h\); its centralizer unitaries are contained in the set in (MSD.5), proving the assertion.

## A unitary column gives a displacement family

Let \(\varphi\) be a faithful normal state, \(\xi=\xi_\varphi\), and \(x\in M\) satisfy \(\varphi(x)=0\). For every \(r>0\) there is a sequence \((a_i)\subset M_\varphi(r)\) with

\[
 \sum_i a_i^*a_i=1,\qquad
 \sum_i\|(xa_i-a_ix)\xi\|^2\ge\tfrac12\|x\xi\|^2.
 \tag{MSD.7}
\]

If \(x=0\), take \(a_1=1\) and the other entries zero. Otherwise work in \(\widetilde M=M\bar\otimes B(\ell^2)\), with \(\rho=\varphi\otimes\operatorname{Tr}\). TW2 constructs this faithful normal semifinite weight, and TW4–5 gives its complete GNS space and modular action
\(\sigma_t^\rho=\sigma_t^\varphi\otimes\operatorname{id}\).
In particular its centralizer contains \(1\otimes B(\ell^2)\), so it has infinite multiplicity.

The filling isometries of PC5 identify \(\widetilde M\) normally with \(M\). Explicitly, choose \(s_i^*s_j=\delta_{ij}1\), \(\sum_i s_is_i^*=1\); the map \((\zeta_i)\mapsto\sum_i s_i\zeta_i\) is an onto unitary from \(\ell^2(H)\) to \(H\). Its conjugation takes an array \([y_{ij}]\) to \(\sum_{ij}s_i y_{ij}s_j^*\), with inverse array \([s_i^*ys_j]\). Finite-coordinate computation and bounded strong limits give the complete normal isomorphism. Transporting (MSD.1) therefore permits (MSD.5) on \(\widetilde M\).

For \(X=x\otimes1\), obtain a scalar \(\lambda1\) in that convex closure. In the tensor GNS space use \(\Gamma=\xi\otimes e_{11}\), where \(e_{11}\) has Hilbert–Schmidt norm one. The map \(Y\mapsto Y\Gamma\) is ultraweak-to-weak continuous on bounded sets, by normality of the representation. A norm ball is weakly closed; consequently

\[
 \|(X-\lambda)\Gamma\|
 \le\sup_{u\in\mathcal U(\widetilde M)\cap\widetilde M_\rho(r)}
        \|(X-u^*Xu)\Gamma\|
 =\sup_u\|[X,u]\Gamma\|.
\]

Since \(\varphi(x)=0\), the square of the left side is
\(\|x\xi\|^2+|\lambda|^2\), at least \(\|x\xi\|^2>0\).
Choose one \(u\) with \(\|[X,u]\Gamma\|^2\ge\|x\xi\|^2/2\), and set \(a_i=u_{i1}\). Its column has \(\sum_i a_i^*a_i=1\) strongly, by the \((1,1)\) coefficient of \(u^*u=1\). Equivariant normal coefficient maps put every \(a_i\) in \(M_\varphi(r)\). TW4's column action gives

\[
 [X,u]\Gamma=\sum_i(xa_i-a_ix)\xi\otimes e_{i1}
\]

in Hilbert norm. Squaring the norm in this orthogonal sum proves (MSD.7).

## From a column to a single operator

Let \(\xi\in P\) be a cyclic separating unit vector, and let \(\eta\in H\) be a \(J\)-real unit vector perpendicular to \(\xi\). For every \(\delta>0\) there is an operator \(a\) with

\[
 \|a\xi\|^2+\|a\eta\|^2<8\|[a,\eta]\|^2,
 \qquad \|[a,\xi]\|^2<\delta\|[a,\eta]\|^2.
 \tag{MSD.8}
\]

Put \(\varphi=\omega_\xi\), \(\psi=\omega_\eta\), and \(\delta_0=\min(\delta,1)\). We distinguish whether \(\psi\) is dominated by a finite multiple of \(\varphi\).

If \(\psi\le K\varphi\), increase \(K\) to at least one. The map \(c':b\xi\mapsto b\eta\) is well-defined and bounded by \(\sqrt K\), since \(\|b\eta\|^2\le K\|b\xi\|^2\). Cyclicity extends it to \(H\), and its defining formula makes it commute with each \(b\in M\); hence \(c'\in M'\). Set \(x=Jc'J\in M\). Then \(\|x\|\le\sqrt K\), \(x\xi=\eta\), and \(\varphi(x)=0\), using \(J\eta=\eta\).

Take the family (MSD.7) at

\[
 r=\min\left(\sqrt{\delta_0/8},\frac1{\sqrt{128K}}\right)<1.
\]

By (MSD.4), the summed squared reference commutators are at most \(r^2\), while the sum of the two mass terms is exactly two. The identity
\([a_i,\eta]=[a_i,x]\xi+x[a_i,\xi]\)
and the triangle inequality in the Hilbert direct sum give

\[
 \left(\sum_i\|[a_i,\eta]\|^2\right)^{1/2}
 \ge\frac1{\sqrt2}-\sqrt K\,r
 \ge\frac7{8\sqrt2}.
\]

Thus

\[
 \sum_i\left(\|a_i\xi\|^2+\|a_i\eta\|^2
             +\frac8{\delta_0}\|[a_i,\xi]\|^2\right)
 \le3<\frac{49}{16}
 \le8\sum_i\|[a_i,\eta]\|^2.
\]

Both sides are finite: for the last sum use the displayed commutator identity and \(\sum_i\|[a_i,x]\xi\|^2\le2\sum_i\|a_i\eta\|^2+2\|x\|^2\sum_i\|a_i\xi\|^2\). Hence at least one index satisfies the strict termwise inequality. Its \(a_i\) gives (MSD.8), with \(\delta_0\le\delta\).

If no such finite \(K\) exists, some projection \(p\) has
\(\psi(p)>(16/\delta_0)\varphi(p)\).
Indeed the contrary inequality on all projections extends first to positive spectral step sums, then by uniform approximation to every bounded positive element, giving the excluded functional domination. Split \(p\) into seventeen nonzero orthogonal projections, using repeated proper-infinite splitting. At least one, call it \(q\), has \(\psi(q)\le\psi(p)/17<\psi(p)/16\). PC8 gives a partial isometry \(v\) with \(v^*v=p-q\), \(vv^*=q\). Since \(J\eta=\eta\),

\[
 \|v\eta\|^2=\psi(p-q),\qquad
 \|\eta v\|^2=\|v^*\eta\|^2=\psi(q).
\]

The reverse triangle inequality yields

\[
 D:=\|[v,\eta]\|
 \ge\frac{\sqrt{15}-1}{4}\sqrt{\psi(p)}
 >\tfrac12\sqrt{\psi(p)}.
\]

On the other hand,

\[
 \|v\xi\|^2+\|v\eta\|^2
 \le\varphi(p)+\psi(p)<\tfrac{17}{16}\psi(p)<8D^2,
\]

and \(\|[v,\xi]\|^2\le2\varphi(p)<\delta_0\psi(p)/8<\delta_0D^2\). The estimate for \(\xi\) uses \(J\xi=\xi\) and \(v^*v+vv^*=p\). Thus \(a=v\) proves (MSD.8) also in this case; no faithful-state assumption is imposed on \(\psi\).

## A selfadjoint witness

Under the preceding vector hypotheses, for every \(\delta>0\) there is \(b=b^*\) such that

\[
 \|b\xi\|^2+\|b\eta\|^2<32\|[b,\eta]\|^2,
 \qquad\|[b,\xi]\|^2<\delta\|[b,\eta]\|^2.
 \tag{MSD.9}
\]

Choose (MSD.8) at tolerance \(\min(\delta,1)/4\), write \(D=\|[a,\eta]\|>0\), and put \(S(a)=\|a\xi\|^2+\|a\eta\|^2\). For either \(J\)-real vector \(\zeta\),
\(\|[a^*,\zeta]\|=\|[a,\zeta]\|\), because \(J[a,\zeta]=-[a^*,\zeta]\). Also
\(\|a^*\zeta\|=\|\zeta a\|\le\|a\zeta\|+\|[a,\zeta]\|\).
Squaring with \((s+t)^2\le2s^2+2t^2\) therefore gives

\[
 S(a^*)\le2S(a)+2\|[a,\xi]\|^2+2D^2<20D^2.
\]

Let \(b=(a+a^*)/2\), \(c=(a-a^*)/(2i)\). The parallelogram identity yields

\[
 S(b)+S(c)=\tfrac12(S(a)+S(a^*))<14D^2,
\]


\[
 \|[b,\eta]\|^2+\|[c,\eta]\|^2=D^2,
 \qquad
 \|[b,\xi]\|^2+\|[c,\xi]\|^2=\|[a,\xi]\|^2.
\]

Consequently

\[
 \sum_{z=b,c}\left(S(z)+\frac{32}{\delta}\|[z,\xi]\|^2\right)
 <22D^2<32\sum_{z=b,c}\|[z,\eta]\|^2.
\]

One of these two selfadjoint operators satisfies the strict termwise inequality. Relabel it as \(b\); discarding each of its nonnegative summands proves (MSD.9).

## Extracting the projection with the full premise proved

For the same \(\xi,\eta\) and any \(\delta>0\), there is a nonzero projection \(p\) with

\[
 \|p\xi\|^2+\|p\eta\|^2<128\|[p,\eta]\|^2,
 \qquad\|[p,\xi]\|^2<\delta\|[p,\eta]\|^2.
 \tag{MSD.10}
\]

Apply (MSD.9) with tolerance \(\delta^2/(64\cdot32)\). Its witness satisfies both premises of SCV02 with \(K=32\). The fully proved real spectral transfer in that earlier lesson gives (MSD.10) immediately. Both the existence premise and the projection selection are therefore supplied; the assertion here is stronger than the conditional transfer alone. The strict inequality excludes the zero projection.

These are the complete claims of Takesaki, *Theory of Operator Algebras III*, XVIII.3, Lemmas 3.8–3.11 and 3.13, printed pp.334–339 and 342–343. Lemma 3.12's spectral integration was proved separately in SCV01. All vector hypotheses, infinite-multiplicity and separable-predual restrictions are retained. The integration weight used for the projection is \(|\lambda|\), with the corrected first power established in SCV01–02. The later passage from local projections to an exhaustive partition and a uniform displacement bound requires an additional argument.
