import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_option=Options()
chrome_option.add_argument("--headless")
chrome_option.add_argument("--ignore-certificate-errors")
chrome_option.add_argument("--ignore-ssl-errors")
chrome_option.add_argument("--allow-running-insecure-content")
from selenium.webdriver.edge.options import Options

edge_option = Options()
edge_option.add_argument("--ignore-certificate-errors")
edge_option.add_argument("--ignore-ssl-errors")
edge_option.add_argument("--allow-running-insecure-content")

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="class")
def browser_setup(request):
    browser=request.config.getoption("--browser")
    if browser=="chrome":
        print("-----Lunching Chrome browser----")
        driver=webdriver.Chrome()
    elif browser=="edge":
        print("-----Lunching edge browser----")
        driver=webdriver.Edge()
    elif browser=="firefox":
        print("-----Lunching firefox browser----")
        driver=webdriver.Firefox()
    elif browser=="headless":
        print("-----Lunching Chrome headless browser----")
        driver=webdriver.Chrome(options=chrome_option)
    else:
        print("-----Lunching Edge in else wala browser----")
        driver = webdriver.Edge(options=edge_option)
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver=driver
    yield driver
    driver.quit()


@pytest.fixture(params=[("user","pwd","loginpass"),
                        ("user","pwd2","loginfail"),
                        ("user","pwd3","loginfail"),
                        ("user","pwd4","loginfail")
])
def test_data_sampleapp(request):
    return request.param