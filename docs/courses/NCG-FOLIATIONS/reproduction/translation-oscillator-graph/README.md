# Translation oscillator reproduction

Section 11E contains the complete proof and Exercises 119–121 contain all three
complete solutions (16+14+20=50 points). The scalar oscillator is odd as an
operator; its KK cycle is even. Actual smooth graph realization is restricted
to the stated germ-effective, isometric lattice suspension over the torus.
The general holonomy-groupoid problem remains open.

Use Python 3.13.9 with the pinned requirements:

    python -m pip install -r requirements.txt
    python draw_translation_oscillator.py
    python check_translation_oscillator_formulas.py
    python verify_translation_oscillator_reproduction.py

The commands may run from any working directory. Files are resolved relative
to the scripts. The figure generator writes ../../figures/
kt-translation-oscillator-graph.png and .svg. The finite checker defaults to
../../src/k-theory-of-the-leaf-space.md; --lesson-source accepts an explicit
complete source when reviewing an isolated candidate. Finite checks never
replace the completed analytic arguments. The reproduction verifier writes
only its selected work directory (default qa/ beside the scripts), launches
two fresh isolated generator processes, compares all three generated outputs
with the reference and verifies all ten actual font loads plus the full
embedded font notice. It has no network step.

The six panels are: exact even Gaussian; exact d=2 multiplicities k=0,…,5;
the literal measurable cube/regular unitary; the +1 Gaussian translation;
the actual fixed-source convolution with t=1/4, t'=3/4, r=3/2; and the
completed-domain/localized-compactness distinction. Input y'=y+t-t' corresponds
to the operator T_(t'-t), under T_delta f(y)=f(y-delta). No range derivative,
global graph compact resolvent or normal index is inferred from the picture.

Read COMPONENT-TERMS.md, FONT-NOTICE.txt, both font notices and all retained
software notices for the separately scoped actual component terms. Original
proof/caption/generator/checker expression is CC0 1.0. No protected source
expression or pixels, private audit receipts, or dependency binaries are
included.
