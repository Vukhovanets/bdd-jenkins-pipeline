Feature: User Login on Swag Labs
  As a registered user
  I want to log in to the application
  So that I can see the inventory

  Scenario: Successful login with standard user
    Given I open the Swag Labs login page
    When I enter username "standard_user" and password "secret_sauce"
    Then I should be redirected to the inventory page

  Scenario: Failed login with locked out user
    Given I open the Swag Labs login page
    When I enter username "locked_out_user" and password "secret_sauce"
    Then I should see an error message "Sorry, this user has been locked out."
