
from flask import Flask, request, render_template
from flask import jsonify

app = Flask(__name__)


@app.route("/")

def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])

def main():
                 n = request.form['text']
                 arr = ['zero','one','two','three','four','five','six','seven','eight','nine']

                 res = []
                 for x in n:
                    res.append(arr[int(x)])

                 return jsonify(res)

app.run(debug=True)
