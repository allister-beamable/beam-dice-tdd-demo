Feature: rolling dice
  As a gamer
  In order to have random outcomes
  I want to roll virtual dice

  Scenario: rolling one six-sided die
    Given the dice roller is set up
    When we roll one die
    Then the total number should be between 1 and 6

  Scenario: rolling something other than six
    Given the dice roller is set up
    When we roll a bunch of times
    Then eventually the number should be something other than 6