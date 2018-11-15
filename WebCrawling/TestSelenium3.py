from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException

def waitForLoad(driver):
    elem = driver.find_element_by_tag_name("html")
    count = 0
    while True:
        count += 1
        if count > 10:
            print("Time Out after 5 seconds")
            return
        time.sleep(.5)
        try:
            elem = driver.find_element_by_tag_name("div")
        except NoSuchElementException:
            return

driver = webdriver.PhantomJS(executable_path='C:/phantomjs-2.1.1/bin/phantomjs.exe')
driver.get("http://127.0.0.1:81/AJAX/redirectDemo1.html")
waitForLoad(driver)
print(driver.page_source)
