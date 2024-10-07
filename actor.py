class Actor:
    def __init__(self, name):
        self.name = name
        self.abilities = {}

    def who_can(self, ability):
        self.abilities[ability.__class__.__name__] = ability
        return self

    def attempts_to(self, task):
        task.perform_as(self)

    def should_see_the(self, question):
        return question.answered_by(self)

    def ability_to_use_browser(self):
        return self.abilities['UseBrowser']
