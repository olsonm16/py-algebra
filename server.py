from flask import Flask
app = Flask(__name__)

from polynomial import *

@app.route('/solve/<polynomial>')
def solve(polynomial):
    poly = Polynomial(polynomial)
    return poly.solve()

@app.route('/eval/<polynomial>/at/<factor>')
def eval(polynomial, factor):
	fac = float(factor)
	poly = Polynomial(polynomial)
	return str(poly.evaluate(fac))


if __name__ == "__main__":
    app.run(debug=True)