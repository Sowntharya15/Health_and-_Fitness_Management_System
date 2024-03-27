from Modal import User_info
from DAO import User_details

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
    
    ud = User_details()
    ud.insertUserinformation(u1)



print("Enter the E-mail:",end=" ")
mail=input()
print("Enter the Password:",end=" ")
password=input()
us.passwordChecker(mail,password) 




