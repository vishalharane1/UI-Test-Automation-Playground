import time

import pytest

from pageObjects.dynamictable_to_visibility_page_objects import Dynamictable, Verify_text_class, Progressbar_class, \
    visibility_class
from utilites.Logger import Log_genrator_class
from utilites.Read_Properties_dynamictable_to_visibility import Read_Config_for_dynamic_visible

@pytest.mark.usefixtures("browser_setup")
class Test_Playgroud_003:
    driver=None

    url_dynamic=Read_Config_for_dynamic_visible.get_url_dynamic_table()
    verify_text_url=Read_Config_for_dynamic_visible.get_url_verifytext()
    Logs=Log_genrator_class.logs_method(".\\Logs\\dynamic_tables.logs")
    url_visibility=Read_Config_for_dynamic_visible.get_url_visibility()
    progressbar_url=Read_Config_for_dynamic_visible.get_url_progressbar()

    def test_dynamic_table_0010(self):
        self.driver.get(self.url_dynamic)


        self.Logs.info("---Starting fo test test_dynamic_table_0010---")
        self.Logs.info(f"---URL--->{self.url_dynamic}")
        self.Logs.info(f"---TITLE--->{self.driver.title}")
        assert self.driver.title=="Dynamic Table","Wa are not landed correct page"
        self.dyanicm=Dynamictable(self.driver)
        total_columns = self.dyanicm.get_len_from_table()
        verfily=self.dyanicm.verfiy_text()

        name_col = 0
        cpu_col = 0

        # Find Name and CPU column index
        for j in range(1, total_columns + 1):

            header = self.dyanicm.table_interable_xpath(
                f"/html/body/section/div/div/div[2]/div[1]/span[{j}]"
            )

            self.Logs.info(f"Header {j} ---> {header}")

            if header == "Name":
                name_col = j

            elif header == "CPU":
                cpu_col = j

        self.Logs.info(f"Name Column = {name_col}")
        self.Logs.info(f"CPU Column = {cpu_col}")

        # Find Chrome row
        for i in range(1, total_columns + 1):

            browser = self.dyanicm.table_interable_xpath(
                f"/html/body/section/div/div/div[3]/div[{i}]/span[{name_col}]"
            )

            if browser == "Chrome":
                cpu_value = self.dyanicm.table_interable_xpath(
                    f"/html/body/section/div/div/div[3]/div[{i}]/span[{cpu_col}]"
                )

                self.Logs.info(f"Chrome CPU Value ---> {cpu_value}")
                assert cpu_value in verfily, f"Expected {verfily}, but got {cpu_value}"

                break

    def test_verify_text_0011(self):
        self.driver.get(self.verify_text_url)
        self.Logs.info("---Starting fo test test_verify_text_0011---")
        assert self.driver.title=="Verify Text","We not landed correct page"
        self.ver_text=Verify_text_class(self.driver)
        self.Logs.info(f"----Title-- > {self.driver.title}")
        text= self.ver_text.text_ruturn()
        self.Logs.info(f"--Return text--->{text}")
        assert "Welcome" in text, f"Failed Test cases -->test_verify_text_0011 return text{text}"

    def test_progressbar_012(self):
        self.driver.get(self.progressbar_url)
        self.Logs.info("---Starting fo test test_progressbar_012---")
        assert self.driver.title == "Progress Bar", f"We not landed correct page page title-->{self.driver.title}"
        self.processbar=Progressbar_class(self.driver)
        self.processbar.click_processbar_button()
        # self.Logs.info(f"---Processbar--->{self.processbar.click_processbar_button().progress}")

    @pytest.mark.xfail
    def test_visibility_013(self):
        self.driver.get(self.url_visibility)
        self.vissiblity=visibility_class(self.driver)
        assert self.vissiblity.click_removedButton().is_displayed()
        assert self.vissiblity.click_zeroWidthButton().is_displayed()
        assert self.vissiblity.click_overlappedButton().is_displayed()
        self.vissiblity.click_hide_button()
        time.sleep(3)
        self.driver.save_screenshot(".\\Screenshots\\button_visiblity_23232.png")
        assert not self.vissiblity.click_removedButton().is_displayed()
        assert not  self.vissiblity.click_zeroWidthButton().is_displayed()
        assert not  self.vissiblity.click_overlappedButton().is_displayed()









