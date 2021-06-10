from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("https://debrid-link.com/webapp/seedbox")
usernames = ["uc1234"]
password = "asdf1234"
magnet = "magnet:?xt=urn:btih:"

usernameTextbox = driver.find_element_by_xpath('//*[@id="cont"]/div[2]/div/div/div/div/form/div[1]/input')
usernameTextbox.send_keys(usernames[1])

passwordBox = driver.find_element_by_xpath('//*[@id="cont"]/div[2]/div/div/div/div/form/div[2]/input')
passwordBox.send_keys(password)

loginButton = driver.find_element_by_xpath('//*[@id="cont"]/div[2]/div/div/div/div/form/div[3]/button')
loginButton.click()

sleep(10)

magnetLinkBox = driver.find_element_by_xpath('//*[@id="cont"]/div[2]/div/div[1]/div[3]/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/input')

while True:
	magnetLinkBox.send_keys(magnet)
	sleep(5)

	try:
		upgradeAccountError = driver.find_element_by_xpath('//*[@id="cont"]/div[2]/div/div[1]/div[3]/div[3]/div[3]')
		overloadedError = driver.find_element_by_xpath('//*[@id="cont"]/div[2]/div/div[1]/div[3]/div[3]/div[2]/div[2]')
	except:
		break
	
	reset = driver.find_element_by_xpath('//*[@id="cont"]/div[2]/div/div[1]/div[3]/div[2]/div[2]/div/div[2]/button')
	reset.click()
