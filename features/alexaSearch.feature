Feature: alexaSearch

    Scenario: As a Customer when I search for Alexa, I want to see if the third option on the second page is available for purchase and can be added to the cart.
        Given I log in to the Amazon Shop app
        When I make a search
        #And I use the 'Alexa' keyword
        #And I navigate to the second page
        #And I select the third item
        Then I am able to add it to the cart