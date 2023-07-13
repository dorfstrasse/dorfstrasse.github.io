import os
import psycopg2

def dbApp():
    connection = psycopg2.connect(host="ep-red-pond-101960-pooler.ap-southeast-1.postgres.vercel-storage.com",
                                  database="verceldb",
                                  user='default',
                                  password='IJLa1BnO5Nyz')
    # connection = psycopg2.connect(host="localhost", database="erasky", user='postgres', password='db4329')
    return connection