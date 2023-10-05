from flask import Flask, render_template
import requests

# constant
ENDPOINT = 'https://api.npoint.io/eb6cd8a5d783f501ee7d'

response = requests.get(ENDPOINT)
data = response.json()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    post = None
    for item in data:
        if item['id'] == post_id:
            post = item
            break
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)