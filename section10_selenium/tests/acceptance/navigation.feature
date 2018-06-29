Feature: Test navigation between the pages

  Scenario: Can go from Homepage to Blog page
    Given I am on the Homepage
    When I click the Blog link
    Then I am redirected to the Blog page

  Scenario: Can go from Blog to Homepage
    Given I am on the Blog page
    When I click the Homepage link
    Then I am redirected to the Homepage