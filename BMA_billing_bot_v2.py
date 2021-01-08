from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time 


browser = webdriver.Chrome(executable_path="/Users/chirawathanchiew/desktop/my_projects/chromedriver")
browser.get("https://online.rezexpert.com/")


user_name = "joe hanchiew"
password = "Hanchiew12"

user_ele = browser.find_element_by_id("txtUserName")
user_ele.send_keys(user_name)

password_ele = browser.find_element_by_id("txtPassword")
password_ele.send_keys(password)
password_ele.submit()


wait = lambda time: browser.implicitly_wait(time) # second

slow = lambda second: time.sleep(second) # second

def page_load(second, ele_id):

	loaded = WebDriverWait(browser, second).until(EC.presence_of_element_located((By.ID, f"{ele_id}")))
	return loaded



try:

	page_load(120, "tblGridbody")

	slow(2)

	wait(10) 

	grid_ele = browser.find_element_by_xpath("//*[@id='tblGridbody']/tbody/tr[3]/td[5]").click()

	slow(2)

	wait(10)

	admin_button = browser.find_element_by_xpath("//*[@id='mnuAdmin']").click()

except TimeoutException: 

	print("Loading Took Too Long")



try : 

	page_load(120, "wrapper")

	slow(2)

	wait(10)

	perio_bil_drop = browser.find_element_by_xpath("//*[@id='drawers-wrapper']/h3[1]").click()

	slow(2)

	wait(10)

	bill_setup = browser.find_element_by_xpath("//*[@id='drawers-wrapper']/div[1]/ul/li[1]/a").click()

except TimeoutException: 

	print("Loading Took Too Long")



try:

	page_load(120, "wrapper")

	slow(2)

	wait(10)

	billing_type = browser.find_element_by_xpath("//*[@id='cboBillPolicyType']").click()

	slow(2)

	wait(10)

	bma_type = browser.find_element_by_xpath("//*[@id='cboBillPolicyType']/option[2]").click()

	slow(2)

	wait(10)

	activte_billing_body = browser.find_element_by_xpath("//*[@id='tblActiveBillingPolicies']").click()

	slow(2)

	wait(10)

	first_billing = browser.find_element_by_xpath("//*[@id='tbActiveBillingPolicies']/tr[1]").click()

	slow(2)

	wait(10)

	edit_button = browser.find_element_by_xpath("//*[@id='btnCancel0']").click()

except TimeoutException: 

	print("Loading Took Too Long")



