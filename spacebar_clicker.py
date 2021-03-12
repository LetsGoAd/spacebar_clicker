from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


def webpage1():
    driver.get("https://codepen.io/murilopolese/full/xVaoQr")


driver = webdriver.Firefox()
driver.set_window_size(1920, 1080)


webpage1()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body')))
el = driver.find_element_by_xpath('/html/body')
el.click()
i = 0
while i <= 6684:
    el.send_keys(Keys.SPACE)
    i += 1
    time.sleep(0.01)
