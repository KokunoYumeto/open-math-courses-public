# Haar uniqueness through shrinking neighborhoods

*Source companion by GPT-6.1 Sol (OpenAI), Ultra reasoning effort, 5 October 2026. Original text: public domain (CC0). This note records the source and the conventions of the Fremlin argument in Theorem 9.2 of the Haar lesson.*

The complete shrinking-neighborhood argument is proved in [Theorem 9.2 of the Haar lesson](../haar-measure-on-locally-compact-groups.md#oa-fnd-hm-06). It compares the two measures on an open subset of the product, squeezes the ratios of small symmetric neighborhoods, and then extends equality from relatively compact open sets to every Borel set. The main lesson supplies each step of this proof, including the open-set product theorem; this companion does not repeat the proof.

Fremlin works with a broader topological measure convention. Theorem 9.2 assumes the convention already defined and constructed in the course: measures are finite on compact sets, inner regular on open sets and outer regular on Borel sets. Accordingly its last step uses Borel outer regularity directly. It does not assume sigma-finiteness or inner compact regularity on all Borel sets. The comparison with Fremlin’s completed-measure convention is proved separately in [Proposition 13.7](../haar-measure-on-locally-compact-groups.md#haar-measure-convention-bridge).

## Source

D. H. Fremlin, [*Measure Theory*, Volume 4, Topological Measure Spaces](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/index.htm), §442B, gives the neighborhood-ratio argument; its [editable TeX](https://www1.essex.ac.uk/maths/people/fremlin/mt4.2013/mt442.tex) is freely accessible.

Theorem 9.2 differs from Fremlin’s treatment in three respects: it works in the course’s LCH/Borel convention, it expands the compact shrinking step, and it replaces the quasi-Radon base-uniqueness step by inner regularity on open sets and outer regularity on Borel sets.
