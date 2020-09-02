# import required

from selenium import webdriver
import time


class BrowserExample:

    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.get('https://translate.google.com/')


class LanguageContent:

    def __init__(self):
        self.browser = BrowserExample().browser
        self.target_language_list = list()
        self.translated_hello_world = dict()

    def insert_source_text(self):
        text_box = 'source'
        self.browser.find_element_by_id(text_box).send_keys("Hello World")

    def click_target_dropdown(self):
        dropdown_target_button = '/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[4]/div[3]'
        self.browser.find_element_by_xpath(dropdown_target_button).click()

    def grab_target_languages(self):
        locator = '//div[@class="language-list"][2]//div[@class="language_list_item language_list_item_language_name"]'
        target_element_list = self.browser.find_elements_by_xpath(locator)

        for each in target_element_list:

            if each.text:
                self.target_language_list.append(each.text)

    def select_single_language(self):

        for each_language in self.target_language_list:
            self.click_target_dropdown()
            target_language = f"//div[@class='language-list-unfiltered-langs-tl_list']//div[text()='{each_language}']"
            self.browser.find_element_by_xpath(target_language).click()
            time.sleep(0.5)

            if each_language == "English":
                new_text = "//span[@class='tlid-translation translation']"
            else:
                new_text = "//span[@class='tlid-translation translation']/span"

            text_language = self.browser.find_element_by_xpath(new_text).text

            self.translated_hello_world[each_language] = text_language

    def print_statement(self):
        print(self.translated_hello_world)

    def end_process(self):
        self.browser.quit()


class TestPytestClass:

    def test_every_language(self):
        self.selection = LanguageContent()
        self.selection.insert_source_text()
        self.selection.click_target_dropdown()
        self.selection.grab_target_languages()
        self.selection.select_single_language()
        self.selection.print_statement()
        self.selection.end_process()