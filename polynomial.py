import math

class Polynomial():

	def __init__(self, string):
		self.initial = string
		self.constant_list, self.leading_power= self.build_constant_list(string)

	def __str__(self):
		return self.initial

	def solve(self):
		answers = self.zeros()
		return "Polynomial " + self.initial + " has solutions at x = " + str(answers[0]) + " and x = " + str(answers[1]) + "."

	def reduce(self):
		divisor = self.constant_list[0]
		if divisor > 1:
			reduced = [0]*len(self.constant_list)
			for i in range(len(self.constant_list)):
				reduced[i] = self.constant_list[i]/divisor
			return reduced
		return self.constant_list

	def evaluate(self, x):
		answer = 0
		length = len(self.constant_list)
		for i in range(length):
			answer += self.constant_list[i] * (x ** (length - i - 1))
		return answer

	def zeros(self):
		reduced = self.reduce()
		answers = []
		if self.leading_power == 2:
			b = reduced[1]
			c = reduced[2]
			return self.quadratic_formula(1.0, b, c)

	def quadratic_formula(self, a, b, c):
		inside_quad = b**2 - 4*a*c
		if inside_quad < 0:
			first = complex(round(-b/(2*a), 2), round(math.sqrt(abs(inside_quad))/(2*a), 2))
			second = complex(round(-b/(2*a), 2), -round(math.sqrt(abs(inside_quad))/(2*a), 2))
		else:
			first = round((-b + math.sqrt(inside_quad))/(2*a), 2)
			second = round((-b -+ math.sqrt(inside_quad))/(2*a), 2)
		return first, second

	def build_constant_list(self, string):
		List = string.split(" ")
		length = len(List)

		newList = []
		newList.append(List[0])

		for i in range(1, length):
			if List[i] == "+":
				newList.append(List[i + 1])
			elif List[i] == "-":
				newList.append("-" + List[i + 1])

		leading_power = int(List[0].split("^")[1]) + 1
		ConstantList = [0.0]*leading_power

		for term in newList:
			split_term = term.split("^")

			#This case means we have a term with power greater than one.
			if len(split_term) > 1:
				length = len(split_term[0])
				if length == 1:
					constant_term = 1
				elif split_term[0].split("x")[0] == "-":
					constant_term = -1
				else:
					constant_term = float(split_term[0][0:length-1])
				ConstantList[int(split_term[1])] = constant_term

			#This case means we've reached the x to the 1 power.
			elif len(split_term) == 1 and "x" in split_term[0]:
				if len(split_term[0]) == 1:
					constant_term = 1
				elif split_term[0].split("x")[0] == "-":
					constant_term = -1
				else:
					constant_term = float(split_term[0].split("x")[0])
				ConstantList[1] = constant_term

			elif len(split_term) == 1  and not ("x" in split_term[0]):
				constant_term = float(split_term[0])
				ConstantList[0] = constant_term

		return list(reversed(ConstantList)), leading_power - 1





