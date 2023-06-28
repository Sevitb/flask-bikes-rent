from . import app, mail
from flask import render_template, request, redirect, flash, url_for
from flask_mail import Mail, Message
from .forms import ContactsForm, RentForm, BuyForm
from .utils import send_mail

@app.route('/', methods=['POST','GET'])
def index():
    form = ContactsForm()
    buyForm = BuyForm()
    rentForm = RentForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            form_data = {
                'name': request.form.get('name'),
                'email': request.form.get('email'),
                'phone': request.form.get('phone'), 
                'message': request.form.get('message') 
            }
            try:
                msg = Message('Письмо с сайта', recipients=['peskovatzkov.vs@gmail.com'])
                msg.html = render_template("mail/contact-letter.html", form_data=form_data)
                mail.send(msg)
                flash("Спасибо, за сообщение! Оператор ответит вам как только сможет.")
                return redirect(url_for('index'))
            except:
                flash("Извините, не удалось отправить ваше сообщение! Пожалуйста, попробуйте позже.", 'error')
                return redirect(url_for('index'))
        else:
            flash("Что-то пошло не так, проверьте правильность заполнения полей.", 'error')

    return render_template('pages/homemade/index.html', title='Главная', form=form, buyForm=buyForm, rentForm=rentForm)


@app.route('/rent', methods=['POST','GET'])
def rent():
    if request.method == 'POST':
        rentForm = RentForm()
        print(rentForm.validate_on_submit())
        if rentForm.validate_on_submit():
            form_data = {
                'name': request.form.get('name'),
                'email': request.form.get('email'), 
                'phone': request.form.get('phone'),
                'date': request.form.get('date'),
                'message': request.form.get('message') 
            }
            try:
                msg = Message('Заявка на аренду!', recipients=['peskovatzkov.vs@gmail.com'])
                msg.html = render_template("mail/rent-letter.html", form_data=form_data)
                mail.send(msg)
                flash("Спасибо, за заявку! Оператор ответит вам как только сможет.")
            except:
                flash("Извините, не удалось отправить ваше сообщение! Пожалуйста, попробуйте позже.", 'error')
    return redirect(url_for('index'))

@app.route('/buy', methods=['POST','GET'])
def buy():
    if request.method == 'POST':
        buyForm = BuyForm()
        if buyForm.validate_on_submit():
            try:
                msg = Message('Спасибо за заказ в нашем магазине!', recipients=[request.form.get('email')])
                msg.html = render_template("mail/rent-letter.html")
                mail.send(msg)
                flash("Спасибо, за покупку! Ждем вашего возвращения.")
            except:
                flash("Извините, не удалось отправить ваше сообщение! Пожалуйста, попробуйте позже.", 'error')
    return redirect(url_for('index'))