from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver.common.by import By
import time

def main():
    user = "youremail"
    pwd = "password"
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://accounts.google.com/ServiceLogin/identifier?continue=https%3A%2F%2Fmyactivity.google.com%2Fmyactivity&hl=en&flowName=GlifWebSignIn&flowEntry=AddSession")
    driver.implicitly_wait(5)
    username = driver.find_element_by_id("identifierId");
    username.send_keys(user)
    driver.implicitly_wait(5)
    spans = driver.find_elements(By.XPATH, "//span")
    next = spans[3]
    next.click()

    password = driver.find_element_by_name('password')
    password.send_keys(pwd)
    driver.implicitly_wait(5)
    spans = driver.find_elements(By.XPATH, "//span")
    hidden = spans[4]
    hidden.click()
    next = spans[6]
    next.click()

if __name__=='__main__':
    main()



