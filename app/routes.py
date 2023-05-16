from flask import render_template, flash, redirect, url_for
from flask import request
from flask_login import current_user, login_user
from flask_login import logout_user
from werkzeug.urls import url_parse

from app import app, db
from app.filter import partList, partFilter, pcFilter, computerList
from app.forms import LoginForm
from app.forms import RegistrationForm
from app.models import User, Post


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/computerparts')
def computerparts():
    part = request.args.get('part')
    partsList, name, price, rating = partFilter(partList, part=part)
    return render_template('computerparts.html', part=part, info=zip(partsList, name, price, rating))


@app.route('/cart')
def cart():
    return render_template('computerparts.html')


@app.route('/review')
def review():
    return render_template('review.html')



@app.route('/prebuilt')
def prebuilt():
    pcType = request.args.get('pcType')
    pcList, name, price, rating, processorType, diskSize, ram, processorSpeed, gpu = pcFilter(computerList, pcType=pcType)
    return render_template('prebuilt.html', pcType=pcType, pcinfo=zip(pcList, name, price, rating, processorType, diskSize, ram, processorSpeed, gpu))


@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/rating')
def rating():
    return render_template('rating.html')

