# -*- coding: utf-8 -*-
"""Generate the formula-book page formula.html for the 5 Edexcel Pure topics.
Focused on what the exam provides vs what must be memorised for these topics.
"""
import os
from _common import BASE, CSS, MJAX_HEAD, verify_mathjax

# ---------- Data ----------
# (group, [(subsection, [(label, formula/text)])])
BOOKLET = [
    ('Provided in the formula booklet', [
        ('quadratic formula', r'ax^{2}+bx+c=0\ \Rightarrow\ x=\frac{-b\pm\sqrt{b^{2}-4ac}}{2a}'),
    ]),
]

RECALL = [
    ('Proof notation', [
        (r'\mathbb{N}', 'the set of natural numbers'),
        (r'\mathbb{Z}', 'the set of integers'),
        (r'\mathbb{Q}', 'the set of rational numbers'),
        (r'\mathbb{R}', 'the set of real numbers'),
        ('LHS / RHS', 'left-hand side / right-hand side of an equation or identity'),
    ]),
    ('Laws of indices', [
        (r'a^{x} \times a^{y}', r'a^{x+y}'),
        (r'a^{x} \div a^{y}', r'a^{x-y}'),
        (r'(a^{x})^{y}', r'a^{x y}'),
        ('change of base', r'9^{4} = (3^{2})^{4} = 3^{8}'),
    ]),
    ('Surds', [
        (r'\sqrt{a}\,\sqrt{b}', r'\sqrt{ab}'),
        (r'\frac{\sqrt{a}}{\sqrt{b}}', r'\sqrt{\frac{a}{b}}'),
        (r'(\sqrt{a})^{2}', r'a'),
        ('rationalise (single surd)', r'\frac{1}{\sqrt{b}}=\frac{\sqrt{b}}{b}'),
        ('rationalise (binomial)', r'\frac{1}{a+\sqrt{b}}=\frac{a-\sqrt{b}}{a^{2}-b}'),
    ]),
    ('Quadratics', [
        ('discriminant', r'\Delta = b^{2}-4ac'),
        ('three cases', r'\Delta>0:\ 2\ real\ roots;\quad \Delta=0:\ 1\ repeated\ root;\quad \Delta<0:\ no\ real\ roots'),
        ('completing the square', r'y=a(x+p)^{2}+q,\quad p=\frac{b}{2a},\quad q=c-\frac{b^{2}}{4a}'),
        ('turning point', r'(-p,\ q)'),
    ]),
]

TOC = [
    ('booklet', '1 · Provided in the booklet'),
    ('recall', '2 · Must memorise'),
    ('methods', '3 · Solving methods'),
]


def cell(s):
    """Wrap cells containing LaTeX markers in a display formula; otherwise plain text."""
    s = html_escape(s)
    if '\\' in s or '^' in s or '_' in s:
        return '$$%s$$' % s
    return s


def html_escape(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))


def table(items):
    rows = ''.join('<tr><td class="lb">%s</td><td>%s</td></tr>' % (cell(lb), cell(fx))
                   for lb, fx in items)
    return '<table class="fx"><tbody>%s</tbody></table>' % rows


def render_group(groups):
    """Accepts (group, [(label, formula/text), ...])."""
    out = []
    for gname, items in groups:
        out.append('<h3>%s</h3>' % gname)
        out.append(table(items))
    return ''.join(out)


def main():
    booklet_html = render_group(BOOKLET)
    recall_html = render_group(RECALL)
    toc = ''.join('<a href="#%s">%s</a>' % (i, t) for i, t in TOC)

    html = f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Edexcel Pure Maths &middot; Formula Book</title>
{MJAX_HEAD}
<link rel="stylesheet" href="_theme.css">
<style>
table.fx{{width:100%;font-size:15px}}
table.fx td{{border:1px solid var(--line);padding:7px 10px;vertical-align:middle}}
table.fx td.lb{{width:34%;color:var(--dim);background:var(--panel2)}}
.tocbar{{display:flex;gap:10px;flex-wrap:wrap;margin:10px 0 18px}}
.tocbar a{{background:var(--panel2);border:1px solid var(--line);border-radius:6px;padding:5px 10px;font-size:13px}}
.method{{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:14px 18px;margin:12px 0}}
.method ol{{margin-left:18px}}
.method li{{margin:6px 0}}
</style></head>
<body>
<div class="wrap">
<div class="side">
  <h1>Edexcel Pure Maths<br>Formula Book</h1>
  <div class="sub">For the 5 Pure topics</div>
  <div class="grp">On this page</div>
  {toc}
  <div class="grp" style="margin-top:16px">Other pages</div>
  <a class="item" href="index.html">&larr; Home</a>
  <a class="item" href="slides.html">Class slides</a>
  <a class="item" href="guide.html">Study guide</a>
  <a class="item" href="practice.html">Practice</a>
</div>
<div class="main">
<div class="hero">
<h1>Formula Book</h1>
<div class="meta">
Following the Pearson Edexcel A-Level (9MA0) formula booklet and specification:
<b>Part 1</b> is given in the exam booklet (do not memorise), <b>Part 2</b> is what you must know by heart.
</div>
</div>

<h2 id="booklet">1 &middot; Provided in the booklet</h2>
<p class="note">Given with the question paper. You do not need to memorise it, but you must know when and how to use it.</p>
{booklet_html}

<h2 id="recall">2 &middot; Must memorise</h2>
<p class="note">The specification lists these as "students should know"; they do not appear in the booklet.
Index laws, surd rules, the discriminant and completing the square all belong here.</p>
{recall_html}

<h2 id="methods">3 &middot; Solving methods</h2>
<p class="note">These are procedures rather than single formulae &mdash; learn the steps and practise them.</p>

<div class="method">
<h4>Linear simultaneous equations &mdash; elimination</h4>
<ol>
<li>Multiply one (or both) equations by constants so the coefficients of one unknown match.</li>
<li>If the matching coefficients have the <em>same</em> sign, subtract the equations; if <em>different</em> signs, add them.</li>
<li>Solve the resulting equation for one unknown.</li>
<li>Substitute that value into an original equation to find the other unknown.</li>
<li>Check by substituting both values into the equation you did not use in step 4.</li>
</ol>
</div>

<div class="method">
<h4>Linear simultaneous equations &mdash; substitution</h4>
<ol>
<li>Rearrange one equation to make one unknown the subject.</li>
<li>Substitute that expression into the other equation.</li>
<li>Solve for the remaining unknown.</li>
<li>Substitute back to find the first unknown.</li>
<li>Check both values in the original equation you rearranged in step 1.</li>
</ol>
</div>

<div class="method">
<h4>Quadratic simultaneous equations</h4>
<p>One equation is quadratic, the other linear. You <strong>must</strong> use substitution:</p>
<ol>
<li>Rearrange the linear equation to make one unknown the subject.</li>
<li>Substitute into the quadratic equation.</li>
<li>Solve the resulting quadratic (usually two values).</li>
<li>Substitute each value back to find the matching other unknown.</li>
<li>Check each pair in the original quadratic equation.</li>
</ol>
</div>

<div class="footer">
Formulae follow the Pearson Edexcel A-Level Mathematics (9MA0) formulae booklet and specification.
This page is an original study aid and is not affiliated with or endorsed by Pearson.
</div>
</div></div>
</body></html>"""

    out = os.path.join(BASE, 'formula.html')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    print('written', out, len(html))
    verify_mathjax(out)


if __name__ == '__main__':
    main()
