"""
    this file create for flowing class and functions
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Create_New_Account:
    """
    in this class we are defining the different def functions for browser
    """

    def __init__(self):
        """
            this function will do
                inti the browser
        """
        self.browser = webdriver.Chrome("/home/vinay/selenium/chromedriver")

    def open_url(self, url):
        """
            this function will do
                open the given url
        root to ulr at browser
        :param url:
        :return:
        """
        self.browser.get(url)

    def maximize(self):
        """
        by using the maximize it well help to maximize the browser window
        :return:maximize_window
        """
        self.browser.maximize_window()

    def getpage_title(self):
        """
        by using this function we will get the page title
        :return:browser_title
        """
        return self.browser.title

    def click_on_inputs_send_keys(self, x_path, value):
        """
        by using the function we can get the part of required element
        :param x_path:need x_pathbrowser will find the x_path
        :param value:need to send the value
        :return:browser will find the x_path and sent key value
        """
        self.browser.find_element_by_xpath(x_path).send_keys(value)

    def click_on_elements(self, x_path):
        """
        by using the function we can get the part of required element
        :param x_path: need x_path
        :return:browser will find the x_path
        """
        time.sleep(2)
        self.browser.find_element(By.XPATH, x_path).click()

    def select_on_element(self, x_path):
        """
        by using the function we can get the part of required element
        :param x_path:x_path: need x_path
        :return:browser will find the x_path
        """
        self.browser.find_element(By.XPATH, x_path)
