import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models import db

app = Flask(__name__)

curr_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(curr_dir, 'week7_database.sqlite3')
db.init_app(app)

@app.route('/')
def homepage():
    pass



if __name__ == '__main__':
    app.run(debug=True)