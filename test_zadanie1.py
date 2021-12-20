import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TestMBank:

    def setup(self):
        """
        Setup for tests. Open browser and maximize window, open login page and find basic element for login.
        :return:
        """
        self.driver = webdriver.Chrome('.\drivers\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('http://demo.testarena.pl/zaloguj')
        self.driver.implicitly_wait(5)
        self.email_box = self.driver.find_element('id', 'email')
        self.password_box = self.driver.find_element('id', 'password')
        self.button = self.driver.find_element('id', 'login')

    @pytest.mark.parametrize("_login, _password", 'expected',
                             [('administrator@testarena.pl', 'sumXQQ72$L', 'Kokpit - TestArena Demo')])
    def test_login_correct(self, _login, _password, expected):
        """
        Test login on website with correct data
        :param _login: login email
        :param _password: login password
        :param expected: expected site title after login
        :return:
        """
        self.email_box.send_keys(_login)
        self.password_box.send_keys(_password)
        self.button.click()

        assert self.driver.title == expected

    @pytest.mark.parametrize("_login, _password", 'expected',
                             [('administrator@testarena.pl', 'sumXQQ72$L', 'Kokpit - TestArena Demo')])
    def test_add_new_task(self, _login, _password, expected):
        """
        Test login on website, go to project and add new task.
        :param _login: login email
        :param _password: login password
        :param expected: expected site title after login
        :return:
        """
        self.email_box.send_keys(_login)
        self.password_box.send_keys(_password)
        self.button.click()
        assert self.driver.title == expected

        self.project_box = self.driver.find_element('xpath',
                                                    '/html/body/header/div[1]/span/div[1]/form/div/a/span').click()
        self.project_box_name = self.driver.find_element('xpath',
                                                         '/html/body/header/div[1]/span/div[1]/form/div/div/div/input')
        self.project_box_name.send_keys('Projekt_testowy_MB')
        self.project_box_name.send_keys(Keys.RETURN)
        self.tasks_menu = self.driver.find_element('xpath', '/html/body/aside/div/ul/li[7]/a')

        self.tasks_menu.click()
        self.add_task = self.driver.find_element('xpath', '/html/body/div[1]/section/article/nav/ul/li/a').click()
        # find elements on page
        self.task_title = self.driver.find_element('xpath', '//*[@id="title"]')
        self.task_description = self.driver.find_element('xpath', '//*[@id="description"]')
        self.task_release_name = self.driver.find_element('xpath', '//*[@id="releaseName"]')
        self.task_environments = self.driver.find_element('xpath', '//*[@id="token-input-environments"]')
        self.task_version = self.driver.find_element('xpath', '//*[@id="token-input-versions"]')
        self.task_priority = self.driver.find_element('xpath', '//*[@id="priority"]')
        self.task_priority_critical = self.driver.find_element('xpath',
                                                               '/html/body/div[1]/section/article/form/div[7]/span/div/select/option[1]')
        self.task_date = self.driver.find_element('xpath', '//*[@id="dueDate"]')
        self.task_assignee_name = self.driver.find_element('xpath', '//*[@id="assigneeName"]')
        self.task_tags = self.driver.find_element('xpath', '//*[@id="token-input-tags"]')
        self.task_assign_to_me = self.driver.find_element('xpath', '//*[@id="j_assignToMe"]')
        self.task_save_button = self.driver.find_element('xpath', '//*[@id="save"]')

        self.task_title.send_keys('Testowanie aplikacji webowej.')
        self.task_description.send_keys(
            'W zadaniu należy przetestować wszystkie elementy znajdujące się na strone startowej www.google.com')
        self.task_release_name.send_keys('test')
        self.task_environments.send_keys('Chrome')
        time.sleep(0.5)
        self.task_environments.send_keys(Keys.RETURN)
        self.task_version.send_keys('0.1')
        time.sleep(0.5)
        self.task_version.send_keys(Keys.ENTER)
        self.task_priority.click()
        self.task_priority_critical.click()
        self.task_date.send_keys('2022-01-03 23:59')
        self.task_assign_to_me.click()
        self.task_save_button.click()

        self.task_add_confirm = self.driver.find_element('xpath', '/html/body/div[1]/p').get_attribute('innerHTML')

        assert self.task_add_confirm == 'Zadanie zostało dodane.'

    @pytest.mark.parametrize("_login, _password", 'expected',
                             [('administrator@testarena.pl', 'sdasdawad', 'Kokpit - TestArena Demo'),
                              ('dsadasdasd', 'sumXQQ72$L', 'Kokpit - TestArena Demo'),
                              ('ddasdas', 'e1231', 'Kokpit - TestArena Demo')])
    def test_login_incorrect(self, _login, _password, expected):
        self.email_box.send_keys(_login)
        self.password_box.send_keys(_password)
        self.button.click()

        assert self.driver.title != expected

    def teardown(self):
        """
        Teardown for test. Close webdriver.
        :return:
        """
        self.driver.close()
        self.driver.quit()
