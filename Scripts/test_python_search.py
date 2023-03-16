from time import sleep
from TestBase.WebDriverSetup import WebDriverSetup
from PageObject.Pages.HomePage import Home


class PythonSearch(WebDriverSetup):
    def test_python_search(self):
        driver = self.driver
        wait = self.wait

        home = Home(driver, wait)
        sleep(1)
        home.paste_searched_text()
        home.submit()
        home.check_if_result_of_search_is_present()
