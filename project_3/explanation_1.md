**sqrt(number) using Babylonian method**
**Time Complexity**
sqrt(n)
------
f(O) = 1
f(k + 1) = (n + f(k)) / 2
-----
We go half by half from f(0) to sqr(number) so the runtime would be roughly O(logn)
**Spcace Complexity**
O(1) as no extra data structure is used.