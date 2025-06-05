import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import allure


@allure.title("Test Login with Valid Credentials")
def test_login_with_valid_credentials(driver):
    driver.find_element(By.LINK_TEXT, "Make Appointment").click()
    action = ActionChains(driver)

    username_field = driver.find_element(By.NAME, "username")
    action.click(username_field).send_keys("John Doe").perform()
    password_field = driver.find_element(By.NAME, "password")
    action.click(password_field).send_keys("ThisIsNotAPassword").perform()
    driver.find_element(By.ID, "btn-login").click()
    expected_text = 'Make Appointment'
    actual_text = driver.find_element(By.XPATH, "// h2[text() = 'Make Appointment']").text
    assert expected_text == actual_text


@allure.title("Test Login with Invalid Credentials")
def test_login_with_invalid_credentials(driver):
    driver.find_element(By.LINK_TEXT, "Make Appointment").click()
    action = ActionChains(driver)
    name = 'Aniket Jaiswal'
    passWord = '123123123'
    username_field = driver.find_element(By.NAME, "username")
    action.click(username_field).send_keys(name).perform()
    password_field = driver.find_element(By.NAME, "password")
    action.click(password_field).send_keys(passWord).perform()
    driver.find_element(By.ID, "btn-login").click()
    expected_text = 'Make Appointment.'
    actual_text = driver.find_element(By.XPATH, "//p[@class='lead text-danger']").text
    if expected_text != actual_text:
        driver.get_screenshot_as_file("screenshots/login-failed-with-invalid-cred.png")
        allure.attach(driver.get_screenshot_as_png(), name="Invalid Creds", attachment_type=allure.attachment_type.PNG)
        print("Screenshot Captured!!")
        print("Invalid credentials :")
        print("Name : " + name)
        print("Password :" + passWord)
        assert expected_text == actual_text


@allure.title("Test Login with Valid Username and Invalid Password")
def test_login_with_invalid_password(driver):
    driver.find_element(By.LINK_TEXT, "Make Appointment").click()
    action = ActionChains(driver)
    name = 'John Doe'
    passWord = '123123123'
    username_field = driver.find_element(By.NAME, "username")
    action.click(username_field).send_keys(name).perform()
    password_field = driver.find_element(By.NAME, "password")
    action.click(password_field).send_keys(passWord).perform()
    driver.find_element(By.ID, "btn-login").click()
    expected_text = 'Make Appointment.'
    actual_text = driver.find_element(By.XPATH, "//p[@class='lead text-danger']").text
    if expected_text != actual_text:
        driver.get_screenshot_as_file("screenshots/login-failed-with-invalid-password.png")
        allure.attach(driver.get_screenshot_as_png(), name="Invalid Password",
                      attachment_type=allure.attachment_type.PNG)
        print("Screenshot Captured!!")
        print("Invalid credentials(Password) :")
        print("Name : " + name)
        print("Password :" + passWord)
        assert expected_text == actual_text


@allure.title("Test Login with Invalid Username and Valid Password")
def test_login_with_invalid_username(driver):
    driver.find_element(By.LINK_TEXT, "Make Appointment").click()
    action = ActionChains(driver)
    name = 'Rohan '
    passWord = 'ThisIsNotAPassword'
    username_field = driver.find_element(By.NAME, "username")
    action.click(username_field).send_keys(name).perform()
    password_field = driver.find_element(By.NAME, "password")
    action.click(password_field).send_keys(passWord).perform()
    driver.find_element(By.ID, "btn-login").click()
    expected_text = 'Make Appointment.'
    actual_text = driver.find_element(By.XPATH, "//p[@class='lead text-danger']").text
    if expected_text != actual_text:
        driver.get_screenshot_as_file("screenshots/login-failed-with-invalid-username.png")
        allure.attach(driver.get_screenshot_as_png(), name="Invalid Username",
                      attachment_type=allure.attachment_type.PNG)
        print("Screenshot Captured!!")
        print("Invalid credentials(Username) :")
        print("Name : " + name)
        print("Password :" + passWord)
        assert expected_text == actual_text


@allure.title("Test Login Without Credentials")
def test_login_without_credentials(driver):
    driver.find_element(By.LINK_TEXT, "Make Appointment").click()
    action = ActionChains(driver)

    username_field = driver.find_element(By.NAME, "username")
    action.click(username_field).send_keys("").perform()
    password_field = driver.find_element(By.NAME, "password")
    action.click(password_field).send_keys("").perform()
    driver.find_element(By.ID, "btn-login").click()
    expected_text = 'Make Appointment'
    actual_text = driver.find_element(By.XPATH, "//p[@class='lead text-danger']").text

    if expected_text != actual_text:
        driver.get_screenshot_as_file("screenshots/login-failed-without-cred.png")
        allure.attach(driver.get_screenshot_as_png(), name="Without Creds", attachment_type=allure.attachment_type.PNG)
        print("Screenshot Captured!!")
        print("No credentials :")
        print("Name : ''")
        print("Password : '' ")
        assert expected_text == actual_text

