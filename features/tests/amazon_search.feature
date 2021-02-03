# Created by nurdi at 1/24/2021
Feature: # Amazon Search Test
  # Enter feature description here

  # This is a Gherkin file (.feature)
    # Gherkin file should have key words: feature, scenario
  # Given = precondition
  # When = action
  # and == when (or copy of step above)
  # Then = verify


  Scenario Outline: The user can search for a <search_query>
    Given Open Amazon page
    When Input <search_query> into Amazon search field
    And Click on Amazon search icon
    Then Product results for <result> are shown on Amazon
    And Page URL has <search_query> in it
    Examples:
    |search_query|result   |
    |Watches     |"Watches"|
    |Dress       |"Dress"  |







#  Scenario: The user can search for a Watch
#    Given Open Amazon page
#    When Input Watches into Amazon search field
#    And Click on Amazon search icon
#    Then Product results for "Watches" are shown on Amazon
#    And Page URL has Watches in it
#
#
#  Scenario: The user can search for a Dress
#    Given Open Amazon page
#    When Input Dress into Amazon search field
#    And Click on Amazon search icon
#    Then Product results for "Dress" are shown on Amazon
#    And Page URL has Dress in it