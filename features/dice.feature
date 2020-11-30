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

  Scenario Outline: rolling one of the six valid faces
    Given the dice roller is set up
    When we roll a bunch of times
    Then eventually <side> should appear

    Examples:
    | side |
    | 1    |
    | 2    |
    | 3    |
    | 4    |
    | 5    |
    | 6    |
