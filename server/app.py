#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    title = "Python Operations with Flask Routing and Views"
    return f'<h1>{title}</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print (f'{param}')
    return param

@app.route('/count/<int:param>')
def count(param):
    count = f""
    for n in range(param):
        count += f'{n}\n'
    return count

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:  # Avoiding division by zero
            result = num1 / num2
        else:
            err= f"Error: You have {num1} apples but you want to divide them equally among {num2} friends. This is an undefined operation"
            return f'<p style="color: red">{err}</p>'
    elif operation == '%':
        result = num1 % num2

    if result is not None:
        return f'{result}'
        # return f'<p>{num1} {"÷" if operation == "div" else operation} {num2} = {result}</p>'
    else:
        return 'You did math wrong mate'