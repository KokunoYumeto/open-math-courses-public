<span id="exact-application-bindings-for-the-orbit-prerequisite-route"></span>
# Predual, normal-weight and cone arguments for the orbit proof

Normal-weight and cone arguments use the bounded predual, convexity and Hilbert-space results described below. Their applications are given for arbitrary algebras and Hilbert spaces, without a separability reduction.

<span id="the-bounded-foundation-contract-used-by-nw"></span>
## The bounded foundation contract used by NW

The duality prerequisite **NW-DEP-DUAL** is supplied by [Concrete preduals from Hilbert tensors](../../../OA-MOD/OA-MOD-CP.html), Sections CP06–08 and CP11–12. CP06 gives the Banach predual and its isometric dual identification. CP07 gives positive spanning/separation, ultraweak closedness of positive cones and norm balls, norm closure of the predual and its positive cone, and order normality of predual positives. CP11 gives the inherited corner topology and predual. CP12 gives bounded normal positive-functional supports from the earlier bounded support/one-sided-ideal proof, without the NW converse or a finite-domain weight theorem. Fixed multiplication is BK03; adjoint continuity is CP07.

The topology prerequisite **NW-DEP-TOPO** is supplied by [Concrete preduals from Hilbert tensors](../../../OA-MOD/OA-MOD-CP.html), Sections CP08–10. The proof of CP09 handles the conjugate Hilbert summand explicitly, so it applies to arbitrary Hilbert spaces and gives the full continuous dual, not merely a bounded-set dual. CP10 includes the real selfadjoint-space statement needed by NW09. Its convex-closure assertion uses HB6 Theorem 6.3/Corollary 6.4(2), at arbitrary locally convex generality. The empty convex set is handled separately in that proof.

The convexity prerequisite **NW-DEP-CONVEX** uses the following results:

| Required statement | Full proof witness | Application |
| --- | --- | --- |
| Open/strict real locally convex separation | Hahn–Banach, Baire and the basic theorems on Banach spaces, Theorem 6.3 and Corollary 6.4(2), including the Minkowski/open-separation proof | NW06–09 convex closures and positive separation |
| Weak-star compactness of dual balls for arbitrary normed spaces | [Weak topologies and compactness](../../../foundations-of-von-neumann-algebras/weak-topologies-tychonoff-banach-alaoglu-mazur-bipolars-krein-milman-and-eberlein-smulian.html), Theorem 3.1 and its Tychonoff proof | Compact balls of `M=(M_*)*` in NW03/06/09 |
| Weak compactness of arbitrary Hilbert balls | [Hilbert spaces and compact operators](../../../foundations-of-von-neumann-algebras/hilbert-spaces-and-compact-operators.html), Theorem 2.3, and weak-topology Theorem 3.1, via the specialization below | Hilbert ball in NW06 |
| Krein–Šmulian for a convex subset of a Banach dual, every closed norm-ball slice | [Compact and trace-class operators, the predual of B(H), and the operator topologies](../../../foundations-of-von-neumann-algebras/compact-and-trace-class-operators-the-predual-of-b-h-and-the-operator-topologies.html), Theorem 9.3; its `c0*=ell1` input is Example 5.1(a) | NW06–09 pass from all bounded closed slices to an entire ultraweak closed set |

The Krein–Šmulian proof uses separation, Banach–Alaoglu and the actual sequence-space dual proof; no trace-class duality or separable-Hilbert hypothesis is needed by that selected argument. NW09's selfadjoint convex set can be viewed as a convex subset of `M`, whose selfadjoint part is ultraweakly closed. Thus Krein–Šmulian is applied to the already identified Banach dual `M=(M_*)*`; a new real Banach-predual theorem is unnecessary.

