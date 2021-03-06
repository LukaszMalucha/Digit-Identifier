from selenium.webdriver.common.by import By

from tests.acceptance.locators.base_page import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'http://127.0.0.1:5000'

    @property
    def title(self):
        return self.driver.find_element(*BasePageLocators.TITLE)

    @property
    def navigation(self):
        return self.driver.find_elements(*BasePageLocators.NAV_LINKS)

    @property
    def dropdown(self):
        return self.driver.find_element(*BasePageLocators.DROPDOWN)

    @property
    def dropdown_links(self):
        return self.driver.find_elements(*BasePageLocators.DROPDOWN_LINKS)

    @property
    def clear_button(self):
        return self.driver.find_element(*BasePageLocators.CLEAR_BUTTON)

    @property
    def download_button(self):
        return self.driver.find_element(*BasePageLocators.DOWNLOAD_BUTTON)

    @property
    def predict_button(self):
        return self.driver.find_element(*BasePageLocators.PREDICT_BUTTON)

    @property
    def result(self):
        return self.driver.find_element(*BasePageLocators.RESULT)

    def form_field(self, name):
        return self.form.find_element(By.ID, name)
