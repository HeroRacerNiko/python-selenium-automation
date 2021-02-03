# Created by nurdi at 2/3/2021
Feature: # Check Amazon cart
  # Enter feature description here

  Scenario: # User is able to add items to cart
    # Enter steps here
    Given Open Amazon page
    When Input dress into Amazon search field
    When Press Enter after input
    When Select first dress
    And Add the dress to cart
    Then Go to cart to check content
