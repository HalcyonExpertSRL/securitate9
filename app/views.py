from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_user, current_user, logout_user
from .forms import RegistrationForm, LoginForm
from .models import User, db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('views.login'))
    return render_template('register.html', form=form)

@views.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('views.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('views.home'))
    return render_template('login.html', form=form)

@views.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('views.home'))

@views.route('/account')
def account():
    return render_template('account.html')
