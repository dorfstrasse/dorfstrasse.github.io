import os
import base64
from werkzeug.utils import secure_filename
from application import app
from flask import Flask,render_template,redirect, request,url_for,session,flash
from application.routes.login import cek_login
from application.models.pendingListing import listing
from application.models.listingDisplay import listing_display
from application.models.addListing import submit_listing
from application.models.adminRole import admin_terima
from application.controller.dbConnect import dbApp
from datetime import datetime
import psycopg2

pend_listing = listing()
view_listing = listing_display()


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
    list_listing = view_listing.new_listing()
    listing = []
    for pl in list_listing:
        print('\n\n\n')
        pl['foto1'] = base64.b64encode(pl['foto1']).decode('utf-8')
        listing.append(pl)
    return render_template('002-beli.html', data=listing)
    # return render_template('002-beli.html')

@app.route('/beli/detail-listing', methods=['GET','POST'])
def beli_detail_listing():
    listing_title = request.args.get('judul_iklan')
    alamat_properti = request.args.get('alamat_properti')
    display_listing = view_listing.new_listing()
    selected_listing = next((d for d in display_listing if d['judul_iklan'] == listing_title and d['alamat_properti'] == alamat_properti), None)
    if selected_listing:
        return render_template('100-detail-listing.html', data = selected_listing)
    return render_template('98-error-404.html')


# -------------------------------------------
# SEWA
# -------------------------------------------
@app.route('/sewa', methods=['GET','POST'])
# @cek_login
def sewa():
    list_listing = view_listing.new_listing()
    listing = []
    for pl in list_listing:
        listing.append(pl)
    return render_template('003-sewa.html', data=listing)

@app.route('/sewa/detail-listing', methods=['GET','POST'])
def sewa_detail_listing():
    listing_title = request.args.get('judul_iklan')
    alamat_properti = request.args.get('alamat_properti')
    display_listing = view_listing.new_listing()
    selected_listing = next((d for d in display_listing if d['judul_iklan'] == listing_title and d['alamat_properti'] == alamat_properti), None)
    if selected_listing:
        return render_template('100-detail-listing.html', data = selected_listing)
    return render_template('98-error-404.html')


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
# @cek_login
def buat_listing():
    pending_listing = pend_listing.pending_listing()
    list_pending = []
    for pl in pending_listing:
        list_pending.append(pl)
    return render_template('010-buat-listing.html', data=list_pending)

@app.route('/buat-listing/input-listing', methods=['GET', 'POST'])
# @cek_login
def input_listing():
    return render_template('101-input-listing.html')

@app.route('/buat-listing/listing-masuk', methods=['GET', 'POST'])
# @cek_login
def bl_listing_masuk():
    id_listing = request.args.get('id_listing')
    d_pending_listing = pend_listing.pending_listing()
    selected_row = next((d for d in d_pending_listing if d['id_listing'] == id_listing), None)
    if selected_row:
        return render_template('102-listing-masuk.html', data = selected_row)
    return render_template('98-error-404.html')

# -------------------------------------------
# KONFIRM LISTING
# -------------------------------------------

@app.route('/konfirm-listing', methods=['GET', 'POST'])
# @cek_login
def konfirm_listing():
    pending_listing = pend_listing.pending_listing()
    list_pending = []
    for pl in pending_listing:
        list_pending.append(pl)
        print(list_pending)
    return render_template('011-konfirm-listing.html', data=list_pending)

@app.route('/konfirm-listing/listing-masuk', methods=['GET', 'POST'])
# @cek_login
def kl_listing_masuk():
    id_listing = request.args.get('id_listing')
    d_pending_listing = pend_listing.pending_listing()
    selected_row = next((d for d in d_pending_listing if d['id_listing'] == id_listing), None)
    if selected_row:
        return render_template('102-listing-masuk.html', data = selected_row)
    return render_template('98-error-404.html')

@app.route('/submit', methods=['GET', 'POST'])
# @cek_login
def submit():
    submit_listing()
    return redirect(url_for('buat_listing'))

@app.route('/terima', methods=['GET', 'POST'])
# @cek_login
def terima():
    conn = dbApp()
    cur = conn.cursor()
    id_listing = request.args.get('id_listing')
    status = 'Diterima'

    query = '''
            UPDATE pending_listing
            SET status = %s
            WHERE id_listing = %s
            '''
    data = (status, id_listing)
    cur.execute(query, data)

    conn.commit()
    
    cur.close()
    conn.close()

    return redirect(url_for('konfirm_listing'))

@app.route('/minta-perbaikan', methods=['GET', 'POST'])
# @cek_login
def mintaPerbaikan():
    conn = dbApp()
    cur = conn.cursor()
    id_listing = request.args.get('id_listing')
    status = 'Perbaiki'

    query = '''
            UPDATE pending_listing
            SET status = %s
            WHERE id_listing = %s
            '''
    data = (status, id_listing)
    cur.execute(query, data)

    conn.commit()
    
    cur.close()
    conn.close()
    
    return redirect(url_for('konfirm_listing'))

@app.route('/tolak', methods=['GET', 'POST'])
# @cek_login
def tolak():
    conn = dbApp()
    cur = conn.cursor()
    id_listing = request.args.get('id_listing')
    status = 'Ditolak'

    query = '''
            UPDATE pending_listing
            SET status = %s
            WHERE id_listing = %s
            '''
    data = (status, id_listing)
    cur.execute(query, data)

    conn.commit()
    
    cur.close()
    conn.close()
    
    return redirect(url_for('konfirm_listing'))