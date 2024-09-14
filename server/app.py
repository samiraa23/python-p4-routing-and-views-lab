from flask import Flask

app = Flask(__name__)

# Index route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print string route
@app.route('/print/<string:text>')
def print_string(text):
    print(text)
    return text

# Count route
@app.route('/count/<int:number>')
def count(number):
    return '\n'.join(str(i) for i in range(number)) + '\n'


# Math operations route
@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation", 400
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
