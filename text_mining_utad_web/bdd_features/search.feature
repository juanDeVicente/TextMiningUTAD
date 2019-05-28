Feature: Search button

  Scenario: Search an user tuits.

	Given I have entered an user
	When I press search button
	Then I can see the list with the tuits
