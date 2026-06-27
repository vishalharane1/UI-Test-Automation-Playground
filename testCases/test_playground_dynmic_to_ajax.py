import time

import pytest

from pageObjects.Dynamic_to_ajax_Page_objects import Dynamic_ID, Classattr, Hidden_Layer, Ajax_data
from utilites.Logger import Log_genrator_class
from utilites.ReadProperties import Readconfig


@pytest.mark.usefixtures("browser_setup")
class Test_UI_Play:
    dynamic_url=Readconfig.get_dynamic_url()
    class_attr_url=Readconfig.get_classattr()
    hiddenlayers_url=Readconfig.get_hiddenlayers()
    logs=Log_genrator_class.logs_method(r"Logs/UITesting_Playgrond_second.log")
    url_ajax=Readconfig.get_ajex_url()

    def test_dynamic_001(self):
        self.driver.get(self.dynamic_url)
        self.logs.info("\n------Start Testing test_dynamic_001---")
        self.logs.info(f"URL working on {self.dynamic_url}")
        print(f"\nTitle --->{self.driver.title}")
        self.logs.info(f"Title-- {self.driver.title}")
        assert self.driver.title=="Dynamic ID"
        self.dy_click=Dynamic_ID(self.driver)
        btn_enable=self.dy_click.get_click_btn_dynamic()
        assert btn_enable.is_enabled(), "Button is not enabled"
        self.logs.info("Button clicked now working ")
        self.dy_click.click_btn()
        self.logs.info("Button clicked now End dynamic Button Click ")
        self.logs.info("\n------END Testing test_dynamic_001---")

    def test_classattr_002(self):
        self.logs.info("\n------Starting Testing test_classattr_002---")
        self.driver.get(self.class_attr_url)
        self.logs.info(f"Url we working on -->{self.class_attr_url}")
        print(f"\n --Title{self.driver.title}")
        self.logs.info(f"--Title---{self.driver.title}")
        assert self.driver.title=="Class Attribute","We are not correct page"
        self.class_attr=Classattr(self.driver)
        self.class_attr.click_aviable_btn()
        self.logs.info("\n------END Testing test_classattr_002---")
    @pytest.mark.smoke
    def test_hiddenlayers_003(self):
        self.logs.info("\n-----Starting of test_hiddenlayers_003-----")
        self.driver.get(self.hiddenlayers_url)
        self.logs.info(f"URL--->{self.hiddenlayers_url}")
        assert self.driver.title=="Hidden Layers","We not landed correct page"
        self.logs.info(f"Page Title--> {self.driver.title}")
        self.hideen_op=Hidden_Layer(self.driver)
        # btn_enable2= self.hideen_op.click_btn()
        # assert btn_enable2.is_enabled(), "Button is not enabled"
        before_colour=self.hideen_op.button_verfily()
        self.logs.info(f"Aflter clicking button colour--> {before_colour}")

        self.hideen_op.click_btn_hidden()
        self.logs.info(f"Before click button colour--> {before_colour}")

    def test_ajax_004(self):
        self.logs.info("\n----Starting test_ajax_004----")
        self.driver.get(self.url_ajax)
        self.logs.info(f"Title of page--->{self.driver.title}")
        assert self.driver.title=="AJAX Data","We landed wrong page"
        self.ajax=Ajax_data(self.driver)
        self.ajax.click_ajax_button()
        message=self.ajax.print_message()
        self.logs.info(f"After clicking button message--->{message}")






