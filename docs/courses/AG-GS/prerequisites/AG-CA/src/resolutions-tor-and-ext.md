# Resolutions, Tor and Ext

*Written and self-checked by GPT-6.1 Sol (OpenAI) in Codex, Ultra setting, October 2026. Original exposition, CC0.*

The flatness and depth lessons use homology to turn an exactness question into a group that measures its failure. This lesson supplies the comparison and exact-sequence arguments needed for that use. Modules and free ranks may be arbitrary. We use the universal properties of tensor products, kernels and quotients, and the definition of a projective module: maps from it lift across surjections.

## 1. Constructing and comparing resolutions

An augmented projective resolution of a module \(M\) is an exact sequence
\[
\cdots\longrightarrow P_2\xrightarrow{d_2}P_1\xrightarrow{d_1}P_0\xrightarrow{\epsilon}M\longrightarrow0
\]
with projective terms. Such resolutions exist: take a free module onto \(M\), a free module onto its kernel, and continue. A free module is projective because the images of its basis vectors can be lifted separately. A projective module is a direct summand of a free module: split a free surjection onto it. Conversely a summand of a free module has the lifting property by extending a map by zero on the complementary summand.

**Theorem 1.1 (comparison).** A map \(f:M\to N\) lifts to a chain map between any projective resolutions \(P\to M\), \(Q\to N\). Two such lifts are chain homotopic. For \(f=1_M\), comparison maps in the two directions are inverse up to homotopy.

**Proof.** Lift \(f\epsilon_P:P_0\to N\) across \(Q_0\to N\). If maps have been chosen through degree \(n-1\), the map \(P_n\to Q_{n-1}\) given by \(f_{n-1}d_n\) lands in \(\ker d_{n-1}=\operatorname{im}d_n\). Projectivity lifts it to \(Q_n\). This gives a chain map by induction.

For two lifts \(f_\bullet,g_\bullet\), set \(h_{-1}=0\). Their degree-zero difference lands in \(\ker\epsilon_Q\), so lift it to \(h_0:P_0\to Q_1\). Inductively,
\[
d_Q(f_n-g_n-h_{n-1}d_P)
=(f_{n-1}-g_{n-1}-d_Qh_{n-1})d_P
=h_{n-2}d_P^2=0.
\]
Lift this map through \(Q_{n+1}\twoheadrightarrow\ker d_Q\) to \(h_n\). Thus
\[
f_n-g_n=d_Qh_n+h_{n-1}d_P.
\tag{1}
\]
Applying the same argument to a composite lifting \(1_M\) compares it with the identity chain map. Tensoring (1), or applying \(\operatorname{Hom}\) to it, preserves the homotopy identity. Homotopic maps induce the same map on homology, since their difference on a cycle is a boundary. \(\square\)

## 2. The connecting homomorphism

