from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

"""
Created by Mohamed Amine Guedria

Simple test automation for webpage using Selenium.

Selenium is an automated software that tests web applications. The Selenium framework 
is an amalgamation of various Selenium tools that automate the web application testing process. 
It reduces the time of testing cycles and saves money and resources.

Selenium WebDriver offers native bindings for JavaScript, Python, Java, C#, and Ruby.

how to execute the code:

open with an IDE and execute  
or in the terminal with the command "python automation.py -v". 
if the test passed, an "Ok" is printed, otherwise "FAILED".
"""


class Testprofilence(unittest.TestCase):

    def setUp(self):
        self.URL = "https://profilence.com/"
        self.TITLE = "Profilence Technical Quality Analysis"
        # configure webdriver manager
        self.driver = webdriver.Chrome(r"D:/Uni_Ulm/oulu/test/selenium driver/chromedriver.exe")
        self.driver.implicitly_wait(5)
        # launch URL
        self.driver.get(self.URL)

    def test_1_main_url(self):
        expected = self.URL
        self.driver.implicitly_wait(5)
        assert self.driver.current_url == expected, f"Error. Expected text:{expected}, " \
                                                    f"but actual text: {self.driver.current_url}"

    def test_2_title(self):
        expected = self.TITLE
        self.driver.implicitly_wait(5)
        assert self.driver.title == expected, f"Error. Expected text:{expected}, but actual text: {self.driver.title}"

    def test_3_url(self):
        self.driver.find_element(By.XPATH, "//*[@id='content']/div/article/section[2]/div/div[1]/div/a").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//*[@id='tabby-toggle_developers']").click()
        self.driver.implicitly_wait(5)
        assert "product" in self.driver.current_url

    def test_4_Wrong_email(self):
        self.driver.find_element(By.XPATH, "//*[@id='content']/div/article/section[8]/div/div/a").click()

        # Store iframe web element
        iframe = self.driver.find_element(By.XPATH, "//*[@id='hs-form-iframe-0']")
        # switch to selected iframe
        self.driver.switch_to.frame(iframe)

        email = self.driver.find_element(By.XPATH, "//*[@id='email-86ce5875-6792-4ff9-b92b-4a05c970cb56']")
        email.send_keys("test.me@mail.test")

        self.driver.find_element(By.CLASS_NAME, "actions").click()
        actual_output = self.driver.find_element(By.XPATH,
                                                 "//*[@id='hsForm_86ce5875-6792-4ff9-b92b-4a05c970cb56']"
                                                 "/div[1]/ul/li[1]/label").text

        expected_output = "Please enter a valid email address."
        assert actual_output == expected_output, f"Error. Expected text:{expected_output}, " \
                                                 f"but actual text: {actual_output}"

    def test_5_connect_us_empty(self):
        self.driver.find_element(By.XPATH, "//*[@id='content']/div/article/section[8]/div/div/a").click()
        self.driver.implicitly_wait(5)

        # Store iframe web element
        iframe = self.driver.find_element(By.XPATH, "//*[@id='hs-form-iframe-0']")
        # switch to selected iframe
        self.driver.switch_to.frame(iframe)

        self.driver.find_element(By.CLASS_NAME, "actions").click()
        self.driver.implicitly_wait(5)
        actual_output = self.driver.find_element(By.XPATH,
                                                 "//*[@id='hsForm_86ce5875-6792-4ff9-b92b-4a05c970cb56']"
                                                 "/div[6]/ul/li/label").text
        expected_output = "Please complete all required fields."
        assert actual_output == expected_output, f"Error. Expected text:{expected_output}, " \
                                                 f"but actual text: {actual_output}"

    def test_6_external_url(self):
        self.driver.find_element(By.XPATH, "/html/body/footer/div/div[2]/ul/li[2]/a").click()
        self.driver.implicitly_wait(10)
        expected_output = "https://www.linkedin.com/company/profilence/"
        assert self.driver.current_url == expected_output, f"Error. Expected text:{expected_output}," \
                                                           f" but actual text: {self.driver.current_url}"

    # Closing the browser.
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
