from select import select
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestUpdateStatus(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/")
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi username
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        browser.find_element(By.ID,"btnLogin").click() # klik tombol login
        time.sleep(2)

    def test_a_success_update_status(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu_buzz_viewBuzz").click() # klik menu buzz
        browser.find_element(By.ID,"status-tab-label").click() # klik update status
        browser.find_element(By.ID,"createPost_content").send_keys("Have a great day") # tulis status
        browser.find_element(By.ID,"postSubmitBtn").click() # klik post
        time.sleep(3)

        #validasi
        response_data = browser.find_element(By.ID,"postContent_17").text
        self.assertEqual('Have a great day', response_data)

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()