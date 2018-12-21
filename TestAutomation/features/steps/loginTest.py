from behave import *
from features.lib.constants import base_Constants
from features.pages.loginPage import LoginPage
from features.pages.homePage import HomePage
from nose.tools import assert_equal


@given('Hudl Coach navigate to the login page')
def step_impl(context):
    context.browser.get(base_Constants['base_url'] + 'login')


@when('the Coach login with valid username and password')
def step_impl(context):
    login_page = LoginPage(context.browser)
    login_page.validLogin()


@then('the Coach is presented with the Home page')
def step_impl(context):
    home_page = HomePage(context.browser)
    assert_equal(home_page.getHomeMenuText(), "Home")


@when('the Coach login with invalid username and password')
def step_impl(context):
    login_page = LoginPage(context.browser)
    login_page.invalidLogin()


@then('the Coach is presented with an error message')
def step_impl(context):
    login_page = LoginPage(context.browser)
    assert_equal(login_page.getLoginErrorText(), "We didn't recognize that email and/or password. Need help?")
