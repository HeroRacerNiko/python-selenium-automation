# Created by nurdi at 2/10/2021
Feature: Amazon Prime Tests
  This feature is ran on Amazon Prime Services

  Scenario: Verify number of boxes match expected number | Amazon Prime
    # Enter steps here
      Given Open Amazon Prime page
      Then Verify page has 8 boxes

  Scenario: Verify number of links on bestsellers page | Amazon Bestsellers
      Given Open Amazon Prime BestSellers page
      Then Verify page has 5 links