import pandas as pd
from sqlalchemy import create_engine

# Before reading from The_Joy_Of_Painting-Episode_Dates, we need to remove all
# '(' and ')' characters from the file.
# Instead of doing this directly to the file, we will copy the file to a new file,
# and then read from that file to prevent transforming the original file.
f = open('./datasets/Episode_Dates.txt', 'x')
with open('./datasets/The_Joy_Of_Painting-Episode_Dates.txt', 'r') as f:
	with open('./datasets/Episode_Dates.txt', 'w') as f2:
		for line in f:
			f2.write(line.replace('(', '').replace(')', ''))

# Edits need to be made on the colors_used dataset .txt file, as well.
# Every instance of '\n' and '\r' needs to be removed.
# Also, each array has a stray `'` character before and after it which needs removing.
f = open('./datasets/Colors_Used.txt', 'x')
with open('./datasets/The_Joy_Of_Painting-Colors_Used.txt', 'r') as f:
	with open('./datasets/Colors_Used.txt', 'w') as f2:
		# iterate through each line to remove '\' and the character after it
		for line in f:
			f2.write(line.replace('\\n', '').replace('\\r', '').replace('"[', '[').replace(']"', ']'))

# Last but not least, subject_matter needs some tweeking.
# The titles are all stored in a set of 3 quotes, so lets remove those.
f = open('./datasets/Subject_Matter.txt', 'x')
with open('./datasets/The_Joy_Of_Painting-Subject_Matter.txt', 'r') as f:
	with open('./datasets/Subject_Matter.txt', 'w') as f2:
		for line in f:
			f2.write(line.replace('"', ''))


# Read data from txt file in datasets folder
df = pd.read_csv('./datasets/Episode_Dates.txt', header=None, sep='\t', names=['title', 'episode_date'])
df2 = pd.read_csv('./datasets/Subject_Matter.txt', sep="\t")
df3 = pd.read_csv('./datasets/Colors_Used.txt', sep="\t")

# url connection string for pandas to_sql function
engine = create_engine('postgresql://postgres:hank@localhost:5432/postgres')

df.to_sql('episode_dates', engine, if_exists='replace')
df2.to_sql('subject_matter', engine, if_exists='replace')
df3.to_sql('colors_used', engine, if_exists='replace')