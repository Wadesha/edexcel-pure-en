# Proof · Mathematical Proof

> Edexcel A-Level Pure Mathematics — Topic 1. A proof is a logical argument that shows a statement is true (or false) for every value in a specified set. This topic underpins later Pure work and appears across the Pure papers.

## Specification

- Understand and use the structure of mathematical proof, including **proof by deduction**, **proof by exhaustion** and **disproof by counter example**.
- Use correct mathematical language and notation for proof (e.g. integer $\mathbb{Z}$, constant, variable, equation, identity).
- Distinguish an **equation** (true for some values, must be solved) from an **identity** (true for all allowed values, written with $\equiv$).

## Notes

### What is a proof?

A proof is a sequence of logical steps that shows whether a result is true or not for a specified set of numbers — for example, all integers, or all even numbers. Testing a few values gives *evidence*, not proof.

A standard proof has three parts:

1. **Assumptions** — what you are given (e.g. "$n$ is an integer").
2. **Logical steps** — each step follows from the previous one using definitions, known identities, or algebraic rules.
3. **Conclusion** — state clearly "therefore the result holds for all …".

Key vocabulary: an *equation* is true only for certain values and must be **solved** (e.g. $x^2=4$); an *identity* is true for every allowed value and is written with $\equiv$ (e.g. $\sin^2\theta+\cos^2\theta\equiv 1$). You can solve an equation, but you cannot "solve" an identity.

### Notation in proof

- $\mathbb{N}$: the set of natural numbers.
- $\mathbb{Z}$: the set of integers.
- $\mathbb{Q}$: the set of rational numbers.
- $\mathbb{R}$: the set of real numbers.
- **LHS** and **RHS** are abbreviations for *left-hand side* and *right-hand side*.

### Proof by deduction

Start from general assumptions and use algebra to reach the conclusion. The key trick is usually to write a **general term** and factorise or rearrange it into a form whose property is obvious.

For example, to show $n^2+n$ is even for any integer $n$:

$$n^2+n=n(n+1)$$

$n$ and $n+1$ are consecutive integers, so one of them is even, and the product is even.

### Proof by exhaustion

Check **every** allowed value — not just a few. This is only practical when the number of cases is finite and small.

- To show a number is prime, you only need to test factors up to its square root.
- Exhaustion proves the statement only for the cases you actually list; widen the range and it may fail.

### Disproof by counter example

To disprove "the statement holds for all …", you need only find **one** value that makes it false. That value is a **counter example**. It must lie inside the claimed set, and you must *verify* that it really breaks the statement.

Helpful places to look: zero, negatives, and (in trigonometry) angles that share the same sine value.

### Common pitfalls

- Treating "three examples work" as a proof.
- Forgetting to state the range of the variable ($n$ an integer? a real number?).
- Replacing a real step with "obviously" or "clearly".

## Examples

### Example 1 (Deduction: parity)

Prove that, for any integer $n$, $n^2+3n$ is even.

**Solution**

$$n^2+3n=n(n+3)$$

If $n$ is even, write $n=2k$; then $n(n+3)=2k(2k+3)$, which has a factor $2$, so it is even.
If $n$ is odd, then $n+3$ is even; write $n+3=2m$; then $n(n+3)=2mn$, which is even.
Both cases give an even number, so $n^2+3n$ is even for every integer $n$. $\square$

(Shortcut: $n$ and $n+3$ differ by $3$, an odd number, so they have opposite parity; one is even, hence the product is even.)

### Example 2 (Identity)

Prove that, for $x\neq 1$, $\dfrac{x^2-1}{x-1}-x\equiv 1$.

**Solution**

$$\frac{x^2-1}{x-1}-x=\frac{(x-1)(x+1)}{x-1}-x=(x+1)-x=1$$

The expression equals $1$ for every $x\neq 1$, so it is an identity. $\square$

### Example 3 (Counter example)

Statement: "For all real $x$, $(x+2)^2>x^2+4$." Decide whether it is true; if not, give a counter example.

**Solution**

$(x+2)^2=x^2+4x+4$. The claim becomes $x^2+4x+4>x^2+4$, i.e. $4x>0$, i.e. $x>0$.
So the statement is false for any $x\le 0$. Counter example: $x=0$ gives LHS $=4$, RHS $=4$, and $4>4$ is false. $\square$

## Exercises

**Q1.** Prove that, for any integer $n$, $n^3-n$ is divisible by $3$.

**A1.** $n^3-n=n(n-1)(n+1)$, the product of three consecutive integers. Among any three consecutive integers one is a multiple of $3$, so the product is divisible by $3$. $\square$

**Q2.** Prove that the sum of the squares of two odd integers is even but not divisible by $4$.

**A2.** Odd integers: $2a+1$, $2b+1$. $(2a+1)^2+(2b+1)^2=4a^2+4a+1+4b^2+4b+1=4(a^2+a+b^2+b)+2$, which is $4k+2$: even, and not a multiple of $4$. $\square$

**Q3.** Prove that, for any integer $n$, $n^2+n+1$ is odd.

**A3.** $n^2+n=n(n+1)$ is the product of two consecutive integers, hence even; write $n^2+n=2k$. Then $n^2+n+1=2k+1$, which is odd. $\square$

**Q4.** Give a counter example to: "For all real $x$ and $y$, if $x^2=y^2$ then $x=y$."

**A4.** Take $x=1$, $y=-1$. Then $x^2=y^2=1$ but $x\neq y$.

**Q5.** Prove by exhaustion that, for integer $n$ with $1\le n\le 5$, $n^2-n+11$ is prime.

**A5.** $n=1$: $11$; $n=2$: $13$; $n=3$: $17$; $n=4$: $23$; $n=5$: $31$ — all prime. $\square$

**Q6.** State, for each, whether it is an equation or an identity: $2(x+3)\equiv 2x+6$; $2(x+3)=10$.

**A6.** The first is an identity (true for all $x$, written with $\equiv$); the second is an equation (true only at $x=2$).

**Q7.** Prove that the difference between the squares of two consecutive integers is odd.

**A7.** Consecutive integers $n$ and $n+1$. $(n+1)^2-n^2=2n+1$, which is odd for every integer $n$. $\square$
