
import pandas as pd
import psycopg2
import os

from pyparsing import col

csv_files = []
try:
    for file in os.listdir(os.getcwd()):
        if file.endswith('.csv'):
            csv_files.append(file)
except:
    pass

dataset_dir = 'datasets'
try:
    mkdir = 'mkdir -p {0}'.format(dataset_dir)
    os.system(mkdir)
except:
    pass


#mv filename directory
for csv in csv_files:
    mv_file = "mv '{0}' {1}".format(csv, dataset_dir)
    os.system(mv_file)

data_path = os.getcwd() + '/'+ dataset_dir + '/'
df = {}
for file in csv_files:
    try:
        df[file] = pd.read_csv(data_path+file)
    except UnicodeDecodeError:
        df[file] = pd.read_csv(data_path+file, encoding="ISO-8859-1")

for k in csv_files:
    dataframe = df[k]
    clean_tbl_name = k.lower().replace(" ", "_").replace("-", "")

    tbl_name = '{0}'.format(clean_tbl_name.split('.')[0])

    dataframe.columns = [x.lower() for x in dataframe.columns]
    replacements = {
    'object': 'varchar',
    'int64': 'int'
    }
    #table schema
    col_str = ", ".join("{} {}".format(n, d) for (n, d) in zip(dataframe.columns, dataframe.dtypes.replace(replacements)))
    host = 'localhost'
    dbname = 'postgres'
    user = 'postgres'
    password = 'mypass123'


    conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (host, dbname, user, password))
    cursor = conn.cursor()
    cursor.execute("drop table if exists %s;" % (tbl_name))
    cursor.execute("create table %s (%s);" % (tbl_name, col_str))
    print(tbl_name)

    dataframe.to_csv(k, header=dataframe.columns, index=False, encoding='utf-8')
    myfile = open(k)
    SQL_STATEMENT = """
    COPY %s FROM STDIN WITH
        CSV
        HEADER
        DELIMITER AS ','
    """
    cursor.copy_expert(sql=SQL_STATEMENT % tbl_name, file=myfile)
    cursor.execute('grant select on table %s to public' % tbl_name)

    conn.commit()
    cursor.close()
    print('table {0} imported to db completed'.format(tbl_name))

print("success!!!")