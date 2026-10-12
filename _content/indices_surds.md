# Indices & Surds

> Edexcel A-Level Pure Mathematics — Topic 2. Index laws let you simplify powers; surds let you work with exact irrational roots. Both appear throughout Pure and are tested on their own and inside harder algebra.

## Specification

- Use and apply the **laws of indices** to simplify and manipulate expressions involving powers.
- Change the base of a term to simplify expressions with different bases.
- Understand a **surd** as an irrational root and simplify surd expressions.
- **Rationalise the denominator** of a fraction involving surds.

## Notes

### Laws of indices

Index laws let you simplify and manipulate expressions involving powers. Note: "index" is the singular, "indices" the plural. The laws only work for terms that share the **same base**.

- $a^{x}\times a^{y}=a^{x+y}$
- $a^{x}\div a^{y}=a^{x-y}$
- $(a^{x})^{y}=a^{x y}$

**Changing the base.** When terms have different bases, rewrite one base to match the other. For example, $9^{4}=(3^{2})^{4}=3^{8}$, so $9^{4}\div 3^{7}=3^{8}\div 3^{7}=3^{1}=3$.

### Manipulating surds

A **surd** is an irrational root — for instance $\sqrt{n}$ where $n$ is a positive integer that is not a perfect square. Surds are examples of irrational numbers.

- $\sqrt{a}\,\sqrt{b}=\sqrt{ab}$
- $\dfrac{\sqrt{a}}{\sqrt{b}}=\sqrt{\dfrac{a}{b}}$

When simplifying, **look for square factors**: $\sqrt{12}=\sqrt{4\times3}=2\sqrt{3}$.
You can collect like surds just as you collect like letters: $3\sqrt{2}+5\sqrt{2}=8\sqrt{2}$. But do not confuse this with the multiplication/division rules — you cannot add "under the surd", since $\sqrt{2}+\sqrt{3}\neq\sqrt{5}$.

Leaving an answer in exact surd form is often required; it avoids the rounding error you would get from carrying an approximation like $7.07$ forward into later working.

### Rationalising the denominator

Rationalising turns a fraction with a surd in its denominator into an equal fraction whose denominator is rational (usually an integer), with any surd moved up to the numerator.

- **Single surd:** multiply top and bottom by that surd — $\dfrac{1}{\sqrt{b}}=\dfrac{\sqrt{b}}{b}$.
- **Binomial with a surd:** multiply top and bottom by the **conjugate** — $\dfrac{1}{a+\sqrt{b}}=\dfrac{a-\sqrt{b}}{a^{2}-b}$.

Note: "in the form $p+q\sqrt{3}$ where $p$ and $q$ are rational" does **not** mean $p$ and $q$ must be integers or positive — rationals include fractions and negatives.

## Examples

### Example 1 (Indices: same base)

Simplify $8^{5}\times 2^{-3}\div 4^{2}$.

**Solution**

Rewrite every base as $2$: $8=2^{3}$ and $4=2^{2}$.
$$8^{5}\times 2^{-3}\div 4^{2}=(2^{3})^{5}\times 2^{-3}\div(2^{2})^{2}=2^{15}\times 2^{-3}\div 2^{4}=2^{15-3-4}=2^{8}=256.$$

### Example 2 (Surds: simplification)

Simplify $\sqrt{50}+3\sqrt{8}-2\sqrt{18}$.

**Solution**

$$\sqrt{50}=\sqrt{25\times2}=5\sqrt{2},\qquad 3\sqrt{8}=3\sqrt{4\times2}=6\sqrt{2},\qquad 2\sqrt{18}=2\sqrt{9\times2}=6\sqrt{2}.$$
So $5\sqrt{2}+6\sqrt{2}-6\sqrt{2}=5\sqrt{2}$.

### Example 3 (Rationalising)

Write $\dfrac{5}{2+\sqrt{3}}$ in the form $a+b\sqrt{3}$ with $a,b$ rational.

**Solution**

Multiply numerator and denominator by the conjugate $2-\sqrt{3}$:
$$\frac{5}{2+\sqrt{3}}=\frac{5(2-\sqrt{3})}{(2+\sqrt{3})(2-\sqrt{3})}=\frac{10-5\sqrt{3}}{4-3}=10-5\sqrt{3}.$$
So $a=10$ and $b=-5$.

## Exercises

**Q1.** Simplify $3^{4}\times 3^{2}\div 3^{5}$.

**A1.** $3^{4+2-5}=3^{1}=3$.

**Q2.** Simplify $(2^{3})^{4}\div 2^{5}$.

**A2.** $2^{12}\div 2^{5}=2^{7}=128$.

**Q3.** Simplify $\sqrt{45}$.

**A3.** $\sqrt{45}=\sqrt{9\times5}=3\sqrt{5}$.

**Q4.** Simplify $2\sqrt{12}-3\sqrt{3}$.

**A4.** $2\sqrt{12}=2\sqrt{4\times3}=4\sqrt{3}$; $4\sqrt{3}-3\sqrt{3}=\sqrt{3}$.

**Q5.** Write $\dfrac{1}{\sqrt{5}}$ with a rational denominator.

**A5.** $\dfrac{1}{\sqrt{5}}=\dfrac{\sqrt{5}}{5}$.

**Q6.** Write $\dfrac{3}{1-\sqrt{2}}$ in the form $a+b\sqrt{2}$ with rational $a,b$.

**A6.** $\dfrac{3(1+\sqrt{2})}{(1-\sqrt{2})(1+\sqrt{2})}=\dfrac{3+3\sqrt{2}}{1-2}=-3-3\sqrt{2}$. So $a=-3$, $b=-3$.

**Q7.** Write $\dfrac{4}{\sqrt{3}+1}$ in the form $a+b\sqrt{3}$ with rational $a,b$.

**A7.** $\dfrac{4(\sqrt{3}-1)}{(\sqrt{3}+1)(\sqrt{3}-1)}=\dfrac{4\sqrt{3}-4}{3-1}=2\sqrt{3}-2$. So $a=-2$, $b=2$.

**Q8.** Simplify $9^{3}\div 3^{4}$.

**A8.** $9^{3}=(3^{2})^{3}=3^{6}$; $3^{6}\div3^{4}=3^{2}=9$.
