import pytest
from login_page import login

@pytest.fixture
def loginpage(page):
    p = login(page)
    p.direction()
    return p

# def test_run(loginpage):
#     loginpage.inputfield("standard_user", "secret_sauce")
#     assert "inventory" in loginpage.page.url