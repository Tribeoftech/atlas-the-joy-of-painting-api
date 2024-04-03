import pandas as pd
import pymysql

# Read data from source files
episodes_data = pd.read_csv('episodes.csv')
artists_data = pd.read_json('artists.json')
techniques_data = pd.read_excel('techniques.xlsx')

# Transform data
# Assuming data transformation steps here to match the database schema

# Establish database connection
connection = pymysql.connect(host='localhost',
                             user='your_username',
                             password='your_password',
                             database='joy_of_painting')

# Insert data into database
try:
    with connection.cursor() as cursor:
        # Insert episodes data
        for index, row in episodes_data.iterrows():
            sql = "INSERT INTO Episode (title, season, episode_number, air_date, description) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (row['title'], row['season'], row['episode_number'], row['air_date'], row['description']))
        
        # Insert artists data
        for index, row in artists_data.iterrows():
            sql = "INSERT INTO Artist (name) VALUES (%s)"
            cursor.execute(sql, (row['name'],))
        
        # Insert techniques data
        for index, row in techniques_data.iterrows():
            sql = "INSERT INTO PaintingTechnique (name) VALUES (%s)"
            cursor.execute(sql, (row['name'],))
    
    # Commit changes
    connection.commit()
    print("Data successfully imported into the database.")

except Exception as e:
    print(f"Error: {e}")
    connection.rollback()

finally:
    connection.close()