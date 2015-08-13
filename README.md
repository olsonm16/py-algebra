# Basic Algebra in Python

A polynomial is formed from some user input that looks like "x^2 + bx + c".

General polynomial: ax^n + bx^n-1 + cx^n-2 + ... + dx + e.

We'll build a list of constants:
List, [a, b, c, ...., d, e]
Elements in the list are 0 if the constant for a term is 0, or rather, there is no x raised to that power.
For example, if we had the poly x^2 - 4, the list would be [1, 0, -4]

To use the polynomial functionality (a quadratic solver and an evaluator), download a zip of this repo, open Terminal, go to the directory of the unzipped repo, and enter into a simple ti89 emulator:

```
python ti89.py

__________T1_89_________
____Basic Calculator____
Functions: solve(quadratic), eval(polynomial)
>>: 

```

You may solve or eval as follows:

```
>>: solve(x^2 + x + 1)
Polynomial x^2 + x + 1 has solutions at x = (-0.5+0.87j) and x = (-0.5-0.87j).
```

Note that the solve function only takes quadratics right now.

```
>>: eval(x^3 + 2x + 1, 1)
4.0
```

You may also set variables for the app to use.

For example:

```
>>: gamma = x^2 - 4
>>: solve(gamma)
Polynomial x^2 - 4 has solutions at x = 2.0 and x = -2.0.

>>: eval(gamma, 1)
-3.0
```

Have fun!
