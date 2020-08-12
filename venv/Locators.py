from appium import webdriver

desired_cap = {
    'platformName': 'Android',
    'deviceName': 'NE1GAM4792312176',
    'app': "/home/golnaz/Desktop/Vandar_0.1.0.apk"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

# next button clicked
driver.find_element_by_id("io.vandar.app:id/text_next_page").click()
driver.find_element_by_id("io.vandar.app:id/text_next_page").click()
driver.find_element_by_id("io.vandar.app:id/text_next_page").click()

login_element = driver.find_element_by_xpath(
    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/android.view.ViewGroup/android.widget.EditText")
login_element.send_keys("09163513306")
button_login = driver.find_element_by_id("io.vandar.app:id/next_button").click()
