from flask_wtf import FlaskForm
from wtforms import Form, ValidationError
from wtforms import StringField, IntegerField, TextAreaField, SelectField, PasswordField, DateField
from wtforms.validators import DataRequired, Email, Length

class ContactsForm(FlaskForm):
    name = StringField("Имя", validators=[DataRequired(), Length(min=3, max=30)], description={'placeholder': 'Введите ваше имя'})
    email = StringField("Email", validators=[DataRequired(), Email()], description={'placeholder': 'Введите email'})
    phone = StringField("Контактный телефон", validators=[DataRequired()], description={'placeholder': 'Введите телефон'})
    message = TextAreaField("Сообщение", validators=[DataRequired()], description={'placeholder': 'Введите ваше сообщение'})

class RentForm(FlaskForm):
    name = StringField("Имя", validators=[DataRequired(), Length(min=3, max=30)], description={'placeholder': 'Введите ваше имя'})
    email = StringField("Email", validators=[DataRequired(), Email()], description={'placeholder': 'Введите email'})
    phone = StringField("Контактный телефон", validators=[DataRequired()], description={'placeholder': 'Введите телефон'})
    date = DateField('Дата', format='%Y-%m-%d')
    message = TextAreaField("Комментарий к заказу", validators=[DataRequired()], description={'placeholder': 'Введите ваше сообщение'})

class BuyForm(FlaskForm):
    name = StringField("Имя", validators=[DataRequired(), Length(min=3, max=30)], description={'placeholder': 'Имя'})
    surname = StringField("Фамилия", validators=[DataRequired(), Length(min=3, max=30)], description={'placeholder': 'Фамилия'})
    email = StringField("Email", validators=[DataRequired(), Email()], description={'placeholder': 'Введите email'})
    phone = StringField("Контактный телефон", validators=[DataRequired()], description={'placeholder': 'Введите телефон'})
    card_number = StringField("Номер карты", validators=[DataRequired(), Length(min=16, max=16)], description={'placeholder': '**** **** **** ****'})
    card_time = StringField("Дата карты", validators=[DataRequired(), Length(min=5, max=5)], description={'placeholder': 'DD/MM'})
    card_cvc = StringField("CVC-код", validators=[DataRequired(), Length(min=3, max=3)], description={'placeholder': 'CVC'})
    country = SelectField("Страна", choices=[('ru', 'Россия'), ('kz', 'Казахстан'), ('br', 'Белорусь')], validators=[DataRequired()], description={'placeholder': 'Страна'})
    postal_code = StringField("Почтовый индекс", validators=[DataRequired()], description={'placeholder': 'Почтовый индекс'})