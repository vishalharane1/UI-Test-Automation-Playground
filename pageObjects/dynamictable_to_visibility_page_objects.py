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



