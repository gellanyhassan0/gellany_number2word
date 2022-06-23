
from flask import Flask, request, render_template
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template('homepage.html', title="Homepage", custom_css="home")


@app.route('/', methods=['POST'])
def homepage_response():
                 n = request.form['text']
                 arr = ['zero','one','two','three','four','five','six','seven','eight','nine']

                 res = []
                 for x in n:
                    res.append(arr[int(x)])

                 return jsonify(res)

@app.route("/add")
def add():
  return render_template("add.html", title="Add Skill", custom_css="add")


@app.route("/skills")
def skills():

  my_skills = [("Html", 80), ("CSS", 75), ("Python", 95), ("MySQL", 45), ("Go", 35)]

  return render_template("skills.html",title="My Skills", custom_css="skills", page_head="My Skills",description="This Is My Skills Page", skills=my_skills)


@app.route("/about")
def about():
  return render_template("about.html", title="About Us")



app.run(debug=True, port=5000)
