# This file is going to include that will parse 
# the specific data that we need from each one of the deal boxes.

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BookingReport:
    def __init__(self,boxes_section_element:WebDriver):
        self.boxes_section_element=boxes_section_element
        self.deal_boxes = self.pull_deal_boxes_info()
    
    def pull_deal_boxes_info(self):
        return self.boxes_section_element.find_elements(By.CSS_SELECTOR,"[data-testid='property-card']")
    
    def pull_deal_box_details(self):
        collection = []
        # Pulling the titles of the hotels
        for deal_box in self.deal_boxes:
            hotel_name=deal_box.find_element(By.CSS_SELECTOR,"[data-testid='title']").get_attribute('innerHTML').strip()
            hotel_price=deal_box.find_element(By.CSS_SELECTOR,"[data-testid='price-and-discounted-price']").text.strip()
            hotel_score=deal_box.find_element(By.CSS_SELECTOR,"[class='a3b8729ab1 d86cee9b25']").text.strip()
            collection.append([hotel_name,hotel_price,hotel_score])
        
        return collection
        
            
        