from behave import *
from BBC_programming_task import getElements

@given("I have a dictionary {dictionary}")
def have_URL(step, dictionary):
    step.dictionary = eval(dictionary)

@when("I pass it to the getElements function")
def check_url(step):
    step.result = {}
    step.result = getElements(step.dictionary)

@then("I expect the function to return a dictionary containing the elements")
def expect_false(step):
    assert set(step.dictionary.keys()) == set(['status-code', 'content-length', 'date-time'])
