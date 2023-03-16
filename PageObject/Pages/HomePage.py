from selenium.webdriver.common.by import By
from PageObject.Locators import Locator
from selenium.webdriver.support import expected_conditions as EC


class Home(object):
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        try:
            self.driver.find_element(By.XPATH, Locator.accept_cookie).click()
        except:
            print("hehe")

    def paste_searched_text(self, text='Python'):
        """
        Method paste given text into search box

        :param text: Text which should be send to search box on YouTube page
        :return: None
        """
        self.wait.until(EC.visibility_of_element_located((By.XPATH, Locator.search_box)))
        elements_with_search = self.driver.find_elements(By.ID, Locator.search_input)
        for elem in elements_with_search:
            if elem.tag_name == 'input':
                elem.send_keys(text)

    def submit(self):
        """
        Method clicks on search icon

        :return: None
        """
        self.wait.until(EC.visibility_of_element_located((By.XPATH, Locator.search_icon)))
        self.driver.find_element(By.XPATH, Locator.search_icon).click()


    def check_if_result_of_search_is_present(self):
        """
        Method checks if result of searched text is present

        :return: None
        """
        self.wait.until(EC.visibility_of_element_located((By.XPATH, Locator.result_of_search)))
