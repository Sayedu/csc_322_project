from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import LoginForm
from app.models import User, Post, Cart, Computers
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from flask import request
from werkzeug.urls import url_parse
from app.forms import RegistrationForm
from app.forms import EditProfileForm


@app.route('/')
@app.route('/index')
@login_required
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title='Home Page', posts=posts)


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



@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts)



@app.route('/', methods=["GET", "POST"])
def computers():
    computers = Computers.query.all()
    return render_template('computers.html', computers = computers)

@app.route('/<int:computer_id>', methods=["GET"])
def getComputer(computer_id):
    computer = Computers.query.get(computer_id)
    return render_template('singlecomputer.html', computer = computer)

@login_required
@app.route("/cart")
def cart():
    user_id = current_user.id
    cart_items = Cart.query.filter_by(user_id=user_id).all()
    computers = []
    final_total = 0
    for item in cart_items:
        computer = Computers.query.get(item.computer_id)
        computer.quantity = item.quantity
        final_total += computer.price * computer.quantity
        computers.append(computer)
    return render_template('cart.html', cart=computers, final_total = final_total)


@app.route('/<int:computer_id>/add_to_cart', methods=["POST", "GET"])
def add_to_cart(computer_id):

    if current_user.is_authenticated:
        user_id = current_user.id
        cart_item = Cart.query.filter_by(computer_id = computer_id, user_id=user_id).first()
        if cart_item:
            cart_item.quantity += 1
            cart_item.saveToDB()
        else:
            cart = Cart(computer_id = computer_id, user_id = user_id, quantity=1)
            cart.saveToDB()
    else:
        flash('You need to log in to add items to your cart', category='danger')
        return redirect(url_for('auth.loginPage'))
    return redirect(url_for('cart'))

@app.route('/cart/<int:computer_id>/remove', methods=["POST", "GET"])
def remove_from_cart(computer_id):
    user_id = current_user.id
    cart_item = Cart.query.filter_by(computer_id = computer_id, user_id=user_id).first()

    if not cart_item:
        return redirect(url_for('cart'))

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.saveToDB()
    else:
        cart_item.deleteFromDB()

    return redirect(url_for('cart'))

@app.route('/cart/clear', methods=["POST", "GET"])
def clear_cart():
    user_id = current_user.id
    cart_items = Cart.query.filter_by(user_id = user_id).all()

    for cart_item in cart_items:
        cart_item.deleteFromDB()

    return redirect(url_for('cart'))
