# this DAO class has methods to modify data in user_details table in db 
import mysql.connector as my
# from import User_info

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
        query= "insert into User_details(userName,mail_Id,password,age,gender,height,weight,goal) values (%s, %s, %s, %s, %s, %s, %s, %s)"
        dummy = (u1.get_userName(),u1.get_Email(),u1.get_password(),u1.get_age(), u1.get_gender(), u1.get_height(), u1.get_weight(), u1.get_goal())
        key = con.cursor()
        key.execute(query,dummy)
        print("Inserted Successfully")
        
    def is_user_exist(u1):
        con = my.connect(host='localhost',user='root',password = 'Sow15', database = 'wellness')
        query = "select mail_Id from user_details where mail_Id = %s "
        dummy = u1.get_Email()
        key = con.cursor() 
        key.execute(query,dummy)
        if query != None:
            return True 
        else:
            return False
    def insert_goal(choice,u1):
        con = my.connect(host='localhost',user='root',password = 'Sow15', database = 'wellness')        
        query = "insert into Goal_Setting (Goal_Name,userId) values (%s, ) "

        
        


        



