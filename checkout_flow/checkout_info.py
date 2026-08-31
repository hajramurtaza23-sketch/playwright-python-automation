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