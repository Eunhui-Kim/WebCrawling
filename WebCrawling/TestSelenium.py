
from selenium import webdriver
import time

driver = webdriver.PhantomJS(executable_path='C:/phantomjs-2.1.1/bin/phantomjs.exe')
driver.get("http://127.0.0.1:81/AJAX/demo_ajax.html")
time.sleep(3)
print(driver.find_element_by_id("content").text)
print(driver.find_element_by_tag_name("div").text)
print(driver.find_element_by_css_selector("#content").text)

print(driver.find_element_by_tag_name("a").text)
print(driver.find_element_by_tag_name("p").text)
driver.close()