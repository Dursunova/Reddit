from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.implicitly_wait(5)
driver.get("https://www.reddit.com/")

login_button = driver.find_element(By.ID, "login-button")
login_button.click()
username_input = driver.find_element(By.NAME, "username")
password_input = driver.find_element(By.NAME, "password")
username_input.send_keys("Big-Strawberry-8750")
password_input.send_keys("Nrgzd1707")
login_button2 = driver.find_element(By.XPATH, '//*[@id="login"]/auth-flow-modal/div[2]/faceplate-tracker/button')
login_button2.click()

time.sleep(10)


hot_button = driver.find_element(By.XPATH, '//*[@id="main-content"]')
hot_button.click()

time.sleep(5)


driver.quit()