from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.maximize_window()
location = " Path to Prompt_Alert.HTML>"
driver.get(location)
button = driver.find_element_by_name('continue')
button.click()
obj = driver.switch_to.alert

time.sleep(2)

 
obj.send_keys('Meenakshi')

time.sleep(2)

obj.accept()
message=obj.text
print ("Alert shows following message: "+ message )

time.sleep(2)

obj.accept()
txt = driver.find_element_by_id('msg')
print(txt.text)

driver.close