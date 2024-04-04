#!/usr/bin/python3
# Extract

import pandas as pd

# Create dataframes
subject_df = pd.read_csv('./resources/subject', sep=',')
colors_df = pd.read_csv('./resources/colors', sep=',')
dates_df = pd.read_csv('./resources/modified_dates', sep=',', names=['title', 'date', 'other'])


## Transform

# Delete unnecessary columns
subject_df = subject_df.drop(['EPISODE', 'TITLE', 'GUEST', 'DIANE_ANDRE', 'STEVE_ROSS'], axis=1)
subject_df.drop(list(subject_df.filter(regex = 'FRAME')), axis = 1, inplace = True)

# Create list of all subjects (drop first column)
cols = subject_df.columns.tolist()[1:]
# delete empty
for col in cols:
	if (subject_df[col].mean() == 0):
		subject_df = subject_df.drop(col, axis=1)

# Lowercase all data in columns
subject_df.columns = subject_df.columns.str.lower()

# For each row, add column name to list if value is 1
def get_subjects(row):
	cols = []
	for col in row.index:
		if row[col] == 1:
			cols.append(col)
	return cols

# Create new column for each row based of get_subjects function
subject_df['subject_list'] = subject_df.apply(lambda row: get_subjects(row), axis=1)

# Convert subject_list column to string
subject_df['subject_list'] = subject_df['subject_list'].apply(lambda x: ', '.join(x))

# Remove every column except for subject_list
subject_df = subject_df.drop(subject_df.columns.difference(['subject_list']), axis=1)

# Create same index in all dataframes
subject_df['id'] = range(0, len(subject_df))


# Delete unnecessary columns
colors_df.drop(['Unnamed: 0', 'painting_index', 'season', 'episode', 'color_hex', 'colors', 'painting_title', 'youtube_src'], axis=1, inplace=True)

# Find list of all possible colors
cols = colors_df.columns.tolist()[3:]
# Sum number of colors for each painting
colors_df['verify_colors'] = colors_df[cols].sum(axis=1)
# Verify that calculated number of colors matches given number of colors
colors_df.loc[~(colors_df['verify_colors'] == colors_df['num_colors'])]

# Since verification passed, delete both columns
colors_df.drop(['verify_colors', 'num_colors'], axis=1, inplace=True)

# Lowercase all data in columns
colors_df.columns = colors_df.columns.str.lower()

# For each row, add column name to list if value is 1
def get_colors(row):
	cols = []
	for col in row.index:
		if row[col] == 1:
			cols.append(col)
	return cols

# Create new column for each row based of get_colors function
colors_df['color_list'] = colors_df.apply(lambda row: get_colors(row), axis=1)

# Convert color_list column to string
colors_df['color_list'] = colors_df['color_list'].apply(lambda x: ', '.join(x))

# Remove every column except for color_list
colors_df = colors_df.drop(colors_df.columns.difference(['color_list']), axis=1)

# Create same index in all dataframes
colors_df['id'] = range(0, len(colors_df))


dates_df.drop(['other'], axis=1, inplace=True)
dates_df['id'] = range(0, len(dates_df))

# id should be first column
dates_df = dates_df[['id', 'title', 'date']]


# Merge dataframes based on ep_id
two_df = pd.merge(dates_df, colors_df)
three_df = pd.merge(two_df, subject_df)

# All column names are lowercse
three_df.columns = three_df.columns.str.lower()


# Load

import sqlite3

# Define column types
col_list = ['id INTEGER NOT NULL PRIMARY KEY', 'title VARCHAR(50) NOT NULL UNIQUE', 'date VARCHAR(20) NOT NULL UNIQUE', 'color_list BLOB NOT NULL', 'subject_list BLOB NOT NULL']
col_list = ','.join(col_list)

# If database exists, connect to it - otherwise create it and then connect
conn = sqlite3.connect('./happy_lil_trees.db')
cursor = conn.cursor()

# Create table with column names and values based on col_str
cursor.execute('CREATE TABLE IF NOT EXISTS episodes(col_str)')


import sqlalchemy

# Connect to database
engine = sqlalchemy.create_engine('sqlite:///./happy_lil_trees.db')

# Convert lists to strings
three_df = three_df.applymap(str)

# Add data in dataframe to table
three_df.to_sql('episodes', engine, if_exists='replace', index=False)



