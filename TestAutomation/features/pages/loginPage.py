from features.pages.basePage import BasePage
from features.pages.uimaps.login_page_map import loginPage_locator
from features.pages.homePage import HomePage
from features.lib.constants import base_Constants


class LoginPage(BasePage):

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(30,
                                             "id",
                                             loginPage_locator['username']
            )
        except:
            raise Exception("Incorrect page")

    def login(self, username, password):

        self.fill_out_field("id",
                            "email",
                            username
        )
        self.fill_out_field("id",
                            "password",
                            password
        )
        self.click(10,
                   "id",
                   loginPage_locator['loginButton']
        )

    def validLogin(self):
        self.login(base_Constants['valid_username'], base_Constants['valid_password'])
        return HomePage(self.driver)

    def invalidLogin(self):
        self.login(base_Constants['invalid_username'], base_Constants['invalid_password'])
        return self

    def getLoginErrorText(self):
        loginErrorText = self.wait_for_element_visibility(30,
                                                          "xpath",
                                                          loginPage_locator['loginError']).text
        return loginErrorText
