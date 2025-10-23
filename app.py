from flask import Flask

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'

@app.route('/calc/<int:num1>/<string:operation>/<int:num2>')
def calculator(num1, operation, num2):

    # Program the logic of a calculator here

    # E.g. if operation = "add" then result = num1 + num2
    if operation == "add" or operation == "plus" or operation =="+":
        result = num1 + num2
    elif operation == "div" or operation == "/" or operation == "divide":
        result = num1 / num2
    elif operation == "times" or operation == "*" or operation == "mult" or operation == "multiply":
        result = num1 * num2
    elif operation == "minus" or operation == "subtract" or operation =="-" or operation =="sub" or operation =="min":
        result = num1 - num2
    else:
        result = "uh oh"


    return f'{num1} {operation} {num2} = {result}'

if __name__ == '__main__':

    app.run(debug=True)