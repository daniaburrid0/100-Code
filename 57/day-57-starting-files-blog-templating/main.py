from flask import Flask, render_template
import requests

blog_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
blog_dict = blog_response.json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", blog_posts=blog_dict)

@app.route('/post/<int:index>')
def post(index):
    requested_post = None
    for blog_post in blog_dict:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
