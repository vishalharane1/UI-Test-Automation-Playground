from selenium.webdriver.common.by import By

class ShadowDOMPage:

    HOST = "guid-generator"

    def __init__(self, driver):
        self.driver = driver

    def get_shadow_root(self):
        host = self.driver.find_element(By.CSS_SELECTOR, self.HOST)
        return self.driver.execute_script(
            "return arguments[0].shadowRoot", host
        )

    def click_generate(self):
        shadow = self.get_shadow_root()
        shadow.find_element(By.CSS_SELECTOR, "button:nth-of-type(1)").click()

    def click_copy(self):
        shadow = self.get_shadow_root()
        shadow.find_element(By.CSS_SELECTOR, "button:nth-of-type(2)").click()

    def get_guid(self):
        shadow = self.get_shadow_root()
        return shadow.find_element(By.CSS_SELECTOR, "input").get_attribute("value")