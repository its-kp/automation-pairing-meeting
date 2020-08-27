# Import webdriver
from selenium import webdriver
browser = webdriver.Chrome()

# Navigate to translate.google.com
browser.get('https://translate.google.com/')

# Grab list of languages from source dropdown
dropdown_source_button = '/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[3]'
browser.find_element_by_xpath(dropdown_source_button).click()
find_language = '//div[@class="language_list_item language_list_item_language_name"]'
source_language = browser.find_elements_by_xpath(find_language)
source_language_list = list()
for each in source_language:
    source_language_list.append(each.text)

# Grab list of languages from target dropdown
dropdown_target_button = '/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[4]/div[3]'
browser.find_elements_by_xpath(dropdown_target_button)
translate_language = '//div[@class="language_list_item language_list_item_language_name"]'
translate_target = browser.find_elements_by_xpath(translate_language)
translate_target_list = list()
for each in translate_target:
    translate_target_list.append(each.text)

# Verify that all languages in both lists are present.
if source_language_list == translate_target_list:
    print("These are the same.")
    print(translate_target_list)
    print(source_language_list)