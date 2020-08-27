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
find_language = '//div[@class="language_list_item language_list_item_language_name"]'
languages = browser.find_elements_by_xpath(find_language)
# print(languages)
# Verify Polish appears in the dropdown
for language_search in languages:
    if 'Polish' == language_search.text:
       print('POLISH!!')