Feature: The pages should have correct content

  Scenario: Blog page has correct title
    Given I am on the Blog page
    Then The title is visible
    And The title is "This is the blog page"

  Scenario: Homepage has correct title
    Given I am on the Homepage
    Then The title is visible
    And The title is "This is the homepage"

  Scenario: Blog page loads the posts
    Given I am on the Blog page
    And I wait for posts to load
    Then The posts section is present on the page

  Scenario: User can create a new post
    Given I am on the new post page
    When I input "Test title" in the "title" field
    And I input "Test content" in the "content" field
    And I submit the data
    Then I am redirected to the Blog page
    Given I wait for posts to load
    Then The post with "Test title" is visible on the Blog page
