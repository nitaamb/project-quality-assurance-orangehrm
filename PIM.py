from select import select
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class AddEmployee(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/")
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi username
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        browser.find_element(By.ID,"btnLogin").click() # klik tombol login
        time.sleep(2)

    def test_a_success_add_employee_without_create_login_details(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu_pim_viewPimModule").click() # klik menu PIM
        browser.find_element(By.ID,"menu_pim_addEmployee").click() # klik add employee
        browser.find_element(By.NAME,"firstName").send_keys("Michael") # isi first name
        browser.find_element(By.NAME,"middleName").send_keys("Jack") # isi middle name
        browser.find_element(By.NAME,"lastName").send_keys("Lee") # isi last name
        browser.find_element(By.NAME,"photofile").send_keys("D:\code\Final Project\P.jpg") # isi photo
        browser.find_element(By.ID,"btnSave").click() # klik tombol save

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div[1]/h1").text
        self.assertIn('Personal Details', response_data)

    def test_b_success_add_employee_with_create_login_details(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu_pim_viewPimModule").click() # klik menu PIM
        browser.find_element(By.ID,"menu_pim_addEmployee").click() # klik add employee
        browser.find_element(By.NAME,"firstName").send_keys("Michael") # isi first name
        browser.find_element(By.NAME,"middleName").send_keys("Jack") # isi middle name
        browser.find_element(By.NAME,"lastName").send_keys("Lee") # isi last name
        browser.find_element(By.NAME,"photofile").send_keys("D:\code\Final Project\P.jpg") # isi photo
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[4]/input").click() # klik checkbox
        browser.find_element(By.ID,"user_name").send_keys("Michael") # isi username
        browser.find_element(By.NAME,"user_password").send_keys("michael123") # isi password
        browser.find_element(By.NAME,"re_password").send_keys("michael123") # isi confirm password
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[8]/select/option[1]").click() # select status
        time.sleep(2)
        browser.find_element(By.ID,"btnSave").click() # klik tombol save

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div[1]/h1").text
        self.assertIn('Personal Details', response_data)

    def test_c_failed_add_employee_with_all_empty_fields(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu_pim_viewPimModule").click() # klik menu PIM
        browser.find_element(By.ID,"menu_pim_addEmployee").click() # klik add employee
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[4]/input").click() # klik checkbox
        browser.find_element(By.ID,"btnSave").click() # klik tombol save

        # validasi
        response_full_name = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/ol/li[1]/span").text
        response_last_name = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/ol/li[3]/span").text
        response_username = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[5]/span").text
        response_password = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[6]/span").text
            
        self.assertEqual('Required', response_full_name)
        self.assertEqual('Required', response_last_name)
        self.assertEqual('Should have at least 5 characters', response_username)
        self.assertEqual('Should have at least 8 characters', response_password)

    def test_d_failed_add_employee_with_employee_Id_already_used(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu_pim_viewPimModule").click() # klik menu PIM
        browser.find_element(By.ID,"menu_pim_addEmployee").click() # klik add employee
        browser.find_element(By.NAME,"firstName").send_keys("Michael") # isi first name
        browser.find_element(By.NAME,"middleName").send_keys("Jack") # isi middle name
        browser.find_element(By.NAME,"lastName").send_keys("Lee") # isi last name
        browser.find_element(By.NAME,"employeeId").send_keys(Keys.CONTROL, "a") # ctrl+a
        browser.find_element(By.NAME,"employeeId").send_keys(Keys.DELETE) # tekan delete
        browser.find_element(By.NAME,"employeeId").send_keys("1") # isi id employee
        browser.find_element(By.ID,"btnSave").click() # klik tombol save

        # validasi
        response_data = browser.find_element(By.XPATH,"//div[@id='addEmployeeTbl']/div").text
        self.assertEqual('Failed To Save: Employee Id Exists', response_data)

    def test_e_failed_add_employee_with_username_less_than_5_characters(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu_pim_viewPimModule").click() # klik menu PIM
        browser.find_element(By.ID,"menu_pim_addEmployee").click() # klik add employee
        browser.find_element(By.NAME,"firstName").send_keys("Michael") # isi first name
        browser.find_element(By.NAME,"middleName").send_keys("Jack") # isi middle name
        browser.find_element(By.NAME,"lastName").send_keys("Lee") # isi last name
        browser.find_element(By.NAME,"photofile").send_keys("D:\code\Final Project\P.jpg") # isi photo
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[4]/input").click() # klik checkbox
        browser.find_element(By.ID,"user_name").send_keys("Lee") # isi username
        browser.find_element(By.NAME,"user_password").send_keys("michael123") # isi password
        browser.find_element(By.NAME,"re_password").send_keys("michael123") # isi confirm password
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[8]/select/option[1]").click() # select status
        time.sleep(2)
        browser.find_element(By.ID,"btnSave").click() # klik tombol save

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[5]/span").text
        self.assertEqual('Should have at least 5 characters', response_data)

    def test_e_failed_add_employee_with_password_less_than_8_characters(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu_pim_viewPimModule").click() # klik menu PIM
        browser.find_element(By.ID,"menu_pim_addEmployee").click() # klik add employee
        browser.find_element(By.NAME,"firstName").send_keys("Michael") # isi first name
        browser.find_element(By.NAME,"middleName").send_keys("Jack") # isi middle name
        browser.find_element(By.NAME,"lastName").send_keys("Lee") # isi last name
        browser.find_element(By.NAME,"photofile").send_keys("D:\code\Final Project\P.jpg") # isi photo
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[4]/input").click() # klik checkbox
        browser.find_element(By.ID,"user_name").send_keys("Michael") # isi username
        browser.find_element(By.NAME,"user_password").send_keys("michael") # isi password
        browser.find_element(By.NAME,"re_password").send_keys("michael") # isi confirm password
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[8]/select/option[1]").click() # select status
        time.sleep(2)
        browser.find_element(By.ID,"btnSave").click() # klik tombol save

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[6]/span").text
        self.assertEqual('Should have at least 8 characters', response_data)

    def test_e_failed_add_employee_with_confirm_password_doesnt_match(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu_pim_viewPimModule").click() # klik menu PIM
        browser.find_element(By.ID,"menu_pim_addEmployee").click() # klik add employee
        browser.find_element(By.NAME,"firstName").send_keys("Michael") # isi first name
        browser.find_element(By.NAME,"middleName").send_keys("Jack") # isi middle name
        browser.find_element(By.NAME,"lastName").send_keys("Lee") # isi last name
        browser.find_element(By.NAME,"photofile").send_keys("D:\code\Final Project\P.jpg") # isi photo
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[4]/input").click() # klik checkbox
        browser.find_element(By.ID,"user_name").send_keys("Michael") # isi username
        browser.find_element(By.NAME,"user_password").send_keys("michael123") # isi password
        browser.find_element(By.NAME,"re_password").send_keys("michael1") # isi confirm password
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[8]/select/option[1]").click() # select status
        time.sleep(2)
        browser.find_element(By.ID,"btnSave").click() # klik tombol save

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[7]/span").text
        self.assertEqual('Passwords do not match', response_data)

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()