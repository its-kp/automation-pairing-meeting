# Setup Webdrive
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
# Navigate to the Webpage
browser.get("https://translate.google.com/")
# Click the dropdown button
dropdown_button = "/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]"
browser.find_element_by_xpath(dropdown_button).click()
# Grab all languages from the dropdown

# Verify Polish appears in the dropdown