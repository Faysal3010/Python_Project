from flask import Flask, render_template
from post import Post
import requests

response = requests.get('https://api.npoint.io/15f154cf734a1c16fde2')
all_blogs = response.json()
post_objects = []
for post in all_blogs:
    post_objects.append(Post(post_id=post['id'], title=post['title'], subtitle=post['subtitle'], body=post['body']))

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",blogs=post_objects)


@app.route('/post/<int:post_id>')
def get_post(post_id):
    requested_post = None
    for post in all_blogs:
        if post['id'] == post_id:
            requested_post = post
            break
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
