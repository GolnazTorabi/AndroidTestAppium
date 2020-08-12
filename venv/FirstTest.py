from appium import webdriver

desired_cap = {
    'platformName': 'Android',
    'deviceName': 'NE1GAM4792312176',
    'app': "/home/golnaz/Desktop/Vandar_0.1.0.apk"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
