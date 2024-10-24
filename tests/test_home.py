
def test_open_home_page(setup):
    driver = setup
    expected_title = "#1 Leader in Individualized, Cross-Channel CX — Insider"
    actual_title = driver.title
    assert actual_title == expected_title, f"Expected title to be '{expected_title}' but got '{actual_title}'"
