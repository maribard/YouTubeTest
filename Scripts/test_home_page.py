from TestBase.WebDriverSetup import WebDriverSetup


class YouTubeHomePage(WebDriverSetup):

    def test_home_page(self):
        driver = self.driver
        driver.get("https://www.youtube.com/")
        driver.set_page_load_timeout(30)

        web_page_title = "YouTube"
        self.assertEqual(driver.title, web_page_title)
