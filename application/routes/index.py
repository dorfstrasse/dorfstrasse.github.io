import os
from werkzeug.utils import secure_filename
from application import app
from flask import Flask,render_template,redirect, request,url_for,session,flash

@app.route('/')
# @cek_login
def home():
    return render_template('01-home.html')

@app.route('/beli', methods=['GET','POST'])
# @cek_login
def beli():
    return render_template('02-beli.html')

@app.route('/sewa', methods=['GET','POST'])
# @cek_login
def sewa():
    return render_template('03-sewa.html')

@app.route('/agen-kami-summarecon-bekasi', methods=['GET','POST'])
# @cek_login
def agen_kami_sb():
    return render_template('04-agen-summarecon-bekasi.html')

@app.route('/agen-kami-harapan-indah', methods=['GET','POST'])
# @cek_login
def agen_kami_hi():
    return render_template('05-agen-harapan-indah.html')

@app.route('/properti-baru', methods=['GET','POST'])
# @cek_login
def properti_baru():
    return render_template('06-properti-baru.html')

@app.route('/berita', methods=['GET','POST'])
# @cek_login
def berita():
    return render_template('08-berita.html')

@app.route('/tentang-kami', methods=['GET','POST'])
# @cek_login
def tentang_kami():
    return render_template('09-tentang-kami.html')

@app.route('/join-us', methods=['GET','POST'])
# @cek_login
def join_us():
    return render_template('10-join-us.html')

@app.route('/beli/detail-listing', methods=['GET','POST'])
def beli_detail_listing():
    return render_template('11-detail-listing.html')

@app.route('/sewa/detail-listing', methods=['GET','POST'])
def sewa_detail_listing():
    return render_template('11-detail-listing.html')

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('00-login.html')