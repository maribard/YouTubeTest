from selenium.webdriver.common.by import By
from PageObject.Locators import Locator


class ListOfVideo(object):
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def select_first_video(self):
        """
        Method selects the first video from resulting list

        :return: None
        """
        list_videos = self.driver.find_elements(By.XPATH, Locator.ytd_list_video)
        print(list_videos)
        list_videos[1].click()
