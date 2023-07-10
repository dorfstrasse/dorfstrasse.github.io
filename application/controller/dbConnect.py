import os
import psycopg2

def dbApp():
    # connection = psycopg2.connect(host="ep-ancient-math-184814-pooler.ap-southeast-1.postgres.vercel-storage.com",
    #                               database="verceldb",
    #                               user='default',
    #                               password='rse2IPfnQSx5')
    connection = psycopg2.connect(host="localhost", database="erasky", user='postgres', password='db4329')
    return connection