For the Hilbert-ball specialization, let `R(eta)(xi)=<xi,eta>`, with inner product linear first. HS2.3 makes `R` an onto conjugate-linear isometry `H -> H*`. On a ball, convergence of all `R(eta)(xi)` is equivalent to convergence of all `<eta,xi>`, by complex conjugation. Thus `R` is a homeomorphism from the weak Hilbert ball onto the weak-star dual ball, which WT3.1 makes compact. Scaling covers every radius; the zero space is immediate. This proves precisely the compactness used in NW06, without a separability or reflexivity import.

The full NW11 proof is the actual chain `P=>L=>N=>A`, `A=>L`, `L=>P`. NW03–08 justify the sigma-finite localization and arbitrary-family gluing; NW09–10 prove positive separation and the supremum. A faithful normal state is used only within its support corner. The family of dominated normal functionals need not be directed, and the theorem retains zero and infinite weight values.

<span id="an-acyclic-application-to-the-gns-normality-statement"></span>
## An acyclic application to the GNS normality statement

The bounded positive-map normality criterion in WG001 is proved after Corollary 11.5 of [The universal enveloping von Neumann algebra](../../../foundations-of-von-neumann-algebras/the-universal-enveloping-von-neumann-algebra-of-a-c-star-algebra-and-w-star-algebras.html). The following direct specialization after NW11 also proves GNS normality, without using that criterion or its singular-functional argument.

Let `phi` be any normal weight, with the GNS representation of WG006. The direct increasing-net calculation in WG007 proves `pi_phi(a_alpha) -> pi_phi(a)` strongly whenever `0 <= a_alpha ↑ a`. That calculation uses only weight normality and the finite GNS domain; it does not need the bounded-map normality converse.

For `xi` in the GNS space set `f_xi(a)=<pi_phi(a)xi,xi>`. This is a bounded positive functional and is order normal by the preceding strong convergence. Apply NW11 to the finite-valued weight `f_xi` on `M+`. It gives

`f_xi(a)=sup{rho(a): rho in M_*+, rho <= f_xi}`.

If `f_xi(1)=0`, the functional is zero. Otherwise choose dominated `rho_n` with `rho_n(1) -> f_xi(1)`. Positivity and CP07's bounded-functional norm formula give

`||f_xi-rho_n||=f_xi(1)-rho_n(1) -> 0`.

This norm formula applies to all bounded positive functionals; it does not presume that `f_xi` is already in the predual. Norm closure of `M_*` in CP06 now gives `f_xi in M_*+`. Polarization gives every mixed vector pullback in `M_*`. For a square-summable vector-series functional on `B(H_phi)`, its pullback is the norm-convergent sum of these mixed pullbacks, since the norm of each term is at most `||xi_n||||eta_n||` and that scalar series converges. CP06 again gives membership in `M_*`. All ultraweak test functionals therefore pull back continuously, which is exactly ultraweak continuity of `pi_phi`.

The order is acyclic: bounded CP supports and topology -> WG003–006 and NW01–11 -> WG007's GNS normality conclusion -> OW/WH/SF. NW01–11 uses WG003–006, not WG007, and no bounded-map converse appears in its proof. This preserves arbitrary weights and Hilbert spaces; semifiniteness is not added to WG007.

<span id="the-precise-ow-and-wh-applications"></span>
## The precise OW and WH applications

OW02 identifies a normal positive functional `omega <= c phi` with its bounded positive commutant operator `h_omega`. Domination is on all of `M+`, and `c` is finite, including zero. The proof uses DW03 on the finite algebraic domain and WG008's **increasing net of finite positive contractions** to extend order back to all of `M+`. The operators `e_alpha a e_alpha` need not increase; their norm-bounded strong/ultraweak convergence suffices for bounded normal functionals. Do not substitute finite projections or a sequence of cutoffs.

OW03 uses DW04's comparison operator into the bounded functional's GNS space. Its range is dense here because the finite positive cutoffs put the cyclic vector in its range closure, and this reducing closure contains the cyclic orbit. The polar operator therefore satisfies `UU*=I_Homega`, whereas `U*U=s(h_omega)`. The vector `eta_omega=U*Omega_omega` satisfies

