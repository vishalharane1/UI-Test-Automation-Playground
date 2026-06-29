import time

import allure
from selenium.webdriver.common.by import By


class Dynamictable:
    table_len_xpath="//span[@role='cell'][1]"
    verfiy_value_xpath="/html/body/section/div/p[2]"
    # abs_xpath_dynamic=f"/html[1]/body[1]/section[1]/div[1]/div[1]/div[3]/div[{i}]/span[5]"

    def __init__(self,driver):
        self.driver=driver

    def get_len_from_table(self):
        len_table=self.driver.find_elements(By.XPATH,self.table_len_xpath)
        return len(len_table)

    def table_interable_xpath(self,abs_xpath=None):
        return self.driver.find_element(By.XPATH,abs_xpath).text

    def verfiy_text(self):
        return self.driver.find_element(By.XPATH,self.verfiy_value_xpath).text


class Verify_text_class:
    text_class="bg-primary"

    def __init__(self,driver):
        self.driver=driver

    def text_ruturn(self):
        return self.driver.find_element(By.CLASS_NAME,self.text_class).text

class Progressbar_class:
    start_button_xpath="//button[@id='startButton']"
    stop_button_xpath="//button[@id='stopButton']"
    processbar_id="progressBar"
    def __init__(self, driver):
        self.driver = driver
    def click_processbar_button(self):
        self.driver.find_element(By.XPATH,self.start_button_xpath).click()
        while True:
            progress = self.driver.find_element(By.ID,self.processbar_id).text
            # Example: "75%"

            if progress == "75%":
                self.driver.find_element(By.XPATH, self.stop_button_xpath).click()
                self.driver.save_screenshot(".\\Screenshots\\Processbar_status.png")
                # def click_stop_button(self):
                #     self.driver.find_element(By.XPATH,self.stop_button_xpath).click()
                break


class visibility_class:
    hide_button_xpath="//button[@id='hideButton']"
    removedButton="removedButton"
    zeroWidthButton="zeroWidthButton"
    overlappedButton="overlappedButton"


    def allure_attech_screeshot(self,name="screenshot00+"):
        allure.attach(self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    def __init__(self, driver):
        self.driver = driver
    def click_hide_button(self):
        self.driver.find_element(By.XPATH, self.hide_button_xpath).click()
        time.sleep(3)
        self.allure_attech_screeshot("Button is visbile or not checking")
        self.driver.save_screenshot(".\\Screenshots\\button_visiblity.png")
    def click_removedButton(self):
        removedButton=self.driver.find_element(By.ID, self.removedButton)
        return removedButton

    def click_zeroWidthButton(self):
        zeroWidthButton= self.driver.find_element(By.ID, self.zeroWidthButton)
        return zeroWidthButton

    def click_overlappedButton(self):
        overlappedButton= self.driver.find_element(By.ID, self.overlappedButton)
        return overlappedButton











