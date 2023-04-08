import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# Create a Service object
chrome_service = Service(executable_path=".\\lib\\chromedriver.exe")

# Create a webdriver instance for Chrome
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Send text to the chat
textarea = driver.find_element(by=By.TAG_NAME, value="textarea")
textarea.send_keys("Send me friendly greeting in 100 words or less")
textarea.send_keys(Keys.RETURN)

print("waiting for output")
time.sleep(0.5)

# find the div element with class "flex flex-col items-center text-sm dark:bg-gray-800"
div_element = driver.find_element(by=By.CSS_SELECTOR, value="div.flex.flex-col.items-center.text-sm.dark\:bg-gray-800")

# find the last div element inside the div_element
inner_divs = div_element.find_elements(by=By.CSS_SELECTOR, value="div:first-child")

last_text_div_element = inner_divs[-2]
last_response_button_element = inner_divs[-1]
child_elements = last_response_button_element.find_elements(by=By.CSS_SELECTOR, value="*")

# Wait until the buttons appear which mean the text is completed
found_button = False
while not found_button:
    try:
        # p_element = last_text_div_element.find_element(by=By.CSS_SELECTOR, value="p")
        style = last_response_button_element.get_attribute('class')
        if "invisible" in style:
            raise Exception("Button is invisible")

        found_button = True
    except Exception as e:
        print("Awaiting response...")
        time.sleep(0.5)

# get the text the last div which is our response
text = last_text_div_element.text
print(text)
# idx = text.find("{")
# text = text[idx:]
# print("Json: \n" + text)

