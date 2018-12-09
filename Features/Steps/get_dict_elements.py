from behave import *
from BBC_programming_task import getElements

class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

response = MockResponse({"key1": "value1"}, 200)

@given("I have a Response object and URL")
def have_URL(step):
    step.response = response
    step.url = 'http://www.google.co.uk'

@when("I pass it to the getElements function")
def check_url(step):
    step.result = {}
    step.result = getElements(step.url, step.dictionary)

@then("I expect the function to return json containing the elements")
def expect_elements(step):
    print(step.dictionary.keys())
    assert set(step.dictionary.keys()) == set(["Url", "Status_code", "Content_length", "Date"])
