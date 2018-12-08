Feature: Retrieving desired elements (status code, content length and date-time) from returned headers
    Scenario Outline: Get desired elements from the returned headers
        Given I have a dictionary <dictionary>
        When I pass it to the getElements function
        Then I expect the function to return a dictionary containing the element

    Examples:
        | dictionary |
        | {'Date': 'Sat, 08 Dec 2018 16:28:45 GMT', 'Expires': '-1', 'Cache-Control': 'private, max-age=0', 'Content-Type': 'text/html; charset=ISO-8859-1', 'P3P': 'CP="This is not a P3P policy! See g.co/p3phelp for more info."', 'Content-Encoding': 'gzip', 'Server': 'gws', 'Content-Length': '4867', 'X-XSS-Protection': '1; mode=block', 'X-Frame-Options': 'SAMEORIGIN', 'Set-Cookie': '1P_JAR=2018-12-08-16; expires=Mon, 07-Jan-2019 16:28:45 GMT; path=/; domain=.google.co.uk, NID=150=pxa_fQwJ5fnZuUhNCjxRIiTW_95YZFBr3aIhoNEct7u9PlN3kq__5yhS9HhwafuOenklj_lnzMFs2dLZXfTDfIQ7NTMex4ma60D01wlH2qWZQiJChgdFScQ38o35kLjvy0dJs7bY1Bwd2pGzhD5L0b2jK3Q7IjJsEySt592pPs0; expires=Sun, 09-Jun-2019 16:28:45 GMT; path=/; domain=.google.co.uk; HttpOnly'} |
