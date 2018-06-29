from behave import *
from selenium import webdriver

from tests.acceptance.page_model.new_post_page import NewPostPage

# steps in this file executed by selenium

use_step_matcher('re')  # re = regular expression, from behave library


@when('I click the Blog link')
def step_impl(context):
    link = context.driver.find_element_by_id('blog-link')
    link.click()

@when('I click the Homepage link')
def step_impl(context):
    link = context.driver.find_element_by_id('home-link')
    link.click()


@when('I input "(.*)" in the "(.*)" field')
def step_impl(context, content, field_name):
    page = NewPostPage(context.driver)
    page.form_field(field_name).send_keys(content)

@when('I submit the data')
def step_impl(context):
    page = NewPostPage(context.driver)
    page.submit_button.click()
