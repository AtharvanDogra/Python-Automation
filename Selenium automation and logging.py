from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import requests
import time
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')          #for log file
file_handler = logging.FileHandler('/home/atharvan/Documents/ATGtask2Log.log')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()        #for console
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)



driver = webdriver.Firefox(executable_path="/home/atharvan/Downloads/geckodriver")

driver.maximize_window()

driver.get('https://www.atg.party/')

print("Http Response Code = ", (requests.get("https://www.atg.party/")).status_code)

#logging

navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

backendPerformance = responseStart - navigationStart
frontendPerformance = domComplete - responseStart

logger.info('RESPONSE TIME => Backend Performance: {}, Frontend Performance: {}'.format(backendPerformance, frontendPerformance))         #LOG



driver.find_element_by_link_text("Login").click()

driver.find_element_by_id("email").send_keys("wiz_saurabh@rediffmail.com")
driver.find_element_by_id("password").send_keys("Pass@123")

driver.find_element_by_xpath("/html/body/header/div[1]/div[2]/div/div/div/div/div/div/div/div/div[2]/div/form/div[3]/button").click()

time.sleep(15)

driver.get("https://www.atg.party/article")

time.sleep(3)

driver.find_element_by_name("title").send_keys("Selenium")
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/form/div/div/div[2]/div/div/div/div[1]/div/div/div").send_keys("My first selenium automation code")

#driver.switch_to.frame(0)
driver.find_element_by_xpath("//*[@id='cover_image']").send_keys("/home/atharvan/Pictures/selenium_exp_wait.png")
time.sleep(10)

driver.find_element_by_xpath("//*[@id='hpost_btn']").click()            #post

driver.switch_to.window(driver.window_handles[-1])
time.sleep(10)
logger.info('URL of the child page after upload: {}'.format(driver.current_url))
