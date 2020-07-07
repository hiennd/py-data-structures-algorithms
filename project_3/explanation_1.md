**sqrt(number) using Babylonian method**
**Time Complexity**
- Time complexity: O(n)
Let's take a look at the definition of f(x) = sqrt(x) = y <==> y^2 = x 0  <==> y = x / y
------
f(O) = 1
f(k + 1) = (n + f(k)) / 2,   while k >= x / k + PRECEIS * x 
-----
We go half by half from f(0) to sqrt(number) so the runtime would be O(log(sqrt(n))) 
because sqrt(n) << n, when n -> infinity
so it is equivelant to O(logn)
**Spcace Complexity**
O(1) as no extra data structure is used.