For a chain complex, \(H_n=\ker d_n/\operatorname{im}d_{n+1}\). A degreewise exact sequence of complexes \(0\to C'\xrightarrow{i}C\xrightarrow{j}C''\to0\) has a natural long exact homology sequence.

**Proof and construction.** Given a cycle \(z''\in C''_n\), lift it to \(z\in C_n\). Then \(dz=i(w)\) for a unique \(w\in C'_{n-1}\), and injectivity of \(i\) gives \(dw=0\). Set \(\partial[z'']=[w]\). Changing \(z\) by \(i(v)\) changes \(w\) by \(dv\); changing \(z''\) by a boundary can be lifted by a boundary in \(C\) and leaves its class unchanged.

At \(H_n(C)\), a class mapping to zero can be represented, after subtracting a lifted boundary, by a cycle in \(i(C')\). At \(H_n(C'')\), vanishing of \(\partial[z'']\) means \(w=dv\); then \(z-i(v)\) is a cycle lifting \(z''\). At \(H_{n-1}(C')\), a class that becomes a boundary in \(C\) is obtained by applying this construction to the image in \(C''\) of that boundary's preimage. These are the three exactness assertions; their repetition gives the whole sequence. A commuting diagram of short exact sequences takes the chosen lifts and differentials to lifts and differentials, proving naturality. Reversing degrees gives the corresponding cohomology sequence. \(\square\)

## 3. Balance and symmetry of Tor

Define \(\operatorname{Tor}_n^R(M,N)=H_n(P\otimes_RN)\), using a projective resolution of \(M\). Theorem 1.1 makes this independent of the choice, naturally in both variables. The tensor functor is right exact by its presentation by bilinear generators and relations, so degree zero is \(M\otimes_RN\).

**Lemma 3.1 (total-complex comparison).** Let \(P\to M\), \(Q\to N\) be projective resolutions. Put
\[
T_n=\bigoplus_{a+b=n}P_a\otimes_RQ_b,
\qquad d(u\otimes v)=d_Pu\otimes v+(-1)^a u\otimes d_Qv.
\tag{2}
\]
The augmentations \(T\to P\otimes_RN\) and \(T\to M\otimes_RQ\) induce isomorphisms on homology.

**Proof.** Projective modules are flat: free modules preserve injections under tensor, and so do their summands. Consequently each augmented column \(P_a\otimes Q\to P_a\otimes N\) is exact. Include its augmented term in vertical degree \(-1\). Its resulting total complex is acyclic. Indeed, in a cycle choose the component with largest horizontal degree \(a\). Its vertical differential is zero, because no component of larger horizontal degree can contribute. Exactness of that augmented column supplies a vertical preimage. Subtract its total boundary, with the sign from (2); this removes the component and creates components only in smaller horizontal degree. Repeat. There are finitely many degrees in a total-degree element, and the procedure ends after the degree-zero column. Every cycle is therefore a boundary. This augmented total complex is the mapping cone of the augmentation, with a degree shift and the same signs. Equivalently, the lift-and-boundary argument of Section 2 says directly that acyclicity makes the augmentation a homology isomorphism. Applying the identical argument to rows proves the second assertion. No infinite sum or convergence is used. \(\square\)

**Theorem 3.2.** Tor can be computed by resolving either variable, and
\[
\operatorname{Tor}_n^R(M,N)\cong\operatorname{Tor}_n^R(N,M)
\]
naturally. It has long exact sequences in both variables.

**Proof.** Lemma 3.1 identifies the two computations. The interchange map on (2), \(u\otimes v\mapsto(-1)^{ab}v\otimes u\), is a chain isomorphism to the total complex with the two resolutions interchanged: checking the horizontal and vertical summands gives respectively the signs \((-1)^{(a-1)b}\) and \((-1)^{a+a(b-1)}\). Comparison maps show naturality and independence of resolutions. For a short exact sequence in the unresolved variable, every term of the resolved complex is flat, so tensor gives a degreewise short exact sequence. Section 2 supplies its long exact sequence. Balance supplies it in the other variable. \(\square\)

## 4. Ext in either variable

Define
\[
\operatorname{Ext}_R^n(M,N)=H^n(\operatorname{Hom}_R(P_\bullet,N)),
\qquad \delta(\varphi)=\varphi d_P.
\tag{3}
\]
In degree zero this is \(\operatorname{Hom}_R(M,N)\). Comparison proves independence and functoriality, contravariantly in \(M\) and covariantly in \(N\). Projectivity makes \(\operatorname{Hom}_R(P_a,-)\) exact, so Section 2 immediately supplies the second-variable long exact sequence.

**Lemma 4.1 (horseshoe).** From \(0\to M'\to M\to M''\to0\) and projective resolutions \(P'\), \(P''\), one can build a resolution \(P\to M\) and a degreewise split exact sequence \(0\to P'\to P\to P''\to0\), with \(P_n=P'_n\oplus P''_n\).

**Proof.** Lift the map \(P''_0\to M''\) to \(M\), and combine it with \(P'_0\to M'\to M\). This is onto: first lift an element's image in \(M''\), then correct its difference in \(M'\). Its kernel \(K\) fits into \(0\to K'\to K\to K''\to0\). To check the last surjection, an element of \(K''\) lifts to \(P''_0\); its image in \(M\) belongs to \(M'\), and can be cancelled by an element of \(P'_0\). The kernel is exactly \(K'\). Repeat this construction on the short exact sequence of kernels, with \(P'_1,P''_1\), then on the next kernels. The differentials land in the preceding kernels by construction. Exactness at every degree and the indicated split sequence follow. \(\square\)

Applying \(\operatorname{Hom}_R(-,N)\) gives a degreewise short exact sequence of cochain complexes in the reverse order. Section 2 now proves the first-variable long exact Ext sequence. Naturality follows by comparing resolutions: maps induced by a map of short exact module sequences can be lifted compatibly to the horseshoes. At each degree the lift is chosen on the quotient projective summand and corrected on the submodule summand, as in the preceding construction. Two choices are homotopic by the same kernel-lifting induction as (1), so the maps on cohomology are canonical.

## 5. Exercises and solutions

**Exercise 5.1 (easy).** Compute \(\operatorname{Tor}^{\mathbb Z}_n(\mathbb Z/a,\mathbb Z/b)\), for positive integers \(a,b\).

**Solution.** Resolve the first variable by \(0\to\mathbb Z\xrightarrow{a}\mathbb Z\to\mathbb Z/a\to0\). Tensoring gives multiplication by \(a\) on \(\mathbb Z/b\). Its kernel and cokernel are cyclic of order \(\gcd(a,b)\); higher homology is zero. The symmetry theorem explains the symmetry of this answer.

**Exercise 5.2 (medium).** Compute \(\operatorname{Ext}_{\mathbb Z}^1(\mathbb Z/a,N)\) and explain why higher Ext vanishes.

**Solution.** Apply \(\operatorname{Hom}(-,N)\) to that resolution. The resulting cochain differential is multiplication by \(a\) on \(N\). Thus \(\operatorname{Ext}^1=N/aN\), while degree zero is the subgroup killed by \(a\). There are no terms above degree one. The latter argument applies to every \(N\), including nonfinite modules.

**Exercise 5.3 (hard).** Explain why an element killed in a tensor product need not vanish before tensoring, using the connecting map for \(0\to\mathbb Z\xrightarrow{a}\mathbb Z\to\mathbb Z/a\to0\).

**Solution.** Tensor with \(\mathbb Z/a\). The injection becomes the zero map, and its kernel is all of \(\mathbb Z/a\). The Tor long exact sequence identifies this kernel with \(\operatorname{Tor}_1^{\mathbb Z}(\mathbb Z/a,\mathbb Z/a)\). A cycle represented in the quotient resolution lifts to an element whose differential is \(a\); its preimage in the submodule is \(1\), so the connecting map gives the corresponding residue class. This is exactly the lift-and-differentiate construction of Section 2.

## Sources and proof dependencies

The comparison, total-complex and horseshoe arguments are standard homological algebra. For reference, the Stacks Project Authors give the Tor and Ext constructions in the algebra chapter, Tags 00LZ, 00M0, 00M3, 00LT and 00LU. This lesson supplies its own complete elementary arguments and does not require the derived-functor theory as an external proof provider. The later flatness and depth lessons use Theorems 1.1 and 3.2 and Section 4.
