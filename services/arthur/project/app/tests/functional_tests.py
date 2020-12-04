import os
import time
import unittest
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys


class CamelotTestCase(unittest.TestCase):

    URL = 'http://35.224.48.117'

    USERNAME = ''
    PASSWORD = ''

    PERSONAL_MODEL_CREATION_TIME = 60 * 3 + 10
    PLAYLIST_CREATION_WAIT_TIME = 60 * 2

    driver = Chrome(executable_path='/opt/WebDriver/bin/chromedriver')

    def test_app(self):

        self.driver.get(self.URL)

        self.login(self.USERNAME, self.PASSWORD)

        create_playlist_button, discover_button = self.get_submit_buttons()

        self.type_on_search_bar('piano')

        #time.sleep(self.PLAYLIST_CREATION_WAIT_TIME)

        create_playlist_button.click()

        #time.sleep(self.PLAYLIST_CREATION_WAIT_TIME)

        self.driver.get(self.URL + '/playlist')

        table = self.driver.find_elements_by_tag_name('tr')
        self.assertGreaterEqual(len(table), 1)

        self.driver.quit()

    def login(self, username, password):

        self.find_button_by_class_name('nav-link', 'Login').click()

        self.find_button_by_class_name('btn-primary', 'Login with Spotify').click()

        username_field = self.driver.find_element_by_name('username')
        password_field = self.driver.find_element_by_name('password')

        username_field.send_keys(username)
        password_field.send_keys(password)

        self.find_button_by_id('login-button', 'LOG IN').click()

        time.sleep(2)

        self.find_button_by_id('auth-accept', 'AGREE').click()

        time.sleep(2)

        nav_item = self.driver.find_elements_by_class_name('nav-item')
        self.assertEqual(len(nav_item), 3)
        self.assertEqual(nav_item[0].text, username)

    def find_button_by_class_name(self, class_name, text):
        button = self.driver.find_element_by_class_name(class_name)
        self.assertEqual(button.text, text)
        return button

    def find_button_by_id(self, id, text):
        button = self.driver.find_element_by_id(id)
        self.assertEqual(button.text, text)
        return button

    def get_submit_buttons(self):

        search_buttons = self.driver.find_elements_by_tag_name('button')

        self.assertEqual(len(search_buttons), 2)

        self.assertEqual(search_buttons[0].text, 'Create Playlist')
        self.assertEqual(search_buttons[1].text, 'Discover')

        return search_buttons

    def type_on_search_bar(self, text):

        search_box = self.driver.find_element_by_class_name('google-search')
        search_box.send_keys(text)


if __name__ == '__main__':
    unittest.main()