from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import getpass
 


driver = webdriver.Firefox()
driver.get('https://www.facebook.com/')
print("facebook opened...")
sleep(2)
Email = raw_input("Enter your Email ID:")
email = driver.find_element_by_xpath("//input[@id='email' or @name='email']")
email.send_keys(Email)
print("Email Id entered...")
password1=getpass.getpass("Enter your Facebook password: ")
password = driver.find_element_by_xpath("//input[@id='pass']")
password.send_keys(password1)
print("Password entered...")
button = driver.find_element_by_xpath("//input[@value='Log In']")
button.click()
print("signed in")
sleep(5)
Account_Setting = driver.find_element_by_xpath("//a[@id='pageLoginAnchor']")
Account_Setting.send_keys(Keys.ENTER)
sleep(3)
Log_Out = driver.find_element_by_link_text("Log out")
Log_Out.click()
print("signed Out")
sleep(3)
driver.close()