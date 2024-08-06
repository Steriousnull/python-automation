from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options
username = "858479649"
password = "usac427t"
options = Options()
options.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open a webpage
driver.get("https://india.1xbet.com/live/cricket")
driver.maximize_window()

block_button = driver.find_element(By.CLASS_NAME, "pf-subs-btn-link")
block_button.click()

# Find the element by ID
element = driver.find_element(By.ID, "curLoginForm")

# Click the element
element.click()
driver.find_element(By.ID, 'auth_id_email').send_keys(username)
driver.find_element(By.ID, 'auth-form-password').send_keys(password)
driver.find_element(By.CLASS_NAME, 'auth-button__text').click()
