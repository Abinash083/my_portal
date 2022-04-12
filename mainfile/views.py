from flask import Blueprint, render_template, session, redirect, url_for
from . import db
from .models import User

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html",user=None)


@views.route('/index')
def index():
    if "user_id" in session:
        id = session["user_id"]
        user = User.query.filter_by(id=id).first()
        return render_template("index.html", user=user)
    else:
        return redirect (url_for("auth.login"))


@views.route('/note')
def note():
    if "user_id" in session:
        id = session["user_id"]
        user = User.query.filter_by(id=id).first()
        return render_template("note.html", user=user)
    else:
        return redirect (url_for("auth.login"))