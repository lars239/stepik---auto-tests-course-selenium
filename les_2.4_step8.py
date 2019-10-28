from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time, math


def clac(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    button_book = browser.find_element_by_id("book")
    prise = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "100")
            )
    button_book.click()

    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    answer = clac(x)

    inpute_answer = browser.find_element_by_id("answer")
    inpute_answer.send_keys(answer)

    button_submit = browser.find_element_by_css_selector("button#solve")
    button_submit.click()


finally:
    time.sleep(10)
    browser.quit()
