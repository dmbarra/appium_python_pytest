import os
import pytest

from selenium.webdriver.common.keys import Keys
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
APPIUM_LOCAL_HOST_URL = 'http://localhost:4723/wd/hub'
PLATFORM_VERSION = '6.0'


class TestWebViewAndroid:
    @pytest.fixture(scope="function")
    def driver(self, request):
        desired_caps = {
            'platformName': 'Android',
            'platformVersion': PLATFORM_VERSION,
            'deviceName': 'Android Emulator',
            'app': PATH('C:\\Users\\dbarra\\Documents\\Android\\rw.apk')
        }
        driver = webdriver.Remote(APPIUM_LOCAL_HOST_URL, desired_caps)

        def fin():
            driver.quit()

        request.addfinalizer(fin)
        return driver  # provide the fixture value

    def test_create_user(self, driver):
        driver.find_element_by_id("action_bar_root").click()
        driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]").click()
        TouchAction(driver).press(x=422, y=376).move_to(x=-358, y=3).release().perform()
        TouchAction(driver).press(x=422, y=376).move_to(x=-358, y=3).release().perform()
        driver.find_element_by_id("btLogin").click()
        driver.find_element_by_id("btLogin").click()

        name = driver.find_element_by_id("etName")
        name.send_keys("Barra")

        # driver.find_element_by_id("br.com.zup.rwwhitelabel:id/etDocument").send_keys("29878194477")
        # driver.execute_script("mobile: scroll", {"direction": "down", element: element.getAttribute("id")})

        # document = driver.find_element_by_id("etDocument")
        # driver.scroll(document)
        # document.send_keys("0000000000000")
        #
        # driver.find_element_by_id("etEmail").send_keys("sos@sos.org")
        # driver.find_element_by_id("etPassword").send_keys("12345678")
        # driver.find_element_by_id("btCreateAccount").click()
        #
        # alert = driver.switch_to_alert()
        #
        # no way to handle alerts in Android
        # driver.find_element_by_android_uiautomator('new UiSelector().clickable(true)').click()

