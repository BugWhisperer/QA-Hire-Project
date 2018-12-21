from features.pages.basePage import BasePage
from features.pages.uimaps.home_page_map import homePage_locator


class HomePage(BasePage):
    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    def _verify_page(self):
        try:
            self.wait_for_element_visibility(30,
                                             "xpath",
                                             homePage_locator['home_menu']
        )
        except:
            raise Exception("Incorrect page")

    def getHomeMenuText(self):
        homeMenuText = self.find_element("xpath",
                                         homePage_locator['home_menu']).text
        return homeMenuText
