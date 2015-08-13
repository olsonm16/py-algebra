"""

A quadratic has the form ax^2 + bx + c.

First, we divide by the leading term a, and get back a new formula:

x^2 + bx + c.

Now, we can try to factor.

(x - d)(x - e) = x^2 + bx + c if d*e = c and d + e = b.

d and e will each be less than or equal to c.

Let's try to put that into an algorithm.

First we need a good form for a quadratic.

Let's let a quadratic be an instance of a general class Polynomial.

A polynomial is formed from some user input that looks like "x^2 + bx + c".

We'll need to parse that string.

We'll build a list of constants. That's it.

General polynomial: ax^n + bx^n-1 + cx^n-2 + ... + dx + e.

List, [a, b, c, ...., d, e]

Elements in the list are 0 if the constant for a term is 0, or rather, there is no x raised to that power.

For example, if we had the poly x^2 - 4, the list would be [1, 0, -4]

Cool.

But how can we parse that initial string input.

String = "x^2 + bx + c"

List = String.split(" + ")  #["x^2, "bx", "c"]

leading_power = List[0].split("^")[1]

ConstantList = [0]*leading_power = [0, 0, 0]

for term in List:
	split_term = term.split("^")

	#This case means we have a term with power greater than one.
	if len(split_term) > 1:
		length = len(split_term[0])
		constant_term = int(split_term[0][0:length-1])
		ConstantList[int(split_term[1])] = constant_term

	#This case means we've reached the x to the 1 power.
	elif len(split_term) == 1 and "x" in split_term:
		constant_term = int(split_term.split("x")[0])
		ConstantList[1] = constant_term

	elif len(split_term) == 1  and not ("x" in split_term):
		constant_term = int(split_term)
		ConstantList[0] = constant_term
"""