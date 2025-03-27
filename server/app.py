from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initialize Flask-Migrate

@app.route('/')
def home():
    return "Flask-SQLAlchemy CRUD Demo"

if __name__ == '__main__':
    app.run(debug=True)