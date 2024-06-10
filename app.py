#Flask uygulamasının ana dosyası.

from flask import Flask, render_template, redirect, url_for, request, session
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db, User, Debt, Income, Expense
from utils import debt_tracking, repayment_plans, strategies

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            return "Login Failed"
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))
    user = User.query.get(user_id)
    debts = Debt.query.filter_by(user_id=user_id).all()
    return render_template('dashboard.html', user=user, debts=debts)

# Diğer route'ları ve işlevleri buraya ekleyin...

if __name__ == '__main__':
    app.run(debug=True)