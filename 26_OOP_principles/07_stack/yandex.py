import mysql.connector # pip install mysql-connector-python
assingnelist =[]

for i in range(10000,10006,1):
    assingnelist.append(i)

days  =  7
mydb = mysql.connector.connect(host="localhost", user="user", passwd="pass", database="dbname")
cursor = mydb.cursor(dictionary=True)
sql_1 = "(SELECT key,asignee FROM ST_TASKS WHERE STATUS IN ('Open', 'On support side', 'Verifying') " \
      "AND DATEDIFF(NOW(),CREATED) > {days};".format(days= days)
cursor.execute(sql_1)
assigns = cursor.fetchall()

sql_2 = "Select count(k.key) as needtask, k.asignee from (SELECT key,asignee FROM ST_TASKS WHERE STATUS IN ('Open', 'On support side', 'Verifying') " \
      "AND DATEDIFF(NOW(),CREATED) > {days}) k group by k.asignee;".format(days= days)
cursor.execute(sql_2)
a = cursor.fetchall()

for row in assigns:
    