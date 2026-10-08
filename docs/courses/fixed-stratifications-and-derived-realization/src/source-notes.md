# Sources, dependencies and reuse

These notes identify the mathematical sources, proof dependencies and reuse terms of the two readings and their six complete solutions.

## The checked human source

Valery A. Lunts and Olaf M. Schnürer, [*Categories of constructible sheaves*, arXiv:2601.05477v1](https://arxiv.org/abs/2601.05477v1), 9 January 2026. The versioned arXiv record identifies the source's [Creative Commons Attribution 4.0 licence](https://creativecommons.org/licenses/by/4.0/). Page numbers below are the printed numbers in that version. The checked PDF's SHA-256 is `5a049456debc9ba715280f5406f750f1d47167ac3dcb0377f1d3f76c10f16d80`.

The presentation uses newly written teaching prose, retains the source's mathematical scope where stated, condenses parts of its argument and expands other calculations. There are no verbatim prose extracts. The shared proof route is acknowledged as source-derived; fresh wording does not make that route an independently discovered proof. This attribution does not imply endorsement by the source authors.

## Realization criterion: exact dependencies

On narrow screens, the source table scrolls horizontally.

| Reading passage | Checked source passage | What is used |
| --- | --- | --- |
| Coefficient convention and local-system preliminaries, equation 22 | §1.1, p. 2; Definitions 2.2–2.3 and 2.8, p. 3; Propositions 3.3–3.4, pp. 7–8; Proposition 3.11, pp. 10–11 | Arbitrary associative unital rings and arbitrary stalk modules; local simple connectivity, local degree-one acyclicity and the local-system heart. |
| One-stratum realization, equations 23–25 | Theorem 4.1, pp. 11–13; Remark 4.3, p. 14 | The universal-cover projective generator, cohomology comparison, projective summands and coproducts, finite truncations and the telescope. |
| Boundary comparisons, equations 26–29 | §5.16 and Lemma 5.17, pp. 19–20; Proposition 5.24, pp. 24–25 | The internal-to-ambient comparison, compatibility with adjunction, open/closed localization and finite induction on strata. |
| Full criterion, equation 30 | Theorem 5.25, pp. 25–27 | The one-stratum tests and direct-image comparisons; two Hom filtrations for full faithfulness; finite gluing for essential surjectivity; restriction and adjunction for necessity. |
| Normal neighborhoods and injective link test, equations 31–34 | Definition 6.2 and §6.3, pp. 27–28; Lemma 6.6 and Corollary 6.8, pp. 28–29; Theorem 6.10, pp. 29–30 | Local conical products and link cohomology; testing the comparison on internally injective local systems; fundamental-group criteria. |
| Three torus-orbit strata of the projective line, equation 35 | Theorem 6.10, pp. 29–30; Proposition 6.11, p. 31 | The criterion applied to the explicitly computed disks, punctured disks and circle links. The reading does not prove the general toric geometry asserted in Proposition 6.11. |
| Finite cohomology versus the finite heart | Lemma 7.2 and Corollary 7.5, pp. 31–32; the distinction following Theorem 2.15, p. 5 | Restricting an equivalence to finite-cohomology objects is separate from deriving the finite-stalk heart. |

The first reading follows the source's central proof architecture. Its explicit telescope cohomology calculation, presentation of the adjunction and localization maps, and four solutions are expanded teaching checks. They are not a claim to an independent theorem or a new proof of every prerequisite.

Two scope restrictions are essential. First, the equivalence is proved for bounded and bounded-below complexes; it is not asserted for arbitrary unbounded targets. Second, the finite-kernel averaging alternative requires the kernel's order to be invertible in the coefficient ring. The source's wording in terms of characteristic, read for a general coefficient ring, would be insufficient; the reading keeps the stronger, explicit unit hypothesis and its existing integer-coefficient counterexample. Injective fundamental-group maps remain a separate sufficient alternative.

## Projective line: source and explicit calculations

Remark 6.12 (p. 31) supplies the two-stratum projective-line failure example. Theorem 5.25 and Theorem 6.10 supply the criterion against which its boundary is tested. The second reading itself constructs the one-arrow sheaf category, proves its projective resolution in equation 15, compares the missing degree-two morphism in equation 16, and constructs and excludes the cone object in equation 17. The argument preserves the cone sign, both cohomological degrees, the unrestricted and finite hearts, and the distinction between this fixed partition and failure after all refinements.

The circle calculation in equations 18–19 and both solutions show precisely why an internally injective open coefficient need not be ambient-direct-image acyclic, and why testing a finite constant coefficient would be the wrong injective test for the three-stratum partition. Those complete calculations go beyond the short source remark and are retained as original AI exposition. The link calculation uses the usual local-coefficient cohomology of circles and disks; the ambient degree-two class uses constant-coefficient cohomology of the two-sphere.

<a id="earlier-background-citation-and-remaining-prerequisites"></a>

## Remaining prerequisites

The realization and boundary criteria use the Lunts–Schnürer passages mapped above. Their applications also use the sheaf-theoretic and topological prerequisites below. The source map identifies those inputs and distinguishes them from the calculations supplied in these readings.

Ordinary sheaf adjunctions, enough injectives, projective resolutions, derived localization and truncations, and exact coproducts are prerequisites. The programme's *Complexes, cones and localization*, Section 4, and *Injective modules and bounded-below derived functors*, Sections 3–4, give relevant formal arguments; their own human-source licences remain attached to those separate works. Their texts are not imported or relicensed here.

The topology used for local-coefficient cohomology, the neighborhood computation in a general normal structure, and the sheaf-to-topological cohomology comparisons are still background inputs. Lunts–Schnürer §6.3 and Lemma 6.6 supply the stated normal-neighborhood mechanism; they do not turn this pair of readings into a complete development of those topological foundations. The general normal toric geometry paragraph remains an explicitly external geometric input. This bounded source comparison neither clears all programme foundations nor claims completion of the parent course.

## Reuse and changes

The text, explanatory checks, exercises and solutions, and the reader implementation are dedicated under [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/). They are written independently; the results and proof routes are credited to Lunts–Schnürer above.

The source document is not bundled; the versioned reference above identifies it.

[Reading index](../index.html) · [Reuse terms](../LICENSE.txt) · Provenance
