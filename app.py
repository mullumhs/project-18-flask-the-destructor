from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    inventory_items = [name, 'banana', 'cherry']
    return render_template('hello.html', inventory=inventory_items)

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


@app.route('/meow/<word>/<int:number>')
def meow(word, number):
    awesome = []
    while len(awesome) < number:
        awesome.append(f"{word} is {len(awesome)}")
    
    return render_template('test.html', awesome=awesome)


@app.route('/woof/<word>/<int:number>')
def woof(word, number):
    awesome = []
    while len(awesome) < number:
        awesome.append(f"{word} is {len(awesome)}")
    
    return render_template('boottest.html', awesome=awesome)


@app.route('/contact', methods=['GET', 'POST'])

def contact():

    if request.method == 'POST':

        name = request.form['name']

        email = request.form['email']

        message = request.form['message']

        # Here you would typically save this data or send an email

        return redirect(url_for('thankyou', name=name, message=message))

    return render_template('contact.html')



@app.route('/thankyou')

def thankyou():

    name = request.args.get('name')

    message = request.args.get('message')

    return render_template('thankyou.html', name=name, message=message)

if __name__ == '__main__':

    app.run(debug=True)