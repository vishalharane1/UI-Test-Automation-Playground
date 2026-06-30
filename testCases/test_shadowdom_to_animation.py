import pyperclip
import pytest

from pageObjects.shadowdom_to_animation_page_objects import ShadowDOMPage
from utilites.Read_properties_shadowdom_to_animation import Read_url_showdown_to_animation


@pytest.mark.usefixtures("browser_setup")
class Test_shadowndom_to_animation:
    driver=None
    shodowndom_url=Read_url_showdown_to_animation.get_showdown_url()

    def test_shadowndom_016(self):
        self.driver.get(self.shodowndom_url)
        assert self.driver.title=="Shadow DOM","We not landed correct page"
        shadow=ShadowDOMPage(self.driver)
        shadow.click_generate()

        input_guid = shadow.get_guid()

        assert input_guid != ""

        shadow.click_copy()

        clipboard_text = pyperclip.paste()

        print(input_guid)
        print(clipboard_text)

        assert clipboard_text == input_guid

