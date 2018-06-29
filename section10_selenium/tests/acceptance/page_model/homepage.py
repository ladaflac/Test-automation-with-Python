from tests.acceptance.locators.homepage import HomepageLocators
from tests.acceptance.page_model.base_page import BasePage


class Homepage(BasePage):   # inherrits the title from class BasePage
    # init not needed anymore after we added inherritance from BasePage
    # def __init__(self, driver):
    #    self.driver = driver

    @property   # enables the method to be accessible without the brackets (used only if there are no input args)
    def url(self):
        # return 'http://127.0.0.1:5000/'
        return super(Homepage, self).url + '/'      # access to the property of super class in context of the current object

    @property
    def blog_link(self):
        return self.driver.find_element(*HomepageLocators.NAVIGATION_LINK)
