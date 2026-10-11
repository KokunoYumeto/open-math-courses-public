"""Row syntax regression from the lattice-counting course; synthetic path tests."""
import html
import unittest

from course_reader import render_markdown_math


class RowBreakPrivacyTests(unittest.TestCase):
    def test_unspaced_lattice_conditions_preserve_tex(self):
        formulas = [
            r'\sum_{\substack{x\ \text{primitive}\\R\leq|x|<2R}}g(x)^3',
            r'\sum_{\substack{A\in\mathcal E\\A\bmod h\in\mathcal O}}W(A)',
            r'\substack{a\\R\leq(x+1)}',
            r'\substack{a\\R\leq[x]}',
            r'\substack{a\\R\leq{x}}',
            r'\begin{aligned}x&=y\\A\bmod p^2\in\mathcal O\end{aligned}',
            r'\begin{matrix}x\\A\bmod p_1\notin\mathcal O\end{matrix}',
            r'\substack{x\\A\bmod p^{12}\equiv 0}',
        ]
        for formula in formulas:
            for left, right in (('$', '$'), (r'\(', r'\)'), ('$$\n', '\n$$'), (r'\[', r'\]')):
                source = left + formula + right
                with self.subTest(source=source):
                    self.assertIn('data-tex="' + html.escape(source, quote=True) + '"',
                                  render_markdown_math(source))

    def test_row_exception_does_not_admit_literal_paths(self):
        expressions = [
            r'\\server\share\Book.pdf',
            r'\substack{x\\server\share\Book}',
            r'\substack{x\\A\bmod\Book.pdf}',
            r'\substack{x\\A\bmod h\Private}',
            r'\substack{x}\quad\\A\bmod h\in\mathcal O',
            r'\substack{x}\quad\\R\leq|x|',
            r'\substack{\text{\\R\leq|x|}}',
            r'\begin{matrix}\texttt{\\A\bmod h\in\mathcal O}\end{matrix}',
            r'\begin{matrix}\verb|\\A\bmod h\in\mathcal O|\end{matrix}',
            r'\begin{matrix}\verb*+\\R\leq|x|+\end{matrix}',
            r'\substack{x\\R\leq\Book.pdf}',
            r'\substack{x\\A\bmod h\in\mathcal O}\quad D:' r'\Private\Book.pdf',
            r'\substack{x\\R\leq|x|}\quad\\server\share\Book',
        ]
        for expression in expressions:
            for left, right in (('$', '$'), (r'\(', r'\)'), ('$$\n', '\n$$'), (r'\[', r'\]')):
                with self.subTest(expression=expression), self.assertRaisesRegex(ValueError, 'local source'):
                    render_markdown_math(left + expression + right)


if __name__ == '__main__':
    unittest.main()
