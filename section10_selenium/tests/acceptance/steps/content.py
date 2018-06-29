from behave import *
# from selenium.webdriver.common.by import By   # not needed after replacing (By.TAG_NAME, 'h1') with (*HomepageLocators.TITLE)
                                                # so selenium is not needed in this file anymore
# from tests.acceptance.locators.homepage import HomepageLocators   # not needed after adding the page model and locators file
# from tests.acceptance.page_model.homepage import Homepage     # not needed after replacing Homepage with BasePage
from tests.acceptance.page_model.base_page import BasePage
from tests.acceptance.page_model.blog_page import BlogPage

use_step_matcher('re')


@then('The title is visible')
def step_impl(context):
    # title_tag = context.driver.find_element(By.TAG_NAME, 'h1')
    # title_tag = context.driver.find_element(*HomepageLocators.TITLE)   # find_element expects 2 args; * enables that the tuple gets deconstructed into 2 separate elements and pass them to the method
                                                                        # not needed after adding the page model and locators file
    page = BasePage(context.driver)
    assert page.title.is_displayed()     # check that it is visible, not only present on the page


@then('The title is "(.*)"')    # @then or @step - @step means it can be used in any step (given, when or then)
def step_impl(context, content):
    # title_tag = context.driver.find_element(By.TAG_NAME, 'h1')
    # title_tag = context.driver.find_element(*HomepageLocators.TITLE) # not needed after adding the page model and locators file
    page = BasePage(context.driver)
    assert page.title.text == content


@then('The posts section is present on the page')
def step_impl(context):
    page = BlogPage(context.driver)
    assert page.posts_section.is_displayed()

@then('The post with "(.*)" is visible on the Blog page')
def step_impl(context, title):
    page = BlogPage(context.driver)
    posts_with_title = [post for post in page.posts if post.text == title]
    assert len(posts_with_title) > 0    # check that the post with the passed title is there
    assert all([post.is_displayed() for post in posts_with_title])  # check that our post is visible
