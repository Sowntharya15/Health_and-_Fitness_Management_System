from Main import User_info
from Main import User_details_dao

if __name__=="__init__":
            print("***************Welcome to Health and Fitness Management System***************")
            print("click 1 for Sign-up")
            print("Click 2 for Sign-in")
            choice=int(input("Choice: "))
            if choice =='1':
                u1 = User_info()
                u1.set_userName(input("Enter your Name: "))
                u1.set_Email(input("Enter your Email: "))
                u1.set_password(input("Enter your Password: "))
                u1.set_age(int(input("Enter your age: ")))
                u1.set_gender(input("Enter your Gender: "))
                u1.set_height(input("Enter your Height: "))
                u1.set_weight(input("Enter your Weight: "))
                u1.set_goal(input("Enter your Goal: "))
                
                ud = User_details_dao()
                a = ud.is_user_exist(u1) 
                if a :
                    print("User Already Exist")
                    # want to sign in
                else:
                    ud.insertUserinformation(u1)
                    print("What's your goal ?")
                    print("1. Weightloss")
                    print("2. Weightgain")
                    print("Your choice: ")
                    my_choice = input()
                    if(my_choice==1):
                        ud.insert_goal("Weightloss",u1)
                    elif(my_choice==2):
                        ud.insert_goal("WieghtGain",u1)


            












