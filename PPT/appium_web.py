# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
#adb shell dumpsys window windows | grep -E 'mCurrentFocus|mFocusedApp'
#appium --allow-insecure chromedriver_autodownload

import time
from appium import webdriver

caps = {}
caps["appium:platformName"] = "Android"
caps["appium:platformVersion"] = "10"
caps["appium:deviceName"] = "Nokia"
caps["appium:automationName"] = "UIAutomator2"
caps["appium:udid"] = "J0AA002437J82602777"
caps["appium:noReset"] = True
caps["browserName"] = "Chrome"
caps["appium:newCommandTimeout"] = 0
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.implicitly_wait(5)

print(driver.current_context)
driver.get("https://www.google.com")
search_field_el = driver.find_element_by_xpath('//input[@type="search"]')
search_field_el.send_keys("MSBC\n")



