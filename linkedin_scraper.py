from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os

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
