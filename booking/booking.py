from selenium import webdriver
from selenium.webdriver.common.by import By
import booking.constants as const
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from booking.booking_filteration import BookingFilteration
from booking.booking_report import BookingReport
from prettytable import PrettyTable
import time


class Booking(webdriver.Chrome):
   
    def __init__(self,teardown=False):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach',True)
        options.add_experimental_option('excludeSwitches',['enable-logging'])
        self.teardown=teardown
        super(Booking,self).__init__(options=options)
        self.implicitly_wait(5)
        self.maximize_window()

    def __exit__(self,exc_type,exc_value,exc_tb):
        if self.teardown:
            self.quit()
        


    def land_first_page(self):
        self.get(const.BASE_URL)

    def close_signin_modal(self):
        close_modal=self.find_element(By.CSS_SELECTOR,'[aria-label="Dismiss sign-in info."]')
        close_modal.click()
    
    def change_currency(self,currency=None):
        currency_element=self.find_element(By.CSS_SELECTOR,'button[data-testid="header-currency-picker-trigger"]')
        currency_element.click()
        
        selected_currency_element=self.find_element(By.XPATH,(f'//div[contains(text(),"{currency}")]'))
        selected_currency_element.click()

    def select_place_to_go(self,place):
        search_field=self.find_element(By.ID,":re:")
        search_field.clear()
        search_field.send_keys(place)  
        time.sleep(1)
        first_result=self.find_element(By.ID,"autocomplete-result-0")
        first_result.click()
    
    def select_date(self,check_in_date,check_out_date,interval=0):
        check_in_element = self.find_element(By.CSS_SELECTOR, (f'span[data-date="{check_in_date}"]'))
        check_in_element.click()
        next_month_select_element = self.find_element(By.CSS_SELECTOR,'button[class="a83ed08757 c21c56c305 f38b6daa18 d691166b09 f671049264 deab83296e f4552b6561 dc72a8413c f073249358"]')
        for i in range(interval):
            next_month_select_element.click()
        
        check_out_element = self.find_element(By.CSS_SELECTOR, (f'span[data-date="{check_out_date}"]'))
        check_out_element.click()

    def select_adults(self,count=1):
        selection_element=self.find_element(By.CSS_SELECTOR,"button[data-testid='occupancy-config']")
        selection_element.click()
        decrease_adults_element=self.find_element(By.CSS_SELECTOR,"button[class='a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e bb803d8689 e91c91fa93']")
        
        while True:
            adult_count = self.find_element(By.CSS_SELECTOR,'span[class="d723d73d5f"]').text
            decrease_adults_element.click()
            #If the value of adult reaches 1, then we should get out of the loop
            if int(adult_count)==1:
                break

        increase_adult_element=self.find_element(By.CSS_SELECTOR,"button[class='a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e bb803d8689 f4d78af12a']")
        for i in range(count-1):
            increase_adult_element.click()
        

    def select_children(self,count=0):
        increase_children_element=self.find_element(By.CSS_SELECTOR,"button[class='a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e bb803d8689 f4d78af12a']")
        for i in range(count):
            increase_children_element.click()

    def select_room(self,count=1):
        increase_room_element=self.find_element(By.CSS_SELECTOR,"button[class='a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e bb803d8689 f4d78af12a']")
        for i in range(count-1):
            increase_room_element.click()

    def click_search(self):
        search_button=self.find_element(By.CSS_SELECTOR,"button[type='submit']")
        search_button.click()

    def apply_filtrations(self):
        filteration = BookingFilteration(driver=self)
        filteration.sort_price_lowest_first()
        filteration.apply_star_rating(3,4,5)

     #hotellist = document.querySelector("[class='d4924c9e74']")
     #hotellists.querySelectorAll("[data-testid='property-card']")

    def report_results(self):
        hotel_boxes=self.find_element(By.CLASS_NAME,"d4924c9e74")
        report = BookingReport(hotel_boxes)
        table = PrettyTable(field_names=["Hotel Name","Hotel Price","Hotel Score"])
        table.add_rows(report.pull_deal_box_details())
        print(table)
            


