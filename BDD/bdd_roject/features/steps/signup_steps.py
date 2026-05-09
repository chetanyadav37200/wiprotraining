import allure
from behave import given, when, then

from pages.signup_page import SignupPage
from utils.logger import LogGen
from utils.screenshot_util import ScreenshotUtil

logger=LogGen.loggen()
@given('User launches Demoblaze application')
def step_impl(context):
    logger.info('Demoblaze url loaded')

@when('User clicks on Sign up menu')
def step_impl(context):
    logger.info("Step : Click Sign UP Menu")
    context.signup_page=SignupPage(context.driver)
    context.signup_page.click_signup_menu()

@when('User enters signup username "{username}"')
def step_impl(context, username):
    logger.info(f"Step : Enter Username : {username}")
    context.signup_page.enter_username(username)

@when('User enters signup password "{password}"')
def step_impl(context, password):
    logger.info(f"Step : Enter Password : {password}")
    context.signup_page.enter_password(password)

@when('User clicks Signup button')
def step_impl(context):
    logger.info(f"Step :Click Signup button")
    context.signup_page.click_signup_button()

@then('User should see signup success message')
def step_impl(context):
    logger.info("Step : Verify Successful Signup")
    context.signup_page.verify_successful_signup()
    screenshot_path = (ScreenshotUtil.capture_screenshot(context.driver, "successful_login"))
    logger.info(f"Screenshot Captured : {screenshot_path}")
    allure.attach(context.driver.get_screenshot_as_png(), name="Successful Login",
                  attachment_type=allure.attachment_type.PNG)