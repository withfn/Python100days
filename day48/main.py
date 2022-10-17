import time
import datetime 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_driver_path = "chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID,'cookie')

buys = driver.find_elements(By.CSS_SELECTOR, '.grayed > b')
testeb = buys[0].text.split("- ")

for x in buys[0: -1]:
    x = x.text.split("- ")
    x = x[1]
    print(x)

# time_execution = 30   # [seconds]
# initial_time = time.time()
# timeout = initial_time + time_execution
# step = 5 + initial_time

# while True:
#     cookie.click()
#     if time.time() > timeout:
#         break
#     if time.time() > step:
#         step += 5
#         print(step)
#         # break
    

# print(timeout)