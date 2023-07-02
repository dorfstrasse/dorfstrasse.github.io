from application.controller.dbConnect import dbApp

class listing(object):
    def rows_to_dict_list(self,cursor):
        columns = [i[0] for i in cursor.description]
        return [dict(zip(columns, row)) for row in cursor]

    def pending_listing(self):
        conn = dbApp()
        try:
            cur = conn.cursor()
            query = '''
					select * from pending_listing
					'''
            cur.execute(query)
            data = self.rows_to_dict_list(cur)
            conn.commit()
            return data
        except Exception as e:
            conn.rollback()
            return str(e)
        finally:
            if conn is not None:
                cur.close()
                conn.close()