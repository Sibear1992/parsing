import gspread
from oauth2client.service_account import ServiceAccountCredentials
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pprint

# # use creds to create a client to interact with the Google Drive API
# scope = ['https://www.googleapis.com/auth/drive']
# creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
# client = gspread.authorize(creds)
#
# # Find a workbook by name and open the first sheet
# # Make sure you use the right name here.
# sht = client.open("AllylBalance")
# sheet = sht.worksheet('Исходные_данные')
#
# pp = pprint.PrettyPrinter()
# # Extract and print all of the values
# result = sheet.cell(8,8).value
# pp.pprint(result)

driver = webdriver.Chrome()
driver.get("http://lab.lpcma.tsu.ru")

elem_id = driver.find_element_by_id("edit-name")
elem_id.send_keys("sqwi@bk.ru")
elem_pas = driver.find_element_by_id("edit-pass")
elem_pas.send_keys("IloveTSU")
elem_submit = driver.find_element_by_id("edit-submit")
elem_submit.click()
elem_zaia = driver.find_elements_by_class_name("sf-depth-1")
elem_zaia.click()


# driver.close()