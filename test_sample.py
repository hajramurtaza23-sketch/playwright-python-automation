from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)  # headless=False = you SEE the browser
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.saucedemo.com")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    print("pass")
    assert "inventory" in page.url
    print("Login test passed! ✅")
    print(page.url)

# other way to get locator 
#page.get_by_placeholder("Username")
# page.get_by_role("button", name="Login")
# page.get_by_text("Login")
    
    page.wait_for_timeout(5000) 

    browser.close()




    