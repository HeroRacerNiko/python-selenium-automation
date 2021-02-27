# Created by nurdi at 2/22/2021
Feature: Amazon Sign in tests
  # Enter feature description here

  Scenario: Sign in page can be opened from popup
    Given Open Amazon page
    When Click on Sign In from popup
    Then Verify Sign In page opens

  Scenario Outline: Sign in tooltip popup stays up for certain amount of time
    Given Open Amazon page
    When Verify tooltip popup appears and clickable
    When Wait for <sec> seconds
    When Verify tooltip popup appears and clickable
    Then Verify tooltip disappears in <sec> seconds
  Examples:
    |sec|
    |2  |
    #|6  |
    #|10 |