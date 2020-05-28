from flask import Flask, render_template
app = Flask(__name__)
@app.route('/hi')
def hello_world():
    return "Hello Word"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')