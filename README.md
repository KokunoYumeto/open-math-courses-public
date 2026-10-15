# Open Mathematics Courses

A growing mathematics library for independent study and teaching: lessons with complete arguments, worked examples,
solved exercises and editable sources, from graduate foundations to research topics.

[Read online](https://kokunoyumeto.github.io/open-math-courses-public/)

## Contents

The [course list](https://kokunoyumeto.github.io/open-math-courses-public/) groups the courses by subject. Lessons name their prerequisites and link the earlier
lessons that prove them where such lessons exist. Some lessons use results whose proofs are not yet written in these
courses.

The lessons are also available as a dataset, one row per lesson:
[KokunoYumeto/open-math-courses](https://huggingface.co/datasets/KokunoYumeto/open-math-courses) on Hugging Face.

## Why these courses

**Translation and reuse.** AI systems can translate mathematical writing well, but many mathematical texts are hard to
use this way: some licences do not allow derivative works such as translations, and many texts exist only as scanned
pages. These lessons are independent expositions that cite the works they draw on, and they are dedicated to the
public domain (CC0). Anyone, person or machine, may translate, adapt, excerpt and reuse them, including in ways that a
no-derivatives licence would not allow.

**One connected body of mathematics.** The courses are lesson series for study and teaching, and they are linked to
each other: a lesson names the earlier lessons whose results it uses. Following these links shows how results in
different areas depend on one another.

**New results in context.** A new result can be added with its prerequisites and its uses, so that its consequences
for other areas are easier to find, and AI systems can carry it through the connected material. OpenAI's 2026 release
of 719 manuscripts in 372 families of results is an example: courses on several of these families work through the
proofs and link them to the courses they build on.

**Review.** Writing a lesson means working through every step of an argument, so the work also acts as a review. When
it finds a gap or an error in a published argument, the lesson proves a corrected statement.

These aims match uses of AI in mathematics that Terence Tao lists in his talk "Math 2.0" (Caltech, 2026): explaining
results whose known proofs are opaque ("open exposition problems"), collating research papers into a living network
of results, and writing well-organized texts that synthesize many results of a theory
([slides](https://teorth.github.io/tao-web/slides/math-2-0-caltech-2026.pdf), slides 22 and 26).

Further reasons, from Claude (Anthropic), which writes many of these lessons:

- In the courses Claude writes, each lesson separates what it proves from what it assumes: a result used without
  proof is stated exactly, with free references, and recorded as an open obligation. A reader can see what a theorem
  rests on.
- The gaps become a work list. When several courses assume the same standard result, one foundation lesson that
  proves it closes the gap in all of them.
- The sources are plain Markdown with TeX and stable links between lessons, so they can be checked by programs
  (formulas, links, numerical checks of identities) and later connected to formal proofs.

## What we would like to do next

- Treat more of mathematics in the same way, with complete arguments and links between courses.
- Integrate more of the research literature, from arXiv and other open sources, so that the lessons cite and use as
  much of it as possible.
- Translate the lessons into more languages. An AI translator reads every argument again, so each translation is also
  a further check.

## Authorship and licences

Each lesson states who wrote it and how it was checked. Lessons were written by AI systems (Claude Opus 5.5 by
Anthropic; GPT-6 Astra and GPT-6.1 Sol by OpenAI) and build on credited human work, cited in each lesson.
Every file in this repository is marked [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/) (public
domain); lessons that contain text under other licences are not part of this edition. The pages load the MathJax and
KaTeX formula renderers from the jsDelivr CDN.

## Support

The courses are free to read, copy and translate. Sponsorship pays for the computing that writes and checks them. [Sponsor this work](https://github.com/sponsors/KokunoYumeto).
