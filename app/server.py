# app/server.py

from flask import Flask, request, jsonify
from app.calculator import add, subtract, multiply, divide

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add_route():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = add(a, b)
    return jsonify(result=result)

@app.route('/subtract', methods=['GET'])
def subtract_route():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = subtract(a, b)
    return jsonify(result=result)

@app.route('/multiply', methods=['GET'])
def multiply_route():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    result = multiply(a, b)
    return jsonify(result=result)

@app.route('/divide', methods=['GET'])
def divide_route():
    a = float(request.args.get('a'))
    b = float(request.args.get('b'))
    try:
        result = divide(a, b)
    except ValueError as e:
        return jsonify(error=str(e)), 400
    return jsonify(result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
