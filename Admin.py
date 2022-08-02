from select import select
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class AddUser(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/")
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi username
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        browser.find_element(By.ID,"btnLogin").click() # klik tombol login
        time.sleep(2)

    def test_a_success_add_user(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu_admin_viewAdminModule").click() # klik menu admin
        browser.find_element(By.ID,"menu_admin_UserManagement").click() # klik user management
        time.sleep(2)
        browser.find_element(By.ID,"menu_admin_viewSystemUsers").click() # klik users
        browser.find_element(By.NAME,"btnAdd").click() # klik add
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/select/option[1]").click() # select user role
        time.sleep(3) 
        browser.find_element(By.ID,"systemUser_employeeName_empName").send_keys("Jadine Jackie") # isi employee name
        browser.find_element(By.XPATH,"//strong[contains(.,'Jadine Jackie')]").click() # klik
        time.sleep(3)
        browser.find_element(By.NAME,"systemUser[userName]").send_keys("ImJadinee") # isi username
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[4]/select/option[1]").click() # select status
        time.sleep(3) 
        browser.find_element(By.NAME,"systemUser[password]").send_keys("jadine123") # isi password
        browser.find_element(By.NAME,"systemUser[confirmPassword]").send_keys("jadine123") # isi confirm password
        browser.find_element(By.ID,"btnSave").click() # klik save
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.XPATH,"//form[@id='frmList_ohrmListComponent']/div[2]").text
        self.assertEqual('Successfully Saved', response_data)
    
    def test_b_failed_add_user_with_all_empty_fields(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu_admin_viewAdminModule").click() # klik menu admin
        browser.find_element(By.ID,"menu_admin_UserManagement").click() # klik user management
        time.sleep(2)
        browser.find_element(By.ID,"menu_admin_viewSystemUsers").click() # klik users
        browser.find_element(By.NAME,"btnAdd").click() # klik add
        browser.find_element(By.ID,"systemUser_employeeName_empName").send_keys("") # isi employee name
        browser.find_element(By.NAME,"systemUser[userName]").send_keys("") # isi username
        browser.find_element(By.NAME,"systemUser[password]").send_keys("") # isi password
        browser.find_element(By.NAME,"systemUser[confirmPassword]").send_keys("") # isi confirm password
        browser.find_element(By.ID,"btnSave").click() # klik save
        time.sleep(3)

        # validasi
        response_employee_name = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[2]/span").text
        response_username = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[3]/span").text
            
        self.assertEqual('Required', response_employee_name)
        self.assertEqual('Required', response_username)

    def test_c_failed_add_user_with_employee_name_doesnt_exist_in_database(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu_admin_viewAdminModule").click() # klik menu admin
        browser.find_element(By.ID,"menu_admin_UserManagement").click() # klik user management
        time.sleep(2)
        browser.find_element(By.ID,"menu_admin_viewSystemUsers").click() # klik users
        browser.find_element(By.NAME,"btnAdd").click() # klik add
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/select/option[1]").click() # select user role
        time.sleep(3)
        browser.find_element(By.ID,"systemUser_employeeName_empName").send_keys("Nita") # isi employee name
        browser.find_element(By.NAME,"systemUser[userName]").send_keys("ImNita") # isi username
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[4]/select/option[1]").click() # select status
        time.sleep(3)
        browser.find_element(By.NAME,"systemUser[password]").send_keys("nitaa123") # isi password
        browser.find_element(By.NAME,"systemUser[confirmPassword]").send_keys("nitaa123") # isi confirm password
        browser.find_element(By.ID,"btnSave").click() # klik save
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[2]/span").text
        self.assertEqual('Employee does not exist', response_data)

    def test_d_failed_add_user_with_username_less_than_5_characters(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu_admin_viewAdminModule").click() # klik menu admin
        browser.find_element(By.ID,"menu_admin_UserManagement").click() # klik user management
        time.sleep(2)
        browser.find_element(By.ID,"menu_admin_viewSystemUsers").click() # klik users
        browser.find_element(By.NAME,"btnAdd").click() # klik add
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/select/option[1]").click() # select user role
        time.sleep(3)
        browser.find_element(By.ID,"systemUser_employeeName_empName").send_keys("Jadine Jackie") # isi employee name
        browser.find_element(By.XPATH,"//strong[contains(.,'Jadine Jackie')]").click() # klik
        time.sleep(3)
        browser.find_element(By.NAME,"systemUser[userName]").send_keys("Jadi") # isi username
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[4]/select/option[1]").click() # select status
        time.sleep(3)
        browser.find_element(By.NAME,"systemUser[password]").send_keys("jadine123") # isi password
        browser.find_element(By.NAME,"systemUser[confirmPassword]").send_keys("jadine123") # isi confirm password
        browser.find_element(By.ID,"btnSave").click() # klik save
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[3]/span").text
        self.assertEqual('Should have at least 5 characters', response_data)

    def test_e_failed_add_user_with_password_less_than_8_characters(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu_admin_viewAdminModule").click() # klik menu admin
        browser.find_element(By.ID,"menu_admin_UserManagement").click() # klik user management
        time.sleep(2)
        browser.find_element(By.ID,"menu_admin_viewSystemUsers").click() # klik users
        browser.find_element(By.NAME,"btnAdd").click() # klik add
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/select/option[1]").click() # select user role
        time.sleep(3)
        browser.find_element(By.ID,"systemUser_employeeName_empName").send_keys("Jadine Jackie") # isi employee name
        browser.find_element(By.XPATH,"//strong[contains(.,'Jadine Jackie')]").click() # klik
        time.sleep(3)
        browser.find_element(By.NAME,"systemUser[userName]").send_keys("Jaadine") # isi username
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[4]/select/option[1]").click() # select status
        time.sleep(3)
        browser.find_element(By.NAME,"systemUser[password]").send_keys("jadine") # isi password
        browser.find_element(By.NAME,"systemUser[confirmPassword]").send_keys("jadine") # isi confirm password
        browser.find_element(By.ID,"btnSave").click() # klik save
        time.sleep(3)

        # validasi
        response_password = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[6]/span").text
        response_confirm_password = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[7]/span").text
            
        self.assertEqual('Should have at least 8 characters', response_password)
        self.assertEqual('Please enter at least 8 characters.', response_confirm_password)

    def test_f_failed_add_user_with_confirm_password_doesnt_match(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu_admin_viewAdminModule").click() # klik menu admin
        browser.find_element(By.ID,"menu_admin_UserManagement").click() # klik user management
        time.sleep(2)
        browser.find_element(By.ID,"menu_admin_viewSystemUsers").click() # klik users
        browser.find_element(By.NAME,"btnAdd").click() # klik add
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/select/option[1]").click() # select user role
        time.sleep(3)
        browser.find_element(By.ID,"systemUser_employeeName_empName").send_keys("Jadine Jackie") # isi employee name
        browser.find_element(By.XPATH,"//strong[contains(.,'Jadine Jackie')]").click() # klik
        time.sleep(3)
        browser.find_element(By.NAME,"systemUser[userName]").send_keys("ImJackie") # isi username
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[4]/select/option[1]").click() # select status
        time.sleep(3)
        browser.find_element(By.NAME,"systemUser[password]").send_keys("jadine123") # isi password
        browser.find_element(By.NAME,"systemUser[confirmPassword]").send_keys("jadine12") # isi confirm password
        browser.find_element(By.ID,"btnSave").click() # klik save
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[7]/span").text
        self.assertEqual('Passwords do not match', response_data)

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()