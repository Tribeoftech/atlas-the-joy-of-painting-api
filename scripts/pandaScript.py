"""Opens the episode dates text file, reads it line by line, 
removes any parentheses, and writes the cleaned lines to a new file."""
import pandas as pd
from sqlalchemy import create_engine

f = open('./datasets/Episode_Dates.txt', 'x')
with open('./datasets/The_Joy_Of_Painting-Episode_Dates.txt', 'r') as f:
	with open('./datasets/Episode_Dates.txt', 'w') as f2:
		for line in f:
			f2.write(line.replace('(', '').replace(')', ''))

"""
Opens and reads in text files containing cleaned episode data, 
removes additional cleanup needed, and writes to new files.

Reads in the colors used and subject matter text files, 
removing remaining cleanup artifacts.

Reads in the cleaned episode dates and writes to a Pandas DataFrame.
Also reads in the cleaned subject matter and colors used data.
"""
f = open('./datasets/Colors_Used.txt', 'x')
with open('./datasets/The_Joy_Of_Painting-Colors_Used.txt', 'r') as f:
	with open('./datasets/Colors_Used.txt', 'w') as f2:
		# iterate through each line to remove '\' and the character after it
		for line in f:
			f2.write(line.replace('\\n', '').replace('\\r', '').replace('"[', '[').replace(']"', ']'))

f = open('./datasets/Subject_Matter.txt', 'x')
with open('./datasets/The_Joy_Of_Painting-Subject_Matter.txt', 'r') as f:
	with open('./datasets/Subject_Matter.txt', 'w') as f2:
		for line in f:
			f2.write(line.replace('"', ''))



df = pd.read_csv('./datasets/Episode_Dates.txt', header=None, sep='\t', names=['title', 'episode_date'])
df2 = pd.read_csv('./datasets/Subject_Matter.txt', sep="\t")
df3 = pd.read_csv('./datasets/Colors_Used.txt', sep="\t")

"""
Write the episode dates, subject matter, and colors used DataFrames to a 
PostgresSQL database using the provided engine connection.

The to_sql() method is used to write each DataFrame to a separate table 
in the database, replacing any existing tables with the same name.

The if_exists='replace' argument replaces existing tables instead of 
appending.
"""
engine = create_engine('postgresql://postgres:hank@localhost:5432/postgres')

df.to_sql('episode_dates', engine, if_exists='replace')
df2.to_sql('subject_matter', engine, if_exists='replace')
df3.to_sql('colors_used', engine, if_exists='replace')