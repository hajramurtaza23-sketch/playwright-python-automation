class login :
    def __init__(self,page ):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")

    def direction(self):
        self.page.goto("https://www.saucedemo.com")

    def inputfield (self,user,pwd):
        self.username.fill(user)
        self.password.fill(pwd)
        self.button.click()

        