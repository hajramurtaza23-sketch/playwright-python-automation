# # class Cat:
# #     def __init__(self, name, color):
# #         # store name and color as attributes, same way Dog did
# #         self.name = name
# #         self.color = color


# #     def meow(self):
# #         # print something using self.name
# #         print(f"{self.name} say cat")


# # my_cat = Cat("muffion", "black")
# # my_cat.meow() 


# class bank:
#     def __init__(self,owner,balance): #  init is a bulit in method used for creting object  The __init__() method is called automatically
#         self.owner = owner
# #The self parameter must be the first parameter of any method in the class. 
# #The self parameter is a reference to the current instance of the class.
# #It is used to access properties and methods that belong to the class
# #Note: While you can use a different name, it is strongly recommended to use self as it is the convention in Python and makes your code more readable to others.
#         self.balance = balance

#     def deposit(self,amount): # A method is just a function that belongs to a class, and can only be used through an object.
        
#         self.balance =  self.balance + amount
#         print(f"{self.owner} deposited {amount} now your total balance is {self.balance}")


# acc = bank("hajra",1000)
# acc.deposit(30:

class loginpage :
    def __init__(self,page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.button = page.locator("#login-button")


    def goto(self):
        self.page.goto("https://www.saucedemo.com")

    def logindetail(self,user,pwd):
        self.username.fill(user)
        self.password.fill(pwd)
        self.button.click()


def test_login(page):
    log_in = loginpage(page)
    log_in.goto()
    log_in.logindetail("standard_user", "secret_sauce")
    
    assert "inventory" in page.url



        
    