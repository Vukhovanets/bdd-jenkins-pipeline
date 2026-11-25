from behave import given, when, then
from pages.login_page import LoginPage


@given('I open the Swag Labs login page')
def open_login_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()


@when('I enter username "{user}" and password "{pwd}"')
def enter_credentials(context, user, pwd):
    context.login_page.login(user, pwd)


@then('I should be redirected to the inventory page')
def verify_redirect(context):
    assert "inventory.html" in context.driver.current_url


@then('I should see an error message "{expected_error}"')
def verify_error_message(context, expected_error):
    assert expected_error in context.login_page.get_error_text()
