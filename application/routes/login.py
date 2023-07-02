from application import app
from flask import Flask,render_template,redirect, request,url_for,session
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
    return render_template('000-login.html')
    # if session.get('login') == True:
    #     return redirect(url_for('home'))
    # form = FlaskForm()
    # masuk = Loginvalidate()
    # if form.validate_on_submit():
    #     if request.method == 'POST':
    #         email  = request.form['email']
    #         password  = request.form['password']
    #         cek_login = masuk.loginCek(username,password)
            
    #         if len(cek_login) > 0 :
    #             for data in cek_login:
    #                 if bcrypt.hashpw(password.encode('UTF-8'),data['mu_password'].encode('UTF-8')) == data['mu_password'].encode('UTF-8'):
    #                     session['login'] = True
    #                     session['name'] = data['mu_name']
    #                     session['dc'] = data['mu_mb_id']
    #                     session['nik'] = data['mu_nik']
    #                     session['jabatan'] = data['mu_jabatan']
    #                     session['email'] = data['mu_email']
    #                     session['id_akses'] = data['mu_mr_id']
    #                     return redirect(url_for('dashboard'))
    #                 else:
    #                     pesan =  'Password tidak sesuai'
    #                     return render_template('login.html',pesan=pesan,form=form)
    #         else:
    #             pesan =  'User tidak terdaftar'
    #             return render_template('login.html',pesan=pesan,form=form)
    #     return render_template('login.html',form=form)
    # return render_template('login.html', form=form)

# @app.route('/logout')
# @cek_login
# def logout():
#     session.clear()
#     return redirect(url_for('login'))