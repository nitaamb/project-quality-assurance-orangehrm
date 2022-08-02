from select import select
import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class AddJobVacancy(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/")
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi username
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        browser.find_element(By.ID,"btnLogin").click() # klik tombol login
        time.sleep(2)

    def test_a_success_add_job_vacancy(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu_recruitment_viewRecruitmentModule").click() # klik menu recruitment
        browser.find_element(By.ID,"menu_recruitment_viewJobVacancy").click() # klik vacancies
        browser.find_element(By.ID,"btnAdd").click() # klik add
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/select/option[6]").click() # select job title
        browser.find_element(By.NAME,"addJobVacancy[name]").send_keys("Senior BA") # isi vacancy name
        browser.find_element(By.NAME,"addJobVacancy[hiringManager]").send_keys("Melan Peiris") # isi hiring manager
        time.sleep(1)
        browser.find_element(By.NAME,"addJobVacancy[hiringManager]").send_keys(Keys.ENTER) # tekan enter
        browser.find_element(By.NAME,"addJobVacancy[noOfPositions]").send_keys("1") # isi number of positions
        browser.find_element(By.ID,"addJobVacancy_description").send_keys("Urgently needed") # isi deskripsi
        browser.find_element(By.ID,"btnSave").click() # klik tombol save

        # validasi
        response_data = browser.find_element(By.XPATH,"//div[@id='addJobVacancy']/div[2]/div").text
        self.assertEqual('Successfully Saved', response_data)

    def test_b_failed_add_job_vacancy_with_all_empty_fields(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu_recruitment_viewRecruitmentModule").click() # klik menu recruitment
        browser.find_element(By.ID,"menu_recruitment_viewJobVacancy").click() # klik vacancies
        browser.find_element(By.ID,"btnAdd").click() # klik add
        browser.find_element(By.ID,"btnSave").click() # klik tombol save

        # validasi
        response_job_title = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/span").text
        response_vacancy_name = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[2]/span").text
        response_hiring_manager = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[3]/span").text
            
        self.assertEqual('Required', response_job_title)
        self.assertEqual('Required', response_vacancy_name)
        self.assertEqual('Invalid', response_hiring_manager)

    def test_c_faied_add_job_vacancy_with_registered_vacancy(self): 
        # steps
        browser = self.browser 
        browser.find_element(By.ID,"menu_recruitment_viewRecruitmentModule").click() # klik menu recruitment
        browser.find_element(By.ID,"menu_recruitment_viewJobVacancy").click() # klik vacancies
        browser.find_element(By.ID,"btnAdd").click() # klik add
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[1]/select/option[6]").click() # select job title
        browser.find_element(By.NAME,"addJobVacancy[name]").send_keys("Senior BA") # isi vacancy name
        browser.find_element(By.NAME,"addJobVacancy[hiringManager]").send_keys("Melan Peiris") # isi hiring manager
        time.sleep(1)
        browser.find_element(By.NAME,"addJobVacancy[hiringManager]").send_keys(Keys.ENTER) # tekan enter
        browser.find_element(By.NAME,"addJobVacancy[noOfPositions]").send_keys("1") # isi number of positions
        browser.find_element(By.ID,"addJobVacancy_description").send_keys("test") # isi deskripsi
        browser.find_element(By.ID,"btnSave").click() # klik tombol save

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[2]/span").text
        self.assertEqual('Already exists', response_data)

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()