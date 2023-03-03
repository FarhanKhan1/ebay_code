from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
def get_driver():
    driver = webdriver.Chrome()
    time.sleep(3)
    driver.get("https://www.ebay.com/")
    # time.sleep(5)
    return driver