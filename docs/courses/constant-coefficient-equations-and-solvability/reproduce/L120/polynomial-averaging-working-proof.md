# Smooth averaging away from the zeros of a polynomial

*Written by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, October2026. Original exposition CC0.*

This is the exact finite-degree averaging receiver used in AN02-L004. Its construction is written below, rather than supplied by a reference to a private book. The ordinary scalar complex Taylor theorem for an entire function restricted to a complex line, elementary finite-dimensional compactness, smooth scalar cutoffs, and real Lebesgue integration/Fubini remain declared inputs. No general analytic functional theorem is assumed. No wider AN-01 assignment is transferred.

## PA036-1. The precise statement

Fix integers n>=1, m>=0 and rho>0. Let P_m be the complex polynomials on C^n of degree at most m. Use the Hermitian coefficient inner product, linear in the first variable,

\[
 \langle p,q\rangle_J=\sum_{|\alpha|\le m}
       \partial^\alpha p(0)\overline{\partial^\alpha q(0)},
 \qquad |q|_J^2=\langle q,q\rangle_J.\tag{PA1}
\]

There is a nonnegative real smooth function Phi(q,z) on (P_m minus0) times C^n, smooth in the real and imaginary coefficient coordinates, and a compact K contained in0<|z|<rho, such that

\[
 \operatorname{supp}_z\Phi(q,\cdot)\subset K,
 \quad \Phi(aq,z)=\Phi(q,z)\quad(a\in\mathbb C\setminus\{0\}),\tag{PA2}
\]
\[
 \int_{\mathbb C^n} H(z)\Phi(q,z)\,d\lambda(z)=H(0)
       \quad\text{for every entire holomorphic }H,\tag{PA3}
\]
\[
 |q(z)|\ge c|q|_J\quad\text{whenever }\Phi(q,z)>0,\tag{PA4}
\]

for one c>0 depending only on the fixed m,n,rho and the construction. In particular Phi has integral one. The assertion includes constant nonzero polynomials and coefficient families whose actual degree drops. It does not assert a single averaging density independent of q.

## PA036-2. Averaging under one simultaneous complex rotation

For any nonnegative compact smooth psi on C^n, supported away from0, with integral one and

\[
 \psi(e^{it}z)=\psi(z)\quad(t\in\mathbb R),\tag{PA5}
\]

equation PA3 holds with psi in place of Phi. Indeed the real map z->e^{it}z is orthogonal and has absolute determinant one. Change variables, then average t and apply Fubini. All integrands are bounded on the compact set of rotations of the support. For fixed z, the one-variable function w->H(wz) is entire. Its Taylor series converges uniformly on |w|=1. Integrating term by term kills every strictly positive Taylor power and leaves H(0). Consequently

\[
 \int H(z)\psi(z)\,d\lambda(z)
 =\int\psi(z)\left[\frac1{2\pi}\int_0^{2\pi}H(e^{it}z)\,dt\right]d\lambda(z)
 =H(0).\tag{PA6}
\]

Only simultaneous rotation of every complex coordinate is needed. Separate coordinate rotations, full radial symmetry, or invariance of q under rotations are not assumptions.

Here are explicit localized such densities. For a unit u in C^n, set d_u(v)=1-|<v,u>|^2 on the unit sphere. It is real smooth, nonnegative and invariant under v->e^{it}v. A smooth nonnegative bump b(d_u(v)), supported in a sufficiently small interval0<=d_u(v)<delta and positive near0, localizes near the phase orbit of u. Take a nonzero nonnegative radial bump a supported in an interval (r_-,r_+) with0<r_-<r_+<rho. Then

\[
 \psi(z)=Z^{-1}a(|z|)b\left(1-
               \frac{|\langle z,u\rangle|^2}{|z|^2}\right),
 \qquad Z=\int a(|z|)b\left(1-
               \frac{|\langle z,u\rangle|^2}{|z|^2}\right)d\lambda(z),\tag{PA7}
\]

extended by zero, is smooth on all of C^n. The radial support is separated from0 and has a compact margin before rho. The integral Z is finite and positive: for n>1 the bump is positive on a nonempty open annular set; for n=1 its angular argument is identically0 and the nonzero radial annulus has positive real two-dimensional measure. The bumps can be constructed from the scalar function exp(-1/t) for t>0, extended by zero for t<=0. Thus no partition of unity on an unproved projective manifold is required.

## PA036-3. A nonvanishing full circle for every nonzero polynomial

For any nonzero q0 with |q0|_J=1 there is a unit u such that the one-variable polynomial t->q0(tu) is not identically zero. Otherwise evaluating each such polynomial at the positive real number |z| would give q0(z)=0 for every z!=0; continuity also gives q0(0)=0, contradicting its nonzero coefficient norm. A nonzero one-variable polynomial of degree at most m has at most m roots: polynomial division at a root reduces degree by one, inductively.

Choose r in (rho/3,2rho/3) unequal to the modulus of any of those finitely many roots. Compactness of the phase circle gives

\[
 d_0=\min_{0\le t\le2\pi}|q_0(re^{it}u)|>0.\tag{PA8}
\]

There are closed radial and angular neighborhoods of that circle, still in0<|z|<rho, on which |q0(z)|>=d0/2. One direct justification is uniform continuity on a closed ball and the phase-orbit distance formula

\[
 \min_{|a|=1}|v-au|^2=2-2|\langle v,u\rangle|,
                  \quad |v|=|u|=1.\tag{PA9}
\]

