**sqrt(number) using Babylonian method**
**Time Complexity**
- Time complexity: O(log(sqrt(n))) 
Let's take a look at the definition of f(x) = sqrt(x) = y <==> y^2 = x <==> y = x / y
------
y(0) = 1
y(k + 1) = (y(k) + n / y(k)) / 2,   while y^2 > PRECEISE * x
-----
We go half by half between f(0) and sqrt(number) so the runtime would be O(log(sqrt(n))) 
**Spcace Complexity**
O(1) as no extra data structure is used.