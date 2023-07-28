# This program uses pgadmin to restructure a csv file that may not be formatted correctly
import psycopg2
import pandas as pd

from sqlalchemy import create_engine 

#connect to pgadmin
conn = psycopg2.connect(host="localhost", dbname = "rssProcess", user="postgres",
                        password = "putpgadminpassword", port=5432)
cur = conn.cursor()


#bcreate table (if it does not already exist) with the following headers
cur.execute(''' CREATE TABLE IF NOT EXISTS trialcommentsnew (
            id VARCHAR(255),
            creator_id VARCHAR(255),
            post_id INT,
            title text,
            removed text,
            published text
            );


            ''')

# add the data values for those columns
cur.execute('''COPY trialcommentsnew(
            id,
            creator_id,
            post_id,
            title,
            removed,
            published
            )

FROM 'ENTER_FILE_NAME.csv'
DELIMITER ','
CSV HEADER;''')


# creating the engine
engine = create_engine('postgresql://postgres:ricekrispies@localhost/rssProcess')

# using a sql query to read in from the table 
dataPhase = pd.read_sql_query('SELECT * FROM trialcommentsnew', engine)
print("Successfully exported")

engine.dispose()

# exporting that to a csv file 
dataPhase.to_csv('EXPORT_FILE_NAME.csv', index=False)
            

conn.commit()

cur.close()
conn.close()