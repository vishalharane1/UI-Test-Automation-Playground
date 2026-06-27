import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Client_side_delay:
    button_id="ajaxButton"
    message_class="bg-success"

    def __init__(self,driver):
        self.driver=driver


    def click_button_tringger(self):
        self.driver.find_element(By.ID,self.button_id).click()


    def message_for_print(self):
        try:
            message=WebDriverWait(self.driver,15,2).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,self.message_class)))
            return message.text
        except:
            print("WE not foudn that message element ")

class Click:
    click_id="badButton"
    def __init__(self,driver):
        self.driver=driver

    def attach_screenshot(self, name="Screenshot"):
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    def click_badButton(self):
        self.driver.find_element(By.ID,self.click_id).click()
        self.attach_screenshot("Buttonclick_test")





