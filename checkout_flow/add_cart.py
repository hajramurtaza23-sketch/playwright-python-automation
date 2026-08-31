class addcart :
    def __init__(self,page):
        self.page = page
        self.add= page.locator("#add-to-cart-sauce-labs-backpack")
        self.cart=page.locator(".shopping_cart_link")

    def link_to_add(self):
        self.page.goto("https://www.saucedemo.com/inventory.html")

    def click_on_item(self):
        self.add.click()

    def cart_check(self):
        self.cart.click()

class checkout :
    def __init__(self,page):
        self.page = page
        self.check_out = page.locator("#checkout")
    def checkout_btn(self):
        self.check_out.click()

class checkout_info :
    def __init__(self,page):
        self.page = page
        self.first_name = page.locator("#first-name")
        self.last_name = page.locator("#last-name")
        self.zip= page.locator("#postal-code")
        self.cont_button = page.locator("#continue")
        self.finish_btn= page.locator("#finish")

    def info (self,firstname,lastname,zp):
        self.first_name.fill(firstname)
        self.last_name.fill(lastname)
        self.zip.fill(zp)
        self.cont_button.click()

    def finish(self):
        self.finish_btn.click()


        
        