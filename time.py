from select import select
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class AddCustomer(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/")
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi username
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        browser.find_element(By.ID,"btnLogin").click() # klik tombol login
        time.sleep(2)
    
    def test_a_success_add_customer(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu_time_viewTimeModule").click() # klik menu time
        browser.find_element(By.ID,"menu_admin_ProjectInfo").click() # klik project info
        browser.find_element(By.ID,"menu_admin_viewCustomers").click() # klik customers
        browser.find_element(By.ID,"btnAdd").click() # klik add
        browser.find_element(By.NAME,"addCustomer[customerName]").send_keys("IT Tech") # isi customer name
        browser.find_element(By.NAME,"addCustomer[description]").send_keys("Information technology (IT) consulting services") # isi deskripsi
        browser.find_element(By.ID,"btnSave").click() # klik tombol save

        # validasi
        response_data = browser.find_element(By.XPATH,"//form[@id='frmList_ohrmListComponent']/div[2]").text
        self.assertEqual('Successfully Saved', response_data)

    def test_b_failed_add_customer_with_all_empty_fields(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu_time_viewTimeModule").click() # klik menu time
        browser.find_element(By.ID,"menu_admin_ProjectInfo").click() # klik project info
        browser.find_element(By.ID,"menu_admin_viewCustomers").click() # klik customers
        browser.find_element(By.ID,"btnAdd").click() # klik add
        browser.find_element(By.NAME,"addCustomer[customerName]").send_keys("") # isi customer name
        browser.find_element(By.NAME,"addCustomer[description]").send_keys("") # isi deskripsi
        browser.find_element(By.ID,"btnSave").click() # klik tombol save

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[1]/span").text
        self.assertEqual('Required', response_data)

    def test_c_failed_add_customer_with_registered_customer(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu_time_viewTimeModule").click() # klik menu time
        browser.find_element(By.ID,"menu_admin_ProjectInfo").click() # klik project info
        browser.find_element(By.ID,"menu_admin_viewCustomers").click() # klik customers
        browser.find_element(By.ID,"btnAdd").click() # klik add
        browser.find_element(By.NAME,"addCustomer[customerName]").send_keys("IT Tech") # isi customer name
        browser.find_element(By.NAME,"addCustomer[description]").send_keys("Information technology (IT) consulting services") # isi deskripsi
        browser.find_element(By.ID,"btnSave").click() # klik tombol save

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[1]/span").text
        self.assertEqual('Already exists', response_data)

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()