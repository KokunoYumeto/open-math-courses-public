# Radial phase and solenoidal potential

The formulas below use the conventions in OpenAI, [*Finite Time Blowup for Navier–Stokes*](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf), pages 90–93, equations (8.4)–(8.14). The full definitions and proofs are in [Radial primitives and the complete mean equations](src/radial-primitives-and-the-mean-equations.md), RP1–RP6.

For fixed axial coordinate and time, the auxiliary coordinate changes along a radial path by
\[
Y'=Y+((r')^{d_r}-r^{d_r})v_r.
\]
The covering matrix satisfies \(J_gv_r=\Lambda_gv_r\). Applying \(J_g^{i_0}\) and substituting \(r=\sqrt Q R\), \(r'=\sqrt Q R'\), with \(Q>0\), gives
\[
y'=y+\Lambda_g^{i_0}Q^{d_r/2}((R')^{d_r}-R^{d_r})v_r,
\qquad M=\Lambda_g^{i_0}Q^{d_r/2}.
\]
Both radial powers contribute the factor \(Q^{d_r/2}\). RP2 also proves the exact comparison with the distinct scale \(\widetilde M=\Lambda_g^{i_0}Q^{d_r}/2\), including the different inverse estimates.

The compact radial primitive \(\mathcal I_c\) defined in RP3 gives the azimuthal potential
\[
\Psi=r^{-1}\mathcal I_c(r\gamma_{d,\mathrm{phys}}),
\qquad \mathcal A=\Psi e_\theta.
\]
The cylindrical basis has \(e_\theta=(-x_2/r,x_1/r,0)\). Thus
\[
\mathcal A=(-x_2,x_1,0)\frac{\Psi}{r},\qquad
\operatorname{curl}\mathcal A
=-\partial_z\Psi\,e_r+(\partial_r+r^{-1})\Psi\,e_z.
\]
For example, the third curl component is
\[
\partial_{x_1}(x_1\Psi/r)+\partial_{x_2}(x_2\Psi/r)
=2\Psi/r+r\partial_r(\Psi/r)=\partial_r\Psi+\Psi/r.
\]
The first two curl components are \(-x_1\partial_z\Psi/r\) and \(-x_2\partial_z\Psi/r\). Their radial component is therefore \(-\partial_z\Psi\). On the active shell, where the radial derivative includes the stated auxiliary-coordinate evaluation, RP5 gives the full physical velocity increments and their viscosity factors. The primitive and its cutoff vanish near the axis, so this cylindrical expression has the smooth Cartesian extension proved there.
