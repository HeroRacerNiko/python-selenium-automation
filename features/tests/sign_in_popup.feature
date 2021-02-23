# Created by nurdi at 2/22/2021
Feature: Amazon Sign in tests
  # Enter feature description here

  Scenario: Sign in page can be opened from popup
    Given Open Amazon page
    When Click on Sign In from popup
    Then Verify Sign In page opens


