from selenium.webdriver.common.by import By
import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_find_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_element(By.XPATH, "//*[@id='add_to_basket_form']/button")