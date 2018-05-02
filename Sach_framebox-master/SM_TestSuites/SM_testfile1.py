from nose.plugins.attrib import attr
from SM_Pages import LoginPage
import unittest, datetime
from SM_Utils.Test_context import test_context as tc
from selenium import webdriver
import allure
import pytest
from SM_Utils.Excel_bundle import Excel


class LoginToQSBW(unittest.TestCase):

    def setUp(self):
        self.Failures = []
        self.driver = webdriver.Chrome()
        self.driver.get(tc.test_url)
        self.driver.implicitly_wait(tc.implicit_wait)
        self.driver.maximize_window()

    @attr('sanity')
    @allure.step('step one')
    def test_LoginTest(self):
        """
        Tests Login functionality of the QA Environment for Investis
        """
        ex = Excel()
        testdata = ex.get_test_data_as_dictionary('testdata.xlsx', self.__class__.__name__, self._testMethodName)


        # Load the main page. In this case the home page of Investis QA.
        login_page = LoginPage.LoginPageClass(self.driver)

        # Checks if the word "QA site" is in title
        with pytest.allure.step('step one'):
            assert login_page.is_title_matches(), "QA site did not appeared"

        # Sets username and password"
        with pytest.allure.step('step two'):
            login_page.Login_to_QA(user=testdata['username'], password=testdata['password'])

        # Verifies verify the successful login
        with pytest.allure.step('step three'):
            assert login_page.is_login_successful(user="inv.adminuser"), "Login was not successful"

    #@attr('sanity12')
    #@nose.allure.story('Story2')
    def test_SampleTest(self):
        ex = Excel()
        testdata = ex.get_test_data_as_dictionary('testdata.xlsx', self.__class__.__name__, self._testMethodName)
        print(testdata['username'])
        print(testdata['password'])
        self.assertTrue(expr="1=>2", msg="Pass Message")

    # @attr('fail123')
    #@nose.allure.story('Story3')
    def test_SampleFail(self):
        try:
            self.assertFalse(expr="1=>2", msg="Failed Message")
        except:
            self.Failures.append("This is a failure")
        if len(self.Failures) > 0:
            self.assertFalse(self.Failures)

    def tearDown(self):
        # if sys.exc_info()[0]:  # Returns the info of exception being handled
        #     fail_url = self.driver.current_url
        #     print(fail_url)
        #     now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S-%f')
        #     self.driver.get_screenshot_as_file(
        #     'D:/Sachin_Sandbox/Sach_framebox-master/Sach_framebox-master/tmp/%s.png' % now)  # my tests work in parallel, so I need unique file names
        #     fail_screenshot_url = 'D:/Sachin_Sandbox/Sach_framebox-master/Sach_framebox-master/tmp/%s.png' % now
        #     print(fail_screenshot_url)
        self.driver.close()
        self.Failures.clear()
        print("Setup TearDown Happened")


if __name__ == "__main__":
    unittest.main()
