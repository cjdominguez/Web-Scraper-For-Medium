
import Scrape.constants as const    # imports constants.py file
import os
from selenium import webdriver      # imports webdriver module from library for automating the opening of the webbrowser


class Login(webdriver.Chrome):
    """"
    This class will deal with logging us into
    """
    def __init__(self, driver_path=r"\Desktop\selenium_drivers"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        super(Login, self).__init__()

    def launch_Page(self):
        self.get(const.BASE_URL)