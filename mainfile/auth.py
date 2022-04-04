from flask import Blueprint, render_template,request,flash,redirect,url_for,session
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

        user = User.query.filter_by(email=email).first()

        if user:
            flash('User Already exist',category='error')
        elif len(password)<8:
            flash('Not sufficent length for password',category='error')
        elif password != password1:
            flash('two passwords do not match',category='error')
        else:
            new_user = User(email=email, first_name= first_name, last_name=last_name, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('account created', category='sucess')
            session['user_id'] = user.id
            return redirect(url_for('views.index))
    else:
        if "user_id" in session:
            return redirect(url for("views.index"))
    return render_template("signup.html")
    
    
@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password') 
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                session['user_id'] = user.id
                return redirect(url_for('views.index'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    else:
        if "user_id" in session:
            return redirect(url for("views.index"))
    return render_template("login.html")

@auth.route('/logout')
def logout():
   session.pop("user_id", None)


    return redirect(url_for('views.home'))