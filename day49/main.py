from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_driver_path = "chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/home")

user_label = driver.find_element(By.NAME,'session_key')
user_label.send_keys('thiagowfn@gmail.com')

password_label = driver.find_element(By.NAME,'session_password')
password_label.send_keys('soueu321')

signin_button = driver.find_element(By.CLASS_NAME, 'sign-in-form__submit-button')
signin_button.click()

