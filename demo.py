
from operator import index
import pandas as pd
import psycopg2

df = pd.read_csv("./source_csv/The Joy Of Painiting - Colors Used.csv")
#print(df.head())

# clean file name
file = "The Joy Of Painiting - Colors Used.csv"
clean_tbl_name = file.lower().replace(" ", "_").replace("-", "")
print(clean_tbl_name)
df.columns = [x.lower() for x in df.columns]
#print(df.columns)
# print(df.dtypes)

replacements = {
    'object': 'varchar',
    'int64': 'int'
}

col_str = ", ".join("{} {}".format(n, d) for (n, d) in zip(df.columns, df.dtypes.replace(replacements)))
# print(col_str)

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=mypass123")
cursor = conn.cursor()
#print(1)

cursor.execute("drop table if exists colors_used")
cursor.execute("create table colors_used(id int, painting_index int, img_src varchar, painting_title varchar, season int, episode int, num_colors int, youtube_src varchar, colors varchar, color_hex varchar, black_gesso int, bright_red int, burnt_umber int, cadmium_yellow int, dark_sienna int, indian_red int, indian_yellow int, liquid_black int, liquid_clear int, midnight_black int, phthalo_blue int, phthalo_green int, prussian_blue int, sap_green int, titanium_white int, van_dyke_brown int, yellow_ochre int, alizarin_crimson int)")

df.to_csv('the_joy_of_painiting__colors_used.csv', header=df.columns, index=False, encoding='utf-8')
myfile = open('the_joy_of_painiting__colors_used.csv')
print(1)

SQL_STATEMENT = """
    COPY colors_used FROM STDIN WITH
        CSV
        HEADER
        DELIMITER AS ','
"""
cursor.copy_expert(sql=SQL_STATEMENT, file=myfile)
cursor.execute('grant select on table colors_used to public')
conn.commit()
cursor.close()
print(2)