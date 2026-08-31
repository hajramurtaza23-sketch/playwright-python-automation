import pytest
from login_page import login

@pytest.mark.parametrize("user,pwd,should_match",[
    ("standard_user", "secret_sauce", True),
    ("standard_user",  "secret_sauce", True),
])

def test_logindata(page,user,pwd,should_match):
    log_in = login(page)
    log_in.direction()
    log_in.inputfield(user,pwd)
    if should_match :
        assert "inventory" in page.url
    else:
        assert log_in.error_message.is_visible()


