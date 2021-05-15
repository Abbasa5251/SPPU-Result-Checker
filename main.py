from decouple import config
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from time import sleep

URL = config("URL")
MOTHER_NAME = config("MOTHER_NAME")
driver = webdriver.Firefox()
driver.get(url=URL)

try:
    for i in range(13100, 13500):
        sleep(3)
        seat_number_input = driver.find_element_by_id(
            "ctl00_ContentPlaceHolder1_txtSeatno")

        mothers_name_input = driver.find_element_by_id(
            "ctl00_ContentPlaceHolder1_txtMother")

        submit_btn = driver.find_element_by_id(
            "ctl00_ContentPlaceHolder1_btnSubmit")

        seat_number_input.clear()
        mothers_name_input.clear()
        mothers_name_input.send_keys(MOTHER_NAME)
        seat_number_input.send_keys(i)
        submit_btn.click()
        a = Alert(driver)
        a.dismiss()

except Exception as e:
    sleep(5)
    print("Result Found")
    print(f"Seat Number: {i}")
    print(driver.find_element_by_xpath(
        "/html/body/form/div[5]/div[2]/span/div/table[1]/tbody/tr[2]/td[1]").text)
    print(driver.find_element_by_xpath(
        "/html/body/form/div[5]/div[2]/span/div/table[3]/tbody/tr[28]/td[1]").text.strip())

finally:
    driver.close()
