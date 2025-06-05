import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def driver():
    #Setup
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    driver.maximize_window()

    yield driver  # Provide the fixture value

    # Teardown
    driver.quit()

