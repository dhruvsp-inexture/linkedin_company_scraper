import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

from selenium.webdriver.support.wait import WebDriverWait

load_dotenv()

PATH = "/home/root352/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://www.linkedin.com/login/")
driver.maximize_window()
# https://www.linkedin.com/search/results/companies/

login_form_email = driver.find_element(By.ID, "username")
login_form_email.send_keys(os.environ.get("EMAIL"))

login_form_password = driver.find_element(By.ID, "password")
login_form_password.send_keys(os.environ.get("PASSWORD"))

login_submit_button = driver.find_element(By.CLASS_NAME, "from__button--floating").click()

driver.get("https://www.linkedin.com/search/results/companies/")

all_filters_button = WebDriverWait(driver, timeout=10).until(
    lambda d: d.find_element(By.CSS_SELECTOR, "div.relative.mr2 button.artdeco-pill")).click()

locations_checkboxes = WebDriverWait(driver, timeout=10).until(
    lambda d: d.find_element(By.CLASS_NAME, "search-reusables__secondary-filters-values"))
all_checkboxes = WebDriverWait(locations_checkboxes, timeout=10).until(
    lambda d: d.find_elements(By.TAG_NAME, "li"))
north_america_location_checkbox = (all_checkboxes[0]).find_element(By.TAG_NAME, "label").click()
custom_location_checkbox = all_checkboxes[-1].find_element(By.TAG_NAME, "button").click()
custom_location = all_checkboxes[-1].find_element(By.TAG_NAME, "input")
custom_location.send_keys("India")
time.sleep(5)