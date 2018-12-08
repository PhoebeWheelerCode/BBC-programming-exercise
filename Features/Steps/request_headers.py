import requests
from behave import *
from BBC_programming_task import getHTTP

@given("I have the valid URL {URL}")
def have_URL(step, URL):
    step.url = URL

@when("I pass it to the getHTTP function")
def pass_url(step):
    step.result = getHTTP(step.url)

@then("I expect the function to return an object of the type requests.structures.CaseInsensitiveDict")
def expect_dict(step):
    assert isinstance(step.result, requests.structures.CaseInsensitiveDict)
