from select import select
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class ShowTimesheet(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/")
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi username
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        browser.find_element(By.ID,"btnLogin").click() # klik tombol login
        time.sleep(2)

    def test_a_success_show_timesheet(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu_dashboard_index").click() # klik menu dashboard
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div[1]/div/div/div/fieldset/div/div/table/tbody/tr/td[6]/div/a/span").click() # klik my timesheets

        # validasi
        expected_current_url = "https://opensource-demo.orangehrmlive.com/index.php/time/viewMyTimesheet"
        self.assertEqual(expected_current_url, browser.current_url)

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()