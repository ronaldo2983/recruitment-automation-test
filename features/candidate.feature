Feature: Manage candidate recruitment process

  Scenario: Admin logs in, adds a candidate, schedules an interview, and hires the candidate
    Given the browser is open and navigated to the login page
    When the Admin logs in
    And the Admin navigates to the Recruitment module
    And the Admin adds a new candidate "Ronaldo Jose Rodríguez" with email "ronaldojose@gmail.com" and contact "60000000"
    And the Admin changes the candidate's state to "Shortlist"
    And the Admin saves the form
    And the Admin schedules an interview for the candidate with "Lindsay Joanne Nicolas Anderson" on "2024-10-15"
    And the Admin changes the candidate's state to "Mark Interview Passed"
    And the Admin saves the form
    And the Admin changes the candidate's state to "Offer Job"
    And the Admin saves the form
    And the Admin changes the candidate's state to "Hire"
    And the Admin saves the form
    Then the Admin should see the candidate's status as "Hired"
