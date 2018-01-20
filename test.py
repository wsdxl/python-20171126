from selenium import webdriver
driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get('https://biz.86links.com')
driver.maximize_window()
driver.find_element_by_id('username').send_keys('13641878150')
driver.find_element_by_id('password').send_keys('a111111')
from time import sleep
sleep(5)
driver.find_element_by_class_name('submit').click()
