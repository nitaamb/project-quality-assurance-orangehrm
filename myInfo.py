from select import select
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class AddSkill(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/")
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi username
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        browser.find_element(By.ID,"btnLogin").click() # klik tombol login
        time.sleep(2)

    def test_a_success_add_skill(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu_pim_viewMyDetails").click() # klik menu my info
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/ul/li[10]/a").click() # klik qualifications
        browser.find_element(By.ID,"addSkill").click() # klik add skill
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[6]/div[2]/form/fieldset/ol/li[1]/select/option[2]").click() # select skill
        browser.find_element(By.NAME,"skill[years_of_exp]").send_keys("5") # isi year of experience
        browser.find_element(By.NAME,"skill[comments]").send_keys("HTML") # isi comments
        browser.find_element(By.ID,"btnSkillSave").click() # klik tombol save

        # validasi
        response_data = browser.find_element(By.XPATH,"//div[@id='tblSkill']/div[2]/div").text
        self.assertEqual('Successfully Saved', response_data)

    def test_b_failed_add_skill_with_all_empty_fields(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu_pim_viewMyDetails").click() # klik menu my info
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[1]/ul/li[10]/a").click() # klik qualifications
        browser.find_element(By.ID,"addSkill").click() # klik add skill
        browser.find_element(By.ID,"btnSkillSave").click() # klik tombol save

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[6]/div[2]/form/fieldset/ol/li[1]/span[1]").text
        self.assertEqual('Required', response_data)

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()