`h_omega^(1/2)Lambda_phi(x)=pi_phi(x)eta_omega` for **exactly** `x in n_phi`,

`omega(a)=<pi_phi(a)eta_omega,eta_omega>` for all `a in M`, and

`||eta_omega||^2=omega(1)=||omega||`.

This requires `phi` normal and semifinite, and allows nonfaithfulness and nonseparability. Do not promote the general DW04 range `K` to the whole target without OW03's density argument. The cutoff density can also be checked directly by `||(pi_omega(e_alpha)-I)Omega_omega||^2 <= omega(1-e_alpha) -> 0`.

These are the inputs of WH10, where `h_omega` is a contraction for `omega<=phi`. The norm supremum first holds on GNS vectors by NW11, then extends by its 1-Lipschitz bound. WH10's separate commutant-orbit totality uses faithfulness in its faithfulness argument. WH11 uses the selfadjoint multiplier `h_omega^(1/2)` and RD07 to place `eta_omega` in the right algebra; the NW11 supremum then proves the exact finite energy and equality of the recovered left-bounded vector. WH12 uses the same vectors in the opposite finite cone and variational formula. The strict multiplier bound follows by scaling `t eta`, `t ↑ 1`, including infinite suprema.

WH13 gives the arbitrary-algebra n.s.f.-weight construction. Its use of bounded positive-functional supports in WS04–06 also follows from CP12: if `p=s(omega)`, compression and faithfulness on `pMp` give

`omega(x*x)=omega(p x*x p)=0 iff x p=0`.

Indeed, `p x*x p=(xp)*(xp)` is positive in `pMp`, so corner faithfulness applies. This is exactly WH.44. Zorn's maximal orthogonal family of state supports then has sum one, and its arbitrary sum of functionals is normal; finite support sums have finite weight and WG008 proves semifiniteness. No faithful state on the whole algebra is used.

<span id="the-precise-sf-applications-and-limits"></span>
## The precise SF applications and limits

SF02 itself proves the positive symmetric extension bridge: the completion of the initial form norm embeds injectively in `H` by symmetry, yielding a closed dense positive form for QF03. QF04's unitary form symmetry then proves affiliation. It never assumes that the initial form is already closed.

SF03 binds the product graph-core test to RD06 and the affiliated multiplier on the **opposite right algebra** to HA07. The positive extension of SF02 and its spectral cutoffs give the reverse square-cone inclusion. WH11 gives recovery of positive left multipliers as finite-energy GNS vectors. The mirror side uses the actual WH08/12 right-weight GNS construction. Its two square cones are dual in the **complex** sense of SF01: each pairing is real and nonnegative, not just nonnegative real part on all of `H`.

SF04 uses MF06–09's actual analytic algebra and product identities. MF07 gives bijective complex-power action on that algebra; MF08 gives simultaneous vector, involution-graph and uniformly bounded multiplier approximation. MF09 checks nondegeneracy, product density and joint power cores. MA16 supplies arbitrary-Hilbert Gaussian continuation; the real Gaussian and the bounded spectral function `exp(-(log s)^2/(4r))` make the smoothing preserve dual positivity and land in every real-power domain. The quarter-power equality is a domain statement, not a formal manipulation.

SF05 uses MF05 for `JMJ=M'`, HAP08 for `JzJ=z*`, and HAP05 on the nondegenerate analytic multiplier algebra for arbitrary `xJxJ` cone invariance. HAP05's approximants are norm bounded and converge strongly with their adjoints. SF06–07 then prove the orthogonal-support geometry and both norm inequalities. They establish uniqueness of cone representatives and of cone-preserving intertwiners whenever those objects exist.

**SF02–07 does not prove existence of a cone representative for every bounded normal positive functional.** That existence result is the additional argument of [The positive cone of a standard representation](../../reader/orbit-proof-route/sf.html), Sections SF08–10. The bounded bicommutant theorem, WH05–09's weight/GNS results, HAP01–04's multiplier approximation and MA08–09's analytic-domain results remain distinct prerequisites where used.
