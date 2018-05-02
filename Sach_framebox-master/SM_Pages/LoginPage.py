from selenium import webdriver
from SM_Pages.BasePage import BasePageClass
from selenium.webdriver.common.by import By


class LoginPageClass(BasePageClass):
    """Home page action methods come here. """


    LOGIN_BUTTON = (By.XPATH, "//*[@id='block-bootstrap-account-menu']//a[text()='Log in']")
    USER_NAME = (By.ID, "edit-name")
    USER_PSWD = (By.ID, "edit-pass")
    BTN_LOGIN = (By.ID, "edit-submit")

    #Declares a variable that will contain the retrieved text
    #search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "Log in | Road Runner Site" in self.driver.title

    def click_Login_button(self):
        """Triggers the search"""
        element = self.driver.find_element(self.LOGIN_BUTTON)
        element.click()

    def Login_to_QA(self, user, password):
        """Triggers the Login functionality"""
        userid_element = self.driver.find_element(*LoginPageClass.USER_NAME)
        userid_element.send_keys(user)
        userpswd_element = self.driver.find_element(*LoginPageClass.USER_PSWD)
        userpswd_element.send_keys(password)
        login_btn = self.driver.find_element(*LoginPageClass.BTN_LOGIN)
        login_btn.click()

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "Log in" not in self.driver.page_source

    def is_login_successful(self, user):
        return user+" | Road Runner Site" in self.driver.title
