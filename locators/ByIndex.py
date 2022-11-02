from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


# Desired Capabilities
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel3XL'
desired_caps['app'] = '/Users/ksma/Downloads/Android_Demo_App.apk'
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'


# Webdriver object
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

# Action on the app
ele_index = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(4)")
ele_index.click()
