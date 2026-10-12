# Quadratics

> Edexcel A-Level Pure Mathematics — Topic 3. Quadratics cover the graph of $y=ax^2+bx+c$, the discriminant, completing the square, solving by factorising / formula / square-completion, and "hidden" quadratics solved by substitution.

## Specification

- Sketch quadratic graphs and find their intercepts and turning point.
- Use the **discriminant** $b^2-4ac$ to determine the number of real roots and to solve related inequalities.
- **Complete the square** and use it to locate the turning point.
- Solve quadratic equations by factorising, completing the square, and the quadratic formula.
- Solve **hidden quadratics** using a substitution.

## Notes

### Quadratic graphs

The general equation is $y=ax^2+bx+c$. Its shape is a **parabola**. If $a>0$ it opens upward $(\cup)$; if $a<0$ it opens downward $(\cap)$.

From the equation you should be able to:
- sketch the graph, possibly after rearranging into $y=ax^2+bx+c$;
- read off the axis intercepts;
- factorise (when possible) to find the roots;
- find the coordinates of the turning point (maximum or minimum).

### The discriminant

The **discriminant** is the part under the square root in the quadratic formula: $b^2-4ac$. It is often written $\Delta$.

- $\Delta>0$: the graph crosses the $x$-axis twice → two distinct real roots.
- $\Delta=0$: the graph touches the $x$-axis once → one repeated real root.
- $\Delta<0$: the graph does not cross the $x$-axis → no real roots.

When a question mentions only "real roots", it means **distinct or repeated** (not complex), so you solve $\Delta\ge 0$. For inequalities, sketch the quadratic and decide whether you need the region above or below zero.

### Completing the square

This rewrites $y=ax^2+bx+c$ as $y=a(x+p)^2+q$.

- When $a=1$: $p=\dfrac{b}{2}$ and $q=c-p^2$.
- When $a\neq 1$: factor $a$ out of the $x^2$ and $x$ terms first, then proceed.

It is useful for finding the turning point $(-p,\,q)$, for building a quadratic from its turning point, and for proving results that rely on a squared term always being $\ge 0$.

### Solving quadratic equations

First write the equation as $ax^2+bx+c=0$. The three methods are **factorising**, **completing the square**, and the **quadratic formula**. Factorising is fastest but does not always work; the other two always work. A calculator may give the roots, but method marks still matter.

### Hidden quadratics

A **hidden quadratic** is a quadratic in a function $f(x)$: $a[f(x)]^2+b[f(x)]+c=0$. Substitute $u=f(x)$, solve the ordinary quadratic for $u$, then substitute back. For example, $\sin^2x+2\sin x-3=0$ is the hidden quadratic $u^2+2u-3=0$ with $u=\sin x$.

## Examples

### Example 1 (Discriminant)

Find the values of $k$ for which $x^2+kx+4=0$ has exactly one real root.

**Solution**

Exactly one real root means $\Delta=0$:
$$k^2-4(1)(4)=0\quad\Rightarrow\quad k^2=16\quad\Rightarrow\quad k=\pm 4.$$

### Example 2 (Completing the square)

Write $x^2-6x+2$ as $(x+p)^2+q$ and state its turning point.

**Solution**

$p=-\dfrac{6}{2}=-3$; $q=2-(-3)^2=2-9=-7$. So
$$x^2-6x+2=(x-3)^2-7.$$
The turning point is $(3,-7)$, a minimum because $a=1>0$.

### Example 3 (Hidden quadratic)

Solve $\sin^2x+2\sin x-3=0$ for $0\le x\le 2\pi$.

**Solution**

Let $u=\sin x$. Then $u^2+2u-3=0=(u+3)(u-1)$, so $u=-3$ or $u=1$.
$\sin x=-3$ is impossible (sine lies in $[-1,1]$). $\sin x=1$ gives $x=\dfrac{\pi}{2}$ in the range.
Solution: $x=\dfrac{\pi}{2}$.

## Exercises

**Q1.** For what values of $k$ does $x^2-4x+k=0$ have two distinct real roots?

**A1.** $\Delta=16-4k>0$ ⇒ $k<4$.

**Q2.** Find the discriminant of $2x^2-3x+1=0$ and state how many real roots it has.

**A2.** $\Delta=9-8=1>0$ → two distinct real roots.

**Q3.** Complete the square for $x^2+4x-1$ and state the turning point.

**A3.** $(x+2)^2-5$. Turning point $(-2,-5)$.

**Q4.** Solve $x^2-5x+6=0$ by factorising.

**A4.** $(x-2)(x-3)=0$ ⇒ $x=2$ or $x=3$.

**Q5.** Solve $2x^2+5x-12=0$ using the quadratic formula.

**A5.** $x=\dfrac{-5\pm\sqrt{25+96}}{4}=\dfrac{-5\pm11}{4}$ ⇒ $x=\dfrac{3}{2}$ or $x=-4$.

**Q6.** Solve $x^2+4x-7=0$ by completing the square, giving surd form.

**A6.** $(x+2)^2-11=0$ ⇒ $(x+2)^2=11$ ⇒ $x=-2\pm\sqrt{11}$.

**Q7.** Solve $e^{2x}-5e^x+6=0$ (a hidden quadratic with $u=e^x$).

**A7.** $u^2-5u+6=0=(u-2)(u-3)$ ⇒ $e^x=2$ or $e^x=3$ ⇒ $x=\ln2$ or $x=\ln3$.

**Q8.** Write $2x^2-8x+5$ in the form $a(x+p)^2+q$.

**A8.** $2(x^2-4x)+5=2[(x-2)^2-4]+5=2(x-2)^2-3$.
