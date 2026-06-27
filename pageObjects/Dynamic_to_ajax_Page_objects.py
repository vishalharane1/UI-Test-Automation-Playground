from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Dynamic_ID:
    btn_click_dynamic_class_name="btn-primary"
    def __init__(self,driver):
        self.driver=driver

    def get_click_btn_dynamic(self):
        btn_click=self.driver.find_element(By.CLASS_NAME,self.btn_click_dynamic_class_name)
        return btn_click
    def click_btn(self):
        self.get_click_btn_dynamic().click()

class Classattr:
    btn1_classname="class1"
    btn2_classname="class2"
    btn3_classname="class3"

    def __init__(self, driver):
        self.driver = driver
    def get_btn1(self):
        btn_click1=self.driver.find_element(By.CLASS_NAME,self.btn1_classname)
        return btn_click1
    def get_btn2(self):
        btn_click2=self.driver.find_element(By.CLASS_NAME,self.btn2_classname)
        return btn_click2
    def get_btn3(self):
        btn_click3=self.driver.find_element(By.CLASS_NAME,self.btn3_classname)
        return btn_click3

    def click_aviable_btn(self):
        buttons = [
            ("Button1", self.get_btn1),
            ("Button2", self.get_btn2),
            ("Button3", self.get_btn3)
        ]
        for name,button  in buttons:
            try:
                btn=button()
                if btn.is_displayed() and btn.is_enabled():
                    btn.click()
                    try:
                        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
                        print(f"{name} clicked successfully")
                        print(f"{name} generated alert")
                        print("Alert Text :", alert.text)

                        alert.accept()  # OK button press
                        return name

                    except TimeoutException:(
                        print(f"{name} clicked but no alert found"))
                    return name
            except (NoSuchElementException, ElementNotInteractableException):
                continue

        print("No button is clickable")
        return None

class Hidden_Layer:
    btn_xpath="greenButton"
    def __init__(self, driver):
        self.driver = driver

    def click_btn_hidden(self):
        green_bnt=WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID,self.btn_xpath)))
        green_bnt.click()
        # btn_click=self.driver.find_element(By.ID,self.btn_xpath)
        # btn_click.click()
    def button_verfily(self):
        button = self.driver.find_element(By.ID, self.btn_xpath)
        color = button.value_of_css_property("background-color")
        print(color)
        return color


class Ajax_data:
    button_xpath="//button[@id='ajaxButton']"
    message_class="bg-success"

    def __init__(self, driver):
        self.driver = driver

    def click_ajax_button(self):
        self.driver.find_element(By.XPATH,self.button_xpath).click()

    def print_message(self):
        try:
            message=WebDriverWait(self.driver,15,2).until(EC.visibility_of_element_located((By.CLASS_NAME,self.message_class)))
            return message.text
        except:
            print("IT take more time")













