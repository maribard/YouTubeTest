from time import sleep

from PageObject.Pages.HomePage import Home
from PageObject.Pages.ListOfVideoPage import ListOfVideo
from TestBase.WebDriverSetup import WebDriverSetup


class ListVideo(WebDriverSetup):
    def test_select_first_video(self):
        driver = self.driver
        wait = self.wait

        home = Home(driver, wait)
        sleep(1)
        home.search_text()
        home.submit()
        home.check_if_result_of_search_is_present()

        list_video = ListOfVideo(driver, wait)
        list_video.select_first_video()
        sleep(5)
