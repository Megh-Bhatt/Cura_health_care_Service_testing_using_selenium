import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import allure


@allure.title("Make appointment with Valid Credentials")
def test_make_appointment(driver):
    driver.find_element(By.LINK_TEXT, "Make Appointment").click()
    action = ActionChains(driver)

    username_field = driver.find_element(By.NAME, "username")
    action.click(username_field).send_keys("John Doe").perform()
    password_field = driver.find_element(By.NAME, "password")
    action.click(password_field).send_keys("ThisIsNotAPassword").perform()
    driver.find_element(By.ID, "btn-login").click()
    time.sleep(1)
    facility_field = driver.find_element(By.ID, "combo_facility")
    facility_dropdown = Select(facility_field)
    facility_dropdown.select_by_visible_text("Seoul CURA Healthcare Center")
    time.sleep(1)

    # checkbox
    driver.find_element(By.ID, "chk_hospotal_readmission").click()
    time.sleep(1)

    # Healthcare Program radio button
    driver.find_element(By.XPATH, "//label[@class='radio-inline']/input[@id= 'radio_program_none']").click()

    # Appointment date
    date_field = driver.find_element(By.ID, "txt_visit_date")
    action.click(date_field).send_keys("26-08-2024").perform()
    time.sleep(1)

    # comment area
    comment_area = driver.find_element(By.ID, "txt_comment")
    action.click(comment_area).send_keys("No healthcare program selected. Symptoms include headache and high fever. ").perform()

    # book button
    driver.find_element(By.ID, "btn-book-appointment").click()

    # Confirmation
    expected_text = 'Appointment Confirmation'
    confirmation_heading = driver.find_element(By.XPATH, "//h2[text()='Appointment Confirmation']")
    assert expected_text.__eq__(confirmation_heading.text)

    # display appointment summary
    booking_title = driver.find_element(By.XPATH,"//p[text()='Please be informed that your appointment has been booked as following:']")
    all_labels = driver.find_elements(By.XPATH, "//*[@class='col-xs-offset-2 col-xs-8']//div/label")
    all_para = driver.find_elements(By.XPATH, "//*[@class='col-xs-offset-2 col-xs-8']//div/p")

    # Ensure the lengths are the same to pair each label with its corresponding paragraph
    min_length = min(len(all_labels), len(all_para))

    print(confirmation_heading.text)
    print(booking_title.text)
    print("--------------------------------")
    # Print each label and its corresponding paragraph
    for label, para in zip(all_labels[:min_length], all_para[:min_length]):
        print(label.text + " ---> " + para.text)

    # Go to homepage
    driver.find_element(By.LINK_TEXT, "Go to Homepage").click()
    time.sleep(1)

    # Check history
    menu_button = driver.find_element(By.ID, "menu-toggle")
    wait = WebDriverWait(driver, 10)
    history_field = driver.find_element(By.XPATH, "//a[text()='History']")
    time.sleep(1)

    action.click(menu_button).move_to_element(history_field).click().perform()
    time.sleep(1)

    # screenshot of history of appointment
    driver.get_screenshot_as_file("screenshots\\Appointment-schedule.png")
    allure.attach(driver.get_screenshot_as_png(),name="Appointment-schedule",attachment_type=allure.attachment_type.PNG)
    driver.find_element(By.LINK_TEXT, "Go to Homepage").click()

    # Logout
    menu_button = driver.find_element(By.ID, "menu-toggle")
    wait = WebDriverWait(driver, 10)
    logout = driver.find_element(By.XPATH, "//a[text()='Logout']")
    action.click(menu_button).move_to_element(logout).click().perform()
    expected_h3 = 'We Care About Your Health'
    actual_h3 = driver.find_element(By.XPATH, "//h3").text
    assert expected_h3.__eq__(actual_h3)

