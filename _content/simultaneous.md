# Simultaneous Equations

> Edexcel A-Level Pure Mathematics — Topic 4. Simultaneous equations involve more than one equation in more than one unknown. Linear pairs are solved by elimination or substitution; a quadratic paired with a linear equation is solved by substitution only.

## Specification

- Solve **linear** simultaneous equations using **elimination** and **substitution**.
- Solve **quadratic** simultaneous equations (one quadratic, one linear) using substitution.

## Notes

### Linear simultaneous equations

You have more than one equation in more than one unknown. An equation is **linear** when no unknown is raised to a power other than $1$. Solving the pair means finding values that make both equations true at the same time. A pair of linear equations graphs as two straight lines that cross (when a solution exists).

### Solving linear equations by elimination

1. Multiply one (or both) equations by a constant so the coefficients of one unknown match.
2. If the matching coefficients have the **same** sign, subtract the equations; if **opposite** signs, add them.
3. Solve the new equation for one unknown.
4. Substitute that value into an original equation to find the other unknown.
5. Check by substituting both values into the equation you did **not** use in step 4.

Mishandling minus signs is the single most common error here — never skip the checking step.

### Solving linear equations by substitution

1. Rearrange one equation to make one unknown the subject.
2. Substitute that expression into the other equation.
3. Solve for the remaining unknown.
4. Substitute back to find the first unknown.
5. Check using the equation you rearranged in step 1.

Either method always works for a linear pair; substitution is also the one you need for quadratic pairs.

### Quadratic simultaneous equations

One equation is quadratic, the other linear. You **must** use substitution (elimination will not work):

1. Rearrange the linear equation to make one unknown the subject.
2. Substitute into the quadratic equation.
3. Solve the resulting quadratic (usually two values).
4. Substitute each value back to find the matching other unknown.
5. Check each pair in the original quadratic equation.

There are usually two solution pairs, but there can be one or none.

## Examples

### Example 1 (Linear: elimination)

Solve $x+y=10$ and $2x-y=5$.

**Solution**

Add the equations to eliminate $y$:
$$(x+y)+(2x-y)=10+5\quad\Rightarrow\quad 3x=15\quad\Rightarrow\quad x=5.$$
Substitute into $x+y=10$: $5+y=10$ ⇒ $y=5$.
Check in $2x-y=5$: $2(5)-5=5$ ✓.
Solution: $x=5$, $y=5$.

### Example 2 (Linear: substitution)

Solve $x=2y+1$ and $x+y=7$.

**Solution**

Substitute $x=2y+1$ into $x+y=7$:
$$(2y+1)+y=7\quad\Rightarrow\quad 3y=6\quad\Rightarrow\quad y=2.$$
Then $x=2(2)+1=5$.
Check in $x+y=7$: $5+2=7$ ✓.
Solution: $x=5$, $y=2$.

### Example 3 (Quadratic simultaneous)

Solve $y=x^2-4$ and $y=3x$.

**Solution**

Substitute $y=3x$ into the quadratic:
$$3x=x^2-4\quad\Rightarrow\quad x^2-3x-4=0\quad\Rightarrow\quad (x-4)(x+1)=0.$$
So $x=4$ or $x=-1$.
If $x=4$, $y=12$; if $x=-1$, $y=-3$.
Check each in $y=x^2-4$: $12=16-4$ ✓, and $-3=1-4$ ✓.
Solutions: $(4,12)$ and $(-1,-3)$.

## Exercises

**Q1.** Solve by elimination: $x+y=9$, $x-y=3$.

**A1.** Add: $2x=12$ ⇒ $x=6$; then $y=3$. Check: $6-3=3$ ✓.

**Q2.** Solve by substitution: $y=2x-1$, $x+y=5$.

**A2.** $x+(2x-1)=5$ ⇒ $3x=6$ ⇒ $x=2$; $y=3$. Check: $2+3=5$ ✓.

**Q3.** Solve $3x+2y=12$ and $x-y=1$.

**A3.** From the second, $x=y+1$. Substitute: $3(y+1)+2y=12$ ⇒ $5y+3=12$ ⇒ $y=\dfrac{9}{5}$; then $x=\dfrac{14}{5}$. Check: $\dfrac{42}{5}+\dfrac{18}{5}=12$ ✓.

**Q4.** Solve $2x+3y=17$ and $3x-2y=6$.

**A4.** Multiply the first by $2$ and the second by $3$: $4x+6y=34$, $9x-6y=18$. Add: $13x=52$ ⇒ $x=4$; then $2(4)+3y=17$ ⇒ $y=3$. Check second: $12-6=6$ ✓.

**Q5.** Solve the quadratic pair: $y=x^2-1$ and $y=2x+2$.

**A5.** $2x+2=x^2-1$ ⇒ $x^2-2x-3=0=(x-3)(x+1)$ ⇒ $x=3$ ⇒ $y=8$; $x=-1$ ⇒ $y=0$. Solutions $(3,8)$ and $(-1,0)$.

**Q6.** Solve $y=4-x$ and $x^2+y=10$.

**A6.** Substitute $y=4-x$: $x^2+4-x=10$ ⇒ $x^2-x-6=0=(x-3)(x+2)$ ⇒ $x=3$ ⇒ $y=1$; $x=-2$ ⇒ $y=6$. Solutions $(3,1)$ and $(-2,6)$.

**Q7.** Solve $x+y=6$ and $xy=8$.

**A7.** From the first, $y=6-x$. Substitute: $x(6-x)=8$ ⇒ $x^2-6x+8=0$ ⇒ $(x-2)(x-4)=0$ ⇒ $x=2$ ⇒ $y=4$; $x=4$ ⇒ $y=2$. Solutions $(2,4)$ and $(4,2)$.
