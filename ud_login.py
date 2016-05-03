from selenium import webdriver
import unittest,time,re

class login_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.water = time.sleep(5)
        self.base_url = "http://reocar.udesk20.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        self.water = time.sleep(5)
        driver.find_element_by_class_name("login").click()
        self.water = time.sleep(5)
        driver.find_element_by_id("user_email").send_keys("zhangs@udesk.cn")
        driver.find_element_by_id("user_password").send_keys("zs123456")
        driver.find_element_by_name("commit").click()
        self.water = time.sleep(30)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "main":
    unittest.main()



