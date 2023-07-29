from flask import Flask, render_template, request, jsonify

obj = Flask(__name__)

@obj.route('/')
def welcome():
    return "Welcome to the Flask!"


@obj.route('/cal', methods=['GET'])
def math_operator():
    operation = request.json["operation"]
    number1 = request.json["number1"]
    number2 = request.json["number2"]

    if operation == 'add':
        result = int(number1) + int(number2)
    elif operation == 'mul':
        result = int(number1) * int(number2)
    elif operation == 'div':
        result = int(number1) / int(number2)
    else:
        result = int(number1) - int(number2)
    return result



print(__name__)

if __name__ == '__main__':
    obj.run(debug=True)