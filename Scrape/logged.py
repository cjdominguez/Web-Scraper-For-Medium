import Scrape.constants as const  # imports constants.py file
import os
from selenium import webdriver  # imports webdriver module from library for automating the opening of the webbrowser
#import urllib3


class Login(webdriver.Chrome):
    """"
    This class will deal with logging us into medium

    """

    def __init__(self, driver_path=r"\Desktop\selenium_drivers"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Login, self).__init__()

    def launch_Page(self):
        self.get(const.BASE_URL)
        self.find_element_by_xpath(const.XPATH_LOGIN).click()
        self.find_element_by_css_selector(const.CSS_POPUP).click()

    def logins(self):
        self.find_element_by_css_selector(const.XPATH_Email).send_keys(const.USERNAME)
        self.find_element_by_css_selector(const.CSS_Next).click()
        #fill in username stored in constants
        #THEN HIT NEXT
        #fill in password stored in constants
        #then somehting

        #ran into issue with logging into google through selenium on google drive


class Scraper:

    def find_reading_list(self):
        pass
