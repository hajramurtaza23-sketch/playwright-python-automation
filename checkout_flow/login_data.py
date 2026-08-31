import pytest
from first_login import login
from add_cart import addcart 
from checkout_page import  checkout 
from checkout_info import checkout_info

@pytest.mark.parametrize("username,password,should_check",[
    ("standard_user", "secret_sauce", True),
    ("standard_user",  "secret_sauce", True),
])
def test_login_data(page,username,password,should_check):
    log = login(page)
    log.page_link()
    log.fill_the_input(username,password)
    if should_check :
        assert "inventory.html" in page.url
        add_to_cart=addcart(page)
        add_to_cart.click_on_item()
        add_to_cart.cart_check()
        assert "cart.html" in page.url
        check= checkout(page)
        check.checkout_btn()
        assert "checkout-step-one.html" in page.url
        information = checkout_info(page)
        information.info("hajra","abbasi","4400")
        assert "checkout-step-two.html" in page.url
        information.finish()
        assert "checkout-complete.html" in page.url
        page.wait_for_timeout(5000) 

    else:
        assert log.error_message.is_visible()

