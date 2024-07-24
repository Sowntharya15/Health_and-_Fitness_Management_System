class User_info():
    #instance variable :
    userName = None
    Email = None
    password = None
    age = None
    gender = None
    height = None
    weight = None
    goal = None
    def set_userName(self,userName):
        self.userName = userName
    def set_Email(self,Email):
        self.Email = Email
    def set_password(self,password):
        self.password = password
    def set_age(self,age):
        self.age = age 
    def set_gender(self,gender):
        self.gender = gender 
    def set_height(self,height):
        self.height = height 
    def set_weight(self,weight):
        self.weight = weight
    def set_goal(self,goal):
        self.goal = goal 
    def get_userName(self):
        return self.userName 
    def get_Email(self):
        return self.Email
    def get_password(self):
        return self.password 
    def get_age(self):
        return self.age
    def get_gender(self):
        return self.gender
    def get_height(self):
        return self.height
    def get_weight(self):
        return self.weight
    def get_goal(self):
        return self.goal
    
    def show_details(self):
        print("USER_NAME: ",self.userName)
        print("E-MAIL ID: ",self.Email)
        print("PASSWORD: ",self.password)
        print("AGE: ",self.age)
        print("GENDER: ",self.gender)
        print("HEIGHT: ",self.height)
        print("WEIGHT: ",self.weight)
        print("GOAL: ",self.goal)


    






    