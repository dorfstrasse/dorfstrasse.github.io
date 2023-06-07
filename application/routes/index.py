import os
from werkzeug.utils import secure_filename
from application import app
from flask import Flask,render_template,redirect, request,url_for,session,flash

@app.route('/login', methods=['GET','POST'])
def login():
    return render_template('000-login.html')


# -------------------------------------------
# HOME
# -------------------------------------------
@app.route('/')
# @cek_login
def home():
    return render_template('001-home.html')


# -------------------------------------------
# BELI
# -------------------------------------------
@app.route('/beli', methods=['GET','POST'])
# @cek_login
def beli():
    return render_template('002-beli.html')

@app.route('/beli/detail-listing', methods=['GET','POST'])
def beli_detail_listing():
    return render_template('100-detail-listing.html')


# -------------------------------------------
# SEWA
# -------------------------------------------
@app.route('/sewa', methods=['GET','POST'])
# @cek_login
def sewa():
    return render_template('003-sewa.html')

@app.route('/sewa/detail-listing', methods=['GET','POST'])
def sewa_detail_listing():
    return render_template('100-detail-listing.html')


# -------------------------------------------
# PROPERTI BARU
# -------------------------------------------
@app.route('/properti-baru', methods=['GET','POST'])
# @cek_login
def properti_baru():
    return render_template('004-properti-baru.html')


# -------------------------------------------
# BERITA
# -------------------------------------------
@app.route('/berita', methods=['GET','POST'])
# @cek_login
def berita():
    return render_template('005-berita.html')


# -------------------------------------------
# AGEN KAMI
# -------------------------------------------
@app.route('/agen-kami-summarecon-bekasi', methods=['GET','POST'])
# @cek_login
def agen_kami_sb():
    return render_template('006-agen-summarecon-bekasi.html')

@app.route('/agen-kami-harapan-indah', methods=['GET','POST'])
# @cek_login
def agen_kami_hi():
    return render_template('007-agen-harapan-indah.html')


# -------------------------------------------
# TENTANG KAMI
# -------------------------------------------
@app.route('/tentang-kami', methods=['GET','POST'])
# @cek_login
def tentang_kami():
    return render_template('008-tentang-kami.html')


# -------------------------------------------
# JOIN US
# -------------------------------------------
@app.route('/join-us', methods=['GET','POST'])
# @cek_login
def join_us():
    return render_template('009-join-us.html')


# -------------------------------------------
# LISTING INPUT
# -------------------------------------------
@app.route('/buat-listing', methods=['GET', 'POST'])
def buat_listing():
    return render_template('010-buat-listing.html')

@app.route('/buat-listing/input-listing', methods=['GET', 'POST'])
def input_listing():
   return render_template('101-input-listing.html')