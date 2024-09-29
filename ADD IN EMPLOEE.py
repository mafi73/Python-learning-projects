import mysql.connector

cnx = mysql.connector.connect(user='root', password='1234',
                              host='127.0.0.1',
                              database='test')

print('connectet to database')
name=input('say your name? ')
age=int(input('how old are you?' ))
sex=input('what is your gender? ')
cursor=cnx.cursor()
query=('INSERT INTO people VALUES (\'%s\',\'%s\',%i);')%(name ,sex,age)
cursor.execute(query)

#result=cursor.fetchall()
#for x in cursor:
#    print (x)
cnx.commit()
cursor.close()
cnx.close()  

print('yourdata add on database succesfully') 