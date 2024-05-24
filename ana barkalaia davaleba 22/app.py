from flask import Flask, render_template, request, session, redirect, url_for
from datetime import timedelta
app = Flask(__name__)
app.secret_key = 'marwyvi'
app.permanent_session_lifetime=timedelta(minutes=5)

@app.route('/')
def home():
    if 'username' in session:
        return redirect('user')
    else:
        return redirect('login')



@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        session.permanent = True
        username = request.form['Username']
        password = request.form['Password']
        session['Password'] = password
        session['Username'] = username
        return redirect(url_for('user'))
    else:
        if 'Username' in session:
            return redirect(url_for('user'))
        return render_template('login.html',)


@app.route('/home')
def user():
    if 'Username'in session:
        username = session['Username']
        return render_template('home.html',username = username)
    else:
        redirect('login')


@app.route('/logout')
def logout():
    session.pop('Username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)