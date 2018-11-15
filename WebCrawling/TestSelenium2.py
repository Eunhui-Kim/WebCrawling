from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.PhantomJS(executable_path='C:/phantomjs-2.1.1/bin/phantomjs.exe')
driver.get("http://127.0.0.1:81/AJAX/demo_post.html")
try:
    element = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "XButton")))
finally:
    print(driver.find_element_by_tag_name("div").text)
    driver.close()
