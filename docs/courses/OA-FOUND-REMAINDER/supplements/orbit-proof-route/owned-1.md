<span id="the-standard-crossed-product-commutant"></span>
## The standard crossed-product commutant

Let $G$ be a locally compact group, $M$ a von Neumann algebra, and $\alpha:G\to\operatorname{Aut}(M)$ a point-ultraweakly continuous action. Represent $M$ faithfully in a standard form on $K$, with modular conjugation $J$. Its canonical unitary implementers $U_g$ are strongly continuous, satisfy $U_gxU_g^*=\alpha_g(x)$, and commute with $J$, as in lesson 10. On $L^2(G,K)$ let

$$ \pi_\alpha(x)\xi=\alpha_{s^{-1}}(x)\xi(s),\qquad
   \lambda_g\xi=\xi(g^{-1}s),\qquad
   R_g\xi=\Delta_G(g)^{1/2}\xi(sg). \tag{I1} $$

Write $P=M\rtimes_\alpha G=(\pi_\alpha(M)\cup\lambda(G))''$. Choose an n.s.f. weight. The general standard-form equivalence theorem `OA-MOD-SE-10` transports its canonical GNS standard form onto the prescribed form, preserving J and the canonical automorphism implementers by SE-11; its arbitrary directed support-corner patching does not require a faithful state on the whole algebra. For the standard model chosen initially in BF77, one may simply start with this weight-constructed form. The coefficient construction in `OA-FLOW.DW.LEFTHILBERT` supplies a left Hilbert algebra $\mathcal A_\varphi\subset L^2(G,K)$ whose generated left von Neumann algebra is $P$. The closed-operator theorem `OA-FLOW.DW.INVARIANTCORE`, equation M25, identifies the closure of its coefficient involution and its polar conjugation, including equality of domains. In the conventions of (I1) the conjugation is

$$ \mathcal J\xi=\Delta_G(s)^{-1/2}U_s^*J\xi(s^{-1}). $$

The general Hilbert-algebra commutant theorem `OA-MOD-MF-05` applies directly to this left Hilbert algebra and its closed polar decomposition. Its full-completion step WH-03–04 preserves both the generated algebra and the closed involution. The theorem therefore gives

$$ \mathcal J P\mathcal J=P'. \tag{I2} $$

This argument retains arbitrary Hilbert dimension and the full locally compact group scope. The coefficient-domain construction requires the exact general GNS input and the relative Tomita domain and standard transport identities D23–D24. Equation M25 additionally uses the real-power domain theorem, M23 imaginary-power invariance and `OA-FLOW.GRAPH.POWERS`. The displayed antiunitary formula alone proves neither the closed polar identification nor (I2). Reconstructing the associated dual weight in lesson 14 is needed for its weight and modular-action identifications; that second reconstruction is not an additional premise of this commutant calculation.

The two conjugations can be checked on continuous compactly supported $K$-valued sections. Since $U_sJ=JU_s$ and $U_{s^{-1}}^*=U_s$, direct substitution gives

$$ \mathcal J\pi_\alpha(x)\mathcal J=JxJ\otimes1. \tag{I3} $$

For a group generator, the argument arriving at the innermost section is $sg$, while its operator coefficient is $U_s^*U_{sg}=U_g$. The Haar scalars reduce to $\Delta_G(g)^{1/2}$, so

$$ \mathcal J\lambda_g\mathcal J\xi
     =\Delta_G(g)^{1/2}U_g\xi(sg)
     =(U_g\otimes R_g)\xi. \tag{I4} $$

These identities hold on all vectors by boundedness. Standard form gives $JMJ=M'$. Since antiunitary conjugation preserves generated von Neumann algebras, (I2)–(I4) prove

$$ P'=\bigl(M'\otimes1\ \cup\ \{U_g\otimes R_g:g\in G\}\bigr)''. \tag{I5} $$

There is no abelian, discrete, compact, unimodular, or separability assumption in this standard-representation calculation. The right regular factor in (I4) is essential for a nonunimodular group. Formula (I5) proves the standard-form case of the source's crossed-product commutant theorem X.1.21. Its additional concrete assertion for every possibly nonstandard covariant representation is a separate representation-extension obligation; the intrinsic consequences below need only (I5).

