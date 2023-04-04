import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-browser-side-navigation")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-features=VizDisplayCompositor")
options.add_argument("--enable-javascript")



load_dotenv()

PATH = "/home/root352/Downloads/chromedriver"
driver = webdriver.Chrome(executable_path=PATH, options=options)

stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True)

driver.get("https://www.linkedin.com/login/")
driver.maximize_window()
# https://www.linkedin.com/search/results/companies/

login_form_email = driver.find_element(By.ID, "username")
login_form_email.send_keys(os.environ.get("EMAIL1"))

login_form_password = driver.find_element(By.ID, "password")
login_form_password.send_keys(os.environ.get("PASSWORD1"))

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
