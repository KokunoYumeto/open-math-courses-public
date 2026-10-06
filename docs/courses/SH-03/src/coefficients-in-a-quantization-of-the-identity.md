# Coefficients in a quantization of the identity

A contact transformation moves covectors. An operator above that transformation also acts on sheaf coefficients. Even when the covectors stay fixed, the operator can change a coefficient line or shift every complex. We identify the local coefficient complex of an identity quantization and prove that it must define an equivalence on the bounded coefficient category itself.

Use When a kernel quantizes a contact transformation, Local existence of contact kernel equivalences, and Microlocal composition at prescribed covectors for the kernel-germ action. We keep a commutative ring \(k\) of finite global dimension \(g\). All derived categories below contain arbitrary bounded coefficient complexes. Finite generation, perfectness and a field hypothesis will be stated whenever used.

*Written by GPT-6.1 Sol (OpenAI), Ultra, September 2026. Author self-check recorded; not independently reviewed. New original text is public domain (CC0).*

## The conormal category, including its morphisms

Let \(S\) be a smooth closed submanifold in a coordinate neighborhood of a real manifold \(X\), and let \(p\in T_S^*X\). Denote by \(\mathcal C_S(p)\) the full subcategory of \(D^b(k_X;p)\) whose objects have microsupport contained in \(T_S^*X\) on some neighborhood of \(p\). Microsupport as a germ is invariant under localized isomorphism, so this definition is independent of the representative.

Write \(A_S\) for a constant bounded coefficient complex \(A\) on \(S\), extended by zero. Everything here is local around the base point of \(p\); extension beyond a smaller chart does not specify a global constant model for an arbitrary original sheaf.

We need two precise conormal prerequisites. The local model theorem says every object of \(\mathcal C_S(p)\) is isomorphic to some \(A_S\). The conormal morphism normalization says the natural coefficient map gives

\[
\operatorname{Hom}_{D^b(k)}(A,B[j])
\xrightarrow{\sim}
\operatorname{Hom}_{D^b(k_X;p)}(A_S,B_S[j])
\quad(j\in\mathbb Z),
\qquad\text{(1)}
\]

compatibly with identities and composition, for arbitrary bounded \(A,B\). Equivalently, one may combine the point-localized morphism theorem with the normalized local calculation
\(\mu\operatorname{hom}(A_S,B_S)_p\simeq R\operatorname{Hom}_k(A,B)\).
There is no codimension shift in this calculation. These are statements at one cotangent point; they do not identify morphisms over an arbitrary open region with global sections of microlocal Hom.

The second prerequisite is stronger than an object classification. It is also stronger than the special formula with first argument \(k_S\). We state it separately so that neither essential surjectivity nor a perfect-coefficient calculation silently replaces (1). The foundational proof of this arbitrary-coefficient normalization belongs to the conormal and microlocal-Hom prerequisites.

Together the two prerequisites give an equivalence

\[
I_S:D^b(k)\xrightarrow{\sim}\mathcal C_S(p),
\qquad A\longmapsto A_S.
\qquad\text{(2)}
\]

Indeed the local model gives essential surjectivity, while (1) with \(j=0\) gives full faithfulness for every pair of objects. The construction is exact, since constant extension and closed direct image take a coefficient triangle to the corresponding sheaf triangle.

For every \(p\) a suitable \(S\) exists locally. If \(p=(x;0)\), choose \(S=X\) in a small chart. If \(p\ne0\), take a coordinate \(t\) with \(dt_x\) equal to its covector and use \(S=\{t=t(x)\}\). Thus (2) is available both at zero and at nonzero covectors.

## A diagonal coefficient is the local identity kernel

Suppose \(K\) is a kernel above the identity on a selected cotangent neighborhood \(\Omega\) of \(p\). Its physical graph is

\[
\Lambda_{\mathrm{id}}=
\{(x,x;\xi,-\xi):(x;\xi)\in\Omega\}
\subset T_\Delta^*(X\times X),
\qquad\text{(3)}
\]

where \(\Delta\) is the diagonal. Assume the two selected-region microsupport conditions from the contact-kernel lesson. The conormal local model on \(X\times X\) gives a bounded complex \(M\) of \(k\)-modules such that

\[
K\simeq M_\Delta
\quad\text{in }D^b(k_{X\times X};(p,p^a)).
\qquad\text{(4)}
\]

For passage from (4) to an operator we also use the kernel-germ calculus: over a graph with the two localized admissibility conditions, the operator at the chosen output covector depends only on the kernel germ at its unique corresponding input covector. In the notation of microlocal composition, the graph kernel lies in the class for which composition with every input germ is defined. This is a germ-descent statement, not ordinary convolution of arbitrary representatives of a fraction. A roof representing (4) is interpreted through that calculus.

It follows that, naturally for \(G\in D^b(k_X;p)\),

\[
\Phi_KG\simeq\Phi_{M_\Delta}G
\simeq M_X\otimes_k^LG.
\qquad\text{(5)}
\]

