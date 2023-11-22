#This file will include a class with instance methods to filter the booking data
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BookingFilteration:
    def __init__(self,driver:WebDriver):
        self.driver=driver
    
    def apply_star_rating(self,*star_values):
        star_filteration_box = self.driver.find_element(By.ID,"filter_group_class_:rt:")
        star_child_elements = star_filteration_box.find_elements(By.CSS_SELECTOR,"*")
        
        for star_value in star_values:
            for star_element in star_child_elements:
                if star_element.get_attribute('innerHTML').strip()==(f'{star_value} stars'):
                    star_element.click()
                    break
    
    def sort_price_lowest_first(self):
        list_element=self.driver.find_element(By.CSS_SELECTOR,"button[data-testid='sorters-dropdown-trigger']")
        list_element.click()
        element=self.driver.find_element(By.CSS_SELECTOR,"button[data-id='price']")
        element.click()

    

        
