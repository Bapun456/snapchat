# import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class LoginPage:

    def __init__(self,driver):
        self.driver=driver
        self.email=(By.XPATH,"//input[@class='SignInForm_input__CtA7_']")
        self.login_button=(By.XPATH,"//button[@class='ColoredButton_blueButton__IeoF4 buttons_sdsButton__57EIz']")

    def log(self,email):
        wait=WebDriverWait(self.driver,30)
        wait.until(ec.visibility_of_element_located(self.email)).send_keys(email)
        wait.until(ec.element_to_be_clickable(self.login_button)).click()