The last equality can be checked before localization. Let \(\delta:X\hookrightarrow X\times X\) and let \(q_1,q_2\) be the projections. The closed-embedding projection formula gives
\(M_\Delta\otimes q_2^{-1}G\simeq\delta_*(M_X\otimes G)\).
Since \(q_1\delta=\mathrm{id}_X\), proper-support direct image returns \(M_X\otimes G\). There is no orientation factor or dimension shift. The diagonal is closed and its projection to \(X\) is the identity, hence proper on this support.

The statement is local. It does not identify a kernel on the entire product with a globally constant diagonal kernel, and it does not assert a single coefficient complex throughout a large cotangent region.

## A directional tensor equivalence forces a coefficient equivalence

**Theorem.** Fix any \(p\in T^*X\) and \(M\in D^b(k)\). If

\[
L=M_X\otimes_k^L-:
D^b(k_X;p)\longrightarrow D^b(k_X;p)
\qquad\text{(6)}
\]

is an equivalence, then

\[
T_M=M\otimes_k^L-:
D^b(k)\longrightarrow D^b(k)
\qquad\text{(7)}
\]

is an equivalence.

**Proof.** First construct the right adjoint on the same bounded localized category:

\[
R=R\mathcal Hom(M_X,-).
\qquad\text{(8)}
\]

Boundedness is necessary here. If \(M\) has cohomology in \([a,b]\) and \(F\) in \([c,d]\), the arbitrary-sheaf bounded-Hom prerequisite on an \(n\)-manifold places (8) in \([c-b,d-a+3n+g+1]\). Its coarse upper bound suffices; no perfectness of \(M\) has been assumed. Tensor is bounded by finite global dimension.

Both operations preserve microsupport containment:

\[
\operatorname{SS}(LF)\subset\operatorname{SS}(F),
\qquad \operatorname{SS}(RF)\subset\operatorname{SS}(F).
\qquad\text{(9)}
\]

For the tensor estimate the other factor \(M_X\) has microsupport in the zero section, so the noncharacteristic tensor condition is automatic. For Hom the same zero-section condition on the first factor makes the noncharacteristic Hom estimate applicable. Adding a zero covector leaves the second microsupport unchanged. These estimates apply to arbitrary bounded coefficients and do not use coefficient duality or biduality.

In particular both functors take objects null at \(p\) to objects null at \(p\). Their ordinary tensor-Hom adjunction therefore descends, with its units, counits and triangle identities, to the quotient category. An adjoint to an equivalence is a quasi-inverse, so (8) is a quasi-inverse to (6).

Choose \(S\) as above. By (9), both \(L\) and \(R\) preserve \(\mathcal C_S(p)\). Thus they restrict to inverse equivalences on that full subcategory: their unit and counit remain isomorphisms there, and the restricted right functor supplies a preimage for every object. Preservation by \(L\) alone would not have established this last assertion.

Finally, coefficient tensor and closed extension give the natural identification

\[
L I_S(A)=(M_X\otimes A_S)
\simeq(M\otimes A)_S=I_S T_M(A).
\qquad\text{(10)}
\]

Conjugate the restricted equivalence by (2). Equation (10) identifies the conjugate with \(T_M\), proving (7). This argument uses the full morphism statement (1), not merely the existence of conormal coefficient models. \(\square\)

Conversely, a coefficient tensor equivalence gives a directional equivalence at every \(p\). The next argument constructs its tensor inverse and hence proves this directly, without appealing to an unspecified inverse sheaf functor.

## What invertibility means over the ring

For a bounded coefficient complex \(M\), the following conditions are equivalent:

1. \(T_M\) is an equivalence of \(D^b(k)\).
2. There is \(N\in D^b(k)\) with \(M\otimes_k^LN\simeq k\).

**Proof.** The module tensor-Hom adjunction has a bounded right adjoint \(R\operatorname{Hom}_k(M,-)\): for the same intervals its cohomology lies in \([c-b,d-a+g]\). If \(T_M\) is an equivalence, this right adjoint is its inverse. The actual counit at \(k\) is therefore an isomorphism

\[
M\otimes_k^L R\operatorname{Hom}_k(M,k)
\xrightarrow{\sim}k.
\qquad\text{(11)}
\]

Set \(N=R\operatorname{Hom}_k(M,k)\). Conversely, associativity and commutativity of derived tensor identify both \(T_MT_N\) and \(T_NT_M\) with the identity if \(M\otimes N\simeq k\). This proves the equivalence. Applying the same tensor identities to sheaves gives inverse functors \(M_X\otimes-\) and \(N_X\otimes-\); (9) ensures descent at every covector. \(\square\)

An invertible module \(P\), meaning \(P\otimes_kP^\vee\simeq k\) with \(P\) finite projective of rank one, gives \(M=P[r]\) and \(N=P^\vee[-r]\). The shift signs cancel. This family is available over a general ring, but we have not classified all invertible complexes by one global shift.

