import time

import pytest

from pageObjects.Clientdelay_to_scrollbars_page_objects import Client_side_delay, Click, TexbBox, Scrollbars_page_object
from utilites.Logger import Log_genrator_class
from utilites.ReadProperties import Readconfig, TextBox_data


@pytest.mark.usefixtures("browser_setup")
class Test_clientdelay_to_scrollbars:
    driver=None
    clientdelay_url=Readconfig.get_client_delay_url()
    click_url=Readconfig.get_click_url()
    textbox_url=Readconfig.get_textbox_url()
    button_text = TextBox_data.get_data_button_text()
    scroller_url=Readconfig.get_scrollbars_url()

    logs=Log_genrator_class.logs_method(f".\\Logs\\clientdelay_to_scrollbars.log")
    logs_for_Textbox=Log_genrator_class.logs_method(f".\\Logs\\textbox_logs.log")


    @pytest.mark.skip
    def test_client_delay_005(self):
        self.logs.info("--Starting test_client_delay_005----")
        self.driver.get(self.clientdelay_url)
        self.logs.info(f"URL--->{self.clientdelay_url}")
        self.logs.info(f"TITLE--->{self.driver.title}")
        assert self.driver.title=="Client Side Delay","We are not in correct page"
        self.logs.info("---End TestCase test_client_delay_005---")
        self.client=Client_side_delay(self.driver)
        self.client.click_button_tringger()
        message=self.client.message_for_print()
        print(f"message--> {message}")
        self.logs.info(f"Message for dealy client checking--->{message}")

    @pytest.mark.flaky(reruns=2, reruns_delay=2)
    def test_click_006(self):
        self.logs.info("\n----starting test_click_006-----")
        self.driver.get(self.click_url)
        self.logs.info(f"URL--->{self.click_url}")
        assert self.driver.title=="Click"
        self.logs.info(f"TITLE--->{self.driver.title}")
        self.click=Click(self.driver)
        self.click.click_badButton()
        time.sleep(4)


    def test_textbox_007(self):

        self.logs_for_Textbox.info("----------------\nStarting test_text_box_007---------------")
        self.driver.get(self.textbox_url)
        self.logs_for_Textbox.info(f"----opening url---> {self.textbox_url}")
        self.logs_for_Textbox.info(f"Page Title ---> {self.driver.title}")
        assert self.driver.title=="Text Input","We not landed correct page"
        self.text_ob=TexbBox(self.driver)
        self.text_ob.text_box_send_value(self.button_text)
        self.text_ob.click_button_text()
        verify = self.text_ob.button_text_verication()
        self.logs_for_Textbox.info(f"button_text ---> {self.button_text}")
        self.logs_for_Textbox.info(f"from page same text for verfily ---> {verify}")
        assert verify==self.button_text,"I think we missing something"

    def test_scroller_btn_click_008(self):
        self.driver.get(self.scroller_url)
        self.scoller=Scrollbars_page_object(self.driver)
        btn=self.scoller.click_button_scoller()
        assert btn.is_displayed() and  btn.is_enabled() ,"Button is not clickable"



