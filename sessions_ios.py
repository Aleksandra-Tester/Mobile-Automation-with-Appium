from appium import webdriver
from os import path

CUR_Dir = path.dirname(path.abspath(__file__))
APP = path.join(CUR_DIR, 'TheApp.app.zip')
APPIUM = 'http://localhost:4723'

CAPS = {
    'platformName': 'iOS'
    'platformVersion': '13.6'
    'deviceName': 'iPhone11',
    'automtionName': 'XCUITest'
    'app' : APP,
}

driver = webdriver.Remote(
    command_executor=APPIUM,
    desired_capabilities=CAPS
)
driver.quit()