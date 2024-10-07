from selenium import webdriver
from tasks.login import Login
from tasks.add_candidate import AddCandidate
from tasks.interview import ScheduleInterview
from questions.check_status import CheckCandidateStatus
from abilities.use_browser import UseBrowser
from actor import Actor
from tasks.navegate_to import NavigateTo
from tasks.navigate_to_recruitment import NavigateToRecruitment
from tasks.save_form import Save

if __name__ == "__main__":
    # Configure the browser
    browser = webdriver.Firefox()

    browser.get('https://opensource-demo.orangehrmlive.com/')
    assert 'OrangeHRM' in browser.title, "Failed to load the login page."

    actor = Actor('Admin').who_can(UseBrowser(browser))

    try:
        # Login as Admin
        actor.attempts_to(Login.as_admin())
        print("Logged in as Admin")

        # Enter the Recruitment module
        actor.attempts_to(NavigateToRecruitment())
        print("Navigated to Recruitment module")

        # Add candidate
        actor.attempts_to(AddCandidate("Ronaldo", "Jose",
                          "Rodríguez", "ronaldojose@gmail.com", "60000000"))
        print("Added candidate: Ronaldo Jose Rodríguez")

        # Change state to "Shortlist"
        actor.attempts_to(NavigateTo("Shortlist"))

        # Save the "Shortlist" status change
        actor.attempts_to(Save())

        # Change state to "Interview" and save
        actor.attempts_to(ScheduleInterview(
            "Insights and Inspiration", "Lindsay Joanne Nicolas Anderson", "2024-10-15"))
        print("Scheduled interview")

        # Change state to "Mark Interview Passed"
        actor.attempts_to(NavigateTo("Mark Interview Passed"))

        # Save the "Mark Interview Passed" status change
        actor.attempts_to(Save())

        # Change state to "Offer Job"
        actor.attempts_to(NavigateTo("Offer Job"))

        # Save the "Offer Job" status change
        actor.attempts_to(Save())

        # Change state to "Hire"
        actor.attempts_to(NavigateTo("Hire"))

        # Save the "Hire" status change
        actor.attempts_to(Save())
        print("Hired candidate")

        # Check candidate status "Hire"
        status = actor.should_see_the(
            CheckCandidateStatus("Ronaldo Jose Rodríguez"))
        print(f"Candidate status: {status}")

    finally:
        # Close the browser
        actor.ability_to_use_browser().quit()
        print("Browser closed")
