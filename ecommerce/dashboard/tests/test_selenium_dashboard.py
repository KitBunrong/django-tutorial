import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

"""
Behide the scene, test data base are build, and then 
it add a new user to admin table and run the test and then
the database rollback to the initial state. [end]
"""
# @pytest.mark.selenium
# def test_create_new_admin_user(create_admin_user):
#     assert create_admin_user.__str__() == "asdmin"


@pytest.mark.selenium
def test_dashboard_admin_login(live_server, db_fixture_setup, chrome_browser_instance):

    # i = User.objects.get(id=1)
    # print(i.username, i.password)
    
    browser = chrome_browser_instance

    browser.get(("%s%s" % (live_server.url, "/admin/login/")))

    user_name = browser.find_element(By.NAME, "username")
    user_password = browser.find_element(By.NAME, "password")
    submit = browser.find_element(By.XPATH, "//input[@value='Log in']")

    user_name.send_keys("asdmin")
    user_password.send_keys("asdFasdf")
    submit.send_keys(Keys.RETURN)

    assert "Site administration" in browser.page_source
