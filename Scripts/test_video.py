from time import sleep
from PageObject.Pages.HomePage import Home
from PageObject.Pages.ListOfVideoPage import ListOfVideo
from PageObject.Pages.VideoPage import Video
from TestBase.WebDriverSetup import WebDriverSetup


class SelectedVideo(WebDriverSetup):
    def test_selected_video(self):
        driver = self.driver
        wait = self.wait

        home = Home(driver, wait)
        sleep(1)
        home.paste_searched_text()
        home.submit()
        home.check_if_result_of_search_is_present()

        list_video = ListOfVideo(driver, wait)
        list_video.select_first_video()

        video = Video(driver, wait)
        sleep(1)
        video.move_slide_bar()
        video.mute_video()
        video.get_video_info()
        video.switch_to_the_next_video()
        video.pause_video_after_given_sec()

