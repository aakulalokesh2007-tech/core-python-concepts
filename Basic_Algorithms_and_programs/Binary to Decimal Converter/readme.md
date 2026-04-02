# Here is the core logic that makes it work:
* ✂️ .split('.') to separate the integer bits from the fractional bits.
* ◀️ Reversing the integer string to calculate powers of 2 from right to left ($2^0, 2^1, 2^2$).
* ▶️ Iterating through the fractional string from left to right to calculate negative powers of 2 ($2^{-1}, 2^{-2}, 2^{-3}$).
* 🛡️ all() combined with list comprehension to build a bulletproof input validator that rejects anything other than 0, 1, and ..
