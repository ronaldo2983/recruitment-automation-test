class UseBrowser:
    def __init__(self, browser):
        self.browser = browser

    def perform_as(self, actor):
        pass

    @staticmethod
    def ability(browser):
        return UseBrowser(browser)

    def quit(self):
        self.browser.quit()
