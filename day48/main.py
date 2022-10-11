import time
import datetime 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_driver_path = "chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID,'cookie')

time_execution = 30   # [seconds]
initial_time = time.time()
timeout = initial_time + time_execution
step = 5 + initial_time

while True:
    cookie.click()
    if time.time() > timeout:
        break
    if time.time() > step:
        step += 5
        print(step)
        # break
    

print(timeout)