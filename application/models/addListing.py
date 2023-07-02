from application.controller.dbConnect import dbApp
from application.models.generateId import number5
from flask import request, redirect, url_for
from datetime import datetime
import psycopg2

def submit_listing():
    conn = dbApp()
    cur = conn.cursor()
    if request.method == 'POST':
        
        id_string = datetime.now().strftime('%d%m%Y')
        id_string = str(id_string)

        waktu = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        nama_marketing = request.form['nama_marketing']
        jual_sewa = request.form['jual_sewa']
        tipe_properti = request.form['tipe_properti']
        luas_tanah = request.form['luas_tanah']
        luas_bangunan = request.form['luas_bangunan']
        jmlh_kmr_tidur = request.form['jmlh_kmr_tidur']
        jmlh_kmr_mandi = request.form['jmlh_kmr_mandi']
        alamat_properti = request.form['alamat_properti']
        sertifikat = request.form['sertifikat']
        jmlh_lantai = request.form['jmlh_lantai']
        hadap = request.form['hadap']
        fasilitas_lainnya = request.form['fasilitas_lainnya']
        judul_iklan = request.form['judul_iklan']
        deskripsi = request.form['deskripsi']
        harga_jual = request.form['harga_jual']
        status = 'Pending'

        if tipe_properti.lower() == 'rumah':
            id_listing = 'esrm-'+number5+id_string
        elif tipe_properti.lower() == 'ruko':
            id_listing = 'esrk-'+number5+id_string
        elif tipe_properti.lower() == 'apartemen':
            id_listing = 'esat-'+number5+id_string
        elif tipe_properti.lower() == 'gudang/pabrik':
            id_listing = 'esgp-'+number5+id_string
        elif tipe_properti.lower() == 'tanah/kavling':
            id_listing = 'estk-'+number5+id_string
        elif tipe_properti.lower() == 'ruang usaha':
            id_listing = 'esru-'+number5+id_string
        elif tipe_properti.lower() == 'lainnya':
            id_listing = 'esln-'+number5+id_string
        
        try:
            query = """
                    INSERT INTO pending_listing
                    (waktu,
                    nama_marketing,
                    jual_sewa,
                    tipe_properti,
                    luas_tanah,
                    luas_bangunan,
                    jmlh_kmr_tidur,
                    jmlh_kmr_mandi,
                    alamat_properti,
                    sertifikat,
                    jmlh_lantai,
                    hadap,
                    fasilitas_lainnya,
                    judul_iklan,
                    deskripsi,
                    harga_jual,
                    id_listing,
                    status)
                    VALUES (
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s)
                    """
            data = (waktu,
                    nama_marketing,
                    jual_sewa,
                    tipe_properti,
                    luas_tanah,
                    luas_bangunan,
                    jmlh_kmr_tidur,
                    jmlh_kmr_mandi,
                    alamat_properti,
                    sertifikat,
                    jmlh_lantai,
                    hadap,
                    fasilitas_lainnya,
                    judul_iklan,
                    deskripsi,
                    harga_jual,
                    id_listing,
                    status)
            
            cur.execute(query, data)

            conn.commit()
            
            cur.close()
            conn.close()

            return redirect(url_for('buat_listing'))
        except (Exception, psycopg2.DatabaseError) as error:
            return "Terjadi kesalahan: " + str(error)