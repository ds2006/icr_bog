# This program takes in a csv file and outputs that same file along with the sentiment analysis results

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import csv
import pandas as pd


sentiment = SentimentIntensityAnalyzer()

## read in the csv file given the path
df=pd.read_csv("file_name.csv")
# grab the column with the comments
specific_column=df["title"]
# get the length of that column - 1 so that you can iterate through that row
numofcolumns=(len(specific_column))-1

# set the output file
f = open('output_file_name.csv', 'w')

# iterate through all of the rows in that column
for i in specific_column:
  # get the polarity scores for that sentence/phrase
  sentiment_dict = sentiment.polarity_scores(i)
  # get the compound score for the phrase and multiply it by 100 to get a number between -100 and 100
  sent_1 = sentiment_dict['compound']*100
  # 
  writer = csv.writer(f)
  # write that out into the csv file with the delimeter as the @ sign 
  writer.writerow([i+"@" +str(int(sent_1))+"%"])


f.close()


