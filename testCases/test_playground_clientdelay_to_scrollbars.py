import time

import pytest

from pageObjects.Clientdelay_to_scrollbars_page_objects import Client_side_delay, Click
from utilites.Logger import Log_genrator_class
from utilites.ReadProperties import Readconfig


@pytest.mark.usefixtures("browser_setup")
class Test_clientdelay_to_scrollbars:
    driver=None
    clientdelay_url=Readconfig.get_client_delay_url()
    click_url=Readconfig.get_click_url()
    logs=Log_genrator_class.logs_method(f".\\Logs\\clientdelay_to_scrollbars.log")


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

    def test_click_006(self):
        self.logs.info("\n----starting test_click_006-----")
        self.driver.get(self.click_url)
        self.logs.info(f"URL--->{self.click_url}")
        assert self.driver.title=="Click"
        self.logs.info(f"TITLE--->{self.driver.title}")
        self.click=Click(self.driver)
        self.click.click_badButton()
        time.sleep(4)



