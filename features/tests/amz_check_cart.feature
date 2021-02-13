# Created by nurdi at 2/3/2021
Feature: # Check Amazon cart
  # Enter feature description here

  Scenario Outline: User is able to add items to cart
    # Enter steps here
    Given Open Amazon page
    When Input <item> into Amazon search field
    When Press Enter after input
    When Select first search result
    And Add the first element to cart with default size and <quantity> quantity
    Then Go to cart to check content
    Examples:
      |item|quantity|
      |shoes|1       |
      |dress|1      |
      |coffee mug|1  |
      |shoes|5       |
      |dress|5      |
      |coffee mug|5  |