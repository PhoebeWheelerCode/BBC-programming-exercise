from behave import *
from BBC_programming_task import checkURL

@given("I have the URL {URL}")
def have_URL(step, URL):
    step.url = URL

@when("I pass it to the checkURL function")
def check_url(step):
    step.result = checkURL(step.url)
    print (step.url)
    print (checkURL(step.url))

@then("I expect the function to return False")
def expect_result(step):
    assert step.result == False

@then("I expect the function to return True")
def expect_result(step):
    assert step.result == True
