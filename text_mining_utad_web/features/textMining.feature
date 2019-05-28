Feature: Website

  Scenario: Search an user tweets.

	  Given I have not entered an user
	  Given I cant see the list with the tuits
	  When I introduce an user
	  When I introduce a language
	  When I press search button
	  Then I can see the list with the tuits


  Scenario: After a successful search, we have a list with the tuits
    Given  I have the list with the tuits
	When I press delete button
	Then I do not have the list with the tuits