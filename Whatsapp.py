# Whatsapp Message - Python Script
# https://www.youtube.com/watch?v=5hr0IdVM7Qg  - Reference Url

# Step 1
# For ChromeDriver download it from this website
# https://chromedriver.storage.googleapis.com/index.html?path=2.35/
# unzip the folder it must contain the chromedriver.exe

# Step 2
# Install Selenium python pacakage
# Use the below command in cmd C:/Python27/
# pip install selenium --proxy approxy.rockwellcollins.com:9090

# Step 3
# Import WebDriver from Selenium
# create a chrome driver and add the path of user chromedriver to 
#   Chrome(r'C:\Users\smeda\Downloads\Logs\audio\chromedriver_win32/chromedriver')

# Step 4
# Get the name of the user as available in the Whatsapp saved contacts directory
# Get the message
# get the count, number of times u wanna send the message

# Step 5
# Open the Whatsapp web and scan the QR Code
# Inspect the web page and identidy the user Name -> Click the user name (using driver/Selenium)
# Inspect the web page and identidy the text Container(Message box) -> Enter the text using send_keys method (using driver/Selenium)
# Inspect the web page and identidy the send button class -> Click the button(using driver/Selenium)


# Step 2
from selenium import webdriver
import time

# Step 3
driver = webdriver.Chrome(r'C:\Users\smeda\Downloads\Logs\audio\chromedriver_win32/chromedriver')
driver.get('https://web.whatsapp.com/')

# Step 4
name = raw_input('Enter the name of user or group: ')
msg = raw_input('Enter your message: ')
# count = int(raw_input('Enter Count: '))

raw_input('Open Whatsapp web, scan the QR Code and then hit enter')

# Step 5
# Locate the User Name from the Whatsapp web and click it
# user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
# user.click()

# Now locate the Entry filed, enter message

# msg_box = driver.find_element_by_class_name('_2bXVy')


# Code to send message based on the count
for i in range(count):
	msg_box.send_keys(msg)
	# Now locate the Send button and click it
	button	= driver.find_element_by_class_name('_2lkdt') # These Classes are tend to change
  # Inspect the WEbpage and then use it
	button.click()


"""
def search_user():
  search_bar = driver.find_element_by_class_name("_2MSJr"); # The Search Box Class
  search_bar.send_keys(name)
  time.sleep(0.5)
  user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
  user.click()
  time.sleep(1.0)
  msg_box = driver.find_element_by_class_name('_2bXVy')
  msg_box.send_keys(msg)
  button	= driver.find_element_by_class_name('_2lkdt')
  button.click()
  
search_user()
"""
