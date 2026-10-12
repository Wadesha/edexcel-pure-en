# -*- coding: utf-8 -*-
"""生成入口页 index.html。"""
import os
from _common import BASE, CONTENT, TOPICS, GROUP_TITLE, CSS, md_to_html, parse_topic, slug, MJAX_HEAD, verify_mathjax
from _build_slides import build_deck


def build():
    data = []
    for fn, grp, label in TOPICS:
        d = parse_topic(os.path.join(CONTENT, fn))
        d['group'] = grp
        d['key'] = slug(fn.replace('.md', ''))
        d['n_ex'] = len(d['examples'])
        d['n_q'] = len(d['questions'])
        data.append(d)

    tot_ex = sum(d['n_ex'] for d in data)
    tot_q = sum(d['n_q'] for d in data)
    tot_sl = sum(len(build_deck(d)['slides']) for d in data)

    groups = []
    present = list(dict.fromkeys(d['group'] for d in data))
    for g in present:
        rows = ''.join(
            '<tr><td><a href="guide.html#%s">%s</a></td><td>%d</td>'
            '<td><a href="practice.html" onclick="sessionStorage.setItem(\'deck\',\'%s\')">%d Qs</a></td>'
            '<td><a href="slides.html" onclick="sessionStorage.setItem(\'deck\',\'%s\')">Slides</a></td></tr>'
            % (d['key'], d['title'], d['n_ex'], d['key'], d['n_q'], d['key'])
            for d in data if d['group'] == g)
        groups.append('<h3>%s</h3><table><thead><tr><th>Topic</th><th>Examples</th><th>Exercises</th><th>Slides</th></tr></thead>'
                      '<tbody>%s</tbody></table>' % (GROUP_TITLE[g], rows))

    html = f"""<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Edexcel Pure Maths &middot; Learning Kit</title>
{MJAX_HEAD}
<link rel="stylesheet" href="_theme.css">
<style>
.cards{{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px;margin:18px 0}}
.card{{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:18px 20px}}
.card:hover{{border-color:var(--acc)}}
.card h3{{margin:0 0 6px;color:var(--acc);font-size:17px}}
.card p{{color:var(--dim);font-size:13.5px;margin:4px 0 0}}
.stat{{display:flex;gap:22px;flex-wrap:wrap;margin:12px 0}}
.stat div{{background:var(--panel);border:1px solid var(--line);border-radius:10px;padding:10px 16px}}
.stat b{{display:block;font-size:22px;color:var(--acc2)}}
.stat span{{font-size:12.5px;color:var(--dim)}}
</style></head>
<body>
<div class="wrap">
<div class="side">
  <h1>Edexcel Pure Maths<br>Study Kit</h1>
  <div class="sub">Edexcel A-Level Mathematics · 9MA0</div>
  <div class="grp">Four pages</div>
  <a class="item" href="slides.html">① Class slides</a>
  <a class="item" href="guide.html">② Study guide</a>
  <a class="item" href="formula.html">③ Formula book</a>
  <a class="item" href="practice.html">④ Practice</a>
  <div class="grp" style="margin-top:16px">Topic index</div>
  {''.join('<a class="item" href="guide.html#%s">%s</a>' % (d['key'], d['title']) for d in data)}
</div>
<div class="main">
<div class="hero">
<h1>Edexcel Pure Maths &middot; Study Kit</h1>
<div class="meta">Pearson Edexcel A-Level Mathematics (9MA0) &middot; Pure Paper 1<br>
Five foundational Pure topics: Proof, Indices &amp; Surds, Quadratics, Simultaneous Equations.<br>
Notes in English; Edexcel terminology kept in its original form. Formulae rendered with MathJax, fully offline.</div>
</div>

<div class="stat">
<div><b>{len(data)}</b><span>Topics</span></div>
<div><b>{tot_ex}</b><span>Worked examples</span></div>
<div><b>{tot_q}</b><span>Practice questions</span></div>
<div><b>{tot_sl}</b><span>Slides</span></div>
<div><b>P1</b><span>Pure Paper 1</span></div>
</div>

<div class="cards">
<a class="card" href="slides.html" style="color:inherit">
  <h3>① Class slides</h3>
  <p>{tot_sl} slides (5 topics): concept &rarr; examples (question first, then solution) &rarr; in-class exercises. Full-screen projection, keyboard navigation, Ctrl+P to print a PDF handout.</p>
</a>
<a class="card" href="guide.html" style="color:inherit">
  <h3>② Study guide</h3>
  <p>Five topics explained: specification checklist + worked notes + example solutions. Sidebar TOC; example solutions collapse/expand with one click.</p>
</a>
<a class="card" href="formula.html" style="color:inherit">
  <h3>③ Formula book</h3>
  <p>What the exam provides vs what you must memorise for these five topics: index laws, surd rules, discriminant, completing the square, quadratic formula.</p>
</a>
<a class="card" href="practice.html" style="color:inherit">
  <h3>④ Practice</h3>
  <p>Play questions topic by topic; answers hidden by default; &larr; &rarr; to flip, Space for answer, Esc to return. For class projection and self-test.</p>
</a>
</div>

<h2>Where these topics sit</h2>
<table>
<thead><tr><th>Qualification</th><th>Pure component</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>A-Level (9MA0)</td><td>Paper 1, Paper 2, Paper 3 &mdash; Pure Mathematics</td><td>Three 2-hour, 100-mark Pure papers; these five topics are core Paper 1 material.</td></tr>
<tr><td>AS (8MA0)</td><td>Paper 1 &mdash; Pure Mathematics</td><td>One 2-hour, 100-mark Pure paper; same core topics.</td></tr>
</tbody></table>
<p class="note">All papers permit a calculator; the formulae booklet is provided. These five topics are foundational Pure content examined across the Pure papers.</p>

<h2>Topic index</h2>
{''.join(groups)}

<div class="footer">
Source: Pearson Edexcel A-Level Mathematics (9MA0) specification. The explanations, worked examples and exercises on this site are original study write-ups and are not affiliated with or endorsed by Pearson.
</div>
</div></div>
</body></html>"""

    out = os.path.join(BASE, 'index.html')
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    print('written', out, len(html))
    verify_mathjax(out)


if __name__ == '__main__':
    build()
