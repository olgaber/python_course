import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import elements


driver = webdriver.Chrome()
driver.get(elements.url)

# # Fill and submit form
el1 = driver.find_element(By.XPATH, elements.el1)
driver.execute_script("arguments[0].scrollIntoView()", el1)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(el1))
el1.click()

el2 = driver.find_element(By.XPATH, elements.el2)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(el2))
el2.click()

full_name = driver.find_element(By.ID, elements.full_name)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(full_name))

full_name.click()
full_name.send_keys(elements.full_name_txt)

email = driver.find_element(By.ID, elements.email)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(email))
email.click()
email.send_keys(elements.email_txt)

address1 = driver.find_element(By.ID, elements.address1)
address1.click()
address1.send_keys(elements.address1_txt)

address2 = driver.find_element(By.ID, elements.address2)
driver.execute_script("arguments[0].scrollIntoView()", address2)
address2.click()
address2.send_keys(elements.address2_txt)

submit = driver.find_element(By.XPATH, elements.submit)
submit.click()

output_name = driver.find_element(By.ID, elements.output_name)
print(type(output_name.text))
print(type(f"Name:{elements.full_name_txt}"))

print(output_name.text)
print(f"Name:{elements.full_name_txt}")

assert output_name == f"Name:{elements.full_name_txt}"

# Checkboxes

chb_m = driver.find_element(By.ID, elements.chb_m)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(chb_m))
chb_m.click()

shevron1 = driver.find_element(By.XPATH, elements.shevron1)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(shevron1))
shevron1.click()

shevron2 = driver.find_element(By.XPATH, elements.shevron2)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(shevron2))
shevron2.click()

shevron3 = driver.find_element(By.XPATH, elements.shevron3)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(shevron3))
shevron3.click()

private = driver.find_element(By.ID, elements.private)
WebDriverWait(driver, 50).until(EC.element_to_be_clickable(private))
driver.execute_script("arguments[0].scrollIntoView()", private)
private.click()

# Form

form_section = driver.find_element(By.XPATH, elements.forms_section)
driver.execute_script("arguments[0].scrollIntoView()", form_section)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(form_section))
form_section.click()

form_m = driver.find_element(By.XPATH, elements.form_m)
form_m.click()

first_name = driver.find_element(By.XPATH, elements.first_name)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(first_name))
first_name.click()
first_name.send_keys(elements.f_name)

last_name = driver.find_element(By.XPATH, elements.last_name)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(last_name))
last_name.click()
last_name.send_keys(elements.l_name)

email1 = driver.find_element(By.XPATH, elements.email1)
WebDriverWait(driver, 20).until(EC.element_to_be_clickable(email1))
email1.click()
email1.send_keys(elements.email1_adr)

gender = driver.find_element(By.XPATH, elements.gender)
WebDriverWait(driver, 100).until(EC.element_to_be_clickable(gender))
# driver.execute_script("arguments[0].click();", gender)
gender.click()

phone = driver.find_element(By.XPATH, elements.phone)
WebDriverWait(driver, 100).until(EC.element_to_be_clickable(phone))
phone.click()
phone.send_keys(elements.phone_num)

calendar = driver.find_element(By.XPATH, elements.calendar)
driver.execute_script("arguments[0].scrollIntoView()", calendar)
WebDriverWait(driver, 100).until(EC.element_to_be_clickable(calendar))
calendar.click()

month_select = driver.find_element(By.XPATH, elements.month_select)
m_select = Select(month_select)
m_select.select_by_index(4)

year_select = driver.find_element(By.XPATH, elements.year_select)
y_select = Select(year_select)
y_select.select_by_visible_text(elements.year)

date = driver.find_element(By.XPATH, elements.date)
date.click()

choose_btn = driver.find_element(By.XPATH, elements.choose_btn)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable(choose_btn))
# choose_btn.click()
driver.executeScript("arguments[0].click();", choose_btn)

time.sleep(5)

driver.quit()