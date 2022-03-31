from flask import render_template, request, Blueprint
from flaskblog.models import Post

main = Blueprint('main', __name__)

# Setting up a main.route decorator will handle the complicated backend stuff and allow us to write a function that returns the information that will be shown on the site
# Think of it as a root page
@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("home.html", posts=posts)


@main.route("/about")
def about():
    # return "<h1>About Page</h1>"
    return render_template("about.html", title="About")