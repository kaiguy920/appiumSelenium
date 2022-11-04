from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'IOS'
desired_caps['platformVersion'] = '16.1'
desired_caps['deviceName'] = 'iPhone 14 Pro'
desired_caps['automationName'] = 'XCUITest'
desired_caps['app'] = ('/Users/ksma/Documents/VSCode-Projects/UIKitCatalog.app')

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)