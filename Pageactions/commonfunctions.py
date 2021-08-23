from selenium import webdriver
from selenium.webdriver.common.by import By
import time



class Create_New_Account:
    """

    """

    def __init__(self):
        self.browser = webdriver.Chrome("/home/vinay/selenium/chromedriver")

    def open_url(self, url):
        """

        :param url:
        :return:
        """
        self.browser.get(url)

    def maximize(self):
        """

        :return:
        """
        self.browser.maximize_window()

    def getpage_title(self):
        """

        :return:
        """
        return self.browser.title

    def click_on_inputs_send_keys(self, x_path, value):
        """

        :param x_path:
        :param value:
        :return:
        """
        self.browser.find_element_by_xpath(x_path).send_keys(value)

    def click_on_elements(self, x_path):
        """

        :param x_path:
        :return:
        """
        time.sleep(2)
        self.browser.find_element(By.XPATH, x_path).click()

    def select_on_element(self, x_path):
        """

        :param x_path:
        :return:
        """
        self.browser.find_element(By.XPATH, x_path)

