from flask  import render_template, redirect, request, url_for
from app import app, db
from flask_login import current_user, login_user, logout_user
from app.models import User

message = {
    'visible' : False,
    'text' : ''
}

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', title = "index")

@app.route("/login", methods=['POST', 'GET'])
def login():
    if(request.method == 'POST'):
        message['visible'] = False
        user = User.query.filter_by(email_Id = request.form['username']).first()
        if(user is None or not user.check_password(request.form['password'])):
            message['visible'] = True
            message['visible'] = 'Invalid username or password!'
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('index'))        
    else:
        if(current_user.is_authenticated):
            return redirect(url_for('index'))
    return render_template('login.html', title = "login", message = message)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route("/register", methods=['GET', 'POST'])
def register():
    if(request.method == 'POST'):
        if(current_user.is_authenticated):
            return redirect(url_for('index'))
        else:
            user = User(first_name = request.form['first_name'], last_name = request.form['last_name'], email_Id = request.form['email_Id'])
            user.set_password(request.form['password'])
            db.session.add(user)
            db.session.commit()
            message['visible'] = True
            message['text'] = 'User Registration Succesfull !!'
            return redirect(url_for('login'))
    return render_template('register.html', title = "Register User")
    
@app.route("/profile")
def profile():
    if(current_user.is_authenticated):
        return render_template('profile.html', title="Profile")
    return redirect(url_for('login'))

@app.route("/createUser", methods=['POST'])
def createUser():
    return redirect(url_for('index'))

    