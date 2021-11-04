# This file will use for Filtration after the search is complete

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BookingFiltration:
    def __init__(self, driver: WebDriver):
        self.d = driver

    def star_filtration(self, *stars):
        box_element = self.d.find_element(
            By.CSS_SELECTOR,
            'div[data-filters-group="class"]'
        )
        inside_elements = box_element.find_elements(
            By.CSS_SELECTOR,
            '*'
        )
        for star in stars:
            for star_element in inside_elements:
                if str(star_element.get_attribute('innerHTML')).strip() == f'{star} stars':
                    star_element.click()
                elif str(star_element.get_attribute('innerHTML')).strip() == f'{star} star':
                    star_element.click()

    def lowest_price_filtration(self):
        lowest_price_btn = self.d.find_element(
            By.CSS_SELECTOR,
            'li[data-id="price"]'
        )
        lowest_price_btn.click()
