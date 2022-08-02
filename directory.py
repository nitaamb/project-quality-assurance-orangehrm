from select import select
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class SearchDirectory(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/")
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi username
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        browser.find_element(By.ID,"btnLogin").click() # klik tombol login
        time.sleep(2)

    def test_a_success_verify_existing_value_in_database(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu_directory_viewDirectory").click() # klik menu directory
        browser.find_element(By.NAME,"searchDirectory[emp_name][empName]").send_keys("Aaliyah Haq") # isi name
        time.sleep(1)
        browser.find_element(By.NAME,"searchDirectory[emp_name][empName]").send_keys(Keys.ENTER) # tekan enter
        browser.find_element(By.ID,"searchBtn").click() # klik search
        time.sleep(3)

        #validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/table/tbody/tr[2]/td[2]/ul/li[1]/b").text
        self.assertEqual('Aaliyah Haq', response_data)

    def test_b_success_verify_non_existing_value_in_database(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu_directory_viewDirectory").click() # klik menu directory
        browser.find_element(By.NAME,"searchDirectory[emp_name][empName]").send_keys("nita") # isi name
        browser.find_element(By.ID,"searchBtn").click() # klik search
        time.sleep(3)

        #validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]").text
        self.assertEqual('No Records Found', response_data)

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()