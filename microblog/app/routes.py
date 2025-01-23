from app import app
from app import db
from flask import render_template
from app.forms import LoginForm, AlgebraForm
from app.forms import RegistrationForm
from flask import render_template, flash, redirect,  url_for, request
from random import  randint, choice
import os
from werkzeug.utils import secure_filename
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask_login import login_required
from urllib.parse import urlparse
@app.route('/')
@app.route('/index')
@login_required
def index():
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
    return render_template('index.html', title='Home', posts = posts)
def generateQuestion():
    num1 = randint(1,10)
    num2 = randint(1,10)
    operations = ["+", "-", "*", "/"]
    operation = operations[randint(0,3)]
    if operation == "/":
        num1 = num1 * num2
    if num2 > num1:
        num1copy = num1
        num1 = num2
        num2 = num1copy
    text = "{0}{1}{2} = ".format(num1, operation, num2)
    answer = 4
    if operation == "+":
        answer = num1 + num2
    elif operation == "-":
        answer = num1 - num2
    elif operation == "*":
        answer = num1 * num2
    elif operation == "/":
        answer = num1 / num2
    return text,int(answer)

symbols = ["🍒", "🔔", "🍋", "⭐", "🍇"]

def spin():
    return choice(symbols), choice(symbols), choice(symbols)

def check_win(symbol1, symbol2, symbol3):
    if symbol1 == symbol2 == symbol3:
        if symbol1 == "🍒":
            return "Вы выиграли 5x ставку!", 5
        elif symbol1 == "🔔":
            return "Вы выиграли 3x ставку!", 3
        else:
            return "Вы выиграли 2x ставку!", 2
    else:
        return "Попробуйте еще раз.", 0
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
        next_page = request.args.get('next')
        if not next_page or urlparse(next_page).netloc != '': #or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
        #return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
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
@app.route('/algebra', methods=['GET', 'POST'])
def algebra():
    form = AlgebraForm()

    if form.validate_on_submit():
        if form.answer.data == form.hidden_data.data:
            flash('Верно, Ваш ответ *{}* совпадает с вопросом: '.format(
                form.answer.data, category="message"))
        else:
            flash('Нет, правильный ответ: *{}*'.format(
                form.hidden_data.data, category="message"))
        return redirect(url_for('index'))
    else:
        text, answer = generateQuestion()
        form.hidden_data.data = answer
        return render_template('algebra.html', title='Sign In', form=form, qwestion = text)
@app.route('/slot', methods=['GET', 'POST'])
def slot():
    message = "жми"
    symbols = ("", "🤗", "")
    if request.method == 'POST':
        symbols = spin()
        message, multiplier = check_win(*symbols)
    return render_template('slot.html', message=message, symbols=symbols)

@app.route('/python')
@login_required
def python_ed():
    return render_template('python/page1.html')
@app.route('/python_page2')
def python_page2():
    return render_template('python/page2.html')
@app.route('/python_page3')
def python_page3():
    return render_template('python/page3.html')
@app.route('/python_page4')
def python_page4():
    return render_template('python/page4.html')
@app.route('/python_page5')
def python_page5():
    return render_template('python/page5.html')
@app.route('/python_page6')
def python_page6():
    return render_template('python/page6.html')
@app.route('/python_page7')
def python_page7():
    return render_template('python/page7.html')
@app.route('/python_page8')
def python_page8():
    return render_template('python/page8.html')
@app.route('/python_page9')
def python_page9():
    return render_template('python/page9.html')
@app.route('/python_page10')
def python_page10():
    return render_template('python/page10.html')
@app.route('/python_page11')
def python_page11():
    return render_template('python/page11.html')
@app.route('/python_page12')
def python_page12():
    return render_template('python/page12.html')
@app.route('/python_page13')
def python_page13():
    return render_template('python/page13.html')
@app.route('/lua')
def lua_ed():
    return render_template('lua/page1.html')
@app.route('/ideology')
def ideology():
    return render_template('ideology/ideology.html')
@app.route('/lua_page2')
def lua_page2():
    return render_template('lua/page2.html')
@app.route('/lua_page3')
def lua_page3():
    return render_template('lua/page3.html')
@app.route('/lua_page4')
def lua_page4():
    return render_template('lua/page4.html')
@app.route('/lua_page5')
def lua_page5():
    return render_template('lua/page5.html')
@app.route('/lua_page6')
def lua_page6():
    return render_template('lua/page6.html')

@app.route('/scratch')
def scratch_ed():
    return render_template('scratch/page1.html')
@app.route('/scratch_page2')
def scratch_page2():
    return render_template('scratch/page2.html')
@app.route('/scratch_page3')
def scratch_page3():
    return render_template('scratch/page3.html')
@app.route('/lua_intensiv')
def lua_intensiv_page1():
    return render_template('lua_intensiv/page1.html')
@app.route('/lua_intensiv_page2')
def lua_intensiv_page2():
    return render_template('lua_intensiv/page2.html')
@app.route('/lua_intensiv_page3')
def lua_intensiv_page3():
    return render_template('lua_intensiv/page3.html')
@app.route('/lua_intensiv_page4')
def lua_intensiv_page4():
    return render_template('lua_intensiv/page4.html')
@app.route('/lua_intensiv_page5')
def lua_intensiv_page5():
    return render_template('lua_intensiv/page5.html')
@app.route('/lua_intensiv_page6')
def lua_intensiv_page6():
    return render_template('lua_intensiv/page6.html')
