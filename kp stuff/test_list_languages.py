# Import webdriver
from selenium import webdriver
import time

browser = webdriver.Chrome()

# Navigate to translate.google.com
browser.get('https://translate.google.com/')

# Grab list of languages from source dropdown
dropdown_source_button = '/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]'
browser.find_element_by_xpath(dropdown_source_button).click()
time.sleep(1)
source_locator = '//div[@class="language-list"][1]//div[@class="language_list_item language_list_item_language_name"]'
source_element_list = browser.find_elements_by_xpath(source_locator)
source_language_list = list()
for each in source_element_list:
    source_language_list.append(each.text)

# Grab list of languages from target dropdown
dropdown_target_button = '/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[4]/div[3]'
browser.find_element_by_xpath(dropdown_target_button).click()
browser.find_element_by_xpath(dropdown_target_button).click()
browser.find_elements_by_xpath(dropdown_target_button)
time.sleep(1)
target_locator = '//div[@class="language-list"][2]//div[@class="language_list_item language_list_item_language_name"]'
target_element_list = browser.find_elements_by_xpath(target_locator)
target_language_list = list()
for each in target_element_list:
    target_language_list.append(each.text)

# Verify that all languages in both lists are present.
if source_language_list == target_language_list:
    print("These are the same.")
else:
    print("NOT THE SAME.")

print("This is the source list:", source_language_list)
print("This is that target list:", target_language_list)

browser.quit()
