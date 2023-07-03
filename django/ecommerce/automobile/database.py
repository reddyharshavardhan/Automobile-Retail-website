import pandas as pd
import mysql.connector

conn = mysql.connector.connect(host="localhost",database="djangoecom",user="root",password="",port=3306)
cursor = conn.cursor()
data = pd.read_csv("automobile_product.csv")
data = data.values.tolist()
count = 0
for i in data:
    query = """INSERT INTO automobile_product(
        slug,name,product_image,small_description,quantity,description,original_price,selling_price,status,trending,tag,meta_title,meta_keywords,meta_description,created_at,Category_id 
    )
    values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","{}","1");""".format(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9],i[10],i[11],i[12],i[13],i[14],i[15])
    cursor.execute(query)
    conn.commit()
    print(count)
    count+=1


conn.close()