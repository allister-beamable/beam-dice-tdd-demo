Feature: rolling dice

  Scenario: rolling one six-sided die
    Given our dice rolling interface
    When we ask to roll one die
    Then the total number should be between 1 and 6