The minimizing phase is explicit if the inner product is nonzero, and if it is zero every phase has the displayed distance. Choose radial support sufficiently close to r and angular parameter1-|<v,u>|^2 sufficiently small. Formula PA9 places every supported point sufficiently close to some point of the original circle. Use PA7 to obtain a phase-invariant normalized psi0 with support in that neighborhood. Therefore

\[
       |q_0(z)|\ge d_0/2\quad(z\in\operatorname{supp}\psi_0).\tag{PA10}
\]

The construction needs no continuous enumeration of polynomial roots and no constant actual degree.

## PA036-4. Stability under changes of coefficients and their phase

The exact finite Taylor expression and Cauchy--Schwarz give

\[
 |p(z)|\le B_\rho|p|_J,\quad |z|\le\rho,
 \qquad B_\rho=
 \left(\sum_{|\alpha|\le m}\frac{\rho^{2|\alpha|}}{(\alpha!)^2}\right)^{1/2}.\tag{PA11}
\]

For unit coefficient vectors p,q0 the same phase-distance formula holds in the J inner product. If

\[
 s_{q_0}(p)=1-|\langle p,q_0\rangle_J|^2<\delta,
 \quad 0<\delta<1,\tag{PA12}
\]

there is |a|=1 with |p-aq0|_J<=sqrt(2delta), since1-sqrt(1-delta)<=delta. Select delta so small that B_rho sqrt(2delta)<d0/4. On the full support of psi0, PA10--PA11 then give

\[
        |p(z)|\ge d_0/4.\tag{PA13}
\]

This neighborhood is invariant under multiplication of p by a unit scalar. The lower bound concerns the modulus of q; q itself need not have the same phase at different supported points.

## PA036-5. A finite smooth invariant coefficient partition

Apply PA036-3--4 to each point of the unit coefficient sphere. The open neighborhoods s_{q0}<delta/2 cover that compact sphere; a finite subcover yields q1,...,qJ, associated deltas delta_j, densities psi_j, and numbers d_j>0. Fix one smooth scalar function beta>=0 which is positive on [0,1/2] and zero on [1,infinity), for example beta(t)=exp(-1/(1-t)) for t<1 and0 for t>=1, restricted to t>=0. For arbitrary q!=0 define

\[
 b_j(q)=\beta\left(\frac{1-
 |\langle q,q_j\rangle_J|^2/|q|_J^2}{\delta_j}\right),
 \qquad h_j(q)=\frac{b_j(q)}{\sum_{\ell=1}^Jb_\ell(q)}.\tag{PA14}
\]

The denominator is positive because some member of the finite subcover has argument<1/2. Every b_j and h_j is real smooth for q!=0, nonnegative and unchanged by every nonzero complex scalar multiplying q. Their sum is one. If h_j(q)>0, then s_{q_j}(q/|q|_J)<delta_j, so PA13 applies. Set

\[
 \Phi(q,z)=\sum_{j=1}^Jh_j(q)\psi_j(z),
 \qquad K=\bigcup_{j=1}^J\operatorname{supp}\psi_j,
 \qquad c=\min_j d_j/4>0.\tag{PA15}
\]

The finite union K is compact in0<|z|<rho. Smoothness, positivity, invariance and common support are immediate from the explicit finite expression. Equation PA6 for each psi_j gives PA3. If Phi(q,z)>0, at least one positive term has h_j(q)>0 and psi_j(z)>0; its bound PA13 after restoring |q|_J gives PA4. This proves PA036-1 with every quantifier retained. The only compactness sphere is the fixed degree-at-most-m coefficient sphere, so lower-degree polynomials and degree-dropping families are included.

For n=0 the space is one point with its unit-mass zero-dimensional Lebesgue convention. Nonzero polynomials are constants. Phi(q,0)=1 gives the same averaging identity and bound with c=1, with K={0}. The additional assertion K separated from0 is specific to n>=1 and is not imposed at this endpoint.

## PA036-6. Division and coefficient derivatives

Define A(q,z)=Phi(q,z)/q(z) where q(z)!=0. Define it as zero near q(z)=0. This defines one smooth function: PA4 says Phi=0 on the open set |q(z)|<c|q|_J, so a whole neighborhood of every division zero is zero. All real coefficient derivatives retain common z-support K. For every j>=0 their multilinear operator norms are bounded on the compact product {|q|_J=1} times K. Off K all those derivatives are zero, because Phi is identically zero there for every q. Since A(tq,z)=t^(-1)A(q,z) for t>0, differentiating j times in real coefficient directions yields

\[
 |d^jA(q,z)[r_1,...,r_j]|
 \le C_j\frac{\prod_{\nu=1}^j|r_\nu|_J}{|q|_J^{j+1}}.\tag{PA16}
\]

This is exactly the denominator/differentiation receiver of L004 Lemma2.1, now supplied by the written averaging construction. It does not independently admit that lesson's full distributional family topology, convolution identities, or recursive Fourier/integration prerequisites.

## Human credit and exact retained scope

The current L004 receiver credits Lars Hormander's polynomial averaging method and the Malgrange--Ehrenpreis existence theorem. The historical reference is *On the existence and the regularity of solutions of linear pseudo-differential equations*, L'Enseignement Mathematique17(1971),99--163, [primary archive](https://www.e-periodica.ch/digbib/view?lang=en&pid=ens-001%3A1971%3A17%3A%3A213). The archive's title and volume were verified. Its chapter download returned a verification-required HTML page, so no original proof page or exact original lemma number is claimed inspected. The construction above uses its own finite rotation-invariant densities and explicit coefficient partition and requires no unavailable source proof. All actual declared scalar/Taylor/compactness/cutoff/integration inputs remain explicit. The full course remains unfinished.
