from application import app
from flask import Flask, render_template,redirect, request, url_for, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import InputRequired
from functools import wraps
from application.models.login import Loginvalidate
import bcrypt

def cek_login(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'login' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap


@app.route('/login', methods=['GET','POST'])
def login():
    # return render_template('000-login.html')
    if session.get('login') == True:
        return redirect(url_for('home'))
    form = FlaskForm()
    masuk = Loginvalidate()
    if form.validate_on_submit():
        if request.method == 'POST':
            email = request.form['email-login']
            password = request.form['password-login']
            cek_login = masuk.loginCek(email, password)
            
            if len(cek_login) > 0 :
                for data in cek_login:
                    if password == data['password']:
                        session['login'] = True
                        session['id_team'] = data['id_team']
                        session['nama_account'] = data['nama_account']
                        session['no_hp'] = data['no_hp']
                        session['posisi'] = data['posisi']
                        return redirect(url_for('home'))
                    else:
                        pesan =  'Password tidak sesuai'
                        return render_template('000-login.html',pesan=pesan,form=form)
            else:
                pesan =  'User tidak terdaftar'
                return render_template('000-login.html',pesan=pesan,form=form)
        return render_template('000-login.html',form=form)
    return render_template('000-login.html', form=form)

@app.route('/logout')
@cek_login
def logout():
    session.clear()
    return redirect(url_for('login'))