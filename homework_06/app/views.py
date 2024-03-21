from flask import render_template, app

from homework_06.app.models import User, Post


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/<int:user_id>/')
def user(user_id):
    user_item = User.query.get_or_404(user_id)
    return render_template('user.html', user=user_item)


@app.route('/<int:post_id>/')
def post(post_id):
    post_item = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post_item)
