# This file will parse the data from the deal
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class BookingReport:
    def __init__(self, boxes_section_element: WebElement):
        self.bse = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()

    def pull_deal_boxes(self):
        return self.bse.find_elements(
            By.CSS_SELECTOR,
            'div[data-testid="property-card"]'
        )

    def pull_title_and_price(self):
        collections = []
        for deal_box in self.deal_boxes:
            hotel_price = deal_box.find_element(
                By.CLASS_NAME,
                '_e885fdc12'
            ).text
            hotel_name = deal_box.find_element(
                By.CSS_SELECTOR,
                'div[data-testid="title"]'
            ).text

            collections.append(
                [hotel_name, hotel_price]
            )
        return collections
