import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

class Sampleapp_to_overlapped_class:
    xpath_uername="UserName"
    xpath_password="Password"
    login_button_xpath="//button[@id='login']"
    log_in_status_id="loginstatus"

    def __init__(self,driver):
        self.driver=driver

    def username_fill(self,name):
        username=self.driver.find_element(By.NAME,self.xpath_uername)
        username.send_keys(name)

    def password_fill(self,password):
        passwr=self.driver.find_element(By.NAME,self.xpath_password)
        passwr.send_keys(password)

    def click_login_button(self):
        button=self.driver.find_element(By.XPATH,self.login_button_xpath)
        button.click()

    def login_status_text(self):
        message=self.driver.find_element(By.ID,self.log_in_status_id)
        return message.text

class Mouse_Hover:
    xpath_click_btn="//a[@title='Active Link']"

    def __init__(self,driver):
        self.driver=driver
    def click_me_button(self):
        button=self.driver.find_element(By.XPATH,self.xpath_click_btn)
        actonchain=ActionChains(self.driver)
        actonchain.move_to_element(button).click().perform()
        # button.click()
        time.sleep(3)
        self.driver.save_screenshot(".\\Screenshots\\checkme_button.png")


class Non_Breaking_Space_class:
    button_xpath = "//button[text()='My\u00A0Button']"

    def __init__(self, driver):
        self.driver = driver

    def click_button(self):
        button1=self.driver.find_element(By.XPATH,self.button_xpath)
        button1.click()
        return button1







