import time

import pytest

from pageObjects.config_sampleapp_to_overlapped_page_objects import Sampleapp_to_overlapped_class, Mouse_Hover, \
    Non_Breaking_Space_class, Overlapped_Element_class
from utilites.Read_Properties_config_sampleapp_to_overlapped import Read_properties_sampleapp_to_overlapp


@pytest.mark.usefixtures("browser_setup")
class Test_sampleapp_to_overlapped_class:
    driver=None
    sampleapp_url=Read_properties_sampleapp_to_overlapp.get_url_sampleapp()
    mousehover_url=Read_properties_sampleapp_to_overlapp.get_url_mouseover()
    nbsp_url=Read_properties_sampleapp_to_overlapp.get_url_nbsp()
    overlapped_url = Read_properties_sampleapp_to_overlapp.get_url_overlapped()

    def test_sampleapp_014(self,test_data_sampleapp):
        self.driver.get(self.sampleapp_url)
        username1=test_data_sampleapp[0]
        password2=test_data_sampleapp[1]
        expected_result=test_data_sampleapp[2]
        assert self.driver.title=="Sample App","We landed incorrect page"
        self.sampleapp=Sampleapp_to_overlapped_class(self.driver)
        time.sleep(3)
        self.sampleapp.username_fill(username1)
        time.sleep(3)
        self.sampleapp.password_fill(password2)
        time.sleep(3)
        self.sampleapp.click_login_button()
        text_message=self.sampleapp.login_status_text()
        if text_message=="Welcome, user!":
            actual_result="loginpass"
        else:
            actual_result="loginfail"

        assert actual_result==expected_result,"Something doing wrong way"

    def test_mouseover_015(self):
        self.driver.get(self.mousehover_url)
        assert self.driver.title=="Mouse Over","We landed incorrect page"
        self.mousehv=Mouse_Hover(self.driver)
        self.mousehv.click_me_button()
        time.sleep(3)

    def test_click_nbsp(self):
        self.driver.get(self.nbsp_url)
        assert self.driver.title == "Non-Breaking Space", "We landed incorrect page"
        self.nbsp=Non_Breaking_Space_class(self.driver)
        self.nbsp.click_button()
        button=self.nbsp.click_button()
        assert button.is_enabled(),"Not Enabled to click nbsp button"

    def test_Overlapped_Element(self):
        self.driver.get(self.overlapped_url)
        assert self.driver.title == "Overlapped Element", "We landed incorrect page"
        self.overlapped=Overlapped_Element_class(self.driver)
        self.overlapped.Entet_Id("93938")
        self.overlapped.enter_name("vishal h")













