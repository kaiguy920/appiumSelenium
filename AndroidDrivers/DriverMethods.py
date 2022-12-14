from appium import  webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '10'
desired_caps['deviceName'] = 'Pixel'
desired_caps['app'] = ('/Users/ksma/Downloads/Android_Demo_App.apk')
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver =webdriver.Remote("http://127.0.0.1:4723/wd/hub",desired_caps)

print("Current Activity ==>",driver.current_activity)
print("Current Package ==>",driver.current_package)
print("Current context ==>",driver.current_context)
print("Current orientation ==>",driver.orientation)
print("Check Whether device is locked or not ==>",driver.is_locked())