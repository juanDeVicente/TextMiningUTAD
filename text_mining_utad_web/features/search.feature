Feature: Search button

  Scenario: Search an user tuits.
	  Given I have not entered an user
	  Given I cant see the list with the tuits
	  When I introduce an user
	  When I introduce a language
	  When I press search button
	  Then I can see the list with the tuits
