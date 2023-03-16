import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        self.wait = WebDriverWait(self.driver, 50)
        self.driver.get("https://www.youtube.com/")
        self.driver.set_page_load_timeout(10)

    def tearDown(self):
        if self.driver is not None:
            print("Cleanup of test environment")
            self.driver.close()
            self.driver.quit()
