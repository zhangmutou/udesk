from selenium import webdriver
import unittest, time


class Auto_test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.water = time.sleep(3)
        self.base_url = "http://reocar.tiyanudesk.com"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        self.water = time.sleep(5)
        driver.find_element_by_class_name("login").click()
        self.water = time.sleep(2)
        driver.find_element_by_id("user_email").send_keys("zhangs@udesk.cn")
        driver.find_element_by_id("user_password").send_keys("zs123456")
        driver.find_element_by_name("commit").click()
        self.water = time.sleep(30)
        driver.find_element_by_css_selector(".nav .fa-tasks").click()
        self.water = time.sleep(20)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/nav/dl/dd/a[2]").click()
        self.water = time.sleep(5)
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/div[1]/h3/div/a").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
