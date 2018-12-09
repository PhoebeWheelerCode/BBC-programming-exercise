Feature: Testing getHTTP function return values

    Scenario Outline: Get headers
        Given I have the valid URL <URL>
        When I pass it to the getHTTP function
        Then I expect the function to return an object of the type requests.models.Response, or an error message

    Examples:
        | URL |
        | http://www.bbc.co.uk/iplayer |
        | https://google.com |
        | http://www.oracle.com/technetwork/java/javase/downloads/index.html |
        | https://www.pets4homes.co.uk/images/articles/1646/large/kitten-emergencies-signs-to-look-out-for537479947ec1c.jpg |
