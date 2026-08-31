def test_run(loginpage):
    loginpage.inputfield("standard_user", "secret_sauce")
    assert "inventory" in loginpage.page.url