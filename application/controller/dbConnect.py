import os
import psycopg2


# def dbApp():
#     connection = psycopg2.connect(host="localhost",database="ap_dashboard",user='tomi_findb',password='f1n#D85e12v3r*]')
#     return connection
def dbApp():
    connection = psycopg2.connect(host="localhost",database="finance",user='postgres',password='12345')
    return connection