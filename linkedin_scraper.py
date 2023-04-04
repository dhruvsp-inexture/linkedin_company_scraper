import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
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
# https://www.linkedin.com/search/results/companies/

login_form_email = driver.find_element(By.ID, "username")
login_form_email.send_keys(os.environ.get("EMAIL"))

login_form_password = driver.find_element(By.ID, "password")
login_form_password.send_keys(os.environ.get("PASSWORD"))

login_submit_button = driver.find_element(By.CLASS_NAME, "from__button--floating").click()

driver.get("https://www.linkedin.com/search/results/companies/")

all_filters_button = WebDriverWait(driver, timeout=10).until(
    lambda d: d.find_element(By.CSS_SELECTOR, "div.relative.mr2 button.artdeco-pill")).click()

all_checkboxes_filter = WebDriverWait(driver, timeout=10).until(
    lambda d: d.find_elements(By.CLASS_NAME, "search-reusables__secondary-filters-values"))

# location filtering
locations_checkboxes = all_checkboxes_filter[0]
all_checkboxes = WebDriverWait(locations_checkboxes, timeout=10).until(
    lambda d: d.find_elements(By.TAG_NAME, "li"))
north_america_location_checkbox = (all_checkboxes[0]).find_element(By.TAG_NAME, "label").click()
custom_location_checkbox = all_checkboxes[-1].find_element(By.TAG_NAME, "button").click()
custom_location = all_checkboxes[-1].find_element(By.TAG_NAME, "input")
custom_location.send_keys("India")
time.sleep(1)
custom_location.send_keys(Keys.ARROW_DOWN)
custom_location.send_keys(Keys.RETURN)

# industry filtering
Industry_checkboxes = all_checkboxes_filter[1]
all_checkboxes = WebDriverWait(Industry_checkboxes, timeout=10).until(
    lambda d: d.find_elements(By.TAG_NAME, "li"))
technology_industry_checkbox = (all_checkboxes[0]).find_element(By.TAG_NAME, "label").click()
custom_industry_checkbox = all_checkboxes[-1].find_element(By.TAG_NAME, "button").click()
custom_industry = all_checkboxes[-1].find_element(By.TAG_NAME, "input")
custom_industry.send_keys("Software Development")
time.sleep(1)
custom_industry.send_keys(Keys.ARROW_DOWN)
custom_industry.send_keys(Keys.RETURN)

company_size = all_checkboxes_filter[2]
all_checkboxes = WebDriverWait(company_size, timeout=10).until(
    lambda d: d.find_elements(By.TAG_NAME, "li"))
size_51_to_200_checkbox = (all_checkboxes[2]).find_element(By.TAG_NAME, "label").click()
size_201_to_500_checkbox = (all_checkboxes[3]).find_element(By.TAG_NAME, "label").click()

show_results_button = driver.find_element(By.CLASS_NAME,
                                          "search-reusables__secondary-filters-show-results-button").click()


company_list = []
next_page_button = WebDriverWait(driver, timeout=10).until(lambda d:d.find_element(By.CLASS_NAME, "artdeco-pagination__button--next"))
while next_page_button.is_enabled():
    companies = WebDriverWait(driver, timeout=10).until(
        lambda d: d.find_elements(By.CLASS_NAME, "entity-result__title-text"))
    for company in companies:
        company_link = company.find_element(By.CLASS_NAME, "app-aware-link ").get_attribute('href')
        company_list.append(f'{company_link}about/')
    next_page_button.click()
    next_page_button = WebDriverWait(driver, timeout=10).until(lambda d:d.find_element(By.CLASS_NAME, "artdeco-pagination__button--next"))

print(company_list)

time.sleep(5)
