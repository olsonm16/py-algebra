from polynomial import *

def TI89():

	print("__________T1_89_________")
	print("____Basic Calculator____")
	print("Functions: solve(quadratic), eval(polynomial)")

	memory = {}

	while True:

		x = raw_input(">>: ")
		if 'solve' in x:
			split = x.split('solve')
			string = split[1].split('(')[1].split(')')[0]
			poly = None
			if string.isalpha():
				if string in memory.keys():
					poly = memory[string]
				else:
					print("Variable " + string  + " unbound to a polynomial in this environment.")
			else:
				try:
					poly = Polynomial(string)
				except:
					print("Bad input")

			if poly != None:
				if poly.leading_power > 2:
					print("Solve only works for quadratics right now.")
				else:
					solution = poly.solve()
					print(solution)

		elif 'eval' in x:
			split = x.split('eval')
			string = split[1].split('(')[1].split(')')[0]
			polyeval = string.split(", ")
			num = float(polyeval[1])
			poly = None
			if polyeval[0].isalpha():
				if polyeval[0] in memory.keys():
					poly = memory[polyeval[0]]
				else:
					print("Variable " + polyeval[0]  + " unbound to a polynomial in this environment.")
			else:
				try:
					poly = Polynomial(polyeval[0])
				except:
					print("Bad input")

			if poly != None:
				solution = poly.evaluate(num)
				print(solution)

		elif 'quit' in x:
			break

		elif "=" in x:
			assignment_list = x.split(" = ")
			memory[assignment_list[0]] = Polynomial(assignment_list[1])

		elif "memory" in x:
			for key in memory.keys():
				print key + " : " + str(memory[key])

		else:
			if x in memory.keys():
				print memory[x]

if __name__ == "__main__":
	TI89()