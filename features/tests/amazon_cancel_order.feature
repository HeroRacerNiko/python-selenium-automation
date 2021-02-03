# Created by nurdi at 2/2/2021
  # The "Click on search bar is not really necessary as test runs demonstrate, but left for practice

Feature: Amazon help search bar test
  # Enter feature description here
  #This feature tests amazon cancellations

  Scenario Outline: User can search <command> in help search bar
    # Enter steps here
    Given Open Amazon customer help page
    When Click on search bar
    When Enter <command> into search bar
    And Press ENTER in search bar after input
    Then <result> should be visible
    Examples:
      |command     |result        |
      |Cancel order|Cancel Items or Orders|
      |Cancel      |Cancel Items or Orders|
      |Return      |Returns & Refunds     |
      |Tracking information |Where's My Stuff?     |
      |Where is my order    |Where's My Stuff?     |