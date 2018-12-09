Feature: Retrieving desired elements (status code, content length and date-time) from returned headers
    Scenario Outline: Get desired elements from the returned headers
        Given I have a Response object and URL
        When I pass it to the getElements function
        Then I expect the function to return json containing the elements
