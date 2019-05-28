Feature: Delete button

  Scenario: After a successful search, we have a list with the tuits.

	Given  I have the list with the tuits
	When I press delete button
	Then I do no￿t have the list with the tuits
