# Created by nurdi at 2/22/2021
Feature: Looping through amazon product colors
  # Enter feature description here

  Scenario Outline: Can loop over colors of product
    Given Open amazon url with product <product_id>
    Then Iterate over list of colors, assert, print
    Examples:
    |product_id|
    |B07P5RT34Y|
    |B07BJKRR25|

  Scenario: Can loop over Whole Foods and verify 'regular' in each item
    Given Open amazon Whole Foods page
    When Iterate and verify product name in each element
    Then Iterate and verify keyword "Regular"
