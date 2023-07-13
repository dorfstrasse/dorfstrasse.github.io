from application.controller.dbConnect import dbApp
from psycopg2.extras import execute_values

class Loginvalidate(object):

	def rows_to_dict_list(self,cursor):
		columns = [i[0] for i in cursor.description]
		return [dict(zip(columns, row)) for row in cursor]

	def loginCek(self,email,password):
		conn = dbApp()
		try:
			cur = conn.cursor()
			bind = dict()
			bind['email'] = email
			bind['password'] = password
			query = '''
					SELECT * FROM akun WHERE email = %(email)s
					'''
			cur.execute(query, bind)
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
