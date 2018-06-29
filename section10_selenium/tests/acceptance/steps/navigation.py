from behave import *
from selenium import webdriver

from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.homepage import Homepage
from tests.acceptance.page_model.new_post_page import NewPostPage

use_step_matcher('re')

@given('I am on the Homepage')
def step_impl(context):
    context.driver = webdriver.Chrome('C:\Windows\Webdriver\chromedriver.exe')    # if no arguments, it looks for the driver in the PATH; other specific location can be written in ()
    page = Homepage(context.driver)
    context.driver.get(page.url)

@given('I am on the Blog page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:\Windows\Webdriver\chromedriver.exe')    # if no arguments, it looks for the driver in the PATH; other specific location can be written in ()
    page = BlogPage(context.driver)
    context.driver.get(page.url)

@given('I am on the new post page')
def step_impl(context):
    context.driver = webdriver.Chrome('C:\Windows\Webdriver\chromedriver.exe')
    page = NewPostPage(context.driver)
    context.driver.get(page.url)

@then('I am redirected to the Blog page')
def step_impl(context):
    expected_url = BlogPage(context.driver).url
    assert context.driver.current_url == expected_url

@then('I am redirected to the Homepage')
def step_impl(context):
    expected_url = Homepage(context.driver).url
    assert context.driver.current_url == expected_url


# step_impl - 2 equal function names would normally be a problem, but
# with decorators they are not