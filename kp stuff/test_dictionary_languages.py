# import required

from selenium import webdriver
import time

def find_browser():

    # Create the browser
    browser = webdriver.Chrome()

    # Navigate to Google Translate
    browser.get('https://translate.google.com/')
    return browser

browser = find_browser()

# Locate xpath of text box where we can insert text.
text_box = 'source'
browser.find_element_by_id(text_box).send_keys("Hello World")

# Click the Target dropdown to view a list of languages
dropdown_target_button = '/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[4]/div[3]'
browser.find_element_by_xpath(dropdown_target_button).click()

# Determine all possible languages (find common xpath)
target_locator = '//div[@class="language-list"][2]//div[@class="language_list_item language_list_item_language_name"]'
target_element_list = browser.find_elements_by_xpath(target_locator)
target_language_list = list()

for each in target_element_list:

    if each.text:
        target_language_list.append(each.text)

browser.find_element_by_xpath(dropdown_target_button).click()

translated_hello_world = dict()

for each_language in target_language_list:

    browser.find_element_by_xpath(dropdown_target_button).click()

    # Select a language
    translate_language = each_language
    target_language = f"//div[@class='language-list-unfiltered-langs-tl_list']//div[text()='{translate_language}']"
    browser.find_element_by_xpath(target_language).click()
    time.sleep(0.5)

    # Grab the text which will be translated
    if "English":
        new_text = "//span[@class='tlid-translation translation']"
    else:
        new_text = "//span[@class='tlid-translation translation']/span"

    text_language = browser.find_element_by_xpath(new_text).text

    # Store all the results as a dictionary.
    translated_hello_world[translate_language] = text_language

# Debug print.
print(translated_hello_world)

# quit browser
browser.quit()