Over a nonzero field \(k\) the classification is elementary: \(M\) must be a one-dimensional vector space in one cohomological degree. To prove it, use (11). The bounded field Künneth formula reads
\(H^*(M\otimes N)=H^*(M)\otimes_k H^*(N)\).
Both factors are nonzero because their tensor is \(k\). If \(H^*(M)\) had two nonzero degrees, tensoring either with any fixed nonzero degree of \(H^*(N)\) would produce two nonzero output degrees. Thus both have a single degree. Their vector-space tensor is one-dimensional, which forces each factor to be one-dimensional. Splitting a bounded complex of vector spaces identifies \(M\) with that line and its shift. Conversely a shifted line is invertible.

For the zero ring all these categories are zero, and every functor between them is the unique equivalence. The nonzero qualification in the field classification avoids inferring a nonexistent one-dimensional vector space from that case.

## Exercises with complete solutions

### The diagonal does not add a dimension shift

*Difficulty: Introductory.*

On an \(n\)-manifold take \(K=k_\Delta[r]\). Compute its operator and inverse at an arbitrary covector. Explain why the codimension \(n\) of the diagonal does not contribute another shift.

**Solution.** Formula (5) gives \(\Phi_KG=G[r]\), whose inverse is \(G\mapsto G[-r]\). The calculation uses closed direct image and the identity projection of the diagonal, not exceptional inverse image along the diagonal. Projection formula and \(q_1\delta=\mathrm{id}\) produce no dualizing complex. Consequently the only shift is the explicitly supplied \(r\).

### Preservation alone does not restrict an equivalence

*Difficulty: Intermediate.*

Find an equivalence of a category that takes a full subcategory into itself but whose restriction is not essentially surjective. Locate the extra check in the proof of the theorem.

**Solution.** Regard \(\mathbb Z\) as a discrete category and use the equivalence \(n\mapsto n+1\). The full subcategory on nonnegative integers is preserved, but zero is absent from the restricted image. In the theorem the right adjoint is an inverse to \(L\), and the second estimate in (9) shows that this inverse also preserves the conormal subcategory. For every conormal object \(F\), its inverse \(RF\) is again conormal and \(LRF\simeq F\). This is the missing essential-surjectivity check.

### A torsion coefficient cannot quantize the identity invertibly

*Difficulty: Intermediate.*

Let \(k=\mathbb Z\) and \(M=\mathbb Z/7\) in degree zero. Show that \(M\otimes^L-\) is not a coefficient equivalence. Explain its consequence for a directional identity operator.

**Solution.** The nonzero module \(\mathbb Q\) is flat over \(\mathbb Z\), and \((\mathbb Z/7)\otimes\mathbb Q=0\). Thus \(M\otimes^L\mathbb Q=0\), so the functor sends a nonzero object to zero and cannot be an equivalence. The theorem rules out an equivalence \(M_X\otimes-\) at any covector. One may also test the nonzero conormal object \(\mathbb Q_S\): (2) proves it is nonzero at \(p\), while (10) shows its image is zero.

### Different components can carry different shifts

*Difficulty: Advanced.*

Let \(k=k_1\times k_2\), with both factors nonzero and of finite global dimension. Write \(e_1,e_2\) for the central orthogonal idempotents. For integers \(r\ne s\), prove that
\(M=e_1k[r]\oplus e_2k[s]\)
is invertible. Show that it is not a single shifted invertible module over \(k\).

**Solution.** The idempotent summands are projective, their mixed tensor products are zero, and \(e_i k\otimes e_i k\simeq e_i k\). Hence with \(N=e_1k[-r]\oplus e_2k[-s]\) the tensor \(M\otimes^L N\) is \(e_1k\oplus e_2k=k\). The preceding criterion proves invertibility. On an arbitrary complex \(A\), tensor with \(M\) shifts \(e_1A\) by \(r\) and \(e_2A\) by \(s\). Because the factors are nonzero and \(r\ne s\), \(M\) has nonzero cohomology in two different degrees. A single shifted module has cohomology in at most one degree, so no such description is possible. Its diagonal kernel is nevertheless an equivalence above the identity. This example explains why the field classification cannot be imposed over a disconnected coefficient ring.

## References

Kernels quantizing the identity and the conormal object model are part of Kashiwara and Schapira's theory of contact transformations for sheaves; see M. Kashiwara and P. Schapira, [*Microlocal study of sheaves*](https://webusers.imj-prg.fr/~pierre.schapira/BooksMono/Ast128.pdf), Astérisque 128 (1985), Chapters 6–7, and P. Schapira, [*A short review on microlocal sheaf theory*](https://webusers.imj-prg.fr/~pierre.schapira/LectNotes/MuShv.pdf) (2016). The full arbitrary-coefficient morphism normalization (1) is a foundational input, distinct from the object statement.
