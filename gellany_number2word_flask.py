
from flask import Flask, request, render_template
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def my_form():
    return render_template('homepage.html', pagetitle="Homepage")


@app.route('/', methods=['POST'])
def main():
                 n = request.form['text']
                 arr = ['zero','one','two','three','four','five','six','seven','eight','nine']

                 res = []
                 for x in n:
                    res.append(arr[int(x)])

                 return jsonify(res)


@app.route("/about")
def about():
  return render_template("about.html", pagetitle="About Us")



app.run(debug=True, port=5000)
