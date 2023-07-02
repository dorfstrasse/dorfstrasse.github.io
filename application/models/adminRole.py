from application.controller.dbConnect import dbApp
from flask import request, redirect, url_for
from datetime import datetime
import psycopg2

def admin_terima():
    conn = dbApp()
    cur = conn.cursor()
    if request.method == 'POST':
        id_listing = request.form.get('id_listing')
        keterangan = 'Terima'
        print(id_listing)
        try:
            query = '''
                    UPDATE pending_listing
                    SET status = %s
                    WHERE id_listing = 'esrm-8417326062023'
                    '''
            data = (keterangan)
            cur.execute(query, data)

            conn.commit()
            
            cur.close()
            conn.close()

            return redirect(url_for('konfirm_listing'))
        except (Exception, psycopg2.DatabaseError) as error:
                return "Terjadi kesalahan: " + str(error)