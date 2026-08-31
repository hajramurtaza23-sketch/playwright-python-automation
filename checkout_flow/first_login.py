class login :
    def __init__(self,page):
        self.page= page
        self.name = page.locator("#user-name")
        self.pwd = page.locator("#password") 
        self.button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")

    def page_link(self):
         self.page.goto("https://www.saucedemo.com")

    def fill_the_input(self,user,pwd):
        self.name.fill(user)
        self.pwd.fill(pwd)
        self.button.click()

        