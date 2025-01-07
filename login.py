from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://www.reddit.com/")

    login_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@href='https://www.reddit.com/login/']"))
    )
    login_button.click()

    username_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "login-username"))
    )
    password_field = driver.find_element(By.ID, "login-password")

    username_field.send_keys("Big-Strawberry-8750")
    password_field.send_keys("Nrgzd1707")

    password_field.send_keys(Keys.RETURN)
    print("Giriş uğurla tamamlandı!")

finally:
    driver.quit()
