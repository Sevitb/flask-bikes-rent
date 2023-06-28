import os

MAIL_SERVER='mail.example.ru'
MAIL_PORT=465
MAIL_USE_SSL=True
MAIL_USERNAME='info@example.ru'
MAIL_DEFAULT_SENDER='info@example.ru'
MAIL_PASSWORD='example'

SECRET_KEY=os.urandom(32)
