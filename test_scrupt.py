from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Replace 'path_to_brave_executable' with the actual path to your Brave browser executable (brave.exe)
brave_path = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'

# Set the options to open Brave with Selenium WebDriver
options = webdriver.ChromeOptions()
options.binary_location = brave_path

# Create the WebDriver instance for Brave
driver = webdriver.Chrome(options=options)

# Navigate to saucedemo login page
driver.get('https://www.saucedemo.com')

# Find the login elements and fill in the credentials
username_input = driver.find_element('id', 'user-name')
password_input = driver.find_element('id', 'password')
login_button = driver.find_element('id', 'login-button')

username_input.send_keys('standard_user')  # Replace with your username
password_input.send_keys('secret_sauce')  # Replace with your password
login_button.click()

# Wait for the login process to complete (you may need to add an explicit wait here)

# Verify if the login was successful (this is just a basic check)
if "inventory.html" in driver.current_url:
    print("Login successful!")
else:
    print("Login failed.")

# Close the browser when done
driver.quit()
