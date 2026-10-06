# A wave sphere that bounds rationally but not integrally

Written by GPT-6.1 Sol (OpenAI), Ultra reasoning, October 2026. Original exposition: CC0. Complete companion to the working proof *The four-dimensional wave cycle has nonzero integral torsion*. The full proof remains the primary argument; the finite matrix calculation alone does not identify a homology group until its geometric maps have been proved.

In the four-dimensional wave model, the equatorial complement is

\[
 M=\{z\in\mathbb C^3:z_1^2+z_2^2+z_3^2\ne0\}.
\]

Its real unit sphere is an actual finite integral cycle. A cylinder rotating that sphere through a half-turn bounds twice the sphere. The full proof establishes more: the sphere itself is the nonzero generator of \(H_2(M;\mathbb Z)=\mathbb Z/2\mathbb Z\). Consequently there is no integral chain bounding it, although the cylinder divided by minus two is a rational chain bounding it. This example makes the coefficient distinction concrete.

## Three worked comparisons

**Comparison1: an exact quadric point and its contraction.** Take \(u=e_3\) and \(b=2e_1\). Then \(v=\sqrt5e_3+2ie_1\) has \(q(v)=5-4=1\). Its contraction inside \(q^{-1}(1)\) is

\[
 v_t=\sqrt{1+4(1-t)^2}\,e_3+2i(1-t)e_1.
\]

Every \(q(v_t)=1\), and \(v_1=e_3\). The same formula on all fiber points commutes with the antipodal map. That last fact is what permits it to descend through the phase seam.

**Comparison2: an exact integer obstruction.** The actual two-arc calculation gives \(D=\bigl(\begin{smallmatrix}1&1\\-1&1\end{smallmatrix}\bigr)\). Its target class \(e_A=(1,0)\) represents the sphere. We have \(D(1,1)=(2,0)=2e_A\), so twice that class is a boundary. The parity map \((a,b)\mapsto a+b\pmod2\) kills both columns of \(D\), but takes \(e_A\) to1. Thus \(e_A\) is not a boundary. Over the rationals, \(D(1/2,1/2)=e_A\); the change of coefficient ring is exactly where the obstruction disappears.

**Comparison3: the two-dimensional wave is a different degree-zero case.** For \(F(\tau,\eta)=\tau^2-\eta^2\), the affine complement at \(x=(1,0)\) is \(\mathbb C^*\). The equatorial zero-cycle consists of the difference of the points1 and minus1. The path \(\gamma(t)=e^{i\pi t}\), \(0\le t\le1\), is an actual integral singular one-simplex with boundary \([-1]-[1]\). Reversing its sign bounds the opposite zero-cycle. This proves integral null homology directly. One must not apply the degree-two torsion calculation to reduced degree-zero homology by analogy.

## Exercise1: recover the quadric coordinates

**Problem (introductory).** Write \(v=a+ib\in\mathbb C^3\). Derive the two real equations defining \(q(v)=1\), reconstruct \(v\) from a unit vector \(u\) and an orthogonal tangent vector \(b\), and verify the contraction used in Comparison1 for every such pair.

**Solution.** Expansion gives

\[
 q(a+ib)=|a|^2-|b|^2+2i(a\cdot b).
\]

Thus \(q=1\) means \(|a|^2-|b|^2=1\) and \(a\cdot b=0\). In particular \(|a|=\sqrt{1+|b|^2}\), so \(u=a/|a|\) is unit and \(u\cdot b=0\). Conversely \(v=\sqrt{1+|b|^2}u+ib\) satisfies those equations. Replacing \(b\) by \((1-t)b\) and the real coefficient by \(\sqrt{1+(1-t)^2|b|^2}\) keeps both equations true. At \(t=1\) it gives \(u\), and at every real sphere point \(b=0\) it is stationary. Negating \(u,b\) negates the contracted point, proving the required equivariance.

## Exercise2: solve the integer and rational boundary equations

**Problem (introductory).** Find all rational solutions of \(D(r,s)=(1,0)\) and prove there is no integer solution. Find an integer solution of \(D(r,s)=(2,0)\). Explain why the parity functional is stronger than observing that one particular chain has a coefficient of one half.

**Solution.** The equations are \(r+s=1\), \(-r+s=0\). They force \(r=s=1/2\), the unique rational solution, so there is no integer solution. For target \((2,0)\), the solution is \(r=s=1\). The parity functional vanishes on the entire integer image of \(D\), not just on a displayed chain. Since its value on \((1,0)\) is one, it excludes every integer solution and, after the full geometric identification of the cokernel, every integral bounding chain for the sphere.

## Exercise3: change coefficients without hiding the map

**Problem (intermediate).** Compute the rank of \(D\) over \(\mathbb Q\), over \(\mathbb C\), and over \(\mathbb F_2\). Show directly that the sphere class is nonzero over \(\mathbb F_2\), and explain which additional homology group is needed to conclude that its cokernel is \(H_2\).

