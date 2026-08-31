class checkout :
    def __init__(self,page):
        self.page = page
        self.check_out = page.locator("#checkout")
    def checkout_btn(self):
        self.check_out.click()