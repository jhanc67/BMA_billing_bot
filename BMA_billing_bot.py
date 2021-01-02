from selenium import webdriver

browser = webdriver.Chrome(executable_path="/Users/chirawathanchiew/desktop/my_projects/web_scraping/chromedriver")
browser.get("https://online.rezexpert.com/")

user_name = "joe hanchiew"
password = "Hanchiew12"

user_ele = browser.find_element_by_id("txtUserName")
user_ele.send_keys(user_name)

password_ele = browser.find_element_by_id("txtPassword")
password_ele.send_keys(password)
password_ele.submit()



browser.implicitly_wait(10)
admin = browser.find_element_by_xpath("//*[@id='mnuAdmin']")
admin.click()

browser.implicitly_wait(10)
per_bill = browser.find_element_by_xpath("/html/body/div[1]/div[1]/nav/div/div/h3[1]")
per_bill.click()

bill_type = browser.find_element_by_xpath("//*[@id='drawers-wrapper']/div[1]")
bill_type.click()

bma_type = browser.find_element_by_xpath("//*[@id='cboBillPolicyType']/option[2]")
bma_type.click()

browser.implicitly_wait(15)
into_bill = browser.find_element_by_xpath("//*[@id='tbActiveBillingPolicies']/tr[1]/td[1]")
into_bill.click()
