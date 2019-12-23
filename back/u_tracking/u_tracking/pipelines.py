import sqlite3
import psycopg2
import logging

# DROP TABLE IF EXISTS flights_status
class UTrackingPipeline(object):
    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'postgres'  # the username when you create the database
        password = ''  # change to your password
        database = 'job'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.c = self.connection.cursor()
        # try:
        #
        #     self.c.execute('''
        #
        #          CREATE TABLE api_manager_app_u_tracking_return(
        #             ori TEXT,
        #             des TEXT,
        #             flight_no TEXT,
        #             etd TEXT,
        #             eta TEXT,
        #             status TEXT
        #          )
        #
        #      ''')
        #     self.connection.commit()
        # except sqlite3.OperationalError:
        #     pass

    def close_spider(self, spider):
        self.c.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.c.execute('''INSERT INTO api_manager_app_u_tracking_return (ori,des,flight_no,etd,eta,status) VALUES(%s, 
        %s, %s, %s, %s, %s) 

         ''', (
            item.get('ori'),
            item.get('des'),
            item.get('flight_no'),
            item.get('etd'),
            item.get('eta'),
            item.get('status')
        ))
        self.connection.commit()
        return item
