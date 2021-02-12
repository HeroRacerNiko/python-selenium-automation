# Created by nurdi at 2/3/2021
Feature: # Check Amazon cart
  # Enter feature description here

  Scenario Outline: User is able to add items to cart
    # Enter steps here
    Given Open Amazon page
    When Input <item> into Amazon search field
    When Press Enter after input
    When Select first search result
    And Add the first element to cart
    Then Go to cart to check content
    Examples:
      |item|
      |dress|
      |coffee mug|
