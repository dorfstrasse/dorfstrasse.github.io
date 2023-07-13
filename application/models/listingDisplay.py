from application.controller.dbConnect import dbApp

class listing_display(object):
    def rows_to_dict_list(self,cursor):
        columns = [i[0] for i in cursor.description]
        return [dict(zip(columns, row)) for row in cursor]

    def new_listing(self):
        conn = dbApp()
        try:
            cur = conn.cursor()
            query = '''
					SELECT * from fix_listing
					'''
            cur.execute(query)
            data = self.rows_to_dict_list(cur)
            conn.commit()
            print(data)
            return data
        except Exception as e:
            conn.rollback()
            return str(e)
        finally:
            if conn is not None:
                cur.close()
                conn.close()

#============================================================================
# import base64
# from application.controller.dbConnect import dbApp

# class listing_display(object):


#     def convert_bytea_to_string(self, bytea_data):
#         return bytea_data.decode('utf-8')


#     def get_data(self):
#         conn = dbApp()
#         try:
#             cur = conn.cursor()
#             query = '''
#                 SELECT * FROM new_listing0
#                 '''
#             cur.execute(query)
#             rows = cur.fetchall()
#             cur.close()
#             conn.commit()

#             data = []
#             for row in rows:
#                 waktu = row[1]
#                 nama_marketing = row[2]
#                 jual_sewa = row[3]
#                 tipe_properti = row[4]
#                 luas_tanah = row[5]
#                 luas_bangunan = row[6]
#                 jmlh_kmr_tidur = row[7]
#                 jmlh_kmr_mandi = row[8]
#                 alamat_properti = row[9]
#                 sertifikat = row[10]
#                 jmlh_lantai = row[11]
#                 hadap = row[12]
#                 fasilitas_lainnya = row[13]
#                 judul_iklan = row[14]
#                 deskripsi = row[15]
#                 harga_jual = row[16]
#                 id_listing = row[17]
#                 link_foto = row[18]
#                 foto1 = row[19]
#                 foto2 = row[20]
#                 foto3 = row[21]
#                 foto4 = row[22]
#                 foto5 = row[23]
#                 foto6 = row[24]
#                 foto7 = row[25]
#                 foto8 = row[26]
#                 foto9 = row[27]
#                 foto10 = row[28]
#                 foto11 = row[29]
#                 foto12 = row[30]
#                 if foto1 is not None:
#                     foto1_base64 = self.convert_bytea_to_base64(foto1)
#                     data.append({
#                         'foto1_base64': foto1_base64,
#                         'waktu' : waktu,
#                         'nama_marketing' : nama_marketing,
#                         'jual_sewa' : jual_sewa,
#                         'tipe_properti' : tipe_properti,
#                         'luas_tanah' : luas_tanah,
#                         'luas_bangunan' : luas_bangunan,
#                         'jmlh_kmr_tidur' : jmlh_kmr_tidur,
#                         'jmlh_kmr_mandi' : jmlh_kmr_mandi,
#                         'alamat_properti' : alamat_properti,
#                         'sertifikat' : sertifikat,
#                         'jmlh_lantai' : jmlh_lantai,
#                         'hadap' : hadap,
#                         'fasilitas_lainnya' : fasilitas_lainnya,
#                         'judul_iklan' : judul_iklan,
#                         'deskripsi' : deskripsi,
#                         'harga_jual' : harga_jual,
#                         'id_listing' : id_listing,
#                         'link_foto' : link_foto,
#                         'foto1' : foto1,
#                         'foto2' : foto2,
#                         'foto3' : foto3,
#                         'foto4' : foto4,
#                         'foto5' : foto5,
#                         'foto6' : foto6,
#                         'foto7' : foto7,
#                         'foto8' : foto8,
#                         'foto9' : foto9,
#                         'foto10' : foto10,
#                         'foto11' : foto11,
#                         'foto12' : foto12
#                     })

#             return data
#         except Exception as e:
#             conn.rollback()
#             return str(e)
#         finally:
#             if conn is not None:
#                 conn.close()