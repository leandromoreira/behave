Feature: showing off complex math

  Scenario: run a simple addition
    Given we a machine to sum two numbers
      when the first one is "3" and the second is "2"
      then the sum is "5"!

  Scenario: run a wrong addition
    Given we a machine to sum two numbers
      when the first one is "3" and the second is "2"
      then the sum is "6"!
