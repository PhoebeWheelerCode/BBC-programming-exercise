Feature: Testing URL format validation

Scenario Outline: Invalid URLs
    Given I have the URL <URL>
    When I pass it to the checkURL function
    Then I expect the function to return False

Examples:
    | URL |
    | bad://address |
    | Not An Address |
    | www.fakewebsite.com |

Scenario Outline: Valid URLs
    Given I have the URL <URL>
    When I pass it to the checkURL function
    Then I expect the function to return True

Examples:
    | URL |
    | http://www.bbc.co.uk/iplayer |
    | https://google.com |
    | http://www.bbc.co.uk/missing/thing |
    | http://not.exists.bbc.co.uk/ |
    | http://www.oracle.com/technetwork/java/javase/downloads/index.html |
    | https://www.pets4homes.co.uk/images/articles/1646/large/kitten-emergencies-signs-to-look-out-for537479947ec1c.jpg |
    | http://site.mockito.org/ |
