from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from PageObject.Locators import Locator
from selenium.webdriver.support import expected_conditions as EC



class Video(object):
    """
    Class Video represent a page of one particular video on YouTube
    """
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, Locator.skip_add)))
            self.driver.find_element(By.XPATH, Locator.skip_add).click()
        except:
            print("Button SKIP_ADD was not shown")

        try:
            EC.presence_of_element_located((By.XPATH, Locator.spec_button))
            self.driver.find_element(By.XPATH, Locator.spec_button).click()
        except:
            print("Button NO_THANKS was not shown")

    def move_slide_bar(self):
        """
        Method drag the video slidebar to approximately the middle of the video

        :return: None
        """
        elem = self.driver.find_element(By.XPATH, Locator.slide_bar)
        width = elem.size

        act = ActionChains(self.driver)
        act.move_to_element(elem).move_by_offset((width['width'] // 10), 0).click().perform()

    def mute_video(self):
        """
        Method mute the video, before mute action video is paused, after mute action video is played

        :return: None
        """
        self.driver.find_element(By.XPATH, Locator.video_box).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, Locator.mute_video)))
        self.driver.find_element(By.XPATH, Locator.mute_video).click()
        self.driver.find_element(By.XPATH, Locator.video_box).click()


    def get_video_info(self):
        """
        Method get info from video (title of the video, duration of the video, name of the channel,
        amount of views, date of upload, amount of likes) and write it to standard out
        #TODO Read info about amount of dislikes, now it is hidden info

        :return: None
        """
        elem = self.driver.find_element(By.XPATH, Locator.title_video)
        print(f"Title of the video: {elem.text}")

        elem = self.driver.find_element(By.XPATH, Locator.duratiorn_video)
        print(f"Duration of the video: {elem.text}")

        elem = self.driver.find_elements(By.XPATH, Locator.channel_name)
        for e in elem:
            if e.text != "":
                print(f"Name of the channel: {e.text}")
                break

        self.driver.find_element(By.XPATH, Locator.expand_container).click()
        elem = self.driver.find_element(By.XPATH, Locator.amount_of_views)
        print(f"Amount of views: {elem.text}")

        elem = self.driver.find_element(By.XPATH, Locator.date_of_upload)
        print(f"Date of upload: {elem.text}")

        elem = self.driver.find_element(By.XPATH, Locator.amount_of_likes)
        print(f"Amount of likes: {elem.text}")

    def switch_to_the_next_video(self):
        """
        Method switch to the next video from panel on the right

        :return: None
        """
        self.driver.find_element(By.XPATH, Locator.next_video_button).click()
        sleep(3)

    def pause_video_after_given_sec(self, seconds=10):
        """
        Method waits until video reaches a given number of seconds and pause it afterwards

        :param seconds: int, optional
        :return:
        """
        act = ActionChains(self.driver)
        elem_video = self.driver.find_element(By.XPATH, Locator.video_box)
        elem_login = self.driver.find_element(By.XPATH, Locator.login_button)

        while True:
            sleep(1)
            act.move_to_element(elem_video).perform()
            elem = self.driver.find_element(By.XPATH, Locator.current_time)
            print(elem.text)
            if len(elem.text) > 3 and int(elem.text[-2:]) >= seconds:
                break
            act.move_to_element(elem_login).perform()

        self.driver.find_element(By.XPATH, Locator.video_box).click()
        sleep(3)


