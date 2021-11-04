import bookings.constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from bookings.booking_Filterartion import BookingFiltration
from bookings.booking_report import BookingReport



# import os


class Booking(webdriver.Chrome):
    def __init__(self, exiting=False):

        # These three lines will help in resolving the DevTools Error.
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super().__init__(options=options)

        # It helps in maintaining the exit after the program finish its work.
        self.ex = exiting

        # This will help in the slow loading scenarios.
        self.implicitly_wait(15)
        self.maximize_window()

    # def __init__(self, driver_path=r"C:\Piyush\Drivers"):
    #     self.driver = driver_path
    #     os.environ['PATH'] += driver_path
    #     super(Booking, self).__init__()

    # This is a Magic Function for maintaining exiting of the Window after the program worked perfectly
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.ex:
            self.quit()

    # This function will start the browser and go to the URL
    def land_page(self):
        self.get(const.BASE_URL)

    # It helps in changing the page currency
    def change_currency(self, currency=None):
        currency_element = self.find_element(
            By.CSS_SELECTOR,
            'button[data-tooltip-text="Choose your currency"]'
        )
        currency_element.click()

        select_currency = self.find_element(
            By.CSS_SELECTOR,
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )

        select_currency.click()

    # Selecting the place to go
    def select_place_to_go(self, place_name=None):
        search_field = self.find_element(By.ID, 'ss')
        search_field.clear()
        search_field.send_keys(place_name)

        first_result = self.find_element(By.CSS_SELECTOR, 'li[data-i="0"]')
        first_result.click()

    def select_dates(self, check_in_dates, check_out_dates):
        check_in_element = self.find_element(
            By.CSS_SELECTOR,
            f'span[aria-label="{check_in_dates}"]'
        )
        check_in_element.click()
        check_out_element = self.find_element(
            By.CSS_SELECTOR,
            f'span[aria-label="{check_out_dates}"]'
        )
        check_out_element.click()

    def select_adults(self, count=0):
        select_element = self.find_element(
            By.ID,
            'xp__guests__toggle'
        )
        select_element.click()

        decreasing_btn = self.find_element(
            By.CSS_SELECTOR,
            'button[aria-label="Decrease number of Adults"]'
        )
        increase_btn = self.find_element(
            By.CSS_SELECTOR,
            'button[aria-label="Increase number of Adults"]'
        )
        # This loop helps in decreasing the no. of adults to 1
        while True:
            decreasing_btn.click()
            adults_count = self.find_element(
                By.ID,
                'group_adults'
            ).get_attribute('value')
            if int(adults_count) == 1:
                break

        for i in range(count - 1):
            increase_btn.click()

    def search(self):
        search_btn = self.find_element(
            By.CSS_SELECTOR,
            'button[type="submit"]'
        )
        search_btn.click()

    def start_filtration(self):
        filtration = BookingFiltration(driver=self)
        filtration.star_filtration(3)
        filtration.lowest_price_filtration()

    def show_results(self):
        hotel_boxes_list = self.find_element(
            By.CLASS_NAME,
            '_814193827'
        )
        report = BookingReport(hotel_boxes_list)
        print(report.pull_title_and_price())
