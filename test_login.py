def test_login(page):
    page.goto("https://www.saucedemo.com")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    print("pass")

    assert "inventory" in page.url

def test_login_wrong_password(page):
    page.goto("https://www.saucedemo.com")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("wrong_password")
    page.locator("#login-button").click()

    error_message = page.locator("[data-test='error']")
    # assert error_message.is_visible()
    page.wait_for_timeout(5000) 