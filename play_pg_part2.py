#! /usr/bin/env python3

import psycopg2
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import schedule 
import time
sentiment = SentimentIntensityAnalyzer()
from datetime import date
import os
import subprocess
import csv
import matplotlib.pyplot as plt


def main():
    num_comments=0
    num_comments_array=[]
    sentiment_scores=[]
    conn = psycopg2.connect(database="lemmy",
                            host="172.18.0.3",
                            user="lemmy",
                            password="lemmylemmy",
                            port="5432")
    print('made connection')
    cursor = conn.cursor()
    cursor.execute('select * from comment;')
    all_comments = cursor.fetchall()
    #for i, info in enumerate(all_comments):
        #print('index:', i, '   info:', info)
    cursor.execute('select * from comment;')
    all_comments = cursor.fetchall()
    with open('converted_csv_file.csv', 'w', newline='') as csvfile:
        fieldnames = ['title', 'link']
        writer = csv.DictWriter(csvfile, delimiter='@', fieldnames=fieldnames)
        writer.writeheader()
        for i, info in enumerate(all_comments):
            num_comments= num_comments+1
            num_comments_array.append(num_comments)
            sentiment_dict = sentiment.polarity_scores(info[3])
            sent_1 = '@'+ str(int(sentiment_dict['compound']*100))
            temp = int(sentiment_dict['compound']*100)
            sentiment_scores.append(temp)
            writer.writerow({'title':info[3], 'link':sent_1})
    print(num_comments_array)
    print(sentiment_scores)
    plt.plot(num_comments_array, sentiment_scores)
    plt.xlabel('comment number')
    # naming the y axis
    plt.ylabel('sentiment analysis score')
 
    plt.title('Overall Sentiment Analysis Scores')
 
    plt.savefig('sentiment__scores.png')
    num_comments_array=[]
    sentiment_scores=[]
   # cursor.execute('select * from comment where (datetime.datetime > 2023-08-01 AND datetime.datetime -08-02);')
    all_comments = cursor.fetchall()

def create_a_table(cursor, table_name):
    """This was for playing around, it is not to be used in a running
    lemmy system."""
    create_str = f"""CREATE TABLE {table_name} (
    LastName varchar(255),
    FirstName varchar(255),
    age int
    );
    """
    cursor.execute(create_str)
def clear_terminal():
    subprocess.run('clear',shell=True)
    

schedule.every(1).minutes.do(main)




while True: 
    schedule.run_pending() 
    time.sleep(1) 

if __name__ == '__main__':
    main()
    #break

