# Created by nurdi at 2/27/2021
Feature: Practicing with multiple windows: store, switch, close
  # Enter feature description here

  Scenario: Amazon 404 leads to dogs blogs. Switch, close
    Given Open amazon url with product 'RANDOM_PR_ID_123'
    When Store original window
    And Click on 404 blog
    And Switch to the newly opened window
    Then User can close new window and switch back to the original

  Scenario: User can open and close Amazon Applications page
    Given Open Amazon T&C page
    When Store original window
    And Click on Amazon applications link
    And Switch to the newly opened window
    Then Verify Amazon app page is opened
    And User can close new window and switch back to the original

  Scenario: Iterate over Best Sellers
    Given Open Amazon Prime BestSellers page
    Then Iterate over bestseller links, verify changes in title