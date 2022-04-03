from flask import Blueprint, render_template,request,flash,redirect,url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password = request.form.get('password')
        password1 = request.form.get('password1')

        if len(password)<8:
            flash('Not sufficent length for password',category='error')
        if password != password1:
            flash('two passwords do not match',category='error')
        else:
            new_user = User(email=email, first_name= first_name, last_name=last_name, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('account created', category='sucess')
            return redirect(url_for('views.home'))
    return render_template("signup.html")
    
    
@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "logout"