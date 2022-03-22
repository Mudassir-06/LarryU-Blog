import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    # "import secrets" in Terminal -> secrets.token_hex(16).
    SECRET_KEY = "c188044384c87340b6589cd20cf75491"
    SQLALCHEMY_DATABASE_URI  = "sqlite:///site.db"
    SQLALCHEMY_TRACK_MODIFICATIONS  = False
    MAIL_SERVER ='smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS =True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')