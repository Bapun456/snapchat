import pytest

from pages.test_login_page import LoginPage
from utills.excel_reader import get_test_data

test_data=get_test_data(r"C:\Users\91773\PycharmProjects\Python snapchat\data\snapchat_m.xlsx","Sheet1")

@pytest.mark.parametrize('url,email',test_data)
def test_script(driver,url,email):
    driver.get(url)

    login=LoginPage(driver)
    login.log(email)