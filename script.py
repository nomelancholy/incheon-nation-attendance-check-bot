import os
import time

from selenium import webdriver
from dotenv import load_dotenv, find_dotenv

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
load_dotenv(find_dotenv())


def chul_check():
    driver.get('https://incheonation.kr/')

    ID = os.environ.get("ID")
    PW = os.environ.get("PW")

    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'bt_login'))
        )
    except:
        driver.quit()

    login_popup_load_btn = driver.find_element(
        by=By.CLASS_NAME, value='bt_login')
    login_popup_load_btn.click()

    id_field = driver.find_element(by=By.NAME, value='user_id')
    id_field.send_keys(ID)
    pw_field = driver.find_element(by=By.NAME, value='password')
    pw_field.send_keys(PW)

    login_btn = driver.find_element(
        by=By.CSS_SELECTOR, value='.bt_area .bt_login')
    login_btn.click()

    # https://incheonation.kr/attendance
chul_check()
