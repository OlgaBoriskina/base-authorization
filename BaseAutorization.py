from selenium import webdriver
import unittest

username = 'aerobatic'
password = 'aerobatic'


class Test (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("chromedriver.exe")
        self.base_url = "auth-demo.aerobatic.io/protected-standard/"
        self.driver.get('https://' + username + ':' + password + '@' + self.base_url)

    def test_base(self):
        assert self.driver.find_element_by_xpath("//a[contains(@href, '/')]").is_displayed()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()