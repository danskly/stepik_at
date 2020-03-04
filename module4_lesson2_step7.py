#module4_lesson2_step5.py
from selenium import webdriver
import time
import math

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute('valuex')
    y = calc(x)

    y_element = browser.find_element_by_id("answer")
    y_element.send_keys(y)

    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()

    option1 = browser.find_element_by_id("robotsRule")
    option1.click()

    sbmt_element = browser.find_element_by_css_selector("[type = 'submit']")
    sbmt_element.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

#
