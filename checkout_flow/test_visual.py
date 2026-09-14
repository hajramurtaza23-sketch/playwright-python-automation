def test_visual_check(page, assert_snapshot):
    page.goto("https://www.saucedemo.com")
    assert_snapshot(page.screenshot())