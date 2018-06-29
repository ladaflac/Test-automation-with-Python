from selenium.webdriver.common.by import By


class NewPostPageLocators:
    # BACK_TO_BLOG_LINK = By.ID, 'blog-link'    # ovo necemo (ponovo) testirati u ovom testu
    NEW_POST_FORM = By.ID, 'post-form'
    TITLE_FIELD = By.ID, 'title'
    CONTENT_FIELD = By.ID, 'content'
    SUBMIT_BUTTON = By.ID, 'create-post'

