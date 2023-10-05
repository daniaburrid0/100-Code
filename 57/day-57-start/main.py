from flask import Flask, render_template
import random
import datetime
import requests

AGE = "https://api.agify.io/?name="
GEN = "https://api.genderize.io/?name="

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year = datetime.datetime.now().year
    name = "Dani"
    return render_template("index.html", num=random_number, year=year, name=name)

@app.route('/guess/<name>')
def guess(name):
    name = name.title()
    gen_response = requests.get(GEN + name)
    gen_data = gen_response.json()
    gender = gen_data['gender']
    age_response = requests.get(AGE + name)
    age_data = age_response.json()
    age = age_data['age']
    return render_template('guess.html', name=name, gender=gender, age=age)

@app.route('/blog')
def get_blog():
    blog_url = "https://api.npoint.io/88441cc45e581e4b67b6"
    response = requests.get(blog_url)
    all_posts = response.json()
    print(all_posts)
    return render_template('blog.html', posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)


