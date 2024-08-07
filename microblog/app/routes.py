from app import app
from flask import render_template
from app.forms import LoginForm, AlgebraForm
from flask import render_template, flash, redirect,  url_for
from random import  randint
import os
from werkzeug.utils import secure_filename
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel', 'admin': 'El Primo'}
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
    return render_template('index.html', title='Home', user=user, posts = posts)
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data, category="message"))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
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


