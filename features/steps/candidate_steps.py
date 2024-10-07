from behave import given, when, then
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


@given('the browser is open and navigated to the login page')
def step_given_browser_is_open(context):
    context.browser = webdriver.Firefox()
    context.browser.get('https://opensource-demo.orangehrmlive.com/')
    assert 'OrangeHRM' in context.browser.title, "Failed to load the login page"
    context.actor = Actor('Admin').who_can(UseBrowser(context.browser))


@when('the Admin logs in')
def step_when_admin_logs_in(context):
    context.actor.attempts_to(Login.as_admin())
    print("Logged in as Admin")


@when('the Admin navigates to the Recruitment module')
def step_when_admin_navigates_to_recruitment(context):
    context.actor.attempts_to(NavigateToRecruitment())
    print("Navigated to Recruitment module")


@when('the Admin adds a new candidate "{first_name} {last_name}" with email "{email}" and contact "{contact}"')
def step_when_add_candidate(context, first_name, last_name, email, contact):
    context.actor.attempts_to(AddCandidate(
        first_name, "Jose", last_name, email, contact))
    print(f"Added candidate: {first_name} {last_name}")


@when('the Admin changes the candidate\'s state to "{state}"')
def step_when_change_candidate_state(context, state):
    context.actor.attempts_to(NavigateTo(state))
    print(f"Changed candidate's state to {state}")


@when('the Admin saves the form')
def step_when_save_form(context):
    context.actor.attempts_to(Save())
    print("Form saved")


@when('the Admin schedules an interview for the candidate with "{interviewer}" on "{date}"')
def step_when_schedule_interview(context, interviewer, date):
    context.actor.attempts_to(ScheduleInterview(
        "Insights and Inspiration", interviewer, date))
    print(f"Scheduled interview with {interviewer} on {date}")


@then('the Admin should see the candidate\'s status as "Hired"')
def step_then_check_candidate_status(context):
    status = context.actor.should_see_the(
        CheckCandidateStatus("Ronaldo Jose Rodríguez"))
    assert status == "Hired", f"Expected status to be 'Hired' but got '{
        status}'"
    print(f"Candidate status: {status}")
