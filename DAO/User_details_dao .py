# this DAO class has methods to modify data in user_details table in db 
import mysql.connector as my

class User_details:
    def passwordChecker(mail,password):
        con = my.connect(host = 'localhost', user = 'root', password = "Sow15", database = 'wellness')
        query = "select roles from user_details where mail_id = %s and password = %s"
        key = con.cursor()
        user=(mail,password)
        m = key.execute(query,user)
        rows = key.fetchall()
        # for i in rows :
        #     print(i)
        if len(rows)==0:
            print("Password is incorrect")
        else:
            print("Password is correct")

    def insertUserInformation(u1):
        con = my.connect(host='localhost',user='root',password = 'Sow15', database = 'wellness')
        query= "insert into User_details(userName,mail_Id,password,age,gender,height,weight,goal) values (u1,)"
        