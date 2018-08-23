This is a math problem.
X and Y are independent.

f(x) = |x - a1| + |x - a2| + ... + |x - an|
a1 <= a2 <= a3 ... <= an
find the x to make f(x) get the minium number

when n = 2*k, f(x) reaches the minium if x belongs [x_k, x_k+1]
when n = 2*k - 1, f(x) reaches the minimum if x == x_k

Proof:

- when x < x1
x1 - x > 0
xn - x > xn - x1
|x - x1| + |x - xn| = x1 - x + xn - x > xn - x1

- when x1 <= x <= xn
|x - x1| + |x - xn| = x - x1 + xn - x = xn - x1

- when x > xn
x - x1 > xn - x1
x - xn > 0
|x - x1| + |x - xn| > xn - x1

so |x - x1| + |x - xn| >= xn - x1, and only when x1 <= x <= xn, it reaches min xn - x1

when n = 2 * k:
|x - x1| + |x - xn| >= xn - x1, equal only when x1 <= x <= xn
|x - x2| + |x - x_n-1| >= x_n-1 - x1, equal only when x2 <= x <= x_n-1
...
|x - x_k| + |x - x_k+1| >= x_k+1 - x_k, equal only when x_k <= x <= x_k+1

so the interseciton of all the equal requirements is x_k <= x <= x_k+1

when n = 2 * k - 1:
|x - x1| + |x - xn| >= xn - x1, equal only when x1 <= x <= xn
|x - x2| + |x - x_n-1| >= x_n-1 - x1, equal only when x2 <= x <= x_n-1
...
|x - x_k-1| + |x - x_k+1| >= x_k+1 - x_k-1, equal only when x_k-1 <= x <= x_k+1
|x - x_k| >= x_k, equal only when x = x_k
so the interseciton of all the equal requirements is x = x_k


