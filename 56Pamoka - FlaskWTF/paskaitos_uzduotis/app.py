from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

with app.app_context():
    db.create_all()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return "Registered successfully!"
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            return "Logged in successfully!"
        else:
            return "Incorrect email or password!"
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
