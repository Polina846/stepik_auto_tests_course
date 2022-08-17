import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
from selenium.webdriver.support.ui import Select

def sum(x, y):
  return str(str(int(x)+int(y)))
link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element(By.ID, "num1")
    x = int(x_element.text)
    y_element = browser.find_element(By.ID, "num2")
    y = int(y_element.text)
    c = sum(x, y)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(c)) 
    
    
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла