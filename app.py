from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the Flask!"


print(__name__)

if __name__ == '__main__':
    app.run(debug=True)