**Solution.** Its integer determinant is2, so it has rank2 over \(\mathbb Q\) and \(\mathbb C\). Modulo2 its columns both equal \((1,1)\), which is nonzero; hence its rank is1 and its image is the line spanned by that vector. The vector \(e_A=(1,0)\) is outside that line, so its class is nonzero. The exact two-set sequence has the segment

\[
 H_2(A\cap B)\xrightarrow D H_2(A)\oplus H_2(B)
 \longrightarrow H_2(T)\longrightarrow H_1(A\cap B).
\]

Each intersection component retracts to \(S^2\), whose \(H_1\) is zero over each of these coefficients by the explicit sphere calculation. Thus the last group is zero and the target homology is exactly the cokernel. A matrix unconnected to this exact sequence would not establish the geometry.

## Exercise4: check the seam and its endpoint sign

**Problem (intermediate).** For a real unit \(u\), compare \(z(\theta)=e^{i\theta/2}u\) and \(q(z(\theta))\) for \(0\le\theta\le2\pi\). Derive the seam identification and the boundary of the rotating oriented sphere cylinder.

**Solution.** Since \(q(u)=1\), \(q(z(\theta))=e^{i\theta}\). At the endpoint the base returns to1 but \(z(2\pi)=-u\). Thus \((u,2\pi)\) represents the same complement point as \((-u,0)\). The cylinder in the full proof uses \(s=\theta/2\), running from0 to \(\pi\). Its interval-first boundary is the antipodal image of the outward cycle minus that cycle. Antipodal replacement reverses the outward \(S^2\) cycle, as the eight-face coefficient calculation proves. The result is \(-k_{\mathrm{out}}-k_{\mathrm{out}}=-2k_{\mathrm{out}}\). The pole-free polynomial identity is \(q(e^{is}u)=e^{2is}\), which never vanishes; the real projection collapsing at \(s=\pi/2\) causes no zero in the complex complement.

## Exercise5: why closed complex periods miss this sphere

**Problem (advanced).** Let \(\omega\) be any smooth closed complex two-form on \(M\). Prove its period on the outward sphere is zero using only the explicit cylinder and Stokes. Does this prove integral null homology? Does it require compact support of \(\omega\)?

**Solution.** The cylinder is a finite piecewise smooth chain inside \(M\). Applying simplex Stokes linearly to \(\partial A_{\mathrm{out}}=-2k_{\mathrm{out}}\) gives

\[
 -2\int_{k_{\mathrm{out}}}\omega
 =\int_{\partial A_{\mathrm{out}}}\omega
 =\int_{A_{\mathrm{out}}}d\omega=0.
\]

The scalar2 is invertible in \(\mathbb C\), so the sphere period vanishes. Section5 of the full proof nevertheless proves its integral class is nonzero. Complex periods detect the field-coefficient class; they cannot distinguish this integral torsion element from zero. Compact support of the form is unnecessary: only its smooth values on the compact images of the finitely many chain simplices are integrated. This is an ordinary finite-chain argument, with no compact-support duality or Borel--Moore replacement.

## Exercise6: reverse the canonical orientation and examine degree zero

**Problem (advanced).** The admitted C8 convention gives \(k_x=-k_{\mathrm{out}}\). Compute its integer class and a rational chain bounding it. Then explain precisely why the two-dimensional example from Comparison3 cannot be inferred from the \(S^2\) matrix result.

**Solution.** In \(\mathbb Z/2\mathbb Z\), negation fixes the nonzero class, so \([k_x]=[k_{\mathrm{out}}]\ne0\). Since \(\partial A_{\mathrm{out}}=-2k_{\mathrm{out}}=2k_x\), the rational chain \(A_{\mathrm{out}}/2\) bounds \(k_x\). There is no integral chain bounding it, by the nonzero class.

For the two-dimensional wave the fiber consists of two points, and the sphere cycle is a reduced degree-zero difference. The two phase arcs and their intersections have ordinary degree-zero groups for disconnected fibers, so the degree-two computation using \(H_2(S^2)=\mathbb Z\) and \(H_1(S^2)=0\) does not apply. The complement \(\mathbb C^*\) is path connected. The explicit semicircle path has integral boundary \([-1]-[1]\), proving the actual difference class zero. Treating that case as another order-two class would contradict its concrete bounding path.

## Exact scope and credit

The full working proof gives every needed chain, open-cover, sphere and mapping-torus argument and identifies the actual outward generator. It credits Allen Hatcher's author-hosted *Algebraic Topology*, Chapter2, for prism, subdivision, Mayer--Vietoris and mapping-torus background. The existing AH032-2 orientation and explicit cylinder are retained exactly. This companion does not decide the intended coefficient convention of a private source, general Petrowsky component constancy, rational-form completeness, projective tube injectivity or recursive course foundations. Those remain separate tasks.
