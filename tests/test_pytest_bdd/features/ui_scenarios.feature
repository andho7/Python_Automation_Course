# Created by ango at 23.10.2022
Feature: Basic CRUD operations using UI

  Scenario: Create user
    When I create a new user
    Then I ensure that username can be found in user's list
    Then I delete newly created user

  Scenario: Get user data
    When I create a new user
    Then I ensure that user data is equal to data for created user
    Then I delete newly created user

  Scenario: Edit user data
    When I create a new user
    Then I ensure that username can be found in user's list
    When I update username
    Then I ensure that username can be found in user's list
    Then I delete newly created user

  Scenario: Delete user
    When I create a new user
    Then I ensure that username can be found in user's list
    When I delete newly created user
    Then I ensure that username can NOT be found in user's list