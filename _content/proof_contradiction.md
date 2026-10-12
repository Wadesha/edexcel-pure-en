# Proof by Contradiction

> Edexcel A-Level Pure Mathematics — Topic 1 (extension of Proof). Assume the opposite of what you want to prove, then show this assumption leads to an impossible conclusion. The classic applications are the irrationality of $\sqrt{2}$ and the infinity of primes.

## Specification

- Understand and use **proof by contradiction**.
- Apply it to standard results, including the proof that $\sqrt{2}$ is irrational (and, as an extension, that there are infinitely many primes).
- Support algebraic steps with clear written explanation.

## Notes

### What is proof by contradiction?

Assume the **opposite** of the statement you want to prove is true. Then, through a chain of logical steps, show that this assumption leads to something impossible — a **contradiction**. Because the assumption cannot be true, the original statement must be true.

This method often mixes written sentences with algebra. A typical opening is:

> Assume, for contradiction, that …

The contradiction usually takes one of these forms:
- a number is forced to be both even and odd;
- two integers are shown to share a factor after we assumed they do not;
- a quantity is both rational and irrational.

### Using prime factorisation

For statements about divisibility or primes, write a number in terms of its prime factors. A clean contradiction often comes from the fact that an integer has a **unique** prime factorisation.

## Examples

### Example 1 (Irrationality of √2)

Prove that $\sqrt{2}$ is irrational.

**Solution**

Assume, for contradiction, that $\sqrt{2}$ is rational. Then we can write
$$\sqrt{2}=\frac{p}{q}$$
where $p$ and $q$ are integers with **no common factor**.

Squaring gives $2q^2=p^2$, so $p^2$ is even, and therefore $p$ is even. Write $p=2k$.
Then $2q^2=(2k)^2=4k^2$, so $q^2=2k^2$, and $q^2$ is even, so $q$ is even.

But now $p$ and $q$ are both even — they share a factor of $2$, contradicting "no common factor". Therefore $\sqrt{2}$ cannot be rational; it is irrational. $\square$

### Example 2 (Parity contradiction)

Prove that, if $n^2$ is even, then $n$ must be even.

**Solution**

Assume, for contradiction, that $n$ is odd. Then $n=2k+1$ for some integer $k$, and
$$n^2=(2k+1)^2=4k^2+4k+1=2(2k^2+2k)+1,$$
which is odd. This contradicts the given fact that $n^2$ is even. Therefore $n$ cannot be odd, so $n$ is even. $\square$

### Example 3 (No positive integer solution)

Prove that the equation $x^2=2y^2$ has no solution in positive integers.

**Solution**

Assume a positive integer solution $(x,y)$ exists. Then $x^2=2y^2$, so $x^2$ is even, and by Example 2 $x$ is even: write $x=2m$.
Substituting: $4m^2=2y^2$, so $y^2=2m^2$, so $y^2$ is even, and $y$ is even.
Then $x$ and $y$ are both even, so they share a factor of $2$ — contradicting that we may take them with no common factor. Therefore no positive integer solution exists. $\square$

## Exercises

**Q1.** Prove that $\sqrt{3}$ is irrational.

**A1.** Assume $\sqrt{3}=p/q$ in lowest terms. Then $3q^2=p^2$, so $p^2$ is divisible by $3$, hence $p$ is divisible by $3$: $p=3k$. Then $3q^2=9k^2$, so $q^2=3k^2$, so $q$ is divisible by $3$. Thus $p$ and $q$ share a factor $3$, a contradiction. So $\sqrt{3}$ is irrational. $\square$

**Q2.** Prove that, if $n^2$ is a multiple of $3$, then $n$ is a multiple of $3$.

**A2.** Assume $n$ is not a multiple of $3$. Then $n=3k\pm1$, so $n^2=9k^2\pm6k+1=3(3k^2\pm2k)+1$, which is not a multiple of $3$ — contradiction. Hence $n$ is a multiple of $3$. $\square$

**Q3.** Prove that, if $a$ is rational and $b$ is irrational, then $a+b$ is irrational.

**A3.** Assume, for contradiction, that $a+b$ is rational. Then $(a+b)-a=b$ is the difference of two rationals, so $b$ is rational — contradicting that $b$ is irrational. Therefore $a+b$ is irrational. $\square$

**Q4.** Prove that $\sqrt{5}$ is irrational.

**A4.** Assume $\sqrt{5}=p/q$ in lowest terms; then $5q^2=p^2$, so $5\mid p$, write $p=5k$; then $5q^2=25k^2$, so $q^2=5k^2$, so $5\mid q$ — contradiction with lowest terms. Hence $\sqrt{5}$ is irrational. $\square$

**Q5.** Prove that, if $n^2$ is odd, then $n$ is odd.

**A5.** Assume $n$ is even: $n=2k$, so $n^2=4k^2$, which is even — contradiction with $n^2$ odd. Hence $n$ is odd. $\square$

**Q6.** Prove that the equation $x^2-2=0$ has no rational solution.

**A6.** A rational solution would mean $\sqrt{2}=x$ is rational, contradicting Example 1. Therefore there is no rational solution. $\square$
