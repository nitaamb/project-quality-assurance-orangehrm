from select import select
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class CheckEmployeeLeaveEntitlements(unittest.TestCase): 

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
        browser.find_element(By.ID,"menu_leave_viewLeaveModule").click() # klik menu leave
        browser.find_element(By.ID,"menu_leave_Entitlements").click() # klik entitlements
        browser.find_element(By.ID,"menu_leave_viewLeaveEntitlements").click() # klik employee entitlements
        time.sleep(1)
        browser.find_element(By.ID,"entitlements_employee_empName").send_keys("Aaliyah Haq") # isi employee name
        time.sleep(1)
        browser.find_element(By.ID,"entitlements_employee_empName").send_keys(Keys.ENTER) # tekan enter
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[2]/select/option[1]").click() # select leave type
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[3]/select/option[1]").click() # select leave period
        browser.find_element(By.ID,"searchBtn").click() # klik search
        time.sleep(3)

        #validasi
        response_data = browser.find_element(By.XPATH,"//table[@id='resultTable']/tfoot/tr/td[2]").text
        self.assertIn('Total', response_data)
    
    def test_b_success_verify_non_existing_value_in_database(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu_leave_viewLeaveModule").click() # klik menu leave
        browser.find_element(By.ID,"menu_leave_Entitlements").click() # klik entitlements
        browser.find_element(By.ID,"menu_leave_viewLeaveEntitlements").click() # klik employee entitlements
        time.sleep(1)
        browser.find_element(By.ID,"entitlements_employee_empName").send_keys("Aaliyah Haq") # isi employee name
        time.sleep(1)
        browser.find_element(By.ID,"entitlements_employee_empName").send_keys(Keys.ENTER) # tekan enter
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[2]/select/option[1]").click() # select leave type
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[3]/select/option[3]").click() # select leave period
        browser.find_element(By.ID,"searchBtn").click() # klik search
        time.sleep(3)

        #validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/form/div[4]/table/tbody/tr/td").text
        self.assertEqual('No Records Found', response_data)

    def test_c_failed_with_empty_employee_field(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu_leave_viewLeaveModule").click() # klik menu leave
        browser.find_element(By.ID,"menu_leave_Entitlements").click() # klik entitlements
        browser.find_element(By.ID,"menu_leave_viewLeaveEntitlements").click() # klik employee entitlements
        time.sleep(1)
        browser.find_element(By.ID,"entitlements_employee_empName").send_keys("") # isi employee name
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[2]/select/option[1]").click() # select leave type
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[3]/select/option[3]").click() # select leave period
        browser.find_element(By.ID,"searchBtn").click() # klik search

        #validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[1]/span").text
        self.assertEqual('Required', response_data)


    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()