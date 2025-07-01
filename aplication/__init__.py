from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import os


aplication = Flask(__name__)

aplication.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
aplication.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:CostadoMarfimrx8*10@localhost:3306/info_dados_db'


aplication.config['SECRET_KEY'] = 'secret'

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'upload') # constante do endereço para armazenar a imagem


login_manager = LoginManager(aplication)
db = SQLAlchemy(aplication)
