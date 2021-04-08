from pymysql import connect
conn = connect(host='localhost',port =3306,user='root',password='a6151211',database='temp',charset='utf8')
cursor = conn.cursor()
inp = input("请输入")
if inp == '1':
    a='a1'
elif inp =='2':
        a='a2'
else:
        a='a3'






cursor.execute("select * from ac01 where "+a+"=")
print(cursor.fetchall())
cursor.close()