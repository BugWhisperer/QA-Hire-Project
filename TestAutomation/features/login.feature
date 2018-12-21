Feature: Login
  In order to use the app the user must be able to Login with valid credentials

  Scenario: Valid login
    Given Hudl Coach navigate to the login page
    When the Coach login with valid username and password
    Then the Coach is presented with the Home page

  Scenario: Invalid login
    Given Hudl Coach navigate to the login page
    When the Coach login with invalid username and password
    Then the Coach is presented with an error message