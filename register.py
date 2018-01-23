from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get('https://auth.86links.com/register')
driver.maximize_window()
driver.find_element_by_css_selector('form:nth-child(3) > div.content > div:nth-child(1) > div.content > div > input').send_keys('test110')
n1=driver.find_element_by_css_selector('div.slider')
ActionChains(driver).move_to_element(n1).click_and_hold().move_by_offset(400,0).perform()
driver.find_element_by_css_selector('form:nth-child(3) > div.buttons > button > span').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="register-view"]/form[2]/div[2]/div[1]/div[1]/div/input').send_keys('009')
driver.find_element_by_xpath('//*[@id="register-view"]/form[2]/div[2]/div[2]/div[1]/div/input').send_keys('test')
driver.find_element_by_xpath('//*[@id="register-view"]/form[2]/div[2]/div[4]/div[1]/div/input').send_keys('a111111')
driver.find_element_by_css_selector('form:nth-child(4) > div.buttons > div > button:nth-child(3) > span').click()